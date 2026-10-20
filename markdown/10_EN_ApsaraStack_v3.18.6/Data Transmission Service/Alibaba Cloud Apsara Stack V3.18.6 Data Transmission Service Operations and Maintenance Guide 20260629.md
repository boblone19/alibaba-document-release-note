---
title: "Data Transmission Service Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 32
source_pdf: "45b58ca37518b1e5_Alibaba Cloud Apsara Stack V3.18.6 Data Transmission Service Operations and Maintenance Guide 202606"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Data%20Transmission%20Service%20Operations%20and%20Maintenance%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Data Transmission Service Operations and Maintenance Guide

## Table of Contents

- 1 DTS O&M console overview
- 2 Log on to the DTS O&M console
- 3 Task management
  - 3.1 Manage tasks
  - 3.2 Manage modules in a task
  - 3.3 Resize the DStore memory
- 4 Task engine
  - 4.1 Query tasks
- 5 Monitoring and alerting
  - 5.1 View the monitoring information of full data migration tasks
  - 5.2 View dashboard data
- 6 Cluster management
  - 6.1 Manage clusters
  - 6.2 Manage change tracking tasks in DStore Workbench
- 7 Resource management
  - 7.1 View DTS resources
  - 7.2 Manage DTS resources
  - 7.3 View the CIDR blocks of DTS servers
- 8 O&M support
  - 8.1 Modify the Numen configurations
- 9 O&M practices
  - 9.1 View alerts
  - 9.2 View logs
  - 9.3 Practices for managing data migration and data synchronization tasks
  - 9.4 Practices for managing change tracking tasks

## 1 DTS O&M console overview

The Data Transmission Service (DTS) O&M console is a backend system for DTS. This topic describes the features of the DTS O&M console.

**Features**

The DTS O&M console provides the following features: You can view the information about DTS tasks, such as the basic information, source database information, and destination database information. You can query information such as task type, error messages, business ID, creation time, and last modification time. You can view the information about performance monitoring and alerts. You can manage clusters. You can manage various resources of DTS. e

## 2 Log on to the DTS O&M console

**console**

This topic describes how to log on to the Data Transmission Service (DTS) O&M console as a role such as an O&M engineer.

**Prerequisites**

1. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

2. In the top navigation bar of the Apsara Uni-manager Operations Console, click **Products**.
3. Choose **Databases** > **Data Transmission Service**. Then, you are navigated to the **DTS**
**O&M console**.

## 3 Task management

### 3.1 Manage tasks

This topic describes how to manage data migration, data synchronization, and change tracking tasks on the **Task List** page in the Data Transmission Service (DTS) O&M console. You can view the task details and status such as checkpoints, configure full and incremental data verification parameters, perform quick diagnostics, modify consumption time points and task configurations, and release tasks.
1. Log in to the DTS O&M console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. In the upper part of the page, you can enter a keyword in the search box and click **Query**
to search for tasks.

> **Note:** You can also click **Advanced Options** to specify more filter conditions to filter tasks.

4. Find the task that you want to manage and click the task name.
5. On the **Task Details** page, perform the following operations based on your business
requirements:

**View task details**

You can view the instance information, task information, source database information, destination database information, and DStore information.

**View the basic information about a module**

a. Find the module that you want to view, such as the Structure Migration, Full Migration, or Sync module and click **Details**. b. On the **Basic information** tab, you can view the basic information about the module, including the task ID, the IP address of the server on which the module runs, and the running version.

> **Note:** For example, you can view the running version in the Running version parameter that starts with `core-` .

**View the point in time at which the latest data record is**

**synchronized to the destination database**

a. Find the **Sync** or **Full Migration** module and click **Details**. b. On the **Basic information** tab, view the **Checkpoint** parameter whose value indicates the point in time at which the latest data record is synchronized to the destination database.

**Perform full data verification**

In the upper-right corner of the Task Details page, click **Full calibration**. In the dialog box that appears, configure the parameters and click **Add**.

> **Note:** This feature is supported only by some databases, such as MySQL, PolarDB for PostgreSQL, and MongoDB. In addition, the source and destination databases must have the same database engine.

