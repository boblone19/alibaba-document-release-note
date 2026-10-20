---
title: "Apsara Big Data Manager User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 50
source_pdf: "f2627c6e2d3afa58_Alibaba Cloud Apsara Stack V3.18.6 Apsara Big Data Manager User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%AE%A1%E5%AE%B6/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Big%20Data%20Manager%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Apsara Big Data Manager User Guide 20260629

## Table of Contents

- 1 Apsara Big Data Manager
- 2 Common operations
- 3 Quick start
  - 3.1 Log on to Apsara Bigdata Manager
  - 3.2 Set the console theme
  - 3.3 View dashboards
  - 3.4 View cluster status
  - 3.5 View and handle cluster alerts
- 4 Monitoring
  - 4.1 View dashboards
  - 4.2 View resource libraries
  - 4.3 Check service health status
  - 4.4 View reports
  - 5.1 ABM O&M feature and page
  - 5.2 Business O&M
    - 5.2.1 View cron jobs
    - 5.2.2 Create and configure a zone-disaster recovery project in MaxCompute
- 6 Management
  - 6.1 Overview
  - 6.2 Jobs
    - 6.2.1 Overview
    - 6.2.2 Jobs
      - 6.2.2.1 Manually execute a job
      - 6.2.2.2 View cron jobs
      - 6.2.2.3 View the execution history of a job
      - 6.2.2.4 View job execution history
  - 6.3 Health management
    - 6.3.1 Monitoring configuration
    - 6.3.2 Inspection management
  - 6.4 Operation audit
- 7 FAQ
  - 7.1 How do I view service cluster traffic?
- 8 Go to other consoles

ager

## 1 Apsara Big Data Manager

Apsara Big Data Manager (ABM) is an O&M platform tailored for big data services. ABM supports monitoring, management, and O&M in multiple dimensions, such as business, services, clusters, and hosts. Customer O&M teams or on-site personnel can use ABM to perform O&M operations on big data services and manage the services in an efficient and centralized manner. ABM supports the following services: MaxCompute DataWorks DataHub Flink RealtimeCompute Hologres Dataphin Quick BI

## 2 Common operations

This topic describes how to use the search and sort features to facilitate data retrieval on the Operation and maintenance page in Apsara Big Data Manager (ABM). This topic also describes how to view and zoom in trend charts of cluster metrics such as CPU utilization and memory usage to efficiently monitor cluster performance. In this topic, MaxCompute and DataHub are used. You can perform these operations on other big data services by referring to this topic.

**Search for data**

You can search for an item in a list by column, which is similar to filtering data. For example, you can perform the following steps to search for a checker:
1. Log in to the ABM console. In the upper-left corner of the ABM console, click the More icon
and select **MaxCompute**. In the upper-right corner of the MaxCompute page, click
**Operation and maintenance**. On the page that appears, click the **Cluster O&M** tab. On
the Cluster O&M page, click the **Health** tab.
2. In the **Checker** list, click the Filter icon in a column and enter a keyword in the search box.
3. Click **Search**. The checkers that meet the requirements appear.
4. If the search results do not meet your business requirements, you can continue to perform
this operation on other columns.

**Sort projects based on a column**

You can sort projects based on a column in ascending or descending order.
1. Log in to the ABM console. In the upper-left corner of the ABM console, click the More icon
and select **MaxCompute**. In the upper-right corner of the MaxCompute page, click
**Operation and maintenance**. On the page that appears, click the **Cluster O&M** tab. On
the Cluster O&M page, click the **Health** tab.
2. In the **Checker** list, click a column heading or the sort icon in the column heading to sort
checkers in ascending or descending order. The highlighted up arrow indicates that the checkers are sorted in ascending order. The highlighted down arrow indicates that the checkers are sorted in descending order.

**View the trend charts for a MaxCompute cluster**

Log in to the ABM console. In the upper-left corner of the ABM console, click the More icon and select **MaxCompute**. In the upper-right corner of the MaxCompute page, click
**Operation and maintenance**. On the page that appears, click the **Cluster O&M** tab. On
the Cluster O&M page, click the **Overview** tab. On the Overview tab, you can view relevant metrics, such as CPU utilization and memory usage, of the selected cluster. The following example describes the CPU utilization of a cluster. The trend chart displays the trend lines of the total CPU utilization (cpu), CPU utilization for executing code in kernel space (sys), and CPU utilization for executing code in user space (user) for the specified cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster within the specified period of time.

**View the trend charts for a DataHub cluster**

1. Log in to the ABM console. In the upper-left corner of the ABM console, click the More icon
and select **DataHub**. In the upper-right corner of the DataHub page, click **Operation and**
**maintenance**. On the page that appears, click the **Service operation and maintenance**
tab. In the left-side navigation pane, click **Control Services**.
2. On the **Overview** page, view the trend charts of resource usage for the specified DataHub
cluster. The trend charts, such as those of the cluster read/write latency and the number of cluster read and write records, appear in the Resource Usage Trends section. Each chart displays the trend lines of the metrics over time in different colors. You can click the name of a metric under the chart to show or hide the corresponding trend line in the chart. A highlighted metric name indicates that the corresponding trend line is displayed, while a dimmed metric name indicates that the corresponding trend line is hidden.

## 3 Quick start

### 3.1 Log on to Apsara Bigdata Manager

**Manager**

This topic describes how to log on to Apsara Bigdata Manager.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .
5. After you log on to the Apsara Uni-manager Operations Console, click **Product O&M** in the
top menu bar.
6. Select **Big Data O&M > General Big Data O&M · Apsara Bigdata Manager** , and the
Dashboard page of Apsara Bigdata Manager opens automatically.

### 3.2 Set the console theme

