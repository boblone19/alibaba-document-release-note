---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Big Data Manager User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 89
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Big Data Manager User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%A4%A7%E6%95%B0%E6%8D%AE/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Apsara%20Big%20Data%20Manager%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Big Data Manager User Guide 20220928

## Table of Contents

- 1 What is Apsara Big Data Manager?
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
  - 4.3 ABM O&M overview
  - 4.4 Service O&M
    - 4.4.1 Service overview
    - 4.4.2 Service hosts
  - 4.5 Cluster O&M
    - 4.5.1 Cluster overview
    - 4.5.2 Cluster health
    - 4.5.3 Restore environment settings
  - 4.6 Host O&M
    - 4.6.1 Host overview
    - 4.6.2 Host health
- 5 Management
  - 5.1 Overview
  - 5.2 Jobs
    - 5.2.1 Overview
    - 5.2.2 Jobs
      - 5.2.2.1 Run a job from a scheme
      - 5.2.2.2 Create a job from a scheme
      - 5.2.2.3 Enable or disable a cron job
      - 5.2.2.4 Manually run a job
      - 5.2.2.5 View jobs
      - 5.2.2.6 View the execution history of a job
    - 5.2.3 Schemes
      - 5.2.3.1 Create a scheme from a job
      - 5.2.3.2 View schemes
      - 5.2.3.3 View the execution history of a scheme
    - 5.2.4 View the execution history
  - 5.3 Account management
    - 5.3.1 Terms
    - 5.3.2 Log on to the Apsara Uni-manager Operations Console
    - 5.3.3 Add a role
    - 5.3.4 Add an Apsara Stack account
    - 5.3.5 Modify a role assigned to an account
    - 5.3.6 Grant permissions to an Apsara Stack account
  - 5.4 Patch management
  - 5.5 Hot upgrade
  - 5.6 Health management
  - 5.7 Operation auditing
- 6 Go to other consoles

Manager?

## 1 What is Apsara Big Data Manager?

Manager? Apsara Big Data Manager (ABM) is an operations and maintenance (O&M) platform tailored for big data services. ABM supports the following services: MaxCompute DataWorks RealtimeCompute Quick BI DataHub Machine Learning Platform for AI ABM supports O&M on big data services from the perspectives of business, services, clusters, and hosts. ABM also allows you to update big data services, customize alert configurations, and view the O&M history. Onsite Apsara Stack engineers can use ABM to easily manage big data services. For example, they can view metrics, check and handle alerts, and modify configurations.

## 2 Common operations

The data tables and legends in the ABM console facilitate operations. This topic uses MaxCompute and DataHub as examples to describe the common operations. Search for a project You can perform a quick search for a project by project name.
1. On the MaxComput e page, click O&M in the upper-right corner, and then click the Business tab.
The Project List page under Project s appears.
2. In the Project field, enter a keyword of the project name. Auto-suggestion is supported. Select
the target project from the drop-down list, or select the project by using the up and down arrow keys, and then press Ent er. Not e When a project is matched, the region of the project appears before the project name. The following figure shows the search result. Filter projects You can set filter conditions for multiple columns at the same time to filter projects and find the target projects.
1. On the MaxComput e page, click O&M in the upper-right corner, and then click the Business tab.
The Project List page under Project s appears.
2. On the Project List page, click Filt er in the upper-left corner of the list. A field for setting filter
conditions appears for each column.
3. Click the icon next to each field for setting filter conditions and select the filtering method. The
default method is Cont ains. You can select one of the following filtering methods: Equals Not equal St art s wit h Ends wit h Cont ains Not cont ains
4. After you select the filtering method, enter the filter condition. The projects that meet the filter
condition appear.
5. If the filtering result is not accurate, you can continue performing this operation on other columns.
After you set the filter conditions for the projects, the Filt er button is highlighted. If you need to cancel filtering, click the highlighted Filt er button. Search for an item You can search for an item in a table by column, which is similar to filtering projects. For example, you can perform the following steps to search for a checker:
1. On the MaxComput e page, click O&M in the upper-right corner, and then click the Clust ers tab.
On the Clusters page, click the Healt h St at us tab.
2. In the checker list, click the Filt er icon in a column and enter a keyword in the search box.
3. Click Search. The checkers that meet the requirements appear.
4. If the search result is not accurate, you can continue performing this operation on other columns.
Customize a column You can customize columns in the list. For example, you can set the column position or column width, and determine whether to display a column. You can also set filter conditions for columns. On the Project List page, you can drag a column to change its position. You can click in a column heading to customize the column. Pin Column: allows you to fix a column to the rightmost or leftmost of the list. Unless being pinned, a column appears at the default position. Aut osize T his Column: allows you to adjust the width of a column automatically. Aut osize All Columns: allows you to adjust the width of all columns automatically. Reset Columns: allows you to reset a column to its initial status. T ool Panel: Click in a column heading and set a filter condition to filter projects based on the column. Click in a column heading and select the columns to display. If you select the check box of a column name, the column appears. Otherwise, the column is hidden. Show the tool panel After the tool panel appears, it is attached to the right of the list so that you can set the columns to display. On the Project List page, click in a column heading and select T ool Panel. The tool panel is then attached to the right of the list. Sort projects based on a column You can sort projects based on a column in ascending or descending order. On the Project List page, click a column heading in the list. When you click the column heading for the first time, the projects are sorted based on the column in ascending order. When you click the column heading for the second time, the projects are sorted in descending order. When you click the column heading for the third time, the default sorting is restored. Sort items based on a column You can sort items based on a column in ascending or descending order. The procedure and display method are different from those described in Sort projects based on a column.
1. On the MaxComput e page, click O&M in the upper-right corner, and then click the Clust ers tab.
On the Clusters page, click the Healt h St at us tab.
2. In the checker list, click a column heading or the Sort icon in the column heading to sort checkers in
ascending order or descending order. The highlighted up arrow indicates that the checkers are sorted in ascending order. The highlighted down arrow indicates that the checkers are sorted in descending order. View the trend charts for a MaxCompute cluster On the MaxComput e page, click O&M in the upper-right corner, and then click the Clust ers tab. On the Clusters page, you can view relevant metrics, such as CPU and memory usage, of the selected cluster. Take CPU usage as an example. The trend chart displays the trend lines of the total CPU usage (cpu), CPU usage for executing code in kernel space (sys), and CPU usage for executing code in user space (user) for the specified cluster over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the CPU usage of the cluster in the specified period. View the trend charts for a DataHub cluster
1. On the Dat aHub page, click O&M in the upper-right corner, and then click the Services tab. In the
left-side navigation pane of the Services tab, click Manage Service.
2. On the Overview page, you can view the trend charts of resource usage for the specified cluster.
The trend charts, such as the trend charts of the read/write latency and the number of read/write records, appear in the Trend for Resource Usage section. Each chart displays the trend lines of the metrics over time in different colors. You can customize the metrics to display. You can click the name of a metric under the chart to determine whether to display the corresponding trend line in the chart. A highlighted metric name indicates that the corresponding trend line is visible, whereas a dimmed metric name indicates that the corresponding trend line is hidden.

## 3 Quick start

### 3.1 Log on to the ABM console

This topic describes how to log on to the Apsara Big Data Manager (ABM) console. Prerequisites The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome. Procedure
1. Open your Chrome browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the
Enter key. Not e You can select a language from the drop-down list in the upper-right corner of the page.
3. Enter your username and password.
Not e Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. For security reasons, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains the following special characters: ! @ # $ % The password must be 10 to 20 characters in length.
4. Click Log On.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, click O&M.
6. In the left-side navigation pane, choose Product Management > Product s.
7. In the Big Dat a Services section, choose General-Purpose O&M > Apsara Big Dat a Manager.

### 3.2 Set the theme of the console

You can set the theme of the Apsara Big Data Manager (ABM) console to dark or bright based on your preferences. By default, the dark theme is used. Prerequisites An ABM account and the corresponding password are obtained. Procedure
1. Log on to the ABM console.
2. Set the theme of the ABM console to dark or bright based on your preferences.

| Theme | Description |
|---|---|
| Bright | If the dark theme is used, you can move the pointer over the username in the upper-right corner and turn off the switch to change to the bright theme. |
| Dark | If the bright theme is used, you can move the pointer over the username in the upper-right corner and turn on the switch to change to the dark theme. |

### 3.3 View the trace dashboards

