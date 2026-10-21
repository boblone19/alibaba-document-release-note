---
title: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for RDS Operations and Maintenance Guide 20250407"
product_version: "V3.18.3"
doc_version: "20250407"
pdf_pages: 41
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for RDS Operations and Maintenance Guide 20250407.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93RDS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20ApsaraDB%20for%20RDS%20Operations%20and%20Maintenance%20Guide%2020250407.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for RDS Operations and Maintenance Guide 20250407

## Table of Contents

- 1 Architecture
  - 1.1 O&M architecture
  - 1.2 System architecture
- 2 Log on to the ApsaraDB Operations and Maintenance System
- 3 Dukang-Database Management Platform O&M
  - 3.1 Homepage
  - 3.2 Instance management
    - 3.2.1 Instance batch management
      - 3.2.1.1 Migrate instances in batch
      - 3.2.1.2 Modify instance parameters in batch
      - 3.2.1.3 Modify DIY parameters in batch
      - 3.2.1.4 Modify Redis parameters in batch
      - 3.2.1.5 Manage batch tasks
      - 3.2.1.6 Manage batch task types
      - 3.2.1.7 Manage SQL templates
    - 3.2.2 Singal instance management
      - 3.2.2.1 Overview
      - 3.2.2.2 Views instances.
      - 3.2.2.3 Instance diagnostics
      - 3.2.2.4 Manage emergency response plans
      - 3.2.2.5 Use the instance dashboard
      - 3.2.2.6 Manage instance migration plans
  - 3.3 Host management
    - 3.3.1 Create a host
    - 3.3.2 Configure hosts in batch
    - 3.3.3 View the details of a host
  - 3.4 Cluster management
    - 3.4.1 Create a cluster
    - 3.4.2 Manage service types
    - 3.4.3 Manage service nodes
    - 3.4.4 Manage DB configuration templates
    - 3.4.5 Manage Fangcunshan clusters
    - 3.4.6 Manage locations
  - 3.5 Task management
    - 3.5.1 Manage interrupted tasks
    - 3.5.2 Manage temporarily closed tasks
  - 3.6 System management
- 4 Security maintenance
  - 4.1 Network security maintenance
  - 4.2 Account password maintenance
- 5 High-risk operations
- 6 Redline V4.3.3 O&M description
  - 6.1 Services provided by Redline Enterprise
  - 6.2 Paths of files in the Docker container of redline-perf
  - 6.3 Perform environment checks
  - 6.4 O&M operations
    - 6.4.1 Scale in or out a cluster
    - 6.4.2 Upgrade or restart a cluster
    - 6.4.3 Fix connection failures
    - 6.4.4 Activate clusters in the deactived state
    - 6.4.5 Troubleshoot program exceptions
    - 6.4.6 Reset node data
    - 6.4.7 Dump logs

## 1 Architecture

### 1.1 O&M architecture

This topic describes the O&M architecture of ApsaraDB RDS.

**O&M architecture**

| Category | Component | Description |
|---|---|---|
| Business Foundation System | ServiceTest | Automated regression testing for ApsaraDB RDS features. |
|   | Abs and Service | The OpenAPI service for ApsaraDB RDS. |
|   | Location Initialization | Initialization of the Location configurations. |
|   | Database Initialization | DDL and DML configurations used to initialize ApsaraDB RDS Business Foundation System. |
| TianLong | dbinit | Initialization of TianLong. |
|   | TianLongServer | The TianLong service. |
|   | TunnelServer | An intermediate service that manages communications between ApsaraDB RDS and Elastic Compute Service (ECS). |
| ApsaraDB RDS for MySQL | InitCluster | Initialization of the cluster and host list. |
|   | DbMySQL | Database node initialization, database installation, and RPM package management. |
| ApsaraDB RDS for MySQL Management Service | PengineMySQL | The task flow service related to ApsaraDB RDS for MySQL. |
|   | RdsApiMySQL | API operations related to ApsaraDB RDS for MySQL. |
|   | McNode | The messaging agent node. |
|   | DbInit | DML configurations used to initialize ApsaraDB RDS for MySQL. |
| PolarDB | DbPolaro | The physical nodes of PolarDB. |
|   | InitCluster | Initialization of the cluster and host list. |
| ApsaraDB RDS for PostgreSQL | DbPgSql | Local SSDs: physical nodes of ApsaraDB RDS for PostgreSQL. Standard SSDs: deployed on ECS instances. |
|   | InitCluster | Initialization of the cluster and host list. |
|   | DbMssql | Resources deployed on ECS instances. |
|   | InitCluster | Initialization of the instance and host list. |

| Operations and Maintena e·Architecture | nce Gui ApsaraDB for RD |   |
|---|---|---|
| ApsaraDB RDS for SQL Server |   |   |
|   | EcsImport2012Ent | Initialization of ECS images of different SQL Server versions. |
|   | EcsImport2016Ent |   |
|   | EcsImport2012Std |   |
|   | EcsImport2016Std |   |
|   | EcsImport2017Ag |   |
| ApsaraDB RDS for SQL Server Management Service | DbInit | DML configurations used to initialize ApsaraDB RDS for SQL Server. |
|   | PengineMssql | The task flow service related to ApsaraDB RDS for SQL Server. |
|   | RdsApiMssql | API operations related to ApsaraDB RDS for SQL Server. |
|   | McNode | The messaging agent node. |
| Core services | YumServer | Deployment of host nodes for database services. |
|   | Robot | Automated O&M for database services. |
|   | MC (MessageCenter) | The message center service. |
|   | Aurora | The high-availability platform for database services. |
|   | API | The backend core API service. |
|   | Stat | The real executor of scheduled tasks for various monitoring and inspection activities. |
|   | ApsaraDB Operations and Maintenance System | The O&M platform for database services. |
|   | Performance Collection | Performance collection of earlier-version instances and hosts, and audit log collection of instances. |
|   | Backup | Full backup and incremental backup of databases. |
|   | TASK | Scheduling of the management task flow. |
|   | Whitelists | IP address whitelists of instances. |
|   | BackendLocation | The cluster and location management services. |
|   | NameService | The name service. |
|   | Database Initialization | Initialization of metadatabases. |
|   | Environment Configuration Initialization | Initialization of information of services such as Object Storage Service (OSS), Virtual Private Cloud (VPC), and Bakowner. |