| Param eter | Description | Usage notes |
|---|---|---|
| Count Validati on | OFF: performs full-field verification on the extracted data. ON: Perform full data verification based on the number of rows in the table, instead of the data content. | If you turn on Count Validation, you can configure only the following parameters: Number of threads, Verification completion notification, Notify Recipient, and Regular check. |
| Revise | Specifies whether to use the source database as the benchmark to directly revise inconsistent data in the destination database. | We recommend that you do not enable this feature if you require high data security. |
| CHECK SUM | Specifies whether to use the MySQL checksum table command to check for inconsistent data. If you enable this feature, the entire table works as the checksum value for comparison. | The settings take effect only when the task synchronizes or migrates data between MySQL databases. |
| Sampli ng check percen tage | The sampling ratio for full field verification. The value must be an integer between 1 and 100. | The default 0 is equivalent to 100. |
| Numbe r of threads | The size of the thread pool during data verification. You can adjust the parallelism of verification tasks. | We recommend that you set this value to a value smaller than 5. Otherwise, the load on the source database may greatly increase. |
| Slice size | The amount of data in a slice, which is the estimated amount of data in a single query. | Default value: 3000. We recommend that you do not change the value. |
| Numbe r of metad ata save differe nces | The size of the recheck slice. | Default value: 300. We recommend that you do not change the value. |

| Maxim um single table varianc e limit | The threshold for inconsistent data that is allowed for a single table during validation. | If the number of inconsistent data entries exceeds the specified value, the verification task stops checking the table. As a result, the data verification result may be inaccurate. |
|---|---|---|
| Upper limit of single table verifica tion data without primar y key | The upper limit on full verification on the table if the table contains neither a primary key nor a unique index. | If a table to be verified contains neither a primary key nor a unique index and the number of rows in the table exceeds this threshold, DTS does not perform data verification on the table. |
| Verifica tion comple tion notifica tion | Specifies whether to send a notification to the specified recipient after the data verification task is completed. | Skip this parameter. This feature is not in use. |
| Regula r check | Specifies whether to start or end the verification task at a specified time. | Skip this parameter. This feature is not in use. |

**Perform incremental data verification**

In the upper-right corner of the Task Details page, click **Incremental Check**. In the dialog box that appears, configure the parameters and click **Add**.

> **Note:** This feature is supported only by some databases, such as MySQL, PolarDB for PostgreSQL, and MongoDB. In addition, the source and destination databases must have the same database engine.

|   | Param eter | Description |   |   | Usage notes |
|---|---|---|---|---|---|
|   |   | The database and table range to be verified. Example: {"public": {"name": "public", "all": true}} specifies all tables in the public schema. |   |   | Specify the value in the JSON format. To verify a specific table, change the value of all to false and specify a list of table names. |
|   |   |   | {"public": {"name": |   |   |
|   |   | "public", "all": true}} |   |   |   |
|   | DB LIST _ |   |   |   |   |

| Source Paralleli sm | The number of concurrent threads used to read data from the source database for verification. | We recommend that you set this value to 1 to reduce the impact on the source database. |
|---|---|---|
| Process Paralleli sm | The number of concurrent threads for internal data processing and the comparison logic. | You can adjust the parallelism based on the server CPU resources. |
| Sink Paralleli sm | The number of concurrent threads used to write inconsistent data to the destination storage device, such as a database or a log. | Specify a value based on your business requirements. |
| Batch Interval | The waiting time interval for batch data processing. Unit: seconds. | A larger interval accelerates data aggregation and reduces the I/O frequency. |
| Batch Size | The number of data entries processed in each batch. | Specify a value based on your business requirements. |
| Sink Retries | The maximum number of retries allowed when the task fails to write inconsistent data. | Specify a value based on your business requirements. |
| Flink Window Size | The time window of the Flink compute engine. Unit: seconds. | Specify a value based on your business requirements. For example, if you set the time window to 10 seconds, calculation and verification output are triggered every 10 seconds. |
| Max Survival Time | The uptime of the verification task. Unit: seconds. The task automatically stops when the specified time duration ends. | Specify a proper value based on the actual production environment and the expected verification duration. |
| Retry N times, if still inconsis tent, output to databas e | If the same data entry remains inconsistent after the specified number of verifications, the data entry is declared inconsistent data and output to the database. | This feature is used to filter temporary inconsistent data caused by network jitter or latency. |