The dashboard is used to display the key running metrics of MaxCompute, DataWorks, RealtimeCompute, and DataHub products, as well as alarms of all big data products. This allows you to understand the running status of big data products as a whole. Prerequisites Your ABM account is granted the required permissions on services on which you want to perform O&M. Background information The dashboard is a feature of the ABM console. As the homepage of the ABM console, the dashboard allows you to view the overall running information about all big data services. Procedure
1. Log on to the ABM console.
After logging in to the Apsara Big Data Manager, the default display Dashboard page. If you are currently on another page, you can click the icon and select ABM products to enter Dashboard page.
2. View and clear service alerts.
In the alert list, view the number of alerts for all big data products. Crit ical and Warning type alarms must be fixed in a timely manner. i. In the Dashboard On t he page, click the Crit ical or Warning quantity, into the product Clust er O&M > Healt h page. In the Healt h On the page that appears, you can view all check items of the product. ii. Click the Det ails to view the details of the check item and the alert solution of the check item, and press Solut ion T he st eps in to handle alerts. iii. Log on to the hosts on which the alerts are detected to handle the alerts. Click in front of the check item that has an alarm. Fold icon, and then click the Logon icon. iv. In the newly opened T erminalService On the page that appears, select a host on the left to log on.
3. In the Dashboard On the page that appears, click the MaxComput e , view MaxComput e .
MaxComput e T he section displays the job running overview, control system saturation, data import traffic, computing resource usage, storage resource usage, and the logical and physical CPU usage trend charts of the MaxCompute cluster.
4. In the Dashboard On the page that appears, click the Dat aWorks , view Dat aWorks .
Dat aWorks T he section displays the node scheduling overview, slot resource overview, and the cumulative trend chart of task completion in the DataWorks cluster.
5. In the Dashboard On the page that appears, click the Realt imeComput e , view
Realt imeComput e . Realt imeComput e T he section displays the trend charts of TPS and FAILOVER for RealtimeCompute cluster jobs, and the trend charts of CPU and memory usage.
6. In the Dashboard On the page that appears, click the Dat aHub , view Dat aHub .
Dat aHub section displays the trend charts of read /write latency, number of read /write records, read /write QPS, read /write byte traffic, CPU level, and memory level of the DataHub cluster.

### 3.4 View the cluster running status

Apsara Big Data Manager (ABM) provides you with several operation metrics of clusters, such as CPU usage, memory usage, load, storage, and health check result. This helps you understand the running status of clusters at any time. Based on relevant metrics, you can evaluate whether the selected cluster has operation risks. Prerequisites Your ABM account is granted the required permissions to perform O&M operations on the corresponding service. Context In the ABM console, the procedures of viewing the cluster running status for different services are the same. This topic uses one of the services as an example. Procedure
1. Log on to the ABM console.
2. Click
in the upper-left corner and then click a service.
3. On the page that appears, click O&M in the upper-right corner, and then click the Clust ers tab.
4. On the Clust ers page, select a cluster in the left-side navigation pane. The Overview page for the
cluster appears. On the Overview page, you can view the host status, service status, health check result, and health check history of the selected cluster. You can also view the trend charts of CPU usage, disk usage, memory usage, load, and packet transmission for the cluster. What's next You can evaluate the operation risks of a cluster based on the metrics such as the service status, CPU usage, disk usage, memory usage, and load. If the cluster has any Critical, Warning, or Exception alerts, you need to check and clear them in a timely manner. You need to pay special attention to the Critical and Warning alerts. For more information, see View and clear cluster alerts.

### 3.5 View and clear cluster alerts

If you find alerts on the cluster overview page, go to the cluster health status page to view and clear the alerts. This topic uses one Apsara Big Data Manager (ABM) service as an example to describe how to view and clear alerts. Prerequisites Your ABM account is granted the required permissions to perform O&M operations on the corresponding service. Context In the ABM console, the procedures of viewing and clearing alerts for different services are the same. If a service has alerts, especially the Critical and Warning alerts, pay attention to them and clear them in a timely manner to make sure that the cluster can run properly. Procedure
1. Log on to the ABM console.
2. Click
in the upper-left corner and then click a service.
3. On the Clust ers page, select a cluster in the left-side navigation pane, and then click the Healt h
St at us tab. The Health Status page for the cluster appears.
4. On the Healt h St at us page, click + to expand a checker with alerts. You can view all hosts where
the checker is run.
5. Click a hostname. In the dialog box that appears, click Det ails in the Actions column of a check
result to view the alert causes.
6. On the Healt h St at us page, click Det ails in the Actions column of the checker to view the
schemes to clear the alerts.
7. Clear the alerts according to the schemes.
To log on to a host with alerts for related operations, click the Log On icon next to the name of the host. On the T erminalService page that appears, click the hostname on the left to log on to the host.
8. After you clear an alert for a host, click Ref resh in the Actions column of the host to run the
checker again for the host. In this way, you can check whether the alert is cleared.

## 4 ABM

### 4.1 ABM dashboard

The Apsara Bigdata Manager (ABM) dashboard shows the key indicators of MaxCompute, DataWorks, Realtime Compute for Apache Flink, and DataHub. The dashboard also provides information about the alerts for all big data services and helps you understand the overall status of these services. The dashboard supports auto-refresh and full-screen display. Go to the Dashboard tab After you log on to the ABM console, the Dashboard tab appears by default. To return to the Dashboard tab, click the icon in the upper-left corner and click ABM. In the upper-left corner of the Dashboard tab, you can select a region from the drop-down list to view the cluster status of each big data service in the region. View and handle the alerts of various services In the Overview section, you can view the numbers of Crit ical, Warning, and Except ion alerts that are reported for each big data service. If a service has alerts, especially Crit ical or Warning alerts, handle these alerts on time.
1. On the Dashboard tab, find the check item of a service that you want to query, and click the
number in the Crit ical or Warning column of the service. The Healt h St at us page for the service appears on the Clust ers tab. On the Healt h St at us page, you can view all the check items of the service.
2. Click Det ails in the Actions column of a check item for which alerts are reported. In the Details
dialog box, view the details of the check item and the descriptions to handle the alerts. Perform the steps provided in the Descript ion section to handle the alerts.
3. Log on to the hosts on which the alerts are detected to handle the alerts.
Click the plus sign (+) to expand a check item with alerts, and click the Log On icon next to the name of a host with alerts. On the TerminalService page that appears, click the hostname on the left to log on to the host. View key indicators of MaxCompute The ABM dashboard shows the key indicators of MaxCompute. On the Dashboard tab, click MaxComput e to view the information. In the MaxComput e section, you can view the job status, the real-time capacity for the control system, computing resource usage, and storage resource usage. You can also view the trend charts of imported data traffic, logical CPU utilization, and physical CPU utilization. View key indicators of DataWorks The ABM dashboard shows key indicators of DataWorks. On the Dashboard tab, click Dat aWorks in the Monit oring column to view the information. In the Dat aWorks section, you can view the node scheduling and slot usage of a DataWorks cluster. You can also view the trend chart of the total number of daily finished tasks. View key indicators of Realtime Compute for Apache Flink The ABM dashboard shows key indicators of Realtime Compute for Apache Flink. On the Dashboard tab, click Realt ime Comput e in the Monit oring column to view the information. In the Realt ime Comput e section, you can view the trend charts of the transactions per second (TPS), failover rate, CPU utilization, and memory usage for a Realtime Compute for Apache Flink cluster. View key indicators of DataHub The ABM dashboard shows key indicators of DataHub. On the Dashboard tab, click Dat aHub in the Monit oring column to view the information. In the Dat aHub section, you can view the trend charts of the read/write latency, read/write records, read/write queries per second (QPS), and read/write throughput. You can also view the trend charts of CPU utilization and memory usage of a DataHub cluster. Enable and disable auto-refresh By default, auto-refresh is disabled on the Dashboard tab, and the statistics of cluster metrics from the last two days are displayed on this page. You can specify a time range to view the metric statistics. If you enable auto-refresh, the system automatically updates the metric data of clusters based on the specified interval.
1. At the top of the Dashboard tab, click the
icon.
2. In the dialog box that appears, configure the Ref reshing every and Ref reshing range
parameters. The Ref reshing range parameter specifies a time period for the trend charts, such as those for the CPU utilization and memory usage of each cluster.
3. After you configure these parameters, click OK to enable auto-refresh.
If auto-refresh is enabled, the icon is replaced with the icon. The system automatically updates all data on the dashboard based on the specified time interval. If you want to disable auto-refresh, click the icon. Display the dashboard in full-screen The dashboard supports full-screen display. This feature allows you to view the status of big data services. At the top of the Dashboard tab, click the icon to display the Dashboard tab in full-screen mode.

### 4.2 ABM repository

The Repository page in the Apsara Big Data Manager (ABM) console displays the resource usage in MaxCompute, DataWorks, and DataHub. This topic describes the features of the ABM repository and how to access the Repository page. Entry
1. Log on to the ABM console.
Not e By default, the Dashboard page appears. To return to the Dashboard page from any other page, click in the upper-left corner and then click ABM.
2. On the Dashboard page, click the Reposit ory tab. The Reposit ory page appears.
View the resource usage in MaxCompute In the left-side navigation pane of the Reposit ory page, click MaxComput e. On the page that appears, you can view the resource usage in MaxCompute. For MaxCompute, the Repository page displays the trend charts of CU and storage usage, records of CU and storage usage, and proportions of idle CUs and storage. View the resource usage in DataWorks In the left-side navigation pane of the Reposit ory page, click Dat aWorks. On the page that appears, you can view the resource usage in DataWorks. For DataWorks, the Repository page displays the trend chart of slot usage, records of slot usage, and proportion of idle slots. View the resource usage in DataHub In the left-side navigation pane of the Reposit ory page, click Dat aHub. On the page that appears, you can view the resource usage in DataHub. For DataHub, the Repository page displays the trend chart of storage usage, records of storage usage, and proportion of idle storage. Other operations You can filter or sort records of CU, storage, and slot usage based on a column to facilitate information retrieval. For more information, see Common operations.

