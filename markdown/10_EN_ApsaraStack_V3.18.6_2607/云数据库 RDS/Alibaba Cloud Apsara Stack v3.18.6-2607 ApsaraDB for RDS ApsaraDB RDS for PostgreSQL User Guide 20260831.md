---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 164
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20RDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20RDS%20ApsaraDB%20RDS%20for%20PostgreSQL%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for PostgreSQL User Guide 20260831

## Console release notes

This topic describes new features and important updates for the RDS PostgreSQL console.

**v3.18.6sp-2607**

| Feature | Description | References |
|---|---|---|
| Configuration overview for instance creation | During instance creation, a configuration overview panel appears on the right after you enter all required parameters. This panel lets you review the instance's overall configuration and ensure it meets your requirements. | Create Instance |

## What is ApsaraDB RDS?

ApsaraDB RDS is a stable, reliable, and scalable online database service that is built on top of Apsara Distributed File System and high-performance storage. It provides a comprehensive portfolio of solutions for disaster recovery, backup, restoration, monitoring, and migration to facilitate database O&M. ApsaraDB RDS supports four database engines: MySQL, SQL Server, PolarDB, and PostgreSQL. You can create database instances based on these database engines to meet your business requirements. This topic describes the PostgreSQL engine.

**ApsaraDB RDS for PostgreSQL**

ApsaraDB RDS for PostgreSQL is an advanced database service that is fully compatible with SQL syntax and supports a diverse range of data such as JSON, IP, and geometric data. It supports SQL:2003 and later, as well as procedural SQL languages such as PL/pgSQL and PL/Java. It also supports Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC). In addition to features such as transactions, subqueries, multi-version concurrency control (MVCC), and data integrity check, ApsaraDB RDS for PostgreSQL integrates a series of features including high availability, backup, and restoration to ease O&M loads. for PostgreSQL

## Limits on ApsaraDB RDS for

**PostgreSQL**

Before you use ApsaraDB RDS for PostgreSQL, you must understand its limits and take the necessary precautions. The following table describes the limits on ApsaraDB RDS for PostgreSQL.

| Operation | Limit |
|---|---|
| Root permissions of databases | Superuser permissions are not provided. |
| Database replication | ApsaraDB RDS for PostgreSQL provides a primary/secondary replication architecture except in the Basic Edition. The secondary instances in the architecture are hidden and cannot be accessed by your applications. |
| Instance restart | Instances must be restarted by using the ApsaraDB RDS console or API operations. |

DB RDS instances that run Postgr eSQL 9.4 and PostgreSQL 10 are no longer available for purchase i n Apsara Stack V3.18

**4.[Announcement] ApsaraDB**

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

## Instance types

This topic describes the instance types of ApsaraDB RDS for PostgreSQL. Different instance types deliver different performance.

**IOPS**

The maximum IOPS of an ApsaraDB RDS instance that uses local SSDs varies based on the instance type. The maximum IOPS of an ApsaraDB RDS instance that uses cloud disks varies based on the instance type and storage capacity. The following formula can be used to calculate the IOPS of an ApsaraDB RDS instance that uses cloud disks. The storage capacity is measured in GB.

```
min{1800 + 30 × Storage capacity, 25000}
```

If the throughput of an RDS instance reaches the upper limit, the IOPS of the instance also decreases.

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

| psaraDB RDS fo r Guide·Instance |   |   |   |   |   |
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

## Log on to the ApsaraDB

**RDS console**

This topic describes how to log on to the ApsaraDB RDS console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.

**Procedure**

1. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
2. Click **Log On**.
3. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**. For more information, see the **Bind a virtual MFA device to enable**
**MFA** topic in **Apsara Uni-manager Management Console User Guide** .
4. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**.

## Quick Start

### Procedure

ApsaraDB RDS quick start covers the following topics: creating an ApsaraDB RDS instance, configuring a whitelist, creating a database, creating an account, and connecting to the instance.

**Flowchart for an ApsaraDB RDS instance**

If you are using ApsaraDB RDS for the first time, you can start with Limits on ApsaraDB RDS for PostgreSQL. The following figure shows the operations that you must perform before you use an ApsaraDB RDS instance.

### Create an instance

This topic describes how to create an ApsaraDB RDS for PostgreSQL instance in the ApsaraDB RDS console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
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

| Specificat |   |   |
|---|---|---|
|   | Storage Type | The storage type of the instance. Local SSDs and standard SSDs are supported. The storage types that are supported vary based on the engine version: PostgreSQL 11.0: Local SSDs and standard SSDs are supported. PostgreSQL 12.0: Local SSDs and standard SSDs are supported. PostgreSQL 13.0: Local SSDs and standard SSDs are supported. |
| ions |   |   |
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

### Configure an IP address

**whitelist**

This topic describes how to configure a whitelist for an ApsaraDB RDS instance. Only entities that are listed in a whitelist can access your ApsaraDB RDS instance.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure and do not interrupt the operations of your ApsaraDB RDS instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance. The IP address whitelist labeled default contains only the default IP address 0.0.0.0/0, which allows all entities to access your ApsaraDB RDS instance. Configure an ECS security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.
You can also click **Create Whitelist** to create a whitelist.
6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks used to access the
instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your ApsaraDB RDS instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Alibaba Cloud account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### Create a database and an

**account**

Before you start to use ApsaraDB RDS, you must create databases and accounts on an ApsaraDB RDS instance. This topic describes how to create a database and an account on an ApsaraDB RDS for PostgreSQL instance.

**Account types**

ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. The following table describes these types of accounts.

| Account type | Description |
|---|---|

| Privileged account | You can create and manage privileged accounts in the ApsaraDB RDS console or by calling API operations. You can create multiple privileged accounts for each RDS instance. The privileged accounts of an RDS instance have the permissions to manage all standard accounts and databases that are created on the instance. A privileged account allows you to manage permissions at fine-grained levels based on your business requirements. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect all standard accounts of the RDS instance on which the privileged account is created. |
|---|---|
| Standard account | You can create and manage standard accounts in the ApsaraDB RDS console, by using the ApsaraDB RDS API, or by executing SQL statements. You can create multiple standard accounts for each RDS instance. You must grant the permissions on specific databases to standard accounts. You cannot use a standard account to create or manage other accounts, or close connections that are established by using other accounts. |

**Usage notes**

You can create multiple privileged accounts and standard accounts in the ApsaraDB RDS console. You can also create and manage standard accounts by using SQL statements. Privileged accounts created on an instance that uses local SSDs cannot be deleted. Before you migrate data from an on-premises database to an RDS instance, you need to create a database and an account on the RDS instance. Make sure that the created database has the same properties as the on-premises database. In addition, make sure that the created account has the same permissions on the created database as the account that is authorized to manage the on-premises database. We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple databases and accounts and grant each account only the permissions to access specified databases. This way, you can implement fine-grained access control. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for accounts and change the passwords on a regular basis.

**Create a privileged account or a standard account**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Account Management**.
5. On the Accounts page, click **Create Account** and configure the following parameters.

| Parameter | Description |
|---|---|
| Database Account | The username of the account. It must be 2 to 63 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a letter and end with a letter or a digit. It cannot be the same as the username of an existing account. It cannot start with pg. It cannot contain SQL keywords. For more information, see SQL keywords. |
| Account Type | ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. A privileged account has all operation permissions on all databases. Standard accounts have all operation permissions only on their authorized databases. Note The permitted operations include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER. |
| New Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ |
| Confirm Password | Enter the password of the account again. |
| Description | This parameter is available only if the instance uses standard SSDs. It is an optional parameter. You can enter description to make the account easier to identify. The description can be up to 256 characters in length. |

6. Click **OK**.

**Create a database and a standard account**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the upper-right corner of the page, click **Log On to Database**.
5. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
**Database Type**, **Instance Region**, and **Connection String Address**. If the values are
correct, specify the **Database Account** and **Database Password** parameters.

| Parameter | Description |
|---|---|
| Database Type | The engine of the database. By default, the engine of the database to be connected is selected. |
| Instance Region | The region where the instance is deployed. By default, the region of the current instance is selected. |
| Connection String Address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The username of the database account. |
| Database Password | The password of the database account. |

6. Click **Login**. If you want the browser to save the password, select **Remember password**
before you click **Login**. If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
7. The **SQLConsole** page appears after you log in to the instance. Execute a statement in the
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

### Connect to an ApsaraDB RDS

**for PostgreSQL instance**

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an RDS instance. DMS is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational databases, such as MySQL, SQL Server, PostgreSQL, MongoDB, and Redis databases. DMS can also be used to manage NoSQL databases and Linux-based database servers. You can also use a database client to connect to an RDS instance. ApsaraDB RDS is fully compatible with open source database engines. Therefore, you can connect these two types of databases in the same way. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Use DMS to log on to an ApsaraDB RDS instance.

**Use the pgAdmin 4 client to connect to an instance**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.
For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows). In this example, pgAdmin 4 v6.15 is downloaded.
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

**Important**

The postgres database is the default system database. Do not perform operations on the postgres database.

## Instances

### Create an instance

This topic describes how to create an ApsaraDB for RDS for PostgreSQL instance in the console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click **Create Instance**.
3. Configure the following parameters.

| Category | Paramete r | Description |
|---|---|---|
| Basic configura tions | Organizat ion | The organization that owns the instance. |
|   | Resource Group | The resource group for the instance. |
| Region and zone | Region | The region where the instance will be created. You cannot change the region after creation. Instances in different regions cannot communicate over the internal network. |
|   | Primary Availabili ty Zone | The availability zone for the primary node of the instance. |
|   | Deploym ent Mode | ApsaraDB for RDS supports multi-AZ deployment and single-AZ deployment. The deployment mode is automatically selected based on your choice of Primary Availability Zone. |
|   | Database Engine | The database engine. Select PostgreSQL. |
|   | Database Version | The database version. Versions 11.0, 12.0, and 13.0 are supported. |
|   | Edition | For ApsaraDB for RDS for PostgreSQL, only the High-availability Edition is available. |

|   | Storage Type | The instance storage type. Supports local SSDs and SSD cloud disks. The following storage types are supported for each database version: 11.0: local SSD and SSD cloud disk 12.0: local SSD and SSD cloud disk 13.0: local SSD and SSD cloud disk |
|---|---|---|
| Instance configura tions |   |   |
|   | Enable Encryptio n | Enables encryption for the SSD cloud disk. This option is available only when you select SSD cloud disk for the Storage Type parameter. If enabled, you must also select an Encryption Key. If you do not have a key, create one in Key Management Service. For more information, see the Create a key section in the Key Management Service User Guide. |
|   | Encryptio n Key | Select an Encryption Key for the current SSD cloud disk. This parameter is available only when the Encryption parameter is enabled. |
|   | Instance Class | The instance class, which determines its memory size, maximum connections, and IOPS. The exact values are displayed in the console. For more information, see Instance classes. For a recommendation, click AI-Powered Specification Recommendation and describe your use case to Apsara AI Assistant. |
|   | Storage Space | The storage capacity, which includes space for data, system files, binary log files, and transaction files. Valid values range from 20 GB to 6,000 GB, in 5 GB increments. |
|   | Connecti on Type | ApsaraDB for RDS provides the following two types of connection endpoints: Public connection: Use this endpoint to access the database from the internet. Internal connection: Use this endpoint to access the database from the internal network. Important This setting cannot be changed after the instance is created. Choose with caution. |

| Network |   |   |
|---|---|---|
|   | Network Type | Supported network types for ApsaraDB for RDS instances: Classic Network: Services in a classic network are not isolated at the network layer. Access control relies on security groups and IP address whitelists. Virtual Private Cloud (VPC): A VPC provides an isolated network environment where you can define custom route tables, IP address ranges, and gateways. We recommend using a VPC for better security. Note For a multi-AZ deployment, you must have a VSwitch in both the primary and secondary availability zones of the selected VPC. After you select VPC as the network type, you must select the corresponding VPC and VSwitch. |
|   | VPC | These parameters are required only when the Network Type is set to Virtual Private Cloud (VPC). |
|   | VSwitch Availabili ty Zone |   |
|   | VSwitch |   |
|   | IP Address Whitelist | Enter the IP addresses or CIDR blocks that are allowed to access this instance. |
| Instance settings | Number of Instances | The number of instances to create. You can create multiple instances at once. The default value is 1. |
|   | Instance Name | The name of the RDS instance. The name must meet the following requirements: Must be 2 to 64 characters in length. Must start with a letter or a Chinese character. Can contain digits, hyphens (-), underscores ( ), and colons (:). _ Cannot start with http:// or https://. |

4. Review the configuration in the **Configuration Overview** panel on the right to ensure all
settings are correct. If you have insufficient quota, click **Quota Management** to request an increase. For more information, see the **Quota Management** section in the **Unified Cloud Management**
**Platform User Guide**.
5. When you have finished configuring the parameters, click **Submit**.

### View basic information of an

**instance**

This topic describes how to view the details of an ApsaraDB RDS instance, such as its basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. Use one of the following methods to go to the **Basic Information** page of an instance:
On the **Instances** page, click the ID of the instance to go to the **Basic Information** page. On the **Instances** page, find the instance and click **Manage** in the **Actions** column to go to the **Basic Information** page.

### Restart an instance

This topic describes how to manually restart an ApsaraDB RDS instance. This applies if the number of connections exceeds the specified threshold or if an instance has performance issues.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the upper-right corner of the page, click **Restart Instance**.
When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.
5. In the message that appears, click **Confirm**.

### Change the specifications of

**an instance**

This topic describes how to change the specifications of an ApsaraDB RDS instance. You can upgrade or downgrade an ApsaraDB RDS instance to meet your business needs.

**Prerequisites**

The instance is in the **Running** state and is not in the backing up or restoring state.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the **Configure Information** section of the **Basic Information** page, click **Change**
**Specifications**.
5. On the **Change Specifications** page, set **Edition**, **Instance Type**, and **Storage**
**Capacity**.
6. Click **Submit**.

### Set a maintenance window

This topic describes how to set a maintenance window for an ApsaraDB RDS instance.

