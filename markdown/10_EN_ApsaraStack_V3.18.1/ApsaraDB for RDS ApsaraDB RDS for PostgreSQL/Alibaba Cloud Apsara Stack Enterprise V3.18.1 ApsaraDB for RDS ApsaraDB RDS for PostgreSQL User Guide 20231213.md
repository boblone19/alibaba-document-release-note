---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20231213"
product_version: "V3.18.1"
doc_version: "20231213"
pdf_pages: 132
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20231213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/RDS/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20ApsaraDB%20for%20RDS%20ApsaraDB%20RDS%20for%20PostgreSQL%20User%20Guide%2020231213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20231213

## Table of Contents

- 1 What is ApsaraDB RDS?
- 2 Limits on ApsaraDB RDS for PostgreSQL
- 3.[Announcement] ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL 10 are no longer available for purchase in Apsara Stack V3.18
- 4 Instance types
- 5 Log on to the ApsaraDB RDS console
- 6 Quick Start
  - 6.1 Procedure
  - 6.2 Create an instance
  - 6.3 Configure an IP address whitelist
  - 6.4 Create a database and an account
  - 6.5 Connect to an ApsaraDB RDS for PostgreSQL instance
- 7 Instances
  - 7.1 Create an instance
  - 7.2 View basic information of an instance
  - 7.3 Restart an instance
  - 7.4 Change the specifications of an instance
  - 7.5 Set a maintenance window
  - 7.6 Configure primary/secondary switchover
  - 7.7 Release an instance
  - 7.8 Configure instance parameters
  - 7.9 Read-only instances
    - 7.9.1 Overview of read-only ApsaraDB RDS for PostgreSQL instances
    - 7.9.2 Create a read-only ApsaraDB RDS for PostgreSQL instance
    - 7.9.3 View a read-only ApsaraDB RDS for PostgreSQL instance
    - 7.9.4 Manage a read-only ApsaraDB RDS for PostgreSQL instance
- 8 Database connection
  - 8.1 Connect to an ApsaraDB RDS for PostgreSQL instance
  - 8.2 Use DMS to log on to an ApsaraDB RDS instance
  - 8.3 View and modify the internal endpoint and port number
- 9 Accounts
  - 9.1 Create an account
  - 9.2 Reset the password of a database account
  - 9.3 Lock or delete an account from an instance
  - 9.4 Delete an account
- 10 Databases
  - 10.1 Create a database
  - 10.2 Delete a database
- 11 Networks, VPCs, and vSwitches
  - 11.1 Change the VPC and vSwitch of an instance
  - 11.2 Change the network type of an ApsaraDB RDS for PostgreSQL instance
  - 11.3 Configure hybrid access from both the classic network and VPCs
- 12 Monitoring
  - 12.1 View monitored resources
- 13 Data security
  - 13.1 Switch to the enhanced whitelist mode
  - 13.2 Configure an IP address whitelist
  - 13.3 Configure SSL encryption
  - 13.4 Configure data encryption
  - 13.5 Configure TDE
- 14 Logs and audit
  - 14.1 Configure SQL audit
  - 14.2 Manage logs
- 15 Backup
  - 15.1 Back up an ApsaraDB RDS for PostgreSQL instance
  - 15.2 Download data and log backup files
  - 15.3 Create a logical backup for an ApsaraDB RDS for PostgreSQL instance
  - 15.4 Create a full backup of an ApsaraDB RDS for PostgreSQL instance
- 16 Restoration
  - 16.1 Restore data of an ApsaraDB RDS for PostgreSQL instance
  - 16.2 Restore data from a logical backup file
- 17 CloudDBA
  - 17.1 Introduction to CloudDBA
  - 17.2 Diagnostics
  - 17.3 Session management
  - 17.4 Real-time monitoring
  - 17.5 Storage analysis
  - 17.6 Dashboard
  - 17.7 Slow query logs
- 18 Plug-ins
  - 18.1 Plug-ins supported
  - 18.2 Use mysql_fdw to read and write data from and to a MySQL database
  - 18.3 Use oss_fdw to read and write foreign data files
- 19 Use Pgpool for read/write splitting in ApsaraDB RDS for PostgreSQL
- 20 Use ShardingSphere to develop ApsaraDB RDS for PostgreSQL

## 1 What is ApsaraDB RDS?

ApsaraDB RDS is a stable, reliable, and scalable online database service that is built on top of Apsara Distributed File System and high-performance storage. It provides a comprehensive portfolio of solutions for disaster recovery, backup, restoration, monitoring, and migration to facilitate database O&M. ApsaraDB RDS supports four database engines: MySQL, SQL Server, PolarDB, and PostgreSQL. You can create database instances based on these database engines to meet your business requirements. This topic describes the PostgreSQL engine.

**ApsaraDB RDS for PostgreSQL**

ApsaraDB RDS for PostgreSQL is an advanced database service that is fully compatible with SQL syntax and supports a diverse range of data such as JSON, IP, and geometric data. It supports SQL:2003 and later, as well as procedural SQL languages such as PL/pgSQL and PL/Java. It also supports Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC). In addition to features such as transactions, subqueries, multi-version concurrency control (MVCC), and data integrity check, ApsaraDB RDS for PostgreSQL integrates a series of features including high availability, backup, and restoration to ease O&M loads. for PostgreSQL

## 2 Limits on ApsaraDB RDS for PostgreSQL

**PostgreSQL**

Before you use ApsaraDB RDS for PostgreSQL, you must understand its limits and take the necessary precautions. The following table describes the limits on ApsaraDB RDS for PostgreSQL.

| Operation | Limit |
|---|---|
| Root permissions of databases | Superuser permissions are not provided. |
| Database replication | ApsaraDB RDS for PostgreSQL provides a primary/secondary replication architecture except in the Basic Edition. The secondary instances in the architecture are hidden and cannot be accessed by your applications. |
| Instance restart | Instances must be restarted by using the ApsaraDB RDS console or API operations. |

DB RDS instances that run Postgr eSQL 9.4 and PostgreSQL 10 are no longer available for purchase i n Apsara Stack V3.18

**3.[Announcement] ApsaraDB**

**RDS instances that run**

**PostgreSQL 9.4 and**

**PostgreSQL 10 are no longer**

**available for purchase in**

**Apsara Stack V3.18**

ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL 10 are no longer available for purchase in Apsara Stack V3.18. Only technical support is provided for these instances.

**Involved edition**

Apsara Stack V3.18

**Involved instance**

ApsaraDB RDS instances that run PostgreSQL 9.4 ApsaraDB RDS instances that run PostgreSQL 10

**Causes**

The open source PostgreSQL community no longer provides maintenance for PostgreSQL 9.4 or PostgreSQL 10. If you continue to use PostgreSQL 9.4 and PostgreSQL 10, you may encounter potential risks.

**Impacts**

You can no longer purchase ApsaraDB RDS instances that run PostgreSQL 9.4 or PostgreSQL 10. The existing ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL 10 can run as expected. However, Alibaba Cloud no longer provides updates or maintenance for the minor engine versions of ApsaraDB RDS instances that run PostgreSQL 9.4 and PostgreSQL
10. Alibaba Cloud provides only technical support for these instances.

**Suggestions**

If you want to purchase an ApsaraDB RDS for PostgreSQL instance, we recommend that you select PostgreSQL 11 or later.

## 4 Instance types

This topic describes the instance types of ApsaraDB RDS for PostgreSQL. Different instance types deliver different performance.

**IOPS**

The maximum IOPS of an ApsaraDB RDS instance that uses local SSDs varies based on the instance type. The maximum IOPS of an ApsaraDB RDS instance that uses cloud disks varies based on the instance type and storage capacity. The following formula can be used to calculate the IOPS of an ApsaraDB RDS instance that uses cloud disks. The storage capacity is measured in GB.

```
min{1800 + 30 × Storage capacity, 25000}
```

> **Note:** If the throughput of an RDS instance reaches the upper limit, the IOPS of the instance also decreases.

**Primary instance**

**Local SSD**

| Instance family | Instance type | Number of CPU cores and memory capacity | Maximum IOPS | Maximum number of connections | Storage capacity |
|---|---|---|---|---|---|
| Dedicated instance types (with a large memory capacity) | pg.x8.mediu m.2 | 2 cores, 16 GB | 4,500 | 2,500 | 20 GB - 6,000 GB |
|   | pg.x8.large.2 | 4 cores, 32 GB | 9,000 | 5,000 |   |
|   | pg.x8.xlarge. 2 | 8 cores, 64 GB | 18,000 | 10,000 |   |
|   | pg.x8.2xlarge .2 | 16 cores, 128 GB | 36,000 | 12,000 |   |
|   | pg.x4.large.2 | 4 cores, 16 GB | 4,500 | 2,500 |   |
|   | pg.x4.xlarge. 2 | 8 cores, 32 GB | 9,000 | 5,000 |   |

| psaraDB for RDS |   |   |   |   |   |
|---|---|---|---|---|---|
| Dedicated instance types (with a large number of cores) |   |   |   |   |   |
|   | pg.x4.2xlarge .2 | 16 cores, 64 GB | 18,000 | 10,000 |   |
|   | pg.x4.4xlarge .2 | 32 cores, 128 GB | 36,000 | 12,000 |   |
| Dedicated host instance types | rds.pg.st.h43 | 60 cores, 470 GB | 50,000 | 4,000 |   |

**Cloud disk**

| Instance family | Instance type | Number of CPU cores and memory capacity | Maximum IOPS | Maximum number of connections | Storage capacity |
|---|---|---|---|---|---|
| General- purpose instance types | pg.n2.small.2 c | 1 core, 2 GB | 50,000 | 200 |   |
|   | pg.n2.mediu m.2c | 2 cores, 4 GB | 50,000 | 400 |   |
|   | pg.x4.mediu m.2c | 2 cores, 8 GB | 50,000 | 800 |   |
|   | pg.x8.mediu m.2c | 2 cores, 16 GB | 50,000 | 1,600 |   |
|   | pg.x2.large.2 c | 4 cores, 8 GB | 50,000 | 800 |   |
|   | pg.x4.large.2 c | 4 cores, 16 GB | 50,000 | 1,600 |   |
|   | pg.x8.large.2 c | 4 cores, 32 GB | 50,000 | 3,200 |   |
|   | pg.x2.xlarge. 2c | 8 cores, 16 GB | 50,000 | 1,600 |   |
|   | pg.x4.xlarge. 2c | 8 cores, 32 GB | 50,000 | 3,200 |   |

|   | pg.x8.xlarge. 2c | 8 cores, 64 GB | 50,000 | 6,400 |   |
|---|---|---|---|---|---|
|   | pg.x2.3large. 2c | 12 cores, 24 GB | 50,000 | 2,400 |   |
|   | pg.x4.3large. 2c | 12 cores, 48 GB | 50,000 | 4,800 |   |
|   | pg.x8.3large. 2c | 12 cores, 96 GB | 50,000 | 9,600 |   |
| Dedicated instance types |   |   |   |   |   |
|   | pg.x2.2xlarge .2c | 16 cores, 32 GB | 50,000 | 3,200 |   |
|   | pg.x4.2xlarge .2c | 16 cores, 64 GB | 50,000 | 6,400 |   |
|   |   |   |   |   | 20 GB - 6,000 GB |
|   | pg.x8.2xlarge .2c | 16 cores, 128 GB | 50,000 | 12,800 |   |
|   | pg.x2.3xlarge 2c | 24 cores, 48 GB | 50,000 | 4,800 |   |
|   | pg.x4.3xlarge .2c | 24 cores, 96 GB | 50,000 | 19,200 |   |
|   | pg.x8.3xlarge .2c | 24 cores, 196 GB | 50,000 | 19,200 |   |
|   | pg.x2.4xlarge .2c | 32 cores, 64 GB | 50,000 | 6,400 |   |
|   | pg.x4.4xlarge .2c | 32 cores, 128 GB | 50,000 | 12,800 |   |
|   | pg.x8.4xlarge .2c | 32 cores, 256 GB | 50,000 | 25,600 |   |
|   | pg.x2.13large .2c | 52 cores, 96 GB | 50,000 | 10,400 |   |

|   | pg.x4.13large .2c | 52 cores, 192 GB | 50,000 | 19,200 |   |
|---|---|---|---|---|---|
|   | pg.x8.13large .2c | 52 cores, 384 GB | 50,000 | 38,400 |   |
|   | pg.x2.8xlarge .2c | 64 cores, 128 GB | 50,000 | 12,800 |   |
|   | pg.x4.8xlarge .2c | 64 cores, 256 GB | 50,000 | 25,600 |   |
|   | pg.x8.8xlarge .2c | 64 cores, 512 GB | 50,000 | 51,200 |   |
|   | pg.x2.13xlarg e.2c | 104 cores, 192 GB | 50,000 | 19,200 |   |
|   | pg.x4.13xlarg e.2c | 104 cores, 384 GB | 50,000 | 38,400 |   |
|   | pg.x8.13xlarg e.2c | 104 cores, 768 GB | 50,000 | 76,800 |   |

**Read-only instance**

| Instance type | Number of CPU cores and memory capacity | Maximum number of connections |
|---|---|---|
| pgro.n2.small.1c | 1 core, 2 GB | 200 |
| pgro.n2.medium.1c | 2 cores, 4 GB | 400 |
| pgro.x4.medium.1c | 2 cores, 8 GB | 800 |
| pgro.x8.medium.1c | 2 cores, 16 GB | 1,600 |
| pgro.x2.large.1c | 4 cores, 8 GB | 800 |
| pgro.x4.large.1c | 4 cores, 16 GB | 1,600 |

| pgro.x8.large.1c | 4 cores, 32 GB | 3,200 |
|---|---|---|
| pgro.x2.xlarge.1c | 8 cores, 16 GB | 1,600 |
| pgro.x4.xlarge.1c | 8 cores, 32 GB | 3,200 |
| pgro.x8.xlarge.1c | 8 cores, 64 GB | 6,400 |
| pgro.x2.3.large.1c | 12 cores, 24 GB | 2,400 |
| pgro.x4.3.large.1c | 12 cores, 48 GB | 4,800 |
| pgro.x8.3.large.1c | 12 cores, 96 GB | 9,600 |
| pgro.x2.2.xlarge.1c | 16 cores, 32 GB | 3,200 |
| pgro.x4.2.xlarge.1c | 16 cores, 64 GB | 6,400 |
| pgro.x8.2.xlarge.1c | 16 cores, 128 GB | 12,800 |
| pgro.x2.3.xlarge.1c | 24 cores, 48 GB | 4,800 |
| pgro.x4.3.xlarge.1c | 24 cores, 96 GB | 9,600 |
| pgro.x8.3.xlarge.1c | 24 cores, 192 GB | 19,200 |
| pgro.x2.4.xlarge.1c | 32 cores, 64 GB | 6,400 |
| pgro.x4.4.xlarge.1c | 32 cores, 128 GB | 12,800 |
| pgro.x8.4.xlarge.1c | 32 cores, 256 GB | 25,600 |
| pgro.x2.13.large.1c | 52 cores, 104 GB | 10,400 |
| pgro.x4.13.large.1c | 52 cores, 192 GB | 19,200 |
| pgro.x8.13.large.1c | 52 cores, 384 GB | 38,400 |

| pgro.x2.8.xlarge.1c | 64 cores, 128 GB | 12,800 |
|---|---|---|
| pgro.x4.8.xlarge.1c | 64 cores, 256 GB | 25,600 |
| pgro.x8.8.xlarge.1c | 64 cores, 512 GB | 51,200 |
| pgro.x2.13.xlarge.1c | 104 cores, 192 GB | 19,200 |
| pgro.x4.13.xlarge.1c | 104 cores, 384 GB | 38,400 |
| pgro.x8.13.xlarge.1c | 104 cores, 768 GB | 76,800 |

RDS console

## 5 Log on to the ApsaraDB RDS console

**RDS console**

This topic describes how to log on to the ApsaraDB RDS console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.

**Procedure**

1. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

2. Click **Log On**.
3. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

4. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**.

## 6 Quick Start

### 6.1 Procedure

ApsaraDB RDS quick start covers the following topics: creating an ApsaraDB RDS instance, configuring a whitelist, creating a database, creating an account, and connecting to the instance.

**Flowchart for an ApsaraDB RDS instance**

If you are using ApsaraDB RDS for the first time, you can start with Limits. The following figure shows the operations that you must perform before you use an ApsaraDB RDS instance.

### 6.2 Create an instance

This topic describes how to create an ApsaraDB RDS for PostgreSQL instance in the ApsaraDB RDS console.

**Procedure**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, click **Create Instance**.
3. Configure the following parameters.

| Section | Paramete r | Description |
|---|---|---|
| Basic Configura tions | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
| Area | Region | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|   | Primary Node Zone | The zone where the primary instance is deployed. |
|   | Deploym ent Method | Specifies whether to deploy the primary and secondary instances in different zones. ApsaraDB RDS supports Multi-zone Deployment and Single-zone Deployment. A deployment method is automatically selected based on the value of Primary Node Zone. |
|   | Database Engine | The database engine of the instance. Select PostgreSQL. |
|   | Engine Version | The version of the database engine. Valid values: 11.0 12.0 13.0 |
|   | Edition | The RDS instance edition. Select High-availability Edition. |

| Specificat ions |   |   |
|---|---|---|
|   | Storage Type | The storage type of the instance. Local SSDs and standard SSDs are supported. The storage types that are supported vary based on the engine version: PostgreSQL 11.0: Local SSDs and standard SSDs are supported. PostgreSQL 12.0: Local SSDs and standard SSDs are supported. PostgreSQL 13.0: Local SSDs and standard SSDs are supported. |
|   | Encrypte d | Specifies whether to encrypt standard SSDs. This parameter is available only when you set the Storage Type parameter to Standard SSD. If you select Encrypted, you must specify the Encryption Key parameter. If you do not have a key, you must first create one in the Key Management Service (KMS) console. For more information, see User Guide > Create a CMK in Key Management Service. |
|   | Encryptio n Key | The key that is used to encrypt standard SSDs. This parameter is available only when you select Encrypted. |
|   | Instance Specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The maximum storage capacity that is provisioned to store data files, system files, binary log files, and transaction files in the RDS instance. Valid values: 20 to 6000. Unit: GB. The value is in 5 GB increments. |
|   | Connecti on Type | The connection type of the instance. Valid Values: Internet: Instances of this connection type can be connected over the Internet. Internal Network: Instances of this connection type can be connected over an internal network. Note After the instance is created, its connection type cannot be changed. Proceed with caution. |

| Network |   |   |
|---|---|---|
|   | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Note If you configure multi-zone deployment, you must create vSwitches for the zones of primary and secondary instances in the specified VPC. If you select VPC, you must specify a VPC and a vSwitch. |
|   | VPC | If you set Network Type to VPC, you must select a VPC and a vSwitch. |
|   | vSwitch Zone |   |
|   | VSwitch |   |
|   | IP Whitelist | The IP address or CIDR block that is allowed to connect to the RDS instance. |
| Instance Settings | Quantity | The number of instances that you want to create. Default value: 1. |
|   | Instance Name | The name of the instance. It must be 2 to 64 characters in length. It must start with a letter. It can contain letters, digits, and the following special characters: - : _ It cannot start with http:// or https://. |

4. Click **Submit**.

### 6.3 Configure an IP address whitelist

**whitelist**

This topic describes how to configure a whitelist for an ApsaraDB RDS instance. Only entities that are listed in a whitelist can access your ApsaraDB RDS instance.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure and do not interrupt the operations of your ApsaraDB RDS instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance.

> **Note:** The IP address whitelist labeled default contains only the default IP address 0.0.0.0/0, which allows all entities to access your ApsaraDB RDS instance.

Configure an ECS security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

> **Note:** You can also click **Create Whitelist** to create a whitelist.