### 1.2 System architecture

This topic describes the system architecture of ApsaraDB RDS.

**Backup system**

ApsaraDB RDS can back up databases at any time and restore them to a specific point in time based on the backup policy, which makes the data more traceable. Automatic backup: ApsaraDB RDS provides various types of backup. You can flexibly configure the backup start time within off-peak hours. Manual backup: You can manually back up databases at any time. Cloned instance: A cloned instance is a new instance that has the same content as the primary instance, including data and settings. This feature allows you to restore data of the primary instance or create multiple instances that are the same as the primary instance. Backup file download: During the retention period of backup files, you can log on to the ApsaraDB RDS console and download backup files to your computer.

**Data migration system**

ApsaraDB RDS provides Data Transmission Service (DTS) to help you migrate databases. ApsaraDB RDS allows you to migrate databases from one instance to another. ApsaraDB RDS provides professional tools and migration wizards to help you migrate data to or from ApsaraDB RDS instances.

**Monitoring system**

ApsaraDB RDS provides multi-dimensional monitoring services across the physical, network, and application layers to ensure business availability. Performance monitoring: ApsaraDB RDS monitors nearly 20 system performance metrics, such as disk capacity, IOPS, connections, CPU utilization, network traffic, transactions per second (TPS), queries per second (QPS), and cache hit ratio. SQL audit: The system records the SQL statements and related information sent to ApsaraDB RDS instances, such as the connection IP address, database name, access account, execution time, and number of records returned. You can use SQL audit to perform troubleshooting and check instance security. Threshold-based alerting: ApsaraDB RDS provides alert SMS notifications in the event of exceptions in instance status or performance. Web operation logging: The system records all modification operations in the ApsaraDB RDS console for administrators to check. These logs are retained for up to 30 days.

**Control system**

If a host or instance stops responding, it switches workloads over within 30 seconds after the high-availability (HA) component detects an exception. This ensures that applications run normally.

**Task scheduling system**

You can use the ApsaraDB RDS console or API operations to create and delete instances, or switch instances between the internal network and Internet. All instance operations are scheduled, traced, and displayed as tasks. ations and Maintenance System

## 2 Log on to the ApsaraDB Operations and Maintenance System

**Operations and Maintenance**

**System**

This topic describes how to log on to the ApsaraDB Operations and Maintenance System.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the format of ops.asconsole.intranet-domain-id.com. A web browser. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the logon page.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. ations and Maintenance System To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
> **Databases** > **ApsaraDB Operations and Maintenance System** .

## 3 Dukang-Database Management Platform O&M

**Management Platform O&M**

### 3.1 Homepage

The homepage of ApsaraDB Operations and Maintenance System provides an overview of your databases. You can view the basic information and exceptions, search for instances, and use the advanced search features. Log on to the ApsaraDB Operations and Maintenance System console. On the homepage that is displayed, you can find and handle ApsaraDB RDS alerts in time, and continuously optimize existing metrics. Click the number next to the exception information to view the exception details. For example, if you click **Backup exception** in the **Backup information** section, you can view the all the exceptions on RDS instances on the page that appears. You can click the exceptions and handle them accordingly.

### 3.2 Instance management

#### 3.2.1 Instance batch management

##### 3.2.1.1 Migrate instances in batch

This topic describes how to migrate multiple instances at a time.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch instance migration** in the **Instance batch**
**management** column.
5. On the **Batch instance migration waiting list** page, click **Download template file** and
fill in the template file accordingly.
6. Click **Select File**.
7. Select the completed template file and then click **Submit**.

> **Note:** Instances that use HAProxy do not experience service interruptions only when they are migrated within the same cluster.
> Batch instance migration operations do not go through approval workflows. Proceed with caution.

**What to do next**

You can click **Batch instance migration success list** or **Batch instance migration**
**failure list** in the upper part of the **Batch instance migration waiting list** page to view
the details of the migration operations.

##### 3.2.1.2 Modify instance parameters in batch

This topic describes how to modify multiple instance parameters at a time.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch instance parameter refresh** in the **Instance**
**batch management** column.
5. Select the clusters for which you want to modify the parameters and click **Select**
**parameter Template**.

> **Important:** Instance parameter changes may cause risks such as transient connections or unavailability. You can modify the parameters by following the instructions on the console.

6. On the page that appears, select the parameter template and click **Next Step**
7. Select the instances and click **Submit**.

**What to do next**

You can click **Batch refresh parameter instance successful list** or **Batch refresh**
**parameter instance failure list** in the upper part of the **Batch instance parameter**
**refresh** page to view the details of the modified parameters.

##### 3.2.1.3 Modify DIY parameters in batch

This topic describes how to modify multiple DIY parameters at a time.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch DIY parameter refresh** in the **Instance batch**
**management** column.
5. On the **BatchDIYRefresh parameter wait list** page, configure the parameters described
in the following table.

| Parameter | Description |
|---|---|

| Instance name | Instances for which you want to modify DIY parameters. Note Make sure that each database instance is of the same type and version. No spaces, tabs, or blank lines are allowed. Only parameters that take effect without restarts are supported. |
|---|---|
| dbType | The type of the database engine. Select the database engine of the specified instances. |
| dbVersion | The version of the database engine that is run by the instance. Select the database engine version of the specified instances. |
| Remarks | Enter a description. |

6. Click **To select parameters**.
7. In the message that appears, click **Determine**.
8. Select the parameters to be modified and specify the new values on the right side of the
page.
9. Click **Save** in the lower-left corner of the page.

**What to do next**

You can click **BatchDIYRefresh parameter successful list** or **BatchDIYRefresh**
**parameter failure list** in the upper part of the **Batch DIY parameter refresh** page to view
the details of the modified DIY parameters.

##### 3.2.1.4 Modify Redis parameters in batch

This topic describes how to modify multiple Redis parameters at a time.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch Redis parameter refresh** in the **Instance batch management** column.
5. In the **redis2.8 cluster** list, select the clusters for which you want to modify parameters.
6. In the list in the lower part of the page, find the parameters that you want to modify and
enter the new values in the **Set value** column. Click **Save** for each parameter.
7. In the **Modify configuration** message, click **Determine**.

