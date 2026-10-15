---
title: "ApsaraDB for RDS Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260629"
pdf_pages: 196
source_pdf: "b97a06689dd1b45f_Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for RDS Operations and Maintenance Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93RDS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20RDS%20Operations%20and%20Maintenance%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# ApsaraDB for RDS Operations and Maintenance Guide

## Table of Contents

- 1 Architecture
  - 1.1 O&M architecture
  - 1.2 System architecture
- 2 文档标题缺失，请补全后重新导出
  - 2.1 Log in to ApsaraDB Operations and Maintenance System Smart Edition
  - 2.2 Overview of the homepage of ApsaraDB Operations and Maintenance System Smart Edition
  - 2.3 Instance management
    - 2.3.1 Overview of the instance details page
    - 2.3.2 View instance information
    - 2.3.3 Instance O&M operations
      - 2.3.3.1 Important Notes
      - 2.3.3.2 Recreate a secondary database
      - 2.3.3.3 Migrate an instance
      - 2.3.3.4 Upgrade the minor version
      - 2.3.3.5 Change the specification of a database instance
      - 2.3.3.6 Lock an instance
      - 2.3.3.7 Perform an HA switchover
      - 2.3.3.8 Modify the storage capacity
    - 2.3.4 Monitoring and alerting
    - 2.3.5 Diagnose an instance
    - 2.3.6 View status inspection records
    - 2.3.7 Manage audit logs
    - 2.3.8 Change records
    - 2.3.9 Manage tasks
    - 2.3.10 Backup management
    - 2.3.11 Data restoration
    - 2.3.12 Security configuration
    - 2.3.13 Parameter configurations
    - 2.3.14 O&M configurations
    - 2.3.15 Tag configurations
    - 2.3.16 Manage databases
    - 2.3.17 Account management
  - 2.4 Intelligent O&M
    - 2.4.1 Intelligent host diagnostics
    - 2.4.2 Information collection
    - 2.4.3 Automated script management
  - 2.5 Host management
    - 2.5.1 Host software package management
    - 2.5.2 Physical machine groups
  - 2.6 Software package management
- 3 文档标题缺失，请补全后重新导出
  - 3.1 Log in to ApsaraDB Operations and Maintenance System
  - 3.2 Home page
  - 3.3 Manage instances
    - 3.3.1 Instance list
    - 3.3.2 View instance details
    - 3.3.3 General instance O&M
      - 3.3.3.1 Important Notes
      - 3.3.3.2 Check instances
      - 3.3.3.3 Diagnose an instance
      - 3.3.3.4 Restart an instance
      - 3.3.3.5 Migrate an instance
      - 3.3.3.6 Upgrade the minor version
      - 3.3.3.7 Manage instance parameters
      - 3.3.3.8 Change specifications
      - 3.3.3.9 Change storage capacity
      - 3.3.3.10 Perform an HA switchover
      - 3.3.3.11 Lock an instance
      - 3.3.3.12 Backup and restoration
      - 3.3.3.13 Recreate a secondary database
      - 3.3.3.14 Manage instance tasks
      - 3.3.3.15 Disable instance allocation
    - 3.3.4 Other instance O&M
      - 3.3.4.1 Upgrade an instance from ApsaraDB RDS for MySQL Two-node Edition with Local Disks to PolarDB for MySQL Primary/Secondary Edition
      - 3.3.4.2 Common O&M operations for secondary PolarDB for MySQL nodes
      - 3.3.4.3 Perform zone-disaster recovery switchover for PolarDB for PostgreSQL Shared Storage Edition
      - 3.3.4.4 Query SQL information for PolarDB-X instances
      - 3.3.4.5 Handle failed PolarDB-X tasks
      - 3.3.4.6 Change PolarDB-X data node specifications
      - 3.3.4.7 Configure PolarDB-X instance resources
      - 3.3.4.8 Add proxy nodes to a Tair (Redis OSS-compatible) instance
      - 3.3.4.9 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance
    - 3.3.5 Manage instances in batches
      - 3.3.5.1 Migrate multiple instances at a time
      - 3.3.5.2 Modify multiple instance parameters at a time
      - 3.3.5.3 Modify DIY parameters for multiple instances at a time
      - 3.3.5.4 Modify Redis parameters for multiple clusters at a time
      - 3.3.5.5 Manage tasks in batches
      - 3.3.5.6 Manage batch task types
      - 3.3.5.7 Manage SQL templates
    - 3.3.6 Manage instance plan migration
    - 3.3.7 View the instance dashboard
  - 3.4 Host management
    - 3.4.1 Create a host
    - 3.4.2 Configure multiple hosts at a time
    - 3.4.3 View host information
    - 3.4.4 Physical machine group
    - 3.4.5 Manage host software packages
  - 3.5 Cluster management
    - 3.5.1 Configure cluster parameters
    - 3.5.2 Manage service types
    - 3.5.3 Manage service nodes
    - 3.5.4 Manage DB configuration templates
    - 3.5.5 Manage Fangcunshan clusters
    - 3.5.6 Manage locations
  - 3.6 Task management
    - 3.6.1 Manage interrupted tasks
    - 3.6.2 Manage temporarily closed tasks
    - 3.6.3 View workflow O&M information
  - 3.7 System management
    - 3.7.1 Feature Overview
    - 3.7.2 Change the unified storage location of logs
  - 3.8 Check important components
  - 3.9 Handle exceptions
  - 3.10 Appendix
    - 3.10.1 Log in to the Apsara Uni-manager Operations Console
- 4 Security maintenance
  - 4.1 Network security maintenance
  - 4.2 Account password maintenance
- 5 High-risk operations
- 6 Redline V4.3.3 O&M description
  - 6.1 Services provided by Redline Enterprise
  - 6.2 Paths of files in the Docker container of redline-perf
  - 6.3 Environment checks
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

ServiceTest Abs and Service Location Database Initialization Initialization

**Business**

**Foundation**

**System**

**On**

**On**

**NC**

**ECS**

InitCluster InitCluster InitCluster Pengine RdsApi MySQL MySQL DbPolaro DbMySQL DbMssql DbInit

**ApsaraDB RDS**

**PolarDB**

**ApsaraDB RDS for SQL**

**ApsaraDB**

**for MySQL**

**RDS for SQL**

**Server Management**

**Server**

**Service**

InitCluster Pengine RdsApi InitCluster TianLongServer TunnelServer 1/2 MySQL MySQL DbPgSql DbInit DbPgSql dbinit DBaaS DB initialization, such as

**ApsaraDB RDS**

**ApsaraDB RDS for**

ECS users

**ApsaraDB RDS**

**TianLong**

**MySQL Management**

**for**

**for**

**PostgreSQL**

**Service**

**PostgreSQL**

**Core**

YumServer Performance

**Services**

Collection Robot Aurora Stat Backup Whitelists MC API TASK TASK ApsaraDB Operations and Maintenance System BackendLocation and NameService Database Initialization and Environment Configuration Initialization

| Category | Component | Description |
|---|---|---|
| Business Foundation System | ServiceTest | Automated regression testing for ApsaraDB RDS features. |
|   | Abs and Service | The OpenAPI service for ApsaraDB RDS. |
|   | Location Initialization | Initialization of the Location configurations. |
|   | Database Initialization | DDL and DML configurations used to initialize ApsaraDB RDS Business Foundation System. |

| TianLong | dbinit | Initialization of TianLong. |
|---|---|---|
|   | TianLongServer | The TianLong service. |
|   | TunnelServer | An intermediate service that manages communications between ApsaraDB RDS and Elastic Compute Service (ECS). |
| ApsaraDB RDS for MySQL | InitCluster | Initialization of the cluster and host list. |
|   | DbMySQL | Database node initialization, database installation, and RPM package management. |
| ApsaraDB RDS for MySQL Management Service | PengineMySQL | The task flow service related to ApsaraDB RDS for MySQL. |
|   | RdsApiMySQL | API operations related to ApsaraDB RDS for MySQL. |
|   | McNode | The messaging agent node. |
|   | DbInit | DML configurations used to initialize ApsaraDB RDS for MySQL. |
| PolarDB | DbPolaro | The physical nodes of PolarDB. |
|   | InitCluster | The initialization of the cluster and host list. |
| ApsaraDB RDS for PostgreSQL | DbPgSql | Local SSDs: physical nodes of ApsaraDB RDS for PostgreSQL. Standard SSDs: deployed on ECS instances. |
|   | InitCluster | Initialization of the cluster and host list. |
| ApsaraDB RDS for SQL Server | DbMssql | Resources deployed on ECS instances. |
|   | InitCluster | Initialization of the instance and host list. |
|   | EcsImport2012Ent |   |
|   | EcsImport2016Ent |   |

|   |   | Operations and Maintenance Gu de·Architectur |
|---|---|---|
|   |   | Initialization of ECS images of different SQL Server versions. |
|   | EcsImport2012Std |   |
|   | EcsImport2016Std |   |
|   | EcsImport2017Ag |   |
| ApsaraDB RDS for SQL Server Management Service | DbInit | DML configurations used to initialize ApsaraDB RDS for SQL Server. |
|   | PengineMssql | The task flow service related to ApsaraDB RDS for SQL Server. |
|   | RdsApiMssql | API operations related to ApsaraDB RDS for SQL Server. |
|   | McNode | The messaging agent node. |
| Core services | YumServer | Deployment of host nodes for database services. |
|   | Robot | Automated O&M for database services. |
|   | The message center service. | The high-availability platform for database services. |
|   | Aurora | The high-availability platform for database services. |
|   | API | The backend core API service. |
|   | Stat | The actual executor of scheduled tasks for various monitoring and inspection activities. |
|   | ApsaraDB Operations and Maintenance System | The O&M platform for database services. |
|   | Performance Collection | Performance collection of earlier-version instances and hosts, and audit log collection of instances. |
|   | Backup | Full backup and incremental backup of databases. |

|   | TASK | Scheduling of the management task flow. |
|---|---|---|
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

You can use the ApsaraDB RDS console or API operations to create and delete instances, or switch instances between the internal network and Internet. All instance operations are scheduled, traced, and displayed as tasks.

## 2 文档标题缺失，请补全后重新导出

### 2.1 Log in to ApsaraDB Operations and Maintenance System Smart Edition

**and Maintenance System Smart**

**Edition**

This topic describes how to log in to ApsaraDB Operations and Maintenance System Smart Edition.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console and press
Enter. You can select a language from the drop-down list in the upper-right corner of the page.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, click **Products** and choose **Databases** > **ApsaraDB System**
**O&M Smart Pro Edition**.

### 2.2 Overview of the homepage of ApsaraDB Operations and Maintenance System Smart Edition

**ApsaraDB Operations and**

**Maintenance System Smart Edition**

The homepage of ApsaraDB Operations and Maintenance System Smart Edition displays global data, helps you locate exceptions, and provides an intelligent navigation system to enable you to quickly gain system insights and efficiently complete routine O&M. This topic describes the core modules on the homepage and the benefits from the perspective of customers.

**Key benefits of the homepage**

The homepage serves as a database O&M hub. It comes with the following core capabilities: Global control: displays the status of all instances, clusters, and tasks. Exception alerting: identifies system risks in real time and provides suggestions on how to fix them. Knowledge base: quickly navigates you to the official tutorials and user guides to improve your O&M efficiency.

**Global view section: View system health status within 10**

**seconds**

**System status overview**

Click a metric to view details.

| Metric | Description | Benefit |
|---|---|---|
| Health status | The health score (such as 85.2) and the health level (such as good). | Helps you quickly determine the health level of the system. |
| Key metrics | The total number of database engines, total number of clusters, total number of instances, and total number of hosts. | Helps you learn about the amount of resources and assess the O&M load. |

**Exception overview**

When the instance exception donut chart shows exceptions, you can click it to view the abnormal instances. The donut charts display exceptions from the following dimensions: instance exceptions, resource quota exceptions, host exceptions, system exceptions, cluster exceptions, instance backup exceptions, instance HA exceptions, and number of interrupted tasks. Visualization: donut chart + specific values (such as two HA failover exceptions) Benefits: Quickly identify the types and number of exceptions. Prioritize high-risk exceptions. Exceptions in yellow are normal and those in red are critical. Click a donut chart to navigate to the details page and handle the exceptions.

**Monitoring section: Master the key components**

**HA information**

Key metrics: number of HA instances, number of HA exceptions, and number of HA failovers. Dynamic trend chart: displays the trend of HA failover tasks. You can view the trend within the previous 1 hour, 4 hours, or 12 hours. Benefits: Monitor the high availability of databases. Identify the frequency of unexpected HA failovers based on the trend chart, such as a sharp spike within a short period of time. Ensure business continuity.

**Status of core control components**

Components: RDSAPI, Dukang, DBass, Perf, and Bak. Status: green (normal) and red (abnormal). Benefits: Confirm the status of the O&M platform.

**Instance and cluster management modules**

| Module | Key capability | Customer operation |
|---|---|---|
| Instance managemen t | Displays instance status by database engine, such as MySQL and Redis. Displays the distribution of chip types, such as Hygon and Phytium. | Click View more to manage instances. |
| Cluster managemen t | Displays the top five resources with the highest sales rate Monitors host status (normal or abnormal). Displays the distribution of host chips. | Identify heavy-load clusters based on top five ranking. |

**Task and risk management**

**Task management**

Task status donut chart: displays the total number of tasks (such as 304) and the proportions of running tasks, pending tasks, and interrupted tasks in real time. Task details list: displays key information about tasks, such as the task ID, task name, source, and duration. Customer operations: View the details of an interrupted task to identify the source that causes the interruption. Click **View more** to navigate to the corresponding page and handle the interrupted task.

**System inspection (worst-performing ranking and best-**

**performing ranking)**

Worst-performing top eight: database performance issues, such as pgxc_replication_stop and pgxc_conf_inconsistent. Best-performing top eight: configuration and security risks, such as docker_hostnames_unavailable. Radar chart: visualizes the severity levels of issues. Benefits: Prioritize high-risk issues in the best-performing ranking list. Mitigate potential system risks.

**Use cases: Identify databases that respond slowly**

1. Step 1: Check whether the health score of the system drops in the System Status Overview
section of the homepage.
2. Step 2: Check whether new instance exceptions are identified in the Overview of abnormal
data section.
3. Step 3: Look for the pgxc_replication_stop issue in the Black List TOP8 section.
4. Step 4: Navigate to the page of the corresponding feature from the details page of the
database instance and handle the issue. You can also look for a solution in the corresponding documentation of Apsara Stack.

**Best practices**

1. Routine check
Focus on the health score, overview of exceptions, and system inspection ranking lists. Suggested operations: Add newly identified exceptions to the O&M plan of the current day.
2. Response to emergencies
When an alert is triggered, check the statistics in the Overview of abnormal data and Task Management sections first. Key operations: Use quick navigation and a troubleshooting workflow repository to standardize emergency solutions.
3. Knowledge accumulation
When a new issue is identified, search for it by keyword on the homepage, such as an excessive number of connections. Benefits: Automatically matches topics in the knowledge base to avoid making the same mistake.

### 2.3 Instance management

#### 2.3.1 Overview of the instance details page

The instance details page of ApsaraDB O&M System Smart Pro Edition is a key feature module. This page displays and allows you to manage the status, configurations, performance metrics, and O&M operations of a database instance.

**Key features**

**Comprehensive information display**: The instance details page displays the basic
information, specifications, network topology, and host information of an instance in a centralized manner. Donut charts are provided to show the usage of resources, such as CPU utilization, memory usage, disk usage, input/output operations per second (IOPS) utilization, and number of connections.
**Visualized topology**: Logical and physical topology views are provided to graphically
display the organizational structure and deployment relationships of instances.
**Multi-dimensional monitoring and alerting**: A dynamic monitoring dashboard is
provided to display monitoring metrics in line charts. You can filter monitoring metrics and alerts by node or time range.
**Intelligent diagnostic tool set**: The tool set provides features such as 360 diagnosis,
special diagnosis (such as analysis of slow SQL query logs, diagnosis of instance stutters and slow responses, real-time information check, and InnoDB status check), and status checks to help you quickly identify performance bottlenecks and root causes of failures.
**Audit logs and change records**: You can query and archive SQL audit logs, and
download archived SQL audit logs. The system records 10 types of logs that cover all operations and changes to your instance, including general logs, high availability (HA) logs, API logs, and management logs.
**Backup and restoration management**: You can manage data backup policies and binary
log backup policies. Restoration by backup set and point-in-time recovery (PITR) are supported.
**Security and parameter configuration**: You can manage IP address whitelists, security
groups, kernel parameters, control parameters, O&M configurations, and instance tags to ensure instance security and compliance.
**Database and account management**: The system allows you to manage the database
list, user accounts, and system accounts of an instance. You can create and delete accounts, grant permissions to accounts, and manage account passwords.

**Scenarios**

Routine O&M inspection: You can quickly view the health status, resource usage, and performance metrics of your instance. Troubleshooting: You can precisely identify the root causes of failures through 360 diagnosis, special diagnosis, and audit logs. Configuration management and changes: You can modify instance configurations such as backup policies, security configurations, and runtime parameters. Data security management: You can perform data security-related operations such as backup and restoration, and account permission management.

**Usage notes**

**Limits**

Currently, the instance details page of ApsaraDB O&M System Smart Pro Edition displays the details of only MySQL instances. For more information, see the following table. For more information about the O&M operations on other types of instances, see the Instance management section of ApsaraDB Operations and Maintenance System - Operations and Maintenance Guide.

| Item | Description |
|---|---|

| Visibility of the Physical Topology tab | The Physical Topology tab is displayed only for MySQL instances that do not use the new architecture. |
|---|---|
| Visibility of the Instance View menu | The Instance View menu is displayed only when the current instance is the primary instance. |
| MaxScale logs | MaxScale logs are displayed only for MySQL instances. |
| Real-time instance information | The real-time instance information is displayed only for MySQL instances. |
| Real-time status of InnoDB instances | The real-time InnoDB status is displayed only for MySQL instances. |
| InnoDB status | The InnoDB status is displayed only for MySQL instances. |
| Host connectivity test | You can perform a host connectivity test only on MySQL instances. |
| Limitation on SQL statement execution | Only single-line SQL statements are supported, and SQL statements cannot contain line breaks. You must switch a PolarDB child instance to the primary instance to execute SQL statements. |
| Maximum number of returned rows after an SQL statement is executed | Valid values: 1 to 10000. |
| Diagnosis of instance stutters and slow responses | Up to 50 diagnosis records are displayed on each page. |
| Audit log archiving | You can archive and store audit logs in Object Storage Service (OSS). A confirmation message appears before the operation continues. |
| Account password complexity | The password must be 8 to 32 characters in length and contain at least three of the following types: uppercase letters, lowercase letters, digits, and special characters. |

**Safety precautions**

**Warning**

Executing SQL statements is risky. Exercise caution when you perform this operation. A confirmation message appears before you perform a Kill session operation for multiple diagnostic items on the special diagnosis page. If you terminate the session for multiple diagnostic items at a time, your business may be affected. Deleted databases and accounts cannot be restored. A confirmation message appears before the deletion operation continues. If you modify kernel parameters, you must restart the instance for some kernel parameters to take effect. We recommend that you perform this operation during off-peak hours.

**Getting started**

**Step 1: Go to the instance details page**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. You are redirected to the instance details page. The **Basic information** page is displayed
by default.

**Step 2: View the basic information of an instance**

On the **Basic information** page, you can view the relevant information in the following sections:
**Basic information**: This section displays the basic information about the instance,
including instance ID, instance name, database type, database version, instance status, locked state, region, zone, cluster name, and data center.
**SLB information**: This section displays the address and port number of the Server Load
Balancer (SLB) instance that is associated with the instance.
**Performance Information**: This section displays the performance information about the
instance in donut charts, including CPU utilization, memory usage, disk usage, IOPS utilization, and number of connections. The **Performance Monitoring** and **Resource allocation** buttons are provided on the right side of this section.
**Instance Specifications**: This section displays the instance specifications, including
number of CPU cores, memory size, disk capacity, and maximum number of connections.
**Host Information**: This section displays the details about the physical host where the
instance resides. You can perform a connectivity test on MySQL instances.
**Network information**: This section displays the network configuration information about
the instance, including VPC, vSwitch, internal endpoint, and public endpoint.

**Step 3: View monitoring metrics**

1. In the left-side navigation pane of the instance details page, click **Monitoring Alarm**.
2. On the monitoring dashboard, view the monitoring metrics, such as CPU utilization, memory
usage, queries per second (QPS), transactions per second (TPS), and network traffic.
3. Select a time range to view historical data.
You can select the monitored nodes at the instance level or child node level for each metric panel. The metrics are displayed in line charts.

**FAQ**

**Q: Why is the Physical Topology tab not displayed?**

A: The Physical Topology tab is displayed only for MySQL instances that do not use the new architecture. If your instance is not of the MySQL type or does not use the new architecture, this tab is not displayed.

