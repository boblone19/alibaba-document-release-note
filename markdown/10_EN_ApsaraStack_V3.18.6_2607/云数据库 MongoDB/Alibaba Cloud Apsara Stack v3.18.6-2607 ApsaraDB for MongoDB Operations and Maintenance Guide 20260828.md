---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for MongoDB Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 315
source_pdf: "59dd34463f7a1a0b_Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for MongoDB Operations and Maintenance Guide 202608"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20MongoDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20MongoDB%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for MongoDB Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Service architecture
  - 1.1 System architecture
    - 1.1.1 Backup system
    - 1.1.2 Data migration system
    - 1.1.3 Control system
    - 1.1.4 Monitoring system
    - 1.1.5 Task scheduling system
- 2 文档标题缺失，请补全后重新导出
  - 2.1 Console release notes
  - 2.2 Log in to ApsaraDB Operations and Maintenance System Smart Edition
  - 2.3 Overview of the ApsaraDB O&M System Smart Pro Edition homepage
  - 2.4 Instance management
    - 2.4.1 Instance list
      - 2.4.1.1 Overview of the instance details page
      - 2.4.1.2 View instance information
      - 2.4.1.3 Instance O&M operations
        - 2.4.1.3.1 Important Notes
        - 2.4.1.3.2 Scheduled migration management
        - 2.4.1.3.3 Batch operation management
        - 2.4.1.3.4 Instance dashboard
        - 2.4.1.3.5 Recreate a secondary database
        - 2.4.1.3.6 Migrate an instance
        - 2.4.1.3.7 Upgrade the minor version
        - 2.4.1.3.8 Change the specification of a database instance
        - 2.4.1.3.9 Lock an instance
        - 2.4.1.3.10 Perform an HA switchover
        - 2.4.1.3.11 Modify the storage capacity
      - 2.4.1.4 Monitoring and alerting
      - 2.4.1.5 Diagnose an instance
      - 2.4.1.6 View status inspection records
      - 2.4.1.7 Manage audit logs
      - 2.4.1.8 Change records
      - 2.4.1.9 Manage tasks
      - 2.4.1.10 Backup management
      - 2.4.1.11 Data restoration
      - 2.4.1.12 Security configuration
      - 2.4.1.13 Parameter configurations
      - 2.4.1.14 O&M configurations
      - 2.4.1.15 Tag configurations
      - 2.4.1.16 Manage databases
      - 2.4.1.17 Account management
    - 2.4.2 Cluster instance list
      - 2.4.2.1 Cluster instance list overview
      - 2.4.2.2 Basic information of cluster instances
      - 2.4.2.3 Task list
      - 2.4.2.4 Instance change records
      - 2.4.2.5 Kernel instance parameters
  - 2.5 Host management
    - 2.5.1 Host management overview
    - 2.5.2 System host
    - 2.5.3 Host details
    - 2.5.4 Manage host software packages
    - 2.5.5 Physical machine group
  - 2.6 Cluster management
    - 2.6.1 Cluster management overview
    - 2.6.2 System clusters
    - 2.6.3 Service type management
    - 2.6.4 Service node management
    - 2.6.5 Location
  - 2.7 Task management
    - 2.7.1 Task management overview
    - 2.7.2 Pengine tasks
      - 2.7.2.1 Pengine task overview
      - 2.7.2.2 Instance task list
      - 2.7.2.3 PengineClass Meta tool
      - 2.7.2.4 PengineStep Meta tool
      - 2.7.2.5 Task statistics
    - 2.7.3 Grand Canal task
    - 2.7.4 Migration task
  - 2.8 Log management
  - 2.9 Disaster recovery management
    - 2.9.1 Disaster recovery switchover
    - 2.9.2 Disaster recovery tasks
  - 2.10 HA management
    - 2.10.1 HA management overview
    - 2.10.2 Robot management
      - 2.10.2.1 Robot processing logs
      - 2.10.2.2 Robot switch control
      - 2.10.2.3 Robot repair statistics
      - 2.10.2.4 Robot processing blacklist
      - 2.10.2.5 Robot task management
  - 2.11 System management
    - 2.11.1 System management overview
    - 2.11.2 System settings
    - 2.11.3 Tag list
    - 2.11.4 Custom template
    - 2.11.5 Whitelist management
    - 2.11.6 Host blocking during migration
    - 2.11.7 General instance O&M management
    - 2.11.8 Scheduled task management
  - 2.12 Intelligent O&M
    - 2.12.1 Intelligent host diagnostics
    - 2.12.2 One-click information collection
    - 2.12.3 Automated script management
  - 2.13 Database agent O&M
    - 2.13.1 Overview of database agent O&M
    - 2.13.2 Agent overview
    - 2.13.3 Agent management
    - 2.13.4 Observable diagnosis
    - 2.13.5 Knowledge base management
  - 2.14 Package management
  - 2.15 Exception management
    - 2.15.1 Exception management overview
    - 2.15.2 Exception dashboard
    - 2.15.3 Exception list
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
      - 3.3.4.8 Disable backup for PolarDB-X instance
      - 3.3.4.9 Add proxy nodes to a Tair (Redis OSS-compatible) instance
      - 3.3.4.10 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance
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
- 4 Platform Operation in the Apsara Uni-manager Operations Console
  - 4.1 Turn on the IPv6 display switch for ApsaraDB for MongoDB
- 5 Security maintenance
  - 5.1 Network security maintenance
  - 5.2 Account password maintenance

## 1 Service architecture

### 1.1 System architecture

#### 1.1.1 Backup system

**Automatic backup**

ApsaraDB for MongoDB supports both physical backup and logical backup. You can flexibly configure the backup start time based on the service off-peak hours. All backup files are retained for seven days.

**Temporary backup**

You can initiate a temporary backup as required. The backup files are retained for seven days.

**Log management**

ApsaraDB for MongoDB generates operation logs and allows you to download them. You can use the operation logs for local incremental backup.

**Data backtracking**

ApsaraDB for MongoDB can use backup files and logs to generate a temporary instance for any time point within the past seven days. After verifying that the data in the temporary instance is correct, you can use the temporary instance to restore data to the specified time point. Creating a temporary instance does not affect the running of the current instance. Only one temporary instance can be created for each ApsaraDB for MongoDB instance at a time. A temporary instance is valid for 48 hours. You can create a maximum of 10 temporary instances for an ApsaraDB for MongoDB instance each day.

#### 1.1.2 Data migration system

**Database replication between instances**

ApsaraDB for MongoDB allows you to easily migrate databases from one instance to another.

**Data migration to or from ApsaraDB for MongoDB**

ApsaraDB for MongoDB provides a professional tool and a migration wizard to help you migrate data to or from ApsaraDB for MongoDB.

**Backup file download**

ApsaraDB for MongoDB retains backup files for seven days. During this period, you can log on to the ApsaraDB for MongoDB console to download the backup files.

#### 1.1.3 Control system

If a host or an instance crashes, the ApsaraDB for MongoDB high-availability (HA) component fails services over within 30 seconds after the exception is detected. This guarantees that applications run properly and ApsaraDB for MongoDB is highly available.

#### 1.1.4 Monitoring system

**Performance monitoring**

ApsaraDB for MongoDB provides nearly 20 metrics for system performance monitoring, such as disk capacity, IOPS, connections, CPU utilization, network traffic, TPS, QPS, and cache hit rate. You can obtain the running status information of instances over the past year.

**SQL auditing**

The system records the SQL statements and related information sent to ApsaraDB for MongoDB instances, such as the connection IP address, database name, access account, execution time, and the number of records returned. You can use SQL auditing to locate problems and check instance security.

**Threshold alarms**

ApsaraDB for MongoDB provides alarm SMS notifications in the event of exceptions in instance status or performance. These exceptions can include instance locking, insufficient disk capacity, abnormal IOPS, abnormal number of connections, and over high CPU utilization. You can configure alarm thresholds and up to 50 alarm contacts (of which only five are effective at a time). When a threshold is exceeded in an instance, an SMS notification is sent to the alarm contacts.

**Web operation logs**

The system logs all modification operations in the ApsaraDB for MongoDB console for administrators to check. These logs are retained for a maximum of 30 days.

#### 1.1.5 Task scheduling system

You can use the ApsaraDB for MongoDB console or APIs to create or delete instances or switch instances between the intranet and Internet. All instance operations are scheduled, traced, and displayed as tasks.

## 2 文档标题缺失，请补全后重新导出

### 2.1 Console release notes

This topic outlines the new features and key updates for Dukang Intelligent Edition, a unified operations platform for cloud databases.

**v3.18.6sp-2607**

| Feature overview | Description | Related documentation |
|---|---|---|
| Instance list | A unified operations entry point is now available on the instance list and instance details pages for PolarDB for PostgreSQL Primary/Standby Edition instances. You can filter instances by criteria such as engine type and instance status. You can view basic information, SLB information, performance overview, and specification information for an instance. This feature supports O&M operations, including scheduled migration management, batch operation management, instance dashboard, rebuilding a standby instance, instance migration, minor version upgrades, specification changes, instance locking, HA switchover, and storage space changes. This feature also integrates capabilities such as monitoring and alarms, 360° diagnosis, specialized diagnostics, audit logs, task management, backup management, and data recovery. | Instance list |
| Cluster instance list | A new Cluster Instance List page is available. You can filter cluster instances by cluster name, service type, and service version, and export the list data. You can view basic information, specification information, network information, region information, sub-instance information, whitelist information, and user information for cluster instances. This page provides features such as Task List, Instance Change History, and Redis kernel instance parameter management, and dynamically displays operations based on the instance type, such as specification change, primary/standby switchover, restart instance, lock/unlock instance, version upgrade, instance migration, modify whitelist, delete instance, and clear data. | Cluster instance list |

| Host management | A new Host Management module is available. Centrally view the list of system hosts managed by the platform and filter them by various dimensions, including IP address, hostname, machine status, machine type, database type, cluster, and data center. Perform operations such as refreshing the resource cache, batch configuring instance allocation, tagging hosts, and deleting hosts. View host details, host instance information, host performance information, host change history, and host software package management, and perform operations such as connectivity checks, switching clusters, enabling or disabling instance allocation, marking a host as down, and taking an HAProxy host offline. Create, edit, and delete physical machine groups to achieve hardware resource pool isolation and fine-grained scheduling. | Host management |
|---|---|---|
| Cluster management | A new Cluster Management module is available. Create, edit, and delete system clusters, manage their tags, and view cluster details. View the cluster host list and resource charts for the CPU/memory allocation rate and usage rate, and use features such as batch-configuring autoscaling, refreshing the synchronization mode, refreshing the resource cache, refreshing off-site backups, configuring service nodes, and viewing whitelists. Manage service types, service nodes, and the location information tree. Create, edit, and delete service nodes, and run the Dukang health check, cluster consistency check, and subdomain consistency check. | Cluster management |
| Task management | A new Task Management module is available. Centrally view and manage Pengine tasks, Grand Canal tasks, and migration tasks. Filter the instance task list across multiple dimensions, and view task details, view subtasks, check intervention history, modify remarks, and perform batch retries. Use the PengineClass Meta tool and PengineStep Meta tool to maintain task types and step metadata. The Task Statistics page uses charts to display the total number of tasks executed, failure rate trends, and the most frequently executed and failed task types, to help you monitor the health of platform tasks. | Task management |

| Log management | A new Log Management module is now available to centrally record operations, API calls, parameter changes, high- availability switchovers, and O&M audit information on the platform. You can query operation logs, kernel instance parameter change history, RDS API call logs, API call logs, HA switchover logs, general O&M audit logs, and custom template execution records. You can filter logs by criteria such as operator, operation object, API name, access IP, and time range to facilitate operation tracing, troubleshooting, and auditing. | Log management |
|---|---|---|
| Disaster recovery management | A new Disaster Recovery Management module is available. You can view disaster recovery instance information by data center. This view shows the number of switchable and degradable instances, along with assessment results for DNS, ALB, Proxy, and instance validation. You can create a disaster recovery switchover task and choose between a normal switchover or a forced switchover. You can create a disaster recovery downgrade task to downgrade eligible instances from a multi-availability zone to a single availability zone. You can create a real-time refresh task to increase the frequency of instance information collection. The Disaster Recovery Task List allows you to view task parameters, execution details, data statistics, and task logs. | Disaster recovery management |
| High availability management | A new High Availability Management module is now available, which provides a Robot-based automated mechanism for resolving exceptions, reducing the need for manual intervention with database high-availability issues. You can view Robot processing logs and the details of each processing step. The Robot switch control allows you to enable or disable automated processing for specific task types. Robot repair statistics help you analyze processing data, such as success, failure, rejection, and auto-recovery counts, as well as the overall repair rate. Robot processing blacklist management allows you to block automated processing for specified instances or hosts within a specific time frame. Robot task management allows you to view task sources, processing results, and O&M times. | High availability management |

| System management | The new System Management module is the platform's global configuration center. You can configure database parameter templates, system parameters, component exception levels, and exception types. The Tag List Management page allows you to maintain tag definitions for customer instances, hosts, and clusters. Custom Template Management includes SQL templates, blacklist rules, and execution rules. Whitelist Management allows you to view and refresh Classic/VPC whitelists by region, database type, and machine type. It supports migration host shielding, general instance O&M management, and scheduled task management for platform-level parameter configuration, secure access control, and O&M scheduling. | System management |
|---|---|---|
| Database agent O&M | A new Database Agent O&M module is available. Perform centralized O&M for database intelligent agents. The Agent Overview displays the total number of agents, today's call volume, average success rate, token consumption, status distribution, and a 7-day trend of call volume. It provides agent management and instance detail views, allowing you to check instance resource metrics, event logs, and runtime status. Manage configurations, including prompt version management, model configuration, tool execution confirmation configuration, and custom parameter configuration. Provides observability and diagnostics, including a metrics overview, session history, and tracing. Manage the knowledge base, including knowledge base version updates, historical version viewing, and version switching. | Database agent O&M |

| Exception management | A new Exception Management module is available. Accessed from Quick Navigation, this module lets you centrally monitor and handle platform operational exceptions. The Exception Dashboard displays the number of critical, warning, and ignorable exceptions, as well as exception trends, distribution across target types, and a ranking of components with the most exceptions. The Exception List allows you to filter exceptions by severity level, exception type, component type, and postponed processing status. You can handle exceptions individually or in batches, either immediately or by postponing them. The system records the cause and solution for each exception. The Health Check Task Management page allows you to view task scheduling status, block counts, and alert thresholds. You can also modify the cron expression and enable or disable health check tasks. | Exception management |
|---|---|---|
| Automated script import | You can now import external scripts from the Tongque Platform and manage their full lifecycle. This enables unified scheduling, execution, and security auditing for both built-in and external scripts, increasing operational flexibility. | Automated script management |
| Import custom DAG diagnosis template | You can now download and import DAG-based diagnostic packages from the Tongque Platform. In one-click information collection, you can select "Extended Scenarios" to load a custom template. The system then automatically executes a multi-step diagnosis based on the predefined logic and displays detailed results, to support customized troubleshooting of complex faults. | One-click information collection |

### 2.2 Log in to ApsaraDB Operations and Maintenance System Smart Edition

**and Maintenance System Smart**

**Edition**

This topic describes how to log in to ApsaraDB Operations and Maintenance System Smart Edition.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.

**Procedure**

1. Open a web browser.
2. In the address bar, enter the URL of the Apsara Uni-manager Operations Console and press
Enter.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter the correct username and password.

> **Note:** Obtain the username and password that are used to log in to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.
> If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account.
> The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted.
> To enhance security, make sure that your password meets the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, click **Products** and choose **Databases** > **ApsaraDB System**
**O&M Smart Pro Edition**.

### 2.3 Overview of the ApsaraDB O&M System Smart Pro Edition homepage

**O&M System Smart Pro Edition**

**homepage**

The ApsaraDB O&M System Smart Pro Edition homepage is the core entry point of ApsaraDB O&M System Smart Pro Edition. It provides global data display, rapid exception identification, and intelligent navigation to help O&M personnel monitor the operational status of the system and perform daily O&M tasks.

**Homepage layout**

The homepage consists of the following modules from top to bottom:

| Module | Description |
|---|---|
| System status overview | Displays the health score and a summary of core resource metrics. |
| Quick navigation | Provides access to frequently used knowledge bases and common features. |
| Overview of abnormal data | Provides multi-dimensional exception statistics and quick navigation links. |
| High availability HA information | Displays HA monitoring trends and the health status of platform components. |
| Instance management | Displays instance status statistics by database engine and chip architecture. |
| Cluster management | Displays cluster resource rankings and host monitoring status. |
| Task management | Displays task running status statistics and a list of interrupted tasks. |
| Ops review | Displays issue rankings on the blocklist and allowlist along with health scores. |

**System status overview**

This module is located at the top of the homepage and provides a centralized view of the overall system health status.
**Health status**: Displays the overall score (for example, 91.1) and a Healthy label. The
system calculates the score based on the number of exceptions and the maximum interval duration.
**Core metrics**: Displays the total number of database engines, clusters, instances, and
hosts to help you quickly understand the resource scale.

> The statistical data on this page comes from the cache and refreshes every 10 minutes.

**Quick navigation**

This module provides common entry points:

| Category | Entry | Description |
|---|---|---|
| Common knowledge bases | ApsaraDB O&M Guide | Navigates to the online help documentation. |
|   | Typical troubleshooting | Navigates to the troubleshooting reference. |
| Common features | Exception management | Navigates to the exception management page. The exception management feature is not displayed in the left navigation bar, so you can access it only through the quick navigation on the homepage. |

**Overview of abnormal data**

This module uses a donut chart and numeric values to display multi-dimensional exception statistics, helping you quickly identify system risks.
**Eight exception dimensions**:

| Exception dimension | Description | Solution |
|---|---|---|
| Instance exceptions | The number of instances with abnormal running status. | Click to go to the instance list for troubleshooting. |
| Resource configuration exception | Resource quota or configuration exceptions. | Click to go to Resource Management. |
| Host exception | The number of hosts with downtime. | Click to go to Host Management. |
| System operation exception | Errors, warnings, or tips from the platform. | Click to view details. |

| Cluster exception | Insufficient cluster resources or configuration exceptions. | Click to go to Cluster Management. |
|---|---|---|
| Instance backup exception | The number of failed backup tasks. | Click to go to Backup Management. |
| Instance HA status exception | The number of instances with HA disabled or abnormal HA status. | Click to go to HA Management. |
| Interrupted tasks | The number of interrupted tasks. | Click to go to Task Management. |

Visual presentation: The donut chart displays specific numeric values and uses colors to indicate severity levels (yellow for warning and red for major issues). Click a section of the exception overview to go directly to the corresponding details page.

**High availability information**

This module displays the following core monitoring metrics for database high availability:
**HA-enabled instances**: The total number of instances with HA enabled.
**HA status exceptions**: The number of instances with abnormal HA status.
**HA switching times**: The number of HA switchovers in the last hour.
**Switchover trend chart**: You can view the trend by time range, such as the last 1 hour, 4
hours, or 12 hours. The trend chart helps you identify abnormal switchover frequencies, such as a sudden spike in switchovers within a short period, and assess business continuity.

**Core control component status**

This module displays the running status of the core components of the O&M platform:

| Component | Description |
|---|---|
| RDSAPI | The RDS API service. |
| Perf | The performance collection service. |
| Bak | The backup service. |
| Dukang | The control service of ApsaraDB Operations and Maintenance System. |
| DBass | The database control service. |

Status indicators: green for Normal and red for Exception.

**Instance management**

This module shows the distribution of instance status by database engine and chip architecture:
**By engine type**: Statistics on the number of instances for each engine, such as MySQL,
PolarDB PostgreSQL (primary/secondary edition), Redis, and MongoDB.
**By chip type**: Statistics on the distribution of instances across chip architectures such as
Hygon and Phytium. Click **View more** to go to the Instance List page.

**Cluster management**

This module displays cluster resource usage and host monitoring status:
**Top 5 resource sales rate**: A ranking of clusters by resource usage to help identify
heavily loaded clusters.
**Host monitoring status**: Statistics on the number of normal and abnormal hosts.
**Host chip statistics**: Statistics on the number of hosts by chip architecture.

**Task management**

This module displays the running status of tasks on the current platform:
**Task status statistics**: The number of running, waiting, and interrupted tasks.
**Task interrupt details**: Information including the job ID, task name, source, instance
name, and execution time. Click **View more** to go to the Task Management page and manage interrupted tasks.

**Ops review**

This module displays current system issues and risks in ranking lists:
**Black List TOP8**: A ranking of database performance issues, such as replication latency
and consistency problems.
**Honor roll TOP8**: A ranking of configuration and security risks, such as unavailable
hostnames.
**Radar chart**: A visual representation of issue severity.

> **Important:** A higher number of exceptions and a longer maximum interval result in a lower score and a lower rank.
> When scores are equal, a higher value of (number of exceptions × 6 + maximum interval × 4) results in a lower rank.
> The Honor roll TOP8 section selects the highest-ranked items from those with exception data.

**Example: Identify slow database response**

1. Check the **System Status Overview** module on the homepage to confirm whether the
health score has decreased.
2. Check the **Overview of abnormal data** module for new instance exceptions.
3. Identify specific performance issues in the Black List TOP8 section of the **Ops Review**
module.
4. Click the exception module to go to the instance details page for troubleshooting and
resolution.

### 2.4 Instance management

#### 2.4.1 Instance list

##### 2.4.1.1 Overview of the instance details page

The instance details page of the ApsaraDB O&M System Smart Pro Edition is a key feature module. This page displays and allows you to manage the status, configurations, performance metrics, and O&M operations of a database instance.

**Supported database engines**

ApsaraDB RDS for MySQL PolarDB for MySQL Primary/Secondary Edition PolarDB for PostgreSQL Primary/Secondary Edition

> **Note:** For O&M operations on other instance types, refer to the Instance management section in the ApsaraDB Operations and Maintenance System - Operations and Mai ntenance Guide.
> The menus and features on the instance details page vary depending on the instance engine. This topic describes the page structure and these engine-specific differences.

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

| Item | Description |
|---|---|
| Visibility of the Physical Topology tab | The system displays the Physical Topology tab only for MySQL and PostgreSQL instances that do not use the new architecture. |
| Database information | For the PolarDB for PostgreSQL Primary/Secondary Edition, the database information menu is not displayed, and management of the database list on the details page is not supported. |
| Specialized diagnosis | The PolarDB for PostgreSQL Primary/Secondary Edition supports only two diagnostic tabs. |

**Safety precautions**

> **Warning:** Executing SQL statements is risky. Exercise caution when you perform this operation.
> A confirmation message appears before you perform a Kill session operation for multiple diagnostic items on the special diagnosis page. If you terminate the session for multiple diagnostic items at a time, your business may be affected.
> Deleted databases and accounts cannot be restored. A confirmation message appears before the deletion operation continues.
> If you modify kernel parameters, you must restart the instance for some kernel parameters to take effect. We recommend that you perform this operation during off-peak hours.

**Getting started**

**Step 1: Go to the instance details page**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.

> **Note:** The Instance List page displays all database instances in the current environment and supports filtering by engine type, instance status, and tag. The top of the page also provides the following shortcuts:
> Scheduled migration management: Manage planned migration tasks for instances.
> Batch operation management: Perform batch O&M operations on multiple instances.
> Instance dashboard: Monitor the global status of instances on a dashboard.

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

**Why is the Physical Topology tab not displayed?**

The Physical Topology tab appears only for MySQL (ApsaraDB RDS for MySQL and PolarDB for MySQL Primary/Secondary Edition) and PostgreSQL (PolarDB for PostgreSQL Primary/Secondary Edition) instances that do not use the new architecture. Otherwise, the tab is not displayed.

**Q: Why is the Instance View menu not displayed?**

The Instance View menu is displayed only when the current instance is the primary instance. If the current instance is a read-only or secondary instance, this menu is not displayed.

**Q: What do I do if the notinwhiteList message appears when I**

**execute an SQL statement?**

Add the current IP address to the IP address whitelist of your instance. Go to the instance details page. In the left-side navigation pane, click **Security Configuration**. On the Security Configuration page, click the **ip whitelist** tab. On the page that appears, add the current IP address to the IP address whitelist and execute the SQL statement again.

**Q: Why are multi-line SQL statements not supported?**

Only single-line SQL statements are supported, and SQL statements cannot contain line breaks. Merge multi-line SQL statements into a single-line SQL statement before you execute it.

**Q: What do I do if an SQL statement fails to be executed on a**

**PolarDB child instance?**

You must switch a PolarDB child instance to the primary instance to execute SQL statements. In the Master Library/Standby Library section on the Execute SQL tab, select Master Library and click Execute to execute the SQL statement again.

**Q: Will my business be affected if I perform a Kill session**

**operation?**

If you perform a Kill session operation, the selected session process is terminated. This may affect your ongoing business operations. We recommend that you perform this operation after you confirm that the session does not affect your core business. A confirmation message appears before the operation continues. Exercise caution when you perform this operation.

**Q: What do I do if the status data disappears after I switch**

**from the Real-time status of Innodb instances tab to another**

**tab?**

The status data collection automatically stops when you switch to another tab. After you return to the Real-time status of Innodb instances tab, you must manually click **START** to restart status data collection.

**Q: What can I do if audit logs fail to be archived?**

To resolve this issue, check the following items: Verify that the OSS storage configuration is correct. Verify that the data volume of logs under the filter conditions does not exceed the limit. On the SQL Archiving History tab, view the cause of the failure, handle the failure as prompted, and then archive the audit logs again.

**Q: What do I do if the account password fails to be changed?**

Verify that the account password meets the following complexity requirements: The password must be 8 to 32 characters in length and contain at least three of the following types: uppercase letters, lowercase letters, digits, and special characters. If the failure persists, contact the administrator to check whether the account status is normal.

**Q: How to view the consistency check results of the primary**

**and secondary instances?**

Go to the instance details page. In the left-side navigation pane, click **Change record**. On the page that appears, click the **Primary and secondary inconsistency check** tab to view the check results. For a task in the Not Started, Failed, Interrupted, or Checking state, you can go to the **Parameter configuration** page to check the configurations.

**Q: What is the purpose of specifying the expiration time for a**

**tag?**

You can specify the expiration time for some tags. When the specified expiration time is reached, the tag value may become invalid or a specific behavior may be triggered. When you edit a tag, you can use the date picker to specify the expiration time for the tag. The specified expiration time can be accurate to hour, minute, and second. You can also leave the Expiration Time parameter blank. In this case, No is displayed for the Expiration Time parameter.

##### 2.4.1.2 View instance information

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

> **Note:** The physical topology is provided only for instances that meet the following requirements:
> The database engine of the instance is MySQL.
> The instance does not use a new architecture.

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

##### 2.4.1.3 Instance O&M operations

###### 2.4.1.3.1 Important Notes

**Read before operation**

> **Warning:** Some operations described in this section, such as instance restart, minor engine version update, and backup and restoration, involve core changes to the underlying infrastructure. These operations are irreversible or high-risk. Improper operations may lead to data loss, service interruption, or performance jitter.
> Before you perform any O&M operations, carefully read the relevant tutorials and the precautions and key risk reminders on the console interface. If necessary, perform operations under the guidance of Alibaba Cloud professional technicians. Once you click Submit, Confirm or similar commands, it is deemed that you have been fully aware of all potential risks and voluntarily bear all the consequences arising therefrom. Proceed with caution.

###### 2.4.1.3.2 Scheduled migration management

This topic describes how to manage scheduled migration tasks for instances in ApsaraDB O&M System Smart Pro Edition. You can use this feature to create a migration plan, migrate multiple instances at a time to a specified destination region or zone, and configure the migration solution and virtual IP (VIP) switching mode for each instance.

**Feature overview**

The scheduled migration management page provides the following core features: Create a migration plan: Select candidate instances, configure parameters such as the destination location, migration window, and VIP switching mode for each instance, and apply default configurations to all instances at a time. View migration plans: View the plan list, which includes the plan name, status, total number of instances, number of successful, failed, and canceled instances, and completion percentage. Modify a plan name: Modify the plan name when the plan is pending. Cancel a plan: Cancel a migration plan that is running or pending. Retry failed instances: Retry the failed instances in a plan. Delete a plan: Delete migration plans that you no longer need. View plan details: Click a plan name to view the details of the migration plan.

**Migration plan statuses**

A migration plan has the following statuses:

| Status value | Status name | Description |
|---|---|---|
| 0 | Running | The migration task is running. |
| 1 | Wait | The plan is created and is waiting for execution. |
| 2 | Success | All instances are migrated successfully. |
| 3 | Failed | The migration failed. |
| 4 | Partial success | Some instances are migrated successfully, while others failed. |
| 6 | Canceled | The plan is canceled. |

**Create a migration plan**

1. Log in to ApsaraDB Operations and Maintenance System Smart Edition. In the left-side
navigation pane, choose **Instance Management** > **Instance list**.
2. On the instance list page, click **Scheduled migration management** at the top of the
page.
3. Click **Create a migration plan**. In the panel that appears, specify the following
information:

