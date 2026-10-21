---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager User Guide 20250225"
product_version: "V3.18.3"
doc_version: "20250225"
pdf_pages: 52
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager User Guide 20250225.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A4%A7%E6%95%B0%E6%8D%AE%E7%AE%A1%E5%AE%B6/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Big%20Data%20Manager%20User%20Guide%2020250225.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Big Data Manager User Guide 20250225

## Table of Contents

- 1 Apsara Big Data Manager
- 2 Common operations
- 3 Quick start
  - 3.1 Log on to the ABM console
  - 3.2 Set the theme of the console
  - 3.3 View the trace dashboards
  - 3.4 View the cluster running status
  - 3.5 View and clear cluster alerts
- 4 ABM
  - 4.1 ABM dashboard
  - 4.2 ABM repository
  - 4.3 O&M overview
  - 4.4 Cluster O&M
    - 4.4.1 Cluster overview
    - 4.4.2 Cluster health
  - 4.5 Host O&M
    - 4.5.1 Host overview
- 5 Management
  - 5.1 Overview
  - 5.2 Jobs
    - 5.2.1 Overview
    - 5.2.2 Jobs
      - 5.2.2.1 Enable or disable a cron job
      - 5.2.2.2 Manually run a job
      - 5.2.2.3 View the execution history of a job
    - 5.2.3 View execution history
  - 5.3 Health management
  - 5.4 Operation auditing
- 6 Go to other consoles

ager

## 1 Apsara Big Data Manager

Apsara Big Data Manager (ABM) is an operations and maintenance (O&M) platform tailored for big data services. ABM supports monitoring, management, and O&M in multiple dimensions, such as business, services, clusters, and hosts. Customer O&M teams or on-site personnel can easily complete unified O&M of big data services based on the service capabilities of ABM. ABM supports the following services: MaxCompute DataWorks Realtime Compute (Blink) Quick BI DataHub E-MapReduce ABM supports O&M on big data services from the perspectives of business, services, clusters, and hosts. ABM also allows you to update big data services, customize alert configurations, and view the O&M history.

## 2 Common operations

The data tables and legends in the Apsara Big Data Manager (ABM) console help you perform common operations. This topic uses MaxCompute to describe the common operations. The data tables and legends in the ABM console help you perform common operations. This topic uses MaxCompute to describe the common operations.

**Search**

You can search for an item in a table by column, which is similar to filtering projects. For example, you can perform the following steps to search for a checker:
1. Log on to the ABM console. In the upper-left corner of the ANM console, click the More icon
and select MaxCompute. In the upper-right corner of the **MaxCompute** page, click **O&M**. On the page that appears, click the **Clusters** tab. On the Clusters page, click the **Health**
**Status** tab.
2. In the checker list, click the **Filter** icon in a column and enter a keyword in the search box.
3. Click **Search**. The checkers that meet the requirements appear.
4. If the search result is not met your business requirements, you can continue performing
this operation on other columns.

**Sort items based on a column**

You can sort items based on a column in ascending or descending order. The procedure and display method are different from those described in Common operations.
1. Log on to the ABM console. In the upper-left corner of the ANM console, click the More icon
and select MaxCompute. In the upper-right corner of the **MaxCompute** page, click **O&M**. On the page that appears, click the **Clusters** tab. On the Clusters page, click the **Health**
**Status** tab.
2. In the checker list, click a column heading or the sort icon in the column heading to sort
checkers in ascending order or descending order. The highlighted up arrow indicates that the checkers are sorted in ascending order. The highlighted down arrow indicates that the checkers are sorted in descending order.

**View the trend charts for a MaxCompute cluster**

Log on to the ABM console. In the upper-left corner of the ANM console, click the More icon and select MaxCompute. In the upper-right corner of the **MaxCompute** page, click **O&M**. On the page that appears, click the **Clusters** tab. On the Clusters page, you can view relevant metrics, such as CPU and memory usage, of the desired cluster. The following example describes the CPU usage of a cluster. The trend chart displays the trend lines of the total CPU usage (cpu), CPU usage for executing code in kernel space (sys), and CPU usage for executing code in user space (user) for the specified cluster over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the CPU utilization of the cluster in the specified period.

## 3 Quick start

### 3.1 Log on to the ABM console

This topic describes how to log on to the Apsara Big Data Manager (ABM) console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

2. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
3. Click **Log In**.
4. In the top navigation bar of the Apsara Uni-manager Operations Console, click **Products**.
5. In the **Big Data** section, click **Apsara Bigdata Manager** to go to the homepage of the
ABM console.

### 3.2 Set the theme of the console

You can set the theme of the Apsara Big Data Manager (ABM) console to dark or bright based on your preferences. By default, the dark theme is used.

**Prerequisites**

An ABM account and the corresponding password are obtained.

**Procedure**

1. Log on to the ABM console.
2. Set the theme of the ABM console to dark or bright based on your preferences.

| Theme | Description |
|---|---|
| Bright | If the dark theme is used, you can move the pointer over the username in the upper-right corner and turn off the switch to change to the bright theme. |
| Dark | If the bright theme is used, you can move the pointer over the username in the upper-right corner and turn on the switch to change to the dark theme. |

### 3.3 View the trace dashboards

The dashboard is used to display the key operation metrics of MaxCompute and DataWorks products, as well as alarms of all big data products. This allows you to understand the operation status of big data products as a whole.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M.

**Background information**

The dashboard is a feature of the ABM console. As the homepage of the ABM console, the dashboard allows you to view the overall running information about all big data services.

**Procedure**

1. Log on to the ABM console.
After logging in to the Apsara Big Data Manager, the default display **Dashboard** page. If you are currently on another page, you can click the icon and select **ABM** products to enter **Dashboard** page.
2. View and clear service alerts.
In the alert list, view the number of alerts for all big data products. **Critical** and **Warning** type alarms must be fixed in a timely manner. i. In the **Dashboard On the** page, click the **Critical** or **Warning** quantity, into the product
**Cluster O&M > Health** page.
In the **Health** On the page that appears, you can view all check items of the product. ii. Click the **Details** to view the details of the check item and the alert solution of the check item, and press **Solution The steps in** to handle alerts. iii. Log on to the hosts on which the alerts are detected to handle the alerts. Click in front of the check item that has an alarm. **Fold** icon, and then click the **Logon** icon. iv. In the newly opened **TerminalService** On the page that appears, select a host on the left to log on.
3. In the **Dashboard** On the page that appears, click the **MaxCompute** , view **MaxCompute**
.
**MaxCompute The** section displays the job running overview, control system saturation,
data import traffic, computing resource usage, storage resource usage, and the logical and physical CPU usage trend charts of the MaxCompute cluster.
4. In the **Dashboard** On the page that appears, click the **DataWorks** , view **DataWorks** .
**DataWorks The** section displays the node scheduling overview, slot resource overview,
and the cumulative trend chart of task completion in the DataWorks cluster.

### 3.4 View the cluster running status

**status**

Apsara Big Data Manager (ABM) provides you with several operation metrics of clusters, such as CPU usage, memory usage, load, storage, and health check result. This helps you understand the running status of clusters at any time. Based on relevant metrics, you can evaluate whether the selected cluster has operation risks.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background information**

In the ABM console, the procedures of viewing the cluster running status for different services are the same. This topic uses one of the services as an example.

**Procedure**

1. Log on to the ABM console.
2. Click
in the upper-left corner and then click a service.
3. On the page that appears, click **O&M** in the upper-right corner, and then click the **Clusters**
tab.
4. On the **Clusters** page, select a cluster in the left-side navigation pane. The **Overview** page
for the cluster appears. On the **Overview** page, you can view the host status, service status, health check result, and health check history of the selected cluster. You can also view the trend charts of CPU usage, disk usage, memory usage, load, and packet transmission for the cluster.

**What to do next**

You can evaluate the operation risks of a cluster based on the metrics such as the service status, CPU usage, disk usage, memory usage, and load. If the cluster has any Critical, Warning, or Exception alerts, you need to check and clear them in a timely manner. You need to pay special attention to the Critical and Warning alerts. For more information, see View and clear cluster alerts.

### 3.5 View and clear cluster alerts

If you find alerts on the cluster overview page, go to the cluster health status page to view and clear the alerts. This topic uses one Apsara Big Data Manager (ABM) service as an example to describe how to view and clear alerts.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background information**

In the ABM console, the procedures of viewing and clearing alerts for different services are the same. If a service has alerts, especially the Critical and Warning alerts, pay attention to them and clear them in a timely manner to make sure that the cluster can run properly.

**Procedure**