**Background information**

To ensure the stability of ApsaraDB RDS instances, the backend system performs maintenance on the instances at irregular intervals. The default maintenance window is from 02:00 to 06:00. You can set the maintenance window to the off-peak period of your business to avoid impact on business.

**Precautions**

To ensure stability of the maintenance process, the instance enters the **Maintaining**
**Instance** state before the maintenance window. When the instance is in this state, access
to data in the database and query operations such as performance monitoring are not affected. However, except for account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. You may encounter a network interruption during the maintenance window. Make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the **Configuration Information** section, click **Configure** to the right of **Maintenance**
**Window**.
5. Select a maintenance window and click **OK**.
The time displayed on the page is in UTC+8.

### Configure primary/secondary

**switchover**

ApsaraDB RDS provides the primary/secondary switchover feature to ensure the high availability of databases. The primary/secondary switchover is performed when the primary instance becomes unavailable. You can also manually switch your business to the secondary instance. This topic describes how to manually switch over services between a primary instance and its secondary instance.

**Background information**

Data is synchronized in real time between the primary and secondary instances. You can access only the primary instance. The secondary instance serves only as a backup instance and does not allow external access. After the switchover, the original primary instance becomes the secondary instance. Network interruptions may occur during a switchover. Make sure that your applications are configured with automatic reconnection policies.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Service Availability**.
5. In the **Availability Information** section of the page that appears, click **Switch**
**Primary/Secondary Instance**.
6. In the dialog box that appears, specify the time when the switching is performed and click
**OK**.
During the switchover, operations such as managing databases and accounts and changing network types cannot be performed. Therefore, we recommend that you select Switch Within Maintenance Window. For more information about how to set a maintenance window, see Set a maintenance window.

### Release an instance

This topic describes how to manually release an instance.

**Precautions**

Only instances in the Running state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance. When you release a primary instance, all of its read-only instances are also released.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. Find the instance that you want to release and choose **More > Release Instance** in the
Actions column.
3. In the message that appears, click **OK**.

### Configure instance

**parameters**

This topic describes how to view and modify the values of instance parameters and query parameter modification history in the console.

**Precautions**

To ensure instance stability, you can modify only some parameters in the console. When you modify a parameter value, refer to the **Value Range** column on the **Editable**
**Parameters** page.
Some parameters require an instance restart to take effect. For more information, see the
**Restart Required** column on the **Editable Parameters** page. Perform this operation
during off-peak hours and make sure that your application has a reconnection mechanism.

**Configure parameters**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Parameters**.
5. You can perform the following operations:
Modify multiple parameters at a time: a. Export the parameters. On the Editable Parameters tab, click **Export Parameters**. The parameter settings of the instance are exported as a TXT file to your computer. b. Modify the parameter values in the exported file. c. Click **Import Parameters** and paste the modified parameters from the file into the dialog box. d. Click **OK**. e. In the upper-right corner, click **Apply Changes**. If a modified parameter requires an instance restart to take effect, the system prompts you to restart the instance. Perform this operation during off-peak hours and make sure that your application has a reconnection mechanism. Before you apply the changes, you can click **Cancel Changes** to cancel the modifications. Modify a single parameter: a. In the **Editable Parameters** list, find the parameter that you want to modify and click the icon in the **Running Value** column. b. Enter a new value based on the displayed value range. c. Click **OK**. d. In the upper-right corner, click **Apply Changes**. If a modified parameter requires an instance restart to take effect, the system prompts you to restart the instance. Perform this operation during off-peak hours and make sure that your application has a reconnection mechanism. Before you apply the changes, you can click **Cancel Changes** to cancel the modifications.

**View the parameter modification history**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the navigation pane on the left of the page that appears, click **Parameters**.
5. Click the **Parameter Modification History** tab.
6. Select a time range and click **OK**.

**Appendix: Editable parameters**

| Parameter | Maj or Ver sion | Def ault Val ue | Value Rang e | Res tart Req uire d | Description |
|---|---|---|---|---|---|
| array nulls _ | 13 | on | [on\|off ] | No | Controls whether unquoted NULL values are recognized when you input a string that contains array elements. |
| authenticatio n timeout _ | 13 | 60 | [1- 600] | No | Specifies the maximum time in seconds that a client can wait to complete identity verification. |
| auto explain. _ log analyze _ | 11, 12, 13 | off | [on\|off ] | No | Controls whether to record the query plan and analysis information in the log. If you enable this parameter, detailed performance data is provided, but overhead increases. |
| auto explain. _ log buffers _ | 11, 12, 13 | off | [on\|off ] | No | Controls whether to log buffer usage during query execution. If you enable this parameter, you can analyze performance issues and check whether performance degrades due to insufficient buffers. |

| auto explain. _ log format _ | 11, 12, 13 | text | [text\|x ml\|jso n\|yaml ] | No | Specifies the output format of the query plan log generated by the auto explain module. Valid _ values include text (default, plain text format) and json (structured JSON format). This parameter controls the readability or machine parsability of the log. |
|---|---|---|---|---|---|
| auto explain. _ log min dura _ _ tion | 11, 12, 13 | -1 | [-1- 60000 ] | No | Specifies the minimum running time threshold in milliseconds. Queries that exceed this threshold are logged. The default value is -1, which indicates that no queries are logged. |
| auto explain. _ log nested s _ _ tatements | 11, 12, 13 | off | [on\|off ] | No | Controls whether to log the query plans of nested SQL statements, such as statements in functions or subtransactions. If you set this parameter to on, the query plans of these statements are also logged for in-depth analysis of performance issues. |
| auto explain. _ log timing _ | 11, 12, 13 | on | [on\|off ] | No | Controls whether to include timing information for each query step in the output of auto explain. If _ you set this parameter to on, the running time is recorded. If you set this parameter to off, timing information is not recorded. The default value is on. |
| auto explain. _ log triggers _ | 11, 12, 13 | off | [on\|off ] | No | Controls whether to include trigger execution information in the auto explain log. If you set this _ parameter to on, trigger execution details are logged to help analyze the impact of triggers on query performance. The default value is off. |
| auto explain. _ log verbose _ | 11, 12, 13 | off | [on\|off ] | No | Controls whether to include detailed plan information in the auto explain output. If you set _ this parameter to on, more detailed query plan information is logged, including extra information for each node. The default value is off. |
| auto explain. _ sample rate _ | 11, 12, 13 | 1 | [0-1] | No | Specifies the probability for the auto explain _ module to sample query plans. This controls the logging frequency. The value ranges from 0 to 1. A value of 0 indicates no sampling, and a value of 1 indicates that every query plan is logged. |

| autovacuum _ analyze scal _ e factor _ | 13 | 0.1 | [0.0- 100.0] | No | Controls the frequency of auto-analyze triggers. It specifies a fraction of the table size to add to autovacuum analyze threshold to determine the _ _ trigger threshold. Auto-analyze is triggered when the number of changed tuples exceeds autovacuum analyze threshold + _ _ (autovacuum analyze scale factor × number of _ _ _ tuples). |
|---|---|---|---|---|---|
| autovacuum _ analyze thre _ shold | 13 | 50 | [0- 21474 83647 ] | No | The number of insert, update, or delete operations required to trigger an auto-analyze operation on a table. When this threshold is reached, the system automatically collects statistics on the table to optimize query plans. |
| autovacuum _ freeze max _ _ age | 13 | 200 000 000 | [1000 00000 - 75000 0000] | Yes | Specifies the maximum age that a transaction ID (TXID) can attain before an autovacuum operation is forced to freeze it. |
| autovacuum _ multixact fre _ eze max ag _ _ e | 13 | 400 000 000 | [1000 0000- 20000 00000 ] | Yes | Controls the autovacuum process to trigger a VACUUM operation when a multixact ID reaches a specified age. |
| autovacuum _ naptime | 13 | 15 | [1- 21474 83] | No | The time in seconds that the autovacuum daemon process waits after cleaning a database before it starts the next check on the same database. |
| autovacuum _ vacuum cost _ delay _ | 11, 12, 13 | 1 1 an d 1 2: 0 1 3: 2 | [0-50] | No | Defines the time interval in milliseconds that the autovacuum process pauses after each cleanup operation. This is used to control the impact of cleanup on system performance. |
| autovacuum _ vacuum cost _ limit _ | 11, 12, 13 | 200 | [200- 10000 ] | No | Sets the cost limit for a single autovacuum operation to balance the impact of cleanup tasks on system performance. |

| autovacuum _ vacuum inse _ rt scale fact _ _ or |   | 13 | 0.2 | [0.0- 100.0] | No | Triggers an autovacuum operation when the number of inserted tuples in a table exceeds (this factor × total number of rows) + autovacuum vacuum insert threshold . _ _ _ |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | (this factor × total number of rows) + |
|   | _ |   |   |   |   | autovacuum vacuum insert threshold _ _ _ |   |
| autovacuum _ vacuum inse _ rt threshold _ |   | 13 | 100 0 | [-1- 21474 83647 ] | No | Specifies the number of inserted tuples required to trigger an autovacuum operation in any table. If set to -1, autovacuum will not trigger a VACUUM operation on any table based on the number of insertions. |   |
| autovacuum _ vacuum scal _ e factor _ |   | 11, 12, 13 | 1 1 an d 1 2: 0. 0 2 1 3: 0. 0 5 | [0.005 -0.15] | No | Triggers an autovacuum operation when the number of dead tuples in a table reaches a specified proportion. |   |
| autovacuum _ vacuum thre _ shold |   | 13 | 50 | [50- 21474 83647 ] | No | Specifies the minimum number of rows to trigger a VACUUM operation during the autovacuum process. |   |
| backend flus _ h after _ |   | 13 | 0 | [0- 256] | No | Controls how much data is written before the PostgreSQL backend process triggers a file system buffer flush (fsync). |   |
| backslash qu _ ote |   | 13 | safe enc _ odin g | [safe _ encodi ng\|on\| off] | No | Controls whether \' can be used in a string literal to represent a quote mark. `on` always allows \' . `off` always rejects it. `safe encoding` accepts \' only if the client _ encoding does not allow an ASCII \ within a multi-byte character. |   |
| bgwriter del _ ay |   | 13 | 200 | [10- 10000 ] | No | Defines the delay in milliseconds between two scans of the shared buffer by the background writer process to find dirty pages that can be written to disk. |   |

| bgwriter flus _ h after _ | 13 | 64 | [0- 256] | No | Controls how much data the background writer (bgwriter) process flushes to disk after performing a write operation. The unit is kilobyte (KB). |
|---|---|---|---|---|---|
| bgwriter lru _ _ maxpages | 13 | 100 0 | [0- 10737 41823 ] | No | Controls the maximum number of dirty pages that the background writer can clean up during each Least Recently Used (LRU) scan. |
| bgwriter lru _ _ multiplier | 13 | 10.0 | [0.0- 10.0] | No | The emphasis that the background writer process places on the Least Recently Used (LRU) algorithm when scanning the shared buffer. This value multiplied by bgwriter lru maxpages _ _ defines the upper limit on the target number of pages to be written back to disk from the dirty page list. |
| bytea output _ | 13 | hex | [escap e\|hex] | No | Sets the output format for values of the bytea type. |
| check functi _ on bodies _ | 13 | on | [on\|off ] | No | Controls the validation of the function body string during CREATE FUNCTION. |
| checkpoint c _ ompletion ta _ rget | 13 | 0.4 | [0.0- 1.0] | No | The proportion of time before the next checkpoint starts that PostgreSQL should attempt to complete the current checkpoint write operation. |
| checkpoint fl _ ush after _ | 13 | 32 | [0- 256] | No | Controls how much data is written before triggering a file system buffer flush during a checkpoint. |
| checkpoint _ warning | 13 | 30 | [0- 21474 83647 ] | No | If checkpoints caused by filling WAL segment files occur more frequently than this parameter value, a corresponding message is written to the server log. The unit is second. |

| client min m _ _ essages | 13 | notic e | [debu g5\|de bug4\| debug 3\|deb ug2\|d ebug1 \|log\|no tice\|w arning \|error] | No | The message level sent to the client. |
|---|---|---|---|---|---|
| commit sibli _ ngs | 13 | 5 | [0- 1000] | No | The minimum number of concurrent active transactions required when performing a commit delay delay. _ |
| constraint ex _ clusion | 13 | parti tion | [partiti on\|on\| off] | No | Controls the query planner's use of table constraints to optimize queries. `on` checks constraints for all tables. `off` never checks constraints. `partition` checks constraints only for inherited child tables and UNION ALL subqueries. |
| cron.databas e name _ | 13 | 'post gres' | .* | Yes | The database that stores pg cron metadata. _ |
| cron.log stat _ ement | 13 | on | [on\|off ] | Yes | Controls whether to log all cron statements before execution. |
| cron.max ru _ nning jobs _ | 13 | 32 | [0- 100] | Yes | The maximum number of jobs that can run concurrently. |
| cursor tuple _ _ fraction | 13 | 0.1 | [0.0- 1.0] | No | Estimates the proportion of rows retrieved from a table when using a cursor query. |
| datestyle | 13 | 'ISO, YMD ' | (ISO\|P ostgre s\|SQL\| Germa n),s* (DMY\| MDY\|Y MD) | No | Sets the display format for date and time values, and the rules for interpreting ambiguous date input values. |