| Configuration item | Description |
|---|---|
| Plan Name | The name of the migration plan. |

4. In the candidate instance table, select the instances that you want to migrate. You can
search for instances by name and filter them by database engine and role.

> **Note:** The system automatically verifies the migration eligibility of the selected instances. The system marks instances that fail the verification as "Not migratable" and displays the reason.

5. After you add candidate instances to the list of selected instances, configure migration
parameters for each instance. You can use the **Default configuration** feature in the upper-right corner of the page to set multiple common parameters at a time:

| Parameter | Description | Required |
|---|---|---|
| Target region | The destination region for the migration. | Yes |
| Target Zone | The destination zone for the migration. | Yes |
| Target subdomain | The destination subdomain for the migration. | Yes |
| vSwitchId | The vSwitch ID. This parameter is required when you migrate a VPC instance across zones. | Optional |
| CPU architecture | The destination CPU architecture type. This parameter is optional. | No |
| Release migration task window | The execution time window for the migration task. If you do not select a window, the system dispatches the task within the O&M window by default. | No |
| VIP Switch Mode | The execution timing for VIP switching during the migration. Valid values: Immediately: The system performs VIP switching immediately during the migration. O & M window: The system performs VIP switching within the O&M window. Specified time: The system performs VIP switching at a specified time. You must set a specific time. | Yes |
| VIP Switch Time | The time for VIP switching. This parameter is required when you set VIP Switch Mode to Specified time. | Optional |
| The primary and secondary minor versions are consistent. | Specifies whether the primary and secondary instances must run the same minor version. This parameter is available only for MySQL instances. | No |

6. After you confirm that the configuration is correct, click **Save**.

> **Note:** When you create a migration plan, the system automatically retrieves the migration information of each instance, such as the current zone, whether the instance is a VPC instance, and the CPU architecture list. The system uses this information to assist with configuration and verification.

**Modify the plan name**

> **Note:** You can modify the plan name only when the plan is in the Wait status.

1. In the migration plan list, find the plan that you want to manage.
2. In the Operation column, click **Modify**.
3. Enter a new plan name in the dialog box.
4. Click **OK**.

**Cancel a plan**

> **Note:** You cannot cancel a plan in the Success or Canceled status. After you cancel a plan, the system cancels all instances that are in the Wait or Running status in the plan.

1. In the migration plan list, find the plan that you want to manage.
2. In the Operation column, click **Cancel**.
3. In the confirmation dialog box, click **OK**.

**Retry a failed instance**

> **Note:** You can perform a retry only when the plan is in the Failed or Partial success status.

1. In the migration plan list, find the plan that you want to manage.
2. In the Operation column, click **Retry**.
3. In the confirmation dialog box, click **OK**.

> **Note:** The retry operation applies only to the failed instances in the plan. Instances that are already successful or canceled will not be affected.

**Delete a plan**

1. In the migration plan list, find the plan that you want to manage.
2. In the Operation, click **Delete**.
3. In the confirmation dialog box, click **OK**.

> **Important:** You cannot recover a deleted plan. Proceed with caution.

**View plan details**

1. In the migration plan list, click the name of the plan that you want to manage.
2. The plan details panel appears, which displays the migration details of all instances in the
plan.

**Verify the results**

After you create a migration plan, you can verify the results by using the following methods:
1. Return to the migration plan list and confirm that the new plan appears in the list with the
status Wait or Running.
2. Click the plan name to view details and confirm that the migration status of each instance
is correct.
3. After the migration completes, check whether the plan status changes to Failed or Partial
success.

###### 2.4.1.3.3 Batch operation management

This topic describes how to use the batch operation management feature in the ApsaraDB O&M System Smart Pro Edition to perform batch O&M operations on multiple instances.

**Feature overview**

On the top of the instance list page, click **Batch operation management** to go to the batch operation management page. The left side of the page provides the following three submodules. Click a submodule to go to the corresponding page:

| Submodule | Description |
|---|---|
| Batch parameter refresh | Refresh kernel parameters in batches for multiple instances of the same type and version. This submodule applies to scenarios such as emergency upgrades by the kernel team. |
| Batch task management | Create and manage general batch tasks and performs operations on multiple instances based on predefined task types. |
| Batch task type management | Manage the type definitions of batch tasks, including basic information, parameter rules, and verification rules. |

**Batch parameter refresh**

In the Batch parameter refresh section, you can refresh kernel parameters in batches for multiple instances of the same type and version.

> **Warning:** Instance parameter changes may cause risks such as transient connection interruptions and instance unavailability. This feature is available only to the kernel team for emergency upgrades. Before execution, send the relevant notifications and perform a canary release.
> Make sure that all the instance names you enter are for database instances of the same type and version.
> Only parameters that do not require a restart are supported.
> To modify kernel parameters for Redis DB nodes, go to the logical instance page and make the changes there.

**View the parameter refresh task list**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance List**. On the page that appears, click
**Batch operation management** at the top of the page.
2. On the page that appears, click **Batch parameter refresh**.
3. View the parameter refresh task list. The list contains the following fields:

| Field | Description |
|---|---|
| Task ID | The unique ID of the parameter refresh task. Click the ID to view the task details. |
| Database type | The database engine of the target instances for the task. |
| Database version | The database version of the target instances for the task. |
| Status | The execution status of the task. |
| Total | The total number of instances in the task. |
| Success | The number of instances for which the parameter refresh succeeded. |
| Failed | The number of instances for which the parameter refresh failed. |
| Canceled | The number of canceled instances. |
| Completion percentage | The completion progress of the task. |

| Founder | The creator of the task. |
|---|---|
| Creation time | The time when the task was created. |

4. (Optional) Search for tasks by **Status** or by **Advanced Filter**.

**Create a parameter refresh task**

1. On the Batch parameter refresh page, click **Create a parameter refresh task** .
2. In the **Select Instances** step, select the target instances from the candidate instance list,
click **Add Selected**, and then click **Next Step**.

> **Note:** The candidate instance list supports searching by **Instance name/ID** or by **Advanced** **Filter** to quickly locate instances.

3. In the **Configure parameters** step, select the parameters to refresh and enter the new
value.. The parameter list is retrieved based on the selected instances and includes fields such as parameter name, current value, default value, value range, unit, and description.
4. Click **Submit** to create the task.

**Manage parameter refresh tasks**

In the Operation column of the task list, you can perform the following operations:

| Operation | Status | Description |
|---|---|---|
| Cancel | Running and Wait | Cancel tasks that are running or waiting. |
| Retry | Failed | Retry the parameter refresh for failed instances. |
| Delete | All | Delete the task record. |

**Batch task management**

In the Batch task management section, you can create and manage general batch tasks. You can perform operations on multiple instances based on predefined task types.

**View the batch task list**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. On the page that appears, click
**Batch operation management** at the top of the page.
2. On the page that appears, click **Batch task management**.
3. View the batch task list. The list contains the following fields:

| Field | Description |
|---|---|
| Task ID | The unique ID of the task. Click the ID to view the task details. |
| Task type | The classification name of the task. This value comes from the types defined in batch task type management. |
| Execution time | The execution time mode of the task, including Immediately, O & M Window, and Specified time. |
| Specified time | When the execution time mode is set to Specified time, this field displays the specific execution time range. |
| Status | The execution status of the task. |
| Total | The total number of instances in the task. |
| Success | The number of instances for which the task execution succeeded. |
| Failed | The number of instances for which the task execution failed. |
| Progress | The completion percentage of the task. |
| Remarks | The remarks for the task. |
| Founder | The creator of the task. |
| Creation time | The time when the task was created. |

4. (Optional) Search for tasks by **Status** or by **Advanced Filter**.

**Create a batch task**

1. On the Batch task management page, click **Create batch tasks**.
2. In the dialog box that appears, select a **Task type** (required).
3. Select an **Execution time** mode (required):

| Mode | Description |
|---|---|
| Immediately | The system executes the task immediately. |

| O & M time | The system executes the task within the O&M time window. |
|---|---|
| Specified time | The system executes the task within the specified time range. |

4. (Optional) Enter remarks in the **Remarks** field.
5. In the **Candidate instances** list, select the instances that you want to manage and click
**Add selected** to add them to the selected list on the right.

> **Note:** The Candidate instances list supports searching by **Instance name/ID** and **Advanced** **filter** to quickly locate instances. You can clear the selected list.

6. After you confirm the configuration, click **Submit** to create the task.

**Manage batch tasks**

In the Operation column of the task list, you can perform the following operations:

| Action | Applicable status | Description |
|---|---|---|
| Cancel | Running and Wait | Cancel a running or waiting task. |
| Retry | Failed and Partial success | Rerun the task on failed instances. |
| Delete | All | Delete the task record. |

**Batch task type management**

In the Batch task type management section, you can create and manage type templates for batch tasks, including basic information, parameter rules, and verification rules of tasks.

**View the task type list**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. On the page that appears, click
**Batch operation management** at the top of the page.
2. On the page that appears, click **Batch task type management** .
3. View the task type list. The list contains the following fields:

| Field | Description |
|---|---|
| Type name | The display name of the task type. |
| Type encoding | The unique encoding of the task type. |

| API call name | The backend API that the system calls when the task runs. |
|---|---|
| Concurrency | The maximum number of concurrent executions for the task. |
| Error threshold | The system stops the task when the number of errors reaches this threshold. |
| Remarks | The remarks for the task type. |
| Creation time | The time when the system created the task type. |

4. (Optional) Search for task types by **Type name/encoding** or by **Advanced Filter**.

**Add a task type**

1. On the Batch task type management page, click **Add type**.
2. In the **Basic information** section, specify the following parameters:

| Parameter | Description |
|---|---|
| Type name | The display name of the task type. This parameter is required. |
| Type encoding | The unique encoding of the task type. This parameter is required. |
| API call name | The backend API that the system calls when the task runs. |
| Instance parameter fields | The name of the parameter that passes the instance identity when the system calls the API. |
| Prompt text | The prompt message that the system displays when the task runs. |
| Remarks | The remarks for the task type. |
| Error stop threshold | The system stops the task when the number of errors reaches this threshold. |
| Concurrency limit | The limit on the number of concurrent executions for the task. |

3. (Optional) In the **Parameter rules** section, click **Add** to configure the parameters required
for task execution.

| Configuration item | Description |
|---|---|

| Parameter name | The name of the parameter. |
|---|---|
| API parameter name | The name of the input parameter for API calls. |
| Parameter type | The data type of the parameter, such as string. |
| Check regular | The regular expression that verifies the parameter value. |
| Prompt | The prompt message for the parameter. |

4. (Optional) In the **Verification rules** section, click **Add** to configure the verification items
for the instance before the task runs:

| Configuration item | Description |
|---|---|
| Attribute name | The attribute name of the validation object. |
| Verification rules | The comparison rule for the verification, such as Equal. |
| Check value | The target value for comparison. |
| Prompt information | The prompt message for a verification failure. |

5. Click **OK** to save the settings.

**Edit a task type**

1. Find the task type that you want to edit.
2. In the Operation column, click **Edit**.
3. After you modify the configuration, click **OK** to save the changes.

**Delete a task type**

1. Find the task type that you want to delete.
2. In the Operation column, click **Delete**.
3. In the message that appears, click **OK**.

> **Important:** You cannot delete a task type that is referenced by batch tasks. Make sure that no batch tasks reference the task type before you delete it.

###### 2.4.1.3.4 Instance dashboard

This topic describes how to use the instance dashboard feature in ApsaraDB O&M System Smart Pro Edition to view instance utilization rankings, quickly identify high-load instances, and perform O&M interventions. The instance dashboard displays the top 20 instances with the highest CPU, connection, IOPS, and disk utilization.

**Feature overview**

The instance dashboard provides two view modes:

| Mod e | Description |
|---|---|
| Overv iew | Displays the top 20 instances for four metrics in four columns. The system highlights instances that appear in multiple columns with a background color. |
| Detail ed | Displays the top 20 instances for a selected metric in a single column. You can switch between metrics. |

The page supports utilization rankings for the following four metrics:

| Metric | Description |
|---|---|
| CPU | The CPU utilization of the instance |
| Connections | The connection utilization of the instance |
| IOPS | The IOPS utilization of the instance |
| Disk | The disk utilization of the instance |

**Overview mode**

The overview mode displays the top 20 instances for four metrics in four columns to help you quickly identify instances with high load across multiple dimensions.
1. Log in to ApsaraDB Operations and Maintenance System Smart Edition. In the left-side
navigation pane, choose **Instance Management** > **Instance list**.
2. Go to the **Instance dashboard** page. The system displays the **Overview** mode by default.
3. View the top 20 instances for the four metrics.

> **Note:** When an instance appears in the top 20 lists of multiple metrics, the system highlights it with a background color. A pink background indicates that the instance appears in the lists of two metric. A red background indicates that the instance appears in the lists of three or more metrics. When you move the pointer over these instances, the message "The instance is listed in the N metric list" will be displayed.

**Detailed mode**

The detailed mode displays the top 20 instances for a selected metric in a bar chart.
1. On the instance dashboard page, click the **Detailed** tab.
2. Switch between metrics (CPU, connections, IOPS, and disk) by using the tabs at the top-
right corner.
3. View the rankings in the bar chart:

| Utilization range | Description |
|---|---|
| < 70% | Normal |
| 70% ~ 85% | Alert |
| >= 85% | Critical |

4. The left side of the chart displays the instance names and utilization percentages. The
instances are sorted in descending order of utilization from top to bottom.

> **Note:** The bar chart is displayed in a stacked manner, with different parts of the same instance in different utilization ranges highlighted in different colors. This facilitates visual comparison of load levels across instances.

**Multi-dimension load alerts**

The core value of the instance dashboard lies in cross-metric analysis. When an instance appears in the top rankings of multiple metrics, it indicates that the instance is under multidimension load pressure and requires special attention: Listed in the top rankings of two metrics (pink background): Monitor the overall load of the instance. Listed in the top rankings of three or more metrics (red background): Immediately check whether the instance has resource bottlenecks or abnormal load.

**Precautions**

The instance dashboard data comes from the Godseye performance collection system. The data update frequency depends on the performance collection configuration. In the overview mode, if no data is available for a metric, the corresponding column displays "No data". In the detailed mode, the bar chart sorts instances in descending order of utilization and displays only the top 20 instances.

###### 2.4.1.3.5 Recreate a secondary database

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

> **Note:** You can enter a keyword into the search box to quickly find the desired instance. You can also click Advanced Filter to customize filter conditions to locate the instance.

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

###### 2.4.1.3.6 Migrate an instance

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

> **Note:** The migration configuration varies depending on the database engine used. The actual migration configuration in the console prevails.
> You cannot migrate instances deployed in virtual private clouds (VPCs) to random zones.
> The vSwitch ID is required during cross-zone migration.
> The primary and standby nodes must be deployed in the same zone in primary zone mode.
> Instances for sale can be migrated only to the sales subdomain. Internal instances can be migrated only to the ODBS subdomain.

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

###### 2.4.1.3.7 Upgrade the minor version

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
following parameters, and then click **Submit**.

> **Note:** This topic uses PolarDB for MySQL Primary/Secondary Edition as an example. The parameters and page may vary depending on the database engine used. The actual configuration in the console prevails.

| Parameter | Description |
|---|---|
| Database Version | The major version of the current instance. The system supports only minor version upgrades within the same major version. |
| Small version number | Select the minor version to which the instance will be upgraded.T he current minor version of the instance will be displayed on the right side for comparison. |
| Specify method | Operation and maintenance time switching: The upgrade is performed during the specified maintenance window. You can configure the maintenance window in the Operation and maintenance time information section on the Basic information page of the instance. Switch now: The upgrade immediately takes effect and may affect your business. Specified time switch: The upgrade is performed at the scheduled time, which requires manual configuration. |

**View the upgrade progress**

After the upgrade task is initiated, you can go to the **Task Management** page to view the upgrade progress.

###### 2.4.1.3.8 Change the specification of a database instance

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

###### 2.4.1.3.9 Lock an instance

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

###### 2.4.1.3.10 Perform an HA switchover

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

> **Note:** Switch now: This method is used in emergency scenarios.
> Operation and maintenance time switching: This method is suitable for routine O&M, such as O&M in the early morning every day. The O&M task is automatically executed.
> Specified time switch: This method is suitable for specific time windows, such as application release.

5. After you complete the configuration, you can view the task progress on the **Task**
**Management** page until the task is complete. If the task is interrupted, contact Apsara
Stack technical support. For more information about how to view the task progress, see the Manage instance tasks topic.

**Verify the result**

After Step 4 is complete, the IP addresses and ports are reassigned to match the new primary and secondary roles. The HA task flow is complete.

**Perform a rollback**

Follow the same procedure to swap the roles of the primary and secondary nodes.

###### 2.4.1.3.11 Modify the storage capacity

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

> **Note:** You can view the details of all tasks, interrupted tasks, and paused tasks.
> You can also customize the columns displayed in the task list.

##### 2.4.1.4 Monitoring and alerting

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

##### 2.4.1.5 Diagnose an instance

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
The following metric groups are displayed on the page in a terminal-like style (dark theme).

> **Note:** Abnormal values are highlighted in red.

| Metric group | Metrics in the metric group |
|---|---|
| MySQL status | Queries per second (QPS), transactions per second (TPS), and the number of connections. |
| InnoDB row-related operations | The number of read rows, inserted rows, updated rows, and deleted rows. |
| Thread | The number of active threads and waiting threads. |
| InnoDB page | The number of dirty pages, idle pages, and data pages. |
| Fsync | Statistics on file synchronization operations. |

6. Click **STOP** to stop data collection.

> **Note:** The system automatically stops data collection when you switch to another tab. You must manually restart data collection after you return to this tab.

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

> **Note:** Up to 50 diagnosis records are displayed on each page.

**Execute SQL statements**

You can execute SQL statements online and check the results.

> **Warning:** Executing SQL statements is risky. Exercise caution when you perform this operation.

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
This tab displays all historical execution records, including SQL statements, execution time, destination database, and success/failed status. For a record that shows the successful execution of an SQL statement, the number of returned rows and the execution duration are displayed. For a record that shows a failure in executing an SQL statement, the error information is displayed.

> **Note:** You must switch a PolarDB child instance to the primary instance to execute SQL statements.

##### 2.4.1.6 View status inspection records

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

##### 2.4.1.7 Manage audit logs

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

##### 2.4.1.8 Change records

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

##### 2.4.1.9 Manage tasks

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

##### 2.4.1.10 Backup management

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

> The temporary backup is valid for only 18 hours. If the temporary backup expires, you need to re-initiate it.

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

> **Important:** This operation is irreversible once initiated.

##### 2.4.1.11 Data restoration

This topic describes how to perform data restoration operations in the ApsaraDB O&M System Smart Pro Edition console, including backup set-based restoration and point-in-time restoration.

**Restore data from a backup set**

This section describes how to restore the instance data to a point in time corresponding to a completed and valid backup set.

> **Important:** The instance must have at least one successful and valid backup set before a restoration is performed. You can check the validity of a backup set in the **Valid** column of the backup list. Invalid or corrupted backup sets cannot be used for restoration.
> If no backup set is available, create a temporary backup.

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

To restore data to a point in time, make sure that:

> Log backup is enabled.
> A valid full backup set exists, and no overlaying restoration has occurred between two full backups.
> The target point in time is within the log retention period.

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

##### 2.4.1.12 Security configuration

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
deletion.

> **Note:** Only IP addresses that are added to a whitelist can access the instance.

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

##### 2.4.1.13 Parameter configurations

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
Find the parameter that you want to modify, click Edit in the Operation column, and then configure a new value. Save the modification.

> **Note:** Some parameter changes require an instance restart to take effect. We recommend that you perform such operations during off-peak hours.
> Typical parameters include innodbbufferpoolsize, waittimeout, maxconnections, and characterset_server.

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

##### 2.4.1.14 O&M configurations

This topic describes how to manage temporary resource allocation and underlying O&M policies for instances in the ApsaraDB O&M System Smart Pro Edition console. You can temporarily increase computing or storage resources to handle traffic spikes, and configure system-level parameters such as high availability, log auditing, and performance metric collection.

**Temporary resource configurations**

This feature allows you to temporarily adjust computing resources (CPU and IOPS), the number of connections, and storage space for an instance during peak hours or emergencies. You can also configure an automatic restoration time to alleviate resource bottlenecks without changing the instance specifications.

> **Important:** Temporarily improving resource usage is used only for short-term mitigation. For sustained resource usage improvement, perform an instance specification change (configuration change).
> All temporary configurations must include a restoration value and a restoration time. The system automatically reverts to the original settings at the scheduled time.

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

You can temporarily expand the storage space of an instance to accommodate data surges.

> **Note:** Temporary disk expansion is irreversible. Upon expiration, the system automatically reverts to the original capacity.

| Parameter | Description |
|---|---|
| Maximum disk space | The target total disk capacity for temporary expansion (unit: GB). |
| Recovery value | The standard disk capacity configuration of the instance. The system automatically reverts the disk capacity configuration to this value upon expiration of the temporary adjustment. |
| Recovery time | The exact time when the temporary configuration expires and reverts to the original settings. |

**Configure the disk space check feature**

Specifies whether to lock the instance when the disk usage exceeds a specific limit.

> **Note:** When this feature is disabled, the instance is not locked even if disk usage exceeds the limit.

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

> **Important:** When this feature is enabled, the system implements strict memory resource isolation for the instance. When this feature is disabled, faults may occur. Currently, you cannot disable this feature.

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

You can configure a destination for storing SQL audit details.

> **Note:** If you want to modify settings, contact the TX team for technical support.

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

You can configure the version of the log audit feature.

> **Note:** If you want to modify settings, contact the TX team for technical support.

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

You can configure the timeout for backup set replay verification when you restore child instances, create read-only instances, create disaster recovery instances, or recreate secondary instances.

> **Note:** If you set this parameter to a non-zero value, the backup set is verified to ensure backup availability when you perform the preceding operations.

| Parameter | Description |
|---|---|
| Backup set playback verification timeout | The timeout period. Unit: seconds. If you set this parameter to 0, verification is skipped. |

**Configure the performance collection frequency**

You can configure the interval for collecting instance performance metrics, such as CPU, memory, and I/O.

| Parameter | Description |
|---|---|
| Collection frequency | The interval at which data is collected. Unit: seconds. A higher frequency enables finer-grained monitoring but increases system overhead. |

##### 2.4.1.15 Tag configurations

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
Find the tag that you want to manage and click **Edit** in the Operation column.

> **Note:** For a non-editable tag, Edit is unavailable in the Operation column.

5. In the dialog box that appears, modify the parameters described in the following table.

| Parameter | Description |
|---|---|
| Label type | This field is read-only and cannot be modified. |
| Current value | This field is required. |
| Expiration Time | Specify the expiration time. This field is optional. |

6. Click **OK**. The list is automatically updated.

##### 2.4.1.16 Manage databases

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

> **Note:** Separate multiple database names with commas (,).

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

##### 2.4.1.17 Account management

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

> **Note:** The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.

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

> **Note:** The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.

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

You can grant or revoke access permissions on specific databases for standard accounts.

> **Note:** The account must be a standard account.
> The account must have a list of permissions.

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

> **Note:** The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
> The system hides the reset password button for some special permission types, such as aurora and replicator.

5. Click **Submit**.

**Delete a system account**

You can delete specific system accounts. Exercise caution when you perform this operation.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Instance Management > Instance list**. Find the instance that you want to manage and click the instance name.
2. In the left-side navigation pane of the instance details page, click **Account information**.
Then, click the **System account** tab.
3. Find the account that you want to manage and click **Delete** in the Operation column.
4. In the message that appears, click **Submit**.

#### 2.4.2 Cluster instance list

##### 2.4.2.1 Cluster instance list overview

The cluster instance list page displays all cluster instances that the platform manages. It supports filtering by multiple dimensions and data export. On this page, you can quickly view instance information such as the status, service type, and version, and navigate to the instance details page for advanced management.

**Page layout**

Log in to ApsaraDB Operations and Maintenance System Smart Edition. In the left-side navigation pane, choose **Instance management > Cluster instance list**. The cluster instance list page consists of the following sections: Filter section: Provides filtering by cluster name, service type, and service version at the top of the page. Data list: Displays cluster instance information in a table and supports sorting and pagination. Export button: Allows you to export the current list data.

**List field descriptions**

| Field | Description |
|---|---|
| Instance name | The cluster instance name. You can click the name to navigate to the instance details page. |

| Business type | The business type identifier of the instance. |
|---|---|
| Instance level code | The instance level code. |
| Link type | The network link type of the instance. |
| Lock mode | The lock status mode of the instance. |
| Service type | The database service type that the instance uses. |
| Service version | The database service version of the instance. |
| Instance status | The current running status of the instance. |
| Creation time | The creation time of the instance. |
| Remarks | The remarks of the instance. |

**Filter conditions**

| Filter | Type | Description |
|---|---|---|
| Cluster name | Text box | Perform a fuzzy search by cluster instance name. |
| Service type | Drop-down list | Filter by database service type. The system dynamically loads the options. |
| Service version | Drop-down list | Filter by service version. You must select a service type first. |

**Instance status**

The following table describes common statuses of a cluster instance and their meanings:

| Status | Description |
|---|---|
| Creating | The system is creating the instance. |
| In use | The instance runs normally and provides services. |

| Reviewing | The system is reviewing the instance. |
|---|---|
| Deleting | The system is deleting the instance. |
| Restarting | The system is restarting the instance. |
| Migrating | The system is migrating the instance. |
| Upgrading/Downgrading | The system is upgrading or downgrading the instance specification. |
| Upgrading minor version | The system is upgrading the minor version of the instance. |
| Locked | The instance is locked and services are suspended. |
| Destroyed | The instance is destroyed. |
| Initializing | The system is initializing the instance. |

> **Note:** The complete status list contains more than 60 statuses that cover intermediate states of various operations such as creation, modification, migration, expansion, backup, and restoration.

**Data export**

The cluster instance list supports the data export feature. On the cluster instance list page, click the button in the upper-right corner of the page to export all data based on the filter conditions.

**View cluster instance details**

1.
2. The cluster instance details page is displayed.
This page displays the complete information of a single cluster instance and provides the following four feature subpages through the side menu. On this page, you can view instance properties, track task statuses, audit change history, and perform O&M operations such as specification changes, restarts, and locking.

| Feature subpage | Description |
|---|---|
| Basic instance information | Displays detailed information about the cluster instance, including instance information, specification information, network information, and region information, and provides access to O&M operations. |

| Task list | Displays all task records related to the instance, including task statuses, progress, and operation information. |
|---|---|
| Instance change records | Records all API call history of the instance, including API names, request times, request content, and response results. |
| Internal validation instance parameters | Displays and manages the kernel parameter configuration of Redis instances, including parameter viewing, editing, and modification history. This subpage is available only for Redis instances. |

##### 2.4.2.2 Basic information of cluster instances

The basic information of cluster instances page displays complete attribute information for a cluster instance, including instance, specification, network, and region information. Information sections vary by instance type, and the system dynamically loads the corresponding modules based on the service type of the instance.

**Entry**

1.
2. The system displays the **Basic instance information** subpage by default. You can also
navigate to this page from the left-side navigation menu.

**Information sections**

The basic instance information page displays instance properties in multiple sections. Each section supports independent refresh. Depending on the instance type, the displayed sections may include the following content.

> **Note:** The following information sections represent typical content for common instance types. The actual number of sections and fields varies based on the service type and database engine of the instance. The system dynamically loads the information sections that the instance type supports.
> For Lindorm instances, the system displays only basic information and does not provide operation buttons.

**Cluster instance information**

| Field | Description |
|---|---|
| name | The unique name of the cluster instance. |
| classCode | The specification ID of the instance. |
| status | The instance status, such as ACTIVE. |

| service | The database engine type of the instance, such as redis. |
|---|---|
| connType | The network connection type of the instance, such as LVS. |
| serviceVersion | The database version number of the instance. |
| bizType | The business type ID of the instance. |
| lockMode | The lock status of the instance, such as NOLOCK. |

**Specification information**

| Field | Description |
|---|---|
| classCode | The full instance name. |
| cpuCores | The number of CPU cores that the specification allocates. |
| maxQps | The maximum number of queries per second that the specification supports. |
| memSizeMB | The memory size that the specification allocates, in MB. |
| maxIops | The maximum number of I/O operations per second that the specification supports. |
| diskSizeMB | The disk size that the specification allocates, in MB. |
| maxConn | The maximum number of concurrent connections that the specification supports. |
| solationType | The resource isolation mode, such as COMMON. |
| category | The standard type of the specification, such as STANDARD. |

**Network information**

| Field | Description |
|---|---|

| address | The access endpoint of the instance. |
|---|---|
| netType | The network type of the instance, such as CLASSIC. |
| port | The access port of the instance. |
| vip | The virtual IP address of the instance. |
| vport | The virtual port of the instance. |
| type | The type of the connection endpoint, such as NORMAL. |
| userVisible | Specifies whether users can view the connection endpoint. |

**Region information**