1. Log on to the ABM console.
2. Click
in the upper-left corner and then click a service.
3. On the **Clusters** page, select a cluster in the left-side navigation pane, and then click the
**Health Status** tab. The Health Status page for the cluster appears.
4. On the **Health Status** page, click **+** to expand a checker with alerts. You can view all hosts
where the checker is run.
5. Click a hostname. In the dialog box that appears, click **Details** in the Actions column of a
check result to view the alert causes.
6. On the **Health Status** page, click **Details** in the Actions column of the checker to view the
schemes to clear the alerts.
7. Clear the alerts according to the schemes.
To log on to a host with alerts for related operations, click the **Log On** icon next to the name of the host. On the **TerminalService** page that appears, click the hostname on the left to log on to the host.
8. After you clear an alert for a host, click **Refresh** in the Actions column of the host to run
the checker again for the host. In this way, you can check whether the alert is cleared.

## 4 ABM

### 4.1 ABM dashboard

The Apsara Bigdata Manager (ABM) dashboard shows key indicators of MaxCompute and DataWorks. The dashboard also provides information about the alerts for all big data services and helps you understand the overall status of these services. The dashboard also supports auto-refresh and full-screen display.

**Go to the Dashboard tab**

After you log on to the ABM console, the **Dashboard** tab appears by default. To return to the
**Dashboard** tab, click the
icon in the upper-left corner and click **ABM**. In the upper-left corner of the **Dashboard** tab, you can select a region from the drop-down list to view the cluster status of each big data service in the region.

**View and handle the alerts of various services**

In the Overview section, you can view the numbers of **Critical**, **Warning**, and **Exception** alerts that are reported for each big data service. If a service has alerts, especially **Critical** or
**Warning** alerts, handle these alerts on time.
1. On the **Dashboard** tab, find the check item of a service that you want to query, and click
the number in the **Critical** or **Warning** column of the service. The **Health Status** page for the service appears on the **Clusters** tab. On the **Health Status** page, you can view all the check items of the service.
2. Click **Details** in the Actions column of a check item for which alerts are reported. In the
Details dialog box, view the details of the check item and the descriptions to handle the alerts. Perform the steps provided in the **Description** section to handle the alerts.
3. Log on to the hosts on which the alerts are detected to handle the alerts.
Click the plus sign (+) to expand a check item with alerts, and click the **Log On** icon next to the name of a host with alerts. On the TerminalService page that appears, click the hostname on the left to log on to the host.

**View key indicators of MaxCompute**

The ABM dashboard shows the key indicators of MaxCompute. On the **Dashboard** tab, click
**MaxCompute** to view the information.
In the **MaxCompute** section, you can view the job status, the real-time capacity for the control system, computing resource usage, and storage resource usage. You can also view the trend charts of imported data traffic, logical CPU utilization, and physical CPU utilization.

**View key indicators of DataWorks**

The ABM dashboard shows key indicators of DataWorks. On the **Dashboard** tab, click
**DataWorks** in the **Monitoring** column to view the information.
In the **DataWorks** section, you can view the node scheduling and slot usage of a DataWorks cluster. You can also view the trend chart of the total number of daily finished tasks.

**Enable and disable auto-refresh**

By default, auto-refresh is disabled on the Dashboard tab, and the statistics of cluster metrics from the last two days are displayed on this page. You can specify a time range to view the metric statistics. If you enable auto-refresh, the system automatically updates the metric data of clusters based on the specified interval.
1. At the top of the **Dashboard** tab, click the
icon.
2. In the dialog box that appears, configure the **Refreshing every** and **Refreshing range**
parameters. The **Refreshing range** parameter specifies a time period for the trend charts, such as those for the CPU utilization and memory usage of each cluster.
3. After you configure these parameters, click **OK** to enable auto-refresh.
If auto-refresh is enabled, the icon is replaced with the icon. The system automatically updates all data on the dashboard based on the specified time interval. If you want to disable auto-refresh, click the icon.

**Display the dashboard in full-screen**

The dashboard supports full-screen display. This feature allows you to view the status of big data services. At the top of the **Dashboard** tab, click the icon to display the **Dashboard** tab in fullscreen mode.

### 4.2 ABM repository

The Repository page in the Apsara Big Data Manager (ABM) console displays the resource usage in MaxCompute and DataWorks. This topic describes the features of the ABM repository and how to access the Repository page.

**Entry**

1. Log on to the ABM console.

> **Note:** By default, the **Dashboard** page appears. To return to the **Dashboard** page from any other page, click
> in the upper-left corner and then click **ABM**.