| deadlock tim _ eout | 13 | 100 0 | [1- 21474 83647 ] | No | Sets the maximum time in milliseconds that PostgreSQL waits when detecting a deadlock. |
|---|---|---|---|---|---|
| debug pretty _ print _ | 13 | on | [on\|off ] | No | Controls the format of internal structures, such as query plan trees, when PostgreSQL prints them. |
| debug print _ _ parse | 13 | off | [on\|off ] | No | Controls whether to output the parse tree of an SQL statement to the log. If you set this parameter to on, PostgreSQL logs the parsed internal representation of a query during its execution. |
| debug print _ _ plan | 13 | off | [on\|off ] | No | Controls whether to print debug information during the query plan generation phase. If you set this parameter to on, PostgreSQL outputs detailed query plan information to the log, including the plan tree construction process and the selected execution policy. |
| debug print _ _ rewritten | 13 | off | [on\|off ] | No | Controls whether to output the rewritten SQL statement to the server log. |
| default statis _ tics target _ | 13 | 100 | [1- 10000 ] | No | Sets the default statistics target, which determines the level of detail of statistics collected by PostgreSQL when analyzing a table. |
| default trans _ action deferr _ able | 11, 12, 13 | off | [off\|on ] | No | Sets whether a default transaction can be deferred. This controls whether a transaction is allowed to be deferred in read-only mode to optimize performance. |
| default trans _ action isolati _ on | 13 | 'rea d com mitt ed' | ['serial izable' \|'repe atable read'\|' read commi tted'\|'r ead uncom mitted '] | No | Controls the default isolation level for each new transaction. |
| effective io _ _ concurrency | 13 | 1 | [0- 1000] | No | Sets the number of concurrent disk I/O operations that the query executor expects when performing a table scan. |

| enable bitm _ apscan | 13 | on | [on\|off ] | No | Controls whether to enable the Bitmap Scan query execution policy. |
|---|---|---|---|---|---|
| enable gath _ ermerge | 13 | on | [on\|off ] | No | Controls whether to enable the use of Gather Merge nodes in a query plan. |
| enable hash _ agg | 13 | on | [on\|off ] | No | Controls whether to enable Hash Aggregation. |
| enable hashj _ oin | 13 | on | [on\|off ] | No | Controls whether to enable the Hash Join algorithm. |
| enable incre _ mental sort _ | 13 | on | [on\|off ] | No | Controls whether the query planner can use incremental sort steps. |
| enable index _ onlyscan | 13 | on | [on\|off ] | No | A parameter that controls whether the query optimizer enables the IndexOnlyScan access method. |
| enable index _ scan | 13 | on | [on\|off ] | No | Controls whether the query planner selects index scan as the access method. |
| enable mate _ rial | 13 | on | [on\|off ] | No | Controls whether to enable Materialize nodes. |
| enable merg _ ejoin | 13 | on | [on\|off ] | No | Controls whether to enable the Merge Join connection method. |
| enable nestl _ oop | 13 | on | [on\|off ] | No | Controls whether the query optimizer can use the nested loop join algorithm. |
| enable parall _ el append _ | 13 | on | [on\|off ] | No | Controls whether to enable parallel append operations in the query plan. |
| enable parall _ el hash _ | 13 | on | [on\|off ] | No | Controls whether to enable parallel processing in hash aggregation and hash join operations. |
| enable partit _ ion pruning _ | 13 | on | [on\|off ] | No | Controls whether to enable the partition pruning optimization feature. |

| enable partit _ ionwise aggr _ egate | 11, 12, 13 | on | [off\|on ] | No | Controls whether to enable partition-wise aggregate operations. If you set this parameter to on, PostgreSQL attempts to perform aggregation on each partition of a partitioned table separately, which may improve query performance. |
|---|---|---|---|---|---|
| enable partit _ ionwise join _ | 11, 12, 13 | on | [off\|on ] | No | Controls whether to enable partition-wise join optimization. If you set this parameter to on, PostgreSQL attempts to perform more efficient join operations on partitioned tables to improve query performance. |
| enable seqsc _ an | 13 | on | [off\|on ] | No | Controls whether the query optimizer can consider sequential scan (seq scan) as a method to access table data. |
| enable sort _ | 13 | on | [off\|on ] | No | Controls the enabled state of sort operations. |
| enable tidsc _ an | 13 | on | [off\|on ] | No | Controls whether to enable TID (Tuple ID) scan. |
| escape strin _ g warning _ | 13 | on | [off\|on ] | No | Controls whether a warning should be issued when a processed string contains a backslash (\). |
| extra float d _ _ igits | 11, 12, 13 | 1 1 an d 1 2: 0 1 3: 1 | [-15-3] | No | Controls the number of extra digits of precision displayed for floating-point number types, such as float4 and float8. A negative value reduces precision, while a positive value increases it, affecting the display format of floating-point numbers. |
| force paralle _ l mode _ | 13 | 0 | [0\|1\|o n\|off] | No | Forces the enabling or disabling of parallel execution mode for queries. |
| from collaps _ e limit _ | 13 | 8 | [1- 21474 83647 ] | No | If the resulting FROM list does not exceed this parameter value, the planner will merge subqueries into the upper query. |
| geqo | 13 | on | [off\|on ] | No | Enables or disables genetic query optimization. |

| geqo effort _ | 13 | 5 | [1-10] | No | Controls the trade-off between planning time and query plan effectiveness in GEQO. |
|---|---|---|---|---|---|
| geqo genera _ tions | 13 | 0 | [0- 21474 83647 ] | No | Controls the number of iterations of the algorithm used by GEQO. If set to 0, an appropriate value is chosen based on geqo pool size. _ _ |
| geqo pool si _ _ ze | 13 | 0 | [0- 21474 83647 ] | No | Controls the pool size used by GEQO, which is the number of individuals in the genetic population. |
| geqo selecti _ on bias _ | 13 | 2 | [1.5- 2.0] | No | Controls the selection bias used by GEQO. |
| geqo thresh _ old | 13 | 12 | [2- 21474 83647 ] | No | Sets the threshold of FROM items above which GEQO will be used. |
| gin fuzzy se _ _ arch limit _ | 13 | 0 | [0- 21474 83647 ] | No | Controls the maximum number of keys that the engine attempts to match when performing a fuzzy search using a GIN (Generalized Inverted Index) index. |
| gin pending _ _ list limit _ | 13 | 409 6 | [64- 21474 83647 ] | No | Controls the maximum size of the pending list for a GIN index during its construction or maintenance. The unit is KB. |
| hash mem _ _ multiplier | 13 | 1 | [1.0- 1000. 0] | No | Used to calculate the maximum amount of memory that can be used by hash-based operations. The final limit is determined by work mem multiplied by hash mem multiplier. _ _ _ |
| hot standby _ _ feedback | 13 | off | [on\|off ] | No | Controls whether a hot standby server sends feedback to the primary server to prevent long- running queries from causing rows on the primary server to be locked for too long. |
| idle in trans _ _ action sessio _ n timeout _ | 11, 12, 13 | 360 000 0 | [3000- 36000 000] | No | Sets the timeout for idle transaction sessions. Sessions that exceed this time are automatically terminated. |
| index advise _ r.enable log _ | 13 | on | [on\|off ] | No | Enables index advisor logging. _ |

| index advise _ r.max aggre _ gation colum _ n count _ | 13 | 10 | [0- 21474 83647 ] | No | Specifies the maximum number of columns or expressions allowed in the GROUP BY, ORDER BY, and DISTINCT clauses of a table. |
|---|---|---|---|---|---|
| index advise _ r.max candid _ ate index co _ _ unt | 13 | 500 | [0- 21474 83647 ] | No | The maximum number of index candidates for all tables. |
| intervalstyle | 13 | post gres | [postg res\|po stgres verbo _ se\|sql _ standa rd\|iso _ 8601] | No | Sets the display format for interval values. |
| jit | 11, 12 | off | [off\|on ] | No | Controls whether PostgreSQL enables the Just-In- Time (JIT) compilation feature to accelerate query execution. A value of on enables it, and a value of off disables it. |
| join collapse _ limit _ | 13 | 8 | [1- 21474 83647 ] | No | Controls the complexity of reordering multi-table joins (JOINs) when the query optimizer considers a query plan. |
| lc monetary _ | 13 | C | .* | No | Sets the locale for formatting monetary amounts. |
| lc numeric _ | 13 | C | .* | No | Sets the locale for formatting numbers. |
| lc time _ | 13 | C | .* | No | Sets the locale for formatting dates and times. |
| lock timeout _ | 11, 12, 13 | 0 | [0- 36000 000] | No | Sets the timeout for acquiring a lock in a single database transaction. If the timeout is exceeded, the attempt is aborted and an error is reported. The unit is millisecond. A value of 0 indicates no timeout. |
| log autovacu _ um min dur _ _ ation | 13 | 100 00 | [-1- 21474 83647 ] | No | During an autovacuum process, information about an operation is logged to the server log only if the operation's running time exceeds the specified value in milliseconds. A value of 0 logs all autovacuum actions. A value of -1 disables logging of autovacuum actions. |

| log checkpoi _ nts | 13 | on | [off\|on ] | No | Controls whether to log checkpoint information in the PostgreSQL log file. |
|---|---|---|---|---|---|
| log connecti _ ons | 11, 12, 13 | off | [off\|on ] | No | Controls whether to log client connection and disconnection events in the PostgreSQL log file. If this option is set to on, the system generates a log entry each time a client attempts to connect or successfully establishes a session with the database server. |
| log disconne _ ctions | 11, 12, 13 | off | [off\|on ] | No | Controls whether the PostgreSQL database logs client disconnection information. If set to on, the system generates a corresponding record in the log file whenever a client disconnects from the database. |
| log duration _ | 11, 12, 13 | off | [off\|on ] | No | Controls whether to log the running time of each SQL statement. If set to on, PostgreSQL adds the running time of each SQL statement in milliseconds to the log file. |
| log executor _ stats _ | 13 | off | [off\|on ] | No | Controls whether to log query executor statistics. |
| log min dura _ _ tion sample _ | 13 | -1 | [-1- 21474 83647 ] | No | Defines a threshold. Only statements whose running time exceeds this threshold are logged. A value of -1 disables slow query logging. A value of 0 logs all statements and their running times. The unit is millisecond. |
| log min dura _ _ tion stateme _ nt | 11, 12, 13 | 1 1 an d 1 2: 5 0 0 0 1 3: 1 0 0 0 | [1000- 60000 0] | No | Logs SQL statements whose running time exceeds the specified number of milliseconds to locate slow queries. |
| log paramet _ er max leng _ _ th | 13 | -1 | [-1- 10737 41823 ] | No | Sets the maximum data length in bytes to be logged for a statement. A value of 0 indicates that no data is logged. A value of -1 indicates no length limit. |

| log paramet _ er max leng _ _ th on error _ _ | 13 | 0 | [-1- 10737 41823 ] | No | The maximum data length in bytes to be logged in the error log when an error occurs. A value of 0 indicates that no data is logged. A value of -1 indicates no length limit. |
|---|---|---|---|---|---|
| log parser st _ _ ats | 13 | off | [on\|off ] | No | Controls whether to log statistics for the query parsing phase. |
| log planner _ _ stats | 13 | off | [on\|off ] | No | Controls whether to log query planner statistics. |
| log replicatio _ n commands _ | 13 | off | [on\|off ] | No | Controls whether to log all replication-related commands to the server log. |
| log stateme _ nt | 11, 12, 13 | ddl | [ddl\|m od\|all] | No | Controls which SQL statements are logged. Valid values: ddl: Logs only data definition language (DDL) statements, such as CREATE, ALTER, and DROP. mod: Logs all DDL statements and data modification language (DML) statements, such as INSERT, UPDATE, and DELETE. all: Logs all SQL statements. |
| log stateme _ nt sample ra _ _ te | 13 | 1.0 | [0.0- 1.0] | No | The proportion of statements that should be logged among those whose running time exceeds log min duration sample. _ _ _ |
| log stateme _ nt stats _ | 13 | off | [on\|off ] | No | Controls whether to log execution statistics for each SQL statement. |
| log temp file _ _ s | 11, 12, 13 | 131 072 | [4096- 10485 76] | No | Sets the threshold in kilobytes for logging temporary file sizes. When the size of a temporary file, such as one generated by a sort or hash operation, exceeds this value, PostgreSQL logs relevant information. A value of - 1 disables logging of any temporary file information. |
| log transacti _ on sample r _ _ ate | 13 | 0 | [0.0- 1.0] | No | The proportion of newly started transactions to be logged. A value of 0 disables transaction- based sample logging. A value of 1 logs all statements in every transaction. |
| logical deco _ ding work m _ _ em | 13 | 655 36 | [64- 20971 51] | No | Sets the maximum memory to be used for logical decoding. The unit is KB. |

| maintenance io concurre _ _ ncy | 13 | 0 | [-1- 1000] | No | A special version of effective io concurrency, _ _ specifically for optimizing the I/O performance of database maintenance operations. It sets how many concurrent I/O requests can be initiated simultaneously. |
|---|---|---|---|---|---|
| max files pe _ _ r process _ | 13 | 100 0 | [64- 21474 83647 ] | Yes | The maximum number of files that each PostgreSQL backend process can open simultaneously. |
| max logical _ _ replication w _ orkers | 13 | 32 | [0- 26214 3] | Yes | The maximum number of logical replication worker processes. |
| max pred lo _ _ cks per pag _ _ e | 13 | 2 | [0- 21474 83647 ] | No | Sets the maximum number of predicate locks per data page. |
| max pred lo _ _ cks per relat _ _ ion | 13 | -2 | [- 21474 83648 - 21474 83647 ] | No | Controls the maximum number of predicate locks that can exist simultaneously on a single relation (table). |
| max pred lo _ _ cks per tran _ _ saction | 13 | 64 | [10- 21474 83647 ] | Yes | Sets the maximum number of predicate locks that each transaction can hold. |
| max replicati _ on slots _ | 13 | 16 | [0- 26214 3] | Yes | Sets the maximum number of logical replication slots that can exist simultaneously in the database system. |
| max slot wal _ _ keep size _ _ | 13 | -1 | [-1- 21474 83647 ] | No | Sets the maximum WAL size that can be reserved by replication slots. The unit is MB. A value of -1 indicates no limit. |
| max stack d _ _ epth | 13 | 204 8 | [100- 6144] | No | Controls the maximum stack depth allowed during query execution in a PostgreSQL process. |