##### 3.2.1.5 Manage batch tasks

This topic describes how to manage batch tasks.

**Create a task**

1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch task management** in the **Instance batch management** column.
5. In the upper part of the page, click **Create task**.
6. In the **Create task** dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Task type | Select a task type. Valid values include Batch enable SQL WALL, Batch link switching, and Batch instance minor version update. |
| Task tips | Tips for the selected task type. |
| Task parameters | Parameters for the selected task type. |
| Time rules | Issue immediately: immediately executes the task. Operation and maintenance time: executes the task in the O&M window. Specify time: executes the tasks in the specified periods of time. |
| Send SMS | Specifies whether to send SMS notifications. Valid values: Yes No |
| Instance source | The instance source. Valid values: Cluster and SqlTemplate. |
| Please select a source cluster | This parameter is available only when Instance source is set to Cluster. The instances in the cluster will populate the Input instance parameter. |
| Please selectSqlTemplat e | This parameter is available only when Instance source is set to SqlTemplate. The SQL template will populate the Input instance parameter. Note You can click Create Template on the right side to create SQL templates on the SQL Template management page. |
| Input instance | The instances on which the batch task is executed. Enter an instance name on each line. |
| Remarks | Remarks of the task. Note This is an optional parameter. |

7. Click **Submit**.

##### 3.2.1.6 Manage batch task types

This topic describes how to create a type of batch tasks.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch task type management** in the **Instance batch**
**management** column.
5. Click **New type** in the upper part of the **Instance batch management-Task type**
**management** page.
6. In the **New type** dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Name | The name of the new task type. |
| Number | The ID of the new task type. |
| API | The API name for the new task type. |
| apiInstance parameter name | The parameter of the API. Default value: DBInstanceName. |
| Prompt information | The prompt that is displayed for the task type. |
| Parameter rules | The parameter rules, including the parameter name, API parameter name, and parameter type. |
| Validation rules | The validation rules, including the validation relationship, attribute name, validation rule, and validation value. |
| Highest concurrency | The largest number of tasks of this type that can be executed at the same time. |
| Stop failure rate | The probability for the tasks to be stopped or fail. |
| Remarks | The remarks of the task type. |

7. Click **Submit**.

##### 3.2.1.7 Manage SQL templates

This topic describes how to create an SQL template.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **SQL Template management** in the **Instance batch**
**management** column.
5. Click **New template** in the upper part of the page.
6. In the **NewTemplate** dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Template name | The name of the new template. |
| Template type | The type of the new template. |
| Database name | The database on which the template is used. |

| Database type | The engine of the target database. |
|---|---|
| SQL script | The script of the SQL template. |
| New reason | The reason that you create the template. |

> **Note:** Custom SQL templates support only SELECT statements and can be used only for DBaaS databases. The creation of SQL templates must be approved in the business process management system. To ensure that the SQL template is not mistakenly executed by other users, we recommend that you give the template a descriptive name and describe the purpose of the template in detail in the New reason parameter.

7. Click **Submit**.

#### 3.2.2 Singal instance management

##### 3.2.2.1 Overview

In the instance list, you can view the information about instances, such as the basic information, data links, databases, and accounts.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
On the Instances page, you can perform the following operations: Click **Batch query** and enter instance names to query multiple instances at a time. Click **Advanced search** and configure parameters such as Database type and Instance status to query instances. Click the name of the instance that you want to view to go to the Basic information page of the instance. You can view the instance information or manage the instance. For more information, see View an instance, Diagnose an instance, Manage emergency response plans, Use the instance dashboard, and Manage instance migration plans.

##### 3.2.2.2 Views instances.

This topic describes how to view information of an instance, such as the basic information and instance performance, on the instance details page.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Find the required instance and click its name in the **User instance name** column.

> **Note:** You can also search for the target instance by entering keywords in the search box on the top of the page. You can also click **Advance search** to filter the instances by specifying the conditions.

4. In the **Basic Information** section, view the basic information about the instance. You can
also click the options in the Instance details column to perform operations such as performing backup and restoration, viewing the change records, and querying the SQL information.

##### 3.2.2.3 Instance diagnostics

You can use the instance diagnostics feature to view the performance metrics of an instance.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance Details** navigation pane, select **Instance diagnostics**. You can view the
performance metrics of the instance on the page that appears.

**References**

The performance metrics of an instance vary with the engine, engine version, and storage types of the instance. The following table lists the common performance metrics of ApsaraDB RDS for MySQL instances. For instances that run other engines or versions, the performance metrics displayed in the console shall prevail.

| Metric | Description |
|---|---|
| MySQL NetworkTraffic _ | The average volume of inbound traffic to the RDS instance per second and the average volume of outbound traffic from the RDS instance per second. Unit: KB/s. |
| MySQL QPSTPS _ | The average number of SQL statements executed per second and the average number of transactions executed per second. |
| MySQL Sessions _ | The number of active connections and the total number of connections. Unit: counts. |
| MySQL InnoDBBufferRatio _ | The read hit ratio, usage, and dirty ratio of the InnoDB buffer pool. Unit: %. |
| MySQL InnoDBDataReadWriten _ | The average volume of data that InnoDB reads per second and the average volume of data that InnoDB writes per second. Unit: KB. |