6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks used to access the
instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your ApsaraDB RDS instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Alibaba Cloud account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### 6.4 Create a database and an account

**account**

Before you start to use ApsaraDB RDS, you must create databases and accounts on an ApsaraDB RDS instance. This topic describes how to create a database and an account on an ApsaraDB RDS for PostgreSQL instance.

**Account types**

ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. The following table describes these types of accounts.

| Account type | Description |
|---|---|

| Privileged account | You can create and manage privileged accounts in the ApsaraDB RDS console or by calling API operations. You can create multiple privileged accounts for each RDS instance. The privileged accounts of an RDS instance have the permissions to manage all standard accounts and databases that are created on the instance. A privileged account allows you to manage permissions at fine-grained levels based on your business requirements. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect any standard account of the RDS instance on which the privileged account is created. |
|---|---|
| Standard account | You can create and manage standard accounts in the ApsaraDB RDS console, by using the ApsaraDB RDS API, or by executing SQL statements. You can create multiple standard accounts for each RDS instance. You must grant the permissions on specified databases to standard accounts. You cannot use a standard account to create, manage, or log off other accounts from the instance on which the standard account is created. |

**Precautions**

You can create multiple privileged accounts and standard accounts in the ApsaraDB RDS console. You can also create and manage standard accounts by using SQL statements.

> **Note:** Privileged accounts created on an instance that uses local SSDs cannot be deleted.

Before you can migrate data from an on-premises database to an RDS instance, you must create a database and an account on the RDS instance. Make sure that the created database has the same properties as the on-premises database. In addition, make sure that the created account has the same permissions on the created database as the account that is authorized to manage the on-premises database. We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple databases and accounts and grant each account only the permissions to access specified databases. This way, you can implement fine-grained access control. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for accounts and change the passwords on a regular basis.

**Create a privileged account or a standard account**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. On the Accounts page, click **Create Account** and configure the following parameters.

| Parameter | Description |
|---|---|

| Database Account | The username of the account must be 2 to 16 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a letter and end with a letter or a digit. It cannot be the same as the username of an existing account. It cannot start with pg. It cannot contain SQL keywords. For more information, see SQL Keywords. |
|---|---|
| Account Type | ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. A privileged account has all operation permissions on all databases. Standard accounts have all operation permissions only on their authorized databases. Note The permitted operations include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER. |
| Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ |
| Re-enter Password | Enter the password of the account again. |
| Note | This parameter is available only if the instance uses standard SSDs. It is an optional parameter. You can enter description to make the account easier to identify. The description can be up to 256 characters in length. |

6. Click **OK**.

**Create a database and a standard account**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to Database** in the upper-right corner of the page.
5. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
the **Database Type**, **Instance Region**, and **Connection string address** parameters. If the information is correct, specify the **Database Account** and **Database password** parameters, as shown in the following figure.

| Parameter | Description |
|---|---|
| Database Type | The engine of the database. By default, the engine of the database to be connected is selected. |
| Instance Region | The region where the instance is deployed. By default, the region of the current instance is selected. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The username of the database account. |
| Database password | The password of the database account. |

6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

> **Note:** If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.

7. The **SQLConsole** page appears after you log on to the instance. Execute a statement in the
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

8. Click **Execute**.
9. In the SQL window, execute a statement in the following format to create a standard
account:

```
CREATE USER name [ [ WITH ] option [ ... ] ] where option can be:
   SUPERUSER | NOSUPERUSER
 | CREATEDB | NOCREATEDB
 | CREATEROLE | NOCREATEROLE
 | CREATEUSER | NOCREATEUSER
 | INHERIT | NOINHERIT
 | LOGIN | NOLOGIN
 | REPLICATION | NOREPLICATION
 | CONNECTION LIMIT connlimit
 | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
 | VALID UNTIL 'timestamp'
 | IN ROLE role_name [, ...]
 | IN GROUP role_name [, ...]
 | ROLE role_name [, ...]
 | ADMIN role_name [, ...]
 | USER role_name [, ...]
 | SYSID uid
```

For example, if you want to create a user account named test2 whose password is 123456, execute the following statement:

```
create user test2 password '123456';
```

0. Click **Execute**.

### 6.5 Connect to an ApsaraDB RDS for PostgreSQL instance

**for PostgreSQL instance**

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an RDS instance. DMS is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational databases, such as MySQL, SQL Server, PostgreSQL, MongoDB, and Redis databases. DMS can also be used to manage NoSQL databases and Linux-based database servers. You can also use a database client to connect to an RDS instance. ApsaraDB RDS is fully compatible with open source database engines. Therefore, you can connect these two types of databases in the same way. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Log on to an ApsaraDB for RDS instance by using DMS.

**Use the pgAdmin 4 client to connect to an instance**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.

> **Note:** For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows). In this example, pgAdmin 4 v6.15 is downloaded.

3. Right-click **Servers** and choose **Register > Server**, as shown in the following figure.
4. On the **General** tab of the **Register - Server** dialog box, enter the name of the server, as
shown in the following figure.
5. Click the **Connection** tab and enter the information of the instance, as shown in the
following figure.

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the RDS instance. For more information about how to view the internal endpoint of an RDS instance, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |
| Username | The name of the privileged account on the RDS instance. For more information about how to obtain a privileged account, see Create a database and an account. |
| Password | The password of the privileged account of the ApsaraDB RDS instance. |

6. Click **Save**.
7. If the connection information is correct, choose **Servers > <Server Name> >**
**Databases > postgres**. If the following page appears, the connection is established.

> **Important:** The postgres database is the default system database. Do not perform operations on the postgres database.

## 7 Instances

### 7.1 Create an instance

This topic describes how to create one or more ApsaraDB RDS for PostgreSQL instances in the ApsaraDB RDS console.

**Procedure**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, click **Create Instance** in the upper-right corner.
3. Configure the following parameters.

| Section | Paramete r | Description |
|---|---|---|
| Basic Settings | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
| Region | Region | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|   | Zone of Primary Node | The zone where the primary instance is deployed. |
|   | Deployme nt Method | Specifies whether to deploy the primary and secondary instances in separate zones. ApsaraDB RDS supports Multi-zone Deployment and Single-zone Deployment. If you select Multi-zone Deployment, you must configure Zone of Secondary Node. |
|   | Zone of Secondar y Node | The zone where the secondary instance is deployed. This parameter is available only when Deployment Method is set to Multi-zone Deployment. Note If you select the same zone for both the primary and secondary instances, the deployment is equivalent to single-zone deployment. |
|   | Quantity | The number of ApsaraDB RDS instances that you want to create. Default value: 1. |
|   | Instance Name | The name of the instance. The name must be 2 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, and the following special characters: - : _ The name cannot start with http:// or https://. |

|   | Connectio n Type | The connection type of the instance. ApsaraDB RDS instances support the following connection types: Internet: ApsaraDB RDS instances of this connection type can be connected over the Internet. Internal Network: ApsaraDB RDS instances of this connection type can be connected over an internal network. Note The value of this parameter cannot be changed after the instance is created. Proceed with caution. |
|---|---|---|
| Specificat ions |   |   |
|   | Database Engine | The database engine of the instance. Select PostgreSQL. |
|   | Engine Version | The version of the database engine. Valid values: 9.4 10.0 11.0 12.0 |
|   | Edition | The edition of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Type | The storage type of the instance. Local and standard SSDs are supported. Note Instances that run PostgreSQL 9.4 support only local SSDs. |
|   | Encrypte d | Specifies whether to encrypt the standard SSD. This parameter is available only when Storage Type is set to Standard SSD. If you select Encrypted, you must specify the Encryption Key parameter. If you do not have a key, you must first create one in Key Management Service (KMS). For more information, see Create a CMK in Key Management Service User Guide. |
|   | Encryptio n Key | The key that is used to encrypt the standard SSD. This parameter is available only when you select Encrypted. |
|   | Instance Type | The instance type of the instance. Memory size determines the maximum number of connections and the input/output operations per second (IOPS). The actual values are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The storage capacity of the instance, which includes the space to store data, system files, binlog files, and transaction files. Valid values: 20 to 600. Unit: GB. The value must be in 1 GB increments. |

| Network | Network Type | The network type of the instance. ApsaraDB RDS instances support the following network types: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Note If you configure multi-zone deployment, you must create vSwitches for the zones of primary and secondary instances in the specified VPC. If you select VPC, you must specify a VPC and a vSwitch. |
|---|---|---|
|   | IP Address Whitelist | The IP addresses that are allowed to connect to the instance. |

4. Click **Submit**.

### 7.2 View basic information of an instance

**instance**

This topic describes how to view the details of an ApsaraDB RDS instance, such as its basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. Use one of the following methods to go to the **Basic Information** page of an instance:
On the **Instances** page, click the ID of the instance to go to the **Basic Information** page. On the **Instances** page, find the instance and click **Manage** in the **Actions** column to go to the **Basic Information** page.

### 7.3 Restart an instance

This topic describes how to manually restart an ApsaraDB RDS instance. This applies if the number of connections exceeds the specified threshold or if an instance has performance issues.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the upper-right corner of the page, click **Restart Instance**.

> **Note:** When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.

5. In the message that appears, click **Confirm**.

### 7.4 Change the specifications of an instance

**an instance**

This topic describes how to change the specifications of an ApsaraDB RDS instance. You can upgrade or downgrade an ApsaraDB RDS instance to meet your business needs.

**Prerequisites**

The instance is in the **Running** state and is not in the backing up or restoring state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Configure Information** section of the **Basic Information** page, click **Change**
**Specifications**.
5. On the **Change Specifications** page, set **Edition**, **Instance Type**, and **Storage**
**Capacity**.
6. Click **Submit**.

### 7.5 Set a maintenance window

This topic describes how to set a maintenance window for an ApsaraDB RDS instance.

**Background information**

To ensure the stability of ApsaraDB RDS instances, the backend system performs maintenance on the instances at irregular intervals. The default maintenance window is from 02:00 to 06:00. You can set the maintenance window to the off-peak period of your business to avoid impact on business.

**Precautions**

To ensure stability of the maintenance process, the instance enters the **Maintaining**
**Instance** state before the maintenance window. When the instance is in this state, access
to data in the database and query operations such as performance monitoring are not affected. However, except for account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. You may encounter a network interruption during the maintenance window. Make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Configuration Information** section, click **Configure** to the right of **Maintenance**
**Window**.
5. Select a maintenance window and click **OK**.

> **Note:** The time displayed on the page is in UTC+8.

### 7.6 Configure primary/secondary switchover

**switchover**

ApsaraDB RDS provides the primary/secondary switchover feature to ensure the high availability of databases. The primary/secondary switchover is performed when the primary instance becomes unavailable. You can also manually switch your business to the secondary instance. This topic describes how to manually switch over services between a primary instance and its secondary instance.

**Background information**

Data is synchronized in real time between the primary and secondary instances. You can access only the primary instance. The secondary instance serves only as a backup instance and does not allow external access. After the switchover, the original primary instance becomes the secondary instance.

> **Note:** Network interruptions may occur during a switchover. Make sure that your applications are configured with automatic reconnection policies.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Service Availability**.
5. In the **Availability Information** section of the page that appears, click **Switch**
**Primary/Secondary Instance**.
6. In the dialog box that appears, specify the time when the switching is performed and click
**OK**.

> **Note:** During the switchover, operations such as managing databases and accounts and changing network types cannot be performed. Therefore, we recommend that you select Switch Within Maintenance Window.

For more information about how to set a maintenance window, see Set a maintenance window.

### 7.7 Release an instance

This topic describes how to manually release an instance.

**Precautions**

Only instances in the Running state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance. When you release a primary instance, all of its read-only instances are also released.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. Find the instance that you want to release and choose **More > Release Instance** in the
Actions column.
3. In the message that appears, click **OK**.

### 7.8 Configure instance parameters

**parameters**

This topic describes how to view and modify the values of instance parameters and query parameter modification history in the console.

**Precautions**

To ensure instance stability, not all parameters can be modified in the ApsaraDB RDS console. When you modify parameters on the **Editable Parameters** tab, you can refer to the **Value**
**Range** column corresponding to each parameter.
Some parameters require an instance restart for the changes to take effect. You can refer to the **Force Restart** column on the **Editable Parameters** tab. We recommend that you configure parameters during off-peak hours and make sure that your application is configured to automatically reconnect to your RDS instance.

**Configure parameters**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Parameters**.
5. You can perform the following operations:
Modify multiple parameters at a time. a. Export the parameter settings of the ApsaraDB RDS instance to your computer. On the Editable Parameters tab, click **Export Parameters**. The parameter settings of the instance are exported as a TXT file to your computer. b. Modify the parameter values in the TXT file. c. On the Editable Parameters tab, click **Import Parameters**. In the dialog box that appears, paste the modified parameters into the editor. d. Click **OK**. e. In the upper part of the page, click **Apply Changes**.

> **Note:** If the modified parameters require an instance restart for the changes to take effect, ApsaraDB RDS prompts you to restart the RDS instance. We recommend that you restart the RDS instance during off-peak hours and make sure that your application is configured to automatically reconnect to the RDS instance.
> Before the new parameter values take effect, you can click **Cancel Changes** to revoke the changes.

Modify the value of a single parameter. a. On the **Editable Parameters** tab, find the parameter that you want to modify, and click the icon in the **Running Parameter Value** column. b. Enter a new value based on the value range that is displayed. c. Click **OK**. d. In the upper part of the page, click **Apply Changes**.

> **Note:** If the modified parameters require an instance restart for the changes to take effect, ApsaraDB RDS prompts you to restart the RDS instance. We recommend that you restart the RDS instance during off-peak hours and make sure that your application is configured to automatically reconnect to the RDS instance.
> Before the new parameter values take effect, you can click **Cancel Changes** to revoke the changes.

**View the parameter modification history**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane of the page that appears, click **Parameters**.
5. On the Parameters page, click the **Edit History** tab.
6. Select a time range and click **Search**.

### 7.9 Read-only instances

#### 7.9.1 Overview of read-only ApsaraDB RDS for PostgreSQL instances

**for PostgreSQL instances**

This topic provides an overview of read-only ApsaraDB RDS for PostgreSQL instances. If your database system receives a small number of write requests but a large number of read requests, a single primary RDS instance may be overwhelmed by read requests and have its workloads affected. To offload read requests from the primary RDS instance, you can create one or more read-only RDS instances. Read-only RDS instances help increase the read capability of your database system and the throughput of your application.

**Overview**

When a read-only RDS instance is being created, ApsaraDB RDS replicates data from the secondary RDS instance to the read-only RDS instance. After the read-only RDS instance is created, it has the same data as the primary RDS instance. In addition, after the data on the primary RDS instance is updated, ApsaraDB RDS immediately synchronizes the updates to all read-only RDS instances that are attached to the primary RDS instance.

> **Note:** Each read-only RDS instance runs in a single-node architecture. In this architecture, no secondary RDS instance is provided as a standby for a read-only RDS instance.

The following figure shows the topology of the primary RDS instance and its read-only RDS instances.

**Features**

Read-only RDS instances reside within the same region as the primary RDS instance, but can reside in different zones. The specifications and storage space of read-only RDS instances cannot be lower than those of the primary RDS instance. The network types of read-only RDS instances can differ from the network type of the primary RDS instance. The databases and accounts on read-only RDS instances are synchronized from the primary RDS instance. You do not need to manage databases or accounts on read-only RDS instances. When you create a read-only RDS instance, ApsaraDB RDS replicates the IP address whitelists of the primary RDS instance to the read-only RDS instance. However, the IP address whitelists of the read-only RDS instance are independent of the IP address whitelists of the primary RDS instance. For more information about how to modify the IP address whitelists of a read-only RDS instance, see Configure an IP address whitelist. Read-only RDS instances support monitoring and alerting. You can monitor metrics such as disk usage, IOPS, number of connections, and CPU utilization.

**Limits**

A maximum of five read-only RDS instances can be created on a primary RDS instance. You cannot configure backup policies or manually create backups for read-only RDS instances. These operations are performed on primary RDS instances. You cannot migrate data to read-only RDS instances. You cannot create or delete databases on read-only RDS instances. You cannot create or delete accounts, grant permissions to accounts, or change the passwords of accounts on read-only RDS instances.

**FAQ**

Q: After I create accounts on my primary RDS instance, can I manage the accounts on the read-only RDS instances of my primary RDS instance? No, you cannot manage the accounts on the read-only RDS instances. Although the accounts created on your primary RDS instance are synchronized to the read-only RDS instances, the accounts have only the read permissions on the read-only RDS instances.

#### 7.9.2 Create a read-only ApsaraDB RDS for PostgreSQL instance

**PostgreSQL instance**

This topic describes how to create a read-only RDS instance for a primary ApsaraDB RDS for PostgreSQL instance, which can improve the read capability of your database system and the throughput of your application. Each read-only RDS instance is a replica of the primary RDS instance. Data updates on the primary RDS instance are automatically synchronized to all read-only RDS instances that are attached to the primary RDS instance.

**Prerequisites**

The primary instance runs PostgreSQL 10.0 or later.

**Usage notes**

You can create read-only RDS instances for the primary RDS instance. You cannot convert existing RDS instances to read-only RDS instances. When you create a read-only RDS instance, ApsaraDB RDS replicates data from the secondary RDS instance to the read-only RDS instance. This prevents interruptions to your workloads that are run on the primary RDS instance. A read-only RDS instance does not inherit the parameter settings of the primary RDS instance. Default parameter settings are generated for the read-only RDS instance. You can modify the default parameter settings in the ApsaraDB RDS console. The instance type and storage capacity of a read-only instance cannot be lower than that of the primary instance. You can create up to five read-only instances for a primary instance.

**Create a read-only instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Instance Distribution** section of the Basic Information page, click **Add** to the right
of **Read-only Instance**.
5. On the Create Read-only Instance page, configure parameters and click **Submit**. The
following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|

| Area | Region | The region in which you want to create the read- only instance. |
|---|---|---|
| Specifications | Database Engine Type | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Engine Version | The version of the database engine, which is the same as that of the primary instance and cannot be changed. |
|   | Instance Edition | The edition of the read-only instance. The edition cannot be changed. |
|   | Specification | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type as the primary instance for the read-only instance. |
|   | Storage | The storage capacity of the read-only instance. Valid values: 20 to 6000. Unit: GB. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same storage capacity as the primary instance for the read-only instance. |
| Network Type | Network Type | The network type of the read-only instance. This must be the same as that of the primary instance and cannot be changed. |
|   | VPC | The VPC in which you want to create the read- only instance. This parameter is required when Network Type is set to VPC. |
|   | vSwitch | The vSwitch in the VPC. This parameter is required when Network Type is set to VPC. |

#### 7.9.3 View a read-only ApsaraDB RDS for PostgreSQL instance

**PostgreSQL instance**

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View instance details of a read-only instance by using its ID**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to view.
3. Click the ID of the instance or click **Manage** in the corresponding Actions column to go to
the Basic Information page.

**View details of a read-only instance by using the primary**

**instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. On the **Basic Information** page, move the pointer over the number below **Read-only**
**Instance** in the **Distributed by Instance Role** section. The ID of the read-only instance is
displayed.
5. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

**View the latency of data replication to a read-only RDS**

**instance**

A read-only RDS instance may synchronize data from the primary RDS instance at a specific latency. You can go to the Basic Information page of a read-only RDS instance to view the latency of data replication to the instance.

#### 7.9.4 Manage a read-only ApsaraDB RDS for PostgreSQL instance

**PostgreSQL instance**

This topic describes how to change specifications of a read-only RDS instance, release a readonly RDS instance, and view monitoring and alerting information of a read-only RDS instance.