You can set the theme of the Apsara Big Data Manager (ABM) console to dark or bright. By default, the dark theme is used. This topic describes how to switch between the two themes based on your preferences.

**Prerequisites**

An ABM account and the corresponding password are obtained.

**Procedure**

1. Log in to the ABM console.
2. Set the theme of the ABM console to dark or bright based on your preferences.
If the dark theme is used, you can move the pointer over the username in the upper-right corner and click the **Dark** switch to switch to the bright theme. If the bright theme is used, you can move the pointer over the username in the upperright corner and click the **Bright** switch to switch to the dark theme.

### 3.3 View dashboards

The Instrument cluster tab displays the key metrics of DataWorks, MaxCompute, StreamCompute, and DataHub, and the alert information of all big data services. This helps you comprehensively understand the overall status of big data services. This topic describes how to view the key metrics of big data services and the status of clusters on the Instrument cluster tab.

**Prerequisites**

Your Apsara Big Data Manager (ABM) account is granted the required permissions on the services on which you want to perform O&M.

**Background information**

The dashboard is a feature of the ABM console. As the homepage of the ABM console, the dashboard allows you to view the overall status of all big data services.

**Procedure**

1. Log in to the ABM console.
After you log in to the ABM console, the **Instrument cluster** tab appears by default. To return to the **Instrument cluster** tab, click the icon in the upper-left corner and then click **ABM**.
2. On the **Instrument cluster** tab, click the **DataWorks** section to view the metrics of
**DataWorks**.
The **DataWorks** section displays the overview of nodes, overview of slot usage, and trend charts of completed tasks of a DataWorks cluster.
3. On the **Instrument cluster** tab, click the **MaxCompute** section to view the metrics of
**MaxCompute**.
The **MaxCompute** section displays the overview of jobs, real-time capacity for the control system, data import traffic, computing resource usage, physical storage resource usage, and trend charts of logical and physical CPU utilization of a MaxCompute cluster.
4. On the **Instrument cluster** tab, click the **StreamCompute** section to view the metrics of
StreamCompute. The **StreamCompute** section displays the trend charts of the transactions per second (TPS), failover rate, CPU utilization, and memory usage of a StreamCompute cluster.
5. On the **Instrument cluster** tab, click the **DataHub** section to view the metrics of
**DataHub**.
The **DataHub** section displays the read/write latency, numbers of read/write records, read/write queries per second (QPS), read/write throughputs, and trend charts of CPU utilization and memory usage of a DataHub cluster.

### 3.4 View cluster status

Apsara Big Data Manager (ABM) allows you to view the key metrics of a MaxCompute cluster, including the CPU utilization, memory usage, load, storage space, and health status. This helps you understand the cluster status in real time and evaluate potential risks and health status based on these metrics.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background information**

In the ABM console, the procedures for viewing the cluster status for different services are the same. In this topic, MaxCompute is used to describe how to view the cluster status.

**Procedure**

1. Log in to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select MaxCompute.
3. In the top navigation bar of the MaxCompute page, click **Operation and maintenance**.
On the page that appears, click the **Cluster O&M** tab.
4. In the upper-left corner of the **Cluster O&M** tab, select the cluster that you want to view.
The **Overview** tab of the selected cluster appears. On the **Overview** tab, you can view the host status, service status, and health check result of the selected cluster. You can also view the trend charts of CPU utilization, disk usage, memory usage, load, and packet transmission for the cluster.

**What to do next**

You can evaluate the operation risks of the selected cluster based on the metrics such as the service status, CPU utilization, memory usage, storage space, and load. If the cluster has any Critical, Warning, or Exception alerts, you need to check and clear them at the earliest opportunity. You need to pay special attention to the Critical and Warning alerts. For more information, see View and clear cluster alerts.

### 3.5 View and handle cluster alerts

If you find alerts on the Overview tab of a cluster, you can go to the Health tab of the cluster to view and handle the alerts. This topic describes how users granted O&M permissions can view and handle cluster alerts in Apsara Big Data Manager (ABM) to ensure cluster stability. In this topic, MaxCompute and DataHub are used. You can view and handle cluster alerts for other services by referring to this topic.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background information**

In the ABM console, the procedures for viewing and handling cluster alerts for different services are the same. If a service cluster has alerts, especially the Critical and Warning alerts, pay attention to and handle them at the earliest opportunity to ensure that the cluster can run properly.

**Limits**

Only MaxCompute, DataHub, RealtimeCompute, Hologres, DataWorks, Dataphin, and QuickBI support cluster O&M.

**Procedure**

1. Log in to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select a service.
3. In the top navigation bar of the service page, click **Operation and maintenance**. On the
page that appears, click the **Cluster O&M** tab.

> **Note:** The Cluster O&M tab is displayed only for MaxCompute, DataHub, RealtimeCompute, Hologres, DataWorks, Dataphin, and QuickBI.

4. On the **Cluster O&M** tab, click the **Health** tab.
5. On the **Health** tab, click the
icon to expand a checker with alerts. You can view all hosts where the checker is run.
6. Click the name of the host that you want to view. In the panel that appears, click **Details** in
the Actions column of a checker to view the cause of the alert.
7. On the **Health** tab, click **Details** in the Actions column of the checker to view the solutions
to handle the alerts.
8. Handle the alerts based on the solutions.
To log in to a host with alerts for related operations, click the **Log in** icon next to the name of the host. On the **TerminalService** page, click the hostname on the left to log in to the host.
9. Click **Refresh** in the Actions column of the host to run the checker again. This way, you can
check whether the alert is cleared.

## 4 Monitoring

### 4.1 View dashboards

The Instrument cluster tab displays the key metrics of DataWorks, MaxCompute, StreamCompute, and DataHub, and the alert information of all big data services. On this tab, you can specify a time range to view data, refresh the tab, and enable the full-screen mode. This helps you comprehensively understand the overall status of big data services. This topic describes how to view the key metrics of big data services and the status of clusters on the Instrument cluster tab.