| MySQL InnoDBLogRequests _ | The average number of reads from the InnoDB buffer pool per second and the average number of writes to the InnoDB buffer pool per second. Unit: count/s. |
|---|---|
| MySQL InnoDBLogWrites _ | The average number of log write requests per second, the average number of physical writes to log files per second, and the average number of writes performed by calling the fsync() function to log files per second. Unit: count/s. |
| MySQL TempDiskTableCreates _ | The number of temporary tables that are automatically created on the hard disk during statement execution. Unit: tables. |
| MySQL MyISAMKeyBufferRatio _ | The average usage, read hit ratio, and write hit ratio of the MyISAM key buffer per second. Unit: %. |
| MySQL MyISAMKeyReadWrites _ | The average number of reads from the buffer pool by MyISAM per second, the average number of writes to the buffer pool by MyISAM per second, the average number of reads from the hard disk by MyISAM per second, and the average number of writes to the hard disk by MyISAM per second. Unit: count/s. |
| MySQL COMDML _ | The average number of DELETE statements executed per second, the average number of INSERT statements executed per second, the average number of INSERT SELECT statements _ executed per second, the average number of REPLACE statements executed per second, the average number of REPLACE SELECT statements executed per second, the average _ number of SELECT statements executed per second, and the average number of UPDATE statements executed per second. Unit: count/s. |
| MySQL RowDML _ | The average number of rows read from InnoDB tables per second, the average number of rows updated in InnoDB tables per second, the average number of rows deleted from InnoDB tables per second, the average number of rows inserted into InnoDB tables per second, and the average number of physical writes to log files per second. Unit: row/s or count/s. |
| MySQL MemCpuUsage _ | The CPU utilization and memory usage of the non-serverless ApsaraDB RDS for MySQL instance within the entire operating system. Unit: %. |
| MySQL IOPS _ | The input/output operations per second (IOPS) of the RDS instance. Unit: count/s. |
| MySQL DetailedSpaceUsage _ | The details about the disk usage of the RDS instance. These details include the total amount of disk space occupied by the RDS instance, the amount of disk space occupied by data files, the amount of disk space occupied by log files, the amount of disk space occupied by temporary files, and the amount of disk space occupied by system files. Unit: MB. |

| slavestat | The latency of data replication to the read-only RDS instance of the RDS instance. Unit: seconds. |
|---|---|
| MySQL ThreadStatus _ | The number of active threads and the number of threads connected. Unit: threads. |
| MySQL ReplicationDelay _ | The latency of data replication to the secondary RDS instance of the RDS instance. Unit: seconds. |
| MySQL ReplicationThread _ | The status of the I/O thread and the status of the SQL thread. The value 1 indicates that the thread is normal, and the value 0 indicates that the thread is lost. |
| MySQL ROW LOCK _ _ | The maximum time of a row-level lock that has been waited for in milliseconds, the average time of row-level locks that have been waited for in milliseconds, and the number of times the row-level locks have been waited for. |
| MySQL SelectScan _ | The number of times that full table scans are performed on the RDS instance. Unit: scans. |

##### 3.2.2.4 Manage emergency response plans

This topic describes how to manage emergency response plans for instances.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System** ,
choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Emergency response plan**.
4. Use the search box on the right side of the page to find the target instance and select the
check box to the left of the instance.
5. You can export the instance information to your computer as a spreadsheet file by clicking
the button in the upper part of the page.

> **Note:** Specifying conditions to search for the instance is required for exporting the instance information.

##### 3.2.2.5 Use the instance dashboard

This topic describes how to view metrics of instances, such as CPU utilization and connection utilization, on the instance dashboard.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System** ,
choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance dashboard**.
4. On the page that appears, you can view the CPU utilization, connection utilization, IOPS,
and disk usage of the instances.

##### 3.2.2.6 Manage instance migration plans

Instance migration plans can be uploaded by specifying the instances or the IP addresses of hosts. This topic describes how to migrate instances by instance plans.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System** ,
choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance plan migration**
**management**.
4. Select an upload mode for the list of instances to be migrated.

> **Note:** Mode 1: If you select Submit by instance, when an instance that cannot be migrated is detected, submission for all the instances will be stopped.
> Mode 2: If you select By hostIPSubmit, the instances that cannot be migrated will be filtered out and ignored.

5. Click **Download template file** and fill in the template file accordingly.
6. Click **Select File** and select the completed template file.
7. Click **Submit**.

> **Note:** For more information about instance migration, see Instance migration.

**What to do next**

You can click **Push success list** or **Deleted list** in the upper part of the **Instance plan**
**migration management** page to view the information about the migrated instances.

### 3.3 Host management

#### 3.3.1 Create a host

This topic describes how to create a host.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System** ,
choose **Host management > System host**.
3. Click **Emergency response plan** in the upper part of the page.
4. On the page that appears, click **New host**.
5. In the dialog box that appears, configure the parameters and click **Submit**.

#### 3.3.2 Configure hosts in batch

This topic describes how to configure multiple hosts at a time.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. Select the hosts that you want to configure and then click **Batch configuration** in the
upper part of the page.
4. In the dialog box that appears, configure the parameters and click **Submit**.

#### 3.3.3 View the details of a host

This topic describes how to view the details of a host.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, choose **Host management > System host**.
3. Search for the host you want to view by its IP address or host name.
4. Click the IP address of the host and view information on the **Host details** page. The
information includes the CPU utilization, memory usage, disk usage, and the number of instances. You can also click the options in the Host details column to view the information about host instances, performance, backups, and accounts.

### 3.4 Cluster management

#### 3.4.1 Create a cluster

This topic describes how to create a cluster.

**Create a system cluster**

1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. On the **System Cluster** page, click **New Cluster**.
4. In the dialog box that appears, select a database type and click **OK**.
5. In the **Create a cluster** dialog box, configure the parameters and click **Confirm**.

> **Note:** You can refer to the tooltip or text next to the parameter for detailed description.

**Create a user cluster template**

1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management column, click **User Cluster** and then click **Cluster Template**
on the page that appears.
4. In the dialog box that appears, click **Create a cluster Template**.
5. In the **Create a cluster Template** dialog box, configure the required parameters and click
**Submit**.

> **Note:** You can refer to the tooltip or text next to the parameter for detailed description.

#### 3.4.2 Manage service types

This topic describes how to manage cloud service types.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. Click **Service Type Management** in the Cluster management column. The **Service Type**
**Management** page appears.
Find the target service type and click **Edit** in the **Operation** column to modify the service type. Find the target service type and click **Delete** in the **Operation** column to delete the service type.

#### 3.4.3 Manage service nodes

This topic describes how to create, modify, or delete a service node.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management column, click **Service node management**.
In the upper part of the page, click **New service node**. In the dialog box that appears, configure the required parameters and click **OK**. Find the target service node that you want to modify and click **Edit** in the **Operation** column to modify the service node. Find the target service node that you want to delete and click **Delete** in the **Operation** column to delete the service node.

#### 3.4.4 Manage DB configuration templates