**Change specifications of a read-only RDS instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click the ID of the instance or click **Manage** in the Actions column to go to the Basic
Information page.
4. In the **Configuration Information** section of the **Basic Information** page, click **Change**
**Specifications**.
5. On the **Change Specifications** page, configure the parameters described in the following
table and click **Submit**.

| Parameter | Description |
|---|---|
| Edition | The edition of the read-only instance. It cannot be modified. |
| Storage Type | The storage type is the same as that before the specification change and cannot be changed. |
| Specification | The instance type of the read-only instance. For more information, see Instance types in ApsaraDB RDS Production Introduction. |
| Storage Capacity | The maximum amount of storage capacity that is provisioned to store data files, system files, binary log files, and transaction files in the read-only RDS instance. |

**Release a read-only RDS instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click the ID of the instance or click **Manage** in the Actions column to go to the Basic
Information page.
4. In the **Status** section of the **Basic Information** page, click **Release Instance**. In the
message that appears, click **Confirm**.

**View monitoring and alerting information of a read-only RDS**

**instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click the ID of the instance or click **Manage** in the Actions column to go to the Basic
Information page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.

> **Note:** The monitoring and alerting feature of read-only RDS instances can be used in the same manner as that of the primary instance. For more information, see View monitored resources.

## 8 Database connection

### 8.1 Connect to an ApsaraDB RDS for PostgreSQL instance

**for PostgreSQL instance**

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an RDS instance. DMS is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational databases, such as MySQL, SQL Server, PostgreSQL, MongoDB, and Redis databases. DMS can also be used to manage NoSQL databases and Linux-based database servers. You can also use a database client to connect to an RDS instance. ApsaraDB RDS is fully compatible with open source database engines. Therefore, you can connect these two types of databases in the same way. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Log on to an ApsaraDB for RDS instance by using DMS.

**Use the pgAdmin 4 client to connect to an instance**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.

> **Note:** For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows). In this example, pgAdmin 4 v6.15 is downloaded.

3. Right-click **Servers** and choose **Register > Server**, as shown in the following figure.
4. On the **General** tab of the **Register - Server** dialog box, enter the name of the server, as
shown in the following figure.
5. Click the **Connection** tab and enter the information of the instance, as shown in the
following figure.

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the RDS instance. For more information about how to view the internal endpoint of an RDS instance, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |
| Username | The name of the privileged account on the RDS instance. For more information about how to obtain a privileged account, see Create a database and an account. |
| Password | The password of the privileged account of the ApsaraDB RDS instance. |

6. Click **Save**.
7. If the connection information is correct, choose **Servers > <Server Name> >**
**Databases > postgres**. If the following page appears, the connection is established.

> **Important:** The postgres database is the default system database. Do not perform operations on the postgres database.

### 8.2 Use DMS to log on to an ApsaraDB RDS instance

**ApsaraDB RDS instance**

This topic describes how to use Data Management (DMS) to log on to an ApsaraDB RDS instance.

**Prerequisites**

The IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to DB** in the upper-right corner of the page.
5. In the **Login instance** dialog box of the **DMS** console, check values of **Database type**,
**Instance Area**, and **Connection string address**. If the information is correct, enter
**Database account** and **Database password**, as shown in the following figure.

| Parameter | Description |
|---|---|
| Database type | The engine of the database. By default, the engine of the database to be connected is displayed. |
| Instance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database account | The account of the database to be connected. |
| Database password | The password of the account used to connect to the database. |

6. Click **Login**.

> **Note:** If you want the browser to remember the password, select **Remember** **password** before you click **Login**.

### 8.3 View and modify the internal endpoint and port number

**endpoint and port number**

You must use the internal endpoint and port number to access an ApsaraDB RDS instance. This topic describes how to view and modify the internal endpoint and port number of an ApsaraDB RDS instance in the ApsaraDB RDS console.

**View the internal endpoint and port number**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Basic Information** section, view the internal endpoint and port number of the
instance.

**Modify the internal endpoint and port number**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the right side of the page, click **Change Endpoint**.
6. In the dialog box that appears, set **Connection Type** to **Internal Endpoint**.
7. Modify the endpoint prefix and port number and click **OK**.

**FAQ**

Q: Do I need to modify the endpoint or port number in my application after I modify the endpoint or port number of an instance? A: Yes, you must modify the endpoint or port number in the application after you modify them. Otherwise, the application cannot connect to databases of the instance. Q: Does the modification of the endpoint take effect immediately? Do I need to restart the instance? A: No, you do not need to restart the instance. The modification takes effect immediately.

## 9 Accounts

### 9.1 Create an account

Database accounts are required for using ApsaraDB RDS instances. This topic describes how to create an account on an ApsaraDB RDS for PostgreSQL instance.

**Account types**

ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. The following table describes these types of accounts.

| Account type | Description |
|---|---|
| Privileged account | You can create and manage privileged accounts in the ApsaraDB RDS console or by calling an API operation. You can create multiple privileged accounts for each RDS instance. The privileged accounts of an RDS instance have the permissions to manage all standard accounts and databases that are created on the instance. A privileged account allows you to manage permissions at fine-grained levels based on your business requirements. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect all standard accounts of the RDS instance on which the privileged account is created. |
| Standard account | You can create and manage standard accounts in the ApsaraDB RDS console, by using the ApsaraDB RDS API, or by executing SQL statements. You can create multiple standard accounts for each RDS instance. You must grant the permissions on specified databases to standard accounts. You cannot use a standard account to create, manage, or log off other accounts from the instance on which the standard account is created. |

**Usage notes**

You can create multiple privileged accounts and standard accounts in the ApsaraDB RDS console. You can also create and manage standard accounts by using SQL statements.

> **Note:** Privileged accounts created on an instance that uses local SSDs cannot be deleted.

Before you migrate data from an on-premises database to an RDS instance, you need to create a database and an account on the RDS instance. Make sure that the created database has the same properties as the on-premises database. In addition, make sure that the created account has the same permissions on the created database as the account that is authorized to manage the on-premises database. We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple accounts and grant each account only the permissions to access the data of specified databases. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for accounts and change the passwords on a regular basis.

**Create a privileged or standard account**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. On the Accounts page, click **Create Account** and configure the following parameters.

| Parameter | Description |
|---|---|
| Database Account | The username of the account must be 2 to 16 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a lowercase letter and end with a lowercase letter or a digit. It cannot be the same as the username of an existing account. The username of the account cannot start with pg. The username of the account cannot contain SQL keywords. For more information, see SQL keywords. |
| Account Type | ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. A privileged account has all operation permissions on all databases. Standard accounts have all operation permissions only on their authorized databases. Note The operation permissions include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER. |
| Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ |
| Confirm Password | Enter the password of the account again. |
| Description | This parameter is available only if the instance uses standard SSDs. It is an optional parameter. You can enter description to make the account easier to identify. The description can be up to 256 characters in length. |

6. Click **OK**.

### 9.2 Reset the password of a database account

**database account**

This topic describes how to use the ApsaraDB RDS console to reset the password of your database account if you forget the password.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Reset Password**.
6. In the dialog box that appears, enter a new password and click **OK**.

> **Note:** The password must meet the following requirements:
> The password must be 8 to 32 characters in length.
> It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
> Supported special characters: ! @ # $ % ^ & * ( ) _ + - =

### 9.3 Lock or delete an account from an instance

**from an instance**

This topic describes how to lock or delete an account from an ApsaraDB RDS for PostgreSQL instance that uses standard SSDs.

**Prerequisites**

Your RDS instance uses standard SSDs.

**Lock an account of an instance**

> **Note:** When an account is locked, you cannot use the account to log on to the RDS instance.

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Lock**.

> **Note:** Wait a few minutes. When the **Status** column displays **Locking**, the account is locked. If you want to use the account again, click **Unlock** in the **Actions** column.

**Delete an account from an instance**

> **Note:** If the account that you want to delete is granted permissions on databases, tables, or other objects, the "Some objects depend on account" message is displayed when you attempt to delete the account. You can delete the account only after you remove the permissions of the account.

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Delete**.
6. In the message that appears, click **OK**.

### 9.4 Delete an account

You can delete a database account in the ApsaraDB RDS console.

**Prerequisites**

You can use the console to delete privileged and standard accounts that are no longer used.

**Procedure**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to delete and click **Delete** in the Actions column.
5. In the message that appears, click **Confirm**.

> **Note:** Accounts in the **Processing** state cannot be deleted.

## 10 Databases

### 10.1 Create a database

Before you start to use ApsaraDB RDS, you must create a database on an ApsaraDB RDS instance. This topic describes how to create a database on an ApsaraDB RDS for PostgreSQL instance.

**Prerequisites**

An ApsaraDB RDS for PostgreSQL instance is created. For more information, see Create an instance. An account is created. For more information, see Create an account.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to DB** in the upper-right corner of the page.
5. In the **Login instance** dialog box of the **DMS** console, check values of **Database type**,
**Instance Area**, and **Connection string address**. If the information is correct, enter
**Database account** and **Database password**, as shown in the following figure.

| Parameter | Description |
|---|---|

| Database type | The engine of the database. By default, the engine of the database to be connected is displayed. |
|---|---|
| Instance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database account | The account of the database to be connected. |
| Database password | The password of the account used to connect to the database. |

6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

> **Note:** If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.

7. The **SQLConsole** page appears after you log on to the instance. Execute a statement in the
following format to create a database:

```
CREATE DATABASE name;
```

For example, if you want to create a database named test, execute the following statement:

```
create database test;
```

8. Click **execute**.

### 10.2 Delete a database

This topic describes how to delete a database in the ApsaraDB RDS for PostgreSQL console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to DB** in the upper-right corner of the page.
5. In the **Login instance** dialog box of the **DMS** console, check values of **Database type**,
**Instance Area**, and **Connection string address**. If the information is correct, enter
**Database account** and **Database password**, as shown in the following figure.

| Parameter | Description |
|---|---|
| Database type | The engine of the database. By default, the engine of the database to be connected is displayed. |
| Instance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database account | The account of the database to be connected. |
| Database password | The password of the account used to connect to the database. |

6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

> **Note:** If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.

7. The **SQLConsole** page appears after you log on to the instance. Execute the following
statement to delete a database:

```
drop database <database name>;
```

For example, if you want to delete a database named test2, execute the following statement:

```
drop database test2;
```

8. Click **execute**.
witches

## 11 Networks, VPCs, and vSwitches

**vSwitches**

### 11.1 Change the VPC and vSwitch of an instance

**of an instance**

This topic describes how to change the virtual private cloud (VPC) and vSwitch for an ApsaraDB RDS for PostgreSQL instance.

**Prerequisites**

The ApsaraDB RDS for PostgreSQL instance is deployed in a VPC.

> **Note:** The ApsaraDB RDS for PostgreSQL 10.0 instances that use local SSDs do not support this feature.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch vSwitch**.
6. In the dialog box that appears, select a destination vSwitch and click **OK**.

> **Note:** If you want to create a vSwitch, click **go to the VPC console**.

7. In the message that appears, click **Switch**.

> **Note:** When you switch an instance to a different vSwitch, a transient connection that lasts approximately 30 seconds occurs. Make sure that your application is configured to automatically reconnect to your instance.
> If data is cached on your client, you can read data but cannot write data. After the vSwitch of your instance is changed, we recommend that you immediately clear the cache on the client.

### 11.2 Change the network type of an ApsaraDB RDS for PostgreSQL instance

**an ApsaraDB RDS for PostgreSQL**

**instance**

This topic describes how to change the network type of an ApsaraDB RDS for PostgreSQL instance between classic network and Virtual Private Cloud (VPC). witches

**Prerequisites**

The ApsaraDB RDS instance uses local SSDs.

**Background information**

Classic network: ApsaraDB RDS instances in the classic network are not isolated. You can block unauthorized access only by configuring IP address whitelists on these instances. VPC: Each VPC is an isolated network. We recommend that you use the VPC network type because it provides a higher security level. You can configure route tables, CIDR blocks, and gateways within a VPC. To smoothly migrate applications to the cloud, you can use the leased line or VPN method to create a virtual data center that consists of your self-managed data center and a VPC.

**Change the network type from VPC to classic network**

Precautions The ApsaraDB RDS instance must be in a VPC. After you change the network type from VPC to classic network, the internal endpoint of the ApsaraDB RDS instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, you cannot connect Elastic Compute Service (ECS) instances deployed in VPCs to the ApsaraDB RDS instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. You may encounter a network interruption of about 30 seconds during the change process. To avoid business interruptions, we recommend that you change the network type during off-peak hours or make sure that your application is configured to automatically reconnect to the instance.
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to Classic**
**Network**.
6. In the message that appears, click **OK**.

> **Note:** After the network type is changed to classic network, only ECS instances within the classic network can connect to the ApsaraDB RDS instance by using the internal endpoint. You must configure the internal endpoint for the ECS instances.

7. Configure an IP address whitelist to allow ECS instances within the classic network to
connect to the ApsaraDB RDS instance by using the internal endpoint. witches

> **Note:** If the network isolation mode of the ApsaraDB RDS instance is standard whitelist, add the internal IP addresses of the ECS instances to a whitelist of your ApsaraDB RDS instance.
> If the network isolation mode of the ApsaraDB RDS instance is enhanced whitelist, add the internal IP addresses of the ECS instances to a whitelist of the classic network type. If no whitelists of the classic network type are available, create a whitelist. For more information about the enhanced whitelist mode, see Switch to the enhanced whitelist mode.

**Change the network type from classic network to VPC**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to VPC**.
6. In the Switch to VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. witches

> **Note:** Select a VPC. We recommend that you select the VPC where your ECS instances are deployed. Otherwise, the ECS instances cannot communicate with the ApsaraDB RDS instance over the internal network.
> Select a vSwitch. If no vSwitches are available in the selected VPC, create one in the same zone where the ApsaraDB RDS instance is deployed. For more information, see Create a vSwitch in **Virtual Private Cloud User Guide**.
> Clear or select the **Reserve Original Classic Network Endpoint** check box.
> **Clear the Reserve Original Classic Network Endpoint check box**
> The classic network endpoint is not retained and changes to a VPC endpoint.
> When you change the network type from classic network to VPC, a network interruption of 30 seconds occurs. In this case, ECS instances located in the classic network are disconnected from your ApsaraDB RDS instance.
> **Select the Reserve Original Classic Network Endpoint check box**
> The classic network endpoint is retained, and a new VPC endpoint is generated. In this case, your ApsaraDB RDS instance runs in hybrid access mode. Both ECS instances located in the classic network and ECS instances located in the selected VPC can access your ApsaraDB RDS instance over an internal network. You must set **Expiration Time** **(Important)** to **14 Days Later**, **30 Days Later**, **60 Days Later**, or **120** **Days Later** for the classic network. You can also modify the expiration date after the network type is changed. For more information, see Configure hybrid access from both the classic network and VPCs.
> When you change the network type from classic network to VPC, no network interruptions occur. ECS instances located in the classic network are still connected with your ApsaraDB RDS instance until the classic network endpoint expires.
> Before the classic network endpoint expires, you must add the new VPC endpoint to your applications that run on the ECS instances located in the selected VPC. This allows ApsaraDB RDS to migrate your workloads to the selected VPC without network interruptions. Seven days before the classic network endpoint expires, the system sends a text message to the phone number bound to your Apsara Stack tenant account every day.

For more information, see Hybrid access from both the classic network and VPCs.
7. Add the internal IP addresses of ECS instances located in the selected VPC to an IP address
whitelist of the VPC network type. This allows the ECS instances to connect to your ApsaraDB RDS instance over an internal network. If no IP address whitelists of the VPC network type are available, create one.

> **Note:** If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires.
> If you do not retain the classic network endpoint, connections between ECS instances in the classic network and the ApsaraDB RDS instance over the internal network are interrupted. You must add the VPC endpoint to ECS instances in the VPC immediately after the network type is changed.

witches

### 11.3 Configure hybrid access from both the classic network and VPCs

**both the classic network and VPCs**

This topic describes how to use the hybrid access solution of ApsaraDB RDS to change the network type of an instance from classic network to Virtual Private Cloud (VPC) without network interruptions.

**Prerequisites**

The ApsaraDB RDS instance uses local SSDs. The ApsaraDB RDS instance is deployed in the classic network. Available VPCs and vSwitches exist in the zone where the ApsaraDB RDS instance is deployed.

**Background information**

In the past, when you change the network type of an ApsaraDB RDS instance from classic network to VPC, the internal endpoint of the ApsaraDB RDS instance would remain the same but the IP address bound to the endpoint would change to the corresponding IP address in the VPC. This change would cause a 30-second network interruption, and ECS instances within the classic network would not be able to access the ApsaraDB RDS instance by using the internal endpoint within this period. To smoothly change the network type, ApsaraDB RDS provides the hybrid access solution. Hybrid access refers to the ability of an ApsaraDB RDS instance to be accessed by ECS instances in both the classic network and VPCs. During the hybrid access period, the ApsaraDB RDS instance reserves the original internal endpoint of the classic network and adds the internal endpoint of VPCs. This prevents network interruptions during the network type switchover. For better security and performance, we recommend that you use the internal endpoint of VPCs. Hybrid access is available for a limited period of time. The internal endpoint of the classic network is released when the hybrid access period expires. In that case, your applications cannot access the ApsaraDB RDS database by using the internal endpoint of the classic network. You must configure the internal endpoint of VPCs in all your applications during the hybrid access period. This ensures smooth network switchover and minimizes the impact on your services. For example, your company wants to use the hybrid access solution to change the network type from classic network to VPC. During the hybrid access period, some applications can access the database by using the internal endpoint of VPCs, and the other applications can access the database by using the original internal endpoint of the classic network. When all the applications access the database by using the internal endpoint of VPCs, the internal endpoint of the classic network can be released. The following figure illustrates the scenario. witches

**Limits**

During the hybrid access period, the instance has the following limits: The network type of your instance cannot be changed to classic network. Your instance cannot be migrated to another zone.

**Change the network type from classic network to VPC**

For more information, see Change the network type from classic network to VPC.

**Change the expiration time for the original internal endpoint of**

**the classic network**

During the period in which your instance can be accessed over the classic network or VPCs, you can specify the expiration time for the endpoint of the classic network. The setting takes effect immediately. For example, if the endpoint of the classic network is about to expire on August 18, 2017 and you change the expiration time to 14 days later on August 15, 2017, the endpoint of the classic network is released on August 29, 2017. To change the expiration time, perform the following steps:
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the **Instance Connection** tab, click **Change Expiration Time**.
6. In the **Change Expiration Time** dialog box, select an expiration time and click **OK**.

## 12 Monitoring

### 12.1 View monitored resources

ApsaraDB RDS provides a wide range of performance metrics. This topic describes how to view resource monitoring data in the ApsaraDB RDS console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.
5. On the **Monitoring** tab, select a time range to query the corresponding monitoring data.

> **Note:** You can click **Refresh** in the upper-right corner of the **Monitoring** tab to refresh the monitoring information.

## 13 Data security

### 13.1 Switch to the enhanced whitelist mode

**whitelist mode**

This topic describes how to switch an ApsaraDB RDS instance from the standard whitelist mode to the enhanced whitelist mode. The enhanced whitelist mode provides higher security than the standard whitelist mode.

**Prerequisites**

Major engine version: ApsaraDB RDS for PostgreSQL V10.0. Storage type: local SSDs.

**Network isolation modes**

ApsaraDB RDS instances support the following network isolation modes: Standard whitelist mode IP addresses from both the classic network and VPCs are added to the same IP address whitelist. The standard whitelist mode may incur security risks. Therefore, we recommend that you switch the network isolation mode to enhanced whitelist. Enhanced whitelist mode IP addresses from the classic network and VPCs are added to different IP address whitelists. When you create an enhanced IP address whitelist, you must specify its network type.

**Changes after you switch to the enhanced whitelist mode**