**Q: Why is the Instance View menu not displayed?**

A: The Instance View menu is displayed only when the current instance is the primary instance. If the current instance is a read-only or secondary instance, this menu is not displayed.

**Q: What do I do if the notinwhiteList message appears when I**

**execute an SQL statement?**

A: Add the current IP address to the IP address whitelist of your instance. Go to the instance details page. In the left-side navigation pane, click **Security Configuration > ip whitelist** tab. On the page that appears, add the current IP address to the IP address whitelist and execute the SQL statement again.

**Q: Why are multi-line SQL statements not supported?**

A: Only single-line SQL statements are supported, and SQL statements cannot contain line breaks. Merge multi-line SQL statements into a single-line SQL statement before you execute it.

**Q: What do I do if an SQL statement fails to be executed on a**

**PolarDB child instance?**

A: You must switch a PolarDB child instance to the primary instance to execute SQL statements. In the Master Library/Standby Library section on the Execute SQL tab, select Master Library and click Execute to execute the SQL statement again.

**Q: Will my business be affected if I perform a Kill session**

**operation?**

A: If you perform a Kill session operation, the selected session process is terminated. This may affect your ongoing business operations. We recommend that you perform this operation after you confirm that the session does not affect your core business. A confirmation message appears before the operation continues. Exercise caution when you perform this operation.

**Q: What do I do if the status data disappears after I switch**

**from the Real-time status of Innodb instances tab to another**

**tab?**

A: The status data collection automatically stops when you switch to another tab. After you return to the Real-time status of Innodb instances tab, you must manually click **START** to restart status data collection.

**Q: What can I do if audit logs fail to be archived?**

A: To resolve this issue, check the following items: Verify that the OSS storage configuration is correct. Verify that the data volume of logs under the filter conditions does not exceed the limit. On the SQL Archiving History tab, view the cause of the failure, handle the failure as prompted, and then archive the audit logs again.

**Q: What do I do if the account password fails to be changed?**

Verify that the account password meets the following complexity requirements: The password must be 8 to 32 characters in length and contain at least three of the following types: uppercase letters, lowercase letters, digits, and special characters. If the failure persists, contact the administrator to check whether the account status is normal.

**Q: How to view the consistency check results of the primary**

**and secondary instances?**

A: Go to the instance details page. In the left-side navigation pane, click **Change record >**
**Primary and secondary inconsistency check** tab to view the check results. For a task in
the Not Started, Failed, Interrupted, or Checking state, you can go to the **Parameter**
**configuration** page to check the configurations.

**Q: What is the purpose of specifying the expiration time for a**

**tag?**

A: You can specify the expiration time for some tags. When the specified expiration time is reached, the tag value may become invalid or a specific behavior may be triggered. When you edit a tag, you can use the date picker to specify the expiration time for the tag. The specified expiration time can be accurate to hour, minute, and second. You can also leave the Expiration Time parameter blank. In this case, No is displayed for the Expiration Time parameter.

#### 2.3.2 View instance information

This topic describes how to view the basic information (including instance type, performance, and network type) and the logical and physical topology of an instance on the instance details page in the ApsaraDB O&M System Smart Pro Edition console. This topic also describes how to view the details of child instances of a primary instance.

**Basic instance information**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. The **Basic information** page is displayed by default. This page consists of multiple
information sections that are arranged vertically.
3. You can view the relevant information in the following sections:
**Basic information**: This section displays the basic information about the instance, such
as instance ID, instance name, database type, database version, instance status, locked state, region, zone, cluster name, and data center. You can click View to view details about the region and zone of the instance.
**SLB information**: This section displays the address and port number of the Server Load
Balancer (SLB) instance that is associated with the instance.
**Performance Information**: This section displays the performance information about the
instance in donut charts, including CPU utilization, memory usage, disk usage, IOPS utilization, and number of connections. The disk usage is a percentage of used disk capacity relative to total disk capacity. The **Performance Monitoring** and **Resource**
**allocation** buttons are provided on the right side of this section.
**Instance Specifications**: This section displays the instance specifications, including
number of CPU cores, memory size, disk capacity, and maximum number of connections.
**Other information**: This section displays the supplementary configuration information
of the instance.
**Host Information**: This section displays the details about the physical host where the
instance resides. You can perform a connectivity test on MySQL instances.
**Network information**: This section displays the network configuration information
about the instance, including VPC, vSwitch, internal endpoint, and public endpoint.

**Instance topology**

**View the logical topology**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Instance topology**.
3. The Logical topology tab is displayed by default.
The Logical topology tab displays the logical organizational structure of the instance. Different node types are shown in different colors. On this tab, you can perform the following operations: Search for instances by instance name. Show or hide the legend description. Click the Refresh button to update the topology data.

**View the physical topology**

The physical topology is provided only for instances that meet the following requirements: The database engine of the instance is MySQL. The instance does not use a new architecture.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Instance topology**.
3. On the page that appears, click the **Physical topology** tab.
The Physical topology tab shows the physical deployment structure of the instance. Lines in different colors indicate different link types:

| Line color | Link type |
|---|---|
| Purple | Business access link |
| Orange | Access control and detection link |
| Blue | Replication link |

| Cyan | Backup link |
|---|---|

**Instance view**

**View the list of child instances**

To view the list of child instances under the primary instance, make sure that **the current**
**instance is the primary instance**.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Instance View**.
3. View all associated child instances under the primary instance. These child instances are
grouped and displayed by instance type. Instance types include primary instance, read-only instance, and secondary read-only instance. Each child instance contains the following sections:
**Instance information**: This section displays the information about the instance,
including instance name, cluster, and locked state. You can copy the instance name.
**Host list**: This section displays the information about all hosts, including host IP address,
port number, master/slave role, and host instance ID. You can click **View details** to check the connectivity.

#### 2.3.3 Instance O&M operations

##### 2.3.3.1 Important Notes

**Read before operation**

**Warning**

Some operations described in this section, such as instance restart, minor engine version update, and backup and restoration, involve core changes to the underlying infrastructure. These operations are irreversible or high-risk. Improper operations may lead to data loss, service interruption, or performance jitter. Before you perform any O&M operations, carefully read the relevant tutorials and the precautions and key risk reminders on the console interface. If necessary, perform operations under the guidance of Alibaba Cloud professional technicians. Once you click Submit, Confirm or similar commands, it is deemed that you have been fully aware of all potential risks and voluntarily bear all the consequences arising therefrom. Proceed with caution.

##### 2.3.3.2 Recreate a secondary database

If an exception occurs in the secondary database, you can recreate the secondary database to ensure the continuity of the primary/secondary HA architecture.

**Use scenarios**

You must recreate a secondary database in the following scenarios: The secondary database fails and cannot provide services. Data in the secondary database is corrupted, which causes data inconsistency between the primary and secondary databases or interrupts data synchronization. You need to replace the server where the secondary database resides due to reasons such as hardware upgrades, migration, and resource adjustment.

**Usage notes**

Secondary database recreation does not affect the operations performed on the primary database or services in the production environment. If you want to recreate the secondary database due to data inconsistency between the primary and secondary databases, you must **trigger a backup of the primary database** first in case the secondary database becomes unavailable. We recommend that you back up the primary database during off-peak hours. You can go to the **Data backup**
**management > Backup policy** page and click **Create a temporary backup** to back up
the primary database. For more information, see Backup management.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. In the left-side navigation pane, choose **Instance Management > Instance list**.
3. Click the name of the desired instance to go to the **Basic information** page.
You can enter a keyword into the search box to quickly find the desired instance. You can also click Advanced Filter to customize filter conditions to locate the instance.
4. In the upper part of the page, click **Recreation [Secondary Database Recreation |**
**Node Recreation]**.
5. In the dialog box that appears, follow the instructions to complete the required settings.
The following table describes the parameters. The actual parameters displayed in the console prevail.

| Parameter | Description |
|---|---|
| Force Primary Node Backup | By default, this option is not selected. You can specify whether to require the task flow to initiate the backup operation from the physical host where the primary database is located (not the physical host where the secondary database is located). That is, the backup set must be generated by the primary database. Note If the secondary database or its host experiences performance exception or access exception, we recommend that you select Force Primary Node Backup. This prevents initiating backups from the secondary database. Otherwise, the task flow will be interrupted or fail. |

| Please select the host to be rebuilt | Select the host. Make sure that the instance role of the selected host is a secondary database, such as slave . |
|---|---|
| Whether to enforce alignment of the kernel iteration with the instance master replica | Select this option based on your business requirements. Note If you select Yes, the target instance is forced to not use other minor engine versions. If the minor engine version of the primary and replica nodes is unavailable in the target instance, the recreation operation fails. We recommend that you refer to Upgrade the minor engine version and upgrade the minor engine version of the instance in advance. If you select No, the target instance preferably uses the minor engine version of the primary and replica nodes. If the minor engine version is unavailable in the target instance, upgrade the instance to the latest minor version. |
| Select Local Recreation or Cross-Host Recreation. | If the cluster has sufficient available resources, we recommend that you select Cross-Host Recreation. If the operating system or file system of the physical host where the secondary database is located is abnormal, you must select Cross-Host Recreation. Important In this case, before you initiate a secondary database recreation, you must shut down the secondary database or power off the faulty host. This prevents system environment exceptions on the secondary database from affecting the execution of task flow steps. Otherwise, an unavoidable task interruption will occur. If the cluster mode of the selected host is Host Pair, you must select Local Recreation. |

| Specify Host | If you select Cross-Host Recreation in the previous step, you can specify a data center or host. Note In most cases, you do not need to specify a host, and migration is scheduled by the resource manager. For more information, see the additional description in the blue box in the console. Click Troubleshooting host reasons to view the reasons why a physical host is excluded from the list of available hosts. |
|---|---|

6. After the configuration is complete, click **Submit**.
7. Then, you can view the task progress on the **Task Management** page until the task is
completed. If the task is interrupted, contact Apsara Stack technical support. For more information about how to view the task progress, see the Task management topic.

##### 2.3.3.3 Migrate an instance

ApsaraDB Operations and Maintenance System Smart Edition allows you to migrate instances across zones or subdomains. You can migrate instances in scenarios such as resource scheduling, disaster recovery drilling, and hardware upgrades. You can also choose to migrate the primary nodes, standby nodes, and read-only nodes.

**Preparations**

Before you submit a migration request, we recommend that you record the host information of the current instance. Check for ongoing tasks or exceptionally interrupted tasks on the physical instance (primary node, standby node, or read-only node) to migrate and the logical instance to which the physical instance belongs. If such tasks are identified, complete or delete them before you migrate the instance.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. In the left-side navigation pane, choose **Instance Management > Instance list**.
3. Click the name of the desired instance in the **User instance name** column to go to the
details page.
4. In the upper part of the **Basic information** page, click **Migrate**.
5. Configure the destination and click **Submit**.
The migration configuration varies depending on the database engine used. The actual migration configuration in the console prevails. You cannot migrate instances deployed in virtual private clouds (VPCs) to random zones. The vSwitch ID is required during cross-zone migration. The primary and standby nodes must be deployed in the same zone in primary zone mode. Instances for sale can be migrated only to the sales subdomain. Internal instances can be migrated only to the ODBS subdomain.

| Parameter | Description |
|---|---|
| VIP switching time | Operation and maintenance time switching: The migration is performed during a predefined maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic information page. Switch now: The migration immediately takes effect and may affect your business. Specify time: You can specify a time point for the migration. |
| Disk type | Select a disk type based on your business requirement. You can also skip this parameter. Valid values: SSD SATA Hybrid Storage |
| Region | Specify the region of the source instance to migrate. The actual regions available in the console prevail. |
| Subdomain | Select the destination subdomain. |
| Migration reason | Enter the reason of the migration for audit and ticket tracking. |

| Whether to enforce kernel iteration alignment with source instance master replica | Control the minor engine version of the destination host. Valid values: Yes (forced alignment): The destination host must use the same minor engine version as the source instance. If the version is unavailable, the migration fails. We recommend that you check whether the minor engine version is available on the destination host before the migration. No (intelligent adaptation): The system preferentially attempts to match the minor engine version of the source instance. If the version is unavailable, the latest minor engine version on the destination host is used. Note If you want to migrate a read-only node, specify the primary node corresponding to the read-only node as the source instance. |
|---|---|
| Specify host | Specify a destination host. If you manually specify a destination physical host, the success rate of the migration will be low. Do not specify a destination host (recommended): If you do not specify a destination host, the resource manager automatically allocates the optimal host. The success rate of the migration will be high. Note Click Troubleshooting host reasons in the Description section to view the reason why certain physical hosts are excluded. |

**View the migration progress**

After you click **Submit**, you are redirected to the **Task Management > Migration Task** page. You can view the migration progress on this page.

**View host information before and after the migration**

Navigate to the **Basic information** page of the instance. In the **Host Information** section, view the host ID before the migration and the host ID after the migration.

##### 2.3.3.4 Upgrade the minor version

ApsaraDB Operations and Maintenance System Smart Edition allows you to securely upgrade the minor version of database instances. Minor version upgrades usually involve performance optimization, new features, and fixes. They can ensure the stability and performance of databases.

**Prerequisites**

The instance whose minor version you want to upgrade must be a non-temporary instance and in both In Use and Unlocked states.

**Usage notes**

If you do not specify a minor version, the system upgrades the instance to the latest version by default. When you update the minor engine version of your PolarDB for MySQL V2.0 cluster, applications may temporarily disconnect from your cluster for 30 seconds. We recommend that you update the minor engine version during off-peak hours or make sure that your application is configured to automatically reconnect to the cluster. After the minor version of an instance is upgraded, you cannot downgrade the instance to an earlier version. Exercise caution when you perform this operation.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. In the left-side navigation pane, choose **Instance Management** > **Instance list**.
3. Find the desired instance in the instance list and click its name in the **User instance name**
column to go to the details page.
4. In the upper part of the **Basic information** page, click **Version Upgrade**, configure the
following parameters, and then click **Submit**. This topic uses PolarDB for MySQL Primary/Secondary Edition as an example. The parameters and page may vary depending on the database engine used. The actual configuration in the console prevails.

| Parameter | Description |
|---|---|
| Database Version | The major version of the current instance. The system supports only minor version upgrades within the same major version. |
| Small version number | Select the minor version to which the instance will be upgraded.T he current minor version of the instance will be displayed on the right side for comparison. |
| Specify method | Operation and maintenance time switching: The upgrade is performed during the specified maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic information page of the instance. Switch now: The upgrade immediately takes effect and may affect your business. Specified time switch: The upgrade is performed at the scheduled time, which requires manual configuration. |

**View the upgrade progress**

After the upgrade task is initiated, you can go to the **Task Management** page to view the upgrade progress.

##### 2.3.3.5 Change the specification of a database instance

**instance**

This topic describes how to change the specification of a database instance.

**Preparations**

Before you change the specification of a database instance, make sure that you have completed the following tasks: Instance status verification: Make sure that the instance is in the Running state and no other tasks (such as backup, migration, and restart) are in progress. Data backup: We recommend that you manually create a temporary snapshot or full backup in advance so that you can quickly restore data when an exception occurs.

**Usage notes**

| Perform this operation only during off-peak hours. | A temporary disconnection lasting 5 to |
|---|---|
| 30 seconds may occur during the operation. Make sure that the application has an |   |
| automatic reconnection mechanism to avoid business interruptions. |   |

We recommend that you forcefully align the minor engine versions (enabled by default) in case compatibility issues occur due to minor engine version inconsistency among cluster nodes. If the desired specification is unavailable, you must click Exclude specification reasons to view the reason. Do not attempt to change the specification directly. After you submit the specification change task, monitor the task progress in real time until it is complete. If the task is interrupted or stuck, contact Apsara Stack technical support. Strictly abide by the review workflow and compare the CPU, memory, and disk specifications before and after the change. This helps prevent resource waste or service degradation caused by user errors.

**Use scenarios**

Performance upgrade: Meet business development requirements, withstand unexpected traffic spikes, or resolve issues such as slow response or queue congestion caused by CPU or memory bottlenecks. Cost optimization: Release idle resources in low-load or non-core environments by downgrading the specification to reduce O&M costs. Storage expansion: Expand the storage space when the disk usage reaches the threshold to prevent write locks or service interruptions. Version management: Use the specification change mechanism to forcibly align minor engine versions in order to eliminate compatibility and stability risks posed by version inconsistency among cluster nodes. Fault fixing: Modify the specification of the target node to restore the standard configuration or unify the cluster architecture after an instance is migrated or an HA switchover is performed.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. On the **Instance Management > Instance list** page, click the name of the desired
instance.
3. On the Basic information page, choose **More > Specification change**.
4. On the page that appears, specify whether to align the minor engine versions, configure
the **Storage space (GB)**, **Instance specifications**, **Switch Mode**, and **Reason for**
**change** parameters, and then click **Next step**.
Whether to align with the minor engine version of the source primary and replica nodes: If you select Yes, the target instance is forced to not use other minor engine versions. If the minor engine version of the primary and replica nodes is unavailable in the target instance, the specification change operation fails. We recommend that you refer to ApsaraDB Operations and Maintenance System O&M Guide and upgrade minor engine version of the instance. For more information about how to update the minor engine version, see Upgrade the minor version. If you select No, the target instance preferably uses the minor engine version of the primary and replica nodes. If the minor engine version is unavailable in the target instance, upgrade the instance to the latest minor version.
5. In the **Audit comments** section, confirm the comments and click **Audit changes**.
6. After you complete the configuration, you can view the task progress on the **Task**
**Management** page until the task is complete. If the task is interrupted, contact Apsara
Stack technical support. For more information about how to view the task progress, see the Manage instance tasks topic.

##### 2.3.3.6 Lock an instance

This topic describes how to lock an instance to help you resolve issues.

**Usage notes**

Make sure that operations are performed during off-peak hours and your applications have an automatic reconnection mechanism to handle unexpected interruptions. For full-disk locks, you must first clear or expand the disk space. For rollback locks, forced restarts are strictly prohibited, and the root cause (such as high resource usage or failed changes) must be resolved before you attempt to unlock the instances. After you submit a task to lock an instance, you must continuously monitor the progress. If the task is interrupted or stuck, it is strictly prohibited to retry the task without investigating the root cause. In this case, immediately contact Apsara Stack technical support to prevent a deadlock. After an instance is locked, it becomes read-only and your business is affected. You must perform this operation within an O&M window and pay close attention to the potential risks during the operation.

**Use scenarios**

This topic lists only some use scenarios for reference. In other scenarios, lock your instance based on the actual situations. Observation period for business undeployment: Before you delete an instance, manually lock the instance and set the observation period to more than seven days. Make sure that the business has no implicit dependencies or does not receive any complaints before you delete the instance. This helps prevent accidental loss of production data. Emergency isolation and damage control: In the event of attacks, abnormal SQL queries, or data tampering, manually lock the instance immediately and close all connections. This prevents the spread of the faults and saves time for troubleshooting. Self-protection triggered by resource exhaustion: When the disk space is exhausted or a hardware fault occurs, the system automatically triggers a full-disk lock or migration lock. This prevents metadata corruption and ensures strict data consistency. Rollback protection for high-risk changes: When a specification change or upgrade fails, the system automatically triggers a rollback lock to freeze the instance state. This ensures that data is not in an intermediate state.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. On the **Instance management > Instance list** page, click the name of the desired
instance.
3. On the Basic information page, choose **More > Locking an instance**.
4. Specify **Lock mode** and **Locking reason** and click **Submit**.
5. View the task progress on the **Task Management** page until the task is complete. If the
task is interrupted, contact Apsara Stack technical support. For more information about how to view the task progress, see the Manage instance tasks topic.

##### 2.3.3.7 Perform an HA switchover

This topic describes how to manually perform an HA switchover.

**Background information**

In most cases, when the primary node fails, the system automatically performs an HA switchover to restore services. Manual HA switchovers are usually performed in proactive O&M scenarios. This means manually switching the business traffic from the current primary node to the secondary node and promoting the secondary node to the new primary node when no failover is triggered.

**Preparations**

Before you perform an HA switchover, make sure that the following items are checked: Instance status verification: Make sure that the instance is in the Running status and no other operations (such as specification change, restart, or backup and restoration) are being performed. Primary and secondary node synchronization: Make sure that data is synchronized to the secondary node as normal. Make sure that the latency is zero or within the acceptable range. The suggested latency is less than 1 second. If data is synchronized to the secondary node with a delay, forceful switchovers may result in data loss. Secondary node health check: Make sure that the host of the secondary node has sufficient resources, the network connectivity is normal, and no hardware alerts are generated.

**Usage notes**

We recommend that you perform this operation during off-peak hours and ensure that an automatic reconnection mechanism is used to avoid network jitters. After a switchover, you need to monitor the task progress in real time until the task is complete. If the task is interrupted or stuck, immediately contact Apsara Stack technical support. We recommend that you wait until data synchronization between the primary and secondary nodes is complete before you perform a switchover.