| Max inconsis tent data per sink, excess only logged | The maximum number of inconsistent data entries that each sink node can output to the database. Data entries that exceed this threshold are recorded in the log and are not written to the database. | This prevents high loads or storage overflow in the destination database due to a large amount of inconsistent data. |
|---|---|---|
| Check Start Time | The start time of the incremental verification task. | Format: YYYY-MM-DD HH:MM:SS . |
| Check End Time | The end time of the incremental verification task. | Format: YYYY-MM-DD HH:MM:SS . The data verification task automatically stops at the specified time. |
| Send Notifica tion on Comple tion | Specifies whether to send a notification after the verification task ends. | Skip this parameter. This feature is not in use. |
| Notifica tion Recipie nts | The account or contact information about the recipients of the verification result notification. | Skip this parameter. This feature is not in use. |

**Perform quick diagnostics**

Click **One-click diagnosis** in the upper-right corner to create a diagnostic task. If an error is detected, the system provides diagnostic results and suggestions based on the checks on the source database, destination database, and network.

**View user operations**

In the **Task Information** section, click **View User Actions** next to Task ID to view the operation records of the task.

**Modify the consumption checkpoint (supported only by**

**change tracking tasks)**

In the **Task Information** section, click **Modify** next to **Consumption Checkpoint**. In the dialog box that appears, enter the UNIX timestamp that corresponds to the consumption checkpoint and click **OK**.

**Modify the task description**

In the **Task Information** section, click **Modify** next to **Task Description**. In the dialog box that appears, enter the description and click **OK**.

**Modify task configurations**

In the **Task Information** section, click **Modify Configuration** to modify the configurations of the task.

**Release a task**

In the **Task Information** section, click **Release Task**.

> **Warning:** After a task is released, all data of the task is deleted and cannot be retrieved. Proceed with caution.

**Update the change tracking information (supported only by**

**change tracking tasks)**

In the **Task Information** section, click **Update Subscription**. In the message that appears, click **OK**.

### 3.2 Manage modules in a task

A DTS task comprises multiple modules. This topic explains how to manage them.
1. Log on to the DTS console.
2. In the left navigation pane, choose **Task Management > All Tasks** or **Task**
**Management > Asynchronous Tasks**.
3. Find the target task and click the task name.
4. The status of each module is displayed at the top of the **Task Details** page.

> **Note:** The color of each module indicates its status:
> Red: The module has failed.
> Blue: The module is running.
> Yellow: The module is paused.
> Green: The module is complete or has no latency.

5. Click **Details** for a module to open its management page.
6. On the module's management page, you can perform the following operations:

> **Note:** The following steps use the **schema migration** module as an example. The procedure is similar for other modules.

On the **Basic Information** tab, you can restart, pause, or skip the module, replace the instance, or modify its memory, module configuration, or task configuration.

> **Important:** When modifying the module configuration:

> **Configurable parameters**
> Click **Module Configuration**. The system displays the parameters that you

|   | mysql concurrent metadata |
|---|---|
| mysql concurrent metadata read thread count |   |

> items and their constraints (for example, "The thread count cannot be less than 5") are subject to what is displayed in the console.
> **Parameter descriptions**
> To view a parameter's full description, hover over it in the **Parameter** **Description** column. The description appears at the top of the page.
> **Activation and risks**
> You must restart the task for module configuration changes to take effect.
> Restarting a task can lead to data consistency issues, service interruption, or a rollback of migration progress.
> **We recommend performing this operation under the guidance of** **Alibaba Cloud technical support.**

On the **Migration Objects** tab, you can view the information, status, and DDL statements for each migration object.

### 3.3 Resize the DStore memory