If your RDS instance resides in a VPC, an IP address whitelist of the VPC network type is automatically created. The new IP address whitelist contains all IP addresses that are replicated from the original IP address whitelists. If your RDS instance resides in the classic network, an IP address whitelist of the classic network type is automatically created. The new IP address whitelist contains all IP addresses and CIDR blocks that are replicated from the original IP address whitelists. If your ApsaraDB RDS instance runs in hybrid access mode, two identical IP address whitelists are created: an IP address whitelist of the VPC network type and an IP address whitelist of the classic network type. Both the new IP address whitelists contain all IP addresses that are replicated from the original IP address whitelists. For more information, see Hybrid access from both the classic network and VPCs.

> **Note:** After you switch to the enhanced whitelist mode, the IP addresses that come from Elastic Compute Service (ECS) security groups remain unchanged.

**Precautions**

You can switch from the standard whitelist mode to the enhanced whitelist mode, but not the other way around. In enhanced whitelist mode, an IP address whitelist of the classic network type can also be used to allow access over the Internet. If you want to access your RDS instance from a host over the Internet, you must add the public IP address of the host to an IP address whitelist of the classic network type.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Switch to Enhanced Whitelist (Recommended)** .
6. In the message that appears, click **Confirm**.

### 13.2 Configure an IP address whitelist

**whitelist**

This topic describes how to configure a whitelist for an ApsaraDB RDS instance. Only entities that are listed in a whitelist can access your ApsaraDB RDS instance.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure and do not interrupt the operations of your ApsaraDB RDS instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance.

> **Note:** The IP address whitelist labeled default contains only the default IP address 0.0.0.0/0, which allows all entities to access your ApsaraDB RDS instance.

Configure an ECS security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

> **Note:** You can also click **Create Whitelist** to create a whitelist.

6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks used to access the
instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your ApsaraDB RDS instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Alibaba Cloud account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### 13.3 Configure SSL encryption

This topic describes how to configure SSL encryption for an ApsaraDB RDS instance.

**Prerequisites**

The ApsaraDB RDS instance uses standard SSDs.

**Precautions**

After SSL encryption is enabled, SSL is used to encrypt all the data that is transmitted over an internal network or the Internet. SSL encryption protects the data in transit from being leaked. After SSL encryption is enabled, you must close the existing connection and establish a new one to bring SSL encryption into effect.

**Enable SSL encryption**

The Internet Engineering Task Force (IETF) upgraded SSL 3.0 to Transport Layer Security (TLS). However, the term "SSL encryption" is still used in the industry. In this topic, SSL encryption refers to TLS encryption.

> **Note:** ApsaraDB RDS supports TLS 1.0, TLS 1.1, and TLS 1.2.

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL Encryption** tab.
5. Click **Configure SSL**. In the dialog box that appears, select a protected endpoint, click OK,
and then wait for the system to enable SSL encryption.

**Connect to an ApsaraDB RDS for PostgreSQL instance over SSL**

Make sure that the CA certificate has been downloaded to your computer. For more information, see Enable SSL encryption.
1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.

> **Note:** To download the pgAdmin 4 client, visit pgAdmin 4 (Windows).

3. Right-click **Servers** and choose **Register > Server**.
4. On the **General** tab of the **Register - Server** dialog box, enter the name of the
connection.
5. Click the **Connection** tab and enter the information of the instance.

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the RDS instance. For more information about how to view the internal endpoint of an RDS instance, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |
| Username | The username of the account that is used to log on to the RDS instance. For information about how to create a database account, see Create a database and an account. |
| Password | The password of the account. |

6. On the **SSL** tab, set the **SSL mode** and **Root certificate** parameters, as shown in the
following figure.

| Parameter | Description |
|---|---|
| SSL mode | If SSL encryption is enabled for the RDS instance, the RDS instance allows SSL connections from the database client. You need to set the SSL mode parameter based on whether to enable SSL. If you want to enable SSL, select one of the following options: Require: The database client encrypts the SSL connections that are used to transmit data. However, the database client does not validate the RDS instance. Verify-CA: The database client encrypts the SSL connections that are used to transmit data and validates the RDS instance. Verify-Full: The database client encrypts the SSL connections that are used to transmit data, validates the RDS instance, and verifies that the CN or Domain Name System (DNS) specified in the server certificate is consistent with the endpoint that is configured during connection establishment. If you do not want to enable SSL, set the parameter to Disable. |
| Root certificate | If you set the SSL mode parameter to Verify-CA or Verify-Full, you must set the Root certificate parameter to the save path of the file that contains the server CA certificate. Note The CA certificate was generated in the Enable SSL encryption step in this topic. |

7. Click **Save**.
8. If the connection information is correct, choose **Servers > Server Name > Databases >**
**postgres**. If the following page appears, the connection is established.

> **Important:** The postgres database is the default system database. Do not perform operations on the postgres database.

**Disable SSL encryption**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL Encryption** tab.
5. Turn off **SSL Encryption**. In the message that appears, click OK and wait for the system to
disable SSL encryption.

> **Important:** This operation triggers a restart of your RDS instance. Proceed with caution.

### 13.4 Configure data encryption

This topic describes how to configure data encryption for an ApsaraDB RDS instance that uses standard SSDs. The disk encryption feature improves data security and eliminates the need to modify business or application configurations. ApsaraDB RDS automatically applies disk encryption to both the snapshots that are generated from the encrypted SSDs and the SSDs that are created from those snapshots.

**Prerequisites**

The ApsaraDB RDS instance uses standard SSDs.

**Configure disk encryption**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** **First logon**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forget password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log On**.
4. In the top navigation bar, choose **Products > Security > Key Management Service**.
5. Click **Create Key**.
6. Configure the following parameters.

| Section | Parameter | Description |
|---|---|---|
| Area | Organizatio n | The organization to which the key belongs. |
|   | Resource set | The resource set to which the key belongs. |
|   | Region | The region in which the key resides. |

| Basic configuratio n | Key type | Key Management Service (KMS) supports the following key types: Symmetric customer managed keys (CMKs): Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ |
|---|---|---|
|   | Key usage | ENCRYPT/DECRYPT: encrypts or decrypts data. |
|   | Protection Level | SOFTWARE: Use a software module to protect the CMK. |
|   | Alias | The identifier of the CMK. For more information, see Use aliases in KMS User Guide. |
|   | Description s | The description of the key. |
| Advanced configuratio n | Rotation cycle | Indicates whether automatic rotation is enabled. If you choose to enable automatic rotation, you must select a rotation cycle. For more information about rotation, see Key rotation in KMS User Guide. Valid values: 30 Days 90 Days 180 Days 365 Days Custom: You can specify a custom cycle that ranges from 7 days to 730 days. Note You can configure this parameter only if you set the Key type parameter to Aliyun AES 256. _ _ |
|   | Key Material Source | The source of the key material. You can configure this parameter only if you set the Key type parameter to Aliyun AES 256. _ _ Alibaba Cloud KMS: Use KMS to generate key material. External: Manually import external key material. Note If Rotation cycle is set to Open, the External option is unavailable. |

7. Click **Submit**.
8. Create an RDS instance. Select Disk Encryption when you create the instance. For more
information, see Create an instance.

### 13.5 Configure TDE

ApsaraDB RDS for PostgreSQL provides the Transparent Data Encryption (TDE) feature. This topic describes how to enable TDE for your ApsaraDB RDS for PostgreSQL instance. This topic also describes how to use TDE to encrypt and decrypt tables and indexes.

**Prerequisites**

**q**

The RDS instance meets the following requirements: The RDS instance runs PostgreSQL 10 or later. The RDS instance uses local disks. If read-only RDS instances are attached to your RDS instance, make sure the read-only RDS instances also meet the preceding requirements. Key Management Service (KMS) is activated.

**Usage notes**

When you enable TDE, your RDS instance restarts. As a result, a transient connection occurs. Proceed with caution. Before you enable TDE, we recommend that you make appropriate arrangements for your workloads based on your business requirements. After you enable TDE, you cannot disable TDE. After TDE is enabled, database performance may be affected in I/O bound workload scenarios. If TDE is enabled for the primary RDS instance, streaming replication between the primary RDS instance and its self-managed secondary instance is not supported. If KMS is overdue, the cloud disk of your RDS instance cannot be decrypted and become unavailable. Make sure that KMS runs as normal. If you use an existing custom key for TDE, take note of the following items: If you disable or delete the custom key, the RDS instance cannot run as expected. The affected operations include creating a snapshot, restoring data by using a snapshot, and rebuilding a secondary RDS instance. If you restart your RDS instance after you disable the custom key, your RDS instance becomes unavailable. You must use an Alibaba Cloud account or an account to which the AliyunSTSAssumeRoleAccess policy is attached.

> **Note:** For more information, see **What Is Key Management Service?**

**Enable TDE**

**Use an automatically generated key**

> **Note:** The key encryption key (KEK) used by this method is the service key that is provided by KMS.

1. Log on to the ApsaraDB RDS console.
2. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, turn on **TDE Status**.
5. In the dialog box that appears, select **Use Automatically Generated Key** and click **OK**.

**Use an existing custom key**

> **Note:** The KEK used by this method is the customer master key (CMK) that you upload to KMS.

1. Log on to the ApsaraDB RDS console.
2. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, turn on **TDE Status**.
5. In the dialog box that appears, select **Use Existing Custom Key** and click **OK**.

> **Note:** If you do not have a custom key, you can click **go to the KMS console** to create one. In the KMS console, you can create a key and import your own key material.

**Replace a key**

TDE is enabled.
1. Log on to the ApsaraDB RDS console.
2. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, click **Replace key** to the right of **TDE Status**.
5. In the dialog box that appears, select **Use Automatically Generated Key** or **Use**
**Existing Custom Key** and click **OK**.

> **Note:** If you do not have a custom key, you can click **go to the KMS console** to create a custom key and import your own key material.

**Use TDE to encrypt or decrypt a table or an index**

After TDE is enabled for your RDS instance, you must use TDE to encrypt or decrypt tables on the RDS instance.

> **Note:** Encryption and decryption may cause performance loss. We recommend that you select an appropriate encryption range to minimize performance loss.

Encrypt a table or an index. Encrypt a table.

```
-- Create an encrypted table. CREATETABLE <tablename> WITH (encryption=on); -- Set the encryption parameter to on for a table. ALTERTABLE <tablename> SET (encryption=on);
```

Encrypt an index.

```
-- Create an encrypted index. CREATE INDEX <indexname> ... WITH (encryption=on); -- Set the encryption parameter to on for an index. ALTERINDEX <indexname> SET (encryption=on);
```

> **Note:** The following types of indexes can be encrypted: B-tree, hash, SP-GiST, GIN, GiST, and BRIN.

Decrypt a table or an index.

> **Note:** The following ALTER statements trigger the rewriting of a table or an index, which is similar to the VACUUM FULL statement. We recommend that you execute the following statements during off-peak hours.

Decrypt an encrypted table.

```
ALTER TABLE <tablename> SET (encryption=off);
```

Decrypt an encrypted index.

```
ALTER INDEX <indexname> SET (encryption=off);
```

View the encryption status of a table or an index.

```
SELECT relname, reloptions FROM pg_class WHERE relname IN('<tablename>', '<indexname>');
```

## 14 Logs and audit

### 14.1 Configure SQL audit

This topic describes how to configure the SQL audit feature to audit SQL executions and check the details. SQL audit does not affect instance performance.

**Precautions**

SQL audit does not affect instance performance. SQL audit logs are retained for 30 days. Log files exported from SQL audit are retained for two days. The system deletes files that are retained for longer than two days. SQL audit is disabled by default. You must manually enable it. You cannot view logs that are generated before SQL audit is enabled.

**Enable SQL audit**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. Click the **SQL Audit** tab.
6. Click **Enable SQL Audit** or **Enable now**.
7. In the message that appears, click **Confirm**.

> **Note:** After SQL audit is enabled, you can query SQL information based on conditions such as the time, database, user, and keyword.

**Disable SQL audit**

You can disable SQL audit when it is no longer needed. To disable SQL audit, perform the following steps:

> **Important:** After SQL audit is disabled, all SQL audit logs are deleted. We recommend that you export and store audit logs to your computer before you disable SQL audit.

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. Click the **SQL Audit** tab. Click **Export File**.

> **Note:** If more than 1 million SQL audit logs meet the filter conditions you specify, only 1 million logs can be exported. SQL audit logs are exported at a speed of 900 entries per second. It takes about 20 minutes to export 1 million SQL audit logs.

6. Click **Files**. Find a file and click Download in the **Action** column to download the file to your
computer.
7. Click **Disable SQL Audit**.
8. In the message that appears, click **Confirm**.

### 14.2 Manage logs

You can view logs for errors, slow queries, and primary/secondary instance switching for ApsaraDB RDS for PostgreSQL instances in the ApsaraDB RDS console or by executing SQL statements. These logs help you troubleshoot errors. This topic describes how to manage logs in the console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Logs**.
5. On the **Logs** page, click the **Error Logs**, **Slow Query Logs**, or **Primary/Secondary**
**Switching Logs** tab, select a time range, and then click **Search**.

| Tab | Description |
|---|---|
| Error Logs | Records database running errors that occurred within the last month. |
| Slow Query Logs | Records SQL statements within the last month that took longer than one second to execute. Duplicated SQL statements are removed. |
| Primary/Secondary Switching Logs | Records switchovers between the primary and secondary instances within the last month. |

## 15 Backup

### 15.1 Back up an ApsaraDB RDS for PostgreSQL instance

**PostgreSQL instance**

This topic describes how to back up an ApsaraDB RDS for PostgreSQL instance. You can configure a backup policy that is used to automatically back up your ApsaraDB RDS instance. If you do not configure a backup policy, the default backup policy is used. You can also manually back up your ApsaraDB RDS instance.

**Precautions**

Do not execute data definition language (DDL) statements during a backup. These statements trigger locks on tables, and the backup may fail as a result of the locks. We recommend that you back up your ApsaraDB RDS instance during off-peak hours. If your ApsaraDB RDS instance has a large amount of data, a backup may require a long period of time. Backup files are retained for a specific retention period. Before the specific retention period elapses, we recommend that you download the required backup files to your computer.

**Backup description**

ApsaraDB RDS for PostgreSQL allows you to perform full physical backup and back up archived redo log files of databases.

**Configure a backup policy for automatic backups**

ApsaraDB RDS can automatically back up your instance based on the backup policy that you specify.
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. On the **Backup and Restoration** page, click the **Backup Settings** tab and click **Edit**.
6. In the dialog box that appears, configure the following parameters and click **OK**. The
following table lists the parameters.

| Paramete r | Description |
|---|---|
| Data Retention Period | The number of days for which you want to retain data backup files. Valid values: 7 to 730. Unit: days. Default value: 7. |
| Backup Cycle | The cycle to create backups. You can select one or more days of the week. Note To ensure data security, we recommend that you back up your ApsaraDB RDS instance at least twice a week. |
| Backup Time | The period of time for which you want to back up data. Unit: hours. |

| Log Backup | Specifies whether to enable the log backup feature. Important If you disable this feature, all log backup files are deleted and your instance cannot be restored to previous points in time. |
|---|---|
| Log Retention Period | The period of time for which you want to retain log backup files. Valid values: 7 to 730. Unit: days. Default value: 7. The log retention period must be less than or equal to the data retention period. |
| OSS Dump Status | Specifies whether to enable Object Storage Service (OSS) dump. When OSS dump is enabled, new backup files are automatically dumped to a specific OSS bucket. Valid values: Enabled Disabled |
| OSS Dumped Data | The type of backup files that are dumped to an OSS bucket. You can select multiple values. Valid values: Data Backup Log Backup |
| OSS Bucket | The OSS bucket to which you want to dump backup files. |

**Manually back up your ApsaraDB RDS instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the upper-right corner of the page, click **Back Up Instance**. The **Back Up Instance**
dialog box appears.
5. Select the backup mode and backup policy, and click **OK**.

> **Note:** The backup mode is **Full Backup** and the backup policy is **Instance** **Backup**.

**What to do next**

You can click the icon in the upper-right corner of the page to view the task progress displayed in the **Task Progress** list.

### 15.2 Download data and log backup files

**backup files**

This topic describes how to download unencrypted data and log backup files in the ApsaraDB RDS console to archive the files and restore data to an on-premises database.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Backup and Restoration** to go to the **Backup and**
**Restoration** page.
5. Click the Data Backup or Archived Logs tab.
To download data backup files, click the **Data Backup** tab. To download log files, click the **Archived Logs** tab.
6. Select a time range to which you want to restore the instance.
7. Find the data backup or log file that you want to download and click **Download** in the
**Actions** column.

> **Note:** If you want to download a data backup file and use the file to restore data, we recommend that you select the data backup file that is created at the point in time closest to the point in time at which the required data exists.
> If you want to download an archived log backup file and use the file to restore data to an on-premises database, take note of the following items:
> The instance No. of the log file must be the same as that of the data backup file.
> The start time of the log file must be later than the data backup time and earlier than the time for restoration.

8. In the message that appears, select a download method.

| Download method | Description |
|---|---|
| Download | Download the file by using the public endpoint. |
| Copy Internal Endpoint | Copy the internal endpoint to download the file. If your ECS and ApsaraDB RDS instances are deployed within the same region, you can log on to the ECS instance and use the internal endpoint to download the file. This method is fast and secure. |
| Copy Public Endpoint | Copy the public endpoint to download the file. If you want to use other tools to download the file, use the public endpoint. |

> **Note:** If you use a Linux operating system, you can run the following command to download the file:

```
wget -c '<Public endpoint of the backup file, which is the download URL>' -O <Fil e name>
```