**Use scenarios**

Maintenance or upgrade of underlying resources: When the physical machine, host, or storage device of the primary node needs to be suspended for maintenance, firmware upgrade, or migration, manually switch services to the secondary node in advance to avoid service interruptions. Risk elimination: When the primary node experiences hardware faults or network jitters, but the node is still up, switch the services to the secondary node to eliminate the risk of business interruptions.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. On the **Instance Management > Instance list** page, click the name of the desired
instance.
3. On the Basic information page, choose **More > HA switch**.
4. After you confirm that the information of the primary and secondary nodes, specify the
**Switching method** and **Specify method** parameters and click **Submit**.
Switch now: This method is used in emergency scenarios. Operation and maintenance time switching: This method is suitable for routine O&M, such as O&M in the early morning every day. The O&M task is automatically executed. Specified time switch: This method is suitable for specific time windows, such as application release.
5. After you complete the configuration, you can view the task progress on the **Task**
**Management** page until the task is complete. If the task is interrupted, contact Apsara
Stack technical support. For more information about how to view the task progress, see the Manage instance tasks topic.

**Verify the result**

After Step 4 is complete, the IP addresses and ports are reassigned to match the new primary and secondary roles. The HA task flow is complete.

**Perform a rollback**

Follow the same procedure to swap the roles of the primary and secondary nodes.

##### 2.3.3.8 Modify the storage capacity

This topic describes how to modify the storage capacity of an instance.

**Usage notes**

The primary node is in the Running state and has no pending modification tasks, such as upgrade, migration, and backup tasks. We recommend that you perform this operation during off-peak hours to avoid extreme network fluctuations. If you want to shrink the storage capacity, make sure that the new storage capacity is not smaller than the current storage usage of the instance plus 20 GiB. The storage capacity changes take effect on the logical instances of a cluster. After you modify the storage configuration of the primary node, the changes are synchronized to all read-only and standby nodes in the cluster. Proceed with caution.

**Use scenarios and issues addressed**

**Expand the storage capacity**

Support business growth: As business data grows rapidly, and the disk usage approaches the threshold (such as 80%), you need to immediately expand the storage capacity of the database in case your database instance enters the read-only state or your business is interrupted. Reserve buffer space: You need to reserve sufficient write buffer space before promotional events, batch writes, or historical data archiving. Eliminate performance bottlenecks: In certain scenarios, a larger storage capacity usually means a higher IOPS value (depending on the instance specifications). You can expand the storage capacity of your database instance to improve its throughput.

**Shrink the storage capacity**

Cost optimization: After business data cleanup, such as deletions of large tables and archiving of historical data, the actual storage usage is usually lower than the current storage capacity. In this case, you can shrink the storage capacity to release idle storage resources and reduce the monthly payment. Avoid resource waste: Shrink the storage capacity to the actual storage usage level to avoid resource waste, which is caused by inaccurate resource assessment at the early stage of the project.

**Procedure**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. On the **Instance Management > Instance list** page, click the name of the desired
instance.
3. On the Basic information page, choose **More > Storage space changes**.
4. In the dialog box that appears, enter the new storage capacity and click **Submit**.

**View the details of a task**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
2. On the **Instance list > Task Management** page, you can view the status of tasks.
You can view the details of all tasks, interrupted tasks, and paused tasks. You can also customize the columns displayed in the task list.

#### 2.3.4 Monitoring and alerting

This topic describes how to view information and perform operations on the performance monitoring dashboard of an instance in the ApsaraDB O&M System Smart Pro Edition console. You can dynamically select monitoring metrics, change the monitoring granularity of a monitored node, select a time range, and quickly search for specific metrics from the full monitoring metric directory. Through these operations, you can fully understand the status of your instance.

**View performance monitoring data**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Monitoring Alarm**.
3. On the monitoring dashboard, perform the following operations based on your business
requirements:
**Select monitoring metrics**: The system displays available monitoring metrics, such as
CPU utilization, memory usage, queries per second (QPS), transactions per second (TPS), and network traffic, based on the instance type.
**Change the monitoring granularity of monitored nodes** : The system allows you to
select the monitoring granularity for each metric panel. You can switch between instance-level monitoring and child node-level monitoring.
**Select a time range**: You can specify a time range to view historical performance data
in different periods of time.
**View the full monitoring metric directory**: Click the
icon in the middle-right part of the page to show the full monitoring metric directory. You can enter keywords to quickly search for and locate the monitoring metrics.

#### 2.3.5 Diagnose an instance

This topic describes how to perform comprehensive health checks and performance analysis on a database instance in the ApsaraDB O&M System Smart Pro Edition console, including viewing 360 diagnostic reports, querying MaxScale logs, monitoring real-time sessions, checking InnoDB status, analyzing slow SQL query logs, diagnosing instance stutters and slow responses, executing SQL statements online in a safe manner.

**View 360 diagnostic reports**

You can quickly know about the overall health status of an instance by viewing the 360 diagnostic report of the instance.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **360 diagnosis**.
3. On the page that appears, view the diagnostic details in the following sections:
**Basic information**: This section displays the summary of diagnostic results, which are
indicated by three colors. Green represents normal, orange represents warning, and red represents abnormal.
**Disk Space Details (MB)**: This section provides a time series line chart to display the
trend of disk space changes. By default, the disk space change data of the last two days is displayed in the line chart. You can specify a time range for the line chart.
**Instances on the same host** : This section displays the information about other
instances that reside on the same host as the current instance in a table, including the host IP address, host port, instance name, instance ID, disk usage, and database type. You can click the host IP address to go to the host details page, and click the instance name to go to the instance details page.
**HA switch record**: This section displays the history of high-availability (HA) switchovers.
**Task record**: This section displays the task execution records associated wit the
instance.
**O&M Records**: This section displays the O&M operation logs of the instance in a table.

**Special diagnosis**

**View MaxScale logs of an instance**

You can view the proxy-layer MaxScale logs of an MySQL instance. **This feature is available**
**only for MySQL instances**.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Instance MaxScale Logs** tab.
4. Optional. Specify the following filter conditions:

| Filter condition | Description |
|---|---|
| Start time/End time | The start/end time of the log that you want to view. The start and end time can be accurate to hour, minute and second. |
| Log Level | The level of the log that you want to view. Select info/notice/warning/error from the drop- down list. |
| Log content | The content of the log that you want to view. Enter a keyword to search for logs. |

5. View the log list, which contains the following fields:

| Field | Description |
|---|---|
| Log time | The time when the log was generated. |
| Log Level | The level of the log. The value of this field is fixed to info/notice/warning/error. |
| Log content | The specific information in the log. |

**View the real-time information of an instance**

You can view the list of session processes that are being executed on MySQL instances. **This**
**feature is available only for MySQL instances**.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Instance real-time information** tab.
4. A line chart of the number of connections is displayed at the top of the page, and a session
list is displayed at the bottom of the page.
5. Optional. Specify the following filter conditions:

| Filter condition | Description |
|---|---|
| Command | The command type. The following command types are provided: All, Query, Sleep, and Connect. By default, Query is selected. |
| State | The state of the thread. More than 20 thread states are provided. Select a state from the drop-down list. |
| Time (> =) | The threshold for session execution time. Unit: seconds. Enter a value for this parameter to filter sessions whose execution time exceeds the specified value. |
| Info | Keyword fuzzy match is applied to SQL statements. Enter a keyword. |
| Host | IP address or port number fuzzy match is applied to the host. Enter an IP address or a port number. |

6. View the session list, which contains the following fields:

| Field | Description |
|---|---|
| USER | The name of the connected user. |
| HOST | The IP address of the client. |
| Thread ID | The identification number of the session thread. |
| DB | The current database. |
| COMMAND | The command type, including Query, Sleep, and Connect. |

| TIME | The elapsed time of the session execution duration. Unit: seconds. |
|---|---|
| STATE | The state of the thread. |
| INFO | The content of the SQL statement that is being executed. |

7. Optional. **Kill multiple sessions at a time**: Select multiple sessions and click **Kill**
**session**. In the message that appears, click OK. This way, the selected sessions are
terminated at a time.

**View the real-time status of an InnoDB instance**

The key operating metrics of the InnoDB storage engine are collected and displayed in real time. **This feature is available only for MySQL instances** .
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Real-time status of Innodb instances** tab.
4. In the operation section, specify the data collection interval. Unit: seconds. Valid values: 1
to 300.
5. Click **START** to start real-time data collection using the polling method.
The following metric groups are displayed on the page in a terminal-like style (dark theme). Abnormal values are highlighted in red.

| Metric group | Metrics in the metric group |
|---|---|
| MySQL status | Queries per second (QPS), transactions per second (TPS), and the number of connections. |
| InnoDB row-related operations | The number of read rows, inserted rows, updated rows, and deleted rows. |
| Thread | The number of active threads and waiting threads. |
| InnoDB page | The number of dirty pages, idle pages, and data pages. |
| Fsync | Statistics on file synchronization operations. |

6. Click **STOP** to stop data collection.
The system automatically stops data collection when you switch to another tab. You must manually restart data collection after you return to this tab.

**View the InnoDB status**

You can view the detailed running status of the InnoDB engine. **This feature is available**
**only for MySQL instances**.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Innodb status** tab.
The page displays the detailed running status of the InnoDB engine, including diagnostic data such as memory usage, transaction status, and log write operations.

**Analyze slow SQL query logs**

You can analyze the slow SQL query logs of your instance.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Slow SQL analysis** tab.
4. Optional. Specify the following filter conditions:

| Filter condition | Description |
|---|---|
| Start time/End time | The time when a slow SQL query starts or ends. By default, the time range covering the last 3 hours is used. |
| Database name | The name of the database on which a slow SQL query is executed. Enter a keyword. |
| Data sorting type | The sorting type of the searched data. Valid values: Start time and Query time. By default, the searched data is sorted by start time. |

5. View the list of slow SQL query logs, which contains the following fields:

| Field | Description |
|---|---|
| Database name | The name of the database on which the slow SQL query is executed. |

| User host | The address of the user host that initiates the slow SQL query. |
|---|---|
| Query time (S) | The execution duration of the SQL statement. Unit: seconds. |
| Lock time (S) | The duration that the SQL statement waits for a lock. Unit: seconds. |
| Number of scan lines | The total number of rows that are scanned by the SQL statement. |
| Returns the number of rows | The number of rows that are finally returned after the SQL statement is executed. |
| Start time | The time when the SQL statement was executed. |
| Query statement | The complete SQL statement. |

**Diagnose instance stutters and slow responses**

You can diagnose issues such as instance stutters and slow responses.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Slow diagnosis of instance card** tab.
4. Optional. Specify the following filter conditions:

| Filter condition | Description |
|---|---|
| Start time/End time | The time when the instance that you want to diagnose starts or ends. By default, the time range covering the last day is used. |

5. View the list of instance stutters and slow responses, which contains the following fields:

| Field | Description |
|---|---|
| Problem SQL | The SQL statement that causes the instance stutter or slow response. |

| Query time (S) | The execution duration of the SQL statement. Unit: seconds. |
|---|---|
| Start time | The time when the SQL statement was executed. |
| Optimization suggestions | The optimization solution that is provided by the system. |

Up to 50 diagnosis records are displayed on each page.

**Execute SQL statements**

You can execute SQL statements online and check the results.

**Warning**

Executing SQL statements is risky. Exercise caution when you perform this operation.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Special diagnosis**.
3. On the page that appears, click the **Execute SQL** tab.
4. In the SQL statement execution section, configure the following parameters:

| Parameter | Description |
|---|---|
| Master Library/Standby Library | The primary or secondary instance of the database on which the SQL statement is executed. Select Master Library or Standby Library. |
| Database | The database on which the SQL statement is executed. Select a database from the drop- down list. |
| Maximum number of returned rows | The maximum number of returned rows in the query result. Valid values: 1 to 10000. |
| SQL statement input field | Enter the SQL statement that you want to execute. Only single-line SQL statements are supported, and SQL statements cannot contain line breaks. |

5. Click **Execute**.
6. View the execution results:
**Execution result** tab:
SELECT queries: This tab displays the query results in a table. The number of returned rows and the execution duration measured in milliseconds are displayed at the bottom of this tab. DML operations, including INSERT, UPDATE, and DELETE statements: This tab displays the number of affected rows and the execution duration.
**Execution History** tab:
This tab displays all historical execution records, including SQL statements, execution time, destination database, and success/failed status. For a record that shows the successful execution of an SQL statement, the number of returned rows and the execution duration are displayed. For a record that shows a failure in executing an SQL statement, the error information is displayed. You must switch a PolarDB child instance to the primary instance to execute SQL statements.

#### 2.3.6 View status inspection records

This topic describes how to view the status inspection records of an instance in the ApsaraDB O&M System Smart Pro Edition console, including availability check logs, fault event records, and runtime error logs. This helps you quickly identify instance exceptions and potential risks.

**View availability**

You can view the availability check logs of an instance to monitor the survival status and availability metric changes of the instance.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Status inspection**.
3. On the page that appears, click the **View availability** tab.
On this tab, the availability check logs of the instance are displayed in a table. These logs record the survival status and availability metric changes of the instance. You can filter availability check logs by time range.

**View faults**

You can view the fault event records of an instance to know about the occurrence time, type, and impact scope of each fault.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Status inspection**.
3. On the page that appears, click the **View faults** tab.
On this tab, fault event records of the instance are displayed in a table. These records include fault occurrence time, fault type, and impact scope. You can filter fault event records by time range.

**View error logs**

You can view the runtime error logs of an instance to help identify and handle runtime exceptions.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Status inspection**.
3. On the page that appears, click the **View error logs** tab.
On this tab, the runtime error logs of the instance are displayed in a table.These logs help you identify and handle runtime exceptions. You can filter runtime error logs by time range.

#### 2.3.7 Manage audit logs

This topic describes how to manage the SQL audit logs of an instance in ApsaraDB O&M System Smart Pro Edition. You can query and filter real-time logs by conditions, archive historical logs to Object Storage Service (OSS), and view historical archive records and download archived historical logs.

**View SQL audit logs**

You can query and filter the SQL audit logs of an instance to track database operations.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree, click **Audit Logs**.
3. Optional. Specify filter conditions.

| Filter condition | Description |
|---|---|
| Start time or End time | The beginning or end of the time range to query. The time is accurate to seconds. By default, the time range is the previous day. |
| Log type | The log type. Valid values: User logs and Other logs. |
| Data sorting type | The data sorting type. Valid values: Default and Query time. |
| Keywords | The search keyword. |

4. View the list of SQL audit logs. The following table describes the fields of the list.

| Field | Description |
|---|---|
| SQL statement | The SQL statement that is audited. |
| Execution time | The time when the SQL statement was executed. |
| Execution result | The returned result of the SQL statement. |
| Database | The database on which the SQL statement was executed. |
| Username | The name of the user who executed the SQL statement. |
| Client IP | The IP address of the client from which the request was initiated. |
| Consumption time (microseconds) | The execution duration of the SQL statement. |
| Number of returned Records | The number of records returned by the SQL statement. |
| tid | The transaction ID. |

**Archive SQL audit logs**

You can export and archive SQL audit logs to OSS to meet long-term retention or compliance audit requirements.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree, click **Audit Logs**.
3. On the Audit Logs page, specify filter conditions to determine the logs to be archived.
4. Click **SQL Archive**.
5. In the message that appears, click OK. The system exports and archives SQL audit logs to
OSS.

**View the SQL archive history**

You can view historical archive records and download archived historical logs.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree, click **Audit Logs**.
3. On the Audit Logs page, click **SQL archive history**. In the SQL archive history panel, view
the list of historical archive records. The following table describes the fields of the list.

| Field | Description |
|---|---|
| Archive start time | The start time of data archiving. |
| Archive end time | The end time of data archiving. |
| File name | The name of the object that contains archived historical logs. |
| File size | The size of the object. |
| Cause of failure | The cause of failure if data archiving fails. |
| Filter SQL parameters | The parameters used to filter data for archiving. |
| Status | The state of data archiving. |
| Download address | Click Download to download the object. |

#### 2.3.8 Change records

This topic describes how to view various change and O&M records of an instance in the ApsaraDB O&M System Smart Pro Edition console, including general operation logs, HA logs, API call logs, management logs, primary/secondary inconsistency check, historical tasks of automated robots (ROBOT/bartender), data migration list, and restoration logs, to help comprehensively audit key events in the instance lifecycle.

**General log query**

You can view the general operation logs of an instance. You can also filter logs by time and view API details or task steps.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. The **General Log Query** tab is displayed by default.
4. Optional. Specify the following filter conditions.

| Filter condition | Description |
|---|---|
| Start time | The start time of the logs. |

| End time | The end time of the logs. |
|---|---|

5. View the general log list, which includes the following fields:
Log type, Operation description, Operation Time, and Operator.
6. Perform operations based on the log type:
API logs: Click **View details** to go to the details page. Task logs: Click **View task steps** or **View task history**.

**HA logs**

View the detailed records of high-availability (HA) switchover events, including the primary database endpoints before and after a switchover, switchover results, and root cause analysis.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **HA log** tab.
4. View the HA log list, which includes the following fields.

| Field | Description |
|---|---|
| UUID | The unique ID of a switchover event. |
| Master IP before switching | The endpoint of the primary database before the switchover. |
| Master IP after switching | The endpoint of the primary database after the switchover. |
| Port | The service port. |
| VIP/VPORT | The virtual IP address (VIP) and virtual port. |
| Library type | The database type. |
| Switching time | The time when the switchover occurred. |
| Switching result | Succeeded/Failed/Ignored (displayed as color-coded tags). |
| Switching root cause | The reason why the switchover is triggered. |

| Switching type | The switchover mode. |
|---|---|

5. Click **HA switching procedure** or **Associated tasks** to view the details.

**API logs**

View operation logs generated by API calls. You can filter operations by operation name and time, and view complete request and response information.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **API logs** tab.
4. Optional. Specify the following filter conditions.

| Filter condition | Description |
|---|---|
| Start time | The start time of the logs. |
| End time | The end time of the logs. |
| Interface name | Specify a specific API operation to filter logs. |

5. View the API log list, which includes the following fields:
Interface name, Instance name, Log creation time, Request time, Response time, Request content, Request result, Time consumption (ms), Operation user, Access IP, and AccessId.
6. Click **View details**. The page displays the complete request and response information.

**Management logs**

You can view operation logs related to system management and mask the operation records of specific users. This enables you to focus on critical management activities.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Manage logs** tab.
4. Optional. Specify the following filter conditions.

| Filter condition | Description |
|---|---|
| Start time | The start time of the logs. |
| End time | The end time of the logs. |

| Mask username | Masks the operation logs of a specific user. |
|---|---|

5. View the management log list, which includes the following fields:
Instance name, Role description, Operation object category, Operation objectId (some are clickable links), Creation time, Operation user, and Operation description.

**Primary/secondary inconsistency check**

You can view the status and results of primary/secondary inconsistency check tasks. You can retry, interrupt, or configure parameters for abnormal tasks.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Primary and secondary inconsistency check** tab.
4. View the check result list, which includes the following fields.

| Field | Description |
|---|---|
| Instance ID | You can click an instance ID to go to the instance details page. |
| Task ID | The ID of the check task. |
| Library name | The database to be checked. A null value indicates that all databases will be checked. |
| Table name | The table to be checked. A null value indicates that the whole table will be checked. |
| Status | Not Started/Started/Checking/Completed/Failed/Inte rrupted/Stopped. |
| Creation time | The time when the check task was created. |
| Modification time | The time when the check task was last modified. |
| Description | The description of the check result. |

5. Perform operations based on the task status.

| Status | Operation |
|---|---|

| Checking | Try to interrupt the task. Try to stop the task. |
|---|---|
| Failed/Interrupted/Stopped | Retry the task. |
| Started | View details. |
| Not Started/Failed/Interrupted/Checking | Open the configuration interface and configure parameters. |

**Robot logs**

You can view the processing logs of automated O&M robots, including the processing result status and detailed steps.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **ROBOT logs** tab.
4. View the robot log list, which includes the following fields:
Task type, Processing result (Started/Succeeded/Failed/Auto-Repaired/Rejected/Unable to Process, displayed as color-coded tags), and Processing time.
5. Click the link in the **Procedure details** column to view the detailed processing steps.

**Bartender repair history**

You can view the operation history of the automatic repair engine (bartender), including the exception type, repair method, and SQL details.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Bartender repair history** tab.
4. View the repair history list, which includes the following fields:
ID, Exception type, Repair Method, Security level (color-coded tag), Repair SQL details, Exception information, Processing result (Succeeded/Failed), Task ID (clickable link), Creation time, and Modification time.

**Bartender task history**

View the complete history of automated system O&M tasks. You can view instance details and repair plans.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Bartender task history** tab.
4. View the task history list, which includes the following fields.