This topic describes how to manage DB configuration templates.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management column, click **DB configuration template** to go to the **DB**
**configuration template** page.
In the upper part of the page, click **New DB template**, enter the template information, and then click **Save** in the **Operation** column. Find the template that you want to modify, click **Edit** in the **Operation** column to modify the template, and then click **Save** in the **Operation** column. Find the template that you want to delete and click **Delete** in the **Operation** column to delete the template.

#### 3.4.5 Manage Fangcunshan clusters

This topic describes how to manage Fangcunshan clusters.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management column, click **Fangcunshan cluster management** to go to
the **Cluster group configuration** page.
4. In the upper part of the page, click **New cluster group**.
5. In the dialog box that appears, select a region, enter the cluster group name, and then click
**Confirm**.
6. Click **Set up a cluster** in the **Operation** column of the new cluster. In the dialog box that
appears, configure the resource type of the instance and click **Confirm**.
7. Optional. Find the cluster group that you want to modify and click **Modify** in the **Operation**
column to modify the template.
8. Optional. Find the cluster group that you want to delete and click **Delete** in the **Operation**
column to delete the template.

#### 3.4.6 Manage locations

This topic describes how to configure the locations of clusters.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management column, click **Location** to open the Location page.
4. On the page that appears, search for clusters by keyword and configure their locations.

> **Note:** You can also perform cluster consistency check and subdomain consistency check on this page.

Click **Add** next to the required unit, region, or zone to add a location node, and then click
**Submit**.
Click **Parameters** next to the required unit, region, zone, or subdomain to add, modify, or delete parameters. Click **Delete** next to the required unit, region, zone, or subdomain to delete a unit, region, zone, or subdomain.

### 3.5 Task management

#### 3.5.1 Manage interrupted tasks

This topic describes how to manage interrupted tasks, including user instance tasks, host instance tasks, and host tasks. This topic uses a user instance task as an example to describe how to manage interrupted tasks.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
**console**, click **Task Management**. In the upper-left corner of the **Instance tasks** page,
select **Interrupted tasks** from the drop-down list.

> **Note:** If interrupted tasks exist, perform the following steps.
> If no tasks are displayed, skip the remaining part of this topic.

3. Click a task in the **Task Name** column to view and analyze the cause of the task failure.

> **Note:** In most cases, if you encounter issues such as abnormal status of secondary databases, connection timeout errors, or password errors, you can log on to the required instance by using the instance IP address and fix the issue.

4. After you fix the issue, click **Operation** in the **Operation** column of the task.
5. Click **Perform tasks**.
6. In the **Re-execute the task** dialog box, click **Current step retry** to run the task again.

> **Important:** If you want to retry the task starting from a specific step, click **Continue from the** **specified step**. We recommend that you do not retry the task if you are not familiar with the task or purposes of the steps.

7. In the upper-left corner of the Instance tasks page, select **Running tasks** from the drop-
down list to view the status of the task.

> **Note:** If the task fails again, repeat the preceding steps.

#### 3.5.2 Manage temporarily closed tasks

This topic describes how to manage temporarily closed tasks.
1. Log on to the ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System** ,
click **Task management**. In the upper-left corner of the Instance tasks page, select
**Temporarily Closed tasks** from the drop-down list.
Click the **name** of a task. In the message that appears, view the steps during the execution of the task. Click the **operation object** of a task to view the tasks for this operation object. Click the **executor** of a task to view the information of the executor. Click **Operation** in the **Operation** column of a task to view the reason why the task is temporarily closed. On the page that appears, click **Perform tasks** to retry the task. On the page that appears, click **Intervention record** to view the intervention records of the task. Click **Add remarks** in the Operation column of a task to add remarks for the task.

### 3.6 System management

This topic describes the features of system management. Table 1. System management

| Feature | Description | Remarks |
|---|---|---|
| System Settings | Create packages, configure system settings, manage database parameter templates, configure system parameter settings, manage traffic statistics rules, configure performance settings, manage ISP information, configure component exception levels, and configure Linux kernel parameters. | The operations are high-risk operations. |
| Permission configuration | Add roles and manage permission codes. | Managing permission codes is a high-risk operation. |
| General configuration | Enable or disable ACL cache, enable or disable email, create cluster information, and send cluster information. | None. |
| Label list | Add labels and view the types, aliases, and values of labels. | None. |
| Group management | Create groups for monitoring. | None. |
| Cluster management | Create clusters, refresh management machine whitelists, refresh synchronization modes, and refresh resource cache. | The operations are high-risk operations. |
| Whitelist management | View and refresh region whitelists. | None. |
| Service Type Management | Modify and delete service types. | Creating a service type is a high-risk operation. |
| Migrate host mask information | Add and remove masked host IP addresses. | None. |

| AccessKey management | Create and view AccessKey pairs, and view logs for O&M APIs. | The operations are high-risk operations. |
|---|---|---|
| Fangcunshan cluster configuration | View the configurations of cluster groups and create cluster groups. | The operations are high-risk operations. |
| Petadata cluster statistics | View the information of Petadata clusters. | None. |
| Disaster Recovery Management | Inspect link components, inspect control components, perform DR switching, and manage DR tasks. | None. |
| Scheduled task management | Manage the scheduled tasks in the system. | None. |

## 4 Security maintenance

### 4.1 Network security maintenance

Network security maintenance consists of device and network security maintenance.

**Device security**

Check network devices and enable their security management protocols and configurations of devices. Check for timely updates to secure versions of network device software. For more information about the security maintenance method, see the device documentation.

**Network security**

Based on your network considerations, select the intrusion detection system (IDS) or intrusion prevention system (IPS) to detect abnormal Internet and Intranet traffic and protect against attacks.

### 4.2 Account password maintenance

**maintenance**

Account passwords include RDS system passwords and device passwords. To ensure account security, you must periodically change the system and device passwords, and use passwords with high complexity.

## 5 High-risk operations