**Go to the Instrument cluster tab**

After you log in to the Apsara Big Data Manager (ABM) console, the **Instrument cluster** tab appears by default. To return to the **Instrument cluster** tab, click the icon in the upperleft corner and then click **ABM**. In the upper-left corner of the **Instrument cluster** tab, you can select a **region** from the
**Area** drop-down list to view the cluster status of each big data service in the region.

**View key metrics of DataWorks**

The Instrument cluster tab displays the key metrics of **DataWorks**. To view these metrics, click the **DataWorks** section of the **Instrument cluster** tab. The **DataWorks** section displays the overview of node, overview of slot usage, and trend charts of completed tasks of a DataWorks cluster.

**View key metrics of MaxCompute**

The Instrument cluster tab displays the key metrics of **MaxCompute**. To view these metrics, click the **MaxCompute** section of the **Instrument cluster** tab. The **MaxCompute** section displays the overview of jobs, real-time capacity of the control system, data import traffic, compute resource usage, physical storage resource usage, and trend charts of logical and physical CPU utilization of a MaxCompute cluster.

**View key metrics of StreamCompute**

The Instrument cluster tab displays the key metrics of StreamCompute. To view these metrics, click the **StreamCompute** section of the **Instrument cluster** tab. The **StreamCompute** section displays the trend charts of the transactions per second (TPS), failover rate, CPU utilization, and memory usage of a StreamCompute cluster.

**View key metrics of DataHub**

The Instrument cluster tab displays the key metrics of **DataHub**. To view these metrics, click the **DataHub** section of the **Instrument cluster** tab. The **DataHub** section displays the read/write latency, numbers of read/write records, read/write queries per second (QPS), read/write throughputs, and trend charts of CPU utilization and memory usage of a DataHub cluster.

**Specify a time range to view metric data**

By default, the Instrument cluster tab displays cluster metric data from the last two days. You can specify a time range to view the metric data. In the **Select Time** section of the **Instrument cluster** tab, specify the start time and end time by year, month, or day, and then click **OK** to view the metric data in the specified time range.

**Enable the full-screen mode**

On the Instrument cluster tab, you can view the status of big data services in full-screen mode. At the top of the **Instrument cluster** tab, click the icon to display the **Instrument**
**cluster** tab in full-screen mode.

### 4.2 View resource libraries

The Resource Library tab displays the resource usage data of MaxCompute, DataWorks, and DataHub in trend charts and lists. This helps you effectively manage resources. This topic describes how to access the Resource Library tab and view resource libraries of MaxCompute, DataWorks, and DataHub.

**Go to the Resource Library tab**

1. Log in to the Apsara Big Data Manager (ABM) console.

> **Note:** After you log in to the ABM console, the **Instrument cluster** tab appears by default. To return to the **Instrument cluster** tab, click the
> icon in the upper-left corner and
> then click **ABM**.

2. On the **Instrument cluster** tab, click the **Resource Library** tab. The Resource Library tab
appears.

**View the resource library of MaxCompute**

In the left-side navigation pane of the **Resource Library** tab, click **MaxCompute**. On the page that appears, you can view the resource usage in MaxCompute. For MaxCompute, the Resource Library tab displays the trend charts of compute unit (CU) and storage usage, lists of CU and storage usage, and proportions of idle CUs and storage.

**View the resource library of DataWorks**

In the left-side navigation pane of the **Resource Library** tab, click **DataWorks**. On the page that appears, you can view the resource usage in DataWorks. For DataWorks, the Resource Library tab displays the trend chart of slot usage, list of slot usage, and proportion of idle slots.

**View the resource library of DataHub**

In the left-side navigation pane of the **Resource Library** tab, click **DataHub**. On the page that appears, you can view the resource usage in DataHub. For DataHub, the Resource Library tab displays the trend chart of storage usage, list of storage usage, and proportion of idle storage.

**Perform other operations in charts or lists**

You can sort and filter records of CU and storage usage by column to facilitate information retrieval. For more information, see Common operations.

### 4.3 Check service health status

In the Apsara Big Data Manager (ABM) console, the Degree of health tab allows you to view the monitoring items of each big data service and the alerts of different severity levels and check the monitoring items and alerts again after the alerts are handled. This topic describes how to view and filter health data in ABM including the monitoring item, monitoring source, and severity level.

**Procedure**

1. Log in to the ABM console.
After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You can click the icon in the upper-left corner and select the big data service that you want to view.
2. In the top navigation bar, click **Monitoring**.
3. Click the **Degree of health** tab to view the health check results.
On the Degree of health tab, you can view the monitoring items, monitoring sources, and severity levels. You can also view monitoring details and filter data based on your business requirements.

### 4.4 View reports

The report feature allows you to view the inspection reports of big data services, including the report ID, report name, and report template. This topic describes how to use the report feature in Apsara Big Data Manager (ABM) and view inspection reports as needed.

**Procedure**

1. Log on to Apsara Bigdata Manager.
2. Click the
icon in the upper-left corner. Then select **DataHub**.
3. In the top menu bar, click **Monitoring**.
4. Click the **Report** tab to view the reports.
On the Report tab, you can view the information about each report in the following columns: Id, Report Name, Product, Template Name, Instance Type, Created By, and Created At. You can also view the details of each report.

## 5 O&M

### 5.1 ABM O&M feature and page

This topic describes the O&M feature of Apsara Big Data Manager (ABM) and how to go to the O&M page.

**Introduction to the ABM O&M feature**

The O&M page of ABM displays the Business operation and maintenance module. The following table describes the features of this module.

