---
title: "ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260630"
pdf_pages: 117
source_pdf: "07b67ff965920bf4_Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Ed"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/PolarDB%20PG%E6%9C%AC%E5%9C%B0%E7%9B%98/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20POLARDB%20PolarDB%20for%20PostgreSQL%20%28Primary_Secondary%20Edition%29%20Operations%20and%20Maintenance%20Guide%2020260630.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary_Secondary Edition) Operations and Maintenance Guide

## Table of Contents

- 1 Architecture
  - 1.1 System architecture
  - 1.2 Component architecture
- 2 文档标题缺失，请补全后重新导出
  - 2.1 Log in to ApsaraDB Operations and Maintenance System
  - 2.2 Home page
  - 2.3 Manage instances
    - 2.3.1 Instance list
    - 2.3.2 View instance details
    - 2.3.3 General instance O&M
      - 2.3.3.1 Important Notes
      - 2.3.3.2 Check instances
      - 2.3.3.3 Diagnose an instance
      - 2.3.3.4 Restart an instance
      - 2.3.3.5 Migrate an instance
      - 2.3.3.6 Upgrade the minor version
      - 2.3.3.7 Manage instance parameters
      - 2.3.3.8 Change specifications
      - 2.3.3.9 Change storage capacity
      - 2.3.3.10 Perform an HA switchover
      - 2.3.3.11 Lock an instance
      - 2.3.3.12 Backup and restoration
      - 2.3.3.13 Recreate a secondary database
      - 2.3.3.14 Manage instance tasks
      - 2.3.3.15 Disable instance allocation
    - 2.3.4 Other instance O&M
      - 2.3.4.1 Upgrade an instance from ApsaraDB RDS for MySQL Two-node Edition with Local Disks to PolarDB for MySQL Primary/Secondary Edition
      - 2.3.4.2 Common O&M operations for secondary PolarDB for MySQL nodes
      - 2.3.4.3 Perform zone-disaster recovery switchover for PolarDB for PostgreSQL Shared Storage Edition
      - 2.3.4.4 Query SQL information for PolarDB-X instances
      - 2.3.4.5 Handle failed PolarDB-X tasks
      - 2.3.4.6 Change PolarDB-X data node specifications
      - 2.3.4.7 Configure PolarDB-X instance resources
      - 2.3.4.8 Add proxy nodes to a Tair (Redis OSS-compatible) instance
      - 2.3.4.9 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance
    - 2.3.5 Manage instances in batches
      - 2.3.5.1 Migrate multiple instances at a time
      - 2.3.5.2 Modify multiple instance parameters at a time
      - 2.3.5.3 Modify DIY parameters for multiple instances at a time
      - 2.3.5.4 Modify Redis parameters for multiple clusters at a time
      - 2.3.5.5 Manage tasks in batches
      - 2.3.5.6 Manage batch task types
      - 2.3.5.7 Manage SQL templates
    - 2.3.6 Manage instance plan migration
    - 2.3.7 View the instance dashboard
  - 2.4 Host management
    - 2.4.1 Create a host
    - 2.4.2 Configure multiple hosts at a time
    - 2.4.3 View host information
    - 2.4.4 Physical machine group
    - 2.4.5 Manage host software packages
  - 2.5 Cluster management
    - 2.5.1 Configure cluster parameters
    - 2.5.2 Manage service types
    - 2.5.3 Manage service nodes
    - 2.5.4 Manage DB configuration templates
    - 2.5.5 Manage Fangcunshan clusters
    - 2.5.6 Manage locations
  - 2.6 Task management
    - 2.6.1 Manage interrupted tasks
    - 2.6.2 Manage temporarily closed tasks
    - 2.6.3 View workflow O&M information
  - 2.7 System management
    - 2.7.1 Feature Overview
    - 2.7.2 Change the unified storage location of logs
  - 2.8 Check important components
  - 2.9 Handle exceptions
  - 2.10 Appendix
    - 2.10.1 Log in to the Apsara Uni-manager Operations Console
- 3 Apsara Uni-manager Platform Operations
  - 3.1 Configure a custom password policy for PolarDB
  - 3.2 Turn on the IPv6 display switch for PolarDB
- 4 Security maintenance
  - 4.1 Network security maintenance
  - 4.2 Account and password maintenance
- 5 Troubleshooting
  - 5.1 Fault emergency mechanism
  - 5.2 Stock-up mechanism
  - 5.3 Troubleshooting procedure
  - 5.4 Common faults and solutions
    - 5.4.1 High CPU utilization of an instance
    - 5.4.2 Sudden increase in database disk usage
    - 5.4.3 Interrupted rebuild of a secondary database with local disks
    - 5.4.4 Instance Cross-Machine Upgrade/Downgrade: Read-Only Original Instance, Target Instance Not Started, or Instance Promote Failed
    - 5.4.5 pg_wal logs fill up disk space on a PolarDB for PostgreSQL instance
    - 5.4.6 What do I do if the disk space is insufficient?
    - 5.4.7 Interrupted replication
    - 5.4.8 Insufficient swap space
    - 5.4.9 High loads
    - 5.4.10 High replication latency
    - 5.4.11 Module exceptions
  - 5.5 Hardware troubleshooting
    - 5.5.1 Disk failure
    - 5.5.2 Failures requiring server shutdown, including memory, motherboard, CPU, and power supply failures
- 6 High-risk operations
- 7 Redline V4.3.3 O&M description
  - 7.1 Services provided by Redline Enterprise
  - 7.2 Paths of files in the Docker container of redline-perf
  - 7.3 Perform environment checks
  - 7.4 O&M operations
    - 7.4.1 Scale in or out a cluster
    - 7.4.2 Upgrade or restart a cluster
    - 7.4.3 Fix connection failures
    - 7.4.4 Activate clusters in the deactived state
    - 7.4.5 Troubleshoot program exceptions
    - 7.4.6 Reset node data
    - 7.4.7 Dump logs

e

## 1 Architecture

### 1.1 System architecture

This topic describes the architecture of PolarDB for PostgreSQL.

**Backup system**

PolarDB for PostgreSQL can back up databases anytime and restore them to a point in time based on backup policies. This way, data is more traceable. Automatic backup: PolarDB for PostgreSQL provides various types of backup. You can flexibly configure the backup start time within off-peak hours. Manual backup: You can manually back up databases at any time. Cloned instance: A cloned instance is a new instance that has the same content as the primary instance, including data and settings. This feature allows you to restore data of the primary instance or create multiple instances that are the same as the primary instance. Backup file download: During the retention period of backup files, you can log on to the PolarDB console and download backup files to your computer.

**Data migration system**

PolarDB for PostgreSQL provides Data Transmission Service (DTS) to help you migrate databases. Data replication between instances: You can migrate databases from one instance to another with ease. Data migration: Professional tools and migration wizards are provided to help you migrate data to or from PolarDB instances.

**Monitoring system**

PolarDB for PostgreSQL provides multilevel monitoring services across the physical, network, and application layers to ensure service availability. Performance monitoring: PolarDB monitors nearly 20 system performance metrics, such as disk capacity, IOPS, connections, CPU utilization, transactions per second (TPS), and queries per second (QPS). SQL Audit: The system records the SQL statements and related information sent to PolarDB instances, such as the connection IP address, database name, access account, execution time, and number of records returned. You can use SQL Audit to identify problems and check instance security. Threshold-based alerting: PolarDB can send alert notifications by SMS in the event of exceptions in instance status or performance. Web operation logging: The system records all modification operations in the PolarDB console for administrators to check. These logs are retained for up to 30 days.

**Control system**

If a host or an instance fails, the workloads are switched over within 30 seconds after the high-availability (HA) component detects an exception. This ensures that applications run as expected.

**Task scheduling system**

e You can use the PolarDB console or call API operations to create and delete instances, or switch instances between the internal network and Internet. All instance operations are scheduled, traced, and displayed as tasks in the backend.

### 1.2 Component architecture

This topic describes the components of PolarDB for PostgreSQL.

| Component | Description |
|---|---|
| Metadabase (including the overall metadabase, ApsaraDB Operations and Maintenance System, FTP, DRC, and performance library) | Manages the metadata and the tasks of each component in PolarDB for PostgreSQL. |
| proxy | Implements the features such as database sharding, table partitioning, routing, and firewall. |
| Maotai | Manages the resources, tasks, backups, performance, and releases in PolarDB for PostgreSQL and optimizes SQL queries. |
| aurora | Ensures the high availability of all database nodes. |
| PolarDB API | Calls API operations to access PolarDB. |
| Database node | Stores user data. |
| DRC | Imports user data to the cloud and migrates data between instances. |
| REDIS | Stores the SQL details and performance data of instances. |
| ApsaraDB Operations and Maintenance System | A backend database management platform system. |
| Message center | Sends messages between control nodes and database nodes. |
| Jstorm/kafka/zookee per | SQL statements are stored into Kafka and then written to Simple Log Service (SLS) by using JStorm. Zookeeper is used for configuration file management. |
| FTP | Uploads backup sets for Windows users. |

e

| Bianque | Diagnoses function-related issues. |
|---|---|
| Logagent | Collects host logs. |
| Erlbox | Manages log collection components. |
| Mscheck | Verifies data for master and replica nodes. |
| Mysqlpcap | Collects SQL statements to Tair (Redis OSS-compatible). |
| Tcprt | Collects the response time of user requests. |
| Webdump | Collects the Internet traffic of users. |

## 2 文档标题缺失，请补全后重新导出

### 2.1 Log in to ApsaraDB Operations and Maintenance System

**and Maintenance System**

This topic describes how users, such as O&M engineers, log in to ApsaraDB Operations and Maintenance System.

**Use the Apsara Uni-manager Operations Console**

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
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
5. In the top navigation bar of the Apsara Uni-manager Operations Console, click **Product**
**Operation**. In the **Databases** section, select **ApsaraDB O&M System**.

### 2.2 Home page

This topic provides an overview of the home page of the ApsaraDB Operations and Maintenance System console and describes how to navigate to other pages.

**Home page overview**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the home page, you can view the overall dashboard information, such as **instance**
**distribution by version** and **host distribution by model**, exceptions, instance query,
and advanced query.
3. When O&M personnel receive database-related P0 or P1 alerts, they can check for
exceptions in tasks, components, hosts, and instances on the home page and Exception list page of ApsaraDB Operations and Maintenance System, and promptly handle or confirm high-risk events. You can click the number next to an exception item to view the exception details. For example, you can click **Backup exception** in the Backup information section to go to the instance exception information page. On the page that appears, all database instance exceptions are displayed. You can click the exceptions and handle them accordingly.

**Data Summary**

Data summary is presented across three dimensions: instances, hosts, and clusters. Click **HA shutdown** to view a statistical chart of HA-disabled instances categorized by database engine. Click other data items to go to filtered result pages for instances, hosts, or clusters based on specific criteria. In the following sections, you can view different types of dashboards or exception data. You can click to go to the corresponding page.

**Backup information**

This section displays the number of instances with backup exceptions, ongoing backups, binlog switch exceptions, and other statuses. You can click to go to the corresponding instance list page to view details such as the instance status, exception cause, and detection time.

**High availability HA information**

This section displays the number of instances with HA disabled, the number of instances with abnormal HA status, and the number of HA switches in the last hour.

**Resource Information**

This section provides statistics for two types of exceptions: resource configuration exceptions and system operation exceptions. Diagnostic levels include Error, Warning, and Tips. Click the exception count on the right to go to the detailed list page.

**Task information**

This section displays the total number of tasks in Running, Waiting, and Interrupted statuses. Click **Number of tasks** to go to the **Task management > Instance tasks** page.

**Dependency component state**

This section visually presents the health status of dependent components, including rdsapi, perf, bak, dukang, and dbass.

**System Inspection**

This section displays the total score of the health status, and the top 8 charts for black list (abnormal items) and honor roll of system inspection results. Worst-performing top eight: database performance issues, such as pgxc_replication_stop and pgxc_conf_inconsistent. Best-performing top eight: configuration and security risks, such as docker_hostnames_unavailable.

**Exception list**

Click **View details** in the upper-left corner of the **System Inspection** section. You are redirected to the **Exception list > Customer Instance** page. By default, the **customer**
**instances** whose exception level is Critical are displayed.
In the left-side navigation pane, you can go to the **Host**, **Host Instance**, **HA**, **Scheduled**
**Service**, and **Backup** pages to view critical-level exception information for various
resources. You can also switch to the **Abnormal market** page, which supports sorting by score and component name, as well as searching by component name. Click a component name to go to the Exception information Host page, where exception handling operations can be performed on problematic hosts.

### 2.3 Manage instances

#### 2.3.1 Instance list

This topic describes how to view the information about instances, such as the basic information, data links, databases, and accounts, in the instance list.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, choose **Instance management > Instance List**. On the Instance List page, you can perform the following operations: Click **Batch query**. In the Batch query dialog box, enter instance names to query multiple instances at a time. Click **Advance search** and configure parameters such as Database type and Instance status to query instances. Find an instance that you want to manage and click its name to go to the Instance details page. You can view the instance information and manage the instance. For more information, see Diagnose an instance, Manage multiple instances at a time, Use the instance dashboard, and Manage instance migration plans.

#### 2.3.2 View instance details

On the Instance Details page, you can view the basic information of the instance and perform O&M operations.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.

> **Note:** For a specific database cluster instance, such as Tair (Redis OSS-compatible) or AnalyticDB for PostgreSQL, choose **Instance management > Cluster instance List**.

3. On the Instance List page, find the instance that you want to manage and click its name in
the **User instance name** column.

> **Note:** You can search for the instance by entering keywords in the search box in the upper part of the page. You can also click **Advance search** to filter instances by condition.

4. On the **Instance details** page, you can view the basic information of the instance. In the
lower part of the page, you can click the buttons to perform quick O&M operations. You can also click a menu in the left-side navigation pane to go to the corresponding page to perform more O&M operations on the instance. For more information about the instance O&M capabilities supported in the ApsaraDB Operations and Maintenance System console, see Instance O&M overview.

**Instance O&M overview**

> **Note:** The following table describes parameters for the new version of the console. If you use the previous version, click **Switch to New Version** at the top of the page.
> The O&M capabilities vary across instances based on the database engines. For more information about the supported O&M capabilities, see the ApsaraDB Operations and Maintenance System console.

| Menu in the left-side navigation pane | Page introduction | Remarks |
|---|---|---|
| Basic information | Displays the basic information of the instance, including instance topology, instance status, network information, performance information, management parameters, SLB connection information, region information, host instance information, instance type, and O&M time. In the lower part of the page, you can perform O&M operations on the instance, such as Migration, Version upgrade, Specification change, HA switch, Standby database reroute, Restart an instance, Delete an instance, and Storage space changes. | None. |
| Instance Panorama | Displays the instance roles, disk space trend, HA switchover records, suggestions for slow SQL queries and indexes, task records, and O&M records of the instance. | None. |
| Data Link | Displays the data link of the instance. | None. |
| Instance diagnosis | Displays the trend charts of key performance metrics of the instance. You can select a time range to display the trend charts. | For more information, see Diagnose an instance. |
| Task list/Task Management | Displays the task list. You can view the task parameters, task operations, and execution logs of the instance. | For more information, see Manage instance tasks. |
| Go to Whitelist | Navigates to the task management page, where you can add a whitelist. | None. |
| Go to Approval Applications | Navigates to the task management page, where you can view information such as the approver corresponding to a task ID. | None. |

| Instance change Records | Displays instance logs, task logs, HA logs, API logs, management logs, primary-secondary inconsistency check, ROBOT logs, Bartender restoration history, and Bartender task history. | None. |
|---|---|---|
| Database information | Displays the database information in the instance. Allows you to perform operations, such as creating, migrating, and deleting databases. | Migrating databases and deleting databases are high-risk operations. |
| Account information | Displays the account information of the instance. Allows you to perform operations, such as creating accounts, changing passwords, and resetting the password of an account. | Resetting and changing passwords are high-risk operations. |
| Kernel-instance parameters | Allows you to modify the parameters of an instance or view the parameter modification history. | Modifying parameters is a high-risk operation. For more information, see Manage instance parameters. |
| Management- instance parameters |   |   |
| Instance SQL information | Allows you to view the SQL log details, slow SQL query details, and index statistics of the instance. | None. |
| Configure an instance | Allows you to configure whitelists, instance tags, instance resources, instance performance, and O&M settings. Among which: Whitelist: You can create and configure whitelists and configure security groups. Instance tag: You can configure instance tags. Instance resource: You can configure the IOPS, CPU, maximum number of connections, and disk space. Instance performance: You can configure the performance collection frequency. Instance O&M: You can configure instance memory isolation, availability and reliability policies, whether to enable SQL details collection, and log audit versions. | Except for configuring whitelists, all the operations are high-risk operations. |

| Backup Recovery | Displays the backup history. Allows you to restore data to a point in time, obtain backup details, obtain information about the uploaded file, and restore the instance data from a data backup file. | Restoring data to a point in time is a high-risk operation. Proceed with caution. For more information, see Backup and recovery. |
|---|---|---|
| Backup policy | Displays the backup information, backup policies, and IDs of binary logs. Allows you to modify backup policies, create temporary backups, create databases for individual databases, modify binary log policies, and clear logs. |   |
| BINLOG log | Displays the history of binary logs, the generation and consumption trends of binary logs, and a list of binary logs. Allows you to obtain the download links and upload information of binary logs. | None. |
| BINLOG management | Allows you to view the history of binary logs. Allows you to view and modify the binary log policies, including the upload method, whether to compress data during upload, local cleanup method, whether to enable log backup, local retention period, and number of retained binlogs. | None. |
| Migration recovery log | Displays a list of migration tasks, instance recovery logs, and logs for database migration across instances. | None. |
| Historical availability | Allows you to view availability, failures, and error logs. | None. |

#### 2.3.3 General instance O&M

##### 2.3.3.1 Important Notes

**Read before operation**

> **Warning:** Some operations described in this section, such as instance restart, minor engine version update, and backup and restoration, involve core changes to the underlying infrastructure. These operations are irreversible or high-risk. Improper operations may lead to data loss, service interruption, or performance jitter.
> Before you perform any O&M operations, carefully read the relevant tutorials and the precautions and key risk reminders on the console interface. If necessary, perform operations under the guidance of Alibaba Cloud professional technicians. Once you click Submit, Confirm or similar commands, it is deemed that you have been fully aware of all potential risks and voluntarily bear all the consequences arising therefrom. Proceed with caution.