| Type | Operation | Impact |
|---|---|---|
| Instance connection | Release a public endpoint | You can no longer use the public endpoint to connect to the instance. |
|   | Switch an instance to a different vSwitch | When you switch an instance to a different vSwitch, a transient connection that lasts approximately 30 seconds occurs. Make sure that your application is configured to automatically reconnect to your instance. If data is cached on your client, you can read data but cannot write data. After the vSwitch of your instance is changed, we recommend that you immediately clear the cache on the client. |
|   | Change the network type of an instance | After you change the network type of an instance from the classic network to a virtual private cloud (VPC), you cannot change the network type of the instance back to the classic network. |
| Instance management | Restart an instance | After you restart an instance, a transient connection that lasts approximately 30 seconds occurs. Before you restart an instance, we recommend that you do not write data to the instance. Proceed with caution. |
|   | Release or unsubscribe from an instance | After you release or unsubscribe from an instance, the instance is immediately removed from the console, and its data is deleted. |
|   | Manage an instance in the recycle bin | If an instance is moved to the recycle bin, the database accounts that are created for the instance are released. If you destroy an instance in the recycle bin, all data backup files of the instance are destroyed. Proceed with caution. |
| Instance configuration change | Change the specifications of an instance | When the new specifications are being applied to an instance, a transient connection that lasts approximately 30 seconds occurs. In some scenarios, you cannot perform most of the operations that are related to databases, accounts, and network settings of an instance during instance specifications change. We recommend that you do not perform DDL operations before a specification change is applied. |
|   | Perform a primary/secon dary switchover | Transient connections occur during a primary/secondary switchover. Make sure that your application is configured to automatically reconnect to your database system. A read-only instance synchronizes data from the primary instance at a specific latency. The latency may be a few minutes. |

|   | Migrate an instance across zones | The cross-zone migration triggers a transient connection. Make sure that your application is configured to automatically reconnect to your instance. If your application is not configured to automatically reconnect to your instance, you must manually reconnect your application to the instance. During cross-zone migration, your instance is unavailable for a short period of time. |
|---|---|---|
|   | Set a maintenance window | One or two transient connections occur during the maintenance window. Make sure that your application is configured to automatically reconnect to your instance. |
|   | Change the endpoint of an instance | Your application may fail to connect to the instance. Note After the endpoint or port of the instance is changed, the endpoint or port in your application also needs to be changed. |
| Upgrade of a database engine version | Upgrade the database engine version of an instance | The database engine version cannot be rolled back after it is upgraded. The virtual IP address (VIP) of the instance is changed. The instance is unavailable for a few minutes during the upgrade. A major engine version upgrade may cause compatibility issues. |
|   | Update the minor engine version of an instance | The minor engine version of an instance cannot be rolled back after it is updated. The instance is unavailable for a few minutes during the update. |
| Parameter management | Configure parameters for an instance | After you modify some parameters and apply the modification, the instance immediately restarts. |
| Management of accounts and permissions | Delete an account from an instance | If you delete a privileged account, features such as primary/secondary replication, replication between the primary and read-only instances, high availability (HA), and backup are unavailable. |
| Database management | Change the character set collation and time zone of databases on an instance | When you change the character set collation and time zone of databases on an instance, the instance restarts. During the restart, the instance is unavailable. |
|   | Delete a database from an instance | You can no longer access the database. |
| Data security | Configure an IP address whitelist for an instance | If you add 0.0.0.0/0 to a whitelist of an instance, all IP addresses are allowed to access the instance. This operation poses security risks. Proceed with caution. |

| psaraDB for RDS |   |   |
|---|---|---|
| Data security |   |   |
|   | Change the network isolation mode of an instance to the enhanced whitelist mode | You cannot switch back to the standard whitelist mode. |

on

## 6 Redline V4.3.3 O&M description

**description**

### 6.1 Services provided by Redline Enterprise

**Enterprise**

This topic describes the services provided by Redline Enterprise. Redline Enterprise provides the following services: redline-perf.LogWorker# redline-perf.OpenApi# redline-perf.PerfMaster# redline-perf.PerfWorkerr#

> **Note:** redline-perf.DbInit is discontinued.
> The collection agent of UE is deployed on physical machines in other modes.

### 6.2 Paths of files in the Docker container of redline-perf

**container of redline-perf**

This topic describes the paths of files in the Docker container of redline-perf.

**PerfMaster, PerfWorker, and LogWorker**

The following table describes the mapping relationships between the preceding data collection services and clusters.

| Service | Cluster |
|---|---|
| PerfMaster | master |
| PerfWorker | perf |
| LogWorker | log |

Paths: Root path: /home/admin/redline-perf/ Path of database data in the Docker container: /home/admin/redline-perf/ignite Paths of database data on the host

| Node | Path |
|---|---|
| PerfMaster node | /cloud/data/redline-perf/PerfMaster#/perf-master/home/admin/redline-perf/ignite/ |
| PerfWorker node | /cloud/data/redline-perf/PerfWorker#/perf-worker/home/admin/redline-perf/ignite/ |

on

| LogWorker node | /cloud/data/redline-perf/LogWorker#/log-worker/home/admin/redline-perf/ignite/ |
|---|---|

Path of log data in the Docker container: /home/admin/redline-perf/log

> **Note:** `app.log` is the main program log, which contains the log entries that record the extract, transform, load (ETL), storage, data retrieval API operation, and data aggregation to minute granularity.
> `datax.log` is the synchronization module log, which contains the log entries that record the operations of synchronizing metadata from the metadatabase and pushing real-time tables to CloudMonitor.

Paths of log data on the host

| Node | Path |
|---|---|
| PerfMaster node | /cloud/data/redline-perf/PerfMaster#/perf-master/home/admin/redline-perf/log/ |
| PerfWorker node | /cloud/data/redline-perf/PerfWorker#/perf-worker/home/admin/redline-perf/log/ |
| LogWorker node | /cloud/data/redline-perf/LogWorker#/log-worker/home/admin/redline-perf/log/ |

**OpenAPI**

This is an end-to-end gateway service. Paths: Root path: /home/admin/dll-service-aliyun-com Path of log data in the Docker container: /home/admin/dll-service-aliyun-com/logs Path of log data on the host: /cloud/data/redline-perf/OpenApi#/open-api/home/admin/dllservice-aliyun-com/logs

### 6.3 Perform environment checks

This topic describes how to perform environment checks.

**Prepare the script for batch operations**

1. Run the following commands on a jumper server to prepare the script for batch operations:

```bash
curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.PerfMaster%23" | grep ip | awk -F '"' '{print $(NF-1)}' > masterhosts curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.PerfWorker%23" | grep ip | awk -F '"' '{print $(NF-1)}' > perfworkerhosts curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.LogWorker%23" | g rep ip | awk -F '"' '{print $(NF-1)}' > logworkerhosts cat perfworkerhosts logworkerhosts masterhosts | sort -u > allhosts
```

2. Run the following command to install parallel-ssh (pssh). Skip this step if pssh has been
installed. on

```bash
wget https://parallel-ssh.googlecode.com/files/pssh-2.3.1.tar.gz
# If the jump server cannot be connected to the Internet, you can download the instal
lation file to another machine and upload the file to the jump server. tar zxvf pssh-2.3.1.tar.gz cd pssh-2.3.1 python setup.py install
```

**Check node connectivity**

After you install pssh, check whether all nodes are running normally.
1. (Required) Check the communication information between LogWorker nodes.
i. Run the following command on the jumper server:

```
pssh -h logworkerhosts -p 1 -P 'docker ps |grep redline | grep LogWorker|awk '"'"'{ print $1}'"'"' | xargs -I ID docker exec ID curl 'http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=log''
```

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see Fix connection failures.
2. (Required) Check the communication information between PerfWorker nodes.
i. Run the following command on the jumper server:

```
pssh -h perfworkerhosts -p 1 -P 'docker ps |grep redline | grep PerfWorker|awk '"'" '{ print $1}'"'"' | xargs -I ID docker exec ID curl 'http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=perf''
```

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see Fix connection failures.
3. (Required) Check the communication information between PerfMaster nodes.
i. Run the following command on the jumper server:

```
pssh -h masterhosts -p 1 -P 'docker ps |grep redline | grep PerfMaster|awk '"'"'{ p rint $1}'"'"' | xargs -I ID docker exec ID curl 'http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=master''
```

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see Fix connection failures.
4. (Required) Check whether clusters are active.
i. Run the following command on the jumper server:

```
pssh -h allhosts -p 1 -P 'docker ps |grep redline | grep -v Open|awk '"'"'{ print $ 1}'"'"' | xargs -I ID sh -c "echo ID && docker exec ID tail -n 50 ./log/app.log |gr ep '"'deactived'"'"'
```

ii. Check whether log entries that include deactived are returned. If yes, go to the corresponding Docker container and activate the clusters in the deactived state. For more information, see Activate clusters in the deactived state. on

**Check for program exceptions**

(Required) Check application logs for exceptions.
1. Run the following command on the jumper server:

```
pssh -h allhosts -p 1 -P 'docker ps |grep redline | grep -v Open|awk '"'"'{ print $1} '"'"' | xargs -I ID sh -c "echo ID && docker exec ID tail -n 100 ./log/app.log |grep -C 10 '"'Exception'"'"'
```

2. If exception logs are returned, fix this issue. For more information, see Troubleshoot
program exceptions.
3. If this issue cannot be fixed by using the solutions described in Troubleshoot program
exceptions, contact development personnel or reset node data. For more information, see Reset node data.

### 6.4 O&M operations

#### 6.4.1 Scale in or out a cluster

This topic describes how to scale in or out a cluster.

**Determine whether scale-out is required**

Check the diagnostic information of an instance in the Apsara Uni-manager Management Console. If it takes more than 5 seconds for the data records of the last 3 hours to appear, you may need to add nodes. A larger number of nodes can increase the response speed. You can balance the return on investment (ROI) of hardware based on your needs. Ten nodes can support 3,000 host nodes of ApsaraDB RDS for MySQL instances. A single ApsaraDB RDS for MySQL instance may contain more than one host node.

**Add a node**

1. Add a node and start it.

> **Note:** You can add multiple nodes at a time.

2. Connect to a node that assumes a master role.
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether expected node information is returned.
4. If the expected node information is returned, run the `curl`

```
http://127.0.0.1:8080/admin/makeBaseline?apply=true command.
```

**Remove a node**

1. Remove a node.

> **Note:** You can remove only a single node at a time.

2. Connect to a node that assumes a master role.
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether expected node information is returned.

| 4. If the expected node information is returned, run the |   |
|---|---|
| http://127.0.0.1:8080/admin/makeBaseline?apply=true |   |

5. Wait 30 minutes for data to be balanced among the remaining nodes and then continue to
on remove other nodes based on your needs.

#### 6.4.2 Upgrade or restart a cluster

This topic describes how to upgrade or restart a cluster.
1. Connect to a PerfMaster node and run the following commands to disable its database. If no
`success` message is returned, repeat the following commands until a `success` message is returned.

```bash
curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=perf" curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=log" curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=master"
```

2. Wait 2 minutes and upgrade or restart the cluster after data is stored to disks.
3. After the upgrade or restart is complete, perform environment checks. For more
information, see Perform environment checks.

#### 6.4.3 Fix connection failures

This topic describes how to fix connection failures.

**Fix the failure of missing nodes in the communication**

**information**

1. Connect to a missing node and run the following command:

```
ps aux|grep java|grep -v grep|awk '{ print $2}'|xargs kill -9
```

2. Wait 3 minutes and check node connectivity again.

**Fix the NOT IN BASELINE failure in the communication**

**information**

Run the following command on a PerfMaster node:

```bash
curl "http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=${cluster}&apply=true"
```