| Module | Feature | Description |
|---|---|---|
| Business operation and maintenance | Timed Job Statistics | Allows you to view the product-level statistics of cron jobs. Allows you to view the trend charts of channel engine scheduling. Allows you to view the trend charts of instances that have execution errors. |

**Go to the ABM O&M page**

1. Log in to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **ABM**.
3. In the top navigation bar of the **ABM** page, click **Operation and maintenance**. The
**Operation and maintenance** page displays the **Business operation and maintenance**
module.

### 5.2 Business O&M

#### 5.2.1 View cron jobs

Apsara Big Data Manager (ABM) allows you to view the trend charts of cron jobs of each big data service, channel engine scheduling, and instances with execution errors. This helps you understand the execution status of jobs. This topic describes how to view cron job statistics and the execution history of cron jobs in ABM.

**Procedure**

1. In the upper-left corner of the ABM console, click the
icon and select **ABM**.
2. In the upper-right corner of the **ABM** page, click **Operation and maintenance**. By default,
the **Business operation and maintenance** page appears.
3. In the left-side navigation pane, click **Timed Job Statistics** to view cron job statistics and
other information.
4. Optional. Find the service that you want to view and click **View History** in the **Operation**
column. The **Management** page of the service appears. You to view the job execution history on the Execution History tab.

#### 5.2.2 Create and configure a zone-disaster recovery project in MaxCompute

**recovery project in MaxCompute**

This topic describes how to create and configure a zone-disaster recovery project in MaxCompute, including the procedure, key parameters, and usage notes. You can properly configure a zone-disaster recovery project to prevent resource competition among clusters, ensure stable data synchronization, and optimize synchronization policies to reduce the consumption of bandwidth and storage resources.

**Background**

To avoid competition among clusters for resources such as bandwidth and storage space, you can create disaster recovery projects based on your business requirements.

**Usage notes**

When you configure a disaster recovery project, take note of the following items: If the **EnableEvent** parameter is set to `true` , the data in the project is synchronized immediately after it is changed. Additionally, the amount of data that is synchronized each time is all data in the table or partition. For example, if a non-partitioned table contains 1 TB of data and one data entry needs to be inserted into the table, the entire 1 TB of data must be copied to the secondary data center. If the data entry is written 10 times within 1 minute, the 1 TB of data is copied to the secondary data center 10 times within 1 minute. As a result, 9 TB of data needs to be recycled. Therefore, we strongly recommend that you disable real-time replication to reduce the bandwidth and storage pressure on data centers. We also recommend that you configure a periodic replication policy. For example, you can set the **ScanMetaInterval** parameter to 6 hours, which means that the metadata is scanned and replicated every 6 hours. That is,
**EnableEvent** = `false` and **ScanMetaInterval** = `21600` . Note that 6 hours is equal to
21,600 seconds. To prevent MaxCompute from consuming the full bandwidth of the cluster during peak hours, we recommend that you specify the **InstanceCount** parameter to limit synchronization bandwidth. Each InstanceCount uses approximately 10 MB to 50 MB of bandwidth. If the Recovery Point Objective (RPO) is always greater than the synchronization interval, the amount of data to be synchronized is very large and all data cannot be synchronized at a time. Solutions: i. Check the disk space usage of the secondary cluster and determine whether the data synchronization failure is caused by insufficient cluster disk space. You can use one of the following methods for inspection: Log in to the Apsara Uni-manager Management Console to view the disk space usage of the secondary cluster. Log in to the MaxCompute AG in the secondary data center and run the following command to view the disk space usage of the secondary cluster. The unit of disk space is bytes (B). To convert a value in bytes to gigabytes (GB), divide the value by 1024 × 1024 × 1024. The ${projectName} parameter needs to be replaced with the actual project name.

```
pu quota /product/aliyun/odps/${projectName}
```

ii. Adjust the following two parameters based on the actual volume of data to be synchronized and the bandwidth and RPO requirements: Increase the value of the ScanMetaInterval parameter. This results in a larger RPO but ensures data consistency to the maximum extent. Increase the value of the InstanceCount parameter. This results in a larger bandwidth used for data synchronization. Therefore, pay attention to the bandwidth of the primary and secondary data centers to avoid affecting data synchronization of other services. We recommend that you specify the value of the InstanceCount parameter as available bandwidth × 0.5/project data to be synchronized/50 MB based on the bandwidth of the on-premises primary and secondary data centers. For example, if the acceptable RPO is 1 day and the amount of data to be synchronized is 1 TB, the value of the InstanceCount parameter is calculated as 1 TB/(24 × 60 × 60) . To ensure sufficient bandwidth, you can multiply the calculated result by 2.

**Create a disaster recovery project**

Log in to the Apsara Uni-manager Management Console as an administrator and create a multi-cluster project. For more information, see **Apsara Stack Help CenterBig Data Services > MaxCompute**
**> User Guide > Preparations > Create a project**.

> **Note:** Single-cluster projects do not support disaster recovery.

**Configure the disaster recovery project**

1. Log in to the Apsara Big Data Manager (ABM) console.
2. In the upper-left corner, click the
icon and choose **Big Data Computing >**
**MaxCompute**.
3. In the upper-right corner of the page that appears, click Operation and maintenance. The
**Business operation and maintenance** tab is displayed by default. In the left-side
navigation pane, choose **Project Management > Project List**.
4. Find the project that you want to configure and click **Update replication status** in the
**Actions** column.
5. In the **View Multi-Cluster Replication configuration** panel, set the **Open** parameter to
**true** and specify the required information in the **Configuration** field.
The following table describes the key configuration items.

| Parameter | Key parameter | Description |
|---|---|---|
| Open | / | Valid values: true: enables multi-cluster replication. false: disables multi-cluster replication. Default value: false. |
|   | ScanMetaInteva l | The data synchronization interval. Unit: seconds. |

