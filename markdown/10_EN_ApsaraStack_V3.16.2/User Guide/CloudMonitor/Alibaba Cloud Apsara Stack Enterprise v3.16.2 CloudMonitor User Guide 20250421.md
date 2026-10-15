---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor User Guide"
product_version: "V3.16.2"
doc_version: "20250421"
pdf_pages: 205
source_pdf: "5508daed61bcf25a_Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor User Guide 20250421.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%91%E6%8E%A7CMS/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20CloudMonitor%20User%20Guide%2020250421.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 CloudMonitor User Guide

## Table of Contents

- 1 CloudMonitor
- 2 Overview
- 3 Custom dashboards
- 4 Host monitoring
  - 4.1 Install the CloudMonitor agent
  - 4.2 Monitor processes
- 5 Cloud service monitoring
  - 5.1 Metrics
  - 5.2 View the monitoring data
  - 5.3 View alert rules
- 6 Kubernetes container monitoring
- 7 Alert service
  - 7.1 Alert history
  - 7.2 Alert rules
    - 7.2.1 Create an alert rule
    - 7.2.2 Manage alert rules
    - 7.2.3 Notification methods supported by CloudMonitor
  - 7.3 Alert templates
    - 7.3.1 Create an alert template
    - 7.3.2 Manage alert templates
  - 7.4 Use the initiative alerting feature
- 8 Statistical analysis
  - 8.1 Sort monitoring data
  - 8.2 Data subscription
- 9 Event monitoring
  - 9.1 System events
    - 9.1.1 System events of cloud services
    - 9.1.2 View system events
    - 9.1.3 Create a system event-triggered alert rule
    - 9.1.4 Manage system event-triggered alert rules
- 10 Application group
  - 10.1 Create an application group
  - 10.2 Manage application groups
  - 10.3 Availability monitoring
    - 10.3.1 Create an availability monitoring task
    - 10.3.2 Manage availability monitoring tasks
    - 10.3.3 Status codes
- 11 Download a report
- 12 Namespaces
  - 12.1 Time series metrics
  - 12.2 System events
    - 12.2.1 Event monitoring metrics of cloud services
    - 12.2.2 View system event metrics
- 13 Business monitoring
  - 13.1 Monitor SLS logs
- 14 Availability monitoring

## 1 CloudMonitor

CloudMonitor provides an out-of-the-box one-stop enterprise-grade monitoring solution for you to monitor resources on Apsara Stack Enterprise Edition. CloudMonitor supports cloud service monitoring, host monitoring, alert service, statistical analysis, event monitoring, application groups, and report download. You can use CloudMonitor to collect data on monitoring metrics of various cloud services, such as Elastic Compute Service (ECS), Server Load Balancer (SLB), Object Storage Service (OSS), and Log Service. The metrics include event metrics and custom metrics. CloudMonitor helps you implement multidimensional and efficient monitoring. You can improve system service availability and reduce the operations and maintenance (O&M) costs of IT infrastructure.

## 2 Overview

**Monitoring overview**

CloudMonitor provides an overview of your cloud resources. You can monitor the resource usage and status of your cloud services. You can also receive and resolve alerts at the earliest opportunity to ensure the availability of your applications. The following sections are displayed on the **Overview** page in CloudMonitor: **Alerting Cloud products**, **Alert Rules**,
**Event-triggered Alert Rules**, **Alert History**, and **Dashboards**.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, move the pointer over**Products** and choose **Monitoring and**
**O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Overview**.
4. On the**Overview**page, click the**Monitoring overview**tab to view the monitoring
overview.

| Module | Description |
|---|---|
| Alerting Cloud products | This section displays the number of alerts from cloud services that are supported by CloudMonitor and for which alerting is enabled. You can click View Details to go to the Alarm History page to view the alert details. |

| Alert Rules | This section displays the numbers of alert rules in theA larm in progress, Insufficient data, and Normal states. Note An alert rule in the Insufficient data state may be generated in the following scenarios: The cloud service does not report data of the specified metric. The cloud service instance is deleted. The cloud service instance is missing or is not created in the Logstore of Simple Log Service. In this case, further troubleshooting is required. You can click View Details to go to the Alarm Rules page to view the details of alert rules. |
|---|---|
| Event- triggered Alert Rules | This section displays the status of system events and event-triggered alerts for cloud services. This helps you troubleshoot business exceptions in an efficient manner. You can click View Details to go to the System Events page to view the alert details. |
| Alert History | This section displays the detailed records of recent alerts from cloud services that are supported by CloudMonitor and for which alerting is enabled. You can click View Details to go to the Alarm History page to view the alert details. |
| Dashboards | CloudMonitor automatically collects the statistics of cloud service instances and alerts within the current Apsara Stack account. You can click the cloud service name to go to the corresponding monitoring page and view the monitoring chart and alert rules of each instance. To view the alert rules of the cloud service, click the icon. To view the monitoring data of the cloud service, click the icon. |

**Governance detection**

The governance detection feature analyzes the resource instance metrics and alert rules in the current resource set and organization, evaluates and diagnoses the validity of metrics and alerts, and then provides suggestions. This feature allows you to fix issues with a few clicks.
1. On the**Overview**page, click the**Governance detection**tab to view the governance
detection information.

| Module | Description |
|---|---|
| Governance detection | In the Governance detection section, you can click Detect Now or Re-detection. Note If no governance detection is performed, Detect Now is displayed. If a governance detection is performed, Re-detection is displayed. The latest detection results are also displayed. |

| Detection details | If an anomaly is detected, click View Details and Governance Guidelines to the right of the detection item. In the DETECTION DETAILS panel, you can view information, such as the detection mechanism, detection range, and governance objects. Indicator Validity Detection ECS host plug-in status check: Checks whether all plug-ins of Elastic Compute Service (ECS) instances are running. No data alarm rule detection: Checks whether no-data alert is enabled for at least one instance of a cloud service in the current resource set and organization to monitor the metric data existence for all metrics of the cloud service. No data indicator detection: Checks whether all metrics of monitored cloud services have data and the data can be queried. Alarm Validity Detection Continuous alarm rule detection: Checks whether an alert rule has been in the alerting state within the previous 24 hours. Alarm Validity Test: Checks whether the callback URL of an alert rule fails to be queried within the previous 24 hours. Invalid alarm rule detection: Checks whether cloud service resources have invalid alert rules. Cloud product alarm coverage detection: Checks whether no alert rules are configured for cloud service resources. Note By default, if the initiative alerting feature is enabled for all instances of a cloud service in the level-1 organization, all instances of the cloud service are configured with alert rules. If the alert rules of a cloud service take effect only for a specific resource set, all instances of the cloud service in the specified resource set within the current Apsara Stack account are configured with the alert rules. If at least one metric of a resource instance is configured with an alert rule, the resource instance is configured with the alert rule. |
|---|---|

## 3 Custom dashboards

You can create custom dashboards for data visualization based on your business requirements to monitor, analyze, and display key metrics. This helps you understand and manage data in an intuitive and efficient manner.

**Preset dashboards**

CloudMonitor provides preset dashboards for the following cloud services: ApsaraMQ Elasticsearch on Kubernetes Object Storage Service (OSS) Server Load Balancer (SLB) Elastic Compute Service (ECS) PolarDB-X 1.0 ApsaraDB for Redis (Cluster Architecture) ApsaraDB for Redis (Standard Master-replica or Read/write Splitting Architecture) ApsaraDB RDS for PostgreSQL (Cloud Disk) ApsaraDB RDS for PostgreSQL (Local SSD) PolarDB ApsaraDB RDS for MySQL

**Create a folder**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Custom Dashboard**.
4. On the **Custom Dashboard** page, click **Create a folder** in the upper-right corner.
5. In the **Create a folder** dialog box, enter a folder name.
6. Click **OK**.

**Modify the name of a folder**

**Important**

You cannot modify the name of a preset folder.
1. On the **Custom Dashboard** page, find the folder whose name you want to modify and click
**Edit** to the right of the folder name.
2. In the **Edit folder** dialog box, enter a new folder name.
3. Click **OK**.

**Delete a folder**

**Important**

You cannot delete a preset folder. If you delete a folder, the dashboards in the folder are also deleted. Proceed with caution.
1. On the **Custom Dashboard** page, find the folder that you want to delete and click **Delete**
to the right of the folder name.
2. In the message that appears, click **OK**.

**Create a dashboard**

**Important**

Before you create a dashboard, you must create a folder. Otherwise, the dashboard cannot be saved without a folder.
1. On the **Custom Dashboard** page, click **Create a dashboard** in the upper-right corner.
2. On the **New Board** page, add charts and row containers.

**Add a chart**

a. On the **New Board** page, click **Create a chart** and select **Create a chart**. b. On the **Create a chart** page, configure settings in the **Basic style** and **Cloud**
**Monitoring Metrics** sections.
In the **Basic style** section, configure the basic information, chart type, chart elements, coordinate axes, legends, and auxiliary markers. In the **Cloud Monitoring Metrics** section, select a cloud service, metrics, statistical method, and monitoring scope. You can add multiple metrics. c. Click **Applied to large plate** in the upper-right corner to save the chart. You can click **Cancel** in the upper-right corner to cancel the chart. You can click **Last Day** in the upper-right corner and select a time range or specify a custom time range in the dialog box that appears. After the chart is created, you can click the icon on the chart card to
**modify**, **copy**, or **delete** the chart based on your business requirements.

**Add a row container**

a. On the **New Board** page, click **Create a chart** and select **Create row container**. b. Move the pointer over the row container and click the icon to modify the name of the row container. Move the pointer over the row container and click the icon to delete the row container.
3. After the charts and row containers are added, customize the dashboard layout.
You can select **Custom layout**, **1 Display per line**, **2 in each row**, **Show 3 per line**,
**Show 4 per line**, or **Show 5 per line** from the drop-down list in the upper-right corner
of the canvas. You can drag a chart or a row container to change its position.
4. Optional. Click **Last 1 hour** in the upper-right corner of the **New Board** page and select or
specify a time range. If the time range specified for the dashboard is different from that specified for the chart, the time range specified for the dashboard prevails.
5. Optional. Click the downward arrow next to the
icon in the upper-right corner of the
**New Board** page and select a refresh interval for the dashboard from the drop-down list.
If you select off, automatic refresh is disabled for the dashboard.
6. Click **Save large plate** in the upper-right corner. In the **Save large plate** dialog box,
configure the **Board Name** and **Folder** parameters. The dashboard is created.
7. Optional. Click **Set the dashboard** in the upper-right corner of the **New Board** page. In
the Settings panel, view the basic configurations and JSON mode of the dashboard.

**Basic configuration**

In the **Basic configuration** section, you can view or modify the dashboard name and folder name, and turn on or off **Editable**. If you turn on **Editable**, you can add or delete charts or row containers, and customize the dashboard layout. If you turn off Editable, you cannot perform the preceding operations.

**JSON mode**

In JSON mode, the dashboard information is displayed in the JSON format. You can also modify the dashboard information in the JSON format and click **Preview** to preview whether the modified dashboard information meets your expectations. If the modified dashboard information meets your expectations, click **Save large plate** to save the dashboard information in the JSON format.

**Modify the content and layout of a dashboard**

**Important**

You cannot modify the content or layout of a preset dashboard.
1. On the **Custom Dashboard** page, select the folder in which you want to modify the
dashboard, find the dashboard in the folder, and then click the name of the dashboard.
2. On the dashboard details page, modify the charts, row containers, and layout of the
dashboard based on your business requirements. For more information, see the Create a dashboard section of this topic.

**Modify the name of a dashboard**

**Important**

You cannot modify the name of a preset dashboard.
1. On the **Custom Dashboard** page, find the dashboard that you want to delete and click the
icon in the **Operation** column.
2. In the **Edit dashboard** dialog box, enter a new name for the dashboard.
3. Click **OK**.

**Move one or more dashboards**

**Important**

You cannot move preset dashboards.

**Move a dashboard**

i. On the **Custom Dashboard** page, find the dashboard that you want to delete and click the icon in the **Operation** column. ii. In the **Edit dashboard** dialog box, select the folder to which you want to move the dashboard. iii. Click **OK**.

**Move multiple dashboards at a time**

i. On the **Custom Dashboard** page, select the check boxes before the names of the dashboards that you want to move. ii. In the lower-left corner of the page, click **Batch move**. iii. In the **Mobile Dashboard** dialog box, select the folder to which you want to move the dashboards. iv. Click **OK**.

**Copy a dashboard**

You can copy a dashboard to create a new dashboard.
1. On the **Custom Dashboard** page, find the dashboard that you want to delete and click the
icon in the **Operation** column.
2. In the **Copy dashboard** dialog box, enter a new dashboard name and select the folder to
which you want to copy the dashboard.
3. Click **OK**.

**Specify the default dashboard**

**Important**

You can specify only one default dashboard. After you specify a dashboard as the default dashboard, the previous default dashboard is no longer the default, and the details page of the default dashboard is automatically displayed when you access the **Custom Dashboard** page. Click the icon in the upper-left corner of the details page of the default dashboard to return to the **Custom Dashboard** page.
1. On the **Custom Dashboard** page, find the dashboard that you want to specify as the
default dashboard and click the icon in the **Operation** column.
2. In the message that appears, click **OK**. After the configuration is complete,
in the Operation column of the dashboard changes to .

**Cancel the default dashboard**

**Important**

After you cancel the default dashboard, the folders are displayed by default when you access the **Custom Dashboard** page.
1. On the **Custom Dashboard** page, find the default dashboard in a folder and click the
icon in the **Operation** column.
2. In the message that appears, click **OK**. After the default dashboard is canceled,
in the
**Operation** column of the dashboard changes to
.

**Delete one or more dashboards**

**Important**

You cannot delete preset dashboards.

**Delete a dashboard**

i. On the **Custom Dashboard** page, find the dashboard that you want to delete and click the icon in the **Operation** column. ii. In the message that appears, click **OK**.

**Delete multiple dashboards at a time**

i. On the **Custom Dashboard** page, select the check boxes before the names of the dashboards that you want to delete. ii. Click **Batch deletion** in the lower-left corner of the page. iii. In the message that appears, click **OK**.

## 4 Host monitoring

After the CloudMonitor agent is installed on your Elastic Compute Service (ECS) instances, CloudMonitor can collect various monitoring data of metrics about the operating system that the ECS instances run. You can configure alert rules for the metrics to reduce monitoring costs. The following table describes features of host monitoring.

| Feature | Description |
|---|---|
| Easy-to-use agent | After the CloudMonitor agent is installed on your ECS instances, CloudMonitor can collect various monitoring data of metrics about the operating system that the ECS instances run. For more information, see Install the CloudMonitor agent. |
| Various metrics | Host monitoring supports metrics about the CPU, memory, disks, and network to meet your basic O&M requirements. For more information about the metrics supported by CloudMonitor, see Metrics. |
| Business-specific process monitoring | Host monitoring collects the CPU utilization, memory usage, and the number of opened files for active processes. This helps you monitor the resource usage of your ECS instances. For more information, see Monitor processes. |
| Flexible alerting | Host monitoring allows you to manage ECS instances across regions and configure alert rules by application group. This reduces the costs of monitoring management. |

### 4.1 Install the CloudMonitor agent

You can install the CloudMonitor agent on Elastic Compute Service (ECS) instances to collect the monitoring data of operating systems.

**Batch install or upgrade the CloudMonitor agent**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, click **Host Monitoring**.
4. On the **Host Monitoring** page, select the ECS instances for which you want to install or
upgrade the agent and click **Bulk install or upgrade plug-ins** in the lower-left corner of the instance list. You can only install the CloudMonitor agent for ECS instances that run the **Linux** and
**Windows** operating systems.
5. In the message that appears, click **OK**.
The installation or upgrade process takes approximately five minutes. After the agent changes from the **In Installation** state to the **In operation** state, the CloudMonitor agent is installed or upgraded.

**Install or upgrade the CloudMonitor agent globally**

This operation takes effect on multiple ECS instances and can be performed every 30 minutes.
1. On the **Host Monitoring** page, click **Install/Upgrade Agent**.
2. In the **Install/Upgrade Agent** dialog box, select **Install Only for Uninstalled**, **Only**
**Upgrade for Installed** or **Install and Upgrade to Latest Version** .
**Install Only for Uninstalled**: installs the CloudMonitor agent only on the ECS
instances that are not installed with the agent.
**Only Upgrade for Installed**: upgrades the CloudMonitor agent for the ECS
instances that are installed with the agent.
**Install and Upgrade to Latest Version** : installs and upgrades the
CloudMonitor agent to the latest version for all existing ECS instances.
3. Click **Execute Now**.

**Install the CloudMonitor agent on a single ECS instance**

1. Find the ECS instance on which you want to install the CloudMonitor agent and click the
icon.
2. In the message that appears, click **OK**.
If the CloudMonitor agent fails to be installed, click the icon in the Agent Status column to view the installation failure details, including **Last Installation Failure**
**Cause**, **Installation History Details**, **Installation Status**, and **Installed Agent**
**Output**.

### 4.2 Monitor processes

CloudMonitor provides the process monitoring feature to help you collect information about the active processes of Elastic Compute Service (ECS) instances during a period of time. You can collect the following information: CPU utilization, memory usage, and the number of opened files. If you add a process keyword, you can obtain the number of processes that match the keyword.

**Prerequisites**

A CloudMonitor agent is installed on the ECS instances. For more information, see Install the CloudMonitor agent.

**Background information**

CloudMonitor identifies the top five processes with the highest CPU utilization at 1-minute intervals and records the CPU utilization, memory usage, and the number of opened files in these processes. CPU utilization and memory usage of a process: You can check the output of the **top** command in the Linux operating system to understand the two metrics. Number of opened files in a process: You can check the output of the **lsof** command in the Linux operating system to understand this metric. CloudMonitor collects the CPU utilization of only the top five CPU-intensive processes. The following issues may occur: If a process occupies multiple CPU cores, the collected CPU utilization may exceed 100%. This is because CloudMonitor collects the total CPU utilization of the process on all the occupied CPU cores. If the top five CPU-intensive processes change during the period specified in your query, the process list displays all the processes that have ranked top five over the specified period. The time displayed in the list indicates when the processes last ranked top five. CloudMonitor collects the CPU utilization, memory usage, and number of opened files for a process only when the process is among the top five CPU-intensive processes. If a process has not stayed in the top five within the period specified in your query, its monitoring data is displayed as dispersed data points in the monitoring charts. The density of the data points indicates the activity level of the process on the host. Examples: In the following figures, the data points for the wrapper process are sparse and discontinuous in the monitoring charts. This is because the wrapper process did not continuously rank top five with the highest CPU utilization during the specified period. In the following figures, the data points for the java process are dense and continuous in the monitoring charts. This is because the java process continuously ranked top five with the highest CPU utilization during the specified period.

**Add or remove system processes**

You can monitor the number of processes on ECS instances and collect the number of key processes to obtain the availability of the key processes.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Products > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Host Monitoring**.
4. On the **Host monitoring** page, find the ECS instance that you want to manage and click
the name of the ECS instance.
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

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Products > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Host Monitoring**.
4. On the Host monitoring page, click **Create alarm rules**.
5. In the **Create alarm rules** panel, click Add Rule Description. In the Add Rule Description
panel, select the **(Agent)process.count_processname** metric from the **Monitoring**
**indicators** drop-down list, and configure other parameters based on your business
requirements. If multiple processes run on the ECS instance and the number of processes that match each process keyword varies, you can go back to the Create alarm rules panel and click **Add**
**Rule Description** to configure alert rules for the processes one by one. For more
information about how to configure parameters in an alert rule, see Create an alert rule.
6. Click **Confirm**.

## 5 Cloud service monitoring

CloudMonitor automatically retrieves the resources of cloud services that belong to the current Apsara Stack account. You can view the monitoring charts of each cloud service to understand the status of resources. You can also configure alert rules to monitor resources. If an alert is triggered based on an alert rule, CloudMonitor sends an alert notification. This way, you can understand the status of your resources at the earliest opportunity. For more information about the cloud services that are supported by CloudMonitor, see Metrics.

### 5.1 Metrics

This topic describes the metrics supported by each service. CloudMonitor checks the availability of services based on their metrics. You can configure alert rules and notification policies for these metrics to monitor the status and performance of service instances. CloudMonitor can monitor the resources of other Apsara Stack services. The following tables describe the metrics supported by each service.

**Elastic Compute Service (ECS)**

**Basic metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds. The metrics described in the following table are collected from the virtual host layer and are slightly different from metrics collected in the operating system.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (ECS) CPU Utilization | % | CPUUtilization | userId and instanceId | The CPU utilization. |
| (ECS)InternetInRa te(Classic Network) | Bit/s | InternetInRate | userId and instanceId | The rate of inbound traffic over the Internet. |
| (ECS)IntranetInRa te | Bit/s | IntranetInRate | userId and instanceId | The rate of inbound traffic over the intranet. |
| (ECS)InternetOut Rate(Classic Network) | Bit/s | InternetOutRate | userId and instanceId | The rate of outbound traffic over the Internet. |

| (ECS)IntranetOut Rate | Bit/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic over the intranet. |
|---|---|---|---|---|
| (ECS)DiskReadBP S | Bytes/s | DiskReadBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS)DiskWriteBP S | Bytes/s | DiskWriteBPS | userId and instanceId | The number of bytes written to all disks per second. |
| (ECS)DiskReadIO PS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |
| (ECS)DiskWriteIO PS | Count/s | DiskWriteIOPS | userId and instanceId | The number of write IOPS of all disks. |

**Operating system-related metrics**

To collect operating system-related metrics of ECS instances, you must install a monitoring plug-in. To install a monitoring plug-in, perform the following operations: In the left-side navigation pane of the CloudMonitor console, click **Cloud Service Monitoring**. On the **Cloud product monitoring** page, click **ECS**. On the **Host monitoring** page, select the instances that you want to monitor and click **Bulk install or upgrade**
**plug-ins** below the instance list.
Metric data is displayed in the monitoring charts in 5 to 10 minutes after the monitoring plug-in is installed. Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: 15. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)cpu.total | % | cpu total _ | userId and instanceId | The CPU utilization. |

| (Agent)memory.u sed.utilization | % | memory usedutilization _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| (Agent)load.15m | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
| (Agent)load.1m | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
| (Agent)load.5m | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| Host.diskusage.ut ilization | % | diskusage utilization _ | userId, instanceId, and device | The disk usage. |
| (Agent)fs.inode.u tilization device _ | % | fs inodeutilization _ | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |

| (Agent)disk.read. bps device _ | Byte s/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
|---|---|---|---|---|
| (Agent)disk.read.i ops device _ | Coun t/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
| (Agent)disk.write. bps device _ | Byte s/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent)disk.write. iops device _ | Coun t/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent)network.t cp.connection st _ ate | Coun t | net tcpconnection _ | userId, instanceId, and state | The number of TCP connections in each state. |
| (Agent)process.e xpend pid _ | N/A | process.expend | userId, instanceId, name, and pid | The detailed statistical metrics for the top 5 processes. |
| (Agent)process.c ount processnam _ e | Coun t | process.number | userId, instanceId, and processName | The number of matched processes. |
| io saturation | % | disk io util _ _ | userId, instanceId, and device | The I/O saturation. |
| Agent(zombie pr _ ocess number) _ | Coun t | zombieProcessNumber | userId and instanceId | The total number of zombie processes. |
| Agent(total proce _ ss number) _ | Coun t | totalProcessNumber | userId and instanceId | The total number of processes. |
| Agent(swap parti _ tion usage) _ | % | swapUtilization | userId and instanceId | The usage of the swap partition. |

| Agent(networkou t drop ratio) _ _ | % | networkout drop ratio _ _ | userId, instanceId, and device | The loss rate of packets that are sent by network interface controllers (NICs). |
|---|---|---|---|---|
| Agent(networkou t error ratio) _ _ | % | networkout error ratio _ _ | userId, instanceId, and device | The sending error rate of NICs. |
| Agent(networkin _ drop ratio) _ | % | networkin drop ratio _ _ | userId, instanceId, and device | The loss rate of packets that are received by NICs. |
| Agent(networkin _ error ratio) _ | % | networkin error ratio _ _ | userId, instanceId, and device | The receiving error rate of NICs. |

**Disk-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 15. Default value: 15. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Descriptio n |
|---|---|---|---|---|
| Total Disk Space | GB | DiskSerialTotal | userId, instanceId, and id serial _ | The total capacity of disks. |
| Disk Space Used | GB | DiskSerialUsed | userId, instanceId, and id serial _ | The used disk capacity. |
| (Agent) Percentage of cloud disk usage | % | DiskSerialUsePercent | userId, instanceId, and id serial _ | The percentage of used disk capacity. |
| Free Disk Space | GB | DiskSerialFree | userId, instanceId, and id serial _ | The available disk capacity. |

**GPU-related metrics**

Set the **Namespace** parameter to **acs_ecs_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (Agent)gpu.decoder.utiliz ation gpuid _ | % | gpu decoder utilizat _ _ ion | userId, instanceId, and gpuId | The decoder usage of a GPU. |
| (Agent)gpu.encoder.utiliz ation gpuid _ | % | gpu encoder utilizat _ _ ion | userId, instanceId, and gpuId | The encoder usage of a GPU. |
| (Agent)gpu.temperature _ gpuid | °C | gpu gpu temperatur _ _ e | userId, instanceId, and gpuId | The GPU temperature. |
| (Agent)gpu.usedutilizatio n gpuid _ | % | gpu gpu usedutiliza _ _ tion | userId, instanceId, and gpuId | The GPU utilization. |
| (Agent)gpu.memory.free. space gpuid _ | Bytes | gpu memory freesp _ _ ace | userId, instanceId, and gpuId | The idle video memory of a GPU. |
| (Agent)gpu.memory.free. utilization gpuid _ | % | gpu memory freeuti _ _ lization | userId, instanceId, and gpuId | The percentage of the idle video memory of a GPU. |
| (Agent)gpu.memory.used .space gpuid _ | Bytes | gpu memory useds _ _ pace | userId, instanceId, and gpuId | The used video memory of a GPU. |
| gpu memory usedutilizat _ _ ion | % | gpu memory usedut _ _ ilization | userId, instanceId, and gpuId | The video memory usage of a GPU. |
| (Agent)gpu.power.readin gspowerdraw gpuid _ | W | gpu power readings _ _ power draw _ _ | userId, instanceId, and gpuId | The GPU power. |

**ApsaraDB RDS**

By default, an old link is used for ApsaraDB RDS. ApsaraDB RDS supports four types of engines: MySQL, SQL Server, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | MySQL NetworkI _ nNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| NetworkOutRate | Bit/s | MySQL NetworkO _ utNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS _ | userId and instanceId | The number of QPS of the ApsaraDB RDS for MySQL instance. |

| Docker Cpu Usage | % | DockerCpuUsage | userId and instanceId | The CPU usage of the database proxy. |
|---|---|---|---|---|

**ApsaraDB RDS for SQL Server**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage. |
| NetworkInRate | Bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |
| NetworkOutRate | Bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |

**ApsaraDB RDS for PolarDB**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliza tion | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilization | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUtilization | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUtilization | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsU tilization | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| DiskUtilizatio n | % | DiskUsage | userId and instanceId | The disk usage. |

| IOPSUtilizatio n | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
|---|---|---|---|---|
| MemoryUtiliz ation | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Average active connections per CPU PG cloud disk _ | Count | ActiveConnections | userId and instanceId | The average number of active connections per CPU. |
| Inode Usage PG _ Disk | % | InodeUsage | userId and instanceId | The inode usage. |
| Read-only synchronization delay PG cloud _ disk | Second s | ReadLag | userId and instanceId | The synchronization latency of the read-only instance. |
| Database Age PG _ Disk | xids | DBAge | userId and instanceId | The age of the database. |
| Read-only Stream replication state pg cloud _ disk | Value | StreamingStatus | userId and instanceId | The stream replication status of the read-only instance. |
| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| Pg disk space _ usage | % | local fs size usage _ _ _ | userId and instanceId | The disk usage. |

| PG Memory Usage _ | % | mem usage _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|

**ApsaraDB RDS (New)**

ApsaraDB RDS also supports a new link. Data is collected at 60-second intervals. ApsaraDB RDS (New) supports three engines: MySQL, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| MySQL Network inflow bandwidth (new) | Bit/s | MySQL NetworkInNew _ _ new | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |

| MySQL Network outflow bandwidth (new) | Bit/s | MySQL NetworkOutNew _ new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
|---|---|---|---|---|
| MySQL queries per second (new) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of QPS of the ApsaraDB RDS for MySQL instance. |
| DataDelay | Second s | DataDelay | userId and instanceId | The latency between primary and secondary instances. |
| RWDelay (New) | Second s | RWDelay | userId, instanceId, and slave | The read and write latency. |
| ThreadsConnected | Count | ThreadsConnected | userId and instanceId | The number of thread connections. |
| ThreadsRunning | Count | ThreadsRunning | userId and instanceId | The number of active threads. |
| SlowQueriesPs | Count | SlowQueriesPs | userId and instanceId | The number of slow queries per second. |
| Total Wait Time for Row Locks (New) | Millisec onds | InnodbRowLockTime | userId and instanceId | The total wait time for row locks. |
| Average Wait Tim for Row Locks (New) | Millisec onds | InnodbRowLockTimeAv g | userId and instanceId | The average wait time for row locks. |
| Row Lock Waits (New) | Count | InnodbRowLockWaits | userId and instanceId | The number of wait times for row locks. |
| Total Number of Connections (New) | Count | TotalConnections | userId and instanceId | The total number of connections. |

| Average number of active MySQL connections | Count | MySQL ActiveSession _ | userId and instanceId | The average number of active connections to the ApsaraDB for MySQL instance. |
|---|---|---|---|---|
| Innodb row lock cu _ _ _ rrent waits _ | Count | Innodb row lock curre _ _ _ nt waits _ | userId and instanceId | The number of sessions that are waiting for row locks. |
| mdl lock session _ _ | Count | mdl lock session _ _ | userId and instanceId | The number of connections blocked by metadata locks (MDLs). |
| lock deadlocks _ | Count | lock deadlocks _ | userId and instanceId | The number of deadlocks. |

**ApsaraDB RDS for PolarDB**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |

| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| PPAS Primary/Standby Disconnect | Count | PPAS ReplicationNum _ | userId and instanceId | The number of disconnection s between primary and secondary ApsaraDB RDS for PPAS instances. 1: The primary and secondary ApsaraDB RDS for PPAS instances are connected. 0: The primary and secondary ApsaraDB RDS for PPAS instances are disconnecte d. |
| PPAS primary/standby delay | Seconds | PPAS ReplicationLag _ | userId and instanceId | The latency between the primary and secondary ApsaraDB RDS for PPAS instances. |
| PG ActiveConnect _ ionsPerCpu | Count | PG ActiveConnections _ PerCpu | userId and instanceId | The average number of active connections per core to the PolarDB for Oracle Enterprise Edition database that uses local disks. |

| PG Database age _ | xids | PG O DBAge _ _ | userId and instanceId | The age of the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |
|---|---|---|---|---|
| PG SwellTime _ | Seconds | PG SwellTime _ | userId and instanceId | The period during which the PolarDB for Oracle Enterprise Edition database that uses local SSDs experiences storage bloat. |
| PG CheckpointLat _ encyMB | MB | PG CheckpointLatency _ MB | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay during a checkpoint process. |
| PG InactiveSlots _ | Count | PG InactiveSlots _ | userId and instanceId | The number of times that the replication slot is disconnected in the PolarDB for Oracle Enterprise Edition database that uses local SSDs. |

| PG ReplayLatency _ InMB | MB | PG ReplayLatencyInM _ B | userId and instanceId | The size of data written to the PolarDB for Oracle Enterprise Edition database that uses local SSDs with a delay. |
|---|---|---|---|---|

**ApsaraDB RDS for PostgreSQL**

Set the **Namespace** parameter to **acs_rds_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**ApsaraDB RDS for PostgreSQL instances that use local SSDs**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage ne _ w | userId and instanceId | The connection utilization. |
| CPU usage (new) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk usage (new) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS usage (new) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory usage (new) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |

| PG primary/standby disconnection | Count | PG ReplicationNum _ | userId and instanceId | The number of connections between the primary and secondary ApsaraDB RDS for PostgreSQL instances. 1: The primary and secondary ApsaraDB RDS for PostgreSQL instances are connected. 0: The primary and secondary ApsaraDB RDS for PostgreSQL instances are disconnecte d. |
|---|---|---|---|---|
| PG primary/standby delay | Seconds | PG ReplicationLag _ | userId and instanceId | The latency between the primary and secondary ApsaraDB RDS for PostgreSQL instances. |

**ApsaraDB RDS for PostgreSQL instances that use cloud disks**

| Console-based metric | Unit | API-based metric | Dimensions | Description |
|---|---|---|---|---|
| Average number of active connections per CPU PG cloud _ disk (new) | Count | ActiveConnections ne _ w | userId and instanceId | The average number of active connections per CPU. |

| Pg connection _ usage | % | conn usage _ | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| PG CPU usage _ | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| PG IOPS usage _ | % | iops usage _ | userId and instanceId | The IOPS usage. |
| INODE usage PG _ cloud disk (new) | % | InodeUsage new _ | userId and instanceId | The inode usage. |
| Pg disk space _ usage | % | local fs size usage _ _ _ | userId and instanceId | The disk usage. |
| PG Memory _ Usage | % | mem usage _ | userId and instanceId | The memory usage. |
| Read-only synchronization delay PG cloud _ disk (new) | Second s | ReadLag new _ | userId and instanceId | The synchronization latency of the read-only instance. |
| Database age PG _ cloud disk (new) | xids | DBAge new _ | userId and instanceId | The age of the database. |
| Read-only Stream Copy Status PG _ Cloud Disk (New) | Value | StreamingStatus new _ | userId and instanceId | The streaming replication status of the read-only instance. |

| Number of Primary/Secondar y Connections (Value 0 indicates disconnected. Value 1 indicates connected.) | Count | PG ESSD ReplicationN _ _ um | userId and instanceId | The number connections between the primary and secondary ApsaraDB RDS for PostgreSQL instances. 1: The primary and secondary ApsaraDB RDS for PostgreSQL instances are connected. 0: The primary and secondary ApsaraDB RDS for PostgreSQL instances are disconnected . |
|---|---|---|---|---|
| PG cloud disk primary/stan _ dby delay | Second s | PG ESSD ReplicationL _ _ ag | userId and instanceId | The latency between the primary and secondary ApsaraDB RDS for PostgreSQL instances. |

**Server Load Balancer (SLB)**

Set the **Namespace** parameter to **acs_slb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceActiveCo nnection | Count | InstanceActiveConnec tion | userId, instanceId, and protocol | The number of active TCP connections. |

| InstanceInactiveC onnection | Count | InstanceInactiveConn ection | userId, instanceId, and protocol | The number of inactive connections on the port. |
|---|---|---|---|---|
| InstanceDropCon nection | Count/s | InstanceDropConnecti on | userId, instanceId, and protocol | The number of connections dropped from the listener per second. |
| InstancecDropTra fficRX | Bit/s | InstanceDropTrafficRX | userId, instanceId, and protocol | The number of inbound bits dropped from the listener per second. |
| InstanceDropTraf ficTX | Bit/s | InstanceDropTrafficTX | userId, instanceId, and protocol | The number of outbound bits dropped from the listener per second. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketR X | userId, instanceId, and protocol | The number of inbound packets dropped per second on an instance. |
| InstanceDropPac ketRX | Count/s | InstanceDropPacketT X | userId, instanceId, and protocol | The number of outbound packets dropped per second on an instance. |
| InstanceMaxConn ection | Count/s | InstanceMaxConnecti on | userId, instanceId, and protocol | The number of concurrent connections per second on the port. |
| InstanceNewCon nection | Count | InstanceNewConnecti on | userId, instanceId, and protocol | The number of new TCP connections. |
| InstancePacketR X | Count/s | InstancePacketRX | userId, instanceId, and protocol | The number of inbound packets per second. |

| InstancePacketTX | Count/s | InstancePacketTX | userId, instanceId, and protocol | The number of outbound packets per second. |
|---|---|---|---|---|
| InternetInRate | Bit/s | InstanceTrafficRXNew | userId, instanceId, and protocol | The inbound bandwidth. |
| InternetOutRate | Bit/s | InstanceTrafficTXNew | userId, instanceId, and protocol | The outbound bandwidth. |
| HealthyServerCo unt | Count | InstanceHeathyServer Count | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
| UnhealthyServer Count | Count | InstanceUnhealthySer verCount | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Sum of inflow bandwidth | Bit/s | InstanceTrafficRXNew SUM _ | userId, instanceId, and protocol | The total inbound bandwidth. |
| Sum of outflow bandwidth | Bit/s | InstanceTrafficTXNew SUM _ | userId, instanceId, and protocol | The total outbound bandwidth. |
| Seven-layer instance Qps | Request s/s | InstanceSevenFloorQp s | userId and instanceId | The QPS at Layer 7. |
| InstanceFailConn ection | Count | InstanceFailConnectio n | userId and instanceId | The number of failed connections to the instance per second. |
| Instance Layer -7 Back-end Health Check Failure Rate | % | InstanceSeventhFloor UnhealthyServerRate | userId, instanceId, and rip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |

| QPS usage of seven-tier instances | % | InstanceSevenFloorQp sRate | userId and instanceId | The QPS usage of the instance at Layer 7. |
|---|---|---|---|---|
| Maximum instance connections usage | % | InstanceMaxConnecti onRate | userId and instanceId | The maximum connection utilization of the instance. |

**Port-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| TCPActiveConnec tion | Count | ActiveConnection | userId, instanceId, port, and protocol | The number of active TCP connections per second. |
| TCPInactiveConn ection | Count | InactiveConnecti on | userId, instanceId, port, and protocol | The number of inactive TCP connections. |
| DropConnection | Count/s | DropConnection | userId, instanceId, port, and protocol | The number of connections dropped from the listener per second. |
| DropTrafficRX | Bit/s | DropTrafficRX | userId, instanceId, port, and protocol | The number of inbound bits dropped from the listener per second. |
| DropTrafficTX | Bit/s | DropTrafficTX | userId, instanceId, port, and protocol | The number of outbound bits dropped from the listener per second. |
| DropPacketRX | Count/s | DropPacketRX | userId, instanceId, port, and protocol | The number of inbound packets that are dropped per second. |
| DropPacketTX | Count/s | DropPacketTX | userId, instanceId, port, and protocol | The number of outbound packets that are lost per second. |

| MaxConnection | Count/s | MaxConnection | userId, instanceId, port, and protocol | The number of concurrent connections to the TCP port per second. |
|---|---|---|---|---|
| TCPNewConnecti on | Count | NewConnection | userId, instanceId, port, and protocol | The number of new TCP connections. |
| PacketInPerSecon d | Count/s | PacketRX | userId, instanceId, port, and protocol | The number of inbound packets per second. |
| PacketOutPerSec ond | Count/s | PacketTX | userId, instanceId, port, and protocol | The number of outbound packets per second. |
| IntranetInRate | Bit/s | TrafficRXNew | userId, instanceId, port, and protocol | The inbound bandwidth. |
| IntranetOutRate | Bit/s | TrafficTXNew | userId, instanceId, port, and protocol | The outbound bandwidth. |
| HealthyServerCo unt | Count | HeathyServerCou nt | userId, instanceId, port, and vip | The number of normal ECS instances that are added as backend servers. |
| UnhealthyServer Count | Count | UnhealthyServer Count | userId, instanceId, port, and vip | The number of abnormal ECS instances that are added as backend servers. |
| Port inflow bandwidth sum | Bit/s | TrafficRXNew SU _ M | userId, instanceId, port, and protocol | The total inbound bandwidth. |
| Port outflow bandwidth sum | Bit/s | TrafficTXNew SU _ M | userId, instanceId, port, and protocol | The total outbound bandwidth. |

| Seven layers Qps | Requests/s | SevenFloorQps | userId, instanceId, and port | The number of queries per second at Layer 7. |
|---|---|---|---|---|
| Number of connection failures per second | Count | FailConnection | userId, instanceId, and port | The number of failed connections per second. |
| Failure rate of seven-tier back- end health check | % | SeventhFloorUnh ealthyServerRate | userId, instanceId, port, and vip | The percentage of backend ECS instances that fail to pass the health check at Layer 7. |

**Object Storage Service (OSS)**

Set the **Namespace** parameter to **acs_oss_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Overview**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| ValidRequestCou nt | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Bytes | InternetSend | userId and BucketName | The outbound traffic over the Internet. |

| InternetRecv | Bytes | InternetRecv | userId and BucketName | The inbound traffic over the Internet. |
|---|---|---|---|---|
| IntranetSend | Bytes | IntranetSend | userId and BucketName | The outbound traffic over the intranet. |
| IntranetRecv | Bytes | IntranetRecv | userId and BucketName | The inbound traffic over the intranet. |
| CdnSend | Bytes | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CdnRecv | Bytes | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Bytes | SyncSend | userId and BucketName | The outbound traffic that is generated when you use the cross-region replication feature. |
| SyncRecv | Bytes | SyncRecv | userId and BucketName | The inbound traffic that is generated when you use the cross-region replication feature. |
| MeteringStorage Utilization | Bytes | MeteringStorage Utilization | userId and BucketName | The size of the storage in use. |
| MeteringStorage UtilizationGB | GB | MeteringStorage UtilizationGB | userId and BucketName | The storage size. |
| Storage Usage | % | MeteringStorage UtilizationPercent | userId and BucketName | The storage usage. |

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

| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error indicating that resources cannot be found. |
|---|---|---|---|---|
| ClientTimeoutErr orRate | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | % | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The total number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The total number of redirect requests. |
| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirect requests. |

**Maximum latency-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum end-to-end (E2E) latency of GetObject requests. |
| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |

| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
|---|---|---|---|---|
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPostObjectE2 eLatency | Milliseconds | MaxPostObjectE2 eLatency | userId and BucketName | The maximum E2E latency of PostObject requests. |
| MaxPostObjectSe rverLatency | Milliseconds | MaxPostObjectSe rverLatency | userId and BucketName | The maximum server latency of PostObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |
| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |

| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |
|---|---|---|---|---|
| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |

**Metrics related to successful requests of different types**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| GetObjectCount | Count | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PutObjectCount | Count | PutObjectCount | userId and BucketName | The number of successful PutObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |

| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
|---|---|---|---|---|
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

**ApsaraDB for Redis (Old)**

Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConnectionsUtiliz ation | % | ConnectionUsage | userId and instanceId | The connection utilization. |
| CPU Utilization | % | CpuUsage | userId and instanceId | The CPU utilization. |
| Failed Operations | Count | FailedCount | userId and instanceId | The number of failed operations. |
| Cache Inbound Bandwidth | Bytes/s | IntranetIn | userId and instanceId | The inbound traffic over the intranet. |
| Inbound Bandwidth Usage | % | IntranetInRatio | userId and instanceId | The usage of write inbound bandwidth. |
| Cache Outbound Bandwidth | Bytes/s | IntranetOut | userId and instanceId | The outbound traffic over the intranet. |

| Outbound Bandwidth Usage | % | IntranetOutRatio | userId and instanceId | The outbound bandwidth usage. |
|---|---|---|---|---|
| MemoryUtilizatio n | % | MemoryUsage | userId and instanceId | The memory usage of the ApsaraDB for Redis instance. |
| Used QPS | Count/s | UsedQPS | userId and instanceId | The number of used QPS. |

**Tair (Redis OSS-compatible)**

Set the **Namespace** parameter to **acs_kvstore**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Standard instances and read/write splitting instances**

Standard instances and read/write splitting instances of Tair (Redis OSS-compatible) share a set of metrics.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Standard Edition) | % | StandardConnec tionUsage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Standard Edition) | Kbit/s | StandardIntranet In | userId and instanceId | The inbound bandwidth. |
| Incoming Bandwidth Utilization (Standard Edition) | % | StandardIntranet InRatio | userId and instanceId | The inbound bandwidth usage. |

| Outgoing Bandwidth (Standard Edition) | Kbit/s | StandardIntranet Out | userId and instanceId | The outbound bandwidth. |
|---|---|---|---|---|
| Outgoing Bandwidth Usage (Standard Edition) | % | StandardIntranet OutRatio | userId and instanceId | The outbound bandwidth usage. |
| Memory Usage (Standard Edition) | % | StandardMemory Usage | userId and instanceId | The memory usage. |
| QPS usage (standard edition) | % | StandardQPSUsa ge | userId and instanceId | The QPS usage. |
| CPU usage (standard edition) | % | StandardCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average Visits Per Second (Standard Edition) | Count/s | StandardUsedQP S | userId and instanceId | The average QPS. |
| Total QPS (Standard Edition) | Count/s | StandardTotalQp s | userId and instanceId | The total QPS. |
| Current Total Connections (Standard Edition) | Count | StandardTotalCo nnections | userId and instanceId | The total number of connections. |
| Used Connection | Count | StandardUsedCo nnection | userId and instanceId | The number of active connections. |
| Average Response Time (Standard Edition) | Milliseconds | StandardAvgRt | userId and instanceId | The average response time. |
| Data Node Hit Ratio (Standard Edition) | % | StandardHitRate | userId and instanceId | The hit rate. |

**Cluster instances**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (Cluster Edition) | % | ShardingConnecti onUsage | userId and instanceId | The connection utilization. |
| Incoming Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranetI n | userId and instanceId | The inbound bandwidth. |
| Outgoing Bandwidth (Cluster Edition) | Kbit/s | ShardingIntranet Out | userId and instanceId | The outbound bandwidth. |
| Incoming Bandwidth Usage (Cluster Edition) | % | ShardingIntranetI nRatio | userId and instanceId | The inbound bandwidth usage. |
| Outgoing Bandwidth Usage (Cluster Edition) | % | ShardingIntranet OutRatio | userId and instanceId | The outbound bandwidth usage. |
| Memory Usage (Cluster Edition) | % | ShardingMemory Usage | userId and instanceId | The memory usage. |
| QPS usage (cluster version) | % | ShardingQPSUsa ge | userId and instanceId | The QPS usage. |
| CPU usage (Cluster Edition) | % | ShardingCpuUsa ge | userId and instanceId | The CPU utilization. |
| Average visits per second (cluster version) | Count/s | ShardingUsedQP S | userId and instanceId | The average QPS. |
| Total QPS (cluster version) | Count/s | ShardingTotalQp s | userId and instanceId | The total QPS. |
| Total Current Connections (Cluster Edition) | Count | ShardingTotalCo nnections | userId and instanceId | The total number of connections. |
| Used Connection | Count | ShardingUsedCo nnection | userId and instanceId | The number of active connections. |

| Average Response Time (Cluster Edition) | Millisec onds | ShardingAvgRt | userId and instanceId | The average response time. |
|---|---|---|---|---|
| Data Node Hit Ratio (Cluster Edition) | % | ShardingHitRate | userId and instanceId | The hit rate. |

**Cluster instances - Node**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Connections Usage (Node) | % | NodeConnection Usage | userId, instanceId, and nodeId | The connection utilization. |
| Incoming Bandwidth (Node) | Kbit/s | NodeIntranetIn | userId, instanceId, and nodeId | The inbound bandwidth. |
| Outgoing Bandwidth (Node) | Kbit/s | NodeIntranetOut | userId, instanceId, and nodeId | The outbound bandwidth. |
| Incoming Bandwidth Utilization (Node) | % | NodeIntranetInR atio | userId, instanceId, and nodeId | The inbound bandwidth usage. |
| Outgoing Bandwidth Utilization (Node) | % | NodeIntranetOut Ratio | userId, instanceId, and nodeId | The outbound bandwidth usage. |
| Memory Usage (Node) | % | NodeMemoryUs age | userId, instanceId, and nodeId | The memory usage. |
| QPS usage (node) | % | NodeQPSUsage | userId, instanceId, and nodeId | The QPS usage. |
| CPU usage (node) | % | NodeCpuUsage | userId, instanceId, and nodeId | The CPU utilization. |

| Average Visits Per Second (Node) | Count/s | NodeUsedQPS | userId, instanceId, and nodeId | The average QPS. |
|---|---|---|---|---|
| Total QPS (nodes) | Count/s | NodeTotalQps | userId, instanceId, and nodeId | The total QPS. |
| Total Current Connections (Nodes) | Count | NodeTotalConne ctions | userId, instanceId, and nodeId | The total number of connections. |
| Used Connection | Count | NodeUsedConne ction | userId, instanceId, and nodeId | The number of active connections. |
| Average response time | Millisecond s | NodeAvgRt | userId and instanceId | The average response time. |
| Hit rate | % | NodeHitRate | userId and instanceId | The hit rate. |

**ApsaraDB for MongoDB (Old)**

Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Basic metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU Utilization | % | CPUUtilization | userId, instanceId, and role | The CPU utilization. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |
| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The disk usage. |

| IOPS Usage | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |
|---|---|---|---|---|
| Connection Usage | % | ConnectionUtiliza tion | userId, instanceId, and role | The connection utilization. |
| QPS | Count | QPS | userId, instanceId, and role | The number of requests per second. |
| UsedConnections | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| InstanceUsedDisk Space | Bytes | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |
| LogUsedDiskSpac e | Bytes | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
| Disk Space Occupied by Logs | Bytes | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network request-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IntranetIn | Bytes | IntranetIn | userId, instanceId, and role | The inbound traffic over the intranet. |
| IntranetOut | Bytes | IntranetOut | userId, instanceId, and role | The outbound traffic over the intranet. |

| Requests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |
|---|---|---|---|---|

**Operation count-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| OpCounters for Command | Count | OpCommand | userId, instanceId, and role | The number of Command operations. |
| OpCounters for Delete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
| OpCounters for Getmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpCounters for Insert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |
| OpCounters for Query | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
| OpCounters for Update | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

**ApsaraDB for MongoDB (New)**

Set the **Namespace** parameter to **acs_mongodb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Basic metrics**

| 7 |   |   | > Documen | t Version: 2025042 |
|---|---|---|---|---|

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPUUtilization ne _ w | % | CPUUtilization ne _ w | userId, instanceId, and role | The CPU utilization. |
| Memory usage (new) | % | MemoryUtilizatio n new _ | userId, instanceId, and role | The memory usage. |
| Disk Usage (New) | % | DiskUtilization n _ ew | userId, instanceId, and role | The disk usage. |
| IOPS usage (new) | % | IOPSUtilization n _ ew | userId, instanceId, and role | The IOPS usage. |
| Connection Usage (New) | % | ConnectionUtiliza tion new _ | userId, instanceId, and role | The connection utilization. |
| Visits per second (new) | Count | QPS new _ | userId, instanceId, and role | The number of requests per second. |
| Connection Usage (New) | Count | ConnectionAmou nt new _ | userId, instanceId, and role | The number of used connections. |
| Current Total Connections (New) | Count | TotalConnections | userId, instanceId, and role | The total number of connections. |

**Disk capacity-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| The amount of disk space occupied by the instance (new) | Bytes | InstanceDiskAmo unt new _ | userId, instanceId, and role | The disk space occupied by the instance. |

| Amount of disk space occupied by data (new) | Bytes | DataDiskAmount new _ | userId, instanceId, and role | The disk space occupied by data. |
|---|---|---|---|---|
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
| Number of Delete operations (new) | Count | OpDelete new _ | userId, instanceId, and role | The number of Delete operations. |
| Number of Getmore operations (new) | Count | OpGetmore new _ | userId, instanceId, and role | The number of Getmore operations. |

| Number of Insert operations (new) | Count | OpInsert new _ | userId, instanceId, and role | The number of Insert operations. |
|---|---|---|---|---|
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
| (Cluster Edition) Total Number of Connections | Count | TotalConnections _ cluster | userId, instanceId, and role | The total number of connections. |

**Disk capacity related metrics (Cluster Edition)**

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
|---|---|---|---|---|
| (Cluster version) Insert operations | Count | OpInsert new _ cluster _ | userId, instanceId, and role | The number of Insert operations. |
| (Cluster Version) Query Operation Times | Count | OpQuery new _ cluster _ | userId, instanceId, and role | The number of Query operations. |
| (Cluster Edition) Update Operation Times | Count | OpUpdate ne _ w cluster _ | userId, instanceId, and role | The number of Update operations. |

**AnalyticDB for PostgreSQL**

Set the **Namespace** parameter to **acs_hybriddb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Computing and storage-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Computing and Storage Integration] Connection Usage | % | ConnectionUsage | userId, instanceId, and role | The connection utilization. |
| [Integration of Computing and Storage] CpuUsage | % | CpuUsage | userId, instanceId, and role | The CPU utilization. |
| [Computing and Storage Integration] DiskUsage | % | DiskUsage | userId, instanceId, and role | The disk usage. |
| [Integration of computing and storage] IOPSUsage | % | IOPSUsage | userId, instanceId, and role | The IOPS utilization. |
| [Computing and Storage Integration] MemoryUsage | % | MemoryUsage | userId, instanceId, and role | The memory usage. |

**Storage reservation-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| adbpg master cn _ _ t unhealth _ | Count | adbpg master cn _ _ t unhealth _ | instanceId, instance compon _ ent, and hostname | The number of abnormal coordinator nodes. |
| adbpg segment _ _ cnt unhealth _ | Count | adbpg segment _ _ cnt unhealth _ | instanceId, instance compon _ ent, and hostname | The number of abnormal compute nodes. |
| adbpg instance _ _ disk used mb _ _ | MB | adbpg instance _ _ disk used mb _ _ | instanceId, instance compon _ ent, and hostname | The amount of used disk space. |
| adbpg instance _ _ disk usage perce _ _ nt | % | adbpg instance _ _ disk usage perce _ _ nt | instanceId, instance compon _ ent, and hostname | The disk usage. |
| Storage Reservation Instance Active Connections | Count | adbpg conn acti _ _ ve | instanceId, instance compon _ ent, and hostname | The number of active connections on the instance. |
| adbpg conn idle _ _ | Count | adbpg conn idle _ _ | instanceId, instance compon _ ent, and hostname | The number of idle connections on the instance. |
| adbpg conn cou _ _ nt | Count | adbpg conn cou _ _ nt | instanceId, instance compon _ ent, and hostname | The number of connections of the coordinator node. |
| adbpg query blo _ _ cked | Count | adbpg query blo _ _ cked | instanceId, instance compon _ ent, and hostname | The number of blocked queries on the instance. |

| adbpg query que _ _ ued | Count | adbpg query qu _ _ eued | instanceId, instance compon _ ent, and hostname | The number of queued queries on the AnalyticDB for PostgreSQL instance. |
|---|---|---|---|---|
| [Storage Reservation] Number of active queries on the master node instance (new) | Count | adbpg query acti _ _ ve | instanceId, instance compon _ ent, and hostname | The number of active queries on the AnalyticDB for PostgreSQL instance. |
| [Storage Reservation] Number of nodes (new) whose master node coordinates the node out of sync | Count | adbpg master cn _ _ t repl not sync _ _ _ | instanceId, instance compon _ ent, and hostname | The number of coordinator nodes that are in the out-of-sync state. |
| [Storage Reservation] Number of nodes that coordinates nodes that are out of sync | Count | adbpg segment _ _ cnt repl not syn _ _ _ c | instanceId, instance compon _ ent, and hostname | The number of compute nodes that are in the out-of-sync state. |
| node cpu used p _ _ _ ercent | % | node cpu used p _ _ _ ercent | instanceId, instance compon _ ent, and hostname | The CPU utilization of the node. |
| node mem used _ _ _ percent | % | node mem used _ _ percent _ | instanceId, instance compon _ ent, and hostname | The memory usage of the node. |
| node disk iops _ _ | Count | node disk iops _ _ | instanceId, instance compon _ ent, and hostname | The IOPS of the node. |
| [Storage Reservation] Node Disk Usage | MB | node disk used _ _ _ mb | instanceId, instance compon _ ent, and hostname | The used disk space of the node. |
| node disk used _ _ _ percent | % | node disk used _ _ _ percent | instanceId, instance compon _ ent, and hostname | The disk usage of the node. |

**AnalyticDB for PostgreSQL (New)**

Set the **Namespace** parameter to **acs_hybriddb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Computing and storage integration metrics (primary node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Computing and Storage Integration] Primary Node Connection Number Usage (New) | % | ConnectionUsageM aster | userId, instanceId, and role | The usage of primary node connections. |
| [Integration of computing and storage] master node CPU usage (new) | % | CpuUsageMaster | userId, instanceId, and role | The CPU utilization of the primary node. |
| [Computing and Storage Integration] Primary Node Disk Usage (New) | % | DiskUsageMaster | userId, instanceId, and role | The disk usage of the primary node. |
| [Integration of computing and storage] master node IO throughput usage (new) | % | IOPSUsageMaster | userId, instanceId, and role | The IOPS usage of the primary node. |
| [Computing and Storage Integration] Master Node Memory Usage (New) | % | MemoryUsageMast er | userId, instanceId, and role | The memory usage of the primary node. |