| max standby _ archive del _ _ ay | 13 | 300 000 | [-1- 21474 83647 ] | No | Sets the maximum time a standby server waits for new WAL segments from the primary server when applied write-ahead log (WAL) records conflict with changes on the primary server during archive recovery or streaming replication. The unit is millisecond. |
|---|---|---|---|---|---|
| max standby _ streaming d _ _ elay | 13 | 300 000 | [-1- 21474 83647 ] | No | The maximum delay allowed on a hot standby database to ensure synchronization with the primary database. The unit is millisecond. |
| max sync w _ _ orkers per s _ _ ubscription | 13 | 2 | [0- 26214 3] | No | The maximum number of synchronization workers per subscription. |
| min parallel _ _ index scan s _ _ ize | 13 | 64 | [0- 71582 7882] | No | Controls the minimum amount of data required to enable parallel query when performing an index scan. |
| min parallel _ _ table scan si _ _ ze | 13 | 102 4 | [0- 71582 7882] | No | In PostgreSQL, the query optimizer considers using a parallel scan only when the data volume of a table exceeds this threshold during a table scan. |
| old snapshot _ threshold _ | 11, 12, 13 | -1 | [-1- 2880] | Yes | Controls the expiration threshold for old snapshots. Snapshots older than this threshold are cleaned up to prevent excessive resource consumption. A negative value, such as -1, disables automatic cleanup. The unit is minute. |
| operator pre _ cedence war _ ning | 13 | off | [on\|off ] | No | When enabled, the parser will issue a warning for any construct whose meaning has changed due to operator precedence changes since PostgreSQL 9.4. |
| parallel lead _ er participati _ on | 13 | on | [on\|off ] | No | Allows the leader process to no longer wait for worker processes when executing query plans under Gather and Gather Merge nodes. |
| password en _ cryption | 13 | md5 | [md5\| scram- sha- 256] | No | Controls the encryption algorithm that PostgreSQL uses when storing user passwords. |
| pg stat state _ _ ments.max | 13 | 500 0 | [100- 21474 83647 ] | Yes | Controls the maximum number of queries that the pg stat statements extension can track. _ _ |

| pg stat state _ _ ments.save | 13 | off | [on\|off ] | No | Controls whether to retain the statistics collected by the pg stat statements module after the _ _ PostgreSQL instance restarts. |
|---|---|---|---|---|---|
| pg stat state _ _ ments.track | 13 | top | [none\| top\|all ] | No | Specifies which types of SQL statements are tracked by pg stat statements. _ _ |
| pg stat state _ _ ments.track _ utility | 13 | off | [on\|off ] | No | Controls whether to collect and log statistics for utility commands tracked by the pg stat statements module. _ _ |
| pgaudit.log c _ atalog | 13 | on | [on\|off ] | No | Enables session logging when all relations in a statement are in pg catalog. _ |
| pgaudit.log l _ evel | 13 | log | [debu g5\|de bug4\| debug 3\|deb ug2\|d ebug1 \|info\|n otice\| warnin g\|log] | No | Specifies the log level to be used for log entries. |
| pgaudit.log _ parameter | 13 | off | [on\|off ] | No | Controls whether the audit log should include the parameter values passed during statement execution. |
| pgaudit.log r _ elation | 13 | off | [on\|off ] | No | Controls whether to create a separate audit log entry for each relation (such as TABLE, VIEW) referenced in a SELECT or DML statement when it is executed. |
| pgaudit.log s _ tatement on _ ce | 13 | off | [on\|off ] | No | When a single statement (or sub-statement) generates multiple audit logs, this controls whether the full statement text and parameter values are included only in the first log entry or repeated in every log entry. |
| pgaudit.role | 13 | '' | .* | No | Specifies the master role for object audit logging. |
| pglogical.bat ch inserts _ | 13 | on | [on\|off ] | Yes | Performs bulk inserts when possible. |

| pglogical.con flict log level _ _ | 13 | log | [debu g5\|de bug4\| debug 3\|deb ug2\|d ebug1 \|info\|n otice\| warnin g\|error \|log\|fa tal\|pa nic] | No | Sets the log level for logging resolved conflicts. |
|---|---|---|---|---|---|
| pglogical.con flict resolutio _ n | 13 | appl y re _ mot e | [error\| apply _ remot e\|keep local\|l _ ast up _ date _ wins\|fi rst up _ date _ wins] | No | Sets the method used to resolve conflicts when they can be resolved. |
| pglogical.ext ra connectio _ n options _ | 13 | '' | .* | No | Connection options to be added to all peer node connections. |
| pglogical.syn chronous co _ mmit | 13 | off | [on\|off ] | Yes | pglogical-specific synchronous commit value. |
| pglogical.use spi _ | 13 | off | [on\|off ] | Yes | Controls whether to use SPI (Server Programming Interface) instead of low-level APIs to apply changes. |
| plan cache _ _ mode | 13 | auto | [auto\|f orce g _ eneric plan\|f _ orce c _ ustom plan] _ | No | Controls whether the planner uses custom or generic plans. |

| quote all ide _ _ ntifiers | 13 | off | [on\|off ] | No | Controls whether to use double quotes to quote all identifiers, such as table names and column names, in generated SQL statements. |
|---|---|---|---|---|---|
| rds auditlog _ _ max query l _ _ ength | 13 | 819 2 | [512- 49152 ] | No | The maximum length of the audit log. The unit is byte. |
| rds force tra _ _ ns ro non su _ _ _ p | 13 | off | [on\|off ] | No | Controls whether non-superusers are read-only. |
| rds max log _ _ files _ | 11, 12, 13 | 1 1 an d 1 2: 2 0 1 3: 4 | 11 and 12: [10- 200 ] 13: [3- 200 ] | No | Sets the maximum number of log files. The size of each log file is 100 MB. |
| rds sync rep _ _ lication time _ out | 11, 12, 13 | 0 | [0- 30000 0] | Yes | The maximum time to wait for WAL synchronous replication. When a timeout occurs, synchronous replication changes to asynchronous replication until the replication catches up. The unit is millisecond. |
| row security _ | 13 | on | [on\|off ] | No | Controls whether row-level security policies are enabled. |
| session repli _ cation role _ | 13 | origi n | [origin \|replic a\|local ] | No | Controls the triggering of replication-related triggers and rules for the current session. |

| shared prelo _ ad libraries _ | 13 | 'pg _ stat _ stat eme nts,a uth _ dela y,zh pars er' | 'pg st _ at stat _ ement s,auth delay _ ,passw ordche ck,aut o expl _ ain,pg path _ man,p gaudit ,pglogi cal,pg bigm, _ pg hin _ t plan, _ pg pre _ warm, zhpars er,tim escale db,pg _ jieba,p lugin _ debug ger,in dex a _ dviser, pg cro _ n,pg s _ tat kc _ ache' | Yes | Specifies a list of shared libraries to preload when the PostgreSQL database starts. |
|---|---|---|---|---|---|
| sql firewall.fi _ rewall | 13 | disa ble | [disabl e\|lear ning\|p ermiss ive\|enf orcing ] | Yes | Determines the operating mode of the sql firewall _ extension. |
| ssl max prot _ _ ocol version _ | 13 | '' | [''\|TLS v1\|TLS v1.1\|T LSv1.2 \|TLSv1 .3] | No | The maximum SSL/TLS version to use. If set to an empty string, any protocol version is allowed. |
| ssl min prot _ _ ocol version _ | 13 | TLSv 1 | [TLSv1 \|TLSv1 .1\|TLS v1.2\|T LSv1.3 ] | No | The minimum SSL/TLS version to use. |

| standard con _ forming strin _ gs | 13 | on | [on\|off ] | No | Controls whether ordinary string literals treat backslashes as plain text according to the SQL standard. |
|---|---|---|---|---|---|
| statement ti _ meout | 11, 12, 13 | 0 | [0- 86400 000] | No | Sets the maximum time a single database query is allowed to run before it is forcibly terminated. The unit is millisecond. The default value is 0, which indicates no limit. |
| synchronize _ seqscans | 13 | on | [on\|off ] | No | Controls whether to synchronize during sequential scans. |
| synchronous commit _ | 11, 12, 13 | off | [off\|lo cal\|re mote _ write\|r emote apply _ \|on] | No | Controls whether a transaction commit waits for write-ahead logging (WAL) records to be written to disk or a synchronous standby server to ensure data durability and consistency. Valid values: off: Does not wait for WAL records to be written. Some committed transactions may be lost. local: Waits only for the local WAL write to complete. remote write: Waits for at least one _ synchronous standby server to receive the WAL record. remote apply: In a streaming replication _ scenario, when the primary database commits a transaction, it waits for the standby database to apply the corresponding changes before it returns a success message to the client. on: In a streaming replication scenario, when the primary database commits a transaction, it waits for the standby database to receive the WAL stream from the primary database and write it to the WAL file before it returns a success message to the client. |
| synchronous standby na _ _ mes | 13 | '' | [''\|'sta ndby1' ] | No | Defines which standby servers should be considered synchronous standby servers. |
| tcp keepaliv _ es count _ | 13 | 10 | [0- 21474 83647 ] | No | Defines the maximum number of TCP keepalive probes that the system can send before the connection is considered dead. |
| tcp keepaliv _ es idle _ | 13 | 45 | [0- 21474 83647 ] | No | Sets the amount of time in seconds that a TCP connection must remain idle before the first keepalive probe is sent. |

| tcp keepaliv _ es interval _ | 13 | 10 | [0- 21474 83647 ] | No | Sets the interval in seconds between consecutive keepalive probes when the keepalive feature is enabled on a TCP connection. |
|---|---|---|---|---|---|
| temp buffers _ | 13 | 102 4 | [100- 10737 41823 ] | No | Sets the amount of memory allocated for each database session to handle temporary tables, temporary indexes, and sort operations. |
| timezone | 13 | Asia/ Sha ngh ai | .* | No | Sets the time zone for the database session. |
| track activity _ query size _ _ | 13 | 409 6 | [100- 10485 76] | Yes | Sets the maximum length of the currently executing query text stored in the activity view. The unit is byte. |
| track commi _ t timestamp _ | 11, 12, 13 | off | [on\|off ] | Yes | Controls whether to record the timestamp of a transaction commit. If enabled, you can query the commit time of a transaction, but it increases storage overhead. The default value is off. |
| transform nu _ ll equals _ | 13 | off | [on\|off ] | No | Controls whether expressions of the form expr = NULL are treated as expr IS NULL. |
| vacuum clea _ nup index sc _ _ ale factor _ | 13 | 0.1 | [0.0- 10000 00000 0.0] | No | The ratio of the number of inserted tuples to the number of tuples in the table before cleaning up the index. |
| vacuum cost _ delay _ | 13 | 0 | [0- 100] | No | A parameter that controls cost calculation during autovacuum. It defines the number of milliseconds the process should wait after performing certain costly cleanup operations. |
| vacuum cost _ limit _ | 13 | 100 00 | [200- 10000 ] | No | Controls the cost limit for autovacuum and manual VACUUM operations. |
| vacuum cost _ page dirty _ _ | 13 | 20 | [0- 10000 ] | No | Controls the cost of modifying a dirty page during a VACUUM operation. |
| vacuum cost _ page hit _ _ | 13 | 1 | [0- 10000 ] | No | Defines the cost when a VACUUM operation accesses a page that is already in the shared buffer. |

| vacuum cost _ page miss _ _ | 13 | 2 | [0- 10000 ] | No | Sets the cost of a VACUUM operation when a page is not in the shared buffer, which means it needs to be read from disk. |
|---|---|---|---|---|---|
| vacuum defe _ r cleanup ag _ _ e | 11, 12, 13 | 0 | [0- 50000 00] | No | Specifies the number of transactions by which a VACUUM operation defers cleaning up dead tuples to reduce cleanup conflicts caused by concurrent transactions. The value can be 0 or a positive integer. The default value is 0, which indicates immediate cleanup. |
| vacuum free _ ze min age _ _ | 13 | 500 000 00 | [0- 20000 00000 ] | No | Controls when VACUUM (including autovacuum) starts to freeze transaction IDs to prevent transaction ID wraparound when processing a table. |
| vacuum free _ ze table age _ _ | 13 | 200 000 000 | [0- 20000 00000 ] | No | Controls at what table age a freeze process is triggered during an autovacuum operation. |
| vacuum mul _ tixact freeze _ min age _ _ | 13 | 500 000 0 | [0- 10000 00000 ] | No | Controls the minimum age before a transaction ID is frozen (converted to a permanent XID) during a VACUUM operation. |
| vacuum mul _ tixact freeze _ table age _ _ | 13 | 200 000 000 | [0- 20000 00000 ] | No | A parameter that controls when a VACUUM operation starts to consider freezing row versions, especially for rows that are marked for update due to multixact IDs. |
| wal compres _ sion | 13 | off | [on\|off ] | No | Controls whether to enable compression for write-ahead logging (WAL). |
| wal keep siz _ _ e | 13 | 204 8 | [0- 10240 00] | No | Sets the size of write-ahead log (WAL) files to be retained on the primary server to ensure that standby servers have enough WAL records to catch up with the primary server's state. The unit is MB. |
| wal keep se _ _ gments | 11, 12 | 0 | [0- 10240 00] | No | Specifies the minimum number of write-ahead logging (WAL) file segments to be retained in the pg wal directory. _ |
| wal level _ | 11, 12, 13 | repli ca | [replic a\|logic al] | Yes | Controls the level of write-ahead logging (WAL), which determines the availability of replication and recovery features. Valid values include replica (supports replication) and logical (supports logical decoding). |

| wal receiver _ status inter _ _ val | 13 | 1 | [0- 21474 83] | No | Sets the frequency at which the WAL receiver process sends status messages to the primary server. The unit is second. |
|---|---|---|---|---|---|
| wal receiver _ timeout _ | 13 | 600 00 | [0- 21474 83647 ] | No | Sets the maximum idle time in milliseconds that the write-ahead logging (WAL) receiver waits for WAL data from the primary server during replication. |
| wal sender t _ _ imeout | 13 | 600 00 | [0- 21474 83647 ] | No | Sets the maximum idle time in milliseconds that the primary server waits for the standby server to receive write-ahead logging (WAL) data. |
| wal skip thr _ _ eshold | 13 | 204 8 | [-1- 20971 51] | No | The file size threshold in KB that triggers the "fsync instead of WAL write" optimization strategy. |
| wal writer d _ _ elay | 13 | 200 | [1- 10000 ] | No | Defines the sleep time in milliseconds between two write operations of the write-ahead logging (WAL) writer process. |
| wal writer fl _ _ ush after _ | 13 | 128 | [0- 21474 83647 ] | No | Controls the minimum number of bytes accumulated by the WAL writer process before PostgreSQL writes write-ahead logging (WAL) data to disk. |
| xmlbinary | 13 | base 64 | [base6 4\|hex] | No | Sets how binary values are encoded as XML. |
| xmloption | 13 | cont ent | [conte nt\|doc ument ] | No | Sets whether XML data is treated as a document or a content fragment in implicit parsing and serialization operations. |