> The -c option enables resumable download.
> The -O option saves the downloaded file by using a specified name. We recommend that you use the file name contained in the download URL.
> If the URL contains more than one parameter, enclose the download URL in a pair of single quotation marks (').

### 15.3 Create a logical backup for an ApsaraDB RDS for PostgreSQL instance

**an ApsaraDB RDS for PostgreSQL**

**instance**

This topic describes how to use the pg_dump utility to create a logical backup for an ApsaraDB RDS for PostgreSQL instance and export the backup file to your computer.

**Background information**

The pg_dump utility provided with PostgreSQL is used to back up individual databases. For more information, see pg_dump. In this example, an RDS instance that runs PostgreSQL 10 and a host that runs CentOS 7 are used.

**Prerequisites**

The IP address of your Elastic Compute Service (ECS) instance or on-premises host is added to the whitelist of an ApsaraDB RDS for PostgreSQL instance. For more information, see Configure an IP address whitelist. Your ECS instance or on-premises host runs the same version of PostgreSQL as your ApsaraDB RDS for PostgreSQL instance.

**Precautions**

We recommend that you use the privileged account of the RDS instance. This ensures that you have all the required permissions.

**Back up a database**

1. Log on to your ECS instance or on-premises host. Then, run the following command to back
up a database of the RDS instance:

```
pg_dump -h '<hostname>' -U <username> -p <port> -Fc <dbname> > <dumpdir>
```

| Parameter | Description |
|---|---|

| hostname | The endpoint that is used to connect to the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance uses an internal endpoint to connect to the RDS instance, you must make sure that the ECS instance and the RDS instance use the same network type. If both instances use the VPC network type, you must also make sure that they reside in the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
|---|---|
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number that is used to connect to the ApsaraDB RDS for PostgreSQL instance. |
| -Fc | The format of the output file. -Fc specifies the use of the custom format. This format is ideal when you use pg restore to _ import logical backup files and restore databases. For more information, see pg dump. _ |
| dbname | The name of the database that you want to back up. |
| dumpdir | The directory and name of the logical backup file to export. |

Example

```
pg_dump -h 'pgm-bpxxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -Fc testdb > /tmp/te stdb.dump
```

2. When `Password:` appears on the command line, enter the password of the privileged
account of the RDS instance and press the Enter key.

**Back up one or more tables**

1. Log on to your ECS instance or on-premises host. Then, run the following command to back
up one or more tables from a database in the RDS instance:

```
pg_dump -h '<hostname>' -U <username> -p <port> -t <table> -Fc <dbname> > <dumpdir>
```

| Parameter | Description |
|---|---|

| hostname | The endpoint that is used to connect to the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance uses an internal endpoint to connect to the RDS instance, you must make sure that the ECS instance and the RDS instance use the same network type. If both instances use the VPC network type, you must also make sure that they reside in the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |   |   |
|---|---|---|---|
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |   |   |
| port | The port number that is used to connect to the ApsaraDB RDS for PostgreSQL instance. |   |   |
| table | The name of the table that you want to back up. You can use -t <table> to specify multiple tables. |   |   |
|   |   | -t |   |
| -Fc | The format of the output file. -Fc specifies the use of the custom format. This format is ideal when you use pg restore to _ import logical backup files and restore databases. For more information, see pg dump. _ |   |   |
| dbname | The name of the database that you want to back up. |   |   |
| dumpdir | The directory and name of the logical backup file to export. |   |   |

|   | <table> |
|---|---|

Example

```
pg_dump -h 'pgm-bpxxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -t products1 -Fc tes tdb2 > /tmp/testdb2.dump
```

2. When `Password:` appears on the command line, enter the password of the privileged
account of the RDS instance and press the Enter key.

**Back up a database with one or more tables excluded**

1. Log on to your ECS instance or on-premises host. Then, run the following command to back
up a database from the RDS instance with one or more tables excluded:

```
pg_dump -h '<hostname>' -U <username> -p <port> -T <table> -Fc <dbname> > <dumpdir>
```

| Parameter | Description |
|---|---|
| hostname | The endpoint that is used to connect to the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance uses an internal endpoint to connect to the RDS instance, you must make sure that the ECS instance and the RDS instance use the same network type. If both instances use the VPC network type, you must also make sure that they reside in the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |

| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |   |   |
|---|---|---|---|
| port | The port number that is used to connect to the ApsaraDB RDS for PostgreSQL instance. |   |   |
| table | The name of the table that you want to exclude. You can use -T <table> to specify multiple tables. |   |   |
|   |   | -T |   |
| -Fc | The format of the output file. -Fc specifies the use of the custom format. This format is ideal when you use pg restore to _ import logical backup files and restore databases. For more information, see pg dump. _ |   |   |
| dbname | The name of the database that you want to back up. |   |   |
| dumpdir | The directory and name of the logical backup file to export. |   |   |

|   | <table> |
|---|---|

Example

```
pg_dump -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -T products1 -Fc test db2 > /tmp/testdb2.dump
```

2. When `Password:` appears on the command line, enter the password of the privileged
account of the RDS instance and press the Enter key.

**Back up the schema of a database with data excluded**

1. Log on to your ECS instance or on-premises host. Then, run the following command to back
up the schema of a database from the RDS instance:

```
pg_dump -h '<hostname>' -U <username> -p <port> -s -Fc <dbname> > <dumpdir>
```

| Parameter | Description |
|---|---|
| hostname | The endpoint that is used to connect to the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance uses an internal endpoint to connect to the RDS instance, you must make sure that the ECS instance and the RDS instance use the same network type. If both instances use the VPC network type, you must also make sure that they reside in the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number that is used to connect to the ApsaraDB RDS for PostgreSQL instance. |
| -s | Specifies that only the schema of the database is backed up. The data of the database is not backed up. For more information, see pg dump. _ |

| -Fc | The format of the output file. -Fc specifies the use of the custom format. This format is ideal when you use pg restore to _ import logical backup files and restore databases. For more information, see pg dump. _ |
|---|---|
| dbname | The name of the database that you want to back up. |
| dumpdir | The directory and name of the logical backup file to export. |

Example

```
pg_dump -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -s -Fc testdb2 > /tmp /testdb2.dump
```

2. When `Password:` appears on the command line, enter the password of the privileged
account of the RDS instance and press the Enter key.

### 15.4 Create a full backup of an ApsaraDB RDS for PostgreSQL instance

**ApsaraDB RDS for PostgreSQL**

**instance**

This topic describes how to use the pg_basebackup utility provided by open source PostgreSQL to create a full backup of your ApsaraDB RDS for PostgreSQL instance and export the backup files to your computer.

**Prerequisites**

The IP address of your ECS instance or host is added to a whitelist of your ApsaraDB RDS for PostgreSQL instance. For more information, see Configure an IP address whitelist. Your ECS instance or host runs the same version of PostgreSQL as the ApsaraDB RDS for PostgreSQL instance.

**Background information**

pg_basebackup backs up all data of a PostgreSQL instance. Backup files can be used for point-in-time recovery. For more information, visit pg_basebackup. In this example, CentOS 7 is used to create a full backup.

**Precautions**

We recommend that you use the privileged account of the ApsaraDB RDS for PostgreSQL instance to ensure that you have all the required permissions.

**Procedure**

> **Note:** pg_basebackup cannot back up a single database or database object. For more information about how to back up a single database or database object, see Create a logical backup for an ApsaraDB RDS for PostgreSQL instance.

1. Log on to your ECS instance or host. Then, run the following command to back up a
database from the ApsaraDB RDS for PostgreSQL instance:

```
pg_basebackup -Ft -Pv -Xf -z -D <backupdir> -Z5 -h '<hostname>' -p <port> -U <usernam e> -W
```

The following table describes the parameters in this command. For more information, visit pg_basebackup.

| Parameter | Description |
|---|---|
| backupdir | The directory of backup files that are exported. The system automatically creates this directory. However, if this directory already exists and is not empty, the system reports an error. |
| hostname | The internal endpoint of the ApsaraDB RDS for PostgreSQL instance. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| port | The port number of the ApsaraDB RDS for PostgreSQL instance. |
| username | A username of the ApsaraDB RDS for PostgreSQL instance. |

Example:

```
pg_basebackup -Ft -Pv -Xf -z -D /pg12/backup1/ -Z5 -h pgm-bpxxxxx.pg.rds.aliyuncs.com -p 1433 -U test1 -W
```

2. When `Password:` appears, enter the password of the username of the ApsaraDB RDS for
PostgreSQL instance and press the Enter key.

## 16 Restoration

### 16.1 Restore data of an ApsaraDB RDS for PostgreSQL instance

**RDS for PostgreSQL instance**

This topic describes how to use the backups of an ApsaraDB RDS for PostgreSQL instance to restore data.

**Usage notes**

The new instance has the same IP address whitelists, backup settings, and parameter settings as the original instance. The new instance has the same data and account information as the backup set or instance at the time point.

**Prerequisites**

The original RDS instance whose data you want to restore must meet the following requirements: The original RDS instance is in the Running state and is not locked. The original RDS instance does not have ongoing migration tasks. If you want to restore data to a point in time, the log backup feature is enabled for the original RDS instance. If you want to restore individual databases or tables from a backup set, make sure that at least one backup set is available.

**Restore data of an ApsaraDB RDS for PostgreSQL instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. In the upper-right corner of the page, click **Restore Database (Previously Clone**
**Database)**.
6. Configure the following parameters:

| Section | Paramete r | Description |
|---|---|---|
| Area | Region | The region where the instance is deployed. |
| Restore Database | Restore Mode | By Time: allows you to restore the data to a point in time within the specified log backup retention period. For more information about how to view or change the log backup retention period, see Back up an ApsaraDB RDS for PostgreSQL instance. By Backup Set: allows you to restore the data from a backup set. Note The By Time option is available only after the log backup feature is enabled. |
| Document Ver | sion: 20231213 8 |   |

| Guide·Restora |   |   |
|---|---|---|
|   | Restore Time | The time to which the database is restored. This parameter is displayed when you set Restore Mode to By Time. |
|   | Backup Set | The backup set used to restore the database. This parameter is displayed when you set Restore Mode to By Backup Set. |
| Specificat ions | Instance Name | The name of the instance. |
|   | Database Engine | The engine of the database. The value of this parameter is set to PostgreSQL and cannot be changed. |
|   | Engine Version | The version of the database engine. The value of this parameter is set to the engine version of the current instance and cannot be changed. |
|   | Edition | The edition of the instance. |
|   | Storage Type | The storage type of the instance. The value of this parameter is set to the storage type of the current instance and cannot be changed. |
|   | Instance Type | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. Valid values: 20 to 6000. Unit: GB. The value is in 5 GB increments. |
| Network | Network Type | The network type of the instance. ApsaraDB RDS instances support the following network types: Classic Network: Cloud services on a classic network are not isolated from each other. Unauthorized access to a cloud service is blocked only by the security group or whitelist of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Note If you set the network type to VPC, you must also select a VPC and a vSwitch. |

7. Click **Submit**.

### 16.2 Restore data from a logical backup file

**backup file**

This topic describes how to restore data from a logical backup file to an ApsaraDB RDS for PostgreSQL instance or an on-premises PostgreSQL database.

**Background information**

A logical backup file is used to restore a small amount of data, such as data in a table. For a large amount of data, we recommend that you restore it from a full physical backup file to a new ApsaraDB RDS instance and then use Data Transmission Service (DTS) to migrate data to the original ApsaraDB RDS instance.

**Prerequisites**

Data in the ApsaraDB RDS for PostgreSQL instance is logically backed up. For more information, see Create a logical backup for an ApsaraDB RDS for PostgreSQL instance.

**Precautions**

We recommend that you do not restore data to the default postgres database. When you restore the data of a table, the system does not restore the database objects on which the table depends. The restoration may fail.

**Restore the data of a database**

1. Log on to the ECS instance or on-premises host that houses the logical backup file and run
the following command to restore the data of a database:

```
pg_restore -h '<hostname>' -U <username> -p <port> -d <dbname> <dumpdir>
```

| Parameter | Description |
|---|---|
| hostname | The endpoint of the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance connects to the ApsaraDB RDS for PostgreSQL instance by using an internal endpoint, make sure that the ECS and ApsaraDB RDS instances have the same network type. If both instances are of the VPC network type, make sure that both instances reside within the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number of the ApsaraDB RDS for PostgreSQL instance. |
| dbname | The name of the database whose data you want to restore. |
| dumpdir | The directory and name of the logical backup file to use. |

Example:

```
pg_restore -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -d testdb2 /tmp/te stdb.dump
```

2. When `Password:` appears, enter the password of the privileged account of your ApsaraDB
RDS instance and press the Enter key.

> **Note:** You can ignore alerts generated by the embedded plpgsql plug-in.

**Restore the data of a table**

1. Log on to the ECS instance or on-premises host that houses the logical backup file and run
the following command to restore the data of a table:

```
pg_restore -h '<hostname>' -U <username> -p <port> -d <dbname> -t <table> -c <dumpdir
```

`>`

| Parameter | Description |
|---|---|
| hostname | The endpoint of the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance connects to the ApsaraDB RDS for PostgreSQL instance by using an internal endpoint, make sure that the ECS and ApsaraDB RDS instances have the same network type. If both instances are of the VPC network type, make sure that both instances reside within the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number of the ApsaraDB RDS for PostgreSQL instance. |
| dbname | The name of the database whose data you want to restore. |
| table | The name of the table whose data you want to restore. |
| -c | -c : specifies to delete the database objects on which the table depends before data restoration. For more information, visit pg restore. _ |
| dumpdir | The directory and name of the logical backup file to use. |

Example:

```
pg_restore -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -d testdb2 -t prod ucts -c /tmp/testdb.dump
```

2. When `Password:` appears, enter the password of the privileged account of your ApsaraDB
RDS instance and press the Enter key.

**Restore the schema of a database with data excluded**

1. Log on to the ECS instance or on-premises host that houses the logical backup file and run
the following command to restore only the schema of a database:

```
pg_restore -h '<hostname>' -U <username> -p <port> -d <dbname> -s <dumpdir>
```

| Parameter | Description |
|---|---|

| hostname | The endpoint of the ApsaraDB RDS for PostgreSQL instance. Note If your ECS instance connects to the ApsaraDB RDS for PostgreSQL instance by using an internal endpoint, make sure that the ECS and ApsaraDB RDS instances have the same network type. If both instances are of the VPC network type, make sure that both instances reside within the same VPC. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
|---|---|
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number of the ApsaraDB RDS for PostgreSQL instance. |
| dbname | The name of the database whose schema you want to restore. |
| -s | -s : specifies to restore only the schema of the database. The data of the database is not restored. For more information, visit pg restore. _ |
| dumpdir | The directory and name of the logical backup file to use. |

Example:

```
pg_restore -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -d testdb4 -s /tmp /testdb2.dump
```

2. When `Password:` appears, enter the password of the privileged account of your ApsaraDB
RDS instance and press the Enter key.

> **Note:** You can ignore alerts generated by the embedded plpgsql plug-in.

## 17 CloudDBA

### 17.1 Introduction to CloudDBA

CloudDBA is a cloud service for database self-detection, self-repair, self-optimization, selfmaintenance, and self-security based on machine learning and expertise. CloudDBA helps you ensure stable, secure, and efficient databases without worrying about the management complexity and service failures caused by manual operations.

**Features**

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the following features: You can diagnose your instance and view the visualized diagnostic results. You can view sessions, check session statistics, analyze SQL statements, and optimize the execution of SQL statements. You can view the real-time information of your instance, such as the queries per second (QPS), transactions per second (TPS), number of connections, and network traffic. You can view the storage overview, trends, exceptions, tablespaces, and data spaces. You can view and compare performance trends, customize monitoring dashboards, check exceptions, and view instance topologies. You can view the trends and statistics of slow queries.

### 17.2 Diagnostics

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the diagnostics feature. This feature diagnoses your ApsaraDB RDS for PostgreSQL instance and provides visualized results.

**Navigate to the Diagnostics tab**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**.

> **Note:** For more information, see Diagnostics in **Database Autonomy Service** **User Guide**.

### 17.3 Session management

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the session management feature. This feature allows you to view and manage the sessions of an instance.

**Navigate to the Session Management tab**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**.
4. Click the **Session Management** tab.

> **Note:** For more information, see Instance sessions in **Database Autonomy** **Service User Guide**.

### 17.4 Real-time monitoring

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the real-time monitoring feature. This feature allows you to view the real-time performance of your ApsaraDB RDS for PostgreSQL instance.

**Navigate to the Real-time Monitoring tab**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**.
4. Click the **Real-time Monitoring** tab.

> **Note:** For more information, see Real-time monitoring in **Database Autonomy** **Service User Guide**.

### 17.5 Storage analysis

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the storage analysis feature. This feature allows you to check and solve storage exceptions in a timely manner to ensure database stability.

**Background information**

You can use the storage analysis feature of CloudDBA to view the disk space usage of your ApsaraDB RDS for PostgreSQL instance and the number of remaining days when disk space is available. It also provides information about the space usage, fragmentation, and exception diagnostic results of a table.

**Navigate to the Storage Analysis tab**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Diagnostics**.
4. Click the **Storage Analysis** tab.

> **Note:** For more information, see Storage analysis in **Database Autonomy** **Service User Guide**.

### 17.6 Dashboard

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the dashboard feature. This feature allows you to view performance trends in specific ranges, compare performance trends, and customize charts to view performance trends.

**Navigate to the Dashboard page**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Dashboard**.

> **Note:** For more information, see Dashboard in **Database Autonomy Service** **User Guide**.

### 17.7 Slow query logs

In ApsaraDB RDS for PostgreSQL, CloudDBA provides the slow query logs feature. This feature allows you to view the trends and execution details of slow queries and obtain optimization suggestions for your ApsaraDB RDS for PostgreSQL instance.

**Navigate to the Slow Query Logs page**

1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Slow Query Logs**.

> **Note:** For more information, see Slow query logs in **Database Autonomy** **Service User Guide**.

## 18 Plug-ins

### 18.1 Plug-ins supported

This topic describes the plug-ins that are supported by ApsaraDB RDS for PostgreSQL and their available versions.

|   | Note The following table only lists the common plug-ins. After connecting to the instance, you can use the SELECT * FROM pg available extensions; command to view all plug-ins and versions supported by _ _ the current instance. The actual query results prevail. If the queried plug-in versions are different from the following table, upgrade the cloud environment to the latest version. |
|---|---|
|   | pg available extensions; _ _ |

| Extension name | 13 | 12 | 11 | 10 |
|---|---|---|---|---|
| address standardizer _ | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 |
| address standardizer data u _ _ _ s | 3.1.4 | 3.1.4 | 3.1.4 | 3.1.4 |
| aggs for arrays _ _ | Not supported | Not supported | Not supported | 1.3.1 |
| bloom | 1.0 | 1.0 | 1.0 | 1.0 |
| btree gin _ | 1.3 | 1.3 | 1.3 | 1.2 |
| btree gist _ | 1.5 | 1.5 | 1.5 | 1.5 |
| chkpass | Not supported | Not supported | Not supported | 1.0 |
| citext | 1.6 | 1.6 | 1.5 | 1.4 |
| cube | 1.4 | 1.4 | 1.4 | 1.2 |
| dblink | 1.2 | 1.2 | 1.2 | 1.2 |
| decoderbufs | 0.1.0 | 0.1.0 | 0.1.0 | 0.1.0 |

| dict int _ | 1.0 | 1.0 | 1.0 | 1.0 |
|---|---|---|---|---|
| earthdistance | 1.1 | 1.1 | 1.1 | 1.1 |
| fuzzystrmatch | 1.1 | 1.1 | 1.1 | 1.1 |
| ganos address standardizer _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos address standardizer _ _ _ data us _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos geometry _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos geometry pyramid _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos geometry sfcgal _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos geometry topology _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos networking _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos pointcloud _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos pointcloud geometry _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos raster _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos spatialref _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos tiger geocoder _ _ | 5.5 | 5.5 | 5.5 | 5.5 |
| ganos trajectory _ | 5.5 | 5.5 | 5.5 | 5.5 |
| hll | 2.15 | 2.14 | 2.14 | Not supported |
| hstore | 1.7 | 1.6 | 1.5 | 1.4 |
| hypopg | 1.3.1 | 1.3.1 | 1.3.1 | 1.3.1 |

| index adviser _ | 2.0 | 2.0 | 2.0 | 2.0 |
|---|---|---|---|---|
| intagg | 1.1 | 1.1 | 1.1 | 1.1 |
| intarray | 1.3 | 1.2 | 1.2 | 1.2 |
| ip4r | 2.4 | Not supported | Not supported | Not supported |
| isn | 1.2 | 1.2 | 1.2 | 1.1 |
| ltree | 1.2 | 1.1 | 1.1 | 1.1 |
| log fdw _ | Not supported | Not supported | 1.0 | Not supported |
| madlib | Not supported | 1.18.0 | 1.18.0 | Not supported |
| mysql fdw _ | 1.1 | 1.1 | 1.1 | 1.1 |
| oracle fdw _ | Not supported | 1.1 | Not supported | Not supported |
| orafce | Not supported | Not supported | 3.8 | 3.6 |
| oss fdw _ | 1.1 | 1.1 | 1.1 | 1.1 |
| pase | 0.0.1 | 0.0.1 | 0.0.1 | Not supported |
| pg bigm _ | 1.2 | 1.2 | 1.2 | 1.2 |
| pg buffercache _ | 1.3 | 1.3 | 1.3 | 1.3 |
| pg concurrency control _ _ | Not supported | Not supported | 1.0 | 1.0 |
| pg cron _ | 1.1 | 1.1 | 1.1 | 1.1 |
| pg freespacemap _ | 1.2 | 1.2 | 1.2 | 1.2 |

| pg jieba _ | 1.1.0 | 1.1.0 | 1.1.0 | 1.1.0 |
|---|---|---|---|---|
| pg hint plan _ _ | 1.3.7 | 1.3.7 | 1.3.7 | 1.3.0 |
| pg pathman _ | 1.5 | 1.5 | 1.5 | 1.5 |
| pg prewarm _ | 1.2 | 1.2 | 1.2 | 1.1 |
| pg profile _ | 4.1 | 4.1 | 4.1 | 4.1 |
| pg repack _ | 1.4.6 | 1.4.6 | 1.4.6 | 1.4.6 |
| pg sphere _ | Not supported | Not supported | Not supported | 1.0 |
| pg stat kcache _ _ | 2.2.1 | 2.2.1 | 2.2.1 | 2.2.1 |
| pg stat statements _ _ | 1.8 | 1.7 | 1.6 | 1.6 |
| pg trgm _ | 1.5 | 1.4 | 1.4 | 1.3 |
| pgaudit | 1.5 | 1.4.1 | 1.3.2 | 1.2.2 |
| pgcrypto | 1.3 | 1.3 | 1.3 | 1.3 |
| pgl ddl deploy _ _ | 2.1 | Not supported | Not supported | Not supported |
| pglogical | 2.4.2 | 2.4.2 | 2.4.0 | 2.4.0 |
| pgrouting | 3.4.2 | 3.4.2 | 3.4.2 | 3.4.2 |
| pgrowlocks | 1.2 | 1.2 | 1.2 | 1.2 |
| pgstattuple | 1.5 | 1.5 | 1.5 | 1.5 |
| pldebugger | 1.1 | 1.1 | 1.1 | 1.1 |
| plperl | 1.0 | 1.0 | 1.0 | 1.0 |

| plpgsql | 1.0 | 1.0 | 1.0 | 1.0 |
|---|---|---|---|---|
| plproxy | 2.10.0 | 2.9.0 | 2.9.0 | 2.8.0 |
| pltcl | 1.0 | 1.0 | 1.0 | 1.0 |
| plv8 | 2.3.15 | 2.3.15 | 2.3.15 | 2.3.15 |
| postgis | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 |
| postgis sfcgal _ | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 |
| postgis tiger geocoder _ _ | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 |
| postgis topology _ | 3.3.2 | 3.3.2 | 3.3.2 | 3.3.2 |
| postgres fdw _ | 1.0 | 1.0 | 1.0 | 1.0 |
| q3c | Not supported | Not supported | Not supported | 1.5.0 |
| rdkit | Not supported | 3.8 | Not supported | Not supported |
| rds tde utils _ _ | 1.0 | 1.0 | 1.0 | 1.0 |
| roaringbitmap | 0.5 | 0.5 | Not supported | Not supported |
| rum | 1.3 | 1.3 | 1.3 | 1.3 |
| sequential-uuids | 1.0.2 | 1.0.2 | 1.0.2 | 1.0.2 |
| smlar | 1.0 | 1.0 | 1.0 | 1.0 |
| sql firewall _ | Not supported | 0.8 | 0.8 | 0.8 |
| sslinfo | 1.2 | 1.2 | 1.2 | 1.2 |

| tablefunc | 1.0 | 1.0 | 1.0 | 1.0 |
|---|---|---|---|---|
| tds fdw _ | 2.0.3 | 2.0.1 | 2.0.1 | Not supported |
| timescaledb | 2.5.0 | 1.7.1 | 1.7.1 | 1.3.0 |
| tsm system rows _ _ | 1.0 | 1.0 | 1.0 | 1.0 |
| tsm system time _ _ | 1.0 | 1.0 | 1.0 | 1.0 |
| unaccent | 1.1 | 1.1 | 1.1 | 1.1 |
| uuid-ossp | 1.1 | 1.1 | 1.1 | 1.1 |
| varbitx | Not supported | Not supported | 1.0 | 1.0 |
| wal2json | 2.3 | 2.3 | 2.2 | 2.2 |
| xml2 | 1.1 | 1.1 | 1.1 | 1.1 |
| zhparser | 1.0 | 1.0 | 1.0 | 1.0 |
| zombodb | Not supported | Not supported | 4.0 | Not supported |

### 18.2 Use mysql_fdw to read and write data from and to a MySQL database

**write data from and to a MySQL**

**database**

This topic describes how to use the mysql_fdw extension of ApsaraDB RDS for PostgreSQL to read data from and write data to a MySQL database. The MySQL database can be a database on an ApsaraDB RDS for MySQL instance or a self-managed MySQL database.

**Prerequisites**

The instance runs PostgreSQL 10. The ApsaraDB RDS for PostgreSQL instance and the MySQL database are interconnected.

**Background information**

PostgreSQL 9.6 and later versions support parallel computing. PostgreSQL 11 can complete join queries on 1 billion data records within seconds. A large number of users use PostgreSQL to build lightweight data warehouses that can handle highly concurrent requests. The mysql_fdw extension can establish a connection and synchronize data between an ApsaraDB RDS for PostgreSQL instance and a MySQL database.

**Procedure**

1. Log on to a database of your ApsaraDB RDS for PostgreSQL instance. For more information,
see Connect to an ApsaraDB RDS for PostgreSQL instance.
2. Create the mysql_fdw extension.

```
create extension mysql_fdw;
```

3. Define a MySQL server.

```
CREATE SERVER <Name of the MySQL server> FOREIGN DATA WRAPPER mysql_fdw OPTIONS (host '<Endpoint used to connect to the MySQL server>', port '<Port used to c onnect to the MySQL server>');
```

Example:

```
CREATE SERVER mysql_server FOREIGN DATA WRAPPER mysql_fdw OPTIONS (host 'rm-xxx.mysql.rds.aliyuncs.com', port '3306');
```

4. Map the MySQL server to an account that is created on the RDS instance. You can use the
account to read data from and write data to the MySQL database, which resides on the MySQL server.

```
CREATE USER MAPPING FOR <Username of the account to which the MySQL server is mapped> SERVER <The name of the MySQL server> OPTIONS (username '<The username of the account that is used to connect to the MySQL database>', password '<The password of the preceding account>');
```

Example:

```
CREATE USER MAPPING FOR pgtest SERVER mysql_server OPTIONS (username 'mysqltest', password 'Test1234!');
```

5. Create a foreign MySQL table by using the account that you mapped to the MySQL server
in the previous step.

> **Note:** The field names in the foreign MySQL table must be the same as the field names in the table in the MySQL database. You can choose to create only the fields that you want to query. For example, if the table in the MySQL database contains the ID, NAME, and AGE fields, you can create only the ID and NAME fields in the foreign MySQL table.

```
CREATE FOREIGN TABLE <Name of the foreign MySQL table> (<Name of Field 1> <Data type of Field 1>,<Name of Field 2> <Data type of Field 2>...) server <Name of the MySQL se rver> options (dbname '<Name of the MySQL database>', table_name '<Name of the table in the MySQL database>');
```

Example:

```
CREATE FOREIGN TABLE ft_test (id1 int, name1 text) server mysql_server options (dbnam e 'test123', table_name 'test');
```

**What to do next**

You can use the foreign MySQL table to check whether the extension has enabled read and write operations on the MySQL database.

> **Note:** Data can be written to the table in the MySQL database only when the table is assigned a primary key. If the table is not assigned a primary key, the following error is returned:

```
ERROR: first column of remote table must be unique for INSERT/UPDATE/DELETE operation. select * from ft_test ; insert into ft_test values (2,'abc'); insert into ft_test select generate_series(3,100),'abc'; select count(*) from ft_test ;
```

Run postgres=> explain verbose select count(*) from ft_test; to find out how the requests sent from your ApsaraDB RDS for PostgreSQL instance are executed to query data from the MySQL database. Sample output:

```
                                  QUERY PLAN
-------------------------------------------------------------------------------
 Aggregate  (cost=1027.50..1027.51 rows=1 width=8)
   Output: count(*)
   ->  Foreign Scan on public.ft_test  (cost=25.00..1025.00 rows=1000 width=0)
         Output: id, info
         Remote server startup cost: 25
         Remote query: SELECT NULL FROM `test123`.`test`
(6 rows)
```

### 18.3 Use oss_fdw to read and write foreign data files

**write foreign data files**

This topic describes how to use the oss_fdw plug-in to load data between Object Storage Service (OSS) and PostgreSQL or PPAS databases.

**oss_fdw parameters**

The oss_fdw plug-in uses a method similar to other Foreign Data Wrapper (FDW) interfaces to encapsulate foreign data stored in OSS. You can use oss_fdw to read data stored in OSS. This process is similar to reading data tables. oss_fdw provides unique parameters to connect and parse file data in OSS.

> **Note:** oss_fdw can read and write files of the following types in OSS: TXT and CSV files as well as GZIP-compressed TXT and CSV files.
> The value of each parameter must be enclosed in double quotation marks (") and cannot contain unnecessary spaces.

**CREATE SERVER parameters**

ossendpoint: the endpoint used to access OSS over the internal network, also known as the host. id oss: the AccessKey ID of the OSS account. key oss: the AccessKey secret of the OSS account. bucket: the bucket where the data you want to access is stored. You must create an OSS account before you specify this parameter. The following fault tolerance parameters can be used for data import and export. If network connectivity is poor, you can adjust these parameters to ensure successful import and export. oss_connect_timeout: the connection timeout period. Default value: 10. Unit: seconds. oss_dns_cache_timeout: the DNS timeout period. Default value: 60. Unit: seconds. oss_speed_limit: the minimum data transmission rate. Default value: 1024. Unit: bytes/s. oss_speed_time: the maximum waiting period during which the data transmission rate is lower than the minimum value. Default value: 15. Unit: seconds. If the default values of oss_speed_limit and oss_speed_time are used, a timeout error occurs when the transmission rate is lower than 1,024 bytes/s for 15 consecutive seconds.

**CREATE FOREIGN TABLE parameters**

filepath: a file name that contains a path in OSS. The file name specified by this parameter contains the directory name but not the bucket name. This parameter matches multiple files in the corresponding path in OSS. You can load multiple files to a database. You can import files that adhere to the filepath or filepath.x format to a database. The values of x must be consecutive numbers starting from 1. For example, among the files named filepath, filepath.1, filepath.2, filepath.3, and filepath.5, the first four files are matched and imported. The filepath.5 file is not imported. dir: the virtual file directory in OSS. The specified directory must end with a forward slash (/). All files (excluding subfolders and files in subfolders) in the virtual file directory specified by dir are matched and imported to a database. prefix: the prefix of the path name corresponding to the data file. The prefix does not support regular expressions. The prefix, filepath, and dir parameters are mutually exclusive. Therefore, only one of them can be specified at a time. format: the file format, which can only be CSV. encoding: the file data encoding format. It supports common PostgreSQL encoding formats, such as UTF-8. parse_errors: the fault-tolerant parsing mode. If an error occurs during the parsing process, the entire row of data is ignored. delimiter: the string used to delimit columns. quote: the quote character for files. escape: the escape character for files. null: sets the column matching the specified string to null. For example, null 'test' is used to set the value of the 'test' column to null. force_not_null: sets the value of a column to a non-null value. For example, force_not_null 'id' is used to set the value of the 'id' column to empty strings. compressiontype: the format of the files to be read or written in OSS. none: The files are uncompressed. This is the default value. gzip: The files are compressed in the GZIP format. compressionlevel: the degree to which data files written to OSS are compressed. Valid values: 1 to 9. Default value: 6.

> **Note:** You must specify filepath and dir in the OPTIONS parameter.
> You must specify filepath or dir.
> The export mode can only be dir.

**Export mode parameters for CREATE FOREIGN TABLE**

oss_flush_block_size: the buffer size for the data written to OSS at a time. Default value: 32. Valid values: 1 to 128. Unit: MB. oss_file_max_size: the maximum size of a data file allowed to be written to OSS. If a data file reaches the maximum size, the remaining data is written to another data file. Default value: 1024. Valid values: 8 to 4000. Unit: MB. num_parallel_worker: the maximum number of threads that are allowed to run in parallel to compress the data written to OSS. Valid values: 1 to 8. Default value: 3.

**Auxiliary functions**

FUNCTION oss_fdw_list_file (relname text, schema text DEFAULT 'public') This function obtains the name and size of the OSS file that a foreign table matches. The file size is measured in bytes. The following result is returned after select * from oss_fdw_list_file('t_oss'); is executed:

```
              name              |   size
--------------------------------+-----------
 oss_test/test.gz.1  | 739698350
 oss_test/test.gz.2  | 739413041
 oss_test/test.gz.3  | 739562048
(3 rows)
```

**Auxiliary features**

oss_fdw.rds_read_one_file: In read mode, this feature is used to specify a file to match the foreign table. The foreign table matches only the specified file during data import. Example: set oss_fdw.rds_read_one_file = 'oss_test/example16.csv.1';

| ed after | set oss fdw.rds read one file = _ _ _ _ |   |
|---|---|---|
| select * from oss fdw list file('t oss'); _ _ _ _ |   |   |
|   |   | are executed: |

```
              name              |   size
--------------------------------+-----------
  oss_test/test.gz.2  | 739413041
(1 rows)
```

**oss_fdw example**

```bash
# Create the plug-in for a PostgreSQL database.
create extension oss_fdw; -- For a PPAS database, execute select rds_manage_extension('create','oss_fdw');
# Create a server.
CREATE SERVER ossserver FOREIGN DATA WRAPPER oss_fdw OPTIONS
     (host 'oss-cn-hangzhou.aliyuncs.com', id 'xxx', key 'xxx', bucket 'mybucket');
# Create an OSS foreign table.
CREATE FOREIGN TABLE ossexample
    (date text, time text, open float,
     high float, low float, volume int)
     SERVER ossserver
     OPTIONS ( filepath 'osstest/example.csv', delimiter ',' ,
         format 'csv', encoding 'utf8', PARSE_ERRORS '100');
# Create a table named example to which to import data.
create table example
        (date text, time text, open float,
         high float, low float, volume int);
# Load data from ossexample to example.
insert into example select * from ossexample;
# Result
# oss_fdw estimates the file size in OSS and formulates a query plan.
explain insert into example select * from ossexample;
                             QUERY PLAN
---------------------------------------------------------------------
 Insert on example  (cost=0.00..1.60 rows=6 width=92)
   ->  Foreign Scan on ossexample  (cost=0.00..1.60 rows=6 width=92)
         Foreign OssFile: osstest/example.csv.0
         Foreign OssFile Size: 728
(4 rows)
# Write the data in the example table to OSS.
insert into ossexample select * from example; explain insert into ossexample select * from example;
                           QUERY PLAN
-----------------------------------------------------------------
 Insert on ossexample  (cost=0.00..16.60 rows=660 width=92)
   ->  Seq Scan on example  (cost=0.00..16.60 rows=660 width=92)
(2 rows)
```

**Additional considerations**

oss_fdw is a foreign table plug-in developed based on the PostgreSQL FOREIGN TABLE framework. The data import performance varies based on the PostgreSQL cluster resources (CPU, I/O, and memory) and OSS. To ensure data import performance, the ApsaraDB RDS for PostgreSQL instance must be in the same region as the OSS bucket.

**ID and key encryption**

If the id and key parameters for CREATE SERVER are not encrypted, the `select * from` `pg_foreign_server` statement execution result displays the information. Your AccessKey ID and AccessKey secret are exposed. You can use symmetric encryption to hide your AccessKey ID and AccessKey secret. Use different AccessKey pairs for different instances to further protect your information. However, to avoid incompatibility with earlier versions, do not add data types as you would in Greenplum. Encrypted information:

```
postgres=# select * from pg_foreign_server ;
  srvname  | srvowner | srvfdw | srvtype | srvversion | srvacl |
srvoptions -----------+----------+--------+---------+------------+--------+------------------------- ----------------------------------------------------------------------------------------- --------------- ----------------------------------
 ossserver |       10 |  16390 |         |            |        | {host=oss-cn-hangzhou-z
mf.aliyuncs.com,id=MD5xxxxxxxx,key=MD5xxxxxxxx,bucket=067862}
```

The encrypted information is preceded by the MD5 hash value. The remainder of the total length divided by 8 is 3. Therefore, encryption is not performed again when the exported data is imported. You cannot create an AccessKey pair that is preceded by MD5. e splitting in ApsaraDB RDS for P ostgreSQL

## 19 Use Pgpool for read/write splitting in ApsaraDB RDS for PostgreSQL

**splitting in ApsaraDB RDS for**

**PostgreSQL**

This topic describes how to use the Pgpool tool of PostgreSQL installed on an ECS instance to implement read/write splitting for your primary and read-only ApsaraDB RDS for PostgreSQL instances.

**Background information**

If you do not use Pgpool to ensure high availability, Pgpool is stateless. The decrease in performance can be ignored. Additionally, Pgpool supports horizontal scaling of your database system. You can use Pgpool and the high availability architecture of ApsaraDB RDS for PostgreSQL to implement read/write splitting.

**Set up a test environment**

If you have purchased a primary ApsaraDB RDS instance that runs PostgreSQL 10 and have attached read-only instances to the primary instance, you need only to install Pgpool . For more information, see Create an instance and Create a read-only ApsaraDB RDS for PostgreSQL instance. After you install Pgpool, go to Configure Pgpool.
1. Run the `vi /etc/sysctl.conf` command to open the sysctl.conf file. Modify the following
configurations:

```bash
# add by digoal.zhou
fs.aio-max-nr = 1048576 fs.file-max = 76724600
# Optional. Set the kernel.core_pattern parameter to
/data01/corefiles/core_%e_%u_%t_%s.%p.
# The /data01/corefiles directory that is used to store core dumps is created with th
e 777 permission before testing. If a symbolic link is used, change the directory to 777. kernel.sem = 4096 2147483647 2147483646 512000
# Specify the semaphore. You can run the ipcs -l or -u command to obtain the semaphor
e count. Each group of 16 processes requires a semaphore with a count of 17. kernel.shmall = 107374182
# Specify the total size of shared memory segments. Recommended value: 80% of the mem
ory capacity. Unit: pages. kernel.shmmax = 274877906944
# Specify the maximum size of a single shared memory segment. Recommended value: 50%
of the memory capacity. Unit: bytes. In PostgreSQL versions later than 9.2, the use o f shared memory significantly drops. kernel.shmmni = 819200
# Specify the total number of shared memory segments that can be generated. At least
two shared memory segments must be generated within each PostgreSQL cluster. net.core.netdev_max_backlog = 10000 net.core.rmem_default = 262144
#Thedefaultsettingofthesocketreceivebufferinbytes.
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
# The default setting of the socket receive buffer in bytes.
net.core.rmem_max = 4194304
# The maximum receive socket buffer size in bytes
net.core.wmem_default = 262144
# The default setting (in bytes) of the socket send buffer.
net.core.wmem_max = 4194304
# The maximum send socket buffer size in bytes.
net.core.somaxconn = 4096 net.ipv4.tcp_max_syn_backlog = 4096 net.ipv4.tcp_keepalive_intvl = 20 net.ipv4.tcp_keepalive_probes = 3 net.ipv4.tcp_keepalive_time = 60 net.ipv4.tcp_mem = 8388608 12582912 16777216 net.ipv4.tcp_fin_timeout = 5 net.ipv4.tcp_synack_retries = 2 net.ipv4.tcp_syncookies = 1
# Enable SYN cookies. If an SYN waiting queue overflows, you can enable SYN cookies t
o defend against a small number of SYN attacks. net.ipv4.tcp_timestamps = 1
# Reduce the time after which a network socket enters the TIME-WAIT state.
net.ipv4.tcp_tw_recycle = 0
# If you set this parameter to 1 to enable the recycle function, network sockets in t
he TIME-WAIT state over TCP connections are recycled. However, if network address tra nslation (NAT) is used, TCP connections may fail. We recommend that you set this para meter to 0 on the database server. net.ipv4.tcp_tw_reuse = 1
# Enable the reuse function. This function enables network sockets in the TIME-WAIT s
tate to be reused over new TCP connections. net.ipv4.tcp_max_tw_buckets = 262144 net.ipv4.tcp_rmem = 8192 87380 16777216 net.ipv4.tcp_wmem = 8192 65536 16777216 net.nf_conntrack_max = 1200000 net.netfilter.nf_conntrack_max = 1200000 vm.dirty_background_bytes = 409600000
# If the size of dirty pages reaches the specified limit, a background scheduling pro
cess (for example, pdflush) is invoked to flush the dirty pages to disks. These are t he pages that are generated n seconds earlier. The value of n is calculated by using the following formula: n = Value of the dirty_expire_centisecs parameter/100.
# The default limit is 10% of the memory capacity. If the memory capacity is large, w
e recommend that you specify the limit in bytes. vm.dirty_expire_centisecs = 3000
# Specify the maximum period to retain dirty pages. Dirty pages are flushed to disks
after the time period specified by this parameter elapses. The value 3000 indicates 3 0 seconds. vm.dirty_ratio = 95
# The processes that users call to write data onto disks must actively flush dirty pa
ges to disks. This applies when the background scheduling process to flush dirty page s is slow and the size of dirty pages exceeds 95% of the memory capacity. These proce sses include fsync and fdatasync.
# Set this parameter properly to prevent user-called processes from flushing dirty pa
ges to disks. This allows you to create multiple ApsaraDB RDS instances on a single s
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
erver and use control groups to limit the input/output operations per second (IOPS) p er instance. vm.dirty_writeback_centisecs = 100
# Specify the time interval at which the background scheduling process (such as pdflu
sh) flushes dirty pages to disks. The value 100 indicates 1 second. vm.swappiness = 0
# Disable the swap function.
vm.mmap_min_addr = 65536 vm.overcommit_memory = 0
# Specify whether you can allocate more memory space than the physical host has avail
able. If you set this parameter to 1, the system always considers the available memor y space sufficient. If the memory capacity provided in the test environment is low, w e recommend that you set this parameter to 1. vm.overcommit_ratio = 90
# Specify the memory capacity that can be allocated when the overcommit_memory parame
ter is set to 2. vm.swappiness = 0
# Disable the swap function.
vm.zone_reclaim_mode = 0
# Disable non-uniform memory access (NUMA). You can also disable NUMA in the vmlinux
file. net.ipv4.ip_local_port_range = 40000 65535
# Specify the range of TCP or UDP port numbers for the physical host to allocate.
fs.nr_open=20480000
# Specify the maximum number of file handles that a single process can open.
# Take note of the following parameters:
#vm.extra_free_kbytes = 4096000   # If the physical host provides a low memory capaci
ty, do not specify a large value such as 4096000. If you specify a large value, the p hysical host may not start.
#vm.min_free_kbytes = 6291456    # We recommend that you increase the value of the vm
.min_free_kbytes parameter by 1 GB for every 32 GB of memory.
# If the physical host does not provide much memory, we recommend that you do not con
figure vm.extra_free_kbytes and vm.min_free_kbytes.
# vm.nr_hugepages = 66536
# If the size of the shared buffer exceeds 64 GB, we recommend that you use huge page
s. You can specify the page size by setting the Hugepagesize parameter in the /proc/m eminfo file.
#vm.lowmem_reserve_ratio = 1 1 1
# If the memory capacity exceeds 64 GB, we recommend that you set this parameter. Oth
erwise, we recommend that you retain the default value 256 256 32.
```

2. Run the `vi /etc/security/limits.conf` command to open the limits.conf file. Modify the
following configurations: e splitting in ApsaraDB RDS for P ostgreSQL

```bash
* soft    nofile  1024000
* hard    nofile  1024000
* soft    nproc   unlimited
* hard    nproc   unlimited
* soft    core    unlimited
* hard    core    unlimited
* soft    memlock unlimited
* hard    memlock unlimited
# Comment out the other parameters in the limits.conf file.
# Comment out the /etc/security/limits.d/20-nproc.conf file.
```

3. Run the following commands to open the rc.local file:

```
chmod +x /etc/rc.local vi /etc/rc.local
```

Modify the following configurations to disable transparent huge pages, configure huge pages, and start PostgreSQL:

```bash
# Disable transparent huge pages.
if test -f /sys/kernel/mm/transparent_hugepage/enabled; then
   echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

`fi`

```bash
# Configure huge pages for two instances. Each instance has a shared buffer of 16 GB.
sysctl -w vm.nr_hugepages=17000
# Start the two instances.
su - postgres -c "pg_ctl start -D /data01/pg12_3389/pg_root" su - postgres -c "pg_ctl start -D /data01/pg12_8002/pg_root"
```

4. Create a file system.

> **Warning:** If you use a new disk, you must verify that the new disk belongs to the vdb partition instead of the vda partition. If the new disk belongs to the vda partition, data may be deleted from the new disk.

```
parted -a optimal -s /dev/vdb mklabel gpt mkpart primary 1MiB 100%FREE mkfs.ext4 /dev/vdb1 -m 0 -O extent,uninit_bg -E lazy_itable_init=1 -b 4096 -T largefi le -L vdb1 vi /etc/fstab LABEL=vdb1 /data01 ext4 defaults,noatime,nodiratime,nodelalloc,barrier=0,data=writeback 0 0 mkdir /data01 mount -a
```

5. Start the irqbalance command line tool.

```bash
systemctl status irqbalance systemctl enable irqbalance systemctl start irqbalance systemctl status irqbalance
```

e splitting in ApsaraDB RDS for P ostgreSQL
6. Install PostgreSQL 10 and Pgpool.

```bash
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgd g-redhat-repo-latest.noarch.rpm yum search all postgresql yum search all pgpool yum install -y postgresql12* yum install -y pgpool-II-12-extensions
```

7. Initialize the data directory of your database system.

```
mkdir /data01/pg12_3389 chown postgres:postgres /data01/pg12_3389
```

8. Configure environment variables for the postgres user.

```
su - postgres vi .bash_profile
```

Append the following parameters to the environment variables:

```
export PS1="$USER@`/bin/hostname -s`-> " export PGPORT=3389 export PGDATA=/data01/pg12_$PGPORT/pg_root export LANG=en_US.utf8 export PGHOME=/usr/pgsql-12 export LD_LIBRARY_PATH=$PGHOME/lib:/lib64:/usr/lib64:/usr/local/lib64:/lib:/usr/lib:/usr/local ib:$LD_LIBRARY_PATH export DATE=`date +"%Y%m%d%H%M"` export PATH=$PGHOME/bin:$PATH:. export MANPATH=$PGHOME/share/man:$MANPATH export PGHOST=$PGDATA export PGUSER=postgres export PGDATABASE=db1 alias rm='rm -i' alias ll='ls -lh' unalias vi
```

9. Initialize your primary ApsaraDB RDS instance.

```
initdb -D $PGDATA -U postgres -E UTF8 --lc-collate=C --lc-ctype=en_US.utf8
```

0. Modify the postgresql.conf file.

```
listen_addresses = '0.0.0.0' port = 3389 max_connections = 1500 superuser_reserved_connections = 13 unix_socket_directories = '., /var/run/postgresql, /tmp' tcp_keepalives_idle = 60 tcp_keepalives_interval = 10 tcp_keepalives_count = 10 sharedbuffers = 16GB
```

e splitting in ApsaraDB RDS for P ostgreSQL `_`

```
huge_pages = on work_mem = 8MB maintenance_work_mem = 1GB dynamic_shared_memory_type = posix vacuum_cost_delay = 0 bgwriter_delay = 10ms bgwriter_lru_maxpages = 1000 bgwriter_lru_multiplier = 10.0 bgwriter_flush_after = 512kB effective_io_concurrency = 0 max_worker_processes = 128 max_parallel_maintenance_workers = 3 max_parallel_workers_per_gather = 4 parallel_leader_participation = off max_parallel_workers = 8 backend_flush_after = 256 wal_level = replica synchronous_commit = off full_page_writes = on wal_compression = on wal_buffers = 16MB wal_writer_delay = 10ms wal_writer_flush_after = 1MB checkpoint_timeout = 15min max_wal_size = 64GB min_wal_size = 8GB checkpoint_completion_target = 0.2 checkpoint_flush_after = 256kB random_page_cost = 1.1 effective_cache_size = 48GB log_destination = 'csvlog' logging_collector = on log_directory = 'log' log_filename = 'postgresql-%a.log' log_truncate_on_rotation = on log_rotation_age = 1d log_rotation_size = 0 log_min_duration_statement = 1s log_checkpoints = on log_connections = on log_disconnections = on log_line_prefix = '%m [%p] ' log_statement = 'ddl' log_timezone = 'Asia/Shanghai' autovacuum = on log_autovacuum_min_duration = 0 autovacuum_vacuum_scale_factor = 0.1 autovacuum_analyze_scale_factor = 0.05 autovacuum_freeze_max_age = 800000000 autovacuum_multixact_freeze_max_age = 900000000 autovacuum_vacuum_cost_delay = 0 vacuum_freeze_table_age = 750000000 vacuum_multixact_freeze_table_age = 750000000 datestyle = 'iso, mdy'
```

e splitting in ApsaraDB RDS for P ostgreSQL

```
timezone = 'Asia/Shanghai' lc_messages = 'en_US.utf8' lc_monetary = 'en_US.utf8' lc_numeric = 'en_US.utf8' lc_time = 'en_US.utf8' default_text_search_config = 'pg_catalog.english'
```

1. Modify the pg_hba.conf file.

> **Note:** Pgpool-II is installed on the same ECS instance as the database server where PostgreSQL resides. If you specify the 127.0.0.1 IP address in the pg_hba.conf file, you must enter the correct password to ensure a successful logon.

```bash
# "local" is for Unix domain socket connections only
local all all trust
# IPv4 local connections:
host all all 127.0.0.1/32 md5
# IPv6 local connections:
host all all ::1/128 trust
# Allow replication connections from localhost, by a user with the
# replication privilege.
local replication all trust host replication all 127.0.0.1/32 trust host replication all ::1/128 trust host db123 digoal 0.0.0.0/0 md5
```

2. Execute a statement in the database to create a user authorized with streaming replication
permissions. Example:

```
create role rep123 login replication encrypted password 'xxxxxxx';
```

3. Execute statements in the database to create a user and authorize it to manage your
ApsaraDB RDS instances. Example:

```
create role digoal login encrypted password 'xxxxxxx'; create database db123 owner digoal;
```

4. Create a user who is authorized to check the health heartbeats between Pgpool and your
read-only ApsaraDB RDS instances. With the parameters of Pgpool properly configured, this user can check the write-ahead logging (WAL) replay latency on each read-only ApsaraDB RDS instance. Example:

```
create role nobody login encrypted password 'xxxxxxx';
```

**Create a secondary ApsaraDB RDS instance**

To simplify the test procedure, perform the following steps to create a secondary ApsaraDB RDS instance on the same ECS instance as your primary ApsaraDB RDS instance:
1. Use the pg_basebackup tool to create a secondary ApsaraDB RDS instance.

```
pg_basebackup -D /data01/pg12_8002/pg_root -F p --checkpoint=fast -P -h 127.0.0.1 -p 3389 -U rep123
```

2. Run the following commands to open the postgresql.conf file of the secondary ApsaraDB
RDS instance: e splitting in ApsaraDB RDS for P ostgreSQL

```
cd /data01/pg12_8002/pg_root vi postgresql.conf
```

Modify the following configurations:

```bash
# The secondary ApsaraDB RDS instance has the following configurations different from
the primary ApsaraDB RDS instance: port = 8002 primary_conninfo = 'hostaddr=127.0.0.1 port=3389 user=rep123' # You do not need to se t the password. This is because trust relationships are configured on the primary Aps araDB RDS instance. hot_standby = on wal_receiver_status_interval = 1s wal_receiver_timeout = 10s recovery_target_timeline = 'latest'
```

3. Configure the standby.signal file of the secondary ApsaraDB RDS instance.

```
cd /data01/pg12_8002/pg_root touch standby.signal
```

4. Execute the SELECT * FROM pg_stat_replication ; statement in the database to check
whether data is properly synchronized between the primary and secondary ApsaraDB RDS instances. The following output is returned:

```
-[ RECORD 1 ]----+-----------------------------pid | 21065 usesysid | 10 usename | postgres application_name | walreceiver client_addr | 127.0.0.1 client_hostname | client_port | 47064 backend_start | 2020-02-29 00:26:28.485427+08 backend_xmin | state | streaming sent_lsn | 0/52000060 write_lsn | 0/52000060 flush_lsn | 0/52000060 replay_lsn | 0/52000060 write_lag | flush_lag | replay_lag | sync_priority | 0 sync_state | async reply_time | 2020-02-29 01:32:40.635183+08
```

**Configure Pgpool**

1. Query the location where Pgpool is installed.
e splitting in ApsaraDB RDS for P ostgreSQL

```
rpm -qa|grep pgpool pgpool-II-12-extensions-4.1.1-1.rhel7.x86_64 pgpool-II-12-4.1.1-1.rhel7.x86_64 rpm -ql pgpool-II-12-4.1.1
```

2. Run the following commands to open the pgpool.conf file:

```
cd /etc/pgpool-II-12/ cp pgpool.conf.sample-stream pgpool.conf vi pgpool.conf
```

Modify the following configurations:

```bash
listen_addresses = '0.0.0.0' port = 8001 socket_dir = '/tmp' reserved_connections = 0 pcp_listen_addresses = '' pcp_port = 9898 pcp_socket_dir = '/tmp'
# - Backend Connection Settings -
backend_hostname0 = '127.0.0.1'
                                   # Host name or IP address to connect to for backend
backend_port0 = 3389
                                   # Port number for backend 0
backend_weight0 = 1
                                   # Weight for backend 0 (only in load balancing
mode) backend_data_directory0 = '/data01/pg12_3389/pg_root'
                                   # Data directory for backend 0
backend_flag0 = 'ALWAYS_MASTER'
                                   # Controls various backend behavior
                                   # ALLOW_TO_FAILOVER, DISALLOW_TO_FAILOVER
                                   # or ALWAYS_MASTER
backend_application_name0 = 'server0'
                                   # walsender's application_name, used for "show
pool_nodes" command backend_hostname1 = '127.0.0.1' backend_port1 = 8002 backend_weight1 = 1 backend_data_directory1 = '/data01/pg12_8002/pg_root' backend_flag1 = 'DISALLOW_TO_FAILOVER' backend_application_name1 = 'server1'
# - Authentication -
enable_pool_hba = on
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
                                   # Use pool_hba.conf for client authentication
pool_passwd = 'pool_passwd'
                                   # File name of pool_passwd for md5 authentication.
                                   # "" disables pool_passwd.
                                   # (change requires restart)
allow_clear_text_frontend_auth = off
                                   # Allow Pgpool-II to use clear text password
authentication
                                   # with clients, when pool_passwd does not
                                   # contain the user password
# - Concurrent session and pool size -
num_init_children = 128
                                   # Number of concurrent sessions allowed
                                   # (change requires restart)
max_pool = 4
                                   # Number of connection pool caches per connection
                                   # (change requires restart)
# - Life time -
child_life_time = 300
                                   # Pool exits after being idle for this many seconds
child_max_connections = 0
                                   # Pool exits after receiving that many connections
                                   # 0 means no exit
connection_life_time = 0
                                   # Connection to backend closes after being idle for
this many seconds
                                   # 0 means no close
client_idle_limit = 0
                                   # Client is disconnected after being idle for that
many seconds
                                   # (even inside an explicit transactions!)
                                   # 0 means no disconnection
#------------------------------------------------------------------------------
# LOGS
#------------------------------------------------------------------------------
# - Where to log -
log_destination = 'syslog'
                                   # Where to log
                                   # Valid values are combinations of stderr,
                                   # and syslog. Default to stderr.
log_connections = on
                                   # Log connections
log_standby_delay = 'if_over_threshold'
                                   # Log standby delay
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
                                   # Valid values are combinations of always,
                                   # if_over_threshold, none
#------------------------------------------------------------------------------
# FILE LOCATIONS
#------------------------------------------------------------------------------
pid_file_name = '/var/run/pgpool-II-12/pgpool.pid'
                                   # PID file name
                                   # Can be specified as relative to the"
                                   # location of pgpool.conf file or
                                   # as an absolute path
                                   # (change requires restart)
logdir = '/tmp'
                                   # Directory of pgPool status file
                                   # (change requires restart)
#------------------------------------------------------------------------------
# CONNECTION POOLING
#------------------------------------------------------------------------------
connection_cache = on
                                   # Activate connection pools
                                   # (change requires restart)
                                   # Semicolon separated list of queries
                                   # to be issued at the end of a session
                                   # The default is for 8.3 and later
reset_query_list = 'ABORT; DISCARD ALL'
#------------------------------------------------------------------------------
# LOAD BALANCING MODE
#------------------------------------------------------------------------------
load_balance_mode = on
                                   # Activate load balancing mode
                                   # (change requires restart)
ignore_leading_white_space = on
                                   # Ignore leading white spaces of each query
white_function_list = ''
                                   # Comma separated list of function names
                                   # that don't write to database
                                   # Regexp are accepted
black_function_list = 'currval,lastval,nextval,setval'
                                   # Comma separated list of function names
                                   # that write to database
                                   # Regexp are accepted
black_query_pattern_list = ''
                                   # Semicolon separated list of query patterns
                                   # that should be sent to primary node
                                   # Regexp are accepted
                                   # valid for streaming replicaton mode only.
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
database_redirect_preference_list = ''
                                   # comma separated list of pairs of database and
node id.
                                   # example: postgres:primary,mydb[0-4]:1,mydb[5-
9]:2'
                                   # valid for streaming replicaton mode only.