### 4.3 ABM O&M overview

This topic describes the O&M modules of ABM and how to go to the ABM O&M page. Modules ABM O&M includes the following modules: services, clusters, and hosts. The following table describes these modules.

| Module | Feature | Description |
|---|---|---|
| Services | Overview | Shows the trend charts of CPU utilization, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for each server role in a cluster. |
|   | Server | Shows the host list of each server role in a cluster so that you can understand the deployment of server roles on hosts. |
| Clusters | Overview | Shows the trend charts of CPU utilization, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for a cluster. |
|   | Health Status | Shows all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any exist). You can also log on to a host and perform manual checks on the host. |

| User Guide·ABM | Apsara Big Data Manage |   |
|---|---|---|
| Module | Feature | Description |
| Hosts | Overview | Shows the overall running and health check information about a host. You can view the root disk usage, total usage, 1-minute load, 5-minute load, 15-minute load, health check results, and health check history of the host. You can also view the trend charts of CPU utilization, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for the host. |
|   | Health Status | Shows the checkers of the selected host, including the checker details, health check results, health check history, and schemes to clear alerts (if any exist). You can also log on to a host and perform manual checks on the host. |

Go to the Apsara Big Data Manager O&M page
1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and click ABM.
3. In the upper-right corner of the page that appears, click O&M. The Services tab appears.
The O&M page includes the following modules: Services, Clust ers, and Host s.

### 4.4 Service O&M

#### 4.4.1 Service overview

The Overview page lists all Apsara Big Data Manager (ABM) services in a cluster. You can view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for each service. Entry On the Services page, select a cluster above the left-side service list, select a service in the service list, and then click the Overview tab. The Overview page for the service appears. On the Overview page, you can view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for the selected service. CPU This chart displays the trend lines of the total CPU usage (cpu), CPU usage for executing code in kernel space (sys), and CPU usage for executing code in user space (user) for the selected service over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the CPU usage of the service in the specified period. DISK This chart displays the trend lines of the storage space usage on the /, /boot, /home/admin, and /home directories for the selected service over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the storage space usage of the service in the specified period. LOAD This chart displays the trend lines of the 1-minute, 5-minute, and 15-minute load averages for the selected service over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the 1-minute, 5-minute, and 15-minute load averages of the selected service in the specified period. MEMORY This chart displays the trend lines of the memory usage (mem), total memory size (total), used memory size (used), size of memory used by kernel buffers (buff), size of memory used by the page cache (cach), and available memory size (free) for the selected service over time in different colors. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the memory usage of the selected service in the specified period. PACKAGE This chart displays the trend lines of the number of dropped packets (drop), that of error packets (error), that of received packets (in), and that of sent packets (out) for the selected service over time in different colors. These trend lines reflect the data transmission status of the service. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the data transmission status of the selected service in the specified period. TCP This chart displays the trend lines of the number of failed TCP connection attempts (atmp_fail), that of the times of resetting TCP connections in the ESTABLISHED state (est_reset), that of active TCP connections (active), that of passive TCP connections (pasive), that of received TCP packets (iseg), and that of sent TCP packets (outseg) for the selected service over time in different colors. These trend lines reflect the TCP connection status of the service. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the TCP connection status of the selected service in the specified period. DISK ROOT This chart displays the trend line of the average root disk usage (avg) for the selected service over time. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the average root disk usage of the selected service in the specified period.

#### 4.4.2 Service hosts

Apsara Big Data Manager (ABM) allows you to view the host list of each ABM service so that you can understand the service deployment on hosts. On the Services page, select a cluster above the left-side service list, select a service in the service list, and then click the Server tab. The Server page for the service appears. On the Server page, you can view the hosts where the selected service is run.

### 4.5 Cluster O&M

#### 4.5.1 Cluster overview

The cluster overview page displays the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for a cluster. Entry On the Clust ers page, select a cluster in the left-side navigation pane, and then click the Overview tab. The Overview page for the cluster appears. The cluster overview page displays the trend charts of CPU usage, memory usage, and load for a cluster. The trend charts are described as follows: CPU This chart shows the trend lines of the total CPU utilization (cpu), CPU utilization for executing code in kernel space (sys), and CPU utilization for executing code in user space (user) for the cluster in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the CPU utilization of the cluster in the specified period. MEMORY This chart shows the trend lines of the memory usage (mem), total memory size (total), used memory size (used), size of memory used by buffers (buff), size of memory used by the page cache (cach), and available memory size (free) for the cluster in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the memory usage of the cluster in the specified period. LOAD This chart shows the trend lines of the 1-minute, 5-minute, and 15-minute load averages for the cluster in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the 1-minute, 5-minute, and 15-minute load averages of the cluster in the specified period.

#### 4.5.2 Cluster health

On the cluster health status page, you can view all checkers of a cluster, including the checker details, check results for the hosts in the cluster, and schemes to clear alerts (if any). In addition, you can log on to a host and perform manual checks on the host. Entry On the Clust ers page, select a cluster in the left-side navigation pane, and then click the Healt h St at us tab. The Health Status page for the cluster appears. On the Healt h St at us tab, you can view all checkers for the cluster and the check results for the hosts in the cluster. The following alerts may be reported on a host: CRIT ICAL, WARNING, and EXCEPT ION. The alerts are represented in different colors. You must handle the alerts in a timely manner, especially the CRIT ICAL and WARNING alerts. View checker details
1. On the Health Status tab, click Det ails in the Actions column of a checker. On the Details page,
view checker details. The checker details include Name, Source, Alias, Applicat ion, T ype, Scheduling, Dat a Collect ion, Def ault Execut ion Int erval, and Descript ion. The schemes to clear alerts are provided in the description.
2. Click Show More to view more information about the checker.
You can view information about Script , T arget (T ianJi), Def ault T hreshold, and Mount Point . View the hosts for which alerts are reported and causes for the alerts You can view the check history and check results of a checker on a host.
1. On the Health Status tab, click + to expand a checker for which alerts are reported. You can view all
hosts where the checker is run.
2. Click a hostname. In the panel that appears, click Det ails in the Actions column of a check result to
view the cause of the alert. Clear alerts On the Health Status tab, click Det ails in the Actions column of a checker for which alerts are reported. On the Details page, view the schemes to clear alerts. Log on to a host You may need to log on to a host to handle alerts or other issues that occurred on the host.
1. On the Health Status tab, click + to expand a checker for which alerts are reported.
2. Click the Login in icon of a host. The T erminalService page appears.
3. On the T erminalService page, click the hostname in the left-side navigation pane to log on to the
host. Run a checker again After you clear an alert for a host, click Ref resh in the Actions column of the host to run the checker again for the host. This way, you can check whether the alert is cleared.

#### 4.5.3 Restore environment settings

If a host in the cluster encounters RPMDB errors, Apsara Big Data Manager (ABM) allows you to restore environment settings. Prerequisites bigdata-sre is installed on the machine that you want to manage. If the machine is a Docker container, make sure that the staragent process runs in the container. Restore environment settings
1. Log on to the ABM console.
2. In the upper-left corner, click the
icon and then click ABM.
3. In the top navigation bar of the ABM page, click O&M. Then, click the Clust ers tab.
4. In the left-side navigation pane of the Clust ers tab, select a cluster. Then, click the Healt h
St at us tab. The Healt h St at us tab appears.
5. In the upper-right corner of the tab, click Act ions and select Rest ore Environment Set t ings. In
the Rest ore Environment Set t ings pane, enter a hostname. If you enter multiple hostnames, separate them with commas (,).
6. Click Run.
7. Check the execution status.
Click Act ions and select Execut ion Hist ory next to Rest ore Environment Set t ings to view the execution history. It requires a long time to restore environment settings. RUNNING indicates that the execution is in progress. SUCCESS indicates that the execution succeeded. FAILED indicates that the execution failed.
8. If the status is RUNNING, click Det ails in the Details column to view the steps and progress of
restoration.
9. If the status is FAILED, click Det ails in the Details column to identify the cause of the failure. For
more information, see Identify the cause of the failure to restore environment settings. Identify the cause of the failure to restore environment settings This section describes how to identify the cause of the failure to restore environment settings.
1. In the upper-right corner of the Clust ers tab, click Act ions and select Execut ion Hist ory next to
Rest ore Environment Set t ings to view the execution history.
2. Click Det ails in the Details column of a failed record to identify the cause of the failure.
You can also view information about parameter settings, host details, script, and runtime parameters to identify the cause of the failure.

### 4.6 Host O&M

#### 4.6.1 Host overview