### Read-only instances

#### Overview of read-only ApsaraDB RDS

**for PostgreSQL instances**

This topic provides an overview of read-only ApsaraDB RDS for PostgreSQL instances. If your database system receives a small number of write requests but a large number of read requests, a single primary RDS instance may be overwhelmed by read requests and have its workloads affected. To offload read requests from the primary RDS instance, you can create one or more read-only RDS instances. Read-only RDS instances help increase the read capability of your database system and the throughput of your application.

**Overview**

When a read-only RDS instance is being created, ApsaraDB RDS replicates data from the secondary RDS instance to the read-only RDS instance. After the read-only RDS instance is created, it has the same data as the primary RDS instance. In addition, after the data on the primary RDS instance is updated, ApsaraDB RDS immediately synchronizes the updates to all read-only RDS instances that are attached to the primary RDS instance. Each read-only RDS instance runs in a single-node architecture. In this architecture, no secondary RDS instance is provided as a standby for a read-only RDS instance. The following figure shows the topology of the primary RDS instance and its read-only RDS instances.

**Features**

Read-only RDS instances reside within the same region as the primary RDS instance, but can reside in different zones. The specifications and storage space of read-only RDS instances cannot be lower than those of the primary RDS instance. The network types of read-only RDS instances can differ from the network type of the primary RDS instance. The databases and accounts on read-only RDS instances are synchronized from the primary RDS instance. You do not need to manage databases or accounts on read-only RDS instances. When you create a read-only RDS instance, ApsaraDB RDS replicates the IP address whitelists of the primary RDS instance to the read-only RDS instance. However, the IP address whitelists of the read-only RDS instance are independent of the IP address whitelists of the primary RDS instance. For more information about how to modify the IP address whitelists of a read-only RDS instance, see Configure an IP address whitelist. Read-only RDS instances support monitoring and alerting. You can monitor metrics such as disk usage, IOPS, number of connections, and CPU utilization.

**Limits**

A maximum of five read-only RDS instances can be created on a primary RDS instance. You cannot configure backup policies or manually create backups for read-only RDS instances. These operations are performed on primary RDS instances. You cannot migrate data to read-only RDS instances. You cannot create or delete databases on read-only RDS instances. You cannot create or delete accounts, grant permissions to accounts, or change the passwords of accounts on read-only RDS instances.

**FAQ**

Q: After I create accounts on my primary RDS instance, can I manage the accounts on the read-only RDS instances of my primary RDS instance? No, you cannot manage the accounts on the read-only RDS instances. Although the accounts created on your primary RDS instance are synchronized to the read-only RDS instances, the accounts have only the read permissions on the read-only RDS instances.

#### Create a read-only ApsaraDB RDS for

**PostgreSQL instance**

This topic describes how to create a read-only RDS instance for a primary ApsaraDB RDS for PostgreSQL instance, which can improve the read capability of your database system and the throughput of your application. Each read-only RDS instance is a replica of the primary RDS instance. Data updates on the primary RDS instance are automatically synchronized to all read-only RDS instances that are attached to the primary RDS instance.

**Prerequisites**

The primary instance runs PostgreSQL 10.0 or later.

**Usage notes**

You can create read-only RDS instances for the primary RDS instance. You cannot convert existing RDS instances to read-only RDS instances. When you create a read-only RDS instance, ApsaraDB RDS replicates data from the secondary RDS instance to the read-only RDS instance. This prevents interruptions to your workloads that are run on the primary RDS instance. A read-only RDS instance does not inherit the parameter settings of the primary RDS instance. Default parameter settings are generated for the read-only RDS instance. You can modify the default parameter settings in the ApsaraDB RDS console. The instance type and storage capacity of a read-only instance cannot be lower than that of the primary instance. You can create up to five read-only instances for a primary instance.

**Create a read-only instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the **Instance Distribution** section of the Basic Information page, click **Add** to the right
of **Read-only Instance**.
5. On the Create Read-only Instance page, configure parameters and click **Submit**. The
following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Area | Region | The region in which you want to create the read- only instance. |
| Specifications | Database Engine Type | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Engine Version | The version of the database engine, which is the same as that of the primary instance and cannot be changed. |
|   | Instance Edition | The edition of the read-only instance. The edition cannot be changed. |
|   | Specification | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type as the primary instance for the read-only instance. |
|   | Storage | The storage capacity of the read-only instance. Valid values: 20 to 6000. Unit: GB. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same storage capacity as the primary instance for the read-only instance. |
| Network Type | Network Type | The network type of the read-only instance. This must be the same as that of the primary instance and cannot be changed. |
|   | VPC | The VPC in which you want to create the read- only instance. This parameter is required when Network Type is set to VPC. |
|   | vSwitch | The vSwitch in the VPC. This parameter is required when Network Type is set to VPC. |

#### View a read-only ApsaraDB RDS for

**PostgreSQL instance**

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View instance details of a read-only instance by using its ID**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to view.
3. Click the ID of the instance or click **Manage** in the corresponding Actions column to go to
the Basic Information page.

**View details of a read-only instance by using the primary**

**instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. On the **Basic Information** page, move the pointer over the number below **Read-only**
**Instance** in the **Distributed by Instance Role** section. The ID of the read-only instance is
displayed.
5. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

**View the latency of data replication to a read-only RDS**

**instance**

A read-only RDS instance may synchronize data from the primary RDS instance at a specific latency. You can go to the Basic Information page of a read-only RDS instance to view the latency of data replication to the instance.

#### Manage a read-only ApsaraDB RDS for

**PostgreSQL instance**

This topic describes how to change specifications of a read-only RDS instance, release a readonly RDS instance, and view monitoring and alerting information of a read-only RDS instance.

**Change specifications of a read-only RDS instance**

1. Log in to the ApsaraDB RDS console.
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

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click the ID of the instance or click **Manage** in the Actions column to go to the Basic
Information page.
4. In the **Status** section of the **Basic Information** page, click **Release Instance**. In the
message that appears, click **Confirm**.

**View monitoring and alerting information of a read-only RDS**

**instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click the ID of the instance or click **Manage** in the Actions column to go to the Basic
Information page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.
The monitoring and alerting feature of read-only RDS instances can be used in the same manner as that of the primary instance. For more information, see View monitored resources.

### Manage tags

If you have a large number of instances, you can create multiple tags and add the tags to the instances. Then, you can query instances by tag. This topic describes how to manage tags.

**Usage notes**

A tag consists of a key-value pair. Each key must be unique for an Alibaba Cloud account in a region. This limit does not apply to the values of keys. You can add up to 20 tags to an instance. If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.

**Add tags**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, enter the tag key and tag value and click **OK**.

**Search for an instance by tag**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click **Advanced Filter**.
3. You can search for your instance by **Instance ID /Name**, **VIP**, and **Tag Filtering**. Select a
tag from the **Filter by Tag** drop-down list.
4. After you select a tag, the instance list displays all instances that are bound with the tag.

**View the tags that are added to an instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, if a small number of tags are added to an instance, the
corresponding tags are displayed in the Tag column. If a large number of tags are added to an instance, move the pointer over the icon in the **Tag** column to view all the tags that are added to the instance.

**Remove a tag**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, click the
icon to the right of the tag and click **OK**.

## Database connection

### Connect to an ApsaraDB RDS

**for PostgreSQL instance**

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an RDS instance. DMS is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational databases, such as MySQL, SQL Server, PostgreSQL, MongoDB, and Redis databases. DMS can also be used to manage NoSQL databases and Linux-based database servers. You can also use a database client to connect to an RDS instance. ApsaraDB RDS is fully compatible with open source database engines. Therefore, you can connect these two types of databases in the same way. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Use DMS to log on to an ApsaraDB RDS instance.

**Use the pgAdmin 4 client to connect to an instance**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.
For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows). In this example, pgAdmin 4 v6.15 is downloaded.
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

**Important**

The postgres database is the default system database. Do not perform operations on the postgres database.

### Use DMS to log on to an

**ApsaraDB RDS instance**

This topic describes how to use Data Management (DMS) to log on to an ApsaraDB RDS instance.

**Prerequisites**

The IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
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
If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

### View and modify the internal

**endpoint and port number**

You must use the internal endpoint and port number to access an ApsaraDB RDS instance. This topic describes how to view and modify the internal endpoint and port number of an ApsaraDB RDS instance in the ApsaraDB RDS console.

**View the internal endpoint and port number**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the **Basic Information** section, view the internal endpoint and port number of the
instance.

**Modify the internal endpoint and port number**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the right side of the page, click **Change Endpoint**.
6. In the dialog box that appears, set **Connection Type** to **Internal Endpoint**.
7. Modify the endpoint prefix and port number and click **OK**.

**FAQ**

Q: Do I need to modify the endpoint or port number in my application after I modify the endpoint or port number of an instance? A: Yes, you must modify the endpoint or port number in the application after you modify them. Otherwise, the application cannot connect to databases of the instance. Q: Does the modification of the endpoint take effect immediately? Do I need to restart the instance? A: No, you do not need to restart the instance. The modification takes effect immediately.

## Accounts

### Create an account

Database accounts are required for using ApsaraDB RDS instances. This topic describes how to create an account on an ApsaraDB RDS for PostgreSQL instance.

**Account types**

ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. The following table describes these types of accounts.

| Account type | Description |
|---|---|
| Privileged account | You can create and manage privileged accounts in the ApsaraDB RDS console or by calling API operations. You can create multiple privileged accounts for each RDS instance. The privileged accounts of an RDS instance have the permissions to manage all standard accounts and databases that are created on the instance. A privileged account allows you to manage permissions at fine-grained levels based on your business requirements. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect all standard accounts of the RDS instance on which the privileged account is created. |
| Standard account | You can create and manage standard accounts in the ApsaraDB RDS console, by calling API operations, or by executing SQL statements. You can create multiple standard accounts for each RDS instance. You must grant the permissions on specific databases to standard accounts. You cannot use a standard account to create or manage other accounts, or close connections that are established by using other accounts. |

**Usage notes**

You can create multiple privileged accounts and standard accounts in the ApsaraDB RDS console. You can also create and manage standard accounts by using SQL statements. Privileged accounts created on an instance that uses local SSDs cannot be deleted. Before you migrate data from an on-premises database to an RDS instance, you need to create a database and an account on the RDS instance. Make sure that the created database has the same properties as the on-premises database. In addition, make sure that the created account has the same permissions on the created database as the account that is authorized to manage the on-premises database. We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple databases and accounts and grant each account only the permissions to access specified databases. This way, you can implement fine-grained access control. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for accounts and change the passwords on a regular basis.

**Create a privileged or standard account**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Account Management**.
5. On the Accounts page, click **Create Account** and configure the following parameters.

| Parameter | Description |
|---|---|
| Database Account | The username of the account. It must be 2 to 63 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a letter and end with a letter or a digit. It cannot be the same as the username of an existing account. It cannot start with pg. It cannot contain SQL keywords. For more information, see SQL keywords. |
| Account Type | ApsaraDB RDS for PostgreSQL instances support two types of accounts: privileged accounts and standard accounts. A privileged account has all operation permissions on all databases. Standard accounts have all operation permissions only on their authorized databases. Note The permitted operations include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER. |
| New Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ |
| Confirm Password | Enter the password of the account again. |

| Description | This parameter is available only if the instance uses standard SSDs. It is an optional parameter. You can enter description to make the account easier to identify. The description can be up to 256 characters in length. |
|---|---|

6. Click **OK**.

### Reset the password of a

**database account**

This topic describes how to use the ApsaraDB RDS console to reset the password of your database account if you forget the password.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Reset Password**.
6. In the dialog box that appears, enter a new password and click **OK**.
The password must meet the following requirements: The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) _ + - =

### Lock or delete an account

**from an instance**

This topic describes how to lock or delete an account from an ApsaraDB RDS for PostgreSQL instance that uses standard SSDs.

**Prerequisites**

Your RDS instance uses standard SSDs.

**Lock an account of an instance**

When an account is locked, you cannot use the account to log on to the RDS instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Lock**.
Wait a few minutes. When the **Status** column displays **Locking**, the account is locked. If you want to use the account again, click **Unlock** in the **Actions** column.

**Delete an account from an instance**

If the account that you want to delete is granted permissions on databases, tables, or other objects, the "Some objects depend on account" message is displayed when you attempt to delete the account. You can delete the account only after you remove the permissions of the account.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Delete**.
6. In the message that appears, click **OK**.

### Delete an account

You can delete a database account in the ApsaraDB RDS console.

**Prerequisites**

You can use the console to delete privileged and standard accounts that are no longer used.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to delete and click **Delete** in the Actions column.
5. In the message that appears, click **Confirm**.
Accounts in the **Processing** state cannot be deleted.

## Databases

### Create a database

Before you start to use ApsaraDB RDS, you must create a database on an ApsaraDB RDS instance. This topic describes how to create a database on an ApsaraDB RDS for PostgreSQL instance.

**Prerequisites**

An ApsaraDB RDS for PostgreSQL instance is created. For more information, see Create an instance. An account is created. For more information, see Create an account.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
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
If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
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

### Delete a database

This topic describes how to delete a database in the ApsaraDB RDS for PostgreSQL console.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
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
If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
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

## Networks, VPCs, and

**vSwitches**

### Change the VPC and vSwitch

**of an instance**