2. On the **Dashboard** page, click the **Repository** tab. The **Repository** page appears.

**View the resource usage in MaxCompute**

In the left-side navigation pane of the **Repository** page, click **MaxCompute**. On the page that appears, you can view the resource usage in MaxCompute. For MaxCompute, the Repository page displays the trend charts of CU and storage usage, records of CU and storage usage, and proportions of idle CUs and storage.

**View the resource usage in DataWorks**

In the left-side navigation pane of the **Repository** page, click **DataWorks**. On the page that appears, you can view the resource usage in DataWorks. For DataWorks, the Repository page displays the trend chart of slot usage, records of slot usage, and proportion of idle slots.

**Other operations**

You can filter or sort records of CU, storage, and slot usage based on a column to facilitate information retrieval. For more information, see Common operations.

### 4.3 O&M overview

This topic describes the O&M modules of Apsara Big Data Manager (ABM) and how to go to the O&M page of ABM.

**O&M modules**

The O&M page of ABM provides the following modules: Business, Clusters, and Hosts. The following table describes these modules.

| Module | Submodule or feature | Description |
|---|---|---|
| Environment O&M | Single-Host Basic Components | Shows the status of single-host basic components within a cluster. |

**Go to the O&M page**

1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and click **ABM**.
3. In the upper-right corner of the ABM page, click **O&M**. By default, the **Business** tab
appears. The **O&M** page consists of the **Business** and **Environment O&M** modules.

### 4.4 Cluster O&M

#### 4.4.1 Cluster overview

The cluster overview page displays the trend charts of CPU usage, disk usage, memory usage, packet transmission, and load of an Apsara Infrastructure Management Framework cluster.

**Go to the Overview page of a cluster**

Log on to the Apsara Big Data Manager (ABM) console. Click the More icon in the upper-left corner and then click ABM. On the page that appears, click O&M in the top navigation bar, and then click the **Clusters** tab. On the Clusters tab, select a cluster in the left-side navigation pane. The **Overview** page of the cluster appears. The cluster overview page displays the trend charts of CPU usage, disk usage, memory usage, packet transmission, and load of a cluster. For more information, see the following sections.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the cluster in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the cluster in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the cluster in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the cluster over time in different colors. These trend lines reflect the data transmission status of the cluster. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the cluster in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the cluster in the specified period.

#### 4.4.2 Cluster health

On the cluster health status page, you can view all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any). In addition, you can log on to a host and perform manual checks on the host.

**Entry**

On the **Clusters** page, select a cluster in the left-side navigation pane, and then click the
**Health Status** tab. The Health Status page for the cluster appears.
On the **Health Status** tab, you can view all check items for the cluster and the check results for the hosts in the cluster. The following alerts may be reported on a host: **Critical**,
**Warning**, and **Exception**. The alerts are represented in different colors. You must handle the
alerts at the earliest opportunity, especially the **Critical** and **Warning** alerts. The following table describes the check results.

**View the details of a check item**

1. On the Health Status tab, find the check item whose details you want to view and click
**Details** in the Actions column. In the Details message, view the details of the check item.
The following information about the check item is displayed: **Name**, **Source**, **Alias**,
**Application**, **Type**, **Scheduling**, **Data Collection**, **Default Execution Interval**, and
**Description**. The schemes to clear alerts are provided in the description.
2. Click **Show More** to view more information about the check item.
You can view more information in the **Script**, **Target (TianJi)**, **Default Threshold**, and
**Mount Point** sections.

**View the hosts for which alerts are reported and causes for the**

**alerts**

You can view the check history and check results of a check item on a host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click a hostname. In the panel that appears, find the alert that you want to manage and
click **Details** in the Actions column to view the cause of the alert.

**Log on to a host**

You may need to log on to a host to handle alerts or other issues that occur on the host.
1. On the Health Status tab, click the **+** icon on the left of a check item to show all alerts that
are triggered by the check item. You can view all hosts on which the check item is run.
2. Click the **Login in** icon next to a hostname. The **TerminalService** page appears.
3. On the **TerminalService** page, click the hostname in the left-side navigation pane to log
on to the host.

**Run a check item again**

After you handle an alert for a host, click **Refresh** in the Actions column of the host to run the check item again for the host. This way, you can check whether the alert is cleared.

### 4.5 Host O&M

#### 4.5.1 Host overview

