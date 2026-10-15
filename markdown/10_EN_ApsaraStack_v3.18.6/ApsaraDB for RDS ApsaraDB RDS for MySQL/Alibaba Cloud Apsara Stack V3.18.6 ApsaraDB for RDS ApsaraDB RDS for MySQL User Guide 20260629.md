---
title: "ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 181
source_pdf: "2908166cb8bc81e5_Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93RDS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20RDS%20ApsaraDB%20RDS%20for%20MySQL%20User%20Guide%2020260629.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260629

## Table of Contents

- 1 What is ApsaraDB RDS?
- 2 Instance types
- 3 Log in to the ApsaraDB RDS console
- 4 Quick start
  - 4.1 Limits
  - 4.2 Procedure
  - 4.3 Create an instance
  - 4.4 Initialization settings
    - 4.4.1 Configure an IP address whitelist for an ApsaraDB RDS instance
    - 4.4.2 Create an account
    - 4.4.3 Create a database
  - 4.5 Connect to an ApsaraDB RDS for MySQL instance
- 5 Instances
  - 5.1 Create an instance
  - 5.2 View the details of an ApsaraDB RDS instance
  - 5.3 Restart an instance
  - 5.4 Change instance specifications
  - 5.5 Set a maintenance window
  - 5.6 Change the data replication mode
  - 5.7 Release an instance
  - 5.8 Update the minor engine version of an instance
  - 5.9 Configure instance parameters
  - 5.10 Read-only instances
    - 5.10.1 Overview of read-only instances
    - 5.10.2 Create a read-only instance
    - 5.10.3 View details of read-only instances
  - 5.11 Manage instances in the recycle bin
  - 5.12 Manage tags
- 6 Accounts
  - 6.1 Language Detection
  - 6.2 Package Audit
  - 6.3 Product Material Optimization Pro
  - 6.4 Modify the permissions of an account
  - 6.5 Product Material Optimization Lite
- 7 Category Match
  - 7.1 Category Attribute Match
  - 7.2 Delete a database
- 8 Size Chart Extraction
  - 8.1 Change the endpoint and port number of an instance
  - 8.2 Apply for and release an internal endpoint or a public endpoint for an instance
  - 8.3 Use DMS to log in to an ApsaraDB RDS instance
  - 8.4 Configure the hybrid access solution
  - 8.5 Change the network type of an instance
  - 8.6 Change the VPC and vSwitch for an instance
- 9 Database proxy
  - 9.1 Configure dedicated proxy
  - 9.2 Configure short-lived connection optimization
  - 9.3 Configure transaction splitting
  - 9.4 Read/write splitting
    - 9.4.1 Enable read/write splitting
    - 9.4.2 Configure read/write splitting
    - 9.4.3 Disable read/write splitting
- 10 Monitoring and alerts
  - 10.1 View resources and engine monitoring data
  - 10.2 Configure an alert rule
- 11 Cloud Monitor
  - 11.1 View performance metrics
  - 11.2 Alert history
  - 11.3 Alert rules
    - 11.3.1 Create an alert rule
    - 11.3.2 Manage alert rules
- 12 Data security
  - 12.1 Configure an IP address whitelist
  - 12.2 Configure SSL encryption
  - 12.3 Configure TDE
  - 12.4 SQL Audit
- 13 Service availability
  - 13.1 Switch workloads between primary and secondary ApsaraDB RDS instances
  - 13.2 Change the data replication mode
- 14 Database backup and restoration
  - 14.1 Configure automatic backup
  - 14.2 Manually back up an instance
  - 14.3 Download data backup files and log backup files
  - 14.4 Use the Upload Binlogs feature to upload binary log files
  - 14.5 Restore data to a new instance (formerly known as cloning an instance)
- 15 Autonomy services
  - 15.1 Introduction to DAS
  - 15.2 Perform quick diagnostics
  - 15.3 Manage sessions
  - 15.4 View real-time performance
  - 15.5 Storage analysis
  - 15.6 Lock analysis
  - 15.7 Performance trends
  - 15.8 View slow query logs
  - 15.9 Diagnostic reports
- 16 Log management
- 17 Use mysqldump to migrate MySQL data

## 1 What is ApsaraDB RDS?

ApsaraDB RDS is a stable, reliable, and scalable online database service. Based on the distributed file system and high-performance storage, ApsaraDB RDS provides a set of solutions for disaster recovery, backup, restoration, monitoring, and migration. ApsaraDB RDS supports four database engines, which are MySQL, SQL Server, PolarDB, and PostgreSQL. You can create RDS instances that run these engines to meet your business requirements.

**ApsaraDB RDS for MySQL**

ApsaraDB RDS for MySQL is developed based on AliSQL and provides excellent performance. ApsaraDB RDS for MySQL is a tried and tested solution that handled the high-volume concurrent traffic during Double 11. ApsaraDB RDS for MySQL supports deployment with mixed x86 and ARM clusters. It integrates basic features such as whitelist configuration, backup and restoration, Transparent Data Encryption (TDE), data migration, and management of instances, accounts, and databases. ApsaraDB RDS for MySQL also provides the following advanced features:
**Read-only instance:** In scenarios in which ApsaraDB RDS for MySQL handles a small
number of write requests but a large number of read requests, you can create read-only instances to scale up reading capabilities and increase the application throughput.
**Read/write splitting:** The read/write splitting feature provides a read/write splitting
endpoint. This endpoint enables automatic read/write splitting for a primary RDS instance and all of its read-only RDS instances. An application can connect to the read/write splitting endpoint to read and write data. Write requests are forwarded to the primary RDS instance while read requests are forwarded to read-only RDS instances based on their weights. To increase the reading capability of your database system, you need to only add more readonly RDS instances.
**High availability based on zone-disaster recovery**: RDS for MySQL instances that run
RDS High-availability Edition adopt an HA architecture that consists of a primary node and a secondary node deployed in two different zones within the same region, such as China (Shanghai) Zone A and China (Shanghai) Zone B. The primary node handles read and write requests. The secondary node synchronizes data from the primary node in real time and does not handle requests. When the zone in which the primary node is deployed becomes unavailable due to power outage or network issues, the secondary node is automatically promoted to the primary node within a period ranging from 30 seconds to 5 minutes. The time required for the failover depends on the fault detection and recovery mechanism.

## 2 Instance types

This topic describes the instance types of ApsaraDB RDS for MySQL. Different instance types deliver different performance.

**Instance type comparison**

| Instance type | Characteristics | Applicable scenarios |
|---|---|---|
| Dedicated | A dedicated cluster occupies all allocated compute resources such as CPUs. The cluster does not share compute resources with other instances that run on the same server. This improves the reliability and stability of the instance. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| General- purpose | Idle compute resources such as CPUs are shared among instances that run on the same server. Resource sharing allows you to deploy a large number of instances at low costs. | Scenarios in which cost-effectiveness is prioritized. |
| Dedicated host | The instances have exclusive access to all resources on a physical host, making it the highest-tier dedicated specification. | Scenarios in which maximum performance stability and isolation are required. Databases are used as core systems in sectors such as finance, e- commerce, public services, and large- and medium-sized Internet services. |

**IOPS**

The maximum IOPS of an ApsaraDB RDS for MySQL instance that uses local disks varies based on the instance type. The maximum IOPS of an ApsaraDB RDS for MySQL instance that uses cloud disks varies based on the instance type and storage capacity. The following formula can be used to calculate the IOPS of an ApsaraDB RDS for MySQL instance that uses cloud disks. The storage capacity is measured in GB.

```
min{1800 + 30 × Storage capacity, 25000}
```

**Note**

If the throughput of an ApsaraDB RDS for MySQL instance reaches the upper limit, the IOPS of the instance also decreases.

**Primary ApsaraDB RDS for MySQL instances**

**High-availability Edition**

| Instanc e family | Suppor ted version | Instance type | Number of CPU cores and memory capacity | Maxim um IOPS | Maxim um numb er of conne ctions | Storage capacity |
|---|---|---|---|---|---|---|
| General- purpose instance family | MySQL 5.7 and MySQL 8.0 | rds.mysql.t1.small | 1 core, 1 GB | 1,200 | 300 | 5 GB to 2,000 GB |
|   |   | rds.mysql.s1.small | 1 core, 2 GB | 2,000 | 600 |   |
|   |   | rds.mysql.s2.large | 2 cores, 4 GB | 4,000 | 1,200 |   |
|   |   | rds.mysql.s2.xlarge | 2 cores, 8 GB | 6,000 | 2,000 |   |
|   |   | rds.mysql.s3.large | 4 cores, 8 GB | 8,000 | 2,000 |   |
|   |   | rds.mysql.m1.medi um | 4 cores, 16 GB | 14,000 | 4,000 |   |
|   |   | rds.mysql.c1.large | 8 cores, 16 GB | 20,000 | 4,000 |   |
|   |   | rds.mysql.c1.xlarge | 8 cores, 32 GB | 28,000 | 8,000 |   |
|   |   | rds.mysql.g2.2xlarg e | 16 cores, 32 GB | 40,000 | 8,000 | 50 GB to 3,000 GB |
|   |   | rds.mysql.c2.xlarge | 16 cores, 64 GB | 40,000 | 16,000 | 5 GB to 3,000 GB |
|   |   | rds.mysql.c2.xlp2 | 16 cores, 96 GB | 40,000 | 24,000 |   |
|   | 5.7 | rds.mysql.c2.2xlarg e | 16 cores, 128 GB | 16,000 | 32,000 |   |

|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.g2.3xlarg e | 24 cores, 48 GB | 40,000 | 12,000 | 50 GB to 3,000 GB |
|---|---|---|---|---|---|---|
|   |   | rds.mysql.x2.3xlarg e | 24 cores, 48 GB | 50,000 | 12,000 | 50 GB to 2,000 GB |
|   |   | rds.mysql.g4.3xlarg e | 24 cores, 96 GB | 50,000 | 24,000 | 50 GB to 3,000 GB |
|   |   | rds.mysql.g2.4xlarg e | 32 cores, 64 GB | 60,000 | 16,000 |   |
|   |   | rds.mysql.g4.4xlarg e | 32 cores, 128 GB | 60,000 | 32,000 |   |
|   |   | rds.mysql.g2.8xlarg e | 64 cores, 128 GB | 60,000 | 32,000 |   |
|   | MySQL 5.7 and MySQL 8.0 | mysql.x8.medium.2 | 2 cores, 16 GB | 15,000 | 2,500 | 50 GB to 1,000 GB |
|   |   | mysql.x4.large.2 | 4 cores, 16 GB | 30,000 | 2,500 |   |
|   |   | mysql.x8.large.2 | 4 cores, 32 GB | 40,000 | 5,000 |   |
|   |   | mysql.x4.xlarge.2 | 8 cores, 32 GB | 45,000 | 5,000 | 500 GB to 3,000 GB |
| Dedicat ed instance family |   |   |   |   |   |   |
|   |   | mysql.x8.xlarge.2 | 8 cores, 64 GB | 50,000 | 10,000 |   |
|   |   | rds.mysql.x2.2xlarg e | 16 cores, 32 GB | 40,000 | 8,000 | 50 GB to 2,000 GB |
|   |   | mysql.x4.2xlarge.2 | 16 cores, 64 GB | 60,000 | 10,000 | 500 GB to 3,000 GB |
|   |   | mysql.x8.2xlarge.2 | 16 cores, 128 GB | 60,000 | 20,000 |   |
|   |   | rds.mysql.x4.3xlarg e | 24 cores, 96 GB | 50,000 | 24,000 | 50 GB to 2,000 GB |

|   |   | rds.mysql.x2.4xlarg e | 32 cores, 64 GB | 60,000 | 16,000 | 50 GB to 3,000 GB |
|---|---|---|---|---|---|---|
|   |   | mysql.x4.4xlarge.2 | 32 cores, 128 GB | 80,000 | 20,000 | 1,000 GB to 6,000 GB |
|   |   | rds.mysql.x4.4xlarg e | 32 cores, 128 GB | 60,000 | 32,000 | 50 GB to 3,000 GB |
|   |   | mysql.x8.4xlarge.2 | 32 cores, 256 GB | 100,000 | 40,000 | 1,000 GB to 6,000 GB |
|   |   | rds.mysql.x2.8xlarg e | 64 cores, 128 GB | 60,000 | 32,000 | 50 GB to 3,000 GB |
|   |   | mysql.x8.8xlarge.2 | 64 cores, 512 GB | 150,000 | 80,000 | 1,000 GB to 6,000 GB |
| Dedicat ed host instance family | 5.7 | rds.mysql.st.h43 | 60 cores, 470 GB | 150,000 | 100,00 0 | 1,000 GB to 6,000 GB |
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.st.v52 | 90 cores, 720 GB | 150,000 | 150,00 0 |   |

**Read-only instance**

| Instance family | Supporte d version | Instance type | Number of CPU cores and memory capacity | Maxim um numbe r of connec tions | Storage capacity |
|---|---|---|---|---|---|
|   |   | rds.mysql.t1.small | 1 core, 1 GB | 300 |   |
|   |   | rds.mysql.s1.small | 1 core, 2 GB | 600 |   |
|   |   | rds.mysql.s2.large | 2 cores, 4 GB | 1,200 |   |
|   |   | rds.mysql.s2.xlarge | 2 cores, 8 GB | 2,000 |   |

| General- purpose instance family | MySQL 5.7 and MySQL 8.0 |   |   |   | 5 GB to 2,000 GB |
|---|---|---|---|---|---|
|   |   | rds.mysql.s3.large | 4 cores, 8 GB | 2,000 |   |
|   |   | rds.mysql.m1.medium | 4 cores, 16 GB | 4,000 |   |
|   |   | rds.mysql.c1.large | 8 cores, 16 GB | 4,000 |   |
|   |   | rds.mysql.c1.xlarge | 8 cores, 32 GB | 8,000 |   |
|   |   | rds.mysql.c2.xlarge | 16 cores, 64 GB | 16,000 | 5 GB to 3,000 GB |
|   |   | rds.mysql.c2.xlp2 | 16 cores, 96 GB | 24,000 |   |
| Dedicated instance family | MySQL 5.7 and MySQL 8.0 | mysqlro.x8.medium.1 | 2 cores, 16 GB | 2,500 | 50 GB to 1,000 GB |
|   |   | mysqlro.x4.large.1 | 4 cores, 16 GB | 2,500 |   |
|   |   | mysqlro.x8.large.1 | 4 cores, 32 GB | 5,000 |   |
|   |   | mysqlro.x4.xlarge.1 | 8 cores, 32 GB | 5,000 |   |
|   |   | mysqlro.x8.xlarge.1 | 8 cores, 64 GB | 10,000 | 500 GB to 3,000 GB |
|   |   | mysqlro.x4.2xlarge.1 | 16 cores, 64 GB | 10,000 |   |
|   |   | mysqlro.x8.2xlarge.1 | 16 cores, 128 GB | 20,000 |   |
|   |   | mysqlro.x4.4xlarge.1 | 32 cores, 128 GB | 20,000 |   |
|   |   | mysqlro.x8.4xlarge.1 | 32 cores, 256 GB | 40,000 |   |
| 3 |   | > Document |   |   | Version: 2026062 |

|   |   |   |   |   | S for MySQL User G ide·Instance type |
|---|---|---|---|---|---|
|   |   |   |   |   | 1,000 GB to 6,000 GB |
|   |   | mysqlro.x8.8xlarge.1 | 64 cores, 512 GB | 80,000 |   |
| Dedicated host instance family | 5.7 | rds.mysql.st.h43 | 60 cores, 470 GB | 100,000 | 1,000 GB to 6,000 GB |
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.st.v52 | 90 cores, 720 GB | 150,000 |   |

console

## 3 Log in to the ApsaraDB RDS console

**console**

This topic describes how to log in to the ApsaraDB RDS console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. **Procedure**
console i. In the address bar of your browser, enter the service domain name for the Apsara Unimanager Management Console and press Enter.

**Note**

You can click the current language in the upper-right corner to switch to another language. ii. Enter your username and password.

**Note**

You can obtain the username and logon password from an operations administrator. If this is your first time logging on to the Apsara Uni-manager Management Console, you must change your password. For security, the password must be 10 to 32 characters long and contain uppercase letters, lowercase letters, digits, and special characters. The supported special characters are: !, @, #, $, and %. console iii. Select **I Have Read And Agree To The Product Service Agreement, Privacy**
**Agreement, And User Agreement**.

**Note**

The link text on the logon page is the title of the agreement document. You can click the link to view the details of the agreement. The **Product Service Agreement**, **Privacy Agreement**, and **User**
**Agreement** are displayed only if they have been published. If none of these
agreements are published, you can skip this step. iv. Click **Account Logon** or **Authorized Logon**.

**Note**

The Authorized Logon button is displayed only if the global IdP setting for third-party authentication is enabled. This display name can be customized. The default name is "Authorized Logon". v. If multi-factor authentication (MFA) is enabled for your account, follow the steps for one of the following scenarios:

**Note**

When you log on from the Internet, multi-factor authentication (MFA) is mandatory by default.

**First logon after MFA is enabled**

a. After you log on with your username and password, the Bind Virtual MFA Device page appears. b. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind a virtual MFA device. c. You have logged in to the console.

**MFA is already enabled and a device is bound**

Enter the six-digit MFA code and click **Authenticate**.
2. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**.

## 4 Quick start

### 4.1 Limits

To ensure instance stability and security, ApsaraDB RDS for MySQL has specific service limits, as listed in the following table.

| Item | Limits |
|---|---|
| Instance parameters | Instance parameters can be modified by using the ApsaraDB RDS console or API operations. Due to security and stability considerations, only specific parameters can be modified. |
| Root permissions of databases | The root or system administrator permissions are not provided. |
| Database backup | Logical backup can be performed by using the CLI or GUI. Physical backup can be performed only by using the ApsaraDB RDS console or API operations. |
| Database restoration | Logical restoration can be performed by using the CLI or GUI. Physical restoration can be performed only by using the ApsaraDB RDS console or API operations. |
| ApsaraDB RDS for MySQL storage engine | Only InnoDB is supported. To ensure performance and security, we recommend that you use the InnoDB storage engine. The TokuDB storage engine is not supported. Percona no longer provides support for TokuDB, which in extreme cases may lead to bugs that cannot be fixed and impact your workloads. The MyISAM storage engine is not supported Due to the inherent shortcomings of the MyISAM engine, data may be lost. Only specific existing instances use the MylSAM engine. MyISAM engine tables in newly created instances are automatically converted to InnoDB engine tables. The Memory engine is not supported. Newly created Memory tables are automatically converted into InnoDB tables. |
| Database replication | ApsaraDB RDS for MySQL provides a primary/secondary replication architecture. The secondary instances in this replication architecture are hidden and cannot be directly accessed. |
| Instance restart | Instances must be restarted by using the ApsaraDB RDS console or API operations. |
| Account and database management | ApsaraDB RDS for MySQL allows you to manage accounts and databases by using the ApsaraDB RDS console. ApsaraDB RDS for MySQL also allows you to create a privileged account to manage users, passwords, and databases. |
| Standard account | Authorization is not allowed. The ApsaraDB RDS console allows you to manage accounts and databases. Instances that support standard accounts also support privileged accounts. |

| Privileged account | Authorization is allowed on standard accounts. The privileged account cannot be reverted to a standard account. |
|---|---|

### 4.2 Procedure

ApsaraDB RDS quick start covers the following topics: creating an ApsaraDB RDS instance, configuring an IP address whitelist, creating a database, creating an account, and connecting to the instance. This topic describes how to use ApsaraDB RDS and provides all the necessary information to create an ApsaraDB RDS instance. ApsaraDB RDS for MySQL is used in the example. Typically, after an instance is created, you must perform several operations to make the instance ready for use, as shown in Quick start flowchart. Figure 1. Quick start flowchart An instance is a virtual database server on which you can create and manage multiple databases. After you create an RDS instance, you must configure IP address whitelists for the RDS instance to allow access from external devices. Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your RDS instance, the workloads on the instance are not affected. Category Attribute Match and Language Detection Before you use a database, you must create the database and an account on the ApsaraDB RDS instance. After you create an ApsaraDB RDS instance, configure an IP address whitelist, and create a database and an account, you can connect to the instance by using a database client.

### 4.3 Create an instance

This topic describes how to create one or more instances in the ApsaraDB RDS console.

**Prerequisites**

An Apsara Stack tenant account is created.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, click **Create Instance** in the upper-right corner.
3. Select an option from the **Service Catalog** drop-down list and click **OK**.
4. Configure the parameters described in the following table.

| Section | Paramete r | Configuration |
|---|---|---|
| Basic Configura tions | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
| Area | Region | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|   | Primary Node Zone | The zone in which the primary instance is deployed. Note To deploy a multi-zone instance or an Enterprise Edition instance, select a zone whose name contains MAZ . |
|   | Deployme nt Method | Specifies whether to deploy the primary and secondary instances in separate zones. ApsaraDB RDS supports Multi-zone Deployment and Single-zone Deployment. A deployment method is automatically selected based on the value of Primary Node Zone. |
|   | Database Engine | The database engine of the instance. Select MySQL. |

| saraDB RDS fo e·Quick start | r MySQL User G ApsaraDB for RD |   |
|---|---|---|
| Specificat ions |   |   |
|   | Chip Architect ure | The chip architecture of the host on which the instance is deployed. Note If you do not have permissions to select an option, contact the operations administrator to grant the permissions to your account. |
|   | Engine Version | The version of the database engine. Valid values: 8.0 5.7 5.6 Note To deploy an Enterprise Edition instance, select 5.7. |
|   | Edition | The edition of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. Note To deploy an Enterprise Edition instance, select Enterprise Edition. |
|   | Storage Type | The storage type of the instance. Select Local SSD. |
|   | Instance Specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the new RDS instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| Network | Connectio n Type | The connection type of the instance. Valid values: Internet: Instances of this connection type can be connected over the Internet. Internal Network: Instances of this connection type can be connected over an internal network. Note After the instance is created, the value of this parameter cannot be changed. Proceed with caution. |
|   | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Note Instances that use standard SSDs cannot be deployed in the classic network. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. |

|   | VPC | The VPC in which you want to create the instance. Note When Network Type is set to VPC, you must specify this parameter. |
|---|---|---|
|   | vSwitch Zone | The zone in which the vSwitch is located. If you setP rimary Node Zone to a zone whose name contains MAZ, you must specify the zone in which the vSwitch that you want to use is located. Note This parameter is available only when Network Type is set to VPC. |
|   | vSwitch | The vSwitch to which the instance is connected. Note When Network Type is set to VPC, you must specify this parameter. |
|   | IP Whitelist | The IP address or CIDR block that is allowed to connect to the instance. |
| Instance Settings | Quantity | The number of instances that you want to create. Default value: 1. |
|   | Instance Name | The name of the instance. It must be 2 to 64 characters in length. It must start with a letter. It can contain letters, digits, hyphens (-), underscores ( ), and _ colons (:). The name cannot start with http:// or https://. |

5. Click **Submit**.

### 4.4 Initialization settings

#### 4.4.1 Configure an IP address whitelist for an ApsaraDB RDS instance

**ApsaraDB RDS instance**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are used for database access to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your RDS instance, the workloads on the instance are not affected. To configure a whitelist, you can perform the following operations: Configure an IP address whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance. Configure an Elastic Compute Service (ECS) security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Usage notes**

The default IP address whitelist can be modified or cleared, but cannot be deleted. You can add up to 1,000 IP addresses or CIDR blocks to a whitelist. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 192.168.1.0/24.

**Configure a standard IP address whitelist**

1. Log on to the ApsaraDB for RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Security Controls**.
4. On the **Whitelist Settings** tab, click **Edit** corresponding to an IP address whitelist.

**Note**

If you want to connect an ECS instance to an ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type. Otherwise, the connection fails. You can also click **Create Whitelist** to create an IP address whitelist.
5. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that you want to
allow to access your RDS instance and click **OK**. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.xx format can access your RDS instance. If you enter more than one IP address or CIDR block, separate them with commas (,). Do not add spaces preceding or following the commas. Example:

```
 192.168.0.1,172.16.213.9 .
```

If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

**Note**

If you add a new IP address or CIDR block to the **default** whitelist, the default address 127.0.0.1 is deleted.

#### 4.4.2 Create an account

Detect the language of the input text. Supports automatic recognition of 23 languages. Best suited to short text such as search queries, product titles, and chat messages. Synchronous.

**Endpoint**

```
POST /ai/text/marco/language-detection
```

**Use cases**

Cross-border search -- detect the buyer's search-query language and route to the matching index. Title preprocessing -- detect source language automatically before calling the Text Translation API, so callers do not need to pass `SourceLanguage` . Chat routing -- forward users to native-language agents based on detected language.

**Quick start**

```java
import json data = json.dumps({ "SourceText": "Hello world" }) result = make_signed_request("/ai/text/marco/language-detection", data) print(result["Data"]["DetectedLanguage"]) # en
```

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceText | String | Yes | Text to identify. Up to ~1024 characters recommended; very short inputs (single tokens) have lower accuracy. |

**Response fields**

| Field | Type | Description |
|---|---|---|
| Code | String | Business status. Success when OK; otherwise see Error codes. |
| Message | String | Business message. |
| RequestId | String | Unique request identifier. |
| Success | Boolean | Whether the call succeeded. |
| Data.DetectedLanguage | String | Detected language code; see "Supported languages" below. |
| Data.UsageMap.RequestCount | Number | Request count for billing reconciliation. |

|   | Data.UsageMap.RequestCount |   |
|---|---|---|

**Response example**

`{`

```json
  "Code": "Success",
  "Message": "ok",
  "RequestId": "21570000-0000-0000-0000-000000000001",
  "Success": true,
  "Data": {
    "DetectedLanguage": "en",
    "UsageMap": { "RequestCount": 1 }
```

`}` `}`

**Supported languages (23)**

| ngali ( bn ), German ( de he ), Indonesian ( id ), It tch ( nl ), Polish ( pl ), Po krainian ( uk ), Urdu ( ur Traditional ( zh-tw ). |   | de |   |
|---|---|---|---|
|   | id |   |   |
|   |   |   | ), It ), Po |
|   | pl |   |   |

|   | es |
|---|---|
| ja |   |

( `fr` ), Hebrew ( `he` ), Indonesian ( `id` ), Italian ( `it` ), Japanese ( `ja` ), Korean ( `ko` ),