| Field | Description |
|---|---|
| Task ID | Click the link to open the task details. |
| Exception type | The type of the detected exception. |
| Problems and repair methods | You can expand to view the detailed repair solution. |
| Instance information | You can expand to view instance details. |
| Security level | The security level is displayed as a color-coded tag. |
| Exception information | The details about the exception. |
| Task type | Diagnosis Only/Diagnosis and Repair. |
| Source | The source that triggers the task. |
| Status | The status of the task. |
| Target instance information | The details of the destination instance. |
| Creation time/Modification time | The time when the task was created and the time when the task was last modified. |

**Migration list**

You can view the records of data migration operations on an instance, including the source and destination versions, specifications, and migration status.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Migration list** tab.
4. View the migration list, which includes the following fields:
Migration ID (clickable link), current cluster, source version, source instance specification, migration version, migration instance specifications, migration status, switching time, migration time, and migration information.

**Restore logs**

You can view the history of data restoration operations. Data restoration can be performed based on backup sets or point in time. Configurations such as original instance retention are recorded.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Change record**.
3. On the page that appears, click the **Restore logs** tab.
4. View the restoration log list, which includes the following fields:
Migration ID (clickable link), current cluster, recovery type (based on backup sets or points in time), backup set ID, recovery time point, migration status, retain the original instance (yes/no), migration time, and migration information.

#### 2.3.9 Manage tasks

This topic describes how to manage the tasks of an instance in ApsaraDB O&M System Smart Pro Edition. You can view the task list and filter tasks by status and time range. You can also perform operations such as viewing subtasks, modifying remarks, viewing intervention records, viewing details, and retrying multiple tasks at a time.

**View the task list**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree, click **Task Management**.
3. Optional. Specify filter conditions.
Filter tasks by status. Filter tasks by time range.
4. View the task list. The following table describes the fields of the list.

| Field | Description |
|---|---|
| Task ID | The unique ID of the task. |
| Task name | The name of the task. |
| Source | The source that triggers the task. |
| Operation object | The object for which the task is run. |
| Parent task | The parent task of the task. |
| Status | The state of the task. |

| Progress | The progress of the task. |
|---|---|
| Time consuming | The duration of the task. |
| Executor | The user who runs the task. |
| Creation time | The time when the task was created. |
| Modification time | The time when the task was last modified. |
| Owner | The owner of the task. |
| Remarks | The remarks of the task. |

5. In the **Operation** column, click buttons to perform the following operations as needed:
View subtasks. Modify or add remarks. View intervention records. View details.

**Retry tasks**

If tasks fail or need to be run again, you can retry one or more tasks at a time.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree, click **Task Management**.
3. In the task list, select one or more tasks that you want to retry.
4. In the upper part of the page, click **Batch retry**.

#### 2.3.10 Backup management

This topic describes how to manage data and log backups for instances in the ApsaraDB O&M System Smart Pro Edition console. You can view and modify automatic backup policies and binary log backup policies and query historical backup records.

**Usage notes**

Download limits: You cannot directly download backup set files in the console. If you want to archive data offline or restore data locally, log on to the Apsara Uni-manager Management Console and download the data. Restoration duration: The time required for data restoration is affected by multiple factors, including instance specifications, data volume, network bandwidth, and cluster load.

**Data backup management**

**View and modify backup policies**

You can view the automatic data backup policy for an instance, including the backup cycle, time window, and retention period. You can also modify the policy configurations based on your business requirements.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the page that appears, click the **Backup policy** tab.
4. View the configurations of a data backup policy, including the following fields:
Instance name, Database, Backup switch, Backup not landing, Retention days, Estimated time, DB list, Backup time, Backup Status, Next backup time, Backup method, Backup type, Backup machine IP, Data Center, Backup start time, Start time of backup Upload, Backup cycle, Backup compression, Backup source, Backup retention policy after instance release, and Remarks.
5. Optional. Modify the backup policy as prompted and save the modification.

| Parameter | Description |
|---|---|
| Backup retention days | Specify the retention period of the backup set. Default value: 7. You can set the retention period based on your business requirements, such as 30 days. Backups are automatically deleted upon expiration. |
| Backup level | Select Just so-so, Medium, or High based on your business requirements. |
| Backup time | Modify the value based on your business requirements. We recommend that backup operations be performed during off-peak hours, such as 06:00. |
| Backup cycle | Select specific days of the week. Perform at least two backups per week for data security. |
| Backup not landing | Close Data only |
| Backup compression | Specify the backup compression mode based on your business requirements. |
| Compression parallelism | Specify the number of concurrent threads for the backup process based on your business requirements. |

**Create a temporary backup**

**Important**

The temporary backup is valid for only 18 hours. If the temporary backup expires, you need to re-initiate it.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the **Backup policy** tab, click **Create a temporary backup**. Then, configure the
following parameters.

| Parameter | Description |
|---|---|
| Backup type | AUTO: determined by the system. FULL: full backup |
| Backup method | Snapshot backup Backup physical backup Physical backup of primary Library |
| Backup time | The backup time can be accurate to the second level. |

**Create a single-database backup**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the **Backup policy** tab, click **Create a single-database backup**.
4. Configure the parameters such as the backup time and then click **Submit**.

**View the backup history**

You can view the list of historical data backup records, view backup details, and perform restoration operations based on backup sets.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the page that appears, click the **Backup history** tab.
4. View the backup history list, including the backup time, backup type, backup size, and
backup status.
5. Click the actions in the **Operation** column to perform the following operations:
View backup details. Perform backup and restoration operations.

**Regular backup repair**

You can repair regular backup tasks that are in an incomplete or failed state due to exceptions and correct backup record status to ensure data consistency.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the **Backup history** tab, click **Regular backup repair**.
4. Read the tips and click **OK**.

**Log backup management**

**View and modify binary log backup policies**

You can view the binary log backup policy for an instance, including the backup retention period. You can also modify the policy configurations based on your business requirements.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **binlog backup management**.
3. On the page that appears, click the **binlog backup policy** tab.
4. View the configurations of a binary log backup policy, including the following fields:
The backup retention period, upload compression, retention days of remote storage, number of local reservations, upload method, disk overuse cleanup, critical alert threshold for disk space, local retention time, local retention space, log backup, and local cleaning method.
5. Optional. Modify the policy configuration as prompted and save the modification.

| Parameter | Description |
|---|---|
| Upload method | Do not Upload Upload Upload in seconds |
| Local cleaning method | Do not clean Clean up |
| Upload compression | Select Uncompressed , zlib compression , or lz4 Compression . Enabling compression can save bandwidth and remote storage, but may increase the local CPU overhead. |
| Log backup | Close: If you disable this feature, all log backup files are deleted and you cannot restore the data of the instance to the specified point in time. Enable and charge: The log backup feature is enabled. |
| Remote storage retention days | Configure the retention period for logs in remote storage. Logs whose retention period exceeds this period are automatically deleted. |

| Local Retention time | Configure the maximum retention period for logs. If the binary log files whose retention period exceeds the specified retention period are backed up by using the log backup feature, the system automatically deletes the binary log files. |
|---|---|
| Local reserved space | Monitor the percentage of the total disk space used by the local binary log directory. |
| Number of local reservations | The maximum number of binary log files that can be retained. If the number of retained binary log files exceeds the maximum number, the system automatically deletes earlier binary log files until the number is less than the maximum number. |
| Critical disk space warning threshold | If the space occupied by local binary logs exceeds this threshold, a critical alert is triggered. |
| High Disk Cleanup | Enable: When disk space becomes critically low, the system automatically deletes older logs to maintain stable operation, which may prevent recovery to earlier points in time. Disable: If the disk is full, the instance may be suspended. |

**View the backup history of binary logs**

View the list of historical binary log backup records, including the backup time, file size, and backup status.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **binlog backup management**.
3. On the page that appears, click the **binlog backup history** tab.
4. View the list of historical binary log backup records, including the backup time, file size, and
backup status.

**Log reloading**

When the modified policy is not synchronized to the underlying agent, you can manually trigger a reload.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **binlog backup management**.
3. On the page that appears, click the **binlog backup history** tab and then click **Overload**.

**Clear logs**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **binlog backup management**.
3. On the page that appears, click the **binlog backup history** tab and then click **Clear logs**.

**Important**

This operation is irreversible once initiated.

#### 2.3.11 Data restoration

This topic describes how to perform data restoration operations in the ApsaraDB O&M System Smart Pro Edition console, including backup set-based restoration and point-in-time restoration.

**Restore data from a backup set**

This section describes how to restore the instance data to a point in time corresponding to a completed and valid backup set.

**Important**

The instance must have at least one successful and valid backup set before a restoration is performed. You can check the validity of a backup set in the **Valid** column of the backup list. Invalid or corrupted backup sets cannot be used for restoration. If no backup set is available, create a temporary backup.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the **Backup history** tab, find the backup set that you want to manage and click
**Restore by backup set** in the Operation column.
4. On the page that appears, configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Reserved Instances | Specify whether to retain the current instance based on your business requirements. If you want to restore data of a dedicated instance, you can determine whether to retain or replace the current instance. If you determine to replace the current instance, the data of the current instance will be restored in overwrite mode. If you retain the current instance, the data of the current instance is not affected. The system will generate a child instance to restore the required backup data. By default, the child instance is retained for two days and is automatically deleted upon expiration. If you replace the current instance, the data of the current instance is lost. The instance will be rolled back to the desired backup data state. |

| Cross-cluster allocation | Select whether to enable cross-cluster allocation as needed. When no resources are available in the current cluster, resources can be requested from other clusters within the same data center. Note that if you use a virtual IP address (VIP) to access the instance, you may need to re-bind or modify the VIP configuration after restoration. |
|---|---|
| Network type | Select Private network or Public network based on your business requirements. |

**Restore data to a point in time**

Instance data can be restored to any specified point in time within the log retention period.

**Important**

To restore data to a point in time, make sure that: Log backup is enabled. A valid full backup set exists, and no overlaying restoration has occurred between two full backups. The target point in time is within the log retention period.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Data backup management**.
3. On the **Backup history** tab, click **Restore to point in time** in the upper part of the page.
4. In the dialog box that appears, configure the following parameters. Then, click **Submit**.

| Parameter | Description |
|---|---|
| Recovery time point | Precise to the second. |
| Cross-cluster allocation | Select whether to enable cross-cluster allocation as needed. When no resources are available in the current cluster, resources can be requested from other clusters within the same data center. Note that if you use a virtual IP address (VIP) to access the instance, you may need to re-bind or modify the VIP configuration after restoration. |
| Network type | Select Private network or Public network based on your business requirements. |

#### 2.3.12 Security configuration

This topic describes how to manage IP address whitelist rules and associated security group rules for an instance in the ApsaraDB O&M System Smart Pro Edition console.

**Manage IP address whitelists**

This feature allows you to view, add, modify, and delete IP address whitelist rules for an instance to manage the range of IP addresses that can access the instance.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Security Configuration**.
3. On the page that appears, click the **ip whitelist** tab.
4. View the IP address whitelists.
5. Perform the following operations:
**Add a whitelist rule**: Add an IP address whitelist rule as prompted.
**Modify a whitelist rule**: Modify an IP address whitelist rule.
**Delete a whitelist rule**: Select the rule that you want to delete and confirm the
deletion. Only IP addresses that are added to a whitelist can access the instance.

**Manage security groups**

This feature allows you to view the list of associated security groups, and associate new security groups or disassociate existing ones.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Security Configuration**.
3. On the page that appears, click the **Security Group** tab.
4. View the list of associated security groups.
5. Perform the following operations:
**Associate a security group**: associates a new security group with the instance.
**Disassociate a security group**: disassociates an associated security group from the
instance.

#### 2.3.13 Parameter configurations

This document describes how to view and modify runtime parameters at both the database kernel level and the management system level in the ApsaraDB O&M System Smart Pro Edition console.

**View and modify kernel-instance parameters**

This feature displays all configurable kernel parameters in a table format, including the parameter name, default value, current value, and value range. It also allows you to modify parameter values based on your business requirements and view the modification history.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Parameter configuration**.
3. On the page that appears, click the **Kernel instance parameters** tab.
4. View the parameter list. This tab displays all configurable parameters in a table format,
including the following fields.

| Parameter | Description |
|---|---|
| Parameter name | The name of the parameter. |
| Default value | The system default value for the parameter. |
| Current value | The actual value of the parameter. |
| Value range | The valid range of minimum and maximum values for the parameter. |
| Unit | The unit of measurement for the parameter value. |
| Division factor | The divisibility requirement that the parameter value must satisfy. |
| User-visible | Specify whether the parameter is visible to users. |
| User-modifiable | Specify whether the parameter allows users to modify it. |

5. Optional. Modify the value of a parameter:
Find the parameter that you want to modify, click Edit in the Operation column, and then configure a new value. Save the modification. Some parameter changes require an instance restart to take effect. We recommend that you perform such operations during off-peak hours. Typical parameters include innodbbufferpoolsize, waittimeout, maxconnections, and characterset_server.
6. Optional. View the parameter modification history, which includes the following fields.

| Parameter | Description |
|---|---|
| Parameter name | The name of the parameter that was modified. |

| Old value | The parameter value before modification. |
|---|---|
| New value | The parameter value after modification. |
| Modification time | The time when the modification was performed. |

**View control instance parameters**

This feature allows you to view the list of instance parameters at the management system level, including the parameter names and current values.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Parameter configuration**.
3. On the page that appears, click the **Control instance parameters** tab.
4. View the control parameter list, including the parameter names and parameter values.

#### 2.3.14 O&M configurations

This topic describes how to manage temporary resource allocation and underlying O&M policies for instances in the ApsaraDB O&M System Smart Pro Edition console. You can temporarily increase computing or storage resources to handle traffic spikes, and configure system-level parameters such as high availability, log auditing, and performance metric collection.

**Temporary resource configurations**

This feature allows you to temporarily adjust computing resources (CPU and IOPS), the number of connections, and storage space for an instance during peak hours or emergencies. You can also configure an automatic restoration time to alleviate resource bottlenecks without changing the instance specifications.

**Important**

Temporarily improving resource usage is used only for short-term mitigation. For sustained resource usage improvement, perform an instance specification change (configuration change). All temporary configurations must include a restoration value and a restoration time. The system automatically reverts to the original settings at the scheduled time.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **O & M configuration**.
3. On the page that appears, click the **Temporary resource configuration** tab.
4. View the current temporary resource configurations. Configure the parameters in the
following sections based on your business requirements and submit the configurations.

**Set IOPS**

You can temporarily adjust the maximum disk read/write performance of an instance.

| Parameter | Description |
|---|---|
| IOPS | The target IOPS value for the temporary adjustment. |
| Recovery value | The standard IOPS configuration of the instance. The system automatically reverts the IOPS to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Set CPU**

You can temporarily adjust the number of CPU cores or the CPU allocation ratio available to the instance.

| Parameter | Description |
|---|---|
| CPU | The target CPU value for the temporary adjustment. |
| Recovery value | The standard CPU configuration of the instance. The system automatically reverts the CPU configuration to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Set the maximum number of connections**

You can temporarily increase the maximum number of concurrent client connections allowed for the instance.

| Parameter | Description |
|---|---|
| Maximum connections | The target maximum number of connections for the temporary adjustment. |
| Recovery value | The standard maximum number of connections for the instance. The system automatically reverts the maximum number of connections to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Configure the number of reserved_connections connections**

You can temporarily adjust the number of reserved connections (typically used for internal monitoring or privileged accounts).

| Parameter | Description |
|---|---|
| reserved connections _ | The target number of reserved connections for the temporary adjustment. |
| Recovery value | The standard number of reserved connections for the instance. The system automatically reverts the number of reserved connections to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Configure disk space**

You can temporarily expand the storage space of an instance to accommodate data surges. Temporary disk expansion is irreversible. Upon expiration, the system automatically reverts to the original capacity.

| Parameter | Description |
|---|---|
| Maximum disk space | The target total disk capacity for temporary expansion (unit: GB). |
| Recovery value | The standard disk capacity configuration of the instance. The system automatically reverts the disk capacity configuration to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Configure the disk space check feature**

Specifies whether to lock the instance when the disk usage exceeds a specific limit. When this feature is disabled, the instance is not locked even if disk usage exceeds the limit.

| Parameter | Description |
|---|---|

| Check disk space | Valid values: Enable and Close. When this parameter is set to Enable, the protection mechanism is triggered if no disk space is available. When this parameter is set to Close, the protection mechanism is not triggered. |
|---|---|
| Recovery value | The default switch state. The system reverts the switch to this state upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**O & M configuration**

This feature allows you to configure underlying O&M parameters of an instance, such as highavailability policies, log auditing, SQL details collection, and performance monitoring frequency, to meet specific compliance or stability requirements.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **O & M configuration**.
3. On the page that appears, click the **O & M configuration** tab.
4. View the current O&M configurations, including parameters such as the maintenance
window and automatic repair policy. Configure the parameters in the following sections based on O&M requirements and submit the configurations.

**Configure the instance memory isolation feature**

This feature specifies whether to implement strict memory resource isolation for an instance.

**Important**

When this feature is enabled, the system implements strict memory resource isolation for the instance. When this feature is disabled, faults may occur. Currently, you cannot disable this feature.

| Parameter | Description |
|---|---|
| Instance memory isolation | Valid values: Enable and Close. We recommend that you enable this feature to ensure stability. |

**Configure availability and reliability policies**

You can configure the primary/secondary synchronization mode and high-availability failover priority to balance data security and business continuity.

| Parameter | Description |
|---|---|

| sync binlog settings _ | Security mode: Set this parameter to 1 for both primary and standby databases. This ensures the highest data security at the cost of lower performance. Normal mode (default): Set this parameter to 1 for the primary database and to 1000 for the secondary database. This balances performance and data security. High performance mode: Set this parameter to 1000 for both the primary and secondary databases. This ensures the highest performance but may lose a small amount of data in extreme cases. |
|---|---|
| HA priority mode | Availability first (default): The system prioritizes business continuity, potentially at the expense of partial data consistency. Reliability priority: The system prioritizes zero data loss, which may result in slightly longer failover times. |
| Binlog synchronization settings | Asynchronous mode (default): A response is returned immediately after a write operation is performed on the primary database, whereas asynchronous replication is performed on the secondary database. This provides the best performance. Semi-synchronous mode (recommended): A response is returned only after at least one secondary database acknowledges receipt. Dual Channel Mode: An enhanced synchronization mechanism that provides stronger consistency guarantees. |

**Configure a migration solution for large instances**

This parameter specifies whether to enable special migration logic for large instances.

| Parameter | Description |
|---|---|
| Large instance migration solution | Valid values: Enable and Close. If this feature is enabled, specific optimization policies are used when large instances are migrated. |

**Configure a data source of SQL details**

You can configure a destination for storing SQL audit details. If you want to modify settings, contact the TX team for technical support.

| Parameter | Description |
|---|---|

| SQL detail data source | Write SLS only Write only Fangcun Mountain Write both SLS and Fangcun Mountain Write kepler only Write SLS and kepler simultaneously |
|---|---|

**Configure whether to enable SQL details collection**

You can configure whether to collect detailed SQL execution records.

| Parameter | Description |
|---|---|
| SQL details collection | Valid values: Enable and Close. If this feature is enabled, certain performance overhead is required to collect audit logs. |

**Specify a log audit version**

You can configure the version of the log audit feature. If you want to modify settings, contact the TX team for technical support.

| Parameter | Description |
|---|---|
| Log audit version | Old version log audit: Traditional audit logic is used. New log audit: The audit logic is optimized to provide better performance. |

**Configure the percentage for table consistency verification**

You can configure the data sampling ratio for table consistency verification during a primary/secondary failover or failback.

| Parameter | Description |
|---|---|
| Table consistency verification percentage | Enter a percentage value (0–100). 0% disables verification, while 100% indicates that full verification is performed. |

**Configure a timeout period for backup set playback**

**verification**

You can configure the timeout for backup set replay verification when you restore child instances, create read-only instances, create disaster recovery instances, or recreate secondary instances. If you set this parameter to a non-zero value, the backup set is verified to ensure backup availability when you perform the preceding operations.

| Parameter | Description |
|---|---|
| Backup set playback verification timeout | The timeout period. Unit: seconds. If you set this parameter to 0, verification is skipped. |

**Configure the performance collection frequency**

You can configure the interval for collecting instance performance metrics, such as CPU, memory, and I/O.

| Parameter | Description |
|---|---|
| Collection frequency | The interval at which data is collected. Unit: seconds. A higher frequency enables finer-grained monitoring but increases system overhead. |

#### 2.3.15 Tag configurations

This topic describes how to view and modify the tags of an instance in the ApsaraDB O&M System Smart Pro Edition console. The tag information includes the label type, current value, and expiration time.

**View and modify instance tags**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane, click **Tag configuration**.
3. View the list of tags, which includes the following fields.

| Field | Description |
|---|---|
| Label type | The name of the tag category. |
| Default value | The default value of the tag. |
| Value range | The range of values that can be set for the tag. |
| Value description | A description of the meaning for each value. |