**Storage reservation-related metrics (primary node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| [Storage Reservation] Number of Master Node Coordination Node Connections (New) | Coun t | adbpg conn coun _ _ t master _ | instance id, _ instance componen _ t, and hostname | The number of coordinator node connections. |
|---|---|---|---|---|
| [Storage Reservation] CPU usage of the master node (new) | % | node cpu used p _ _ _ ercent master _ | instance id, _ instance componen _ t, and hostname | The CPU utilization of the primary node. |
| [Storage Reservation] Primary Node Memory Usage (New) | % | node mem used _ _ _ percent master _ | instance id, _ instance componen _ t, and hostname | The memory usage of the primary node. |
| [Storage Reservation] Number of abnormal master node coordination nodes (new) | Coun t | adbpg master cn _ _ t unhealth maste _ _ r | instance id _ | The number of abnormal coordinator nodes of the primary node. |
| [Storage Reservation] The number of nodes (new) whose master node coordinates the node out of sync. | Coun t | adbpg master cn _ _ t repl not sync _ _ _ _ master | instance id _ | The number of primary nodes that are not synchronized to coordinator nodes. |
| [Storage Reservation] Number of Queued Queries of Primary Node Instances (New) | Coun t | adbpg query que _ _ ued master _ | instance id _ | The number of queued queries on the primary node instance. |
| [Reserved storage] Number of active connections of the primary node instance (new) | Coun t | adbpg conn activ _ _ e master _ | instance id _ | The number of active connections to the primary node instance. |
| [Storage Reservation] Number of active queries on the master node instance (new) | Coun t | adbpg query acti _ _ ve master _ | instance id _ | The number of active queries on the primary node instance. |
| [Storage Reservation] Number of idle connections of the master node instance (new) | Coun t | adbpg conn idle _ _ _ master | instance id _ | The number of idle connections of the primary node instance. |

**Computing and storage integration metrics (compute group**

**node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Integration of computing and storage] CPU usage of computing group nodes (new) | % | CpuUsageSegment | userId, instanceId, and role | The CPU utilization of the nodes in the compute group. |
| [Computing and Storage Integration] Computing Group Node Disk Usage (New) | % | DiskUsageSegment | userId, instanceId, and role | The disk usage of the nodes in the compute group. |
| [Integration of computing and storage] I/O throughput usage of computing group nodes (new) | % | IOPSUsageSegmen t | userId, instanceId, and role | The IOPS usage of the nodes in the compute group. |
| [Computing and Storage Integration] Computing Group Node Memory Usage (New) | % | MemoryUsageSeg ment | userId, instanceId, and role | The memory usage of the nodes in the compute group. |

**Storage reservation-related metrics (compute group node)**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| [Storage Reservation] CPU usage of Compute Group Node (New) | % | node cpu used per _ _ _ cent segment _ | instance id, _ instance compon _ ent, and hostname | The CPU utilization of nodes in the compute group. |
| [Storage reservation] Memory Usage of Compute Group Node (New) | % | node mem used pe _ _ _ rcent segment _ | instance id, _ instance compon _ ent, and hostname | The memory usage of nodes in the compute group. |
| [Storage Reservation] Compute group node disk usage (new) | % | node disk used per _ _ _ cent segment _ | instance id, _ instance compon _ ent, and hostname | The disk usage of nodes in the compute group. |

| [Storage Reservation] Calculate the disk usage of the group node instance (new) | % | adbpg instance dis _ _ k usage percent se _ _ _ gment | instance id _ | The disk usage of node instances in the compute group. |
|---|---|---|---|---|
| [Reserved Storage] Local Data Read IOPS | Count /s | node disk iops rea _ _ _ d segment _ | instance id _ | The read IOPS of nodes in the compute group. |
| [Reserved Storage] Local Data Write IOPS | Count /s | node disk iops writ _ _ _ e segment _ | instance id _ | The write IOPS of nodes in the compute group. |
| [Reserved Storage] Local Data File Size | MB | adbpg local data di _ _ _ r size segment _ _ | instance id _ | The size of files in the nodes in the compute group. |

**VPN Gateway**

Set the **Namespace** parameter to **acs_vpn**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| IPSec.connection. rxPkgs | Packets/s | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate at which packets are received over the IPsec-VPN connection. |
| IPSec.connection. txpkgs | Packets/s | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate at which packets are sent over the IPsec- VPN connection. |
| IPSec.connection. rx.rate | Bit/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits of the connection per second. |

| IPSec.connection. tx.rate | Bit/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits of the connection per second. |
|---|---|---|---|---|
| SSL Client Count | Count | ssl client.count _ | userId, instanceId, and ipsecId | The number of connections. |

**AnalyticDB for MySQL V3.0**

Set the **Namespace** parameter to **acs_adb**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connections | Count | connections | userId and instanceId | The rate of inbound packets of the connection. |
| Average CPU usage of nodes | % | worker avg cpu _ _ _ used | userId and instanceId | The CPU utilization of the node. |
| Query the average CPU usage of a computing node | % | executor avg cp _ _ u used _ | userId and instanceId | The CPU utilization of a compute node. |
| (Reserved Mode) Maximum Node Disk Usage | % | worker max nod _ _ e disk used perc _ _ _ ent | userId and instanceId | The maximum disk usage of the node in reserved mode. |
| Disk usage | % | disk used percen _ _ t | userId and instanceId | The disk usage in reserved mode. |
| (Elastic Mode) Maximum Node Disk Usage | MB | worker max nod _ _ e disk used MB _ _ _ | userId and instanceId | The maximum used disk space of the node in elastic mode. |

| (Elastic Mode) Disk Cold Data Usage | MB | ColdDataDiskUsa ge | userId and instanceId | The used disk space for cold data in elastic mode. |
|---|---|---|---|---|
| (Elastic Mode) Disk Hot Data Usage | MB | HotDataDiskUsag e | userId and instanceId | The used disk space for hot data in elastic mode. |
| Average disk reads | MB | worker avg read _ _ bytes _ | userId and instanceId | The read throughput of the read-write node. |
| Average disk writes | MB | worker avg write _ _ bytes _ | userId and instanceId | The write throughput of the storage node. |
| Query the read throughput of compute nodes | MB | executor avg re _ _ ad bytes MB _ _ | userId and instanceId | The read throughput of the compute node. |
| Query compute node write throughput | MB | executor avg wri _ _ te bytes MB _ _ | userId and instanceId | The write throughput of the compute node. |
| Disk read throughput | Count/s | worker avg read _ _ iops _ | userId and instanceId | The read IOPS of the read-write node. |
| Disk write throughput | Count/s | worker avg write _ _ iops _ | userId and instanceId | The write IOPS of the read-write node. |
| Query compute node read IOPS | Count/s | executor avg re _ _ ad iops _ | userId and instanceId | The read IOPS of the compute node. |
| Query compute node write IOPS | Count/s | executor avg wri _ _ te iops _ | userId and instanceId | The write IOPS of the compute node. |
| Disk IO usage | % | worker avg io ut _ _ _ il | userId and instanceId | The disk I/O usage. |
| QPS | Count/s | qps | userId and instanceId | The number of QPS. |

| Average query time | Milliseconds | query avg rt _ _ | userId and instanceId | The average query time. |
|---|---|---|---|---|
| Maximum query time | Milliseconds | query max rt _ _ | userId and instanceId | The maximum query time. |
| Total query average waiting time | Milliseconds | query total wait _ _ _ time | userId and instanceId | The average query waiting time. |
| TPS | Count/s | tps | userId and instanceId | The number of transactions per second (TPS). |
| Average write response time | Milliseconds | insert avg rt _ _ | userId and instanceId | The average write response time. |
| Maximum write response time | Milliseconds | insert max rt _ _ | userId and instanceId | The maximum write response time. |
| Write throughput | MB | insert in bytes _ _ | userId and instanceId | The write throughput. |

**PolarDB-X 1.0**

Set the **Namespace** parameter to **acs_polarx_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | useId and InstanceId | The CPU utilization. |
| Memory Usage | % | MemoryUtilization | useId and InstanceId | The memory usage. |
| Network input | Bytes/ s | NetworkInputTraffi c | useId and InstanceId | The inbound traffic. |

| Network output | Bytes/ s | NetworkOutputTraf fic | useId and InstanceId | The outbound traffic. |
|---|---|---|---|---|
| Average number of logical requests per second | Count | LogicQPS | useId and InstanceId | The average number of logical requests per second. |
| Average Logical Response Time | Millise conds | LogicRT | useId and InstanceId | The average response time of logical requests. |
| Average number of physical requests per second | Count | PhysicsQPS | useId and InstanceId | The average number of physical requests per second. |
| Average Physical Response Time | Millise conds | PhysicsRT | useId and InstanceId | The average response time of physical requests. |
| Number of connections | Count | ConnectionCount | useId and InstanceId | The total number of sessions. |
| Number of active sessions | Count | ThreadCount | useId and InstanceId | The number of active sessions. |
| Average Logical Errors per Second | Count | LogicErrorCount | useId and InstanceId | The average number of logical errors per second. |

**PolarDB-X 2.0**

**Compute node-related metrics**

Set the **Namespace** parameter to **acs_drds**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU usage | % | CPUUtilization | userId and instanceId | The CPU utilization. |

| Number of connections | Count | ConnectionCount | userId and instanceId | The total number of sessions. |
|---|---|---|---|---|
| Average number of logical requests per second | Count | LogicQPS | userId and instanceId | The number of requests per second. |
| Average Logical Response Time | Millis econ ds | LogicRT | userId and instanceId | The average response time of logical requests. |
| Memory Usage | % | MemoryUtilization | userId and instanceId | The memory usage. |
| Network input | Bit/s | NetworkInputTraffic | userId and instanceId | The inbound bandwidth. |
| Network output | Bit/s | NetworkOutputTraffic | userId and instanceId | The outbound bandwidth. |
| Average number of physical requests per second | Count | PhysicsQPS | userId and instanceId | The physical QPS. |
| Average Physical Response Time | Millis econ ds | PhysicsRT | userId and instanceId | The physical response time. |
| Number of active sessions | Count | ThreadCount | userId and instanceId | The number of active threads. |
| Heap memory usage | % | HeapMemoryUsage | userId and instanceId | The heap memory usage. |
| Log directory size | Bytes | LogSize | userId and instanceId | The size of the log directory. |
| Number of errors per second | Count | SecondErrorCount | userId and instanceId | The number of errors per second. |
| Physical slow SQL per second | Count | SecondPhysicalSqlCoun t | userId and instanceId | The number of physical slow SQL queries per second. |

| Slow requests per second | Count | SecondRequestCount | userId and instanceId | The number of slow QPS. |
|---|---|---|---|---|
| spill directory size | Bytes | SpillSize | userId and instanceId | The size of the spill directory. |
| Temporary directory size | Bytes | TmpSize | userId and instanceId | The size of the temporary directory. |

**Data node-related metrics**

The **Namespace** parameter to **acs_polarxsn_dashboard**. Set the **Period** parameter to an integer multiple of a value in the range of 60 to 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Connection Usage (New) | % | ConnectionUsage new _ | userId and instanceId | The connection utilization. |
| CPU Utilization (New) | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| Disk Usage (New) | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPS Usage (New) | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| Memory Utilization (New) | % | MemoryUsage new _ | userId and instanceId | The memory usage. |
| Inbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkInNew _ new _ | userId and instanceId | The inbound traffic to the MySQL data node per second. |

| Outbound Bandwidth of an ApsaraDB RDS for MySQL Instance (New) | Bit/s | MySQL NetworkOutNe _ w new _ | userId and instanceId | The outbound traffic from the MySQL data node per second. |
|---|---|---|---|---|
| QPS of an ApsaraDB RDS for MySQL Instance (New) | Count/ s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second on the MySQL data node. |

**Elastic IP Address (EIP)**

Set the **Namespace** parameter to **acs_vpc_eip**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| net rx.rate _ | Bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
| net rxPkgs.rate _ | Count/s | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | Bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |
| net txPkgs.rate _ | Count/s | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
| Out Ratelimit Drop Speed | Packets/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The outbound packet loss rate. |
| In Ratelimit Drop Speed | Packets/s | in ratelimit drop _ _ speed _ | userId and instanceId | The inbound packet loss rate. |

**API Gateway**

Set the **Namespace** parameter to **acs_apigateway_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Latency | Milliseconds | Latency | userId, region, and apiUid | The response time. |
| SumQPS | Count | SumQPS | userId, region, and apiUid | The total QPS. |
| TrafficRX | KB | TrafficRX | userId, region, and apiUid | The inbound traffic. |
| TrafficTX | KB | TrafficTX | userId, region, and apiUid | The outbound traffic. |
| code2XX Number | Count | code2XX | userId, region, and apiUid | The number of times that a 2XX HTTP status code is returned. |
| code4XX Number | Count | code4XX | userId, region, and apiUid | The number of times that a 4XX HTTP status code is returned. |
| code5XX Number | Count | code5XX | userId, region, and apiUid | The number of times that a 5XX HTTP status code is returned. |

**Hologres**

Set the **Namespace** parameter to **acs_hologres**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Connections Used | Count | connection num _ | userId and instanceId | The number of SQL connections. |
| Connection Usage | % | connection usag _ e | userId and instanceId | The connection utilization of an instance. |
| Export QPS | Count/s | record output qp _ _ s | userId and instanceId | The QPS. |
| Micro batch size | Count/s | scan batchsize _ | userId and instanceId | The size of the micro batch. |
| CPU Utilization | % | cpu usage _ | userId and instanceId | The CPU utilization. |
| memory usage | % | memory usage _ | userId and instanceId | The memory usage. |
| storage usage _ | Bytes | storage usage _ | userId and instanceId | The used storage. |
| I/O Write Throughput | Bytes/s | io write through _ _ put | userId and instanceId | The write I/O throughput per second. |
| I/O Read Throughput | Bytes/s | io read throughp _ _ ut | userId and instanceId | The read I/O throughput per second. |

**Status-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Failed Query Qps | Count/s | failed query qps _ _ | userId and instanceId | The number of failed QPS. |

| Query Latency Detail | Milliseconds | query latency _ | instanceId, userId, and cmdType | The latency of the query. |
|---|---|---|---|---|
| Query QPS Detail | Count/s | query qps _ | instanceId, userId, and cmdType | The detailed QPS data. |

**Tablestore**

Set the **Namespace** parameter to **acs_ots_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

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
|---|---|---|---|---|
| Total Request | Count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| 2xx Request | Count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests for which a 2XX HTTP status code is returned. |
| 429 Request | Count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests for which the HTTP status code 429 is returned. |
| 4xx Request | Count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests for which a 4XX HTTP status code is returned. |
| 5xx Request | Count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests for which a 5XX HTTP status code is returned. |
| Internet Inbound | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic over the Internet. |
| Internet Outbound | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic over the Internet. |
| Free Outbound Internet | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The free outbound traffic over the Internet. |
| Total Rows | Count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| Failed Rows | Count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |

**NAT Gateway**

Set the **Namespace** parameter to **acs_nat_gateway**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total number of sessions | Count/s | curr num _ | userId and instanceId | The total number of sessions. |
| Capacity Discard Connections (Cumulative Value) | Count | capacity drop _ | userId and instanceId | The number of capacity-dropped connections. |
| Number of new discarded connections (cumulative value) | Count | ratelimit drop _ | userId and instanceId | The number of new dropped connections. |
| Capacity Discard Connections Per Second | Count/s | capacity drop in _ _ c | userId and instanceId | The number of capacity-dropped connections per second. |
| Number of new and discarded connections per second | Count/s | ratelimit drop in _ _ c | userId and instanceId | The number of new dropped connections per second. |
| Number of new connections per second | Count/s | establish rate _ | userId and instanceId | The number of new connections per second. |

**Elasticsearch on Kubernetes**

Set the **Namespace** parameter to **acs_elasticsearch**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ClusterStatus | Value | ClusterStatus | userId and instanceId | The status of the cluster. Valid values: 0: green, which indicates normal. 1: yellow, which indicates warning. 2: red, which indicates exception. |
| Number of tasks waiting to be executed | Count | PendingTaskCou nt | userId and instanceId | The number of tasks that are waiting to be executed. |
| The maximum waiting time for a task to be executed | Milliseconds | PendingTaskMax WaitTime | userId and instanceId | The maximum waiting time for a task to be executed. |
| Number of data nodes | Count | DataNodes | userId and instanceId | The number of data nodes. |
| Active Shards | Count | ActiveShards | userId and instanceId | The number of active shards. |
| Unallocated Shards | Count | UnassingnedShar dsShards | userId and instanceId | The number of unallocated shards. |

**Node-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Node CPU usage | % | NodeCPUUtil | userId, instanceId, and nodeName | The CPU utilization of the node. |

| Node disk usage | % | NodeDiskUtil | userId, instanceId, and nodeName | The disk usage of the node. |
|---|---|---|---|---|
| NodeHeapMemor yUtilization | % | NodeHeapMemor yUtil | userId, instanceId, and nodeName | The heap memory usage of the node. |
| Node cpu 1min load | Value | NodeLoad1 | userId, instanceId, and nodeName | The average load of the node over the last 1 minute. |
| Node cpu 5min load | Value | NodeLoad5 | userId, instanceId, and nodeName | The average load within 5 minutes of the node. |
| Node cpu 15min load | Value | NodeLoad15 | userId, instanceId, and nodeName | The average load within 15 minutes of the node. |
| Node OldGC times-Cumulative Value | Count | OldGCTotalCount | userId, instanceId, and nodeName | The total number of times that garbage collection (GC) is performed in the old generation space of the node. |
| Node OldGC Time- Accumulation Value | Milliseconds | OldGCTotalTime | userId, instanceId, and nodeName | The total amount of time consumed by GC in the old generation space of the node. |
| Node OldGC average time consumption | Milliseconds | OldGCCostTime | userId, instanceId, and nodeName | The average amount of time consumed by GC in the old generation space of the node. |
| Node OldGC rate | Count/s | OldGCRate | userId, instanceId, and nodeName | The rate of GC in the old generation space of the node. |

| Node YoungGC times-Cumulative Value | Count | YoungGCTotalCo unt | userId, instanceId, and nodeName | The total number of times that GC is performed in the young generation space of the node. |
|---|---|---|---|---|
| Node YoungGC Time- Accumulation Value | Count | YoungGCTotalTi me | userId, instanceId, and nodeName | The total amount of time consumed by GC in the young generation space of the node. |
| Average Node YoungGC Time Consumption (MS) | Milliseconds | YoungGCCostTim e | userId, instanceId, and nodeName | The average amount of time consumed by GC in the young generation space of the node. |
| Node YoungGC rate | Count/s | YoungGCRate | userId, instanceId, and nodeName | The rate of GC in the young generation space of the node. |
| Node Free Disk Space | GB | AvailableDiskSize | userId, instanceId, and nodeName | The available disk space of the node. |
| Node heap memory usage | GB | NodeHeapMemor y | userId, instanceId, and nodeName | The heap memory usage of the node. |
| Number of node documents | Count | NodeDocumentC ount | userId, instanceId, and nodeName | The number of node documents. |
| Number of node segments | Count | NodeSegmentCo unt | userId, instanceId, and nodeName | The number of node segments. |
| Disk IO Rate | Count/s | NodeDiskIOOper ationsRate | userId, instanceId, and nodeName | The disk I/O rate. |
| Disk write rate | Count/s | NodeWriteIOOper ationsRate | userId, instanceId, and nodeName | The disk write rate. |

| Disk read rate | Count/s | NodeReadIOOper ationsRate | userId, instanceId, and nodeName | The disk read rate. |
|---|---|---|---|---|
| Number of threads | Count | IndexThread | userId, instanceId, and nodeName | The number of threads. |
| Query thread | Count | WriteThread | userId, instanceId, and nodeName | The number of query threads. |
| Node data size | MB | NodeData | userId, instanceId, and nodeName | The size of the data disk of the node. |
| Various memory usage of nodes | KB | NodeIndexMemor yLucene | userId, instanceId, and nodeName | The various memory usage of the node. |
| Node terms memory usage | KB | NodeIndexMemor yTerms | userId, instanceId, and nodeName | The terms memory usage of the node. |
| Node points memory usage | KB | NodeIndexMemor yPoints | userId, instanceId, and nodeName | The points memory usage of the node. |
| Average time consumption for a single query | Milliseconds | NodeSearchLaten cy | userId, instanceId, and nodeName | The average amount of time that is consumed by a single query. |
| Average Time Consumption of a Single Index | Milliseconds | NodeIndexingLat ency | userId, instanceId, and nodeName | The average amount of time that is consumed by a single index. |

**Index-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Write rate | Count/s | IndexRate | userId and indexName | The write rate. |

| Average write time | Milliseconds | AvgIndexTime | userId and indexName | The average amount of time that is consumed by a single write operation. |
|---|---|---|---|---|
| Query Rate | Count/s | SearchRate | userId and indexName | The query rate. |
| Average time consumption of a single query | Milliseconds | AvgSearchTime | userId and indexName | The average amount of time that is consumed by a single query. |
| Number of indexed documents | Count | IndexDocummen tCount | userId and indexName | The number of indexed documents. |
| Total Number of Segments | Count | IndexSegmentAll Shard | userId and indexName | The total number of segments. |
| Number of main segmentation | Count | IndexSegmentPri maries | userId and indexName | The number of primary shard segments. |
| Field memory | Bytes | FielddataMemory BytesTotal | userId and indexName | The field memory. |
| Index terms memory | Bytes | IndexMemoryTer ms | userId and indexName | The memory of the index terms. |
| Node points memory usage | Bytes | IndexMemoryPoi nts | userId and indexName | The memory of index points. |
| Index data size | Bytes | IndexDisk | userId and indexName | The size of the index data. |
| Index master slice data size | Bytes | IndexDiskPrimari es | userId and indexName | The data size of the primary shard of the index. |

**ApsaraMQ for RocketMQ**

Set the **Namespace** parameter to **acs_rocketmq_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Instance-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Message retention duration | Hour | MessageRetentio nPeriod | userId and instanceId | The retention duration of messages. |
| ReceiveMessage CountPerInstance | Count/min | ReceiveMessage CountPerInstance | userId and instanceId | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerInstance | Count/min | SendMessageCou ntPerInstance | userId and instanceId | The number of messages that the producer sends per minute. |
| Consumer(Instan ce) receives message TPS | Count/min | ReceiveMessage TPSPerInstance | userId and instanceId | The TPS for receiving messages by the consumer per minute. |
| Producer(Instanc e) sends messages TPS | Count/min | SendMessageTPS PerInstance | userId and instanceId | The TPS for sending messages by the producer per minute. |

**Group-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer Gid | Count | ConsumerLag | userId, instanceId, and groupId | The number of accumulated messages. |

| ReceiveMessage CountPerGid | Count/min | ReceiveMessage CountPerGid | userId, instanceId, and groupId | The number of messages that the consumer receives per minute. |
|---|---|---|---|---|
| SendDLQMessag eCountPerGid | Count/min | SendDLQMessag eCountPerGid | userId, instanceId, and groupId | The number of dead-letter messages generated per minute. |
| Producer(GroupId ) Number of messages sent per minute | Count/min | SendMessageCou ntPerGid | userId, instanceId, and groupId | The number of messages that the producer sends per minute. |
| Consumer(GroupI d) receives messages TPS | Count/min | ReceiveMessage TPSPerGid | userId, instanceId, and groupId | The TPS for receiving messages by the consumer per minute. |
| Producer(GroupId ) sends messages TPS | Count/min | SendMessageTPS PerGid | userId, instanceId, and groupId | The TPS for sending messages by the producer per minute. |

**Topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ReceiveMessage CountPerTopic | Count/min | ReceiveMessage CountPerTopic | userId, instanceId, and topic | The number of messages that the consumer receives per minute. |
| SendMessageCou ntPerTopic | Count/min | SendMessageCou ntPerTopic | userId, instanceId, and topic | The number of messages that the producer sends per minute. |

| Consumer (Topic) receives message TPS | Count/min | ReceiveMessage TPSPerTopic | userId, instanceId, and topic | The TPS for receiving messages by the consumer per minute. |
|---|---|---|---|---|
| Producer(Topic) sends messages TPS per minute | Count/min | SendMessageTPS PerTopic | userId, instanceId, and topic | The TPS for sending messages by the producer per minute. |

**Group and topic-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ConsumerLagPer GidTopic | Count | ConsumerLagPer GidTopic | userId, instanceId, groupId, and topic | The number of accumulated messages. |
| ReceiveMessage CountPerGidTopic | Count/min | ReceiveMessage CountPerGidTopi c | userId, instanceId, groupId, and topic | The number of messages that the consumer receives per minute. |
| SendDLQMessag eCountPerGidTop ic | Count/min | SendDLQMessag eCountPerGidTop ic | userId, instanceId, groupId, and topic | The number of dead-letter messages generated per minute. |
| Producer(GroupId & Topic) Number of messages sent per minute | Count/min | SendMessageCou ntPerGidTopic | userId, instanceId, groupId, and topic | The number of messages that the producer sends per minute. |

**File Storage NAS (NAS)**

Set the **Namespace** parameter to **acs_nas**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**File system-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Aligned Size | Bytes | AlignedSize | userId and fileSystemId | The data volume of the General- purpose NAS file systems, excluding the Infrequent Access (IA) storage class. |
| Storage Usage of IA Storage Medium | Bytes | SecondaryAligne dSize | userId and fileSystemId | The data volume of the IA storage class. |
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

**PolarDB**

Set the **Namespace** parameter to **acs_polardb_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**PolarDB-M**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-M) Connection Usage | % | ConnectionUsa ge new _ | userId and instanceId | The connection utilization. |
| (PolarDB-M) CPU usage | % | CpuUsage new _ | userId and instanceId | The CPU utilization. |
| (PolarDB-M) Memory Usage | % | MemoryUsage _ new | userId and instanceId | The memory usage. |
| Number of active connections | Count | Active Session _ new _ | userId and instanceId | The number of active connections. |
| Storage Engine IO throughput per second | KB | Iops throughou _ t new _ | userId and instanceId | The I/O throughput of the storage engine per second. |
| Storage engine IO times per second | Count/s | Mps new _ | userId and instanceId | The number of I/O operations of the storage engine per second. |
| IO times per second | Count/s | DataIo Ps new _ _ | userId and instanceId | The number of I/O operations per second. |

| Number of queries | Count | Queries Ps ne _ _ w | userId and instanceId | The number of queries. |
|---|---|---|---|---|
| Slow queries per second | Count/s | SlowQueries Ps _ new _ | userId and instanceId | The number of slow QPS. |
| TPS | Count/s | Tps M _ | userId and instanceId | The TPS. |
| Blktag Usage | % | BlktagUsage | userId and instanceId | The usage of blktags. |
| BlktagLeft | MB | BlktagLeft | userId and instanceId | The remaining size of blktags. |
| InodeUsage | % | InodeUsage | userId and instanceId | The inode usage. |
| InodeLeft | MB | InodeLeft | userId and instanceId | The remaining size of inodes. |
| DiskLeft | % | DiskLeft | userId and instanceId | The remaining disk space. |
| DiskUsage | MB | DiskUsage | userId and instanceId | The disk usage. |

**PolarDB-O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| (PolarDB-O)TPS | % | Tps O _ | userId and instanceId | The TPS. |
| (PolarDB-O) database CPU usage | % | Cgroup Cpu To _ _ tal | userId and instanceId | The CPU utilization of the database. |
| (PolarDB-O) Database Memory Usage | % | Cgroup Mem U _ _ sage | userId and instanceId | The memory usage of the database. |

| (PolarDB-O) Connection Usage | % | Connection Rati _ o | userId and instanceId | The connection utilization. |
|---|---|---|---|---|
| (PolarDB-O) Connections | Count | Connections O _ | userId and instanceId | The number of connections. |
| (PolarDB-O) Active Connections | Count | Active Connecti _ ons | userId and instanceId | The number of active connections. |
| (PolarDB-O)PFS reads IOPS | Frequenc y | Pfsd Read Iops _ _ | userId and instanceId | The read IOPS of the Polar file system (PFS). |
| (PolarDB-O)PFS writes IOPS | Frequenc y | Pfsd Write Iops _ _ | userId and instanceId | The write IOPS of the PFS. |
| (PolarDB-O) Database Age | xids | Db Age _ | userId and instanceId | The age of the database. |
| (PolarDB-O) Local Disk Usage | % | Local Disk Usa _ _ g | userId and instanceId | The local disk usage. |

**Data Transmission Service (DTS)**

Set the **Namespace** parameter to **acs_dts_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console- based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| ChangeTrackin gLatency | Seconds | ChangeTrackingLatenc y | userId and instanceId | The latency of the change tracking task. |
| Synchronizatio nLatency | Seconds | SynchronizationLatenc y | userId and instanceId | The latency of the data synchronization task. |
| MigrationLaten cy | Seconds | MigrationLatency | userId and instanceId | The latency of the data migration task. |