##### 2.3.3.2 Check instances

This topic describes instance-related check operations to help you resolve issues quickly.

**Background information**

Primary/secondary synchronization, version consistency, and read/write isolation are fundamental to database security and stability. Instance diagnostics empower O&M personnel to probe the underlying database status by using SQL statements. This enables rapid verification of instance health and security during routine inspections, troubleshooting, or disaster recovery drills.

**Applicable scenarios**

Routine health inspection: regularly verifies that the primary/secondary latency is zero, versions are consistent, and read/write roles are correct to prevent potential risks. Emergency troubleshooting: quickly identifies the root causes of data inconsistencies, write failures, or switchover exceptions (such as synchronization interruptions, version mismatches, or configuration errors). Change and drill verification: verifies whether instance status meets expectations after upgrades or switchover drills, or before major security events. Compliance and security audit: ensures that instances run on approved secure versions and eliminate unauthorized write paths.

**Usage notes**

Pre-check of whitelists: If a `not in whiteList` error is returned when you execute an SQL statement, you must log in to the console and add the current IP address to the whitelist of the instance. Otherwise, no diagnostic results can be obtained. Differentiation of the primary and secondary roles: When you run commands, you must clearly distinguish between the primary and secondary databases. Despite separate selection of the primary and secondary databases on the operation interfaces, evaluation criteria vary. For example, `read_only` must be set to OFF on the primary database and to ON on the secondary database, whereas synchronization status is monitored on the secondary database. Do not confuse the roles of the primary and secondary databases, as this will lead to incorrect status assessments. If exceptions occur, forced repairs or restarts without authorization are not allowed. You should retain the evidence and immediately contact Alibaba Cloud technical support to prevent spreading the failure impact or causing data loss. MySQL is used in the following operations. You can refer to the actual environment for specific details.

**Check primary/secondary synchronization**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. In the left-side navigation pane, click **Instance diagnosis**. On the page that appears, click
the **ExecutionSQL** tab.
4. In the lower part of the page, select **Main Library**, enter the following command in the
command box, and then click **Execution** to view the output result. Repeat this step for
**Backup Library**.

```
show slave status\G;
```

5. If the following results are returned, the primary/secondary synchronization status is
normal. If the results do not meet expectations, contact Alibaba Cloud technical support.

> **Note:** If a `not in whiteList` error is returned, check the whitelist settings.

Slave_IO_Running : Yes Slave_SQL_Running : Yes Seconds_Behind_Master : 0

**Check the read-only attribute of an instance**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. In the left-side navigation pane, click **Instance diagnosis**. On the page that appears, click
the **ExecutionSQL** tab.
4. In the lower part of the page, select **Main Library**, enter the following command in the
command box, and then click **Execution** to view the output result. Repeat this step for
**Backup Library**.

```
show variables like 'read_only';
```

5. If the value of this parameter is OFF for the primary database and ON for the secondary
database, the results meet expectations. If the results do not meet expectations, contact Alibaba Cloud technical support.

**Check the minor version of an instance**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. In the left-side navigation pane, click **Instance diagnosis**. On the page that appears, click
the **ExecutionSQL** tab.
4. In the lower part of the page, select **Main Library**, enter the following commands in the
command box, and then click **Execution** to obtain the minor version and kernel version. Repeat this step for **Backup Library**.

```
show variables like 'rds_release_date'; select version();
```

##### 2.3.3.3 Diagnose an instance

The instance diagnosis feature of ApsaraDB Operations and Maintenance System provides comprehensive database health check and performance analysis services. The feature supports real-time monitoring of instance resource usage, performance metrics, and internal engine status. This helps O&M personnel accurately locate performance bottlenecks, efficiently troubleshoot exceptions, and optimize instance configurations. This comprehensively improves the efficiency and stability of database O&M.

**Scenarios**

Performance bottleneck analysis: When an instance experiences high CPU utilization, saturated IOPS, or high memory usage, this feature can be used to locate the resource usage bottleneck and identify the source of abnormal consumption. Troubleshooting of exceptions: When an instance shows a sudden increase in connections, an abnormal primary/secondary latency, or slow request response, this feature can be used to quickly locate the root cause of the fault and shorten the mean time to repair (MTTR). SQL optimization: When your business returns slow queries and needs to identify highconsumption statements, this feature can be used to obtain the list of slow SQL statements and optimization suggestions. Emergency O&M operations: When you need to directly execute diagnostic SQL statements or view the underlying engine status in the console, this feature allows direct connection to the instance to execute specific diagnostic commands.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. On the Instance List page, find the required instance and click its name in the **User**
**instance name** column.
4. In the **Instance Details** section, click **Instance diagnosis**. You can click the
corresponding tab to view data or perform operations.

> **Note:** The diagnostic capabilities vary across different database engines. The actual feature tabs displayed are subject to the console configuration. The following description takes PolarDB for MySQL as an example.

| Feature module | Description |
|---|---|
| Instance Proxy Connection Logs | Displays log information for connections to the instance through the Proxy layer. |

| Instance Performance Information | Displays the trend charts of the core performance metrics of the instance. Supported intervals: 15 minutes, 3 hours, 6 hours, 12 hours, 1 day, 2 days, or custom. Supported metrics: Disk space details, disk utilization, CPU utilization, IPOS utilization. Note A large number of metrics are supported. The actual displayed metrics are subject to the console configuration. |
|---|---|
| Real-time Instance Information | View the trend of instance connections. |
| InnoDB Instance Real- Time Status | Obtains status by directly connecting to the instance of users, with a customizable interval time (in seconds). |
| Innodb Status | Obtains InnoDB status information by directly connecting to the instance of users and running the SHOW ENGINE INNODB STATUS command. Used for in-depth analysis of deadlock, transaction wait and other underlying problems, with a customizable interval time (in seconds). |
| Instance Log and Slow Diagnosis | Automatically analyzes slow SQL queries and performance lag in the instance and provides optimization suggestions, with customizable interval time queries. |
| Execution of SQL Statements | i. Configure the SQL execution location: primary or secondary, and set the destination database and maximum number of returned rows. ii. Enter the SQL statement to execute and click the Execute button. Important Executing SQL statements is risky and may cause failures. Exercise caution when you perform this operation. Line breaks are not supported. Only single-line SQL statements can be executed. SQL execution for PolarDB child instances is only allowed on the primary instance. |

##### 2.3.3.4 Restart an instance

ApsaraDB Operations and Maintenance System supports restarting various database instances to handle service exceptions, enable configuration changes, or meet maintenance requirements.

**Usage notes**

**Feature coverage**: The instance restart feature applies to most database instance types
such as ApsaraDB for RDS, PolarDB, and AnalyticDB. However, advanced configurations such as cold/hot restart policies and node selection are only supported for AnalyticDB instances.
**Service interruption**: During the restart, the instance will be unavailable for a short
period of time. We recommend that you perform this operation during off-peak hours.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance in the **User instance name** column to go to the
Instance details page. Scroll down to the bottom of the page and click **Restart an**
**instance**.
4. Confirm or configure the restart policy and click **OK**. This topic uses `AnalyticDB` as an
example to describe operations on the restart page.

> **Note:** The restart policies displayed or supported on the page vary based on the database type. For more information, see the restart policies displayed on the page.

| Parameter | Description |
|---|---|
| Restart policy | Hot start: Only processes in the container are restarted. The original environment of the container is retained. This is similar to docker restart . It is suitable for quick recovery from process exceptions with short service interruption. Cold start: The container is destroyed and rebuilt, and the runtime environment is reset. This is similar to docker rm && docker run . It is suitable for solving the environmental pollution of the container or deep-seated state issues, with longer service interruption. |
| Concurrencie s | Controls the number of nodes that are restarted at the same time. A smaller value reduces impact on services but increases total duration; a larger value improves parallelism but causes higher instantaneous load. We recommend that you configure the settings based on your business tolerance. |
| Host instance | Lists all compute nodes under the current instance. You can select specific nodes as needed for a rolling restart. For example, you can restart only abnormal nodes to avoid impacting overall services caused by a full restart. |

##### 2.3.3.5 Migrate an instance

ApsaraDB Operations and Maintenance System supports migrating instances across zones or subdomains. Migration applies to scenarios such as resource scheduling, disaster recovery drills, and hardware upgrades. You can configure migration for primary instances, standby instances, and read-only (RO) instances.

**Preparations**

Before submitting a migration task, we recommend that you record the host information of the current instance. Check whether the physical instance (the primary, secondary, or read-only node) to be migrated and its associated logical instance have any running tasks or abnormally interrupted tasks. If such tasks exist, resolve or terminate them before proceeding with the migration.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance in the **User instance name** column to go to the
Instance details page. Find the migration entry:

> **Note:** The entry may vary slightly by database engine. The actual displayed items are subject to the console configuration.

Migration entry 1: On the **Basic Information** page, scroll down to the bottom of the page and click
**Migration**.
Migration entry 2: a. On the **Basic information** page, find the **Sub-instance Information** section. In this section, click the ID of a standby instance or a read-only instance. This example demonstrates how to migrate a standby instance. b. Scroll down to the bottom of the page and click **Migration**.
4. Configure the migration destination and click **Submit**.

> **Note:** Migration configuration items may vary slightly by database engine. The actual displayed items are subject to the console configuration.
> Virtual Private Cloud (VPC) instances do not support random zones.
> The vSwitch ID is required during cross-zone migration.
> The primary and secondary nodes must be in the same zone in primary zone mode,.
> Commercial instances can only be migrated to commercial subdomains, and internal instances can only be migrated to ODBS subdomains.

| Parameter | Description |
|---|---|

| VIP switching time | Operation and maintenance time switching: The migration is performed during a preset maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic information page of the instance. Switch now: The migration immediately takes effect and may affect your business. Specify Time: You can specify a time point for the migration. Configuration is required. |
|---|---|
| Disk type | Select as needed. You can leave it unspecified. Available disk types: SSD SATA Hybrid storage |
| Region | Must be the same as the source instance. The available options are limited. The actual displayed items are subject to the console configuration. |
| Subdomain | Select the destination subdomain. |
| Migration reason | Enter the reason for audit and ticket tracking. |
| Whether to enforce kernel iteration alignment with source instance master replica | Controls the minor engine version on the destination host: Yes (forced alignment): The destination host must have the same minor engine version as the source instance. If the version is unavailable, the migration fails. We recommend that you check whether the minor engine version of the destination host is ready in advance. No (intelligent adaptation): The system preferentially attempts to match the source version. If the version is unavailable, the latest valid minor engine version on the destination host is automatically used. Note If the migrated instance is a read-only instance, the source instance of the read-only instance is the corresponding primary instance. |
| Specify host | Specify a destination host: If you manually specify a physical host to migrate to, the success rate decreases. Do not specify a destination host (recommended): If you do not specify a destination host, the resource manager automatically allocates the optimal host. The success rate is high. Note Click Troubleshooting host reasons in the Description section to view why certain physical hosts are not available. |

**View the migration task progress**

After you click **Submit**, you are redirected to the **Task Management > Migration tasks** page. You can view the migration progress on this page.

**View host information before and after migration**

Go to the **Basic information** page of the instance. In the **Host instance information** section, view the host ID before and after the migration.

##### 2.3.3.6 Upgrade the minor version

ApsaraDB Operations and Maintenance System supports secure and controllable minor version upgrades for database instances. This type of upgrade usually includes performance optimization, introduction of new features, and fixes for known issues, helping ensure stable and efficient operation of databases.

**Prerequisites**

The instance for which you want to upgrade the minor version must be a non-temporary instance and must be in both In Use and Unlocked states.

**Usage notes**

If you do not specify the target version number, the system upgrades the instance to the latest minor version in the series by default. When you update the minor engine version of your PolarDB for MySQL V2.0 cluster, applications may temporarily disconnect from your cluster for 30 seconds. We recommend that you update the minor engine version during off-peak hours or make sure that your application is configured to automatically reconnect to the cluster. Once the minor version is upgraded, you cannot downgrade the version to an earlier version. Exercise caution when you perform this operation.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Locate the required instance in the instance list and click the corresponding **User instance**
**name** to go to the Instance details page.
4. In the lower part of the **Basic Information** page, click **Version Upgrade**, configure the
following parameters, and then click **Submit**.

> **Note:** This document uses the minor version upgrade of PolarDB for MySQL Primary/Secondary Edition as an example. Configuration items and interface display may vary by database type. The actual displayed items are subject to the console configuration.

| Configuratio n item | Description |
|---|---|
| Database version | Displays the major version of the current instance. The system only supports minor version upgrades within the same major version. |

| Small version number | Select the minor version to upgrade to. The current minor version of the instance will appear on the right for comparison. |
|---|---|
| Specify method | Operation and maintenance time switching: The upgrade is performed during the pre-configured maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic Information page of the instance. Switch now: The upgrade immediately takes effect and may affect your business. Specified time switch: You can create a custom time for the upgrade, which requires manual configuration. |

**View the upgrade progress**

After the upgrade task is initiated, you can go to the **Task Management** page to view the upgrade progress.

##### 2.3.3.7 Manage instance parameters

ApsaraDB Operations and Maintenance System supports manual configuration of instance kernel parameters and viewing of the managed parameters, which can be used for information query or fault troubleshooting scenarios.

> **Note:** The instance parameter management capabilities vary by database engine. The actual displayed capabilities are subject to the console configuration.

**Kernel – instance parameters**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance to go to the **Basic Information** page.

> **Note:** You can enter a keyword in the search box to quickly query the required instance. You can also click Advance search to customize filter conditions to locate the required instance.

4. In the left-side navigation pane, click**Kernel-instance parameters**. The capabilities
supported under different tabs on this page are as follows: .

> **Important:** If the new parameter settings take effect only after you restart the instance, we recommend that you restart the instance during off-peak hours and make sure that your application is configured to automatically reconnect to the instance.

| Category | Description | Modifiable | Instance restart required to take effect |
|---|---|---|---|
| Read-only parameters | Parameters that cannot be modified. Read-only parameters may vary across different versions and deployment modes. | No | N/A |
| Read/write parameters (The database will not be restarted) | Parameters that can be modified, subject to value range validation. The value range displayed on the console shall prevail. | Yes | No |
| Read/write parameters (Automatically restarts the database) | Parameters that can be modified, subject to value range validation. The value range displayed on the console shall prevail. | Yes | Yes |
| Parameters being synchronized | Historical parameter records that are being delivered or have not fully taken effect. Parameters in this state are not applied to the current instance. | N/A | N/A |
| Parameter modification history | Query of parameter modification records. | N/A | N/A |

**Management-instance parameters**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance to go to the **Basic Information** page.

> **Note:** You can enter a keyword in the search box to quickly query the required instance. You can also click Advance search to customize filter conditions to locate the required instance.

4. In the left-side navigation pane, click **Management-instance parameters**.
On the **Management-instance parameters** page, you can view the parameters, including **Parameter name**, **Parameter value**, and **Modify**.

##### 2.3.3.8 Change specifications

This topic describes how to change specifications and helps you resolve related issues.

**Preparations**

Before performing a specification change, ensure that you complete the following checks: Instance status verification: Ensure that the instance is in the Running status and no other tasks (such as backup, migration, and restart) are in progress. Data backup recommendation: We recommend that you manually create a temporary snapshot or full backup before the operation to quickly restore data in case of exceptions.

**Usage notes**

| Operate only during off-peak hours. | A transient connection interruption lasting 5 to 30 |
|---|---|
| seconds may occur during the change. Ensure that the application has an automatic |   |
| reconnection mechanism to avoid business errors. |   |

We recommend that you maintain the default option of force alignment of minor engine versions to prevent compatibility issues caused by inconsistent node versions within the cluster. If the target specification is unavailable, you must click to check specific exclusion reasons and avoid blind attempts. After the change, you need to monitor the task progress in real time until completion. If the task is interrupted or stalls for an extended period, you need to immediately contact Alibaba Cloud technical support. Strictly implement the review process and carefully check the CPU, memory, and disk values before and after the change to prevent resource waste or service degradation due to misoperations.

**Scenarios**

Performance expansion: Respond to business growth or traffic bursts, and resolve issues such as slow response and long queues caused by CPU/memory bottlenecks. Cost optimization: Release idle resources for low-load or non-core environments by downgrading specifications to reduce O&M costs. Storage expansion: When the disk usage reaches the threshold, the storage space is urgently expanded to prevent write locks or service interruptions. Version management: Use the specification change mechanism to forcibly align minor engine versions to eliminate compatibility and stability risks caused by inconsistent node versions in a cluster. Fault recovery: After an instance is migrated or a high-availability switchover is performed, the target node specifications are modified to restore the standard configuration or unify the cluster architecture.
1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the lower part of the Basic information page, click **Specification change**.
4. On the page that appears, specify **Storage space (GB)**, **Instance specifications**,
**Switch Mode**, and **Reason for change**. Then, click **Next step**.
Forced alignment of minor engine versions during migration: Yes: The system enforces that no other minor engine version may be used on the target host. If the target host does not have a minor engine version consistent with those of the primary and replica nodes, the specification change will fail. We recommend that you manually install the required minor engine version on the target host in advance by referring to the O&M manual of ApsaraDB Operations and Maintenance System. For more information about how to update the minor engine version, see Update the minor engine version. No: The system preferentially uses the minor engine version consistent with those of the primary and replica nodes of the instance on the target host. If the target host does not have such a minor engine version, the latest valid minor engine version available on the target host will be used instead.
5. In the **Audit comments** section, confirm the comments and click **Audit changes**.
6. After the operation, you can view the task progress on the **Task Management** page until
the task is completed. If the task is interrupted, contact Alibaba Cloud technical support. For more information about how to view the task progress, see Manage instance tasks.

##### 2.3.3.9 Change storage capacity

This topic describes how to modify the storage capacity of an instance to help you resolve issues efficiently.

**Usage notes**

The primary instance is in the Running status and has no pending modification tasks, such as upgrades, migrations, and backups. We recommend that you perform this operation during off-peak hours to avoid the risk of extreme network fluctuations. The storage capacity after scale-down cannot be less than the total used storage space of the instance plus 20 GiB. The change takes effect on the logical instances of the cluster. If you modify the storage specifications of the primary instance, the changed specifications are applied to all readonly and secondary nodes in the cluster. Proceed with caution.

**Scenarios and common issues**

**Storage upgrade (scale-up)**