The Data Transmission Service (DTS) O&M console is a graphic user interface (GUI) that helps you adjust the memory of DStore in a secure manner. This prevents out-of-memory (OOM) error caused by insufficient memory and improves task stability.

**Scenarios**

OOM or frequent full garbage collection (GC) errors occur in DStore, and you need to temporarily or permanently increase the memory of DStore to ensure the stability of tasks. Incremental logs are accumulated due to traffic spiking in the source database, such as large transactions and batch import operations. In this case, you must increase the memory. You need to create a high-throughput synchronization task, which requires a proper memory size based on the task specifications. You need resource allocation for existing tasks and implement finer-grained O&M.

**Usage notes**

After the memory is resized, you must restart the task for the new memory to take effect. We recommend that you perform this operation during off-peak hours.
1. Log in to the DTS O&M console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. In the upper part of the page, you can enter a keyword in the search box and click **Query**
to search for tasks.

> **Note:** You can also click **Advanced Options** to specify more filter conditions to filter tasks.

4. Click the name of the task that you want to manage. On the **Task Details** page, click
**Details** in the **Incremental Data Service** module.
5. On the **Incremental Data Service** page, click the **DStore** tab and click **Detailed** in the
Operation column.
6. In the dialog box that appears, click **Modification** to the right of **Running memory**.

> **Note:** If the memory size you enter is less than 100 MB, the system automatically ignores this setting and restores to the default memory size of the current instance type.

7. Click **Determine**.

## 4 Task engine

### 4.1 Query tasks

On the Task Query page, you can find tasks in the task engine using the task ID, business ID, sub-business ID, task creation time, or task type.
1. Log on to the DTS console.
2. In the navigation pane on the left, click **Task Engine > Task Query**.
3. On the **Task Engine - Query** page, specify the filter conditions and click **Query**.

> **Note:** Click the **ID** of a task to view its detailed information.

## 5 Monitoring and alerting

### 5.1 View the monitoring information of full data migration tasks

**information of full data migration**

**tasks**

A full data migration task needs to read data from the source database and write data to the destination database. This topic describes how to view the monitoring information of full data migration tasks.
1. Log on to the DTS console.
2. In the navigation pane on the left, choose **Monitoring and Alerting > Full Data**
**Monitoring**.
3. On the **Full Data Monitoring** page, specify filter conditions, such as task ID, name, status,
database type, and region, and then click **Query**. You can view the status of the full migration and the data transfer progress. You can also click a task name to open the task details page.

> **Note:** You can enable the **Auto-refresh** feature. The system then automatically updates the Full Data Monitoring page, so you do not need to refresh it manually.

### 5.2 View dashboard data

You can use the DTS O&M platform to view dashboards for full data migration, incremental data migration, and data synchronization tasks. This topic describes the procedure using the full data migration dashboard as an example.
1. Log on to the DTS console.
2. In the navigation pane on the left, click **Monitoring and Alerting > Full Data Migration**
**Dashboard**.

> **Note:** You can also click **Monitoring and Alerting > Incremental Data Migration** **Dashboard** or **Monitoring and Alerting > Data Synchronization** **Dashboard** to view other dashboards.
> The information displayed varies by dashboard. For example, the **Incremental** **Data Migration Dashboard** and **Data Synchronization Dashboard** display task performance information.

3. Perform the following operations as needed.
View information about full data migration tasks The **Full Data Migration Dashboard** page displays the basic information, status, and monitoring data for all full data migration tasks.

> **Note:** You can also filter tasks by specifying conditions at the top of the page or enable the auto-refresh feature.
> On the **Full Data Migration Dashboard**, the color of the **Alarm** information indicates the task status: blue indicates Pending, yellow indicates Running, green indicates Successful, and red indicates Failed.

Manage a single task In the **Operations** column, you can pause, restart, or skip a task. Manage tasks in a batch Select one or more tasks to pause, restart, or skip them in a batch. View batch operation records On the **Batch Records** tab, you can view the records of previous batch operations.

## 6 Cluster management

### 6.1 Manage clusters