This topic describes how to change the virtual private cloud (VPC) and vSwitch for an ApsaraDB RDS for PostgreSQL instance.

**Prerequisites**

The ApsaraDB RDS for PostgreSQL instance is deployed in a VPC. The ApsaraDB RDS for PostgreSQL 10.0 instances that use local SSDs do not support this feature.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch vSwitch**.
6. In the dialog box that appears, select a destination vSwitch and click **OK**.
If you want to create a vSwitch, click **go to the VPC console**.
7. In the message that appears, click **Switch**.
When you switch an instance to a different vSwitch, a transient connection that lasts approximately 30 seconds occurs. Make sure that your application is configured to automatically reconnect to your instance. If data is cached on your client, you can read data but cannot write data. After the vSwitch of your instance is changed, we recommend that you immediately clear the cache on the client.

### Change the network type of

**an ApsaraDB RDS for PostgreSQL**

**instance**

This topic describes how to change the network type of an ApsaraDB RDS for PostgreSQL instance between classic network and Virtual Private Cloud (VPC). witches

**Prerequisites**

The ApsaraDB RDS instance uses local SSDs.

**Background information**

Classic network: ApsaraDB RDS instances in the classic network are not isolated. You can block unauthorized access only by configuring IP address whitelists on these instances. VPC: Each VPC is an isolated network. We recommend that you use the VPC network type because it provides a higher security level. You can configure route tables, CIDR blocks, and gateways within a VPC. To smoothly migrate applications to the cloud, you can use the leased line or VPN method to create a virtual data center that consists of your self-managed data center and a VPC.

**Change the network type from VPC to classic network**

Precautions The ApsaraDB RDS instance must be in a VPC. After you change the network type from VPC to classic network, the internal endpoint of the ApsaraDB RDS instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, you cannot connect Elastic Compute Service (ECS) instances deployed in VPCs to the ApsaraDB RDS instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. You may encounter a network interruption of about 30 seconds during the change process. To avoid business interruptions, we recommend that you change the network type during off-peak hours or make sure that your application is configured to automatically reconnect to the instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to Classic**
**Network**.
6. In the message that appears, click **OK**.
After the network type is changed to classic network, only ECS instances within the classic network can connect to the ApsaraDB RDS instance by using the internal endpoint. You must configure the internal endpoint for the ECS instances.
7. Configure an IP address whitelist to allow ECS instances within the classic network to
connect to the ApsaraDB RDS instance by using the internal endpoint. witches If the network isolation mode of the ApsaraDB RDS instance is standard whitelist, add the internal IP addresses of the ECS instances to a whitelist of your ApsaraDB RDS instance. If the network isolation mode of the ApsaraDB RDS instance is enhanced whitelist, add the internal IP addresses of the ECS instances to a whitelist of the classic network type. If no whitelists of the classic network type are available, create a whitelist. For more information about the enhanced whitelist mode, see Switch to the enhanced whitelist mode.

**Change the network type from classic network to VPC**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to VPC**.
6. In the Switch to VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. witches Select a VPC. We recommend that you select the VPC where your ECS instances are deployed. Otherwise, the ECS instances cannot communicate with the ApsaraDB RDS instance over the internal network. Select a vSwitch. If no vSwitches are available in the selected VPC, create one in the same zone where the ApsaraDB RDS instance is deployed. For more information, see Create a vSwitch in **Virtual Private Cloud User Guide**. Clear or select the **Reserve Original Classic Network Endpoint** check box.

**Clear the Reserve Original Classic Network Endpoint check box**

The classic network endpoint is not retained and changes to a VPC endpoint. When you change the network type from classic network to VPC, a network interruption of 30 seconds occurs. In this case, ECS instances located in the classic network are disconnected from your ApsaraDB RDS instance.

**Select the Reserve Original Classic Network Endpoint check box**

The classic network endpoint is retained, and a new VPC endpoint is generated. In this case, your ApsaraDB RDS instance runs in hybrid access mode. Both ECS instances located in the classic network and ECS instances located in the selected VPC can access your ApsaraDB RDS instance over an internal network. You must set **Expiration Time**
**(Important)** to **14 Days Later**, **30 Days Later**, **60 Days Later**, or **120**
**Days Later** for the classic network. You can also modify the expiration
date after the network type is changed. For more information, see Configure hybrid access from both the classic network and VPCs. When you change the network type from classic network to VPC, no network interruptions occur. ECS instances located in the classic network are still connected with your ApsaraDB RDS instance until the classic network endpoint expires. Before the classic network endpoint expires, you must add the new VPC endpoint to your applications that run on the ECS instances located in the selected VPC. This allows ApsaraDB RDS to migrate your workloads to the selected VPC without network interruptions. Seven days before the classic network endpoint expires, the system sends a text message to the phone number bound to your Apsara Stack tenant account every day. For more information, see Configure hybrid access from both the classic network and VPCs.
7. Add the internal IP addresses of ECS instances located in the selected VPC to an IP address
whitelist of the VPC network type. This allows the ECS instances to connect to your ApsaraDB RDS instance over an internal network. If no IP address whitelists of the VPC network type are available, create one. If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires. If you do not retain the classic network endpoint, connections between ECS instances in the classic network and the ApsaraDB RDS instance over the internal network are interrupted. You must add the VPC endpoint to ECS instances in the VPC immediately after the network type is changed. witches

### Configure hybrid access from

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
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the **Instance Connection** tab, click **Change Expiration Time**.
6. In the **Change Expiration Time** dialog box, select an expiration time and click **OK**.

## Monitoring

### View monitored resources

ApsaraDB RDS provides a wide range of performance metrics. This topic describes how to view resource monitoring data in the ApsaraDB RDS console.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.
5. On the **Monitoring** tab, select a time range to query the corresponding monitoring data.
You can click **Refresh** in the upper-right corner of the **Monitoring** tab to refresh the monitoring information.

### Configure an alert rule

This topic describes how to create alert rules in the ApsaraDB RDS for PostgreSQL console. This allows you to identify and handle monitoring data anomalies at the earliest opportunity.

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
|---|---|
| Effective time | The period during which the alert rule takes effect. Cloud Monitor checks whether the monitoring data triggers the alert rule only during the effective period. |
| Alarm callback | The callback URL to which Cloud Monitor sends alert notifications by using the POST request method. Note The callback URL must be accessible for Cloud Monitor. You can enter only an HTTP URL. IP addresses are not supported. |
| No data processing method | Specify how Cloud Monitor acts when no alert is triggered. Valid values: No processing: Cloud Monitor does not perform any operations when no alert is triggered. Send no data alarm: Cloud Monitor sends the corresponding notifications to contacts when no alert is triggered. |
| Alarm contact | The alert contacts or alert contact groups to which Cloud Monitor sends alert notifications. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

## Data security

### Configure an IP address

**whitelist**

This topic describes how to configure a whitelist for an ApsaraDB RDS instance. Only entities that are listed in a whitelist can access your ApsaraDB RDS instance.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure and do not interrupt the operations of your ApsaraDB RDS instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the ApsaraDB RDS instance. The IP address whitelist labeled default contains only the default IP address 0.0.0.0/0, which allows all entities to access your ApsaraDB RDS instance. Configure an ECS security group: Add an ECS security group for the ApsaraDB RDS instance to allow ECS instances in the group to connect to the ApsaraDB RDS instance.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.
You can also click **Create Whitelist** to create a whitelist.
6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks used to access the
instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your ApsaraDB RDS instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Alibaba Cloud account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### Configure SSL encryption

This topic describes how to configure SSL encryption for an ApsaraDB RDS instance.

**Prerequisites**

The ApsaraDB RDS instance uses standard SSDs.

**Usage notes**

After SSL encryption is enabled, SSL is used to encrypt all the data that is transmitted over an internal network or the Internet. SSL encryption protects the data in transit from being leaked. After SSL encryption is enabled, you must close the existing connection and establish a new one to bring SSL encryption into effect.

**Enable SSL encryption**

The Internet Engineering Task Force (IETF) upgraded SSL 3.0 to TLS. The term SSL encryption is used in the industry. In this topic, SSL encryption refers to TLS encryption. ApsaraDB RDS supports TLS 1.0, TLS 1.1, and TLS 1.2.
1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. On the **SSL** tab, click **Configure SSL**.
5. In the dialog box that appears, select an endpoint for which you want to enable SSL
encryption and click **OK**. The process to enable the SSL encryption feature requires approximately 1 minute to complete. You can refresh the page to view the status of the feature.

**Connect to an ApsaraDB RDS for PostgreSQL instance over SSL**

Make sure that the CA certificate has been downloaded to your computer. For more information, see Enable SSL encryption.
1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Launch the pgAdmin 4 client.
To download the pgAdmin 4 client, visit pgAdmin 4 (Windows).
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
|---|---|

7. Click **Save**.
8. If the connection information is correct, choose **Servers > Server Name > Databases >**
**postgres**. If the following page appears, the connection is established.

**Important**

The postgres database is the default system database. Do not perform operations on the postgres database.

**Update the validity period of the SSL certificate**

The **Update Validity** operation causes your RDS instance to restart. Proceed with caution.
1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. Click **Update Validity**.

**Disable SSL encryption**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. Turn off **SSL Encryption**. In the message that appears, click **OK**.

**Important**

This operation triggers a restart of your RDS instance. Proceed with caution.

### Configure data encryption

This topic describes how to configure data encryption for an ApsaraDB RDS instance that uses standard SSDs. The disk encryption feature improves data security and eliminates the need to modify business or application configurations. ApsaraDB RDS automatically applies disk encryption to both the snapshots that are generated from the encrypted SSDs and the SSDs that are created from those snapshots.

**Prerequisites**

The ApsaraDB RDS instance uses standard SSDs.

**Configure disk encryption**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log In**.
4. In the top navigation bar, choose **Products > Security > Key Management Service**.
5. Click **Create Key**.
6. Configure the following parameters.

| Section | Parameter | Description |
|---|---|---|
| Area | Organizatio n | The organization to which the key belongs. |
|   | Resource set | The resource set to which the key belongs. |
|   | Region | The region in which the key resides. |
| Basic configuratio n | Key type | Key Management Service (KMS) supports the following key types: Symmetric customer managed keys (CMKs): Aliyun AES 256 _ _ Asymmetric CMKs: RSA 2048 _ EC P256 _ EC P256K _ |
|   | Key usage | ENCRYPT/DECRYPT: encrypts or decrypts data. |
|   | Protection Level | SOFTWARE: Use a software module to protect the CMK. |
|   | Alias | The identifier of the CMK. For more information, see Use aliases in KMS User Guide. |
|   | Description s | The description of the key. |
| Advanced configuratio n | Rotation cycle | Indicates whether automatic rotation is enabled. If you choose to enable automatic rotation, you must select a rotation cycle. For more information about rotation, see Key rotation in KMS User Guide. Valid values: 30 Days 90 Days 180 Days 365 Days Custom: You can specify a custom cycle that ranges from 7 days to 730 days. Note You can configure this parameter only if you set the Key type parameter to Aliyun AES 256. _ _ |
|   | Key Material Source | The source of the key material. You can configure this parameter only if you set the Key type parameter to Aliyun AES 256. _ _ Alibaba Cloud KMS: Use KMS to generate key material. External: Manually import external key material. Note If Rotation cycle is set to Open, the External option is unavailable. |

7. Click **Submit**.
8. Create an RDS instance. Select Disk Encryption when you create the instance. For more
information, see Create an instance.

### Configure TDE

ApsaraDB RDS for PostgreSQL provides the Transparent Data Encryption (TDE) feature. This topic describes how to enable TDE for your ApsaraDB RDS for PostgreSQL instance. This topic also describes how to use TDE to encrypt and decrypt tables and indexes.

**Prerequisites**

The RDS instance meets the following requirements: The RDS instance runs PostgreSQL 10 or later. The RDS instance uses local disks. If read-only RDS instances are attached to your RDS instance, make sure the read-only RDS instances also meet the preceding requirements. Key Management Service (KMS) is activated.

**Usage notes**

After TDE is enabled, database performance may be affected in I/O bound workload scenarios. If TDE is enabled for the primary RDS instance, streaming replication between the primary RDS instance and its self-managed secondary instance is not supported. If KMS is overdue, the cloud disk of your RDS instance cannot be decrypted and become unavailable. Make sure that KMS runs as normal. If you use an existing custom key for TDE, take note of the following items: If you disable or delete the custom key, the RDS instance cannot run as expected. The affected operations include creating a snapshot, restoring data by using a snapshot, and rebuilding a secondary RDS instance. If you restart your RDS instance after you disable the custom key, your RDS instance becomes unavailable. You must use an Alibaba Cloud account or an account to which the AliyunSTSAssumeRoleAccess policy is attached. For more information, see **What Is Key Management Service?**

**Enable TDE**

**Use an automatically generated key**

The key encryption key (KEK) used by this method is the service key that is provided by KMS.
1. Log in to the ApsaraDB RDS console.
2. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, turn on **TDE Status**.
5. In the dialog box that appears, select **Use Automatically Generated Key** and click **OK**.

**Use an existing custom key**

The KEK used by this method is the customer master key (CMK) that you upload to KMS.
1. Log in to the ApsaraDB RDS console.
2. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, turn on **TDE Status**.
5. In the dialog box that appears, select **Use Existing Custom Key** and click **OK**.
If you do not have a custom key, you can click **go to the KMS console** to create one. In the KMS console, you can create a key and import your own key material.

**Replace a key**

TDE is enabled.
1. Log in to the ApsaraDB RDS console.
2. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane of the page that appears, click **Data Security**.
4. On the **TDE** tab, click **Replace key** to the right of **TDE Status**.
5. In the dialog box that appears, select **Use Automatically Generated Key** or **Use**
**Existing Custom Key** and click **OK**.
If you do not have a custom key, you can click **go to the KMS console** to create a custom key and import your own key material.

**Use TDE to encrypt or decrypt a table or an index**

After TDE is enabled for your RDS instance, you must use TDE to encrypt or decrypt tables on the RDS instance. Encryption and decryption may cause performance loss. We recommend that you select an appropriate encryption range to minimize performance loss. Encrypt a table or an index. Encrypt a table.