| Field | Description |
|---|---|
| region | The ID of the region in which the instance resides. |
| avz | The ID of the zone in which the instance resides. |
| subDomain | The ID of the subdomain in which the instance resides. |

**Sub-instance information**

This section displays information about sub-instances, such as replica sets, under the instance. Click **View** to open the panel and view the detailed sub-instance list.

**Whitelist information**

This section displays the IP address whitelist configuration of the instance. Click **View** to open the panel and view the whitelist details.

**User information**

| Field | Description |
|---|---|
| userId | The ID of the user who owns the instance. |
| aliUid | The Alibaba Cloud account ID of the user who owns the instance. |

**O&M operations**

The page displays O&M operation buttons in the upper-right corner. The system dynamically generates buttons based on the service type and status of the instance. **Available**

**operations vary by instance type. Refer to the interface for the specific O&M**

**operations that the system supports.**

**Common operations**

| Operation | Description | Common applicable instance types |
|---|---|---|
| Restart the instance | Restart the service of the instance. | Redis/gpdb |
| Lock an instance | Control the lock status of the instance. | Redis/gpdb |
| Restore CS single node mode | Restore the single-node mode of the Redis cluster. | Redis |
| Unlock an instance | Control the lock status of the instance. | gpdb |
| Version Upgrade | Upgrade the database version of the instance. | gpdb |
| Delete an instance | Delete the instance. This operation is irreversible, and you cannot recover the data. | gpdb |
| HA manual switching | Manually trigger the HA switchover of the instance. | gpdb |
| Back-up | Rebuild the secondary database node of the instance. | gpdb |
| Specify minor version upgrade | Upgrade the instance to a specified database minor version. | gpdb |
| Vertical upgrade or downgrade | Adjust the vertical specification configuration of the instance. | gpdb |

**Risk levels of operations**

Each operation has a corresponding risk level. The confirmation dialog box displays the risk level and description of the current operation.

| > Document Version: 202608 | 28 | 9 |
|---|---|---|

| Risk level | Co lor | Description |
|---|---|---|
| User unperceived | Gr ee n | The operation is imperceptible to users and does not cause service interruption. |
| User-aware, but does not cause instance access disconnection. | Yel lo w | Users can perceive the operation, but it does not cause transient connections during instance access. |
| The user is aware and may cause instance access disconnection. | Or an ge | Users can perceive the operation, and it causes transient connections during instance access. |
| Sensitive operation | Re d | Users can perceive the operation, and it may cause severe consequences such as service termination. |

**General steps for performing an operation**

1. In the upper-right corner of the page, click an operation button.
2. In the dialog box that appears, review the risk warning and fill in the dynamically generated
form parameters.
3. Enter the reason for the change. This field is required.
4. Click **Submit**. The system automatically initiates an approval process or directly executes
the operation based on the operation type.

> **Important:** For some high-risk operations such as deleting an instance or clearing data, a secondary confirmation dialog box appears before execution. If the operation requires approval after submission, the system redirects you to the approval page.

##### 2.4.2.3 Task list

The task list page displays all task records related to the current cluster instance, including the task execution status, progress, and operation information. On this page, you can view the execution details, intervention records, and sub-workflows of a task.

**Page entry**

1.
2. In the left-side navigation menu, click **Task list**.

**Task list**

All task records related to the instance are displayed in a table. By default, this page sorts the tasks by time in descending order and supports pagination.

**Table fields**

| Field | Description |
|---|---|
| Task ID | The unique ID of the task. |
| Product CODE | The identification code of the product to which the task belongs. |
| Task name | The task type. |
| Target type | The type of the target object for the task operation, such as a cluster instance. |
| Target ID | The ID of the target instance for the task operation. |
| Task Status | The current execution status of the task, indicated by a colored dot. A red dot indicates task interruption, and a green dot indicates successful execution. |
| Progress | The task execution progress. |
| Remarks | The remarks for the task. |
| Workflow ID | The ID of the workflow associated with the task. |
| Operation | The buttons for available operations, which are displayed based on the task status. |

**Task status**

| Status | Color indicator | Description |
|---|---|---|
| Successful Execution | Green dot | The task is complete. |
| Task interruption | Red dot | An interruption occurred during task execution and requires manual intervention. |

**Operation column**

The Operation column of each task record provides buttons for the following operations. The system displays available operations based on the task status:

> **Note:** Not all operation buttons are visible for every task. The system displays available operations based on the status and type of the task.

| Operation | Description |
|---|---|
| Details | View the detailed information of the task. |
| Intervention record | View the manual intervention records of the task. |
| Sub-workflow | View the execution status of the sub-workflows associated with the task. |
| Add remarks | Add remarks to the task. |
| Retry | Re-execute a failed task. |
| Temporarily closed | Temporarily close the current task. |

**Batch operations**

The system provides a button for batch retry at the bottom of the list. Select multiple tasks and click **Batch retry** to retry multiple failed tasks at once.

**Pagination**

The system provides pagination controls at the bottom of the list, which display the total number of entries, the current page number, and the number of entries per page. Each page displays 10 entries by default.

##### 2.4.2.4 Instance change records

The instance change records page displays all API call records for the current cluster instance, including the interface name, request time, request content, and response result. You can check the complete history of all change operations on this page.

**Entry**

1.
2. In the left-side navigation menu, click **Instance change Records**.

**Filter conditions**

Click **Advanced Filter** to expand the full filter panel. The top of the page provides the following filter conditions to help you quickly locate the desired change records:

| 02 | > Document Version: 2026082 |
|---|---|

| Filter | Description |
|---|---|
| Interface name | Perform a fuzzy search by API name. |
| Request time | Filter by time range. You can specify a time range that is accurate to seconds. |
| Access IP | Filter by access IP address. |

**Change record list**

Change records are displayed in a table. The table shows common fields by default, and you can expand additional fields through the column settings feature.

**Default fields**

| Field | Description |
|---|---|
| Interface name | The name of the API that the change operation calls. |
| Request time | The time when the change request was initiated. |
| Request content | The detailed request parameters in JSON format. The system truncates long content, and you can click it to view the full content. |
| Response time | The time when the API returned a response. |
| Request result | The execution result of the request, indicated by color: green indicates success (such as 200 successful), and red indicates failure (such as 403 BackupJobExists). You can click it to view the full result details. |
| Operation user | The name of the user who performed the change operation. |
| Access IP | The IP address that initiated the change request. |
| AccessId | The access ID that initiated the request. |

**Expandable fields**

You can also display the following fields through the table column settings feature:

| Field | Description |
|---|---|
| Request Id | The unique ID of the request. |
| Time consumin g | The execution time from request initiation to response, in milliseconds. |
| Log Id | The log ID of the change record. |
| Instance name | The name of the instance involved in the change operation. |

**View request content**

The **Request content** column displays request parameters in JSON format. When the content exceeds 50 characters, the list truncates the display to the first 50 characters followed by an ellipsis. You can click the content to open a dialog box and view the complete formatted JSON content.

**View request results**

The **Request result** column uses colors to indicate the execution status of the request: Green text: indicates a successful request (such as "200 successful"). Red text: indicates a failed request (such as "403 BackupJobExists"). You can click the result to open a dialog box and view the complete response content.

**Pagination**

The system provides pagination controls at the bottom of the list, which display the total number of entries, the current page number, and the number of entries per page. Each page displays 10 entries by default.

##### 2.4.2.5 Kernel instance parameters

The kernel instance parameters page allows you to view and manage the kernel parameter configurations of Redis cluster instances. On this page, you can view the default and current values of parameters, modify editable parameters, and view the modification history of parameters.

> **Important:** This page is available only to Redis instances. For other instance types, you will not see this page in the navigation menu.

**Entry**

1.
2. In the left-side navigation menu, click **Internal validation instance parameters**.

**Parameter categories**

The top of the page displays parameters of different character set types, such as db, in tabs. Click a tab to switch to the parameter list of a different type.

**Filter conditions**

The following filter conditions are available above the parameter list:

| Filter | Description |
|---|---|
| Parameter type | Filter parameters by type. Available options include Read-only parameters, Read/write parameters (database will not be restarted), Read/write parameters (the database is automatically restarted), and External parameters (custom parameters automatically restart the database). |
| Parameter name | Perform a fuzzy search by parameter name. |

> **Note:** The parameter type filter determines the scope of parameters displayed in the list and the available operations.

**Parameter list**

All kernel parameters of the current type are displayed in a table. The table contains the following fields:

**Table fields**

| Field | Description |
|---|---|
| Parameter name | The kernel parameter name. |
| Default value | The system default value of the parameter. |
| Current value | The current effective value of the parameter. |
| Value range | The allowed value range of the parameter. |
| Unit | The unit of the parameter value. |
| Division factor | The divisor of the parameter value. |
| User-visible | Indicates whether the parameter is visible to users. Valid values: Yes and No. |

| User-modifiable | Indicates whether users can modify the parameter. Valid values: Yes and No. |
|---|---|
| Operation | The available operations, including Parameter modification history and Edit. |

**Operation instructions**

The Operation column of each parameter record provides the following operations:

> **Important:** Read-only parameters and parameters that are being synchronized do not support editing or viewing the modification history.

| Operatio n | Description | Limitations |
|---|---|---|
| Paramet er modifica tion history | Displays the modification history of the parameter. Click this button to open a panel that displays the modification history table of the parameter. | This operation is unavailable for read-only parameters and parameters that are being synchronized. |
| Edit | Modifies the parameter value. Click this button to open an edit dialog box where you can modify the parameter value and view the value range and unit. After modification, you must confirm the effective conditions, such as whether the database requires a restart. | This operation is unavailable for read-only parameters and parameters that are being synchronized. You cannot edit external parameters. |

**Top buttons**

The following buttons are available above the parameter list:

| Button | Description |
|---|---|
| Parameter modification history | Opens a panel that displays the modification history of all parameters under the current character set type. |
| Parameters being synchronized | Opens a panel that displays the list of parameters that are currently being synchronized. |

> **Important:** Kernel parameters are internal system configuration items, and changes to them may affect the running status of the instance. You should verify the value range and impact of a parameter before you modify it. Modifications of a read/write parameter that automatically restarts the database will trigger an automatic database restart. You should perform such modifications during off-peak periods.

**Pagination**

The system provides pagination controls at the bottom of the list, which display the total number of entries, the current page number, and the number of entries per page. Each page displays 10 entries by default.

### 2.5 Host management

#### 2.5.1 Host management overview

Host management is a core module of ApsaraDB O&M System Smart Pro Edition. This module allows you to manage the underlying physical machines and VMs on the platform in a unified manner. You can use the host management feature to view basic host information, monitor host running status, manage host resource configurations, and perform various O&M operations.

**Feature overview**

The host management module includes the following features:

| Feature | Description |
|---|---|
| System host | Displays a list of all hosts managed by the platform and supports multi- dimension filtering, resource cache refresh, and batch configuration. |
| Host details | Displays detailed information about a single host, including host information, ECS information, performance information, disk information, and namespace overview, and supports various O&M operations. |
| Host package management | Manages software packages installed on hosts and supports package installation, uninstallation, upgrade, and change record queries. |
| Physical machine group | Builds independent logical resource pools to achieve physical isolation and fine-grained scheduling of underlying hardware resources. |

**Host status**

The following table describes the statuses of hosts on the platform. The available operations for each host depend on the host's status:

| Status value | Status name | Description |
|---|---|---|
| 0 | Machine creation | The host is being initialized and created. |
| 1 | Normal operation | The host is running normally and can host instances. |

| 2 | Downtime | The host is experiencing downtime and cannot provide services. |
|---|---|---|
| 3 | Pre- disconnection | The host is undergoing the pre-disconnection process after downtime. |
| 4 | Maintenance pre- disconnection | The host is undergoing the pre-disconnection process for maintenance. |
| 5 | Officially offline | The host has been disconnected and no longer hosts instances. |
| 6 | Restart | The host is restarting. |
| 7 | Locked | The host is locked and does not accept new tasks. |

**Machine model series**

The platform supports the following machine model series:

| Model value | Model series | Description |
|---|---|---|
| 0 | D series model | D series physical machines. |
| 1 | S series model | S series physical machines. |
| 2 | ECS virtual machine | Elastic Computing Service (ECS) VMs. |
| 3 | N series hybrid storage | N series hybrid storage machines. |
| 4 | POLAR | POLAR series machines. |

#### 2.5.2 System host

The System host page displays all hosts that the platform manages and provides management capabilities such as multi-dimensional filtering, resource cache refresh, and batch configuration. On this page, you can quickly view the running status and resource usage of hosts, and navigate to host details for in-depth O&M.

**Page layout**

The System host page contains the following sections: Filter section: Located at the top of the page, this section provides multiple filter conditions and supports filtering by IP address, hostname, machine status, model, and database engine. Action button section: Located on the right side of the filter section, this section provides entry points for features such as refreshing the resource cache, grouping physical machines, and intelligent host diagnosis. Data list: Displays host information in a table format and supports sorting, pagination, and row selection. Batch operation section: Allows you to perform batch configuration operations after selecting multiple hosts.

**List field descriptions**

| Field | Description |
|---|---|
| IP | The IP address of the host. You can click it to navigate to the Host details page. |
| Hostname | The name of the host. |
| Cluster name | The name of the cluster to which the host belongs. |
| Data Center | The data center where the host is located. |
| Number of instances | The number of active instances that the host runs. |
| Database version | The database engine and version that run on the host. |
| Model | The model specification of the host. |
| Nic | The network interface controller (NIC) speed of the host. |
| Assign instances | Specifies whether the system allows new instance allocation on the current host: Allow or Not Allowed. |
| Machine status | The current running status of the host. |
| CPU | The CPU usage, in percentage. |
| Mem | The memory usage, in percentage. |
| Diskused | The disk usage, in percentage. |
| IO Util | The I/O usage, in percentage. |

| Data space usage | The data space usage, in percentage. |
|---|---|
| OS Load | The operating system load value. |
| Network card traffic | The real-time NIC traffic. |

**Filter conditions**

The System host page provides the following filter conditions to help you quickly locate target hosts:

| Filter | Type | Description |
|---|---|---|
| IP | Input box | Searches for hosts by exact IP address. |
| Hostname | Input box | Searches for hosts by a fuzzy match on the hostname. |
| Machine status | Multi-select drop- down | Filters hosts by running status, such as Normal operation, Downtime, and Locked. |
| Model | Multi-select drop- down | Filters hosts by model specification. |
| Database type | Drop-down | Filters hosts by database engine, such as MySQL or PostgreSQL. |
| Subdomain | Drop-down | Filters hosts by subdomain. |
| Cluster name | Drop-down | Filters hosts by cluster name. You must select a database engine first. |
| Data Center | Drop-down | Filters hosts by data center. You must select a cluster name first. |
| Single machine or not | Drop-down | Filters hosts by deployment mode: Single Machine or Multi-machine. |
| Cabinet | Multi-select drop- down | Filters hosts by cabinet. |
| Resource bucket | Drop-down | Filters hosts by whether they serve as resource bucket hosts: Yes or No. |

| Assign instances | Drop-down | Specifies whether the system allows new instance allocation on the current host: Allow or Not Allowed. |
|---|---|---|
| Capture task | Drop-down | Filters hosts by whether a capture task exists: Yes or No. |
| Publishing status | Multi-select drop- down | Filters hosts by publishing status, such as Publishing, Normal, or Publishing Failed. |
| Model Series | Multi-select drop- down | Filters hosts by model series, such as D series model, S series model, ECS virtual machine, and N series hybrid storage. |
| Host label | Multi-select drop- down | Filters hosts by host tag. |
| Kernel version | Multi-select drop- down | Filters hosts by operating system kernel version. |
| Host network card (M) | Input box | Filters hosts by NIC speed. |
| Business type | Multi-select drop- down | Filters hosts by business type, such as system hosts or SQL Server security hosts. |

**Instructions**

**View host details**

1.
2. The system navigates to the Host details page, which displays the complete information of
the host.

**Refresh the resource cache**

You can refresh the resource cache data for one or more hosts. This way, the platform retrieves the latest host resource information.
1. To refresh the resource cache data for specific hosts, select the hosts in the list.
2. At the top of the page, click **Refresh the resource cache**.
3. A confirmation dialog box prompts you to confirm whether to refresh the resource cache for
the selected hosts.
4. Click **OK** to complete the operation.

> **Important:** If you do not select any host, the system performs a global refresh and refreshes the resource cache for all hosts.

**Batch configuration**

You can configure multiple hosts in batches to specify whether to allow instance allocation and specify the recovery time.
1. Select one or multiple target hosts in the host list.
2. At the bottom of the host list, click **Batch configuration**.
3. In the dialog box that appears, configure the following parameters:
**Whether to allow instance allocation** : Select Allow or Not allowed.
**Restore to the time allowed for allocation** : Specify the time when the system
restores the permission to allocate instances. The default value is 7 days.
4. Click **OK** to complete the configuration.

**Manage tags**

1. Find the host whose tags that you want to manage and click **Sign** in the **Operation**
column.
2. In the dialog box that appears, find the tag that you want to edit click **Edit**.
3. In the Edit dialog box, modify the tag configuration and click OK. Then, click **OK** to save the
change.

**Delete a host**

> **Warning:** Deleting a host is a high-risk operation. Make sure that no critical instances are running on the host before you delete it.

1. Find the host that you want to delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

**Physical machine grouping**

1. Click **Physical Machine grouping** at the top of the **System host** page.
2. The system navigates to the Physical Machine grouping page. For more information, see
Physical machine group.

**Intelligent host diagnosis**

1. Click **Intelligent host diagnosis** at the top of the **System host** page.
2. The system navigates to the Intelligent host diagnosis page, where the system performs
intelligent diagnostics and analysis on the host.

#### 2.5.3 Host details

The host details page displays complete information about a single host and provides multiple feature subpages through the side menu. On this page, you can view host hardware information, performance metrics, disk status, and space overview, and perform O&M operations such as modifying remarks, switching clusters, and marking hosts as down.

**Page structure**

The host details page consists of the following sections: Header bar: Displays basic information such as the host IP address, hostname, database type, and cluster name, and provides O&M operation buttons. Side menu: Allows you to switch between feature subpages. Content area: Displays content based on the subpage you selected.

**Side menu**

The host details page contains the following side menu items:

| Menu item | Description |
|---|---|
| Host details | Displays basic host information, performance information, disk information, and a space overview. |
| Host instance information | Displays a list and details of all instances that run on this host. |
| Host performance information | Displays performance monitoring data of the host, including CPU, memory, and disk I/O metrics. |
| Host change record | Records the history of all change operations on this host. |
| Host package management | Allows you to manage software packages installed on this host. For more information, see Manage host software packages. |

**Host details page content**

The host details page organizes information in the following sections:

**Host information**

This section displays basic host attributes, including the host IP address, hostname, host status, server model, database type, cluster name, data center, rack, NIC speed, and kernel version.

**Performance information**

This section displays the current real-time performance metrics of the host, including CPU utilization, memory utilization, disk utilization, and I/O utilization.

**Disk information**

This section displays the disk partitions and usage of the host, including the mount point, total capacity, used space, and utilization of each partition.

**Space overview**

> **Note:** The system displays this section only when the database type is MySQL, SQL Server, or MongoDB.

This section displays a usage overview of the host data space and log space to help you quickly understand space allocation and consumption.

**O&M operations**

In the operation area at the top of the host details page, you can perform the following operations based on the host type and status:

**Modify remarks**

1. Click **Modify remarks**.
2. Enter remarks in the dialog box that appears. The remarks can be up to 500 characters in
length.
3. Click **OK** to save the remarks.

**Switch clusters**

Switch the current host to another cluster.
1. Click **Switch clusters**.
2. Select the destination cluster in the dialog box that appears.
3. Click **OK** to complete the switch.

**Tag management**

1. Click **Sign**.
2. Add or remove tags for the current host in the tag management dialog box that appears.
3. Close the dialog box after you complete the operation.

**Enable or disable instance allocation**

Control whether the system allows allocation of new database instances on the current host.
1. Click **Enable instance allocation** or **Disable instance assignment**.
2. In the confirmation dialog box, click **OK** to complete the operation.

> **Note:** This operation is available only for system hosts.

**Connectivity detection**

Check the network connectivity of the current host.
1. Click **Connectivity detection**.
2. The system automatically runs the detection and displays the results in a pop-up window
after the detection completes.

**Mark downtime**

> **Important:** After you mark a host as down, you cannot restore it to the normal state. Proceed with caution.

1. Click **Mark downtime**.
2. In the confirmation dialog box, confirm the operation risks and click **OK**.

> **Note:** This operation is supported only when the host status is Normal operation or Officially offline.

**Take HAProxy hosts offline**

> **Note:** The system displays this operation only when the database type is HAProxy.

1. Click the **Host offline** button.
2. Configure the following parameters in the dialog box that appears:
**Offline type**: Select "Graceful offline" or "Immediate offline".
**Force offline**: Select "Force" or "Do not force".
**Whether to re-match**: Select "Yes" or "No".
3. Click **OK** to complete the offline operation.

**Shutdown detection**

> **Note:** The system displays this operation only in the MiniDukang environment.

1. Click the **Shutdown detection** button.
2. The system runs the detection and displays the results in a pop-up window after the
detection completes.

**Retry failed tasks**

1. Click **Failed task retry**.
2. In the confirmation dialog box, click **OK** to retry the failed tasks on the host.
```html ```

#### 2.5.4 Manage host software packages

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

#### 2.5.5 Physical machine group

ApsaraDB O&M System Smart Pro Edition allows you to create physical machine groups to build independent logical resource pools in order to physically isolate underlying hardware resources and schedule them in a fine-grained manner. In this way, your businesses can use resources exclusively and stably.

**Background information**

The physical machine group feature allows you to build a resource pool consisting of multiple physical machines. The physical machines in the resource pool are isolated from other resources. This feature provides the following benefits: You can create different physical machine groups for database instances of different levels and types to physically isolate resources. You can isolate physical machines used in testing environments from those used in production environments so that testing and production instances will not be created on the same physical machine. This prevents stress tests on testing instances from compromising the performance of production instances. You can plan different resource pools for legacy and new machines during model upgrades.

> **Note:** The physical machine group feature currently supports only instances.
> After you create a physical machine group (for more information, see the Create a physical machine group section), you can specify the physical machine resource pool for a database instance when you create the instance in the Apsara Uni- Manager Management Console. For more information, see the Create an instance topic in the relevant User Guide.

**View all group information**

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

> **Note:** Before you delete a physical machine group, make sure that all instances deployed on the physical machine are cleared.

1. On the **Physical Machine grouping** page, find the physical machine group that you want
to delete and click **Delete** in the Operation column.
2. In the message that appears, click **OK**.

**Parameters**

| 18 | > Document Version: 2026082 |
|---|---|

| Parameter | Description |
|---|---|
| Custom group name | The group name. Only letters and digits are supported. |
| Database Engine | The database engine type of the group. |
| Machine | The list of physical machines in the group, including the hostname and the number of instances. |
| Operation | The Edit and Delete buttons. |

### 2.6 Cluster management

#### 2.6.1 Cluster management overview

Cluster management is a core module of ApsaraDB O&M System Smart Pro Edition. It allows you to manage resources such as database cluster instances, system clusters, service types, and service nodes in a unified manner. You can use this module to monitor cluster status, manage cluster configurations, and perform various O&M operations.

**Feature overview**

The cluster management module includes the following features:

| Feature | Description |
|---|---|
| System Cluster | View the list of system clusters managed by the platform, check the cluster status, and navigate to the cluster details page to view specific configuration information. |
| Service Type Management | View the service type categories and service type names supported by the cluster. |
| Service node management | Maintain service node information in the cluster, including the IP address, port, role, and status of each node. |
| Location | Configure the location (deployment position) information for the cluster and manage the region or zone attributes of the cluster. |

**Page structure**

The cluster management page consists of a left navigation menu and a right content area. The left navigation menu lists the entry points for each feature as shown below. You can click one of the following features to navigate to the corresponding feature page: System Cluster

> **Note:** In the system cluster list, you can click **Cluster Details** in the Operation column to navigate to the cluster details page, which displays the detailed configuration information of the cluster.

#### 2.6.2 System clusters

The System Cluster page displays all system clusters that the platform manages and serves as the primary entry point for the cluster management module. On this page, you can view basic cluster information, manage cluster configurations, and access the details page of an individual cluster for advanced management.

**Page layout**

The System Cluster page consists of three sections: the filter section, the action buttons section, and the data list.

**Filters**

The top of the page provides the following filters to help you quickly locate the target cluster:

| Filter | Description |
|---|---|
| Cluster name | Search for clusters by fuzzy-matching the cluster name. |
| Cluster label | Search for clusters by cluster label. |
| Ignore alerts | Filter clusters based on whether alerts are ignored. Available options: Yes and No. |
| Resources are tight | Filter clusters based on whether their resources are tight. Available options: Yes and No. |
| Database type | Filter clusters by database engine type in a cascading manner. |
| Link type | Filter clusters by link type. Available options: LVS, PROXY, and DNS. |
| Query Fangcun Mountain | Filter clusters based on whether Fangcun Mountain clusters are queried. Available options: Yes and No. |

| Resource allocation | Filter clusters by whether their resources are allocatable. Available options: Yes and No. |
|---|---|
| Cross-data center | Filter clusters by whether they are deployed across data centers. Available options: Yes and No. |
| Host pair allocation | Filter clusters by host pair allocation mode. Available options: Host pair and Single Machine. |
| Data Center | Filter clusters by data center name. |
| Location information | Filter clusters by data center or subdomain location. |
| Cluster business type | Filter clusters by business type. Available options: Open logon and Non- open logon. |

**Cluster list**

The system cluster list displays all cluster information in a table format and includes the following fields:

| Field | Description |
|---|---|
| Cluster name | The unique identifier of the cluster. Click the name to go to the System host page and view the host list of the cluster. |
| Link type | The network link type of the cluster, including LVS, PROXY, and DNS. |
| Database type | The database engine types that the cluster supports. |
| Synchronization mode | The data synchronization mode, including asynchronous, semi- synchronous, and dual channel. |
| Number of hosts (total/empty) | The total number of hosts and the number of idle hosts in the cluster. Click the value to view the host list. |
| Data Center (subdomain) | The data center subdomain to which the cluster belongs. |
| Data Center name | The name of the data center where the cluster resides. |
| Remarks | The remarks for the cluster. |

| Founder | The creator of the cluster. |
|---|---|
| Operation | The available operations, including viewing cluster details, editing cluster details, and deleting a cluster. |

**Create a cluster**

1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Cluster Management > System Cluster**.
2. On the **System Cluster** page, click **Create a cluster**.
3. In the panel that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Cluster name | The unique name of the cluster. The name is in the Region Data center _ 1 Data center 2 Engine ECS (optional) Business type format. Example: _ _ _ _ HANGZHOU EM21 MYSQL ECS. The name must start with an uppercase _ _ _ letter and can contain uppercase letters, digits, and underscores ( ). _ |
| Business type | The business type to which the cluster belongs. |
| Link type | The network link type, including LVS, PROXY, and DNS. For ODPS clusters, DNS is typically selected. If you select LVS, the cluster must be associated with Server Load Balancer (SLB) configurations. If you select PROXY, the cluster must be associated with SLB and Proxy Group. |
| Database type | The database engine type of the cluster. |
| Priority | The priority value of the cluster. |
| Whether to assign an instance | Specifies whether to enable instance allocation for this cluster. |
| Cross-data center | Specifies whether to deploy the cluster across data centers. If you enable this option, you must enter the cross-data center name. |
| Single-machine allocation | The resource allocation mode, including single-machine allocation or host pair allocation. |
| Find the number of available hosts first | The number of available hosts to search first when you assign instances. |
| Data Center name | The name of the data center in lowercase. This name must match the site name of the host. _ |

| Location information | The location information of the data center or subdomain. |
|---|---|
| Synchronization mode | The data synchronization mode, including asynchronous, semi-synchronous, and dual channel. |
| Resource retention percentage | The percentage of cluster resources not for sale. Valid values: 0 to 100. We recommend that you set this value to 0. |
| Remarks | The remarks for the cluster. |

4. After you confirm the configurations, click **OK** to complete the creation.

**Edit a cluster**

When you edit a cluster, you can modify its runtime configurations. You cannot modify the cluster name or database type in edit mode.
1. In the cluster list, find the cluster you want to edit.
2. In the Operation column, click **Edit**.
3. In the panel that appears, modify the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Cluster name | — | This parameter is read-only. |
| Business type | Yes | Select the business type of the cluster. |
| Link type | Yes | Select the network link type, such as LVS, PROXY, or DNS. For ODPS clusters, DNS is typically selected. If you select LVS, the cluster must be associated with SLB configurations. If you select PROXY, the cluster must be associated with SLB and a proxy group. |
| Database type | — | This parameter is read-only. |
| Priority | Yes | Configure the priority value of the cluster. The default value is 1. |
| Whether to assign an instance | Optional | Specify whether new instances can be allocated in this cluster. This option is enabled by default. |
| Cross-data center | Optional | Specify whether to deploy the cluster across data centers. |