The host overview page displays the overall running information about a host in an Apsara Big Data Manager (ABM) cluster. On this page, you can view the root disk usage, total usage, 1-minute load, 5minute load, 15-minute load, health check result, and health check history of the host. You can also view the trend charts of CPU usage, disk usage, memory usage, load, packet transmission, TCP connection, and root disk usage for the host. Entry On the Host s page, select a host in the left-side navigation pane. The Overview page for the host appears. Root Disk Usage, Total, and 1-Minute Load These sections display the root disk usage, total usage, and 1-minute load for the selected host. The Root Disk Usage section provides the usage of the /tmp directory. The Total section provides the system usage and user usage. The 1-Minute Load section provides the 1-minute, 5-minute, and 15minute load averages. CPU The CPU chart shows the trend lines of the total CPU utilization (cpu), CPU utilization for executing code in kernel space (sys), and CPU utilization for executing code in user space (user) of the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the CPU utilization of the host in the specified period. DISK The DISK chart shows the trend lines of the storage usage in the/, /boot, /home/admin, and /home directories for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the storage usage of the host in the specified period. MEMORY The MEMORY chart shows the trend lines of the memory usage (mem), total memory size (total), used memory size (used), size of memory used by kernel buffers (buff), size of memory used by the page cache (cach), and available memory size (free) for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the memory usage of the host in the specified period. LOAD The LOAD chart shows the trend lines of the 1-minute, 5-minute, and 15-minute load averages for the host over time in different colors. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the 1-minute, 5-minute, and 15-minute load averages of the host in the specified period. PACKAGE The PACKAGE chart shows the trend lines of the number of dropped packets (drop), that of error packets (error), that of received packets (in), and that of sent packets (out) for the host over time in different colors. These trend lines reflect the data transmission status of the host. In the upper-right corner of the chart, click the icon to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the data transmission status of the host in the specified period. TCP This chart displays the trend lines of the number of failed TCP connection attempts (atmp_fail), that of the times of resetting TCP connections in the ESTABLISHED state (est_reset), that of active TCP connections (active), that of passive TCP connections (pasive), that of received TCP packets (iseg), and that of sent TCP packets (outseg) for the host over time in different colors. These trend lines reflect the TCP connection status of the host. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the TCP connection status of the host in the specified period. DISK ROOT This chart displays the trend line of the average usage of the root disk (/) for the host over time. Click in the upper-right corner of the chart to zoom in the chart. You can specify the start time and end time in the upper-left corner of the enlarged chart to view the average root disk usage of the host in the specified period. Health Check This section displays the number of checkers deployed for the host and the respective number of Critical, Warning, and Exception alerts. Click View Det ails to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health. Health Check History This section displays a record of the health checks performed on the host. Click View Det ails to go to the Health Status page. On this page, you can view the health check details. For more information, see Host health. You can click the event content of a check to view the exception items.

#### 4.6.2 Host health

On the host health status page, you can view the checkers of the selected host, including the checker details, check results, and schemes to clear alerts (if any). In addition, you can log on to the host. Entry At the top of the O&M page, click the Host s tab. On the page that appears, select a host in the leftside navigation pane, and then click the Healt h St at us tab. The Healt h St at us page for the host appears. On the Healt h St at us page, you can view all checkers and the check results for the host. The check results are divided into Crit ical, Warning, and Except ion. They are displayed in different colors. Pay attention to the check results, especially the Crit ical and Warning results, and handle them in a timely manner. View checker details
1. On the Health Status page, click Det ails in the Actions column of a checker. In the dialog box that
appears, view the checker details. The checker details include the name, source, alias, application, type, default execution interval, and description of the checker, whether scheduling is enabled, and whether data collection is enabled. The schemes to clear alerts are provided in the description.
2. Click Show More at the bottom to view more information about the checker.
You can view information about the execution script, execution target, default threshold, and mount point for data collection. View alert causes You can view the check history and check results of a checker.
1. On the Health Status page, click + to expand a checker with alerts.
2. Click the hostname. In the dialog box that appears, click Det ails in the Actions column of a check
result to view the alert causes. Clear alerts On the Health Status page, click Det ails in the Actions column of a checker with alerts. In the dialog box that appears, view the schemes to clear alerts. Log on to a host To log on to a host to clear alerts or perform other operations, follow these steps:
1. On the Health Status page, click + to expand a checker with alerts.
2. Click the Log On icon of a host. The T erminalService page appears.
3. On the T erminalService page, click the hostname on the left to log on to the host.
Run a checker again After you clear an alert for a host, click Ref resh in the Actions column of the host to run the checker again for the host. In this way, you can check whether the alert is cleared.

## 5 Management

### 5.1 Overview

The management module is the configuration and software management center of Apsara Big Data Manager (ABM). It is an important functional module that supports and customizes O&M items for services. The management module supports the following features: Job execution and management: You can generate jobs based on the scheme library to perform O&M operations on services. Patch management: You can deploy upgrade patches for various services. Hot upgrade: You can perform hot upgrades on the monitoring configuration and monitoring items of ABM so that services are not interrupted during the upgrade process. Health management: You can create health checkers and apply them to service hosts. Operation audit: You can view the records of job execution and other service O&M operations in ABM.

### 5.2 Jobs

#### 5.2.1 Overview

This topic describes the Jobs page and concepts related to jobs. Apsara Big Data Manager (ABM) runs jobs to perform O&M operations on big data services. Jobs, also known as service O&M tasks, are O&M operations performed on physical devices in the cluster. The Jobs page consists of the Job Execut ion and Job Management tabs. Concepts Concepts related to jobs include: Ordinary job: a job that can only be manually run. Cron job: a job that is automatically run based on timer settings. Scheme: a job template provided by ABM. You can use schemes to generate jobs. Atom: a step template provided by ABM. You can use atoms as steps when generating jobs. Ordinary step: a step that you need to create when using schemes to generate jobs. Step types include the following: command execution, script execution, file push, API call, and manual step. Atomic step: a step that you can directly use when using schemes to generate jobs. ABM provides common schemes and atoms that support most O&M scenarios. Job Execution page The Job Execut ion page provides the following features: Ordinary Jobs: You can view and run ordinary jobs, and view their execution history. You can search for a specific ordinary job. Cron Jobs: You can enable, disable, view, or run cron jobs, and view their execution history. You can search for a specific cron job. Scheme Library (Top 8): dynamically displays the top 8 most used schemes. Cron Jobs (Top 8): dynamically displays the top 8 most used cron jobs. Execution History: You can view the execution history of ordinary and cron jobs. You can search for the execution record of a specific job by multiple conditions. Job Management page The Job Management page provides the following features: You can generate and run jobs based on schemes and view the execution history of schemes. You can search for a specific scheme. You can view schemes in grid or list mode.

#### 5.2.2 Jobs

##### 5.2.2.1 Run a job from a scheme

When you perform O&M operations, you can directly run jobs from schemes that meet your requirements. This enables you to quickly perform product O&M jobs. Prerequisites You must have an ABM administrator account. Context When you run a job from a scheme, you need to specify the T arget Group and Global Variable parameters. The other parameters cannot be modified. If you want to modify the parameters, see Create a job from a scheme. Running a job from a scheme is a one-time operation and does not generate a job on the Ordinary Jobs tab. You can view the history operations on the Execut ion Hist ory tab. For more information, see View the execution history. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Run a job by using one of the following methods:
In the Scheme Library (T op 8) section, select a scheme. Not e This method only allows you to choose a scheme from the top 8 most frequently used schemes. On the Jobs page, click the Job Management tab, and then click Run in the Actions column of a scheme in the Schemes list.
4. On the Run f rom Scheme page, you need to set T arget Group and Variable Name as needed.
The instructions for setting T arget Group and Variable Name are shown in . Job parameters

| Parameter | Description |
|---|---|
| T arget Group | A collection of target nodes on which the operations are performed. After you have added nodes to target groups, you can select a value for T arget Group based on your needs when you configure the steps. Click next to the target group, and set the nodes to be included in the target group as needed. When you add a node, you can either select the name of the node in Apsara Inf rast ruct ure Management Framework or enter the IP address of the node under Servers. |
| Global Variable | If global variables are set in the scheme, you need to enter the variable value. |

5. After you have configured the preceding parameters, click Run in the upper-right corner.
6. Confirm the job risks in the displayed dialog box, and click Conf irm Execut ion.
After you have confirmed, a record is automatically generated on the Execut ion Hist ory page. For more information, see View the execution history.
7. On the job execution page, click St art at the top to start the execution.
If you do not perform any operation and exit the job execution page, you can find a job record on the Execut ion Hist ory page. Click View to go to the job execution page again.

##### 5.2.2.2 Create a job from a scheme

This topic describes how to generate a job from a scheme. You can generate both ordinary and cron jobs from schemes. Prerequisites An Apsara Big Data Manager (ABM) administrator account is obtained. Context ABM allows you to create both ordinary and cron jobs from schemes. Settings for creating an ordinary job and a cron job are similar, but a schedule must be created for a cron job. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. On the Jobs page, click the Job Management tab, and click Generat e Job in the Actions column
of a scheme in the Schemes list.
4. On the Creat e Job page, set the parameters in the Job Propert ies and St eps sections as needed.
For more information about the parameter configuration of Job Propert ies, see . Job properties