This topic describes how to manage clusters in the Data Transmission Service (DTS) O&M console.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Cluster Management > Clusters**.
3. By default, the information about all clusters is displayed. You can find a cluster and click
the buttons in the **Actions** column to perform operations on the cluster based on your business requirements.

### 6.2 Manage change tracking tasks in DStore Workbench

**in DStore Workbench**

The DStore module is used to store incremental data. You can view the details of each functional module in Data Transmission Service (DTS) or restart multiple DStore tasks at a time in DStore Workbench.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Cluster Management > DStore Workbench**.
3. On the **DStore Workbench** page, perform the following operations based on your business
requirements.

> **Note:** In the upper-right corner of the page, you can enter a keyword to search for tasks or click Advanced Options to specify more filter conditions to filter tasks.

View the details of a functional module Click a tab to view the details of specific tasks on the tab. Restart or pause multiple tasks at a time a. Click the **Batch Restart Reader/Writer** tab. b. Select one or more tasks. c. Click **Batch Restart** or **Batch Pause**. d. In the dialog box that appears, click **Batch Run**.

## 7 Resource management

### 7.1 View DTS resources

You can view the overview information of Data Transmission Service (DTS) resources. This helps you understand the status of DTS resources.
1. Log on to the DTS console.
2. In the navigation pane on the left, click **Resource Management > DTS Resources**.
On the DTS Resources page, the information about all DTS resources is displayed. The information about a resource includes the region in which the resource resides, CPU utilization, and memory usage.

### 7.2 Manage DTS resources

You can view and manage Data Transmission Service (DTS) resources in the DTS O&M console.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Resource Management > DTS Resources**.
3. Perform the following operations based on your business requirements:
View resource information By default, the information about all DTS resources is displayed. In the upper part of the page, you can specify filter conditions such as resource group, region, and server IP address, and then click **Search** to filter resources. Manage resources Find a resource and click the buttons in the **Actions** column to perform operations on the resource. Initialize multiple servers at a time Select one or more resources and click **Initialize Servers**. Then, complete the subsequent operations as prompted. Add resources to a resource group Select one or more resources and click **Add Resources to Group**. Then, complete the subsequent operations as prompted.

### 7.3 View the CIDR blocks of DTS servers

**servers**

You can view the CIDR blocks of Data Transmission Service (DTS) servers of different regions and network types. This helps you troubleshoot DTS connectivity issues. For example, you can check whether the CIDR blocks of DTS servers of the corresponding region and network type are added to the IP address whitelist of a database instance or the firewall rules of a selfmanaged database.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Resource Management > DTS CIDR Blocks**.
By default, the CIDR blocks of all regions and all network types are displayed.
3. In the upper part of the page, specify a region and a network type. Then, click **Search** to
filter CIDR blocks.

## 8 O&M support

### 8.1 Modify the Numen configurations

**configurations**

This topic describes how to globally modify the key runtime parameters of the Numen component on the **O & M Support** page in the DTS O&M console.

**Supported configuration items**

| Configuration item | Parameter | Description |
|---|---|---|

| Private cloud IP address whitelist | internet ip whit _ _ e list _ | Function: The IP address blocking policy used when a DTS proxy node accesses a self-managed source or destination database over the Internet. Only IP addresses or CIDR blocks in this whitelist are allowed to establish connections. Default behavior: If this parameter is not specified, all public IP connections are blocked by default. Format: A single IP address, multiple IP addresses, CIDR blocks, or domain names Separate multiple values with commas ( , ). Spaces are not allowed. Example: 192.168.1.100,10.0.0.0/8,example.com Applicable scenarios: Security hardening: In Apsara Stack, to meet strict security compliance requirements, DTS can only access the IP addresses of specific self-managed databases. Batch authorization: You can configure a single IP address, multiple IP addresses, or a CIDR block, such as 192.168.1.0/24. This method is applicable to scenarios where you need to allow the entire CIDR block or multiple discrete IP addresses. Allow all (use with caution): If you want to allow access from all IP addresses, set this parameter to 0.0.0.0/0 . If you want to allow access from all domain names, set this parameter to * . Note The evaluation logic for IP whitelists is independent of that for domain whitelists. Please configure them according to your actual access method (direct IP connection or domain name resolution). We recommend you set this parameter to this value only in test environments or when unrestricted access is necessary. |
|---|---|---|