| Current value | The current value set for the tag. |
|---|---|
| Current Expiration Time | The expiration time of the tag. If a tag does not have this attribute, "No expired attribute" is displayed. |

4. Optional. Modify tags:
Find the tag that you want to manage and click **Edit** in the Operation column. For a non-editable tag, Edit is unavailable in the Operation column.
5. In the dialog box that appears, modify the parameters described in the following table.

| Parameter | Description |
|---|---|
| Label type | This field is read-only and cannot be modified. |
| Current value | This field is required. |
| Expiration Time | Specify the expiration time. This field is optional. |

6. Click **OK**. The list is automatically updated.

#### 2.3.16 Manage databases

This topic describes how to manage the databases of an instance in ApsaraDB O&M System Smart Pro Edition. You can view the database list and details, create one or more databases at a time, and delete databases.

**View the database list**

You can view the list of all databases in an instance, including the name, status, account information, and character set of each database. You can also use the search box to quickly find a database.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree of the instance details page, click **Database information**.
3. View the database list. The following table describes the fields of the list.

| Field | Description |
|---|---|
| Database name | The name of the database. |

| Database status | The state of the database, such as Running, Creating or Deleting. |
|---|---|
| Account information | The account information of the database. The current number and maximum number of accounts are displayed. You can click a number to go to the account list. |
| Character set | The character encoding used by the database, such as utf8 . |
| Business type | The business category to which the database belongs. |
| Remarks | The description of the database. |

4. Optional. Enter a database name in the search box to search for the database in exact
match mode.

**Create a database**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree of the instance details page, click **Database information**.
3. On the Database list page, click **Create a database**.
4. In the dialog box that appears, enter the database configuration information and click **OK**.

**Create multiple databases at a time**

You can create multiple databases at a time to improve the efficiency of batch initialization.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree of the instance details page, click **Database information**.
3. On the Database list page, click **Create databases in batches**.
Separate multiple database names with commas (,).
4. In the dialog box that appears, enter the configuration information of multiple databases
and click **OK**.

**View the details of a database**

You can view the details of a database, including its deep structure information such as the list of tables.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree of the instance details page, click **Database information**.
3. Find the database that you want to view and click **Details** in the Operation column.
In the panel that appears, view the details of the database, such as table schemas.

**Delete a database**

You can delete databases that are no longer needed. Before you delete a database, you must confirm the database name to prevent accidental deletion.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the navigation tree of the instance details page, click **Database information**.
3. Find the database that you want to delete and click **Delete** in the Operation column.
4. In the message that appears, confirm the database name and click **OK**.

#### 2.3.17 Account management

This topic describes how to manage user accounts and system accounts of instances in the ApsaraDB O&M System Smart Pro Edition console. The core features include account viewing, account creation (normal, privileged, and management), password maintenance (modify, reset, or view), modification of remarks, authorization, and account deletion.

**User accounts**

**View user accounts**

You can view and manage user-created database accounts and status information.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
3. On the page that appears, click the **User account** tab.
4. Optional. Filter accounts by account name or database name.
5. View the list of user accounts, which includes the following fields.

| Field | Description |
|---|---|
| Account name | The name of the database account. |
| Account Status | The account is in the Creating, In use, or Deleting state. |
| Database type | The type of database engine to which the account belongs. |
| Account type | The account type can be a standard account, a global read-only account, a read-only account for global logs, or a privileged account. |
| Remarks | The description of the account. |

**Create a standard account**

You can create standard accounts with basic read and write permissions.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Click **Create a normal user account**
4. In the dialog box that appears, configure the account settings.
5. Click **Submit**.

**Create a privileged account**

You can create privileged accounts that have higher operation permissions.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Click **Create a high-privilege user account**.
4. In the dialog box that appears, configure the account settings.
5. Click **Submit**.

**Create a management account**

You can create an administrator account that has the permissions to manage instances.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Click **Create a management account**.
4. In the dialog box that appears, configure the account settings.
5. Click **Submit**.

**Change a password**

You can change the login password of an account.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Find the account that you want to manage and click **Change password** in the Operation
column.
4. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Original password | Enter the password that is currently used. |
| New password | Enter a new password, which must meet the complexity requirements. |
| Confirm password | Enter the new password again for confirmation. |

The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Click **Submit**.

**Reset a password**

You can forcibly reset the login password of an account without requiring the old password.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Find the account that you want to manage and click **Reset password** in the Operation
column.
4. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| New password | Enter a new password, which must meet the complexity requirements. |
| Confirm password | Enter the new password again for confirmation. |

The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
5. Click **Submit**.

**Modify remarks**

You can modify or add the description of an account.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Find the account that you want to manage and click **Modify remarks** in the Operation
column.
4. In the dialog box that appears, enter remarks.
5. Click **Submit**.

**Grant or revoke permissions**

You can grant or revoke access permissions on specific databases for standard accounts. The account must be a standard account. The account must have a list of permissions.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Find the account that you want to manage and click **Authorization** in the Operation
column.
4. Grant or revoke permissions:
Grant permissions: Click **Edit**. In the dialog box that appears, the database permission management table is displayed. You can configure the permissions (read/write, readonly, DML only, and DDL only). Revoke permissions: Click **Revoke permissions**.
5. Click **Submit**. Then, click **Submit**.

**Delete an account**

You can delete accounts that are no longer needed to release resources.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **User account** tab.
3. Find the account that you want to manage and click **Delete** in the Operation column.
4. In the message that appears, click **Submit**.

**System accounts**

**View system accounts**

You can view the list and status of various built-in system O&M accounts.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **System account** tab.
3. View the list of system accounts, including the following fields: Account name, Account
Status, Business type, Account type, and Remarks.

**View O&M passwords**

You can view the O&M password of a system account and copy the password.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **System account** tab.
3. Find the account that you want to manage and click **View the operation and**
**maintenance password** in the Operation column.
4. In the message that appears, you can view the account name and password. You can also
copy the password.

**Reset the password of a system account**

You can reset the password of a system account. The system prompts special permission types.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **System account** tab.
3. Find the account that you want to manage and click **Reset password** in the Operation
column.
4. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| New password | Enter a new password, which must meet the complexity requirements. |

| Confirm password | Enter the new password again for confirmation. |
|---|---|

The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The system hides the reset password button for some special permission types, such as aurora and replicator.
5. Click **Submit**.

**Delete a system account**

You can delete specific system accounts. Exercise caution when you perform this operation.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **System account** tab.
3. Find the account that you want to manage and click **Delete** in the Operation column.
4. In the message that appears, click **Submit**.

### 2.4 Intelligent O&M

#### 2.4.1 Intelligent host diagnostics

ApsaraDB Operations and Maintenance System Smart Edition provides the intelligent host performance diagnostics feature, which displays statistics in flame graphs. This feature can automatically parse CPU-intensive functions, abnormal call stacks, and resource consumption tracing. It can accurately identify system-level performance bottlenecks, locate the root cause, and compare the performance of instances in scenarios where your database is heavily loaded, responds with a high latency, or experiences kernel-level stuttering.

**Background information**

Definition of flame graphs: A flame graph is a visualized performance analysis tool that displays how a program runs on a CPU. X-axis (width): The number of CPU samples. A wider bar indicates more CPU time spent by a function and its call chain. This is the major performance hotspot. Y-axis (height): The depth of the call stack. It displays the hierarchical relationship among different functions. Color: Different colors indicate different code modules or call stacks. Core logic: The x-axis is used to quickly locate the most time-consuming code execution pipeline, transforming complex performance statistics into simple graphs.

**Use scenarios**

In database O&M scenarios, flame graphs can resolve the following issues. For more information, see the Use cases of database diagnostics section in this topic. High CPU utilization: When the CPU utilization of a database process is excessively high, you can use flame graphs to quickly identify the functions that are occupying excessive computing resources, such as sorting, hash computing, and regular expression matching functions. Response latency spikes: When the response latency of a service periodically spikes, you can compare flame graphs of different time periods to identify the abnormal call stack that causes the latency spike. Lock contentions and spinlocks: When the QPS remains low and the CPU is not fully loaded, you can use flame graphs to capture abnormal hotspots in lock-related functions, such as `mutex_lock` and `futex` , and then locate the cause of lock contentions. Optimization verification: After parameter tuning, system upgrade, or SQL optimization, you can use the hotspot comparison feature to visually check whether the hotspot function bar becomes narrow or disappears in the flame graph. Kernel-level stuttering troubleshooting: When an issue involves system calls (such as frequent packet processing or memory copy), the flame graphs can display the distribution of time consumption of kernel mode functions.

**Usage notes**

**Data timeliness limit**: By default, the system allows you to view only the data collected
within the previous seven days (based on the collection time in file metadata).
**Historical data processing**: If you want to analyze outdated data, we recommend that
you collect the data again.

**Preparations**

Contact Apsara Stack technical support to help deploy the lightweight probe on the desired host to collect data.

**Procedure**

1. **Access the intelligent host diagnostics page**
i. Log in to ApsaraDB Operations and Maintenance System Smart Edition. ii. In the left-side navigation pane, choose **Intelligent O & M > AI Host Diagnosis**.
2. **Upload the collected data**
In the upper-right corner of the page, click **Upload**. In the dialog box that appears, select a local performance data file. The system will automatically parse the file and generate a flame graph.
3. **View the analysis results**
After the system completes parsing, you can view and analyze performance data on the Hot spot distribution tab, Hot spot comparison tab, and Process function call relationship hotspot diagram.

**Hot spot distribution tab**

Hot process distribution map: displays the percentage of CPU resources occupied by each process in a ring chart. Process hotspot timing diagram: displays the trend of changes in process heat over time. We recommend that you pay close attention to peaks. Higher and denser bars indicate heavier CPU loads. Process function call relationship hotspot diagram: Function heat: the amount of time consumed by a function to execute code. Total heat: the total amount of time consumed by a function and all its child functions to execute code.

**Hot spot comparison tab**

Hotspot comparison enables you to view differential flame graphs of the same instance, process, or time period or different instances, processes, or time periods. It helps you verify optimizations and locate performance issues caused by version rollbacks or environment differences.

**Use cases of database diagnostics**

The following cases are for reference only. We recommend that you handle the issues based on the actual situations.

**Case 1: High database CPU utilization**

Issue: An alert is triggered indicating that the CPU utilization of a database instance consistently remains above 90%. The business response is severely slowed down. Diagnostics: Confirm whether the database instance is actually busy (computing-intensive), a lock wait issue occurs, or the resources occupied by the instance are idle. Procedure: i. Collect host performance data during the time period within which the CPU utilization is high and upload the performance data file to the platform. ii. View the process and function relationship hotspot chart. iii. Find the widest function bar. Analysis: Case A (SQL computing hotspot): The hotspot function is `mysql_parse` , `sort_table` , `hash_join` , or a function related to a business table. Conclusion: Slow SQL queries exist, such as full table scans or complex sorting. Solution: Extract the corresponding SQL queries, analyze the execution plans, and optimize the indexes. Case B (system call hotspot): The hotspot function is `sys_call_table` or

```
 network_receive .
```

Conclusion: Packet processing or system calls are frequent. Solution: Check the number of network connections, look for bandwidth bottlenecks, or verify the middleware configuration. Case C (lock contention hotspot): The hotspot function is `mutex_lock` or `futex_wait` . Conclusion: Threads spend most of the time waiting for locks instead of performing computing. Solution: Check the deadlock logs and optimize the granularity of transactions.

**Case 2: Periodic business response latency spikes**

Issue: The QPS is stable, but the service interface encounters periodic latency spikes. Diagnostics: Check performance differences between the normal period and latency spike period. Procedure: i. Collect performance data during the normal period and latency spike period. ii. Upload the performance data files and use the hotspot comparison feature to generate differential flame graphs. iii. Observe the new red hotspots in the differential flame graphs. Analysis: Most differential hotspots located in `gc_worker` or the memory allocation function. Conclusion: The issue is caused by garbage collection or memory allocation. Most differential hotspots located in a specific business logic function. Conclusion: The issue is caused by a scheduled task or batch job. Solution: Adjust the execution time of the scheduled task or batch job, or optimize memory allocation.

**Case 3: Kernel-level stuttering**

Issue: The CPU utilization of the database process is not high, but the loads (Load Average) are excessively high. The database process is not responding. Diagnostics: Check whether the kernel mode fails to respond. Procedure: i. Upload the performance data file and view the kernel mode flame graph. ii. Search for system call functions, such as `rwsem` and `spin_lock` . Analysis: An excessive amount of time is spent on kernel lock wait or frequent context switching ( `context_switch` ). Conclusion: System resource contention is severe, or a driver or kernel bug exists. Solution: Check the system log (dmesg) to assess whether the kernel needs an upgrade or system parameters (such as the number of file handles and the size of the network buffer) need to be modified.

**Case 4: Optimization verification**

Issue: After you optimize SQL queries or modify parameters, you need to confirm whether the performance of the database instance is improved. Diagnostics: Quantify changes in hotspot functions. Procedure: i. Collect performance data before the optimization and after the optimization. ii. Use the hotspot comparison feature. iii. Observe the change in the width of the hotspot function bar. Analysis: The hotspot function bar becomes narrow or disappears. Conclusion: The optimization takes effect and the performance bottleneck is eliminated. The width of the hotspot function bar remains unchanged, but a new hotspot appears. Conclusion: The bottleneck is transferred. In this case, you need to optimize the new hotspot.

#### 2.4.2 Information collection

ApsaraDB Operations and Maintenance System Smart Edition provides the information collection feature, which allows you to use various search parameters (including keywords, ApsaraDB Operations and Maintenance System task IDs, DTS task IDs, or instance IDs) to quickly trigger a diagnostic task. It can automatically aggregate the logs of relevant services and generate a structured diagnostic report. This topic uses Data Transmission Service (DTS) task diagnosis as an example to describe how to collect information based on task IDs and keywords. This topic also describes how to download logs, decrypt logs, and import logs for offline analysis.

**Use scenarios**

Quick issue locating: When a task is abnormal, you can use the task ID or business keyword to trigger end-to-end log collection. Offline analysis: You can export an encrypted log package and replay it in a non-production environment. This helps developers or the L2 technical support team to locate the root cause. Unified diagnostic entry: Data can be centrally collected, displayed, and analyzed on the platform regardless of the sources of tasks. This greatly improves the O&M efficiency.

**Usage notes**

The log package that you upload must comply with the internal format. It must include certain paths and metadata. Logs in invalid formats cannot be parsed. Apsara Stack Inspection System is an internal, centralized testing platform. Only users with L2 or higher permissions have access to the platform. It is not deployed on user sites.

**Suggestions**

We recommend that you click View details in the console to analyze existing issues first. Use the log download and import feature only for cross-environment collaboration, long-term archiving, or in-depth debugging.

**Supported collection methods**

Collect based on instance IDs or task IDs: Only ApsaraDB RDS for MySQL instances support this method. Collect based on keywords: You can collect only service rule logs displayed in the service rule drop-down list in the console. The actual service rule logs displayed in the console prevail. Collect based on keywords: Only ApsaraDB RDS for MySQL, DTS, and PolarDB-X support this method.

**Method 1: Diagnose based on task IDs**

Use this method if the task is created and its ID is obtained. For example, you can use method if the user reports that a migration task failed.
1. **Go to the information collection page**
i. Log in to ApsaraDB Operations and Maintenance System Smart Edition. ii. In the left-side navigation pane, choose **Intelligent O & M > Info Gathering**.
2. **Initiate a diagnostic**
Set Parameter type to **DTS JOB ID**, specify the **parameter value**, and then click **Start**
**diagnosis**.
The system will automatically call the backend service to aggregate the scheduling, execution, monitoring, and error logs related to the task.
3. **View diagnostic logs**
After the diagnostic is complete, click **View details** in the Operation column of the task. On the task details page, click **View details** to view the logs.
4. **Download the log package**
Click **Download logs** in the Operation column to download the log package. The following figure shows the downloaded logs.
5. **Decrypt logs**
After the logs are downloaded, log in to Apsara Stack Inspection System. On the diagnostic plan page, click **Log Parse** in the upper-right corner to decrypt the logs.

**Method 2: Diagnose based on keywords**

Use this method if the task ID is unavailable but the task can still be found by using fuzzy match based on business context.
1. **Go to the information collection page**
i. Log in to ApsaraDB Operations and Maintenance System Smart Edition. ii. In the left-side navigation pane, choose **Intelligent O & M > Info Gathering**.
2. **Initiate a diagnostic**
Set Parameter type to **Keywords**, specify the **parameter value**, select **dts** as the scenario, and then click **Start diagnosis**.
3. **View diagnostic logs**
After the diagnostic is complete, click **View details** in the Operation column of the task. On the task details page, click **View details** to view the logs.
4. **Download the log package**
Click **Download logs** in the Operation column to download the log package. The following figure shows the downloaded logs.
5. **Decrypt logs**
After the logs are downloaded, log in to Apsara Stack Inspection System. On the diagnostic plan page, click **Log Parse** in the upper-right corner to decrypt the logs.

**Import and replay logs for offline analysis**

On the **One-click information collection** page, click **Import view** and upload the log package ( `ZIP file` ). Make sure that the log package uses the requested format. The system will automatically parse and display the log content for offline replay and analysis. For more information about how to download logs, see Step 4 in the Method 1 or Method 2 section of this topic.

#### 2.4.3 Automated script management

ApsaraDB Operations and Maintenance System Smart Edition provides the automated script management capability to help you transform frequent, complex CLI-based O&M operations, such as instance status restoration, backup task intervention, and resource cleanup, into standardized automated workflows. With the built-in risk classification and review mechanism, this capability can greatly reduce user errors and the time consumption of database O&M, improving the overall efficiency and security.

**Usage notes**

**Risks**: The automated scripts described in this topic involve changes to metadata and
control logic. If you cannot determine whether this operation adversely affects your business, do not perform the operation on your own. We recommend that you submit a ticket to Apsara Stack technical support for risk assessment and assistance.
**Review mechanism**: The executions of all scripts must follow the "review before
execution" principle. After you submit a task, the script is executed only after the task is approved by the platform O&M administrator. Unapproved scripts are not executed. Low-risk scripts: After a script is approved, the system automatically executes the script. Medium-risk and high-risk scripts: After a script is approved, the task enters the Pending Confirmation state. In this case, you need to manually confirm to execute the script. If you do not confirm, the task remains in the current state.

**Use scenarios**

**Abnormal status fixing**: You can use this capability if the status of a database instance is
abnormal because the underlying engine is missing, a task is interrupted, or metadata inconsistency occurs. For example, ServiceTest fails to reach the desired state or residual testing instances are found.
**Emergency handling**: You can use this capability if an instance fails to restart or a backup
task remains in the Check state. In addition, you cannot fix the issue by using regular methods.
**Resource usage governance**: You can use this capability if you want to delete expired
data in batches because the Object Storage Service (OSS) storage usage of backups is excessively high or the usage of local disks of the instance is excessively high due to the accumulation of historical data or logs.
**Workflow unblocking**: You can use this capability if you want to skip non-key detection
steps to accelerate the workflow in disaster recovery system upgrade or special change scenarios.

**Benefits**

**Simplified procedure and visualized risks**: Standard, tested scripts are built into this
feature to help you quickly handle the complex underlying logic. The system will display the risks, risk levels (low, medium, and high), and scope of impact before it executes a script to help you make informed decisions.
**Standardized review workflow**: This feature comes with a strict review mechanism,
which can automatically generate URLs and send them to reviewers. A script is executed only after it is approved, which ensures the compliance and traceability of script executions.
**End-to-end transparent monitoring**: This feature can track the status of script
execution tasks in real time, allows you to download logs, and can interrupt tasks when exceptions occur. This ensures that the executions of all tasks are transparent.
**Reduced user errors**: This feature allows you to configure parameters instead of running
commands at the CLIT, which greatly reduces the chances of user errors.

**Supported automated scripts**

**Script overview**

| Automated script | Description | Risk level | Supported database engine |
|---|---|---|---|

| Hack ServiceTest | Forcefully terminate the ServiceTest process to make it reach the desired state. This helps address the issue that the upgrade process is blocked due to environmental differences. | Low risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition Tair (Redis OSS- compatible) MongoDB |
|---|---|---|---|
| Restore status and delete residual MySQL testing instances caused by task interruption | Delete residual MySQL testing instances and the relevant task flow caused by a task interruption, release resources, and restore the status of the instance to ensure consistency. | Low risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition |
| Forcefully cancel a MySQL instance backup task | Forcefully delete the record of a backup task that remains in the Check state and fails to be canceled. | Low risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition |
| Forcefully restart a MySQL instance | Run a command to forcefully restart an instance that is in an abnormal state and fails to be restarted in the console. This script does not support instances that have transparent data encryption (TDE) enabled. | Medium risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition |
| Delete expired historical data or logs in OSS | Delete full backup files and incremental backup files that have exceeded the specified retention period in OSS buckets in order to release storage space. | Medium risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition Tair (Redis OSS- compatible) |
| Address the issue that the incremental logs of MySQL instances are not uploaded or deleted | Revise the records of abnormal states in the archivelog list table in the _ bak metabase. This addresses the issue that incremental logs are not uploaded and local incremental logs are not deleted. | Low risk | RDS MySQL PolarDB for MySQL Primary/Seconda ry Edition |