| Parameter | Description |
|---|---|
| Job T ype | The type of the job. Ordinary Job: jobs that must be manually run. Cron Jobs: jobs that automatically run based on a schedule. You can enter a cron expression or click Conf igure Cron Job to create a schedule. Cron expressions are based on cront ab commands. If you are new to cront ab commands, click Conf igure Cron Job to quickly set up a schedule. |
| Job Name | The name of the job. Set the job name based on the functionality of the job to be created so that the user understands what it is and can search for it. |
| T arget Group | A collection of target nodes on which the operations are performed. After you have added nodes to the target groups, you can select the target group based on your needs when you configure the steps. After you have created a group, click to add nodes to the group. When you add a node, you can either select the name of the node in T ianji or enter the IP address of the node under Servers. |

| Parameter | Description |
|---|---|
| Global Variable | Click Add Variable and set the parameters in the dialog box that appears. The Scope parameter is used to set the scope of the variable. If it is set Global, it is valid for the entire job. If you select a certain step, it is only valid for this step. |

5. On the Creat e Job page, add steps as needed.
The steps include ordinary steps and atomic steps. +At omic St ep: a range of built-in steps provided by the system. +Ordinary St ep: Ordinary steps are classified into multiple types. Choose the required type and set the parameters accordingly. , , , , and describe the parameters for different types of ordinary steps. Parameters of command execution steps

| Section | Parameter | Description |
|---|---|---|
| N/A | St ep Name | The name of the step. Enter a step name that reflects the functionality of the step. |
| Basic conf igurat ion | T arget Node Group | The group of nodes on which the step is performed. |
|   | Commands | The commands to be executed in this step. |
|   | User Ident it y | The user who executes this step on the nodes, with a default setting of admin. |
|   | Descript ion | The description of the step. |
|   | Input Cont ext | Enable this option if you need to obtain the output of the previous step. When enabled, this step reads the file specified by the $contextInput variable to obtain the context. |
|   | Out put Cont ext | Enable this option if you need to export the context to the next step. When enabled, this step writes the context to the file specified by the $co ntextOutput variable to export the context. |

|   | User Guide·Managemen |   |
|---|---|---|
|   | Parameter | Description |
| Section |   |   |
| Advanced Conf igurat ion | T imeout Period | The maximum time period allowed to execute the step. If the step is not complete before the time runs out, the execution is stopped and you are notified that the operation is timed out. The default value is 60 seconds. |
|   | Ret ries | The number of times to retry the execution after a failure or timeout error occurs. The default value is 0. |
|   | Ret ry Int erval | The interval between two executions. The default value is 300 seconds. The retry interval is the period of time between the last timeout (or failure) and the next try. |

Parameters of script execution steps

| Section | Parameter | Description |
|---|---|---|
| N/A | St ep Name | The name of the step. Enter a step name that reflects the functionality of the step. |
| Basic conf igurat ion | T arget Node Group | The group of nodes on which the step is performed. |
|   | Script Cont ent | Write the script based on the actual O&M requirements. Currently, Shell and Python are supported. You can write new scripts or upload local scripts to configure the script content. |
|   | User Ident it y | The user who executes this step on the nodes, with a default setting of admin. |
|   | Descript ion | The description of the step. |
|   | Input Cont ext | Enable this option if you need to obtain the output of the previous step. When enabled, this step reads the file specified by the $contextInput variable to obtain the context. |
|   | Out put Cont ext | Enable this option if you need to export the context to the next step. When enabled, this step writes the context to the file specified by the $co ntextOutput variable to export the context. |

|   | Apsara Big Data Manage |   |
|---|---|---|
| Section | Parameter | Description |
| Advanced Conf igurat ion | T imeout Period | The maximum time period allowed to execute the step. If the step is not complete before the time runs out, the execution is stopped and you are notified that the operation is timed out. The default value is 60 seconds. |
|   | Ret ries | The number of times to retry the execution after a failure or timeout error occurs. The default value is 0. |
|   | Ret ry Int erval | The interval between two executions. The default value is 300 seconds. The retry interval is the period of time between the last timeout (or failure) and the next try. |

Parameters of file push steps

| Parameter | Description |
|---|---|
| St ep Name | The name of the step. Enter a step name that reflects the functionality of the step. |
| T arget Node Group | The group of nodes to which the file is pushed. |
| T arget Pat h | The directory to which the file is pushed. |
| File Permission | The permission of the file. |
| File Owner | The owner of the file. |
| File Cont ent | Enter the file content in the code editor or upload a local file. After you enter or upload the content, specify the file name in the code editor. |

Parameters of API call steps

| Parameter | Description |
|---|---|
| St ep Name | The name of the step. Enter a step name that reflects the functionality of the step. |
| T arget URL | The URL of the API. |

| Parameter | Description |
|---|---|
| HT T P Met hod | The type of request that you want to send. GET : Query. POST : Create. PUT : Modify. DELET E: Delete. |
| Cont ent Format | The Content-Type field of the header in the HTTP packet. Select a value from the drop-down list. |
| APP NAME | APP NAME and APP KEY are included in the request to call APIs for authenticating permissions. |
| APP KEY |   |
| BODY | The body of the HTTP request. |
| T imeout Period | The maximum time period allowed to execute the step. If the step is not complete before the time runs out, the execution is stopped and you are notified that the operation is timed out. The default value is 60 seconds. |
| Ret ries | The number of times to retry the execution after a failure or timeout error occurs. The default value is 0. |
| Ret ry Int erval | The interval between two executions. The default value is 300 seconds. The retry interval is the period of time between the last timeout (or failure) and the next try. |

Parameters of manual steps

| Parameter | Description |
|---|---|
| St ep Name | The name of the step. Enter a step name that reflects the functionality of the step. |
| Document Cont ent | The instructions to help relevant engineers complete this step. |

6. To change the order of steps, click Sort in the upper-right corner of the St eps section and drag
the steps to put them into the correct order.
7. After you have set the preceding parameters, click Save in the upper-right corner.
Result If you created an ordinary job, it appears on the Ordinary Jobs tab. If you created a cron job, it appears on the Cron Jobs tab. What's next If you created an ordinary job, you need to run it manually. For more information, see Manually run a job. If you created a cron job, you need to enable it. For more information, see Enable or disable a cron job. You can also manually run a cron job. For more information, see Manually run a job.

##### 5.2.2.3 Enable or disable a cron job

When a cron job is generated from a scheme, the job is disabled by default. You must manually enable it. If you do not need the cron job to run during a specified time period, you can manually disable it. Prerequisites You must have an ABM administrator account. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. On the Job Execut ion page, click Cron Jobs.
4. On the Cron Jobs page, you can enable or disable a cron job.
To enable a cron job in the inactive status, click Enable in the Actions column of the cron job. After a cron job is enabled, its st at us changes to Act ive. The Enable button is replaced by Disable. To disable a cron job in the active status, click Disable in the Actions column of the cron job. After a cron job is disabled, its st at us changes to Inact ive. The Disable button is replaced by Enable.

##### 5.2.2.4 Manually run a job

After you have created an ordinary job, you must manually run the job in order to perform O&M operations on the product. You can also manually run a cron job. Prerequisites You must have an ABM administrator account. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Click Ordinary Jobs on the Job Execut ion page.
If you need to manually run a cron job, click Cron Jobs. The procedure to manually run a cron job is the same as that of an ordinary job. This topic takes ordinary jobs as an example.
4. In the Ordinary Jobs list, click Run in the Actions column of a job.
5. Confirm the job risks in the dialog box that appears, and click Conf irm.
After you have confirmed, a record is automatically generated on the Execut ion Hist ory page. For more information, see View the execution history.
6. On the job execution page, click St art at the top to start the execution.
You can find the record about a job on the Execut ion Hist ory page, and click View to go to the detailed execution page.

##### 5.2.2.5 View jobs

After you have created an ordinary job or a cron job, you can view job details, save the job as a scheme, and run the job in the jobs list. Prerequisites You must have an ABM administrator account. Context The topic describes how to view ordinary jobs. You can follow the same procedure to view cron jobs. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Click Ordinary Jobs on the Job Execut ion page.
4. Click View in the Actions column of an ordinary job to view its job details.

##### 5.2.2.6 View the execution history of a job

Apsara Big Data Manager (ABM) allows you to view the execution history of a specific job to learn the execution status of it. Prerequisites An ABM administrator account is obtained. Context After you confirm to run a job, ABM generates logs for the job execution. You can learn the execution status by using the log data. The Execut ion Hist ory page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the Pending state or retry the execution of a job that is in the Except ion state. This topic describes how to view the execution history of an ordinary job. You can follow a similar procedure to view the execution history of a cron job. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Click the Ordinary Jobs tab on the Job Execut ion page.
4. On the Ordinary Jobs page, click Hist ory in the Actions column of an ordinary job. The Execut ion
Hist ory page appears. You can view the execution history of this job on the Execut ion Hist ory page. For more information, see View the execution history.