The host overview page displays the overall running information about a host in an Apsara Big Data Manager (ABM) cluster. On this page, you can view the root disk usage, total usage, 1-minute load, 5-minute load, 15-minute load, health check result, and health check history of the host. You can also view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for the host.

**Entry**

On the **Hosts** page, select a host in the left-side navigation pane. The **Overview** page for the host appears.

**Root Disk Usage, Total, and 1-Minute Load**

These sections display the root disk usage, total usage, and 1-minute load for the selected host. The Root Disk Usage section provides the usage of the /tmp directory. The Total section provides the system usage and user usage. The 1-Minute Load section provides the 1-minute, 5-minute, and 15-minute load averages.

**CPU**

The CPU chart shows the trend lines of the total CPU utilization, CPU utilization for running code in kernel space, and CPU utilization for running code in user space for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the CPU utilization of the host in the specified period.

**DISK**

The DISK chart shows the trend lines of the storage usage in the /, /boot, /home/admin, and /home directories for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the storage usage of the host in the specified period.

**MEMORY**

The MEMORY chart shows the trend lines of the memory usage, total memory size, used memory size, size of memory used by buffers, size of memory used by the page cache, and available memory size for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the memory usage of the host in the specified period.

**LOAD**

The LOAD chart shows the trend lines of the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the average loads for every 1 minute, every 5 minutes, and every 15 minutes for the host in the specified period.

**PACKAGE**

The PACKAGE chart shows the trend lines of the numbers of dropped packets, error packets, received packets, and sent packets for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in on the chart. You can specify the start time and end time in the upper-right corner of the enlarged chart to view the data transmission status of the host in the specified period.

**TCP**

This chart displays the trend lines of the number of failed TCP connection attempts (atmp_fail), that of the times of resetting TCP connections in the ESTABLISHED state (est_reset), that of active TCP connections (active), that of passive TCP connections (pasive), that of received TCP packets (iseg), and that of sent TCP packets (outseg) for the host over time in different colors. These trend lines reflect the TCP connection status of the host. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the TCP connection status of the host in the specified period.

**DISK ROOT**

This chart displays the trend line of the average usage of the root disk (/) for the host over time. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the average root disk usage of the host in the specified period.

**Health Check**

This section displays the number of checkers deployed for the host and the respective number of Critical, Warning, and Exception alerts. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health.

**Health Check History**

This section displays a record of the health checks performed on the host. Click **View Details** to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health. You can click the event content of a check to view the exception items.

## 5 Management

### 5.1 Overview

The management module is the configuration and software management center of Apsara Big Data Manager (ABM). It is an important functional module that supports and customizes O&M items for services. The management module supports the following features: Jobs: allows you to run jobs to perform O&M operations on big data products. API Management: allows you to manage the permissions of ABM APIs. Health Checks: allows you to create health check items and apply them to service hosts. Operation Logs: allows you to view the job execution records and other service O&M operations in ABM.

### 5.2 Jobs

#### 5.2.1 Overview

This topic describes the UIs for job management and terms related to jobs in Apsara Big Data Manager (ABM). ABM allows you to run jobs to perform O&M operations on big data services. Jobs in ABM are run to perform O&M operations on physical devices in a cluster. The Jobs page contains the
**Job Execution** page.

**Terms**

Terms related to jobs include: Ordinary job: A job that can only be manually run. No timer is set. Cron job: A job that is automatically run based on timer settings.

**Job Execution page**

The **Job Execution** page contains the following tabs: You can view and run ordinary jobs, and view their execution history. You can search for a specific ordinary job. Cron Jobs You can enable, disable, view, or run cron jobs, and view their execution history. You can search for a specific cron job. Execution History You can view the execution history of ordinary and cron jobs. You can specify multiple filter conditions to search for a specific job and view the execution history of the specific job.

#### 5.2.2 Jobs

##### 5.2.2.1 Enable or disable a cron job

When a cron job is generated from a scheme, the job is disabled by default. You must manually enable it. If you do not need the cron job to run during a specified time period, you can manually disable it.

**Prerequisites**

You must have an ABM administrator account.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. On the **Job Execution** page, click **Cron Jobs**.
4. On the **Cron Jobs** page, you can enable or disable a cron job.
To enable a cron job in the inactive status, click **Enable** in the Actions column of the cron job. After a cron job is enabled, its **status** changes to **Active**. The **Enable** button is replaced by **Disable**. To disable a cron job in the active status, click **Disable** in the Actions column of the cron job. After a cron job is disabled, its **status** changes to **Inactive**. The **Disable** button is replaced by **Enable**.