1. Log in to the DTS O&M console.
2. In the left-side navigation pane, choose **O & M Support > Operation and maintenance**
**tools**.
3. On the **NUMEN configuration modification** tab, find the target configuration item (such
as **Private cloud IP address whitelist**) in the upper-left corner and click **Modification** in the **Operation** column.
4. In the dialog box that appears, enter the configuration value and click **Save**.

## 9 O&M practices

### 9.1 View alerts

On the **Alerts** page, you can search for alerts by product, alert ID, source, level, status, and time range. You can then perform O&M operations on a target alert.

> **Note:** For more information about monitoring, alerts, and platform O&M operations, see the **Apsara Uni-manager Management Console O&M Guide** .

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
5. In the top menu bar, choose **Monitoring and Alerts > Alert Management > Alerts**.
The **Open** tab is displayed by default. You can also switch to the **Closed** tab to view the details of closed alerts.
6. In the **Resource Ownership** section at the top of the page, select **dts**.

> **Note:** You can also enter a keyword for a fuzzy search or use the **Advanced Search** options.

7. In the **Alert Metric ID/Alert Metric Name** column, click the ID of the target alert to open
the alert details page.
8. **Optional:** Process the alert information.
i. **Optional:** Click **Suggestions** to view the recommended actions for the alert. ii. Click **Process** or **Close**. iii. In the dialog box that appears, click **OK**. The **Alert Status** changes to **Processing** or
**Closed**.

### 9.2 View logs

This topic describes the types of Data Transmission Service (DTS) logs and how to query them. This information helps you troubleshoot issues when a task is in an abnormal state.

**Step 1: Access the DTS terminal from the Apsara Infrastructure**

**Management platform**

1.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3.
4. Click **Log In**.
5. Go to the DTS **Service Management** page.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top menu bar, choose **Platform O&M > Apsara Infrastructure Management >**
**O&M Tools**.
iii. In the navigation pane on the left, choose **O&M Tools > Service Management**. iv. On the **Service Management** page, search for and select **dts-dts** from the **Service** drop-down list.
6. On the **Service Management** page, click the **Service Instances** tab.
7. In the **Actions** column for the DTS cluster, click **Instance Details**.
8. In the **Component List**, click the target component. On the **Instance List** tab, click
**Terminal** in the **Actions** column for the target instance to access the terminal.
9. After you access the terminal, click the target host in the navigation pane on the left.
0. Select a **Server Account**, and click **OK**.

**Step 2: Find logs in the terminal**

The main components that record logs in the terminal are **DtsPortal#**, which runs the console, and **DtsNode#**, which runs the task. Both components contain log information about task failures. The following section describes how to locate the log information in these two components.

**DtsNode#**

i. Obtain the ID of the task that you want to query. For more information, see Manage tasks. ii. Access the terminal for the **DtsNode#** component. For more information, see Step 1: Access the DTS terminal from the Apsara Infrastructure Management platform.

```
iii. Run the cd /apsara/cloud/app/dts-dts/DtsNode#/dts_node/current/run/<Task ID>
```

command to navigate to the log storage directory. Other components i. Access the terminal for the component. ii. Run the docker ps | grep <Component name> command to query the ID of the container that stores the component logs. iii. Run the `docker exec -it <Container ID> /bin/bash` command to access the container. iv. Run the `cd <Log path>` command to navigate to the log storage path to view the logs.

> **Note:** Most DTS component logs are stored in /dts/<Component name>/logs/<Component name>.log. For more information, see Main log components.

**Main log components**

> **Note:** The logs for the DtsNode component are stored on the host. The logs for other components are stored in containers.