> **Note:** ${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

#### 6.4.4 Activate clusters in the deactived state

This topic describes how to activate the clusters in the deactived state. Run the following command on a PerfMaster node:

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}"
```

> **Note:** ${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

on

#### 6.4.5 Troubleshoot program exceptions

This topic describes how to troubleshoot program exceptions.

**Troubleshoot the exception of "partition has been lostPart"**

LogWorker node

```bash
### Connect to a Docker container of LogWorker and run the following reset commands:
curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=TABLE_LOG_AUDIT_SQLS" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=TABLE_LOG_ERROR_SQLS" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=TABLE_LOG_SLOW_SQLS" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=TABLE_LOG_AUDIT_SQL_TEMPLATES" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=TABLE_LOG_AUDIT_SQLS_ROUTE_INFO" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=CACHE_CODEC" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=CACHE_CODEC_LOCK" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=CACHE_CODEC_ATOMIC_LONG" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=ignite-sys-atomic-cache@default-ds-group" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=ignite-sys-atomic-cache@default-volatile-ds-group" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=log&cacheName=NOTIFY_LOG_IGNITE_SHUTTING_DOWN"
```

PerfWorker node on

```bash
### Connect to a Docker container of PerfWorker and run the following reset commands:
curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=CACHE_CODEC" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=CACHE_CODEC_LOCK" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=CACHE_CODEC_ATOMIC_LONG" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=NOTIFY_PERF_IGNITE_SHUTTING_DOWN" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=MONITOR_ALERT_HIS_CACHE" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=MONITOR_ALERT_STATUS_INFO_CACHE" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=CACHE_REDLINE_SNAPSHOT" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=seconds-level" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=perf&cacheName=minutes-level"
```

PerfMaster node on

```bash
### Connect to a Docker container of PerfMaster and run the following reset commands:
curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_TS_CACHE_NAME" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=NOTIFY_MASTER_IGNITE_SHUTTING_DOWN" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=LOCK_MASTER_COMPETING" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CLUSTER_COMMAND" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC_LOCK" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC_ATOMIC_LONG" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=NODE_EXECUTE_COMMAND_RECORD" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=IGNITE_PERF_LOG_METADATA" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CHECKPOINT_CACHE_NAME"
```

**Troubleshoot the exception of "Failed to perform WAL**

**operation"**

If a message of Failed to perform WAL operation is returned, contact technical personnel or reset node data. For more information, see Reset node data.

#### 6.4.6 Reset node data

This article describes how to reset node data.

**Precautions**

This operation deletes all data of a specific node. Monitoring data stored on the node is deleted and cannot be recovered. Proceed with caution.
1. Connect to the node or Docker container whose data you want to reset and run the
following command:

```
touch log/HOLD_START && ps aux|grep java|grep -v grep|awk '{ print $2}'|xargs kill -9 && rm -rf ignite/* && sleep 60 && rm -f log/HOLD_START &
```

2. Wait 3 minutes and run the following commands:
on

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}" curl "http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=${cluster}&apply=true"
```

> **Note:** ${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

#### 6.4.7 Dump logs

This topic describes how to dump logs.

**Background information**

Historical audit log data can be dumped for query.

**Precautions**

This feature is available only for ApsaraDB RDS for PostgreSQL instances that use standard SSDs. Object Storage Service (OSS) buckets must be created to store audit logs. For more information about how to create a bucket, see Create a bucket in **Object Storage Service**
**User Guide**.
OSS buckets must be cleared on a regular basis if log dump is enabled.

**Enable or disable log dump**

1. Log on to the OPS1 host. Run the following command in the /root/redline directory to obtain
the log worker nodes. If the redline directory does not exist, you can create it.

```bash
curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.LogWorker%23" | grep ip | awk -F '"' '{print $(NF-1)}' > logworkerhosts
```

2. Enable log dump.
Enable log dump for all instances.

```
pssh -h logworkerhosts 'curl "http://<The URL of the logworker cluster>:8080/admin/logTransferStore? transType=oss&accessKey=AK&accessSecret=SK&endpoint=http://oss-cn-neimeng-env30-d01 -a.intra.env30.shuguang.com/&bucketName=lztest&region=cn-neimeng-env30-d01"'
```

> **Note:** You can obtain the logworker cluster URL from Apsara Infrastructure Management Framework.

Enable log dump for the instances that are included in IP address whitelists.

```
pssh -h logworkerhosts 'curl "http://<The URL of the logworker cluster>:8080/admin/logTransferStore?transType=oss&accessK ey=AK&accessSecret=SK&endpoint=oss-cn-beijing.aliyuncs.com&bucketName=rds-sqlaudit& filterType=WHITE&whiteList=%5B%22ppassql-HttpApiTest-INS-NAME-5%22%2C%22ppassql-Htt pApiTest-INS-NAME-6%22%5D"'
```

on

|   | Note In the preceding command, ppassql-HttpApiTest-INS-NAME-5 and ppassql- HttpApiTest-INS-NAME-6 are sample instances that are included in IP address whitelists for you to enable log dump. You can add actual instance names to the command based on your needs. If you want to configure multiple instances, perform the following operations: a. Add %22 before and after each instance name. b. Use %2C to concatenate instance names with %22 added before and after. c. Add the string in between %5B and %5D after whiteList. Sample configuration: whiteList=%5B%22Instance name%22%2C%22Instance name%22%2C%22Instance na me%22%5D |
|---|---|
|   | HttpApiTest-INS-NAME-6 |

3. Disable log dump.

```
pssh -h logworkerhosts 'curl "http://<The URL of the logworker cluster>:8080/admin/logTransferStore?/admin/logTransferStore? transType=close&accessKey=&accessSecret=&endpoint=&bucketName=&region="'
```

**Use log parsing tools**

Log dump splits historical audit log data into multiple small files. To facilitate your query and analysis, you can use a log parsing tool. By default, each dump log contains data of up to 15 seconds in length or 100 MB in size.

**Configuration command**

```
java -jar perf-tools-0.0.1.jar --input <Log storage directory> --output <Directory of p arsed logs> --begin <Start timestamp> --interval <Scan duration>
```

**Parameters**

| Parameter | Description | Required |
|---|---|---|
| --input | The directory in which instance logs are stored. | Yes. |
| --output | The directory in which parsed logs are stored. | No. If this parameter is not specified, the dumped logs are stored in the standard output directory. Note The grep command can be used with a vertical bar (\|) to query logs. |
| --begin | The start timestamp of the query. Unit: seconds. | Yes. |
| --interval | The time range of the query. Unit: seconds. | No. Default value: 3600. Maximum value: 10800. |

**Sample commands**

on Parse logs.

```
java -jar perf-tools-0.0.1.jar --input /logs/ppassql-HttpApiTest-INS-NAME-0 --output /logs/ppassql-HttpApiTest-INS-NAME-0/result.data --begin 1602592098 --interval 10800
```

Use a grep keyword and a vertical bar (|) to query logs.

```
java -jar ../perf-tools-0.0.1.jar --input /logs/ppassql-HttpApiTest-INS-NAME-0 --begi n 1602592098 --interval 10800 | grep incomplete
```