|   | archivelog list _ |
|---|---|
| bak |   |

**Hack ServiceTest**

This script is used to hack ServiceTest to force it to enter the desired state in special scenarios, such as environment upgrade for emergencies, single disaster recovery data center upgrade, or requirement from the customer. ServiceTest is typically used to automatically and periodically inspect the lifecycle of instances. It covers key scenarios such as instance creation, account management, backup task execution, and instance deletion. This mechanism can proactively probe APIs or features in the environment and accurately identify faults, which ensures the real-time stability of the platform. If you proactively hack ServiceTest, the inspection process will be forcefully terminated. Consequently, the preceding feature becomes unavailable. Terminating ServiceTest affects only the automated inspection logic on the platform side. It does not affect your production instances and has no negative impact on the production environment.

**Use scenarios**

Troubleshooting results indicate that no cluster using the corresponding database engine is deployed. Consequently, ServiceTest fails to reach the desired state. In a disaster recovery environment that consists of Data Center A and Data Center B, only Data Center A is upgraded. In this case, you need to force ServiceTest to reach the desired state in case the entire upgrade workflow is stuck. The customer wants to skip the test step.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**db_type**: Specify the database engine, which can be mysql, polaro, redis, or mongo.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Restore status and delete residual MySQL testing instances**

**caused by task interruption**

In most cases, the system will automatically delete testing instances. However, if the testing task is interrupted, the system will fail to delete the testing instances through the testing task. In this case, you need to manually handle these instances. Deleting the residuals of testing tasks has no impact on the cloud platform.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**custins_id**: Specify the ID of the instance.
**task_id**: Specify the ID of the interrupted task. You can navigate to the **Task**
**Management** page and then go to the task details page to view the task ID.
**pengine_id**: Specify the Pengine ID. You can navigate to the **Task Management** page
and then go to the task details page to view the Pengine ID.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Forcefully cancel a MySQL instance backup task**

Use this script only in emergency scenarios in which backup anomalies occur. If the instance backup task remains in the `Check` state and cannot be manually canceled, you can run this script to forcefully delete the record of the task. This script fixes backup anomalies to avoid risks. Therefore, it does not pose any risks.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**custins_id**: Specify the ID of the instance.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Forcefully restart a MySQL instance**

When the status of a MySQL instance is abnormal and it cannot be restarted in the console (for example, the `The process doesn't have the permission to invoke the program. Please` `contact with RDS operator` error is thrown), you can run this script to restart the instance.

**Important**

Business impact: If you forcefully restart the instance, the instance will be disconnected from the application during the restart process. Confirm with the business owner before you restart the instance and perform this operation during off-peak hours. Limits: This script does not support instances that have TDE enabled.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**custins_id**: Specify the ID of the instance.
**hostins_id**: Specify the ID of the host. You can view the host ID on the **Basic**
**information** page of the instance.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Delete expired historical data or logs in OSS**

After OSS storage usage analysis, large amounts of expired full or incremental backup files are identified in the `rds-backup` bucket. These files have exceeded the retention period of historical backups. If you do not delete them promptly, the OSS storage usage will consistently increase and cause backup task failures.

**Important**

Business impact: This script targets only expired historical data. It does not affect production instances. Risks: If you accidentally delete a valid backup file, historical data will be lost. In this case, you will fail to restore data to a specific point in time. Before you run this script, strictly check the files to delete and their TTLs.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**remain_days**: Specify the time range within which historical data is deleted. This
parameter specifies the number of days before which historical data is deleted. Specify at least eight days in case the up-to-date data is accidentally deleted.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Address the issue that the incremental logs of MySQL**

**instances are not uploaded or deleted**

This script only revises the metadata logic on the control plane side. It does not affect production instances.

**Use scenarios**

Abnormal OSS storage usage: The storage usage of `rds-backup` is excessively high and the data volume continuously increases. This means that incremental logs failed to be archived to OSS. High local disk usage: Local binary logs or other incremental logs are accumulated because the log cleanup mechanism failed to take effect. Consequently, the disk usage of the instance has exceeded the threshold and triggered an alert.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management**.
3. Click **Execute** in the **Operation** column of the script.
4. In the panel that appears, read the script details, including the script description, affected
entities, risk level, and possible risks. In the **Parameter settings** section, configure the following parameters:
**custins_id**: Specify the ID of the instance.
**hostins_id**: Specify the ID of the host. You can specify at most two host IDs and separate
them with a comma (,). You can go to the **Basic information** page of the instance to view the host ID.
**Execution reason**: Specify the execution reason for review.
5. Click **Confirm execution**.

**Common operations**

**View the details of a script**

Click **Script details** in the **Operation** column of a script. In the panel that appears, you can view the script description, affected entities, number of executions, number of successful executions, risk level, and detailed risk information.

**View script execution records**

You can view the execution records of a single script or view the execution records of all scripts. You can also view the review progress, execution status, and detailed logs by using either of the two methods. You can view the following detailed information by using either of the two methods.

| Execution details | Description |
|---|---|
| Review informatio n | You are redirected to the review page of the O&M change console. On this page, you can approve, reject, or transfer review tasks. |
| Execution informatio n | Click Execution Information to view the execution status, reason, execution result, and start time and end time. |
| Execution process | You are redirected to Apsara Stack Inspection System, which displays the real-time execution logs and tracks the execution process in a more fine-grained manner. |

**Method 1: View the execution records of a single script**

Click **Execution record** in the **Operation** column of a script. In the panel that appears, you can view the review progress, execution status, and detailed logs of historical tasks.

**Method 2: View the execution records of all scripts**

In the left-side navigation pane, choose **Intelligent O & M > Automated script**
**management > Execution record**. On this tab, you can view the review progress,
execution status, and detailed logs of all historical tasks.

**Download script execution logs**

Click **Execution record** in the **Operation** column of a script. In the panel that appears, click
**Download logs** to download all execution logs of the current task.

**Disable a script**

Click **Disable** in the **Operation** column of a script and click **OK** in the message that appears to disable the script.

**Terminate the execution of a script**

You can terminate only script execution tasks in the **Pending approval**. You cannot terminate succeeded or failed tasks. Click **Execution record** in the **Operation** column of a script. In the panel that appears, choose
**> Termination**.

### 2.5 Host management

#### 2.5.1 Host software package management

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

**Important**

Uninstalling a package is a high-risk operation. If a running database instance depends on dynamic libraries or binary files within the package, forcibly uninstalling it can cause missing dependencies, which may prevent the database instance from starting or lead to downtime. Before you proceed, ensure that no critical instances are running on the target host, or that you have a comprehensive disaster recovery and rollback plan in place.
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

#### 2.5.2 Physical machine groups

ApsaraDB Operations and Maintenance System Smart Edition allows you to create physical machine groups to build independent logical resource pools in order to physically isolate underlying hardware resources and schedule them in a fine-grained manner. This way, your businesses are able to use resources exclusively and stably.

**Background information**

You can use the **physical machine group** feature to create a resource pool consisting of multiple physical machines. The physical machines in the resource pool are isolated from other resources. This feature provides the following benefits: You can create different physical machine groups for database instances of different levels and types to physically isolate resources. You can isolate physical machines used in staging environments from those used in production environments in case testing and production instances are created on the same physical machine. This prevents stress tests on testing instances from compromising the performance of production instances. You can create different resource pools for legacy machines and new machines in model upgrade scenarios. The physical machine group feature is supported only by PolarDB-X V2.0 instances. After you create a physical machine group, you can specify it when you create a database instance in the Apsara Uni-manager Management Console. For more information, see the Create an instance topic in User Guide of the corresponding service.

**View all physical machine groups**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console.
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

Before you delete a physical machine group, make sure that all instances deployed on the physical machine are cleared.
1. On the **Physical Machine grouping** page, find the physical machine group that you want
to delete and click **Delete** in the Operation column.
2. In the message that appears, click **OK**.

### 2.6 Software package management

**management**

This topic describes the three key operations that you can perform to manage software packages on ApsaraDB Operations and Maintenance System Smart Edition: enable or disable software packages, batch install or uninstall software packages, and query software package operation records.

**Use scenarios**

Cluster scale-out and version consistency assurance Scenario: During the scale-out of a database cluster, the initial version of new nodes differs from that of the existing nodes. Benefit: You can batch install software packages of the specified version to ensure that all cluster nodes use the same version. This helps avoid compatibility issues. Emergency fixing and version rollback Scenario: Known bugs are identified in the current version, or performance regression occurs after a new version is installed. Benefit: You can batch install patches to quickly fix bugs. When an upgrade exception occurs, you can uninstall the new version and roll back to a stable version to minimize the service downtime. Canary release and circuit breaking Scenario: At the early stage of a new release, you need to control the impact scope of risks and prevent the spread of bugs. Benefit: Control the distribution of a software package by enabling or disabling it. You can enable a software package for a specific host (canary release). After you confirm that the package does not pose risks, distribute it to all hosts. If critical bugs are identified, disable the package immediately (circuit breaking).

**Usage notes**

ApsaraDB Operations and Maintenance System Smart Edition is not completely compatible with the certificate system of the old version of ApsaraDB Operations and Maintenance System. Therefore, before you navigate to certain pages on ApsaraDB Operations and Maintenance System Smart Edition, complete authentication in the old version of ApsaraDB Operations and Maintenance System.

**Supported database engines**

**Only the following software packages based on the Apsara Infrastructure**

**Management architecture are supported**:
RDS MySQL PolarDB for MySQL Primary/Secondary Edition PolarDB PostgreSQL PolarDB for PostgreSQL (Compatible with Oracle)

**Enable and disable a software package**

1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Package Management > Package List**. On the
Package List page, find the desired package and click **Disable** or **Enable** in the **Operation** column. Disable: A disabled software package can no longer be installed on hosts. Enable: An enabled software package can be installed on hosts.

**Install and uninstall software packages**

You can install a software package on multiple hosts or uninstall it from multiple hosts at a time. Take note that the **OS version** and **chip architecture** of the hosts and software package must be the same. Otherwise, the hosts are not displayed.

**Important**

Uninstalling a software package is a high-risk O&M operation. If a database instance relies on dynamic libraries or binary files in the package, forced uninstallation may result in missing dependencies. Consequently, the database instance will fail to start or the service will be interrupted. Before you uninstall a software package, make sure that no important instances are running on the hosts or formulate disaster recovery and rollback plans in advance.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Package Management > Package List**. On the
Package List page, find the desired package and click **Host management** in the
**Operation** column.
3. In the panel that appears, select one or more hosts and click **Installation** or **Uninstall**.
Install: Make sure that **Not installed** is displayed in the **Installation status** column of a host before you select the host. Uninstall: Make sure that **Installed** is displayed in the **Installation status** column of a host before you select the host.
4. In the dialog box that appears, select **Operating Instructions**, specify **Operation**
**reason**, and click **OK**.
In the host management panel, you can view the progress in the Installation status column of the host. Install: If the status changes from **Installing** to **Installed**, the installation is complete. Uninstall: If the status changes from **Uninstalling** to **Uninstalled**, the uninstallation is complete.

**Query software package operation records**

You can query whether software packages are enabled, disabled, installed, or uninstalled. This helps meet the requirements for O&M compliance and fault postmortem.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition.
2. In the left-side navigation pane, choose **Package Management > Package List**. On the
Package List page, find the desired package and click **Change record** in the **Operation** column. The panel displays each operation, the time when the operation was performed, and the result of the operation. You can specify filter conditions (time range or operation) above the list to quickly find specific operations.

## 3 文档标题缺失，请补全后重新导出

### 3.1 Log in to ApsaraDB Operations and Maintenance System

**and Maintenance System**

This topic describes how users, such as O&M engineers, log in to ApsaraDB Operations and Maintenance System.

**Use the Apsara Uni-manager Operations Console**

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, click **Product**
**Operation**. In the **Databases** section, select **ApsaraDB O&M System**.

### 3.2 Home page

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

### 3.3 Manage instances

#### 3.3.1 Instance list

This topic describes how to view the information about instances, such as the basic information, data links, databases, and accounts, in the instance list.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, choose **Instance management > Instance List**. On the Instance List page, you can perform the following operations: Click **Batch query**. In the Batch query dialog box, enter instance names to query multiple instances at a time. Click **Advance search** and configure parameters such as Database type and Instance status to query instances. Find an instance that you want to manage and click its name to go to the Instance details page. You can view the instance information and manage the instance. For more information, see Diagnose an instance, Manage multiple instances at a time, Use the instance dashboard, and Manage instance migration plans.

#### 3.3.2 View instance details

On the Instance Details page, you can view the basic information of the instance and perform O&M operations.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
For a specific database cluster instance, such as Tair (Redis OSS-compatible) or AnalyticDB for PostgreSQL, choose **Instance management > Cluster instance List**.
3. On the Instance List page, find the instance that you want to manage and click its name in
the **User instance name** column. You can search for the instance by entering keywords in the search box in the upper part of the page. You can also click **Advance search** to filter instances by condition.
4. On the **Instance details** page, you can view the basic information of the instance. In the
lower part of the page, you can click the buttons to perform quick O&M operations. You can also click a menu in the left-side navigation pane to go to the corresponding page to perform more O&M operations on the instance. For more information about the instance O&M capabilities supported in the ApsaraDB Operations and Maintenance System console, see Instance O&M overview.

**Instance O&M overview**

The following table describes parameters for the new version of the console. If you use the previous version, click **Switch to New Version** at the top of the page. The O&M capabilities vary across instances based on the database engines. For more information about the supported O&M capabilities, see the ApsaraDB Operations and Maintenance System console.

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

#### 3.3.3 General instance O&M

##### 3.3.3.1 Important Notes

**Read before operation**

**Warning**

Some operations described in this section, such as instance restart, minor engine version update, and backup and restoration, involve core changes to the underlying infrastructure. These operations are irreversible or high-risk. Improper operations may lead to data loss, service interruption, or performance jitter. Before you perform any O&M operations, carefully read the relevant tutorials and the precautions and key risk reminders on the console interface. If necessary, perform operations under the guidance of Alibaba Cloud professional technicians. Once you click Submit, Confirm or similar commands, it is deemed that you have been fully aware of all potential risks and voluntarily bear all the consequences arising therefrom. Proceed with caution.

##### 3.3.3.2 Check instances

This topic describes instance-related check operations to help you resolve issues quickly.

**Background information**

Primary/secondary synchronization, version consistency, and read/write isolation are fundamental to database security and stability. Instance diagnostics empower O&M personnel to probe the underlying database status by using SQL statements. This enables rapid verification of instance health and security during routine inspections, troubleshooting, or disaster recovery drills.

**Applicable scenarios**

Routine health inspection: regularly verifies that the primary/secondary latency is zero, versions are consistent, and read/write roles are correct to prevent potential risks. Emergency troubleshooting: quickly identifies the root causes of data inconsistencies, write failures, or switchover exceptions (such as synchronization interruptions, version mismatches, or configuration errors). Change and drill verification: verifies whether instance status meets expectations after upgrades or switchover drills, or before major security events. Compliance and security audit: ensures that instances run on approved secure versions and eliminate unauthorized write paths.

**Usage notes**

Pre-check of whitelists: If a `not in whiteList` error is returned when you execute an SQL statement, you must log in to the console and add the current IP address to the whitelist of the instance. Otherwise, no diagnostic results can be obtained. Differentiation of the primary and secondary roles: When you run commands, you must clearly distinguish between the primary and secondary databases. Despite separate selection of the primary and secondary databases on the operation interfaces, evaluation criteria vary. For example, `read_only` must be set to OFF on the primary database and to ON on the secondary database, whereas synchronization status is monitored on the secondary database. Do not confuse the roles of the primary and secondary databases, as this will lead to incorrect status assessments. If exceptions occur, forced repairs or restarts without authorization are not allowed. You should retain the evidence and immediately contact Alibaba Cloud technical support to prevent spreading the failure impact or causing data loss.

**Procedure**

MySQL is used in the following operations. You can refer to the actual environment for specific details.

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
normal. If the results do not meet expectations, contact Alibaba Cloud technical support. If a `not in whiteList` error is returned, check the whitelist settings. Slave_IO_Running : Yes Slave_SQL_Running : Yes Seconds_Behind_Master : 0

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

##### 3.3.3.3 Diagnose an instance

The instance diagnosis feature of ApsaraDB Operations and Maintenance System provides comprehensive database health check and performance analysis services. The feature supports real-time monitoring of instance resource usage, performance metrics, and internal engine status. This helps O&M personnel accurately locate performance bottlenecks, efficiently troubleshoot exceptions, and optimize instance configurations. This comprehensively improves the efficiency and stability of database O&M.

**Scenarios**

Performance bottleneck analysis: When an instance experiences high CPU utilization, saturated IOPS, or high memory usage, this feature can be used to locate the resource usage bottleneck and identify the source of abnormal consumption. Troubleshooting of exceptions: When an instance shows a sudden increase in connections, an abnormal primary/secondary latency, or slow request response, this feature can be used to quickly locate the root cause of the fault and shorten the mean time to repair (MTTR). SQL optimization: When your business returns slow queries and needs to identify highconsumption statements, this feature can be used to obtain the list of slow SQL statements and optimization suggestions. Emergency O&M operations: When you need to directly execute diagnostic SQL statements or view the underlying engine status in the console, this feature allows direct connection to the instance to execute specific diagnostic commands.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. On the Instance List page, find the required instance and click its name in the **User**
**instance name** column.
4. In the **Instance Details** section, click **Instance diagnosis**. You can click the
corresponding tab to view data or perform operations. The diagnostic capabilities vary across different database engines. The actual feature tabs displayed are subject to the console configuration. The following description takes PolarDB for MySQL as an example.

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

##### 3.3.3.4 Restart an instance

ApsaraDB Operations and Maintenance System supports restarting various database instances to handle service exceptions, enable configuration changes, or meet maintenance requirements.

**Usage notes**

**Feature coverage**: The instance restart feature applies to most database instance types
such as ApsaraDB for RDS, PolarDB, and AnalyticDB. However, advanced configurations such as cold/hot restart policies and node selection are only supported for AnalyticDB instances.
**Service interruption**: During the restart, the instance will be unavailable for a short
period of time. We recommend that you perform this operation during off-peak hours.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance in the **User instance name** column to go to the
Instance details page. Scroll down to the bottom of the page and click **Restart an**
**instance**.
4. Confirm or configure the restart policy and click **OK**. This topic uses `AnalyticDB` as an
example to describe operations on the restart page. The restart policies displayed or supported on the page vary based on the database type. For more information, see the restart policies displayed on the page.

| Parameter | Description |
|---|---|
| Restart policy | Hot start: Only processes in the container are restarted. The original environment of the container is retained. This is similar to docker restart . It is suitable for quick recovery from process exceptions with short service interruption. Cold start: The container is destroyed and rebuilt, and the runtime environment is reset. This is similar to docker rm && docker run . It is suitable for solving the environmental pollution of the container or deep-seated state issues, with longer service interruption. |
| Concurrencie s | Controls the number of nodes that are restarted at the same time. A smaller value reduces impact on services but increases total duration; a larger value improves parallelism but causes higher instantaneous load. We recommend that you configure the settings based on your business tolerance. |
| Host instance | Lists all compute nodes under the current instance. You can select specific nodes as needed for a rolling restart. For example, you can restart only abnormal nodes to avoid impacting overall services caused by a full restart. |

##### 3.3.3.5 Migrate an instance

ApsaraDB Operations and Maintenance System supports migrating instances across zones or subdomains. Migration applies to scenarios such as resource scheduling, disaster recovery drills, and hardware upgrades. You can configure migration for primary instances, standby instances, and read-only (RO) instances.

**Preparations**

Before submitting a migration task, we recommend that you record the host information of the current instance. Check whether the physical instance (the primary, secondary, or read-only node) to be migrated and its associated logical instance have any running tasks or abnormally interrupted tasks. If such tasks exist, resolve or terminate them before proceeding with the migration.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance in the **User instance name** column to go to the
Instance details page. Find the migration entry: The entry may vary slightly by database engine. The actual displayed items are subject to the console configuration. Migration entry 1: On the **Basic Information** page, scroll down to the bottom of the page and click
**Migration**.
Migration entry 2: a. On the **Basic information** page, find the **Sub-instance Information** section. In this section, click the ID of a standby instance or a read-only instance. This example demonstrates how to migrate a standby instance. b. Scroll down to the bottom of the page and click **Migration**.
4. Configure the migration destination and click **Submit**.
Migration configuration items may vary slightly by database engine. The actual displayed items are subject to the console configuration. Virtual Private Cloud (VPC) instances do not support random zones. The vSwitch ID is required during cross-zone migration. The primary and secondary nodes must be in the same zone in primary zone mode,. Commercial instances can only be migrated to commercial subdomains, and internal instances can only be migrated to ODBS subdomains.

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