**Realtime Compute (Blink)**

Set the **Namespace** parameter to **acs_blink**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| FetchedDelay | Seconds | FetchedDelay | userId, regionId, projectName, and jobName | The processing latency. |
| Response Delay | % | inputDelay | userId, regionId, projectName, and jobName | The service latency. |
| Read RPS | RPS | ParserTpsRate | userId, regionId, projectName, and jobName | The read records per second (RPS). |
| Write RPS | RPS | SinkOutTpsRate | userId, regionId, projectName, and jobName | The write RPS. |
| FailoverRate | % | TaskFailoverRate | userId, regionId, projectName, and jobName | The failover rate. |

**MaxCompute**

Set the **Namespace** parameter to **acs_maxcompute_prepay**. Set the **Period** parameter to an integer multiple of 300. Default value: 300. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Project Use Space | Bytes | project used size _ _ | instanceId | The space used by the project. |

| Project upper limit space | Bytes | project max size _ _ | instanceId | The maximum space of the project. |
|---|---|---|---|---|
| Project space usage | % | project used rate _ _ | instanceId | The usage of the project space. |
| Number of files used by the project | Count | project used file _ _ _ number | instanceId | The number of files used by the project. |

**Realtime Compute for Apache Flink**

Set the **Namespace** parameter to **acs_flink.** Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Overview**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Times a Job Is Restarted upon a Failure | Count | flink jobmanager job nu _ _ _ mRestarts | userId and jobId | The number of times that a job is restarted upon a failure. |
| Job Duration | Milliseco nds | flink jobmanager job upti _ _ _ me | userId and jobId | The job duration. |
| Running Jobs | Count | flink jobmanager numRu _ _ nningJobs | userId and jobId | The number of jobs in progress. |
| Available Slots | Count | flink jobmanager taskSlo _ _ tsAvailable | userId and jobId | The number of available slots. |
| Total Number of Slots for a Task | Count | flink jobmanager taskSlo _ _ tsTotal | userId and jobId | The total number of slots for a task. |
| TM Quantity | Count | flink jobmanager numRe _ _ gisteredTaskManagers | userId and jobId | The number of task managers (TMs). |

| Processing Latency | Milliseco nds | flink taskmanager job ta _ _ _ sk operator currentEmitE _ _ ventTimeLag | userId and jobId | The processing latency. |
|---|---|---|---|---|
| Transmission Latency | Seconds | flink taskmanager job ta _ _ _ sk operator currentFetch _ _ EventTimeLag | userId and jobId | The transmission latency. |
| Total Number of Input Data Records of All Operators | N/A | flink taskmanager job ta _ _ _ sk operator numRecordsI _ _ n | userId and jobId | The total number of input data records of all operators. |
| Total Number of Output Data Records | Count | flink taskmanager job ta _ _ _ sk operator numRecords _ _ Out | userId and jobId | The total number of output data records. |
| Number of Input Data Records per Second for All Data Streams | Count/s | flink taskmanager job ta _ _ _ sk operator numRecordsI _ _ nPerSecond | userId and jobId | The number of input data records per second for all data streams. |
| Number of Output Data Records per Second for All Data Streams | Count/s | flink taskmanager job ta _ _ _ sk operator numRecords _ _ OutPerSecond | userId and jobId | The number of output data records per second for all data streams. |
| Number of Data Records Not Read by the Source | Count | flink taskmanager job ta _ _ _ sk operator pendingReco _ _ rds | userId and jobId | The number of data records that are not read by the source. |
| Duration for Which Data Is Not Processed in the Source | Milliseco nds | flink taskmanager job ta _ _ _ sk operator sourceIdleTi _ _ me | userId and jobId | The duration for which data is not processed in the source. |

**Checkpoint**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Number of Checkpoints | Count | flink jobmanager job total _ _ _ NumberOfCheckpoints | userId and jobId | The total number of checkpoints. |
| Number of Failed Checkpoints | Count | flink jobmanager job num _ _ _ berOfFailedCheckpoints | userId and jobId | The number of failed checkpoints. |

| Number of Completed Checkpoints | Count | flink jobmanager job num _ _ _ berOfCompletedCheckpoint s | userId and jobId | The number of completed checkpoints. |
|---|---|---|---|---|
| Number of In- progress Checkpoints | Count | flink jobmanager job num _ _ _ berOfInProgressCheckpoint s | userId and jobId | The number of checkpoints in progress. |
| Duration of the Last Checkpoint | Millisec onds | flink jobmanager job lastC _ _ _ heckpointDuration | userId and jobId | The duration of the last checkpoint. |
| Size of the Last Checkpoint | Bytes | flink jobmanager job lastC _ _ _ heckpointSize | userId and jobId | The size of the last checkpoint. |

**State**

| Console-based metric | Uni t | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Maximum Latency in a State Data Cleanup | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name st _ _ _ _ ateClearLatency | userId and jobId | The maximum latency in a state data cleanup. |
| Maximum Latency in Single ValueState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name val _ _ _ _ ueStateGetLatency | userId and jobId | The maximum latency in a query of the value state. |
| Maximum Latency in Single ValueState Access (Update) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name val _ _ _ _ ueStateUpdateLatency | userId and jobId | The maximum latency in an update of the value state. |
| Maximum Latency in Single AggregatingState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateGetLatency | userId and jobId | The maximum latency in a query of the aggregated value. |
| Maximum Latency in Single AggregatingState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateAddLatency | userId and jobId | The maximum latency that occurs when an aggregated value is added. |