app_name_redirect_preference_list = ''
                                   # comma separated list of pairs of app name and
node id.
                                   # example: 'psql:primary,myapp[0-4]:1,myapp[5-
9]:standby'
                                   # valid for streaming replicaton mode only.
allow_sql_comments = off
                                   # if on, ignore SQL comments when judging if load b
alance or
                                   # query cache is possible.
                                   # If off, SQL comments effectively prevent the
judgment
                                   # (pre 3.4 behavior).
disable_load_balance_on_write = 'transaction'
                                   # Load balance behavior when write query is issued
                                   # in an explicit transaction.
                                   # Note that any query not in an explicit
transaction
                                   # is not affected by the parameter.
                                   # 'transaction' (the default): if a write query is i
ssued,
                                   # subsequent read queries will not be load balanced
                                   # until the transaction ends.
                                   # 'trans_transaction': if a write query is issued,
                                   # subsequent read queries in an explicit
transaction
                                   # will not be load balanced until the session ends.
                                   # 'always': if a write query is issued, read queries
will
                                   # not be load balanced until the session ends.
statement_level_load_balance = off
                                   # Enables statement level load balancing
#------------------------------------------------------------------------------
# MASTER/SLAVE MODE
#------------------------------------------------------------------------------
master_slave_mode = on
                                   # Activate master/slave mode
                                   # (change requires restart)