| Component | Log file location | Description |
|---|---|---|
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /logs/node.log | Main log information. Records the run logs of the node. If a task fails to run on a node, you can view the corresponding logs based on the node IP address and task ID. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/dts ddlmove.log _ Note Example: /dts/node/run/td0v********* /dts ddlmove.log _ | Records the run logs of the precheck and schema migration modules. If an error occurs in these modules, you can view the corresponding log information. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/amp.log | Records the run logs of the full migration, incremental migration, or synchronization modules. If an error occurs in these modules, you can view the corresponding log information. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/extractor.log | Records the run logs of the DReader module of the DStore console. The DReader module reads incremental logs from the source database. If an error occurs in the DReader module, you can view the corresponding log information. |

| dts-dts.DtsNode# |   |   |
|---|---|---|
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/k.log | Records the run logs of the Kafka middleware that stores incremental data. These logs are rarely used for troubleshooting. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/kafka.log | Records the log information about the connection between the DReader module, the DStore module (which stores incremental logs of the source database), and the Kafka middleware. If an error such as UNKOWN SERVER ERROR is reported for _ _ the DReader, incremental migration, or synchronization module, and the extractor.log or amp.log file indicates a DStore connection error, you can view this log to determine whether the Kafka middleware connection is abnormal. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/server.log | Records the run logs of the DStore module. These logs are rarely used for troubleshooting. |
|   | /apsara/cloud/app/dts- dts/DtsNode#/dts node/current _ /run/<Task ID>/any-all.log | Records the run logs of the full migration, incremental migration, or synchronization modules for the A2A version. If an error occurs in these modules, you can view the corresponding log information. Note For more information about how to determine the running version, see Manage tasks. |
| dts- dts.DtsPortalA2A# | /dts/portal/logs/portal.log | Main log information. Records logs of access to DTS servers from the DTS console and using OpenAPI. If a task fails to be configured or a page error occurs, you can view the corresponding logs based on the RequestId in the error message. |
|   | /dts/portal/logs/http.log | Page logs of the DTS console. |
| dts-dts.DtsMaster# | /dts/master/logs/master.log | Master scheduling logs. If a DTS task module fails to be scheduled, you can view this log. |
| dts-dts.DtsNumen# | /dts/numen/logs/numen.log | Numen run logs. These logs are rarely used for troubleshooting. |

| dts-dts.DtsProxy# | /dts/proxy/logs/proxy.log | Proxy run logs. The proxy acts as an intermediary to provide message producers and consumers with information such as the IP addresses and port numbers of the Kafka middleware. These logs are rarely used for troubleshooting. If a connection error is displayed for the DStore, DReader, incremental migration, or synchronization module (data writing module), you can view the corresponding log information. |
|---|---|---|

### 9.3 Practices for managing data migration and data synchronization tasks

**migration and data**

**synchronization tasks**

This topic describes how to perform O&M operations on a data migration or data synchronization task on Data Transmission Service (DTS) operation platform.

**Background information**

On the **Task Details** page, most modules of a data migration task are the same as those of a data synchronization task, except for the last module. Therefore, you can refer to the following examples for both data migration and data synchronization tasks.

**Skip a precheck item**

If a task fails the precheck, you can skip a specific precheck item in the DTS O&M console.

> **Note:** Before you skip a precheck item, you must be aware of the issues that are detected in the precheck and the impact of the operation. For example, if you skip a precheck item for permissions on the source database, you may fail to complete a data migration or data synchronization task due to insufficient permissions.

1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. Find the target task and click the task name.
4. On the **Task Details** page, click **Details** in the **Precheck** section.
5. On the **Precheck** page, click the **Check Items** tab.
6. On the page that appears, find the check item that you want to skip and click **Block** in the
**Actions** column.
7. After you skip a precheck item, you can restart the task in the DTS console to perform a
precheck again.

**Troubleshoot schema migration issues**