| er Guide·O&M | Apsara Big Data Manage |   |
|---|---|---|
| Configuration |   |   |
|   | InstanceCount | The data synchronization bandwidth. |
|   | SyncObject | The synchronization cluster and the type of data to be synchronized. Change the name of the MaxCompute cluster to the name of the on-premises primary or secondary cluster, as shown in the preceding figure, to enable full data replication in MaxCompute. Important The name of the MaxCompute cluster must be in uppercase letters. |
|   | EnableEvent | Specifies whether data is synchronized in real time. When this parameter is set to true , any data in the primary cluster changes is immediately synchronized to the secondary cluster, and the ScanMetaInteval parameter becomes invalid. Important If you enable real-time synchronization or specify a short data synchronization interval, more network bandwidth is consumed. We recommend that you disable real-time synchronization and increase the data synchronization interval when you need to synchronize a large amount of data. |

6. Optional. After you modify the parameters in the**Configuration**field, click**Compare**
**Versions**to view the highlighted version differences.
7. Confirm the correctness of parameter configurations and click **Run**.

> **Note:** If the modified configurations do not take effect, the reason may be that the zone- disaster recovery feature of ABM is not enabled. In this case, contact Apsara Stack technical support.

## 6 Management

### 6.1 Overview

The management module is the configuration and software management center of Apsara Big Data Manager (ABM). As the core module that supports personalized O&M on big data services, it provides features such as job services, health management, process services, operational audit, and data log management to improve O&M efficiency and management capabilities. The management module provides the following features: Job Services: allows you to run jobs to perform O&M operations on big data services. Health Management: allows you to create health check items and apply them to service hosts. Process Services: allows you to view pending and completed manual tasks, view process information including flowcharts and XML definitions, and view the information about process instances in different states, such as Running, Complete, Exception, and Terminated. Operational Audit: allows you to view the job execution records and other service O&M operations in ABM. Data Log Management: allows you to collect logs from Logstores of databases such as MySQL, PolarDB, and PolarDB-X, as well as data logs of DataWorks, DataHub, and Hologres. The collected data logs are stored in a specific sls-pub Project, which are used to address issues of inconsistent and insufficiently accessible data logs, audit logs, and data metrics across databases and big data services.

### 6.2 Jobs

#### 6.2.1 Overview

This topic describes the terms, interface layout, and core modules of Apsara Big Data Manager (ABM) job services for DataHub. This topic also describes how to create, execute, and manage regular jobs and cron jobs. Jobs can be manually executed and automatically scheduled. This helps you efficiently perform O&M operations on big data services.

**Background information**

ABM allows you to execute jobs to perform O&M operations on big data services. Jobs in ABM are executed to perform O&M operations on physical devices in a cluster. The Job Services module contains the **Job Execution** page.

**Terms**

Terms related to jobs include: Regular job: A job that can only be manually executed. No timer settings are specified for such a job. Cron job: A job that is automatically executed based on timer settings.

**Job Execution page**

The **Job Execution** page contains the following tabs:

| Tab | Description |
|---|---|
| Jobs | You can view and execute regular jobs and view their execution history. You can search, copy, export, and delete regular jobs. |
| Cron Jobs | You can enable, disable, view, or execute cron jobs, and view their execution history. You can search, copy, export, and delete cron jobs. |
| Execution History | You can view the execution history of regular and cron jobs. You can search, view details of, and preview job execution history. |

#### 6.2.2 Jobs

##### 6.2.2.1 Manually execute a job

After a regular job is created, you must manually execute it to complete O&M operations. You can also manually execute cron jobs based on your business requirements. This topic describes how to manually execute a job in Apsara Big Data Manager (ABM). You can select the service, configure execution parameters, and view execution history of the job. This helps you flexibly perform O&M jobs. In this topic, DataHub is used.

**Prerequisites**

An ABM administrator account is obtained.

**Procedure**

1. Log in to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select DataHub.
3. In the top navigation bar, click **Management**.
4. In the left-side navigation pane, click **Job Services**.
5. On the **Job Execution** page, click the **Jobs** tab.
If you need to manually execute a cron job, click the **Cron Jobs** tab. The procedure for manually executing a cron job is the same as that for a regular job. In this topic, a regular job is used.
6. On the **Jobs** page, find the job that you want to execute and click **Run** in the Actions
column.
7. In the dialog box that appears, configure the required parameters in the **Configure target**
**group and parameters** step and click **Next Step**.
8. In the **Confirm Risk** step, confirm the risks and click **Confirm**.

**Note**

A record is automatically generated on the **Execution History** tab. For more information, see View job execution history.
9. On the job execution page, click **Start** in the upper part to execute the job.
If you exit the job execution page without performing any operations, you can find the execution record on the **Execution History** tab and click **Details** in the **Actions** column to go to the job execution page.

##### 6.2.2.2 View cron jobs

A cron job is enabled by default and automatically executed. On the Cron Jobs tab, you can view and manage existing jobs. You can manually run, copy, export, or delete existing jobs.

**Prerequisites**

An Apsara Big Data Manager (ABM) administrator account is obtained.

**Procedure**

1. Log in to the ABM console.
2. In the top navigation bar, click **Management**.
3. In the left-side navigation pane, click **Job Services**.
4. On the **Execution** page, click the **cron job** tab.
5. On the cron job page, all cron job are in the**Effective**state. You can perform the following
operations in the Actions column:

| View | : View the detailed configurations of the job |
|---|---|

| History | : View the execution history of the job. |
|---|---|

| Execute | : manually triggers an immediate execution. |
|---|---|

| Copy | : creates a job based on the current job |
|---|---|

| Export | : exports job configurations. |
|---|---|

| Delete | : deletes the cron job. |
|---|---|