| Single-machine allocation | Optional | Specify the resource allocation mode, including single- machine allocation and host pair allocation. This option is enabled by default. |
|---|---|---|
| Find the number of available hosts first | Optional | Specify the number of available hosts to search first when instances are allocated. The default value is 2. |
| Data Center name | Yes | Enter the data center name in lowercase. This name must match the site name of the host. If the site of the host is _ not in the site list of the cluster, the host becomes unavailable. |
| Location information | Yes | Select the location information of the data center or subdomain. |
| Synchronization mode | Yes | Select the data synchronization mode, including asynchronous, semi-synchronous, and dual channel. The default mode is semi-synchronous. |
| Resource retention percentage | Optional | Set the percentage of cluster resources not for sale. Valid values: 0 to 100. We recommend that you set this value to 0. |
| Remarks | Yes | Enter the remarks for the cluster. |

4. After you confirm the configurations, click **OK** to save the changes.

> **Note:** After you modify the cluster configurations, you must refresh the resource cache or wait 10 minutes for the changes to take effect.

**Manage tags**

1. In the cluster list, find the cluster that you want to manage.
2. In the Operation column, click **Label**.
3. In the Tag management dialog box, view the tag list of the current cluster. You can click
**Edit** in the Operation column to enable or disable a tag.

> **Note:** The tag management feature supports only viewing and editing operations. You cannot add new tags or delete existing tags.

**Delete a cluster**

1. In the cluster list, find the cluster that you want to delete.
2. In the Operation column, click **Delete**.
3. In the message that appears, click **OK**.

> **Important:** The operation is irreversible. Proceed with caution. You must obtain security approval before you delete a cluster.

**Cluster details**

In the cluster list, click **Cluster Details** in the Operation column to go to the Cluster Details page. This page displays a list of all hosts in the cluster.

**Features**

The Cluster Details page provides the following features: Basic cluster information: displays the basic attributes of the cluster, including the cluster name, database type, link type, business type, synchronization mode, priority, cross-data center deployment status, resource retention percentage, data center name, location information, and management IP address. Return to the cluster list: Click **Go back cluster list** in the upper-left corner of the page to return to the cluster list page. Modify the cluster: Click **Modify a cluster** in the upper-right corner of the page to open the cluster editing panel. For more information, see the Edit a cluster section above. Cluster operation logs: Click **Cluster operation logs** in the upper-right corner of the page to view the historical operation records of the cluster. View all hosts: Click the **View all hosts** link to view the complete list of all hosts in the cluster.

**Host list**

The Cluster Details page displays all hosts in the cluster in a table. The table contains the following fields:

| Field | Description |
|---|---|
| IP | The IP address of the host. Click the IP address to go to the host details page. |
| Hostname | The name of the host. |
| Data Center | The name of the data center where the host resides. |
| CPU usage | The CPU usage of the host, in percentage. |
| CPU sales rate | The CPU sales rate of the host, in percentage. |
| Memory usage | The memory usage of the host, in percentage. |
| Memory sales rate | The memory sales rate of the host. |

| Disk Usage | The disk usage of the host, in percentage. |
|---|---|
| Number of instances | The number of database instances that run on the host. |
| Database version | The version of the database that runs on the host. |
| Model | The model specification of the host. |
| Machine status | The running status of the host, such as normal. |

**Resource charts**

The Chart section below the host list displays bar charts that show the CPU and memory resource utilization of each host in the cluster. These charts help administrators quickly identify imbalances in resource allocation and usage. The Chart section contains the following two chart groups.

| Chart name | Description |
|---|---|
| CPU sales rate/Usage | Display the CPU sales rate (blue bars) and CPU usage (green bars) of each host in a bar chart. |
| Memory sales rate/usage rate | Display the memory sales rate (blue bars) and memory usage (green bars) of each host in a bar chart. |

X-axis: The host IP addresses. Y-axis: The percentage (0% to 80%). Legend: Blue bars represent the sales rate, and green bars represent the usage. Data source: The charts display the same data as the host list table above, and information is displayed by host. The charts update with the host list pagination, and each page displays data for up to 10 hosts. Empty state: The chart section is not displayed when the cluster contains no hosts.

**Batch operations**

After you select one or more clusters, the following batch operation buttons appear at the bottom of the page.

**Batch configuration**

You can configure the automatic expansion setting and recovery time for multiple clusters at a time. This feature helps you manage automatic expansion policies for multiple clusters in a unified manner.
1. Log in to the ApsaraDB O&M System Smart Pro Edition console. In the left-side navigation
pane, choose **Cluster Management > System Cluster**.
2. In the cluster list, select the clusters that you want to manage and click **Batch**
**configuration** at the bottom of the cluster list.
3. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Automatic expansion | Yes | Select Enable or Close. |
| Time to restore to automatic scale-out | Conditionall y required | If you set Automatic expansion to Close, you must specify the time to re-enable automatic expansion. |

4. Click **OK** to save the settings.

**Refresh synchronization mode**

You can refresh the data synchronization mode for multiple clusters at a time. This feature applies to scenarios where you need to adjust the synchronization policies of multiple clusters in a unified manner.
1. In the cluster list, select the clusters that you want to manage and click **Refresh**
**synchronization mode** at the bottom of the cluster list.
2. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Required | Description |
|---|---|---|
| Synchronization mode | Required | Select a synchronization mode: asynchronous, semi-synchronous, or dual-channel. |
| Refresh method | Required | Select Do not brush old instances or Brush old instances. |

3. Click **OK** to refresh synchronization mode.

**Refresh the resource cache**

You can refresh the resource cache data for multiple clusters at a time. This feature applies to scenarios where the cluster resource information is inconsistent with the actual state and you need to force a cache refresh.
1. In the cluster list, select the clusters that you want to manage and click **Refresh the**
**resource cache** at the bottom of the cluster list.
2. In the message that appears, click **OK** to refresh the resource cache.

> **Important:** This operation may take some time. Perform this operation during off-peak hours.

**Refresh backup without landing**

You can refresh the backup without landing policy for multiple clusters at a time. This feature applies to scenarios where you need to adjust the backup storage policies of multiple clusters in a unified manner.
1. In the cluster list, select the clusters that you want to manage and click **Refresh backup**
**without landing** at the bottom of the cluster list.
2. In the dialog box that appears, select a refresh backup policy.

| Policy | Description |
|---|---|
| Data logs do not land | Neither data nor logs are stored on local disks. |
| Data only | Only data is not stored on local disks. Logs are still stored on local disks. |
| Not enabled | Disable the backup without landing policy and restore the default landing storage. |

3. Click **OK** to perform the refresh.

**Single cluster operations**

After you select a single cluster, the operation area at the top of the page displays the following additional buttons.

**Configure a service node**

You can configure the service node allocation for a cluster. This feature applies to scenarios where you need to adjust the deployment and allocation of service nodes in a cluster.
1. Select the cluster that you want to manage and click **Configure a service node** at the top
of the cluster list.
2. In the message that appears, click OK. The Configure a service node panel appears.
3. Configure the service node information in the panel.
4. Save the changes after you complete the configuration.

**View whitelist**

View the management IP address whitelist of a cluster. This feature applies to scenarios where you need to verify the IP access control policy of the current cluster.
1. Select the cluster that you want to manage and click **View whitelist** at the top of the
cluster list.
2. In the dialog box that appears, view the IP address whitelist of the current cluster.

#### 2.6.3 Service type management

This topic describes the service type management feature. This feature allows you to maintain service type definitions for clusters, including service categories, cluster associations, exclusive attributes, and subtype configurations. You can view key information such as the ID, category, service name, and association status in the service type list to enable unified management and configuration of service types.

**Service type list**

All defined service types are displayed in a table. The table contains the following fields:

| Field | Description |
|---|---|
| ID | The unique ID of the service type. |
| Category | The service category (A, B, C, or D). |
| Service name | The service name. |
| Cluster Association | Indicates whether the service type is associated with a cluster (Yes or No). |
| Cluster exclusive | Indicates whether the service type is exclusive to a cluster (Yes or No). |
| Is there a subtype | Indicates whether the service type contains subtypes (Yes or No). |

#### 2.6.4 Service node management

The service node management page allows you to maintain service node information in a cluster, including configurations such as the IP address, port, role, and status of each node.

**Filter conditions**

The page provides the following filter conditions at the top:

| Filter | Description |
|---|---|
| IP | Search by node IP address. |
| Name | Search by node name. |
| Service type | Filter by service type. |
| Data Center | Filter by data center name. |

**Service node list**

All node information are displayed in a table. The table includes the following fields:

| Field | Description |
|---|---|
| bakId | The unique ID of the node. |

| IP | The IP address of the node. |
|---|---|
| PORT | The port number of the node. |
| Name | The node name. |
| Type | The service type. Display format: [Category] service name. |
| Role | The node role. Valid values: master and slave. |
| Data Center | The name of the data center where the node resides. |
| Number of clusters | The number of associated clusters. Click the number to view cluster details. |
| Service Status | The service status of the node. Valid values: Normal, and Machine Offline. |
| Publishing status | The publishing status of the node. Valid values: Publishing, Normal, and Publishing failed. |
| Logical group | The logical group to which the node belongs. |
| Operation | The available operations (Edit/Delete). |

**Create a service node**

1.
2. On the service node management page, click **Create a service node**.
3. In the panel that appears, configure the following parameters:

| Parameter | Description |
|---|---|
| IP | The IP address of the node. |
| PORT | The port number of the node. |
| Name | The node name. |
| Role | The node role. Valid values: master and slave. |

| Logical group | Enter the logical group to which the node belongs. |
|---|---|
| Data Center | The data center where the node resides. |
| Publishing status | The publishing status of the node. Valid values: Publishing, Normal, and Publishing failed. |
| API URL _ | The API URL in JSON format. |
| Service type | The service type. |

4. Click **OK** to complete the creation.

**Edit a service node**

1. In the service node list, find the node that you want to edit.
2. In the Operation column, click **Edit**.
3. In the panel that appears, modify the node configuration. You can also add child nodes
(IP/PORT/Resource Type).
4. Click **OK** to save the changes.

**Delete a service node**

1. In the service node list, find the node that you want to delete.
2. In the Operation column, click **Delete**.
3. In the confirmation dialog box, click **OK**.

**Du Kang health check**

Click **Du Kang health check** at the top of the page to open the health check panel and check the health status of service nodes.

**View cluster information**

In the service node list, click the number in the **Number of clusters** column. A dialog box appears and displays all cluster information associated with the node, including fields such as Cluster name, Location, Priority, Whether to assign an instance, and OnECS.

#### 2.6.5 Location

The Location page allows you to maintain the location information tree of ApsaraDB O&M System Smart Pro Edition. It organizes location data such as units, regions, zones, subdomains, and clusters in a hierarchical structure and provides cluster consistency check and subdomain consistency check features.

**Page layout**

The Location page displays data in two sections: Left section: The location directory tree, which supports search and node management. Right section: The details of the selected node, which includes the Cluster consistency check and Subdomain consistency check tabs.

**Location directory tree**

The location directory tree displays the hierarchical relationships of location information, which include the following levels from top to bottom:

| Level | Description |
|---|---|
| Unit | The top-level organization unit. |
| Region | A geographic region. |
| Zone | A zone. |
| Subdomain | A subdomain identifier. |
| Cluster | A leaf node that associates with a specific database cluster. |

The tree nodes are marked with colored tags to indicate different levels: Unit: Red tag Region: Blue tag Zone: Purple tag Subdomain: Green tag

**Search for nodes**

Enter a keyword in the search box above the directory tree to filter and display matching nodes. The system automatically displays all matching results during the search.

**Refresh data**

If the location data does not update, click **Click here to refresh** above the directory tree to refresh the location information.

**Parameter management**

On the right side of a tree node, click **Parameter** to manage the parameter configuration of that node level.

**Cluster consistency check**

After you select a location node, on the **Cluster consistency check** tab on the right, you can view the consistency status of all clusters under that node and associate or disassociate clusters.

**Subdomain consistency check**

After you select a location node, on the **Subdomain consistency check** tab on the right, you can check the consistency of subdomain configurations and identify inconsistencies.

### 2.7 Task management

#### 2.7.1 Task management overview

Task management is a core O&M feature of ApsaraDB O&M System Smart Pro Edition. It allows you to manage and monitor all O&M tasks on the platform in a unified manner. You can use this module to view the execution status of tasks, manage task execution workflows, analyze task statistics, and perform interventions such as retrying or closing tasks.

**Feature overview**

The task management module includes the following features:

| Page | Subpage | Description |
|---|---|---|
| Pengine Task | Instance task list | View all pengine task lists with multi-dimensional filtering and batch operations. |
|   | PengineClass Meta tools | Manage the class metadata of pengine tasks to define task types and attributes. |
|   | PengineStep Meta tools | Manage the step metadata of pengine tasks to define task execution steps and parameters. |
|   | Task statistics | Analyze task execution statistics, including success rates, failure rates, and task type distribution. |
| Grand Canal Task | / | Manage tasks generated by the Grand Canal workflow engine. |
| Migration Task | / | View and manage database instance migration tasks. |

**Task engine**

The platform supports two types of task engines:

| Task engine | Applicable scenarios |
|---|---|
| Pengine | This engine manages O&M tasks for services deployed on Tianji. |
| Grand Canal | This engine manages O&M tasks for services deployed on PaaS. |

**Task status**

**Pengine task status**

| Status value | Status name | Description |
|---|---|---|
| 0 | Waiting | The task has been created and is waiting for scheduling and execution. |
| 1 | Running | The task is running. |
| 2 | Ended | The task is complete. |
| 3 | Failed | The task failed. |
| 4 | Closed | The task is manually closed. |
| 5 | Canceled | The task is canceled. |
| 6 | Retrying | The task is retrying. |
| 7 | Paused | The task is paused. |
| 8 | Interrupted | The task execution is interrupted. |

**Grand Canal task status**

| Status value | Status name | Description |
|---|---|---|
| WAITING | Waiting | The task is waiting for execution. |
| RUNNING | Running | The task is running. |
| COMPLETED | Successful Execution | The task is complete. |
| TEMP TERMINATED _ | Temporarily closed | The task is temporarily closed. |
| FAILED | Task failed | The task failed. |
| PAUSE | Task paused | The task is paused. |

| HUMAN PROCESSING _ | Task interruption | The task is interrupted and requires manual processing. |
|---|---|---|
| BLOCKING | Interrupted | The task is under interruption. |

#### 2.7.2 Pengine tasks

##### 2.7.2.1 Pengine task overview

Pengine is a task engine developed by ApsaraDB O&M System Smart Pro Edition. It allows you to manage various tasks during database O&M, such as instance creation, specification changes, and version upgrades. All O&M operations initiated through the system, such as backup, migration, and parameter changes, ultimately run as Pengine tasks.

**Task engine concepts**

Pengine tasks adopt a layered architecture: Task: A complete O&M operation that contains multiple execution steps. Each task has a unique ID, status, progress, and executor. Step: A specific execution unit of a task. Each step corresponds to an atomic operation. Steps run in sequence and support retry on failure. Class: The type of a task. It determines the steps and parameters that the task includes.

**Task status description**

Pengine tasks have the following lifecycle states:

| Status | Color | Description |
|---|---|---|
| Waiting | Blue | The task is created and waits for scheduling. |
| Running | Blue | The task is running. |
| Ended | Green | The task is complete. |
| Failed | Red | The task failed. |
| Closed | Yellow | The task is manually closed. |
| Canceled | Yellow | The task is canceled. |
| Retrying | Blue | The task is retrying. |

| Paused | Yellow | The task is paused. |
|---|---|---|
| Interrupted | Red | The task execution was interrupted. |

**Task management entry**

The Pengine Task feature includes the following sub-features. For details, see the corresponding sub-documents: Instance task list: This feature allows you to view and manage all Pengine tasks. It supports multi-dimensional filtering, batch operations, and detail viewing. PengineClass Meta tools: This feature allows you to manage the metadata definitions of task types, including the steps and parameters that each task contains. PengineStep Meta tools: This feature allows you to manage the metadata definitions of task steps, including step execution parameters and timeout configuration. Task statistics: This feature allows you to perform statistical analysis of task execution, including success rate, failure rate, and task type distribution.

##### 2.7.2.2 Instance task list

The instance task list page displays all tasks from the Pengine task engine and provides management features such as multi-dimensional filtering, batch retry, and viewing details. You can monitor task execution status, view task details, add notes, and manage subtasks and intervention records on this page.

**Supported database types**

| Database type | Value |
|---|---|
| MySQL | mysql |
| Redis | redis |
| PostgreSQL | pgsql |
| MongoDB | mongodb |
| PolarX | polarx |
| ADB | adb |
| Lindorm | lindorm |

**Page layout**

The instance task list page consists of the following components: Filter: Located at the top of the page, the filter allows you to filter tasks by dimensions such as task status, database type, responsibility, and object type. Batch operation buttons: This page provides buttons for operations such as batch retry and batch preferential execution. Data list: The list displays task information and supports row selection and pagination.

**List fields**

| Field | Description |
|---|---|
| Task ID | The unique ID of the task. You can click it to view the task details. |
| Task name | The class name of the Pengine task. If this field is empty, the system displays the task key. |
| Source | The task creator name. |
| Operation object | The name of the target object for the task operation. You can click it to navigate to the instance details page. |
| Parent task | The ID of the parent task of the current task, if applicable. You can click it to navigate to the parent task details page. |
| Status | The task status. |
| Progress | The task progress. |
| Time consuming | The total execution time of the task. |
| Executor | The task executor name. |
| Creation time | The time when the task was created. |
| Modification time | The time when the task was last modified. |
| Responsible Person | The person responsible for the task. |
| Remarks | The remarks for the task. |

| Operation | The available operations, such as viewing details, adding or modifying remarks, viewing intervention records, and viewing subtasks. |
|---|---|

**Filter conditions**

| Filter | Type | Description |
|---|---|---|
| Task Status | Drop-down list | Filter tasks by status. The Interrupted status is selected by default. Valid values: Waiting, Running, Ended, Failed, Closed, Canceled, Retrying, Paused, and Interrupted. |
| Database type | Drop-down list | Filter tasks by database type. Valid values: MySQL, Redis, PostgreSQL, MongoDB, PolarX, ADB, and Lindorm. |
| Responsibilit ies | Drop-down list | Filter tasks by responsibility. Valid values: I executed it, I created, and I'm in charge. |
| Object Type | Drop-down list | Filter tasks by object type. Valid values: User instance tasks, Host instance tasks, and Host task. |
| Host IP | Input box | Filter tasks by host IP address. |
| Instance ID | Numeric input | Perform a precise search by instance ID. |
| Instance name | Input box | Perform a fuzzy search by instance name. |
| Start time | Date picker | Filter tasks by start time. |
| End time | Date picker | Filter tasks by end time. |

**Instructions**

**View task details**

1.
2. On the instance task list page, click the **Task ID** of the task that you want to manage.
3. The page redirects to the task details page and displays the complete execution
information of the task.

> **Note:** For pending tasks that have not yet generated a Pengine class, the system displays a remarks dialog box where you can prioritize or close the task.

**Add or modify remarks**

1. In the **Operation** column of the task list, click **Add remarks** or **Modify remarks**.
2. Enter remarks in the dialog box.
3. Click **OK** to save the remarks.

**View intervention records**

1. In the **Operation** column of the task list, click **Intervention record**.
2. In the panel that is displayed, view all manual intervention records of the task.

**View subtasks**

1. In the **Operation** column of the task list, click **View subtasks**.

> **Note:** This operation is available only when the task contains subtasks.

2. In the panel that is displayed, view all subtasks of the task.

**Batch retry**

1. Select one or more tasks in the task list.
2. Click **Batch retry** in the top-left corner.
3. In the confirmation dialog box, click **OK** to perform a batch retry.

> **Note:** You must select at least one task before you perform a batch retry.

##### 2.7.2.3 PengineClass Meta tool

The PengineClass Meta tools page allows you to manage the class metadata of the Pengine task engine. Class metadata defines the basic attributes of task types, including the task name, description, and whether the task can be canceled. It serves as the basic configuration for Pengine task scheduling and execution.

**Page layout**

The PengineClass Meta tools page consists of the following sections: Filter section: allows you to filter records by Pengine class name and description. Button section: provides buttons for you to perform operations such as adding, exporting data, and clearing change history. Data list: displays all class metadata records.

**Parameters**

| Parameter | Description |
|---|---|
| id | The unique ID of the record. |
| pengine class | The class of the Pengine task. |
| pengine description | The class description. |
| can cancel | Indicates whether tasks of this type can be canceled. |
| operation | The Edit and Delete buttons. |

**View the class metadata list**

1.
2. In the left-side navigation pane, click **PengineClass Meta tools**.
3. The page displays all class metadata records.
4. You can use filter conditions to quickly locate the records that you want to manage.

**Add class metadata**

1. Click **Add** in the upper-left corner of the page.
2. In the dialog box that appears, enter the following information:
**pengine class**: The class name.
**class desc**: The class description.
**can cancel**: Indicates whether the task can be canceled. A value of 0 indicates that the
task cannot be canceled, and a value of 1 indicates that the task can be canceled.
3. Click **OK**.

**Edit class metadata**

1. In the **operation** column of the list, click **Edit**.

> **Important:** You cannot edit records that contain system data (where systemData is set to true).

2. In the dialog box that appears, modify the description.
3. Click **OK** to save the changes.

> **Important:** You can modify only the desc field (description). The Pengine class name and ID cannot be modified.

**Delete class metadata**

> **Important:** Before you delete class metadata, make sure that no task records are associated with this type.

1. In the **operation** column of the list, click **Delete**.
2. In the confirmation dialog box, click **OK**.

> **Note:** You cannot delete records that contain system data (where systemData is set to true).

**Export data**

The PengineClass Meta tools page provides two export methods: Export the current list data: This method exports the data currently displayed in the table. Export changed data: This method exports only the data that has changed since the last synchronization.

**Clear change history**

> **Warning:** After you clear change history, all change records will be permanently deleted. This operation is irreversible.

1. Click **Clear change history** in the upper-left corner.
2. In the confirmation dialog box, click **OK**.

##### 2.7.2.4 PengineStep Meta tool

The PengineStep Meta tools page allows you to manage step metadata for the Pengine task engine. This metadata defines the detailed configuration for each step during task execution, including parameters such as the timeout period, retry count, alert type, and rollback steps. It serves as the core configuration for controlling the Pengine task execution flow.

**Page layout**

The PengineStep Meta tools page consists of the following sections: Filter section: allows you to filter records by Pengine class and step name. Button section: provides buttons for you to perform operations such as adding records. Data list: displays all step metadata records.

**Parameters**

| Parameter | Description |
|---|---|
| id | The unique ID of the record. |

| pengine class | The name of the Pengine class to which the record belongs. |
|---|---|
| step name | The step name. |
| timeout | The step timeout period in seconds. |
| step description | The step description. |
| ops advice | The O&M advice. |
| retries | The number of retries. |
| alert type | The alert type. |
| rollbackStep | The name of the rollback step. |
| retryInterval | The retry interval. |
| canCancel | Indicates whether the step can be canceled. |
| progressInfo | The progress information. |
| workNo | The employee ID. |
| skipRisk | Indicates whether to skip the risk check. |
| operation | The Edit and Delete buttons. |

**View the step metadata list**

1.
2. In the left-side navigation pane, click **PengineStep Meta tools**.
3. The page displays all step metadata records.
4. You can use filter conditions to quickly locate the records that you want to manage.

**Add step metadata**

1. Click the **Add** button in the upper-left corner of the page.
2. Fill in the required information in the dialog box that appears.
3. Click **OK**.

**Edit step metadata**

1. In the **operation** column of the list, click **Edit**.
2. Modify the following fields in the dialog box that appears:
**timeout**: The step timeout period.
**desc**: The step description.
**opsSuggest**: The O&M advice.
**retries**: The number of retries.
**alertType**: The alert type.
**workNo**: The employee ID.
**skipRisk**: Indicates whether to skip the risk check.
3. Click **OK** to save the changes.

> **Note:** The pengine class, step name, rollbackStep, retryInterval, canCancel, and progressInfo fields are read-only and cannot be modified. For system data, the desc and opsSuggest fields also cannot be modified.

**Delete step metadata**

> **Important:** Before you delete step metadata, make sure that no task execution records are associated with the step.

1. In the **operation** column of the list, click **Delete**.
2. In the confirmation dialog box, click **OK**.

##### 2.7.2.5 Task statistics

The task statistics page provides statistical analysis of Pengine task execution. You can view key metrics such as the number of executed tasks, failure rate, and task type distribution in the charts. This helps you understand the status of tasks running on the platform.

**Page layout**

The task statistics page consists of the following sections: Time range selection section: provides a date range picker at the top of the page. Data from the last 7 days are displayed by default. Chart section: displays statistical analysis results in column charts and line charts.

**Chart descriptions**

**Overall task execution**

A stacked column chart displays the daily executed tasks within the selected time range, including the distribution of successful and failed tasks. Horizontal axis: Date. Vertical axis: Number of tasks. Color: Successful tasks appear in green, and failed tasks appear in orange.

**Task failure statistics**

An area line chart displays the trend of task failure rate within the selected time range, which helps you identify abnormal fluctuations in the failure rate. Horizontal axis: Time. Vertical axis: Failure rate. Trend: Displayed by the line.

**Types of tasks that have been executed the most times**

A column chart displays the ranking of the types of tasks that have been executed the most times within the selected time range. This helps you understand the primary types of tasks on the platform. Horizontal axis: Task type. Vertical axis: Number of executions. Annotation: The top of each column displays the specific value.

**Types of tasks that failed the most times**

A column chart displays the ranking of the types of tasks that failed the most times within the selected time range. This helps you identify task types with frequent failures. Horizontal axis: Task type. Vertical axis: Number of failures. Annotation: The top of each column displays the specific value.

**Operation instructions**

**Adjust the statistical time range**

1. In the date range picker at the top of the page, select a start date and an end date.
2. The page automatically refreshes the chart data after you make a selection.

> **Note:** The default time range is the last 7 days. You can select any time range for statistical analysis.

**Usage recommendations**

Routine inspection: Regularly review the overall task execution and failure statistics to identify exceptions. Troubleshooting: When the failure rate increases abnormally, use the **Types of tasks that**
**failed the most times** chart to identify the task types with high failure rates.
Capacity planning: Use the **Types of tasks that have performed the most times** chart to understand the task load distribution on the platform and inform resource planning.

#### 2.7.3 Grand Canal task

Grand Canal is the workflow engine of the platform and processes complex, multi-step O&M tasks. The Grand Canal task page displays the execution status of all workflow tasks and provides management operations such as multi-dimensional filtering and batch retry.

**Page layout**

The Grand Canal task page consists of the following componenets: Filters: You can use filters at the top of the page to filter tasks by job ID, workflow ID, workflow name, target ID, service code, target type, task status, and time. Batch operation button: After you select multiple tasks, you can perform a batch retry. Data list: This list displays workflow task information.

**Filter conditions**

| Filter | Type | Description |
|---|---|---|
| Task ID | Input box | Search by job ID for an exact match. |
| Workflow ID | Input box | Search by workflow ID for an exact match. |
| Workflow name | Input box | Search by workflow name for a fuzzy match. |
| Target ID | Input box | Search by target object ID. |
| Product Code | Drop-down list | Filter by product code. The system loads options dynamically. |
| Target type | Drop-down list | Filter by Target type. |
| Task Status | Drop-down list | Filter by Task status. The Task interruption status is selected by default. |
| Time | Date range | Filter by time range. |

**Target type**

| Target type | Description |
|---|---|
| Cluster instance | The target is a cluster instance. |
| User instance | The target is a user instance. |
| Host | The target is a host. |

| K8S cluster | The target is a Kubernetes cluster. |
|---|---|

**Task status**

| Status | Description |
|---|---|
| Waiting | The task is waiting for execution. |
| Running | The task is running. |
| Successful Execution | The task is complete. |
| Temporarily closed | The task is temporarily closed. |
| Task failed | The task failed to execute. |
| Task paused | The task is paused. |
| Task interruption | The task encountered an interruption and requires manual intervention. |
| Interrupted | The task is being interrupted. |

**Batch retry**

You can retry multiple tasks that are in the Task paused or Task interruption status. 1.
2. Select one or more tasks from the task list.

> **Note:** The batch retry button is available only when all selected tasks are in the Task paused or Task interruption status.

3. Click **Batch retry** at the bottom of the page.
4. In the confirmation dialog box, click **OK**.

**List fields**

The Grand Canal task list displays the following key information:

| Field | Description |
|---|---|

| Task ID | The unique ID of the workflow task. |
|---|---|
| Workflow ID | The unique ID of the workflow instance. |
| Workflow name | The workflow name. |
| Target ID | The ID of the target object for the task operation. |
| Target type | The type of the target object, such as a cluster instance, user instance, host, or Kubernetes cluster. |
| Product CODE | The code of the product to which the task belongs. |
| Task Status | The task status. |
| Progress | The task progress. |
| Workflow time consuming | The total execution time of the task. |
| Creation time | The time when the task was created. |
| Operation | The available operations, such as viewing details. |