##### 5.2.2.2 Manually run a job

After you have created an ordinary job, you must manually run the job in order to perform O&M operations on the product. You can also manually run a cron job.

**Prerequisites**

You must have an ABM administrator account.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. Click **Ordinary Jobs** on the **Job Execution** page.
If you need to manually run a cron job, click **Cron Jobs**. The procedure to manually run a cron job is the same as that of an ordinary job. This topic takes ordinary jobs as an example.
4. In the **Ordinary Jobs** list, click **Run** in the Actions column of a job.
5. Confirm the job risks in the dialog box that appears, and click **Confirm**.
After you have confirmed, a record is automatically generated on the **Execution History** page. For more information, see View execution history.
6. On the job execution page, click **Start** at the top to start the execution.
You can find the record about a job on the **Execution History** page, and click **View** to go to the detailed execution page.

##### 5.2.2.3 View the execution history of a job

Apsara Big Data Manager (ABM) allows you to view the execution history of a specific job to learn the execution status of it.

**Prerequisites**

An ABM administrator account is obtained.

**Background information**

After you confirm to run a job, ABM generates logs for the job execution. You can learn the execution status by using the log data. The **Execution History** page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the **Pending** state or retry the execution of a job that is in the
**Exception** state.
This topic describes how to view the execution history of an ordinary job. You can follow a similar procedure to view the execution history of a cron job.

**Procedure**

1. Log on to the ABM console.
2. Click **Management** in the upper-right corner. On the page that appears, click **Jobs** in the
left-side navigation pane.
3. Click the **Ordinary Jobs** tab on the **Job Execution** page.
4. On the **Ordinary Jobs** page, click **History** in the Actions column of an ordinary job. The
**Execution History** page appears.
You can view the execution history of this job on the **Execution History** page. For more information, see View execution history.

#### 5.2.3 View execution history

Apsara Big Data Manager (ABM) allows you to view the execution history of jobs and schemes to learn about their execution details.

**Prerequisites**

An ABM administrator account is obtained.

**Background information**

After you have confirmed the execution of a job, a record is automatically generated on the Execution History page. The **Execution History** page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the **Pending** state or retry the execution of a job that is in the
**Exception** state.

**Procedure**

1. Log on to the ABM console.
2. In the upper-right corner of the ABM console, click **Management**. In the left-side
navigation pane of the page that appears, click **Jobs**.
3. On the **Job Execution** page, click the **Execution History** tab.
4. If a large number of execution records exist, filter them by a combination of one or more of
the following filter conditions: **job name**, **creator**, **execution status**, and time range. Then, click to search for the desired records.
5. Click **View** in the Actions column of a record to view the execution details.
The following table lists the operations that you can perform on records in different states.

| Execution status | Feature | Procedure |
|---|---|---|

| All states | View the parameter configuration | Click Parameter Configuration in the upper-right corner of the job details page, and select Context Parameters or Global Parameters to view the context parameters or global parameters of the job. |
|---|---|---|
|   | Download execution details | Click Download Execution Details in the upper-right corner of the job details page to download the job execution details to your on-premises machine. Save the job into a TXT file. The execution details record the JSON and raw data of job execution. |
|   | View the execution details of steps | On the Servers page of a step, click View Details in the Actions column of a server. The execution details of the step on the server, including the execution output, appear in the Execution Details section. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|   | Refresh the page | If the job is in the running state, you can clickR efresh in the upper-right corner of the job details page to view the latest execution status. |
| Pending | Start the job | Click Start in the upper-right corner of the job details page to start the job. |
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |
| Unconfirmed | Complete the manual operation | At the manual step that you want to perform, follow the instructions and click OK to go to the next step. |
|   | Roll back to the complete status of the previous step | At the manual step that you want to perform, click Rollback to roll back to the complete status of the previous step. |
|   | Cancel the job | Click Cancel to cancel the job. |
|   | Retry the step that has exceptions | In the step that has exceptions, click Retry to execute the step again. |
|   | Skip the step that has exceptions | In the step that has exceptions, click Skip to skip this step and execute the subsequent steps. |
|   | Roll back to the complete status of the previous step | In the step that has exceptions, click Rollback to roll back to the complete status of the previous step. |