Support business growth: When business data grows rapidly, and the disk usage approaches the threshold (such as 80%), emergency scale-up is required to prevent the database from entering the read-only status or service interruption due to full storage. Reserved buffer space: Scale up storage in advance to reserve sufficient write buffer space before large-scale promotions, batch data import, or historical data archiving. Remove performance limits: In specific scenarios, a larger storage quota may be associated with a higher IOPS limit (depending on the specific instance specification policies) to improve the throughput.

**Storage downgrade (scale-down)**

Cost optimization: After business data is deleted, such as large tables, and historical data is archived, the actual usage is much lower than the current quota. Downgrading the configuration releases idle resources and immediately reduces the monthly bill. Fix over-provisioning: Rectify the resource waste caused by inaccurate estimations in the initial project stage, and adjust the storage to align with actual business needs.
1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the lower part of the Basic information page, click **Storage space changes**.
4. In the dialog box that appears, enter the new storage capacity and click **Confirm**.

**View task details**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Task Management > Instance tasks** page, you can view the task status.

> **Note:** You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks.
> You can customize list items. You can select the task fields that you want to view based on your needs.

##### 2.3.3.10 Perform an HA switchover

This topic describes how to manually perform an HA switchover and helps you efficiently resolve related issues.

**Background information**

In most cases, when the primary node fails, the system automatically performs an HA switchover to restore services. Manual HA switchover is usually performed in active O&M scenarios, that is, manually transferring traffic from the current primary node to the secondary node without waiting for a fault to occur, promoting the original secondary node to the new primary node.

**Preparations**

Before you perform an HA switchover, ensure that the following items are checked: Instance status check: Ensure that the instance is in the Running status and no other operations (such as specification modification, restart, or backup and recovery) are being performed. Primary/secondary synchronization status: Ensure that data synchronization on the secondary node is normal. Ensure that the latency is 0 or within the allowable range. The recommended value is less than one second. If the synchronization of the secondary node is delayed, a forced switchover may cause data loss. Secondary node health check: Ensure that the host where the secondary node is located has sufficient resources, network connectivity is normal, and no hardware alerts are generated.

**Usage notes**

We recommend that you perform this operation during off-peak hours and ensure that a complete automatic reconnection mechanism is in place to avoid the risk of extreme network fluctuations. After the switchover, you need to monitor the task progress in real time until completion. If the task is interrupted or stalls for an extended period, you need to immediately contact Alibaba Cloud technical support. We recommend that you wait until the data synchronization between the primary and secondary data is complete before you perform the switchover.

**Scenarios**

Maintenance/upgrade of underlying resources: When the physical machines, hosts, or storage devices of the primary node need to be stopped for maintenance, firmware upgrade, or migration, manually switch services to the secondary node first to avoid service interruption. Troubleshooting: If the primary node experiences hardware issues or network jitters, but is not completely down, the system switches services to a healthy secondary node to avoid risks.
1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the lower part of the Basic information page, click **HA swtich**.
4. After you confirm that the primary/secondary information is correct, specify the **Switching**
**method** and **Specify method** parameters, and click Submit.

> **Note:** Switch now: This method is used for emergency avoidance.
> Operation and maintenance time switching: This method is suitable for routine O&M windows, such as early morning every day. The O&M task is automatically executed.
> Specified time switch: This method is suitable for specific change windows, such as application release.

5. After the operation, you can view the task progress on the **Task Management** page until
the task is completed. If the task is interrupted, contact Alibaba Cloud technical support. For more information about how to view task progress, see Manage instance tasks.

**Verify results**

After Step 4, the IP addresses and port numbers are reassigned to match the new primary and secondary roles. The HA task flow is completed normally.

**Rollback**

Repeat the procedure to swap the primary and secondary nodes.

##### 2.3.3.11 Lock an instance

This topic describes how to lock an instance to help you resolve issues.

**Usage notes**

Ensure that operations are performed during off-peak hours and your applications have an automatic reconnection mechanism to handle potential disruptions. For disk-full locks, you must first clear or expand the disk space. For rollback locks, forced restarts are strictly prohibited, and the root cause (such as high resource usage or failed changes) must be resolved before you attempt unlocking. After a task is submitted, continuous monitoring of the progress is required. If the task is interrupted or becomes unresponsive, retries without investigating the root cause are prohibited. You should immediately contact Alibaba Cloud technical support to prevent deadlock. After an instance is locked, it becomes read-only and affects your business. You must perform this operation within an O&M window and proceed with caution regarding execution risks.

**Applicable scenarios**

This topic lists only some applicable scenarios for reference. For situations not covered here, adapt your approach based on actual requirements. Cooling-off period verification for business unpublishing: Prior to instance deletion, manually lock the instance and enforce an observation period of at least 7 days. Proceed with permanent deletion only after you confirm no hidden dependencies or user complaints, which helps prevent accidental loss of production data. Emergency fault isolation and damage control: In the event of malicious attacks, abnormal SQL consumption, or data tampering, manually lock the instance immediately to cut off all connections. This prevents the spread of faults and buys time for troubleshooting. Resource exhaustion self-protection: When disk capacity is exhausted or hardware fails, the system automatically triggers a disk-full lock or migration lock. This prevents metadata corruption and ensures strong data consistency. Rollback protection for high-risk changes: When a specification change or upgrade fails, the system automatically triggers a rollback lock to freeze the instance status to prevent data from being inconsistent in the intermediate state.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. On the Basic information page, click **Locking an instance** in the lower part of the page.
4. Specify **Lock mode** and **Locking reason**, and then click **Submit**.
5. View the task progress on the **Task Management** page until the task is complete. If the
task is interrupted, contact Alibaba Cloud technical support. For more information about how to view the task progress, see Manage instance tasks.

##### 2.3.3.12 Backup and restoration

ApsaraDB Operations and Maintenance System supports automatic policy configuration, manual temporary backup, and multi-dimensional restoration (by backup set and by point in time). Through full, incremental, and log backup mechanisms, the platform can meet strict RPO (Recovery Point Objective) and RTO (Recovery Time Objective) requirements against user errors, hardware failures, and logical corruptions.

**Usage notes**

Download limits: You cannot directly download backup set files in the console. If you want to archive data offline or restore data locally, log on to the Apsara Uni-manager Management Console and download the data. Restoration duration: The time required for data restoration is affected by multiple factors, including instance specifications, data volume, network bandwidth, and cluster load.

**Purpose of log backups**

Enabling log backup determines the granularity of data restoration.

| Configuratio n status | Recovery ability | Scenario |
|---|---|---|
| Log backup is disabled. | Only data restoration by backup set is supported. Data can only be rolled back to the completion time of the latest full or incremental backup. | Scenarios with low requirements for data consistency or where a small amount of data loss is acceptable. |
| Log backup is enabled. | Point-in-time recovery (PITR) is supported. Data can be accurately restored to any second within the log retention period. | Core production business scenarios that need to handle fine-grained operational errors such as accidental table deletion or incorrect updates. |

**Manage backup policies**

**View the backup policy**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup policy**. On the page that appears, view the
data backup policy and log backup policy.

**Modify a data backup policy**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup policy**. Click **Modify a backup policy**, read
the warning, and then click **Confirm**.
5. In the dialog box that appears, modify the parameters that are described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| Backup retention days | Specify the retention period of the backup set. The default value is 7, which is set as needed (such as 30 days). Backups are automatically deleted upon expiration. |
| Backup level | Select from General, Zhongzhong, and High based on your business requirements. |
| Backup time | Modify the value as needed. We recommend that you modify the value during off-peak hours, such as 06:00. |
| Backup cycle | Select specific days of the week. Perform at least two backups per week for data security. |
| Backup does not fall | Close Only data does not fall to the ground |
| Backup compression | Specify the backup compression mode based on your business requirements. |
| Compression parallelism | Specify the number of concurrent threads for the backup process based on your business requirements. |

**Modify a binary log backup policy**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup policy**. In the lower part of the page, click
**ModifyBINLOGBackup policy**.
5. In the dialog box that appears, modify the parameters that are described in the following
table and click **Submit**.

| Parameter | Description |
|---|---|
| Upload method | Do not Upload Upload Second-level upload |

| Local cleaning method | Do not clean Clean up |
|---|---|
| Upload Compression | Select No compression , zlib compression , or lz4 Compression . Enabling compression can save bandwidth and remote storage, but may increase the local CPU overhead. |
| Log backup | Close: If you disable this feature, all log backup files are deleted and you cannot restore the data of the cluster to the specified point in time. Open and charge: The log backup feature is enabled. |
| Retention days of remote storage | Configure the retention period for logs in remote storage. Logs whose retention period exceeds this period are automatically deleted. |
| Local retention period | Configure the maximum retention period for logs. If the binary log files whose retention period exceeds the specified retention period are backed up by using the log backup feature, the system automatically deletes the binary log files. |
| Local retention space | Monitor the percentage of the total disk space used by the local binary log directory. |
| Locally Retained Binlogs | The maximum number of binary log files that can be retained. If the number of retained binary log files exceeds the maximum number, the system automatically deletes earlier binary log files until the number is less than the maximum number. |
| Critical Alert Threshold for Disk Space | If the space occupied by local binary logs exceeds this threshold, a critical alert is triggered. |
| Clean up when disk is too high | Open: When disk space becomes critically low, the system automatically deletes older logs to maintain stable operation, which may prevent recovery to earlier points in time. Close: If the disk is full, the instance may be suspended. |

|   |   | No compression |
|---|---|---|
|   | Compression |   |

**Reload a binary log backup policy**

When the modified policy is synchronized to the underlying agent, you can manually trigger a reload.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup policy**. In the lower part of the page, click
**Reload Backup strategy of binlog**, and then click **Confirm**.

**Clean up binary logs**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **BINLOG management**. On the **Binlog backup**
**policy** tab, click **Clear logs** in the upper-right corner.

**Create a temporary backup**

> **Important:** The temporary backup is valid for only 18 hours. If the temporary backup expires, you need to re-initiate it.

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup policy**. Click **Create a temporary backup**.
Read the alert and click **Confirm**.
5. In the dialog box that appears, modify the parameters that are described in the following
table and click **Confirm**.

| Parameter | Description |
|---|---|
| Backup type | AUTO: determined by the system. FULL: full backup |
| Backup method | Backup physical backup Primary physical backup |
| Backup time | Precise to the minute. |

**Data restoration**

**Restore data from a backup set**

This section describes how to restore the instance data to a point in time when a backup set is completed.

> **Important:** The instance must have at least one successful and valid backup set before a restoration is performed. You can check the validity of a backup set in the **Valid** column of the backup list. Invalid or corrupted backup sets cannot be used for restoration. If no backup set is available, create a temporary backup.

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup Recovery**. Find the backup set that you
want to restore and click **Restore by backup set** in the Operation One column.
5. On the page that appears, configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Reserved instance | Select whether to retain the current instance as needed. If you want to restore data of a dedicated instance, you can determine whether to retain or replace the current instance. If you determine to replace the current instance, the data of the current instance will be restored in overwrite mode. If you retain the current instance, the data of the current instance is not affected. The system will generate a child instance to restore the required backup data. By default, the child instance is retained for two days and is automatically deleted upon expiration. If you replace the current instance, the data of the current instance is lost. The instance will be rolled back to the desired backup data state. |
| Cross-cluster allocation | Select whether to enable cross-cluster allocation as needed. When no resources are available in the current cluster, resources can be requested from other clusters within the same data center. Note that if you use a virtual IP address (VIP) to access the instance, you may need to re-bind or modify the VIP configuration after restoration. |
| Network Type (Private network/Public network) | Select the network type as needed. |

**Restore data to a point in time**

**Important**

To restore data to a point in time, make sure that:

> Log backup is enabled.
> A valid full backup set exists, and no overlaying restoration has occurred between two full backups.
> The target point in time is within the log retention period.

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **Backup Recovery**. In the upper part of the page,
click **Restore to point in time** .
5. In the message that appears, read the warning and click **Confirm**.
6. In the dialog box that appears, configure the following parameters. Then, click **Submitted**.

| Parameter | Description |
|---|---|
| Recovery time | Precise to the second. |
| Cross-cluster allocation | Select whether to enable cross-cluster allocation as needed. When no resources are available in the current cluster, resources can be requested from other clusters within the same data center. Note that if you use a virtual IP address (VIP) to access the instance, you may need to re-bind or modify the VIP configuration after restoration. |
| Network Type (Private network/Public network) | Select a network type as needed. |

**View the backup policy**

**Data backup history**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the left-side navigation pane on the **Instance details** page, click **Backup Recovery**. On
the page that appears, view the data backup policy.

**Binary log backup history**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Find the required instance and click its name in the **User instance name** column.
4. In the **Instance details** section, click **BINLOG management**. On the **Backup history**
tab, view the backup history of binary logs.

##### 2.3.3.13 Recreate a secondary database

If an exception occurs in the secondary database, you can recreate a secondary database to ensure the continuity of the primary/secondary high-availability architecture.

**Scenarios**

You must recreate a secondary database in the following conditions: The secondary database fails and cannot provide services. The data in the secondary database is damaged, which leads to data inconsistency between the primary and secondary databases or synchronization interruption. You need to replace the server where the secondary database resides due to reasons such as hardware upgrades, migration, and resource adjustment.

**Usage notes**

Secondary database recreation has no impact on the operations of the primary database or online services. If you want to recreate the secondary database because of an inconsistency between the primary and secondary databases, you must **trigger a backup of the primary database** first to prevent the secondary database from becoming invalid. We recommend that the primary database be backed up during off-peak hours. You can choose **Instance details** **>**
**Backup policy** and then click **Create a temporary backup** to create a temporary
backup. For more information, see Backup and restoration.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. On the Instance List page, find the instance that you want to manage and click its name to
go to the **Basic information** page.

> **Note:** You can enter a keyword in the search box to quickly find the desired instance. You can also click Advance search to specify filter conditions for an exact search.

4. In the lower part of the page, click **Reroute [standby database reroute | Node**
**reroute]**.
5. In the dialog box that appears, follow the instructions to complete the required settings.
The following table describes the related parameters. The parameters displayed in the console shall prevail.

| Parameter | Description |
|---|---|
| Whether to force primary database backup | By default, this option is not selected. You can choose whether to require that the task flow initiate the backup operation from the physical host where the primary database is located (not the physical host where the secondary database is located). That is, the backup set must be generated by the primary database. Note If the secondary database or its host experiences performance exception or access exception, we recommend that you select Whether to force primary database backup. This prevents initiating backups from the secondary database, which can cause the task flow to interrupt or fail. |
| Select the host that needs to be re-built | Select the host. Ensure that the Instance role of the selected host is a secondary database, such as slave . |

| Whether to enforce alignment of the kernel iteration with the instance master replica | If this option appears, select it based on your business requirements. Note If you select Yes, the system will enforce the use of a specific minor version on the destination host. If the destination host lacks the minor engine version that matches the primary database of the instance, the recreation will fail. We recommend that you install the required minor engine version on the destination host in advance by referring to Update the minor version. If you select No, the system preferentially uses the minor engine version that matches the primary database of the instance on the destination host. If this specific version is unavailable on the destination host, the latest valid minor version available on the destination host is used. |
|---|---|
| Select Locally Recreate Node or Cross-machine rematch. | If the cluster has sufficient available resources, we recommend that you select Cross-machine rematch. If the operating system or file system of the physical host where the secondary database is located is abnormal, you must select Cross-machine rematch. Important In this case, before you initiate a secondary database recreation, you must shut down the secondary database or power off the faulty host. This prevents system environment exceptions on the secondary database from interfering with the normal execution of task flow steps, which could otherwise cause an unavoidable task interruption. If the cluster mode of the selected host is Host Pair, you must select Locally Recreate Node. |

| Specify host | If you select Cross-machine rematch in the previous step, you can specify a data center or host. Note In most cases, you do not need to specify a host, and migration is scheduled by the resource manager. For more information, see the supplementary description in the blue box in the console. Click Troubleshooting host reasons to view the reasons why a physical host is excluded from the list of available hosts. |
|---|---|

6. After the configuration is complete, click **Submit**.
7. After the operation, you can view the task progress on the **Task Management** page until
the task is completed. If the task is interrupted, contact Alibaba Cloud technical support. For more information about how to view task progress, see Manage instance tasks.

##### 2.3.3.14 Manage instance tasks

This topic describes how to view the progress and details of a task.

**View task details**

> **Note:** You can view the task details of an instance in one of the following ways based on the database storage type:
> Pengine instance tasks: local disk storage architecture.
> GrandCanal task list: shared storage architecture.

**Method 1: View the task details of a Pengine instance**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. In the left-side navigation pane of the instance details page, click **Task list**. On the Task list
page, you can view the status of task execution.
4. In the drop-down list at the top of the page, select a task status, such as **Interrupted**
**tasks** or **Running tasks**.
5. Optional. Click the quick filter buttons (**I executed**, **I created**, and **I am responsible**) or
enter an instance name to filter instances.
6. On the task list page, find the task that you want to manage and click Operation in the
**Operation** column.

**Method 2: View the task details of a GrandCanal instance**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. In the left-side navigation pane of the instance details page, click **Task list**. On the Task list
page, you can view the status of task execution.
4. In the upper part of the page, click a task tab based on your business requirements.
5. Optional. Search for or filter data by fields such as **product code** (such as polardb_mysql
and redis), **target type**, and **workflow ID**.
6. On the task list page, find the task that you want to manage and click **Details** in the
**Operation** column.

> **Note:** You can view the status of various tasks, such as all tasks, interrupted tasks, and suspended tasks.
> You can customize the task fields that you want to view based on your requirements.

##### 2.3.3.15 Disable instance allocation

**Background information**

During the running of existing cloud database clusters that were deployed in the early days, their workloads may accumulate over a long period of time. As a result, key resource metrics of these clusters, such as CPU utilization, memory usage, and number of connections, remain at high levels. If you continue to schedule new instances to these high-load clusters, the uneven distribution of workloads will be exacerbated, which potentially leads to performance bottlenecks.

**Usage notes**

After you perform an operation, you must check the dbaas database for the status of hosts and check the dukang database for the status of scheduled tasks to ensure status synchronization between the control plane and the data plane. Before you disable instance allocation for a high-usage cluster, make sure that the lowusage cluster has sufficient resources. This prevents new instance creation failures or blocked business expansion due to a reduction in available resource pools. When instance allocation is disabled for multiple hosts at a time, a secondary confirmation mechanism or phased execution is required to prevent traffic from being routed to the lowusage cluster due to accidental operations.

**Pre-operation checklist**