```
-- Create an encrypted table. CREATETABLE <tablename> WITH (encryption=on); -- Set the encryption parameter to on for a table. ALTERTABLE <tablename> SET (encryption=on);
```

Encrypt an index.

```
-- Create an encrypted index. CREATE INDEX <indexname> ... WITH (encryption=on); -- Set the encryption parameter to on for an index. ALTERINDEX <indexname> SET (encryption=on);
```

The following types of indexes can be encrypted: B-tree, hash, SP-GiST, GIN, GiST, and BRIN. Decrypt a table or an index. The following ALTER statements trigger the rewriting of a table or an index, which is similar to the VACUUM FULL statement. We recommend that you execute the following statements during off-peak hours. Decrypt an encrypted table.

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

## Logs and audit

### SQL Audit (DataBase Audit)

The SQL Audit feature for RDS enables you to view SQL details and regularly audit SQL statements. This feature does not affect the performance of your instance.

**Precautions**

The SQL Audit feature does not affect instance performance. SQL audit logs are retained for 7 days. Exported SQL audit files are retained for 2 days and then automatically deleted. The SQL Audit feature is disabled by default. You must enable it manually. You cannot view logs that were generated before you enabled the SQL Audit feature. A single SQL statement is limited to 4 KB.

**Enable SQL Audit**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Data Security**.
5. Click the **SQL Audit** tab.
6. Click **Enable SQL Audit** or **Enable Now**.
7. In the message that appears, click **Confirm**.
After you enable SQL Audit, you can query audit logs by time range, DB, user, and keyword.

**Disable SQL Audit**

If you no longer need the SQL Audit feature, you can disable it.

**Important**

When you disable the SQL Audit feature, all SQL audit logs, including historical logs, are deleted. Before you disable the feature, export the audit logs and save them locally.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Data Security**.
5. Select the **SQL Audit** tab and click **Export File**.
If more than 1 million SQL audit logs match the filter conditions, only the first 1 million logs are exported. At an export speed of 900 rows per second, it takes approximately 20 minutes to export 1 million SQL audit logs.
6. Click **File List**. In the **Operation** column for the object file, click Download to save the file
to your computer.
7. Click **Disable SQL Audit**.
8. In the message that appears, click **Confirm**.

**Switch the storage location of audit logs**

By default, audit logs are stored in SLS-inner. You can switch the storage location to the publicly accessible SLS-PUB.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Data Security**.
5. Click the **SQL Audit** tab.
6. Enable storage of audit logs to SLS-PUB.

**Important**

This operation cannot be reversed. Proceed with caution.

### Manage logs

You can view logs for errors, slow queries, and primary/secondary instance switching for ApsaraDB RDS for PostgreSQL instances in the ApsaraDB RDS console or by executing SQL statements. These logs help you troubleshoot errors. This topic describes how to manage logs in the console.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Logs**.
5. On the **Logs** page, click the **Error Logs**, **Slow Query Logs**, or **Primary/Secondary**
**Switching Logs** tab, select a time range, and then click **Search**.

| Tab | Description |
|---|---|
| Error Logs | Records database running errors that occurred within the last month. |
| Slow Query Logs | Records SQL statements within the last month that took longer than one second to execute. Duplicated SQL statements are removed. |

| Primary/Secondary Switching Logs | Records switchovers between the primary and secondary instances within the last month. |
|---|---|

## Backup

### Back up an ApsaraDB RDS for

**PostgreSQL instance**

This topic describes how to back up an ApsaraDB RDS for PostgreSQL instance. You can configure a backup policy based on which ApsaraDB RDS automatically backs up your RDS instance. If you do not configure a backup policy, the default backup policy is used. You can also manually back up your RDS instance.

**Precautions**

Do not perform data definition language (DDL) operations during a backup. If you do so, the backup may fail due to table locks. We recommend that you back up your ApsaraDB RDS instance during off-peak hours. If the amount of data is large, it may take a long time to back up your ApsaraDB RDS instance. Backup files are retained for a specified retention period. We recommend that you download the required backup files to your computer before they are deleted.

**Backup description**

ApsaraDB RDS for PostgreSQL allows you to perform full physical backup and back up archived redo log files of databases.

**Configure a backup policy for automatic backup**

ApsaraDB RDS automatically backs up your instance based on the specified backup policy.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. On the **Backup and Restoration** page, click the **Backup Settings** tab and then click
**Edit**.
6. In the dialog box that appears, configure the parameters and click **Save**. The following
table describes the parameters.

| Paramete r | Description |
|---|---|
| Data Backup Retention | The default value is 7 days. You can set this parameter to a value from 7 to 730 days. |

| Backup Cycle | You can select one or more days of the week. Note To ensure data security, you must perform at least two backups per week. |
|---|---|
| Backup Time | You can set this parameter to any time period in hours. |
| Log Backup | The switch controlling log backup. Important Disabling log backup clears all log backups and disables the point-in-time recovery feature. |
| Log Backup Retention | The number of days to retain log backup files. The default value is 7 days. You can set this parameter to a value from 7 to 730 days. The value must be less than or equal to the data backup retention period. |

**Manual backup**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. Click **Backup Instance** in the upper-right corner of the page to open the **Backup**
**Instance** dialog box.
5. Select a backup mode and a backup policy, and then click **OK** to start the backup.
The backup mode is fixed at **Full Backup** and the backup policy is fixed at **Instance**
**Backup**.

**What to do next**

You can click the icon in the upper-right corner of the page to open the **Task Progress** list and view the task progress.

### Download data and log

**backup files**

This topic describes how to download unencrypted data and log backup files in the ApsaraDB RDS console to archive the files and restore data to an on-premises database.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Backup and Restoration** to open the **Backup and**
**Restoration** page.
5. Click the Data Backup or Log Backup tab.
To download data backup files, click the **Data Backup** tab. To download log backup files, click the **Log Backup** tab.
6. Select a time range to which you want to restore the instance.
7. Find the data backup or log backup file that you want to download and click **Download**
**Instance Backup** or **Download** in the **Actions** column.
If you want to download a data backup file and use the data backup file to restore data, we recommend that you select the data backup file created closest to the point in time when the required data exists. If the log backup file is used to restore data to an on-premises database, take note of the following items: The instance ID of the log backup file must be the same as that of the data backup file. The start time of the log backup file must be later than the data backup time and earlier than the time for restoration.
8. In the dialog box that appears, select a download method.

| Download method | Description |
|---|---|
| Download button | Use a browser to download the backup file. |
| Download URL | Copy the download URL. If you want to use other tools to download the file, use this method. |

If you use a Linux operating system, you can run the following command to download the file:

```
wget -c '<Download URL of the backup file>' -O <File name>
```