master_slave_sub_mode = 'stream'
                                   # Master/slave sub mode
                                   # Valid values are combinations stream, slony
                                   # or logical. Default is stream.
                                   # (change requires restart)
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
# - Streaming -
sr_check_period = 3
                                   # Streaming replication check period
                                   # Disabled (0) by default
sr_check_user = 'nobody'
                                   # Streaming replication check user
                                   # This is neccessary even if you disable streaming
                                   # replication delay check by sr_check_period = 0
sr_check_password = ''
                                   # Password for streaming replication check user
                                   # Leaving it empty will make Pgpool-II to first look
for the
                                   # Password in pool_passwd file before using the
empty password sr_check_database = 'postgres'
                                   # Database name for streaming replication check
delay_threshold = 512000
                                   # Threshold before not dispatching query to standby
node
                                   # Unit is in bytes
                                   # Disabled (0) by default
#------------------------------------------------------------------------------
# HEALTH CHECK GLOBAL PARAMETERS
#------------------------------------------------------------------------------
health_check_period = 5
                                   # Health check period
                                   # Disabled (0) by default
health_check_timeout = 10
                                   # Health check timeout
                                   # 0 means no timeout
health_check_user = 'nobody'
                                   # Health check user
health_check_password = ''
                                   # Password for health check user
                                   # Leaving it empty will make Pgpool-II to first look