| Check item | Standard/Threshold | Verification method |
|---|---|---|
| Target host usage | The CPU utilization, memory usage, or number of connections of the target host is greater than X% of the corresponding threshold. For this percentage, 85% is recommended. | Check the target host usage in the monitoring dashboard or on the Host Details page. |

| Receiving cluster capacity | The remaining resources of the low-usage cluster are sufficient to receive the expected additional traffic. | Check the cluster capacity in the resource report or by using a capacity planning tool. |
|---|---|---|
| Operation execution period | The operation is performed during off-peak hours, and no major change window exists. | Check in the O&M calendar. |
| Status precheck of both databases | The host status of the dbaas database is normal, and the dukang database has no pending tasks that are caused by exceptions. | Execute the following SQL statements for verification. |

**Baseline status check (SQL example)**

You must record the current status before you perform the operation for post-operation comparison.
1. Check the dbaas database for the basic status of hosts.

```
-- Log in to the dbaas database. SELECT id, status, allocatable, cpu_usage, mem_usage FROM hostinfo WHERE id = '<Target host ID>'; -- Expected: The value of the allocatable field must be 1, which indicates that alloc ation is allowed.
```

2. Check the dukang database for the status of scheduled tasks.

```
-- Log in to the dukang database. -- Confirm whether the host has any pending scheduled task. SELECT * FROM scheduler_tasks WHERE host_id = '<Target host ID> 'AND status='pending; -- Expected: No pending scheduled tasks are recorded or the recorded pending schedule d tasks have been processed.
```

1. Log in to ApsaraDB Operations and Maintenance System.
2. You can perform the operation in two modes. Select one of the following modes based on
your business scenario:

**Fine-grained control of a single host**

i. In the left-side navigation pane, choose **Host management > System host**. On the page that appears, find the host that you want to manage and click **Details** in the
**Operation** column to go to the Host details page.
ii. On the Host Information tab of the Host details page, click **Turn off instance allocation** . iii. In the dialog box that appears, specify whether to permanently disable instance allocation.

> **Note:** If you select **No**, you can specify a time to restore instance allocation. If you do not select a time, instance allocation will be restored seven days later by default.
> If you select **Yes**, the system will not automatically restore instance allocation, and you must manually enable instance allocation when needed.

iv. Click **OK**.

**Batch configuration of multiple hosts**

i. In the left-side navigation pane, choose **Host management > System host**. ii. In the host list, select the hosts that you want to manage and click **Batch configuration** in the upper-right corner. iii. In the Batch configuration parameters panel, configure the parameters and click **Submit**.
3. After the configuration is complete, you can check whether the configuration is correct in
the **Allow instance allocation** section of the Host Information tab.

**Rollback operation**

**Scenario 1: Restore instance allocation before the specified**

**restoration time after you temporarily disable this feature**

1. Go to the Host details page and click Turn on instance allocation.
2. Verify that the status of `system_param_record` tasks in the dukang database has changed
to Completed or has been cleared.

**Scenario 2: Enable instance allocation again after you**

**permanently disable this feature**

1. Go to the Host details page and click Turn on instance allocation.
2. Verify that the `allocatable` field in the `hostinfo` table of the dbaas database has
changed to the Allowed state.
3. You must create a test instance to ensure that the node can be re-identified by the
scheduler.

**Scenario 3: Perform emergency restoration after an accidental**

**operation that disables instance allocation for multiple hosts at**

**a time**

1. Stop the subsequent batch tasks immediately.
2. In the host list, select the low-usage hosts for which instance allocation has been
accidentally disabled.
3. Click Batch turn on instance allocation.

#### 2.3.4 Other instance O&M

##### 2.3.4.1 Upgrade an instance from ApsaraDB RDS for MySQL Two-node Edition with Local Disks to PolarDB for MySQL Primary/Secondary Edition

**for MySQL Two-node Edition with Local Disks to**

**PolarDB for MySQL Primary/Secondary Edition**

**Usage notes**

To ensure smooth database migration and business stability, carefully check the following environmental requirements and instance status before you perform the migration.

**Summary of supported scope and limits**

| Category | Check item | Scenarios that are not supported or need to be modified | Suggestion |
|---|---|---|---|
| Operating system (OS) server version | Non-compatible OS versions, such as some old custom OS versions | Servers with 6U OS are not supported. | If an incompatible OS version is deployed on the server, upgrade the server OS to a recommended version first, such as a standard Linux 7U or later distribution. |
| Database engine version | RDS MySQL 5.6 | Direct migration is not supported. | Upgrade the instance engine version to MySQL 5.7 or 8.0 before you perform the migration. |
| Instance architecture | ApsaraDB RDS for MySQL Three-node Edition | Direct migration of the architecture is not supported. | Migrate the instance to PolarDB Converged Edition (Centralized & Distributed) before you perform subsequent operations. |

| Associated instance | Primary instance that has read-only instances | Separate switchover of the primary instance is not supported. | The primary instance and all its associated read-only instances are switched to PolarDB instances at the same time as a group. Separate switchover of the primary instance is not supported. |
|---|---|---|---|

**Instance health and status requirements**

Before you initiate a migration task, make sure that the source ApsaraDB RDS for MySQL instance is in a healthy and idle state. This ensures data consistency and system stability. Normal synchronization status: No synchronization latency exists between the primary and secondary instances used in the synchronization task. That is, the latency is 0. If any read-only instances exist, the synchronization latency between the primary instance and all read-only instances must be 0. Low resource usage: The CPU utilization of the instance is below 75%. The memory usage of the instance is below 75%. No running tasks: The instance is not in backup, restart, specification change, or other O&M processes.

**Other suggestions**

Connection proxy component compatibility: If your business uses a database proxy cluster for connection, we recommend that you switch the connection proxy. to MaxScale before or after the migration for better compatibility and performance. Migration irreversibility: To ensure data consistency and long-term running stability, after you upgrade an ApsaraDB RDS for MySQL instance to a PolarDB for MySQL primary/secondary instance, rollback to the original ApsaraDB RDS for MySQL instance is not supported by default. Please fully evaluate your business requirements before you proceed with the upgrade. Canary release: We strongly recommend that you perform migration drills in a non-production environment, such as test or staging environment. After sufficient verification through business functional tests, performance stress testing, and compatibility tests is complete, you can schedule a formal switchover to the production environment. Trend to unify the kernel version: As the service evolves, the kernel of new and existing ApsaraDB RDS for MySQL instances will be uniformly upgrade to the PolarDB for MySQL kernel to provide better performance and maintenance experience. In routine O&M scenarios such as secondary instance recreation, the system preferentially uses the next-generation kernel technology.

**Business impact**

**Impact on applications**: During the minor kernel version upgrade, a high availability (HA)
switchover between the primary and secondary instances is triggered. Service connections are not interrupted. However, applications may experience second-level interruptions (typically about 10 seconds) during read and write operations to the database.
**Changes to API access**: After the switchover, the product code is updated to PolarDB. For
services that access the instance by calling API operations, such as using third-party monitoring tools or management tools outside the cloud platform, you must update the configurations to PolarDB after the switchover.
**Upstream and downstream ecosystem tools and integrated products** : After the
switchover, related features must continue to run properly on the PolarDB for MySQL primary/secondary instance. Specific configuration information may need to be updated to the format that is supported by PolarDB for MySQL instances. The involved scenarios include but are not limited to: Internal O&M platforms, such as Apsara Uni-manager Operations Console and Cloud Monitor (CMS). Ecosystem tools, such as Data Transmission Service (DTS), Database Backup (DBS), Log Audit, and DataWorks. Zone-disaster recovery and geo-redundancy backup platforms, such as Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) and Apsara Stack Resilience for Backup and Recovery (ASR-BR). For more information about the impact, see the Upgrade risks section of this topic.

**Solution**

**Environment check**

The PolarDB for MySQL Primary/Secondary Edition that involves product-polardb and product-rds is deployed. Required version: 3.18.6. The PolarDB version is 3.18.6. The version of the Apsara Uni-manager Management Console is v3.16.2r-ascm-SP024 or later.

**Pre-preparation**

1. Log in to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose**Platform Operation > Apsara Infrastructure**

**Management > Resource Management > Resource Management > Product &**

**Cluster O&M**. On the Cluster Details page, click **Desired State Configuration**.
3. Configure the PolarDB for MySQL kernel package. For the **kv.conf** and **tag.conf** variables
of the mysql_7u cluster, modify the value of the PolarDB_Mysql parameter to true. Click
**Preview and Submit**.
4. After you modify the cluster variables, the system performs a rolling update. Wait until the
cluster returns to its normal running state.
5. If you can query the PolarDB for MySQL kernel package from the mysql_7u cluster, the
modification is successful. To verify this, log in to the physical machine of the ApsaraDB RDS for MySQL instance and run the following command:

```
rpm -qa |grep polardb
```

image.png
6. A version reference to the PolarDB for MySQL kernel is generated in the metadatabase
named dbaas. Make sure that the RPM package mentioned in Step 3 is written to dbaas. To verify this, log in to dbaas and execute the following SQL statement:

```
select * from minor_version_release where db_type='mysql' order by id desc;
```

7. Check for proper functioning. After the preceding configurations are complete, log in to the
Apsara Uni-manager Management Console and create a PolarDB for MySQL instance. Verify that the backup and restoration, monitoring, and parameter adjustment features of the instance function properly.
8. Log in to the ApsaraDB Operations and Maintenance System console and set
RDS_UPGRADE_TO_POLARDB_WHITE_LIST to false. This operation ensures that the
**Upgrade to PolarDB** button is visible.

**Upgrade to PolarDB**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. On the Instance List page, find the instance that you want to manage and click its name in
the User instance name column.

> **Note:** You can search for the instance by entering keywords in the search box in the upper part of the page. You can also click **Advance search** to filter instances by condition.

4. On the **Basic information** tab, click **Upgrade to PolarDB**.
5. In the **Upgrade to PolarDB** dialog box, click **Submit**. In the message that appears, click
**OK**.
6. After the upgrade is complete, run the following command to verify that the kernel of the
instance (including read-only instances) is a PolarDB kernel. Additionally, no error is reported and the related information about the PolarDB kernel version information can be queried.

```
show polardb_version.
```

7. Log in to the Apsara Uni-manager Management Console, check whether the instance has
been switched to the PolarDB cluster, and view the related instance information.
8. Correct the organization and resource set of the PolarDB for MySQL primary/secondary
instance in the Apsara Uni-manager Management Console. For more information about how to make corrections, see the **Change the ownership of an instance** topic in **Apsara**
**Uni-manager Management Console User Guide**.
Make corrections after all or a batch of ApsaraDB RDS for MySQL instances are upgraded and the normal service is verified. This operation ensures that the organization and resource set of the PolarDB for MySQL primary/secondary instance after the upgrade are the same as those of the ApsaraDB RDS for MySQL instance before the upgrade.
9. Log in to the destination database.

```
use brm;
```

0. Back up the resource table.

```
create table if not exists resource_instance_bak241104 like resource_instance; insert into resource_instance_bak241104 select * from resource_instance;
```

1. Check the data. Check the PolarDB for MySQL primary/secondary instance after the
upgrade for any inconsistent organization and resource set compared with the ApsaraDB RDS for MySQL instance before the upgrade.

```
select a.d_binstance_id,a.organization_id,a.resource_group_id,'rds_instance',b.organization_id .resource_group_id,b.type from resource_instance b join rds_instance a on a.d_binstan ce_id = b.instance_id where b.type = 'polardb_instance' and a.resource_group_id != b. resource_group_id;
```

2. Implement the plan. Adjust the organization and resource set of the ApsaraDB RDS for
MySQL instances before the upgrade and those of the PolarDB for MySQL primary/secondary instances after the upgrade to the same.

```
update resource_instance b join rds_instance a on a.d_binstance_id = b.instance_id se t b.organization_id=a.organization_id, b.resource_group_id=a.resource_group_id where b.type = 'polardb_instance' and a.resource_group_id != b.resource_group_id;
```

**Rollback scenarios**

**Scenario 1:** Roll back a PolarDB for MySQL instance to an ApsaraDB RDS for MySQL instance
due to exceptions.

**Rollback metadata**

The primary instance, read-only instance, and secondary read-only instance of the same instance must be rolled back within the same transaction.

**Rollback SQL statements:**

rds-yaochi.phoenixrds:

```
UPDATE rds_instancesetproduct_code='rds',gmt_modified=now() WHERE instance_id = xxx limit1;
```

rds-maotai.dbaas:

```
DELETE FROM custins_param WHERE custins_id = xxx AND name = "pop_code" AND VALUES = "polardb" limit 1; DELETE FROM custins_param WHERE custins_id = xxx AND name = "upgrade_to_polardb" li mit 1;
```

**Scenario 2:** If a node failure occurs during the version upgrade process, the node and
instance can be recovered by recreating secondary instances in the ApsaraDB Operations and Maintenance System console.

**Upgrade risks**

The following tables describe the impact on related cloud services that are categorized by product line.

**Databases**

| Service | Impact description | Risk |
|---|---|---|
| RDS | Automatic update of kernel versions: The existing MySQL 5.7 and 8.0 kernel versions are automatically upgraded to the latest PolarDB kernel in all instance restoration scenarios. | Low |
| minirds | Automatic update of kernel versions: The existing MySQL 8.0 kernel version is automatically upgraded to the latest PolarDB kernel in all instance restoration scenarios. | Low |
| PolarDB | Automatic enabling of other PolarDB databases: If ApsaraDB RDS for MySQL and PolarDB for Oracle are deployed at the client site, PolarDB for PostgreSQL instances can be created on the PolarDB page after the patch is installed. PolarDB for Oracle instances that are created based on the original ApsaraDB RDS for MySQL instances are not affected. ApsaraDB RDS for MySQL and PolarDB for Oracle: Their kernels are automatically upgraded to the latest versions. Note After you create a PolarDB instance, you cannot directly log in to the instance through Data Management (DMS). You must log in to DMS and add the instance as a PolarDB for MySQL instance for management before you can use the instance. | Low |
| DTS | Existing DTS migration, synchronization, and subscription tasks are not affected. Impact scope: When you create a database or modify the configurations of a database, such as its connection string, account, or password, Virtual Private Cloud (VPC) is not supported, and you can only select Internet as the network type. | Mediu m |
| DMS | Existing databases are not affected. Impact scope: When you create a database or modify the configurations of a database, such as its connection string, account, or password, you must reconfigure DMS. If a PolarDB instance is created, it cannot be managed in PolarDB. Instead, you must add the instance to PolarDB for MySQL for management. To resolve this issue, upgrade the version of DTS to v3.16.2r-dts-hotfeature- SP020. This version is released. | None |

| DBS | The service is affected and needs to be replaced with ASR-BR. Impact scope: Existing DBS backup plans become invalid and you need to specify a new backup policy. PolarDB supports two backup methods: backup in the PolarDB console and backup using the ASR-BR backup platform. We recommend that you use the ASR-BR backup platform to manage the backup data of PolarDB. Backup in the PolarDB console is suitable for simple backup policies. Backup sets are stored in the default space. You cannot change the storage address of backup sets. The ASR-BR console supports local and geo-redundancy backups. You can specify a backup storage address and a variety of backup policies. You need to back up the instance in the console before you perform a switchover. Handling method: 1. Back up the instance in the console. 2. The following is the procedure for backup using the ASR-BR backup platform: i. In the Apsara Uni-manager Management Console, select ASR for Backup and Recovery. ii. Create a backup plan and select PolarDB Local Disk for the Instance Type parameter. iii. Select the database instance to be backed up. iv. Specify a backup policy. | High |
|---|---|---|
| DAS | Not affected. | None |

**Big data**

| Service | Impact description | Risk |
|---|---|---|

| DataWorks | The offline jobs related to existing data sources are not affected. Note Currently, the VPC network type is not supported. To use VPC, a knowledge base must be applied. If no knowledge base is applied, when you create a database or modify the configurations of a database, such as its connection string, account, or password, in a classic network scenario, you cannot access the database from an instance, but need to access the database by using connection strings. You can perform the following operations to modify a connection string: 1. Log in to the DataWorks console and choose Data Aggregation > Data Integration. 2. Select a MySQL database. 3. In the Add MySQL Data Source panel, select Connection String Mode for the Data Source Type parameter. | None |
|---|---|---|
| Blink | Not affected. Access only in connection string mode: normal and not affected. | None |
| Flink | Not affected. Access only in connection string mode: not affected. | None |
| Datahub | Not affected. Existing instances are not affected. Note The database type is still MySQL, the data is synchronized in sub-string mode, and the instance ID and other information remain unchanged. | None |

**Data intelligence**

| Service | Impact description | Risk |
|---|---|---|
| Dataphin | Not affected. Existing data sources are not affected. New data sources can be accessed only in connection string mode: normal and not affected. | None |

| QuickBI | New data sources can be accessed only in connection string mode: normal and not affected. | None |
|---|---|---|
| DataV | Not affected. | None |
| DataQ | Affected. Existing instances are not affected. Others: not supported for other cloud resources. | None |

**Unified cloud management platforms**

| Service | Impact description | Risk |
|---|---|---|
| ASCM | Affected. You need to enable and configure PolarDB quotas for users. | Mediu m |
| ASO | The alert information is not affected, and the resources are still allocated to ApsaraDB RDS. | None |
| CMS | No exception is found for existing alerts. The alerts are still associated with ApsaraDB RDS. Impact scope: When you create a monitoring task, you need to select PolarDB Local Disk and create a rule for the monitoring task based on PolarDB. The monitoring metrics in the rule must be consistent with those for the new ApsaraDB RDS link. image.png | Mediu m |
| ASR (bcmc) | Affected. ASR for Zone-disaster Recovery allows you to add multiple instances that are involved in an application to a protection group for a unified switchover. PolarDB for MySQL instances cannot be added to the protection group. Check whether the project uses the protection group feature of ASR for Zone- disaster Recovery. If the protection group feature is used, the support of hotfeature is required. | Mediu m |

| ASR-DR | Affected. The ASR-DR protection group needs to be reconfigured. | Mediu m |
|---|---|---|
| ASR-BR | Affected. Existing backup tasks are not affected. When you create a backup task, you need to reconfigure a backup policy for the PolarDB instance. | Mediu m |
| AOP | Not affected. | Low |

**Security**

| Service | Impact description | Risk |
|---|---|---|
| SDDP | Not affected. | Low |

**Elastic computing**