##### 3.3.3.6 Upgrade the minor version

ApsaraDB Operations and Maintenance System supports secure and controllable minor version upgrades for database instances. This type of upgrade usually includes performance optimization, introduction of new features, and fixes for known issues, helping ensure stable and efficient operation of databases.

**Prerequisites**

The instance for which you want to upgrade the minor version must be a non-temporary instance and must be in both In Use and Unlocked states.

**Usage notes**

If you do not specify the target version number, the system upgrades the instance to the latest minor version in the series by default. When you update the minor engine version of your PolarDB for MySQL V2.0 cluster, applications may temporarily disconnect from your cluster for 30 seconds. We recommend that you update the minor engine version during off-peak hours or make sure that your application is configured to automatically reconnect to the cluster. Once the minor version is upgraded, you cannot downgrade the version to an earlier version. Exercise caution when you perform this operation.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**.
3. Locate the required instance in the instance list and click the corresponding **User instance**
**name** to go to the Instance details page.
4. In the lower part of the **Basic Information** page, click **Version Upgrade**, configure the
following parameters, and then click **Submit**. This document uses the minor version upgrade of PolarDB for MySQL Primary/Secondary Edition as an example. Configuration items and interface display may vary by database type. The actual displayed items are subject to the console configuration.

| Configuratio n item | Description |
|---|---|
| Database version | Displays the major version of the current instance. The system only supports minor version upgrades within the same major version. |

| Small version number | Select the minor version to upgrade to. The current minor version of the instance will appear on the right for comparison. |
|---|---|
| Specify method | Operation and maintenance time switching: The upgrade is performed during the pre-configured maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic Information page of the instance. Switch now: The upgrade immediately takes effect and may affect your business. Specified time switch: You can create a custom time for the upgrade, which requires manual configuration. |

**View the upgrade progress**

After the upgrade task is initiated, you can go to the **Task Management** page to view the upgrade progress.

##### 3.3.3.7 Manage instance parameters

ApsaraDB Operations and Maintenance System supports manual configuration of instance kernel parameters and viewing of the managed parameters, which can be used for information query or fault troubleshooting scenarios. The instance parameter management capabilities vary by database engine. The actual displayed capabilities are subject to the console configuration.

**Kernel – instance parameters**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. Click the name of the required instance to go to the **Basic Information** page.
You can enter a keyword in the search box to quickly query the required instance. You can also click Advance search to customize filter conditions to locate the required instance.
4. In the left-side navigation pane, click**Kernel-instance parameters**. The capabilities
supported under different tabs on this page are as follows: .

**Important**

If the new parameter settings take effect only after you restart the instance, we recommend that you restart the instance during off-peak hours and make sure that your application is configured to automatically reconnect to the instance.

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
You can enter a keyword in the search box to quickly query the required instance. You can also click Advance search to customize filter conditions to locate the required instance.
4. In the left-side navigation pane, click **Management-instance parameters**.
On the **Management-instance parameters** page, you can view the parameters, including **Parameter name**, **Parameter value**, and **Modify**.

##### 3.3.3.8 Change specifications

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

**Procedure**

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

##### 3.3.3.9 Change storage capacity

This topic describes how to modify the storage capacity of an instance to help you resolve issues efficiently.

**Usage notes**

The primary instance is in the Running status and has no pending modification tasks, such as upgrades, migrations, and backups. We recommend that you perform this operation during off-peak hours to avoid the risk of extreme network fluctuations. The storage capacity after scale-down cannot be less than the total used storage space of the instance plus 20 GiB. The change takes effect on the logical instances of the cluster. If you modify the storage specifications of the primary instance, the changed specifications are applied to all readonly and secondary nodes in the cluster. Proceed with caution.

**Scenarios and common issues**

**Storage upgrade (scale-up)**

Support business growth: When business data grows rapidly, and the disk usage approaches the threshold (such as 80%), emergency scale-up is required to prevent the database from entering the read-only status or service interruption due to full storage. Reserved buffer space: Scale up storage in advance to reserve sufficient write buffer space before large-scale promotions, batch data import, or historical data archiving. Remove performance limits: In specific scenarios, a larger storage quota may be associated with a higher IOPS limit (depending on the specific instance specification policies) to improve the throughput.

**Storage downgrade (scale-down)**

Cost optimization: After business data is deleted, such as large tables, and historical data is archived, the actual usage is much lower than the current quota. Downgrading the configuration releases idle resources and immediately reduces the monthly bill. Fix over-provisioning: Rectify the resource waste caused by inaccurate estimations in the initial project stage, and adjust the storage to align with actual business needs.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the lower part of the Basic information page, click **Storage space changes**.
4. In the dialog box that appears, enter the new storage capacity and click **Confirm**.

**View task details**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Task Management > Instance tasks** page, you can view the task status.
You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks. You can customize list items. You can select the task fields that you want to view based on your needs.

##### 3.3.3.10 Perform an HA switchover

This topic describes how to manually perform an HA switchover and helps you efficiently resolve related issues.

**Background information**

In most cases, when the primary node fails, the system automatically performs an HA switchover to restore services. Manual HA switchover is usually performed in active O&M scenarios, that is, manually transferring traffic from the current primary node to the secondary node without waiting for a fault to occur, promoting the original secondary node to the new primary node.

**Preparations**

Before you perform an HA switchover, ensure that the following items are checked: Instance status check: Ensure that the instance is in the Running status and no other operations (such as specification modification, restart, or backup and recovery) are being performed. Primary/secondary synchronization status: Ensure that data synchronization on the secondary node is normal. Ensure that the latency is 0 or within the allowable range. The recommended value is less than one second. If the synchronization of the secondary node is delayed, a forced switchover may cause data loss. Secondary node health check: Ensure that the host where the secondary node is located has sufficient resources, network connectivity is normal, and no hardware alerts are generated.

**Usage notes**

We recommend that you perform this operation during off-peak hours and ensure that a complete automatic reconnection mechanism is in place to avoid the risk of extreme network fluctuations. After the switchover, you need to monitor the task progress in real time until completion. If the task is interrupted or stalls for an extended period, you need to immediately contact Alibaba Cloud technical support. We recommend that you wait until the data synchronization between the primary and secondary data is complete before you perform the switchover.

**Scenarios**

Maintenance/upgrade of underlying resources: When the physical machines, hosts, or storage devices of the primary node need to be stopped for maintenance, firmware upgrade, or migration, manually switch services to the secondary node first to avoid service interruption. Troubleshooting: If the primary node experiences hardware issues or network jitters, but is not completely down, the system switches services to a healthy secondary node to avoid risks.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. In the lower part of the Basic information page, click **HA swtich**.
4. After you confirm that the primary/secondary information is correct, specify the **Switching**
**method** and **Specify method** parameters, and click Submit.
Switch now: This method is used for emergency avoidance. Operation and maintenance time switching: This method is suitable for routine O&M windows, such as early morning every day. The O&M task is automatically executed. Specified time switch: This method is suitable for specific change windows, such as application release.
5. After the operation, you can view the task progress on the **Task Management** page until
the task is completed. If the task is interrupted, contact Alibaba Cloud technical support. For more information about how to view task progress, see Manage instance tasks.

**Verify results**

After Step 4, the IP addresses and port numbers are reassigned to match the new primary and secondary roles. The HA task flow is completed normally.

**Rollback**

Repeat the procedure to swap the primary and secondary nodes.

##### 3.3.3.11 Lock an instance

This topic describes how to lock an instance to help you resolve issues.

**Usage notes**

Ensure that operations are performed during off-peak hours and your applications have an automatic reconnection mechanism to handle potential disruptions. For disk-full locks, you must first clear or expand the disk space. For rollback locks, forced restarts are strictly prohibited, and the root cause (such as high resource usage or failed changes) must be resolved before you attempt unlocking. After a task is submitted, continuous monitoring of the progress is required. If the task is interrupted or becomes unresponsive, retries without investigating the root cause are prohibited. You should immediately contact Alibaba Cloud technical support to prevent deadlock. After an instance is locked, it becomes read-only and affects your business. You must perform this operation within an O&M window and proceed with caution regarding execution risks.

**Applicable scenarios**

This topic lists only some applicable scenarios for reference. For situations not covered here, adapt your approach based on actual requirements. Cooling-off period verification for business unpublishing: Prior to instance deletion, manually lock the instance and enforce an observation period of at least 7 days. Proceed with permanent deletion only after you confirm no hidden dependencies or user complaints, which helps prevent accidental loss of production data. Emergency fault isolation and damage control: In the event of malicious attacks, abnormal SQL consumption, or data tampering, manually lock the instance immediately to cut off all connections. This prevents the spread of faults and buys time for troubleshooting. Resource exhaustion self-protection: When disk capacity is exhausted or hardware fails, the system automatically triggers a disk-full lock or migration lock. This prevents metadata corruption and ensures strong data consistency. Rollback protection for high-risk changes: When a specification change or upgrade fails, the system automatically triggers a rollback lock to freeze the instance status to prevent data from being inconsistent in the intermediate state.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**. On the
Instance List page, click the name of the instance that you want to manage.
3. On the Basic information page, click **Locking an instance** in the lower part of the page.
4. Specify **Lock mode** and **Locking reason**, and then click **Submit**.
5. View the task progress on the **Task Management** page until the task is complete. If the
task is interrupted, contact Alibaba Cloud technical support. For more information about how to view the task progress, see Manage instance tasks.

##### 3.3.3.12 Backup and restoration

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

**Important**

The temporary backup is valid for only 18 hours. If the temporary backup expires, you need to re-initiate it.
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

**Important**

The instance must have at least one successful and valid backup set before a restoration is performed. You can check the validity of a backup set in the **Valid** column of the backup list. Invalid or corrupted backup sets cannot be used for restoration. If no backup set is available, create a temporary backup.
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

To restore data to a point in time, make sure that: Log backup is enabled. A valid full backup set exists, and no overlaying restoration has occurred between two full backups. The target point in time is within the log retention period.
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

##### 3.3.3.13 Recreate a secondary database

If an exception occurs in the secondary database, you can recreate a secondary database to ensure the continuity of the primary/secondary high-availability architecture.

**Scenarios**

You must recreate a secondary database in the following conditions: The secondary database fails and cannot provide services. The data in the secondary database is damaged, which leads to data inconsistency between the primary and secondary databases or synchronization interruption. You need to replace the server where the secondary database resides due to reasons such as hardware upgrades, migration, and resource adjustment.

**Usage notes**

Secondary database recreation has no impact on the operations of the primary database or online services. If you want to recreate the secondary database because of an inconsistency between the primary and secondary databases, you must **trigger a backup of the primary database** first to prevent the secondary database from becoming invalid. We recommend that the primary database be backed up during off-peak hours. You can choose **Instance details** **>**
**Backup policy** and then click **Create a temporary backup** to create a temporary
backup. For more information, see Backup and restoration.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. On the Instance List page, find the instance that you want to manage and click its name to
go to the **Basic information** page. You can enter a keyword in the search box to quickly find the desired instance. You can also click Advance search to specify filter conditions for an exact search.
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

##### 3.3.3.14 Manage instance tasks

This topic describes how to view the progress and details of a task.

**View task details**

You can view the task details of an instance in one of the following ways based on the database storage type: Pengine instance tasks: local disk storage architecture. GrandCanal task list: shared storage architecture.

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
You can view the status of various tasks, such as all tasks, interrupted tasks, and suspended tasks. You can customize the task fields that you want to view based on your requirements.

##### 3.3.3.15 Disable instance allocation

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

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. You can perform the operation in two modes. Select one of the following modes based on
your business scenario:

**Fine-grained control of a single host**

i. In the left-side navigation pane, choose **Host management > System host**. On the page that appears, find the host that you want to manage and click **Details** in the
**Operation** column to go to the Host details page.
ii. On the Host Information tab of the Host details page, click **Turn off instance allocation** . iii. In the dialog box that appears, specify whether to permanently disable instance allocation. If you select **No**, you can specify a time to restore instance allocation. If you do not select a time, instance allocation will be restored seven days later by default. If you select **Yes**, the system will not automatically restore instance allocation, and you must manually enable instance allocation when needed. iv. Click **OK**.

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

#### 3.3.4 Other instance O&M

##### 3.3.4.1 Upgrade an instance from ApsaraDB RDS for MySQL Two-node Edition with Local Disks to PolarDB for MySQL Primary/Secondary Edition

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

**Procedure**

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
the User instance name column. You can search for the instance by entering keywords in the search box in the upper part of the page. You can also click **Advance search** to filter instances by condition.
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

##### 3.3.4.2 Common O&M operations for secondary PolarDB for MySQL nodes

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
If no secondary database exists, this button is unavailable.

**Perform an HA switchover**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the required
instance.
3. On the page that appear, click **HA switch**.
4. On the HA switch page, select the target node and click **Submit**.
HA switchover allows switching between read-write (RW) nodes and read-only (RO) nodes, as well as between RW nodes and secondary nodes. Switchover between RW nodes and secondary nodes is permitted only if there are no available RO nodes.

**View task details**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Task Management > Instance tasks** page, you can view the task status.
You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks. You can customize list items. You can select the task fields that you want to view based on your needs.

##### 3.3.4.3 Perform zone-disaster recovery switchover for PolarDB for PostgreSQL Shared Storage Edition

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

**Important**

During switchover, a transient connection interruption may occur once or twice within 30 seconds. After the switchover is complete, you can view the updated instance architecture in the
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

**Important**

Switching the standby node to read/write mode will delete and rebuild existing readonly nodes. During this period, the services of the read-only nodes are interrupted. Be aware of this risk and proceed with caution. After the switchover is complete, you can view the updated instance architecture in the
**Instance topology** section on the **Basic information** page.

##### 3.3.4.4 Query SQL information for PolarDB-X instances

**instances**

This topic describes how to view instance SQL information such as SQL log details (SLS), slow SQL details, SQL injection detection, and primary key statistics. The following example shows how to view SQL log details.

**Scenarios**

**Identify the causes of sudden high load:** Set the time range to 30 minutes before and
after the failure, sort by latency in descending order to find the top 5 most time-consuming SQL statements, and check with the development team for possible optimization.
**Verify the SQL performance after deployment:** Record the execution time of the
benchmark SQL statement before deploying a new version. Compare changes in execution time and the number of returned rows for the same SQL statements after deployment.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the left-side navigation pane, click **Instance SQL information**. On the page that
appears, click the **SQLLog details(SLS)** tab.
4. You can query SQL statements by **Date Time**, **Log type**, **Data sorting type**, or
**Keywords**.
Separate keywords with spaces during queries.
**SQL archive**:
Export current query results or save them to a historical archive database. This method is suitable for regularly backing up important SQL logs for subsequent auditing or review.
**SQL archive query**:
Access the query interface for archived historical SQL logs. Search for saved SQL records across different time periods.

##### 3.3.4.5 Handle failed PolarDB-X tasks

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

##### 3.3.4.6 Change PolarDB-X data node specifications

This topic describes how to change data node specifications and helps you resolve related issues.

**Usage notes**

After you change the data node specifications, the specifications of data nodes in the PolarDB- X instance become inconsistent. As a result, the instance operation methods change as follows: You cannot directly upgrade or downgrade a PolarDB-X instance. To upgrade or downgrade a PolarDB-X instance, you need to upgrade or downgrade the computing nodes and data nodes in the instance separately. You cannot scale in a PolarDB-X instance by changing the number of data nodes. To scale in a PolarDB-X instance, you need to delete the specified data nodes on the Data Node Management page.

**Procedure**

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
You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks. You can customize list items. You can select the task fields that you want to view based on your needs.

##### 3.3.4.7 Configure PolarDB-X instance resources

You can configure IOPS, CPU specifications, and disk space for instances. This topic uses IOPS configuration as an example to describe the detailed procedure and help you resolve issues quickly.

**Usage notes**

Do not arbitrarily increase the IOPS. This may overload the underlying storage, causing latency or even downtime. If you modify a logic instance, the IOPS configurations of the DN nodes are modified accordingly. You can also modify the IOPS configurations of each node separately. Configure a proper restoration time to avoid resource waste or security risks caused by forgotten restorations. Configure CPU specifications appropriately. An excessively low specification may result in slow SQL execution, connection timeouts, and transaction backlogs. After adjusting disk space settings, immediately perform actual capacity expansion or data cleanup, and restore the limits at an appropriate time. If you do not check the disk space, the disk space of the host may be exhausted. Proceed with caution.

**Scenarios**

Temporarily increase the upper limit of IOPS to ensure business continuity and prevent full disk I/O caused by a sudden burst of a large number of writes. Temporarily reduce the IOPS for throttling protection to prevent disk overload caused by malicious programs or abnormal SQL statements. Isolate problematic instances during troubleshooting and lower CPU quotas to check whether cluster pressure is relieved. Temporarily expand the disk quota when disk usage exceeds 95% to keep businesses running while arranging capacity expansion.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the left-side navigation pane, click **Configure an instance**. On the page that appears,
click the **Instance resource configuration** tab.
4. In the **Set IOSP** section, specify **IOPS** and **Recovery time**, and then click **Submit**.
5. In the message that appears, click **OK**.
After the configured restoration time expires, the IOPS value is restored within 5 minutes.

##### 3.3.4.8 Add proxy nodes to a Tair (Redis OSS-compatible) instance

**compatible) instance**

When business traffic increases or the load on existing proxy nodes becomes excessively high (for example, when CPU, memory, or network bandwidth reaches the threshold), you can scale out horizontally by increasing the number of Proxy nodes. This effectively distributes client request pressure, and improves overall system throughput and high availability.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Add Proxy Instance Node**.
4. In the dialog box that appears, enter the number of nodes and click **Submit**.

##### 3.3.4.9 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance

**primary/secondary synchronization buffer for a**

**Tair (Redis OSS-compatible) instance**

In high write-load scenarios, the latency of primary/secondary synchronization increases, causing data lag in the secondary database. This affects read consistency and failover reliability. In this case, you can increase the primary/secondary synchronization buffer to improve the primary/secondary synchronization throughput and reduce latency. This topic describes how to temporarily increase the primary/secondary synchronization buffer.

**Usage notes**

The value is automatically reset to the default after the instance restarts. Ensure that sufficient memory is available on the host before the change. We recommend that you perform the operation during off-peak hours, such as 02:00 to 04:00.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Temporarily scale-up the primary-**
**standby synchronization buffer**.
4. In the dialog box that appears, enter the target scaling ratio and click **Submit**.
The scaling ratio ranges from 1.0 to 5.0. This operation applies to normal, db, and logic instances. When performed on a logic instance, the operation takes effect on all underlying db instances. normal instance: Also known as a Redis-Normal instance. A standard Redis instance in single-node or primary-replica architecture. db instance: a subinstance that acts as the data node in the Redis-Logic cluster architecture. It refers to the DB-role subinstance that physically stores data in the Cluster Edition. logic instance: a Redis-Logic cluster instance that has multiple roles of Proxy, CS, and DB. It is a clustered deployment that supports read/write splitting and shard routing.

#### 3.3.5 Manage instances in batches

##### 3.3.5.1 Migrate multiple instances at a time

This topic describes how to migrate multiple instances at a time.

**Procedure**

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
Instances that use HAProxy do not experience service interruptions only if migrated within the same cluster. Batch instance migration operations are not reviewed. Proceed with caution.

**References**

You can click **Batch instance migration success list** or **Batch instance migration**
**failure list** in the upper part of the **Batch instance migration** page to view the details of
the migrated instances.

##### 3.3.5.2 Modify multiple instance parameters at a time

**time**

This topic describes how to modify multiple instance parameters at a time.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. On the page that appears, click **Batch instance parameter refresh** in the **Instance**
**batch operations** section.
5. Select the clusters for which you want to modify the parameters and click **Select**
**parameter Template**.

**Important**

Instance parameter changes may cause risks such as transient connections or unavailability. You can modify the parameters by following the instructions on the console.
6. On the page that appears, select the parameter template and click **Next Step**
7. Select the instances and click **Submit**.

**References**

You can click **Batch refresh parameter instance successful list** or **Batch refresh**
**parameter instance failure list** in the upper part of the **Batch instance parameter**
**refresh** page to view the details of the modified parameters.

##### 3.3.5.3 Modify DIY parameters for multiple instances at a time

**instances at a time**

This topic describes how to modify DIY parameters for multiple instances at a time.

**Procedure**

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

##### 3.3.5.4 Modify Redis parameters for multiple clusters at a time

**clusters at a time**