| ms |   | ), |
|---|---|---|
| ( |   |   |

Malay ( `ms` ), Dutch ( `nl` ), Polish ( `pl` ), Portuguese ( `pt` ), Russian ( `ru` ), Thai ( `th` ),

**Error codes**

Common error codes: `InvalidParameter` (missing or empty `SourceText` ), `InternalError` (system busy). See Error codes for the full reference.

**What's next**

Text Translation API -- translate plain text. Text Correction API -- spelling correction.

#### 4.4.3 Create a database

Multimodal-LLM-based cross-platform category-attribute filling. Given source-platform product info (title, source category, description, SKU, attributes, up to 10 images), match the precise target-platform category and fill every required attribute, with a per-attribute confidence and rationale. Synchronous.

**Endpoint**

```
POST /ai/material/category/attribute
```

**Use cases**

1688 → TEMU cross-platform listing where platform categories differ significantly and have complex hierarchical relations (material → wood species → density). Top sellers' bulk publishing, ERP / SaaS integrations, fast SMB single-item listing.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category path. |

| A | psaraDB for RDS |   | Apsara | DB RDS for MySQL User G uide·Quick star | t |
|---|---|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductDescription | String | No | Product description. |
| SkuInfo | Object[] | No | SKU list (spec + price per item). |
| ProductAttributes | Object | No | Source-platform attribute key-value pairs. |
| ImageUrls | String[] | No | Up to 10 image URLs. The multimodal model infers attributes from images. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Matched precise category path on the target platform. |
| Data.Attributes | Object[] | Filled attributes. Each item has Name , Value , Confidence (0-100), Reason , and SourceMatched (whether the value reused a source- platform attribute). |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Fans > USB Fans",
    "Attributes": [
      { "Name": "Battery Type", "Value": "Lithium-Ion", "Confidence": 92, "Reason": "Ti
tle and image both indicate rechargeable", "SourceMatched": false },
      { "Name": "Connectivity",  "Value": "USB Type-C",  "Confidence": 88, "Reason": "P
ort visible in image", "SourceMatched": true }
```

`]` `}` `}`

**Error codes**

See Error codes.

**What's next**

Category Match API -- category match alone.

### 4.5 Connect to an ApsaraDB RDS for MySQL instance

**for MySQL instance**

After you complete the initial configuration of your ApsaraDB RDS for MySQL instance, you can connect to it from an Elastic Compute Service (ECS) instance or an on-premises client.

**Background information**

After you Create an instance, Configure an IP address whitelist, and Language Detection, you can connect to the ApsaraDB RDS for MySQL instance by using a database client or by configuring the endpoint, port, and account information in your application. If you need to connect an ECS instance to an ApsaraDB RDS instance, you must make sure that both instances are in the classic network or in the same virtual private cloud (VPC), and the IP address of the ECS instance is added to an IP address whitelist of the ApsaraDB RDS instance.

**Connect to an instance from a client**

ApsaraDB RDS for MySQL is fully compatible with open source MySQL. You can connect to an ApsaraDB RDS instance from a database client by using a method similar to the method that is used to connect to an open source MySQL database. In the following example, the HeidiSQL client is used.
1. Start the HeidiSQL client.
2. In the lower-left corner of the Session manager dialog box, click **New**.
3. Enter information about the ApsaraDB RDS instance to which you want to connect. The
following table describes the required parameters.

| Paramet er | Description |
|---|---|
| Networ k type | Select the network type of the ApsaraDB RDS instance to which you want to connect. For example, select MariaDB or MySQL (TCP/IP). |
| Hostna me / IP | Enter the internal or public endpoint of the ApsaraDB RDS instance. If your client is deployed on an ECS instance that is in the same region and has the same network type as the ApsaraDB RDS instance, use the internal endpoint. For example, if the ECS and ApsaraDB RDS instances are both in a VPC located in the China (Hangzhou) region, you can use the internal endpoint of the ApsaraDB RDS instance to create a secure connection. In other scenarios, use the public endpoint. To view the internal and public endpoints and port numbers of the ApsaraDB RDS instance, perform the following operations: i. Log in to the ApsaraDB RDS console. ii. Find the ApsaraDB RDS instance to which you want to connect and click its ID. iii. In the Basic Information section, view the internal and public endpoints and port numbers of the instance. |
| User | Enter the name of the account used to connect to the ApsaraDB RDS instance. |
| Passwor d | Enter the password of the account used to connect to the ApsaraDB RDS instance. |

| Port | If you connect to the instance over an internal network, enter the internal port number of the instance. If you connect to the instance over the Internet, enter the public port number of the instance. |
|---|---|

4. Click **Open**. If the connection information is correct, you can connect to the instance.

## 5 Instances

### 5.1 Create an instance

This topic describes how to create one or more instances in the ApsaraDB RDS console.

**Prerequisites**

You must have an account that can be used to log on to the Alibaba Cloud Management Console.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the navigation pane on the left, click **Instance List**, and then click **Create Instance**.
3. Configure the parameters described in the following table.

| Category | Configura tion | Description |
|---|---|---|
| Basic Configura tions | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource group to which the instance belongs. |
| Area | Region | The region where the instance is located. Products in different regions cannot communicate with each other over the internal network. You cannot change the region after the instance is created. |
|   | Deploym ent Method | ApsaraDB RDS supports Multi-zone Deployment and Single-zone Deployment. You can select the zones for the primary and secondary nodes as needed. |
|   | Primary Node Zone | The zone where the primary node of the instance is located. |
|   | Secondar y Node Zone | The zone where the secondary node of the instance is located. This parameter is available only when you select Multi-zone Deployment. |
|   | Database Engine | The type of the database. Select MySQL. |

| saraDB RDS fo e·Instances |   |   |
|---|---|---|
| Specificat ions |   |   |
|   | Chip Architect ure | Select the chip architecture of the host for the RDS instance. Note If an authorization error message appears when you select this configuration, contact the administrator to grant permissions to the account. |
|   | Database Version | The version of the database. The following versions are supported: 8.0 5.7 |
|   | Edition | The edition of the database. For more information, see theI nstance Types section in ApsaraDB RDS Product Introduction. |
|   | Storage Type | The storage type of the database. Select local SSDs. |
|   | Instance Specificat ions | The type of the instance. Different memory sizes correspond to different maximum connections and input/output operations per second (IOPS). The actual values in the console prevail. For more information, see the Instance Types section in ApsaraDB RDS Product Introduction. Click AI-powered Instance Type Recommender and enter your scenario in Apsara AI Assistant to receive recommendations for the optimal instance type that balances cost and performance. |
|   | Storage Capacity | The storage space includes space for data, system files, binary logging (binlog) files, and transaction files. For more information, see the Instance Types section in ApsaraDB RDS Product Introduction. |
|   | Connecti on Type | ApsaraDB RDS provides the following two types of endpoints: Public Endpoint: You can use this endpoint to access the database from the internet. Internal Endpoint: You can use this endpoint to access the database from the internal network. Note You cannot change this setting after the instance is created. Select the type with caution. |

|   | Network Type | The network types supported by the RDS instance: Classic Network: Alibaba Cloud services in a classic network are not isolated from each other. You can only use security groups or whitelists of the services to block unauthorized access. Note Cloud disk instances do not support this network type. Virtual Private Cloud: A virtual private cloud (VPC) is an isolated network environment on Alibaba Cloud. In a VPC, you can define a custom route table, IP address range, and gateway. For better security, select a VPC. |
|---|---|---|
| Network |   |   |
|   | VPC | Select your VPC. Note This parameter is required when you set Network Type to VPC. |
|   | vSwitch Zone | The zone where the vSwitch is located. Note This parameter is visible only when you set Network Type to VPC. You do not need to set this parameter in other scenarios. |
|   | VSwitch | Select a vSwitch in the VPC. Note This parameter is required when you set Network Type to VPC. |
|   | IP Whitelist | Add IP addresses to the whitelist to allow access to the RDS instance. |
| Instance Settings | Quantity | ApsaraDB RDS supports creating instances in batches. You can specify the number of RDS instances to create. The default value is 1. |
|   | Instance Name | The name of the RDS instance. The name must be 2 to 64 characters in length. It must start with a letter or a Chinese character. It can contain digits, hyphens (-), underscores ( ), and colons (:). _ It cannot start with http:// or https://. |

4. Click **Submit**.

### 5.2 View the details of an ApsaraDB RDS instance

**ApsaraDB RDS instance**

This topic describes how to view the details of an ApsaraDB RDS instance, such as its basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. Use one of the following methods to go to the **Basic Information** page of an RDS instance:
On the **Instances** page, click the ID of the instance to go to the **Basic Information** page. On the **Instances** page, click **Manage** in the **Actions** column of the instance to go to the
**Basic Information** page.

**References**

For more information about the mappings between MySQL versions of ApsaraDB RDS for MySQL and the MySQL community, see Release notes for AliSQL.

### 5.3 Restart an instance

This topic describes how to manually restart an ApsaraDB RDS instance. This applies if the number of connections exceeds the specified threshold or if the instance has performance issues.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page that appears, click **Restart Instance**.

**Note**

When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.
4. In the message that appears, click **OK**.

### 5.4 Change instance specifications

**specifications**

If the specifications of an ApsaraDB RDS for MySQL instance cannot meet your business requirements, you can change the instance specifications. This topic describes how to change the specifications, such as the instance type and storage capacity.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane of the **ApsaraDB RDS** console, click **Instances**. On the
page that appears, click the ID of the instance that you want to manage or click **Manage** in the **Actions** column of the instance to go to the **Basic Information** page.
3. In the upper-right corner of the **Configuration Information** section, click **Change**
**Specifications**.
4. On the **Change Specifications** page, configure the **Edition**, **Storage Type**, **Instance**
**Type**, **Storage Capacity**, and **Switching Time** parameters.

**Note**

If you set the **Switching Time** parameter to **Specified Time**, you must specify a point in time for the change.
5. Click **Submit**.
6. Confirm the changes and click **OK**.

### 5.5 Set a maintenance window

This topic describes how to set a maintenance window for an ApsaraDB RDS instance.

**Background information**

To ensure the stability of ApsaraDB RDS instances, the backend system performs maintenance on the instances at irregular intervals. The default maintenance window is from 02:00 to 06:00. You can set the maintenance window to off-peak hours based on your business to avoid impact on business.

**Usage notes**

To ensure stability of the maintenance process, the instance changes to the **Maintaining** state before the maintenance window. When the instance is in this state, access to data in the database and query operations such as performance monitoring are not affected. However, except for account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. During the maintenance window, connections to the instance may be temporarily interrupted once or twice. Make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the **Configuration Information** section, click **Settings** to the right of the
**Maintenance Window** parameter.
4. Select a maintenance window and click **Yes**.

**Note**

The maintenance window is displayed in UTC+8.

### 5.6 Change the data replication mode

**mode**

You can set the data replication mode between primary and secondary ApsaraDB RDS instances to improve database availability.

**Background information**

ApsaraDB RDS supports the following data replication modes: Semi-synchronous mode After an application-initiated update is complete on the primary instance, logs are synchronized to all the secondary instances. The transaction is considered committed when at least one secondary instance has received the logs, regardless of whether the secondary instance has completed executing the updates recorded in the logs. If the secondary instances are unavailable or a network interruption occurs between the primary and secondary instances, the semi-synchronous mode is demoted to the asynchronous mode. Asynchronous mode When your application initiates a request to add, delete, or modify data, the primary instance responds to your application immediately after it completes the requested operation. At the same time, the primary instance asynchronously replicates data to the secondary instances. During asynchronous data replication, the unavailability of secondary instances does not affect the operations on the primary instance. Data remains consistent even if the primary instance is unavailable.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Service Availability**.
4. In the upper-right corner of the **Instance Availability** section, click **Change Data**
**Replication Mode**.
5. In the dialog box that appears, select a data replication mode and click **OK**.

### 5.7 Release an instance

This topic describes how to manually release an instance.

**Usage notes**

Only instances in the Running state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click **Release an instance** in the **Operation** column.
3. In the dialog box that appears, click **Release**.

### 5.8 Update the minor engine version of an instance

**version of an instance**

ApsaraDB RDS for MySQL supports both automatic updates and manual updates to the minor engine version of an ApsaraDB RDS for MySQL instance. These updates improve performance, introduce new features, or fix known issues.

**Description**

By default, the minor engine version of your ApsaraDB RDS for MySQL instance is manually updated. You can log in to the ApsaraDB RDS console, go to the **Basic Information** page of your ApsaraDB RDS for MySQL instance, and then view the settings of **Automated Update**
**of Minor Engine Version** in the Configuration Information section.
**Automatic Upgrade**: Each time you log in to the ApsaraDB RDS console and view the
basic information about your ApsaraDB RDS instance, the system queries the minor engine version of the ApsaraDB RDS instance. When a new minor engine version is released, the system automatically updates the minor engine version of your ApsaraDB RDS instance during the specified maintenance window. For more information, see Set a maintenance window.
**Manual Upgrade**: Each time you log in to the ApsaraDB RDS console and view the basic
information about your ApsaraDB RDS instance, the system queries the minor engine version of the ApsaraDB RDS instance. When a new minor engine version is released, the system does not automatically update the minor engine version of your ApsaraDB RDS instance. You can manually update the minor engine version on the **Basic Information** page. For more information, see Manually update the minor engine version.

**Usage notes**

When you update the minor engine version of your ApsaraDB RDS instance, a transient disconnection that lasts approximately 30 seconds may occur. We recommend that you update the minor engine version during off-peak hours or make sure that your application is configured to automatically reconnect to the ApsaraDB RDS instance. After you update the minor engine version of your ApsaraDB RDS instance, you cannot roll the minor engine version of the ApsaraDB RDS instance back to the previous version. After you upgrade the specifications of your ApsaraDB RDS instance, the system updates the ApsaraDB RDS instance to the latest minor engine version.

**Change the settings for Automated Update of Minor Engine**

**Version**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the **Configuration Information** section of the Basic Information page, click **Settings** to
the right of **Automated Update of Minor Engine Version**.
4. In the dialog box that appears, select **Manual Upgrade** and click **OK**.

**Manually update the minor version**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the **Configuration Information** section of the page, click **Update Minor Engine**
**Version**.

**Note**

The **Upgrade Minor Engine Version** button is displayed only when a new minor engine version is available.
4. In the dialog box that appears, specify the Update Time parameter and click **OK**.

**FAQ**

**I updated the minor engine version of my ApsaraDB RDS instance but the MySQL**

**version remains unchanged. Why?**

The minor engine version that you updated is the minor engine version of ApsaraDB RDS, but not the MySQL version. To view the minor engine version, you must run the `show variables` like '%rds_release_date%' command.

### 5.9 Configure instance parameters

**parameters**

This topic describes how to view and modify the values of some instance parameters and query the parameter modification records in the ApsaraDB RDS console.

**Usage notes**

**Limits on modifiable parameters**: To ensure instance stability, you can modify only
some parameters in the ApsaraDB RDS console.
**Value range**: When you modify a parameter, refer to the values specified in the **Value**
**Range** column on the **Modifiable Parameters** tab in the ApsaraDB RDS console.
**Restart impact**: The modification of some parameters takes effect only after you restart
your ApsaraDB RDS instance. You can check the values in the **Force Restart** column on the **Modifiable Parameters** tab in the ApsaraDB RDS console to identify the parameters. To avoid service interruptions, we recommend that you perform this operation during offpeak hours and ensure that your application is configured to automatically reconnect to the instance.
**Effective period selection**: You must specify an effective period for the parameters
before you submit them. Valid values: Take Effect Immediately, Take Effect Within the Maintenance Window 02:00-06:00, and Take Effect at Specified Time. For the parameters that do not require the instance to be restarted, if you select a value of effective period other than Take Effect Immediately for these parameters, you need to check the business status before the specified time. For the parameters that require the instance to be restarted, the system will apply the parameters based on the restart policy. In this case, be sure to evaluate the impact on your business.

**Modify the values of parameters**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Parameters**.
4. Perform the following operations:

**Export parameters**

On the Modifiable Parameters tab, click **Export Parameters**. The parameter settings of the instance are exported as a TXT file to your computer.

**Modify and import the parameters**

i. After you modify the exported parameter file, click **Import Parameters** and paste the content of the parameter file into the dialog box. ii. Click **OK**. iii. In the upper-right corner of the page, click **Apply Changes**. iv. In the dialog box that appears, specify an effective period for the parameters to take effect and click **OK**. You can select one of the following methods for the parameters to take effect:
**Take Effect Immediately**: The parameters are applied and take effect immediately
after they are modified.
**Take Effect Within the Maintenance Window 02:00-06:00** : The parameters
automatically take effect within the maintenance window (02:00-06:00).
**Take Effect at Specified Time**: The parameters take effect at the user-defined point
of time.

**Note**

If the modified parameter requires an instance restart to take effect, the system prompts you to confirm the restart. Perform this operation during offpeak hours and ensure that your application is configured to automatically reconnect to the instance. If you have not applied the parameter modification, you can click **Cancel**
**Changes** to undo the modification.

**Modify a single parameter.**

i. On the **Modifiable Parameters** tab, find the parameter that you want to modify and click the icon in the **Running Value** column. ii. Enter a value based on the value range and click **OK**. iii. In the upper-right corner of the page, click **Apply Changes**. iv. In the dialog box that appears, specify an effective period for the parameters to take effect and click **OK**. You can select one of the following methods for the parameters to take effect:
**Take Effect Immediately**: The parameters are applied and take effect immediately
after they are modified.
**Take Effect Within the Maintenance Window 02:00-06:00** : The parameters
automatically take effect within the maintenance window (02:00-06:00).
**Take Effect at Specified Time**: The parameters take effect at the user-defined point
of time.

**Note**

If the modified parameter requires an instance restart to take effect, the system prompts you to confirm the restart. Perform this operation during offpeak hours and ensure that your application is configured to automatically reconnect to the instance. If you have not applied the parameter modification, you can click **Cancel**
**Changes** to undo the modification.

**View parameter modification history**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Parameters**. On the Parameters page, click the **Edit**
**History** tab.
4. Select a time range and click **OK** to query the parameter modification records within the
specified time range.

**Appendix 1: Parameters whose values will be synchronized to**

**read-only instances when they are modified**

When you modify the following parameters of a primary ApsaraDB RDS for MySQL instance, the changes are automatically synchronized to all of its read-only instances if they have the same parameters: lower_case_table_names

**Note**

This parameter cannot be modified for ApsaraDB RDS for MySQL 8.0 instances. innodb_large_prefix loose_validate_password_length default_time_zone rpl_semi_sync_slave_enabled

**Note**

Modifications to other parameters on the primary instance are not automatically synchronized to read-only instances. You must manually modify these parameters on each read-only instance.

**Appendix 2: List of available parameters**

| Parameter | Maj or engi ne vers ion | Def ault valu e | Value range |   | Res tart req uire d | Parameter description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| auto increment i _ _ ncrement | MyS QL 8.0 and MyS QL 5.7 | 1 | [1-65535] |   | No | The increment value of an auto- increment column. |   |   |   |   |
| auto increment o _ _ ffset | MyS QL 8.0 and MyS QL 5.7 | 1 | [1-65535] |   | No | The offset that is applied on an auto- increment column when auto-increment- increment is set to a value other than 1. |   |   |   |   |
| autocommit | 5.7 | ON | [ON\|OFF] |   | No | The autocommit mode. If you set this parameter to ON, all changes to a table immediately take effect. If you set this parameter to OFF, you must use COMMIT to accept a transaction or use ROLLBACK to cancel a transaction. If you set this parameter to OFF and then change the value to ON, MySQL automatically commits all open transactions. Note If you use the autocommit mode, you cannot manually commit transactions. If you want to manually commit transactions, you must use the SET autocommit = OFF; setting to disable the autocommit mode. |   |   |   |   |
|   |   |   |   |   |   |   |   | SET autocommit = |   |   |
|   |   |   |   |   |   |   | OFF; |   |   |   |

| automatic sp pri _ _ vileges | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | If the default value ON is used for this parameter, the server automatically grants the EXECUTE and ALTER ROUTINE permissions to the user who creates a stored procedure when the user cannot execute, alter, or delete the stored procedure. The ALTER ROUTINE permission is required to delete a stored procedure. When the stored procedure is deleted, the server automatically revokes the permissions from the user. If you set this parameter to OFF, the server does not automatically grant or revoke the permissions. |
|---|---|---|---|---|---|
| avoid temporal u _ _ pgrade | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether the ALTER TABLE statement can be executed to implicitly upgrade temporal columns of the types that are supported in versions earlier than MySQL 5.6.4. The temporal columns indicate TIMESTAMP columns that do not support fractional seconds, TIME columns, and DATETIME columns. Upgrading the columns creates tables. This disables fast alterations on the columns. |
| back log _ | MyS QL 8.0 and MyS QL 5.7 | 300 0 | [0-65535] | Yes | The number of outstanding connection requests that are allowed in MySQL. |
| binlog cache size _ _ | MyS QL 8.0 and MyS QL 5.7 | 209 715 2 | [4096- 16777216] | No | The size of the cache for transactions that are used to update binary logs. |
| binlog checksum _ | MyS QL 8.0 and MyS QL 5.7 | CRC 32 | [CRC32\|NO NE] | Yes | The type of BINLOG CHECKSUM ALG. _ _ Binary logs include the checksum for log events. Valid values: NONE and CRC32. Default value: CRC32. |

| binlog order com _ _ mits | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | If you enable this parameter for the replication source server, transactions are committed in the same order as they are written to the binary log. By default, this parameter is enabled for the replication source server. If this parameter is disabled, transactions can be committed in parallel. In some cases, disabling this parameter may improve performance. |
|---|---|---|---|---|---|
| binlog row imag _ _ e | MyS QL 8.0 and MyS QL 5.7 | full | [full\|minim al\|noblob] | No | Specifies the data recording granularity of row-formatted binary logs to balance storage overheads with data integrity. You need to consider the parsing capabilities of downstream subscription tools and the requirements for historical data backtracking when you select this parameter. Valid values: full: The system records the pre-image and post-image of all columns to ensure data integrity and high compatibility. This is the default value. minimal: The system records only the primary key (pre-image) and changed column (post-image), which significantly reduces the log volume and I/O load. This value is suitable for high-concurrency wide table scenarios where a primary key is available. noblob: The system automatically omits unchanged large non-primary key fields, such as BLOB and TEXT fields, based on the full settings. This value is suitable for scenarios that contain large objects but have infrequent updates. |
| binlog rows quer _ _ y log events _ _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | This parameter affects only row-based logging. If you enable this parameter, the MySQL server writes informational log events, such as row query log events, into its binary log. The informational log events can be used for debugging and related purposes. For example, if you cannot reconstruct a primary query from row updates, you can use the informational log events to obtain the original query issued on the primary query. |

| binlog stmt cach _ _ e size _ | MyS QL 8.0 and MyS QL 5.7 | 327 68 | [4096- 16777216] | No | The size of the cache for non- transactional statements that are used to update the binary log. |
|---|---|---|---|---|---|
| block encryption _ mode _ | MyS QL 8.0 and MyS QL 5.7 | "aes - 128- ecb" | ["aes-128- ecb"\|"aes- 192- ecb"\|"aes- 256- ecb"\|"aes- 128- cbc"\|"aes- 192- cbc"\|"aes- 256-cbc"] | No | The block encryption mode for block- based algorithms such as AES. It affects the behaviors of AES ENCRYPT() and _ AES DECRYPT(). _ |
| bulk insert buffe _ _ r size _ | MyS QL 8.0 and MyS QL 5.7 | 419 430 4 | [0- 42949672 95] | No | MyISAM uses a special tree-like cache to accelerate the execution of statements that are used to insert a large number of data records to non-empty tables at a time, such as INSERT ... SELECT, INSERT ... VALUES (...), (...), ..., and LOAD DATA INFILE. This parameter limits the size of the cache tree per thread. Unit: bytes. If you set this parameter to 0, the special tree-like cache is not used to accelerate the insert operations. Default value: 8 MB. |

| character set file _ _ system | MyS QL 8.0 and MyS QL 5.7 | bina ry | [utf8\|latin1 \|gbk\|binary ] | No | The character set of the file system. This parameter is used to interpret string literals that reference file names, such as the LOAD DATA INFILE and SELECT ... INTO OUTFILE statements and the LOAD FILE() function. The file names are _ converted from character set client to _ _ character set filesystem before the file _ _ opening attempt occurs. Default value: binary, which specifies that no conversion occurs. For systems on which multi-byte file names are allowed, we recommend that you set this parameter to a value other than binary. For example, if the system uses UTF-8 to represent file names, you need to set character set filesystem to 'utf8'. _ _ |
|---|---|---|---|---|---|
| character set ser _ _ ver | MyS QL 8.0 and MyS QL 5.7 | utf8 | [utf8\|latin1 \|gbk\|gb18 030\|utf8m b4] | Yes | The default character set of the server. |
| collation server _ | 8.0 | utf8 gen _ eral ci _ | [utf8 gene _ ral ci\|utf8 _ mb4 0900 _ ai ci\|utf8 _ _ mb4 gener _ al ci] _ | Yes | Specifies the collation of the character set. Exercise caution when you modify this parameter. If this parameter is incompatible with the character set server parameter, the _ _ instance cannot be started. |
| concurrent insert _ | MyS QL 8.0 and MyS QL 5.7 | 1 | [0\|1\|2] | No | 0: disables concurrent inserts. 1: enables concurrent inserts for MyISAM tables that have no holes. This is the default value. 2: enables concurrent inserts for all MyISAM tables even if the tables have holes. If a table that has a hole is being used by another thread, new rows are inserted at the end of the table. Otherwise, MySQL acquires a normal write lock and inserts rows into the hole. |

| connect timeout _ | MyS QL 8.0 and MyS QL 5.7 | 10 | [1-3600] | No | The period of time that the MySQL server waits for a CONNECT packet before it responds to a bad handshake. Unit: seconds. For MySQL 5.1.23 or earlier, the default value is 5 seconds. For versions later than MySQL 5.1.23, the default value is 10 seconds. If your client frequently encounters errors such as "Lost connection to MySQL server at 'XXX', system error: errno", you can increase the value of connect timeout. _ |
|---|---|---|---|---|---|
| default storage e _ _ ngine | MyS QL 8.0 and MyS QL 5.7 | Inno DB | [InnoDB\|in nodb] | Yes | The default storage engine of the new table. |
| default time zon _ _ e | MyS QL 8.0 and MyS QL 5.7 | SYS TEM | [SYSTEM\|- 12:00\|- 11:00\|- 10:00\|- 9:00\|- 8:00\|- 7:00\|- 6:00\|- 5:00\|- 4:00\|- 3:00\|- 2:00\|- 1:00\|\+0:0 0\|\+1:00\|\ +2:00\|\+3: 00\|\+4:00\| \+5:00\|\+5 :30\|\+5:45 \|\+6:00\|\+ 6:30\|\+7:0 0\|\+8:00\|\ +9:00\|\+1 0:00\|\+11: 00\|\+12:00 \|\+13:00] | Yes | The default time zone of the database. |
| default week for _ _ mat | MyS QL 8.0 and MyS QL 5.7 | 0 | [0-7] | No | The default mode value to use the WEEK() function. |

| delay key write _ _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF\|A LL] | No | This parameter applies only to MyISAM tables. This parameter affects the handling of the DELAY KEY WRITE table _ _ option that can be used in CREATE TABLE statements. Valid values: OFF: The DELAY KEY WRITE table option _ _ is ignored. ON: You can specify any DELAY KEY WRITE option for the _ _ CREATE TABLE statement in MySQL. This is the default value. ALL: The system processes all newly opened tables as tables that are created with the DELAY KEY WRITE option _ _ enabled. Important If you set this parameter to ALL, you cannot use in-use MyISAM tables from other programs, such as other MySQL servers or myisamchk. This helps prevent index damages. |
|---|---|---|---|---|---|
| delayed insert li _ _ mit | MyS QL 8.0 and MyS QL 5.7 | 100 | [1- 42949672 95] | No | After a specific number of delayed insert operations are performed, the INSERT DELAYED handler thread checks whether pending SELECT statements exist. The number of delayed insert operations is specified by delayed insert limit. If _ _ pending SELECT statements exist, the statements can be executed before the remaining delayed insert operations are performed. |
| delayed insert ti _ _ meout | MyS QL 8.0 and MyS QL 5.7 | 300 | [1-3600] | No | The period of time that an INSERT DELAYED handler thread can wait for INSERT statements before the thread is terminated. Unit: seconds. |

| delayed queue si _ _ ze | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [1- 42949672 95] | No | The maximum number of rows that can be queued on each table when INSERT DELAYED statements are executed. If the queue is full, all clients from which INSERT DELAYED requests are sent must wait until the queue has space available. |
|---|---|---|---|---|---|
| disconnect on ex _ _ pired password _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | Yes | Specifies how the server handles clients with expired passwords. |
| div precision incr _ _ ement | MyS QL 8.0 and MyS QL 5.7 | 4 | [0-30] | No | The number of decimal places that need to be added to the result of a division operation performed with the / operator. Default value: 4. Minimum value: 0. Maximum value: 30. |
| end markers in j _ _ _ son | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to add an end marker to the JSON output of an optimizer. |
| eq range index _ _ _ dive limit _ | MyS QL 8.0 and MyS QL 5.7 | 100 | [0- 42949672 95] | No | The number of equality ranges for an index. If the number of equality ranges for an index is greater than or equal to the value of this parameter, the optimizer uses existing index statistics instead of doing index dives for equality ranges. If you set this parameter to 0, index dives are used. |
| event scheduler _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to enable the event scheduler. Valid values: ON, OFF, and DISABLED. The value DISABLED indicates that the event scheduler is completely disabled and cannot be enabled at runtime. |

| explicit defaults _ _ for timestamp _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether the default value of the TIMESTAMP column is the current timestamp. |
|---|---|---|---|---|---|
| flush time _ | MyS QL 8.0 and MyS QL 5.7 | 0 | [0- 31536000] | No | If you set this parameter to a value other than 0, all tables are closed at an interval that is specified by flush time to _ release resources and synchronize unflushed data to the disk. We recommend that you use this parameter only on systems with minimal resources. |
| ft max word len _ _ _ | MyS QL 8.0 and MyS QL 5.7 | 84 | [10- 42949672 95] | Yes | The maximum length of the word that needs to be included in a MyISAM FULLTEXT index. |
| ft min word len _ _ _ | MyS QL 8.0 and MyS QL 5.7 | 4 | [1-3600] | Yes | The minimum length of the word that needs to be included in a MyISAM FULLTEXT index. |
| ft query expansi _ _ on limit _ | MyS QL 8.0 and MyS QL 5.7 | 20 | [0-1000] | Yes | The number of top N matches that you want to use for full-text searches with WITH QUERY EXPANSION modifiers. |
| general log _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | Yes | Specifies whether to enable general query logging. The destination for log output is specified by log output. _ |

| group concat ma _ _ x len _ | MyS QL 8.0 and MyS QL 5.7 | 102 4 | [4- 18446744 07370954 752] | No | The maximum length of the result for the GROUP CONCAT() function. Unit: bytes. _ Default value: 1024. |
|---|---|---|---|---|---|
| host cache size _ _ | MyS QL 8.0 and MyS QL 5.7 | 644 | [0-65535] | No | The size of the host cache. If you set this parameter to 0, host caching is disabled. Changing the cache size at runtime causes an implicit FLUSH HOSTS operation that clears the host cache and truncates the host cache table. _ |
| innodb adaptive _ _ flushing | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to dynamically adjust the flush rate of dirty pages in the InnoDB buffer pool based on workloads. Adjusting the flush rate aims to prevent burstable I/O operations. |
| innodb adaptive _ _ flushing lwm _ | MyS QL 8.0 and MyS QL 5.7 | 10 | [0-70] | No | The threshold for the percentage of redo log capacity. If the threshold is reached, adaptive flushing is enabled. |
| innodb adaptive _ _ hash index _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable adaptive hash indexing. This parameter is available for the InnoDB storage engine. |

| innodb adaptive _ _ max sleep delay _ _ | MyS QL 8.0 and MyS QL 5.7 | 150 000 | [1- 1000000] | No | Enables InnoDB to automatically adjust the value of innodb thread sleep delay _ _ _ based on workloads. innodb thread sleep delay specifies the _ _ _ sleep duration of an InnoDB thread when the InnoDB thread has no pending events. If you set innodb adaptive max sleep delay to a _ _ _ _ value other than 0, the value of innodb thread sleep delay is _ _ _ automatically adjusted. The maximum value of innodb thread sleep delay is _ _ _ specified by innodb adaptive max sleep delay. Unit: _ _ _ _ microseconds. This parameter is suitable for scenarios in which systems slow down, especially when more than 16 InnoDB threads exist. This parameter is most suitable for MySQL systems that have hundreds or thousands of concurrent connections. |
|---|---|---|---|---|---|
| innodb autoexte _ nd increment _ | MyS QL 8.0 and MyS QL 5.7 | 64 | [1-1000] | No | The increment size that is used to extend the size of an auto-extending InnoDB system tablespace file when the size of the file reaches the upper limit. Unit: megabytes. Default value: 64. |
| innodb autoinc l _ _ ock mode _ | MyS QL 8.0 and MyS QL 5.7 | 2 | [0\|1\|2] | Yes | The lock mode that is used to generate auto-increment values. Valid values: 0: traditional mode. 1: consecutive mode. 2: interleaved mode. |
| innodb buffer po _ _ ol dump at shut _ _ _ down | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to record the pages that are cached in the InnoDB buffer pool when the MySQL server is shut down. Recording the pages shortens the warmup process at the next restart. In most cases, this parameter is used in combination with innodb buffer pool load at startup. _ _ _ _ _ innodb buffer pool dump pct defines _ _ _ _ the percentage of most recently used pages that need to be dumped in the buffer pool. |

| innodb buffer po _ _ ol dump pct _ _ | MyS QL 8.0 and MyS QL 5.7 | 25 | [1-100] | No | The percentage of the most recently used pages that need to be read and dumped in each buffer pool. Valid values: 1 to 100. Default value: 25. For example, if four buffer pools are available, 100 pages are cached in each buffer pool, and innodb buffer pool dump pct is set to _ _ _ _ 25, a total of 25 most recently used pages from each buffer pool are dumped. |
|---|---|---|---|---|---|
| innodb buffer po _ _ ol instances _ | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 8)} | [1-64] | Yes | The number of regions into which the InnoDB buffer pool is divided. For a system with a buffer pool in the multi- gigabyte range, dividing the buffer pool into separate instances can improve concurrency and reduce contention when different threads read data from and write data to cached pages. Each page that is stored in or read from the buffer pool is randomly assigned to one of the buffer pool instances by calling a hash function. Each buffer pool manages its idle lists, flush lists, least recently used (LRU) lists, and other data structures connected to the buffer pool, and is protected by its own buffer pool mutex. |
| innodb buffer po _ _ ol load at startu _ _ _ p | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | Yes | Specifies whether to load the same pages stored in the InnoDB buffer pool to automatically warm up the buffer pool during the MySQL server startup. In most cases, this parameter is used in combination with innodb buffer pool dump at shutdown. _ _ _ _ _ |
| innodb change b _ _ uffering | MyS QL 8.0 and MyS QL 5.7 | all | [none\|inser ts\|deletes\| changes\|p urges\|all] | No | Specifies whether InnoDB performs change buffering to delay write operations to secondary indexes so that the I/O operations can be sequentially performed. |

| innodb change b _ _ uffer max size _ _ | MyS QL 8.0 and MyS QL 5.7 | 25 | [0-50] | No | The maximum size of the InnoDB change buffer, as a percentage of the total size of the buffer pool. You can increase the value for a MySQL server on which a large number of insert, update, and delete operations are performed. You can also decrease the value for a MySQL server with unchanging data that is used for reporting. |
|---|---|---|---|---|---|
| innodb checksu _ m algorithm _ | MyS QL 8.0 and MyS QL 5.7 | crc3 2 | [innodb\|crc 32\|none\|st rict innodb _ \|strict crc3 _ 2\|strict no _ ne] | No | Specifies how to generate and verify the checksum stored in the disk blocks of InnoDB tablespaces. |
| innodb cmp per _ _ _ index enabled _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable compression-related statistics on each index for the INFORMATION SCHEMA.INNODB CMP PE _ _ _ R INDEX table. Statistics collection is _ costly. We recommend that you enable this parameter in development and testing environments or for secondary instances to improve performance related to InnoDB compressed tables. |
| innodb commit c _ _ oncurrency | MyS QL 8.0 and MyS QL 5.7 | 0 | [0-1000] | Yes | The number of threads that can be committed at a time. The default value 0 indicates that the number is unlimited. |
| innodb compress _ ion failure thresh _ _ old pct _ | MyS QL 8.0 and MyS QL 5.7 | 5 | [0-100] | No | The threshold of the compression failure rate for a table, in percentage. If this threshold is reached, MySQL adds padding to compressed pages. This helps prevent costly compression failures. If this threshold is exceeded, MySQL reserves additional idle storage for each new compressed page and dynamically adjusts the amount of the idle storage up to the percentage of the idle storage that is specified by innodb compression pad pct max. If _ _ _ _ you set this parameter to 0, the mechanism that is used to monitor compression efficiency and dynamically adjust the padding amount is disabled. |

| innodb compress _ ion level _ | MyS QL 8.0 and MyS QL 5.7 | 6 | [0-9] | No | The level of the zlib compression for InnoDB compressed tables and indexes. A large value allows you to store a large amount of data in a storage device but causes a high CPU overhead during compression. A small value allows you to reduce the CPU overhead when the storage is not a critical metric or the data that you want to use cannot be efficiently compressed. |
|---|---|---|---|---|---|
| innodb compress _ ion pad pct max _ _ _ | MyS QL 8.0 and MyS QL 5.7 | 50 | [0-70] | No | The maximum percentage of the idle storage that can be reserved for each compressed page. This ensures sufficient storage to reorganize the data and modification logs within a page when a compressed table or index is updated or the data may need to be compressed again. This parameter is suitable only when innodb compression failure threshold p _ _ _ _ ct is set to a value other than 0 and the compression failure rate exceeds the threshold. |
| innodb concurre _ ncy tickets _ | MyS QL 8.0 and MyS QL 5.7 | 500 0 | [1- 42949672 95] | No | The number of threads that can concurrently enter InnoDB. If the number of threads reaches the limit, a thread that tries to enter InnoDB is put into the queue. When a thread is allowed to enter InnoDB, tickets are assigned to the thread. The thread can enter and exit InnoDB until it runs out of the tickets. The number of tickets is the same as the value of innodb concurrency tickets. If a _ _ thread runs out of the tickets and tries to enter InnoDB again, it is subject to concurrency checks and may be put into a queue again. Default value: 5000. |
| innodb data file _ _ _ purge | 8.0 | ON | [ON\|OFF] | No | Specifies whether to enable asynchronous file deletion. |
| innodb data file _ _ _ purge interval _ | 8.0 | 100 | [0-10000] | No | The interval to delete the file. Unit: milliseconds. |
| innodb data file _ _ _ purge max size _ _ | 8.0 | 128 | [16- 10737418 24] | No | The maximum size of the file that you can delete. Unit: MB. |

| innodb deadlock _ _ detect | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to disable deadlock detection. If a large number of threads wait for the same lock in a high- concurrency system, deadlock detection may slow down the system. In some cases, we recommend that you disable deadlock detection and configure innodb lock wait timeout for transaction _ _ _ rollback, which is more efficient. |
|---|---|---|---|---|---|
| innodb disable s _ _ ort file cache _ _ | 5.7 | ON | [ON\|OFF] | No | If this parameter is enabled, page caching is disabled when InnoDB uses sorted files. |
| innodb flush met _ _ hod | MyS QL 8.0 and MyS QL 5.7 | O DI _ REC T | [fsync\|O D _ SYNC\|little sync\|nosyn c\|O DIREC _ T\|O DIREC _ T NO FSY _ _ NC] | Yes | The method that is used to flush data to InnoDB data files and log files, which may affect I/O throughput. |
| innodb flush nei _ _ ghbors | MyS QL 8.0 and MyS QL 5.7 | 0 | [0\|1\|2] | No | Specifies whether to flush dirty pages in the same extension when a page is flushed from the InnoDB buffer pool. |
| innodb flush syn _ _ c | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | This parameter is enabled by default. This setting causes the innodb io capacity setting to be ignored _ _ when burstable I/O operations occur at checkpoints. To make sure that the number of I/O operations does not exceed the number specified by innodb io capacity, we recommend that _ _ you set innodb flush sync to OFF. _ _ |
| innodb ft cache _ _ _ size | MyS QL 8.0 and MyS QL 5.7 | 800 000 0 | [1600000- 80000000] | Yes | The memory that is allocated to the InnoDB FULLTEXT index cache. The memory is used to store parsed documents when an InnoDB FULLTEXT index is created. Unit: bytes. Index insert and update operations can be committed to the disk only when the cache size limit that is specified by innodb ft cache size is reached. _ _ _ innodb ft cache size defines the cache _ _ _ size on a per-table basis. |

| innodb ft enable _ _ diag print _ _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable additional full-text search (FTS) diagnostic output. This parameter is intended for advanced FTS debugging and is not of interest to most users. Output is recorded in error logs, including information. |
|---|---|---|---|---|---|
| innodb ft enable _ _ stopword _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies a set of stopwords to associate with an InnoDB FULLTEXT index when the index is created. If innodb ft user stopword table is _ _ _ _ configured, the stopwords are obtained from the table specified by innodb ft user stopword table. If _ _ _ _ innodb ft server stopword table is _ _ _ _ configured, the stopwords are obtained from the table specified by innodb ft server stopword table. If none _ _ _ _ of these parameters is configured, the default stopword set is used. |
| innodb ft max to _ _ _ ken size _ | MyS QL 8.0 and MyS QL 5.7 | 84 | [10-84] | Yes | The maximum length of a word that is stored in an InnoDB FULLTEXT index. |
| innodb ft min to _ _ _ ken size _ | MyS QL 8.0 and MyS QL 5.7 | 3 | [0-16] | Yes | The minimum length of a word that is stored in an InnoDB FULLTEXT index. |
| innodb ft num w _ _ _ ord optimize _ | MyS QL 8.0 and MyS QL 5.7 | 200 0 | [0-10000] | No | The number of words that need to be processed during each OPTIMIZE TABLE operation on an InnoDB FULLTEXT index. If you perform a large number of insert or update operations on a table that contains an InnoDB FULLTEXT index, a large number of index maintenance operations are required to incorporate all changes. As a result, a large number of OPTIMIZE TABLE statements may be executed, and each statement is executed at the point at which the last statement is stopped. |

| innodb ft result _ _ _ cache limit _ | MyS QL 8.0 and MyS QL 5.7 | 200 000 000 0 | [1000000- 42949672 95] | No | The result cache limit on each InnoDB full-text search or thread. Unit: bytes. Intermediate and final InnoDB full-text search query results are processed in memory. This parameter helps prevent excessive memory consumption when an InnoDB full-text search generates a query result that contains a large number of data records, such as millions or hundreds of millions of data rows. Memory is allocated for a full-text search based on your business requirements. If the result cache limit is reached, an error indicating that the full-text search exceeds the maximum allowed memory is reported. |
|---|---|---|---|---|---|
| innodb ft sort pll _ _ _ degree _ | MyS QL 8.0 and MyS QL 5.7 | 2 | [1-16] | Yes | The number of threads that are used for parallel indexing and to tokenize text in an InnoDB FULLTEXT index when a search index is created. |
| innodb ft total c _ _ _ ache size _ | MyS QL 8.0 and MyS QL 5.7 | 640 000 000 | [32000000 - 16000000 00] | Yes | The total memory that is allocated for the index caches of InnoDB full-text searches on all tables. Unit: bytes. If you create a large number of tables that contain FULLTEXT search indexes, a large amount of memory is occupied. innodb ft total cache size defines a _ _ _ _ global memory limit on all FULLTEXT search indexes to prevent excessive memory consumption. If the amount of memory consumed by index-related operations reaches the global memory limit, forceful synchronization is triggered. |
| innodb io capacit _ _ y | MyS QL 8.0 and MyS QL 5.7 | 200 00 | [0- 18446744 07370955 1615] | No | The maximum number of I/O operations for InnoDB background tasks, such as flushing pages from the buffer pool and merging data from the change buffer. |

| innodb io capacit _ _ y max _ | MyS QL 8.0 and MyS QL 5.7 | 400 00 | [0- 18446744 07370955 1615] | No | If a flushing operation falls behind, InnoDB can forcefully perform the operation at a higher rate than that specified by innodb io capacity. In this _ _ case, innodb io capacity max defines _ _ _ the maximum number of I/O operations for InnoDB background tasks. |
|---|---|---|---|---|---|
| innodb large pre _ _ fix | 5.7 | OFF | [ON\|OFF] | No | If this parameter is enabled, the length of the prefix for an index can be longer than 767 bytes. The maximum length of the prefix for an index is 3,072 bytes. This parameter is suitable for InnoDB tables that use the DYNAMIC or COMPRESSED row format. |
| innodb lock wait _ _ timeout _ | MyS QL 8.0 and MyS QL 5.7 | 50 | [1- 10737418 24] | No | The period of timeout that an InnoDB transaction waits for a row lock before the transaction is aborted. Unit: seconds. Default value: 50. |
| innodb log check _ _ sums | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable the checksums for redo log pages. innodb log checksums is an alternative _ _ for innodb log checksum algorithm. _ _ _ |
| innodb log comp _ _ ressed pages _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to write images of re- compressed pages to the redo log. Recompression may occur when the compressed data is changed. |
| innodb log file si _ _ _ ze | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/6, 157 286 400 0)} | [4194304- 10737418 2400] | Yes | The size of each log file in a log group. Unit: bytes. |

| innodb lru scan _ _ _ depth | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76/8 , 819 2)} | [100- 18446744 07370955 1615] | No | A parameter that affects the flush algorithms and heuristic algorithms of the InnoDB buffer pool. This parameter is used to tune I/O-intensive workloads. It specifies how deep the page cleaner thread scans the LRU lists in the buffer pool to identify dirty pages to be flushed for a buffer pool instance. The operation is performed in the background once per second. |
|---|---|---|---|---|---|
| innodb max dirty _ _ pages pct _ _ | MyS QL 8.0 and MyS QL 5.7 | 75 | [0-99] | No | The value of this parameter is an integer that ranges from 0 to 100. The default value for the built-in InnoDB storage engine is 90. The default value for the InnoDB extension is 75. The main thread in InnoDB tries to write data from the buffer pool to pages so that the percentage of dirty pages does not exceed this value. |
| innodb max dirty _ _ pages pct lwm _ _ _ | MyS QL 8.0 and MyS QL 5.7 | 10 | [0-99] | No | The threshold for the percentage of dirty pages. If the threshold is exceeded, preflushing is enabled to control the ratio of dirty pages. The default value 0 indicates that preflushing is disabled. |
| innodb max purg _ _ e lag _ | MyS QL 8.0 and MyS QL 5.7 | 0 | [0- 42949672 95] | No | The maximum length of the purge lag. The default value 0 indicates that no limits are imposed and no latency occurs. |
| innodb max purg _ _ e lag delay _ _ | MyS QL 8.0 and MyS QL 5.7 | 0 | [0- 10000000] | No | The maximum latency when the threshold specified by innodb max purge lag is exceeded. _ _ _ Unit: microseconds. A non-zero value indicates the maximum latency that is imposed based on the value of innodb max purge lag. The default _ _ _ value 0 indicates that no upper limit is imposed on the latency. |

| innodb max und _ _ o log size _ _ | MyS QL 8.0 and MyS QL 5.7 | 107 374 182 4 | [10485760 - 18446744 07370955 1615] | No | The threshold of the undo tablespace. If an undo tablespace exceeds the threshold, it can be marked for truncation when innodb undo log truncate is enabled. _ _ _ Default value: 1073741824 bytes, which is 1,024 MiB. |
|---|---|---|---|---|---|
| innodb monitor _ _ disable | 8.0 | - | all | No | Disables the InnoDB metrics counter. You can use the INFORMATION SCHEMA.INNODB METRIC _ _ S table to query counter data. |
| innodb monitor e _ _ nable | 8.0 | - | all | No | Enables the InnoDB Monitor for output. After the InnoDB Monitor is enabled, InnoDB generates detailed runtime information that can be used for performance analysis and troubleshooting. You can execute the SHOW ENGINE INNODB STATUS statement to view the output. |
| innodb old block _ _ s pct _ | MyS QL 8.0 and MyS QL 5.7 | 37 | [5-95] | No | The approximate percentage of the InnoDB buffer pools that are used for the old block sublist. This parameter is suitable only for the InnoDB extension. Valid values: 5 to 95. Default value: 37, which is 3/8 of the buffer pools. |
| innodb old block _ _ s time _ | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [0-1024] | No | The period of time that a block inserted into the old sublist must stay after its first access before the block can be moved to the new sublist. Unit: milliseconds. This parameter is suitable only for the InnoDB extension. If the default value 0 is used for this parameter, a block inserted into the old sublist is immediately moved to a new sublist after its first access, regardless of when the block is accessed. If you set this parameter to a value greater than 0, a block inserted into the old sublist must stay for the specified period of time and then is moved to a new sublist after its first access. Unit: milliseconds. |

| innodb online alt _ _ er log max size _ _ _ | MyS QL 8.0 and MyS QL 5.7 | 134 217 728 | [13421772 8- 21474836 47] | No | The maximum size of alter logs for online index creation. |
|---|---|---|---|---|---|
| innodb open files _ _ | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl assC PU* 500, 800 0)} | [1-8192] | Yes | The maximum number of InnoDB files that can remain open at a time in MySQL. This parameter is suitable only when multiple InnoDB tablespaces are used. |
| innodb optimize _ _ fulltext only _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | The changes on how the OPTIMIZE TABLE statement is executed on InnoDB tables. This parameter is temporarily enabled when InnoDB tables with FULLTEXT indexes are maintained. |
| innodb page cle _ _ aners | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 8)} | [1-64] | Yes | The number of page cleaner threads that are used to flush dirty pages from buffer pool instances. Page cleaner threads are used to flush LRU lists and flush lists. In MySQL 5.6, one page cleaner thread is introduced to offload the buffer pool refresh from the InnoDB main thread. In MySQL 5.7, multiple page cleaner threads are supported by InnoDB. The value 1 indicates that the configuration for the versions earlier than MySQL 5.7 is used, which indicates one page cleaner thread exists. If multiple page cleaner threads exist, the flushing tasks for each buffer pool instance are distributed to idle page cleaner threads. In MySQL 5.7, the default value of this parameter is changed from 1 to 4. If the number of page cleaner threads exceeds the number of buffer pool instances, the additional threads remain idle and do not consume CPU resources. This parameter is dynamic and can be changed online. |

| innodb print all _ _ _ deadlocks | MyS QL 8.0 and MyS QL 5.7 | OFF | [OFF\|ON] | No | If this parameter is enabled, information about all deadlocks is recorded in the MySQL error log. By default, this parameter is disabled. |
|---|---|---|---|---|---|
| innodb purge ba _ _ tch size _ | MyS QL 8.0 and MyS QL 5.7 | 300 | [1-5000] | Yes | The number of undo logs to purge in one batch. The purge operation is to flush changed blocks in the buffer pool to the disk. |
| innodb purge rse _ _ g truncate frequ _ _ ency | MyS QL 8.0 and MyS QL 5.7 | 128 | [1-128] | No | The frequency at which the purge system releases rollback segments in terms of the number of times that the PURGE method is invoked. Before rollback segments are released, an undo tablespace cannot be truncated. In most cases, the purge system releases rollback segments every 128 times that the PURGE method is invoked. Default value: 128. A small value indicates a high frequency at which the purge thread releases rollback segments. |
| innodb purge thr _ _ eads | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 8)} | [1-32] | Yes | The number of background threads dedicated to the InnoDB purge operation. |
| innodb random r _ _ ead ahead _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable random read-ahead to optimize InnoDB I/O operations. |

| innodb read ahe _ _ ad threshold _ | MyS QL 8.0 and MyS QL 5.7 | 56 | [0-1024] | No | The sensitivity of linear read-ahead that InnoDB uses to prefetch pages into the buffer pool. This parameter is suitable only for the InnoDB extension. If the number of pages that InnoDB sequentially reads from an extent (64 pages) is greater than or equal to the value of innodb read ahead threshold, _ _ _ an asynchronous read for the following extents is enabled. |
|---|---|---|---|---|---|
| innodb read io t _ _ _ hreads | MyS QL 8.0 and MyS QL 5.7 | 4 | [1-64] | Yes | The number of I/O threads for read operations in InnoDB. This parameter is suitable only for the InnoDB extension. Default value: 4. |
| innodb rollback _ _ on timeout _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [OFF\|ON] | Yes | By default, InnoDB rolls back only the last statement when a transaction times out. If innodb-rollback-on-timeout is configured, a transaction timeout causes InnoDB to abort and roll back the entire transaction. This process is the same as that in MySQL 4.1. This parameter is introduced in MySQL 5.1.15. |
| innodb rollback s _ _ egments | MyS QL 8.0 and MyS QL 5.7 | 128 | [1-128] | No | The number of rollback segments used by InnoDB. |
| innodb sort buffe _ _ r size _ | MyS QL 8.0 and MyS QL 5.7 | 104 857 6 | [65536- 67108864] | Yes | The size of the sort buffer that is used to sort data during InnoDB index creation. The amount of data that is read into memory for internal sorting and written to the disk. This process is called "running". During the merge phase, a pair of buffers with the specified size are read and merged. A large value indicates a few running processes and merging operations. |
| innodb spin wait _ _ delay _ | MyS QL 8.0 and MyS QL 5.7 | 6 | [0- 42949672 95] | No | The maximum latency between polls for a spin lock. The underlying implementation of this mechanism varies based on the combination of hardware and operating systems. As a result, the latency is not fixed. |

| innodb stats aut _ _ o recalc _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable InnoDB to automatically recalculate persistence statistics after the data in a table is significantly changed. The threshold equals 10% of the rows in the table. This parameter is suitable for tables that are created when innodb stats persistent is _ _ enabled. You can also configure the STATS PERSISTENT = 1 setting for the _ CREATE TABLE or ALTER TABLE statement to automatically recalculate persistence statistics. The amount of sample data that is used to generate statistical data is specified by innodb stats persistent sample pages. _ _ _ _ |
|---|---|---|---|---|---|
| innodb stats met _ _ hod | MyS QL 8.0 and MyS QL 5.7 | nulls equ _ al | [nulls equ _ al\|nulls un _ equal\|nulls ignored] _ | No | The method that the server uses to process NULL values during the collection of statistics about the distribution of index values for InnoDB tables. Valid values: nulls equal, _ nulls unequal, and nulls ignored. The _ _ value nulls equal indicates that all NULL _ values are considered equivalent and a single value group that has the same size as the number of NULL values is generated. The value nulls unequal _ indicates that NULL values are considered unequivalent, and each NULL value forms a distinct value group with the size of 1. The value nulls ignored _ indicates that NULL values are ignored. |
| innodb stats on _ _ _ metadata | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | This parameter is suitable only when optimizer statistics are non-persistent. If a table is created or changed when innodb stats persistent is disabled or _ _ STATS PERSISTENT is set to 0, optimizer _ statistics are not stored to disks. |
| innodb stats per _ _ sistent | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether InnoDB index statistics are stored to disks. If InnoDB index statistics are not stored to disks, statistical data may be frequently recalculated, which may cause changes to query execution plans. This setting is stored with each table when the table is created. You can set innodb stats persistent at the global _ _ level before you create a table, or use the STATS PERSISTENT clause in the _ CREATE TABLE and ALTER TABLE statements to override the system-level setting and configure persistent statistics for individual tables. |

| innodb stats per _ _ sistent sample p _ _ ages | MyS QL 8.0 and MyS QL 5.7 | 20 | [0- 42949672 95] | No | The number of index pages to sample when cardinality and other statistics, such as statistics calculated by the ANALYZE TABLE statement, are estimated for an indexed column. A large value indicates a high accuracy of index statistics. This improves the query execution plan but increases the I/O workloads during the execution of the ANALYZE TABLE statement on an InnoDB table. |
|---|---|---|---|---|---|
| innodb stats sa _ _ mple pages _ | 5.7 | 8 | [1- 42949672 96] | No | The number of index pages that are used for index distribution statistics, such as the statistics calculated by the ANALYZE TABLE statement. This parameter is suitable only for the InnoDB extension. Default value: 8. |
| innodb stats tran _ _ sient sample pag _ _ es | MyS QL 8.0 and MyS QL 5.7 | 8 | [1- 42949672 95] | No | The number of index pages to sample when cardinality and other statistics, such as statistics calculated by the ANALYZE TABLE statement, are estimated for an indexed column. Default value: 8. A large value indicates a high accuracy of index statistics. This improves the query execution plan but increases the I/O workloads when an InnoDB table is opened or the statistics are recalculated. |
| innodb status ou _ _ tput | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable periodic output for the standard InnoDB Monitor. This parameter is used in combination with innodb status output locks to _ _ _ enable or disable periodic output for the InnoDB Lock Monitor. |

| innodb status ou _ _ tput locks _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable the InnoDB Lock Monitor. If this parameter is enabled, the InnoDB Lock Monitor records additional information about locks in the SHOW ENGINE INNODB STATUS output and records the information in the periodic output of the MySQL error log. The periodic output for the InnoDB Lock Monitor is recorded as part of the output of the standard InnoDB Monitor. As a result, the standard InnoDB Monitor must be enabled for the InnoDB Lock Monitor to periodically record data to the MySQL error log. |
|---|---|---|---|---|---|
| innodb strict mo _ _ de | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether InnoDB returns an error rather than a warning for similar operations in strict SQL mode under certain conditions. This parameter is suitable only for the InnoDB extension. Default value: OFF. For more information about the affected conditions, see the description of innodb strict mode. _ _ |
| innodb sync arra _ _ y size _ | MyS QL 8.0 and MyS QL 5.7 | 128 | [1-1024] | Yes | The size of the mutex or lock wait array. Increasing the value splits the internal data structure that is used to coordinate threads. This improves the concurrency in workloads with a large number of waiting threads. You must configure this parameter when you start the MySQL instance. The setting of the parameter cannot be changed. We recommend that you set this parameter to a large value for workloads that frequently generate a large number of waiting threads, typically greater than 768. |
| innodb sync spin _ _ loops _ | MyS QL 8.0 and MyS QL 5.7 | M y S Q L 8. 0: 1 0 0 M y S Q L 5. 7: 3 0 | [0- 42949672 95] | No | The number of times a thread waits for an InnoDB mutex to be released before the thread is suspended. |

| innodb table loc _ _ ks | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | If autocommit is set to 0, InnoDB accepts LOCK TABLES. MySQL does not return results before the LOCK TABLES ... WRITE statement is executed until all threads release their locks on a table. Default value: 1, which indicates that LOCK TABLES causes InnoDB to internally lock a table when autocommit is set to 0. |
|---|---|---|---|---|---|
| innodb thread co _ _ ncurrency | MyS QL 8.0 and MyS QL 5.7 | 0 | [0-1000] | No | The maximum number of threads that can be concurrently run in InnoDB. If this threshold is reached, additional threads enter the first in, first out (FIFO) queue. |
| innodb thread sl _ _ eep delay _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [0- 1000000] | No | The number of microseconds that an InnoDB thread sleeps for before the InnoDB thread enters the InnoDB queue. The value 0 indicates that the InnoDB thread does not sleep. |
| innodb undo log _ _ _ truncate | 5.7 | OFF | [ON\|OFF] | No | If this parameter is enabled, undo tablespaces that exceed the threshold specified by innodb max undo log size _ _ _ _ are marked for truncation. |
| innodb write io t _ _ _ hreads | MyS QL 8.0 and MyS QL 5.7 | 4 | [1-64] | Yes | The number of I/O threads that are used for write operations in InnoDB. This parameter is suitable only for the InnoDB extension. Default value: 4. |
| interactive timeo _ ut | MyS QL 8.0 and MyS QL 5.7 | 720 0 | [10-86400] | No | The period of time that the server waits for the activity on an interactive connection before the interactive connection is terminated. An interactive client is defined as a client that uses the CLIENT INTERACTIVE option to connect _ to mysql real connect(). _ _ Unit: seconds. |

| join buffer size _ _ | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76* 128, 262 144) } | [128- 42949672 95] | No | The minimum size of the buffer used for plain index scans, range index scans, and joins that do not use indexes and thus perform full table scans. |
|---|---|---|---|---|---|
| key cache age t _ _ _ hreshold | MyS QL 8.0 and MyS QL 5.7 | 300 | [100- 42949672 95] | No | The demotion of buffers from the hot sublist of a key cache to the warm sublist. A small value indicates a quick demotion. Minimum value: 100. Default value: 300. Unit: seconds. |
| key cache block _ _ _ size | MyS QL 8.0 and MyS QL 5.7 | 102 4 | [512- 16384] | No | The size of blocks in the key cache. Default value: 1024. Unit: bytes. |
| key cache divisio _ _ n limit _ | MyS QL 8.0 and MyS QL 5.7 | 100 | [1-100] | No | The division point between the hot sublist and warm sublist of the key cache buffer list. The value is the percentage of the buffer list that can be used for the warm sublist. Valid values: 1 to 100. Default value: 100. |

| lc time names _ _ | MyS QL 8.0 and MyS QL 5.7 | en _ US | [ja JP\|pt B _ _ R\|en US] _ | No | The locale that controls the language used to display the day name, month name, and abbreviations. This parameter affects the output of the DATE FORMAT(), DAYNAME() and _ MONTHNAME() functions. Locale names are POSIX-style values such as 'ja JP' or _ 'pt BR'. Default value: 'en US', _ _ regardless of the system locale settings. |
|---|---|---|---|---|---|
| local infile _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable the server- side LOCAL capability for LOAD DATA statements. |
| lock wait timeou _ _ t | MyS QL 8.0 and MyS QL 5.7 | 315 360 00 | [1- 10737418 24] | No | The timeout for an attempt to acquire metadata locks. Unit: seconds. Valid values: 1 to 31536000. The value 31536000 indicates a year. Default value: 31536000. |
| log error verbosi _ _ ty | MyS QL 8.0 and MyS QL 5.7 | 2 | [1-3] | No | The verbosity of the server to handle events that are used for error logs. |
| log queries not _ _ _ using indexes _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to write queries that do not use indexes to slow query logs. |
| log slow admin s _ _ _ tatements | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to write slow administration statements to slow query logs. |

| log throttle queri _ _ es not using ind _ _ _ exes | MyS QL 8.0 and MyS QL 5.7 | 0 | [0- 42949672 95] | No | If log queries not using indexes is _ _ _ _ enabled, log throttle queries not using indexes _ _ _ _ _ limits the number of queries that can be written to the slow query logs per minute. This parameter is suitable when the queries do not use indexes. |
|---|---|---|---|---|---|
| long query time _ _ | MyS QL 8.0 and MyS QL 5.7 | 1 | [0.1- 31536000] | No | If a query takes a period of time that is longer than the threshold specified by this parameter, the Slow queries counter _ increments. If slow query logging is enabled, the query is written to the slow query log file. Unit: seconds. |
| loose ccl queue _ _ _ bucket count _ | MyS QL 8.0 and MyS QL 5.7 | 4 | [1-64] | No | The number of groups when the concurrency control (CCL) queue is used. |
| loose ccl queue _ _ _ bucket size _ | MyS QL 8.0 and MyS QL 5.7 | 64 | [1-4096] | No | The maximum number of concurrent requests when the CCL queue is used. |
| loose ccl queue _ _ _ hot delete _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to enter the CCL queue in a delete operation under certain conditions. |
| loose ccl queue _ _ _ hot update _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to enter the CCL queue in an update operation under certain conditions. |
| loose collation s _ _ erver | 5.7 | utf8 gen _ eral ci _ | [utf8 bin\|u _ tf8 general _ ci\|latin1 b _ _ in\|latin1 g _ eneral ci\|g _ bk chinese _ ci\|gbk bin _ _ \|utf8mb4 _ general ci\| _ utf8mb4 bi _ n] | Yes | The default collation of the server. |

| loose connection _ control failed co _ _ _ nnections thresh _ old | 8.0 | 3 | [0- 21474836 47] | No | - |
|---|---|---|---|---|---|
| loose connection _ control max con _ _ _ nection delay _ | 8.0 | 200 0 | [1000- 21474836 47] | No | - |
| loose connection _ control min con _ _ _ nection delay _ | 8.0 | 100 0 | [1000- 21474836 47] | No | - |
| loose ignore ind _ _ ex hint error _ _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to ignore index prompt errors. |
| loose information _ schema stats e _ _ _ xpiry | 8.0 | 864 00 | [0- 31536000] | No | The period of time that the system receives the data read by mysqld from the storage engine and replaces the data in the cache. Unit: seconds. |
| loose innodb dat _ _ a file purge _ _ | 5.7 | ON | [ON\|OFF] | No | Specifies whether to delete data files in phases. |
| loose innodb dat _ _ a file purge inter _ _ _ val | 5.7 | 100 | [0-10000] | No | The interval between two consecutive data file deletions. Unit: milliseconds. |
| loose innodb dat _ _ a file purge max _ _ _ size _ | 5.7 | 512 | [16- 10737418 24] | No | The maximum size of data files that can be deleted at a time. Unit: MB. |
| loose innodb log _ _ optimize ddl _ _ | MyS QL 8.0 and MyS QL 5.7 | M y S Q L 8. 2: O N M y S Q L 5. 7: O FF | [ON\|OFF] | No | Specifies whether to reduce redo logs when indexes are created or when tables are recreated locally. The value OFF prevents latencies caused by page refresh operations and allows concurrent backups. |

| loose innodb log _ _ write ahead siz _ _ _ e | 8.0 | 409 6 | [512- 16384] | No | The size of write-ahead logs in bytes. To prevent read-on-write operations, this parameter must match the I/O size of the OS block size. |
|---|---|---|---|---|---|
| loose innodb nu _ _ ma interleave _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | Yes | Specifies whether to enable the NUMA interleave memory policy for allocation of the InnoDB buffer pool. When this parameter is enabled, the NUMA memory policy of mysqld is set to MPOL INTERLEAVE. After the InnoDB _ buffer pool is allocated, the NUMA memory policy is set back to MPOL DEFAULT. This parameter is _ suitable only when MySQL is compiled on a NUMA-enabled Linux system. |
| loose innodb par _ _ allel read thread _ _ s | 8.0 | 1 | [0-256] | No | The number of threads to read in parallel. |
| loose innodb rds _ _ faster ddl _ _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable the faster DDL feature. |
| loose innodb rds _ _ flashback task _ _ _ enabled | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to roll forward new read views by default. |
| loose internal tm _ _ p disk storage e _ _ _ ngine | 5.7 | INN ODB | [INNODB\|M YISAM] | No | The internal temporary table engine on the disk. |
| loose innodb und _ _ o retention _ | 8.0 | 900 | [0- 42949672 95] | No | This parameter specifies the retention period of undo records. Undo records that are generated after the retention period elapses cannot be queried. Unit: seconds. If you set the loose innodb rds flashback task enable _ _ _ _ _ d parameter to OFF, you must also set this parameter to 0. |

| loose innodb und _ _ o space reserved _ _ size _ | 8.0 | 0 | [0- 42949672 95] | No | This parameter specifies the amount of disk space that is reserved for the undo tablespace. Unit: MB. If the value of the loose innodb undo retention parameter _ _ _ is not 0, a larger value of this parameter indicates that more undo records can be reserved in the undo tablespace. |
|---|---|---|---|---|---|
| loose innodb und _ _ o space supremu _ _ m size _ | 8.0 | 102 40 | [0- 42949672 95] | No | This parameter specifies the maximum disk space that can be occupied by the undo tablespace. Unit: MB. When the maximum disk space is reached, the undo records are forcefully deleted regardless of the value of the loose innodb undo retention parameter. _ _ _ |
| loose max execu _ _ tion time _ | 5.7 | 0 | [0- 42949672 95] | No | If the execution of a statement lasts longer than the value of this parameter, the execution is interrupted. |
| loose max state _ _ ment time _ | 5.7 | 0 | [0- 42949672 95] | No | If the execution of a statement lasts longer than the value of this parameter, the execution is interrupted. |
| loose multi block _ _ s ddl count _ _ | 8.0 | 0 | [0-1024] | No | The number of blocks that can be queried at a time in some DDL queries. |
| loose opt rds en _ _ _ able show slave _ _ _ lag | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | If you set this parameter to ON, the show slave lag command is allowed. |
| loose opt rds las _ _ _ t error gtid _ _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | If you set this parameter to ON, Last SQL Error Gtid is displayed in _ _ _ the show slave status command. |

| ide·Instances |   |   |   |   |   |
|---|---|---|---|---|---|
| loose optimizer s _ _ witch | 5.7 | inde x m _ erge =on ,ind ex _ mer ge u _ nion =on ,ind ex _ mer ge s _ o rt u _ nion =on ,ind ex _ mer ge i _ nter secti on= on,e ngin e co _ n ditio n p _ ush dow n=o n,in dex _ con ditio n p _ ush dow n=o n,mr r =on ,mrr cos _ t ba _ sed =on ,bloc k ne _ sted loo _ p=o n,ba tche d | .* | No | This parameter controls optimizer behaviors. |

|   |   | key _ acc _ ess =off ,mat erial izati on= on,s emij oin= on,l oo sesc an= on,fi rstm atch =on ,sub quer y m _ ateri aliza tion c _ ost _ base d=o n,us e in _ dex _ exte nsio ns= on |   |   |   |
|---|---|---|---|---|---|
| loose optimizer t _ _ race | MyS QL 8.0 and MyS QL 5.7 | ena bled =off ,one line _ =off | .* | No | This parameter has the following options: enabled and one line. _ |

| loose optimizer t _ _ race features _ | MyS QL 8.0 and MyS QL 5.7 | gree dy s _ earc h=o n,ra nge _ opti mize r=o n,dy nam ic ra _ nge =on ,rep eate d su _ bsel ect =on | .* | No | This parameter specifies the features that are not traced. |
|---|---|---|---|---|---|
| loose password _ _ history | 8.0 | 0 | [0-10] | No | - |
| loose performanc _ e point iostat int _ _ _ erval | 5.7 | 2 | [0-60] | No | The interval at which I/O statistics are collected. Unit: milliseconds. |
| loose performanc _ e point iostat vol _ _ _ ume size _ | 5.7 | 100 00 | [0-100000] | Yes | The maximum capacity of I/O statistics that can be collected. Unit: number of slots. |
| loose performanc _ e point lock rwlo _ _ _ ck enabled _ | 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable the performance optimization feature for read or write locks. |
| loose performanc _ e schema accou _ _ nts size _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the accounts table. If you set this parameter to 0, Performance Schema neither maintains connection statistics in the accounts table nor maintains status parameter information in the status by account _ _ table. |
| loose performanc _ e schema digest _ _ s size _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of rows in the events statements summary by digest _ _ _ _ table. If this threshold is exceeded, a digest cannot be instrumented. As a result, Performance Schema increases the value of performance schema digest lost. _ _ _ |

| loose performanc _ e schema error _ _ _ size | 8.0 | 0 | [0- 1048576] | Yes | The number of codes of server errors that are detected. The default value is the actual number of codes of server errors. You can set this parameter to a value within the value range. The expected purpose of this parameter is to detect all errors (the default value) or to indicate no errors (the value 0). |
|---|---|---|---|---|---|
| loose performanc _ e schema hosts _ _ _ size | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the hosts table. If you set this parameter to 0, Performance Schema neither maintains connection statistics in the hosts table nor maintains status parameter information in the status by host table. _ _ |
| loose performanc _ e schema max c _ _ _ ond instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of instrumented condition objects. |
| loose performanc _ e schema max fi _ _ _ le instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [-1- 1048576] | Yes | The maximum number of instrumented file objects. |
| loose performanc _ e schema max i _ _ _ ndex stat _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of indexes for Performance Schema to maintain statistics. If this threshold is exceeded, index statistics are lost. As a result, Performance Schema increases the value of performance schema index stat lost. _ _ _ _ The default value is automatically adjusted based on the value of performance schema max table instanc _ _ _ _ es. |
| loose performanc _ e schema max _ _ _ metadata locks _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of metadata lock instruments. This parameter specifies the size of the metadata locks table. If _ this threshold is exceeded, a metadata lock cannot be instrumented. As a result, Performance Schema increases the value of performance schema metadata lock los _ _ _ _ t. |

| loose performanc _ e schema max _ _ _ mutex instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 10485760 0] | Yes | The maximum number of instrumented mutex objects. |
|---|---|---|---|---|---|
| loose performanc _ e schema max p _ _ _ repared stateme _ nts instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [-1- 4194304] | Yes | The maximum number of rows in the prepared statements instances table. If _ _ this threshold is exceeded, a prepared statement cannot be instrumented. As a result, Performance Schema increases the value of performance schema prepared stateme _ _ _ nts lost. _ |
| loose performanc _ e schema max p _ _ _ rogram instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of stored procedures for Performance Schema to maintain statistics. If this threshold is exceeded, Performance Schema increases the value of performance schema program lost. _ _ _ |
| loose performanc _ e schema max r _ _ _ wlock instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 10485760 0] | Yes | The maximum number of instrumented RW lock objects. |
| loose performanc _ e schema max s _ _ _ ocket instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [-1- 1048576] | Yes | The maximum number of instrumented socket objects. |
| loose performanc _ e schema max t _ _ _ able handles _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of open table objects. This parameter controls the size of the table handles table. If this _ threshold is exceeded, a table handle cannot be instrumented. As a result, Performance Schema increases the value of performance schema table handles lost _ _ _ _ . |

| loose performanc _ e schema max t _ _ _ able instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 0 | [-1- 1048576] | Yes | The maximum number of instrumented table objects. |
|---|---|---|---|---|---|
| loose performanc _ e schema max t _ _ _ able lock stat _ _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of tables for which Performance Schema maintains lock statistics. If this threshold is exceeded, table lock statistics are lost. As a result, Performance Schema increases the value of performance schema table lock stat los _ _ _ _ _ t. |
| loose performanc _ e schema max t _ _ _ hread instances _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of instrumented thread objects. This parameter controls the size of the threads table. If this threshold is exceeded, a thread cannot be instrumented. As a result, Performance Schema increases the value of performance schema thread instances l _ _ _ _ ost. |
| loose performanc _ e schema setup _ _ _ actors size _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the setup actors _ table. |
| loose performanc _ e schema setup _ _ _ objects size _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the setup objects _ table. |
| loose performanc _ e schema users _ _ _ size | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the users table. If you set this parameter to 0, Performance Schema neither maintains connection statistics in the users table nor maintains status parameter information in the status by user table. _ _ |

| loose rds audit _ _ _ max sql size _ _ | 5.7 | 819 2 | [0-32768] | No | The maximum size of SQL statements in the ApsaraDB RDS audit log. |
|---|---|---|---|---|---|
| loose rds check _ _ _ core file enabled _ _ | 5.7 | ON | [ON\|OFF] | No | Specifies whether to enables core files checking |
| loose polarscale _ _ parallel computin _ g ct limit high _ _ _ | 8.0 | 500 000 | [0- 10000000] | No | Specifies the high watermark that is controlled by the pipeline. |
| loose polarscale _ _ parallel computin _ g ct limit low _ _ _ | 8.0 | 500 00 | [0- 2000000] | No | Specifies the low watermark that is controlled by the pipeline. |
| loose polarscale _ _ parallel computin _ g order row num _ _ _ | 8.0 | 100 000 | [10- 10000000] | No | The number of rows processed in each pipeline unit for parallel sort operators. |
| loose polarscale _ _ parallel computin _ g read consisten _ _ t | 8.0 | 1 | [0\|1] | No | Specifies whether to enable the ReadView feature. If you set this parameter to 0, the ReadView feature is disabled. If you set this parameter to 1, the ReadView feature is enabled. |
| loose polarscale _ _ parallel computin _ g row num _ _ | 8.0 | 100 00 | [10- 200000] | No | The number of rows processed in each pipeline unit for parallel scan operators. |
| loose polarscale _ _ parallel computin _ g switch _ | 8.0 | 1 | [0\|1] | No | Specifies whether to enable the parallel computing feature. If you set this parameter to 0, the parallel computing feature is disabled. If you set this parameter to 1, the parallel computing feature is enabled. |
| loose polarscale _ _ parallel computin _ g thread num _ _ | 8.0 | 32 | [1-128] | No | Specifies the degree of parallelism. |
| loose polarscale _ _ parallel computin _ g trace _ | 8.0 | 0 | [0\|1] | No | Specifies whether to enable the trace feature. If you set this parameter to 0, the trace feature is disabled. If you set this parameter to 1, the trace feature is enabled. |
| loose rds audit l _ _ _ og event buffer _ _ _ size | 8.0 | 204 8 | [0-32768] | No | The maximum size of SQL statements in the ApsaraDB RDS audit log. |

| loose rds kill con _ _ _ nections | MyS QL 8.0 and MyS QL 5.7 | 20 | [0- 18446744 07370955 1615] | No | The number of additional connections for users that are specified by rds user with kill option. _ _ _ _ |
|---|---|---|---|---|---|
| loose rds set co _ _ _ nnection id enab _ _ led | 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable the patches about proxy connection IDs. |
| loose recycle bin _ _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [OFF\|ON] | No | Specifies whether to enable the recycle bin. |
| loose recycle bin _ _ retention _ | MyS QL 8.0 and MyS QL 5.7 | 604 800 | [86400- 1209600] | No | The retention period in the recycle bin. Unit: seconds. |
| loose recycle sch _ _ eduler | MyS QL 8.0 and MyS QL 5.7 | OFF | [OFF\|ON] | No | Specifies whether to clean up threads. |
| loose sql safe up _ _ _ dates | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | If this parameter is enabled, an error occurs when keys are not used in the WHERE or LIMIT clause of the UPDATE or DELETE statement. |

| loose thread poo _ _ l enabled _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether to enable thread pooling. |
|---|---|---|---|---|---|
| loose thread poo _ _ l oversubscribe _ | MyS QL 8.0 and MyS QL 5.7 | 32 | [10-64] | No | The number of additionally active worker threads in each group. |
| loose thread poo _ _ l size _ | MyS QL 8.0 and MyS QL 5.7 | 4 | [1-16] | No | The number of thread groups in the thread pool. |
| loose validate pa _ _ ssword check us _ _ er name _ | 5.7 | ON | [ON\|OFF] | No | When you set this parameter to ON, the password can be the same as the username. |
| loose validate pa _ _ ssword length _ | MyS QL 8.0 and MyS QL 5.7 | 8 | MySQL 8.0: 1 to 32 MySQL 5.7: 0 to 256 | No | The minimum length of the password. If you set this parameter to 8, the length of the password must be greater than or equal to 8. |
| loose validate pa _ _ ssword mixed ca _ _ se count _ | MyS QL 8.0 and MyS QL 5.7 | 1 | MySQL 8.0: 0 to 32 MySQL 5.7: 0 to 256 | No | If the password policy is MEDIUM or STRONG, this parameter specifies the minimum number of lowercase and uppercase letters in the password specified by validate password. The total _ number of lowercase and uppercase letters in a password must be greater than or equal to the value of this parameter. |
| loose validate pa _ _ ssword number c _ _ ount | MyS QL 8.0 and MyS QL 5.7 | 1 | MySQL 8.0: 0 to 32 MySQL 5.7: 0 to 256 | No | The number of digits in the password. |

| loose validate pa _ _ ssword policy _ | 5.7 | 1 | [0\|1\|2] | No | The password policy in MySQL. Valid values consist of two types: 0, 1, and 2; LOW, MEDIUM, and STRONG. 0 or LOW: a loose policy. The password must contain at least one character, and the length of the password must be greater than or equal to the value of loose validate password length. _ _ _ 1 or MEDIUM: a medium policy. The password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character. In addition, the length of the password must be greater than or equal to the value of loose validate password length. _ _ _ 2 or STRONG: a strict policy. The password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character. The length of the password must be greater than or equal to the value of loose validate password length. In _ _ _ addition, the system checks whether the password exists in the dictionary file. |
|---|---|---|---|---|---|
| loose validate pa _ _ ssword special c _ _ har count _ | MyS QL 8.0 and MyS QL 5.7 | 1 | MySQL 8.0: 0 to 32 MySQL 5.7: 0 to 256 | No | The number of special characters in the password. |
| low priority upda _ _ tes | MyS QL 8.0 and MyS QL 5.7 | 0 | [0\|1] | No | If you set this parameter to 1, all INSERT, UPDATE, DELETE, and LOCK TABLE WRITE statements wait until no pending SELECT or LOCK TABLE READ statements exist on the required table. This parameter is suitable for storage engines that use only table-level locking, such as MyISAM, MEMORY, and MERGE. This parameter is formerly known as sql low priority updates. _ _ _ |
| lower case table _ _ names _ | 5.7 | 1 | [0\|1] | Yes | If you set this parameter to 1, table names are stored in lowercase on the disk and table names are not case- sensitive. If you use a file system that is not case-sensitive, we recommend that you set this parameter to 2. |

| master verify ch _ _ ecksum | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | If you enable this parameter, the primary server verifies checksums when it reads data from the binary log. By default, this parameter is disabled. In this case, the primary server uses the event length from the binary log to verify events. This ensures that only complete events can be read from the binary log. |
|---|---|---|---|---|---|
| max allowed pac _ _ ket | MyS QL 8.0 and MyS QL 5.7 | 107 374 182 4 | [16384- 10737418 24] | No | The maximum size of a packet, a generated string, or an intermediate string. Unit: bytes. |
| max binlog cach _ _ e size _ | MyS QL 8.0 and MyS QL 5.7 | 184 467 440 737 095 475 20 | [4096- 18446744 07370954 7520] | No | The size of the transaction cache. The visibility of max binlog cache size to _ _ _ sessions matches that of binlog cache size. _ _ |
| max binlog stmt _ _ cache size _ _ | MyS QL 8.0 and MyS QL 5.7 | 184 467 440 737 095 475 20 | [4096- 18446744 07370954 7520] | No | If the memory that is required for non- transactional statements is greater than the value of this parameter, an error is reported. Minimum value: 4096. Maximum value and default value: 4 GB for 32-bit platforms and 16 exabytes (EB) for 64-bit platforms. |
| max connect err _ _ ors | MyS QL 8.0 and MyS QL 5.7 | 100 | [0- 42949672 95] | No | If the number of failed connection requests caused by interrupted consecutive connection requests from a host is greater than the value of this parameter, the server blocks the requests from the host. To resolve this issue, you can flush the host cache. |
| max error count _ _ | MyS QL 8.0 and MyS QL 5.7 | 64 | [0-65535] | No | The maximum number of error, warning, and information messages to be stored for display by the SHOW ERRORS and SHOW WARNINGS statements. The value is the same as the number of condition areas in the diagnostics area. You can execute the GET DIAGNOSTICS statement to diagnose the same number of conditions. |

| max execution ti _ _ me | 8.0 | 0 | [0- 42949672 95] | No | The execution timeout of the statement. If this threshold is exceeded, the statement is interrupted. |
|---|---|---|---|---|---|
| max heap table _ _ _ size | MyS QL 8.0 and MyS QL 5.7 | 671 088 64 | [16384- 18446744 07370954 752] | No | The maximum size to which a user- created MEMORY table can be increased. This parameter is used to calculate the MAX ROWS value in the MEMORY table. _ This parameter is suitable only if you execute the CREATE TABLE statement to recreate the table or execute the ALTER TABLE or TRUNCATE TABLE statement to modify the table. Otherwise, this parameter has no effect on any existing MEMORY table. If your server is restarted, the maximum size of an existing MEMORY table is set to the value of max heap table size. _ _ _ |

| max join size _ _ | MyS QL 8.0 and MyS QL 5.7 | M y S Q L 8. 0: 1 8 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 6 1 5 M y S Q L 5. 7: 1 8 4 4 6 7 4 4 0 7 3 7 0 9 5 0 0 0 0 0 | [1- 18446744 07370955 1615] | No | If the number of rows or row groups or the number of disk queries is greater than the value of this parameter, the statements cannot be executed. If you execute single-table statements, this parameter specifies the maximum number of rows. If you execute multi- table statements, this parameter specifies the maximum number of row groups. This parameter helps identify the statements that do not properly use keys and thus require a long period of time. If you want to perform join operations that lack a WHERE clause, require a long period of time, or return millions of rows, we recommend that you configure this parameter. |
|---|---|---|---|---|---|

| max length for s _ _ _ ort data _ | MyS QL 8.0 and MyS QL 5.7 | 102 4 | [0-838860] | No | The cutoff on the size of an index value, which determines the file sorting algorithm. |
|---|---|---|---|---|---|
| max points in ge _ _ _ ometry | MyS QL 8.0 and MyS QL 5.7 | 655 36 | [3- 1048576] | No | The maximum value of points per circle _ _ in the ST Buffer Strategy() function. _ _ |
| max prepared st _ _ mt count _ | MyS QL 8.0 and MyS QL 5.7 | 163 82 | [0- 1048576] | No | The total number of prepared statements in the server. |
| max seeks for k _ _ _ ey | MyS QL 8.0 and MyS QL 5.7 | 184 467 440 737 095 000 00 | [1- 18446744 07370955 1615] | No | The assumed maximum number of times that rows are identified based on keys. When the MySQL optimizer scans an index, the MySQL optimizer assumes that the number of times that keys are checked to identify required rows is less than or equal to the value of this parameter, regardless of the cardinality of the index. You can set this parameter to a small value, such as 100, to force the MySQL optimizer to prefer index scans over table scans. |

| max sort length _ _ | MyS QL 8.0 and MyS QL 5.7 | 102 4 | [4- 8388608] | No | The number of bytes that are used to sort data values. The server uses only the first max sort length bytes of each _ _ value. As a result, the bytes except the first max sort length bytes are _ _ considered the same for GROUP BY, ORDER BY, and DISTINCT operations. |
|---|---|---|---|---|---|
| max sp recursio _ _ n depth _ | MyS QL 8.0 and MyS QL 5.7 | 0 | [0-255] | No | The number of times that a given stored procedure may be recursively called. Default value: 0, which indicates that recursion of stored procedures is disabled. Maximum value: 255. |
| max write lock c _ _ _ ount | MyS QL 8.0 and MyS QL 5.7 | 102 400 | [1-102400] | No | If the number of write locks reaches the value of this parameter, read locks are allowed to run. |
| metadata locks c _ _ ache size _ | 5.7 | 102 4 | [1- 1048576] | No | The size of the metadata lock cache. The server uses this cache to prevent the creation and destruction of synchronization objects. This parameter is helpful on costly systems such as Windows XP. |
| min examined ro _ _ w limit _ | MyS QL 8.0 and MyS QL 5.7 | 0 | [0- 42949672 95] | No | If the number of rows checked by a query is less than the value of this parameter, the query is not recorded to the slow query log. |

| myisam sort buff _ _ er size _ | MyS QL 8.0 and MyS QL 5.7 | 262 144 | [262144- 16777216] | No | The size of the buffer that is allocated when the REPAIR TABLE statement is executed to sort MyISAM indexes or when the CREATE INDEX or ALTER TABLE statement is executed to create indexes. |
|---|---|---|---|---|---|
| mysql native pas _ _ sword proxy use _ _ rs | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether the mysql native password built-in _ _ authentication extension supports proxy users. The effect of this parameter varies based on check proxy users. _ _ |
| net buffer length _ _ | MyS QL 8.0 and MyS QL 5.7 | 163 84 | [1024- 1048576] | No | Each client thread is associated with a connection buffer and a result buffer. This parameter specifies the minimum size of the connection buffer or result buffer. You can increase the size of the connection buffer or result buffer to the value of max allowed packet based on _ _ your business requirements. After each SQL statement is executed, the size of the result buffer is decreased to the value of net buffer length. _ _ |
| net read timeout _ _ | MyS QL 8.0 and MyS QL 5.7 | 30 | [1- 18446744 07370955 1615] | No | The number of seconds to wait for more data from a connection before the read operation is aborted. |
| net retry count _ _ | MyS QL 8.0 and MyS QL 5.7 | 10 | [1- 42949672 95] | No | The number of retries before a read or write operation on a communication port is aborted if the operation is interrupted. |
| net write timeou _ _ t | MyS QL 8.0 and MyS QL 5.7 | 60 | [1- 18446744 07370955 1615] | No | The number of seconds to wait for a block to be written to a connection before the write operation is aborted. |

| ngram token siz _ _ e | MyS QL 8.0 and MyS QL 5.7 | 2 | [0-20] | Yes | The n-gram token size for the n-gram full-text parser. This parameter is read- only and can only be modified at startup. Default value: 2 (2-tuples). Maximum value: 10. |
|---|---|---|---|---|---|
| old passwords _ | 5.7 | 0 | [0\|2] | No | The password hashing method of the PASSWORD() function. This parameter also specifies the password hashing method for the CREATE USER and GRANT statements for which a password is specified in the IDENTIFIED BY clause. |
| open files limit _ _ | MyS QL 8.0 and MyS QL 5.7 | 655 35 | [1- 18446744 07370955 1615] | Yes | If you set this parameter to a value other than 0, mysqld uses the value to reserve file descriptors for the use with setrlimit(). |
| optimizer prune l _ _ evel | MyS QL 8.0 and MyS QL 5.7 | 1 | [0\|1] | No | The heuristics method applied during query optimization to prune some less- promising plans from the optimizer search space. If you set this parameter to 0, the heuristics method is disabled, and the optimizer performs an exhaustive search. If you set this parameter to 1, the optimizer prunes the plans based on the number of rows retrieved by intermediate plans. |
| optimizer search _ depth _ | MyS QL 8.0 and MyS QL 5.7 | 62 | [0-62] | No | The maximum depth of a search performed by the query optimizer. If you set this parameter to a value that is greater than the number of relations in the result of a query, a better query plan is used, but it requires a long period of time to generate an execution plan for a query. If you set this parameter to a value that is smaller than the number of relations in the result of a query, an execution plan is generated in a quick manner, but the query plan is not optimal. If you set this parameter to 0, the system automatically uses an appropriate value. |

| optimizer trace li _ _ mit | MyS QL 8.0 and MyS QL 5.7 | 1 | [0- 42949672 95] | No | The maximum number of optimizer traces to display. |
|---|---|---|---|---|---|
| optimizer trace _ _ max mem size _ _ | MyS QL 8.0 and MyS QL 5.7 | 163 84 | [0- 42949672 95] | No | The maximum cumulative size of stored optimizer traces. |
| optimizer trace o _ _ ffset | MyS QL 8.0 and MyS QL 5.7 | -1 | [- 21474836 48- 21474836 47] | No | The offset of optimizer traces to display. |
| opt indexstat _ | 8.0 | OFF | [ON\|OFF] | Yes | Specifies whether to collect statistics on indexes. |
| opt tablestat _ | 8.0 | OFF | [ON\|OFF] | Yes | Specifies whether to collect statistics on tables. |
| performance poi _ nt iostat interval _ _ | 8.0 | 2 | [0-60] | No | The interval at which I/O statistics are collected. Unit: milliseconds. |
| performance poi _ nt iostat volume _ _ size _ | 8.0 | 100 00 | [0-100000] | Yes | The maximum capacity of I/O statistics that can be collected. Unit: number of slots. |
| performance poi _ nt lock rwlock e _ _ _ nabled | 8.0 | ON | [ON\|OFF] | No | Specifies whether to enable the performance optimization feature for read or write locks. |

| performance sch _ ema | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/85 899 345 92, 1)} | [0-1] | Yes | Specifies whether to enable Performance Schema. When the server starts, you can configure this parameter based on your business requirements. You can set this parameter to 1 to enable Performance Schema. You can also set this parameter to 0 to disable Performance Schema. |
|---|---|---|---|---|---|
| preload buffer si _ _ ze | MyS QL 8.0 and MyS QL 5.7 | 327 68 | [1024- 10737418 24] | No | The size of the buffer that is allocated to preload indexes. |
| query alloc block _ _ size _ | MyS QL 8.0 and MyS QL 5.7 | 819 2 | [1024- 16384] | No | The size of memory blocks that are allocated to created objects during statement parsing and execution. Unit: bytes. |
| query cache limi _ _ t | 5.7 | 104 857 6 | [1- 1048576] | No | The maximum number of bytes that can be cached in a result. |
| query cache min _ _ res unit _ _ | 5.7 | 102 4 | [512- 18446744 07370955 1608] | No | The minimum size of a block allocated by the query cache. Unit: bytes. |

| query cache size _ _ | 5.7 | 0 | [0- 10485760 000] | No | The amount of memory that is allocated to cache query results. The default value 0 indicates that query caching is disabled. Valid values: multiples of 1024. If the value is not a multiple of 1024, the value is rounded to the nearest multiple. Unit: bytes. |
|---|---|---|---|---|---|
| query cache typ _ _ e | 5.7 | 0 | [0\|1\|2] | Yes | 0: does not cache or retrieve the query results. 1: caches all results except for the results of SELECT SQL NO CACHE. _ _ 2: caches only the results of SELECT SQL CACHE. _ |
| query cache wlo _ _ ck invalidate _ | 5.7 | OFF | [ON\|OFF] | No | In most cases, if a client acquires a write lock on a MyISAM table, other clients are not prohibited from issuing statements that read data from the table if the query results exist in the query cache. If you set this parameter to ON, the acquisition of a write lock on a table causes the queries that reference the table in the query cache to be invalid. In this case, other clients that attempt to access the table must wait when the lock is in effect. |
| query prealloc si _ _ ze | MyS QL 8.0 and MyS QL 5.7 | 819 2 | [8192- 1048576] | No | The size of the persistent buffer that is used for statement parsing and execution. This buffer is not released between statements. If complex queries are being run, a large value of query prealloc size helps improve query _ _ performance because the large value reduces the need for the server to allocate memory during queries. Unit: bytes. |
| range alloc block _ _ size _ | MyS QL 8.0 and MyS QL 5.7 | 409 6 | [4096- 18446744 07370955 1615] | No | The size of blocks that are allocated when range optimization is performed. |

| range optimizer _ _ max mem size _ _ | MyS QL 8.0 and MyS QL 5.7 | 838 860 8 | [0- 18446744 07370955 1615] | No | The limit on memory consumption for the range optimizer. The value 0 indicates that no limits are imposed. If an execution plan selected by the optimizer uses the range access method but the optimizer estimates that the amount of memory required for this method may exceed the limit, the optimizer abandons the execution plan and selects other plans. |
|---|---|---|---|---|---|
| rds reserved con _ _ nections | 5.7 | 512 | [0-512] | No | The number of connections that are reserved for maintenance users. |
| read buffer size _ _ | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76* 128, 262 144) } | [8200- 21474795 52] | No | The size of the buffer allocated for each table that is scanned by a thread for sequential scans on a MyISAM table. Unit: bytes. If the value of this parameter is not a multiple of 4 KB, the value is rounded to the nearest multiple of 4 KB. |
| relay log recover _ _ y | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | Yes | If you set this parameter to ON, the automatic relay log recovery feature will be enabled immediately after the server is started. This global variable is read- only at runtime. |
| session track gti _ _ ds | MyS QL 8.0 and MyS QL 5.7 | OFF | [OFF\|OWN _ GTID\|ALL _ GTIDS] | No | Specifies whether to capture global transaction identifiers (GTIDs) and return the tracers of the GTIDs in the OK packet. If this parameter is enabled, the specified GTID is captured by the tracer and appended to the OK packet at the end of a transaction. |
| sha256 password _ proxy users _ _ | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether the sha256 password _ built-in authentication extension supports proxy users. This parameter takes effect only when check proxy users is enabled. _ _ |

| show compatibili _ ty 56 _ | 5.7 | OFF | [ON\|OFF] | No | The INFORMATION SCHEMA table _ contains information about system variables and status variables. The Performance Schema table is used to replace the INFORMATION SCHEMA table _ that is deprecated as of MySQL 5.7.6 and is removed from later MySQL versions. |
|---|---|---|---|---|---|
| show old tempor _ _ als | MyS QL 8.0 and MyS QL 5.7 | OFF | [ON\|OFF] | No | Specifies whether to include comments in the output of SHOW CREATE TABLE to mark the temporal columns of the types that are supported in versions earlier than MySQL 5.6.4. The temporal columns indicate TIMESTAMP columns that do not support fractional seconds, TIME columns, and DATETIME columns. This parameter is disabled by default. If this parameter is enabled, the output of SHOW CREATE TABLE includes the comments to mark the temporal columns. |
| slave net timeou _ _ t | MyS QL 8.0 and MyS QL 5.7 | 60 | [15-300] | No | The number of seconds for the primary server to wait for more data. If this threshold is exceeded, the secondary server considers the connection disconnected, terminates read operations, and then tries to reconnect. |
| slave parallel typ _ _ e | MyS QL 8.0 and MyS QL 5.7 | LOG ICAL CL _ OCK | [DATABAS E\|LOGICAL CLOCK] _ | Yes | The policy used to determine the transactions to be executed in parallel on the secondary server. This parameter is not suitable for the secondary server for which multithreading is disabled. If slave preserve commit order is set to 1, _ _ _ the value of this parameter must be LOGICAL CLOCK. _ |
| slave type conve _ _ rsions | MyS QL 8.0 and MyS QL 5.7 | - | [SPACE\|AL L LOSSY\|A _ LL NON L _ _ OSSY\|ALL _ SIGNED\|AL L UNSIGNE _ D] | Yes | The type conversion mode on the secondary server when row-based replication is used. |
| slow launch time _ _ | MyS QL 8.0 and MyS QL 5.7 | 2 | [1-1024] | No | If the time that is required to create a thread exceeds the value of this parameter, the server increases the value of slow launch threads. _ _ |

| slow query log _ _ | MyS QL 8.0 and MyS QL 5.7 | ON | [ON\|OFF] | No | Specifies whether slow query logging is enabled. If this parameter is not used or set to ON, slow query logging is enabled. If this parameter is not specified or set to OFF, slow query logging is disabled. |
|---|---|---|---|---|---|
| sort buffer size _ _ | MyS QL 8.0 and MyS QL 5.7 | 262 144 | [32768- 42949672 95] | No | The size of the buffer allocated to each session that must perform a sort operation. |
| sql mode _ | MyS QL 8.0 and MyS QL 5.7 | ONL Y F _ ULL _ GRO UP _ BY,S TRIC T T _ RAN S T _ ABL ES,N O Z _ ERO IN _ _ | (SPACE\|RE AL AS FLO _ _ AT\|PIPES A _ S CONCAT _ \|ANSI QUO _ TES\|IGNOR E SPACE\|O _ NLY FULL _ _ GROUP BY _ \|NO UNSIG _ NED SUBT _ RACTION\|N O DIR IN _ _ _ CREATE\|A NSI\|NO AU _ TO VALUE _ ON ZERO\| _ _ NO BACKS _ LASH ESC _ APES\|STRI CT TRANS _ _ TABLES\|ST RICT ALL _ _ TABLES\|NO ZERO IN _ _ _ DATE\|NO _ ZERO DAT _ E\|ALLOW I _ NVALID D _ ATES\|ERR OR FOR DI _ _ VISION BY _ ZERO\|TRA _ DITIONAL\| HIGH NOT _ PRECEDE _ NCE\|NO E _ NGINE SU _ BSTITUTIO N\|PAD CH _ AR TO FUL _ _ L LENGTH) _ (,REAL AS _ _ FLOAT\|,PIP ES AS CO _ _ NCAT\|,ANS | No | The SQL mode that defines the SQL syntax supported for MySQL and the type of data validation. |

|   |   | DAT E,N O Z _ ERO DA _ TE,E RRO R F _ OR _ DIVI SIO N B _ Y Z _ ERO ,NO _ EN GIN E S _ UBS TITU TIO N | I QUOTES\|, _ IGNORE SP _ ACE\|,ONLY FULL GRO _ _ UP BY\|,NO _ UNSIGNE _ D SUBTRA _ CTION\|,NO DIR IN C _ _ _ REATE\|,AN SI\|,NO AUT _ O VALUE _ _ ON ZERO\|, _ NO BACKS _ LASH ESC _ APES\|,STRI CT TRANS _ _ TABLES\|,S TRICT ALL _ TABLES\|, _ NO ZERO I _ _ N DATE\|,N _ O ZERO D _ _ ATE\|,ALLO W INVALID _ DATES\|,E _ RROR FOR _ DIVISION _ _ BY ZERO\|, _ TRADITION AL\|,HIGH _ NOT PREC _ |   |   |
|---|---|---|---|---|---|
|   |   |   | EDENCE\|,N O ENGINE _ _ SUBSTITUT ION\|,PAD _ CHAR TO _ _ FULL LENG _ TH)* |   |   |
| stored program _ _ cache | MyS QL 8.0 and MyS QL 5.7 | 256 | [16- 524288] | No | The soft upper limit on the number of cached stored procedures for each connection. This parameter is specified based on the number of stored procedures in the caches that the MySQL server uses for stored procedures and stored functions. |
| sync master info _ _ | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [0- 18446744 07370955 1615] | No | The effects of this parameter on a secondary server for replication vary based on the value (FILE or TABLE) of master info repository that is specified _ _ for the secondary server. |

| sync relay log in _ _ _ fo | MyS QL 8.0 and MyS QL 5.7 | 100 00 | [0- 18446744 07370955 1615] | No | This parameter setting immediately takes effect for all replication channels, including running channels. |
|---|---|---|---|---|---|
| table definition c _ _ ache | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24* 512, 204 8) } | [400- 524288] | No | The number of table definitions that can be stored in the definition cache. The table definitions are from a .frm file. If you use a large number of tables, you can create a large table definition cache to speed up the opening of tables. The table definition cache does not use file descriptors and occupies less storage than a standard table cache. Minimum value: 400. Default value: 400. |
| table open cach _ _ e | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24* 256, 204 8) } | [1-524288] | No | The number of open tables for all threads. A large value increases the number of file descriptors that mysqld requires. You can check Opened tables _ to determine whether to increase the table cache. For more information, see Server status variables. If the value of Opened tables is large and you do not _ frequently use FLUSH TABLES, we recommend that you set this parameter to a large value. FLUSH TABLES forcefully closes all tables and opens the tables again. |

| table open cach _ _ e instances _ | MyS QL 8.0 and MyS QL 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 16)} | [1-64] | Yes | The number of open table cache instances. To improve scalability by reducing contention among sessions, the system can partition the open table cache into smaller cache instances. The number of the smaller cache instances is calculated by using the following formula: Value of table open cache/Value of _ _ table open cache instances. A session _ _ _ needs to lock only one instance and access the instance to execute DML statements. This segments cache access among instances, improving execution performance of the statements that use the cache when a large number of sessions access tables. DDL statements still need to lock the entire cache, but the frequency to use DDL statements is much less than the frequency to use DML statements. |
|---|---|---|---|---|---|
| temptable max r _ _ am | 8.0 | 107 374 182 4 | [2097152- 10737418 2400] | No | The maximum amount of memory that the TempTable storage engine can allocate from random-access memory (RAM) before data is stored to the disk. Unit: bytes. |
| thread cache siz _ _ e | MyS QL 8.0 and MyS QL 5.7 | M y S Q L 8. 0: 1 0 0 M y S Q L 5. 7: 2 5 6 | [0-16384] | No | The number of threads that are cached by the server for reuse. If a client disconnects and the number of client threads in the cache is less than the value of thread cache size, the threads _ _ are stored in the cache. Requests for threads are satisfied by reusing threads in the cache if possible. A thread is created only when the cache is empty. If a large number of new connections are established, you can increase the value of this parameter to improve performance. In most cases, if a thread is implemented in a better manner, this parameter does not significantly improve performance. However, if your server processes hundreds of connections per second, we recommend that you set thread cache size to a large value. This _ _ way, most new connections can use cached threads. You can check the differences between Connections and Threads created to view the caching _ efficiency. |

| thread stack _ | MyS QL 8.0 and MyS QL 5.7 | 262 144 | [131072- 18446744 07370955 1615] | Yes | The stack size of each thread. The default value is 192 KB. If you use a 64- bit operating system, the default value is 256 KB. The default value is enough for standard operations. If the stack size of a thread is set to a small value, the following items are affected: the capability of the server to process complex SQL statements, the recursion depth of stored procedures, and memory-consuming operations. |
|---|---|---|---|---|---|
| tls version _ | MyS QL 8.0 and MyS QL 5.7 | TLS v1.2 | [TLSv1,TLS v1.1,TLSv1 .2\|TLSv1,T LSv1.1\|TLS v1.2] | Yes | The version of the protocol that the server can use to encrypt connections. The value of this parameter is a comma- separated list that contains one or more protocol versions. The protocols that can be specified for this parameter depend on the SSL library used to compile MySQL. |
| tmp table size _ _ | MyS QL 8.0 and MyS QL 5.7 | 209 715 2 | [262144- 13421772 8] | No | The maximum size of the internal in- memory temporary table. |
| transaction alloc _ block size _ _ | MyS QL 8.0 and MyS QL 5.7 | 819 2 | [1024- 131072] | No | The amount of memory that is allocated to a memory pool to process each additional transaction. Unit: bytes. For more information, see the description of transaction prealloc size. _ _ |
| transaction isolat _ ion | MyS QL 8.0 and MyS QL 5.7 | REA D- COM MITT ED | [READ- UNCOMMIT TED\|READ- COMMITTE D\|REPEATA BLE- READ\|SERI ALIZABLE] | No | The transaction isolation level. |

| transaction preal _ loc size _ | MyS QL 8.0 and MyS QL 5.7 | 409 6 | [1024- 131072] | No | The initial size of the memory pool for a transaction. Unit: bytes. The memory pool is used to allocate transaction- related memory. If each allocation cannot be satisfied from the pool because the pool does not have sufficient memory, the size of the pool is increased by the value of transaction alloc block size. When the _ _ _ transaction ends, the pool is truncated to transaction prealloc size bytes. _ _ |
|---|---|---|---|---|---|
| updatable views _ _ with limit _ | MyS QL 8.0 and MyS QL 5.7 | YES | [YES\|NO] | No | Specifies whether a view can be updated when the LIMIT clause is used in updates and when the view does not contain all columns of the primary key defined in the underlying table. In most cases, these updates are generated by GUI tools. An update can be an UPDATE or DELETE statement. The primary key indicates a primary key, or a UNIQUE index in which no column can contain NULL. |
| wait timeout _ | MyS QL 8.0 and MyS QL 5.7 | 864 00 | [1- 31536000] | No | The period of time that the server waits for activity on a non-interactive connection before the server closes the non-interactive connection. Unit: seconds. |

### 5.10 Read-only instances

#### 5.10.1 Overview of read-only instances

ApsaraDB RDS for MySQL allows you to create read-only instances. In scenarios where an instance has a small number of write requests but a large number of read requests, you can create read-only instances to distribute database access loads away from the primary instance. This topic describes the features and limits of read-only instances. To scale up the reading capability and distribute database access loads, you can create one or more read-only instances in a region. Read-only instances can increase the application throughput when a large amount of data is being read. A read-only instance with a single physical node and no backup node uses the native replication capability of MySQL to synchronize changes from the primary instance to all its read-only instances. Read-only instances must be in the same region as the primary instance but do not have to be in the same zone as the primary instance. The following figure shows the topology of read-only instances.
**Read-only instances have the following features**:
Specifications of a read-only instance can be different from those of the primary instance and can be changed at any time. This facilitates elastic scaling. Read-only instances do not require account or database maintenance. Account and database information is synchronized from the primary instance. The whitelists of read-only instances can be independently configured. System performance monitoring is provided. ApsaraDB RDS provides up to 20 system performance monitoring views, including those for disk capacity, IOPS, connections, CPU utilization, and network traffic. You can view the load of instances. ApsaraDB RDS provides a variety of optimization recommendations, such as storage engine check, primary key check, large table check, and check for excessive indexes and missing indexes. You can optimize your databases based on the optimization recommendations and specific applications.

#### 5.10.2 Create a read-only instance

You can create read-only instances of different specifications based on your business requirements.

**Usage notes**

A maximum of five read-only instances can be created for a primary instance. Read-only instances do not support backup settings or temporary backup. Read-only instances do not support instance restoration. Data migration to read-only instances is not supported. Read-only instances do not support database creation or deletion. Read-only instances do not support account creation, deletion, authorization, or password changes. After a read-only instance is created, you cannot restore data by directly overwriting the data of its primary instance with a backup set.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the **Instance Distribution** section on the right side of the **Basic Information** page,
click **Add**.
4. On the **Create Read-only ApsaraDB RDS Instance** page, configure the parameters for
the read-only instance.

| Section | Parameter | Description |
|---|---|---|
| Area | Region | The region in which you want to create the read- only ApsaraDB RDS instance. |
| Specification Configuration | Database Type | The database type of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Database Version | The version of the database engine for the read- only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Series | Read-only Instance is always selected. |
|   | Specifications | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time to facilitate flexible upgrade and downgrade. |
|   | Storage Capacity | The storage capacity of the read-only instance. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type and storage capacity as the primary instance for the read- only instance. Valid values: 20 to 6000. Unit: GB. The value is in 1 GB increments. |
| Network Type | Network Type | The network type of the read-only instance. It must be the same as that of the primary instance and cannot be changed. |
|   | Private network vpc | The virtual private cloud (VPC) in which you want to create the read-only instance. This parameter is required when Network Type is set to Proprietary Network. |
| Document Version: 2026 | 0629 10 |   |

|   | Switch vswitch | The vSwitch in the VPC. This parameter is required when Network Type is set to Proprietary Network. |
|---|---|---|

5. After you complete the configuration, click **Submit**.

#### 5.10.3 View details of read-only instances

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instance List page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View details of a read-only instance from the Instance List**

**page**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, click the ID
of the read-only instance that you want to view to go to the **Basic Information** page.

**Note**

In the instance list, the **Instance type** column of read-only instances displays **Read-**
**only instance**.

**View details of a read-only instance from the Basic Information**

**page of the primary instance**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. On the **Basic Information** page, move the pointer over the number to the right of **Read-**
**only Instance** in the **Instance Distribution** section. The ID of the read-only instance is
displayed.
4. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

### 5.11 Manage instances in the recycle bin

**recycle bin**

This topic describes how to recreate or destroy an ApsaraDB RDS instance in the recycle bin.

**Usage notes**

All ApsaraDB RDS for MySQL instances, except for the following instances, are moved to the recycle bin after they are manually released: Instances that are manually released within seven days after they are created. Instances that are **read-only**.

**Recreate an instance**

If you manually release an ApsaraDB RDS instance that runs for more than seven days, backup files of the instance are retained for another eight days. Within the eight-day retention period, you can create another instance and restore data from the backup files to the new instance. Instance backups are no longer retained on the 9th day after the instance is released.
1. Log in to the ApsaraDB RDS console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Recycle Bin**.
3. Find the released instance and click **Reconstruction Recovery** in the Operation column.
4. On the **RDS restoration** page, specify **Storage space** and **Network Type** for the new
instance and click **Submit**.

**Note**

If you set **Network Type** to **Proprietary Network**, you must configure a **VPC** and a **vSwitch**. Other configurations remain the same as the original instance and cannot be changed.

**Destroy an instance**

You can destroy an ApsaraDB RDS instance that is no longer needed in the recycle bin.

**Warning**

After you destroy an instance, **all** the backup files of the instance are destroyed, including regular data backup files, archived backup files, and log backup files. The destroyed backup files **cannot be restored**. Proceed with caution.
1. Log in to the ApsaraDB RDS console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Recycle Bin**.
3. Find the released instance and click **Destroy immediately** in the Operation column. In the
message that appears, click **OK**.

### 5.12 Manage tags

If you have a large number of instances, you can create multiple tags and add the tags to the instances. Then, you can query instances by tag. This topic describes how to manage tags.

**Usage notes**

A tag consists of a key-value pair. Each key must be unique for an Alibaba Cloud account in a region. This limit does not apply to the values of keys. You can add up to 20 tags to an instance. If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.

**Add tags**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, enter the tag key and tag value and click **OK**.

**Search for an instance by tag**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, click **Advanced Filter**.
3. You can search for your instance by **Instance ID /Name**, **VIP**, and **Tag Filtering**. Select a
tag from the **Filter by Tag** drop-down list.
4. After you select a tag, the instance list displays all instances that are bound with the tag.

**View the tags that are added to an instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, if a small number of tags are added to an instance, the
corresponding tags are displayed in the Tag column. If a large number of tags are added to an instance, move the pointer over the icon in the **Tag** column to view all the tags that are added to the instance.

**Remove a tag**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, click the
icon to the right of the tag and click **OK**.

## 6 Accounts

### 6.1 Language Detection

Detect the language of the input text. Supports automatic recognition of 23 languages. Best suited to short text such as search queries, product titles, and chat messages. Synchronous.

**Endpoint**

```
POST /ai/text/marco/language-detection
```

**Use cases**

Cross-border search -- detect the buyer's search-query language and route to the matching index. Title preprocessing -- detect source language automatically before calling the Text Translation API, so callers do not need to pass `SourceLanguage` . Chat routing -- forward users to native-language agents based on detected language.

**Quick start**

```java
import json data = json.dumps({ "SourceText": "Hello world" }) result = make_signed_request("/ai/text/marco/language-detection", data) print(result["Data"]["DetectedLanguage"]) # en
```

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceText | String | Yes | Text to identify. Up to ~1024 characters recommended; very short inputs (single tokens) have lower accuracy. |

**Response fields**

| Field | Type | Description |
|---|---|---|
| Code | String | Business status. Success when OK; otherwise see Error codes. |
| Message | String | Business message. |
| RequestId | String | Unique request identifier. |
| Success | Boolean | Whether the call succeeded. |

| psaraDB RDS for MySQL User G |   | ApsaraDB for RD |
|---|---|---|

| Field | Type | Description |
|---|---|---|
| Data.DetectedLanguage | String | Detected language code; see "Supported languages" below. |
| Data.UsageMap.RequestCount | Number | Request count for billing reconciliation. |

|   | Data.UsageMap.RequestCount |   |
|---|---|---|

**Response example**

`{`

```json
  "Code": "Success",
  "Message": "ok",
  "RequestId": "21570000-0000-0000-0000-000000000001",
  "Success": true,
  "Data": {
    "DetectedLanguage": "en",
    "UsageMap": { "RequestCount": 1 }
```

`}` `}`

**Supported languages (23)**

| ngali ( bn ), German ( de he ), Indonesian ( id ), It tch ( nl ), Polish ( pl ), Po krainian ( uk ), Urdu ( ur Traditional ( zh-tw ). |   | de |   |
|---|---|---|---|
|   | id |   |   |
|   |   |   | ), It ), Po |
|   | pl |   |   |

| lish ( | en |
|---|---|
| it |   |

|   | es |
|---|---|
| ja |   |

( `fr` ), Hebrew ( `he` ), Indonesian ( `id` ), Italian ( `it` ), Japanese ( `ja` ), Korean ( `ko` ),

| ms |   | ), |
|---|---|---|
| ( |   |   |

Malay ( `ms` ), Dutch ( `nl` ), Polish ( `pl` ), Portuguese ( `pt` ), Russian ( `ru` ), Thai ( `th` ),

**Error codes**

Common error codes: `InvalidParameter` (missing or empty `SourceText` ), `InternalError` (system busy). See Error codes for the full reference.

**What's next**

Text Translation API -- translate plain text. Text Correction API -- spelling correction.

### 6.2 Package Audit

Logistics package audit endpoint powered by a multimodal LLM (MLLM) plus a dedicated CV model. Submit a raw capture image and an annotated image (with manual bounding boxes) to receive a boolean decision plus a Chinese explanation. **Asynchronous**: submit the task to obtain a TaskId, then poll the unified async result endpoint. Built-in scene routing automatically detects background type (white / green) and bounding-box type (none / single / double) -- no scene flag required from the caller.

**Endpoint**

Asynchronous: submit the task to obtain a `TaskId` , then poll the unified async result endpoint ( `QueryAsyncTaskResult` ). See the official released API documentation for the submit endpoint path.

**Use cases**

Package bounding-box audit -- detect over-sized or under-sized bounding boxes in warehouse quality checks. Foreign-object detection -- flag fingers, keyboards, or auxiliary tools that interfere with package measurement. Multi-capture-environment support -- handles white-background with blue box, greenbackground with blue + red box, and other hardware setups. Receiving-line quality control -- replaces or augments manual outsourced review.

**Quick start**

```java
import json import time
# 1. Submit the audit task
submit_data = json.dumps({
    "RawImageUrl": "https://example.com/raw.jpg",
    "AnnotatedImageUrl": "https://example.com/annotated.jpg"
```

`})`

```python
submit_resp = make_signed_request("<package_audit_submit_endpoint>", submit_data) task_id = submit_resp["Data"]["TaskId"]
# 2. Poll the unified async query endpoint
while True:
    query_data = json.dumps({"TaskId": task_id})
    query_resp = make_signed_request("/ai/async/task/result", query_data)
    status = query_resp["Data"]["Status"]
    if status == "COMPLETED":
        result_obj = query_resp["Data"]["Result"]  # nested object
        print(result_obj["info"], "PASS" if result_obj["result"] else "REJECT")
        break
    elif status == "FAILED":
        print("Task failed")
        break
    time.sleep(5)
```

**Request parameters (Submit)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| RawImageUrl | String | Yes | Publicly accessible URL of the unannotated package capture image. Requirements: PNG / JPEG / JPG / BMP / WEBP; resolution <= 4000 x 4000; file size <= 10 MB. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| AnnotatedImageUrl | String | Yes | Publicly accessible URL of the annotated image (raw image with manual blue / red rectangle annotations overlaid). Same requirements as RawImageUrl . |

|   | AnnotatedImageUrl |
|---|---|

**Response fields**

**Submit response**

`{`

```json
  "Data": {
    "TaskId": "a8323ada-a196-9061-976f-90e38b27323a"
```

`},`

```json
  "RequestId": "F93D82E4-D0B6-1043-AC58-282597BC3C10",
  "Message": "Success",
  "Code": "success",
  "Success": true
```

`}`

**Query response (COMPLETED)**

`{`

```json
  "Data": {
    "Status": "COMPLETED",
    "UsageMap": { "ProcessingCount": "1" },
    "TaskId": "a8323ada-a196-9061-976f-90e38b27323a",
    "Result": {
```

`"info": "`审核通过`",`

```json
      "result": true,
      "usageMap": { "ProcessingCount": 1 }
```

`}` `},`

```json
  "RequestId": "BB79D551-60FA-16FB-A78C-88B0A881BEC4",
  "Message": "Success",
  "Code": "success",
  "Success": true
```

`}`

|   | Data.Result |
|---|---|
| result |   |

**Note**: `Data.Result` in the query response is a **nested object** (not a boolean). It contains
`result` (boolean), `info` (string), and `usageMap` .

**Decision values**

`Data.Result.info` returns one of the following Chinese strings:

| Data.Result.result | Data.Result.info (CN) | Meaning |
|---|---|---|

| Data.Result.result | Data.Result.info (CN) | Meaning |
|---|---|---|
| true | 审核通过 | Package capture passes every audit dimension. |
| false | 审核不通过:框选过大 | Bounding box is clearly larger than the actual package; recapture required. |
| false | 审核不通过:框选过小 | Bounding box is clearly smaller than the actual package; recapture required. |
| false | 审核不通过:存在异物 | A foreign object (finger, keyboard, etc.) is interfering with the capture. |

**Error codes**

| Common error codes: | InvalidParameter |
|---|---|
| DownstreamUnavailable |   |
| InputContentBlocked |   |

`DownstreamUnavailable` (image download failed or downstream model unavailable), `InputContentBlocked` (image triggered content safety review), `InternalError` (system busy). See Error codes for the full reference.

**Architecture**

**MLLM semantic understanding** -- the multimodal LLM handles scene-level semantic
understanding and foreign-object detection (fingers / keyboards / auxiliary tools).
**Dedicated CV model** -- a package-segmentation + IoU-evaluation model quantifies
bounding-box fit (over-sized / under-sized).
**Intelligent routing** -- built-in background-type recognition (white / green) and bounding-
box-type recognition (none / single / double) route the request to the appropriate audit subflow.

**What's next**

Error codes -- full error code reference. Rate limits -- QPS limits.

### 6.3 Product Material Optimization Pro

**Pro**

The **best-quality** tier of the one-click cross-platform material optimization service. Given a 1688 product URL, produce TEMU-ready titles, attributes, hero images, SKU images, detail images, and copy. Uses the official Best Quality workflow: full AI capability stack, preserves and localizes brand marketing assets, and emits category-specific assets (e.g., size charts) for apparel. Asynchronous.

**Endpoints**

**Submit optimization task**

```
POST /ai/material/optimization/pro
```

**Query optimization result**

```
POST /ai/material/optimization/pro/result
```

**Use cases**

High ASP, brand merchants, apparel / accessories / beauty / home -- categories that rely on marketing assets. Multi-language, multi-market localization. Scenarios needing category-specific assets (size chart, package weight/dimensions).

**Workflow**

The official Best Quality workflow:
1. Parse the 1688 product URL, extract all assets, diagnose gaps.
2. LLM compliance filtering, SEO keyword optimization, five-point bullets, multi-language
localized rewrite.
3. Images: invoke smart element detection / matting / removal / image translation Pro /
expansion / smart crop / upscale; remove non-compliant elements while **preserving and**
**rewriting marketing copy**.
4. Category-specific assets: apparel size charts, package weight/dimensions, etc.
5. Output a standardized material package via API and / or Excel export.

**Request parameters**

Pro and Lite share the same 31-field schema; the difference is the server-side workflow. See the Smart Image Generation API for the full schema. Pro typically enables `Ability=` `[1,2,3,4,5,6,7]` -- all 7 atomic capabilities.

**Response fields (query)**

Pro adds the following fields on top of Lite:

| Field | Type | Description |
|---|---|---|
| Data.Result.BulletPoints | String[] | Five-point bullets for detail- page selling points. |
| Data.Result.SizeChart | Object | Apparel size chart (when applicable); fields include size / bust / waist / length. |
| Data.Result.PackageInfo | Object | Package weight / dimension info (when applicable). |
| Data.Result.TranslatedImag es | Object[] | Marketing images localized through Image Translation Pro. |

|   | Data.Result.BulletPoints |
|---|---|

|   | Data.Result.TranslatedImag | O |
|---|---|---|
| es |   |   |

Shared fields ( `Status` , `Images` , `Title` , `Attributes` , `CategoryPath` , `UsageMap` ) are the same as Lite.

**Error codes**

See Error codes.

**What's next**

Product Material Optimization Lite -- lowest-cost tier. Smart Image Generation API -- detailed field schema for the 7 atomic capabilities.

### 6.4 Modify the permissions of an account

**account**

You can edit the account permissions of your ApsaraDB RDS instance at any time.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to manage and click **Change Permissions** in the **Actions**
column.

**Note**

You can only edit the permissions of standard accounts. The permissions of privileged accounts can only be reset to the default settings and cannot be changed to a specific set of permissions.
5. Configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Authorize Database | On the Edit Account Permissions tab, select a database in the left Unauthorized Databases section, and click Add to authorize the database. In the right Authorized Databases section, select a database and click Remove to remove the permissions from the database. |
| Set Account Permissions | You can set permissions on each database in the Authorized Databases section. You can also click the button such as Set All to Read/Write in the upper-right corner to set the permissions of the account on all authorized databases. Read-Only: grants the account read-only permissions on databases. Read/Write: grants the account read and write permissions on databases. DDL Only: grants the account DDL permissions on databases. DML Only: grants the account DML permissions on databases. |

6. After you complete the configuration, click **OK**.

### 6.5 Product Material Optimization Lite

**Lite**

The **lowest-cost** tier of the one-click cross-platform material optimization service. Given a 1688 product URL, produce TEMU-ready titles, attributes, hero images, SKU images, detail images, and copy. Uses the official Lowest Cost workflow: filtering and light processing, no high-cost image translation. Asynchronous.

**Endpoints**

**Submit optimization task**

```
POST /ai/material/optimization/lite
```

**Query optimization result**

```
POST /ai/material/optimization/lite/result
```

**Use cases**

Cross-border listing: 1688 → TEMU broad assortment publishing. High-SKU bulk listing, entry-level AI processing in ERP/SaaS pipelines. High daily volume but lower marketing performance bar. Filter out watermark / non-compliant images and pick clean originals; skip AI generation.

**Workflow**

The end-to-end Lowest Cost workflow:
1. Parse the 1688 product URL: extract title / SKU / hero image / detail images / attributes.
2. Filter text and apply SEO optimization against the TEMU blacklist and compliance rules.
3. Detect watermark / logo / Chinese copy in images; **prefer clean originals and skip**
**image translation** (high-converting marketing-text images may be filtered out).
4. Apply category matching, attribute filling, and multi-language localization to the target
platform.
5. Output a standardized material package; delivered via API and / or Excel export.

**Request parameters**

Lite and Pro share the same 31-field schema; the difference is the server-side workflow. Core fields below; for the full schema see the Smart Image Generation API.

| Parameter | Type | Required | Description |
|---|---|---|---|
| ImageUrl | String | Yes | Image URL (or 1688 product URL parsed by the server). Resolution > 512×512; long side ≤ 1920; short side ≤ 1080; size ≤ 5 MB; png / jpeg / jpg / bmp / webp. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Ability | Number[] | Yes | AI capabilities to invoke: 1=element detection, 2=smart matting, 3=smart removal, 4=image translation Pro, 5=image expansion, 6=smart crop, 7=upscale. Lite typically omits 4. |
| TargetPlatform | String | Yes | Target listing platform. Only TEMU is supported today. |
| TargetLanguage | String | No | Target language for text localization. |

| s ( |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| TargetWidth |   |   | TargetHeight |   |   |   |
|   |   | , |   | , | UpscaleFactor | , etc.) |

semantics as in the Smart Image Generation API.

**Response fields (query)**

| Field | Type | Description |
|---|---|---|
| Data.Status | String | Task state: RUNNING , COMPLETED , FAILED . |
| Data.Result.Images | Object[] | Processed image list (hero, SKU, detail). |
| Data.Result.Title | String | SEO-optimized title. |
| Data.Result.Attributes | Object[] | Target-platform attribute fills. |
| Data.Result.CategoryPath | String | Matched category path on the target platform. |
| Data.Result.UsageMap.Proce ssedImageCount | Number | Images processed (for billing reconciliation). |

|   | RUNNING |   |
|---|---|---|
| COMPLETED |   |   |

|   | Data.Result.CategoryPath |
|---|---|

|   | Data.Result.UsageMap.Proce | Number |
|---|---|---|
| ssedImageCount |   |   |

**Lite vs Pro**

| Dimension | Lite (this API) | Pro |
|---|---|---|
| Workflow | Lowest Cost | Best Quality |
| Marketing copy in images | Images with marketing copy filtered out | Preserved and rewritten |
| Image Translation Pro | Not invoked | Invoked |
| Category-specific assets | None | Yes (size charts, etc.) |

| A u | psaraDB RDS for MySQL User G ide·Accounts |   | ApsaraDB for RD | S |
|---|---|---|---|---|

| Dimension | Lite (this API) | Pro |
|---|---|---|
| Best fit | Broad assortment, low ASP, high velocity | Brand, high ASP, high conversion |

**Error codes**

See Error codes.

**What's next**

Product Material Optimization Pro -- best-quality tier. Smart Image Generation API -- detailed field schema for the 7 atomic capabilities.

## 7 Category Match

LLM-based cross-platform category matching. Given source-platform product info, automatically pick the best category on the target listing platform and return the full path, a confidence score, and the rationale. Synchronous. Only `TEMU` is supported today.

**Endpoint**

```
POST /ai/material/category/match
```

**Use cases**

Merchants relisting sourced goods need to map to the correct node in the target platform's category tree. Top sellers' internal bulk pipelines, ERP / SaaS-driven publishing, fast SMB single-item listing.

**Effect showcase**

| Case | Example image |
|---|---|
| 1688 USB fan → TEMU "Home Appliances > Heating, Cooling & Air Quality Appliances > Fans > USB Fans" | USB fan case |
| 1688 bracelet → TEMU "Clothing, Shoes & Jewelry > Women's Fashion > Women's Accessories > Women's Fashion Bracelets..." | Bracelet case |

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category (e.g., full 1688 category path). |
| ProductDescription | String | No | Product description. |
| SkuInfo | String | No | SKU information. |
| ProductAttributes | Object | No | Product attribute key- value pairs. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Full category path on the target platform, separated by > . |
| Data.CategoryName | String | Leaf category name. |
| Data.Confidence | Number | Confidence score (0-100). Recommend human review below 70. |
| Data.Reason | String | Match rationale. |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Heating, Cooling & Air Quality > Fans > USB Fans
```

`",`

```json
    "CategoryName": "USB Fans",
    "Confidence": 95,
    "Reason": "Title contains USB / fan keywords; source category is synonymous."
```

`}` `}`

**Error codes**

See Error codes.

**What's next**

Category Attribute Match API -- fill required attributes within the matched category.

### 7.1 Category Attribute Match

Multimodal-LLM-based cross-platform category-attribute filling. Given source-platform product info (title, source category, description, SKU, attributes, up to 10 images), match the precise target-platform category and fill every required attribute, with a per-attribute confidence and rationale. Synchronous.

**Endpoint**

```
POST /ai/material/category/attribute
```

**Use cases**

1688 → TEMU cross-platform listing where platform categories differ significantly and have complex hierarchical relations (material → wood species → density). Top sellers' bulk publishing, ERP / SaaS integrations, fast SMB single-item listing.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category path. |
| ProductDescription | String | No | Product description. |
| SkuInfo | Object[] | No | SKU list (spec + price per item). |
| ProductAttributes | Object | No | Source-platform attribute key-value pairs. |
| ImageUrls | String[] | No | Up to 10 image URLs. The multimodal model infers attributes from images. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Matched precise category path on the target platform. |
| Data.Attributes | Object[] | Filled attributes. Each item has Name , Value , Confidence (0-100), Reason , and SourceMatched (whether the value reused a source- platform attribute). |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Fans > USB Fans",
    "Attributes": [
      { "Name": "Battery Type", "Value": "Lithium-Ion", "Confidence": 92, "Reason": "Ti
tle and image both indicate rechargeable", "SourceMatched": false },
      { "Name": "Connectivity",  "Value": "USB Type-C",  "Confidence": 88, "Reason": "P
ort visible in image", "SourceMatched": true }
```

`]` `}` `}`

**Error codes**

See Error codes.

**What's next**

Category Match API -- category match alone.

### 7.2 Delete a database

You can delete databases that are no longer used in the ApsaraDB RDS console.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Databases**.
4. Find the database that you want to delete and click **Delete** in the **Actions** column.
5. In the message that appears, click **OK**.

## 8 Size Chart Extraction

Use a multimodal LLM to extract structured size-chart and package-dimension data from

| ColumnNameList |   | t |
|---|---|---|
| n; |   |   |

images. `ColumnNameList` targets specific columns (e.g., Size, Bust, Length) for precise extraction; `LanguageModel` controls output language (Chinese, English, or original). Asynchronous: submit, then poll.

**Endpoints**

**Submit extraction task**

```
POST /ai/image/size-chart/extraction
```

**Query extraction result**

```
POST /ai/image/size-chart/extraction/result
```

**Input example**

Size chart input example

**Use cases**

Apparel category size-chart text-ification. Bulk structuring of package weight / dimension info.

**Request parameters (submit)**

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| ImageUrl | String | Yes |   | URL of the image containing the size chart. |   |   |
| ColumnNameList | String[] | No |   | Target columns to extract (e.g., ["Size", "Bust", "Length"] ). Omit to extract all columns. |   |   |
|   |   |   |   |   | ["Size", "Bust", |   |
|   |   |   |   | "Length"] |   |   |
| LanguageModel | String | No |   | Output language: cn or en . Omit to keep the original language. |   |   |

**Request parameters (query)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| TaskId | String | Yes | Task ID returned by the submit endpoint. |

**Response fields (query)**

The response carries the raw multimodal-model structure (snake_case), which differs from the PascalCase convention used elsewhere: `{`

```json
  "Code": "Success",
  "Data": {
    "message": {
      "<ImageUrl>": {
        "size_chart": [
```

`{`

```json
            "Weight":  { "unit": "kg", "upper_value": 47.5, "lower_value": 40 },
            "Length":  { "unit": "CM", "value": 81 },
            "Size":    { "value": "S" },
            "Waist (stretched)": { "unit": "CM", "value": 58 }
```

`}` `],`

```json
        "intersection_attributes": ["Size", "Length", "Waist (stretched)", "Weight"],
        "size_chart_attributes":   ["Size", "Length", "Waist (stretched)", "Weight"]
```

`}` `},`

```json
    "usageMap": { "ProcessedImageCount": 1 }
```

`}` `}`

| : message.<ImageUrl>.size chart (extracted rows), intersection attributes _ _ tersecting ColumnNameList ), size chart attributes (columns actually _ _ usageMap.ProcessedImageCount (usage). | message.<ImageUrl>.size chart _ |   |   |   | (extracted rows), | intersection attributes _ |
|---|---|---|---|---|---|---|
|   |   | ColumnNameList | ), |   |   |   |
| usageMap.ProcessedImageCount |   |   |   |   |   |   |

**Error codes**

See Error codes.

**What's next**

Size Chart Detection API -- screen images first to save cost before extraction.

### 8.1 Change the endpoint and port number of an instance

**number of an instance**

This topic describes how to view and change the endpoint and port number of an ApsaraDB RDS instance.

**View the endpoint and port number of an instance**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the **Basic Information** section, view the internal and public endpoints and port
numbers.

**Change the endpoint and port number of an instance**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. On the page that appears, click **Modify Endpoint**.
5. In the dialog box that appears, set the connection type, endpoint, and port number, and
click **OK**.

**Note**

The prefix of an endpoint must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). It must start with a lowercase letter. The port number must be a value within the range of 1000 to 65534.

### 8.2 Apply for and release an internal endpoint or a public endpoint for an instance

**internal endpoint or a public**

**endpoint for an instance**

ApsaraDB RDS supports two types of endpoints: internal endpoints and public endpoints. The default type of the endpoint used to connect to an ApsaraDB RDS instance is determined by the network connection type selected when you create the instance. This topic describes how to apply for and release an internal endpoint or a public endpoint for an ApsaraDB RDS instance.

**Apply for an internal endpoint or a public endpoint**

If you set **Network Connection Type** to **Public network connection** when you create an ApsaraDB RDS instance, the database system assigns a public endpoint to the instance, and you can apply for an internal endpoint. Otherwise, the database system assigns an internal endpoint to the instance, and you can apply for a public endpoint.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. Apply for an internal endpoint or a public endpoint:
To apply for a public endpoint, click **Apply for Public Endpoint**. To apply for an internal endpoint, click **Apply for Internal Endpoint**.
5. In the message that appears, click **OK**.

**Release an internal endpoint or a public endpoint**

If an endpoint is no longer needed, you can release the endpoint to ensure instance security.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. Release an internal endpoint or a public endpoint:
To release a public endpoint, click **Release Public Endpoint**. To release an internal endpoint, click **Release Internal Endpoint**.
5. In the message that appears, click **OK**.

**FAQ**

Q: Can I change the endpoints and port numbers of my ApsaraDB RDS instance? A: You can change only the prefixes and port numbers of the endpoints. For more information, see Change the endpoint and port number of an instance. Q: Can I configure the endpoints of my ApsaraDB RDS instance to static IP addresses? A: No, you cannot configure the endpoints of your ApsaraDB RDS instance to static IP addresses. Both primary/secondary switchovers and specification changes may cause changes to the IP addresses. We recommend that you connect to your ApsaraDB RDS instance by using an endpoint. This allows you to minimize the impact on your workloads and eliminates the need to modify the configuration data on your application. Q: How do I connect to my ApsaraDB RDS instance by using a public endpoint? A: For more information, see Connect to an ApsaraDB RDS for MySQL instance.

### 8.3 Use DMS to log in to an ApsaraDB RDS instance

**ApsaraDB RDS instance**

This topic describes how to log in to an ApsaraDB RDS instance by using Data Management (DMS).

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page, click **Log On to Database**.
4. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
the **Database Type**, **Instance Region**, and **Connection String Address** parameters. If the values are correct, specify the **Database Account** and **Database Password** parameters.

| Parameter | Description |
|---|---|
| Database Type | The engine of the database. By default, the engine of the database to be connected is selected. |
| Instance Region | The region where the instance is deployed. By default, the region of the current instance is selected. |
| Connection String Address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database Account | The account of the database to be connected. |
| Database Password | The password of the account used to connect to the database. |

5. Click **Login**.

**Note**

If you want the browser to save the password, select **Remember password** and then click **Login**.

### 8.4 Configure the hybrid access solution

**solution**

This topic describes how to configure the hybrid access solution for an ApsaraDB RDS instance. This solution allows you to retain both the classic network endpoint and Virtual Private Cloud (VPC) endpoint of your ApsaraDB RDS instance. This way, you can migrate your ApsaraDB RDS instance from the classic network to a VPC without network interruptions.

**Background information**

When you migrate your ApsaraDB RDS instance from the classic network to a VPC, the internal classic network endpoint of the instance changes to the internal VPC endpoint. In this case, the endpoint remains unchanged, but the IP address that is bound to the endpoint changes. This change causes a network interruption of 30 seconds or less, and Elastic Compute Service (ECS) instances located in the classic network can no longer connect to your ApsaraDB RDS instance over an internal network. To facilitate a smooth migration, ApsaraDB RDS provides the hybrid access solution. Hybrid access indicates that your ApsaraDB RDS instance can be connected by both ECS instances located in the classic network and ECS instances located in a VPC. During the validity period of the hybrid access solution, ApsaraDB RDS retains the internal classic network endpoint and generates an internal VPC endpoint. This prevents network interruptions when you migrate your ApsaraDB RDS instance from the classic network to a VPC. For security and performance purposes, we recommend that you use only the internal VPC endpoint. You must specify a validity period for the hybrid access solution. When the validity period expires, ApsaraDB RDS releases the internal classic network endpoint and applications are unable to use the endpoint to connect to your ApsaraDB RDS instance. Therefore, you must add the internal VPC endpoint to your applications before the validity period expires. This ensures a smooth migration and prevents interruptions to your workloads. For example, assume that a company uses the hybrid access solution to migrate its ApsaraDB RDS instance from the classic network to a VPC. During the validity period of the hybrid access solution, some applications use the internal VPC endpoint to connect to the ApsaraDB RDS instance, whereas the others continue to use the internal classic network endpoint to connect to the instance. When all applications of the company can use the internal VPC endpoint to connect to the instance, the internal classic network endpoint can be released. The following figure demonstrates this scenario.

**Limits**

During the validity period of the hybrid access solution, your ApsaraDB RDS instance has the following limits: The network type of the instance cannot be changed to classic network. The instance cannot be migrated to another zone.

**Prerequisites**

The ApsaraDB RDS instance resides in the classic network. Available VPCs and vSwitches exist in the zone where the ApsaraDB RDS instance resides. Your ApsaraDB RDS instance provides an internal endpoint. If no internal endpoint exists, you must apply for one. For more information, see Apply for and release an internal endpoint or a public endpoint for an instance.

**Change the network type from classic network to VPC**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. On the page that appears, click **Switch to VPC**.
5. In the Switch to VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. Clear or select the **Retain Original Classic Network Endpoint** check box based on the details described in the following table.

| Action | Description |
|---|---|

| Clear the Retain Original Classic Network Endpoint check box | The classic network endpoint is not retained and changes to a VPC endpoint. When you change the network type from classic network to VPC, a network interruption of approximately 30 seconds occurs and ECS instances located in the classic network are disconnected from your ApsaraDB RDS instance. |
|---|---|
| Select the Retain Original Classic Network Endpoint check box | The classic network endpoint is retained, and a new VPC endpoint is generated. In this case, your ApsaraDB RDS instance runs in hybrid access mode. Both ECS instances located in the classic network and ECS instances located in the selected VPC can access your ApsaraDB RDS instance over an internal network. When you change the network type from classic network to VPC, no network interruptions occur. ECS instances located in the classic network are still connected with your ApsaraDB RDS instance until the classic network endpoint expires. Specify the validity period of the classic network endpoint. Before the classic network endpoint expires, you must add the new VPC endpoint to your applications that run on the ECS instances located in the selected VPC. This allows ApsaraDB RDS to migrate your workloads to the selected VPC without network interruptions. |

6. Add the internal IP addresses of ECS instances located in the selected VPC to an IP address
whitelist of the VPC network type. This allows the ECS instances to connect to your ApsaraDB RDS instance over an internal network. If no IP address whitelists of the VPC network type are available, create one. For more information about how to configure a whitelist, see Configure an IP address whitelist.

**Change the expiration date of the internal classic network**

**endpoint**

During the validity period of the hybrid access solution, you can change the expiration date of the classic network endpoint based on your business requirements. The expiration date is immediately recalculated starting from the day when you make the change. For example, assume that the classic network endpoint is configured to expire on August 18, 2017. On August 15, 2017, you extend the validity period of the classic network endpoint by 14 days. In this case, ApsaraDB RDS releases the classic network endpoint on August 29, 2017. To change the expiration date, perform the following operations:
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. On the page that appears, click **Change Expiration Time**.
5. In the **Change Expiration Time** dialog box, select an expiration date and click **OK**.

### 8.5 Change the network type of an instance

**an instance**

This topic describes how to change the network type of an ApsaraDB RDS instance between the classic network and Virtual Private Cloud (VPC).

**Background information**

Classic network: RDS instances in the classic network are not isolated. To block unauthorized access to these instances, you must configure whitelists or security groups. VPC: Each VPC is an isolated virtual network. We recommend that you select the VPC type because it is more secure than the classic network. You can configure route tables, CIDR blocks, and gateways in a VPC. You can also connect your data center to a VPC by using Express Connect circuits or VPNs. The data center and the VPC comprise a virtual data center. You can use the virtual data center to migrate your applications to the cloud with no downtime.

**Change the network type from VPC to classic network**

Usage notes After you change the network type from VPC to classic network, the internal endpoint of your RDS instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, Elastic Compute Service (ECS) instances located in the same VPC as your RDS instance can no longer connect to your RDS instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. When you change the network type, a network interruption of 30 seconds may occur. To avoid business interruption, change the network type during off-peak hours or make sure that your application is configured to automatically reconnect to the instance.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. In the upper-right corner of the Database Connection section, click **Switch to Classic**
**Network**.
5. In the message that appears, click **OK**.

**Change the network type from classic network to VPC**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. In the upper-right corner of the Database Connection section, click **Switch to VPC**.
5. In the dialog box that appears, select a VPC and vSwitch, select or unselect **Retain**
**Original Classic Network Endpoint**, and click OK. For more information about the
**Retain Original Classic Network Endpoint** option, see Hybrid access from both the classic
network and VPCs.

### 8.6 Change the VPC and vSwitch for an instance

**for an instance**

This topic describes how to change the virtual private cloud (VPC) and vSwitch for an ApsaraDB RDS instance.

**Prerequisites**

**q**

The instance is deployed in a VPC.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Connection**.
4. On the right side of the page that appears, click **Switch vSwitch**.
5. In the dialog box that appears, select a VPC and a vSwitch, and click **OK**.
6. In the message that appears, click **OK**.

**Note**

During the switchover, your application is temporarily disconnected from the instance for 30 seconds. Make sure that your application is configured to automatically reconnect to the instance. If data is cached on your client, you can read data but cannot write data. After the switchover, we recommend that you immediately clear the cache on the client.

## 9 Database proxy

### 9.1 Configure dedicated proxy

This topic describes the dedicated proxy feature provided by ApsaraDB RDS. The dedicated proxy feature provides advanced features such as read/write splitting, connection pooling, and transaction splitting.

**Background information**

The dedicated proxy feature uses dedicated proxy computing resources. This feature has the following benefits: A unified proxy endpoint is provided to connect to all the dedicated proxies that are enabled on your ApsaraDB RDS instance. This reduces maintenance costs by eliminating the need to update the endpoints on your application. The proxy endpoint remains valid until you release the dedicated proxies. For example, you can enable read/write splitting during peak hours and then disable read/write splitting and release read-only instances during off-peak hours. In these cases, you do not need to update the endpoints on your application because the proxy endpoint remains connected. Dedicated proxies serve your ApsaraDB RDS instance and its read-only instances exclusively. You do not need to compete with other users for resources. This ensures service stability. Dedicated proxies are scalable. You can add dedicated proxies based on your business requirements to handle more workloads.

**Limits**

Dedicated proxies do not support SSL encryption. Dedicated proxies do not support compression protocols.

**Usage notes**

When you change the specifications of the primary instance or its read-only instances, a service interruption may occur. If you connect your application to the proxy endpoint, all requests that are encapsulated in transactions are routed to the primary instance. This applies when the transaction splitting feature is not enabled. If a proxy endpoint is used to implement read/write splitting, read consistency cannot be ensured for the requests that are not encapsulated in transactions. If you require read consistency for these requests, you can encapsulate these requests in transactions. If a proxy endpoint is used for connection, the `SHOW PROCESSLIST` statement returns a result set for each query. The result set consists of the query results from the primary and read-only instances. If you execute multi-statements or stored procedures, the read/write splitting feature is disabled and all subsequent requests over the current connection are routed to the primary instance. To enable the read/write splitting feature again, you must close the current connection and establish a new connection. The dedicated proxy feature supports the `/*FORCE_MASTER*/` and `/*FORCE_SLAVE*/` hints. However, requests that contain hints have the highest route priorities and are not constrained by consistency or transaction limits. Before you use these hints, you must check whether these hints are suitable for your workloads. A hint cannot contain statements that change environment variables. An example is `/*FORCE_SLAVE*/ set names` utf8; . Otherwise, an error may occur in the subsequent procedure. After you enable the dedicated proxy feature, each connection is replicated to the primary instance and all of its read-only instances in compliance with the 1:N connection model. We recommend that you specify the same connection specifications for these instances. If these instances have different connection specifications, the number of connections allowed depends on the lowest connection specifications among these instances. If you create or restart a read-only instance after you enable the dedicated proxy feature, only the requests sent over new connections are routed to the new or restarted read-only instance. The **max_prepared_stmt_count** parameter must be set to the same value for the primary instance and all of its read-only instances.

**Enable the dedicated proxy feature**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the page that appears, click **Enable**.

**Note**

If the network type of the instance is **Classic Network**, the dedicated proxy feature is enabled. If the network type of the instance is **VPC**, you must select a vSwitch and click
**Enable** in the dialog box that appears.

**Overview of the Proxy Service tab**

When the dedicated proxy feature is enabled, you can use the generated proxy endpoint to implement features such as read/write splitting, short-lived connection optimization, and transaction splitting.

| Section | Parameter | Description |
|---|---|---|
|   | Instance ID | The ID of the primary ApsaraDB RDS instance. |
|   | Enabled Proxies | The number of enabled dedicated proxies. You can enable more dedicated proxies to increase the maximum number of requests that can be processed. |
|   | Read/Write Splitting | Specifies whether to enable the read/write splitting feature for the proxy endpoint. For more information, see Configure read/write splitting. |

|   | Short-Lived Connection Optimization | The type of connection pool for the proxy endpoint. This feature is suitable for scenarios where PHP short-lived connections are established. For more information, see Configure short-lived connection optimization. Note You can click Enable or Disable to the right of Short- Lived Connection Optimization to enable or disable this feature. |
|---|---|---|
| Proxy Endpoint |   |   |
|   | Transaction Splitting | Specifies whether to enable the transaction splitting feature for the proxy endpoint. For more information, see Configure transaction splitting. Note You can click Enable or Disable to the right of Transaction Splitting to enable or disable this feature. |
|   | Endpoint | The proxy endpoint that is generated when the dedicated proxy feature is enabled. This endpoint connects to all the dedicated proxies that are enabled on the ApsaraDB RDS instance. The read/write splitting feature is also bound to this endpoint. Note You can click Copy Endpoint to the right of Endpoint to copy the endpoint. |
|   | Port | The port number that is used to connect to the proxy endpoint. |
|   | Endpoint Type | The network type of the proxy endpoint. |
|   | Proxy Type | The type of proxy that is enabled. Only Dedicated Proxy is supported. |
|   | Proxy Specifications | The CPU and memory specifications of the dedicated proxies. Only 2-core CPU and 4 GB memory is supported. |

| Proxy |   |   |
|---|---|---|
|   | Enabled Proxies | The number of dedicated proxies that are enabled on the primary ApsaraDB RDS instance. Up to 60 dedicated proxies are supported. Note We recommend that you use the following formula to determine the number of dedicated proxies to specify: (Total number of CPU cores of your primary ApsaraDB RDS instance and its read-only instances)/8, rounded up to the nearest integer. For example, if your primary ApsaraDB RDS instance has 8 CPU cores and its read-only instances have 4 CPU cores, the recommended number of dedicated proxies is 2, as calculated in the following formula: ⌈(8 + 4)/8⌉ = 2. |

**Adjust the number of dedicated proxies**

**Note**

When you adjust the number of dedicated proxies, a service interruption may occur. Make sure that your application is configured to automatically reconnect to the instance.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. In the **Proxy** section of the Proxy Service tab, change the number in the **Adjusted Proxies**
column and click **Apply** in the **Adjustment Plan** column.
5. In the Configure Proxy Resources dialog box, select **Migrate Immediately** to apply the
change. You can also select **Next Maintenance Period** to set a maintenance window for the change to take effect. Click **OK**.

**Disable the dedicated proxy feature**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. In the upper-right corner of the page that appears, click **Disable Database Proxy**.
5. In the message that appears, click **OK**.

### 9.2 Configure short-lived connection optimization

**connection optimization**

This topic describes the short-lived connection optimization feature provided by ApsaraDB RDS in its dedicated proxy feature. The short-lived connection optimization feature effectively resolves the issue of heavy instance loads caused by frequent short-lived connections such as short-lived connections over PHP.

**Prerequisites**

The dedicated proxy feature is enabled for your ApsaraDB RDS instance. For more information, see Configure dedicated proxy.

**Background information**

The short-lived connection optimization feature is used to reduce workloads on the ApsaraDB RDS instance caused by frequent short-lived connections. When a client is disconnected, the system checks whether the closed connection is idle. If the connection is considered idle, the dedicated proxy retains the connection in the connection pool for a short period of time. When the client initiates a request for access to your instance again, the dedicated proxy searches the connection pool for an idle connection that matches the request. The connection pool is matched based on the values of the user, clientip, and dbname fields in the request. If the dedicated proxy finds an idle connection that matches the request, it reuses the matched idle connection. If no idle connection can be matched, a new connection is established with your instance to reduce database connection overheads.

**Note**

The short-lived connection optimization feature does not reduce the number of concurrent connections with the instance. It decreases the frequency at which connections are established between an application and your instance to reduce overheads of the primary MySQL thread and improve efficiency to process business requests. However, idle connections in the connection pool still occupy the database threads for a short period of time.

**Usage notes**

You cannot configure different permissions for different source IP addresses by using the same account. Otherwise, errors may occur when connections in the connection pool are reused. For example, if a user account has permissions on database_a when its source IP address is 192.168.1.1 but does not have permissions on database_a when its source IP address is 192.168.1.2, the short-lived connection optimization feature may encounter permission errors.

**Enable short-lived connection optimization**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, click **Enable** to the right of **Short-Lived Connection**
**Optimization**.

### 9.3 Configure transaction splitting

This topic describes the transaction splitting feature provided by the dedicated proxy of ApsaraDB RDS. This feature identifies and distributes read requests initiated before write requests within a transaction to read-only instances. This reduces workloads on the primary instance.

**Prerequisites**

The dedicated proxy feature is enabled for your ApsaraDB RDS instance. For more information, see Configure dedicated proxy.

**Background information**

By default, the dedicated proxy sends all requests in transactions to the primary instance to ensure the correctness of the transactions. If the framework encapsulates all requests in transactions, the primary instance becomes heavily loaded. In this case, you can enable the transaction splitting feature. When transaction splitting is enabled and the default isolation level READ COMMITTED is used, the ApsaraDB RDS instance starts a transaction only for write requests when autocommit is disabled (set autocommit=0). Read requests that arrive before the transaction is started are distributed to read-only instances by the load balancer.

**Note**

Explicit transactions cannot be split. These explicit transactions include the transactions that are started by using BEGIN or START statements. If the transaction splitting feature is enabled, global consistency cannot be ensured. Before you use this feature, we recommend that you evaluate whether this feature is suitable for your workloads.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, click **Enable** to the right of **Transaction Splitting**.

**Note**

When you no longer need transaction splitting, you can click **Disable** to the right of **Transaction Splitting**. The operation to enable or disable transaction splitting takes effect only on new connections.

### 9.4 Read/write splitting

#### 9.4.1 Enable read/write splitting

This topic describes the read/write splitting feature. This feature allows ApsaraDB RDS to route read and write requests to primary and read-only instances based on the dedicated proxy endpoint (also called read/write splitting endpoint).

**Prerequisites**

The database proxy or dedicated proxy feature is enabled. For more information, see Enable the database proxy feature or Enable the dedicated proxy feature. At least one read-only instance is created. For more information about how to create a read-only instance, see Create a read-only instance.

**Background information**

If your database system receives a large number of read requests and a small number of write requests, a single primary ApsaraDB RDS instance may fail to process read requests and your workloads may be interrupted. In this case, you can create one or more read-only ApsaraDB RDS instances to offload read requests from the primary instance and increase the read capability of your database system. For more information, see Create a read-only instance. After you create read-only instances, you can enable read/write splitting. In this case, a read/write splitting endpoint is provided. After you add the endpoint to your application, write requests are routed to the primary instance, and read requests are routed to the read-only instances.

**Differences between the read/write splitting endpoint and the**

**internal and public endpoints**

After you enable read/write splitting and add the read/write splitting endpoint to your application, all requests are first routed to this endpoint, and then to the primary and readonly instances based on the request types and the read weights of these instances. If the internal or public endpoint of the primary instance is added to your application, all requests are routed to the primary instance. To implement read/write splitting, you must add the endpoints and read weights of the primary and read-only instances to your application.

**Logic for routing requests**

The following requests are routed only to the primary instance: All requests that are used to execute DML statements such as INSERT, UPDATE, DELETE, and SELECT FOR UPDATE. All requests that are used to execute DDL statements, such as the DDL statements that are used to create databases or tables, delete databases or tables, and change schemas or permissions. All requests that are encapsulated in transactions. Requests that are used to call user-defined functions. Requests that are used to run stored procedures. Requests that are used to execute EXECUTE statements Requests that are used to run multi-statement queries. For more information, see Multistatement. Requests that involve temporary tables. Requests that are used to execute SELECT last_insert_id() statements. All requests that are used to query or reconfigure user variables. Requests that are used to execute SHOW PROCESSLIST statements. Requests that are used to execute KILL statements in SQL. These statements are different from the KILL commands in Linux. The following requests are routed to the primary instance or its read-only instances: Read requests that are not encapsulated in transactions. Requests that are used to execute COM_STMT_EXECUTE statements. The following requests are routed to all the instances: All requests that are used to modify system variables. Requests that are used to execute USE statements. Requests that are used to execute COM_STMT_PREPARE statements. Requests that are used to execute COM_CHANGE_USER, COM_QUIT, and COM_SET_OPTION statements.

**Benefits**

Easier maintenance by using a unified read/write splitting endpoint If you do not enable the read/write splitting feature, you must add the endpoints of the primary and read-only instances to your application. This way, your database system routes write requests to the primary instance and read requests to the read-only instances. If you enable the read/write splitting feature, you can use a dedicated proxy endpoint to implement read/write splitting. After your application is connected to this endpoint, your database system routes read and write requests to the primary and read-only instances based on the read weights of these instances. This reduces maintenance costs. You can also create read-only instances to improve the read capability of your database system. You do not need to modify the configuration data on your application. Higher performance and lower maintenance costs by using a native link If you build your own proxy layer in the cloud to implement read/write splitting, data must be parsed and forwarded by multiple components before the data reaches your database system. As a result, response latencies increase. The read/write splitting feature is embedded in the ApsaraDB RDS ecosystem to reduce response latencies, increase processing speeds, and reduce maintenance costs. Ideal in a variety of use scenarios based on configurable read weights and thresholds You can specify the read weights of the primary and read-only instances. You can also specify the latency threshold for data replication to the read-only instances. High availability based on instance-level health checks The read/write splitting feature enables ApsaraDB RDS to actively check the health status of the primary and read-only instances. If a read-only instance unexpectedly breaks down or its data replication latency exceeds the specified threshold, ApsaraDB RDS stops routing read requests to the instance. ApsaraDB RDS redirects read requests that are destined for the faulty read-only instance to healthy instances in your database system. This ensures service availability in the event of faults on individual read-only instances. After the faulty read-only instance is recovered, ApsaraDB RDS resumes routing read requests to the instance.

**Note**

To avoid single points of failure (SPOFs), we recommend that you create at least two read-only instances.

**Usage notes**

When you change the specifications of the primary instance or its read-only instances, a service interruption may occur. After you create a read-only instance, only the requests over new connections can be routed to the read-only instance. The dedicated proxy endpoint does not support SSL encryption. The dedicated proxy endpoint does not support compression protocols. If a dedicated proxy endpoint is used to connect to your database system, all the requests that are encapsulated in transactions are routed to the primary instance. If a dedicated proxy endpoint is used to implement read/write splitting, the read consistency of the requests that are not encapsulated in transactions cannot be ensured. If you require read consistency for these requests, you can encapsulate these requests in transactions. If a dedicated proxy endpoint is used for connection, the `SHOW PROCESSLIST` statement returns a result set for each query. The result set consists of the query results from the primary and read-only instances. If the short-lived connection optimization feature is enabled, the `SHOW PROCESSLIST` statement may return idle connections. If you execute multi-statements or stored procedures, the read/write splitting feature is disabled and all subsequent requests over the current connection are routed to the primary instance. To enable the read/write splitting feature again, you must close the current connection and establish a new connection. The dedicated proxy feature supports the `/*FORCE_MASTER*/` and `/*FORCE_SLAVE*/` hints. However, requests that contain hints have the highest route priorities and are not constrained by consistency or transaction limits. Before you use these hints, you must check whether these hints are suitable for your workloads. A hint cannot contain statements that change environment variables. An example is `/*FORCE_SLAVE*/ set names` utf8; . Otherwise, an error may occur in the subsequent procedure.

**Prerequisites**

A read-only instance is created for the primary instance. For more information, see Create a read-only instance.

**Enable read/write splitting**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the page that appears, select **Read/Write Splitting** tab and click **Enable now**.
5. Configure the parameters described in the following table.

| Paramete r | Description |
|---|---|
| Latency Threshold | The maximum latency that is allowed for data replication from the primary instance to the read-only instances. If the latency at which a read-only instance replicates data from the primary instance exceeds the value of this parameter, the system no longer routes read requests to the read-only instance regardless of the read weight of the read-only instance. Valid values: 0 to 7200. Unit: seconds. The read-only instances may replicate data from the primary instance at a specific latency. The latency varies based on the statuses of the SQL statements that are executed. We recommend that you set this parameter to a value that is greater than or equal to 30. |
| Read Weight Distributi on | The method that is used to assign read weights. A higher read weight indicates that more read requests need to be processed. For example, three read-only instances are attached to the primary instance, the read weight of the primary instance is 0, and the read weights of the three read-only instances are 100, 200, and 200. In this case, the primary instance processes only write requests, and the three read-only instances process all read requests based on the 1:2:2 ratio. Automatic Distribution: The system automatically assigns a read weight to each instance in your database system based on the specifications of each instance. After you create a read-only instance, the system automatically assigns a read weight to the read-only instance and adds the read-only instance to the read/write splitting link. Customized Distribution: You must specify a read weight for each instance in your database system. Valid values: 0 to 10000. After you create a read-only instance, ApsaraDB RDS sets the read weight of the read-only instance to 0 by default. You must manually modify the read weight of the created read-only instance. |

6. Click **OK**.

#### 9.4.2 Configure read/write splitting

This topic describes how to configure the latency threshold and specify read weights for an ApsaraDB RDS instance in the ApsaraDB RDS console.

**Prerequisites**

Read/write splitting is enabled. For more information, see Enable read/write splitting.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Read/Write Splitting** tab, click **Configure Read/Write Splitting**.
5. Configure the parameters described in the following table.

| Paramete r | Description |
|---|---|

| Latency Threshold | The maximum latency that is allowed for data replication from the primary instance to the read-only instances. If the latency at which a read-only instance replicates data from the primary instance exceeds the value of this parameter, the system no longer routes read requests to the read-only instance regardless of the read weight of the read-only instance. Valid values: 0 to 7200. Unit: seconds. The read-only instances may replicate data from the primary instance at a specific latency. The latency varies based on the statuses of the SQL statements that are executed. We recommend that you set this parameter to a value that is greater than or equal to 30. |
|---|---|
| Read Weight Distributi on | The method that is used to assign read weights. A higher read weight indicates that more read requests need to be processed. For example, three read-only instances are attached to the primary instance, the read weight of the primary instance is 0, and the read weights of the three read-only instances are 100, 200, and 200. In this case, the primary instance processes only write requests, and the three read-only instances process all read requests based on the 1:2:2 ratio. Automatic Distribution: The system automatically assigns a read weight to each instance in your database system based on the specifications of each instance. After you create a read-only instance, the system automatically assigns a read weight to the read-only instance and adds the read-only instance to the read/write splitting link. Customized Distribution: You must specify a read weight for each instance in your database system. Valid values: 0 to 10000. After you create a read-only instance, ApsaraDB RDS sets the read weight of the read-only instance to 0 by default. You must manually modify the read weight of the created read-only instance. |

6. Click **OK**.

#### 9.4.3 Disable read/write splitting

This topic describes how to disable the read/write splitting feature of an ApsaraDB RDS instance in the ApsaraDB RDS console.

**Prerequisites**

Read/write splitting is enabled. For more information, see Enable read/write splitting.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Read/Write Splitting** tab, click **Disable Read/Write Splitting**.
5. Click **Confirm**.

## 10 Monitoring and alerts

### 10.1 View resources and engine monitoring data

**monitoring data**

The ApsaraDB RDS console provides a variety of performance metrics to monitor the status of your instances.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Monitoring and Alerts** page, click the **Resource Monitoring**, **Engine**
**Monitoring**, or **Deploy Monitoring** tab and specify a time range to view the
corresponding monitoring data. The following table describes the metrics.

| Monitor ing type | Metric | Description |
|---|---|---|
| Resourc e Monitor ing | Disk Space (MB) | The disk space usage of the instance. It consists of the following items: Instance size Data usage Log size Temporary file size Other system file size Unit: MB. |
|   | IOPS | The number of input/output operations per second (IOPS) of the instance. |
|   | Total Connections | The number of active connections to the instance and the total number of connections to the instance. |
|   | CPU Utilization and Memory Usage (%) | The CPU utilization and memory usage of the instance. These metrics do not include the CPU utilization and memory usage for the operating system. |
|   | Network Traffic (KB) | The inbound and outbound traffic of the instance per second. Unit: KB. |

| Engine Monitor ing | Transactions per Second (TPS)/Queries per Second (QPS) | The average number of transactions per second (TPS) and the average number of SQL statements executed per second. |
|---|---|---|
|   | InnoDB Buffer Pool Read Hit Ratio, Usage Ratio, and Dirty Block Ratio (%) | The read hit ratio, usage ratio, and dirty block ratio of the InnoDB buffer pool. |
|   | InnoDB Read/Write Volume (KB) | The amount of data that InnoDB reads and writes per second. Unit: KB. |
|   | InnoDB Buffer Pool Requests | The number of read and write operations that InnoDB performs per second. |
|   | InnoDB Log Reads/Writes/fsync( ) Operations | The number of physical writes to log files by InnoDB per second, the number of log write requests by InnoDB per second, and the number of fsync writes to log files by InnoDB per second. |
|   | Temporary Tables Automatically Created on Hard Disk when MySQL Statements Are Executed | The number of temporary tables that are automatically created on the hard disk when the database executes SQL statements. |
|   | MySQL COMDML _ | The number of SQL statements that the database executes per second. The following SQL statements are included: Insert Delete Insert Select _ Replace Replace Select _ Select Update |
|   | MySQL RowDML _ | The number of operations that InnoDB performs per second. The following items are included: The number of physical writes to log files per second The number of rows on which InnoDB performs operations per second. This includes the number of rows that are read from InnoDB tables per second, the number of rows that are updated in InnoDB tables per second, the number of rows that are deleted from InnoDB tables per second, and the number of rows that are inserted into InnoDB tables per second. |

|   | MyISAM Reads and Writes | The numbers of operations that MyISAM performs per second. The following items are included: The number of MyISAM reads and writes from the buffer pool per second The number of MyISAM reads and writes from the hard disk per second |
|---|---|---|
|   | MyISAM Key Buffer Read/Write/Usage Ratio (%) | The read hit ratio, write hit ratio, and usage of the MyISAM key buffer per second. |
| Deploy Monitor ing | Replication Thread Status of Secondary Instances | The status of the threads that are used to replicate data to the secondary RDS instance. I/O Thread Status of Secondary Instances: The value 1 indicates that the thread is normal, and the value 0 indicates that the thread is lost. SQL Thread Status of Secondary Instances: The value 1 indicates that the thread is normal, and the value 0 indicates that the thread is lost. |
|   | Replication Latency of Secondary Instances (s) | The latency of data replication to the secondary RDS instance. Unit: seconds. |

### 10.2 Configure an alert rule

This topic describes how to create alert rules in the ApsaraDB RDS console. This allows you to identify and handle exceptions at the earliest opportunity.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Alerts** tab, click **Alert Rule Settings**.
5. On the **Alert Rule** page, click **Create an alert rule**.
6. In the **Create an alert rule** panel, configure the parameters described in the following
table and click **OK**.

| Parameter | Description |
|---|---|

| Cloud product selection | Select ApsaraDB RDS or ApsaraDB RDS (New). Note For old links, the MySQL, SQL Server, PolarDB O, and PostgreSQL engines are supported, the namespace of monitoring data is acs rds dashboard, and the data collection period varies from 60 to _ _ 300 seconds. For new links, only the MySQL, PolarDB O, and PostgreSQL engines are supported. acs rds dashboard is also used as _ _ the namespace of monitoring data, but a more stable data collection period of 60 seconds is provided. |
|---|---|
| Resource scope | The resources to which the alert rule applies. Valid values: Instance dimension: Select one or more instances in the resource set of the current organization. Resource set dimension: Select a resource set in the current organization and region. Apply grouping dimensions: Select an application group in the current organization and region. All resources: The alert rule applies to all resources of the specified cloud service. |
| Resource Selection | The resources to be associated with the alert rule. Select one or more resources based on the selected resource scope. |
| Alarm rule description | The trigger conditions of the alert rule. If the monitoring data meets the specified conditions, the alert rule is triggered. To configure the trigger conditions, perform the following steps: i. Click Rule description. ii. In the Rule description panel, configure the Rule name, Monitoring Metrics, Metric dimension, and Threshold and alarm level parameters. Note The Metric dimension parameter is displayed only if you set the Resource scope parameter to Instance dimension. iii. Click Confirm. |
| Silence channel period | The mute period after which Cloud Monitor resends an alert notification before the alert is cleared. Valid values: 5 minutes, 15 minutes, 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, and 24 hours. An alert is triggered if the conditions of an alert rule are met. Cloud Monitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, Cloud Monitor resends alert notifications. For example, if you set the Silence channel period parameter to 12 hours, Cloud Monitor resends alert notifications only if the alert still persists after 12 hours. |

| Effective time | The period during which the alert rule takes effect. Cloud Monitor checks whether the monitoring data triggers the alert rule only during the effective period. |
|---|---|
| Alarm callback | The callback URL to which Cloud Monitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for Cloud Monitor. You can enter only an HTTP URL. IP addresses are not supported. |
| No data processing method | Specify how Cloud Monitor acts when no alert is triggered. Valid values: No processing: Cloud Monitor does not perform any operations when no alert is triggered. Send no data alarm: Cloud Monitor sends the corresponding notifications to contacts when no alert is triggered. |
| Alarm contact | The alert contacts or alert contact groups to which Cloud Monitor sends alert notifications. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

## 11 Cloud Monitor

### 11.1 View performance metrics

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

### 11.2 Alert history

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

| Export alert history | i. On the Alert History page, click in the upper-right corner. ii. In the Export Task dialog box, set Time Range and Task Name. Then, click OK. |
|---|---|

### 11.3 Alert rules

#### 11.3.1 Create an alert rule

Create an alert rule that triggers alerts for a cloud service based on specified metric thresholds and promptly notifies relevant users.

**Background information**

During its effective period, an alert rule checks at a default detection frequency if a metric exceeds the specified threshold. If a metric exceeds the threshold and becomes abnormal, an alert is sent to the specified alert contacts or other alert processing platforms.

**Note**

The minimum alert detection frequency is once per minute.

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

| Resource Selection | Based on the selected Resource Scope, select a specific resource instance, resource set, or application group. |
|---|---|
| Alert Rule Description | The main body of the alert rule. The rule is triggered when monitoring data meets the alert conditions. To set the rule description: i. Click Create Alert Rule. ii. In the Create Alert Rule panel, set the Rule Name, Metric Dimension, Monitoring Metric, Threshold, AndAlert Level. Note The Metric Dimension parameter is displayed only when Resource Scope is set to Instance. iii. Click Confirm. |
| Mute For | The interval at which to resend an alert notification if the alert is not resolved. Valid values: 5 Minutes, 15 Minutes, 30 Minutes, 1 Hour, 3 Hours, 6 Hours, 12 Hours, and 24 Hours. When a metric exceeds the alert threshold, an alert is triggered. If the metric continues to exceed the threshold during the mute period, no more alert notifications are sent. If the metric has not recovered after the mute period, CloudMonitor sends another alert notification. For example, if Mute For is set to 12 Hours, CloudMonitor sends another alert notification if the metric that exceeded the threshold has not recovered 12 hours after the first alert was triggered. |
| Effective Period | The period during which the alert rule is active. The rule only checks if monitoring data exceeds the alert threshold during this period. |
| Alert Callback | A webhook address that receives alert messages pushed by CloudMonitor through POST requests. Note The webhook address must be a domain name accessible to CloudMonitor. Only the HTTP protocol is supported. You cannot enter an IP address. |
| No Data Handling Method | The method for handling alerts when there is no monitoring data. Do Nothing Send No-data Alert |
| Alert Contact | Select the user group or user to whom alert messages are sent. The default alert contact group for an Alibaba Cloud account is an empty group. You can use it to test the validity of an alert rule. |

6. Click **OK**.

**Rule description parameters**

| Parameter | Description |
|---|---|
| Rule Name | Enter a name for the alert rule. |
| Monitoring Metric | From all the metrics available for the selected cloud service, select the target metric. For more information about the metrics for each cloud service, see the relevant monitoring documentation. |
| Metric Dimension | Refers to dimensions other than the instance ID. This parameter is displayed only when Resource Scope is set to Instance. |
| Threshold And Alert Level (unit: %) | The alert levels are Critical, Warning, and Info. The aggregation method for monitoring data can be Average, Minimum, or Maximum. You can set the monitoring data epoch to 1 Consecutive Epoch, 5 Consecutive Epochs, 10 Consecutive Epochs, 15 Consecutive Epochs, 30 Consecutive Epochs, or 60 Consecutive Epochs. The comparison operator between the actual monitoring data and the alert threshold. Supported operators include “>”, “ >=”, “<”, “<= ”, “=”, “!=”, “Day-on-day Increase”, “Day-on-day Decrease”, “Period-on-period Increase”, “period-on-period Decrease”, “increase From Last Period”, and “decrease From Last Period”. You can also set a threshold and the number of times it must be met to trigger an alert. |

**Example configuration**

This example creates an alert rule named "example" for an Elastic Compute Service (ECS) instance to monitor its CPU utilization. The rule triggers a Critical alert if the maximum CPU utilization is greater than or equal to 70% for three occurrences within five detection periods. The following figure shows the rule description configuration for this scenario.

#### 11.3.2 Manage alert rules

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

| Check rule validity | In the Validity column of the target alert rule, click Click To Inspect. The inspection result is displayed in the Validity column. Note If the inspection result is abnormal, click Detection Result. In the panel that appears, view the results for Alert Rule Execution Anomaly Detection, Alert Rule Load Detection, Invalid Alert Rule Detection, and Alert Rule Callback Detection. Click Re-detect to check the rule validity again. |
|---|---|
| View rule execution records | In the Rule Execution Record column of the target alert rule, click View Rule Execution Record. On the Alert Rule Execution Record panel, filter the execution records by time range. |
| Modify an alert rule | i. In the Operation column of the target alert rule, click Edit. ii. On the Modify Alert Rule panel, modify the alert rule. For more information about the configuration parameters, see Create an alert rule. iii. After you finish the modification, click OK. |
| Disable an alert rule | Disable alert rules when you manually stop a cloud product for maintenance or an upgrade. This prevents unnecessary alert notifications. Note Before disabling an alert rule, make sure that its Status is Normal. Disable a single rule a. In the Operation column of the target alert rule, click the icon, and then click Disable. b. In the Disable Alert Rule dialog box, click OK. Disable rules in a batch a. Select the check boxes next to the target alert rules, and then click Disable in the lower-left corner of the list. b. In the Disable Alert Rule dialog box, click OK. |

| Enable an alert rule | After you finish the maintenance or upgrade of a cloud product, re-enable the disabled alert rules. Note Before enabling an alert rule, make sure that its Status is Disabled. Enable a single rule a. In the Operation column of the target alert rule, click Enable. b. In the Enable Alert Rule dialog box, click OK. Enable rules in a batch a. Select the check boxes next to the target alert rules, and then click Enable in the lower-left corner of the list. b. In the Enable Alert Rule dialog box, click OK. |
|---|---|
| Delete an alert rule | Delete a single rule a. In the Operation column of the target alert rule, click the icon, and then click Delete. b. In the Delete Alert Rule dialog box, click OK. Delete rules in a batch a. Select the check boxes next to the target alert rules, and then click Delete in the lower-left corner of the list. b. In the Delete Alert Rule dialog box, click OK. |

## 12 Data security

### 12.1 Configure an IP address whitelist

**whitelist**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are used for database access to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your RDS instance, the workloads on the instance are not affected. To configure a whitelist, you can perform the following operations: Configure an IP address whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance. Configure an Elastic Compute Service (ECS) security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Usage notes**

The default IP address whitelist can be modified or cleared, but cannot be deleted. You can add up to 1,000 IP addresses or CIDR blocks to a whitelist. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 192.168.1.0/24.

**Configure a standard IP address whitelist**

1. Log on to the ApsaraDB for RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Security Controls**.
4. On the **Whitelist Settings** tab, click **Edit** corresponding to an IP address whitelist.

**Note**

If you want to connect an ECS instance to an ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type. Otherwise, the connection fails. You can also click **Create Whitelist** to create an IP address whitelist.
5. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that you want to
allow to access your RDS instance and click **OK**. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.xx format can access your RDS instance. If you enter more than one IP address or CIDR block, separate them with commas (,). Do not add spaces preceding or following the commas. Example:

```
 192.168.0.1,172.16.213.9 .
```

If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

**Note**

If you add a new IP address or CIDR block to the **default** whitelist, the default address 127.0.0.1 is deleted.

### 12.2 Configure SSL encryption

This topic describes how to make data transmission more secure by configuring Secure Sockets Layer (SSL) encryption. You must enable SSL encryption and install SSL certificates that are issued by certificate authorities (CAs) to the required applications. SSL is used to encrypt connections at the transport layer and enhance the security and integrity of the transmitted data. However, SSL encryption increases the round-trip time.

**Prerequisites**

Your ApsaraDB RDS instance runs one of the following MySQL versions and RDS editions: MySQL 8.0 on RDS High-availability Edition (with local SSDs) MySQL 5.7 on RDS High-availability Edition (with local SSDs)

**Usage notes**

An SSL certificate remains valid for one year. Before the used SSL certificate expires, you must update the validity period of the SSL certificate. If you do not update the expired SSL certificate, the RDS instance still runs as expected and no security risks occur. However, your application cannot establish encrypted connections to the RDS instance. When the certificate is about to expire, Alibaba Cloud will notify you by sending emails or internal messages. You can view the internal messages on the Event Center page. SSL encryption may cause a sharp increase in CPU utilization. We recommend that you enable SSL encryption only if you want to encrypt the connections that are established to the public endpoint of your RDS instance. In most cases, connections that are established to the internal endpoint of your cluster are secure and do not require SSL encryption. SSL encryption is not supported for the connections to the read/write splitting endpoint of your RDS instance. If you disable SSL encryption, your RDS instance restarts. Proceed with caution.

**Enable SSL encryption**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. In the **SSL Settings** section, turn on **SSL Encryption**.
6. In the **Configure SSL Encryption** dialog box, select the endpoint for which you want to
enable SSL encryption and click **OK**.
7. Click Download CA Certificate to download the SSL CA certificate files in a compressed
package. The file that you downloaded is a package that contains the following files: P7B file: contains the server CA certificate that can be imported into a Windows operating system. PEM file: a CA certificate file that is used for an operating system or application that is not Windows-based. JKS file: an SSL certificate file that is stored in the Java-supported truststore. You can use this file to import the SSL certificate files from an SSL certificate chain into Java-based applications. The default password is apsaradb.

**Note**

If the JKS file is used in Java, you must modify the default JDK security configuration in JDK 7 and JDK 8. Open the `/jre/lib/security/java.security` file on the host where your application resides and modify the following configurations:

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

If you do not modify these configurations, the following error is reported. In most cases, other similar errors are also caused by invalid Java security configurations:

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

**Configure an SSL certificate**

After SSL encryption is enabled, you must configure an SSL certificate on your application or client to connect to your RDS instance. In this topic, MySQL Workbench and Navicat are used as examples. If you want to use other applications or clients, see the related instructions. Perform the following steps to configure an SSL certificate on MySQL Workbench:
1. Start MySQL Workbench.
2. Choose **Database > Manage Connections**.
3. In the **Connection** section, click the **SSL** tab and configure the following parameters.
①: Enable **Use SSL**. ②: Import the SSL CA certificate file. Configure a certificate on Navicat
1. Start Navicat.
2. Right-click the database and select **Edit Connection**.
3. Click the **SSL** tab. Select the path of the PEM-formatted CA certificate and complete the
required settings based on the following figure.
4. Click **OK**.

**Note**

If the `connection is being used` error message is displayed, the previous session remains connected. In this case, you must restart Navicat.
5. Double-click the database to test whether the database is connected.

**Update the validity period of an SSL CA certificate**

**Note**

The **Update Validity** operation causes your RDS instance to restart. Proceed with caution.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. Click **Update Validity**.

**Disable SSL encryption**

**Note**

When you disable SSL encryption, your RDS instance restarts. In this case, the system triggers a primary/secondary switchover to reduce the impacts on your workloads. We still recommend that you disable SSL encryption during off-peak hours. Disabling SSL encryption enhances access performance but reduces security for the RDS instance. We recommend that you disable SSL encryption only in secure environments.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. In the **SSL Settings** section, turn off **SSL Encryption**. In the message that appears, click
**OK**.

### 12.3 Configure TDE

Transparent Data Encryption (TDE) allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to the disk and is decrypted when it is read from the disk to the memory. After you enable TDE for your RDS instance, the size of data files in your RDS instance does not increase. You can use TDE without the need to modify the configurations of your application.

**Prerequisites**

Your ApsaraDB RDS instance runs the RDS High-availability Edition with local disks. Key Management Service (KMS) is activated. If KMS is not activated, you can activate it as prompted when you enable TDE.

**Background information**

The key that is used for TDE is created and managed by KMS. ApsaraDB RDS does not provide the key or certificates that are required for TDE. In some zones, you can use an automatically generated key or a custom key that is generated from your own key material. After you select a key, you must authorize your RDS instance to use that key.

**Usage notes**

When TDE is being enabled, your ApsaraDB RDS instance is restarted and all services are disconnected. Make appropriate service arrangements before you enable TDE. Proceed with caution. After you enable TDE, you cannot disable TDE. After you enable TDE, you cannot change the key that is used for TDE. After you enable TDE, you must decrypt the data on your RDS instance if you want to restore the data to an on-premises database. For more information, see Decrypt a table. After you enable TDE, the CPU utilization of your RDS instance significantly increases. If you use an existing custom key for TDE, take note of the following information: If you disable the key, configure a plan to delete the key, or delete the key material, the key becomes unavailable. If your RDS instance restarts after you revoke the key, your RDS instance becomes unavailable. You must use an Alibaba Cloud account or an account to which the AliyunSTSAssumeRoleAccess policy is attached.

**Note**

For more information, see topics about key management in **Key Management**
**Service > User Guide**.

**Use a key that is automatically generated by Alibaba Cloud**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **TDE** tab.
5. In the **TDE Settings** section, turn on **TDE Status**.
6. In the dialog box that appears, select **Use Automatically Generated Key** and click **OK**.

**Note**

If the instance runs MySQL 5.7 on RDS High-availability Edition, you can select one of the following encryption methods: SM4 encryption AES_256_CBC encryption

**Use an existing custom key**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click Data Security.
4. Click the **TDE** tab.
5. In the **TDE Settings** section, turn on **TDE Status**.
6. In the dialog box that appears, select **Use an existing custom key** and click **OK**.

**Note**

If you do not have a custom key, you need to click **go to the KMS console** to create a CMK and import your own key material. For more information, see the **Create a key** section in **Key Management ServiceKey Management Service > User Guide**.

**Encrypt a table**

Log in to the database and execute the following statement to encrypt a table: MySQL 5.7 or MySQL 8.0

```
alter table <tablename> encryption='Y';
```

**Decrypt a table**

Execute the following statement to decrypt a table that is encrypted by using TDE: MySQL 5.7 or MySQL 8.0

```
alter table <tablename> encryption='N';
```

**FAQ**

After I enable TDE, can I use common database tools such as Navicat? Yes, after you enable TDE, you can use common database tools such as Navicat. After I enable TDE, why is my data still in plaintext? After you enable TDE, your data is stored in ciphertext. However, when the data is queried, it is decrypted and loaded in plaintext to the memory. A: TDE encrypts backup files to prevent data leaks. Before you restore the data of your ApsaraDB RDS instance from an encrypted backup file to your computer, you must decrypt the file. For more information, see the "Decrypt a table" section of this topic.

### 12.4 SQL Audit

This topic describes how to use the SQL audit feature on an ApsaraDB RDS instance. You can use the SQL audit feature to view the details about the SQL statements that are executed on your RDS instance and audit the SQL statements on a regular basis. The SQL audit feature does not affect instance performance.

**Background information**

**Note**

You cannot view the SQL statements that are executed before the SQL audit feature is enabled. You can view the incremental data of your ApsaraDB RDS for MySQL instance in SQL audit logs or binary logs. The two methods differ in the following ways: SQL audit logs are similar to audit logs in MySQL. They record all DML and DDL operations using network protocol analysis. SQL audit does not parse the actual parameter values. If many SQL statements are executed to query data, a small amount of data may be lost. The incremental data obtained using this method may be inaccurate. Binary logs record all add, delete, and modify operations that are performed in the database and the incremental data that is used to restore data. Binary logs are temporarily stored in your instance after they are generated. The system transfers full binary log files to an Object Storage Service (OSS) bucket on a regular basis. The binary log files are stored in the OSS bucket for seven days. If data is being written to a binary log file, the file cannot be transferred. Therefore, after you click **Upload Binlogs** on the **Backup and**
**Restoration** page, some binary log files are not uploaded to the OSS bucket. You can use
this method to obtain accurate incremental data. However, you cannot use this method to obtain real-time logs.

**Usage notes**

By default, SQL audit is enabled. SQL audit logs are retained for seven days. The retention period of SQL audit log files is one hour. The system automatically deletes the SQL audit log files that are stored for longer than one hour. In the SQL audit feature, the maximum length of a single SQL statement is 4 KB.

**Disable the SQL audit feature**

**Note**

After the SQL audit feature is disabled, all SQL audit logs, including historical SQL audit logs, are deleted. Before you disable the SQL audit feature, we recommend that you export the SQL audit logs to your on-premises machine. If you no longer require the SQL audit feature, you can disable the feature to reduce costs.
1. Log in to the ApsaraDB RDS console.
2. In the navigation pane on the left, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the
**Operations** column to go to the **Basic Information** page.
3. In the navigation pane on the left, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Click **Export File** to export the SQL audit logs to your on-premises machine.
6. After the logs are exported, click **Disable SQL Auditing**.
7. In the message that appears, click **OK**.

**Enable the SQL audit feature**

1. Log in to the ApsaraDB RDS console.
2. In the navigation pane on the left, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the
**Operations** column to go to the **Basic Information** page.
3. In the navigation pane on the left, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Click **Enable SQL Auditing**.
6. In the message that appears, click **OK**.
After you enable the SQL Audit feature, you can query SQL statements based on filter criteria such as the time, DB, user, and keyword.

**Switch the storage location of audit logs**

By default, audit logs are stored in SLS-inner. If needed, you can switch the storage location to the publicly accessible SLS-PUB.
1. Log in to the ApsaraDB RDS console.
2. In the navigation pane on the left, click **Instances**. Find the target instance and click its ID,
or click **Manage** in the **Operations** column to go to the **Basic Information** page.
3. In the navigation pane on the left, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Enable storage of audit logs in SLS-PUB.

**Important**

This action cannot be reverted. Proceed with caution.

## 13 Service availability

### 13.1 Switch workloads between primary and secondary ApsaraDB RDS instances

**primary and secondary ApsaraDB**

**RDS instances**

This topic describes how to switch workloads between a primary ApsaraDB RDS instance and its secondary instance. ApsaraDB RDS supports both manual switchover and automatic switchover. After a switchover is complete, the primary ApsaraDB RDS instance becomes the secondary instance

**Feature overview**

ApsaraDB RDS supports both manual switchover and automatic switchover. Automatic switchover: By default, the automatic switchover feature is enabled. If the primary ApsaraDB RDS instance becomes faulty, ApsaraDB RDS automatically switches workloads over to the secondary instance. Manual switchover: You can manually switch workloads between the primary and secondary ApsaraDB RDS instances even when the automatic switchover feature is enabled.

**Usage notes**

Data is synchronized between the primary and secondary ApsaraDB RDS instances in real time. The secondary instance serves only as a read-only instance or standby. We recommend that you do not modify the data of the secondary instance. If you modify the data of the secondary instance, the data of the primary instance may be accidentally deleted or overwritten, which may irreparably impact your workloads. If the secondary ApsaraDB RDS instance serves as a read-only instance, the secondary instance serves as the new primary instance after a primary/secondary switchover. We recommend that you plan the read and write workloads for the new primary instance before the switchover. We recommend that you reserve and plan resources in advance. During a switchover, your service may be interrupted. Make sure that your application is configured to automatically reconnect to the instance. If the primary ApsaraDB RDS instance is attached with read-only instances, the read-only instances need to re-establish the connections that are used for data replication and synchronize incremental data after a switchover. As a result, data synchronization to the read-only instances has a latency of a few minutes.

**Manually perform a primary/secondary switchover**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Service Availability**.
4. On the right side of the page that appears, click **Switch Primary/Secondary Instance**.

**Note**

You may encounter one or two service interruptions during a switchover. Make sure that your application is configured to automatically reconnect to the instance.
5. In the dialog box that appears, click **OK**.

**Note**

In the dialog box, you can also select **Switch Within Maintenance Window** and click
**OK**. Then, the system performs the primary/secondary switchover within the specified
maintenance window. For more information about how to set the maintenance window, see Set a maintenance window. You can also click **Modify** on the right to change the maintenance window.

**FAQ**

Q: Can I connect to secondary instances? A: No, you cannot connect to secondary instances in the same manner as you connect to the primary instance. Secondary instances serve only as a read-only instance or standby. We recommend that you do not modify the data of secondary instances. If you modify the data of secondary instances, the data of the primary instance may be accidentally deleted or overwritten, which may irreparably impact your workloads.

### 13.2 Change the data replication mode

**mode**

You can set the data replication mode between primary and secondary ApsaraDB RDS for MySQL instances to improve database availability.

**Prerequisites**

Your ApsaraDB RDS for MySQL instance runs the High-availability Edition.

**Data replication modes**

Semi-synchronous mode After an update that is initialized by your application is complete on the primary instance, logs are synchronized to all the secondary instances. After the secondary instances receive the logs, the update transaction is considered committed. Your database system does not need to wait for the logs to be replayed. If the secondary instances are unavailable or a network interruption occurs between the primary and secondary instances, the semi-synchronous mode is demoted to the asynchronous mode. Asynchronous mode When your application initiates a request to add, delete, or modify data, the primary instance responds to your application immediately after it completes the requested operation. At the same time, the primary instance asynchronously replicates data to the secondary instances. During asynchronous data replication, the unavailability of secondary instances does not affect the operations on the primary instance. Data remains consistent even if the primary instance is unavailable.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Service Availability**.
4. On the right side of the page that appears, click **Change Data Replication Mode**.
5. In the dialog box that appears, select a data replication mode and click **OK**.

**FAQ**

Q: Which data replication mode is recommended? A: You can select a data replication mode based on your business requirements. If you require quick responses, we recommend that you select the asynchronous mode. In other scenarios, you can select the semi-synchronous mode. ation

## 14 Database backup and restoration

**restoration**

### 14.1 Configure automatic backup

Automatic backup of ApsaraDB RDS supports full physical backups. ApsaraDB RDS automatically backs up data based on pre-configured policies. This topic describes how to configure a policy for automatic backup.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. Click the **Backup Settings** tab.
5. Click **Edit** and configure the following parameters.

**Note**

To ensure data security, the system compares the new backup cycle and time with the original settings and selects the most recent point in time to back up the data. Therefore, the next backup may still be performed based on the original backup cycle and time. For example, assume that the scheduled backup cycle and time are set to 19:00-20:00 every Wednesday. If you modify the backup cycle and time to 19:00-20:00 every Thursday before the scheduled backup occurs, the system still backs up data at the original scheduled time of 19:00-20:00 on Wednesday.

| Parameter | Description |
|---|---|
| Backup Cycle | The backup cycle. You can select one or more days within a week. |
| Backup Time | A period of time within a day. Unit: hours. We recommend that you back up data during off-peak hours. |
| Retention Period | The retention period of regular backup (hot backup) and whether to retain the data for a long time before the instance is released. Note Data backup sets that are retained for more than 730 days will be automatically converted to archived backups (cold backup). The retention period of archived backups is at least 30 days. |

ation

| Log Backup | Specifies whether to enable log backup. Important If you disable log backup, all the log backup files are deleted and you cannot restore data to a specific point in time. |
|---|---|
| Log Backup Retention Period | The number of days for which log backup files are retained. Valid values: 7 to 730. Default value: 7. |

6. After you complete the configuration, click **Save**.

### 14.2 Manually back up an instance

Manual backup of ApsaraDB RDS supports both full physical and logical backups. This topic describes how to manually back up an ApsaraDB RDS instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the upper-right corner of the page that appears, click **Backup Instance**.
4. In the dialog box that appears, configure the backup mode and backup policy, and then
click **OK**.

**Note**

The following backup modes are available: Physical Backup: directly backs up all files in all databases. Logical Backup: extracts data from the databases by using SQL statements and backs up the data in the text format. If you select Logical Backup, you must select one of the following backup policies: Instance Backup: backs up the entire instance. Single-Database Backup: backs up one of the databases on the instance.

### 14.3 Download data backup files and log backup files

**and log backup files**

This topic describes how to download unencrypted data backup files and log backup files in the ApsaraDB RDS console to archive the files and restore data to an on-premises database.

**Limits**

| Database engine | Download of data backup files | Download of log backup files |
|---|---|---|

ation

| MySQL 5.7 on RDS High- availability Edition | Supported | Supported |
|---|---|---|
| MySQL 8.0 on RDS High- availability Edition | Supported | Supported |

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, click the ID of the
instance that you want to manage, or click **Manage** in the **Actions** column to go to the
**Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. Click the Data Backup or Log Backup tab.
To download data backup files, click the **Data Backup** tab. To download log backup files, click the **Log Backup** tab.
5. Select a time range to which you want to restore the instance.
6. Find the data backup file or log backup file that you want to download, and click **Download**
**Instance Backup** or **Download** in the **Actions** column.

**Note**

If the Download button is unavailable, check whether the requirements in the Limits section are met. If you want to download data backup file and use the backup file to restore data, we recommend that you select the data backup file created closest to the point in time when the required data exists. If the log backup file is used to restore the data of your RDS instance to an onpremises database, take note of the following items: The instance ID of the log backup file must be the same as the instance ID of the backup set that you select. The start time of the log backup file must be later than the end time of the backup set that you select and earlier than the point in time to which you want to restore the data of your RDS instance.
7. In the dialog box that appears, click **Download**.

| Download method | Description |
|---|---|

ation

| Download button | Use a browser to download the backup file. |
|---|---|
| Download URL | Copy the download URL. If you want to use other tools to download the file, use this method. |

**Note**

If you use a Linux operating system, you can run the following command to download the file:

```
wget -c '<Download URL of the backup file>' -O <File name>
```

The -c option enables resumable download. The -O option saves the downloaded file by using a specified name. We recommend that you use the file name contained in the download URL. If the URL contains more than one parameter, we recommend that you enclose the URL in a pair of single quotation marks (').

### 14.4 Use the Upload Binlogs feature to upload binary log files

**feature to upload binary log files**

**Background information**

ApsaraDB RDS for MySQL allows you to upload binary log files to Object Storage Service (OSS) for storage. This topic describes how to upload binary log files to OSS.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration** to go to the **Backup and**
**Restoration** page.
4. On the page that appears, click **Upload Binlogs**.
5. In the message that appears, click **OK**.

### 14.5 Restore data to a new instance (formerly known as cloning an instance)

**instance (formerly known as**

**cloning an instance)**

ation You can clone an instance that has the same content as the primary instance, including data and settings. This feature allows you to restore data of the primary instance or create multiple instances that are the same as the primary instance.

**Prerequisites**

Before you clone an instance, make sure that the following requirements are met: The primary instance is in the running state. The primary instance does not have any ongoing migration tasks. Data backup and log backup are enabled. The primary instance has at least one completed backup set before you clone the instance by backup set.

**Usage notes**

You can specify a backup set or a point in time within the backup retention period to clone an instance.

**Note**

A cloned instance copies only the content of the primary instance, but not the content of read-only instances. The copied data includes database information, account information, and instance settings, such as whitelist settings, backup settings, parameter settings, and alert threshold settings. The database engine of a cloned instance must be the same as that of the primary instance. Other settings can be different, such as the instance edition, zone, network type, instance type, and storage capacity. If you want to restore the data of a primary instance, we recommend that you select a higher instance type and larger storage capacity than those of the primary instance. This can accelerate the data restoration process. The account type of a cloned instance must be the same as that of the primary instance. The account password of the cloned instance can be changed.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the Data Backup tab, find the backup file from which you want to restore data and click
**Restore** in the Actions column.
5. In the message that appears, click **OK**.
6. On the **RDS restoration** page, configure the following parameters.

| Section | Parameter | Description |
|---|---|---|
| Area | Geography | The region in which the cloned instance resides. |

ation

| Database Recovery | Restore mode | The data restore mode of the primary instance. Valid values: By point in time By Backup Set |
|---|---|---|
|   | Restore time | The point in time to which you want to restore the primary instance. Note When Restore mode is set to By point in time, you must specify this parameter. |
|   | Backup Set | The backup set for restoration. Note When Restore mode is set to By Backup Set, you must specify this parameter. |
| Specification Configuration | Instance name | The name of the cloned instance. |
|   | Database Type | The database engine of the cloned instance, which cannot be modified. |
|   | Database Version | The engine version of the cloned instance, which cannot be modified. |
|   | Series | The RDS edition of the cloned instance. The actual values are displayed in the console. |
|   | Storage Type | The storage type of the cloned instance. The actual values are displayed in the console. |

ation

|   | Instance specifications | The instance type of the cloned instance. Note We recommend that you select a higher instance type and larger storage capacity than those of the primary instance. This can accelerate the data restoration process. |
|---|---|---|
|   | Storage space | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. The available storage capacity displayed in the console prevails. Note A dedicated AsparaDB RDS instance that uses local SSDs exclusively occupies the allocated resources, and its storage capacity varies based on the instance type. |
| Network Type | Network Type | The network type of the cloned instance. ApsaraDB RDS instances support the following network types: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by using security groups or whitelists. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. |
|   | VPC | The VPC in which the cloned instance resides. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
|   | vSwitch | The vSwitch in the VPC. Note When Network Type is set to Proprietary Network, you must specify this parameter. |

ation
7. After you complete the configuration, click **Submit**.

## 15 Autonomy services

### 15.1 Introduction to DAS

Database Autonomy Service (DAS) is a cloud service that uses machine learning and expert experience to automate perception, healing, optimization, O&M, and security for databases. DAS simplifies database management and prevents service failures that are caused by manual operations. This way, DAS helps ensure that the database service of users runs in a stable, secure, and efficient manner.

**Features**

In ApsaraDB RDS for MySQL, DAS provides the following features: Diagnostics You can diagnose your instance and view the visualized diagnostic results. Instance sessions You can view sessions, check session statistics, analyze SQL statements, and optimize the execution of SQL statements. Real-time monitoring You can view the real-time information about your instance, such as the queries per second (QPS), transactions per second (TPS), number of connections, and network traffic. You can view the storage overview, trends, exceptions, tablespaces, and data spaces. Deadlock analysis You can view and analyze the last deadlock in a database. Dashboard You can view and compare performance trends, customize monitoring dashboards, check exceptions, and view instance topologies. Slow query logs You can view the trends and statistics of slow queries. You can generate diagnostic reports or view automatically generated reports about instance health, alerts, and slow queries.

### 15.2 Perform quick diagnostics

**Go to the Diagnostics tab**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. On the page that appears, click the **Diagnostics** tab.

**Note**

For more information, see the **Diagnostics** topic in **Database Autonomy Service >**

**User Guide.**

### 15.3 Manage sessions

In ApsaraDB RDS for MySQL, autonomy services provide the session management feature. This feature allows you to view and manage sessions of an instance.

**Go to the Session Management tab**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. Click the **Session Management** tab.

**Note**

For more information, see the **Instance sessions** topic in **Database Autonomy**

**Service (DAS) > User Guide.**

### 15.4 View real-time performance

In ApsaraDB RDS for MySQL, autonomy services provide the real-time performance view. This feature allows you to view the real-time performance of MySQL.

**Go to the Real-Time Performance page**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. Click the **Real-Time Performance** tab.

**Note**

For more information, see the **Real-time monitoring** topic in **Database Autonomy**

**Service (DAS) > User Guide.**

### 15.5 Storage analysis

Database Autonomy Service (DAS) provides the storage analysis feature for ApsaraDB RDS for MySQL. You can use this feature to identify and fix storage exceptions in databases at the earliest opportunity to ensure database security.

**Background information**

The storage analysis feature allows you to view the storage usage and the number of remaining days for which storage is available on a database instance. This feature also allows you to view the storage usage of a specified table, tablespace fragments, and diagnostic results on the database.

**Go to the Storage Analysis tab**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. On the page that appears, click the **Storage Analysis** tab.

**Note**

For more information, see the **Storage analysis** topic in **Database Autonomy**
**Service User Guide**. **>**

### 15.6 Lock analysis

Database Autonomy Service (DAS) provides the lock analysis feature for ApsaraDB RDS for MySQL. You can use this feature to view and analyze the last deadlock of a database.

**Go to the Lock Analysis tab**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. On the page that appears, click the **Lock Analysis** tab.

**Note**

For more information, see the **Lock analysis** topic in **Database Autonomy Service**
**User Guide**.

### 15.7 Performance trends

Database Autonomy Service (DAS) provides the dashboard feature for ApsaraDB RDS for MySQL. This feature allows you to view performance trends in specific ranges, compare performance trends, and customize charts to view performance trends.

**Go to the Dashboard page**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Dashboard**.

**Note**

For more information, see the **Performance trends** topic in **Database Autonomy**
**Service User Guide**.

### 15.8 View slow query logs

In ApsaraDB RDS for MySQL, autonomy services provide the slow query logs feature. This feature allows you to view the trends of slow queries, execution details of slow queries, and optimization suggestions.

**Go to the Slow Query Logs page**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Slow Query Logs**.

**Note**

For more information, see the **Slow query logs** topic in **Database Autonomy**

**Service (DAS) > User Guide.**

### 15.9 Diagnostic reports

Database Autonomy Service (DAS) provides the diagnostic reports feature for ApsaraDB RDS for MySQL. This feature allows you to create and view diagnostic reports.

**Go to the Diagnostic Reports page**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostic Reports**.

**Note**

For more information, see the **Diagnostic reports** topic in **Database Autonomy**
**Service User Guide**. **>**

## 16 Log management

ApsaraDB RDS instances support log management. You can query the details of error and slow query logs of an ApsaraDB RDS instance by using the ApsaraDB RDS console. The logs help you perform troubleshooting.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to open the **Basic Information** page.
3. In the left-side navigation pane, click **Logs**.
4. On the **Logs** page, click the **Error Logs**, **Slow Query Logs**, or **Primary/Secondary**
**Switching Logs** tab. Specify a time range and click **OK**.

| Log | Content |
|---|---|
| Error Logs | Records database running errors that occurred within the last 15 days. |
| Slow Query Logs | Records SQL statements within the last 15 days that took longer than one second to execute. Duplicated SQL statements are removed. Note You can view and export slow query logs for any seven days within the last 15 days. |
| Slow Log Statistics | Summarizes SQL statements within the last 15 days that took longer than one second to execute. Note You can view slow log statistics for any seven days within the last 15 days. |
| Primary/Secondary Switching Logs | Records events of primary/secondary instance switchovers. This feature is available for ApsaraDB RDS for MySQL instances that run RDS High- availability Edition. |

MySQL data

## 17 Use mysqldump to migrate MySQL data

**migrate MySQL data**

This topic describes how to use mysqldump to migrate data from an on-premises database to an ApsaraDB RDS for MySQL instance.

**Prerequisites**

An ECS instance is created.

**Background information**

mysqldump is easy to use but requires extensive downtime. This tool is suitable for scenarios where the amount of data is small or extensive downtime is allowed. ApsaraDB RDS for MySQL is fully compatible with the native database service. The procedure of migrating data from the original database to an ApsaraDB RDS for MySQL instance is similar to that of migrating data from one MySQL server to another. Before you migrate data, you must create an account that is used to migrate data from the on-premises MySQL database. You must grant the read and write permissions on the onpremises MySQL databases to the account.

**Procedure**

1. Run the following command to create a migration account for the on-premises database:

```
 CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

Parameter description: username: the name of the account to be created. host: the host from which the account is authorized to log on to the on-premises MySQL database. If you want to allow access from a local host, set this parameter to **localhost**. If you want to allow access from all hosts, set this parameter to a percent sign (**%**). password: the password of the account. For example, you can run the following command to create an account with the username
**William** and the password **Changme123**. The account is authorized to log on to the on-
premises MySQL database from all hosts.

```
 CREATE USER 'William'@'%' IDENTIFIED BY 'Changme123';
```

2. Run the following command to grant permissions to the migration account in the on-
premises database:

```
 GRANT SELECT ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; GRANT
REPLICATION SLAVE ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; GRANT REPLICATION SLAVE ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

Parameter description: privileges: the operation permissions granted to the account, such as SELECT, INSERT, and UPDATE. To authorize the account to perform all operations, set this parameter to
**ALL**.
databasename: the name of the on-premises MySQL database. If you want to grant all database permissions to the account, set this parameter to an asterisk (*). tablename: the name of the table whose data you want to migrate. If you want to grant all table permissions to the account, set this parameter to an asterisk (*). username: the name of the account. host: the host from which the account is authorized to log on to the on-premises MySQL MySQL data database. If you want to allow access from a local host, set this parameter to **localhost**. If you want to allow access from all hosts, set this parameter to a percent sign (**%**). WITH GRANT OPTION: authorizes the account to use the GRANT statement. This parameter is optional. For example, you can execute the following statement to grant all permissions on tables and databases to the **William** account. The account is authorized to log on to the database from all hosts.

```
 GRANT ALL ON *. * TO 'William'@'%';
```

3. Use the data export tool of mysqldump to export data from the database as a data file.

**Important**

Do not update data during data export. In this step, only data is exported. Stored procedures, triggers, and functions are not exported.

```
 mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob
dbName --skip-triggers > /tmp/dbName.sql
```

Parameter description: localIp: the IP address of the host where the on-premises MySQL database resides. userName: the account that is used to migrate data from the on-premises MySQL database. dbName: the name of the on-premises MySQL database. /tmp/dbName.sql: the name of the exported data file.
4. Use mysqldump to export stored procedures, triggers, and functions.

**Important**

Skip this step if no stored procedures, triggers, or functions are used in the database. When stored procedures, triggers, and functions are exported, you must remove the DEFINER to ensure compatibility with ApsaraDB RDS for MySQL.

```
 mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob
dbName -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/triggerProcedure.sql
```

Parameter description: localIp: the IP address of the host where the on-premises MySQL database resides. userName: the account that is used to migrate data from the on-premises MySQL database. dbName: the name of the on-premises MySQL database. /tmp/triggerProcedure.sql: the name of the exported stored procedure file.
5. Upload the data file and stored procedure file to the ECS instance.
In this example, the files are uploaded to the following paths:

```
 /tmp/dbName.sql
 /tmp/triggerProcedure.sql
```

6. Log on to the ECS console and import both the data file and the stored procedure file to the
destination ApsaraDB RDS for MySQL instance.

**Note**

For information about how to log on to the ECS instance, see topics in the
**Connect to an instance** section of ECS User Guide.

| mysql -h intranet4example.mysql.rds.aliyuncs.com –u userName -p dbName < |   |
|---|---|

MySQL data

```
 mysql -h intranet4example.mysql.rds.aliyuncs.com -u userName -p dbName <
/tmp/triggerProcedure.sql
```

Parameter description: intranet4example.mysql.rds.aliyuncs.com: the endpoint of the ApsaraDB RDS for MySQL instance. An internal endpoint is used in this example. userName: the migration account of the ApsaraDB RDS for MySQL database. dbName: the name of the on-premises MySQL database from which you want to import data. /tmp/dbName.sql: the name of the data file that you want to import. /tmp/triggerProcedure.sql: the name of the stored procedure file that you want to import.