| Service | Impact description | Risk |
|---|---|---|
| ESS: Auto Scaling | Affected. Currently, PolarDB is not supported. If you use auto scaling resources for ApsaraDB RDS, we recommend that you do not perform a switchover. | Mediu m |
| ROS | Affected. You need to update the APIs in the Resource Orchestration Service (ROS) auto-scaling scripts to use PolarDB. | Mediu m |

**External systems of the cloud platform**

| Service | Impact description | Risk |
|---|---|---|
| Monitoring service | Affected. If you want to connect to PolarDB, select PolarDB as the service under monitoring. | Mediu m |

| APIs | Affected. External systems must be reconnected to PolarDB. For the PolarDB for MySQL primary/secondary instance, the pop code is _ polardb and the version is 2024-01-30. For the ApsaraDB RDS for MySQL instance, the pop code is rds and the _ version is 2014-08-15. OpenAPI: The PolarDB for MySQL primary/Secondary instance and the ApsaraDB RDS for MySQL instance are consistent. Their API operation names and parameters are the same, and only the pop code and version _ are different | Mediu m |
|---|---|---|

##### 2.3.4.2 Common O&M operations for secondary PolarDB for MySQL nodes

**PolarDB for MySQL nodes**

This topic describes common operations on secondary nodes to help you resolve issues efficiently.

**Usage notes**

We recommend that you perform the operation during off-peak hours, such as 02:00 to 04:00 in the early morning. When you delete a secondary database, you need to confirm that no tasks are running on the logical instance. Ensure the primary node is in service status and has no running or interrupted tasks. The physical instance of the secondary node has no running or interrupted tasks. The specifications of the secondary node must be **no less than** those of the primary node.

**Local reconstruction of secondary nodes**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the sub-instance information section of the Basic Information page, click the name of the
required instance.
4. On the page that appears, click **Rebuild the standby node locally**.
5. In the dialog box that appears, click **OK**.

**Add a secondary database**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. On the Basic information page, click **Add a standby database**.
4. In the dialog box that appears, click **OK**.
It takes about five minutes to add a secondary node. The time consumption varies based on the database loads and the number of databases and tables. The entire process does not affect the database.

**Delete a secondary node**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. On the Basic information page, click **Delete a standby database**.
4. In the dialog box that appears, click **OK**.

> **Note:** If no secondary database exists, this button is unavailable.

**Perform an HA switchover**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. On the page that appear, click **HA switch**.
4. On the HA switch page, select the target node and click **Submit**.

> **Note:** HA switchover allows switching between read-write (RW) nodes and read-only (RO) nodes, as well as between RW nodes and secondary nodes. Switchover between RW nodes and secondary nodes is permitted only if there are no available RO nodes.

**View task details**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Task Management > Instance tasks** page, you can view the task status.

> **Note:** You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks.
> You can customize list items. You can select the task fields that you want to view based on your needs.

##### 2.3.4.3 Perform zone-disaster recovery switchover for PolarDB for PostgreSQL Shared Storage Edition

**for PolarDB for PostgreSQL Shared Storage Edition**

To ensure business continuity, the PolarDB for PostgreSQL cluster that runs Shared Storagebased Cluster Edition provides high-availability switchover in zone-disaster recovery scenarios. You can perform operations such as **switching a read-only node to read/write**
**mode** or **switching a secondary node to read-write mode** through the O&M platform.
This allows you to perform quick recovery after the primary node fails or active disaster recovery drills.

**Switch read-only to read/write**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. On the page that appears, find the required instance and click its name to go to the **Basic**
**information** page.
4. In the lower part of the page, click **Switch from Read-only to Read/Write** and then **OK**.

> **Important:** During switchover, a transient connection interruption may occur once or twice within 30 seconds.

After the switchover is complete, you can view the updated instance architecture in the
**Instance topology** section on the **Basic information** page.

**Switch a secondary node to read/write**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. On the page that appears, find the required instance and click its name to go to the **Basic**
**information** page.
4. In the lower part of the page, click **Switch from Secondary to Read/Write** . In the dialog
box that appears, select **Switch Mode**.
**Strong cut**: performs an immediate switchover. Unsynchronized data may be lost. We
recommend that you use this method only in extreme failure scenarios.
**Eager**: automatically switches after the standby node has fully synchronized with the
primary node. This ensures data consistency. If the read-only node is normal, this method is recommended.
5. Click **OK**.

> **Important:** Switching the standby node to read/write mode will delete and rebuild existing read- only nodes. During this period, the services of the read-only nodes are interrupted. Be aware of this risk and proceed with caution.

After the switchover is complete, you can view the updated instance architecture in the
**Instance topology** section on the **Basic information** page.

##### 2.3.4.4 Query SQL information for PolarDB-X instances

**instances**

This topic describes how to view instance SQL information such as SQL log details (SLS), slow SQL details, SQL injection detection, and primary key statistics. The following example shows how to view SQL log details.

**Scenarios**

**Identify the causes of sudden high load:** Set the time range to 30 minutes before and
after the failure, sort by latency in descending order to find the top 5 most time-consuming SQL statements, and check with the development team for possible optimization.
**Verify the SQL performance after deployment:** Record the execution time of the
benchmark SQL statement before deploying a new version. Compare changes in execution time and the number of returned rows for the same SQL statements after deployment.
1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the left-side navigation pane, click **Instance SQL information**. On the page that
appears, click the **SQLLog details(SLS)** tab.
4. You can query SQL statements by **Date Time**, **Log type**, **Data sorting type**, or
**Keywords**.

> **Note:** Separate keywords with spaces during queries.
> **SQL archive**:
> Export current query results or save them to a historical archive database.
> This method is suitable for regularly backing up important SQL logs for subsequent auditing or review.
> **SQL archive query**:
> Access the query interface for archived historical SQL logs.
> Search for saved SQL records across different time periods.

##### 2.3.4.5 Handle failed PolarDB-X tasks

The data nodes and GMS of the PolarDB-X cluster are independent ApsaraDB RDS for MySQL instances. Therefore, PolarDB-X tasks such as cluster creation, specification modification, upgrade, release, and node addition will all trigger corresponding ApsaraDB RDS for MySQL task flows. If an ApsaraDB RDS for MySQL workflow fails, the corresponding PolarDB-X task also fails. All PolarDB-X task steps are idempotent and support retry. However, some failure scenarios require special handling, such as failures in underlying RDS tasks. This document describes common solutions for failed ApsaraDB RDS for MySQL tasks that affect PolarDB-X operations.

**Failed PolarDB-X creation task**

If a PolarDB-X instance fails to be created and is stuck at the wait_create_xdb_complete step of the create_polardbx_cluster task, the failure typically occurs because PolarDB-X times out while waiting for the creation of its attached storage nodes and GMS nodes to complete. Solution: Check whether the creation tasks of these ApsaraDB RDS for MySQL nodes run properly. Then, you can retry the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide. On the PolarDB-X instance details page, click the corresponding ApsaraDB RDS for MySQL instance. In the left-side navigation pane of the page that appears, click **Task list**. On the page that appears, you can view the task flows of the corresponding storage nodes and GMS nodes.

**Failed PolarDB-X release task**

If the delete_polardbx_cluster task is stuck at drop_storage or drop_meta_db, you can retry it repeatedly. These two steps send requests to release the GMS node and storage nodes, respectively. If the ApsaraDB RDS for MySQL instance is not in the Running state, you need to wait for other ApsaraDB RDS for MySQL tasks to be executed before you retry the task. If the delete_polardbx_cluster task is stuck at wait_drop_storage, the system is waiting for the completion of the release tasks for ApsaraDB RDS for MySQL. You need to verify that the release tasks of these ApsaraDB RDS for MySQL nodes are normal. Then, you can retry the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed PolarDB-X specification modification task**

If the modify_polardbx_cluster task is stuck at modify_storage_srv_class, the system is sending requests to modify the specifications of storage nodes and GMS nodes. If the resources are insufficient, this task fails. You can add cluster resources. If no resources are available, you can skip to the step do_disable_aurora and continue to modify the specifications of compute nodes. If the modify_polardbx_cluster task is stuck at wait_xdb_status_activation, the system is waiting for the completion of specification modification tasks for ApsaraDB RDS for MySQL. You need to verify that the specification modification tasks for ApsaraDB RDS for MySQL are normal. Then, you can retry the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed PolarDB-X kernel version upgrade task**

If the upgrade_polardbx_cluster task is stuck at upgrade_storage_version, the system is sending requests to upgrade the versions of storage nodes and GMS nodes. If the ApsaraDB RDS for MySQL instance is not in the Running state, the task will fail. You can wait for other ApsaraDB RDS for MySQL tasks to complete and then retry this task. If the upgrade_polardbx_cluster task is stuck at wait_xdb_status_activation, the system is waiting for the completion of the upgrade tasks for ApsaraDB RDS for MySQL. You need to verify that the upgrade tasks for ApsaraDB RDS for MySQL are normal. Then, you can retry the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed PolarDB-X node addition task**

If the add_node_polardbx_cluster task is stuck at wait_new_storage_activation, the system is waiting for the completion of new storage node creation tasks. You need to verify that the creation tasks of these ApsaraDB RDS for MySQL nodes are normal. Then, you can retry the task by referring to ApsaraDB RDS for MySQL Operations and Maintenance Guide.

**Failed PolarDB-X backup task**

If the task is stuck at wait_backup_job_finished, the system is waiting for the completion of the backup task on new storage nodes. If the task is stuck at additional_backup_set_info, the system is retrieving information about ApsaraDB RDS for MySQL backup sets, such as backup set size. This step fails because the task is completed when wait_backup_job_finished is displayed, but the backup set is unavailable. In this case, you also need to check the execution status of the backup task on storage nodes. On the Instance details page of each data node, click **Backup Recovery** in the left-side navigation pane to view the status of the backup task.

##### 2.3.4.6 Change PolarDB-X data node specifications

This topic describes how to change data node specifications and helps you resolve related issues.

**Usage notes**

After you change the data node specifications, the specifications of data nodes in the PolarDB- X instance become inconsistent. As a result, the instance operation methods change as follows: You cannot directly upgrade or downgrade a PolarDB-X instance. To upgrade or downgrade a PolarDB-X instance, you need to upgrade or downgrade the computing nodes and data nodes in the instance separately. You cannot scale in a PolarDB-X instance by changing the number of data nodes. To scale in a PolarDB-X instance, you need to delete the specified data nodes on the Data Node Management page.
1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Specification change**.
4. On the page that appears, specify **Storage space (GB)**, **Instance specifications**,
**Switch Mode**, and **Reason for change**. Then, click **Next step**.
5. In the **Audit comments** section, confirm the comments and click **Confirm correct**
**submit for approval**.

**View task details**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Task Management > Instance tasks** page, you can view the task status.

> **Note:** You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks.
> You can customize list items. You can select the task fields that you want to view based on your needs.

##### 2.3.4.7 Configure PolarDB-X instance resources

You can configure IOPS, CPU specifications, and disk space for instances. This topic uses IOPS configuration as an example to describe the detailed procedure and help you resolve issues quickly.

**Usage notes**

Do not arbitrarily increase the IOPS. This may overload the underlying storage, causing latency or even downtime. If you modify a logic instance, the IOPS configurations of the DN nodes are modified accordingly. You can also modify the IOPS configurations of each node separately. Configure a proper restoration time to avoid resource waste or security risks caused by forgotten restorations. Configure CPU specifications appropriately. An excessively low specification may result in slow SQL execution, connection timeouts, and transaction backlogs. After adjusting disk space settings, immediately perform actual capacity expansion or data cleanup, and restore the limits at an appropriate time. If you do not check the disk space, the disk space of the host may be exhausted. Proceed with caution.

**Scenarios**

Temporarily increase the upper limit of IOPS to ensure business continuity and prevent full disk I/O caused by a sudden burst of a large number of writes. Temporarily reduce the IOPS for throttling protection to prevent disk overload caused by malicious programs or abnormal SQL statements. Isolate problematic instances during troubleshooting and lower CPU quotas to check whether cluster pressure is relieved. Temporarily expand the disk quota when disk usage exceeds 95% to keep businesses running while arranging capacity expansion.
1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the left-side navigation pane, click **Configure an instance**. On the page that appears,
click the **Instance resource configuration** tab.
4. In the **Set IOSP** section, specify **IOPS** and **Recovery time**, and then click **Submit**.
5. In the message that appears, click **OK**.

> **Note:** After the configured restoration time expires, the IOPS value is restored within 5 minutes.

##### 2.3.4.8 Add proxy nodes to a Tair (Redis OSS-compatible) instance

**compatible) instance**

When business traffic increases or the load on existing proxy nodes becomes excessively high (for example, when CPU, memory, or network bandwidth reaches the threshold), you can scale out horizontally by increasing the number of Proxy nodes. This effectively distributes client request pressure, and improves overall system throughput and high availability.
1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Add Proxy Instance Node**.
4. In the dialog box that appears, enter the number of nodes and click **Submit**.

##### 2.3.4.9 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance

**primary/secondary synchronization buffer for a**

**Tair (Redis OSS-compatible) instance**

In high write-load scenarios, the latency of primary/secondary synchronization increases, causing data lag in the secondary database. This affects read consistency and failover reliability. In this case, you can increase the primary/secondary synchronization buffer to improve the primary/secondary synchronization throughput and reduce latency. This topic describes how to temporarily increase the primary/secondary synchronization buffer.

**Usage notes**

The value is automatically reset to the default after the instance restarts. Ensure that sufficient memory is available on the host before the change. We recommend that you perform the operation during off-peak hours, such as 02:00 to 04:00.
1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Temporarily scale-up the primary-**
**standby synchronization buffer**.
4. In the dialog box that appears, enter the target scaling ratio and click **Submit**.

> **Note:** The scaling ratio ranges from 1.0 to 5.0.
> This operation applies to normal, db, and logic instances. When performed on a logic instance, the operation takes effect on all underlying db instances.

normal instance: Also known as a Redis-Normal instance. A standard Redis instance in single-node or primary-replica architecture. db instance: a subinstance that acts as the data node in the Redis-Logic cluster architecture. It refers to the DB-role subinstance that physically stores data in the Cluster Edition. logic instance: a Redis-Logic cluster instance that has multiple roles of Proxy, CS, and DB. It is a clustered deployment that supports read/write splitting and shard routing.

#### 2.3.5 Manage instances in batches

##### 2.3.5.1 Migrate multiple instances at a time

This topic describes how to migrate multiple instances at a time.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management** to go to
the **Instance batch operations** page.
4. On the page that appears, click **Batch instance migration** in the **Instance batch**
**operations** section.
5. On the **Batch instance migration waiting list** tab, click **Download template file** and
then fill in the template file.
6. Click **Select File**.
7. Select the completed template file and then click **Submit**.

> **Note:** Instances that use HAProxy do not experience service interruptions only if migrated within the same cluster.
> Batch instance migration operations are not reviewed. Proceed with caution.

**References**

You can click **Batch instance migration success list** or **Batch instance migration**
**failure list** in the upper part of the **Batch instance migration** page to view the details of
the migrated instances.

##### 2.3.5.2 Modify multiple instance parameters at a time

**time**

This topic describes how to modify multiple instance parameters at a time.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch instance parameter refresh** in the **Instance**
**batch operations** section.
5. Select the clusters for which you want to modify the parameters and click **Select**
**parameter Template**.

> **Important:** Instance parameter changes may cause risks such as transient connections or unavailability. You can modify the parameters by following the instructions on the console.

6. On the page that appears, select the parameter template and click **Next Step**
7. Select the instances and click **Submit**.

**References**

You can click **Batch refresh parameter instance successful list** or **Batch refresh**
**parameter instance failure list** in the upper part of the **Batch instance parameter**
**refresh** page to view the details of the modified parameters.

##### 2.3.5.3 Modify DIY parameters for multiple instances at a time

**instances at a time**

This topic describes how to modify DIY parameters for multiple instances at a time.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch DIY parameter refresh** in the **Instance batch operations** section.
5. On the **BatchDIYRefresh parameter wait list** page, configure the parameters described
in the following table.

| Parameter | Description |
|---|---|
| Instance name | Enter the names of the instances for which you want to modify DIY parameters in the text box. Note Ensure that all entered instances are of the same database type and version. Do not enter spaces, tabs, or blank lines. Only parameters that can be applied without restarting the instance are supported. |
| dbType | The database type. Select the database type of the specified instances. |
| dbVersion | The version of the database engine. Select the database engine version of the specified instances. |
| Remarks | Enter remarks. |

6. After configuration, click **To select parameters**.
7. In the **Confirm** dialog box, click **Confirm**.
8. Select the parameters that you want to modify and enter the new values in the far-right
column.
9. In the lower-left corner of the page, click **Save**.

**References**

You can click **BatchDIYRefresh parameter successful list** or **BatchDIYRefresh**
**parameter failure list** in the upper part of the **Batch DIY parameter refresh** page to view
the details of the modified DIY parameters.

##### 2.3.5.4 Modify Redis parameters for multiple clusters at a time

**clusters at a time**

This topic describes how to modify multiple Redis parameters at a time.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch Redis parameter refresh** in the **Instance batch operations** section.
5. In the **redis2.8Cluster** list, select the clusters for which you want to modify parameters.
6. In the list in the lower part of the page, find the parameter that you want to modify, enter a
value in the **Set value** column, and then click **Save**.
7. In the **Modify configuration** message, click **Determine**.

##### 2.3.5.5 Manage tasks in batches

This topic describes how to manage tasks in batches.

**Create a task**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch task management** in the **Instance batch operations** section.
5. In the upper part of the Batch task management page, click **Create task**.
6. In the **Create task** dialog box, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Task type | Select the type of task to be performed based on your requirements. For example, you can perform batch enabling of SQL Wall, batch link switchover, and batch minor engine version update of instances. |
| Task tips | The system displays the corresponding precautions for different task types. |
| Task parameters | Specify the parameters for the selected task type. Select values based on the actual task. |

| Time rules | Execute immediately: immediately executes the task. Operation and maintenance time: executes the task during the maintenance window. Specify time: executes the tasks within a specified time period. |
|---|---|
| Send SMS | Specify whether to send SMS notifications. Valid values: Yes No |
| Instance source | Specify the source of instances. Valid values: Cluster and SqlTemplate. |
| Please select a source cluster | This parameter is available only when the Instance source parameter is set to Cluster. Select a source cluster to populate the instance name. |
| SelectSqlTemplat e | This parameter is available only when the Instance source parameter is set to SqlTemplate. Select an SQL template to populate the instance name. Note You can click Create Template to the right of the parameter to create SQL templates on the SQL Template management page. |
| Input instance | Specify the instances on which the batch task runs. Enter one instance name per line. |
| Remarks | Enter the remarks. Note This parameter is optional. |