| Exception |   |   |
|---|---|---|
|   | Reset the step that has exceptions to the Pending state | In the step that has exceptions, click Reset to reset the step to the Pending state. When the step that has exceptions is reset to the Pending state, the execution status becomes Paused. You can click Continue in the upper-right corner of the job details page to execute the step again. |
|   | View the execution details of steps that has exceptions | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you view the details of the server that has exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to execute the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
| Failure | Retry the failed step | In the failed step, click Retry to execute the step again. |
|   | Skip the failed step | In the failed step, click Skip to skip this step and execute the subsequent steps. |
|   | Roll back to the complete status of the previous step | In the failed step, click Rollback to roll back to the complete status of the previous step. |
|   | Reset the failed step to the Pending state | In the failed step, click Reset to reset the step to the Pending state. When the failed step is reset to the Pending state, the execution status becomes Paused. You can click Continue in the upper-right corner of the job details page to execute the step again. |

|   | View the execution details of failed steps | On the Servers page of a step, click View Details in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you view the details of the server that has exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Retry to execute the step again on the server. If the step contains a script, the Script Content and Execution Parameters pages will appear. You can view the script content and the script execution parameters. If the step contains a command, the Commands and Execution Parameters pages will appear. You can view the command content and the command execution parameters. |
|---|---|---|
|   | Cancel the job | Click Cancel in the upper-right corner of the job details page to cancel the job. |

### 5.3 Health management

Apsara Big Data Manager (ABM) provides a wide variety of built-in checkers for each big data service. These checkers are used to check service faults and send alerts. This helps you detect and fix faults in a timely manner.

**Prerequisites**

Your ABM account is granted the required permissions on services on which you want to perform O&M. The alert sources and checkers of the monitoring items are obtained.

**Background information**

Different services have different scheduling and monitoring items, but the configuration and operations that can be performed on services are the same. This topic describes the scheduling and monitoring items of MaxCompute. Scheduling: Checkers run scheduling scripts on the servers of specific TianJi roles and generate raw alert data. Raw alert data provides information about the checker, server, alert severity, and alert content. Raw alert data is stored in the ABM database. Monitoring: You can mount checkers to service pages in ABM. You can configure filter policies to display alerts about high priority checkers. Both the scheduling items and monitoring items are built-in and you cannot add more scheduling and monitoring items. However, you can modify some parameters of the items, such as whether to enable an item, running parameters, and description. In addition, you can configure mount points of the monitoring items or delete monitoring items.

**View details and mount points of scheduling items**

The mount points of scheduling items are built-in and you cannot add, modify, or delete mount points. The mount points of the scheduling items correspond to the list of all hosts corresponding to the Apsara Infrastructure Management role that runs the scheduling script.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears. The **Scheduling** tab displays all scheduling items of the current product.
4. On the **Scheduling** tab, find the desired scheduling item and click **View** in the Actions
column to view the details of the scheduling item.
5. Click the plus sign to expand a scheduling item. Then, view the mount points of the
scheduling item.

**Modify a scheduling item**

You can configure the scheduling interval and running parameters of a scheduling item, and configure whether to enable the scheduling item.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears.
4. On the **Scheduling** tab, find the desired scheduling item and click **Edit** in the Actions
column. In the Modify Checker dialog box, configure relevant parameters.
**Type**: The value **System Default** indicates that parameters, such as **Execution Interval**
and **Parameters**, use the default settings. The value **Custom** indicates that the parameters can be customized.

> **Note:** Configure the **Execution Interval** parameter based on the **crontab** command.

5. Click **OK**. The scheduling item is modified.

**View faulty hosts**

You can view all the faulty hosts in the current cluster.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**. The **Scheduling** tab appears.
4. In the upper-right corner of the Scheduling tab, click **Faulty Servers** to view the faulty
hosts in the cluster. The list of the faulty hosts shows all faulty hosts in the current cluster and the role of each host in the Apsara Infrastructure Management.

**Modify a monitoring item**

You can modify the name and description of a monitoring item and determine whether to enable the monitoring item. The alert sources and checkers of monitoring items are built-in. We recommend that you do not modify them.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears. The **Monitoring** tab displays all monitoring items of the current service.
5. On the **Monitoring** tab, find the desired monitoring item and click **Modify** in the Actions
column to modify the configuration of the monitoring item.
6. Click **OK**. The scheduling item is modified.

**Add a mount point for a monitoring item**