##### 6.2.2.3 View the execution history of a job

Apsara Big Data Manager (ABM) allows you to view the execution history of a specific job to understand its execution status.

**Background information**

After you confirm to run a job, ABM generates execution logs for the job. You can understand the execution status based on the log data. The **Execution History** page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter configuration information, and allows you to download job execution details. Allows you to perform certain operations depending on the job status. For example, you can
**Start** a job that is in the **Pending** state or **Retry** the execution of a job that is in the
**Exception** state.
This topic describes how to view the execution history of a regular job. You can follow a similar procedure to view the execution history of a cron job.

**Prerequisites**

An ABM administrator account is obtained.

**Procedure**

1. Log on to Apsara Bigdata Manager.
2. Click the
icon in the upper-left corner and select DataHub.
3. In the top menu bar, click **Management**.
4. In the navigation pane on the left, click **Job Service**.
5. On the **Job Execution** page, click the **Jobs** tab.
6. On the **Jobs** page, click **History** in the Actions column of a regular job. The **Execution**
**History** tab appears.
On the **Execution History** tab, you can view the execution history of this job. For more information, see View job execution history.

##### 6.2.2.4 View job execution history

DataHub lets you view the execution history for a specific job or for all jobs. This helps you monitor job and plan execution.

**Background information**

After you confirm job or plan execution, DataHub records execution details for each job. You can review these details later. The **Execution History** page supports the following features: View information such as the task’s trigger method, current status, start time, and end time. View the task execution procedure and parameter settings. You can also download detailed task execution information. Perform different operations based on the task’s status. For example, you can **Start** a task that is **Not Started** or **Retry** a task that is **Abnormal**. Execution history information is identical for regular jobs and scheduled jobs. This topic uses a regular job as an example.

**Prerequisites**

You have an Apsara Bigdata Manager administrator account.

**View a specific job's execution history**

1. Log on to Apsara Bigdata Manager.
2. Click the
icon in the upper-left corner and select DataHub.
3. In the top menu bar, click **Management**.
4. In the navigation pane on the left, click **Job Service**.
5. On the **Execution** page, click the **Job List** tab.
6. On the **Job List** page, click **History** next to the regular job that you want to view. This
opens the **Execution History** page. On the **Execution History** page, you can view the job’s execution history. For more information, see View job execution history.

**View execution history**

1. Go to the **Execution History** page. If many history records exist, filter them by instance
name, time range, or execution status. Then, click **Search** to find matching records.
2. Click **Operation > Details** for a history record to view its details.
Available operations depend on the status of the history record:

| Task execution record status | Supported feature | Procedure |
|---|---|---|
| All statuses | View parameter settings | Click Parameter Settings at the top. Select Context Parameters or Global Parameters to view the context or global parameters for the task. |
|   | Download execution details | Click Download Execution Details at the top to download the job execution details to your local machine as a .txt file. The execution details include information such as the execution JSON and raw data. |
|   | View step execution details | On the Machine Details page for a step, click View Details next to a machine. The execution details for that step on the machine appear on the right, including the execution outputs. If it is a script step, the Script Content and Runtime Parameters pages are displayed. You can view the script content and runtime parameters. If it is a command step, the Command Content and Runtime Parameters pages are displayed. You can view the command content and runtime parameters. |
|   | Refresh the interface | If the task is running, click Refresh at the top to view the latest execution status. |
| Not Started | Start execution | Click Start at the top to begin execution. |
|   | Cancel execution | Click Cancel at the top to cancel execution. |

| Pending Manual Confirmation | Complete manual operation and confirm | In the manual step that requires an operation, perform the required actions as prompted. Then, click Confirm to proceed to the next step. |
|---|---|---|
|   | Roll back to the state after the previous step was completed | In the manual step that requires an operation, click Rollback to return to the state after the previous step was completed. |
|   | Cancel execution | Click Cancel to cancel this execution. |
| Abnormal | Retry the abnormal step | In the abnormal step, click Retry to execute the step again. |
|   | Skip the abnormal step | In the abnormal step, click Skip to skip this step and continue with the subsequent steps. |
|   | Roll back to the state after the previous step was completed | In the abnormal step, click Rollback to return to the state after the previous step was completed. |
|   | Reset the abnormal step to the Not Started state | In the abnormal step, click Reset to reset the step to the Not Started state. When an abnormal step is reset to the Not Started state, the execution status changes to Paused. You can then click Continue at the top to re-execute the current step. |
|   | View abnormal step execution details | On the Machine Details page for a step, click View Details next to a machine. The execution details for that step on the machine appear on the right, including execution outputs and error messages. For a machine where the execution was abnormal, after you view the details, you can click Skip to skip this machine or click Retry to execute the step again on the machine. If it is a script step, the Script Content and Runtime Parameters pages are displayed. You can view the script content and runtime parameters. If it is a command step, the Command Content and Runtime Parameters pages are displayed. You can view the command content and runtime parameters. |
|   | Retry the failed step | In the failed step, click Retry to execute the step again. |
|   | Skip the failed step | In the failed step, click Skip to skip this step and continue with the subsequent steps. |

| er Guide·Manageme |   |   |
|---|---|---|
| Failed |   |   |
|   | Roll back to the state after the previous step was completed | In the failed step, click Rollback to return to the state after the previous step was completed. |
|   | Reset the failed step to the Not Started state | In the failed step, click Reset to reset the step to the Not Started state. When a failed step is reset to the Not Started state, the execution status changes to Paused. You can then click Continue at the top to restart the current step. |
|   | View failed step execution details | On the Machine Details page for a step, click View Details next to a machine. The execution details for that step on the machine appear on the right, including execution outputs and error messages. For a machine where the execution was abnormal, after you view the details, you can click Skip to skip this machine or click Retry to execute the step again on the machine. If it is a script step, the Script Content and Runtime Parameters pages are displayed. You can view the script content and runtime parameters. If it is a command step, the Command Content and Runtime Parameters pages are displayed. You can view the command content and runtime parameters. |
|   | Cancel execution | Click Cancel at the top to cancel the execution. |