#### 2.7.4 Migration task

The migration task page displays the execution details of database instance migration tasks, including the migration status and the specification and namespace information of the source and destination instances. On this page, you can monitor migration progress and track the status of each phase of a migration task.

**Page layout**

The migration task page displays all migration task information in a list and supports pagination.

**List fields**

| Field | Description |
|---|---|
| Migration ID | The unique ID of the migration task. |
| SOURCE instance name | The name of the source instance for the migration. |

| Target instance name | The name of the destination instance for the migration. |
|---|---|
| Migration status | The status of the migration task. |
| SOURCE specification | The specification of the source instance. |
| Target Specification | The specification of the destination instance. |
| SOURCE Space | The disk space size of the source instance. |
| Target space | The disk space size of the destination instance. |
| Start migration time | The start time of the migration task. |
| Switching time | The time when the virtual IP (VIP) switching occurs during migration. |

**Migration status**

A migration task has the following statuses:

| Status value | Status name | Description |
|---|---|---|
| 0 | Not started | The migration task has not started. |
| 10 | Pending review | The migration task is pending review. |
| 14 | Not started | The migration task is created but not started. |
| 1 | vip before switching | The migration is in progress and the VIP has not switched. |
| 11 | vip before switching | The migration is in progress and the VIP has not switched. |
| 15 | Waiting | The migration task is waiting for execution. |
| 16 | After VIP switching | The VIP has switched and the migration is proceeding with subsequent steps. |

| 2 | Ended successfully | The migration task is complete. |
|---|---|---|
| 12 | Ended successfully | The migration task is complete. |
| 3 | Failed | The migration task failed. |
| 13 | Failed | The migration task failed. |
| 99 | Canceled | The migration task is canceled. |

**View the migration task list**

1.
2. The page displays all migration tasks in a list.
You can browse all historical migration records by turning pages.

**Migration workflow**

A migration task typically goes through the following phases:
1. Pending review or not started: The migration task has been created and is waiting for
review or startup.
2. Before VIP switching: During the data synchronization phase, the system is synchronizing
data from the source instance to the destination instance, and the VIP has not switched to the destination instance.
3. After VIP switching: The VIP has switched to the destination instance, and the system
proceeds with subsequent cleanup and verification steps.
4. Ended successfully, failed, or canceled: The migration task ends and the final status is
displayed based on the execution result.

> **Note:** If an exception occurs during the migration, the task status changes to Failed. You can locate the issue based on the failure cause and then initiate the migration again.

### 2.8 Log management

This topic describes the log management feature of ApsaraDB O&M System Smart Pro Edition. Log management centrally records various operations and events during platform operation to help you trace operations, locate system issues, audit O&M actions, and monitor key events such as HA switchovers.

**Feature overview**

The log management page organizes data into tabs and allows you to query and audit the following seven types of logs:

| Tab | Description |
|---|---|
| Operation Log | Records all management operations on the platform and supports filtering by operation type and time range. |
| Kernel instance parameter modification history | Records the change history of database kernel parameters. |
| RDS API call logs | Records all call requests initiated through the RDS API. |
| API call logs | Records details about all API calls on the platform. |
| HA switch log | Records the triggering and execution processes of HA switchovers. |
| General O & M audit logs | Records audit information for general O&M operations. |
| Custom template execution records | Records the execution history of custom SQL templates. |

**Operation log**

This tab records all management operations performed by users on the platform. It helps you trace user operations and audit O&M activities.

**Filter conditions**

| Filter | Description |
|---|---|
| Operation user | Search by the operator username. |
| Operation object ID | Search by operation object ID. |
| Operation object category | Filter by the operation object type. |
| Start time | Filter by the start time of the operation. |
| End time | Filter by the end time of the operation. |

**Operation log list**

| Field | Description |
|---|---|

| Operation object category | The operation object type. |
|---|---|
| Operation object Id | The unique ID of the operation object. |
| Creation time | The time when the operation occurred. |
| Operation user | The operator username. |
| Operation description | The detailed description of the operation. |

**Kernel instance parameter modification history**

This tab records modifications to the kernel parameters of a database instance, including the parameter name, the original value before the modification, and the new value after the modification. It helps you track parameter changes.

**Parameter modification history list**

| Field | Description |
|---|---|
| Change ID | The unique ID of the modification record. |
| Instance ID | The ID of the instance where the parameter modification occurred. |
| Instance name | The name of the instance where the parameter modification occurred. |
| Parameter name | The name of the modified parameter. |
| Original value | The value of the parameter before the modification. |
| New value | The value of the parameter after the modification. |
| Creation time | The time when the parameter was modified. |

**RDS API call logs**

This tab records all call requests initiated through the RDS API, including the API name, access IP address, request content, and response results. It helps you identify API call exceptions.

**Filter conditions**

| Filter | Description |
|---|---|

| Instance name | Search by the name of the associated instance. |
|---|---|
| Interface name | Search by the API name. |
| Access IP | Search by the IP address that initiated the request. |
| Access User | Search by the username of the access user. |
| Start time | Filter by the request start time. The default value is the last 3 hours. |
| End time | Filter by the request end time. The default value is the current time. |

**API call log list**

| Field | Description |
|---|---|
| Log ID | The unique ID of the log record. |
| Interface name | The name of the called API. |
| Access IP | The IP address that initiated the request. |
| Instance name | The name of the associated database instance. |
| Time consumption (ms) | The response latency of the API call, in milliseconds. |
| Request content | The content of the API request. |
| Response result | The result returned by the API. |
| AccessId | The access ID. |
| Request time | The time when the request was initiated. |
| Response time | The time when the result was returned. |

**API call logs**

This tab records the details of internal API calls on the platform, including the request URL, request parameters, response result, and latency. It helps you identify internal API call issues.

**API call log list**

| Field | Description |
|---|---|
| Log ID | The unique ID of the log record. |
| Interface name | The name of the called service API. |
| Request ID | The unique ID of the request. |
| Request URL | The complete URL of the API request. |
| Request parameters | The parameters included in the API request. |
| Response result | The result returned by the API. |
| Time consumption (ms) | The response latency of the API call, in milliseconds. |
| Type | The type of the API call. |
| Creator | The user who initiated the call. |
| Creation time | The time when the call occurred. |
| Remarks | The remarks for the call. |

**HA switch log**

This tab records the details of HA switchovers, including the IP addresses before and after the switchover, virtual IP address (VIP), DNS, and switchover time. It helps you analyze the causes and impacts of HA switchover.

**HA switchover log list**

| Field | Description |
|---|---|
| IP1 | The IP address of the primary node before the switchover. |

| IP2 | The IP address of the primary node after the switchover. |
|---|---|
| Port | The port number of the instance. |
| VIP | The VIP. The system displays "-" if this value is unavailable. |
| VPORT | The virtual port number. |
| DNS | The domain name resolution address. The system displays "-" if this value is unavailable. |
| Cluster name | The name of the cluster to which the instance belongs. |
| Library type | The type of the database engine. |
| Switching time | The time when the HA switchover occurred. |

**General O&M audit logs**

This tab tracks the call statistics of various O&M operations on the platform, including the number of calls, successes, failures, and the success rate. It helps you understand the execution results and release status of O&M operations.

**Filter conditions**

| Filter | Description |
|---|---|
| Database type | Filter by database engine type. |
| Operation Name | Search by O&M operation name. |
| Api parameter name | Search by API parameter name. |
| Publishing status | Filter by release status. You can select multiple options. |

**Audit log list**

| Field | Description |
|---|---|
| Database type | The database engine type associated with the operation. |

| Operation Name | The name of the O&M operation. |
|---|---|
| Api parameter name | The API parameter name corresponding to the operation. |
| Publishing status | The release status of the operation, displayed with a colored dot. |
| Number of calls | The total number of times the operation was called. |
| Number of successful calls | The number of successful calls. |
| Call failures | The number of failed calls. |
| Success Rate | The percentage of successful calls out of the total number of calls. |

> **Note:** Operations with a success rate below 100% may experience exceptions. We recommend that you check other logs for further troubleshooting.

**Custom template execution records**

This tab displays the execution history and statistics of custom SQL templates, including the number of executions, successful executions, failed executions, and success rate. You can view the detailed record of each execution.

**Template execution statistics list**

| Field | Description |
|---|---|
| ID | The unique ID of the template. |
| Template name | The custom template name. |
| Template content | The SQL content that the template contains. |
| Number of executions | The total number of times the template was executed, including successful and failed executions. |
| Number of successful executions | The number of successful template executions. |

| Number of execution failures | The number of failed template executions. |
|---|---|
| Success Rate | The percentage of successful executions out of the total number of executions. |
| Operation | The available operations, such as viewing execution records. |

**View execution records**

1. On the **Custom template execution records** tab, find the template that you want to
manage.
2. In the Operation column, click **Execution record**.
3. In the panel that appears, view the detailed execution records of the template. The records
include the following fields:

| Field | Description |
|---|---|
| ID | The unique ID of the execution record. |
| Execution content | The SQL content that was actually executed. |
| Operation object ID | The ID of the target object for the operation. |
| Operation object | The type of the target object for the operation. |
| Execution result | The execution result, which indicates success or failure. |
| Execution time | The time when the execution occurred. |
| Time consumption (ms) | The execution duration, in milliseconds. |
| Executor | The username of the user who performed the operation. |

### 2.9 Disaster recovery management

**management**

#### 2.9.1 Disaster recovery switchover

This topic describes how to perform a disaster recovery (DR) switchover. The DR switchover page displays DR instance information by data center. You can use filter conditions to view the instance status and create DR switchover, DR downgrade, and real-time refresh tasks.

**View the DR instance list**

View DR instance information by data center to assess DR switchover readiness. 1.
2. On the **Disaster recovery switchover** page, set filter conditions in the filter area and
view the DR instance list. The top of the page displays statistics: N instances in total, with 145 instances that meet the conditions, 115 instances that can be switched, and 0 instances that can be downgraded.

| Filter condition | Description |
|---|---|
| Data Center | Required. Select the target data center from the drop-down list. The system automatically selects the first data center as the default value. |
| Display | Choose to display all instances or only unavailable instances. |
| Engine | Select a database engine type from the drop-down list. Options in the drop-down list change based on the selected data center. |
| Switchable | Filter instances that can or cannot be switched. Options include Unlimited, Switchable, and Not switchable. |
| Degraded | Filter instances that can be downgraded. Options include Unlimited and Degraded. |
| Name Matching | Enter an instance name for fuzzy matching. |
| Standby latency ≤ | Enter a value in seconds to filter instances whose secondary database latency does not exceed the specified value. |

3. View the instance list, which includes the following fields:

| Field | Description |
|---|---|
| Instance ID | The unique ID of the DR instance. |
| Available instances | The availability check result of the instance. OK indicates available, and FA indicates unavailable. |

| Switchable | Indicates whether the instance can be switched. OK indicates switchable, and FA indicates non-switchable. Move the pointer over the field to view the reason why the instance is non-switchable. |
|---|---|
| ALB Main | The name of the current primary data center for ALB. |
| Name | The instance name. You can click the name to go to the instance details page. |
| Link | The instance link type. |
| Engine | The type and version of the database engine. |
| Zone | The zone type. Multi indicates multi-zone, and Single indicates single zone. |
| Master Library Information | The detailed information of the primary database. Click to view the JSON details. |
| Backup database information | The detailed information of the secondary database. Click to view the JSON details. |
| Other information | Other related information. Click to view the JSON details. |
| DNS verification | The DNS verification result. OK indicates passed, and FA indicates failed. |
| ALB verification | The ALB verification result. OK indicates passed, and FA indicates failed. |
| Proxy verification | The proxy verification result. OK indicates passed, and FA indicates failed. |
| Other checks | The verification results of other check items. OK indicates passed, and FA indicates failed. |
| Instance verification | The instance verification result. OK indicates passed, and FA indicates failed. |
| Maximum standby latency | The maximum synchronization delay of the secondary database, in seconds. N/A indicates not applicable. |
| Evaluation results | The comprehensive evaluation result. OK indicates that the operation is available, and FA indicates that the operation is unavailable. Move the pointer over the field to view the reason. |

| Update information | The update time and the source IP address of the update. |
|---|---|

**Create a DR switchover task**

Perform a primary/secondary switchover on eligible DR instances.

> **Important:** The switchover button is available only when switchable instances exist.

1. On the **Disaster recovery switchover** page, check the number of switchable instances in
the statistics.
2. Click **Switch** in the top-left corner.
3. In the confirmation dialog box, view the instance statistics of the current data center.
4. Select a switchover mode:

| Switchover mode | Description |
|---|---|
| Normal switching | The system performs a forced switchover on all unavailable instances and a normal switchover on available instances. |
| Force switch | The system performs a forced switchover on all instances regardless of their availability check results. |

5. Click **Normal switching** or **Force switch** to perform the switchover.

**Create a DR downgrade task**

Downgrade eligible DR instances from multi-zone to single zone.

> **Important:** The downgrade button is available only when the page contains instances that can be downgraded.

1. On the **Disaster recovery switchover** page, check the number of instances that can be
downgraded in the statistics.
2. Click **Downgrade** in the top-left corner.
3. In the confirmation dialog box, view the instance statistics of the current data center.
4. Click **OK** to confirm the downgrade operation.

**Create a real-time refresh task**

You can create a real-time refresh task to increase the frequency of instance information collection within a specified duration and obtain the latest DR status.
1. On the **Disaster recovery switchover** page, click **Real-time refresh** in the top-left
corner.
2. In the dialog box that appears:
If no refresh task is in progress in the current data center, select a refresh duration (5 minutes, 10 minutes, 20 minutes, 30 minutes, or 60 minutes) and then click **OK**. If a pending real-time refresh task already exists in the current data center, the system prompts that a pending task exists and does not allow you to create a new task. If a real-time refresh task is running in the current data center, the system displays the end time of the current refresh task and does not allow you to create a new task.

> **Note:** During real-time refresh, the inspection prioritizes collecting DR data for the data center and collects instance information more frequently.

#### 2.9.2 Disaster recovery tasks

This topic describes how to view and manage disaster recovery (DR) tasks. The DR task page displays the history of all DR switchovers, degradation, and real-time refresh tasks, and allows you to view task details, task parameters, and execution logs.

**View the DR task list**

View the history of all DR tasks.
1. In the left-side navigation pane, click **Disaster recovery task**.
2. View the DR task list. The list contains the following fields:

| Field | Description |
|---|---|
| Task ID | The unique ID of the task. You can click the task ID to view the task details. |
| Task type | The task type. Valid values: Real-time refresh, Switchover, and Zone alignment. |
| Start time | The time when the task started. |
| End time | The time when the task ended. |
| Data Center | The target data center of the task operation. |
| Task parameters | The task parameters. You can click View to view the detailed parameters of the task. |
| Status | The execution status of the task. Valid values: Pending, Running, Succeeded, Failed, and Canceled. |
| Prompt information | The prompt information generated during task execution. |

| Creation time | The time when the task was created. |
|---|---|
| Modificatio n time | The time when the task was last modified. |
| Operation IP | The IP address from which the task was created. |
| Operation | The available operation. Click View details to view the complete details of the task. |

**Task status description**

| Status | Description |
|---|---|
| Pending | The system created the task, and it is waiting for execution. |
| Running | The system is executing the task. |
| Succeeded | The system completed the task successfully. |
| Failed | The task failed. |
| Canceled | The user canceled the task. |

**View task parameters**

View the detailed parameters of the DR task.
1. In the DR task list, find the target task and click **View** in the **Task parameters** column.
2. In the dialog box that appears, view the detailed parameters of the task in JSON format.

**View task details**

View the complete details of a DR task, including data statistics, basic information, task parameters, and task logs. In the DR task list, find the target task and click the job ID or **View details** in the Action column. In the drawer panel that appears, view the following information:

**Data statistics**

| Field | Description |
|---|---|
| Not started | The number of instances that have not started execution. |
| Running | The number of instances that are currently running. |
| Succeeded | The number of instances that completed successfully. |
| Failed | The number of instances that failed. |
| Total | The total number of instances involved in the task. |

**Basic information**: includes the job ID, task type, task start time, task end time, data
center, status, information, creation time, modification time, and operation IP address.
**Task parameters**: displays the complete parameter information of the task in JSON
format.
**Task logs**: displays the detailed logs during task execution. You can click **Refresh** in the
upper-right corner to obtain the latest logs.

### 2.10 HA management

#### 2.10.1 HA management overview

This topic describes the HA management feature of ApsaraDB O&M System Smart Pro Edition. The HA management feature uses the robot automatic recovery mechanism to automatically detect and handle common HA exceptions for database instances, which reduces manual intervention and improves system availability and stability.

**Feature overview**

The core of HA management is the robot management system. The robot is an automated exception handling engine that automatically detects, evaluates, and fixes common exceptions of database instances. The robot management page includes the following five subpages:

| Subpage | Feature |
|---|---|
| Robot processing logs | View all records of tasks executed by the robot. |
| Robot switch control | Control whether to enable or disable the robot. |
| Robot Repair statistics | Track the success rate and coverage of robot recovery. |

| Robot processing blacklist | Manage instances or scenarios that do not require automatic processing by the robot. |
|---|---|
| Robot Task Management | View and manage tasks generated by the robot. |

#### 2.10.2 Robot management

##### 2.10.2.1 Robot processing logs

The robot processing logs page records the execution history of tasks automatically processed by the robot. It helps you understand the robot running status and processing results.

**Filter conditions**

You can select the following filter conditions at the top of the page:

| Filter | Description |
|---|---|
| Task type | Filter by robot task type. |
| Processing result | Filter by processing result. Valid values: Start processing, Processing successfully, Processing failed, Automatic Repair, Reject processing, and Unable to process. |
| Target name | Search by target instance or hostname. |
| Time | Filter by processing time range. |

**Processing log list**

The processing log list displays all robot processing records and includes the following fields:

| Field | Description |
|---|---|
| Task type | The name of the exception type that the robot processes. |
| Target name | The name of the instance or host that the robot processes. |
| Processing result | The processing result status, displayed with a colored dot. |
| Processing time | The time when the robot performs the processing. |

| Procedure details | The access to the processing details. Click Detailed steps in this column to view the detailed steps of the processing record. |
|---|---|

**Processing results**

| Result | Color | Description |
|---|---|---|
| Start processing | Defaul t | The robot starts processing the exception. |
| Processing successfully | Green | The robot successfully resolved the exception. |
| Processing failed | Red | The robot failed to process the exception. |
| Automatic Repair | Defaul t | The robot resolved the exception through the automatic repair mechanism. |
| Reject processing | Defaul t | The robot rejected the exception processing. |
| Unable to process | Defaul t | The robot cannot process this exception type. |

**View processing details**

1.
2. In the robot processing log list, find the record that you want to manage.
3. In the **Procedure details** column, click **Detailed steps**.
4. In the panel that appears, view the detailed step records of the robot processing, including
the task type, target name, processing content, and processing time.

##### 2.10.2.2 Robot switch control

The robot switch control page allows you to manage the start and stop of various robot automated tasks. You can enable or disable specific types of automated tasks based on O&M requirements.

**Task type list**

The robot switch control page displays all configurable robot task types in a table. The table contains the following fields:

| Field | Description |
|---|---|

| Task type | The type of the exception automatically handled by the robot. |
|---|---|
| Task Status | The task status (Enabled or Closed, displayed as a colored tag). |
| Task Description | The feature description of the task type. |
| Recently modified | The operator who last modified the task status. |
| Modification time | The time when the status was last modified. |
| Operation | The available operations (enable or disable). |

**Task status description**

| Status | Color | Description |
|---|---|---|
| Enabled | Green | The robot is automatically detecting and handling exceptions of this type. |
| Closed | Red | The robot does not automatically handle exceptions of this type. |

**Enable or disable a task**

1. In the robot switch control list, find the task type that you want to manage.
2. In the Operation column, click **Enable** (when the status is Closed) or **Disable** (when the
status is Enabled).
3. Click OK in the confirmation dialog box.

> **Important:** After you disable a task type, the robot no longer automatically handles exceptions of that type, and manual intervention is required. Evaluate the impact scope before you disable a task type.

##### 2.10.2.3 Robot repair statistics

The Robot Repair statistics page analyzes the repair effectiveness of robots within a specified time range and helps users evaluate the operational efficiency and repair success rate of robots.

**Filter condition**

| Filter | Description |
|---|---|
| Time | Select the time range for statistics. The time range can be specified with second-level precision. |

**Statistical table**

The statistical table displays repair data by task type and includes the following fields.

| Field | Description |
|---|---|
| Task type | The name of the exception type that robots process. |
| Success | The number of successful processing attempts. |
| Failed | The number of failed processing attempts. |
| Reject | The number of rejected processing attempts. |
| Automatic Recovery | The number of automatic recovery attempts. |
| Total number of times | The total number of processing attempts for the task type. |
| Repair rate | The percentage of successful attempts out of the total number of attempts. |

**Problem instance and host analysis**

Below the statistical table, the system displays rankings of problem hosts and problem instances for each task type, including: Problem hosts: The system displays the hosts that robots process most frequently and the corresponding processing counts. Problem instances: The system displays the instances that robots process most frequently and the corresponding processing counts.

> **Note:** The repair rate is a key metric for measuring the repair effectiveness of robots. Task types with low repair rates may require manual intervention to optimize processing policies.

**View repair statistics details**

1.
2. Go to the **Robot Repair statistics** page to view the details of the target task.

##### 2.10.2.4 Robot processing blacklist

The robot processing blacklist page allows you to manage instances or hosts that you do not want the robot to process automatically. Robot does not automatically process targets on the blacklist within the specified time range.

> **Note:** The blacklist applies only to exceptions of the MySQL SQL threads, I/O threads, latency, and instance unavailability types. When you select a host, the robot filters all instances on that host. When you select a user instance, the robot filters only that instance.

**Blacklists**

All configured blacklist records are displayed in a table. The table contains the following fields:

| Field | Description |
|---|---|
| Target type | The target type of the blacklist. Valid values: User instance and Host. |
| Target name | The name of the blocked instance or the IP address of the blocked host. |
| Alert or not | Specifies whether the system generates alerts during the blocking period. Valid values: No alarm and Alert. |
| Start time | The time when the blacklist takes effect. |
| End time | The time when the blacklist becomes invalid. |
| Creation time | The time when the system created the blacklist record. |
| Operation | The available operation (Delete). |

**Add a blacklist**

1. On the blacklist page, click **Add blacklist**.
2. In the dialog box that appears, configure the following parameters:

| Parameter | Description |
|---|---|
| Target type | The target type. Valid values: User instance and Host. |

| Target name | The target name. For a host, enter the host IP address. For an instance, enter the instance name. |
|---|---|
| Alert or not | Specifies whether the system generates alerts during the blocking period. Valid values: No alarm and Alert. |
| Start time | The time when the blacklist takes effect. |
| End time | The time when the blacklist becomes invalid. |

3. Click **OK** to complete the creation.

**Delete a blacklist**

1. On the blacklist page, find the record that you want to manage.
2. In the Operation column, click **Delete**.
3. In the confirmation dialog box, click **OK**.

> **Important:** After you delete the blacklist, the robot resumes automatic processing of the target.

##### 2.10.2.5 Robot task management

The robot task management page displays task records in the robot task pool, including the task origin, type, processing result, and O&M time.

**Filter conditions**

The top of the page provides the following filter conditions:

| Filter | Description |
|---|---|
| Task source | Filter tasks by source (slave sql, slave io, slave alive, or slave lag). _ _ _ _ |
| Processing result | Filter tasks by processing result (Not started, Started successfully, Ended successfully, Failed, or Closed). |
| Time | Filter tasks by time range. |

**Task list**

The Robot task list displays all tasks in the task pool in a table. The table contains the following fields:

| Field | Description |
|---|---|

| Task source | The task source. |
|---|---|
| Task type | The type of the task processed by the robot. |
| Target name | The name of the instance or host that the task processes. |
| Processing result | The processing result of the task (Not started, Started successfully, Ended successfully, Failed, or Closed). |
| O & M start time | The time when the O&M operation starts. |
| O & M end time | The time when the O&M operation ends. |
| Creation time | The time when the task was created. |
| Procedure details | The detailed steps of the task processed by the robot. Click the value to view details. |

**Processing result descriptions**

| Result | Description |
|---|---|
| Not started | The task has not started. |
| Started successfully | The task has started. |
| Ended successfully | The task is complete. |
| Failed | The task failed. |
| Closed | The task is closed. |

**View processing details**

1.
2. Click Robot Task Management and find the task that you want to manage.
3. In the **Procedure details** column, click **Detailed steps**.
4. In the panel that appears, view the detailed step records of the task processed by the
robot, including the task type, target name, processing content, and processing time.

### 2.11 System management

#### 2.11.1 System management overview

The system management page is the global configuration center of ApsaraDB O&M System Smart Pro Edition. It provides platform administrators with centralized management of core configuration items such as database parameter templates, tag systems, custom script templates, whitelists, and scheduled tasks.

**Feature overview**

The system management page allows you to perform the following tasks: Parameter and configuration management: Maintain system parameters and performance configurations to ensure standardization of instance types and parameters. Tag and template management: Manage the tag system across instances, hosts, and clusters, and configure custom SQL templates and whitelist/blacklist rules. Security and access control: Manage region-level IP address whitelists and control host blocking policies for migration. Task management: Configure general O&M operations for instances and manage scheduled tasks.

**Sub-feature navigation**

| Sub-feature | Description |
|---|---|
| System Settings | Configure global system parameters. |
| Tag list | Manage the platform tag system. |
| Custom template | Manage custom SQL script templates. |
| Whitelist management | Manage region-level IP address whitelists. |
| Migration host blocking | Configure host blocking policies for migration. |
| General instance O&M Management | Configure general O&M operations for instances. |
| Scheduled task management | Manage scheduled tasks. |

#### 2.11.2 System settings

The system settings feature allow you to manage core configuration parameters at the platform level across four feature tabs: Database parameter Template, System parameter configuration, Component exception level configuration, and Exception type configuration. These configuration items define the parameter control scope and anomaly detection strategies that the platform applies to database instances.

**Access method**

1.
2. At the top of the page, select the feature tab that you want to manage.

**Database parameter template**

This tab allows you to manage configuration parameter templates for database engines, including which parameters are visible to users, whether users can modify them, and whether a restart is required for changes to take effect.

**Parameter description**

| Parameter | Description |
|---|---|
| Parameter name | The name of the database engine configuration parameter. |
| Database | The database type to which the parameter belongs. |
| Default value | The default value of the parameter. |
| Restart the database | Indicates whether a restart is required for parameter changes to take effect. |
| Visible | Controls whether the parameter appears on the user-side parameter configuration page. |
| Modifiable | Controls whether users can modify the parameter. |
| Unit | The unit of the parameter. |

**Create a parameter template**

1. On the Database parameter Template tab, click **Create a parameter Template**.
2. In the dialog box that appears, enter the parameter name, database type, database
version, default value, and other information.
3. Configure parameter such as Visible and Modifiable as needed.
4. Click **OK** to complete the creation.

**Edit a parameter template**

1. In the parameter template list, find the parameter that you want to manage and click
**Modify** in the Operation column.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **OK** to save the changes.

**Delete a parameter template**

1. In the parameter template list, find the parameter that you want to manage and click
**Delete** in the Operation column.
2. In the confirmation dialog box, click **OK** to complete the deletion.

**System parameter configuration**

This tab allows you to manage platform-level key-value configuration resources, including properties such as the resource key, actual value, and display value.

**Parameter description**

| Parameter | Description |
|---|---|
| Resource KEY | The unique ID of the system resource. |
| True Value | The value that the system actually uses for the resource. |
| Display value | The value displayed on the user interface. |
| Sort | The sequence number for displaying the resource. |
| Remarks | Additional description of the resource. |

**Operation instructions**

Create: Click **Create** in the top-left corner, enter information such as the resource key, true value, and display value, and then click OK. Modify: Click **Modify** in the Operation column, modify the fields, and then save the changes. Delete: Click **Delete** in the Operation column, and confirm the deletion of the resource.

**Component exception level configuration**

This tab allows you to manage the severity level policies for various component exceptions on the platform and controls the severity levels of exceptions and alert trigger thresholds.

**Exception levels**

| Level | Description |
|---|---|
| Critical | Exceptions that require immediate operations and may affect business continuity. |
| Warning | Exceptions that require attention but are not urgent and may escalate into critical issues. |

| Ignored | Known exceptions that do not require operations. |
|---|---|

**Alert trigger threshold**

You can configure alert trigger thresholds for different exception levels. The system triggers an alert only when the number of consecutive exception occurrences reaches the configured threshold: Critical-alert initiation: Controls the alert trigger threshold for critical exceptions. Warning-alarm start times: Controls the alert trigger threshold for warning-level exceptions. Negligible-alarm start times: Controls the alert trigger threshold for ignorable exceptions.