After a mount point is added for a monitoring item, the monitoring item mounts the raw alert data to the O&M page of each service in the ABM console.
1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. On the **Monitoring** tab, click the plus sign to expand a monitoring item. Then, view the
mount points of the monitoring item.
6. Click **Add Mount Point** under the mount point list. In the Add Amount Point dialog box,
configure relevant parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Mount Point | The mount point to which the required inspection result of this monitoring item that you want to mount. For example, the value odps/host indicates that the result is mounted to the host O&M page of MaxCompute. |
| Filter Policy | Valid values: None: All alerts generated by the monitoring item is displayed. Custom: The alerts generated by the monitoring item in accordance with the filter configured for the service tree node are displayed. Node Name: The alerts whose node name is the same as the name of the current node are displayed. |
| Enabled | Specifies whether the mount point takes effect. |

7. Click **OK**. The scheduling item is modified.

**Delete a mount point from a monitoring item**

1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. On the **Monitoring** tab, click the plus sign to expand a monitoring item. Then, view the
mount points of the monitoring item.
6. Find the desired mount point and click **Delete** in the Mount Point column. In the message
that appears, click **OK**. The mount point is deleted.

**Delete a monitoring item**

1. Log on to the ABM console.
2. In the upper-left corner of the ABM console, click the
icon and select **MaxCompute**.
3. In the upper-right corner of the MaxCompute page, click **Management**. In the left-side
navigation pane of the **Management** page, click **Health Checks**.
4. On the **Health Management** page, click the **Monitoring** tab. The **Monitoring** tab
appears.
5. Find the desired monitoring item and click **Delete** in the Actions column. In the message
that appears, click **OK**. The monitoring item is deleted.

### 5.4 Operation auditing

This feature allows you to view the O&M operations of the current service of Apsara Big Data Manager (ABM). The details of each operation are provided for retrieval and fault locating.

**Prerequisites**

Your ABM account is granted the required permissions to perform O&M operations on the corresponding service.

**Background**

You can view operation logs by service. For example, to view the operation logs of MaxCompute, you must go to the MaxCompute page first. The following describes how to view the operation logs of MaxCompute.

> **Note:** This page displays only the O&M operations of a service. Note that the O&M operations of job services are not included.

**Procedure**

1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click **MaxCompute**.
3. Click **Management** in the upper-right corner of the MaxCompute page, and then click
**Operation Audit** in the left-side navigation pane of the **Management** page.
The **Operation Audit** page displays the O&M operations of the current service. In this example, the information about MaxCompute O&M operations is displayed, including the operation name, operation ID, status, submission time, start time, end time, operator, and implementation method.
4. Click **Details** for an operation to view the O&M operation details.
You can also view the causes of failed steps in detail.
5. If an O&M operation fails, view the cause of the failure.
6. When the task is in the Failure, Not Started, Pending, or Exception state, perform the
operations listed in the following table based on your situation.

| State | Executable operation |
|---|---|
| Not Started | Click Start to start the task. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Pending | Follow the instructions and click OK to go to the next step. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |

| Exception | Click Retry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |
|---|---|
| Failure | Click Retry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Parameter Configuration to view the parameter configuration of the task. Click Cancel to cancel the task. |

7. To download the O&M operation execution logs, click **Download Execution Details** at the
top to save the logs to your local device.

## 6 Go to other consoles

Apsara Big Data Manager (ABM) provides links to the Apsara Uni-manager Operations Console (ASO), Apsara Infrastructure Management Framework console, and Apsara Stack Security Center console to facilitate the operations and maintenance (O&M) of big data services. Apsara Big Data Manager (ABM) provides links to the Apsara Uni-manager Operations Console (ASO) and Apsara Infrastructure Management Framework console to facilitate the operations and maintenance (O&M) of big data services.

**Prerequisites**

An ABM account that works properly and its password are obtained.

**Procedure**

1. Log on to the ABM console.
2. On the homepage of ABM, click the
icon in the upper-left corner. In the **Site Navigation** section, click **ASO**, **TIANJI**, or **YUNDUN** to go to the console that you want to access.
3. On the homepage of ABM, click the
icon in the upper-left corner. In the **Site Navigation** section, click **ASO** or **TIANJI** to go to the console that you want to access.

**Result**

After you click **ASO** or **TIANJI**, you can log on to the Apsara Uni-manager Operations Console or the Apsara Infrastructure Management Framework console without the need to enter your username and password. After you click **YUNDUN**, you must enter the username and password to log on to the Apsara Stack Security Center console.