### 6.3 Health management

#### 6.3.1 Monitoring configuration

Apsara Big Data Manager provides a variety of built-in scheduling items and monitoring items for each product. These items are used to detect product faults and generate alerts. This helps you detect and fix product faults in a timely manner.

**Prerequisites**

A Apsara Big Data Manager account with the required O&M permissions is obtained. You have obtained the alert sources and check items of the monitoring items.

**Background information**

> **Note:** Different products have different scheduling items and monitoring items, but their configurations and operation methods are the same. .

Scheduling item: The scheduling item runs the scheduling script in the full machine list corresponding to the specified tianji role to generate the raw data of the alarm (which scheduling item generates what level of alarm on which machine and what is the alarm result data). The raw data is reported to the database of ABM for storage. Monitoring item: The monitoring item mounts the alarm raw data generated by the scheduling item to the page of the corresponding product in ABM. When you attach a metric to a product page, you can configure different filter policies to filter the alert results of the metrics you are concerned about on the specified page. Both scheduling items and monitoring items are built-in and cannot be added. However, you can modify some parameters of scheduling items and monitoring items, such as whether to enable, running parameters, and description. You can also configure mount points and delete them.

**Go to the management page**

1. Log on to the Apsara Big Data Manager.
2. Click the
icon in the upper-left corner and select the target product.
3. In the top navigation bar, click **Management**.

**Scheduling Management**

**View the details and mount points of a scheduling item**

The mount point of a scheduling item is built-in and cannot be added, modified, or deleted. The mount points of scheduling items correspond to the list of all hosts corresponding to the Apsara Infrastructure Management role that runs the scheduling script.
1. In the left-side navigation pane, click **Health Management**. The **Scheduling** tab of the
**Monitoring Configuration** page appears by default.
The **Scheduling** tab displays all scheduling items of the service.
2. On the **Scheduling** tab, find the scheduling item that you want to view and click **View** in
the Actions column to view the details of the scheduling item. The details of the scheduling item include the checker name, checker alias, description, and processing steps.
3. On the Scheduling tab, find the scheduling item that you want to view and click the
icon on the left to view the mount points of the scheduling item.

**Modify a scheduling item**

You can configure the scheduling interval and running parameters of a scheduling item, and configure whether to enable the scheduling item.
1. In the left-side navigation pane, click **Health Management**. The **Scheduling** tab of the
**Monitoring Configuration** page appears by default.
2. On the **Scheduling** tab, find the scheduling item that you want to manage and click **Edit** in
the Actions column. In the Modify Checker dialog box, configure the parameters.
**Type**: If you set this parameter to **System Default**, other parameters, such as **Execution**
**Interval** and **Parameters**, are set to the default values. If you set this parameter to
**Custom**, you can configure other parameters as needed.

> **Note:** Configure the **Execution Interval** parameter based on the **crontab** command.

3. Click **OK**. The scheduling item is modified.

**View the list of faulty machines**

You can view all the faulty hosts in the current cluster.
1. In the left-side navigation pane, click **Health Management**. The **Scheduling** tab of the
**Monitoring Configuration** page appears by default.
2. Click **Faulty Servers** in the upper-right corner to view the faulty hosts in the cluster.
The list of faulty hosts shows all faulty hosts in the current cluster and the role of each host in Apsara Infrastructure Management.

**Basic monitoring**

**Add a metric**

You can manually add metrics.
1. In the left-side navigation pane, click **Health Management**. The **Monitoring**
**Configuration > Scheduling** page appears.
2. Click the **Monitoring** tab.
The **Monitoring** page displays all metrics of the current product.
3. Click **Create Monitoring Item** and configure the parameters.
4. After you configure the preceding parameters, click **OK**. A message appears, indicating that
the creation is successful.

**Modify a metric**

You can modify the name and description of a metric and set whether to enable the metric. The alert sources and check items of the monitoring items are built-in. Do not modify them.
1. In the left-side navigation pane, click **Health Management**. The **Monitoring**
**Configuration > Scheduling** page appears.
2. Click the **Monitoring** tab.
The **Monitoring** page displays all metrics of the current product.
3. Click **Edit** next to a metric to modify the configurations of the metric.
4. After you configure the preceding parameters, click **OK**. A message appears, indicating that
the modification is successful.

**Add a mount point to a metric**

You can add a mount point to mount the alarm raw data to the O&M interface of each product in ABM.
1. In the left-side navigation pane, click **Health Management**. The **Monitoring**
**Configuration > Scheduling** page appears.
2. Click the **Monitoring** tab.
3. Click the
icon in front of a metric to view the mount point of the metric.
4. Click **Add Mount Point** below the mount point list. In the dialog box that appears, set the
parameters. The following table describes the key parameters.

| Parameter | Description |
|---|---|
| Mount Point | The mount point to which the required check result of this monitoring item that you want to mount. For example, the value odps/host specifies that the result is mounted to the host O&M page of MaxCompute. |
| Filter Policy | The filtering policy. Valid values: None: All alerts generated by the monitoring item are displayed. Custom: The alerts generated by the monitoring item in accordance with the filter configured for the service tree node are displayed. Node Name: The alerts whose node name is the same as the name of the current node are displayed. |
| Effective | Sets whether the mount point takes effect. |

5. After you configure the preceding parameters, click **OK**. A message appears, indicating that
the modification is successful.

**Delete the mount point of a metric**