**Modify exception levels**

1. In the exception level configuration list, find the exception type that you want to manage
and click **Modify level**.
2. In the dialog box that appears, select a new exception level (Serious, Warning, or
Negligible).
3. Click **OK** to save the changes.

**Modify alert trigger thresholds**

1. In the upper-left corner of the **Component exception level configuration** page, click
**Modify the number of alert starts at the exception level** .
2. Modify the parameters and click **OK** to submit the changes.

**Exception type configuration**

This tab allows you to manage the definition of anomaly detection rules, including parameters such as the exception name, operation object type, exception level, and alert time.

**Parameter description**

| Parameter | Description |
|---|---|
| Exception name | The name of the anomaly detection rule. |
| Operation object type | The target object type for anomaly detection, such as customer instances, host instances, or petadata instances. |
| Exception level | The severity level of the exception (Critical, Warning, or Ignored). |
| Comment | The supplementary description of the exception type. |
| Alert Threshold | The number of consecutive exception occurrences that triggers an alert. |
| Alert start time | The start time of the alert. |

| Alarm end time | The end time of the alert. |
|---|---|

**Create an exception type configuration**

1. On the Exception type configuration tab, click **Create**.
2. In the dialog box that appears, enter the exception name, select the operation object type,
and configure the exception level and alert parameters.
3. Configure the alert threshold and alert time as needed.
4. Click **OK** to complete the creation.

**Modify an exception type configuration**

1. In the exception type configuration list, find the configuration that you want to manage and
click **Modify** in the Operation column.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **OK** to save the changes.

**Delete an exception type configuration**

1. In the exception type configuration list, find the configuration that you want to manage and
click **Delete** in the Operation column.
2. In the confirmation dialog box, click **OK** to complete the deletion.

#### 2.11.3 Tag list

The tag list feature allows you to manage tag definitions across three dimensions in the platform: instances, hosts, and clusters. As key metadata in O&M workflows, tags serve as matching conditions for instance filtering, resource grouping, permission control, and automated O&M policies.

**Access method**

1.
2. In the left-side navigation pane, click **Tag list**.

**Tag range**

The following three tag ranges are supported:

| Tag type | Identifie r | Description |
|---|---|---|
| Customer instance | CUSTINS | These tags apply to customer instances for instance grouping and filtering. |
| Host | HOST | These tags apply to physical machines and virtual machines for host resource management. |
| Cluster | CLUSTER | These tags apply to clusters for resource identification at the cluster level. |

**Parameters**

| Parameter | Description |
|---|---|
| Label range | The entity type to which the tag applies (CUSTINS, HOST, or CLUSTER). |
| Label type | The name of the tag for internal system use. |
| Label alias | The name of the tag for display on the interface. |
| Default value | The default value of the tag. |
| Value range | The allowed value range for the tag. |
| Value description | The supplementary description of the value range. |
| Have expired attributes or not | Indicates whether the tag supports expiration time settings (with or without expiration attributes). |

**Add a tag**

1. On the Tag list page, click **Add Tags**.
2. In the dialog box that appears, enter the following information:
**Label range**: The entity type to which the tag applies (CUSTINS, HOST, or CLUSTER).
**Label type**: The name of the tag for internal system use.
**Label alias**: The name of the tag for display on the interface.
**Value range**: The allowed value range for the tag (optional).
**Default value**: The default value of the tag (optional).
**Value description**: The supplementary description of the value range (optional).
**Have expired attributes or not**: Indicates whether the tag supports the configuration
of expiration time.
3. Click **OK** to complete the creation.

**Edit a tag**

1. Find the tag that you want to manage in the tag list and click **Edit**.
2. In the dialog box that appears, modify the fields that you want to change.

> **Note:** For system data tags, some fields (Label range, Label type, Label alias, and Value description) are read-only and cannot be modified.

3. Click **OK** to save the changes.

**Precautions**

The core fields of built-in system tags (system data tags) are read-only. You can only modify non-core fields such as the default value, value range, and expiration attributes. Before you delete a tag, verify that no O&M workflows reference the tag. Otherwise, the related workflows may encounter exceptions. Use meaningful English identifiers to name label types to facilitate references in automated scripts and workflows.

#### 2.11.4 Custom template

The custom template page allows you to manage database SQL execution templates and related security rules. The page includes three tabs: Template list, Blacklist management, and Execution rule management. You can use custom templates to standardize common SQL operations and use blacklists and execution rules to control the security boundaries of SQL execution.

**Access mode**

1.
2. In the left-side navigation pane, click **Custom template**.
3. At the top of the page, select the tab you need.

**Template list**

This tab allows you to manage the definitions of SQL execution templates. Each template includes attributes such as SQL content, protocol type, database engine, and risk assessment.

**Template fields**

| Field | Description |
|---|---|
| Template name | The SQL template name. |
| SQL content | The SQL statement that the template executes. |
| Template description | The supplementary description of the template purpose. |
| Protocol type | The protocol type for SQL execution. |
| Database engine | The database engine that the template applies to. |
| Write permission | Specifies whether the template requires write permission. |
| Cost risk | The risk assessment of the impact on costs when the system executes this template. |

| Stability risk | The risk assessment of the impact on system stability when the system executes this template. |
|---|---|
| Sensitivity risk | The risk assessment of the impact on data sensitivity when the system executes this template. |
| Read-only risk | The risk assessment of whether executing this template involves read-only operations. |
| Number of executions | The total number of times the system has executed the template. |
| Successful execution count | The total number of times the system has successfully executed the template. |
| Failed execution count | The total number of times the system has failed to execute the template. |
| Founder | The user who created the template. |
| Creation time | The time when the user created the template. |
| Modifier | The user who last modified the template. |
| Last modified time | The time when the user last modified the template. |

**Add a template**

1. On the Template list tab, click **Add Template**.
2. In the dialog box that appears, configure the template name, SQL content, and template
description.
3. Click **OK** to complete the creation.

**Edit a template**

1. Find the template that you want to edit and click **Edit**.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **OK** to save the changes.

**Delete a template**

1. Find the template that you want to delelte and click **Delete**.
2. In the confirmation dialog box, click **OK** to complete the deletion.

**Blacklist management**

This tab allows you to maintain blacklist rules for SQL template execution and use regular expressions to match SQL patterns that are prohibited from execution.

**Blacklist fields**

| Field | Description |
|---|---|
| Database type | The database type to which the blacklist rule applies. |
| Execution agreement | The protocol type to which the blacklist rule applies. |
| Regular expression | The regular expression that matches SQL content. |
| Remarks | The supplementary description of the blacklist rule. |
| Founder | The user who created the blacklist rule. |
| Creation time | The time when the user created the blacklist rule. |
| Modifier | The user who last modified the blacklist rule. |
| Last modified time | The time when the user last modified the blacklist rule. |

**Add a blacklist rule**

1. On the Blacklist management tab, click **Add blacklist**.
2. In the dialog box that appears, select the database type and protocol type.
3. Enter the regular expression that matches SQL content.
4. Enter remarks (optional).
5. Click **OK** to complete the creation.

**Edit a blacklist rule**

1. Find the blacklist rule that you want to edit and click **Edit**.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **OK** to save the changes.

**Delete a blacklist rule**

1. Find the blacklist rule that you want to delete and click **Delete**.
2. In the confirmation dialog box, click **OK** to complete the deletion.

**Execution rule management**

This tab allows you to configure execution rules for specific SQL templates and use regular expressions to control the execution behavior of templates under specific conditions.

**Execution rule fields**

| Field | Description |
|---|---|
| Template name | The name of the associated SQL template. |
| Rule type | The type of the execution rule. |
| Regular expression | The regular expression that matches execution conditions. |
| Founder | The user who created the execution rule. |
| Creation time | The time when the user created the execution rule. |
| Modifier | The user who last modified the execution rule. |
| Last modified time | The time when the user last modified the execution rule. |

**Add an execution rule**

1. On the Template list tab, click
**> Execution rules** in the Operation column.
2. Click **Add execution rules**.
3. In the dialog box that appears, configure the rule type and regular expression.
4. Click **OK** to complete the creation.

**Edit an execution rule**

1. Find the execution rule that you want to edit and click **Edit**.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **OK** to save the changes.

**Delete an execution rule**

1. Find the execution rule that you want to delete and click **Delete**.
2. In the confirmation dialog box, click **OK** to complete the deletion.

#### 2.11.5 Whitelist management

The whitelist management feature allows you to manage the IP addresses that are allowed to access a database instance. You can view and refresh whitelists by region, database engine, and machine type, and manage cluster-level whitelist groups. The whitelist defines which IP addresses can access a database instance and serves as a critical component of database access control.

**Access method**

1.
2. In the left-side navigation pane, click **Whitelist management**.

**Whitelist**

The whitelist list displays information by region, database type, and machine type.

**Parameters**

| Parameter | Description |
|---|---|
| Region | The region to which the whitelist belongs. |
| DB type | The type of the database associated with the whitelist. |
| Machine type | The host type (physical machine or ECS). |
| Cluster list | The cluster names. |

**Filter whitelists**

You can filter whitelists by the following conditions: Region: Enter a region name. DB type: Select a database type from the drop-down list. Machine type: Select physical machine or ECS. Cluster: Enter a cluster name.

**View whitelists for the classic network**

View the whitelist information for the classic network in a specified region.
1. In the whitelist list, find the record that you want to view and click **classic whitelist**.
2. In the dialog box that appears, you can view all effective whitelists for the classic network
in the current region in the **Final whitelist** section.
3. Close the dialog box after you finish viewing.

**View whitelists for VPC**

View the whitelist information for virtual private cloud (VPC) in a specified region.
1. In the whitelist list, find the record that you want to view and click **vpc whitelist**.
2. In the dialog box that appears, you can view all all effective whitelists for VPC in the current
region in the **Final whitelist** section.
3. Close the dialog box after you finish viewing.

**Refresh whitelists to instances**

Refresh the whitelist configurations for a specified region, database type, and machine type to all associated instances.

> **Warning:** This operation refreshes the whitelist to all instances within the specified scope. Confirm the scope of impact before you proceed.

1. In the whitelist list, find the record that you want to manage and click **Refresh to**
**instance**.
2. In the confirmation dialog box, view the scope of impact (region, database type, and
machine type).
3. After you confirm the information, click **OK** to submit the refresh operation.
4. The system refreshes the whitelist asynchronously. After you submit the refresh operation,
you can verify whether the configuration takes effect on the instances.

**Cluster whitelist management**

This feature allows you to view and manage whitelist groups at the cluster level.
1. In the whitelist list, find the record that you want to manage and click **Cluster whitelist**.
2. In the slide-out panel that appears, view the whitelist configurations of each cluster in the
region.
3. In the panel, you can perform the following operations:
View the effective whitelist of a cluster. View user-defined whitelist groups. Create a whitelist group. Refresh a whitelist group to a specified cluster instance.
4. Close the slide-out panel after you complete the operations.

**Precautions**

The system performs whitelist refresh operations asynchronously. After you submit the refresh operation, it takes some time for the changes to take effect on all instances. The refresh-to-instance operation affects all instances within the specified scope. You should perform this operation during off-peak periods. Cluster whitelist management supports fine-grained configuration for individual clusters. You can use cluster-level management to minimize the scope of impact. The classic network and VPC whitelists operate independently and do not affect each other.

#### 2.11.6 Host blocking during migration

The host blocking during migration feature allows you to manage the list of host IP addresses to block during migration. The system excludes hosts on the blocklist from instance migration allocation.

**Blocklist**

| Field | Description |
|---|---|
| IP | The IP address of the blocked host. |

| Add time | The time when the blocking record was added. |
|---|---|
| Remarks | The reason for blocking. |
| Add person | The user who added the blocking record. |
| Operation | The Delete button. |

**Add a host IP address**

1. On the Migration host blocking page, click **Add host IP**.
2. In the dialog box that appears, configure the following parameters:

| Config uratio n Item | Required | Description |
|---|---|---|
| IP list | Yes | The IP addresses of the hosts to be blocked. Enter one IP address per line. |
| Remar ks | No | The reason for blocking. |

3. Click **OK**.

**Delete a blocked IP address**

1. In the blocklist, find the record that you want to manage.
2. In the Operation column, click **Delete**.
3. In the confirmation dialog box, click **OK**.

> **Important:** After you delete a blocking record, the blocked host will be allowed to participate in migration allocation.

#### 2.11.7 General instance O&M management

The general instance O&M management page allows you to configure and manage general O&M operations at the instance level, including operation definitions, parameter configuration, release status, and risk assessment. On this page, you can standardize common O&M operations into configurable operation items that can be called and executed by the instance details page.

**Access method**

1.
2. Click **General instance O & M Management** in the left-side navigation pane.

**Operation item fields**

| Field | Description |
|---|---|
| Database type | The database type to which the operation item applies. |
| Operation Name | The O&M operation name. |
| Api parameter name | The name of the backend API that corresponds to the operation item. |
| Publishing status | The release status of the operation item. Valid values: Beta, Official Version, and Expired. |
| Cost | The impact of the operation on costs. Valid values: Cost increase, Cost unchanged, and Cost reduction. |
| Risk level | The risk level assessment of the operation. |
| Risk description | The detailed description of the risk level. |
| Creation time | The time when the operation item was created. |
| Modification time | The time when the operation item was last modified. |

**Publishing statuses**

| Status | Description |
|---|---|
| Beta | The operation item is in the testing phase and is for verification only. It may be unstable. |
| Official Version | The operation item has been officially released and is available for production environments. |
| Expired | The operation item has expired and is not recommended. |

**Add an operation configuration**

1. On the general instance O&M management page, click **Add configuration**.
2. In the dialog box that appears, specify the following information:
**Database type**: The database type to which the operation item applies.
**Operation Name**: The O&M operation name.
**Api parameter name**: The name of the corresponding backend API.
**Publishing status**: The release status. Valid values: Beta, Official Version, and Expired.
**Cost**: The impact on costs.
**Risk level**: The risk level.
**Risk description**: The detailed description of the risk level.
3. Click **Submit** to complete the creation.

**Edit an operation configuration**

1. In the operation configuration list, find the configuration that you want to edit and click
**Edit**.
2. In the dialog box that appears, modify the fields that you want to change.
3. Click **Submit** to save the changes.

**Copy an operation configuration**

1. In the operation configuration list, find the configuration that you want to copy and click
**Copy**.
2. The system creates a replica based on this configuration, and you can modify the replica as
needed.
3. After you complete the modifications, click **Submit** to save the changes.

**Delete an operation configuration**

1. In the operation configuration list, find the configuration that you want to delete and click
**Delete**.
2. In the confirmation dialog box, click **OK** to complete the deletion.

**Parameter management**

Each operation configuration supports a parameter list. The list defines the parameters to pass when the operation runs.

**Parameter fields**

| Field | Description |
|---|---|
| Parameter code | The unique ID of the parameter. |
| Api parameter name | The name of the parameter in the API call. |
| Parameter display name | The display name of the parameter. |
| Parameter type | The data type of the parameter. |
| Options | The available values for the parameter. |
| Default value | The default value of the parameter. |

| Required | Specifies whether the parameter is required. |
|---|---|
| Whether to disable | Specifies whether the parameter is disabled. |
| Check regular | The validation rule for the parameter value. |
| Prompt information | The input prompt message for the parameter. |

**Add a parameter**

1. On the general instance O&M management page, click **Add configuration**.
2. In the dialog box that appears, click **Add parameters**.
3. Specify the API parameter name, parameter display name, and other information.
4. Select the parameter type and configure properties such as whether the parameter is
required or disabled.
5. Click **OK** to add the parameter.

#### 2.11.8 Scheduled task management

The scheduled task management feature allows you to manage scheduled tasks in the platform. On this page, you can create, edit, start, stop, and manage scheduled tasks, view their scheduling history and execution results, and preview the trigger times of Cron expressions.

**Access method**

1.
2. Click **Scheduled task management** in the left-side navigation pane.

**Parameters**

| Parameter | Description |
|---|---|
| Task name | The name of the scheduled task. |
| Cron expression | The scheduling frequency expression of the task. |
| Scheduling status | The scheduling status of the task. |
| Business running status | The business running status of the task. |
| Effective time | The start time for scheduling the task. |

| Expiration Time | The end time for scheduling the task. |
|---|---|
| Task Description | Additional information about the task. |

**Scheduling status**

| Status | Description |
|---|---|
| Normal Scheduling | The task is scheduled and executed properly according to the Cron expression. |
| Closed | A user manually closed the task, and the system no longer schedules it. |
| Error | An error occurred during the scheduling of the task. |
| Invalid | The task is invalid and no longer takes effect. |
| Not effective | The system does not schedule the task because it has not reached its effective time. |

**Business running status**

| Status | Description |
|---|---|
| Normal running | The task executes its business logic properly. |
| Abnormal running | The task encounters an error during the running of its business logic. |
| Skip Running | The task skips the current execution because it does not meet the conditions. |

**Create a scheduled task**

1. On the **Scheduled task management** page, click **Add**.
2. Enter the required information in the dialog box.
3. Click **OK** to complete the creation.

> **Note:** The system validates the Cron expression format and supports six fields (second, minute, hour, day, month, week) or seven fields (second, minute, hour, day, month, week, year).

**Edit a scheduled job**

1. Find the task that you want to manage in the scheduled task list and click **Edit** in the
Operation column.
2. Modify the fields that you want to change in the dialog box.
3. Click **OK** to save the changes.

**Enable or disable a scheduled job**

1. Find the task that you want to manage in the scheduled task list.
2. Click **Enable** or **Close** to change the scheduling status of the task.
3. Click **OK** in the confirmation dialog box to complete the operation.

**Delete a scheduled job**

1. Find the task that you want to manage in the scheduled task list and click **Delete** in the
Operation column.
2. Click **OK** in the confirmation dialog box to complete the deletion.

**View task details**

1. Find the task that you want to manage in the scheduled task list and click **Details** in the
Operation column.
2. View the detailed information of the task in the slide-out panel, including:
Basic task information, such as the task name, Cron expression, and execution method. Scheduling status and business running status. Task messages (scheduling result information) and business messages (business execution result information). Start time and end time.

**Filter tasks**

You can filter tasks by using the following conditions: Task name: Enter a keyword of the task name to filter tasks. Scheduling status: Select a scheduling status to filter tasks. Business running status: Select a business running status to filter tasks.

**Precautions**

A Cron expression must conform to the standard format (six or seven fields). We recommend that you use the trigger time preview feature to verify the expression before you create a task. If you disable a task, the execution of the task will be skipped, but the task configuration will not be deleted. You can re-enable the task at any time. Deleting a task is an irreversible operation. Confirm the action before you proceed. Available task execution methods are subject to the execution methods that have been registered in the background. To add a new method, contact Alibaba Cloud technical support.

### 2.12 Intelligent O&M

#### 2.12.1 Intelligent host diagnostics

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

> **Note:** The following cases are for reference only. We recommend that you handle the issues based on the actual situations.

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

#### 2.12.2 One-click information collection

The one-click information collection feature in ApsaraDB One-Stop O&M Platform for Database Autonomy Service (DAS) Enterprise Edition lets you trigger diagnostic tasks using a task ID, instance ID, keyword, or custom DAG template. The system then automatically aggregates service logs and generates diagnostic reports.

**Use cases**

Troubleshoot task exceptions: When a task fails, use a task ID or keyword to trigger end-toend log collection. Offline analysis: Export encrypted log packages and replay them in a non-production environment. This helps development or L2 support teams conduct in-depth troubleshooting. Unified diagnostic portal: Collect, view, and analyze information on a single platform without switching between different tools. Customized diagnosis: For failures that are not covered by built-in scenarios, import a DAG template from Tongquetai to perform custom troubleshooting.

**Notes**

Uploaded log packages must adhere to internal format specifications, including specific path structures and metadata. Otherwise, the system cannot parse them. Tongquetai is an internal centralized testing platform accessible only to personnel with L2 or higher permissions. It is not deployed in customer on-premises environments. DAG templates must be obtained from official Tongquetai release channels to ensure security and compatibility. Imported template names must be unique. If you re-import a template with an existing name, the system updates its version number and execution time and does not create a new entry.

**Recommendations**

For on-site issues, first analyze the problem in the console by clicking **View Details**. Reserve the log download and import features for cross-environment collaboration, long-term archiving, or in-depth debugging.

**Supported collection types**

Collection by instance ID or task ID: Only RDS MySQL instances are supported. Collection by keyword: This method supports the pre-configured Service Rule (SR) log types available in the console. Currently, you can select scenarios for RDS MySQL, DTS, and PolarDB-X. Collection by extended scenario (DAG template): Import standardized DAG packages to implement custom, multi-step automated diagnostic workflows for non-standard troubleshooting scenarios.

**Method 1: Task ID diagnosis**

This method is ideal when you know the ID of a task, such as a failed migration task.
1. **Go to the one-click information collection page**
i. Log on to ApsaraDB One-Stop O&M Platform for Database Autonomy Service (DAS) Enterprise Edition. ii. In the left-side navigation pane, choose **Intelligent O&M > one-click information**
**collection**.
2. **Start a diagnosis**
For Parameter Type, select **DTS task ID**, enter the **Parameter Value**, and then click **Start**
**Diagnosis**.
The system automatically aggregates the scheduling, execution, monitoring, and error logs for the task.
3. **View diagnostic logs**
After the diagnosis is complete, click **View Details** in the Actions column. On the task details page, click **View Details** again to view the logs.
4. **Download the log package**
In the Actions column, click **Download Logs** to download the compressed log package for the task.
5. **Decrypt the logs**
After you download the logs, go to the Tongquetai platform. On the **Diagnosis Plan** page, click **Log Parsing** in the upper-right corner to decrypt the logs.

**Method 2: Keyword diagnosis**

This method is useful when you do not have the task ID but can search using a related keyword.
1. **Go to the one-click information collection page**
i. Log on to ApsaraDB One-Stop O&M Platform for Database Autonomy Service (DAS) Enterprise Edition. ii. In the left-side navigation pane, choose **Intelligent O&M > one-click information**
**collection**.
2. **Start a diagnosis**
For Parameter Type, select **Keyword** and enter the Parameter Value. For Scenario Name, select **dts**, and then click **Start Diagnosis**.
3. **View diagnostic logs**
After the diagnosis is complete, click **View Details** in the Actions column. On the task details page, click **View Details** again to view the logs.
4. **Download the log package**
In the Actions column, click **Download Logs** to download the compressed log package for the task.
5. **Decrypt the logs**
After you download the logs, go to the Tongquetai platform. On the **Diagnosis Plan** page, click **Log Parsing** in the upper-right corner to decrypt the logs.

**Method 3: DAG template diagnosis**

Use this method for complex diagnostic scenarios that require a custom workflow.
1. **Download a DAG template from Tongquetai**
i. Log on to Tongquetai and go to the **Diagnosis Center > Diagnosis Plan** page. ii. In the upper-right corner of the page, click **Download**. iii. In the dialog box that appears, select a **Site Name**, select the checkbox for the target template, and then click **Download** to get the DAG package in `.zip` format.
2. **Import the DAG template into the DAS Enterprise Edition console**
i. Log on to ApsaraDB One-Stop O&M Platform for Database Autonomy Service (DAS) Enterprise Edition. ii. In the left-side navigation pane, choose **Intelligent O&M > one-click information**
**collection**.
iii. In the upper-right corner of the page, click **Import DAG**. iv. Select the downloaded `.zip` file and confirm the import. After a successful import, the template appears in the **Select Template** drop-down list for subsequent use.
3. **Start an extended scenario diagnosis**
i. From the **Collection Scenario** drop-down list, select Extended Scenario. From the
**Select Template** drop-down list, select the template that you just imported.
ii. Click **Start Diagnosis**. The system automatically runs the diagnostic steps in the order defined by the DAG nodes, such as `check_lock_status` and `get_host_ins_list` . The real-time execution status of each node is displayed in the list.
4. **View the diagnostic results**
In the Actions column for the task, click **View Details** to go to the **One-click Information**
**Collection Task Details** page.
The tree structure on the left displays all diagnostic nodes and their statuses: green for success and red for failure. The pane on the right displays the detailed output log for the selected node, such as

```
 instance is not locked .
```

You can expand or collapse nodes, search for a node by name, and switch between different nodes to view their logs.

**Offline log import and analysis**

On the **one-click information collection** page, click **Import and View** to upload a compliant log package ( `.zip` ).The system then parses the logs for offline replay and analysis. For instructions on how to download logs, see Step 4 in Method 1 or Method 2.

#### 2.12.3 Automated script management

ApsaraDB Unified O&M Platform Dukang Smart Edition provides full-lifecycle automated script management. The platform features rigorously validated, built-in O&M scripts that automate complex, high-frequency operations (such as instance status correction, backup task intervention, and resource cleanup) and also supports importing standardized script packages from the Tongquetai O&M support platform to address emergency needs for specific scenarios or new failure patterns. With built-in risk levels, strict approval mechanisms, and comprehensive version change auditing, the platform significantly reduces manual operation time and the risk of human error, enhancing the efficiency, flexibility, and security of database O&M.

**Before you begin**

**Risk notice**: The automated scripts described in this topic modify underlying metadata
and control logic. If you cannot accurately assess the impact of an operation on your business, do not execute the script. You must submit a ticket to Alibaba Cloud technical support for evaluation and assistance.
**Approval mechanism**: All script execution tasks follow an "approve first, execute later"
security principle. After a task is initiated, a platform O&M administrator must approve it before it can run. Unapproved tasks will not be executed. Low-risk scripts: After approval, the system automatically triggers execution. Medium- and high-risk scripts: After approval, the task status changes to "To be confirmed". The initiator must then manually confirm the execution to start the task. Without this confirmation, the task remains in a waiting state.

**Use cases**

**Fix abnormal states**: Resolve instance status issues caused by missing underlying
engines, task interruptions, or metadata inconsistencies, such as a ServiceTest process that fails to finalize or residual test instances.
**Handle emergency failures**: Address instances that cannot be restarted normally, or a
backup task is stuck in the Check state and conventional methods are ineffective.
**Manage resource usage**: Clean up expired data in bulk when OSS backup storage or
instance local disks reach high usage levels due to an accumulation of historical data or logs.
**Unblock stalled processes**: Bypass non-critical check steps during disaster recovery
upgrades or special change scenarios to advance the overall process.

**Benefits**

**Flexible and extensible sources** : In addition to using built-in scripts, you can download
and import the latest DAG templates from Tongquetai to quickly adapt to new O&M scenarios.
**Streamlined workflow with visible risk** : Use validated, built-in scripts to handle
complex underlying logic with a single click. The risk level (Low, Medium, or High) and impact scope are clearly displayed before execution to help you make an informed decision.
**Standardized approval workflow**: An integrated, strict approval mechanism
automatically generates and sends an approval link to authorized personnel. The task is executed automatically after approval, ensuring all operations are compliant and traceable.
**End-to-end transparent monitoring**: Provides real-time task status tracking, detailed
execution log downloads, and task interruption capabilities, offering full transparency into the operation process.
**Reduced human error**: Using parameterized configurations instead of manual command-
line operations significantly reduces production incidents caused by human error.

**Script sources and categories**

Scripts are categorized by source and distinguished by different labels. You can view the source in the **Source** column on the **script list** page.
**Built-in scripts**: Standard O&M scripts pre-installed on the platform. The source is labeled
as "Built-in".
**Imported scripts**: Script packages that you download from Tongquetai and import. The
source is marked with a purple "Imported" label, and the specific "Import Time" is recorded.

**Supported built-in automated scripts**

**Script overview**

| Script | Description | Risk level | Supported databases |
|---|---|---|---|
| Hack ServiceTest# to finalize state | Forcibly terminates the ServiceTest inspection process to move an instance to its "final state". Use this script to resolve upgrade blockages caused by environmental discrepancies. | Low risk | RDS MySQL PolarDB for MySQL High- Availability Edition Tair (compatible with Redis) MongoDB |
| Correct task interruptions and status for MySQL test instances | Cleans up residual MySQL test instances and related task flows from interrupted tasks, releasing resources and restoring state consistency. | Low risk | RDS MySQL PolarDB for MySQL High- Availability Edition |

| Forcibly cancel a backup task for a MySQL instance | Forcibly cleans up abnormal task records when a backup task is stuck in the Check state and cannot be canceled manually. | Low risk | RDS MySQL PolarDB for MySQL High- Availability Edition |
|---|---|---|---|
| Forcibly restart a MySQL instance | Forcibly restarts an instance by using low- level commands when the instance is in an abnormal state and fails to restart from the console. This script is not supported for TDE-enabled instances. | Medium risk | RDS MySQL PolarDB for MySQL High- Availability Edition |
| Clean up expired backup sets or log data in OSS | Performs a bulk cleanup of expired full or incremental backup files from an OSS bucket based on the retention policy to free up storage space. | Medium risk | RDS MySQL PolarDB for MySQL High- Availability Edition Tair (compatible with Redis) |
| Resolve issues with incremental log upload and cleanup for MySQL | Corrects abnormal status records in the archivelog list table of the bak _ metadata database. This resolves log accumulation issues caused by failed uploads or local cleanup failures of incremental logs. | Low risk | RDS MySQL PolarDB for MySQL High- Availability Edition |