| Maximum Latency in Single AggregatingState Access (MerageNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name ag _ _ _ _ gregatingStateMergeName spacesLatency | userId and jobId | The maximum latency that occurs when the aggregation states of namespaces are merged. |
|---|---|---|---|---|
| Maximum Latency in Single ReducingState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateGetLatency | userId and jobId | The maximum latency in a query of the reduced value. |
| Maximum Latency in Single ReducingState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateAddLatency | userId and jobId | The maximum latency that occurs when a value is added to the state. |
| Maximum Latency in Single ReducingState Access (MerageNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name re _ _ _ _ ducingStateMergeNamesp acesLatency | userId and jobId | The maximum latency that occurs when aggregation states of namespaces are merged. |
| Maximum Latency in Single MapState Access (IsEmpty) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIsEmptyLatency | userId and jobId | The maximum latency in a check on whether a map contains any key- value mappings. |
| Maximum Latency in Single MapState Access (teratorHasNext) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorHasNextLat ency | userId and jobId | The maximum latency in a check on whether the next entry exists. |
| Maximum Latency in Single MapState Access (IteratorNext) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorNextLatenc y | userId and jobId | The maximum latency in a query of the next key- value pair during the iteration of entries in a MapState. |
| Maximum Latency in Single MapState Access (IteratorRemove) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorRemoveLat ency | userId and jobId | The maximum latency in a removal of an entry during the iteration of a MapState. |

| Maximum Latency in Single MapState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateGetLatency | userId and jobId | The maximum latency in a query of a key-value pair in a MapState. |
|---|---|---|---|---|
| Maximum Latency in Single MapState Access (Put) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStatePutLatency | userId and jobId | The maximum latency that occurs when a key-value pair is written to a MapState. |
| Maximum Latency in Single MapState Access (PutAll) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStatePutAllLatency | userId and jobId | The maximum latency that occurs when a group of key-value pair is written to a MapState. |
| Maximum Latency in Single MapState Access (Remove) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateRemoveLatency | userId and jobId | The maximum latency that occurs when a key-value pair is removed from a MapState. |
| Maximum Latency in Single MapState Access (Contains) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateContainsLatency | userId and jobId | The maximum latency in a check on whether a key- value pair exists in a MapState. |
| Maximum Latency in Single MapState Access (EntriesInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateEntriesInitLatency | userId and jobId | The maximum latency that occurs when a MapState is initialized. |
| Maximum Latency in Single MapState Access (KeysInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateKeysInitLatency | userId and jobId | The maximum latency that occurs when keys of a MapState are loaded during the initialization of the MapState. |

| Maximum Latency in Single MapState Access (ValuesInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateValuesInitLatency | userId and jobId | The maximum latency that occurs when values of a MapState are loaded during the initialization of the MapState. |
|---|---|---|---|---|
| Maximum Latency in Single MapState Access (IteratorInit) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name m _ _ _ _ apStateIteratorInitLatency | userId and jobId | The maximum latency that occurs when an iterator is initialized. |
| Maximum Latency in Single ListState Access (Get) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateGetLatency | userId and jobId | The maximum latency in a query of the key-value pairs in a ListState. |
| Maximum Latency in Single ListState Access (Add) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateAddLatency | userId and jobId | The maximum latency that occurs when a key-value pair is added to a ListState. |
| Maximum Latency in Single ListState Access (AddAll) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateAddAllLatency | userId and jobId | The maximum latency that occurs when a group of key-value pairs is added to a ListState. |
| Maximum Latency in Single ListState Access (Update) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateUpdateLatency | userId and jobId | The maximum latency that occurs when data in a ListState is updated. |
| Maximum Latency in Single ListState Access (MergeNamespaces) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name list _ _ _ _ StateMergeNamespacesLat ency | userId and jobId | The maximum latency that occurs when namespaces are merged. |

| Maximum Latency in Single SortedMapState Access (FirstEntry) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name so _ _ _ _ rtedMapStateFirstEntryLat ency | userId and jobId | The maximum latency that occurs when the first entry in a sorted MapState is queried. |
|---|---|---|---|---|
| Maximum Latency in Single SortedMapState Access (LastEntry) | Na nos eco nds | flink taskmanager job tas _ _ _ k operator state name so _ _ _ _ rtedMapStateLastEntryLate ncy | userId and jobId | The maximum latency that occurs when the last entry in a sorted MapState is queried. |

**Network**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Input Pool Usage | % | flink taskmanager job tas _ _ _ k buffers inPoolUsage _ _ | userId and jobId | The usage of the input pool. |
| Output Pool Usage | % | flink taskmanager job tas _ _ _ k buffers outPoolUsage _ _ | userId and jobId | The usage of the output pool. |
| Input Queue Length | Valu e | flink taskmanager job tas _ _ _ k buffers inputQueueLeng _ _ th | userId and jobId | The length of the input queue. |
| Output Queue Length | Valu e | flink taskmanager job tas _ _ _ k buffers outputQueueLe _ _ ngth | userId and jobId | The length of the output queue. |

**I/O**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Total Number of Input Bytes | Bytes | flink taskmanager job tas _ _ _ k operator numBytesIn _ _ | userId and jobId | The total number of input bytes. |
| Total Number of Input Bytes per Second (Local) | Bytes/s | flink taskmanager job tas _ _ _ k numBytesInLocalPerSec _ ond | userId and jobId | The total number of input bytes per second of a local system. |

| Total Number of Input Bytes per Second (Remote) | Bytes/s | flink taskmanager job tas _ _ _ k numBytesInRemotePerS _ econd | userId and jobId | The total number of input bytes per second of a remote system. |
|---|---|---|---|---|
| Total Number of Input Buffers per Second (Local) | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersInLocalPerSe _ cond | userId and jobId | The total amount of data imported from buffers per second in a local system. |
| Total Number of Input Buffers per Second (Remote) | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersInRemotePer _ Second | userId and jobId | The total amount of data imported from buffers per second in a remote system. |
| Total Number of Input Bytes per Second (Operator) | Bytes/s | flink taskmanager job tas _ _ _ k operator numBytesInPer _ _ Second | userId and jobId | The total number of input bytes received by an operator per second. |
| Total Number of Output Bytes | Bytes | flink taskmanager job tas _ _ _ k operator numBytesOut _ _ | userId and jobId | The total number of output bytes. |
| Total Number of Output Bytes per Second | Bytes/s | flink taskmanager job tas _ _ _ k numBytesOutPerSecond _ | userId and jobId | The total number of output bytes per second. |
| Total Number of Output Buffers per Second | Bytes/s | flink taskmanager job tas _ _ _ k numBuffersOutPerSecon _ d | userId and jobId | The total number of bytes that are sent from buffers per second. |
| Total Number of Output Bytes per Second (Operator) | Bytes/s | flink taskmanager job tas _ _ _ k operator numBytesOutP _ _ erSecond | userId and jobId | The total number of output bytes sent by an operator per second. |

| Total Number of Data Records That Flow into Each Subtask | Count | flink taskmanager job tas _ _ _ k numRecordsIn _ | userId and jobId | The total amount of data received by each subtask. |
|---|---|---|---|---|
| Total Number of Data Records That Are Exported by Each Subtask | Count | flink taskmanager job tas _ _ _ k numRecordsOut _ | userId and jobId | The total amount of data exported by each subtask. |
| Total Number of Data Records That Flow into Each Subtask per Second | Count/ s | flink taskmanager job tas _ _ _ k numRecordsInPerSecond _ | userId and jobId | The total amount of data received by each subtask per second. |
| Total Number of Data Records That Are Exported by Each Subtask per Second | Count/ s | flink taskmanager job tas _ _ _ k numRecordsOutPerSeco _ nd | userId and jobId | The total amount of data exported by each subtask per second. |
| Time Required by Each Subtask to Export the Last Data Record to the Sink | Second s | flink taskmanager job tas _ _ _ k operator currentSendTi _ _ me | userId and jobId | The duration that is required by each subtask to export the last data record to the sink. |

**Watermark**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Time When Each Task Receives the Latest Watermark | Millis econ ds | flink taskmanager job ta _ _ _ sk currentInputWatermar _ k | userId and jobId | The time when each task receives the latest watermark. |
| Time When Each Task Receives the Latest Watermark (Operator) | Millis econ ds | flink taskmanager job ta _ _ _ sk operator currentInput _ _ Watermark | userId and jobId | The time when each task receives the last watermark in an operator. |

| Time When Each Task Transmits the Latest Watermark (Operator) | Millis econ ds | flink taskmanager job ta _ _ _ sk operator currentOutpu _ _ tWatermark | userId and jobId | The time when each task sends the last watermark in an operator. |
|---|---|---|---|---|
| Watermark Latency | Millis econ ds | flink taskmanager job ta _ _ _ sk operator watermarkLa _ _ g | userId and jobId | The latency of watermarks. |

**CPU**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU Load of a Single JM | % | flink jobmanager Statu _ _ s JVM CPU Load _ _ _ | userId and jobId | The CPU load of a JobManager. |
| CPU Load of a Single TM | % | flink taskmanager Stat _ _ us JVM CPU Load _ _ _ | userId and jobId | The CPU load of a TaskManager. |
| CPU Utilization of a Single TM | % | flink taskmanager Stat _ _ us ProcessTree CPU Us _ _ _ age | userId and jobId | The CPU utilization of a TaskManager. |

**Memory**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Heap Memory of JM (Used) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Use _ _ _ _ d | userId and jobId | The heap memory used by the JobManager. |
| Heap Memory of JM (Committed) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Co _ _ _ _ mmitted | userId and jobId | The heap memory allocated by the JobManager. |
| Heap Memory of JM (Max) | Byte s | flink jobmanager Status _ _ JVM Memory Heap Ma _ _ _ _ x | userId and jobId | The maximum heap memory that can be used by the JobManager. |

| Non-Heap Memory for JM (Used) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Used _ | userId and jobId | The non-heap memory that is used by the JobManager. |
|---|---|---|---|---|
| Non-Heap Memory of JM (Committed) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Committed _ | userId and jobId | The non-heap memory that is allocated by the JobManager. |
| Non-Heap Memory of JM (Max) | Byte s | flink jobmanager Status _ _ JVM Memory NonHeap _ _ _ Max _ | userId and jobId | The maximum non-heap memory that can be used by the JobManager. |
| Used Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap Us _ _ _ _ ed | userId and jobId | The heap memory used by the TaskManager |
| Committed Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap Co _ _ _ _ mmitted | userId and jobId | The heap memory allocated by the TaskManager. |
| Max. Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory Heap M _ _ _ _ ax | userId and jobId | The maximum heap memory that can be used by the TaskManager. |
| Used Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Used _ | userId and jobId | The non-heap memory used by the TaskManager. |
| Committed Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Committed _ | userId and jobId | The non-heap memory allocated by the TaskManager. |
| Max. Non-Heap Memory of TM | Byte s | flink taskmanager Statu _ _ s JVM Memory NonHea _ _ _ p Max _ | userId and jobId | The maximum non-heap memory that can be used by the TaskManager. |

| Memory of the Entire Process by Using Linux | Byte s | flink taskmanager Statu _ _ s ProcessTree Memory _ _ _ RSS | userId and jobId | The amount of memory consumed by the entire process on Linux. |
|---|---|---|---|---|

**JVM**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Number of Threads of JM | Count | flink jobmanager Status _ _ _ JVM Threads Count _ _ | userId and jobId | The number of threads of the JobManager. |
| Number of Threads of TM | Count | flink taskmanager Statu _ _ s JVM Threads Count _ _ _ | userId and jobId | The number of threads of a TaskManager. |
| Number of GCs on JM (ParNew) | Count | flink jobmanager Status _ _ _ JVM GarbageCollector Pa _ _ rNew Count _ | userId and jobId | The number of GCs performed by using ParNew on a JobManager. |
| Number of GCs on JM (ConcurrentMarkSwe ep) | Count | flink jobmanager Status _ _ _ JVM GarbageCollector Co _ _ ncurrentMarkSweep Cou _ nt | userId and jobId | The number of GCs performed by using Concurrent Mark Sweep (CMS). |
| Duration of Each GC on JM (ParNew) | Millisec onds | flink jobmanager Status _ _ _ JVM GarbageCollector Pa _ _ rNew Time _ | userId and jobId | The duration of each GC performed by using ParNew. |
| Duration of Each GC on JM (ConcurrentMarkSwe ep) | Millisec onds | flink jobmanager Status _ _ _ JVM GarbageCollector Co _ _ ncurrentMarkSweep Tim _ e | userId and jobId | The duration of each GC performed by using CMS. |
| Number of GCs on TM (ParNew) | Count | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ParNew Count _ | userId and jobId | The number of GCs performed by using ParNew on a TaskManager. |

| Number of GCs on TM (ConcurrentMarkSwe ep) | Count | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ConcurrentMarkSweep C _ ount | userId and jobId | The number of GCs performed by using CMS on a TaskManager. |
|---|---|---|---|---|
| Duration of Each GC on JM (ParNew) | Millisec onds | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ParNew Time _ | userId and jobId | The duration of each GC performed by using ParNew on a TaskManager. |
| Duration of Each GC on JM (ConcurrentMarkSwe ep) | Millisec onds | flink taskmanager Statu _ _ s JVM GarbageCollector _ _ _ ConcurrentMarkSweep Ti _ me | userId and jobId | The duration of each GC performed by using CMS on a TaskManager. |
| Total Classes Loaded After the JVM Where the JM Resides Is Created | Value | flink jobmanager Status _ _ _ JVM ClassLoader Classes _ _ Loaded |   | The total number of classes loaded after the Java Virtual Machine (JVM) where the JobManager resides is created. |
| Total Classes Unloaded After the JVM Where the JM Resides Is Created | Value | flink jobmanager Status _ _ _ JVM ClassLoader Classes _ _ Unloaded | userId and jobId | The total number of classes unloaded after the JVM where the JobManager resides is created. |
| Total Classes Loaded After the JVM Where the TM Resides Is Created | Value | flink taskmanager Statu _ _ s JVM ClassLoader Class _ _ _ esLoaded | userId and jobId | The total number of classes loaded after the JVM where the TaskManager resides is created. |
| Total Classes Unloaded After the JVM Where the TM Resides Is Created | Value | flink taskmanager Statu _ _ s JVM ClassLoader Class _ _ _ esUnloaded | userId and jobId | The total number of classes unloaded after the JVM where the TaskManager resides is created. |

**Cloud Storage Gateway (CSG)**

Set the **Namespace** parameter to **acs_csg_dashboard**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| csg gateway cpu us _ _ _ age percentage _ | % | csg gateway cpu usage _ _ _ percentage _ | userId and instanceId | The CPU utilization of the gateway. |
| csg gateway memor _ _ y usage percentage _ _ | % | csg gateway memory u _ _ _ sage percentage _ | userId and instanceId | The memory usage of the gateway. |
| csg gateway cache _ _ _ usage percentage _ | % | csg gateway cache usa _ _ _ ge percentage _ | userId, instanceId, and shareName | The cache space usage of the gateway. |
| csg gateway running _ _ state _ | Count | csg gateway running st _ _ _ ate | userId, instanceId, and shareName | The status of the gateway. |
| csg gateway share _ _ _ upload queue num _ _ | Count | csg gateway file share _ _ _ _ upload queue num _ _ | userId, instanceId, and shareName | The number of queued requests for uploading files to a bucket. |
| csg gateway file sha _ _ _ re remaining meta s _ _ _ pace bytes _ | Bytes | csg gateway file share _ _ _ _ remaining meta space _ _ _ bytes | userId, instanceId, and shareName | The remaining metadata space for gateway file share. |
| csg gateway file sha _ _ _ re throttling state _ _ | Count | csg gateway file share _ _ _ _ throttling state _ | userId, instanceId, and shareName | The throttling status of gateway file share. |
| csg gateway file sha _ _ _ re read write rate K _ _ _ _ Bps | Kbit/s | csg gateway file share _ _ _ _ read write rate KBps _ _ _ | userId, instanceId, and shareName | The read and write rate of gateway file share. |

| csg gateway file sha _ _ _ re read IOPS _ _ | Kbit/s | csg gateway file share _ _ _ _ read IOPS _ | userId, instanceId, and shareName | The read IOPS of gateway file share. |
|---|---|---|---|---|
| csg gateway file sha _ _ _ re write IOPS _ _ | Kbit/s | csg gateway file share _ _ _ _ write IOPS _ | userId, instanceId, and shareName | The write IOPS of gateway file share. |
| csg gateway file sha _ _ _ re upload rate KBps _ _ _ | Kbit/s | csg gateway file share _ _ _ _ upload rate KBps _ _ | userId, instanceId, and shareName | The rate at which the shared file is uploaded to OSS buckets. |

**Lindorm**

Set the **Namespace** parameter to **acs_lindorm**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Wide table engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Wide Table Engine Metrics-Read Requests-Read Request Volume | Rows/s | WTEM RR readRequestVolu _ _ me | userId and instanceId | The number of read requests per second in the wide table engine. |
| Wide table engine metric-read request- read average RT | Millisec onds | WTEM RR readAverageRT _ _ | userId and instanceId | The average response time of read requests in the wide table engine. |
| Wide Table Engine Metrics-Read Request-Read Traffic | Value | WTEM RR readTraffic _ _ | userId and instanceId | The read traffic in the wide table engine. |
| Wide table engine metric-read request- Get request volume | Rows/s | WTEM RR getRequestVolum _ _ e | userId and instanceId | The number of GET requests per second in the wide table engine. |

| Wide table engine metric-read request- Get average RT | Millisec onds | WTEM RR getAverageRT _ _ | userId and instanceId | The average response time of GET requests in the wide table engine. |
|---|---|---|---|---|
| Wide table engine metric-read request- Get P99 RT | Millisec onds | WTEM RR getP99RT _ _ | userId and instanceId | The average P99 response time of read requests in the wide table engine. |
| Wide table engine metrics-read requests-Scan requests | Reques ts/s | WTEM RR scanRequestVolu _ _ me | userId and instanceId | The number of SCAN requests per second in the wide table engine. |
| Wide table engine metric-read request- Scan average RT | Millisec onds | WTEM RR scanAverageRT _ _ | userId and instanceId | The average response time of SCAN requests in the wide table engine. |
| Wide table engine metric-read request- Scan P99 RT | Millisec onds | WTEM RR scanP99RT _ _ | userId and instanceId | The average P99 response time of SCAN requests in the wide table engine. |
| Wide Table Engine Metrics-Write Requests-Write Request Volume | Reques ts/s | WTEM WR writeRequestVol _ _ ume | userId and instanceId | The number of requests per second in the wide table engine. |
| Wide Table Engine Metrics-Write Request-Write Average RT | Millisec onds | WTEM WR writeRequests _ _ | userId and instanceId | The average response time of write request in the wide table engine. |
| Wide Table Engine Metrics-Write Request-Write Traffic | Value | WTEM WR writeTraffic _ _ | userId and instanceId | The write traffic in the wide table engine. |

| Wide Table Engine Metrics-Write Requests-Put Total Requests | Reques ts/s | WTEM WR putTotalRequest _ _ Volume | userId and instanceId | The number of PUT requests per second in the wide table engine. |
|---|---|---|---|---|
| Wide table engine metric-write request- Put average RT | Millisec onds | WTEM WR putAverageRT _ _ | userId and instanceId | The average response time of PUT requests in the wide table engine. |
| Wide Table Engine Metrics-Write Requests-Put Requests | Reques ts/s | WTEM WR putRequestVolu _ _ me | userId and instanceId | The number of PUT requests per second in the wide table engine. |
| WTEM WR exceeding _ _ MemstoreUpperLimit | Count | WTEM WR exceedingMemst _ _ oreUpperLimit | userId and instanceId | The number of times that the memstore limit has been exceeded. |
| Wide table engine metric-write request- Put P99 RT | Millisec onds | WTEM WR putP99RT _ _ | userId and instanceId | The average P99 response time of PUT requests in the wide table engine. |
| Wide table engine metric -- SQLv2- Number of SQL connections | Count | WTEM SQLv2 sQLConnectio _ _ nCount | userId and instanceId | The number of SQL connections. |
| Wide Table Engine Metrics-SQLv2- Number of select requests | Reques ts/s | WTEM SQLv2 selectRequest _ _ Count | userId and instanceId | The number of SELECT requests per second. |
| Wide table engine metrics-SQLv2-select request p99 time consumption | Millisec onds | WTEM SQLv2 selectP99Req _ _ uestTime | userId and instanceId | The average P99 response time of SELECT requests in the wide table engine. |
| Wide Table Engine Metrics-SQLv2- Number of upsert requests | Reques ts/s | WTEM SQLv2 upsertReques _ _ tCount | userId and instanceId | The number of UPSERT requests. |

| Wide Table Engine Metrics-SQLv2-upsert Request p99 Time | Millisec onds | WTEM SQLv2 upsertP99Req _ _ uestTime | userId and instanceId | The average P99 response time of UPSERT requests. |
|---|---|---|---|---|
| Wide Table Engine Metrics-SQLv2- Number of delete requests | Reques ts/s | WTEM SQLv2 deleteReques _ _ tCount | userId and instanceId | The number of DELETE requests. |
| Wide table engine metric -- SQLv2- delete request p99 time consumed | Millisec onds | WTEM SQLv2 deleteP99Req _ _ uestTime | userId and instanceId | The average P99 response time of DELETE requests. |
| WTEM CL rSRegionC _ _ ount | Count | WTEM CL rSRegionCount _ _ | userId and instanceId | The number of regions managed by the region server. |
| Wide Table Engine Metrics-Cluster Load- Handler Queue Length | Count | WTEM CL handlerQueueLen _ _ gth | userId and instanceId | The number of requests queued on the Handler. |
| Wide Table Engine Metrics-Cluster Load- Compaction Queue Length | Count | WTEM CL compactionQueu _ _ eLength | userId and instanceId | The number of requests in the compaction queue. |
| Wide Table Engine metric-SQLv2-median time spent on delete requests | Millisec onds | WTEM SQLv2 deleteMedian _ _ RequestTime | userId and instanceId | The P50 response time of DELETE requests. |
| Wide table engine metric-SQLv2-median upsert request time | Millisec onds | WTEM SQLv2 upsertMedian _ _ RequestTime | userId and instanceId | The P50 response time of UPSERT requests. |
| Wide table engine metric-SQLv2-median time spent on select requests | Millisec onds | WTEM SQLv2 selectMedian _ _ RequestTime | userId and instanceId | The P50 response time of SELECT requests. |

**Time series engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| Timing Engine Metrics-Write Volume | Points/ s | TSEM WV _ | userId and instanceId | The amount of data written per second. |
| Timing Engine Metrics-Failure Amount | Points/ s | TSEM FV _ | userId and instanceId | The amount of data that fails to be written. |
| Timing Engine Metrics-Write Request Volume | Reques ts/s | TSEM writeRequestVolume _ | userId and instanceId | The number of write requests per second. |
| Time series engine metrics-write average RT | Millisec onds | TSEM writeAverageRT _ | userId and instanceId | The average response time of write requests. |
| Timing Engine Metrics-Write RT P99 | Millisec onds | TSEM writeRTP99 _ | userId and instanceId | The average P99 response time of write requests. |
| Time Series Engine Metrics-Read Request Volume | Reques ts/s | TSEM readRequestVolume _ | userId and instanceId | The number of read requests per second. |
| Time Series Engine Metrics-Number of Active Connections | Count | TSEM activeConnectionsCou _ nt | userId and instanceId | The number of active connections. |
| Time Series Engine Metrics-Number of Active Statements | Count | TSEM activesStatementCou _ nt | userId and instanceId | The number of active statements. |
| Timing Engine Metrics-Number of Active Resultsets | Count | TSEM activeResultSetCount _ | userId and instanceId | The number of active result sets. |
| Time Series Engine Metrics-Insert Rows | Rows/s | TSEM insertRowCount _ | userId and instanceId | The number of inserted rows. |
| Timing Engine Metrics-Select Number of Scan Lines | Rows/s | TSEM selectScanRowCount _ | userId and instanceId | The number of scanned rows. |

| Time Series Engine Metrics-Number of Select requests | Rows/s | TSEM selectRequestCount _ | userId and instanceId | The number of SELECT requests. |
|---|---|---|---|---|
| Time Series Engine metric-Select average RT | Millisec onds | TSEM selectAverageRT _ | userId and instanceId | The average response time of SELECT requests. |
| Time series engine metrics-Select time consumption P99 | Millisec onds | TSEM selectTimeP99 _ | userId and instanceId | The average P99 response time of SELECT requests. |
| Time Series Engine Metrics - Client Connections | Count | TSEM clientConnectionCoun _ t | userId and instanceId | The number of client connections. |
| Time Series Engine Metrics - Average RT for API-based Multi- value Query | Millisec onds | TSEM queryAverageRT mqu _ _ ery | userId and instanceId | The average response time of multi-value queries based on API. |
| Time Series Engine Metrics - Average RT for API-based Single- value Query | Millisec onds | TSEM TSEM queryAverageR _ _ T query _ | userId and instanceId | The average response time of single-value queries based on API. |
| Time Series Engine Metrics - RT for API- based Multi-value Query (P99) | Millisec onds | TSEM queryRTP99 mquery _ _ | userId and instanceId | The P99 response time of multi-value queries. |
| Time Series Engine Metrics - RT for API- based Single-value Query (P99) | Millisec onds | TSEM queryRTP99 query _ _ | userId and instanceId | The P99 response time of single-value queries. |
| Time Series Engine Metrics-Number of Timelines | Count | TSEM timelineCount _ | userId and instanceId | The number of time series. |

**File engine-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| File Engine Metrics- Storage (Hot Storage) Usage- Storage Usage | Value | FEM SU storageUsed _ _ | userId and instanceId | The usage of hot storage space. |
|---|---|---|---|---|
| File Engine Metrics- Storage (Hot Storage) Usage-Total Storage | Value | FEM SU totalStorage _ _ | userId and instanceId | The total hot storage space. |
| File Engine Metrics- Storage (Hot Storage) Usage- (lindorm Multi-AZ) | Value | FEM SU dfs fsnamesystem _ _ _ _ capacitytotal | userId and instanceId | The usage of hot storage in multiple zones of Lindorm. |
| File Engine Metrics- Storage (Hot Storage) Usage- (Lindorm Multi-AZ) | Value | FEM SU dfs fsnamesystem _ _ _ _ capacityused | userId and instanceId | The usage of hot storage in multiple zones of Lindorm. |
| File Engine Indicator- Storage (Hot Storage) Level | % | FEM sWatermark _ | userId and instanceId | The usage of the hot storage. |
| File Engine Metrics- NameNode Operands (times/sec)- create file ops _ _ | Operati ons/s | FEM NO create file ops _ _ _ _ | userId and instanceId | The number of times that files are created on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- delete file ops _ _ | Operati ons/s | FEM NO delete file ops _ _ _ _ | userId and instanceId | The number of times that files are deleted from NameNodes per second. |

| File Engine Metrics- NameNode Operands (times/sec)- add block ops _ _ | Operati ons/s | FEM NO add block ops _ _ _ _ | userId and instanceId | The number of times that blocks are added to NameNodes per second. |
|---|---|---|---|---|
| File Engine Metrics- NameNode Operands (times/sec)- get blockloc ops _ _ | Operati ons/s | FEM NO _ | userId and instanceId | The number of times that blocks are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- get file info ops _ _ _ | Operati ons/s | FEM NO get file info ops _ _ _ _ _ | userId and instanceId | The number of times that files are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- list dir ops _ _ | Operati ons/s | FEM NO list dir ops _ _ _ _ | userId and instanceId | The number of times that directories are queried on NameNodes per second. |
| File Engine Metrics- NameNode Operands (times/sec)- block report ops _ _ | Operati ons/s | FEM NO block report ops _ _ _ _ | userId and instanceId | The number of times that reports of blocks are exported on NameNodes per second. |
| File engine metrics- DataNode read traffic | Value | FEM dataNodeReadTraffic _ | userId and instanceId | The read traffic of DataNodes. |
| File engine metrics- DataNode write traffic | Value | FEM dataNodeWriteTraffic _ | userId and instanceId | The write traffic of DataNodes. |

**Container Service Monitoring**

Set the **Namespace** parameter to **acs_k8s**. Set the **Period** parameter to an integer multiple of 60. Default value: 60. Unit: seconds.

**Cluster**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| CPU resource limit | Cores | cluster.cpu.limit | user id and _ cluster name _ | The maximum number of CPU cores that can be used by a container. |
| CPU resource request | Cores | cluster.cpu.request | user id and _ cluster name _ | The minimum number of CPU cores requested by a container during scheduling. |
| CPU usage | Cores | cluster.cpu.usage rate _ | user id and _ cluster name _ | The CPU utilization. |
| cpu usage of cluster dimension | % | cluster.cpu.utilization | user id and _ cluster name _ | The CPU utilization. |
| Filesystem resource available | Bytes | cluster.filesystem.available | user id and _ cluster name _ | The size of the file system that is available to the cluster. |
| Filesystem resource limit | Bytes | cluster.filesystem.limit | user id and _ cluster name _ | The maximum number of file systems in the cluster. |
| Cluster Memory Limits | Bytes | cluster.memory.limit | user id and _ cluster name _ | The maximum memory of the cluster. |
| Cluster Memory Requests | Bytes | cluster.memory.request | user id and _ cluster name _ | The memory requested by the cluster. |
| cluster.memory.utiliz ation | % | cluster.memory.utilization | user id and _ cluster name _ | The memory usage of the cluster. |

**Node-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|

| node.cpu.allocatabl e | Cores | node.cpu.allocatable | userId, cluster, and node | The number of CPU cores that can be allocated to the node. |
|---|---|---|---|---|
| node.cpu.capacity | Cores | node.cpu.capacity | userId, cluster, and node | The CPU capacity of the node. |
| node.cpu.limit | Cores | node.cpu.limit | userId, cluster, and node | The maximum number of CPU cores of the node. |
| node.cpu.oversale r _ ate(usage/request) | % | node.cpu.oversale rate _ | userId, cluster, and node | The oversold ratio of CPU resources. |
| node.cpu.request | Cores | node.cpu.request | userId, cluster, and node | The CPU resources requests by the node. |
| node.cpu.reservatio n | Cores | node.cpu.reservation | userId, cluster, and node | The reserved CPU resources of the node. |
| node.cpu.usage rat _ e | Cores | node.cpu.usage rate _ | userId, cluster, and node | The CPU usage. |
| node.cpu.utilization | % | node.cpu.utilization | userId, cluster, and node | The CPU utilization. |
| node.filesystem.avai lable | Count | node.filesystem.available | userId, cluster, and node | The number of file systems that can be used by the node. |
| node.filesystem.ino des | Count | node.filesystem.inodes | userId, cluster, and node | The inodes of file systems of the node. |

| node.filesystem.limi t | Count | node.filesystem.limit | userId, cluster, and node | The maximum number of file systems that can be used by the node. |
|---|---|---|---|---|
| node.filesystem.usa ge | Count | node.filesystem.usage | userId, cluster, and node | The file system usage. |
| node.memory.alloca table | GB | node.memory.allocatable | userId, cluster, and node | The memory allocated to the node. |
| node.memory.cache | GB | node.memory.cache | userId, cluster, and node | The memory cache of the node. |
| node.memory.capac ity | Count | node.memory.capacity | userId, cluster, and node | The memory capacity of the node. |
| node.memory.limit | Count | node.memory.limit | userId, cluster, and node | The maximum memory that can be used by the node. |
| node.memory.major page faults _ _ | Count | node.memory.major page f _ _ aults | userId, cluster, and node | The number of major page faults that occur on the node. |
| node.memory.major page faults rate _ _ _ | Count | node.memory.major page f _ _ aults rate _ | userId, cluster, and node | The rate at which major page faults occur on the node. |
| node.memory.overs ale rate _ | % | node.memory.oversale rate _ | userId, cluster, and node | The oversold ratio of memory resources. |
| node.memory.page _ faults | Count | node.memory.page faults _ | userId, cluster, and node | The number of page faults that occur on the node. |

| node.memory.page _ faults rate _ | Count | node.memory.page faults r _ _ ate | userId, cluster, and node | The rate at which page faults occur on the node. |
|---|---|---|---|---|
| node.memory.reque st | Count | node.memory.request | userId, cluster, and node | The memory requested by the node. |
| node.memory.reser vation | Count | node.memory.reservation | userId, cluster, and node | The reserved memory of the node. |
| node.memory.rss | Count | node.memory.rss | userId, cluster, and node | The resident set size (RSS). |
| node.memory.usage | Count | node.memory.usage | userId, cluster, and node | The memory usage. |
| node.memory.utiliza tion | Count | node.memory.utilization | userId, cluster, and node | The memory usage. |
| node.memory.worki ng set _ | Count | node.memory.working set _ | userId, cluster, and node | The working set memory of the node. |
| node.network.rx err _ ors | Count | node.network.rx errors _ | userId, cluster, and node | The number of receive errors that occur on the network of the node. |
| node.network.rx err _ ors rate _ | % | node.network.rx errors rate _ _ | userId, cluster, and node | The rate at which receive errors occur on the network of the node. |
| node.network.rx rat _ e | Count/ s | node.network.rx rate _ | userId, cluster, and node | The number of send errors that occur on the network of the node. |
| node.network.tx err _ ors rat _ | % | node.network.tx errors rat _ _ | userId, cluster, and node | The rate at which send errors occur on the network of the node. |

**Pod-related metrics**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| pod.cpu.limit | Cores | pod.cpu.limit | userId, cluster, namespace, type, app, and pod | The maximum amount of CPU resources that can be used by the pod. |
| pod.cpu.oversale rat _ e | % | pod.cpu.oversale rate _ | userId, cluster, namespace, type, app, and pod | The oversold ratio of CPU resources. |
| pod.cpu.request | Cores | pod.cpu.request | userId, cluster, namespace, type, app, and pod | The minimum amount of CPU resources requested by the pod. |
| pod.cpu.usage rate _ | Cores | pod.cpu.usage rate _ | userId, cluster, namespace, type, app, and pod | The CPU usage of the pod. |
| pod.cpu.utilization | % | pod.cpu.utilization | userId, cluster, namespace, type, app, and pod | The CPU utilization of the pod. |
| pod.filesystem.availa ble | Bytes | pod.filesystem.available | userId, cluster, namespace, type, app, and pod | The available size of the file system in the pod. |
| pod.filesystem.limit | Bytes | pod.filesystem.limit | userId, cluster, namespace, type, app, and pod | The maximum size of file systems in the pod. |
| pod.filesystem.usage | Bytes | pod.filesystem.usage | userId, cluster, namespace, type, app, and pod | The file systems used by the pod. |
| pod.filesystem.utiliza tion | % | pod.filesystem.utilization | userId, cluster, namespace, type, app, and pod | The file system usage of the pod. |

| pod.memory.cache | Bytes | pod.memory.cache | userId, cluster, namespace, type, app, and pod | The memory resource cache of the pod. |
|---|---|---|---|---|
| pod.memory.limit | Bytes | pod.memory.limit | userId, cluster, namespace, type, app, and pod | The maximum memory that can be allocated to the pod. |
| pod.memory.oversal e rate _ | % | pod.memory.oversale rate _ | userId, cluster, namespace, type, app, and pod | The oversold ratio of memory resources. |
| pod.memory.request | Bytes | pod.memory.request | userId, cluster, namespace, type, app, and pod | The minimum amount of memory resources requested by the pod. |
| pod.memory.rss | Bytes | pod.memory.rss | userId, cluster, namespace, type, app, and pod | The RSS of the pod. |
| pod.memory.utilizati on | % | pod.memory.utilization | userId, cluster, namespace, type, app, and pod | The memory usage of the pod. |
| pod.memory.working set _ | Bytes | pod.memory.working set _ | userId, cluster, namespace, type, app, and pod | The amount of memory of the container. |
| pod.network.rx error _ s rate _ | Count/ s | pod.network.rx errors rate _ _ | userId, cluster, namespace, type, app, and pod | The rate at which receive errors occur in the network of the pod. |
| pod.network.rx rate _ | Bytes/s | pod.network.rx rate _ | userId, cluster, namespace, type, app, and pod | The rate at which the pod receives data. |

| pod.network.tx error _ s rate _ | Bytes/s | pod.network.tx errors rate _ _ | userId, cluster, namespace, type, app, and pod | The rate at which send errors occur in the network of the pod. |
|---|---|---|---|---|
| pod.network.tx rate _ | Bytes/s | pod.network.tx rate _ | userId, cluster, namespace, type, app, and pod | The rate at which the pod sends data. |

**Deployment**

| Console-based metric | Unit | API-based metric | Dimension | Description |
|---|---|---|---|---|
| deployment.cpu.limit | Cores | deployment.cpu.limit | userId, cluster, namespace, type, and app | The maximum amount of CPU resource that can be allocated to the Deployment. |
| deployment.cpu.usag e rate _ | Cores | deployment.cpu.usage rate _ | userId, cluster, namespace, type, and app | The CPU resources used by the Deployment. |
| deployment.filesyste m.available | byte | deployment.filesystem.avai lable | userId, cluster, namespace, type, and app | The size of the file system available to the Deployment. |
| deployment.filesyste m.limit | Bytes | deployment.filesystem.limit | userId, cluster, namespace, type, and app | The maximum number of file systems that can be used by the Deployment. |
| deployment.filesyste m.usage | Bytes | deployment.filesystem.usa ge | userId, cluster, namespace, type, and app | The used size of the file system of the Deployment. |
| deployment.filesyste m.utilization | % | deployment.filesystem.utili zation | userId, cluster, namespace, type, and app | The file system usage of the Deployment. |

| deployment.memory.l imit | Bytes | deployment.memory.limit | userId, cluster, namespace, type, and app | The maximum size of memory that can be allocated to the Deployment. |
|---|---|---|---|---|
| deployment.memory. request | Bytes | deployment.memory.reque st | userId, cluster, namespace, type, and app | The minimum amount of memory resources requested by the Deployment. |
| deployment.memory. working set _ | Bytes | deployment.memory.worki ng set _ | userId, cluster, namespace, type, and app | The working set memory of the Deployment. |
| deployment.network.r x errors rate _ _ | Bytes/s | deployment.network.rx err _ ors rate _ | userId, cluster, namespace, type, and app | The rate at which receive errors occur in the network of the Deployment. |
| deployment.network.t x errors rate _ _ | Bytes/s | deployment.network.tx err _ ors rate _ | userId, cluster, namespace, type, and app | The rate at which send errors occur in the network of the Deployment. |

### 5.2 View the monitoring data

On the monitoring page of a cloud service, you can view the status of resources and the metrics.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Cloud Service Monitoring**.
4. On the **Cloud Service Monitoring** page, select a cloud service whose monitoring data you
want to view.
5. On the monitoring page of the cloud service, click **Monitoring Charts** in the **Actions**
column of a resource. On the page that appears, you can view the monitoring charts of the resource. You can view the monitoring data of the last 30 days at most.

### 5.3 View alert rules

On the monitoring page of a cloud service, you can view all alert rules of the cloud service in the current resource set and organization.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, click **Cloud Service Monitoring**.
4. On the **Cloud Service Monitoring** page, click a cloud service.
5. On the monitoring page of the cloud service, click **View Alert Rules** in the upper-right
corner.
6. Optional. Find the alert rule whose details you want to view. Click **Details** in the **Actions**
column of the alert rule. In the **Alert Rules/Alert Logs/Faulty Instances** panel, view the
**rule details**, **alert history**, and **faulty resources**.
monitoring

## 6 Kubernetes container monitoring

**monitoring**

You can monitor Kubernetes clusters by monitoring Kubernetes containers. This way, you can understand the health status of your clusters and identify and resolve issues at the earliest opportunity.

**Background information**

You can perform the following operations on Kubernetes clusters by monitoring Kubernetes containers: Monitor and configure alert rules for Kubernetes clusters. Synchronize Kubernetes clusters and display the information about Kubernetes clusters in a list. The information includes the cluster name, cluster ID, health status, and number of nodes. Monitor a single cluster and display the monitoring data in charts, including the metrics related to the CPU, memory, and file system. Configure alert rules for the metrics related to the CPU, memory, and file system of a single cluster.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Container Service Monitoring**.
4. On the **Kubernetes container monitoring** page, view the information about Kubernetes
clusters in the columns of the cluster list, including **Cluster ID / Cluster Name** , **Health**
**status**, **Organization**, **Geography**, and **Number of nodes**.
5. Find the cluster that you want to manage and click its ID. The cluster details page appears.
In the basic information section, view the information about the cluster from the following parameters: **Cluster Name**, **Cluster ID**, **Cluster Type**, **Version**, and **Virtual private**
**network (VPC)**.
On the **Monitoring chart** tab, view the monitoring charts of metrics related to the CPU, memory, and file system of the cluster. You can view the monitoring data generated within the previous **1 hour**, **6 hours**, **12 hours**, **1 day**, **3 days**, **7 days**, and **14 days**, or a custom time range. monitoring On the **Kubernetes container monitoring** page, you can also find the cluster that you want to manage and click **Monitoring chart** in the **Operation** column to go to the **Monitoring chart** tab. On the Monitoring chart tab, you can select **One per line**, **Two in each line**, or **Three per line** from the drop-down list in the upper-right corner to display monitoring charts in different ways. You can click the icon in the upper-right corner of a monitoring chart to open the Add Rule Description panel and create an alert rule. For more information, see Create an alert rule. You can click the icon in the upper-right corner of a monitoring chart to display the monitoring chart in a larger screen. On the **Alarm Rules** tab, view the information about alert rules in the following columns:
**Rule Name**, **Product Name**, **Status**, **Enable**, **Related Resource**, **Alert Condition**
**Description**, and **Notification Contact**.
monitoring On the **Kubernetes container monitoring** page, you can also find the cluster that you want to manage and click **Alarm Rules** in the **Operation** column to go to the **Alarm Rules** tab. On the **Alarm Rules** tab, you can click **Create Alert Rule** to create an alert rule. For more information, see Create an alert rule. On the **Alarm Rules** tab, you can find the alert rule that you want to manage and click a button in the Actions column to manage the alert rule. For more information, see Manage alert rules.

## 7 Alert service

You can manage alert rules, alert history, and alert templates in the Alert Service module of CloudMonitor. You can configure alert rules to specify how CloudMonitor checks monitoring data. If monitoring data triggers the alert rules, CloudMonitor sends alert notifications. When an alert is generated, CloudMonitor records the alert information in the alert history. You can review and analyze the alert history to troubleshoot issues and make predictions. Alert templates simplify the process of creating and maintaining alert rules when you need to manage a large number of cloud resources. This helps you monitor cloud services more efficiently.

### 7.1 Alert history

You can specify filter conditions such as the cloud service, instance, and alert level to view the alert history. You can also export and download the alert history to your on-premises machine for data analysis.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose**Alert Service** > **Alert History**.
4. Optional. On the Alert History page, specify a **cloud service**, **rule ID**, **rule name**,
**instance ID**, or **alert level**, and a time range to filter the alert history that you want to
view.
5. On the Alert History page, perform the required operations. The following table describes
the operations that you can perform.

| Operation | Description |
|---|---|
| View the alert history | On the Alarm History page, view the information about alerts in the columns, including Product Name, Fault instance, Time of occurrence, Rule Name, Status, Grade, and Notification Object. Find an alert record that you want to view and click the rule name in the Rule Name column to view the details of the alert rule. Note By default, you can query the alert history of the previous two days. |

| Create a report export task and download a report on the alert history | i. On the Alert History page, click the icon in the upper- right corner. ii. In the Export Tasks dialog box, configure the Time selection and Task Name parameters and click OK. iii. In the left-side navigation pane, click Export Report. On the Report Export page, click the Alert History tab. iv. On the Alert History tab, find the export task that you created and click Download Report Task in the Operation column. v. In the Download Report Task message, click OK. Note The downloaded report is in the .xlsx format. You can find the downloaded report in the default download directory of your browser. |
|---|---|

### 7.2 Alert rules

You can configure alert rules for host monitoring metrics and instances in cloud service monitoring. You can apply an alert rule to all resources, an application group, or an instance. Alert Service sends alert notifications to contacts by using emails, DingTalk messages, and webhook URLs.

#### 7.2.1 Create an alert rule

You can create alert rules for cloud services that are connected to CloudMonitor, such as Elastic Compute Service (ECS). If the threshold that is specified in an alert rule is reached or exceeded, an alert is triggered and an alert notification is sent to the related contacts.

**Background information**

If you want to apply an alert rule to instances in an application group, make sure that the application group is created and the instances are added to the application group. For more information, see Create an application group and Manage application groups. During the validity period of an alert rule, CloudMonitor checks whether the metric values of cloud services exceed the specified thresholds at the default monitoring frequency. If a metric value exceeds the threshold, CloudMonitor sends alert notifications to the specified contacts or alert processing platforms. For ApsaraDB RDS that uses the old link, the monitoring frequency varies from every 60 to 300 seconds. For all other cloud services, the minimum monitoring frequency is set to once per minute.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Rule**. On the **Alert Rules**
page, click **Create Alert Rule**.
4. In the **Create alarm rules** panel, configure the parameters. The following table describes
the parameters in an alert rule.

| Parameter | Description |
|---|---|
| Cloud product selection | The cloud service that you want to monitor. |
| Resource scope | The resources that are associated with the alert rule. Valid values: Instance dimension: Select one or more instances in the resource set of the current organization. Resource set dimension: Select a resource set in the current organization and region. Application grouping dimensions: Select an application group in the current organization and region. All resources: By default, you cannot select this value. |
| Resource Selection | The resources to be associated with the alert rule. Select one or more resources based on the selected resource type. |
| Alarm rule description | The trigger conditions of the alert rule. If the metrics meet the specified conditions, the alert rule is triggered. To configure the trigger conditions, perform the following steps: i. Click Add Rule Description. ii. In the Add Rule Description panel, specify the rule name, metric, and threshold and alert level. For more information, see the Parameters in the rule description section of this topic. iii. Click OK. |
| Silent Channel cycle | The interval at which CloudMonitor resends an alert notification if the alert is not cleared. Valid values: 5 Minutes, 15 Minutes, 30 Minutes, 1 hour, 3 hours, 6 hours, 12 hours, and 24 hours. CloudMonitor sends an alert notification when a metric value reaches the threshold. If the metric value reaches the threshold again within the mute period, CloudMonitor does not resend an alert notification. If the alert is not cleared after the mute period ends, CloudMonitor resends an alert notification. For example, if you set the Silent Channel cycle parameter to 12 hours and the alert is not cleared 12 hours after the alert is triggered for the first time, CloudMonitor resends an alert notification. |
| Effective time | The period during which the alert rule is effective. CloudMonitor checks whether the monitoring data can trigger the alert rule only during the effective period. |

| Alert Callback | The callback URL to which CloudMonitor sends alert notifications by initiating an HTTP request. The alert callback is implemented based on the webhook mechanism. If the system detects system events or custom events, CloudMonitor sends alert notifications to the URL by initiating an HTTP request. For more information, see the "Notification by using webhook URLs" section of the Notification methods supported by CloudMonitor topic. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
|---|---|
| Method to handle alerts when no monitoring data is found | The method that is used to handle alerts when no monitoring data is found. Valid values: Do not do anything (default): If no monitoring data is found for the specified metric, the alert rule does not trigger any action. This option is suitable for monitoring scenarios that are not sensitive to the no-data state. Send no data alarm: If the metric has no data for five consecutive cycles, CloudMonitor triggers an alert and sends an alert notification through the configured notification methods, such as text messages, emails, and webhooks. This option is suitable for scenarios where monitoring interruptions or data loss need to be detected in a timely manner. Important Instance deletion also triggers a no-data alert. |
| Alert contact | The user groups or users to which alert notifications are sent. CloudMonitor can send alert notifications by email or DingTalk. For more information, see the "Notification by using DingTalk and email" section of the Notifications methods supported by CloudMonitor topic. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

5. Click **Confirm**.

**Parameters in the rule description**

| Parameter | Description |
|---|---|
| Rule Name | The name of the alert rule. |
| Metric | The metric of the cloud service that you want to monitor. For more information about the metrics of cloud services, see "Metrics". |

| Comparison | The comparison condition between the monitoring data and alert threshold. Valid values: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, and Year-on-year decline at the same time yesterday. |
|---|---|
| Threshold and Alert Level | Valid values of the alert level: Critical, Warning, and Info. Valid values of the aggregate value type: Average, Minimum, and Maximum. Valid values of the monitoring period: continuous, 5 cycles (1 cycle =60S), 10 cycles (1 cycle =60S), 15 cycles (1 cycle =60S), 30 cycles (1 cycle =60S), and 60 cycles (1 cycle =60S). Valid values of the comparison relationship between the monitoring data and alert threshold: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, Year-on-year decline at the same time yesterday, Increase compared with the last monitoring cycle, Decline compared with the last monitoring cycle. You also need to set an alert threshold and a trigger count. An alert is generated if the monitoring data reaches the specified threshold for the specified number of times at a specific interval. |

**Sample alert rule**

Create an alert rule named example to monitor the CPU utilization of ECS instances. When the CPU utilization is equal to or greater than 70% three times within five intervals, an alert of the Critical level is generated. The following figure shows the parameter settings in the rule description.

#### 7.2.2 Manage alert rules

You can modify, disable, enable, and delete alert rules on the **Alert Rules** page in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Rule**.
4. On the **Alert Rules** page, find the alert rule that you want to manage and perform the
required operations. The following table describes the operations that you can perform on alert rules.

| Operation | Procedure |
|---|---|
| View the details of an alert rule | Find the alert rule that you want to manage and clickD etails in the Actions column. In the Alert Rules/Alert Logs/Faulty Instances panel, view the details of the alert rule. The rule details include the service name, alert status, metric, and associated resources. |

| Check the validity of an alert rule | Find the alert rule that you want to check and clickC heck in the Validity column. You can view the check result in the Validity column. Note If the check result is abnormal, click Detection Result. In the panel that appears, you can view the results of Alert Rule Execution Anomaly, Alert Rule Loading, Invalid Alert Rule Detection, and Alert Rule Callback Detection. Click Re-check to re-check the validity of the alert rule. |
|---|---|
| Modify an alert rule | i. Find the alert rule that you want to manage and clickE dit in the Actions column. ii. In the Modify alarm rules panel, modify the settings of the following parameters: Alarm Rule Description, Silence Channel cycle, Effective time, Alarm callback, No data processing method, and Alarm Contact. For more information about the parameters, see Create an alert rule. iii. After you modify the alert rule, click OK. |
| Disable one or more alert rules | If you stop a cloud service for maintenance or upgrade purposes, you can disable the alert rules that are associated with the cloud service. This way, manual operations on the service do not trigger CloudMonitor to send alert notifications. Note Make sure that the alert rule is in the Normal state before you disable the alert rule. Disable a single alert rule a. On the Alert Rules page, find the alert rule that you want to disable, click the icon in the Actions column, and then click Disable. b. In the Disable alarm rules message, click OK. Disable multiple alert rules at a time a. On the Alert Rules page, select the check boxes before the alert rules that you want to disable and click Disable in the lower-left corner of the alert rule list. b. In the Disable alarm rules message, click OK. |

| Enable one or more alert rules | After you maintain or upgrade a cloud service, you can enable all disabled alert rules. Enable a single alert rule a. Find the alert rule that you want to enable and clickE nable in the Actions column. b. In the Enable alarm rules message, click OK. Enable multiple alert rules at a time a. Select the check boxes before the alert rules that you want to enable and click Enable in the lower-left corner of the alert rule list. b. In the Enable alarm rules message, click OK. |
|---|---|
| Delete one or more alert rules | Delete a single alert rule a. Find the alert rule that you want to delete, click the icon in the Actions column, and then click Delete. b. In the Delete Alert Rule message, click OK. Delete multiple alert rules at a time a. Select the alert rules that you want to delete and clickD elete in the lower-left corner of the alert rule list. b. In the Delete Alert Rule message, click OK. |
| Export and download an alert rule report | i. On the Alert Rules page, click the icon in the upper-right corner. ii. In the Export task dialog box, specify the task name. iii. Click OK. iv. In the left-side navigation pane, click Export Report. On the Report Export page, click the Alarm Rules tab. v. On the Alert Rules tab, find the report that you want to manage and click Download Report Task in the Operation column. vi. In the Download Report Task message, click OK. |

#### 7.2.3 Notification methods supported by CloudMonitor

## CloudMonitor

CloudMonitor can send alert notifications by using DingTalk, email, webhook URLs, and the Apsara Uni-manager Operations Console.

**Notification by using DingTalk and email**

**Configure alert contacts**

When you create or modify an alert rule, select one or more contacts or contact groups from the Alarm Contact drop-down list. For more information, see Create an alert rule.

**Enable notification by using DingTalk or email for the**

**selected users**

You must enable notification by using DingTalk or email for the selected users or users in the selected user groups, and configure the corresponding DingTalk keys and email addresses of the users. You can create or modify the DingTalk keys and email addresses, and enable the notification methods when you create or modify users. For more information, see "Create a user" in the documentation of the Apsara Uni-manager Management Console. The message body in an email-based notification contains a notification of an alert, a log, or an event. The following sample templates are provided:

**Sample template for an alert notification**

HTML

```xml
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <body>
```

```xml
        <style>table{font-size:14px;}</style>
        <div align="center">
        <font color="#525252">
        <table border="0" style="border:5px solid #F2F2F2;" cellspacing="2"
cellpadding="2" width="900" style="table-layout:fixed">
            <tr bgcolor="#D1D1D1">
                <th align="left" style="font-size:23px;">Alert information</th>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert rule name: {{ .ruleName }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Service: {{ .metricProject }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">
                    <b>Instance ID: </b>{{ .instanceId }}
                </td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">
                    <b>Instance name: </b>{{ .instanceName }}
                </td>
            </tr>
   ASCM_PRODUCT_EXTRA_INFO_PLACE_HOLDER
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert level: {{ .level }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Time when the alert is triggered: {{ .time }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Monitoring metric: {{ .metricName }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Evaluation rule: {{ .expression }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert threshold: {{ .value }}</td>
            </tr>
        </table>
        <br/>
```

```xml
        <p>This message is automatically sent by CloudMonitor. Do not reply.</p>
    </body>
</html>
```

**Sample template for a log notification**

HTML

```xml
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <body>
        <style>table{font-size:14px;}</style>
        <div align="center">
        <font color="#525252">
        <table border="0" style="border:5px solid #F2F2F2;" cellspacing="2"
cellpadding="2" width="900" style="table-layout:fixed">
            <tr bgcolor="#D1D1D1">
                <th align="left" style="font-size:23px;">Log alert</th>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert rule name: {{ .ruleName }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert name: {{ .alertName }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Evaluation rule: {{ .expression }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert threshold: {{ .value }}</td>
            </tr>
   ASCM_PRODUCT_EXTRA_INFO_PLACE_HOLDER
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert level: {{ .level }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Time when the alert is triggered: {{ .time }}</td>
            </tr>
        </table>
        <br/>
        <p>This message is automatically sent by CloudMonitor. Do not reply.</p>
    </body>
</html>
```

**Sample template for an event notification**

HTML

```xml
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
    <body>
        <style>table{font-size:14px;}</style>
        <div align="center">
        <font color="#525252">
        <table border="0" style="border:5px solid #F2F2F2;" cellspacing="2"
cellpadding="2" width="900" style="table-layout:fixed">
            <tr bgcolor="#D1D1D1">
                <th align="left" style="font-size:23px;">Event alert</th>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert rule name: {{ .ruleName }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert name: {{ .alertName }}</td>
            </tr>
   ASCM_PRODUCT_EXTRA_INFO_PLACE_HOLDER
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Alert level: {{ .level }}</td>
            </tr>
            <tr>
                <td align="left" style="font-family:Microsoft YaHei; size=5" style
="WORD-WRAP:break-word">Time when the alert is triggered: {{ .time }}</td>
            </tr>
        </table>
        <br/>
        <p>This message is automatically sent by CloudMonitor. Do not reply.</p>
    </body>
</html>
```

The message body in a DingTalk-based notification contains a notification of an alert, a log, or an event. The following sample templates are provided:

**Sample template for an alert notification**

HTML

```
<font color=#778899 face="Microsoft YaHei">Service</font>: {{ .metricProject }} & ensp;&ensp; <font color=#778899 face="Microsoft YaHei">Level</font>: <font color= {{ .color }} face="SimHei">{{ .level }}</font> <font color=#778899 face="Microsoft YaHei">Metric</font>: {{ .metricName }} &ensp ;&ensp; <font color=#778899 face="Microsoft YaHei">Alert threshold</font>: {{ .v alue }} <font color=#778899 face="Microsoft YaHei">Instance ID</font>:&ensp;{{ .instanceI d }} <font color=#778899 face="Microsoft YaHei">Instance name</font>:&ensp;{{ .instanc eName }} <font color=#778899 face="Microsoft YaHei">Alert rule name</font>: {{ .ruleName }
```

`}`

```
ASCM_PRODUCT_EXTRA_INFO_PLACE_HOLDER <font color=#778899 face="Microsoft YaHei">Monitoring metric</font>: {{ .metricNa me }} <font color=#778899 face="Microsoft YaHei">Evaluation rule</font>: {{ .expression
```

`}}`

```
<font color=#778899 face="Microsoft YaHei">Time when the alert is triggered</font>: {{ .time }}
 *****
 >This message is sent by the Apsara Uni-manager Management Console. Handle the a
lert at the earliest opportunity.
```

**Sample template for a log notification**

HTML

```
<font color=#778899 face="Microsoft YaHei">Log alert</font>
 *****
<font color=#778899 face="Microsoft YaHei">Service</font>: {{ .product }} &ensp;& ensp; <font color=#778899 face="Microsoft YaHei">Level</font>: <font color={{ .co lor }} face="SimHei">{{ .level }}</font> <font color=#778899 face="Microsoft YaHei">Alert rule name</font>: {{ .ruleName }
```

`}`

```
<font color=#778899 face="Microsoft YaHei">Evaluation rule</font>: {{ .expression
```

`}}`

```
<font color=#778899 face="Microsoft YaHei">Alert threshold</font>: {{ .value }} <font color=#778899 face="Microsoft YaHei">Alert name</font>: {{ .alertName }} <font color=#778899 face="Microsoft YaHei">Time when the alert is triggered</font>: {{ .time }}
 *****
 >This message is sent by the Apsara Uni-manager Management Console. Handle the a
lert at the earliest opportunity.
```

**Sample template for an event notification**

HTML

```
<font color=#778899 face="Microsoft YaHei">Event alert</font>
 *****
<font color=#778899 face="Microsoft YaHei">Service</font>: {{ .product }} &ensp;& ensp; <font color=#778899 face="Microsoft YaHei">Level</font>: <font color={{ .co lor }} face="SimHei">{{ .level }}</font> <font color=#778899 face="Microsoft YaHei">Alert rule name</font>: {{ .ruleName }
```

`}`

```
ASCM_PRODUCT_EXTRA_INFO_PLACE_HOLDER <font color=#778899 face="Microsoft YaHei">Alert name</font>: {{ .alertName }} <font color=#778899 face="Microsoft YaHei">Time when the alert is triggered</font>: {{ .time }}
 *****
 >This message is sent by the Apsara Uni-manager Management Console. Handle the a
lert at the earliest opportunity.
```

**Configre ANS**

**Important**

After you select the alert contacts or contact groups and enable notification by using DingTalk and email for the contacts, you also need to check the configurations and configure Application Naming Service (ANS). CloudMonitor can use these methods to send alert notifications only after you configure the email addresses and DingTalk keys. i. Check whether the ANS cluster is deployed. a. Log on to the Apsara Infrastructure Management Console. b. In the left-side navigation pane, choose **Operations** > **Cluster Operations**. c. On the **Cluster Operations** page, enter ans in the **Cluster** field to search for the ans cluster. d. Click the cluster name to go to the details page of the ans cluster. e. On the **Cluster Configuration** page, click **Edit** in the upper-right corner. Then, find the **tag.conf** file and check the ANS version. Check whether ANS is updated to the latest version, which is more stable and has fewer issues. ii. Connect ANS to an external network. Contact technical support to connect the ansApi.aliyunNotifyService# container to the corresponding DingTalk server or email server. The container resides in a classic network in Apsara Stack. iii. Check whether the service is normal. a. On the details page of the ans cluster, find the **Service Instances** section. b. In the **Service Instances** section, find the **ansApi** service and click **Details** in the
**Actions** column to go to the service details page.
c. On the service details page, find the **ansApi**.**aliyunNotifyService#** component and click **Details** in the **Actions** column. On the **Server Role Dashboard** page**,** click
**Terminal** in the **Actions** column of the **Machine Information** section.
d. On the page that appears, run the following command to check whether the service is normal: Shell

```bash
docker exec -it `docker ps|awk '/aliyunNotifyService/{print $1}'` bash cd /apsara/ans/
# Check whether the service is normal.
ps -ef | grep notifier | grep -v grep netstat -antp | grep notifier | grep 8010
```

iv. Configure and check email addresses and DingTalk keys. Contact technical support to configure and check email addresses and DingTalk keys.

**Important**

To configure a DingTalk chatbot, we recommend that you configure the DingTalk chatbot with a signature to enhance security.

**Notification by using webhook URLs**

CloudMonitor sends POST requests to the domain names that are configured by users. Therefore, you must configure a service to receive POST requests sent by CloudMonitor.

**Configure a service**

If you want to use your platform to handle alerts and have a service to receive requests sent by CloudMonitor, you can configure alert callback settings when you create or modify an alert rule. For more information, see Create an alert rule.

**Important**

You must specify a domain name instead of an IP address when you configure the alert callback settings. The suffix of the domain name must be the same as the value of the internet_domain environment variable in the cms.cloudmonitor container. The URL that you specify must be connected to the networks of the aliyunNotifyService# container of CloudMonitor and the primary and secondary data centers.

**Request method**

By default, POST requests are sent. The value of the Content-Type field is fixed to application/x-www-form-urlencoded by default.

**Request parameters (Apsara Stack v3.16.2 SP002 and later)**

If the alert rule is triggered, CloudMonitor sends an alert notification to the callback URL by using the POST method over HTTP or HTTPS. The following table describes the parameters that are configured in the POST request.

**Apsara Stack v3.16.2 SP022 and earlier**

| Parameter | Data type | Description |
|---|---|---|
| userId | String | The user ID. |
| alertName | String | The alert name. |
| timestamp | String | The time when the alert is triggered. The value is a timestamp. |
| alertState | String | The alert state. Valid values: ALARM, OK, and INSUFFICIENT DATA. _ |
| curlLevel | String | The severity level of the alert. Valid values: CRITICAL WARN INFO |
| curLevelDisplay | String | The displayed level of the alert. |
| dimensions | String | The object for which the alert is triggered. Example: {userId=110803419679****, instanceId=i- 8psdh7l6lphbn10l****}. |
| expression | String | The alert conditions. |
| curValue | String | The value of the metric when the alert is triggered or cleared. |
| metricName | String | The name of the alert metric. For more information about metrics, see Metrics. |
| metricProject | String | The name of the cloud service. The value of this parameter is the same as the value of the namespace parameter. For more information, see "Cloud service monitoring". |

| namespace | String | The namespace of the cloud service. The value of this parameter is the same as the value of the metricProject parameter. For more information, see "Cloud service monitoring". |
|---|---|---|

**Apsara Stack v3.16.2 SP023 to v3.16.2 SP029**

| Parameter | Data type | Description |
|---|---|---|
| userId | String | The user ID. |
| alertName | String | The alert name. |
| timestamp | String | The time when the alert is triggered. The value is a timestamp. |
| alertState | String | The alert state. Valid values: ALARM, OK, and INSUFFICIENT DATA. _ |
| curlLevel | String | The severity level of the alert. Valid values: CRITICAL WARN INFO |
| curLevelDisplay | String | The displayed level of the alert. |
| expression | String | The alert conditions. |
| curValue | String | The value of the metric when the alert is triggered or cleared. |
| metricName | String | The name of the alert metric. For more information about metrics, see Metrics. |
| metricProject | String | The name of the cloud service. The value of this parameter is the same as the value of the namespace parameter. For more information, see "Cloud service monitoring". |
| namespace | String | The namespace of the cloud service. The value of this parameter is the same as the value of the metricProject parameter. For more information, see "Cloud service monitoring". |

| dimensionsOrigin al | String | The object for which the alert is triggered. This is the original dimension. Example: {userId=110803419679****, instanceId=i- 8psdh7l6lphbn10l****}. |
|---|---|---|
| dimensions | String | The object for which the alert is triggered. This is the processed dimension. Example:" {\"instanceld\": \"r-***\", \"nodeId\": \"xxxx\", \"userId\": \"114981*****\"}". |
| appkey | String | The ID of the resource set to which the instance belongs. |
| appName | String | The name of the resource set to which the instance belongs. |
| sourceLevel | String | The original level of the alert rule. Example: WARN. |

**Apsara Stack v3.16.2 SP030 and later**

| Parameter | Data type | Description |
|---|---|---|
| userId | String | The user ID. |
| alertName | String | The alert name. |
| timestamp | String | The time when the alert is triggered. The value is a timestamp. |
| alertState | String | The alert state. Valid values: ALARM, OK, and INSUFFICIENT DATA. _ |
| curlLevel | String | The severity level of the alert. Valid values: CRITICAL WARN INFO |
| curLevelDisplay | String | The displayed level of the alert. |
| expression | String | The alert conditions. |
| curValue | String | The value of the metric when the alert is triggered or cleared. |

| metricName | String | The name of the alert metric. For more information about metrics, see Metrics. |
|---|---|---|
| metricProject | String | The name of the cloud service. The value of this parameter is the same as the value of the namespace parameter. For more information, see "Cloud service monitoring". |
| namespace | String | The namespace of the cloud service. The value of this parameter is the same as the value of the metricProject parameter. For more information, see "Cloud service monitoring". |
| dimensionsOrigin al | String | The object for which the alert is triggered. This is the original dimension. Example: {userId=110803419679****, instanceId=i- 8psdh7l6lphbn10l****}. |
| dimensions | String | The object for which the alert is triggered. This is the processed dimension. In particular, the notification for the "SLB metric health check - Number of unhealthy backend ECS instances" metric contains the IP address information of the ECS instance. Example: {userId=110803419679****, instanceId=lb- 8psdh7l6lphbn10l****,rips=10.11.1.****}. |
| appkey | String | The ID of the resource set to which the instance belongs. |
| appName | String | The name of the resource set to which the instance belongs. |
| sourceLevel | String | The original level of the alert rule. Example: WARN. |

**Troubleshooting**

After you configure an alert callback, you can contact technical support to troubleshoot the issue if no callback is received.

**Notification by using the Apsara Uni-manager Operations**

**Console**

By default, CloudMonitor receives alert notifications in the Apsara Uni-manager Operations Console. CloudMonitor can use the Apsara Uni-manager Operations Console to send alert notifications. To obtain more information, contact technical support.

### 7.3 Alert templates

#### 7.3.1 Create an alert template

If you want to monitor a large number of resources, you can use the alert template feature. This feature helps you save multiple alert rules on the metrics of various cloud services as a template. You can create or modify alert rules by using alert templates. This prevents repeated workloads of configuring each alert rule.

**Background information**

You must use alert templates together with application groups. You can create an application group first. Then, you can create an alert template and apply the alert template to the application group to create alert rules for the application group. This simplifies the creation and maintenance of alert rules. For more information about how to create an application group, see Create an application group.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Templates**.
4. On the **Alarm Template** page, click **Create an alarm Template**.
5. In the **Create an alarm Template** panel, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Template Name | The name of the alert template. The name can contain letters, digits, and underscores ( ). We recommend that the name be 1 to 30 _ characters in length. |
| Description | Optional. The description of the alert template. We recommend that the description be 1 to 100 characters in length. |
| Clone Template | Optional. The existing alert template that you want to clone. You can modify the configurations of the selected template to create a new alert template. |
| Select Product | The cloud services for which you want to apply the alert template. |

6. Click **Add Rule** to configure an alert rule. The following table describes the parameters of
the alert rule.

| Parameter | Description |
|---|---|
| Rule Name | The name of the alert rule. |
| Metric | The metrics that you want to monitor. For more information about the metrics of cloud services, see the "Metrics" topic. |
| Comparison | The comparison condition between metric data and thresholds. If the metric data exceeds the specified thresholds, the alert rule is triggered. Valid values: >, >=, <, <=, =, !=, Year-on-year increase at the same time yesterday, and Year-on-year decline at the same time yesterday. |

| Threshold and Notification Methods | The conditions, alert thresholds, and alert levels of the alert rule. You can specify multiple alert levels with different conditions. Alert levels: Critical Warn Info Number of times for which the metric data is equal to or greater than the threshold: The number of times determines whether the alert notification is sent. Valid values: 1 Consecutive Cycles 2 Consecutive Cycles 3 Consecutive Cycles 4 Consecutive Cycles 5 Consecutive Cycles 10 Consecutive Cycles 15 Consecutive Cycles 20 Consecutive Cycles |
|---|---|

7. After you add rules for each cloud service, click **Confirm**.

#### 7.3.2 Manage alert templates

On the Alarm Template page, you can modify, clone, export, delete, and apply alert templates.

**Background information**

Alert templates include preset alert templates and custom alert templates. You cannot modify or delete preset alert templates. Alert templates must be used with resource sets and application groups. You can apply alert templates to resource sets or application groups to create alert rules for cloud services. Before you apply an alert template, make sure that the alert template and an application group or a resource set are created. For more information, see Create an alert template, Create an application group, and Create a resource set.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Alert Templates**.
4. On the **Alarm Template** page, select an alert template and perform the required
operations. The following table describes the operations that you can perform on alert templates.

| Operation | Procedure |
|---|---|

| Modify an alert template | i. Find the alert template that you want to modify and click Modification in the Actions column. ii. In the Modify Alarm Template panel, modify the description, Alibaba Cloud services, and rules of the alert template. iii. Click OK. Note You cannot modify preset alert templates. |
|---|---|
| Clone an alert template | You can clone an alert template to copy the template configurations to create a new alert template. i. Find the alert template that you want to clone and clickT emplate Cloning in the Operation column. ii. In the Clone an alarm Template panel, configure the Template Name and Description parameters, select the template to be cloned from the Template Cloning drop-down list, select services from the Product selection drop-down list, and create an alert rule. iii. Click OK. iv. In the Alarm Template Creation/Modification Complete message, click OK or Cancel. Note In this step, you can click OK to apply the alert template to an application group. For more information, see the Apply one or more alert templates to application groups or resource sets operation in this table. In this step, you can click Cancel to cancel the application of the alert template to the application group. |

| Delete one or more alert templates | Warning An alert template cannot be restored after it is deleted. Proceed with caution. Delete a alert template a. Find the alert template that you want to delete and clickD elete in the Actions column. b. In the Delete Alert Template message, click OK. Delete multiple alert templates at a time a. Select the alert templates that you want to delete and click Delete in the lower-left corner of the page. b. In the Delete Alert Template message, click OK. |
|---|---|
| Apply one or more alert templates to application groups or resource sets | Important After you select an alert template and apply the alert template to an application group or a resource set, CloudMonitor deletes the existing alert rules that are created based on the original alert template except for the process monitoring and availability monitoring rules. Then, CloudMonitor creates new alert rules based on the new alert template. We recommend that you apply an alert template to up to five application groups or resource sets. Otherwise, the alert template may fail to take effect for some application groups or resource sets. Apply an alert template to application groups or resource sets a. Find the alert template that you want to apply, click the icon in the Actions column, and then click Application alarm Template. b. In the Apply Template to Grouping dialog box, configure the Overwrite/Append, Resource Set, Resource selection, Channel Silence Period, Effective time, Alarm callback, and Alarm Contact Group parameters. c. Click OK. d. In the Apply Template to Group message, click OK. Apply multiple alert templates to application groups or resource sets a. Select the alert templates that you want to apply and click Batch Application Template in the lower-left corner. b. In the Apply Template to Grouping dialog box, configure the Overwrite/Append, Resource Set, Resource selection, Channel Silence Period, Effective time, Alarm callback, and Alarm Contact Group parameters. c. Click OK. d. In the Apply Template to Group message, click OK. |

| Create a report export task and download a report on alert templates | i. On the Alarm Template page, click the icon in the upper-right corner. ii. In the Export Tasks dialog box, set the Task Name parameter . iii. Click OK. iv. In the left-side navigation pane, click Export Report. On the Report Export page, click the Alarm Template tab. v. On the Alarm Template tab, find the report that you want to download and click Download Report Task in the Operation column. vi. In the Download Report Task message, click OK. Note The report is in the .xlsx format. You can find the downloaded report in the default download directory of your browser. |
|---|---|

### 7.4 Use the initiative alerting feature

**feature**

The initiative alerting feature allows you to configure alert rules for the key metrics of the specified cloud services with a few clicks. This way, you can quickly create an alert system for cloud services to monitor the key metrics of cloud services, and handle exceptions at the earliest opportunity.

**Important**

To use the initiative alerting feature, you must install Apsara Stack V3.16.2r-cms-SP013.

**Background information**

The initiative alerting feature can be enabled or disabled for a specific cloud service. After you enable the initiative alerting feature for a cloud service, all the predefined alert rules of the cloud service are enabled by default. CloudMonitor automatically creates an alert system for the specified metrics. After you enable the initiative alerting feature for a cloud service, the alert rules of the cloud service are applied to both the existing resources and resources that are subsequently created in the current level-1 organization. After you enable the initiative alerting feature for a cloud service, you can create, modify, delete, or disable alert rules for the cloud service based on your business requirements. If an alert rule is triggered after you enable the initiative alerting feature for a cloud service, an alert is generated. By default, CloudMonitor sends alert notifications to the alert contacts specified for your Apsara Stack account. After you disable the initiative alerting feature for a cloud service, all alert rules of the cloud service are disabled.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Alert Service** > **Initiative Alerting**.
4. On the page that appears, perform the operations that are described in the following table.

| Operation | Procedure |
|---|---|
| Enable the initiative alerting feature | i. Find the cloud service for which you want to enable the initiative alert feature and click the icon in the Initiative Alert column. : indicates that the initiative alerting feature is disabled. : indicates that the initiative alert feature is enabled. ii. In the message that appears, click Enable. Important After the initiative alerting feature is enabled, the predefined alert rules of the cloud service are enabled and added to the Alarm Rules page. iii. Click the icon in front of the cloud service to view the alert rules of the cloud service. |
| Disable the initiative alerting feature | i. Find the cloud service for which you want to disable the initiative alert feature and click the icon in the Initiative Alert column. ii. Click Close. Important After the initiative alerting feature is disabled, the alert rules of the cloud service are removed from the Alarm Rules page. |
| Create alert rules | i. Click the icon in front of the cloud service for which the initiative alert feature is enabled. ii. Click Create Alert Rule. iii. In the Create Alert Rule panel, set the Rule Name, Metric, and Threshold and Alarm Level parameters. For more information about how to configure an alert rule, see Create an alert rule. iv. Click OK. The Create Alert Rule panel appears. v. Configure the Silent Channel cycle, Effective time, Alarm callback, No data processing method, and Alarm Contact parameters. For more information, see Create an alert rule. vi. Click Confirm. |

| Enable or disable an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Perform the following operations to enable or disable an alert rule: Find the alert rule that is in the Enable state and click Disable in the Operation column. In the message that appears, click Disable. After you disable the alert rule, the corresponding alert rule on the Alarm Rules page is also disabled. Find the alert rule that is in the Disable state and click Enable in the Operation column. In the message that appears, click Enable. After you enable the alert rule, the corresponding alert rule on the Alarm Rules page is also enabled. |
|---|---|
| Modify an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Perform the following operations to modify a single alert rule or modify multiple alert rules at a time: Modify a single alert rule a. Find the alert rule that you want to modify and clickE dit in the Operation column. b. In the Modify alarm rules panel, modify the alert rule based on your business requirements. c. Click Confirm. Modify multiple alert rules at a time a. Select the alert rules that you want to modify. b. Click Batch Edit below the rule list. c. In the Batch Edit dialog box, configure the parameters, including Channel Silence Period, Effective time, Alarm callback, No data processing method, and Alarm Contact Group. d. Click Confirm. |
| Delete an alert rule | i. Click the icon before the name of the cloud service for which the initiative alerting feature is enabled. ii. Find the alert rule that you want to delete and clickD elete in the Operation column. Important After the alert rule is deleted, the corresponding alert rule on theA lert Rules page is deleted. The deletion cannot be rolled back. Proceed with caution. |

## 8 Statistical analysis

You can use CloudMonitor to analyze the monitoring data of all supported cloud services in a specified organization.

### 8.1 Sort monitoring data

You can use CloudMonitor to sort and analyze the monitoring data of supported cloud services in a specific organization.

**Limits**

CloudMonitor allows you to sort data of the top 1,000 instances of a cloud service in an organization. Data computing fails if the number of instances exceeds this limit.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Statistical Analysis** **>** **Sorting****.**
4. On the **Monitoring Sort** page, select a cloud service and specify the **Indicator Name**,
**Monitoring Sort**, **Indicator Aggregation Value**, and **Quantity** parameters.
**Monitoring Sort**: You can set this parameter to **Ascending** or **Descending**. If
you set this parameter to **Ascending**, the monitoring data is sorted in ascending order. If you set this parameter to **Descending**, the monitoring data is sorted in descending order.
**Indicator Aggregation Value**: You can set this parameter to sort the average,
minimum, or maximum value of the specified metric of instances.
**Quantity**: You can set this parameter to 10, 50, 100, or 200 to display the top
10, top 50, top 100, or top 200 monitoring data records.
5. Optional. In the upper-right corner, click **Report Export** to go to the **Product Data**
**Analysis** page. On the **Product Data Analysis** page, configure custom settings to export
a report.

### 8.2 Data subscription

By creating a data subscription task, you can view the data in the current level-1 organization.

**Limits**

You can create data subscription tasks, and consume and view the data subscribed from Simple Log Service (SLS). You can create a data subscription task only for a level-1 organization. If you have multiple level-1 organization, you must create a subscription task for each level-1 organization.

**Create a data subscription task**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Statistical Analysis** **>** **Data Subscription****.**
4. Click **Create a subscription**. In the **Create a subscription** panel, configure the
parameters in the **Basic configuration** and **SLS configuration** sections. The following table describes the parameters.

| Category | Parameter | Description |
|---|---|---|
| Basic configuration | Task name | The name of the data subscription task. |
|   | Time range | By default, the data subscription task starts from the time when the task is created. |
|   | Data range | All products /indicators: Subscribes to the metric data of all cloud services that are connected to CloudMonitor. Some products/indicators: Subscribes to the metric data of the selected cloud services. |

|   | Product/indicato r selection | Note This parameter is required only when you set Data range to Some products/indicators. Click Add Entry to configure metrics. You can add multiple entries. Cloud product selection: Select the cloud service to which you want to subscribe. Metric scope: All indicators: subscribes to all metrics of the selected cloud service. Some indicators: subscribes to the selected metrics. Indicator selection: Select the metrics to which you want to subscribe. Note This parameter is required only when you set Metric scope to Some indicators. |
|---|---|---|
| SLS configuration | Obtain the SLS configuration address | Click the link to go to the SLS page to obtain the SLS configuration. |
|   | slsProject | The project name. |
|   | slsLogstore | The Logstore name. Note You can create only one data subscription task for an SLS Logstore. |
|   | SlsAk | The AccessKey ID of the level-1 organization. |
|   | SlsSk | The AccessKey secret of the level-1 organization. |

To obtain the AccessKey ID and AccessKey secret of the level-1 organization, perform the following steps: a. Log on to the Apsara Uni-manager Management Console. b. Choose **Enterprise > Resources > ***************. Select the organization, and click
**Management Accesskey** on the right side of the **Basic Information** section. In the
**Management AccessKey** dialog box, you can view the AccessKey ID and AccessKey
secret of the organization.
5. After you complete the configurations, click **OK**. The data subscription task is created.
You can create five data subscription tasks at most. If you need to create more tasks, contact the Apsara Stack technical support.

**Manage data subscription tasks**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Statistical Analysis** **>** **Data Subscription****.**
4. On the **Data subscription** page, view the created data subscription tasks.
5. Modify a task: Find the task that you want to modify and click **Edit** in the **Actions** column.
You can modify the task name and data range.
6. Delete a task: Find the task that you want to delete and click **Delete** in the **Actions**
column.
7. Disable a task: Find the task that you want to disable and click **Disable** in the **Actions**
column.
8. Enable a task: Find the task that you want to enable and click **Enable** in the **Actions**
column.

**View SLS data**

1. On the **Data subscription** page, view the Logstore and project of your data subscription
task.
2. Log on to the Apsara Uni-manager Management Console.
3. In the top navigation bar, choose **Products** > **Storage** > **Log Service**.
4. In the project list on the **Log Service** page, click the name of the project obtained in **Step**
**1**.
5. On the page of the project, click the name of the **Logstore** obtained in **Step 1** to view the
subscribed data.

## 9 Event monitoring

The Event Monitoring module provides a unified portal for you to query and manage system events of CloudMonitor, Hybrid Disaster Recovery, and Elastic Compute Service. You can view the status of the cloud services and receive alert notifications. This helps you troubleshoot business exceptions at the earliest opportunity.

### 9.1 System events

#### 9.1.1 System events of cloud services

This topic describes the cloud services that are supported by CloudMonitor and their system events. For more information about the event metrics, see Event monitoring metrics of cloud services.

| Service | System event |
|---|---|
| CloudMonitor | Agent Status Stopped _ _ Agent Status Running _ _ |

**HDR**

| Service | System event |
|---|---|
| Hybrid Disaster Recovery (HDR) | PrimarySiteVpc:Deleted SecondarySiteVpc:Deleted PrimarySiteNetwork:Deleted SecondarySiteNetwork:Deleted PrimarySecurityGroup:Deleted SecondarySecurityGroup:Deleted SecurityGroup:Inconsistency ProductSiteNetwork:Inconsistency DrSiteNetwork:Inconsistency ProductSiteStorage:Inconsistency DrSiteStorage:Inconsistency PrimarySiteComputation:Inconsistency DrSiteComputation:Inconsistency ReplicationGroup:Inconsistency ReplicationPair:Inconsistency Gateway:Inconsistency ShadowEcs:Inconsistency |

**Backup Management Platform**

| Service | System event |
|---|---|
| Backup Management Platform | BackupPlan RecoveryTask MigratePlan LICENSE |

**ROS**

| Service | System event |
|---|---|
| Resource Orchestration Service (ROS) | Stack:StatusChange StackResource:StatusChange StackGroup:OperationStatusChange |

**ApsaraDB RDS**

| Service | System event |
|---|---|
| ApsaraDB RDS | Instance:HASwitch |

**ECS**

| Service | System event |
|---|---|
|   | Disk:ConvertToPostpaidCompleted Disk:DiskOperationCompleted Disk:ErrorDetected:Executed Disk:ErrorDetected:Executing Disk:OverduePaymentRelease Disk:Stalled:Executed Disk:Stalled:Executing Instance:AutoReactivateCompleted Instance:BurstablePerformanceRestricted Instance:InstanceFailure.PerformanceImpact:Executed Instance:InstanceFailure.PerformanceImpact:Executing Instance:InstanceFailure.Reboot:Executed Instance:InstanceFailure.Reboot:Executing Instance:LiveMigrationAcrossDDH |

|   | Instance:PerformanceModeChange Instance:PreemptibleInstanceInterruption Instance:Security.TpmAlert:Executed Instance:Security.TpmAlert:Executing Instance:StateChange |
|---|---|
| Elastic Compute Service (ECS) | Instance:SystemFailure.Delete:Avoided Instance:SystemFailure.Delete:Executed Instance:SystemFailure.Delete:Executing Instance:SystemFailure.PerformanceImpact:Executed Instance:SystemFailure.PerformanceImpact:Executing Instance:SystemFailure.Reboot:Executed Instance:SystemFailure.Reboot:Executing Instance:SystemFailure.Reboot:Failed Instance:SystemFailure.Redeploy:Avoided Instance:SystemFailure.Redeploy:Canceled Instance:SystemFailure.Redeploy:Executed Instance:SystemFailure.Redeploy:Executing Instance:SystemFailure.Redeploy:Scheduled Instance:SystemFailure.Stop:Executed Instance:SystemFailure.Stop:Executing Instance:SystemMaintenance.IsolateErrorDisk:Avoided Instance:SystemMaintenance.IsolateErrorDisk:Canceled Instance:SystemMaintenance.IsolateErrorDisk:Executed Instance:SystemMaintenance.IsolateErrorDisk:Executing Instance:SystemMaintenance.IsolateErrorDisk:Failed Instance:SystemMaintenance.IsolateErrorDisk:Inquiring Instance:SystemMaintenance.PerformanceImpact:Executed Instance:SystemMaintenance.PerformanceImpact:Executing Instance:SystemMaintenance.ReInitErrorDisk:Avoided Instance:SystemMaintenance.ReInitErrorDisk:Canceled Instance:SystemMaintenance.ReInitErrorDisk:Executed Instance:SystemMaintenance.ReInitErrorDisk:Executing Instance:SystemMaintenance.ReInitErrorDisk:Failed Instance:SystemMaintenance.ReInitErrorDisk:Inquiring Instance:SystemMaintenance.Reboot:Avoided Instance:SystemMaintenance.Reboot:Canceled Instance:SystemMaintenance.Reboot:Executed Instance:SystemMaintenance.Reboot:Executing Instance:SystemMaintenance.Reboot:Failed Instance:SystemMaintenance.Reboot:Inquiring Instance:SystemMaintenance.Reboot:Scheduled Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Avoided |

|   | Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Canceled Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Executed Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Executing Instance:SystemMaintenance.RebootAndIsolateErrorDisk:Inquiring Instance:SystemMaintenance.RebootAndReInitErrorDisk:Avoided Instance:SystemMaintenance.RebootAndReInitErrorDisk:Canceled Instance:SystemMaintenance.RebootAndReInitErrorDisk:Executed Instance:SystemMaintenance.RebootAndReInitErrorDisk:Executing Instance:SystemMaintenance.RebootAndReInitErrorDisk:Inquiring Instance:SystemMaintenance.Redeploy:Avoided Instance:SystemMaintenance.Redeploy:Canceled Instance:SystemMaintenance.Redeploy:Executed Instance:SystemMaintenance.Redeploy:Executing Instance:SystemMaintenance.Redeploy:Inquiring Instance:SystemMaintenance.Redeploy:Scheduled Instance:SystemMaintenance.Stop:Avoided Instance:SystemMaintenance.Stop:Canceled Instance:SystemMaintenance.Stop:Executed Instance:SystemMaintenance.Stop:Executing Instance:SystemMaintenance.Stop:Failed Instance:SystemMaintenance.Stop:Scheduled NetworkInterface:NetworkInterfaceOperateCompleted Snapshot:CreateSnapshotCompleted Instance:VmLivemigrateException Instance:VmDownCausedByNcDown Instance:VmDownEnd Instance:VmPanicEvent Instance:VmCrashEvent |
|---|---|

**ApsaraDB for Redis**

| Service | System event |
|---|---|
| ApsaraDB for Redis | Instance:HASwitch |

**ApsaraDB for MongoDB**

| Service | System events |
|---|---|
| ApsaraDB for MongoDB | Instance:HASwitch |

**PolarDB-X 1.0**

| Service | System events |
|---|---|
| PolarDB-X 1.0 | Instance:HighPhysicalConnectionPoolUsage Instance:CriticalPhysicalConnectionPoolUsage |

#### 9.1.2 View system events

CloudMonitor provides the event monitoring feature to help you query and analyze system events that are generated for various cloud services. The feature allows you to track the use of cloud services.

**Background information**

For more information about the cloud services and system events to which the event monitoring feature is applicable, see System events of cloud services.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** **>** **System Events**.
4. Click the **Event Monitoring** tab. On the **Event Monitoring** tab, select a cloud service, an
event level, an event name, and a time range, and then click **Search**.
5. View the event monitoring chart.
The x-axis indicates the time, and the y-axis indicates the number of events. Move the pointer over the line chart to view the **start time**, **end time**, and **number of**
**events**.
6. In the **System events** section, view the event information. Find the event that you want to
view and click **Details** in the **Operation** column. In the **System events detail** panel, you can view the event details in the **JSON** format.

#### 9.1.3 Create a system event-triggered alert rule

**rule**

You can create alert rules for system events of cloud services. If an exception occurs, an alert is generated and CloudMonitor sends notifications to alert contacts. This helps you analyze and troubleshoot issues.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring** **>** **System Events**.
4. On the **System Event** page, click the **Event-triggered Alert Rules** tab, and then click
**Create Event-triggered Alert Rule**.
5. In the **Create Event-triggered Alert Rule** panel, configure parameters. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Alert Rule Name | The name of the system event-triggered alert rule. The name must be 1 to 30 characters in length and can contain letters, digits, and underscores ( ). _ |
| Product | The cloud service to which the system event-triggered alert rule is applied. For more information about the cloud services that are supported by CloudMonitor, see System events of cloud services. |
| Event Level | The level of the event that triggers alerts. For more information about the event levels that are supported by each cloud service, see Event metrics of cloud services. |
| Event Name | The name of the event that triggers alerts. For more information about the events that are supported by each cloud service, see Event metrics of cloud services. |
| Alert Callback | The callback URL to which CloudMonitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
| Alert Contact | The contact group or contact that receives alert notifications. |

6. Click **OK**.

#### 9.1.4 Manage system event-triggered alert rules

**rules**

You can modify, disable, enable, and delete system event-triggered alert rules on the System Events page in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, choose **Event Monitoring**>**System Events**.
4. On the **System Events** page, click the **Event Alarm rules** tab. On the **Event Alarm**
**rules** tab, find the system event-triggered alert rule that you want to manage and perform
required operations. The following table describes supported operations.

| Operation | Procedure |
|---|---|
| Modify a system event-triggered alert rule | i. Find the system event-triggered alert rule that you want to modify, and click Edit in the Operation column. In the panel that appears, modify the following parameters: Alert Rule Name, Product, Event Level, Event Name, Alert Callback, and Alert Contact. For more information about the parameters, see Create a system event-triggered alert rule. ii. Click OK. |
| Disable one or more system event- triggered alert rules | Note You can disable only event-triggered alert rules in the Enabled state. After you disable an alert rule, the alert rule no longer takes effect. Disable a single system event-triggered alert rule i. Find the system event-triggered alert rule that you want to disable and click Disable in the Operation column. ii. In the message that appears, click OK. Disable multiple system event-triggered alert rules at a time i. Select the system event-triggered alert rules that you want to disable and click Disable in the lower-left corner of the alert rule list. ii. In the message that appears, click OK. |
| Enable one or more system event- triggered alert rules | You can enable system event-triggered alert rules in the Disabled state. Enable a single system event-triggered alert rule i. Find the system event-triggered alert rule that you want to enable and click Enable in the Operation column. ii. In the message that appears, click OK. Enable multiple system event-triggered alert rules at a time i. Select the system event-triggered alert rules that you want to enable and click Enable in the lower-left corner of the alert rule list. ii. In the message that appears, click OK. |
| Delete one or more system event- triggered alert rules | Delete a single system event-triggered alert rule i. Find the system event-triggered alert rule that you want to delete and click Delete in the Operation column. ii. In the message that appears, click OK. Delete multiple system event-triggered alert rules at a time i. Select the system event-triggered alert rules that you want to delete and click Delete in the lower-left corner of the alert rule list. ii. In the message that appears, click OK. |

| View the records of system event- triggered alerts | After an event-triggered alert rule is created or enabled, CloudMonitor records the information about alerts that are generated based on the alert rule. i. Click the Event Alarm history tab. ii. Optional. Enter a rule ID or rule name and select a time range. The information about the alert rule is displayed: Product, Rule Name, Instance Name, Event Name, Event Level, and Alert Time. |
|---|---|

## 10 Application group

Application groups allow you to manage Elastic Compute Service (ECS) instances by group based on your business requirements. You can use an application group to manage businessspecific ECS instances in a centralized manner. You can manage the alert rules and view monitoring data of different application groups. This greatly simplifies management complexity and improves efficiency.

### 10.1 Create an application group

The application group feature allows you to manage resources from different cloud services and regions by group. You can use application groups to manage business-specific alert rules and view business-specific monitoring data to improve O&M efficiency.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application Groups** page, click **Create Application Group**.
5. In the **Create an application Group** panel, configure the parameters described in the
following table.

| Parameter | Description |
|---|---|
| Creation Method | Create Based on Instance Name: If you select this option, an application group is dynamically created based on instance names. This option is available for feature- specific resource sets or all resources of the current organization. Create manually: If you want to manage existing instances based on your business requirements, you can manually create a standard application group. Dynamic creation: If you select this option, an application group is dynamically created based on the specified resource set. This way, resource instances created in the resource set are automatically added to the application group, unless explicitly excluded. |
| Application Group Name | The name of the application group. |
| Resource Set | Note This parameter is displayed only if you set the creation method to Create Based on Instance Name. By default, Specified Resource Set is selected. |
| Resource Set Selection | The resource set in which you want to create an application group. The resource set must belong to the current organization. |

| Alert Contact | The alert contacts that receive alert notifications. You can select multiple alert contacts from the drop-down list. |
|---|---|
| Add Resource Item | Note This parameter is displayed only if you set the creation method to Create manually or Create Based on Instance Name. Click Add Entry. In the dialog box that appears, configure the following information: Select Cloud Product, Rule Relationship, Rule Configuration, and Add Instance. Important The application group contains all instances that you add. |
| Exclude Resource Items | Note This parameter is displayed only if you set the creation method to Dynamic creation. Click Add Entry. In the dialog box that appears, configure the following information: Select Cloud Product and Batch Exclude Instances. Important The application group does not contain the instances that you select. |

6. Click **OK**.

### 10.2 Manage application groups

You can modify or delete application groups on the Application Groups page in CloudMonitor.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**. On the **Application Groups**
page, manage the application groups. The following table describes supported operations.

| Operation | Procedure |
|---|---|

| View the information about an application group | i. Optional. In the top navigation bar, select the organization in which you want to manage application groups. On the Application Groups page, enter an application group name or ID, and then click Search to search for the application group. ii. Click the name of the application group whose information you want to view. On the details page of the application group, click tabs in the left-side pane to view the corresponding information. Group Overview: displays the basic information about the application group and the associated cloud services. Group Resources: displays the details of the resources in the application group. Availability Monitoring: displays the availability monitoring data of all Elastic Compute Service (ECS) instances in the current application group. |
|---|---|
| Modify an application group | i. Optional. In the top navigation bar, select the organization in which you want to manage application groups. On the Application Groups page, enter an application group name or ID, and then click Search to search for the application group. ii. Find the application group that you want to modify, click the icon in the application group card, and then click Modify Group. iii. In the Modify application Group panel, modify the Application Group Name, Alert Contact, and resources in the application group. iv. After the modification is complete, click OK. |
| Delete one or more resources from an application group | i. Find the application group that you want to manage and click its name. In the left-side pane, click the Group Resources tab. ii. In the list of ECS instances, delete one or more instances. Delete a single instance i. Find the instance that you want to delete, and clickD elete in the Operation column. ii. In the message that appears, click OK. Delete multiple instances at a time i. Select the instances that you want to delete and clickD elete in the lower-left corner of the instance list. ii. In the message that appears, click OK. |

| Delete an application group | Note If you delete an application group, all alert rules and event- triggered alerts of the application group are deleted. The instances in the application group are automatically migrated back to the pool that contains all instances. i. Optional. In the top navigation bar, select an organization in which you want to manage application groups. On the Application Groups page, enter an application group name or ID, and then click Search to search for the application group. ii. On the Application Groups page, delete one or more application groups. Delete a single application group i. Find the application group that you want to delete, click the icon in the application group card, and then click Delete Group. ii. In the Delete Group message, click OK. Delete multiple application groups at a time i. Select the application groups that you want to delete and click Delete in the lower-left corner of the application group list. ii. In the Delete Group message, click OK. |
|---|---|

### 10.3 Availability monitoring

#### 10.3.1 Create an availability monitoring task

CloudMonitor provides the availability monitoring feature to help you check whether a local service or cloud server responds as expected. You can specify the path and port for the local service or cloud server. If the local service or cloud server times out or returns an error code, CloudMonitor sends an alert notification. This way, you can troubleshoot the issue at the earliest opportunity.

**Procedure**

Availability monitoring allows you to use Elastic Compute Service (ECS) instances as the monitoring nodes.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application Groups** page, click the name of the application group that you want to
manage. On the page that appears, click the **Availability Monitoring** tab in the left-side navigation pane.
5. Click **Add Availability Monitoring**. In the **Create/Modify Availability Monitor** wizard,
configure the parameters. The following table describes the parameters.

| Step and parameter |   | Description |
|---|---|---|
| Create Task | Task Name | The name of the availability monitoring task. The name must be 4 to 50 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ |
|   | Monitoring Nodes | Select one or more instances that you want to monitor in the application group. Note If you create more than 500 tasks for an instance, some tasks may fail. |
|   | Detection target | The object that you want to monitor. Default value:U RL or IP. |
|   | Probe Type | HTTP(S): If you select this option, enter the URL that you want to monitor. TELNET: If you select this option, enter the IP address that you want to monitor. PING: If you select this option, enter the IP address that you want to monitor. |
|   | Request Method | The request method. Valid values: HEAD, GET and POST. Note This parameter is displayed only if the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S). |
|   | Monitoring Frequency | The interval at which detection requests are sent. Default value: 1Minutes . Note This parameter is displayed only if the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S). |

|   | Headers | The headers of the HTTP or HTTPS request. Format: parameter1:value1 . Separate multiple headers with commas (,). Note If the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure this parameter. |
|---|---|---|
|   | POST Content | The content is submitted in POST requests during site monitoring. This parameter is displayed only if you set the Request Method parameter to POST. Format: parameter1=value1&parameter2=value2 . |
|   | Match Response Content | The response content that you want to match and the method to match the response content. If you specify response content, the monitoring task checks whether the first 64 KB of the HTTP response body contains the response content that you specify. Valid values: Generate Alerts If Response Contains Generate Alerts If Response Does Not Contain Note If the Detection target parameter is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure this parameter. |
|   | Status Code | The range of the status codes that you want to match. CloudMonitor generates an alert if the returned status code meets the alert condition. For more information about status codes, see Status codes. Note This parameter is required if you set the Probe Type parameter to HTTP(S) or TELNET. If the status code, packet loss rate, or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert contact group. |

|   | Response Time | The periods of the response time that you want to match. CloudMonitor generates an alert if the response time meets the alert condition. Unit: milliseconds. Note If the status code, packet loss rate, or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert contact group. |
|---|---|---|
| Alert settings |   |   |
|   | Packet Loss Rate | The range of the packet loss rates that you want to match. CloudMonitor generates an alert if the packet loss rate meets the alert condition. Note This parameter is required if you set the Probe Type parameter to PING. If the status code, packet loss rate, or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert contact group. |
|   | Alert Level | The alert level and the methods that are used to send alert notifications. Valid values: Critical (SMS + Mail + Webhook) Warning (SMS + Mail + Webhook) Info (Mail + Webhook) |
|   | Alert Callback | The URL that can be accessed over the Internet. CloudMonitor sends POST requests to push alert notifications to the specified URL. Note You can enter only an HTTP URL. |

|   | Channel Silence Period | The interval at which CloudMonitor resends an alert notification if the alert is not cleared. Valid values: 5Minutes, 10Minutes, 15Minutes, 30Minutes, 60Minutes, 3Hours, 6Hours, 12Hours, and 24Hours. CloudMonitor sends an alert notification when a metric value reaches the threshold. If the metric value reaches the threshold again within the mute period, CloudMonitor does not resend an alert notification. If the alert is not cleared after the mute period ends, CloudMonitor resends an alert notification. Note You can click Advanced Configuration to configure this parameter for the alert rule. |
|---|---|---|
|   | Effective time | The period during which the alert rule is effective. CloudMonitor sends alert notifications within the effective period and only records alerts beyond the effective period. Note You can click Advanced Configuration to configure this parameter for the alert rule. |

#### 10.3.2 Manage availability monitoring tasks

You can modify, disable, enable, and delete availability monitoring tasks on the **Availability**
**Monitoring** tab of an instance in CloudMonitor.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **CloudMonitor**.
3. In the left-side navigation pane, click **Application Group**.
4. On the **Application Groups** page, click the name of the application group that you want to
manage. On the page that appears, click the **Availability Monitoring** tab in the left-side navigation pane. On the **Availability Monitoring** tab, perform required operations. The following table describes the supported operations.

| Operation | Procedure |
|---|---|
| Modify an availability monitoring task | i. Find the availability monitoring task that you want to modify and click Modification in the Operation column. ii. In the Create/Modify Availability Monitor panel, modify the parameters as prompted. For more information about the parameters, see Create an availability monitoring task. iii. After the modification is complete, click OK. |

| Disable or enable one or more availability monitoring tasks | Note You can disable one or more availability monitoring tasks in the Enable state, or enable one or more availability monitoring tasks in the Disable state. Disable or enable a single availability monitoring task i. Click Disable or Enable in the Operation column of the task. ii. In the Disable or Enable message, click OK. Disable or enable multiple availability monitoring tasks at a time i. Select the availability monitoring tasks that you want to disable or enable and click Batch Disable or Batch Enable in the lower-left corner of the task list. ii. In the Disable or Enable message, click OK. |
|---|---|
| Delete one or more availability monitoring tasks | Delete a single availability monitoring task i. Find the availability monitoring task that you want to delete and click Delete in the Operation column. ii. In the Delete message, click OK. Delete multiple availability monitoring tasks at a time i. Select the availability monitoring tasks that you want to delete and click Batch Delete in the lower-left corner of the task list. ii. In the Delete message, click OK. |

#### 10.3.3 Status codes

If an error occurs when you use the availability monitoring feature of CloudMonitor to check the availability of a specified path or port, the corresponding status code is returned. The following table describes status codes.

| Protocol type | Status code | Description |
|---|---|---|
| HTTP | 610 | The status code returned because the connection times out. If CloudMonitor does not receive a response within 5 seconds after CloudMonitor sends an HTTP request, CloudMonitor determines that the connection times out. |
|   | 611 | The status code returned because the monitoring fails. |
| Telnet | 630 | The status code returned because the connection times out. If CloudMonitor does not receive a response within 5 seconds after CloudMonitor sends a Telnet request, CloudMonitor determines that the connection times out. |
|   | 631 | The status code returned because the monitoring fails. |

## 11 Download a report

You can export reports of the alert history, alert rules, and alert templates, and then download the reports to your local device.

**Background information**

Before you download the reports of the alert history, alert rules, or alert templates, make sure that the reports are exported. The downloaded reports are in the **.xlsx** format. You can find the downloaded reports in the default download directory of your browser. You can export and download the following types of reports: Alert history report: The report contains the service namespace, instance that triggers the alert, alert rule name, alert rule ID, point in time when the alert occurs, report export status, alert level, alert contacts, metric, alert expression, and monitoring data of each alert. Alert rule report: The report contains the service namespace, alert rule name, alert rule ID, dimension (instance-specific or not), monitored instance, group (resource set), alert rule status (enabled or disabled), report export status, alert contacts, metric, and alert expression of each alert rule. Alert template report: The report contains the template name, template ID, description, resource set, modification time, and template type (system template or not) of each alert template.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Products > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click**Export Report**.
4. On the**Report Export**page, perform the required operations. The following table
describes the operations that you can perform on reports.

| Operation | Description |
|---|---|
| Download a report | i. Click the Alarm History, Alarm Rules, or Alarm Template tab. ii. Optional. Filter reports by report status. iii. Find the report that you want to download and clickD ownload Report Task in the Operation column. iv. In the Download Report Task message, click OK. |
| Delete a report task | i. Click the Alarm History, Alarm Rules, or Alarm Template tab. ii. Optional. Filter reports by report status. iii. Find the report task that you want to delete and clickD elete Report Task in the Operation column. iv. In the Delete Report Task message, click OK. |

## 12 Namespaces

**Important**

To use the namespace feature, you must install Apsara Stack V3.16.2r-cms-SP013.

### 12.1 Time series metrics

The Time Series Metrics tab on the Namespace page provides a centralized platform for you to query cloud service metrics. This allows you to query the information about each cloud service metric, such as the definition and calculation method.

**Background information**

The Time Series Metrics tab displays the metrics of all cloud services that are connected to CloudMonitor. The displayed information is consistent with the information about the cloud services and their metrics that are described in the Metrics topic. The Time Series Metrics tab displays the lineage information about each metric, including how the metric is created as a virtual SQL metric, the underlying source metric (actual SQL metric) on which the metric depends, and the data source, such as the project and Logstore in which data is stored. The lineage information displays the dependency relationships among metrics. This helps you track and troubleshoot data issues. The Time Series Metrics tab presents metrics in visual charts, which facilitates data analysis and visual representation.

**View time series metrics**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Namespace**. By default, the **Time Series Metrics**
tab appears.
4. In the left-side**Alibaba Cloud Services** section, click a cloud service. Then, the metric
information about the cloud service is displayed in the right-side section.
5. Find the metric that you want to view and click the
icon next to its name. In the chart that appears, you can view the lineage of the metric, which tracks the flow from the SQL statement that creates the metric through to the dependencies on source data stored in the specific Simple Log Service project and Logstore and also includes the dimension (DIM) table of CloudMonitor that is associated with the metric. Not all cloud service metrics have DIM table data.
6. Click each node in the flow. On the **Inspection Item Details** tab of the **Availability**
**Monitoring Details** panel, check whether data exists. You can troubleshoot issues based
on the results of inspection items. An issue may occur due to the raw data, intermediate process, or aggregation calculation in the final stage. If an issue occurs, troubleshoot the issue based on the results of the related inspection items.

| Node | Inspection item |
|---|---|
| VIRTUAL SQL _ | Checks whether the virtual metric has data. Checks whether the fields of the virtual metric do not match those of the source metric. Checks whether the fields of the virtual metric are inconsistent with the query results of Tablestore. |
| SQL | Checks whether the source metric has data. Checks whether the fields of the metric are inconsistent with the query results of Tablestore. Indicates the normal latency of the metric. |
| DIM | Checks whether the sampled instances have DIM table data. |

| STREAM | Checks whether the project is running. Checks whether all Logstores within the stream are running. Checks whether all partitions within the project are running. Checks whether traffic exists in the partitions. Checks whether traffic exists in the stream. Checks whether the inbound and outbound data of the stream meets the conditions of the metric. |
|---|---|
| LOGSTORE | Checks whether the shards of the Logstore meet the business requirements. Checks whether the Logstore exists and whether data exists in the Logstore. Checks whether inbound traffic exists in the Logstore. Checks whether the Logstore runs in the source as expected. Checks whether the Logstore has a corresponding Logstore. |

7. On the **Monitoring Details** tab of the **Availability Monitoring Details** panel of the
VIRTUAL_SQL and SQL nodes, configure the Instance ID, Aggregate Value, and Select Time parameters, and then click **Search**. The corresponding monitoring data is displayed in the Monitoring Chart section.

| Parameter | Description |
|---|---|
| Namespace | The namespace to which the metric belongs. The default value is used. |
| Metric Name | The name of the metric. The default value is used. |
| Instance ID | The ID of the cloud service instance that you want to query. |
| Aggregate Value | The aggregation method. Note The available aggregation methods vary based on cloud services. |
| Select Time | The time range of the monitoring data. You can select 1 hour, 4 hours, 12 hours, or a custom time range. |
| Log Service Data | This parameter is displayed only on the Monitoring Details tab of SQL nodes. This parameter specifies whether Simple Log Service data exists. |

| Monitoring Chart | A monitoring chart is generated based on the specified instance ID, aggregate value, and time range. You can view the trend of metric data on the monitoring chart. |
|---|---|

### 12.2 System events

#### 12.2.1 Event monitoring metrics of cloud services

**services**

This topic describes the event monitoring metrics of cloud services. The information about a system event includes the event name, event description, event level, event status, and event type.

**Event monitoring metrics of CloudMonitor**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Agent Status Stopped _ _ | CloudM onitor | The CloudMonitor agent stops sending heartbeat messages. | CRITICAL | Stoppe d | StatusNotif ication |
| Agent Status Running _ _ | CloudM onitor | The CloudMonitor agent resumes sending heartbeat messages. | CRITICAL | Runnin g | StatusNotif ication |

**Event monitoring metrics of HDR**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|

| PrimarySiteVpc:Delete d | Hybrid Disaster Recover y (HDR) | The virtual private cloud (VPC) in which the production site is deployed is deleted. | CRITICAL | Failed | StatusNotif ication |
|---|---|---|---|---|---|
| SecondarySiteVpc:Del eted | HDR | The VPC in which the disaster recovery site is deployed is deleted. | CRITICAL | Failed | StatusNotif ication |
| PrimarySiteNetwork:D eleted | HDR | The network of the production site is disconnected. | CRITICAL | Failed | StatusNotif ication |
| SecondarySiteNetwor k:Deleted | HDR | The network of the disaster recovery site is disconnected. | CRITICAL | Failed | StatusNotif ication |
| PrimarySecurityGroup :Deleted | HDR | The security group of the production site is deleted. | CRITICAL | Failed | StatusNotif ication |
| SecondarySecurityGro up:Deleted | HDR | The security group of the disaster recovery site is deleted. | CRITICAL | Failed | StatusNotif ication |
| SecurityGroup:Inconsi stency | HDR | The security group policies are inconsistent. | CRITICAL | Failed | StatusNotif ication |
| ProductSiteNetwork:In consistency | HDR | The network information about the production site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| DrSiteNetwork:Inconsi stency | HDR | The network information about the disaster recovery site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ProductSiteStorage:In consistency | HDR | The storage information about the production site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| DrSiteStorage:Inconsi stency | HDR | The storage information about the disaster recovery site is abnormal. | CRITICAL | Failed | StatusNotif ication |

| PrimarySiteComputati on:Inconsistency | HDR | The computing information about the production site is abnormal. | CRITICAL | Failed | StatusNotif ication |
|---|---|---|---|---|---|
| DrSiteComputation:In consistency | HDR | The computing information about the disaster recovery site is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ReplicationGroup:Inco nsistency | HDR | The replication pair- consistent group information is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ReplicationPair:Incons istency | HDR | The replication pair information is abnormal. | CRITICAL | Failed | StatusNotif ication |
| Gateway:Inconsistenc y | HDR | The gateway is abnormal. | CRITICAL | Failed | StatusNotif ication |
| ShadowEcs:Inconsiste ncy | HDR | The Elastic Compute Service (ECS) instance replication is abnormal. | CRITICAL | Failed | StatusNotif ication |

**Event monitoring metrics of ASR-BR**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| BackupPlan | Apsara Stack Resilien ce for Backup and Recover y (ASR- BR) | An alert related to backup schedules is triggered. | CRITICAL | FAILED | StatusNotif ication |

| RecoveryTask | ASRBR | An alert related to recovery tasks is triggered. | CRITICAL | FAILED | StatusNotif ication |
|---|---|---|---|---|---|
| MigratePlan | ASRBR | An alert related to migration tasks is triggered. | CRITICAL | FAILED | StatusNotif ication |
| LICENSE | ASRBR | An alert related to authorized quotas is triggered. | CRITICAL | FAILED | Maintenan ce |

**Event monitoring metrics of ROS**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Stack:StatusChange | Resourc e Orchestr ation Service (ROS) | The status of a stack is changed. | INFO | Normal | StatusNotif ication |
| StackResource:Status Change | ROS | The status of the resources in a stack is changed. | INFO | Normal | StatusNotif ication |
| StackGroup:Operation StatusChange | ROS | The operation status of a stack group is changed. | INFO | Normal | StatusNotif ication |

**Event monitoring metrics of ApsaraDB RDS**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Instance:HASwitch | ApsaraD B RDS | An alert related to high- availability (HA) switchovers is triggered. | WARN | Normal | Maintenan ce |

**Event monitoring metrics of ECS**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Disk:ConvertToPostpai dCompleted | ECS | The billing method of the disk is changed to pay-as-you-go. | INFO | Normal | StatusNotif ication |
| Disk:DiskOperationCo mpleted | ECS | The disk operations are complete. | INFO | Normal | StatusNotif ication |
| Disk:ErrorDetected:Ex ecuted | ECS | An alert related to the damage to a local disk ends. | CRITICAL | Execut ed | Exception |
| Disk:ErrorDetected:Ex ecuting | ECS | An alert related to the damage to a local disk starts. | CRITICAL | Executi ng | Exception |
| Disk:OverduePayment Release | ECS | A disk is released due to overdue payments. | CRITICAL | Normal | StatusNotif ication |
| Disk:Stalled:Executed | ECS | The impact on the disk performance ends. | CRITICAL | Execut ed | Exception |
| Disk:Stalled:Executing | ECS | The impact on the disk performance starts. | CRITICAL | Executi ng | Exception |
| Instance:AutoReactiva teCompleted | ECS | An instance is automatically restarted. | INFO | Normal | StatusNotif ication |
| Instance:BurstablePer formanceRestricted | ECS | The performance of a burstable instance is restricted. | WARN | Normal | StatusNotif ication |
| Instance:InstanceFailu re.PerformanceImpact :Executed | ECS | The potential impact of an instance error on the instance performance ends | WARN | Execut ed | Exception |
| Instance:InstanceFailu re.PerformanceImpact :Executing | ECS | The potential impact of an instance error on the instance performance starts. | WARN | Executi ng | Exception |

| Instance:InstanceFailu re.Reboot:Executed | ECS | An instance reboot that is caused by an instance error is complete. | CRITICAL | Execut ed | Exception |
|---|---|---|---|---|---|
| Instance:InstanceFailu re.Reboot:Executing | ECS | An instance reboot that is caused by an instance error starts. | CRITICAL | Executi ng | Exception |
| Instance:LiveMigratio nAcrossDDH | ECS | An instance is hot migrated between dedicated hosts. | INFO | Normal | StatusNotif ication |
| Instance:Performance ModeChange | ECS | The performance mode of a burstable instance is changed. | INFO | Normal | StatusNotif ication |
| Instance:PreemptibleI nstanceInterruption | ECS | A preemptible instance is interrupted. | WARN | Normal | StatusNotif ication |
| Instance:Security.Tpm Alert:Executed | ECS | A Trusted Platform Module (TPM) security alert ends. | WARN | Execut ed | Exception |
| Instance:Security.Tpm Alert:Executing | ECS | A TPM security alert starts. | WARN | Executi ng | Exception |
| Instance:StateChange | ECS | The state of an ECS instance is changed. | INFO | Normal | StatusNotif ication |
| Instance:SystemFailur e.Delete:Avoided | ECS | The automatic instance release that is caused by an instance creation failure is avoided. | CRITICAL | Avoide d | Exception |
| Instance:SystemFailur e.Delete:Executed | ECS | The automatic instance release that is caused by an instance creation failure is complete. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Delete:Executing | ECS | The automatic instance release that is caused by an instance creation failure is in progress. | CRITICAL | Executi ng | Exception |

| Instance:SystemFailur e.PerformanceImpact: Executed | ECS | The impact of a system error on the instance performance ends. | WARN | Execut ed | Exception |
|---|---|---|---|---|---|
| Instance:SystemFailur e.PerformanceImpact: Executing | ECS | The impact of a system error on the instance performance starts. | WARN | Executi ng | Exception |
| Instance:SystemFailur e.Reboot:Executed | ECS | An instance reboot that is caused by a system error is complete. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Reboot:Executing | ECS | An instance reboot that is caused by a system error starts. | CRITICAL | Executi ng | Exception |
| Instance:SystemFailur e.Reboot:Failed | ECS | An instance reboot that is caused by a system error fails. | CRITICAL | Failed | Exception |
| Instance:SystemFailur e.Redeploy:Avoided | ECS | An instance redeployment that is caused by a system error is avoided. | CRITICAL | Avoide d | Exception |
| Instance:SystemFailur e.Redeploy:Canceled | ECS | An instance redeployment that is caused by a system error is canceled. | CRITICAL | Cancel ed | Exception |
| Instance:SystemFailur e.Redeploy:Executed | ECS | An instance redeployment that is caused by a system error is complete. | CRITICAL | Execut ed | Exception |
| Instance:SystemFailur e.Redeploy:Executing | ECS | An instance redeployment that is caused by a system error is being executedin progress. | CRITICAL | Executi ng | Exception |
| Instance:SystemFailur e.Redeploy:Scheduled | ECS | An instance redeployment that is caused by a system error is scheduled. | CRITICAL | Schedu led | Exception |
| Instance:SystemFailur e.Stop:Executed | ECS | An instance stop that is caused by a system error is complete. | CRITICAL | Execut ed | Exception |

| Instance:SystemFailur e.Stop:Executing | ECS | An instance stop that is caused by a system error starts. | CRITICAL | Executi ng | Exception |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.IsolateErrorDi sk:Avoided | ECS | The damaged-disk isolation that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Canceled | ECS | The damaged-disk isolation that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Executed | ECS | The damaged-disk isolation that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Executing | ECS | The damaged-disk isolation that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Failed | ECS | The damaged-disk isolation that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.IsolateErrorDi sk:Inquiring | ECS | The damaged-disk isolation that is caused by system maintenance is waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.PerformanceI mpact:Executed | ECS | The potential impact of system maintenance on the instance performance ends. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.PerformanceI mpact:Executing | ECS | The potential impact of system maintenance on the instance performance starts. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Avoided | ECS | The damaged-disk reinitialization that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |

| Instance:SystemMaint enance.ReInitErrorDis k:Canceled | ECS | The damaged-disk reinitialization that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.ReInitErrorDis k:Executed | ECS | The damaged-disk reinitialization that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Executing | ECS | The damaged-disk reinitialization that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Failed | ECS | The damaged-disk reinitialization that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.ReInitErrorDis k:Inquiring | ECS | The damaged-disk reinitialization that is caused by system maintenance is waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Avoide d | ECS | A scheduled instance reboot that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Cancel ed | ECS | A scheduled instance reboot that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Execut ed | ECS | A scheduled instance reboot that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Execut ing | ECS | A scheduled instance reboot that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |

| Instance:SystemMaint enance.Reboot:Failed | ECS | A scheduled instance reboot that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.Reboot:Inquiri ng | ECS | A scheduled instance reboot that is caused by system maintenance is waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Reboot:Sched uled | ECS | An instance reboot that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Avoided | ECS | An instance reboot and damaged-disk isolation that are caused by system maintenance are avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Canceled | ECS | An instance reboot and damaged-disk isolation that are caused by system maintenance are canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Executed | ECS | An instance reboot and damaged-disk isolation that are caused by system maintenance are complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Executin g | ECS | An instance reboot and damaged-disk isolation that are caused by system maintenance are in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.RebootAndIsol ateErrorDisk:Inquiring | ECS | An instance reboot and damaged-disk isolation that are caused by system maintenance are waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |

| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Avoided | ECS | An instance reboot and damaged-disk reinitialization that are caused by system maintenance are avoided. | CRITICAL | Avoide d | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Canceled | ECS | An instance reboot and damaged-disk reinitialization that are caused by system maintenance are canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Executed | ECS | An instance reboot and damaged-disk reinitialization that are caused by system maintenance are complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Executing | ECS | An instance reboot and damaged-disk reinitialization that are caused by system maintenance are in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.RebootAndReI nitErrorDisk:Inquiring | ECS | An instance reboot and damaged-disk reinitialization that are caused by system maintenance are waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Avoi ded | ECS | A scheduled instance redeployment that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Can celed | ECS | A scheduled instance redeployment that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Exe cuted | ECS | A scheduled instance redeployment that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |

| Instance:SystemMaint enance.Redeploy:Exe cuting | ECS | A scheduled instance redeployment that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
|---|---|---|---|---|---|
| Instance:SystemMaint enance.Redeploy:Inqu iring | ECS | A scheduled instance redeployment that is caused by system maintenance is waiting for your confirmation. | CRITICAL | Inquirin g | Maintenan ce |
| Instance:SystemMaint enance.Redeploy:Sch eduled | ECS | An instance redeployment that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |
| Instance:SystemMaint enance.Stop:Avoided | ECS | A scheduled instance stop that is caused by system maintenance is avoided. | CRITICAL | Avoide d | Maintenan ce |
| Instance:SystemMaint enance.Stop:Canceled | ECS | A scheduled instance stop that is caused by system maintenance is canceled. | CRITICAL | Cancel ed | Maintenan ce |
| Instance:SystemMaint enance.Stop:Executed | ECS | A scheduled instance stop that is caused by system maintenance is complete. | CRITICAL | Execut ed | Maintenan ce |
| Instance:SystemMaint enance.Stop:Executin g | ECS | A scheduled instance stop that is caused by system maintenance is in progress. | CRITICAL | Executi ng | Maintenan ce |
| Instance:SystemMaint enance.Stop:Failed | ECS | A scheduled instance stop that is caused by system maintenance fails. | CRITICAL | Failed | Maintenan ce |
| Instance:SystemMaint enance.Stop:Schedule d | ECS | An instance stop that is caused by system maintenance is scheduled. | CRITICAL | Schedu led | Maintenan ce |

| NetworkInterface:Net workInterfaceOperate Completed | ECS | The network interface controller (NIC) operations are complete. | INFO | Normal | StatusNotif ication |
|---|---|---|---|---|---|
| Snapshot:CreateSnap shotCompleted | ECS | A snapshot is created for a disk. | INFO | Normal | StatusNotif ication |
| Instance:VmLivemigra teException | ECS | The VM status is abnormal after hot migration. | WARN | Normal | StatusNotif ication |
| Instance:VmDownCau sedByNcDown | ECS | A VM breaks down due to the breakdown of a physical server. | WARN | Normal | StatusNotif ication |
| Instance:VmDownEnd | ECS | A VM is recovered from a breakdown. | WARN | Execut ed | StatusNotif ication |
| Instance:VmPanicEve nt | ECS | A VM is restarted after a panic event caused by internal errors. | WARN | Normal | StatusNotif ication |
| Instance:VmCrashEve nt | ECS | A VM crashes due to exceptions. | WARN | Normal | StatusNotif ication |

**Event monitoring metrics of ApsaraDB for Redis**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Instance:HASwitch | ApsaraD B for Redis | An alert related to HA switchovers is triggered. | WARN | Normal | Maintenan ce |

**Event monitoring metrics of ApsaraDB for MongoDB**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Instance:HASwitch | ApsaraD B for MongoD B | An alert related to HA switchovers is triggered. | WARN | Normal | Maintenan ce |

**Event monitoring metrics of PolarDB-X 1.0**

| Event name | Cloud service | Event description | Event level | Event status | Event type |
|---|---|---|---|---|---|
| Instance:HighPhysical ConnectionPoolUsage | PolarDB -X 1.0 | The usage of the physical connection pool is high. | WARN | Normal | StatusNotif ication |
| Instance:CriticalPhysic alConnectionPoolUsag e | PolarDB -X 1.0 | The usage of the physical connection pool exceeds the alert threshold. | CRITICAL | Normal | StatusNotif ication |

#### 12.2.2 View system event metrics

The System Event tab on the Namespace page provides a centralized platform for you to query the system event metrics of cloud services. This allows you to query the information about each system event metric, including the level, status, and type of the metric.

**Background information**

The system event metrics on the System Event tab are the same as those that are described in the System events of cloud services topic.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Namespace**.
4. On the Namespace page, click the **System Event** tab.
5. In the left-side **Alibaba Cloud Services** section, click a cloud service. Then, the system
event metrics of the cloud service are displayed in the right-side section.

## 13 Business monitoring

### 13.1 Monitor SLS logs

You can monitor the logs in Simple Log Service (SLS) to monitor keywords in logs and detect potential issues at the earliest opportunity. This improves system stability and O&M efficiency.

**Create a log monitoring metric**

You can create a log monitoring metric to track and analyze log data in real time.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, choose **Business Monitoring** > **Simple Log Service Log**
**Monitoring**.
4. On the **SLS log monitoring** page, click **Create Log Monitoring**.
5. In the **Create Log Monitoring** panel, configure parameters in the following steps: **Basic**
**information**, **Log Data Source**, and **Compute Configuration**.
i. In the **Basic information** step, enter a name in the **Monitoring Item Name** field and click **Next step**. A metric name must be unique in a level-1 organization. ii. In the **Log Data Source** step, configure the **SLS log source**, **SlsProject**, and
**SlsLogstore** parameters and click **Next step**.
**SLS log source**: the source of the log data. Default value: Redline.
**SlsProject**: the name of the project in SLS.
**SlsLogstore**: the name of the Logstore in SLS.
iii. In the **Compute Configuration** step, configure the **Unit**, **Aggregation cycle**,
**Statistical Methods**, **Extension field**, **Log Filtering**, and **Group By** parameters, and
then click **Submit**.

| Parameter | Description |
|---|---|
| Unit | The unit of the metric. |

| Aggregati on cycle | The statistical period of the metric. Unit: minutes. Valid values: 1 minute, 2 minutes, 3 minutes, 4 minutes, 5 minutes, 10 minutes, 15 minutes, 20 minutes, 30 minutes, and 60 Minutes. |
|---|---|
| Statistical Methods | The statistical methods that are used to aggregate log data within a statistical period. If the values of log fields are of the numeric type, you can use all the supported aggregate functions. Otherwise, you can use only the COUNT and COUNTPS aggregate functions. Valid values: Count, Sum, Maximum, Minimum, Average, countps, sumps, and distinct. Count: calculates the number of values of the specified field within a statistical period. Sum: calculates the sum of the values of the specified field within a statistical period. Maximum: calculates the maximum value of the specified field within a statistical period. Minimum: calculates the minimum value of the specified field within a statistical period. Average: calculates the average of the values of the specified field within a statistical period. countps: calculates the number of values of the specified field divided by the total number of seconds within a statistical period. sumps: calculates the sum of the values of the specified field divided by the total number of seconds within a statistical period. distinct: calculates the number of unique values of the specified field within a statistical period after duplicate values are removed. For example, if you want to calculate the number of values of the sql rendered _ _ field, add an entry for the Statistical Methods parameter. Enter sql rendered in _ _ the first column as the log field and select Count from the drop-down list in the second column. Then, sql rendered count is automatically entered in the _ _ __ column after as. |
| Extension field | The extended fields that allow you to perform basic operations on the aggregation results of log data. For example, you have configured the Statistical Methods parameter to calculate the total number of HTTP requests as TotalNumber and the number of HTTP requests whose status code is greater than 499 as 5XXNumber. You can calculate the server error rate by adding the following formula as an extended field: 5XXNumber/TotalNumber × 100. |
| Log Filtering | The conditions that are used to filter log data. This parameter is equivalent to the WHERE clause in SQL. For example, the sql rendered field is used and the keyword to be monitored in _ _ the values of the field is ERROR. In this case, enter sql rendered in the first _ _ column, select Contains from the drop-down list in the second column, and then enter ERROR in the third column. Important The name of the log field that you use to filter data cannot contain Chinese characters. |

| Group By | The dimensions based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL. Log data is grouped based on the specified dimensions. If you do not specify a dimension, all data is aggregated based on the specified aggregate functions. |
|---|---|

**View the details of a metric**

After a log monitoring metric is created, you can view the details of the metric, including the basic information, monitoring charts, and alert rules.
1. On the **SLS log monitoring** page, view the information about a metric in the following
columns: **Monitoring Items**, **Data source (Region/Logstore/Project)**, **Log Filtering**, and **Creation time**.
2. In the metric list, find the metric that you want to view and click **Details** in the **Operation**
column.
3. On the details page of the metric, view the details of the metric.
In the basic information section, view the basic information about the metric from the following parameters: **Monitoring Items**, **Geography**, **Logstore**, **SlsProject**, and
**Creation time**.
On the **Monitoring chart** tab, view the monitoring charts of the metric. You can view the monitoring data generated within the previous **1 hour**, **3 hours**, **6 hours**, **12 hours**, **1**
**day**, **3 days**, **7 days**, and **14 days**, or **a custom time range**.
You can click **Create alarm rules** to create an alert rule. For more information, see Create an alert rule. On the **Alarm Rules** tab, view the alert rules of the metric. You can click **Create alarm rules** to create an alert rule. For more information, see Create an alert rule. You can click buttons in the **Operation** column to manage alert rules. For more information, see Manage alert rules.

**Modify a metric**

If the information about a metric changes, you can modify the metric. The name of a metric cannot be modified.
1. On the **SLS log monitoring** page, find the metric that you want to modify and click **Edit** in
the **Operation** column.
2. In the **Edit Log Monitoring** panel, follow the steps in the wizard to modify the metric
based on your business requirements. For more information about the parameters, see the Create a log monitoring metric section of this topic.

**Copy a metric**

You can copy a metric to quickly create a metric that is the same as the copied metric. You can fine-tune the new metric based on your business requirements.
1. On the **SLS log monitoring** page, find the metric that you want to copy and click **Copy** in
the **Operation** column.
2. In the **Replication Log Monitoring** panel, follow the steps in the wizard to modify the
metric based on your business requirements. For more information about the parameters, see the Create a log monitoring metric section of this topic.

**Delete a metric**

You can delete a metric that is no longer needed.
1. On the **SLS log monitoring** page, find the metric that you want to delete and click **Delete**
in the **Operation** column.
2. In the **Delete monitoring items** message, click **OK**.
g

## 14 Availability monitoring

CloudMonitor provides the availability monitoring feature to help you check whether a local service or cloud server responds as expected. You can specify the path and port for the local service or cloud server. If the local service or cloud server times out or returns an error code, CloudMonitor sends an alert notification. This way, you can troubleshoot the issue at the earliest opportunity. Availability monitoring allows you to use Elastic Compute Service (ECS) instances as the monitoring nodes.

**Create an availability monitoring task**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Monitoring and O&M** > **Cloud Monitor**.
3. In the left-side navigation pane, click **Service Availability Monitoring**.
4. On the **Service Availability Monitoring** page, click **Add Availability Monitoring**. In the
**Create Availability Monitoring** panel, configure the parameters. The following tables
describe the parameters. i. **Create Task** step

| Parameter | Description |
|---|---|
| Task Name | The name of the availability monitoring task. The name must be 4 to 50 characters in length, and can contain letters, digits, underscores ( ), and hyphens _ (-). |
| Probe Source | The instances from which you want to send detection requests. |
| Detection target | The object that you want to monitor. Default value:U RL or IP. |
| Probe Type | The detection method. Valid values: HTTP(S), TELNET, and PING. HTTP(S): sends HTTP or HTTPS requests to detect the health status of the specified object. You need to enter the URL of the object. Example: http://localhost:8081/check health.html . _ TELNET: runs the TELNET command to detect the health status of the specified object. You need to enter the IP address and port number of the object. Example: 192.168.1.1:22 . PING: runs the PING command to detect the health status of the specified object. You need to enter the IP addresses of the object. Example: 192.168.1.1 . |

g

| Request Method | The request method. Valid values: HEAD, GET and POST. Note This parameter is displayed only if the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S). |
|---|---|
| Advanced Configurati on | Note If the Detection target is set to URL or IP and the Probe Type parameter is set to HTTP(S), you can click Advanced Configuration to configure the following parameters. Request Parameters Headers: the headers of the HTTP or HTTPS request. Format: key1:value1. Enter each header in a separate line. Submitted Content: the content to be submitted in POST requests during site monitoring. This parameter is displayed only if you set the Request Method parameter to POST. Format: parameter1=value1&parameter2=value2 . Match Response Content: the response content that you want to match and the method to match the response content. If you specify response content, the monitoring task checks whether the first 64 KB of the HTTP response body contains the response content that you specify. Valid values: Generate Alerts If Response Contains Generate Alerts If Response Does Not Contain User Authentication HTTP authentication User name: the username for HTTP authentication. HTTP authentication password: the password for HTTP authentication. Monitoring frequency: the interval at which detection requests are sent. Valid value: 15 seconds. |

ii. Alert settings

| Parameter | Description |
|---|---|

g

| Alert Rule | If you set the Probe Type parameter to HTTP(S) or TELNET, the Status Code and Response time parameters are displayed and required. If you set the Probe Type parameter to PING, the Packet loss and Response time parameters are displayed and required. Note Status Code: the range of the status codes that you want to match. CloudMonitor generates an alert if the returned status code meets the alert condition. For more information, see . Packet loss: the range of the packet loss rates that you want to match. CloudMonitor generates an alert if the packet loss rate meets the alert condition. Response time: the periods of the response time that you want to match. CloudMonitor generates an alert if the response time meets the alert condition. Unit: milliseconds. If the status code, packet loss rate, or response time reaches the specified threshold, an alert is triggered and a notification is sent to the specified alert contact group. |
|---|---|
| Alert Level | The alert level and the methods that are used to send alert notifications. Valid alert levels: Critical Warning Info |
| Alert Callback | The URL that can be accessed over the Internet. CloudMonitor sends HTTP POST requests to push alert notifications to the specified URL. Note You can enter only an HTTP URL. |
| Select Alert Contact Groups | Select the alert contact groups that receive alert notifications. |

g

| Advanced Configuration | Note Click Advanced Configuration to configure the following parameters. Channel Silence Period: the interval at which CloudMonitor resends an alert notification if the alert is not cleared. Valid values: 5Minutes, 10Minutes, 15Minutes, 30Minutes, 60Minutes, 3Hours, 6Hours, 12Hours, and 24Hours. CloudMonitor sends an alert notification when a metric value reaches the threshold. If the metric value reaches the threshold again within the mute period, CloudMonitor does not resend an alert notification. If the alert is not cleared after the mute period ends, CloudMonitor resends an alert notification. Effective time: the period during which the alert rule is effective. CloudMonitor sends alert notifications within the effective period and only records alerts beyond the effective period. |
|---|---|

iii. **Create Results** step After the availability monitoring task is created, you can view the task in the task list.

**View an availability monitoring task**

1. In the task list of the **Service Availability Monitoring** page, view the information about
availability monitoring tasks displayed in the following columns: **Task Name/Task ID**,
**Monitoring Status**, **Detection target**, **Probe Type**, **Number of abnormal machines**
**probed**, **Number of abnormal plug-in machines**, **Total number of machines** ,
**Availability**, and **Average Latency**.
You can click the icon above the list to set the automatic refresh interval or perform manual refresh. The automatic refresh interval can be set to 1, 3, or 5 minutes. You can click the icon above the list to select the columns to be displayed. If you clear a column, the column is not displayed.
2. Find the availability monitoring task that you want to manage and click the
icon in the
**Operation** column to view the monitoring details.
3. In the upper part of the task details page, view the basic information about the monitoring
task.
4. Select one or more monitored instances from the drop-down list.
g
5. Select a monitoring time range based on your business requirements. You can select **1**
**Hour**, **6 Hours**, **12 Hours**, **1 Day**, **3 Days**, **7 Days**, or **14 Days** or specify a custom time
range.
6. View the trend charts of the selected instances within the specified monitoring time range.

**Modify an availability monitoring task**

If the information about an existing availability monitoring task changes, you can modify the availability monitoring task based on your business requirements.
1. On the **Service Availability Monitoring** page, find the availability monitoring task that
you want to manage and click **Modification** in the **Operation** column.
2. In the **Modifying Availability Monitoring** panel, modify the parameters based on your
business requirements. For more information about the parameters, see the Create an availability monitoring task section of this topic.

**Important**

The **Detection target** and **Probe Type** parameters cannot be modified.

**Disable one or more availability monitoring tasks**

You can disable an availability monitoring task if you do not need to monitor the corresponding resources.

**Important**

You can disable only availability monitoring tasks in the **Enable** state. Disable a single availability monitoring task i. On the**Service Availability Monitoring**page, find the availability monitoring task that you want to disable and click **Disable** in the **Operation** column. ii. Click **OK**. Disable multiple availability monitoring tasks at a time i. On the **Service Availability Monitoring** page, select the availability monitoring tasks that you want to disable. ii. Click **Batch Disable** in the lower-left corner of the task list. iii. Click **OK**.

**Enable one or more availability monitoring tasks**

g You can enable a disabled availability monitoring task if you want to monitor the corresponding resources again.

**Important**

You can enable only availability monitoring tasks in the **Disable** state. Enable a single availability monitoring task i. On the **Service Availability Monitoring** page, find the availability monitoring task that you want to enable and click **Enable** in the **Operation** column. ii. Click **OK**. Enable multiple availability monitoring tasks at a time i. On the **Service Availability Monitoring** page, select the availability monitoring tasks that you want to enable. ii. Click **Batch Enable** in the lower-left corner of the task list. iii. Click **OK**.

**Delete one or more availability monitoring tasks**

You can delete an availability monitoring task if you no longer need it. Delete a single availability monitoring task i. On the **Service Availability Monitoring** page, find the availability monitoring task that you want to delete and click **Delete** in the **Operation** column. ii. Click **OK**. Delete multiple site monitoring tasks at a time i. On the **Service Availability Monitoring** page, select the availability monitoring tasks that you want to delete. ii. Click **Batch Delete** in the lower-left corner of the task list. iii. Click **OK**.
