---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary/Secondary Edition) User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 373
source_pdf: "1e649a57cb95f10e_Secondary Edition) User Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E5%BA%93%20PolarDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20POLARDB%20PolarDB%20for%20PostgreSQL%20%28Primary/Secondary%20Edition%29%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for POLARDB PolarDB for PostgreSQL (Primary/Secondary Edition) User Guide 20260831

## Table of Contents

- 1 Log on to the Cloud-native Database PolarDB console
- 2 Instance types
- 3 Quick Start
  - 3.1 Limits
  - 3.2 Get started with PolarDB for PostgreSQL Primary/Secondary Edition
- 4 Instances
  - 4.1 Create an instance
  - 4.2 Restart an instance
  - 4.3 Change specifications
  - 4.4 Configure a maintenance window
  - 4.5 Primary/standby switchover
  - 4.6 Release an instance
  - 4.7 Upgrade a minor engine version
  - 4.8 Manage instances in the recycle bin
  - 4.9 Read-only instance
    - 4.9.1 Overview
    - 4.9.2 Create a read-only instance
    - 4.9.3 View details of read-only instances
  - 4.10 Modify the values of parameters for an instance
  - 4.11 Manage tags
- 5 Database connection
  - 5.1 View and manage instance endpoints and ports
  - 5.2 Connect to an instance
  - 5.3 Use DMS to log on to a PolarDB for PostgreSQL instance that uses local disks
  - 5.4 Configure the hybrid access solution
  - 5.5 Change the network type of an instance
- 6 Accounts
  - 6.1 Create an account
  - 6.2 Reset the password
  - 6.3 Delete an account
  - 6.4 Lock an account
- 7 Databases
  - 7.1 Create a database
  - 7.2 Delete a database
- 8 Monitoring
  - 8.1 View monitoring data
  - 8.2 Configure an alert rule
- 9 Cloud Monitor
  - 9.1 View performance metrics
  - 9.2 Alert history
  - 9.3 Alert rules
    - 9.3.1 Create an alert rule
    - 9.3.2 Manage alert rules
- 10 Data security
  - 10.1 Configure an IP address whitelist
  - 10.2 Configure SSL encryption
  - 10.3 Configure TDE
  - 10.4 SQL audit
- 11 Backup
  - 11.1 Back up data
  - 11.2 Download data backup files and log backup files
  - 11.3 Restore full data
  - 11.4 Restore data of databases and tables
- 12 Plug-in management
  - 12.1 Supported extensions
  - 12.2 Manage extensions
  - 12.3 GanosBase TSDB
    - 12.3.1 Quick start
  - 12.4 Heterogeneous data access
    - 12.4.1 mysql_fdw
    - 12.4.2 oss_fdw
  - 12.5 WAL logical decoding
    - 12.5.1 decoderbufs (decode to ProtoBuf)
    - 12.5.2 wal2json
  - 12.6 Similarity calculation
    - 12.6.1 hll
    - 12.6.2 imgsmlr (similar images)
    - 12.6.3 smlar
  - 12.7 Full-text search
    - 12.7.1 Quick start
    - 12.7.2 pg_bigm
    - 12.7.3 pg_jieba
    - 12.7.4 rum (full-text search acceleration)
  - 12.8 PGVector
  - 12.9 AGE (graph database)
  - 12.10 hypopg (hypothetical indexes)
  - 12.11 ip4r (network address storage)
  - 12.12 pg_cron
  - 12.13 pg_profile (resource monitoring)
  - 12.14 pg_sphere (spherical data calculations)
  - 12.15 pgAudit
  - 12.16 sequential_uuid (UUID generation)
  - 12.17 pg_pathman
  - 12.18 zhparser
  - 12.19 pldebugger
  - 12.20 Use PASE for efficient vector search
  - 12.21 pg_hint_plan
  - 12.22 varbitx
  - 12.23 pg_search (BM25 index)
- 13 Manage logs
- 14 CloudDBA
  - 14.1 Overview of CloudDBA
  - 14.2 Perform quick diagnostics
    - 14.2.1 Manage sessions
    - 14.2.2 Use the real-time monitoring feature
    - 14.2.3 Lock analysis
    - 14.2.4 View storage overview
  - 14.3 Performance Trend
  - 14.4 Slow query logs
  - 14.5 Diagnostic reports
- 15 AI capabilities
  - 15.1 Intelligent migration
    - 15.1.1 Intelligent migration guide
    - 15.1.2 AI Migration Assistant
    - 15.1.3 Migrate data from a PolarDB for PostgreSQL 14 cluster to a PolarDB for PostgreSQL 16 cluster through visualized operations
      - 15.1.3.1 Prechecks
        - 15.1.3.1.1 Syntax compatibility check
        - 15.1.3.1.2 Plug-in compatibility check
        - 15.1.3.1.3 Account migration
      - 15.1.3.2 Use DTS to migrate data
        - 15.1.3.2.1 Data migration
        - 15.1.3.2.2 Data synchronization
    - 15.1.4 Migrate data from ApsaraDB RDS for PostgreSQL to PolarDB for PostgreSQL through visualized operations
      - 15.1.4.1 Use DTS to migrate data
        - 15.1.4.1.1 Migrate data
        - 15.1.4.1.2 Data synchronization
        - 15.1.4.1.3 View data migration tasks
      - 15.1.4.2 Prechecks
        - 15.1.4.2.1 Syntax compatibility check
        - 15.1.4.2.2 Check the compatibility of extensions
        - 15.1.4.2.3 Migrate accounts from the ApsaraDB RDS for PostgreSQL instance to the PolarDB for PostgreSQL cluster
  - 15.2 AI-native operations for MCP services
  - 15.3 Best practices for connecting PolarDB for PostgreSQL to Dify by using the MCP service
- 16 Appendix
  - 16.1 Authorize a tenant organization to access SLB
  - 16.2 Launch templates

g on to the Cloud-native Databas e PolarDB console

## 1 Log on to the Cloud-native Database PolarDB console

**Database PolarDB console**

This topic describes how to log on to the Cloud-native Database PolarDB console using Google Chrome as an example.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. g on to the Cloud-native Databas e PolarDB console You can click the current language in the upper-right corner to switch to another language. The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button. If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.
Obtain the username and password from an operations administrator. The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**. For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in Apsara Uni-manager Management Console User Guide.
5. In the top menu bar, click **Products > Databases > Relational Database > Cloud-**
**native Database PolarDB**.
stance types

## 2 Instance types

This topic describes the instance types of PolarDB for PostgreSQL.

**Comparison between general-purpose and dedicated instance**

**types**

| Instance type | Feature | Scenario |
|---|---|---|
| Dedicated | A dedicated cluster occupies all allocated compute resources such as CPUs. The cluster does not share compute resources with other clusters that run on the same server. This improves the reliability and stability of the cluster. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| General- purpose | Idle compute resources such as CPUs are shared among clusters that run on the same server. Resource sharing allows you to deploy a large number of clusters at low costs. | Scenarios in which cost-effectiveness is prioritized. |

| Subtype | Code of instance type | CPU and memory |
|---|---|---|
| General- purpose | polardb.g4.medium.2 | 2 cores, 8 GB |
|   | polardb.g2.large.2 | 4 cores, 8 GB |
|   | polardb.g4.large.2 | 4 cores, 16 GB |
|   | polardb.g2.xlarge.2 | 8 cores, 16 GB |
|   | polardb.g4.xlarge.2 | 8 cores, 32 GB |
|   | polardb.g2.2xlarge.2 | 16 cores, 32 GB |
|   | polardb.g4.2xlarge.2 | 16 cores, 64 GB |
|   | polardb.g2.4xlarge.2 | 32 cores, 64 GB |
|   | polardb.g4.4xlarge.2 | 32 cores, 128 GB |
| > Document Versio | n: 20260831 1 |   |

stance types

|   | polardb.g8.4xlarge.2 | 32 cores, 256 GB |
|---|---|---|
|   | polardb.x4.medium.2 | 2 cores, 8 GB |
|   | polardb.x8.medium.2 | 2 cores, 16 GB |
|   | polardb.x4.large.2 | 4 cores, 16 GB |
|   | polardb.x8.large.2 | 4 cores, 32 GB |
| Dedicated |   |   |
|   | polardb.x4.xlarge.2 | 8 cores, 32 GB |
|   | polardb.x8.xlarge.2 | 8 cores, 64 GB |
|   | polardb.x4.2xlarge.2 | 16 cores, 64 GB |
|   | polardb.x8.2xlarge.2 | 16 cores, 128 GB |
|   | polardb.x4.4xlarge.2 | 32 cores, 128 GB |
|   | polardb.x8.4xlarge.2 | 32 cores, 256 GB |
|   | polardb.x4.8xlarge.2 | 64-core, 256 GB |
|   | polardb.x8.8xlarge.2 | 64 cores, 512 GB |
|   | polardb.x8.12xlarge.2 | 88 cores, 710 GB |
| Exclusive | polardb.x8.15xlarge.2 Important This specification is for exclusive servers and depends on a specific model. It is disabled by default. To enable it, contact technical support. | 120 cores, 960 GB |

uick Start

## 3 Quick Start

### 3.1 Limits

To ensure stability and security, PolarDB for PostgreSQL clusters that run Primary/Secondary Edition have certain limits, as listed in the following table.

| Item | Limit |
|---|---|
| Instance parameters | You can modify most cluster parameters in the PolarDB console or by calling API operations. For security and stability purposes, specific parameters cannot be modified. |
| Root permissions | Root or system administrator permissions are not provided. |
| Database backup | Logical backup can be performed by using the CLI or GUI. You can perform physical backup only in the PolarDB console or by calling API operations. |
| Database restoration | Logical restoration can be performed by using the CLI or GUI. You can perform physical restoration only in the PolarDB console or by calling API operations. |
| Database replication | PolarDB for PostgreSQL provides dual-node clusters that run on top of a primary/secondary replication architecture. The secondary instances in this replication architecture are hidden and cannot be directly accessed. |
| PolarDB for PostgreSQL cluster restart | You can restart PolarDB for PostgreSQL clusters only in the PolarDB console or by calling API operations. |
| Account and database management | By default, you must use the PolarDB console to manage accounts and databases. PolarDB for PostgreSQL also allows you to create a privileged account to manage users, passwords, and databases. |
| Standard account | Authorization is not allowed. You can use the console to manage accounts and databases. Clusters that support standard accounts also support privileged accounts. |
| Privileged account | Authorization is allowed on standard accounts. You can use the console to create and manage accounts. You can perform permission operations by using command lines. The privileged account cannot be reverted to a standard account. |

uick Start

### 3.2 Get started with PolarDB for PostgreSQL Primary/Secondary Edition

**PostgreSQL Primary/Secondary**

**Edition**

To quickly launch a PolarDB for PostgreSQL Primary/Secondary Edition instance, you need to create the instance, configure a whitelist, create a database, create an account, and then connect to the instance. This topic describes how to create a PolarDB for PostgreSQL Primary/Secondary Edition instance. You must perform the following steps before you can use a PolarDB for PostgreSQL instance. PolarDB for PostgreSQL instances are virtualized database servers. You can create PolarDB for PostgreSQL instances based on your business requirements. You can create and manage multiple databases on a PolarDB for PostgreSQL instance. To ensure the security and stability of databases, after you create a PolarDB for PostgreSQL Primary/Secondary Edition instance, you need to add the IP addresses or CIDR blocks of clients to a whitelist to allow external access to the instance. Whitelists provide controlled access to PolarDB for PostgreSQL Primary/Secondary Edition instances at the highest security level. We recommend that you maintain whitelists regularly. Configuring whitelists for your instance does not affect the workloads on the instance.
3. Create a database and create an account
Before you get started with PolarDB for PostgreSQL Primary/Secondary Edition, you must create a database and an account for the instance.
4. Use Data Management (DMS) to log in to the PolarDB for PostgreSQL instance
After you create a PolarDB for PostgreSQL instance, configure an IP address whitelist, and create a database and an account. Then, you can connect to the instance by using a database client. stances

## 4 Instances

### 4.1 Create an instance

This topic describes how to use the ApsaraDB for PolarDB private cloud console to create an ApsaraDB for PostgreSQL primary/standby edition instance.

**Prerequisites**

You must have an account to log on to the Alibaba Cloud console.

**Procedure**

1. Log on to the ApsaraDB for PolarDB console.
2. On the **instance list** page, click **Create instance** in the upper-left corner.
3. Configure the following parameters.

| Category | Paramete r | Description |
|---|---|---|
| Basic informati on | Organizat ion | The organization to which the instance belongs. |
|   | Resource group | The resource group to which the instance belongs. |
|   | Region | The region where the instance is deployed. Instances in different regions cannot communicate over the internal network. You cannot change the region after the instance is created. |
|   | Deployme nt solution | The deployment solution for the instance. Supported options are: single-AZ/MAZ deployment and multi-AZ deployment. |
|   | Primary AZ | The availability zone where the primary node is deployed. |
|   | Standby AZ | The availability zone where the standby node is deployed. Note This parameter is required only if you select multi-AZ deployment as the deployment solution. If you select the same availability zone as the primary node, the configuration is equivalent to a single-AZ deployment. |

stances

| Instance configurati on | Chip architect ure | The chip architecture of the instance's host. |
|---|---|---|
|   | Database type | Select a database type. PostgreSQL-Compatible Oracle-Compatible |
|   | Compatib le version | The syntax-compatible version of the database. The following versions are supported: 17 16 14 Note Versions 17 and 16 are supported only when Database Type is set to PostgreSQL-Compatible. |
|   | Number of minor versions to display | The number of minor versions to display. |
|   | Database minor version | The minor version of the database. By default, the latest minor version is selected. |
|   | Series | The instance series. The following options are available: high- availability edition and read-only instance. |
|   | Storage type | The instance storage type, which is fixed to local SSD. |
|   | Enable TDE | Specifies whether to enable Transparent Data Encryption (TDE). Note Once enabled, TDE cannot be disabled. You can enable TDE only when creating an instance. |

stances

|   | Encryptio n algorithm | Select an encryption algorithm. Valid values: aes-256 (default) sm4 Note This parameter is required only when TDE is enabled. It cannot be changed after the instance is created. |
|---|---|---|
|   | Encryptio n key | Select an encryption key. This parameter is required if TDE is enabled. You can use a key automatically generated by Alibaba Cloud, or create a custom key in Key Management Service (KMS). To create a custom key, see the documentation for Key Management Service, specifically the Create a key > User Guide. |
|   | Instance type | The instance type. Different instance types offer different memory sizes, maximum connections, and IOPS. Specific values are displayed on the console page. |
|   | Storage space | The total storage space, which includes space for data, system files, binary log files, and transaction files. The actual available storage space is displayed on the console. |
|   | Connectiv ity type | The network connectivity types supported by the instance: Public Connection: Provides an endpoint to access the database from the internet. Private Connection: Provides an endpoint to access the database from the Alibaba Cloud internal network. Note This setting cannot be changed after the instance is created. |
|   | Network type | The network types supported by the instance: Classic Network: Cloud services in a classic network are not isolated at the network layer. You must rely on the service's security group or whitelist rules to block unauthorized access. Virtual Private Cloud (VPC): A Virtual Private Cloud (VPC) is an isolated network environment on Alibaba Cloud. You can customize the route table, IP address range, and gateway in the VPC. We recommend using a VPC for enhanced security. Note If you select VPC, you must also select a VPC and a VSwitch. |

stances

| Network |   |   |
|---|---|---|
|   | IP type | IPv4: Assigns only an IPv4 address. This is suitable for IPv4-only network environments. IPv4/v6 dual-stack: Assigns both an IPv4 and an IPv6 address. This is suitable for mixed network environments where clients must connect by using either IPv4 or IPv6. If you enable this option, you must configure an IPv6 whitelist to control access from IPv6 addresses. Note To configure this parameter, you must first enable the IPv6 switch. For more information, see the "Enable the PolarDB IPv6 switch" section in the O&M Guide. If you receive an "unauthorized" or similar error message, see Authorize Server Load Balancer Service for Tenant Organization. |
|   | VPC | Select a VPC. This parameter is required when Network type is set to Virtual Private Cloud (VPC). |
|   | VSwitch availabilit y zone | Select the availability zone for the VSwitch. This parameter is required when Network type is set to Virtual Private Cloud (VPC). |
|   | VSwitch | Select a VSwitch. This parameter is required when Network type is set to Virtual Private Cloud (VPC). |
|   | IP address whitelist | The IP addresses or CIDR blocks allowed to access theP olarDB instance. Note When IP type is set to IPv4/v6 dual-stack, the IPv6 whitelist parameter is displayed and must be configured. |
|   | IPv6 whitelist |   |
| Instance settings | Number of instances | Specify the number of PolarDB instances to create. The default value is 1. Batch creation is supported. |
|   | Instance name | Specify an instance name that meets the following requirements: Must start with a letter or a Chinese character. It can contain digits and the following special characters: colons ( : ), underscores ( ), _ and hyphens ( - ). Must be 2 to 64 characters in length. Cannot start with http:// or https:// . |

4. Before you create the instance, review the configuration in the **Configuration Summary**
panel on the right to confirm your settings. stances You can click **Save as launch template** in the **Configuration Summary** panel to save the current settings as a launch template. You can use this template to quickly create instances with the same configuration in the future. If your quota is insufficient, click **Quota management** to adjust it. For more information, see the **Quota Management** chapter in the **Unified Cloud Management Platform Us**
**er Guide**.
5. After you complete the configuration, click **Submit**.

### 4.2 Restart an instance

This topic describes how to manually restart a local disk-based PolarDB for PostgreSQL instance. This applies if the number of connections exceeds the specified threshold or if a local disk-based PolarDB for PostgreSQL instance has performance issues.

**Prerequisites.**

The local disk-based PolarDB for PostgreSQL instance that you want to restart is in the
**Running** state.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. Click **Restart Instance** in the upper-right corner.
When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.
4. In the dialog box that appears, click **OK**.

### 4.3 Change specifications

This topic describes how to change the instance type and storage space of a local disk-based PolarDB for PostgreSQL instance.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, click the ID of the cluster that you want to manage.
3. In the **Configure Information** section of the **Basic Information** page, click **Change**
**Specifications**.
4. On the **PolarDB Primary/Secondary Edition Configuration Change** page, configure
the **Cluster Edition**, **Storage Class**, **Instance Type**, **Storage Capacity**, and
**Configuration Change Time** parameters.
5. Click **Submit**.
stances

### 4.4 Configure a maintenance window

**window**

You can specify a maintenance window for a PolarDB for PostgreSQL instance that runs Primary/Secondary Edition based on your business requirements.

**Background information**

After you configure a maintenance window for your PolarDB for PostgreSQL instance that runs Primary/Secondary Edition, the backend system maintains the instance during the maintenance window. This ensures the stability of the instance. The default maintenance window spans from 02:00 to 06:00. We recommend that you set the maintenance window to an off-peak hour based on your business requirements. This helps prevent interruptions to your workloads.

**Usage notes**

To ensure stability of the maintenance process, the instance enters the **Maintaining**
**Instance** state before the maintenance window. When the instance is in this state,
database access and query operations, such as performance monitoring, are not affected. However, modification operations, such as upgrades, downgrades, and restarts, are temporarily unavailable, except for account management, database management, and IP address whitelist configuration. During the maintenance window, connections to the instance may be temporarily interrupted once or twice. Make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, find the instance that you want to manage and
click its ID or click **Management** in the **Operation** column of the instance to go to the details page.
3. In the **Configuration Information** section of the page that appears, click **Settings** to the
right of **Maintenance Window**.
4. Select a maintenance window and click **Yes**.
The maintenance window is displayed in UTC+8.

### 4.5 Primary/standby switchover

ApsaraDB for PolarDB supports primary/standby switchover. This feature ensures high availability by promoting the standby node to primary, either automatically or manually, if the primary node becomes unavailable.

**Background information**

stances The architecture of a PolarDB for PostgreSQL (Primary/Standby Edition) instance is designed to ensure service availability in the event of a single node failure. If the primary node fails, the standby node is promoted to primary. If the standby node fails or the former primary node is demoted to standby, the instance's control plane first waits for the affected node to recover and re-establish data synchronization with the current primary node. If the wait time exceeds a specified threshold, the control plane initiates a cross-host rebuild to create a new standby node on a different host. The deprecated standby node is then released and its resources are reclaimed by a periodic inspection task. The primary and standby nodes of a PolarDB for PostgreSQL (Primary/Standby Edition) instance synchronize data in real time. You can access only the primary instance. The standby instance serves only as a backup and does not handle service requests. After a primary/standby switchover, the former primary instance becomes the standby instance.

**Important**

A primary/standby switchover may cause a transient interruption. Perform this operation during off-peak hours and ensure that your application has an automatic reconnection mechanism.

**Procedure**

1. Log on to the ApsaraDB for PolarDB console.
2. On the **instance list** page, click the ID of the target instance or click **manage** in the
**actions** column to open the **basic information** page.
3. In the left-side navigation pane, choose **service availability**.
4. In the **instance availability** section, click **primary/standby switchover**.
5. In the dialog box that appears, set the switchover to take place immediately or at a
specified time, and then click **OK**.

**Important**

During a primary/standby switchover, operations such as managing databases and accounts or switching network types cannot be performed. Schedule the switchover within a maintenance window.

### 4.6 Release an instance

This topic describes how to release a local disk-based PolarDB for PostgreSQL instance. You can release a local disk-based PolarDB for PostgreSQL instance based on your business requirements.

**Usage notes**

Only instances in the Running state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance.

**Procedure**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, find the instance that you want to manage and
click **Release an instance**.
3. In the message that appears, click **OK**.
stances

### 4.7 Upgrade a minor engine version

**version**

PolarDB for PostgreSQL (High-availability Edition) instances support manual minor engine version upgrades. A minor engine version upgrade may include performance improvements, new features, or bug fixes. Each time you log on to the console, the system automatically checks for new minor engine versions. If a new minor engine version is released, the system does not automatically upgrade the instance. You can manually upgrade the minor engine version on the Basic Information page of the instance.

**Precautions**

Upgrading the minor engine version restarts the instance and causes a transient disconnection that lasts about 30 seconds. Perform the upgrade during off-peak hours and make sure your application has an automatic reconnection mechanism. If it does not, manually reconnect your application to the database. You cannot downgrade the minor engine version after an upgrade. Operations such as a hardware upgrade or configuration adjustment may cause the instance to automatically upgrade to the latest minor engine version. This behavior depends on the system policy.

**Manually upgrade a minor engine version**

1. Log on to the PolarDB console.
2. On the **Instance List** page, click the target instance ID or click **Manage** in the **Actions**
column. This opens the **Basic Information** page.
3. To the right of the **Configuration Information** section, click **Upgrade Minor Engine**
**Version**.
If this button does not appear, the kernel is already the latest version.
4. In the dialog box that appears, select a **DB Minor Version** (optional), set the **Upgrade**
**Time**, and click **OK**.

**Important**

If you do not select a target minor version, the system upgrades the instance to the latest minor engine version by default.

### 4.8 Manage instances in the recycle bin

**recycle bin**

This topic describes how to recreate or destroy a PolarDB instance in the recycle bin.

**Feature description**

All PolarDB for PostgreSQL instances that run Primary/Secondary Edition are moved to the recycle bin after they are manually released: An instance is not moved to the recycle bin in the following scenarios: stances The instance is manually released within seven days after creation. The instance is a **read-only instance**.

**Rebuild an instance**

If you manually release an instance that runs for more than seven days, backup files of the instance are retained for another eight days. Within the eight-day retention period, you can create another instance and restore data from the backup files to the new instance. After the eight-day retention period elapses, the backup files of the instance are deleted.
1. Log in to the PolarDB console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Recycle Bin**.
3. Find the released instance and click **Rebuild and restore** in the Operation column.
4. On the PolarDB Primary-Secondary Edition Recovery page, select **Database Version**,
**Storage Capacity**, and **Network Type** for the new instance and click **Submit**.
If you set **Network Type** to **VPC**, you must configure a virtual private cloud (**VPC**) and a **vSwitch**. Other configurations remain the same as the original instance and cannot be changed.

**Destroy an instance**

You can destroy a PolarDB instance that is no longer needed in the recycle bin.

**Warning**

After you destroy an instance, **all** the backup files of the instance are destroyed, including regular data backup files, archived backup files, and log backup files. The destroyed backup files **cannot be restored**. Proceed with caution.
1. Log in to the PolarDB console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Recycle Bin**.
3. Find the released instance and click **Destroy now** in the Operation column. In the message
that appears, click **OK**.

### 4.9 Read-only instance

#### 4.9.1 Overview

PolarDB for PostgreSQL allows you to create read-only instances. In scenarios in which PolarDB for PostgreSQL has a small number of write requests but a large number of read requests, you can create read-only instances to offload read requests from the primary instance. This topic describes the features and limits of read-only instances. If a large number of read requests overwhelm the primary instance, service interruptions may occur. In this case, you can create one or more read-only instances to offload read traffic from the primary instance. This scales the read capacity of the database system and improves application throughput. stances Read-only instances are deployed in the same region as the primary instance but may reside in different zones. The following figure shows the topology of read-only instances.

| Read and Write Requests Business Server Read- only Requests | Zone A Primary Primary Node RO Primary Read-only | Physical | Zone B Standby Secondary Node Physical Replicatio Standby Secondary Read-only |
|---|---|---|---|
|   |   | Replication Physical Replication |   |

**Read-only instances have the following features:**

Specifications of a read-only instance can be different from those of the primary instance and can be changed at any time, which facilitates elastic scaling. Read-only instances do not require database or account maintenance, because their database and account information is synchronized with the primary instance. The whitelists of read-only instances can be configured independently. System performance monitoring is provided. PolarDB for PostgreSQL provides a variety of optimization suggestions. For example, it provides storage engine check, primary key check, large table check, and check for excessive indexes and missing indexes. You can optimize databases based on the optimization suggestions and your applications.

#### 4.9.2 Create a read-only instance

This topic describes how to create a read-only instance, which you can use to handle large numbers of read requests.

**Usage notes**

A maximum of five read-only instances can be created for a primary instance. Backup settings and temporary backup are not supported. Instance restoration is not supported. Database creation and deletion are not supported. Read-only instances do not support account creation, deletion, authorization, or password changes. After a read-only instance is created, you cannot overwrite the data of its primary instance by using a data backup file.

**Procedure**

stances
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the **Instance Distribution** section of the **Basic Information** page, click **Add** to the
right of Read-only Instance.
4. On the Creating a read-only instance for PolarDB primary/standby edition page, configure
the read-only instance parameters.

| Section | Parameter | Description |
|---|---|---|
| Region | Region | The region where the PolarDB instance resides. |
| Configuratio n | Database Engine | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Syntax Compatibility | The version of the database engine, which is the same as that of the primary instance and cannot be changed. |
|   | Series | The value is fixed to Read-Only Instance. |
|   | Storage Class | The storage type of the read-only instance. |
|   | Instance Type | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time to facilitate flexible upgrade and downgrade. |
|   | Storage Space | The storage capacity of the read-only instance. To ensure sufficient I/O throughput for data synchronization, the read- only instance must have instance specifications and storage capacity equal to or greater than those of the primary instance. |
|   | Network Type | The network type of the read-only instance. It must be the same as that of the primary instance and cannot be changed. |

stances

|   | IP Type | IPv4: Assign IPv4 addresses only. Applies to pure IPv4 network environment. Dual-Stack: IPv4 and IPv6 addresses are assigned to the same network. This method is suitable for hybrid network scenarios that require access from both IPv4 and IPv6 clients. Note To configure this parameter, you must first enable the IPv6 switch. For more information, see the "Enable the PolarDB IPv6 switch" section in the O& M Guide. If you receive an "unauthorized" or similar error message, see Authorize Server Load Balancer Service for Tenant Organization. |
|---|---|---|
| Network Type |   |   |
|   | VPC | The virtual private cloud (VPC) in which you want to create the read-only instance. This parameter is required when Network Type is set to VPC. |
|   | vSwitch | The vSwitch in the VPC. This parameter is required when Network Type is set to VPC. |

5. After you complete the configuration, click **Confirm Order**.

#### 4.9.3 View details of read-only instances

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances Using Local Disks page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View details of a read-only instance from the Instances Using**

**Local Disks page**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, click the ID of the read-only instance that you
want to view to go to the **Basic Information** page. In the instance list, the **Instance Type** column of read-only instances is displayed as
**Read-Only Instance**.

**View details of a read-only instance from the Basic Information**

**page of the primary instance**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page. stances
3. On the **Basic Information** page, move the pointer over the number next to **Read-only**
**Instance** in the **Instance Distribution** section. The ID of the read-only instance is
displayed.
4. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

### 4.10 Modify the values of parameters for an instance

**parameters for an instance**

This topic describes how to view and modify the values of some parameters and query the parameter modification records in the console.

**Modify the values of parameters**

1. Log on to the Apsara Stack console for PolarDB for PostgreSQL V2.0.
2. On the **Instances Using Local Disks** page, click the ID of the target instance, or click
**Manage** in the **Actions** column. The **Basic Information** page is displayed.
3. In the navigation pane on the left, click **Parameters**.
4. You can perform the following operations:

**Export parameters**

On the Modifiable Parameters tab, click **Export Parameters**. The parameter settings of the instance are exported as a TXT file to your computer.

**Modify parameters in batches by importing a file**

a. Modify the parameter settings in the TXT file. Then, click **Import Parameters**. In the Import Parameters dialog box, copy the parameter settings from the TXT file and paste them to the dialog box. b. Click **OK**. c. In the upper part of the page, click **Apply Changes**. If the new parameter settings take effect only after you restart the instance, the system prompts you to restart the instance. We recommend that you restart the instance during off-peak hours and make sure that your application is configured to automatically reconnect to the instance. Before the new parameter values are applied, you can click **Cancel**
**Changes** to cancel the modification.

**Modify a single parameter**

a. On the **Modifiable Parameters** tab, find the parameter that you want to modify and click the icon in the **Current Value** column. b. Enter a value based on the value range. c. Click **OK**. stances d. In the upper part of the page, click **Apply Changes**. If the new parameter settings take effect only after you restart the instance, the system prompts you to restart the instance. We recommend that you restart the instance during off-peak hours and make sure that your application is configured to automatically reconnect to the instance. Before the new parameter values are applied, you can click **Cancel**
**Changes** to cancel the modification.

**View the parameter modification history**

1. Log on to the Apsara Stack console for PolarDB for PostgreSQL V2.0.
2. On the **Instances Using Local Disks** page, click the ID of the target instance, or click
**Manage** in the **Actions** column. The **Basic Information** page is displayed.
3. In the navigation pane on the left, click **Parameter Settings**.
4. Click the **Modification History** tab.
5. Select a time range and click **Query**.

**Parameter descriptions**

| Parame ter | Default value | Recomm ended value | Value range | Res tart req uire d | Description |
|---|---|---|---|---|---|
| log conn _ ections | off | off | [on\|off] | No | Specifies whether to record an event log for each successful client connection to the database instance. Enabling this parameter increases the log volume, especially in high-concurrency scenarios. Plan your log storage policy accordingly. |
| log disc _ onnectio ns | off | off | [on\|off] | No | Specifies whether to record an event log for the disconnection at the end of each database session. Enabling this parameter increases the log volume, especially in high-concurrency scenarios. Plan your log storage policy accordingly. |

stances

| archive _ mode | on | on | [always\|o n\|off] | Yes | ARCHIVELOG mode. In addition to `off` which disables the mode, two other modes are available: `on` and `always`. During normal operations, these two modes are identical. However, when set to `always`, the WAL archiving process remains enabled even during archive recovery or in standby mode. In `always` mode, all files restored from the archive or transferred using streaming replication are archived again. |
|---|---|---|---|---|---|
| old snap _ shot thr _ eshold | -1 | -1 | [-1- 86400] | Yes | Controls the expiration threshold for old snapshots. Snapshots older than this threshold are cleared to prevent excessive resource consumption. A negative value, such as -1, disables automatic cleanup. The unit is minutes. |
| shared _ preload _ libraries | 'polar vf _ s,polar _ worker,p g stat st _ _ atement s,auth d _ e lay,auto explain, _ zhparser ,plugin _ debugge r,polar _ mo nitor pre _ load,pg _ pathman ' | 'polar vfs, _ polar work _ er,pg stat _ statemen _ ts,auth de _ lay,auto e _ xplain,zhp arser,plugi n debugg _ er,polar m _ o nitor prelo _ ad,pg pat _ hman' | ^'(polar _ vfs,polar _ worker) (,\w+)*'$ | Yes | Specifies a list of shared libraries to preload when the PostgreSQL instance starts. These libraries, separated by commas, typically contain extensions or plugins. After this parameter is set, the related features take effect across the entire database cluster. Note Changing this parameter requires a restart of the PostgreSQL service. |
| track co _ mmit ti _ mestam p | off | off | [on\|off] | Yes | Specifies whether to record the timestamp of a transaction commit. If this parameter is enabled, you can query the commit time of transactions, but this adds some storage overhead. The default value is `off`. |

stances

| wal leve _ l | logical | logical | [minimal\| replica\|lo gical] | Yes | Controls the level of information written to the Write-Ahead Logging (WAL). This determines the availability of replication and recovery features. Common values include `minimal` (logs the minimum information), `replica` (supports replication), and `logical` (supports logical decoding). |
|---|---|---|---|---|---|
| autovac uum vac _ uum cos _ t delay _ | 0 | 0.0 | [-1-100] | No | Defines the time interval in milliseconds that the autovacuum process pauses after each cleanup operation. This is used to control the impact of cleanup on system performance. |
| autovac uum vac _ uum cos _ t limit _ | 10000 | 10000 | [-1- 10000] | No | Sets the cost limit for a single autovacuum operation. This is used to balance the impact of cleanup tasks on system performance. |
| auto ex _ plain.log analyze _ | off | off | [on\|off] | No | Controls whether to log the execution plan and analysis information of a query. Enabling this parameter provides detailed performance data but increases overhead. |
| auto ex _ plain.log buffers _ | off | off | [on\|off] | No | Controls whether to log buffer usage during query execution. Enabling this parameter can help you analyze performance issues and check whether performance degradation is caused by insufficient buffers. |
| auto ex _ plain.log format _ | text | text | [text\|xml\| json\|yaml ] | No | Specifies the output format for the query plan logs generated by the auto explain _ module. Options typically include text (default, plain text format) and json (structured JSON format). This controls the readability or machine-parsability of the logs. |
| auto ex _ plain.log min du _ _ ration | -1 | -1 | [-1- 2147483 647] | No | Sets the minimum execution time threshold in milliseconds. Queries that exceed this threshold are logged. The default value is -1, which means no queries are logged. |
| auto ex _ plain.log nested _ _ stateme nts | off | off | [on\|off] | No | Controls whether to log the execution plans of nested SQL statements, such as statements in functions or sub- transactions. When set to `on`, the execution plans of these statements are also logged, which helps with in-depth performance analysis. |

stances

| auto ex _ plain.log timing _ | on | on | [on\|off] | No | Controls whether to include timing information for each query step in the auto explain output. When set to `on`, _ execution times are recorded. When set to `off`, timing information is not recorded. The default value is typically `on`. |
|---|---|---|---|---|---|
| auto ex _ plain.log triggers _ | off | off | [on\|off] | No | Specifies whether to include trigger execution information in the auto explain log. When set to `on`, _ trigger execution details are recorded, which helps analyze the impact of triggers on query performance. The default value is `off`. |
| auto ex _ plain.log verbose _ | off | off | [on\|off] | No | Specifies whether to include detailed plan information in the auto explain _ output. When set to `on`, more detailed query execution plans are recorded, including extra information for each node. The default value is `off`. |
| auto ex _ plain.sa mple rat _ e | 1 | 1 | [0-1] | No | Sets the probability for the auto explain _ module to sample execution plans. This controls the logging frequency. The value ranges from 0 to 1, where 0 means no sampling and 1 means every execution is logged. |
| datestyl e | 'ISO,YM D' | 'ISO,YMD' | ^'(MDY\|I SO\|Postgr es\|SQL\|G erman\|Y MD\|... | No | Defines the display format for dates and times, and the default rules for parsing input. It affects the output style of dates (such as ISO, SQL, or Postgres) and the order of month and day (such as MDY or DMY). |
| default t _ ransacti on defer _ rable | off | off | [on\|off] | No | Sets whether the default transaction is deferrable. This controls whether transactions are allowed to be deferred in read-only mode to optimize performance. |
| default _ with oid _ s | off | off | [on\|off] | No | Determines whether to include an OID column by default when a new table is created. |
| enable p _ artitionw ise aggr _ egate | on | on | [on\|off] | No | Controls whether to enable partition- wise aggregate operations. When set to `on`, PostgreSQL attempts to perform aggregation on each partition of a partitioned table separately, which may improve query performance. |

stances

| enable p _ artitionw ise join _ | on | on | [on\|off] | No | Controls whether to enable partition- wise join optimization. When set to `on`, PostgreSQL attempts to perform more efficient join operations on partitioned tables to improve query performance. |
|---|---|---|---|---|---|
| extra flo _ at digits _ | 0 | 0 | [-15-3] | No | Controls the number of extra digits of precision displayed for floating-point number types, such as float4 and float8. A negative value reduces precision, and a positive value increases precision. This affects the display format of floating- point numbers. |
| idle in tr _ _ ansactio n sessio _ n timeo _ ut | 3600000 | 3600000 | ^(0\|[1- 9]\d\d\d\|\ d{5,9}\|1\ d{9}\|200 0... | No | Sets the timeout for idle transaction sessions. A session is automatically terminated after it is idle for longer than this time. |
| idle sess _ ion time _ out | 8640000 0 | 86400000 | [0- 2147483 647] | No | Sets the maximum duration for an idle session before it is automatically terminated. |
| jit | off | off | [on\|off] | No | Controls whether PostgreSQL enables the Just-In-Time (JIT) compilation feature to accelerate query execution. A value of `on` enables JIT, and `off` disables it. |
| lock tim _ eout | 0 | 0 | ^(0\|[1- 9]\d\d\d\|\ d{5,9}\|1\ d{9}\|200 0... | No | Sets the timeout in milliseconds for acquiring a lock in a single database transaction. If the timeout is exceeded, the attempt is aborted and an error is reported. A value of 0 means no timeout. |
| log min _ _ duration statem _ ent | 1000 | 1000 | [-1- 2147483 647] | No | Logs SQL statements whose execution time exceeds the specified number of milliseconds. This is used to locate slow queries. A value of 0 logs all statements, and -1 logs none. |

stances

| log stat _ ement | ddl | ddl | [none\|ddl \|mod\|all] | No | Controls which SQL statements are logged by PostgreSQL. It can be set to one of the following values: none: Does not log any SQL statements. ddl: Logs only data definition language (DDL) statements, such as CREATE, ALTER, and DROP. mod: Logs all data modification statements, such as INSERT, UPDATE, and DELETE, along with DDL statements. all: Logs all SQL statements. |
|---|---|---|---|---|---|
| log tem _ p files _ | 100000 | 100000 | [-1- 2147483 647] | No | Sets the threshold in kilobytes for logging the size of temporary files. When the size of a temporary file, such as a file generated by a sort or hash operation, exceeds this value, PostgreSQL logs related information. A value of -1 means no temporary file information is logged. |
| log time _ zone | UTC | UTC | ^'(((UTC) (-){0,1} (\d\|[1- 9]\d\|1([0- 5... | No | Sets the time zone used in PostgreSQL log records to standardize the display of log times. The default value is typically the system time zone. |
| min par _ allel ind _ ex scan _ _ size | 64 | 64 | [0- 7158278 82] | No | Sets the minimum table size required for a parallel index scan. Tables smaller than this size do not use parallel scans. |
| min par _ allel tabl _ e scan s _ _ ize | 1024 | 1024 | [0- 7158278 82] | No | Sets the minimum table size that can be processed in parallel by a table scan. |
| polar en _ able cic _ _ on partit _ ioned | on | on | [on\|off] | No | Controls whether to enable Constraint Exclusion on partitioned tables. When set to `on`, the optimizer automatically skips unnecessary partition scans based on partition constraints, which improves query performance. When set to `off`, this feature is disabled. The default value is typically `on`. |

stances

| polar en _ able con _ vert or t _ _ o union _ _ all | off | off | [on\|off] | No | Controls whether to optimize SQL queries by converting OR conditions into the UNION ALL form. Enabling this can improve query performance in specific scenarios but may increase the complexity of the query plan. on: Enables the conversion. off: Disables the conversion (default). |
|---|---|---|---|---|---|
| polar en _ able cre _ ate tabl _ e as bul _ _ k insert _ | on | on | [on\|off] | No | Specifies whether to enable the optimization feature for bulk inserts using the CREATE TABLE AS statement. |
| polar en _ able ddl _ replicat _ ion | on | on | [on\|off] | No | Specifies whether to enable replication for data definition language (DDL) operations. When enabled, DDL operations on the primary node are synchronously replicated to secondary nodes, ensuring consistent table schemas between the primary and secondary nodes. |
| polar en _ able pgs _ tat in sh _ _ ared sto _ rage | on | on | [on\|off] | No | Specifies whether to enable the feature that saves PostgreSQL performance statistics in shared storage. |
| polar en _ able px _ | off | off | [on\|off] | No | Specifies whether to enable the parallel execution feature. |
| polar nu _ m parts _ for pts _ _ | 32 | 32 | [-1- 2147483 647] | No | Specifies the number of partitions used for parallel transmission in PolarDB. This affects the efficiency of parallel processing and resource allocation. |
| polar px _ dop pe _ _ r node _ | 3 | 3 | [1-128] | No | The degree of parallelism (DOP) per node. This controls the number of parallel execution threads for queries on each node in PolarDB for PostgreSQL. A higher value can improve query performance but also increases resource consumption. |

stances

| polar px _ enable _ _ adps | off | off | [on\|off] | No | Specifies whether to enable the Advanced Data Processing Service (ADPS) feature of PolarDB to optimize the performance of complex queries and large-scale data processing. The value is a Boolean type (on/off). |
|---|---|---|---|---|---|
| polar px _ enable _ _ create t _ able as _ | on | on | [on\|off] | No | Specifies whether to enable the feature that creates tables using the CREATE TABLE AS statement. |
| polar px _ enable _ _ cte | on | on | [on\|off] | No | Specifies whether to enable optimization support for common table expressions (CTEs). |
| polar px _ enable _ _ cte shar _ ed scan _ | on | on | [on\|off] | No | Controls whether to enable shared scan optimization for common table expressions (CTEs) to improve query performance. |
| polar px _ enable _ _ explain _ all stat _ | off | off | [on\|off] | No | When enabled, the EXPLAIN command displays statistics for all nodes. This is used to analyze and optimize query plans. |
| polar px _ enable _ _ join pref _ etch inn _ er | on | on | [on\|off] | No | Controls whether to enable the inner table prefetch feature in parallel join operations to optimize query performance. |
| polar px _ enable _ _ left inde _ x nestlo _ op join _ | off | off | [on\|off] | No | Controls whether to enable the Left Index Nested Loop Join optimization strategy. When set to `on`, this optimization method is allowed to improve query performance. When set to `off`, this feature is disabled. |
| polar px _ enable _ _ partition | on | on | [on\|off] | No | Specifies whether to enable the partitioned table feature. When enabled, it supports parallel query optimization for partitioned tables. |
| polar px _ enable _ _ partition hash _ | on | on | [on\|off] | No | Enables or disables the hash distribution feature for partitioned tables to optimize the parallel query performance of large- scale partitioned tables. |

stances

| polar px _ enable _ _ plpgsql | on | on | [on\|off] | No | Specifies whether to enable PL/pgSQL language support. When set to `on`, you can use PL/pgSQL to write stored procedures and functions in PolarDB for PostgreSQL. |
|---|---|---|---|---|---|
| polar px _ enable _ _ prepare _ stateme nt | on | on | [on\|off] | No | Specifies whether to enable the Prepare Statement feature to optimize query execution efficiency. |
| polar px _ enable _ _ pre opti _ mizer ch _ eck | on | on | [on\|off] | No | Controls whether to enable pre-optimizer checks for additional logical validation and optimization preparation before query optimization. |
| polar px _ enable _ _ procedur e | on | on | [on\|off] | No | Specifies whether to enable the feature that allows PolarDB to execute stored procedures in parallel. |
| polar px _ enable _ _ result h _ ash filte _ r | on | on | [on\|off] | No | Controls whether to enable the result hash filter feature to optimize query execution performance. |
| polar px _ enable _ _ spi read _ all nam _ _ espaces | off | off | [on\|off] | No | Specifies whether to allow reading data from all namespaces through the SPI interface. |
| polar px _ enable _ _ subquer y | on | on | [on\|off] | No | Controls whether to enable parallel execution optimization for subqueries. When set to `on`, subqueries can be processed in parallel to improve performance. When set to `off`, this feature is disabled. |
| polar px _ enable _ _ tableless scan _ | off | off | [on\|off] | No | Specifies whether to enable the tableless scan feature to optimize query performance. |

stances

| polar px _ enable _ _ window _ function | on | on | [on\|off] | No | Enables or disables the window function feature in PolarDB for PostgreSQL. |
|---|---|---|---|---|---|
| polar px _ ignore f _ _ unction | '1574,15 75,1576, 1765,30 78,4032' | '1574,157 5,1576,17 65,3078,4 032' |   | No | Controls whether to ignore the execution of certain functions. This is typically used in debugging or optimization scenarios. |
| polar px _ interco _ nnect tr _ ansmit t _ imeout | 3600 | 3600 | [1-7200] | No | Sets the timeout for communication transmission between PolarDB PX nodes. This controls the maximum wait time for data transmission. |
| polar px _ max sli _ _ ces | 50 | 50 | [0- 2147483 647] | No | Controls the maximum number of segments in a parallel query. This affects the granularity of parallel execution and resource allocation. |
| polar px _ optimiz _ er bitma _ pscan fa _ ctor | 1.0 | 1.0 | [0- 9999999 99999.0] | No | Adjusts the cost factor for bitmap scans in the PolarDB parallel query optimizer. This affects the selection priority of bitmap scans in the query plan. The larger the value, the more the optimizer prefers other scan methods. |
| polar px _ optimiz _ er enabl _ e brinsc _ an | on | on | [on\|off] | No | Specifies whether to enable optimizer support for BRIN index scans. When set to `on`, the optimizer is allowed to consider using BRIN indexes to accelerate queries. When set to `off`, the optimizer ignores BRIN indexes. |
| polar px _ optimiz _ er enabl _ e crossp _ roduct | off | off | [on\|off] | No | Specifies whether to enable the cross- product optimizer feature. |
| polar px _ optimiz _ er enabl _ e dyna _ micinde xscan | on | on | [on\|off] | No | Specifies whether to enable the dynamic index scan optimizer feature. |

stances

| polar px _ optimiz _ er enabl _ e dyna _ micshar eindexsc an | on | on | [on\|off] | No | Enables or disables the dynamic shared index scan feature of the optimizer to improve query performance. |
|---|---|---|---|---|---|
| polar px _ optimiz _ er enabl _ e dyna _ mictable scan | on | on | [on\|off] | No | Specifies whether to enable the dynamic table scan optimizer feature. |
| polar px _ optimiz _ er enabl _ e group _ agg | on | on | [on\|off] | No | Controls whether to enable the Group Aggregate feature in the PolarDB parallel execution optimizer. When set to `on`, group aggregation operations can be executed in parallel to improve performance. When set to `off`, this feature is disabled. The default value is typically `on`. |
| polar px _ optimiz _ er enabl _ e hasha _ gg | on | on | [on\|off] | No | Controls whether to enable the hash- based aggregation optimization strategy. |
| polar px _ optimiz _ er enabl _ e hashjo _ in | on | on | [on\|off] | No | Controls whether to enable the hash join optimizer. When set to `on`, the optimizer is allowed to use the hash join algorithm. When set to `off`, hash join optimization is disabled. |
| polar px _ optimiz _ er enabl _ e indexo _ nlyscan | on | on | [on\|off] | No | Controls whether to enable the Index- Only Scan optimization strategy. When set to `on`, the optimizer considers using index-only scans to improve query performance. When set to `off`, the optimizer disables this strategy. The default value is typically `on`. |
| polar px _ optimiz _ er enabl _ e indexs _ can | on | on | [on\|off] | No | Specifies whether to enable the index scan optimizer. This controls whether index scans are considered during query optimization. |

stances

| polar px _ optimiz _ er enabl _ e lasj n _ _ otin | on | on | [on\|off] | No | Specifies whether to enable optimizer support for Left Anti Semi Join (LASJ) and NOT IN subqueries. |
|---|---|---|---|---|---|
| polar px _ optimiz _ er enabl _ e like to _ _ range r _ _ ewrite | off | off | [on\|off] | No | Controls whether to enable the optimization that rewrites LIKE expressions into range queries. When set to `on`, PostgreSQL attempts to convert LIKE expressions into more efficient range scan operations to improve query performance. |
| polar px _ optimiz _ er enabl _ e merge _ join | on | on | [on\|off] | No | Controls whether to enable the Merge Join feature in the optimizer. When set to `on`, the optimizer is allowed to select merge join as part of the query execution plan. |
| polar px _ optimiz _ er enabl _ e motio _ n broad _ cast | on | on | [on\|off] | No | Specifies whether to enable the broadcast data distribution optimization strategy. When set to `on`, the optimizer considers using the broadcast method to transfer data in the query plan. This is suitable for certain distributed query scenarios. |
| polar px _ optimiz _ er enabl _ e motio _ n gather _ | on | on | [on\|off] | No | Specifies whether to enable the Motion Gather operation in the optimizer to optimize data transfer in distributed queries. |
| polar px _ optimiz _ er enabl _ e motio _ n redistr _ ibute | on | on | [on\|off] | No | Enables or disables the optimizer's data redistribution optimization feature. |

stances

| polar px _ optimiz _ er enabl _ e partiti _ on selec _ tion | on | on | [on\|off] | No | Controls whether to enable the partition selection optimization feature for partitioned tables. |
|---|---|---|---|---|---|
| polar px _ optimiz _ er enabl _ e seqsc _ an | on | on | [on\|off] | No | Specifies whether to enable the sequential scan optimization strategy. |
| polar px _ optimiz _ er enabl _ e seqsh _ arescan | on | on | [on\|off] | No | Specifies whether to enable optimizer support for shared sequential scans. |
| polar px _ optimiz _ er enabl _ e sharei _ ndexsca n | on | on | [on\|off] | No | Specifies whether to enable the shared index scan optimizer feature. |
| polar px _ optimiz _ er enabl _ e sort _ | on | on | [on\|off] | No | Specifies whether to enable the sort feature in the optimizer. |
| polar px _ optimiz _ er index _ onlyscan factor _ | 1.0 | 1.0 | [0- 9999999 99999.0] | No | Controls the optimizer's preference for Index-Only Scans when evaluating the cost of an index scan. The higher the value, the more the optimizer prefers index scans. |
| polar px _ optimiz _ er index _ scan fac _ tor | 1.0 | 1.0 | [0- 9999999 99999.0] | No | An optimizer parameter that controls the cost of an index scan. It is used to adjust the priority of index scans in the query plan. The larger the value, the higher the cost of the index scan, which may cause the optimizer to prefer other scan methods. |
| polar px _ optimiz _ er nestl _ oop fact _ or | 1024.0 | 1024.0 | [1- 9999999 99999.0] | No | Controls the cost factor for nested loop joins. This affects the optimizer's preference for nested loop joins. The higher the value, the more the optimizer prefers other join methods. |

stances

| polar px _ optimiz _ er remo _ ve super _ fluous o _ rder | on | on | [on\|off] | No | Controls whether the optimizer removes superfluous sort operations to improve query performance. |
|---|---|---|---|---|---|
| polar px _ optimiz _ er share _ indexsc _ an facto _ r | 1.0 | 1.0 | [0- 9999999 99999.0] | No | Controls the cost factor for shared index scans in the parallel query optimizer. This affects the optimizer's choice of index scan method. The larger the value, the less likely shared index scans are used. |
| polar px _ optimiz _ er share _ tablesc _ an facto _ r | 1.0 | 1.0 | [0- 9999999 99999.0] | No | Controls the optimization factor for table scan sharing in parallel queries. This affects the allocation policy for table scans during parallel execution. A larger value indicates a preference for shared scans. A smaller value indicates a preference for independent scans. |
| polar px _ wait lo _ _ ck timeo _ ut | 1800000 | 1800000 | [0- 2147483 647] | No | Sets the timeout in milliseconds for PolarDB parallel execution (PX) to wait for a lock. A lock wait timeout error is triggered if the timeout is exceeded. This is used to avoid long-term blocking. |
| stateme nt timeo _ ut | 0 | 0 | ^(0\|[1- 9]\d{3,8} \|1\d{9}\|2 0000000 00)... | No | Sets the maximum allowed execution time for a single database query. The query is forcibly terminated if it exceeds this time. The unit is milliseconds. The default value is 0, which means no limit. |

stances

| synchro nous co _ mmit | off | off | [local\|re mote wri _ te\|remote apply\|on _ ... | No | Controls whether a transaction commit waits for the Write-Ahead Logging (WAL) record to be synchronized to the disk or a synchronous secondary database. This ensures data durability and consistency. The values include the following: on: Ensures that each commit waits for the WAL record to be written to storage. off: Does not wait for the WAL record to be written. Some committed transactions may be lost. local: Waits only for the local WAL write to complete. remote write: Waits for at least one _ synchronous secondary database to receive the WAL record. remote apply: Waits for at least one _ synchronous secondary database to apply the WAL record. |
|---|---|---|---|---|---|
| temp fil _ e limit _ | 100GB | 100GB | [-1- 2147483 647] | No | Controls the maximum size in kilobytes (KB) of temporary files that a single query can create. If the limit is exceeded, the query is canceled. A value of -1 means no limit. This is used to prevent temporary files from exhausting disk space. |
| timezon e | UTC | UTC | ^'(((UTC) (-){0,1} (\d\|[1- 9]\d\|1([0- 5... | No | Sets the time zone for the database. This affects the display and storage of timestamps. The default value is typically the system time zone. |
| vacuum _ defer cl _ eanup a _ ge | 0 | 0 | [0- 1000000] | No | Specifies the number of transactions by which VACUUM operations will defer the cleanup of dead tuples. This is used to reduce cleanup conflicts caused by concurrent transactions. The value can be 0 or a positive integer. The default value is 0, which means immediate cleanup. |

### 4.11 Manage tags

stances If you have a large number of instances, you can create multiple tags and add the tags to the instances. Then, you can query instances by tag. This topic describes how to manage tags.

**Usage notes**

A tag consists of a key-value pair. Each key must be unique for an account in a region. This limit does not apply to the values of keys. You can add up to 20 tags to an instance. If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.

**Add a tag**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, enter the tag key and tag value and click **OK**.

**Search for an instance by tag**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, click **Advanced Filter**.
3. You can search for your instance by **Instance ID/Name**, **VIP**, and **Filter by Tag**. Select a
tag from the **Filter by Tag** drop-down list.
4. After you select a tag, the instance list displays all instances that are bound with the tag.

**View the tags that are added to an instance**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, move the pointer over the
icon in the **Tag** column of the desired instance.

**Remove a tag**

1. Log in to the PolarDB console.
2. On the **List of local disk instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, click the
icon to the right of the tag and click **OK**. atabase connection

## 5 Database connection

### 5.1 View and manage instance endpoints and ports

**endpoints and ports**

This topic describes how to view and change the endpoint and port number of a database and configure the IPv6 feature.

**Endpoint overview**

PolarDB for PostgreSQL provides two types of endpoints to meet different network access requirements:

| Network type | Description |
|---|---|
| Private endpoint (VPC address) | When you create an instance, a default private endpoint is created. This endpoint can be modified but cannot be deleted. This endpoint can only be accessed from Elastic Compute Service (ECS) instances or resources that reside in the same virtual private cloud (VPC). When you access an instance over an internal network, PolarDB provides high security and optimal performance. |
| Public endpoint (public address) | You can apply for or release a public endpoint based on your business requirements. The public network, namely the Internet, is constrained by bandwidth limitations and security policies, resulting in lower performance compared with internal network access. |

**Usage notes**

If you change the endpoint or port number of your instance, you must update the endpoint or port number information on your application. If you do not update the information, your application cannot connect to your instance. After the endpoint or port number is changed, the change immediately takes effect. You do not need to restart the instance. After the public endpoint is released, it cannot be restored. A new endpoint is assigned if you reapply for a public endpoint. Switch workloads to the new endpoint in advance. Disable the IPv6 feature will interrupt all IPv6 client connections. Make sure that no IPv6 business traffic is active before you proceed.

**View the internal and public endpoints and port numbers**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the **Basic Information** section, view the internal and public endpoints and port numbers
of the instance. atabase connection You can also switch to the **Database Connection** page and view the internal and public endpoints and port numbers. The internal and public endpoints of an instance are displayed only after you configure IP address whitelists for the instance. For more information, see Configure an IP address whitelist. The public endpoint of an instance is displayed only after you apply for a public endpoint for the instance.

**Change the internal and public endpoints and port numbers**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. On the right side of the page, click **Modify the connection address**.
5. In the dialog box that appears, set **Connection type** to **Public network** or **VPC**.
6. Modify the endpoint prefix and port number and then click **OK**.
The prefix of the endpoint must contain letters, digits, hyphens (-), and periods (.). It must start with a letter and end with a letter or digit. The length of each segment of the domain name (separated by periods) cannot exceed 63 characters. The total length cannot exceed 253 characters. The port number must be 4 digits between 3000 and 5999.

**Apply for or release a public endpoint**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Apply for public network** or **Release the public network** to the right of the Public
network address field.

**Important**

You can decide whether to enable the IPv6 feature when applying for the public endpoint. A released endpoint cannot be restored and can only be reapplied for. Before you release an endpoint, make sure that your application is connected to the cluster by using another endpoint.
5. Click **OK**.

**Enable or disable the IPv6 feature**

atabase connection
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. Enable or disable IPv6.

**Important**

After you disable IPv6, the services that access the database by using an IPv6 address are disconnected from the database and interrupted. Before you proceed, make sure that no service is connected to the database by using an IPv6 address.
5. Click **OK**.

### 5.2 Connect to an instance

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an ApsaraDB RDS instance. Data Management (DMS) is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational and non-relational databases, such as MySQL, SQL Server, and PostgreSQL. It can also be used to manage Linux servers. You can also use a database client to connect to an ApsaraDB RDS instance. ApsaraDB RDS is fully compatible with PolarDB. You can connect to PolarDB instances in the similar manner as you would connect to an open source PolarDB database. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an ApsaraDB RDS instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Log on to an ApsaraDB for RDS instance by using DMS.

**Use the pgAdmin 4 client to connect to an ApsaraDB RDS**

**instance**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP whitelist.
2. Start the pgAdmin 4 client.
For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows).
3. Right-click **Servers** and choose **Create > Server**, as shown in the following figure.
4. On the **General** tab of the **Create - Server** dialog box, enter the name of the server, as
shown in the following figure.
5. Click the **Connection** tab and enter the information of the instance, as shown in the
following figure. atabase connection

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the ApsaraDB RDS instance. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the ApsaraDB RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |
| Username | The name of the privileged account for the ApsaraDB RDS instance. For more information about how to create an privileged account, see Create a database and an account. |
| Password | The password of the privileged account. |

6. Click **Save**.
7. If the connection information is correct, choose **Servers > Server Name > Databases >**
**postgres**. If the following page appears, the connection is established.

**Important**

The postgres database is the default system database of the ApsaraDB RDS instance. Do not perform operations on this database.

### 5.3 Use DMS to log on to a PolarDB for PostgreSQL instance that uses local disks

**PolarDB for PostgreSQL instance**

**that uses local disks**

This topic describes how to log on to a PolarDB for PostgreSQL instance by using Data Management (DMS).

**Prerequisites**

An IP address whitelist is configured. For details, see Configure an IP address whitelist.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page, click **Log On to Database**.
4. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
the **Database Type**, **Instance Region**, and **Connection String Address** parameters. If the values are correct, configure the **Database Account** and **Database Password** parameters.

| Parameter | Description |
|---|---|

atabase connection

| Database Type | The engine of the database. By default, the engine of the database to be connected is selected. |
|---|---|
| Instance Region | The region in which the instance is deployed. By default, the region of the current instance is selected. |
| Connection String Address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The account used to log on to the database. |
| Database Password | The password used to log on to the database. |

5. Click **Login**.
If you want the browser to save the password, select **Remember password** and then click **Login**.

### 5.4 Configure the hybrid access solution

**solution**

This topic describes how to configure the hybrid access solution for a PolarDB for PostgreSQL Primary/Secondary Edition cluster. This solution allows you to migrate your cluster from the classic network to a virtual private cloud (VPC) without network interruptions.

**Prerequisites**

The PolarDB for PostgreSQL cluster resides in the classic network. A VPC and a vSwitch are created in the zone in which the PolarDB for PostgreSQL cluster resides.

**Background information**

When you migrate a PolarDB for PostgreSQL cluster from the classic network to a VPC, the internal endpoint type changes from classic network to VPC. Although the endpoint string remains unchanged, the IP address bound to the endpoint changes. As a result, a temporary disconnection of about 30 seconds occurs, and Elastic Compute Service (ECS) instances in the classic network can no longer connect to the PolarDB for PostgreSQL cluster over an internal network. To ensure a smooth migration, PolarDB for PostgreSQL provides a hybrid access mode. Hybrid access means that your PolarDB for PostgreSQL cluster can be connected to ECS instances in both the classic network and VPCs. In hybrid access mode, the system retains the original internal endpoint of the classic network type and generates an internal endpoint of the VPC type for the PolarDB for PostgreSQL cluster. This prevents temporary disconnections during network type migration. atabase connection To improve security and performance, we recommend that you use only the internal VPC endpoint. You must specify a validity period for the hybrid access mode. After the validity period expires, the system releases the original internal endpoint of the classic network type, and applications can no longer connect to the cluster by using this endpoint. Before the validity period expires, you must update your applications to use the internal VPC endpoint. This ensures a smooth migration and prevents service interruptions. For example, during the validity period of the hybrid access mode, specific applications can connect to the cluster by using the internal VPC endpoint, while others continue to use the internal classic network endpoint. After all applications are updated to use the internal VPC endpoint, the internal classic network endpoint can be released. The following figure shows this scenario. Smooth Migration from Classic Network to VPC ECS ECS ECSECS ECS New ECS Instance ECS ECS ECS ECS ECS ECS ECS ECS New ECS In ECS ECS SQL SQL SQL SQL Classic Network

| Classic IP | VPC IP |
|---|---|

Classic IP VPC IP PolarDB PolarDB PolarDB VPC VPC Classic Hybrid Nt k A

**Limits**

After the hybrid access mode is enabled, your PolarDB for PostgreSQL cluster has the following limits: The network type of the cluster cannot be changed to classic network. The cluster cannot be migrated to another zone.

**Change the network type from classic network to VPC**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Switch over VPC**.
5. In the Switch over VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. Select Yes or No for **Retain the original classic network**.
**No**: The classic network endpoint is not retained and changes to a VPC endpoint.
atabase connection When you change the network type from the classic network to a VPC, a temporary disconnection of approximately 30 seconds occurs, and all internal network connections from classic network ECS instances to the PolarDB for PostgreSQL cluster are closed.
**Yes**: The classic network endpoint is retained, and a new VPC endpoint is generated. In
this case, your PolarDB for PostgreSQL cluster runs in hybrid access mode. Both classic network-type and VPC-type ECS instances can access your cluster over an internal network. If you change the network type from the classic network to a VPC, no temporary disconnections occur. Internal network connections from classic network ECS instances to the PolarDB for PostgreSQL cluster remain available until the classic network endpoint expires. Specify the validity period of the classic network endpoint. Before the classic network endpoint expires, you must add the new VPC endpoint to applications that run on ECS instances in the selected VPC. This allows PolarDB for PostgreSQL to migrate your workloads to the selected VPC without network interruptions.
6. Add the private IP address of the required ECS instance to the whitelist of the PolarDB for
PostgreSQL cluster. This allows the ECS instance to connect to the cluster over the internal network. If no IP address whitelists of the VPC network type are available, create one. For more information, see Configure an IP address whitelist.

### 5.5 Change the network type of an instance

**an instance**

This topic describes how to change the network type of a PolarDB instance between classic network and VPC.

**Background information**

Classic network: PolarDB instances in the classic network are not isolated. You can block unauthorized access only by configuring IP address whitelists on these instances. VPC: Each VPC is an isolated network. A VPC provides higher security than the classic network. We recommend that you select the VPC network type. You can configure route tables, CIDR blocks, and gateways in a VPC. To smoothly migrate applications to the cloud, you can use leased lines or VPNs to connect your data center to a VPC to create a virtual data center.

**Change the network type from VPC to classic network**

Precautions After you change the network type from VPC to classic network, the internal endpoint of the PolarDB instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, you cannot connect Elastic Compute Service (ECS) instances deployed in VPCs to the PolarDB instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. When you change the network type, a 30-second network interruption may occur. To avoid business interruption, change the network type during off-peak hours or make sure that your applications are configured with automatic reconnection policies.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
atabase connection
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to Classic**
**Network**.
6. In the dialog box that appears, click **OK**.
After the network type is changed to classic network, only ECS instances within the classic network can connect to the PolarDB instance by using the internal endpoint. You must configure the internal endpoint for the ECS instances.
7. Configure a whitelist to allow ECS instances within the classic network to connect to the
PolarDB instance by using the internal endpoint.

**Change the network type from classic network to VPC**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to VPC**.
6. In the Switch to VPC dialog box, select a VPC and vSwitch and specify whether to retain the
endpoint used in the classic network. atabase connection Select a VPC. We recommend that you select the VPC where your ECS instances are deployed. Otherwise, the ECS instances cannot communicate with the PolarDB instance over the internal network. Select a vSwitch. If no vSwitches are available in the selected VPC, create one in the same zone where the PolarDB instance is deployed. For more information, see Create a vSwitch in Quick Start of **VPC User Guide**. Determine whether to select the **Reserve Original Classic Network Endpoint** option. The following table describes the details.

**Not selected**

The classic network endpoint is not retained, and the endpoint of the instance changes to a VPC endpoint. When you change the network type, a 30-second network interruption may occur, and connections between ECS instances in the classic network and the PolarDB instance are interrupted.

**Selected**

The classic network endpoint is retained, and a new VPC endpoint is generated. In such cases, the PolarDB instance runs in hybrid access mode. ECS instances in both the classic network and a VPC can connect to the PolarDB instance over an internal network. When you change the network type, no network interruptions occur. Connections between ECS instances in the classic network and the PolarDB instance remain available until the classic network endpoint expires. To migrate your business to the VPC without interruption, you must add the VPC endpoint to access the ECS instances before the classic network endpoint expires. Seven days before the classic network endpoint expires, the system sends a text message to the phone number bound to your Apsara Stack account every day. For more information, see Hybrid access from both the classic network and VPCs.
7. Add the internal IP addresses of ECS instances in the selected VPC to a VPC whitelist. This
allows the ECS instances to access the PolarDB instance over the internal network. If no VPC whitelists are available, create a whitelist. If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires. If you do not retain the classic network endpoint, connections between ECS instances in the classic network and the PolarDB instance over the internal network are interrupted. You must add the new endpoint to ECS instances in the VPC immediately after the network type is changed. counts

## 6 Accounts

### 6.1 Create an account

After you create a PolarDB for PostgreSQL instance and configure a whitelist, you must create a database account to connect to the instance and manage data. This topic describes how to create privileged and standard accounts.

**Background information**

You can create privileged and standard database accounts on a PolarDB for PostgreSQL instance. You can manage all accounts in the PolarDB console. For more information about permissions that can be granted to each type of account, see the Account permissions section of this topic.

| Account type | Description |
|---|---|
| Privileged account | You can create and manage privileged accounts in the PolarDB console or by calling API operations. You can create multiple privileged accounts for each instance. You can use privileged accounts to manage all standard accounts and databases of the instance. The first privileged account that you create is the owner of the default public schema of the standard system database named template1. By default, the CREATE DATABASE statement creates a database by replicating the template1 system database. The first privileged account owns the public schema of all databases that are created by using this statement. A privileged account allows you to manage permissions in a fine-grained manner. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect all accounts of the instance to which it belongs. |
| Standard account | You can create and manage standard accounts in the PolarDB console, by calling API operations, or by using SQL statements. You can create multiple standard accounts for each instance. You must grant standard accounts the required permissions on specific databases. A standard account does not have the permissions to create, manage, or disconnect other accounts. |

**Usage notes**

You can create multiple privileged accounts and standard accounts in the console. You can also create and manage standard accounts by using SQL statements. Before you migrate data from an on-premises database to a PolarDB for PostgreSQL instance, you must create a database with the same name and an account with the same username and password in the PolarDB for PostgreSQL instance. counts We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple database accounts and grant each account only the permissions to access the data of specified databases. This way, you can implement fine-grained permission management. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for accounts and change the passwords on a regular basis.

**Create a privileged account**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**. On the page that appears, click **Create**
**Account**.
4. Configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Database Account | The name of the account. The name must meet the following requirements: It can contain keywords such as root. It must be 1 to 32 characters in length. It must start with a letter and end with a letter or a digit. It can contain lowercase letters, digits, and underscores ( ). _ |
| Account Type | The account type. Select High privilege account. |

counts

| New Password | The password of the account. The name must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ Note PolarDB supports custom password constraints. To implement custom password constraints, configure a custom password policy in the Apsara Uni- manager Operations Console. Then, error messages are displayed when users enter non-compliant passwords. For more information, see Configure a custom password policy for PolarDB in the O&M Guide. If you do not have the permissions on the Apsara Uni-manager Operations Console, contact Alibaba Cloud technical support. |
|---|---|
| Confirm Password | The password of the account. Enter the password again to confirm it. |
| Remarks | This parameter is optional. Enter a description that is used to identify the account to facilitate account management. The description can be up to 256 characters in length. |

**Reset of the permissions of a privileged account**

If an issue occurs in a privileged account, you can enter the password of the privileged account to reset its permissions. For example, you can reset the permissions if the permissions are accidentally revoked.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the privileged account that you want to reset and click **Reset account permissions**
in the **Operation** column.
5. In the dialog box that appears, enter the password of the privileged account and click **OK**.

**Create a standard account**

1. Log in to the PolarDB console.
counts
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**. On the page that appears, click **Create**
**Account**.
4. Configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Database Account | The name of the account. The name must meet the following requirements: It can contain keywords such as root. It must be 1 to 32 characters in length. It must start with a letter and end with a letter or a digit. It can contain lowercase letters, digits, and underscores ( ). _ |
| Account Type | The account type. Select Ordinary account. |
|   | The authorized databases of the account. You can specify one or more authorized databases. You can also leave this parameter empty at this time and authorize databases after the account is created. i. In the Unauthorized database section, select one or more databases. Then, click the icon to move the selected databases to the Authorized Database section. |

counts

| Authorizatio n Database |   | ii. In the Authorized Database section, select Owner or Create permissions for each database. If you want to grant the same permissions on multiple databases to the account at a time, click the button in the upper-right corner of the section. For example, select Owner or Create permissions for all databases. Comparison of permissions between CREATE and OWNER GRANT CREATE ON DATABASE db TO user only grants a user permission to create new schemas within that database. It does not automatically grant permission to create objects (such as tables) in existing schemas (such as public ). The database owner has full control over the database, including lifecycle management, parameter configuration, permission assignment, and access to all objects within the database. Database CREATE Database OWNER Capability permission permission Create a new schema. √ √ |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   |   | Capability |   | Database CREATE permission | Database OWNER permission |
|   |   |   | Create a new schema. |   | √ | √ |
|   |   |   | Create a table in a public schema. |   | × (The user is granted the CREATE permission on the public schema.) | √ |
|   |   |   | Modify database parameters (using ALTER DATABASE SET ). |   | × | √ |
|   |   |   |   | ALTER DATABASE |   |   |
|   |   |   | SET |   |   |   |
|   |   |   | Rename or delete a database. |   | × | √ |
|   |   |   | Grant database permissions to others. |   | × | √ |

counts

| New Password | The password of the account. The name must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ Note PolarDB supports custom password constraints. To implement custom password constraints, configure a custom password policy in the Apsara Uni- manager Operations Console. Then, error messages are displayed when users enter non-compliant passwords. For more information, see Configure a custom password policy for PolarDB in the O&M Guide. If you do not have the permissions on the Apsara Uni-manager Operations Console, contact Alibaba Cloud technical support. |
|---|---|
| Confirm Password | The password of the account. Enter the password again to confirm it. |
| Remarks | This parameter is optional. Enter a description that is used to identify the account to facilitate account management. The description can be up to 256 characters in length. |

**Account permissions**

| Permission | Privileged account | Standard account |
|---|---|---|
| CREATEDB | √ | × |
| CREATEROLE | √ | × |
| REPLICATION | √ | × |
| SELECT | √ | √ |
| INSERT | √ | √ |
| UPDATE | √ | √ |
| DELETE | √ | √ |
| TRUNCATE | √ | √ |

counts

| REFERENCES | √ | √ |
|---|---|---|
| CREATE | √ | √ |
| CONNECT | √ | √ |
| TEMPORARY | √ | √ |
| EXECUTE | √ | √ |
| USAGE | √ | √ |

### 6.2 Reset the password

This topic describes how to use the PolarDB for PostgreSQL console to reset the password of your account if you forget the password.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to manage and click **Reset Password** in the Operation
column.
5. In the dialog box that appears, enter and confirm the new password, and then click **OK**.
The password must meet the following requirements: It must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! @ # $ % ^ & * ( ) _ + - =

### 6.3 Delete an account

You can delete a database account in the PolarDB console.

**Prerequisites**

counts You can use the console to delete privileged and standard accounts that are no longer used.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to delete and click **Delete** in the Operation column.
5. In the message that appears, click **OK**.
Accounts in the processing state cannot be deleted.

### 6.4 Lock an account

You can lock a database account in the console.

**Prerequisites**

You can use the console to lock privileged and standard accounts that are no longer used.

**Lock an account**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to lock and click **Lock** in the Operation column.
5. In the message that appears, click **OK**.

**Unlock an account**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to delete and click **Unlock** in the Operation column.
5. In the message that appears, click **OK**.
atabases

## 7 Databases

### 7.1 Create a database

Before you get started with aPolarDB for PostgreSQL cluster, you must create a database for the cluster. This topic describes how to create a database on a PolarDB for PostgreSQL cluster.

**Prerequisites**

A PolarDB for PostgreSQL cluster is created. For more information, see Create an instance.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page, click **Log On to Database**.
4. In the **Log on to Database Instance** dialog box of the **Data Management (DMS)**
console, check the values of the **Database Type**, **Instance Region**, and **Connection**
**string address** parameters. If the values are correct, specify the **Database Account** and
**Database Password** parameters.

| Parameter | Description |
|---|---|
| Database Engine Type | The engine of the database. By default, the engine of the database to be connected is selected. |

atabases

| Instance Region | The region in which the instance is deployed. By default, the region of the current instance is selected. |
|---|---|
| Connection String Address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The account used to log on to the database. |
| Database Password | The password of the database account. |

5. Click **Login**. If you want the browser to save the password, select **Remember password**
before you click **Login**. If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
6. The **SQLConsole** page appears after you log on to the instance. Execute a statement in the
following format to create a database:

```
CREATE DATABASE name
 [ [ WITH ] [ OWNER [=] user_name ]
        [ TEMPLATE [=] template ]
        [ ENCODING [=] encoding ]
        [ LC_COLLATE [=] lc_collate ]
        [ LC_CTYPE [=] lc_ctype ]
        [ TABLESPACE [=] tablespace_name ]
        [ CONNECTION LIMIT [=] connlimit ] ]
```

For example, if you want to create a database named test, execute the following statement:

```
create database test;
```

7. Click **Execute**.

### 7.2 Delete a database

This topic describes how to delete a database from a PolarDB instance.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page, click **Log On to Database**.
atabases
4. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
the **Database Type**, **Instance Region**, and **Connection String Address** parameters. If the values are correct, specify the **Database Account** and **Database Password** parameters.

| Parameter | Description |
|---|---|
| Database Engine Type | The engine of the database. By default, the engine of the database to be connected is selected. |
| Instance Region | The region in which the instance is deployed. By default, the region of the current instance is selected. |
| Connection String Address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The account used to log on to the database. |
| Database Password | The password of the database account. |

5. Click **Login**. If you want the browser to save the password, select **Remember password**
before you click **Login**. atabases If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
6. The **SQLConsole** page appears after you log on to the PolarDB for PostgreSQL instance.
Execute the following statement to delete the database:

```
drop database <database name>;
```

7. Click execute.
onitoring

## 8 Monitoring

### 8.1 View monitoring data

PolarDB provides a wide range of performance metrics. This topic describes how to view resource monitoring data in the PolarDB console.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Monitor** tab, select a time range to query the corresponding monitoring data. The
following table lists the specific metrics.

| Monitoring metric | Description |
|---|---|
| Memory Usage | The memory usage of the instance. |
| CPU Utilization | The CPU utilization of the instance. |
| IOPS | The number of IOPS of the data and log disks. |
| On-premises Storage Capacity | The on-premises storage space of the instance. |
| Network | The amount of data received and sent over the network of the instance. |
| Retransmission | The number of retransmissions over the network of the instance. |
| Connections | The total number of connections, number of active connections, number of pending connections, and number of idle connections of the instance. |
| Scanned Rows | The number of rows that are read, inserted, updated, returned, and deleted per second on the instance. |
| TPS | The number of transactions processed per second by the instance. |
| Duration of Current Longest Transaction | The duration of the longest transaction currently running in the instance. |

onitoring

| Latency | The sending latency of the primary database, replay latency of the secondary database, and logical replication latency of the instance. |
|---|---|
| Slow SQL Queries | The information about slow SQL queries of the instance. |
| Long-running Transactions | The number of long-running transactions for the instance. |
| Long-running XA Transactions | The number of long-running XA transactions for the instance. |

### 8.2 Configure an alert rule

This topic describes how to create alert rules in the PolarDB console. This allows you to identify and handle exceptions at the earliest opportunity.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Alert** tab, click **Alert Rule Settings**.
5. On the **Alert Rule** page, click **Create an alert rule**.
6. In the **Create an alert rule** panel, configure the following parameters:

| Parameter | Description |
|---|---|
| Cloud product selection | PolarDB for PostgreSQL Primary/Secondary Edition |
| Resource scope | The resources to which the alert rule applies. Valid values: Instance dimension: Select one or more instances in the resource set of the current organization. Resource set dimension: Select a resource set in the current organization and region. Application grouping dimensions: Select an application group in the current organization and region. All resources: The alert rule applies to all resources of the specified cloud service. |
| Resource Selection | The resources to be associated with the alert rule. Select one or more resources based on the selected resource type. |

onitoring

| Alarm rule description | The trigger conditions of the alert rule. If the monitoring data meets the specified conditions, the alert rule is triggered. To configure the trigger conditions, perform the following steps: i. Click Rule description. ii. In the Rule description panel, configure the Rule name, Monitoring Metrics, Metric dimension, and Threshold and alarm level parameters. Note The Metric dimension parameter is displayed only if you set the Resource scope parameter to Instance dimension. iii. Click OK. |
|---|---|
| Silence channel period | The mute period after which CloudMonitor resends an alert notification before the alert is cleared. Valid values: 5 minutes, 15 minutes, 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, and 24 hours. An alert is triggered if the conditions of an alert rule are met. CloudMonitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, CloudMonitor resends alert notifications. For example, if you set the Silence channel period parameter to 12 hours, CloudMonitor resends alert notifications only if the alert still persists after 12 hours. |
| Effective time | The validity period of the alert rule. CloudMonitor checks whether the monitoring data triggers the alert rule only during the effective period. |
| Alarm callback | The callback URL to which CloudMonitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for CloudMonitor. You can enter only an HTTP URL. IP addresses are not supported. |
| No data processing method | Specify how CloudMonitor acts when no alert is triggered. Valid values: No processing: CloudMonitor does not perform any operations when no alert is triggered. Send no data alarm: CloudMonitor sends the corresponding notifications to contacts when no alert is triggered. |
| Alarm contact | The alert contacts or alert contact groups to which CloudMonitor sends alert notifications. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

7. After you complete the configuration, click **OK**.
oud Monitor

## 9 Cloud Monitor

### 9.1 View performance metrics

PolarDB for MySQL V2.0 provides rich performance metrics and second-level monitoring frequency, which allow you to easily track the status of clusters and address operational challenges.

**View the dashboard**

1. Log in to the PolarDB for MySQL V2.0 console.
2. On the **Instances Using Local Disks** page, find the cluster that you want to manage and
click its ID.
3. In the left-side navigation pane, click **CloudMonitor**.
4. You can view metrics related to **computing resources**, **disks**, **networks**, **deadlocks**,
and **read-only instances**. View performance metrics

**View monitoring information**

1. Log in to the PolarDB for MySQL V2.0 console.
2. In the left-side navigation pane, click **CloudMonitor**.
3. In the **time granularity** drop-down list, select **1 Minute** or **1 Hour** (default value) as the
data collection interval.

### 9.2 Alert history

After an alert is triggered, you can view its history. You can also export and download the alert history for local data analytics.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **Cloud Monitor** and choose **Alert Service** > **Alert**
**History**.
4. (Optional) On the **Alert History** page, filter the alert history by **Rule ID**, **Rule Name**, **Alert**
**Level**, and time.
5. On the Alert History page, you can perform the following tasks.

| Task | Procedure |
|---|---|
| View alert history | In the Alert History list, view the Product Name, Affected Instance, Time, Rule Name, Status, Level, and Notification Recipient. Click the rule name to view the details of the alert rule. Note By default, you can query alert history data from the last 2 days. |

oud Monitor

| Export alert history | i. On the Alert History page, click in the upper-right corner. ii. In the Export Task dialog box, set Time Range and Task Name. Then, click OK. |
|---|---|

### 9.3 Alert rules

#### 9.3.1 Create an alert rule

Create an alert rule that triggers alerts for a cloud service based on specified metric thresholds and promptly notifies relevant users.

**Background information**

During its effective period, an alert rule checks at a default detection frequency if a metric exceeds the specified threshold. If a metric exceeds the threshold and becomes abnormal, an alert is sent to the specified alert contacts or other alert processing platforms. The minimum alert detection frequency is once per minute.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **CloudMonitor**, and then choose **Alert Service** >
**Alert Rules**.
4. Above the list, click **Create Alert Rule**.
5. In the **Create Alert Rule** panel, set the parameters as needed.

| Parameter | Description |
|---|---|
| Cloud Service Selection | This is set by default and does not need to be selected. |
| Resource Scope | The scope of resources associated with the alert rule. The following types are supported. The available scope types may vary by cloud service. Instance: Select one or more target instances from the resource set of the current organization. Resource Set: Select a target resource set in the current organization and region. Application Group: Select an application group in the current organization and region. All Resources: This option is not supported by default. |

oud Monitor

| Resource Selection | Based on the selected Resource Scope, select a specific resource instance, resource set, or application group. |
|---|---|
| Alert Rule Description | The main body of the alert rule. The rule is triggered when monitoring data meets the alert conditions. To set the rule description: i. Click Create Alert Rule. ii. In the Create Alert Rule panel, set the Rule Name, Metric Dimension, Monitoring Metric, Threshold, AndAlert Level. Note The Metric Dimension parameter is displayed only when Resource Scope is set to Instance. iii. Click Confirm. |
| Mute For | The interval at which to resend an alert notification if the alert is not resolved. Valid values: 5 Minutes, 15 Minutes, 30 Minutes, 1 Hour, 3 Hours, 6 Hours, 12 Hours, and 24 Hours. When a metric exceeds the alert threshold, an alert is triggered. If the metric continues to exceed the threshold during the mute period, no more alert notifications are sent. If the metric has not recovered after the mute period, CloudMonitor sends another alert notification. For example, if Mute For is set to 12 Hours, CloudMonitor sends another alert notification if the metric that exceeded the threshold has not recovered 12 hours after the first alert was triggered. |
| Effective Period | The period during which the alert rule is active. The rule only checks if monitoring data exceeds the alert threshold during this period. |
| Alert Callback | A webhook address that receives alert messages pushed by CloudMonitor through POST requests. Note The webhook address must be a domain name accessible to CloudMonitor. Only the HTTP protocol is supported. You cannot enter an IP address. |
| No Data Handling Method | The method for handling alerts when there is no monitoring data. Do Nothing Send No-data Alert |
| Alert Contact | Select the user group or user to whom alert messages are sent. The default alert contact group for an Alibaba Cloud account is an empty group. You can use it to test the validity of an alert rule. |

6. Click **OK**.
oud Monitor

**Rule description parameters**

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the alert rule. |
| Monitoring Metric | From all the metrics available for the selected cloud service, select the target metric. For more information about the metrics for each cloud service, see the relevant monitoring documentation. |
| Metric Dimension | Refers to dimensions other than the instance ID. This parameter is displayed only when Resource Scope is set to Instance. |
| Threshold And Alert Level (unit: %) | The alert levels are Critical, Warning, and Info. The aggregation method for monitoring data can be Average, Minimum, or Maximum. You can set the monitoring data epoch to 1 Consecutive Epoch, 5 Consecutive Epochs, 10 Consecutive Epochs, 15 Consecutive Epochs, 30 Consecutive Epochs, or 60 Consecutive Epochs. The comparison operator between the actual monitoring data and the alert threshold. Supported operators include “>”, “ >=”, “<”, “<= ”, “=”, “!=”, “Day-on-day Increase”, “Day-on-day Decrease”, “Period-on-period Increase”, “period-on-period Decrease”, “increase From Last Period”, and “decrease From Last Period”. You can also set a threshold and the number of times it must be met to trigger an alert. |

**Example configuration**

This example creates an alert rule named "example" for an Elastic Compute Service (ECS) instance to monitor its CPU utilization. The rule triggers a Critical alert if the maximum CPU utilization is greater than or equal to 70% for three occurrences within five detection periods. The following figure shows the rule description configuration for this scenario. oud Monitor

#### 9.3.2 Manage alert rules

From the list of alert rules, you can modify, enable, disable, and delete rules.

**Procedure**

1. Log on to the ApsaraDB for Tair (Redis-compatible) console.
2. On the **Instance List** page, click the ID of the instance.
3. In the navigation pane on the left, click **Cloud Monitor** and then choose **Alert Service**>
**Alert Rules**.
4. Find the desired alert rule and perform the required operation.

| Task | Procedure |
|---|---|
| View alert rule details | In the Operation column of the target alert rule, click Details to view the rule details on the Alert Rule/Alert History/Faulty Resources panel. |

oud Monitor

| Check rule validity | In the Validity column of the target alert rule, click Click To Inspect. The inspection result is displayed in the Validity column. Note If the inspection result is abnormal, click Detection Result. In the panel that appears, view the results for Alert Rule Execution Anomaly Detection, Alert Rule Load Detection, Invalid Alert Rule Detection, and Alert Rule Callback Detection. Click Re-detect to check the rule validity again. |
|---|---|
| View rule execution records | In the Rule Execution Record column of the target alert rule, click View Rule Execution Record. On the Alert Rule Execution Record panel, filter the execution records by time range. |
| Modify an alert rule | i. In the Operation column of the target alert rule, click Edit. ii. On the Modify Alert Rule panel, modify the alert rule. For more information about the configuration parameters, see Create an alert rule. iii. After you finish the modification, click OK. |
| Disable an alert rule | Disable alert rules when you manually stop a cloud product for maintenance or an upgrade. This prevents unnecessary alert notifications. Note Before disabling an alert rule, make sure that its Status is Normal. Disable a single rule a. In the Operation column of the target alert rule, click the icon, and then click Disable. b. In the Disable Alert Rule dialog box, click OK. Disable rules in a batch a. Select the check boxes next to the target alert rules, and then click Disable in the lower-left corner of the list. b. In the Disable Alert Rule dialog box, click OK. |

oud Monitor

| Enable an alert rule | After you finish the maintenance or upgrade of a cloud product, re-enable the disabled alert rules. Note Before enabling an alert rule, make sure that its Status is Disabled. Enable a single rule a. In the Operation column of the target alert rule, click Enable. b. In the Enable Alert Rule dialog box, click OK. Enable rules in a batch a. Select the check boxes next to the target alert rules, and then click Enable in the lower-left corner of the list. b. In the Enable Alert Rule dialog box, click OK. |
|---|---|
| Delete an alert rule | Delete a single rule a. In the Operation column of the target alert rule, click the icon, and then click Delete. b. In the Delete Alert Rule dialog box, click OK. Delete rules in a batch a. Select the check boxes next to the target alert rules, and then click Delete in the lower-left corner of the list. b. In the Delete Alert Rule dialog box, click OK. |

ata security

## 10 Data security

### 10.1 Configure an IP address whitelist

**whitelist**

This topic describes how to configure an IP address whitelist for a PolarDB for PostgreSQL Primary/Secondary Edition instance to control which sources can access the database. You can also specify the network type (IPv4 or IPv6) when adding a whitelist group, meeting the need for fine-grained access control in mixed-protocol stack environments.

**Background information**

The IP whitelist is a core security mechanism for the PolarDB for PostgreSQL Primary/Secondary Edition instance. You can explicitly authorize trusted IP addresses or CIDR blocks to effectively block unauthorized access. We recommend that you regularly maintain the whitelist policy to follow the principle of least privilege. Configuring the whitelist does not affect normal instance operations. You can use the following methods to configure a whitelist: Configure an IP whitelist: Add IPv4 or IPv6 addresses and CIDR blocks to allow access from specific clients. Configure an Elastic Compute Service (ECS) security group: Associate an ECS security group, which automatically allow access from all ECS instances in the group (only for instances in the same region and with the same network type). If an ECS instance needs to access a PolarDB instance by using an internal endpoint, make sure that the two instances reside in the same region and have the same network type (such as VPC). Otherwise, the connection will fail even if the whitelist is correctly configured.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** .
4. On the **Whitelist Settings** tab, perform one of the following operations:
Edit the default group: locate the `default` group and click **Edit** in the Operation column. To create a custom whitelist, click **Add a whitelist group**. You can specify IPv4 or IPv6 as the network type to implement protocol stack isolation.
5. In the panel that appears, you can:
Delete an existing IP address or CIDR block. Click **Add** and enter the IP address or CIDR block to be authorized. For example, `10.10.10.0/24` indicates that the `10.10.10.x` range is allowed. ata security Separate multiple entries with commas (,). Do not contain spaces before or after the commas. Example: `192.168.0.1,172.16.213.9,2001:db8::/32` . Click **Load the internal IP address of the ECS instance** . The internal IP addresses of all ECS instances under the current account are automatically listed for quick selection. Click **Import File (.txt)** to import IP addresses in the `.txt` format. After you add an IP address to the `default` group, the system automatically removes the default reserved address `127.0.0.1` . Once the network type of the custom group is selected, it cannot be changed. Configure it carefully based on the actual service protocol stack.

### 10.2 Configure SSL encryption

This topic describes how to make data transmission more secure by configuring Secure Sockets Layer (SSL) encryption. You must enable SSL encryption and install SSL certificates that are issued by certificate authorities (CAs) to the required applications. SSL is used to encrypt connections at the transport layer and enhance the security and integrity of the transmitted data. However, SSL encryption increases the round-trip time.

**Usage notes**

The validity period of an SSL certificate is one year. If an SSL certificate is about to expire, renew the certificate at the earliest opportunity and then download and configure the certificate again. Otherwise, clients may fail to connect to the cluster over SSL. For more information about how to renew a certificate, see the Renew an SSL certificate section of this topic. SSL may significantly increase the CPU utilization. We recommend that you enable SSL only if you want to encrypt connections that are established to the public endpoint of your cluster. In most cases, connections that are established to the internal endpoint of your cluster are secure and do not require SSL encryption. This operation restarts your cluster. Proceed with caution.

**Enable SSL encryption and download an SSL certificate**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** to go to the **Data Security** page.
4. On the **SSL** tab, select a certificate type, which can be **Cloud Certificate** or **Custom**
**Certificate**.
5. In the certificate type section, click **Configuration** to the right of **Configure Database**
**Certificate (to Prevent Database Disguise)** to enable SSL encryption.
6. In the dialog box that appears, select the endpoint that you want to protect. If you select
**Custom Certificate**, specify **Server Certificate** and **Private Key of Server Certificate**,
and click **OK**. ata security After you configure the server certificate, the certificate is automatically updated and your cluster will be restarted. Before you renew the certificate, make sure that your businesses are not interrupted by this operation.
7. After **SSL Encryption** displays **Enabled** and **Configuration Status** displays **Successful**,
click **Download CA Certificate**. The package that you download contains the following files: P7B file: contains the CA certificate that can be imported to a Windows operating system. PEM file: contains the CA certificate that can be imported to an operating system other than Windows or an application that is not run on Windows. JKS file: the Java truststore file. The password is apsaradb. The file is used to import the CA certificate chain to Java programs. If you want to use a JKS certificate file in Java, you must modify the default JDK security configuration in JDK 7 and JDK 8. In the `jre/lib/security/java.security` file of the server that connects to the PolarDB for PostgreSQL cluster, modify the following two configurations:

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

If you do not modify the configurations, the following error is returned. In most cases, other similar errors are also caused by invalid Java security configurations:

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

**Renew an SSL certificate**

After you change the endpoint that has SSL encryption enabled or when the SSL certificate is about to expire, you must renew the SSL certificate. This section describes how to renew an SSL certificate.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** to go to the **Data Security** page.
4. In the certificate type section of the On the **SSL** tab, click **Modify** to the right of **Configure**
**Database Certificate (to Prevent Database Disguise)** to renew the certificate.
The renewal operation will restart the cluster. Proceed with caution.
5. After the SSL certificate is renewed, download and configure the SSL certificate again.
ata security For more information about how to download an SSL certificate, see Step 7 in the Enable SSL encryption and download an SSL certificate section of this topic.

**Configure a client CA certificate or client certificate revocation**

**list file**

After SSL encryption is enabled, you can configure a client CA certificate to verify the identity of the client. You can also add a client certificate revocation list file to verify the validity of the issued certificate in order to maximize database access security.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** to go to the **Data Security** page.
4. In the **Configure Client CA Certificate** section of the **SSL** tab, click **Enable Client CA**
**Certificate**. In the dialog box that appears, enter the public key of the client CA certificate
and click **OK**. After you modify the client CA certificate, the cluster is automatically restarted. Make sure that your business is not interrupted.
5. After the client CA certificate is enabled, you can configure the client certificate revocation
list file. In the **Upload or Update Revocation File of Client Certificate** section, click
**Enable Certificate Revocation File**. In the dialog box that appears, enter the content of
the file and click **OK**. After you modify the client certificate revocation list file, the cluster is automatically restarted. Make sure that your business is not interrupted.
6. Optional. After the certificate is uploaded, you can click **View Client CA Certificate**
**Details** to confirm the current certificate configuration. If the certificate is no longer used,
click **Clear Client CA Certificate** or **Clear Certificate Revocation File**.

**Configure the ACL level**

After SSL encryption is enabled, you can configure the ACL level for connecting clients to the database over SSL.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** to go to the **Data Security** page.
4. On the **SSL** tab, click **Modify** to the right of **Configure ACL**. In the dialog box that appears,
select an SSL authentication method. ata security After you configure the ACL, the cluster automatically restarts. Make business arrangements and proceed with caution. Select **verify-ca**, **verify-full**, or **cert** only after you configure the client CA certificate or client certificate revocation list file. For more information, see the Configure a client CA certificate or client certificate revocation list file section of this topic.
**prefer**: preferentially encrypts the data link. You can connect clients to the cluster over
SSL connections based on your business requirements.
**required**: encrypts the data link. This method denies non-SSL client connections, allows
access to the database through password authentication, and does not force client/server certificate verification or certificate CN consistency verification.
**verify-ca**: encrypts the data link and performs client authentication.
**verify-full**: encrypts the data link, performs client authentication, and checks whether
the certificate CN matches the database username.
**cert**: uses certificate authentication instead of password authentication, encrypts the
data link, performs client authentication, and checks whether the certificate CN matches the database username.

**Disable SSL encryption**

After you disable SSL encryption, the cluster is restarted. We recommend that you disable SSL encryption during off-peak hours. After you disable SSL encryption for a cluster, the performance of your cluster is improved but data security is compromised. We recommend that you disable SSL encryption only in secure environments.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security** to go to the **Data Security** page.
4. On the **SSL** tab, click **Disable SSL** to the right of **SSL Encryption** to disable SSL
encryption.
5. In the dialog box that appears, click **OK**.

### 10.3 Configure TDE

PolarDB supports the Transparent Data Encryption (TDE) feature. TDE encrypts and decrypts data files in real time. It encrypts data files when they are written to disks, and decrypts data files when they are loaded to the memory from disks. After you enable TDE for your instance, the size of data files in your instance does not increase. You can use TDE without the need to modify the configurations of your application.

**Background information**

ata security TDE performs data-at-rest encryption at the database layer. This prevents potential attackers from bypassing the database to read sensitive information from storage. TDE can encrypt sensitive data within tablespaces and data stored in disks and backups. TDE also automatically decrypts data to plaintext for applications and users that have passed the database authentication. The operating system and unauthorized users are not allowed to access the encrypted data in plaintext form. To use the TDE feature, you must also purchase Key Management Service (KMS). PolarDB does not provide the keys or certificates that are required for encryption. You can authorize PolarDB to use the keys that are automatically generated by Alibaba Cloud or the keys that are generated by using your own key information.

**Precautions**

After you enable TDE, you cannot disable TDE. You can enable TDE only when you create a PolarDB instance. In I/O bound workload scenarios, TDE may affect database performance after it is enabled. If you use an existing custom key for TDE, take note of the following information: If you disable the key, configure a plan to delete the key, or delete the key material, the key becomes unavailable. After you revoke the key that is authorized for a PolarDB instance, the instance becomes unavailable after it is restarted. You must use an Alibaba Cloud account or an account to which the AliyunSTSAssumeRoleAccess policy is attached.

**Enable TDE**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, click **Create an instance** in the upper-right corner.
3. On the page that appears, configure the required parameters and enable TDE.
For more information about the parameters for creating an instance, see Create an instance.
4. Click **Submit**.

**View TDE status**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. On the page that appears, click the **TDE** tab. View **TDE Status**.

### 10.4 SQL audit

PolarDB supports an SQL audit feature that you can use to view SQL details and periodically audit SQL records.

**Notes**

ata security The SQL audit feature is disabled by default. You must enable it manually. You cannot view SQL records generated before the sql audit feature was enabled. SQL audit logs are retained for 30 days. Exported SQL audit files are retained for two days. Files older than two days are automatically deleted. Enabling the SQL audit feature does not affect instance performance.

**View SQL audit information**

1. Log on to the ApsaraDB for PolarDB console.
2. On the **instance list** page, click the ID of the target instance or click **manage** in the
**actions** column, which takes you to the **basic information** page.
3. In the left-side navigation pane, click **data security**.
4. Click the **sql audit** tab.
You can query SQL information by criteria such as time range, database name, database user, and keywords. You can also sort the results by Top SQL execution time.

**Disable SQL audit**

If you no longer need to audit SQL activity, you can disable the sql audit feature.

**Important**

Disabling the sql audit feature permanently deletes all sql audit records, including historical data. Before you disable this feature, we recommend exporting the audit logs and saving them locally.
1. Log on to the ApsaraDB for PolarDB console.
2. On the **instance list** page, click the ID of the target instance or click **manage** in the
**actions** column, which takes you to the **basic information** page.
3. In the left-side navigation pane, click **data security**.
4. Click the **sql audit** tab.
5. Select a time range for the data that you want to export, and then click **export data >**
**create export data task** . The system exports the SQL records that match the current
filter criteria. Save the exported file locally. To view exported files, click **export data > view exported file list**. In the dialog box that appears, you can view information such as the file name, creation time, file status, and file size.
6. After you export the file, click **disable sql audit** in the upper-right corner of the page.
7. In the dialog box that appears, click **OK**.

**Change audit log storage location**

By default, audit logs are stored in an internal SLS instance (SLS-inner). Writing a large volume of audit logs to this instance can create performance pressure and affect the stability of the Apsara Stack control plane and monitoring pipelines. To prevent these issues, you can change the storage location to a public SLS instance (SLS-PUB).
1. Log on to the ApsaraDB for PolarDB console.
2. In the left-side navigation pane, click **instance list**, and then click the ID of the target
instance, which takes you to the **basic information** page. ata security
3. In the left-side navigation pane, click **data security**.
4. On the right side of the page, click the **sql audit** tab.
5. Enable the option to store audit logs in SLS-PUB.

**Important**

This action cannot be undone. Proceed with caution. ackup

## 11 Backup

### 11.1 Back up data

This topic describes how to back up a PolarDB for PostgreSQL cluster. You can configure a backup policy that allows PolarDB for PostgreSQL to automatically back up your cluster. You can also manually back up your cluster.

**Usage notes**

Do not execute DDL statements during a backup operation. If DDL statements are executed during a backup operation, the relevant tables are locked, and the backup operation fails. We recommend that you back up your cluster during off-peak hours. If your cluster stores a large amount of data, a backup may require a long period of time. Backup files are retained for the specified period of time. We recommend that you download the backup files to your computer before the specified retention period ends.

**Backup notes**

| Database type | Data backup | Log backup |
|---|---|---|
| PolarDB | Supports full physical backup. | Write-ahead logs (WALs) are compressed and uploaded immediately after they are generated. Each log takes up 16 MB of storage space. Logs in the on-premises environment are deleted within 24 hours. |

**Configure a backup policy for automatic backup**

PolarDB for PostgreSQL automatically backs up your cluster based on the backup policy that you configure.
1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Backup and Restoration** page, click the **Backup Settings** tab and click **Edit**.
5. In the dialog box that appears, configure the parameters as required and click **Save**. The
following table describes the parameters.

| Paramete r | Description |
|---|---|
| Data Backup Retention (Days) | The number of days for which you want to retain backup files. Valid values: 7 to 730. Default value: 7. |

ackup

| Backup Cycle | The days on which you want to perform backups. You can select one or more days of the week. Note For data security purposes, we recommend that you select at least two days of the week. |
|---|---|
| Backup Time | The period in hours during which you want to perform a backup. |
| Log Backup | Specify whether to enable or disable the log backup feature. Important If you disable this feature, all log backup files are deleted and you cannot restore the data of the cluster to the specified point in time. |
| Log Backup Retention Period (Days) | The number of days for which you want to retain log backup files. Valid values: 7 to 730. Default value: 7. The log retention period must be less than or equal to the data retention period. |

**Manually back up a PolarDB for PostgreSQL cluster**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page, click **Backup Instance**. The Backup Instance dialog
box appears.
4. Select the backup mode and click **OK**.
You can set the backup mode and backup policy only to **Full Backup** and **Instance**
**Backup**.
5. Click the
icon in the upper-right corner to view the progress in the **Task Progress** column. Wait until the task is complete. You cannot download backup files to your computer.

**FAQ**

1. Q: Can I disable data backup for a PolarDB for PostgreSQL cluster?
ackup A: No, you cannot disable the data backup feature for your PolarDB for PostgreSQL cluster. However, you can reduce the data backup frequency to as low as twice a week. The data backup retention period must be within the range of 7 to 730 days.
2. Q: Can I disable log backup for a PolarDB for PostgreSQL cluster?
A: Yes, you can disable the log backup feature for your PolarDB for PostgreSQL cluster. To disable the log backup feature, perform the following steps: Log on to the PolarDB console, go to the Backup Settings tab of your PolarDB for PostgreSQL cluster, and modify the backup settings to disable the log backup feature.

### 11.2 Download data backup files and log backup files

**and log backup files**

PolarDB for PostgreSQL allows you to download unencrypted data backup files and log backup files and restore data from the backup files to your on-premises databases. This topic describes how to download data backup files and log backup files.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration** to go to the **Backup and**
**Restoration** page.
4. Click the Data Backup or Log Backup (Previously Archived Logs) tab.
To download data backup files, click the **Data Backup** tab. To download log backup files, click the **Log Backup (Previously Archived Logs)** tab.
5. Select a time range.
6. Find the data backup or log backup file that you want to download, and click Download
Instance Backup or **Download** in the **Actions** column. If you want to download a data backup file and use the data backup file to restore data, we recommend that you select the data backup file created closest to the point in time when the required data exists. If the log backup file is used to restore data to an on-premises database, take note of the following items: The instance ID of the log backup file (redolog) must be the same as the instance ID of the data backup file that you select. The start time of the log backup file must be later than the end time of the data backup file that you select and earlier than the point in time to which you want to restore the data of your cluster.
7. In the **Download Instance Backup Set** dialog box, select a download method.

| Download method | Description |
|---|---|

ackup

| Download backup files over the Internet. | Directly download the backup file. |
|---|---|
| Copy the internal URL. | Download the backup file from the internal URL. If your Elastic Compute Service (ECS) and PolarDB for PostgreSQL instance reside within the same region, you can log on to the ECS instance and use the internal URL to download the file. This method is fast and secure. |
| Copy the public URL | Download the backup file from the public URL. If you want to use other tools to download the file, use the public URL. |

If you use a Linux operating system, you can run the following command to download the file:

```
wget -c '<Download URL of the backup file>' -O <File name>
```

The -c option enables the resumable download feature. The -O option saves the downloaded file by using the specified name. We recommend that you use the file name contained in the download URL. If the URL contains more than one parameter, we recommend that you enclose the URL in a pair of single quotation marks (').

### 11.3 Restore full data

PolarDB supports cloning a new instance from a backup set or a point in time, fully restoring the database data, account information, and instance configuration of the primary instance. The cloned instance runs independently without affecting the primary instance, and supports custom configurations such as specifications and network settings. This is suitable for scenarios such as full recovery after accidental deletion or corruption of the primary instance, audit backtracking, and quick build of a test environment. This topic is suitable for full data restoration. For more information about how to restore data of databases and tables, see Restore data of databases and tables.

**Background information**

You can use one of the following methods to restore a cloned instance: restoring from a specified backup set or from a point in time within the valid retention period.
**Clone scope**: Only the database data, account information, and instance configurations
(such as whitelists, backup policies, parameter settings, and threshold alerts) of the primary instance are replicated. Read-only instances under the primary instance are not cloned. ackup
**Constraints**: The clone instance must have the same database type and version as the
primary instance. Other configurations, such as the edition, zone, network type, instance type, and storage capacity, can be customized.
**Account management**: The account system of the clone instance is identical to that of
the primary instance, but you can modify the account passwords on the clone instance.
**Performance recommendations**: If the clone instance is used for restoring data from the
primary instance, it is recommended to select a specification and storage space that are equal to or greater than those of the primary instance. Selecting lower specifications may significantly prolong the data recovery time due to performance limitations.

**Prerequisites**

Before you create a clone instance, ensure that the primary instance meets the following requirements:
**Instance status**: The primary instance must be in the Running state.
**No ongoing migration tasks**: The instance has no ongoing migration or switchover tasks.
**Backup enabled**: Data backup and log backup are enabled.
**Backup availability**:
To restore from a backup set: At least one completed data backup set exists. To restore from a point in time: The selected time must fall within the log backup retention period.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Data Backup** tab, find the backup file from which you want to restore data and
click **Restore**.
5. In the **Restore** message, read the note and click **OK**.
6. On the **PolarDB Primary-Secondary Edition Recovery** page, configure the parameters
in the following table.

| Section | Parameter | Description |
|---|---|---|
| Area | Region | The region of the PolarDB for PostgreSQL cluster. |
|   | Restoration Mode | The restoration mode used by the primary instance. Valid values: By Point in Time By Backup Set |

ackup

| Database Restoration |   |   |
|---|---|---|
|   | Restoration Time | The point in time to which you want to restore the primary instance. Note When Restore Mode is set to By Point in Time, you must specify this parameter. |
|   | Backup Set | The backup set for restoration. Note When Restore Mode is set to By Backup Set, you must specify this parameter. |
| Specification Configuration | Instance Name | The name of the cloned instance. |
|   | Database Type | The database engine of the cloned instance, which cannot be modified. |
|   | Engine Version | The engine version of the cloned instance, which cannot be modified. |
|   | Number of Minor Database Versions to Display | The number of minor versions to be displayed. |
|   | Minor Database Version | The minor version of the database. We recommend that you keep the current version or upgrade to the latest version. By default, the latest minor version is used. |
|   | Series | The edition of the cloned instance. The edition displayed in the console prevails. |
|   | Storage Type | The storage type of the cloned instance. The storage type displayed in the console prevails. |
|   | Specifications | The instance type of the cloned instance. Note We recommend that you select a higher instance type and larger storage capacity than those of the primary instance. This can accelerate the data restoration process. |

ackup

|   | Storage Capacity | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. The available storage capacity displayed in the console prevails. Note A dedicated instance that uses local disks exclusively occupies the allocated resources, and its storage capacity varies based on the instance type. |
|---|---|---|
|   | Network Type | PolarDB for PostgreSQL supports the following network types: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by using security groups or whitelists. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways for a VPC. For security purposes, we recommend that you select the VPC network type. |
|   | IP Type | IPv4: assigns an IPv4 address to the instance. This option is suitable for IPv4 networks. Dual-Stack (IPv4/IPv6): assigns IPv4 and IPv6 addresses to the instance. This option is suitable for hybrid networks in which both IPv4 and IPv6 clients need to access the instance. If you select this option, you must configure an IPv6 address whitelist to limit the IPv6 addresses that can access the instance. |
| Network Type |   |   |
|   | VPC | The VPC in which you want to create the instance. Note When Network Type is set to VPC, you must specify this parameter. |
|   | VSwitch | The vSwitch to which the instance is connected. Note When Network Type is set to VPC, you must specify this parameter. |

ackup

|   | IP Whitelist | The IP addresses that are allowed to access the instance. Note If IP Type is set to Dual-Stack, the IPv6 Whitelist configuration items be visible and must be configured. |
|---|---|---|
|   | IPv6 Whitelist |   |

7. After you complete the configuration, click **Submit**.

### 11.4 Restore data of databases and tables

**and tables**

PolarDB allows you to restore a specified database or table to the original instance based on a backup set or a point in time, without a full restore. This is ideal for correcting misoperations and analyzing historical data.

**Prerequisites**

The primary instance is in the running state. No asynchronous tasks such as migration and configuration change are being executed. Data backup and log backup are enabled. Restore from a backup set: At least one complete full backup set exists. Restore from a point in time: The target point in time must be within the log backup retention period, and a valid full backup exists before that point in time.

**Description**

**Restoration granularity**

Database-level restoration: Restores all user tables in the selected database. The system appends a suffix to the original database name for identification. You can also specify a custom database name. Table-level restoration: Restores only the selected tables. The system appends a suffix to the original table name for identification. You can also specify a custom table name.

**Permission inheritance mechanism**

The restore operation also restores the access permissions of the original table. The data written by a privileged account can still be queried and written by that account after the restoration.

**Naming requirements for database names, schema names, and table names**

Without quoted identifiers: Names can contain letters, digits, and underscores ( `[a-zA-` `Z0-9_]+` ) and must start with a letter. With double‑quoted identifiers: Names can contain letters, digits, underscores ( `_` ), hyphens ( `-` ), and escaped double quotation marks ( `""` ). The first character must be a letter. Special characters, such as number signs ( `#` ), spaces, and Chinese characters, are not supported. Using them may cause recovery failures or metadata anomalies.

**Metadata logic of point-in-time recovery (PITR)**

ackup If you choose to restore data to a specific point in time, the list of databases and tables that you obtain is retrieved from the metadata of the most recent full backup before the target point in time, not from the real‑time state of databases and tables at that target time. The destination table must exist in the full backup. Otherwise, the backup cannot be restored. If the original database or table has been deleted, you can restore data only by backup set, but not by point in time. The selected point in time must fall within the recoverable range. To use the point-in-time restoration method, make sure that the full backup set that is closest to the specified point in time contains the tables to be restored. The recoverable time range is determined by the log backup retention period configured in the backup settings. PostgreSQL WAL logs record data changes, but do not independently retain historical metadata snapshots. To balance accuracy and system overhead, the metadata from the most recent backup set is currently used as the basis for selecting objects to be restored. In a production environment where the schemas of the databases and tables remain relatively stable, this method is generally reliable.

**Limits**

**Table quantity limit**: The total number of tables in the instance must be less than 50,000.
If the number of tables exceeds the limit, the database and table restoration feature is not supported.
**Restore location**: You can restore individual databases or tables of an instance only to the
original instance. Cross‑instance restoration is not supported.
**Unrestored objects**: Views, functions, stored procedures, sequences, triggers, and foreign
keys cannot be restored independently.
**Table name length limit**: The maximum length is 64 characters. Exceeding parts are
automatically truncated. You can manually modify the destination table name before restoration.
**Maximum number of tables to be restored at a time** : For non‑full database restore, a
maximum of 100 tables in the database can be restored at a time. For full database restore, all tables in that database are restored.

**Impact**

**Availability**: During the restoration period, the instance remains fully available with no
service interruption. Existing connections and services operate normally.
**Resource consumption**: The restoration process consumes some CPU, IOPS, and
database connection resources, which may affect the performance for a short period of time.
**Data writing**: Data is written into newly created independent databases or tables, leaving
the original data unaffected.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page. ackup
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Data Backup** tab, click **Restore Database (Table)**, configure the following
information, and then click **OK**.

| Parameter | Description |
|---|---|
| Recovery location | Default value: Restore to Current Instance. |
| Recovery Method | Restore by backup set: You also need to select the target backup set. Restore by point in time: You need to enable log backup and then select a recoverable time point. The system restores the full backup data first, and then restores the incremental log backup data. You can select a point in time within the log backup retention period. |
| Libraries and tables to be restored | The databases and tables that you want to restore. |
| Selected Databases and Tables | Check or manage the selected databases or tables. You can specify custom names for restored databases or tables. |

After the restore completes, you can connect to the database and view the data restored to the original instance.

## 12 Plug-in management

### 12.1 Supported extensions

This topic describes the extensions and extension versions supported by PolarDB for PostgreSQL.

**Supported extensions and extension versions**

The following table describes common extensions and extension versions that are supported by different versions of PolarDB for PostgreSQL. To query the extensions supported by your instance, execute the following statement:

```
SELECT * FROM pg_available_extensions;
```

| Extension | PostgreSQL 17 | PostgreSQL 16 | PostgreSQL 14 | Description |
|---|---|---|---|---|
| address sta _ ndardizer | 3.3.7 | 3.3.7 | 3.3.7 | Provides the address standardization service. |
| address sta _ ndardizer da _ ta us _ | 3.3.7 | 3.3.7 | 3.3.7 | Provides the address standardization service. You can use it to format and standardize US addresses. |
| AGE | - | 1.5.0 | 1.5.0 | Allows you to query graphs in a database by using Cypher. |
| bloom | 1 | 1 | 1 | Provides an index access method based on Bloom filters. |
| btree gin _ | 1.3 | 1.3 | 1.3.1 | Provides sample Generalized Inverted Index (GIN) operator classes used to implement B- tree equivalent behavior across multiple data types or all enumerated types. |
| btree gist _ | 1.7 | 1.7 | 1.6.1 | Provides sample GiST operator classes used to implement B-tree equivalent behavior across multiple data types and all enumerated types. |

| citext | 1.6 | 1.6 | 1.6 | Provides a string type that is not case-sensitive. |
|---|---|---|---|---|
| cube | 1.5 | 1.5 | 1.5 | Provides a data type used to represent multidimensional cubes. |
| dblink | 1.2 | 1.2 | 1.2 | Manages tables across databases. |
| decoderbufs | 0.1.0 | - | 0.1.0 | Generates data compatible with the Debezium platform based on the Protocol Buffers protocol. |
| dict int _ | 1 | 1 | 1 | Provides a sample add-on dictionary template used to run full-text searches. |
| earthdistanc e | 1.2 | 1.2 | 1.1 | Provides two methods for computing great-circle distances on the surface of Earth. |
| encdb | - | - | 1.1.14 | Provides the always- confidential database feature. |
| fuzzystrmatc h | 1.2 | 1.2 | 1.1 | Computes string similarity and distance. |
| ganos addre _ ss standardi _ zer | - | 7.4 | 7.3 | Standardizes the names of geographical locations based on Postal Address Geocode (PAGC). |
| ganos addre _ ss standardi _ zer data us _ _ | - | 7.4 | 7.3 | Standardizes the names of the geographical locations in the US based on PAGC. |
| ganos geom _ etry | 7.7 | 7.4 | 7.3 | Computes and analyzes spatial geometries. |
| ganos geom _ etry pyrami _ d | 7.7 | 7.4 | 7.3 | Displays 2D geometric big data at high speeds. |

| ganos geom _ etry sfcgal _ | 7.7 | 7.4 | 7.3 | Processes spatial geometries. This is an extension of the SFCGAL extension. |
|---|---|---|---|---|
| ganos geom _ etry topolog _ y | 7.7 | 7.4 | 7.3 | Computes and analyzes spatial geometries. |
| ganos netw _ orking | 7.7 | 7.4 | 7.3 | Computes and analyzes spatial network geometries. |
| ganos point _ cloud | 7.7 | 7.4 | 7.3 | Stores, computes, and analyzes point cloud data. |
| ganos point _ cloud geom _ etry | 7.7 | 7.4 | 7.3 | Stores, computes, and analyzes point cloud data. |
| ganos raster _ | 7.7 | 7.4 | 7.3 | Stores, computes, and analyzes spatial grids. |
| ganos spati _ alref | 7.7 | 7.4 | 7.3 | Computes and analyzes spatial references. |
| ganos tiger _ _ geocoder | - | 7.4 | 7.3 | Supports the TIGER data format used by USCB. |
| ganos trajec _ tory | 7.7 | 7.4 | 7.3 | Computes and analyzes objects in the Ganos MOD system. |
| hll | 2.18 | 2.18 | 2.17 | Efficiently estimates business metrics, such as page views (PV) and unique visitors (UV). |
| hstore | 1.8 | 1.8 | 1.8 | Stores key-value pairs in a PostgreSQL value. |
| hypopg | - | - | 1.4.0 | Creates hypothetical indexes. |
| imgsmlr | - | - | 1 | Supports similar image searches. |
| intagg | 1.1 | 1.1 | 1.1 | Provides an integer aggregator and an enumerator. |

| intarray | 1.5 | 1.5 | 1.5 | Provides functions and operators used to manage null-free integer arrays. |
|---|---|---|---|---|
| ip4r | 2.4 | - | 2.4 | Stores IPv4 and IPv6 addresses in PostgreSQL. |
| isn | 1.2 | 1.2 | 1.2 | Validates input numbers and hyphenates output numbers based on a hard-coded list of prefixes. |
| ltree | 1.3 | 1.2 | 1.2 | Labels the data stored in a hierarchical tree structure. |
| mysql fdw _ | 1.2 | 1.2 | 1.2 | Reads data from and writes data to MySQL databases. |
| oss fdw _ | 1.1 | 1.1 | 1.1 | Reads data from and writes data to Object Storage Service (OSS) bucket. |
| pase | 0.0.1 | 0.0.1 | 0.0.1 | Efficiently searches for vectors. |
| pg bigm _ | 1.2 | 1.2 | 1.2 | Creates a 2-gram GIN used to accelerate full-text searches. |
| pg buffercac _ he | 1.6 | 1.5 | 1.5 | Examines shared buffers in real time. |
| polar tde uti _ _ ls | 1 | 1 | 1 | Bulk encrypts and decrypts tables and indexes by using transparent data encryption (TDE). |
| pg cron _ | 1.5 | 1.5 | 1.5 | Configures scheduled tasks. |
| pg freespac _ emap | 1.2 | 1.2 | 1.2 | Examines the free space map (FSM). |
| pg jieba _ | 1.1.0 | 1.1.0 | 1.1.0 | Segments Chinese text. |
| pg pathman _ | - | - | 1.5 | Partitions tables at high performance. |

| pg hint plan _ _ | 1.7.0 | - | 1.4.1 | Adds hints to SQL statements. The hints are used to change the execution plans of SQL statements. |
|---|---|---|---|---|
| pg profile _ | - | - | 4.1 | Collects statistics on resource- intensive activities. |
| pg prewarm _ | 1.2 | 1.2 | 1.2 | Loads data to an operating system buffer or a PostgreSQL buffer. |
| pg sphere _ | - | - | 1 | Provides spherical data types, functions, operators, and indexes for PostgreSQL. |
| pg search _ | - | 0.17.2 | - | Provides high-performance full-text search capabilities based on the BM25 algorithm. This extension supports joint indexing and search for multiple data types, such as text, numeric, BOOLEAN, time, and JSON. |
| pg stat kcac _ _ he | 2.3.0 | - | 2.2.1 | Collects statistics on read and write operations in file systems. |
| pg stat stat _ _ ements | 1.11 | 1.1 | 1.9.2 | Tracks the statistics of all SQL statements executed on a specific server. |
| pg trgm _ | 1.6 | 1.6 | 1.6 | Provides functions and operators used to compute the similarity between alphanumeric texts. It also provides index operator classes used to efficiently search for similar strings. |
| pgaudit | 17.1 | - | 1.6.2 | Generates audit logs containing session and object details. |

| pgcrypto | 1.3 | 1.3 | 1.3 | Provides cryptographic functions for PostgreSQL. |
|---|---|---|---|---|
| pgrouting | 3.4.2 | 3.4.2 | 3.4.2 | Performs network analysis and routing tasks. |
| pgrowlocks | 1.2 | 1.2 | 1.2 | Provides a function that is used to display row lock information about a specific table. |
| pgstattuple | 1.5 | 1.5 | 1.5 | Provides various functions used to obtain tuple-level statistics. |
| pgvector | 0.8.0 | 0.8.0 | 0.8.0 | Performs high-dimensional vector similarity searches. |
| pldebugger | 1.1 | 1.1 | 1.1 | Debugs stored procedures. |
| plperl | 1 | 1 | 1 | Supports the Perl procedural language. |
| plpgsql | 1 | 1 | 1 | Supports the SQL procedural language. |
| pltcl | 1 | 1 | 1 | Supports the TCL procedural language. |
| postgis | 3.3.7 | 3.3.7 | 3.3.7 | Processes and stores spatial geographic data in PostGIS. |
| postgis sfcg _ al | 3.3.7 | 3.3.7 | 3.3.7 | Manages spatial geographic data in PostGIS. |
| postgis tiger _ geocoder _ | 3.3.7 | 3.3.7 | 3.3.7 | Manages PostGIS data in the TIGER format. |
| postgis topo _ logy | 3.3.7 | 3.3.7 | 3.3.7 | Manages topological objects in PostGIS. |
| roaringbitma p | 0.5 | 0.5 | 0.5 | Computes bitmaps to improve query performance. |

| rum | 1.3 | 1.3 | 1.3 | Efficiently runs full-text searches. |
|---|---|---|---|---|
| sequential u _ uid | 1.0.3 | - | 1.0.2 | Generates sequential UUIDs. |
| smlar | - | - | 1 | Computes the similarity between two arrays of the same data type. |
| sslinfo | 1.2 | 1.2 | 1.2 | Obtains information about the SSL certificate provided by the connected client. |
| tablefunc | 1 | 1 | 1 | Provides functions used to return tables. |
| tds fdw _ | 2.0.4 | - | 2.0.2 | Queries data from other types of databases. |
| timescaledb | - | 2.18.0 | 2.16.1 | Enables automatic sharding, efficient writing, retrieval, and near-real-time aggregation of time-series data. |
| tsm system _ _ rows | 1 | 1 | 1 | Provides the SYSTEM ROWS _ table sampling method. |
| tsm system _ _ time | 1 | 1 | 1 | Provides the SYSTEM TIME _ table sampling method. |
| unaccent | 1.1 | 1.1 | 1.1 | Provides a text search dictionary used to remove accent marks or diacritic signs from lexemes. |
| uuid-ossp | 1.1 | 1.1 | 1.1 | Provides functions that use a standard algorithm to generate UUIDs. |
| varbitx | 1.1 | 1.1 | 1.1 | Supports various BIT-type operations. |
| wal2json | - | 2.6 | 2.6 | Exports logical log records as a file in the JSON format. |

| xml2 | 1.1 | 1.1 | 1.1 | Provides XPath query and XSLT functionality. |
|---|---|---|---|---|
| zhparser | 2.2 | 2.2 | 1 | Supports full-text Chinese searches. |

### 12.2 Manage extensions

This topic describes how to install and uninstall an extension for a PolarDB for PostgreSQL instance. Extension management allows you to flexibly enable advanced features such as PostGIS, full-text retrieval, and vector computing to meet diverse business requirements.

**Background information**

PolarDB for PostgreSQL supports a wide range of open-source and self-developed extensions, such as PostGIS, pgvector, and TimescaleDB. On‑demand enabling: By default, the extension is not installed. It is installed only when you need it. This reduces resource usage and minimize potential security risks. Database-level isolation: An extension is installed in a specific database. Extensions in different databases do not affect each other. Scenarios: Spatial analysis: Install `PostGIS` to process map and trajectory data. AI vector retrieval: Install `pgvector` to support vector storage and search for large language models. Time series data: Install `TimescaleDB` to optimize monitoring and IoT data storage.

**Prerequisites**

At least one database already exists in the instance. Only privileged accounts that have the DBOwner permission are allowed to install extensions.

**Install extensions**

**Install a single extension**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Plug-in Management** and choose **Manage Plug-ins**
**> Available Plug-ins**.
4. In the upper-right corner of the page, select the database on which to install the extension.
You can also use the extension type filter in the same area to quickly locate the desired extension.
5. Find the extension that you want to install and click **Install** in the **Actions** column.
6. In the dialog box that appears, select the account name and click **OK**.

**Batch install extensions**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Plug-in Management** and choose **Manage Plug-ins**
**> Available Plug-ins**.
4. In the upper-right corner of the page, select the database on which to install the extension.
You can also use the extension type filter in the same area to quickly locate the desired extension.
5. Select the extensions that you want to install and click **Batch Install**.
6. In the dialog box that appears, select the account name and click **OK**.

**Uninstall extensions**

**Uninstall a single extension**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Plug-ins** and choose **Manage Plug-ins > Installed**
**Plug-ins**.
4. In the upper-right corner of the page, select the database from which the extension is to be
uninstalled. You can also use the extension type filter in the same area to quickly locate the desired extension.
5. Find the extension that you want to uninstall and click **Detach** in the **Actions** column.
6. In the message that appears, click **OK**.

**Batch uninstall extensions**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Plug-ins** and choose **Manage Plug-ins > Installed**
**Plug-ins**.
4. In the upper-right corner of the page, select the database from which the extension is to be
uninstalled. You can also use the extension type filter in the same area to quickly locate the desired extension.
5. Select the extensions that you want to uninstall and click **Batch Detach**.
6. In the message that appears, click **OK**.

### 12.3 GanosBase TSDB

Time Series Databases (TSDBs) are specially designed to efficiently store and process time series data. Time series data is a sequence of data points arranged in chronological order. Each data point usually contains a timestamp and one or more values (metrics). Time series data is widely used in fields such as Internet of Things (IoT), monitoring systems, financial transactions, industrial control, sensor networks, meteorological records, and server metric monitoring.

**Background information**

**g**

TSDBs were introduced for the following reasons: Emergence of IoT: With the increasing popularity of IoT technology, a large number of devices and sensors are deployed around the world. They continuously generate time series data, such as temperature, humidity, and device status. Such data is usually timestamped and huge in size. This makes it difficult for traditional relational databases to store and process such data efficiently. Growing demand for monitoring and log management: Monitoring of systems and applications is becoming increasingly important in fields such as IT, industrial control, and energy management. These applications need to collect and analyze time series data to discover anomalies, performance bottlenecks, and trends to assist decision-making. Traditional databases are inadequate for dealing with highly concurrent writes, data compression, and efficient query of time series data. Big data analysis and forecasting needs: With the development of data analysis technology, enterprises and research institutions focus more on the analysis of historical time series data for predictive maintenance, market trend prediction, and climate model prediction. This requires databases not only to store large-scale time series data efficiently, but also to support complex analysis and queries of time series data. Resource optimization and cost control: In many scenarios, the cost of storing and processing time series data is an important consideration. TSDBs use technologies such as data compression, efficient indexing, and storage optimization to significantly reduce storage and computing resource costs while ensuring query efficiency. Therefore, TSDBs were introduced to store time series data. They are optimized based on the characteristics of time series data, such as high write throughput, data compression, and time range query optimization, to better meet the requirements of those scenarios.

**Features**

GanosBase TSDB is a time series database implemented on PolarDB for PostgreSQL. GanosBase TSDB is fully compatible with open-source TimescaleDB Apache 2.0. It provides advanced features such as continuous aggregates, time series compression, statistical analysis, pre-downsampling during data writes, SSL-encrypted transmission, transparent data encryption (TDE) for data storage, and nanosecond timestamp resolution.

**High-performance reads and writes**

GanosBase TSDB can process tens of thousands of data point writes per second and provides fast historical data retrieval capabilities to meet real-time monitoring and analysis requirements.

**Continuous aggregates**

GanosBase TSDB supports custom aggregation views. In these views, raw time series data is aggregated and calculated (such as the sum, average, maximum, or minimum calculation) at a specified time interval (such as every minute, every hour, or every day), and the results are stored in a separate materialized view. This process is automated. After the configuration is complete, GanosBase TSDB updates these aggregate views in the background at a regular interval or based on data changes to ensure that the aggregated data is updated in real time.

**Cross-modal data processing**

GanosBase TSDB supports integrated storage and retrieval of data in different modalities, such as time series and spatio-temporal data. Data can be partitioned based on time and space. During queries, data can be automatically partitioned and pruned to accelerate retrieval efficiency.

**Low-cost storage**

GanosBase TSDB uses optimized storage structures and compression algorithms to reduce storage space consumption. It supports deduplication and high-compression storage for similar or duplicate data, which reduces the storage space by more than 70%. GanosBase TSDB is interoperable with Object Storage Service (OSS) to archive cold data and greatly reduce storage costs. This is important for large amounts of time series data.

**Data retention policies**

GanosBase TSDB supports flexible data retention policies and can automatically delete expired data based on business requirements. This helps control data storage costs and keeps databases running efficiently.

**Scalability and high availability**

For large applications, GanosBase TSDB relies on PolarDB to provide horizontal scaling capabilities and failover mechanisms to ensure system stability and reliability.

**Pre-downsampling during data write**

To accelerate subsequent time series-based downsampling queries, GanosBase TSDB provides the feature of pre-downsampling during data writes. The following section describes details of this feature: Pre-downsampling mechanism: When data is written, the system performs preliminary aggregation or downsampling on raw data based on user-defined rules, such as time windows and aggregation functions. Performance optimization: The computing overhead of subsequent queries is significantly reduced by reducing the amount of stored raw data. This improves the response speed of downsampling queries. Flexibility: You can define downsampling policies based on your business requirements, such as aggregation by minute, hour, or day.

**Data security: SSL-encrypted transmission and TDE for data storage**

GanosBase TSDB provides a comprehensive data security guarantee system to ensure data security during data transmission and storage. For more information, see Configure SSL encryption and Configure TDE.

**Nanosecond timestamp resolution**

GanosBase TSDB supports timestamp resolutions up to nanoseconds, which meets the storage and query requirements for high-precision time series data. Timestamp precision: GanosBase TSDB supports timestamp resolutions ranging from seconds to nanoseconds. You can select an appropriate timestamp resolution based on your business requirements. High-performance storage: GanosBase TSDB of PolarDB can maintain high write and query performance even at a nanosecond resolution. Wide applicability: GanosBase TSDB is suitable for scenarios such as high-frequency sensor data collection and high-frequency financial trading analysis. In summary, GanosBase TSDB can process time series data with its unique design and optimization. It is indispensable for large-scale monitoring, analysis, and prediction tasks.

**Scenarios**

**IoT**

A large number of devices, such as smart sensors, continuously generate monitoring data such as temperature, humidity, and pressure. Such data has time series characteristics and needs to be collected, stored, and analyzed in real time to achieve remote monitoring and fault early warning.

**Monitoring systems**

These systems perform IT infrastructure monitoring, such as server performance and network traffic monitoring, and application performance management. These systems need to record changes in system metrics over time to quickly discover problems and optimize performance.

**Financial services**

Data on stock prices, trading volumes, and exchange rates in financial markets are typical time series data. TSDBs can be used for high-frequency trading analysis, market trend prediction, and risk management.

**Energy and utilities**

The operational data and energy consumption data of smart grid and hydropower stations are stored and analyzed by using TSDBs to help improve energy allocation efficiency and forecasting.

**Industrial automation**

Equipment status monitoring and production process control in the manufacturing industry generate a large amount of time series data. TSDBs implement equipment health management and capacity optimization.

#### 12.3.1 Quick start

GanosBase TSDB is a time series database service that is provided as an extension of PolarDB for PostgreSQL. GanosBase TSDB inherits all the features of PolarDB for PostgreSQL clusters, such as shared storage, one primary node and multiple read-only nodes, and backup and restoration. GanosBase TSDB is compatible with TimescaleDB Apache 2.0 and provides advanced features such as continuous aggregates, compression, and statistical analysis of time series data. This topic describes the terms of time series databases and the usage of GanosBase TSDB, including how to start, upgrade, and use GanosBase TSDB.

**Enable GanosBase TSDB**

To enable GanosBase TSDB in a PolarDB for PostgreSQL cluster, you must add **timescaledb** to the `shared_preload_libraries` parameter. You can modify the shared_preload_libraries parameter in the PolarDB console.

**Important**

The cluster restarts after you modify the shared_preload_libraries parameter. Proceed with caution.

**Install the extension**

The GanosBase TSDB extension relies on the **TimescaleDB** extension. You can use one of the following methods to install the GanosBase TSDB extension: Use the CASCADE keyword to automatically install both the `ganos_tsdb` extension and the TimescaleDB extensions in one step.

```
CREATE EXTENSION ganos_tsdb CASCADE;
```

Manually install extensions. Install the TimescaleDB extension first, and then install the `ganos_tsdb` extension.

```
CREATE EXTENSION timescaledb; CREATE EXTENSION ganos_tsdb;
```

|   | ERROR: Disable the injection of custom functions when creating extension: |
|---|---|
| metadata insert trigger (21128) _ _ |   |

extension, contact us to obtain related permissions and then reinstall the extension. Alternatively, install the extension in the PUBLIC schema, which avoids permissionrelated issues.

```
CREATE EXTENSION ganos_tsdb WITH SCHEMA PUBLIC CASCADE;
```

**Upgrade the extension**

To upgrade the GanosBase TSDB and TimescaleDB extensions in a cluster where these extensions are already installed, execute the following statements:

```
-- Upgrade the timescaledb extension first. ALTER EXTENSION timescaledb UPDATE; -- Upgrade the ganos_tsdb extension. ALTER EXTENSION ganos_tsdb UPDATE;
```

**Time series hypertables**

Hypertables are a special table type provided in time series databases. It can easily process time series data. All operations that can be performed on common tables can be completed on hypertables.

**Features**

A hypertable is a data table in PolarDB for PostgreSQL that can be used to automatically partition data by time. Hypertables are interacted in the same way as common tables, but hypertables also have some additional features that make them easier to manage time series data. In a time series database, hypertables coexist with common tables. You can use a hypertable to store time series data. This improves the performance of data writes and queries and allows you to use sequence functions on the hypertable. Time series databases can partition time series data in hypertables based on time parameters. In the background, time series databases automatically configure and maintain hypertable partitions.

**Create a hypertable**

Execute the following statement to convert a common table into a hypertable:

```
SELECT create_hypertable(
    'table_name',
    'time_column_name',
    'partitioning_column_name',
    number_partitions,
    'associated_schema_name',
    'associated_table_prefix',
    chunk_time_interval,
    create_default_indexes,
    if_not_exists,
    partitioning_func,
    migrate_data,
    chunk_target_size,
    chunk_sizing_func,
    time_partitioning_func
```

); The following table describes the parameters.

| Parameter | Requ ired | Description |
|---|---|---|
| table name _ | Yes | The name or OID of the common table. To distinguish the common table from the hypertable, the former is called the original table. The converted hypertable has the same name as the original table. |
| time column nam _ _ e | Yes | The name of the time column that has time series characteristics in the original table. The following data types are supported: TIMESTAMP, TIMESTAMPTZ, and DATE. INTEGER, which is treated as microseconds. INTERVAL. |
| partitioning colum _ n name _ | No | The name of the partition column. By default, the hypertable is partitioned based on the time column of the original table. |
| number partitions _ | No | The number of partitions. |
| associated schema _ name _ | No | The schema of the hypertable. |
| associated table p _ _ refix | No | A hypertable consists of multiple chunks, which are automatically created by the system. You can specify the prefix of chunks. |
| chunk time interv _ _ al | No | The interval at which the hypertable is divided into chunks. The default value is 7 days. |

| create default ind _ _ exes |   | No | Specifies whether to create B-Tree indexes on the time column of the hypertable. Valid values: true (default) false |
|---|---|---|---|
| if not exists _ _ |   | No | Specifies whether to return an error if the hypertable is created. Valid values: true false (default) |
| partitioning func _ |   | No | If spatial partitioning is used, you can specify a custom spatial partitioning function. |
| migrate data _ |   | No | Specifies whether to transfer the data to the hypertable if the original table already has data. Valid values: true false (default) |
| chunk target size _ _ |   |   | The size of the chunk. Example: '1000MB', 'estimate', or 'off' . |
|   | hunk target size _ _ | No | 'off' |
| chunk sizing func _ _ |   | No | The custom function used to count chunking intervals. This parameter is used together with the chunk target size parameter. _ _ |
| time partitioning f _ _ unc |   | No | The partitioning function used for time partitions. |

**Partitions in a hypertable**

When you create and use a hypertable, it automatically partitions data by time or by space. Each hypertable consists of multiple chunks. Each chunk is assigned a time range and contains only data within that time range. If a hypertable is also partitioned by space, each chunk is also assigned a subset of the space values. Each chunk of a hypertable contains only data within a specific time range. When you insert data in a time range that has not been assigned to an existing chunk, a chunk is automatically created. By default, a hypertable is partitioned at a seven-day interval. You can also execute the following SQL statement to modify the partitioning interval.

```
SELECT set_chunk_time_interval(
    'table_name',
    chunk_time_interval,
    'dimension_name'
```

); The following table describes the parameters.

| Parameter | Description |
|---|---|
| table name _ | The name of the hypertable. |
| chunk time interval _ _ | The interval at which the hypertable is divided into chunks. |
| dimension name _ | Optional. The partitioning (dimension) policy. Default value: NULL. |

**Example**

Create a hypertable to store transaction data.
1. Create a common table.

```
CREATE TABLE transaction_data(
   tm TIMESTAMPTZ NOT NULL,
   id INT NOT NULL,
   price double precision);
```

2. Set the replication identifier of the common table, which must be DEFAULT.

```
ALTER TABLE transaction_data replica IDENTITY DEFAULT;
```

3. Convert the common table into a hypertable.

```
SELECT create_hypertable('transaction_data', 'tm', chunk_time_interval => INTERVAL '1 day');
```

If the common table already contains data, you need to include the `migrate_data` parameter and set it to `true` to migrate the existing data to the hypertable. If the common table contains a large amount of data, the migration process may take a significant amount of time.
4. (Optional) Modify the partitioning interval of the hypertable.

```
SELECT set_chunk_time_interval('transaction_data', chunk_time_interval => INTERVAL '2 day');
```

**Continuous aggregates**

Continuous aggregates are an automated precomputation mechanism designed to periodically or continuously update predefined aggregation results, such as hourly averages. Instead of recalculating these aggregates from scratch each time, queries can directly access the precomputed results. This enables faster and more efficient data retrieval. Unlike traditional materialized views, continuous aggregates are specifically optimized for time series data and support incremental updates. Only new or modified data is processed during updates, avoiding the need to recompute the entire dataset. This approach significantly reduces computational overhead and accelerates queries on large datasets.

**Benefits**

Query acceleration: Continuous aggregates enable direct querying of precomputed results, which eliminates the need to perform full table scans of raw data. Resources saving: By avoiding on-the-fly recalculations, continuous aggregates significantly reduce the consumption of CPU and memory resources. Automated maintenance: Continuous aggregates automatically manage updates for both new and historical data without manual intervention.

**Create a continuous aggregate**

```
CREATE MATERIALIZED VIEW transaction_min_cagg
    WITH (timescaledb.continuous) -- declares the materialized view as a continuous agg
regate.
```

`AS`

```
    SELECT id,
        time_bucket(INTERVAL '1 min', tm) AS bucket, -- groups data into 1-minute
intervals.
        AVG(price),
        MAX(price),
        MIN(price)
    FROM transaction_data
    GROUP BY id, bucket;
```

**Store continuous aggregate results**

The results of continuous aggregates are stored in a dedicated materialized view, with the data organized into time-based chunks. These chunks align with the partitioning of the underlying hypertable data.

**Task scheduling**

Continuous aggregates use a task scheduling mechanism to ensure that aggregated results are refreshed automatically or manually.

**Create a job**

Create a job to invoke a function or stored procedure at defined intervals.

```
integer add_job(
                proc REGPROC,
                schedule_interval INTERVAL,
                config JSONB DEFAULT NULL,
                initial_start TIMESTAMPTZ DEFAULT NULL,
                scheduled BOOL DEFAULT true,
                check_config REGPROC DEFAULT NULL,
                fixed_schedule BOOL DEFAULT TRUE,
                timezone TEXT DEFAULT NULL
```

); The following table describes the parameters.

| Parameter | Description |
|---|---|
| proc | The name or OID of the function or stored procedure to be executed. |

| schedule interval _ | The interval at which the job runs. |
|---|---|
| config | The configuration parameters for the job. |
| initial start _ | The execution start time of the job. By default, the job starts at the time when it is created. |
| scheduled | Specifies whether the job is scheduled to run automatically. Default value: true . |
| check config _ | The function used to validate the config parameter. Default value: NULL. |
| fixed schedule _ | Specifies whether the job runs at the specified intervals. Default value: true . |
| timezone | The time zone. Default value: NULL. |

**Example**

1. Prepare basic data. Create a stored procedure to be executed by a job.

```
CREATE OR REPLACE PROCEDURE user_defined_action(job_id int, config jsonb) LANGUAGE PL PGSQL AS
```

$$

```
BEGIN
  RAISE NOTICE 'Executing action % with config %', job_id, config;
END $$;
```

2. Create a job. A unique job `ID` is returned after the job is created.

```
SELECT add_job('user_defined_action','1 hour'); SELECT add_job('user_defined_action','1h', initial_start => '2024-03-11 00:00:00');
```

**Modify a job**

Modify an existing job.

```
void alter_job( job_id INTEGER,
        schedule_interval INTERVAL = NULL,
        max_runtime INTERVAL = NULL,
        max_retries INTEGER = NULL,
        retry_period INTERVAL = NULL,
        scheduled BOOL = NULL,
        config JSONB = NULL,
        next_start TIMESTAMPTZ = NULL,
        if_exists BOOL = FALSE,
        check_config REGPROC = NULL,
        fixed_schedule BOOL = NULL,
        initial_start TIMESTAMPTZ = NULL,
        timezone TEXT DEFAULT NULL
```

); The following table describes only some key parameters.

| Parameter | Description |
|---|---|
| job id _ | The ID of the job that you want to modify. |
| max runtime _ | The maximum amount of time that the job is allowed to run. Default value: NULL. |
| max retries _ | The maximum number of retries allowed if the job fails. Default value: NULL. |
| retry period _ | The time interval between retries if the job fails. Default value: NULL. |

**Example**

```
SELECT alter_job(1002, schedule_interval => INTERVAL '2 hours');
```

**Manually run a job**

Manually run an existing job.

```
void run_job(job_id int);
```

The following table describes the parameters.

| Parameter | Description |
|---|---|
| job id _ | The ID of the job that you want to run. |

**Example**

```
CALL run_job(1002);
```

**Delete a job**

Delete a job.

```
void delete_job(job_id int);
```

The following table describes the parameters.

| Parameter | Description |
|---|---|
| job id _ | The ID of the job that you want to delete. |

**Example**

```
SELECT delete_job(1002);
```

**Refresh continuous aggregates**

**Manually refresh a continuous aggregate**

Manually refresh the stored procedure of a continuous aggregate.

```
refresh_continuous_aggregate(
    cagg     REGCLASS,
    window_start             "any",
    window_end               "any"
```

); The following table describes the parameters.

| Parameter | Description |
|---|---|
| cagg | The name or OID of the continuous aggregate that you want to refresh. |
| window start _ | The start time of the refresh window. The data type must match the time field used in the continuous aggregate. If the start time is not aligned with the aggregation interval, you can align it with the nearest interval boundary by using the date trunc function. For _ example, if the continuous aggregate is performed at a 1-minute interval and the desired start time is 2024-03-11 13:01:29 , you can truncate it to 2024-03-11 13:01:00 . Setting this parameter to NULL is not recommended because this requires the database to determine the start time from the table data, which can be time-consuming if the dataset is large. |

| window end _ | The end time of the refresh window. The data type must match the time field used in the continuous aggregate. If the end time is unknown, you can set this parameter to NULL. When NULL is used, the refresh process updates the continuous aggregate up to the latest timestamp in the raw data table. |
|---|---|

**Usage notes**

Continuous aggregates are designed to precompute results for fixed time intervals. When you refresh a continuous aggregate, the refresh window must align with the predefined intervals of the aggregate. If they do not align, partial or incomplete intervals are ignored. If you call the `refresh_continuous_aggregate` function multiple times with overlapping refresh windows, overlapping intervals are recalculated only if there is new or modified data in those intervals. `refresh_continuous_aggregate` is a stored procedure function. You can invoke the function only by using the CALL statement.

**Example**

```
CALL refresh_continuous_aggregate('transaction_min_cagg', '2024-03-11 00:00:00+08'::timestamptz, NULL);
```

**Automate the refreshing of a continuous aggregate**

You can use one of the following methods to automate the refreshing of a continuous aggregate.

**(Recommended) Combine task scheduling with the refresh_continuous_aggregate**

**procedure**

The `add_job` function allows you to flexibly automate the refreshing of continuous aggregates. When using the function, you must distinguish between the `initial_start` and `window_start` parameters. The initial_start parameter specifies when the scheduled task first executes. The window_start parameter specifies the start time to refresh the continuous aggregate. The initial_start parameter must be a whole unit of time. If you set the parameter to NULL, the scheduled task is executed when it is created. If you set the parameter to a future time, the task begins execution at the specified time.

**Example**

1. Create a refresh policy.

```
CREATE OR REPLACE PROCEDURE transaction_min_cagg_refresh() LANGUAGE PLPGSQL AS
```

$$

```
DECLARE BEGIN
    -- Set the start time of the refresh window to '2024-03-11 00:00:00+08' and the e
nd time of the refresh window to NULL.
    CALL refresh_continuous_aggregate('transaction_min_cagg', '2024-03-11
00:00:00+08'::timestamptz, NULL); END $$;
```

2. Add the refresh task to the automated task execution queue. Schedule the procedure to
run at 1-minute intervals starting from `'2024-04-01 00:00:00+08'` .

```
SELECT add_job('transaction_min_cagg_refresh','1 min', initial_start => '2024-04-01 0 0:00:00+08'::timestamptz);
```

**Use the add_continuous_aggregate_policy function**

Create a refresh policy to automate the refreshing of a specified continuous aggregate.

```
integer add_continuous_aggregate_policy(
                cagg REGCLASS,
                start_offset "any",
                end_offset "any",
                schedule_interval INTERVAL,
                if_not_exists BOOL = false,
                initial_start TIMESTAMPTZ = NULL,
                timezone TEXT = NULL
```

); The following table describes the parameters.

| Parameter | Description |
|---|---|
| cagg | The name or OID of the continuous aggregate that you want to refresh. |
| start offset _ | The offset from the time when the function is executed to determine the start time of the refresh window. If you set this parameter to NULL, the refresh window starts from the earliest timestamp in the underlying hypertable. The start offset value must be earlier than the end offset value. _ _ |
| end offset _ | The offset from the time when the function is executed to determine the end time of the refresh window. If you set this parameter to NULL, the refresh window ends at the latest timestamp in the underlying hypertable. |
| schedule interval _ | The interval at which the continuous aggregate is refreshed. Default value: 1 day. |
| if not exists _ _ | Specifies whether an error is thrown if the refresh policy already exists. Valid values: true: A warning instead of an error is thrown if the refresh policy already exists. false (default): An error is thrown if the refresh policy already exists. |
| initial start _ | Specifies the first execution time of the refresh policy. Default value: NULL. If you specify the first execution time, it works in conjunction with the schedule interval parameter. _ |
| time zone _ | The time zone. Default value: NULL, which indicates that the time is displayed in UTC. |

**Example**

```
SELECT add_continuous_aggregate_policy('transaction_min_cagg',
    start_offset => '1 hour', -- The refresh window starts 1 hour before the current ti
me to ensure data completeness.
    end_offset => INTERVAL '0', -- The refresh window ends at the current time.
    schedule_interval => INTERVAL '1 sec' -- Refresh every second.
```

);

**Real-time query**

If real-time query is disabled when you perform continuous aggregate queries, the queries return only results based on data that has already been fully aggregated. To view newly received raw data that has not yet been aggregated, enable real-time query.

**Enable real-time query**

```
ALTER MATERIALIZED VIEW transaction_min_cagg SET (timescaledb.materialized_only = fal se);
```

**Disable real-time query**

```
ALTER MATERIALIZED VIEW transaction_min_cagg SET (timescaledb.materialized_only = tru e);
```

**Nested aggregation**

Nested aggregates create continuous aggregates based on the materialized views generated by continuous aggregates. For example, you can create a daily aggregate based on the hourly aggregate results, or create a monthly aggregate based on the daily aggregate results. This reduces data redundancy and improves the aggregate performance.
1. Create the first-level aggregation. In this example, the aggregation is performed at 1-
minute intervals.

```
CREATE MATERIALIZED VIEW transaction_min_cagg
    WITH (timescaledb.continuous) AS
    SELECT id,
        time_bucket(INTERVAL '1 min', tm) AS bucket,
        AVG(price) as avg,
        MAX(price) as max,
        MIN(price) as min
    FROM transaction_data
    GROUP BY id, bucket;
```

2. Create a nested aggregation, which aggregates data by 1-hour intervals based on the
results of the 1-minute aggregation.

```
CREATE MATERIALIZED VIEW transaction_one_hour_mview
    WITH (timescaledb.continuous) AS
    SELECT id,
        time_bucket(INTERVAL '1 hour', bucket) AS bucket,
        AVG(avg) as avg,
        MAX(max) as max,
        MIN(min) as min
    FROM transaction_min_cagg
    GROUP BY id, time_bucket(INTERVAL '1 hour', bucket);
```

**Time series compression**

If time series partitions are determined to be historical data, you can enable the data compression feature. GanosBase TSDB provides the compression feature for an entire table and for specified partitions. Compression can save data storage space. The compression ratio can be more than 70% to greatly reduce storage costs. Compressed data can only be read but not written.

**Uninstall the extension**

```
DROP EXTENSION ganos_tsdb CASCADE; DROP EXTENSION timescaledb CASCADE;
```

**Appendix 1: Terms**

**Time series data**: refers to the data recorded in chronological order. The characteristic of
this data type is that the data points not only contain numerical information, but also are associated with specific timestamps, reflecting the trend or pattern of a variable over time. Time series data is widely used in many fields, such as financial transactions, meteorological observation, sensor monitoring, web traffic analysis, and disease transmission research. The key elements of time series data include: Timestamps: Each data point has clear timestamps indicating when the data was collected. Observations: data values measured or recorded at various points in time. Sequentiality: Data points are arranged in chronological order, which reflects the time relationship between data points and the characteristics of time series. Trends and periodicity: Time series data analysis often focuses on long-term trends, seasonal fluctuations, cyclical changes, and random fluctuations in the data.
**Metrics**: monitoring metrics, such as temperature, stock price, and network traffic, that
can be quantified and measured. Metrics can help depict the behavior patterns of time series data, predict future trends, and discover and respond to anomalies in a timely manner.
**Aggregation**: the process of aggregating high-frequency data with low-frequency data in
time series data analysis. Data is merged or aggregated in time dimension to reduce the granularity of the data while keeping its main trends or characteristics. This approach is useful for data dimensionality reduction, trend analysis, anomaly detection, and the construction of predictive models.
**Downsampling**: can reduce the sampling frequency of time series data (or the number of
data points), and keep core features or trends of raw data. The following methods are often used for time series downsampling: Decimation: This is the most straightforward method. Decimation obtains a data point every N points. For example, if the original sequence is sampled 10 times per second, you can keep only the first one of every 5 data points to achieve sampling twice per second. This method is simple but may lose high-frequency information. Averaging: Consecutive data points are averaged before downsampling. For example, five consecutive data points are averaged to obtain a new data point. This method can smooth the data and reduce noise, but may obscure changing details. Median: This method is similar to the averaging method, but uses the median of consecutive data points instead of the average. It is more robust when dealing with time series containing outliers. Maximum or minimum: The maximum or minimum among consecutive data points is selected as the new data point. This method is applicable to scenarios where peak values or bottom values need to be retained. Resampling: adjusts data to a new time point by using methods such as interpolation, and then performs uniform sampling on the new time line. Common resampling methods include linear interpolation, nearest neighbor interpolation, and cubic interpolation. The resampling method is flexible and can be adjusted to any sampling frequency while maintaining the original data form. Model prediction downsampling: uses statistical or machine learning models to predict data points at lower sampling rate. For example, you can use models such as ARIMA and LSTM to predict values at each new point in time, and then use these predicted values as the data after downsampling. This method implements downsampling more intelligently, but incurs higher computational costs.

**Appendix 2: Comparison between Ganosbase TSDB and**

**TimescaleDB**

TimescaleDB: an open-source time series database built on top of PostgreSQL, optimized for managing time series data such as sensor readings, monitoring metrics, and financial data. It retains the full SQL functionality of PostgreSQL, and provides efficient storage, fast write, and complex query capabilities for time series data. GanosBase TSDB: a time series engine developed on top of TimescaleDB. It is provided as an extension of the PolarDB for PostgreSQL clusters and inherits all capabilities of PolarDB such as shared storage, one primary node and multiple read-only nodes, and backup and restoration. GanosBase TSDB and TimescaleDB mainly differ in features. TimescaleDB Apache 2 Edition is released under the Apache 2.0 license, which is an open-source license that allows users to use or modify the source code. However, this edition provides only basic features. GanosBase TSDB provides advanced features such as continuous aggregates, data series compression, and cold-hot tiered storage in Object Storage Service (OSS) in addition to the basic features provided by TimescaleDB.

### 12.4 Heterogeneous data access

#### 12.4.1 mysql_fdw

`mysql_fdw` is an open source third-party extension that allows PolarDB for PostgreSQL clusters to read data from and write data to PolarDB for MySQL instances, ApsaraDB RDS for MySQL instances, and self-managed MySQL instances.

**Usage notes**

You need to add the CIDR block of the virtual private cloud (VPC) to which the PolarDB for PostgreSQL cluster belongs to allow the cluster to communicate with the MySQL instance. An example CIDR block is 172.xx.xx.xx/16. PolarDB for PostgreSQL does not allow you to specify the host and port keywords in the OPTIONS statement. Use channel_name instead. By default, each cluster is configured with a channel named localhost, which is the channel to connect to the local server. If you want to connect to other clusters, create a channel first. If you need to configure the channel, contact us.

**Usage**

1. Create the mysql_fdw extension.

```
CREATE EXTENSION IF NOT EXISTS mysql_fdw;
```

Only privileged accounts can execute this statement.
2. Define a MySQL server.

```
CREATE SERVER <The server name>
    FOREIGN DATA WRAPPER mysql_fdw
    OPTIONS (channel_name 'The channel name');
```

PolarDB for PostgreSQL allows you to specify the connection information of the MySQL instance only by using channel_name in the OPTIONS statement. In the following sample code, a polar_channel named mysqlchannel is used:

```
CREATE SERVER mysql_server
     FOREIGN DATA WRAPPER mysql_fdw
     OPTIONS (channel_name 'mysqlchannel');
```

3. Create a user mapping that maps the MySQL server to an account in the PolarDB for
PostgreSQL cluster. You can use the account to read data from and write data to the MySQL database, which resides on the MySQL server.

```
CREATE USER MAPPING FOR <PolarDB for PostgreSQL username> SERVER <The name of the MySQL server> OPTIONS (username '<The MySQL username>', password '<The password of the MySQL user>'
```

); Example:

```
CREATE USER MAPPING FOR pgtest SERVER mysql_server OPTIONS (username 'mysqltest', password 'Test1234!');
```

4. Create a foreign table for the MySQL instance by using the PolarDB for PostgreSQL user
that is specified in Step 3. The field names in the foreign MySQL table must be the same as the field names in the table in the MySQL database. You can choose to create only the fields that you want to query. For example, if the table in the MySQL database contains the ID, NAME, and AGE fields, you can create the ID and NAME fields in the foreign MySQL table.

```
CREATE FOREIGN TABLE <Table name> (<Field name> <Data type>,<Field name> <Data type>...) server <Server name> options (dbname '<MySQL database name>', table_name '< MySQL table name>');
```

Example:

```
CREATE FOREIGN TABLE ft_test (id1 int, name1 text) server mysql_server options (dbnam e 'test123', table_name 'test');
```

5. Check whether you can perform read and write operations to the MySQL database.
You can use the foreign MySQL table to check whether you can perform read and write operations on the MySQL database. Data can be written to the table in the MySQL database only when the table is assigned a primary key. If the table is not assigned a primary key, the following error is returned:

```
ERROR: first column of remote table must be unique for INSERT/UPDATE/DELETE op eration. SELECT * FROM ft_test ; INSERT INTO ft_test VALUES (2,'abc'); INSERT 0 1 INSERT INTO ft_test SELECT generate_series(3,100),'abc'; INSERT 0 98 SELECT count(*) FROM ft_test ;
 count
------- (1 row)
```

View the execution plan to check how the requests sent by the PolarDB for PostgreSQL cluster to query data from the MySQL database are executed.

```
explain verbose SELECT count(*) FROM ft_test ;
                                  QUERY PLAN
-------------------------------------------------------------------------------
 Aggregate  (cost=1027.50..1027.51 rows=1 width=8)
   Output: count(*)
   ->  Foreign Scan on public.ft_test  (cost=25.00..1025.00 rows=1000 width=0)
         Output: id, info
         Remote server startup cost: 25
         Remote query: SELECT NULL FROM `test123`.`test`
(6 rows) explain verbose SELECT id FROM ft_test WHERE id=2;
                               QUERY PLAN
-------------------------------------------------------------------------
 Foreign Scan on public.ft_test  (cost=25.00..1025.00 rows=1000 width=4)
   Output: id
   Remote server startup cost: 25
   Remote query: SELECT `id` FROM `test123`.`test` WHERE ((`id` = 2))
(4 rows)
```

#### 12.4.2 oss_fdw

This topic describes the overview, limits, and usage of the oss_fdw extension.

**Overview**

`oss_fdw` is a foreign data wrapper (FDW) extension of PolarDB for PostgreSQL. It can associate data in Object Storage Service (OSS) with foreign table definitions in PolarDB clusters. This allows you to store data in database tables to OSS while you can still read and write data by executing standard SQL statements. OSS is a secure, cost-effective, and highly reliable cloud storage service that allows you to store a large amount of data. OSS provides multiple storage classes to help you manage and reduce storage costs. Historical data, read-only archived data, and cold data in databases are ideal for being stored in OSS to save storage costs.

**Prerequisites**

OSS is activated and a bucket is created.

**Limits**

| oss fdw _ |   | foreig |
|---|---|---|
| not the |   |   |

`oss_fdw` foreign tables support only the `SELECT` , `INSERT` , and `TRUNCATE` statements, not the `UPDATE` or `DELETE` statements. Therefore, the extension is only used to archive data. After data is written to OSS, it can only be read and cannot be updated.

**Usage**

**Install the oss_fdw extension**

```
CREATE EXTENSION oss_fdw;
```

**Create a foreign data server**

Configure OSS connection information and create a mapping between PolarDB and the OSS bucket. Example:

```
CREATE SERVER ossserver FOREIGN DATA WRAPPER oss_fdw OPTIONS (
    host 'oss-cn-xxx.aliyuncs.com',
    bucket 'mybucket',
    id 'xxx',
    key 'xxx'
```

); Parameters in the statement: `host` : the endpoint of OSS. `bucket` : the name of the OSS bucket. `id` / `key` : the AccessKey ID and AccessKey secret of your Alibaba Cloud account.

**Map a foreign table to an OSS directory**

1. Create an OSS foreign table in PolarDB and map it tothe directory for the foreign data
source as specified in Create a foreign data server.

```
CREATE FOREIGN TABLE t1_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (dir 'archive/');
```

2. Import data to the OSS foreign table.

```
INSERT INTO t1_oss VALUES (generate_series(1,100), 0.1, 'hello');
```

The data inserted into the table is written to the file in the `archive/` directory of OSS. You can query the foreign table by using the following method.

```
EXPLAIN SELECT COUNT(*) FROM t1_oss;
```

Sample result:

```
                           QUERY PLAN
-----------------------------------------------------------------
 Aggregate  (cost=6.54..6.54 rows=1 width=8)
   ->  Foreign Scan on t1_oss  (cost=0.00..6.40 rows=54 width=0)
         Directory on OSS: archive/
         Number Of OSS file: 1
         Total size of OSS file: 1292 bytes
(5 rows) SELECT COUNT(*) FROM t1_oss;
```

Sample result:

```
 count
------- (1 row)
```

When the `INSERT` statement is executed on the table again, the data is written to a new file in the OSS directory.

```
INSERT INTO t1_oss VALUES (generate_series(1,100), 0.1, 'hello');
```

Query data in the table:

```
EXPLAIN SELECT COUNT(*) FROM t1_oss;
```

Sample result:

```
                            QUERY PLAN
-------------------------------------------------------------------
 Aggregate  (cost=12.07..12.08 rows=1 width=8)
   ->  Foreign Scan on t1_oss  (cost=0.00..11.80 rows=108 width=0)
         Directory on OSS: archive/
         Number Of OSS file: 2
         Total size of OSS file: 2584 bytes
(5 rows) SELECT COUNT(*) FROM t1_oss;
```

Sample result:

```
 count
------- (1 row)
```

Execute the `TRUNCATE` statement to remove all OSS mapping files for the foreign table.

```
TRUNCATE t1_oss;
```

Query data in the table after file removal:

```
SELECT COUNT(*) FROM t1_oss;
```

Sample result:

```
WARNING: does not match any file in oss
 count
------- (1 row)
```

**Map a foreign table to a directory prefix**

1. Create a foreign table by using the `prefix` option.

```
CREATE FOREIGN TABLE t2_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (prefix 'prefix/file_');
```

2. Multiple files with the same prefix name are created when you execute the INSERT
statement on the foreign table.

```
INSERT INTO t2_oss VALUES (generate_series(1,100), 0.1, 'hello'); INSERT INTO t2_oss VALUES (generate_series(1,100), 0.1, 'hello'); EXPLAIN SELECT COUNT(*) FROM t2_oss;
```

Sample result:

```
                            QUERY PLAN
-------------------------------------------------------------------
 Aggregate  (cost=12.07..12.08 rows=1 width=8)
   ->  Foreign Scan on t2_oss  (cost=0.00..11.80 rows=108 width=0)
         Directory on OSS: prefix/file_
         Number Of OSS file: 2
         Total size of OSS file: 2584 bytes
(5 rows)
```

Query data in the table:

```
SELECT COUNT(*) FROM t2_oss;
```

Sample result:

```
 count
------- (1 row)
```

**OSS file storage format**

`oss_fdw` allows you to set the format of data stored in OSS. The default value is `CSV` . You can also explicitly specify the format. When you execute the `INSERT` statement on the OSS foreign table, data is written in the `CSV` format to an OSS file.

```
CREATE FOREIGN TABLE t3_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (dir 'archive_csv/', format 'csv');
```

**View the files for the OSS foreign table**

1. Create an OSS foreign table and execute the `INSERT` statement three times to write data
to three OSS files.

```
CREATE FOREIGN TABLE t4_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (dir 'archive_file_list/'); INSERT INTO t4_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t4_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t4_oss VALUES (generate_series(1,10000), 0.1, 'hello');
```

2. View the files for the OSS foreign table by using the following function and specifying the
table name and schema name of the OSS foreign table. The default name is `public` . Use the default schema name to query the files for the OSS foreign table.

```
SELECT * FROM oss_fdw_list_file('t4_oss');
```

Sample result:

```
                   name                    |  size
-------------------------------------------+--------
 archive_file_list/_t4_oss_783053364762580 | 148894
 archive_file_list/_t4_oss_783053364849053 | 148894
 archive_file_list/_t4_oss_783053366496328 | 148894
(3 rows)
```

Use a specified schema name to query the files for the OSS foreign table.

```
SELECT * FROM oss_fdw_list_file('t4_oss', 'public');
```

Sample result:

```
                   name                    |  size
-------------------------------------------+--------
 archive_file_list/_t4_oss_783053364762580 | 148894
 archive_file_list/_t4_oss_783053364849053 | 148894
 archive_file_list/_t4_oss_783053366496328 | 148894
(3 rows)
```

**OSS compression**

The `compressiontype` parameter specifies the compression algorithm for writing data to OSS files. This parameter is left empty by default, which indicates that data is not compressed. Valid values: gzip and zstd. The `compressionlevel` parameter specifies a compression level. A higher compression level indicates that more CPU is occupied during compression and decompression, and that a smaller data volume is transferred over the network and less OSS space is used by the foreign table.

**Gzip compression algorithm**

Valid values of the compression level for the Gzip compression algorithm: 1 to 9. Default value: 6.

```
CREATE FOREIGN TABLE t5_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (
    dir 'archive_file_compression/',
    compressiontype 'gzip',
    compressionlevel '9'
```

);

```
INSERT INTO t5_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t5_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t5_oss VALUES (generate_series(1,10000), 0.1, 'hello');
```

When you view the files for the OSS foreign table, the sizes of Gzip-compressed files are significantly smaller than those of the files that are not compressed. Query the sizes of non-Gzip-compressed files for the OSS foreign table:

```
SELECT * FROM oss_fdw_list_file('t4_oss');
```

Sample result:

```
                   name                    |  size
-------------------------------------------+--------
 archive_file_list/_t4_oss_741147680906121 | 148894
 archive_file_list/_t4_oss_741147680965631 | 148894
 archive_file_list/_t4_oss_741147681201236 | 148894
(3 rows)
```

Query the sizes of Gzip-compressed files for the OSS foreign table:

```
SELECT * FROM oss_fdw_list_file('t5_oss');
```

Sample result:

```
                        name                         | size
-----------------------------------------------------+-------
 archive_file_compression/_t5_oss_741147752563794.gz | 23654
 archive_file_compression/_t5_oss_741147752633713.gz | 23654
 archive_file_compression/_t5_oss_741147752828680.gz | 23654
(3 rows)
```

**Zstandard compression algorithm**

Valid values of the compression level for the Zstandard compression algorithm: -7 to 22. Default value: 6.

```
CREATE FOREIGN TABLE t6_oss (
    id INT,
    f FLOAT,
    txt TEXT
```

`)`

```
SERVER ossserver OPTIONS (
    dir 'archive_file_zstd/',
    compressiontype 'zstd',
    compressionlevel '9'
```

);

```
INSERT INTO t6_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t6_oss VALUES (generate_series(1,10000), 0.1, 'hello'); INSERT INTO t6_oss VALUES (generate_series(1,10000), 0.1, 'hello');
```

When you view the files for the OSS foreign table, the sizes of Zstandard-compressed files are significantly smaller than those of the files that are not compressed. Query the sizes of non-Zstandard-compressed files for the OSS foreign table:

```
SELECT * FROM oss_fdw_list_file('t4_oss');
```

Sample result:

```
                   name                    |  size
-------------------------------------------+--------
 archive_file_list/_t4_oss_741147680906121 | 148894
 archive_file_list/_t4_oss_741147680965631 | 148894
 archive_file_list/_t4_oss_741147681201236 | 148894
(3 rows)
```

Query the sizes of Zstandard-compressed files for the OSS foreign table:

```
SELECT * FROM oss_fdw_list_file('t6_oss');
```

Sample result:

```
                     name                      | size
-----------------------------------------------+------
 archive_file_zstd/_t6_oss_748106174612293.zst | 6710
 archive_file_zstd/_t6_oss_748106174700206.zst | 6710
 archive_file_zstd/_t6_oss_748106174866829.zst | 6710
(3 rows)
```

**Uninstall the oss_fdw extension**

```
DROP EXTENSION oss_fdw;
```

### 12.5 WAL logical decoding

#### 12.5.1 decoderbufs (decode to ProtoBuf)

decoderbufs is an output plugin for the PostgreSQL logical decoder that decodes data into the Protocol Buffers format for logical replication.

**Usage notes**

The decoderbufs extension depends on the following libraries: PostgreSQL: Engine version 9.6 or later. Protobuf-c: Version 1.2 or later, for data serialization. PostGIS: Version 2.1 or later, to support PostgreSQL spatial geographic types.

**Usage**

The decoderbufs extension is loaded automatically by default, so you do not need to load it manually. You must set the wal_level parameter to logical. This setting adds the information required for logical decoding to the write-ahead logging (WAL). The wal_level parameter can be modified in the console. The cluster restarts after you modify the parameter. Proceed with caution. The following example shows how to perform logical replication:
1. Create a logical replication slot and set the decoder plugin to decoderbufs.

```
SELECT * FROM pg_create_logical_replication_slot('decoderbufs_demo', 'decoderbufs');
```

2. On the publisher instance, modify the table that you want to replicate.
3. Use the decoderbufs debug mode to view the WAL log.

```
SELECT data FROM pg_logical_slot_peek_changes('decoderbufs_demo', NULL, NULL, 'debugmode', '1');
```

4. Use decoderbufs to retrieve WAL changes and update the WAL position.

```
SELECT data FROM pg_logical_slot_get_changes('decoderbufs_demo', NULL, NULL, 'debug-m ode', '1');
```

5. View the WAL position of the logical replication.

```
SELECT * FROM pg_replication_slots WHERE slot_type = 'logical';
```

**Type mapping**

The following table describes the mapping between PostgreSQL types and decoderbufs fields.

| PostgreSQL type | Decoderbuf field |
|---|---|
| BOOLOID | datum boolean _ |
| INT2OID | datum int32 _ |
| INT4OID | datum int32 _ |

| INT8OID | datum int64 _ |
|---|---|
| OIDOID | datum int64 _ |
| FLOAT4OID | datum float _ |
| FLOAT8OID | datum double _ |
| NUMERICOID | datum double _ |
| CHAROID | datum string _ |
| VARCHAROID | datum string _ |
| BPCHAROID | datum string _ |
| TEXTOID | datum string _ |
| JSONOID | datum string _ |
| XMLOID | datum string _ |
| UUIDOID | datum string _ |
| TIMESTAMPOID | datum string _ |
| TIMESTAMPTZOID | datum string _ |
| BYTEAOID | datum bytes _ |
| POINTOID | datum point _ |
| PostGIS geometry | datum point _ |
| PostGIS geography | datum point _ |

#### 12.5.2 wal2json

PolarDB for PostgreSQL provides the wal2json plug-in to generate logical log files in the JSON format.

**Background information**

wal2json is a logic decoding plug-in that provides the following features: Access tuples generated by executing the `INSERT` and `UPDATE` statements. Access `UPDATE` and `DELETE` old row versions depending on the specified duplicate identity. Consume changes by using the streaming protocol (logical replication slots) or special SQL APIs. The wal2json plug-in produces a JSON object for each transaction. All new and old tuples are available in the JSON object. In addition, options include properties such as transaction timestamp, qualified schema, data type, and transaction ID.

**Usage notes**

Because PolarDB for PostgreSQL uses the replication method of `REPLICA_IDENTITY_FULL` , the entire row of data is displayed during UPDATE and DELETE, instead of the columns before and after UPDATE and DELETE. To modify only the columns before and after UPDATE, you must set the `polar_create_table_with_full_replica_identity` parameter to off. This parameter cannot be modified in the console. You must contact technical support to modify the parameter. The wal2json plug-in requires logical encoding and decoding. You must modify the `wal_level` parameter to `logical` . The wal_level parameter can be modified in the console. The cluster restarts after you modify the parameter. Proceed with caution.

**Execute SQL statements to obtain JSON objects**

You do not need to execute the `CREATE EXTENSION` statement to create the wal2json plug-in. You can create a logical replication slot to load the wal2json plug-in.
1. After you create a logical replication slot that contains the wal2json plug-in, execute the
following statement to obtain the JSON object in WAL:

```
-- Create tables with and without primary keys. CREATE TABLE table2_with_pk (a SERIAL, b VARCHAR(30), c TIMESTAMP NOT NULL, PRIMARY K EY(a, c)); CREATE TABLE table2_without_pk (a SERIAL, b NUMERIC(5,2), c TEXT); -- Create a logical replication slot of the wal2json type. SELECT 'init' FROM pg_create_logical_replication_slot('test_slot', 'wal2json'); -- Commit a transaction and write it to WAL. BEGIN; INSERT INTO table2_with_pk (b, c) VALUES('Backup and Restore', now()); INSERT INTO table2_with_pk (b, c) VALUES('Tuning', now()); INSERT INTO table2_with_pk (b, c) VALUES('Replication', now()); DELETE FROM table2_with_pk WHERE a < 3; INSERT INTO table2_without_pk (b, c) VALUES(2.34, 'Tapir'); UPDATE table2_without_pk SET c = 'Anta' WHERE c = 'Tapir'; COMMIT; -- Obtain the JSON object in WAL. SELECT data FROM pg_logical_slot_get_changes('test_slot', NULL, NULL, 'pretty-print', '1');
```

Sample result: `{`

```json
    "change": [
```

`{`

```json
            "kind": "insert",
            "schema": "public",
            "table": "table2_with_pk",
            "columnnames": ["a", "b", "c"],
            "columntypes": ["integer", "character varying(30)", "timestamp without
time zone"],
            "columnvalues": [1, "Backup and Restore", "2018-03-27 12:05:29.914496"]
```

`}` `,{`

```json
            "kind": "insert",
            "schema": "public",
            "table": "table2_with_pk",
            "columnnames": ["a", "b", "c"],
            "columntypes": ["integer", "character varying(30)", "timestamp without
time zone"],
            "columnvalues": [2, "Tuning", "2018-03-27 12:05:29.914496"]
```

`}` `,{`

```json
            "kind": "insert",
            "schema": "public",
            "table": "table2_with_pk",
            "columnnames": ["a", "b", "c"],
            "columntypes": ["integer", "character varying(30)", "timestamp without
time zone"],
            "columnvalues": [3, "Replication", "2018-03-27 12:05:29.914496"]
```

`}` `,{`

```json
            "kind": "delete",
            "schema": "public",
            "table": "table2_with_pk",
            "oldkeys": {
                "keynames": ["a", "c"],
                "keytypes": ["integer", "timestamp without time zone"],
                "keyvalues": [1, "2018-03-27 12:05:29.914496"]
```

`}` `}` `,{`

```json
            "kind": "delete",
            "schema": "public",
            "table": "table2_with_pk",
            "oldkeys": {
                "keynames": ["a", "c"],
                "keytypes": ["integer", "timestamp without time zone"],
                "keyvalues": [2, "2018-03-27 12:05:29.914496"]
```

`}` `}` `,{`

```json
            "kind": "insert",
            "schema": "public",
            "table": "table2_without_pk",
            "columnnames": ["a", "b", "c"],
            "columntypes": ["integer", "numeric(5,2)", "text"],
            "columnvalues": [1, 2.34, "Tapir"]
```

`}` `]` `}`
2. Delete the `test_slot` replication slot and return the string `'stop'` .

```
SELECT 'stop' FROM pg_drop_replication_slot('test_slot');
```

**Parameters**

The following table describes the parameters related to the wal2json plug-in.

| Parameter | Description |
|---|---|
| change | The WAL entry for each DML, such as the WAL records for INSERT, UPDATE, DELETE, and TRUNCATE. |
| changeset | A set of several changes. |
| include-xids | Specifies whether to add xid to each changeset. Default value: false. Valid values: true false |

| include-timestamp | Specifies whether to add a timestamp to each changeset. Default value: false. Valid values: true false |
|---|---|
| include-schemas | Specifies whether to add a schema to each change. Default value: true. Valid values: true false |
| include-types | Specifies whether to add a type to each change. Default value: true. Valid values: true false |
| include-typmod | Specifies whether to add a modifier to types that have it, such as varchar(20) instead of varchar. Default value: true. Valid values: true false |
| include-type-oids | Specifies whether to add the type oids. Default value: false. Valid values: true false |
| include-not-null | Specifies whether to add not null information as columnoptionals. Default value: false. Valid values: true false |
| pretty-print | Specifies whether to add spaces and indents to the JSON structure for formatting. Default value: false. Valid values: true false |
| write-in-chunks | Specifies whether to write data after each change instead of each changeset. Default value: false. Valid values: true false |

| include-lsn | Specifies whether to add nextlsn to each changeset. Default value: false. Valid values: true false |
|---|---|
| filter-tables | Excludes rows from the specified tables. By default, this parameter is empty, indicating that no table is excluded. Note Separate multiple tables with commas (,). You must specify a schema for each table. *.foo indicates table foo in all schemas, while bar.* indicates all tables in schema bar. Special characters (space, single quote, comma, period, asterisk) must be escaped with backslashes (\). Schemas and tables are case-sensitive. Table Foo bar in schema public must be specified as public.Foo\bar . |
| add-tables | Includes only rows from the specified tables. By default, all tables from all schemas are parsed. For more information, see filter- tables. |
| filter-msg-prefixes | Excludes rows with the specified prefix. This parameter is typically used in the pg logical slot peek changes() function. By _ _ _ _ default, this parameter is empty, indicating that no row is excluded. Separate multiple prefixes with commas (,). |
| add-msg-prefixes | Includes rows with the specified prefix. This parameter is typically used in the pg logical slot peek changes() function. By _ _ _ _ default, all prefixes are selected. Separate multiple prefixes with commas (,). You must use filter-msg-prefixes before this parameter. |
| format-version | Defines which output format to use. Default value: 1. Valid values: 1: uses format version 1. 2: uses format version 2. |
| actions | Specifies which operations are sent. By default, all operations, including INSERT, UPDATE, DELETE, and TRUNCATE, are sent. If format-version 1 is used, the TRUNCATE operation is not sent. |

**Examples**

`include-xids` is used in the following examples.
1. Create a table and a logical replication slot. Insert a row of data.

```
DROP TABLE IF EXISTS tbl; CREATE TABLE tbl (id int); SELECT 'init' FROM pg_create_logical_replication_slot('regression_slot', 'wal2json'); INSERT INTO tbl VALUES (1);
```

2. Enter the parameters and values in the function.

```
SELECT count(*) = 1, count(distinct ((data::json)->'xid')::text) = 1 FROM pg_logical_slot_get_changes( 'regression_slot', NULL, NULL, 'format-version', '1', 'include-xids', '1');
```

### 12.6 Similarity calculation

#### 12.6.1 hll

This topic describes the hll extension, which supports the HyperLogLog data type to estimate metrics such as page views (PVs) and unique visitors (UVs).

**Background information**

The hll extension supports an extendable, set-resembled data type HyperLogLog (hll) to estimate DISTINCT elements under a specified accuracy. For example, you can use 1,280 bytes of hll data to accurately estimate billions of DISTINCT elements. The hll extension is suitable for industries that need estimation analysis, such as Internet advertisement analysis, to estimate PVs and UVs.

**Install the hll extension**

```
CREATE EXTENSION hll;
```

**Basic operations**

Execute the following statement to create a table that contains hll fields:

```
CREATE TABLE agg (id INT PRIMARY KEY, userids hll);
```

Execute the following statement to convert INT data to hll_hashval data:

```
SELECT 1::hll_hashval;
```

Sample result:

```
 hll_hashval
------------- (1 row)
```

**Basic operators**

The hll data type supports the following operators: = != <>
||
#
Examples: =

```
SELECT hll_add_agg(1::hll_hashval) = hll_add_agg(2::hll_hashval);
```

Sample result:

```
 ?column?
----------
```

`f`

```
(1 row)
```

||

```
SELECT hll_add_agg(1::hll_hashval) || hll_add_agg(2::hll_hashval);
```

Sample result:

```
                 ?column?
------------------------------------------
 \x128b7f00000000000000010000000000000002
(1 row)
```

#

```
SELECT #hll_add_agg(1::hll_hashval);
```

Sample result:

```
 ?column?
---------- (1 row)
```

The hll_hashval data type supports the following operators: = != <> Examples: =

```
SELECT 1::hll_hashval = 2::hll_hashval;
```

Sample result:

```
 ?column?
----------
```

`f`

```
(1 row)
```

<>

```
SELECT 1::hll_hashval <> 2::hll_hashval;
```

Sample result:

```
 ?column?
----------
```

`t`

```
(1 row)
```

**Basic functions**

The hll extension supports hash functions such as hll_hash_boolean, hll_hash_smallint, and hll_hash_bigint. Examples:

```
SELECT hll_hash_boolean(true);
```

Sample result:

```
  hll_hash_boolean
---------------------
 8849112093580131862
(1 row) SELECT hll_hash_integer(1);
```

Sample result:

```
   hll_hash_integer
----------------------
 -8604791237420463362
(1 row)
```

The hll extension supports the hll_add_agg function to convert the data type from INT to hll. Example:

```
SELECT hll_add_agg(1::hll_hashval);
```

Sample result:

```
       hll_add_agg
--------------------------
 \x128b7f0000000000000001
(1 row)
```

The hll extension supports the hll_union function to perform UNION operations on hll data. Example:

```
SELECT hll_union(hll_add_agg(1::hll_hashval), hll_add_agg(2::hll_hashval));
```

Sample result:

```
                hll_union
------------------------------------------
 \x128b7f00000000000000010000000000000002
(1 row)
```

The hll extension supports the hll_set_defaults function to set the accuracy. Example:

```
SELECT hll_set_defaults(15,5,-1,1);
```

Sample result:

```
 hll_set_defaults
------------------
 (11,5,-1,1)
(1 row)
```

The hll extension supports the hll_print function to display debug information. Example:

```
SELECT hll_print(hll_add_agg(1::hll_hashval));
```

Sample result:

```
                                  hll_print
-----------------------------------------------------------------------------
 EXPLICIT, 1 elements, nregs=32768, nbits=5, expthresh=-1(2560), sparseon=1:+
 0:                    1
(1 row)
```

**Uninstall the hll extension.**

```
DROP EXTENSION hll;
```

**Examples**

1. Prepare basic data.

```
CREATE TABLE access_date (acc_date DATE UNIQUE, userids hll); INSERT INTO access_date
     SELECT current_date, hll_add_agg(hll_hash_integer(user_id))
     FROM generate_series(1,10000) t(user_id);
INSERT INTO access_date
     SELECT current_date-1, hll_add_agg(hll_hash_integer(user_id))
     FROM generate_series(5000,20000) t(user_id);
INSERT INTO access_date
     SELECT current_date-2, hll_add_agg(hll_hash_integer(user_id))
     FROM generate_series(9000,40000) t(user_id);
```

2. Execute the following query statements.

```
SELECT #userids FROM access_date WHERE acc_date=current_date;
```

Sample result:

```
     ?column?
------------------
 9725.852733707077
(1 row) SELECT #userids FROM access_date WHERE acc_date=current_date-1;
```

Sample result:

```
     ?column?
------------------
 14968.65968832792
(1 row) SELECT #userids FROM access_date WHERE acc_date=current_date-2;
```

Sample result:

```
     ?column?
------------------
 29361.520914991113
(1 row)
```

#### 12.6.2 imgsmlr (similar images)

`imgsmlr` is a third-party extension for PolarDB for PostgreSQL and supports similar image searches. The `imgsmlr` extension uses the `Haar` wavelet transform algorithm to fetch feature values from images, such as PNG and GIF files. It then uses an index to retrieve similar images.

**Usage**

**Data types**

The `imgsmlr` extension provides two data types: `pattern` and `signature` .

| Data type | Storage size | Description |
|---|---|---|
| pattern | 16,388 bytes | The result of a Haar wavelet transform on an image. |
| signature | 64 bytes | A compact representation of a pattern. A Generalized Search Tree (GiST) index can be used for fast searches. |

**Functions**

The `imgsmlr` extension provides several functions. You can use these functions to convert

| to the | pattern |   |
|---|---|---|
| pattern |   |   |
|   |   | type t |

various image types to the `pattern` type. The extension also provides a function to create a

| Functions | Data type of return value | Description |
|---|---|---|
| jpeg2pattern(byte a) | pattern | Converts a JPEG image to the pattern type. |
| png2pattern(byte a) | pattern | Converts a PNG image to the pattern type. |
| gif2pattern(bytea) | pattern | Converts a GIF image to the pattern type. |
| pattern2signature (pattern) | signature | Creates a signature from a pattern. |
| shuffle pattern(pa _ ttern) | pattern | Shuffles a pattern to reduce sensitivity to image offset. |

**Operators**

| pattern |   | and | signature |   |
|---|---|---|---|---|
| The |   |   |   | type also |

Both the `pattern` and `signature` types support the `<->` operator for Euclidean distance. The `signature` type also supports a GiST index on the `<->` operator.

| Operator | Data type of the left operand | Data type of the right operand | Data type of return value | Description |
|---|---|---|---|---|
| <-> | pattern | pattern | float8 | Calculates the Euclidean distance between two images of the pattern type. |

| <-> | signature | signature | float8 | Calculates the Euclidean distance between two images of the signature type. |
|---|---|---|---|---|

**Examples**

**Install the extension**

```
CREATE EXTENSION imgsmlr;
```

**Create a table for image feature values**

Assume that an `image` table exists and it contains an `id` column and a `data` column. The `data` column contains binary JPEG data. You can execute the following SQL statement to create a table that contains the `pattern` and `signature` for the images.

```
CREATE TABLE pat AS (
 SELECT
  id,
  shuffle_pattern(pattern) AS pattern,
  pattern2signature(pattern) AS signature
 FROM (
  SELECT
   id,
   jpeg2pattern(data) AS pattern
  FROM
   image
 ) x
```

);

**Create a GiST index**

```
ALTER TABLE pat ADD PRIMARY KEY (id); CREATE INDEX pat_signature_idx ON pat USING gist (signature);
```

**Search for similar images**

| pecified id , us ve the top 100 pattern to find | id |   | , us |
|---|---|---|---|
| pattern |   |   |   |

To find the top `10` images that are most similar to an image with a specified `id` , use a subquery. The subquery uses a GiST index on the `signature` to retrieve the top `100` candidate images. The outer query then searches these candidates by `pattern` to find the top `10` matches.

```
SELECT
 id,
 smlr
FROM
```

`(`

```
 SELECT
  id,
  pattern <-> (SELECT pattern FROM pat WHERE id = :id) AS smlr
 FROM pat
 WHERE id <> :id
 ORDER BY
  signature <-> (SELECT signature FROM pat WHERE id = :id)
 LIMIT 100
) x ORDER BY x.smlr ASC LIMIT 10;
```

**Uninstall the extension**

```
DROP EXTENSION imgsmlr;
```

#### 12.6.3 smlar

Similarity calculation of large amounts of data is key in areas such as e-commerce and search engine. Simple implementations of similarity calculation consume large amounts of resources and provide low performance. smlar is an open-source third-party extension for PolarDB for PostgreSQL. It provides functions that can calculate data similarity in databases and similarity operators that support Generalized Search Tree (GiST) and Generalized Inverted Index (GIN) indexes. The smlar extension supports all built-in data types of PostgreSQL.

**Usage**

1. Install the smlar extension.

```
CREATE EXTENSION smlar;
```

The % operator of the smlar extension conflicts with that of the rum extension. Therefore, you cannot create the two extensions in the same schema.
2. Execute the following statement to calculate the similarity of two arrays.

```
SELECT smlar('{3,2}'::int[], '{3,2,1}');
```

Sample result:

```
----------
 0.816497
(1 row)
```

```
SELECT smlar('{1,4,6}'::int[], '{5,4,6}', 'N.i / (N.a + N.b)' );
```

Sample result:

```
----------
 0.333333
(1 row)
```

For more information about other functions, see the **Functions and operators** section of this topic.
3. Uninstall the smlar extension.

```
DROP EXTENSION smlar;
```

**Functions and operators**

| Function and operator | Description |
|---|---|
| float4 smlar(anyarray, anyarray) | Calculates the similarity of two arrays of the same data type. The arrays must use the same data type. |
| float4 smlar(anyarray, anyarray, bool useIntersect) | Calculates the similarity of two arrays of custom composite types (elements and weights). The useIntersect parameter specifies whether only overlapping elements or all elements are involved in the operation. Note Execute the following statement to define composite types: CREATE TYPE type name AS (element name anytype, _ _ weight name FLOAT4); _ |
| float4 smlar(anyarray a, anyarray b, text formula) | Calculates the similarity between two arrays of the same data type. The arrays are specified by the formula parameter. The predefined variables for the formula parameter are described as follows: N.i: the number of identical elements in two arrays (intersection). N.a: the number of unique elements in the first array. N.b: the number of unique elements in the second array. |
| anyarray % anyarray | Returns TRUE if the similarity of the two arrays exceeds the threshold. Otherwise, returns FALSE. |

| text[] tsvector2textarray(tsvector) | Converts an array of the tsvector type to a string. |
|---|---|
| anyarray array unique(anyarray) _ | Sorts and deduplicates the array. |
| float4 inarray(anyarray, anyelement) | Returns 1.0 if the element exists in the array. Otherwise, returns 0. |
| float4 inarray(anyarray, anyelement, float4, float4) | Returns the third parameter if the element exists in the array. Otherwise, returns the fourth parameter. |

**Parameters**

| Parameter | Description |
|---|---|
| smlar.threshold FLOAT | The similarity threshold. It is used to determine whether two arrays combined with the percent sign (%) operator are similar. |
| smlar.persistent cache BOOL _ | Specifies whether to store the cached global statistics in transaction-independent memory. |
| smlar.type STRING | The formula used to calculate the similarity. The following similarity types are available: cosine (default), tfidf, and overlap. |
| smlar.stattable STRING | The name of the table that stores collection range statistics. You can execute the following statement to create a table: CREATE TABLE table name ( _ value data type UNIQUE, _ ndoc int4 (or bigint) NOT NULL CHECK (ndoc>0) ); |
| smlar.tf method STRING _ | The method used to calculate the term frequency (TF). Default value: n. Valid values: n: simple counting log: 1 + log(n) const: 1 |
| smlar.idf plus one BOOL _ _ | The method used to calculate the inverse document frequency (IDF). Default value: FALSE. Valid values: FALSE: log(d/df) TRUE: log(1 + d/df) |

### 12.7 Full-text search

#### 12.7.1 Quick start

This topic describes the basic operations of full-text search for PolarDB for PostgreSQL, including extension installation and uninstallation, table creation, index creation, and performing queries.

**Install the extension**

```
CREATE EXTENSION rum;
```

If you need to use the Chinese word segmentation feature, you can install the extension for Chinese word segmentation by executing the following statement:

```
CREATE EXTENSION pg_jieba;
```

**Create a table**

Create a table for English text:

```
CREATE TABLE test_english(id serial, t text, d timestamp);
```

Create a table for Chinese text:

```
CREATE TABLE test_chinese(id serial, t text, d timestamp, v tsvector);
```

**Insert data**

Populate the English table with test data:

```
INSERT INTO test_english(t,d) VALUES ('The situation is most beautiful', '2016-05-01 20:21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It is a beautiful', '2016-05-01 21:21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It looks like a beautiful place', '2016-05-01 22:21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It looks l a beautiful place', '2016-05-02 00: 21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It looks like a beautiful places', '2016-05-02 02:21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It looks like a beaut places', '2016-05-02 03: 21:22.326724'); INSERT INTO test_english(t,d) VALUES ('It looks like a pig', '2016-05-02 03:21:22.326724');
```

Populate the Chinese table with test data: `INSERT INTO test_chinese(t,d) VALUES ('`南财理财通数据显示，`5`月公募理财产品吸金榜前十名归属于`5` 家机构，信银理财有`5`只产品上榜，南银理财占两席，民生理财、恒丰理财、浦银理财各占一席，上榜产品均为中低风险的封闭式固收类产品。从投资周期看，本月榜单产品中有`6`只产品投资周期为`1-2`年，`3-6`个月及`6-12`个月期限

```
产品各有2只。 ', '2016-05-01 20:21:22.326724');
```

`INSERT INTO test_chinese(t,d) VALUES ('`其中，信银理财“安盈象固收稳利十四个月封闭式`95`号”理财产品夺得吸金榜冠军，募集规模达到`106.204` 亿元；民生理财“富竹固收优选`14`个月封闭`39`号”位列第二，募集规模为`46.606`亿元；信银理财“安盈象固收稳利十四个月封闭式`94`号”排名第三，募集规模为`41.365` 亿元。 `', '201`

```
6-05-01 20:21:22.326724');
```

`INSERT INTO test_chinese(t,d) VALUES ('5`月新发产品募集规模最大的是信银理财“安盈象固收稳利十四个月封闭式`95`号”，实际募集资金高达`106.204`亿元，该系列产品已蝉联`4`个月榜首。 `', '2016-05-01`

```
20:21:22.326724');
```

`INSERT INTO test_chinese(t,d) VALUES ('`南财理财通数据显示，“安盈象固收稳利十四个月封闭式`95`号” 理财产品成立于`2024`年`05`月`16`日，将于`2025`年`07`月`16`日到期，风险评级`PR2`（中低风险），产品有`A`、`C`、`D`、`K`类份额，投资周期`1-2`年，业绩比较基准2.90%~3.45%。 ', '2016-05-01 20:21:22.326724');

```
-- This operation can be performed by executing an update operation or using a trigge
```

`r.`

```
UPDATE test_chinese SET v = to_tsvector('jiebacfg', t);
```

**Create an index**

Create an index for the English table:

```
CREATE INDEX ON test_english USING rum (t rum_text_ops);
```

Create an index for the Chinese table:

```
CREATE INDEX ON test_chinese USING rum (v rum_tsvector_ops);
```

**Perform queries**

Perform queries on the English table: Query rows that contain the `beautiful` or `place` keyword:

```
SELECT * FROM test_english WHERE to_tsvector('english', t) @@ to_tsquery('english', 'beautiful | place');
```

Sample result:

```
id | t | d ----+----------------------------------+----------------------------
  1 | The situation is most beautiful  | 2016-05-01 20:21:22.326724
  2 | It is a beautiful                | 2016-05-01 21:21:22.326724
  3 | It looks like a beautiful place  | 2016-05-01 22:21:22.326724
  4 | It looks l a beautiful place     | 2016-05-02 00:21:22.326724
  5 | It looks like a beautiful places | 2016-05-02 02:21:22.326724
  6 | It looks like a beaut places     | 2016-05-02 03:21:22.326724
```

Query rows that contain the `beautiful` or `place` keyword, calculate the similarity between each record and the keyword, and sort the results in descending order of similarity.

```
SELECT *, to_tsvector('english', t) <=> to_tsquery('english', 'beautiful | place') AS rank FROM test_english WHERE to_tsvector('english', t) @@ to_tsquery('english', 'beautiful | place') ORDER BY to_tsvector('english', t) <=> to_tsquery('english', 'beautiful | place') D ESC;
```

Sample result:

```
 id |                t                 |             d              |  rank
----+----------------------------------+----------------------------+---------
  1 | The situation is most beautiful  | 2016-05-01 20:21:22.326724 | 16.4493
  2 | It is a beautiful                | 2016-05-01 21:21:22.326724 | 16.4493
  6 | It looks like a beaut places     | 2016-05-02 03:21:22.326724 | 16.4493
  3 | It looks like a beautiful place  | 2016-05-01 22:21:22.326724 | 8.22467
  4 | It looks l a beautiful place     | 2016-05-02 00:21:22.326724 | 8.22467
  5 | It looks like a beautiful places | 2016-05-02 02:21:22.326724 | 8.22467
(6 rows)
```

Perform queries on the Chinese table: Query rows that contain the 数据 or 理财 keyword:

```
SELECT id, v <=> to_tsquery('jiebacfg', '数据 | 理财') as rank FROM test_chinese where v @@ to_tsquery('jiebacfg', '数据 | 理财');
```

Sample result:

```
 id |   rank
----+-----------
  1 | 6.6024785
  2 |  12.08523
  3 |  16.44934
  4 |   8.22467
```

| ds that contain '数据 \| 理财' | 数据 , and re |
|---|---|

| n | v |   |
|---|---|---|
| id |   |   |

```
SELECT id, v <=> to_tsquery('jiebacfg', '数据 | 理财') as rank FROM test_chinese where v @@ to_tsquery('jiebacfg', '数据');
```

Sample result:

```
 id |   rank
----+-----------
  1 | 6.6024785
  4 |   8.22467
```

**(Optional) Uninstall the extension**

```
DROP EXTENSION rum CASCADE; DROP EXTENSION pg_jieba CASCADE;
```

#### 12.7.2 pg_bigm

The pg_bigm extension in PolarDB for PostgreSQL supports full-text search and allows you to create a 2-gram Generalized Inverted Index (GIN) index to accelerate full-text search.

**Usage notes**

The size of the column on which you create a GIN index cannot exceed 107,374,180 bytes, which is approximately 102 MB. Example:

```
CREATE TABLE t1 (description text); CREATE INDEX t1_idx ON t1 USING gin (description gin_bigm_ops); INSERT INTO t1 SELECT repeat('A', 107374181);
```

If the data in your PolarDB cluster is not encoded in the ASCII format, we recommend that you change the encoding format to UTF-8. Execute the following statement to query the encoding format of the current database:

```
SELECT pg_encoding_to_char(encoding) FROM pg_database WHERE datname = current_database();
```

**Basic operations**

Create the pg_bigm extension.

```
CREATE EXTENSION pg_bigm;
```

When you create a GIN index, you must specify the operators provided by the `pg_bigm` extension.

```
CREATE TABLE pg_tools (tool text, description text); INSERT INTO pg_tools VALUES ('pg_hint_plan', 'Tool that allows a user to specify an o ptimizer HINT to PostgreSQL'); INSERT INTO pg_tools VALUES ('pg_dbms_stats', 'Tool that allows a user to stabilize p lanner statistics in PostgreSQL'); INSERT INTO pg_tools VALUES ('pg_bigm', 'Tool that provides 2-gram full text search c apability in PostgreSQL'); INSERT INTO pg_tools VALUES ('pg_trgm', 'Tool that provides 3-gram full text search c apability in PostgreSQL'); CREATE INDEX pg_tools_idx ON pg_tools USING gin (description gin_bigm_ops); CREATE INDEX pg_tools_multi_idx ON pg_tools USING gin (tool gin_bigm_ops, description gin_bigm_ops) WITH (FASTUPDATE = off);
```

Perform full-text search.

```
SELECT * FROM pg_tools WHERE description LIKE '%search%';
```

Sample result:

```
  tool   |                             description
---------+---------------------------------------------------------------------
 pg_bigm | Tool that provides 2-gram full text search capability in PostgreSQL
 pg_trgm | Tool that provides 3-gram full text search capability in PostgreSQL
(2 rows)
```

Use the =% operator to perform a similarity search.

```
SELECT tool FROM pg_tools WHERE tool =% 'bigm';
```

Sample result:

```
  tool
--------- (1 row)
```

Uninstall the pg_bigm extension.

```
DROP EXTENSION pg_bigm;
```

**Basic functions**

likequery Purpose: generates a string that can be identified based on the LIKE keyword. Request parameters: one request parameter of the STRING type. Return value: a string that can be identified based on the LIKE keyword. Implementation: Add a percent sign ( % ) before and after the keyword. Use a backward slash ( \ ) to escape the percent sign ( % ). Example:

```
SELECT likequery('pg_bigm has improved the full text search performance by 200%')
```

; Sample result:

```
                             likequery
-------------------------------------------------------------------
 %pg\_bigm has improved the full text search performance by 200\%%
(1 row) SELECT * FROM pg_tools WHERE description LIKE likequery('search');
```

Sample result:

```
  tool   |                             description
---------+---------------------------------------------------------------------
 pg_bigm | Tool that provides 2-gram full text search capability in PostgreSQL
 pg_trgm | Tool that provides 3-gram full text search capability in PostgreSQL
(2 rows)
```

show_bigm Purpose: obtains all 2-gram elements of a string. Request parameters: one request parameter of the STRING type. Return value: an array that consists of all 2-gram elements of a string. Implementation: Add a space before and after the string. Identify all 2-gram elements in the string. Example:

```
SELECT show_bigm('full text search');
```

Sample result:

```json
                            show_bigm
------------------------------------------------------------------
 {" f"," s"," t",ar,ch,ea,ex,fu,"h ","l ",ll,rc,se,"t ",te,ul,xt}
(1 row)
```

bigm_similarity Purpose: obtains the similarity between two strings. Request parameters: two request parameters of the STRING type. Return value: a floating-point number that indicates the similarity between the two strings. Implementation: Identify the 2-gram elements that are included in both of the two strings. The return value ranges from 0 to 1. A value of 0 indicates that the two strings are different. A value of 1 indicates that the two strings are the same. This function adds a space before and after each string. Therefore, the similarity between the `ABC` string and the `B` string is 0, and the similarity between the `ABC` string and the `A` string is 0.25. This function is case-sensitive. For example, this function determines that the similarity between the `ABC` string and the `abc` string is 0. Example:

```
SELECT bigm_similarity('full text search', 'text similarity search');
```

Sample result:

```
 bigm_similarity
-----------------
        0.571429
(1 row) SELECT bigm_similarity('ABC', 'A');
```

Sample result:

```
 bigm_similarity
-----------------
            0.25
(1 row) SELECT bigm_similarity('ABC', 'B');
```

Sample result:

```
 bigm_similarity
----------------- (1 row) SELECT bigm_similarity('ABC', 'abc');
```

Sample result:

```
 bigm_similarity
----------------- (1 row)
```

pg_gin_pending_stats Purpose: obtains the number of pages and the number of tuples in the pending list of a GIN index. Request parameters: one parameter that specifies the name or OID of the GIN index. Return value: the number of pages and the number of tuples in the pending list of the GIN index. If you set the **FASTUPDATE** parameter to **False** for a GIN index, the GIN index does not have a pending list. In this case, this function returns two values, 0 and 0. Example:

```
SELECT * FROM pg_gin_pending_stats('pg_tools_idx');
```

Sample result:

```
 pages | tuples
-------+--------
     0 |      0
(1 row)
```

**Behavior control parameters**

pg_bigm.enable_recheck This parameter specifies whether to perform a recheck. We recommend that you use the default value ON. This way, you can obtain accurate query results. Example: i. Prepare test data.

```
CREATE TABLE tbl (doc text); INSERT INTO tbl VALUES('He is awaiting trial'); INSERT INTO tbl VALUES('It was a trivial mistake'); CREATE INDEX tbl_idx ON tbl USING gin (doc gin_bigm_ops);
```

ii. Execute the following statements. Use the default value of the pg_bigm.enable_recheck parameter to perform a recheck.

```
SET enable_seqscan TO off; EXPLAIN ANALYZE SELECT * FROM tbl WHERE doc LIKE likequery('trial');
```

Sample result:

```
                                                   QUERY PLAN
----------------------------------------------------------------------------------- ----------------------------
 Bitmap Heap Scan on tbl  (cost=20.00..24.01 rows=1 width=32) (actual time=0.020.
.0.021 rows=1 loops=1)
   Recheck Cond: (doc ~~ '%trial%'::text)
   Rows Removed by Index Recheck: 1
   Heap Blocks: exact=1
   ->  Bitmap Index Scan on tbl_idx  (cost=0.00..20.00 rows=1 width=0) (actual ti
me=0.013..0.013 rows=2 loops=1)
         Index Cond: (doc ~~ '%trial%'::text)
 Planning Time: 0.117 ms
 Execution Time: 0.043 ms
(8 rows)
```

Execute the following statement:

```
SELECT * FROM tbl WHERE doc LIKE likequery('trial');
```

Sample result:

```
         doc
----------------------
 He is awaiting trial
(1 row)
```

Set the pg_bigm.enable_recheck parameter to off to prevent performing a recheck.

```
SET pg_bigm.enable_recheck = off; SELECT * FROM tbl WHERE doc LIKE likequery('trial');
```

Sample result:

```
           doc
--------------------------
 He is awaiting trial
 It was a trivial mistake
(2 rows)
```

pg_bigm.gin_key_limit This parameter specifies the maximum number of 2-gram elements that can be used to perform a full-text search. The default value is 0, which specifies that all 2-gram elements are used. If query performance decreases due to the use of all 2-gram elements, you can decrease the value of this parameter. pg_bigm.similarity_limit This parameter specifies the threshold for similarity. The tuples between which the similarity exceeds the specified threshold are returned as similarity search results.

**Appendix: Comparison between the pg_bigm extension and the**

**pg_trgm extension**

The pg_trgm extension in PolarDB for PostgreSQL uses the 3-gram model to implement fulltext search. The pg_bigm extension is developed based on the pg_trgm extension. The following table describes the differences between the two extensions.

| Functionality | pg trgm _ | pg bigm _ |
|---|---|---|
| Phrase matching model | 3-gram | 2-gram |
| Index types | GIN and Generalized Search Tree (GiST) | GIN |
| Operators | LIKE , ILIKE , ~ , and ~* | LIKE |
| Non-alphabet full-text search | Not supported | Supported |
| Full-text search by using keywords that contain 1 to 2 characters | Slow | Fast |
| Similarity search | Supported | Supported |
| Maximum size of an indexed column | 238,609,291 bytes, which are approximately 228 MB | 107,374,180 bytes, which are approximately 102 MB |

#### 12.7.3 pg_jieba

pg_jieba is an open source third-party extension used for full-text search in Chinese.

**Overview**

The pg_jieba extension provides the following text search modes: jiebacfg: exact mode. This mode precisely splits the text without redundant words. jiebaqry: full mode. This mode obtains all matching words in the text. Redundant words may exist. jiebacfg_pos: exact mode (with subscript position). The subscript information of each word is added to the result of the exact mode. The stopwords that are ignored in exact mode (highly frequent words that are not used in the search) are also displayed.

**Usage**

**Install and uninstall the extension**

Only privileged accounts are authorized to execute the following statements. Install the pg_jieba extension.

```
CREATE EXTENSION pg_jieba;
```

Uninstall the pg_jieba extension.

```
DROP EXTENSION pg_jieba;
```

**Examples**

**Example 1**

jiebacfg: exact mode. `SELECT * FROM to_tsvector('jiebacfg', '`小明硕士毕业于中国科学院计算所，后在日本京都大学深造'); Sample result:

```
                                   to_tsvector
----------------------------------------------------------------------------------
```

`'`中国科学院`':5 '`小明`':1 '`日本京都大学`':10 '`毕业`':3 '`深造`':11 '`硕士`':2 '`计算所`':6`

```
(1 row)
```

jiebaqry: full mode. `SELECT * FROM to_tsvector('jiebaqry', '`小明硕士毕业于中国科学院计算所，后在日本京都大学深造'); Sample result:

```
                                                                           to_tsvector
--------------------------------------------------------------------------------------- ------------------------------------------------------------------------
```

`'`中国`':5 '`中国科学院`':9 '`京都`':16 '`大学`':17 '`学院`':7 '`小明`':1 '`日本`':15 '`日本京都大学`':18 '` 毕业`':3 '`深造`':19 '`硕士`':2 '`科学`':6 '`科学院`':8 '`计算`':10 '`计算所`':11`

```
(1 row)
```

jiebacfg_pos: exact mode (with subscript position). `SELECT * FROM to_tsvector('jiebacfg_pos', '`小明硕士毕业于中国科学院计算所，后在日本京都大学深造'); Sample result:

```
                                                               to_tsvector
--------------------------------------------------------------------------------------- -------------------------------------------------
```

`'`中国科学院`:7':5 '`于`:6':4 '`后`:16':8 '`在`:17':9 '`小明`:0':1 '`日本京都大学`:18':10 '`毕业`:4':3 '` 深造`:24':11 '`硕士`:2':2 '`计算所`:12':6 '`，`:15':7`

```
(1 row)
```

**Example 2**

jiebacfg: exact mode. `SELECT * FROM to_tsvector('jiebacfg', '`李小福是创新办主任也是云计算方面的专家'); Sample result:

```
                            to_tsvector
-------------------------------------------------------------------
```

`'`专家`':11 '`主任`':5 '`云计算`':8 '`创新`':3 '`办`':4 '`方面`':9 '`李小福`':1`

```
(1 row)
```

jiebaqry: full mode. `SELECT * FROM to_tsvector('jiebaqry', '`李小福是创新办主任也是云计算方面的专家'); Sample result:

```
                                 to_tsvector
-----------------------------------------------------------------------------
```

`'`专家`':12 '`主任`':5 '`云计算`':9 '`创新`':3 '`办`':4 '`方面`':10 '`李小福`':1 '`计算`':8`

```
(1 row)
```

jiebacfg_pos: exact mode (with subscript position). `SELECT * FROM to_tsvector('jiebacfg_pos', '`李小福是创新办主任也是云计算方面的专家'); Sample result:

```
                                                        to_tsvector
--------------------------------------------------------------------------------------- ----------------------------------
```

`'`专家`:17':11 '`主任`:7':5 '`也`:9':6 '`云计算`:11':8 '`创新`:4':3 '`办`:6':4 '`方面`:14':9 '`是`:10':7` `'`是`:3':2 '`李小福`:0':1 '`的`:16':10`

```
(1 row)
```

**Extended features**

The pg_jieba extension allows you to configure multiple custom dictionaries and switch between the dictionaries.

|   | Important To use custom dictionaries, you need to add pg jieba to the _ shared preload libraries parameter. You can configure the _ _ shared preload libraries parameter in the console. The cluster restarts after you _ _ configure this parameter. Proceed with caution. |   |
|---|---|---|

1. Insert data into the first custom dictionary. By default, data is inserted into the first custom
dictionary. The first custom dictionary is represented by 0. The weight value of the first custom dictionary is 10.

```
INSERT INTO jieba_user_dict VALUES ('阿里云'); INSERT INTO jieba_user_dict VALUES ('研发工程师',0,10);
```

2. Use the dictionary predefined in the pg_jieba extension to segment Chinese text.
`SELECT * FROM to_tsvector('jiebacfg', 'zth`是阿里云的一个研发工程师'); Sample result:

```
                     to_tsvector
------------------------------------------------------
```

`'zth':1 '`一个`':6 '`云`':4 '`工程师`':8 '`研发`':7 '`阿里`':3`

```
(1 row)
```

3. Switch to custom dictionary 0.

```
SELECT jieba_load_user_dict(0);
```

Sample result:

```
 jieba_load_user_dict
---------------------- (1 row)
```

4. Use custom dictionary 0 to split words.
`SELECT * FROM to_tsvector('jiebacfg', 'zth`是阿里云的一个研发工程师'); Sample result:

```
                to_tsvector
--------------------------------------------
```

`'zth':1 '`一个`':5 '`研发工程师`':6 '`阿里云`':3`

```
(1 row)
```

#### 12.7.4 rum (full-text search acceleration)

When a standard Generalized Inverted Index (GIN) is used for full-text search, performance may degrade in scenarios such as result sorting, phrase queries, and sorting by timestamp. A GIN index stores neither token positions nor additional information, which leads to an additional scan during query execution. The `RUM` extension addresses GIN performance bottlenecks by storing token positions or additional columns, such as timestamps, in the RUM index. As a result, the `RUM` extension is efficient in full-text search scenarios that require sorting and can improve query performance. It is suitable for applications that require sorting by relevance or time, such as log analysis and article search.

**Background information**

GIN indexes support full-text search using the `tsvector` and `tsquery` data types, but they have the following issues:
**Slow sorting**: Sorting requires word position information. Because GIN indexes do not
store this information, an additional scan is required to retrieve it after the index scan.
**Slow phrase queries**: GIN indexes require position information to perform phrase
searches.
**Slow timestamp sorting**: GIN indexes cannot store related information in an index that
contains lexemes. Therefore, an additional scan is required. The `RUM` extension is based on GIN indexes. It solves these issues by storing extra information, such as word or timestamp positions, in the RUM index. RUM indexes take longer to build and have slower insert performance than GIN indexes. This is because RUM indexes must store additional information in addition to keys and use general Write-Ahead Logging (WAL) records.

**rum general operators**

The `RUM` extension provides the following operators:

| Operator | Return value data type | Description |
|---|---|---|
| tsvector <=> tsquery | float4 | Calculates the distance between a tsvector and a tsquery . |
| timestamp <=> timestamp | float8 | Calculates the distance between two timestamps. |
| timestamp <=\| timestamp | float8 | Calculates the distance for all timestamps that are earlier than the current timestamp. |
| timestamp \|=> timestamp | float8 | Calculates the distance for all timestamps that are later than the current timestamp. |

The `<=>` , <=| , and |=> operators also apply to the following data types:

```
 timestamptz
 int2
 int4
 int8
 float4
 float8
 money
 oid
```

**Usage**

**Install the RUM extension**

You can execute the following SQL statement to install the RUM extension.

```
CREATE EXTENSION rum;
```

**Function usage**

The `rum_tsvector_ops` operator class stores `tsvector` lexemes with position information. It supports sorting by the `<=>` operator and prefix search. Example: i. Prepare the test data:

```
CREATE TABLE test_rum(t text, a tsvector); CREATE TRIGGER tsvectorupdate
    BEFORE UPDATE OR INSERT ON test_rum
    FOR EACH ROW
    EXECUTE PROCEDURE tsvector_update_trigger('a', 'pg_catalog.english', 't');
INSERT INTO test_rum(t) VALUES ('The situation is most beautiful'); INSERT INTO test_rum(t) VALUES ('It is a beautiful'); INSERT INTO test_rum(t) VALUES ('It looks like a beautiful place');
```

ii. Create a rum index:

```
CREATE INDEX rumidx ON test_rum USING rum (a rum_tsvector_ops);
```

iii. Execute the following query statements: Query statement 1:

```
SELECT t, a <=> to_tsquery('english', 'beautiful | place') AS rank FROM test_rum WHERE a @@ to_tsquery('english', 'beautiful | place') ORDER BY a <=> to_tsquery('english', 'beautiful | place');
```

The following result is returned:

```
                t                |   rank
---------------------------------+----------
 It looks like a beautiful place |  8.22467
 The situation is most beautiful | 16.44934
 It is a beautiful               | 16.44934
(3 rows)
```

Query statement 2:

```
SELECT t, a <=> to_tsquery('english', 'place | situation') AS rank FROM test_rum WHERE a @@ to_tsquery('english', 'place | situation') ORDER BY a <=> to_tsquery('english', 'place | situation');
```

The following result is returned:

```
                t                |   rank
---------------------------------+----------
 The situation is most beautiful | 16.44934
 It looks like a beautiful place | 16.44934
(2 rows)
```

The `rum_tsvector_hash_ops` operator class stores the hash values and position

| mation of | tsvector |
|---|---|

information of `tsvector` lexemes. It supports sorting by the `<=>` operator, but does not support prefix search. The `rum_tsvector_hash_ops` operator class supports sorting using the `<=>` , <=| ,

|   | rum tsvector addon ops _ _ _ |
|---|---|
| rum anyarray addon ops _ _ _ |   |

and |=> operators. It can be used with the `rum_tsvector_addon_ops` , The `rum_TYPE_ops` operator class supports the following data types and operators:

| le data types: int2 , int4 , int8 , float4 , float8 , money , oid , timetz , date , interval , macaddr , inet , cidr , text , varchar bytea , bit , varbit , numeric , timestamp , and timestamptz . |   | , | float4 |   |   | , | float8 |   |   | , , | money |   | , | oid |   | , |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   | varchar |   |   |   |
|   |   |   |   | , |   |   | , | cidr |   |   | text | , |   |   |   |   |
| bytea |   | , |   |   |   |   |   | , and |   |   |   |   |   |   | . |   |

|   |   |   |   |   |   |   | int4 |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | date |   |   |   |   | interval |   |   |   |
|   |   |   |   |   | , |   |   |   |   |
| bit |   |   |   |   |   |   |   |   |   |
|   |   |   | , |   |   |   |   | , |   |

| operators: The < <=> , <=\| , and float8 , money , |   |   | < | , <= |
|---|---|---|---|---|
|   |   |   |   | \|=> |
| float8 |   |   |   |   |
|   | , |   |   | oid |

Supported operators: The `<` , `<=` , `=` , `>=` , and `>` operators support all data

|   | int2 | , | int4 |   |
|---|---|---|---|---|
| timestamptz |   |   |   |   |
|   |   |   |   | dat |

types. The `<=>` , <=| , and |=> operators support the `int2` , `int4` , `int8` , `float4` , `float8` , `money` , `oid` , `timestamp` , and `timestamptz` data types. The `rum_tsvector_addon_ops` operator class stores `tsvector` lexemes and values in an addon field. Example: i. Prepare data:

```
CREATE TABLE tsts (id int, t tsvector, d timestamp); \copy tsts from 'external/rum/data/tsts.data' CREATE INDEX tsts_idx ON tsts USING rum (t rum_tsvector_addon_ops, d) WITH (attach = 'd', to = 't');
```

Click to view the tsts.data test data

```
1 2016-05-01 20:21:22.326724 2 2016-05-01 21:21:22.326724 3 2016-05-01 22:21:22.326724 4 2016-05-01 23:21:22.326724 5 2016-05-02 00:21:22.326724 6 2016-05-02 01:21:22.326724 7 2016-05-02 02:21:22.326724 8 2016-05-02 03:21:22.326724 9'b9''c9''cc''cx''di''ec''eo''f5''fn''gd''ge''gh''hc''hy''i8''if''
```

```
9 b9 c9 cc cx di ec eo f5 fn gd ge gh hc hy i8 if iq' 'ir' 'ix' 'ja' 'jl' 'jx' 'km' 'l5' 'l8' 'le' 'mm' 'oc' 'pr' 'qg' 'qo' 'rm' 'ro' 'rv' 'sm' 'td' 'th' 'tm' 'tx' 'u7' 'uc' 'ue' 'uk' 'ux' 'vw' 'wa' 'wb' 'wd' 'wh' 'wr ' 'ww' 'xa' 'xj' 'xz' 'y4' 'yd' 'yl' 'ym' 'zf' 'zv' 2016-05-02 04:21:22.326724 10 'a9' 'ag' 'bh' 'dk' 'dq' 'e3' 'e7' 'ea' 'ee' 'ej' 'et' 'ez' 'f1' 'gh' 'gn' 'gr' 'hb' 'hf' 'hh' 'hz' 'ip' 'iw' 'j7' 'jh' 'ki' 'kp' 'kx' 'ml' 'nu' 'ov' 'ow' 'pg' 'ph ' 'pn' 'po' 'pu' 'qd' 'qe' 'qr' 'qs' 'qv' 'r2' 'r3' 'rb' 'rd' 'ry' 's3' 'sd' 'sr' ' su' 'sz' 'tp' 'ty' 'uh' 'un' 'v0' 'v4' 'w0' 'wa' 'wk' 'wq' 'wx' 'xe' 'y6' 'yd' 'yf' 'yj' 'yl' 'zt' 2016-05-02 05:21:22.326724 11 'de' 'mc' 'q1' 'q8' 'qp' 'qt' 'rq' 'rv' 'sa' 'sn' 'u8' 'vs' 'w9' 'wo' 'wp' 'ww' 'yl' 2016-05-02 06:21:22.326724 12 '4w' 'ad' 'ak' 'as' 'b3' 'bd' 'cy' 'dt' 'du' 'dy' 'e2' 'e4' 'en' 'es' 'et' 'ew' 'ex' 'f2' 'fl' 'fr' 'ft' 'gv' 'h1' 'ha' 'hd' 'hh' 'hs' 'hv' 'ic' 'io' 'ja' 'jm' 'k2 ' 'ku' 'kw' 'ld' 'ls' 'lx' 'ma' 'nu' 'ny' 'ov' 'pm' 'ps' 'q6' 'qa' 'qd' 'qo' 'qs' ' qv' 'qy' 'ra' 'rs' 'rt' 'rv' 'rw' 's8' 'sa' 'sw' 'tj' 'ug' 'ui' 'ur' 'ut' 'ux' 'v6' 'vt' 'w4' 'w7' 'wa' 'wb' 'wc' 'wg' 'wh' 'wi' 'wt' 'wu' 'wy' 'wz' 'x2' 'xb' 'xm' 'yg ' 'yh' 'yi' 'yu' 'yy' 'z5' 'zg' 'zo' 2016-05-02 07:21:22.326724 13 '2r' '7g' 'a1' 'ar' 'av' 'b8' 'dj' 'dr' 'e7' 'ee' 'fd' 'fn' 'fp' 'gf' 'gp' 'gq' 'gw' 'jm' 'jv' 'ke' 'ki' 'kl' 'l9' 'lc' 'lg' 'lh' 'nm' 'oc' 'oq' 'px' 'q6' 'qe' 'qh ' 'qu' 'rs' 's8' 't0' 'tt' 'tw' 'u2' 'uu' 'uy' 'vr' 'vs' 'wg' 'wt' 'ww' 'x3' 'x5' ' xu' 'yw' 'zh' 'zp' 'zt' 2016-05-02 08:21:22.326724 14 'a9' 'av' 'aw' 'dj' 'e0' 'ej' 'er' 'eu' 'ez' 'fr' 'gq' 'hh' 'hp' 'ko' 'kq' 'lw' 'n8' 'pe' 'pl' 'pn' 'pp' 'pv' 'q9' 'qc' 'qj' 'qs' 'qw' 'r6' 'rl' 'tq' 'u5' 'uu' 'uz ' 'wn' 'wp' 'wr' 'zo' 2016-05-02 09:21:22.326724 15 '0p' 'ab' 'as' 'az' 'b5' 'bl' 'cn' 'cr' 'ct' 'cu' 'dq' 'dr' 'em' 'eq' 'fe' 'fj' 'fk' 'fy' 'gn' 'gx' 'h9' 'hg' 'hk' 'hr' 'io' 'iy' 'jh' 'la' 'lb' 'll' 'ln' 'lq' 'me ' 'mp' 'mr' 'mv' 'ns' 'od' 'op' 'os' 'ov' 'po' 'pv' 'qa' 'qn' 'qp' 'qs' 'qt' 'r0' ' rc' 'rd' 'rl' 's5' 'si' 't7' 'tc' 'th' 'u0' 'um' 'uz' 'vg' 'vo' 'wa' 'wp' 'wu' 'xk' 'yg' 'yh' 'yi' 'yo' 'yy' 'zy' 2016-05-02 10:21:22.326724 16 'a3' 'a5' 'ai' 'av' 'ay' 'c3' 'cp' 'd3' 'dn' 'du' 'dz' 'e9' 'ed' 'ei' 'ek' 'em' 'eo' 'ev' 'f2' 'gh' 'gl' 'gy' 'h6' 'h8' 'hb' 'he' 'hg' 'hm' 'hp' 'hy' 'hz' 'id' 'ie ' 'it' 'ix' 'j2' 'ja' 'jc' 'jf' 'k5' 'ki' 'kk' 'kv' 'l4' 'l6' 'ls' 'm9' 'mg' 'mt' ' nb' 'ng' 'oh' 'ot' 'oz' 'pw' 'py' 'pz' 'q0' 'q3' 'q8' 'qb' 'qh' 'qj' 'qk' 'ql' 'qp' 'qq' 'qr' 'qt' 'qw' 'rb' 'rz' 's3' 'sl' 'tb' 'u0' 'u5' 'uo' 'us' 'vc' 'wg' 'wh' 'wj ' 'wr' 'wt' 'wu' 'wy' 'x1' 'y1' 'yh' 'z7' 'zf' 'zs' 'zu' 2016-05-02 11:21:22.326724 17 'bt' 'c5' 'd1' 'd7' 'g6' 'gk' 'ib' 'iv' 'ml' 'om' 'qd' 'qg' 'ql' 'r3' 'rc' 'u4' 'uh' 'uo' 'wh' 'y0' 'yn' 'yz' 'zo' 2016-05-02 12:21:22.326724 18 '7a' 'a3' 'dl' 'fo' 'hb' 'ki' 'kk' 'lo' 'pl' 'q5' 'qy' 'r1' 'rj' 'sy' 'tv' 'w3' 'wm' 'wn' 'yj' 'yr' 'zi' 'zq' 2016-05-02 13:21:22.326724 19 'av' 'aw' 'bl' 'bt' 'cj' 'cx' 'df' 'ea' 'ed' 'ee' 'ef' 'ew' 'f5' 'fq' 'ft' 'fu' 'g6' 'gl' 'gs' 'ha' 'hj' 'hr' 'i8' 'ia' 'ic' 'ir' 'iz' 'j0' 'j5' 'jp' 'ju' 'k6' 'ki ' 'lk' 'lz' 'mh' 'nl' 'o4' 'ob' 'oo' 'op' 'pf' 'po' 'pq' 'pr' 'q2' 'q3' 'q6' 'qd' ' qj' 'qk' 'qn' 'qt' 'qw' 'ro' 'rr' 'ru' 'rv' 'sc' 'sw' 'sy' 'sz' 't2' 'tb' 'tg' 'tl' 'tp' 'tv' 'u4' 'u9' 'um' 'uu' 'vj' 'vt' 'vu' 'wg' 'wh' 'wj' 'wo' 'wq' 'wt' 'xd' 'y1 ' 'yc' 'ye' 'yl' 'yw' 'zb' 'zd' 'zm' 'zr' 2016-05-02 14:21:22.326724 20 'ja' 'k2' 'ko' 'o6' 'ob' 'ps' 't9' 'tz' 'uk' 'um' 'vv' 2016-05-02 15:21:22.326724 21 'dq' 'ed' 'el' 'fg' 'fv' 'gh' 'hx' 'i2' 'iv' 'jc' 'la' 'ld' 'nb' 'oa' 'of' 'oi' 'py' 'q7' 'qe' 'qr' 'qs' 'qw' 'qx' 'qz' 'rl' 'rr' 'sp' 't3' 'te' 'ti' 'tu' 'ue' 'w0 ' 'wa' 'wq' 'wu' 'xn' 2016-05-02 16:21:22.326724 22 'ah' 'ao' 'aq' 'aw' 'az' 'b5' 'bd' 'bg' 'bj' 'bq' 'bu' 'cc' 'cv' 'dt' 'e0' 'e2' 'e4' 'ec' 'eu' 'fd' 'fi' 'gg' 'gu' 'ha' 'hb' 'he' 'hj' 'hy' 'ih' 'in' 'iv' 'ji' 'js ' 'ks' 'l1' 'la' 'lg' 'mh' 'mi' 'mk' 'o7' 'oh' 'oj' 'om' 'on' 'op' 'oq' 'or' 'os' ' p1' 'pe' 'pq' 'pv' 'q8' 'qe' 'qg' 'qj' 'ql' 'qm' 'qn' 'qo' 'qr' 'qs' 'qt' 'qv' 'qy' 'r1' 'r9' 'rb' 'rl' 'ro' 'ru' 'rw' 'ry' 's0' 's6' 'sn' 't0' 't1' 'tr' 'ty' 'u0' 'u8
```

```
' 'up' 'uv' 'vn' 'wb' 'wg' 'ww' 'x1' 'yb' 'yj' 'ym' 'yx' 'zz' 2016-05-02 17:21:22.3 26724 23 'a9' 'aa' 'aq' 'ay' 'bb' 'cg' 'db' 'de' 'do' 'e4' 'e5' 'e9' 'ek' 'ep' 'er' 'fi' 'fp' 'gb' 'hj' 'hk' 'hw' 'ir' 'iy' 'l1' 'lj' 'mb' 'nq' 'oi' 'pj' 'px' 'q9' 'qe' 'qu ' 'qw' 'qz' 'rh' 'rl' 'sv' 'tc' 'ts' 'tv' 'uo' 'ur' 'vh' 'vp' 'w7' 'wf' 'wh' 'wo' ' wr' 'xu' 'z4' 'zc' 'zv' 2016-05-02 18:21:22.326724 24 '6u' 'a5' 'ai' 'au' 'b1' 'be' 'bg' 'by' 'ce' 'co' 'cw' 'db' 'dw' 'e8' 'ec' 'em' 'en' 'er' 'f7' 'fh' 'fu' 'gb' 'gq' 'h4' 'hf' 'hy' 'hz' 'ig' 'iq' 'kj' 'kk' 'kp' 'ky ' 'ld' 'lr' 'na' 'nd' 'ny' 'o8' 'o9' 'og' 'oh' 'ok' 'ot' 'ou' 'ow' 'ox' 'p8' 'pl' ' pp' 'ps' 'px' 'q0' 'q1' 'qa' 'qm' 'qr' 'qs' 'qx' 'r9' 'rd' 're' 'rf' 'rl' 'rn' 'rr' 'ru' 'rz' 'sc' 'sn' 'so' 't1' 'tl' 'tr' 'ts' 'tt' 'tx' 'ub' 'um' 'un' 'uo' 'ut' 'vr ' 'wa' 'wb' 'wc' 'wj' 'wl' 'wp' 'wq' 'ws' 'wx' 'wz' 'yp' 'yt' 'yy' 'zc' 2016-05-02 19:21:22.326724 25 '2v' '7j' '7r' 'a7' 'aj' 'av' 'br' 'cg' 'd8' 'ei' 'en' 'ez' 'f5' 'fb' 'go' 'h0' 'hf' 'hk' 'hm' 'i9' 'ia' 'ig' 'ik' 'im' 'iq' 'it' 'iv' 'ja' 'je' 'ji' 'ks' 'lo' 'mo ' 'mq' 'nj' 'o5' 'of' 'on' 'ot' 'ox' 'p1' 'p6' 'pb' 'ph' 'pj' 'pn' 'pp' 'pq' 'pr' ' qa' 'qh' 'qj' 'qm' 'qn' 'qo' 'qu' 'r2' 'ro' 's1' 'sa' 'se' 'sp' 't6' 'ti' 'tu' 'u2' 'ug' 'uh' 'ui' 'ur' 'uy' 'v9' 'wl' 'wn' 'wt' 'wv' 'wy' 'wz' 'xm' 'xs' 'ya' 'yi' 'yu ' 'z8' 'zl' 2016-05-02 20:21:22.326724 26 '27' '2e' '2p' 'aa' 'eh' 'en' 'eq' 'eu' 'ew' 'ff' 'g8' 'hv' 'mx' 'oi' 'pd' 'q3' 'qs' 'rl' 'sa' 'sw' 'te' 'tn' 'ty' 'uh' 'uo' 'wb' 'wh' 'wy' 'xx' 'z8' 'zt' 2016-05- 02 21:21:22.326724 27 'c0' 'd4' 'dw' 'ef' 'em' 'j2' 'kj' 'ql' 'rn' 'ta' 'uk' 'vv' 'wf' 'y9' 'zq' 2016- 05-02 22:21:22.326724 28 'by' 'c1' 'da' 'ec' 'ej' 'ew' 'g4' 'gq' 'gt' 'ir' 'jv' 'kl' 'kz' 'l5' 'nm' 'oi' 'on' 'pc' 'q2' 'qx' 'qz' 'rd' 'se' 'sq' 'ti' 'tk' 'to' 'ur' 'w8' 'wm' 'wr' 'y1' 'yn ' 'yp' 'zy' 2016-05-02 23:21:22.326724 29 '6d' '8t' 'bl' 'gu' 'iu' 'kd' 'kj' 'kq' 'nw' 'nx' 'o6' 'oa' 'qk' 'ql' 'rd' 'ri' 'uc' 'vi' 'wy' 'xq' 'z2' 2016-05-03 00:21:22.326724 30 'ao' 'ei' 'ep' 'fc' 'fm' 'gr' 'ha' 'he' 'i5' 'ia' 'if' 'kh' 'lv' 'ml' 'ms' 'n9' 'nh' 'nl' 'oe' 'of' 'ow' 'pb' 'pu' 'pw' 'q0' 'qr' 'qt' 'qu' 'qv' 'qw' 'ra' 'sv' 'ti ' 'u0' 'u4' 'ug' 'uq' 'vx' 'w1' 'wy' 'x1' 'xh' 'xz' 2016-05-03 01:21:22.326724 31 'ah' 'ai' 'b8' 'ci' 'd2' 'ea' 'ed' 'en' 'et' 'fj' 'fv' 'ht' 'iu' 'iv' 'iw' 'jb' 'jd' 'ky' 'mj' 'nt' 'q1' 'qb' 'qe' 'ql' 'qz' 'ru' 'sg' 'tl' 'tm' 'tn' 'tw' 'ty' 'u1 ' 'ud' 'us' 'wj' 'y1' 'zd' 'zj' 2016-05-03 02:21:22.326724 32 '5z' 'ad' 'al' 'ax' 'b4' 'bx' 'd7' 'da' 'dp' 'dz' 'e3' 'ef' 'en' 'es' 'et' 'ev' 'ex' 'f6' 'fj' 'fr' 'ft' 'fv' 'h9' 'hn' 'hx' 'i0' 'ii' 'it' 'jf' 'jk' 'jl' 'ka' 'kr ' 'l9' 'lf' 'm3' 'mm' 'nc' 'nd' 'nr' 'o8' 'oe' 'ok' 'om' 'pd' 'ph' 'pz' 'qd' 'qf' ' qo' 'qp' 'qw' 'qx' 'qy' 'r6' 'rc' 'rg' 'rw' 'rx' 's8' 'se' 't3' 'tb' 'tc' 'ti' 'tl' 'to' 'tw' 'ub' 'ue' 'uf' 'uy' 'vf' 'vh' 'vr' 'w0' 'w9' 'wd' 'wf' 'wh' 'wp' 'wu' 'x0 ' 'x8' 'y2' 'ye' 'yq' 'ys' 'yt' 'z6' 'zf' 'zp' 2016-05-03 03:21:22.326724 33 'az' 'bl' 'dl' 'ec' 'gg' 'jq' 'o0' 'oj' 'q8' 'qq' 'ta' 'un' 'wb' 'wo' 'xu' 2016- 05-03 04:21:22.326724 34 '9a' 'aa' 'bo' 'br' 'bv' 'bz' 'c1' 'c7' 'cz' 'db' 'dh' 'dj' 'e4' 'e8' 'eh' 'ew' 'gd' 'gg' 'gp' 'gu' 'gx' 'hc' 'ho' 'ht' 'hv' 'ia' 'ii' 'ij' 'ir' 'iw' 'j5' 'jk' 'jv ' 'la' 'lc' 'lp' 'lt' 'lw' 'na' 'nt' 'nv' 'nw' 'o8' 'o9' 'ou' 'oy' 'p0' 'pc' 'pq' ' py' 'q4' 'q8' 'qi' 'qk' 'qn' 'qr' 'qt' 'qw' 'r5' 'r8' 're' 'rj' 'rt' 'rv' 'ry' 'rz' 's8' 'sg' 'sv' 'ta' 'td' 'tl' 'tm' 'ul' 'up' 'ut' 'uz' 'vf' 'w1' 'wb' 'wc' 'wd' 'wf ' 'wi' 'wl' 'wu' 'x8' 'xg' 'xm' 'y1' 'yl' 'yr' 'ys' 'z8' 2016-05-03 05:21:22.326724 35 '80' 'ak' 'al' 'an' 'aq' 'as' 'at' 'bg' 'bn' 'bq' 'bx' 'd4' 'db' 'dg' 'dq' 'dv' 'ef' 'ej' 'en' 'eu' 'ex' 'f9' 'fu' 'g1' 'g2' 'g3' 'gj' 'gn' 'gs' 'gt' 'gx' 'h4' 'h8 ' 'hb' 'hn' 'hx' 'hy' 'i5' 'im' 'ji' 'jo' 'jy' 'k1' 'kb' 'kh' 'kp' 'kv' 'l4' 'lf' ' lt' 'ml' 'mv' 'na' 'ny' 'o2' 'oj' 'oq' 'or' 'os' 'pp' 'q3' 'q8' 'qc' 'qf' 'qp' 'qt' 'qv' 'rc' 'rg' 'rm' 's4' 'sa' 'sk' 'sp' 'su' 'sv' 'sy' 't5' 'te' 'tm' 'tn' 'to' 'tt
```

```
' 'tw' 'tx' 'tz' 'ue' 'ug' 'ul' 'un' 'uq' 'us' 'v3' 'wd' 'wr' 'wu' 'wy' 'x3' 'x8' ' xk' 'yf' 'yj' 'yk' 'yp' 'z0' 2016-05-03 06:21:22.326724 36 'cq' 'er' 'hy' 'ie' 'jg' 'ke' 'lw' 'mf' 'p0' 'pe' 'pv' 'qk' 'qt' 'qy' 'sh' 'th' 'ti' 'ue' 'w5' 'wl' 'y4' 'y5' 'yi' 'yy' 'za' 2016-05-03 07:21:22.326724 37 '3d' 'at' 'aw' 'bt' 'by' 'cg' 'dk' 'do' 'ec' 'eu' 'gv' 'is' 'k9' 'kb' 'kc' 'me' 'mm' 'o5' 'oe' 'pr' 'qa' 'qn' 'rc' 'rl' 'rn' 'rw' 'sc' 'sk' 'st' 't1' 't7' 'td' 'to ' 'ue' 'up' 'ur' 'uy' 've' 'wi' 'xf' 'xu' 'yf' 'z9' 'zo' 'zr' 2016-05-03 08:21:22.3 26724 38 '0z' 'ae' 'br' 'cr' 'dd' 'di' 'du' 'e7' 'ea' 'eb' 'ee' 'ej' 'em' 'eo' 'fo' 'fs' 'gc' 'gf' 'gj' 'hu' 'iv' 'kc' 'lb' 'nw' 'o9' 'ov' 'oz' 'pq' 'qq' 'ro' 'rr' 'rt' 'ru ' 'rw' 's4' 'te' 'tm' 'tq' 'um' 'v7' 'va' 'vi' 'vr' 'wb' 'wg' 'wo' 'wp' 'wr' 'ww' ' wy' 'xv' 'y1' 'y9' 'ya' 'ym' 'yt' 'yu' 'z5' 'zl' 'zs' 2016-05-03 09:21:22.326724 39 'a7' 'ab' 'ba' 'bv' 'e7' 'ea' 'eh' 'ep' 'er' 'es' 'f4' 'gq' 'hg' 'hi' 'hs' 'ip' 'iw' 'je' 'k0' 'kh' 'kn' 'ko' 'lo' 'ly' 'm6' 'n2' 'o1' 'oh' 'on' 'op' 'os' 'pi' 'q6 ' 'q9' 'qh' 'qj' 'qm' 'qn' 'qp' 'qs' 's7' 'sa' 'sb' 'sc' 'tn' 'tq' 'tt' 'u4' 'un' ' ux' 've' 'w1' 'wd' 'wf' 'wj' 'wl' 'wr' 'wu' 'wy' 'xf' 'xx' 'y3' 'y9' 'yk' 'zh' 'zn' 'zo' 'zr' 2016-05-03 10:21:22.326724 40 '19' 'a4' 'a7' 'ae' 'ar' 'as' 'bj' 'bp' 'bv' 'cp' 'd8' 'dp' 'e0' 'e8' 'ea' 'ee' 'ek' 'ep' 'es' 'et' 'ez' 'fp' 'gu' 'h2' 'h4' 'he' 'hp' 'ii' 'im' 'in' 'lc' 'lk' 'lu ' 'lv' 'ma' 'od' 'oe' 'p7' 'pm' 'q7' 'qa' 'qe' 'qf' 'qi' 'qr' 'qu' 'rc' 'rd' 're' ' rj' 'rl' 'ro' 'tj' 'tw' 'v4' 'vb' 'w7' 'wc' 'wg' 'wi' 'wm' 'wu' 'y4' 'yj' 'yv' 'z1' 'zt' 'zu' 2016-05-03 11:21:22.326724 41 'at' 'b7' 'be' 'c3' 'cc' 'cd' 'cj' 'e8' 'eb' 'ei' 'fd' 'g8' 'gh' 'go' 'gv' 'if' 'ih' 'j7' 'jy' 'kj' 'lh' 'mc' 'oe' 'og' 'oy' 'oz' 'pm' 'qd' 'qe' 'qo' 'rg' 'rq' 'rx ' 'se' 'su' 't3' 't6' 't9' 'u5' 'us' 'vw' 'w4' 'wb' 'wg' 'ws' 'xw' 'yu' 'yx' 'zj' 2 016-05-03 12:21:22.326724 42 '19' '1t' 'aa' 'ah' 'ak' 'an' 'aq' 'bx' 'cc' 'dd' 'ed' 'ee' 'ei' 'ej' 'en' 'er' 'es' 'eu' 'fj' 'fs' 'fy' 'gd' 'gs' 'hw' 'ie' 'ig' 'ix' 'jc' 'jj' 'jk' 'jq' 'kb' 'kv ' 'li' 'mr' 'no' 'nq' 'o9' 'oo' 'os' 'oy' 'p2' 'pd' 'ph' 'pn' 'pp' 'ql' 'qr' 'qy' ' r1' 'rb' 'rd' 'rn' 'ru' 's9' 'sf' 'tk' 'to' 'u1' 'u5' 'ub' 'ud' 'uf' 'vh' 'vx' 'w1' 'w8' 'wg' 'wn' 'wq' 'wu' 'wy' 'xc' 'xm' 'xw' 'y8' 'yk' 'yr' 'z3' 'zm' 2016-05-03 13 :21:22.326724 43 '7h' 'an' 'b6' 'cl' 'e1' 'e4' 'en' 'ey' 'ff' 'gn' 'h7' 'ht' 'i5' 'i9' 'ia' 'iw' 'jx' 'kl' 'ku' 'op' 'pe' 'pt' 'qb' 'ql' 'qp' 'qy' 'ri' 'se' 'si' 'ta' 'ti' 'tl' 'tp ' 'uo' 'vr' 'w4' 'wn' 'xi' 'xs' 'ym' 2016-05-03 14:21:22.326724 44 'bv' 'cv' 'dy' 'ec' 'ef' 'eg' 'eh' 'eu' 'ew' 'fc' 'fn' 'fs' 'g9' 'hj' 'hk' 'i3' 'iu' 'ja' 'k6' 'l1' 'la' 'nl' 'oh' 'oi' 'oy' 'pc' 'qe' 'ql' 'qq' 'qs' 'qu' 're' 'sf ' 'sq' 'tb' 'up' 'w1' 'w2' 'wg' 'wi' 'xd' 'xt' 'xv' 'yf' 'zn' 'zz' 2016-05-03 15:21 :22.326724 45 '2f' 'af' 'al' 'at' 'bc' 'bo' 'cd' 'd6' 'dk' 'dp' 'dy' 'ea' 'eu' 'ev' 'ey' 'fe' 'ft' 'gd' 'gi' 'ha' 'hm' 'hr' 'i6' 'im' 'is' 'iz' 'jb' 'jt' 'ju' 'li' 'm4' 'my' 'na ' 'nm' 'nu' 'oh' 'p4' 'pa' 'pn' 'po' 'qk' 'qz' 'r4' 're' 'rf' 'rs' 'sm' 'tb' 'ti' ' to' 'tw' 'u7' 'ut' 'vz' 'w3' 'w5' 'w9' 'wc' 'wj' 'wq' 'wr' 'x7' 'xg' 'xz' 'ye' 'yx' 'ze' 'zo' 2016-05-03 16:21:22.326724 46 '2l' '55' 'aq' 'aw' 'cm' 'dq' 'eb' 'fl' 'fo' 'fp' 'fy' 'gk' 'hy' 'ic' 'iu' 'jc' 'jl' 'lc' 'mb' 'nx' 'oe' 'oo' 'oz' 'p5' 'pa' 'pf' 'qr' 'rj' 'sc' 'sz' 'td' 'tz' 'u1 ' 'vq' 'wu' 'xb' 'xx' 'y0' 'za' 'zc' 2016-05-03 17:21:22.326724 47 'bt' 'dy' 'gy' 'hg' 'i7' 'it' 'jv' 'lh' 'ox' 'qo' 'ri' 's3' 'ss' 'u1' 'uq' 'wr' 2016-05-03 18:21:22.326724 48 '3v' 'ab' 'at' 'bn' 'bz' 'cx' 'eh' 'gd' 'hd' 'hr' 'i9' 'j8' 'jg' 'jx' 'lf' 'ng' 'oj' 'ov' 'oz' 'pn' 'ps' 'qq' 'qr' 'ro' 'rt' 'u9' 'up' 'uz' 'yl' 'yw' 'zi' 2016-05- 03 19:21:22.326724 49 '5y' 'af' 'av' 'az' 'cj' 'cp' 'cq' 'dk' 'e6' 'e7' 'ea' 'ec' 'ee' 'ei' 'ek' 'em' 'ga' 'gk' 'gw' 'hc' 'id' 'ie' 'kp' 'kv' 'lw' 'm0' 'mf' 'mn' 'mw' 'ny' 'ob' 'ol' 'p9
```

```
' 'ph' 'pk' 'pp' 'pw' 'q0' 'qg' 'qi' 'ql' 'qv' 'qx' 'r3' 'rg' 'ry' 'se' 'sh' 'sq' ' sz' 't1' 'tu' 'u2' 'uh' 'uj' 'uk' 'ut' 'w2' 'wb' 'ww' 'wx' 'yf' 'yo' 'zr' 2016-05-0 3 20:21:22.326724 50 '18' 'a6' 'af' 'ax' 'du' 'dy' 'e7' 'ei' 'ej' 'es' 'eu' 'fj' 'gt' 'hn' 'hu' 'ky' 'le' 'lo' 'm8' 'nb' 'of' 'oj' 'ok' 'op' 'oz' 'pw' 'q7' 'qi' 'qu' 'r4' 'rp' 's7' 'sk ' 'tb' 'tf' 'tp' 'ua' 'um' 'up' 'ur' 'uz' 'w4' 'wc' 'wn' 'wv' 'wx' 'wy' 'yc' 'yq' ' yx' 2016-05-03 21:21:22.326724 51 'ag' 'ay' 'b6' 'bk' 'c6' 'cp' 'da' 'ea' 'eh' 'es' 'f1' 'fj' 'fv' 'gb' 'gn' 'ic' 'id' 'in' 'iq' 'iw' 'kx' 'ly' 'n7' 'o5' 'oc' 'og' 'op' 'os' 'pa' 'pr' 'q4' 'q6' 'qf ' 'qg' 'qh' 'qp' 'qq' 'qu' 'qw' 'qy' 'qz' 'rj' 'rm' 'ro' 's1' 'w2' 'we' 'wl' 'wn' ' wp' 'yj' 'yp' 'yx' 2016-05-03 22:21:22.326724 52 'cr' 'd3' 'e5' 'ei' 'fb' 'gd' 'gx' 'hm' 'it' 'jp' 'ku' 'lf' 'lh' 'lp' 'ma' 'md' 'nt' 'o9' 'ot' 'pk' 'pm' 'ps' 'qc' 'qi' 'qp' 'qt' 'ra' 'rk' 'rq' 'rt' 'tb' 'tc' 'tg ' 'to' 'u8' 'vg' 'vj' 'vt' 'w0' 'wr' 'wx' 'yd' 'zx' 2016-05-03 23:21:22.326724 53 '4z' 'a8' 'ds' 'dv' 'dx' 'eq' 'f1' 'fs' 'gs' 'h9' 'hm' 'hp' 'hu' 'hz' 'i6' 'ip' 'is' 'j4' 'jf' 'k3' 'ku' 'lc' 'le' 'lj' 'nb' 'o6' 'ob' 'of' 'p6' 'pj' 'pm' 'ps' 'qc ' 'qf' 'qh' 'ql' 'qr' 'qu' 'qx' 'r3' 'rf' 'ri' 's1' 's4' 'sr' 'st' 'sw' 'tb' 'tc' ' tg' 'tr' 'tz' 'ug' 'uq' 'uu' 'uv' 'uw' 'uz' 'vl' 'w2' 'w4' 'wq' 'wx' 'xe' 'xv' 'xx' 'y6' 'yg' 'yn' 'yp' 'yr' 2016-05-04 00:21:22.326724 54 '70' 'ai' 'bj' 'bm' 'cj' 'ct' 'eb' 'ef' 'ek' 'es' 'fg' 'gh' 'gu' 'hg' 'ia' 'iu' 'iw' 'jt' 'ko' 'kq' 'mb' 'n1' 'o1' 'ox' 'pa' 'pr' 'q4' 'qd' 'qo' 'qr' 'qt' 'qw' 'qz ' 'r3' 'r5' 'rg' 'ri' 'rj' 'rn' 'rp' 's7' 'sn' 't9' 'tq' 'tx' 'ty' 'uj' 'v0' 'vt' ' vz' 'w1' 'ww' 'xb' 'z6' 'zi' 2016-05-04 01:21:22.326724 55 'aa' 'al' 'e9' 'hm' 'ir' 'kc' 'l0' 'pi' 'po' 'qa' 'qk' 'r0' 'rd' 'rz' 'se' 'sr' 'vp' 'w6' 'w8' 'yd' 'yk' 2016-05-04 02:21:22.326724 56 '27' '3p' '6r' 'a8' 'an' 'ap' 'au' 'ay' 'bi' 'c6' 'cy' 'dh' 'ds' 'eg' 'eh' 'ej' 'es' 'eu' 'fm' 'fp' 'fq' 'fx' 'g2' 'gg' 'gv' 'hz' 'ij' 'il' 'iq' 'iw' 'j8' 'j9' 'k3 ' 'kr' 'lq' 'm7' 'm9' 'mj' 'n0' 'n6' 'nr' 'nx' 'ox' 'pq' 'qc' 'qd' 'qe' 'qg' 'qh' ' qj' 'qk' 'qm' 'qn' 'qr' 'qu' 'qv' 'qw' 'qx' 're' 'rg' 'rr' 'rz' 's1' 'sj' 'sl' 'sy' 't4' 't7' 'tb' 'tr' 'uc' 'un' 'uq' 'ut' 'vf' 'w7' 'w9' 'wg' 'wh' 'wp' 'wq' 'ws' 'wx ' 'x8' 'xp' 'xy' 'y0' 'y1' 'ya' 'yu' 'yz' 'z2' 'z5' 'zz' 2016-05-04 03:21:22.326724 57 'a7' 'a9' 'al' 'aq' 'ar' 'as' 'b2' 'cj' 'cl' 'co' 'cu' 'cv' 'dc' 'e3' 'e5' 'e7' 'ea' 'ee' 'eh' 'en' 'es' 'ev' 'ez' 'fl' 'fp' 'gm' 'hm' 'it' 'iu' 'iv' 'j8' 'jd' 'jo ' 'kn' 'ko' 'ky' 'ln' 'mr' 'nc' 'o2' 'ok' 'ot' 'pc' 'pe' 'pz' 'q2' 'qe' 'qi' 'qq' ' qr' 'qs' 'r8' 'rm' 'rn' 'ro' 'rx' 'sz' 'te' 'tn' 'tq' 'tx' 'u1' 'ub' 'ul' 'up' 'uq' 'wf' 'wh' 'wk' 'wl' 'wo' 'wq' 'wt' 'wu' 'wv' 'xh' 'xz' 'y5' 'y9' 'yv' 'yx' 'yz' 'zj ' 2016-05-04 04:21:22.326724 58 'am' 'hw' 'jd' 'na' 'oe' 'pw' 'ql' 'qr' 's9' 'sk' 'u7' 'wa' 'wg' 'wu' 'x6' 'xr' 'yf' 2016-05-04 05:21:22.326724 59 '2n' 'aa' 'ab' 'ae' 'ah' 'aj' 'as' 'av' 'ax' 'bc' 'be' 'bi' 'by' 'cg' 'ck' 'cm' 'cx' 'dq' 'dr' 'e5' 'ed' 'ef' 'ei' 'em' 'eu' 'fd' 'fq' 'fu' 'gd' 'gl' 'gs' 'he' 'ia ' 'iz' 'jc' 'je' 'jt' 'k7' 'km' 'ko' 'l4' 'lh' 'mk' 'nl' 'ny' 'oa' 'oh' 'op' 'p1' ' pj' 'pm' 'ps' 'q1' 'q7' 'qc' 'qg' 'qj' 'qo' 'qr' 'qt' 'qu' 'qv' 'qw' 'rf' 'ri' 'rl' 'rw' 'sf' 'su' 't4' 'tc' 'tn' 'to' 'tq' 'tr' 'tt' 'tv' 'tz' 'u0' 'u6' 'ub' 'ug' 'up ' 'uv' 'ux' 'uy' 'vv' 'w2' 'wx' 'xi' 'xu' 'xw' 'yj' 'yt' 'yw' 'z3' 'z7' 'zb' 2016-0 5-04 06:21:22.326724 60 'bq' 'cc' 'cg' 'dc' 'fu' 'ho' 'ja' 'jt' 'km' 'lk' 'ln' 'o2' 'ob' 'ou' 'pd' 'ph' 'pn' 'pt' 'pz' 'q5' 'qa' 'ql' 'qq' 'qv' 'rk' 'rm' 'ry' 'sq' 'su' 'sx' 'uc' 'un' 'uo ' 'ur' 'uy' 'w9' 'wj' 'wl' 'wm' 'yk' 'ym' 2016-05-04 07:21:22.326724 61 'bl' 'bn' 'cy' 'ea' 'ed' 'ef' 'ei' 'em' 'er' 'es' 'fp' 'gb' 'hi' 'hp' 'if' 'io' 'ir' 'kw' 'lg' 'lo' 'ls' 'n8' 'nj' 'np' 'oa' 'of' 'oi' 'p6' 'pw' 'q3' 'q4' 'q8' 'qf ' 'qh' 'qo' 'qw' 'rg' 'rt' 'sy' 't3' 'u8' 'ug' 'uo' 'uv' 'w6' 'we' 'wg' 'wl' 'wy' ' x9' 'yy' 'yz' 2016-05-04 08:21:22.326724 62 'aa' 'af' 'ah' 'am' 'as' 'cd' 'ch' 'dd' 'dg' 'dr' 'e2' 'eb' 'eq' 'er' 'fb' 'fj' 'fk''fn''f''gk''gs''h8''hg''hj''ia''ij''in''j''l9''lj''l''nk''nt
```

```
'fk' 'fn' 'fx' 'gk' 'gs' 'h8' 'hg' 'hj' 'ia' 'ij' 'in' 'jw' 'l9' 'lj' 'lw' 'nk' 'nt ' 'o1' 'ob' 'oo' 'p5' 'pd' 'pk' 'qq' 'sb' 'sd' 'sg' 'u4' 'wl' 'wq' 'wr' 'wu' 'xc' ' xj' 'xt' 'yq' 'zl' 2016-05-04 09:21:22.326724 63 '10' '2p' '6r' 'a2' 'bb' 'c9' 'dq' 'dy' 'ec' 'eh' 'ej' 'ek' 'es' 'fl' 'g1' 'g9' 'gd' 'h1' 'h2' 'hj' 'hn' 'hw' 'ip' 'iz' 'jg' 'jl' 'l5' 'le' 'lk' 'me' 'mi' 'o0' 'o6 ' 'oa' 'oe' 'ox' 'pd' 'pm' 'pr' 'py' 'q1' 'qo' 'qq' 'qz' 'r3' 'rs' 'rw' 's7' 'sl' ' sw' 't2' 't4' 'td' 'tj' 'u3' 'ud' 'ur' 'uw' 'vy' 'wi' 'wj' 'wl' 'wq' 'ys' 'yu' 'z7' 'zp' 2016-05-04 10:21:22.326724 64 'aj' 'cl' 'cy' 'ee' 'i3' 'ir' 'nx' 'oz' 'qm' 'qw' 'r2' 't2' 'u0' 'ub' 'ur' 'wj' 2016-05-04 11:21:22.326724 65 '3f' '93' 'am' 'an' 'at' 'bj' 'bm' 'bw' 'c6' 'eb' 'ef' 'em' 'eq' 'es' 'g9' 'hc' 'hl' 'hm' 'kg' 'kt' 'mg' 'nq' 'op' 'ox' 'pc' 'py' 'qd' 'qn' 'qz' 'rb' 'rw' 's6' 'se ' 'sr' 'sy' 'ts' 'u4' 'ud' 'un' 'w3' 'w8' 'wb' 'wf' 'wg' 'wy' 'x1' 'xl' 'xy' 'yk' ' yo' 'zp' 2016-05-04 12:21:22.326724 66 'at' 'ec' 'hs' 'ix' 'ks' 'lq' 'ls' 'pk' 'qs' 'qy' 'rc' 'ut' 'xv' 'yo' 'ys' 2016- 05-04 13:21:22.326724 67 'ac' 'al' 'b3' 'bg' 'ci' 'cn' 'ea' 'f4' 'ih' 'ix' 'kt' 'p8' 'pk' 'qd' 'qe' 'qi' 'rb' 'rc' 'ru' 'te' 'th' 'tl' 'tn' 'vb' 'wb' 'ws' 'ww' 'xk' 'xo' 'yb' 'zf' 2016-05- 04 14:21:22.326724 68 'a5' 'ao' 'av' 'b0' 'bh' 'bk' 'cj' 'd0' 'do' 'ds' 'e1' 'ee' 'ep' 'fa' 'fh' 'fv' 'hc' 'hh' 'hq' 'i1' 'if' 'iv' 'ix' 'iy' 'jq' 'jw' 'jz' 'ko' 'll' 'lr' 'lx' 'ns' 'nz ' 'og' 'or' 'os' 'oz' 'p0' 'p8' 'pr' 'pv' 'q6' 'q9' 'qb' 'qd' 'qe' 'qh' 'qi' 'qq' ' qt' 'qu' 'qy' 'rd' 'ri' 'rq' 'rr' 'ry' 'sf' 'sg' 'sh' 'si' 'sw' 'sx' 'tc' 'tq' 'u3' 'uh' 'ul' 'us' 'wg' 'wn' 'wx' 'x3' 'xb' 'ya' 'yg' 'yn' 'yo' 'yp' 'yr' 'yw' 2016-05- 04 15:21:22.326724 69 'al' 'ar' 'av' 'bg' 'bh' 'bz' 'e9' 'ed' 'ee' 'ef' 'eh' 'es' 'fl' 'fz' 'gl' 'h1' 'he' 'hf' 'hv' 'hw' 'i1' 'jg' 'kj' 'kn' 'kz' 'lr' 'pp' 'q1' 'qa' 'qf' 'qt' 'qz' 'rg ' 'rj' 's5' 'sv' 'sx' 't4' 'th' 'tn' 'ur' 'wz' 'xp' 'yg' 'ym' 'yr' 'ze' 2016-05-04 16:21:22.326724 70 '26' '4v' 'a1' 'ac' 'af' 'ah' 'au' 'cn' 'd3' 'dn' 'e4' 'ec' 'eg' 'ep' 'er' 'fa' 'fb' 'g6' 'gr' 'h3' 'hb' 'hf' 'hj' 'iu' 'iv' 'j1' 'jk' 'jy' 'k2' 'k8' 'kd' 'lc' 'lf ' 'mb' 'nn' 'ot' 'p5' 'pb' 'pl' 'pw' 'py' 'q4' 'q9' 'qf' 'r6' 'ra' 'rl' 'rr' 'ru' ' rz' 'ta' 'te' 'ti' 'tp' 'u1' 'uy' 'w6' 'wb' 'wc' 'wd' 'wh' 'wv' 'wy' 'xo' 'xu' 'yd' 'yh' 'yo' 'yt' 2016-05-04 17:21:22.326724 71 '8w' 'ao' 'aw' 'bk' 'by' 'c5' 'ch' 'cw' 'd0' 'dh' 'e2' 'eq' 'ev' 'ha' 'hk' 'ii' 'ir' 'iv' 'j8' 'ki' 'kp' 'lm' 'lx' 'nh' 'ns' 'nt' 'o3' 'on' 'ov' 'ow' 'ox' 'pl' 'q3 ' 'qc' 'qd' 'qe' 'qh' 'qm' 'qo' 'qr' 'qs' 'qt' 'qx' 'r2' 'r8' 'rc' 'rd' 'rh' 'ri' ' rk' 'rq' 'rt' 's3' 'sm' 'sq' 'sz' 't1' 't6' 'tx' 'u2' 'ue' 'up' 'uq' 'ut' 'ux' 'vg' 'vp' 'w3' 'wb' 'wc' 'wd' 'wr' 'xf' 'xp' 'y1' 'ya' 'yf' 'yg' 'yi' 'yn' 'yq' 'zn' 201 6-05-04 18:21:22.326724 72 '1l' 'b5' 'dq' 'fw' 'hz' 'in' 'ml' 'nb' 'nu' 'o2' 'or' 'q7' 'qb' 'qh' 'qt' 'rv' 'so' 'tp' 'tr' 'u0' 'v6' 'wl' 'xb' 2016-05-04 19:21:22.326724 73 'ah' 'aw' 'e5' 'en' 'ew' 'fi' 'fm' 'gq' 'gt' 'hy' 'ib' 'ie' 'ir' 'j9' 'jr' 'js' 'ny' 'ob' 'or' 'ot' 'oy' 'pt' 'qi' 'rd' 'ri' 'rl' 'ro' 'rt' 'ss' 'tb' 'tg' 'th' 'vy ' 'wq' 'wz' 'xt' 'y6' 'y8' 'zf' 'zh' 2016-05-04 20:21:22.326724 74 '3d' 'ad' 'dr' 'ee' 'ez' 'f4' 'fd' 'fg' 'fu' 'g9' 'gk' 'h9' 'hl' 'iz' 'jd' 'nb' 'o0' 'oo' 'oy' 'qj' 'qt' 'rp' 'ru' 'sv' 'tl' 'tv' 'wf' 'wp' 'wy' 2016-05-04 21:21:2 2.326724 75 '48' 'ae' 'au' 'az' 'b2' 'di' 'ep' 'eq' 'ev' 'f7' 'fw' 'gh' 'gj' 'gn' 'hz' 'i5' 'iy' 'jf' 'kg' 'kj' 'kk' 'nc' 'nm' 'o4' 'oc' 'oe' 'of' 'oh' 'ol' 'ov' 'oz' 'pt' 'pv ' 'q5' 'q7' 'qb' 'qe' 'qf' 'rh' 'ry' 'se' 'so' 'tv' 'ua' 'vd' 'wb' 'wg' 'wi' 'wp' ' xf' 'xo' 'yl' 'yr' 'yy' 'z0' 2016-05-04 22:21:22.326724 76 '5c' 'ag' 'ak' 'ao' 'ap' 'at' 'bo' 'br' 'bs' 'bw' 'cv' 'e9' 'et' 'ex' 'ez' 'fj' 'fu' 'fz' 'gm' 'gq' 'gu' 'h8' 'hl' 'i7' 'ic' 'ik' 'il' 'is' 'j1' 'jc' 'k2' 'k3' 'k6 ''k7''kf''km''kr''lj''mb''md''nf''om''ow''p4''pk''pw''q2''qe''qh''
```

```
 k7 kf km kr lj mb md nf om ow p4 pk pw q2 qe qh
qn' 'qq' 'qu' 'qz' 'r0' 'ra' 'rp' 'ru' 'rw' 'rz' 'sv' 'ta' 'ti' 'tq' 'ua' 'up' 'us' 'ut' 'uz' 'vd' 'wl' 'wq' 'xg' 'xk' 'y0' 'yd' 'yw' 'zd' 'zq' 2016-05-04 23:21:22.326 77 '20' 'ag' 'az' 'b9' 'bg' 'bh' 'c2' 'dd' 'di' 'do' 'dw' 'e1' 'e3' 'e8' 'eb' 'ev' 'fc' 'fj' 'fu' 'fw' 'fx' 'gb' 'gf' 'hu' 'hw' 'hz' 'ih' 'ik' 'iq' 'jc' 'jq' 'ka' 'kf ' 'kh' 'kw' 'ky' 'ly' 'lz' 'mc' 'n8' 'o3' 'o7' 'oa' 'os' 'ou' 'pf' 'q5' 'q6' 'qg' ' ql' 'qo' 'qy' 'r2' 'rf' 'rp' 'ru' 'ry' 's1' 's5' 'se' 'si' 'sn' 'su' 'ta' 'tn' 'tu' 'tv' 'tw' 'u9' 'ua' 'uh' 'uu' 'vo' 'w8' 'wa' 'wc' 'we' 'wi' 'wu' 'ww' 'wy' 'x3' 'xl ' 'yb' 'yg' 'yk' 'yv' 2016-05-05 00:21:22.326724 78 'ef' 'ej' 'fn' 'ho' 'ia' 'il' 'iq' 'mj' 'nr' 'p5' 'rm' 'sd' 'ux' 'vi' 'wq' 'y6' 2016-05-05 01:21:22.326724 79 'ab' 'av' 'c9' 'cs' 'cx' 'dy' 'e4' 'eb' 'ej' 'er' 'ez' 'f0' 'f2' 'ft' 'gk' 'h5' 'i5' 'ic' 'ig' 'io' 'ki' 'kz' 'lj' 'mm' 'of' 'og' 'ov' 'oz' 'p4' 'pl' 'qh' 'qx' 'rw ' 's1' 'sf' 'tw' 'uc' 'ui' 'uo' 'uw' 'x4' 'xk' 'ze' 2016-05-05 02:21:22.326724 80 'ca' 'do' 'h5' 'i9' 'io' 'jk' 'jl' 'kn' 'qq' 'tm' 'ul' 'w9' 'wb' 'wp' 'wt' 'wx' 'y3' 'zd' 2016-05-05 03:21:22.326724 81 'a2' 'cs' 'ee' 'em' 'gk' 'hv' 'iy' 'kq' 'nc' 'pb' 'q5' 'qy' 'rq' 'rr' 'ts' 'uq' 'vt' 'w0' 'y6' 'yz' 2016-05-05 04:21:22.326724 82 'av' 'ej' 'el' 'ep' 'fp' 'hh' 'hz' 'l9' 'mr' 'q3' 'qn' 'qq' 'qy' 'rh' 'tw' 'vt' 'vu' 'w5' 'wg' 'wk' 'wo' 'x5' 'y9' 'yk' 'zm' 2016-05-05 05:21:22.326724 83 'az' 'cx' 'dm' 'do' 'dq' 'e2' 'e5' 'e8' 'eb' 'fh' 'fj' 'fq' 'gj' 'gl' 'hq' 'im' 'iq' 'iz' 'jn' 'ku' 'l1' 'mz' 'nt' 'o6' 'q1' 'qn' 'qo' 'qz' 'r4' 'rh' 'rn' 'rw' 'sn ' 'sv' 't7' 'ud' 'ue' 'ur' 'uv' 'w9' 'wh' 'wk' 'wy' 'xq' 'yh' 'zs' 'zw' 2016-05-05 06:21:22.326724 84 '5o' 'ad' 'aw' 'az' 'bi' 'bo' 'd1' 'db' 'di' 'do' 'e7' 'eb' 'ei' 'em' 'ep' 'eq' 'eu' 'fo' 'gg' 'gw' 'i0' 'ig' 'ih' 'iu' 'j3' 'j4' 'jo' 'js' 'kq' 'lc' 'lo' 'lu' 'm9 ' 'mi' 'mk' 'mt' 'n4' 'ni' 'o7' 'od' 'ot' 'pc' 'pg' 'pp' 'qc' 'qr' 'qw' 'rd' 'rx' ' se' 'sq' 'sy' 't5' 'ts' 'ub' 'vz' 'wb' 'wl' 'wr' 'wt' 'xe' 'xt' 'yg' 'yr' 'zw' 2016 -05-05 07:21:22.326724 85 'bt' 'c9' 'db' 'dy' 'ee' 'ej' 'eo' 'et' 'fr' 'gm' 'hz' 'ic' 'ik' 'is' 'jk' 'ls' 'lt' 'oj' 'or' 'ox' 'p8' 'pl' 'pz' 'q1' 'qq' 'qt' 'rw' 's7' 't4' 't8' 'to' 'tp' 'u7 ' 'ub' 'vx' 'w4' 'ws' 'wt' 'wv' 'x8' 'xs' 'xt' 'yg' 'yo' 2016-05-05 08:21:22.326724 86 '4d' '9f' 'aa' 'ad' 'av' 'b1' 'bb' 'bd' 'bk' 'd2' 'd6' 'd7' 'de' 'do' 'ds' 'dx' 'e4' 'eh' 'en' 'ep' 'ew' 'fd' 'fg' 'fo' 'fp' 'ga' 'gw' 'gz' 'h2' 'h4' 'hc' 'hk' 'ic ' 'ih' 'io' 'iv' 'iy' 'jj' 'jt' 'jz' 'kb' 'ke' 'kl' 'lh' 'lm' 'nc' 'ni' 'nl' 'o9' ' oi' 'oo' 'pd' 'pj' 'po' 'pr' 'qa' 'qf' 'qi' 'qm' 'qn' 'qp' 'qt' 'qu' 'rb' 're' 'rf' 'rn' 'rz' 'sz' 't0' 'tg' 'ti' 'ut' 'v9' 'vg' 'wb' 'wc' 'wf' 'wx' 'x0' 'xb' 'xv' 'y6 ' 'yb' 'yg' 'yh' 'yk' 'ym' 'yn' 'yw' 'yx' 'yz' 'z8' 'zp' 'zs' 'zw' 2016-05-05 09:21 :22.326724 87 '6g' 'ar' 'ce' 'cn' 'ds' 'dt' 'e9' 'eh' 'el' 'ew' 'gt' 'gw' 'gx' 'hb' 'ho' 'i8' 'j8' 'jp' 'jr' 'kb' 'la' 'lr' 'mg' 'mi' 'ml' 'nd' 'ng' 'oj' 'op' 'pb' 'pd' 'pn' 'py ' 'qc' 'qe' 'qk' 'qr' 'qt' 'qv' 'qz' 'sm' 'tc' 'tg' 'ti' 'tp' 'ty' 'u8' 'uq' 'uw' ' uy' 've' 'w0' 'wb' 'wd' 'wp' 'x4' 'xm' 'ym' 'z2' 'zh' 'zz' 2016-05-05 10:21:22.326724 88 'af' 'as' 'b2' 'bl' 'bz' 'ca' 'cd' 'co' 'de' 'dp' 'e4' 'ed' 'en' 'eo' 'eu' 'ft' 'g0' 'gj' 'ha' 'hh' 'hn' 'hy' 'ij' 'jb' 'jj' 'jn' 'l7' 'll' 'lp' 'oh' 'ot' 'pb' 'ph ' 'pi' 'pn' 'qc' 'qx' 'r5' 'rb' 'ri' 'sb' 'sd' 'sn' 'sv' 'sw' 't7' 'tb' 'ti' 'ty' ' u7' 'un' 'uo' 'wb' 'we' 'wf' 'wh' 'wo' 'wp' 'yb' 'yc' 'ys' 2016-05-05 11:21:22.326724 89 '5s' 'aa' 'ar' 'bu' 'c2' 'cw' 'd2' 'ej' 'g8' 'gy' 'ij' 'iv' 'k0' 'l1' 'lb' 'm1' 'od' 'pm' 'q1' 'q4' 'q5' 'qd' 'rn' 'ry' 'sj' 'sm' 'ta' 'th' 'u8' 'vf' 'wr' 'xm' 201 6-05-05 12:21:22.326724 90 'am' 'db' 'dj' 'dn' 'ec' 'eo' 'ev' 'ex' 'fn' 'fw' 'fz' 'gi' 'gn' 'gq' 'ha' 'ho' 'in' 'is' 'ja' 'jj' 'jk' 'js' 'kv' 'lc' 'lz' 'mj' 'o2' 'oa' 'of' 'oi' 'pe' 'pn' 'ps
```

`j` `jj` `j` `j` `j` `p` `p` `p`

```
' 'pv' 'py' 'q3' 'qa' 'qb' 'qi' 'qn' 'qo' 'qq' 'qr' 'qv' 'rk' 'rl' 't8' 'tk' 'tv' ' tw' 'ug' 'uk' 'ux' 'uz' 'v7' 'vr' 'wd' 'wf' 'wk' 'wv' 'ya' 'yq' 'yu' 'zp' 'zx' 2016 -05-05 13:21:22.326724 91 'a3' 'ac' 'af' 'ar' 'b4' 'cu' 'd6' 'dx' 'dz' 'eb' 'ej' 'ek' 'eo' 'es' 'eu' 'ff' 'gj' 'go' 'h6' 'ho' 'hx' 'i6' 'ih' 'ir' 'iy' 'jd' 'jg' 'jh' 'k5' 'n0' 'nn' 'oe' 'og ' 'pj' 'pk' 'pq' 'px' 'q5' 'qc' 'qf' 'qg' 'qi' 'qm' 'qx' 'rb' 'rd' 're' 'rx' 'sn' ' sq' 'tp' 'uh' 'ul' 'um' 'uo' 'up' 'uq' 'uz' 'vt' 'wb' 'wj' 'wp' 'ws' 'wv' 'xk' 'xo' 'yv' 'yw' 'yx' 2016-05-05 14:21:22.326724 92 '1l' '24' '2o' 'ad' 'am' 'ao' 'bf' 'bl' 'ca' 'ce' 'cn' 'cw' 'cy' 'd4' 'dm' 'e9' 'ed' 'ee' 'ei' 'ep' 'f0' 'fk' 'fu' 'fw' 'g3' 'g4' 'gm' 'gn' 'gu' 'ha' 'hh' 'id' 'iq ' 'it' 'iw' 'ix' 'iy' 'j4' 'j6' 'jo' 'jp' 'js' 'jv' 'k6' 'kb' 'ke' 'kh' 'l9' 'lh' ' lr' 'mr' 'n7' 'n8' 'nd' 'o6' 'of' 'oi' 'op' 'ox' 'p6' 'q2' 'qb' 'qd' 'qi' 'qk' 'qn' 'qq' 'qt' 'qy' 'r2' 're' 'rf' 'rk' 's4' 'sb' 'se' 'sh' 't4' 'tb' 'tn' 'tq' 'ty' 'u4 ' 'u5' 'ub' 'ue' 'uf' 'uk' 'uo' 'vc' 'vs' 'vu' 'w7' 'wd' 'wh' 'xm' 'yk' 'yv' 'zl' ' zz' 2016-05-05 15:21:22.326724 93 '1h' '4r' 'a9' 'ag' 'ah' 'ak' 'as' 'at' 'b2' 'be' 'cs' 'd6' 'd7' 'da' 'dg' 'dl' 'dr' 'dy' 'dz' 'e8' 'e9' 'eg' 'eh' 'ek' 'eq' 'es' 'f3' 'f9' 'fs' 'gh' 'go' 'gq' 'gz ' 'ha' 'hc' 'hi' 'hp' 'if' 'ig' 'im' 'iv' 'jd' 'jt' 'kp' 'kt' 'l6' 'le' 'lg' 'lo' ' mz' 'ns' 'oc' 'ok' 'p6' 'pa' 'pt' 'pv' 'px' 'q1' 'q5' 'qa' 'qe' 'qg' 'qh' 'qi' 'qn' 'qp' 'qs' 'qu' 'qv' 'qy' 'rh' 'rl' 'rp' 'rv' 'rx' 'rz' 's8' 'sc' 'sr' 'su' 't6' 'tb ' 'tq' 'tw' 'u9' 'vr' 'w7' 'wb' 'wj' 'wq' 'ww' 'xr' 'xx' 'yb' 'yl' 'yn' 'yr' 'zw' 2 016-05-05 16:21:22.326724 94 '1g' '3e' 'a5' 'ae' 'ar' 'bt' 'cb' 'ck' 'co' 'd5' 'dh' 'dm' 'dr' 'dt' 'e0' 'e9' 'eh' 'el' 'em' 'f2' 'f3' 'fb' 'ff' 'fg' 'gu' 'hb' 'he' 'hr' 'hx' 'i7' 'ib' 'if' 'ig ' 'io' 'iu' 'jc' 'jo' 'jv' 'kh' 'kx' 'lb' 'lh' 'lw' 'lx' 'ly' 'mp' 'oa' 'oc' 'oz' ' pa' 'q9' 'qi' 'qp' 'qq' 'qw' 'r3' 'rb' 'rd' 're' 'rn' 'ry' 'rz' 's5' 'su' 'sz' 'td' 'tf' 'tt' 'u9' 'uh' 'um' 'un' 'va' 'vh' 'vt' 'w7' 'wb' 'wc' 'wg' 'wh' 'wx' 'xd' 'xz ' 'y8' 'yf' 'yg' 'yh' 'ym' 'zy' 2016-05-05 17:21:22.326724 95 '5f' '5i' 'ak' 'cg' 'dh' 'di' 'dk' 'eq' 'f6' 'g1' 'g8' 'ie' 'md' 'o0' 'oj' 'oq' 'pt' 'q7' 'qb' 'qd' 'qe' 'qo' 'ro' 'ru' 'rv' 'rx' 'sp' 'sr' 'tf' 'tp' 'uh' 'ul' 'vs ' 'xn' 'xw' 'y2' 'yh' 'yk' 'zg' 'zm' 'zq' 2016-05-05 18:21:22.326724 96 '82' 'a2' 'ad' 'dp' 'el' 'ep' 'fk' 'gd' 'hj' 'ij' 'lc' 'lm' 'lv' 'ml' 'n2' 'n6' 'o1' 'oi' 'on' 'oo' 'ow' 'pb' 'pe' 'pq' 'q6' 'qi' 'qo' 'qp' 'qw' 'rs' 'rv' 's6' 'sa ' 'sk' 't8' 'tl' 'tt' 'tx' 'ub' 'ue' 'uf' 'uj' 'va' 'wl' 'xv' 'y1' 'ye' 'ym' 'yw' ' zm' 2016-05-05 19:21:22.326724 97 '2s' 'a5' 'aw' 'b5' 'b7' 'ce' 'cq' 'dc' 'dp' 'eb' 'eq' 'ez' 'ff' 'gg' 'gy' 'iw' 'jd' 'jl' 'kw' 'ky' 'mt' 'ng' 'o9' 'od' 'oe' 'po' 'pp' 'qa' 'qe' 'qk' 'ql' 'qp' 'r4 ' 'r9' 'rb' 'si' 'sl' 'sn' 'sq' 'tg' 'ti' 'tx' 'uh' 'ws' 'xf' 'yv' 'z1' 'zm' 2016-0 5-05 20:21:22.326724 98 'cd' 'dl' 'e6' 'en' 'eu' 'gg' 'je' 'kp' 'lv' 'pv' 'q0' 'q3' 'qc' 'qd' 'qo' 'qs' 'qz' 'rw' 'se' 'tx' 'uh' 'uj' 'ul' 'wo' 'ye' 'yi' 'zx' 2016-05-05 21:21:22.326724 99 'ak' 'at' 'cs' 'di' 'dt' 'ef' 'eq' 'f1' 'f8' 'fb' 'fh' 'fv' 'g4' 'hs' 'j2' 'jo' 'kq' 'lf' 'lq' 'no' 'oa' 'ot' 'q0' 'qh' 'qs' 'qw' 'se' 'so' 'sx' 't3' 'ul' 'un' 'uu ' 'wn' 'ws' 'wx' 'y0' 'y3' 'yf' 'zb' 'zc' 2016-05-05 22:21:22.326724 100 '1k' '1p' 'a6' 'ah' 'ap' 'ay' 'az' 'bi' 'bj' 'cv' 'd1' 'd2' 'd5' 'db' 'dm' 'dn' 'e7' 'eg' 'eh' 'el' 'en' 'eo' 'er' 'f4' 'fy' 'gf' 'gp' 'hd' 'hj' 'hp' 'i2' 'i7' 'ij ' 'ik' 'jq' 'jy' 'kg' 'kh' 'kw' 'lr' 'ls' 'n5' 'ne' 'o7' 'od' 'oi' 'oo' 'os' 'oy' ' pd' 'ph' 'pm' 'pw' 'px' 'qa' 'qb' 'qc' 'qk' 'ql' 'qm' 'qn' 'qr' 'qs' 'qu' 'qx' 'r5' 'rh' 'ri' 'rk' 'rn' 'ry' 's0' 'sa' 'si' 'sr' 'st' 'ub' 'uc' 'uf' 'uq' 'ur' 'v9' 'vn ' 'w9' 'wd' 'we' 'wk' 'wt' 'wv' 'ww' 'xj' 'xk' 'yh' 'yk' 'zd' 'zw' 'zy' 2016-05-05 23:21:22.326724 101 'a6' 'aa' 'ae' 'bn' 'c0' 'c7' 'ck' 'df' 'dn' 'ds' 'dt' 'e0' 'ea' 'eo' 'eu' 'f0' 'f6' 'g1' 'gd' 'i4' 'j6' 'ja' 'je' 'jt' 'mv' 'no' 'of' 'os' 'ou' 'ox' 'pi' 'pq' 'pr ' 'q6' 'qk' 'ql' 'qv' 'qw' 'rh' 'rm' 'rv' 'sv' 't6' 'u2' 'un' 'ux' 'wc' 'wl' 'wo' '
```

```
wp' 'xg' 'y7' 'y8' 'ya' 'yn' 'yx' 'zl' 2016-05-06 00:21:22.326724 102 '2o' '2w' 'ac' 'an' 'bb' 'be' 'c3' 'db' 'dj' 'dm' 'dw' 'eb' 'ed' 'eh' 'ew' 'ex' 'fb' 'fi' 'g2' 'gh' 'gv' 'h6' 'hw' 'id' 'ie' 'iz' 'j8' 'jk' 'jv' 'kd' 'lk' 'm8' 'ml ' 'mr' 'mx' 'np' 'oe' 'on' 'oz' 'pj' 'pk' 'pm' 'pu' 'qb' 'ql' 'qv' 'qx' 'r0' 're' ' rj' 'rq' 'rw' 't3' 'ta' 'tc' 'td' 'th' 'to' 'tu' 'tx' 'ty' 'tz' 'u3' 'uf' 'vp' 'vz' 'wd' 'wh' 'wk' 'wl' 'wx' 'wy' 'wz' 'xe' 'xm' 'xs' 'ye' 'zd' 'zk' 2016-05-06 01:21:2 2.326724 103 'a6' 'au' 'aw' 'bj' 'bn' 'cy' 'dg' 'e3' 'ei' 'ek' 'em' 'et' 'ex' 'fi' 'fm' 'g4' 'gm' 'gz' 'hp' 'ia' 'ie' 'jd' 'lg' 'lj' 'm6' 'mi' 'nd' 'oj' 'oo' 'ov' 'px' 'q0' 'q4 ' 'qj' 'qp' 'qq' 'r1' 'r5' 'rh' 'ro' 'tg' 'tr' 'tu' 'ty' 'u2' 'uk' 'ux' 'we' 'wi' ' wk' 'wq' 'wu' 'xy' 'y0' 2016-05-06 02:21:22.326724 104 'ab' 'am' 'aq' 'b9' 'bj' 'ck' 'cw' 'e2' 'e8' 'ek' 'eo' 'ew' 'f2' 'ff' 'fh' 'ft' 'gl' 'gs' 'h7' 'i0' 'ik' 'jl' 'jo' 'jq' 'jr' 'kc' 'kg' 'kw' 'mm' 'mo' 'pb' 'pn' 'qe ' 'qg' 'qk' 'qr' 'qu' 'r2' 's8' 'sd' 'sq' 'su' 'td' 'tr' 'uh' 'uu' 'v2' 'vl' 'w8' ' wg' 'wm' 'wt' 'xl' 'xq' 'yi' 'yo' 'yq' 2016-05-06 03:21:22.326724 105 'da' 'e5' 'ec' 'gd' 'gf' 'jj' 'kx' 'ly' 'pd' 'pj' 'q6' 'qk' 'rm' 'sa' 'te' 'ut' 'wa' 'wc' 'wl' 'ws' 'wv' 'zb' 'zk' 'zz' 2016-05-06 04:21:22.326724 106 'am' 'as' 'ay' 'bl' 'e0' 'e1' 'ea' 'eg' 'f6' 'fc' 'fx' 'ia' 'io' 'jq' 'jx' 'kd' 'ky' 'lb' 'll' 'lr' 'lv' 'me' 'nv' 'o4' 'o7' 'oe' 'ok' 'oq' 'pe' 'pr' 'py' 'q7' 'qg ' 'qh' 'qj' 'qk' 'ql' 'qq' 'qr' 'qs' 'r1' 'rg' 'rl' 'rm' 'ro' 'sq' 'sr' 'sz' 'ti' ' ts' 'ue' 'ui' 'uu' 'uz' 'vk' 'y0' 'y2' 'y9' 'ym' 'yt' 'yx' 'z8' 'zd' 2016-05-06 05: 21:22.326724 107 '1d' 'a2' 'af' 'bb' 'dd' 'dg' 'dl' 'du' 'ee' 'ff' 'g0' 'hj' 'hk' 'i4' 'iy' 'jt' 'kq' 'm6' 'mh' 'ov' 'qf' 'qh' 'qq' 'rt' 'sw' 'ta' 'tc' 'we' 'wn' 'wy' 'wz' 'xd' 'xs ' 'y2' 'yg' 'yj' 'yk' 'zi' 'zq' 'zw' 2016-05-06 06:21:22.326724 108 '2e' 'ak' 'bv' 'cb' 'ch' 'cy' 'd9' 'dq' 'dr' 'e8' 'ec' 'ef' 'ek' 'es' 'f1' 'fw' 'gj' 'gw' 'hh' 'hr' 'i3' 'i6' 'ic' 'ji' 'jr' 'jy' 'kr' 'md' 'mu' 'od' 'og' 'oo' 'p9 ' 'pd' 'q1' 'q3' 'qq' 'qw' 'qy' 'ra' 'rj' 'rl' 'rn' 'sf' 't4' 't5' 't7' 'tl' 'tm' ' ts' 'u4' 'ug' 'ui' 'uw' 'vo' 'ws' 'ww' 'wy' 'yd' 'yo' 'yq' 'zm' 'zp' 'zw' 2016-05-0 6 07:21:22.326724 109 'ag' 'ao' 'ay' 'bk' 'bl' 'bw' 'cq' 'dp' 'dv' 'e5' 'ee' 'eu' 'fv' 'fx' 'gg' 'h8' 'ha' 'hk' 'ii' 'im' 'iq' 'it' 'je' 'jf' 'jr' 'js' 'km' 'ks' 'lo' 'lz' 'o8' 'ot' 'pg ' 'pl' 'q3' 'q9' 'qa' 'qd' 'qe' 'qf' 'qh' 'qn' 'qq' 'qy' 'qz' 'r7' 're' 'ri' 'rl' ' ro' 'rr' 'rx' 'ry' 'sh' 'sl' 'ss' 'sw' 't5' 'ta' 'te' 'th' 'tr' 'tt' 'tu' 'tv' 'u7' 'uk' 'um' 'up' 'uu' 'vl' 'vw' 'w0' 'wl' 'ws' 'wt' 'ww' 'xe' 'ya' 'yb' 'ye' 'yf' 'za ' 2016-05-06 08:21:22.326724 110 '5o' 'ar' 'at' 'c1' 'ch' 'cr' 'dp' 'dy' 'ed' 'el' 'er' 'f0' 'f7' 'fc' 'fh' 'fm' 'fx' 'g8' 'gd' 'gf' 'gh' 'gl' 'gp' 'gv' 'gy' 'hs' 'ht' 'hv' 'hy' 'i2' 'ia' 'lc' 'lu ' 'lv' 'ly' 'mb' 'mq' 'nn' 'nz' 'oa' 'oq' 'ot' 'ox' 'oz' 'p8' 'pc' 'pn' 'py' 'q2' ' q7' 'qe' 'qj' 'qn' 'qs' 'qv' 'qw' 'r1' 'r4' 'rh' 'rn' 'rq' 'rr' 's1' 'sa' 'sd' 'se' 'sr' 't6' 'ta' 'tf' 'ts' 'tw' 'tx' 'uk' 'ul' 'uw' 'v7' 'vu' 'vz' 'w7' 'wc' 'wd' 'wk ' 'wl' 'wo' 'wr' 'wv' 'x9' 'xe' 'xj' 'xl' 'xu' 'yi' 'ym' 'yq' 'z1' 'z5' 'zm' 2016-0 5-06 09:21:22.326724 111 '2i' 'ap' 'aw' 'bd' 'bs' 'c9' 'db' 'di' 'dl' 'dq' 'dr' 'e5' 'ej' 'el' 'ez' 'f9' 'ga' 'gp' 'hm' 'if' 'im' 'j9' 'k9' 'ka' 'kd' 'kj' 'lc' 'lf' 'lk' 'mf' 'mq' 'mr' 'o3 ' 'oe' 'oj' 'op' 'p5' 'p7' 'p8' 'pb' 'pv' 'py' 'qc' 'qd' 'qf' 'qi' 'qk' 'qq' 'qu' ' qw' 'qz' 'r2' 'r8' 'r9' 'rj' 'rk' 'ry' 'rz' 'sd' 'sk' 'sm' 't2' 't6' 't7' 'tp' 'tq' 'tt' 'tw' 'u7' 'uh' 'uv' 'vh' 'w0' 'wc' 'we' 'wh' 'wk' 'wl' 'yf' 'yk' 'ys' 'zi' 'zq ' 'zs' 2016-05-06 10:21:22.326724 112 '4u' 'a3' 'ck' 'dw' 'e5' 'fu' 'ij' 'iu' 'jd' 'jp' 'ka' 'kb' 'ld' 'op' 'p1' 'po' 'pw' 'q5' 'q7' 'qf' 'qq' 'qr' 'qv' 'rm' 'sv' 't6' 'td' 'tp' 'uw' 'vb' 'w4' 'w6' 'wq ' 'xh' 'y2' 'yf' 'yt' 'zj' 'zz' 2016-05-06 11:21:22.326724 113 'a6' 'ao' 'aq' 'ba' 'be' 'bg' 'cb' 'ci' 'cj' 'cq' 'cs' 'dc' 'e6' 'ea' 'ei' 'ex' 'fw' 'fy' 'g7' 'gg' 'gq' 'hg' 'ib' 'ig' 'im' 'jz' 'kv' 'me' 'mi' 'mj' 'mp' 'o6' 'oq
```

```
' 'os' 'ov' 'pd' 'pl' 'pr' 'px' 'qf' 'qg' 'ql' 'qr' 'qz' 'r5' 'rl' 'ro' 'ru' 'rz' ' sy' 'sz' 't7' 'tt' 'u7' 'uf' 'ug' 'uo' 'vt' 'w3' 'w8' 'wb' 'wp' 'ww' 'wy' 'xl' 'xv' 'yc' 'z3' 2016-05-06 12:21:22.326724 114 'ca' 'cm' 'cr' 'eh' 'fd' 'fp' 'g8' 'ga' 'gh' 'h1' 'iu' 'je' 'jy' 'kh' 'lx' 'o4' 'oi' 'ov' 'ph' 'pm' 'qi' 'qv' 're' 'rg' 'rv' 'ry' 'si' 'sl' 'sv' 'sx' 'tq' 'tz' 'uh ' 'uq' 'uy' 'wi' 'wo' 'y7' 'yc' 'yn' 'yy' 2016-05-06 13:21:22.326724 115 'af' 'bq' 'c9' 'cg' 'eg' 'ei' 'eq' 'ez' 'fo' 'fp' 'gl' 'i6' 'it' 'iz' 'jg' 'ka' 'lf' 'lm' 'lr' 'mv' 'oc' 'oj' 'om' 'or' 'p1' 'p4' 'pt' 'q3' 'qd' 'qe' 'qh' 'qx' 'ra ' 'rd' 'sr' 'sz' 'tb' 'tc' 'tj' 'ug' 'uh' 'ux' 'wb' 'wc' 'wj' 'wy' 'xa' 'xb' 'y0' ' yj' 'yp' 'yz' 'zf' 'zl' 'zq' 2016-05-06 14:21:22.326724 116 '5y' 'a2' 'by' 'c9' 'e6' 'fd' 'fn' 'g7' 'h9' 'hj' 'j9' 'kg' 'kk' 'kn' 'kx' 'ln' 'q3' 'qa' 'qh' 'rb' 'rh' 'sj' 'sn' 'tx' 'tz' 'un' 'us' 've' 'vf' 'vh' 'wf' 'wp' 'wz ' 'xj' 'xq' 'yi' 'yz' 2016-05-06 15:21:22.326724 117 'a3' 'b9' 'c0' 'cg' 'ct' 'cu' 'dy' 'eh' 'el' 'ge' 'gt' 'hh' 'hu' 'if' 'j5' 'kq' 'lb' 'mh' 'o3' 'o6' 'oe' 'oi' 'ow' 'p5' 'ph' 'pw' 'q0' 'qh' 'ql' 'qy' 'r7' 'si' 'sk ' 'sv' 'tf' 'tm' 'to' 'tt' 'ty' 'u3' 'uj' 'uo' 'vi' 'vl' 'wc' 'wf' 'xx' 'y0' 'ya' ' yu' 2016-05-06 16:21:22.326724 118 'aj' 'ak' 'aq' 'ba' 'bd' 'bj' 'bk' 'bx' 'cr' 'cx' 'd0' 'dj' 'dl' 'ef' 'ei' 'ej' 'ek' 'em' 'eq' 'er' 'f3' 'f7' 'fi' 'fp' 'gv' 'h7' 'ha' 'hc' 'hh' 'hk' 'hn' 'ia' 'id ' 'im' 'iq' 'is' 'iw' 'ji' 'jk' 'js' 'ju' 'jx' 'l0' 'm1' 'mq' 'ng' 'o8' 'ot' 'ov' ' oy' 'p1' 'pu' 'pv' 'pz' 'qc' 'qh' 'qm' 'qq' 'qs' 'qt' 'qw' 'rc' 'rq' 'rt' 'sd' 't5' 'ta' 'tb' 'tj' 'tp' 'uk' 'un' 'v9' 'vt' 'wa' 'wd' 'wf' 'wm' 'wn' 'wv' 'wz' 'xp' 'ya ' 'yg' 'ym' 'yn' 'yr' 'zi' 2016-05-06 17:21:22.326724 119 'ae' 'ap' 'bi' 'd7' 'ee' 'ej' 'ek' 'ev' 'ew' 'fb' 'gm' 'hf' 'ho' 'hz' 'i6' 'ib' 'id' 'il' 'im' 'io' 'ip' 'ir' 'iv' 'j2' 'jf' 'jl' 'jo' 'kh' 'kk' 'kt' 'lr' 'm4' 'mi ' 'nm' 'ns' 'og' 'pv' 'pw' 'q4' 'qd' 'qi' 'r6' 'r8' 'rn' 'rp' 'si' 't7' 'ta' 'td' ' te' 'ti' 'tm' 'u6' 'ub' 'vu' 'w6' 'w8' 'wa' 'wb' 'wc' 'wd' 'wf' 'wh' 'wn' 'wt' 'wz' 'y5' 'ya' 'yg' 'yk' 'yn' 'z3' 2016-05-06 18:21:22.326724 120 'a6' 'ao' 'az' 'by' 'db' 'dl' 'eg' 'ei' 'el' 'eo' 'fh' 'fv' 'gl' 'h0' 'hl' 'hx' 'i9' 'iq' 'j7' 'jx' 'kg' 'kh' 'l9' 'nz' 'o9' 'oi' 'om' 'on' 'oq' 'or' 'pf' 'pz' 'qf ' 'qj' 'r5' 'rq' 'rw' 'sr' 'sx' 'tc' 'tg' 'tj' 'tl' 'to' 'uj' 'un' 'vw' 'w1' 'w5' ' w8' 'wn' 'ws' 'wv' 'x2' 'x3' 'xi' 'y4' 'yd' 'ym' 'ys' 'z7' 'zq' 'zv' 2016-05-06 19: 21:22.326724 121 'az' 'eq' 'fe' 'go' 'gv' 'ig' 'iz' 'ja' 'l4' 'mo' 'nm' 'no' 'of' 'pk' 'q9' 'qb' 'ql' 'qt' 'r7' 'rc' 'rm' 'tg' 'tv' 'u3' 'u7' 'wc' 'x4' 'xw' 'yl' 'zk' 'zn' 2016-05- 06 20:21:22.326724 122 '1f' '2j' '2q' '5c' 'am' 'ap' 'aq' 'az' 'bu' 'bx' 'cr' 'e0' 'e7' 'ea' 'eb' 'ec' 'eg' 'ew' 'ey' 'fh' 'fk' 'g2' 'go' 'h4' 'h8' 'ha' 'hb' 'hm' 'ia' 'ic' 'ie' 'ik' 'iu ' 'iv' 'j7' 'ja' 'k9' 'kw' 'lp' 'ly' 'mb' 'ns' 'ny' 'o0' 'of' 'ok' 'oz' 'pe' 'pr' ' qb' 'qd' 'qg' 'qt' 'qx' 'qy' 'rg' 'ro' 'rq' 'rz' 'sh' 'si' 'sl' 'sm' 'td' 'tg' 'tx' 'uh' 'um' 'up' 'uw' 've' 'vl' 'vp' 'vw' 'w2' 'w5' 'wc' 'wf' 'wi' 'wn' 'wq' 'ws' 'wv ' 'wy' 'wz' 'x1' 'xr' 'y1' 'zs' 'zz' 2016-05-06 21:21:22.326724 123 '25' 'cd' 'd2' 'dv' 'eo' 'es' 'f4' 'oc' 'qc' 'sh' 'te' 'tv' 'wd' 'wn' 'wo' 'xp' 'zt' 2016-05-06 22:21:22.326724 124 '28' 'b1' 'bj' 'bm' 'cz' 'dd' 'ds' 'ed' 'em' 'hh' 'hr' 'ie' 'ii' 'im' 'io' 'jn' 'jw' 'lg' 'lo' 'm6' 'mn' 'mw' 'ny' 'o6' 'p7' 'q4' 'qd' 'qf' 'qn' 'qq' 'qt' 'r1' 'r2 ' 'rn' 'rt' 'sh' 'ur' 'uv' 'ux' 'vc' 'wb' 'wn' 'xh' 'xx' 'yw' 2016-05-06 23:21:22.3 26724 125 '1m' '1s' 'aa' 'b0' 'be' 'cb' 'dc' 'dd' 'dh' 'eq' 'fa' 'ib' 'if' 'ik' 'it' 'jr' 'jz' 'ka' 'lq' 'lu' 'm2' 'o2' 'ob' 'oc' 'of' 'om' 'oz' 'pv' 'q4' 'qb' 'qk' 'qn' 'qs ' 'qu' 'r3' 'r9' 'rs' 'rw' 'sg' 'si' 'sv' 't9' 'tw' 'vq' 'vy' 'w2' 'w6' 'w9' 'y0' ' y1' 'ye' 'yq' 'z1' 2016-05-07 00:21:22.326724 126 '3k' '3v' 'a0' 'ah' 'am' 'an' 'ay' 'bd' 'cs' 'cu' 'cw' 'db' 'dp' 'e3' 'et' 'ey' 'fi' 'gl' 'gq' 'hh' 'hk' 'hx' 'i8' 'ih' 'ii' 'iv' 'iz' 'j5' 'jf' 'jo' 'jr' 'kd' 'km ''l''li''lt''4''
```

`'``'` `'``'`

```
''3''h'' ''9''d''f''h''k''
```

`'``'`

```
' 'lg' 'li' 'lt' 'm4' 'mo' 'mv' 'mw' 'n3' 'nh' 'nn' 'o9' 'od' 'of' 'oh' 'ok' 'or' ' pc' 'pg' 'pm' 'pn' 'q6' 'qj' 'qn' 'qr' 'qs' 'qw' 'r7' 'r9' 're' 'rm' 'rr' 'rt' 'rz' 'sb' 'sf' 'td' 'tu' 'uc' 'ug' 'uj' 'uu' 'w3' 'wa' 'wc' 'wg' 'wi' 'wm' 'wp' 'ww' 'wx ' 'wz' 'xb' 'xi' 'y0' 'y9' 'ya' 'yd' 'yg' 'yh' 'yv' 'yy' 'zo' 'zz' 2016-05-07 01:21 :22.326724 127 'bs' 'ee' 'gz' 'hv' 'ib' 'kc' 'lb' 'nu' 'ps' 'pt' 'qh' 'ud' 'vo' 'vq' 'vu' 'wb' 'wj' 'x3' 'xu' 'yf' 2016-05-07 02:21:22.326724 128 '12' 'ac' 'ay' 'bc' 'bj' 'bm' 'bo' 'ce' 'cf' 'ck' 'cr' 'db' 'do' 'du' 'dy' 'ea' 'ej' 'ek' 'eo' 'ep' 'et' 'f2' 'fc' 'fl' 'fs' 'fy' 'g9' 'gf' 'hj' 'hk' 'hp' 'i1' 'i5 ' 'ih' 'ii' 'im' 'jp' 'jx' 'k9' 'kf' 'ky' 'mb' 'mj' 'mk' 'nb' 'nc' 'o0' 'o9' 'oc' ' oj' 'oq' 'pm' 'ps' 'pt' 'pu' 'pv' 'py' 'qd' 'qi' 'qj' 'qk' 'ql' 'qm' 'qs' 'qz' 'ra' 'rc' 'rd' 'rh' 'ri' 'ro' 's0' 's3' 's7' 's9' 'sv' 't2' 't7' 'tm' 'tp' 'tw' 'tx' 'ty ' 'u3' 'u6' 'uf' 'ug' 'ui' 'uk' 'ut' 'ux' 'v5' 'w3' 'wk' 'wt' 'xo' 'xq' 'xr' 'xu' ' ye' 'yl' 'yn' 'yt' 'yv' 'zm' 2016-05-07 03:21:22.326724 129 '4d' '5a' 'ab' 'ae' 'ah' 'ai' 'be' 'cb' 'd6' 'dw' 'ea' 'eu' 'fb' 'fd' 'fe' 'fj' 'fk' 'g0' 'g9' 'gf' 'hc' 'hh' 'hk' 'i4' 'ik' 'iv' 'iz' 'j1' 'j3' 'j5' 'ju' 'jz' 'kc ' 'md' 'ng' 'nk' 'o1' 'o9' 'oi' 'om' 'p4' 'pl' 'pn' 'ps' 'q8' 'qa' 'qb' 'qh' 'qj' ' qm' 'qn' 'qo' 'qq' 'qr' 'qt' 'qu' 'qy' 'qz' 'ro' 'rs' 's2' 'sl' 'sm' 'sp' 'ti' 'tn' 'tu' 'tw' 'u7' 'ug' 'ui' 'ul' 'us' 'ut' 'vc' 've' 'vj' 'vk' 'w0' 'w2' 'w8' 'wi' 'wk ' 'wl' 'wm' 'wt' 'x6' 'xh' 'xy' 'yr' 'ys' 'yt' 'yy' 'yz' 'zr' 2016-05-07 04:21:22.3 26724 130 '1n' 'am' 'b9' 'bc' 'bi' 'dl' 'dv' 'ea' 'eq' 'ey' 'fj' 'g1' 'g3' 'g8' 'ge' 'it' 'iu' 'jh' 'jz' 'kk' 'ln' 'mc' 'mw' 'nf' 'nj' 'o4' 'o9' 'ob' 'ox' 'pq' 'q4' 'qb' 'qk ' 'qn' 'qs' 'qt' 'r4' 'ra' 'rg' 'rp' 'rx' 'sj' 'sq' 'ss' 't0' 'tg' 'ty' 'ue' 'ui' ' uj' 'uv' 'v6' 'vr' 'w1' 'w9' 'wj' 'wy' 'xt' 'ym' 'ys' 'yz' 2016-05-07 05:21:22.326724 131 'a2' 'bx' 'e4' 'em' 'eu' 'ey' 'gd' 'jj' 'k1' 'lm' 'my' 'oz' 'p8' 'pa' 'pj' 'qj' 'qp' 'qy' 'ri' 'rw' 'sj' 'sw' 'tv' 'uj' 'uk' 'um' 'ux' 'vs' 'wd' 'wf' 'xj' 'xs' 'xx ' 'xy' 'yd' 2016-05-07 06:21:22.326724 132 'az' 'bl' 'bo' 'cf' 'gt' 'h0' 'hx' 'iq' 'k2' 'kb' 'oc' 'qg' 'qn' 'qz' 're' 'rl' 'rv' 'xp' 'y8' 'yf' 2016-05-07 07:21:22.326724 133 'ab' 'ae' 'al' 'am' 'an' 'ap' 'be' 'd2' 'eb' 'ec' 'ep' 'eq' 'fn' 'hp' 'hx' 'i9' 'ie' 'jn' 'kh' 'kv' 'mi' 'mq' 'mv' 'ox' 'oz' 'pn' 'qk' 'qo' 'qr' 'r8' 're' 'rf' 'rp ' 't8' 'uj' 'uk' 'up' 'ur' 'vo' 'w7' 'wf' 'wp' 'ws' 'wt' 'ww' 'wx' 'xw' 'yd' 'yj' ' yn' 'yv' 'zr' 2016-05-07 08:21:22.326724 134 'af' 'ag' 'ak' 'bb' 'cr' 'cy' 'd7' 'db' 'df' 'di' 'eh' 'ew' 'fl' 'fr' 'gd' 'gp' 'hf' 'hk' 'hu' 'ib' 'ik' 'io' 'ix' 'jg' 'k9' 'kc' 'ke' 'm4' 'ma' 'mx' 'mz' 'ob' 'oi ' 'oo' 'or' 'ox' 'pg' 'pl' 'pu' 'qc' 'qe' 'qg' 'rl' 'ro' 'rv' 'rz' 'sj' 'sq' 'u4' ' ve' 'we' 'wi' 'wk' 'wy' 'xd' 'yh' 'yq' 'yv' 'yx' 2016-05-07 09:21:22.326724 135 '18' 'at' 'c6' 'ca' 'dj' 'dl' 'dx' 'ec' 'ek' 'f4' 'fo' 'fs' 'fz' 'h8' 'hn' 'ik' 'il' 'j4' 'jn' 'ld' 'ln' 'ls' 'lx' 'nu' 'o6' 'os' 'ot' 'ox' 'pa' 'pe' 'pp' 'pw' 'q1 ' 'qc' 'qd' 'qh' 'qk' 'qq' 'qr' 'rq' 'rr' 'rt' 'rv' 'rz' 's5' 'sd' 'sh' 'sy' 't3' ' tu' 'ty' 'uj' 'uo' 'up' 'uu' 've' 'vl' 'vu' 'wa' 'wd' 'wo' 'wr' 'ws' 'ww' 'xk' 'y0' 'y6' 'yi' 'yq' 'yy' 'z3' 2016-05-07 10:21:22.326724 136 'b6' 'bq' 'dv' 'e1' 'ez' 'f5' 'fh' 'ik' 'iy' 'jy' 'li' 'm2' 'qe' 'rp' 'te' 'u4' 'u8' 'uo' 'w3' 'w8' 'we' 'wo' 'wu' 'x5' 'yl' 2016-05-07 11:21:22.326724 137 'ak' 'ar' 'dg' 'ds' 'ep' 'fv' 'ge' 'jd' 'no' 'on' 'q5' 'qd' 'qo' 'qv' 'qx' 'r7' 'ra' 'ru' 'sa' 'ud' 'uo' 'wl' 'ye' 'yl' 2016-05-07 12:21:22.326724 138 '0w' 'bu' 'df' 'dj' 'du' 'dy' 'dz' 'gj' 'ho' 'je' 'kw' 'm1' 'o3' 'oo' 'pf' 'qh' 'qn' 'qu' 'rf' 'rj' 'ro' 'rv' 'ss' 't4' 'tc' 'tf' 'um' 'uo' 'v6' 'v8' 'wn' 'wo' 'xh ' 'y0' 'yz' 'zr' 2016-05-07 13:21:22.326724 139 '4t' 'ay' 'b3' 'dz' 'eo' 'ep' 'fd' 'fh' 'ht' 'hw' 'i3' 'jl' 'kn' 'op' 'qb' 'qd' 'ql' 'qm' 'qp' 'qy' 'rc' 'rh' 'rs' 'rw' 'sm' 't9' 'td' 'tu' 'tw' 'tz' 'u1' 'ug' 'uh ' 'ur' 'vt' 'we' 'wi' 'wn' 'x7' 'y8' 'yn' 'yy' 2016-05-07 14:21:22.326724 140'4a''56''ae''ao''ay''bn''bx''c9''cl''d0''d7''en''et''fj''fk''fu'
```

```
140 4a 56 ae ao ay bn bx c9 cl d0 d7 en et fj fk fu 'g4' 'ha' 'ht' 'hv' 'ih' 'ij' 'ir' 'iw' 'k1' 'k7' 'kq' 'kw' 'lg' 'm5' 'me' 'nw' 'oj ' 'ou' 'p6' 'pl' 'pq' 'pt' 'qc' 'qg' 'qk' 'ql' 'qm' 'qo' 'qq' 'rj' 's1' 'sd' 'sq' ' sz' 'tb' 'td' 'tr' 'tw' 'ug' 'uj' 'uo' 'ut' 'uy' 'wj' 'wk' 'ws' 'wz' 'x2' 'xx' 'xy' 'y1' 'y4' 'yc' 'yk' 'yt' 'yx' 'zp' 2016-05-07 15:21:22.326724 141 '3q' 'an' 'cp' 'ej' 'fx' 'gj' 'i3' 'ib' 'ik' 'jt' 'k5' 'n9' 'no' 'os' 'pg' 'qo' 'qp' 'qx' 'rb' 'rk' 'su' 'tk' 'tv' 'u1' 'up' 'w1' 'we' 'wj' 'wr' 'yf' 'yq' 'z5' 'zd ' 2016-05-07 16:21:22.326724 142 '3b' 'am' 'aq' 'ar' 'bm' 'de' 'e7' 'ed' 'eh' 'es' 'ey' 'fx' 'g5' 'gf' 'gs' 'hl' 'i7' 'iy' 'jn' 'k9' 'kf' 'km' 'll' 'ly' 'm0' 'm5' 'mh' 'nm' 'nq' 'of' 'or' 'p5' 'pn ' 'pz' 'qp' 'qt' 'qv' 'r0' 'rb' 'sg' 'sv' 'uv' 'w3' 'w8' 'w9' 'wa' 'we' 'wj' 'wn' ' wr' 'yd' 'yk' 'zq' 2016-05-07 17:21:22.326724 143 'cm' 'd2' 'en' 'ex' 'f4' 'f9' 'fp' 'ga' 'gk' 'hy' 'i3' 'j4' 'j9' 'jb' 'kj' 'ls' 'lw' 'mb' 'mq' 'o9' 'qg' 'qi' 'qm' 'qo' 'qw' 'qy' 'rc' 'rf' 'rj' 'rm' 's8' 'tb' 'tl ' 'tp' 'um' 'vg' 'vn' 'wb' 'wf' 'wl' 'xw' 'yl' 'zf' 'zt' 2016-05-07 18:21:22.326724 144 'aa' 'ap' 'b0' 'c6' 'e1' 'ex' 'fe' 'fu' 'fz' 'g1' 'g8' 'go' 'hl' 'iz' 'k3' 'ls' 'mw' 'mz' 'oa' 'ow' 'p6' 'q5' 'qh' 'qq' 'qx' 'ra' 'rh' 'rp' 'rw' 'tf' 'tk' 'tl' 'uc ' 'wi' 'x1' 'xb' 'yb' 'yw' 'yz' 'zm' 2016-05-07 19:21:22.326724 145 'gs' 'i6' 'i9' 'j2' 'l0' 'oq' 'qx' 'sc' 'xe' 'yu' 2016-05-07 20:21:22.326724 146 'bt' 'dg' 'dz' 'e4' 'ek' 'ep' 'fi' 'gk' 'gl' 'gu' 'hl' 'ho' 'io' 'ls' 'ni' 'nw' 'pv' 'px' 'qe' 'qf' 'qj' 'ql' 'qu' 'qy' 'rw' 'rx' 'ss' 't7' 'tt' 'ty' 'ud' 'up' 'uq ' 'uw' 'wn' 'wy' 'xt' 'yv' 'yx' 'za' 'zv' 'zw' 2016-05-07 21:21:22.326724 147 '1w' '2r' '9e' '9r' 'ci' 'es' 'f1' 'f4' 'fb' 'fx' 'g6' 'ga' 'gk' 'hj' 'hm' 'hu' 'i5' 'ii' 'jg' 'ji' 'ko' 'ku' 'l2' 'ld' 'lx' 'mt' 'n1' 'no' 'nw' 'o7' 'oi' 'pk' 'qy ' 'r9' 'rj' 'rr' 'rt' 's6' 'sd' 't0' 'tc' 'to' 'tp' 'tv' 'ud' 'ux' 'vk' 'wr' 'wy' ' xb' 'xr' 'xt' 'yc' 'yp' 'zy' 2016-05-07 22:21:22.326724 148 '3k' 'di' 'dp' 'em' 'ew' 'f5' 'hb' 'hn' 'j3' 'k0' 'lk' 'm4' 'mq' 'pr' 'qe' 'qo' 'qy' 'rc' 'ri' 'rt' 'so' 'ts' 've' 'w4' 'w7' 'wl' 'wn' 'wy' 'xf' 'y6' 'yt' 2016-05- 07 23:21:22.326724 149 '7n' 'ai' 'aj' 'ap' 'b9' 'bx' 'cu' 'dn' 'e1' 'e2' 'ed' 'eg' 'eo' 'hu' 'ie' 'ln' 'lq' 'nl' 'oa' 'qa' 'qe' 'qo' 'r5' 'ra' 'ri' 'rm' 'rw' 'ss' 'sx' 't3' 'tz' 'ut' 'uz ' 'wd' 'we' 'wn' 'wq' 'wr' 'ws' 2016-05-08 00:21:22.326724 150 'a0' 'ad' 'ak' 'ao' 'au' 'b0' 'dg' 'dt' 'e9' 'em' 'fg' 'fk' 'fn' 'gq' 'h7' 'hf' 'hm' 'ia' 'id' 'ig' 'iv' 'kv' 'l1' 'lm' 'lz' 'm1' 'mw' 'mz' 'na' 'nh' 'nl' 'nn' 'o1 ' 'o3' 'om' 'p2' 'p9' 'pj' 'pw' 'pz' 'qk' 'qm' 'qy' 'rs' 'ru' 'ry' 'sf' 'su' 'sw' ' sx' 'td' 'tl' 'tp' 'tw' 'u1' 'ug' 'un' 'uo' 'uq' 'ur' 'v5' 'vk' 'wd' 'wf' 'wj' 'wq' 'wy' 'xg' 'xk' 'xn' 'xq' 'yb' 'z0' 'zt' 'zu' 2016-05-08 01:21:22.326724 151 '6i' 'a3' 'ac' 'ax' 'br' 'ck' 'dc' 'dj' 'dn' 'dq' 'dt' 'dv' 'eb' 'ed' 'ei' 'en' 'eq' 'ey' 'f4' 'fk' 'fm' 'fp' 'fw' 'gn' 'gw' 'he' 'ho' 'io' 'ja' 'jj' 'jn' 'ju' 'jy ' 'kc' 'kk' 'l1' 'l4' 'lt' 'lx' 'm1' 'm7' 'mc' 'o6' 'ol' 'p3' 'pc' 'pe' 'pp' 'pv' ' px' 'q0' 'qb' 'qe' 'qr' 'qs' 'qt' 'qu' 'qv' 'qy' 'rg' 'rq' 's3' 'sm' 'so' 't5' 't9' 'tb' 'tp' 'ty' 'tz' 'u6' 'ua' 'ui' 'uv' 'vm' 'vw' 'w2' 'wa' 'wf' 'wi' 'wj' 'wt' 'ww ' 'wz' 'xg' 'y1' 'ya' 'yb' 'yd' 'yg' 'yh' 'yi' 'yk' 'yp' 'yz' 'zb' 'zk' 'zm' 'zo' 2 016-05-08 02:21:22.326724 152 '1r' '2z' '3d' '6d' 'ay' 'bb' 'bh' 'bq' 'bv' 'cn' 'cr' 'cs' 'd5' 'd9' 'dh' 'dq' 'dw' 'dz' 'e5' 'ea' 'eb' 'eh' 'er' 'fu' 'g0' 'ga' 'gc' 'h4' 'hf' 'hh' 'hx' 'ih' 'io ' 'jz' 'kk' 'ko' 'li' 'lz' 'n1' 'n4' 'nn' 'nt' 'o8' 'oa' 'oe' 'oh' 'ov' 'oz' 'p2' ' p5' 'pg' 'pt' 'px' 'qa' 'qe' 'qg' 'qm' 'qt' 'qv' 'qx' 'ro' 'rp' 'rv' 's6' 'sh' 'sn' 'sx' 'sz' 't6' 'th' 'tj' 'tu' 'u5' 'uk' 'uq' 'wg' 'wp' 'wv' 'xe' 'xv' 'y4' 'yf' 'yo ' 'yx' 'zr' 2016-05-08 03:21:22.326724 153 '2s' 'a7' 'ae' 'am' 'bx' 'd5' 'de' 'do' 'ds' 'dt' 'e1' 'e3' 'e7' 'ed' 'ee' 'eg' 'ek' 'em' 'es' 'ev' 'fi' 'fw' 'g2' 'gf' 'gs' 'gu' 'gy' 'h7' 'hh' 'hi' 'hm' 'hu' 'ih ' 'in' 'io' 'jr' 'js' 'jw' 'k0' 'k5' 'kb' 'l4' 'lu' 'm6' 'm8' 'mc' 'nb' 'od' 'ox' ' pc' 'pg' 'pv' 'py' 'q5' 'qc' 'qe' 'qf' 'qh' 'ql' 'qm' 'qo' 'qq' 'ra' 'rk' 'ro' 'rp' 'rr' 'ru' 'rw' 'se' 'sh' 't9' 'to' 'tq' 'tt' 'tw' 'u1' 'u4' 'ui' 'un' 'uq' 'vr' 'vy
```

`q` `q` `y`

```
' 'vz' 'wh' 'wp' 'ws' 'wt' 'wy' 'xt' 'y8' 'yd' 'zp' 2016-05-08 04:21:22.326724 154 '1f' '2u' 'ap' 'as' 'ax' 'bb' 'bf' 'cg' 'di' 'du' 'g3' 'g7' 'gk' 'ha' 'hv' 'hw' 'i6' 'jw' 'kg' 'ko' 'lu' 'ob' 'pn' 'qb' 'qg' 'qi' 'qs' 'qw' 'r3' 'r7' 'r9' 'rc' 're ' 'rf' 'rn' 'ru' 'rz' 'sh' 'sq' 't7' 'ta' 'td' 'u2' 'ua' 'uy' 'v8' 'va' 'wk' 'wn' ' wu' 'wy' 'xr' 'yi' 'yt' 'za' 2016-05-08 05:21:22.326724 155 '3w' 'aa' 'ad' 'cj' 'cu' 'cv' 'dv' 'ei' 'ej' 'ep' 'er' 'fc' 'fd' 'g5' 'ga' 'go' 'gr' 'gs' 'hq' 'hx' 'hy' 'i1' 'i5' 'ie' 'ip' 'jh' 'jn' 'jq' 'k7' 'ks' 'l0' 'l6' 'l9 ' 'lm' 'm5' 'mj' 'ng' 'nh' 'o8' 'od' 'on' 'pq' 'q3' 'q8' 'qb' 'qc' 'qf' 'qp' 'qs' ' r1' 'ra' 'rj' 'rw' 'si' 'sp' 't6' 'ta' 'tc' 'tk' 'tm' 'ty' 'ua' 'ud' 'ug' 'v7' 'vg' 'vm' 'w3' 'wc' 'wi' 'wp' 'wy' 'xk' 'xv' 'yi' 'ym' 'ys' 'zl' 2016-05-08 06:21:22.326 156 '2y' 'a3' 'ac' 'ae' 'ar' 'dp' 'ec' 'f8' 'f9' 'ga' 'gq' 'gs' 'hm' 'ib' 'if' 'im' 'j0' 'na' 'pb' 'pf' 'q9' 'qa' 'qu' 'qw' 'ra' 'rj' 'rm' 'rr' 'su' 'tj' 'vw' 'wb' 'wf ' 'wk' 'wo' 'ym' 'yu' 2016-05-08 07:21:22.326724 157 'an' 'cp' 'dq' 'ej' 'ez' 'lj' 'ln' 'nu' 'qy' 'sm' 't8' 'td' 'tg' 'us' 'uw' 'vn' 'y4' 'z9' 2016-05-08 08:21:22.326724 158 '1r' '2q' 'aa' 'ae' 'ah' 'aq' 'at' 'bx' 'c6' 'ca' 'cl' 'da' 'dp' 'ds' 'e0' 'e6' 'ea' 'eb' 'eg' 'er' 'ev' 'ew' 'fs' 'fw' 'gm' 'gx' 'hl' 'hv' 'hw' 'ib' 'iw' 'jc' 'jn ' 'jr' 'ju' 'k0' 'k5' 'k8' 'kf' 'kn' 'l1' 'ln' 'lp' 'ly' 'mz' 'n3' 'nc' 'ng' 'nk' ' o8' 'oe' 'oi' 'ol' 'ot' 'pb' 'pe' 'pk' 'q0' 'qa' 'qe' 'qg' 'qi' 'ql' 'qo' 'qv' 'r0' 'r2' 'r4' 'rg' 'rj' 'rm' 'sv' 'tk' 'to' 'tt' 'u7' 'ud' 'uo' 'ur' 'us' 'uv' 'vf' 'vm ' 'vn' 'w6' 'w7' 'wa' 'wb' 'wf' 'wg' 'wi' 'wv' 'ww' 'wx' 'xk' 'xy' 'yg' 'yh' 'ym' 2 016-05-08 09:21:22.326724 159 'd6' 'do' 'e4' 'eg' 'hm' 'i3' 'kg' 'nz' 'ow' 'pc' 'pv' 'q0' 'q4' 'q6' 'qx' 'r0' 'ri' 'sm' 'sn' 'tw' 'u9' 'ul' 'up' 'vk' 'we' 'wm' 'zv' 2016-05-08 10:21:22.326724 160 'ai' 'cg' 'cs' 'dc' 'dg' 'di' 'dj' 'dk' 'dp' 'du' 'eb' 'ec' 'ee' 'ei' 'ek' 'eu' 'f2' 'fh' 'fm' 'fy' 'hc' 'hm' 'i2' 'ia' 'jj' 'ke' 'kl' 'lb' 'lc' 'ln' 'me' 'nc' 'nf ' 'o6' 'oc' 'ok' 'os' 'pc' 'po' 'px' 'q2' 'q8' 'qa' 'qb' 'qd' 'qe' 'qg' 'qi' 'qo' ' qs' 'qt' 'qv' 'qx' 'r4' 'r9' 'ri' 'rn' 'rq' 'rr' 'rz' 's9' 'sf' 'sr' 'su' 'sw' 'sy' 'sz' 't2' 'ti' 'tv' 'ud' 'uv' 'wa' 'wc' 'wi' 'wk' 'wm' 'ws' 'wu' 'wv' 'wz' 'x2' 'xa ' 'xf' 'y8' 'yb' 'yd' 'yl' 'yp' 'yr' 'ys' 'z5' 'zh' 2016-05-08 11:21:22.326724 161 '1i' 'db' 'e4' 'er' 'fh' 'ft' 'hm' 'lg' 'll' 'of' 'og' 'q6' 'qj' 'r0' 're' 'th' 'up' 'ut' 'uw' 'vf' 'wq' 'ws' 'wx' 'zi' 2016-05-08 12:21:22.326724 162 '2k' '2v' '4h' '7c' 'a3' 'aa' 'al' 'an' 'aq' 'aw' 'b7' 'bb' 'bl' 'bn' 'by' 'ca' 'cf' 'cu' 'dd' 'dn' 'e6' 'ej' 'en' 'et' 'eu' 'ey' 'g8' 'gg' 'go' 'gw' 'hj' 'ho' 'i3 ' 'ii' 'iy' 'ke' 'kh' 'le' 'lf' 'lu' 'ml' 'ny' 'oa' 'oc' 'og' 'oh' 'os' 'pf' 'pl' ' qb' 'qd' 'qf' 'qj' 'qn' 'qu' 'qw' 'r8' 'rd' 're' 'rh' 'sc' 'sn' 'ss' 't0' 't7' 'tl' 'tt' 'tx' 'tz' 'u9' 'uc' 'ud' 'ul' 'us' 'ux' 'vb' 'vf' 'vg' 'vp' 'w5' 'w6' 'wk' 'wt ' 'wy' 'xd' 'xk' 'xm' 'xn' 'xr' 'xx' 'y0' 'yf' 'yl' 'yo' 'yw' 'zv' 2016-05-08 13:21 :22.326724 163 '3z' 'ah' 'ai' 'aq' 'bn' 'ck' 'cm' 'cq' 'ct' 'cy' 'd1' 'db' 'dn' 'e2' 'e7' 'ed' 'ee' 'eh' 'eq' 'er' 'ew' 'fc' 'fn' 'fp' 'fs' 'fw' 'fx' 'gl' 'gp' 'gw' 'ha' 'hq' 'hw ' 'hx' 'i2' 'ir' 'j9' 'jb' 'jn' 'jr' 'jx' 'jy' 'kk' 'kl' 'kx' 'kz' 'li' 'm2' 'me' ' mj' 'mr' 'na' 'nu' 'oe' 'ol' 'on' 'po' 'pv' 'q7' 'qa' 'qb' 'qd' 'qh' 'qp' 'qv' 'rh' 'rz' 'sf' 'sp' 't6' 'tl' 'to' 'tx' 'ty' 'ue' 'uf' 'un' 'uu' 'uw' 'vb' 'vq' 'wg' 'wp ' 'wt' 'wu' 'xb' 'xp' 'y1' 'y9' 'yi' 'yj' 'ys' 'yu' 'z7' 'zf' 'zt' 2016-05-08 14:21 :22.326724 164 'aa' 'ch' 'cm' 'db' 'dd' 'e7' 'eu' 'f5' 'fr' 'gg' 'ie' 'jc' 'kt' 'na' 'on' 'or' 'po' 'q0' 're' 's3' 'tb' 'tc' 'td' 'tt' 'tv' 'uf' 'wi' 'wq' 'wt' 'y8' 'ys' 2016-05- 08 15:21:22.326724 165 'a5' 'ab' 'ad' 'ao' 'b6' 'ea' 'es' 'ez' 'gm' 'gv' 'i0' 'in' 'jw' 'lh' 'lm' 'my' 'oj' 'ox' 'oy' 'pv' 'q1' 'qf' 'qh' 'qj' 'qo' 'qs' 'qt' 'qw' 'r0' 'ri' 'rk' 'ry' 's4 ' 'vs' 'wa' 'xy' 'y5' 'yg' 'yl' 'zm' 2016-05-08 16:21:22.326724 166 'ab' 'an' 'bm' 'bn' 'bp' 'ca' 'd9' 'dc' 'e0' 'e4' 'e5' 'eh' 'er' 'fe' 'fk' 'fv'
```

```
'ga' 'ge' 'hy' 'ic' 'ie' 'io' 'ja' 'jb' 'je' 'kp' 'ks' 'ln' 'md' 'ng' 'nr' 'oj' 'oy ' 'p5' 'p6' 'p7' 'pe' 'pg' 'pu' 'qa' 'qq' 'qv' 'qw' 'qy' 'rg' 'rj' 'rk' 'sk' 'tf' ' tw' 'ui' 'um' 'uu' 'v9' 'vu' 'wo' 'wp' 'wx' 'wy' 'xf' 'y0' 'yp' 'z6' 'zi' 2016-05-0 8 17:21:22.326724 167 '5i' 'a4' 'a8' 'ae' 'af' 'am' 'ap' 'ax' 'bf' 'cr' 'cw' 'dk' 'dz' 'ea' 'eb' 'ec' 'ef' 'ep' 'er' 'et' 'ex' 'fp' 'fv' 'gh' 'hy' 'hz' 'i8' 'ig' 'io' 'iq' 'ji' 'jw' 'kt ' 'le' 'lo' 'mi' 'nb' 'nq' 'o1' 'ol' 'oo' 'oq' 'oy' 'q3' 'q8' 'qi' 'qk' 'qo' 'qq' ' qs' 'r0' 'rg' 'rl' 'rt' 's6' 'sb' 'sk' 'sq' 't9' 'ta' 'tb' 'tg' 'tj' 'tu' 'ty' 'un' 'ur' 'uw' 'vi' 'wf' 'wk' 'wo' 'wt' 'wy' 'xj' 'xq' 'y0' 'y1' 'y9' 'yc' 'yn' 'yu' 'zs ' 2016-05-08 18:21:22.326724 168 '4m' 'a3' 'ac' 'ag' 'ai' 'au' 'av' 'bd' 'bu' 'cl' 'd0' 'dc' 'dy' 'ej' 'el' 'eo' 'es' 'eu' 'ex' 'fr' 'fx' 'g6' 'g9' 'gk' 'gq' 'gr' 'gw' 'gx' 'gz' 'hv' 'ii' 'ix' 'jj ' 'jy' 'k0' 'kl' 'kn' 'kw' 'l5' 'lo' 'lz' 'm1' 'n5' 'n9' 'nf' 'nm' 'nz' 'ol' 'os' ' ot' 'oy' 'p1' 'p9' 'pa' 'pj' 'pl' 'pp' 'qc' 'qh' 'qj' 'qr' 'qs' 'qw' 'qz' 'rg' 'ri' 'rl' 'rn' 'rp' 'rt' 'rx' 'rz' 'se' 'sl' 'sv' 'sy' 't8' 'td' 'th' 'tr' 'tx' 'u3' 'u7 ' 'uc' 'ud' 'ul' 'un' 'up' 'uv' 've' 'vz' 'w7' 'wr' 'y0' 'y6' 'yh' 'yo' 'yu' 'yy' ' yz' 'z6' 'zm' 2016-05-08 19:21:22.326724 169 'cb' 'ib' 'ih' 'jx' 'oy' 'ph' 'tl' 'ty' 'vb' 'vu' 'wu' 2016-05-08 20:21:22.326724 170 'ae' 'ak' 'ax' 'cm' 'cw' 'cx' 'df' 'dm' 'dw' 'eb' 'ef' 'ei' 'el' 'f1' 'fn' 'gu' 'hf' 'hk' 'ik' 'iw' 'jd' 'ju' 'jz' 'k7' 'ku' 'lq' 'mf' 'mw' 'oa' 'od' 'oe' 'ou' 'ow ' 'pc' 'ph' 'pw' 'q0' 'q2' 'qd' 'qq' 'qw' 'qx' 'rj' 'rk' 'rn' 'rx' 's2' 'sm' 'sx' ' t9' 'ti' 'tu' 'tw' 'u3' 'ud' 'wf' 'wm' 'wt' 'xl' 'xo' 'xs' 'yh' 'yi' 'ym' 'yr' 'yu' 'yw' 'z2' 'za' 'zf' 'zl' 'zz' 2016-05-08 21:21:22.326724 171 'a0' 'a6' 'aa' 'bk' 'dk' 'dv' 'e8' 'ff' 'fo' 'go' 'hh' 'hl' 'hu' 'if' 'jx' 'kc' 'kq' 'lr' 'lx' 'n6' 'ni' 'ob' 'ol' 'ql' 'rf' 'ry' 'sm' 'sn' 't7' 'tu' 'tz' 'uc' 'um ' 'uv' 'wf' 'wr' 'ws' 'wu' 'ww' 'xi' 'ym' 'z7' 'zo' 'zv' 'zz' 2016-05-08 22:21:22.3 26724 172 'ec' 'fd' 'gm' 'it' 'iu' 'kx' 'l1' 'pi' 'q1' 'qe' 'qs' 'ra' 'ri' 'rp' 'tn' 'to' 'vx' 'wh' 'wl' 2016-05-08 23:21:22.326724 173 '6y' 'aw' 'az' 'cn' 'cs' 'cx' 'd4' 'di' 'dl' 'e7' 'eg' 'eh' 'eo' 'ep' 'et' 'ew' 'ex' 'ey' 'fv' 'fz' 'gu' 'gv' 'hg' 'hl' 'hm' 'iv' 'jc' 'lb' 'me' 'nc' 'nz' 'o2' 'ox ' 'pn' 'po' 'pw' 'q4' 'q5' 'qg' 'qq' 'qv' 'qz' 'r7' 're' 'rl' 'rq' 'rs' 'rx' 'sa' ' se' 'ti' 'tj' 'tn' 'tz' 'u6' 'uq' 'ur' 'us' 'v9' 'we' 'wn' 'wp' 'wr' 'ws' 'xo' 'ya' 'ye' 'yg' 'yx' 'zj' 'zl' 2016-05-09 00:21:22.326724 174 '12' 'ao' 'ed' 'ek' 'ew' 'ey' 'fm' 'gr' 'hc' 'ht' 'io' 'ir' 'jb' 'jw' 'ke' 'ld' 'qj' 'se' 'tm' 'tn' 'tw' 'wv' 'y5' 'yt' 'z6' 2016-05-09 01:21:22.326724 175 '6f' 'a1' 'ag' 'ak' 'ap' 'au' 'b1' 'b5' 'bi' 'c1' 'cu' 'd5' 'dc' 'dr' 'dv' 'eg' 'ej' 'ek' 'em' 'et' 'fe' 'fr' 'fz' 'ga' 'gb' 'gk' 'gu' 'gv' 'h5' 'hh' 'ho' 'hy' 'ii ' 'ik' 'ip' 'iv' 'ja' 'jg' 'jz' 'k0' 'kt' 'm6' 'mj' 'nd' 'o0' 'o1' 'oj' 'or' 'ot' ' ov' 'oz' 'ph' 'pm' 'pv' 'qa' 'qe' 'qf' 'qg' 'qh' 'qj' 'qn' 'qt' 'qy' 'r5' 'rd' 'rg' 'rs' 'ru' 'rz' 's7' 'sf' 'si' 'sl' 'sw' 'sy' 't0' 't3' 'th' 'tn' 'tq' 'tu' 'ub' 'us ' 'ux' 'vb' 'vo' 'wa' 'wd' 'wn' 'wq' 'wt' 'ww' 'wx' 'y1' 'yh' 'yo' 'yq' 'yz' 'z7' ' ze' 2016-05-09 02:21:22.326724 176 '2p' '3w' 'ah' 'at' 'bg' 'bv' 'bz' 'cu' 'd8' 'dw' 'eb' 'ec' 'ei' 'er' 'es' 'fn' 'gl' 'hd' 'hx' 'ij' 'ip' 'ki' 'lh' 'mx' 'my' 'nq' 'o3' 'o7' 'ok' 'or' 'os' 'pd' 'pu ' 'q5' 'qa' 'qc' 'qd' 'qg' 'qh' 'ql' 'qs' 'qt' 'qu' 'qx' 'qy' 'rb' 'rd' 'rk' 'rs' ' ru' 'rv' 'rw' 'sn' 'tm' 'vw' 'w9' 'wa' 'wb' 'wm' 'ws' 'xe' 'xo' 'xu' 'y6' 'yh' 'yj' 'z4' 'zg' 2016-05-09 03:21:22.326724 177 '2y' '4v' 'ac' 'at' 'av' 'bd' 'bs' 'c3' 'ca' 'cf' 'cg' 'cq' 'cw' 'cz' 'db' 'dx' 'e7' 'eg' 'ei' 'el' 'et' 'ey' 'fo' 'fq' 'fw' 'fx' 'gd' 'gl' 'gw' 'h6' 'hd' 'hp' 'hy ' 'il' 'ir' 'is' 'j5' 'k4' 'k8' 'kc' 'kp' 'kz' 'l0' 'l1' 'm4' 'm6' 'mn' 'mr' 'nx' ' ov' 'ox' 'pn' 'pq' 'q3' 'qd' 'qj' 'qk' 'qo' 'qw' 'qx' 'rd' 're' 'rg' 'rq' 'rr' 'rx' 'rz' 'sb' 't0' 't3' 't4' 'tc' 'tk' 'tp' 'tr' 'tv' 'u7' 'uf' 'um' 'uo' 'uq' 'va' 'vc
```

```
' 'vi' 'vy' 'vz' 'w1' 'w6' 'wo' 'wq' 'xh' 'xn' 'y5' 'yo' 'ys' 'yt' 'zs' 'zu' 2016-0 5-09 04:21:22.326724 178 '3i' 'a3' 'af' 'cc' 'cs' 'cv' 'd8' 'ei' 'ej' 'ep' 'et' 'ex' 'fb' 'fe' 'fx' 'hc' 'ij' 'jf' 'jp' 'jr' 'js' 'kc' 'km' 'kz' 'lc' 'm7' 'nv' 'ob' 'oc' 'pt' 'q5' 'q7' 'q8 ' 'qc' 'qm' 'qn' 'qs' 'qy' 'ra' 're' 'rk' 'rx' 's0' 's4' 'se' 'sh' 'sm' 't7' 'tl' ' to' 'tz' 'ue' 'um' 'w3' 'wk' 'wp' 'ya' 'yl' 'yn' 'ys' 2016-05-09 05:21:22.326724 179 'ah' 'c3' 'd1' 'dh' 'dz' 'ei' 'em' 'ex' 'fe' 'fk' 'g7' 'gz' 'hi' 'hx' 'i3' 'iu' 'j1' 'jm' 'k8' 'kb' 'ku' 'lf' 'lv' 'lz' 'm3' 'mn' 'my' 'nc' 'oj' 'pk' 'qh' 'qn' 'qo ' 'qq' 'rf' 'ru' 'ry' 's9' 'sa' 'sc' 'sd' 'se' 'sz' 'td' 'tg' 'tq' 'tx' 'tz' 'vr' ' vu' 'w3' 'wd' 'wl' 'wp' 'x9' 'yb' 'yd' 'yr' 'yt' 2016-05-09 06:21:22.326724 180 '6t' 'a9' 'db' 'ea' 'ec' 'ez' 'fq' 'gj' 'hb' 'hs' 'lc' 'or' 'p4' 'ph' 'pp' 'qr' 'qx' 'rc' 'rl' 'tn' 'u5' 'w9' 'x1' 2016-05-09 07:21:22.326724 181 '5l' 'a2' 'ak' 'au' 'cj' 'cx' 'ed' 'eg' 'ej' 'em' 'es' 'ex' 'fs' 'ft' 'hm' 'i9' 'ky' 'l3' 'lz' 'mi' 'o2' 'oc' 'oe' 'ok' 'p2' 'q1' 'q5' 'qo' 'qv' 'qw' 'rf' 'rm' 'rv ' 'sc' 'si' 'tx' 'uq' 'v3' 'v4' 'vo' 'w4' 'wf' 'wl' 'wq' 'wt' 'xj' 'yr' 2016-05-09 08:21:22.326724 182 'a3' 'ag' 'ar' 'au' 'ax' 'be' 'cy' 'd7' 'dd' 'do' 'e3' 'eb' 'eo' 'er' 'ev' 'ey' 'fp' 'gj' 'hk' 'hw' 'hy' 'if' 'ig' 'ii' 'in' 'io' 'iq' 'is' 'kh' 'll' 'n8' 'nd' 'np ' 'nz' 'og' 'ot' 'ox' 'oy' 'pe' 'px' 'qa' 'qb' 'qe' 'qf' 'qh' 'qj' 'qm' 'qn' 'qt' ' qu' 'qw' 'qx' 'r6' 'r9' 'rb' 'rc' 'rd' 'rn' 'rq' 'se' 't7' 'tb' 'ti' 'tq' 'u0' 'u6' 'ub' 'ud' 'vd' 'vj' 'vl' 'vo' 'wd' 'wg' 'wh' 'wi' 'wk' 'wo' 'wv' 'wz' 'xy' 'y9' 'yl ' 'ym' 'yo' 'yp' 'ys' 'yu' 2016-05-09 09:21:22.326724 183 'bs' 'cd' 'ci' 'cq' 'dd' 'el' 'ev' 'f4' 'f6' 'f7' 'fh' 'fu' 'hi' 'ib' 'kp' 'nn' 'nu' 'oc' 'os' 'qc' 'qj' 'qm' 'qn' 'qu' 'qw' 'qx' 'r7' 'rc' 'rv' 't1' 'tl' 'tr' 'u0 ' 'vi' 'wl' 'wp' 'wu' 'xc' 'y2' 'yu' 'zc' 'zi' 'zw' 'zy' 2016-05-09 10:21:22.326724 184 'a7' 'bq' 'el' 'ey' 'fp' 'fu' 'fx' 'gr' 'hi' 'hl' 'jm' 'ki' 'kp' 'n6' 'o9' 'oj' 'op' 'ou' 'p7' 'pm' 'pp' 'q7' 'qa' 'qc' 'qj' 'qk' 'qm' 'si' 'st' 'tn' 'uc' 'w6' 'wp ' 'xu' 'y5' 'yk' 'ys' 'yu' 'zs' 2016-05-09 11:21:22.326724 185 'al' 'fh' 'fk' 'gy' 'he' 'ie' 'iz' 'lq' 'oh' 'pu' 'q7' 's6' 'sd' 'sr' 'sw' 'uu' 'uz' 'v6' 'ws' 'xo' 2016-05-09 12:21:22.326724 186 'ch' 'e1' 'fi' 'g8' 'go' 'hf' 'i1' 'ic' 'in' 'it' 'j7' 'jk' 'jl' 'jv' 'nm' 'of' 'oz' 'r8' 'rc' 'rk' 'rp' 'rx' 'sp' 'tb' 'tv' 'tw' 'ul' 'wx' 'zj' 2016-05-09 13:21:2 2.326724 187 'ab' 'ac' 'b9' 'br' 'c8' 'eh' 'en' 'eq' 'ev' 'ew' 'f6' 'gd' 'ik' 'j5' 'jm' 'kc' 'ke' 'ok' 'p6' 'pa' 'qv' 'ri' 'rm' 'ro' 'rp' 'rq' 'rx' 'rz' 'se' 'tb' 'td' 'ti' 'tj ' 'tn' 'ul' 'wj' 'wp' 'ws' 'yh' 'zb' 'zc' 2016-05-09 14:21:22.326724 188 'd6' 'e4' 'ev' 'fd' 'i3' 'if' 'j1' 'j5' 'o8' 'oj' 'ok' 'pw' 'qc' 'qd' 'qf' 'qt' 't8' 'tw' 'u1' 'u7' 'wr' 'wv' 'ww' 'yh' 'yn' 'yz' 2016-05-09 15:21:22.326724 189 '2u' 'au' 'bz' 'cd' 'cj' 'cm' 'cq' 'ct' 'cw' 'd1' 'ds' 'dw' 'dz' 'ec' 'ei' 'eo' 'fk' 'fq' 'fx' 'g6' 'gl' 'gs' 'i5' 'if' 'im' 'iq' 'jd' 'k0' 'k5' 'kr' 'lv' 'lx' 'n5 ' 'na' 'ny' 'ob' 'ot' 'ox' 'pa' 'pi' 'ps' 'qa' 'qc' 'qg' 'qh' 'qj' 'ql' 'qm' 'qo' ' qr' 'qs' 'r2' 'rh' 'rl' 'rr' 'rw' 'rx' 's0' 's8' 'sb' 'sc' 'sg' 'si' 'sl' 'so' 'sv' 't7' 't9' 'tc' 'te' 'tl' 'tn' 'to' 'tr' 'tx' 'ty' 'un' 'uz' 'vg' 'vw' 'ws' 'wt' 'wu ' 'xj' 'xy' 'y0' 'y1' 'ya' 'ye' 'yl' 'yn' 'yr' 'ys' 'yt' 'z3' 'z6' 'zw' 2016-05-09 16:21:22.326724 190 'bg' 'eh' 'eq' 'gg' 'gh' 'gm' 'gx' 'i7' 'iv' 'm3' 'mv' 'n3' 'o6' 'ox' 'oz' 'pb' 'qk' 'rj' 'rs' 'sk' 'su' 'tg' 'uf' 'uj' 've' 'ww' 'yf' 2016-05-09 17:21:22.326724 191 'a3' 'ai' 'ap' 'ar' 'at' 'be' 'br' 'bz' 'cw' 'd2' 'd6' 'df' 'dk' 'do' 'dp' 'dr' 'dw' 'e2' 'ef' 'eg' 'ej' 'eq' 'fb' 'fd' 'fq' 'ge' 'gr' 'h0' 'hp' 'i8' 'ih' 'ir' 'jb ' 'jd' 'kj' 'kz' 'l4' 'lm' 'lt' 'mj' 'mz' 'nc' 'ni' 'nw' 'of' 'oh' 'ol' 'ot' 'ov' ' p5' 'pf' 'pn' 'pp' 'pv' 'py' 'q2' 'q3' 'q7' 'qb' 'qc' 'qj' 'qo' 'qp' 'qr' 'qs' 'r6' 'ra' 'rc' 'rd' 'rx' 'se' 'sn' 'sr' 'sx' 't2' 't9' 'tm' 'tr' 'uj' 'vh' 'vn' 'vs' 'w0 ' 'w2' 'w3' 'wd' 'we' 'wj' 'wq' 'wr' 'wv' 'xe' 'xo' 'ya' 'ye' 'yq' 'yt' 'yw' 2016-0 5-09 18:21:22.326724 192'97'' ''h''b''8''dl''d''d''2''b'' ''j''
```

`'``'`

```
''f1''f'
```

```
192 '97' 'ac' 'ah' 'bn' 'c8' 'dl' 'ds' 'dw' 'e2' 'eb' 'eg' 'ej' 'ep' 'eu' 'f1' 'fe' 'g9' 'gs' 'h0' 'ha' 'he' 'hh' 'hy' 'i0' 'i8' 'i9' 'ia' 'ij' 'ip' 'jr' 'jt' 'jw' 'kq ' 'lo' 'lq' 'm7' 'me' 'na' 'ns' 'o1' 'od' 'oe' 'oi' 'om' 'oz' 'pc' 'pj' 'pk' 'qh' ' qi' 'qj' 'ql' 'qo' 'qq' 'qr' 'qs' 'qt' 'qw' 'qz' 'rc' 're' 'rh' 'ri' 'rr' 'sz' 'tc' 'tf' 'tk' 'tl' 'ue' 'uh' 'uj' 'un' 'uz' 'vq' 'vr' 'vv' 'w3' 'w4' 'we' 'wk' 'wt' 'wx ' 'xa' 'xh' 'xl' 'yg' 'yi' 'yj' 'ym' 2016-05-09 19:21:22.326724 193 'ah' 'ai' 'aj' 'cb' 'cg' 'dd' 'dl' 'dp' 'eb' 'ee' 'ei' 'es' 'ey' 'f5' 'fm' 'fr' 'g0' 'gj' 'gp' 'gq' 'gw' 'hc' 'hf' 'ig' 'ij' 'iu' 'kg' 'ld' 'mr' 'nh' 'o2' 'pp' 'pz ' 'qk' 'qr' 'qv' 'qz' 'r4' 'rb' 'rd' 'ro' 'rt' 'rw' 'rz' 'sr' 'sw' 'sy' 't6' 't9' ' tb' 'ts' 'tt' 'uo' 'vg' 'wd' 'wj' 'wl' 'wo' 'wp' 'wq' 'wt' 'ww' 'x8' 'yw' 'yx' 'z3' 'z9' 'zi' 'zz' 2016-05-09 20:21:22.326724 194 'a9' 'b8' 'de' 'dl' 'eg' 'fb' 'fi' 'fm' 'gj' 'hp' 'hx' 'if' 'ig' 'ii' 'ik' 'io' 'iw' 'ix' 'j1' 'j3' 'j8' 'ji' 'ki' 'kt' 'ld' 'm8' 'mi' 'mj' 'mx' 'mz' 'n2' 'nk' 'oe ' 'ok' 'oq' 'os' 'ot' 'pj' 'q4' 'qe' 'ql' 'qp' 'qq' 'r4' 'rl' 'rq' 'rx' 'sf' 'ss' ' td' 'ti' 'tl' 'u4' 'u5' 'uq' 'ux' 'v4' 'vl' 'vs' 'wb' 'wc' 'wg' 'wj' 'wn' 'ww' 'x9' 'xa' 'ye' 'yg' 'yl' 'yn' 2016-05-09 21:21:22.326724 195 'al' 'ar' 'ax' 'be' 'bu' 'dl' 'do' 'du' 'e5' 'es' 'ey' 'fb' 'fn' 'ga' 'he' 'hh' 'ho' 'i8' 'ic' 'in' 'iy' 'j1' 'j6' 'j9' 'jk' 'jm' 'ko' 'kv' 'kz' 'lk' 'ls' 'nb' 'oe ' 'ou' 'pf' 'pj' 'pm' 'pu' 'py' 'q4' 'q7' 'qe' 'ql' 'qo' 'qr' 'qt' 'rh' 'rs' 'ry' ' s3' 's6' 'sl' 'sq' 'tm' 'ud' 'uf' 'ur' 'vy' 'w5' 'w8' 'wp' 'wt' 'wx' 'xq' 'yc' 'yd' 'yi' 'yl' 'ym' 2016-05-09 22:21:22.326724 196 'b0' 'b7' 'bh' 'bt' 'c0' 'cd' 'dv' 'e5' 'ed' 'ef' 'eq' 'ff' 'fj' 'fk' 'ga' 'gt' 'gx' 'hm' 'hx' 'i1' 'ih' 'il' 'j5' 'ja' 'jf' 'jp' 'jt' 'm2' 'nf' 'nt' 'of' 'oo' 'ou ' 'p7' 'pa' 'pl' 'po' 'qa' 'qd' 'qr' 'qs' 'qt' 'qx' 'rb' 'rd' 're' 'rf' 'rv' 's0' ' sj' 'sw' 'tf' 'tu' 'tz' 'u2' 'ue' 'uq' 'ur' 'us' 'vw' 'w8' 'wc' 'wo' 'wt' 'x8' 'xo' 'yd' 'zi' 'zq' 2016-05-09 23:21:22.326724 197 '2d' '2w' 'ag' 'aj' 'am' 'ce' 'd2' 'd4' 'dd' 'dn' 'e0' 'e6' 'ef' 'ej' 'ek' 'er' 'f9' 'fd' 'fe' 'fq' 'ft' 'fv' 'gq' 'gy' 'he' 'ij' 'iq' 'it' 'iy' 'jf' 'jl' 'jr' 'ju ' 'kq' 'ku' 'lm' 'nj' 'nw' 'nx' 'oa' 'oe' 'oj' 'p2' 'pa' 'pm' 'pq' 'pv' 'q5' 'q9' ' qb' 'qd' 'qg' 'qj' 'qk' 'ql' 'qm' 'qu' 'qx' 'qz' 'rp' 'rq' 'rs' 's5' 'sk' 'ss' 'sy' 't2' 'ta' 'ts' 'tw' 'tx' 'u5' 'w3' 'w7' 'wa' 'wp' 'ws' 'wu' 'wy' 'wz' 'xz' 'y4' 'yn ' 'yy' 'zt' 'zw' 2016-05-10 00:21:22.326724 198 'ac' 'al' 'am' 'ap' 'ar' 'av' 'c1' 'cl' 'cz' 'dm' 'dp' 'dt' 'du' 'e0' 'es' 'eu' 'ev' 'ez' 'fa' 'fc' 'fj' 'fw' 'fz' 'gm' 'gx' 'ha' 'i6' 'i7' 'if' 'iz' 'j0' 'jd' 'jx ' 'k0' 'kr' 'mj' 'mk' 'mp' 'n4' 'nm' 'om' 'ot' 'pl' 'px' 'qa' 'qb' 'qg' 'qk' 'qn' ' qo' 'qr' 'qu' 'r7' 'rc' 'rk' 's3' 's4' 'se' 'ss' 'su' 't8' 'ta' 'te' 'tj' 'tk' 'ts' 'tz' 'ub' 'v2' 'wb' 'wd' 'we' 'wf' 'wj' 'wq' 'wr' 'ws' 'wv' 'wx' 'y6' 'ym' 'yn' 'yq ' 'ys' 'yv' 'zt' 2016-05-10 01:21:22.326724 199 '2o' '4i' '93' 'a2' 'az' 'b5' 'bk' 'cd' 'do' 'ea' 'ed' 'ej' 'el' 'es' 'ez' 'fd' 'fk' 'fu' 'h7' 'hg' 'hr' 'hs' 'hv' 'iz' 'j0' 'j9' 'jb' 'jc' 'jt' 'ln' 'lu' 'lw' 'lz ' 'mz' 'ns' 'nv' 'o8' 'oi' 'oq' 'ov' 'oz' 'pr' 'qi' 'qw' 'rb' 'rg' 'ro' 'rq' 'sb' ' sc' 't8' 't9' 'te' 'ti' 'tm' 'uo' 'uz' 'wd' 'wi' 'wn' 'wp' 'ww' 'wx' 'xt' 'xv' 'yb' 'yr' 'zs' 2016-05-10 02:21:22.326724 200 '1p' 'a7' 'ae' 'b2' 'dd' 'ef' 'eh' 'el' 'em' 'eo' 'fc' 'g0' 'hf' 'hh' 'i8' 'i9' 'in' 'is' 'iy' 'j3' 'ja' 'jl' 'js' 'jt' 'kz' 'lk' 'ng' 'nu' 'o6' 'oc' 'oe' 'om' 'ox ' 'pi' 'pp' 'pq' 'ps' 'qc' 'qe' 'qy' 'rh' 'rk' 'rn' 's3' 'sc' 'so' 'st' 'tc' 'tm' ' tp' 'tq' 'vh' 'wa' 'ya' 'zq' 2016-05-10 03:21:22.326724 201 '4r' 'ae' 'd9' 'da' 'ef' 'em' 'en' 'gi' 'h8' 'jq' 'kf' 'kh' 'kr' 'kv' 'li' 'lq' 'lr' 'm2' 'ny' 'po' 'q0' 'q8' 'qf' 'qg' 'qu' 'qw' 'qx' 'rd' 'rh' 'ry' 'sm' 'st' 't3 ' 'tc' 'u5' 'un' 'uw' 'wg' 'wt' 'yt' 'z9' 'zc' 2016-05-10 04:21:22.326724 202 'aa' 'ab' 'ag' 'ar' 'az' 'bp' 'bx' 'cx' 'eb' 'eh' 'ek' 'eo' 'eq' 'ez' 'fl' 'gm' 'gw' 'hd' 'ib' 'ig' 'jz' 'kg' 'lf' 'nw' 'oh' 'ok' 'om' 'oy' 'pg' 'ph' 'pi' 'qb' 'qi ' 'qn' 'qs' 'qt' 'qy' 'rl' 'sy' 'tc' 'tt' 'up' 'ur' 'uy' 'w6' 'w8' 'wb' 'wh' 'wv' ' ww' 'y5' 'yi' 'yp' 2016-05-10 05:21:22.326724 203'a5''al''b6''bu''co''d0''d4''db''e0''e2''eb''ei''ej''el''et''ez'
```

```
203 a5 al b6 bu co d0 d4 db e0 e2 eb ei ej el et ez 'g7' 'gu' 'j6' 'jl' 'k3' 'kf' 'km' 'kw' 'kx' 'lp' 'me' 'mw' 'my' 'n2' 'n5' 'n7' 'nr ' 'ny' 'oj' 'q8' 'qb' 'qg' 'qn' 'qq' 'qz' 'ra' 'rk' 'rl' 'rn' 's3' 's6' 't2' 't8' ' tk' 'tm' 'ul' 'uq' 'wg' 'y1' 'yc' 'yn' 'yq' 'yy' 'zr' 2016-05-10 06:21:22.326724 204 'a2' 'a8' 'ae' 'b3' 'b5' 'bn' 'bq' 'd4' 'd7' 'dh' 'dl' 'dt' 'e6' 'es' 'fa' 'fb' 'ff' 'gd' 'ge' 'h8' 'hj' 'hm' 'hq' 'hw' 'hy' 'im' 'ip' 'kb' 'kh' 'ku' 'lm' 'ly' 'mf ' 'nn' 'o0' 'oi' 'ok' 'or' 'pn' 'po' 'pq' 'pt' 'pv' 'q4' 'qc' 'qd' 'qu' 'qv' 'rd' ' rh' 'ri' 'rk' 'rp' 'rr' 'ru' 'si' 'sk' 'sq' 'ss' 'sx' 'sy' 'ta' 'tm' 'tq' 'tx' 'ul' 'um' 'uv' 'vj' 'vt' 'w7' 'wh' 'wi' 'wl' 'wn' 'wp' 'wq' 'ww' 'xb' 'y6' 'yq' 'z2' 'zn ' 2016-05-10 07:21:22.326724 205 '1o' '1v' '4v' 'ab' 'at' 'b5' 'bw' 'bz' 'cm' 'dc' 'dh' 'dj' 'dk' 'dq' 'e1' 'e5' 'ee' 'el' 'em' 'eo' 'ep' 'ew' 'fi' 'fy' 'gd' 'gh' 'gw' 'h7' 'i6' 'ia' 'ii' 'ip' 'is ' 'iu' 'jk' 'k5' 'kb' 'mf' 'mp' 'mw' 'mx' 'n1' 'na' 'nm' 'nq' 'ob' 'of' 'pa' 'pb' ' pd' 'pu' 'q4' 'qb' 'qe' 'qf' 'qj' 'qo' 'qr' 're' 'rj' 'ro' 'rt' 'rv' 'sb' 'sp' 'st' 'ub' 'ue' 'um' 'vz' 'w3' 'w7' 'w8' 'wh' 'wo' 'wt' 'x5' 'x9' 'xd' 'xj' 'xm' 'ya' 'yb ' 'yg' 'zr' 'zv' 2016-05-10 08:21:22.326724 206 'ay' 'bg' 'bp' 'cm' 'eg' 'ev' 'ff' 'go' 'hc' 'hl' 'jj' 'l0' 'os' 'q9' 'qc' 'qh' 'qo' 'rt' 'rx' 'so' 'sr' 'to' 'tx' 'uk' 'wb' 'y4' 2016-05-10 09:21:22.326724 207 'bj' 'dq' 'e2' 'ec' 'fs' 'g8' 'gd' 'iw' 'jt' 'nn' 'ns' 'o9' 'p0' 'tb' 'u7' 'uv' 'wf' 'wr' 'xf' 'z3' 2016-05-10 10:21:22.326724 208 'ae' 'af' 'ay' 'da' 'dp' 'dq' 'e1' 'gi' 'gk' 'rl' 'sf' 'ta' 'td' 'tf' 'tt' 'tw' 2016-05-10 11:21:22.326724 209 'ad' 'bs' 'dx' 'fi' 'i5' 'ia' 'j3' 'm5' 'mn' 'nr' 'ox' 'tg' 'un' 'vo' 'wj' 'wt' 'ys' 2016-05-10 12:21:22.326724 210 'cx' 'dg' 'do' 'dt' 'e7' 'ek' 'ez' 'fn' 'hj' 'hv' 'i2' 'i6' 'is' 'it' 'ka' 'kh' 'l5' 'lg' 'p5' 'qa' 'qf' 'qj' 'qw' 'qz' 'rl' 'sl' 'sr' 't7' 'tf' 'tu' 'uc' 'ud' 'uv ' 'vr' 'w0' 'we' 'wf' 'wj' 'ws' 'ww' 'xe' 'xh' 'xn' 'y9' 'yv' 2016-05-10 13:21:22.3 26724 211 '1h' '3s' 'ab' 'ae' 'ax' 'b1' 'bz' 'cy' 'dk' 'dq' 'ds' 'du' 'e8' 'ef' 'ej' 'ek' 'ex' 'f1' 'fe' 'ff' 'fn' 'fo' 'ft' 'fx' 'ge' 'go' 'gz' 'h6' 'hz' 'i2' 'iv' 'iy' 'j5 ' 'j6' 'ke' 'kf' 'lh' 'lr' 'mc' 'mj' 'na' 'ng' 'oh' 'om' 'oy' 'p2' 'pi' 'pk' 'py' ' q3' 'qb' 'qc' 'qg' 'qn' 'qo' 'qq' 'qu' 'qw' 'qx' 'qy' 'qz' 'r1' 'rk' 'rl' 'rq' 'rs' 'rt' 'ry' 'rz' 'sk' 'sl' 'so' 't9' 'td' 'te' 'tn' 'tw' 'tz' 'ud' 'uk' 'uo' 'uq' 'uw ' 'ux' 'uy' 'v1' 'vg' 'vq' 'w4' 'w9' 'wa' 'wg' 'wj' 'wm' 'wo' 'wr' 'ww' 'wy' 'xf' ' xg' 'y9' 'yh' 'yi' 'yk' 'ym' 'yq' 'yv' 'zm' 2016-05-10 14:21:22.326724 212 'aa' 'cb' 'd2' 'dd' 'de' 'e4' 'gd' 'go' 'hc' 'ic' 'in' 'ip' 'js' 'lm' 'o1' 'o3' 'pl' 'ra' 'rx' 'sj' 'ti' 'tu' 'tv' 'wc' 'we' 'wl' 'wq' 'wx' 'xg' 'xi' 'yc' 'yi' 201 6-05-10 15:21:22.326724 213 '8j' 'ao' 'bc' 'bh' 'co' 'cz' 'di' 'dq' 'dr' 'e1' 'ec' 'ei' 'el' 'et' 'eu' 'ex' 'f8' 'g7' 'gl' 'hq' 'hw' 'ib' 'kh' 'kn' 'kt' 'lc' 'md' 'n7' 'oe' 'p0' 'pg' 'pl' 'pm ' 'po' 'pr' 'q0' 'q6' 'ql' 'qv' 'qy' 'r7' 'ra' 're' 'rq' 'ru' 'ry' 'sm' 'sn' 't4' ' t5' 'tw' 'ty' 'u7' 'ud' 'uh' 'um' 'us' 'ux' 'v0' 'v7' 'vn' 'w6' 'we' 'wi' 'wm' 'x1' 'xo' 'xz' 'yn' 'yo' 'yz' 2016-05-10 16:21:22.326724 214 '4a' 'aj' 'an' 'aq' 'ax' 'bb' 'bh' 'ci' 'cn' 'd4' 'df' 'ea' 'ef' 'ek' 'en' 'eo' 'ex' 'fc' 'fj' 'fz' 'gb' 'gl' 'h7' 'hg' 'i1' 'i4' 'ia' 'im' 'j9' 'jg' 'ji' 'jj' 'kl ' 'l2' 'lb' 'ld' 'lh' 'm1' 'mf' 'n1' 'nd' 'ob' 'od' 'ot' 'ph' 'pk' 'po' 'pv' 'q1' ' q2' 'q4' 'qb' 'qu' 'qz' 'ra' 'rh' 'ro' 'rp' 's1' 'si' 'sl' 'sn' 't7' 't8' 'ta' 'tc' 'ub' 'ue' 'ul' 'v9' 'w7' 'wd' 'xq' 'y5' 'yj' 'yl' 'yp' 'yw' 'z9' 'zb' 'zu' 'zy' 201 6-05-10 17:21:22.326724 215 'a7' 'a9' 'ab' 'af' 'ah' 'bc' 'bg' 'bi' 'c2' 'cj' 'cl' 'dj' 'dn' 'do' 'dv' 'dw' 'e5' 'ec' 'es' 'f4' 'fa' 'fk' 'fv' 'h9' 'hi' 'hu' 'i5' 'ic' 'ig' 'im' 'ir' 'ji' 'jt ' 'k2' 'kc' 'kd' 'ki' 'km' 'kz' 'l3' 'lh' 'li' 'lv' 'ml' 'ne' 'ni' 'nt' 'nx' 'o9' ' pm' 'pn' 'pr' 'px' 'q0' 'qa' 'qe' 'qj' 'r6' 'ra' 'rj' 'rn' 'rq' 'ru' 'ry' 's0' 'sq' 'tb' 'to' 'tw' 'ua' 'ub' 'uf' 'ui' 'un' 'uu' 'vi' 'vo' 'vv' 'w5' 'w7' 'w8' 'wo' 'wv ' 'wy' 'xy' 'y2' 'ya' 'yh' 'yj' 'yo' 'za' 'zh' 2016-05-10 18:21:22.326724
```

`y` `y` `y` `ya` `y` `yj` `yo` `a` `8:` `:`

```
.367 216 '16' 'ae' 'al' 'ef' 'eg' 'ew' 'gi' 'ha' 'id' 'ng' 'o3' 'on' 'p9' 'rz' 'uf' 'vg' 'wo' 'wr' 'zh' 2016-05-10 19:21:22.326724 217 '1v' '20' 'au' 'bo' 'br' 'c9' 'cv' 'dp' 'ep' 'fo' 'gj' 'hb' 'hx' 'iv' 'iw' 'jc' 'jm' 'jw' 'k8' 'kg' 'km' 'kn' 'nd' 'o8' 'oh' 'ok' 'op' 'oy' 'px' 'pz' 'qh' 'qo' 'qp ' 'qs' 'qw' 're' 'rr' 'ry' 's3' 'sj' 't7' 't9' 'tt' 'tw' 'u9' 'ue' 'us' 'uu' 'v2' ' w3' 'wa' 'wf' 'wg' 'wt' 'wv' 'xc' 'yi' 'yu' 'yv' 'z4' 'zj' 2016-05-10 20:21:22.326724 218 'e2' 'ef' 'ev' 'fe' 'ij' 'j8' 'jm' 'kw' 'nb' 'ny' 'o6' 'o7' 'ou' 'pb' 'qd' 'qv' 'rh' 'rp' 's7' 'ti' 'ub' 'uk' 'wh' 'wi' 'wj' 'xj' 'xo' 'yx' 2016-05-10 21:21:22.326 219 'ao' 'as' 'bz' 'dc' 'dl' 'dn' 'du' 'dy' 'e3' 'ed' 'ee' 'ej' 'em' 'eo' 'ep' 'eq' 'er' 'fc' 'ft' 'g4' 'gc' 'gm' 'gq' 'gr' 'gy' 'hq' 'jg' 'k6' 'k9' 'ks' 'kz' 'l7' 'lo ' 'lu' 'lw' 'ly' 'nb' 'oc' 'oo' 'q9' 'qc' 'qd' 'qk' 'qs' 'qv' 'ro' 'rx' 'ry' 'sk' ' sv' 'sy' 'ti' 'tk' 'ui' 'un' 'uq' 'vl' 'w4' 'wl' 'wm' 'yj' 'yo' 'yu' 'yw' 'zg' 2016 -05-10 22:21:22.326724 220 '7w' 'ch' 'd7' 'eo' 'gw' 'i4' 'lq' 'o6' 'qt' 'y0' 2016-05-10 23:21:22.326724 221 '0h' '42' 'ak' 'al' 'bf' 'bz' 'co' 'd3' 'dc' 'dt' 'dy' 'ed' 'ee' 'eg' 'ev' 'ew' 'fg' 'fr' 'fz' 'gi' 'gy' 'ha' 'hb' 'hd' 'hl' 'hn' 'hs' 'ht' 'ij' 'io' 'iv' 'jh' 'jl ' 'jr' 'kc' 'kj' 'kt' 'ku' 'ky' 'ln' 'ml' 'mu' 'ng' 'nm' 'o0' 'o1' 'of' 'oh' 'or' ' p8' 'q8' 'qb' 'qp' 'qr' 'qt' 'qu' 'qv' 'r8' 'rj' 'rl' 'rp' 'rw' 'sk' 'ss' 'sw' 't9' 'th' 'tl' 'u5' 'uj' 'us' 'vg' 'vt' 'vz' 'w4' 'wb' 'we' 'wl' 'ww' 'wx' 'wy' 'wz' 'xj ' 'yb' 'yg' 'yn' 'yp' 'ys' 'yw' 'yz' 'zk' 'zp' 'zu' 2016-05-11 00:21:22.326724 222 '2i' 'am' 'ar' 'bl' 'by' 'ci' 'da' 'db' 'dc' 'dg' 'ea' 'ed' 'ei' 'ek' 'em' 'en' 'er' 'f2' 'f7' 'fi' 'fj' 'fu' 'fy' 'g0' 'g8' 'gn' 'gr' 'hl' 'hr' 'i2' 'it' 'ix' 'jg ' 'jr' 'ju' 'jx' 'lh' 'lj' 'm8' 'n7' 'o1' 'o5' 'ob' 'og' 'ok' 'oz' 'pg' 'pl' 'pz' ' q4' 'q9' 'qf' 'qh' 'qn' 'qt' 'qu' 'qw' 're' 'ri' 'rn' 'ro' 'rp' 'rz' 's7' 'st' 'sz' 't3' 'tk' 'tw' 'u1' 'u5' 'uh' 'uy' 've' 'vh' 'w1' 'x2' 'xi' 'y4' 'ya' 'yi' 'yk' 'yn ' 'zb' 'zo' 2016-05-11 01:21:22.326724 223 'ak' 'bg' 'bk' 'du' 'eb' 'ef' 'el' 'ft' 'gb' 'gc' 'hc' 'ho' 'i6' 'iv' 'ji' 'ke' 'mo' 'oc' 'oh' 'pe' 'pj' 'q6' 'qe' 'qg' 'qs' 'qv' 'r1' 'rr' 'rx' 'tc' 'te' 'tf' 'tk ' 'tq' 'ua' 'uq' 'ur' 'wq' 'wx' 'wz' 'xi' 'xq' 'yk' 'yo' 2016-05-11 02:21:22.326724 224 'ag' 'bm' 'co' 'cr' 'd7' 'dk' 'do' 'e6' 'e9' 'eb' 'ed' 'ef' 'eh' 'ep' 'eq' 'ew' 'f4' 'fd' 'fr' 'gc' 'gg' 'gq' 'gt' 'gv' 'h0' 'h4' 'hi' 'hm' 'i4' 'ib' 'im' 'is' 'j0 ' 'jc' 'jd' 'jo' 'ka' 'kk' 'kx' 'm3' 'nj' 'nr' 'nu' 'o2' 'ob' 'oe' 'oi' 'om' 'ow' ' oz' 'p3' 'pd' 'pf' 'ph' 'qi' 'qj' 'qu' 'qw' 'qy' 'r2' 'ra' 'rg' 'rj' 'rm' 'rn' 'ro' 'rp' 'rr' 'ry' 'rz' 's3' 'sa' 'so' 't6' 't7' 'ta' 'tc' 'u3' 'ub' 'vj' 'vm' 'vn' 'w7 ' 'wb' 'wf' 'wk' 'wn' 'x2' 'yi' 'zf' 'zh' 2016-05-11 03:21:22.326724 225 '2l' 'a4' 'ae' 'ag' 'cb' 'cs' 'cu' 'cy' 'dd' 'dj' 'ed' 'ee' 'ef' 'es' 'ex' 'ey' 'ft' 'fy' 'gs' 'h4' 'ho' 'ht' 'i2' 'i7' 'ia' 'iq' 'iz' 'jz' 'ku' 'kv' 'lq' 'mv' 'of ' 'oi' 'op' 'pb' 'pd' 'pl' 'pn' 'pq' 'q0' 'q3' 'qe' 'qi' 'qp' 'qs' 'qy' 'qz' 'r3' ' ra' 'rh' 'rk' 'ry' 'sj' 'st' 'ta' 'tc' 'te' 'tf' 'th' 'ti' 'to' 'tt' 'u2' 'u5' 'vf' 'vx' 'w4' 'w7' 'wm' 'wt' 'ww' 'wx' 'x2' 'xi' 'y1' 'ye' 'yq' 'yv' 'za' 'zo' 'zy' 201 6-05-11 04:21:22.326724 226 '1v' '44' 'aj' 'al' 'am' 'ba' 'bi' 'br' 'bt' 'c0' 'd6' 'dg' 'di' 'e1' 'e4' 'ei' 'ek' 'er' 'et' 'eu' 'ev' 'ex' 'fa' 'fc' 'fe' 'fh' 'fr' 'ga' 'gh' 'gu' 'hp' 'hq' 'ib ' 'if' 'io' 'ix' 'jo' 'jv' 'kd' 'l1' 'me' 'mh' 'mn' 'mo' 'mt' 'n7' 'nf' 'nk' 'oe' ' oy' 'pa' 'pg' 'pj' 'pm' 'pn' 'pq' 'py' 'q1' 'qd' 'qe' 'qi' 'qj' 'qr' 'qs' 'qz' 'rb' 'rs' 'su' 'sw' 't5' 'ti' 'tx' 'uc' 'ug' 'ui' 'uq' 'uz' 'v6' 'vp' 'we' 'wf' 'wj' 'wm ' 'wx' 'xe' 'y7' 'yt' 'yy' 2016-05-11 05:21:22.326724 227 'a6' 'ac' 'ao' 'au' 'cf' 'co' 'cr' 'd9' 'da' 'ds' 'du' 'e4' 'ea' 'ew' 'f1' 'fx' 'hr' 'hu' 'ic' 'id' 'ii' 'in' 'iq' 'iy' 'j3' 'jb' 'ji' 'jl' 'kf' 'mi' 'mp' 'o3' 'oe ' 'oj' 'on' 'p5' 'ph' 'pk' 'q1' 'q9' 'qa' 'qs' 'qu' 'qv' 'r9' 'rc' 'rj' 'rv' 's1' ' se' 'sl' 'su' 't2' 't5' 'tk' 'u8' 'uv' 'v9' 'vd' 'vi' 'w0' 'w3' 'we' 'wh' 'wm' 'wp' 'xm' 'y0' 'y1' 'y8' 'yf' 'yo' 'yw' 'zv' 2016-05-11 06:21:22.326724
```

```
228 'aw' 'dz' 'el' 'hb' 'iu' 'lc' 'm9' 'r5' 'rt' 'uz' 'x2' 'zp' 2016-05-11 07:21:22 .326724 229 'ap' 'i2' 'k0' 'n4' 'ou' 'px' 'qe' 'qo' 'qr' 't1' 'yz' 2016-05-11 08:21:22.326724 230 '3p' '5x' 'ag' 'au' 'aw' 'dl' 'eg' 'f2' 'f8' 'fb' 'fn' 'g9' 'ge' 'gt' 'hd' 'i7' 'ia' 'ij' 'is' 'jc' 'ku' 'kx' 'l7' 'lb' 'lq' 'mc' 'o3' 'oj' 'q1' 'qa' 'qg' 'qt' 'r9 ' 'rg' 'tw' 'tz' 'u6' 'us' 'w2' 'wr' 'wt' 'wu' 'x3' 'xx' 2016-05-11 09:21:22.326724 231 '4k' 'af' 'ah' 'b7' 'bj' 'by' 'ci' 'df' 'ds' 'eh' 'em' 'eq' 'ey' 'ez' 'fu' 'fv' 'g1' 'ga' 'go' 'gs' 'gy' 'gz' 'ho' 'i0' 'ie' 'ir' 'iv' 'k5' 'kj' 'ks' 'kw' 'l4' 'li ' 'm0' 'mo' 'o8' 'ol' 'oq' 'os' 'ox' 'pk' 'pl' 'pq' 'q3' 'q6' 'qa' 'qg' 'qj' 'qn' ' qq' 'qr' 'qu' 'r5' 'r9' 'rb' 'ri' 'rl' 'rs' 'ry' 's7' 's9' 'sa' 'sd' 'sx' 'ta' 'tc' 'td' 'tf' 'tg' 'th' 'ti' 'to' 'tq' 'tv' 'uo' 'ut' 've' 'vt' 'w8' 'wg' 'wm' 'ws' 'wy ' 'xy' 'y8' 'ya' 'yc' 'yf' 'ys' 'yu' 'zy' 2016-05-11 10:21:22.326724 232 '1h' '1j' '1o' '2d' 'ac' 'ak' 'b6' 'cx' 'd3' 'ds' 'dv' 'e7' 'es' 'ev' 'ez' 'fs' 'fx' 'fy' 'gc' 'gh' 'gs' 'gt' 'hk' 'ho' 'i8' 'id' 'ig' 'ii' 'iq' 'j5' 'jd' 'je' 'jg ' 'jk' 'jl' 'jo' 'jr' 'kf' 'kl' 'kq' 'lf' 'lh' 'lz' 'mb' 'mu' 'ni' 'nz' 'o4' 'ol' ' p7' 'pl' 'pm' 'pv' 'q5' 'qa' 'qe' 'qh' 'qi' 'ql' 'qq' 'qw' 'ra' 'rb' 'rn' 's5' 'sf' 'sh' 'so' 'sp' 'sq' 'sw' 'tj' 'tu' 'ty' 'u3' 'ue' 'uo' 'ux' 'v8' 'vo' 'vr' 'vz' 'w4 ' 'w8' 'wa' 'wk' 'wl' 'wo' 'wr' 'wu' 'ww' 'xs' 'xx' 'yb' 'yf' 'yn' 'yt' 'yw' 'zf' ' zg' 'zs' 2016-05-11 11:21:22.326724 233 '1m' '37' 'a8' 'ab' 'at' 'ce' 'cx' 'd6' 'dk' 'e9' 'eh' 'ei' 'el' 'eo' 'eu' 'ew' 'ex' 'f4' 'fh' 'fr' 'fs' 'fy' 'g6' 'gf' 'gl' 'gm' 'gp' 'h8' 'ha' 'hf' 'hi' 'hl' 'hr ' 'ie' 'ir' 'j6' 'jd' 'jr' 'jv' 'kz' 'l1' 'lg' 'ln' 'lp' 'ls' 'm0' 'ma' 'mi' 'mo' ' mu' 'na' 'np' 'o8' 'oc' 'oe' 'oh' 'ot' 'oy' 'ps' 'pw' 'q5' 'qa' 'qe' 'qg' 'qh' 'qi' 'qq' 'qz' 'rd' 'rg' 'ru' 'rv' 's9' 'sr' 'sv' 'sy' 'sz' 'ts' 'ty' 'uc' 'uh' 'uj' 'uk ' 'up' 'v9' 'vc' 'vg' 'vt' 'vy' 'wl' 'wm' 'wv' 'wy' 'wz' 'xg' 'yg' 'yv' 'yw' 'yy' ' z0' 2016-05-11 12:21:22.326724 234 'av' 'bh' 'cd' 'cw' 'dv' 'em' 'gn' 'iw' 'ja' 'ki' 'lc' 'lx' 'my' 'oi' 'ox' 'q0' 'qb' 'qi' 'qn' 'uf' 'ux' 'we' 'wn' 'xd' 'xq' 'y4' 'y9' 'zf' 'zs' 2016-05-11 13:21:2 2.326724 235 '11' '3o' '7a' 'au' 'bc' 'bx' 'cg' 'dz' 'e5' 'ea' 'eb' 'ee' 'eg' 'eo' 'er' 'eu' 'g2' 'gq' 'gx' 'i4' 'in' 'ip' 'iv' 'k4' 'kd' 'kw' 'lf' 'ls' 'oq' 'ot' 'oz' 'p7' 'ph ' 'pk' 'ps' 'qa' 'qd' 'qf' 'qi' 'qj' 'qr' 'qt' 'r4' 'rb' 'rd' 'rl' 'th' 'tl' 'tx' ' uc' 'uj' 'v6' 'vj' 'vz' 'we' 'wj' 'wl' 'wm' 'wp' 'wy' 'wz' 'xj' 'xk' 'xl' 'ya' 'yj' 'yl' 'yo' 'yw' 'zs' 'zv' 'zw' 2016-05-11 14:21:22.326724 236 '16' '64' 'aj' 'aw' 'bf' 'c0' 'ca' 'd2' 'd6' 'ec' 'ed' 'eq' 'ew' 'go' 'h2' 'in' 'is' 'j0' 'jd' 'ji' 'kv' 'l5' 'lp' 'lz' 'og' 'pb' 'pw' 'q9' 'qb' 'qe' 'qf' 'qg' 'qn ' 'qp' 'qt' 'qy' 'r7' 'rh' 'rw' 'sz' 't8' 'tb' 'te' 'tx' 'ui' 'un' 'uq' 'wa' 'wp' ' wu' 'wy' 'yn' 'ys' 2016-05-11 15:21:22.326724 237 '41' '7r' 'a2' 'ad' 'aj' 'ak' 'ao' 'as' 'b1' 'b2' 'cn' 'db' 'eb' 'ec' 'ee' 'em' 'ev' 'ex' 'f8' 'fa' 'fo' 'fs' 'fu' 'gh' 'gk' 'gr' 'gx' 'iq' 'iv' 'j9' 'jb' 'jc' 'jr ' 'kf' 'lg' 'm1' 'mq' 'mt' 'ne' 'nv' 'o5' 'od' 'os' 'ox' 'pc' 'pj' 'pq' 'q1' 'q6' ' q7' 'q8' 'qk' 'qm' 'qn' 'qp' 'qs' 'rj' 'rk' 's5' 'sb' 'sk' 'sn' 'sv' 't4' 'tb' 'th' 'ti' 'uc' 'uj' 'ut' 'vh' 'vp' 'wg' 'wi' 'wk' 'wp' 'ws' 'wv' 'wx' 'wy' 'x6' 'xa' 'xg ' 'xr' 'xy' 'y6' 'yj' 'yo' 'yv' 'yw' 'zt' 'zw' 2016-05-11 16:21:22.326724 238 '3b' '4p' 'ae' 'aj' 'ap' 'b3' 'bb' 'c0' 'cc' 'cf' 'cn' 'dz' 'e1' 'e9' 'eo' 'ew' 'ey' 'fk' 'fo' 'gd' 'gp' 'hb' 'i8' 'ia' 'ib' 'ie' 'ij' 'iq' 'ir' 'ix' 'jo' 'kp' 'lc ' 'ld' 'lp' 'ml' 'on' 'p8' 'pd' 'pf' 'pi' 'pn' 'pr' 'pt' 'pw' 'qe' 'qi' 'qj' 'qp' ' qr' 'qw' 'qz' 'r0' 'rj' 'rn' 'ro' 'rq' 'rr' 's3' 'sg' 'sz' 'tn' 'tw' 'ty' 'ui' 'uj' 'vj' 'vr' 'w5' 'w9' 'wa' 'wp' 'xt' 'ya' 'ym' 'z0' 'zr' 2016-05-11 17:21:22.326724 239 '1f' '3z' '43' 'am' 'b9' 'bg' 'cc' 'ct' 'cx' 'd0' 'de' 'dm' 'dr' 'e0' 'e8' 'ef' 'en' 'ev' 'fd' 'ff' 'fx' 'ga' 'gm' 'gp' 'gr' 'gs' 'gy' 'h1' 'hi' 'hl' 'hs' 'i4' 'i5 ' 'ic' 'jb' 'jj' 'kj' 'lh' 'ng' 'ni' 'nn' 'ns' 'nx' 'o1' 'oa' 'oe' 'og' 'p4' 'pd' ' ph' 'pj' 'pl' 'pw' 'q9' 'qa' 'qd' 'qh' 'ql' 'qr' 'qs' 'qw' 'qx' 'ro' 'rs' 'rw' 'ry'
```

```
'rz' 'sb' 'sj' 'sm' 'so' 't0' 't6' 'tc' 'ti' 'tk' 'tn' 'uk' 'um' 'uw' 'uy' 'v9' 'vd ' 'vg' 'w3' 'wf' 'wg' 'wi' 'wk' 'wm' 'wx' 'xe' 'xm' 'xn' 'y5' 'ye' 'yk' 'yq' 'z3' ' zj' 'zk' 'zt' 'zz' 2016-05-11 18:21:22.326724 240 '1s' '95' 'ac' 'aq' 'cb' 'ch' 'cq' 'ct' 'cz' 'dg' 'dj' 'eb' 'ed' 'ee' 'eg' 'en' 'eo' 'ep' 'es' 'fc' 'fl' 'fp' 'gu' 'gw' 'hx' 'i0' 'i2' 'ig' 'ih' 'il' 'in' 'iu' 'iy ' 'iz' 'jc' 'k7' 'ka' 'kl' 'km' 'kn' 'lz' 'mx' 'n6' 'nc' 'og' 'pt' 'pw' 'q0' 'qa' ' qe' 'qf' 'ql' 'qm' 'qp' 'qt' 'r7' 'rp' 'ru' 'rw' 'sb' 'sd' 't0' 't7' 'ta' 'tl' 'tn' 'tv' 'ty' 'ui' 'vx' 'wa' 'wc' 'wm' 'wp' 'wy' 'xi' 'xj' 'xk' 'yz' 2016-05-11 19:21:2 2.326724 241 '6n' 'da' 'dl' 'dx' 'el' 'ew' 'ff' 'fl' 'gc' 'iu' 'jh' 'jt' 'kt' 'lz' 'pd' 'q6' 'qj' 'ql' 'r3' 'ra' 'rn' 'ry' 'sg' 'tf' 'tp' 'tt' 'ub' 'ye' 'yf' 'yl' 'yp' 2016-05- 11 20:21:22.326724 242 '14' '1t' 'aa' 'ab' 'ag' 'aq' 'ax' 'bc' 'cb' 'cm' 'd1' 'db' 'ea' 'ek' 'en' 'ey' 'f0' 'g6' 'g7' 'gx' 'ha' 'ho' 'i1' 'i6' 'i8' 'it' 'iw' 'jl' 'jp' 'ko' 'kt' 'la' 'le ' 'mb' 'mk' 'mt' 'n6' 'na' 'ob' 'oc' 'od' 'on' 'op' 'or' 'ot' 'q6' 'qd' 'qf' 'qk' ' qp' 'qq' 'qr' 'qw' 'qy' 'r5' 'rf' 'rk' 'se' 'sp' 'sx' 't0' 'tj' 'tk' 'tq' 'tv' 'tx' 'u0' 'ub' 'ue' 'uf' 'um' 'us' 'uu' 'v9' 'vi' 'wb' 'wo' 'wu' 'wy' 'x9' 'xs' 'xu' 'y0 ' 'yo' 'zi' 2016-05-11 21:21:22.326724 243 '1i' 'ap' 'bh' 'ce' 'cp' 'di' 'dm' 'dt' 'es' 'eu' 'f2' 'f3' 'fw' 'fx' 'g5' 'gf' 'gy' 'h2' 'hl' 'i4' 'ii' 'iy' 'kp' 'lh' 'lr' 'me' 'of' 'og' 'ok' 'on' 'oo' 'pb' 'pd ' 'pt' 'qf' 'qk' 'qz' 'r4' 'r7' 're' 'ri' 'rj' 'ro' 'rx' 's2' 'tk' 'tl' 'tq' 'tx' ' ub' 'ui' 'us' 'vm' 'w1' 'w7' 'wi' 'wj' 'wq' 'wx' 'xp' 'yg' 'yr' 'yx' 2016-05-11 22: 21:22.326724 244 '3y' 'ak' 'am' 'b8' 'cp' 'd7' 'df' 'di' 'eg' 'em' 'en' 'eo' 'es' 'f6' 'fc' 'gg' 'gt' 'gv' 'hd' 'i3' 'jk' 'k6' 'la' 'lc' 'ol' 'ov' 'ow' 'p5' 'pl' 'qc' 'qf' 'rl' 'rn ' 'rt' 'rx' 't1' 'tf' 'tj' 'tz' 'ug' 'uo' 'we' 'wg' 'wk' 'wp' 'wv' 'y7' 2016-05-11 23:21:22.326724 245 'ae' 'ai' 'di' 'ea' 'eb' 'ec' 'gw' 'h8' 'hb' 'iw' 'iz' 'jf' 'jg' 'ks' 'le' 'p8' 'pl' 'pp' 'qd' 'qg' 'qm' 'qn' 'qu' 'qy' 'r4' 'rf' 'rq' 's1' 'sc' 'sq' 'v8' 'vh' 'vk ' 'wd' 'x7' 'y7' 'ym' 'yp' 'yr' 'yw' 2016-05-12 00:21:22.326724 246 'a7' 'ag' 'aq' 'aw' 'az' 'bf' 'bg' 'ce' 'cp' 'cx' 'dc' 'ek' 'en' 'es' 'fj' 'gb' 'hr' 'hs' 'ie' 'ik' 'is' 'jl' 'jr' 'kc' 'ku' 'l5' 'lj' 'lq' 'lr' 'nu' 'og' 'oj' 'os ' 'oy' 'p1' 'p6' 'pc' 'pk' 'pr' 'pu' 'px' 'py' 'q1' 'q4' 'qb' 'qc' 'ql' 'qo' 'qv' ' qz' 'r9' 'ra' 'rg' 'rp' 'sq' 'ts' 'tx' 'u8' 'ue' 'ui' 'uj' 'uk' 'up' 'v4' 'vg' 'vn' 'w2' 'w9' 'wa' 'wk' 'wt' 'y0' 'y9' 'yc' 'ym' 'ys' 'zh' 2016-05-12 01:21:22.326724 247 'af' 'aq' 'at' 'bh' 'cc' 'd3' 'dd' 'dg' 'dq' 'e1' 'e6' 'ec' 'ee' 'ex' 'ey' 'go' 'gt' 'h3' 'h8' 'hd' 'he' 'hm' 'i7' 'ii' 'ik' 'io' 'ip' 'it' 'iz' 'jg' 'k0' 'k5' 'k7 ' 'kb' 'ks' 'kw' 'ln' 'lp' 'lx' 'm3' 'nf' 'nh' 'of' 'og' 'oj' 'ok' 'ow' 'p7' 'pd' ' pj' 'pm' 'q1' 'q7' 'qg' 'qh' 'qk' 'qq' 'qr' 'qt' 'qw' 'rr' 'rs' 'ry' 's4' 's7' 'sd' 'si' 'sl' 'sp' 'sw' 'sz' 't6' 't8' 'tc' 'u2' 'um' 'uo' 'ux' 'vb' 'w2' 'wb' 'wi' 'wj ' 'ws' 'wt' 'wx' 'x3' 'xf' 'xt' 'yb' 'ym' 'zb' 'ze' 'zm' 2016-05-12 02:21:22.326724 248 '3g' 'af' 'aj' 'ak' 'ap' 'as' 'au' 'cp' 'cx' 'dh' 'dn' 'dr' 'ds' 'ej' 'en' 'eo' 'et' 'eu' 'ex' 'fq' 'fs' 'ft' 'gw' 'h5' 'i5' 'ix' 'j6' 'jc' 'jg' 'k1' 'kb' 'kh' 'kn ' 'kv' 'lj' 'lu' 'mc' 'mi' 'na' 'nq' 'ns' 'o4' 'o7' 'of' 'q5' 'q7' 'qe' 'qh' 'qi' ' qk' 'qr' 'qu' 'qw' 'r9' 'rb' 'ri' 'rx' 's3' 'sf' 'sm' 'so' 'sq' 'ss' 'su' 'sy' 't7' 'ta' 'ti' 'tn' 'tr' 'tx' 'u1' 'u3' 'ue' 'uh' 'up' 'uw' 'uy' 'va' 'w6' 'wg' 'wm' 'wp ' 'ws' 'wy' 'x1' 'y4' 'y6' 'yk' 'ys' 'yy' 'zf' 'zv' 2016-05-12 03:21:22.326724 249 'as' 'dj' 'dq' 'e3' 'ej' 'es' 'fn' 'fp' 'fu' 'ga' 'hb' 'hy' 'jz' 'l6' 'mp' 'ps' 'q4' 'qd' 'qm' 'qw' 'qy' 'qz' 'sa' 'sv' 'td' 'tn' 'tu' 'tx' 'ud' 'ue' 'uq' 'uv' 'v0 ' 'wi' 'wk' 'wm' 'wx' 'xh' 'y3' 'yd' 'yi' 'yn' 'yx' 'yy' 'zc' 2016-05-12 04:21:22.3 26724 250 'ar' 'ei' 'kq' 'ma' 'qa' 'qh' 'qq' 'qz' 'rx' 'st' 2016-05-12 05:21:22.326724 251 'a1' 'aa' 'c1' 'd7' 'dc' 'df' 'dh' 'e4' 'e9' 'ec' 'es' 'et' 'eu' 'ev' 'f3' 'g2' 'gu' 'he' 'il' 'j1' 'j6' 'jt' 'jv' 'ke' 'm8' 'm9' 'mh' 'ng' 'o8' 'on' 'pe' 'pf' 'pi
```

```
' 'pn' 'qf' 'qn' 'qu' 'qv' 'qw' 'rh' 'rl' 'rr' 'ru' 'sg' 'sk' 'uk' 'ul' 'ux' 'vd' ' vj' 'wk' 'yd' 'yn' 'yx' 'z0' 2016-05-12 06:21:22.326724 252 'af' 'as' 'at' 'aw' 'ax' 'ay' 'az' 'b2' 'bf' 'bl' 'ck' 'cs' 'df' 'dn' 'dv' 'ei' 'ek' 'ev' 'fg' 'fm' 'h0' 'hb' 'hk' 'i0' 'ib' 'if' 'ir' 'lk' 'm5' 'mr' 'np' 'om' 'p5 ' 'p7' 'pl' 'pq' 'q3' 'qh' 'qi' 'qj' 'qo' 'qp' 'qs' 'qt' 'qu' 'qv' 'qy' 'ra' 'sh' ' sm' 'so' 't2' 'ta' 'ti' 'tv' 'tz' 'u1' 'ug' 'um' 'v5' 'vd' 'w1' 'wn' 'wp' 'wr' 'ws' 'ww' 'xk' 'xx' 'y7' 'yf' 'yh' 'yk' 'yt' 'zr' 'zv' 2016-05-12 07:21:22.326724 253 '3a' '5k' 'a2' 'ah' 'au' 'ba' 'bb' 'bh' 'bu' 'cb' 'cj' 'cv' 'cx' 'df' 'dy' 'e4' 'e6' 'ed' 'ep' 'et' 'ev' 'ez' 'f1' 'fb' 'fl' 'fx' 'fz' 'gg' 'h5' 'hj' 'io' 'iz' 'ja ' 'k7' 'kf' 'lu' 'lv' 'md' 'ne' 'nh' 'oh' 'on' 'ow' 'p0' 'p8' 'pc' 'px' 'q3' 'qa' ' qf' 'qg' 'qj' 'qr' 'qs' 'qt' 'qv' 'qx' 'qz' 'r3' 'rm' 'rq' 'rt' 'rv' 'sa' 'sf' 'so' 't1' 't7' 'tb' 'tn' 'tq' 'tr' 'ts' 'tu' 'tz' 'u7' 'uf' 'uk' 'um' 'ut' 'va' 'vj' 'vm ' 'vx' 'vz' 'wa' 'we' 'wf' 'xe' 'xg' 'ya' 'yb' 'yu' 'zg' 'zo' 'zt' 'zz' 2016-05-12 08:21:22.326724 254 'aa' 'av' 'ay' 'bn' 'by' 'cm' 'da' 'dd' 'dj' 'dk' 'dr' 'dz' 'eu' 'ev' 'ez' 'f1' 'f8' 'gr' 'he' 'hp' 'hs' 'hw' 'iz' 'k1' 'kc' 'km' 'ko' 'kt' 'ln' 'ls' 'mx' 'n3' 'nl ' 'oe' 'oj' 'om' 'os' 'oy' 'pg' 'pr' 'pt' 'pv' 'qa' 'qc' 'qe' 'qi' 'qj' 'qm' 'qn' ' qq' 'qu' 'qx' 'qz' 'r0' 'r1' 'rf' 'rs' 'rx' 'ry' 's4' 'sg' 't2' 'tq' 'tt' 'tv' 'ty' 'ua' 'uj' 'uq' 'vi' 'vk' 'vx' 'wc' 'we' 'wi' 'wl' 'wo' 'wp' 'wv' 'ww' 'xi' 'xr' 'xs ' 'y9' 'yg' 'ym' 'yr' 'yt' 'yz' 'zo' 'zw' 2016-05-12 09:21:22.326724 255 '8p' 'ao' 'aq' 'c1' 'dh' 'dt' 'e9' 'eo' 'ev' 'fp' 'fu' 'gc' 'gz' 'hk' 'i5' 'id' 'ip' 'iy' 'jg' 'jr' 'k2' 'lo' 'mb' 'mf' 'oi' 'ou' 'qp' 'qr' 'qw' 'qx' 'ra' 'rj' 'tl ' 'ui' 'uu' 'uy' 'vb' 'wh' 'yt' 2016-05-12 10:21:22.326724 256 'aa' 'am' 'av' 'dt' 'du' 'eh' 'em' 'ev' 'ex' 'gu' 'h0' 'i4' 'i8' 'ku' 'la' 'lo' 'lw' 'n0' 'n9' 'on' 'pc' 'pl' 'pn' 'pr' 'q8' 'qc' 'ql' 'qn' 'qz' 'ra' 'rd' 'ry' 'sp ' 'tn' 'ts' 'u4' 'vg' 'vs' 'w7' 'wj' 'wm' 'xl' 'yg' 'yh' 'z0' 'zs' 2016-05-12 11:21 :22.326724 257 'ab' 'ah' 'ax' 'bd' 'ca' 'dh' 'e3' 'ea' 'ed' 'ef' 'en' 'eo' 'er' 'ev' 'ex' 'ez' 'f5' 'fh' 'fo' 'fv' 'ga' 'gb' 'gk' 'id' 'ik' 'in' 'ir' 'jp' 'js' 'jv' 'kf' 'kr' 'lx ' 'mu' 'mz' 'n5' 'od' 'on' 'pr' 'pt' 'pv' 'qb' 'qe' 'qj' 'ql' 'qq' 'qu' 'qw' 'rd' ' rl' 'rz' 's4' 'sv' 'ta' 'tj' 'tk' 'u8' 'ui' 'uj' 'uk' 'um' 'ux' 'uz' 'v9' 'vh' 'vl' 'w7' 'wb' 'wi' 'wm' 'ws' 'xi' 'ye' 'yg' 'yr' 'yw' 'zj' 'zn' 'zs' 2016-05-12 12:21:2 2.326724 258 'an' 'as' 'cm' 'dh' 'dk' 'do' 'ds' 'dv' 'e1' 'eh' 'ek' 'el' 'er' 'ew' 'ff' 'fo' 'fq' 'g2' 'gz' 'h0' 'hi' 'hk' 'hm' 'hs' 'i4' 'ij' 'iy' 'j5' 'jj' 'jk' 'jw' 'kq' 'kx ' 'ky' 'lo' 'lp' 'lw' 'ly' 'm2' 'm6' 'md' 'mv' 'ng' 'of' 'om' 'oy' 'p7' 'pr' 'q7' ' qc' 'ql' 'qq' 'qs' 'qy' 'qz' 'r2' 'r9' 'ra' 'rn' 'ro' 'rq' 'rv' 'rx' 'ry' 'rz' 's0' 'si' 'sy' 'sz' 't6' 't7' 'to' 'tt' 'tv' 'tx' 'ub' 'ur' 'uv' 've' 'vj' 'w3' 'w8' 'w9 ' 'wa' 'wb' 'wc' 'we' 'wm' 'wt' 'wu' 'wx' 'wy' 'y9' 'yd' 'yg' 'ym' 'yp' 'yt' 'yu' ' yy' 2016-05-12 13:21:22.326724 259 '1i' '3z' 'b6' 'bh' 'bn' 'bu' 'cm' 'do' 'dt' 'ef' 'eg' 'ek' 'eo' 'et' 'ex' 'f9' 'g3' 'gj' 'gl' 'h7' 'hp' 'i8' 'ih' 'im' 'in' 'jn' 'k1' 'k7' 'kd' 'lq' 'ms' 'mv' 'n7 ' 'nj' 'nt' 'o4' 'o9' 'ov' 'q2' 'qa' 'qh' 'qk' 'ql' 'qp' 'qu' 'qv' 'rj' 's8' 'sf' ' sh' 't7' 't8' 'um' 'un' 'uo' 'ut' 'uu' 'w1' 'wa' 'wf' 'wi' 'wx' 'xj' 'yc' 'yo' 'yt' 2016-05-12 14:21:22.326724 260 '8d' 'a2' 'af' 'ap' 'as' 'cg' 'cr' 'd4' 'dg' 'du' 'dv' 'eg' 'ei' 'el' 'em' 'fg' 'ft' 'g1' 'gt' 'h1' 'hg' 'i5' 'i8' 'ih' 'im' 'ir' 'iw' 'jd' 'jf' 'js' 'jw' 'jz' 'k8 ' 'ko' 'ky' 'la' 'lr' 'mq' 'no' 'ox' 'p8' 'p9' 'pb' 'pv' 'pw' 'px' 'q0' 'q1' 'q5' ' q7' 'qd' 'qh' 'qj' 'ql' 'qn' 'qo' 'qq' 'qx' 'qy' 'rc' 'rd' 'rf' 'rh' 'rr' 'rs' 'sd' 'sw' 'sz' 't3' 'tf' 'tn' 'to' 'tv' 'tx' 'ty' 'ua' 'ub' 'ud' 'uk' 'ul' 'us' 'uu' 'ux ' 'vl' 'vs' 'wf' 'wg' 'wl' 'wq' 'wt' 'wu' 'wx' 'x6' 'xi' 'yg' 'yh' 'z7' 'ze' 2016-0 5-12 15:21:22.326724 261 'ak' 'ar' 'cm' 'cq' 'da' 'df' 'e3' 'ew' 'fe' 'fr' 'gm' 'id' 'io' 'iy' 'jg' 'jt' 'jx' 'kb' 'lf' 'nv' 'od' 'qy' 'r3' 'r4' 'ro' 'rq' 'rw' 'sl' 'ss' 'su' 'sw' 't7' 'th ''ti''tp''u9''uq''v9''vq''vw''we''wg''wk''ws''xr''yf'2016051216:21
```

```
' 'ti' 'tp' 'u9' 'uq' 'v9' 'vq' 'vw' 'we' 'wg' 'wk' 'ws' 'xr' 'yf' 2016-05-12 16:21 :22.326724 262 '5h' 'a2' 'ad' 'ag' 'ar' 'cf' 'ch' 'dd' 'e6' 'ei' 'el' 'em' 'f3' 'fx' 'ga' 'gm' 'h8' 'hi' 'hl' 'hm' 'ix' 'jb' 'l5' 'm2' 'mh' 'mm' 'mu' 'n9' 'nf' 'nq' 'nw' 'o4' 'oe ' 'pa' 'pl' 'q1' 'qb' 'qd' 'qi' 'qj' 'qk' 'qu' 'qy' 'r0' 'r3' 'r8' 'rg' 'rj' 'rt' ' s1' 'sa' 'ss' 'sx' 'tb' 'tc' 'tj' 'uf' 'uh' 'um' 'uo' 'ut' 'vf' 'vo' 'w4' 'w7' 'wf' 'wk' 'wp' 'wq' 'wr' 'wt' 'wy' 'wz' 'xk' 'xt' 'ye' 'yv' 'zd' 'zp' 'zw' 2016-05-12 17 :21:22.326724 263 'ar' 'c3' 'c6' 'e0' 'e9' 'ed' 'ex' 'fh' 'fi' 'gu' 'ha' 'hr' 'id' 'jr' 'kk' 'kr' 'kz' 'm0' 'mp' 'ng' 'om' 'pa' 'qa' 'qf' 'rj' 'sp' 'to' 'tu' 'ty' 'ub' 'ud' 'ug' 'uk ' 'vj' 'vp' 'wf' 'wl' 'wu' 'x6' 'xs' 'y0' 'ya' 2016-05-12 18:21:22.326724 264 '5z' 'ai' 'al' 'ax' 'cd' 'dr' 'e1' 'ep' 'fi' 'gh' 'gk' 'ha' 'hc' 'ht' 'i5' 'ic' 'id' 'iq' 'iz' 'kk' 'kt' 'ld' 'mi' 'oh' 'ov' 'pn' 'q2' 'q7' 'qm' 'qy' 'ri' 'ru' 'rv ' 'sq' 'u8' 'u9' 'un' 'wq' 'wt' 'yd' 'yk' 'ys' 2016-05-12 19:21:22.326724 265 'aj' 'as' 'aw' 'bc' 'bj' 'bm' 'cd' 'd7' 'd9' 'di' 'ef' 'er' 'es' 'ew' 'fi' 'ft' 'g2' 'gq' 'gx' 'h9' 'he' 'hg' 'hu' 'i8' 'ie' 'ik' 'im' 'iq' 'ix' 'iy' 'jf' 'ji' 'ka ' 'kl' 'kt' 'la' 'lf' 'm8' 'm9' 'nh' 'nw' 'o7' 'oi' 'pi' 'ps' 'q6' 'qa' 'qb' 'qf' ' qm' 'qo' 'qq' 'qs' 'r9' 'rb' 'rf' 'rk' 'rx' 'sa' 'sb' 'sp' 't1' 'tb' 'tl' 'tm' 'u6' 'uc' 'um' 'un' 'ur' 'w3' 'wj' 'wu' 'xm' 'xr' 'xy' 'ya' 'yd' 'ye' 'yf' 'yj' 'yo' 'ys ' 'zc' 'zg' 'zl' 'zv' 'zz' 2016-05-12 20:21:22.326724 266 '1a' '4p' 'bn' 'br' 'dk' 'ec' 'en' 'eu' 'gd' 'h0' 'ha' 'hm' 'if' 'il' 'io' 'ip' 'is' 'iz' 'jl' 'jq' 'k6' 'kd' 'kf' 'kn' 'kp' 'ld' 'lf' 'lt' 'n8' 'na' 'nl' 'o1' 'pd ' 'pr' 'q8' 'qf' 'qr' 'qw' 're' 'rx' 'sa' 'sf' 'ta' 'tq' 'ux' 'v3' 'w6' 'wp' 'x2' ' y9' 'yi' 'yw' 'yx' 'z5' 'zl' 'zs' 2016-05-12 21:21:22.326724 267 'c8' 'db' 'dh' 'fh' 'g7' 'gm' 'if' 'ih' 'jd' 'li' 'ms' 'mt' 'no' 'or' 'p7' 'pc' 'qb' 'qm' 'sh' 'tk' 'uf' 'uz' 'vb' 'vp' 'wh' 'wr' 'wv' 'xh' 'xm' 'xp' 'zj' 2016-05- 12 22:21:22.326724 268 '1p' '51' 'aj' 'av' 'bj' 'bn' 'c1' 'dx' 'ex' 'gz' 'he' 'ia' 'ic' 'ip' 'kn' 'mx' 'o6' 'or' 'ql' 'rc' 'wf' 'wi' 'wn' 'y8' 'yr' 2016-05-12 23:21:22.326724 269 '8l' 'au' 'ay' 'bn' 'bs' 'ch' 'co' 'cu' 'dq' 'dv' 'eq' 'ev' 'ff' 'fp' 'fr' 'fz' 'gb' 'gu' 'hb' 'he' 'hj' 'id' 'ih' 'jb' 'kg' 'lm' 'ls' 'nm' 'oe' 'ot' 'p6' 'pb' 'ps ' 'q0' 'q8' 'qg' 'qh' 'qj' 'qo' 'qp' 'qr' 'qt' 'qz' 'r1' 're' 'rh' 'rp' 'ry' 's1' ' s4' 'sc' 'sd' 'sn' 'tf' 'ty' 'u4' 'us' 'vt' 'vx' 'wc' 'wd' 'ws' 'wv' 'xp' 'y2' 'y5' 'y6' 'yy' 'zh' 'zx' 2016-05-13 00:21:22.326724 270 'au' 'bo' 'dz' 'ek' 'eq' 'et' 'fa' 'hw' 'id' 'im' 'kr' 'p4' 'qx' 'rb' 'rx' 'sf' 'tl' 'tx' 'uf' 'ui' 'uw' 'vr' 'wb' 'wn' 'xw' 'yd' 2016-05-13 01:21:22.326724 271 '5q' '7c' 'a1' 'ac' 'ao' 'az' 'bw' 'cz' 'd8' 'dr' 'dy' 'ec' 'eg' 'ej' 'el' 'es' 'et' 'fa' 'fh' 'g2' 'gm' 'go' 'gp' 'gy' 'h6' 'hd' 'he' 'ho' 'ij' 'ik' 'it' 'jc' 'ji ' 'k8' 'ku' 'l8' 'lf' 'mw' 'n8' 'nb' 'nd' 'o3' 'ok' 'ol' 'ot' 'p8' 'pi' 'pl' 'pn' ' ps' 'qd' 'qe' 'qk' 'ql' 'qt' 'qz' 'r0' 'r7' 'rd' 'rg' 'rh' 'rm' 'ro' 'rp' 'ru' 'rz' 'sj' 'sm' 'sr' 'su' 'sv' 'sx' 't1' 'tc' 'tl' 'tq' 'uj' 'um' 'uv' 'uw' 'wa' 'wb' 'wi ' 'wo' 'wr' 'ws' 'wv' 'wz' 'xb' 'xg' 'ya' 'yb' 'yh' 'yi' 'ym' 'yn' 'yr' 'yv' 'z6' ' zf' 'zz' 2016-05-13 02:21:22.326724 272 '1j' 'ag' 'c3' 'cl' 'e4' 'ef' 'eh' 'f5' 'fi' 'gy' 'hx' 'lw' 'oa' 'pu' 'qa' 'qi' 'qt' 'qu' 'rl' 'ro' 'rs' 'sg' 'uq' 'wq' 'ya' 'yh' 'ys' 2016-05-13 03:21:22.326724 273 '6d' 'ao' 'bo' 'cq' 'e0' 'fi' 'fm' 'h6' 'i2' 'jl' 'kn' 'mj' 'nv' 'oq' 'p6' 'qd' 'qi' 'qn' 'r2' 'r8' 'rd' 'sd' 'sl' 'ta' 'tp' 'ub' 'uh' 'w3' 'wh' 'y1' 'yj' 'zk' 201 6-05-13 04:21:22.326724 274 '2a' '4s' 'c4' 'cd' 'dh' 'dv' 'eh' 'ek' 'ew' 'ex' 'ez' 'fm' 'hh' 'hj' 'ig' 'jf' 'ld' 'ly' 'mg' 'mx' 'o5' 'or' 'pa' 'pv' 'q1' 'qe' 'qj' 'qq' 'qr' 'qw' 'rb' 'rr' 's4 ' 's9' 'tm' 'uj' 'wc' 'wv' 'x0' 'xt' 'yc' 'ye' 'yh' 'yi' 'yk' 'yy' 2016-05-13 05:21 :22.326724 275 'aa' 'af' 'ee' 'hb' 'ih' 'j2' 'lv' 'mw' 'pp' 'q3' 'rd' 'tb' 'td' 'ua' 'ug' 'up' 'xh' 'yy' 2016-05-13 06:21:22.326724 276'ad''ar''az''b7''cf''cm''ct''cw''cy''dh''dn''ds''ef''en''eo''er'
```

```
276 ad ar az b7 cf cm ct cw cy dh dn ds ef en eo er 'fh' 'fi' 'fq' 'fr' 'fx' 'gp' 'gq' 'gu' 'gx' 'h8' 'hf' 'hj' 'hk' 'ho' 'hw' 'hy' 'i3 ' 'i4' 'ik' 'iu' 'iy' 'jj' 'kn' 'l8' 'lb' 'lg' 'lo' 'm7' 'mx' 'nj' 'nt' 'o6' 'ob' ' oh' 'ok' 'ot' 'pr' 'pz' 'q7' 'q8' 'qa' 'qd' 'qg' 'qh' 'qi' 'qn' 'qz' 'r7' 're' 'ri' 'rk' 'ry' 's4' 'sa' 'sd' 'sm' 'sn' 'sp' 'sw' 'sy' 'tf' 'th' 'to' 'tr' 'tv' 'tz' 'u0 ' 'u1' 'u5' 'ue' 'uk' 'uq' 'vb' 'vp' 'vr' 'vu' 'wa' 'wb' 'wg' 'wi' 'wk' 'wm' 'wt' ' ya' 'yj' 'yl' 'z3' 2016-05-13 07:21:22.326724 277 'ak' 'bg' 'bj' 'bn' 'co' 'e6' 'e7' 'ec' 'ek' 'el' 'ew' 'ez' 'fo' 'im' 'jm' 'js' 'lc' 'lh' 'ob' 'oi' 'os' 'ot' 'ou' 'p0' 'pu' 'q0' 'qh' 'ra' 'rc' 'rm' 'rr' 'sd' 'sq ' 'tc' 'tl' 'wj' 'wy' 'x2' 'xw' 'y6' 'yp' 'yv' 'zj' 2016-05-13 08:21:22.326724 278 'al' 'ar' 'cl' 'dl' 'dz' 'ej' 'fj' 'gu' 'i2' 'i6' 'ih' 'jx' 'k9' 'ln' 'ls' 'mf' 'mx' 'oi' 'om' 'pn' 'q4' 'qd' 'qe' 'qg' 'qk' 'qp' 'qr' 'qw' 'qx' 'rr' 'sd' 'sf' 'ub ' 'uh' 'um' 'uu' 'vg' 'w6' 'wj' 'wp' 'ws' 'yn' 'zc' 'zm' 2016-05-13 09:21:22.326724 279 'ab' 'ag' 'aw' 'b4' 'd4' 'ds' 'e1' 'ea' 'eb' 'ee' 'ef' 'eh' 'ek' 'el' 'en' 'eu' 'ex' 'fv' 'fx' 'gi' 'gp' 'gt' 'i3' 'ie' 'jd' 'jk' 'jn' 'kv' 'l7' 'n8' 'ns' 'nx' 'o2 ' 'o3' 'oh' 'os' 'ow' 'p2' 'pr' 'pu' 'q3' 'qd' 'qe' 'qk' 'qq' 'qz' 'r9' 'rb' 'ri' ' rm' 'rr' 'rw' 'ry' 'sc' 'sj' 'sl' 'sx' 'tk' 'tr' 'tw' 'u4' 'ub' 'ud' 'uf' 'uh' 'un' 'uv' 'v6' 'vc' 'vf' 'vi' 'wg' 'wr' 'ws' 'wv' 'x7' 'xf' 'xo' 'y0' 'yi' 'yo' 'yt' 'yy ' 'za' 'zm' 'zu' 'zx' 2016-05-13 10:21:22.326724 280 '1w' '5i' 'a4' 'a6' 'bz' 'de' 'dg' 'dt' 'ed' 'ei' 'ej' 'ey' 'fa' 'ff' 'gg' 'hi' 'hj' 'ho' 'i2' 'ii' 'ij' 'jq' 'jy' 'ka' 'kr' 'kw' 'lv' 'm7' 'nd' 'ot' 'ov' 'oy' 'oz ' 'pe' 'pj' 'qb' 'qj' 'qq' 'qt' 'qv' 'r0' 'r3' 'r4' 'ri' 'rj' 'si' 'ta' 'tc' 'ts' ' tx' 'u3' 'uj' 'ur' 'v6' 'vh' 'w3' 'w6' 'wc' 'wg' 'wq' 'x5' 'xv' 'yb' 'yt' 'yx' 'zl' 2016-05-13 11:21:22.326724 281 'a8' 'ad' 'ai' 'al' 'as' 'av' 'ay' 'az' 'bf' 'bg' 'c6' 'dc' 'dd' 'dz' 'ef' 'eh' 'eu' 'ft' 'g0' 'g4' 'gf' 'gm' 'hq' 'im' 'iw' 'ix' 'j5' 'jj' 'jn' 'jv' 'k1' 'ko' 'ma ' 'n0' 'nw' 'o9' 'om' 'op' 'ox' 'p4' 'pa' 'pe' 'pm' 'ps' 'q2' 'qb' 'qc' 'qf' 'qi' ' ql' 'qu' 'qw' 'qy' 'qz' 'rl' 'rn' 'rs' 'ru' 'se' 'sf' 'sm' 't8' 'tc' 'tg' 'uq' 'uz' 'va' 'vj' 'wa' 'we' 'wg' 'wk' 'wq' 'wu' 'wy' 'xb' 'xo' 'y3' 'ye' 'ym' 'ys' 'yt' 'z8 ' 'zd' 'zo' 2016-05-13 12:21:22.326724 282 '7k' 'et' 'ew' 'ez' 'g9' 'gk' 'he' 'hp' 'ip' 'jp' 'jq' 'jr' 'jv' 'kb' 'kk' 'ku' 'lx' 'o0' 'o3' 'oa' 'or' 'ou' 'q7' 'qa' 'qf' 'qg' 'qh' 'qo' 'ro' 'rx' 'tl' 'us' 'vk ' 'vw' 'wc' 'wp' 'x0' 'xz' 'yg' 'z5' 2016-05-13 13:21:22.326724 283 '1s' 'a0' 'ac' 'aj' 'am' 'ao' 'aw' 'bi' 'bm' 'by' 'ca' 'cu' 'dc' 'di' 'dp' 'e0' 'e9' 'eg' 'eq' 'fh' 'fi' 'gc' 'gi' 'gq' 'gx' 'h4' 'he' 'hk' 'i2' 'ix' 'jc' 'jl' 'jm ' 'k1' 'kf' 'kg' 'kn' 'kq' 'la' 'nj' 'nw' 'o9' 'og' 'p0' 'p6' 'pj' 'pn' 'pp' 'q4' ' qf' 'ql' 'qm' 'qs' 'qt' 'qu' 'qz' 'r5' 'r6' 'ri' 'ro' 'rw' 'sv' 'sx' 't5' 'th' 'tl' 'tp' 'u0' 'ue' 'uf' 'ug' 'un' 'uq' 'vx' 'wd' 'we' 'wg' 'wj' 'wk' 'wp' 'wr' 'ws' 'wt ' 'x2' 'xq' 'xt' 'xw' 'xx' 'ya' 'yk' 'yl' 'yr' 'yt' 'za' 'zh' 2016-05-13 14:21:22.3 26724 284 '4y' '6h' 'a0' 'a6' 'bo' 'bq' 'co' 'cv' 'dv' 'ec' 'ee' 'eh' 'ei' 'en' 'er' 'ew' 'f1' 'fk' 'fq' 'fy' 'ga' 'gj' 'gp' 'gv' 'gx' 'hv' 'i0' 'i5' 'ij' 'ik' 'in' 'kb' 'ks ' 'kw' 'kz' 'la' 'lh' 'lq' 'ls' 'mu' 'nl' 'og' 'oi' 'om' 'pf' 'pu' 'pv' 'q6' 'q9' ' qe' 'qk' 'ql' 'qo' 'qq' 'qu' 'qw' 'r5' 'rb' 'rn' 'rr' 'rt' 's4' 'sc' 'sg' 'si' 'sm' 'sn' 'sp' 'ss' 'tb' 'tc' 'tg' 'tk' 'tm' 'tr' 'tt' 'tu' 'tv' 'u0' 'u3' 'uj' 'un' 'uz ' 'vp' 'w6' 'w8' 'wc' 'we' 'wi' 'wt' 'wx' 'xp' 'xz' 'y0' 'y4' 'z0' 'zj' 'zy' 2016-0 5-13 15:21:22.326724 285 'ad' 'af' 'ar' 'b0' 'bw' 'c4' 'cn' 'do' 'e0' 'e4' 'em' 'eo' 'fn' 'ga' 'gg' 'gy' 'hf' 'ht' 'id' 'ig' 'ik' 'iv' 'j6' 'mi' 'n5' 'ng' 'ob' 'og' 'ou' 'oy' 'p4' 'pd' 'pg ' 'pk' 'po' 'pt' 'pw' 'q3' 'q5' 'qb' 'qr' 'qt' 'r3' 'rc' 'rd' 'rl' 's0' 'sy' 't9' ' tc' 'tm' 'tq' 'ub' 'up' 'uv' 'ux' 'vm' 'vv' 'vw' 'wc' 'wg' 'wk' 'wm' 'x0' 'xp' 'xr' 'xv' 'xx' 'yg' 'ym' 'yw' 2016-05-13 16:21:22.326724 286 '1d' 'a4' 'ai' 'av' 'b9' 'be' 'c9' 'cc' 'cy' 'de' 'ee' 'g8' 'gg' 'gl' 'gs' 'gu' 'hb' 'kl' 'kr' 'ky' 'mi' 'mz' 'nd' 'og' 'op' 'pr' 'q0' 'q5' 'qk' 'qy' 'r4' 'sk' 'sz ' 't1' 't8' 'td' 'tn' 'tx' 'ty' 'tz' 'uc' 'up' 'vq' 'wa' 'ws' 'wv' 'x3' 'yn' 'yq' '
```

```
yy' 'zm' 2016-05-13 17:21:22.326724 287 'a1' 'aj' 'bi' 'cd' 'cw' 'd2' 'e4' 'e9' 'gz' 'ij' 'k1' 'kb' 'kn' 'lw' 'me' 'nj' 'oq' 'p4' 'ph' 'ps' 'q3' 'q4' 'qj' 's7' 'sp' 'sx' 'tc' 'tw' 'v1' 'vj' 'vt' 'w7' 'wa ' 'wb' 'wp' 'y1' 'zc' 2016-05-13 18:21:22.326724 288 'a1' 'a5' 'aw' 'b5' 'cd' 'dz' 'em' 'eq' 'eu' 'fx' 'gk' 'hi' 'hq' 'ju' 'k8' 'kl' 'kw' 'la' 'lk' 'lm' 'm1' 'mj' 'mp' 'nz' 'o6' 'o8' 'oc' 'q0' 'q1' 'qg' 'qh' 'qw' 'rc ' 'rd' 'ro' 'rr' 'sg' 'sy' 'th' 'ti' 'tt' 'uk' 'uo' 'ut' 'vy' 'wg' 'wi' 'x7' 'yr' ' yu' 'yx' 'yz' 'zr' 'zz' 2016-05-13 19:21:22.326724 289 'a2' 'a9' 'ac' 'bw' 'cu' 'dm' 'e8' 'ee' 'ej' 'ep' 'f7' 'fh' 'ga' 'go' 'im' 'it' 'jv' 'kg' 'lb' 'ml' 'oi' 'p5' 'p9' 'pe' 'pf' 'pp' 'qk' 'rg' 'rh' 'sn' 'sv' 't5' 'tj ' 'tk' 'tq' 'ty' 'v6' 'vk' 'w2' 'w5' 'wh' 'wy' 'y7' 'yf' 'zq' 'zt' 2016-05-13 20:21 :22.326724 290 '70' 'e0' 'ep' 'ex' 'hh' 'jn' 'kg' 'nq' 'rg' 'rj' 'uf' 'vs' 'ys' 2016-05-13 21: 21:22.326724 291 '4j' 'af' 'ap' 'bn' 'ch' 'dc' 'df' 'e0' 'ef' 'eg' 'er' 'g3' 'hh' 'hi' 'hw' 'i1' 'if' 'ii' 'in' 'iy' 'l1' 'mx' 'og' 'px' 'q3' 'qc' 'qg' 'qt' 'qy' 'r3' 'r6' 'rd' 'rj ' 'rz' 'sm' 't2' 't4' 'td' 'tj' 'tm' 'tx' 'ty' 'u9' 'uo' 'up' 'v8' 'wv' 'ye' 'zb' ' zc' 'zi' 'zy' 2016-05-13 22:21:22.326724 292 'cy' 'ey' 'gr' 'lq' 'n1' 'pp' 'pq' 'qb' 'qe' 'se' 'wb' 2016-05-13 23:21:22.326724 293 'gn' 'gx' 'hf' 'ji' 'kx' 'nh' 'o6' 'pe' 'q1' 'qt' 'rw' 'sc' 'ss' 'yh' 'zm' 2016 -05-14 00:21:22.326724 294 '2e' '3y' 'ap' 'as' 'bl' 'di' 'dl' 'e9' 'eh' 'er' 'ff' 'fg' 'fh' 'gc' 'gg' 'hp' 'hq' 'i3' 'ih' 'jm' 'kw' 'lc' 'li' 'ls' 'nm' 'ok' 'pc' 'pn' 'q1' 'qf' 'qi' 'qk' 'r0 ' 'rl' 'sp' 'sy' 'sz' 'ta' 'to' 'ts' 'tv' 'uh' 'uk' 'vb' 'wa' 'wg' 'wi' 'wp' 'yl' ' yq' 'yw' 'yy' 2016-05-14 01:21:22.326724 295 'af' 'am' 'az' 'ce' 'ci' 'dd' 'e5' 'eb' 'ee' 'eh' 'fe' 'fj' 'fv' 'ge' 'gl' 'hp' 'hx' 'i5' 'i8' 'ia' 'ig' 'jb' 'jm' 'jv' 'k6' 'kg' 'kv' 'li' 'ls' 'lx' 'm2' 'md' 'mz ' 'o0' 'oe' 'oy' 'pv' 'q5' 'qh' 'qm' 'qo' 'qy' 'rf' 'ri' 'rp' 'rz' 'su' 'tj' 'tz' ' u2' 'uh' 'ur' 'vg' 'we' 'wi' 'xj' 'yb' 'yx' 'yz' 'z0' 2016-05-14 02:21:22.326724 296 '1o' 'ah' 'ap' 'ba' 'bn' 'cs' 'cu' 'd2' 'd8' 'dg' 'dr' 'ed' 'ee' 'er' 'et' 'eu' 'ey' 'ff' 'g1' 'hj' 'i3' 'i5' 'il' 'in' 'jd' 'kd' 'ku' 'lm' 'lv' 'mu' 'nu' 'ok' 'ol ' 'oo' 'ov' 'oy' 'p8' 'pu' 'qb' 'qq' 'qx' 'r5' 'rm' 'rp' 'rv' 'sh' 'sk' 'sl' 'sr' ' tx' 'uy' 'v3' 'vu' 'w3' 'wa' 'wb' 'wv' 'xh' 'xq' 'ys' 'yt' 'yx' 'z2' 'zi' 2016-05-1 4 03:21:22.326724 297 'a2' 'a7' 'aq' 'bv' 'cy' 'd0' 'df' 'dg' 'do' 'ei' 'ek' 'ev' 'ey' 'fg' 'ge' 'gg' 'h4' 'hv' 'im' 'iq' 'ix' 'j4' 'j5' 'jt' 'kv' 'nc' 'o2' 'ou' 'ow' 'ph' 'pz' 'qf' 'qj ' 'qm' 'qo' 'qq' 'qs' 'ra' 'rl' 'rz' 'te' 'tj' 'tp' 'tr' 'ts' 'tx' 'u5' 'ue' 'uj' ' uk' 'uo' 'us' 'v7' 'w2' 'wa' 'wu' 'wv' 'ww' 'wz' 'y2' 'y8' 'yy' 'zg' 2016-05-14 04: 21:22.326724 298 '1n' '2h' 'at' 'ax' 'c0' 'cn' 'dc' 'df' 'dg' 'e1' 'e5' 'ea' 'eq' 'ex' 'ez' 'f7' 'f8' 'fa' 'gt' 'gv' 'gy' 'hb' 'i3' 'i8' 'id' 'iw' 'ix' 'jc' 'jg' 'k0' 'kh' 'ky' 'kz ' 'lj' 'lm' 'lq' 'mj' 'o8' 'og' 'op' 'ow' 'p5' 'p9' 'qc' 'qe' 'qf' 'qg' 'qo' 'qq' ' qv' 'qz' 'rq' 'rt' 'ru' 's2' 's5' 'sf' 'sl' 'sm' 'st' 'sw' 'tc' 'tl' 'ts' 'tz' 'ud' 'ur' 've' 'wd' 'wj' 'wn' 'wq' 'xa' 'xb' 'yf' 'yj' 'yn' 'yt' 'yv' 'zf' 2016-05-14 05 :21:22.326724 299 '4j' 'bi' 'bk' 'c0' 'c5' 'dh' 'dy' 'e8' 'fw' 'g3' 'g8' 'h6' 'hd' 'hn' 'jl' 'kc' 'kj' 'km' 'll' 'lo' 'nh' 'nj' 'nt' 'ob' 'on' 'oq' 'or' 'ox' 'ph' 'qc' 'qj' 'ql' 'qm ' 'qo' 'qu' 'qz' 'sr' 't7' 'tc' 'ug' 'uq' 'wn' 'wr' 'ws' 'yv' 'z3' 'zj' 'zz' 2016-0 5-14 06:21:22.326724 300 'ab' 'ap' 'ay' 'b6' 'bg' 'bm' 'bq' 'br' 'ce' 'co' 'dt' 'e4' 'ef' 'ej' 'ek' 'ep' 'fj' 'fq' 'fu' 'g3' 'gg' 'gp' 'hk' 'i3' 'i9' 'je' 'k7' 'ku' 'li' 'lq' 'lt' 'lx' 'mc ' 'mz' 'n7' 'nl' 'o1' 'of' 'os' 'pm' 'qc' 'ql' 'qs' 'qw' 'r6' 'rf' 'rj' 'rp' 'ru' ' rx' 'rz' 'tl' 'tw' 'ty' 'u1' 'u3' 'ud' 'un' 'uw' 'vu' 'w6' 'wf' 'wl' 'wq' 'xh' 'xm'
```

```
'yc' 'yh' 'yr' 'yw' 'z9' 2016-05-14 07:21:22.326724 301 '1b' 'cp' 'di' 'ed' 'fv' 'gx' 'hs' 'i8' 'lh' 'lq' 'lz' 'p7' 'p8' 'pc' 'ql' 'qn' 'qw' 're' 'rg' 'tv' 'we' 'wp' 'yr' 'zj' 2016-05-14 08:21:22.326724 302 'h7' 'in' 'is' 'o7' 'q0' 'qa' 'qq' 'rl' 'rs' 'tu' 'u9' 'v3' 'vr' 'yq' 'zy' 2016 -05-14 09:21:22.326724 303 '6w' 'af' 'ak' 'b7' 'bf' 'bi' 'bv' 'cx' 'dy' 'es' 'ey' 'ez' 'f0' 'fe' 'fw' 'ge' 'gt' 'iw' 'j9' 'jh' 'kh' 'l0' 'l1' 'l8' 'm5' 'nv' 'o6' 'pw' 'qi' 'r0' 'se' 'ta' 'tf ' 'th' 'to' 'u8' 'ux' 'vm' 'w4' 'w6' 'wa' 'wt' 'wu' 'xo' 'xu' 'yo' 'z0' 'zc' 2016-0 5-14 10:21:22.326724 304 '6q' 'ac' 'ag' 'av' 'aw' 'az' 'bj' 'bq' 'bx' 'cj' 'dc' 'dd' 'dq' 'eg' 'ei' 'ek' 'em' 'f7' 'fg' 'fq' 'fx' 'gb' 'gp' 'hb' 'hk' 'i9' 'ii' 'im' 'ip' 'ir' 'iz' 'jx' 'le ' 'lf' 'll' 'lx' 'mp' 'mv' 'of' 'oq' 'pb' 'pg' 'pj' 'py' 'pz' 'qi' 'qk' 'ql' 'qs' ' qu' 'qw' 'r8' 'ra' 'rc' 'rj' 'sj' 'tg' 'tk' 'tl' 'tm' 'tp' 'tw' 'u4' 'uf' 'ui' 'um' 'vu' 'w7' 'wd' 'wn' 'wt' 'wy' 'wz' 'y1' 'y3' 'y9' 'yl' 'yo' 'yq' 'yu' 'zb' 'zu' 'zv ' 2016-05-14 11:21:22.326724 305 '6h' '7f' 'ab' 'aq' 'ax' 'bc' 'bl' 'ce' 'cm' 'dn' 'do' 'e1' 'ec' 'ed' 'en' 'fc' 'fl' 'g1' 'ga' 'ge' 'gn' 'h8' 'i0' 'id' 'iq' 'iw' 'jc' 'ji' 'lt' 'mj' 'nm' 'o0' 'o6 ' 'oo' 'pa' 'pb' 'pt' 'q6' 'qf' 'qg' 'qz' 'r1' 'r2' 'r8' 'rd' 'rf' 's9' 'se' 't8' ' tc' 'te' 'u3' 'u5' 'uc' 'ug' 'ul' 'us' 'uu' 'v2' 'vz' 'wp' 'x8' 'ye' 'yq' 'yw' 2016 -05-14 12:21:22.326724 306 '5k' 'a1' 'ab' 'an' 'ar' 'as' 'av' 'ax' 'br' 'c2' 'c7' 'd5' 'da' 'dl' 'dr' 'dz' 'e3' 'ec' 'ed' 'ek' 'el' 'em' 'eu' 'ew' 'fd' 'ff' 'fw' 'g8' 'gb' 'gl' 'hh' 'hs' 'hz ' 'i6' 'ia' 'ig' 'ii' 'ik' 'iq' 'ix' 'j0' 'j9' 'jf' 'jl' 'jo' 'jw' 'ko' 'kt' 'lm' ' nl' 'nm' 'ov' 'p3' 'p6' 'p7' 'pg' 'pl' 'pn' 'pp' 'qd' 'qe' 'qf' 'qn' 'qo' 'qq' 'qs' 'qt' 'qv' 'r9' 'rf' 'rj' 'rt' 'rw' 'sa' 'sl' 't2' 'tg' 'tk' 'tq' 'ty' 'ua' 'ud' 'vi ' 'vm' 'w2' 'w6' 'wb' 'wd' 'wf' 'wi' 'wl' 'wq' 'wr' 'wy' 'x5' 'x8' 'y0' 'y1' 'ys' ' yx' 2016-05-14 13:21:22.326724 307 'a3' 'a4' 'a5' 'bd' 'co' 'cq' 'd8' 'da' 'dn' 'do' 'du' 'dv' 'ed' 'ei' 'en' 'eo' 'es' 'et' 'f1' 'fa' 'ha' 'hr' 'i6' 'id' 'ie' 'if' 'ir' 'jx' 'kd' 'kh' 'mb' 'mq' 'mv ' 'o6' 'oa' 'or' 'oy' 'pl' 'pr' 'q3' 'q8' 'qa' 'qb' 'qc' 'qd' 'qk' 'qs' 'ra' 'rc' ' rp' 'rz' 'se' 'tg' 'tj' 'u2' 'uq' 'uv' 'uy' 'vm' 'vz' 'wh' 'wu' 'xf' 'xs' 'yc' 'ye' 'yl' 'yn' 'z1' 'zf' 2016-05-14 14:21:22.326724 308 'a3' 'ch' 'cs' 'e1' 'gq' 'gx' 'lz' 'nh' 'os' 'po' 'qs' 'rr' 'tx' 'ud' 'uj' 'uv' 've' 'w0' 'wj' 'xo' 'xz' 2016-05-14 15:21:22.326724 309 'ab' 'ad' 'al' 'cm' 'cw' 'dh' 'dn' 'dy' 'e8' 'ea' 'ed' 'ej' 'eq' 'er' 'eu' 'ev' 'f5' 'fb' 'fj' 'fr' 'gc' 'gp' 'h2' 'h6' 'hc' 'hw' 'i3' 'i5' 'id' 'ir' 'ix' 'ka' 'kj ' 'ko' 'lv' 'lx' 'mj' 'mv' 'nq' 'ns' 'oa' 'od' 'ok' 'om' 'os' 'p1' 'p5' 'pb' 'pg' ' pj' 'pl' 'ps' 'pu' 'q1' 'qb' 'qd' 'qe' 'qj' 'qk' 'ql' 'qr' 'qs' 'rd' 'rl' 'ro' 'rs' 'rx' 's1' 'sf' 'sg' 't0' 'tb' 'te' 'tf' 'tg' 'tl' 'tp' 'tq' 'u3' 'uf' 'ug' 'up' 'uq ' 'vx' 'vy' 'w5' 'wa' 'wc' 'wr' 'ws' 'wu' 'wx' 'wy' 'wz' 'yf' 'ym' 'yz' 'ze' 'zs' ' zy' 'zz' 2016-05-14 16:21:22.326724 310 '4f' 'e4' 'ep' 'fa' 'ff' 'iv' 'j4' 'kw' 'oj' 'pa' 'pw' 'q0' 'rv' 'ry' 't3' 'ul' 'vq' 'w1' 'wj' 'xm' 'ye' 'yu' 2016-05-14 17:21:22.326724 311 'di' 'ec' 'i4' 'iq' 'iw' 'ko' 'l3' 'mw' 'py' 'qo' 'rx' 'wt' 'yl' 2016-05-14 18: 21:22.326724 312 '1q' '2n' '4p' '8n' 'a3' 'aa' 'bn' 'bq' 'bu' 'cg' 'db' 'dl' 'dx' 'dy' 'e2' 'e3' 'e4' 'ea' 'eq' 'ff' 'fk' 'fn' 'fv' 'gf' 'gh' 'h1' 'hs' 'hu' 'ij' 'in' 'iv' 'kc' 'ke ' 'ln' 'm2' 'mc' 'mf' 'o2' 'og' 'oo' 'ov' 'p8' 'pl' 'pm' 'ps' 'pv' 'pz' 'qa' 'qc' ' qe' 'qh' 'qi' 'qj' 'qm' 'qo' 'qq' 'qv' 'qw' 'qy' 're' 'rz' 'sd' 'si' 'sj' 'sp' 'su' 'tc' 'tk' 'tn' 'tq' 'u7' 'ut' 'uv' 'v5' 'vr' 'wb' 'we' 'wm' 'ws' 'wv' 'xc' 'xy' 'y9 ' 'yj' 'yq' 'yv' 'yw' 'zb' 'zw' 'zz' 2016-05-14 19:21:22.326724 313 '2a' '5d' 'ag' 'ar' 'at' 'dc' 'fa' 'fh' 'gn' 'gx' 'hh' 'iy' 'kd' 'ke' 'ld' 'nd' 'nx' 'oz' 'qc' 'qd' 'qo' 'qp' 'qu' 'r0' 'rg' 't5' 'tc' 'tg' 'th' 'tk' 'w2' 'w5' 'wt ' 'yl' 'zn' 2016-05-14 20:21:22.326724
```

```
314 '30' 'cl' 'dl' 'e7' 'ee' 'ef' 'eh' 'el' 'fk' 'fn' 'fs' 'gi' 'gw' 'i2' 'il' 'l7' 'm6' 'm9' 'mf' 'o8' 'ob' 'ok' 'pc' 'pe' 'qb' 'qe' 'qn' 'qr' 'tu' 'uc' 'ud' 'wp' 'xq ' 'ym' 'ys' 2016-05-14 21:21:22.326724 315 'a7' 'ad' 'aq' 'ck' 'cu' 'd8' 'db' 'do' 'dt' 'e7' 'eg' 'em' 'eq' 'ex' 'ez' 'fl' 'gr' 'h4' 'hd' 'he' 'hg' 'id' 'ie' 'if' 'in' 'io' 'j4' 'j7' 'je' 'jm' 'jo' 'k5' 'kg ' 'kj' 'kn' 'l9' 'lb' 'lc' 'ld' 'lf' 'li' 'lj' 'na' 'nz' 'oa' 'ok' 'oo' 'pj' 'px' ' q3' 'q4' 'q6' 'qd' 'qi' 'qm' 'qq' 'qt' 'qx' 'r1' 'rg' 'ri' 'rn' 'sm' 'so' 'su' 'sy' 'tq' 'u5' 'uc' 'ue' 'us' 'w3' 'wc' 'we' 'wj' 'wk' 'wt' 'x8' 'xj' 'yc' 'yy' 2016-05- 14 22:21:22.326724 316 'a1' 'ab' 'ad' 'ag' 'bd' 'bf' 'bo' 'bt' 'cl' 'cn' 'cq' 'cz' 'd4' 'db' 'dc' 'dk' 'dn' 'dq' 'ea' 'el' 'em' 'ev' 'ew' 'ex' 'fr' 'ft' 'ga' 'gc' 'gd' 'gg' 'gl' 'gp' 'hp ' 'hu' 'id' 'ij' 'jn' 'kl' 'kt' 'lh' 'lk' 'lm' 'mi' 'mw' 'n4' 'nk' 'oj' 'ok' 'on' ' ph' 'pk' 'pt' 'q0' 'q8' 'qa' 'qe' 'qf' 'qg' 'qh' 'qi' 'qr' 'qt' 'qv' 'qw' 'qx' 'rd' 're' 'rg' 'rq' 'rr' 'sb' 'sg' 'te' 'tj' 'us' 'w5' 'w9' 'wb' 'wf' 'wh' 'wp' 'wq' 'ws ' 'wt' 'wu' 'wv' 'y7' 'yb' 'ye' 'yf' 'yq' 'yu' 'yy' 'yz' 'zx' 2016-05-14 23:21:22.3 26724 317 'ad' 'am' 'av' 'ax' 'dl' 'dt' 'dw' 'ej' 'ez' 'f6' 'fe' 'g5' 'ga' 'gv' 'hr' 'hx' 'id' 'ie' 'ii' 'im' 'ix' 'jd' 'kn' 'ml' 'nu' 'ol' 'oo' 'pu' 'qd' 'qm' 'qt' 'r5' 'rb ' 'rd' 'rg' 'ru' 'sg' 'ub' 'uk' 'vm' 'wl' 'wr' 'wz' 'x4' 'yf' 'yu' 'yv' 'yw' 'yx' ' zt' 2016-05-15 00:21:22.326724 318 'aa' 'af' 'bp' 'c2' 'cd' 'ci' 'dl' 'du' 'dz' 'es' 'fn' 'fo' 'g7' 'ga' 'gc' 'gj' 'gx' 'hc' 'ht' 'iu' 'jl' 'jm' 'ke' 'kk' 'kr' 'lc' 'le' 'lr' 'lw' 'ms' 'n2' 'nq' 'nw ' 'nz' 'o1' 'op' 'oq' 'ot' 'ow' 'p0' 'pb' 'pp' 'pr' 'qc' 'qh' 'qp' 'qr' 'qu' 'qy' ' r3' 'r9' 'rc' 'rk' 'rr' 'ry' 'sb' 'sf' 'sk' 'sl' 't1' 'ta' 'tb' 'tk' 'tz' 'ud' 'ur' 've' 'vn' 'vt' 'vw' 'w6' 'w9' 'wg' 'wk' 'xg' 'yg' 'yh' 'yj' 'ys' 'yt' 'yv' 'yy' 'z3 ' 'zo' 'zq' 2016-05-15 01:21:22.326724 319 '4m' 'at' 'be' 'bo' 'bz' 'cv' 'd0' 'd8' 'ea' 'ec' 'ed' 'ex' 'f9' 'ff' 'fk' 'fv' 'gc' 'ge' 'i8' 'ij' 'is' 'k4' 'k6' 'mw' 'ob' 'ov' 'oy' 'pv' 'q1' 'q2' 'q9' 'qc' 'ql ' 'r4' 'rn' 'ru' 'rx' 'ry' 'sj' 'tg' 'ts' 'tv' 'uj' 'vf' 'vh' 'w4' 'wc' 'ww' 'x5' ' xf' 'xx' 'y5' 'yg' 'yy' 'zg' 'zn' 'zw' 2016-05-15 02:21:22.326724 320 'ew' 'fi' 'g2' 'ku' 'od' 'pk' 'tm' 'tq' 'tu' 'uf' 'wn' 'y1' 2016-05-15 03:21:22 .326724 321 '2e' '3u' 'aa' 'an' 'ap' 'bc' 'br' 'bx' 'cc' 'dt' 'ea' 'ei' 'ej' 'em' 'eo' 'ep' 'eq' 'es' 'et' 'ey' 'fb' 'fw' 'gh' 'gs' 'gv' 'hd' 'hg' 'hn' 'i7' 'it' 'jf' 'ka' 'kl ' 'l8' 'la' 'm0' 'nu' 'o2' 'oc' 'oy' 'ph' 'po' 'pz' 'q2' 'qg' 'qh' 'qn' 'qp' 'qt' ' r7' 'r8' 'rd' 'rf' 'rj' 'rk' 'sm' 't1' 'tb' 'th' 'ub' 'ui' 'ul' 'um' 'uu' 've' 'w8' 'wj' 'wx' 'y8' 'zf' 'zn' 2016-05-15 04:21:22.326724 322 'as' 'b1' 'bc' 'br' 'cd' 'dw' 'e2' 'ec' 'ew' 'f1' 'f2' 'f6' 'g0' 'gi' 'gy' 'hf' 'hk' 'if' 'ii' 'is' 'iy' 'j2' 'jp' 'kl' 'ku' 'l4' 'lg' 'lp' 'lv' 'lw' 'nd' 'ng' 'oo ' 'q4' 'q6' 'q9' 'qc' 'qh' 'ql' 'qm' 'qo' 'qx' 'qz' 're' 'ro' 'sm' 't5' 'th' 'tt' ' ul' 'um' 'v0' 'vb' 'vf' 'vx' 'w9' 'wc' 'we' 'wp' 'xi' 'xl' 'xt' 'xv' 'y3' 'y6' 'ye' 'yg' 'yq' 'yw' 'yx' 'zs' 'zu' 2016-05-15 05:21:22.326724 323 '15' '72' 'av' 'ba' 'dt' 'ev' 'hd' 'hu' 'jy' 'lo' 'mo' 'mt' 'oe' 'oi' 'pa' 'qc' 'qe' 'qt' 'r1' 'rg' 'ry' 'td' 'tk' 'us' 'wk' 'wq' 'ww' 'wz' 'x7' 'xq' 'y9' 'yx' 'z3 ' 2016-05-15 06:21:22.326724 324 '2b' 'a4' 'aa' 'ay' 'br' 'cf' 'd3' 'dh' 'dw' 'e1' 'e8' 'eg' 'en' 'ep' 'ff' 'fj' 'g2' 'go' 'gq' 'i4' 'i8' 'if' 'jc' 'jj' 'jo' 'k1' 'kk' 'ks' 'la' 'ld' 'lm' 'm4' 'ml ' 'o4' 'oe' 'og' 'os' 'oy' 'pc' 'pd' 'pr' 'px' 'q5' 'q6' 'qd' 'qh' 'qj' 'ql' 'qo' ' qt' 'qu' 'qw' 'rb' 're' 'rk' 'rn' 'rr' 'rw' 'sl' 'sm' 'te' 'tf' 'tk' 'u6' 'ui' 'ul' 'uo' 'ur' 'us' 'va' 'vt' 'w7' 'wf' 'wg' 'wm' 'wn' 'ws' 'xo' 'y8' 'yj' 'zh' 2016-05- 15 07:21:22.326724 325 'a1' 'a6' 'aq' 'bk' 'bu' 'ch' 'dd' 'dj' 'dx' 'e7' 'ef' 'ei' 'ek' 'el' 'ez' 'fp' 'ft' 'gb' 'go' 'hd' 'hh' 'hj' 'ho' 'hs' 'ic' 'il' 'ip' 'jh' 'jn' 'jq' 'jx' 'kq' 'kv ' 'la' 'm8' 'mv' 'ng' 'oh' 'or' 'p7' 'p9' 'pe' 'pk' 'px' 'q7' 'qc' 'qd' 'qh' 'qj' ' qk''qr''q''rd''rl''rq''sl''sq''st''s''th''tn''9''c''d''g''
```

`'`

```
qk' 'qr' 'qx' 'rd' 'rl' 'rq' 'sl' 'sq' 'st' 'sy' 'th' 'tn' 'u9' 'uc' 'ud' 'ug' 'uy' 'uz' 'vl' 'vn' 'wa' 'wb' 'wd' 'wt' 'xi' 'xs' 'xz' 'y5' 'yi' 'yk' 'yt' 'yw' 'z7' 'zg ' 2016-05-15 08:21:22.326724 326 '2j' 'ai' 'al' 'ch' 'dy' 'dz' 'ed' 'ei' 'fg' 'fk' 'gp' 'i0' 'il' 'ip' 'iv' 'ix' 'js' 'lm' 'na' 'p1' 'pq' 'pu' 'qe' 'qi' 'qk' 'ql' 'qq' 'qv' 'qx' 'r0' 'rl' 'rm' 'rv ' 'sf' 'sj' 'te' 'tk' 'tq' 'tt' 'tu' 'uc' 'ud' 'um' 'un' 'uq' 'vg' 'vu' 'vz' 'w8' ' wa' 'wf' 'xg' 'yj' 'yw' 'yy' 'z6' 2016-05-15 09:21:22.326724 327 '6w' 'a1' 'aa' 'ab' 'af' 'ao' 'aq' 'ay' 'cd' 'cg' 'dn' 'dp' 'dy' 'e0' 'e6' 'eb' 'ej' 'fh' 'fi' 'fs' 'g0' 'gc' 'gi' 'gs' 'gv' 'gw' 'hd' 'ho' 'i8' 'i9' 'ia' 'ic' 'ie ' 'ik' 'ja' 'jd' 'ji' 'jm' 'k0' 'kj' 'lj' 'm8' 'n0' 'nh' 'nl' 'nn' 'o8' 'of' 'ou' ' oz' 'ph' 'po' 'q0' 'q3' 'q6' 'q7' 'qa' 'qc' 'qd' 'qn' 'qp' 'qq' 'qu' 'qw' 'qz' 'rd' 'rm' 'rn' 'rp' 'rs' 'sj' 'tg' 'tj' 'tr' 'tv' 'u0' 'uf' 'uh' 'uk' 'vv' 'wa' 'wc' 'wf ' 'wg' 'wn' 'wo' 'wp' 'wr' 'ww' 'xt' 'y3' 'y7' 'yc' 'yf' 'yp' 'yy' 2016-05-15 10:21 :22.326724 328 '4p' 'bw' 'cq' 'dk' 'dr' 'dx' 'e3' 'e8' 'ex' 'ez' 'g9' 'h9' 'ih' 'in' 'kt' 'lt' 'me' 'o7' 'od' 'oi' 'on' 'p1' 'pu' 'qa' 'qd' 'qm' 'rz' 'sd' 'tn' 'ua' 'uz' 'vg' 'vx ' 'wx' 'xy' 'ya' 'yl' 'yx' 2016-05-15 11:21:22.326724 329 '1m' '2u' 'ai' 'ap' 'bb' 'bd' 'cb' 'dn' 'fl' 'fm' 'fo' 'fu' 'gi' 'gl' 'gs' 'hg' 'hi' 'hm' 'hp' 'i0' 'if' 'ij' 'jn' 'jt' 'ju' 'k8' 'ld' 'lm' 'oe' 'ox' 'pa' 'q7' 'qe ' 'qi' 'qo' 'qw' 'rf' 'rg' 'ry' 'sq' 't7' 'tk' 'tn' 'tz' 'u5' 'uc' 'v4' 'vr' 'w4' ' w6' 'wd' 'wo' 'ws' 'wt' 'wu' 'wv' 'x3' 'yl' 2016-05-15 12:21:22.326724 330 '25' 'ad' 'ao' 'at' 'ch' 'db' 'dz' 'eq' 'fp' 'gq' 'ih' 'iu' 'jo' 'km' 'p1' 'pb' 'qa' 'qb' 'qc' 'qg' 'ql' 'qq' 'qy' 'rb' 'rf' 'rl' 'rw' 'sp' 'ty' 'uk' 'ur' 'wu' 'wv ' 'yw' 2016-05-15 13:21:22.326724 331 '1a' '3r' 'ai' 'b8' 'bp' 'd6' 'do' 'dp' 'du' 'e0' 'e1' 'ek' 'es' 'eu' 'ey' 'ez' 'fq' 'fs' 'fy' 'gd' 'gm' 'h1' 'hu' 'i0' 'is' 'iv' 'iz' 'jd' 'jn' 'jz' 'kc' 'lf' 'lp ' 'lt' 'ly' 'm2' 'mb' 'mt' 'n1' 'nr' 'of' 'oi' 'oq' 'ow' 'pe' 'pm' 'pn' 'q0' 'qb' ' qg' 'qk' 'qo' 'qz' 'r4' 'r8' 'ra' 'rn' 'rs' 's7' 'sa' 'sj' 'so' 'su' 'sv' 'sx' 'ti' 'tl' 'ts' 'ty' 'u4' 'up' 'vr' 'w2' 'wg' 'wi' 'wk' 'wl' 'ws' 'xl' 'xx' 'yf' 'yk' 'yn ' 'yq' 'yv' 2016-05-15 14:21:22.326724 332 'aa' 'ah' 'bo' 'dz' 'pd' 'pm' 'qf' 'qw' 'rd' 'rn' 'tf' 'wu' 2016-05-15 15:21:22 .326724 333 'ad' 'ao' 'au' 'az' 'ci' 'dj' 'dv' 'e1' 'ei' 'ej' 'em' 'eq' 'fa' 'fi' 'fj' 'fn' 'fw' 'he' 'i8' 'in' 'io' 'jd' 'jt' 'jv' 'lr' 'mt' 'mx' 'ns' 'nt' 'oc' 'oe' 'oi' 'pz ' 'qe' 'ql' 'qt' 'qy' 'rq' 'sc' 'sp' 'te' 'um' 'wo' 'wv' 'x6' 'xu' 'yf' 'yi' 'yo' ' yv' 'yw' 'yz' 'zg' 2016-05-15 16:21:22.326724 334 '13' '6k' 'ae' 'ah' 'an' 'at' 'aw' 'cc' 'cn' 'du' 'dx' 'ek' 'el' 'em' 'en' 'es' 'ey' 'f2' 'fe' 'fh' 'fk' 'fv' 'g6' 'g9' 'gw' 'hj' 'hn' 'hs' 'hu' 'hv' 'ia' 'im' 'iq ' 'ix' 'jh' 'jm' 'ki' 'lj' 'lo' 'lt' 'lw' 'm1' 'nv' 'nw' 'ny' 'oj' 'oo' 'ot' 'ov' ' ox' 'pd' 'pv' 'q1' 'q7' 'qc' 'qd' 'qj' 'ql' 'qp' 'qq' 'qv' 'qw' 'qx' 'r7' 'ry' 'so' 'st' 'su' 'sx' 't9' 'tf' 'th' 'ty' 'uh' 'uo' 'ut' 'uv' 'uy' 'vj' 'vp' 'vu' 'vw' 'w3 ' 'w5' 'w8' 'wc' 'we' 'wg' 'wi' 'wl' 'wv' 'xh' 'xx' 'yb' 'yd' 'yj' 'yn' 'yo' 'yr' ' yy' 'zk' 'zx' 2016-05-15 17:21:22.326724 335 'ad' 'av' 'be' 'bi' 'bk' 'bu' 'ce' 'cv' 'd8' 'df' 'dh' 'du' 'e1' 'em' 'ep' 'ex' 'ey' 'f1' 'fd' 'fh' 'fp' 'gn' 'gu' 'h8' 'i8' 'ii' 'il' 'iz' 'j0' 'ji' 'jv' 'jz' 'k2 ' 'k9' 'ky' 'l9' 'lo' 'm6' 'mc' 'md' 'ng' 'nz' 'ot' 'p2' 'pa' 'pj' 'ps' 'pv' 'q5' ' qd' 'qf' 'qm' 'qq' 'qr' 'qt' 'qv' 'qx' 'rc' 'rh' 'rp' 'rq' 'rs' 'sb' 'sc' 'te' 'to' 'ts' 'tw' 'up' 'vn' 'vw' 'wa' 'wg' 'wh' 'wn' 'wp' 'wz' 'xc' 'xf' 'xt' 'y5' 'yh' 'yn ' 'yy' 'yz' 'za' 'zh' 'zy' 2016-05-15 18:21:22.326724 336 'a1' 'b0' 'd0' 'db' 'ef' 'er' 'ev' 'ew' 'fe' 'fm' 'g8' 'la' 'n5' 'oh' 'os' 'pk' 'pn' 'qq' 'r7' 'sq' 'tw' 'ua' 'uu' 'wa' 'wk' 'wr' 'wu' 'xc' 'yi' 2016-05-15 19:21:2 2.326724 337 '2k' '4s' 'd2' 'dk' 'dm' 'ea' 'ej' 'ep' 'et' 'eu' 'fr' 'gk' 'gs' 'hm' 'iu' 'jq' 'kj' 'km' 'lm' 'nb' 'nr' 'o1' 'oc' 'od' 'of' 'oj' 'ox' 'pf' 'pj' 'px' 'q0' 'q2' 'qa ''qe''qh''qv''r5''r9''rb''rh''ti''tl''tw''u2''vb''vc''vs''xe''xn''
```

```
 qe qh qv r5 r9 rb rh ti tl tw u2 vb vc vs xe xn
y7' 'yb' 'yg' 'yy' 'zb' 'zl' 2016-05-15 20:21:22.326724 338 'a5' 'ae' 'ah' 'as' 'b9' 'bh' 'c5' 'd0' 'dc' 'dd' 'do' 'dp' 'dz' 'eg' 'eh' 'fg' 'fu' 'g3' 'gh' 'gu' 'ha' 'hb' 'hd' 'hg' 'hw' 'i3' 'ib' 'jb' 'je' 'jm' 'js' 'm8' 'ma ' 'n4' 'nu' 'nz' 'ob' 'oy' 'qu' 'qz' 'r5' 'rd' 're' 'rr' 'ru' 's5' 'sf' 'sp' 'st' ' tn' 'uz' 'vi' 'vo' 'w9' 'wj' 'wm' 'ws' 'wu' 'wv' 'wy' 'xa' 'xc' 'yl' 'zd' 'zp' 2016 -05-15 21:21:22.326724 339 'gi' 'n3' 'n7' 'om' 'qa' 'r7' 're' 'ug' 'w7' 'wi' 'x4' 'yn' 2016-05-15 22:21:22 .326724 340 'as' 'bb' 'bn' 'ce' 'd4' 'dp' 'ez' 'gu' 'gw' 'hd' 'hp' 'ia' 'ih' 'ij' 'j6' 'jm' 'jz' 'ku' 'kw' 'lh' 'mu' 'nl' 'nu' 'oc' 'pa' 'pm' 'q8' 'qd' 'qg' 'qi' 'qm' 'qn' 'qr ' 'qs' 'qw' 'r9' 're' 'ro' 'ru' 'rv' 'rw' 't1' 't3' 'tm' 'u4' 'uf' 'uw' 'wa' 'wf' ' wk' 'xa' 'xs' 'yg' 'yp' 'ys' 'yu' 'yz' 'z4' 2016-05-15 23:21:22.326724 341 'a3' 'b3' 'bv' 'ck' 'cl' 'cs' 'cv' 'cy' 'dc' 'dl' 'dq' 'dr' 'du' 'eg' 'el' 'en' 'ex' 'fv' 'fx' 'gd' 'gk' 'gu' 'h7' 'ic' 'jf' 'jz' 'lf' 'lq' 'nl' 'nm' 'o6' 'ob' 'ol ' 'pe' 'po' 'q2' 'qa' 'qk' 'qo' 'qp' 'qr' 'qv' 'qz' 'r5' 're' 'rk' 'ss' 'sv' 't2' ' tf' 'ti' 'tj' 'ua' 'ud' 'v8' 'vb' 'vg' 'vh' 'vi' 'w1' 'w5' 'wb' 'wd' 'we' 'wf' 'wj' 'wr' 'ws' 'wv' 'xq' 'xs' 'y1' 'ye' 'yi' 'yp' 'yr' 'ys' 'yu' 'yw' 'z7' 'z8' 'zf' 'zq ' 2016-05-16 00:21:22.326724 342 '1l' '2u' 'ao' 'av' 'bb' 'c7' 'c8' 'ca' 'cm' 'cp' 'dc' 'di' 'e2' 'e4' 'eo' 'er' 'et' 'ex' 'g1' 'gb' 'hi' 'hr' 'ht' 'i9' 'id' 'ie' 'jk' 'jq' 'ju' 'k3' 'k5' 'lb' 'lm ' 'lv' 'mg' 'no' 'o8' 'oo' 'ot' 'p2' 'pn' 'pw' 'py' 'q6' 'qg' 'ql' 'qo' 'r2' 'rf' ' rk' 'rq' 'ry' 't2' 'tb' 'tn' 'tr' 'tw' 'ub' 'w1' 'wa' 'wb' 'we' 'wi' 'ww' 'xo' 'yk' 'ys' 'yx' 'zg' 2016-05-16 01:21:22.326724 343 '4u' 'a2' 'aq' 'as' 'b8' 'bu' 'cc' 'cp' 'cv' 'dg' 'e3' 'e9' 'eh' 'fg' 'fh' 'g9' 'gf' 'gk' 'gx' 'hp' 'il' 'jq' 'kc' 'l4' 'lm' 'mt' 'my' 'nw' 'oq' 'pe' 'qe' 'qu' 'qz ' 'r1' 'rb' 'sh' 'sx' 't5' 'td' 'tl' 'tr' 'vb' 'vd' 'w6' 'wh' 'wk' 'wp' 'wv' 'y0' ' ye' 'yq' 'z2' 'zj' 'zz' 2016-05-16 02:21:22.326724 344 '1l' '2t' '2z' 'af' 'az' 'be' 'br' 'cm' 'cu' 'cy' 'd2' 'd4' 'dd' 'dx' 'ec' 'ed' 'g2' 'gs' 'gu' 'id' 'ig' 'in' 'it' 'jh' 'jl' 'l6' 'ld' 'lg' 'lr' 'ly' 'nf' 'nj' 'ob ' 'ot' 'p4' 'p8' 'pe' 'ph' 'q5' 'qa' 'qd' 'qe' 'qi' 'qo' 'qv' 'qz' 'ra' 'ri' 'rl' ' rr' 's7' 'sj' 'sx' 't0' 'tj' 'to' 'u2' 'ui' 'uq' 'ut' 'uw' 'vg' 'vs' 'w2' 'wa' 'wi' 'wl' 'wr' 'wu' 'ww' 'x7' 'xm' 'ym' 'yn' 'yp' 'zh' 2016-05-16 03:21:22.326724 345 '1x' '2h' '6b' 'ah' 'av' 'ay' 'b9' 'bu' 'bv' 'c6' 'dv' 'e2' 'ea' 'ec' 'fh' 'gk' 'ia' 'j2' 'ji' 'k2' 'kc' 'kg' 'kq' 'kz' 'la' 'mq' 'nb' 'od' 'oe' 'ot' 'p8' 'pm' 'pp ' 'qc' 'qi' 'qr' 'rg' 'rp' 'rw' 'tl' 'u5' 'ub' 'un' 'uv' 'vc' 'vi' 'wc' 'wi' 'wp' ' wv' 'xg' 'xq' 'yq' 'z3' 'zd' 'zv' 'zx' 'zy' 2016-05-16 04:21:22.326724 346 'a2' 'al' 'av' 'b9' 'bd' 'bo' 'c8' 'cq' 'dz' 'ej' 'el' 'ep' 'ew' 'f3' 'f5' 'fr' 'ft' 'h2' 'i3' 'ic' 'id' 'iy' 'jd' 'ke' 'kf' 'kr' 'l3' 'lf' 'mg' 'mu' 'nj' 'o3' 'ob ' 'ol' 'ov' 'pb' 'pj' 'pl' 'pp' 'qn' 'qz' 're' 'rg' 'rk' 'ru' 's3' 'sa' 'sh' 'sj' ' su' 'sw' 'tb' 'tk' 'tv' 'ue' 'uh' 'ul' 'un' 'vk' 'vu' 'w0' 'wa' 'wm' 'wo' 'wq' 'xa' 'xl' 'ya' 'yn' 'yo' 2016-05-16 05:21:22.326724 347 'a5' 'av' 'dc' 'dm' 'dt' 'dw' 'e2' 'ea' 'en' 'et' 'ez' 'f2' 'fg' 'fn' 'fv' 'gn' 'gu' 'h5' 'ht' 'i2' 'ie' 'ik' 'il' 'in' 'it' 'iv' 'iy' 'ji' 'jj' 'ju' 'kf' 'kn' 'ko ' 'ku' 'l6' 'ls' 'nz' 'o2' 'o4' 'of' 'on' 'op' 'p7' 'q0' 'q2' 'qa' 'qt' 'r1' 'r9' ' ri' 'rq' 'rv' 'se' 'sp' 'sx' 't0' 't2' 't9' 'te' 'tq' 'tu' 'u8' 'uc' 'ue' 'ug' 'ui' 'ut' 'uu' 'v0' 'v7' 'vs' 'w0' 'wc' 'wh' 'wn' 'wo' 'ws' 'y1' 'y3' 'y5' 'ya' 'yc' 'yi ' 'ys' 'yt' 'zf' 'zq' 2016-05-16 06:21:22.326724 348 'eq' 'g7' 'jc' 'jf' 'ji' 'lw' 'ma' 'oe' 'p7' 'qb' 'qj' 'qo' 'u7' 'v7' 'w3' 'wd' 'wz' 'xg' 'yr' 2016-05-16 07:21:22.326724 349 'b8' 'eh' 'g5' 'gn' 'jo' 'mx' 'og' 'ol' 'on' 'px' 'rr' 'sl' 'un' 'uz' 'wv' 'yf' 2016-05-16 08:21:22.326724 350 'at' 'bm' 'd0' 'd5' 'eg' 'ei' 'ek' 'eq' 'er' 'eu' 'ez' 'fs' 'gh' 'hc' 'ho' 'ix' 'ko' 'kq' 'l1' 'll' 'mz' 'ob' 'ou' 'p2' 'pi' 'pl' 'ps' 'pt' 'q0' 'q5' 'qa' 'qg' 'qj ' 'qm' 'qq' 'qt' 'rf' 'ri' 'rm' 'ru' 'rv' 'rx' 'ry' 's4' 't4' 'td' 'tn' 'tq' 'tx' '
```

`q` `qq` `q` `y` `q`

```
u3' 'up' 'uq' 'vn' 'wb' 'wf' 'wk' 'wr' 'wv' 'wy' 'xh' 'xx' 'y3' 'yc' 'ye' 'ys' 'za' 'zd' 'zo' 'zs' 'zv' 'zy' 2016-05-16 09:21:22.326724 351 'a0' 'a7' 'ad' 'ae' 'ah' 'ay' 'b8' 'bh' 'dc' 'di' 'do' 'e5' 'ea' 'eb' 'ep' 'ev' 'fn' 'gq' 'gr' 'gs' 'h8' 'hc' 'hj' 'i3' 'ih' 'it' 'iw' 'ja' 'jf' 'kc' 'l8' 'lp' 'lx ' 'ly' 'm1' 'og' 'oy' 'p7' 'pp' 'q7' 'qa' 'qm' 'qq' 'qr' 'qu' 'r3' 'rd' 'rg' 'rj' ' rw' 'si' 'sq' 'ss' 't0' 'tb' 'tg' 'tl' 'to' 'tp' 'tx' 'u9' 'ub' 'um' 'up' 'ux' 'vc' 'w0' 'w2' 'w5' 'wl' 'wy' 'xg' 'yb' 'yg' 'yh' 'za' 2016-05-16 10:21:22.326724 352 '1z' 'aq' 'cf' 'cl' 'e1' 'e5' 'ee' 'eg' 'eo' 'er' 'ff' 'fh' 'fx' 'g5' 'ga' 'gd' 'gm' 'gn' 'hc' 'hf' 'hi' 'hk' 'ho' 'ib' 'ik' 'in' 'iw' 'ix' 'jd' 'kl' 'ky' 'lp' 'm3 ' 'm5' 'n4' 'ng' 'o0' 'oc' 'oj' 'ot' 'ou' 'p2' 'pa' 'pd' 'pg' 'ps' 'pw' 'q1' 'q8' ' qb' 'qc' 'qd' 'qi' 'qr' 'qs' 'qu' 'qv' 'ra' 'rg' 'rt' 'rz' 's7' 'sm' 'sn' 't0' 'tb' 'th' 'tx' 'tz' 'ub' 'ud' 'ue' 'un' 'ur' 'ut' 'vb' 'vj' 'wg' 'wh' 'wj' 'wl' 'wn' 'ww ' 'wz' 'x0' 'xc' 'xq' 'xr' 'xw' 'y8' 'y9' 'yr' 'z7' 'zt' 2016-05-16 11:21:22.326724 353 '2u' '3q' '7p' 'b4' 'b8' 'bb' 'bq' 'bu' 'ce' 'dk' 'dn' 'e0' 'ea' 'ed' 'ef' 'eg' 'eh' 'ej' 'ek' 'em' 'en' 'eo' 'et' 'fh' 'fr' 'fw' 'gj' 'gx' 'ho' 'i7' 'i9' 'if' 'ii ' 'il' 'in' 'iq' 'iw' 'jy' 'k0' 'k1' 'km' 'kr' 'lh' 'lq' 'lw' 'ma' 'mb' 'md' 'mj' ' nh' 'ni' 'nj' 'ob' 'p5' 'p7' 'pc' 'pk' 'pl' 'pu' 'q2' 'qa' 'qc' 'qe' 'qi' 'qm' 'qn' 'qt' 'rb' 'rp' 'rx' 'sd' 't6' 'tb' 'tl' 'tw' 'u5' 'u7' 'ug' 'uh' 'ut' 'vs' 'wi' 'wj ' 'wp' 'ws' 'wu' 'wv' 'xm' 'xs' 'y2' 'y6' 'yd' 'yh' 'yl' 'yr' 'yx' 'yz' 2016-05-16 12:21:22.326724 354 '4c' '4z' 'ag' 'ak' 'an' 'as' 'aw' 'bl' 'd7' 'dy' 'e7' 'eb' 'ec' 'eq' 'et' 'fx' 'gg' 'gm' 'ht' 'hv' 'ik' 'in' 'ip' 'j6' 'k6' 'ka' 'lc' 'md' 'mx' 'n7' 'pw' 'py' 'q7 ' 'qa' 'qg' 'qh' 'qn' 'qo' 'qt' 'ri' 'rl' 'rs' 'sj' 'su' 'tj' 'u0' 'ua' 'w0' 'wh' ' wi' 'wp' 'wr' 'wx' 'wz' 'ys' 'yx' 2016-05-16 13:21:22.326724 355 '3s' '6q' 'ad' 'am' 'as' 'ay' 'cd' 'ci' 'cl' 'dw' 'eb' 'en' 'ep' 'ew' 'ey' 'fh' 'g6' 'gb' 'gk' 'h5' 'hk' 'hp' 'hy' 'i8' 'ia' 'ic' 'ih' 'in' 'is' 'iw' 'jd' 'je' 'kh ' 'kp' 'ks' 'lg' 'lz' 'mx' 'my' 'nf' 'nh' 'no' 'nv' 'o4' 'oa' 'oc' 'op' 'p2' 'p5' ' pa' 'pb' 'pt' 'pw' 'q2' 'q4' 'qb' 'qg' 'qh' 'qq' 'qs' 'qt' 'qx' 'qy' 'qz' 'r7' 'rc' 'rk' 'rt' 'sr' 'sx' 'sy' 'tc' 'tn' 'tr' 'tv' 'u1' 'u7' 'ua' 'uh' 'uz' 'vi' 'wd' 'wr ' 'x3' 'x5' 'xa' 'xe' 'y5' 'y7' 'yb' 'yg' 'yk' 'ym' 'yr' 'yt' 'z7' 'zc' 'zf' 'zj' ' zp' 2016-05-16 14:21:22.326724 356 'aq' 'bo' 'cx' 'dl' 'dm' 'ed' 'ee' 'ei' 'er' 'eu' 'f4' 'fe' 'fw' 'g2' 'gj' 'h7' 'hv' 'im' 'j8' 'jf' 'kl' 'la' 'lj' 'mo' 'oc' 'oh' 'oi' 'ol' 'pa' 'pb' 'pf' 'pk' 'po ' 'q9' 'qf' 'qj' 'qq' 'qv' 'r8' 're' 'rg' 'rh' 'rj' 'rr' 'ru' 'ry' 's8' 'sd' 'sg' ' sj' 'sk' 'so' 'sv' 't3' 'tz' 'u5' 'ua' 'uk' 'um' 'vi' 'vt' 'wb' 'we' 'wk' 'wn' 'wt' 'wu' 'wz' 'xk' 'xz' 'yi' 'yl' 'yz' 'z9' 'zd' 'zu' 'zw' 2016-05-16 15:21:22.326724 357 'a7' 'ah' 'cj' 'co' 'cv' 'dt' 'ex' 'fs' 'gx' 'hn' 'jv' 'kp' 'l5' 'od' 'on' 'pr' 'q6' 'q8' 'qi' 'qq' 'qr' 'rl' 'u2' 'wb' 'wx' 'yh' 'zq' 2016-05-16 16:21:22.326724 358 '18' 'bf' 'bj' 'cs' 'dw' 'el' 'ep' 'ez' 'fr' 'g1' 'gv' 'hu' 'hz' 'ii' 'jc' 'je' 'jj' 'jo' 'jv' 'n5' 'ni' 'ns' 'oh' 'oi' 'ov' 'pe' 'q8' 'qg' 'qi' 'qr' 'r6' 'rh' 's3 ' 'sj' 'sr' 't0' 'ta' 'u2' 'uj' 'ur' 'vu' 'wb' 'wh' 'wx' 'yn' 'yq' 'zg' 'zr' 2016-0 5-16 17:21:22.326724 359 'au' 'bl' 'c4' 'd7' 'dc' 'dm' 'ea' 'eo' 'ft' 'gb' 'h3' 'ia' 'ix' 'jr' 'kc' 'ke' 'lq' 'lr' 'mn' 'op' 'pj' 'qc' 'qj' 'qn' 'qq' 'qx' 'r8' 'rb' 'ri' 'rm' 'rn' 'rx' 't6 ' 'tf' 'tv' 'um' 'vg' 'vi' 'we' 'wp' 'wz' 'x6' 'xb' 'xd' 'xg' 'xv' 'yx' 'yz' 2016-0 5-16 18:21:22.326724 360 '1o' '7o' 'a1' 'aq' 'b4' 'bi' 'bp' 'c9' 'cb' 'cd' 'cf' 'co' 'cp' 'd3' 'd8' 'ds' 'dv' 'dy' 'eb' 'ee' 'ef' 'eh' 'em' 'eo' 'es' 'ez' 'fi' 'fk' 'fl' 'gj' 'gn' 'gt' 'h1 ' 'hn' 'ho' 'hp' 'hu' 'ic' 'ik' 'il' 'im' 'ir' 'iw' 'ji' 'jp' 'k4' 'ks' 'm0' 'ml' ' n0' 'ns' 'oj' 'on' 'or' 'os' 'ov' 'pr' 'pv' 'px' 'py' 'q6' 'qa' 'qc' 'qg' 'qj' 'qm' 'qn' 'qp' 'qq' 'qs' 'qv' 'qz' 'r0' 'ra' 's0' 'te' 'tg' 'tm' 'to' 'tw' 'u1' 'u7' 'ug ' 'um' 'uw' 'ux' 'uz' 'vm' 'vu' 'w4' 'wg' 'wh' 'wj' 'wk' 'wm' 'wo' 'wq' 'ws' 'wt' ' wz' 'x0' 'x5' 'yg' 'yn' 'z6' 2016-05-16 19:21:22.326724 361 '1a' 'a0' 'ab' 'ah' 'ay' 'cd' 'db' 'di' 'eh' 'eo' 'eq' 'f4' 'f8' 'fs' 'gv' 'h7'
```

```
'he' 'hf' 'i0' 'id' 'il' 'io' 'ip' 'kc' 'l1' 'l7' 'lw' 'mp' 'na' 'nb' 'nj' 'oj' 'ou ' 'pa' 'pn' 'ps' 'pu' 'qb' 'qf' 'ql' 'qn' 'qr' 'rn' 'rw' 'so' 'tf' 'tg' 'th' 'tr' ' us' 'w3' 'w6' 'wb' 'wc' 'wf' 'wg' 'wp' 'wr' 'yv' 'yw' 'zh' 2016-05-16 20:21:22.326724 362 '5o' 'ar' 'at' 'az' 'bf' 'bv' 'e0' 'ew' 'fh' 'hd' 'ij' 'in' 'is' 'iu' 'ji' 'l5' 'ld' 'mz' 'nk' 'oc' 'p2' 'ph' 'px' 'q9' 'qi' 'qn' 'qo' 'qq' 'qv' 'rw' 'sf' 'sp' 'te ' 'up' 'y8' 2016-05-16 21:21:22.326724 363 '2s' '3k' '4b' '6s' 'a1' 'b2' 'b9' 'bi' 'bz' 'c0' 'c3' 'ck' 'cl' 'cu' 'de' 'dl' 'do' 'dp' 'e8' 'ec' 'ee' 'ei' 'ek' 'eu' 'ez' 'fi' 'fo' 'fr' 'fu' 'fx' 'gh' 'gk' 'go ' 'gq' 'h4' 'hd' 'hm' 'hz' 'ia' 'id' 'iv' 'jb' 'jh' 'km' 'kp' 'l4' 'l7' 'l8' 'ld' ' lj' 'nb' 'o7' 'oc' 'oh' 'os' 'p4' 'p9' 'pd' 'q6' 'q7' 'q8' 'qc' 'qh' 'qj' 'qk' 'qw' 'rg' 'rj' 'rm' 'rn' 'rp' 'ru' 'rz' 's5' 'si' 'sv' 'sy' 'tc' 'tg' 'tk' 'tv' 'ue' 'uf ' 'ux' 'uz' 'vl' 'w2' 'w6' 'wf' 'wm' 'wu' 'wx' 'xh' 'ya' 'yc' 'ye' 'z7' 'zi' 'zo' ' zq' 2016-05-16 22:21:22.326724 364 'ap' 'aw' 'ba' 'cz' 'dw' 'eh' 'g5' 'g9' 'gc' 'gi' 'go' 'ir' 'j8' 'kl' 'mg' 'p6' 'ql' 'qu' 'qz' 'sa' 't7' 'tw' 'v5' 'v7' 'wj' 'xt' 'y6' 'yg' 'yh' 'yq' 'z5' 'zj' 201 6-05-16 23:21:22.326724 365 'a9' 'ad' 'az' 'bo' 'bq' 'by' 'c8' 'cb' 'cp' 'd9' 'de' 'dj' 'dp' 'e4' 'ef' 'ey' 'fn' 'gc' 'ge' 'gp' 'gs' 'gu' 'gx' 'hf' 'ic' 'ie' 'ir' 'kc' 'kp' 'ku' 'l2' 'lv' 'mx ' 'n7' 'o3' 'o7' 'oe' 'pb' 'ps' 'q3' 'q4' 'qb' 'qn' 'qo' 'qq' 'qu' 'qw' 'r3' 'ra' ' rk' 'sg' 'si' 'sv' 'sw' 'tb' 'tg' 'tw' 'u2' 'uc' 'uf' 'uj' 'us' 'ut' 'uu' 'v3' 'va' 'wa' 'wd' 'ww' 'wy' 'wz' 'xk' 'y6' 'y8' 'ya' 'yc' 'ye' 'yo' 'yx' 'z3' 2016-05-17 00 :21:22.326724 366 'a8' 'am' 'as' 'bb' 'cn' 'co' 'dd' 'di' 'dx' 'dz' 'e3' 'e5' 'ea' 'ef' 'eh' 'el' 'en' 'eo' 'ew' 'fe' 'fg' 'gc' 'gi' 'gj' 'gp' 'ha' 'hl' 'hy' 'i3' 'id' 'ij' 'ir' 'is ' 'k9' 'kc' 'kf' 'l9' 'ln' 'ls' 'lw' 'm0' 'm8' 'my' 'nn' 'on' 'p9' 'ph' 'pm' 'pw' ' q1' 'q3' 'qc' 'qm' 'qq' 'qv' 'rg' 'ro' 'se' 'sw' 'sx' 'ta' 'tl' 'tz' 'u4' 'uo' 'vg' 'vl' 'vm' 'vn' 'w3' 'wd' 'wm' 'wo' 'wp' 'wt' 'yg' 'yj' 'yv' 'yx' 'yz' 'zu' 'zx' 'zy ' 2016-05-17 01:21:22.326724 367 '1u' 'ad' 'al' 'c4' 'cz' 'db' 'dk' 'dr' 'e5' 'e7' 'ea' 'f6' 'fk' 'fw' 'g3' 'gl' 'gt' 'gu' 'ha' 'hk' 'hv' 'ie' 'ka' 'kq' 'ks' 'lr' 'nf' 'pk' 'q3' 'q8' 'qf' 'qj' 'qo ' 'rp' 'rr' 'rz' 'ss' 'sv' 'sx' 'tb' 'th' 'tt' 'ur' 'vp' 'wj' 'ws' 'wt' 'xk' 'xo' ' ym' 'yz' 2016-05-17 02:21:22.326724 368 '3t' '5u' 'aa' 'ab' 'b9' 'd8' 'di' 'dj' 'dq' 'dx' 'dy' 'ea' 'ek' 'el' 'es' 'ev' 'ey' 'ez' 'fk' 'fp' 'g3' 'gb' 'gd' 'gg' 'gi' 'go' 'hj' 'hz' 'i3' 'i5' 'in' 'io' 'is ' 'jv' 'kb' 'kr' 'lu' 'md' 'nd' 'ny' 'o6' 'oe' 'ok' 'ow' 'ox' 'p4' 'p7' 'p8' 'pb' ' pu' 'q1' 'q3' 'q4' 'qd' 'qj' 'qk' 'qq' 'qx' 'qy' 'r6' 'ro' 'rw' 'rx' 'ry' 'se' 'sp' 't0' 't1' 'th' 'tl' 'tn' 'tp' 'tr' 'tx' 'u5' 'uf' 'uo' 'ux' 'vc' 'vz' 'w2' 'w5' 'wa ' 'wb' 'we' 'wi' 'wj' 'ws' 'wt' 'xh' 'y1' 'yb' 'yg' 'yi' 'zd' 'zm' 'zt' 2016-05-17 03:21:22.326724 369 '2s' '4q' '8x' 'aa' 'ac' 'ah' 'av' 'aw' 'c4' 'c5' 'ce' 'd1' 'dj' 'dq' 'e7' 'e9' 'ea' 'ef' 'fc' 'fs' 'fz' 'gb' 'ge' 'gx' 'hf' 'hl' 'hm' 'i5' 'i7' 'ie' 'ii' 'iw' 'kf ' 'ko' 'kx' 'lb' 'm6' 'mh' 'ob' 'od' 'oe' 'og' 'oq' 'or' 'pn' 'ps' 'pu' 'q4' 'qf' ' qg' 'qj' 'ql' 'qn' 'qt' 'qy' 'r3' 'ra' 'ri' 'rj' 'rv' 'sr' 'tg' 'th' 'tl' 'tx' 'u7' 'ub' 'uh' 'uq' 'uu' 'uy' 'vn' 'vt' 'wa' 'we' 'wh' 'wn' 'wp' 'wr' 'ww' 'xg' 'xk' 'xs ' 'ya' 'yc' 'yd' 'yf' 'yl' 'ym' 'ys' 'z6' 'zj' 'zm' 'zv' 'zw' 2016-05-17 04:21:22.3 26724 370 '2y' '8i' 'by' 'dl' 'h6' 'hj' 'm3' 'ml' 'qa' 'qx' 'r1' 'rm' 'rn' 'u4' 'uj' 'wo' 'xv' 2016-05-17 05:21:22.326724 371 '2h' '9y' 'ac' 'at' 'cf' 'e3' 'e6' 'ec' 'ek' 'en' 'f1' 'fa' 'fn' 'gm' 'gx' 'hk' 'i7' 'id' 'iw' 'ke' 'kl' 'ks' 'l6' 'l8' 'ls' 'lx' 'me' 'o4' 'oi' 'oj' 'ox' 'pn' 'qa ' 'qh' 'qk' 'ql' 'rp' 'tb' 'te' 'tn' 'ts' 'u4' 'u9' 'ud' 'vj' 'vz' 'wc' 'wr' 'ye' ' yk' 'yq' 'zq' 2016-05-17 06:21:22.326724 372 '5t' 'al' 'av' 'ax' 'by' 'cr' 'cx' 'df' 'dh' 'dp' 'dq' 'e4' 'e7' 'en' 'ff' 'fg'
```

```
'fo' 'g4' 'ge' 'gg' 'gm' 'gr' 'gt' 'hc' 'hn' 'hq' 'hs' 'i0' 'i1' 'id' 'ig' 'im' 'jb ' 'jv' 'k9' 'kl' 'km' 'lh' 'lp' 'lq' 'mm' 'ne' 'nk' 'nu' 'od' 'os' 'pj' 'pw' 'pz' ' q0' 'q1' 'qa' 'qd' 'qe' 'qf' 'qk' 'ql' 'qn' 'qp' 'qt' 'r0' 'rx' 'sx' 'sy' 't0' 't1' 't8' 'th' 'ti' 'tp' 'tv' 'tz' 'ub' 'uc' 'ul' 'v5' 'vp' 'vu' 'w8' 'wd' 'we' 'wf' 'wh ' 'wm' 'wq' 'wr' 'ws' 'wy' 'wz' 'xg' 'y9' 'yg' 'yh' 'yq' 'yz' 'z0' 2016-05-17 07:21 :22.326724 373 'bf' 'cf' 'cg' 'cj' 'ef' 'ej' 'ek' 'ep' 'fk' 'gi' 'ik' 'ir' 'j0' 'km' 'ko' 'lu' 'mr' 'n6' 'oc' 'op' 'pt' 'q4' 'qe' 'qk' 'qv' 'rc' 'rt' 's8' 't3' 'tk' 'ut' 'wc' 'we ' 'ws' 'wt' 'ww' 'y8' 'yd' 'yr' 2016-05-17 08:21:22.326724 374 'a6' 'ad' 'ak' 'ap' 'd1' 'de' 'dj' 'eb' 'eg' 'fi' 'fq' 'ft' 'gx' 'gy' 'hn' 'hs' 'i4' 'ia' 'im' 'is' 'kf' 'ko' 'kt' 'l0' 'lr' 'm8' 'mv' 'oi' 'on' 'pc' 'pl' 'pn' 'pp ' 'q2' 'q4' 'qj' 'ql' 'qv' 'qy' 'r2' 'rc' 'rd' 're' 'rm' 'rt' 'sj' 'tb' 'tc' 'tf' ' tk' 'uf' 'uk' 'ul' 'um' 'uq' 'uy' 'vj' 'wl' 'wv' 'ww' 'x7' 'xj' 'y7' 'yx' 'zb' 2016 -05-17 09:21:22.326724 375 '5f' 'ac' 'ad' 'aj' 'av' 'bg' 'ch' 'ci' 'dg' 'di' 'dl' 'dx' 'ep' 'ew' 'f8' 'fp' 'fr' 'fs' 'g4' 'g6' 'gb' 'h5' 'he' 'hk' 'hx' 'i1' 'ic' 'im' 'ji' 'jm' 'js' 'k9' 'kq ' 'lf' 'ln' 'mj' 'n2' 'ni' 'no' 'o5' 'oi' 'ot' 'oy' 'pa' 'pj' 'qk' 'qq' 'qt' 'qu' ' r4' 'r8' 'rb' 'rh' 'rj' 'rm' 'ro' 'rp' 'rq' 'rt' 'ru' 'sb' 'th' 'tu' 'tz' 'u9' 'un' 'uo' 'us' 've' 'vi' 'vq' 'vx' 'wf' 'wg' 'wi' 'wq' 'wr' 'wt' 'x5' 'xz' 'y6' 'yd' 'yo ' 'yq' 'yx' 'z3' 'zl' 2016-05-17 10:21:22.326724 376 'a3' 'do' 'ef' 'hp' 'ih' 'im' 'jp' 'km' 'lv' 'mt' 'nh' 'oc' 'od' 'ph' 'pi' 'pj' 'qe' 'qh' 'qr' 'rq' 'rr' 'rs' 'sc' 'st' 'ts' 'tt' 'tw' 'ut' 'vv' 'w7' 'wv' 'x3' 'xa ' 'xc' 'xl' 'zc' 2016-05-17 11:21:22.326724 377 '2o' '6t' 'a7' 'bv' 'di' 'dm' 'ea' 'eo' 'fd' 'fj' 'ft' 'fw' 'gs' 'hu' 'hz' 'ik' 'it' 'jc' 'js' 'jx' 'jz' 'k4' 'lp' 'lx' 'ol' 'p3' 'pf' 'q9' 'qu' 'qv' 'qx' 're' 'rl ' 'ro' 'sb' 'ur' 'vf' 'wd' 'wk' 'wo' 'wx' 'yp' 'zo' 2016-05-17 12:21:22.326724 378 '7u' '7z' 'a0' 'a5' 'c6' 'cj' 'cx' 'do' 'e4' 'eg' 'eh' 'eq' 'ey' 'ez' 'fe' 'fu' 'gk' 'gy' 'h9' 'ih' 'ik' 'il' 'j0' 'jt' 'jy' 'k1' 'k5' 'ke' 'lp' 'lx' 'ly' 'ma' 'mj ' 'mm' 'mt' 'nb' 'nm' 'o3' 'o5' 'of' 'oi' 'ov' 'p2' 'pf' 'ph' 'pt' 'q8' 'qj' 'qk' ' qp' 'qs' 'r1' 'r8' 'rl' 'rp' 'rt' 's5' 'sb' 'sh' 'sk' 'so' 'sr' 'su' 'tc' 'tn' 'tr' 'tx' 'u4' 'uh' 'ul' 'up' 'ur' 'uw' 'uy' 'vm' 'w5' 'wb' 'wj' 'wm' 'wq' 'wy' 'x6' 'xq ' 'xs' 'y8' 'y9' 'yi' 'yj' 'yv' 'yx' 'zi' 'zy' 2016-05-17 13:21:22.326724 379 '2n' 'ar' 'b3' 'bc' 'bd' 'c0' 'c9' 'cb' 'cp' 'do' 'ee' 'eh' 'ep' 'f3' 'fb' 'fj' 'gg' 'gk' 'gm' 'h9' 'hk' 'hp' 'ht' 'i7' 'ij' 'iw' 'kx' 'm2' 'mt' 'mv' 'nj' 'ns' 'o7 ' 'oa' 'od' 'of' 'om' 'or' 'pg' 'pm' 'pu' 'qq' 'qw' 'qx' 'r0' 'rb' 'rg' 'rk' 'rv' ' se' 'sj' 'sp' 'su' 'tf' 'uu' 'v9' 've' 'vg' 'vm' 'w5' 'w6' 'w8' 'wa' 'wp' 'y5' 'y9' 'yk' 'yy' 'z2' 'zd' 'zw' 2016-05-17 14:21:22.326724 380 '1i' '6c' 'ah' 'aq' 'ax' 'b4' 'cg' 'd5' 'da' 'do' 'eu' 'ex' 'ez' 'fa' 'go' 'gt' 'h5' 'h8' 'hi' 'i2' 'ib' 'il' 'in' 'is' 'iz' 'j0' 'j7' 'jn' 'jq' 'ku' 'kw' 'li' 'ls ' 'n3' 'nc' 'nt' 'o6' 'oc' 'p4' 'p7' 'pc' 'qc' 'qi' 'qp' 'qs' 'qw' 'r3' 'rl' 'rq' ' ry' 's5' 'si' 'sm' 'ta' 'tr' 'ud' 'ut' 'uw' 'v0' 'w7' 'wg' 'wm' 'xi' 'yi' 'yl' 'yn' 'z1' 'z5' 'zk' 'zp' 2016-05-17 15:21:22.326724 381 'a2' 'a4' 'ac' 'ag' 'ao' 'ay' 'ce' 'di' 'dm' 'dr' 'dz' 'e9' 'eg' 'ej' 'el' 'em' 'eq' 'et' 'ey' 'fa' 'fw' 'fz' 'gg' 'gh' 'gp' 'gr' 'h6' 'hj' 'hk' 'i7' 'id' 'ik' 'iu ' 'j2' 'kc' 'l1' 'lh' 'm5' 'm9' 'mj' 'mr' 'mx' 'ok' 'ot' 'ov' 'oz' 'p5' 'q0' 'q1' ' qe' 'qg' 'r2' 'rj' 'rk' 'rw' 'sa' 't3' 't6' 't9' 'te' 'tf' 'tj' 'tk' 'u4' 'wa' 'wf' 'wu' 'wy' 'yg' 'yj' 'ys' 'zk' 'zy' 2016-05-17 16:21:22.326724 382 'a0' 'a8' 'b4' 'b9' 'bb' 'cb' 'cn' 'cq' 'ds' 'e2' 'eb' 'ex' 'ez' 'fa' 'fu' 'fz' 'ge' 'gy' 'h0' 'hj' 'ht' 'hu' 'ig' 'in' 'iq' 'is' 'iu' 'jg' 'le' 'ln' 'lr' 'nj' 'nu ' 'oe' 'oo' 'ow' 'oz' 'pf' 'ph' 'pj' 'ps' 'pu' 'pv' 'q0' 'q4' 'qf' 'qm' 'qn' 'qo' ' qq' 'qs' 'qw' 'r2' 'r3' 'ra' 'rk' 's7' 'sa' 'sp' 'tl' 'ue' 'ui' 'vo' 'vs' 'wj' 'wk' 'wn' 'wv' 'ww' 'x0' 'xg' 'xh' 'xx' 'y0' 'yd' 'yr' 'zg' 'zn' 2016-05-17 17:21:22.326 383 '1u' '5k' 'ax' 'az' 'c4' 'eo' 'fi' 'gq' 'hg' 'ho' 'is' 'jq' 'ki' 'oq' 'ov' 'p4' 'l''
```

`'``'`

```
''f''
```

`'``'`

```
''3'' ''d''
```

`'``'`

```
''tb''td''4''5''l''
```

```
'pl' 'po' 'qe' 'qf' 'qn' 'qy' 'r3' 'rm' 'sd' 'se' 'sz' 'tb' 'td' 'u4' 'u5' 'vl' 'vv ' 'wb' 'we' 'wh' 'wz' 'y5' 'ye' 'yv' 'zh' 'zj' 2016-05-17 18:21:22.326724 384 '5y' 'av' 'ax' 'cl' 'cw' 'dh' 'di' 'g7' 'ga' 'gi' 'gx' 'gy' 'i0' 'iu' 'iv' 'jk' 'jv' 'k3' 'l2' 'lo' 'lq' 'mj' 'oj' 'pd' 'pn' 'pv' 'q6' 'qq' 'qv' 'sc' 'tt' 'tv' 'ug ' 'ut' 've' 'vy' 'wi' 'xg' 'xo' 'yi' 'yl' 'yv' 'zm' 2016-05-17 19:21:22.326724 385 'bp' 'cy' 'd6' 'd7' 'em' 'et' 'gf' 'gt' 'hl' 'ib' 'io' 'kz' 'mx' 'nm' 'oe' 'pd' 'qf' 'qk' 'rk' 'rz' 'se' 'si' 'tq' 'tu' 'uu' 'v3' 'wa' 'wf' 'wg' 'wx' 'yd' 'ym' 201 6-05-17 20:21:22.326724 386 'ah' 'ar' 'bk' 'db' 'dd' 'dq' 'eo' 'fe' 'fj' 'fv' 'g2' 'gc' 'hp' 'i7' 'j2' 'k9' 'kt' 'l9' 'ld' 'lu' 'lz' 'me' 'mr' 'mu' 'mx' 'nr' 'o6' 'ol' 'or' 'pa' 'ph' 'pi' 'q4 ' 'qn' 'qp' 'r5' 'rb' 'rn' 's8' 'sf' 't6' 'tl' 'tq' 'tx' 'u6' 'uc' 'uv' 'wf' 'x1' ' x7' 'xa' 'xl' 'xm' 'yb' 'yh' 'yw' 'zw' 2016-05-17 21:21:22.326724 387 'cp' 'i0' 'ia' 'jh' 'kh' 'kl' 'ql' 'sb' 'u3' 'wy' 'ys' 2016-05-17 22:21:22.326724 388 '2o' 'af' 'ah' 'aj' 'al' 'ap' 'as' 'bc' 'd2' 'di' 'dm' 'do' 'ds' 'dt' 'dy' 'eb' 'ed' 'ee' 'ej' 'es' 'ev' 'ex' 'ey' 'gs' 'hk' 'hr' 'hw' 'hz' 'ig' 'is' 'jp' 'jv' 'jx ' 'k4' 'kh' 'kv' 'lb' 'll' 'lw' 'na' 'no' 'o1' 'o8' 'oh' 'oo' 'op' 'pb' 'po' 'q2' ' q4' 'q7' 'qa' 'qc' 'qe' 'qg' 'qm' 'qo' 'qt' 'qw' 'qy' 'qz' 'r4' 'r7' 'r8' 'rp' 'rs' 's2' 'sb' 'sg' 'sl' 't1' 'tj' 'to' 'ts' 'tx' 'u5' 'uz' 'v6' 'w4' 'w5' 'we' 'wh' 'wn ' 'wr' 'wu' 'wv' 'x1' 'y1' 'y8' 'ya' 'yk' 'ym' 'yw' 'z5' 'zx' 2016-05-17 23:21:22.3 26724 389 'bw' 'ci' 'cp' 'cu' 'cw' 'd7' 'e0' 'e3' 'em' 'ev' 'fi' 'fk' 'fm' 'fu' 'ht' 'ix' 'jn' 'kc' 'kw' 'lm' 'mo' 'n8' 'od' 'oo' 'q1' 'qd' 'qw' 'rs' 'sd' 'su' 'sz' 'th' 'ti ' 'ts' 'tw' 'ty' 'u3' 'ua' 'wa' 'wt' 'wy' 'xg' 'xh' 'xp' 'xr' 'yd' 'yj' 'yq' 'yx' ' zu' 2016-05-18 00:21:22.326724 390 'ak' 'dx' 'eb' 'es' 'eu' 'fd' 'ga' 'gf' 'hl' 'i2' 'kb' 'kd' 'mz' 'n1' 'o8' 'qe' 'qs' 'qw' 'rp' 'sf' 'sk' 'sp' 't0' 'tu' 'uh' 'v9' 'vj' 'vs' 'vw' 'wv' 'xs' 'yo' 'z2 ' 2016-05-18 01:21:22.326724 391 '3q' 'am' 'ar' 'az' 'bo' 'cb' 'cv' 'dd' 'ds' 'e1' 'e7' 'en' 'eq' 'er' 'eu' 'ew' 'fq' 'fx' 'g8' 'gm' 'h5' 'ic' 'if' 'jp' 'kw' 'kz' 'l4' 'lf' 'li' 'lm' 'lq' 'lu' 'lz ' 'ml' 'nz' 'o4' 'o6' 'op' 'ow' 'po' 'py' 'qj' 'qk' 'qn' 'qp' 'qw' 'qz' 'r6' 'r8' ' rc' 'rl' 'rt' 's6' 'sh' 'sx' 'sz' 'tc' 'ti' 'tt' 'ty' 'uf' 'uh' 'uj' 'um' 'ut' 'uu' 'uv' 'vn' 'vt' 'we' 'wh' 'wi' 'wq' 'wu' 'wz' 'xn' 'y4' 'yu' 'yz' 'z9' 'ze' 2016-05- 18 02:21:22.326724 392 'ad' 'aj' 'ar' 'b4' 'dj' 'eo' 'eu' 'ex' 'gt' 'hj' 'ie' 'ij' 'iz' 'kg' 'ks' 'l1' 'ld' 'me' 'my' 'mz' 'oi' 'pr' 'qb' 'ry' 'sd' 'to' 'u5' 'wc' 'wf' 'wl' 'xs' 'y2' 'yg ' 'z1' 'zj' 'zt' 2016-05-18 03:21:22.326724 393 'ae' 'cn' 'ct' 'dz' 'eb' 'ee' 'ff' 'fi' 'fk' 'fo' 'ft' 'gj' 'gr' 'ie' 'il' 'iv' 'iw' 'iy' 'jb' 'jf' 'ji' 'ke' 'ku' 'kx' 'l3' 'la' 'of' 'ol' 'ox' 'pb' 'pi' 'pq' 'q8 ' 'qi' 'qj' 'qp' 'qq' 'qw' 'r0' 'r5' 'rk' 'rq' 'ru' 'rz' 'su' 't8' 'tb' 'u0' 'ue' ' um' 'w2' 'wc' 'wm' 'ws' 'wt' 'x4' 'xc' 'xd' 'xm' 'xn' 'y0' 'yb' 'zi' 'zp' 2016-05-1 8 04:21:22.326724 394 'a3' 'ai' 'at' 'd7' 'eu' 'fu' 'gd' 'ii' 'ik' 'j0' 'je' 'lw' 'ly' 'mx' 'n7' 'pm' 'qf' 'qk' 'qt' 'ss' 'to' 'tq' 'un' 'vn' 'vq' 'wo' 'wz' 'yk' 'yy' 'zf' 'zg' 2016-05- 18 05:21:22.326724 395 'dz' 'ea' 'h8' 'j9' 'mr' 'pc' 'qa' 'qt' 'rm' 'rv' 'ub' 'wg' 2016-05-18 06:21:22 .326724 396 'a4' 'an' 'go' 'ki' 'px' 'qq' 'td' 'tm' 'ur' 'wc' 'wp' 'yx' 2016-05-18 07:21:22 .326724 397 '0e' 'a0' 'a1' 'a5' 'ad' 'ao' 'bp' 'bw' 'c0' 'ca' 'cw' 'cx' 'cy' 'dg' 'e8' 'eb' 'ef' 'ek' 'fd' 'fk' 'fv' 'g3' 'gj' 'gn' 'gw' 'hr' 'if' 'ij' 'is' 'ix' 'j7' 'km' 'kp ' 'kq' 'ks' 'kt' 'kv' 'lk' 'mj' 'mn' 'mv' 'mz' 'nn' 'o5' 'oa' 'ol' 'on' 'os' 'pa' ' pb' 'pf' 'po' 'pq' 'pr' 'pv' 'py' 'q1' 'q6' 'qf' 'qh' 'qj' 'qn' 'qt' 'qu' 'qw' 'rf' 'rk' 'rt' 's5' 'sq' 'ss' 't5' 'ta' 'th' 'tj' 'to' 'ts' 'tx' 'tz' 'u0' 'ua' 'ug' 'ui ''uw''ux''vh''vp''we''wg''wi''wj''wp''wq''xm''y6''yr''yt''yu''z8''
```

```
 uw ux vh vp we wg wi wj wp wq xm y6 yr yt yu z8
zs' 2016-05-18 08:21:22.326724 398 'a6' 'ad' 'aj' 'b1' 'bz' 'cd' 'df' 'ed' 'eg' 'eh' 'ev' 'fi' 'fo' 'gj' 'h3' 'he' 'ib' 'j0' 'jc' 'jz' 'kz' 'lc' 'mh' 'pk' 'pu' 'q4' 'qc' 'qk' 'qr' 'qw' 'rc' 'rl' 'ro ' 'rr' 'so' 'sw' 'td' 'tw' 'tx' 'ue' 'us' 'ut' 'vd' 'wi' 'wu' 'xm' 'y2' 'y8' 'ym' ' z6' 'zm' 2016-05-18 09:21:22.326724 399 '4z' 'a2' 'eg' 'f4' 'g9' 'gi' 'hd' 'hn' 'ij' 'io' 'ix' 'iz' 'jb' 'jd' 'kk' 'l4' 'lh' 'lq' 'p9' 'pa' 'pb' 'q7' 'qh' 'qi' 'qk' 'qs' 'r9' 'rc' 'ro' 'rr' 's4' 'tj' 'tz ' 'vi' 'we' 'wp' 'xe' 'yd' 'yg' 'zj' 2016-05-18 10:21:22.326724 400 '5y' 'aw' 'e2' 'gd' 'gn' 'hn' 'ig' 'k9' 'ki' 'oj' 'pk' 'ql' 'qz' 'sl' 't3' 'u4' 'v8' 'wg' 'wu' 'xk' 'ya' 'yf' 'zr' 2016-05-18 11:21:22.326724 401 '5h' 'ak' 'al' 'aq' 'cw' 'd7' 'dm' 'ec' 'ee' 'ef' 'el' 'f4' 'f5' 'f8' 'fh' 'fr' 'fu' 'gh' 'hk' 'ir' 'ix' 'k0' 'k2' 'ka' 'ku' 'lg' 'lr' 'm8' 'mf' 'nq' 'of' 'ph' 'pr ' 'px' 'q2' 'qf' 'qh' 'qk' 'qn' 'qq' 'qs' 'qv' 'qx' 'qy' 'qz' 're' 'rh' 'ro' 'rx' ' sa' 'sh' 'sk' 'tb' 'u1' 'ud' 'uo' 'us' 'uw' 'vg' 'vp' 'w3' 'wb' 'wc' 'wf' 'wg' 'wi' 'wk' 'yr' 'ys' 'yw' 'zw' 'zz' 2016-05-18 12:21:22.326724 402 'af' 'dt' 'e4' 'e8' 'eq' 'et' 'gr' 'kr' 'kv' 'lu' 'oy' 'pb' 'qh' 'ql' 'qw' 'r4' 't8' 'tb' 'td' 'tn' 'uc' 'uj' 'wh' 'xn' 'xs' 'yi' 2016-05-18 13:21:22.326724 403 'am' 'bv' 'dt' 'dy' 'ed' 'gx' 'm7' 'mt' 'q5' 'qv' 'rr' 'sh' 'th' 'ut' 'wd' 'wm' 'y1' 'ym' 'yq' 'yr' 'yt' 2016-05-18 14:21:22.326724 404 'aa' 'al' 'ay' 'c1' 'ca' 'de' 'ea' 'ee' 'eq' 'er' 'ez' 'fc' 'gy' 'i1' 'jb' 'jn' 'jz' 'lp' 'o5' 'om' 'os' 'ou' 'ox' 'px' 'q3' 'qc' 'qs' 'rm' 'rq' 'rt' 'rx' 'ry' 'rz ' 'ss' 'ta' 'tg' 'ti' 'tr' 'u6' 'uv' 'vp' 'wn' 'wu' 'zt' 2016-05-18 15:21:22.326724 405 'ad' 'as' 'dn' 'dq' 'e7' 'ei' 'ey' 'fj' 'h2' 'hu' 'hw' 'i7' 'i9' 'iu' 'jr' 'ma' 'na' 'nh' 'nk' 'pa' 'q5' 'qd' 'qn' 's0' 'so' 'sx' 'u7' 'uc' 'um' 'vb' 'w9' 'wf' 'wh ' 'wl' 'wn' 'wr' 'xl' 'y8' 'yl' 'zw' 2016-05-18 16:21:22.326724 406 '1a' 'a0' 'ae' 'av' 'be' 'bj' 'bv' 'bx' 'bz' 'ck' 'd4' 'do' 'ds' 'du' 'ee' 'eu' 'fg' 'fm' 'fy' 'g1' 'gh' 'h8' 'h9' 'ha' 'he' 'hl' 'hy' 'i6' 'ic' 'io' 'jb' 'jk' 'jq ' 'k1' 'kf' 'km' 'kv' 'l8' 'n0' 'n3' 'oh' 'oz' 'po' 'q9' 'qg' 'qh' 'qi' 'ql' 'qp' ' qr' 'qu' 'qw' 'qx' 'rb' 're' 'rf' 'ri' 'rj' 'rv' 'sj' 'sm' 'sz' 't1' 'tl' 'tm' 'tw' 'tz' 'ua' 'uc' 'ug' 'ut' 'uv' 'ux' 'v7' 'wa' 'wc' 'wf' 'wi' 'wl' 'wp' 'wq' 'wr' 'x3 ' 'x6' 'xk' 'xx' 'y4' 'yp' 'yr' 'yw' 'yy' 'ze' 'zk' 'zy' 2016-05-18 17:21:22.326724 407 '2e' 'al' 'am' 'bt' 'eo' 'ff' 'fl' 'ge' 'gz' 'h0' 'hb' 'i0' 'j2' 'lh' 'lm' 'ls' 'mg' 'mw' 'on' 'ox' 'pa' 'pb' 'pg' 'q3' 'q6' 'qe' 'ra' 're' 'rm' 'rr' 'rt' 'ry' 'sc ' 'sm' 't9' 'tu' 'tx' 'ul' 'ux' 'vh' 'wn' 'wt' 'wv' 'ys' 'yw' 2016-05-18 18:21:22.3 26724 408 'ag' 'al' 'ay' 'fw' 'hi' 'ou' 'p6' 'qy' 'rg' 'rz' 'sx' 'uy' 'zb' 2016-05-18 19: 21:22.326724 409 '1o' '3w' 'aw' 'be' 'bx' 'e7' 'eo' 'ey' 'ff' 'fx' 'ht' 'jb' 'km' 'kv' 'l6' 'la' 'nu' 'ny' 'pk' 'qc' 'qi' 'rk' 'ro' 'rw' 's3' 'sh' 't5' 'u1' 'uy' 'vi' 'vm' 'wi' 'x3 ' 'xo' 'yn' 2016-05-18 20:21:22.326724 410 'aa' 'as' 'cg' 'dh' 'dn' 'dr' 'e0' 'h2' 'hr' 'j2' 'jf' 'js' 'kc' 'kw' 'ld' 'lh' 'mk' 'n3' 'q3' 'qe' 'ql' 'rv' 's3' 'w0' 'xg' 'ym' 'yt' 'zv' 2016-05-18 21:21:22.326 411 '3y' 'a1' 'ay' 'cn' 'd3' 'dc' 'dh' 'e9' 'ef' 'ew' 'f9' 'fd' 'fg' 'ft' 'h6' 'hs' 'hu' 'hz' 'i0' 'ib' 'ip' 'iu' 'jw' 'kf' 'kp' 'kw' 'li' 'lp' 'mg' 'mj' 'mz' 'ng' 'oc ' 'od' 'om' 'ou' 'ov' 'p8' 'pi' 'q8' 'qe' 'qf' 'qh' 'qj' 'qo' 'qt' 'qv' 'qz' 'r2' ' r3' 'rc' 'rm' 't4' 'ty' 'tz' 'u6' 'ua' 'ut' 'v3' 'vj' 'w0' 'w6' 'wi' 'wj' 'wq' 'wt' 'wu' 'xe' 'xv' 'xy' 'y3' 'yv' 'zw' 2016-05-18 22:21:22.326724 412 '5q' 'av' 'd2' 'd4' 'e5' 'jc' 'km' 'mm' 'pa' 'rs' 's4' 'si' 'tc' 'ut' 2016-05-1 8 23:21:22.326724 413 'ae' 'av' 'bj' 'bk' 'c3' 'd3' 'dj' 'eb' 'ed' 'ef' 'ei' 'ej' 'en' 'ep' 'fl' 'fp' 'fr' 'fu' 'fz' 'g8' 'gd' 'h6' 'ht' 'hu' 'i7' 'if' 'im' 'j0' 'j1' 'je' 'jx' 'ku' 'l6 ' 'l7' 'll' 'lp' 'mc' 'ns' 'o4' 'oi' 'op' 'oz' 'q4' 'qa' 'qf' 'qh' 'ql' 'qn' 'qv' ' r0' 'r1' 'r4' 'rh' 'rj' 'rw' 'sd' 'sn' 'so' 't6' 'ti' 'tw' 'uc' 'uf' 'uk' 'ul' 'uw'
```

`j`

```
'v3' 'v8' 'vd' 'vr' 'w7' 'w9' 'wa' 'wb' 'wg' 'wh' 'wk' 'wl' 'wn' 'wo' 'wz' 'xf' 'xg ' 'xo' 'xv' 'y2' 'yl' 'zr' 'zs' 'zw' 2016-05-19 00:21:22.326724 414 '1y' '5p' '6o' 'au' 'b2' 'bg' 'do' 'dw' 'e1' 'e9' 'ea' 'ei' 'em' 'ev' 'f0' 'gc' 'hj' 'hx' 'k7' 'km' 'kp' 'kx' 'mj' 'mu' 'o3' 'oz' 'pf' 'q5' 'qe' 'qg' 'qh' 'qk' 'ql ' 'qn' 'qo' 'rh' 'rk' 'ru' 'rx' 't1' 't3' 'th' 'v2' 'vx' 'w2' 'wc' 'wl' 'wm' 'wn' ' ws' 'x5' 'ye' 'yh' 'yk' 'yu' 'zw' 2016-05-19 01:21:22.326724 415 '1x' 'a2' 'ah' 'az' 'bb' 'be' 'bz' 'd1' 'dd' 'du' 'ee' 'eh' 'en' 'eu' 'ey' 'ez' 'fl' 'fs' 'g4' 'gm' 'gr' 'ha' 'hf' 'hg' 'hr' 'hw' 'i6' 'id' 'ij' 'j2' 'jv' 'k9' 'lg ' 'm9' 'md' 'me' 'mg' 'mp' 'nd' 'nf' 'ng' 'nj' 'ny' 'nz' 'oj' 'os' 'pi' 'pj' 'pt' ' q9' 'qa' 'qf' 'qh' 'qk' 'qn' 'qq' 'qs' 'rz' 'sb' 't7' 't8' 'tw' 'ty' 'u2' 'u3' 'ua' 'ub' 'uy' 'uz' 'w1' 'w3' 'w5' 'wa' 'wc' 'we' 'wh' 'wp' 'wr' 'xd' 'xs' 'y3' 'yd' 'yk ' 'yl' 'yo' 'ze' 'zh' 'zo' 2016-05-19 02:21:22.326724 416 '2b' '3f' '5e' '7o' 'a4' 'ai' 'as' 'bc' 'bn' 'cz' 'd8' 'dg' 'dj' 'du' 'e5' 'el' 'et' 'ex' 'gc' 'gj' 'hi' 'hn' 'ig' 'ij' 'j3' 'js' 'l3' 'l6' 'lh' 'ls' 'mb' 'n1' 'o0 ' 'ot' 'q5' 'qd' 'qh' 'qv' 'qz' 'ra' 'rj' 's8' 'tb' 'tf' 'th' 'tx' 'ty' 'vm' 'wf' ' wg' 'wh' 'wn' 'y1' 'y5' 'yw' 'yz' 2016-05-19 03:21:22.326724 417 '2o' 'a5' 'cg' 'ch' 'cp' 'eb' 'eg' 'eh' 'ew' 'fu' 'g4' 'hc' 'hx' 'il' 'li' 'rd' 'sf' 'sw' 'tg' 'uc' 'zj' 2016-05-19 04:21:22.326724 418 'c7' 'eb' 'er' 'gb' 'if' 'ko' 'ml' 'oq' 'ot' 'pa' 'qk' 'qs' 'rl' 'rp' 'sc' 'tf' 'tv' 'tw' 'uc' 'ud' 'uz' 'vk' 'vm' 'w0' 'wm' 'wu' 'yd' 'yq' 'yy' 'zu' 2016-05-19 05 :21:22.326724 419 '5e' 'a1' 'ak' 'at' 'av' 'bi' 'bj' 'c7' 'dl' 'do' 'e0' 'ee' 'el' 'em' 'es' 'fl' 'fy' 'g2' 'g6' 'g7' 'gr' 'gv' 'h3' 'hg' 'hr' 'ht' 'ii' 'il' 'is' 'j8' 'jm' 'jq' 'jv ' 'k0' 'ka' 'kk' 'l3' 'la' 'lh' 'ms' 'mz' 'no' 'oa' 'os' 'ox' 'pa' 'pc' 'pl' 'pq' ' px' 'q1' 'q3' 'q5' 'q8' 'qb' 'qi' 'ql' 'qw' 'qy' 'qz' 're' 'ri' 'rp' 'rx' 's1' 's3' 'sh' 'sq' 't1' 't5' 'ta' 'td' 'tj' 'to' 'tt' 'ub' 'uc' 'ur' 'uv' 'v1' 'vs' 'w7' 'wb ' 'wd' 'wj' 'wl' 'wm' 'wq' 'xr' 'xt' 'ym' 'yu' 'yx' 'yz' 'z8' 'zp' 'zr' 'zs' 2016-0 5-19 06:21:22.326724 420 '2v' '7g' 'a1' 'ar' 'bw' 'cs' 'dt' 'ee' 'eg' 'f4' 'fd' 'fl' 'g0' 'ge' 'gx' 'hf' 'hk' 'ht' 'i7' 'il' 'jy' 'ka' 'kl' 'lb' 'lm' 'lv' 'mu' 'nk' 'ns' 'nw' 'oe' 'og' 'oj ' 'ol' 'ou' 'pk' 'q2' 'q3' 'qi' 'qn' 'qo' 'qs' 'qy' 'r5' 'rh' 'rj' 'rm' 'rq' 'rr' ' rs' 'rt' 'ru' 'rv' 'ss' 'th' 'tj' 'uj' 'ul' 'um' 'un' 'uo' 'uv' 'w2' 'w6' 'wf' 'wh' 'wk' 'wo' 'wx' 'y4' 'y5' 'yb' 'yn' 'yo' 'ys' 'yz' 'zb' 'zt' 'zw' 2016-05-19 07:21:2 2.326724 421 'ai' 'ak' 'as' 'ax' 'b8' 'bd' 'bq' 'bv' 'd1' 'd8' 'dl' 'e9' 'ew' 'ez' 'fz' 'gj' 'gu' 'hk' 'hq' 'i2' 'ie' 'ip' 'iq' 'is' 'iz' 'jf' 'k0' 'kk' 'l6' 'md' 'mx' 'na' 'nf ' 'o5' 'ol' 'p3' 'pe' 'q2' 'qf' 'qj' 'qm' 'qn' 'qs' 'qv' 'r2' 'ra' 'rv' 'ry' 's1' ' s5' 'si' 't0' 'tc' 'te' 'tn' 'tq' 'tz' 'u1' 'uj' 'ut' 'w3' 'wa' 'wd' 'wh' 'wj' 'wo' 'wu' 'wv' 'ww' 'xk' 'xo' 'yi' 'yk' 'yl' 'zb' 'zw' 2016-05-19 08:21:22.326724 422 '6b' 'af' 'd3' 'df' 'dg' 'ds' 'e1' 'eb' 'er' 'f3' 'ft' 'ho' 'ik' 'k1' 'k2' 'li' 'mj' 'ni' 'py' 'qx' 'rb' 'rp' 'rv' 'sd' 'sh' 'sl' 'u5' 'uf' 'vk' 'vs' 'vx' 'wg' 'wm ' 'wr' 'ws' 'wz' 'xn' 'zh' 2016-05-19 09:21:22.326724 423 'ab' 'at' 'cr' 'e9' 'g0' 'gv' 'ib' 'iv' 'iz' 'jb' 'jm' 'k0' 'kh' 'o2' 'o7' 'oq' 'ot' 'pj' 'ps' 'qj' 'qz' 'r9' 'rn' 'sa' 't1' 'ti' 'tq' 'ue' 'us' 'wc' 'wo' 'ww' 'yi ' 'ys' 'za' 2016-05-19 10:21:22.326724 424 '1t' 'ai' 'cu' 'cw' 'cx' 'dd' 'de' 'ds' 'e0' 'e2' 'e6' 'eb' 'ei' 'eq' 'eu' 'ev' 'ez' 'f5' 'f8' 'fc' 'g2' 'gd' 'gs' 'gv' 'hu' 'hy' 'id' 'ig' 'ij' 'ir' 'iv' 'ju' 'ka ' 'kj' 'kl' 'ks' 'kv' 'kw' 'kx' 'la' 'lh' 'lm' 'ls' 'lv' 'lz' 'mg' 'mh' 'mp' 'ns' ' nt' 'nu' 'nx' 'o6' 'o9' 'oc' 'oj' 'pa' 'pj' 'pl' 'pv' 'q3' 'q5' 'qb' 'qh' 'ql' 'qn' 'qr' 'qs' 'qz' 'rb' 'rf' 'rh' 'rm' 'sm' 'sn' 'sw' 't5' 't9' 'tq' 'ty' 'uj' 'v2' 'vz ' 'w6' 'wc' 'wg' 'wi' 'wj' 'wk' 'wm' 'wn' 'wt' 'wv' 'ww' 'wz' 'x0' 'xb' 'xc' 'yb' ' yt' 'yv' 'zp' 'zy' 2016-05-19 11:21:22.326724 425 'ax' 'ch' 'de' 'dl' 'e1' 'el' 'fl' 'fo' 'fp' 'fx' 'gb' 'gj' 'gx' 'hg' 'ho' 'hs' 'ip' 'jr' 'kg' 'l6' 'li' 'ln' 'mg' 'mm' 'mo' 'o2' 'os' 'pm' 'q2' 'q6' 'qr' 're' 'ro
```

```
' 'rr' 'rt' 'rw' 'rx' 'sk' 'tl' 'to' 'tr' 'tt' 'u3' 'u6' 'vo' 'w4' 'w5' 'wb' 'wo' ' wt' 'yi' 'zh' 2016-05-19 12:21:22.326724 426 '4t' 'a3' 'ac' 'au' 'bp' 'br' 'e5' 'ei' 'ek' 'ez' 'fz' 'g5' 'gn' 'ik' 'k9' 'kb' 'kc' 'lm' 'ls' 'ly' 'mj' 'mx' 'nk' 'nr' 'ny' 'o2' 'o8' 'pb' 'pu' 'q2' 'qa' 'qc' 'qh ' 'qi' 'qs' 'qx' 'qz' 'rv' 'rx' 'tc' 'tk' 'tv' 'u8' 'ui' 'uz' 'vo' 'w2' 'wm' 'wp' ' xt' 'yf' 'yv' 'zl' 2016-05-19 13:21:22.326724 427 'aj' 'ar' 'ay' 'eb' 'g5' 'ic' 'la' 'u2' 'up' 'wb' 'x8' 'yr' 2016-05-19 14:21:22 .326724 428 'a2' 'af' 'an' 'aq' 'ar' 'bj' 'bz' 'cx' 'dy' 'eh' 'ek' 'en' 'ex' 'fy' 'gg' 'gr' 'hh' 'if' 'ip' 'it' 'ix' 'j5' 'jf' 'jn' 'k0' 'kk' 'lq' 'nc' 'oc' 'od' 'og' 'oh' 'oo ' 'or' 'pm' 'po' 'qa' 'qd' 'qe' 'qh' 'ql' 'qo' 'qt' 'qx' 'qz' 'rq' 'rr' 'ru' 'sj' ' sk' 'tl' 'tr' 'ug' 'wa' 'wb' 'wd' 'we' 'wk' 'wn' 'wq' 'wr' 'xl' 'xo' 'xw' 'yf' 'yq' 'ys' 'yw' 2016-05-19 15:21:22.326724 429 'ad' 'ai' 'ak' 'df' 'ee' 'fr' 'gg' 'i2' 'i5' 'ig' 'ij' 'ir' 'j1' 'kk' 'km' 'l9' 'qb' 'ql' 'qt' 'qw' 'rb' 's2' 'te' 'ue' 'w0' 'wk' 'wu' 'y4' 'yb' 'yf' 'yp' 'zn' 201 6-05-19 16:21:22.326724 430 '3y' 'a9' 'au' 'bp' 'ca' 'cf' 'cn' 'de' 'dh' 'dk' 'dw' 'ec' 'er' 'ey' 'fn' 'g1' 'hb' 'hd' 'hg' 'hi' 'hj' 'ib' 'if' 'iu' 'j7' 'jd' 'jg' 'jj' 'jx' 'k2' 'km' 'kv' 'ld ' 'lo' 'mz' 'o3' 'ok' 'ot' 'pl' 'pn' 'pr' 'q0' 'q2' 'q7' 'qa' 'qc' 'qg' 'qm' 'qp' ' qx' 'rc' 'rq' 'rt' 'si' 'so' 'tp' 'tu' 'uj' 'vi' 'vx' 'w7' 'wb' 'wd' 'wm' 'ws' 'wt' 'wv' 'y9' 'yf' 'yq' 2016-05-19 17:21:22.326724 431 '10' 'ac' 'as' 'av' 'b6' 'bb' 'cj' 'd3' 'd8' 'dt' 'eb' 'ey' 'ez' 'fm' 'g8' 'gf' 'gs' 'hn' 'hq' 'ib' 'ii' 'j0' 'jb' 'k4' 'l5' 'ld' 'mg' 'mu' 'nz' 'oa' 'ou' 'pn' 'q1 ' 'qa' 'qg' 'qj' 'qm' 'qn' 'qs' 'qx' 'qy' 'rj' 'rm' 'rr' 'ry' 's0' 's7' 't4' 't6' ' tb' 'td' 'u0' 'ua' 'ut' 'ux' 'uz' 'v1' 'v9' 'vd' 'vz' 'wc' 'wj' 'wo' 'ws' 'ww' 'x9' 'xu' 'y7' 'yq' 'yv' 'zw' 'zy' 2016-05-19 18:21:22.326724 432 'ac' 'bv' 'd2' 'de' 'e8' 'ea' 'go' 'gw' 'h4' 'ht' 'iy' 'jm' 'ot' 'pp' 'pw' 'pz' 'qd' 'qn' 'qu' 'qy' 'r1' 'ra' 'rg' 'rh' 'rp' 's0' 'sb' 'sn' 'st' 'td' 'uz' 'vg' 'w1 ' 'w6' 'wa' 'wc' 'we' 'wi' 'wj' 'wu' 'ww' 'y9' 'zr' 2016-05-19 19:21:22.326724 433 '5t' 'ad' 'am' 'ed' 'ei' 'en' 'eo' 'ey' 'f0' 'fp' 'fr' 'gc' 'hp' 'hz' 'ic' 'ix' 'jt' 'kn' 'kr' 'lk' 'ls' 'm1' 'mt' 'nk' 'od' 'p3' 'pa' 'pe' 'pi' 'q4' 'qa' 'qi' 'qk ' 'qq' 'qt' 'qv' 'rb' 'rr' 'rv' 's3' 'se' 'sr' 't0' 'tj' 'tk' 'tp' 'tu' 'u1' 'ud' ' uf' 'uv' 'ux' 'vd' 'vu' 'wh' 'wi' 'wp' 'wu' 'x9' 'xa' 'ye' 'yn' 'yw' 'zj' 'zs' 2016 -05-19 20:21:22.326724 434 'a1' 'ag' 'ai' 'ap' 'bp' 'by' 'dc' 'dy' 'e5' 'eg' 'ei' 'el' 'em' 'fc' 'gl' 'h8' 'hr' 'i1' 'ib' 'ie' 'if' 'ij' 'j5' 'jj' 'kf' 'kx' 'lc' 'm3' 'mg' 'nb' 'ol' 'ph' 'py ' 'q1' 'q5' 'qi' 'qk' 'ql' 'qp' 'qs' 'sv' 'td' 'te' 'tn' 'vd' 'vm' 'vq' 'wv' 'xp' ' xu' 'yb' 'yo' 'yq' 'yx' 'yy' 'zp' 'zr' 'zx' 'zz' 2016-05-19 21:21:22.326724 435 '2l' '9f' 'a2' 'ak' 'as' 'av' 'bi' 'c1' 'cf' 'ct' 'cu' 'db' 'dp' 'du' 'dv' 'e3' 'e9' 'ee' 'eg' 'el' 'fm' 'gu' 'hc' 'he' 'i3' 'i9' 'ib' 'ik' 'im' 'ir' 'j7' 'jp' 'jv ' 'ki' 'kl' 'l6' 'lj' 'lo' 'lw' 'md' 'mj' 'mk' 'ms' 'mw' 'na' 'nq' 'o2' 'od' 'ox' ' p3' 'pj' 'pp' 'q6' 'q7' 'q9' 'qb' 'qg' 'qr' 'qs' 'r7' 'r8' 'rd' 're' 'rf' 'rg' 'rp' 'rv' 'rw' 's6' 'sc' 'sq' 't6' 'tb' 'tc' 'te' 'tj' 'tn' 'tx' 'tz' 'uh' 'uq' 'uu' 'v4 ' 'vw' 'w3' 'w8' 'wa' 'wj' 'wk' 'wp' 'x3' 'xg' 'xy' 'y1' 'y6' 'yc' 'yi' 'yn' 'yo' ' yw' 'yz' 'z6' 'z8' 'zk' 'zz' 2016-05-19 22:21:22.326724 436 '5t' 'al' 'db' 'dt' 'dx' 'ea' 'en' 'g6' 'gc' 'gm' 'gy' 'if' 'ii' 'ik' 'jb' 'jv' 'k5' 'po' 'pv' 'py' 'qj' 'qp' 'rz' 'ux' 'v1' 'w4' 'w8' 'wi' 'yv' 2016-05-19 23:21:2 2.326724 437 'fb' 'in' 'iy' 'lu' 'p4' 'pd' 'qa' 'qq' 's6' 'ta' 'y1' 'yg' 'yy' 'zk' 2016-05-2 0 00:21:22.326724 438 'av' 'dp' 'ff' 'fx' 'jk' 'ke' 'lb' 'lm' 'n1' 'ql' 'rv' 's4' 'uv' 'wl' 'ws' 'yj' 2016-05-20 01:21:22.326724 439 '7y' 'aq' 'cu' 'd3' 'h2' 'ih' 'oc' 'qh' 'rc' 'rs' 't3' 'ud' 'we' 'zt' 2016-05-2 0 02:21:22.326724
```

```
440 '7u' 'a4' 'ah' 'aj' 'al' 'cu' 'e1' 'fi' 'fq' 'fr' 'he' 'hi' 'hk' 'hn' 'hp' 'hs' 'ih' 'iw' 'je' 'k4' 'k6' 'kx' 'l1' 'lf' 'li' 'lj' 'lm' 'lp' 'ls' 'lu' 'ma' 'nr' 'o2 ' 'o4' 'oe' 'oh' 'os' 'ow' 'p7' 'pl' 'q3' 'qj' 'qt' 'qy' 'qz' 'r3' 'rc' 'rm' 'ro' ' s0' 's8' 'so' 't7' 'th' 'ti' 'tm' 'tt' 'ut' 'v5' 'va' 've' 'w7' 'wc' 'wk' 'wl' 'wm' 'wq' 'wu' 'x0' 'zh' 2016-05-20 03:21:22.326724 441 'ah' 'bg' 'bw' 'ca' 'cn' 'cy' 'da' 'dq' 'dt' 'eq' 'ex' 'fe' 'ff' 'ga' 'gr' 'kv' 'ld' 'my' 'od' 'oq' 'p3' 'p5' 'pc' 'pf' 'q5' 'qa' 'qc' 'qi' 'ql' 'qr' 'qx' 'qz' 'rd ' 'rk' 'rq' 'ru' 'rw' 's7' 'sa' 'sh' 'tk' 'um' 'un' 'v4' 'vw' 'wg' 'wr' 'wt' 'xt' ' ya' 'yo' 'z6' 'zm' 2016-05-20 04:21:22.326724 442 'd8' 'dm' 'eg' 'et' 'ge' 'gz' 'i8' 'ig' 'il' 'iy' 'jo' 'k6' 'lm' 'oj' 'p3' 'pw' 'qd' 'qp' 'qq' 'qz' 'r7' 's1' 'sr' 'sx' 't4' 'uz' 'vm' 'vr' 'w0' 'wj' 'wp' 'xc' 'y1 ' 'yj' 'zd' 2016-05-20 05:21:22.326724 443 'a0' 'ck' 'fp' 'g4' 'ib' 'ih' 'im' 'iq' 'kz' 'll' 'lv' 'nc' 'oq' 'qf' 'qv' 'rg' 'rk' 'tc' 'tn' 'u1' 'u8' 'uj' 'un' 'vv' 2016-05-20 06:21:22.326724 444 '6x' 'a4' 'ae' 'as' 'd5' 'df' 'e9' 'ek' 'ew' 'ex' 'ez' 'fa' 'fe' 'fr' 'gk' 'hb' 'hg' 'hl' 'hp' 'id' 'it' 'ix' 'jc' 'jg' 'jk' 'jm' 'js' 'ju' 'ln' 'lq' 'mo' 'ms' 'o7 ' 'od' 'oi' 'oo' 'pn' 'qd' 'qt' 'qv' 'r0' 'rc' 'rj' 'rk' 'rn' 'rp' 'rx' 'rz' 'sc' ' sg' 'sk' 'so' 'ti' 'tn' 'to' 'tr' 'tz' 'uk' 'um' 'ut' 'v1' 'vr' 'wo' 'wr' 'wu' 'wz' 'xn' 'xu' 'y4' 'yg' 'z2' 2016-05-20 07:21:22.326724 445 '1l' '2l' 'ag' 'aj' 'al' 'an' 'ay' 'bo' 'cg' 'cs' 'cw' 'cx' 'db' 'dd' 'e1' 'e8' 'ee' 'ef' 'ej' 'eu' 'ew' 'fc' 'ff' 'fh' 'fo' 'fv' 'fz' 'g1' 'gj' 'gk' 'gw' 'ha' 'i3 ' 'ib' 'iu' 'jv' 'k9' 'kq' 'ku' 'kw' 'lv' 'lw' 'ly' 'mp' 'my' 'nf' 'ng' 'nw' 'o6' ' oe' 'or' 'ou' 'oz' 'p4' 'pc' 'ph' 'pn' 'py' 'q0' 'qd' 'qe' 'qp' 'qs' 'qu' 'qv' 'qz' 'r6' 'rg' 'rj' 'rt' 'ru' 'rv' 'rw' 'sx' 't2' 'tl' 'tn' 'tq' 'tx' 'tz' 'ue' 'ui' 'ul ' 'uo' 'uu' 'w0' 'w1' 'w4' 'w6' 'w8' 'w9' 'wh' 'wi' 'wp' 'ws' 'wt' 'wx' 'yd' 'zd' ' zf' 'zx' 2016-05-20 08:21:22.326724 446 'aw' 'bm' 'dw' 'e5' 'ht' 'j4' 'kv' 'm5' 'oi' 'qa' 'qe' 'qf' 'ri' 'rj' 't6' 't8' 'un' 'wc' 'yb' 'yj' 2016-05-20 09:21:22.326724 447 '4a' 'a9' 'au' 'bn' 'bs' 'cg' 'd4' 'dx' 'fb' 'fk' 'gc' 'hh' 'ht' 'hy' 'iy' 'je' 'jg' 'jj' 'jp' 'ju' 'kz' 'la' 'm8' 'na' 'oa' 'oj' 'ol' 'or' 'ov' 'ox' 'p6' 'po' 'q0 ' 'q9' 'qc' 'qe' 'qi' 'qq' 'qt' 'qx' 'si' 'sn' 'su' 'sw' 't8' 'ta' 'tv' 'tz' 'uq' ' ut' 'w6' 'w7' 'we' 'wk' 'wl' 'wq' 'wy' 'y4' 'ya' 'ze' 'zq' 'zy' 2016-05-20 10:21:22 .326724 448 '3h' '4h' '93' 'ak' 'ao' 'bq' 'cw' 'db' 'dx' 'eb' 'ef' 'el' 'eu' 'ex' 'fc' 'fg' 'fo' 'fr' 'fs' 'fx' 'g5' 'gl' 'go' 'hs' 'i0' 'ii' 'ix' 'j3' 'jc' 'ke' 'l2' 'lf' 'lo ' 'm6' 'ms' 'ne' 'oi' 'ox' 'p6' 'pb' 'pr' 'q9' 'qa' 'qi' 'qj' 'qq' 'qs' 'qu' 'qw' ' re' 'rq' 's0' 'sa' 'se' 'sk' 'sx' 'tj' 'tk' 'u2' 'ua' 'uh' 'un' 'vy' 'wf' 'wh' 'wj' 'wq' 'wv' 'xl' 'xq' 'yf' 'yi' 'yw' 'z3' 2016-05-20 11:21:22.326724 449 'a2' 'ag' 'cz' 'd0' 'd3' 'da' 'di' 'ds' 'e5' 'e6' 'e7' 'ej' 'em' 'ex' 'ff' 'fq' 'gm' 'go' 'gt' 'gv' 'gx' 'ho' 'hv' 'i8' 'ic' 'ii' 'il' 'im' 'it' 'ix' 'j1' 'ja' 'jd ' 'js' 'kw' 'l6' 'le' 'lk' 'ln' 'mt' 'my' 'ns' 'ol' 'op' 'os' 'p0' 'pu' 'pv' 'pz' ' q4' 'q5' 'qe' 'qh' 'ql' 'qx' 'qy' 'r1' 'rk' 'rr' 'sb' 'sn' 'te' 'tt' 'ui' 'v6' 'w6' 'we' 'ws' 'wy' 'xt' 'xu' 'yf' 'yq' 'yz' 'zy' 2016-05-20 12:21:22.326724 450 'ab' 'ct' 'cv' 'cw' 'dg' 'ds' 'e0' 'e5' 'f3' 'fj' 'fl' 'fn' 'gy' 'ha' 'ie' 'if' 'jf' 'ju' 'jx' 'kg' 'ki' 'kw' 'l0' 'ls' 'm9' 'mj' 'nj' 'of' 'om' 'oq' 'os' 'ov' 'pv ' 'pz' 'q0' 'q5' 'q8' 'qf' 'qg' 'qi' 'qj' 'qm' 'qn' 'qw' 'rk' 'ru' 'sc' 'sn' 'so' ' t1' 'tn' 'tz' 'un' 'uv' 'uw' 'vn' 'wh' 'wn' 'ww' 'xy' 'yd' 'yr' 'yv' 'zh' 'zy' 2016 -05-20 13:21:22.326724 451 '45' '85' 'an' 'bi' 'ca' 'cb' 'co' 'cq' 'cu' 'dt' 'e4' 'eb' 'ed' 'ef' 'em' 'eq' 'er' 'et' 'ex' 'fe' 'fk' 'fv' 'fw' 'gm' 'gq' 'hu' 'it' 'iw' 'j5' 'jj' 'jm' 'jr' 'lq ' 'lz' 'mc' 'n0' 'nq' 'o7' 'ok' 'pd' 'ph' 'q6' 'qe' 'qh' 'qm' 'qy' 'qz' 'r2' 'r5' ' ra' 're' 's6' 'sb' 'sl' 'tb' 'tg' 'ur' 'vl' 'wa' 'wf' 'wt' 'wv' 'ww' 'xr' 'xz' 'yb' 'yf' 'zx' 2016-05-20 14:21:22.326724 452 'ap' 'ca' 'dt' 'dx' 'ep' 'f5' 'fg' 'gq' 'hi' 'hj' 'i4' 'ic' 'it' 'iy' 'jl' 'lz' 'd''9''
```

`'``'`

```
''k''6''
```

`'``'`

```
''f''d''t''9'20160520152122326
```

```
'nd' 'o9' 'og' 'oq' 'pk' 'q6' 'qo' 'ra' 'sf' 'wd' 'wt' 'x9' 2016-05-20 15:21:22.326 453 '5g' 'a5' 'dj' 'dl' 'dr' 'e9' 'ed' 'ep' 'er' 'gb' 'hh' 'hl' 'i0' 'if' 'ig' 'io' 'it' 'k2' 'ki' 'll' 'o9' 'om' 'ot' 'p5' 'q1' 'q6' 'qa' 'qp' 'qw' 'qy' 'r9' 'rb' 'rm ' 'ry' 's7' 'tl' 'ts' 'ut' 'w0' 'wd' 'wu' 'wv' 'xk' 'ya' 'z5' 'zq' 'zs' 2016-05-20 16:21:22.326724 454 '6o' 'av' 'ed' 'ee' 'gf' 'ii' 'o8' 'og' 'om' 'qs' 'ta' 'th' 'tk' 'w0' 2016-05-2 0 17:21:22.326724 455 '17' 'bv' 'c5' 'cn' 'd0' 'di' 'dm' 'dz' 'ec' 'ef' 'et' 'ev' 'ew' 'fa' 'fb' 'fh' 'fw' 'fy' 'g8' 'he' 'hf' 'hp' 'hu' 'hz' 'i2' 'ig' 'ix' 'jy' 'lt' 'mi' 'nm' 'nq' 'o5 ' 'oa' 'od' 'oi' 'oo' 'ox' 'pb' 'po' 'qb' 'qc' 'qf' 'qr' 'qs' 'qt' 'qw' 'qx' 'r0' ' rb' 'rf' 'rh' 'rk' 'ry' 'sb' 'sf' 'sh' 'st' 'tb' 'tj' 'tn' 'tq' 'tu' 'ty' 'u9' 'ud' 'ut' 'uw' 'ux' 'w4' 'wi' 'xm' 'ya' 'yl' 'ys' 'yt' 'yv' 'yy' 'zb' 'zv' 2016-05-20 18 :21:22.326724 456 '3h' 'aw' 'az' 'b2' 'bl' 'bq' 'bt' 'c0' 'cd' 'ck' 'cm' 'cw' 'cy' 'd3' 'e0' 'ef' 'eo' 'ew' 'fj' 'fk' 'gb' 'gc' 'gm' 'gt' 'gz' 'hv' 'in' 'ix' 'jb' 'jg' 'jl' 'jn' 'js ' 'k7' 'kg' 'ku' 'kx' 'kz' 'ld' 'nb' 'ni' 'o3' 'o6' 'od' 'om' 'p3' 'p4' 'pn' 'pu' ' q7' 'qd' 'qh' 'qp' 'qq' 'qr' 'qv' 'qy' 'qz' 'rq' 'sb' 'se' 'sf' 'sh' 'sm' 't0' 'tg' 'tj' 'tl' 'tq' 'ua' 'uk' 'us' 'wd' 'we' 'wj' 'wn' 'wq' 'wv' 'wz' 'yd' 'yg' 'ym' 'yn ' 'yr' 'zc' 'zz' 2016-05-20 19:21:22.326724 457 '1t' 'am' 'aw' 'b4' 'bi' 'bm' 'bx' 'cd' 'cj' 'cv' 'e5' 'ek' 'eo' 'er' 'ex' 'f5' 'f8' 'fp' 'fr' 'fw' 'ga' 'gy' 'hm' 'hs' 'ip' 'ir' 'is' 'it' 'iv' 'iz' 'jf' 'jm' 'jp ' 'ju' 'k6' 'kk' 'kr' 'lb' 'le' 'lt' 'mj' 'nk' 'np' 'nr' 'oa' 'oj' 'pm' 'pn' 'q1' ' q3' 'qb' 'qc' 'qf' 'qh' 'qi' 'qj' 'qq' 'qt' 'qw' 'qy' 'r2' 'r8' 'rf' 'rh' 'rw' 's9' 't3' 'te' 'ti' 'tn' 'tq' 'uu' 'uv' 'uw' 'w0' 'w1' 'w3' 'w7' 'wc' 'wi' 'wk' 'wn' 'wr ' 'wt' 'xm' 'y5' 'ya' 'z7' 'zu' 2016-05-20 20:21:22.326724 458 '2l' 'a5' 'ah' 'ak' 'ar' 'be' 'e6' 'eh' 'ge' 'gj' 'gn' 'gt' 'gy' 'ia' 'ii' 'iw' 'ix' 'jb' 'k9' 'kd' 'ke' 'kh' 'kv' 'lm' 'ly' 'me' 'mt' 'nb' 'np' 'o5' 'oe' 'of' 'og ' 'pd' 'pf' 'pm' 'pt' 'pw' 'q3' 'qc' 'qe' 'qg' 'qh' 'qk' 'ql' 'qs' 'qt' 'qx' 'qz' ' rr' 'rw' 'rx' 'ry' 'sk' 'sr' 'su' 'sv' 'sz' 'ug' 'uk' 'uq' 'vg' 'w7' 'wb' 'wn' 'wr' 'ws' 'wz' 'x6' 'yg' 'yj' 'yo' 'zb' 'zx' 2016-05-20 21:21:22.326724 459 'ab' 'c1' 'cl' 'd3' 'do' 'e5' 'e8' 'eg' 'ek' 'ex' 'gy' 'ia' 'iq' 'iw' 'jf' 'kv' 'm9' 'n4' 'nh' 'nj' 'q3' 'qa' 'qe' 'qg' 'qm' 'sy' 'ta' 'w5' 'w6' 2016-05-20 22:21:2 2.326724 460 '1g' '6b' 'az' 'be' 'c5' 'dp' 'dt' 'e6' 'eg' 'en' 'es' 'et' 'f1' 'fi' 'fn' 'ft' 'fz' 'g0' 'gj' 'gv' 'h8' 'hp' 'hs' 'hu' 'hw' 'hz' 'ia' 'im' 'is' 'iv' 'iw' 'iy' 'jd ' 'kw' 'ky' 'l4' 'l7' 'mn' 'nn' 'nr' 'ny' 'ot' 'p2' 'p8' 'pt' 'q8' 'qa' 'qb' 'qf' ' qh' 'qi' 'qm' 'qt' 'qu' 'qv' 'qy' 'ra' 'rl' 'ro' 'rw' 'rx' 's8' 's9' 'sk' 'sn' 'st' 'sv' 'th' 'tl' 'to' 'tp' 'tu' 'ua' 'uk' 'un' 'uv' 'v8' 've' 'vt' 'vu' 'vv' 'w4' 'wc ' 'wh' 'wo' 'wq' 'wy' 'xe' 'xm' 'xp' 'xu' 'yc' 'yn' 'yq' 'zf' 'zj' 'zs' 'zt' 2016-0 5-20 23:21:22.326724 461 '2a' '3o' '6w' '9h' 'ag' 'ak' 'cu' 'db' 'e3' 'ei' 'ep' 'eq' 'f6' 'fm' 'fq' 'fz' 'g5' 'gi' 'gk' 'gn' 'gp' 'gx' 'hb' 'hw' 'ia' 'ic' 'id' 'ig' 'ih' 'im' 'jh' 'jy' 'k3 ' 'kh' 'kv' 'l4' 'lf' 'lh' 'lu' 'ni' 'o7' 'oe' 'oi' 'op' 'os' 'ow' 'p0' 'p1' 'pj' ' pp' 'qa' 'qe' 'qi' 'qm' 'qz' 'rb' 're' 'rh' 'sa' 'sn' 'te' 'th' 'u3' 'ui' 'uj' 'us' 'vh' 'w1' 'w7' 'wc' 'wg' 'wh' 'wo' 'wx' 'xr' 'xw' 'xz' 'y5' 'y6' 'y9' 'ye' 'yo' 'ze ' 'zg' 'zp' 2016-05-21 00:21:22.326724 462 'b7' 'eu' 'g4' 'hw' 'in' 'pi' 'qt' 'r0' 'rg' 'sn' 'sz' 'tc' 'wd' 'zs' 2016-05-2 1 01:21:22.326724 463 'a3' 'ad' 'ar' 'at' 'bb' 'bf' 'bt' 'cg' 'cx' 'd6' 'de' 'df' 'e4' 'e6' 'eg' 'et' 'ex' 'f0' 'fe' 'fg' 'fj' 'fo' 'gh' 'hb' 'hj' 'hq' 'hr' 'hv' 'ia' 'id' 'is' 'it' 'iy ' 'ja' 'jj' 'jq' 'jw' 'l2' 'l7' 'lc' 'lu' 'nc' 'no' 'np' 'nt' 'ob' 'od' 'og' 'oo' ' os' 'pe' 'pj' 'pl' 'po' 'pq' 'pu' 'q2' 'qa' 'qc' 'qf' 'qr' 'qt' 'qx' 're' 'rk' 'rn' 'ro' 'ru' 'rw' 'rx' 's7' 's8' 'sy' 'tc' 'tf' 'tg' 'th' 'tm' 'to' 'tv' 'tx' 'tz' 'va ''vp''w0''w1''wh''wl''wq''wr''wt''ww''wy''x7''xl''xy''y0''ye''yr''
```

```
 vp w0 w1 wh wl wq wr wt ww wy x7 xl xy y0 ye yr
yy' 'z3' 'zf' 'zo' 2016-05-21 02:21:22.326724 464 '15' '4o' '7h' 'aa' 'av' 'b0' 'cb' 'da' 'dh' 'di' 'dr' 'e0' 'ee' 'eo' 'ep' 'ey' 'fi' 'fo' 'fq' 'fx' 'fz' 'g9' 'ge' 'hd' 'hh' 'hs' 'i4' 'i9' 'iq' 'it' 'iw' 'ix' 'iy ' 'j8' 'jr' 'ld' 'm1' 'mo' 'nx' 'ob' 'ol' 'ot' 'pj' 'qf' 'qj' 'qk' 'qp' 'qv' 'qy' ' r4' 'r5' 'rl' 'rm' 'rq' 'rz' 's8' 'sc' 'sd' 'sf' 'sh' 'sn' 'ss' 't5' 't7' 'tj' 'to' 'tw' 'u6' 'uc' 'ud' 'ug' 'ui' 'uk' 'ut' 'uy' 'uz' 'vi' 'w0' 'w9' 'wb' 'wg' 'wl' 'ww ' 'wx' 'wy' 'xa' 'xb' 'xo' 'ya' 'yi' 'yu' 'yv' 'yz' 'zm' 'zv' 'zx' 'zy' 'zz' 2016-0 5-21 03:21:22.326724 465 '2b' '2e' 'ao' 'ap' 'au' 'bo' 'by' 'cr' 'do' 'du' 'dy' 'e7' 'eb' 'eh' 'em' 'ey' 'f6' 'ff' 'fu' 'gc' 'gi' 'gk' 'h1' 'hp' 'hs' 'hy' 'ia' 'ic' 'ig' 'ik' 'im' 'je' 'jf ' 'ji' 'jr' 'l5' 'lf' 'lp' 'mv' 'ne' 'nt' 'oa' 'os' 'pj' 'po' 'q9' 'qd' 'qe' 'qf' ' qw' 'qy' 'ra' 'rg' 'rk' 'rp' 'rq' 'rx' 'sb' 'si' 'sn' 'ta' 'ux' 'v1' 'vd' 'wa' 'wk' 'wr' 'wu' 'xo' 'yg' 'yl' 'yz' 'zi' 'zt' 2016-05-21 04:21:22.326724 466 '3k' 'f5' 'if' 'kg' 'lj' 'ol' 'qr' 'so' 'ta' 'u1' 'vu' 'wr' 'y2' 2016-05-21 05: 21:22.326724 467 'cv' 'ds' 'dx' 'dy' 'ex' 'hh' 'lf' 'mq' 'qe' 'qu' 'rb' 'tb' 'tv' 'tz' 'ue' 'ui' 'wi' 'yb' 'zz' 2016-05-21 06:21:22.326724 468 '1t' 'a0' 'ah' 'ar' 'at' 'be' 'bs' 'bt' 'co' 'd9' 'e9' 'ea' 'ec' 'ei' 'eo' 'er' 'ez' 'fa' 'fz' 'gl' 'gt' 'h8' 'h9' 'hb' 'hv' 'ia' 'ic' 'if' 'im' 'io' 'iq' 'ix' 'k9 ' 'kq' 'lo' 'm4' 'md' 'mo' 'mz' 'ni' 'nr' 'nz' 'o8' 'ox' 'pk' 'pr' 'q1' 'q3' 'q8' ' qa' 'qb' 'qf' 'qg' 'qi' 'ql' 'qr' 'r3' 'rc' 'rf' 'rg' 'rr' 's0' 'sf' 'tg' 'tw' 'u2' 'uh' 'un' 'ur' 'ux' 'vb' 'vr' 'w7' 'w9' 'wd' 'wh' 'wm' 'wo' 'wr' 'ws' 'wv' 'x4' 'xj ' 'xx' 'y3' 'y8' 'yd' 'yl' 'yo' 'yq' 'yr' 'yw' 'z8' 'za' 'zb' 'zg' 'zo' 'zs' 2016-0 5-21 07:21:22.326724 469 'a1' 'cd' 'cl' 'd8' 'ek' 'ig' 'ih' 'in' 'lq' 'o3' 'ow' 'px' 'qg' 'qm' 'qq' 'qr' 'qs' 'qy' 'rd' 'rh' 'to' 'tq' 'ul' 'wc' 'x9' 'ya' 'yf' 'yw' 2016-05-21 08:21:22.326 470 '3q' '5p' 'a2' 'be' 'bv' 'bw' 'cv' 'd8' 'df' 'dh' 'dk' 'e2' 'ec' 'eo' 'fc' 'g8' 'gq' 'h8' 'ig' 'io' 'ir' 'iv' 'je' 'kq' 'kx' 'lc' 'lr' 'lt' 'ok' 'pk' 'q1' 'q4' 'qe ' 'qh' 'qw' 'qz' 'rj' 'rv' 't8' 'tf' 'tl' 'tq' 'uh' 'uz' 'wk' 'wp' 'ws' 'wt' 'wv' ' x3' 'yb' 'ye' 'yo' 'yp' 'yy' 'z6' 'z8' 'zb' 'zm' 2016-05-21 09:21:22.326724 471 'b0' 'bg' 'bh' 'cu' 'd8' 'dv' 'er' 'fd' 'fm' 'fo' 'gg' 'ij' 'ir' 'iu' 'jc' 'jl' 'jn' 'jo' 'k4' 'kb' 'ku' 'lq' 'ly' 'mw' 'of' 'op' 'ph' 'pk' 'ps' 'px' 'q0' 'qd' 'qg ' 'qz' 'rb' 'rp' 'rs' 'rv' 'su' 't9' 'tm' 'tp' 'tx' 'ty' 'ug' 'ul' 'uo' 'up' 'uv' ' v5' 'wh' 'wr' 'ww' 'xw' 'y1' 'yd' 'yf' 'yn' 'z4' 'z8' 'zf' 'zn' 2016-05-21 10:21:22 .326724 472 'cm' 'dm' 'eh' 'em' 'ik' 'j0' 'kk' 'lp' 'ng' 'or' 'pu' 'qd' 'tw' 2016-05-21 11: 21:22.326724 473 '4p' 'am' 'bj' 'bq' 'cg' 'cm' 'cz' 'dm' 'ds' 'du' 'e6' 'eg' 'en' 'eo' 'eq' 'et' 'ev' 'ex' 'fw' 'go' 'hb' 'hq' 'i0' 'ij' 'k6' 'kg' 'l6' 'lm' 'lq' 'mr' 'ms' 'oa' 'p6 ' 'q7' 'qa' 'qi' 'qk' 'r8' 'ra' 're' 'rr' 's8' 'sj' 't6' 't9' 'tc' 'v1' 'vd' 'w1' ' wf' 'wj' 'xy' 'yd' 'yn' 'yo' 'yt' 'yu' 2016-05-21 12:21:22.326724 474 '43' '9w' 'ah' 'av' 'bl' 'dr' 'ef' 'es' 'fm' 'ft' 'gy' 'hg' 'hq' 'hy' 'iu' 'ix' 'j1' 'jn' 'lg' 'np' 'o9' 'op' 'ou' 'ox' 'qq' 'st' 'sw' 't8' 't9' 'vs' 'vw' 'wd' 'wx ' 'wz' 'xr' 'xt' 'xv' 'y5' 'y8' 'yi' 'ze' 2016-05-21 13:21:22.326724 475 'a3' 'bh' 'c2' 'ca' 'e1' 'fb' 'fe' 'hd' 'hx' 'jc' 'md' 'nl' 'q9' 'qi' 'qq' 'qs' 'qt' 'rx' 'te' 'tv' 'u2' 'w8' 'wi' 'wr' 'xq' 'y9' 2016-05-21 14:21:22.326724 476 '1o' 'a0' 'aa' 'bd' 'bj' 'ch' 'cm' 'dj' 'e2' 'eq' 'eu' 'fj' 'fo' 'g9' 'go' 'hi' 'ia' 'ix' 'jh' 'jl' 'jy' 'lh' 'nd' 'nw' 'ox' 'p3' 'pi' 'pm' 'pt' 'q3' 'qh' 'qn' 'ra ' 'ri' 'rr' 'ru' 'rv' 't3' 'tm' 'u3' 'ue' 'us' 'uz' 'vn' 'w1' 'wl' 'wo' 'wx' 'xj' ' xn' 'yc' 'yp' 'zr' 2016-05-21 15:21:22.326724 477 '7a' 'ap' 'bl' 'fl' 'g7' 'ko' 'ma' 'qi' 'ri' 'rp' 'y5' 'yo' 2016-05-21 16:21:22 .326724 478'an''dh''do''hs''hv''ia''ic''ne''of''oi''oq''pe''pg''q9''r5''rk'
```

`a` `d` `do` `s` `a` `c` `e` `o` `o` `oq` `pe` `pg` `q9`

```
'sc' 'sf' 'sh' 'ta' 'tb' 'tq' 'um' 'wb' 'wj' 'wm' 'wq' 'wt' 'yi' 'ym' 2016-05-21 17 :21:22.326724 479 'am' 'aw' 'ay' 'bj' 'df' 'eb' 'eo' 'eq' 'et' 'ey' 'f9' 'fo' 'g0' 'gg' 'h4' 'hq' 'in' 'k4' 'k7' 'kb' 'kl' 'my' 'nt' 'o3' 'og' 'pc' 'q4' 'qg' 'qi' 'qm' 'qy' 'ri' 'rv ' 's9' 'sv' 'tl' 'ue' 'uo' 'v6' 'wb' 'wt' 'wx' 'xi' 'xu' 2016-05-21 18:21:22.326724 480 '1l' 'e2' 'e4' 'eo' 'ep' 'fd' 'ha' 'hp' 'hx' 'io' 'iu' 'jr' 'jx' 'k4' 'l8' 'nb' 'oa' 'om' 'on' 'ow' 'p2' 'qh' 'qp' 'qz' 'ra' 'rz' 'sy' 'tk' 'tt' 'ul' 'uq' 'vm' 'wt ' 'xg' 'xn' 'ya' 'yf' 'yw' 'yx' 'zp' 2016-05-21 19:21:22.326724 481 '3k' 'ag' 'ak' 'bi' 'bl' 'bw' 'by' 'ch' 'cm' 'dw' 'e1' 'e2' 'ed' 'ej' 'ek' 'er' 'eu' 'ez' 'f8' 'fd' 'fi' 'fl' 'gi' 'gm' 'gx' 'gy' 'h2' 'h8' 'hl' 'hn' 'ij' 'ip' 'iq ' 'it' 'jb' 'jl' 'jn' 'k7' 'kh' 'kl' 'kn' 'kt' 'nh' 'nk' 'pa' 'pe' 'pg' 'pp' 'q5' ' q7' 'qi' 'qk' 'ql' 'qs' 'r8' 'ri' 'rj' 'rl' 'rw' 'rx' 'so' 'tb' 'tj' 'tm' 'to' 'tu' 'tv' 'tz' 'u4' 'ue' 'ul' 'uv' 'v1' 'vj' 'vy' 'wc' 'wr' 'wt' 'wx' 'wz' 'xh' 'xj' 'xp ' 'xt' 'y4' 'yb' 'yf' 'ym' 'yo' 'yq' 'yy' 'zp' 'zq' 'zt' 2016-05-21 20:21:22.326724 482 '7r' 'a8' 'aa' 'ag' 'bo' 'bp' 'c7' 'd0' 'd6' 'e5' 'er' 'fc' 'ff' 'go' 'ha' 'hs' 'jj' 'jq' 'ki' 'lc' 'le' 'no' 'pf' 'qc' 'qh' 'qq' 'qs' 'qv' 'rf' 'rj' 'rx' 'su' 'ta ' 'ti' 'tu' 'tv' 'ty' 'ug' 'un' 'up' 'vb' 'vi' 'wp' 'wu' 'wz' 'xt' 'y0' 'yd' 'yu' 2 016-05-21 21:21:22.326724 483 'ad' 'af' 'aj' 'am' 'aq' 'ba' 'bo' 'c0' 'c5' 'cx' 'da' 'dc' 'dk' 'ed' 'ek' 'en' 'eo' 'ep' 'ew' 'fb' 'g4' 'gd' 'h2' 'hm' 'ho' 'hy' 'ib' 'if' 'io' 'ir' 'iv' 'iz' 'jc ' 'jp' 'jt' 'kr' 'lo' 'me' 'na' 'nc' 'nh' 'o6' 'ok' 'oq' 'or' 'ow' 'pn' 'ps' 'q6' ' qa' 'qj' 'qo' 'qx' 'r2' 'r6' 'rd' 're' 'rg' 'rw' 'ta' 'tk' 'uj' 'uo' 'vn' 'wc' 'wh' 'wj' 'wl' 'wu' 'wv' 'ww' 'wx' 'xe' 'xl' 'xn' 'xo' 'xs' 'yb' 'yl' 'yp' 'yw' 'zg' 'zq ' 'zr' 'zu' 'zx' 'zy' 2016-05-21 22:21:22.326724 484 '39' 'a9' 'ag' 'ap' 'ax' 'b9' 'c3' 'dn' 'e4' 'ea' 'f7' 'f9' 'g2' 'gi' 'h4' 'ht' 'ie' 'ij' 'ir' 'is' 'it' 'jd' 'jj' 'jv' 'kp' 'kt' 'kv' 'lh' 'ln' 'ls' 'mg' 'mh' 'nc ' 'nh' 'o0' 'o2' 'od' 'ox' 'pb' 'pn' 'po' 'pz' 'q1' 'q8' 'qc' 'qd' 'qf' 'qh' 'qi' ' qk' 'qz' 'rd' 'rg' 'ro' 'rz' 's7' 'sa' 'sf' 'sn' 'sw' 'tk' 'tu' 'tw' 'u7' 'uu' 'vh' 'wa' 'wd' 'wk' 'wr' 'wu' 'wy' 'wz' 'xh' 'xm' 'xt' 'yb' 'yi' 'yj' 'yn' 'yr' 'z1' 'z8 ' 'zn' 2016-05-21 23:21:22.326724 485 '4g' '8w' 'ab' 'aq' 'at' 'bc' 'bi' 'c7' 'cb' 'cj' 'cs' 'd2' 'd3' 'di' 'dm' 'dx' 'dz' 'ed' 'ex' 'fj' 'gs' 'h1' 'h6' 'he' 'hj' 'hr' 'i1' 'ia' 'ie' 'il' 'ix' 'iy' 'j2 ' 'jd' 'jo' 'jy' 'kx' 'la' 'lv' 'ma' 'mh' 'mp' 'mt' 'n9' 'na' 'nf' 'ng' 'np' 'o7' ' ob' 'on' 'ou' 'ov' 'p9' 'pg' 'po' 'pq' 'q0' 'q4' 'q5' 'qc' 'qj' 'qp' 'qq' 'qt' 'ra' 'rb' 'rq' 'ru' 'sl' 'sp' 't8' 'ta' 'te' 'tl' 'tz' 'u1' 'ud' 'ui' 'uv' 'uw' 'vf' 'vt ' 'vu' 'vz' 'w0' 'w7' 'wc' 'wg' 'wh' 'wq' 'wr' 'wz' 'y6' 'y7' 'ye' 'yh' 2016-05-22 00:21:22.326724 486 '1t' 'a7' 'aj' 'au' 'ca' 'cn' 'cw' 'dg' 'dp' 'ec' 'ei' 'en' 'ew' 'ez' 'f3' 'f8' 'hp' 'ht' 'hw' 'is' 'iv' 'jd' 'ji' 'kn' 'l4' 'lq' 'lz' 'm7' 'o6' 'oj' 'oz' 'p4' 'p7 ' 'po' 'pp' 'q2' 'qa' 'qj' 'qo' 'qt' 'qv' 'qw' 'qy' 'ra' 'rd' 'ri' 'rn' 'rr' 'ry' ' s7' 'st' 'sz' 'tg' 'to' 'tu' 'tx' 'w2' 'w4' 'w5' 'wd' 'we' 'wg' 'wo' 'ws' 'xm' 'y5' 'yf' 'yl' 'ym' 'yr' 'yz' 2016-05-22 01:21:22.326724 487 '1y' '4f' 'ao' 'bv' 'co' 'cq' 'dd' 'df' 'dy' 'eq' 'eu' 'ex' 'gg' 'gm' 'gr' 'hm' 'iw' 'j9' 'jb' 'jg' 'jo' 'ju' 'k0' 'km' 'lf' 'ng' 'np' 'nw' 'nz' 'od' 'oj' 'or' 'pp ' 'pr' 'pu' 'q5' 'q7' 'q9' 'qc' 'qd' 'qn' 'qx' 'r9' 'rd' 'rk' 'ro' 'sb' 'ta' 'th' ' tv' 'ty' 'tz' 'uq' 'vb' 'wb' 'wj' 'xo' 2016-05-22 02:21:22.326724 488 '2t' '4d' 'bb' 'bd' 'cg' 'co' 'd6' 'db' 'dg' 'dn' 'do' 'dy' 'e1' 'e3' 'e6' 'ec' 'em' 'en' 'ep' 'es' 'ev' 'ew' 'fu' 'fz' 'gc' 'gt' 'hg' 'hl' 'hy' 'id' 'in' 'io' 'ir ' 'iu' 'iw' 'jl' 'jo' 'jp' 'jw' 'k4' 'ke' 'ku' 'ld' 'lg' 'li' 'lj' 'lr' 'ls' 'm7' ' n8' 'o6' 'oi' 'op' 'oy' 'pi' 'pq' 'qk' 'qm' 'qn' 'qp' 'qr' 'qu' 'qv' 'qz' 'r3' 're' 'rj' 'rk' 'rq' 'ru' 'rw' 'rz' 'sh' 'si' 'ta' 'to' 'uq' 'ux' 'vc' 'vr' 'wb' 'wh' 'wn ' 'wo' 'wy' 'xg' 'y7' 'yb' 'yd' 'yo' 2016-05-22 03:21:22.326724 489 '5e' 'a2' 'ag' 'ay' 'dc' 'ef' 'jd' 'mn' 'pl' 'qp' 'wu' 'xd' 2016-05-22 04:21:22 .326724
```

```
490 '1x' '3m' 'a1' 'a5' 'a7' 'al' 'aq' 'ar' 'c8' 'cc' 'cd' 'd0' 'dt' 'e6' 'ei' 'em' 'ez' 'f6' 'fc' 'ff' 'fg' 'fp' 'gm' 'h3' 'ha' 'hg' 'ho' 'hs' 'ib' 'ie' 'il' 'it' 'ix ' 'j3' 'jl' 'jt' 'jv' 'jw' 'kd' 'ki' 'l1' 'lk' 'lr' 'lv' 'm0' 'mx' 'my' 'n6' 'ni' ' o2' 'o4' 'o9' 'om' 'p0' 'p6' 'pi' 'pj' 'q5' 'qa' 'qc' 'qg' 'qp' 'qs' 'qu' 'qw' 'rg' 'rt' 'rz' 'se' 'sj' 'sp' 'su' 'sw' 'te' 'tp' 'tq' 'tt' 'tu' 'tx' 'u3' 'un' 'uo' 'up ' 'uq' 'vc' 'vj' 'vu' 'w2' 'wh' 'wj' 'ws' 'wv' 'ww' 'xg' 'yc' 'yf' 'yv' 'z2' 'zl' ' zw' 'zy' 2016-05-22 05:21:22.326724 491 '68' 'af' 'as' 'at' 'cf' 'ci' 'cx' 'dl' 'dt' 'dv' 'e4' 'ea' 'eg' 'es' 'fd' 'fi' 'fo' 'g1' 'gd' 'gy' 'he' 'hu' 'hw' 'hz' 'i0' 'ia' 'if' 'io' 'it' 'iv' 'iz' 'j0' 'jc ' 'jj' 'jm' 'kb' 'ki' 'kk' 'ku' 'ky' 'lr' 'nv' 'oi' 'om' 'p3' 'pa' 'pt' 'qe' 'qh' ' qj' 'qm' 'qq' 'qs' 'qt' 'qu' 'r3' 'rp' 'rr' 'rw' 'rx' 's2' 'sc' 'sp' 'ti' 'tn' 'tv' 'ty' 'ue' 'uk' 'ul' 'up' 'ut' 'uu' 'uw' 'vf' 'vp' 'w2' 'w7' 'wb' 'wl' 'wq' 'xg' 'yc ' 'yh' 'z3' 2016-05-22 06:21:22.326724 492 '9y' 'a0' 'a6' 'ad' 'aj' 'az' 'bw' 'by' 'cg' 'ci' 'dc' 'dk' 'dm' 'dw' 'e0' 'e4' 'ee' 'ef' 'eg' 'en' 'eu' 'fc' 'fg' 'fm' 'fx' 'g7' 'gm' 'go' 'hw' 'hy' 'i4' 'i7' 'ip ' 'iq' 'ir' 'jr' 'ju' 'jx' 'kr' 'ky' 'la' 'lk' 'lq' 'm9' 'mg' 'mp' 'my' 'n6' 'nv' ' nz' 'o1' 'o3' 'oe' 'oy' 'pj' 'pv' 'pz' 'qg' 'ql' 'qp' 'qt' 'qy' 'r4' 'rf' 'rg' 'rk' 'ro' 'rw' 'ry' 's3' 'sd' 'sf' 'sm' 'tf' 'tg' 'tq' 'tu' 'ty' 'tz' 'ub' 'uc' 'uf' 'um ' 'vi' 'vn' 'wa' 'wc' 'we' 'xo' 'xr' 'xs' 'yb' 'yi' 'yw' 'zn' 'zo' 2016-05-22 07:21 :22.326724 493 '4n' '6a' 'a3' 'a5' 'aa' 'ae' 'ag' 'b9' 'ca' 'cf' 'd1' 'da' 'dr' 'dz' 'ee' 'el' 'et' 'ey' 'fj' 'fs' 'gl' 'hk' 'hl' 'hn' 'ie' 'ih' 'im' 'ix' 'j1' 'jr' 'kf' 'kk' 'lc ' 'lk' 'lp' 'lx' 'mh' 'mt' 'mx' 'my' 'nr' 'nu' 'o6' 'og' 'oo' 'p4' 'p7' 'pj' 'pr' ' q3' 'qc' 'qd' 'qj' 'qk' 'ql' 'qp' 'qt' 'qv' 'qx' 'r8' 're' 'rm' 'rs' 'ru' 'rv' 'sp' 'sw' 'td' 'tk' 'to' 'tw' 'tz' 'u8' 'uf' 'vf' 'vw' 'w7' 'wq' 'wr' 'xe' 'ym' 'yo' 'yr ' 'ys' 'yz' 'zc' 'zn' 'zs' 2016-05-22 08:21:22.326724 494 'av' 'es' 'fl' 'gt' 'he' 'it' 'kp' 'mu' 'nc' 'ol' 'om' 'ph' 'qr' 'ra' 'rk' 'ui' 'vh' 'w6' 'wm' 'ws' 'yu' 'z0' 'zl' 'zm' 2016-05-22 09:21:22.326724 495 '3r' '6o' 'ab' 'ay' 'b3' 'bc' 'bh' 'd8' 'dd' 'df' 'eb' 'ee' 'eh' 'el' 'eu' 'ex' 'fn' 'g3' 'ge' 'gr' 'gz' 'hd' 'ib' 'ie' 'ih' 'il' 'it' 'iu' 'jd' 'jq' 'jt' 'jv' 'li ' 'pc' 'pp' 'qc' 'ql' 'qp' 'qu' 'qx' 'qz' 'ro' 'rq' 'sj' 'sz' 'te' 'tt' 'tu' 'uh' ' uo' 'up' 'us' 'uu' 'ux' 'v7' 'w3' 'wl' 'wn' 'xf' 'xu' 'ya' 'yh' 'yk' 'za' 'zt' 2016 -05-22 10:21:22.326724 496 'a0' 'ai' 'bx' 'ca' 'e2' 'eb' 'ed' 'eg' 'eh' 'eo' 'et' 'hn' 'ix' 'jh' 'ki' 'lm' 'lw' 'm8' 'mb' 'mh' 'mk' 'nc' 'o3' 'o9' 'of' 'qc' 'qe' 'qf' 'qh' 'qi' 'qq' 'qr' 'qz ' 'r2' 'r3' 'rc' 'rh' 'rs' 'rv' 'sr' 'uk' 'up' 'ur' 'uv' 'wm' 'wr' 'wz' 'xd' 'y3' ' ya' 'yv' 'zr' 2016-05-22 11:21:22.326724 497 '7h' '7k' 'bi' 'c8' 'cc' 'cj' 'cs' 'd7' 'dh' 'dl' 'dp' 'dt' 'e9' 'ea' 'eh' 'ei' 'ej' 'el' 'ew' 'fo' 'fp' 'ge' 'gg' 'gi' 'gk' 'h2' 'h7' 'hk' 'hs' 'hy' 'ii' 'j4' 'kd ' 'kh' 'kp' 'ks' 'm2' 'n1' 'n3' 'nk' 'nr' 'od' 'ok' 'om' 'oy' 'pb' 'ph' 'pm' 'pp' ' pt' 'q2' 'q8' 'q9' 'qc' 'qf' 'qg' 'qh' 'qj' 'qk' 'qn' 'qo' 'qq' 'qv' 'qx' 'r4' 'rc' 'rg' 'rj' 's9' 'sb' 'sg' 'sj' 'ss' 't6' 'ta' 'tc' 'tm' 'tv' 'us' 'uu' 'uy' 'w7' 'wf ' 'wh' 'wk' 'wz' 'x2' 'xr' 'ya' 'yc' 'yk' 'yp' 'ys' 'yz' 'z4' 'zg' 'zn' 2016-05-22 12:21:22.326724 498 '6p' 'an' 'aq' 'au' 'br' 'bz' 'c3' 'ca' 'cg' 'cn' 'db' 'dk' 'dq' 'e0' 'e8' 'ek' 'eo' 'er' 'ez' 'fd' 'ft' 'g0' 'gd' 'gh' 'gk' 'gn' 'gr' 'gv' 'gy' 'hb' 'hc' 'he' 'ht ' 'ii' 'ip' 'iu' 'j9' 'jn' 'jo' 'jq' 'jz' 'kh' 'kn' 'ko' 'l3' 'ls' 'lz' 'nh' 'nk' ' ok' 'oy' 'p7' 'pd' 'ph' 'pu' 'pw' 'py' 'q7' 'qa' 'qi' 'qk' 'ql' 'qn' 'qq' 'qr' 'qs' 'qv' 'qx' 'qy' 'rg' 'rs' 'ru' 'sg' 'sl' 'sq' 'sr' 'su' 'ts' 'tt' 'ui' 'um' 'ut' 'uu ' 'v0' 'v5' 'w7' 'wb' 'wc' 'wf' 'wi' 'wm' 'xd' 'xs' 'xz' 'y3' 'y4' 'y9' 'yi' 'yp' ' yx' 'z0' 'zf' 2016-05-22 13:21:22.326724 499 'au' 'cm' 'dj' 'e1' 'eh' 'ey' 'f3' 'fd' 'fg' 'fv' 'hn' 'i0' 'ia' 'jt' 'jy' 'k2' 'll' 'ne' 'o0' 'o2' 'op' 'pa' 'pf' 'qq' 'qx' 'rr' 'rs' 's4' 'sn' 'so' 'sq' 'tc' 'tn ' 'ts' 'ty' 'tz' 'un' 'va' 'vg' 'vj' 'w8' 'wa' 'wb' 'wk' 'wo' 'wp' 'wr' 'x3' 'xx' '
```

```
yj' 'yz' 'z3' 'z7' 'zn' 2016-05-22 14:21:22.326724 500 'a4' 'ae' 'ax' 'bb' 'bg' 'ca' 'ch' 'cq' 'cv' 'dm' 'dn' 'en' 'ep' 'eu' 'ev' 'f0' 'g3' 'gk' 'gm' 'hd' 'ho' 'hp' 'hy' 'ij' 'im' 'iy' 'jl' 'jr' 'jy' 'kj' 'kt' 'ku' 'lp ' 'mo' 'mr' 'mz' 'n4' 'nk' 'oc' 'ol' 'oo' 'os' 'oy' 'oz' 'p8' 'p9' 'ps' 'qb' 'qd' ' qg' 'qi' 'qv' 'qx' 'r1' 'ra' 'rf' 'rg' 'rm' 'ro' 'rr' 'rv' 'rz' 's7' 'sm' 'ss' 'tl' 'tr' 'tu' 'ty' 'u5' 'ui' 'un' 'uq' 'uv' 'vn' 'w1' 'w2' 'w6' 'wd' 'we' 'wg' 'wn' 'wp ' 'wy' 'y2' 'y6' 'yc' 'yd' 'yt' 'yw' 'z8' 'ze' 'zs' 2016-05-22 15:21:22.326724 501 'ca' 'fu' 'hv' 'la' 'mt' 'ov' 'pl' 'q8' 'r3' 'sp' 'sy' 'tg' 'to' 'tv' 'wn' 'x4' 'yh' 'yp' 'ze' 2016-05-22 16:21:22.326724 502 'ag' 'ai' 'az' 'br' 'c2' 'cd' 'ck' 'db' 'du' 'e0' 'e7' 'eb' 'ee' 'em' 'ep' 'eq' 'es' 'eu' 'ex' 'fh' 'fi' 'ga' 'gm' 'gn' 'hj' 'hq' 'if' 'ig' 'ii' 'ix' 'jk' 'kd' 'kg ' 'kk' 'kr' 'kt' 'ku' 'lx' 'mp' 'mq' 'nx' 'o9' 'oa' 'om' 'oq' 'p5' 'pd' 'pr' 'pu' ' pw' 'q3' 'qa' 'qd' 'qe' 'qf' 'qi' 'qj' 'ql' 'qn' 'qo' 'qr' 'qt' 'qu' 'qv' 'qx' 'rc' 'rf' 'rl' 'rm' 'rn' 'rp' 'rr' 's7' 'se' 'st' 'sx' 't8' 'to' 'u1' 'ua' 'uq' 'ux' 'w6 ' 'w8' 'wf' 'wt' 'xb' 'xf' 'xk' 'xn' 'y3' 'ym' 'yp' 'yz' 'zi' 'zk' 2016-05-22 17:21 :22.326724 503 '40' '6a' '8j' 'am' 'bf' 'dp' 'dz' 'ew' 'gh' 'he' 'hh' 'ib' 'ii' 'iq' 'is' 'iu' 'kt' 'mf' 'oh' 'or' 'p8' 'pa' 'pb' 'pi' 'qc' 'qo' 'qp' 'qq' 'qs' 'qt' 'qu' 'r4' 'rf ' 'rl' 'sd' 'sl' 't4' 'tb' 'ua' 'ue' 'ut' 'wh' 'wm' 'y0' 'y6' 2016-05-22 18:21:22.3 26724 504 '1b' '42' 'a7' 'ab' 'ak' 'ap' 'at' 'av' 'ay' 'b0' 'b9' 'bb' 'bp' 'bu' 'bz' 'cq' 'da' 'de' 'dn' 'e0' 'eb' 'ef' 'eg' 'ek' 'eq' 'er' 'eu' 'ey' 'fn' 'ft' 'gg' 'h4' 'hk ' 'hl' 'i7' 'ig' 'ik' 'ip' 'ir' 'iu' 'iw' 'jr' 'jw' 'jx' 'kg' 'lc' 'lg' 'm0' 'na' ' np' 'om' 'on' 'oz' 'pg' 'pn' 'ps' 'pt' 'pz' 'q3' 'q6' 'qa' 'qb' 'ql' 'qq' 'qt' 'qv' 'qw' 'qy' 'r8' 'rf' 'ri' 'rk' 'rl' 'rw' 'sg' 'si' 'sp' 'sw' 'ta' 'th' 'ua' 'uj' 'uu ' 'uv' 'uz' 'vj' 'vk' 'vm' 'wc' 'wf' 'wh' 'wn' 'wo' 'ww' 'xb' 'xk' 'xt' 'xw' 'y7' ' ye' 'yl' 'yt' 'yw' 'z4' 'z7' 'zc' 'zw' 2016-05-22 19:21:22.326724 505 '27' '4g' 'a2' 'al' 'bp' 'ca' 'cp' 'da' 'dt' 'e8' 'ee' 'ef' 'eg' 'ej' 'eq' 'eu' 'ev' 'fe' 'gn' 'gq' 'gy' 'i5' 'ic' 'il' 'io' 'ir' 'iw' 'iz' 'j2' 'kz' 'l2' 'l8' 'lh ' 'ln' 'lt' 'np' 'ns' 'oi' 'oj' 'or' 'ph' 'pr' 'pt' 'qa' 'qh' 'qi' 'qs' 'qt' 'qu' ' r1' 'rd' 'ry' 's8' 'sj' 'sk' 'sl' 'sq' 'td' 'te' 'tg' 'tj' 'tq' 'tx' 'u0' 'ub' 'ul' 'uu' 'ux' 'uy' 'v0' 've' 'vg' 'vk' 'wa' 'wj' 'ws' 'wu' 'yb' 'yd' 'yi' 'yk' 'yo' 'yr ' 'ys' 'zp' 2016-05-22 20:21:22.326724 506 'am' 'as' 'b1' 'd3' 'db' 'dl' 'ea' 'ed' 'ee' 'el' 'em' 'ep' 'er' 'ew' 'ez' 'f4' 'fm' 'go' 'h9' 'he' 'hl' 'i0' 'ie' 'ii' 'iz' 'ji' 'kl' 'kn' 'lc' 'lr' 'm7' 'mb' 'mt ' 'my' 'no' 'nu' 'oo' 'or' 'ov' 'ox' 'pe' 'pq' 'q7' 'qc' 'qd' 'qi' 'qj' 'qo' 'qr' ' qs' 'qv' 'qw' 'r0' 'r8' 're' 'rm' 'rn' 'rp' 's0' 'so' 'sp' 'sw' 'sy' 'te' 'tg' 'tl' 'tr' 'uq' 'uz' 'vk' 'wk' 'wl' 'wp' 'wq' 'wr' 'wu' 'ww' 'xs' 'y0' 'yb' 'yn' 'yr' 'ys ' 'yt' 'yy' 'zh' 'zr' 2016-05-22 21:21:22.326724 507 '18' '5j' '6y' 'ax' 'bw' 'c5' 'de' 'dh' 'dl' 'do' 'dx' 'ek' 'el' 'en' 'et' 'ez' 'f1' 'fe' 'fw' 'ge' 'h1' 'h9' 'ha' 'hb' 'hl' 'it' 'jy' 'kl' 'ky' 'lo' 'nr' 'o3' 'o9 ' 'p0' 'pe' 'pg' 'ph' 'q1' 'q5' 'qd' 'qg' 'qh' 'qi' 'qj' 'qp' 'qq' 'qr' 'qv' 'qx' ' r0' 'rd' 're' 'rj' 'rm' 'rn' 'rq' 'rv' 'se' 'sv' 'to' 'tz' 'uo' 'v1' 'vm' 'vr' 'wa' 'we' 'wf' 'wh' 'wp' 'wt' 'wy' 'xe' 'xh' 'xz' 'y6' 'yn' 'zm' 'zy' 2016-05-22 22:21:2 2.326724 508 'bb' 'bq' 'c2' 'cw' 'cy' 'db' 'dd' 'f3' 'fl' 'fn' 'id' 'ig' 'jb' 'kc' 'kl' 'lp' 'lx' 'mh' 'o0' 'pk' 'qi' 'qx' 'rq' 've' 'w8' 'wd' 'x1' 'y4' 'ye' 'zm' 2016-05-22 23 :21:22.326724
```

ii. Execute the following statements:

```
EXPLAIN (costs off) SELECT id, d, d <=> '2016-05-16 14:21:25' FROM tsts WHERE t @@ 'wr&qh' ORDER BY d <=> '2016-05-16 14:21:25' LIMIT 5;
                                    QUERY PLAN
-----------------------------------------------------------------------------------
 Limit
   ->  Index Scan using tsts_idx on tsts
         Index Cond: (t @@ '''wr'' & ''qh'''::tsquery)
         Order By: (d <=> '2016-05-16 14:21:25'::timestamp without time zone)
(4 rows)
```

iii. Execute the following query:

```
SELECT id, d, d <=> '2016-05-16 14:21:25' FROM tsts WHERE t @@ 'wr&qh' ORDER BY d <=> '2016-05-16 14:21:25' LIMIT 5;
```

The following result is returned:

```
 id  |             d              |   ?column?
-----+----------------------------+---------------
 355 | 2016-05-16 14:21:22.326724 |      2.673276
 354 | 2016-05-16 13:21:22.326724 |   3602.673276
 371 | 2016-05-17 06:21:22.326724 |  57597.326724
 406 | 2016-05-18 17:21:22.326724 | 183597.326724
 415 | 2016-05-19 02:21:22.326724 | 215997.326724
(5 rows)
```

Because posting trees have a fixed-length right border and fixed-length non-leaf posting items, a bug may occur in RUM when an index is created by sorting additional information that is passed by reference. The `rum_tsvector_hash_addon_ops` operator class stores the hash values of `tsvector` lexemes and values in an addon field. This operator class does not support prefix search. The `rum_tsquery_ops` operator class applies to the `tsquery` data type and stores the branches of the query tree as additional information. Example: i. Prepare data:

```
CREATE TABLE test_array (i int2[]); INSERT INTO test_array VALUES ('{}'), ('{0}'), ('{1,2,3,4}'), ('{1,2,3}'), ('{1,2}' ), ('{1}'); CREATE INDEX idx_array ON test_array USING rum (i rum_anyarray_ops);
```

ii. Execute the following statements:

```
SET enable_seqscan TO off; EXPLAIN (COSTS OFF) SELECT * FROM test_array WHERE i && '{1}' ORDER BY i <=> '{1}' ASC;
                QUERY PLAN
------------------------------------------
 Index Scan using idx_array on test_array
   Index Cond: (i && '{1}'::smallint[])
   Order By: (i <=> '{1}'::smallint[])
(3 rows)
```

iii. Execute the following query:

```
SELECT * FROM test_array WHERE i && '{1}' ORDER BY i <=> '{1}' ASC;
```

The following result is returned: `i`

```
-----------
 {1}
 {1,2}
 {1,2,3}
 {1,2,3,4}
(4 rows)
```

|   | anyarray |
|---|---|
| <@ |   |

using the `<=>` operator. Example: i. Prepare data:

```
CREATE TABLE test_array (i int2[]); INSERT INTO test_array VALUES ('{}'), ('{0}'), ('{1,2,3,4}'), ('{1,2,3}'), ('{1,2}' ), ('{1}'); CREATE INDEX idx_array ON test_array USING rum (i rum_anyarray_ops);
```

ii. Execute the following statements:

```
SET enable_seqscan TO off; EXPLAIN (COSTS OFF) SELECT * FROM test_array WHERE i && '{1}' ORDER BY i <=> '{1}' ASC;
                QUERY PLAN
------------------------------------------
 Index Scan using idx_array on test_array
   Index Cond: (i && '{1}'::smallint[])
   Order By: (i <=> '{1}'::smallint[])
(3 rows)
```

iii. Execute the following query:

```
SELECT * FROM test_array WHERE i && '{1}' ORDER BY i <=> '{1}' ASC;
```

The following result is returned: `i`

```
-----------
 {1}
 {1,2}
 {1,2,3}
 {1,2,3,4}
(4 rows)
```

The `rum_anyarray_addon_ops` operator class stores `anyarray` elements and values in an addon field.

**Uninstall the RUM extension**

You can execute the following SQL statement to uninstall the RUM extension.

```
DROP EXTENSION rum;
```

### 12.8 PGVector

PGVector is a high-performance database extension for vector similarity searches and supports multiple algorithms and data types. You can use this extension to efficiently store and query vector embeddings. This topic describes the background information, implementation principles, usage, and references of PGVector.

**Background information**

As data science and machine learning develop rapidly, vector computing has become one of the most common computing tasks in the big data field. PolarDB for PostgreSQL integrates the PGVector extension to improve the performance of high-dimensional vector computing. The extension allows you to customize data types and storage methods. High-dimensional storage, including major text embedding models, is used for data input and output. PGVector supports vectors with up to 16000 dimensions.

**Usage notes**

The cross-node parallel execution feature allows you to use the sort clause to traverse highdimensional vectors. The cross-node parallel execution feature does not support index queries.

**How it works**

Like the PASE extension,PGVector uses Inverted File with Flat Compression (IVFFlat) indexes. The IVFFlat algorithm is an approximate nearest neighbor search algorithm based on inverted indexes. It is used in PGVector for vector similarity searches. IVFFlat works by dividing the vector space into regions, with each region encompassing certain vectors. Given a query vector, the algorithm first identifies the region it belongs to and then performs a local search within that region to find the closest match based on inverted indexes. IVFFlatis a simplified Inverted File System with Asymmetric Distance Computation (IVFADC) algorithm. IVFFlat is suitable for business scenarios that require high precision but can tolerate up to 100 milliseconds taken for queries. IVFFlathas the following advantages compared with other algorithms: high recall rate, high precision, simple algorithm and parameters, and low storage usage. The PGVector extension is implemented based on the extension mechanism of PolarDB for PostgreSQL. The PGVector extension is written in the C programming language and supports a variety of vector computing algorithms and data types. The following section describes the process of how the IVFFlat algorithm works:
1. IVFFlat uses a clustering algorithm such as k-means to divide vectors in the high-
dimensional space into clusters based on implicit clustering properties. This way, each cluster has a centroid.
2. IVFFlat traverses the centroids of all clusters to identify the n centroids that are nearest to
the vector that you want to query.
3. IVFFlat traverses and sorts all vectors in the clusters to which the identified n centroids
belong. Then, IVFFlat obtains the nearest k vectors.

**Usage**

The PGVector extension can be used to perform sequential or indexed search for highdimensional vectors. For more information, see**Examples**. Recall rate and query performance In versions earlier than 0.5.0, the PGVector extension uses the IVFFlat indexing method, which is known for its fast building speed. The PGVector extension enhances query performance by using the IVFFlat indexing method. However, the recall rate is moderate, and certain memory is used. As of version 0.5.0, the PGVector extension supports both IVFFlat and Hierarchical Navigable Small World (HNSW) indexes. The HNSW indexing method provides better query performance and a higher recall rate than the IVFFlat indexing method, but it builds more slowly and uses more memory. To effectively query vector data based on vector indexes, you must balance the advantages and disadvantages related to query performance and recall rate. The following section describes how to configure the parameters for the two indexing methods to enhance recall rates. HNSW `m` : the number of bidirectional links (or paths) connected to each index element. Default value: 16. Valid values: 2 to 100. To increase the recall rate, you can specify a large number for this parameter. However, a large number of bidirectional links significantly extends the index generation time and may negatively affect query performance. `ef_construction` : the number of neighbors that you want to check when an element is added to the index. Default value: 64. Valid values: 4 to 100. You can increase the recall rate by increasing the value of this parameter. However, the index building time may be extended. The value of this parameter must be at least twice the value of the `m` parameter.

```
CREATE TABLE vecs (id int PRIMARY KEY, embedding vector(1536)); CREATE INDEX ON vecs USING hnsw(embedding vector_l2_ops) WITH (m=16, ef_construction=64);
```

If you use the HNSW indexing method, you must specify an operator class. For example, if you want to use cosine similarity as the metric for HNSW indexes, execute the following statement:

```
CREATE INDEX ON vecs USING hnsw(embedding vector_cosine_ops);
```

You can use the default index building configuration items to optimize the index building time. If the expected recall rate is not achieved on your dataset, increase the value of the `ef_construction` parameter. Then, adjust the value of the `m` parameter. To increase the recall rate, you can specify a larger value for the `hnsw.ef_search` parameter. For example, you can set the value to `100` . A larger value represents a higher recall rate. IVFFlat `lists` : the number of centroids that are used in the clustering algorithm for all vectors in the PGVector sampling table.

```
CREATE INDEX ON vecs USING ivfflat(embedding) WITH (lists=100);
```

For more information about the index and parameters, see the README module in the open source code.

**Examples**

1. Create the PGVector extension.

```
CREATE EXTENSION vector;
```

2. Create a table.

```
CREATE TABLE t (val vector(3));
```

3. Insert data into the table.

```
INSERT INTO t (val) VALUES ('[0,0,0]'), ('[1,2,3]'), ('[1,1,1]'), (NULL);
```

4. Create a vector index.

```
CREATE INDEX ON t USING ivfflat (val vector_ip_ops) WITH (lists = 1);
```

5. Find similar vectors.

```
SELECT * FROM t ORDER BY val <#> '[3,3,3]';
```

Sample result:

```
   val
---------
 [1,2,3]
 [1,1,1]
 [0,0,0]
(3 rows)
```

In `val vector_ip_ops` , val is the column on which you want to create an index, and `vector_ip_ops` is the vector operator provided byPolarDB for PostgreSQL to calculate the similarities between vectors. This vector operator supports the calculation of dot product distance, cosine similarity, and Euclidean distance between vectors. `WITH (lists = 1)` indicates that only one region is created, which means that all vectors are assigned to the same region. In actual vector query scenarios, specify the number of regions based on the amount of data and query performance.

**References**

For more information about the embedding process of vectors, see the output of Chinese mainland and international text embedding models.

### 12.9 AGE (graph database)

PolarDB for PostgreSQL provides an extension to implement graph databases. You can query graphs in a database by using Cypher. This topic describes the basic concepts and usage of graph databases.

**Terms**

Graph: a non-linear data structure that consists of nodes and edges. It represents a set of entities and their interconnections. Node: the fundamental element of a graph. A node represents an entity such as a user, product, or location. A node can contain properties (data fields) that describe the features or behaviors of the entity. Edge: the relationship or connection between nodes. An edge can be directed or undirected. An edge can contain properties that describe the features of the relationship, such as the type and weight of the relationship. Property: additional information of a node or an edge, such as the name and creation time of a node, or the weight of an edge. It allows you to add more detailed descriptions of nodes and edges. Graph Query Language (GQL): the customized language that is used to interact with graph databases. GQL can be used to query, analyze, and manage graph data. This extension uses Cypher to query data. You can combine Cypher with native PostgreSQL languages, such as SQL and PL/pgSQL, to execute queries. Common query statements include `MATCH` , `WITH` , `RETURN` , `ORDER BY` , `SKIP` , `LIMIT` , `CREATE` , `DELETE` , `SET` , `REMOVE` , and `MERGE` .

**Usage**

**Install the extension**

Use a privileged account to execute the following statement:

```
CREATE EXTENSION age;
```

Add the extension to the search path and pre-load libraries of the database or user. Compatibility issues may occur when you use Data Management (DMS) to configure the `search_path` . In such cases, you can use **PolarDB-Tools** to execute related statements. Load the extension to a session:

```
SELECT * FROM ag_catalog.get_cypher_keywords() limit 0;
```

You can also add `ag_catalog` to `search_path` to simplify queries.

```
SET search_path = ag_catalog, "$user", public;
```

Permanently load the extension:

```
ALTER DATABASE <dbname> SET search_path = public,ag_catalog; ALTER USER <username> SET search_path = public,ag_catalog; ALTER DATABASE <dbname> SET session_preload_libraries TO 'age'; ALTER USER <username> SET session_preload_libraries TO 'age';
```

After executing the preceding statements, reconnect to the cluster to load the extension. If a standard user wants to use this extension, you can perform the following operations:
1. Grant the `USAGE` permissions.

```
GRANT USAGE ON SCHEMA ag_catalog TO <username>;
```

2. Grant the CREATE permissions if the standard user just creates graphs.

```
GRANT CREATE ON DATABASE <dbname> TO <username>;
```

**Create a graph**

Use the `create_graph` function in the `ag_catalog` namespace to create a graph.

```
SELECT create_graph('graph_name');
```

**Create vertices and edges**

Use the `CREATE` clause to create a single vertex that contains labels and properties.

```
SELECT * FROM cypher('graph_name', $$
    CREATE (:label {property:"Node A"})
$$) as (v agtype); SELECT * FROM cypher('graph_name', $$
    CREATE (:label {property:"Node B"})
$$) as (v agtype);
```

Create an edge between two nodes and define the properties of the edge.

```
SELECT * FROM cypher('graph_name', $$
    MATCH (a:label), (b:label)
    WHERE a.property = 'Node A' AND b.property = 'Node B'
    CREATE (a)-[e:RELTYPE {property:a.property + '<->' + b.property}]->(b)
    RETURN e
$$) as (e agtype);
```

**Query nodes**

Execute a query to find connected nodes.

```
SELECT * from cypher('graph_name', $$
        MATCH (V)-[R]-(V2)
        RETURN V,R,V2
$$) as (V agtype, R agtype, V2 agtype);
```

**Delete a graph**

Use the `drop_graph` function in the `ag_catalog` namespace to delete a graph.

```
SELECT drop_graph('graph_name', true);
```

**Uninstall the extension**

```
DROP EXTENSION age;
```

After you uninstall the extension, reset the search path and pre-load libraries.

```
ALTER DATABASE <dbname> RESET search_path; ALTER USER <username> RESET search_path; ALTER DATABASE <dbname> RESET session_preload_libraries; ALTER USER <username> RESET session_preload_libraries;
```

### 12.10 hypopg (hypothetical indexes)

**indexes)**

The hypopg extension helps you check whether an index can improve one or more queries.

**Overview**

The hypopg extension is an open source third-party extension supported by PolarDB for PostgreSQL and PolarDB for PostgreSQL (Compatible with Oracle). Hypothetical indexes created by the hypopg extension do not exist in any system tables. Instead, they are stored in the private memory of your connection. Because hypothetical indexes do not physically exist in any files, they are used only by simple EXPLAIN statements that do not include the ANALYZE option. Hypothetical indexes are not real indexes and do not consume CPU, disk, or other resources. The hypopg extension supports the following index types: btree: B-tree indexes. brin: Block Range Indexes (BRIN). hash: Hash indexes. bloom: Bloom indexes. You must install the bloom extension first.

**Usage notes**

Before you use the hypopg extension, you must determine the following: The queries to optimize. The index types to try.

**Usage**

1. Install the extension.
i. Install the hypopg extension.

```
CREATE EXTENSION hypopg;
```

ii. Check whether the hypopg extension is installed.

```
\dx hypopg
```

Sample result:

```
                  List of installed extensions
  Name  | Version | Schema |             Description
--------+---------+--------+-------------------------------------
 hypopg | 1.3.1   | public | Hypothetical indexes for PostgreSQL
(1 row)
```

The result shows that version 1.3.1 of the hypopg extension is installed. You can also execute an SQL statement to query the pg_extension table to check whether the hypopg extension is installed. Example:

```
SELECT * FROM pg_extension WHERE extname = 'hypopg';
```

Sample result:

```
extname | extowner | extnamespace | extrelocatable | extversion | extconf ig | extcondition --------+----------+--------------+----------------+------------+---------- +--------------
 hypopg |       10 |        2200 | t               | 1.3.1      |
```

|

```
(1 row)
```

2. Configure parameters as described in the following table.

| Parameter | Description |
|---|---|
| hypopg.enabled | The default value is on. Valid values: on: Enables the hypopg extension. off: Disables the hypopg extension. Note When the hypopg extension is disabled, hypothetical indexes are not used. However, existing hypothetical indexes are not deleted. |

| hypopg.use real oids _ _ | The default value is off. Valid values: off: The hypopg extension does not use real object identifiers (OIDs). Instead, it selects an identifier from a free range. These identifiers are reserved by the database for future use. The free identifier range is dynamically calculated when the hypopg extension is first used. This method has the advantage of being usable on standby servers and does not cause issues. Note The disadvantage of this setting is that you cannot have more than approximately 2,500 hypothetical indexes when this parameter is set to off. If the number of existing hypothetical indexes exceeds the maximum limit, creating a new one takes a long time. To resolve this issue, call the hypopg reset() _ function. on: The hypopg extension uses real OIDs. Setting the hypopg.use real oids parameter to on prevents the long creation _ _ time that occurs when the maximum number of indexes is exceeded. The hypopg extension requests real identifiers. This method requires more lock resources and cannot be used on standby servers, but allows all identifiers to be used. Note Modifying this parameter does not require you to reset hypothetical index identifiers. Real and non-real identifiers can coexist. |
|---|---|

3. Uninstall the hypopg extension.

```
DROP EXTENSION hypopg;
```

**Examples**

1. Create a table and insert data. The table has no indexes. Example:

```
CREATE TABLE hypo (id integer, val text); INSERT INTO hypo SELECT i, 'line ' || i FROM generate_series(1, 100000) i; VACUUM ANALYZE hypo;
```

You can check whether an index can improve a simple query. Example:

```
EXPLAIN SELECT val FROM hypo WHERE id = 1;
```

Sample result:

```
                       QUERY PLAN
--------------------------------------------------------
 Seq Scan on hypo  (cost=0.00..1791.00 rows=1 width=10)
   Filter: (id = 1)
(2 rows)
```

The query performs a sequential scan because the hypo table has no index.
2. Create a hypothetical index. Example:

```
SELECT * FROM hypopg_create_index('CREATE INDEX ON hypo (id)');
```

Sample result:

```
indexrelid | indexname ------------+----------------------
      13925 | <13925>btree_hypo_id
(1 row)
```

The following table describes the parameters.

| Parameter | Description |
|---|---|
| 13925 | The identifier of the hypothetical index. |
| <13925>btree hypo id _ _ | The name of the generated hypothetical index. |

A simple B-tree index in the id column accelerates this query. The `hypopg_create_index()` function accepts any standard `CREATE INDEX` statement and creates a hypothetical index for each statement. Any other statements passed to the function are ignored. The identifier is dynamically generated. In this example, it is 13925.
3. Execute an EXPLAIN statement to determine whether the database uses the index.
Example:

```
EXPLAIN SELECT val FROM hypo WHERE id = 1;
```

Sample result:

```
                                     QUERY PLAN
------------------------------------------------------------------------------------
 Index Scan using "<13925>btree_hypo_id" on hypo  (cost=0.04..8.06 rows=1 width=10)
   Index Cond: (id = 1)
(2 rows)
```

The query plan indicates that the database uses this index.
4. Execute an EXPLAIN ANALYZE statement to check whether the database uses the
hypothetical index during actual execution. Example:

```
EXPLAIN ANALYZE SELECT val FROM hypo WHERE id = 1;
```

Sample result:

```
                                            QUERY PLAN
--------------------------------------------------------------------------------------- ----------
 Seq Scan on hypo  (cost=0.00..1791.00 rows=1 width=10) (actual time=0.030..15.439 ro
ws=1 loops=1)
   Filter: (id = 1)
   Rows Removed by Filter: 99999
 Planning Time: 0.066 ms
 Execution Time: 15.492 ms
(5 rows)
```

During actual execution, the database does not use the hypothetical index.

**Hypothetical index operations**

The hypopg extension also provides some useful functions and views. hypopg_list_indexes view: Lists all created hypothetical indexes. Example:

```
SELECT * FROM hypopg_list_indexes;
```

Sample result:

```
 indexrelid |      index_name      | schema_name | table_name | am_name
------------+----------------------+-------------+------------+---------
      13925 | <13925>btree_hypo_id | public      | hypo       | btree
(1 row)
```

hypopg() function: Lists all created hypothetical indexes in the same format as pg_index. Example:

```
SELECT * FROM hypopg();
```

Sample result:

```
      indexname       | indexrelid | indrelid | innatts | indisunique | indkey | indc
ollation | indclass | indoption | indexprs | indpred | amid ----------------------+------------+----------+---------+-------------+--------+------- ------+----------+-----------+----------+---------+------
 <13925>btree_hypo_id |      13925 |    16450 |       1 | f           | 1      | 0
| 1978     |           |          |         |  403
(1 row)
```

hypopg_get_indexdef(oid) function: Retrieves the actual CREATE INDEX command from the hypothetical index identifier. Example:

```
SELECT index_name, hypopg_get_indexdef(indexrelid) FROM hypopg_list_indexes;
```

Sample result:

```
      index_name      |             hypopg_get_indexdef
----------------------+----------------------------------------------
 <13925>btree_hypo_id | CREATE INDEX ON public.hypo USING btree (id)
(1 row)
```

hypopg_relation_size(oid) function: Estimates the size of a hypothetical index. Example:

```
SELECT index_name, pg_size_pretty(hypopg_relation_size(indexrelid)) FROM hypopg_list_indexes;
```

Sample result:

```
      index_name      | pg_size_pretty
----------------------+----------------
 <13925>btree_hypo_id | 2544 kB
(1 row)
```

hypopg_drop_index(oid) function: Deletes the hypothetical index with the specified identifier. Example:

```
SELECT hypopg_drop_index(13925);
```

Sample result:

```
 hypopg_drop_index
-------------------
```

`t`

```
(1 row)
```

hypopg_reset() function: Deletes all hypothetical indexes. Example:

```
SELECT hypopg_reset();
```

Sample result:

```
 hypopg_reset
-------------- (1 row)
```

### 12.11 ip4r (network address storage)

**storage)**

This topic describes the background information, data types, and usage of the `ip4r` extension.

**Background information**

`ip4r` is a third-party extension supported by PolarDB for PostgreSQL. It provides data types for storing IPv4 and IPv6 addresses. Unlike the built-in `inet` and `cidr` data types in PostgreSQL, `ip4r` supports index scans for the contains operator `>>=` . In addition, `ip4r` has the following advantages over the built-in network data types of PostgreSQL: Clearer semantics: It distinguishes between a **network block** and a **specific IP address**
**within a network block**.
Lower overhead: PostgreSQL uses variable-length data types to store IPv6 data. This creates significant overhead when you need to store only IPv4 data. In contrast, `ip4r` uses fixed-length data types for single addresses.

**Data types**

`ip4r` provides a variety of data types to store and represent IPv4 or IPv6 data:

| Data type | Description |
|---|---|
| ip4 | A single IPv4 address. |
| ip4r | An arbitrary IPv4 address range. |
| ip6 | A single IPv6 address. |
| ip6r | An arbitrary IPv6 address range. |
| ipaddress | A single IPv4 or IPv6 address. |
| iprange | An arbitrary IPv4 or IPv6 address range. |

**Single-address data types and type conversions**

The following three data types are used to store single IP addresses: `ip4` : Accepts input in the `nnn.nnn.nnn.nnn` format. The data is stored as a 32-bit unsigned integer. `ip6` : Accepts input in the standard hexadecimal format for an IPv6 address. The data is stored as two 64-bit values. `ipaddress` : Accepts input in the `ip4` or `ip6` format. For these three data types, `ip4r` provides the following type conversion rules: In the following table, `ipX` represents any of the three data types described above.

| Source type | Target type | Format |
|---|---|---|
| ipX | text | text(ipX) or ipX::text (explicit) |
| text | ipX | ipX(text) or text::ipX (explicit) |
| ipX | cidr | cidr(ipX) or ipX::cidr (assignment) |

| psaraDB for POLARDB |   | Secondary Edition) User Guide·P ug-in managemen |
|---|---|---|

| inet | ipX | ipX(inet) or inet::ipX (assignment) |
|---|---|---|
| ipX | numeric | to numeric(ipX) or ipX::numeric (explicit) _ |
| numeric | ipX | ipX(numeric) or bigint::ipX (explicit) |
| ip4 | bigint | to bigint(ip4) or ip4::bigint (explicit) _ |
| bigint | ip4 | ip4(bigint) or bigint::ip4 (explicit) |
| ip4 | float8 | to double(ip4) or ip4::float8 (explicit) _ |
| float8 | ip4 | ip4(float8) or float8::ip4 (explicit) |
| ipX | varbit | to bit(ipX) or ipX::varbit (explicit) _ |
| bit(32) | ip4 | ip4(bit) or bit::ip4 (explicit) |
| bit(128) | ip6 | ip6(bit) or bit::ip6 (explicit) |
| varbit | ipX | ipX(varbit) or varbit::ipX (explicit) |
| ipX | bytea | to bytea(ipX) or ipX::bytea (explicit) _ |
| bytea | ipX | ipX(bytea) or bytea::ipX (explicit) |
| ipX | ipXr | ipXr(ipX) or ipX::ipXr (implicit) |
| ip4 | ipaddress | ipaddress(ip4) or ip4::ipaddress (implicit) |
| ip6 | ipaddress | ipaddress(ip6) or ip6::ipaddress (implicit) |
| ipaddress | ip4 | ip4(ipaddress) or ipaddress::ip4 (assignment) |
| ipaddress | ip6 | ip6(ipaddress) or ipaddress::ip6 (assignment) |

**Address range data types and type conversions**

The following three data types are used to store a range of IP addresses:

|   | 192.0.2.100-192.0.2.200 |
|---|---|
| 192.0.2.0-192.0.2.255 |   |

`192.0.2.0/24` is equivalent to `192.0.2.0-192.0.2.255` .

|   | 2001::1234-2001::2000:0000 |
|---|---|
| 2001::-2001::ffff |   |

range `2001::/112` is equivalent to `2001::-2001::ffff` . `iprange` : Accepts input in either the `ip4r` or `ip6r` format. For these three data types, `ip4r` provides the following type conversion rules: In the following table, `ipXr` represents any of the three data types described above.

| Source type | Target type | Format |
|---|---|---|
| ipX | ipXr | ipXr(ipX) or ipX::ipXr (implicit) |
| ipXr | text | text(ipXr) or ipXr::text (explicit) |
| text | ipXr | ipXr(text) or text::ipXr (explicit) |
| ipXr | cidr | cidr(ipXr) or ipXr::cidr (explicit) |
| cidr | ipXr | ipXr(cidr) or cidr::ipXr (assignment) |
| ipXr | varbit | to bit(ipXr) or ipXr::varbit (explicit) _ |
| varbit | ip4r | ip4r(varbit) or varbit::ip4r (explicit) |
| varbit | ip6r | ip6r(varbit) or varbit::ip6r (explicit) |

**Usage**

**Create the ip4r extension**

```
CREATE EXTENSION ip4r;
```

**Create a test table and import data**

```
CREATE TABLE ipranges (r iprange, r4 ip4r, r6 ip6r); INSERT INTO ipranges
    SELECT r, null, r
    FROM (
        SELECT ip6r(regexp_replace(ls, E'(....(?!$))', E'\\1:', 'g')::ip6,
               regexp_replace(substring(ls FOR n + 1) || substring(us FROM n + 2),
               E'(....(?!$))', E'\\1:', 'g')::ip6) AS r
        FROM (
            SELECT md5(i || ' lower 1') AS ls,
                   md5(i || ' upper 1') AS us,
                   (i % 11) + (i/11 % 11) + (i/121 % 11) AS n
            FROM generate_series(1,13310) i) s1) s2;
```

**Create a GiST index**

```
CREATE INDEX ipranges_r ON ipranges USING gist (r);
```

**Use the contains operator**

```
EXPLAIN (COSTS OFF) SELECT * FROM ipranges WHERE r >>= '5555::' ORDER BY r;
```

Sample result:

```
                     QUERY PLAN
-----------------------------------------------------
 Sort
   Sort Key: r
   ->  Bitmap Heap Scan on ipranges
         Recheck Cond: (r >>= '5555::'::iprange)
         ->  Bitmap Index Scan on ipranges_r
               Index Cond: (r >>= '5555::'::iprange)
(6 rows)
```

**Uninstall the ip4r extension**

```
DROP EXTENSION ip4r;
```

### 12.12 pg_cron

`pg_cron` is a third-party extension supported by PolarDB for PostgreSQL. It allows you to use the cron syntax to execute SQL statements on schedule in PolarDB for PostgreSQL. You can execute SQL statements to create scheduled tasks and configure automatic execution for the tasks at a specified point in time or time interval. This topic describes the background information and working principles of the pg_cron extension. Examples of using the extension are also provided.

**Background information**

A scheduled task is automatically executed at a specified point in time or time interval. Scheduled tasks are usually managed by a scheduler that executes tasks based on specified time rules. You can configure time rules for the scheduler to execute tasks at a specific point in time every day, a specific day and time every week, and a specific day and time every month. You can also configure the scheduler to specify the execution time and interval of the task based on your business requirements. Scheduled tasks are suitable for the following scenarios: When scheduled tasks are executed on the server side, the tasks can be used to periodically execute background tasks, generate reports, and delete unnecessary data. When scheduled tasks are executed on the client side, the tasks can be used to update data, send alerts to users, and perform automated operations. Scheduled tasks can alleviate the burden of manual operations and improve work efficiency regardless of whether they are executed on the server or client side. The `pg_cron` extension provides the following benefits: Ease of use: You can execute SQL statements to create, schedule, and manage tasks without additional programming or configuration. Flexible scheduling options: You can configure the minute, hour, date, week, and month scheduling options, and use the various combinations of these scheduling options. Database-level task management: Scheduled tasks are stored in databases. Scheduled tasks can be shared and managed across multiple databases. Concurrent task execution: You can execute multiple tasks at the same time to improve task execution efficiency. Reliability and fault tolerance: Error handling and fault tolerance mechanisms are provided to ensure the correct execution of tasks. The corresponding log entries are also generated. The `pg_cron` extension provides a simple and efficient way for database administrators and developers to automate repetitive tasks, such as data backup, report generation, and regular cleanup. This improves the management and development efficiency of databases.

**How it works**

**Scheduled task information maintenance**

2. pga_job detects task list
changes through a trigger and refreshes the task list TASK1 JOB1 Function invocation Add by users SCHEDULE 1.JOB LIST Get traverses TASK2 JOB2 tasks cron.job Task scheduling UNSCHEDULE TASK3 JOB3 Delete ... ...

| jobid | schedule | command | username |
|---|---|---|---|
| 43 | 0**** | JOB 2 | test |

TASK JOB LIST LIST All scheduled tasks are stored in the `cron.job` table. You can create or delete scheduled tasks by calling SQL function interfaces. The `pg_cron` extension maintains the JOB LIST and TASK LIST lists for background scheduling and task execution. When a database is started, the JOB LIST and TASK LIST lists

| based on the task list in the | cron.job |
|---|---|
| cron.job cache invalidate _ _ |   |

consistency of the JOB LIST and TASK LIST lists with the `cron.job` table in real time. This ensures that the tasks can be scheduled and executed correctly.

**Scheduled task scheduling and execution**

Check the task Configure the Check the task Repeat the previous Repeat the previous Task complete TASK LIST status Go to the next connection status, step step and check the timeout status, and and receive the task cycle and send a connection status scheduled task execution result connection information TASK1 The task is activated and Succeeded Succeeded Succeeded Succeeded meets execution conditions Scheduling TASK2 WAITING START CONNECTING SENDING RUNNING DONE Otherwise Failed Failed Failed Failed TASK3 Task failed ... ERROR BREAK Clear connection information WAITING: the default state of the task. If the task is in the Non-active state or the scheduled execution time has not arrived, the scheduling of the task is skipped. Otherwise, the task enters the START state. START: establishes the connection information of the task and performs a connection test. If the connection is successful, the task enters the CONNECTING state. Otherwise, the task enters the ERROR state. CONNECTING: checks whether the task is activated and whether the connection is normal. If all conditions are met, the task enters the SENDING state. Otherwise, the task enters the ERROR state. SENDING: checks whether the task is activated and whether the connection is normal. If all the conditions are met, the scheduled task is sent to the PolarDB for PostgreSQL server and enters the RUNNING state. Otherwise, the task enters the ERROR state. RUNNING: checks whether the task is activated and whether the connection is normal. If all conditions are met, the system receives the returned task result and the task enters the DONE state. Otherwise, the system stops waiting and the task enters the ERROR state. ERROR: The task failed. In this case, the system resets the connection information, and then the task enters the DONE state. DONE: The task is complete. In this case, the system resets the task information, and then the task re-enters the WAITING state.

**Functions**

For security purposes, only privileged accounts have the permissions to invoke the

|   | cron.job |
|---|---|
| cron.job |   |

following functions to perform operations on the `cron.job` table. Standard accounts have only the view permission on the `cron.job` table. All scheduled tasks are stored in the `postgres` database. To perform operations on a scheduled task, you must connect to the `postgres` database. Scheduled tasks are run based on Greenwich Mean Time (GMT). You must convert your local time into GMT.

**Create a scheduled task**

**Syntax**

```
cron.schedule (
    job_name TEXT,
    schedule TEXT,
    command TEXT
```

);

**Parameters**

| Parameter | Description |
|---|---|
| job name _ | The name of the task. You can leave this parameter empty. |
| schedule | The scheduled period of the task. The value of this parameter is a standard cron string. |
| command | The content of the task. The value of this parameter is an SQL string. |

**Add a scheduled task to a specified database**

**Syntax**

```
cron.schedule_in_database (
    job_name TEXT,
    schedule TEXT,
    command TEXT,
    db_name TEXT
```

);

**Parameters**

| Parameter | Description |
|---|---|
| job name _ | The name of the task. |
| schedule | The scheduled period of the task. The value of this parameter is a standard cron string. |
| command | The content of the task. The value of this parameter is an SQL string. |
| db name _ | The destination database where the task is executed. |

**Modify a scheduled task**

**Syntax**

```
cron.alter_job (
    job_id BIGINT,
    schedule TEXT DEFAULT NULL,
    command TEXT DEFAULT NULL,
    db_name TEXT DEFAULT NULL,
    active BOOLEAN DEFAULT NULL
```

);

**Parameters**

| Parameter | Description |
|---|---|
| job id _ | The ID of the task to be modified. |
| schedule | The modified schedule of the task. |
| command | The modified content of the task. |
| db name _ | The new database where you want to execute the task. |
| active | Specifies whether the modified task is in the Active (Running) state. |

**Delete a scheduled task**

**Syntax**

```
cron.unschedule(job_id BIGINT); cron.unschedule(job_name TEXT);
```

**Parameters**

| Parameter | Description |
|---|---|
| job id _ | The ID of the task to be deleted. |
| name | The name of the task to be deleted. |

**Usage**

To ensure security, you can perform the following operations only as a privileged user.

**Install the pg_cron extension**

Connect to a database and run the following command to install the `pg_cron` extension:

```
CREATE EXTENSION pg_cron;
```

**Create a scheduled task**

Run the following command to create a task named `task1` for the `db01` database. The task ID is returned.

```
SELECT cron.schedule_in_database('task1', '* * * * *', 'SELECT 1', 'db01');
```

Sample result:

```
 schedule_in_database
---------------------- (1 row)
```

**View the list of scheduled tasks**

Run the following command to view the list of scheduled tasks:

```
SELECT * FROM cron.job;
```

Sample result:

```
jobid | schedule | command | nodename | nodeport | database | username | active | jobname -------+-----------+----------+----------+----------+----------+----------+--------+----- ---
     1 | * * * * * | SELECT 1 | /tmp     |    39361 | db01     | u1       | t      | tas
```

`k1`

```
(1 row)
```

**View the execution history of a scheduled task**

Run the following command to view the execution history of a scheduled task:

```
SELECT * FROM cron.job_run_details;
```

Sample result:

```
 jobid | runid | job_pid | database | username | command  |  status   | return_message
|          start_time           |           end_time
-------+-------+---------+----------+----------+----------+-----------+----------------+- -----------------------------+-------------------------------
     1 |     1 | 4152316 | db01     | u1       | SELECT 1 | succeeded | 1 row          |
2023-10-19 03:55:00.020442+00 | 2023-10-19 03:55:00.021512+00
     1 |     2 | 4152438 | db01     | u1       | SELECT 1 | succeeded | 1 row          |
2023-10-19 03:56:00.006468+00 | 2023-10-19 03:56:00.006822+00 (2 rows)
```

**Delete a scheduled task**

Run the following command to delete a scheduled task:

```
SELECT cron.unschedule('task1');
```

Sample result:

```
 unschedule
------------
```

`t`

```
(1 row)
```

**Delete the pg_cron extension**

Run the following command to delete the `pg_cron` extension:

```
DROP EXTENSION pg_cron;
```

**Examples of time rules**

The `pg_cron` extension uses the standard cron syntax. `*` indicates that the task is run at a specified time interval. The specified numbers indicate the time period between two consecutive executions.

```
┌───────────── Minute (0 to 59)
 │ ┌────────────── Hour (0 to 23)
 │ │ ┌─────────────── Date (1 to 31)
 │ │ │ ┌──────────────── Month (1 to 12)
 │ │ │ │ ┌───────────────── A specific day of the week (0 to 6). The value range repres
ents Sunday to next Saturday. The value 7 also indicates Sunday.
 │ │ │ │ │
 * * * * *
```

Delete expired data at GMT 03:30 every Saturday.

```
SELECT cron.schedule('30 3 * * 6', $$DELETE FROM events WHERE event_time < now() - in terval '1 week'$$);
```

Execute `VACUUM` at GMT 10:00 every day.

```
SELECT cron.schedule('0 10 * * *', 'VACUUM;');
```

Execute specified SQL statements every minute.

```
SELECT cron.schedule('* * * * *', 'SELECT 1;');
```

Execute specified SQL statements at the 23rd minute of each hour.

```
SELECT cron.schedule('23 * * * *', 'SELECT 1;');
```

Execute specified SQL statements on the fourth day of each month.

```
SELECT cron.schedule('* * 4 * *', 'SELECT 1;');
```

### 12.13 pg_profile (resource monitoring)

**monitoring)**

`pg_profile` is a third-party extension supported by PolarDB for PostgreSQL. It collects statistics on resource-intensive activities in a target database to help you analyze and optimize the database. This extension is based on PostgreSQL statistical views and several community extensions. It is written entirely in PL/pgSQL and requires no external libraries or software. When this extension is used with the `pg_cron` extension, you can periodically collect data and monitor resource-intensive activities.

**Usage notes**

Data collection requires the `pg_stat_statements` and `pg_stat_kcache` extensions. Ensure that they are added to the `shared_preload_libraries` parameter of the sampled database. They are loaded by default.

**Important**

The cluster restarts after you modify the parameter. Proceed with caution. In the sampled database, you must create the `pg_stat_statements` extension. You can also create the `pg_stat_kcache` extension to collect more information. Storing sample information consumes disk space. This extension has an automatic cleanup mechanism, but you must still manage data retention. A single sampling operation is time-consuming. Therefore, do not perform sampling too frequently. The recommended frequency is one to two times per hour.

**Usage**

Due to the security restrictions of `dblink` , the profile database and the server database must be created in the same PolarDB for PostgreSQL cluster. The following steps describe how to create a server database and a profile database. During sampling, the profile database sends a sampling request to the server database. After the server database receives the request, it returns its statistics to the profile database. The statistics are then stored in a table. This allows you to obtain statistics for other databases from the profile database.

**Server database**

Create a server database:

```
CREATE DATABASE server;
```

Connect to the server database and create the statistics extensions:

```
\c server CREATE EXTENSION IF NOT EXISTS pg_stat_statements; CREATE EXTENSION IF NOT EXISTS pg_stat_kcache;
```

**Profile database**

Create a profile database:

```
CREATE DATABASE profile;
```

Connect to the profile database and create the pg_profile extension:

```
\c profile CREATE EXTENSION IF NOT EXISTS pg_profile CASCADE;
```

**Create a sampling connection**

```xml
SELECT create_server(
   'server',
   'dbname=server channel_name=localhost user=
<privileged_account_of_the_server_database> password=<password_for_the_account>
```

); The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| server | server | The connection name. This parameter is user- defined. |
| dbname | server | The database name. |
| channel name _ | localhost | The connection information. Only localhost is supported for this parameter. |
| user | test user _ | A privileged account for the cluster where the server database resides. |
| password | T123456! | The password for the account. |

Sample result:

```
                                    show_servers
-------------------------------------------------------------------------------------
 (server,"dbname=server channel_name=localhost user=test_user password=****",t,)
(1 row)
```

**Modify the sampling connection information**

```xml
SELECT set_server_connstr(
   'server',
   'dbname=server channel_name=localhost user=
<privileged_account_of_the_profile_database> password=<password_for_the_account>
```

); The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| server | server | The connection name. Do not modify this parameter. |
| dbname | server | The database name. |
| channel name _ | localhost | The connection information. The value of this parameter is fixed to localhost. |
| user | test user _ | A privileged account for the cluster where the server database resides. |
| password | T123456! | The password for the account. |

**Perform the initial data collection**

```
SELECT take_sample();
```

Sample result:

```
      take_sample
-------------------------
 (server,OK,00:00:02.81)
(1 row)
```

**Collect data again after stress testing the sampled database**

Use the pgbench tool to run a stress test on the sampled server database:

```
pgbench -s 100 -i server -U test_user -h pc-****.pg.rds.aliyuncs.com -p 5432
```

The following table describes the parameters.

| Parameter | Example | Description |
|---|---|---|
| -s | 100 | 100 indicates that 10,000,000 rows are created in the pgbench accounts table. _ |
| -i | server | The name of the database on which you want to perform a stress test. |
| -U | test user _ | A privileged account for the cluster where the server database resides. |
| -h | pc- ****.pg.rds.aliyuncs. com | The endpoint of the cluster where the server database resides. |
| -p | 5432 | The cluster port. Specify the port number shown in the console. |

Connect to the profile database and collect data again:

```
SELECT take_sample();
```

View the collected data:

```
SELECT * FROM show_samples('server');
```

Sample result:

```
sample | sample_time | sizes_collected | dbstats_reset | bgwrstats_reset | archstats_reset --------+------------------------+-----------------+---------------+-----------------+--- ------------
      1 | 2024-02-23 07:29:53+00 | t               |               |                 |
      2 | 2024-02-23 08:11:39+00 | t               |               |                 |
```

**Generate a report from the collected results**

You can export the collected data to a local file using one of the following two methods. Method 1: Run the following SQL statement in the interactive command line of the `psql` client tool to generate the output file.

```
\o report_1_2.html SELECT get_report('server',1,2);
```

Method 2: Use the command line to instruct `psql` to write the data directly to a file.

```
psql -Aqtc "SELECT get_report('server',1,2)" \
   -o report_server_1_2.html -d profile \
   -h <endpoint_of_the_profile_database_cluster> \
   -p <port_of_the_database_cluster> \
   -U <privileged_account_for_the_profile_database_cluster>
```

### 12.14 pg_sphere (spherical data calculations)

**calculations)**

pg_sphere is an open source PostgreSQL extension that supports spherical data types, functions, and operators. It allows you to represent objects on a sphere, such as the points, lines, and polygons of the Earth. It also supports calculating the distance or area between these objects.

**Install and uninstall the extension**

Install the pg_sphere extension.

```
CREATE EXTENSION pg_sphere;
```

Uninstall the pg_sphere extension.

```
DROP EXTENSION pg_sphere;
```

**Data types**

The pg_sphere extension supports the following object types: Point Euler transformation Circle Line Ellipses Path Polygon The following example shows how to create a point object. You can represent a point on a sphere in one of the following three ways: Specify the location by longitude and latitude in radians.

```
SELECT spoint '(0.1,-0.2)';
```

Sample result:

```
    spoint
--------------
 (0.1 , -0.2)
(1 row)
```

Specify the location by longitude and latitude in degrees.

```
SELECT spoint '( 10.1d, -90d)';
```

Sample result:

```
                 spoint
----------------------------------------
 (0.176278254451427 , -1.5707963267949)
(1 row)
```

Specify the longitude and latitude using degrees, minutes, and seconds (DMS).

```
SELECT spoint '( 10d 12m 11.3s, -13d 14m)';
```

Sample result:

```
                  spoint
------------------------------------------
 (0.178078367649387 , -0.230965237680583)
(1 row)
```

A circle is divided into 360 degrees. One degree is divided into 60 minutes. One minute is divided into 60 seconds.

**Constructors**

Constructors are used to create spherical data types, such as Point, Euler transformation, Circle, Line, Ellipses, Path, and Polygon, from other data types. The following example constructs a spherical point from longitude and latitude. The resulting point has a longitude of 270 degrees and a latitude of -30 degrees.

```
SELECT spoint (270.0 * pi() / 180.0, -30.0 * pi() / 180.0) AS spoint;
```

Sample result:

```
                 spoint
-----------------------------------------
 (4.71238898038469 , -0.523598775598299)
(1 row)
```

**Operators**

The pg_sphere extension supports the following operators: Casting Equality Contain and overlap Crossing of lines Distance Length and circumference Center The following example uses the distance operator to calculate the distance between two circles.

```
SELECT 180 * ( scircle '<(0d,20d),2d>' <-> scircle '<(0d,40d),2d>' ) / pi() AS dist;
```

Sample result:

```
 dist
------ (1 row)
```

**Functions**

The pg_sphere extension supports the following calculation functions: Area calculation functions Path calculation functions Distance calculation functions The following examples show how to use the area calculation and point calculation functions. Calculate the area of a sphere in `pi` .

```
SELECT area( scircle '<(0d,90d),60d>' ) / pi() AS area;
```

Sample result:

```
 area
------ (1 row)
```

Retrieve the longitude and latitude of a spherical point in degrees. In the pg_sphere extension, the `long(spoint)` function has been changed to

```
 long_sphere(spoint) .
SELECT long_sphere ( spoint '(10d,20d)' ) * 180.0 / pi() AS longitude;
```

Sample result:

```
longitude ------------ (1 row) SELECT lat ( spoint '(10d,20d)' ) * 180.0 / pi() AS latitude;
```

Sample result:

```
latitude ---------- (1 row)
```

**References**

For more information, see the official pg_sphere documentation.

### 12.15 pgAudit

PolarDB for PostgreSQL supports the pgAudit extension that can produce audit logs required to comply with government, financial, or ISO certifications. Audit logs help you analyze faults and operations on your clusters to obtain information about data queries.

**Usage notes**

To view the generated audit logs, you must enable the SQL Explorer feature. A privileged account is required to configure parameters related to the pgAudit extension.

**Usage**

**Install the pgAudit extension**

```
CREATE EXTENSION pgaudit;
```

**Audit read operations**

Execute the following statement to audit all read operations on a database named

```
 pgaudit_testdb :
ALTER DATABASE pgaudit_testdb SET pgaudit.log = 'READ';
```

After the preceding statement is executed, all read operations, such as `SELECT` operations,

| on the | pgaudit testdb _ |   |
|---|---|---|
| UPDATE |   |   |
|   |   | operations, on |

on the `pgaudit_testdb` database are audited. Write operations, such as `INSERT` and `UPDATE` operations, on the database are not audited.

**Audit read and write operations**

Execute the following statement to audit all read and write operations on the `pgaudit_testdb` database:

```
ALTER DATABASE pgaudit_testdb SET pgaudit.log = 'READ,WRITE';
```

After the preceding statement is executed, all read and write operations, such as `SELECT` , `INSERT` , and `UPDATE` operations, on the `pgaudit_testdb` database are audited.

**Disable log audit**

```
ALTER DATABASE pgaudit_testdb SET pgaudit.log = 'NONE';
```

**Audit operations on a specified object**

Execute the following statements to audit operations performed by the user of the `pgaudit_testdb` database, create a table named test_audit, and then grant all permissions on the table to the user:

```
CREATE USER audit_role; ALTER DATABASE pgaudit_testdb SET pgaudit.role = 'audit_role'; CREATE TABLE test_audit (id INT); GRANT ALL ON test_audit TO audit_role;
```

After the preceding statements are executed, only all operations on the `test_audit` table in the `pgaudit_testdb` database are audited.

**Uninstall the pgAudit extension**

```
DROP EXTENSION pgaudit;
```

**References**

For more information, see pgAudit documentation.

### 12.16 sequential_uuid (UUID generation)

**generation)**

The sequential_uuid extension provides two universally unique identifier (UUID) generators that create sequential patterns. This helps reduce the random I/O issues caused by fully random UUIDs.

**Background information**

Standard random UUID generators select values uniformly from a given range. This leads to poor data locality when you insert data into an index because all index leaf pages are equally likely to be hit. This can force the entire index into memory. This is not an issue for small indexes. However, the cache hit ratio drops quickly when the index size exceeds the shared buffer or RAM size. Compared to random UUIDs, UUIDs that are based on sequences and timestamps have a sequential pattern. This pattern ensures that new data is almost always inserted at the rightmost edge of the index because new sequence values are greater than previous ones and timestamps monotonically increase. This helps improve the cache hit ratio. UUID generators with sequential patterns increase the predictability of UUIDs and the probability of cross-machine collisions. For more information about the benefits of sequential UUIDs, see Sequential UUID Generators. The main goal of the sequential_uuid extension is to generate more sequential UUIDs without significantly reducing randomness. A reduction in randomness can increase the probability of collisions and the predictability of the UUIDs.

**Generator design**

The simplest way to make UUIDs more sequential is to use a sequential value as a prefix. For example, you can take a value from a sequence or a timestamp and append random data to form a 16-byte UUID. This method produces almost completely sequential UUIDs, but it has two problems: Reduced randomness: If you use a sequence that generates bigint values, the random portion of the UUID is reduced from 16 bytes to 8 bytes. Timestamps reduce randomness in a similar way, depending on their precision. This reduction in randomness increases the probability of collisions and the predictability of the UUIDs. For example, you can determine which UUIDs were generated close together in time and even infer the specific timestamp. Bloat: If the values increase monotonically, the index can become bloated after historical data is deleted. An index on a timestamp in a log table is a common example. To solve these problems, the sequential_uuid generators are designed to loop back periodically. A loopback can occur after a set number of UUIDs are generated or after a specific time interval. In both cases, UUIDs are generated in blocks with the format `(block` ID; random data) . The size of the block ID is fixed and depends on the number of blocks, which is a generator parameter. For example, if you use the default of 65,536 blocks, the block ID requires 2 bytes. The block ID increases with each block and eventually loops back. The sequence-based UUID generator can use blocks that contain 256 UUIDs each. The 2byte block ID is calculated as follows:

```
(nextval('s') / 256) % 65536
```

The generator loops back after every 16,777,216 (256 × 65,536) UUIDs are generated. The block size is defined by the number of UUIDs it contains. The timestamp-based UUID generator has a default of 65,536 blocks, the same as the sequence-based generator. The block ID is calculated as follows:

```
(timestamp / 60) % 65536
```

The generator loops back approximately every 45 days. The block size is defined as a time interval. The default value is 60 seconds.

**UUID generation functions**

The sequential_uuid extension provides two functions that generate UUIDs with sequential patterns. One function uses a sequence, and the other uses a timestamp. The **uuid_sequence_nextval** function accepts the following parameters: A sequence object of the regclass type. An integer for the block size. Default value: 65536. An integer for the number of blocks. Default value: 65536. Generate a UUID with a sequential pattern using a sequence:

```
CREATE EXTENSION sequential_uuids; CREATE SEQUENCE s; SELECT uuid_sequence_nextval('s'::regclass, 256, 65536);
```

Sample result:

```
          uuid_sequence_nextval
--------------------------------------
 00005547-8a67-452d-bdf7-b390f1edc49b
(1 row)
```

The **uuid_time_nextval** function accepts the following parameters: An integer for the time interval in seconds. Default value: 60. An integer for the number of blocks. Default value: 65536. Generate a UUID with a sequential pattern using a timestamp:

```
CREATE EXTENSION sequential_uuids; SELECT uuid_time_nextval(1, 256);
```

Sample result:

```
          uuid_time_nextval
--------------------------------------
 08dac705-8776-4ce3-a45c-123fd65e11e8
(1 row)
```

The default values for these parameters are suitable for most scenarios.

### 12.17 pg_pathman

This topic describes how to use the pg_pathman extension.

**Background information**

pg_pathman is an extension that you can use in a PolarDB for PostgreSQL cluster. The pg_pathman extension provides efficient partitioning capabilities and helps effectively manage partitions and improve the performance of partitioned tables.

**Create the pg_pathman extension**

```
CREATE EXTENSION IF NOT EXISTS pg_pathman;
```

After the pg_pathman extension is created, you can execute the following SQL statement to view the version:

```
SELECT extname,extversion FROM pg_extension WHERE extname = 'pg_pathman';
```

Sample result:

```
  extname   | extversion
------------+------------
 pg_pathman | 1.5
(1 row)
```

**Upgrade the extension**

PolarDB for PostgreSQL upgrades the pg_pathman extension on a regular basis to improve database services. To manually upgrade the pg_pathman extension, you can upgrade the cluster to the latest version.

**Features**

Supports hash partitioning and range partitioning. Provides automatic and manual partition management. In automatic partition management, use functions to automatically create partitions and migrate data from a parent table to partitions. In manual partition management, use functions to attach existing tables to a parent table or detach tables from a parent table. Supports a wide range of column types for partitioning, including the INT, FLOAT, and DATE column types and custom domains. Provides optimized plans for queries on a partitioned table, and uses strategies such as joins and subqueries in the plans. Enables dynamic partition selection by using custom plan nodes: `RuntimeAppend` and

```
 RuntimeMergeAppend .
```

Uses the `PartitionFilter` feature to dynamically filter partitions based on query conditions. Automatically adds new partitions when the inserted data exceeds the current partition boundaries. This feature is available only in range partitioning. Directly reads data from and writes data into partitioned tables by using the `COPY` `FROM/TO` statement. Allows you to update partition keys by adding a trigger. If you do not need to update partition keys, we recommend that you do not add the trigger because the trigger may have negative impacts on performance. Allows you to configure custom callback functions that are automatically invoked when partitions are created. Allows you to create partitioned tables and migrate data from a parent table to partitions in a non-blocking manner. Allows you to insert data into foreign tables managed by Foreign Data Wrappers (FDWs) of PostgreSQL or other FDWs. You can use the pg_pathman.insert_into_fdw=(disabled | postgres | any_fdw) parameter to configure this feature.

**Views and tables**

The pg_pathman extension uses functions to manage partitioned tables and creates views for you to view the status of partitioned tables. Examples: pathman_config

```
CREATE TABLE IF NOT EXISTS pathman_config (
    partrel         REGCLASS NOT NULL PRIMARY KEY,  -- The object identifier (OID) of
the parent table.
    attname         TEXT NOT NULL,  -- The name of the partition key column.
    parttype        INTEGER NOT NULL,  -- The partitioning type (hash or range).
    range_interval  TEXT,  -- The range or span of values that each partition covers.
    CHECK (parttype IN (1, 2)) /* check for allowed part types */ );
```

pathman_config_params

```
CREATE TABLE IF NOT EXISTS pathman_config_params (
    partrel        REGCLASS NOT NULL PRIMARY KEY,  -- The OID of the parent table.
    enable_parent  BOOLEAN NOT NULL DEFAULT TRUE,  -- Specifies whether to filter the
parent table in the optimizer.
    auto           BOOLEAN NOT NULL DEFAULT TRUE,  -- Specifies whether to automatical
ly add new partitions.
    init_callback REGPROCEDURE NOT NULL DEFAULT 0); -- The OID of the initialization
callback function that is invoked each time partitions are created.
```

pathman_concurrent_part_tasks

```
-- helper SRF function CREATE OR REPLACE FUNCTION show_concurrent_part_tasks() RETURNS TABLE (
    userid     REGROLE,
    pid        INT,
    dbid       OID,
    relid      REGCLASS,
    processed  INT,
    status     TEXT)
AS 'pg_pathman', 'show_concurrent_part_tasks_internal' LANGUAGE C STRICT; CREATE OR REPLACE VIEW pathman_concurrent_part_tasks AS SELECT * FROM show_concurrent_part_tasks();
```

pathman_partition_list

```
-- helper SRF function CREATE OR REPLACE FUNCTION show_partition_list() RETURNS TABLE (
    parent     REGCLASS,
    partition  REGCLASS,
    parttype   INT4,
    partattr   TEXT,
    range_min  TEXT,
    range_max  TEXT)
AS 'pg_pathman', 'show_partition_list_internal' LANGUAGE C STRICT; CREATE OR REPLACE VIEW pathman_partition_list AS SELECT * FROM show_partition_list();
```

**Partitioning management**

**Perform range partitioning**

Four management functions are used to create range partitions. Two functions are used to specify the start value, interval, and number of partitions. You can define these two functions by using the following syntax:

```
create_range_partitions(relation REGCLASS, -- The OID of the parent table.
                        attribute      TEXT,      -- The name of the partition key
column.
                        start_value    ANYELEMENT,  -- The start value.
                        p_interval     ANYELEMENT,  -- The interval of all data types, w
hich is applicable to all types of partitioned tables.
                        p_count        INTEGER DEFAULT NULL,   --  The number of
partitions.
                        partition_data BOOLEAN DEFAULT TRUE)   --  Specifies whether to
immediately migrate data from the parent table to partitions. We recommend that you cal l the partition_table_concurrently() function to run non-blocking data migration. create_range_partitions(relation REGCLASS, -- The OID of the parent table.
                        attribute      TEXT,      -- The name of the partition key
column.
                        start_value    ANYELEMENT,  -- The start value.
                        p_interval     INTERVAL,    -- The interval of an INTERVAL data
type, which is applicable to ingestion-time partitioned tables.
                        p_count        INTEGER DEFAULT NULL,   --  The number of
partitions.
                        partition_data BOOLEAN DEFAULT TRUE)   --  Specifies whether to
immediately migrate data from the parent table to partitions. We recommend that you inv oke the partition_table_concurrently() function to perform non-blocking data migration.
```

The other two functions are used to specify the start value, end value, and interval. You can define the functions by using the following syntax:

```
create_partitions_from_range(relation REGCLASS, -- The OID of the parent table.
                             attribute      TEXT,      -- The name of the partition key c
olumn.
                             start_value    ANYELEMENT,  -- The start value.
                             end_value      ANYELEMENT,  -- The end value.
                             p_interval     ANYELEMENT,  -- The interval of all data
types, which is applicable to all types of partitioned tables.
                             partition_data BOOLEAN DEFAULT TRUE)   --  Specifies
whether to immediately migrate data from the parent table to partitions. We recommend t hat you call the partition_table_concurrently() function to run non-blocking data migra tion. create_partitions_from_range(relation REGCLASS, -- The OID of the parent table.
                             attribute      TEXT,      -- The name of the partition key c
olumn.
                             start_value    ANYELEMENT,  -- The start value.
                             end_value      ANYELEMENT,  -- The end value.
                             p_interval     INTERVAL,    -- The interval of an INTERVAL
data type, which is applicable to ingestion-time partitioned tables.
                             partition_data BOOLEAN DEFAULT TRUE)   --  Specifies
whether to immediately migrate data from the parent table to partitions. We recommend t hat you invoke the partition_table_concurrently() function to perform non-blocking data migration.
```

Examples:
1. Create a parent table that you want to partition and insert test data.

```
--- Create a parent table that you want to partition. CREATE TABLE part_test(id int, info text, crt_time timestamp not null); -- -- The pa rtition key column must contain the NOT NULL constraint. --- Insert test data into the parent table to simulate a parent table that already ha s data. INSERT INTO part_test SELECT id,md5(random()::text),clock_timestamp() + (id||' hour') ::interval from generate_series(1,10000) t(id);
```

Query the data of the parent table.

```
SELECT * FROM part_test limit 10;
```

Sample result:

```
 id |               info               |          crt_time
----+----------------------------------+----------------------------
  1 | 36fe1adedaa5b848caec4941f87d443a | 2016-10-25 10:27:13.206713
  2 | c7d7358e196a9180efb4d0a10269c889 | 2016-10-25 11:27:13.206893
  3 | 005bdb063550579333264b895df5b75e | 2016-10-25 12:27:13.206904
  4 | 6c900a0fc50c6e4da1ae95447c89dd55 | 2016-10-25 13:27:13.20691
  5 | 857214d8999348ed3cb0469b520dc8e5 | 2016-10-25 14:27:13.206916
  6 | 4495875013e96e625afbf2698124ef5b | 2016-10-25 15:27:13.206921
  7 | 82488cf7e44f87d9b879c70a9ed407d4 | 2016-10-25 16:27:13.20693
  8 | a0b92547c8f17f79814dfbb12b8694a0 | 2016-10-25 17:27:13.206936
  9 | 2ca09e0b85042b476fc235e75326b41b | 2016-10-25 18:27:13.206942
 10 | 7eb762e1ef7dca65faf413f236dff93d | 2016-10-25 19:27:13.206947
(10 rows)
```

2. Create partitions and ensure that each partition contains one month of data.

```
--- Create partitions and ensure that each partition contains one month of data. SELECT create_range_partitions('part_test'::regclass, -- The OID of the parent t able.
                        'crt_time',                        -- The name of the partition
key column.
                        '2016-10-25 00:00:00'::timestamp,  -- The start value of the r
ange for the first partition.
                        interval '1 month',                -- The range or span of valu
es that each partition covers.
                        24,                                -- The number of partitions.
                        false) ;                            -- The data is not
migrated.
```

3. -- Perform non-blocking data migration.

```
--- The data is still in the parent table before migration. SELECT count(*) FROM ONLY part_test;
 count
-------
 10000
(1 row) --- Non-blocking migration API partition_table_concurrently(relation REGCLASS, -- The OID of the paren t table.
                             batch_size INTEGER DEFAULT 1000, -- The number of records
in a transaction that you want to migrate from the parent table.
                             sleep_time FLOAT8 DEFAULT 1.0)    -- The retry interval f
ollowing a failed attempt to acquire a row lock. After 60 failed attempts, the task i s ended. -- Perform non-blocking data migration. SELECT partition_table_concurrently('part_test'::regclass,
                             10000,
                             1.0);
--- After the migration is completed, all data is migrated to the partitions, and the parent table is empty. SELECT count(*) FROM ONLY part_test;
 count
------- (1 row)
```

4. After you migrate the data, we recommend that you disable the parent table. This way, the
parent table is not included in the execution plan.

```
--- Disable the parent table. SELECT set_enable_parent('part_test'::regclass, false); --- Verify the execution plan. EXPLAIN SELECT * FROM part_test WHERE crt_time = '2016-10-25 00:00:00'::timestamp;
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Append  (cost=0.00..16.18 rows=1 width=45)
   ->  Seq Scan on part_test_1  (cost=0.00..16.18 rows=1 width=45)
         Filter: (crt_time = '2016-10-25 00:00:00'::timestamp without time zone)
(3 rows)
```

When you use range partitioning, take note of the following items: The partition key column must contain the NOT NULL constraint. The number of partitions must be sufficient to cover all existing records. Perform non-blocking data migration. After data migration is completed, disable the parent table.

**Perform hash partitioning**

You can use the following management function to create range partitions and specify the start value, interval, and number of partitions:

```
create_hash_partitions(relation REGCLASS, -- The OID of the parent table.
                       attribute        TEXT,      -- The name of the partition key
column.
                       partitions_count INTEGER,   -- The number of partitions.
                       partition_data   BOOLEAN DEFAULT TRUE)   --  Specifies whether to
immediately migrate data from the parent table to the partitions. We recommend that you invoke the partition_table_concurrently() function to perform non-blocking data migrati on.
```

Examples:
1. Create a parent table that you want to partition and insert test data.

```
--- Create a parent table that you want to partition. CREATE TABLE part_test(id int, info text, crt_time timestamp not null); -- The par tition key column must contain the NOT NULL constraint. --- Insert test data into the parent table to simulate a parent table that already ha s data. INSERT INTO part_test SELECT id,md5(random()::text),clock_timestamp() + (id||' hour') ::interval FROM generate_series(1,10000) t(id);
```

Query the data of the parent table.

```
SELECT * FROM part_test limit 10;
```

Sample result:

```
 id |               info               |          crt_time
----+----------------------------------+----------------------------
  1 | 29ce4edc70dbfbe78912beb7c4cc95c2 | 2016-10-25 10:47:32.873879
  2 | e0990a6fb5826409667c9eb150fef386 | 2016-10-25 11:47:32.874048
  3 | d25f577a01013925c203910e34470695 | 2016-10-25 12:47:32.874059
  4 | 501419c3f7c218e562b324a1bebfe0ad | 2016-10-25 13:47:32.874065
  5 | 5e5e22bdf110d66a5224a657955ba158 | 2016-10-25 14:47:32.87407
  6 | 55d2d4fd5229a6595e0dd56e13d32be4 | 2016-10-25 15:47:32.874076
  7 | 1dfb9a783af55b123c7a888afe1eb950 | 2016-10-25 16:47:32.874081
  8 | 41eeb0bf395a4ab1e08691125ae74bff | 2016-10-25 17:47:32.874087
  9 | 83783d69cc4f9bb41a3978fe9e13d7fa | 2016-10-25 18:47:32.874092
 10 | affc9406d5b3412ae31f7d7283cda0dd | 2016-10-25 19:47:32.874097
(10 rows)
```

2. Create partitions.

```
--- Create 128 partitions. SELECT create_hash_partitions('part_test'::regclass, The OID of the parent table.
                        'crt_time',                        -- The name of the partition
key column.
                        128,                               -- The number of partitions
that you want to create.
                        false) ;                            -- The data is not
migrated.
```

3. -- Perform non-blocking data migration.

```
--- The data is still in the parent table before migration. SELECT count(*) FROM ONLY part_test;
 count
-------
 10000
(1 row) --- Non-blocking migration API partition_table_concurrently(relation REGCLASS, -- The OID of the paren t table.
                             batch_size INTEGER DEFAULT 1000, -- The number of records
in a transaction that you want to migrate from the parent table.
                             sleep_time FLOAT8 DEFAULT 1.0)    -- The retry interval f
ollowing a failed attempt to acquire a row lock. After 60 failed attempts, the task i s ended. -- Perform non-blocking data migration. SELECT partition_table_concurrently('part_test'::regclass,
                             10000,
                             1.0);
--- After the migration is completed, all data is migrated to the partitions, and the parent table is empty. SELECT count(*) FROM ONLY part_test;
 count
------- (1 row)
```

4. After you migrate the data, we recommend that you disable the parent table. This way, the
parent table is not included in the execution plan.

```
--- Disable the parent table. SELECT set_enable_parent('part_test'::regclass, false);
```

Verify the execution plan.

```
--- Query a single partition. EXPLAIN SELECT * FROM part_test WHERE crt_time = '2016-10-25 00:00:00'::timestamp;
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Append  (cost=0.00..1.91 rows=1 width=45)
   ->  Seq Scan on part_test_122  (cost=0.00..1.91 rows=1 width=45)
         Filter: (crt_time = '2016-10-25 00:00:00'::timestamp without time zone)
(3 rows)
```

-- The partitioned table has the following restrictions. The pg_pathman extension automatically converts the statement. In traditional inheritance-based partitioning, you cannot filter partitions by using a statement like `SELECT * FROM part_test WHERE crt_time =`

```
'2016-10-25 00:00:00'::timestamp; .
```

```
\d+ part_test_122
                                Table "public.part_test_122"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_122_3_check" CHECK
(get_hash_part_idx(timestamp_hash(crt_time), 128) = 122) Inherits: part_test
```

When you use hash partitioning, take note of the following items: The partition key column must contain the NOT NULL constraint. Perform non-blocking data migration. After data migration is completed, disable the parent table. The pg_pathman extension can work regardless of how the statement is written.

|   | select * from part test where crt time = _ _ |
|---|---|
| '2016-10-25 00:00:00'::timestamp; |   |

partitioning. HASH partition columns are not limited to int-type columns. The column types are automatically converted by a hash function.

**Migrate data to partitions**

If data remains in the parent table, perform non-blocking data migration to migrate data to partitions. Function:

```
WITH tmp AS (DELETE FROM <Primary table> limit xx nowait returning *) INSERT INTO <Part itions> SELECT * FROM tmp;
```

You can also use the following statement to label rows. Then, perform DELETE and INSERT operations.

```
SELECT array_agg(ctid) FROM <Primary table> limit xx FOR UPDATE nowati;
```

Function:

```
partition_table_concurrently(relation REGCLASS, -- The OID of the parent table.
                             batch_size INTEGER DEFAULT 1000, -- The number of records i
n a transaction that you want to migrate from the parent table.
                             sleep_time FLOAT8 DEFAULT 1.0)    -- The retry interval
following a failed attempt to acquire a row lock. After 60 failed attempts, the task is ended.
```

Examples:

```
SELECT partition_table_concurrently('part_test'::regclass,
                             10000,
                             1.0);
```

View the background data migration task.

```
SELECT * FROM pathman_concurrent_part_tasks;
```

**Split range partitions**

To split an excessively large range partition into smaller partitions, use the following function:

```
split_range_partition(partition REGCLASS, -- The OID of the partition.
                      split_value    ANYELEMENT,          -- The split value.
                      partition_name TEXT DEFAULT NULL) -- The name of the added partiti
on.
```

Examples:
1. Use the table in the **Perform range partitioning** section with the following schema.

```
\d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Child tables: part_test_1,
              part_test_10,
              part_test_11,
              part_test_12,
              part_test_13,
              part_test_14,
              part_test_15,
              part_test_16,
              part_test_17,
              part_test_18,
              part_test_19,
              part_test_2,
              part_test_20,
              part_test_21,
              part_test_22,
              part_test_23,
              part_test_24,
              part_test_3,
              part_test_4,
              part_test_5,
              part_test_6,
              part_test_7,
              part_test_8,
              part_test_9
\d+ part_test_1
                                 Table "public.part_test_1"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_1_3_check" CHECK (crt_time >= '2016-10-25 00:00:00'::timestamp
without time zone AND crt_time < '2016-11-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

2. Split the partition.

```
SELECT split_range_partition('part_test_1'::regclass, -- The OID of the partition.
                      '2016-11-10 00:00:00'::timestamp,     -- The point in time at wh
ich the partition is split.
                      'part_test_1_2');                     -- The name of the new part
ition.
```

The partition is split into the following partitions:

```
\d+ part_test_1
                                 Table "public.part_test_1"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_1_3_check" CHECK (crt_time >= '2016-10-25 00:00:00'::timestamp
without time zone AND crt_time < '2016-11-10 00:00:00'::timestamp without time zone) Inherits: part_test \d+ part_test_1_2
                                Table "public.part_test_1_2"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_1_2_3_check" CHECK (crt_time >= '2016-11-10
00:00:00'::timestamp without time zone AND crt_time < '2016-11-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

Data is automatically migrated to the other partition.

```
SELECT count(*) FROM part_test_1;
 count
------- (1 row) SELECT count(*) FROM part_test_1_2;
 count
------- (1 row)
```

The following example describes the inheritance relationship.

```
\d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Child tables: part_test_1,
              part_test_10,
              part_test_11,
              part_test_12,
              part_test_13,
              part_test_14,
              part_test_15,
              part_test_16,
              part_test_17,
              part_test_18,
              part_test_19,
              part_test_1_2,    -- The added partition.
              part_test_2,
              part_test_20,
              part_test_21,
              part_test_22,
              part_test_23,
              part_test_24,
              part_test_3,
              part_test_4,
              part_test_5,
              part_test_6,
              part_test_7,
              part_test_8,
              part_test_9
```

**Merge range partitions**

Only range partitions are supported and they must be adjacent partitions. Call the following function to merge range partitions:

```
--- Specify two partitions that you want to merge. merge_range_partitions(partition1 REGCLASS, partition2 REGCLASS)
```

Examples:
1. Use the table in the **Split range partitions** section to merge partitions.

```
SELECT merge_range_partitions('part_test_1'::regclass, 'part_test_1_2'::regclass);
```

The following error is returned if you merge the partitions that are not adjacent.

```
SELECT merge_range_partitions('part_test_2'::regclass, 'part_test_12'::regclass)
```

;

```
ERROR: merge failed, partitions must be adjacent CONTEXT: PL/pgSQL function merge_range_partitions_internal(regclass,regclass,regclass,anyelement) line 27 at RAISE SQL statement "SELECT public.merge_range_partitions_internal($1, $2, $3, NULL::ti mestamp without time zone)" PL/pgSQL function merge_range_partitions(regclass,regclass) line 44 at EXECUTE
```

2. After you merge the partitions, one of the partitions is deleted.

```
\d part_test_1_2 Did not find any relation named "part_test_1_2". \d part_test_1
             Table "public.part_test_1"
  Column  |            Type             | Modifiers
----------+-----------------------------+-----------
 id       | integer                     |
 info     | text                        |
 crt_time | timestamp without time zone | not null
Check constraints:
    "pathman_part_test_1_3_check" CHECK (crt_time >= '2016-10-25 00:00:00'::timestamp
without time zone AND crt_time < '2016-11-25 00:00:00'::timestamp without time zone) Inherits: part_test SELECT count(*) FROM part_test_1;
 count
------- (1 row)
```

**Add a new range partition**

You can use several methods to add partitions to a parent table that was partitioned. Three methods are described here: append a new range partition, prepend a new range partition, and specify the start value of partitions.

**Append a new range partition**

When you append a new partition to the parent table, the interval that is specified when the partitioned table was created is used. You can query the interval value of each partitioned table from the pathman_config table.

```
SELECT * FROM pathman_config;
  partrel  | attname  | parttype | range_interval
-----------+----------+----------+----------------
 part_test | crt_time |        2 | 1 mon
(1 row)
```

Call the following function to append a new range partition (you cannot specify the tablespace).

```
append_range_partition(parent REGCLASS, -- The OID of the parent tabl
```

`e.`

```
                       partition_name TEXT DEFAULT NULL,   -- The name of the new partit
ion. This parameter is not required.
                       tablespace     TEXT DEFAULT NULL)   -- The tablespace for the new
partition. This parameter is not required.
```

Examples:

```
SELECT append_range_partition('part_test'::regclass); \d+ part_test_25
                                Table "public.part_test_25"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_25_3_check" CHECK (crt_time >= '2018-10-25 00:00:00'::timestamp
without time zone AND crt_time < '2018-11-25 00:00:00'::timestamp without time zone) Inherits: part_test \d+ part_test_24
                                Table "public.part_test_24"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_24_3_check" CHECK (crt_time >= '2018-09-25 00:00:00'::timestamp
without time zone AND crt_time < '2018-10-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

**Prepend a new range partition**

Call the following function to prepend a new range partition.

```
prepend_range_partition(parent REGCLASS,
                        partition_name TEXT DEFAULT NULL,
                        tablespace     TEXT DEFAULT NULL)
```

Examples:

```
SELECT prepend_range_partition('part_test'::regclass); \d+ part_test_26
                                Table "public.part_test_26"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_26_3_check" CHECK (crt_time >= '2016-09-25 00:00:00'::timestamp
without time zone AND crt_time < '2016-10-25 00:00:00'::timestamp without time zone) Inherits: part_test \d+ part_test_1
                                 Table "public.part_test_1"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_1_3_check" CHECK (crt_time >= '2016-10-25 00:00:00'::timestamp w
ithout time zone AND crt_time < '2016-11-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

**Specify the start value of partitions to add a new range**

**partition**

You can create new partitions by specifying the start value of the partitions. If the ranges of the partitions that you want to create do not overlap with existing partitions, the partitions are created. This method allows you to create nonadjacent partitions. For example, if the range of existing partitions is from 2010 to 2015, you can create a partition from 2020. You do not need to create a partition between 2015 and 2020. Function:

```
add_range_partition(relation REGCLASS, -- The OID of the parent table
                    start_value    ANYELEMENT,  -- The start value.
                    end_value      ANYELEMENT,  -- The end value.
                    partition_name TEXT DEFAULT NULL,  -- The name of the partition.
                    tablespace     TEXT DEFAULT NULL)  -- The tablespace for the partiti
on.
```

Examples:

```
SELECT add_range_partition('part_test'::regclass, -- The OID of the parent table.
                    '2020-01-01 00:00:00'::timestamp,  -- The start value.
                    '2020-02-01 00:00:00'::timestamp); -- The end value.
\d+ part_test_27
                                Table "public.part_test_27"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_27_3_check" CHECK (crt_time >= '2020-01-01 00:00:00'::timestamp
without time zone AND crt_time < '2020-02-01 00:00:00'::timestamp without time zone) Inherits: part_test
```

**Delete a partition**

To delete a single range partition, call the following function:

```
drop_range_partition(partition TEXT, -- The name of the partition.
                    delete_data BOOLEAN DEFAULT TRUE) -- Specifies whether to delete t
he data of the partition. If you set the value to FALSE, the data of the partition is migrated to the parent table. Drop RANGE partition and all of its data if delete_data is true.
```

Delete all partitions and specify whether to migrate data to the parent table. Function:

```
drop_partitions(parent REGCLASS,
                delete_data BOOLEAN DEFAULT FALSE)
Drop partitions of the parent table (both foreign and local relations). If delete_data is false, the data is copied to the parent table first. Default is false.
```

Examples: Delete a partition and migrate the data of the partition to the parent table.

```
SELECT drop_range_partition('part_test_1',false); SELECT drop_range_partition('part_test_2',false);
```

Query the data of the current parent table.

```
SELECT count(*) FROM part_test;
 count
-------
 10000
(1 row)
```

Delete a partition and the data of the partition without migrating the data to the parent table.

```
SELECT drop_range_partition('part_test_3',true);
```

Query the data of the current parent table.

```
SELECT count(*) FROM part_test;
 count
------- (1 row) SELECT count(*) FROM ONLY part_test;
 count
------- (1 row)
```

Delete all partitions.

```
SELECT drop_partitions('part_test'::regclass, false); -- Delete all partitions and m igrate the data of partitions to the parent table.
```

Query the data of the parent table.

```
SELECT count(*) FROM part_test;
 count
------- (1 row)
```

**Attach a table to a partition**

You can attach an existing table to a partition of a parent table. The table that you want to attach must have the same schema as the parent table. For example, the two tables must have the same dropped columns. The pg_attribute parameter specifies the schema of a table. Function:

```
attach_range_partition(relation REGCLASS, -- The OID of the parent table.
                       partition   REGCLASS,    -- The OID of the partition.
                       start_value ANYELEMENT,  -- The start value of the range for the
partition.
                       end_value   ANYELEMENT)  -- The end value of the range for the pa
rtition.
```

Examples:
1. Create a table.

```
CREATE TABLE part_test_1 (like part_test including all);
```

2. Attach the table to a parent table.

```
\d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
\d+ part_test_1
                                 Table "public.part_test_1"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
SELECT attach_range_partition('part_test'::regclass, 'part_test_1'::regclass, '2019-0 1-01 00:00:00'::timestamp, '2019-02-01 00:00:00'::timestamp);
```

When you attach the table, inheritance relationships and constraints are automatically created.

```
\d+ part_test_1
                                 Table "public.part_test_1"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_1_3_check" CHECK (crt_time >= '2019-01-01 00:00:00'::timestamp
without time zone AND crt_time < '2019-02-01 00:00:00'::timestamp without time zone) Inherits: part_test
```

**Detach a partition**

When you detach a partition, the data is not deleted, but the inheritance and constraints are deleted. Function:

```
detach_range_partition(partition REGCLASS) -- Specify the partition that you want to c onvert into a common table.
```

Examples:
1. Query the data of the current parent table and the partitioned table.

```
SELECT count(*) FROM part_test;
 count
------- (1 row) SELECT count(*) FROM part_test_2;
 count
------- (1 row)
```

2. Unbind a partition.

```
SELECT detach_range_partition('part_test_2');
```

Query the data of the current parent table and the partitioned table.

```
SELECT count(*) FROM part_test_2;
 count
------- (1 row) SELECT count(*) FROM part_test;
 count
------- (1 row)
```

**Disable the pg_pathman extension**

You can disable the pg_pathman extension for a parent table. Function:

**Important**

The `disable_pathman_for` operation is irreversible. Proceed with caution.

```
\sf disable_pathman_for CREATE OR REPLACE FUNCTION public.disable_pathman_for(parent_relid regclass)
 RETURNS void
 LANGUAGE plpgsql
 STRICT
AS $function$ BEGIN
        PERFORM public.validate_relname(parent_relid);
        DELETE FROM public.pathman_config WHERE partrel = parent_relid;
        PERFORM public.drop_triggers(parent_relid);
        /* Notify backend about changes */
        PERFORM public.on_remove_partitions(parent_relid);
END $function$
```

Examples:

```
SELECT disable_pathman_for('part_test'); \d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Child tables: part_test_10,
              part_test_11,
              part_test_12,
              part_test_13,
              part_test_14,
              part_test_15,
              part_test_16,
              part_test_17,
              part_test_18,
              part_test_19,
              part_test_20,
              part_test_21,
              part_test_22,
              part_test_23,
              part_test_24,
              part_test_25,
              part_test_26,
              part_test_27,
              part_test_28,
              part_test_29,
              part_test_3,
              part_test_30,
              part_test_31,
parttest32
```

```
              part_test_32,
              part_test_33,
              part_test_34,
              part_test_35,
              part_test_4,
              part_test_5,
              part_test_6,
              part_test_7,
              part_test_8,
              part_test_9
\d+ part_test_10
                                Table "public.part_test_10"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descript
ion ----------+-----------------------------+-----------+----------+--------------+----------
```

`-`

```
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_10_3_check" CHECK (crt_time >= '2017-06-25 00:00:00'::timestamp
without time zone AND crt_time < '2017-07-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

After you disable the pg_pathman extension, the inheritance and constraints remain unchanged. The pg_pathman extension does not intervene in the custom scan execution plan. The following example describes the execution plan after the pg_pathman extension is disabled:

```
EXPLAIN SELECT * FROM part_test WHERE crt_time='2017-06-25 00:00:00'::timestamp;
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Append  (cost=0.00..16.00 rows=2 width=45)
   ->  Seq Scan on part_test  (cost=0.00..0.00 rows=1 width=45)
         Filter: (crt_time = '2017-06-25 00:00:00'::timestamp without time zone)
   ->  Seq Scan on part_test_10  (cost=0.00..16.00 rows=1 width=45)
         Filter: (crt_time = '2017-06-25 00:00:00'::timestamp without time zone)
(5 rows)
```

**Advanced partition management**

**Disable a parent table**

After all data of a parent table is migrated to the partitions, you can disable the parent table. Function:

```
set_enable_parent(relation REGCLASS, value BOOLEAN) Include/exclude parent table into/from query plan. In original PostgreSQL planner parent table is always included into query plan even if it's empty which can lead to additional overhead. You can use disable_parent() if you are never going to use parent table as a storage. Default value depends on the partition_data parameter that was specified during initial partitioning in create_range_partitions() or create_partitions_from_range() functions. If the partition_data parameter was true then all data have already been migrated to pa rtitions and parent table disabled. Otherwise it is enabled.
```

Examples:

```
SELECT set_enable_parent('part_test', false);
```

**Enable automatic partition propagation**

You can enable automatic partition propagation for a range-partitioned table. If the inserted data is not within the range of the existing partitions, a partition is automatically created.

```
set_auto(relation REGCLASS, value BOOLEAN) Enable/disable auto partition propagation (only for RANGE partitioning). It is enabled by default.
```

Examples:
1. Query the partitions of the current table.

```
\d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Child tables: part_test_10,
              part_test_11,
              part_test_12,
              part_test_13,
              part_test_14,
              part_test_15,
              part_test_16,
              part_test_17,
```

```
              part_test_18,
              part_test_19,
              part_test_20,
              part_test_21,
              part_test_22,
              part_test_23,
              part_test_24,
              part_test_25,
              part_test_26,
              part_test_3,
              part_test_4,
              part_test_5,
              part_test_6,
              part_test_7,
              part_test_8,
              part_test_9
\d+ part_test_26
                                Table "public.part_test_26"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_26_3_check" CHECK (crt_time >= '2018-09-25
00:00:00'::timestamp without time zone AND crt_time < '2018-10-25 00:00:00'::timestamp without time zone) Inherits: part_test \d+ part_test_25
                                Table "public.part_test_25"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Check constraints:
    "pathman_part_test_25_3_check" CHECK (crt_time >= '2018-08-25
00:00:00'::timestamp without time zone AND crt_time < '2018-09-25 00:00:00'::timestamp without time zone) Inherits: part_test
```

2. If you insert data that is outside the range of existing partitions, new partitions are created
based on the interval specified when the table was partitioned. This operation may require an extended period of time to complete.

```
INSERT INTO part_test VALUES (1,'test','2222-01-01'::timestamp);
```

Query the partitions.

```
\d+ part_test
                                  Table "public.part_test"
  Column  |            Type             | Modifiers | Storage  | Stats target | Descri
ption ----------+-----------------------------+-----------+----------+--------------+-------- ----
 id       | integer                     |           | plain    |              |
 info     | text                        |           | extended |              |
 crt_time | timestamp without time zone | not null  | plain    |              |
Child tables: part_test_10,
              part_test_100,
              part_test_1000,
              part_test_1001,
              ......
```

We recommend that you disable automatic partition propagation for range-partitioned tables because inappropriate automatic partition propagation may require an extended period of time to complete.

**Configure a callback function**

A callback function is automatically called each time a partition is created. For example, you can configure a callback function for DDL logical replication to store the statements in a table. Function:

```
set_init_callback(relation REGCLASS, callback REGPROC DEFAULT 0) Set partition creation callback to be invoked for each attached or created partition (b oth HASH and RANGE). The callback must have the following signature: part_init_callback(args JSONB) RETURNS VOID. Parameter arg consists of several fields whose presence depends on partitioning type: /* RANGE-partitioned table abc (child abc_4) */
```

`{`

```json
    "parent":    "abc",
    "parttype":  "2",
    "partition": "abc_4",
    "range_max": "401",
    "range_min": "301"
```

`}`

```
/* HASH-partitioned table abc (child abc_0) */
```

`{`

```json
    "parent":    "abc",
    "parttype":  "1",
    "partition": "abc_0"
```

`}` Examples:
1. Create a callback function.

```
CREATE OR REPLACE FUNCTION f_callback_test(jsonb) RETURNS void AS
```

$$

```
DECLARE BEGIN
  CREATE TABLE if NOT EXISTS rec_part_ddl(id serial primary key, parent name, parttyp
e int, partition name, range_max text, range_min text);
  if ($1->>'parttype')::int = 1 then
    raise notice 'parent: %, parttype: %, partition: %', $1->>'parent', $1->>'parttyp
e', $1->>'partition';
    INSERT INTO rec_part_ddl(parent, parttype, partition) values (($1-
>>'parent')::name, ($1->>'parttype')::int, ($1->>'partition')::name);
  elsif ($1->>'parttype')::int = 2 then
    raise notice 'parent: %, parttype: %, partition: %, range_max: %, range_min: %',
$1->>'parent', $1->>'parttype', $1->>'partition', $1->>'range_max', $1->>'range_min';
    INSERT INTO rec_part_ddl(parent, parttype, partition, range_max, range_min) value
s (($1->>'parent')::name, ($1->>'parttype')::int, ($1->>'partition')::name, $1->>'ran ge_max', $1->>'range_min');
  END if;
END; $$ LANGUAGE plpgsql strict;
```

2. Prepare the test table.

```
CREATE TABLE tt(id int, info text, crt_time timestamp not null); --- Configure a callback function for the test table. SELECT set_init_callback('tt'::regclass, 'f_callback_test'::regproc); --- Create partitions. SELECT create_range_partitions('tt'::regclass, -- The OID of the parent ta ble.
                        'crt_time',                        -- The name of the partition
key column.
                        '2016-10-25 00:00:00'::timestamp,  -- The start value of the r
ange for the first partition.
                        interval '1 month',                -- The range or span of valu
es that each partition covers.
                        24,                                -- The number of partitions.
                        false) ;
```

3. -- Check whether the callback function is called.

```
SELECT * FROM rec_part_ddl;
```

Sample result:

```
 id | parent | parttype | partition |      range_max      |      range_min
----+--------+----------+-----------+---------------------+---------------------
  1 | tt     |        2 | tt_1      | 2016-11-25 00:00:00 | 2016-10-25 00:00:00
  2 | tt     |        2 | tt_2      | 2016-12-25 00:00:00 | 2016-11-25 00:00:00
  3 | tt     |        2 | tt_3      | 2017-01-25 00:00:00 | 2016-12-25 00:00:00
  4 | tt     |        2 | tt_4      | 2017-02-25 00:00:00 | 2017-01-25 00:00:00
  5 | tt     |        2 | tt_5      | 2017-03-25 00:00:00 | 2017-02-25 00:00:00
  6 | tt     |        2 | tt_6      | 2017-04-25 00:00:00 | 2017-03-25 00:00:00
  7 | tt     |        2 | tt_7      | 2017-05-25 00:00:00 | 2017-04-25 00:00:00
  8 | tt     |        2 | tt_8      | 2017-06-25 00:00:00 | 2017-05-25 00:00:00
  9 | tt     |        2 | tt_9      | 2017-07-25 00:00:00 | 2017-06-25 00:00:00
 10 | tt     |        2 | tt_10     | 2017-08-25 00:00:00 | 2017-07-25 00:00:00
 11 | tt     |        2 | tt_11     | 2017-09-25 00:00:00 | 2017-08-25 00:00:00
 12 | tt     |        2 | tt_12     | 2017-10-25 00:00:00 | 2017-09-25 00:00:00
 13 | tt     |        2 | tt_13     | 2017-11-25 00:00:00 | 2017-10-25 00:00:00
 14 | tt     |        2 | tt_14     | 2017-12-25 00:00:00 | 2017-11-25 00:00:00
 15 | tt     |        2 | tt_15     | 2018-01-25 00:00:00 | 2017-12-25 00:00:00
 16 | tt     |        2 | tt_16     | 2018-02-25 00:00:00 | 2018-01-25 00:00:00
 17 | tt     |        2 | tt_17     | 2018-03-25 00:00:00 | 2018-02-25 00:00:00
 18 | tt     |        2 | tt_18     | 2018-04-25 00:00:00 | 2018-03-25 00:00:00
 19 | tt     |        2 | tt_19     | 2018-05-25 00:00:00 | 2018-04-25 00:00:00
 20 | tt     |        2 | tt_20     | 2018-06-25 00:00:00 | 2018-05-25 00:00:00
 21 | tt     |        2 | tt_21     | 2018-07-25 00:00:00 | 2018-06-25 00:00:00
 22 | tt     |        2 | tt_22     | 2018-08-25 00:00:00 | 2018-07-25 00:00:00
 23 | tt     |        2 | tt_23     | 2018-09-25 00:00:00 | 2018-08-25 00:00:00
 24 | tt     |        2 | tt_24     | 2018-10-25 00:00:00 | 2018-09-25 00:00:00
(24 rows)
```

### 12.18 zhparser

This topic describes how to enable the zhparser extension and customize a Chinese word segment dictionary in PolarDB for PostgreSQL.

**Enable the zhparser extension**

Execute the following statements to enable the zhparser extension:

```
CREATE EXTENSION zhparser; CREATE TEXT SEARCH CONFIGURATION testzhcfg (PARSER = zhparser); ALTER TEXT SEARCH CONFIGURATION testzhcfg ADD MAPPING FOR n,v,a,i,e,l WITH simple; --Optional parameter configuration ALTER role ALL SET zhparser.multi_short=on; --Perform a test.
```

SELECT * FROM ts_parse('zhparser', 'hello world! 2010年保障房建设在全国范围内获全面启动，从中央到地方纷纷加大了保障房的建设和投入力度。 `2011`年，保障房进入了更大规模的建设阶段。住房城乡建设部党组书记、部长姜伟新去年底在全国住房城乡建设工作会议上表示，要继续推进保障性安居工程建设。

```
');
```

SELECT to_tsvector('testzhcfg','“今年保障房新开工数量虽然有所下调，但实际的年度在建规模以及竣工规模会超以往年份，相对应的对资金的需求也会创历史纪录。”陈国强说。在他看来，与`2011`年相比，`2012`年的保障房建设在资金配套上的压力将更为严峻。 '); `SELECT to_tsquery('testzhcfg', '`保障房资金压力'); Execute the following statements to use the zhparser extension to run a full-text index:

```
--Create a full-text index for the name field of table T1 CREATE index idx_t1 ON t1 USING gin (to_tsvector('zhcfg',upper(name) )); --Use the full-text index
 SELECT * FROM t1 WHERE to_tsvector('zhcfg',upper(t1.name)) @@ to_tsquery('zhcfg','(防火
)') ;
```

**Customize a Chinese word segment dictionary**

Execute the following statements to customize a Chinese word segment dictionary:

```
-- The initial segmentation result
```

`SELECT to_tsquery('testzhcfg', '`保障房资金压力');

```
-- Insert a new word segment to the dictionary INSERT INTO pg_ts_custom_word VALUES ('保障房资'); -- Make the inserted word segment take effect SELECT zhprs_sync_dict_xdb(); -- End the connection
```

\c

```
-- Requery to obtain new segmentation results
```

`SELECT to_tsquery('testzhcfg', '`保障房资金压力'); Instructions to use custom word segments: A maximum of 1 million custom word segments can be added. If the number of word segments exceeds the limit, the word segments outside the limit are not processed. Ensure that the number of word segments is within this range. The custom and default word segment dictionaries take effect at the same time. Each word segment can be a maximum of 128 bytes in length. The section after the 128th byte will be truncated. After adding, deleting, or changing word segments, execute the `SELECT` zhprs_sync_dict_xdb(); statement and re-establish a connection to make the operation take effect.

### 12.19 pldebugger

PolarDB for PostgreSQL supports multiple stored procedure languages (SPLs) such as PL/pgSQL, PL/Python, PL/Perl, PL/Tcl, and PL/Java. You can use these SPLs to create functions or stored procedures. PolarDB provides the pldebugger extension to debug stored procedures.

**Prerequisites**

The version of the pgAdmin 4 client is v4.19 or later. For more information about how to download the pgAdmin 4 client, see Download.

**Create the pldebugger extension**

Create and debug the pldebugger extension by using a privileged account.

```
CREATE EXTENSION IF NOT EXISTS pldbgapi;
```

**Use the pldebugger extension**

1. Use pgAdmin 4 to connect to the PolarDB cluster.
2. Find the function to be debugged, right-click the function, and choose **Debugging >**
**Debug**.
3. Use the pldebugger extension in pgAdmin 4.
In the function debugging section on the right of the pgAdmin 4 page, you can perform step-by-step operations to debug the function, such as `step into/over` , `continue` , set breakpoints, and stop. At the bottom of the pgAdmin 4 page, you can view the local variables, debugging results, and function stacks during debugging.

**Monitor connections to pldebugger**

PolarDB allows you to monitor the connections to pldebugger. You can use the following function to query the number of existing connections and the default maximum number of connections to pldebugger.

```
SELECT * FROM polar_monitor_pldebugger_count();
```

Sample result:

```
 current_connection | max_connection
--------------------+----------------
                  6 |              6
(1 row)
```

`current_connection` : the number of existing connections. `max_connection` : the default maximum number of connections. The preceding example shows that six connections are used. Each pldebugger debugging process requires two connections. Therefore, three debugging processes exist in the preceding example. A maximum of three pldebugger processes are allowed.

### 12.20 Use PASE for efficient vector search

**vector search**

This topic describes how to use the PostgreSQL ANN search extension (PASE) to search for vectors in PolarDB for PostgreSQL. PASE works based on the IVFFlat or Hierarchical Navigable Small World (HNSW) algorithm.

**Background information**

Representation learning is a typical AI technology in the deep learning discipline. This technology has rapidly developed over the recent years and is used in various business scenarios such as advertising, facial recognition-based payment, image recognition, and speech recognition. This technology enables data to be embedded into high-dimensional vectors and allows you to query data by using the vector search approach. PASE is a high-performance vector search index plug-in that is developed for PostgreSQL. PASE uses two well-developed, stable, and efficient approximate nearest neighbor (ANN) search algorithms, IVFFlat and HNSW, to query vectors from PostgreSQL databases at high speeds. PASE does not support the extraction or output of feature vectors. You must retrieve the feature vectors of the entities that you want to query. PASE only implements a similarity search among a large number of vectors that are identified based on the retrieved feature vectors.

**Intended audience**

This topic does not explain the terms related to machine learning in detail. Before you read this topic, you must understand the basics of machine learning and search technologies.

**Usage notes**

If an index on a table is bloated, you can obtain the size of the indexed data by executing the select pg_relation_size('Index name'); statement. Then, compare the size of the index with the size of the data in the table. If the size of the indexed data is larger than the size of the data in the table and data queries slow down, you must rebuild the index on the table. An index on a table may be inaccurate after frequent data updates. If you require an accuracy level of 100%, you must rebuild the index on a regular basis. If you want to create an IVFFlat index on a table by using internal centroids, you must set the clustering_type parameter to 1 and insert data into the table. You must use a privileged account to execute the SQL statements that are described in this topic.

**Limits**

Only sequential search for high-dimensional vectors is supported in cross-node parallel execution.

**Algorithms used by PASE**

IVFFlat IVFFlat is a simplified version of the IVFADC algorithm. IVFFlat is suitable for business scenarios that require high precision but can tolerate up to 100 milliseconds taken for queries. IVFFlat has the following advantages compared with other algorithms: If the vector to query is one of the candidate datasets, IVFFlat delivers 100% recall. IVFFlat uses a simple structure to create indexes at fast speeds, and the created indexes occupy less storage. You can specify a centroid for clustering and reconfigure parameters to control precision. The algorithm parameters are interpretable, which allows users to fully control the accuracy of the algorithm. The following figure shows how IVFFlat works. The following procedure describes how IVFFlat works: i. IVFFlat uses a clustering algorithm such as k-means to divide vectors in the highdimensional space into clusters based on implicit clustering properties. This way, each cluster has a centroid. ii. IVFFlat traverses the centroids of all clusters to identify the n centroids that are nearest to the vector that you want to query. iii. IVFFlat traverses and sorts all vectors in the clusters to which the identified n centroids belong. Then, IVFFlat obtains the nearest k vectors. When IVFFlat attempts to identify the nearest n centroids, IVFFlat skips the clusters that are located far from the vector that you want to query. This expedites the query. However, IVFFlat cannot ensure that all the similar k vectors are included in the clusters to which the identified n centroids belong. As a result, precision may decrease. You can use the variable n to control precision. A larger value of n indicates higher precision but more computing workloads. In the first phase, IVFFlat works in the same way as IVFADC. The main differences between IVFFlat and IVFADC lie in the second phase. In the second phase, IVFADC uses product quantization to eliminate the need for traversal computing workloads. This expedites the query but decreases precision. IVFFlat implements brute-force search to ensure precision and allows you to control computing workloads. HNSW HNSW is a graph-based ANN algorithm that is suitable for queries among tens of millions or more vector datasets. Responses to these queries must be returned within 10 milliseconds or less. HNSW searches for similar vectors among proximity graph neighbors. If the data volume is large, HNSW significantly improves performance compared with other algorithms. However, HNSW requires the storage of proximity graph neighbors, which occupy storage space. In addition, after the precision of HNSW reaches a specific level, you cannot increase the precision of HNSW by reconfiguring parameters. The following figure shows how HNSW works. The following procedure describes how HNSW works: i. HNSW builds a hierarchical structure that consists of multiple layers, which are also called graphs. Each layer is the panorama and skip list of its lower layer. ii. HNSW randomly selects an element from the top layer to start a search. iii. HNSW identifies the neighbors of the selected element and adds the identified neighbors to a fixed-length dynamic list based on the distances of the identified neighbors to the selected element. HNSW continues to identify the neighbors of each neighbor that is included in the list and adds the identified neighbors to the list. Every time HNSW adds a neighbor to the list, HNSW re-sorts the neighbors in the list and retains only the first k neighbors. If the list changes, HNSW continues to search until the list reaches the final state. Then, HNSW uses the first element in the list as the start for a search in the lower layer. iv. HNSW repeats the third step until it completes a search in the bottom layer. HNSW constructs a multi-layer structure by using the Navigable Small World (NSW) algorithm that is designed to construct single-layer structures. The employment of an approach for selecting proximity graph neighbors enables HNSW to deliver higher query speedup than clustering algorithms. IVFFlat and HNSW are suitable for specific business scenarios. For example, IVFFlat is suitable for image comparison at high precision, and HNSW is suitable for searches with recommended recall. More industry-leading algorithms will be integrated into PASE.

**PASE usage**

1. Execute the following statement to create PASE:

```
CREATE EXTENSION pase;
```

2. Use one of the following construction methods to calculate vector similarity:
PASE-type-based construction Examples

```
SELECT ARRAY[2, 1, 1]::float4[] <?> pase(ARRAY[3, 1, 1]::float4[]) AS distance; SELECT ARRAY[2, 1, 1]::float4[] <?> pase(ARRAY[3, 1, 1]::float4[], 0) AS distance; SELECT ARRAY[2, 1, 1]::float4[] <?> pase(ARRAY[3, 1, 1]::float4[], 0, 1) AS distance;
```

<?> is a PASE-type operator, which is used to calculate the similarity between the vectors to the left and right of a specific element. The vector to the left must use the float4[] data type, and the vector to the right must use the PASE data type. The PASE data type is defined in PASE and can contain up to three constructors. Take the `float4[], 0, 1` part in the preceding third statement as an example. The first parameter specifies the vector to the right with the float4[] data type. The second parameter does not serve a special purpose and can be set to 0. The third parameter specifies the similarity calculation method, where the value 0 represents the Euclidean distance method and the value 1 represents the dot product method. A dot product is also called an inner product. The vector to the left must have the same number of dimensions as the vector to the right. Otherwise, the system reports similarity calculation errors. String-based construction Examples

```
SELECT ARRAY[2, 1, 1]::float4[] <?> '3,1,1'::pase AS distance; SELECT ARRAY[2, 1, 1]::float4[] <?> '3,1,1:0'::pase AS distance; SELECT ARRAY[2, 1, 1]::float4[] <?> '3,1,1:0:1'::pase AS distance;
```

The string-based construction method differs from the PASE-type-based construction in the following aspect: The string-based construction method uses colons (:) to separate parameters. Take the `3,1,1:0:1` part in the preceding third statement as an example: The first parameter specifies the vector to the right. The second parameter does not serve a special purpose and can be set to 0. The third parameter specifies the similarity calculation method, where the value 0 represents the Euclidean distance method and the value 1 represents the dot product method. A dot product is also called an inner product.
3. Use IVFFlat or HNSW to create an index.
If you use the Euclidean distance method to calculate a vector similarity, the original vector does not need to be processed. If you use the dot product or the cosine method to calculate a vector similarity, the original vector must be normalized. For example, if the original vector is , it must comply with the following formula: . In this example, the dot product is the same as the cosine value. IVFFlat Examples

```
CREATE INDEX ivfflat_idx ON vectors_table USING
  pase_ivfflat(vector)
WITH
  (clustering_type = 1, distance_type = 0, dimension = 256, base64_encoded = 0, clu
stering_params = "10,100");
```

The following table describes the parameters.

| Parameter | Description |
|---|---|

| clustering type _ | The type of clustering operation that IVFFlat performs on vectors. This parameter is required. Valid values: 0: external clustering. An external centroid file is loaded. This file is specified by the clustering params parameter. _ 1: internal clustering. Internal clustering that uses the k-means clustering algorithm is performed. This algorithm is specified by the clustering params parameter. _ If you are using PASE for the first time, we recommend that you select internal clustering. |
|---|---|
| distance type _ | The method that is used to calculate the vector similarity. Default value: 0. Valid values: 0: Euclidean distance. 1: dot product. This method requires the normalization of vectors. The order of dot products is opposite to the order of Euclidean distances. ApsaraDB RDS for PostgreSQL supports only the Euclidean distance method. Dot products can be calculated by using the methods that are described in Appendix only after vectors are normalized. |
| dimension | The number of dimensions. This parameter is required. The maximum value of this parameter is 512. |
| base64 encoded _ | Specifies whether to use Base64 encoding. Default value: 0. Valid values: 0: uses the float4[] data type to represent the vector type. 1: uses the Base64-encoded float[] data type to represent the vector type. |
| clustering params _ | For external clustering, this parameter specifies the directory of the external centroid file that you want to use. For internal clustering, this parameter specifies the clustering algorithm that you want to use. The value of this parameter is in the following format clustering sample ratio,k . This parameter is required. _ _ clustering sample ratio: the sampling fraction with 1000 as the _ _ denominator. The value of this field is an integer within the (0,1000] range. For example, if you set this field to 1, the system samples data from the dynamic list based on the 1/1000 sampling ratio before it performs k-means clustering. A larger value indicates higher query accuracy but slower index creation. We recommend that the total number of data records sampled should not exceed 100,000. k: the number of centroids. A larger value indicates higher query accuracy but slower index creation. We recommend that you set this field to a value within the [100,1000] range. |

HNSW Examples

```
CREATE INDEX hnsw_idx ON vectors_table USING
  pase_hnsw(vector)
WITH
  (dim = 256, base_nb_num = 16, ef_build = 40, ef_search = 200, base64_encoded = 0)
```

; The following table describes the parameters.

| Parameter | Description |
|---|---|
| dim | The number of dimensions. This parameter is required. The maximum value of this parameter is 512. |
| base nb num _ _ | The number of neighbors that you want to identify for an element. This parameter is required. A larger value indicates higher query accuracy, but slower index creation and more storage space occupied. We recommend that you set this parameter to a value within the [16,128] range. |
| ef build _ | The heap length that you want to use during index creation. This parameter is required. A longer heap length indicates higher query accuracy but slower index creation. We recommend that you set this parameter to a value within the [40,400] range. |
| ef search _ | The heap length that you want to use during a query. This parameter is required. A longer heap length indicates higher query accuracy but lower query performance. You can specify this parameter when you initiate a query request. Default value: 200. |
| base64 encoded _ | Specifies whether to use Base64 encoding. Default value: 0. Valid values: 0: uses the float4[] data type to represent the vector type. 1: uses the Base64-encoded float[] data type to represent the vector type. |

4. Use one of the following indexes to query a vector:
IVFFlat index Examples

```
SELECT id, vector <#> '1,1,1'::pase as distance FROM vectors_ivfflat ORDER BY vector <#> '1,1,1:10:0'::pase ASC LIMIT 10;
```

<#> is an operator that is used by IVFFlat indexes. You must execute the ORDER BY statement to make an IVFFlat index take effect. An IVFFlat index allows vectors to be sorted in ascending order. The PASE data type requires three parameters to specify a vector. These parameters are separated by colons (:). For example, `1,1,1:10:0` includes three parameters. The first parameter specifies the vector to query. The second parameter specifies the query efficiency of IVFFlat with a value range of (0,1000], in which a larger value indicates higher query accuracy but poorer query performance. The third parameter specifies the vector similarity calculation method, where the value 0 represents the Euclidean distance method and the value 1 represents the dot product method. A dot product is also called an inner product. The dot product method requires the normalization of vectors. The order of dot products is opposite to the order of Euclidean distances. HNSW index Examples

```
SELECT id, vector <?> '1,1,1'::pase as distance FROM vectors_ivfflat ORDER BY vector <?> '1,1,1:100:0'::pase ASC LIMIT 10;
```

<?> is an operator that is used by the HNSW index. You must execute the ORDER BY statement to make an IVFFlat index take effect. An IVFFlat index allows vectors to be sorted in ascending order. The PASE data type requires three parameters to specify a vector. These parameters are separated by colons (:). For example, `1,1,1:10:0` includes three parameters. The first parameter specifies the vector to query. The second parameter specifies the query efficiency of HNSW with a value range of (0, ∞), in which a larger value indicates higher query accuracy but lower query performance. We recommend that you set the second parameter to 40 and then test the value by small increases until you find the most suitable value for your business. The third parameter specifies the vector similarity calculation method, where the value 0 represents the Euclidean distance method and the value 1 represents the dot product method. A dot product is also called an inner product. The dot product method requires the normalization of vectors. The order of dot products is opposite to the order of Euclidean distances.

**Appendix**

Calculate the dot product of a vector. For this example, use an HNSW index to create a function:

```
CREATE OR REPLACE FUNCTION inner_product_search(query_vector text, ef integer, k inte ger, table_name text) RETURNS TABLE (id integer, uid text, distance float4) AS $$ BEGIN
    RETURN QUERY EXECUTE format('
    select a.id, a.vector <?> pase(ARRAY[%s], %s, 1) AS distance from
    (SELECT id, vector FROM %s ORDER BY vector <?> pase(ARRAY[%s], %s, 0) ASC LIMIT %
s) a
    ORDER BY distance DESC;', query_vector, ef,  table_name,  query_vector, ef, k);
END
```

$$

```
LANGUAGE plpgsql;
```

The dot product of a normalized vector is the same as its cosine value. Therefore, you can also follow this example to calculate the cosine value of a vector. Create an IVFFlat index from an external centroid file. This is an advanced feature. You must upload an external centroid file to the specified directory of the server and use this file to create an IVFFlat index. This file is in the following format:

```
Number of dimensions|Number of centroids|Centroid vector dataset
```

Examples

```
3|2|1,1,1,2,2,2
```

**References**

Product Quantization for Nearest Neighbor Search Herve J ́egou, Matthijs Douze, Cordelia Schmid. Product quantization for nearest neighbor search. Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs Yu.A.Malkov, D.A.Yashunin. Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs.

### 12.21 pg_hint_plan

This topic describes the pg_hint_plan extension. You can use this extension to add hints to SQL statements. The hints specify how you want the SQL statements to be executed. This way, you can optimize the execution plans of the SQL statements.

**Background information**

PostgreSQL uses a cost-based optimizer that works based on data statistics rather than static rules. The optimizer evaluates the costs of all possible execution plans for an SQL statement, and executes the execution plan with the lowest cost. The optimizer makes the best effort, but the selected execution plan may not be the best one, because the optimizer does not consider the underlying relationships among data. You can specify Grand Unified Configuration (GUC) variables to adjust the execution plan, but this would affect the entire session. If you do not want to affect the entire session, you can use the pg_hint_plan extension to optimize a single execution plan.

**Usage notes**

Data Management (DMS) does not support hints. You must use other methods to access your database. The pg_hint_plan extension reads hints from only the first comment block. The pg_hint_plan extension accepts only letters, digits, spaces, and specific special characters, and immediately stops parsing when it identifies other characters. The accepted special characters include _ , ( ) The pg_hint_plan extension compares object names in a case-sensitive way, which is different from how PostgreSQL compares object names. For example, an object named **TBL** in a hint matches only **TBL** in a database. Objects named **tbl** or **Tbl** are ignored.

**Limitations**

The use of the pg_hint_plan extension for a stored procedure defined by using PL/pgSQL is subject to the following limitations: Hints take effect only for the following types of statements: SELECT, INSERT, UPDATE, and DELETE statements. RETURN QUERY statements. EXECUTE QUERY statements. OPEN statements. FOR statements. A hint must be placed immediately after the first word of an SQL statement. If the hint is placed before the first word, the hint is not considered part of the statement.

**Create and load the pg_hint_plan extension**

1. Create the extension.

```
CREATE EXTENSION pg_hint_plan;
```

2. Load the extension.
Automatically load the extension for a single user. Execute the following statement to load the extension.

```
ALTER USER xxx set session_preload_libraries='pg_hint_plan';
```

Replace xxx in the statement with the actual username. Execute the following statement to load the extension for a single database.

```
ALTER DATABASE xxx set session_preload_libraries='pg_hint_plan';
```

If the account cannot log in to the database due to improper configurations, execute one of the following statements to log in to PolarDB through another account or database and reset the configurations.

```
ALTER USER xxx reset session_preload_libraries; ALTER DATABASE xxx reset session_preload_libraries;
```

Automatically load the extension for a database cluster. You need to apply to add the pg_hint_plan extension. Check whether the extension is loaded. a. Execute the following statements to allow debugging information to be sent to the client.

```
SET pg_hint_plan.debug_print TO on; SET pg_hint_plan.message_level TO notice;
```

b. Execute the following statement to check whether the extension is loaded.

```
/*+Set(enable_seqscan 1)*/select 1;
```

If the extension is loaded, the following information is returned.

```
NOTICE: pg_hint_plan: used hint: Set(enable_seqscan 1)
```

c. Execute the following statements to stop sending debugging information to the client.

```
RESET pg_hint_plan.debug_print; RESET pg_hint_plan.message_level;
```

**Usage**

**Basic usage**

A hint starts with the combination of a forward slash, an asterisk, and a plus sign ( `/*+` ) and ends with the combination of an asterisk and a forward slash ( `*/` ). A hint consists of the hint name and the parameters. The parameters are enclosed in a pair of parentheses () and are separated by spaces. For readability purposes, you can start each hint on a new line. Example In this example, HashJoin is used as the joining method, and the pgbench_accounts table is scanned by using the SeqScan method.

```
/*+
   HashJoin(a b)
   SeqScan(a)
```

`*/`

```
EXPLAIN SELECT *
   FROM pgbench_branches b
   JOIN pgbench_accounts a ON b.bid = a.bid
   ORDER BY a.aid;
```

Sample result:

```
                                      QUERY PLAN
---------------------------------------------------------------------------------------
 Sort  (cost=31465.84..31715.84 rows=100000 width=197)
   Sort Key: a.aid
   ->  Hash Join  (cost=1.02..4016.02 rows=100000 width=197)
         Hash Cond: (a.bid = b.bid)
         ->  Seq Scan on pgbench_accounts a  (cost=0.00..2640.00 rows=100000 width=97)
         ->  Hash  (cost=1.01..1.01 rows=1 width=100)
               ->  Seq Scan on pgbench_branches b  (cost=0.00..1.01 rows=1 width=100)
(7 rows)
```

**Hint types**

**Hint types**

Hints are classified into the following six types based on how they affect execution plans:

**Hints for scan methods**

This type of hint specifies the method that is used to scan the specified table. If the specified table has an alias, the pg_hint_plan extension identifies the table based on the alias. Supported scan methods include SeqScan and IndexScan. The hints for scan methods are effective on ordinary tables, inherited tables, unlogged tables, temporary tables, and system tables. However, the hints for scan methods are not effective on external tables, table functions, statements in which the values of constants are specified, universal expressions, views, and subqueries. Example:

```
/*+
    SeqScan(t1)
    IndexScan(t2 t2_pkey)
```

`*/`

```
 SELECT * FROM table1 t1 JOIN table table2 t2 ON (t1.key = t2.key);
```

**Hints for join methods**

This type of hint specifies the method that is used to join the specified tables. The hints for join methods are effective on ordinary tables, inherited tables, unlogged tables, temporary tables, external tables, system tables, table functions, statements in which the values of constants are specified, and universal expressions. The hints for join methods are not effective on views and subqueries.

**Hints for join order**

This type of hint specifies the order in which two or more tables are joined. You can use one of the following methods to specify a hint for join order: Specify the order in which you want to join the specified tables without restricting the direction at each join level. Specify the order in which you want to join the specified tables and the direction at each join level. Example:

```
 /*+
    NestLoop(t1 t2)
    MergeJoin(t1 t2 t3)
    Leading(t1 t2 t3)
```

`*/`

```
 SELECT * FROM table1 t1
     JOIN table table2 t2 ON (t1.key = t2.key)
     JOIN table table3 t3 ON (t2.key = t3.key);
```

Components: `NestLoop(t1 t2)` : specifies the method for joining the t1 and t2 tables. `MergeJoin(t1 t2 t3)` : specifies the method for joining the t1, t2, and t3 tables. `Leading(t1 t2 t3)` : specifies the order in which the three tables are joined.

**Hints for row number correction**

This type of hint corrects row number errors that are caused by the restrictions of the optimizer.

```
 /*+ Rows(a b #10) */ SELECT... ; # Sets the row number of join results to 10.
 /*+ Rows(a b +10) */ SELECT... ; # Increases the row number by 10.
 /*+ Rows(a b -10) */ SELECT... ; # Decreases the row number by 10.
 /*+ Rows(a b *10) */ SELECT... ; # Increases the row number by 10 times.
```

**Hints for parallel execution**

This type of hint specifies the plan that is used to execute SQL statements in parallel. The hints for parallel execution are effective on ordinary tables, inherited tables, unlogged tables, and system tables. However, the hints for parallel execution are not effective on external tables, clauses in which the values of constants are specified, universal expressions, views, and subqueries. You can specify the internal tables of a view by their real names or aliases. The following examples show how an SQL statement is executed in a different way on each table: Example 1: Set the degree of parallelism (DOP) for the c1 table to 3, and that for the c2 table to 5.

```
EXPLAIN /*+ Parallel(c1 3 hard) Parallel(c2 5 hard) */
       SELECT c2.a FROM c1 JOIN c2 ON (c1.a = c2.a);
```

Sample result:

```
                                  QUERY PLAN
-------------------------------------------------------------------------------
 Hash Join  (cost=2.86..11406.38 rows=101 width=4)
   Hash Cond: (c1.a = c2.a)
   ->  Gather  (cost=0.00..7652.13 rows=1000101 width=4)
         Workers Planned: 3
         ->  Parallel Seq Scan on c1  (cost=0.00..7652.13 rows=322613 width=4)
   ->  Hash  (cost=1.59..1.59 rows=101 width=4)
         ->  Gather  (cost=0.00..1.59 rows=101 width=4)
               Workers Planned: 5
               ->  Parallel Seq Scan on c2  (cost=0.00..1.59 rows=59 width=4)
```

Example 2: Set the DOP for the t1 table to 5.

```
EXPLAIN /*+ Parallel(tl 5 hard) */ SELECT sum(a) FROM tl;
```

Sample result:

```
                                    QUERY PLAN
-----------------------------------------------------------------------------------
 Finalize Aggregate  (cost=693.02..693.03 rows=1 width=8)
   ->  Gather  (cost=693.00..693.01 rows=5 width=8)
         Workers Planned: 5
         ->  Partial Aggregate  (cost=693.00..693.01 rows=1 width=8)
               ->  Parallel Seq Scan on tl  (cost=0.00..643.00 rows=20000 width=4)
```

**Hints for GUC parameter setting**

This type of hint temporarily changes the value of a GUC parameter. The values of GUC parameters take effect only when the executor generates execution plans. The values help you improve the query performance without affecting the entire session. If you set more than one hint on a GUC parameter, the latest hint takes effect. Example:

```
 /*+ Set(random_page_cost 2.0) */
 SELECT * FROM table1 t1 WHERE key = 'value';
```

**List of hint syntaxes**

The following table lists all supported hint syntaxes. You can add the hints as comments to your queries to serve specific purposes. Optional parameters are enclosed in pairs of brackets ([ ]) in the syntax.

| Type | Hint syntax | Description |
|---|---|---|
| Hints for scan methods | SeqScan(table) | Specifies a sequence scan. |
|   | TidScan(table) | Specifies a TID scan. |
|   | IndexScan(table[ index...]) | Specifies an index scan. You can specify an index. |
|   | IndexOnlyScan(table[ index...]) | Specifies an index-only scan. You can specify an index. |
|   | BitmapScan(table[ index...]) | Specifies a bitmap scan. You can specify an index. |
|   | NoSeqScan(table) | Prohibits a sequence scan. |
|   | NoTidScan(table) | Prohibits a TID scan. |
|   | NoIndexScan(table) | Prohibits an index scan. |
|   | NoIndexOnlyScan(table) | Prohibits an index scan. Only tables are scanned. |
|   | NoBitmapScan(table) | Prohibits a bitmap scan. |
| Hints for join methods | NestLoop(table table[ table...]) | Specifies a nested loop join. |
|   | HashJoin(table table[ table...]) | Specifies a hash join. |
|   | MergeJoin(table table[ table...]) | Specifies a merge join. |
|   | NoNestLoop(table table[ table...]) | Prohibits a nested loop join. |

|   | NoHashJoin(table table[ table...]) | Prohibits a hash join. |
|---|---|---|
|   | NoMergeJoin(table table[ table...]) | Prohibits a merge join. |
| Hints for join order | Leading(table table[ table...]) | Specifies the join order. |
|   | Leading(<join pair>) | Specifies the join order and direction. |
| Hints for row number correction | Rows(table table[ table...] correction) | Corrects the row number of the join result that is obtained from the specified tables. The following operators are supported: # <n>, + <n>, -<n>, and * <n>. The <n> operator is supported by the strtod function. |
| Hints for parallel execution | Parallel(table <# of workers> [soft\|hard]) | Specifies or prohibits the parallel execution of the specified tables. Note The <# of workers> parameter specifies the number of working programs that are required. The value 0 specifies to prohibit parallel execution. If the third parameter is set to soft, only the value of the max parallel workers per gath _ _ _ _ er parameter is changed, and the other parameters are specified by the optimizer. The third parameter is set to soft by default. If the third parameter is set to hard, the values of all related parameters are changed. |

|   | PX(<# of workers>) | Specifies a cross-node parallel execution. Note <# of workers> specifies the DOP. |
|---|---|---|
|   | NoPX() | Prohibits a cross-node parallel execution. |
| Hints for GUC parameter setting | Set(GUC-param value) | Specifies the value of a GUC parameter when the optimizer runs. |

The pg_hint_plan extension can also specify the execution plan generated during a cross-node parallel execution. During a cross-node parallel execution, the Rows(table table[ table...] correction) hint is not supported. The hints for join methods can be used only to join two tables, and the hints for join order can be used only for all tables.

### 12.22 varbitx

The varbit extension that is provided in the PostgreSQL Community edition supports only simple BIT-type operation functions. The varbitx extension in PolarDB for PostgreSQL supports more BIT-type operations in more scenarios. These scenarios include real-time user profile recommendation, access control advertising, and ticketing.

**Functions**

| Function |   | Description |   |   |
|---|---|---|---|---|
| get bit (varbit a, int b, int _ |   | Obtains a specified number c of bits that start at position b and returns a VARBIT-type string. For example, get bit('111110000011', 3, 5) returns _ 11000. |   |   |
|   | get bit (varbit a, int b, int _ | and returns a VA |   |   |
| c) returns varbit |   |   |   |   |
| set bit array (varbit a, int b, _ _ int c, int[] d) returns varbit |   | Changes the values of the bits that are specified by the subscript array d to values b (0 or 1), and fills the bits that exceed the original length with values c (0 or 1). For example, set bit array('111100001111', 0, 1, _ _ array[1,15]) returns 1011000011111110. |   |   |
|   |   |   | set bit array('111100001111', 0, 1, _ _ |   |
| bit count (varbit a, int b, int _ c, int d) returns int |   | Counts the number of values b (0 or 1) that start at position c among a specified number d of bits. The bits that are beyond the specified length are not counted. For example, bit count('1111000011110000', 1, 5, _ 4) returns 1 (0001). |   |   |
|   |   | 4) |   |   |

|   | set bit array (varbit a, int b, _ _ | exceed the original length with va |
|---|---|---|
| int c, int[] d) returns varbit |   |   |

|   | bit count (varbit a, int b, int _ | beyond the specified le |
|---|---|---|
| c, int d) returns int |   |   |

| bit count (varbit a, int b) _ returns int |   | Counts the total number of values b (0 or 1). For example, bit count('1111000011110000', 1) _ returns 8. |   |   |   |
|---|---|---|---|---|---|
| bit fill (int a, int b) returns _ |   | Fills a specified number b of bits with values a (0 or 1). For example, bit fill(0,10) returns 0000000000. _ |   |   |   |
|   | bit fill (int a, int b) returns _ | Fills a |   |   |   |
| varbit |   |   |   |   |   |
| bit rand (int a, int b, float _ c) returns varbit |   | Obtains a random percentage c of bits from a specified number a of bits, and randomly fills the obtained bits with values b (0 or 1). For example, bit rand(10, 1, 0.3) may return _ 0101000001. |   |   |   |
| bit posite (varbit a, int b, _ boolean c) returns int[] |   | Returns a subscript array. The subscript array indicates the positions of the bits whose values are b (0 or 1). Subscripts start at 0. If the value of c is true, subscripts are returned in a positive sequence. If the value of c is false, subscripts are returned in a negative sequence. For example, bit posite ('11110010011', 1, true) _ returns [0,1,2,3,6,9,10], and bit posite _ ('11110010011', 1, false) returns [10,9,6,3,2,1,0]. |   |   |   |
| bit posite (varbit a, int b, _ int c, boolean d) returns int[] |   | Returns a subscript array. The subscript array indicates the positions of the bits whose values are b (0 or 1). The number of subscripts in the subscript array is c. Subscripts start at 0. If the value of d is true, subscripts are returned in a positive sequence. If the value of d is false, subscripts are returned in a negative sequence. For example, bit posite ('11110010011', 1, 3, _ true) returns [0,1,2], and bit posite _ ('11110010011', 1, 3, false) returns [10,9,6]. |   |   |   |
|   |   |   | bit posite ('11110010011', 1, 3, _ |   |   |
|   |   |   |   | bit posite _ |   |
| get bit array (varbit a, int b, _ _ int c, int d) returns int[] |   | Obtains a specified number c of bits that start at position b, identifies the bits whose values are d (0 or 1) among the obtained bits, and returns a subscript array. The subscript array indicates the positions of the identified bits. For example, get bit array('111110000011', 3, 5, _ _ 1) returns [3,4] for the specified 11000 bit string. |   |   |   |
|   |   | 1) |   |   |   |

|   | bit count (varbit a, int b) _ | Counts |
|---|---|---|
| returns int |   |   |

|   | bit posite (varbit a, int b, _ | returned in a negative s |   |
|---|---|---|---|
| boolean c) returns int[] |   |   |   |

|   | ('11110010011', 1, false) |
|---|---|

|   | bit posite (varbit a, int b, _ | a positive sequence. If the value |
|---|---|---|
| int c, boolean d) returns int[] |   |   |

|   |   | true) |
|---|---|---|

|   | get bit array (varbit a, int b, _ _ | obtained bits, and returns a su array indicates the positions o |
|---|---|---|
| int c, int d) returns int[] |   |   |

|   | get bit array (varbit a, int b, _ _ int[] c) returns int[] |   |   |   | Obtains the bits that are specified by a subscript array c, identifies the bits whose values are b (0 or 1) among the obtained bits, and returns a subscript array. The subscript array indicates the positions of the identified bits. The bits that are not included in the subscript array c are not counted. For example, get bit array('111110000011', 1, _ _ array[1,5,6,7,10,11]) returns [1,10,11]. |   |
|---|---|---|---|---|---|---|
|   | set bit array (varbit a, int b, _ _ |   |   |   | Changes the values of the bits that are specified by a subscript array d to values b (0 or 1), and fills the bits that are beyond the original length with values c (0 or 1). The number of bits that are returned is e. For example, set bit array('111100001111', 1, 0, _ _ array[4,5,6,7], 2) returns 111111001111. |   |
|   |   | set bit array (varbit a, int b, _ _ |   |   | subscript array d to values b (0 or 1), and are beyond the original length with values |   |
|   | int c, int[] d, int e) returns |   |   |   |   |   |
|   |   |   |   |   | nu |   |
|   | varbit |   |   |   |   | set bit array('111100001111', 1, 0, _ _ |
|   |   |   |   |   | _ array[4,5,6,7], 2) | _ |
|   | set bit array record (varbit a, _ _ _ |   |   |   | Changes the values of the bits that are specified by a subscript array d to values b (0 or 1), and fills the bits that are beyond the original length with values c (0 or 1). This function not only returns a bit string but also a subscript array. The subscript array indicates the positions of the bits whose values are changed. For example, set bit array record('111100001111', _ _ _ 0, 1, array[1,15]) returns 1011000011111110 and [1,15]. |   |
|   |   | set bit array record (varbit a, _ _ _ |   |   | function not only returns a bit string but also a subs array. The subscript array indicates the positions of |   |
|   | int b, int c, int[] d) returns |   |   |   | array. The s |   |
|   |   |   |   |   | whose value |   |
|   | (varbit,int[]) |   |   |   |   |   |
|   |   |   |   |   |   | set bit array record('111100001111', _ _ _ |
|   |   |   |   |   | 0, 1, array[1,15]) |   |
|   | set bit array record (varbit a, _ _ _ |   |   |   | Changes the values of the bits that are specified by a subscript array d to values b (0 or 1), and fills the bits that are beyond the original length with values c (0 or 1). This function not only returns a bit string but also a subscript array. The subscript array indicates the positions of the bits whose values are changed. This function returns results immediately after it changes values for a total of e bits. For example, set bit array record('111100001111', _ _ _ 1, 0, array[1,4,5,6,7], 2) returns 111111001111 and [4,5]. |   |
|   |   | set bit array record (varbit a, _ _ _ |   |   | function not only returns a bit string but also a subscript array. The subscript array indicates the positions of the bits |   |
|   | int b, int c, int[] d, int e) |   |   |   |   |   |
|   |   |   |   |   | whose values are ch |   |
|   | returns (varbit,int[]) |   |   |   |   |   |
|   |   |   |   |   |   | set bit array record('111100001111', _ _ _ |
|   |   |   |   |   | 1, 0, array[1,4,5,6,7], 2) |   |
|   | bit count array (varbit a, int _ _ |   |   |   | Counts the number of values b (0 or 1) among the bits that are specified by a subscript array c. |   |
|   |   | bit count array (varbit a, int _ _ |   |   | are specified by a subscr |   |
|   | b, int[] c) returns int |   |   |   | For example, | bit count array('1111000011110000', _ _ |
|   |   |   |   |   | 1, array[1,2,7,8]) |   |

|   | get bit array (varbit a, int b, _ _ | array indicates the posit that are not included in |
|---|---|---|
| int[] c) returns int[] |   |   |

|   |   | get bit array('111110000011', 1, _ _ |
|---|---|---|
|   | array[1,5,6,7,10,11]) |   |

**Usage**

**Create the varbitx extension**

```
CREATE EXTENSION varbitx;
```

**Delete the varbitx extension**

```
DROP EXTENSION varbitx;
```

**Call the functions**

You can execute the `SELECT <function>` statement to call the functions. Examples:

**bit_count function**

```
select bit_count('1111000011110000', 1, 5, 4);
```

Sample result:

```
 bit_count
----------- (1 row)
```

**set_bit_array_record function**

```
select set_bit_array_record('111100001111', 1, 0, array[1,4,5,6,7], 2);
```

Sample result:

```
  set_bit_array_record
------------------------
 (111111001111,"{4,5}")
(1 row)
```

### 12.23 pg_search (BM25 index)

This topic describes how to use the `pg_search` extension in PolarDB for PostgreSQL. `pg_search` is a full-text search extension based on the BM25 ranking algorithm. It provides high-performance, low-latency text search capabilities through a custom index access method. The extension supports keyword searches, phrase searches, fuzzy matching, and filtering with mixed conditions, and can be combined with numeric, boolean, and datetime fields for querying and sorting.

**Applicability**

This extension is available only for PolarDB for PostgreSQL 16 instances.

**Before you begin**

**Enable the pg_search extension**

On the **parameter settings** page of your PolarDB instance, add `pg_search` to the `shared_preload_libraries` parameter, and then click **Submit Parameters**.

**Important**

Modifying the `shared_preload_libraries` parameter automatically restarts the instance. To minimize service disruption, perform this operation during off-peak hours.

**Install the pg_search extension**

After connecting to the database, run the following SQL command to install the extension:

```
CREATE EXTENSION pg_search;
```

**Usage**

1. . Create a test table**

```
CREATE TABLE test(
    id int PRIMARY KEY,
    description text,
    rating int
```

);
2. . Create a BM25 index**
When you create a BM25 index, you must explicitly specify the following: Key column: This must be a unique identifier, such as a primary key, and must be the first column in the index. Include all columns used in search or filter operations to enable predicate pushdown and improve sorting performance. Index definition syntax:

```
CREATE INDEX index_name ON table_name USING bm25(key_col,col1,col2,...) WITH(
    key_field='key_col',
    text_fields='{...}',
    numeric_fields='{...}',
    boolean_fields='{...}',
    datetime_fields='{...}',
    json_fields='{...}'
```

); Field type descriptions:

| Type | Description |
|---|---|
| key field _ | The unique identifier column (required). |
| text fields _ | Text fields, such as text and varchar . These fields support tokenizers and columnar storage optimization. |
| numeric fields _ | Numeric fields, such as int and float . |
| boolean fields _ | Boolean fields. |
| datetime fields _ | Date and time fields. |

|   |   | numeric fields _ |
|---|---|---|

|   |   | boolean fields _ |
|---|---|---|

|   | datetime fields _ |
|---|---|

| json fields _ | json or jsonb fields. |
|---|---|

**Example: Create a composite BM25 index**

```json
CREATE INDEX test_search_idx ON test USING bm25(id,description,rating) WITH(
    key_field='id',
    text_fields='{
        "description": {
            "fast": true,
            "tokenizer": {"type": "default"}
```

`}`

```json
    }',
    numeric_fields='{
        "rating": {"fast": true}
```

`}'` ); `indexed` : Controls whether a column is indexed. The default value is `true` . `fast` : Enables columnar storage to accelerate filtering and sorting. The default value is `false` for text fields and `true` for numeric, boolean, and datetime fields. `tokenizer` : Specifies a tokenizer for a text field. To view available tokenizers, run

```
 SELECT * FROM pgsearch.tokenizers(); .
```

BM25 indexes support partial indexes ( `WHERE` clause) and expression indexes.
3. . Run search queries**
Use the `@@@` operator to perform a full-text search and the `pgsearch.score()` function to retrieve the BM25 relevance score. For queries with non-text filtering conditions, such as `rating>1` , add the corresponding columns to the BM25 index to enable predicate pushdown and significantly improve query performance.

**Basic keyword search**

```
SELECT id,pgsearch.score(id) FROM test WHERE description @@@ 'apple' AND rating>1 ORDER BY pgsearch.score(id) DESC LIMIT 5;
```

**Phrase search**

```
-- Exact phrase match SELECT id,pgsearch.score(id) FROM test WHERE description @@@ '"apple pay"' ORDER BY pgsearch.score(id) DESC LIMIT 5; -- Allow up to 2 words between terms (slop=2) SELECT id,pgsearch.score(id) FROM test WHERE description @@@ '"apple pay"~2' ORDER BY pgsearch.score(id) DESC LIMIT 5; -- Phrase prefix match SELECT id,pgsearch.score(id) FROM test WHERE description @@@ '"apple pay"*' ORDER BY pgsearch.score(id) DESC LIMIT 5;
```

anage logs

## 13 Manage logs

All PolarDB for PostgreSQL clusters support log management. You can use the primary/secondary switchover logs of a PolarDB for PostgreSQL cluster for troubleshooting. This topic describes how to manage the logs of a PolarDB for PostgreSQL cluster.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Logs**.
4. On the **Logs** page, you can query **Error Logs**, **Slow Query Logs**, or **Primary/Secondary**
**Switching Logs**. To do this, specify a time range and click **Search**.

| Log | Content |
|---|---|
| Error Logs | Record database errors that occurred within the most recent 30 days. |
| Slow Query Logs | Record SQL statements that took longer than one second to execute within the last 30 days. Duplicated SQL statements are removed. |
| Primary/Secondary Switching Logs | Record events of primary/secondary instance switchovers. |

oudDBA

## 14 CloudDBA

### 14.1 Overview of CloudDBA

CloudDBA is a cloud service for database self-detection, self-repair, self-optimization, selfmaintenance, and self-security based on machine learning and expertise. CloudDBA helps you ensure stable, secure, and efficient databases without worrying about the management complexity and service failures caused by manual operations.

**Features**

In PolarDB, CloudDBA leverages the core technical capabilities of Database Autonomy Service (DAS) to deeply integrate intelligent diagnosis and autonomous features into the PolarDB console. It provides a one‑stop database management experience and includes the following features: One‑click diagnosis: The One‑click diagnosis feature of PolarDB for PostgreSQL integrates selected capabilities of DAS, including session management, real‑time performance monitoring, lock analysis, and space analysis. This allows you to easily review diagnosis and optimization results. The details are as follows: Session management: You can view abnormal sessions, such as transactions that have not been committed for a long time, export or terminate sessions, and quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation. Real-time performance: You can view and monitor key metrics such as QPS, TPS, and network traffic for the target instance. Lock analysis: When database issues such as deadlocks, transaction blocking, or metadata lock waits occur, you can use the lock analysis feature provided by DAS to visually diagnose lock-wait relationships. This helps quickly identify the root cause of blocking and the dependency chain, which significantly improves troubleshooting efficiency and ensures the stability and high availability of database services. Storage analysis: You can view the storage usage, estimated days of remaining space, and detailed space usage of individual tables, including fragmentation and space anomaly diagnostics. Performance trends: This feature allows you to monitor key metrics such as CPU utilization, memory usage, IOPS, slow queries, and long-running transactions in real time and analyze historical data. This feature also allows you to compare metrics over multiple time periods and customize monitoring dashboard to improve performance and troubleshoot faults. Slow query log analysis: You can view slow query log trends and statistics. Diagnostic report: It helps you evaluate the operational status of database instances and identify performance bottlenecks and potential risks. You can manually trigger diagnostics. You can also configure scheduled tasks to automatically generate reports.

### 14.2 Perform quick diagnostics

#### 14.2.1 Manage sessions

oudDBA This topic describes how to use the session management feature of Database Autonomy Service (DAS) to monitor, analyze, and intervene in active sessions of database instances in real time. You can view abnormal sessions, such as transactions that have not been committed for a long period of time, export or terminate sessions, and quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**. Then, click the
**Session Management** tab.

**Instance sessions**

i. **View abnormal sessions** Click **Anomaly Detection**. In the pop-up dialog box, you can view abnormal sessions that the system identifies, including sessions that have not submitted transactions for a long period of time and sessions that occupy excessive resources. You can click **Optimize** or **End** to handle these sessions. ii. **View key metrics** Move the pointer over **Active session**, **Maximum Execution Duration**, **CPU**
**Utilization**, or **Connection Usage** to view the detailed information and trend in the pop-
up window.

**Session statistics**

**View session statistics**

You can view summarized session information by user, access source, or database, including the total number of sessions, the total number of ongoing sessions, and the longest session duration.

**Export session statistics**

You can export session statistics by summary, user, access source, or database.

#### 14.2.2 Use the real-time monitoring feature

Database Autonomy Service (DAS) provides real-time performance monitoring by collecting key operational metrics of database instances at a high frequency and presenting the data in visual charts and tables. This helps you identify instance load status, locate the root causes of performance jitter, and evaluate resource saturation.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**.
4. On the **Real-time Monitoring** tab, the system automatically loads real-time data. You can
view the real-time data on the **Real-time Charts** or **Real-time Tables** tab. For more information, see **View switching and advanced operations** . oudDBA

**Core metric interpretation**

Based on the console interface (this topic uses MySQL as an example; metrics for databases such as PostgreSQL may differ, so refer to the actual display in the console), real-time performance covers the following four monitoring dimensions. The following table below provides a detailed explanation of each metric along with O&M recommendations:

**BInstance basic instance information overview**

| Modu le | Metric | Description and O&M recommendations |
|---|---|---|
| Serve r Iinfor matio n | Version/Uptime | Displays the database kernel version (such as 8.0.36 ) and the cumulative uptime of the instance. Use this information to verify environment consistency and instance stability. |
| Conn ection Iinfor matio n | Maximum Cconnections/Cu rrent Cconnections/Act ive Cconnections | Format example: 1200 / - / 3 . Maximum Cconnections: Tthe maximum number of connections that the instance allows. Current Cconnections: Tthe total number of established TCP connections. Active Cconnections: Tthe number of connections that are currently executing SQL statements. Note If the number of current connections approaches the upper limit, watch for connection storms. If the number of active connections is much lower than the number of current connections, a large number of idle connections may be consuming resources. |
| Buffer Pool | Total Ppages/IdleFree pPage Percentageratio/ Dirty Ppage Percentageratio | Displays the InnoDB buffer pool status. Idle PFree page Percentageratio: Iindicates the remaining memory space. Dirty Ppage Percentageratio: Iindicates the volume of data pending flush to disk. A high percentageratio may reduce flush efficiency and cause I/O jitter. |

**Throughput, load, and deep engine metrics**

| Categ ory | Metric name | Description | O&M analysis and recommendations |
|---|---|---|---|
| Throu ghput | QPS \| TPS | QPS: The average number of SQL statements executed per second. TPS: The average number of transactions per second. | Trend analysis: A sudden increase typically corresponds to a business peak. Exception troubleshooting: If QPS or TPS drops while CPU usage rises, lock waits or slow SQL query blocking usually exists. |

oudDBA

| DML distrib ution | DML Eexecutio ns count | select: The number of SELECT statements executed per second. insert: The number of INSERT statements executed per second. update: The number of UPDATE statements executed per second. delete: The number of DELETE statements executed per second. | Business profiling: Identify whether the workload is read-heavy or write-heavy to help formulate an index optimization policy, such as adjusting the read/write splitting architecture. |
|---|---|---|---|
| Conne ction sessio ns | Connectio ns | Active Sessionsconnections: The number of open connections that are in an active statuse. Total Cconnections: The total number of open connections. | Bottleneck identification: Monitor the peaks of active connections. If the number of active sessionconnections remains high for an extended period, check for long-running transactions or unreleased application connections. |
| Cache efficie ncy | InnoDB CacheBuff er Pool | Cache Hhit Rratio: The ratioproportion of data read from memory. Cache Uusage: The occupancy ratio of the buffer pool. | Performance key: The hit ratio should be close to 100%. A low hit ratio means that a large number of requests fall through to the disk (physical reads), which causes a sharp performance drop. Consider increasing the buffer pool size or optimizing SQL queries. |
| Data access | InnoDB Raccessed rows | rows read: The number of _ InnoDB rows read per second. rows inserted: The number of _ InnoDB rows inserted per second. rows updated: The number of _ InnoDB rows updated per second. rows deleted: The number of _ InnoDB rows deleted per second. | Index optimization: If rows read is _ extremely high but the returned result set is small, a full table scan exists and you must add an appropriate index. |
| I/O reads and writes | Logical Rreads/ and pPhysical Rreads | Logical Rreads: The number of logical reads per second (read from the buffer pool). Physical Rreads: The number of physical reads per second (read from the disk). | I/O bottleneck: A surge in physical reads severely degrades performance and typically results from cold data access, an insufficient buffer pool, or missing indexes. |

oudDBA

| Lock conte ntion | Average Lrow lock Thold time for InnoDB Row-level Locking | The unit is typically milliseconds (ms), which reflects the average time to acquire a lock. | Concurrency conflicts: A higher value indicates more intense contention between transactions, which may cause timeout errors on the application side. |
|---|---|---|---|
| Lock waits | WInnoDB row lock waits for InnoDB Row-level Locking | Average Waits for InnoDB Rrow-level Llocking waits: The average number of row lock waits within the statistics period. Current Waits for InnoDB Rrow-level Llocking waits: The number of row lock waits at the current moment. | Blocking source: If this curve is not zero, blocking exists. Use the session management feature to locate the blocker and terminate the abnormal session. |
| Temp orary resour ces | Temporary Ttables and Ffiles | Temporary Ttables: The number of temporary tables created. Temporary Ffiles: The number of temporary files created. | SQL optimization: Frequent creation of on-disk temporary files severely degradesslows down SQL performancequeries. This typically occurs because sort buffer size is _ _ insufficient or a lack ofmissing indexes prevents index-based sorting. |
| Excep tion monit oring | Slow Qqueries | Slow Qqueries: The difference in the number of slow queries between two adjacent collection points, which represents the slow query increment within that time period. | Root cause correlation: A sudden increase in slow queries often directly causes CPU spikes and slow responses. Capture the slow query log immediately for analysis. |
| Netwo rk bandw idth | Network Ttraffic | Total Ttraffic, Iinbound Ttraffic, and Ooutbound Ttraffic. | Bandwidth limits: If outbound traffic reaches the instance bandwidth limit, connection timeouts or packet loss occur. If inbound traffic is abnormal, check for large field writes or potential attacks. |

**View switching and advanced operations**

**Comparison between real-time charts and real-time tables**

**Real-time charts**: Suitable for observing trends, peaks and valleys, and correlations
between multiple metrics (for example, whether CPU usage rises synchronously when QPS increases).
**Real-time tables**: Suitable for viewing exact metric values at a specific point in time,
which facilitates baseline data recording and detailed data comparison. Each row in the table represents a sampling point in time, and each column corresponds to the specific value of a metric. oudDBA
**Data download**: On the **Real-time Tables** tab, click the **Download** button in the
upper-right corner of the page to export the current report data to your local device. Some database engines (MongoDB and Redis) do not support the report download feature. The actual availability depends on what the console displays.

**Parameter description**

Click **Metric Description** in the upper-left corner of the page to view the specific definition of each metricmonitoring item, allowing you towhich helps you interpret data more accurately.

**Pause and resume**

The upper-right corner displays the remaining refresh count. You can manually control the automatic refresh frequency of the page, or click **Pause** to freeze the statuse at a specific moment for detailed analysis during troubleshooting.

**Usage recommendations**

Establish a baseline: During stable business periods, observe and record normal QPS, TPS, and CPU usage as a benchmark for subsequent fault comparison. Perform correlation analysis: Avoid viewing a single metric in isolation. For example, when QPS drops, immediately check whether InnoDB row lock waits increase or slow queries increase, and observe forwhether physical reads show abnormal fluctuations in physical reads. Watch for spikes: Sudden spikes in charts typically correspond to specific business events (such as scheduled jobs starts or flash sales). Cross-referencing the timestampCorrelating the point in time with business logs helps you quickly locate the issue.

#### 14.2.3 Lock analysis

When database issues, such as deadlocks, occur, you can use the lock analysis feature provided by Database Autonomy Service (DAS) for quick diagnosis. DAS can analyze the latest deadlock logs and visually diagnose lock-wait relationships. This helps quickly identify the root cause of blocking and the dependency chain, which significantly improves troubleshooting efficiency and ensures the stability and high availability of database services.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**. Then, click **Diagnose**
on the **Lock Analysis** tab. If multiple deadlocks have occurred, DAS analyzes only **the most recent deadlock** and retains the deadlock data.
4. After the diagnostic task is complete, select a time range and click **View Details** in the
**Details** column of the diagnostic task list under recent deadlock analysis to view the
results of deadlock diagnostic tasks that were triggered during the time range. oudDBA

#### 14.2.4 View storage overview

Database Autonomy Service (DAS) provides the storage analysis feature that allows you to view the overall storage usage and estimated days of remaining available storage for a database instance. You can also check the storage usage, space fragmentation, and space anomaly diagnostics for a tablespace in the database.

**Prerequisites**

The database instance that you want to manage is connected to Database Autonomy Service (DAS). If the instance is not connected, an authorization pop-up appears on this page. Click Authorize.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**. Then, click the
**Storage Analysis** tab.
PolarDB for PostgreSQL supports displaying tablespace information at the schema level. This allows you to distinguish between tablespaces with the same name across different schemas. It makes it easier to locate the storage usage of a business module. On the **Storage Analysis** tab, click the **Storage Overview** tab. You can view data such as the storage overview, exception list, storage trend, and tablespaces. On the **Storage Analysis** tab, click the **Data Space** tab. You can view the storage usage of each database and tablespace. Click the name of a tablespace to view the fields and indexes of the tablespace.

### 14.3 Performance Trend

This topic describes how to use CloudDBA to view the performance trend of a PolarDB for PostgreSQL instance. You can monitor key metrics in real time and analyze historical data. These metrics include CPU, memory, IOPS, slow queries, and long-running transactions. The feature also supports performance trend comparison and custom monitoring dashboards to help you efficiently tune performance and troubleshoot failures.

**Features**

The Performance Trend feature displays the following metrics:

| Metric classification | Metrics |
|---|---|
| Host metrics | CPU utilization, memory utilization, and data disk IOPS. |

oudDBA

| PostgreSQL infrastructure monitoring | Latency, two-phase commit (2PC), long-running transactions, slow queries, transactions per second, rows processed, and connections. |
|---|---|

**View performance trends**

1. Log on to the PolarDB console.
2. On the **Instances** page, click the ID of the target instance to go to the instance details
page.
3. In the navigation pane on the left, click **CloudDBA > Performance Trend**.
On the **Performance Trend** tab, view the performance trend of each metric within the selected time range. Click **More Metrics** to select the metrics whose performance trends you want to view. In a metric trend chart, click **Details** to enlarge the chart. You can also change the time range to view the change trends of the metric over different periods. On the **Performance Trend Comparison** tab, set two time ranges and click **View** to see a chart that compares the performance trends. On the **Custom Chart** tab, create custom monitoring dashboards as needed. You can display multiple required performance monitoring metrics in a single chart for easier troubleshooting and analysis. If this is your first time, first click **Add Monitoring Dashboard**.

### 14.4 Slow query logs

In PolarDB, CloudDBA provides the slow query log analysis feature that allows you to view the trends and execution details of slow queries and obtain optimization suggestions for your PolarDB instances.

**Go to the Slow Query Logs page**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Slow Query Logs**.
For more information, see the **Slow query logs** topic in **Database Autonomy**
**Service (DAS) > User Guide.** .

### 14.5 Diagnostic reports

oudDBA Database Autonomy Service (DAS) provides the diagnostic report feature to help you assess the status of database instances and identify performance bottlenecks and potential risks. You can manually trigger a diagnostic or configure a scheduled task to automatically generate a report. Currently, this feature can only assess the status of database instances and display the identified issues. It does not provide any optimization suggestions. You need to troubleshoot the issues based on the generated report.

**Suggestions**

Periodically generate diagnostic reports: We recommend that you configure the system to automatically generate daily diagnostic reports for production instances and formulate performance baselines. Use slow SQL query optimization: Pay close attention to the top 10 slow SQL queries and high-risk SQL queries, and optimize them promptly. Focus on changes in health scores: If the health score consistently drops, check resource configurations or look for performance bottlenecks caused by business growth.

**Procedure**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose Primary/Secondary Edition > Instances. On the **List**
**of local disk instances** page, find the instance that you want to manage and click its ID or
click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostic Reports**.

**Manually initiate a diagnostic**

Click **Create Reports**. In the dialog box that appears, select a time range (Last 1 Hour, Last 3 Hours, Last 6 Hours, Last 12 Hours, or Last 24 Hours) and click **Confirmation**. The system immediately starts the diagnostic task.

**Automatically generate diagnostic reports at a scheduled**

**time**

Click **Auto-generating Report Settings**, select **Scheduled Trigger**, select days and a specific time, and then click **OK**. Due to system scheduling and resource usage, diagnostic reports may be generated with a delay. The actual time prevails.

**View diagnostic report details**

The list on the page shows all available diagnostic reports. Click **View Report** in the Actions column of a diagnostic report to go to the details page. The report displays the following information: instance health status, active sessions, top 10 slow SQL queries, high-risk SQL queries, top 5 tablespaces, redundant indexes, lock analysis, and performance trends. In the upper-right corner of the diagnostic report page, click **Deduction Details** to view the health score deduction details.

**Download a diagnostic report**

Click **View Report** to go to the diagnostic report details page. Then, click **Download** to download the report to your on-premises machine for archiving or sharing. capabilities

## 15 AI capabilities

### 15.1 Intelligent migration

#### 15.1.1 Intelligent migration guide

Intelligent One-Click Migration of PolarDB is a one-stop database migration platform built on DTS capabilities. It provides an end-to-end visual guided workflow that covers scenario selection, prechecks, task configuration, and endpoint switching. Through automated configuration and seamless switchover, it enables transparent application migration with zero downtime. In addition, the integrated AI Migration Assistant supports intelligent Q&A, log diagnostics, and optimization recommendations, significantly improving both migration efficiency and success rates.

**Overview**

PolarDB Intelligent One-Click Migration is an end-to-end, user-friendly, and intelligent database migration solution designed for enterprises. This feature integrates operations previously scattered across multiple consoles into a unified PolarDB console, enabling you to complete the entire process from instance preparation to service cutover without switching between consoles.

**Core features**

| Category | Feature description |
|---|---|
| End-to end visualization | Four-step guided workflow with clear status visibility and closed-loop operation management. |
| Automated configuration | Automatically matches Data Transmission Service (DTS) links and creates migration tasks based on migration scenarios, minimizing manual intervention. |
| Transparent application switchover | Supports one-click switching of database endpoints without service interruption. |
| AI-powered assistance | Features a built-in AI Migration Assistant that provides real-time Q&A, log analysis, and fixing suggestions. |

**Supported migration scenarios**

The following migration paths are supported. The system automatically loads the corresponding operation plans and check items based on the selected scenario to ensure compliant and efficient migration.

| Migration path classification | Supported migration path |
|---|---|

capabilities

| MySQL engine migration | From ApsaraDB RDS for MySQL to PolarDB for MySQL Primary/Secondary Edition From ApsaraDB RDS for MySQL to PolarDB for MySQL Cluster Edition From PolarDB for MySQL Primary/Secondary Edition 5.7 to PolarDB for MySQL Primary/Secondary Edition 8.0 From PolarDB for MySQL Primary/Secondary Edition to PolarDB for MySQL Cluster Edition From PolarDB for MySQL Cluster Edition to PolarDB for MySQL Cluster Edition |
|---|---|
| PostgreSQL engine migration | From ApsaraDB RDS for PostgreSQL to PolarDB for PostgreSQL Primary/Secondary Edition From PolarDB for PostgreSQL Primary/Secondary Edition to PolarDB for PostgreSQL Primary/Secondary Edition |
| PolarDB-X engine migration | From ApsaraDB RDS for MySQL to PolarDB-X 2.0 From PolarDB-X 2.0 to PolarDB-X 2.0 |

**Process**

Intelligent one-click migration adopts a linear four-step guided workflow, which allows you to complete all migration operations on a single page.

**Step 1: Select a migration scenario**

1. Log in to the PolarDB console.
2. In the left-side navigation pane, choose **AI Capabilities > Intelligent Migration**. On the
page that appears, select the type of the source database and the type of the destination PolarDB instance.

**Benefits**

The system automatically identifies migration requirements and pre-populates the parameters required for subsequent steps. The system recommends optimal DTS links and synchronization policies. This significantly reduces configuration overhead and prevents manual selection errors.

**Step 2: Perform a precheck**

Click **Check it out**. You are redirected to the official migration guide based on your selected scenario. There, you will find detailed step-by-step instructions and a pre-migration checklist, covering items such as whether Binlog is enabled and properly formatted on the source database, and whether security groups and whitelists are correctly configured to allow communication.

**Benefits**

Check items are tightly coupled with specific scenarios to prevent omissions. Quick access to official documentation significantly accelerates troubleshooting.

**Step 3: Create a DTS data migration task**

capabilities After you confirm that the precheck is complete, click **To migrate**. The DTS migration task configuration page appears. You need to only specify key information as specified in Step 2 to build a migration path.

**Benefits**

You do not need to go to the DTS console. All task statuses are displayed on this page. Configuration time is significantly reduced, accelerating task startup. Real-time alerts for task exceptions facilitate timely intervention.

**Step 4: View the migration results and change the database**

**endpoints**

When the incremental synchronization latency approaches zero and no errors are reported, you can proceed to change the endpoint configured in your application. We recommend that the endpoint switching be performed during off-peak hours and the reconnection mechanism of your application be verified in advance.
1. On the **Database migration results** tab, confirm that the migration status is normal and
then click **Migrate Endpoint** in the Operation column. In the result list, you can view the details of the task, such as the creation time, running status, the number of rows in the source when the task starts, and the number of rows in the destination when the task ends. Once the task starts, if the source data changes, data inconsistency occurs between the source and destination after the task is complete.
2. On the tab that appears, confirm the information about the source and destination
databases and click **Switch Endpoint**.

**Benefits**

Seamless application migration is implemented with zero downtime. The switchover process can be traced and rolled back with high security.

#### 15.1.2 AI Migration Assistant

AI Migration Assistant is an intelligent tool that supports the one-click migration platform. It uses the Data Transmission Service (DTS) Model Context Protocol (MCP) to provide natural language Q&A, task status queries, and diagnostic capabilities. This helps you resolve issues related to migration path queries, configuration guidance, and error handling during the migration process.

**Features**

AI Migration Assistant is integrated into the Intelligent Migration page of the PolarDB console. It understands your questions and automatically retrieves data and logs from the DTS backend to provide accurate migration support. You can obtain real-time, actionable solutions without leaving the page. Key features include the following: Intent recognition: Supports natural language input in Chinese and accurately parses the intent of your questions. capabilities Migration path query: Query supported DTS migration paths and connection methods, such as cloud instances and public IP addresses, in the current region. Configuration guidance: View the supported object types, such as tables and indexes, and the scope of supported Data Definition Language (DDL) operations for a specific migration path. Status monitoring: Obtain real-time updates on task status, latency, traffic, and synchronization progress. Diagnostics: Analyze task logs to identify the cause of errors and receive recommended solutions.

**Example scenarios**

**Scenario 1: Querying for supported migration paths**

User question: Does the current environment support migration from RDS for PostgreSQL to PolarDB for PostgreSQL? What are the supported data source connection methods, such as cloud instances and public IP addresses? AI response: DTS MCP automatically identifies the current region, product edition, and network environment. It then provides a real-time list of all available DTS migration paths in the region. The response clearly indicates the source and destination database types, supported connection modes (VPC, cloud instance, or public IP address), and any limitations. This improves information retrieval efficiency and reduces tickets related to unclear migration paths by approximately 20%.

**Scenario 2: Querying for migration task configuration**

User question: For a migration path from an RDS for PostgreSQL cloud instance to PolarDB for PostgreSQL, what object types and synchronization operations are supported? AI response: Based on the source and destination information, DTS MCP automatically retrieves and provides the supported migration objects for the path, such as tables, views, functions, and stored procedures. It also lists the supported scope for DDL and Data Manipulation Language (DML) synchronization and any operational restrictions. The response provides configuration guidance for stages such as initial schema synchronization, full migration, and incremental synchronization. This reduces task configuration complexity by up to 20%.

**Scenario 3: Troubleshooting task errors**

User question: Is DTS migration task `l65e721` running correctly? If there are errors, how do I resolve them? AI response: DTS MCP automatically pulls the task's real-time status, latency trends, synchronization progress, throughput, and error logs to accurately assess its health. If an error or potential threat is detected, the AI assistant generates a diagnostic report and recommends a solution. This approach reduces the response time for failures and the need for manual intervention, which decreases tickets and alerts by 30%.

#### 15.1.3 Migrate data from a PolarDB for PostgreSQL 14 cluster to a PolarDB for PostgreSQL 16 cluster through visualized operations

**PostgreSQL 14 cluster to a PolarDB for**

**PostgreSQL 16 cluster through visualized**

**operations**

capabilities This topic describes how to migrate data from a PolarDB for PostgreSQL 14 cluster to a PolarDB for PostgreSQL 16 cluster through visualized operations. The quick migration feature depends on ApsaraDB RDS, PolarDB for PostgreSQL, Data Transmission Service (DTS), and OneConsole. You must upgrade the preceding component versions to the destination versions or later.
1. . Overview**
PolarDB allows you to migrate data from a PolarDB for PostgreSQL 14 cluster to a PolarDB for PostgreSQL 16 cluster. This feature is often used for major engine version upgrades of PolarDB for PostgreSQL. Solution overview: After you create a PolarDB for PostgreSQL 16 cluster, you can use DTS to migrate data to the PolarDB for PostgreSQL 16 cluster. You need only to change the service address after the migration.

**Usage notes**

The migration operation requires your permission. After the migration, the endpoint for connecting to the instance is changed. We recommend that you perform the migration during off-peak hours.

**Benefits**

Supports migration with endpoint unchanged: The endpoint of the source database is retained. This way, you can perform the migration without the need to change endpoints on your applications. Supports migration rollback: After the migration, you can roll back to the source instance if any compatibility issues are detected. Supports visible migration progress at any time: You can view the current migration progress at any time. This helps you to develop a switchover plan. Supports incremental data migration, with the service downtime of less than 10 minutes: DTS is used to implement online hot migration. You do not need to shut down your source instance during the migration. A transient disconnection occurs only when you switch from the PolarDB for PostgreSQL 14 cluster to the PolarDB for PostgreSQL 16 cluster. Therefore, you must schedule and apply for a 10-minute service downtime window.

**Limitations**

Cross-region migration not supported: You can migrate data only between instances in the same region. Major engine versions of PostgreSQL are not fully compatible with each other. If you migrate data across major engine versions of PostgreSQL, you must evaluate the syntax compatibility. Limits on endpoint changes: Only the Domain Name System (DNS) record is modified when the endpoint to the instance is changed. The following limits apply: Only the connection address is switched from the endpoint of the source PolarDB for PostgreSQL cluster to the endpoint of the destination PolarDB for PostgreSQL cluster. Other configurations, such as the vSwitches and virtual IP addresses (VIPs), remain unchanged. The port number also remains unchanged. capabilities Possible DNS caching failures: After the endpoint is changed, issues may arise due to the expiration of the DNS cache. You may fail to connect to the PolarDB for PostgreSQL cluster, or only read operations are supported. To resolve this issue, we recommend that you refresh the DNS cache of your server to speed up the cache update. Other limits and usage notes: For more information, see the usage notes and limits for source and destination databases that are described in the "Migrate data between PolarDB for PostgreSQL clusters" topic of the DTS documentation.
2. . Create a PolarDB for PostgreSQL cluster**
You need to create a PolarDB for PostgreSQL 16 cluster before you perform the migration. To avoid syntax errors or data chaos, we recommend that you perform tests and drills to evaluate the SQL syntax compatibility before you migrate data.

**Usage notes**

Instance type: We recommend that you use the same instance type as the PolarDB for PostgreSQL 14 cluster. Virtual private cloud (VPC): We recommend that you deploy the PolarDB for PostgreSQL 16 cluster in the same VPC as the PolarDB for PostgreSQL 14 cluster. If you use a different VPC, make sure that the VPC is accessible to applications before you start the migration. Network whitelist: After you create a PolarDB for PostgreSQL 16 cluster, you need to configure an IP address whitelist that is the same as the IP address whitelist of the PolarDB for PostgreSQL 14 cluster. This ensures that applications can access the PolarDB for PostgreSQL 16 cluster after you switch to the destination cluster. The instance ID changes after the migration. If you are in one of the following scenarios, we recommend that you communicate with the relevant teams in advance to ensure that all involved systems are switched after the migration. Otherwise, you may encounter issues when you use these application systems. Switchover with endpoints does not require modifications to the endpoint and port number of the destination database, and the existing endpoint is unaffected. However, if you want to change the configurations, you need to change relevant parameters in the following systems: Database services: DTS and Data Management (DMS) that are accessed over cloud instances. Big data services: DataWorks and DataHub that are accessed over cloud instances. CloudMonitor: CloudMonitor monitors the destination instance after the migration.
3. . Precheck for migration**

**Check the kernel parameter configurations of the PolarDB for**

**PostgreSQL 14 cluster**

The PolarDB for PostgreSQL 14 cluster cannot be empty. In other words, the data volume of the database cannot be 0. The value of the `wal_level` kernel parameter must be logical. The value of the `max_replication_slots` parameter must be greater than the total number of two-way DTS connections required, as indicated by the number of databases involved. The value of the `max_wal_senders` parameter must be greater than the total number of two-way DTS connections required, as indicated by the number of databases involved.

**Check the syntax compatibility**

PolarDB for PostgreSQL is fully compatible with PostgreSQL syntax, excluding extensions. capabilities You need to pay attention to the following changes when you upgrade the engine version from PostgreSQL 14 to PostgreSQL 16. Feature enhancements: For example, parallel query is optimized, partition tables are improved, and JSONB performance is improved. Compatibility changes: specific deprecated parameters (such as the adjustment to the

| fsync |   | paramet |
|---|---|---|
| of the |   |   |

default value of the `fsync` parameter), and extensibility and compatibility (such as the Data types for migration: You must ensure that the custom data types are compatible with the new version, accounting for potential handling differences in types such as `JSONB` .

**(Optional) Best practice for checking syntax compatibility by using pg_upgrade**

pg_upgrade: a tool provided by Alibaba Cloud for in-place upgrades across versions. This tool does not require you to perform import or export operations. `pg_upgrade` supports upgrades from PostgreSQL 8.4.X to the latest version, including snapshots and test versions. pg_upgrade also supports pre-upgrade compatibility checks, which detect incompatibility issues related to extensions and data types. Procedure:
1. The following example shows how to deploy a PolarDB for PostgreSQL 14 cluster, a PolarDB
for PostgreSQL 16 cluster, and CentOS 7 on an Elastic Compute Service (ECS) instance. i. Run the following code to deploy PostgreSQL 14.13:

```python
rpm -ivh postgresql14-libs-14.13-.rhel7.x86_64.rpm rpm -ivh postgresql14-14.13-.rhel7.x86_64.rpm rpm -ivh postgresql14-server-14.13-*.rhel7.x86_64.rpm sudo /usr/pgsql-14/bin/postgresql-14-setup initdb sudo systemctl enable postgresql-14 sudo systemctl start postgresql-14
```

ii. Run the following code to deploy PostgreSQL 16.0:

```python
rpm -ivh postgresql16-libs-16.0-.rhel7.x86_64.rpm rpm -ivh postgresql16-16.0-.rhel7.x86_64.rpm rpm -ivh postgresql16-server-16.0-*.rhel7.x86_64.rpm sudo /usr/pgsql-16/bin/postgresql-16-setup initdb sudo systemctl enable postgresql-16 sudo systemctl start postgresql-16
```

2. Import the data to a PostgreSQL 14 database.
i. Run the pg_dump command to export all schemas and data of the source database. a. Obtain the password of the aurora user.

```
b. pg_dump -h <host> -p 5432 -U aurora -F c -f pg14.dump <database>
```

ii. Run the pg_restore command to import data to PostgreSQL 14.x.

```
a. pg_restore -h <host> -p 5432 -U postgres -d <database> -F c pg14.dump
```

3. Call the pg_upgrade tool to verify the compatibility.
capabilities i. Run the following commands on the ECS instance:

```python
# Disable the service.
sudo systemctl stop postgresql-14 sudo systemctl stop postgresql-16
# Perform a compatibility check.
# Use pg_upgrade to verify version compatibility.
su - postgres /usr/pgsql-16/bin/pg_upgrade --old-bindir=/usr/pgsql-14/bin --newbindir=/usr/pgsql-16/bin --old-datadir=/var/lib/pgsql/14/data --newdatadir=/var/lib/pgsql/16/data --check
```

The following results show that the check items pass the compatibility checks:

```
Performing Consistency Checks ----------------------------- Checking cluster versions ok Checking database user is the install user ok Checking database connection settings ok Checking for prepared transactions ok Checking for system-defined composite types in user tables ok Checking for reg* data types in user tables ok Checking for contrib/isn with bigint-passing mismatch ok Checking for user-defined encoding conversions ok Checking for user-defined postfix operators ok Checking for incompatible polymorphic functions ok Checking for presence of required libraries ok Checking database user is the install user ok Checking for prepared transactions ok Checking for new cluster tablespace directories ok *Clusters are compatible*
```

**Check the extension compatibility**

Run the following command to check the extension version on PolarDB for PostgreSQL 14 and PolarDB for PostgreSQL 16, respectively:

```
SELECT * FROM pg_available_extensions;
```

You need to create an extension on the corresponding database before you perform the migration.

**Migrate account permissions on the PolarDB for PostgreSQL 14**

**cluster**

The account permissions on the PolarDB for PostgreSQL 16 cluster are the same as those on the PolarDB for PostgreSQL 14 cluster. You need to only export and import the account permissions.
1. Export user permissions from the source database:
i. Use a privileged account, which is assumed to be `juhuan` in this example. capabilities

| pg dumpall -h <host> -p 5432 -U juhuan --roles-only --no-role-passwords > _ |   |
|---|---|

iii. The following SQL statements are exported: `--`

```
-- PostgreSQL database cluster dump
```

`--`

```
SET default_transaction_read_only = off; SET client_encoding = 'UTF8'; SET standard_conforming_strings = on;
```

`--`

```
-- Roles
```

`--`

```
CREATE ROLE aurora; ALTER ROLE aurora WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NO BYPASSRLS; CREATE ROLE juhuan; ALTER ROLE juhuan WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NO BYPASSRLS; COMMENT ON ROLE juhuan IS 'polar_superuser'; CREATE ROLE polar_gawr_admin; ALTER ROLE polar_gawr_admin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NO REPLICATION NOBYPASSRLS; CREATE ROLE polar_gawr_user; ALTER ROLE polar_gawr_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NOR EPLICATION NOBYPASSRLS; CREATE ROLE polardb_admin; ALTER ROLE polardb_admin WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION B YPASSRLS; CREATE ROLE replicator; ALTER ROLE replicator WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; CREATE ROLE rs_user; ALTER ROLE rs_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS;
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "DateStyle" TO 'ISO,YMD';
```

capabilities `--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET extra_float_digits TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET lock_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET statement_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET extra_float_digits TO '0';
```

`--` capabilities

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET lock_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET statement_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "rs_user"
```

`--`

```
ALTER ROLE rs_user SET default_transaction_read_only TO 'on';
```

`--`

```
-- Role memberships
```

`--`

```
GRANT pg_polar_superuser TO juhuan GRANTED BY aurora;
```

`--`

```
-- PostgreSQL database cluster dump complete
```

`--`
2. Run the following command to import user permissions to the destination PolarDB for
PostgreSQL database: capabilities

```
 psql -h <host> -p 5432 -U aurora -f pg_roles.sql
```

2. Run the following statements to verify the permissions:

```
SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = 'app_user' AND table_name = '<TABLE_NAME>' AND table_schema = 'public';
```

4. . Use DTS to migrate data**

**Procedure**

Data migration applies to database migration scenarios.
1. Log on to the PolarDB console. In the left-side navigation pane, choose **AI Capabilities >**
**Intelligent Migration**.
2. On the Intelligent Migration page, click **PolarDB-PG Primary-Secondary Edition to**
**PolarDB-PG Primary-Secondary Edition**.
3. Click **To Migrate** and configure the parameters. The following table describes the
parameters.
4. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| None | Task Name | Enter the name of the task. DTS automatically generates a task name. We recommend that you specify an informative name to identify the task. You do not need to specify a unique task name. |
|   | Instance Region | Select the region in which the source instance resides. The region is the source region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specify whether to migrate data between instances that belong to different Alibaba Cloud accounts. Select No. |
|   | Architecture | Select Primary/Standby Edition. |

capabilities

|   | PolarDB Cluster ID | Select the ID of the source PolarDB for PostgreSQL cluster. |
|---|---|---|
|   | Database Name | Enter the name of the database in the source PolarDB for PostgreSQL cluster. |
|   | Database Account | Enter the privileged account of the source PolarDB for PostgreSQL cluster. The account must have the owner permission on the database to which the data to be migrated belongs. |
|   | Database Password | Enter the password that is used to access the database. |
|   | Encryption | Configure this parameter based on your business requirements. |
|   | Instance Region | Select the region in which the destination database resides. The region is specified when you create the data migration task. You cannot change the value of this parameter. |
|   | Architecture | Select Primary/Standby Edition. |
|   | PolarDB Cluster ID | Enter the ID of the destination PolarDB for PostgreSQL cluster. |
|   | Database Account | Enter the name of the database used to receive data in the destination PolarDB for PostgreSQL instance. |
|   | Database Account | Enter the database account of the destination PolarDB for PostgreSQL cluster. The account must have the owner permissions on schemas. |
|   | Database Password | Enter the password that is used to access the database. |
|   | Encryption | Configure this parameter based on your business requirements. |

5. In the lower part of the page, click **Test Connectivity and Proceed**.
6. If an IP address whitelist is configured for your PolarDB for PostgreSQL cluster, you must
add the CIDR blocks of DTS servers to the whitelist. Then, click **Test Connectivity and**
**Proceed**.
capabilities If no whitelist is configured for your PolarDB for PostgreSQL cluster, ignore the whitelist settings and click **Test Connectivity and Proceed**.
7. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables with identical names, the precheck is passed. Otherwise, the precheck fails, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database. If the source and destination databases have different schemas, only specific columns may be migrated, or the data migration task may fail. |

capabilities

| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that of the source or destination database. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select schemas or tables as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that reference the object may fail to be migrated. |

8. Click **Next: Advanced Settings** to configure advanced settings. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the connection to the source or destination database fails after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you specify different retry time ranges for multiple data migration tasks that share the same source or destination database, the shortest retry time range takes precedence. |

capabilities
9. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data migration task, a precheck is performed. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.
0. Wait until **Success Rate** reaches 100% and then click **Back**.
If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

**Data synchronization procedure**

Data synchronization applies to table transmission and migration to the cloud.
1. Log on to the PolarDB console. In the left-side navigation pane, choose **AI Capabilities >**
**Intelligent Migration**.
2. On the Intelligent Migration page, click **PolarDB-PG Primary-Secondary Edition to**
**PolarDB-PG Primary-Secondary Edition**.
3. Click **De-synchronization** and configure the parameters. The following table describes the
parameters.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| None | Task Name | Enter the name of the task. DTS automatically generates a task name. We recommend that you specify an informative name to identify the task. You do not need to specify a unique task name. |
|   | Instance Region | Select the region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specify whether to migrate data between instances that belong to different Alibaba Cloud accounts. Select No. |

capabilities

|   | Architectur e | Select Primary/Standby Edition. |
|---|---|---|
|   | PolarDB Cluster ID | Select the ID of the source PolarDB for PostgreSQL cluster. |
|   | Database Account | Enter the name of the database in the source PolarDB for PostgreSQL cluster. |
|   | Database Account | Enter the privileged account of the source PolarDB for PostgreSQL cluster. The account must have the owner permission on the database to which the data to be synchronized belongs. |
|   | Database Password | Enter the password that is used to access the database. |
|   | Encryption | Configure this parameter based on your business requirements. |
|   | Instance Region | Select the region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization task. You cannot change the value of this parameter. |
|   | Architectur e | Select Primary/Standby Edition. |
|   | PolarDB Cluster ID | Enter the ID of the destination PolarDB for PostgreSQL cluster. |
|   | Database Account | Enter the name of the database used to receive data in the destination PolarDB for PostgreSQL instance. |
|   | Database Account | Enter the database account of the destination PolarDB for PostgreSQL cluster. The account must have the owner permissions on schemas. |
|   | Database Password | Enter the password that is used to access the database. |
|   | Encryption | Configure this parameter based on your business requirements. |

5. In the lower part of the page, click **Test Connectivity and Proceed**.
6. If an IP address whitelist is configured for your PolarDB for PostgreSQL cluster, you must
add the CIDR blocks of DTS servers to the whitelist. Then, click **Test Connectivity and**
**Proceed**.
capabilities If no whitelist is configured for your PolarDB for PostgreSQL cluster, ignore the whitelist settings and click **Test Connectivity and Proceed**.
7. Select the objects to be synchronized and the synchronization types. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore, data inconsistency may occur between the source and destination databases. This may cause business loss. If the source and destination databases use the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that of the source or destination database. |

capabilities

| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can select schemas or tables as the objects to be synchronized. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. Note To select SQL operations for the synchronization task, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE clauses to filter data, right-click a table in the Selected Objects section. In the dialog box that appears, specify the filter conditions. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

8. Click **Next: Advanced Settings** to configure advanced settings. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the connection to the source or destination database fails after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you specify different retry time ranges for multiple data migration tasks that share the same source or destination database, the shortest retry time range takes precedence. |

9. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. capabilities If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.
0. Wait until **Success Rate** displays 100% and then click **Back**.

##### 15.1.3.1 Prechecks

###### 15.1.3.1.1 Syntax compatibility check

This topic describes how to perform a syntax compatibility check.

**Overview**

PolarDB for PostgreSQL is fully compatible with PostgreSQL syntax, excluding plug-ins. You must focus on the following changes when upgrading PostgreSQL 14 to 16: Feature enhanced: For example, parallel query is optimized, partition tables are improved, and JSONB performance is improved. Compatibility changed: Specific parameters are deprecated. For example, the default value of the `fsync` parameter is changed. Compatibility for specific parameters is enhanced. For example, the dependencies of `pg_trgm` are updated. Data types migrated: You must ensure that custom data types are compatible with the new version. For example, the processing logic of the `JSONB` data type changes after the upgrade.

**Best practice for checking syntax compatibility by using**

**pg_upgrade**

pg_upgrade: a tool provided by Alibaba Cloud for in-place updates across versions. This tool does not require you to perform any import or export operation. `pg_upgrade` supports upgrades from PostgreSQL 8.4.X to the latest version, including snapshots and test versions. pg_upgrade also supports pre-upgrade compatibility check, which detects incompatibility issues related to plug-ins and data types. Procedure
1. Deploy the PostgreSQL versions before and after the upgrade on an Elastic Compute
Service (ECS) instance that runs CentOS 7. In this example, PostgreSQL 14 and 16 are used. i. Run the following code to deploy PostgreSQL 14.13:

```python
rpm -ivh postgresql14-libs-14.13-.rhel7.x86_64.rpm rpm -ivh postgresql14-14.13-.rhel7.x86_64.rpm rpm -ivh postgresql14-server-14.13-*.rhel7.x86_64.rpm sudo /usr/pgsql-14/bin/postgresql-14-setup initdb sudo systemctl enable postgresql-14 sudo systemctl start postgresql-14
```

capabilities ii. Run the following code to deploy PostgreSQL 16.0:

```python
rpm -ivh postgresql16-libs-16.0-.rhel7.x86_64.rpm rpm -ivh postgresql16-16.0-.rhel7.x86_64.rpm rpm -ivh postgresql16-server-16.0-*.rhel7.x86_64.rpm sudo /usr/pgsql-16/bin/postgresql-16-setup initdb sudo systemctl enable postgresql-16 sudo systemctl start postgresql-16
```

2. Import the data in the original database to Postgres 14.
i. Run the pg_dump command to export all structures and data from the original database. a. Obtain the password of the aurora user.

```
b. pg_dump -h <host> -p 5432 -U aurora -F c -f pg14.dump <database>
```

ii. Run the pg_restore command to import data to Postgres 14.

```
a. pg_restore -h <host> -p 5432 -U postgres -d <database> -F c pg14.dump
```

3. Call the pg_upgrade tool to verify the compatibility.
i. Run the following commands on the ECS instance:

```python
# Disable the service.
sudo systemctl stop postgresql-14 sudo systemctl stop postgresql-16
# Perform compatibility check.
# Use pg_upgrade to verify version compatibility.
su - postgres /usr/pgsql-16/bin/pg_upgrade --old-bindir=/usr/pgsql-14/bin --newbindir=/usr/pgsql-16/bin --old-datadir=/var/lib/pgsql/14/data --newdatadir=/var/lib/pgsql/16/data --check
```

The following results show that all check items passed the compatibility checks:

```
Performing Consistency Checks ----------------------------- Checking cluster versions ok Checking database user is the install user ok Checking database connection settings ok Checking for prepared transactions ok Checking for system-defined composite types in user tables ok Checking for reg* data types in user tables ok Checking for contrib/isn with bigint-passing mismatch ok Checking for user-defined encoding conversions ok Checking for user-defined postfix operators ok Checking for incompatible polymorphic functions ok Checking for presence of required libraries ok Checking database user is the install user ok Checking for prepared transactions ok Checking for new cluster tablespace directories ok *Clusters are compatible*
```

###### 15.1.3.1.2 Plug-in compatibility check

capabilities This topic describes how to perform a plug-in compatibility check. Run the following command on PostgreSQL 14 and 16 respectively to check the available extensions:

```
SELECT * FROM pg_available_extensions;
```

Before migration, you need to manually create the plug-ins in the respective database.

###### 15.1.3.1.3 Account migration

This topic describes how to migrate an account. The account permissions on a PolarDB for PostgreSQL 16 cluster are the same as those on a PolarDB for PostgreSQL 14 cluster. You only need to export and import the account permissions.
1. Export user permissions from the source database as follows:
i. Use a privileged account, which is assumed to be `juhuan` in this example.

| pg dumpall -h <host> -p 5432 -U juhuan --roles-only --no-role-passwords > _ |   |
|---|---|

iii. The following SQL statements are exported: `--`

```
-- PostgreSQL database cluster dump
```

`--`

```
SET default_transaction_read_only = off; SET client_encoding = 'UTF8'; SET standard_conforming_strings = on;
```

`--`

```
-- Roles
```

`--`

```
CREATE ROLE aurora; ALTER ROLE aurora WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NO BYPASSRLS; CREATE ROLE juhuan; ALTER ROLE juhuan WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NO BYPASSRLS; COMMENT ON ROLE juhuan IS 'polar_superuser'; CREATE ROLE polar_gawr_admin; ALTER ROLE polar_gawr_admin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NO REPLICATION NOBYPASSRLS; CREATE ROLE polar_gawr_user; ALTER ROLE polar_gawr_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NOR EPLICATION NOBYPASSRLS; CREATE ROLE polardb_admin; ALTER ROLE polardbadmin WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION B
```

capabilities `_`

```
YPASSRLS; CREATE ROLE replicator; ALTER ROLE replicator WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; CREATE ROLE rs_user; ALTER ROLE rs_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS;
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET extra_float_digits TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET lock_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET statement_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "aurora"
```

`--` capabilities

```
ALTER ROLE aurora SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET extra_float_digits TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET lock_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET statement_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` capabilities `--`

```
-- User Config "rs_user"
```

`--`

```
ALTER ROLE rs_user SET default_transaction_read_only TO 'on';
```

`--`

```
-- Role memberships
```

`--`

```
GRANT pg_polar_superuser TO juhuan GRANTED BY aurora;
```

`--`

```
-- PostgreSQL database cluster dump complete
```

`--`
2. Run the following command to import user permissions to the destination PolarDB for
PostgreSQL database:

```
 psql -h <host> -p 5432 -U aurora -f pg_roles.sql
```

3. Run the following statements to verify the permissions:

```
SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = 'app_user' AND table_name = '<TABLE_NAME>' AND table_schema = 'public';
```

##### 15.1.3.2 Use DTS to migrate data

###### 15.1.3.2.1 Data migration

This topic describes how to migrate data. You can migrate data from an on-premises database, self-managed database, or thirdparty database to an Alibaba Cloud database. This method is suitable for one-time tasks, such as cloud migration, database sharding, and database scale-out.

**Procedure**

Data migration applies to database migration scenarios.
1. Log on to the Data Transmission Service (DTS) console. On the **Data Migration** page, click
**Create Task**, select a region, and specify the number of tasks that you want to create.
capabilities
2. On the Data Migration page, find the data migration task that you created and click
**Configure Task** to configure the source and destination databases. The following table
describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| None | Task Name | The name of the DTS task. DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB for PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. Select No. |
|   | Architecture | The architecture of the source database. Select Two Nodes with Local Disks. |
|   | PolarDB Cluster ID | Select the ID of the source PolarDB for PostgreSQL cluster. |
|   | Database Name | The name of the database in the source PolarDB for PostgreSQL cluster. |
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL cluster. The account must have the owner permission on the database to which the data to be migrated belongs. |
|   | Database Password | Enter the password of the database account. |
|   | Encryption | Configure this parameter based on your business requirements. |
|   | Database Type | The type of the destination database. SelectP olarDB for PostgreSQL. |

| saraDB for POLA | PolarDB for PostgreSQL (Primary RDB Secondary Edition) User Guide·A capabilitie |   |
|---|---|---|
| Destination Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|   | Architecture | The architecture of the destination database. SelectT wo Nodes with Local Disks. |
|   | PolarDB Cluster ID | Select the ID of the destination PolarDB for PostgreSQL cluster. |
|   | Database Name | The name of the database used to receive data in the destination PolarDB for PostgreSQL cluster. |
|   | Database Account | The database account of the destination PolarDB for PostgreSQL cluster. The account must have the owner permissions on schemas. |
|   | Database Password | Enter the password of the database account. |
|   | Encryption | Configure this parameter based on your business requirements. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. If an IP address whitelist is configured for your PolarDB for PostgreSQL cluster, you must
add the CIDR blocks of DTS servers to the whitelist. Then, click **Test Connectivity and**
**Proceed**.
If no whitelist is configured for your PolarDB for PostgreSQL cluster, ignore the whitelist settings and click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Parame ter | Description |
|---|---|

capabilities

| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated, or the data migration task fails. |
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select another option to ensure that the capitalization of object names is the same as that of the source or destination database. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select schemas or tables as the objects to be migrated. |

capabilities

| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|

6. Click **Next: Advanced Settings** to configure advanced settings. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you specify different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is specified takes precedence. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.
8. Wait until **Success Rate** displays 100% and then click **Back**.
If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

###### 15.1.3.2.2 Data synchronization

capabilities This topic describes how to synchronize data. The data synchronization feature is mainly used for table-level continuous tasks. It is applicable to the following scenarios: active geo-redundancy, disaster recovery, data backup, data synchronization across clouds, load balancing, cloud business intelligence (BI) systems, and real-time data warehousing.

**Procedure**

1. Log on to the DTS console. On the **Data Synchronization** page, click **Create Task**, select
a region, and specify the number of tasks that you want to create.
2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task**.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| None | Task Name | The name of the DTS task. DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB for PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization task. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data between instances that belong to different Alibaba Cloud accounts. Select No. |
|   | Architectur e | The architecture of the source database. Select Two Nodes with Local Disks. |
|   | PolarDB Cluster ID | Select the ID of the source PolarDB for PostgreSQL cluster. |

capabilities

|   | Database Name | The name of the database in the source PolarDB for PostgreSQL cluster. |
|---|---|---|
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL cluster. The account must have the owner permission on the database to which the data to be synchronized belongs. |
|   | Database Password | Enter the password of the database account. |
|   | Encryption | Configure this parameter based on your business requirements. |
|   | Database Type | The type of the destination database. SelectP olarDB for PostgreSQL. |
| Destination Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization task. You cannot change the value of this parameter. |
|   | Architectur e | The architecture of the destination database. SelectT wo Nodes with Local Disks. |
|   | PolarDB Cluster ID | Select the ID of the destination PolarDB for PostgreSQL cluster. |
|   | Database Name | The name of the database used to receive data in the destination PolarDB for PostgreSQL cluster. |
|   | Database Account | The database account of the destination PolarDB for PostgreSQL cluster. The account must have the owner permissions on schemas. |
|   | Database Password | Enter the password of the database account. |
|   | Encryption | Configure this parameter based on your business requirements. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
capabilities
5. If an IP address whitelist is configured for your PolarDB for PostgreSQL cluster, you must
add the CIDR blocks of DTS servers to the whitelist. Then, click **Test Connectivity and**
**Proceed**.
If no whitelist is configured for your PolarDB for PostgreSQL cluster, ignore the whitelist settings and click **Test Connectivity and Proceed**.
6. Select the objects to be synchronized and the synchronization types. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of the selected objects from the source database to the destination database. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases use the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select another option to ensure that the capitalization of object names is the same as that of the source or destination database. |

capabilities

| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can select schemas or tables as the objects to be synchronized. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination instance, the name of the object remains unchanged. Note To select SQL operations for the synchronization task, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE clauses to filter data, right-click a table in the Selected Objects section. In the dialog box that appears, specify the filter conditions. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings** to configure advanced settings. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you specify different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is specified takes precedence. |

capabilities
8. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.
9. Wait until **Success Rate** displays 100% and then click **Back**.

#### 15.1.4 Migrate data from ApsaraDB RDS for PostgreSQL to PolarDB for PostgreSQL through visualized operations

**PostgreSQL to PolarDB for PostgreSQL**

**through visualized operations**

This topic describes how to migrate data from an ApsaraDB RDS for PostgreSQL instance to a PolarDB for PostgreSQL cluster through visualized operations.
1. . Overview**
Solution overview: After you create a PolarDB for PostgreSQL cluster, you can use Data Transmission Service (DTS) to migrate data to the PolarDB for PostgreSQL cluster. You only need to change the service address after the migration.

| ApsaraDB RDS for | Online Migration | Create a PolarDB for |
|---|---|---|

**PostgreSQL**

**PostgreSQL cluster**

**Instance**

**Configure**

**the same**

**CIDR block**

**ApsaraDB RDS for**

**PolarDB for PostgreSQL**

**PostgreSQL**

**Cluster**

**Migrate**

**Instance**

**data online**

**Enterprise**

**Edition**

**Server**

**Server**

**ApsaraDB RDS for**

**PolarDB for**

**PostgreSQL**

**PostgreSQLResource**

**Usage notes**

capabilities The migration operation requires your permission. After the migration, the endpoint for connecting to the instance is changed. We recommend that you perform the migration during off-peak hours.

**Benefits**

Supports endpoint migration: You can use a Domain Name System (DNS) record to establish communication without the need to change the endpoint on the application. Supports migration rollback: You can roll back to the previous instance at any time. Supports visible migration progress at any time: You can view the migration progress at any time. Supports incremental migration with a downtime of less than 10 minutes: DTS supports incremental migration.

**Limits**

Cross-region migration is not supported: You can migrate data only between instances in the same region. Possible syntax differences between Postgres versions: PolarDB for PostgreSQL 14 and PolarDB for PostgreSQL 16 are fully compatible with PostgreSQL 14 and 16. When you upgrade to a later version, you need to check whether syntax differences exist. Alibaba Cloud provides methods for compatibility check. You can refer to the "Check the syntax compatibility" section of this topic to perform compatibility checks for your applications. Limits on endpoint changes: Only the DNS record is modified when the endpoint to the instance is changed. The following limits apply: Only the connection address is switched from the endpoint of the ApsaraDB RDS for PostgreSQL instance to the endpoint of the PolarDB for PostgreSQL cluster. The other configurations, such as the vSwitches and virtual IP addresses (VIPs), remain unchanged. Ports are not changed: Ports are not changed even if the connection address is changed. The PolarDB for PostgreSQL cluster uses the same ports, excluding custom ports, as the ApsaraDB RDS for PostgreSQL instance. For more information about how to modify the ports, see the "View and change the endpoints and port numbers" topic in the ApsaraDB RDS for PostgreSQL User Guide. Possible DNS caching failures: After the endpoint is changed, issues may arise due to the expiration of the DNS cache. You may fail to connect to the PolarDB for PostgreSQL cluster or only read operations are supported. To fix this issue, we recommend that you refresh the DNS cache of your server. DTS does not support plug-in migration or account migration.
2. . Create a PolarDB for PostgreSQL cluster**
Create a PolarDB for PostgreSQL cluster before you perform the migration. To prevent data errors and chaos, we recommend that you perform tests and drills before you migrate data.

**Usage notes**

Instance type: We recommend that you use the same instance type as the ApsaraDB RDS for PostgreSQL instance. VPC: We recommend that you deploy the PolarDB for PostgreSQL cluster in the same VPC as the ApsaraDB RDS for PostgreSQL instance. If you use a different VPC, make sure that the VPC is accessible to applications before you start the migration. Network whitelist: After you create a PolarDB for PostgreSQL cluster, configure the same network whitelist as the ApsaraDB RDS for PostgreSQL instance to prevent application inaccessibility. capabilities The instance ID changes after the migration. If you are in one of the following scenarios, we recommend that you communicate with the relevant teams in advance to ensure that all involved systems are switched after the migration. The migration does not change the connection string information, and does not affect the existing endpoints. However, if you change the configurations, you need to update the configurations in the following systems: Database services: DTS and Data Management (DMS) that are accessed over cloud instances. Big data services: DataWorks and DataHub that are accessed over cloud instances. CloudMonitor: CloudMonitor monitors the destination instance after the migration. Data Security Center (DSC, formerly known as SDDP) does not support PolarDB.
3. . Pre-upgrade check on the ApsaraDB RDS for PostgreSQL**

**instance**

**Check the kernel parameter configurations of the ApsaraDB**

**RDS for PostgreSQL instance**

The ApsaraDB RDS for PostgreSQL instance cannot be empty. In other words, the data volume of the database cannot be 0. The value of the `wal_level` kernel parameter must be logical. The value of the `max_replication_slots` parameter must be greater than the total number of two-way DTS connections required, as indicated by the number of databases involved. The value of the `max_wal_senders` parameter must be greater than the total number of two-way DTS connections required, as indicated by the number of databases involved.

**Check the syntax compatibility**

PolarDB for PostgreSQL is fully compatible with the syntax of ApsaraDB RDS for PostgreSQL, excluding plug-ins. Therefore, you can check the syntax compatibility on the official PostgreSQL website or use the pg_upgrade best practices provided by Apsara Stack for syntax compatibility check.

**(Optional) Best practices for syntax compatibility check by using pg_upgrade**

pg_upgrade: pg_upgrade is an Apsara Stack tool that supports cross-version in-place upgrades. You do not need to perform export or import operations. `pg_upgrade` supports upgrades from PostgreSQL 8.4.X to the latest version, including snapshots and test versions. pg_upgrade supports pre-upgrade compatibility check, which detects plug-in incompatibility, data type inconsistency, and other issues. Example: The RDS-PG13 kernel version on Apsara Stack 3.16.2 is 13.14, and the PolarDB-PG14 kernel version is 14.13. You can use the following method to check the compatibility. capabilities

**ApsaraDB**

**ECS**

**Instance for**

**RDS**

**Instance**

**Verification**

PG_13.14 PG_14.13 Instance_1

**dump/restore**

ins1_db_1 db_1 ins1_db_1 ins1_db_n db_n ins1_db_n

**pg_upgrade --check**

Instance_n db_1 ins1_db_1 ins1_db_1 db_n ins1_db_n ins1_db_n Procedure:
1. Apply for an Elastic Compute Service (ECS) instance that runs CentOS 7.9 or another OS
version on Apsara Stack. In this example, CentOS 7.9 is used.
2. Download the installation packages of the open source PostgreSQL 13.14 and 14.13 and
their dependencies from the official website.
3. Install the open source PostgreSQL 13.14 and 14.13 versions. RPM packages are used to
install PostgreSQL 13.14 and 14.13.

```bash
# postgresql 13.14
rpm -ivh libicu-50.2-4.el7_7.x86_64.rpm rpm -ivh postgresql13-libs-13.14-1PGDG.rhel7.x86_64.rpm rpm -ivh postgresql13-13.14-1PGDG.rhel7.x86_64.rpm rpm -ivh postgresql13-server-13.14-1PGDG.rhel7.x86_64.rpm
# postgresql 14.13
rpm -ivh postgresql14-libs-14.13-2PGDG.rhel7.x86_64.rpm rpm -ivh postgresql14-14.13-2PGDG.rhel7.x86_64.rpm rpm -ivh postgresql14-server-14.13-2PGDG.rhel7.x86_64.rpm
```

4. Start PostgreSQL.

```python
# postgresql 13.14
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb sudo systemctl enable postgresql-13 sudo systemctl start postgresql-13 /usr/pgsql-13/bin/psql --version
# postgresql 14.13
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb sudo systemctl enable postgresql-14 sudo systemctl start postgresql-14 /usr/pgsql-14/bin/psql --version
```

capabilities
5. Use a privileged account, such as aurora, to export all structures and data by using
pg_dump on RDS-PG13. i. Obtain the password of the aurora user. ii. Run the following command to export data:

```
 pg_dump -h <host> -p 5432 -U aurora -F c -f rds_pg_13.dump <database>
```

6. Run the pg_restore command to import PostgreSQL 13.x.

```
 pg_restore -h <host> -p 5432 -U postgres -d <database> -F c rds_pg_13.dump
```

7. Run the following commands to stop PostgreSQL 13.x and PostgreSQL 14.x:

```python
sudo systemctl stop postgresql-13 sudo systemctl stop postgresql-14
```

8. Use the pg_upgrade tool to check the compatibility.

```bash
# Switch to the PostgreSQL user.
su - postgres
# Run compatibility checks.
/usr/pgsql-14/bin/pg_upgrade \
  --old-bindir=/usr/pgsql-13/bin \
  --new-bindir=/usr/pgsql-14/bin \
  --old-datadir=/var/lib/pgsql/13/data \
  --new-datadir=/var/lib/pgsql/14/data \
  --check
```

The following results show that the check objects pass the compatibility checks: capabilities

```
[root@iZuf6dpv3pu9lsc2zt2dnlZ ~]# su - postgres Last logon: 21:11:51 (UTC+8) on Monday, December 9, 2024 from pts/0 -bash-4.2$ -bash-4.2$ /usr/pgsql-14/bin/pg_upgrade \
>   --old-bindir=/usr/pgsql-13/bin \
>   --new-bindir=/usr/pgsql-14/bin \
>   --old-datadir=/var/lib/pgsql/13/data \
>   --new-datadir=/var/lib/pgsql/14/data \
>   --check
Performing Consistency Checks ----------------------------- Checking cluster versions ok Checking database user is the install user ok Checking database connection settings ok Checking for prepared transactions ok Checking for system-defined composite types in user tables ok Checking for reg* data types in user tables ok Checking for contrib/isn with bigint-passing mismatch ok Checking for user-defined encoding conversions ok Checking for user-defined postfix operators ok Checking for incompatible polymorphic functions ok Checking for presence of required libraries ok Checking database user is the install user ok Checking for prepared transactions ok Checking for new cluster tablespace directories ok *Clusters are compatible*
```

If an incompatible issue is detected, we recommend that you switch to another version based on the PostgreSQL manual.

**Check the plug-in compatibility**

Perform plug-in compatibility checks on the ApsaraDB RDS for PostgreSQL instance and PolarDB for PostgreSQL cluster. For more information about plug-in compatibility, see List of plug-ins supported by ApsaraDB RDS for PostgreSQL and List of plug-ins supported by PolarDB for PostgreSQL.

**Migrate accounts from the ApsaraDB RDS for PostgreSQL**

**instance to the PolarDB for PostgreSQL instance**

Procedure:
1. Export user permissions from the source ApsaraDB RDS database. For more information
about the users, see the preceding section. i. Use a privileged account, such as aurora. ii. Run the following command to export user permissions:

| pg dumpall -h <host> -p 5432 -U aurora --roles-only --no-role-passwords > _ |   |
|---|---|

The following SQL statements are exported: `--`

```
-- PostgreSQL database cluster dump
```

`--` capabilities

```
SET default_transaction_read_only = off; SET client_encoding = 'UTF8'; SET standard_conforming_strings = on;
```

`--`

```
-- Roles
```

`--`

```
CREATE ROLE aurora; ALTER ROLE aurora WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS; CREATE ROLE juhuan; ALTER ROLE juhuan WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; COMMENT ON ROLE juhuan IS 'polar_superuser'; CREATE ROLE polar_gawr_admin; ALTER ROLE polar_gawr_admin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NOREPLICATION NOBYPASSRLS; CREATE ROLE polar_gawr_user; ALTER ROLE polar_gawr_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN N OREPLICATION NOBYPASSRLS; CREATE ROLE polardb_admin; ALTER ROLE polardb_admin WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS; CREATE ROLE replicator; ALTER ROLE replicator WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; CREATE ROLE rs_user; ALTER ROLE rs_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS;
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET extra_float_digits TO '0';
```

`--`

```
-- User Config "aurora"
```

`--` capabilities

```
ALTER ROLE aurora SET lock_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET statement_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET extra_float_digits TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET lock_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--` capabilities

```
ALTER ROLE replicator SET statement_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "rs_user"
```

`--`

```
ALTER ROLE rs_user SET default_transaction_read_only TO 'on';
```

`--`

```
-- Role memberships
```

`--`

```
GRANT pg_polar_superuser TO juhuan GRANTED BY aurora;
```

`--`

```
-- PostgreSQL database cluster dump complete
```

`--`
2. Check and modify the roles.sql file to filter out irrelevant data such as system users.
The default system users of ApsaraDB RDS include **alicloud_rds_admin** and **aurora**.
3. Run the following command to import user permissions to the destination PolarDB for
PostgreSQL database:

```
 psql -h <host> -p 5432 -U aurora -f rewrite_rds_pg_13_roles.sql
```

4. Run the following statements to verify the permissions:
capabilities

```
SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = 'app_user' AND table_name = '<TABLE_NAME>' AND table_schema = 'public';
```

4. . Use DTS to migrate data**

**Data migration procedure**

Data migration applies to database migration scenarios.
1. Log on to the DTS console. On the **Data Migration** page, click **Create Task**, select a
region, and specify the number of tasks that you want to create. During the migration process, the connection to the database may be closed several times. We recommend that you do not use the db owner user to perform the migration. If you create a privileged user to perform the migration, you may not have sufficient permissions on certain objects. We recommend that you use the super administrator aurora defined by ApsaraDB RDS and PolarDB to migrate data on DTS.
2. On the Data Migration page, find the data migration task that you created and click
**Configure Task**.
Do not use domain names to connect the source and destination databases because the domain names of the databases will be replaced in subsequent steps.

| Section | Parameter | Description |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Select No. |

capabilities

|   | Instance ID | Select the ID of the database that you want to migrate. |
|---|---|---|
|   | Database Name | Enter the name of the source database. |
|   | Database Account | Enter the account that has read and write permissions on the source database. |
|   | Database Password | Enter the password of the database account. |
| Destinatio n Database | Database Type | The type of the destination database. SelectP olarDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration task. You cannot change the value of this parameter. |
|   | Architecture | Select the architecture of the destination database. |
|   | PolarDB Cluster ID | Select the ID of the destination database instance. |
|   | Database Name | Enter the name of the destination database. |
|   | Database Account | Enter the account used to access the destination database. The account must have read and write permissions on the destination database. |
|   | Database Password | Enter the password of the database account. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. Select the objects to be migrated and the migration type.

| Paramet er | Description |
|---|---|

capabilities

| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same table schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database. If the source and destination databases have different table schemas, only specific columns are migrated, or the data migration task fails. |
| Source Objects | Select one or more objects in the Source Objects list and click the icon to add the objects to the Selected Objects list. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

5. Click **Next: Advanced Settings** to configure advanced settings.
capabilities

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

6. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails the precheck, click **View Details** and fix the issue by following the on-screen instructions. Then, perform a precheck again.
7. Wait until **Success Rate** displays 100% and then click **Back**.
If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

**Data synchronization procedure**

Data synchronization applies to table transmission and migration to the cloud.
1. Log on to the DTS console. On the **Data Synchronization** page, click **Create Task**, select
a region, and specify the number of tasks that you want to create.
2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** to configure the source and destination databases. capabilities

| Section | Parameter | Description |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Select No. |
|   | Instance ID | Select the ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | Enter the name of the source database. |
|   | Database Account | Enter the database account of the source ApsaraDB RDS for PostgreSQL instance. Specify a privileged account. The account must be the owner of the source database. |
|   | Database Password | Enter the password of the database account. |
|   | Database Type | The type of the destination database. SelectP olarDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

capabilities

| Destination Database |   |   |
|---|---|---|
|   | PolarDB Cluster ID | Select the ID of the destination database instance. |
|   | Database Name | Enter the name of the destination database. |
|   | Database Account | Enter the account used to access the destination database. The account must have read and write permissions on the destination database. |
|   | Database Password | Enter the password of the database account. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. Select the objects to be synchronized and the synchronization types.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same table schemas, DTS does not synchronize data records that have the same primary key values as data records in the destination database. If the source and destination databases have different table schemas, only specific columns are synchronized, or the data synchronization task fails. |
| Synchronization Topology | Select One-way Synchronization. |

capabilities

| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select another option to ensure that the capitalization of object names is the same as that of the source or destination database. |
|---|---|
| Source Objects | Select one or more objects (tables or databases) in theS ource Objects list and click the icon to add the objects to the Selected Objects list. Note You can select columns, tables, or databases as the objects to be synchronized. |
| Selected Objects | By default, after an object is synchronized to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that depend on the object may fail to be synchronized. |

5. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

capabilities

| Configure ETL | Specify whether to enable the ETL feature. Valid values: Yes: enables the ETL feature. You can enter data processing statements in the code editor. No: disables the ETL feature. |
|---|---|

6. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails the precheck, click **View Details** and fix the issue by following the on-screen instructions. Then, perform a precheck again.
7. Wait until Success Rate displays 100% and then click **Back**.

**Set a database user to read-only**

Procedure: Assume that the user used by the application system is app_user.
1. Set app_user to read-only.
2. Close the connections of app_user to ensure that the configuration of setting the user to
read-only takes effect. The database connection pool supports re-establishment of database connections.
3. Check whether app_user is set to read-only by inserting or updating data in a test table.

```
-- Set the specified user to read-only. ALTER USER app_user SET default_transaction_read_only TO ON; -- Close the connections of the specified user. SELECT pg_terminate_backend(pid) FROM pg_stat_activity where usename= 'app_user'; -- Check the connections of the specified user. SELECT * FROM pg_stat_activity where usename= 'app_user'; SELECT * FROM pg_catalog.pg_user WHERE usename='app_user';
```

Methods for enabling the read-only mode:

```
ALTER SYSTEM SET default_transaction_read_only TO on; SELECT pg_reload_conf(); SHOW default_transaction_read_only;
```

**Record the time when read-only mode is enabled**

Run the following statement to create a timestamp for data restoration from the backup:

```
SELECT CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Shanghai';
```

Check whether the time is the same as that in the DTS console. capabilities

**Verify data consistency**

Procedure:
1. Determine the end of data synchronization.
Traffic = 0 and delay = 1.
2. Use DTS to perform full data verification.
Log on to the Numen DTS O&M platform and create a full data verification task. You can adjust the parameters based on the data volume. Parameters and descriptions:

| Parameter | Description |
|---|---|
| -P 10 | The sampling percentage. By default, 100% of the data is verified. |
| -p 10 | The number of threads. |
| -b 10000 | The slice size. |
| -U 10000 | The number of verified metadata entries. It is determined by the total number of data entries and the sampling percentage. For example, if you have a total number of 1 million data entries and the sampling percentage is 1%, but only 10,000 data entries are verified, the number of verified metadata entries is 10,000. |
| -m 1000000 | The maximum number of inconsistent data entries allowed in a single table. |
| -n 10000 | The maximum number of data entries verified in a single table that does not have a primary key. |

3. Compare the number of data entries between the source and destination databases by
using SQL statements. Compare the number of data entries in the transaction table between the source and destination databases.
5. . Switch to the endpoint of the destination database**
Switch to the endpoint of the destination database during the migration process. After you update the DNS record, clients may still be connected to the source database due to the caching mechanism. You need to close the connections to the source database.

```
-- Close the connections of the specified user SELECT pg_terminate_backend(pid) FROM pg_stat_activity where usename= 'app_user'; -- Check the connections of the specified user. SELECT * FROM pg_stat_activity where usename= 'app_user';
```

6. . (Optional) Roll back the migration**
If you want to roll back the migration, perform Step 5 to switch to the endpoint of the source database. capabilities

##### 15.1.4.1 Use DTS to migrate data

###### 15.1.4.1.1 Migrate data

This topic describes how to migrate data. You can migrate data from an on-premises database, self-managed database, or thirdparty database to an Alibaba Cloud database. This method is suitable for one-time tasks, such as cloud migration, database sharding, and database scale-out.
1. Log on to the Data Transmission Service (DTS) console. On the **Data Migration** page, click
**Create Task**, select a region, and specify the number of instances.
During the migration process, the connection to the database may be closed several times. We recommend that you do not use the db owner user to perform the migration. If you create a privileged user to perform the migration, you may not have sufficient permissions on certain objects. We recommend that you use the super administrator aurora defined by ApsaraDB RDS and PolarDB to migrate data on DTS.
2. On the Data Migration page, find the data migration instance that you created and click
**Configure Task**. Then, configure the source and destination databases.
Do not use domain names to connect the source and destination databases because the domain names of the databases will be replaced in subsequent steps. capabilities

| Section | Parameter | Description |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PostgreSQL for PostgreSQL. |
|   | Access Method | The access method of the database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. In this example, No is selected. |
|   | PolarDB Cluster ID | The ID of the database that you want to migrate. |
|   | Database Name | Enter the name of the source database. |
|   | Database Account | The account that has read and write permissions on the source database. |
|   | Database Password | The password of the database account. |
|   | Database Engine | The type of the destination database. SelectP olarDB for PostgreSQL. |
|   | Access Method | The access method of the database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Architecture | The architecture of the destination database. |

capabilities

| Destinatio n Database |   |   |
|---|---|---|
|   | PolarDB Cluster ID | The ID of the destination database instance. |
|   | Database Name | The name of the destination database to which you want to migrate data on the destination instance. |
|   | Database Account | The account used to access the destination database. The account must have read and write permissions on the destination database. |
|   | Database Password | The password that is used to access the database. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. Select the objects to be migrated and the migration types.

| Paramet er | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source database and destination cluster. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary key values as data records in the destination database. If the source and destination databases have different table schemas, only specific columns are migrated, or the data migration task fails. |

capabilities

| Source Objects | Select one or more objects in the Source Objects list and click the icon to move the objects to the Selected Objects list. Note You can select columns, tables, or databases as the objects to be migrated. |
|---|---|
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

5. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. If not, the migration task fails. Note If you specify different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is specified takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

6. In the lower part of the page, click **Next: Precheck and Start Task**.
capabilities

**Important**

Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click **View Cause** and fix the issue by following the on-screen instruction. Then, perform a precheck again.
7. Wait until **Success Rate** displays 100% and then click **Back**.
If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

###### 15.1.4.1.2 Data synchronization

This topic describes how to synchronize data. The data synchronization feature is mainly used for table-level continuous tasks. It is applicable to the following scenarios: active geo-redundancy, disaster recovery, data backup, data synchronization across clouds, load balancing, cloud business intelligence (BI) systems, and real-time data warehousing.
1. Log on to the Data Transmission Service (DTS) console. In the left-side navigation pane,
click Data Synchronization. On the **Data Synchronization** page, click **Create Task**. In the panel that appears, select a region and specify the number of tasks that you want to create.
2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** to configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
|   | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

capabilities

| Source Database |   |   |
|---|---|---|
|   | Replicate Data Across Alibaba Cloud Accounts | Select No. |
|   | Instance ID | Select the ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | Enter the name of the source database. |
|   | Database Account | Enter the database account of the source ApsaraDB RDS for PostgreSQL instance. Specify a privileged account. The account must be the owner of the source database. |
|   | Database Password | Enter the password of the database account. |
| Destination Database | Database Type | The type of the destination database. SelectP olarDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | PolarDB Cluster ID | Select the ID of the destination database instance. |
|   | Database Name | Enter the name of the destination database. |
|   | Database Account | Enter the account used to access the destination database. The account must have read and write permissions on the destination database. |
|   | Database Password | Enter the password of the database account. |

3. In the lower part of the page, click **Test Connectivity and Proceed**.
4. Select the objects to be synchronized and the synchronization types.
capabilities

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of the selected objects from the source database to the destination database. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same table schemas, DTS does not synchronize data records that have the same primary key values as data records in the destination database. If the source and destination databases have different table schemas, only specific columns are synchronized or the data synchronization task fails. |
| Synchronization Topology | Select One-way Synchronization. |
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select another option to ensure that the capitalization of object names is the same as that of the source or destination database. |
| Source Objects | Select one or more objects (tables or databases) in theS ource Objects list and click the icon to add the objects to the Selected Objects list. Note You can select columns, tables, or databases as the objects to be synchronized. |

capabilities

| Selected Objects | By default, after an object is synchronized to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that depend on the object may fail to be synchronized. |
|---|---|

5. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minute. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specify whether to enable the ETL feature. Valid values: Yes: enables the ETL feature. You can enter data processing statements in the code editor. No: disables the ETL feature. |

6. In the lower part of the page, click **Next: Precheck and Start Task**.

**Important**

Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails the precheck, click **View Details** and fix the issue by following the on-screen instructions. Then, perform a precheck again.
7. Wait until Success Rate displays 100% and then click **Back**.
capabilities

###### 15.1.4.1.3 View data migration tasks

This topic describes how to view data migration tasks and their status.

**Procedure**

1. Log on to the Data Transmission Service (DTS) console.
2. In the left-side navigation pane, click **Data Migration**.
3. Select the migration instance whose migration status and progress you want to view.
To view detailed information, click **Task Details** for the migration instance.

##### 15.1.4.2 Prechecks

###### 15.1.4.2.1 Syntax compatibility check

This topic describes how to perform a syntax compatibility check.

**Overview**

PolarDB for PostgreSQL is fully compatible with the syntax of ApsaraDB RDS for PostgreSQL, excluding plug-ins. Therefore, you can check the syntax compatibility on the official PostgreSQL website or use the pg_upgrade best practices provided by Apsara Stack for syntax compatibility check.

**Best practice for checking syntax compatibility by using**

**pg_upgrade**

pg_upgrade: a tool provided by Alibaba Cloud for in-place upgrades across versions. This tool does not require you to perform import or export operations. `pg_upgrade` supports upgrades from PostgreSQL 8.4.X to the latest version, including snapshots and test versions. pg_upgrade also supports pre-upgrade compatibility checks, which detect incompatibility issues related to plug-ins and data types. The following example shows how to perform a compatibility check. The kernel version of RDS-PG13 on Apsara Stack 3.16.2 is 13.14, and the kernel version of PolarDB-PG14 is 14.13. You can use the following method to check the compatibility. Procedure:
1. Apply for an Elastic Compute Service (ECS) instance on Apsara Stack and install CentOS 7.9
on the ECS instance. You can also install another OS version.
2. Download the installation packages of open source PostgreSQL 13.14 and 14.13 and the
dependencies from the official site.
3. Install the open source PostgreSQL 13.14 and 14.13 versions. RPM packages are used to
install PostgreSQL 13.14 and 14.13. capabilities

```bash
# postgresql 13.14
rpm -ivh libicu-50.2-4.el7_7.x86_64.rpm rpm -ivh postgresql13-libs-13.14-1PGDG.rhel7.x86_64.rpm rpm -ivh postgresql13-13.14-1PGDG.rhel7.x86_64.rpm rpm -ivh postgresql13-server-13.14-1PGDG.rhel7.x86_64.rpm
# postgresql 14.13
rpm -ivh postgresql14-libs-14.13-2PGDG.rhel7.x86_64.rpm rpm -ivh postgresql14-14.13-2PGDG.rhel7.x86_64.rpm rpm -ivh postgresql14-server-14.13-2PGDG.rhel7.x86_64.rpm
```

4. Start PostgreSQL.

```python
# postgresql 13.14
sudo /usr/pgsql-13/bin/postgresql-13-setup initdb sudo systemctl enable postgresql-13 sudo systemctl start postgresql-13 /usr/pgsql-13/bin/psql --version
# postgresql 14.13
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb sudo systemctl enable postgresql-14 sudo systemctl start postgresql-14 /usr/pgsql-14/bin/psql --version
```

5. Use a privileged account, such as aurora, to export all structures and data by using
pg_dump on RDS-PG13. i. Obtain the password of the aurora user. ii. Run the following command to export data:

```
 pg_dump -h <host> -p 5432 -U aurora -F c -f rds_pg_13.dump <database>
```

6. Run the pg_restore command to import PostgreSQL 13.x.

```
 pg_restore -h <host> -p 5432 -U postgres -d <database> -F c rds_pg_13.dump
```

7. Run the following commands to stop PostgreSQL 13.x and PostgreSQL 14.x:

```python
sudo systemctl stop postgresql-13 sudo systemctl stop postgresql-14
```

8. Use the pg_upgrade tool to check the compatibility.

```bash
# Switch the user.
su - postgres
# Perform a compatibility check.
/usr/pgsql-14/bin/pg_upgrade \
  --old-bindir=/usr/pgsql-13/bin \
  --new-bindir=/usr/pgsql-14/bin \
  --old-datadir=/var/lib/pgsql/13/data \
  --new-datadir=/var/lib/pgsql/14/data \
  --check
```

The following result is returned: capabilities

```
[root@iZuf6dpv3pu9lsc2zt2dnlZ ~]# su - postgres Last logon: 21:11:51 (UTC+8) on Monday, December 9, 2024 from pts/0 -bash-4.2$ -bash-4.2$ /usr/pgsql-14/bin/pg_upgrade \
>   --old-bindir=/usr/pgsql-13/bin \
>   --new-bindir=/usr/pgsql-14/bin \
>   --old-datadir=/var/lib/pgsql/13/data \
>   --new-datadir=/var/lib/pgsql/14/data \
>   --check
Performing Consistency Checks ----------------------------- Checking cluster versions ok Checking database user is the install user ok Checking database connection settings ok Checking for prepared transactions ok Checking for system-defined composite types in user tables ok Checking for reg* data types in user tables ok Checking for contrib/isn with bigint-passing mismatch ok Checking for user-defined encoding conversions ok Checking for user-defined postfix operators ok Checking for incompatible polymorphic functions ok Checking for presence of required libraries ok Checking database user is the install user ok Checking for prepared transactions ok Checking for new cluster tablespace directories ok *Clusters are compatible*
```

If an incompatible issue is detected, we recommend that you switch to another version based on the PostgreSQL manual.

###### 15.1.4.2.2 Check the compatibility of extensions

This topic describes how to check the compatibility of extensions. Perform the check on both the ApsaraDB RDS for PostgreSQL instance and the PolarDB for PostgreSQL instance to identify extension compatibility issues. For more information about extension compatibility, see List of plug-ins supported by ApsaraDB RDS for PostgreSQL and List of plug-ins supported by PolarDB for PostgreSQL.

###### 15.1.4.2.3 Migrate accounts from the ApsaraDB RDS for PostgreSQL instance to the PolarDB for PostgreSQL cluster

**RDS for PostgreSQL instance to the PolarDB for**

**PostgreSQL cluster**

This topic describes how to migrate an account from an ApsaraDB RDS for PostgreSQL instance to a PolarDB for PostgreSQL cluster.

**Procedure**

1. Export user permission information from the ApsaraDB RDS for PostgreSQL instance.
capabilities i. Use a privileged account, for example, aurora. ii. Run the following command to export user permission information:

| pg dumpall -h <host> -p 5432 -U aurora --roles-only --no-role-passwords > _ |   |
|---|---|

The following code block shows the exported SQL content: `--`

```
-- PostgreSQL database cluster dump
```

`--`

```
SET default_transaction_read_only = off; SET client_encoding = 'UTF8'; SET standard_conforming_strings = on;
```

`--`

```
-- Roles
```

`--`

```
CREATE ROLE aurora; ALTER ROLE aurora WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS; CREATE ROLE juhuan; ALTER ROLE juhuan WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; COMMENT ON ROLE juhuan IS 'polar_superuser'; CREATE ROLE polar_gawr_admin; ALTER ROLE polar_gawr_admin WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN NOREPLICATION NOBYPASSRLS; CREATE ROLE polar_gawr_user; ALTER ROLE polar_gawr_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB NOLOGIN N OREPLICATION NOBYPASSRLS; CREATE ROLE polardb_admin; ALTER ROLE polardb_admin WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS; CREATE ROLE replicator; ALTER ROLE replicator WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN REPLICATION NOBYPASSRLS; CREATE ROLE rs_user; ALTER ROLE rs_user WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS;
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "aurora"
```

`--` capabilities

```
ALTER ROLE aurora SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET extra_float_digits TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET lock_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET statement_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "aurora"
```

`--`

```
ALTER ROLE aurora SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "TimeZone" TO 'UTC';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET "DateStyle" TO 'ISO,YMD';
```

`--`

```
-- User Config "replicator"
```

`--` capabilities

```
ALTER ROLE replicator SET extra_float_digits TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET lock_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET statement_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_session_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET polar_transaction_timeout TO '0';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET idle_in_transaction_session_timeout TO '3600000';
```

`--`

```
-- User Config "replicator"
```

`--`

```
ALTER ROLE replicator SET temp_file_limit TO '10000000';
```

`--`

```
-- User Configurations
```

`--` `--`

```
-- User Config "rs_user"
```

`--`

```
ALTER ROLE rs_user SET default_transaction_read_only TO 'on';
```

`--`

```
-- Role memberships
```

`--`

```
GRANT pg_polar_superuser TO juhuan GRANTED BY aurora;
```

`--`

```
-- PostgreSQL database cluster dump complete
```

`--` capabilities
2. Check and rewrite roles.sql to filter data, such as system users.
ApsaraDB RDS for PostgreSQL defines the following default system users:
**alicloud_rds_admin** and **aurora**.
3. Run the following command to import user permission information to the PolarDB for
PostgreSQL cluster.

```
 psql -h <host> -p 5432 -U aurora -f rewrite_rds_pg_13_roles.sql
```

4. Execute the following command to verify permissions:

```
SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = 'app_user' AND table_name = '<TABLE_NAME>' AND table_schema = 'public';
```

### 15.2 AI-native operations for MCP services

**services**

AI-native operations for Model Context Protocol (MCP) services provided by PolarDB provide standard, secure, and efficient database access capabilities for large language models (LLMs). With MCP services, AI applications can directly query data, execute SQL statements, or manage database instances, without writing complex code. This enables the quick implementation of AI-native scenarios such as Retrieval-Augmented Generation (RAG), intelligent O&M, and data Q&A.

**Go to the AI-Native API: MCP Service page**

Log in to the **PolarDB console**. In the left-side navigation pane, choose **AI Capabilities >**
**AI-Native API: MCP Service**. On the page that appears, you can view and use multiple MCP
integration solutions to efficiently enable AI applications to access databases.

**Integration solution**

MCP services provide three flexible integration methods to meet different requirements, from quick experience to production integration.

| Solution | Scenario | Solution details |
|---|---|---|
| Hosting mode of Apsara Copilot (recommended for beginners) | Suitable for users who want to quickly verify AI and database scenarios. MCP service deployment or development is not required. | 1. On a page of the PolarDB console, click the Apsara Copilot icon. 2. In the panel that appears, click the Details icon, turn on MCP, and then click Settings. 3. The system automatically loads available MCP agents and services. 4. In the Select MCP panel, select the corresponding functional module as required. |

capabilities

| Hosting mode of AI Gateway (recommended for production integration) | Suitable for enterprise- level AI application integration. Apsara Stack manages backend MCP services. You need to activate only the required MCP service. | 1. Log in to the AI Gateway console. 2. Go to the details page of an AI gateway. Then, click MCP Management. 3. The system automatically loads available MCP agents and services. 4. Activate the required MCP service, such as the PolarDB syntax service or control service. |
|---|---|---|
| Self-deployment (suitable for private or custom deployment scenarios) | Suitable for users who need to privately deploy MCP services, customize the logic of MCP services, or integrate MCP services into their own agents or Robotic Process Automation (RPA) systems. | 1. Download a MCP service package. 2. Deploy the MCP service in an Elastic Compute Service (ECS) instance, a container, or an external server. 3. Integrate the MCP service as a backend service into an AI application, an agent, or a RPA process. 4. Use RESTful APIs or SDKs to call features of the MCP service. |

**Supported MCP services**

**MySQL syntax service of PolarDB MCP**

Overview: The MySQL syntax service of PolarDB MCP provides a native AI interface for MySQL, enabling LLMs to directly interact with databases for access, RAG augmentation, and other scenarios. Core features: `sqlQuery` : Executes read-only queries. `executeSql` : Performs write operations.

**PostgreSQL syntax service of PolarDB MCP**

Overview: The PostgreSQL syntax service of PolarDB MCP provides a native AI interface for MySQL, enabling LLMs to directly interact with databases for access, RAG augmentation, and other scenarios. Core features: `sqlQuery` : Executes read-only queries. `executeSql` : Performs write operations.

**MCP service for PolarDB management and control**

The service allows AI to intelligently manage your database instances. Scenarios: automated AI O&M, resource monitoring, and fault diagnostics. Core features and value:

| Feature | API | Value |
|---|---|---|

capabilities

| Query region availability. | DescribeRegionAvailabili ty | Helps users understand the availability of resources in different regions. This facilitates the selection of the optimal deployment region. |
|---|---|---|
| Query database instance attributes. | DescribeDBInstanceAttri bute | Provides comprehensive instance information. This facilitates user management and monitoring of database status. |
| Query the list of database instances. | DescribeDBInstances | Allows users to view and manage all database instances in a specific region. |
| Query resource usage. | DescribeResourceUsage | Helps users understand resource consumption and optimize resource allocation and cost management. |
| Query error logs. | DescribeErrorLogs | Help users quickly locate and resolve database operation issues. |
| Query performance data. | DescribeDBInstancePerf ormance | Provides performance metrics. This helps users monitor and optimize database performance. |
| Query slow logs. | DescribeSlowLogs | Helps users identify and optimize slow SQL statements. This improves database efficiency. |

### 15.3 Best practices for connecting PolarDB for PostgreSQL to Dify by using the MCP service

**PolarDB for PostgreSQL to Dify by**

**using the MCP service**

This topic describes how to connect a PolarDB for PostgreSQL instance to the Managed Capability Provider (MCP) service of AI Gateway and call this database query capability in the Dify platform of AI Studio. The MCP service encapsulates database operations into API operations that can be called by AI. This service is applicable to **intelligent Q&A and data**
**query**, and is not applicable to data changes or deletions. All components must be deployed
in the **same virtual private cloud (VPC)** to ensure network connectivity.

**Preparations**

Before you perform the operations that are described in this topic, make sure that you have completed the following preparations:

**Obtain the required permissions**

Your Apsara Stack tenant accounts have management permissions on the following services: PolarDB capabilities AI Gateway (Higress engine) Container Service for Kubernetes (ACK) Private DNS (PrivateZone) AI Studio (Dify)

**Confirm the network plan**

Ensure that the same VPC is used for unified deployment of the following resources: PolarDB for PostgreSQL cluster ACK cluster on which the AI Gateway (Higress engine) instance depends AI resource pool to which Dify belongs You must confirm the VPC ID of the destination ACK cluster in the ACK console in advance.

**Prerequisites**

| Component | Requirement |
|---|---|
| PolarDB for PostgreSQL cluster | The network type of the PolarDB for PostgreSQL cluster is VPC. The PolarDB for PostgreSQL cluster resides in the same VPC as the ACK cluster used by the AI Gateway instance. |
| AI Gateway instance | The engine used by the AI Gateway instance must be Higress. The destination ACK cluster is imported. The AI Gateway instance is in the same VPC as the PolarDB for PostgreSQL cluster. |
| Dify instance | The Dify instance is deployed in the previously mentioned VPC. The MCP Server-Sent Event (SSE) plug-in is installed. |
| Network connectivity | The external IP address of the VPC to which the AI Gateway instance belongs is added to the whitelist of the PolarDB for PostgreSQL cluster. The Dify instance can resolve MCP domain names through private DNS resolution. |

If the components are not deployed in the same VPC, you must use Cloud Enterprise Network (CEN), Express Connect, or VPC peering connection to establish network connections between these components. This topic does not cover cross-VPC scenarios.

**Usage notes**

capabilities
**Permission security**: The database account created for the MCP service is a regular
account and is granted only the required read-only permissions.
**DNS configuration**: A private domain name must end with a period ( `.` ), such as `mcp-`
`pg.example.com.` . Otherwise, domain name resolution may fail.
**Port protocol**: The default port of a PolarDB for PostgreSQL cluster is 5432. Select HTTP for
the MCP service. AI Gateway processes protocol conversion.
**Impact of restart**: After you modify a database whitelist or DNS settings, it may take
several seconds to several minutes for the changes to take effect.

**Step 1: Create an AI Gateway instance**

1. **Import the ACK cluster to the API Gateway console**
Log in to the **API Gateway console**. On the **Cluster Management** page, click **Importing**
**a K8s cluster**.

**Important**

The ACK cluster on which the AI Gateway instance depends and the PolarDB for PostgreSQL cluster that you create must **reside in the same VPC**.
**To find the VPC of the ACK cluster** , log in to the **ACK console**. On the
**Clusters** page, click the name of the cluster that you want to view. On the
cluster details page, click the **Cluster Resources** tab to view the details of the VPC.
2. **Create an AI Gateway instance**
On the **AI Gateway** page, click **Create an instance** and configure the following parameters: Gateway Type: Select **AI Gateway**. Deployment Architecture: Select **K8s**. Kubernetes Cluster: Select the ACK cluster imported in Step 1. For more information about how to configure other parameters, see the "Create a gateway instance" section in the AI Gateway User Guide on the API Gateway official website.
3. **Record the external IP address of the VPC to which the AI Gateway instance**

**belongs**

After the AI Gateway instance is created, you can obtain the external IP address of the VPC to which the AI Gateway instance belongs on the **Access Point** tab of the **Overview** page in the **API Gateway console**. Record the external IP address for subsequent database whitelist configuration.

**Step 2: Create and configure a PolarDB for PostgreSQL cluster**

1. **Create a PolarDB for PostgreSQL cluster**
When you create a PolarDB for PostgreSQL cluster, set the network type to **VPC** and make sure that the selected VPC **is the same as the VPC** for the ACK cluster on which the AI Gateway instance depends. capabilities After you create a PolarDB for PostgreSQL cluster, open the **Databases** tab of the instance details page. Create a database named `mcp_db_server` , and insert test data into the database. You can use DMS or a client to connect to the database and insert test data into the database. For more information, see Use DMS to log in to a PolarDB for PostgreSQL instance that uses local disks. On the **Accounts** tab of the instance details page, create a regular account and grant it the read-only permissions on the database that you created in the previous step. Currently, the MCP service supports only data query. **It does not support data**
**changes or deletions**. Therefore, you need to grant only the read-only permissions.
4. **Configure a database whitelist**
Click the **Data Security** tab of the instance details page, and add the external IP address obtained in Substep 3 of Step 1 to the whitelist of the database.
5. **Record the internal endpoint and port number of the database**
The internal endpoint and port number are used to create an MCP service in the AI Gateway instance later. For more information, see View the internal endpoint and port number.

**Step 3: Create an MCP service in the AI Gateway instance**

**3.1 Create a service**

Open the AI Gateway instance created in Step 1. On the **Service** tab of the instance details page, create a service. Configure the following parameters: Source Type: Select **DNS Domain Name**. Node: Select the internal endpoint and port number of the database that you obtained in Substep 5 of Step 2. Protocol Type: Select **HTTP**. For more information about how to configure other parameters, see the "Create a service" section in the AI Gateway User Guide on the API Gateway official website.

**3.2 Create a domain name**

Open the AI Gateway instance created in Step 1. On the **Domain name** tab of the instance details page, click **Associated Domain Name** and set Agreement to **HTTP**.

**3.3 Create an MCP service**

Open the AI Gateway instance created in Step 1. On the **MCP Management** tab of the instance details page, click **Create MCP Service**. Configure the following parameters: MCP Endpoint: Select the domain name created in Step 3.2. Service Type: Select **DB**. Backend Service: Select the service created in Step 3.1. Database configuration: Specify the database type, username, password, and database name based on the information configured in Step 2. capabilities For more information about how to configure other parameters, see the "Manage MCP services" section in the AI Gateway User Guide on the API Gateway official website.

**Step 4: Configure a private DNS instance (enable Dify to**

**resolve MCP domain names)**

1. **Add a domain name**
Log in to the **Alibaba Cloud DNS console**. In the left-side navigation pane, choose
**Private DNS > Private Domain Name for VPC** . On the **Tenant Internal Domain**
**Name** tab of the Private Domain Names for VPC page, click **Add Domain Name**. Set the
**Tenant Internal Domain Name** parameter to the domain name created in Step 3.2. **Add**
`a period (.)` to the end of the domain name.
2. **Add a DNS record**
Click **Configure DNS Records** in the **Actions** column of the domain name created in Step 4.1. On the page that appears, click **Add DNS Record**. Click **Add Entry** and enter the IP address obtained in Step 1.3. Leave the Record Name parameter empty.
3. **Associate with a VPC**
Click **Associate VPC** in the **Actions** column of the domain name created in Step 4.1. In the dialog box that appears, set the **Associate VPC** parameter **to the VPC of the AI**
**Gateway instance**.

**Step 5: Call the MCP service in Dify**

Before you use Dify, make the following preparations and take note of the following items: The resource pool and resource quota are configured. In the ACK console, add ECS instances and then add them to resource quotas. We recommend that you add two ECS instances, each with 16 cores, 32 GB of memory, and 200 GB of hard disks. To prevent unpredictable bugs or Dify creation failures due to resource preemption or node taints, we recommend that you create a dedicated resource quota for Dify, add ECS instances to this quota, and then create a Dify instance within this dedicated resource quota. By default, a Dify instance requires 4 CPU cores and 8 GB of memory.
1. **Create a Dify instance**
For more information, see Tutorials in AI Studio User Guide on the AI Studio official website. i. Log in to the **AI Studio console**. In the left-side navigation pane, choose **Agent**
**Development Platform > Dify Open Source Edition**. On the page that appears, click
**Create Dify**.
ii. In the Basic Configuration step, specify the environment name and description, select the created resource quota, enter the administrator password, and then click **Next**. capabilities iii. In the Parameter step, we recommend that you set the Dify version to 1.7.1. In addition, you must create a bucket in the OSS console and specify the bucket in a **Parameter** configuration item. Keep the default value of authVersion. iv. In the Plugin step, **the MCP SSE plug-in must be installed**. Install other plug-ins based on your business requirements. Wait until the application status changes to Running. This process usually takes about 5 minutes.
2. **Add a Dify user**
Before you create a Dify user, make sure that a Dify instance is created as described in Step 5.1 and the Dify instance is in the Running state. i. Log in to the **AI Studio console**. In the left-side navigation pane, choose **Agent**
**Development Platform > Dify Open Source Edition**. On the page that appears, find
the Dify instance that you created and click **User Management**. ii. Click **Add User**. iii. Select an unadded user from the associated users, enter an **8-character** password, and set the user as an **administrator**.
3. **Add a Dify model**
i. Click **Model Service Management** for the Dify instance. ii. Click **Add Model**. iii. Configure the model information. After you select configuration options, the model name, model URL, and API key are automatically specified. If no value is specified in the API key field, you are not the creator of the model service. Contact the creator of the online service to obtain the API key and enter it manually.
4. **Log in to the Dify instance**
i. Click the icon for the Dify instance. ii. In the dialog box that appears, specify **Email address** and **Password**, and then click
**Sign in**.
5. **Configure the MCP service**
After you open the details page of the Dify instance, choose **Tools > Discover and Call**
**MCP Tools > Authorization** to open the configuration tab of the MCP plug-in.
Edit the JSON configuration: Configure `server_name` based on your business requirements. Set `url` to the SSE endpoint obtained on the MCP management tab of the details page for the MCP service created in Step 3.3. capabilities `{`

```json
    "server_name": {
        "url": "xxxxxxxxxx",
        "headers": {},
        "timeout": 50,
        "sse_read_timeout": 50
```

`}` `}`
6. **Open the application and call the large language model to conduct query**

**conversations**

i. After you save the MCP configuration, click **Studio** and then select a specific application. ii. After you open the application and add MCP-related tools, you can interact with the large language model in the chatbox on the right. ppendix

## 16 Appendix

### 16.1 Authorize a tenant organization to access SLB

**organization to access SLB**

This topic describes how to grant a tenant organization the permissions to access Server Load Balancer (SLB) and helps you efficiently resolve related issues.

**Important**

If you need to create and use IPv6 addresses for your business, you must ensure that the current tenant organization has explicitly granted database services the permissions to access SLB. If such permissions are not granted, IPv6 addresses cannot be created.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the Service-linked Roles page, click **Create Service-linked Role** in the upper-left
corner. Select **Server Load Balancer** for the **Service Name** parameter, and select the organization to which you want to grant permissions for the **Authorized Organization**
**Name** parameter.
5. Click **OK**.

### 16.2 Launch templates

A launch template contains the configuration information required to create an instance. It stores key configuration settings, such as the instance type, storage, and network information, but excludes unique details like the instance name and password. You can use a launch template to quickly create an instance, which simplifies instance creation by eliminating the need to configure each parameter individually.

**Features and benefits**

All configurations in a launch template are optional. This provides flexibility and scalability for your instances, allowing you to customize instances for different scenarios.
**Preconfigured parameters**: You can specify settings such as the instance type, storage,
and network information in advance.
**Standardization and consistency**: Use templates to enforce the same configuration
standards across all instances. This improves consistency across your environment, reduces the risk of manual configuration errors, and simplifies management and maintenance.
**Fast deployment**: Create instances quickly by selecting a template, which reduces
deployment time by eliminating manual configuration.

**Limitations**

ppendix
**Quota**: In each region, you can create a maximum of 50 launch templates per resource set
in your account.
**Optional parameters**: All parameters are optional when you create a launch template.
However, if a template does not include required parameters, such as an instance type or an image, you must specify them when you use the template to create an instance.
**Immutable**: Launch templates are immutable once created.

**Create a launch template**

1. Log on to the Apsara Uni-manager console.
2. In the top navigation bar, click **Products > Databases**, and then select the target
database product.
3. On the list page for your target product, click **Create Instance** or **Create Cluster**, and
then configure the required parameters.
4. After you complete the configuration, click **Save as launch template** in the
**Configuration Overview** panel on the right.
5. In the **Save as launch template** dialog box, set the **Template Name**, **Sharing Scope**,
and **Template Version Description**, and then click **OK**.

**Create an instance from a launch template**

1. Log on to the Apsara Uni-manager console.
2. In the top navigation bar, click **Products > Databases**, and then select the target
database product.
3. On the list page for your target product, click **Create Instance** or **Create Cluster**, and
then click the **Create from Template** tab.
4. In the **Select a Template** area, select the launch template you want to use. After the
configuration information loads, review all the settings. You can modify the instance parameters to meet your needs.
5. Click **Submit**.

**Manage launch templates**

1. Log on to the Apsara Uni-manager console.
2. In the top navigation bar, click **Products > Databases**, and then select the target
database product.
3. On the list page for your target product, click **Create Instance** or **Create Cluster**, and
then click the **Create from Template** tab.
4. In the **Select a Template** area, click **Manage Templates**.
5. On the template list page, you can perform the following actions:
ppendix

| Actions | Procedure |
|---|---|
| Edit a template | i. Click Edit in the Actions column. ii. Modify the Template Name, Description, and Sharing Scope. iii. Click Save. |
| Use a template | i. Click Use Template in the Actions column. ii. After the configuration information loads, review all the settings. You can modify the instance parameters to meet your needs. iii. Follow the on-screen instructions to create the instance. |
| Delete a template | i. Click Delete in the Actions column. ii. In the dialog box, click OK. |