7. Click **Submit**.

##### 2.3.5.6 Manage batch task types

This topic describes how to create a type of batch tasks.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch task type management** in the **Instance batch**
**operations** section.
5. In the upper part of the Batch task type management page, click **New type**.
6. In the **New type** dialog box, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Name | The name of the new task type. |
| Number | The ID of the new task type. |
| API | The API name of the new task. |
| api Instance parameter name | The parameter name of the API instance. Default value: DBInstanceName. |
| Prompt information | The prompts, notes, and reminders that are displayed for the task type. |
| Parameter rules | The parameter rules, including the parameter name, API parameter name, and parameter type. |
| Validation rules | The validation rules, including the validation relationship, attribute name, validation rule, and validation value. |
| Highest concurrency | The maximum number of concurrent tasks. |
| Stop failure rate | The probability of tasks being stopped or failing. |
| Remarks | The remarks of the task type. |

7. Click **Submit**.

##### 2.3.5.7 Manage SQL templates

This topic describes how to create an SQL template.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **SQL Template management** in the **Instance batch**
**operations** section.
5. In the upper part of the SQL template list page, click **New template**. The **NewTemplate**
dialog box appears.
6. In the **NewTemplate** dialog box, configure the parameters described in the following
table.

| Parameter | Description |
|---|---|
| Template name | Enter the name of the new template. |
| Template type | Select the type of the new template. |
| Database name | Select the database on which the template is used. |
| Database type | Select the type of the target database. |
| SQL script | Enter the script of the SQL template. |
| New reason | Enter reason for creating the template. |

> **Note:** Custom SQL templates support only SELECT statements and can be used only for DBaaS databases. The creation of SQL templates requires BPMS approval. To prevent the SQL template from being accidentally executed by other members, which could result in batch tasks being sent to incorrect instances, we recommend that you provide a detailed description of the template name and the reason for its addition in the SQL template.

7. Click **Submit**.

#### 2.3.6 Manage instance plan migration

The instance plan migration list can be uploaded in two ways: batch submission by instance or by host IP address. This topic describes the detailed procedures for instance plan migration.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance plan migration**
**management**.
4. Select an upload mode for the instance migration plans.

> **Note:** Mode 1: If you select Submit by instance and non-migratable instances are detected, the system blocks the entire submission.
> Mode 2: If you select Submit by host IP address, the system directly filters out non-migratable instances.

5. Click **Download template file** and fill in the template file.
6. Click **Select File** and select the completed template file.
7. Click **Submit**.

**References**

You can click **Push success list** or **Deleted list** in the upper part of the **Instance plan**
**migration management** page to view details.

#### 2.3.7 View the instance dashboard

This topic describes how to view metrics of instances, such as CPU utilization and connection utilization, on the instance dashboard.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance dashboard**.
4. You can view the CPU utilization, connections, IOPS, and disk utilization of an instance. The
top 20 items are displayed by default.

### 2.4 Host management

#### 2.4.1 Create a host

This topic describes how to create a host.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. In the upper part of the System host page, click **Emergency response plan**.
4. On the Host Information page, click **New host**.
5. In the dialog box that appears, configure the parameters and click **Submit**.

#### 2.4.2 Configure multiple hosts at a time

This topic describes how to configure multiple hosts at a time.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. On the System host page, select the hosts that you want to configure and click **Batch**
**configuration** in the upper part of the page.
4. In the Batch configuration parameters dialog box, configure the parameters and click
**Submit**.

#### 2.4.3 View host information

This topic describes how to view the information about a host.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. Search for the host you want to view by its IP address or host name.
4. Click the IP address of the host and view information on the **Host details** page. The
information includes the CPU utilization, memory usage, disk usage, and the number of instances. You can also click the options in the Host details section to view the information about host instances, performance, backups, and accounts.

#### 2.4.4 Physical machine group

ApsaraDB Operations and Maintenance System allows you to use the physical machine group feature to build an independent logical resource pool. This enables physical isolation and finegrained scheduling of underlying hardware resources to ensure resource exclusivity and stability across different business scenarios.

**Background information**

You can use the **physical machine group** feature to create a resource pool for multiple physical machines, enabling isolation of physical machine resources. This feature provides the following practical values: Database instances of different levels and categories can use separate physical machine resource pools to achieve physical isolation. The resources of physical machines in the test environment are isolated from those in the production environment. This prevents the test instance and the production instance from being created on the same physical machine and prevents the production instance from being affected in scenarios such as performance stress testing on test instances. During the replacement of old and new machine models, separate resource pools can be planned for legacy and new machines for independent use.

> **Note:** The physical machine group feature is currently supported only for PolarDB-X 2.0 instances.
> After creating a physical machine group, you can specify the physical machine resource pool to which the instance belongs when you create a database instance in the Apsara Uni-manager Management console. For more information, see Create an instance and other relevant chapters in the corresponding User Guide.

**View the information about a group**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. In the upper-right corner of the page that appears, click **Physical Machine grouping** to
go to the **Physical Machine grouping** page. On the page that appears, you can view all groups.

**Create a physical machine group**

1. On the **Physical Machine grouping** page, click **Create a group** in the upper-right
corner.
2. In the **Create Group** dialog box, configure the **Group name** and **Database type**
parameters, and select a machine from the **Machine** drop-down list.
3. Select an idle physical machine and click the
icon to add it to the current physical machine group.
4. Click **Create** to create a group.

**Edit a physical machine group**

1. On the **Physical Machine grouping** page, find the physical machine group that you want
to edit and click **Edit** in the Operation column.
2. On the **Edit Group** dialog box, edit the **Database type** and **Machine** parameters.
3. Click **OK**.

**Delete a physical machine group**

> **Note:** Before you delete a physical machine group, make sure that all instances deployed on the physical machine are cleared.

1. On the **Physical Machine grouping** page, find the physical machine group that you want
to delete and click **Delete** in the Operation column.
2. In the message that appears, click **OK**.

#### 2.4.5 Manage host software packages

This topic describes the core management features of software packages on cloud database hosts, including installation, uninstallation, and operation record query. You can maintain the host running environment in a secure and traceable manner through the unified interface, ensuring the stability and compliance of database services.

**Use cases**

Ensure version consistency during cluster scale-out Scenario: When you scale out a database cluster, new nodes may have an initial version that differs from existing nodes. Solution: Install a specific package version in batches to align new nodes with existing ones. This ensures all nodes in the cluster run the same version and prevents compatibility issues. Perform emergency fixes and version rollbacks Scenario: The production version has a known bug, or a performance regression occurs after an upgrade. Solution: Quickly fix the issue by deploying a patch in batches. If an upgrade fails, you can uninstall the new version and roll back to a stable version to minimize downtime. Use canary releases and circuit breaking Scenario: During the initial stage of a new release, you need to limit risk and prevent defects from spreading. Solution: Control package distribution by enabling or disabling it. You can perform a canary release by first enabling the package on specific hosts. After you confirm its stability, you can roll it out to all hosts. If a critical defect is found, you can immediately disable the package for circuit breaking.

**Supported database types**

The following Apsara architecture packages are supported: RDS MySQL PolarDB for MySQL Active-Standby Edition PolarDB for PostgreSQL PolarDB for PostgreSQL (Oracle Compatible)

**Install a software package**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**. On the page
that appears, find the host that you want to manage and click **Details** in the **Operation** column.
3. In the left-side navigation pane, click **Host software package management**. On the
page that appears, find the package whose status is **Not installed** and click **Software**
**Package Version Management** in the **Operation** column.
4. In the panel that appears, click **Install**.
5. In the dialog box that appears, select **Operating Instructions**, specify **Operation**
**reason**, and click **OK**.
You can view the progress in the **Installation status** column. If the status changes from
**Installing** to **Installed**, the installation is complete.

**Uninstall a software package**

> **Important:** Uninstalling a package is a high-risk operation. If a running database instance depends on dynamic libraries or binary files within the package, forcibly uninstalling it can cause missing dependencies, which may prevent the database instance from starting or lead to downtime.
> Before you proceed, ensure that no critical instances are running on the target host, or that you have a comprehensive disaster recovery and rollback plan in place.

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**. On the page
that appears, find the host that you want to manage and click **Details** in the **Operation** column.
3. In the left-side navigation pane, click **Host software package management**. On the
page that appears, find the package whose status is **Installed** and click **Software**
**Package Version Management** in the **Operation** column.
4. In the panel that appears, click **Uninstall**.
5. In the dialog box that appears, select **Operating Instructions**, specify **Operation**
**reason**, and click **OK**.
You can view the progress in the **Installation Status** column. If the status changes from
**Uninstalling** to **Uninstalled**, the installation is complete.

**Query software package change records**

This feature is used to check whether the software package is installed or uninstalled.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**. On the page
that appears, find the host that you want to manage and click **Details** in the **Operation** column.
3. In the left-side navigation pane, click **Host software package management**. On the
page that appears, click **Package change Records**. The page displays information including operation type, operation time, and result description.

### 2.5 Cluster management

#### 2.5.1 Configure cluster parameters

This topic describes how to configure cluster parameters.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. On the **System Cluster** page, select the cluster for which you want to modify parameters,
click **Cluster parameter settings**, configure the parameters, and then click **Submit**.

> **Important:** You can configure only one cluster at a time.

> Different database types, such as MySQL and MongoDB, support different parameters. The actual displayed parameters are subject to the console configuration.

| Supported configuration item | Description |
|---|---|
| Set Overcommitment Ratio | You can configure the overcommit ratio (in percentage) for CPU (valid values: [100,10000] , where 0 indicates unlimited), memory (valid values: [100,100]), and disk (valid values: [100,5000] ). |
| Set new MySQL default support permission release | Supported options: Permission not released, Permission support release later, and Permission release. Default value: Permission release. Note If no permission policy is specified during instance creation, the default setting above for the cluster is applied. |
| Set Table consistency validation percentage | Control the sampling ratio for table data consistency checks. Unit: percentage. Valid values: [0,100] . |
| Set backup set playback validation timeout | Unit: seconds. Valid values: [0,86400] . Note If the parameter is set to a non-zero value, backup set playback verification is performed during sub-instance restoration, read-only instance creation, disaster recovery instance creation, and standby database rebuild. Verification terminates upon timeout. |
| Set backup set validation percentage | Unit: percentage. Valid values: [0,100] . Note If the parameter is set to a non-zero value, the system periodically extracts the backup set proportionally to create a temporary verification sub-instance. After the verification is complete, the sub- instance is deleted immediately. |
| Set backup does not fall to the ground | All instances within the cluster will uniformly apply this backup storage policy. Supported options: Close, Only data does not fall to the ground, and Data log does not fall to the ground. |
| Set backup compression | Once enabled, all instances within the cluster will uniformly use this compression method. Supported options: no compression and zlib compression. |

| Set backup streaming recovery | Once enabled, all instances within the cluster will uniformly use this streaming recovery mode. Supported options: Close and Streaming recovery. |
|---|---|
| Set instance HA priority mode | Control the priority policy during the HA switchover. Supported options: Availability priority and Reliability first. Default value: Availability priority. |
| Set the sync binlog _ refresh mode | Configure binlog persistence for ApsaraDB RDS for MySQL clusters. Supported options: Security mode ( sync binlogs=1 for both _ primary/secondary), Normal mode (1/1000), and High-performance mode (1000/1000). Default value: Normal mode. |
| Set up PetaData streaming migration | Once enabled, all instances within the cluster will uniformly use this streaming migration method. Supported options: Close and Streaming relocation. |
| Set Supported business type | If this parameter is set to RDS, only ApsaraDB RDS instances can be created in the cluster; RDS is supported by default. Supported options: RDS, PetaData, and All. |
| Set the BINLOG Upload method | Controls whether binary logs are uploaded to remote storage. Supported options: Do not Upload and Upload. Default value: Upload. |
| Set BINLOG local cleanup method | Controls whether local binary log files are automatically cleared. Supported options: Do not clean up and Clean up. Default value: Clean up. |
| Set BINLOG Backup compression | Configures the compression mode for binary log backups. Supported options: no compression and zlib compression. Default value: zlib compression. |
| Set BINLOG disk space warning threshold | When the disk space used by binlogs reaches this threshold, a warning is triggered. Unit: percentage. Valid values: [0,100] . |
| Set the BINLOG disk space warning threshold | When the disk space used by binlogs reaches this threshold, a critical warning is triggered. Unit: percentage. Valid values: [0,100] . |
| Set disk type | Specifies the type of the underlying storage medium of the cluster. Supported options: SSD, SATA, ECS, Mixed, and POLAR. Default value: SSD. |
| Set Mysql large instance migration solution | Controls whether to enable the dedicated migration process for primary ApsaraDB RDS for MySQL instances. Supported options: Disabled and Enabled. |

| Set automatic expansion on | Once enabled, instances in the cluster can be automatically scaled out when the specified conditions are met. Supported options: Close and Open. |
|---|---|
| Set arch version _ | Identifies the cluster architecture version. The specific value is managed by the platform. |
| Set perf status _ | Specifies the link type for collecting performance monitoring data. Supported options: Old link, Grayscale second link, and Second level link. |
| Set host support for gigabit NICs | If not explicitly specified during cluster creation, Gigabit NIC support is disabled by default. Supported options: Not supported (default), Support. |

#### 2.5.2 Manage service types

This topic describes how to manage service types.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Cluster management**.
3. In the left-side navigation pane, click **Service Type Management**. The **Service Type**
**Management** page appears.
Find the service type that you want to modify and click **Edit** in the **Operation** column to modify the service type. Find the service type that you want to delete and click **Delete** in the **Operation** column to delete the service type.

#### 2.5.3 Manage service nodes

This topic describes how to create, modify, and delete a service node.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management section, click **Service node management**.
In the upper part of the page, click **New service node**. In the dialog box that appears, configure the required parameters and click **OK**. Find the service node that you want to modify and click **Edit** in the **Operation** column to modify the service node. Find the service node that you want to delete and click **Delete** in the **Operation** column to delete the service node.

#### 2.5.4 Manage DB configuration templates

This topic describes how to manage DB configuration templates.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Cluster management**.
3. In the Cluster management section, click **DB configuration template** to go to the **DB**
**configuration template** page.
In the upper part of the page, click **New DB template**, enter the template information, and then click **Save** in the **Operation** column. Find the template that you want to modify, click **Edit** in the **Operation** column to modify the template, and then click **Save** in the **Operation** column. Find the template that you want to delete and click **Delete** in the **Operation** column. In the dialog box that appears, click **OK** to delete the template.

#### 2.5.5 Manage Fangcunshan clusters

This topic describes how to manage Fangcunshan clusters.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management section, click **Fangcunshan cluster management** to go to
the **Cluster group configuration** page.
4. In the upper part of the page, click **New cluster group**.
5. In the dialog box that appears, select a region, enter the cluster group name, and then click
**Confirm**.
6. Click **Set up a cluster** in the **Operation** column of the new cluster. In the dialog box that
appears, configure the resource type of the instance and click **Confirm**.
7. Optional. Find the cluster group that you want to modify and click **Modify a cluster group**
in the **Operation** column to modify the cluster group name.
8. Optional. Find the cluster group that you want to delete and click **Delete a cluster group**
in the **Operation** column to delete a cluster group.

#### 2.5.6 Manage locations

This topic describes how to configure the locations of clusters.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. In the left-side navigation pane, click **Location**.
4. On the page that appears, search for clusters by keyword and configure their locations.

> **Note:** You can also perform cluster consistency check and subdomain consistency check on this page.

Click **Add** next to the required unit, region, or zone to add a location node, and then click
**Submit**.
Click **Parameters** next to the required unit, region, zone, or subdomain to add, modify, or delete parameters. Click **Delete** next to the required unit, region, zone, or subdomain to delete a unit, region, zone, or subdomain.

### 2.6 Task management

#### 2.6.1 Manage interrupted tasks

This topic describes how to manage interrupted tasks, including user instance tasks, host instance tasks, and host tasks. This topic uses a user instance task as an example to describe how to manage interrupted tasks.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
**console**, click **Task Management**. In the upper-left corner of the **Instance tasks** page,
select **Interrupted tasks** from the drop-down list.

> **Note:** If interrupted tasks exist, perform the following steps.
> If no tasks are displayed, skip the remaining part of this topic.

3. Click a task in the **Task name** column to view and analyze the cause of the task failure.

> **Note:** In most cases, if you encounter issues such as abnormal status of secondary databases, connection timeout errors, or password errors, you can log in to the required instance by using the instance IP address and fix the issue.

4. After you fix the issue, find the task and click **Operation** in the **Operation** column.
5. On the page that appears, click **Perform tasks**.
6. In the **Re-execute the task** dialog box, click **Current step retry** to run the task again.

> **Important:** If you want to retry the task starting from a specific step, click **Continue from the** **specified step**. We recommend that you do not retry the task if you are not familiar with the task or purposes of its steps.

7. In the upper-left corner of the Instance tasks page, select **Running tasks** from the drop-
down list to view the status of the task.

> **Note:** If the task fails again, repeat the preceding steps.

#### 2.6.2 Manage temporarily closed tasks

This topic describes how to manage temporarily closed tasks.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Task Management**. In the upper-left corner of the Instance tasks page, select **Temporarily Closed tasks** from the drop-down list. Click a task name in the **Task name** column. In the message that appears, view the steps of the task. Find a task and click the operation object name in the **Operation object** column to view the task logs of this operation object. Find a task and click the operator name in the **Executor** column to view the information about the operator. Find a task and click **Operation** in the **Operation** column to view the reason why the task is temporarily closed. On the page that appears, click **Perform tasks** to retry the task. On the page that appears, click **Intervention record** to view the intervention records of the task. Find a task and click **Add remarks** in the Operation column to add remarks for the task.

#### 2.6.3 View workflow O&M information

This topic describes how to view the task list and workflow O&M information. A workflow is triggered when you perform O&M tasks on an instance, such as creating an instance, restarting the instance, and changing its configurations. When the workflow is completed, the related O&M task ends. If a step in the workflow fails, you must troubleshoot the failure.

**View the task list**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click **Advance search** at the top and filter PolarDB-X instances using the search boxes.
4. Find the required instance and click its name in the **User instance name** column.
5. In the left-side navigation pane, click **Task list**. On the right side of the page, you can view
all tasks, tasks being interrupted, waiting tasks, interrupted tasks, temporarily closed tasks, suspended tasks, and running tasks. You can filter tasks and specify which columns to display.