This topic describes how to modify multiple Redis parameters at a time.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance batch management**.
4. Click **Batch Redis parameter refresh** in the **Instance batch operations** section.
5. In the **redis2.8Cluster** list, select the clusters for which you want to modify parameters.
6. In the list in the lower part of the page, find the parameter that you want to modify, enter a
value in the **Set value** column, and then click **Save**.
7. In the **Modify configuration** message, click **Determine**.

##### 3.3.5.5 Manage tasks in batches

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

##### 3.3.5.6 Manage batch task types

This topic describes how to create a type of batch tasks.

**Procedure**

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

##### 3.3.5.7 Manage SQL templates

This topic describes how to create an SQL template.

**Procedure**

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

Custom SQL templates support only SELECT statements and can be used only for DBaaS databases. The creation of SQL templates requires BPMS approval. To prevent the SQL template from being accidentally executed by other members, which could result in batch tasks being sent to incorrect instances, we recommend that you provide a detailed description of the template name and the reason for its addition in the SQL template.
7. Click **Submit**.

#### 3.3.6 Manage instance plan migration

The instance plan migration list can be uploaded in two ways: batch submission by instance or by host IP address. This topic describes the detailed procedures for instance plan migration.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance plan migration**
**management**.
4. Select an upload mode for the instance migration plans.
Mode 1: If you select Submit by instance and non-migratable instances are detected, the system blocks the entire submission. Mode 2: If you select Submit by host IP address, the system directly filters out non-migratable instances.
5. Click **Download template file** and fill in the template file.
6. Click **Select File** and select the completed template file.
7. Click **Submit**.

**References**

You can click **Push success list** or **Deleted list** in the upper part of the **Instance plan**
**migration management** page to view details.

#### 3.3.7 View the instance dashboard

This topic describes how to view metrics of instances, such as CPU utilization and connection utilization, on the instance dashboard.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, choose **Instance management > Instance List**.
3. In the upper part of the **Instance List** page, click **Instance dashboard**.
4. You can view the CPU utilization, connections, IOPS, and disk utilization of an instance. The
top 20 items are displayed by default.

### 3.4 Host management

#### 3.4.1 Create a host

This topic describes how to create a host.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. In the upper part of the System host page, click **Emergency response plan**.
4. On the Host Information page, click **New host**.
5. In the dialog box that appears, configure the parameters and click **Submit**.

#### 3.4.2 Configure multiple hosts at a time

This topic describes how to configure multiple hosts at a time.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. On the System host page, select the hosts that you want to configure and click **Batch**
**configuration** in the upper part of the page.
4. In the Batch configuration parameters dialog box, configure the parameters and click
**Submit**.

#### 3.4.3 View host information

This topic describes how to view the information about a host.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. Search for the host you want to view by its IP address or host name.
4. Click the IP address of the host and view information on the **Host details** page. The
information includes the CPU utilization, memory usage, disk usage, and the number of instances. You can also click the options in the Host details section to view the information about host instances, performance, backups, and accounts.

#### 3.4.4 Physical machine group

ApsaraDB Operations and Maintenance System allows you to use the physical machine group feature to build an independent logical resource pool. This enables physical isolation and finegrained scheduling of underlying hardware resources to ensure resource exclusivity and stability across different business scenarios.

**Background information**

You can use the **physical machine group** feature to create a resource pool for multiple physical machines, enabling isolation of physical machine resources. This feature provides the following practical values: Database instances of different levels and categories can use separate physical machine resource pools to achieve physical isolation. The resources of physical machines in the test environment are isolated from those in the production environment. This prevents the test instance and the production instance from being created on the same physical machine and prevents the production instance from being affected in scenarios such as performance stress testing on test instances. During the replacement of old and new machine models, separate resource pools can be planned for legacy and new machines for independent use. The physical machine group feature is currently supported only for PolarDB-X 2.0 instances. After creating a physical machine group, you can specify the physical machine resource pool to which the instance belongs when you create a database instance in the Apsara Uni-manager Management console. For more information, see Create an instance and other relevant chapters in the corresponding User Guide.

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

Before you delete a physical machine group, make sure that all instances deployed on the physical machine are cleared.
1. On the **Physical Machine grouping** page, find the physical machine group that you want
to delete and click **Delete** in the Operation column.
2. In the message that appears, click **OK**.

#### 3.4.5 Manage host software packages

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

**Important**

Uninstalling a package is a high-risk operation. If a running database instance depends on dynamic libraries or binary files within the package, forcibly uninstalling it can cause missing dependencies, which may prevent the database instance from starting or lead to downtime. Before you proceed, ensure that no critical instances are running on the target host, or that you have a comprehensive disaster recovery and rollback plan in place.
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

### 3.5 Cluster management

#### 3.5.1 Configure cluster parameters

This topic describes how to configure cluster parameters.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. On the **System Cluster** page, select the cluster for which you want to modify parameters,
click **Cluster parameter settings**, configure the parameters, and then click **Submit**.

**Important**

You can configure only one cluster at a time. Different database types, such as MySQL and MongoDB, support different parameters. The actual displayed parameters are subject to the console configuration.

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

#### 3.5.2 Manage service types

This topic describes how to manage service types.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Cluster management**.
3. In the left-side navigation pane, click **Service Type Management**. The **Service Type**
**Management** page appears.
Find the service type that you want to modify and click **Edit** in the **Operation** column to modify the service type. Find the service type that you want to delete and click **Delete** in the **Operation** column to delete the service type.

#### 3.5.3 Manage service nodes

This topic describes how to create, modify, and delete a service node.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. In the Cluster management section, click **Service node management**.
In the upper part of the page, click **New service node**. In the dialog box that appears, configure the required parameters and click **OK**. Find the service node that you want to modify and click **Edit** in the **Operation** column to modify the service node. Find the service node that you want to delete and click **Delete** in the **Operation** column to delete the service node.

#### 3.5.4 Manage DB configuration templates

This topic describes how to manage DB configuration templates.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Cluster management**.
3. In the Cluster management section, click **DB configuration template** to go to the **DB**
**configuration template** page.
In the upper part of the page, click **New DB template**, enter the template information, and then click **Save** in the **Operation** column. Find the template that you want to modify, click **Edit** in the **Operation** column to modify the template, and then click **Save** in the **Operation** column. Find the template that you want to delete and click **Delete** in the **Operation** column. In the dialog box that appears, click **OK** to delete the template.

#### 3.5.5 Manage Fangcunshan clusters

This topic describes how to manage Fangcunshan clusters.

**Procedure**

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

#### 3.5.6 Manage locations

This topic describes how to configure the locations of clusters.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Cluster management**.
3. In the left-side navigation pane, click **Location**.
4. On the page that appears, search for clusters by keyword and configure their locations.
You can also perform cluster consistency check and subdomain consistency check on this page. Click **Add** next to the required unit, region, or zone to add a location node, and then click
**Submit**.
Click **Parameters** next to the required unit, region, zone, or subdomain to add, modify, or delete parameters. Click **Delete** next to the required unit, region, zone, or subdomain to delete a unit, region, zone, or subdomain.

### 3.6 Task management

#### 3.6.1 Manage interrupted tasks

This topic describes how to manage interrupted tasks, including user instance tasks, host instance tasks, and host tasks. This topic uses a user instance task as an example to describe how to manage interrupted tasks.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
**console**, click **Task Management**. In the upper-left corner of the **Instance tasks** page,
select **Interrupted tasks** from the drop-down list. If interrupted tasks exist, perform the following steps. If no tasks are displayed, skip the remaining part of this topic.
3. Click a task in the **Task name** column to view and analyze the cause of the task failure.
In most cases, if you encounter issues such as abnormal status of secondary databases, connection timeout errors, or password errors, you can log in to the required instance by using the instance IP address and fix the issue.
4. After you fix the issue, find the task and click **Operation** in the **Operation** column.
5. On the page that appears, click **Perform tasks**.
6. In the **Re-execute the task** dialog box, click **Current step retry** to run the task again.

**Important**

If you want to retry the task starting from a specific step, click **Continue from the**
**specified step**. We recommend that you do not retry the task if you are not familiar
with the task or purposes of its steps.
7. In the upper-left corner of the Instance tasks page, select **Running tasks** from the drop-
down list to view the status of the task. If the task fails again, repeat the preceding steps.

#### 3.6.2 Manage temporarily closed tasks

This topic describes how to manage temporarily closed tasks.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
console, click **Task Management**. In the upper-left corner of the Instance tasks page, select **Temporarily Closed tasks** from the drop-down list. Click a task name in the **Task name** column. In the message that appears, view the steps of the task. Find a task and click the operation object name in the **Operation object** column to view the task logs of this operation object. Find a task and click the operator name in the **Executor** column to view the information about the operator. Find a task and click **Operation** in the **Operation** column to view the reason why the task is temporarily closed. On the page that appears, click **Perform tasks** to retry the task. On the page that appears, click **Intervention record** to view the intervention records of the task. Find a task and click **Add remarks** in the Operation column to add remarks for the task.

#### 3.6.3 View workflow O&M information

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

### 3.7 System management

#### 3.7.1 Feature Overview

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

#### 3.7.2 Change the unified storage location of logs

**logs**

By default, database system logs, such as audit logs, are written to SLS-inner, which is an internal logging service, and cannot be directly accessed by users. If you have clear global log governance requirements or centralized log analysis requirements, you need to write logs to SLS-PUB, which is a public logging service that you can manage. You can perform a global switchover by enabling log storage to SLS-PUB.

**Usage notes**

**Important**

This operation is a **one-time global configuration** and **cannot be rolled back**
**after it takes effect**. After you enable log storage to SLS-PUB, **all existing and**
**new instances will be affected**. This is reflected on the details page of each
cloud database instance. On the SQL Audit tab of the Data Security page of a database instance, the Enable Log Storage to SLS-PUB switch is turned on by default. All subsequent logs, including audit logs, slow query logs, and error logs, will be stored in SLS-PUB by default. Exercise caution when you perform this operation. To meet the log visibility requirements of a single instance, perform the following operation: Log in to the Apsara Uni-manager Management Console. Go to the Instance Details page, choose Data Security > SQL Audit, and turn on the Enable Log Storage to SLS-PUB switch. You can enable this feature as needed and manage it for a single instance without affecting other instances. This way, instance management is more secure, flexible, and controllable.

**Prerequisites**

Simple Log Service (SLS) is activated. An SLS project (SLS-PUB) is created in the region where the database instance resides.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **System Management** to go to the **System**
**Settings** page.
3. On the **System parameter configuration** tab, change the value of
DUKANG_OPEN_PUB_SLS to **true**. The global switchover entry is displayed on the page only after the value of this parameter is changed to true.
4. Click **Database instance log storage** at the top of the page to enable log storage to SLS-
PUB for all logs.
5. In the message that appears, confirm the risk prompt message and click **OK**.

**Important**

Global switchover is a one-time, irreversible operation. After you enable log storage to SLS-PUB, you cannot switch back to log storage to SLS-inner. The change will take effect within 3 minutes. After you enable this feature, you can view the updated records by performing the following operation: Log in to the Apsara Uni-manager Management Console. Go to the Instance Details page, choose Data Security > SQL Audit to view the updated records.

**Log query description**

After you change the storage location, you can perform the following log query operations: Query by a time range before the change: Historical logs that are stored in SLS-inner can be queried. Query by a time range after the change: New logs that are stored in SLS-PUB can be queried. Query by a time range that spans the point in time of change: Only the logs that are stored in SLS-PUB can be queried. Historical logs that are stored in SLS-inner before the change are not automatically merged and displayed. You must select a time range before the change for the log query.

### 3.8 Check important components

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Important Component**.

| Note If you cannot find the entry point of important components, you can visit the following link https://[Homepage address of ApsaraDB Operations and Maintenance System]/component/home# . |   |   |
|---|---|---|
|   | https://[Homepage address of ApsaraDB Operations and Maintenance |   |
| System]/component/home# |   |   |

3. On the Important components page, view the features of important components. For more
information, see the following table.

**Important**

Important components involve high-risk operations. We recommend that you should not modify these components.

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

### 3.9 Handle exceptions

This topic describes how to handle database alerts in the ApsaraDB Operations and Maintenance System console and optimize existing monitoring metrics.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, click **Home Page**.
3. In the **Data Summary**, **Backup information**, **High availability HA Information**,
**Resource Information**, or **Task information** sections, click the number next to Number
of exceptions to go to the corresponding task page.
4. Select the exception that you want to handle and click **Handling exceptions** in the
**Operation** column.
If you want to handle multiple exceptions at the same time, you can select all the exceptions that you want to handle and click **Batch processing** in the upper-left corner of the list.
5. In the **Handling exceptions** dialog box, view the details and troubleshoot the error
accordingly. If you want to handle multiple exceptions at a time, you can view the details and troubleshoot the error accordingly in the **Batch handling exceptions** dialog box.
6. Click **Submit**.

### 3.10 Appendix

#### 3.10.1 Log in to the Apsara Uni-manager Operations Console

**Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.
3. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from a deployment engineer or an administrator. If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account. The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @
# $ %
The password is 10 to 20 characters in length.
4. Click **Agree to Private Policy and Log On** .

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

| Operations and Ma e·High-risk opera |   |   |
|---|---|---|
| Data security |   |   |
|   | Change the network isolation mode of an instance to the enhanced whitelist mode | You cannot switch back to the standard whitelist mode. |

on

## 6 Redline V4.3.3 O&M description

**description**

### 6.1 Services provided by Redline Enterprise

**Enterprise**

This topic describes the services provided by Redline Enterprise. Redline Enterprise provides the following services: redline-perf.LogWorker# redline-perf.OpenApi# redline-perf.PerfMaster# redline-perf.PerfWorkerr# redline-perf.DbInit is discontinued. The collection agent of UE is deployed on physical machines in other modes.

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

Path of log data in the Docker container: /home/admin/redline-perf/log `app.log` is the main program log, which contains the log entries that record the extract, transform, load (ETL), storage, data retrieval API operation, and data aggregation to minute granularity. `datax.log` is the synchronization module log, which contains the log entries that record the operations of synchronizing metadata from the metadatabase and pushing real-time tables to CloudMonitor. Paths of log data on the host

| Node | Path |
|---|---|
| PerfMaster node | /cloud/data/redline-perf/PerfMaster#/perf-master/home/admin/redline-perf/log/ |
| PerfWorker node | /cloud/data/redline-perf/PerfWorker#/perf-worker/home/admin/redline-perf/log/ |
| LogWorker node | /cloud/data/redline-perf/LogWorker#/log-worker/home/admin/redline-perf/log/ |

**OpenAPI**

This is an end-to-end gateway service. Paths: Root path: /home/admin/dll-service-aliyun-com Path of log data in the Docker container: /home/admin/dll-service-aliyun-com/logs Path of log data on the host: /cloud/data/redline-perf/OpenApi#/open-api/home/admin/dllservice-aliyun-com/logs

### 6.3 Environment checks

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

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see **Fix**
**connection failures**.
on
2. (Required) Check the communication information between PerfWorker nodes.
i. Run the following command on the jumper server:

```
pssh -h perfworkerhosts -p 1 -P 'docker ps |grep redline | grep PerfWorker|awk '"'" '{ print $1}'"'"' | xargs -I ID docker exec ID curl 'http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=perf''
```

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see **Fix**
**connection failures**.
on
3. (Required) Check the communication information between PerfMaster nodes.
i. Run the following command on the jumper server:

```
pssh -h masterhosts -p 1 -P 'docker ps |grep redline | grep PerfMaster|awk '"'"'{ p rint $1}'"'"' | xargs -I ID docker exec ID curl 'http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=master''
```

ii. Check whether the number of nodes displayed in the ONLINE server nodes section is consistent with the number of deployed nodes. If the number is inconsistent or a message of NOT IN BASELINE is returned, fix this issue. For more information, see **Fix**
**connection failures**.
on
4. (Required) Check whether clusters are active.
i. Run the following command on the jumper server:

```
pssh -h allhosts -p 1 -P 'docker ps |grep redline | grep -v Open|awk '"'"'{ print $ 1}'"'"' | xargs -I ID sh -c "echo ID && docker exec ID tail -n 50 ./log/app.log |gr ep '"'deactived'"'"'
```

on ii. Check whether log entries that include deactived are returned. If yes, go to the corresponding Docker container and activate the clusters in the deactived state. For more information, see **Activate clusters in the deactived state**.

**Check for program exceptions**

(Required) Check application logs for exceptions.
1. Run the following command on the jumper server:

```
pssh -h allhosts -p 1 -P 'docker ps |grep redline | grep -v Open|awk '"'"'{ print $1} '"'"' | xargs -I ID sh -c "echo ID && docker exec ID tail -n 100 ./log/app.log |grep -C 10 '"'Exception'"'"'
```

2. If exception logs are returned, fix this issue. For more information, see Troubleshoot
program exceptions.
3. If this issue cannot be fixed by using the solutions described in **Troubleshoot program**
**exceptions**, contact development personnel or reset node data. For more information, see
**Reset node data**.

### 6.4 O&M operations

#### 6.4.1 Scale in or out a cluster

This topic describes how to scale in or out a cluster.

**Determine whether scale-out is required**

Check the diagnostic information of an instance in the Apsara Uni-manager Management Console. If it takes more than 5 seconds for the data records of the last 3 hours to appear, you may need to add nodes. A larger number of nodes can increase the response speed. You can balance the return on investment (ROI) of hardware based on your needs. Ten nodes can support 3,000 host nodes of ApsaraDB RDS for MySQL instances. A single ApsaraDB RDS for MySQL instance may contain more than one host node.

**Add a node**

1. Add a node and start it.
You can add multiple nodes at a time.
2. Connect to a node that assumes a master role.
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether expected node information is returned.
4. If the expected node information is returned, run the `curl`

```
http://127.0.0.1:8080/admin/makeBaseline?apply=true command.
```

**Remove a node**

1. Remove a node.
on You can remove only a single node at a time.
2. Connect to a node that assumes a master role.
3. Run the curl http://127.0.0.1:8080/admin/makeBaseline?apply=false command to check
whether expected node information is returned.
4. If the expected node information is returned, run the `curl`

```
http://127.0.0.1:8080/admin/makeBaseline?apply=true command.
```

5. Wait 30 minutes for data to be balanced among the remaining nodes and then continue to
remove other nodes based on your needs.

#### 6.4.2 Upgrade or restart a cluster

This topic describes how to upgrade or restart a cluster.

**Procedure**

1. Connect to a PerfMaster node and run the following commands to disable its database. If no
`success` message is returned, repeat the following commands until a `success` message is returned.

```bash
curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=perf" curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=log" curl "http://127.0.0.1:8080/admin/deactivateIgnite?igniteCluster=master"
```

2. Wait 2 minutes and upgrade or restart the cluster after data is stored to disks.
3. After the upgrade or restart is complete, perform environment checks. For more
information, see Environment checks.

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

${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

#### 6.4.4 Activate clusters in the deactived state

on This topic describes how to activate the clusters in the deactived state. Run the following command on a PerfMaster node:

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}"
```

${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

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

If a message of Failed to perform WAL operation is returned, contact technical personnel or reset node data. For more information, see Reset node data. on

#### 6.4.6 Reset node data

This article describes how to reset node data.

**Precautions**

This operation deletes all data of a specific node. Monitoring data stored on the node is deleted and cannot be recovered. Proceed with caution.

**Procedure**

1. Connect to the node or Docker container whose data you want to reset and run the
following command:

```
touch log/HOLD_START && ps aux|grep java|grep -v grep|awk '{ print $2}'|xargs kill -9 && rm -rf ignite/* && sleep 60 && rm -f log/HOLD_START &
```

2. Wait 3 minutes and run the following commands:

```bash
curl "http://127.0.0.1:8080/admin/activateIgnite?igniteCluster=${cluster}" curl "http://127.0.0.1:8080/admin/makeBaseline?igniteCluster=${cluster}&apply=true"
```

${cluster} must be replaced with the cluster to which the node belongs, which can be master, perf, or log.

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
Enable log dump for all instances. on

```
pssh -h logworkerhosts 'curl "http://<The URL of the logworker cluster>:8080/admin/logTransferStore? transType=oss&accessKey=AK&accessSecret=SK&endpoint=http://oss-cn-neimeng-env30-d01 -a.intra.env30.shuguang.com/&bucketName=lztest&region=cn-neimeng-env30-d01"'
```

You can obtain the logworker cluster URL from Apsara Infrastructure Management Framework. Enable log dump for the instances that are included in IP address whitelists.

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

**Use log parsing tools**

Log dump splits historical audit log data into multiple small files. To facilitate your query and analysis, you can use a log parsing tool. By default, each dump log contains data of up to 15 seconds in length or 100 MB in size.

**Configuration command**

```
java -jar perf-tools-0.0.1.jar --input <Log storage directory> --output <Directory of p arsed logs> --begin <Start timestamp> --interval <Scan duration>
```

**Parameters**

| Parameter | Description | Required |
|---|---|---|

on

| --input | The directory in which instance logs are stored. | Yes. |
|---|---|---|
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