#### 5.2.3 Schemes

##### 5.2.3.1 Create a scheme from a job

If an ordinary job or a cron job adapts to an O&M scenario of your service, you can save the job as a scheme to create service O&M tasks in similar scenarios. Prerequisites An Apsara Big Data Manager (ABM) administrator account is obtained. Context Both cron jobs and ordinary jobs can be used to generate schemes. The procedures for these two types of jobs are the same. This topic uses the procedure for an ordinary job as an example. Not ice When a cron job is saved as a scheme, no parameters are included. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Click Ordinary Jobs on the Job Execut ion page.
4. On the Ordinary Jobs page, click View in the Actions column of an ordinary job.
5. On the Job Det ails page, click Save as Scheme in the upper-right corner. The system prompts
that you have saved the scheme. Result The new scheme has the same name as the job from which it was created and is listed on the Schemes page.

##### 5.2.3.2 View schemes

A scheme is displayed in the scheme list after it is created. Apsara Big Data Manager (ABM) allows you to view existing schemes in different ways, filter schemes, and search for specific schemes. Prerequisites An ABM administrator account is obtained. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. On the Jobs page, click Job Management .
4. If there are too many schemes, you can enter the scheme name in the search bar to search for the
required scheme.
5. Change the method for viewing schemes
View schemes in list (default): Click in the upper-right corner. View schemes in cards: Click in the upper-right corner.

##### 5.2.3.3 View the execution history of a scheme

Apsara Big Data Manager (ABM) allows you to view the execution history of a specified scheme to learn the execution status of it. Prerequisites An ABM administrator account is obtained. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. On the Jobs page, click Job Management .
4. On the Schemes page, click Hist ory in the Actions column of a scheme that has directly run jobs.
You can view the execution history of this scheme on the Execut ion Hist ory page. For more information, see View the execution history.

#### 5.2.4 View the execution history

Apsara Big Data Manager (ABM) allows you to view the execution history of jobs and schemes so that you can learn about their execution details. Prerequisites An ABM administrator account is obtained. Context After you have confirmed the execution of a job, a record is automatically generated on the Execution History page. The Execut ion Hist ory page provides the following features: Provides information such as the trigger mode, current status, start time, and end time of each job. Provides job execution details and parameter setting information, and allows you to download execution details. Allows you to perform certain operations depending on the job status. For example, you can run a job that is in the Pending state or retry the execution of a job that is in the Except ion state. Procedure
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Jobs in the left-side
navigation pane.
3. Click the Execut ion Hist ory tab on the Job Execut ion page.
4. If there are too many execution records, filter them by a combination of one or more of the
following filter conditions: job name, creator, execution status, and time range. Then, click to search for required records.
5. Click View in the Actions column of a record to view the execution details.
The following table lists the operations that you can perform on records in different states.

| Execution status | Feature | Operation |
|---|---|---|
|   | View the parameter configuration | Click Paramet er Conf igurat ion at the top, and select Cont ext Paramet ers or Global Paramet ers to view the context parameters or global parameters of the task. |
|   | Download execution details | Click Download Execut ion Det ails at the top to download the job execution details to the local device. Save it into a TXT file. The execution details record the JSON and raw data of job execution. |

|   | User Guide·Managemen |   |
|---|---|---|
| Execution status | Feature | Operation |
| All statuses | View the execution details of steps | On the Servers page of a step, click View Det ails in the Actions column of a certain server. The execution details of the step on the server, including the execution output, appear in the Execution Details section. If the step includes a script, the Script Cont ent and Execut ion Paramet ers pages will appear, where you can view the script content and the script execution parameters. If the step includes a command, the Commands and Execut ion Paramet ers pages will appear, where you can view the command content and the command execution parameters. |
|   | Refresh the page | If the task is in progress, you can click Ref resh at the top to view the latest execution status. |
| Pending | Start the execution | Click St art at the top to start the execution. |
|   | Cancel the execution | Click Cancel at the top to cancel the execution. |
| Unconfirmed | Complete the manual operation | At the manual step to be operated, follow the instructions and click OK to go to the next step. |
|   | Roll back to the complete status of the previous step | At the manual step to be operated, click Rollback to roll back to the complete status of the previous step. |
|   | Cancel the execution | Click Cancel to cancel the execution. |
|   | Retry the step with exceptions | At the step with exceptions, click Ret ry to execute the step again. |
|   | Skip the step with exceptions | At the step with exceptions, click Skip to skip this step and execute the subsequent steps. |
|   | Roll back to the complete status of the previous step | At the step with exceptions, click Rollback to roll back to the complete status of the previous step. |
|   | Reset the step with exceptions to the Pending state | At the step with exceptions, click Reset to reset the step to the Pending state. When the step with exceptions is reset to the Not Started state, the execution status becomes Paused. You can click Cont inue at the top to execute the step again. |

| EExxceecputtiioonn status | Feature | Operation |
|---|---|---|
|   | View the execution details of steps with exceptions | On the Servers page of a step, click View Det ails in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you have viewed the details of the server with exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Ret ry to execute the step again on the server. If the step includes a script, the Script Cont ent and Execut ion Paramet ers pages will appear, where you can view the script content and the script execution parameters. If the step includes a command, the Commands and Execut ion Paramet ers pages will appear, where you can view the command content and the command execution parameters. |
| Failure | Retry the failed step | At the failed step, click Ret ry to execute the step again. |
|   | Skip the failed step | At the failed step, click Skip to skip this step and execute the subsequent steps. |
|   | Roll back to the complete status of the previous step | At the failed step, click Rollback to roll back to the complete status of the previous step. |
|   | Reset the failed step to the Pending state | At the failed step, click Reset to reset the step to the Pending state. When the failed step is reset to the Not Started state, the execution status becomes Paused. You can click Cont inue at the top to execute the step again. |

| Execution status | Feature | Operation |
|---|---|---|
|   | View the execution details of failed steps | On the Servers page of a step, click View Det ails in the Actions column of a certain server. The execution details of the step on the server, including the execution output and error message, appear in the Execution Details section. After you have viewed the details of the server with exceptions during the execution, you can click Skip to skip this server. Alternatively, you can click Ret ry to execute the step again on the server. If the step includes a script, the Script Cont ent and Execut ion Paramet ers pages will appear, where you can view the script content and the script execution parameters. If the step includes a command, the Commands and Execut ion Paramet ers pages will appear, where you can view the command content and the command execution parameters. |
|   | Cancel the execution | Click Cancel at the top to cancel the execution. |

### 5.3 Account management

#### 5.3.1 Terms

This topic describes the account-related terms. Apsara Stack account An account that is used to manage all your cloud resources. You can use an Apsara Stack account to access the Apsara Uni-manager Operations Console and the ABM console. role A collection of O&M permissions on cloud services. After you create an Apsara Stack account, you cannot use this account to perform O&M operations on cloud services. You must assign roles that have the required permissions to the account. Permission granting and revoking take effect immediately. You cannot add, modify, or delete the built-in roles of ABM. AccessKey A unique AccessKey pair for the account. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. An AccessKey pair is a username (AccessKey ID) and password (AccessKey secret) pair that is used to connect to cloud service instances. AccessKey pairs and Apsara Stack accounts are used in different scenarios. AccessKey pairs are used when you call the API operations of cloud services.

#### 5.3.2 Log on to the Apsara Uni-manager Operations Console

Operations Console This topic describes how to log on to the Apsara Uni-manager Operations Console. Prerequisites The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome. Procedure
1. Open your Chrome browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the
Enter key. Not e You can select a language from the drop-down list in the upper-right corner of the page.
3. Enter your username and password.
Not e Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. For security reasons, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains the following special characters: ! @ # $ % The password must be 10 to 20 characters in length.
4. Click Log On.

#### 5.3.3 Add a role

This topic describes how to customize roles in the Apsara Uni-manager Operations Console to assign appropriate permissions. Context A role is a collection of access permissions. You can assign different roles to different users to meet requirements for system access control. Roles are classified into basic roles and custom roles. Basic roles, also known as atomic roles, are preset by the Open Application Model (OAM) system. You cannot modify or delete these roles. Custom roles can be modified and deleted. You can create different O&M accounts for big data services such as MaxCompute, DataWorks, Realtime Compute, and DataHub. You can assign roles that have the required permissions to the accounts. This eliminates the need to use the same account to perform O&M operations on all big data services. The following table describes the built-in roles of ABM.