**Hack ServiceTest# to finalize state**

This script forces the ServiceTest# process to a "final state" for special requirements, such as urgent environment upgrades, single-datacenter disaster recovery upgrades, or at a customer's request.

> **Note:** ServiceTest performs periodic, automated health checks across the full instance lifecycle, covering key scenarios such as instance creation, account management, backup execution, and instance termination. This mechanism proactively detects and precisely captures environment-level API exceptions or functional failures, providing real-time monitoring to ensure platform stability. Forcibly terminating the process stops these health checks.
> Stopping ServiceTest affects only the platform's internal self-check logic and does not interfere with the normal operation of business instances. It poses no direct risk to the production environment.

**Typical scenarios**

Troubleshooting shows that the corresponding engine cluster is not deployed, which prevents the ServiceTest process from finalizing naturally. In a disaster recovery environment where only Datacenter A is upgraded but Datacenter B is not, the ServiceTest process must be finalized to avoid blocking the overall upgrade. The customer explicitly requests to skip the testing phase.
1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**db_type**: Enter the database type. Valid values: `mysql` , `polaro` , `redis` , and
`mongo` .
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**Fix task and status for MySQL test instances**

Test instances are typically deleted automatically after they are created. However, if a task is interrupted, it may not delete the test instance, requiring manual intervention.

> **Note:** Cleaning up residual test tasks does not affect the cloud platform.

1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**custins_id**: Enter the instance ID.
**task_id**: Enter the ID of the interrupted task. You can obtain the ID from the task details
page in **Task Management**.
**pengine_id**: Enter the Pengine ID. You can obtain the ID from the task details page in
**Task Management**.
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**Force-cancel MySQL backup tasks**

This script is intended for emergency use in backup failure scenarios only. If an instance backup is stuck in the `check` state and cannot be canceled manually, use this script to forcibly clear the abnormal task record.

> **Note:** This script is a corrective action to mitigate backup risks and is safe to use.

1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**custins_id**: Enter the instance ID.
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**Forcibly restart a MySQL instance**

When a MySQL instance is in an abnormal state and cannot be restarted from the console (for example, if the console returns an error like `The process doesn't have the permission to` `invoke the program. Please contact with RDS operator` ), you can use this script to force a restart.

> **Important:** Business impact: A forced restart causes the instance to be unavailable during the restart. Before you perform this operation, you must communicate with business stakeholders and execute it during off-peak hours.
> Limitation: This method is not supported for instances that have Transparent Data Encryption (TDE) enabled.

1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**custins_id**: Enter the instance ID.
**hostins_id**: Enter the host instance ID. You can obtain the ID from the **Basic**
**Information** page of the instance details.
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**Clean up expired data in OSS**

If an analysis of OSS usage reveals that the `rds-backup` bucket contains many expired backup files (full or incremental), you must clean them up. Otherwise, OSS storage usage will continue to increase and may cause new backup tasks to fail.

> **Important:** Business impact: The cleanup operation targets only expired historical data and does not affect running business instances.
> Risk warning: Accidentally deleting valid backup files causes data loss and prevents point-in-time recovery (PITR). Before execution, you must carefully verify the list of files to be deleted and the time range.

1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**remain_days**: The retention period in days. Data older than this value is deleted.
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**Fix MySQL incremental log issues**

> **Note:** This script corrects only control-plane metadata logic and does not affect the normal use of business instances.

**Typical scenarios**

Abnormal OSS usage: Monitoring shows that the `rds-backup` storage space is heavily occupied, and the data volume continues to increase without periodic decreases. This indicates that incremental logs are not being successfully archived to OSS. Local disk accumulation: A failed cleanup mechanism causes an instance's local binlog or other incremental logs to accumulate, which triggers high disk usage alarms for the instance.
1. Log on to ApsaraDB Unified O&M Platform Dukang Smart Edition.
2. In the left-side navigation pane, click **Intelligent O&M > Automated Script**
**Management**.
3. In the **Actions** column of the script, click **Execute**.
4. In the panel that appears, carefully review the script details (such as description, affected
entities, risk level, and risk warnings). In the **Parameter Settings** section, configure the following parameters:
**custins_id**: Enter the instance ID.
**hostins_id**: Enter the host instance ID. You can enter up to two IDs, separated by a
comma (,). You can obtain the ID from the **Basic Information** page of the instance details.
**Execution reason**: Enter the reason for execution to facilitate approval review.
5. Click **Confirm Execution**.

**General operations**

**Import a script**

If a built-in script does not meet your needs, import a standardized script package from Tongquetai.
1. Download the script package:
i. Log in to the O&M support platform (Tongquetai), go to the scenario-based O&M or related template center, and click **Download** in the upper-right corner of the page. ii. In the dialog box that appears, select a **Site Name**, select the required DAG templates, and click **Download** to get the script package as a `.zip` file.
2. Import the script:
i. In the navigation pane on the left of Dukang Intelligent Edition, click **Intelligent O&M >**
**Automated Script Management**.
ii. On the **Script List** page, click **Import Script** in the upper-left corner. iii. Select the downloaded `.zip` package and click **OK**.
3. Confirm the result:
After the import is successful, the new script appears in the list. The **Source** column displays a purple **Imported** label, and the current **Import Time** is recorded.

> Note on version updates: If a new version of a script is available on Tongquetai, download the latest package and repeat the import process. The system identifies the script as an update, refreshes the **Import Time**, and upgrades the **Version Number**. No duplicate entry is created.

**View script details and version information**

In the **Actions** column for a script, click **Script Details**. In the panel that appears, you can view the full script description, affected entities, number of executions, number of successful executions, risk level, and detailed risk warnings.
**Version number management**: The details page displays the current version number of the
script, such as V1.0.4. For an imported script, if you update it from Tongquetai and re-import it, this version number is also updated. This helps you track script iterations.

**View script execution records**

You can query historical tasks from two locations: the details page of a single script or the complete list of all scripts. Both locations provide a unified view of approval progress, execution status, and detailed process logs. From the details page of any entry point, you can get the following information:

| Execution record details | Description |
|---|---|
| Approval informatio n | The page redirects to the process approval page in the O&M Change Console. On this page, you can approve, reject, or forward the approval task. |
| Execution informatio n | Click Execution Information to view details such as the execution status, reason for execution, execution result, and the script's start and end times. |
| Execution process | The system redirects to the Tongquetai platform, which shows more granular, real-time execution logs and process tracking. |

**Method 1: View execution records for a single script**

In the **Actions** column for the target script, click **Execution Record**. In the panel that appears, you can query the approval progress, execution status, and detailed process logs for historical tasks.

**Method 2: View execution records for all scripts**

In the navigation pane on the left, go to the **Intelligent O&M > Automated Script**
**Management > Execution Record** tab. On this page, you can query the approval
progress, execution status, and detailed process logs for all historical script tasks.

**Download script execution logs**

In the **Actions** column for a script, click **Execution Record**. In the panel that appears, click
**Download Log** to get the complete execution log file for the current task.

**Disable a script**

To temporarily disable a script, click **Disable** in the **Actions** column for the script, and then click **OK**.

**Terminate a script execution**

> **Note:** Only tasks with a status of **Pending Approval** can be terminated. Tasks that have already succeeded or failed cannot be terminated.

In the **Actions** column for the script, click **Execution Record**. In the panel that appears, click
**> Terminate**.

### 2.13 Database agent O&M

The database agent is a core component used for intelligent database O&M in ApsaraDB O&M System Smart Pro Edition. It receives natural language instructions and automatically performs O&M tasks such as database diagnosis, inspection, and troubleshooting.

#### 2.13.1 Overview of database agent O&M

ApsaraDB O&M System Smart Pro Edition provides database agent O&M management capabilities for centralized management and O&M of database agents across all products. This topic describes how to view agent running status, manage agent instances, maintain agent configurations, perform observability diagnostics, and manage knowledge bases.

**Feature overview**

The database agent O&M module provides the following core features:

| Feature | Description |
|---|---|
| Agent overview | View the running status and resource usage of all agent instances. |
| Agent management | Start, stop, configure, and update versions of agent instances. |
| Observable diagnosis | Perform observability diagnostics on agent operations, including metric overview, session history, and tracing analysis. |
| Knowledge base management | Manage the O&M knowledge bases that agents use, and create, read, update, and delete knowledge entries. |

#### 2.13.2 Agent overview

The agent overview page serves as the global entry for database agent O&M and provides a centralized view of all agents running on the platform. This page helps you quickly understand the overall agent scale, daily call volume, success rate, token consumption, and the real-time running status of each agent.

**Page description**

The agent overview page consists of three sections from top to bottom:

**Metric cards**

The top of the page displays four metric cards that present key data for agent O&M:

| Metric | Description |
|---|---|
| Total number of agents | The total number of agents registered on the platform. |
| Number of calls today | The total number of calls made by all agents today, along with the growth rate compared to yesterday. |
| Average success rate | The average success rate of calls made by all agents today, along with the growth rate compared to yesterday. |
| Token consumption today | The total number of tokens consumed by all agents today, which is the sum of input and output tokens. |

The growth rate labels on the metric cards display changes in green for increases or red for decreases. This helps you quickly identify abnormal fluctuations.

**Chart section**

The middle of the page is a chart section, which displays two charts side by side:

**Overview of agent status (donut chart)**

A donut chart displays the distribution of all agents across different statuses, including Normal operation, Alert, Error, and Offline. The right side of the donut chart shows the legend and the specific number of agents in each status. This chart helps you determine whether any agents on the platform are experiencing issues.

**Call trend in recent 7 days (line chart)**

A line chart displays the daily trends in total calls and successful calls over the last 7 days. The horizontal axis represents the date, and the vertical axis represents the number of calls. This chart helps you observe periodic fluctuations and overall trends in agent calls.

**Status of each agent today**

The bottom of the page displays the real-time status of each agent in cards, with six agents per page. Each card contains the following information: Agent name: the agent name. Number of instances: the number of instances registered under the agent. Status tag: a colored dot and text that indicate the current status of the agent. The card background color is consistent with the agent status: green indicates normal operation, yellow indicates alert, red indicates error, and gray indicates offline. You can click the page number or next-page icon at the bottom to browse all agents.

**Procedure**

**View the agent overview**

1.
2. The page displays the agent overview by default, including metric cards, the status
distribution chart, the call trend chart, and agent status cards.

**View agent statuses**

1. View the agent status cards in the **Status of each agent today** section.
2. To view more agents, click a page number or the next-page icon at the bottom to switch
pages.

**Data description**

The data displayed in the **Number of calls today** and **Average success rate** metric cards are based on statistics from 00:00 to the current time of the day. The "Compared with yesterday" label compares the data with the same time period yesterday. In the chart of call trend over the last 7 days, if no call data exists for a particular day, the data for that date will be set to zero to ensure a continuous and complete horizontal axis.

#### 2.13.3 Agent management

The agent management page allows you to view and manage all registered agents on the platform. The list displays the basic information and running status of each agent. You can go to the agent details page to view the instance list and running metrics, and go to the configuration management page to maintain the prompt, model, tool execution confirmation configuration, and custom parameters for each agent.

**Agent list**

**List description**

The information about all agents are displayed in a table. The table includes the following columns:

| Column | Description |
|---|---|
| Agent ID | The unique ID of the agent. You can click the ID to go to the agent details page. |
| Name | The agent name. |
| Engine type | The engine type that the agent uses. |
| Status | The current running status of the agent. The system uses a status tag to indicate the status. |

| Number of instances | The number of instances registered under the agent. |
|---|---|
| Recent heartbeat | The relative time of the most recent heartbeat from the agent. |
| Operation | The available operations, including Instance information and Configuration Management. |

**Filter agents**

1.
2. On the agent management list page, you can click **Advanced Filter** and select a status
(Normal, Alert, Error, or Offline) to filter the agents by status, or leave the field empty to view all agents.

**Agent details**

**Access the agent details page**

1.
2. On the agent management list page, click the ID in the **Agent ID** column, or click **Instance**
**information** in the **Operation** column.
3. The agent details page appears, which displays the list of instances under the agent.

**Instance list**

The instance list displays information about all registered instances under the agent. The list includes the following columns:

| Column | Description |
|---|---|
| Instance ID | The unique ID of the instance. You can click the ID to view the instance details. |
| Status | The current running status of the instance. The system uses a status tag to indicate the status. |
| Deployment Type | The deployment method of the instance. |
| IP | The IP address of the instance. |
| CPU | The current CPU utilization of the instance. |
| Memory | The current memory usage and total memory of the instance. |

| Runtime | The duration for which the instance has been running. |
|---|---|
| Recent heartbeat | The relative time of the most recent heartbeat from the instance. |
| Operation | The View details button. |

**Filter instances**

On the instance list page, you can click **Advanced Filter** and select a status (Running, Alert, Error, Stopped, or Lost contact) to filter the instances by status, or leave the field empty to view all instances.

**View instance details**

1. In the instance list, click the ID in the **Instance ID** column, or click **View details** in the
**Operation** column.
2. An instance details panel appears on the right side of the page and displays the following
information:
**Basic information**: Displays the status, deployment type, instance IP, host IP, region,
zone, namespace, runtime, heartbeat interval, model, configuration version, start time, and recent heartbeat of the instance.
**Resource metrics (current snapshot)**: Displays the current key resource metrics of
the instance in cards, including CPU utilization, memory usage, disk utilization, GC pause time, JVM heap memory usage, and number of threads.
**Event Log**: Displays the event records of the instance in a table, including event time,
event type, and details. Event types include:

| Event type | Description |
|---|---|
| Register | The instance is registered and goes online. |
| Offline | The instance goes offline. |
| Mark loss | The system marks the instance as disconnected. |
| Restore | The instance recovers from the disconnected state. |
| Archive | The system archives the instance. |

**Configuration management**

The configuration management page allows you to maintain the runtime configuration of agents. From the left-side submenu of this page, you can access the following four configuration modules: Prompt configuration: Allows you to manage agent prompt templates and supports version management and rollback. Model configuration: Allows you to configure the large language model for the agent. Tool execution confirmation configuration: Allows you to manage the execution confirmation policies for tool calls. Custom parameters: Allows you to manage custom runtime parameters for agents.

**Access the configuration management page**

1.
2. In the agent management list, click **Configuration Management** in the **Operation**
column.
3. The configuration management page appears and displays the prompt configuration page
by default. You can switch between different configuration modules in the left-side submenu.

**Prompt configuration**

The prompt configuration page allows you to manage various prompt templates for agents. The prompt list displays information about all prompts under an agent, including the prompt key, name, content preview, current version, last modifier, and update time. You can filter prompts by name or prompt key.

**View version history**

1. In the prompt list, click **Version history** in the **Operation** column.
2. A version history panel appears on the right side and displays all version records of the
prompt.
3. Each record includes the version number, status (Current activation or Unused), change
description, operator, creation time, and available operations.
4. Click **View content** to in the Operation column to view the complete prompt content of a
specific version.
5. For an inactive version, click **Switch to this version** to roll back to that version.

**Create a prompt version**

1. In the prompt list, click **Edit** in the **Operation** column.
2. In the dialog box that appears, edit the prompt content and change description.
3. Click **Submit** to create a new version. The system automatically activates the new version.

**Model configuration**

The model configuration page allows you to specify the large language models that agents use in different scenarios. The model list displays the configured model information under an agent, including the configuration key, model name, last modifier, and update time.