The -c option enables resumable download. The -O option saves the downloaded file by using a specified name. We recommend that you use the file name contained in the download URL. If the URL contains more than one parameter, we recommend that you enclose the URL in a pair of single quotation marks (').

### Create a logical backup for

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

### Create a full backup of an

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

pg_basebackup cannot back up a single database or database object. For more information about how to back up a single database or database object, see Create a logical backup for an ApsaraDB RDS for PostgreSQL instance.
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

## Restoration

### Restore data of an ApsaraDB

**RDS for PostgreSQL instance**

This topic describes how to use the backup data of an ApsaraDB RDS for PostgreSQL instance to restore data.

**Usage notes**

The new instance has the same IP address whitelists, backup settings, and parameter settings as the original instance. The new instance has the same data and account information as the backup set or instance at the time point. The SSL encryption settings and alert information of the new instance are different from those of the original instance.

**Prerequisites**

The original RDS instance whose data you want to restore must meet the following requirements: The original RDS instance is in the Running state and is not locked. The original RDS instance does not have ongoing migration tasks. If you want to restore data to a point in time, the log backup feature is enabled for the original RDS instance. If you want to restore data from a backup set, the original RDS instance has at least one backup set.

**Restore data of an ApsaraDB RDS for PostgreSQL instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the target instance.
3. Click the instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. In the upper-left corner of the page that appears, click **Restore Database**.
6. Configure the following parameters.

| Section | Paramete r | Description |
|---|---|---|
| Area | Geograph y | The region where the instance is deployed. |

| Database Recovery | Restore mode | By point in time: allows you to restore the data to a point in time within the specified log backup retention period. For more information about how to view or modify the log backup retention period, see Back up an ApsaraDB RDS for PostgreSQL instance. By Backup Set: allows you to restore the data from a backup set. Note The By point in time option is available only after the log backup feature is enabled. |
|---|---|---|
|   | Restore time | The time to which the database is restored. This parameter is displayed when you set Restore mode to By point in time. |
|   | Backup Set | The backup set used to restore the database. This parameter is displayed when you set Restore mode to By Backup Set. |
| Specificat ion Configura tion | Instance name | The name of the instance. |
|   | Database Type | The engine of the database. The value of this parameter is set to PostgreSQL and cannot be changed. |
|   | Database Version | The version of the database engine. The value of this parameter is set to the engine version of the current instance and cannot be changed. |
|   | Series | The edition of the instance. |
|   | Storage Type | The storage type of the instance. The value of this parameter is set to the storage type of the current instance and cannot be changed. |
|   | Instance specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. For more information, see > Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage space | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. Valid values: 20 to 6000. Unit: GB. The value is in 5 GB increments. |

| Network Type | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services on a classic network are not isolated from each other. Unauthorized access to a cloud service is blocked only by the security group or whitelist of the service. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. Note If you set the network type to Proprietary Network, you must also select a VPC and a vSwitch. |
|---|---|---|

7. Click **Submit**.

### Restore data from a logical

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
|---|---|
| username | The username of the privileged account of the ApsaraDB RDS for PostgreSQL instance. |
| port | The port number of the ApsaraDB RDS for PostgreSQL instance. |
| dbname | The name of the database whose data you want to restore. |
| dumpdir | The directory and name of the logical backup file to use. |

Example:

```
pg_restore -h 'pgm-bpxxxxx.pg.rds.aliyuncs.com' -U test123 -p 3433 -d testdb2 /tmp/te stdb.dump
```

2. When `Password:` appears, enter the password of the privileged account of your ApsaraDB
RDS instance and press the Enter key. You can ignore alerts generated by the embedded plpgsql plug-in.

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
|---|---|
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
RDS instance and press the Enter key. You can ignore alerts generated by the embedded plpgsql plug-in.

## DAS

### Introduction to DAS

Database Autonomy Service (DAS) is a cloud service that uses machine learning and expert experience to automate perception, healing, optimization, O&M, and security for databases. DAS simplifies database management and prevents service failures that are caused by manual operations. This way, DAS helps ensure that the database service of users runs in a stable, secure, and efficient manner.

**Features**

ApsaraDB RDS for PostgreSQL leverages the core capabilities of DAS to deeply integrate intelligent diagnostics and autonomy services into the ApsaraDB RDS console. It offers the following features to provide a one-stop database management experience: Diagnostics: Diagnostics integrates selected features of DAS, including session management, real-time monitoring, and storage analysis. This allows you to conveniently view database diagnostics and optimization results. Session management: supports real-time monitoring, analysis, and intervention of active sessions on database instances. It allows you to view abnormal sessions (such as longrunning uncommitted transactions) and export or terminate sessions. These features help you quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation. Real-time monitoring: allows you to view visualized charts and tables generated from key operational metrics collected at high frequencies. This feature is designed to help database administrators (DBAs) and developers gain insights into the real-time loads of database instances, quickly locate the root cause of performance jitters, and assess the resource usage of database instances. Storage analysis: allows you to view the storage usage and the number of remaining days for which storage is available on a database instance. This feature also allows you to view the storage usage of a specified table, tablespace fragments, and diagnostic results on the database. Dashboard: allows you to view performance metrics, such as TPS, QPS, and throughput, of an instance. You can view performance metrics in different ways. For example, you can view the performance metrics within a specific time period, compare performance metrics collected during different time periods, or customize the performance metrics you want to view. View slow query logs: allows you to view slow query log trends, statistical information, and execution details. It also provides optimization recommendations and allows you to export historical data, helping you quickly locate and resolve performance bottlenecks.

### Diagnostics

#### Session management

Log in to the RDS console and navigate to the **Session Management** page of Database Autonomy Service (DAS) to monitor, analyze, and manage active sessions of database instances in real time. You can view abnormal sessions such as long-uncommitted transactions, export sessions, or terminate sessions. this feature helps you quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instances page, click the
instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane, click **Autonomy Services > Diagnostics**. On the
**Session Management** tab:

**Instance sessions**

i. **View abnormal sessions** Click **Anomaly Detection**. In the pop-up dialog box, you can view abnormal sessions that the system identifies, including sessions that have not submitted transactions for a long period of time and sessions that occupy excessive resources. You can click **Optimize** or **End** to handle these sessions. ii. **View key metrics** Move the pointer over **Active session**, **Maximum Execution Duration**, **CPU**
**Utilization**, or **Connection Usage** to view the detailed information and trend in the pop-
up window.

**Session statistics**

**View session statistics**

You can view summarized session information by user, access source, or database, including the total number of sessions, the total number of ongoing sessions, and the longest session duration.

**Export session statistics**

You can export session statistics by summary, user, access source, or database.

#### Real-time monitoring

After you log in to the ApsaraDB RDS console and navigate to the instance performance page of Database Autonomy Service (DAS), you can view visualized charts and tables generated from key operational metrics collected at high frequencies. This feature is designed to help database administrators (DBAs) and developers gain insights into the real-time loads of database instances, quickly locate the root cause of performance jitters, and assess the resource usage of database instances.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instances page, click the
instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. Click the **Real-time Monitoring** tab. The system automatically loads real-time data. You
can switch between the **Real-time Charts** and **Real-time Tables** views. For more information, see **View switching and advanced operations** in this topic.

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

| DML distrib ution | DML Eexecutio ns count | select: The number of SELECT statements executed per second. insert: The number of INSERT statements executed per second. update: The number of UPDATE statements executed per second. delete: The number of DELETE statements executed per second. | Business profiling: Identify whether the workload is read-heavy or write-heavy to help formulate an index optimization policy, such as adjusting the read/write splitting architecture. |
|---|---|---|---|
| Conne ction sessio ns | Connectio ns | Active Sessionsconnections: The number of open connections that are in an active statuse. Total Cconnections: The total number of open connections. | Bottleneck identification: Monitor the peaks of active connections. If the number of active sessionconnections remains high for an extended period, check for long-running transactions or unreleased application connections. |
| Cache efficie ncy | InnoDB CacheBuff er Pool | Cache Hhit Rratio: The ratioproportion of data read from memory. Cache Uusage: The occupancy ratio of the buffer pool. | Performance key: The hit ratio should be close to 100%. A low hit ratio means that a large number of requests fall through to the disk (physical reads), which causes a sharp performance drop. Consider increasing the buffer pool size or optimizing SQL queries. |
| Data access | InnoDB Raccessed rows | rows read: The number of _ InnoDB rows read per second. rows inserted: The number of _ InnoDB rows inserted per second. rows updated: The number of _ InnoDB rows updated per second. rows deleted: The number of _ InnoDB rows deleted per second. | Index optimization: If rows read is _ extremely high but the returned result set is small, a full table scan exists and you must add an appropriate index. |
| I/O reads and writes | Logical Rreads/ and pPhysical Rreads | Logical Rreads: The number of logical reads per second (read from the buffer pool). Physical Rreads: The number of physical reads per second (read from the disk). | I/O bottleneck: A surge in physical reads severely degrades performance and typically results from cold data access, an insufficient buffer pool, or missing indexes. |

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
which facilitates baseline data recording and detailed data comparison. Each row in the table represents a sampling point in time, and each column corresponds to the specific value of a metric.
**Data download**: On the **Real-time Tables** tab, click the **Download** button in the
upper-right corner of the page to export the current report data to your local device. Some database engines (MongoDB and Redis) do not support the report download feature. The actual availability depends on what the console displays.

**Parameter description**

Click **Metric Description** in the upper-left corner of the page to view the specific definition of each metricmonitoring item, allowing you towhich helps you interpret data more accurately.

**Pause and resume**

The upper-right corner displays the remaining refresh count. You can manually control the automatic refresh frequency of the page, or click **Pause** to freeze the statuse at a specific moment for detailed analysis during troubleshooting.

**Usage recommendations**

Establish a baseline: During stable business periods, observe and record normal QPS, TPS, and CPU usage as a benchmark for subsequent fault comparison. Perform correlation analysis: Avoid viewing a single metric in isolation. For example, when QPS drops, immediately check whether InnoDB row lock waits increase or slow queries increase, and observe forwhether physical reads show abnormal fluctuations in physical reads. Watch for spikes: Sudden spikes in charts typically correspond to specific business events (such as scheduled jobs starts or flash sales). Cross-referencing the timestampCorrelating the point in time with business logs helps you quickly locate the issue.

#### Storage analysis

After you log in to the ApsaraDB RDS console and navigate to the Storage Analysis page of Database Autonomy Service (DAS), you can view the storage usage and the number of remaining days for which storage is available on a database instance. This feature also allows you to view the storage usage of a specified table, tablespace fragments, and diagnostic results on the database.

**Prerequisites**

The database instance is connected to DAS. If the instance is not connected, an authorization message appears on this page. Click Authorize.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instances page, click the
instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**. On the
**Storage Analysis** tab, you can perform the following operations:
On the **Storage Analysis** tab, click the **Storage Overview** tab. You can view data such as the storage overview, exception list, storage trend, and tablespaces. On the **Storage Analysis** tab, click the **Data Space** tab. You can view the storage usage of each database and tablespace. Click the name of a tablespace to view the fields and indexes of the tablespace.

### Dashboard

After you log in to the ApsaraDB RDS console and navigate to the Dashboard page of Database Autonomy Service (DAS), you can view performance metrics, such as TPS, QPS, and throughput, of the instance. You can view performance metrics in different ways. For example, you can view the performance metrics within a specific time period, compare performance metrics collected during different time periods, or customize the performance metrics you want to view.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instances page, click the
instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane, choose **Autonomy Services > Dashboard**.
On the **Performance Trends** tab, you can view the trends of changes in the TPS, QPS, and sessions. You can also click **More Metrics** to customize the metrics you want to view. Click the icon next to the name of a metric to view its description. On the **Performance Trend Comparison** tab, select two time periods to compare the performance metrics collected within the specified time periods. On the **Custom Charts** tab, you can centrally display and manage the desired performance metrics in one chart by customizing performance charts. This simplifies troubleshooting. You must create a dashboard if this is the first time you use **custom charts**.

### View slow query logs

After you log in to the ApsaraDB RDS console and navigate to the Slow Query Logs page of Database Autonomy Service (DAS), you can view slow query log trends, statistical information, and execution details. It also provides optimization recommendations and allows you to export historical data, helping you quickly locate and resolve performance bottlenecks.

**Procedure**

1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instances page, click the
instance ID, or click **Management** in the **Operation** column, to go to the **Basic**
**Information** page.
3. In the left-side navigation pane, choose **Autonomy Services****>****Slow Query Logs** to go to
the slow log analysis details page. On this page, you can view the following information: In the **Slow Log Trend** section, view the slow query log trend of the instance. Click the **Slow Log Statistics** tab to view slow log details for a specified time range and optimize the slow SQL statements. The instances of some database types do not support the SQL optimization feature. Refer to the actual features available in the console. For the instances of ApsaraDB RDS for MySQL and PolarDB for MySQL Primary/Secondary Edition, click the **Optimize** button in the Actions column of the slow SQL record that you want to mange. The record is highlighted in blue to help you quickly locate the SQL statement being analyzed in a large number of slow SQL statements. This highlight persists after you close the optimization window and automatically shifts to the new record when you optimize another slow SQL statement. Click the **Slow Log Details** tab to view the execution details of slow query logs.

## Plug-ins

### Plug-ins supported

This topic describes the plug-ins that are supported by ApsaraDB RDS for PostgreSQL and their available versions. The following table only lists the common plug-ins. After connecting to the instance, you can use the SELECT * FROM pg_available_extensions; command to view all plug-ins and versions supported by the current instance. The actual query results prevail. If the queried plug-in versions are different from the following table, upgrade the cloud environment to the latest version.

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

### Use mysql_fdw to read and

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
in the previous step. The field names in the foreign MySQL table must be the same as the field names in the table in the MySQL database. You can choose to create only the fields that you want to query. For example, if the table in the MySQL database contains the ID, NAME, and AGE fields, you can create only the ID and NAME fields in the foreign MySQL table.

```
CREATE FOREIGN TABLE <Name of the foreign MySQL table> (<Name of Field 1> <Data type of Field 1>,<Name of Field 2> <Data type of Field 2>...) server <Name of the MySQL se rver> options (dbname '<Name of the MySQL database>', table_name '<Name of the table in the MySQL database>');
```

Example:

```
CREATE FOREIGN TABLE ft_test (id1 int, name1 text) server mysql_server options (dbnam e 'test123', table_name 'test');
```

**What to do next**

You can use the foreign MySQL table to check whether the extension has enabled read and write operations on the MySQL database. Data can be written to the table in the MySQL database only when the table is assigned a primary key. If the table is not assigned a primary key, the following error is returned:

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

### Use oss_fdw to read and

**write foreign data files**

This topic describes how to use the oss_fdw plug-in to load data between Object Storage Service (OSS) and PostgreSQL or PPAS databases.

**oss_fdw parameters**

The oss_fdw plug-in uses a method similar to other Foreign Data Wrapper (FDW) interfaces to encapsulate foreign data stored in OSS. You can use oss_fdw to read data stored in OSS. This process is similar to reading data tables. oss_fdw provides unique parameters to connect and parse file data in OSS. oss_fdw can read and write files of the following types in OSS: TXT and CSV files as well as GZIP-compressed TXT and CSV files. The value of each parameter must be enclosed in double quotation marks (") and cannot contain unnecessary spaces.

**CREATE SERVER parameters**

ossendpoint: the endpoint used to access OSS over the internal network, also known as the host. id oss: the AccessKey ID of the OSS account. key oss: the AccessKey secret of the OSS account. bucket: the bucket where the data you want to access is stored. You must create an OSS account before you specify this parameter. The following fault tolerance parameters can be used for data import and export. If network connectivity is poor, you can adjust these parameters to ensure successful import and export. oss_connect_timeout: the connection timeout period. Default value: 10. Unit: seconds. oss_dns_cache_timeout: the DNS timeout period. Default value: 60. Unit: seconds. oss_speed_limit: the minimum data transmission rate. Default value: 1024. Unit: bytes/s. oss_speed_time: the maximum waiting period during which the data transmission rate is lower than the minimum value. Default value: 15. Unit: seconds. If the default values of oss_speed_limit and oss_speed_time are used, a timeout error occurs when the transmission rate is lower than 1,024 bytes/s for 15 consecutive seconds.

**CREATE FOREIGN TABLE parameters**

filepath: a file name that contains a path in OSS. The file name specified by this parameter contains the directory name but not the bucket name. This parameter matches multiple files in the corresponding path in OSS. You can load multiple files to a database. You can import files that adhere to the filepath or filepath.x format to a database. The values of x must be consecutive numbers starting from 1. For example, among the files named filepath, filepath.1, filepath.2, filepath.3, and filepath.5, the first four files are matched and imported. The filepath.5 file is not imported. dir: the virtual file directory in OSS. The specified directory must end with a forward slash (/). All files (excluding subfolders and files in subfolders) in the virtual file directory specified by dir are matched and imported to a database. prefix: the prefix of the path name corresponding to the data file. The prefix does not support regular expressions. The prefix, filepath, and dir parameters are mutually exclusive. Therefore, only one of them can be specified at a time. format: the file format, which can only be CSV. encoding: the file data encoding format. It supports common PostgreSQL encoding formats, such as UTF-8. parse_errors: the fault-tolerant parsing mode. If an error occurs during the parsing process, the entire row of data is ignored. delimiter: the string used to delimit columns. quote: the quote character for files. escape: the escape character for files. null: sets the column matching the specified string to null. For example, null 'test' is used to set the value of the 'test' column to null. force_not_null: sets the value of a column to a non-null value. For example, force_not_null 'id' is used to set the value of the 'id' column to empty strings. compressiontype: the format of the files to be read or written in OSS. none: The files are uncompressed. This is the default value. gzip: The files are compressed in the GZIP format. compressionlevel: the degree to which data files written to OSS are compressed. Valid values: 1 to 9. Default value: 6. You must specify filepath and dir in the OPTIONS parameter. You must specify filepath or dir. The export mode can only be dir.

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

## Use Pgpool for read/write

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

**Warning**

If you use a new disk, you must verify that the new disk belongs to the vdb partition instead of the vda partition. If the new disk belongs to the vda partition, data may be deleted from the new disk.

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
Pgpool-II is installed on the same ECS instance as the database server where PostgreSQL resides. If you specify the 127.0.0.1 IP address in the pg_hba.conf file, you must enter the correct password to ensure a successful logon.

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
If you connect to your ApsaraDB RDS instances by using Pgpool, you must configure the pool_passwd file. This is because Pgpool supports the authentication protocol of PostgreSQL. e splitting in ApsaraDB RDS for P ostgreSQL

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
The pcp.conf file is used to manage the users and passwords of Pgpool. It is not related to the users and passwords of your ApsaraDB RDS instances.

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

If you want to view the logs of Pgpool, run the following command:

```
less /var/log/messages
```

8. Use Pgpool to connect to your ApsaraDB RDS instances.

```
psql -h 127.0.0.1 -p 8001 -U digoal postgres
```

e splitting in ApsaraDB RDS for P ostgreSQL

**FAQ**

Q: How do I test whether read/write splitting is enabled? A: You can connect to your ApsaraDB RDS instances by using Pgpool and call the pg_is_in_recovery() function. Then, close the connection, establish a connection again, and call the pg_is_in_recovery() function again. If you receive a value of false and then a value of true, Pgpool routes requests to your primary ApsaraDB RDS instance and then to your read-only ApsaraDB RDS instances, and read/write splitting is enabled. Q: Does Pgpool increase the latency? A: Pgpool increases the latency slightly. In the test environment you set up in this topic, the latency increases by about 0.12 milliseconds. Q: How does Pgpool check the latency and health on my read-only ApsaraDB RDS instances? A: If the WAL replay latency on a read-only ApsaraDB RDS instance exceeds the specified limit, Pgpool stops routing SQL requests to the read-only instance. Pgpool resumes routing SQL requests to the read-only instance only after it detects that the WAL replay latency on the read-only instance falls below the specified limit. Connect to your primary ApsaraDB RDS instance and query the location where the current WAL data record is written. This location is referred to as log sequence number (LSN) 1. Then, connect to a read-only ApsaraDB RDS instance and query the location where the current WAL data record is replayed. This location is referred to as LSN 2. You can obtain the number of bytes between LSN 1 and LSN 2. This number indicates the latency. Pgpool monitors the health of your read-only ApsaraDB RDS instances. If a read-only instance is unhealthy, Pgpool stops routing requests to the read-only instance. Q: How do I stop Pgpool and reload the configuration of Pgpool? A: Run the `pgpool --help` command to obtain more information about the commands used in Pgpool. Example:

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

## Use ShardingSphere to

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

config-encrypt.yaml: the data encryption configuration file. config-master_slave.yaml: the read/write splitting configuration file. config-sharding.yaml: the data sharding configuration file. server.yaml: the common configuration file.
3. Modify the configuration files.
For more information about the configuration files, see ShardingSphere documentation. In this example, the data sharding and common configuration files are used. Example of a data sharding configuration file: develop ApsaraDB RDS for Postgr eSQL

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

Example of a common configuration file: develop ApsaraDB RDS for Postgr eSQL

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

develop ApsaraDB RDS for Postgr eSQL When you create a table, the system automatically creates horizontal shards in the specific database based on the sharding strategy that you specify.

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