| Role name | Description |
|---|---|
| bcc admin _ | The role of a super administrator. This role is used to grant the highest permissions of ABM to an account. The highest permissions include account management, permission management, and O&M permissions of all cloud services involved. |
| bcc admin odps _ _ | The role of a MaxCompute administrator. This role is used to grant the O&M permissions on MaxCompute resources to an account. |
| bcc admin dat aworks _ _ | The role of a DataWorks administrator. This role is used to grant the O&M permissions on DataWorks resources to an account. |
| bcc admin st reamcomput e _ _ | The role of a Realtime Compute administrator. This role is used to grant the O&M permissions on Realtime Compute resources to an account. |
| bcc admin dat aapp _ _ | The role of an administrator for services other than Apsara, ABM, MiniLVS, MiniRDS, MaxCompute, DataWorks, or Realtime Compute. This role is used to grant the O&M permissions on resources of other services such as Graph Analytics, Quick BI, DataHub, and Machine Learning Platform for AI to an account. |
| bcc admin biggraph _ _ | The role of a BigGraph administrator. This role is used to grant the O&M permissions on BigGraph resources to an account. |
| bcc account admin _ _ | The role of an account administrator. This role is used to grant the O&M permissions on account management and permission management to an account. |

Procedure
1. Log on to the Apsara Uni-manager Operations Console.
2. In the upper-right corner of the page, click Settings. In the left-side navigation pane, choose
Syst em Set t ings > Role Management to go to the Role Management page.
3. Add a role.
Not e Only users that have security officer roles of the Apsara Uni-manager Operations Console can add a role in the console. i. On the Role Management page, click Add. ii. In the Add dialog box, specify the Role Name and Role Descript ion parameters, select a value from the Base Role drop-down list, and then configure the permission parameters. Not e When you specify Base Role, you can search by the bcc keyword. iii. After you configure the parameters, click OK.

#### 5.3.4 Add an Apsara Stack account

An Apsara Stack account is used to manage all your cloud resources. You can use an Apsara Stack account to access the Apsara Uni-manager Operations Console and the ABM console. Prerequisites Departments are created in the Apsara Uni-manager Operations Console. For more information, see Depart ment management in Apsara Uni-manager Operations Console Guide. O&M roles are created for big data services. For more information, see Add a role. Procedure
1. Log on to the Apsara Uni-manager Operations Console.
2. In the upper-right corner, click Settings. In the left-side navigation pane, choose Syst em
Management > User Management . On the page that appears, click the Users page.
3. On the Users tab, click Add.
Not e Only users that have security officer roles of the Apsara Uni-manager Operations Console can add an account in the console.
4. In the Add User dialog box, specify the Username and Password parameters, and click OK.

#### 5.3.5 Modify a role assigned to an account

You can modify a role that is assigned to an account. Prerequisites An Apsara Stack account that is used to manage big data services in the Apsara Uni-manager Operations Console is created. For more information, see Add an Apsara Stack account. Roles that are used to grant permissions to the Apsara Stack account are created in the Apsara Unimanager Operations Console. For more information, see Add a role. Procedure
1. Log on to the Apsara Uni-manager Operations Console.
2. In the upper-right corner, click Settings. In the left-side navigation pane, choose Syst em
Management > User Management . Click the Users tab.
3. On the Users tab, find the account and click Modif y in the Act ions column corresponding to the
account.
4. In the Modif y User dialog box, select a role from the Role drop-down list.
5. Click OK.

#### 5.3.6 Grant permissions to an Apsara Stack account

account After you create an Apsara Stack account, you cannot use this account to perform operations and maintenance (O&M) operations on cloud services. To obtain the O&M permissions, you must assign roles with the required permissions to the account. The granted permissions take effect immediately. Prerequisites You have obtained an account to which the super administrator permission or account management permission has been granted. Context Not e In the Apsara Big Data Manager, all Alibaba Cloud accounts have Alert Conf igurat ion and Cloud cont rol . The following table describes the built-in roles of ABM.

| Role Name | Description |
|---|---|
| bcc admin _ | The role of a super administrator. This role is used to grant the highest permissions of ABM to an account. The highest permissions include account management, permission management, and O&M permissions of all cloud services involved. |
| bcc admin ads _ _ | The role of an AnalyticDB administrator. This role is used to grant the O&M permissions on AnalyticDB resources to an account. |
| bcc admin odps _ _ | The role of a MaxCompute administrator. This role is used to grant the O&M permissions on MaxCompute resources to an account. |
| bcc admin dat aworks _ _ | The role of a DataWorks administrator. This role is used to grant the O&M permissions on DataWorks resources to an account. |
| bcc admin Realt imeComput e _ _ | The RealtimeCompute administrator role is used to grant O&M permissions on RealtimeCompute resources to Alibaba Cloud accounts. |
| bcc admin dat aapp _ _ | Other product administrator roles (except Apsara, ABM, MiniLVS, MiniRDS, AnalyticDB, MaxCompute, DataWorks, and RealtimeCompute) are used to grant O&M permissions on other product resources to Alibaba Cloud accounts, such as I +, QuickBI, DataHub, and PAI. |
| bcc admin biggraph _ _ | The role of a BigGraph administrator. This role is used to grant the O&M permissions on BigGraph resources to an account. |
| bcc account admin _ _ | The role of an account administrator. This role is used to grant the O&M permissions on account management and permission management to an account. |

Procedure
1. Log on to the ABM console.
2. Click at the top Management tab. In the left-side navigation pane, click Account management .
3. Select on the right Permission management tab.
4. In the Permission management On t he page, select the role that you want to grant permissions
to the Alibaba Cloud account. Operat ion > Aut horizat ion .
5. In the Aut horizat ion management In the dialog box that appears, select the Alibaba Cloud
account to be authorized. Not e If you have already assigned the role to an account, you cannot select this account.
6. Click Aut horizat ion , indicating that the authorization is successful.

### 5.4 Patch management

Apsara Big Data Manager (ABM) allows you to deploy and roll back upgrade patches for the services that it maintains. It also allows you to view detailed records of patch deployment and rollback by patch package or host. Prerequisites An ABM account with the required permissions to perform O&M operations on the corresponding service and the corresponding password are obtained. The patch package in the tar.gz format for the service to be upgraded is obtained. The cluster of the service to be upgraded is running properly. Entry
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Packages in the left-
side navigation pane. The Packages page appears. Description of the Packages page: Package Management : allows you to manage the patch packages of the service. You can upload, deploy, or delete the packages. Package Deployment : displays the deployment history and details. The Package Management page appears by default. Upload a patch package This section describes how to upload a patch package for ABM.
1. Click Upload Package on the Package Management page.
2. In the dialog box that appears, select a patch package, and then click Upload. Wait until the
uploading is complete. After the patch package is uploaded, the system prompts a success message. The patch package is then displayed in the list. Deploy a patch package After a patch package is uploaded, you can deploy it to the corresponding service cluster.
1. In the patch package list, click Deploy in the Actions column of a patch package.
2. In the dialog box that appears, set Clust er and Deployment Mode.
The valid values of Deployment Mode include: All: Deploy the patch package to all hosts where it has not been deployed. Phased Release: Deploy the patch package on a random host.
3. Click OK.
The deployment status of the patch package is Deploying. Patch deployment takes some time. Wait until the patch package is deployed. Refresh the page after the deployment is complete. The deployment status is changed to Deployed. Handle deployment failures After you use ABM to deploy a patch for a service, the patch will be automatically bound to the service release (SR) version of the service. If the service is upgraded, the SR version is changed, and the deployment status of the patch package is changed to Deployment Failed (Product Upgraded). After the service is upgraded, ABM cannot determine whether the new version has fixed the problem to be resolved by the patch. Therefore, the patch automatically becomes invalid. If the service upgrade cannot fix the problem to be resolved by the patch, click Force Deploy to deploy the patch again. If the service upgrade has fixed the problem to be resolved by the patch, click Ignore. View the deployment history and details The Deployment Records page displays the deployment information about all patch packages. The Deployment Details page displays the deployment information about all hosts.
1. Click the Package Deployment tab on the Packages page to view the deployment records.
The Deployment Records page displays the deployment records of all patch packages. You can view the name, version, product, cluster, service, service role, application type, deployment mode, and operation type of each patch package. You can also view the users who submitted the deployment requests, the total number of hosts where each patch package needs to be deployed, the number of hosts where each patch package is deployed, the number of hosts where each patch package fails to be deployed, the number of hosts where the deployment has not finished, and the deployment time. If too many deployment records exist, you can filter them by service name or package name.
2. Click the Deployment Det ails tab to view the deployment details.
The Deployment Det ails page displays the deployment information about all hosts, including the IP address, patch package name, version, product, cluster, service, service role, deployment progress, deployment status, associated build ID, deployment time, and log details. If too many deployment details exist, you can filter them by service name, package name, or deployment status. Roll back an upgrade patch After an upgrade patch is deployed, you can roll back the cluster to the version before the deployment if the cluster runs abnormally or encounters other problems.
1. Click Roll Back in the Actions column of the patch package to be rolled back.
Not e A patch package can be rolled back only when the deployment status is Deployed.
2. In the dialog box that appears, set Clust er to the cluster where the patch package is deployed,
and then click OK. Refresh the page in the rollback process. The deployment status is changed to Rolling Back. Rollback takes some time. Wait until the patch package is rolled back. Refresh the page after the rollback is complete. The deployment status is changed to Rolled Back.

### 5.5 Hot upgrade