The Schema Migration module is used to migrate the schemas of the objects from the source database to the destination database, such as tables and views.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. Find the target task and click the task name.
4. On the **Task Details** page, click **Details** in the **Schema Migration** section.
5. Click the **Basic Information** tab. You can view the IP address of the server on which the
Schema Migration module is run. If the migration fails due to a whitelist issue, you can add the IP address to the whitelist of the source or destination database.
6. Click the **Migration Objects** tab. If you encounter schema migration failures, you can
troubleshoot the issues on this tab in most cases.
7. Find a failed object and click the Failed icon in the Status column. In this example, the error
message indicates that the schema migration failed due to a syntax issue. Click **View**
**Creation Syntax** to view the statement that DTS obtains from the source database.
8. Troubleshoot the issue based on the obtained statements. In this example, the view
definition cannot be obtained due to insufficient permissions of the database account. As a result, the schema migration fails. To resolve the issue, grant the required permissions to the database account.

**Troubleshoot full data migration issues**

1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. Find the target task and click the task name.
4. On the **Task Details** page, click **Details** in the **Full Data Migration** section.
5. Click the **Basic Information** tab and check the following parameters.

> **Note:** You can also click the **Migration Objects** and **Run Logs** tabs to troubleshoot issues.

View the IP address of the server on which the Full Data Migration module is run. If the migration fails due to a whitelist issue, you can add the IP address to the whitelist of the source or destination database. Troubleshoot the issue based on the error message. In this example, the request data

| e of the | max allowed packet _ _ |   |
|---|---|---|
| max allowed packet _ _ |   |   |
|   |   | paramet |

Then, click **Restart** to restart the full data migration task.

**Troubleshoot data synchronization or incremental data**

**migration issues**

1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. Find the target task and click the task name.
4. Perform the following operations based on your needs.
Troubleshoot a data synchronization issue On the **Task Details** page, find the **Data Synchronization** module and click **Details**. Troubleshoot an incremental data migration issue On the **Task Details** page, find the **Incremental Data Migration** module and click
**Details**.
5. Click the **Basic Information** tab and check the following parameters.

> **Note:** You can also click the **Run Logs** tab to troubleshoot issues.

| Parameter | Description |
|---|---|
| Run Node | The IP address of the server on which the module is run. If the synchronization or migration fails due to a whitelist issue, you can add the IP address to the whitelist of the source or destination database. |
| Checkpoint | The point in time at which the module writes the latest data record. This parameter can help you check the accuracy of latency. |
| Latency | The latency of the synchronization or migration. If the Checkpoint parameter indicates that a latency exists, you can troubleshoot the issue based on the logs. |
| Traffic | The traffic generated during the synchronization or migration. Normally, the traffic changes. If the value remains 0, an error may occur when DTS writes incremental data. |
| Error Message | The error logs displayed for troubleshooting. |

In this example, the error message indicates that the synchronization or migration fails due to an incorrect database account or password. You can return to the **Task Details** page, and click **Modify Configurations** to modify the database account or password. Then, restart the task.

### 9.4 Practices for managing change tracking tasks

**change tracking tasks**

This topic describes how to perform O&M operations on a change tracking task in the Data Transmission Service (DTS) O&M console.

**Background information**

Change tracking tasks are divided into the new version and the old version: New version: A change tracking task of the new version contains a Precheck module and an Incremental Data Service module. The O&M operations that you can perform on change tracking tasks are the same as those on data migration or data synchronization tasks. For more information, see Practices for managing data migration and data synchronization tasks. Old version: For a change tracking task of the old version, the Task Details page contains only the **Basic Information** section. In this example, a change tracking task of the old version is used.
1. Log on to the DTS console.
2. In the left-side navigation pane, choose **Task Management > All Tasks**.
3. Find the target task and click the task name.
4. On the **Task Details** page, check the consumption checkpoint and timestamp range. The
consumption checkpoint must be within the timestamp range.
5. In the lower part of the page, copy the endpoint of the topic in the **DStore Information**
section.
6. In the DRC Workbench, find the topic based on the endpoint and manage the topic. For
more information, see Manage change tracking tasks in DRC Workbench.
7. On the **Incremental Management** tab, find the store that you want to manage and click
the **+** icon next to it to view the start consumption checkpoint, current consumption checkpoint, and status information.

> **Note:** In this example, the store status indicates that the task failed to read the binary logs. You need to check whether a binlogdump process exists in the source database and whether its status is normal.
