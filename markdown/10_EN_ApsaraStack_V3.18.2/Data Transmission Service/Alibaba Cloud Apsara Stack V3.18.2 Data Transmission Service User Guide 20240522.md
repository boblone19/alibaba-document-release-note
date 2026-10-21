---
title: "Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service User Guide 20240522"
product_version: "V3.18.2"
doc_version: "20240522"
pdf_pages: 458
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service User Guide 20240522.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93DTS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Data%20Transmission%20Service%20User%20Guide%2020240522.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Data Transmission Service User Guide 20240522

## Table of Contents

- 1 What is DTS?
- 2 Log on to the DTS console
- 3 Data migration
  - 3.1 Supported databases and migration types
  - 3.2 Create a data migration instance
  - 3.3 Prepare the database accounts for data migration
  - 3.4 Configure data migration tasks
    - 3.4.1 Migrate data from a self-managed MySQL database to an ApsaraDB RDS for MySQL instance
    - 3.4.2 Migrate data from a self-managed MySQL database to a self-managed Kafka cluster
    - 3.4.3 Migrate data from an ApsaraDB RDS for MySQL instance to a PolarDB-X 1.0 instance
    - 3.4.4 Migrate data from an ApsaraDB RDS for MySQL instance to a self-managed Oracle database
    - 3.4.5 Migrate data from a self-managed SQL Server database to an ApsaraDB RDS for SQL Server instance
    - 3.4.6 Migrate data from an ApsaraDB RDS for SQL Server database to an ApsaraDB RDS for MySQL database
    - 3.4.7 Migrate data between self-managed Oracle databases
    - 3.4.8 Migrate data from a self-managed Oracle database to an ApsaraDB RDS for MySQL instance
    - 3.4.9 Migrate data from a self-managed Oracle database to a PolarDB for PostgreSQL (Compatible with Oracle) cluster
    - 3.4.10 Migrate data from a self-managed Oracle database to a PolarDB-X 1.0 instance
    - 3.4.11 Migrate data from a self-managed Oracle database to an AnalyticDB for PostgreSQL instance
    - 3.4.12 Migrate data from a self-managed Oracle database to a self-managed PostgreSQL database
    - 3.4.13 Migrate data between ApsaraDB RDS for PostgreSQL instances
    - 3.4.14 Migrate data from an ApsaraDB RDS for PostgreSQL instance to an ApsaraDB RDS for MySQL instance
    - 3.4.15 Migrate data between PolarDB for PostgreSQL (Compatible with Oracle) clusters
    - 3.4.16 Migrate data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to a self-managed Oracle database
    - 3.4.17 Migrate data from a PolarDB for PostgreSQL cluster that is compatible with Oracle to a self-managed Kafka cluster
    - 3.4.18 Migrate data between self-managed Redis databases
    - 3.4.19 Migrate data between self-managed MongoDB databases
    - 3.4.20 Migrate data from a MaxCompute project to a MySQL database
    - 3.4.21 Migrate data from a PolarDB-X 2.0 instance
      - 3.4.21.1 Migrate data between PolarDB-X 2.0 instances
      - 3.4.21.2 Migrate data from a PolarDB-X 2.0 instance to a MySQL instance
      - 3.4.21.3 Migrate data from a PolarDB-X 2.0 instance to a Message Queue for Apache Kafka instance
      - 3.4.21.4 Migrate data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance
  - 3.5 Manage data migration tasks
    - 3.5.1 Object name mapping
    - 3.5.2 Specify an SQL condition to filter data
    - 3.5.3 Troubleshoot a failed data migration task
    - 3.5.4 Specify the capitalization of object names in the destination instance
    - 3.5.5 Data formats of a Kafka cluster
    - 3.5.6 Specify the policy for migrating data to Kafka partitions
    - 3.5.7 Configure ETL in a data migration task
  - 3.6 Precheck items
    - 3.6.1 Source database connectivity
    - 3.6.2 Destination database connectivity
    - 3.6.3 Binary logging configurations of the source database
    - 3.6.4 Integrity of the FOREIGN KEY constraints
    - 3.6.5 Existence of FEDERATED tables
    - 3.6.6 Permissions
    - 3.6.7 Object name conflict
    - 3.6.8 Schema existence
    - 3.6.9 Value of server_id in the source database
    - 3.6.10 Source database version
  - 3.7 Data type mappings between heterogeneous databases
  - 3.8 Create an account for a self-managed MySQL database and configure binary logging
  - 3.9 Enable logging and grant fine-grained permissions to an Oracle database account
  - 3.10 Configure RAM authorization for cross-account data migration or synchronization
- 4 Data synchronization
  - 4.1 Supported database types, initial synchronization types, and synchronization topologies
  - 4.2 Create a data synchronization instance
  - 4.3 Synchronization topologies
  - 4.4 Prepare the database accounts for data synchronization
  - 4.5 Configure data synchronization tasks
    - 4.5.1 Synchronize data between ApsaraDB RDS for MySQL instances
    - 4.5.2 Synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project
    - 4.5.3 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL V3.0 cluster
    - 4.5.4 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance
    - 4.5.5 Synchronize data between ApsaraDB RDS for PostgreSQL instances
    - 4.5.6 Synchronize data from a self-managed PostgreSQL database to an AnalyticDB for PostgreSQL instance
    - 4.5.7 Synchronize data from an ApsaraDB RDS for SQL Server database to a DataHub instance
    - 4.5.8 Synchronize data between PolarDB-X 1.0 instances
    - 4.5.9 Synchronize data from a PolarDB-X 1.0 instance to an AnalyticDB for MySQL V3.0 cluster
    - 4.5.10 Synchronize data from a PolarDB-X 1.0 instance to a DataHub project
    - 4.5.11 Synchronize data from a self-managed Db2 for LUW database to an AnalyticDB for PostgreSQL instance
    - 4.5.12 Synchronize data from a self-managed Oracle database to a DataHub project
    - 4.5.13 Synchronize data from a self-managed Oracle database to a MaxCompute project
    - 4.5.14 Synchronize data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to an AnalyticDB for MySQL V3.0 cluster
    - 4.5.15 Synchronize data between ApsaraDB for Redis instances
    - 4.5.16 Synchronize data from a self-managed MongoDB database to an ApsaraDB for MongoDB instance
    - 4.5.17 Synchronize data between ApsaraDB for MongoDB instances
    - 4.5.18 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances
      - 4.5.18.1 Overview
      - 4.5.18.2 Supported synchronization statements
      - 4.5.18.3 Detect and resolve conflicts
      - 4.5.18.4 Limits on data synchronization
      - 4.5.18.5 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances
    - 4.5.19 Synchronize data between PolarDB-X 2.0 instances
    - 4.5.20 Synchronize data from a PolarDB-X 2.0 instance to an ApsaraDB RDS for MySQL instance
    - 4.5.21 Synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance
    - 4.5.22 Synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for MySQL V3.0 cluster
  - 4.6 Manage data synchronization instances
    - 4.6.1 Rename an object to be synchronized
    - 4.6.2 Use SQL conditions to filter data
    - 4.6.3 Add an object to a data synchronization task
    - 4.6.4 Remove an object from a data synchronization task
    - 4.6.5 Specify the capitalization of object names in the destination instance
    - 4.6.6 Troubleshoot precheck failures
    - 4.6.7 Configure ETL in a data synchronization task
  - 4.7 Best practices for data synchronization from PolarDB-X instances
    - 4.7.1 Precautions and limits for synchronizing data between PolarDB-X instances
    - 4.7.2 Solutions of data synchronization from a PolarDB-X instance
- 5 Change tracking
  - 5.1 Overview
  - 5.2 Create a change tracking instance
  - 5.3 Configure change tracking tasks
    - 5.3.1 Track data changes from an ApsaraDB RDS for MySQL instance
    - 5.3.2 Track data changes from a PolarDB-X 1.0 instance
    - 5.3.3 Track data changes from a self-managed Oracle database
  - 5.4 Manage change tracking tasks
    - 5.4.1 Modify the objects for change tracking
    - 5.4.2 Add consumer groups
    - 5.4.3 Manage consumer groups
  - 5.5 Use the SDK to consume tracked data
    - 5.5.1 Methods provided by SDK
    - 5.5.2 Quick start
    - 5.5.3 Parse tracked SQL statements
    - 5.5.4 Run the SDK demo code
  - 5.6 Use a Kafka client to consume tracked data

## 1 What is DTS?

Data Transmission Service (DTS) is a data service that is provided by Alibaba Cloud. DTS supports data transmission between various types of data sources, such as relational databases and big data systems. Compared with traditional data migration or synchronization tools, DTS provides diverse features and high performance, security, reliability, and ease of use. DTS helps you simplify data transmission and focus on your application development. nsole

## 2 Log on to the DTS console

This topic describes how to log on to the Data Transmission Service (DTS) console. Google Chrome is used in this example.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. The Chrome browser is used.

> **Note:** DTS does not support the IE mode of the Edge browser.

**Procedure**

1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Operations Console User Guide** .

5. In the top navigation bar, choose **Products > Data Transmission Service**.
6. On the page that appears, select an organization and a region, and click **Access as**
**Administrator**.

## 3 Data migration

### 3.1 Supported databases and migration types

**migration types**

You can use Data Transmission Service (DTS) to migrate data between homogeneous data sources or between heterogeneous data sources. This feature is suitable for the following scenarios: data migration to Alibaba Cloud, data migration between instances within Alibaba Cloud, and database splitting and scale-out. This topic describes the database types, database versions, and migration types that are supported by data migration.

| Source database | Destination database | Migration type |
|---|---|---|
| Self-managed MySQL database Versions 5.1, 5.5, 5.6, 5.7, and 8.0 ApsaraDB RDS for MySQL All versions | Self-managed MySQL database Versions 5.1, 5.5, 5.6, 5.7, and 8.0 | Schema migration Full data migration Incremental data migration |
|   | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration Incremental data migration |
|   | PolarDB-X 1.0 (formerly known as DRDS) All versions | Full data migration Incremental data migration |
|   | Self-managed Oracle database in a RAC or non-RAC architecture Versions 9i, 10g, 11g, 12c, 18c, and 19c | Schema migration Full data migration Incremental data migration |
|   | AnalyticDB for PostgreSQL (formerly known as HybridDB for PostgreSQL) Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |

|   | Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 Note DTS supports a self- managed PostgreSQL database as the destination database only if the Access Method parameter of the source database is set to Express Connect, VPN Gateway, or Smart Access Gateway, Self- managed Database on ECS, or Database Gateway. | Schema migration Full data migration Incremental data migration |
|---|---|---|
|   | Self-managed Kafka cluster Versions 0.1 to 2.0 | Schema migration Full data migration Incremental data migration |
| ApsaraDB RDS for SQL Server Versions 2012, 2016, and 2017 Self-managed SQL Server database Versions 2005, 2008, 2008 R2, | Self-managed SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, 2016, and 2017 Note DTS does not support SQL Server clusters or SQL Server AOAGs. ApsaraDB RDS for SQL Server Versions 2012, 2014, 2016, and 2017 | Schema migration Full data migration Incremental data migration |
| 2012, 2014, 2016, and 2017 Note DTS does not support SQL Server clusters or SQL Server AlwaysOn availability groups (AOAGs). If the version of the source database is 2005 or 2008, incremental data synchronization is not supported. |   |   |
|   | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration Incremental data migration |
|   | Self-managed Oracle database in a RAC or non-RAC architecture Versions 9i, 10g, 11g, 12c, 18c, and 19c | Schema migration Full data migration Incremental data migration |

| Self-managed Oracle database in a RAC or non-RAC architecture Versions 9i, 10g, 11g, 12c, 18c, and 19c |   |   |
|---|---|---|
|   | PolarDB for PostgreSQL (Compatible with Oracle) Versions 9.3, 9.6, 10, and 11 | Schema migration Full data migration Incremental data migration |
|   | Self-managed MySQL database Versions 5.1, 5.5, 5.6, 5.7, and 8.0 | Schema migration Full data migration Incremental data migration |
|   | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration Incremental data migration |
|   | PolarDB-X 1.0 (formerly known as DRDS) All versions | Full data migration Incremental data migration |
|   | AnalyticDB for MySQL (formerly known as HybridDB for MySQL) Version 3.0 | Schema migration Full data migration Incremental data migration |
|   | AnalyticDB for PostgreSQL (formerly known as HybridDB for PostgreSQL) Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |
|   | Self-managed Kafka cluster Versions 0.1 to 2.0 | Schema migration Full data migration Incremental data migration |

|   | Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 ApsaraDB RDS for PostgreSQL Versions 9.4, 10.0, 11.0, 12.0, and 13.0 | Schema migration Full data migration Incremental data migration |
|---|---|---|
| Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 ApsaraDB RDS for PostgreSQL Versions 9.4, 10.0, 11.0, 12.0, and 13.0 | Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 ApsaraDB RDS for PostgreSQL Versions 9.4, 10.0, 11.0, 12.0, and 13.0 | Schema migration Full data migration Incremental data migration |
|   | ApsaraDB RDS for MySQL | Schema migration Full data migration Incremental data migration |
|   | AnalyticDB for PostgreSQL Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |
| PolarDB for PostgreSQL (Compatible with Oracle) Versions 9.3, 9.6, 10, and 11 | Self-managed Kafka cluster Versions 0.1 to 2.0 | Schema migration Incremental data migration |
|   | Self-managed Oracle database in a RAC or non-RAC architecture Versions 9i, 10g, 11g, 12c, 18c, and 19c | Full data migration Incremental data migration |
|   | PolarDB for PostgreSQL (Compatible with Oracle) Versions 9.3, 9.6, 10, and 11 | Schema migration Full data migration Incremental data migration |

| Self-managed Redis database Versions 2.8, 3.0, 3.2, 4.0, and 5.0 | Self-managed Redis database Versions 2.8, 3.0, 3.2, 4.0, and 5.0 | Full data migration Incremental data migration |
|---|---|---|
| Self-managed MongoDB database (replica set architecture) Versions 3.0, 3.2, 3.4, 3.6, 4.0 and 4.2 ApsaraDB for MongoDB instance (replica set or sharded cluster architecture) | Self-managed MongoDB database (replica set or sharded cluster architecture) ApsaraDB for MongoDB instance (replica set or sharded cluster architecture) Note If the source database is an ApsaraDB for MongoDB instance (sharded cluster architecture), the destination database must be an ApsaraDB for MongoDB instance (sharded cluster architecture). | Schema migration Full data migration Incremental data migration |
| MaxCompute All versions | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration |
| PolarDB-X 1.0 (formerly known as DRDS) | AnalyticDB for MySQL Version 3.0 | Schema migration Full data migration Incremental data migration |
|   | Datahub | Schema migration Incremental data migration |
|   | PolarDB-X 2.0 Note The PolarDB-X 2.0 instance must be compatible with MySQL V5.7. | Schema migration Full data migration Incremental data migration |

|   | AnalyticDB for PostgreSQL Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |
|---|---|---|
| PolarDB-X 2.0 |   |   |
|   | Self-managed Kafka cluster Versions 0.1 to 2.0 | Schema migration Full data migration Incremental data migration |
|   | Self-managed MySQL database Versions 5.1, 5.5, 5.6, 5.7, and 8.0 | Schema migration Full data migration Incremental data migration |
| Db2 for LUW | AnalyticDB for PostgreSQL Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |
| Db2 for i (AS/400) | Self-managed MySQL database Versions 5.1, 5.5, 5.6, 5.7, and 8.0 | Schema migration Full data migration Incremental data migration |

### 3.2 Create a data migration instance

**instance**

Before you configure a task to migrate data, you must create a data migration instance. This topic describes how to create a data migration instance in the Data Transmission Service (DTS) console.

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Data Migration**.
3. Click **Create Task**.
4. In the dialog box that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Source Database Type | The type of the source database. For more information about the supported types of source databases, see Supported databases and migration types. |
| Source Region | The region in which the source database resides. Note You cannot change the value of this parameter after you purchase the data migration instance. Exercise caution when you configure this parameter. |
| Destination Database Type | The type of the destination database. For more information about the supported types of destination databases, see Supported databases and migration types. |
| Destination Region | The region in which the destination database resides. Note You cannot change the value of this parameter after you purchase the data migration instance. Exercise caution when you configure this parameter. |
| Quantity | The number of data migration instances that you want to create at a time. |

> **Note:** In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click **Create**.
6. In the message that appears, click **OK**.

### 3.3 Prepare the database accounts for data migration

**accounts for data migration**

When you configure a data migration task, you must specify the accounts of the source and destination databases. The database accounts are used for data migration. Different databases and migration types require different permissions. You must create and authorize database accounts before you configure a data migration task.

**Permissions required for the source database account**

| Database | Required permission | References |
|---|---|---|
| ApsaraDB RDS for MySQL database | Read permissions on the objects to migrate | See the "Create an account on an ApsaraDB RDS for MySQL instance" and "Modify the permissions of a standard account on an ApsaraDB RDS for MySQL instance" sections of User Guide of ApsaraDB RDS for MySQL. |

| Self-managed MySQL database | Schema migration: the SELECT permission on the objects to migrate Full data migration: the SELECT permission on the objects to migrate Incremental data migration: the SELECT permission on the objects to migrate, the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions, and the permissions to create databases and tables. The permissions allow DTS to create a database named dts to record heartbeat data during migration. | See Create an account for a self- managed MySQL database and configure binary logging. |
|---|---|---|
| PolarDB for MySQL database | Read permissions on the objects to migrate | See the "Create a database account" section of User Guide of PolarDB for MySQL. |
| PolarDB for Oracle database | Permissions of a privileged account | See the "Create a database account" section of User Guide of PolarDB. |
| ApsaraDB RDS for SQL Server database | Schema migration: the SELECT permission on the objects to migrate Full data migration: the SELECT permission on the objects to migrate Incremental data migration: the owner permission on the object to migrate Note A privileged account has the required permissions. | See the "Create an account" section of User Guide of ApsaraDB RDS for SQL Server. |
| Self-managed SQL Server database | Schema migration: the SELECT permission on the objects to migrate Full data migration: the SELECT permission on the objects to migrate Incremental data migration: the permissions of the sysadmin role | See CREATE USER. |

| ApsaraDB RDS for PostgreSQL database | Schema migration: the USAGE permission on pg catalog _ Full data migration: the SELECT permission on the objects to migrate Incremental data migration: the permissions of a privileged account. The account must be the owner of the database. Note If the source database runs on an ApsaraDB RDS for PostgreSQL 9.4 instance and you migrate only DML operations, the database account must have the REPLICATION permission. | See the "Create an account" section of User Guide of ApsaraDB RDS for PostgreSQL. |
|---|---|---|
| Self-managed PostgreSQL database | Schema migration: the USAGE permission on pg catalog _ Full data migration: the SELECT permission on the objects to migrate Incremental data migration: permissions of the superuser role | See CREATE USER and GRANT. |
| Self-managed Oracle database | Schema migration: permissions of the schema owner Full data migration: permissions of the schema owner Incremental data migration: permissions of the database administrator (DBA) | See CREATE USER and GRANT. Important If you need to migrate incremental data from an Oracle database but the DBA permission cannot be granted to the database account, you can grant finer-grained permissions to the account. For more information, see Enable logging and grant fine-grained permissions to an Oracle database account. |
| ApsaraDB for MongoDB database | Full data migration: read permissions on the source database Incremental data migration: the read permissions on the source database, the admin database, and the local database | The default value of the name of the authentication database is admin. The database account is the root account. |

| Self-managed MongoDB database | Full data migration: read permissions on the source database Incremental data migration: the read permissions on the source database, the admin database, and the local database | For more information, see db.createUser(). |
|---|---|---|
| KVStore for Redis database | Read permissions on the objects to migrate | See the "Account management" section of User Guide of KVStore for Redis. |
| Self-managed Redis database | The PSYNC or SYNC statement can be executed on the source Redis database. | None |
| Self-managed Db2 database | Schema migration: the SELECT permission on the objects to migrate and the CONNECT permission Full data migration: the SELECT permission on the objects to migrate and the CONNECT permission Incremental data migration: the DBADM authority | See Creating group and user IDs for a Db2 database installation and Authorities overview. |

**Permissions required for the destination database account**

| Database | Required permission | Authorization method |
|---|---|---|
| ApsaraDB RDS for MySQL database | Read and write permissions on the destination database | See the "Create an account on an ApsaraDB RDS for MySQL instance" and "Modify the permissions of a standard account on an ApsaraDB RDS for MySQL instance" sections of User Guide of ApsaraDB RDS for MySQL. |
| PolarDB for MySQL database | Read and write permissions on the destination database | See the "Create a database account" section of User Guide of PolarDB for MySQL. |
| Self-managed MySQL database | The ALL permission on the destination database | See Create an account for a self- managed MySQL database and configure binary logging. |

| AnalyticDB for MySQL database | V2.0: DTS automatically creates a database account and grants permissions to the account. You do not need to specify the database account. V3.0: Read and write permissions are required. | V3.0: See the "Database accounts and permissions" section of User Guide of AnalyticDB for MySQL. |
|---|---|---|
| AnalyticDB for PostgreSQL database | The initial account or an account that has the RDS SUPERUSER permission is _ required. | See the "Create a database account" and "Manage users and permissions" sections of User Guide of AnalyticDB for MySQL. |
| PolarDB-X database | Read and write permissions on the destination database | For a PolarDB-X 1.0 instance, see the "Create an account on a PolarDB-X 1.0 instance" and "Modify the permissions of a standard account on a PolarDB-X 1.0 instance" sections of User Guide of PolarDB for Xscale (1.0). For a PolarDB-X 2.0 instance, see the "Manage database accounts" section of User Guide of PolarDB for Xscale. |
| ApsaraDB RDS for SQL Server database | Read and write permissions on the destination database | See the "Create an account" section of User Guide of ApsaraDB RDS for SQL Server. |
| Self-managed SQL Server database | The ALL permission on the destination database | See CREATE USER. |
| ApsaraDB RDS for PostgreSQL database | Schema migration: the CREATE and USAGE permissions on the migrated objects Full data migration: permissions of the schema owner Incremental data migration: the permissions of the schema owner | See the "Create an account" section of User Guide of ApsaraDB RDS for PostgreSQL. |
| Self-managed PostgreSQL database | The ALL permission on the destination database | See CREATE USER and GRANT. |
| PolarDB for Oracle database | Permissions of a privileged account | See the "Create a database account" section of User Guide of PolarDB. |
| Self-managed Oracle database | Permissions of the schema owner | See CREATE USER and GRANT. |

| ApsaraDB for MongoDB database | The dbAdminAnyDatabase permission, read and write permissions on the destination database, and read permissions on the local database | The default value of the name of the authentication database is admin. The database account is the root account. |
|---|---|---|
| Self-managed MongoDB database | Read and write permissions on the destination database and the read permissions on the local database | For more information, see db.createUser(). |
| KVStore for Redis database | If you use the instance password, no authorization is required. | None |
|   | If you use a custom account, the read and write permissions are required. | See the "Account management" section of User Guide of KVStore for Redis. |
| Self-managed Redis database | The database password must be valid. | None |
| Message Queue for Apache Kafka instance | N/A | None |
| Self-managed Kafka cluster | N/A Note If no authentication is enabled for the Kafka cluster, you do not need to enter the username or password. | None |

### 3.4 Configure data migration tasks

**tasks**

#### 3.4.1 Migrate data from a self-managed MySQL database to an ApsaraDB RDS for MySQL instance

**MySQL database to an ApsaraDB RDS for**

**MySQL instance**

This topic describes how to migrate data from a self-managed MySQL database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity.

**Prerequisites**

The engine version of the self-managed MySQL database is 5.1, 5.5, 5.6, 5.7, or 8.0.

> **Note:** To ensure compatibility, the version of the destination database must be the same as or later than that of the source database.

The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of the data in the self-managed MySQL database.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | To ensure compatibility, the version of the destination database must be the same as or later than that of the source database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If the source database is a self-managed MySQL database, take note of the following limits: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. |

**Migration types**

Schema migration DTS migrates the schemas of the required objects to the destination instance. DTS supports schema migration for the following types of objects: table, view, trigger, stored procedure, and function.

> **Note:** During schema migration, DTS changes the value of the SECURITY attribute in views, stored procedures, and functions from DEFINER to INVOKER.
> DTS does not migrate user information. Before a user can call views, stored procedures, and functions of the destination database, you must grant the read/write permissions to the user.

Full data migration DTS migrates historical data of the required objects from the user-created MySQL database to the destination database in the ApsaraDB RDS for MySQL instance.

> **Note:** During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination instance. After full data migration is complete, the tablespace of the destination instance is larger than that of the source database.

Incremental data migration After full data migration is complete, DTS retrieves binary log files from the user-created MySQL database. Then, DTS synchronizes incremental data from the user-created MySQL database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from a user-created MySQL database to Alibaba Cloud.

**SQL operations that can be synchronized during incremental**

**data migration**

| Operati on type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE TRUNCATE TABLE |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the self-managed MySQL database. |
|   | Port Number | The service port number of the self-managed MySQL database. Default value: 3306. |
|   | Database Account | The account of the self-managed MySQL database. If you need to perform incremental data migration, the account must have the SELECT permission on the objects to be migrated, the REPLICATION SLAVE permission, the REPLICATION CLIENT permission, and the SHOW VIEW permission. If you need to perform full data migration or schema migration, the account must have the SELECT permission on the objects to be migrated. |
|   | Database Password | The password of the database account. |
| Destinati on Database | Database Type | The type of the destination database. SelectM ySQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data migration task. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed MySQL database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed MySQL database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with that in the source or destination database. For more information,see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |

| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. To specify WHERE conditions to filter data, right-click a table in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information, see Specify an SQL condition to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information,see Configure ETL in a data migration task. No: does not configure the ETL feature. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.2 Migrate data from a self-managed MySQL database to a self-managed Kafka cluster

**MySQL database to a self-managed Kafka**

**cluster**

Kafka is a distributed message queue service that supports high throughput and high scalability. Kafka is widely used for big data analytics such as log collection, monitoring data aggregation, streaming processing, and online and offline analysis. Kafka is an essential service for the big data ecosystem. You can migrate data from a self-managed MySQL database or an ApsaraDB RDS for MySQL instance to a self-managed Kafka cluster by using Data Transmission Service (DTS). The data migration feature allows you to extend message processing capabilities. This topic describes how to migrate data from a self-managed MySQL database to a self-managed Kafka cluster by using DTS.

**Prerequisites**

The version of the self-managed MySQL database is 5.1, 5.5, 5.6, 5.7, or 8.0. The destination Kafka cluster is created and the Kafka version is 0.10 to 2.0.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|---|---|

| Other limits | The service port of the Kafka cluster must be accessible over the Internet. You can select only tables as the objects to be migrated. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Data format**

The data that is migrated to the Kafka cluster is stored in the Avro format. You must parse the data based on the schema definition of DTS Avro. For more information, visit GitHub.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to access the self-managed MySQL database. |

|   | Port Number | The service port number of the self-managed MySQL database. Default value: 3306. |
|---|---|---|
|   | Database Account | The account of the self-managed MySQL database. The account must have the SELECT permission on the objects to be migrated and the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination cluster. Select Kafka. |
|   | Access Method | The access method of the destination cluster. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination cluster resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP Address | The IP address that is used to access the self-managed Kafka cluster. In this example, the public IP address is used. |
|   | Port Number | The service port number of the Kafka cluster. Default value: 9092. |
|   | Database Account | The username that is used to log on to the Kafka cluster. If no authentication is enabled for the Kafka cluster, you do not need to enter the username. |
|   | Database Password | The password of the username. If no authentication is enabled for the Kafka cluster, you do not need to enter the password. |
|   | Kafka Version | The version of the destination Kafka cluster. Note You cannot select Kafka 2.0 in the DTS console. If you are using Kafka 2.0, you must select Kafka 1.0. |
|   | Encryption | Specifies whether to encrypt the connection to the destination cluster. Select Non-encrypted or SCRAM-SHA-256 based on your business and security requirements. |
|   | Topic | The name of the destination topic. Select a value from the drop- down list. |
|   | Topic That Stores DDL Informatio n | The name of the topic that stores the DDL information. Select a value from the drop-down list. If you do not set this parameter, the DDL information is stored in the topic that is specified by the Topic parameter. |

|   | Use Kafka Schema Registry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |
|---|---|---|

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed MySQL database or self-managed Kafka
cluster, add the CIDR blocks of DTS servers that are displayed in the dialog box to the whitelist of the self-managed MySQL database or self-managed Kafka cluster. Then, click
**Test Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for your self-managed MySQL database or self-managed Kafka cluster, ignore the preceding settings and click **Test** **Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Data Format in Kafka | The format in which data records are stored in the Message Queue for Apache Kafka instance. If you select DTS Avro, data is parsed based on the schema definition of DTS Avro. For more information, see GitHub. If you select Canal Json, data is parsed into the Canal JSON format. For more information about the parameters that are used to parse data into the Canal JSON format and the sample code, see Canal Json. |
|---|---|
| Policy for Shippin g Data to Kafka Partitio ns | Select a policy for data migration to Kafka partitions based on your business requirements. For more information, see Specify the policy for migrating data to Kafka partitions. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select only tables as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |
|---|---|

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.3 Migrate data from an ApsaraDB RDS for MySQL instance to a PolarDB-X 1.0 instance

**MySQL instance to a PolarDB-X 1.0 instance**

This topic describes how to migrate data from an ApsaraDB RDS for MySQL instance to a PolarDB-X 1.0 instance by using Data Transmission Service (DTS). PolarDB-X is formerly known as Distributed Relational Database Service (DRDS).

**Prerequisites**

The available storage space of the destination PolarDB-X 1.0 instance is larger than the total size of the data in the source ApsaraDB RDS for MySQL instance.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set _ to row and the binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data migration task cannot be started. For more information, see the "Modify instance parameters" topic in the documentation of ApsaraDB RDS for MySQL. Binary logs are stored for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data consistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration. Incremental DDL operations cannot be migrated. If you perform DDL operations on the source database during incremental data migration, the data migration task fails. If you want to perform DDL operations, we recommend that you perform the operations in the destination database and then perform the same operations in the source database. |
|---|---|

| Other limits | The storage type of the PolarDB-X instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If the source database is a self-managed MySQL database, take note of the following limits: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

**SQL operations that can be incrementally migrated**

INSERT, UPDATE, and DELETE

**Permissions required for database accounts**

| Database | Full data migration | Incremental data migration |
|---|---|---|

| ApsaraDB RDS for MySQL instance | Read and write permissions | Read and write permissions |
|---|---|---|
| PolarDB-X 1.0 instance | Read and write permissions | Read and write permissions |

**Procedure**

1. Create databases and tables in the destination PolarDB-X instance based on the schemas of
the source tables in the ApsaraDB RDS for MySQL instance.
2. Create a data migration instance.
3. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
4. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. In this example, No is selected. Note If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the RAM role, see Configure RAM authorization for cross-account data migration or synchronization. |

|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|---|---|---|
|   | Database Account | The database account of the ApsaraDB RDS for MySQL instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data migration task. |
| Destinati on Database | Database Type | The type of the destination database. SelectP olarDB-X 1.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the destination PolarDB-X 1.0 instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |

5. In the lower part of the page, click **Test Connectivity and Proceed**.
6. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Parame ter | Description |
|---|---|

| Task Stages | To perform only full data migration, select Full Data Migration. To ensure service continuity during data migration, select Full Data Migration and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select columns, tables, or databases as the objects to be migrated. |

| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.4 Migrate data from an ApsaraDB RDS for MySQL instance to a self-managed Oracle database

**MySQL instance to a self-managed Oracle**

**database**

This topic describes how to migrate data from an ApsaraDB RDS for MySQL instance to a selfmanaged Oracle database by using Data Transmission Service (DTS). DTS supports full data migration and incremental data migration. You can select the two migration types to ensure service continuity of the source ApsaraDB RDS for MySQL instance during data migration.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set _ to row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |
|---|---|

| Other limits | Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Permissions required for database accounts**

| Migration type | Full data migration | Incremental data migration |
|---|---|---|
| Source ApsaraDB RDS for MySQL instance | Read and write permissions | Read and write permissions |
| Destination Oracle database | Read and write permissions | Read and write permissions on databases |

**Procedure**

1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click **Configure Task** in the Actions
column.
3. Optional. Enter a name for the task.
DTS automatically generates a name for each task. Duplicate task names are allowed. You can edit the task name based on your business requirements. We recommend that you specify a descriptive name for easy identification.
4. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
|   | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source instance resides. |

| ta Transmission Servi |   |   |
|---|---|---|
| Source Database |   |   |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | RDS Instance ID | The ID of the database that you want to migrate. |
|   | Database Account | The account that has read and write permissions on the source database. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data migration task. |
| Destination Database | Database Type | The type of the destination database. SelectO racle. |
|   | Access Method | The access method of the destination database. Select Public IP Address. |
|   | Instance Region | The region in which the destination database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the destination database. |
|   | Port Number | The port number of the destination database. Default value: 1521. |
|   | Oracle Type | The architecture of the destination Oracle database. If you select Non-RAC Instance, you must specify the SID parameter. If you select RAC or PDB Instance, you must specify the Service Name parameter. |
|   | Database Account | The account that has the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

5. In the lower part of the page, click **Test Connectivity and Proceed**.
6. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

7. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To ensure service continuity during data migration, select Full Data Migration and Incremental Data Migration. To perform only full data migration, select Full Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with that in the source or destination database. For more information,see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |

| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click an object in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information about how to specify the conditions, see Specify an SQL condition to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|

8. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information,see Configure ETL in a data migration task. No: does not configure the ETL feature. |

9. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

0. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.5 Migrate data from a self-managed SQL Server database to an ApsaraDB RDS for SQL Server instance

**Server database to an ApsaraDB RDS for SQL**

**Server instance**

This topic describes how to migrate incremental data from a self-managed SQL Server database to an ApsaraDB RDS for SQL Server instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity.

**Prerequisites**

The version of the self-managed SQL Server database is 2005, 2008, 2008 R2, 2012, 2014, 2016, or 2017.

> **Note:** DTS does not support SQL Server clusters or SQL Server Always On availability groups (AOAGs).
> If the version of the source database is SQL Server 2005, incremental data migration is not supported.
> To ensure compatibility, the version of the destination database must be the same as or later than the version of the source database.

The tables to be migrated from the self-managed SQL Server database have primary keys or UNIQUE NOT NULL indexes.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. The backup mode must be set to Full, and full logical backup must be performed. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|---|---|

| Other limits | A data migration task can migrate incremental data from only one database. To migrate incremental data from multiple databases, you must create a data migration task for each database. DTS does not migrate data of the following types: CURSOR, ROWVERSION, SQL VARIANT, HIERACHYID, and GEOMETRY. _ DTS does not migrate heap tables, tables that contain non-clustered indexes, or tables that contain computed columns. To ensure compatibility, the version of the destination database must be the same as or later than the version of the source database. To ensure that the latency of incremental data migration is accurate, DTS adds a heartbeat table to the self-managed SQL Server database. The name of the heartbeat table is in the source table name dts mysql heartbeat format. _ _ _ If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If the destination instance is an ApsaraDB RDS for SQL Server instance, take note of the following limits: DTS automatically creates a destination database in the ApsaraDB RDS for SQL Server instance. However, if the name of the database to be migrated does not conform to the naming conventions of ApsaraDB RDS, you must manually create a database in the destination ApsaraDB RDS for SQL Server instance before you configure the data migration task. |

**Migration types**

Schema migration DTS migrates the schemas of the required objects from the source database to the destination database. DTS supports schema migration for the following types of objects: table, view, trigger, synonym, SQL stored procedure, SQL function, plan guide, user-defined type, rule, and default. Full data migration DTS migrates historical data of objects from the self-managed SQL Server database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the self-managed SQL Server database to the destination database. Incremental data migration allows you to ensure service continuity when you migrate data from a self-managed SQL Server database to an Alibaba Cloud instance.

**SQL operations that can be incrementally migrated**

INSERT, UPDATE, and DELETE

> **Note:** If an UPDATE operation updates only the large fields, DTS does not migrate the operation.

CREATE TABLE

> **Note:** If a CREATE TABLE operation creates a partitioned table or a table that contains functions, DTS does not migrate the operation.

ALTER TABLE, including only ADD COLUMN, DROP COLUMN, and RENAME COLUMN DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX

**Data migration process**

To prevent data migration failures caused by dependencies among objects, DTS migrates the schemas and data from the source SQL Server database in the following order:
1. Migrate the schemas of tables, views, synonyms, user-defined types, rules, defaults, and
plan guides.
2. Perform full data migration.
3. Migrate the schemas of SQL stored procedures, SQL functions, triggers, and foreign keys.
4. Perform incremental data migration.

> **Note:** During incremental data migration, we recommend that you do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated.

**Preparations**

To perform incremental data migration, configure log settings on the self-managed SQL Server database.

> **Note:** Skip this step if you do not need to perform incremental data migration.

1. Run the following command in the user-created SQL Server database to change the
recovery mode to full mode:

```
use master;
```

`GO`

```
ALTER DATABASE <database_name> SET RECOVERY FULL WITH ROLLBACK IMMEDIATE;
```

`GO` Parameters: <database_name>: the name of the source database. Example:

```
use master;
```

`GO`

```
ALTER DATABASE mytestdata SET RECOVERY FULL WITH ROLLBACK IMMEDIATE;
```

`GO`
2. Run the following command to create a logical backup for the source database. Skip this
step if you have already created a logical backup.

```
BACKUP DATABASE <database_name> TO DISK='<physical_backup_device_name>';
```

`GO` Parameters: <database_name>: the name of the source database. <physical_backup_device_name>: the storage path and file name of the backup file. Example:

```
BACKUP DATABASE mytestdata TO DISK='D:\backup\dbdata.bak';
```

`GO`
3. Run the following command to back up the log entries of the source database:

```
BACKUP LOG <database_name> to DISK='<physical_backup_device_name>' WITH init;
```

`GO` Parameters: <database_name>: the name of the source database. <physical_backup_device_name>: the storage path and file name of the backup file. Example:

```
BACKUP LOG mytestdata TO DISK='D:\backup\dblog.bak' WITH init;
```

`GO`

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select SQL Server. |

| ta Transmissi | on Service User Guide·Data migratio |   |
|---|---|---|
| Source Database |   |   |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed SQL Server database. |
|   | Port Number | The service port number of the self-managed SQL Server database. Default value: 1433. |
|   | Database Account | The account that is used to log on to the self-managed SQL Server database. Note To perform incremental data migration, the account must have the sysadmin permission. To perform schema migration or full data migration, the account must have the SELECT permission on the objects to be migrated. In this example, a self-managed SQL Server database is used as the source database. If your source database is an ApsaraDB RDS for SQL Server instance, you must use a privileged database account. |
|   | Database Password | The password of the database account. |
| Destinati on Database | Database Type | The type of the destination database. SelectS QL Server. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination ApsaraDB RDS for SQL Server instance. Note In this scenario, the destination database can be only a SQL Server database. |
|   | Database Account | The database account of the destination ApsaraDB RDS for SQL Server instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed SQL Server database, add the CIDR blocks
of DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed SQL Server database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| SQL Server Increm ental Synchr onizati on Mode | Log-based Parsing for Non-heap Tables and CDC-based Incremental Synchronization for Heap Tables: Advantages: Supports heap tables, tables without primary keys, compressed tables, and tables with computed columns. Provides higher stability and a variety of complete DDL statements. Disadvantages: DTS creates the trigger dts cdc sync ddl, the heartbeat table dts sync progress, _ _ _ _ _ and the DDL storage table dts cdc ddl history in the source database and _ _ _ enables change data capture (CDC) for the source database and specific tables. You cannot execute the SELECT INTO statement on a table for which CDC is enabled in the source database. You cannot manually delete triggers that are created by DTS in the source database. Incremental Synchronization Based on Logs of Source Database: Advantage: Does not modify settings of the source database. Disadvantage: Does not support heap tables, tables without primary keys, compressed tables, or tables with computed columns. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.6 Migrate data from an ApsaraDB RDS for SQL Server database to an ApsaraDB RDS for MySQL database

**SQL Server database to an ApsaraDB RDS for**

**MySQL database**

This topic describes how to migrate data from an ApsaraDB RDS for SQL Server database to an ApsaraDB RDS for MySQL database by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. When you configure a data migration task, you can select all of the supported migration types to ensure service continuity.

**Prerequisites**

The source ApsaraDB RDS for SQL Server instance is created. The destination ApsaraDB RDS for MySQL instance is created. The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of the data in the source ApsaraDB RDS for SQL Server instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. The backup mode must be set to Full, and full logical backup must be performed. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | DTS does not migrate data of the following types: TEXT, CURSOR, ROWVERSION, HIERACHYID, SQL VARIANT, SPATIAL GEOMETRY, and SPATIAL GEOGRAPHY. _ DTS does not migrate heap tables, tables that contain non-clustered indexes, or tables that contain computed columns. If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**SQL operations that can be incrementally migrated**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |
| DDL | CREATE TABLE Note If a CREATE TABLE operation creates a partitioned table or a table that contains functions, DTS does not migrate the operation. ADD COLUMN and DROP COLUMN DROP TABLE CREATE INDEX and DROP INDEX Note DTS does not migrate DDL operations that contain user-defined types. DTS does not migrate online DDL operations. DTS does not migrate transactional DDL operations. |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and the destination database. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select SQL Server. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the RAM role, see the Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source ApsaraDB RDS for SQL Server instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for SQL Server instance. The account must have the owner permissions on the objects to be migrated. A privileged account has the required permissions. |
|   | Database Password | The password of the database account. |

| Destinati on Database | Database Type | The type of the destination database. SelectM ySQL. |
|---|---|---|
|   | Access Method | The access method of the destination database. Default value: Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a RAM role and grant permissions to the RAM role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data migration task. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the objects to be migrated and advanced settings. The following table describes
the parameters.

| Parameter | Description |
|---|---|

| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If you do not select Incremental Data Migration, we recommend that you do not write data to the source database during data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Schema Mapping Mode of Source and Destination Databases | Select a schema mapping mode based on your business requirements. Important If you do not use the schema names of the source database, the source tables must have unique names across different schemas. Otherwise, data inconsistency may occur or the data migration task may fail. |

| SQL Server Incremental Synchronization Mode | Log-based Parsing for Non-heap Tables and CDC-based Incremental Synchronization for Heap Tables: Advantages: Supports heap tables, tables without primary keys, compressed tables, and tables with computed columns. Provides higher stability and a variety of complete DDL statements. Disadvantages: DTS creates the trigger dts cdc sync ddl, the heartbeat table _ _ _ dts sync progress, and the DDL storage table dts cdc ddl history in _ _ _ _ _ the source database and enables change data capture (CDC) for the source database and specific tables. You cannot execute the SELECT INTO statement on a table for which CDC is enabled in the source database. You cannot manually delete triggers that are created by DTS in the source database. Incremental Synchronization Based on Logs of Source Database (Heap tables are not supported): Advantages: Does not modify the settings of the source database. Disadvantages: Does not support heap tables, tables without primary keys, compressed tables, or tables with computed columns. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, the DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select tables as the objects to be migrated. |

| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations to be incrementally migrated, right- click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. For more information about how to specify conditions to filter data, see Specify an SQL condition to filter data. |
|---|---|

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.7 Migrate data between self-managed Oracle databases

**Oracle databases**

This topic describes how to migrate data between self-managed Oracle databases by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the source Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c.

> **Note:** To ensure compatibility, the version of the destination database must be the same as or later than that of the source database.

Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the source Oracle database. For more information, see Supplemental Logging. The source Oracle database is running in ARCHIVELOG mode. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. The available storage space of the destination Oracle database is larger than the total size of the data in the source Oracle database.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|---|---|

| Other limits | If you perform a primary/secondary switchover on the source and destination databases when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Migration types**

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of the required objects to the destination Oracle database. DTS supports schema migration for the following types of objects: table, view, synonym, trigger, stored procedure, function, package, and user- defined type. Note If an object contains triggers, the data between the source and destination databases will become inconsistent. |
| Full data migration | DTS migrates historical data of the required objects from the source Oracle database to the destination Oracle database. Note During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration, DTS retrieves redo log files from the source Oracle database. Then, DTS synchronizes incremental data from the source Oracle database to the destination Oracle database. Incremental data migration allows you to ensure service continuity when you migrate data between Oracle databases. |

**Permissions required for database accounts**

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source Oracle database | Owner permissions on schemas | Owner permissions on schemas | Permissions of database administrator (DBA) |
| Destination Oracle database | Owner permissions on schemas | Owner permissions on schemas | Owner permissions on schemas |

> **Note:** For more information about how to create an Oracle database account and grant the required permissions to the account, see CREATE USER and GRANT.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The port number of the source Oracle database. Default value: 1521. |
|   | Oracle Type | The architecture of the source Oracle database. Select Non-RAC Instance or RAC or PDB Instance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account that is used to connect to the source Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |

| Destinati on Database | Database Type | The type of the destination database. SelectO racle. |
|---|---|---|
|   | Access Method | The access method of the destination database. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the destination Oracle database. |
|   | Port Number | The port number of the destination Oracle database. Default value: 1521. |
|   | Oracle Type | The architecture of the destination Oracle database. SelectN on- RAC Instance or RAC or PDB Instance based on the architecture of the destination Oracle database. |
|   | SID | The SID of the destination Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account that is used to connect to the destination Oracle database. The account must have the read and write permissions on the database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter or setting | Description |
|---|---|

| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Select the process ing mode of conflict ing tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or schemas as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Specify the retry time range for failed connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.8 Migrate data from a self-managed Oracle database to an ApsaraDB RDS for MySQL instance

**Oracle database to an ApsaraDB RDS for**

**MySQL instance**

This topic describes how to migrate data from a self-managed Oracle database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. When you migrate data from a self-managed Oracle database, you can select all the supported migration types to ensure service continuity.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: Table names in the ApsaraDB RDS for MySQL instance are case-insensitive. If a table name in the source Oracle database contains uppercase letters, ApsaraDB RDS for MySQL converts all uppercase letters to lowercase letters before a table is created. If the source Oracle database contains identical table names that differ only in capitalization, these table names are identified as duplicate. As a result, the "The object already exists" message may be displayed during schema migration. To prevent name conflicts in the destination database, you can use the object name mapping feature to capitalize the table names. For more information, see Object name mapping. DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. |

**Migration types**

Schema migration DTS supports schema migration for tables and indexes. DTS does not support schema migration for the following types of objects: view, synonym, trigger, stored procedure, function, package, and user-defined type. DTS has the following limits on schema migration for tables and indexes: Schema migration of nested tables is not supported. Clustered tables and indexorganized tables (IOTs) are converted into common tables in the destination database. Schema migration of function-based indexes, domain indexes, bitmap indexes, and reverse indexes is not supported. Full data migration DTS migrates historical data of the required objects from the user-created Oracle database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration DTS retrieves redo log files from the user-created Oracle database. Then, DTS synchronizes incremental data from the user-created Oracle database to the destination database in the ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from the user-created Oracle database to the destination database.

**SQL operations that can be incrementally migrated**

INSERT, DELETE, and UPDATE CREATE TABLE

> **Note:** DTS does not migrate the CREATE TABLE operations that are performed to create tables in which functions are nested.

ALTER TABLE, ADD COLUMN, DROP COLUMN, RENAME COLUMN, and ADD INDEX DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX

**Data type mappings**

For more information about, see Data type mappings between heterogeneous databases.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The port number of the source Oracle database. The default port number is 1521. |
|   | Oracle Type | The Oracle data type. Select Non-RAC Instance or RAC or PDB Instance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |

|   | Database Account | The account that is used to connect to the source Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|---|---|---|
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectM ySQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination instance resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
| Destinati on Database |   |   |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data migration task. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, the DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. No: does not configure the ETL feature. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.9 Migrate data from a self-managed Oracle database to a PolarDB for PostgreSQL (Compatible with Oracle) cluster

**Oracle database to a PolarDB for PostgreSQL**

**(Compatible with Oracle) cluster**

This topic describes how to migrate data from a self-managed Oracle database to a PolarDB for PostgreSQL (Compatible with Oracle) cluster by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Limits on features**

During schema migration, the reverse indexes and bitmap indexes of the source database are stored as common indexes in the PolarDB for PostgreSQL (Compatible with Oracle) cluster. During schema migration, partitioned indexes are converted into independent indexes on each partition in the PolarDB for PostgreSQL (Compatible with Oracle) cluster. Incremental data migration supports only tables that have primary keys or UNIQUE NOT NULL indexes. Data of the LONG type cannot be migrated during incremental data migration. DDL operations that are performed during incremental data migration cannot be migrated to the destination database. DTS does not migrate materialized views.

**Data type mappings**

For more information, see Data type mappings between heterogeneous databases.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select Oracle. |

| ta Transmissi | on Service User Guide·Data migratio |   |
|---|---|---|
| Source Database |   |   |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The port number of the source Oracle database. The default port number is 1521. |
|   | Oracle Type | The Oracle data type. Select Non-RAC Instance or RAC or PDB Instance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectP olarDB (Compatible with Oracle). |
|   | Access Method | The access method of the destination cluster. SelectP ublic IP Address. |

| Destinati on Database |   |   |
|---|---|---|
|   | Instance Region | The region in which the destination cluster resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Data Sources | Single Data Source: If you select this option, you must configure the Domain Name or IP Address and Port Number parameters of the primary node in the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. Multiple Data Sources: If you select this option, you must specify the IP addresses and port numbers of multiple nodes, including the primary node, in the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster in the IP:Port of Data Sources field. Note If you select Multiple Data Sources and configure the IP:Port of Data Sources parameter, DTS can automatically switch to a new primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster during primary/secondary switchover. This is suitable for scenarios such as disaster recovery. |
|   | Domain Name or IP Address | The endpoint of the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Port Number | The service port number of the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. Default value: 1521. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Specify the retry time range for failed connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.10 Migrate data from a self-managed Oracle database to a PolarDB-X 1.0 instance

**Oracle database to a PolarDB-X 1.0 instance**

This topic describes how to migrate data from a self-managed Oracle database to a PolarDB-X 1.0 instance by using Data Transmission Service (DTS). DTS allows you to ensure service continuity when you perform full data migration and incremental data migration.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Migration types**

Full data migration DTS migrates the historical data of objects from the source Oracle database to the destination database. Incremental data migration After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database.

> **Note:** The following SQL operations can be migrated during incremental data migration: INSERT, DELETE, and UPDATE operations. DDL operations cannot be migrated during incremental data migration.

**Procedure**

1. Create databases and tables in the destination PolarDB-X 1.0 instance based on the
schemas of the source tables.

> **Note:** The data types of Oracle and PolarDB-X 1.0 do not have one-to-one correspondence. You must create the corresponding data types in the destination instance. For more information, see Data type mappings between heterogeneous databases.

2. Create a data migration instance.
3. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The service port number of the source Oracle database. The default port number is 1521. |
|   | Oracle Type | The Oracle data type. Select Non-RAC Instance or RAC or PDB Instance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
| Document Ver | sion: 20240522 8 |   |

|   | Database Password | The password of the database account. |
|---|---|---|
| Destinati on Database | Database Type | The type of the destination database. SelectP olarDB-X 1.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination instance resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the destination PolarDB-X 1.0 instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

5. In the lower part of the page, click **Test Connectivity and Proceed**.
6. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

7. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Full Data Migration. To ensure service continuity during data migration, select Full Data Migration and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

8. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Specify the retry time range for failed connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

9. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

0. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.11 Migrate data from a self-managed Oracle database to an AnalyticDB for PostgreSQL instance

**Oracle database to an AnalyticDB for**

**PostgreSQL instance**

This topic describes how to migrate data from a self-managed Oracle database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data migration feature allows you to transfer and analyze data with ease.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

**Migration types**

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of required objects from the source database to the destination database. DTS supports schema migration for the following types of objects: table, index, constraint, function, sequence, and view. Warning In this topic, the source and the destination databases are heterogeneous databases. DTS does not ensure that the schemas of the source and destination databases are consistent after schema migration. We recommend that you evaluate the impact of data type conversion on your business. For more information, see Data type mappings between heterogeneous databases. For partitioned tables, DTS discards the partition definitions. You must define partitions in the destination database. |
| Full data migration | DTS migrates the historical data of required objects from the source database to the destination database. Note During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database in real time. DTS can migrate the following SQL operations during incremental data migration: DML operations: INSERT, UPDATE, and DELETE DDL operation: ADD COLUMN Incremental data migration ensures service continuity of self-managed applications during data migration. |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Oracle Type | The type of the source Oracle database. Select Non-RAC Instance or RAC or PDB Instance based on the data type of the self- managed Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter must be specified if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter must be specified if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account that is used to connect to the source Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destinati on | Database Type | The type of the destination database. SelectA nalyticDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination AnalyticDB for PostgreSQL instance resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |

| er Guide·Data |   |   |
|---|---|---|
| on Database |   |   |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination AnalyticDB for PostgreSQL instance. The account must have the read and write permissions on the instance. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
|---|---|
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. No: does not configure the ETL feature. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.12 Migrate data from a self-managed Oracle database to a self-managed PostgreSQL database

**Oracle database to a self-managed**

**PostgreSQL database**

This topic describes how to migrate data from a self-managed Oracle database to a selfmanaged PostgreSQL database by using Data Transmission Service (DTS). Schema migration, full data migration, and incremental data migration ensure service continuity when you perform data migration.

**Prerequisites**

A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source and destination databases when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

**Migration types**

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of required objects from the source database to the destination database. DTS can migrate the following objects: tables, views, and indexes. |
| Full data migration | DTS migrates the historical data of required objects from the source database to the destination database. Note During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database in real time. DTS can migrate the following SQL operations during incremental data migration: DML operations: INSERT, UPDATE, and DELETE Incremental data migration ensures service continuity of self-managed applications during data migration. |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source D t b | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The port number of the source Oracle database. Default value: 1521. |
|   | Oracle Type | The type of the source Oracle database. Select Non-RAC Instance or RAC or PDB Instance based on the data type of the self- managed Oracle database. |

| Database |   |   |
|---|---|---|
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as Oracle Type. |
|   | Service Name | The server name of the database. Note This parameter is required if you select RAC or PDB Instance as Oracle Type. |
|   | Database Account | The account that is used to connect to the source Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destinati on Database | Database Type | The type of the destination database. SelectP ostgreSQL. |
|   | Access Method | The access method of the destination database. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the destination PostgreSQL database. |
|   | Port Number | The service port number of the self-managed PostgreSQL database. Default value: 3433. |
|   | Database Name | The name of the self-managed PostgreSQL database to which you want to migrate objects. |
|   | Database Account | The account of the self-managed PostgreSQL database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle and PostgreSQL databases, add the
CIDR blocks of DTS servers that are displayed in the dialog box to the whitelist. Then, click
**Test Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your self-managed Oracle and PostgreSQL databases, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|

| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|---|---|
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. No: does not configure the ETL feature. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.13 Migrate data between ApsaraDB RDS for PostgreSQL instances

**for PostgreSQL instances**

This topic describes how to migrate data between ApsaraDB RDS for PostgreSQL instances by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity.

**Prerequisites**

The source and destination ApsaraDB RDS for PostgreSQL instances are created.

> **Note:** To ensure compatibility, the version of the destination database must be the same as or later than that of the source database. If the version of the destination database is earlier than that of the source database, database compatibility issues may occur.

The available storage space of the destination ApsaraDB RDS for PostgreSQL instance is larger than the total size of the data in the source ApsaraDB RDS for PostgreSQL instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature is enabled. Data logs are stored for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, the DTS server stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, the DTS server automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain WAL logs that were generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations that are performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during full data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

|   | Data Transmission S | ervice User Guide·Data migratio |
|---|---|---|
|   | Other limits | To ensure that the data migration task runs as expected, you can perform primary/secondary switchover only on an ApsaraDB RDS for PostgreSQL V11 instance during data migration. In this case, you must set the rds failover slot mode parameter to sync . _ _ _ Warning If you perform a primary/secondary switchover on an ApsaraDB RDS for PostgreSQL instance of another version during data migration, the task fails. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. The name of the source database cannot contain hyphens (-). For example, dts- testdata is not allowed. DTS does not check the validity of metadata such as sequences. You must manually check the validity of metadata. Data may be inconsistent between the primary and secondary nodes of the source database due to the latency of incremental data migration. Therefore, you must use the primary node as the data source when you migrate data. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. If you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename the table during incremental data migration, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding sample statement with your actual schema name and table name. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source _ _ database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During incremental data migration, DTS creates a replication slot for the source database. The replication slot is prefixed with dts sync . DTS _ _ automatically clears historical data in the replication slot every 90 minutes to reduce storage usage. |

|   | Note If the data migration task is released or fails, DTS automatically clears the replication slot. If a primary/secondary switchover is performed on the source ApsaraDB RDS for PostgreSQL instance, you must log on to the secondary database to manually clear the replication slot. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. After your workloads are switched to the destination database, newly written sequences do not increment from the maximum value of the sequences in the source database. Therefore, you must query the maximum value of the sequences in the source database before you switch your workloads to the destination database. Then, you must specify the queried maximum value as the starting value of the sequences in the destination database. For more information, see the Statements to query the maximum value of the sequences |
|---|---|
| Special cases | in the source database section of this topic. If the source or destination instance is an ApsaraDB RDS for PostgreSQL instance, take note of the following limits: During data migration, do not modify the endpoint and zone of the ApsaraDB RDS for PostgreSQL instance. Otherwise, the data migration task fails. |

**Statements to query the maximum value of the sequences in**

**the source database**

```
do language plpgsql $$ declare
  nsp name;
  rel name;
  val int8;
begin
  for nsp,rel in select nspname,relname from pg_class t2 , pg_namespace t3 where t2.rel
namespace=t3.oid and t2.relkind='S'
  loop
    execute format($_$select last_value from %I.%I$_$, nsp, rel) into val;
    raise notice '%',
    format($_$select setval('%I.%I'::regclass, %s);$_$, nsp, rel, val+1);
  end loop;
end; $$;
```

**Data migration process**

The following table describes how DTS migrates the schemas and data of the source ApsaraDB RDS for PostgreSQL instance. The process prevents data migration failures that are caused by dependencies between objects.

| Data migration process | Description |
|---|---|

| 1. Schema migration | DTS migrates the schemas of tables, views, sequences, functions, user- defined types, rules, domains, operations, aggregates, and stored procedures to the destination database. Note DTS does not migrate functions that are written in the C programming language. |
|---|---|
| 2. Full data migration | DTS migrates the existing data of objects from the source database to the destination database. |
| 3. Schema migration | DTS migrates the schemas of triggers and foreign keys to the destination database. |
| 4. Incremental data migration | After full data migration is complete, DTS migrates incremental data from the source database to the destination database. Note In this scenario, DTS can migrate only DML operations for incremental data migration, such as INSERT, DELETE, and UPDATE. Incremental data migration does not support the data of the BIT type. |

**Preparations**

If you want to perform incremental data migration, you must perform the following steps: Log on to the ApsaraDB RDS console. Click the ID of the source ApsaraDB RDS for PostgreSQL instance. In the left-side navigation pane, click **Parameters**. Find the **wal_level** parameter and change the value of the parameter to logical.

> **Warning:** After you modify the `wal_level` parameter, you must restart the instance to apply the modification. We recommend that you evaluate the impact on your business and modify the parameter during off-peak hours.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | The name of the source database in the ApsaraDB RDS for PostgreSQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for PostgreSQL instance. Specify a privileged account. The account must be the owner of the source database. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectP ostgreSQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |

| Destination Database |   |   |
|---|---|---|
|   | Instance ID | The ID of the destination ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | The name of the destination database in the destination ApsaraDB RDS for PostgreSQL instance. Note The name of the destination database can be different from that of the source database. |
|   | Database Account | The database account of the destination ApsaraDB RDS for PostgreSQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.14 Migrate data from an ApsaraDB RDS for PostgreSQL instance to an ApsaraDB RDS for MySQL instance

**for PostgreSQL instance to an ApsaraDB RDS**

**for MySQL instance**

This topic describes how to migrate data from an ApsaraDB RDS for PostgreSQL instance to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports full data migration and incremental data migration. When you configure a data migration task, you can select both of the supported migration types to ensure service continuity.

**Prerequisites**

The destination ApsaraDB RDS for MySQL instance is created. The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of the data in the source ApsaraDB RDS for PostgreSQL instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature is enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, the DTS server stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, the DTS server automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the write-ahead logging (WAL) logs generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|   | To ensure that the data migration task is run as expected, you can perform a primary/secondary switchover only on an ApsaraDB RDS for PostgreSQL V11 instance during data migration. In this case, you must set the rds failover slot mode parameter to sync . _ _ _ Warning If you perform a primary/secondary switchover on an ApsaraDB RDS for PostgreSQL instance of another version during data migration, the data migration task fails. |

|   |   | A data migration task can migrate data from only one database. To migrate |
|---|---|---|
|   | Other limits | data from multiple databases, you must create a data migration task for each database. The name of the source database cannot contain hyphens (-). For example, dts- testdata is invalid. DTS does not check the validity of metadata such as sequences. You must manually check the validity of metadata. Data may be inconsistent between the primary and secondary nodes of the source database due to the latency of incremental data migration. Therefore, you must use the primary node as the data source when you migrate data. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. If you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema during incremental data migration, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding sample statement with your actual schema name and table name. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source _ _ database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During incremental data migration, DTS creates a replication slot for the source database. The replication slot is prefixed with dts sync . DTS _ _ automatically clears historical data in the replication slot every 90 minutes to reduce storage usage. Note If the data migration task is released or fails, DTS automatically clears the replication slot. If the source database is an ApsaraDB RDS for PostgreSQL instance and a primary/secondary switchover is performed on the instance, you must log on to the secondary database to manually clear the replication slot. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

|   | schema.table REPLICA IDENTITY FULL; |
|---|---|

|   | After your workloads are switched to the destination database, newly written sequences do not increment from the maximum value of the sequences in the source database. Therefore, you must query the maximum value of the sequences in the source database before you switch your workloads to the destination database. Then, you must specify the queried maximum value as the starting value of the sequences in the destination database. Statements that are executed to query the maximum value of the sequences in the source database: do language plpgsql $$ declare nsp name; rel name; val int8; begin for nsp,rel in select nspname,relname from pg class t2 , _ pg namespace t3 where t2.relnamespace=t3.oid and t2.relkind='S' _ loop execute format($ $select last value from %I.%I$ $, nsp, rel) _ _ _ into val; raise notice '%', format($ $select setval('%I.%I'::regclass, %s);$ $, nsp, _ _ rel, val+1); end loop; end; |
|---|---|
| Special cases | $$; If the source or destination instance is an ApsaraDB RDS for PostgreSQL instance, take note of the following limits: During data migration, do not modify the endpoint or zone of the ApsaraDB RDS for PostgreSQL instance. Otherwise, the data migration task fails. |

**SQL operations that can be incrementally migrated**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Preparations**

If you want to perform incremental data migration, you must perform the following steps: Log on to the ApsaraDB RDS console. Click the ID of the source ApsaraDB RDS for PostgreSQL instance. In the left-side navigation pane, click **Parameters**. Find the **wal_level** parameter and change the value of the parameter to logical.

> **Warning:** After you change the value of the `wal_level` parameter, you must restart the instance to apply the change. We recommend that you evaluate the impact on your business and change the parameter settings during off-peak hours.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note Specifies whether to migrate data between instances that belong to different Alibaba Cloud accounts. If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | The name of the source database in the ApsaraDB RDS for PostgreSQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for PostgreSQL instance. Specify a privileged account. The account must be the owner of the source database. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectM ySQL. |

| er Guide·Data mig | ration Data Transmission Servic |   |
|---|---|---|
| Destination Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Name | The name of the destination database in the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.15 Migrate data between PolarDB for PostgreSQL (Compatible with Oracle) clusters

**PostgreSQL (Compatible with Oracle) clusters**

This topic describes how to migrate data between PolarDB for PostgreSQL (Compatible with Oracle) clusters by using Data Transmission Service (DTS).

**Prerequisites**

The tables that you want to migrate from the source PolarDB for PostgreSQL (Compatible with Oracle) cluster contain primary keys or UNIQUE NOT NULL indexes.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The write-ahead logging (WAL) feature must be enabled. WAL logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the WAL logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of WAL logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the WAL logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the WAL logs of the source database are cleared during full data migration, DTS cannot obtain the WAL logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |
|---|---|

| Other limits | A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding statement with your schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS adds a heartbeat table named dts postgres heartbeat to the source database. _ _ The following figure shows the schema of the heartbeat table. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

|   | schema.table REPLICA IDENTITY FULL; |
|---|---|

**Migration types**

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of objects to the destination PolarDB cluster. DTS supports schema migration for the following types of objects: table, view, synonym, stored procedure, stored function, package, and user-defined type. Important In this scenario, DTS does not support triggers. If an object contains triggers, data inconsistency may occur between the source and destination databases. |

| Full data migration | DTS migrates the historical data of objects from the source database to the destination PolarDB cluster. Important During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
|---|---|
| Incremental data migration | DTS retrieves redo log files from the source database. Then, DTS migrates incremental data from the source database to the destination database. DTS can migrate DML operations, such as INSERT, UPDATE, and DELETE. DTS cannot migrate DDL operations. Incremental data migration allows you to ensure service continuity when you perform data migration. |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB (Compatible with Oracle). |
|   | Access Method | The access method of the source cluster. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Data Sources | Single Data Source: If you select this option, you must configure the Domain Name or IP Address and Port Number parameters of the primary node in the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. Multiple Data Sources: If you select this option, you must specify the IP addresses and port numbers of multiple nodes, including the primary node, in the source PolarDB for PostgreSQL (Compatible with Oracle) cluster in the IP:Port of Data Sources field. Note If you select Multiple Data Sources and specify the IP:Port of Data Sources parameter, DTS can automatically switch to a new primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster during primary/secondary switchover. This is suitable for scenarios such as disaster recovery. |

|   | Domain Name or IP Address | The endpoint of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|---|---|---|
|   | Port Number | The service port number of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. The default port number is 3433. |
|   | Database Name | The name of the source database. |
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectP olarDB (Compatible with Oracle). |
| Destinati on Database |   |   |
|   | Access Method | The access method of the destination cluster. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination cluster resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Data Sources | Single Data Source: If you select this option, you must configure the Domain Name or IP Address and Port Number parameters of the primary node in the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. Multiple Data Sources: If you select this option, you must specify the IP addresses and port numbers of multiple nodes, including the primary node, in the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster in the IP:Port of Data Sources field. Note If you select Multiple Data Sources and specify the IP:Port of Data Sources parameter, DTS can automatically switch to a new primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster during primary/secondary switchover. This is suitable for scenarios such as disaster recovery. |
|   | Domain Name or IP Address | The endpoint of the primary node in the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Port Number | The service port number of the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. Default value: 1433. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination PolarDB for PostgreSQL (Compatible with Oracle) cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the migration types and the objects to be migrated.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information,see Configure ETL in a data migration task. No: does not configure the ETL feature. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.16 Migrate data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to a self-managed Oracle database

**PostgreSQL (Compatible with Oracle) cluster**

**to a self-managed Oracle database**

This topic describes how to migrate data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to a self-managed Oracle database by using Data Transmission Service (DTS).

**Prerequisites**

A self-managed Oracle database is created, and the schema of the Oracle database is the same as the schema of the source database in the PolarDB for PostgreSQL (Compatible with Oracle) cluster. This prerequisite must be met because DTS does not support schema migration from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to a self-managed Oracle database.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The write-ahead logging (WAL) feature is enabled. WAL logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the WAL logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of WAL logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the WAL logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the WAL logs of the source database are cleared during full data migration, DTS cannot obtain the WAL logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding statement with your actual schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source _ _ database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|

|   | schema.table REPLICA IDENTITY FULL; |
|---|---|

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |

| Source Database | Database Type | The type of the source database. Select PolarDB (Compatible with Oracle). |
|---|---|---|
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Data Sources | Single Data Source: If you select this option, you must configure the Domain Name or IP Address and Port Number parameters of the primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster. Multiple Data Sources: If you select this option, you must specify the IP addresses and port numbers of multiple nodes, including the primary node, in the PolarDB for PostgreSQL (Compatible with Oracle) cluster in the IP:Port of Data Sources field. Note If you select Multiple Data Sources and configure the IP:Port of Data Sources parameter, DTS can automatically switch to a new primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster during primary/secondary switchover. This is suitable for scenarios such as disaster recovery. |
|   | Domain Name or IP Address | The endpoint that is used to connect to the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Port Number | The service port number of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. The default port number is 1521. |
|   | Database Name | The name of the source database. |
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectO racle. |
|   | Access Method | The access method of the destination database. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination instance resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint that is used to connect to the destination Oracle database. |
|   | Port Number | The service port number of the destination Oracle database. The default port number is 1521. |

| Destinati on Database |   |   |
|---|---|---|
|   | Oracle Type | The Oracle data type. Select Non-RAC Instance or RAC or PDB Instance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Note This parameter is required if you select Non-RAC Instance as the instance type. |
|   | Service Name | The server name of the instance. Note This parameter is required if you select RAC or PDB Instance as the instance type. |
|   | Database Account | The account that is used to connect to the destination Oracle database. The account must have the read and write permissions on the database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Full Data Migration. To ensure service continuity during data migration, select Full Data Migration and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.17 Migrate data from a PolarDB for PostgreSQL cluster that is compatible with Oracle to a self-managed Kafka cluster

**PostgreSQL cluster that is compatible with**

**Oracle to a self-managed Kafka cluster**

Kafka is a distributed message queue service that supports high throughput and high scalability. Kafka is widely used for big data analytics such as log collection, monitoring data aggregation, streaming processing, and online and offline analysis. Kafka is an essential service for the big data ecosystem. This topic describes how to migrate data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to a self-managed Kafka cluster by using Data Transmission Service (DTS). The data migration feature allows you to extend message processing capabilities.

**Prerequisites**

The tables that you want to migrate from the source PolarDB for PostgreSQL (Compatible with Oracle) cluster contain primary keys or UNIQUE NOT NULL indexes.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data from a database, you must enable the write-ahead logging (WAL) feature for the database. The source PolarDB for PostgreSQL (Compatible with Oracle) cluster must be of the latest version. |
| Other limits | Full data migration is not supported in this scenario. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding statement with your actual schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source _ _ database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

|   | schema.table REPLICA IDENTITY FULL; |
|---|---|

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |

| Source Database | Database Type | The type of the source database. Select PolarDB (Compatible with Oracle). |
|---|---|---|
|   | Access Method | The access method of the source cluster. Select Public IP Address. |
|   | Instance Region | If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Data Sources | Single Data Source: If you select this option, you must configure the Domain Name or IP Address and Port Number parameters of the primary node in the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. Multiple Data Sources: If you select this option, you must enter the IP addresses and port numbers of multiple nodes, including the primary node, in the source PolarDB for PostgreSQL (Compatible with Oracle) cluster in the IP:Port of Data Sources field. Note If you select Multiple Data Sources and configure the IP:Port of Data Sources parameter, DTS can automatically switch to a new primary node in the PolarDB for PostgreSQL (Compatible with Oracle) cluster during primary/secondary switchover. This is suitable for scenarios such as disaster recovery. |
|   | Domain Name or IP Address | The endpoint of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Port Number | The service port number of the PolarDB for PostgreSQL (Compatible with Oracle) cluster. Default value: 1521. |
|   | Database Name | The name of the source database. |
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectK afka. |
|   | Access Method | The access method of the destination cluster. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination cluster resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | IP address (domain name is not supported) | The IP address that is used to access the self-managed Kafka cluster. In this example, the public IP address is used. |
|   | Port Number | The service port number of the self-managed Kafka cluster. Default value: 9092. |

| Destinati |   |   |
|---|---|---|
|   | Database Account | The username that is used to log on to the Kafka cluster. If no authentication is enabled for the Kafka cluster, you do not need to enter the username. |
|   | Database Password | The password of the database account. If no authentication is enabled for the self-managed Kafka cluster, you do not need to specify this parameter. |
| on Database |   |   |
|   | Kafka Version | The version of the destination Kafka cluster. Note You cannot select Kafka 2.0 in the DTS console. If you are using Kafka 2.0, you must select Kafka 1.0. |
|   | Encryption | Specifies whether to encrypt the connection. Select Non- encrypted or SCRAM-SHA-256 based on your business and security requirements. |
|   | Topic | The name of the destination topic. Select a value from the drop- down list. |
|   | Use Kafka Schema Registry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types.

| Parameter | Description |
|---|---|
| Task Stages | Select Incremental Data Migration and Schema Migration. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select only tables as the objects to be migrated. |
| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.18 Migrate data between self-managed Redis databases

**Redis databases**

This topic describes how to migrate data between self-managed Redis databases by using Data Transmission Service (DTS).

**Prerequisites**

The version of the source Redis database is 2.8, 3.0, 3.2, 4.0, or 5.0. The source Redis database uses the standalone architecture rather than the cluster architecture. The `PSYNC` or `SYNC` command can be executed on the source Redis database.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The redo logging and archive logging must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |
|---|---|

| Other limits | If the data eviction policy maxmemory-policy of the destination database is not set to noeviction , data inconsistency may occur between the source and destination databases. If you run the EVAL or EVALSHA command to call Lua scripts, DTS cannot identify whether these Lua scripts are executed in the destination database. This is because the destination database does not explicitly return the execution results of Lua scripts during incremental data migration. When you run the PSYNC or SYNC command to transfer data of the LIST type, DTS does not perform the FLUSH operation on the existing data in the destination database. As a result, the destination database may contain duplicate data records. If an expiration policy is enabled for specific keys in the source database, these keys may not be deleted at the earliest opportunity after they expire. Therefore, the number of keys in the destination database may be less than that in the source database. You can run the INFO command to view the number of keys in the destination database. Note The number of keys that do not have the expiration policy enabled or have not expired is the same between the source and destination databases. To ensure compatibility, the version of the destination Redis database must be the same as or later than the version of the source Redis database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If you perform a primary/secondary switchover on the source or destination self- managed Redis database when the data migration task is running, the task fails. |

**Migration types**

Full data migration: DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration: After full data migration is complete, DTS migrates incremental data from the source database to the destination database in real time.

**Commands that can be incrementally migrated**

APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT FLUSHALL and FLUSHDB GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, PSETEX, and PUBLISH RENAME, RENAMENX, RESTORE, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE

**Before you begin**

To ensure that incremental data migration tasks run as expected, we recommend that you remove the limit on the replication output buffer for the source database. In this topic, a server that runs on Linux is used in the example.

> **Note:** If you perform only full data migration, skip the following steps.

1. Use the redis-cli program to connect to the source database.

> **Note:** You can use the redis-cli program after you install the Redis client. For more information, see Redis community official website.

```
redis-cli -h <host> -p <port> -a <password>
```

> **Note:** <host>: the endpoint that is used to connect to the source database. You can use 127.0.0.1 in this example.
> <port>: the service port number of the source database. The default port number is 6379.
> <password>: the password of the source database.

Example:

```
redis-cli -h 127.0.0.1 -p 6379 -a Test123456
```

2. Run the following command to remove the limit on the replication output buffer:

```
config set client-output-buffer-limit 'slave 0 0 0'
```

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select Redis. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If the Access Method parameter is set to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Instance Mode | The value of this parameter is fixed to Standalone and cannot be changed to Cluster. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source database. |
|   | Port Number | The service port number of the source database. Default value: 6379. |
|   | Database Password | The password of the source database. If password verification is disabled for the source database, you do not need to enter the password. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. |
| Destinati on Database | Database Type | The type of the destination database. SelectR edis. |
|   | Access Method | The access method of the destination database. SelectP ublic IP Address. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | Instance Mode | The value of this parameter is fixed to Standalone and cannot be changed to Cluster. |
|   | Hostname or IP Address | The endpoint that is used to connect to the destination database. |
|   | Port Number | The service port number of the destination database. Default value: 6379. |

|   | Database Password | The password of the destination database. If password verification is disabled for the destination database, you do not need to enter the password. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. |
|---|---|---|

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for the self-managed Redis database, you must manually add the
CIDR blocks of DTS servers to the whitelist of the database. After you configure the whitelist, click **Test Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for the self-managed Redis database, ignore the preceding settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | If you want to perform only full data migration, select Full Data Migration. To ensure service continuity during data migration, select Full Data Migration and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select only databases as the objects to be migrated. You cannot select keys as the objects to be migrated. |
|---|---|
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.19 Migrate data between self-managed MongoDB databases

**MongoDB databases**

This topic describes how to migrate data between self-managed MongoDB databases by using Data Transmission Service (DTS).

**Prerequisites**

The version of the source MongoDB database is 3.0, 3.2, 3.4, 3.6, 4.0, or 4.2.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you need to migrate incremental data, make sure that the following requirements are met: The operation logging feature is enabled. Operation logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the operation logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of operation logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the operation logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the operation logs of the source database are cleared during full data migration, DTS cannot obtain the operation logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Other limits | If you need to migrate incremental data from a standalone MongoDB database, you must enable the operation logging feature. A standalone MongoDB database contains only a primary node. For more information, see the Preparation for a standalone MongoDB database section of this topic. If the source database uses the sharded cluster architecture, you must configure a data migration task for each shard. To ensure compatibility, the version of the destination MongoDB database must be the same as or later than the version of the source MongoDB database. The admin or local database is not used as the source or destination database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the data migration task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|---|---|
| Special cases | If both the source database and destination database are self-managed MongoDB databases, take note of the following items: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

**Migration types**

| Migration type | Description |
|---|---|
| Full data migration | DTS migrates the historical data of the objects to be migrated from the source database to the destination database. Note DTS can migrate the following types of objects: database, collection, and index. |

| Incremental data migration | After full data migration is complete, DTS migrates incremental data from the source database to the destination database in real time. Note DTS can migrate the create and delete operations that are performed on databases, collections, and indexes. DTS can migrate the create, delete, and update operations that are performed on documents. |
|---|---|

**Preparation for a standalone MongoDB database**

If you need to migrate incremental data from a standalone MongoDB database, you must enable the operation logging feature. A standalone MongoDB database contains only a primary node. If you do not need to perform incremental data migration, skip the following steps.

> **Note:** When you enable the operation logging feature, the MongoDB service is restarted. We recommend that you perform this operation during off-peak hours.

1. Use Mongo Shell to connect to the source database.
2. Run the following commands to shut down the MongoDB service:

```
use admin db.shutdownServer()
```

3. Run the following command to start the MongoDB service from the backend as a replica
set:

```
mongod --port 27017 --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log - -replSet rs0 --bind_ip 0.0.0.0 --auth --fork
```

> **Note:** The database path used by the preceding command is /var/lib/mongodb. The log file path is /var/log/mongodb/mongod.log. You must specify the paths based on your business requirements.
> The command uses `0.0.0.0` as the associated IP address of the MongoDB service. This allows you to access the database by using a random IP address. After the migration is complete, run the `kill` command to end the process, and start the MongoDB service by using the original configuration file.
> The command enables authentication. You can access the database only after you pass the authentication.

4. Use Mongo Shell to connect to the source database again.
5. Run the following commands to initialize the replica set:

```
use admin rs.initiate()
```

6. Wait until the role of the current node changes to primary. This indicates that the operation
logging feature is enabled.

> **Note:** You can run the `rs.printReplicationInfo()` command to view the status of the operation logging feature.

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Databas e | Database Type | The type of the source database. Select MongoDB. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to configure the Instance Region parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source database. |
|   | Port Number | The service port number of the source database. |
|   | Database Name | The name of the authentication database. The database account is created in this database. |
|   | Database Account | The account of the source database. The account must have the read permissions on the source database, admin database, and local database. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the database. In this example, Non-encrypted is selected. Note Select SSL-encrypted only when you migrate data from MongoDB Atlas databases. |
| Destinat ion | Database Type | The type of the destination database. SelectM ongoDB. |
|   | Access Method | The access method of the destination database. SelectP ublic IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP Address | The endpoint that is used to connect to the destination database. |

| ion Databas e |   |   |
|---|---|---|
|   | Port Number | The service port number of the destination database. |
|   | Database Name | The name of the authentication database. The database account is created in this database. Note If you want to use the root account, enter admin in the Database Name field. |
|   | Database Account | The account of the destination database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed MongoDB database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist of the self-managed MongoDB database. Then, click **Text Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for your self-managed MongoDB database, ignore the preceding settings and click **Test Connectivity and Proceed**.

6. Select the objects to be migrated and the migration types.

| Parame ter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
|---|---|
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.20 Migrate data from a MaxCompute project to a MySQL database

**project to a MySQL database**

This topic describes how to migrate data from a MaxCompute project to a MySQL database by using Data Transmission Service (DTS). In this example, an ApsaraDB RDS for MySQL instance is used as the destination instance.

**Limits**

DTS uses read and write resources of the source and destination databases during full data migration. This may increase the loads of the database servers. If the database performance is unfavorable, the specification is low, or the data volume is large, database services may become unavailable. For example, DTS occupies a large amount of read and write resources in the following cases: a large number of slow SQL queries are performed on the source database, the tables have no primary keys, or a deadlock occurs in the destination database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. For example, you can migrate data when the CPU utilization of the source and destination databases is less than 30%. DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must manually create a database in the destination instance before you configure the data migration task.

> **Note:** For more information about ApsaraDB RDS for MySQL instances and how to create a database in an ApsaraDB RDS for MySQL instance, see the "Create a database" topic in the documentation of ApsaraDB RDS for MySQL.

To ensure data consistency, we recommend that you do not write data to the source MaxCompute project during full data migration. If a data migration task fails, DTS automatically resumes the task. Before you switch your workloads to the destination instance, stop or release the data migration task. Otherwise, the data in the source database overwrites the data in the destination instance after the task is resumed. MaxCompute does not support the PRIMARY KEY constraint. If network errors occur, DTS retries the data migration task. In this case, duplicate data records may be migrated to the destination tables that do not have primary keys. DTS cannot migrate incremental data from a MaxCompute project to an ApsaraDB RDS for MySQL instance.

> **Note:** To ensure data consistency, we recommend that you do not write data to the source MaxCompute project during data migration.

**Migration types**

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of the required objects to the destination database. DTS supports schema migration for views, tables, and databases. Warning MaxCompute and MySQL are heterogeneous databases. DTS does not ensure that the schemas of the source and destination databases are consistent after schema migration. We recommend that you evaluate the impact of data type conversion on your business. For more information, see Data type mappings between heterogeneous databases. |

| Full data migration | DTS migrates full data of the required objects to the destination database. Note During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the used tablespace of the destination database is larger than that of the source database. |
|---|---|

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MaxCompute. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Project | The name of the MaxCompute project. You can view the name of the MaxCompute project on the Projects page in the MaxCompute console. |
|   | AccessKey ID | The AccessKey ID and AccessKey secret of the account that you use to connect to the source MaxCompute project. Note For more information about how to obtain an AccessKey pair, see the Obtain the AccessKey pair of an organization topic in the Developer Guide of MaxCompute. |
|   | AccessKey Secret |   |
| Destination Database | Database Type | The type of the destination database. SelectM ySQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |

|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have read and write permissions on the destination database. |
|---|---|---|
|   | Database Password | The password of the database account. After you set the destination database parameters, click Test Connectivity next to Database Password to verify whether the specified parameters are valid. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. In the dialog box that appears, click **OK**. In this step, the permissions on the MaxCompute
project are granted to the account used by DTS to migrate data.
6. Select the migration types and the objects to be migrated.

| Parame ter | Description |
|---|---|
| Task Stages | Select Schema Migration and Full Data Migration. Note DTS cannot migrate incremental data from a MaxCompute project to an ApsaraDB RDS for MySQL instance. |
| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with that in the source or destination database. For more information,see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. |
| Selecte d Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data migration task. Select No. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

#### 3.4.21 Migrate data from a PolarDB-X 2.0 instance

**instance**

##### 3.4.21.1 Migrate data between PolarDB-X 2.0 instances

**instances**

This topic describes how to migrate data between PolarDB-X 2.0 instances by using Data Transmission Service (DTS).

**Prerequisites**

The source and destination PolarDB-X 2.0 instances are created and compatible with MySQL 5.7. The available storage space of the destination PolarDB-X 2.0 instance is larger than the total size of the data in the source PolarDB-X 2.0 instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of theP olarDB-X instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X instance must be compatible with MySQL 5.7. |

| Other limits | The destination PolarDB-X instance must be compatible with MySQL 5.7. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
|---|---|
| Precautions | DTS updates the `dts health check`.`ha health check` table in the source _ _ _ _ database as scheduled to move forward the binary log file position. |

**Migration types**

Schema migration DTS migrates the schemas of the selected objects from the source database to the destination database. Full data migration DTS migrates the historical data of the selected objects from the source database to the destination database. Incremental data migration After full data migration is completed, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting the services of self-managed applications during data migration.

**Permissions required for database accounts**

| Database type | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |
| Destination PolarDB-X 2.0 instance | Read and write permissions |   |   |

**SQL operations that can be migrated during incremental data**

**migration**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |

| Destination Database | Database Type | The type of the destination database. Select PolarDB-X 2.0. |
|---|---|---|
|   | Access Method | The access method of the destination database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the destination PolarDB-X 2.0 instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, we recommend that you do not write data to the source database during data migration. This ensures data consistency between the source and destination databases. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. |
| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data migration task does not support the ETL feature. Select No. |
| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

##### 3.4.21.2 Migrate data from a PolarDB-X 2.0 instance to a MySQL instance

**instance to a MySQL instance**

This topic describes how to migrate data from a PolarDB-X 2.0 instance to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS).

**Prerequisites**

The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of data in the source PolarDB-X 2.0 instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to edit the tables in the destination database, such as renaming tables or columns, up to 1,000 tables can be migrated in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches, or configure a task to migrate the entire database. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to FULL. Otherwise, error messages are returned during the precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform both full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you change the network type of a PolarDB-X instance during data migration, contact technical support to change the network connection settings of the data migration instance. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. The PolarDB-X instance must be compatible with MySQL 5.7. |

| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
|---|---|
| Special cases | If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. For more information, see the "Create a database" topic in the documentation of ApsaraDB RDS for MySQL. |

**Migration types**

Schema migration DTS migrates the schemas of the selected objects from the source database to the destination database. Full data migration DTS migrates the historical data of the selected objects from the source database to the destination database. Incremental data migration After full data migration is completed, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting the services of self-managed applications during data migration.

**SQL operations that can be migrated during incremental data**

**migration**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE Note RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object and rename the table during data migration, the data of this table is not migrated to the destination database. To prevent this situation, you can select the database to which this table belongs as the object when you configure the data migration task. TRUNCATE TABLE |
|---|---|

**Permissions required for database accounts**

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |
| ApsaraDB RDS for MySQL | Read and write permissions |   |   |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select PolarDB-X 2.0. |

| ta Transmissi | on Service User Guide·Data migratio |   |
|---|---|---|
| Source Database |   |   |
|   | Access Method | The access method of the source database. Default value:A libaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source instance. |
|   | Database Account | The database account of the source instance. For information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
| Destinati on Database | Database Type | The type of the destination database. SelectM ySQL. |
|   | Access Method | The access method of the destination database. Default value: Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint of the destination instance. |
|   | Port Number | The port number of the destination instance. Default value: 3306. |
|   | Database Account | The database account of the destination instance. For information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your MySQL instance, add the CIDR blocks of DTS servers that
are displayed in the dialog box to the whitelist. After the whitelist is configured, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your MySQL instance, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Configure the objects to be migrated and advanced settings. The following table describes
the parameters.

| Parameter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If you do not select Incremental Data Migration, we recommend that you do not write data to the source database during data migration. This ensures data consistency between the source and destination databases. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be migrated. If you select tables or columns as the objects to be migrated, DTS does not migrate other objects, such as views, triggers, or stored procedures, to the destination database. |

| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|

7. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data migration task does not support the ETL feature. Select No. |
| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

##### 3.4.21.3 Migrate data from a PolarDB-X 2.0 instance to a Message Queue for Apache Kafka instance

**instance to a Message Queue for Apache Kafka**

**instance**

This topic describes how to migrate data from a PolarDB-X 2.0 instance to a Message Queue for Apache Kafka instance by using Data Transmission Service (DTS). Message Queue for Apache Kafka provides extended capabilities to process messages.

**Prerequisites**

A PolarDB-X 2.0 instance is created. In the destination Message Queue for Apache Kafka instance, a topic is created to receive the migrated data. The available storage space of the destination Message Queue for Apache Kafka instance is larger than the total size of the data in the source PolarDB-X 2.0 instance.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of theP olarDB-X instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X instance must be compatible with MySQL 5.7. |
|---|---|

| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
|---|---|
| Precautions | DTS updates the `dts health check`.`ha health check` table in the source _ _ _ _ database as scheduled to move forward the binary log file position. |

**Migration types**

Schema migration DTS migrates the schemas of the selected objects from the source database to the destination database. Full data migration DTS migrates the historical data of the selected objects from the source database to the destination database. Incremental data migration After full data migration is completed, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting the services of self-managed applications during data migration.

**Permissions required for database accounts**

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |

**SQL operations that can be incrementally migrated**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. For more information about the required permissions, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectK afka. |

| ta Transmissi |   |   |
|---|---|---|
| Destinati on Database |   |   |
|   | Access Method | The access method of the destination database. Default value: Public IP Address. Note If you select Public IP Address, you can use a specific IP address to connect to the destination Message Queue for Apache Kafka instance over the classic network. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | IP address (domain name is not supported) | The endpoint of the destination Message Queue for Apache Kafka instance. Note To obtain an IP address of the Message Queue for Apache Kafka instance, perform the following operations: Log on to the Message Queue for Apache Kafka console and go to the Instance Details page of the Message Queue for Apache Kafka instance. In the Endpoint Information section of the Instance Information tab, obtain an IP address from the Default Endpoint parameter. |
|   | Port Number | The service port number of the destination Message Queue for Apache Kafka instance. |
|   | Database Account | The database account of the destination Message Queue for Apache Kafka instance. Note If the Message Queue for Apache Kafka instance is aV PC- connected instance, you do not need to configure the Database Account or Database Password parameter. |
|   | Database Password | The password of the database account. |
|   | Kafka Version | The version of the destination Message Queue for Apache Kafka instance. Note If the version of the destination Message Queue for Apache Kafka instance is 1.0 or later, select 1.0. |

|   | Encryption | Specifies whether to encrypt the connection to the destination instance. Select Non-encrypted or SCRAM-SHA-256 based on your business and security requirements. |
|---|---|---|
|   | Topic | The topic that is used to receive the migrated data. Select a topic from the drop-down list. |
|   | Topic That Stores DDL Information | The topic that is used to store the DDL information. Select a topic from the drop-down list. If you do not configure this parameter, the DDL information is stored in the topic that is specified by the Topic parameter. |
|   | Use Kafka Schema Registry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the objects to be migrated and advanced settings. The following table describes
the parameters.

| Parameter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If you do not select Incremental Data Migration, we recommend that you do not write data to the source database during data migration. This ensures data consistency between the source and destination databases. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Data Format in Kafka | The format in which data is stored in the Message Queue for Apache Kafka instance. If you select DTS Avro, data is parsed based on the schema definition of DTS Avro. For more information, visit GitHub. If you select Canal Json, data is parsed into the Canal JSON format. For more information about the parameters that are used to parse data into the Canal JSON format, see the Canal Json section of the "Data formats of a Kafka cluster" topic. |
| Policy for Shipping Data to Kafka Partitions | The policy based on which data is migrated to the Message Queue for Apache Kafka instance. Select a policy base on your business requirements. For more information, see Specify the policy for migrating data to Kafka partitions. |
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. |
|---|---|
| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to migrate. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. For more information about how to specify WHERE conditions to filter data, see Specify an SQL condition to filter data. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data migration task does not support the ETL feature. Select No. |

| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |
|---|---|

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

##### 3.4.21.4 Migrate data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance

**instance to an AnalyticDB for PostgreSQL instance**

This topic describes how to migrate data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS).

**Prerequisites**

The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The destination AnalyticDB for PostgreSQL instance is created.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of theP olarDB-X instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X instance must be compatible with MySQL 5.7. |
|---|---|

| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
|---|---|

**Migration types**

Schema migration DTS migrates the schemas of the selected objects from the source database to the destination database. Full data migration DTS migrates the historical data of the selected objects from the source database to the destination database. Incremental data migration After full data migration is completed, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting the services of self-managed applications during data migration.

**SQL operations that can be migrated during incremental data**

**migration**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Procedure**

1. Create a data migration instance.
2. On the Data Migration page, find the data migration instance that you created, and click
**Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. The account must have the SELECT permission on the objects to be migrated, the REPLICATION CLIENT permission, and the REPLICATION SLAVE permission. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. Select AnalyticDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |

|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|---|---|---|
|   | Database Name | The name of the destination database in the AnalyticDB for PostgreSQL instance. |
|   | Database Account | The initial database account of the destination AnalyticDB for PostgreSQL instance or an account that has the RDS SUPERUSER permission. _ |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be migrated and the migration types.

| Parameter | Description |
|---|---|
| Task Stages | To perform only full data migration, select Schema Migration and Full Data Migration. To ensure service continuity during data migration, select Schema Migration, Full Data Migration, and Incremental Data Migration. Note If Incremental Data Migration is not selected, we recommend that you do not write data to the source instance during data migration. This ensures data consistency between the source and destination instances. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. |
| Selected Objects | By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data migration task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Note If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data migration task does not support the ETL feature. Select No. |
| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |

7. **Optional.** Click **Next: Configure Database and Table Fields** . Configure the tables that
you want to migrate to the destination AnalyticDB for PostgreSQL instance.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key** **column**, and **distribution key** information for the tables that you want to migrate to the AnalyticDB for PostgreSQL instance.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until **Success Rate** reaches 100%. Then, click **Back**.

> **Note:** If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the migration task enters the **Running** state and is not delayed, and then manually stop the task.

### 3.5 Manage data migration tasks

#### 3.5.1 Object name mapping

Data Transmission Service (DTS) provides the object name mapping feature. You can use this feature to change the names of one or more objects that are migrated to the destination instance. This topic describes how to use the object name mapping feature when you configure a data migration task.

**Limits**

You can use the object name mapping feature only when you configure parameters in the
**Configure Objects and Advanced Settings** step for configuring a data migration task.

> **Note:** We recommend that you do not use the object name mapping feature after a DTS task is started. Otherwise, the task may fail.

**Map the name of a single object**

1. In the **Configure Objects and Advanced Settings** step, move a database or table to the
**Selected Objects** section and right-click the database or table.
2. In the dialog box that appears, set the object name that you want to use in the destination
instance.

> **Note:** If the source and destination databases are self-managed MySQL databases, ApsaraDB RDS for MySQL instances, or PolarDB for MySQL instances, you can select the DDL and DML statements that you want to synchronize or migrate.
> If you select different statements for database name mapping and table name mapping, the statements that are selected for table name mapping prevail.

Database name or schema mapping In the **Edit Schema** dialog box, set the database name that you want to use in the destination instance. Table name mapping In the **Edit Table Name** dialog box, set the table name that you want to use in the destination instance. Column name mapping In the **Edit Table Name** dialog box, set the column names that you want to use in the destination instance. You can clear the columns that do not need to be migrated.

> **Important:** To clear the columns that do not need to be migrated, you must clear **Synchronize All Tables**.

3. Click **OK**.
4. Configure other parameters that are required for the data migration task.

**Map multiple object names at a time**

1. In the **Configure Objects and Advanced Settings** step, move the objects to be migrated
to the **Selected Objects** section.
2. Click **Batch Edit** in the **Selected Objects** section.
3. In the **Batch Edit** dialog box, map the names of databases, tables, and columns based on
your business requirements. i. Select the type of batch edit. In this example, **Select All Databases and Tables** is selected. ii. Select the scope of batch edit.
**Edit Renamed Object Name**: edits the names of databases, tables, and columns
based on their renamed names.
**Edit Original Name**: edits the names of databases, tables, and columns based on
their original names. iii. Select the objects whose names you want to edit. iv. Set the names of databases and tables by using one of the following three rules. Then, click **Add Rule**. Add Prefix and Suffix: Enter a prefix and suffix next to the **Add Prefix and Suffix** field. Change All Names: Select **Change All Names** from the **Select Rule** drop-down list and enter the new name. Shorten All Names: Select **Shorten All Names** from the **Select Rule** drop-down list and enter the keyword that you want to remove from object names.

> **Note:** In the Batch Edit dialog box, you can specify conditions to filter data. For more information, see Specify an SQL condition to filter data.

v. Click **OK**.
4. Configure other parameters that are required for the DTS task.

#### 3.5.2 Specify an SQL condition to filter data

This topic describes how to specify an SQL condition to filter the data of a specific table when you configure a data migration task. Data Transmission Service (DTS) allows you to configure an SQL filter to filter the table data to be migrated. The SQL condition takes effect only within the table that you select. DTS migrates only the data that meets the SQL condition to the destination database. This feature is applicable to scenarios such as regular data migration and table partitioning.

**Limits**

An SQL condition applies only to full data migration. If you select **Incremental Data**
**Migration** as the migration type, the SQL condition does not filter incremental data.

**Specify an SQL condition**

You can specify an SQL condition in the **Configure Objects and Advanced Settings** step when you configure a data migration task. To filter the data of a specific table by using an SQL condition, you must select the table as the object that you want to migrate. You cannot select a database as the object. To specify an SQL condition, perform the following steps.

**Procedure**

1. In the **Selected Objects** section of the **Configure Objects and Advanced Settings**
step, move the pointer over the table for which you want to configure filter conditions and right-click the table.
2. In the **Edit Table Name** dialog box, enter one or more SQL conditions in the **Filter**
**Conditions** field.

|   | Note An SQL condition is a standard SQL WHERE statement. The following operators are supported: = , != , < , > , and in . Only the data that meets the WHERE condition is synchronized to the destination database. In this example, orderid>100 is entered. You can specify a time condition in an SQL WHERE statement. However, you must make sure that the specified time condition is valid. For example, to filter incremental data created since 2020, you must enter create time>'2020-01- _ 01' or create time>'2020-01-01 00:00:00' . You cannot enter _ create time>'2020' . _ You can use single quotation marks (') in an SQL condition if necessary. For example, you can enter address in('hangzhou','shanghai') . Filter conditions are not case-sensitive. If a table in the source database contains Column A and Column a, you can use an SQL WHERE statement to filter only Column A. In this case, you can enter WHERE A=10 rather than WHERE a=10 . Filter statements supported by ApsaraDB for MongoDB instances are different from standard SQL WHERE statements. For example, if you want to use user ID as the filter condition, enter {" id": _ {$gt:"user100844658590795****",$lte:"user101674868045948****"}} . In this statement, gt indicates greater than and lte indicates less than. |   |
|---|---|---|
|   | 01' |   |

|   | {" id": _ |
|---|---|
| {$gt:"user100844658590795****",$lte:"user101674868045948****"}} |   |

3. Click **OK**.
4. Configure other parameters that are required for the data synchronization task as
prompted.

#### 3.5.3 Troubleshoot a failed data migration task

**task**

This topic describes how to troubleshoot a failed data migration task. You can use this feature if your data migration task is in the **Migration Failed** state during schema migration or full data migration.

**Troubleshoot a failed task during schema migration**

Data Transmission Service (DTS) supports data migration between heterogeneous data sources. However, if you migrate data of unsupported types to the destination instance during schema migration, the task may fail.
1. Log on to the DTS console.
2. In the left-side navigation pane, click **Data Migration**.
3. Use one of the following methods to troubleshoot the failed task:
Method 1 a. Find the task and click **View Cause and Rectify**. b. Troubleshoot the issue based on the cause that is displayed in the View Cause and Rectify message. For example, you can troubleshoot an issue by modifying the schema syntax. c. Click **Start Task**. Method 2 a. Click the instance ID or task name. b. In the left-side navigation pane, choose **Migration Details > Schema Migration**. c. On the **Schema Migration** page, find the object that causes the migration failure and click **Rectify** in the Status column. d. Troubleshoot the issue based on the cause that is displayed in the **Rectify** dialog box. For example, you can troubleshoot an issue by modifying the schema syntax. e. Click **Rectify**.

> **Note:** If the failure persists, the **Rectify** dialog box does not close and shows the failure cause. You must continue troubleshooting based on the failure cause until the troubleshooting is successful.
> If the troubleshooting is successful, the **Schema Migration** page appears and the status of the object changes to **Finished**.

4. If no objects are in the Failed state, DTS proceeds with the data migration task, for
example, entering the full data migration process.

**Troubleshoot a failed task during full data migration**

1. Log on to the DTS console.
2. In the left-side navigation pane, click **Data Migration**.
3. Find the task and click **View Cause and Rectify**.
DTS allows you to troubleshoot a task that fails during full data migration due to the following reasons.

> **Note:** If a task fails during full data migration due to other reasons, DTS provides only the **Ignore** option. The object that causes the failure is not migrated to the destination database.

The connection to the source or destination database failed or timed out. Troubleshoot the issue, make sure that the connection is successful, and then restart the task. The storage space of the destination instance is insufficient or the instance is locked. Upgrade the specifications of the destination instance or clear the log space, and then restart the task. MyISAM tables in the source database are corrupted. Troubleshoot the issue in the source database, and restart the task.
4. In the dialog box that appears, troubleshoot the issue based on the failure cause.
5. Click **Start Task**.

#### 3.5.4 Specify the capitalization of object names in the destination instance

**names in the destination instance**

When you configure a data migration or synchronization task, you can specify the capitalization of database names, table names, and column names in the destination instance.

**Capitalization policies**

Data Transmission Service (DTS) supports the following capitalization policies for object names: DTS default policy DTS configures the capitalization of database names, table names, and column names in the destination instance based on the database type and related parameters, such as the `lower_case_table_names` parameter.

| Destination database type | Destination database parameter | Capitalization of object names in the destination instance |
|---|---|---|
| Self-managed MySQL database or ApsaraDB RDS for MySQL PolarDB-X AnalyticDB for MySQL V3.0 | The lower case table names _ _ _ parameter is set to 1 or 2. | Database names and table names in the destination instance are in lowercase. The capitalization of column names in the destination instance is the same as that in the source instance. |
|   | The lower case table names _ _ _ parameter is set to 0. | The capitalization of database names, table names, and column names in the destination instance is the same as that in the source instance. |
| AnalyticDB for MySQL V2.0 DataHub MaxCompute | N/A | Database names, table names, and column names in the destination instance are in lowercase. |
| Self-managed Oracle database | N/A | Database names, table names, and column names in the destination instance are in uppercase. |

| Self-managed SQL Server database or ApsaraDB RDS for SQL Server PolarDB for PostgreSQL (Compatible with Oracle) Self-managed PostgreSQL database or ApsaraDB RDS for PostgreSQL AnalyticDB for PostgreSQL Self-managed MongoDB database or ApsaraDB for MongoDB Self-managed Redis database or ApsaraDB for Redis | N/A | Database names and table names in the destination instance are in lowercase. The capitalization of column names in the destination instance is the same as that in the source instance. |
|---|---|---|

Consistent with the source database The capitalization of database names, table names, and column names in the destination instance is the same as that in the source instance. Consistent with the default policy of the destination database (uppercase) The names of all the databases, tables, and columns that are migrated or synchronized to the destination instance are in uppercase. Consistent with the default policy of the destination database (lowercase) The names of all the databases, tables, and columns that are migrated or synchronized to the destination instance are in lowercase.

#### 3.5.5 Data formats of a Kafka cluster

When you use Data Transmission Service (DTS) to migrate or synchronize data to a Kafka cluster, you can specify the format in which data is stored in the Kafka cluster. This topic describes the formats that you can use to store data in a Kafka cluster. You can parse data based on the definition of these data formats.

**Data formats**

DTS allows you to store data into a Kafka cluster in the following formats: DTS Avro: a data serialization format into which data structures or objects can be converted to facilitate storage and transmission. Shareplex Json: the format in which the data read from the source database by using the data replication software SharePlex is stored. Canal Json: the format in which data is stored in a Kafka cluster after Canal parses the logs about the incremental data of the source database and transmits the incremental data to the Kafka cluster.

**DTS Avro**

**DTS Avro** is the default data format. By default, data that is migrated or synchronized to a
Kafka cluster by using DTS is stored in the DTS Avro format. You must parse the data based on the schema definition of DTS Avro. For more information, visit GitHub.

> **Note:** In the DTS Avro format, the DDL statements are of the STRING type.

**Shareplex Json**

Table 1. Parameters related to the SharePlex JSON format

| Parameter | Description |
|---|---|
| time | The UTC time when the transaction in the database is committed. It is in the yyyy-MM-ddTHH:mm:ssZ format. |
| userid | The ID of the user who commits the transaction. |
| op | The operation type. Valid values: INSERT, UPDATE, DELETE, TRUNCATE, DROP COLUMN, UPDATE BEFORE, and UPDATE AFTER. |
| scn | The system change number (SCN) that identifies the version of the transaction that the database commits at a specific point in time. Each committed transaction is assigned a unique SCN. |
| rowid | A relatively unique address value that is used to identify a record in the database. |
| trans | The ID of the transaction. |
| seq | The sequence number of the operation in the transaction. It starts from 1. |
| size | The total number of operations in the transaction. |
| table | The name of the table. |
| idx | The index of the operation in the transaction, in the seq/size format. For example, 1/11 indicates that the sequence number of the operation is 1 in the transaction that contains a total number of 11 operations. |
| posttime | The time when the transaction is committed to the destination database. |

Examples: Data inserted `{`

```json
    "meta": {
        "time": "2017-06-16T14:24:34",
        "userid": 84,
        "op": "ins",
          "scn": "14589063118712",
          "rowid": "AAATGpAAIAAItcIAAA",
        "trans": "7.0.411499",
        "seq": 1,
        "size": 11,
        "table": "CL_BIZ1.MIO_LOG",
          "idx": "1/11",
        "posttime": "2017-06-16T14:33:52"
```

`},`

```json
    "data": {
        "MIO_LOG_ID": "32539737"
```

`}` `}` Data updated `{`

```json
    "meta": {
        "time": "2017-06-16T15:38:13",
        "userid": 84,
        "op": "upd",
        "table": "CL_BIZ1.MIO_LOG"
        ...
```

`},`

```json
    "data": {
        "CNTR_NO": "1171201606"
```

`},`

```json
    "key": {
        "MIO_LOG_ID": "32537893",
        "PLNMIO_REC_ID": "31557806",
        "POL_CODE": null,
        "CNTR_TYPE": null,
        "CNTR_NO": "1171201606syui26"
```

`}` `}` Data deleted `{`

```json
    "meta": {
        "time": "2017-06-16T15:51:35",
        "userid": 84,
        "op": "del",
```

`},`

```json
    "data": {
        "MIO_LOG_ID": "32539739",
        "PLNMIO_REC_ID": "31557806",
        "POL_CODE": null,
        "CNTR_TYPE": null,
        "CG_NO": null
```

`}` `}`

**Canal Json**

Table 2. Parameters related to the Canal JSON format

| Parameter | Description |
|---|---|
| database | The name of the database. |
| es | The time when the operation is performed on the database. The value is a 13-bit UNIX timestamp. Unit: milliseconds. Note You can use a search engine to obtain a UNIX timestamp converter. |
| id | The serial number of the operation. |
| isDdl | Indicates whether the operation is a DDL operation. Valid values: true: The operation is a DDL operation. false: The operation is not a DDL operation. |
| mysqlType | The data type of the field. |

| old and data | The data before and after update. Note For change tracking instances that are created before March 20, 2022, the value of old is the data after update and the value of data is the data before update. To keep consistent with the open source community, the value of data is the data after update and the value of old is the data before update for change tracking instances that are created or restarted as of March 20, 2022. |
|---|---|
| pkNames | The name of the primary key. |
| sql | The SQL statement. |
| sqlType | The data type of the field after conversion. For example, the type LONG is converted from UNSIGNED INTEGER and BIGDECIMAL from UNSIGNED LONG. |
| table | The name of the table. |
| ts | The time when the operation is written to the destination database. The value is a 13-bit UNIX timestamp. Unit: milliseconds. Note You can use a search engine to obtain a UNIX timestamp converter. |
| type | The operation type. Valid values: DELETE, UPDATE, and INSERT. |

Examples of data updated

> **Note:** For change tracking instances that are created before March 20, 2022, after the `DELETE` statements of the source table are synchronized, the value of `old` is data and the value of `data` is NULL. To keep consistent with the open source community, the value of
> `data` is data and the value of `old` is NULL for change tracking instances that are created or restarted as of March 20, 2022.

**Change tracking instances that are created before March 20, 2022**

`{`

```json
    "old": [
```

`{`

```json
            "shipping_type": "aaa"
```

`}` `],`

```json
    "database": "dbname",
    "es": 1600161894000,
    "id": 58,
    "isDdl": false,
    "mysqlType": {
        "id": "bigint(20)",
        "shipping_type": "varchar(50)"
```

`},`

```json
    "pkNames": [
        "id"
```

`],`

```json
    "sql": "",
    "sqlType": {
        "id": -5,
        "shipping_type": 12
```

`},`

```json
    "table": "tablename",
    "ts": 1600161894771,
    "type": "DELETE"
```

`}`

**Change tracking instances that are created or restarted as of March 20, 2022**

`{`

```json
    "data": [
```

`{`

```json
            "id": "500000287",
            "shipping_type": null
```

`}` `],`

```json
    "database": "dbname",
    "es": 1600161894000,
    "id": 58,
    "isDdl": false,
    "mysqlType": {
        "id": "bigint(20)",
        "shipping_type": "varchar(50)"
```

`},`

```json
    "pkNames": [
        "id"
```

`],`

```json
    "sql": "",
    "sqlType": {
        "id": -5,
        "shipping_type": 12
```

`},`

```json
    "table": "tablename",
    "ts": 1600161894771,
    "type": "DELETE"
```

`}` Example of a DDL operation `{`

```json
    "database": "dbname",    The name of the source database.
    "es": 1600161894000,    The time when the data is written to the binary logs of the
source database.
    "id": 58,      The offsets of DTS cache.
    "isDdl": true,       Indicates that the operation is a DDL operation.
    "sql": "eg: create xxx",      The DDL statements recorded in the binary logs.
    "table": "tablename",       The name of the table that is synchronized.
    "ts": 1600161894771,      The time when the data is written to the destination data
base by using DTS.
    "type":"DDL"
```

`}`

#### 3.5.6 Specify the policy for migrating data to Kafka partitions

**Kafka partitions**

When you configure a task to migrate data to a Kafka cluster, you can specify the policy for migrating data to Kafka partitions. The policy allows you to improve the migration performance. For example, you can migrate data to different partitions based on hash values.

**Hash algorithm**

Data Transmission Service (DTS) uses the hashCode() method in Java to calculate hash values.

**Configuration method**

In the **Configure Objects and Advanced Settings** step of a task creation wizard, you can specify the policy for migrating data to Kafka partitions.

> **Warning:** After a data migration task is started, do not change the number of partitions in the destination topic. Otherwise, data migration fails.

**Policies**

| Policy | Description | Advantage and disadvantage |
|---|---|---|
| Ship All Data to Partition 0 | DTS migrates all data and DDL statements to Partition 0 of the destination topic. | Advantage: The order in which all objects are created and changed is the same as that in the source database. Disadvantage: This policy provides ordinary migration performance. |
| Ship Data to Separate Partitions Based on Hash Values of Database and Table Names | DTS uses the database and table names as the partition key to calculate the hash value. Then, DTS migrates the data and DDL statements of each table to the corresponding partition of the destination topic. Note The data and DDL statements of the same table are migrated to the same partition. If a DDL statement is irrelevant to a table, for example, CREATE DATABASE, the statement is migrated to Partition 0. | Advantage: The order in which a destination table is created and changed is the same as that of the source table. This policy provides good migration performance. Disadvantage: Tables are migrated to different partitions. After data migration, the order of data changes on different tables may become inconsistent. |

| Ship Data to Separate Partitions Based on Hash Values of Primary Keys | DTS uses a table column as the partition key to calculate the hash value. The table column is the primary key by default. If a table does not have a primary key, the unique key is used as the partition key. DTS migrates each row to the corresponding partition of the destination topic. You can specify one or more columns as partition keys to calculate the hash value. Note If you use this policy, DDL statements are migrated to Partition 0 of the destination topic by default. If a table does not have a primary key or unique key, DTS migrates the data and DDL statements of the table to Partition 0 of the destination topic. | Advantage: This policy provides the best migration performance. Disadvantage: After data migration, the order of data changes on each data record remains the same. However, the order of data changes on different tables or tables without a primary key may become inconsistent. |
|---|---|---|

#### 3.5.7 Configure ETL in a data migration task

Data Transmission Service (DTS) provides the extract, transform, and load (ETL) feature to help you process streaming data in real time. The ETL feature is integrated with the data replication capabilities of DTS to achieve streaming data extraction, data transformation and processing, and data loading. The ETL feature can be used in the following scenarios: data filtering, data masking, recording of data modification time, and data change audit. This topic describes how to configure ETL in a data migration task.

**Background information**

DTS is used for data migration and real-time data transmission between data sources. In some cases, you may need to transform or filter real-time data before the data is written to a database. To meet such requirements, DTS provides the ETL feature and allows you to use domain-specific language (DSL) statements to process data in a flexible manner. For more information about DSL, see Overview of DSL.

**Supported databases**

The following table lists the source and destination databases that are supported by the ETL feature.

| Source database | Destination database |
|---|---|
| MySQL | AnalyticDB for PostgreSQL PostgreSQL MySQL Oracle |
| Self-managed Oracle database | MySQL AnalyticDB for PostgreSQL PostgreSQL |
| PolarDB for PostgreSQL (Compatible with Oracle) | PolarDB for PostgreSQL (Compatible with Oracle) |

| Self-managed Db2 for LUW database | AnalyticDB for PostgreSQL Note The ETL feature is supported only during incremental data migration. |
|---|---|
| PostgreSQL | PostgreSQL |

**Configure ETL when you create a data migration task**

**Usage notes**

If the ETL script that you configure contains the operation to add a column, you must manually add a column to the destination table. Otherwise, the ETL script does not take effect. For example, if you configure the ETL script script:e_set(`new_column`, dt_now()) , you must manually add the `new_column` column to the destination table.
1. Create a migration task based on your business requirements and proceed to the
**Advanced Settings** step.
2. Set the **Configure ETL** parameter to **Yes**. In the code editor, enter data processing
statements based on the DSL syntax. For more information, see the DSL syntax section in this topic.

> **Note:** If you want to drop entries whose values of the id column are greater than whether an entry is greater than a specific value. `id` is a variable. This way, entries whose values of the id column are greater than three are filtered out.

|   | script:e if(op gt(`id`, 3), e drop()) _ _ _ |
|---|---|
| op gt _ |   |

3. Click **Next: Precheck and Start Task** and complete the subsequent steps.

**Overview of DSL**

DSL is a scripting language that is designed to process data in data migration. You can use conditional functions to process data of the string, date, and numeric types. DSL boasts the following characteristics that help you process data in a flexible manner: Various functions: DSL provides a variety of functions and supports combined functions. Simple syntax: DSL is easy to use. For more information about how to use DSL to filter, convert, and mask data, see Typical scenarios. High efficiency: DSL has a minimal effect on the data migration performance because DSL uses the code generation mechanism.

**Typical scenarios**

Filter data Filter out data by a numeric column: If an entry whose value of the id column is greater than 10000, drop this entry so that it is not migrated to the destination database. Example: e_if(op_gt(`id`, 10000), e_drop). Filter out data by a specific string: If an entry whose value of the name column contains "hangzhou", drop this entry so that it is not migrated to the destination database. Example: e_if(str_contains(`name`, "hangzhou"), e_drop). Filter out data by date: If an entry whose timestamp of the order column is earlier than a specific point in time, drop this entry so that it is not migrated to the destination database. Example: e_if(op_lt(`order_timestamp`, "2015-02-23 23:54:55"), e_drop). Filter out data by multiple conditions: If an entry whose value of the id column is greater than 1000 and value of the name column contains "hangzhou", drop this entry so that it is not migrated to the destination database. Example: e_if(op_and(str_contains(`name`, "hangzhou"), op_gt(`id`, 1000)), e_drop()). If an entry whose value of the id column is greater than 1000 or value of the name column contains "hangzhou", drop this entry so that it is not migrated to the destination database. Example: e_if(op_or(str_contains(`name`, "hangzhou"), op_gt(`id`, 1000)), e_drop()). Mask data Mask the last four digits of a mobile phone number with four asterisks (*). Example: e_set(`phone`, str_mask(`phone`, 7, 10, '*')). Record the time when data is modified Add a column to all tables: If the value of the __OPERATION__ variable is INSERT, UPDATE, or DELETE, a column named dts_sync_time whose value is the same as the __COMMIT_TIMESTAMP__ variable of logs is added to all tables in the source database.

```
e_if(op_or(op_or(
        op_eq(__OPERATION__, __OP_INSERT__),
        op_eq(__OPERATION__, __OP_UPDATE__)),
        op_eq(__OPERATION__, __OP_DELETE__)),
    e_set(dts_sync_time, __COMMIT_TIMESTAMP__))
```

Add a column to a specific table: If the value of the __OPERATION__ variable is INSERT, UPDATE, or DELETE, a column named dts_sync_time whose value is the same as the __COMMIT_TIMESTAMP__ variable of logs is added to the dts_test_table table in the source database.

```
e_if(op_and(
      op_eq(__TB__,'dts_test_table'),
      op_or(op_or(
        op_eq(__OPERATION__,__OP_INSERT__),
        op_eq(__OPERATION__,__OP_UPDATE__)),
        op_eq(__OPERATION__,__OP_DELETE__))),
      e_set(dts_sync_time,__COMMIT_TIMESTAMP__))
```

> **Note:** To perform the preceding operations, you must add the dts_sync_time column to the corresponding tables in the destination database before the data migration task is started.

Audit data changes Record the type and time of the data changes in tables: 1. Record the data change type in the operation_type column of the destination database. 2. Record the time when data is changed in the updated column of the destination database.

```
e_compose(
    e_switch(
        op_eq(__OPERATION__,__OP_DELETE__), e_set(operation_type, 'DELETE'),
        op_eq(__OPERATION__,__OP_UPDATE__), e_set(operation_type, 'UPDATE'),
        op_eq(__OPERATION__,__OP_INSERT__), e_set(operation_type, 'INSERT')),
    e_set(updated, __COMMIT_TIMESTAMP__),
    e_set(__OPERATION__,__OP_INSERT__)
```

`)`

> **Note:** You must add the operation_type and updated columns to the tables in the destination database before the data migration task is started.

**DSL syntax**

**Constants and variables**

Constants

| Data type | Example |
|---|---|
| Int | 123 |
| Float | 123.4 |
| String | "hello1 world" _ |
| Boolean | true or false |
| Datetime | '2021-01-01 10:10:01' |

Variables

| Variable | Description | Data type | Example |
|---|---|---|---|
| TB __ __ | The table name. | String | table |
| DB __ __ | The name of the database. | String | mydb |
| OPERATION __ __ | The operation type. | String | OP INSERT , OP __ _ ____ _ UPDATE , OP DELE ____ _ TE __ |
| COMMIT TIMESTAM __ _ P __ | The time when the transaction was committed. | Datetime | '2021-01-01 10:10:01' |
| `column` | The column name. | String | `id` or `name` |

**Expression functions**

Arithmetic operators

| Operati on | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|
| Addition | op sum( _ value1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op sum(`col1`, 1.0) _ |
| Subtracti on | op sub(v _ alue1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op sub(`col1`, 1.0) _ |
| Multiplic ation | op mul(v _ alue1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op mul(`col1`, 1.0) _ |
| Division | op div tr _ _ ue(value 1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op div true(`col1`, _ _ 2.0). In this example, if the col1 value is 15, 7.5 is returned. |
| Modulo | op mod( _ value1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op mod(`col1`, 10). In _ this example, if the col1 value is 23, 3 is returned. |

Logical operators

| Operati on | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|
| Equal to | op eq(va _ lue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false, in the Boolean type | op eq(`col1`, 23) _ |

| Greater than | op gt(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false, in the Boolean type | op gt(`col1`, 1.0) _ |
|---|---|---|---|---|
| Less than | op lt(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false, in the Boolean type | op lt(`col1`, 1.0) _ |
| Greater than or equal to | op ge(va _ lue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false, in the Boolean type | op ge(`col1`, 1.0) _ |
| Less than or equal to | op le(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false, in the Boolean type | op le(`col1`, 1.0) _ |
| AND | op and(v _ alue1, value2) | value1: a Boolean value value2: a Boolean value | true or false, in the Boolean type | op and(`is male`, _ _ `is student`) _ |
| OR | op or(val _ ue1, value2) | value1: a Boolean value value2: a Boolean value | true or false, in the Boolean type | op or(`is male`, _ _ `is student`) _ |

**String functions**

| Purpose | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|

| Format strings and append strings | str form _ at(format , value1, value2, value3, ...) | format: a string. Braces ({}) are used as placeholders. Example: "part1: {}, part2: {}". value1: an arbitrary value. value2: an arbitrary value. | The string after the format operation | str format("part1: {}, _ part2: {}", `col1`, `col2`). In this example, if the col1 value is ab and the col2 value is 12, "part1: ab, part2: 12" is returned. |
|---|---|---|---|---|
| Replace strings | str repla _ ce(origin al, oldStr, newStr, count) | original: the original string. oldStr: the string to be replaced. newStr: the string after the replacement. count: an integer that specifies the maximum number of times that a string can be replaced. A value of -1 specifies that all oldStr is replaced with newStr. | The string after the replace operation | Example 1: str replace(`name`, _ "a", 'b', 1). In this example, if the name is aba, bba is returned. Example 2: str replace(`name`, _ "a", 'b', -1). In this example, if the name is aba, bbb is returned. |
| Remove specific characte rs at the start and end of a string | str strip( _ string va _ l, charSet) | string val: the _ original string char set: the set of _ the first characters and the last characters of the string | The string after the remove operation | str strip(`name`, _ 'ab'). In this example, if the name is axbzb, xbz is returned. |
| Convert strings to lowercas e letters | str lower _ (value1) | value1: a column of the string type or a string constant | The string after the convert operation | str lower(`str col`) _ _ |
| Convert strings to uppercas e letters | str upper _ (value1) | value1: a column of the string type or a string constant | The string after the convert operation | str upper(`str col`) _ _ |
| Count strings | str count _ (str, pattern) | str: a column of the string type or a string constant pattern: the substring to query | The number of times for which the substring appears | str count(`str col`, _ _ 'abc'). In this example, if the str col _ value is zabcyabcz, 2 is returned. |

| Query strings | str find(s _ tr, pattern) | str: a column of the string type or a string constant pattern: the substring to query | The position in which the substring matches for the first time. If no match is found, -1 is returned. | str find(`str col`, _ _ 'abc'). In this example, if the str col _ value is xabcy, 1 is returned. |
|---|---|---|---|---|
| Determin e whether a string contains only letters | str isalp _ ha(str) | str: a column of the string type or a string constant | true or false | str isalpha(`str col`) _ _ |
| Determin e whether a string contains only digits | str isdigi _ t(str) | str: a column of the string type or a string constant | true or false | str isdigit(`str col`) _ _ |
| Mask part of a string with specific characte rs. This operatio n can be used for data masking. For example, mask the last four digits of a mobile phone number with four asterisks (*). | str mask _ (str, start, end, maskStr) | str: a column of the string type or a string constant start: an integer that specifies the start position of the masking. The minimum value is 0. end: an integer that specifies the end position of the masking. The maximum value is the length of the string minus 1. maskStr: a string. The length is 1. Example: #. | The string whose part from start to end is masked with specified characters | str mask(`phone`, 7, _ 10, '#') |
| Query the DateTim e value of the current time zone | dt now() _ | N/A | The DateTime value of the current time zone | e set(`dt col`, _ _ dt now()) _ |

| Query the DateTim e value of the current time zone in UTC | dt utcno _ w() | N/A | The DateTime value of the current time zone in UTC | e set(`dt col`, _ _ dt utcnow()) _ |
|---|---|---|---|---|

**Global functions**

Flow control functions

| Purpose | Syntax | Description | Example |
|---|---|---|---|
| The IF statement | e if(bool exp _ _ r, func invoke) _ | bool expr: a Boolean _ constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke: a function. _ Valid values: e drop,e keep,e set,e if,e c _ _ _ _ _ ompose. | e if(op gt(`id`, 10), e drop()). _ _ _ In this example, if an entry whose value of the id column is greater than 10, this entry is dropped. |
| The IF ELSE statement | e if else(bool _ _ expr, _ func invoke1 _ , func invoke2 _ ) | bool expr: a Boolean _ constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke1: a function. _ Invoke this function if the condition is true. func invoke2: a function. _ Invoke this function if the condition is false. | e if else(op gt(`id`, 10), _ _ _ e set(`tag`, 'large'), _ e set(`tag`, 'small')). In this _ example, if an entry whose value of the id column is greater than 10, the tag column is set to large. Otherwise, the tag column is set to small. |
| The SWITCH statement that contains multiple conditions and a default operation | s switch(con _ dition1, func1, condition2, func2, ..., default = default func) _ | condition1: a Boolean constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke: a function. If _ condition1 is true, invoke this function and finish the statement. Otherwise, proceed to the next condition. default func: a function. If _ the preceding conditions are false, invoke this function. | e switch(op gt(`id`, 100), _ _ e set(`str col`, '>100'), _ _ op gt(`id`, 90), e set(`str col`, _ _ _ '>90'), default=e set(`str col`, _ _ '<=90')) |

| Combine multiple operations | e compose(f _ unc1, func2, func3, ...) | func1: a function. Valid values: e set, e drop, and _ _ e if. _ func2: a function. Valid values: e set, e drop, and _ _ e if. _ | e compose(e set(`str col`, _ _ _ 'test'), e set(`dt col`, _ _ dt now())). In this example, the _ value of the str col column is _ set to test, and the value of the dt col column is set to the _ current time. |
|---|---|---|---|

Data manipulation functions

| Purpose | Syntax | Description | Example |
|---|---|---|---|
| Drop an entry so that it is not migrated to the destination database | e drop() _ | N/A | e if(op gt(`id`, 10), e drop()). _ _ _ In this example, entries whose values of the id column are greater than 10 are dropped. |
| Retain an entry so that it is migrated to the destination database | e keep(condi _ tion) | condition: a Boolean expression | e keep(op gt(id, 1)). In this _ _ example, only entries whose values of the id column are greater than one are migrated. |
| Set the value of a column | e set(`col`, _ val) | col: the name of the column. val: a constant or a function. The data type of the val value must match the data type of the col value. | e set(`dt col`, dt now()). In _ _ _ this example, the value of the dt col column is set to _ the current time. e set(`col1`, `col2` + 1). In _ this example, the value of the col1 column is set to the value of the col2 column plus 1. |

### 3.6 Precheck items

#### 3.6.1 Source database connectivity

Data Transmission Service (DTS) checks whether DTS servers can connect to the source database for migration. DTS creates a connection to the source database by using the Java Database Connectivity (JDBC) protocol. If the connection fails, the data migration task fails to pass the connectivity check. The following table describes the possible reasons for a connectivity precheck failure of the source database.

| Check item | Possible reason | Troubleshooting |
|---|---|---|
| JDBC | 1. The username or password of the database account is incorrect, or the IP address or port number of the destination database is incorrect. 2. The database account cannot be used to access the destination database over an endpoint. | 1. Check and correct the connection information about the destination database. 2. Allow access to the destination database over all endpoints. |

| Ping | 1. The network of the service to which the database instance belongs is unavailable. 2. The IP address of the destination database is incorrect. | 1. Check whether the network is available. 2. Check and correct the IP address of the destination database. |
|---|---|---|
| Telnet | 1. The DTS servers are not allowed to access the destination database. 2. The port number of the destination database is incorrect. | 1. Allow access to the destination database from the public CIDR blocks of the DTS servers. For example, disable the firewall of the service to which the destination database belongs or add the public CIDR blocks of the DTS servers to the whitelist of the destination database. 2. Check and correct the port number of the destination database. |

#### 3.6.2 Destination database connectivity

This check item checks whether the Data Transmission Service (DTS) servers can connect to the destination database for migration. DTS creates a connection to the destination database by using the Java Database Connectivity (JDBC) protocol. If the connection fails, the check item fails. The following table describes the possible reasons for a connectivity precheck failure of the destination database.

| Check item | Possible reason | Troubleshooting |
|---|---|---|
| JDBC | 1. The username or password of the database account is incorrect, or the IP address or port number of the destination database is incorrect. 2. The database account cannot be used to access the destination database over an endpoint. | 1. Check and correct the connection information about the destination database. 2. Allow access to the destination database over all endpoints. |
| Ping | 1. The network of the service to which the database instance belongs is unavailable. 2. The IP address of the destination database is incorrect. | 1. Check whether the network is available. 2. Check and correct the IP address of the destination database. |

| Telnet | 1. The DTS servers are not allowed to access the destination database. 2. The port number of the destination database is incorrect. | 1. Allow access to the destination database from the public CIDR blocks of the DTS servers. For example, disable the firewall of the service to which the destination database belongs or add the public CIDR blocks of the DTS servers to the whitelist of the destination database. 2. Check and correct the port number of the destination database. |
|---|---|---|

#### 3.6.3 Binary logging configurations of the source database

**source database**

**Whether binary logging is enabled in the source database**

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether binary logging is enabled in the source database. If binary logging is disabled in the source database, the check result is Failed. Troubleshooting: Run the `log_bin=mysql_bin` command to modify the configuration file of the source database. Restart the source database and run a precheck again.

**Binary log format of the source database**

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the binary log format is set to ROW in the source database. If the binary log format is not set to ROW in the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_format=ROW` command in the source database and run a precheck again. We recommend that you restart the MySQL process. Otherwise, data loss may occur because sessions will continue to be written in a non-ROW mode.

**Binary log files in the source database**

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether specific binary log files are removed from the source database. If binary log files in the source database are incomplete, the check result is Failed. Troubleshooting: Run the `PURGE BINARY LOGS TO 'The name of the first binary log file` `that is not deleted'` command in the source database and run a precheck again. To find the binary log files that are removed from the source database, click the info icon next to the failed item. In the **View Details** dialog box, the names of deleted binary log files are displayed.

**Parameter binlog_row_image of the source database**

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of the binlog_row_image parameter in the source database is set to FULL. This parameter indicates whether the full image is recorded. If the full image is not recorded in binary log files of the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_row_image=FULL` command in the source database and run a precheck again.

#### 3.6.4 Integrity of the FOREIGN KEY constraints

**constraints**

DTS checks whether the parent table on which a child table depends is included in the selected objects. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. If the parent table on which a child table depends is not included in the selected objects, the check result is Failed. Troubleshooting: Do not migrate the child tables that cause the check failure. To do this, remove these child tables from the selected objects and run a precheck again. Migrate the parent tables rather than the child tables. To do this, add the parent tables to the selected objects and run a precheck again. Delete the foreign key dependencies between the parent and child tables in the source database and run a precheck again.

#### 3.6.5 Existence of FEDERATED tables

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the source database contains storage engines that are not supported by incremental data migration. Incremental data migration does not support the FEDERATED and MRG_MyISAM storage engines. If **the FEDERATED storage engine is used by specific tables in the source database**, the check result is Failed. If **the MRG_MyISAM storage engine is used by specific tables in the source**
**database**, the check result is Failed.
Solution: Remove the tables that use the FEDERATED or MRG_MyISAM storage engine from the selected objects. Then, create a separate migration task to perform schema migration and full data migration for these tables.

#### 3.6.6 Permissions

**Source database permissions**

DTS checks whether the account of the source database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks.

**Destination database permissions**

DTS checks whether the account of the destination database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks.

#### 3.6.7 Object name conflict

DTS checks whether the destination database contains objects that have the same names as the objects to be migrated. If the destination database contains objects that have the same names as the objects to be migrated, the check result is Failed. This causes migration failure. If the check result is Failed, an error message is displayed indicating that an object in the destination database has the same name as an object to be migrated. Troubleshooting: Use the object name mapping feature to map the conflicting object name to an object with a different name in the destination database. In the destination database, delete or rename the object that has the same name as the object to be migrated. Remove the conflicting object from the objects to be migrated.

#### 3.6.8 Schema existence

This check item checks whether the database to be migrated exists in the destination instance. If the database does not exist in the destination instance, Data Transmission Service (DTS) automatically creates one. However, the check fails if DTS cannot automatically create the database in the following scenarios: The name of the database to be migrated contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). Cause of failure: The name of the source database is invalid. Troubleshooting: On the Databases page of the RDS console, create a database that meets requirements, and grant the migration account the read and write permissions on the new database. Use the database name mapping feature of DTS to map the source database to the new database. Then, perform a precheck again. The character set of the database to be migrated is not UTF-8, GBK, Latin1, or UTF-8MB4. Cause of failure: The character set of the source database is not supported. Troubleshooting: On the Databases page of the RDS console, create a database that meets requirements, and grant the migration account the read and write permissions on the new database. If the new database and the database to be migrated have different names, you can use the database name mapping feature of DTS to map the database to be migrated to the new database. Then, perform a precheck again. The migration account of the destination database has no read and write permissions on the database to be migrated. Cause of failure: You are not authorized to perform operations on the source database. Troubleshooting: On the Accounts tab of the Databases page in the RDS console, grant the migration account the read and write permissions on the database to be migrated. Then, perform a precheck again.

#### 3.6.9 Value of server_id in the source database

**database**

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of **server-id** in the source database is set to an integer greater than 1. If the check result is Failed, run the `set global server_id='An integer greater than 1'` command in the source database and perform a precheck again.

#### 3.6.10 Source database version

To ensure successful data migration, Data Transmission Service (DTS) checks the version number of the source database during precheck. DTS checks whether the version of the source database is supported. For information about the source database versions that are supported by DTS, see Supported databases and migration types. If the version check fails, you must upgrade or downgrade the source database to a version that is supported by DTS and then perform a precheck again.

### 3.7 Data type mappings between heterogeneous databases

**heterogeneous databases**

Heterogeneous databases support different data types. During schema migration, Data Transmission Service (DTS) converts the data types of the source database into those of the destination database. This topic describes the data type mappings in detail to help you evaluate the impact of data migration on your business.

**Migrate data from an ApsaraDB RDS for MySQL instance or a**

**self-managed MySQL database**

The following table describes the data type mappings between MySQL and heterogeneous databases. The source instance can be a PolarDB for MySQL cluster, an ApsaraDB RDS for MySQL instance, or a self-managed MySQL database. The destination instance can be an AnalyticDB for MySQL cluster or an AnalyticDB for PostgreSQL instance.

> **Note:** If the value range of the data to be migrated from the source instance exceeds the range supported by DTS, the accuracy of the data migrated to the destination instance decreases.

| Type | Data type of the source instance | Value range | Data type of a Message Queue for Apache Kafka instance or a self- managed Kafka cluster |
|---|---|---|---|
| Integer | BIT[(M)] | 1 to 64 |   |
|   | TINYINT[(M)] | -128 to 127 |   |
|   | TINYINT[(M)] [UNSIGNED] | 0 to 255 |   |
|   | SMALLINT[(M)] | -32768 to 32767 |   |
|   | SMALLINT[(M)] [UNSIGNED] | 0 to 65535 |   |
|   | MEDIUMINT[(M)] | -8388608 to 8388607 |   |
|   | MEDIUMINT[(M)] [UNSIGNED] | 0 to 16777215 |   |
|   | INT[(M)] | -2147483648 to 2147483647 |   |
|   | INT[(M)] [UNSIGNED] | 0 to 4294967295 |   |

|   | BIGINT[(M)] | - 922337203685477580 8 to 922337203685477580 7 |   |
|---|---|---|---|
|   | BIGINT[(M)] [UNSIGNED] | 0 to 184467440737095516 15. |   |
|   | DECIMAL[(M[,D])] | M: 0 to 65 D: 0 to 30 |   |
| Decimal |   |   | Consistent with the data types of MySQL |
|   | FLOAT(p) | 1.175494351E-38 ~ 3.402823466E+38 |   |
|   | DOUBLE[(M,D)] | 2.2250738585072014 E-308 ~ 1.7976931348623157 E+308 |   |
| Date and time | DATE | 1000-01-01 to 9999- 12-31 Note The format is YYYY- MM-DD, in UTC. |   |
|   | DATETIME[(fsp)] | 1000-01-01 00:00:00.000000 to 9999-12-31 23:59:59.999999 Note The format is YYYY- MM-DD hh:mm:ss[.fractio n], in UTC. |   |
|   | TIMESTAMP[(fsp)] | 1970-01-01 00:00:01.000000 to 2038-01-19 03:14:07.999999 Note The format is YYYY- MM-DD hh:mm:ss[.fractio n], in UTC. |   |
|   | TIME[(fsp)] | -838:59:59.000000 to 838:59:59.000000 Note The format is hh:mm:ss[.fractio n], in UTC. |   |
|   | YEAR[(4)] | 1901 to 2155, or 0000 |   |

| String | CHAR[(M)] | 0 to 255 characters |   |
|---|---|---|---|
|   | VARCHAR(M) | 0 to 65,535 characters |   |
|   | BINARY[(M)] | 0 to 255 bytes |   |
|   | VARBINARY(M) | 0 to 65,535 bytes |   |
|   | TINYBLOB | 255 (2^8 - 1) bytes |   |
|   | TINYTEXT | 255 (2^8 - 1) characters |   |
|   | BLOB | 65,535 (2^16 - 1) bytes |   |
|   | TEXT | 65,535 (2^16 - 1) characters |   |
|   | MEDIUMBLOB | 16,777,215 (2^24 - 1) bytes |   |
|   | MEDIUMTEXT | 16,777,215 (2^24 - 1) characters |   |
|   | LONGBLOB | 4,294,967,295 or 4 GB (2^32 - 1) bytes |   |
|   | LONGTEXT | 4,294,967,295 or 4 GB (2^32 - 1) characters |   |
|   | ENUM('value1','value2' ,...) | An ENUM column can have a maximum of 65,535 distinct elements. |   |
|   | SET('value1','value2',.. .) | A SET column can have a maximum of 64 distinct elements. |   |
| Spatial | GEOMETRY | Geometry values of any type |   |
|   | POINT | N/A |   |
|   | LINESTRING | N/A |   |
|   | POLYGON | N/A |   |
|   | MULTIPOINT | N/A |   |
|   | MULTILINESTRING | N/A |   |
|   | MULTIPOLYGON | N/A |   |
|   | GEOMETRYCOLLECTIO N | A collection of geometry values of any type |   |
| JSON | JSON | N/A |   |

**Migrate data from an Oracle database**

The following table describes the data type mappings between a self-managed Oracle database and heterogeneous databases. The destination instance can be a self-managed MySQL database, a PolarDB for MySQL cluster, an AnalyticDB for MySQL cluster, an AnalyticDB for PostgreSQL instance, or a PolarDB for Oracle cluster.

> **Note:** If the value range of the data to be migrated from the source instance exceeds the range supported by DTS, the accuracy of the data migrated to the destination instance decreases.

| Type | Data type of Oracle | Value range | Data type of MySQL or PolarDB-X | Data type of AnalyticDB for PostgreSQL | Data type of PolarDB for Oracle |
|---|---|---|---|---|---|
| Numeric | NUMBER(p,s) | 1 to 22 bytes. The argument p indicates precision. Valid values: 1 to 38. The argument s indicates scale. Valid values: -84 to 127. | DECIMAL[(p[,s ])] | DECIMAL \| TINYINT \| SMALLINT \| INTEGER \| BIGINT | NUMBER(p,s) |
|   | FLOAT(p) | 1 to 22 bytes. The variable p indicates a pointer. Valid values: 1 to 126, in units of bits. | DOUBLE | DOUBLE PRECISION | DOUBLE PRECISION |
|   | BINARY FLOA _ T | A 32-bit floating-point number (4 bytes) | DECIMAL(65, 8) | DOUBLE PRECISION | REAL |
|   | BINARY DOU _ BLE | A 64-bit floating-point number (8 bytes) | DOUBLE | DOUBLE PRECISION | DOUBLE PRECISION |
|   | DATE | N/A | DATETIME | TIMESTAMP(0 ) | DATE |
|   | TIMESTAMP [(fractional s _ econds precis _ ion)] | N/A | DATETIME[(fr actional seco _ nds precision _ )] | TIMESTAMP | TIMESTAMP [(fractional s _ econds precis _ ion)] |
|   | TIMESTAMP [(fractional s _ econds precis _ ion)] WITH TIME ZONE | N/A | DATETIME[(fr actional seco _ nds precision _ )] | TIMESTAMP WITH TIME ZONE | TIMESTAMP [(fractional s _ econds precis _ ion)] WITH TIME ZONE |

| Date and |   |   |   |   |   |
|---|---|---|---|---|---|
|   | TIMESTAMP [(fractional s _ econds precis _ ion)] WITH LOCAL TIME ZONE | N/A | DATETIME[(fr actional seco _ nds precision _ )] | TIMESTAMP WITH TIME ZONE | TIMESTAMP [(fractional s _ econds precis _ ion)] WITH TIME ZONE |
| time |   |   |   |   |   |
|   | INTERVAL YEAR [(year precisi _ on)] TO MONTH | N/A | Not supported | VARCHAR(32) | INTERVAL |
|   | INTERVAL DAY [(day precisio _ n)] TO SECOND [(fractional s _ econds precis _ ion)] | N/A | Not supported | VARCHAR(32) | INTERVAL |
| String | CHAR [(size [BYTE \| CHAR])] | 2,000 bytes | CHAR[(n)] | CHAR | CHAR [(size [BYTE \| CHAR])] |
|   | NCHAR[(size)] | 2,000 bytes | NATIONAL CHAR[(n)] | VARCHAR | NCHAR[(size)] |
|   | VARCHAR2(si ze [BYTE \| CHAR]) | If MAX STRING _ _ SIZE is set to EXTENDED, the maximum size is 32,767 bytes. If MAX STRING _ _ SIZE is set to STANDARD, the maximum size is 4,000 bytes. | VARCHAR(n) | VARCHAR | VARCHAR2(si ze [BYTE \| CHAR]) |
|   | NVARCHAR2( size) | If MAX STRING _ _ SIZE is set to EXTENDED, the maximum size is 32,767 bytes. If MAX STRING _ _ SIZE is set to STANDARD, the maximum size is 4,000 bytes. | NATIONALVA RCHAR[(n)] | VARCHAR | NVARCHAR2( size) |
|   | LONG | The maximum size is 2 GB (2^31 - 1). | LONGTEXT | TEXT | LONG |

|   | RAW(size) | The maximum size is 32,767 bytes or 2,000 bytes. | VARBINARY(2 000) | BYTEA | RAW(size) |
|---|---|---|---|---|---|
|   | LONG RAW | The maximum size is 2 GB. | LONGBLOB | BYTEA | LONG RAW |
|   | CLOB | The maximum size is (4 GB - 1) × DB BLOCK SI _ _ ZE. | LONGTEXT | TEXT | CLOB |
|   | NCLOB | The maximum size is (4 GB - 1) × DB BLOCK SI _ _ ZE. | LONGTEXT | TEXT | CLOB |
|   | BLOB | The maximum size is (4 GB - 1) × DB BLOCK SI _ _ ZE. | LONGBLOB | BYTEA | BLOB |
|   | BFILE | The maximum size is 4 GB. | Not supported | Not supported | Not supported |
| JSON | JSON | The maximum size is 32 MB. | Not supported | JSON | JSON |
| ROWID | ROWID | 64 characters | Not supported | OID | VARCHAR |
| Spatial | Customizatio n required | Not supported |   |   |   |

> **Note:** Destination instance: MySQL or PolarDB-X
> If a field of the CHAR data type in the source database is greater than 255 bytes in length, DTS converts this field to the VARCHAR(n) data type in the destination database.
> MySQL does not support the following Oracle data types: BFILE, INTERVAL YEAR TO MONTH, and INTERVAL DAY TO SECOND. Therefore, DTS does not convert these data types during schema migration.
> If a table to be migrated contains these data types, schema migration fails. You must make sure that the columns of these data types are excluded from the objects to be migrated.
> The TIMESTAMP data type of MySQL databases does not contain the time zone information. However, the TIMESTAMP WITH TIME ZONE and TIMESTAMP WITH LOCAL TIME ZONE data types in Oracle databases provide the time zone information. Therefore, DTS converts the values of the latter two data types to UTC time in the destination database.
> Destination instance: AnalyticDB for PostgreSQL
> If an Oracle data type is not supported by AnalyticDB for PostgreSQL, DTS converts the data type to BYTEA. If the conversion fails, DTS sets the field value to NULL.

### 3.8 Create an account for a self-managed MySQL database and configure binary logging

**managed MySQL database and**

**configure binary logging**

Before you use Data Transmission Service (DTS) to migrate, synchronize, or track data from a self-managed MySQL database, you must create a database account and configure binary logging.

**Scenarios and required permissions**

| Scenario | Required permission |
|---|---|
| The source database of a data migration task is a self-managed MySQL database, and you want to perform Incremental data migration . | The SELECT permission on the objects to be migrated, the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions, and the permissions to create databases and tables. The permissions allow DTS to create a database named dts to record heartbeat data during migration. |

| The source database of a data synchronization task is a self-managed MySQL database. | The SELECT permission on the objects to be synchronized, the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions, and the permissions to create databases and tables. The permissions allow DTS to create a database named dts to record heartbeat data during synchronization. |
|---|---|
| The source database of a change tracking task is a self-managed MySQL database. | The SELECT permission on the objects for change tracking, the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions, and the permissions to create databases and tables. The permissions allow DTS to create a database named dts to record heartbeat data during change tracking. |

**Impact**

To perform the operations described in this topic, you must restart the MySQL service. We recommend that you perform the operations during off-peak hours.

**Procedure**

1. Log on to the self-managed MySQL database.
2. Execute the following statement to create an account for data migration or synchronization
in the self-managed MySQL database:

```
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

> **Note:** username: the account to be created.
> host: the host from which the account can be used to log on to the database. If you set this parameter to a percent sign (%), the account can be used to log on to the database from all hosts.
> password: the password of the account.

For example, you can execute the following statement to create an account named dtsmigration. The password is Dts123456. The account is allowed to log on to the database from all hosts.

```
CREATE USER 'dtsmigration'@'%' IDENTIFIED BY 'Dts123456';
```

3. Execute the following statements to grant permissions to the account. For more
information, see Scenarios and required permissions. Execute the following statement to grant the account the permissions on the specified databases and tables:

```
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

Execute the following statement to grant the account the permissions to create databases and tables:

```
GRANT CREATE ON *.* TO 'username'@'host' WITH GRANT OPTION;
```

> **Note:** privileges: the operation permissions to be granted to the account, such as SELECT, INSERT, and UPDATE. To grant all permissions to the account, set this parameter to ALL.
> databasename: the name of the self-managed MySQL database. To grant the operation permissions of all databases to the account, set this parameter to an asterisk (*).
> tablename: the name of the table whose data you want to migrate. To grant the operation permissions of all tables to the account, set this parameter to an asterisk (*).
> username: the account to which you want to grant permissions.
> host: the host from which the account is allowed to log on to the database. If you set this parameter to a percent sign (%), the account is allowed to log on to the database from all hosts.
> WITH GRANT OPTION: grants the account the permission to run the GRANT command. This parameter is optional.

For example, you can execute the following statement to grant all permissions on databases and tables to the dtsmigration account, and allow the account to log on to the database from all hosts.

```
GRANT ALL ON *.* TO 'dtsmigration'@'%';
```

4. Enable binary logging for the self-managed MySQL database and set parameters.
For Linux systems, perform the following steps: a. Run the `vim` command and modify the following parameters in the my.cnf configuration file:

```
log_bin=mysql_bin binlog_format=row server_id=2 # Set this parameter to an integer greater than 1. binlog_row_image=full # You must set this parameter if the engine version of the self-managed MySQL database is later than 5.6.
```

b. Run the following commands to restart the MySQL process:

```
/etc/init.d/mysqld restart
```

> **Note:** You can run other commands or use other methods to restart MySQL.

For Windows systems, perform the following steps: a. Run the following commands to modify the parameters in the my.cnf configuration file:

```
log_bin=mysql_bin binlog_format=row server_id=2 # Set this parameter to an integer greater than 1. binlog_row_image=full # You must set this parameter if the version of the self-ma naged MySQL database is later than 5.6.
```

b. Restart the MySQL service.

> **Note:** You can restart the MySQL service by using the Windows service manager or by running the following commands:

```
net stop mysql net start mysql
```

### 3.9 Enable logging and grant fine-grained permissions to an Oracle database account

**grained permissions to an Oracle**

**database account**

This topic describes how to enable logging and grant fine-grained permissions to an Oracle database account.

> **Important:** If you need to migrate incremental data from an Oracle database but the database administrator (DBA) permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account.

1. Enable archive logging and supplemental logging.

| Log type | Procedure |
|---|---|
| Archive logging | Execute the following statements to enable archive logging: shutdown immediate; startup mount; alter database archivelog; alter database open; archive log list; |

| Supplemental logging | Enable supplemental logging at the database or table level based on your business requirements: Note You can enable database-level supplemental logging to ensure the stability of Data Transmission Service (DTS) tasks. You can enable table-level supplemental logging to reduce the disk usage of the source Oracle database. Enable database-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Execute the following statement to enable primary key and unique key supplemental logging at the database level: alter database add supplemental log data (primary key,unique index) columns; Enable table-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Use one of the following methods to enable table-level supplemental logging: Enable primary key supplemental logging at the table level alter table table name add supplemental log data (primary _ key) columns; Enable table-level supplemental logging for all columns alter table tb name add supplemental log data (all) _ columns; |
|---|---|
| Force logging | Execute the following statement to enable force logging: alter database force logging; |

2. Grant fine-grained permissions to an Oracle database account.

**Oracle versions 9i to 11g**

```bash
# Create a database account named rdsdt_dtsacct and grant permissions to the account.
create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; -- system tables grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; grant select_catalog_role TO rdsdt_dtsacct;
```

**Oracle versions 12c to 19c that use the multitenant**

**architecture**

```bash
# Switch to the pluggable database (PDB). Create a database account named rdsdt_dtsac
ct and grant permissions to the account. ALTER SESSION SET container = ORCLPDB1; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grantselecton alltabcolstordsdtdtsacct;
```

```bash
grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; -- V$PDBS privileges grant select on V_$PDBS to rdsdt_dtsacct; grant select on v$database to rdsdt_dtsacct; grant select on dba_objects to rdsdt_dtsacct; grant select on DBA_TAB_COMMENTS to rdsdt_dtsacct; grant select on dba_tab_cols to rdsdt_dtsacct; grant select_catalog_role TO rdsdt_dtsacct;
# Switch to the CDB$ROOT, which is the root container of the container database (CDB)
. Create a database account and grant permissions to the account. ALTER SESSION SET container = CDB$ROOT;
# Create a database account named rdsdt_dtsacct and grant permissions to the account.
You must modify the default parameters of the Oracle database. alter session set "_ORACLE_SCRIPT"=true; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant select on v_$logmnr_contents to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

**Oracle 12c to 19c (non-tenant mode)**

```bash
# Create a database account named rdsdt_dtsacct and grant permissions to the account.
create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; grant select on v$database to rdsdt_dtsacct; grant select on dba_objects to rdsdt_dtsacct; grant select on DBA_TAB_COMMENTS to rdsdt_dtsacct; grant select on dba_tab_cols to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select_catalog_role TO rdsdt_dtsacct;
```

### 3.10 Configure RAM authorization for cross-account data migration or synchronization

**for cross-account data migration**

**or synchronization**

When you configure cross-account migration or synchronization in Data Transmission Service (DTS), you need to configure RAM authorization for the Apsara Stack account to which the source or destination instance belongs. This topic describes how to configure the RAM authorization.

**Background information**

When you use DTS to migrate or synchronize data across Apsara Stack accounts, you must create RAM users for the Apsara Stack account to which the database instance belongs (hereinafter referred to as Account A). You must specify the Apsara Stack account on which you configure a DTS task (hereinafter referred to as Account B) as a trusted account and authorize Account B to access the cloud resources of Account A by using DTS.

**Precautions**

When you configure a DTS task across accounts, you need to purchase a DTS instance across Apsara Stack accounts and make sure that the network between the two Apsara Stack accounts are established and related configurations are complete. For more information, contact Apsara Stack technical support.

**Procedure**

1. Go to the **Create RAM Role & Attach Policy** page.
i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, click **Enterprise**. iii. In the left-side navigation pane, choose **Permissions > Role Permissions**. iv. In the **Role Permissions** page, click the icon. v. In the lower part of the **Create Custom Role** page, click **Advanced Settings** and click
**Create RAM Role & Attach Policy** .
2. Configure parameters for the RAM role.

| Parameter | Description |
|---|---|
| Role name | The name of the RAM role. In this example, ram-for-dts is used. |
| Description | Optional. The description for the RAM role. |

| Sharing Scope | Default value: Global. |
|---|---|

3. Click **Next** and configure the permission policy.
i. On the page that appears, click **Create Policy**. ii. Configure the permission policy.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |
| Sharing Scope | Default value: Global. |

| Description | Optional. The description for the policy. |
|---|---|
| Policy Content | The content of the policy depends on the database type. The number of characters in a RAM policy content cannot exceed the predefined limit. You cannot enter the complete policy for DTS in this field. The following example shows part of the policy content for MySQL and PolarDB-X 1.0. For more information, see Complete policy. { "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "*" }, { "Action": [ "rds:Describe*", "rds:CreateDBInstance", "rds:CreateAccount*", "rds:CreateDataBase*", "rds:ModifySecurityIps", "rds:GrantAccountPrivilege" ], "Resource": "*", "Effect": "Allow" }, { "Action": [ "drds:DescribeDrds*", "drds:ModifyDrdsIpWhiteList", "drds:DescribeRegions", "drds:DescribeRdsList", "drds:CeateDrdsDB", "drds:DescribeShardDBs" ], "Resource": "*", "Effect": "Allow" } ], "Version": "1" } |

iii. Click **OK**. iv. Select the created policy and click **Next**.
4. Configure the trust policy.

| Parameter | Description |
|---|---|
| Trust Organization | Select the level-1 organization in which the DTS task is created. |
| Trust Cloud Service | Select dts.aliyuncs.com. |
| Trust Policy | If you select a Trust Organization and Trust Cloud Service from the drop-down lists, you do not need to manually configure the trust policy. |

5. Click **Next** to preview the policy.
6. On the page that appears, click **Create** to create a RAM role.
7. Grant permissions to the RAM role.
i. Search for the RAM role that you created, and then click the name of the RAM role. ii. Click the **RAM Role** tab. iii. Click **Create**. iv. Set the **Organization** parameter to the level-1 organization to which the database instance belongs. v. Click **OK**.

**Obtain the Apsara Stack account to which the database**

**instance belongs**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. Click the level-1 organization to which the database instance belongs.
5. Click **Management Accesskey** on the right side of the page.
6. To the right of the **UID** in the **Management AccessKey** dialog box, check the Apsara
Stack account of the database instance.

> **Note:** You need to specify the ID of this Apsara Stack account when you configure cross- account tasks.

**Complete permission policy**

> **Note:** Each `{ "Action": [****], "Resource": "*", "Effect": "Allow"}` represents a complete policy content for a specific database type. You can copy the relevant policy content into **Policy Content** of the RAM role based on your business requirements. If you have any questions when you configure permission policies, contact Apsara Stack technical support.

`{`

```json
  "Version": "1",
  "Statement": [
```

`{`

```json
      "Action": [
        "rds:Describe*",
        "rds:CreateDBInstance",
        "rds:CreateAccount*",
        "rds:CreateDataBase*",
        "rds:ModifySecurityIps",
        "rds:GrantAccountPrivilege",
        "rds:ReceiveDBInstance",
        "rds:CreateMigrateTask",
        "rds:DescribeMigrateTaskById",
        "rds:CreateOnlineDatabaseTask"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "ecs:DescribeSecurityGroupAttribute",
        "ecs:DescribeInstances",
        "ecs:DescribeRegions",
        "ecs:AuthorizeSecurityGroup",
        "ecs:CreateSecurityGroup",
        "ecs:DeleteSecurityGroup",
        "ecs:DescribeSecurityGroups",
        "ecs:JoinSecurityGroup",
        "ecs:LeaveSecurityGroup",
        "ecs:RevokeSecurityGroup"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "dhs:ListProject",
        "dhs:GetProject",
        "dhs:CreateTopic",
        "dhs:ListTopic",
        "dhs:GetTopic",
        "dhs:UpdateTopic",
        "dhs:ListShard",
        "dhs:MergeShard",
        "dhs:SplitShard",
        "dhs:PutRecords",
        "dhs:GetRecords",
        "dhs:GetCursors"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "elasticsearch:DescribeInstance",
        "elasticsearch:ListInstance",
        "elasticsearch:UpdateAdminPwd",
        "elasticsearch:UpdatePublicNetwork",
        "elasticsearch:UpdateBlackIps",
        "elasticsearch:UpdateKibanaIps",
        "elasticsearch:UpdatePublicIps",
        "elasticsearch:UpdatePrivateNetworkWhiteIps",
        "elasticsearch:UpdatePublicWhiteIps",
        "elasticsearch:UpdateWhiteIps"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "drds:DescribeDrds*",
        "drds:ModifyDrdsIpWhiteList",
        "drds:DescribeRegions",
        "drds:DescribeRdsList",
        "drds:CreateDrdsDB",
        "drds:CreateDrdsAccount",
        "drds:DescribeShardDBs"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "polardb:DescribeDBClusterIPArrayList",
        "polardb:DescribeDBClusterNetInfo",
        "polardb:DescribeDBClusters",
        "polardb:DescribeRegions",
        "polardb:DescribeDBClusterEndpoints",
        "polardb:DescribeDBClusterAccessWhiteList",
```

```
        "polardb:ModifyDBClusterAccessWhitelist",
        "polardb:ModifySecurityIps",
        "polardb:DescribeDBClusterAttribute"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "dds:DescribeDBInstanceAttribute",
        "dds:DescribeReplicaSetRole",
        "dds:DescribeSecurityIps",
        "dds:DescribeDBInstances",
        "dds:ModifySecurityIps",
        "dds:DescribeShardingNetworkAddress",
        "dds:DescribeRegions"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "kvstore:DescribeSecurityIps",
        "kvstore:DescribeInstances",
        "kvstore:DescribeRegions",
        "kvstore:ModifySecurityIps",
        "kvstore:DescribeAccounts",
        "kvstore:CreateAccount",
        "kvstore:DescribeDBInstanceNetInfoForInner",
        "kvstore:DescribeDBInstanceNetInfo",
        "kvstore:AllocateInstancePrivateConnection",
        "kvstore:SyncDtsStatus",
        "kvstore:GetDbMasterInfo"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "petadata:DescribeInstanceInfo",
        "petadata:DescribeSecurityIPs",
        "petadata:DescribeInstances",
        "petadata:ModifySecurityIPs"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "adb:DescribeDBClusters",
        "adb:DescribeDBClusterAttribute",
        "adb:DescribeRegions",
        "adb:DescribeDBClusterNetInfo",
        "adb:DescribeDBClusterAccessWhiteList",
"adbModifDBClsterAccessWhiteList"
```

```
        "adb:ModifyDBClusterAccessWhiteList",
        "adb:DescribeDBClusterPerformance"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "gpdb:DescribeDBInstanceAttribute",
        "gpdb:DescribeDBInstances",
        "gpdb:DescribeRegions",
        "gpdb:DescribeDBInstanceIPArrayList",
        "gpdb:DescribeDBClusterIPArrayList",
        "gpdb:ModifySecurityIps",
        "gpdb:DescribeDBInstanceNetInfo",
        "gpdb:DescribeDBClusterPerformance"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "clickhouse:DescribeRegions",
        "clickhouse:DescribeDBClusters",
        "clickhouse:DescribeDBClusterAttribute",
        "clickhouse:DescribeDBClusterNetInfoItems",
        "clickhouse:DescribeDBClusterAccessWhiteList",
        "clickhouse:ModifyDBClusterAccessWhiteList",
        "clickhouse:DescribeAllDataSource"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "ots:ListInstance",
        "ots:GetInstance",
        "ots:GetRow",
        "ots:PutRow",
        "ots:UpdateRow",
        "ots:DeleteRow",
        "ots:BatchWriteRow",
        "ots:BulkImport",
        "ots:CreateTable",
        "ots:DescribeTable",
        "ots:ListTable"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "dg:GetUserDatabases",
        "dg:GetUserGateways"
```

`],` `],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "cen:DeleteRouteServiceInCen",
        "cen:DescribeCenAttachedChildInstances",
        "cen:DescribeCens",
        "cen:DescribeRouteServicesInCen",
        "cen:ResolveAndRouteServiceInCen"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "polardbx:DescribeDBInstances",
        "polardbx:DescribeDBInstanceAttribute",
        "polardbx:DescribeSecurityIps",
        "polardbx:ModifySecurityIps"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "dms:GetUserActiveTenant",
        "dms:GetInstance",
        "dms:GetLogicDatabase",
        "dms:ListLogicDatabases",
        "dms:GetDBTopology",
        "dms:ListLogicTables",
        "dms:GetTableDBTopology"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "vpc:DescribeVpcs",
        "vpc:DescribeVpcAttribute"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `{`

```json
      "Action": [
        "lindorm:GetLindormInstanceListForDMS",
        "lindorm:GetLindormInstanceForDMS",
        "lindorm:UpdateInstanceIpWhiteList"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`},` `,` `{`

```json
      "Action": [
        "hbase:DescribeClusterConnection",
        "hbase:DescribeInstance",
        "hbase:DescribeInstances",
        "hbase:ModifyIpWhitelist"
```

`],`

```json
      "Resource": "*",
      "Effect": "Allow"
```

`}` `]` `}`

## 4 Data synchronization

### 4.1 Supported database types, initial synchronization types, and synchronization topologies

**initial synchronization types, and**

### synchronization topologies

You can use Data Transmission Service (DTS) to synchronize data between various data sources. This topic describes the database types, initial synchronization types, and synchronization topologies that are supported by DTS.

| Source database type | Destination database type | Synchronizati on type | Synchroniza tion topology |
|---|---|---|---|
| Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL instance All versions | Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL instance All versions | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on Two-way synchronizati on |
|   | AnalyticDB for MySQL cluster Version 3.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | AnalyticDB for PostgreSQL instance Version 4.3 or 6.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

|   | Datahub | Schema synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | MaxCompute | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | PolarDB-X 1.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| PolarDB-X 1.0 (formerly known as DRDS) |   |   |   |
|   | Datahub | Schema synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL instance All versions | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

|   | MaxCompute | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | Self-managed Oracle database (RAC or non-RAC architecture) Version 9i, 10g, 11g, 12c, 18c, or 19c | Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | AnalyticDB for MySQL cluster Version 3.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| PolarDB-X 2.0 | PolarDB-X 2.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL instance All versions | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

|   | AnalyticDB for PostgreSQL instance Version 4.3 or 6.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | AnalyticDB for MySQL cluster Version 3.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| Self-managed PostgreSQL database Version 9.4, 9.5, 9.6, 10.x, 11, or 12 ApsaraDB RDS for MySQL instance Version 9.4, 10.0, 11.0, 12.0, or 13.0 | AnalyticDB for PostgreSQL instance Version 4.3 or 6.0 | Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | Self-managed PostgreSQL database Version 9.4, 9.5, 9.6, 10.x, 11, or 12 ApsaraDB RDS for PostgreSQL instance Version 9.4, 10.0, 11.0, 12.0, or 13.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| Db2 for LUW database | AnalyticDB for PostgreSQL instance Version 4.3 or 6.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

| Self-managed Oracle database (RAC or non-RAC architecture) Version 9i, 10g, 11g, 12c, 18c, or 19c | DataHub | Schema synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | MaxCompute | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL instance All versions | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| ApsaraDB for Redis instance Version 4.0 or 5.0 | ApsaraDB for Redis instance Version 4.0 or 5.0 | Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

| ApsaraDB RDS for SQL Server instance Version 2012, 2016, or 2017 Self-managed SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, 2016, and 2017 Note DTS does not support SQL Server clusters or SQL Server AlwaysOn availability groups (AOAGs). If the version of the source database is 2005 or 2008, incremental data synchronization is not supported. | ApsaraDB RDS for SQL Server instance Version 2012, 2016, or 2017 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | DataHub | Schema synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| Self-managed MongoDB database (replica set architecture) ApsaraDB for MongoDB instance (replica set or sharded cluster architecture) | Self-managed MongoDB database (replica set or sharded cluster architecture) ApsaraDB for MongoDB instance (replica set or sharded cluster architecture) Note If the source database is an ApsaraDB for MongoDB instance (sharded cluster architecture), the destination database must be an ApsaraDB for MongoDB instance (sharded cluster architecture). | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |

| PolarDB for PostgreSQL (Compatible with Oracle) | AnalyticDB for MySQL cluster Version 3.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|---|---|---|---|
|   | PolarDB for PostgreSQL (Compatible with Oracle) | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
|   | AnalyticDB for PostgreSQL instance Version 4.3 or 6.0 | Schema synchronizatio n Full data synchronizatio n Incremental data synchronizatio n | One-way synchronizati on |
| MaxCompute | ApsaraDB RDS for MySQL instance All versions | Schema synchronizatio n Full data synchronizatio n | One-way synchronizati on |

### 4.2 Create a data synchronization instance

**instance**

Before you configure a task to synchronize data, you must create a data synchronization instance. This topic describes how to create a data synchronization instance in the Data Transmission Service (DTS) console.

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Data Synchronization**.
3. Click **Create Task**.
4. In the panel that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Source Database Type | The type of the source database. For more information about supported types of source databases, see Supported database types, initial synchronization types, and synchronization topologies. |
| Source Region | The region in which the source database resides. Note You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Destination Database Type | The type of the destination database. For more information about supported types of destination databases, see Supported database types, initial synchronization types, and synchronization topologies. |
| Destination Region | The region in which the destination database resides. Note You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Synchronization Topology | The synchronization topology of the data synchronization instance. For more information about the supported synchronization topologies, see Supported database types, initial synchronization types, and synchronization topologies. |
| Quantity | The number of data synchronization instances that you want to create at a time. |

> **Note:** In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click **Purchase Instance**.
6. In the message that appears, click **OK**.

### 4.3 Synchronization topologies

The data synchronization feature supports multiple types of synchronization topologies. You can plan your data synchronization instances based on your business requirements. This topic describes the synchronization topologies that are supported by Data Transmission Service (DTS) and how to use these topologies.

**One-way synchronization**

To ensure data consistency for one-way synchronization, we recommend that you perform only read operations on the objects in the destination instance. Do not perform write operations on the objects.

| Topology type | Topology | Description |
|---|---|---|

| One-way one-to-one synchronizati on |   | N/A |
|---|---|---|
| One-way one-to-many synchronizati on |   | You must purchase multiple data synchronization instances to implement one- way one-to-many synchronization. For example, if you want to synchronize data from Instance A to Instance B, Instance C, and Instance D, you must purchase three data synchronization instances. |
| One-way cascade synchronizati on |   | You must purchase multiple data synchronization instances to implement one- way cascade synchronization. For example, if you want to synchronize data from Instance A to Instance B and then from Instance B to Instance C, you must purchase two data synchronization instances. |
| One-way many-to-one synchronizati on |   | You must purchase multiple data synchronization instances to implement one- way many-to-one synchronization. For example, if you want to synchronize data from Instance B, Instance C, and Instance D to Instance A, you must purchase three data synchronization instances. Note To ensure data consistency, you must select different objects to synchronize for these data synchronization instances. |

**Two-way synchronization**

DTS supports two-way synchronization only between two MySQL databases.

| Topology type | Topology | Description |
|---|---|---|
| Two-way one- to-one synchronizatio n |   | To ensure data consistency, make sure that data records with the same primary key, business primary key, or unique key are updated on only one of the source and destination instances. |

### 4.4 Prepare the database accounts for data synchronization

**accounts for data synchronization**

When you configure a data synchronization task, you must specify the database accounts for the source and destination databases. The database accounts are used for data synchronization. Different databases and synchronization types require different permissions. You must create and authorize database accounts before you configure a data synchronization task.

**Permissions required for the source database account**

| Database | Required permission | References |
|---|---|---|
| ApsaraDB RDS for MySQL database | Read permissions on the objects to synchronize | See the "Create an account on an ApsaraDB RDS for MySQL instance" and "Modify the permissions of a standard account on an ApsaraDB RDS for MySQL instance" sections of User Guide of ApsaraDB RDS for MySQL. |
| Self-managed MySQL database | The SELECT permission on the objects to synchronize The REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions Permissions to create databases and tables. The permissions allow Data Transmission Service (DTS) to create a database named dts to record heartbeat data during synchronization. | See Create an account for a self- managed MySQL database and configure binary logging. |
| PolarDB for MySQL database | Read permissions on the objects to synchronize | See the "Create a database account" section of User Guide of PolarDB for MySQL. |

| PolarDB for Oracle database | Permissions of a privileged account | See the "Create a database account" section of User Guide of PolarDB. |
|---|---|---|
| Self-managed Oracle database | Permissions of the database administrator (DBA) | See CREATE USER and GRANT. Important If you need to migrate incremental data from an Oracle database but the DBA permission cannot be granted to the database account, you can grant fine-grained permissions to the account. For more information, see Enable logging and grant fine-grained permissions to an Oracle database account. |
| PolarDB-X database | Read permissions on the objects to synchronize | For a PolarDB-X 1.0 instance, see the "Create an account on a PolarDB-X 1.0 instance" and "Modify the permissions of a standard account on a PolarDB-X 1.0 instance" sections of User Guide of PolarDB for Xscale (1.0). For a PolarDB-X 2.0 instance, see the "Manage database accounts" section of User Guide of PolarDB for Xscale. |
| ApsaraDB RDS for SQL Server database | The owner permission on the source database Note A privileged account has the required permissions. | See the "Create an account" section of User Guide of ApsaraDB RDS for SQL Server. |
| Self-managed SQL Server database | The permissions of the sysadmin role | See CREATE USER and GRANT (Transact-SQL). |
| ApsaraDB RDS for PostgreSQL database | Permissions of a privileged account. The account must be the owner of the database. Note If the source database runs on an ApsaraDB RDS for PostgreSQL instance V9.4 and you synchronize only DML operations, the database account must have the REPLICATION permission. | See the "Create an account" section of User Guide of ApsaraDB RDS for PostgreSQL. |

| Self-managed PostgreSQL database | Permissions of the superuser role | See CREATE USER and GRANT. |
|---|---|---|
| KVStore for Redis database | Read and write permissions on the objects to synchronize | See the "Account management" section of User Guide of KVStore for Redis. |
| Self-managed Redis database | The PSYNC or SYNC statement can be executed on the source Redis database. | None |
| ApsaraDB for MongoDB database | Full data migration: read permissions on the source database Incremental data migration: the read permissions on the source database, the admin database, and the local database | The default value of the name of the authentication database is admin. The database account parameter is set to root. |
| Self-managed MongoDB database | Full data migration: read permissions on the source database Incremental data migration: the read permissions on the source database, the admin database, and the local database | See db.createUser(). |

**Permissions required for the destination database account**

| Database | Required permission | References |
|---|---|---|
| ApsaraDB RDS for MySQL database | The read and write permissions on the destination database | See the "Create an account on an ApsaraDB RDS for MySQL instance" and "Modify the permissions of a standard account on an ApsaraDB RDS for MySQL instance" sections of User Guide of ApsaraDB RDS for MySQL. |
| Self-managed MySQL database | The ALL permission on the destination database | See Create an account for a self- managed MySQL database and configure binary logging. |

| PolarDB for MySQL database | The ALL permission on the destination database | See the "Create a database account" section of User Guide of PolarDB for MySQL. |
|---|---|---|
| PolarDB for Oracle database | Permissions of a privileged account | See the "Create a database account" section of User Guide of PolarDB. |
| Self-managed Oracle database | Permissions of the schema owner | See CREATE USER and GRANT. |
| PolarDB-X | Write permissions on the objects to synchronize | For a PolarDB-X 1.0 instance, see the "Create an account on a PolarDB-X 1.0 instance" and "Modify the permissions of a standard account on a PolarDB-X 1.0 instance" sections of User Guide of PolarDB for Xscale (1.0). For a PolarDB-X 2.0 instance, see the "Manage database accounts" section of User Guide of PolarDB for Xscale. |
| KVStore for Redis database | If you use the instance password, no authorization is required. | None |
|   | If you use a custom account, the read and write permissions are required. | See the "Account management" section of User Guide of KVStore for Redis. |
| Self-managed Redis database | The database password must be valid. | None |
| ApsaraDB for MongoDB database | The dbAdminAnyDatabase permission, read and write permissions on the destination database, and read permissions on the local database | The default value of the name of the authentication database is admin. The database account parameter is set to root. |
| Self-managed MongoDB database | The dbAdminAnyDatabase permission, read and write permissions on the destination database, and read permissions on the local database | See db.createUser(). |

| AnalyticDB for MySQL database | V2.0: DTS automatically creates a database account and grants permissions to the account. You do not need to specify the database account. V3.0: Read and write permissions are required. | V3.0: See the "Database accounts and permissions" section of User Guide of AnalyticDB for MySQL. |
|---|---|---|
| AnalyticDB for PostgreSQL database | The initial account or an account that has the RDS SUPERUSER permission is _ required. | See the "Create a database account" and "Manage users and permissions" sections of User Guide of AnalyticDB for MySQL. |
| Message Queue for Apache Kafka instance | N/A | None |
| Self-managed Kafka cluster | N/A Note If no authentication is enabled for the Kafka cluster, you do not need to enter the username or password. | None |
| MaxCompute | The CREATE TABLE, CREATE INSTANCE, CREATE RESOURCE, CREATE JOB, and List permissions on the project to be synchronized | When you configure the data synchronization task, DTS automatically authorizes the database account. |

**Permissions required for the database accounts in two-way**

**data synchronization tasks**

The following table lists the permissions that are required for the source and destination database accounts in two-way data synchronization tasks. The permissions allow DTS to create a database named dts in the source and destination databases to prevent circular data replication.

| Database | Required permission | References |
|---|---|---|
| ApsaraDB RDS for MySQL database | Permissions of a privileged account | See the "Create an account on an ApsaraDB RDS for MySQL instance" and "Modify the permissions of a standard account on an ApsaraDB RDS for MySQL instance" sections of User Guide of ApsaraDB RDS for MySQL. |

| Self-managed MySQL database | The SELECT permission on the objects to synchronize The REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions The permissions to create databases and tables. The permissions allow DTS to create a database named dts to prevent circular data replication. | See Create an account for a self- managed MySQL database and configure binary logging. |
|---|---|---|
| ApsaraDB RDS for PostgreSQL database | Permissions of a privileged account. The account must be the owner of the database. | See the "Create an account" section of User Guide of ApsaraDB RDS for PostgreSQL. |
| Self-managed PostgreSQL database | Permissions of the superuser role | See CREATE USER and GRANT. |
| PolarDB for MySQL database | Permissions of a privileged account | See the "Create a database account" section of User Guide of PolarDB for MySQL. |
| KVStore for Redis database | If you use the instance password, no authorization is required. | None |
|   | If you use a custom account, the read and write permissions are required. | See the "Account management" section of User Guide of KVStore for Redis. |
| Self-managed Redis database | The PSYNC or SYNC statement can be executed on the source Redis database. | None |

### 4.5 Configure data synchronization tasks

**synchronization tasks**

#### 4.5.1 Synchronize data between ApsaraDB RDS for MySQL instances

**RDS for MySQL instances**

This topic describes how to synchronize data between ApsaraDB RDS for MySQL instances by using Data Transmission Service (DTS).

**Prerequisites**

The source and destination ApsaraDB RDS for MySQL instances are created.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Other limits | To ensure compatibility, the version of the destination database must be the same as or later than that of the source database. DTS supports initial schema synchronization for triggers. However, data inconsistency may occur due to triggers. We recommend that you delete the triggers of the source database to prevent data inconsistency caused by the triggers. Limits on RENAME TABLE operations during data synchronization: RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object to be synchronized and rename the table during data synchronization, the data of this table is not synchronized to the destination database. To prevent this situation, you can select the database to which this table belongs as the object to be synchronized when you configure the data synchronization task. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |
|---|---|
| Other limits | Take note of the following items when you configure two-way data synchronization between MySQL instances: To configure two-way data synchronization, you must purchase basic plans for cross- cloud data synchronization and two-way data synchronization. DTS supports two-way data synchronization only between two MySQL databases. DTS does not support two-way data synchronization between multiple MySQL databases. Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. When DTS runs a two-way data synchronization task, DTS creates a database named dts in the destination database to prevent circular synchronization. When the task is running, do not modify the dts database. |

**Supported synchronization topologies**

DTS supports one-way synchronization and two-way synchronization. For more information, see Synchronization topologies.

**SQL operations that can be synchronized**

| Operati on type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE Important RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object to be synchronized and rename the table during data synchronization, the data of this table is not synchronized to the destination database. To prevent this situation, you can select the database to which this table belongs as the object to be synchronized when you configure the data synchronization task. Make sure that the databases to which the table belongs before and after the RENAME TABLE operation are added to the objects to be synchronized. TRUNCATE TABLE |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create a data synchronization task, select **MySQL** as the source and destination database types and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select MySQL. |

| er Guide·Data sy | nchronization Data Transmission Servic |   |
|---|---|---|
| Source Database |   |   |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. Note If the database engine of the source ApsaraDB RDS for MySQL instance is MySQL 5.6, you do not need to configure the Database Account and Database Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the source database. If you select SSL-encrypted, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
|   | Database Type | The type of the destination database. SelectM ySQL. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | RDS instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |

| Destination Database |   |   |
|---|---|---|
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. Note If the database engine of the destination ApsaraDB RDS for MySQL instance is MySQL 5.6, you do not need to configure the Database Account and Database Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the destination database. If you select SSL-encrypted, you must enable SSL encryption for the destination ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the processing mode of conflicting tables and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Synchronization Topology | Select One-way Synchronization. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. |

| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click an object in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information about how to specify the conditions, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |
|---|---|

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.2 Synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project

**RDS for MySQL instance to a MaxCompute**

**project**

This topic describes how to synchronize real-time data from an ApsaraDB RDS for MySQL instance to a MaxCompute project by using Data Transmission Service (DTS). This facilitates real-time data analysis.

**Features**

DTS supports real-time data synchronization from an ApsaraDB RDS for MySQL instance to a MaxCompute project within the same Alibaba Cloud account. DTS supports RDS instances that can be accessed over the classic network or a virtual private cloud (VPC). Objects to be synchronized You can select only tables as the objects to be synchronized.

**Synchronization process**

The synchronization process consists of two stages:
1. Initial full data synchronization.
In this stage, all existing data of the ApsaraDB RDS for MySQL instance is synchronized to the MaxCompute project. Data in each table is synchronized and stored independently to a full baseline table in the MaxCompute project. The default name of the full baseline table is source table name_base. For example, if the source table is named t1, the full baseline table in the destination MaxCompute project is named t1_dts_base. When you configure the data synchronization task, you can modify the prefix of the table name in the destination MaxCompute project.
2. Incremental data synchronization.
In this stage, the incremental data that is generated in the ApsaraDB RDS for MySQL instance is synchronized to the MaxCompute project in real time. The incremental data is stored in incremental data tables in MaxCompute. Each source table corresponds to an incremental data table. The default name of an incremental data table in MaxCompute is source table name_log. When you configure the data synchronization task, you can modify the prefix of the table name in the destination MaxCompute project. Incremental data tables store both the incremental data and specific metadata. Schema of an incremental data table describes the schema of an incremental data table. Table 1. Schema of an incremental data table

| record i _ d | operation _ flag | utc timestam _ p | before fl _ ag | after fl _ ag | co l1 | ... | colN |
|---|---|---|---|---|---|---|---|

| 1 | I | 1476258462 | N | Y | 1 | ... | JustInsert |
|---|---|---|---|---|---|---|---|
| 2 | U | 1476258463 | Y | N | 1 | ... | JustInsert |
| 2 | U | 1476258463 | N | Y | 1 | ... | JustUpdate |
| 3 | D | 1476258464 | Y | N | 1 | ... | JustUpdate |

Take note of the following parameters: record_id: the unique ID of an incremental log entry. The ID auto-increments for each new log entry. If an UPDATE operation is performed on a data record, DTS generates two log entries for an INSERT operation and a DELETE operation. The values of the record_id field in the two log entries are the same. operation_flag: the operation type of the incremental log entry. Valid values: I: an INSERT operation D: a DELETE operation U: an UPDATE operation dts_utc_timestamp: the operation timestamp of the incremental log. It is also the timestamp of the binary log file for the UPDATE record. The timestamp is in the UTC format. before_flag: indicates whether the column values that follow the incremental log entry are pre-update values. Valid values: Y and N. The value of the before_flag field is Y if the column values that follow the log entry are pre-update values. The value of the before_flag field is N if the column values are post-update values. after_flag: indicates whether the column values that follow the incremental log entry are post-update values. Valid values: Y and N. The value of the after_flag field is N if the column values that follow the log entry are pre-update values. The value of the after_flag field is Y if the column values are post-update values. The before_flag and after_flag fields of an incremental log entry are defined based on the operation type. INSERT operation

| record _ id | operation f _ lag | utc timestam _ p | before fla _ g | after fl _ ag | co l1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 1 | I | 1476258462 | N | Y | 1 | .. . | JustInser t |

For an INSERT operation, the column values that follow an incremental log entry are the newly inserted record values (post-update values). Therefore, the value of the before_flag field is N and the value of the after_flag field is Y. UPDATE operation

| record _ id | operation f _ lag | utc timesta _ mp | before fla _ g | after fla _ g | co l1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 2 | U | 1476258463 | Y | N | 1 | .. . | JustInsert |
| 2 | U | 1476258463 | N | Y | 1 | .. . | JustUpdat e |

When an UPDATE operation is performed, two incremental log entries are generated. The two incremental log entries have the same values for the record_id, operation_flag, and dts_utc_timestamp fields. The first log entry records the pre-update values, so the value of the before_flag field is Y and the value of the after_flag field is N. The second log entry records the post-update values, so the value of the before_flag field is N and the value of the after_flag field is Y. DELETE operation

| record _ id | operation fl _ ag | dts utc timest _ _ amp | before fl _ ag | after fl _ ag | c o l 1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 3 | D | 1476258464 | Y | N | 1 | .. . | JustUpdat e |

For a DELETE operation, the column values that follow an incremental log entry are the deleted record values (pre-update values). Therefore, the value of the before_flag field is Y and the value of the after_flag field is N. For each table synchronized from an ApsaraDB RDS for MySQL instance to a MaxCompute project, a full baseline table and an incremental data table are generated in the MaxCompute project. To retrieve the full data of a specific table at a specific point in time in the MaxCompute project, you must merge the corresponding full baseline table and incremental data table. The merging procedure is described later.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
|---|---|
| Other limits | Only tables can be selected as the objects to be synchronized. MaxCompute does not support PRIMARY KEY constraints. If network errors occur, DTS may synchronize duplicate data records to MaxCompute. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

**Configure a data synchronization task**

This section describes how to configure a data synchronization task to synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project in real time.
1. Create a data synchronization instance.

> **Note:** When you create a data synchronization task, set the **Source Database** **Type** parameter to **MySQL**, the **Destination Database type** parameter to **MaxCompute**, and the **Synchronization Topology** parameter to **One-way** **Synchronization**.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. Note If the database engine of the source ApsaraDB RDS for MySQL instance. is MySQL 5.5 or MySQL 5.6, you do not need to configure the Database Account and Database Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source database. Select Non-encrypted or SSL-encrypted based on your business requirements. If you select SSL-encrypted, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
|   | Database Type | The type of the destination database. SelectM axCompute. |

| ta Transmission | Service User Guide·Data synchronizatio |   |
|---|---|---|
| Destination Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the MaxCompute project. |
|   | AccessKey ID | The AccessKey ID and AccessKey secret of the account that you use to connect to the destination MaxCompute project. Note For more information about how to obtain an AccessKey pair, see the Obtain the AccessKey pair of an organization topic in the Developer Guide of MaxCompute. |
|   | AccessKey Secret |   |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Click **OK** to grant permissions to your MaxCompute account.
6. Select the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |

| Apply New Naming Rules of Additional Columns | After DTS synchronizes data to MaxCompute, DTS adds additional columns to the destination table. If the names of additional columns are the same as the names of existing columns in the destination table, data synchronization fails. Configure this parameter based on your business requirements. New Rule: Adopt new naming rules for additional columns. Previous Rule: Adopt old naming rules for additional columns. Do Not Use Default Naming Rules of Additional Columns: Do not adopt any rules for additional columns. Warning Before you specify this parameter, check whether additional columns have the same names as the existing columns in the destination table. |
|---|---|
| Partition Definition of Incremental Data Table | Select the partition names based on your business requirements. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select objects (tables or a database) from the Available section and click the icon to move the objects to the Selected section. Note If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click an object in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information about how to specify the conditions, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

**Merge a full baseline table and an incremental data table**

This section describes how to retrieve the full data of a table at a specific point in time from the full baseline table and incremental data table in the MaxCompute project. You can use SQL statements to merge the two tables. After you merge the full baseline table and incremental data table in MaxCompute by using SQL statements, you can obtain the full data at a specific point in time. The following sample code shows the SQL statements that you can run to merge the two tables:

```
insert overwrite table result_storage_table select col1,
       col2,
       colN
  from(
select row_number() over(partition by t.primary_key_column
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, af
ter_flag, col1,col2,colN
  from(
select incr.record_id, incr.operation_flag, incr.after_flag, incr.col1, incr.col2,incr.colN
  from table_log incr
 where utc_timestamp< timestmap
 union all
select 0 as record_id, 'I' as operation_flag, 'Y' as after_flag, base.col1, base.col2,base.colN
  from table_base base) t) gt
where record_num=1
  and after_flag='Y'
```

Take note of the following variables in the preceding code: result_storage_table: the name of the table that stores the merged data. col1, col2, colN: the names of the columns in the table to be merged. primary_key_column: the name of the primary key column in the table to be merged. table_log: the name of the incremental data table. table_base: the name of the full baseline table. timestamp: the timestamp when the full data to be merged is generated. In the following example, the jiangliu_test_20161010_base table is the full baseline table that corresponds to the jiangliu_test table. The jiangliu_test_20161010_log table is the incremental data table that corresponds to the jiangliu_test table. Schema of an incremental data table describes the schema of the jiangliu_test table. Figure 1. Schema of an incremental data table You can run the following SQL statements in MaxCompute to query the full data of the jiangliu_test table at the 1476263486 time:

```
insert overwrite table jiangliu_test_1476263486 select id,
       name
  from(
select row_number() over(partition by t.id
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, af
ter_flag, id, name
  from(
select incr.record_id, incr.operation_flag, incr.after_flag, incr.id, incr.name
  from jiangliu_test_20161010_log incr
 where utc_timestamp< 1476263486
 union all
select 0 as record_id, 'I' as operation_flag, 'Y' as after_flag, base.id, base.name
  from jiangliu_test_20161010_base base) t) gt
 where gt.row_number= 1
   and gt.after_flag= 'Y' ;
```

You can also use DataWorks to add full data merging nodes before you perform further computing and analysis. After full data is merged, downstream computing and analysis nodes can be automatically triggered. You can set an interval for periodic offline data analysis. At this time, a data synchronization task is configured for synchronizing data from an ApsaraDB RDS for MySQL instance to a MaxCompute project in real time and the full data of tables is merged.

#### 4.5.3 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL V3.0 cluster

**RDS for MySQL instance to an AnalyticDB for**

**MySQL V3.0 cluster**

AnalyticDB for MySQL V3.0 is a real-time online analytical processing (RT-OLAP) service that is developed by Alibaba Cloud for online data analysis with high concurrency. This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL V3.0 cluster by using Data Transmission Service (DTS). After you synchronize data, you can use AnalyticDB for MySQL V3.0 to build internal business intelligence (BI) systems, interactive query systems, and real-time report systems.

**Prerequisites**

The tables that you want to synchronize from the ApsaraDB RDS for MySQL instance contain primary keys. The destination AnalyticDB for MySQL V3.0 cluster has sufficient storage space.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
|---|---|
| Other limits | Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. Due to the limits of AnalyticDB for MySQL V3.0, if the disk space usage of nodes in an AnalyticDB for MySQL V3.0 cluster exceeds 80%, the data synchronization task is delayed and an error is returned. We recommend that you estimate the required disk space based on the objects to be synchronized. You must make sure that the destination cluster has sufficient storage space. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

**SQL operations that can be synchronized**

DDL operations: CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE, ADD COLUMN, and DROP COLUMN DML operations: INSERT, UPDATE, and DELETE

> **Note:** We recommend that you do not change the data type of fields in the source table during data synchronization. Otherwise, DTS generates an error message and stops the data synchronization task.

**Data type mappings**

The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-toone correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table describes the data types that DTS can convert.

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL V3.0 |
|---|---|
| BIGINT UNSIGNED | DECIMAL(20,0) |
| BINARY | VARBINARY |
| BIT | VARCHAR |
| BLOB | VARBINARY |
| CHAR | VARCHAR |
| DATE | DATE |
| DATETIME | DATETIME |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| ENUM | VARCHAR |
| FLOAT | FLOAT |
| GEOMETRY | VARBINARY |
| GEOMETRYCOLLECTION | VARBINARY |
| INT UNSIGNED | BIGINT |
| INTEGER | INT |
| JSON | JSON |
| LINESTRING | VARBINARY |
| LONGBLOB | VARBINARY |
| LONGTEXT | VARCHAR |
| MEDIUMBLOB | VARBINARY |
| MEDIUMINT | INT |
| MEDIUMINT UNSIGNED | INT |
| MEDIUMTEXT | VARCHAR |

| MULTILINESTRING | VARBINARY |
|---|---|
| MULTIPOINT | VARBINARY |
| MULTIPOLYGON | VARBINARY |
| NUMBERIC | DECIMAL |
| POINT | VARBINARY |
| POLYGON | VARBINARY |
| SET | VARCHAR |
| SMALLINT UNSIGNED | INT |
| TEXT | VARCHAR |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| TINYBLOB | VARBINARY |
| TINYINT UNSIGNED | SMALLINT |
| TINYTEXT | VARCHAR |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |
| YEAR | INT |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create a data synchronization instance, select **MySQL** as the source database type, **AnalyticDB MySQL 3.0** as the destination database type, and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |

| ta Transmission |   |   |
|---|---|---|
|   | Service | User Guide·Data synchronizatio |
| Source Database |   |   |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. The account must have the SELECT permission on the objects to be synchronized and the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions. Note If the database engine of the source ApsaraDB RDS for MySQL instance. is MySQL 5.5 or MySQL 5.6, you do not need to configure the Database Account and Database Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method for the connection of the source database. If you select SSL-encrypted, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
| Destination Database | Database Type | The type of the destination database. SelectA nalyticDB for MySQL 3.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for MySQL V3.0 cluster. |
|   | Database Account | The database account of the destination AnalyticDB for MySQL V3.0 cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|

| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
|---|---|
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |

| Merge Tables | Specifies whether to merge tables. If you select Yes, DTS adds the dts data source column to each table to store data sources. In this __ _ _ case, DDL operations cannot be synchronized. If you select No, DDL operations can be synchronized. By default, No is selected. Important If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. If you enable the multi-table merging feature for an incremental data synchronization task, DDL operations are not supported to be synchronized. If you perform DDL operations on the source database, data loss occurs in the destination database or the task fails. |
|---|---|
| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note Only the INSERT, UPDATE, DELETE, and ADD COLUMN operations can be synchronized. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. **Optional:**Click **Next: Configure Database and Table Fields** and specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** for the tables that you want to synchronize to the destination AnalyticDB for MySQL cluster.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.4 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance

**RDS for MySQL instance to an AnalyticDB for**

**PostgreSQL instance**

This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature allows you to transfer and analyze data with ease.

**Prerequisites**

**q**

The tables that you want to synchronize from the source database contain primary keys. The destination AnalyticDB for PostgreSQL instance is created.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Other limits | Requirements for the objects to be synchronized: You can select only tables as the objects to be synchronized. DTS does not synchronize data of the following data types: BIT, VARBIT, GEOMETRY, ARRAY, UUID, TSQUERY, TSVECTOR, and TXID SNAPSHOT. _ Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source self-managed PostgreSQL database. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |
|---|---|

**SQL operations that can be synchronized**

DML operations: INSERT, UPDATE, and DELETE DDL operations: ALTER TABLE, ADD COLUMN, DROP COLUMN, and RENAME COLUMN

> **Note:** The CREATE TABLE and DROP TABLE operations are not supported. To synchronize data from a new table, you must add the table to the selected objects. For more information, see Add an object to a data synchronization task.

**Term mapping**

| Term in ApsaraDB RDS for MySQL | Term in AnalyticDB for PostgreSQL |
|---|---|
| Database | Schema |
| Table | Table |

**Create a data structure in the destination instance**

You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source ApsaraDB RDS for MySQL instance.

**Configure a data synchronization task**

1. Create a data synchronization task. For more information, see Create a data
synchronization instance.

> **Note:** When you create the data synchronization task, select **MySQL** as the source database type, **AnalyticDB for PostgreSQL** as the destination database type, and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source ApsaraDB RDS for MySQL instance resides. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. The account must have the SELECT permission on the objects to be synchronized and the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions. Note If the database type of the source ApsaraDB RDS for MySQL instance is MySQL 5.5 or MySQL 5.6, you do not need to configure the Database Account and Database Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source database. Select Non-encrypted or SSL-encrypted based on your business requirements. Note If you select SSL-encrypted, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |

| Destination Database | Database Type | The type of the destination database. Select AnalyticDB for PostgreSQL. |
|---|---|---|
|   | Access Method | The access method of the destination database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination instance resides. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination AnalyticDB for PostgreSQL instance. Note The database account must have the SELECT, INSERT, UPDATE, DELETE, COPY, TRUNCATE, and ALTER TABLE permissions. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Clear Destination Table: skips the precheck for empty destination tables and clears the data in destination tables before initial full data synchronization. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
|---|---|
| DDL and DML Operations to Be Synchronized | The SQL operations to be synchronized during incremental data migration at the instance level. Note To select the SQL operations performed on a specific database or table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. |
| Source Objects | Select objects (tables) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note The CREATE TABLE operation is not supported. To synchronize data from a new table, you must add the table to the selected objects. For more information, see Add an object to a data synchronization task. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. No: does not configure the ETL feature. |

7. **Optional:**Click **Next: Configure Database and Table Fields** to specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** information for the tables that you want to synchronize to the AnalyticDB for PostgreSQL instance.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.5 Synchronize data between ApsaraDB RDS for PostgreSQL instances

**RDS for PostgreSQL instances**

This topic describes how to synchronize data between ApsaraDB RDS for PostgreSQL instances by using Data Transmission Service (DTS).

**Prerequisites**

The source and destination ApsaraDB RDS for PostgreSQL instances are created.

> **Note:** To ensure compatibility, the version of the destination database must be the same as or later than that of the source database. Otherwise, compatibility issues may occur.

The available storage space of the destination ApsaraDB RDS for PostgreSQL instance is larger than the total size of the data in the source ApsaraDB RDS for PostgreSQL instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed is affected. The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The data logging feature must be enabled. We recommend that you retain data logs for at least seven days during full data synchronization. You can wait until full data synchronization is complete, and then clear the data logs generated in the source database after the DTS task is run. Otherwise, DTS may fail to obtain the write-ahead logging (WAL) logs, which causes the task to fail, or even data inconsistency and data loss. Make sure that you set the retention period of WAL logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Note To ensure data security, the DTS server stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, the DTS server automatically clears the logs that exceed the limit. During schema synchronization and full data synchronization, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data synchronization task fails. If the source database has long-running transactions and incremental data is synchronized in the data synchronization task, the WAL logs generated before the long-running transactions in the source database are committed may be accumulated. As a result, the disk space of the source database may be insufficient. |
|   | To ensure that the data synchronization task is run as expected, you can perform a primary/secondary switchover only on an ApsaraDB RDS for PostgreSQL V11 instance during data synchronization. In this case, you must set the rds failover slot mode parameter to sync . _ _ _ Warning If you perform a primary/secondary switchover on an ApsaraDB RDS for PostgreSQL instance of another version during data synchronization, the data synchronization task fails. A data synchronization task can synchronize data from only one database. To synchronize data from multiple databases, you must create a data synchronization task for each database. The name of the source database cannot contain hyphens (-). For example, dts- testdata is invalid. DTS does not check the validity of metadata such as sequences. You must manually check the validity of metadata. |

|   | Data may be inconsistent between the primary and secondary nodes of the source database due to the latency of incremental data synchronization. Therefore, you must use the primary node as the data source when you synchronize data. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the tablespace of the destination database is |
|---|---|
| Other limits | larger than that of the source database. If you select a schema as the object to be synchronized and create a table in the schema or execute the RENAME statement to rename a table in the schema during incremental data synchronization, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Note Replace the schema and table variables in the preceding sample statement with your actual schema name and table name. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. To ensure that the latency of incremental data synchronization is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source _ _ database. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During incremental data synchronization, DTS creates a replication slot for the source database. The replication slot is prefixed with dts sync . DTS _ _ automatically clears historical data in the replication slot every 90 minutes to reduce storage usage. Note If the data synchronization task is released or fails, DTS automatically clears the replication slot. If the source database is an ApsaraDB RDS for PostgreSQL instance and a primary/secondary switchover is performed on the instance, you must log on to the secondary database to manually clear the replication slot. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. After your workloads are switched to the destination database, newly written sequences do not increment from the maximum value of the sequences in the source database. Therefore, you must query the maximum value of the sequences in the source database before you switch your workloads to the destination database. Then, you must specify the queried maximum value as the starting value of the sequences in the destination database. For more information, see the Statements that are executed to query the maximum value of the sequences in the source database section of this topic. |

| Special cases | If the source or destination instance is an ApsaraDB RDS for PostgreSQL instance, take note of the following limits: During data synchronization, do not modify the endpoint or zone of the ApsaraDB RDS for PostgreSQL instance. Otherwise, the data synchronization task fails. |
|---|---|

**Statements that are executed to query the maximum value of**

**the sequences in the source database**

```
do language plpgsql $$ declare
  nsp name;
  rel name;
  val int8;
begin
  for nsp,rel in select nspname,relname from pg_class t2 , pg_namespace t3 where t2.rel
namespace=t3.oid and t2.relkind='S'
  loop
    execute format($_$select last_value from %I.%I$_$, nsp, rel) into val;
    raise notice '%',
    format($_$select setval('%I.%I'::regclass, %s);$_$, nsp, rel, val+1);
  end loop;
end; $$;
```

**Preparations**

Before you synchronize data from an ApsaraDB RDS for PostgreSQL instance, you must perform the following operations: Log on to the ApsaraDB RDS console. Click the ID of the source ApsaraDB RDS for PostgreSQL instance. In the left-side navigation pane, click
**Parameters**. Find the **wal_level** parameter and change the value of this parameter to
logical.

> **Warning:** After you change the value of the `wal_level` parameter, you must restart the instance to apply the change. We recommend that you evaluate the impact on your business and modify the parameter during off-peak hours.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PostgreSQL** as the source and destination database types and select **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. |
|   | Instance ID | The ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | The name of the database from which you want to synchronize data in the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for PostgreSQL instance. Specify a privileged account. The account must be the owner of the source database. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectP ostgreSQL. |

| ta Transmission S | ervice User Guide·Data synchronizatio |   |
|---|---|---|
| Destination Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | The name of the database in the destination ApsaraDB RDS for PostgreSQL instance. Note The name of the destination database can be different from that of the database in the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for PostgreSQL instance. The account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be synchronized and the synchronization types.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schemas, DTS does not synchronize data records that have the same primary key values as data records in the destination database. If the source and destination databases have different schemas, only specific columns are synchronized or the data synchronization task fails. |
|---|---|
| Synchronization Topology | Select One-way Synchronization. |
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be synchronized. |

| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |
|---|---|

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.6 Synchronize data from a self-managed PostgreSQL database to an AnalyticDB for PostgreSQL instance

**PostgreSQL database to an AnalyticDB for**

**PostgreSQL instance**

This topic describes how to synchronize data from a self-managed PostgreSQL database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature provided by DTS allows you to transfer and analyze data with ease.

**Prerequisites**

The source self-managed PostgreSQL database and the destination AnalyticDB for PostgreSQL instance are created. The available storage space of the AnalyticDB for PostgreSQL instance is larger than the total size of the data in the self-managed PostgreSQL database.

**Limits**

| Category | Description |
|---|---|

|   | Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for data logs must be met: The wal level parameter is set to logical. _ Data logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the data logs generated in the source database after the DTS task is run. Note DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the data logs generated 24 hours ago. As a result, the data synchronization task may fail. |
|---|---|---|
|   |   | DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source self-managed PostgreSQL database. Requirements for the objects to be synchronized: You can select only tables as the objects to be synchronized. DTS does not synchronize data of the following data types: BIT, VARBIT, GEOMETRY, ARRAY, UUID, TSQUERY, TSVECTOR, and TXID SNAPSHOT. _ A single data synchronization task can synchronize data from only one database. To synchronize data from multiple databases, you must create a data synchronization task for each database. During data synchronization, if you select a schema as the object to be synchronized, take note of the following limits: If you create a table in the schema or run the RENAME command to rename the table, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. This ensures data consistency. Note Replace the schema and table variables in the preceding sample statement with the actual schema name and table name. To ensure that the latency of data synchronization is accurate, DTS adds a heartbeat table named dts postgres heartbeat to the source database. _ _ During data synchronization, DTS creates a replication slot in the source database to replicate data. The replication slot is prefixed with dts sync . DTS automatically _ _ clears historical data in the replication slot every 90 minutes to reduce storage usage. |

|   | schema.table REPLICA IDENTITY FULL; |
|---|---|

| Other limits | Note If the data synchronization task is released or fails, DTS automatically clears the replication slot. If the source database is an ApsaraDB RDS for PostgreSQL instance and a primary/secondary switchover is performed on the instance, you must log on to the secondary database to clear the replication slot. |
|---|---|
|   | Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

**SQL operations that can be synchronized**

DML operations: INSERT, UPDATE, and DELETE

**Preparations**

DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source selfmanaged PostgreSQL database.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PostgreSQL** as the source database type, **AnalyticDB for PostgreSQL** as the destination database type, and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PostgreSQL. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Hostname or IP Address | The server IP address of the self-managed PostgreSQL database. |
|   | Port Number | The service port number of the self-managed PostgreSQL database. |
|   | Database Name | The name of the self-managed PostgreSQL database. |
|   | Database Account | The username of the account used to log on to the self- managed PostgreSQL database. The account must have the superuser permissions. |
|   | Database Password | The password that is used to access the self-managed PostgreSQL database. |
| Destination Database | Database Type | The type of the destination database. SelectA nalyticDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The username of the database account of the AnalyticDB for PostgreSQL instance or the database account that has the RDS SUPERUSER permission. _ |
|   | Database Password | The password that is used to access the destination database. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for the self-managed PostgreSQL database, add the CIDR blocks
of DTS servers that are displayed in the dialog box to the whitelist of the database. Then, click **Test Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for the self-managed PostgreSQL database, ignore the preceding settings and click **Test Connectivity and Proceed**.

6. Configure the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. By default, you must also select Full Data Synchronization. Schema Synchronization is not supported. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data serves as the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Clear Destination Table: skips the precheck for empty destination tables and clears the data in destination tables before initial full data synchronization. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| DDL and DML Operations to Be Synchronized | The SQL operations to be synchronized during incremental data migration at the instance level. Note To select the SQL operations performed on a specific database or table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with that in the source or destination database. For more information,see Specify the capitalization of object names in the destination instance. |

| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations performed on a specific table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click an object in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information about how to specify the conditions, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. The data synchronization task does not support the ETL feature. Select No. |
|---|---|

8. **Optional:**Click **Next: Configure Database and Table Fields** to specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** information for the tables that you want to synchronize to the AnalyticDB for PostgreSQL instance.

9. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

0. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.7 Synchronize data from an ApsaraDB RDS for SQL Server database to a DataHub instance

**RDS for SQL Server database to a DataHub**

**instance**

This topic describes how to use Data Transmission Service (DTS) to synchronize data from an ApsaraDB RDS for SQL Server database to a DataHub instance.

**Prerequisites**

DataHub is activated and a project is created to receive the data to be synchronized.

**Limits**

**SQL operations that can be incrementally synchronized**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **SQLServer** as the source database type and **DataHub** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select SQL Server. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note Specifies whether to synchronize data between instances that belong to different Alibaba Cloud accounts. If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source SQL Server instance. |
|   | Database Account | The database account of the source SQL Server instance. The account must have the owner permissions on the objects to be synchronized. A privileged account has the required permissions. |
| Document Ver | sion: 20240522 28 |   |

|   | Database Password | The password of the database account. |
|---|---|---|
| Destinati on Database | Database Type | The type of the destination database. SelectD ataHub. |
|   | Access Method | The access method of the destination database. Default value: Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the DataHub project to which data is synchronized. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be synchronized and the synchronization types.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. By default, you must also select Schema Synchronization. Full Data Synchronization is not supported. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Apply New Naming Rules of Additional Columns | Configure this parameter based on your business requirements. New Rule: Adopt new naming rules for additional columns. Previous Rule: Adopt old naming rules for additional columns. Do Not Use Default Naming Rules of Additional Columns: Do not adopt any rules for additional columns. Warning Before you specify this parameter, check whether additional columns have the same names as the existing columns in the destination table. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. The data synchronization task does not support the ETL feature. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.8 Synchronize data between PolarDB-X 1.0 instances

### 1.0 instances

PolarDB-X 1.0 is formerly known as Distributed Relational Database Service (DRDS). It is compatible with the MySQL protocol and syntax, and supports automatic sharding, online smooth scaling, auto scaling, and transparent read/write splitting. This topic describes how to synchronize data between PolarDB-X 1.0 instances by using Data Transmission Service (DTS).

**Prerequisites**

The tables to be synchronized contain primary keys.

**Limits**

> **Warning:** For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X 1.0 instance, see Precautions and limits for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X 1.0 instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
|---|---|
|   | The storage type of the PolarDB-X 1.0 instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X 1.0 instance, synchronization latency and stability issues may occur when you synchronize data from the source PolarDB-X 1.0 instance to the destination instance. We recommend that you use the following solution to configure data synchronization tasks. For more information about the benefits of this solution, see Solutions of data synchronization from a PolarDB-X instance. You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X 1.0 instance. |

| Other limits | When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X 1.0 instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Note Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X 1.0 instance and you want to synchronize data from the PolarDB-X 1.0 instance to an AnalyticDB for MySQL instance, we recommend that you configure three data |
|---|---|
|   | synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance B, and you want to synchronize data between the two PolarDB-X 1.0 instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to sourceP olarDB-X 1.0 Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X 1.0 Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. We recommend that you do not change the network type of theP olarDB-X 1.0 instances during data synchronization. Note If you change the network type of a PolarDB-X 1.0 instance during data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. During data synchronization, do not upgrade or downgrade theP olarDB-X 1.0 instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. We recommend that you do not use tools such as gh-ost or pt-online-schema- |

change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail.

**Supported synchronization topologies**

DTS supports the following synchronization topologies: one-way one-to-one synchronization, one-way one-to-many synchronization, one-way cascade synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies.

**SQL operations that can be synchronized**

INSERT, UPDATE, and DELETE

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization task, select **PolarDB-X 1.0** as the source database type, **PolarDB-X 1.0** as the destination database type, and **One-** **way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 1.0. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Instance ID | The ID of the source PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 1.0 instance. The account must have the read permissions on the objects to be synchronized. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. SelectP olarDB-X 1.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the destination PolarDB-X 1.0 instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more tables from the Available section and click the icon to move the tables to the Selected section. Note You can select only tables as the objects to be synchronized. |

| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |
|---|---|

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.9 Synchronize data from a PolarDB-X 1.0 instance to an AnalyticDB for MySQL V3.0 cluster

**instance to an AnalyticDB for MySQL V3.0**

**cluster**

This topic describes how to synchronize data from a PolarDB-X 1.0 instance to an AnalyticDB for MySQL V3.0 cluster by using Data Transmission Service (DTS).

**Limits**

> **Warning:** For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X 1.0 instance, see Precautions and limits for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X 1.0 instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. Limits on operations to be performed on the source database: The storage type of the PolarDB-X 1.0 instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. We recommend that you do not change the network type of theP olarDB-X 1.0 instances during data synchronization. Note If you change the network type of a PolarDB-X 1.0 instance during data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. During data synchronization, do not upgrade or downgrade theP olarDB-X 1.0 instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. |
|---|---|
|   | If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X 1.0 instance, synchronization latency and stability issues may occur when you synchronize data from the source PolarDB-X 1.0 instance to the destination instance. We recommend that you use the following solution to configure data synchronization tasks. For more information about the benefits of this solution, see Solutions of data synchronization from a PolarDB-X instance. You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X 1.0 instance. |

| Other limits | When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X 1.0 instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Note Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X 1.0 instance and you want to synchronize data from the PolarDB-X 1.0 instance to an AnalyticDB for MySQL instance, we recommend that you configure three data synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance B, and you want to synchronize data between the two PolarDB-X 1.0 instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to sourceP olarDB-X 1.0 Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X 1.0 Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. Due to the limits of AnalyticDB for MySQL, if the disk space usage of nodes in an AnalyticDB for MySQL cluster exceeds 80%, the data synchronization task is delayed and an error is returned. We recommend that you estimate the required disk space based on the objects to be synchronized. You must make sure that the destination cluster has sufficient storage space. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |   |   |
|---|---|---|---|
|   |   | Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |   |

**Supported synchronization topologies**

DTS supports the following synchronization topologies: one-way one-to-one synchronization, one-way one-to-many synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies.

**SQL operations that can be synchronized**

INSERT, UPDATE, and DELETE

**Data type mappings**

The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-toone correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table describes the data types that DTS can convert.

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL V3.0 |
|---|---|
| BIGINT UNSIGNED | DECIMAL(20,0) |
| BINARY | VARBINARY |
| BIT | VARCHAR |
| BLOB | VARBINARY |
| CHAR | VARCHAR |
| DATE | DATE |
| DATETIME | DATETIME |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| ENUM | VARCHAR |
| FLOAT | FLOAT |
| GEOMETRY | VARBINARY |
| GEOMETRYCOLLECTION | VARBINARY |
| INT UNSIGNED | BIGINT |
| INTEGER | INT |
| JSON | JSON |
| LINESTRING | VARBINARY |
| LONGBLOB | VARBINARY |
| LONGTEXT | VARCHAR |
| MEDIUMBLOB | VARBINARY |
| MEDIUMINT | INT |

| MEDIUMINT UNSIGNED | INT |
|---|---|
| MEDIUMTEXT | VARCHAR |
| MULTILINESTRING | VARBINARY |
| MULTIPOINT | VARBINARY |
| MULTIPOLYGON | VARBINARY |
| NUMBERIC | DECIMAL |
| POINT | VARBINARY |
| POLYGON | VARBINARY |
| SET | VARCHAR |
| SMALLINT UNSIGNED | INT |
| TEXT | VARCHAR |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| TINYBLOB | VARBINARY |
| TINYINT UNSIGNED | SMALLINT |
| TINYTEXT | VARCHAR |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |
| YEAR | INT |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create a data synchronization instance, select **PolarDB-X 1.0** as the source database type, **AnalyticDB MySQL 3.0** as the destination database type, and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |

| Source Database | Database Type | The type of the source database. Select PolarDB-X 1.0. |
|---|---|---|
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Instance ID | The ID of the source PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 1.0 instance. The account must have the read permissions on the objects to be synchronized. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. SelectA nalyticDB for MySQL 3.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for MySQL V3.0 cluster. |
|   | Database Account | The database account of the AnalyticDB for MySQL V3.0 cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data serves as the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |

| Merge Tables | If you select Yes, DTS adds the dts data source column to each __ _ _ table to store data sources. In this case, DDL operations cannot be synchronized. No is selected by default. In this case, DDL operations can be synchronized. Important If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. If you enable the multi-table merging feature for an incremental data synchronization task, DDL operations are not supported to be synchronized. If you perform DDL operations on the source database, data loss occurs in the destination database or the task fails. |
|---|---|
| Source Objects | Select one or more tables from the Source Objects section and click the icon to move the tables to the Selected Objects section. Note You can select only tables as the objects to be synchronized. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. **Optional:**Click **Next: Configure Database and Table Fields** and specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** for the tables that you want to synchronize to the destination AnalyticDB for MySQL cluster.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.10 Synchronize data from a PolarDB-X 1.0 instance to a DataHub project

### 1.0 instance to a DataHub project

This topic describes how to synchronize data from a PolarDB-X 1.0 instance to a DataHub project by using Data Transmission Service (DTS). After you synchronize data, you can use big data services such as Realtime Compute to analyze data in real time.

**Prerequisites**

A DataHub project is created to receive the synchronized data.

**Limits**

> **Warning:** For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X 1.0 instance, see Precautions and limits for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X 1.0 instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. Limits on operations to be performed on the source database: The storage type of the PolarDB-X 1.0 instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. We recommend that you do not change the network type of theP olarDB-X 1.0 instances during data synchronization. Note If you change the network type of a PolarDB-X 1.0 instance during data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. During data synchronization, do not upgrade or downgrade theP olarDB-X 1.0 instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. |
|   | If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X 1.0 instance, synchronization latency and stability issues may occur when you synchronize data from the source PolarDB-X 1.0 instance to the |

| Data Transmission S | ervice User Guide·Data synchronization |
|---|---|
| Other limits | destination instance. We recommend that you use the following solution to configure data synchronization tasks. For more information about the benefits of this solution, see Solutions of data synchronization from a PolarDB-X instance. You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X 1.0 instance. When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X 1.0 instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Note Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X 1.0 instance and you want to synchronize data from the PolarDB-X 1.0 instance to an AnalyticDB for MySQL instance, we recommend that you configure three data synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X 1.0 Instance B, and you want to synchronize data between the two PolarDB-X 1.0 instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to sourceP olarDB-X 1.0 Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X 1.0 Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. Only tables can be selected as the objects to be synchronized. Initial full data synchronization is not supported. DTS does not synchronize historical data of the objects to be synchronized from the source PolarDB-X 1.0 instance to the destination DataHub project. DTS does not synchronize DDL operations. If you perform a DDL operation on the source PolarDB-X instance during data synchronization, data fails to be synchronized. To solve this issue, you must modify the related topic in the destination DataHub project and then restart the data synchronization task. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

**SQL operations that can be synchronized**

INSERT, UPDATE, and DELETE

**Procedure**

1. Create a data synchronization instance. For more information, see Create a data
synchronization instance.

> **Note:** When you create a data synchronization task, select **PolarDB-X 1.0** as the source database type, **DataHub** as the destination database type, and **One-way** **Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 1.0. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Instance ID | The ID of the source PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 1.0 instance. The account must have the read permissions on the objects to be synchronized. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. SelectD ataHub. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

| ta Transmission |   |   |
|---|---|---|
|   | Project | The name of the DataHub project to which data is synchronized. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. You can select only Schema Synchronization. You cannot select Full Data Synchronization. Note During initial synchronization, DTS synchronizes the schemas of the selected objects, such as tables, from the source instance to the destination Datahub project. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Apply New Naming Rules of Additional Columns | After DTS synchronizes data to DataHub, DTS adds additional columns to the destination table. If the names of additional columns are the same as the names of existing columns in the destination table, data synchronization fails. Configure this parameter based on your business requirements. New Rule: Adopt new naming rules for additional columns. Previous Rule: Adopt old naming rules for additional columns. Do Not Use Default Naming Rules of Additional Columns: Do not adopt any rules for additional columns. Warning Before you specify this parameter, check whether additional columns have the same names as the existing columns in the destination table. |

| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
|---|---|
| Source Objects | Select one or more tables from the Source Objects section and click the icon to move the tables to the Selected Objects section. Note You can select only tables as the objects to be synchronized. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. The data synchronization task does not support the ETL feature. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.11 Synchronize data from a self-managed Db2 for LUW database to an AnalyticDB for PostgreSQL instance

**managed Db2 for LUW database to an**

**AnalyticDB for PostgreSQL instance**

This topic describes how to synchronize data from a self-managed Db2 for LUW database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature provided by DTS allows you to transfer and analyze data with ease.

**Prerequisites**

The source self-managed Db2 for LUW database and the destination AnalyticDB for PostgreSQL instance are created. The available storage space of the AnalyticDB for PostgreSQL instance is larger than the total size of the data in the self-managed Db2 for LUW database.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server on which the source database is deployed must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed decreases. The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you want to edit the tables in the destination database, such as renaming tables or columns, you can synchronize up to 1,000 tables in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. The following requirements for data logs must be met: The data logging feature is enabled. Otherwise, error messages are returned during precheck and the data synchronization task cannot be started. If you perform only incremental data synchronization, the data logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the data logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the data logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of data logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. |

| Other limits | Schema synchronization is not supported. Before you configure a data synchronization task, you must create databases and tables in the destination instance based on the databases and tables that you want to synchronize. DTS synchronizes incremental updates from a self-managed Db2 for LUW database to the destination database based on the Change Data Capture (CDC) replication technology of Db2 for LUW. However, the CDC replication technology has its own limits. For more information, see General data restrictions for SQL Replication. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost and pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |
|---|---|
| Special cases | The source database is a self-managed Db2 for LUW database. Therefore, you must take note of the following items: If you perform a primary/secondary switchover on the source database when the data synchronization task is running, the task fails. DTS calculates synchronization latency based on the timestamp of the latest synchronized data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the synchronization latency may be inaccurate. If the latency of the data synchronization task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be synchronized, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

**SQL operations that can be synchronized**

DML operations: INSERT, UPDATE, and DELETE

**Preparations**

Create database accounts and grant permissions to the accounts. Self-managed Db2 for LUW database: the database administrator permissions (DBADM authority). AnalyticDB for PostgreSQL instance: read and write permissions on the destination database. Enable the archive logging feature for the self-managed Db2 for LUW database.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create a data synchronization instance, select **DB2 for LUW** as the source database type and **AnalyticDB PostgreSQL** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source database and destination instance.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | This parameter is set to DB2 for LUW. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Domain Name or IP Address | The endpoint of the self-managed Db2 for LUW database. |
|   | Port Number | The service port number of the self-managed Db2 for LUW database. |
|   | Database Name | The name of the source database. |
|   | Database Account | The account of the self-managed Db2 for LUW database. The account must have the superuser permissions. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | Select AnalyticDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The initial database account of the AnalyticDB for PostgreSQL instance or the database account that has the RDS SUPERUSER permission. _ |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Db2 for LUW database, you must add the
CIDR blocks of DTS servers to the whitelist. Then, click **Test Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for the self-managed Db2 for LUW database, click **Test Connectivity and Proceed**.

6. Configure the synchronization policy and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Clear Destination Table: skips the precheck for empty destination tables and clears the data in destination tables before initial full data synchronization. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| DDL and DML Operations to Be Synchronized | The SQL operations to be synchronized during incremental data migration at the instance level. Note To select the SQL operations performed on a specific database or table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. |

| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with the default capitalization of object names in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
|---|---|
| Source Objects | Select objects (tables) from the Source Objects section and click the icon to move the objects to the Selected Objects section. |
| Selected Objects | By default, after an object is synchronized to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations performed on a specific database or table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click an object in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information about how to specify the conditions, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

8. **Optional:**Click **Next: Configure Database and Table Fields** to specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** information for the tables that you want to synchronize to the AnalyticDB for PostgreSQL instance.

9. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

0. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.12 Synchronize data from a self-managed Oracle database to a DataHub project

**managed Oracle database to a DataHub**

**project**

DataHub is a real-time data distribution platform that is designed to process streaming data. You can publish and subscribe to streaming data in DataHub and distribute the data to other platforms. DataHub allows you to analyze and use streaming data with ease. This topic describes how to synchronize data from a self-managed Oracle database to a DataHub project by using Data Transmission Service (DTS). After you synchronize data, you can use big data services such as Realtime Compute for Apache Flink to analyze the data in real time.

**Prerequisites**

The engine version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. The self-managed Oracle database is running in ARCHIVELOG mode. Archived log files are accessible, and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The destination DataHub project is created. For more information, see the **"Create a**
**project"** topic in the documentation of **DataHub**.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | Requirements for the objects to be synchronized: The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be synchronized cannot exceed 30 bytes in length. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If the self-managed Oracle database is an Oracle Real Application Cluster (RAC) database, you can use only a single virtual IP address (VIP) rather than a Single Client Access Name (SCAN) IP address when you configure the data synchronization task. After you specify the VIP, node failover of the Oracle RAC database is not supported. The following requirements must be met: The redo logging and archive logging features must be enabled. If you perform only incremental data synchronization, the redo logs and archive logs of the source database must be stored for more than 24 hours. If you perform both schema synchronization and incremental data synchronization, the redo logs and archive logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the redo logs and archive logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the schema synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of redo logs and archive logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. If you perform a primary/secondary switchover on the source database when the data synchronization task is running, the task fails. |

| Other limits | You can configure a data synchronization task for this scenario only in the DTS console of the new version. The objects of initial schema synchronization must be tables. Warning In this scenario, DTS does not support triggers. We recommend that you delete the triggers of the source database to prevent data inconsistency caused by the triggers. Full data synchronization is not supported. DTS does not synchronize historical data of the required objects from the source database to the destination DataHub project. Only tables can be selected as the objects to be synchronized. We recommend that you do not use tools such as gh-ost and pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. DTS calculates synchronization latency based on the timestamp of the latest synchronized data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the synchronization latency may be inaccurate. If the latency of the data synchronization task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be synchronized, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |
|---|---|

**Supported synchronization topologies**

One-way one-to-one synchronization One-way one-to-many synchronization One-way many-to-one synchronization

**SQL operations that can be synchronized**

INSERT, UPDATE, and DELETE

**Permissions required for database accounts**

| Database | Required permission | References |
|---|---|---|

| Self-managed Oracle databases | Permissions of database administrator (DBA) | CREATE USER and GRANT Important If you need to synchronize data from an Oracle database but the DBA permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account. |
|---|---|---|

**Enable logging and grant fine-grained permissions to an Oracle**

**database account**

> **Important:** If you need to synchronize data from an Oracle database but the DBA permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account.

1. Enable archive logging and supplemental logging.

| Log type | Procedure |
|---|---|
| Archive logging | Execute the following statements to enable archive logging: shutdown immediate; startup mount; alter database archivelog; alter database open; archive log list; |

| Supplemental logging | Enable supplemental logging at the database or table level based on your business requirements: Note You can enable database-level supplemental logging to ensure the stability of DTS tasks. You can enable table-level supplemental logging to reduce the disk usage of the source Oracle database. Enable database-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Execute the following statement to enable primary key and unique key supplemental logging at the database level: alter database add supplemental log data (primary key,unique index) columns; Enable table-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Enable table-level supplemental logging by using one of the following methods: Execute the following statement to enable primary key supplemental logging at the table level: alter table table name add supplemental log data (primary _ key) columns; Execute the following statement to enable table-level supplemental logging for all columns: alter table tb name add supplemental log data (all) _ columns ; |
|---|---|

2. Grant fine-grained permissions to an Oracle database account.
Oracle 9i to 11g

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the ac
count. create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; -- system tables grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct;
```

Oracle 12c to 19c (tenant mode)

```bash
# Switch to the pluggable database (PDB). Create a database account, such as rdsdt_
dtsacct, and grant permissions to the account. ALTER SESSION SET container = ORCLPDB1; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct;
```

```bash
grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; -- V$PDBS privileges grant select on V_$PDBS to rdsdt_dtsacct;
# Switch to the container database (CDB). Create a database account and grant permi
ssions to the account by using one of the following methods: ALTER SESSION SET container = CDB$ROOT;
# Method 1: Create a global account that starts with C##, such as C##rdsdt_dtsacct,
and grant permissions to the account. If you use this method, you must contact the O&M engineers of DTS. create user C##rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to C##rdsdt_dtsacct; grant connect to C##rdsdt_dtsacct; grant resource to C##rdsdt_dtsacct; grant select on v_$logmnr_contents to C##rdsdt_dtsacct; grant LOGMINING to C##rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to C##rdsdt_dtsacct; grant execute on sys.dbms_logmnr to C##rdsdt_dtsacct;
# Method 2: Create a database account, such as rdsdt_dtsacct, and grant permissions
to the account. If you use this method, you must modify the default parameters of t he Oracle database. alter session set "_ORACLE_SCRIPT"=true; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant select on v_$logmnr_contents to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grantEXECUTECATALOGROLEtordsdtdtsacct
```

```
grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

Oracle 12c to 19c (non-tenant mode)

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the ac
count. create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

> **Note:** To create a global account that starts with C## for a multitenant CDB$ROOT in Oracle 12c to 19c (tenant mode), you must contact the O&M engineers to modify some parameters.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **Oracle** as the source database type and **DataHub** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint or IP address that is used to connect to the self- managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Oracle Type | Non-RAC Instance: If you select this option, you must configure the SID parameter. RAC or PDB Instance: If you select this option, you must configure the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. |
|   | Database Password | The password of the database account. |

| Destination Database | Database Type | The type of the destination database. SelectD ataHub. |
|---|---|---|
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the DataHub project. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. After the whitelist is configured, click **Test Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Configure the synchronization policy and the objects to be synchronized. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | Incremental Data Synchronization is automatically selected. By default, you must also select Schema Synchronization. Full Data Synchronization is not supported. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Apply New Naming Rules of Additional Columns | After DTS synchronizes data to DataHub, DTS adds additional columns to the destination topic. If the names of additional columns are the same as the names of existing columns in the destination topic, data synchronization fails. Configure this parameter based on your business requirements. New Rule: Adopt new naming rules for additional columns. Previous Rule: Adopt old naming rules for additional columns. Do Not Use Default Naming Rules of Additional Columns: Do not adopt any rules for additional columns. Warning Before you set this parameter, check whether additional columns have the same names as the existing columns in the destination topic. |
| Capitalization of Object Names in Destination Instance | Specify the capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects that you want to synchronize in theS ource Objects section and click the icon to move the objects to the Selected Objects section. |

| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations that are performed on a specific table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click a table in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |
|---|---|

7. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Select Encoding Type | The encoding type of data written to the source database. You can select an encoding type based on your business requirements. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Valid values: Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

**Schema of a DataHub topic**

When DTS synchronizes incremental data to a DataHub topic, DTS adds additional columns to store metadata. The following figure shows the schema of a DataHub topic.

> **Note:** In this example, `id` , `name` , and `address` are data fields. DTS adds the `dts_` prefix to data fields because the naming rules of the previous version for additional columns are used.

The following table describes the additional columns in the DataHub topic.

|   |   | Previous additional column name |   |   | New additional column name |   |   | Data type | Description |
|---|---|---|---|---|---|---|---|---|---|
|   |   | dts record _ |   |   |   |   |   | String | The unique ID of the incremental log entry. Note By default, the ID auto- increments for each new log entry. In disaster recovery scenarios, rollback may occur, and the ID may not auto- increment. Therefore, some IDs may be duplicated. If an UPDATE operation is performed, DTS generates two incremental log entries to record the pre- update and post-update values. The values of the dts record id field in _ _ the two incremental log entries are the same. |
|   |   |   | dts record _ |   |   |   | new dts sync dts rec _ _ _ _ | String |   |
|   |   | id _ |   |   |   |   |   |   |   |
|   |   |   |   |   | ord id _ |   |   |   |   |

|   |   | dts operat _ |   |   |   |   |   |   |   |   |   |   |   | String | The operation type. Valid values: I: an INSERT operation D: a DELETE operation U: an UPDATE operation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | dts operat _ |   |   |   |   |   |   | new _ |   |   | dts sync dts ope _ _ _ | String |   |
|   |   | ion flag _ |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ration flag _ |   |   |   |   |   |   |
|   |   | dts instan _ |   |   |   |   |   |   |   |   |   |   |   | String | The server ID of the database. The value is null . The actual value is not displayed. This ensures database security. |
|   |   |   | dts instan _ |   |   |   |   |   |   | ne |   | w dts sync dts ins _ _ _ _ |   | String |   |
|   |   | ce id _ |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | tance id _ |   |   |   |   |   |   |
|   |   | dts db nam _ _ |   |   |   |   |   |   | new dts sync dts db _ _ _ _ _ name |   |   |   |   | String | The name of the database. |
|   |   |   | dts db nam _ _ |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | e |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | dts table _ _ |   |   |   |   |   |   |   |   |   |   |   | String | The name of the table in the database. |
|   |   |   | dts table _ _ |   |   |   |   |   |   | n | ew dts sync dts tab _ _ _ _ |   |   | String |   |
|   |   | name |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | le name _ |   |   |   |   |   |   |
|   |   | dts utc ti |   |   |   |   |   |   | new dts sync dts utc _ _ _ _ timestamp _ |   |   |   |   | String | The operation timestamp, in UTC. It is also the timestamp of the redo log file. |
|   |   |   |   |   |   |   |   |   |   | new dts sync dts utc _ _ _ _ |   |   |   |   |   |
|   |   |   | dts utc ti |   |   |   |   |   |   | new _ |   |   |   |   |   |
|   |   |   | _ _ |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | mestamp |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | dts before _ |   |   |   |   |   |   |   |   |   |   |   | String | Indicates whether the column values are pre-update values. Valid values: Y and N. |
|   |   |   | dts before _ |   |   |   |   |   |   | ne |   | w dts sync dts bef _ _ _ _ |   | String |   |
|   |   | flag _ |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ore flag _ |   |   |   |   |   |   |
|   |   | dts after _ _ |   |   |   |   |   |   |   |   |   |   |   | String | Indicates whether the column values are post-update values. Valid values: Y and N. |
|   |   |   | dts after _ _ |   |   |   |   |   |   | n | ew dts sync dts aft _ _ _ _ |   |   | String |   |
|   |   | flag |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | er flag _ |   |   |   |   |   |   |

| new dts sync dts db _ _ _ _ _ | Stri |
|---|---|

**Additional information about the dts_before_flag and**

**dts_after_flag fields**

The values of the `dts_before_flag` and `dts_after_flag` fields in an incremental log entry vary based on operation types: INSERT operation For an INSERT operation, the column values are the newly inserted record values (postupdate values). The value of the `dts_before_flag` field is N, and the value of the `dts_after_flag` field is Y. UPDATE operation DTS generates two incremental log entries for an UPDATE operation. The two incremental log entries have the same values for the `dts_record_id` , `dts_operation_flag` , and `dts_utc_timestamp` fields. The first log entry records the pre-update values. Therefore, the value of the `dts_before_flag` field is Y, and the value of the `dts_after_flag` field is N. The second log entry records the post-update values. Therefore, the value of the `dts_before_flag` field is N, and the value of the `dts_after_flag` field is Y. DELETE operation For a DELETE operation, the column values are the deleted record values (pre-update values). The value of the `dts_before_flag` field is Y, and the value of the `dts_after_flag` field is N.

#### 4.5.13 Synchronize data from a self-managed Oracle database to a MaxCompute project

**managed Oracle database to a MaxCompute**

**project**

This topic describes how to synchronize data in real time from a self-managed Oracle database to a MaxCompute project by using Data Transmission Service (DTS).

**Prerequisites**

The engine version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. The self-managed Oracle database is running in ARCHIVELOG mode. Archived log files are accessible, and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. The supplemental logging feature is enabled for the self-managed Oracle database, and the SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI parameters are set to Yes. For more information, see Supplemental Logging. A MaxCompute project is created to receive the synchronized data.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | Requirements for the objects to be synchronized: The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be synchronized cannot exceed 30 bytes in length. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, such as renaming tables or columns, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If the self-managed Oracle database is an Oracle Real Application Cluster (RAC) database, you can use only a single virtual IP address (VIP) rather than a Single Client Access Name (SCAN) IP address when you configure the data synchronization task. After you specify the VIP, node failover of the Oracle RAC database is not supported. The following requirements must be met: The redo logging and archive logging features must be enabled. If you perform only incremental data synchronization, the redo logs and archive logs of the source database must be stored for more than 24 hours. If you perform both schema synchronization and incremental data synchronization, the redo logs and archive logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the redo logs and archive logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the schema synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of redo logs and archive logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. If you perform a primary/secondary switchover on the source database when the data synchronization task is running, the task fails. |
|---|---|
| Other limits | Only tables can be selected as the objects to be synchronized. MaxCompute does not support PRIMARY KEY constraints. If network errors occur, DTS may synchronize duplicate data records to MaxCompute. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

**Permissions required for database accounts**

| Database | Required permissions | References |
|---|---|---|

| Self-managed Oracle database | DBA | CREATE USER and GRANT Important If you need to synchronize data from an Oracle database but the database administrator (DBA) permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account. |
|---|---|---|

**Enable logging and grant fine-grained permissions to an Oracle**

**database account**

> **Important:** If you need to synchronize data from an Oracle database but the DBA permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account.

1. Enable archive logging and supplemental logging.

| Log type | Procedure |
|---|---|
| Archive logging | Execute the following statements to enable archive logging: shutdown immediate; startup mount; alter database archivelog; alter database open; archive log list; |

| Supplemental logging | Enable supplemental logging at the database or table level based on your business requirements: Note You can enable database-level supplemental logging to ensure the stability of Data Transmission Service (DTS) tasks. You can enable table-level supplemental logging to reduce the disk usage of the source Oracle database. Enable database-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Execute the following statement to enable primary key and unique key supplemental logging at the database level: alter database add supplemental log data (primary key,unique index) columns; Enable table-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Enable table-level supplemental logging by using one of the following methods: Execute the following statement to enable primary key supplemental logging at the table level: alter table table name add supplemental log data (primary _ key) columns; Execute the following statement to enable table-level supplemental logging for all columns: alter table tb name add supplemental log data (all) _ columns ; |
|---|---|

2. Grant fine-grained permissions to an Oracle database account.
Oracle 9i to 11g

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the ac
count. create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; -- system tables grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct;
```

Oracle 12c to 19c (tenant mode)

```bash
# Switch to the pluggable database (PDB). Create a database account, such as rdsdt_
dtsacct, and grant permissions to the account. ALTER SESSION SET container = ORCLPDB1; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grantselectan tabletordsdtdtsacct
```

```bash
grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; -- V$PDBS privileges grant select on V_$PDBS to rdsdt_dtsacct;
# Switch to the container database (CDB). Create a database account and grant permi
ssions to the account by using one of the following methods: ALTER SESSION SET container = CDB$ROOT;
# Method 1: Create a global account that starts with C##, such as C##rdsdt_dtsacct,
and grant permissions to the account. If you use this method, you must contact the O&M engineers of DTS. create user C##rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to C##rdsdt_dtsacct; grant connect to C##rdsdt_dtsacct; grant resource to C##rdsdt_dtsacct; grant select on v_$logmnr_contents to C##rdsdt_dtsacct; grant LOGMINING to C##rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to C##rdsdt_dtsacct; grant execute on sys.dbms_logmnr to C##rdsdt_dtsacct;
# Method 2: Create a database account, such as rdsdt_dtsacct, and grant permissions
to the account. If you use this method, you must modify the default parameters of t he Oracle database. alter session set "_ORACLE_SCRIPT"=true; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant select on v_$logmnr_contents to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grantEXECUTECATALOGROLEtordsdtdtsacct;
```

```
grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

Oracle 12c to 19c (non-tenant mode)

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the ac
count. create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

> **Note:** To create a global account that starts with C## for a multi-tenant CDB$ROOT in Oracle 12c to 19c (tenant mode), you must contact the O&M engineers to modify some parameters.

**Configure a data synchronization task**

This section describes how to configure a data synchronization task to synchronize data from a self-managed Oracle database to a MaxCompute project in real time.
1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **Oracle** as the source database type and **MaxCompute** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The endpoint or IP address that is used to connect to the self- managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Oracle Type | The architecture of the self-managed Oracle database. If you select Non-RAC Instance, you must configure the SID parameter. If you select RAC or PDB Instance, you must configure the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. |
|   | Database Password | The password of the database account. |

| Destination Database | Database Type | The type of the destination database. SelectM axCompute. |
|---|---|---|
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the MaxCompute project. |
|   | AccessKey ID of Alibaba Cloud Account | The AccessKey ID and AccessKey secret of the account that you use to connect to the destination MaxCompute project. Note For more information about how to obtain an AccessKey pair, see the "Obtain the AccessKey pair of an organization" topic in the documentation of MaxCompute. |
|   | AccessKey Secret of Alibaba Cloud Account |   |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. After the whitelist is configured, click **Test Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Click **OK** to grant permissions to your MaxCompute account.
7. Select the synchronization policy and the objects to be synchronized. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Apply New Naming Rules of Additional Columns | After DTS synchronizes data to MaxCompute, DTS adds additional columns to the destination topic. If the names of additional columns are the same as the names of existing columns in the destination topic, data synchronization fails. Set this parameter based on your business requirements. Valid values: New Rule: adopts new naming rules for additional columns. Previous Rule: adopts old naming rules for additional columns. Do Not Use Default Naming Rules of Additional Columns: does not adopt any rules for additional columns. Warning Before you set this parameter, check whether additional columns have the same names as the existing columns in the destination table. |
| Partition Definition of Incremental Data Table | Select the partition names based on your business requirements. |

| Source Objects | Select one or more objects (tables or databases) in theS ource Objects section and click the icon to move the objects to the Selected Objects section. Note If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note To select the SQL operations performed on a specific database or table, right-click an object in the Selected Objects section. In the dialog box that appears, select the SQL operations that you want to synchronize. To specify WHERE conditions to filter data, right-click a table in the Selected Objects section. In the dialog box that appears, specify the conditions. For more information, see Use SQL conditions to filter data. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

8. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Select Encoding Type | The encoding type of data written to the source database. You can select an encoding type based on your business requirements. |
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Valid values: Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

9. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

0. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.14 Synchronize data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to an AnalyticDB for MySQL V3.0 cluster

**PostgreSQL (Compatible with Oracle) cluster**

**to an AnalyticDB for MySQL V3.0 cluster**

AnalyticDB for MySQL is a real-time online analytical processing (OLAP) service that is developed by Alibaba Cloud for online data analysis with high concurrency. This topic describes how to synchronize data from a PolarDB for PostgreSQL (Compatible with Oracle) cluster to an AnalyticDB for MySQL V3.0 cluster by using Data Transmission Service (DTS).

**Prerequisites**

The tables that you want to synchronize from the source PolarDB for PostgreSQL (Compatible with Oracle) cluster contain primary keys or UNIQUE NOT NULL indexes.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server on which the source database is deployed must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed decreases. The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you want to edit the tables in the destination database, such as renaming tables or columns, you can synchronize up to 1,000 tables in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. The write-ahead logging (WAL) feature must be enabled. If you perform only incremental data synchronization, the WAL logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the WAL logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the WAL logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of WAL logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. If one or more long-running transactions exist in the source database and incremental data is synchronized in the data synchronization task, the WAL logs generated before the long-running transactions in the source database are committed may be accumulated. As a result, the disk space of the source database may be insufficient. During schema synchronization and full data synchronization, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data synchronization task fails. |

| Other limits | Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. Due to the limits of AnalyticDB for MySQL V3.0, if the disk space usage of nodes in an AnalyticDB for MySQL V3.0 cluster exceeds 80%, the data synchronization task is delayed and an error is returned. We recommend that you estimate the required disk space based on the objects to be synchronized. You must make sure that the destination cluster has sufficient storage space. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |
|---|---|

**SQL operations that can be synchronized**

INSERT, UPDATE, and DELETE

> **Note:** When you write data to an AnalyticDB for MySQL V3.0 cluster, the UPDATE statement is automatically converted to the REPLACE INTO statement.

**Procedure**

1. Create a data synchronization task. For more information, see Create a data
synchronization instance.

> **Note:** When you create a data synchronization task, select **PolarDB-O** as the source database type, **AnalyticDB for MySQL 3.0** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select PolarDB-O. |

| er Guide·Data sy | nchronization Data Transmission Servic |   |
|---|---|---|
| Source Database |   |   |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Architecture | The architecture of the data synchronization task. Default value: dts.common.engineArchType.localDiskDoubleNode. Only this architecture type is supported. |
|   | Instance ID | The ID of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Database Name | The name of the source database to be synchronized. |
|   | Database Account | The privileged account of the source PolarDB for PostgreSQL (Compatible with Oracle) cluster. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. SelectA nalyticDB for MySQL 3.0. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for MySQL V3.0 cluster. |
|   | Database Account | The database account of the destination AnalyticDB for MySQL V3.0 cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|

| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
|---|---|
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| DDL and DML Operations to Be Synchronized | The SQL operations to be synchronized during incremental data synchronization at the instance level. For more information, see the SQL operations that can be synchronized section of this topic. Note To select the SQL operations performed on a specific database or table, perform the following steps: In the Selected Objects section, right-click an object. In the dialog box that appears, select the SQL operations that you want to synchronize. |

| Merge Tables | Specifies whether to merge tables. If you select Yes, DTS adds the dts data source column to each table to store data sources. In this __ _ _ case, DDL operations cannot be synchronized. Note After you select multiple tables from the source database, you must change the names of these tables to the name of the destination table. To do this, you can use the object name mapping feature. If you select No, DDL operations can be synchronized. By default, No is selected. Important If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. If you enable the multi-table merging feature for an incremental data synchronization task, DDL operations are not supported to be synchronized. If you perform DDL operations on the source database, data loss occurs in the destination database or the task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination database. By default, DTS default policy is selected. You can select other options to ensure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select objects (tables or a database) from the Source Objects section and click the icon to move the objects to the Selected Objects section. |
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter or setting | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. The data synchronization task does not support the ETL feature. Select No. |

7. **Optional:**Click **Next: Configure Database and Table Fields** and specify a type for the
tables that you want to synchronize to the destination database.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key column**, and **distribution key** for the tables that you want to synchronize to the destination AnalyticDB for MySQL cluster.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.15 Synchronize data between ApsaraDB for Redis instances

**for Redis instances**

You can use Data Transmission Service (DTS) to perform one-way or two-way data synchronization between ApsaraDB for Redis instances. This feature is applicable to scenarios such as resource migration or resource merging and business architecture adjustment.

**Prerequisites**

If the source ApsaraDB for Redis instance is a Community Edition instance, the engine version is 4.0 or 5.0. If the source ApsaraDB for Redis instance is an Enhanced Edition (Tair) instance, the engine version is 5.0.

> **Note:** The engine version of the destination ApsaraDB for Redis instance can be 4.0 or 5.0. The engine version of the destination ApsaraDB for Redis instance must be the same as or later than that of the source ApsaraDB for Redis instance. Before you synchronize data between two ApsaraDB for Redis instances that use different engine versions, check the compatibility of the two versions.

The source ApsaraDB for Redis instance is deployed in a virtual private cloud (VPC). SSL encryption is disabled for the source ApsaraDB for Redis instance. The available storage space of the destination ApsaraDB for Redis instance is larger than the total size of the data in the source ApsaraDB for Redis instance. ApsaraDB for Redis Enhanced Edition (Tair) is integrated with more Redis modules than ApsaraDB for Redis Community Edition. To ensure compatibility between the source and destination instances, if the source instance is an Enhanced Edition (Tair) instance, the destination instance must be an Enhanced Edition (Tair) instance.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The collections to synchronize must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. To ensure the synchronization quality, DTS adds the following key to the source database: DTS REDIS TIMESTAMP HEARTBEAT. This key is used to record the _ _ _ time when data is synchronized to the destination database. To ensure the stability of data synchronization, we recommend that you increase the value of the repl-backlog-size parameter in the redis.conf file. The following requirements for append-only file (AOF) logging must be met: The AOF logging feature must be enabled. If you perform only incremental data synchronization, the AOF logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the AOF logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the AOF logs, and your data synchronization task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of AOF logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Note This limit is not applied to ApsaraDB for Redis instances. If an expiration policy is enabled for specific keys in the source database, these keys may not be deleted at the earliest opportunity after they expire. Therefore, the number of keys in the destination database may be less than that in the source database. You can run the INFO command to view the number of keys in the destination database. If an expiration policy is enabled for specific keys in the source database, these keys may not be deleted at the earliest opportunity after they expire. Therefore, the number of keys in the destination database may be less than that in the source database. You can run the INFO command to view the number of keys in the destination database. If the data eviction policy ( maxmemory-policy ) of the destination database is not set to noeviction , data inconsistency may occur between the source and destination databases. |
|---|---|

|   | maxmemory-policy |
|---|---|
| noeviction |   |

| Other limits | During data synchronization, if the number of shards in the source ApsaraDB for Redis instance is increased or decreased, or if you change the database specifications, such as scaling up the memory capacity, you must reconfigure the data synchronization task. To ensure data consistency, we recommend that you clear the data that has been synchronized to the destination database before you reconfigure the data synchronization task. During data synchronization, if the endpoint of the source ApsaraDB for Redis instance is changed, you must contact technical support to update the change. Otherwise, the AOF logs of the ApsaraDB for Redis instance may be reset. In this case, you must reconfigure the task. To ensure compatibility, make sure that the version of the destination database is the same as or later than that of the source database. If the version of the destination database is earlier than that of the source database, database compatibility issues may occur. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During data synchronization, we recommend that you use only DTS to write data to the destination database. This prevents data inconsistency between the source and destination databases. For example, if you use tools other than DTS to write data to the destination database, data loss may occur in the destination database when you use Data Management (DMS) to perform online DDL operations. |
|---|---|

**SQL operations that can be synchronized**

| Edition | SQL operation |
|---|---|
| ApsaraDB for Redis Community Edition | APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, and PSETEX RENAME, RENAMENX, RESTORE, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE SWAPDB and UNLINK (These two commands can be synchronized only if the engine version of the source instance is Redis 4.0.) |

| ApsaraDB for Redis Enhanced Edition (Tair) | APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, and PSETEX RENAME, RENAMENX, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE UNLINK, ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE |
|---|---|

> **Note:** PUBLISH operations cannot be synchronized.
> If you run the EVAL or EVALSHA command to call Lua scripts, DTS cannot identify whether these Lua scripts are executed on the destination instance. This is because the destination instance does not explicitly return the execution results of Lua scripts during incremental data synchronization.
> When DTS runs the SYNC or PSYNC command to transfer data of the LIST type, DTS does not clear the existing data in the destination instance. As a result, the destination instance may contain duplicate data records.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create a data synchronization task, select **Redis** as the source database type, **Redis** as the destination database type, and **One-way Synchronization** as the synchronization topology.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select Redis. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Instance ID | The ID of the source ApsaraDB for Redis instance. |
|   | Database Password | The database account of the source ApsaraDB for Redis instance. The account must have the read permissions on the source database. If you forget the password, you can reset the password. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. Note This parameter is optional and can be left empty if no password is set. |
|   | Database Type | The type of the destination database. SelectR edis. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

| Destinati |   |   |
|---|---|---|
|   | Instance ID | The ID of the destination ApsaraDB for Redis instance. |
| on Database |   |   |
|   | Database Password | The database account of the destination ApsaraDB for Redis instance. The account must have the read and write permissions on the destination database. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the objects to be synchronized and advanced settings. The following table
describes the parameters.

| Parame ter | Description |
|---|---|
| Task Stages | By default, Full Data Synchronization and Incremental Data Synchronization are selected. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source database to the destination database. The historical data is the basis for subsequent incremental synchronization. Note Full data synchronization is supported only for ApsaraDB for Redis Enhanced Edition (Tair) instances. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, data may fail to be initialized, only some columns are synchronized, or the data synchronization task fails. Operate with caution. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can select only databases as the objects to be synchronized. You cannot select keys as the objects to be synchronized. |
| Selecte d Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. The data synchronization task does not support the ETL feature. Select No. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.16 Synchronize data from a self-managed MongoDB database to an ApsaraDB for MongoDB instance

**managed MongoDB database to an ApsaraDB**

**for MongoDB instance**

This topic describes how to synchronize data from a self-managed MongoDB database to an ApsaraDB for MongoDB instance by using Data Transmission Service (DTS).

**Prerequisites**

The version of the source MongoDB database is 3.0, 3.2, 3.4, 3.6, 4.0, or 4.2.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The source database cannot be a MongoDB sharded cluster. Bandwidth requirements: The server to which the source database belongs must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed is affected. The collections to be synchronized must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select collections as the objects to be synchronized and you want to edit the collections in the destination database, such as renaming the collections, up to 1,000 collections can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 collections, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the collections in batches, or configure a task to synchronize the entire database. The oplog feature must be enabled. Note If you perform only incremental data synchronization, the oplogs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the oplogs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the oplogs and the task may fail. In exceptional cases, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of oplogs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. If you perform a primary/secondary switchover on the source database during synchronization, the synchronization task fails. DTS calculates synchronization latency based on the timestamp of the latest synchronized data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the synchronization latency may be inaccurate. If the latency of the data synchronization task is excessively high, you can perform a DML operation on the source database to update the latency. Note If you select an entire database as the object to be synchronized, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |
|---|---|

| Other limits | If you need to synchronize incremental data from a standalone MongoDB instance, you must enable the oplog feature. A standalone MongoDB instance contains only a primary node. For more information, see Preparation for a standalone MongoDB instance. To ensure compatibility, the version of the destination ApsaraDB for MongoDB instance must be the same as or later than the version of the source MongoDB database. The admin or local database cannot be used as the source or destination database. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the collections of the destination database. After initial full data synchronization is complete, the storage usage of collections in the destination database is larger than that of collections in the source database. Make sure that the destination ApsaraDB for MongoDB database does not have the same primary key as the source database. Otherwise, data loss may occur in the destination database. The default primary key is id. If the destination database has _ the same primary key as the source database, delete the related data from the destination database without affecting your business. For example, if the destination database has the same primary key id as the source database, delete the data that _ has the same id as the data in the source database from the destination database. _ You must use the db.$table name.aggregate([{ $count:"myCount"}]) syntax _ to query the return value of a count operation on the destination ApsaraDB for MongoDB database. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, you must stop or release the failed data synchronization tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination instance after a failed data synchronization task is resumed. |
|---|---|

**Synchronization types**

| Synchronization type | Description |
|---|---|
| Schema synchronization | DTS synchronizes the schemas of the objects to be synchronized from the source MongoDB database to the destination ApsaraDB for MongoDB instance. |
| Full data synchronization | DTS synchronizes all historical data of the objects to be synchronized from the source database to the destination database. Note DTS can synchronize historical data of databases, collections, and indexes. |

| Incremental data synchronization | DTS synchronizes incremental data from the source database to the destination database after full data synchronization is complete. Note DTS can synchronize CREATE and DELETE operations on databases, collections, and indexes. DTS can synchronize INSERT, DELETE, and UPDATE operations on documents. |
|---|---|

**Preparation for a standalone MongoDB instance**

If you need to synchronize incremental data from a standalone MongoDB instance, you must enable the oplog feature. A standalone MongoDB instance contains only a primary node.

> **Note:** When you enable the oplog feature, the MongoDB service is restarted. We recommend that you perform this operation during off-peak hours.

1. Use Mongo Shell to connect to the source database.
2. Run the following commands to shut down the MongoDB service:

```
use admin db.shutdownServer()
```

3. Run the following command to start the MongoDB service from the backend as a replica
set:

```
mongod --port 27017 --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log - -replSet rs0 --bind_ip 0.0.0.0 --auth --fork
```

> **Note:** The database path used by the preceding command is /var/lib/mongodb. The log file path is /var/log/mongodb/mongod.log. You must specify the paths based on your business requirements.
> The command uses `0.0.0.0` as the IP address associated with the MongoDB database. This allows you to access the database by using a random IP address. After the synchronization is complete, run the `kill` command to end the process. Then, start the MongoDB service by using the original configuration file.
> The command enables authentication. You can access the MongoDB database only after you pass the authentication.

4. Use Mongo Shell to connect to the source database again.
5. Run the following commands to initialize the replica set:

```
use admin rs.initiate()
```

6. Wait until the role of the current node changes to primary, which indicates that oplog is
enabled.

> **Note:** You can run the `rs.printReplicationInfo()` command to view the status of the oplog feature.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, set the Source Database Type parameter to **MongoDB**, the Destination Database Type parameter to **MongoDB**, and the Synchronization Topology parameter to **One-way** **Synchronization**.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Databas e | Database Type | The type of the source database. Select MongoDB. |
|   | Access Method | The access method of the source database. Select Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you set the Access Method parameter to Public IP Address, you do not need to set the Instance Region parameter. |
|   | Domain Name or IP | The endpoint that is used to connect to the source database. |
|   | Port Number | The service port number of the source database. |
|   | Database Name | The name of the authentication database. The database account is created in this database. |
|   | Database Account | The database account of the source MongoDB database. The account must have the read permissions on the source database, admin database, and local database. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source database. In this example, Non-encrypted is selected. Note You need to select SSL-encrypted only if the source database is a MongoDB Atlas database. |
|   | Database Type | The type of the destination database. SelectM ongoDB. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |

| er Guide·Data |   |   |
|---|---|---|
| Destinat ion Databas e |   |   |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Architecture | The architecture type of the destination ApsaraDB for MongoDB instance. |
|   | Instance ID | The ID of the destination ApsaraDB for MongoDB instance. |
|   | Authenticati on Database | The name of the authentication database. The database account is created in this database. Note If you want to use the root account, enter admin in the Database Name field. |
|   | Database Account | The database account of the destination ApsaraDB for MongoDB instance. The account must have the dbAdminAnyDatabase permission, the read and write permissions on the destination database, and the read permissions on the local database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed MongoDB database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist of the self-managed MongoDB database. Then, click **Text Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for your self-managed MongoDB database, ignore the preceding settings and click **Test Connectivity and Proceed**.

6. Select the objects to be synchronized and the synchronization types.

| Parame ter or setting | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Select the process ing mode of conflict ing tables | Precheck and Report Errors: checks whether the destination database contains collections that have the same names as collections in the source database. If the source and destination databases do not contain collections that have identical collection names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical collection names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. DTS does not synchronize data records that have the same primary key values as data records in the destination database. Data may fail to be initialized, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Synchr onizati on Topolo gy | Select One-way Synchronization. Note Only one-way synchronization is supported for data synchronization from a self-managed MongoDB database to an ApsaraDB for MongoDB instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select databases or collections as the objects to be synchronized. |
| Selecte d Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.17 Synchronize data between ApsaraDB for MongoDB instances

**for MongoDB instances**

This topic describes how to synchronize data between ApsaraDB for MongoDB instances by using Data Transmission Service (DTS).

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed is affected. The collections to be synchronized must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select collections as the objects to be synchronized and you want to edit the collections in the destination database, such as renaming the collections, up to 1,000 collections can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 collections, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the collections in batches or configure a task to synchronize the entire database. DTS cannot synchronize data from an ApsaraDB for MongoDB sharded cluster instance to an ApsaraDB for MongoDB replica set instance. The oplog feature must be enabled. Note If you perform only incremental data synchronization, the oplogs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the oplogs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the oplogs and the task may fail. In exceptional cases, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of oplogs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. |
|---|---|

| Other limits | If you need to synchronize incremental data from an ApsaraDB for MongoDB standalone instance, you must enable the oplog feature. An ApsaraDB for MongoDB standalone instance contains only a primary node. For more information, see Preparation for a standalone MongoDB database. To ensure compatibility, the version of the destination ApsaraDB for MongoDB instance must be the same as or later than the version of the source ApsaraDB for MongoDB instance. The admin or local database cannot be used as the source or destination database. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the collections of the destination database. After initial full data synchronization is complete, the storage usage of collections in the destination database is larger than that of collections in the source database. Make sure that the destination ApsaraDB for MongoDB instance does not have the same primary key as the source ApsaraDB for MongoDB instance. Otherwise, data loss may occur in the destination database. The default primary key is id. If the _ destination database has the same primary key as the source database, delete the related data from the destination database without affecting your business. For example, if the destination database has the same primary key id as the source _ database, delete the data that has the same id as the data in the source database _ from the destination database. You must use the db.$table name.aggregate([{ $count:"myCount"}]) syntax _ to query the return value of a count operation on the destination ApsaraDB for MongoDB instance. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, you must stop or release the failed data synchronization tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database overwrites the data in the destination instance after a failed data synchronization task is resumed. |
|---|---|

**Synchronization types**

| Synchronization type | Description |
|---|---|
| Schema synchronization | DTS synchronizes the schemas of the objects to be synchronized from the source ApsaraDB for MongoDB instance to the destination ApsaraDB for MongoDB instance. |
| Full data synchronization | DTS synchronizes all historical data of the objects to be synchronized from the source database to the destination database. Note DTS can synchronize historical data of databases, collections, and indexes. |

| Incremental data synchronization | DTS synchronizes incremental data from the source database to the destination database after full data synchronization is complete. Note DTS can synchronize CREATE and DELETE operations on databases, collections, and indexes. DTS can synchronize INSERT, DELETE, and UPDATE operations on documents. |
|---|---|

**Preparation for a standalone MongoDB database**

If you need to migrate incremental data from a standalone MongoDB database, you must enable the operation logging feature. A standalone MongoDB database contains only a primary node. If you do not need to perform incremental data migration, skip the following steps.

> **Note:** When you enable the operation logging feature, the MongoDB service is restarted. We recommend that you perform this operation during off-peak hours.

1. Use Mongo Shell to connect to the source database.
2. Run the following commands to shut down the MongoDB service:

```
use admin db.shutdownServer()
```

3. Run the following command to start the MongoDB service from the backend as a replica
set:

```
mongod --port 27017 --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log - -replSet rs0 --bind_ip 0.0.0.0 --auth --fork
```

> **Note:** The database path used by the preceding command is /var/lib/mongodb. The log file path is /var/log/mongodb/mongod.log. You must specify the paths based on your business requirements.
> The command uses `0.0.0.0` as the associated IP address of the MongoDB service. This allows you to access the database by using a random IP address. After the migration is complete, run the `kill` command to end the process, and start the MongoDB service by using the original configuration file.
> The command enables authentication. You can access the database only after you pass the authentication.

4. Use Mongo Shell to connect to the source database again.
5. Run the following commands to initialize the replica set:

```
use admin rs.initiate()
```

6. Wait until the role of the current node changes to primary. This indicates that the operation
logging feature is enabled.

> **Note:** You can run the `rs.printReplicationInfo()` command to view the status of the operation logging feature.

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, set the Source Database Type parameter to **MongoDB**, the Destination Database Type parameter to **MongoDB**, and the Synchronization Topology parameter to **One-way** **Synchronization**.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Databas e | Database Type | The type of the source database. Select MongoDB. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Architecture | The architecture type of the source ApsaraDB for MongoDB instance. |
|   | Instance ID | The ID of the source ApsaraDB for MongoDB instance. |
|   | Authenticati on Database | The name of the authentication database. The database account is created in this database. |
|   | Database Account | The database account of the source ApsaraDB for MongoDB instance. The account must have the read permissions on the source database, admin database, and local database. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectM ongoDB. |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |

| ta Transmissi | on Service User Guide·Data synchronizatio |   |
|---|---|---|
| Destinat ion Databas e |   |   |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Architecture | The architecture type of the destination ApsaraDB for MongoDB instance. Important If you select Sharded Cluster for the source ApsaraDB for MongoDB instance, you must select Sharded Cluster for the destination ApsaraDB for MongoDB instance. |
|   | Instance ID | The ID of the destination ApsaraDB for MongoDB instance. |
|   | Authenticati on Database | The name of the authentication database. The database account is created in this database. Note If you want to use the root account, enter admin in the Database Name field. |
|   | Database Account | The database account of the destination ApsaraDB for MongoDB instance. The account must have the dbAdminAnyDatabase permission, the read and write permissions on the destination database, and the read permissions on the local database. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed MongoDB database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist of the self-managed MongoDB database. Then, click **Text Connectivity and Proceed**.

> **Note:** If you do not need to configure a whitelist for your self-managed MongoDB database, ignore the preceding settings and click **Test Connectivity and Proceed**.

6. Select the objects to be synchronized and the synchronization types.

| Parame ter or setting | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Select the process ing mode of conflict ing tables | Precheck and Report Errors: checks whether the destination database contains collections that have the same names as collections in the source database. If the source and destination databases do not contain collections that have identical collection names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical collection names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data consistency may occur and your business may be exposed to potential risks. DTS does not synchronize data records that have the same primary key values as data records in the destination database. Data may fail to be initialized, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Synchr onizati on Topolo gy | Select One-way Synchronization. Note Only one-way synchronization is supported for data synchronization between ApsaraDB for MongoDB instances. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select databases or collections as the objects to be synchronized. |
| Selecte d Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.18 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances

**synchronization between ApsaraDB RDS for**

**MySQL instances**

##### 4.5.18.1 Overview

DTS supports two-way real-time data synchronization between RDS instances on any two clouds. This section describes how to use DTS to create a two-way synchronization task between two ApsaraDB RDS for MySQL instances for active geo-redundancy, geo-disaster recovery, and other scenarios.

##### 4.5.18.2 Supported synchronization statements

Two-way synchronization between ApsaraDB RDS for MySQL instances supports all DML updates (including INSERT, UPDATE, and DELETE) and the following DDL updates: ALTER TABLE, ALTER VIEW, ALTER FUNCTION, and ALTER PROCEDURE CREATE DATABASE, CREATE SCHEMA, CREATE INDEX, CREATE TABLE, CREATE PROCEDURE, CREATE FUNCTION, CREATE TRIGGER, CREATE VIEW, and CREATE EVENT DROP FUNCTION, DROP EVENT, DROP INDEX, DROP PROCEDURE, DROP TABLE, DROP TRIGGER, and DROP VIEW RENAME TABLE and TRUNCATE TABLE

> **Note:** To ensure the stability of a two-way synchronization channel, you can synchronize DDL updates on the same table in only one direction.
> For example, for two-way synchronization, you must enable DDL synchronization in either the **A-to-B** or **B-to-A** direction. If DDL synchronization is configured in one direction, it is not supported in the reverse direction. You can only perform DML synchronization.

##### 4.5.18.3 Detect and resolve conflicts

To ensure data consistency, for two-way synchronized instances, make sure that records with the same primary key, business primary key, or unique key are updated only on one of the instances. If you unexpectedly update a record with the same primary key, business primary key, or unique key on both instances that are two-way synchronized, a synchronization conflict occurs. To maximize the stability of two-way synchronized instances, DTS supports detecting and resolving data conflicts.

**Considerations**

During two-way synchronization, the system time of the source and destination instances may not be the same. Additionally, synchronization delays may occur. For these reasons, DTS cannot guarantee that its conflict detection mechanism can completely prevent data conflicts. You must refactor certain business logic to ensure that records of the same primary key, business primary key, or unique key are updated only on one of the instances that are two-way synchronized.

**Supported conflict types**

Currently, DTS supports detecting the following conflict types: Uniqueness conflicts caused by INSERT operations A uniqueness conflict occurs when the synchronization of an inserted row violates the unique constraint. For example, if two instances in two-way synchronization insert a record with the same primary key value at almost the same time, one of the inserted records fails to be synchronized because a record with the same primary key value already exists in the destination instance. Inconsistent records caused by UPDATE operations Update conflicts occur in the following scenarios: The records to be updated do not exist in the destination instance. If the records to be updated do not exist, DTS automatically changes the UPDATE operation to the INSERT operation and inserts these records to the destination instance. In this case, duplicate unique key values may occur. The primary keys or unique keys of the records to be updated conflict with each other. A DELETE operation is made on non-existent records A delete conflict occurs when the records to be deleted do not exist in the destination instance. In this case, DTS automatically ignores the DELETE operation regardless of the conflict resolution policy that you have configured.

**Supported conflict resolution policies**

For the preceding synchronization conflicts, DTS provides the following resolution policies. You can select a conflict resolution policy as required when configuring two-way synchronization. TaskFailed: The synchronization task reports an error and automatically exits the process in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task reports an error and automatically exits the process. The task enters a failed state and you must manually resolve the conflict. This method is the default conflict resolution policy. Ignore: The records in the destination instance are used in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task skips the current synchronization statement and continues the process. The records in the destination instance are used. Overwrite: The conflict records in the destination instance are overwritten in case of a conflict. When the synchronization encounters a conflict of the preceding types, the conflict records in the destination instance are overwritten.

##### 4.5.18.4 Limits on data synchronization

This topic describes the limits on two-way data synchronization tasks that are configured by using Data Transmission Service (DTS).

**Limits on data sources**

Only ApsaraDB RDS for MySQL instances support two-way data synchronization. Other heterogeneous data sources do not support two-way data synchronization. The destination instance cannot be an ApsaraDB RDS for MySQL instance that is accessible in standard mode and has only public endpoints.

**Limits on the synchronization topology**

DTS supports two-way data synchronization between only two ApsaraDB RDS for MySQL instances. Only two-way one-to-one synchronization is supported in DTS.

**Limits on features**

Incompatibility with triggers If the object to be synchronized is the entire database and the database contains a trigger that updates the tables to be synchronized, data inconsistency may occur. For example, the object to be synchronized is Database A that contains Table A and Table B. Table A has a trigger that inserts a row of data into Table B after the row of data is inserted into Table A. In this case, if an INSERT operation is performed on Table A in the source instance during data synchronization, the data in Table B is inconsistent between the source and destination instances. To fix the issue, you must delete the trigger in the destination instance. The data in Table B is synchronized from the source instance. Limits on the RENAME TABLE operation The RENAME TABLE operation may cause data inconsistency between the source and destination instances. For example, if the object to be synchronized includes only Table A and the **rename a to b** command is run in the source instance during data synchronization, subsequent operations on the renamed Table B are not synchronized to the destination instance. To fix the issue, you can synchronize the entire database in which Table A and Table B reside. Limits on DDL synchronization directions To ensure the stability of two-way data synchronization, you can synchronize the DDL operations on a single table only in one direction. For example, in A-to-B or B-to-A synchronization, you can synchronize DDL operations in the **A-to-B** or **B-to-A** direction. If the synchronization of DDL operations is configured in one direction, DDL operations cannot be synchronized in the reverse direction.

##### 4.5.18.5 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances

**between ApsaraDB RDS for MySQL instances**

This topic describes how to configure two-way data synchronization between ApsaraDB RDS for MySQL instances by using Data Transmission Service (DTS).

**Prerequisites**

A basic plan for two-way data synchronization is purchased before you configure two-way data synchronization. The source and destination ApsaraDB RDS for MySQL instances are created.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Note To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
|---|---|
| Other limits | To ensure compatibility, we recommend that you use the same engine versions for the source and destination MySQL databases. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

| Special cases | Take note of the following items when you configure two-way data synchronization between MySQL instances: DTS supports two-way data synchronization only between two MySQL databases. DTS does not support two-way data synchronization between multiple MySQL databases. Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. When DTS runs a two-way data synchronization task, DTS creates a database named dts in the destination database to prevent circular synchronization. When the task is running, do not modify the dts database. |
|---|---|

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Data Synchronization**.
3. On the **Data Synchronization** page, click **Create Task**. In the panel that appears,
configure parameters to create a data synchronization instance.

| Parameter | Description |
|---|---|
| Source Database Type | The type of the source database. Select MySQL. |
| Source Region | The region in which the source instance resides. Note You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Destination Database Type | The type of the destination database. SelectM ySQL. |
| Destination Region | The region in which the destination instance resides. Note You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Synchronization Topology | The synchronization topology of the data synchronization instance. Select Two-way Synchronization. |
| Quantity | The number of data synchronization instances that you want to create at a time. |

4. After you configure the parameters, click **Purchase Instance**. In the message that
appears, click **OK**. After you create a data synchronization instance, go back to the Data Synchronization page. The new data synchronization instance is in the Not Configured state and contains two data synchronization tasks. You can configure data synchronization tasks in the forward and reverse directions.
5. Find the data synchronization task in the forward direction and click **Configure Task**.

> **Note:** When you configure the data synchronization task in the forward direction, the data synchronization task in the reverse direction cannot be configured.

6. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source ApsaraDB RDS for MySQL instance resides. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   | Alibaba Cloud Account | The ID of the Alibaba Cloud account to which the source instance belongs. |
|   | RAM Role Name | The name of the Resource Access Management (RAM) user that is configured by the Alibaba Cloud account to which the source instance belongs. |
|   | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source instance. Select Non-encrypted or SSL- encrypted based on your business requirements. In this example, Non-encrypted is selected. |
| Destination Database | Database Type | The type of the destination database. Select MySQL. |
|   | Access Method | The access method of the destination database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination ApsaraDB RDS for MySQL instance resides. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Password | The password of the database account. |
| Document Version: 2 | 0240522 37 |   |

|   | Encryption | Specifies whether to encrypt the connection to the destination instance. Select Non-encrypted or SSL-encrypted based on your business requirements. In this example, Non-encrypted is selected. |
|---|---|---|

7. In the lower part of the page, click **Test Connectivity and Proceed**.

> **Note:** DTS automatically adds the CIDR blocks of DTS servers in the source or destination region to the whitelist of the source or destination instance.
> After data synchronization is complete, we recommend that you remove the CIDR blocks of DTS servers from the whitelists.

8. Select the processing mode of conflicting tables and the objects to be synchronized.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Note You can use the object name mapping feature to rename the tables that are synchronized to the destination database. You can use this feature if the source and destination databases contain identical table names and the tables in the destination database cannot be deleted or renamed. For more information, see Rename an object to be synchronized. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Exclude DDL Statements | Yes: excludes DDL operations. No: synchronizes DDL operations. Important Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. |

| Conflict Resolution Policy | The resolution policy for synchronization conflicts. By default, TaskFailed is selected. You can select a conflict resolution policy based on your business requirements. TaskFailed The default conflict resolution policy. If a conflict occurs during data synchronization, the synchronization task reports an error and exits. The task enters a failed state and you must manually resolve the conflict. Ignore If a conflict occurs during data synchronization, the synchronization task ignores the current statement and continues. The conflicting records in the destination database are used. Overwrite If a conflict occurs during data synchronization, the conflicting records in the destination database are overwritten. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to add the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be synchronized. If you select tables or columns as the objects to be synchronized, DTS does not synchronize other objects such as views, triggers, or stored procedures to the destination database. |
| Selected Objects | To rename an object that you want to synchronize to the destination instance, right-click the object in the Selected Objects section. For more information, see Rename an object to be synchronized. For information about how to specify WHERE conditions to filter data, see Use SQL conditions to filter data. To select the DML and DDL operations, right-click an object in theS elected Objects section. In the dialog box that appears, select the DML and DDL operations that you want to synchronize. |

9. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

| Configure ETL | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |
|---|---|

0. In the lower part of the page, click **Next: Precheck and Start Task**.
1. Wait until the **Success Rate** value becomes **100%**. Then, click **Back**.
2. After the data synchronization task in the forward direction is initialized, you can configure
the data synchronization task in the reverse direction. For more information about how to configure the task, see the preceding Steps 6 to 11.

> **Important:** The source instance in the reverse direction corresponds to the destination instance in the forward direction. The destination instance in the reverse direction corresponds to the source instance in the forward direction. You must also make sure that the parameter settings such as the database name, account, and password are consistent.

3. Wait until the two data synchronization tasks enter the **Running** state.

#### 4.5.19 Synchronize data between PolarDB-X 2.0 instances

### 2.0 instances

This topic describes how to synchronize data between PolarDB-X 2.0 instances by using Data Transmission Service (DTS).

**Prerequisites**

The source and destination PolarDB-X 2.0 instances are created and compatible with MySQL 5.7. The available storage space of the destination PolarDB-X 2.0 instance is larger than the total size of the data in the source PolarDB-X 2.0 instance.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, such as renaming tables or columns, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. The following requirements for binary logs must be met: Binary logging is enabled on the Calculation layer and Storage layer tabs in the PolarDB-X console. For more information, see the "Parameter settings" topic in the documentation of PolarDB-X. The binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during the precheck and the data synchronization task cannot be started. If you perform only incremental data synchronization, the binary logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the binary logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. The source PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |
|---|---|
| Other limits | The destination PolarDB-X 2.0 instance must be compatible with MySQL 5.7. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost and pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

**SQL operations that can be synchronized**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

**Permissions required for database accounts**

| Database | Schema synchronization | Full data synchronization | Incremental data synchronization |
|---|---|---|---|
| Source PolarDB- X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be synchronized, REPLICATION SLAVE permission, and REPLICATION CLIENT permission |
| Destination PolarDB-X 2.0 Instance | Read and write permissions |   |   |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PolarDB-X 2.0** as the source and destination database types.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and the destination database. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. Default value:A libaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |

|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|---|---|---|
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. The account must have the SELECT permission on the objects to be synchronized, the REPLICATION CLIENT permission, and the REPLICATION SLAVE permission. |
|   | Database Password | The password of the database account. |
| Destinati on Database | Database Type | The type of the destination database. SelectP olarDB-X 2.0. |
|   | Access Method | The access method of the destination database. Default value: Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the destination PolarDB-X 2.0 instance. The account must have the read and write permissions on the destination PolarDB-X 2.0 instance. |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the objects to be synchronized and advanced settings. The following table
describes the parameters.

| Parame ter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of the selected objects from the source database to the destination cluster. The historical data is the basis for subsequent incremental synchronization. |

| Process ing Mode of Conflict ing Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data synchronization task cannot be started. Note If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are synchronized to the destination database. For more information, see Rename an object to be synchronized. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|

| Capitali zation of Object Names in Destina tion Instanc e | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
|---|---|
| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can select columns, tables, or databases as the objects to be synchronized. If you select tables or columns as the objects to be synchronized, DTS does not synchronize other objects such as views, triggers, and stored procedures to the destination database. |
| Selecte d Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|

| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
|---|---|
| Configure ETL | The extract, transform, and load (ETL) feature cannot be enabled for this data synchronization task. Select No. |
| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.20 Synchronize data from a PolarDB-X 2.0 instance to an ApsaraDB RDS for MySQL instance

### 2.0 instance to an ApsaraDB RDS for MySQL

**instance**

This topic describes how to synchronize data from a PolarDB-X 2.0 instance to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS).

**Prerequisites**

The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of data in the source PolarDB-X 2.0 instance.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, such as remaining tables or columns, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If you perform only incremental data synchronization, the binary logs of the source database are retained for at least 24 hours. If you perform both full data synchronization and incremental data synchronization, the binary logs of the source database are retained for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. If the source database is PolarDB-X 2.0 and the name of the table to be synchronized contains uppercase letters, you can perform only schema synchronization. The source PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |
| Other limits | Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the tablespace of the destination database is larger than that of the source database. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the ongoing data synchronization task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database will overwrite the data in the destination database after the failed task is resumed. |
| Special cases | If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data synchronization task. For more information, see the "Create a database" topic in the documentation of ApsaraDB RDS for MySQL. |

**SQL operations that can be synchronized**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE Important RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object to be synchronized and rename the table during data synchronization, the data of this table is not synchronized to the destination database. To prevent this situation, you can select the database to which this table belongs as the object to be synchronized when you configure the data synchronization task. Make sure that the databases to which the table belongs before and after the RENAME TABLE operation are added to the objects to be synchronized. TRUNCATE TABLE |

**Permissions required for database accounts**

| Instance type | Schema synchronization | Full data synchronization | Incremental data synchronization |
|---|---|---|---|
| PolarDB-X 2.0 | SELECT permission | SELECT permission | SELECT permission on the objects to be synchronized, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |
| ApsaraDB RDS for MySQL | Read and write permissions |   |   |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PolarDB-X 2.0** as the source database type and **MySQL** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The name of the task. DTS automatically assigns a name to the task. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. Default value:A libaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accountssyn chronize data between instances that belong to different Alibaba Cloud accounts | Specifies whether to synchronize data between instances that belong to different Alibaba Cloud accounts. Select No. Note If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source instance. |
|   | Database Account | The database account of the source instance. For information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
|   | Database Type | The type of the destination database. SelectM ySQL. |

| ta Transmissi | on Service User Guide·Data synchronizatio |   |
|---|---|---|
| Destinati on Database |   |   |
|   | Access Method | The access method of the destination database. SelectA libaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a RAM role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS instance. |
|   | Database Account | The database account of the destination instance. For information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source database. You can select Non-encrypted or SSL-encrypted based on your business requirements. If you select SSL-encrypted, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Configure the objects to be synchronized and advanced settings. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. You can select columns, tables, or databases as the objects to be synchronized. If you select tables or columns as the objects to be synchronized, DTS does not synchronize other objects such as views, triggers, or stored procedures to the destination database. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data synchronization task does not support the ETL feature. Select No. |

| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |
|---|---|

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.21 Synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance

### 2.0 instance to an AnalyticDB for PostgreSQL

**instance**

This topic describes how to use Data Transmission Service (DTS) to synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance.

**Prerequisites**

The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The destination AnalyticDB for PostgreSQL instance is created.

**Limits**

| Category | Description |
|---|---|

| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, such as remaining tables or columns, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If you perform only incremental data synchronization, the binary logs of the source database are retained for at least 24 hours. If you perform both full data synchronization and incremental data synchronization, the binary logs of the source database are retained for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. If the source database is PolarDB-X 2.0 and the name of the table to be synchronized contains uppercase letters, you can perform only schema synchronization. The source PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |
|---|---|
| Other limits | Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the tablespace of the destination database is larger than that of the source database. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the ongoing data synchronization task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database will overwrite the data in the destination database after the failed task is resumed. |

**SQL operations that can be incrementally synchronized**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE Important RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object to be migrated and rename the table during data migration, the data of this table is not migrated to the destination database. To prevent this situation, select the database to which this table belongs as the object to be migrated when you configure the data migration task. Make sure that the databases to which the table belongs before and after the RENAME TABLE operation are added to the objects to be migrated. TRUNCATE TABLE |
|---|---|

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PolarDB-X 2.0** as the source database type and **AnalyticDB for PostgreSQL** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. The value is fixed to Alibaba Cloud Instance. |

| Source Database |   |   |
|---|---|---|
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. The account must have the SELECT permission on the objects to be synchronized, the REPLICATION CLIENT permission, and the REPLICATION SLAVE permission. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The type of the destination database. Select AnalyticDB for PostgreSQL. |
|   | Access Method | The access method of the destination database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|---|---|---|
|   | Database Name | The name of the destination database in the AnalyticDB for PostgreSQL instance. |
|   | Database Account | The initial database account of the destination AnalyticDB for PostgreSQL instance or an account that has the RDS SUPERUSER permission. _ |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be synchronized and the synchronization types. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Capitalization of Object Names in Destination Instance | The capitalization of database names, table names, and column names in the destination instance. By default, DTS default policy is selected. You can select other options to make sure that the capitalization of object names is consistent with that in the source or destination database. For more information, see Specify the capitalization of object names in the destination instance. |
| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. |

| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |
|---|---|

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data synchronization task does not support the ETL feature. Select No. |
| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |

7. **Optional.** Click **Next: Configure Database and Table Fields** . Configure the tables that
you want to synchronize to the destination AnalyticDB for PostgreSQL instance.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key** **column**, and **distribution key** information for the tables that you want to synchronize to the AnalyticDB for PostgreSQL instance.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

#### 4.5.22 Synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for MySQL V3.0 cluster

### 2.0 instance to an AnalyticDB for MySQL V3.0

**cluster**

This topic describes how to synchronize data from a PolarDB-X 2.0 instance to an AnalyticDB for MySQL V3.0 cluster by using Data Transmission Service (DTS).

**Prerequisites**

The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The destination AnalyticDB for MySQL V3.0 cluster is created.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you need to edit the tables in the destination database, such as remaining tables or columns, up to 1,000 tables can be synchronized in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If you perform only incremental data synchronization, the binary logs of the source database are retained for at least 24 hours. If you perform both full data synchronization and incremental data synchronization, the binary logs of the source database are retained for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance. If the source database is PolarDB-X 2.0 and the name of the table to be synchronized contains uppercase letters, you can perform only schema synchronization. The source PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |

| Other limits | Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data synchronization is complete, the tablespace of the destination database is larger than that of the source database. DTS attempts to resume data synchronization tasks that failed within the last seven days. Before you switch workloads to the destination instance, stop or release the ongoing data synchronization task. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination instance. Otherwise, the data in the source database will overwrite the data in the destination database after the failed task is resumed. |
|---|---|

**SQL operations that can be incrementally synchronized**

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE Note When data is written to the AnalyticDB for MySQL cluster, the UPDATE statement is automatically converted to the REPLACE INTO statement. |
| DDL | CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE, ADD COLUMN, and DROP COLUMN |

**Procedure**

1. Create a data synchronization instance.

> **Note:** When you create the data synchronization instance, select **PolarDB-X 2.0** as the source database type and **AnalyticDB for MySQL V3.0** as the destination database type.

2. On the Data Synchronization page, find the data synchronization task that you created and
click **Configure Task** in the Actions column.
3. Configure the source and destination databases. The following table describes the
parameters.

| Section | Parameter | Description |
|---|---|---|

| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|---|---|---|
| Source Database | Database Type | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Method | The access method of the source database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether to migrate data across Alibaba Cloud accounts. Select No. Note If you select Yes, you must configure the Alibaba Cloud Account and RAM Role Name parameters. For more information about how to create a Resource Access Management (RAM) role and grant permissions to the role, see Configure RAM authorization for cross-account data migration or synchronization. |
|   | Instance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Database Account | The database account of the source PolarDB-X 2.0 instance. The account must have the SELECT permission on the objects to be synchronized, the REPLICATION CLIENT permission, and the REPLICATION SLAVE permission. |
| Document Version: 20 | 240522 39 |   |

|   | Database Password | The password of the database account. |
|---|---|---|
| Destination Database | Database Type | The type of the destination database. Select AnalyticDB for MySQL V3.0. |
|   | Access Method | The access method of the destination database. The value is fixed to Alibaba Cloud Instance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for MySQL V3.0 cluster. |
|   | Database Account | The initial database account of the destination AnalyticDB for MySQL V3.0 cluster or an account that has the RDS SUPERUSER permission. _ |
|   | Database Password | The password of the database account. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the objects to be synchronized and the synchronization types. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Task Stages | By default, Incremental Data Synchronization is selected. You must also select Schema Synchronization and Full Data Synchronization. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
|---|---|
| Merge Tables | If you select Yes, DTS adds the dts data source column to __ _ _ each table to store data sources. In this case, DDL operations cannot be synchronized. If you select No, DDL operations can be synchronized. By default, No is selected. Important If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. If you enable the multi-table merging feature for an incremental data synchronization task, DDL operations are not supported to be synchronized. If you perform DDL operations on the source database, data loss occurs in the destination database or the task fails. |

| Source Objects | Select one or more objects from the Source Objects section and click the icon to move the objects to the Selected Objects section. Note You can use the navigation tree to search for one or more objects. |
|---|---|
| Selected Objects | By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Rename an object to be synchronized. Note If you use the multi-table merging feature to merge source tables, you must change the table names to the names of tables to be synchronized in the destination database. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be synchronized. |

6. Click **Next: Advanced Settings** to configure advanced settings.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connections | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, an error is returned. For predictable errors, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Note If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Configure ETL | Specifies whether to enable the extract, transform, and load (ETL) feature. This data synchronization task does not support the ETL feature. Select No. |

| Whether to delete SQL operations on heartbeat tables of forward and reverse tasks | Specifies whether to write SQL operations on heartbeat tables to the source database while the DTS instance is running. Yes: does not write SQL operations on heartbeat tables. In this case, a latency of the DTS instance may be displayed. No: writes SQL operations on heartbeat tables. In this case, specific features such as physical backup and cloning of the source database may be affected. |
|---|---|

7. **Optional.** Click **Next: Configure Database and Table Fields** . Configure the tables that
you want to synchronize to the destination AnalyticDB for MySQL V3.0 cluster.

> **Note:** If you select **Schema Synchronization**, you must specify the **type**, **primary key** **column**, and **distribution key** information for the tables that you want to synchronize to the AnalyticDB for MySQL V3.0 cluster.

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the data synchronization task, a precheck is performed. You can start the data synchronization task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.

### 4.6 Manage data synchronization instances

**instances**

#### 4.6.1 Rename an object to be synchronized

By default, after an object (such as a database or table) is synchronized from the source instance to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature provided by Data Transmission Service (DTS) to rename the object in the destination instance.

**Usage notes**

You can rename an object only in the **Configure Objects and Advanced Settings** step when you configure a data synchronization task.

> **Note:** We recommend that you do not rename objects after the data synchronization task is started. Otherwise, the task may fail.

**Procedure**

> **Note:** The images in the following example are used for reference only. The actual interface may vary based on the configurations of your instance.

1. In the **Configure Objects and Advanced Settings** step, move a database or table that
you want to manage to the **Selected Objects** section, and then right-click the database or table.

> **Note:** If the source and destination databases are self-managed MySQL databases, ApsaraDB RDS for MySQL databases, or PolarDB for MySQL databases, you can specify the DDL and DML statements that you want to synchronize when you perform database name mapping or table name mapping.
> If you select different statements for database name mapping and table name mapping, the statements that are selected for table name mapping prevail.

2. In the dialog box that appears, specify a name for the object in the destination instance.
Database name or schema mapping In the **Edit Schema** dialog box, set the database name that you want to use in the destination instance. Table name mapping In the **Edit Table Name** dialog box, set the table name that you want to use in the destination instance. Column name mapping In the **Edit Table Name** dialog box, set the column names that you want to use in the destination instance. You can clear the columns that do not need to be synchronized.

> **Important:** To clear the columns that do not need to be migrated, you must clear **Synchronize All Tables**.

3. Click **OK**.
4. Configure other parameters that are required for the data synchronization task as
prompted.

#### 4.6.2 Use SQL conditions to filter data

When you select the objects to be synchronized in a data synchronization task, you can specify SQL conditions to filter data. Only the data that meets the specified conditions is synchronized to the destination database. This feature is applicable to scenarios such as regular data synchronization and table partitioning.

**Prerequisites**

A data synchronization task is being configured. The current step is **Configure Objects and**
**Advanced Settings**. For more information about how to create and configure a data
synchronization task, see configuration examples in Data Transmission Service (DTS) documentation.

**Limits**

You can filter the fields only in the current table. Cross-table filtering is not supported. If the source database is a self-managed PostgreSQL database or an ApsaraDB RDS for PostgreSQL instance, filter conditions do not take effect on incremental data.

**Procedure**

1. In the **Configure Objects and Advanced Settings** step, move the objects that you want
to synchronize to the **Selected Objects** section, and then right-click the table for which you want to configure filter conditions.
2. In the **Edit Table Name** dialog box, enter one or more SQL conditions in the **Filter**
**Conditions** field.

|   | Note An SQL condition is a standard SQL WHERE statement. The following operators are supported: = , != , < , > , and in . Only the data that meets the WHERE condition is synchronized to the destination database. In this example, orderid>100 is entered. You can specify a time condition in an SQL WHERE statement. However, you must make sure that the specified time condition is valid. For example, to filter incremental data created since 2020, you must enter create time>'2020-01- _ 01' or create time>'2020-01-01 00:00:00' . You cannot enter _ create time>'2020' . _ You can use single quotation marks (') in an SQL condition if necessary. For example, you can enter address in('hangzhou','shanghai') . Filter conditions are not case-sensitive. If a table in the source database contains Column A and Column a, you can use an SQL WHERE statement to filter only Column A. In this case, you can enter WHERE A=10 rather than WHERE a=10 . Filter statements supported by ApsaraDB for MongoDB instances are different from standard SQL WHERE statements. For example, if you want to use user ID as the filter condition, enter {" id": _ {$gt:"user100844658590795****",$lte:"user101674868045948****"}} . In this statement, gt indicates greater than and lte indicates less than. |   |
|---|---|---|
|   | 01' |   |

|   | {" id": _ |
|---|---|
| {$gt:"user100844658590795****",$lte:"user101674868045948****"}} |   |

3. Click **OK**.
4. Configure other parameters that are required for the data synchronization task as
prompted.

#### 4.6.3 Add an object to a data synchronization task

**task**

When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to add objects to a data synchronization task in the Data Transmission Service (DTS) console.

**Limits**

You can modify the objects only when a data synchronization task is in the incremental data synchronization phase and not in the Modifying Objects state.

**Start time of data synchronization**

The time when DTS synchronizes data of new objects depends on whether schema synchronization is specified for the data synchronization task. If schema synchronization is specified, DTS synchronizes the schemas of the new objects before DTS synchronizes incremental data. If schema synchronization is not specified, DTS synchronizes data after incremental data is generated on the source instance.

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Data Synchronization**.
3. On the page that appears, find the instance that you want to manage and click **Reselect**
**Objects** in the Actions column.

> **Note:** For instances that failed to run, choose
> > **Reselect Objects**.

4. In the **Available** section, click the object that you want to add, and click the
icon to move the object to the **Selected** section.
5. Click **Next: Advanced Settings**.
6. Click **Next: Precheck and Start Task** to perform the precheck.
After the task passes the precheck, the objects are added to the data synchronization task.
7. You can click **Changed. Return** to view the initial synchronization progress of the new
objects.

> **Note:** When the data synchronization task is in the **Running** state, the objects to be synchronized are modified and the instance is running as expected.

#### 4.6.4 Remove an object from a data synchronization task

**synchronization task**

When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to remove objects from a data synchronization task in the Data Transmission Service (DTS) console.

**Limits**

You can modify the objects only when a data synchronization task is in the incremental data synchronization phase and not in the Modifying Objects state.

**Procedure**

1. Log on to the DTS console.
2. In the left-side navigation pane, click **Data Synchronization**.
3. On the page that appears, find the instance that you want to manage and click **Reselect**
**Objects** in the Actions column.

> **Note:** For instances that failed to run, choose
> > **Reselect Objects**.

4. In the **Selected Objects** section, click the object that you want to remove, and click the
icon to move the object to the **Source Objects** section.
5. Click **Next: Advanced Settings**.
6. Click **Next: Precheck and Start Task** to perform the precheck.
After the task passes the precheck, the objects are removed from the data synchronization task.
7. You can click **Changed. Return** to view the initial synchronization progress of the new
objects.

> **Note:** When the data synchronization task is in the **Running** state, the objects to be synchronized are modified and the instance is running as expected.

#### 4.6.5 Specify the capitalization of object names in the destination instance

**names in the destination instance**

When you configure a data migration or synchronization task, you can specify the capitalization of database names, table names, and column names in the destination instance.

**Capitalization policies**

Data Transmission Service (DTS) supports the following capitalization policies for object names: DTS default policy DTS configures the capitalization of database names, table names, and column names in the destination instance based on the database type and related parameters, such as the `lower_case_table_names` parameter.

| Destination database type | Destination database parameter | Capitalization of object names in the destination instance |
|---|---|---|
| Self-managed MySQL database or ApsaraDB RDS for MySQL PolarDB-X AnalyticDB for MySQL V3.0 | The lower case table names _ _ _ parameter is set to 1 or 2. | Database names and table names in the destination instance are in lowercase. The capitalization of column names in the destination instance is the same as that in the source instance. |
|   | The lower case table names _ _ _ parameter is set to 0. | The capitalization of database names, table names, and column names in the destination instance is the same as that in the source instance. |
| AnalyticDB for MySQL V2.0 DataHub MaxCompute | N/A | Database names, table names, and column names in the destination instance are in lowercase. |
| Self-managed Oracle database | N/A | Database names, table names, and column names in the destination instance are in uppercase. |

| Self-managed SQL Server database or ApsaraDB RDS for SQL Server PolarDB for PostgreSQL (Compatible with Oracle) Self-managed PostgreSQL database or ApsaraDB RDS for PostgreSQL AnalyticDB for PostgreSQL Self-managed MongoDB database or ApsaraDB for MongoDB Self-managed Redis database or ApsaraDB for Redis | N/A | Database names and table names in the destination instance are in lowercase. The capitalization of column names in the destination instance is the same as that in the source instance. |
|---|---|---|

Consistent with the source database The capitalization of database names, table names, and column names in the destination instance is the same as that in the source instance. Consistent with the default policy of the destination database (uppercase) The names of all the databases, tables, and columns that are migrated or synchronized to the destination instance are in uppercase. Consistent with the default policy of the destination database (lowercase) The names of all the databases, tables, and columns that are migrated or synchronized to the destination instance are in lowercase.

#### 4.6.6 Troubleshoot precheck failures

Before Data Transmission Service (DTS) runs a data synchronization task, DTS performs a precheck. This topic describes the precheck items and how to troubleshoot precheck failures.

**Source database connectivity**

DTS checks whether DTS servers can connect to the source RDS instance. DTS creates a connection to the source RDS instance by using the Java Database Connectivity (JDBC) protocol. If the connection fails, the task fails to pass this precheck item. Cause of failure DTS does not support data synchronization between RDS instances in the region in which the source instance resides. The database account or password of the source instance is invalid. Solution Contact Alibaba Cloud technical support.

**Destination database connectivity**

DTS checks whether DTS servers can connect to the destination RDS instance. DTS creates a connection to the destination RDS instance by using the JDBC protocol. If the connection fails, the task fails to pass this precheck item. Cause of failure DTS does not support data synchronization between RDS instances in the region in which the destination instance resides. The database account or password of the destination instance is invalid. Solution Submit a ticket and contact Alibaba Cloud technical support.

**Source database version**

DTS checks whether: i. The database version of the source RDS instance is supported by the data synchronization feature. ii. The database version of the destination RDS instance is the same as the database version of the source RDS instance. Cause of failure The database version of the source RDS instance is earlier than the database versions that are supported by DTS. For example, the data synchronization feature supports the following database versions: MySQL 5.1, 5.5, 5.6, and 5.7. The database version of the destination RDS instance is earlier than the database version of the source RDS instance. Solution If the database version of the source RDS instance is earlier than the database versions that are supported by DTS, update the source RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again. If the database version of the destination RDS instance is earlier than the database version of the source RDS instance, update the destination RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again.

**Database existence**

DTS checks whether the destination database already exists in the destination instance. If the destination database does not exist in the destination instance, DTS automatically creates a database. However, DTS fails to create the database and reports a failure under the following circumstances: The database name contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). The character set of the database is not UTF-8, GBK, Latin1, or UTF-8MB4. The account of the destination database does not have the read and write permissions on the destination database. If the data source is an RDS instance, the task passes this precheck item.

**Source database permissions**

DTS checks whether the account of the source database has the required permissions. If the account does not have the required permissions, the task fails to pass this precheck item. If the data source is an RDS instance, the task passes this precheck item.

**Destination database permissions**

DTS checks whether the account of the destination database has the required permissions. If the account does not have the required permissions, the task fails to pass this precheck item. Cause of failure DTS fails to create a database account in the destination RDS instance. DTS fails to grant the read and write permissions to the database account of the destination RDS instance. Solution Submit a ticket and contact Alibaba Cloud technical support.

**Object name conflict**

DTS checks object names only if you select initial synchronization for a data synchronization task. DTS checks whether an object that you want to synchronize has the same name as an object in the destination RDS instance. Cause of failure If an object in the destination RDS instance has the same name as the object that you want to synchronize, the task fails to pass this precheck item. Solution Delete the conflicting object from the destination database. After the conflicting object is deleted, create a data synchronization task again. Select both Initial Schema Synchronization and Initial Full Data Synchronization.

**Value of server_id in the source database**

DTS checks whether the value of the server_id parameter in the source database is set to an integer that is greater than or equal to 2. If the data source is an RDS instance, the task passes this precheck item.

**Whether binary logging is enabled for the source database**

DTS checks whether the binary logging feature is enabled for the source database. If the binary logging feature is disabled for the source database, the task fails to pass this precheck item. If the data source is an RDS instance, the task passes this precheck item.

**Whether the binary log format is ROW in the source database**

DTS checks whether the binary log format of the source database is set to ROW. If the binary log format of the source database is not set to ROW, the task fails to pass this precheck item. If the data source is an RDS instance, the task passes this precheck item.

**Integrity of the FOREIGN KEY constraints**

DTS checks whether the parent tables and child tables that have referential relationships with each other are all included in the objects to be synchronized. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. Cause of failure One or more child tables are included in the objects to be synchronized. However, the parent tables that are referenced by the child tables are not included in the objects to be synchronized. This impairs the integrity of the FOREIGN KEY constraints. Solution The following solutions are available: Create a data synchronization task again and do not synchronize the child tables that fail to pass this precheck item. Create a data synchronization task again and add the parent tables to the objects to be synchronized. Remove the FOREIGN KEY constraints from the child tables that fail to pass this precheck item. Then, create a data synchronization task again.

**Storage engine**

DTS checks whether the objects to be synchronized use the storage engines that are not supported by the data synchronization feature, such as FEDERATED, MRG_MyISAM, and TokuDB. Cause of failure If the storage engine of a source table is FEDERATED, MRG_MyISAM, or TokuDB, the task fails to pass this precheck item. Solution Change the unsupported storage engine to InnoDB and create a data synchronization task again.

**Character set**

DTS checks whether the objects to be synchronized use the character sets that are not supported by the data synchronization feature, such as the UCS-2 character set. Cause of failure If the character sets used by the objects to be synchronized are not supported by the data synchronization feature, the task fails to pass this precheck item. Solution Change the unsupported character sets to UTF-8, GBK, or Latin1. Then, create a data synchronization task again.

**Complex topologies**

DTS checks whether the topology that you specify for the source and destination RDS instances is supported. Cause of failure The source RDS instance in the current task is being used as the destination instance of another task. The destination RDS instance in the current task is being used as the source or destination instance of another task. The objects that you want to synchronize in the current task are being synchronized by an existing task. The two tasks have the same source and destination RDS instances. Solution If the task that you want to create has the same source and destination RDS instances as an existing task, you can add the objects that you want to synchronize to the existing task. You do not need to create another task to synchronize these objects. If the task that you want to create conflicts with an existing task, wait until the existing task is complete before you create a data synchronization task again.

**Format of the MySQL database password**

DTS checks whether the format of the password that is used to access the source database is no longer valid. If the data source is an RDS instance, the task passes this precheck item.

#### 4.6.7 Configure ETL in a data synchronization task

**task**

Data Transmission Service (DTS) provides the extract, transform, and load (ETL) feature to help you process streaming data in real time. In combination with the efficient data replication capabilities of DTS, ETL can be used to extract, transform, process, and load streaming data. You can use these features to filter data, mask data, record the modification time of data, and audit data changes. This topic describes how to configure ETL in a data synchronization task.

**Background information**

DTS is used for data migration and real-time data transmission between data sources. In some cases, you may need to transform or filter real-time data before the data is written to a database. To meet such requirements, DTS provides the ETL feature and allows you to use domain-specific language (DSL) statements to process data in a flexible manner. For more information about DSL, see Overview of DSL.

**Supported databases**

The following table describes the source and destination databases that are supported by the ETL feature.

| Source database | Destination database |
|---|---|
| MySQL | AnalyticDB for MySQL V3.0 AnalyticDB for PostgreSQL MaxCompute MySQL |
| Self-managed Oracle database | AnalyticDB for PostgreSQL DataHub MaxCompute |
| PolarDB-X 1.0 | MySQL AnalyticDB for MySQL V3.0 PolarDB-X 1.0 MaxCompute |
| Self-managed Db2 for LUW database | AnalyticDB for PostgreSQL |
| MongoDB | MongoDB |
| PostgreSQL | PostgreSQL |

**Configure ETL when you create a data synchronization task**

**Usage notes**

If the ETL script that you configure contains the operation to add a column, you must manually add a column to the destination table. Otherwise, the ETL script does not take effect. For example, if you configure the ETL script script:e_set(`new_column`, dt_now()) , you must manually add the `new_column` column to the destination table.
1. Create a data synchronization task based on your business requirements. Configure the
task and go to the **Advanced Settings** step.
2. Set the **Configure ETL** parameter to **Yes**. In the code editor, enter data processing
statements based on the DSL syntax.

> **Note:** If you want to drop entries whose values of the id column are greater than 3 by using DSL, you can use the script:e_if(op_gt(`id`, 3), e_drop()) statement. In this statement, `op_gt` is an expression function used to determine whether an entry is greater than a specific value. `id` is a variable. This way, entries whose values of the id column are greater than 3 are filtered out.

3. Click **Next: Precheck and Start Task** and complete the subsequent steps.

**Overview of DSL**

DSL is a scripting language that is designed to process data in data synchronization scenarios. You can use conditional functions to process data of the string, date, and numeric types. DSL boasts the following characteristics that help you process data in a flexible manner: Various functions: DSL provides a variety of functions and supports combined functions. Simple syntax: DSL is easy to use. For more information about how to use DSL to filter, transform, and mask data, see Typical scenarios. High efficiency: DSL has a minimal effect on the data synchronization performance because DSL uses the code generation mechanism.

**Typical scenarios**

Filter data Filter out data by a numeric column: If an entry whose value of the id column is greater than 10000, drop this entry so that it is not synchronized to the destination database. Example: e_if(op_gt(`id`, 10000), e_drop). Filter out data by a specific string: If an entry whose value of the name column contains "hangzhou", drop this entry so that it is not synchronized to the destination database. Example: e_if(str_contains(`name`, "hangzhou"), e_drop). Filter out data by date: If an entry whose timestamp of the order column is earlier than a specific point in time, drop this entry so that it is not synchronized to the destination database. Example: e_if(op_lt(`order_timestamp`, "2015-02-23 23:54:55"), e_drop). Filter out data by multiple conditions: If an entry whose value of the id column is greater than 1000 and value of the name column contains "hangzhou", drop this entry so that it is not synchronized to the destination database. Example: e_if(op_and(str_contains(`name`, "hangzhou"), op_gt(`id`, 1000)), e_drop()). If an entry whose value of the id column is greater than 1000 or value of the name column contains "hangzhou", drop this entry so that it is not synchronized to the destination database. Example: e_if(op_or(str_contains(`name`, "hangzhou"), op_gt(`id`, 1000)), e_drop()). Mask data Mask the last four digits of a mobile phone number with four asterisks (*). Example: e_set(`phone`, str_mask(`phone`, 7, 10, '*')). Record the time when data is modified Add a column to all tables: If the value of the __OPERATION__ variable is INSERT, UPDATE, or DELETE, a column named dts_sync_time whose value is the same as the __COMMIT_TIMESTAMP__ variable of logs is added to all tables in the source database.

```
e_if(op_or(op_or(
        op_eq(__OPERATION__, __OP_INSERT__),
        op_eq(__OPERATION__, __OP_UPDATE__)),
        op_eq(__OPERATION__, __OP_DELETE__)),
    e_set(dts_sync_time, __COMMIT_TIMESTAMP__))
```

Add a column to a specific table: If the value of the __OPERATION__ variable is INSERT, UPDATE, or DELETE, a column named dts_sync_time whose value is the same as the __COMMIT_TIMESTAMP__ variable of logs is added to the dts_test_table table in the source database.

```
e_if(op_and(
      op_eq(__TB__,'dts_test_table'),
      op_or(op_or(
        op_eq(__OPERATION__,__OP_INSERT__),
        op_eq(__OPERATION__,__OP_UPDATE__)),
        op_eq(__OPERATION__,__OP_DELETE__))),
      e_set(dts_sync_time,__COMMIT_TIMESTAMP__))
```

> **Note:** To perform the preceding operations, you must add the dts_sync_time column to the corresponding tables in the destination database before the data synchronization task is started.

Audit data changes Record the type and time of the data changes in tables: 1. Record the data change type in the operation_type column of the destination database. 2. Record the time when data is changed in the updated column of the destination database.

```
e_compose(
    e_switch(
        op_eq(__OPERATION__,__OP_DELETE__), e_set(operation_type, 'DELETE'),
        op_eq(__OPERATION__,__OP_UPDATE__), e_set(operation_type, 'UPDATE'),
        op_eq(__OPERATION__,__OP_INSERT__), e_set(operation_type, 'INSERT')),
    e_set(updated, __COMMIT_TIMESTAMP__),
    e_set(__OPERATION__,__OP_INSERT__)
```

`)`

> **Note:** You must add the operation_type and updated columns to the tables in the destination database before the data synchronization task is started.

**DSL syntax**

**Constants and variables**

Constants

| Data type | Example |
|---|---|
| INT | 123 |
| FLOAT | 123.4 |
| STRING | "hello1 world" _ |
| BOOLEAN | true or false |
| DATETIME | '2021-01-01 10:10:01' |

Variables

| Variable | Description | Data type | Example |
|---|---|---|---|
| TB __ __ | The name of the table. | STRING | table |
| DB __ __ | The name of the database. | STRING | mydb |
| OPERATION __ __ | The type of the operation. | STRING | OP INSERT , OP __ _ ____ _ UPDATE , OP DELE ____ _ TE __ |
| COMMIT TIMESTAM __ _ P __ | The time when the transaction was committed. | DATETIME | '2021-01-01 10:10:01' |
| `column` | The name of the column. | STRING | `id` or `name` |

**Expression functions**

Arithmetic operators

| Operati on | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|
| Addition | op sum( _ value1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op sum(`col1`, 1.0) _ |
| Subtracti on | op sub(v _ alue1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op sub(`col1`, 1.0) _ |
| Multiplic ation | op mul(v _ alue1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op mul(`col1`, 1.0) _ |
| Division | op div tr _ _ ue(value 1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op div true(`col1`, _ _ 2.0). In this example, if the col1 value is 15, 7.5 is returned. |
| Modulo | op mod( _ value1, value2) | value1: an integer or a floating-point number value2: an integer or a floating-point number | If value1 and value2 are integers, an integer is returned. Otherwise, a floating- point number is returned. | op mod(`col1`, 10). In _ this example, if the col1 value is 23, 3 is returned. |

Logical operators

| Operati on | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|
| Equal to | op eq(va _ lue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false | op eq(`col1`, 23) _ |

| Greater than | op gt(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false | op gt(`col1`, 1.0) _ |
|---|---|---|---|---|
| Less than | op lt(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false | op lt(`col1`, 1.0) _ |
| Greater than or equal to | op ge(va _ lue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false | op ge(`col1`, 1.0) _ |
| Less than or equal to | op le(val _ ue1, value2) | value1: an integer, a floating-point number, or a string value2: an integer, a floating-point number, or a string | true or false | op le(`col1`, 1.0) _ |
| AND | op and(v _ alue1, value2) | value1: a Boolean value value2: a Boolean value | true or false | op and(`is male`, _ _ `is student`) _ |
| OR | op or(val _ ue1, value2) | value1: a Boolean value value2: a Boolean value | true or false | op or(`is male`, _ _ `is student`) _ |

**String functions**

| Purpose | Syntax | Valid value | Return value | Example |
|---|---|---|---|---|

| Format strings and append strings | str form _ at(format , value1, value2, value3, ...) | format: a string. Braces ({}) are used as placeholders. Example: "part1: {}, part2: {}". value1: an arbitrary value. value2: an arbitrary value. | The string after the format operation. | str format("part1: {}, _ part2: {}", `col1`, `col2`). In this example, if the col1 value is ab and the col2 value is 12, "part1: ab, part2: 12" is returned. |
|---|---|---|---|---|
| Replace strings | str repla _ ce(origin al, oldStr, newStr, count) | original: the original string. oldStr: the string to be replaced. newStr: the string after the replacement. count: an integer that indicates the maximum number of times that a string can be replaced. A value of -1 indicates that all oldStr is replaced with newStr. | The string after the replace operation. | Example 1: str replace(`name`, _ "a", 'b', 1). In this example, if the name is aba, bba is returned. Example 2: str replace(`name`, _ "a", 'b', -1). In this example, if the name is aba, bbb is returned. |
| Remove specific characte rs at the start and end of a string | str strip( _ string va _ l, charSet) | string val: the _ original string. char set: the set of _ the first characters and the last characters of the string. | The string after the remove operation. | str strip(`name`, _ 'ab'). In this example, if the name is axbzb, xbz is returned. |
| Convert strings to lowercas e letters | str lower _ (value1) | value1: a column of the string type or a string constant. | The string after the convert operation. | str lower(`str col`) _ _ |
| Convert strings to uppercas e letters | str upper _ (value1) | value1: a column of the string type or a string constant. | The string after the convert operation. | str upper(`str col`) _ _ |
| Count strings | str count _ (str, pattern) | str: a column of the string type or a string constant. pattern: the substring to query. | The number of times for which the substring appears. | str count(`str col`, _ _ 'abc'). In this example, if the str col _ value is zabcyabcz, 2 is returned. |

| Query strings | str find(s _ tr, pattern) | str: a column of the string type or a string constant. pattern: the substring to query. | The position in which the substring matches for the first time. If no match is found, -1 is returned. | str find(`str col`, _ _ 'abc'). In this example, if the str col _ value is xabcy, 1 is returned. |
|---|---|---|---|---|
| Determin e whether a string contains only letters | str isalp _ ha(str) | str: a column of the string type or a string constant. | true or false | str isalpha(`str col`) _ _ |
| Determin e whether a string contains only digits | str isdigi _ t(str) | str: a column of the string type or a string constant. | true or false | str isdigit(`str col`) _ _ |
| Mask part of a string with specific characte rs. This operatio n can be used for data masking. For example, mask the last four digits of a mobile phone number with four asterisks (*). | str mask _ (str, start, end, maskStr) | str: a column of the string type or a string constant. start: an integer that indicates the start position of the masking. The minimum value is 0. end: an integer that indicates the end position of the masking. The maximum value is the length of the string minus 1. maskStr: a string. The length is 1. Example: #. | The string whose part from start to end is masked with specified characters. | str mask(`phone`, 7, _ 10, '#') |
| Query the DateTim e value of the current time zone | dt now() _ | None | The DateTime value of the current time zone. | e set(`dt col`, _ _ dt now()) _ |

| Query the DateTim e value of the current time zone in UTC | dt utcno _ w() | None | The DateTime value of the current time zone in UTC. | e set(`dt col`, _ _ dt utcnow()) _ |
|---|---|---|---|---|

**Global functions**

Flow control functions

| Purpose | Syntax | Description | Example |
|---|---|---|---|
| The IF statement | e if(bool exp _ _ r, func invoke) _ | bool expr: a Boolean _ constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke: a function. _ Valid values: e drop, _ e keep, e set, e if, and _ _ _ e compose. _ | e if(op gt(`id`, 10), e drop()). _ _ _ In this example, if an entry whose value of the id column is greater than 10, this entry is dropped. |
| The IF ELSE statement | e if else(bool _ _ expr, _ func invoke1 _ , func invoke2 _ ) | bool expr: a Boolean _ constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke1: a function. _ Invoke this function if the condition is true. func invoke2: a function. _ Invoke this function if the condition is false. | e if else(op gt(`id`, 10), _ _ _ e set(`tag`, 'large'), _ e set(`tag`, 'small')). In this _ example, if an entry whose value of the id column is greater than 10, the tag column is set to large. Otherwise, the tag column is set to small. |
| The SWITCH statement that contains multiple conditions and a default operation | s switch(con _ dition1, func1, condition2, func2, ..., default = default func) _ | condition1: a Boolean constant or a function. A Boolean constant: true or false. A function: op gt(`id`, _ 10). func invoke: a function. If _ condition1 is true, invoke this function and finish the statement. Otherwise, proceed to the next condition. default func: a function. If _ the preceding conditions are false, invoke this function. | e switch(op gt(`id`, 100), _ _ e set(`str col`, '>100'), _ _ op gt(`id`, 90), e set(`str col`, _ _ _ '>90'), default=e set(`str col`, _ _ '<=90')) |
| Combine multiple operations | e compose(f _ unc1, func2, func3, ...) | func1: a function. Valid values: e set, e drop, and _ _ e if. _ func2: a function. Valid values: e set, e drop, and _ _ e if. _ | e compose(e set(`str col`, _ _ _ 'test'), e set(`dt col`, _ _ dt now())). In this example, the _ value of the str col column is _ set to test, and the value of the dt col column is set to the _ current time. |

Data manipulation functions

| Purpose | Syntax | Description | Example |
|---|---|---|---|
| Drop this entry so that it is not synchronized to the destination database | e drop() _ | None | e if(op gt(`id`, 10), e drop()). _ _ _ In this example, entries whose values of the id column are greater than 10 are dropped. |
| Retain this entry so that it is synchronized to the destination database | e keep(condi _ tion) | condition: a Boolean expression. | e keep(op gt(id, 1)). In this _ _ example, only entries whose values of the id column are greater than 1 are synchronized. |
| Set the value of a column | e set(`col`, _ val) | col: the name of the column. val: a constant or a function. The data type of the val value must match the data type of the col value. | e set(`dt col`, dt now()). In _ _ _ this example, the value of the dt col column is set to _ the current time. e set(`col1`, `col2` + 1). In _ this example, the value of the col1 column is set to the value of the col2 column plus 1. |

### 4.7 Best practices for data synchronization from PolarDB-X instances

**synchronization from PolarDB-X**

**instances**

#### 4.7.1 Precautions and limits for synchronizing data between PolarDB-X instances

**synchronizing data between PolarDB-X**

**instances**

PolarDB-X does not provide binary logs. To ensure data quality, we recommend that you take note of the limits when you perform business design, business development, and O&M changes.

**Overview**

Limits on the business design Limits on the database architecture Limits on O&M changes Potential risks on data quality Suggestions to ensure data quality

**Limits on the business design**

All tables must have primary keys. Otherwise, data inconsistency may occur in data synchronization because the destination database may contain duplicate data records. We recommend that you do not use the global secondary indexes (GSIs) of PolarDB-X because they are updated asynchronously. If you use GSIs, Data Transmission Service (DTS) can ensure only the eventual consistency of data. The databases that you want to synchronize cannot be deployed in mixed mode. The mixed mode refers to a mode in which both the unit mode and the copy mode are used.

> **Note:** In unit mode, users perform read and write operations in their respective unit nodes. Two-way synchronization is implemented between the databases in each unit node and those in the central node. In copy mode, users write data to the databases in the central node. The data is then synchronized to the databases in each unit node.

If you configure two-way synchronization between PolarDB-X instances and use underlying MySQL databases, fields of the FLOAT or DOUBLE type are not supported in business tables. If the business tables have fields of the FLOAT or DOUBLE type, convert the field type to DECIMAL. If you configure one-way synchronization between PolarDB-X instances, fields of the FLOAT or DOUBLE type are supported in business tables. DTS does not allow you to synchronize objects such as stored procedures, triggers, functions, views, and events in data synchronization between PolarDB-X instances. DTS does not support initial schema synchronization between PolarDB-X instances. You must manually create objects such as databases and tables in the destination database. Make sure that the available storage capacities in PolarDB-X instances are sufficient for business expansion.

**Limits on the database architecture**

An ApsaraDB RDS for MySQL instance that is attached to a PolarDB-X instance cannot be attached to another PolarDB-X instance. The ApsaraDB RDS for MySQL instances attached to the source PolarDB-X instance must have the same specifications as those attached to the destination PolarDB-X instance. For example, if the source PolarDB-X instance has four ApsaraDB RDS for MySQL instances, the destination PolarDB-X instance must have four ApsaraDB RDS for MySQL instances whose specifications are the same as those in the source PolarDB-X instance. The sharding rule of the source PolarDB-X instance must be the same as that of the destination PolarDB-X instance. Otherwise, no data synchronization task can be created. You can synchronize only business tables between Polar-X instances. You cannot synchronize metadata tables or system tables between PolarDB-X instances.

**Limits on O&M changes**

| Change type | Description | Impact and solution |
|---|---|---|
| PolarDB-X instances | Change a sharding rule. For example, change the shard key of a database or table, or change the number of shards. | Not supported. You must perform the following steps to recreate a data synchronization task: 1. Stop and delete the original data synchronization task. 2. Wait until the changes are complete in the source database. Then, clear the data that has been synchronized to the destination database. 3. Configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. |
|   | Change the number of instances at the storage layer. For example, scale out instances or migrate frequently-accessed tables. |   |

| Storage | Change the specifications of instances and switch workloads at the storage layer. | Data synchronization is not affected. |
|---|---|---|
|   | Change parameter settings. | The parameter settings of the source and destination databases must be the same. To change the parameter settings of instances at the storage layer, you must make sure that new parameters do not affect previous parameters. Note If you are not sure about the impact of changing parameter settings, you can contact technical support of Database Expert Service. |
|   | Change backup and recovery policies, and enable auditing and diagnostics for instances at the storage layer. | The change takes effect only on the current instance and does not affect other instances with replication relationships. |
| DTS tasks | Perform DDL operations. | If you configure data synchronization tasks for ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance, the tasks may be delayed after you perform DDL operations. This is caused by the implementation logic of MySQL. |
| DDL operations at the database or table level | Add tables. | Not supported. You must perform the following steps: 1. After you perform DDL operations to create tables in the destination database, perform the same DDL operations to create tables in the source database. 2. Add the new tables to the objects of the data synchronization task. You can write data to the source database only after the preceding operations are complete. If you select tables as the objects of the data synchronization task, you must add the new tables to the synchronization queues on the source and destination instances at the storage layer. |
|   | Add fields, add secondary indexes, delete indexes, and modify indexes (except for replacing secondary indexes with unique indexes). | If you configure a data synchronization task for a PolarDB-X instance, you must perform DDL operations in the destination database, and then perform the same DDL operations in the source database. If you configure data synchronization tasks for ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance, DTS automatically synchronizes the operations that you perform. The following operations can be synchronized: Add fields, add secondary indexes, delete indexes, and modify indexes (except for replacing secondary indexes with unique indexes). |
| > Document Version | : 20240522 42 |   |

|   | Perform other DDL operations. | Only the preceding DDL operations are supported. |
|---|---|---|
| Switchover Note Switchover: After you use DTS to | Perform a switchover. | Before you perform a switchover, make sure that the DTS task is not delayed. Otherwise, data quality issues occur. |
|   | Perform a failover that meets the requirements of recovery point objective (RPO). Note RPO represents the maximum amount of data that can be lost after a recovery from a failure. RPO is measured by time. Warning Failover: If the source instance or the data center where the source instance resides fails, you can switch workloads to a backup system. A failover is a lossy operation. | If a failure such as a network interruption, an equipment failure, or a data center failure occurs and the data synchronization task is delayed, you may need to perform a failover. In this case, if the difference between the time when the last data entry is synchronized to the destination database and the time when the failure occurs is less than the RPO, you can perform a failover to recover your business. For example, if the RPO is 5 minutes, the quality of the data within the 5 minutes cannot be ensured after you perform a failover. You may need to revise the data to ensure consistency. Note To query the time when the last data entry is synchronized to the destination database, refer to the documentation about task management. |
| migrate or synchronize data from the source database to the destination database, you switch workloads from the source database to the destination database. |   |   |
|   | Perform a failover that does not meet the requirements of RPO. | The data synchronization task may be delayed due to the following causes: A large number of DDL operations are performed in the source database, a network failure occurs, and the performance of the destination database is unfavorable. In this case, if the data center fails and the difference between the time when the last data entry is synchronized to the destination database and the time when the failure occurs is greater than the RPO, we recommend that you wait until the data center recovers before you perform a failover. For example, if the RPO is 5 minutes, the quality of the data within the 5 minutes cannot be ensured after you perform a failover. You may need to revise the data to ensure consistency. |

**Potential risks on data quality**

Some changes or switchover operations may cause data quality issues such as schema inconsistency between the source and destination databases. If data latency occurs between the primary and secondary databases of the source instance, the data written to the primary database is not updated to the secondary database at the earliest opportunity. In this case, if you perform a primary/secondary switchover in the source instance, DTS uses the secondary database of the source instance as the source database for data synchronization. As a result, the data that is not updated to the secondary database is lost. If the DTS task is resumed from a network failure after you perform a switchover, DTS attempts to synchronize the data generated before the failure occurs. This mechanism prevents data loss in the destination database. In this case, if the destination tables do not have primary keys, data will be inconsistent between the source and destination databases. If the destination tables have primary keys, data may not be consistent when DTS implements the retry mechanism, but data will remain consistent after the retry ends. The data synchronization task may be delayed due to network failures and DDL operations. The data synchronization task may be delayed or interrupted due to changes to the source database, unfavorable performance of the destination database, and schema inconsistency. Alibaba Cloud cannot solve the preceding issues. You must recreate a DTS task or adjust the source and destination databases.

**Suggestions to ensure data quality**

You must perform all DDL operations with caution. All DDL operations must be confirmed by the technical engineers to comply with the preceding limits. Do not directly perform DDL operations in your program code.

#### 4.7.2 Solutions of data synchronization from a PolarDB-X instance

**a PolarDB-X instance**

Data Transmission Service (DTS) supports data synchronization from a source PolarDB-X instance to a destination instance. However, if more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, we recommend that you do not directly configure a data synchronization task for the source PolarDB-X instance. If you do so, you may encounter a performance bottleneck or stability risks. This may affect your business. To ensure good performance and high stability of data synchronization, we recommend that you configure a data synchronization task for each ApsaraDB RDS for MySQL instance attached to the source PolarDB-X instance.

**Prerequisites**

You have read the Precautions and limits for synchronizing data between PolarDB-X instances topic and understood the relevant conventions and precautions.

**Synchronization solutions**

| Soluti on | Configuration | Description |
|---|---|---|
| Solutio n 1 | You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. You must map the names of databases and tables in the ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination instance. Compared with Solution 2, this solution ensures good performance and high stability of data synchronization. Important If you use this solution, you can select only tables as the objects to be synchronized. | If you require better performance and higher stability, we recommend that you use this solution. This solution has no limits on the number of ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance. |

| Solutio n 2 | You can directly configure a data synchronization task for the source PolarDB-X instance. If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, the performance and stability of data synchronization may deteriorate to the extent that your business may be affected. | If you use this solution, make sure that no more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance. Otherwise, the performance and stability of data synchronization may deteriorate. |
|---|---|---|

**Comparison between the two solutions**

| Comparison item | Solution 1 | Solution 2 |
|---|---|---|
| Performance | This solution requires you to configure multiple data synchronization tasks. This way, this solution multiplies the performance of data synchronization and ensures the feasibility of writing a large amount of data from a PolarDB-X instance. | This solution supports only one data synchronization task for the source PolarDB-X instance. If a large amount of data is written to the source PolarDB-X instance by the business side, a performance bottleneck may occur during data synchronization. |
| Stability | This solution ensures high stability. If a data synchronization task that you configure for one of the ApsaraDB RDS for MySQL instances fails, data synchronization tasks for other ApsaraDB RDS for MySQL instances are not affected. You need to only recover the failed data synchronization task. | This solution provides medium stability. If the data synchronization task for the source PolarDB-X instance fails, data synchronization fails. |
| Ease of use | You must configure multiple data synchronization tasks. This complicates the configuration process. You must configure database and table name mapping for each task. You must map the names of databases and tables in the ApsaraDB RDS for MySQL instances to the names of the databases and tables in the destination instance. | You need to only configure one data synchronization task. This simplifies the configuration process. |
| Resource usage | This solution requires multiple data synchronization instances. | This solution requires only one data synchronization instance. |

**Synchronization of DDL operations**

In most cases, data synchronization from a source PolarDB-X instance does not support the synchronization of DDL operations. If you synchronize DDL operations during a data synchronization task, data may fail to be written to the destination instance. To prevent this problem, you can take one of the following measures:
1. Release the data synchronization task.
2. Clear the destination database.
3. Reconfigure the data synchronization task.
However, in a few cases, you can synchronize DDL operations during data synchronization from a source PolarDB-X instance. The following table describes the details of these cases.

| Case | Supported operation |
|---|---|
| You use Solution 1 and select tables as the objects to be synchronized. | You can add tables to the objects that you select for the data synchronization task. You can also add columns to or remove columns from the objects. However, you can perform these operations only during data synchronization between PolarDB-X instances. To do this, perform the following steps: i. Add columns to or remove columns from the objects that you select for the data synchronization task. ii. Add or remove columns in the destination database, and then perform the same operations in the source database. When DTS detects that a column already exists in the destination database, DTS ignores the error and does not display a write failure. |
| You use Solution 2 and select entire databases as the objects to be synchronized. | You can only add tables to the objects. To do this, you must add tables in the destination database, and then perform the same operations in the source database. You cannot add or remove columns. Warning If you add a column to the database of the source PolarDB-X instance, some physical tables at the underlying layer may contain the column, whereas some physical tables do not contain the column. When DTS executes the assembled SQL statement, DTS may fail to find the column or lose the data in the column. |
| You use Solution 2 and do not select entire databases as the objects to be synchronized. | You can only add tables to the objects. To do this, perform the following steps: i. Add tables to the objects that you select for the data synchronization task. ii. Add tables in the destination database, and then perform the same operations in the source database. You cannot add or remove columns. |

## 5 Change tracking

### 5.1 Overview

You can use Data Transmission Service (DTS) to track data changes from MySQL instances in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations.

**Supported database services**

Self-managed MySQL databases or ApsaraDB RDS for MySQL instances PolarDB-X (formerly known as DRDS) instances Self-managed Oracle databases

**Limits**

By default, the change tracking feature of the previous version is no longer available. The newly created change tracking tasks are of the new version. To run change tracking tasks of the previous version, you must reconfigure the objects for change tracking in the DTS console. Otherwise, the service level agreement (SLA) of DTS does not guarantee service reliability or performance.

**Change tracking objects**

The objects for change tracking include tables and databases. In change tracking, data changes include DML and DDL operations. When you configure a change tracking task, you can select the operation type.

**Change tracking tasks**

A change tracking task is the basic unit of change tracking and data consumption. To track data changes from an RDS instance, you must create a change tracking task in the DTS console for the RDS instance. The change tracking task pulls data changes from the RDS instance in real time and locally stores the data changes. You can use the DTS SDK to consume the tracked data. You can also create, manage, or delete change tracking tasks in the DTS console.

### 5.2 Create a change tracking instance

**instance**

Before you configure a task to track data changes, you must create a change tracking instance. This topic describes how to create a change tracking instance in the Data Transmission Service (DTS) console.

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Change Tracking**.
3. Click **Create Task**.
4. In the panel that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|

| Source Database Type | The type of the source database. |
|---|---|
| Source Region | The region in which the source database resides. Note You cannot change the value of this parameter after you purchase the change tracking instance. Exercise caution when you configure this parameter. |
| Quantity | The number of change tracking instances that you want to create at a time. |

> **Note:** In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click **Create**.
6. In the message that appears, click **OK**.

### 5.3 Configure change tracking tasks

**tasks**

#### 5.3.1 Track data changes from an ApsaraDB RDS for MySQL instance

**RDS for MySQL instance**

Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from an ApsaraDB RDS for MySQL instance.

**Prerequisites**

The database version is 5.6, 5.7, or 8.0.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck, and the change tracking task cannot be started. A read-only instance or temporary instance cannot be used as the source instance for change tracking. |

| Other limits | Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt-online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |
|---|---|

**Procedure**

1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click **Configure Channel** in the
Actions column.
3. Configure the source database and network type.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select MySQL. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source instance resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether data is replicated across multiple Alibaba Cloud accounts. You can select only No. |
|   | RDS Instance ID | The ID of the ApsaraDB RDS for MySQL instance from which you want to track data changes. Note A read-only instance or temporary instance cannot be used as the source instance for change tracking. |

|   | Database Account | The database account of the ApsaraDB RDS for MySQL instance from which you want to track data changes. Note The account must have the SELECT permission on the objects for change tracking, the REPLICATION SLAVE permission, and the REPLICATION CLIENT permission. |
|---|---|---|
|   | Database Password | The password of the database account. |
|   | Network Type | The network type of the change tracking instance. Classic If you select Classic, no other configurations are required. VPC If you select VPC, you must configure the VPC and vSwitch parameters. Note If your change tracking client is deployed on a local server, you can select Classic or VPC. If you track data changes over internal networks, the network latency is minimal. |
| Consume r Network Type |   |   |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the data change types and objects.

| Parame ter | Description |
|---|---|

| Data Change Types | Data Updates DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updates DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Note If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the objects for change tracking. For more information, see Modify the objects for change tracking. |
|---|---|
| Source Objects | Select tables or databases from the Source Objects section and click the icon to move them to the Selected Objects section. |
| Selecte d Objects | If you want to remove a selected object, select the object in theS elected Objects section and click the icon to move it to the Source Objects section. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source database fails to be connected after the change tracking task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source databases within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. |
| Configure ETL | Specifies whether to configure the ETL feature. In this topic, the ETL feature is not supported, and No is selected. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the change tracking task, a precheck is performed. You can start the change tracking task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.
Wait until the change tracking task is started. You can add consumer groups and consume the tracked data only after the task is in the **Normal** state.

#### 5.3.2 Track data changes from a PolarDB-X 1.0 instance

### 1.0 instance

Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a PolarDB-X 1.0 instance.

**Limits**

> **Warning:** For more information about the limits for tracking data changes from a PolarDB-X 1.0 instance, see Precautions and limits for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X 1.0 instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck, and the change tracking task cannot be started. |

| Other limits | If more than two ApsaraDB RDS for MySQL instances are attached to a PolarDB- X 1.0 instance, issues such as latency and instability may occur to the DTS task when you track data changes from the PolarDB-X 1.0 instance. We recommend that you split the task for tracking data changes from a PolarDB-X 1.0 instance into multiple subtasks for tracking data changes from ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X 1.0 Instance A, you must create N change tracking tasks to track data changes from PolarDB-X 1.0 Instance A. We recommend that you estimate the number of change tracking tasks in advance and purchase enough expansion plans. Limits on the objects for change tracking: You can track data changes only at the table level. After the change tracking task is configured, the objects for change tracking cannot be reselected. If you want to track the data changes of tables that are not included in the selected objects, you must create another change tracking task for the tables. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt-online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If you perform a primary/secondary switchover on the source database when the change tracking task is running, the task fails. When the change tracking task is running, do not scale out or scale in the capacity of the source instance, migrate frequently accessed tables, change shards, or perform DDL operations. Otherwise, the change tracking task fails or data inconsistency occurs. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |
|---|---|

**Procedure**

1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click **Configure Channel** in the
Actions column.
3. Configure the source database and network type.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Database Type | The type of the source database. Select PolarDB-X 1.0. |
|   | Access Method | The access method of the source database. Select Alibaba Cloud Instance. |
|   | Instance Region | The region in which the source instance resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |

| ta Transmissi |   |   |
|---|---|---|
| Source Database |   |   |
|   | Replicate Data Across Alibaba Cloud Accounts | Specifies whether data is replicated across multiple Alibaba Cloud accounts. You can select only No. |
|   | Instance ID | The ID of the PolarDB-X 1.0 instance. |
|   | Database Account | The database account of the PolarDB-X 1.0 instance. |
|   | Database Password | The password of the database account. |
| Consume r Network Type | Network Type | The network type of the change tracking instance. Classic If you select Classic, no other configurations are required. VPC If you select VPC, you must configure the VPC and vSwitch parameters. Note If your change tracking client is deployed on a local server, you can select Classic or VPC. If you track data changes over internal networks, the network latency is minimal. |

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. Select the data change types and objects.

| Parameter | Description |
|---|---|

| Data Change Types | Data Updates DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updates DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Note You can track data changes only at the table level. After the change tracking task is configured, the objects for change tracking cannot be reselected. If you want to track the data changes of tables that are not included in the selected objects, you must create another change tracking task for the tables. |
|---|---|
| Source Objects | Select tables or databases from the Source Objects section and click the icon to move them to the Selected Objects section. |
| Selected Objects | If you want to remove a selected object, select the object in theS elected Objects section and click the icon to move it to the Source Objects section. |

6. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source database fails to be connected after the change tracking task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source databases within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. |
| Configure ETL | Specifies whether to configure the ETL feature. In this topic, the ETL feature is not supported, and No is selected. |

7. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the change tracking task, a precheck is performed. You can start the change tracking task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

8. Wait until the success rate becomes 100%. Then, click **Back**.
Wait until the change tracking task is started. You can add consumer groups and consume the tracked data only after the task is in the **Normal** state.

#### 5.3.3 Track data changes from a self-managed Oracle database

**managed Oracle database**

Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a self-managed Oracle database.

**Prerequisites**

The engine version of the self-managed Oracle database is 9i, 10g, or 11g. Real Application Cluster (RAC) instances are not supported. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database is running in ARCHIVELOG mode. Archived log files are accessible, and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files.

**Limits**

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The data logging feature must be enabled. Otherwise, error messages are returned during precheck and the change tracking task cannot be started. |

| Other limits | Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt-online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If you perform a primary/secondary switchover on the source database when the change tracking task is running, the task fails. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |
|---|---|

**Procedure**

1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click **Configure Channel** in the
Actions column.
3. Configure the source database and network type.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The type of the source database. Select Oracle. |
|   | Access Method | The access method of the source database. In this example, Public IP Address is selected. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | Hostname or IP address | The hostname or IP address of the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. |
|   | Oracle Type | You can select only Non-RAC Instance. |
|   | SID | The system ID (SID) of the self-managed Oracle database. |
|   | Database Account | The account of the self-managed Oracle database. Note The account must have the database administrator (DBA) permissions. |
|   | Database Password | The password of the database account. |

| Consume r Network Type | Network Type | The network type of the change tracking instance. Classic If you select Classic, no other configurations are required. VPC If you select VPC, you must configure the VPC and vSwitch parameters. Note If your change tracking client is deployed on a local server, you can select Classic or VPC. If you track data changes over internal networks, the network latency is minimal. |
|---|---|---|

4. In the lower part of the page, click **Test Connectivity and Proceed**.
5. If a whitelist is configured for your self-managed Oracle database, add the CIDR blocks of
DTS servers that are displayed in the dialog box to the whitelist. Then, click **Test**
**Connectivity and Proceed**.

> **Note:** If no whitelist is configured for your Oracle database, ignore the whitelist settings and click **Test Connectivity and Proceed**.

6. Select the data change types and objects.

| Parame ter | Description |
|---|---|
| Data Change Types | Data Updates DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updates DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Note If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the selected objects. For more information, see Modify the objects for change tracking. |
| Source Objects | Select tables or databases from the Source Objects section and click the icon to move them to the Selected Objects section. |

| Selecte d Objects | If you want to remove a selected object, select the object in theS elected Objects section and click the icon to move it to the Source Objects section. |
|---|---|

7. Click **Next: Advanced Settings**.

| Parameter | Description |
|---|---|
| Retry Time for Failed Connection | The retry time range for failed connections. If the source database fails to be connected after the change tracking task is started, DTS immediately retries a connection within the retry time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source databases within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. |
| Configure ETL | Specifies whether to configure the ETL feature. In this topic, the ETL feature is not supported, and No is selected. |
| Select Encoding Type | Select the encoding type of data written to the source database based on your business requirements. |

8. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the change tracking task, a precheck is performed. You can start the change tracking task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

9. Wait until the success rate becomes 100%. Then, click **Back**.
Wait until the change tracking task is started. You can add consumer groups and consume the tracked data only after the task is in the **Normal** state.

**What to do next**

### 5.4 Manage change tracking tasks

#### 5.4.1 Modify the objects for change tracking

Data Transmission Service (DTS) allows you to add or remove the objects for change tracking in the consumption process. This topic describes how to modify the objects for change tracking.

**Procedure**

1. Log on to the DTS console.
2. In the left-side navigation pane, click **Change Tracking**.
3. Find the change tracking task and click **Reselect Objects** in the Actions column.
4. In the **Configure Objects** step, you can add or remove the objects for change tracking.
Add the objects for change tracking In the **Source Objects** section, select one or more objects and click the icon to add the objects to the **Selected Objects** section. Remove the objects for change tracking In the **Selected Objects** section, select one or more objects and click the icon to move the objects to the **Source Objects** section.
5. In the lower part of the page, click **Next: Advanced Settings**.
6. In the lower part of the page, click **Next: Precheck and Start Task**.

> **Important:** Before you can start the change tracking task, a precheck is performed. You can start the change tracking task only after the task passes the precheck.
> If the task fails to pass the precheck, click **View Details** next to each failed item. After you troubleshoot the issues based on the causes, run a precheck again.

#### 5.4.2 Add consumer groups

You can manage consumer groups of a change tracking task in the Data Transmission Service (DTS) console. This topic describes how to add a consumer group.

**Prerequisites**

A change tracking task is created.

**Usage notes**

You can add multiple consumer groups in a change tracking task to repeatedly consume data. A consumer group consumes each message only once. Each consumer in the consumer group serves as a backup for other consumers. In a consumer group, only one consumer can consume data at a time. Other consumers act as disaster recovery nodes.

**Procedure**

1. Log on to the DTS console.
2. In the left-side navigation pane, click **Change Tracking**.
3. On the Change Tracking page, find the change tracking task for which you want to add a
consumer group and click the task ID.
4. In the left-side navigation pane, click **Consume Data**.
5. On the **Consume Data** page, click **Add Consumer Group** in the upper-left corner.
6. In the dialog box that appears, set the parameters for the consumer group.

| Parameter | Description |
|---|---|
| Consumer Group Name | The name of the consumer group. We recommend that you use a descriptive name to identify the consumer group. |

| Account | The username of the consumer group. The username can contain uppercase letters, lowercase letters, and digits. The username can be up to 16 characters in length. |
|---|---|
| Password | The password that corresponds to the username of the consumer group. The password must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| Confirm Password | Enter the password again. |

7. Click **OK**.

#### 5.4.3 Manage consumer groups

You can manage consumer groups of a change tracking task in the Data Transmission Service (DTS) console. This topic describes how to modify the password of a consumer group and how to delete a consumer group.

**Prerequisites**

**Procedure**

1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click **Change Tracking**.
3. On the Change Tracking page, find the change tracking task that you want to manage and
click the task ID.
4. In the left-side navigation pane, click **Consume Data**.
5. Modify the password of a consumer group or delete a consumer group.

**Modify the password**

i. On the **Consume Data** page, find the consumer group that you want to manage and click **Change Password** in the **Actions** column. ii. In the **Add Consumer Group** dialog box, enter a new password and confirm the password.

> **Note:** The password must contain at least two of the following character types: uppercase letters, lowercase letters, and digits.
> The password must be 8 to 32 characters in length.

iii. Click **OK**.

**Delete a consumer group**

> **Note:** After a consumer group is deleted, the data in the group is cleared and cannot be recovered. Proceed with caution.

i. On the **Consume Data** page, find the consumer group that you want to delete and click
**Delete** in the **Actions** column.
ii. In the message that appears, click **OK**.

### 5.5 Use the SDK to consume tracked data

**tracked data**

#### 5.5.1 Methods provided by SDK

You can use the SDK demo code that is provided by DTS to consume tracked data. This topic describes the methods that are available for the SDK classes.

**Methods of the RegionContex class**

| Method | Description |
|---|---|
| setAccessKey(accessKey) | Specifies the AccessKey ID of the Alibaba Cloud account to which the source instance belongs. |
| setSecret(AccessKeySecret) | Specifies the AccessKey secret of the Alibaba Cloud account to which the source instance belongs. |
| setUsePublicIp(usePublicIp) | Specifies whether to track data changes over the Internet. Note DTS can track data changes only over the Internet. Therefore, set the usePublicIp parameter to true . |
| context.setUseBinary(boolean useBinary) | Specifies whether to enable the binary packaging feature. Valid values: True and False. We recommend that you enable this feature to improve consumption performance. |
| context.setUseDrcNet(boolean useDrcNet) | Specifies whether to enable the network optimization feature. Valid values: True and False. We recommend that you enable this feature to improve consumption performance. |

|   | context.setUseBinary(boolean | Specifi Valid v |
|---|---|---|
| useBinary) |   |   |

|   | context.setUseDrcNet(boolean | feature |
|---|---|---|
| useDrcNet) |   |   |

**Methods of the ClusterClient class**

|   | Method |   | Description |   |
|---|---|---|---|---|
|   | void |   | Adds a downstream listener to retrieve data changes from a change tracking instance. Note The ClusterListener arg0 parameter specifies an object of the ClusterListener class. |   |
|   |   | void |   |   |
|   | addConcurrentListener(ClusterListe |   |   |   |
|   |   |   |   | No |
|   | ner arg0) |   |   |   |
|   | void askForGUID(String arg0) |   | Retrieves data changes from a change tracking instance. Set the String arg0 parameter to the ID of the change tracking instance. |   |
|   | List<ClusterListener> getConcurrentListeners() |   | Queries the list of listeners in a ClusterClient object. The return type is List <ClusterListener> . |   |
|   | void start() |   | Starts the SDK client to start change tracking. |   |

|   | List<ClusterListener> | Queries the list |   |
|---|---|---|---|
| getConcurrentListeners() |   |   |   |

| void stop() | Stops the SDK client to stop change tracking. Note Data pulling and notification callback are performed in the same thread of the SDK client. If the consumption code of the notify() method contains a function that prevents signal interruptions, the stop() function may fail to terminate the SDK client. |
|---|---|

**Methods of the ClusterListener class**

The `void notify(List<ClusterMessage> arg0)` method specifies the consumption mode of tracked data. When the DTS SDK receives the data, it uses the notify() function to notify a ClusterListener object to consume the data. Then, the SDK displays the data on the screen.

**Methods of the ClusterMessage class**

> **Note:** Each ClusterMessage object stores the data record of a transaction. Each data record in the transaction is stored by using a Record object.

| Method | Description |
|---|---|
| Record getRecord() | Retrieves a change record from a ClusterMessage object. The change record contains an entry in the binary log file, such as a BEGIN, COMMIT, UPDATE, or INSERT operation. |
| void ackAsConsumed | After the data consumption is complete, you must call this method to send an ACK packet to instruct the DTS server to update the consumer offset. This ensures the integrity of the consumed data after an abnormal SDK client restarts. Note If a downstream SDK client restarts after a breakdown, the client resumes change tracking from the last consumer offset. |

**Methods of the Record class**

The `String getAttribute(String key)` method retrieves the attribute values in a Record object. The following table describes the parameters that are available when you call this method.

| Parameter | Description |
|---|---|
| record id _ | The ID of the record. Note The record ID may not increment during the change tracking process. |
| instance | The endpoint that is used to connect to the database instance. The format is <IP address>:<Port number>. |
| source type _ | The engine type of the database instance. The value is set to MySQL. |
| source category _ | The type of the record. The value is set to full recorded. _ |

| timestamp | The binlog timestamp that is generated when the SQL statement is executed in the source database. |
|---|---|
| checkpoint | The checkpoint of the binary log file. The format is binlog offset@binlog file . _ _ Note The binlog offset parameter _ indicates the offset of a record in the binary log file. The binlog file parameter indicates the numerical _ suffix of the binary log file. For example, if the name of a binary log file is mysql-bin.0008, the value of the binlog file parameter is 8. _ |
| record type _ | The operation type. Valid values: insert, update, delete, replace, ddl, begin, commit, and heartbeat. Note A heartbeat record indicates the heartbeat table that is defined by DTS. The system generates one heartbeat record per second to detect whether the change tracking instance is running as expected. |
| db | The name of the database. |
| table name _ | The name of the table. |
| record recording _ | The encoding format. |
| primary | The name of the primary key column. If the primary key is a composite key, separate column names with commas (,). |
| fields enc _ | The encoding of each field value. Separate fields with commas (,). Note If a field value is not of the character type, the encoding of this field value is null. |

The following table lists the methods that are preset in the SDK demo code. You can call these methods to retrieve the attribute values in a Record object.

| Method | Description |
|---|---|
| Type getOpt() | Queries the operation type. |
| String getCheckpoint() | Queries the checkpoint of the binary log file. |
| String gettimestamp() | Queries the timestamp of the binary log file. |
| String getDbname() | Queries the database name. |
| String getTablename() | Queries the table name. |
| String getPrimaryKeys() | Queries the name of the primary key column. |
| DBType getDbType() | Queries the database type. |

| String getServerId() | Queries the endpoint that is used to connect to the database instance. |
|---|---|
| int getFieldCount() | Queries the number of fields. |
| List<Field> getFieldList() | Queries the definitions of all fields, the pre-change image values, and the post-change image values. For more information, see Methods of the Field class. |
| Boolean isFirstInLogevent() | Checks whether the record is the first transaction log in a large volume of data changes. The return value is True or False. |

**Methods of the Field class**

| Method | Description |
|---|---|
| String getEncoding() | Obtains the encoding format of the field value. |
| String getFieldname() | Queries the name of the field. |
| Type getType() | Queries the data type of the field. |
| ByteString getValue() | Queries the value of the field. The return type is ByteString. If the field is not specified, the method returns NULL . |
| Boolean isPrimary() | Checks whether the field is a primary key column. The return value is True or False. |

#### 5.5.2 Quick start

This section describes how to use the DTS Java SDK to perform some basic operations.

**Initialize a RegionContext object**

A RegionContext object stores the settings of authentication credentials and network access mode. The following code shows how to initialize a RegionContext object.

```java
import java.util.List; import com.aliyun.drc.clusterclient.ClusterClient; import com.aliyun.drc.clusterclient.DefaultClusterClient; import com.aliyun.drc.clusterclient.RegionContext; public class MainClass
```

`{`

```
      public static void main(String[] args) throws Exception {
        // Create a RegionContext object.
          RegionContext context = new RegionContext();
          context.setAccessKey("<AccessKey>");
          context.setSecret("<AccessKeySecret>");
          context.setUsePublicIp(true);
          // Create a ClusterClient object.
          final ClusterClient client = new DefaultClusterClient(context);
          // Other invocation code.
          ...
```

`}` `}`

**Initialize a Listener object**

Data consumption is implemented by using an object of the Listener class. After you initialize the ClusterClient object, you must add a Listener object. The Listener object uses the notify() method to receive and consume the tracked data. The following code shows how to display the tracked data on the screen.

```java
import com.aliyun.drc.clusterclient.ClusterClient; import com.aliyun.drc.clusterclient.ClusterListener; import com.aliyun.drc.clusterclient.DefaultClusterClient; import com.aliyun.drc.clusterclient.RegionContext; import com.aliyun.drc.clusterclient.message.ClusterMessage; public class MainClass
```

`{`

```java
    public static void main(String[] args) throws Exception {
        // Initialize the RegionContext object.
        ...
        //Initialize the ClusterClient object.
        ...
        ClusterListener listener = new ClusterListener(){
             @Override
             public void notify(List<ClusterMessage> messages) throws Exception {
                  for (ClusterMessage message : messages) {
                    // Display the tracked data on the screen.
                      System.out.println(message.getRecord() + ":" +
message.getRecord().getTablename() + ":"
                      + message.getRecord().getOpt());
                      // Call the following method to send an ACK packet to the DTS serv
er.
                      message.ackAsConsumed();
```

`}` `}` `}` `}` DTS saves the consumption checkpoints of the SDK to the DTS server. This simplifies disaster recovery during the use of the SDK. The ackAsConsumed() method sends the checkpoint and timestamp of the latest data record that was consumed by the DTS SDK to the DTS server. If the SDK restarts due to an error, the SDK obtains the consumption checkpoint from the DTS server. The SDK resumes data consumption from the checkpoint. This ensures that the SDK does not consume duplicate data.

**Start the ClusterClient object**

Use the following code:

```java
import java.util.List; import com.aliyun.drc.clusterclient.ClusterClient; import com.aliyun.drc.clusterclient.ClusterListener; import com.aliyun.drc.clusterclient.DefaultClusterClient; import com.aliyun.drc.clusterclient.RegionContext; import com.aliyun.drc.clusterclient.message.ClusterMessage; import org.slf4j.Logger; import org.slf4j.LoggerFactory; public class MainClass
```

`{`

```
   public static void main(String[] args) throws Exception {
    // Initialize the RegionContext object.
    ...
    // Initialize the ClusterClient object.
    ...
    // Initialize the ClusterListener object.
    ...
    // Add a Listener class.
      client.addConcurrentListener(listener);
      // Specify the ID of the change tracking instance.
      client.askForGUID("dts_rdsrjiei2u2afnb_DSF");
      // Start a background thread. The main thread cannot exit.
      client.start();
```

`}` The askForGUID() method sets the ID of the change tracking instance. You can obtain the ID of the change tracking instance from the DTS console. After the ID of the change tracking instance is specified in the askForGUID() method, the SDK retrieves incremental data from this instance. Before you can start a ClusterClient object, you must add a Listener class to the ClusterClient object. When the ClusterClient object pulls incremental data from the change tracking instance, it also calls the notify() method of the Listener class to consume data.

#### 5.5.3 Parse tracked SQL statements

You can use the DTS SDK to track data changes. DTS records the tracked data changes in a custom format. This topic describes how to parse various types of SQL statements.

**Parse a DDL statement**

If a data definition language (DDL) operation is performed in the source database, the operation type of the data record is DDL. The DDL statement is stored in the value of the first column. You can use the following sample code to parse the DDL statement:

```
String ddl_string; Record.Type type=record.getOpt(); if(type.equals(Record.Type.DDL)){
    List<DataMessage.Record.Field> fields = record.getFieldList();
    ddl_string = fields.get(0).getValue().toString();
```

`}`

**Parse an INSERT statement**

If an INSERT operation is performed in the source database, the operation type of the data record is INSERT. You can use the following sample code to parse the INSERT statement:

```
StringBuilder insert_string=new StringBuilder(); Record.Type type=record.getOpt(); DataMessage.Record.Field field; StringBuilder FieldName=new StringBuilder(); StringBuilder FieldValue = new StringBuilder(); if(type.equals(Record.Type.INSERT)){
       int i=0;
       List<DataMessage.Record.Field> fields = record.getFieldList();
       for (; i < fields.size(); i++) {
              field = fields.get(i);
FieldName.append('`'+field.getFieldname().toLowerCase()+'`');
              FieldValue.append("'"+field.getValue()+"'");
              if (i ! = fields.size() - 1) {
                      FieldName.append(',');
                      FieldValue.append(',');
```

`}` `}`

```
        insert_string.append("insert "+ record.getTablename()+"
("+FieldName.toString()+") values("+FieldValue.toString()+");");
```

`}`

**Parse an UPDATE statement**

If an UPDATE operation is performed in the source database, the operation type of the data record is UPDATE. The field values prior to the UPDATE operation are stored in `Record.getFieldList()` entries with even indexes. The field values after the UPDATE operation are stored in Record.getFieldList() entries with odd indexes. If the UPDATE operation is performed on a table that has a primary key, you can use the following sample code to parse the UPDATE statement:

```
StringBuilder update_string=new StringBuilder(); Record.Type type=record.getOpt(); DataMessage.Record.Field field; StringBuilder SetValue = new StringBuilder(); StringBuilder WhereCondition = new StringBuilder(); String ConditionStr; boolean hasPk=false; boolean pkMode=false; boolean hasSet=false; if(type.equals(Record.Type.UPDATE)){
    int i=0;
    DataMessage.Record.Field OldField = null;
```

`g`

```
    DataMessage.Record.Field NewField = null;
    List<DataMessage.Record.Field> fields = record.getFieldList();
    for (; i <fields.size() ; i++) {
        if (i % 2 == 0) {
            OldField = fields.get(i);
            continue;
```

`}`

```
    NewField = fields.get(i);
    field = NewField;
    if (field.isPrimary()) {
        if (hasPk) {
            WhereCondition.append(" and ");
```

`}`

```
        //where old value
        ConditionStr = getFieldValue(OldField);
        if(ConditionStr==null){
WhereCondition.append("`"+field.getFieldname().toLowerCase()+"`" + " " + "is null");
        }else{
               WhereCondition.append("`"+field.getFieldname().toLowerCase()+"`"+" = "+ "
'"+OldField.getValue()+"'");
```

`}`

```
        hasPk = true;
```

`}`

```
    if (hasSet) {
        SetValue.append(",");
```

`}`

```
      SetValue.append("`"+field.getFieldname().toLowerCase()+"`" + " = " +
"'"+field.getValue()+"'");
    String setStr = getFieldValue(field);
    hasSet = true;
```

`}`

```
    update_string.append("Update "+record.getTablename() +" Set " + SetValue + " Where
"+WhereCondition +";");
```

`}`

```java
protected String getFieldValue(Field field) throws Exception {
    ByteString byteString = field.getValue();
    if (byteString == null) {
        return null;
```

`}`

```
    else {
        String value;
        if (field.getType() ==
com.aliyun.drc.client.message.DataMessage.Record.Field.Type.STRING && field.getEncoding() ! = null && field.getEncoding() ! = "ASCII") {
            value = field.getValue().toString(field.getEncoding());
```

`}`

```
        else {
          value = byteString.toString();
```

`}`

```
        return value;
```

`}` `}`

**Parse a DELETE statement**

If a DELETE operation is performed in the source database, the operation type of the data record is DELETE. If the DELETE operation is performed on a table that has a primary key, you can use the following sample code to parse the DELETE statement:

```
StringBuilder delete_string=new StringBuilder(); Record.Type type=record.getOpt(); DataMessage.Record.Field field; StringBuilder FieldName=new StringBuilder(); StringBuilder FieldValue = new StringBuilder(); StringBuilder DeleteCondition = new StringBuilder(); boolean hasPk=false; boolean pkMode=false; if(type.equals(Record.Type.DELETE)){
   int i=0;
   List<DataMessage.Record.Field> fields = record.getFieldList();
   delete_string.append("Delete From" + record.getTablename() + "where");
   // Check whether the table has a primary key.
   if (record.getPrimaryKeys() ! = null) {
             pkMode = record.getPrimaryKeys().length() > 0 ? true : false;
```

`}`

```
   for (; i < fields.size(); i++) {
            if ((pkMode && ! field.isPrimary())) {
                    continue;
```

`}`

```
            if (hasPk) {
                    delete_string.append(" and ");
```

`}`

```
            delete_string.append(field.getFieldname() + "=" + field.getValue());
            hasPk = true;
```

`}`

```
    delete_string.append(";");
```

`}`

**Parse a REPLACE statement**

If a REPLACE operation is performed in the source database, the operation type of the data record is UPDATE or INSERT. If the value specified in the REPLACE statement does not exist, the operation type of the data record is INSERT. If the value specified in the REPLACE statement exists, the operation type of the data record is UPDATE.

**Parse a BEGIN statement**

If a BEGIN operation is performed in the source database, the operation type of the data record is BEGIN. You do not need to perform operations on fields because the BEGIN statement does not modify fields. You only need to check that the operation is a BEGIN operation. You can use the following sample code to parse the BEGIN statement:

```
StringBuilder sql_string = new StringBuilder(); Record.Type type = record.getOpt(); if(type.equals(Record.Type.BEGIN)){
        sql_string.append("Begin");
```

`}`

**Parse a COMMIT statement**

If a COMMIT operation is performed in the source database, the operation type for the data record is COMMIT. You do not need to perform operations on fields because the COMMIT statement does not modify fields. You only need to check that the operation is a COMMIT operation. You can use the following sample code to parse the COMMIT statement:

```
StringBuilder sql_string = new StringBuilder(); Record.Type type = record.getOpt(); if(type.equals(Record.Type.COMMIT)){
        sql_string.append("commit");
```

`}`

#### 5.5.4 Run the SDK demo code

This topic describes how to run the SDK demo code that is provided by the Data Transmission Service (DTS) console.
1. Create an AccessKey.
Your account must pass the AccessKey authentication before you use an SDK to connect to a change tracking instance. Therefore, you must obtain an AccessKey pair before you use the SDK. For more information, see the **Obtain an AccessKey pair** topic of the **DTS**
**Developer Guide**.
2. Install the SDK for Java.
The development environment supported by the DTS SDK for Java is J2SE Development Kit (JDK) V1.5 or later. The following steps provide an example on how to install the SDK for Java: i. Click **View Sample Code** and download the SDK package consumer.jar. ii. In the following example, the jar package is imported to an Eclipse project. In Eclipse, right-click your project and select **Properties**. Click **Java Build Path** on the left, and then click the **Libraries** tab. Click **Add External JARs**. Locate the path in which the consumer.jar file is stored and add the**consumer.jar** file to the project. iii. Select the consumer.jar package and click **OK**. After you perform the preceding steps, you can use the SDK for Java in the project.
3. Run the SDK demo code.
DTS provides the SDK demo code. You can copy the demo code by using the View Sample Code feature in the DTS console. In the following example, the SDK demo code is run in an Eclipse project. i. Create a class named MainClass in the src directory of the Eclipse project. ii. Open the generated Java file MainClass and delete the code template. iii. Paste the demo code into the MainClass file. iv. Modify the AccessKey ID, the AccessKey secret, and the ID of the change tracking instance in the demo code. The following figure shows the sample code. Figure 1. Sample code Replace the marked parts in the preceding sample code with the AccessKey ID, the AccessKey secret, and the ID of the change tracking instance of your account. Log on to the DTS console to obtain the ID of the change tracking instance. In the leftside navigation pane, click **Change ********** to go to the Change Tracking Tasks page. On the page that appears, find the instance that you want to manage and click the ID of the instance in the **ID/Name** column. v. In Eclipse, right-click the demo file and choose **Run As > Java ************* to run the demo code.

### 5.6 Use a Kafka client to consume tracked data

**tracked data**

This topic describes how to use a Kafka client demo to consume tracked data. The change tracking feature of the new version allows you to consume tracked data by using a Kafka client of V0.11 to V2.0.

**Prerequisites**

A change tracking instance is created. For more information, see Track data changes from an ApsaraDB RDS for MySQL instance. One or more consumer groups are created. For more information, see Add consumer groups.

**Precautions**

If you enable auto commit when you use the change tracking feature, some data may be committed before it is consumed. This results in data loss. We recommend that you manually commit data.

> **Note:** If data fails to be committed due to a fault, you can restart the client to continue consuming data from the last recorded consumer offset. However, duplicate data may be generated during this period. You must manually filter out the duplicate data.

Data is serialized and stored in the Avro format. For more information, see Record.avsc.

> **Note:** If the client that you use is not a Kafka client, you must parse the tracked data based on the Avro schema.

Regarding the `offsetFotTimes` interface, the search unit of DTS is seconds, and the search unit of native Kafka is milliseconds.

**Download and run the demo code of the Kafka client**

Download the Kafka client demo. For more information about how to use the demo, see Readme. Table 1. Steps

| Step | File or directory |
|---|---|
| 1. Use the native Kafka consumer to obtain incremental data from the change tracking instance. | subscribe example- _ master/javaimpl/src/main/java/r ecordgenerator/ |
| 2. Deserialize the image of the incremental data, and obtain the pre-image and post-image and other attributes. | subscribe example- _ master/javaimpl/src/main/java/ boot/MysqlRecordPrinter.java |
| 3. Convert the dataTypeNumber values in the deserialized data into MySQL or Oracle data types. Note For more information, see the Mappings between MySQL data types and dataTypeNumber values and Mappings between Oracle data types and dataTypeNumber values sections of this topic. | subscribe example- _ master/javaimpl/src/main/java/r ecordprocessor/mysql/ |

**Procedure**

This procedure uses IntelliJ IDEA (Community Edition 2018.1.4 Windows) as an example.
1. Download the Kafka client demo and decompress the package.
2. Open IntelliJ IDEA. In the window that appears, click **Open**.
3. In the dialog box that appears, go to the directory in which the downloaded demo code
resides and find the pom.xml file.
4. In the dialog box that appears, select **Open as Project**.
5. In the Project tool window of IntelliJ IDEA, expand folders to find the demo file of the Kafka
client, and double-click the file. The file name is NotifyDemo.java.
6. Set the parameters in the NotifyDemo.java file.

|   | Parameter |   | Description |   |   |   |   |   | Method to obtain the parameter value |
|---|---|---|---|---|---|---|---|---|---|
|   | USER NAME _ |   | The account of the consumer group. Warning If you are not using the Kafka client that is described in this topic, you must specify the username in the following format: <Consumer group account>- <Consumer group ID> , for example, dtstest- dtsae******bpv . Otherwise, the connection fails. |   |   |   |   |   | In the Data Transmission Service (DTS) console, find the change tracking instance that you want to view details and click the instance ID. In the left- side navigation pane, click Consume Data. On the page that appears, you can obtain the consumer group ID and the corresponding account information. Note The password of the consumer group account is automatically specified when you create the consumer group. |
|   |   |   |   |   | <Consumer group account>- |   |   |   | instance that you and click the insta |
|   |   |   |   | <Consumer group ID> |   |   |   |   |   |
|   |   |   |   |   |   |   | , for |   |   |
|   |   |   |   |   |   |   |   |   | D |
|   |   |   |   | example, |   |   |   |   |   |
|   |   |   |   | dtsae******bpv |   |   |   |   |   |
|   | PASSWORD NAM _ E |   | The password of the account. |   |   |   |   |   |   |
|   | SID NAME _ |   | The ID of the consumer group. |   |   |   |   |   |   |
|   | GROUP NAME _ |   | The name of the consumer group. Set this parameter to the consumer group ID. |   |   |   |   |   |   |
|   | KAFKA TOPIC _ |   | The topic of the change tracking instance. |   |   |   |   |   | In the DTS console, find the change tracking instance that you want to view details and click the instance ID. In the left-side navigation pane, click Basic Information. On the page that appears, you can view the tracked topic, endpoint, and port number. |
|   | KAFKA BROKER _ _ URL NAME _ |   | The endpoint and port number of the change tracking instance. Note If you track data changes over internal networks, the network latency is minimal. This is applicable if the Elastic Compute Service (ECS) instance on which you deploy the Kafka client resides on the classic network or in the same virtual private cloud (VPC) as the change tracking instance. |   |   |   |   |   |   |

| INITIAL CHECKPO _ INT NAME _ | The consumer offset of consumed data. The value is a UNIX timestamp. Note You must save the consumer offset. If the consumption process is interrupted, you can specify the consumer offset on the change tracking client to resume data consumption. This helps prevent data loss. When you start the change tracking client, you can specify the consumer offset to consume data based on your business requirements. | When you use the Kafka client to track data changes for the first time, convert the required time point into a UNIX timestamp. |
|---|---|---|
| USE CONFIG CHE _ _ CKPOINT NAME _ | Specifies whether to force the client to consume data from the specified consumption checkpoint. Default value: true. You can set this parameter to true to prevent the data that is received but not processed from being lost. | N/A |

7. In the top navigation bar of IntelliJ IDEA, choose **Run > Run** to run the client.

> **Note:** When you run IntelliJ IDEA for the first time, it loads and installs the relevant dependency.

**Execution result**

The following figure shows that the Kafka client can track data changes in the source database. You can also delete the `//` characters from the //log.info(ret); string in line 25 of the NotifyDemo.java file. Then, run the client again to view the data change information.

**Mappings between MySQL data types and dataTypeNumber**

**values**

| MySQL data type | Value of dataTypeNumber |
|---|---|
| MYSQL TYPE DECIMAL _ _ | 0 |
| MYSQL TYPE INT8 _ _ | 1 |
| MYSQL TYPE INT16 _ _ | 2 |

| MYSQL TYPE INT32 _ _ | 3 |
|---|---|
| MYSQL TYPE FLOAT _ _ | 4 |
| MYSQL TYPE DOUBLE _ _ | 5 |
| MYSQL TYPE NULL _ _ | 6 |
| MYSQL TYPE TIMESTAMP _ _ | 7 |
| MYSQL TYPE INT64 _ _ | 8 |
| MYSQL TYPE INT24 _ _ | 9 |
| MYSQL TYPE DATE _ _ | 10 |
| MYSQL TYPE TIME _ _ | 11 |
| MYSQL TYPE DATETIME _ _ | 12 |
| MYSQL TYPE YEAR _ _ | 13 |
| MYSQL TYPE DATE NEW _ _ _ | 14 |
| MYSQL TYPE VARCHAR _ _ | 15 |
| MYSQL TYPE BIT _ _ | 16 |
| MYSQL TYPE TIMESTAMP NEW _ _ _ | 17 |
| MYSQL TYPE DATETIME NEW _ _ _ | 18 |
| MYSQL TYPE TIME NEW _ _ _ | 19 |
| MYSQL TYPE JSON _ _ | 245 |
| MYSQL TYPE DECIMAL NEW _ _ _ | 246 |
| MYSQL TYPE ENUM _ _ | 247 |
| MYSQL TYPE SET _ _ | 248 |
| MYSQL TYPE TINY BLOB _ _ _ | 249 |
| MYSQL TYPE MEDIUM BLOB _ _ _ | 250 |
| MYSQL TYPE LONG BLOB _ _ _ | 251 |
| MYSQL TYPE BLOB _ _ | 252 |
| MYSQL TYPE VAR STRING _ _ _ | 253 |
| MYSQL TYPE STRING _ _ | 254 |
| MYSQL TYPE GEOMETRY _ _ | 255 |

**Mappings between Oracle data types and dataTypeNumber**

**values**

| Oracle data type | Value of dataTypeNumber |
|---|---|
| VARCHAR2 or NVARCHAR2 | 1 |
| NUMBER or FLOAT | 2 |
| LONG | 8 |
| DATE | 12 |
| RAW | 23 |
| LONG RAW _ | 24 |
| UNDEFINED | 29 |
| XMLTYPE | 58 |
| ROWID | 69 |
| CHAR and NCHAR | 96 |
| BINARY FLOAT _ | 100 |
| BINARY DOUBLE _ | 101 |
| CLOB/NCLOB | 112 |
| BLOB | 113 |
| BFILE | 114 |
| TIMESTAMP | 180 |
| TIMESTAMP WITH TIME ZONE _ _ _ | 181 |
| INTERVAL YEAR TO MONTH _ _ _ | 182 |
| INTERVAL DAY TO SECOND _ _ _ | 183 |
| UROWID | 208 |
| TIMESTAMP WITH LOCAL TIME ZONE _ _ _ _ | 231 |