**View workflow details pages**

On the Task list page, click a task ID in the **Task ID** column to go to the workflow details page.
**Basic Information**: displays the basic information of the workflow, including the task ID,
workflow ID, workflow duration, and start and end time.
**Execution Logs of Current Step**: displays the execution logs of the current step.
**Workflow steps**: displays the execution details of each step of the workflow, such as the
execution time, parameters, status, and duration. It also displays the operations in each step, such as retry, step redirection, and temporary closing. The following figure shows a successful step. If a step fails, the retry, step redirection, and temporary closing are supported. The following figure shows a failed step.
**Task Intervention Logs**: displays the operation information of each workflow O&M.
**Interrupt Workflows**: displays the Interrupted task tab. Click the ID of the interrupted task
to go to the workflow details page. You can use it to handle interrupted steps. Retry: Click it to retry the current step. If the step is still interrupted, contact Alibaba Cloud technical support personnel. Temporarily shutdown: If a workflow does not require processing or is temporarily not needed, close the workflow to avoid affecting other workflows. Contact Alibaba Cloud technical support personnel to perform this operation. Redirect to the specified step: You are redirected to another step. Contact Alibaba Cloud technical support personnel to perform this operation.

### 2.7 System management

#### 2.7.1 Feature Overview

This topic describes the features of system management. Table 1. System management

| Feature | Description | Remarks |
|---|---|---|
| System settings | You can create packages, configure system settings, manage database parameter templates, configure system parameter settings, manage traffic statistics rules, configure performance settings, manage Internet service provider (ISP) information, configure component exception levels, and configure Linux kernel parameters. | The operations are of high risks. |
| Permission configuration | You can add roles and manage permission codes. | Permission code management is of high risks. |
| General configuration | You can enable or disable ACL cache, enable or disable email, create cluster information, and send cluster information. | None. |
| Label list | You can add labels and view the types, aliases, and values of labels. | None. |
| Cluster management | You can create clusters, refresh management machine whitelists, refresh synchronization modes, and refresh resource cache. | The operations are of high risks. |
| Whitelist management | You can view and refresh region whitelists. | None. |
| Service type management | You can modify and delete service types. | Service type creation is of high risks. |
| Host masking information management | You can add and remove masked host IP addresses. | None. |
| AccessKey management | You can create and view AccessKey pairs, and view logs for O&M APIs. | The operations are of high risks. |

| Fangcunshan cluster configuration | You can view the configurations of cluster groups and create cluster groups. | The operations are of high risks. |
|---|---|---|
| Disaster recovery management | You can perform inspections on link components and control components, perform switchover, and manage disaster recovery tasks. | None. |
| Scheduled task management | You can manage the scheduled tasks in the system. | None. |

#### 2.7.2 Change the unified storage location of logs

**logs**

By default, database system logs, such as audit logs, are written to SLS-inner, which is an internal logging service, and cannot be directly accessed by users. If you have clear global log governance requirements or centralized log analysis requirements, you need to write logs to SLS-PUB, which is a public logging service that you can manage. You can perform a global switchover by enabling log storage to SLS-PUB.

**Usage notes**

> **Important:** This operation is a **one-time global configuration** and **cannot be rolled back** **after it takes effect**. After you enable log storage to SLS-PUB, **all existing and** **new instances will be affected**. This is reflected on the details page of each cloud database instance. On the SQL Audit tab of the Data Security page of a database instance, the Enable Log Storage to SLS-PUB switch is turned on by default. All subsequent logs, including audit logs, slow query logs, and error logs, will be stored in SLS-PUB by default. Exercise caution when you perform this operation.
> To meet the log visibility requirements of a single instance, perform the following operation: Log in to the Apsara Uni-manager Management Console. Go to the Instance Details page, choose Data Security > SQL Audit, and turn on the Enable Log Storage to SLS-PUB switch. You can enable this feature as needed and manage it for a single instance without affecting other instances. This way, instance management is more secure, flexible, and controllable.

**Prerequisites**

Simple Log Service (SLS) is activated. An SLS project (SLS-PUB) is created in the region where the database instance resides.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **System Management** to go to the **System**
**Settings** page.
3. On the **System parameter configuration** tab, change the value of
DUKANG_OPEN_PUB_SLS to **true**.

> **Note:** The global switchover entry is displayed on the page only after the value of this parameter is changed to true.

4. Click **Database instance log storage** at the top of the page to enable log storage to SLS-
PUB for all logs.
5. In the message that appears, confirm the risk prompt message and click **OK**.

> **Important:** Global switchover is a one-time, irreversible operation. After you enable log storage to SLS-PUB, you cannot switch back to log storage to SLS-inner. The change will take effect within 3 minutes.

After you enable this feature, you can view the updated records by performing the following operation: Log in to the Apsara Uni-manager Management Console. Go to the Instance Details page, choose Data Security > SQL Audit to view the updated records.

**Log query description**

After you change the storage location, you can perform the following log query operations: Query by a time range before the change: Historical logs that are stored in SLS-inner can be queried. Query by a time range after the change: New logs that are stored in SLS-PUB can be queried. Query by a time range that spans the point in time of change: Only the logs that are stored in SLS-PUB can be queried. Historical logs that are stored in SLS-inner before the change are not automatically merged and displayed. You must select a time range before the change for the log query.

### 2.8 Check important components

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Important Component**.

| Note If you cannot find the entry point of important components, you can visit the following link https://[Homepage address of ApsaraDB Operations and Maintenance System]/component/home# . |   |   |
|---|---|---|
|   | https://[Homepage address of ApsaraDB Operations and Maintenance |   |
| System]/component/home# |   |   |

3. On the Important components page, view the features of important components. For more
information, see the following table.

> **Important:** Important components involve high-risk operations. We recommend that you should not modify these components.

| Feature | Description |
|---|---|
| Abnormal instance information | View recent SMS alerts, instances with standby database interruptions, instances where standby database latency exceeds 600s, instances with HA disabled, and oversold host information. |
| HA information | View HA information, such as the system load table, HA switchover records, response time statistics for HA-dependent interfaces, and exception details. |
| Backup information | View backup failure trends, details of recent backup failures, and instances with binlog anomalies. |
| binlog information | View binlog service status, instances with binlog anomalies, and binlog status statistics. |
| SLB O&M management | View the number of SLB cluster instances and RDS cluster information. |
| Inconsistent data centers for instance link | View instances where the primary node and SLB are in different data centers. |
| Proxy cluster information | View proxy cluster information. |
| Page configuration | Add, edit, or delete pages. |
| pengineClassMeta tool | Add, edit, delete, or export pengineClassMeta information. |
| pengineStepMeta tool | Add, edit, delete, or export pengineStepMeta information. |

| Product performance summary and analysis | Displays product performance information. |
|---|---|
| Message list | Displays the message list. |
| Sent message records | Displays sent message records. |
| ROBOT management | Displays ROBOT processing logs, switch controls, alert contacts, repair statistics, and more. |
| Redis proxy slow log management | View Redis proxy slow logs and analyze their causes. |

### 2.9 Handle exceptions

This topic describes how to handle database alerts in the ApsaraDB Operations and Maintenance System console and optimize existing monitoring metrics.
1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Home Page**.
3. In the **Data Summary**, **Backup information**, **High availability HA Information**,
**Resource Information**, or **Task information** sections, click the number next to Number
of exceptions to go to the corresponding task page.
4. Select the exception that you want to handle and click **Handling exceptions** in the
**Operation** column.

> **Note:** If you want to handle multiple exceptions at the same time, you can select all the exceptions that you want to handle and click **Batch processing** in the upper-left corner of the list.

5. In the **Handling exceptions** dialog box, view the details and troubleshoot the error
accordingly.

> **Note:** If you want to handle multiple exceptions at a time, you can view the details and troubleshoot the error accordingly in the **Batch handling exceptions** dialog box.

6. Click **Submit**.

### 2.10 Appendix

#### 2.10.1 Log in to the Apsara Uni-manager Operations Console

**Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
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
manager Platform Operations

## 3 Apsara Uni-manager Platform Operations

**Platform Operations**

### 3.1 Configure a custom password policy for PolarDB

**policy for PolarDB**

In an Apsara Stack environment, if you want to create an account that complies with a custom password policy for PolarDB databases, you need to first configure the corresponding password policy in the Apsara Uni-manager Operations Console. After the policy is configured, it is automatically synchronized to the account creation page of PolarDB in the Apsara Unimanager Management Console for subsequent database account creation.

> **Important:** This operation is a global configuration at the account level. If you enable this policy, the policy takes effect for all tenants under the current account during the creation of PolarDB database accounts in the Apsara Uni-manager Management Console.

**Feature overview**

Visualized configuration: allows you to configure password complexity rules in the console. Real-time verification: When you create a database account, the system verifies whether the password meets the policy requirements in real time. Multi-scenario adaptation: applicable to database instances with different security levels, meeting compliance and security requirements.

**Supported services**

PolarDB for MySQL PolarDB for PostgreSQL

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome. i. Open a browser. manager Platform Operations ii. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

iii. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

iv. Click **Agree to Private Policy and Log On** .
2. **Go to the PolarDB switch management page**
i. In the top navigation bar of Apsara Uni-manager Operations Console, move the pointer over **Platform Operation**. Under **Management and Control Service O&M**, select
**UniConsole**.
ii. On the **Products** page, enter the **polardb** keyword in the search box, click Search, and then click **Channel List** in the **Actions** column.
3. **Configure a custom password policy**
i. **Configure a password policy** On the **polardb Channels** page, search for **PASSWORD_RULES**. Click **Edit** in the Actions column to configure the password policy, and then click **OK**. ii. **Configuration policy description** On the **polardb Channels** page, search for **PASSWORD_RULES_MESSAGE**. Enter the corresponding policy description, and then click **OK**.

> **Note:** After you complete the preceding configurations, all tenants under the current account need to follow the custom password policy when they create PolarDB database accounts in the Apsara Uni-manager Management Console.

4. **Create a database account that complies with the policy**
manager Platform Operations After the password policy takes effect, create a PolarDB database account in the Apsara Uni-manager Management Console. For more information, see the **Create an account**
**topic in the User Guide**. The system automatically applies the configured password
policy and prompts an error in real time when you enter a password that does not comply with the rule.

### 3.2 Turn on the IPv6 display switch for PolarDB

**switch for PolarDB**

If you want to configure an IPv6 address when you create a PolarDB instance in an Apsara Stack environment, you must turn on the IPv6 display switch in the Apsara Uni-manager Operations Console. After the IPv6 display switch is turned on, an IPv6 configuration option is displayed on the instance creation interface in the PolarDB console.

> **Important:** This operation is an account-level global setting. After the IPv6 display switch is turned on, all tenants within the current account can configure IPv6 when they create instances in the PolarDB console.

**Applicable services**

PolarDB for MySQL Primary/Secondary Edition PolarDB for PostgreSQL Primary/Secondary Edition

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome. i. Open a browser. ii. In the address bar, enter the URL of the Apsara Uni-manager Operations Console and press Enter.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

manager Platform Operations iii. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

iv. Click **Agree to Private Policy and Log On** .
2. **Navigate to the switch management page of** PolarDB
i. In the top navigation bar of Apsara Uni-manager Operations Console, move the pointer over **Platform Operation**. Under **Management and Control Service O&M**, select
**UniConsole**.
ii. On the **Products** page, search for **polardb** and click **Switch List** in the **Actions** column.
3. **Turn on the IPv6 display switch**
On the **polardb Switches** page, search for `enableIPv6` .

> **Note:** Click **Change Switch Status** in the **Actions** column to turn on the switch. After the switch is turned on, all tenants within the current account can view and configure IPv6 when they create instances in the PolarDB console.

4. **Create a** PolarDB **instance and configure IPv6**
After the switch is turned on, log in to the PolarDB console, create a PolarDB instance, and configure **IP Type**. For more information, see the **Create an instance** topic in User Guide. aintenance

## 4 Security maintenance

### 4.1 Network security maintenance

Network security maintenance consists of device and network security maintenance.

**Device security**

Check network devices and enable their security management protocols and configurations of devices. Check for timely updates to secure versions of network device software. For more information about the security maintenance method, see the device documentation.

**Network security**

Based on your network considerations, select the intrusion detection system (IDS) or intrusion prevention system (IPS) to detect abnormal Internet and Intranet traffic and protect against attacks.

### 4.2 Account and password maintenance

**maintenance**

Account passwords include PolarDB system passwords and device passwords. To ensure account security, you must use complex passwords for your systems and devices and change these passwords on a regular basis. oting

## 5 Troubleshooting

### 5.1 Fault emergency mechanism

A fault emergency mechanism must be established to minimize the impacts on business.

**Response mechanism**

A fault emergency response mechanism must be established, so that you can contact relevant maintenance engineers to rectify faults or handle security events as soon as possible.

### 5.2 Stock-up mechanism

A stock-up mechanism must be established for fragile hardware devices to ensure that hardware faults are rectified in a timely manner. This mitigates the negative impacts of hardware faults.

### 5.3 Troubleshooting procedure

Faults must be promptly identified and rectified based on their symptoms. This topic describes the troubleshooting procedure. When you detect a system fault during routine maintenance, you can use ApsaraDB Operations and Maintenance System to check the fault details, analyze its causes, and then rectify the fault based on fault logs. If the fault cannot be rectified, collect fault information such as system information and fault symptoms, contact Apsara Stack technical support engineers, and then troubleshoot the fault under the guidance of the engineers. After the fault is rectified, verify the solution, review the troubleshooting method, and then make improvements.

### 5.4 Common faults and solutions

#### 5.4.1 High CPU utilization of an instance

This topic describes common causes of high CPU utilization and their solutions. It also analyzes a typical scenario where CPU utilization reaches 100% and provides corresponding solutions.

**Problem description**

When you use PolarDB for PostgreSQL, CPU utilization may increase significantly and even reach 100%.

**Problem causes**

A sudden surge in active connections. Many slow SQL statements are executed concurrently.

**Solutions**

Step 1: Determine whether the connection surge results from a service peak. oting
1. You can execute the following command to check the current number of active
connections.

```
select count( * ) from pg_stat_activity where state not like '%idle';
```

2. Log on to the console to view monitoring information, such as the number of connections,
and confirm whether an abnormal upward trend exists. Step 2: Identify slow SQL statements using one of the following three methods.
1. Use the `pg_stat_statements` extension to analyze SQL statements with the worst
cumulative performance.

> **Note:** This method applies only to instances where the `pg_stat_statements` extension is enabled.

i. The extension and the database system use counters, such as for accumulated SQL running time. This information accumulates over time and includes historical data. To troubleshoot the current high CPU issue more effectively, first reset the counters using the following commands.

```
create extension pg_stat_statements; select pg_stat_reset(); select pg_stat_statements_reset();
```

ii. Wait for a period, such as 1 minute, to allow the counters to accumulate sufficient information. iii. Execute the following command to query the most time-consuming SQL statements. These statements are often the direct cause of high CPU utilization.

```
select * from pg_stat_statements order by total_time desc limit 5;
```

iv. Execute the following command to query the SQL statements with the highest number of buffer reads. These statements might cause excessive buffer reads and high CPU consumption because the queried data lacks an index.

```
select * from pg_stat_statements order by shared_blks_hit+shared_blks_read desc lim it 5;
```

2. You can directly query the pg_stat_activity view. Use the following SQL statement to
identify long-running SQL statements that have not completed. Such statements can also cause high CPU utilization. oting

```
select datname,
       usename,
       client_addr,
       application_name,
       state,
       backend_start,
       xact_start,
       xact_stay,
       query_start,
       query_stay,
       replace(query, chr(10), ' ') as query
from
  (select pgsa.datname as datname,
          pgsa.usename as usename,
          pgsa.client_addr client_addr,
          pgsa.application_name as application_name,
          pgsa.state as state,
          pgsa.backend_start as backend_start,
          pgsa.xact_start as xact_start,
          extract(epoch
                  from (now() - pgsa.xact_start)) as xact_stay,
          pgsa.query_start as query_start,
          extract(epoch
                  from (now() - pgsa.query_start)) as query_stay,
          pgsa.query as query
   from pg_stat_activity as pgsa
   where pgsa.state != 'idle'
     and pgsa.state != 'idle in transaction'
     and pgsa.state != 'idle in transaction (aborted)') idleconnections
order by query_stay desc limit 5;
```

3. Start by checking table scan information to identify tables that lack an index. If a table
lacks an index and most of its hot data resides in memory—for example, 6 GB of hot data in 8 GB of memory—the database performs a table scan. This process requires processing many irrelevant records already loaded into memory, which consumes significant CPU resources. For tables with more than 100,000 records, a single table scan can consume substantial CPU resources—effectively maxing out one CPU core—especially when hundreds of concurrent connections exist. i. Execute the following command to identify the tables with the highest number of table scans.

```
select * from pg_stat_user_tables where n_live_tup > 100000 and seq_scan > 0 order by seq_tup_read desc limit 10;
```

ii. Execute the following command to query the slow queries that are currently running and accessing the tables identified in the previous step.

```
select * from pg_stat_activity where query ilike '%<table name>%' and query_start now() > interval '10 seconds';
```

oting iii. Use `pg_stat_statements` to identify frequent and inefficient SQL statements that involve the table.

```
select * from pg_stat_statements where query ilike '%<table>%'order by shared_blks_hit+shared_blks_read desc limit 3;
```

Step 3: Handle slow SQL statements.
1. You can execute the following commands to terminate the slow SQL statements and
resume normal service operations.

```
select pg_cancel_backend(pid) from pg_stat_activity where query like '%<query text>% ' and pid != pg_backend_pid(); select pg_terminate_backend(pid) from pg_stat_activity where query like '%<query tex t>%' and pid != pg_backend_pid();
```

If these SQL statements are required for your services, optimize them as follows.
2. For the tables involved in the query, execute the ANALYZE [$Table] or `VACUUM ANALYZE`
[$Table] statement to update table statistics and generate more accurate query plans. To avoid affecting your services, run these statements during off-peak hours.

> **Note:** [$Table] is the table involved in the query.

3. You can execute one of the following SQL statements to view the execution plan. The first
SQL statement displays the plan without actually running the query. The second SQL statement runs the query and provides detailed execution information. For tables that involve a table scan, create an index.