Apsara Big Data Manager (ABM) allows you to upgrade monitoring configuration and items without interrupting the service. On the Hot Upgrades page, you can view the hot upgrade history and upgrade logs. You can also delete the upgrade packages and upgrade history on this page. Prerequisites Your ABM account is granted the required permissions to perform O&M operations on ABM. The monitoring item upgrade package in the tar.gz format is obtained. Upgrade a monitoring item without interrupting the service
1. Log on to the ABM console.
2. Click Management in the upper-right corner. On the page that appears, click Hot Upgrades in the
left-side navigation pane.
3. Click Upload File, and then select and upload the obtained tar.gz file.
The upload logs are displayed in the Upload Log section of the page in the upload process. After the upload is complete, the page displays the upgrade items for this upgrade package.
4. Select the monitoring items to be upgraded, and then click OK.
5. In the dialog box that appears, click OK to start the upgrade.
After the upgrade is complete, the system prompts that the upgrade is successful. View the hot upgrade history and logs After the hot upgrade is complete, a hot upgrade record is generated on the File Management page, including the creation time and ID of the record, and the storage address of the upgrade package. When the hot upgrade fails, you can view the hot upgrade logs to locate the fault.
1. Click the File Management tab on the Hot Upgrades page to view the hot upgrade history.
2. Click View Logs in the Actions column of an upgrade record to view the upgrade logs for each
monitoring item in this hot upgrade process. Delete a hot upgrade record ABM allows you to delete hot upgrade records, together with the corresponding hot upgrade packages and hot upgrade logs.
1. Click the File Management tab on the Hot Upgrades page to view the hot upgrade history.
2. Click Delet e in the Actions column of an upgrade record. In the dialog box that appears, click OK.

### 5.6 Health management

Apsara Big Data Manager (ABM) provides a wide range of built-in scheduling items and monitoring items for each service. These items check service faults and send alerts when necessary, enabling you to detect and fix service faults in time. Prerequisites Your ABM account is granted the required permissions to perform O&M operations on the corresponding service. The alert sources and checkers of the monitoring items are obtained. Background Different services have different scheduling and monitoring items, but their configuration and operations are the same. This topic uses MaxCompute as an example. Scheduling: You can run checkers on all hosts of a specified Apsara Infrastructure Management Framework role as scheduled to generate raw alert data. The raw alert data includes the checker, host, alert severity, and alert information. ABM stores the raw alert data in its database. Monitoring: You can mount checkers to service pages in ABM. When mounting a checker to a service page, you can set a filter policy to display only required alerts. Both the scheduling items and monitoring items are built-in and cannot be added. However, you can modify some parameters of the items, such as whether to enable an item, running parameters, and description. In addition, you can configure mount points of the monitoring items or delete monitoring items. View details and mount points of scheduling items The mount points of scheduling items are built-in and cannot be added, modified, or deleted. The mount points of the scheduling items correspond to the list of all hosts corresponding to the Apsara Infrastructure Management Framework role that runs the scheduling script.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page. The Scheduling page appears. The Scheduling page displays all scheduling items of the current service.
4. On the Scheduling page, click View in the Actions column of a scheduling item to view the details.
The details of a scheduling item include the name, alias, description, alert cause, and alert solution.
5. Click + to expand a scheduling item, and then view the mount points of the scheduling item.
Modify a scheduling item You can set the scheduling interval and running parameters of a scheduling item, and set whether to enable the scheduling item.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page. The Scheduling page appears.
4. On the Scheduling page, click Edit in the Actions column of a scheduling item. In the dialog box
that appears, set relevant parameters. T ype: The value Syst em Def ault indicates that parameters such as Execut ion Int erval and Paramet ers use the default settings. The value Cust om indicates that the parameters can be customized. Not e Set the Execut ion Int erval parameter based on the cront ab command.
5. Click OK. The system prompts that the configuration has been modified.
View faulty hosts You can view all the faulty hosts in the current cluster.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page. The Scheduling page appears.
4. Click Fault y Servers in the upper-right corner to view the faulty hosts in the cluster.
The faulty host list displays all faulty hosts in the current cluster and the Apsara Infrastructure Management Framework role of each host. Modify a monitoring item You can modify the name and description of a monitoring item and determine whether to enable it. The alert sources and checkers of monitoring items are built-in. Do not modify them.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page.
4. On the Healt h Management page, click the Monit oring tab. The Monit oring page appears.
The Monit oring page displays all monitoring items of the current service.
5. On the Monit oring page, click Modif y in the Actions column of a monitoring item to modify its
configuration.
6. Click OK. The system prompts that the configuration has been modified.
Add a mount point for a monitoring item After a mount point is added for a monitoring item, the monitoring item mounts the raw alert data to the O&M page of each service in the ABM console.
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page.
4. On the Healt h Management page, click the Monit oring tab. The Monit oring page appears.
5. On the Monit oring page, click + to expand a monitoring item, and then view the mount points of
the monitoring item.
6. Click Add Mount Point under the mount point list. In the dialog box that appears, set relevant
parameters. The following table describes some key parameters.

| Parameter | Description |
|---|---|
| Mount Point | The mount point to which the required inspection result of this monitoring item is to be mounted. For example, the value odps/host indicates that the result is mounted to the host O&M page of MaxCompute. |
| Filt er Policy | Valid values: None: Display all alerts generated by the monitoring item. Cust om: Display the alerts generated by the monitoring item in accordance with the filter configured for the service tree node. Node Name: Display the alerts whose node name is the same as the name of the current node. |
| Enabled | Specifies whether the mount point takes effect. |

7. Click OK. The system prompts that the configuration has been modified.
Delete a mount point for a monitoring item
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page.
4. On the Healt h Management page, click the Monit oring tab. The Monit oring page appears.
5. On the Monit oring page, click + to expand a monitoring item, and then view the mount points of
the monitoring item.
6. Click Delet e in the Mount Point column of the mount point to be deleted. In the dialog box that
appears, click OK. The system prompts that the deletion is successful. Delete a monitoring item
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Healt h
Management in the left-side navigation pane of the Management page.
4. On the Healt h Management page, click the Monit oring tab. The Monit oring page appears.
5. Click Delet e in the Actions column of the monitoring item to be deleted. In the dialog box that
appears, click OK. The system prompts that the deletion is successful.

### 5.7 Operation auditing

This feature allows you to view the O&M operations of the current service of Apsara Big Data Manager (ABM). The details of each operation are provided for retrieval and fault locating. Prerequisites Your ABM account is granted the required permissions to perform O&M operations on the corresponding service. Background You can view operation logs by service. For example, to view the operation logs of MaxCompute, you must go to the MaxCompute page first. The following describes how to view the operation logs of MaxCompute. Not e This page displays only the O&M operations of a service. Note that the O&M operations of job services are not included. Procedure
1. Log on to the ABM console.
2. Click
in the upper-left corner, and then click MaxComput e.
3. Click Management in the upper-right corner of the MaxCompute page, and then click Operat ion
Audit in the left-side navigation pane of the Management page. The Operat ion Audit page displays the O&M operations of the current service. In this example, the information about MaxCompute O&M operations is displayed, including the operation name, operation ID, status, submission time, start time, end time, operator, and implementation method.
4. Click Det ails for an operation to view the O&M operation details.
You can also view the causes of failed steps in detail.
5. If an O&M operation fails, view the cause of the failure.
6. When the task is in the Failure, Not Started, Pending, or Exception state, perform the operations
listed in the following table based on your situation.

| State | Executable operation |
|---|---|
| Not Started | Click St art to start the task. Click Paramet er Conf igurat ion to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Pending | Follow the instructions and click OK to go to the next step. Click Rollback to roll back to the complete status of the previous step. Click Paramet er Conf igurat ion to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Exception | Click Ret ry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Paramet er Conf igurat ion to view the parameter configuration of the task. Click Cancel to cancel the task. |
| Failure | Click Ret ry to run the step again. Click Skip to skip this step and execute the subsequent steps. Click Rollback to roll back to the complete status of the previous step. Click Paramet er Conf igurat ion to view the parameter configuration of the task. Click Cancel to cancel the task. |

7. To download the O&M operation execution logs, click Download Execut ion Det ails at the top to
save the logs to your local device.

## 6 Go to other consoles

Apsara Big Data Manager (ABM) provides links to the Apsara Uni-manager Operations Console (ASO), Apsara Infrastructure Management Framework console, and Apsara Stack Security Center console to facilitate the operations and maintenance (O&M) of big data services. Prerequisites An ABM account that works properly and its password are obtained. Procedure
1. Log on to the ABM console.
2. On the homepage of ABM, click the
icon in the upper-left corner. In the Sit e Navigat ion section, click ASO, T IANJI, or YUNDUN to go to the console that you want to access. Result After you click ASO or T IANJI, you can log on to the Apsara Uni-manager Operations Console or the Apsara Infrastructure Management Framework console without the need to enter your username and password. After you click YUNDUN, you must enter the username and password to log on to the Apsara Stack Security Center console.