for the
                                   # Password in pool_passwd file before using the
empty password health_check_database = ''
                                   # Database name for health check. If '', tries
'postgres' frist, health_check_max_retries = 60
                                   # Maximum number of times to retry a failed health
check before giving up. health_check_retry_delay = 1
                                   # Amount of time to wait (in seconds) between
retries. connecttimeout=10000
```

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
connect_timeout = 10000
                                   # Timeout value in milliseconds before giving up to
connect to backend.
                                   # Default is 10000 ms (10 second). Flaky network
user may want to increase
                                   # the value. 0 means no timeout.
                                   # Note that this value is not only used for health
check,
                                   # but also for ordinary conection to backend.
#------------------------------------------------------------------------------
# FAILOVER AND FAILBACK
#------------------------------------------------------------------------------
failover_on_backend_error = off
                                   # Initiates failover when reading/writing to the
                                   # backend communication socket fails
                                   # If set to off, pgpool will report an
                                   # error and disconnect the session.
relcache_expire = 0 # After the configuration file is restructured, we recommend tha t you set this parameter to 1, reload the configuration file, and then set this param eter to 0 again. You can also set this parameter to a specific point in time.
                                   # Life time of relation cache in seconds.
                                   # 0 means no cache expiration(the default).
                                   # The relation cache is used for cache the
                                   # query result against PostgreSQL system
                                   # catalog to obtain various information
                                   # including table structures or if it's a
                                   # temporary table or not. The cache is
                                   # maintained in a pgpool child local memory
                                   # and being kept as long as it survives.
                                   # If someone modify the table by using
                                   # ALTER TABLE or some such, the relcache is
                                   # not consistent anymore.
                                   # For this purpose, cache_expiration
                                   # controls the life time of the cache.
relcache_size = 8192
                                   # Number of relation cache
                                   # entry. If you see frequently:
                                   # "pool_search_relcache: cache replacement happend"
                                   # in the pgpool log, you might want to increate
this number.
```

3. Run the `cd /etc/pgpool-II-12` command to configure the pool_passwd file.

> **Note:** If you connect to your ApsaraDB RDS instances by using Pgpool, you must configure the pool_passwd file. This is because Pgpool supports the authentication protocol of PostgreSQL.

e splitting in ApsaraDB RDS for P ostgreSQL

```bash
# Run the following command:
#pg_md5 --md5auth --username=username password
# Generate the passwords of the digoal and nobody users. The passwords are automatica
lly written into the pool_passwd file. pg_md5 --md5auth --username=digoal "xxxxxxx" pg_md5 --md5auth --username=nobody "xxxxxxx"
```

4. Use the system to automatically generate the pool_passwd file.

```
cd /etc/pgpool-II-12 cat pool_passwd
```

5. Run the following commands to configure the pgpool_hba file:

```
cd /etc/pgpool-II-12 cp pool_hba.conf.sample pool_hba.conf vi pool_hba.conf
```

Configure the following parameters:

```
host all all 0.0.0.0/0 md5
```

6. Configure the pcp.conf file.

> **Note:** The pcp.conf file is used to manage the users and passwords of Pgpool. It is not related to the users and passwords of your ApsaraDB RDS instances.

```bash
cd /etc/pgpool-II-12
# pg_md5 abc  # In this command, you set the password to abc and encrypt it by using
the MD5 encryption algorithm. 900150983cd24fb0d6963f7d28e17f72 cp pcp.conf.sample pcp.conf vi pcp.conf
# USERID:MD5PASSWD
manage:900150983cd24fb0d6963f7d28e17f72 # In this command, the manage user is used t o manage PCP.
```

7. Start Pgpool.

```
cd /etc/pgpool-II-12 pgpool -f ./pgpool.conf -a ./pool_hba.conf -F ./pcp.conf
```

> **Note:** If you want to view the logs of Pgpool, run the following command:

```
less /var/log/messages
```

8. Use Pgpool to connect to your ApsaraDB RDS instances.

```
psql -h 127.0.0.1 -p 8001 -U digoal postgres
```

e splitting in ApsaraDB RDS for P ostgreSQL

**FAQ**

Q: How do I test whether read/write splitting is enabled? A: You can connect to your ApsaraDB RDS instances by using Pgpool and call the pg_is_in_recovery() function. Then, close the connection, establish a connection again, and call the pg_is_in_recovery() function again. If you receive a value of false and then a value of true, Pgpool routes requests to your primary ApsaraDB RDS instance and then to your read-only ApsaraDB RDS instances, and read/write splitting is enabled. Q: Does Pgpool increase the latency? A: Pgpool increases the latency slightly. In the test environment you set up in this topic, the latency increases by about 0.12 milliseconds. Q: How does Pgpool check the latency and health on my read-only ApsaraDB RDS instances? A: If the WAL replay latency on a read-only ApsaraDB RDS instance exceeds the specified limit, Pgpool stops routing SQL requests to the read-only instance. Pgpool resumes routing SQL requests to the read-only instance only after it detects that the WAL replay latency on the read-only instance falls below the specified limit.

> **Note:** Connect to your primary ApsaraDB RDS instance and query the location where the current WAL data record is written. This location is referred to as log sequence number (LSN) 1. Then, connect to a read-only ApsaraDB RDS instance and query the location where the current WAL data record is replayed. This location is referred to as LSN 2. You can obtain the number of bytes between LSN 1 and LSN 2. This number indicates the latency.

Pgpool monitors the health of your read-only ApsaraDB RDS instances. If a read-only instance is unhealthy, Pgpool stops routing requests to the read-only instance. Q: How do I stop Pgpool and reload the configuration of Pgpool? A: Run the `pgpool --help` command to obtain more information about the commands used in Pgpool. Example:

```
cd /etc/pgpool-II-12 pgpool -f ./pgpool.conf -m fast stop
```

Q: How do I configure Pgpool if more than one read-only ApsaraDB RDS instance is attached to my primary ApsaraDB RDS instance? A: Add the configurations of all the attached read-only ApsaraDB RDS instances to the pgpool.conf file. Example: e splitting in ApsaraDB RDS for P ostgreSQL

```
backend_hostname1 = 'xx.xx.xxx.xx' backend_port1 = 8002 backend_weight1 = 1 backend_data_directory1 = '/data01/pg12_8002/pg_root' backend_flag1 = 'DISALLOW_TO_FAILOVER' backend_application_name1 = 'server1' backend_hostname2 = 'xx.xx.xx.xx' backend_port1 = 8002 backend_weight1 = 1 backend_data_directory1 = '/data01/pg12_8002/pg_root' backend_flag1 = 'DISALLOW_TO_FAILOVER' backend_application_name1 = 'server1'
```

Q: How do I use pcp commands to view the status of my read-only ApsaraDB RDS instances? A: To obtain the status of your read-only ApsaraDB RDS instances by using pcp commands, run the following command:

```
pcp_node_info -U manage -h /tmp -p 9898 -n 1 -v Password: # Enter the password. Hostname : 127.0.0.1 Port : 8002 Status : 2 Weight : 0.500000 Status Name : up Role : standby Replication Delay : 0 Replication State : Replication Sync State : Last Status Change : 2020-02-29 00:20:29
```

Q: Which listening ports are used by Pgpool for read/write splitting? A: The following listening ports are used by Pgpool for read/write splitting: Primary ApsaraDB RDS instance: Port 3389 Secondary ApsaraDB RDS instance: Port 8002 Pgpool: Port 8001 PCP: Port 9898 develop ApsaraDB RDS for Postgr eSQL

## 20 Use ShardingSphere to develop ApsaraDB RDS for PostgreSQL

**develop ApsaraDB RDS for**

**PostgreSQL**

ShardingSphere is an open source ecosystem that consists of a set of distributed database middleware solutions.

**Prerequisites**

All PostgreSQL versions that are used with ApsaraDB RDS support ShardingSphere.

**Background information**

ApsaraDB RDS for PostgreSQL supports database-integrated sharding plug-ins (such as Citus, Postgres-XC, and AntDB) and massively parallel processing (MPP) products. It also supports sharding middleware products that are similar to those widely used in MySQL, such as ShardingSphere. ShardingSphere is suitable for services that run in databases with thorough, well-organized logical sharding. ShardingSphere provides the following features: Data sharding Database sharding and table sharding Read/write splitting Sharding strategy customization Decentralized distributed primary key Distributed transaction Unified transaction API XA transaction BASE transaction Database orchestration Dynamic configuration Orchestration and governance Data encryption Tracing and observability Elastic scaling out (planning) For more information, see the ShardingSphere documentation.

**ShardingSphere products**

ShardingSphere includes three independent products. You can choose the product that best suits your business requirements. The following table describes these products.

| Parameter | Sharding-JDBC | Sharding-Proxy | Sharding-Sidecar |
|---|---|---|---|
| Supported database engine | All JDBC-compatible database engines such as MySQL, PostgreSQL, Oracle, and SQL Server | MySQL and PostgreSQL | MySQL and PostgreSQL |

develop ApsaraDB RDS for Postgr eSQL

| Connections consumed | High | Low | High |
|---|---|---|---|
| Supported heterogeneous language | Java | All | All |
| Performance | Low overheads | Moderate overheads | Low overheads |
| Decentralized | Yes | No | Yes |
| Stateless API | No | Yes | No |

**Prepare configuration templates**

1. On your Elastic Compute Service (ECS) instance, run the following command to go to the
directory where configuration templates are stored. The directory is under the root directory in this example.

```
cd /root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-bin/conf
```

2. Run the `ll` command to view all files stored in the directory. Sample output:

```
total 24 -rw-r--r-- 1 501 games 3019 Jul 30 2019 config-encrypt.yaml -rw-r--r-- 1 501 games 3582 Apr 22 2019 config-master_slave.yaml -rw-r--r-- 1 501 games 4278 Apr 22 2019 config-sharding.yaml -rw-r--r-- 1 501 games 1918 Jul 30 2019 server.yaml
```

> **Note:** config-encrypt.yaml: the data encryption configuration file.
> config-master_slave.yaml: the read/write splitting configuration file.
> config-sharding.yaml: the data sharding configuration file.
> server.yaml: the common configuration file.

3. Modify the configuration files.

> **Note:** For more information about the configuration files, see ShardingSphere documentation. In this example, the data sharding and common configuration files are used.
> Example of a data sharding configuration file:

develop ApsaraDB RDS for Postgr eSQL

```xml
schemaName: # The name of the logical data source. dataSources: # The configuration of the data source. You can configure more than one data source by using the data_source_name variable.
  <data_source_name>: #You do not need to configure a database connection p
ool. This is different in Sharding-JDBC.
    url: # The URL used to connect to your database.
    username: # The username used to log on to the database.
    password: # The password used to log on to the database.
    connectionTimeoutMilliseconds: 30000 # The connection timeout period in
milliseconds.
    idleTimeoutMilliseconds: 60000 # The idle-connection reclaiming timeout
period in milliseconds.
    maxLifetimeMilliseconds: 1800000 # The maximum connection time to live
(TTL) in milliseconds.
    maxPoolSize: 65 # The maximum number of connections allowed.
shardingRule: # You do not need to configure a sharding rule, because it is the same in Sharding-JDBC.
```

> Example of a common configuration file:

develop ApsaraDB RDS for Postgr eSQL

```bash
Proxy properties
# You do not need to configure the proxy properties that you can find in Sh
arding-JDBC. props:
  acceptor.size: # The number of worker threads that receive requests from
the client. The default number is equal to the number of CPU cores multipli ed by 2.
  proxy.transaction.type: # The type of transaction processed by the proxy.
Valid values: LOCAL | XA | BASE. Default value: LOCAL. Value XA specifies t o use Atomikos as the transaction manager. Value BASE specifies to copy the .jar package that implements the ShardingTransactionManager operation to th e lib directory.
  proxy.opentracing.enabled: # Specifies whether to enable link tracing. Li
nk tracing is disabled by default.
  check.table.metadata.enabled: # Specifies whether to check the consistenc
y of metadata among sharding tables during startup. Default value: false.
  proxy.frontend.flush.threshold: # The number of packets returned in a bat
ch during a complex query. Permission verification This part of the configuration is used to verify your permissions when you attempt to log on to Sharding-Proxy. After you configure the username, pass word, and authorized databases, you must use the correct username and passw ord to log on to Sharding-Proxy from the authorized databases. authentication:
  users:
    root: # The username of the root user.
      password: root# The password of the root user.
    sharding: # The username of the sharding user.
      password: sharding# The password of the sharding user.
      authorizedSchemas: sharding_db, masterslave_db # The databases on whi
ch the specified user has permissions. If you want to specify more than one database, separate them with commas (,). You are granted the permissions of the root user by default. This means that you can access all databases.
```

**Set up a test environment**

On your ECS instance, install Java.

```bash
yum install -y java
```

Configure an ApsaraDB RDS instance that runs PostgreSQL 10. Create an account with username r1. Set the password of the account to "PW123321!". Create the following databases whose owners are user r1: db0, db1, db2, and db3. Add the IP address of your ECS instance to an IP address whitelist of the RDS instance. develop ApsaraDB RDS for Postgr eSQL

| Note For more information about how to create an ApsaraDB RDS for PostgreSQL instance, database, and account, see Create an instance and Create a database and an account. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist. |   |
|---|---|

```
Run vi /root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-
```

`bin/conf/server.yaml` to configure the following common configuration file:

```
  authentication:
  users:
    r1:
      password: PW123321!
      authorizedSchemas: db0,db1,db2,db3
props:
  executor.size: 16
  sql.show: false
```

**Test horizontal sharding**

```
1. Run  vi /root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-bin/conf/config-
```

`sharding.yaml` to modify the following data sharding configuration file:

```
schemaName: sdb dataSources:
  db0:
    url: jdbc:postgresql://pgm-bpxxxxx.pg.rds.aliyuncs.com:1433/db0
    username: r1
    password: PW123321!
    connectionTimeoutMilliseconds: 30000
    idleTimeoutMilliseconds: 60000
    maxLifetimeMilliseconds: 1800000
    maxPoolSize: 65
  db1:
    url: jdbc:postgresql://pgm-bpxxxxx.pg.rds.aliyuncs.com:1433/db1
    username: r1
    password: PW123321!
    connectionTimeoutMilliseconds: 30000
    idleTimeoutMilliseconds: 60000
    maxLifetimeMilliseconds: 1800000
    maxPoolSize: 65
  db2:
    url: jdbc:postgresql://pgm-bpxxxxx.pg.rds.aliyuncs.com:1433/db2
    username: r1
    password: PW123321!
    connectionTimeoutMilliseconds: 30000
    idleTimeoutMilliseconds: 60000
    maxLifetimeMilliseconds: 1800000
    maxPoolSize: 65
  db3:
    url: jdbc:postgresql://pgm-bpxxxxx.pg.rds.aliyuncs.com:1433/db3
    username: r1
```

develop ApsaraDB RDS for Postgr eSQL

```
    password: PW123321!
    connectionTimeoutMilliseconds: 30000
    idleTimeoutMilliseconds: 60000
    maxLifetimeMilliseconds: 1800000
    maxPoolSize: 65
shardingRule:
  tables:
    t_order:
      actualDataNodes: db${0..3}.t_order${0..7}
      databaseStrategy:
        inline:
          shardingColumn: user_id
          algorithmExpression: db${user_id % 4}
      tableStrategy:
        inline:
          shardingColumn: order_id
          algorithmExpression: t_order${order_id % 8}
      keyGenerator:
        type: SNOWFLAKE
        column: order_id
    t_order_item:
      actualDataNodes: db${0..3}.t_order_item${0..7}
      databaseStrategy:
        inline:
          shardingColumn: user_id
          algorithmExpression: db${user_id % 4}
      tableStrategy:
        inline:
          shardingColumn: order_id
          algorithmExpression: t_order_item${order_id % 8}
      keyGenerator:
        type: SNOWFLAKE
        column: order_item_id
  bindingTables:
    - t_order,t_order_item
  defaultTableStrategy:
    none:
```

2. Start ShardingSphere and listen to Port 8001.

```
cd /root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-bin/bin/ ./start.sh 8001
```

3. Connect to the destination database

```
psql -h 127.0.0.1 -p 8001 -U r1 sdb
```

4. Create a table.

```
create table t_order(order_id int8 primary key, user_id int8, info text, c1 int, crt_ time timestamp); create table t_order_item(order_item_id int8 primary key, order_id int8, user_id int8 , info text, c1 int, c2 int, c3 int, c4 int, c5 int, crt_time timestamp);
```

develop ApsaraDB RDS for Postgr eSQL

> **Note:** When you create a table, the system automatically creates horizontal shards in the specific database based on the sharding strategy that you specify.

**FAQ**

If you want to view the SQL parsing and routing statements used in ShardingSphere, run

```
 vi /root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-bin/conf/server.yaml .
  authentication:
  users:
    r1:
      password: PW123321!
      authorizedSchemas: db0,db1,db2,db3
props:
  executor.size: 16
  sql.show: true # Specifies to log parsed SQL statements.
```

If you want to test writes and queries, run the following commands:

```
insert into t_order (user_id, info, c1, crt_time) values (0,'a',1,now()); insert into t_order (user_id, info, c1, crt_time) values (1,'b',2,now()); insert into t_order (user_id, info, c1, crt_time) values (2,'c',3,now()); insert into t_order (user_id, info, c1, crt_time) values (3,'c',4,now()); select * from t_order;
```

The following result is returned in this example:

```
      order_id      | user_id | info | c1 |          crt_time
--------------------+---------+------+----+----------------------------
 433352561047633921 |       0 | a    |  1 | 2020-02-09 19:48:21.856555
 433352585668198400 |       1 | b    |  2 | 2020-02-09 19:48:27.726815
 433352610813050881 |       2 | c    |  3 | 2020-02-09 19:48:33.721754
 433352628370407424 |       3 | c    |  4 | 2020-02-09 19:48:37.907683
(4 rows)
```

If you want to view ShardingSphere logs, go to the following path:

```
/root/apache-shardingsphere-incubating-4.0.0-sharding-proxy-bin/logs/stdout.log
```

If you want to use pgbench for stress testing, run the following commands: develop ApsaraDB RDS for Postgr eSQL

```
vi test.sql \set user_id random(1,100000000) \set order_id random(1,2000000000) \set order_item_id random(1,2000000000) insert into t_order (user_id, order_id, info, c1 , crt_time) values (:user_id, :order _id,random()::text, random()*1000, now()) on conflict (order_id) do update set info=e xcluded.info,c1=excluded.c1,crt_time=excluded.crt_time; insert into t_order_item (order_item_id, user_id, order_id, info, c1,c2,c3,c4,c5,crt_time) values (:order_item_id, :user_id,:order_id,random()::text, r andom()*1000,random()*1000,random()*1000,random()*1000,random()*1000, now()) on confl ict(order_item_id) do nothing; pgbench -M simple -n -r -P 1 -f ./test.sql -c 24 -j 24 -h 127.0.0.1 -p 8001 -U r1 sd b -T 120 progress: 1.0 s, 1100.9 tps, lat 21.266 ms stddev 6.349 progress: 2.0 s, 1253.0 tps, lat 18.779 ms stddev 7.913 progress: 3.0 s, 1219.0 tps, lat 20.083 ms stddev 13.212
```