| n key examples: | main model _ |   |
|---|---|---|
| fallback model _ |   |   |
|   |   | (the fallback |

Configuration key examples: `main_model` (the main model), `summary_model` (the summary

**Edit model configuration**

1. Go to the **Model configuration** page. In the model list, click **Edit** in the **Operation**
column.
2. In the dialog box that appears, select a model name from the list of available models on the
AIBase platform.
3. Click **OK** to save the configuration.

**Tool execution confirmation configuration**

The tool execution confirmation configuration page allows you to control whether manual confirmation is required when an agent calls specific tools. This prevents automatic execution of high-risk operations. The configuration list displays the configured tool execution confirmation rules, including the tool name, tool description, confirmation requirement, confirmation reason, last modifier, and update time.

**Add a tool confirmation configuration**

1. Go to the **Tool execution confirmation configuration** page and click **Add a tool to**
**confirm the configuration**.
2. In the dialog box that appears, fill in the following information:
**Tool name**: The tool name. Example: `execute_sql` .
**Tool description**: The tool description. This field is optional.
**Need to confirm**: Indicates whether to enable or disable manual confirmation.
**Confirm cause description**: The reason for requiring confirmation.
3. Click **OK** to save the configuration.

**Enable or disable confirmation**

1. To enable confirmation, find a tool that does not require confirmation in the configuration
list and click **Enable** in the **Operation** column.
2. To disable confirmation, find a tool that requires confirmation and click **Close** in the
**Operation** column.
3. In the confirmation dialog box, click **OK** to complete the operation.

**Custom parameters**

The custom parameters page allows you to manage additional runtime parameters for agents and store them as key-value pairs. The parameter list displays the configured custom parameters, including the parameter key, parameter value, description, last modifier, and update time.

**Add a parameter**

1. Go to the **Custom parameters** page and click **Add parameters**.
2. In the dialog box that appears, fill in the following information:
**Parameter key**: The parameter key. Example: `max_retry` .
**Parameter value**: The parameter value.
**Description**: The parameter description. This field is optional.
3. Click **OK** to save the parameter.

**Edit a parameter**

1. In the parameter list, click **Edit** in the **Operation** column.
2. In the dialog box that appears, modify the parameter value and description.
3. Click **OK** to save the changes.

#### 2.13.4 Observable diagnosis

The observable diagnosis page provides multidimensional operational observability for database agents and helps you analyze their operational status and call chains across three dimensions: metric monitoring, session replay, and link traking. You can use this page to locate call exceptions, analyze performance bottlenecks, and review user sessions to quickly identify and resolve issues.

**Page description**

The observable diagnosis page provides tabs and an agent selector at the top: Tabs: The page includes three tabs: **Metrics overview**, **Session History**, and **Link**
**Tracking**.
Agent selector: Select the agent to diagnose from the drop-down list in the upper-right corner of the page. After you switch the agent, the system automatically refreshes the data on the current tab.

**Metrics overview**

The Metrics overview page uses charts to display the call metrics and performance data of the selected agent, including O&M metrics such as call volume trends, model distribution, success rate, latency distribution, and execution time distribution.

**Charts**

The Metrics overview page displays the following charts from top to bottom:

**Agent calls and token consumption**

This dual Y-axis line chart shows the daily token consumption (left axis) and number of calls (right axis) of agents over the last 7 days. X-axis: Date in MM-DD format, showing data for the last 7 days. Left Y-axis: Token consumption, displayed as an area chart. Right Y-axis: Number of calls, displayed as a line chart. Supplementary description: The upper-right corner of the chart displays the label "Changes in Token consumption and number of calls in the past 7 days". This chart helps you observe the number of calls and resource consumption trends of agents and determine whether call spikes or abnormal fluctuations occur.

**Today's model invocation distribution**

This donut chart shows the distribution of models called by agents on the current day. Sectors: Each sector represents the proportion of calls for a specific model. Legend: The bottom section displays the model names and their corresponding number of calls. This chart helps you understand the current model distribution of agents and identify the primary and abnormal models.

**Agent call success rate trend**

This line chart shows the daily call success rate and exception rate of agents over the last 7 days. X-axis: Date in MM-DD format. Y-axis: Percentage (%). Green line: Success rate. Red line: Exception rate. Metric area: The top of the chart displays the average success rate and exception rate over the last 7 days. This chart helps you monitor the call quality of agents and promptly detect decreases in the success rate or increases in the exception rate.

**Today's First Token delay distribution**

This bar chart shows the distribution for the latency of the first token returned by models during agent calls on the current day. The latency ranges include:

| Range | Description |
|---|---|
| <200ms | Less than 200 milliseconds |
| 200-500ms | 200 to 500 milliseconds |
| 500ms-1s | 500 milliseconds to 1 second |
| 1-2s | 1 to 2 seconds |
| 2-3s | 2 to 3 seconds |
| 3-5s | 3 to 5 seconds |
| >5s | More than 5 seconds |

This chart helps you evaluate the model response speed and determine whether the latency is too high.

**Today's Agent Runtime Distribution**

This bar chart shows the distribution for the end-to-end execution duration of single agent calls on the current day. The duration ranges include:

| Range | Description |
|---|---|
| <5s | Less than 5 seconds |
| 5-15s | 5 to 15 seconds |
| 15-30s | 15 to 30 seconds |
| 30s-1m | 30 seconds to 1 minute |

| 1-3m | 1 to 3 minutes |
|---|---|
| 3-5m | 3 to 5 minutes |
| >5m | More than 5 minutes |

This chart helps you understand the overall execution duration of agent calls and identify calls with excessive execution time.

**Call Distribution today**

This bar chart shows the hourly distribution for the number of model calls on the current day.
**X-axis**: Hour (from 00:00 to the current time).
**Y-axis**: The number of calls.
**Peak label**: The top of the chart displays the peak value of the day and the corresponding
hour. This chart helps you analyze the time-based distribution of agent calls and identify peak call periods.

**Procedure**

**View the metrics overview**

1.
2. In the agent selector in the upper-right corner of the **Metrics overview** page, select the
agent that you want to view.
3. The page automatically loads and displays the metric charts for the agent.

**Switch agents**

1. In the agent selector in the upper-right corner of the page, click the drop-down list.
2. Select another agent.
3. The page automatically refreshes all chart data to display the metrics of the newly selected
agent.

**Data description**

The call volume and token consumption trend chart always displays data for the past 7 days and fills missing dates with zeros. The success rate trend chart calculates the success and exception rates as a weighted average based on the daily call volume to ensure accuracy when multiple records occur on the same day. The daily call distribution chart displays only data from 00:00 on the current day to the current time and excludes future time periods. The system displays all chart data based on the UTC time to ensure consistency with backend data.

**Session history**

The Session History page displays user session records for the selected agent. You can view the basic information of each session and trace the complete message interaction process, including user queries, assistant responses, reasoning processes, tool calls, and tool results.

**Page description**

The Session History page consists of a filter section, a session list, and a session details panel.

**Filter section**

The top of the page provides two filter conditions:

| Filter | Description |
|---|---|
| User ID | Filter session records by user ID. |
| Session ID | Filter session records by session ID. |

After you enter the filter conditions, click **Search** to query the records, or click **Reset** to clear the filter conditions.

**Session list**

The session list displays session records with 10 records per page. The list includes the following columns:

| Column | Description |
|---|---|
| Session ID | The unique ID of the session. You can click it to view the session details. |
| User ID | The ID of the user who initiated the session. |
| Session Title | The title summary of the session. |
| Last update time | The time of the most recent message in the session. |

Pagination controls at the bottom of the page allow you to navigate to the previous or next page, or jump to a specific page.

**Session details**

Click a Session ID in the session list. A session details panel appears on the right side of the page and displays the complete message interaction history of the session. The system displays each message in a card based on the role (user or assistant): User message: The system displays the message in a card with a blue background and directly shows the text entered by the user. Assistant message: The system displays the message in a card with a gray background. The card contains the following types of message blocks:

| Message block type | Identifie r | Description |
|---|---|---|
| Reasoning content | Plain text | The reasoning and analysis process of the assistant. |
| Tool called |   | The name and input parameters of the tool called by the assistant. You can expand or collapse this block. |
| Tool result |   | The result returned by the tool execution. You can expand or collapse this block. |
| Metric data |   | The metric data generated during the call. You can expand or collapse this block. |

The upper-right corner of each message displays a timestamp and a trace ID (if available) to help you correlate tracing information.

**Procedure**

**View the session list**

1.
2. Click the **Session History** tab.
3. In the agent selector in the upper-right corner of the page, select the agent that you want
to view.
4. The page automatically loads the session list of the selected agent.

**Filter sessions**

1. Enter a **User ID** or **Session ID** in the filter section.
2. Click the **Search** button to refresh the list based on the filter conditions.
3. To clear the filter conditions, click **Reset**.

**View session details**

1. In the session list, click the **Session ID** of the session that you want to view.
2. A session details panel appears on the right side of the page and displays the complete
message interaction history of the session.
3. Click a message block title to expand or collapse detailed content such as tool call
parameters, tool results, and metric data.
4. After you finish viewing the details, click the close icon in the upper-right corner of the
panel to close it.

**Data description**

The system sorts the session list in descending order by last update time. The system displays messages in the session details panel in chronological order, alternating between user and assistant messages. By default, the system collapses tool call and tool result message blocks. Click a block to expand it and view the complete content. If a message contains a trace ID, you can use it to query the corresponding execution trace on the **Link Tracking** page.

**Link tracking**

The Link Tracking page allows you to query and view execution trace details for a specified trace ID. This page shows the complete execution process of a single agent call, including the type, execution time, and status of each step, to help you identify performance bottlenecks and execution exceptions.

> **Note:** The link tracking feature uses trace data from Apsara Stack Doctor (ASD). When you click the **Link Tracking** tab, the system redirects you to the trace details page in ASD.

**Page description**

**Query section**

The top of the page provides a trace ID input box and a query button. You can also press Enter after entering a trace ID in the input box to query data. Trace ID input box: Enter the trace ID that you want to query. Query button: Click this button to query trace data for the entered trace ID.

**Trace results**

After a successful query, the page displays trace execution details, including the following information:

**Trace overview**

| Item | Description |
|---|---|
| Request ID | The request ID of the trace. |
| Status | The overall execution status of the trace. Valid values: Successful, Failed, and Running. |
| Duration | The total execution time of the trace, in milliseconds. |

**Execution step timeline**

The timeline displays each execution step in the trace. Each step includes the following information:

| Item | Description |
|---|---|
| Step name | The name of the execution step. |

| Step type | The step type label, distinguished by color. |
|---|---|
| Execution status | The execution status of the step. Valid values: Successful, Failed, and Running. |
| Execution time | The execution time of the step, in milliseconds. |
| Details | The detailed description of the step, if available. |

Step types and their corresponding colors are as follows:

| Step type | Description | Color |
|---|---|---|
| LLM | The large language model call step. | Blue |
| TOOL | The tool call step. | Green |
| KNOWLEDGE | The knowledge base retrieval step. | Orange |
| OTHER | Other step types. | Gray |

**Procedure**

**Query link tracking**

1.
2. Click the **Link Tracking** tab.
3. Enter the trace ID that you want to query in the trace ID input box.
4. Click **Query** or press Enter to view the execution details of the trace.

**Analyze execution steps**

1. In the trace result area, view the trace summary information (request ID, status, and
duration).
2. View each execution step from top to bottom along the timeline:
Identify the step category based on the step type label (such as LLM call, tool call, or knowledge base retrieval). Check the status label to determine whether the step has been executed successfully. Check the duration to identify time-consuming steps and locate performance bottlenecks. Expand details to view the specific execution information for the step.

**Data notes**

If the trace ID you enter has no corresponding trace data, the page displays the following message: "No corresponding trace data found. Check whether the trace ID is correct." Link tracking supports two return formats: `steps` and `spans` . You can obtain the trace ID from the message details in the session history to facilitate correlation analysis.
```html ```

#### 2.13.5 Knowledge base management

The knowledge base management page allows you to manage the knowledge bases that database agents rely on. When an agent performs database O&M tasks, it retrieves relevant O&M knowledge, operation manuals, and best practices from these knowledge bases. On this page, you can view the knowledge base list, import new versions of knowledge base artifacts, and view and switch to previous versions.

**Page description**

The knowledge base management page displays all knowledge bases in groups. The system groups each knowledge base by its parent folder and places unassigned knowledge bases into the "Ungrouped" category. Each knowledge base appears as a card that contains the following information:

| Item | Description |
|---|---|
| Knowledge base name | The knowledge base name. |
| Code | The unique code of the knowledge base. |
| Aibase UUID | The unique ID of the knowledge base in the AIBase platform, if available. |
| Current version | The version number of the currently active knowledge base. |
| Update time | The time when the knowledge base was last updated. |
| Operation buttons | The Update and Version history buttons. |

**Procedure**

**View the knowledge base list**

1.
2. The page automatically loads and displays all knowledge bases, grouped by folder.

**Update a knowledge base**

You can upload a new knowledge base artifact package to update the knowledge base version.
1. Find the knowledge base that you want to update and click **Update**.
2. In the dialog box that appears:
**Select File**: Click **Select File** and select a knowledge base artifact package in
`.tar.gz` format. The system automatically parses the version information from the uploaded artifact package.
**Remarks** (optional): Enter version remarks to identify the changes in this version.
3. After you confirm that the information is correct, click **OK**.
4. The system starts importing the knowledge base artifact, and the action area of the card
displays the Importing status.
5. After the import completes, the system displays an "Import completed" message,
automatically refreshes the knowledge base list, and updates the current version to the new version.

> **Note:** The import process is an asynchronous operation. The system polls the import status every 3 seconds until the import completes or fails. Keep the page open to receive the import result in a timely manner.

**View previous versions**

1. Find the knowledge base that you want to view previous versions and click **Version**
**history**.
2. The dialog box that appears displays all version records of the knowledge base, including
the following columns:

| Column | Description |
|---|---|
| Version number | The version number of the knowledge base. |
| File size | The file size of the artifact package. |
| Import Status | The import status of the version. Valid values: Importing, Completed, or Failed. |
| Status | Indicates whether this version is the currently active version. |
| Remarks | The version remarks. |
| Import user | The user who performed the import operation. |
| Import time | The time when the version was imported. |
| Operation | The Switch or Retry switching button. |

3. After you finish viewing, close the dialog box.

**Switch the knowledge base version**

You can perform the following operations to switch the knowledge base to a previous version.
1. Find the knowledge base that you want to switch to a previous version amd click **Version**
**history**.
2. In the dialog box, locate the target version to which you want to switch.
3. Confirm that the version meets the following conditions:
The import status is **Completed** or **Failed**. The version is not the currently active version. The version is not in the Importing status. The artifact package is uploaded to Object Storage Service (OSS) and has an OSS URL.
4. Perform the corresponding action based on the version status:
For a completed version: Click **Switch**, and then click **OK** in the confirmation dialog box. For a failed version: Click **Retry switching**. The system re-downloads the artifact from OSS and retries the import. Click **OK** in the confirmation dialog box.
5. The system starts the version switch, and the action area displays the Importing status.
After the switch completes, the system displays a corresponding message and automatically refreshes the knowledge base list.

**Import status**

A knowledge base version has the following import statuses:

| Status | Description |
|---|---|
| Importing | The artifact package is being imported. You cannot perform a switch operation. |
| Completed | The artifact package was imported successfully. You can switch to this version. |
| Failed | The artifact package import failed. You can retry the switch operation, which re-downloads the artifact from OSS and imports it again. |

**Precautions**

Knowledge base artifact packages support only the `.tar.gz` format. The system rejects all other formats. The system automatically parses version information from the artifact package. You do not need to enter the version number manually. Import and switch operations run asynchronously. The system automatically updates the status based on the round-robin mechanism. For a failed version, the system supports re-downloading the artifact from OSS and retrying the import. You do not need to re-upload the file. Version switching affects the knowledge retrieval results of the agent. Perform switch operations during off-peak periods.

### 2.14 Package management

The package management module in ApsaraDB O&M System Smart Pro Edition allows you to manage software packages for database kernels and related components. You can use this module to view package lists, enable or disable packages, install or uninstall packages on hosts, and query package change records. This module meets O&M requirements for scenarios such as cluster scale-out, version consistency assurance, emergency fixes, and canary releases. This topic describes three core package operations in ApsaraDB O&M System Smart Pro Edition: enabling or disabling packages, installing or uninstalling packages, and querying change records.

**Usage notes**

The ApsaraDB O&M System Smart Pro Edition (the new version) does not fully support the certificate system of ApsaraDB Operations and Maintenance System (the old version). Therefore, log in to ApsaraDB Operations and Maintenance System for authentication before you access certain pages of the Smart Pro Edition.

**Supported database engines**

Currently, the system **supports only** the following types of Apsara Infrastructure Management software packages: RDS MySQL PolarDB for MySQL Primary/Standby Edition PolarDB for PostgreSQL PolarDB PostgreSQL (Oracle)

**Package list description**

The package list displays all packages and includes the following columns:

| Column | Description |
|---|---|
| Name | The package name. You can copy the name. |
| Version number | The version number of the package. |
| Release version number | The release version number of the package. |
| OS version | The OS version (alios6, alios7, or alios8). |
| Chip architecture | The chip architecture type (x86 64, aarch64, sw 64, or noarch). _ _ |
| Status | The package status. Valid values: Enable and Disable. |

| Release time | The release time of the package. |
|---|---|
| Operation | The available operations. You can enable or disable the package, manage installations, and view change records. |

**Filter packages**: The list supports the following filter conditions. You can click **Advanced**
**Filter** at the top of the package list page to filter packages:

| Filter | Type | Description |
|---|---|---|
| Name | Text input | Filter by package name. |
| Version number | Text input | Filter by version number. |
| Release version number | Text input | Filter by release version number. |
| OS version | Drop-down list | Valid values: alios6, alios7, and alios8. |
| Chip architecture | Drop-down list | Valid values: x86 64, aarch64, sw 64, and noarch. _ _ |
| Status | Drop-down list | Valid values: Enable and Disable. |

**Enable or disable packages**

1.
2. Click **Disable** or **Enable** in the **Operation** column.
Disable: You cannot install a disabled package on a host. Enable: You can install an enabled package on a host.

**Install or uninstall packages**

Install or uninstall a package on a host. The **OS version** and **chip architecture** of the host must match those of the package. Otherwise, the host does not appear on the page.

> **Important:** Uninstalling a software package is a high-risk O&M operation. If a database instance relies on dynamic libraries or binary files in the package, forced uninstallation may result in missing dependencies. Consequently, the database instance will fail to start or the service will be interrupted. Before you uninstall a software package, make sure that no important instances are running on the hosts, or that you have prepared disaster recovery and rollback plans.

> The OS version and chip architecture of the host must match those of the package. Otherwise, the host does not appear in the host list of the installation management panel.

1.
2. Click **Installtation management** in the **Operation** column.
3. In the panel that appears, select the host that you want to manage and click **Installation**
or **Uninstall**.

> **Note:** Uninstallation is a high-risk operation. You can uninstall only one package from one host at a time.

Install: Make sure that **Not installed** is displayed in the **Installation status** column of a host before you select the host. Uninstall: Make sure that **Installed** is displayed in the **Installation status** column of a host before you select the host. The installation status in the host list includes the following values:

| Status | Description |
|---|---|
| Not installed | The package is not installed on this host. You can install the package. |
| Installed | The package is installed on this host. You can uninstall the package. |
| Installing | The package is being installed. No operations are available. |
| Uninstalli ng | The package is being uninstalled. No operations are available. |

4. In the dialog box that appears, select **Operating Instructions**, enter the **Operation**
**reason**, and then click **OK**.
In the host management panel, you can monitor the progress in the installation status column of the target host: Installation: A status change from **Installing** to **Installed** indicates that the installation is complete. Uninstallation: A status change from **Uninstalling** to **Not installed** indicates that the uninstallation is complete.

**Query package change records**

You can query whether a package was successfully enabled, disabled, installed, or uninstalled to meet O&M compliance and fault review requirements. 1.
2. Click **Change record** in the **Operation** column.
The page displays information such as the operation type, operation time, and result description. You can use the filter conditions at the top, such as time range and operation type, to quickly locate records.

### 2.15 Exception management

Exception management is a module in ApsaraDB O&M System Smart Pro Edition, which allows you to monitor and handle platform O&M exceptions in a centralized manner. It helps you promptly identify and resolve various issues during platform operation.

#### 2.15.1 Exception management overview

Exception management is a module in ApsaraDB O&M System Smart Pro Editionthat allows you to monitor and handle platform O&M exceptions in a centralized manner. This module provides a global view of exception distribution and enables you to handle exceptions one by one, which helps you identify and resolve platform issues promptly.

> **Note:** Exception management does not appear in the left-side navigation pane of the platform. You can access the exception management page from the quick navigation section on the homepage.

**Feature overview**

The exception management module includes the following two subpages:

| Subpage | Description |
|---|---|
| Abnormal dashboard | Displays the global exception distribution and provides statistics by dimensions such as exception type and severity level. |
| Exception list | Provides a detailed list of exceptions and allows you to filter, handle, and close exceptions. |

#### 2.15.2 Exception dashboard

The exception dashboard is the global overview page of the exception management module. This page displays the level distribution, trend changes, target type distribution, and exception component rankings for all exceptions on the platform. You can use this page to understand the overall exception status of the platform, identify components and target types with frequent exceptions, and navigate to the exception list for detailed handling.

**Page description**

The exception dashboard page displays the following four sections from top to bottom:

**Exception level statistics**

This section displays the number of exceptions at each severity level in numeric cards, including:

| Level | Color | Description |
|---|---|---|
| Serious | Red | The number of serious exceptions. |
| Warning | Yellow | The number of warning-level exceptions. |
| Negligible | Gray | The number of ignorable exceptions. |

**Abnormal trend**

This section displays the trend of exception numbers at each severity level over the last N days in a line chart. You can switch between the last 7 days, the last 14 days, and the last 30 days to view the trend.
**Horizontal axis**: Date.
**Vertical axis**: Number of exceptions.
**Red line**: Trend of number of serious exceptions.
**Yellow line**: Trend of number of warning-level exceptions.
**Gray line**: Trend of number of ignorable exceptions.
In the time range tabs at the upper-right corner of the chart, click **Nearly 7 days**, **Last 14**
**days**, or **Last 30 days** to switch the time range of the trend data.

**Number of exceptions for each target type**

This section displays the distribution of exception numbers across target types (such as customer instances, hosts, and host instances) in a column chart.
**Horizontal axis**: Target type name.
**Vertical axis**: Number of exceptions.
The column chart sorts columns by the number of exceptions in descending order. Click a bar in the chart to navigate to the exception list page. The system automatically filters exception records by the corresponding target type.

**Exception components**

This section displays exception component rankings in a table to help you identify the components with the most frequent exceptions. The table contains the following columns:

| Column name | Description |
|---|---|
| Component name | The name of the exception component. You can click the name to navigate to the exception list filtered by this component. |
| Health Score | The health score of the component, displayed as a progress bar. |

| Number of exceptions | The total number of exceptions for this component. |
|---|---|
| Number of serious exceptions | The number of serious exceptions for this component. |

The table sorts components by health score in ascending order. The component with the lowest health score appears at the top.

**Procedure**

**View the exception dashboard**

1.
2. The **Abnormal dashboard** page is displayed by default. On this page, you can view the
exception severity statistics, trend charts, target type distribution, and exception component rankings.

**Switch the time range for the trend**

1. In the **Abnormal trend** chart section, click the time range tab in the upper-right corner.
You can select **Nearly 7 days**, **Last 14 days**, or **Last 30 days**.
2. The trend chart automatically refreshes to display data for the selected time range.

**Navigate to the exception list**

1. In the **Number of exceptions for each target type** chart, click a bar of a target type.
2. Alternatively, in the **Exception component** table, click a component name.
3. The system navigates to the exception list and automatically filters exception records by
the selected target type or component.

**Data description**

The exception level statistics is updated in real time, which reflects the current number of exceptions at each severity level. The system aggregates exception trend data by day. The number of exceptions for each day is the total number of exceptions of all severity levels for that day. The system calculates the health score in the exception component rankings based on the number and severity of exceptions. A lower score indicates poorer component health. When you navigate from the exception dashboard to the exception list, the URL parameters carry the target type and component type information. The exception list page uses this information to automatically set filter conditions.

#### 2.15.3 Exception list

The Exception list page displays all exception records that the platform detects. You can filter records by severity level, exception type, and component type, and process them individually or in batches. On this page, you can also view exception details, record the cause and solution for an exception, or process multiple exceptions of the same type in batches.

**Filter exceptions**

The top of the Exception list page provides a filter section that supports the following filter conditions:

| Filter | Type | Description |
|---|---|---|
| Severity level | Drop-down list | Filters by severity level. You can select Serious, Warning, or Negligible. The default value is Serious. |
| Exception type | Drop-down list | Filters by target type. You can select Customer instance, Host, Host instance, HA, Account permissions, Link, Scheduled service, HA PROXY, Backup, Resource delivery, or maxscale instances. The default value is Customer instance. |
| Componen t type | Drop-down list (searchable) | Filters by exception component subtype. The system dynamically loads options based on the selected exception type. |
| Display delay | Drop-down list | Controls whether delayed exceptions are displayed. You can select Delay exceptions are not displayed (value = 0) or Slow latency exceptions (value = 1). |

> **Note:** When you switch the exception type, the system automatically resets the component type filter and reloads the component list for the corresponding type. When you navigate from the Abnormal dashboard page to the Exception list page, the page automatically applies the target type and component type information in the URL.

**List description**

The Exception list displays exception records in a table. The system dynamically adjusts the columns based on the selected exception type to show the most relevant information for that type.

**Common columns**

The following columns appear for all exception types.

| Column name | Description |
|---|---|
| Processing Method | The processing method for the exception. The value is displayed as Immediate processing or Delayed processing. If the delayed processing time has expired, the system highlights the value in a warning color. |
| Severity level | The severity level of the exception. The system displays this value as a tag, including Serious, Warning, and Negligible. |
| Number of times | The number of times the exception occurred. The system highlights the value in red when the count is greater than 0. |
| Capture time | The time when the system captured the exception. |

| Update Time | The time of the most recent update to the exception record. |
|---|---|
| Check content | The name of the exception component subtype. |
| Exception information | The detailed description of the exception. |
| Operation | The entry point for processing the exception. |

**Dynamic columns**

The following columns are displayed based on the selected exception type:

| Column name | Selected exception types |
|---|---|
| Instance name | Customer instance, HA, Account permissions, Link, HA PROXY, and Backup |
| Hostname | Host and Scheduled service |
| IP | Host, Host instance, and Scheduled service |
| PORT | Host instance |
| Cluster | Host, Host instance, Link, HA PROXY, and Resource delivery |
| Data center | Host and Scheduled service. |
| Type | Scheduled service. |
| Instance type | Account permissions and Link (Exclusive or Shared). |
| Instance task | Customer instance and Host instance. This column provides a link that redirects to the instance task list. |
| View logical instance databases | Specific exception types. This column provides a link that redirects to the logical instance database page. |

> **Note:** The Instance type column displays Exclusive or Share. In the Instance task column and the View logical instance database column, you can click View to go to the corresponding details page.

**Handle exceptions**

The exception handling operation records the processing method, cause, and solution for an exception. The processing methods include immediate processing and delayed processing.

**Handle a single exception**

1.
2. In the left-side submenu, click **Exception list**.
3. Configure filter conditions such as severity level and exception type in the filter section to
locate the target exception.
4. In the exception list, find the target exception record and click **Handle exceptions** in the
**Operation** column.
5. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Processing Method | Select a processing method: Immediate processing or Delayed processing. |
| Delay Time | This parameter appears only when Processing method is set to Delayed processing. Select a specific time for delayed processing. This parameter is required. |
| Cause | Enter the cause of the exception. This parameter is optional. |
| Solution | Enter the solution for the exception. This parameter is optional. |

6. Click **OK** to submit the handling record.

**Handle exceptions in batches**

1. In the exception list, select one or more exception records for batch processing.
2. Click **Batch processing** above the list. The number of selected records is displayed in the
button.

> **Note:** If you do not select any records, the **Batch processing** button is unavailable. Please select the exception to be handled first.

3. In the dialog box that appears, configure the processing method, delay time, cause, and
solution. The procedure is the same as handling a single exception.
4. Click **OK** to submit the batch processing request.

> **Note:** Batch processing applies the same processing method and handling information to all selected exception records. After the processing succeeds, the system clears the selected records and automatically refreshes the list.

**Processing method description**

| Processing method | Description |
|---|---|
| Immediate processing | The system marks the exception for immediate processing and updates the exception status to Processing. |
| Delayed processing | The system marks the exception for delayed processing and requires you to specify a delay time. Before the delay time expires, the list displays the exception with a Delayed processing label. After the delay time expires, the system highlights the processing method in a warning color. |

**Data description**

By default, the exception list filters exception records with a severity level of Serious and an exception type of Customer instance. The Processing Method column displays Delayed processing if the exception has a delay time configured, or Immediate processing if no delay time is configured. When a delayed exception remains unhandled after its delay time expires, the system highlights the Processing Method column in a warning color (yellow) to remind you to handle the exception promptly. When you navigate from the Abnormal dashboard page to the Exception list page, the page automatically applies the targetType, targetSubtype, level, and showFilter parameters carried in the URL.

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

#### 3.3.3 General instance O&M

##### 3.3.3.1 Important Notes

**Read before operation**

> **Warning:** Some operations described in this section, such as instance restart, minor engine version update, and backup and restoration, involve core changes to the underlying infrastructure. These operations are irreversible or high-risk. Improper operations may lead to data loss, service interruption, or performance jitter.
> Before you perform any O&M operations, carefully read the relevant tutorials and the precautions and key risk reminders on the console interface. If necessary, perform operations under the guidance of Alibaba Cloud professional technicians. Once you click Submit, Confirm or similar commands, it is deemed that you have been fully aware of all potential risks and voluntarily bear all the consequences arising therefrom. Proceed with caution.

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
example to describe operations on the restart page.

> **Note:** The restart policies displayed or supported on the page vary based on the database type. For more information, see the restart policies displayed on the page.

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

##### 3.3.3.7 Manage instance parameters

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

> **Note:** You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks.
> You can customize list items. You can select the task fields that you want to view based on your needs.

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

> **Note:** Switch now: This method is used for emergency avoidance.
> Operation and maintenance time switching: This method is suitable for routine O&M windows, such as early morning every day. The O&M task is automatically executed.
> Specified time switch: This method is suitable for specific change windows, such as application release.

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

##### 3.3.3.14 Manage instance tasks

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

> **Note:** Separate keywords with spaces during queries.
> **SQL archive**:
> Export current query results or save them to a historical archive database.
> This method is suitable for regularly backing up important SQL logs for subsequent auditing or review.
> **SQL archive query**:
> Access the query interface for archived historical SQL logs.
> Search for saved SQL records across different time periods.

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

> **Note:** You can view details of tasks in various states, including all tasks, interrupted tasks, and suspended tasks.
> You can customize list items. You can select the task fields that you want to view based on your needs.

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

> **Note:** After the configured restoration time expires, the IOPS value is restored within 5 minutes.

##### 3.3.4.8 Disable backup for PolarDB-X instance

This topic describes how to disable backup for a PolarDB-X instance.

**Scenarios**

This operation is only allowed in test environments. It is designed for test instances with limited storage resources to free up storage space.

**Precautions**

It is an extremely high-risk operation to disable backups. **Do not disable backups for**
**production instances**. If you disable backups, when both the primary and secondary
nodes fail, the absence of backup data prevents recovery and causes data loss. After you disable backups, the system no longer performs any scheduled automatic backups and prohibits manual backup creation. You cannot modify any backup-related parameters while backups are disabled.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. On the **Instance management > Instance List** page, click the name of the instance.
3. In the left-side navigation pane, click **Backup policy**.
4. On the backup information page, click **Disable Backup** in the upper-left corner.
5. In the dialog box, click **Confirm** to disable backups.
To re-enable backup, click **Enable Backup**.

##### 3.3.4.9 Add proxy nodes to a Tair (Redis OSS-compatible) instance

**compatible) instance**

When business traffic increases or the load on existing proxy nodes becomes excessively high (for example, when CPU, memory, or network bandwidth reaches the threshold), you can scale out horizontally by increasing the number of Proxy nodes. This effectively distributes client request pressure, and improves overall system throughput and high availability.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. Choose **Instance management > Instance List** and click the name of the required
instance.
3. In the lower part of the Basic information page, click **Add Proxy Instance Node**.
4. In the dialog box that appears, enter the number of nodes and click **Submit**.

##### 3.3.4.10 Temporarily increase the primary/secondary synchronization buffer for a Tair (Redis OSS-compatible) instance

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

> **Note:** The scaling ratio ranges from 1.0 to 5.0.
> This operation applies to normal, db, and logic instances. When performed on a logic instance, the operation takes effect on all underlying db instances.

normal instance: Also known as a Redis-Normal instance. A standard Redis instance in single-node or primary-replica architecture. db instance: a subinstance that acts as the data node in the Redis-Logic cluster architecture. It refers to the DB-role subinstance that physically stores data in the Cluster Edition. logic instance: a Redis-Logic cluster instance that has multiple roles of Proxy, CS, and DB. It is a clustered deployment that supports read/write splitting and shard routing.

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

> **Note:** Instances that use HAProxy do not experience service interruptions only if migrated within the same cluster.
> Batch instance migration operations are not reviewed. Proceed with caution.

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

> **Important:** Instance parameter changes may cause risks such as transient connections or unavailability. You can modify the parameters by following the instructions on the console.

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
|---|---|
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
| Send SMS | Specify whether to send SMS notifications. Valid values: Yes No |
| Instance source | Specify the source of instances. Valid values: Cluster and SqlTemplate. |
| Please select a source cluster | This parameter is available only when the Instance source parameter is set to Cluster. Select a source cluster to populate the instance name. |
| SelectSqlTemplat e | This parameter is available only when the Instance source parameter is set to SqlTemplate. Select an SQL template to populate the instance name. Note You can click Create Template to the right of the parameter to create SQL templates on the SQL Template management page. |

| Input instance | Specify the instances on which the batch task runs. Enter one instance name per line. |
|---|---|
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
|---|---|
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

> **Note:** Custom SQL templates support only SELECT statements and can be used only for DBaaS databases. The creation of SQL templates requires BPMS approval. To prevent the SQL template from being accidentally executed by other members, which could result in batch tasks being sent to incorrect instances, we recommend that you provide a detailed description of the template name and the reason for its addition in the SQL template.

7. Click **Submit**.

#### 3.3.6 Manage instance plan migration

The instance plan migration list can be uploaded in two ways: batch submission by instance or by host IP address. This topic describes the detailed procedures for instance plan migration.

**Procedure**

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

This topic describes how to view host information in ApsaraDB Operations and Maintenance System.

**Procedure**

1. Log in to ApsaraDB Operations and Maintenance System.
2. In the left-side navigation pane, choose **Host management > System host**.
3. You can filter hosts by IP address or hostname.
4. Click the IP address of the host and view information on the **Host details** page. The
information includes the CPU utilization, memory usage, the number of instances, and disk usage. You can also click the options in the Host details section to view the information about host instances, performance, and accounts.

#### 3.4.4 Physical machine group

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

### 3.5 Cluster management

#### 3.5.1 Configure cluster parameters

This topic describes how to configure cluster parameters.

**Procedure**

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
|---|---|
| Set Table consistency validation percentage | Control the sampling ratio for table data consistency checks. Unit: percentage. Valid values: [0,100] . |
| Set backup set playback validation timeout | Unit: seconds. Valid values: [0,86400] . Note If the parameter is set to a non-zero value, backup set playback verification is performed during sub-instance restoration, read-only instance creation, disaster recovery instance creation, and standby database rebuild. Verification terminates upon timeout. |
| Set backup set validation percentage | Unit: percentage. Valid values: [0,100] . Note If the parameter is set to a non-zero value, the system periodically extracts the backup set proportionally to create a temporary verification sub-instance. After the verification is complete, the sub- instance is deleted immediately. |
| Set backup does not fall to the ground | All instances within the cluster will uniformly apply this backup storage policy. Supported options: Close, Only data does not fall to the ground, and Data log does not fall to the ground. |
| Set backup compression | Once enabled, all instances within the cluster will uniformly use this compression method. Supported options: no compression and zlib compression. |
| Set backup streaming recovery | Once enabled, all instances within the cluster will uniformly use this streaming recovery mode. Supported options: Close and Streaming recovery. |

| Set instance HA priority mode | Control the priority policy during the HA switchover. Supported options: Availability priority and Reliability first. Default value: Availability priority. |
|---|---|
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
| Set arch version _ | Identifies the cluster architecture version. The specific value is managed by the platform. |

| Set perf status _ | Specifies the link type for collecting performance monitoring data. Supported options: Old link, Grayscale second link, and Second level link. |
|---|---|
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

> **Note:** You can also perform cluster consistency check and subdomain consistency check on this page.

Click **Add** next to the required unit, region, or zone to add a location node, and then click
**Submit**.
Click **Parameters** next to the required unit, region, zone, or subdomain to add, modify, or delete parameters. Click **Delete** next to the required unit, region, zone, or subdomain to delete a unit, region, zone, or subdomain.

### 3.6 Task management

#### 3.6.1 Manage interrupted tasks

This topic describes how to manage interrupted tasks, including user instance tasks, host instance tasks, and host tasks. This topic uses a user instance task as an example to describe how to manage interrupted tasks.

**Procedure**

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
| Disaster recovery management | You can perform inspections on link components and control components, perform switchover, and manage disaster recovery tasks. | None. |

| Scheduled task management | You can manage the scheduled tasks in the system. | None. |
|---|---|---|

#### 3.7.2 Change the unified storage location of logs

**logs**

By default, database system logs, such as audit logs, are written to SLS-inner, which is an internal logging service, and cannot be directly accessed by users. If you have clear global log governance requirements or centralized log analysis requirements, you need to write logs to SLS-PUB, which is a public logging service that you can manage. You can perform a global switchover by enabling log storage to SLS-PUB.

**Usage notes**

> **Important:** This operation is a **one-time global configuration** and **cannot be rolled back** **after it takes effect**. After you enable log storage to SLS-PUB, **all existing and** **new instances will be affected**. This is reflected on the details page of each cloud database instance. On the SQL Audit tab of the Data Security page of a database instance, the Enable Log Storage to SLS-PUB switch is turned on by default. All subsequent logs, including audit logs, slow query logs, and error logs, will be stored in SLS-PUB by default. Exercise caution when you perform this operation.
> To meet the log visibility requirements of a single instance, perform the following operation: Log in to the Apsara Uni-manager Management Console. Go to the Instance Details page, choose Data Security > SQL Audit, and turn on the Enable Log Storage to SLS-PUB switch. You can enable this feature as needed and manage it for a single instance without affecting other instances. This way, instance management is more secure, flexible, and controllable.

**Prerequisites**

Simple Log Service (SLS) is activated. An SLS project (SLS-PUB) is created in the region where the database instance resides.

**Procedure**

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
| Message list | Displays the message list. |
| Sent message records | Displays sent message records. |

| ROBOT management | Displays ROBOT processing logs, switch controls, alert contacts, repair statistics, and more. |
|---|---|
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

> **Note:** If you want to handle multiple exceptions at the same time, you can select all the exceptions that you want to handle and click **Batch processing** in the upper-left corner of the list.

5. In the **Handling exceptions** dialog box, view the details and troubleshoot the error
accordingly.

> **Note:** If you want to handle multiple exceptions at a time, you can view the details and troubleshoot the error accordingly in the **Batch handling exceptions** dialog box.

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
ara Uni-manager Operations Con sole

## 4 Platform Operation in the Apsara Uni-manager Operations Console

**Apsara Uni-manager**

**Operations Console**

### 4.1 Turn on the IPv6 display switch for ApsaraDB for MongoDB

**switch for ApsaraDB for MongoDB**

If you want to select IPv6 when you create an ApsaraDB for MongoDB instance in an Apsara Stack environment, you must turn on the IPv6 display switch in the Apsara Uni-manager Operations Console. After you turn on the switch, the setting is synchronized to the instance creation page in the ApsaraDB for MongoDB console. Then, you can configure IPv6 when you create an ApsaraDB for MongoDB instance.

> **Important:** This operation is an account-level global setting. After the IPv6 display switch is turned on, all tenants within the current account can configure IPv6 when they create instances in the ApsaraDB for MongoDB console.

**Prerequisites**

The URL of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: ops.asconsole.intranet-domain-id.com. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

i. Open a browser. ii. In the address bar, enter the URL of the Apsara Uni-manager Operations Console and press Enter.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

ara Uni-manager Operations Con sole iii. Enter the correct username and password.

> **Note:** Obtain the username and password that are used to log in to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.
> If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account.
> The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted.
> To enhance security, make sure that your password meets the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

iv. Click **Agree to Private Policy and Log On** .
2. **Go to the ApsaraDB for MongoDB switch management page**
i. In the top navigation bar of Apsara Uni-manager Operations Console, choose **Platform**
**Operation** > **Management and Control Service O&M** > **UniConsole**.
ii. On the **Products** page, search for **mongodb** and click **Switch List** in the **Actions** column.
3. **Turn on the IPv6 display switch**
On the **mongodb Switches** page, search for `enableIPv6` and turn on the switch.

> **Note:** After the switch is turned on, all tenants within the current account can configure IPv6 when they create instances in the ApsaraDB for MongoDB console.

4. **Create an ApsaraDB for MongoDB instance and configure IPv6**
After the switch is turned on, log in to the ApsaraDB for MongoDB console, create an ApsaraDB for MongoDB instance, and configure **IP Type**. For more information, see the
**Create an instance** topic in User Guide.

## 5 Security maintenance

### 5.1 Network security maintenance

Network security maintenance is aimed at ensuring device security and network security.

**Device security**

Check network devices, and enable security management protocols and configurations of devices. Check for up-to-date versions of network device software and update the software to more secure versions in a timely manner. For more information about the security maintenance method, see the product document of each device.

**Network security**

Select the intrusion detection system (IDS) or intrusion prevention system (IPS) based on the network status to check Internet and intranet traffic and defend the network against abnormal behaviors and attacks.

### 5.2 Account password maintenance

**maintenance**

Account passwords include the ApsaraDB for MongoDB system and device passwords. To ensure account security, change the system and device passwords periodically, and use passwords that meet the complexity requirements.