```
explain [$Query_Text] explain (buffers true, analyze true, verbose true) [$Query_Text]
```

> **Note:** [$Query_Text] is the SQL statement.

4. Rewrite the SQL statements. For example, remove unnecessary subqueries, rewrite UNION
ALL clauses, or use a JOIN clause to control the join order.

#### 5.4.2 Sudden increase in database disk usage

**usage**

This topic describes why database disk usage might suddenly increase and how to resolve the issue.

**Problem description**

The disk space usage of an ApsaraDB PolarDB for PostgreSQL database suddenly increases.

**Causes**

A high volume of updates generates many logs. If these logs are not archived or deleted promptly, they consume disk space. oting Some queries sort or join large amounts of data, creating temporary tables. These temporary tables can overflow to disk, rapidly consuming a large amount of disk space.

**Solutions**

You can increase the disk space of the instance or reduce the frequency of update operations. You can run the following SQL statement with a PolarDB privileged account to set a limit on the temporary tablespace for each query. The limit is specified in kilobytes (KB). If a query exceeds this limit, the database reports an error. This helps you find problematic SQL statements and prevents them from using all your disk space.

```
alter role all set temp_file_limit = [$Table_Space_Limit];
```

> **Note:** [$Table_Space_Limit] is the temporary tablespace limit.

#### 5.4.3 Interrupted rebuild of a secondary database with local disks

**database with local disks**

This topic describes how to handle an interrupted rebuild of a secondary database.

**Problem description**

An exception interrupts the rebuild of a secondary database that uses local disks.

**Solutions**

1. If the current cross-machine rebuild task fails, the process proceeds to
`do_create_drop_mirror_ins_task` to delete the temporary instance. Then, a new crossmachine rebuild task is initiated in Dukang. If a cross-machine rebuild has already been initiated and has failed, do not issue another cross-machine rebuild task. You should first attempt a local rebuild on the secondary database.
2. If the kernel reports the error `xxx has already been removed` :
For a local rebuild: Check the kernel logs on the secondary database. For a cross-machine rebuild: Check the kernel logs on the destination instance. If no logs are found, check the logs on the primary database. To resolve this issue: a. Modify the parameters in the console of the Dukang primary instance (recommended). If this is not supported, modify the `postgresql.conf` file and then execute `select`

```
pg_reload_conf(); :
```

| rease the value of | wal keep segments _ _ |   |
|---|---|---|
| (wal keep segments × 16 / 1000) _ _ |   |   |
|   |   | GB |

not exceed the remaining space on the primary database. For database versions > 12: Increase the value of `wal_keep_size` to 2 to 5 times its current value, ensuring that `(wal_keep_size / 1000)` GB does not exceed the remaining space on the primary database. b. In the instance configuration settings in Dukang, set IOPS to 100000. oting c. For a local rebuild, the workflow proceeds to `do_clean_pg_data` . For a cross-machine rebuild, log on to the target instance, execute `cd /u01/instance_name/ && rm -rf` `./data` , and then the workflow proceeds to `do_backup_on_dst_master` .
3. If the task is interrupted at `do_backup_on_dst_master` or `do_backup_on_slave` :
Log on to the target instance (or secondary database) to check if the `pg_basebackup` process is still running. (The larger the data volume, the longer the process takes. For terabyte-scale data, this process can take several hours). After you confirm that no processes are running, follow the instructions in Step 2 and proceed to the corresponding step. If the process was interrupted at `do_make_dir` : Run the following commands:

```
rm -rf /home/pgsql/instance_name rm -rf /u01/instance_name rm -rf /u02/instance_name userdel -r username
```

After executing the commands, retry the task. To clean up temporary instances left from manual operations, run the following SQL statement:

```
insert into task_queue select 0, id, 0,now(),now(), 'delete_ins', '',8,'',0,0,now(),now(),0,0,null,'',0,'',0,'','','','',0,0 from cust_instance where id=${instance_id};
```

#### 5.4.4 Instance Cross-Machine Upgrade/Downgrade: Read-Only Original Instance, Target Instance Not Started, or Instance Promote Failed

**Upgrade/Downgrade: Read-Only Original**

**Instance, Target Instance Not Started, or**

**Instance Promote Failed**

This topic describes how to resolve issues that occur during a cross-machine instance upgrade or downgrade, such as the original instance becoming read-only, the target instance failing to start, or a failed instance promotion.

**Prerequisites**

The database type is PolarDB PostgreSQL. The database instance version is 12.0 or later.

**Solution**

1. Connect to the target instance and check its status.

```
/u01/pgsql/bin/psql -U aurora -p <port> postgres
```

Execute the following command.

```
SELECT pg_is_in_recovery();
```

oting If the command returns `f` , the instance is already the Master and no further action is required. If the command returns `t` , proceed to the next step.
2. Change to the data catalog directory.

```
cd /u01/<instance name>/data
```

3. Check whether the postgresql.trigger file exists.

```
ls -l postgresql.trigger
```

If the file does not exist, execute the following command to create it.

```
touch postgresql.trigger
```

4. Set the correct permissions.
View the file owner of the current folder:

```
ll | head -5
```

Modify the permissions. For example:

```
chown xxx:xxx postgresql.trigger
```

5. Check the recovery status again.

```
SELECT pg_is_in_recovery();
```

Run the command every 10 seconds and repeat it 5 to 10 times. If the command still returns `t` , proceed to the next step.
6. Restart the database instance.
Replace `<port>` with the actual port number, such as 3001:

```
/usr/bin/pg_safe --defaults-file=/etc/pg<port>.cnf restart -c 1>>/usr/local/polar/log/suc.log 2>>/usr/local/polar/log/err.log
```

7. Verify that the Promote operation was successful.
Run the command again:

```
SELECT pg_is_in_recovery();
```

A return value of `f` indicates that the instance was successfully promoted to a writable Master instance.

#### 5.4.5 pg_wal logs fill up disk space on a PolarDB for PostgreSQL instance

**PolarDB for PostgreSQL instance**

This topic explains why pg_wal logs fill up disk space on a PolarDB for PostgreSQL instance and how to resolve the issue.

**Root cause**

oting The disk of the primary instance becomes full because the primary/standby state of the PolarDB PostgreSQL instance is abnormal or because Write-Ahead Logging (WAL) logs are generated too quickly.

**Solution**

1. Run the following command to clean up WAL logs using pg_archivecleanup.

> **Note:** In DuKang, you can view binlogs. You can delete only logs that have been uploaded to OSS. Otherwise, the rebuild of the secondary database fails.

```
$pg_home/bin/pg_archivecleanup $pg_wal/ 00000000000000000000XXXX
```

Apsara Stack PolarDB PostgreSQL is available in two deployment models: on physical servers and on ECS instances.
2. The PG_HOME and PG_WAL paths vary by deployment model.
i. The server type is physical.

```
PG_HOME:/u01/pgsql_yyyymm/ -- Replace yyyymm with the instance version number. Find it by running ps -ef | grep data and locating the instance by its name. PG_WAL:/home/pgsql/$instance_name/data/pg_wal
```

ii. ECS configurations.

> **Note:** The instance runs inside a Docker container on the ECS instance. You must enter the correct container first.

```
PG_HOME:/u01/pgsql/ PG_WAL:/data/pg_wal
```

3. After you resolve the disk space issue, rebuild the secondary database if the primary and
secondary databases are still abnormal.

#### 5.4.6 What do I do if the disk space is insufficient?

**insufficient?**

If the disk space is insufficient, some operations may fail to be performed.

**Possible cause**

Monitoring logs, PostgreSQL data files, or PostgreSQL log files occupy a large amount of space.

**Solution**

Monitoring logs are stored in the /usr/local/rds/log directory. You can delete earlier logs to free up space. PostgreSQL data files are stored in the /u01 directory. You can scale up your instance or migrate the instance to another machine. oting PostgreSQL log files are stored in the /u02 directory. You can clear PostgreSQL log files in ApsaraDB Operations and Maintenance System.

#### 5.4.7 Interrupted replication

Interruptions may occur when data is being replicated from a primary database to a secondary database.

**Possible causes**

The data in the primary and secondary databases is inconsistent, the network is disconnected, or the tables are damaged.

**Solutions**

If the data in the primary and secondary databases is inconsistent, rebuild the secondary database from scratch. In the Instance management module of the ApsaraDB Operations and Maintenance System, go to the details page of an instance and click **Standby database re-match** to rebuild the secondary database. If the network is disconnection, try reconnecting to the instance over the instance endpoint. If tables are damaged, repair the tables by using the secondary instance. Sample command:

```
 repair table a;
 start slave;
```

#### 5.4.8 Insufficient swap space

This topic describes the possible causes and solutions for insufficient swap space.

**Possible causes**

Too many clusters exist, or programs run abnormally. As a result, too much memory is consumed.

**Solution**

If too many instances run on the host, we recommend that you migrate some of the instances to other hosts. If this fault is caused by other reasons, perform the following steps: i. If the fault exists in the primary database, switch the services over to the secondary database. ii. Run the following command to clear the cache:

```
 /proc/sys/vm/drop_caches;
```

iii. Run the following command to clear the swap space:

```
 swapoff -a ; date ; swapon –a;
```

#### 5.4.9 High loads

This topic describes the possible causes and solutions of high loads.

**Possible causes**

oting Data is being backed up, too many programs are running concurrently, or the efficiency of SQL statements is low.

**Solution**

If data is being backed up, ignore this fault. If a large number of programs are concurrently running, contact the developers to reduce the number of concurrent programs. If high loads are caused by low efficiency of executing SQL statements, execute the EXPLAIN statement to check how the system processes the SQL statements and to find performance bottlenecks. If you cannot use indexes to improve the execution efficiency, contact the developers. Ease the limit on CPU and I/O resources.

#### 5.4.10 High replication latency

This topic describes the possible causes and solutions of high replication latencies.

**Possible causes**

The system is backing up data, no primary key is contained in the tables, an I/O bottleneck exists, or the network is experiencing heavy traffic.

**Solutions**

If the latency is less than 5,000 milliseconds and continues to decrease, the network may be experiencing slowdown due to heavy traffic. No action is required. Enable the concurrent handling feature. Log on to the instance and run the following commands:

```
 stop slave;
 set global slave_parallel_workers=8;
 start slave;
```

#### 5.4.11 Module exceptions

This topic describes a possible cause of module exceptions and its solution.

**Cause**

The module is not loaded.

**Solution**

Run one of the following commands to load the module:

```
 insmod $module file.ko
```

Or

```
 modprode $module file.ko
```

### 5.5 Hardware troubleshooting

#### 5.5.1 Disk failure

oting RAID 5 is configured on database nodes. Faulty disks can be directly replaced without affecting your business.

#### 5.5.2 Failures requiring server shutdown, including memory, motherboard, CPU, and power supply failures

**including memory, motherboard, CPU, and**

**power supply failures**

This topic describes the procedure before you shut down a server. Procedure: If you can enter the system, perform the following operations to stop the services running on the server. i. Stop the instances. It may take about 1 minute.

```
 /bin/bash /etc/init.d/mysql stop
```

ii. Check whether running MySQL instances exist.

```
 ps -ef|grep mysql;
```

iii. Shut down the server after all instances are stopped.

```
 shutdown -h now
```

iv. If you cannot access the system, you need to force shut down the server. After the server is repaired, some secondary databases may fail to run normally. In this case, maintenance personnel can log on to the **ApsaraDB Operations and**
**Maintenance System** and rebuild the secondary databases.
perations

## 6 High-risk operations

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

perations

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

| psaraDB for POLA |   |   |
|---|---|---|
| Data security |   |   |
|   | Change the network isolation mode of an instance to the enhanced whitelist mode | You cannot switch back to the standard whitelist mode. |

3.3 O&M description

## 7 Redline V4.3.3 O&M description

**description**

### 7.1 Services provided by Redline Enterprise

**Enterprise**

This topic describes the services provided by Redline Enterprise. Redline Enterprise provides the following services: redline-perf.LogWorker# redline-perf.OpenApi# redline-perf.PerfMaster# redline-perf.PerfWorkerr#

> **Note:** redline-perf.DbInit is discontinued.
> The collection agent of UE is deployed on physical machines in other modes.

### 7.2 Paths of files in the Docker container of redline-perf

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

3.3 O&M description

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

### 7.3 Perform environment checks

This topic describes how to perform environment checks.

**Prepare the script for batch operations**

1. Run the following commands on a jumper server to prepare the script for batch operations:

```bash
curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.PerfMaster%23" | grep ip | awk -F '"' '{print $(NF-1)}' > masterhosts curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.PerfWorker%23" | grep ip | awk -F '"' '{print $(NF-1)}' > perfworkerhosts curl "http://localhost:7070/api/v3/column/m.ip?m.sr.id=redline-perf.LogWorker%23" | g rep ip | awk -F '"' '{print $(NF-1)}' > logworkerhosts cat perfworkerhosts logworkerhosts masterhosts | sort -u > allhosts
```

2. Run the following command to install parallel-ssh (pssh). Skip this step if pssh has been
installed. 3.3 O&M description

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

ii. Check whether log entries that include deactived are returned. If yes, go to the corresponding Docker container and activate the clusters in the deactived state. For more information, see Activate clusters in the deactived state. 3.3 O&M description

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

### 7.4 O&M operations

#### 7.4.1 Scale in or out a cluster

This topic describes how to scale in or out a cluster.

**Determine whether scale-out is required**

Check the diagnostics information of an instance in the ApsaraDB Operations and Maintenance System console. If the data records of the previous three hours are displayed after more than 5 seconds, you may need to add nodes. More nodes can increase the response speed. You can balance the return on investment (ROI) of hardware based on your needs. Ten nodes can support 3,000 host nodes of MySQL instances of Community Edition. A single PolarDB instance can contain more than one host node.

**Add nodes**

1. Add a node and start it.

> **Note:** You can add multiple nodes at a time.

2. Log on to a master node.
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether the returned node information meets your expectations.
4. If the returned node information meets your expectations, run the `curl`

```
http://127.0.0.1:8080/admin/makeBaseline?apply=true command.
```

**Remove nodes**

1. Remove a node.

> **Note:** You can remove only one node at a time.

2. Log on to a master node.
3.3 O&M description
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether the returned node information meets your expectations.
4. If the returned node information meets your expectations, run the `curl`

```
http://127.0.0.1:8080/admin/makeBaseline?apply=true command.
```

5. Wait 30 minutes for data to be balanced among the remaining nodes and then continue to
remove other nodes based on your needs.

#### 7.4.2 Upgrade or restart a cluster

This topic describes how to upgrade or restart a cluster.
1. Log on to a PerfMaster node and run the following command to disable databases. If no
`success` message is returned, repeat the following command until a `success` message is returned.

```bash
curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=master"
```

2. Wait 2 minutes and upgrade or restart the cluster after data is stored on disks.
3. After the cluster is upgraded or restarted, perform environment checks.

#### 7.4.3 Fix connection failures

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

#### 7.4.4 Activate clusters in the deactived state

This topic describes how to activate the clusters in the deactived state. Run the following command on a PerfMaster node:

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}"
```

3.3 O&M description

> **Note:** ${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

#### 7.4.5 Troubleshoot program exceptions

This topic describes how to troubleshoot program exceptions.

**Troubleshoot the "partition has been lostPart" exception**

Log on to a PerfMaster node to troubleshoot the exception.

```bash
### Connect to a Docker container of PerfMaster and run the following reset commands:
curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_TS_CACHE_NAME" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=NOTIFY_MASTER_IGNITE_SHUTTING_DOWN" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=LOCK_MASTER_COMPETING" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CLUSTER_COMMAND" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC_LOCK" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CACHE_CODEC_ATOMIC_LONG" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=NODE_EXECUTE_COMMAND_RECORD" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=IGNITE_PERF_LOG_METADATA" curl "http://127.0.0.1:8080/admin/resetLostPartitions? igniteCluster=master&cacheName=CHECKPOINT_CACHE_NAME"
```

**Troubleshoot the "Failed to perform WAL operation" exception**

3.3 O&M description If the "Failed to perform WAL operation" message is returned, contact technical support or reset node data.

#### 7.4.6 Reset node data

This article describes how to reset node data.

**Precautions**

This operation deletes all data of a specific node. Monitoring data stored on the node is deleted and cannot be recovered. Proceed with caution.
1. Connect to the node or Docker container whose data you want to reset and run the
following command:

```
touch log/HOLD_START && ps aux|grep java|grep -v grep|awk '{ print $2}'|xargs kill -9 && rm -rf ignite/* && sleep 60 && rm -f log/HOLD_START &
```

2. Wait 3 minutes and run the following commands:

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}" curl "http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=${cluster}&apply=true"
```

> **Note:** ${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

#### 7.4.7 Dump logs

This topic describes how to dump logs.

**Background information**

Historical audit log data can be dumped for query.

**Precautions**

This feature is available only for ApsaraDB RDS for PostgreSQL instances that use standard 3.3 O&M description SSDs. Object Storage Service (OSS) buckets must be created to store audit logs. For more information about how to create a bucket, see Create a bucket in **Object Storage Service**
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

|   | Note In the preceding command, ppassql-HttpApiTest-INS-NAME-5 and ppassql- HttpApiTest-INS-NAME-6 are sample instances that are included in IP address whitelists for you to enable log dump. You can add actual instance names to the command based on your needs. If you want to configure multiple instances, perform the following operations: a. Add %22 before and after each instance name. b. Use %2C to concatenate instance names with %22 added before and after. c. Add the string in between %5B and %5D after whiteList. Sample configuration: whiteList=%5B%22Instance name%22%2C%22Instance name%22%2C%22Instance na me%22%5D |
|---|---|
|   | HttpApiTest-INS-NAME-6 |

3. Disable log dump.

```
pssh -h logworkerhosts 'curl "http://<The URL of the logworker cluster>:8080/admin/logTransferStore?/admin/logTransferStore? transType=close&accessKey=&accessSecret=&endpoint=&bucketName=&region="'
```

3.3 O&M description

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

Parse logs.

```
java -jar perf-tools-0.0.1.jar --input /logs/ppassql-HttpApiTest-INS-NAME-0 --output /logs/ppassql-HttpApiTest-INS-NAME-0/result.data --begin 1602592098 --interval 10800
```

Use a grep keyword and a vertical bar (|) to query logs.

```
java -jar ../perf-tools-0.0.1.jar --input /logs/ppassql-HttpApiTest-INS-NAME-0 --begi n 1602592098 --interval 10800 | grep incomplete
```