1. Go to the management page. In the left-side navigation pane, click **Health Management**.
The **Monitoring Configuration > Scheduling** page appears.
2. Click the **Monitoring** tab.
3. Click the
icon in front of a metric to view the mount point of the metric.
4. Click **Delete** next to the mount target. In the message that appears, click **OK**. A message is
displayed, indicating that the mount target is deleted.

**Delete a metric**

1. Go to the management page. In the left-side navigation pane, click **Health Management**.
The **Monitoring Configuration > Scheduling** page appears.
2. Click the **Monitoring** tab.
3. Find the monitoring item that you want to delete and click **Delete** in the Actions column. In
the message that appears, click **OK**. The monitoring item is deleted.

#### 6.3.2 Inspection management

The inspection management feature of Apsara Big Data Manager (ABM) allows you to configure inspection scenarios, inspection items, and scenario combinations based on your business requirements.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M.

**Go to the Management page**

1. Log in to the ABM console.
2. In the upper-left corner, click the
icon and select the big data service that you want to manage.
3. In the top navigation bar, click **Management** to go to the Management page.

**Create a scenario**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Scenes**.
2. In the upper-right corner of the Scenes tab, click **Create Scene**. In the Create Scene panel,
configure the parameters based on your business requirements.
3. Click **Submit**.
After a scenario is created, you can **Edit**, **Start Patrol**, **Manage Patrol Items**, and view
**Execution History** of the scenario.

**Create an inspection item**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Patrol Items**.
2. In the upper-right corner of the Patrol Items tab, click **Create Patrol Item**.
3. In the **Create Patrol Item** panel, configure the parameters based on your business
requirements.
4. Click **Submit**.
After an inspection item is created, you can **Edit** and **Delete** the inspection item.

**Create a scenario combination**

1. In the left-side navigation pane, click **Health Management**. On the page that appears,
choose **Patrol Configuration > Scenario Combination**.
2. In the upper-right corner of the Scenario Combination tab, click **Create Scene**.
3. In the **Create Scene** panel, configure the parameters based on your business
requirements.
4. Click **Submit**.
After a scenario combination is created, you can **Edit**, **Manage Patrol Items**, and view
**Execution History** of the scenario combination.

### 6.4 Operation audit

The operation audit feature allows you to view the **O&M** operation history of the current big data service managed by Apsara Big Data Manager (ABM). The details of each operation are provided for data retrieval and fault locating.

**Prerequisites**

Your ABM account is granted the required permissions on the services on which you want to perform O&M.

**Background information**

You can view operation audit logs by service. For example, to view the operation audit logs of a big data service, you must go to the service page first.

> **Note:** The Operational Audit page displays only the **O&M** operation history of a big data service. Note that the O&M operations of job services are not included.

**Procedure**

1. Log in to the ABM console.
2. In the upper-left corner, click the
icon and select the big data service whose O&M operation history you want to view.
3. In the top navigation bar, click **Management**. In the left-side navigation pane, click
**Operational Audit**.
The **Operational Audit** page displays the **O&M** operation history of the current big data service, including various parameters such as Operation Name, Operation ID, Risk, Current Status, Submitted At, Started At, Ended At, Operator, Type, Parameters, and Details.
4. Click **Details** for an operation to view the O&M operation details.

## 7 FAQ

### 7.1 How do I view service cluster traffic?

**traffic?**

This topic uses MaxCompute as an example to describe how to view and analyze the port traffic of service clusters in the Network Operations Console. This helps you optimize network performance and troubleshoot faults.

**Problem description**

How do I query the inbound and outbound traffic of a MaxCompute cluster at a specific time, and locate the corresponding vSwitch and port?

**Solution**

**Step 1: Obtain the hostname**

1. Log in to the ABM console.
2. After you log in to the **ABM** console, the **Instrument cluster** tab appears by default. You
can click the icon in the upper-left corner and then choose **Big Data Computing >**
**MaxCompute**.
3. On the MaxCompute page, click **Operation and maintenance** in the top navigation bar.
Then, click the **Cluster O & M** tab.
4. On the **Machine List** tab, you can view the **Hostname** information of all machines in the
cluster.

**Step 2: View the information about the vSwitch and port**

**connected to the host**

1. Log in to the OPS server.
2. Obtain the vSwitch and port information based on **Hostname**.
Run the following command with the `hostname` parameter set to the actual name of the current host to obtain the information about the vSwitch and port connected to the host.

> **Note:** If you want to view the vSwitch and port traffic of other service clusters, replace the
> `hostname` parameter with the `hostname` of the machine in the service cluster to be queried.

```
$curl -s 'http://127.0.0.1:7070/api/v5/GetMachineInfo? hostname=c27***.cloud.c07.amtest35&attr=uplink_info'
```

**Step 3: View the traffic of vSwitch ports**

Log in to the **Network Operations Console** to view the inbound and outbound traffic of the vSwitch ports.
1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network > Network Element**
**Management** to go to the Network Element Management page.
You can view the inbound and outbound traffic of the vSwitch ports based on the obtained IP address and port information. For more information, see **Basic network > Network**
**element management** in **VPC Operations and Maintenance Guide** .

## 8 Go to other consoles

Apsara Big Data Manager (ABM) provides links to the Apsara Uni-manager Operations Console (ASO) and the Apsara Infrastructure Management console to facilitate the O&M of big data services.

**Prerequisites**

An ABM account that works properly and its password are obtained.

**Procedure**

1. Log in to the ABM console.
2. On the homepage of the ABM console, click the
icon in the upper-left corner, and then click **ASO** or **TIANJI** in the **Site Navigation** section. The corresponding platform appears.

**Result**

After you click **ASO** or **TIANJI**, you can log in to the Apsara Uni-manager Operations Console or the Apsara Infrastructure Management console without the need to enter your username and password.
