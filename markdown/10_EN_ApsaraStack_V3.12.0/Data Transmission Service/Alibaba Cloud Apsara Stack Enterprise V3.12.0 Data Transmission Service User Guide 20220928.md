---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 155
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Data%20Transmission%20Service%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Data Transmission Service User Guide 20220928

## Table of Contents

- 1 What is DTS?
- 2 Log on to the DTS console
- 3 Data migration
  - 3.1 Database and migration types
  - 3.2 Create a data migration instance
  - 3.3 Configure data migration tasks
    - 3.3.1 Migrate data between ApsaraDB RDS for PostgreSQL instances
    - 3.3.2 Migrate incremental data from a user-created SQL Server database to an ApsaraDB RDS for SQL Server instance
    - 3.3.3 Migrate data from a user-created MySQL database to an ApsaraDB RDS for MySQL instance
    - 3.3.4 Migrate data from a user-created MySQL database to a Cloud Native Distributed Database PolarDB-X instance
    - 3.3.5 Migrate data from an ApsaraDB RDS for MySQL instance to a user-created Oracle database
    - 3.3.6 Migrate data between user-created Oracle databases
    - 3.3.7 Migrate data from a user-created Oracle database to an ApsaraDB RDS for MySQL instance
    - 3.3.8 Migrate data from a user-created Oracle database to a PolarDB cluster
    - 3.3.9 Migrate data from a user-created Oracle database to a Cloud Native Distributed Database PolarDB-X instance
  - 3.4 Manage data migration tasks
    - 3.4.1 Object name mapping
    - 3.4.2 Specify an SQL condition to filter data
    - 3.4.3 Troubleshoot a failed data migration task
  - 3.5 Precheck items
    - 3.5.1 Source database connectivity
    - 3.5.2 Check the destination database connectivity
    - 3.5.3 Binary logging configurations of the source database
    - 3.5.4 Integrity of the FOREIGN KEY constraints
    - 3.5.5 Existence of FEDERATED tables
    - 3.5.6 Permissions
    - 3.5.7 Object name conflict
    - 3.5.8 Schema existence
    - 3.5.9 Value of server_id in the source database
    - 3.5.10 Source database version
  - 3.6 Data type mappings between heterogeneous databases
- 4 Data synchronization
  - 4.1 Database types, initial synchronization types, and synchronization topologies
  - 4.2 Create a data synchronization instance
  - 4.3 Synchronization topologies
  - 4.4 Configure data synchronization tasks
    - 4.4.1 Configure data synchronization between ApsaraDB RDS for MySQL instances
    - 4.4.2 Synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project
    - 4.4.3 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL cluster
    - 4.4.4 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance
    - 4.4.5 Synchronize data between Cloud Native Distributed Database PolarDB-X instances
    - 4.4.6 Synchronize data from a Cloud Native Distributed Database PolarDB-X instance to an AnalyticDB for MySQL cluster
    - 4.4.7 Synchronize data from a Cloud Native Distributed Database PolarDB-X instance to a DataHub instance
    - 4.4.8 Configure two-way data synchronization between RDS instances
      - 4.4.8.1 Overview
      - 4.4.8.2 Supported synchronization statements
      - 4.4.8.3 Detect and resolve conflicts
      - 4.4.8.4 Synchronization restrictions
      - 4.4.8.5 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances across regions
  - 4.5 Manage data synchronization instances
    - 4.5.1 Specify the name of an object in the destination instance
    - 4.5.2 Check the synchronization performance
    - 4.5.3 Add objects to a data synchronization task
    - 4.5.4 Remove objects from a data synchronization task
    - 4.5.5 Troubleshoot precheck failures
- 5 Change tracking
  - 5.1 Overview
  - 5.2 Create a change tracking instance
  - 5.3 Configure change tracking tasks
    - 5.3.1 Track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance
    - 5.3.2 Track data changes from a PolarDB-X instance
    - 5.3.3 Track data changes from a user-created Oracle database
  - 5.4 Manage change tracking tasks
    - 5.4.1 Modify the consumption checkpoint
    - 5.4.2 Modify the objects for change tracking
    - 5.4.3 Create a consumer group
    - 5.4.4 Manage consumer groups
  - 5.5 Use the SDK to consume tracked data
    - 5.5.1 Methods provided by SDK
    - 5.5.2 Quick start
    - 5.5.3 Parse tracked SQL statements
    - 5.5.4 Run the SDK demo code
  - 5.6 Use a Kafka client to consume tracked data

## 1 What is DTS?

Data Transmission Service (DTS) is a data service that is provided by Alibaba Cloud. DTS supports data transmission between various types of data sources, such as relational databases and big data systems. Features DTS has the following advantages over traditional data migration and synchronization tools: high compatibility, high performance, security, reliability, and ease of use. DTS allows you to simplify data transmission and focus on business development.

| Feature | Description |
|---|---|
| Data migration | You can use DTS to migrate data between homogeneous and heterogeneous data sources. This feature applies to the following scenarios: data migration to Alibaba Cloud, data migration between instances within Alibaba Cloud, and database splitting and scale- out. |
| Data synchronizati on | You can use DTS to synchronize data between data sources. This feature applies to the following scenarios: disaster recovery, data backup, load balancing, cloud BI systems, and real-time data warehousing. |
| Change tracking | You can use DTS to track data changes from user-created MySQL databases, ApsaraDB RDS for MySQL instances, Cloud Native Distributed Database PolarDB-X instances (formerly known as DRDS), and user-created Oracle databases in real time. This feature applies to the following scenarios: cache updates, business decoupling, asynchronous data processing, synchronization of heterogeneous data, and synchronization of extract, transform, and load (ETL) operations. |

le

## 2 Log on to the DTS console

This topic describes how to log on to the Data Transmission Service (DTS) console. Google Chrome is used in this example. Prerequisites The domain name of the ASCM console is obtained from the deployment personnel before you log on to the ASCM console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL used to log on to the ASCM console. Press the Enter key.
2. Enter your username and password.
Obtain the username and password used to log on to the console from the operations administrator.

> Not e When you log on to the ASCM console for the first time, you must change the password of your username. For security reasons, your password must meet the minimum complexity requirements. The password must be 8 to 20 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters.
> Digits.
> Special characters. Special characters include exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).

3. Click Login to go to the ASCM console homepage.
4. In the top navigation bar, choose Product s > Dat a T ransmission Service.
5. On the DT S page, select an organizat ion and region, and then click DT S.

> Not e If the top navigation bar is enabled for the DTS console, you can select the organization and resource set in the top navigation bar after you log on to the DTS console.

## 3 Data migration

### 3.1 Database and migration types

You can use Data Transmission Service (DTS) to migrate data between homogeneous and heterogeneous data sources. Typical scenarios include data migration to Alibaba Cloud, data migration between instances within Alibaba Cloud, and database splitting and scale-out. This topic describes the database types, database versions, and migration types that are supported by data migration.

| Source database | Destination database | Migration type |
|---|---|---|
| User-created MySQL database Versions 5.1, 5.5, 5.6, and 5.7 RDS MySQL All versions | User-created MySQL database Versions 5.1, 5.5, 5.6, and 5.7 | Schema migration Full data migration Incremental data migration |
|   | RDS MySQL Versions 5.6 and 5.7 | Schema migration Full data migration Incremental data migration |
|   | Cloud Native Distributed Database PolarDB- X (formerly known as DRDS) All versions | Full data migration Incremental data migration |
|   | User-created Oracle database (RAC or non- RAC architecture) Versions 9i, 10g, 11g, and 12c | Full data migration Incremental data migration |

| Source database | Destination database | Migration type |
|---|---|---|
| User-created SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, and 2016 Not e DTS does not support SQL Server clusters or SQL Server Always On availability groups (AOAG). If the version of the source database is 2005, incremental data migration is not supported. | User-created SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, and 2016 Not e DTS does not support SQL Server clusters or SQL Server Always On availability groups (AOAG). RDS SQL Server Versions 2005, 2008, 2008 R2, 2012, 2014, and 2016 | Schema migration Full data migration Incremental data migration |
|   | User-created Oracle database (RAC or non- RAC architecture) Versions 9i, 10g, 11g, and 12c | Schema migration Full data migration Incremental data migration |
|   | PolarDB (formerly known as ApsaraDB RDS for PPAS) Version 11 | Schema migration Full data migration Incremental data migration |
| User-created Oracle database (RAC or non-RAC architecture) Versions 9i, 10g, 11g, and 12c |   |   |
|   | User-created MySQL database Versions 5.1, 5.5, 5.6, and 5.7 | Schema migration Full data migration Incremental data migration |
|   | RDS MySQL Versions 5.6 and 5.7 | Schema migration Full data migration Incremental data migration |

| Source database | Destination database | Migration type |
|---|---|---|
|   | Cloud Native Distributed Database PolarDB- X All versions | Full data migration Incremental data migration |
|   | AnalyticDB for MySQL Versions 2.0 and 3.0 | Schema migration Full data migration Incremental data migration |
| User-created PostgreSQL database Versions 9.4, 9.5, 9.6, and 10.x RDS PostgreSQL | User-created PostgreSQL database Versions 9.4, 9.5, 9.6, and 10.x RDS PostgreSQL Versions 9.4 and 10 | Schema migration Full data migration Incremental data migration |
| Versions 9.4 and 10 |   |   |

### 3.2 Create a data migration instance

Before you configure a task to migrate data, you must create a data migration instance. This topic describes how to create a data migration instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. In the upper-right corner, click Creat e Migrat ion T ask.
4. In the Create DTS Instances dialog box, select a region, and enter the number of data migration
instances that you want to create.

> Not e In the Create DTS Instances dialog box, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click Creat e.

### 3.3 Configure data migration tasks

#### 3.3.1 Migrate data between ApsaraDB RDS for PostgreSQL instances

PostgreSQL instances This topic describes how to migrate data between ApsaraDB RDS for PostgreSQL instances by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The network type of both the source and destination ApsaraDB RDS for PostgreSQL instances is VPC. Precautions During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the load of the database server. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. To ensure that the delay time of incremental data migration is accurate, DTS adds a heartbeat table named dts_postgres_heartbeat to the source database. During incremental data migration, DTS creates a replication slot for the source database. The replication slot is prefixed with `dts_sync_` . DTS automatically clears historical replication slots every 90 minutes to prevent them from occupying disk space.

> Not e If a migration task is released or fails, DTS automatically clears the replication slot. After a switchover between primary and secondary ApsaraDB RDS for PostgreSQL databases, you must log on to the secondary database to clear the replication slot.

If a data migration task fails, DTS automatically resumes the task. Before you switch your workloads to the destination instance, stop or release the data migration task. Otherwise, the data in the source instance will overwrite the data in the destination instance after the task is resumed. Limits A single data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, DTS synchronizes only data manipulation language (DML) operations. DML operations include INSERT, DELETE, and UPDATE. Data migration process The following table describes how DTS migrates the schemas and data of the source PostgreSQL database. The process avoids data migration failures that are caused by dependencies between objects.

| Data migration process | Description |
|---|---|
| 1. Schema migration | DTS migrates the schemas of tables, views, sequences, functions, user-defined types, rules, domains, operations, and aggregates to the destination database. Not e DTS does not migrate functions that are written in the C programming language. |
| 2. Full data migration | DTS migrates historical data of the required objects to the destination database. |
| 3. Schema migration | DTS migrates the schemas of triggers and foreign keys to the destination database. |
| 4. Incremental data migration | DTS migrates incremental data of the required objects to the destination database. Not e Incremental data migration does not support the BIT data type. |

Before you begin If you need to perform incremental data migration, you must change the value of the wal_level parameter to logical for the source RDS instance.

> **Warning:** After you change the value of the `wal_level` parameter, you must restart the instance to apply the change. We recommend that you evaluate the impact on your business and change the parameter setting during off-peak hours.

Procedure
1. Create a data migration instance.
2. In the migration task list, find the migration task that you created, and click Conf igure Migrat ion
T ask in the Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | Select RDS inst ance. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the source RDS instance. |
|   | Database Name | Enter the name of the source database. |
|   | Database Account | Enter the database account of the source RDS instance. The account must have the read and write permissions on the source database. |
|   | Database Password | Enter the password of the source database account. |
|   | Instance Type | Select RDS inst ance. |

| Transmission S |   |   |
|---|---|---|
|   | ervice User Guide·Data migratio |   |
| Section | Parameter | Description |
| Destinatio n Database | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination RDS instance. |
|   | Database Name | Enter the name of the destination database. Not e The name of the destination database can be different from the name of the source database. |
|   | Database Account | Enter the database account of the destination RDS instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Paramet er | Description |
|---|---|
| Migratio n Types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Paramet er | Description |
|---|---|
| Objects | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. After an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.2 Migrate incremental data from a user-created SQL Server database to an ApsaraDB RDS for SQL Server instance

created SQL Server database to an ApsaraDB RDS for SQL Server instance This topic describes how to migrate incremental data from a user-created SQL Server database to an ApsaraDB RDS for SQL Server instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The version of the user-created SQL Server database is 2005, 2008, 2008 R2, 2012, 2014, or 2016.

> Not e
> DTS does not support SQL Server clusters or SQL Server Always On availability groups (AOAG).
> If the version of the source database is 2005, incremental data migration is not supported.
> If you migrate data between different versions of databases, make sure that the database versions are compatible.

The tables to be migrated from the user-created SQL Server database must have primary keys or UNIQUE NOT NULL indexes. Precautions During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. To ensure that the incremental data migration task runs as expected, do not frequently back up the source database. We recommend that you retain log files for more than three days. Otherwise, you cannot retrieve log files after they are truncated. To ensure that the delay time of incremental data migration is accurate, DTS adds a heartbeat table to the user-created SQL Server database. The name of the heartbeat table is `Source table name_dt`

```
s_mysql_heartbeat .
```

DTS automatically creates a destination database in the ApsaraDB RDS for SQL Server instance. However, if the name of the source database is invalid, you must manually create a database in the ApsaraDB RDS for SQL Server instance before you configure the data migration task. If a data migration task fails, DTS automatically resumes the task. Before you switch your workloads to the destination instance, stop or release the data migration task. Otherwise, the data in the source database will overwrite the data in the destination instance after the task is resumed. Limits A single data migration task can migrate incremental data from only one database. To migrate incremental data from multiple databases, you must create a data migration task for each database. DTS cannot migrate the schemas of assemblies, service brokers, full-text indexes, full-text catalogs, distributed schemas, distributed functions, CLR stored procedures, CLR scalar-valued functions, CLR table-valued functions, internal tables, systems, or aggregate functions. DTS cannot migrate data of the sql_variant type. DTS cannot migrate tables that contain computed columns. Migration types Schema migration DTS migrates the schemas of the required objects to the destination instance. DTS supports schema migration for the following types of objects: table, view, trigger, synonym, SQL stored procedure, SQL function, plan guide, user-defined type, rule, and default. Full data migration DTS migrates historical data of the required objects from the user-created SQL Server database to the destination ApsaraDB RDS for SQL Server instance. Incremental data migration After full data migration is complete, DTS migrates incremental data from the user-created SQL Server database to the destination ApsaraDB RDS for SQL Server instance. Incremental data migration allows you to ensure service continuity when you migrate data from a user-created SQL Server database to Alibaba Cloud. SQL operations that can be synchronized during incremental data migration INSERT, UPDATE, and DELETE

> Not e DTS cannot synchronize the UPDATE operations that update only the large fields.

CREATE TABLE

> Not e If a CREATE TABLE operation creates a partition table or a table that contains functions, DTS does not synchronize the CREATE TABLE operation.

ALTER TABLE operations, including only ADD COLUMN, DROP COLUMN, and RENAME COLUMN DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX Migration process To avoid data migration failures caused by dependencies among objects, DTS migrates the schemas and data from the source SQL Server database in the following order:
1. Migrate the schemas of tables, views, synonyms, user-defined types, rules, defaults, and plan
guides.
2. Perform full data migration.
3. Migrate the schemas of SQL stored procedures, SQL functions, triggers, and foreign keys.
4. Perform incremental data migration.

> Not e During schema migration and full data migration, do not perform data definition language (DDL) operations on the required objects. Otherwise, the objects may fail to be migrated.

Before you begin Before you configure a data migration task, configure log settings on the user-created SQL Server database.

> Not e Skip this step if you do not need to perform incremental data migration.

1. Run the following command in the user-created SQL Server database to change the recovery mode
to full mode:

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
2. Run the following command to create a logical backup for the source database. Skip this step if
you have already created a logical backup.

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

`GO` Procedure
1. Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | Select an instance type based on where the source database is deployed. In this example, select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select SQL Server. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created SQL Server database. In this example, enter the public IP address. |
|   | Port Number | Enter the service port number of the user-created SQL Server database. The default port number is 1433. |

| Section | Parameter | Description |
|---|---|---|
|   | Database Account | Enter the account that is used to log on to the user-created SQL Server database. Not e To perform incremental data migration, the account must have the sysadmin permission. To perform schema migration or full data migration, the account must have the SELECT permission on the objects that you want to migrate. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination ApsaraDB RDS for SQL Server instance. |
|   | Database Account | Enter the database account of the destination ApsaraDB RDS for SQL Server instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrate d | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |

| Setting | Description |
|---|---|
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.3 Migrate data from a user-created MySQL database to an ApsaraDB RDS for MySQL instance

database to an ApsaraDB RDS for MySQL instance This topic describes how to migrate data from a user-created MySQL database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The version of the user-created MySQL database is 5.1, 5.5, 5.6, or 5.7. If you need to perform incremental data migration, you must enable the binary logging feature. The following requirements must be met: The value of the binlog_format parameter is set to row. The value of the binlog_row_image parameter is set to full. Precautions During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. DTS uses the `ROUND(COLUMN,PRECISION)` function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for the FLOAT data type to 38 digits and the precision for the DOUBLE data type to 308 digits. You must check whether the precision settings meet your business requirements. DTS automatically creates a destination database in the ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must manually create a database in the ApsaraDB RDS for MySQL instance before you configure the data migration task. Migration types Schema migration DTS migrates the schemas of the required objects to the destination instance. DTS supports schema migration for the following types of objects: table, view, trigger, stored procedure, and function.

> Not e
> During schema migration, DTS changes the value of the SECURITY attribute in views, stored procedures, and functions from DEFINER to INVOKER.
> DTS does not migrate user information. Before a user can call views, stored procedures, and functions of the destination database, you must grant the read/write permissions to the user.

Full data migration DTS migrates historical data of the required objects from the user-created MySQL database to the destination database in the ApsaraDB RDS for MySQL instance.

> Not e During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination instance. After full data migration is complete, the tablespace of the destination instance is larger than that of the source database.

Incremental data migration After full data migration is complete, DTS retrieves binary log files from the user-created MySQL database. Then, DTS synchronizes incremental data from the user-created MySQL database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from a user-created MySQL database to Alibaba Cloud. SQL operations that can be synchronized during incremental data migration

| Operation type | SQL statements |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |

| Operation type | SQL statements |
|---|---|
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE TRUNCATE TABLE |

Procedure
1. Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
|   | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address. |

| Transmission S |   |   |
|---|---|---|
|   | ervice User Guide·Data migratio |   |
| Section | Parameter | Description |
| Source Database | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select MySQL. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created MySQL database. |
|   | Port Number | Enter the service port number of the user-created MySQL database. The default port number is 3306. |
|   | Database Account | Enter the account of the user-created MySQL database. To perform incremental data migration, the account must have the SELECT permission on the required objects, the REPLICATION SLAVE permission, the REPLICATION CLIENT permission, and the SHOW VIEW permission. To perform schema migration or full data migration, the account must have the SELECT permission on the required objects. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination RDS instance. |
|   | Database Account | Enter the database account of the destination RDS instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Setting | Description |
|---|---|
| Select the objects to be migrate d | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.4 Migrate data from a user-created MySQL database to a Cloud Native Distributed Database PolarDB-X instance

database to a Cloud Native Distributed Database PolarDB-X instance This topic describes how to migrate data from a user-created MySQL database to a Cloud Native Distributed Database PolarDB-X instance by using Data Transmission Service (DTS). Cloud Native Distributed Database PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). Precautions DTS cannot migrate schemas from a user-created MySQL database to a Cloud Native Distributed Database PolarDB-X instance.

> Not e During schema migration, DTS migrates the schemas of the required objects, such as tables, from the source database to the destination database.

During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. DTS uses the `ROUND(COLUMN,PRECISION)` function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for the FLOAT data type to 38 digits and the precision for the DOUBLE data type to 308 digits. You must check whether the precision settings meet your business requirements. SQL operations that can be synchronized during incremental data migration INSERT, UPDATE, DELETE, and REPLACE Permissions required for database accounts

| Database | Full data migration | Incremental data migration |
|---|---|---|
| User-created MySQL database | The SELECT permission | The REPLICATION SLAVE, REPLICATION CLIENT, SHOW VIEW, and SELECT permissions |
| Cloud Native Distributed Database PolarDB-X | The read and write permissions | The read and write permissions |

Procedure
1. Create databases and tables in the destination PolarDB-X instance based on the schemas of the
source tables.
2. Create a data migration instance.
3. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select MySQL. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created MySQL database. |
|   | Port Number | Enter the service port number of the user-created MySQL database. The default port number is 3306. |
|   | Database Account | Enter the account of the user-created MySQL database. For more information about the permissions that are required for the account, see Permissions required for database accounts. |
| ument Version | : 20220928 3 |   |

|   | gration | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | Enter the password of the source database account. |
|   | Instance Type | Select DRDS Inst ance. |
| Destinatio n Database |   |   |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the Cloud Native Distributed Database PolarDB-X instance. |
|   | Database Name | Enter the name of the destination database. |
|   | Database Account | Enter the database account of the Cloud Native Distributed Database PolarDB-X instance. For more information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Database Password | Enter the password of the destination database account. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. Select the migration types and the objects to be migrated.

| Paramet er | Description |
|---|---|
| Migratio n Types | To perform only full data migration, select Full Dat a Migrat ion. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Paramet er | Description |
|---|---|
| Objects | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |

7. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

8. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.5 Migrate data from an ApsaraDB RDS for MySQL instance to a user-created Oracle database

MySQL instance to a user-created Oracle database This topic describes how to migrate data from an ApsaraDB RDS for MySQL instance to a user-created Oracle database by using Data Transmission Service (DTS). DTS supports full data migration and incremental data migration. You can select these migration types to ensure service continuity of the source ApsaraDB RDS for MySQL instance during data migration. Prerequisites The destination Oracle database is created. The schema of the Oracle database is the same as the schema of the source database in the ApsaraDB RDS for MySQL instance. This is because DTS does not support schema migration from an ApsaraDB RDS for MySQL instance to a user-created Oracle database. Permissions required for database accounts

| Migration type | Full data migration | Incremental data migration |
|---|---|---|
| Source ApsaraDB RDS for MySQL instance | The read and write permissions | The read and write permissions |
| Destination Oracle database | The read and write permissions | The read and write permissions |

Procedure
1. Create a data migration instance.
2. In the migration task list, find the instance that you created, and click Conf igure Migrat ion T ask
in the Actions column.
3. Optional. Enter a name for the task.
DTS automatically generates a name for each task. Duplicate task names are allowed. You can edit the task name based on your needs. We recommend that you specify an informative name for easy identification.
4. Configure the source and destination databases. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
|   | Instance Type | Select RDS Inst ance as the type of the source instance. |

| Guide·Data migration |   | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
| Source Database | Instance Region | The region where the source instance resides. |
|   | RDS Instance ID | Select the ID of the source RDS instance. |
|   | Database Account | Enter an account that has the read and write permissions on the source database. |
|   | Database Password | Enter the password of the source database account. |
| Destination Database | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address as the type of the destination database. |
|   | Instance Region | The region where the destination instance resides. |
|   | Database Type | Select Oracle. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the Oracle database. |
|   | Port Number | The default port number is 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this option, you must specify the SID. RAC Inst ance: If you select this option, you must specify the Service Name. |
|   | Database Account | Enter an account that has the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

5. Click T est Connect ivit y and confirm that the test results for both the source and destination
databases are Passed.
6. In the lower-right corner of the page, click Set Whit elist and Next .
7. Select the migration types based on your needs. Select objects from the Available section and click
the icon to move the objects to the Select ed section. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. To perform only full data migration, select Full Dat a Migrat ion.
8. Click Precheck and wait until the precheck is complete.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

9. Click Next to start the migration task.

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.6 Migrate data between user-created Oracle databases

databases This topic describes how to migrate data between user-created Oracle databases by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The version of the source Oracle database is 9i, 10g, 11g, or 12c.

> Not e To ensure compatibility, make sure the versions of the source and destination databases are the same.

Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the source Oracle database. For more information, see Supplemental Logging. The ARCHIVELOG mode is enabled for the source Oracle database. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. The available storage space of the destination Oracle database is larger than the total size of the data in the source Oracle database. Migration types

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of the required objects to the destination Oracle database. DTS supports schema migration for the following types of objects: table, view, synonym, trigger, stored procedure, function, package, and user- defined type. Not e If an object contains triggers, the data between the source and destination databases will become inconsistent. |

| Migration type | Description |
|---|---|
| Full data migration | DTS migrates historical data of the required objects from the source Oracle database to the destination Oracle database. Not e During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration, DTS retrieves redo log files from the source Oracle database. Then, DTS synchronizes incremental data from the source Oracle database to the destination Oracle database. Incremental data migration allows you to ensure service continuity when you migrate data between Oracle databases. |

Permissions required for database accounts

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source Oracle database | The owner permission on schemas | The owner permission on schemas | SYSDBA |
| Destination Oracle database | The owner permission on schemas | The owner permission on schemas | The owner permission on schemas |

> Not e For more information about how to create and authorize an Oracle database account, see CREATE USER and GRANT.

Procedure
1. Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
|   | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select Oracle. |

|   | ervice | User Guide·Data migratio |
|---|---|---|
| Transmission S |   |   |
| Section | Parameter | Description |
| Source Database | Hostname or IP Address | Enter the endpoint that is used to connect to the source Oracle database. |
|   | Port Number | Enter the port number of the source Oracle database. The default port number is 1521. |
|   | Instance Type | Select Non-RAC Inst ance or RAC Inst ance based on the architecture of the source Oracle database. |
|   | SID | Enter the system ID (SID) of the destination Oracle database. Not e This parameter is required if you select Non-RAC Inst ance as the instance type. |
|   | Service Name | Enter the server name of the instance. Not e This parameter is required if you select RAC Inst ance as the instance type. |
|   | Database Account | Enter the account that is used to connect to the source Oracle database. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n D t b | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select Oracle. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the destination Oracle database. |
|   | Port Number | Enter the port number of the destination Oracle database. The default port number is 1521. |
|   | Instance Type | Select Non-RAC Inst ance or RAC Inst ance based on the architecture of the destination Oracle database. |

| Database Section | Parameter | Description |
|---|---|---|
|   | SID | Enter the SID of the destination Oracle database. Not e This parameter is required if you select Non-RAC Inst ance as the instance type. |
|   | Service Name | Enter the server name of the instance. Not e This parameter is required if you select RAC Inst ance as the instance type. |
|   | Database Account | Enter the account that is used to connect to the destination Oracle database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrate d | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.7 Migrate data from a user-created Oracle database to an ApsaraDB RDS for MySQL instance

database to an ApsaraDB RDS for MySQL instance This topic describes how to migrate data from a user-created Oracle database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. When you migrate data from a user-created Oracle database, you can select all of the supported migration types to ensure service continuity. Prerequisites The version of the user-created Oracle database is 9i, 10g, 11g, or 12c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the user-created Oracle database. For more information, see Supplemental Logging. The ARCHIVELOG mode is enabled for the user-created Oracle database. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Precautions During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. Table names in the ApsaraDB RDS for MySQL instance are case-insensitive. If a table name in the usercreated Oracle database contains uppercase letters, ApsaraDB RDS for MySQL converts all uppercase letters to lowercase letters before creating the table. If the source Oracle database contains identical table names that differ only in capitalization, these table names are identified as duplicate. During schema migration, the following message is returned: The object already exists. To avoid name conflicts in the destination database, you can change the names of the migrated objects by using the object name mapping feature. For more information, see Object name mapping. Migration types Schema migration DTS supports schema migration for tables and indexes. DTS does not support schema migration for the following types of objects: view, synonym, trigger, stored procedure, function, package, and user-defined type. DTS has the following limits on schema migration for tables and indexes: Schema migration of nested tables is not supported. Clustered tables and index-organized tables (IOTs) are converted into common tables in the destination database. Schema migration of function-based indexes, domain indexes, bitmap indexes, and reverse indexes is not supported. Full data migration DTS migrates historical data of the required objects from the user-created Oracle database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration DTS retrieves redo log files from the user-created Oracle database. Then, DTS synchronizes incremental data from the user-created Oracle database to the destination database in the ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from the user-created Oracle database to the destination database. SQL operations that can be synchronized during incremental data migration INSERT, DELETE, and UPDATE CREATE TABLE

> Not e If a CREATE TABLE operation creates a table that contains functions, DTS does not synchronize the CREATE TABLE operation.

ALTER TABLE, ADD COLUMN, DROP COLUMN, RENAME COLUMN, and ADD INDEX DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX Data type mappings For more information, see Data type mappings between heterogeneous databases. Procedure
1. Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
|   | Instance Type | Select an instance type based on where the source database is deployed. In this example, select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |

|   | gration | Data Transmission Servic |
|---|---|---|
| Guide·Data mi |   |   |
| Section | Parameter | Description |
| Source Database | Database Type | Select Oracle. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created Oracle database. |
|   | Port Number | Enter the service port number of the user-created Oracle database. The default port number is 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this option, you must specify the SID. RAC Inst ance: If you select this option, you must specify the Service Name. |
|   | Database Account | Enter the account of the user-created Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permission. To perform schema migration or full data migration, the account must have the owner permission on schemas. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination RDS instance. |
|   | Database Account | Enter the database account of the destination RDS instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrate d | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.8 Migrate data from a user-created Oracle database to a PolarDB cluster

database to a PolarDB cluster This topic describes how to migrate data from a user-created Oracle database to a PolarDB cluster by using Data Transmission Service (DTS). PolarDB is formerly known as ApsaraDB RDS for PPAS. DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The version of the user-created Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the user-created Oracle database. For more information, see Supplemental Logging. The user-created Oracle database is running in ARCHIVELOG mode. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Precautions During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. DTS supports schema migration for the following types of objects: table, view, synonym, trigger, stored procedure, function, package, and user-defined type. Limits During schema migration, the reverse indexes and bitmap indexes of the source database are stored as common indexes in the PolarDB cluster. During schema migration, partitioned indexes are converted into independent indexes on each partition in the PolarDB cluster. Incremental data migration supports only tables that have primary keys or UNIQUE NOT NULL indexes. Incremental data migration does not support the LONG data type. Data definition language (DDL) operations that are performed during incremental data migration cannot be synchronized to the destination database. Materialized views cannot be migrated. Data type mappings For more information, see Data type mappings between heterogeneous databases. Procedure
1. Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | Select an instance type based on where the source database is deployed. In this example, select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select Oracle. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created Oracle database. |
|   | Port Number | Enter the service port number of the user-created Oracle database. The default port number is 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this option, you must specify the SID. RAC Inst ance: If you select this option, you must specify the Service Name. |
|   | Database Account | Enter the account of the user-created Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permission. To perform schema migration or full data migration, the account must have the owner permission on schemas. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination RDS instance. |
|   | Database Name | Enter the name of the destination database. |

|   | gration | Data Transmission Servic |
|---|---|---|
| Database |   |   |
| Section | Parameter | Description |
|   | Database Account | Enter the database account of the destination RDS instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrate d | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |

| Setting | Description |
|---|---|
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### 3.3.9 Migrate data from a user-created Oracle database to a Cloud Native Distributed Database PolarDB-X instance

database to a Cloud Native Distributed Database PolarDB-X instance This topic describes how to migrate data from a user-created Oracle database to a Cloud Native Distributed Database PolarDB-X instance by using Data Transmission Service (DTS). Cloud Native Distributed Database PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). DTS allows you to ensure service continuity when you migrate both historical data and incremental data. Prerequisites The version of the user-created Oracle database is 9i, 10g, 11g, or 12c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the user-created Oracle database. For more information, see Supplemental Logging. The ARCHIVELOG mode is enabled for the user-created Oracle database. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Precautions DTS cannot migrate schemas from a user-created Oracle database to a Cloud Native Distributed Database PolarDB-X instance.

> Not e During schema migration, DTS migrates the schemas of the required objects, such as tables, from the source database to the destination database.

During full data migration, DTS uses read and write resources of the source and destination databases. This may increase the loads of the database servers. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. Migration types Full data migration DTS migrates historical data of the required objects from the source Oracle database to the destination database. Incremental data migration After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS synchronizes incremental data from the source Oracle database to the destination database.

> Not e The following SQL operations can be synchronized during incremental data migration: INSERT, DELETE, and UPDATE operations. Data definition language (DDL) operations cannot be synchronized during incremental data migration.

Procedure
1. Create databases and tables in the destination PolarDB-X instance based on the schemas of the
source tables.

> Not e The data types of Oracle databases and PolarDB-X instances do not have one-to- one correspondence. You must create the corresponding data types in PolarDB-X instances. For more information, see Data type mappings between heterogeneous databases.

2. Create a data migration instance.
3. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |

| Transmission S | ervice | User Guide·Data migratio |
|---|---|---|

| Section | Parameter | Description |
|---|---|---|
| Source Database | Instance Type | Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | Select Oracle. |
|   | Hostname or IP Address | Enter the endpoint that is used to connect to the user-created Oracle database. In this example, enter the public IP address. |
|   | Port Number | Enter the service port number of the user-created Oracle database. The default port number is 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this option, you must specify the SID. RAC Inst ance: If you select this option, you must specify the Service Name. |
|   | Database Account | Enter the account of the user-created Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permission. To perform schema migration or full data migration, the account must have the owner permission on schemas. |
|   | Database Password | Enter the password of the source database account. |
| Destinatio n Database | Instance Type | Select DRDS Inst ance. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the destination Cloud Native Distributed Database PolarDB-X instance. |
|   | Database Account | Enter the database account of the destination Cloud Native Distributed Database PolarDB-X instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select the migratio n types | To perform only full data migration, select only Full Dat a Migrat ion. To ensure service continuity during data migration, select both Full Dat a Migrat ion and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrate d | Select one or more objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature on an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time for failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time based on your needs. If DTS reconnects to the source and destination databases within the specified time, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e When DTS retries a connection, you are charged for the DTS instance. We recommend that you specify the retry time based on your business needs. You can also release the DTS instance at your earliest opportunity after the source and destination instances are released. |

7. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

8. After the task passes the precheck, click Next .

> Not e If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

### 3.4 Manage data migration tasks

#### 3.4.1 Object name mapping

Data Transmission Service (DTS) provides the object name mapping feature. You can use this feature to change the names of one or more objects that are migrated to the destination instance. This topic describes how to use the object name mapping feature when you configure a data migration task. Limits You can use the object name mapping feature only when a data migration task is configured and the current step is Conf igure Migrat ion T ypes and Object s.

> Not e Do not use the object name mapping feature after a data migration task is started. Otherwise, data may fail to be migrated.

Procedure
1. In the Conf igure Migrat ion T ypes and Object s step, move the required objects to the
Select ed section, move the pointer over a database or table, and then click Edit .
2. In the dialog box that appears, specify a name for the object in the destination instance.
Database name mapping In the Edit Dat abase Name dialog box that appears, enter the database name that you want to use in the destination instance. Table name mapping In the Edit T able dialog box that appears, enter the table name that you want to use in the destination instance. Column name mapping In the Edit T able dialog box that appears, enter a new name for each column.

> Not e In this step, you can clear the options of columns that do not need to be synchronized.

3. Click OK.
4. Configure other parameters that are required for the data migration task.

#### 3.4.2 Specify an SQL condition to filter data

This topic describes how to specify an SQL condition to filter the data of a specific table when you configure a data migration task. The SQL condition takes effect only within the table that you select. DTS migrates only the data that meets the SQL condition to the destination database. This feature is applicable to scenarios such as regular data migration and table partitioning. Limits An SQL condition applies only to full data migration. If you select increment al dat a migrat ion as the migration type, the SQL condition does not filter incremental data. Specify an SQL condition You can specify an SQL condition in the Conf igure Migrat ion T ypes and Object s step when you configure a data migration task. To filter the data of a specific table by using an SQL condition, you must select the table as the object that you want to migrate. You cannot select a database as the object. To specify an SQL condition, perform the following steps. Procedure
1. In the Conf igure Migrat ion T ypes and Object s step, move the pointer over a table in the
Select ed section. The Edit button appears, as shown in Edit button. Edit button
2. Click Edit . The Edit Table dialog box appears.
Modif y an SQL condit ion The SQL conditions in DTS are the same as the standard SQL WHERE conditions for databases. You can use SQL conditions to perform operations and run basic functions. Enter an SQL condition in the text box. For example, you can enter id>1000 to migrate the records whose IDs are greater than 1,000 to the destination instance, as shown in Modify an SQL condition. Modify an SQL condition After the SQL condition is specified, click OK.

#### 3.4.3 Troubleshoot a failed data migration task

This topic describes how to troubleshoot a failed data migration task. You can use this feature if your data migration task is in the Migrat ion Failed state during schema migration or full data migration. Troubleshoot a failed task during schema migration DTS supports data migration between heterogeneous data sources. However, if you migrate data of unsupported types to the destination instance during schema migration, the task may fail.
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. Use one of the following methods to troubleshoot the failed task:
Method 1 a. Find the task and click View Cause and Rect if y. b. Troubleshoot the issue based on the cause that is displayed in the View Cause and Rectify message. For example, you can troubleshoot an issue by modifying the schema syntax. c. Click Rest art T ask. Method 2 a. Click the instance ID or task name. b. In the left-side navigation pane, choose Migrat ion Det ails > Schema Migrat ion. c. On the Schema Migrat ion page, find the object that causes the migration failure and click Rect if y in the Status column. d. Troubleshoot the issue based on the cause that is displayed in the Rect if y dialog box. For example, you can troubleshoot an issue by modifying the schema syntax. e. Click Rect if y.

> Not e
> If the failure persists, the Rect if y dialog box does not close and shows the failure cause. You must continue troubleshooting based on the failure cause until the troubleshooting is successful.
> If the troubleshooting is successful, the Schema Migrat ion page appears and the status of the object changes to Finished.

4. If no objects are in the Failed state, DTS proceeds with the data migration task, for example,
entering the full data migration process. Troubleshoot a failed task during full data migration
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. Find the task and click View Cause and Rect if y.
DTS allows you to troubleshoot a task that fails during full data migration due to the following reasons.

> Not e If a task fails during full data migration due to other reasons, DTS provides only the Ignore option. The object that causes the failure is not migrated to the destination database.

The connection to the source or destination database failed or timed out. Troubleshoot the issue, make sure that the connection is successful, and then click Rest art T ask. The storage space of the destination instance is insufficient or the instance is locked. Upgrade the specification of the destination instance or clear the log space, and then click Rest art T ask. MyISAM tables in the source database are corrupted. Troubleshoot the issue in the source database, and then click Rest art T ask.
4. In the dialog box that appears, troubleshoot the issue based on the failure cause.
5. Click Rest art T ask.

### 3.5 Precheck items

#### 3.5.1 Source database connectivity

DTS checks whether DTS servers can connect to the source database. DTS creates a connection to the source database by using the JDBC protocol. If the connection fails, the data migration task fails to pass the connectivity check. The migration task may fail to pass the connectivity check because of the following reasons: The database account or password that is specified in the data migration task is invalid. Troubleshooting: Find a server that can connect to the source database. On the server, enter the database account and password that are specified in the data migration task to check whether the account and password are valid. If the database account or password is invalid, the following error message is displayed: Access deny. Solution: Log on to the DTS console, modify the database account and password, and then run a precheck again. The DTS servers are disallowed to access the source database. Troubleshooting: Find a server that can connect to the source database. On the server, enter the database account and password that are specified in the data migration task to check whether the connection is successful. Only authorized DTS servers can connect to the source database. If the CIDR block of a DTS server is not included in the whitelist of the source database, the DTS server cannot connect to the source database. If the source database is a MySQL database, use a MySQL client to connect to the database and run the SELECT HOST FROM mysql.user WHERE user='Account', password='Password'; command. If the CIDR blocks of DTS servers are not included in the whitelist of the source database, the query result of the preceding command is not %. Solution: If the source database is a MySQL database, run the GRANT ALL ON . TO 'Account'@''%' IDENTIFI ED BY 'Password'; command to authorize the database account. Replace Account and Password in the preceding command with your database account and password. After the account is authorized, run a precheck again. A firewall is configured on the source database server. Troubleshooting: If the server where the source database resides runs Linux, run the `iptables -L` command in the shell to check whether a firewall is configured for the server. If the server where the source database resides runs Windows, find Windows Defender Firewall from the Control Panel and check whether a firewall is configured for the server. Solution: Disable the firewall and run a precheck again. The network between DTS servers and the source database is unavailable. If the failure persists, you can check whether the network between DTS servers and the source database is available. In this case, we recommend that you contact Alibaba Cloud engineers by submitting a ticket.

#### 3.5.2 Check the destination database connectivity

connectivity This check item checks whether the DTS server can connect to the destination database for migration. DTS creates a connection to the destination database by using the JDBC protocol. If the connection fails, the check item fails. The destination database connectivity precheck may fail for the following reasons: An incorrect account or password is provided when a migration task is created. Diagnostics: On any network-ready server that can connect to the destination database, use the account and password specified for creating the migration task to connect to the destination database through client software. Check whether the connection succeeds. If an error is reported for the connection and the error message contains Access deny, the account or password is incorrect. Troubleshooting: Modify the migration task in the DTS console, correct the account and password, and perform the precheck again. There is no connectivity between the DTS server and destination database. If you check that the password and account are correct, the check item may fail because there is no connectivity between the DTS server and the destination database. In this case, contact the DTS engineers on duty.

#### 3.5.3 Binary logging configurations of the source database

database Whether binary logging is enabled in the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether binary logging is enabled in the source database. If binary logging is disabled in the source database, the check result is Failed. Troubleshooting: Run the `log_bin=mysql_bin` command to modify the configuration file of the source database. Restart the source database and run a precheck again. Binary log format of the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the binary log format is set to ROW in the source database. If the binary log format is not set to ROW in the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_format=ROW` command in the source database and run a precheck again. We recommend that you restart the MySQL process. Otherwise, data loss may occur because sessions will continue to be written in a non-ROW mode. Binary log files in the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether specific binary log files are removed from the source database. If binary log files in the source database are incomplete, the check result is Failed. Troubleshooting: Run the `PURGE BINARY LOGS TO 'The name of the first binary log file that is` `not deleted'` command in the source database and run a precheck again. To find the binary log files that are removed from the source database, click the info icon next to the failed item. In the View Det ails dialog box, the names of deleted binary log files are displayed. Parameter binlog_row_image of the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of the binlog_row_image parameter in the source database is set to FULL. This parameter indicates whether the full image is recorded. If the full image is not recorded in binary log files of the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_row_image=FULL` command in the source database and run a precheck again.

#### 3.5.4 Integrity of the FOREIGN KEY constraints

DTS checks whether the parent table on which a child table depends is included in the selected objects. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. If the parent table on which a child table depends is not included in the selected objects, the check result is Failed. Troubleshooting: Do not migrate the child tables that cause the check failure. To do this, remove these child tables from the selected objects and run a precheck again. Migrate the parent tables rather than the child tables. To do this, add the parent tables to the selected objects and run a precheck again. Delete the foreign key dependencies between the parent and child tables in the source database and run a precheck again.

#### 3.5.5 Existence of FEDERATED tables

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the source database contains storage engines that are not supported by incremental data migration. Incremental data migration does not support the FEDERATED and MRG_MyISAM storage engines. If t he FEDERAT ED st orage engine is used by specif ic t ables in t he source dat abase, the check result is Failed. If t he MRG_MyISAM st orage engine is used by specif ic t ables in t he source dat abase, the check result is Failed. Solution: Remove the tables that use the FEDERATED or MRG_MyISAM storage engine from the selected objects. Then, create a separate migration task to perform schema migration and full data migration for these tables.

#### 3.5.6 Permissions

Source database permissions DTS checks whether the account of the source database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks. Destination database permissions DTS checks whether the account of the destination database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks.

#### 3.5.7 Object name conflict

This check item checks for duplicate object names in the destination and source database. If this check item fails, an object in the destination RDS instance has the same name as an object to be migrated. This causes the migration to fail. When this check item fails, an error message is displayed indicating that an object in the destination database has the same name as an object to be migrated from the source database. Troubleshooting: Use the database and table name mapping feature provided by DTS to migrate the object to be migrated to another object with a different name in the destination database. In the destination database, delete or rename the object that has the same name as the object to be migrated. Modify the migration task and delete that object to be migrated from the list of objects to be migrated. Do not migrate this object.

#### 3.5.8 Schema existence

This check item checks whether the database to be migrated exists in the destination RDS instance. If no, DTS creates one automatically. However, under the following circumstances, the automatic database creation fails, and this check item prompts a failure: The database name contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). The cause of the precheck failure is that the name of the source dat abase does not comply with the requirements of RDS. Troubleshooting: On the database management page of the RDS console, create a database that complies with the requirements of RDS and grant the migration account the read and write permissions on the new database. Use the database name mapping feature provided by DTS to map the source database to the new database. Then, perform the precheck again. The character set of the database is not UTF8, GBK, Latin1, or UTF-8MB4. The cause of the precheck failure is that the character set of the source dat abase does not comply with the requirements of RDS. Troubleshooting: On the database management page of the RDS console, create a database that complies with the requirements of RDS and grant the migration account the read and write permissions on the new database. If the new database and the database to be migrated have different names, you can use the database name mapping feature of DTS to map the database to be migrated to the new database. Then re-run the precheck. The migration account of the destination database has no read and write permissions on the database to be migrated. The cause of the precheck failure is that you are not authorized to operate on the source dat abase. Troubleshooting: On the database management page of the RDS console, click the Account Management tab. Grant the migration account the read and write permissions on the source database. Then, perform the precheck again.

#### 3.5.9 Value of server_id in the source database

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of server-id in the source database is set to an integer greater than 1. If the check result is Failed, run the `set global server_id='An integer greater than 1'` command in the source database and perform a precheck again.

#### 3.5.10 Source database version

DTS checks whether the version of the source database is supported. The table lists the source database versions that are supported by DTS. Source database types and versions

| Source database type | Supported version |
|---|---|
| MySQL | 5.0, 5.1, 5.5, 5.6, and 5.7. Only 5.1, 5.5, 5.6, and 5.7 are supported for incremental data migration. |

If the check result is Failed, you must upgrade or downgrade the source database to a supported version before you perform a precheck again.

### 3.6 Data type mappings between heterogeneous databases

heterogeneous databases Heterogeneous databases support different data types. During schema migration, Data Transmission Service (DTS) converts the data types of the source database into those of the destination database. This topic lists the data type mappings for you to evaluate the impact of data migration on your business. Data migration from a user-created Oracle database to a usercreated MySQL database or an ApsaraDB RDS for MySQL instance

| Data type in the Oracle database | Data type in the MySQL database | Supported by DTS |
|---|---|---|
| varchar2(n [char/byte]) | varchar(n) | Yes |
| nvarchar2[(n)] | national varchar[(n)] | Yes |
| char[(n [byte/char])] | char[(n)] | Yes |
| nchar[(n)] | national char[(n)] | Yes |
| number[(p[,s])] | decimal[(p[,s])] | Yes |
| float(p)] | double | Yes |
| long | longtext | Yes |
| date | datetime | Yes |
| binary float _ | decimal(65,8) | Yes |
| binary double _ | double | Yes |
| timestamp[(fractional seconds precision)] _ _ | datetime[(fractional seconds precisi _ _ on)] | Yes |
| timestamp[(fractional seconds precision)]with _ _ localtimezone | datetime[(fractional seconds precisi _ _ on)] | Yes |
| timestamp[(fractional seconds precision)]with _ _ localtimezone | datetime[(fractional seconds precisi _ _ on)] | Yes |
| clob | longtext | Yes |
| nclob | longtext | Yes |
| blob | longblob | Yes |
| raw | varbinary(2000) | Yes |
| long raw | longblob | Yes |
| bfile | N/A | No |
| interval year(year precision) to month _ | N/A | No |
| interval day(day precision)to _ second[(fractional seconds precision)] _ _ | N/A | No |

> Not e
> A char column with a length greater than 255 bytes is converted to the varchar(n) type.
> Data types such as bfile, interval year to month, and interval day to second in Oracle databases are not supported in MySQL databases. They cannot be converted to data types supported by the destination database during schema migration.
> The schema migration fails if the table to be migrated contains these three data types. You must make sure that columns with these three data types are excluded from the objects to be migrated.
> The timestamp data type of MySQL databases does not contain the time zone information. However, the timestamp with time zone and timestamp with local time zone data types in Oracle databases provide time zone information. Therefore, DTS converts the values of these data types based on the time zone to UTC time for storage in the destination instance.

Data migration from a user-created Oracle database to a PolarDB-X instance

| Oracle data type | PolarDB-X data type | Supported by DTS |
|---|---|---|
| varchar2(n [char/byte]) | varchar(n) | Yes |
| nvarchar2[(n)] | national varchar[(n)] | Yes |
| char[(n [byte/char])] | char[(n)] | Yes |
| nchar[(n)] | national char[(n)] | Yes |
| number[(p[,s])] | decimal[(p[,s])] | Yes |
| float(p)] | double | Yes |
| long | longtext | Yes |
| date | datetime | Yes |
| binary float _ | decimal(65,8) | Yes |
| binary double _ | double | Yes |
| timestamp[(fractional seconds precision)] _ _ | datetime[(fractional seconds precisi _ _ on)] | Yes |
| timestamp[(fractional seconds precision)]with _ _ localtimezone | datetime[(fractional seconds precisi _ _ on)] | Yes |
| timestamp[(fractional seconds precision)]with _ _ localtimezone | datetime[(fractional seconds precisi _ _ on)] | Yes |
| clob | longtext | Yes |

| User Guide·Data migration | Data T | ransmission Servic |
|---|---|---|
| Oracle data type | PolarDB-X data type | Supported by DTS |
| nclob | longtext | Yes |
| blob | longblob | Yes |
| raw | varbinary(2000) | Yes |
| long raw | longblob | Yes |
| bfile | None | No |
| interval year(year precision) to month _ | None | No |
| interval day(day precision)to _ second[(fractional seconds precision)] _ _ | None | No |

> Not e
> If a char field in the Oracle database is greater than 255 bytes in length, DTS converts this field to the varchar(n) type in the PolarDB-X instance.
> The timestamp data type of PolarDB-X does not contain the time zone information. However, the timestamp with time zone and timestamp with local time zone data types in Oracle databases provide the time zone information. Therefore, DTS converts the values of these data types into UTC time in the destination PolarDB-X instance.

Data migration from a user-created Oracle database to a PolarDB cluster

| Oracle data type | PolarDB data type | Supported by DTS |
|---|---|---|
| varchar2(n [char/byte]) | varchar2[(n)] | Yes |
| nvarchar2[(n)] | nvarchar2[(n)] | Yes |
| char[(n [byte/char])] | char[(n)] | Yes |
| nchar[(n)] | nchar[(n)] | Yes |
| number[(p[,s])] | number[(p[,s])] | Yes |
| float(p)] | double precision | Yes |
| long | long | Yes |
| date | date | Yes |
| binary float _ | real | Yes |

| ata Transmission Service | User Guid | e·Data migratio |
|---|---|---|

| Oracle data type | PolarDB data type | Supported by DTS |
|---|---|---|
| binary double _ | double precision | Yes |
| timestamp[(fractional seconds precision)] _ _ | timestamp[(fractional seconds precision)] _ _ | Yes |
| timestamp[(fractional seconds precision)] _ _ with time zone | timestamp[(fractional seconds precision)]wit _ _ h time zone | Yes |
| timestamp[(fractional seconds precision)] _ _ with local time zone | timestamp[(fractional seconds precision)]wit _ _ h time zone | Yes |
| clob | clob | Yes |
| nclob | nclob | Yes |
| blob | blob | Yes |
| raw | raw(size) | Yes |
| long raw | long raw | Yes |
| bfile | None | No |
| interval year(year precision) to month _ | interval year to month | No |
| interval day(day precision) to _ second[(fractional seconds precision)] _ _ | interval day to second[(fractional seconds precision)] _ _ | No |

> Not e PolarDB does not support the timestamp[(fractional_seconds_precision)]with local time zone data type. DTS converts the data of this type into UTC time and then stores the data in the destination PolarDB cluster by using the timestamp[(fractional_seconds_precision)]with time zone data type.

## 4 Data synchronization

### 4.1 Database types, initial synchronization types, and synchronization topologies

synchronization types, and

### synchronization topologies

You can use Data Transmission Service (DTS) to synchronize data between various data sources. This topic describes the database types, initial synchronization types, and synchronization topologies that are supported by DTS.

| Source database | Destination database | Initial synchronization type | Synchronizatio n topology |
|---|---|---|---|
| User-created MySQL database 5.1, 5.5, 5.6, and 5.7 RDS MySQL 5.6 and 5.7 | User-created MySQL database 5.1, 5.5, 5.6, and 5.7 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n Two-way synchronizatio n |
|   | RDS MySQL 5.6 and 5.7 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n Two-way synchronizatio n |
|   | AnalyticDB for MySQL 2.0 and 3.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
|   | AnalyticDB for PostgreSQL 4.3 and 6.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
|   | Datahub | Initial schema synchronization | One-way synchronizatio n |

|   | User Guide·Data synchronizatio |   |   |
|---|---|---|---|
| Source database | Destination database | Initial synchronization type | Synchronizatio n topology |
|   | MaxCompute | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
| Cloud Native Distributed Database PolarDB-X (formerly known as DRDS) | Cloud Native Distributed Database PolarDB-X | Initial full data synchronization | One-way synchronizatio n |
|   | Datahub | Initial schema synchronization | One-way synchronizatio n |
|   | AnalyticDB for MySQL 2.0 and 3.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |

### 4.2 Create a data synchronization instance

instance Before you configure a task to synchronize data, you must create a data synchronization instance. This topic describes how to create a data synchronization instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. In the upper-right corner of the page, click Creat e Synchronizat ion T ask.
4. In the Create DTS Instances dialog box, set the required parameters.

| Parameter | Description |
|---|---|
| Source Inst ance Region | Select the region where the source instance resides. |
| Source Inst ance T ype | Select the type of the source instance. MySQL: a user-created MySQL database or an ApsaraDB RDS for MySQL instance Drds: a Cloud Native Distributed Database PolarDB-X instance (formerly known as DRDS) |

| Parameter | Description |
|---|---|
| Dest inat ion Inst ance Region | Select the region where the destination instance resides. |
| Dest inat ion Inst ance T ype | Select the type of the destination instance. MySQL: a user-created MySQL database or an ApsaraDB RDS for MySQL instance Analyt icDB: AnalyticDB for MySQL MaxComput e Dat aHub Drds: a Cloud Native Distributed Database PolarDB-X instance (formerly known as DRDS) Analyt icDB f or Post greSQL: AnalyticDB for PostgreSQL |
| Synchronizat ion Mode | Two-way synchronization is available only when you select MySQL as the type of both the source and destination instances. |
| Inst ances t o Creat e | Set the number of data synchronization instances that you want to create at a time. The default value is 1. |

> Not e In the Create DTS Instances dialog box, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click Creat e.

### 4.3 Synchronization topologies

The data synchronization feature supports multiple types of synchronization topologies. You can select a topology for your data synchronization instances based on your business requirements. This topic describes the synchronization topologies that are supported by DTS and how to use these topologies. One-way synchronization To ensure data consistency for one-way synchronization, we recommend that you perform only read operations on the objects in the destination instance. Do not modify the objects.

| Topology type | Topology | Description |
|---|---|---|

| Topology type | Topology | Description |
|---|---|---|
| One-way one- to-one synchronizatio n |   | None |
| One-way one- to-many synchronizatio n |   | You must purchase multiple synchronization instances to implement one-way one-to- many synchronization. For example, if you want to synchronize data from Instance A to Instance B, C, and D, you must purchase three synchronization instances. |
| One-way cascade synchronizatio n |   | You must purchase multiple synchronization instances to implement one-way cascade synchronization. For example, if you want to synchronize data from Instance A to Instance B and then from Instance B to Instance C, you must purchase two synchronization instances. |

| Topology type | Topology | Description |
|---|---|---|
| One-way many-to-one synchronizatio n |   | You must purchase multiple synchronization instances to implement one-way many-to- one synchronization. For example, if you want to synchronize data from Instance B, C, and D to Instance A, you must purchase three synchronization instances. Not e To ensure data consistency, you must select different objects for these synchronization instances. |

Two-way synchronization DTS supports two-way data synchronization only between two MySQL databases. DTS does not support two-way data synchronization between multiple MySQL databases.

| Topology type | Topology | Description |
|---|---|---|
| Two-way one- to-one synchronizatio n |   | To ensure data consistency, make sure that records with the same primary key, business primary key, or unique key are updated only on one of the instances. |

### 4.4 Configure data synchronization tasks

tasks

#### 4.4.1 Configure data synchronization between ApsaraDB RDS for MySQL instances

ApsaraDB RDS for MySQL instances This topic describes how to configure one-way data synchronization between ApsaraDB RDS for MySQL instances. Prerequisites The source and destination ApsaraDB RDS for MySQL instances are created. Precautions DTS uses the read and write resources of the source and destination databases during initial full data synchronization. This may increase the load of the database server. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. The tables to be migrated in the source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination instance. After initial full data synchronization, the tablespace of the destination instance is larger than that of the source instance. Supported synchronization topologies DTS supports one-way synchronization and two-way synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized

| Operatio n type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE TRUNCATE TABLE |

Limits Incompatibility with triggers If you select a database as the object and the database contains a trigger that updates a table, data inconsistency may occur. To solve this issue, you must delete the trigger in the destination database. Limits on RENAME TABLE operations RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object and rename the table during data synchronization, the data of this table is not synchronized to the destination database. To avoid this situation, you can select the database to which this table belongs as the object when you configure the data synchronization task. Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set both Source Instance Type and Destination Instance Type to MySQL, and set Synchronization Mode to One-Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
|   | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | Select the ID of the source RDS instance. |

|   | ice User Guide·Data synchronizatio |   |
|---|---|---|
|   | Parameter | Description |
| Source Section Instance |   |   |
| Details | Database Account | Enter the database account of the source RDS instance. Not e If the database engine of the source RDS instance is MySQL 5.6, you do not need to configure the dat abase account or dat abase password. |
|   | Database Password | Enter the password of the source database account. |
|   | Encryption | Select an encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |
| Destination Instance Details | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the source instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | Select the ID of the destination RDS instance. |
|   | Database Account | Enter the database account of the destination RDS instance. Not e If the database engine of the destination RDS instance is MySQL 5.6, you do not need to configure the dat abase account or dat abase password. |
|   | Database Password | Enter the password of the destination database account. |
|   | Encryption | Select an encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the processing mode of conflicting tables, and the objects that you want to synchronize.

| Parameter | Description |
|---|---|
| Processing Mode In Existed Target Table | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain identical table names, the precheck is passed. Otherwise, an error is returned during precheck and the data synchronization task cannot be started. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not guaranteed and your business may be exposed to potential risks. DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial data synchronization. This occurs if the source and destination databases have the same schema. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized or the data synchronization task fails. |

| Parameter | Description |
|---|---|
| Select Objects | Select objects (tables or a database) from the Available section and click the icon to move the objects to the Select ed section. Not e If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. After an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |

6. In the lower-right corner of the page, click Next .
7. Configure initial synchronization.

> Not e Initial synchronization includes initial schema synchronization and initial full data synchronization. If you select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion, DTS synchronizes the schemas and historical data of the required objects before DTS synchronizes incremental data.

8. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

9. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.2 Synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project

for MySQL instance to a MaxCompute project MaxCompute (formerly known as ODPS) is a fast and fully managed computing platform for large-scale data warehousing. MaxCompute can process exabytes of data. This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to a MaxCompute project by using Data Transmission Service (DTS). Precautions DTS uses the read and write resources of the source and destination databases during initial full data synchronization. This may increase the load of the database server. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. You can select only tables as the objects to be synchronized. MaxCompute does not support the PRIMARY KEY constraint. If network errors occur, DTS may synchronize duplicate data records to MaxCompute. SQL operations that can be synchronized Data definition language (DDL) operation: ADD COLUMN Data manipulation language (DML) operations: INSERT, UPDATE, and DELETE Synchronization process
1. Initial schema synchronization
DTS synchronizes the schemas of the required objects from the source database to MaxCompute. During initial schema synchronization, DTS adds the _base suffix to the end of the source table name. For example, if the name of the source table is customer, the name of the table in MaxCompute is customer_base.
2. Initial full data synchronization
DTS synchronizes the historical data of the table from the source database to the destination table in MaxCompute. For example, the customer table in the source database is synchronized to the customer_base table in MaxCompute. The data is the basis for subsequent incremental synchronization.

> Not e The destination table that is suffixed with _base is known as a full baseline table.

3. Incremental data synchronization
DTS creates an incremental data table in MaxCompute. The name of the incremental data table is suffixed with _log, for example, customer_log. Then, DTS synchronizes the incremental data that was generated in the source database to the incremental data table.

> Not e For more information, see Schema of an incremental data table.

Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set Source Instance Type to MySQL, set Destination Instance Type to MaxComput e, and set Synchronization Mode to One-Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Instance Details | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | Select the ID of the source RDS instance. |
|   | Database Account | Enter the database account of the source RDS instance. Not e If the database engine of the source RDS instance is MySQL 5.5 or MySQL 5.6, you do not need to configure the dat abase account or dat abase password. |
|   | Database Password | Enter the password of the source database account. |
|   | Encryption | Select Non-encrypt ed or SSL-encrypt ed. If you select SSL- encrypt ed, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |
| Destination Instance Details | Instance Type | This parameter is set to MaxComput e and cannot be changed. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the MaxCompute project. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. In the lower-right corner of the page, click Next . In this step, the permissions on the MaxCompute
project are granted to the synchronization account.
6. Configure the synchronization policy and objects.
7. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

8. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization. Schema of an incremental data table DTS synchronizes incremental data that is generated in the source MySQL database to the incremental data table in MaxCompute. The incremental data table stores incremental data and specific metadata. The following figure shows the schema of an incremental data table.

> Not e In the example, the `modifytime_year` , `modifytime_month` , `modifytime_day` ,
> `modifytime_hour` , and `modifytime_minute` fields form the partition key.

The following table describes the schema of an incremental data table.

| Field | Description |
|---|---|
| record id _ | The ID of the incremental log entry. Not e The ID auto-increments for each new log entry. If an UPDATE operation is performed, DTS generates two incremental log entries for the operation. The two incremental log entries have the same record ID. |

| Field | Description |
|---|---|
| operation flag _ | The operation type. Valid values: I: an INSERT operation. D: a DELETE operation. U: an UPDATE operation. |
| utc timestamp _ | The operation timestamp. It is also the timestamp of the binary log file. The timestamp is in the UTC format. |
| before flag _ | Indicates whether the column values are pre-update values. Valid values: Y and N. |
| after flag _ | Indicates whether the column values are post-update values. Valid values: Y and N. |

Additional information about the before_flag and after_flag fields For different operation types, the bef ore_f lag and af t er_f lag fields of an incremental log entry are defined as follows: INSERT For an INSERT operation, the column values are the newly inserted record values (post-update values). The value of the before_flag field is N and the value of the after_flag field is Y. UPDATE DTS generates two incremental log entries for an UPDATE operation. The two incremental log entries have the same values for the record_id, operation_flag, and dts_utc_timestamp fields. The second log entry records the pre-update values, so the value of the before_flag field is Y and the value of the after_flag field is N. The second log entry records the post-update values, so the value of the before_flag field is N and the value of the after_flag field is Y. DELETE For a DELETE operation, the column values are the deleted record values (pre-update values). The value of the before_flag field is Y and the value of the after_flag field is N. Merge a full baseline table and incremental data table After a data synchronization task is started, DTS creates a full baseline table and an incremental data table in MaxCompute. You can use SQL statements to merge the two tables. This allows you to obtain the full data at a specific time point. This section describes how to merge data for the customer table. The following figure shows the schema of the customer table.
1. Create a table in MaxCompute based on the schema of the source table. The table is used to store
the merged data. For example, you can obtain full data of the customer table at the `1565944878` time point. Run the following SQL statements to create the required table:

```
CREATE TABLE `customer_1565944878` (
    `id` bigint NULL,
    `register_time` datetime NULL,
    `address` string);
```

> Not e For more information about the data types that are supported by MaxCompute, see MaxCompute User Guide.

2. Run the following SQL statements in MaxCompute to merge the full baseline table and incremental
data table and obtain full data at a specific time point:

```xml
set odps.sql.allow.fullscan=true; insert overwrite table <result_storage_table> select <col1>,
       <col2>,
       <colN>
  from(
select row_number() over(partition by t.<primary_key_column>
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, af
ter_flag, <col1>, <col2>, <colN>
  from(
select incr.record_id, incr.operation_flag, incr.after_flag, incr.<col1>, incr.<col2>,i ncr.<colN>
  from <table_log> incr
 where utc_timestamp< <timestamp>
 union all
select 0 as record_id, 'I' as operation_flag, 'Y' as after_flag, base.<col1>, base.<col 2>,base.<colN>
  from <table_base> base) t) gt
where record_num=1
  and after_flag='Y'
```

> Not e
> <result_storage_table>: the name of the table that stores the merged data.
> <col1>/<col2>/<colN>: the names of the columns in the table to be merged.
> <primary_key_column>: the name of the primary key column in the table to be merged.
> <table_log>: the name of the incremental data table.
> <table_base>: the name of the full baseline table.
> <timestamp>: the timestamp that is generated when full data is obtained.

Run the following SQL statements to obtain full data of the customer table at the `1565944878` time point:

```
set odps.sql.allow.fullscan=true; insert overwrite table customer_1565944878 select id,
       register_time,
       address
  from(
select row_number() over(partition by t.id
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, af
ter_flag, id, register_time, address
  from(
select incr.record_id, incr.operation_flag, incr.after_flag, incr.id, incr.register_tim e, incr.address
  from customer_log incr
 where utc_timestamp< 1565944878
 union all
select 0 as record_id, 'I' as operation_flag, 'Y' as after_flag, base.id, base.register _time, base.address
  from customer_base base) t) gt
 where gt.row_number= 1
   and gt.after_flag= 'Y';
```

3. Query the merged data from the customer_1565944878 table.

#### 4.4.3 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL cluster

for MySQL instance to an AnalyticDB for MySQL cluster AnalyticDB for MySQL is a real-time online analytical processing (RT-OLAP) service that is developed by Alibaba Cloud for online data analysis with high concurrency. This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL cluster by using Data Transmission Service (DTS). After you synchronize data, you can use AnalyticDB for MySQL to build internal business intelligence (BI) systems, interactive query systems, and real-time report systems. Prerequisites The tables that you want to synchronize from the ApsaraDB RDS for MySQL instance contain primary keys. The destination AnalyticDB for MySQL cluster has sufficient storage space. Precautions DTS uses the read and write resources of the source and destination databases during initial full data synchronization. This may increase the load of the database server. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. If the disk space usage of nodes in an AnalyticDB for MySQL cluster reaches 80%, the cluster is locked. We recommend that you estimate the required disk space based on the objects to be synchronized. You must ensure that the destination cluster has sufficient storage space. SQL operations that can be synchronized Data definition language (DDL) operations: CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE, ADD COLUMN, and DROP COLUMN Data manipulation language (DML) operations: INSERT, UPDATE, and DELETE

> Not e We recommend that you do not change the data type of fields in the source table during data synchronization. Otherwise, DTS generates an error message and stops the data synchronization task.

Data type mappings The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-to-one correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table lists the data types that DTS can convert.

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
|---|---|
| BIGINT UNSIGNED | DECIMAL(20,0) |
| BINARY | VARBINARY |
| BIT | VARCHAR |
| BLOB | VARBINARY |

| ata Transmission Service | User Guide·Data synchronizatio |
|---|---|

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
|---|---|
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
| MULTIPOINT | VARBINARY |
| MULTIPOLYGON | VARBINARY |
| NUMBERIC | DECIMAL |
| POINT | VARBINARY |
| POLYGON | VARBINARY |
| SET | VARCHAR |

| ser Guide·Data synchronization | Data Transmission Servic |
|---|---|

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
|---|---|
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

Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set Source Instance Type to MySQL, set Destination Instance Type to Analyt icDB, and set Synchronization Mode to One- Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Instance Details | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | Select the ID of the source RDS instance. |
|   | Database Account | Enter the database account of the source RDS instance. The account must have the REPLICATION CLIENT permission, the REPLICATION SLAVE permission, the SHOW VIEW permission, and the permission to perform SELECT operations on the required objects. Not e If the database engine of the source RDS instance is MySQL 5.5 or MySQL 5.6, you do not need to configure the dat abase account or dat abase password. |
|   | Database Password | Enter the password of the source database account. |
|   | Encryption | Select an encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |

|   | ronization | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
| Destination Instance Details | Instance Type | This parameter is set to Analyt icDB and cannot be changed. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Version | Select 3.0. |
|   | Database | Select the ID of the destination AnalyticDB for MySQL cluster. |
|   | Database Account | Enter the database account of the destination AnalyticDB for MySQL cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and objects.

| Parameter | Description |
|---|---|
| Initial Synchronization | You must select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion in most cases. After the precheck, DTS synchronizes the schemas and data of the required objects from the source instance to the destination cluster. The schemas and data are the basis for subsequent incremental synchronization. |

| Parameter | Description |
|---|---|
| Processing Mode In Existed Target Table | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain identical table names, the precheck is passed. Otherwise, an error is returned during precheck and the data synchronization task cannot be started. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not guaranteed and your business may be exposed to potential risks. DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial data synchronization. This occurs if the source and destination databases have the same schema. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized or the data synchronization task fails. |
| Merge Multi Tables | If you select Yes, DTS adds the dts data source column to each table __ _ _ to record data sources. In this case, DDL operations cannot be synchronized. No is selected by default. In this case, DDL operations can be synchronized. Not e You can merge the data source columns based on tasks rather than tables. To merge only the data source columns of specific tables, you can create two data synchronization tasks. |
| Synchronization Type | Select the types of operations that you want to synchronize based on your business requirements. All operation types are selected by default. Not e Only the INSERT, UPDATE, DELETE, and ADD COLUMN operations can be synchronized. |

| Parameter | Description |
|---|---|
| Select Objects | Select objects (tables or a database) from the Available section and click the icon to move the objects to the Select ed section. Not e If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. After an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |

6. In the lower-right corner of the page, click Next .
7. Specify a type for the tables that you want to synchronize to the destination database.

> Not e After you select Init ial Schema Synchronizat ion, you must specify the t ype, primary key column, and part it ion key column for the tables that you want to synchronize to AnalyticDB for MySQL.

8. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

9. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.4 Synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance

for MySQL instance to an AnalyticDB for PostgreSQL instance This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature allows you to transfer and analyze data with ease. Prerequisites The tables that you want to synchronize contain primary keys. An AnalyticDB for PostgreSQL instance is created. Precautions If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. Only one-way synchronization is supported. Limits You can select only tables as the objects to be synchronized. DTS does not synchronize the schemas of the required objects from the source database to the destination database. DTS does not synchronize the following types of data: JSON, GEOMETRY, CURVE, SURFACE, MULTIPOINT, MULTILINESTRING, MULTIPOLYGON, GEOMETRYCOLLECTION, and BYTEA. SQL operations that can be synchronized Data manipulation language (DML) operations: INSERT, UPDATE, and DELETE Data definition language (DDL) operations: ALTER TABLE, ADD COLUMN, DROP COLUMN, and RENAME COLUMN

> Not e The CREATE TABLE and DROP TABLE operations are not supported. To synchronize data from a new table, you must add the table to the selected objects. For more information, see Add objects to be synchronized.

Term mappings

| Term in ApsaraDB RDS for MySQL | Term in AnalyticDB for PostgreSQL |
|---|---|
| Database | Schema |
| Table | Table |

Create a data structure in the destination instance Create a database, schema, and table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source RDS instance. Configure a data synchronization task
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set Source Instance Type to MySQL, set Destination Instance Type to Analyt icDB f or Post greSQL, and set Synchronization Mode to One-Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronization Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Instance Details | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The region where the source RDS instance resides. |
|   | Instance ID | Select the ID of the source RDS instance. |
|   | Encryption | Select Non-encrypt ed or SSL-encrypt ed. Not e If you select SSL-encrypt ed, you must enable SSL encryption for the RDS instance before you configure the data synchronization task. |
| Destination Instance Details | Instance Type | This parameter is set to Analyt icDB f or Post greSQL and cannot be changed. |
|   | Instance Region | The region where the destination instance resides. |
|   | Instance ID | Select the ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | Enter the name of the destination database. |

| Section | Parameter | Description |
|---|---|---|
|   | Database Account | Enter the database account of the destination AnalyticDB for PostgreSQL instance. Not e The database account must have the SELECT, INSERT, UPDATE, DELETE, COPY, TRUNCATE, and ALTER TABLE permissions. |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Wait until the synchronization account is created. Then, click Next .
6. Configure the synchronization policy and objects.

| Section | Parameter | Description |
|---|---|---|
| Synchronization policy | Initial Synchronization | Select Init ial Full Dat a Synchronizat ion. Not e DTS synchronizes the historical data of the required objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |
|   | Processing Mode In Existed Target Table | Pre-Check and int ercept (Selected by default) Checks the Schema Name Conf lict item and generates an error message if the destination table contains data. Clear T arget T able Skips the Schema Name Conf lict item during the precheck. Clears the data in the destination table before initial full data synchronization. If you want to synchronize your business data after testing the data synchronization task, you can select this mode. Ignore Skips the Schema Name Conf lict item during the precheck. Adds data to the existing data during initial full data synchronization. If you want to synchronize data from multiple tables to one table, you can select this mode. |

|   | User Guide·Data synchronizatio |   |
|---|---|---|
| Section | Parameter | Description |
|   | Synchronization Type | Insert Updat e Delet e Alt erT able Not e Select the types of operations that you want to synchronize based on your business requirements. |
|   | N/A | You can select only tables as the objects to be synchronized. You can use the object name mapping feature to change the names of the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. Not e The CREATE TABLE operation is not supported. To synchronize data from a new table, you must add the table to the selected objects. For more information, see Add objects to be synchronized. |
| Select Objects |   |   |

7. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

8. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.5 Synchronize data between Cloud Native Distributed Database PolarDB-X instances

Distributed Database PolarDB-X instances Cloud Native Distributed Database PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). It is compatible with the MySQL protocol and syntax, and supports automatic sharding, online smooth scaling, auto scaling, and transparent read/write splitting. This topic describes how to synchronize data between Cloud Native Distributed Database PolarDB-X instances by using Data Transmission Service (DTS). Prerequisites The tables that you want to synchronize contain primary keys. Precautions DTS uses the read and write resources of the source and destination databases during initial full data synchronization. This may increase the load of the database server. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. We recommend that you do not change the network type of the Cloud Native Distributed Database PolarDB-X instances during data synchronization.

> Not e After you change the network type of a Cloud Native Distributed Database PolarDB- X instance during data synchronization, you must submit a ticket to resume the data synchronization instance.

We recommend that you do not scale up or down the databases in the Cloud Native Distributed Database PolarDB-X instances. Otherwise, data may fail to be synchronized. Supported synchronization topologies DTS supports the following synchronization topologies: one-way one-to-one synchronization, oneway one-to-many synchronization, one-way cascade synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized The INSERT, UPDATE, and DELETE operations can be synchronized. Before you begin Create a database and tables in the destination instance based on the schemas of the objects in the source instance. This is because DTS does not support init ial schema synchronizat ion between Cloud Native Distributed Database PolarDB-X instances.

> Not e During init ial schema synchronizat ion, DTS synchronizes the schemas of the required objects from the source database to the destination database.

Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set both Source Instance Type and Destination Instance Type to Drds, and set Synchronization Mode to One-Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Instance Details | Instance Type | This parameter is set to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the source Cloud Native Distributed Database PolarDB-X instance. |
| Destination Instance Details | Instance Type | This parameter is set to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the destination Cloud Native Distributed Database PolarDB-X instance. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and objects.

| Parameter | Description |
|---|---|
| Processing Mode In Existed Target Table | Pre-check and Int ercept : checks whether the destination tables are empty. If the destination tables are empty, the precheck is passed. If the tables are not empty, an error is returned during the precheck and the data synchronization task cannot be started. Ignore: skips the check for empty destination tables. Warning If you select Ignore, data consistency is not guaranteed and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized or the data synchronization task fails. |

| Parameter | Description |
|---|---|
| Select Objects | Select tables from the Available section and click the icon to move the tables to the Select ed section. Not e You can select only tables as the objects to be synchronized. After an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |

6. Click Next .
7. Specify whether you want to perform initial full data synchronization.

> Not e During init ial f ull dat a synchronizat ion, DTS synchronizes the historical data of the required objects from the source database to the destination database. If you do not select Initial Full Data Synchronization, DTS does not synchronize the historical data.

8. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

9. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.6 Synchronize data from a Cloud Native Distributed Database PolarDB-X instance to an AnalyticDB for MySQL cluster

Distributed Database PolarDB-X instance to an AnalyticDB for MySQL cluster This topic describes how to synchronize data from a Cloud Native Distributed Database PolarDB-X instance to an AnalyticDB for MySQL cluster by using Data Transmission Service (DTS). Prerequisites The tables that you want to synchronize contain primary keys. Precautions If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. Only one-way synchronization is supported. Supported synchronization topologies DTS supports the following synchronization topologies: one-way one-to-one synchronization, oneway one-to-many synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized INSERT, UPDATE, and DELETE Data type mappings The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-to-one correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table lists the data types that DTS can convert.

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
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

| D | ata Transmission Service | User Guide·Data synchronizatio | n |
|---|---|---|---|

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
|---|---|
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

| User Guide·Data synchronization | Data Transmission Servic |
|---|---|

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL |
|---|---|
| TINYTEXT | VARCHAR |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |
| YEAR | INT |

Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set Source Instance Type to Drds, set Destination Instance Type to Analyt icDB, and set Synchronization Mode to One- Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Instance Details | Instance Type | This parameter is set to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the source Cloud Native Distributed Database PolarDB-X instance. |
| Destination Instance Details | Instance Type | This parameter is set to Analyt icDB and cannot be changed. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Version | Select 3.0. |
|   | Database | Select the ID of the destination AnalyticDB for MySQL cluster. |
|   | Database Account | Enter the database account of the destination AnalyticDB for MySQL cluster. |
|   | > Document Version: 2022092 |   |

|   | ice User Guide·Data synchronizatio |   |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | Enter the password of the destination database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and objects

| Section | Parameter | Description |
|---|---|---|
| Synchroniza tion policy | Initial Synchronization | You must select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion in most cases. After the precheck, DTS synchronizes the schemas and data of the required objects from the source instance to the destination cluster. The schemas and data are the basis for subsequent incremental synchronization. |
|   | Processing Mode In Existed Target Table | Clear T arget T able Skips the Schema Name Conf lict item during the precheck. Clears the data in the destination table before initial full data synchronization. If you want to synchronize your business data after testing the data synchronization task, you can select this mode. Ignore Skips the Schema Name Conf lict item during the precheck. Adds data to the existing data during initial full data synchronization. If you want to synchronize data from multiple tables to one table, you can select this mode. |
|   | Synchronization Type | Select the types of operations that you want to synchronize based on your business requirements. Insert Updat e Delet e |

| Section | Parameter | Description |
|---|---|---|
| Select Objects | N/A | Select tables from the Available section and click the icon to move the tables to the Select ed section. Not e You can select only tables as the objects to be synchronized. You can use the object name mapping feature to change the names of the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |

6. Click Next .
7. Specify a type for the tables that you want to synchronize to the destination database.

> Not e After you select Init ial Schema Synchronizat ion, you must specify the t ype, primary key column, and part it ion key column for the tables that you want to synchronize to AnalyticDB for MySQL.

8. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

9. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.7 Synchronize data from a Cloud Native Distributed Database PolarDB-X instance to a DataHub instance

Distributed Database PolarDB-X instance to a DataHub instance This topic describes how to synchronize data from a Cloud Native Distributed Database PolarDB-X instance to a DataHub instance by using Data Transmission Service (DTS). After you synchronize data, you can use big data services such as Realtime Compute to analyze data in real time. Prerequisites The tables that you want to synchronize have PRIMARY KEY or UNIQUE constraints. A DataHub project is created to receive the synchronized data. Precautions If you select one or more tables (not a database) as the required objects, do not use gh-ost or ptonline-schema-change to perform data definition language (DDL) operations on the tables during data synchronization. Otherwise, data may fail to be synchronized. The source database must have PRIMARY KEY or UNIQUE constraints and all fields must be unique. Otherwise, the destination database may contain duplicate data records. Only one-way synchronization is supported. Limits You can select only tables as the objects to be synchronized. Initial full data synchronization is not supported. DTS does not synchronize the historical data of the required objects from the source PolarDB-X instance to the destination DataHub instance. DTS does not synchronize data definition language (DDL) operations to the destination database. If you perform a DDL operation on the source PolarDB-X instance during data synchronization, data fails to be synchronized. To solve this issue, you must modify the related topic in the destination DataHub instance and then restart the data synchronization task. SQL operations that can be synchronized INSERT, UPDATE, and DELETE Procedure
1. Create a data synchronization instance.

> Not e When you create the data synchronization instance, set Source Instance Type to Drds, set Destination Instance Type to Dat ahub, and set Synchronization Mode to One-Way Synchronizat ion.

2. Find the data synchronization instance, and click Conf igure Synchronizat ion Channel in the
Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |

| Section | Parameter | Description |
|---|---|---|
| Source Instance Details | Instance Type | This parameter is set to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region of the source instance. The region is the same as the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the source Cloud Native Distributed Database PolarDB-X instance. |
| Destination Instance Details | Instance Type | This parameter is set to Dat aHub and cannot be changed. |
|   | Instance Region | The region of the destination instance. The region is the same as the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | Select the name of the DataHub project. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and objects.

| Parameter | Description |
|---|---|
| Initial Synchronization | Select Init ial Schema Synchronizat ion. Not e After you select Init ial Schema Synchronizat ion, DTS synchronizes the schemas of the required objects (such as tables) to the destination DataHub instance. |

| Parameter | Description |
|---|---|
| Select Objects | Select objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select only tables as the objects to be synchronized. You can use the object name mapping feature to change the names of the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |

6. In the lower-right corner of the page, click Precheck.

> Not e You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. Then, DTS performs initial synchronization.

#### 4.4.8 Configure two-way data synchronization between RDS instances

between RDS instances

##### 4.4.8.1 Overview

DTS supports two-way real-time data synchronization between RDS instances on any two clouds. This section describes how to use DTS to create a two-way synchronization task between two ApsaraDB RDS for MySQL instances for active geo-redundancy, geo-disaster recovery, and other scenarios.

##### 4.4.8.2 Supported synchronization statements

Two-way synchronization between ApsaraDB RDS for MySQL instances supports all DML updates (including INSERT, UPDATE, and DELETE) and the following DDL updates: ALTER TABLE, ALTER VIEW, ALTER FUNCTION, and ALTER PROCEDURE CREATE DATABASE, CREATE SCHEMA, CREATE INDEX, CREATE TABLE, CREATE PROCEDURE, CREATE FUNCTION, CREATE TRIGGER, CREATE VIEW, and CREATE EVENT DROP FUNCTION, DROP EVENT, DROP INDEX, DROP PROCEDURE, DROP TABLE, DROP TRIGGER, and DROP VIEW RENAME TABLE and TRUNCATE TABLE

> Not e To ensure the stability of a two-way synchronization channel, you can synchronize DDL updates on the same table in only one direction.
> For example, for two-way synchronization, you must enable DDL synchronization in either the A- t o-B or B-t o-A direction. If DDL synchronization is configured in one direction, it is not supported in the reverse direction. You can only perform DML synchronization.

##### 4.4.8.3 Detect and resolve conflicts

To ensure data consistency, for two-way synchronized instances, make sure that records with the same primary key, business primary key, or unique key are updated only on one of the instances. If you unexpectedly update a record with the same primary key, business primary key, or unique key on both instances that are two-way synchronized, a synchronization conflict occurs. To maximize the stability of two-way synchronized instances, DTS supports detecting and resolving data conflicts. Considerations During two-way synchronization, the system time of the source and destination instances may not be the same. Additionally, synchronization delays may occur. For these reasons, DTS cannot guarantee that its conflict detection mechanism can completely prevent data conflicts. You must refactor certain business logic to ensure that records of the same primary key, business primary key, or unique key are updated only on one of the instances that are two-way synchronized. Supported conflict types Currently, DTS supports detecting the following conflict types: Uniqueness conflicts caused by INSERT operations A uniqueness conflict occurs when the synchronization of an inserted row violates the unique constraint. For example, if two instances in two-way synchronization insert a record with the same primary key value at almost the same time, one of the inserted records fails to be synchronized because a record with the same primary key value already exists in the destination instance. Inconsistent records caused by UPDATE operations Update conflicts occur in the following scenarios: The records to be updated do not exist in the destination instance. If the records to be updated do not exist, DTS automatically changes the UPDATE operation to the INSERT operation and inserts these records to the destination instance. In this case, duplicate unique key values may occur. The primary keys or unique keys of the records to be updated conflict with each other. A DELETE operation is made on non-existent records A delete conflict occurs when the records to be deleted do not exist in the destination instance. In this case, DTS automatically ignores the DELETE operation regardless of the conflict resolution policy that you have configured. Supported conflict resolution policies For the preceding synchronization conflicts, DTS provides the following resolution policies. You can select a conflict resolution policy as required when configuring two-way synchronization. TaskFailed: The synchronization task reports an error and automatically exits the process in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task reports an error and automatically exits the process. The task enters a failed state and you must manually resolve the conflict. This method is the default conflict resolution policy. Ignore: The records in the destination instance are used in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task skips the current synchronization statement and continues the process. The records in the destination instance are used. Overwrite: The conflict records in the destination instance are overwritten in case of a conflict. When the synchronization encounters a conflict of the preceding types, the conflict records in the destination instance are overwritten.

##### 4.4.8.4 Synchronization restrictions

This section describes the restrictions in cross-cloud data synchronization using DTS. Restrictions in data sources Currently, only ApsaraDB RDS for MySQL instances support two-way synchronization. Other heterogeneous data sources do not support two-way synchronization. The destination instance cannot be an RDS instance that runs in standard access mode and has only a public network address. Restrictions in synchronization architecture Currently, DTS only supports two-way synchronization between two ApsaraDB RDS for MySQL instances. Two-way synchronization between more than two instances is not supported. Feature restrictions Incompatible with triggers When you synchronize an entire database and the database contains a trigger that updates the synchronization table, the synchronized data may be inconsistent. For example, the object to be synchronized is database A that contains table a and table b. Table a has a trigger that inserts a row to table b after the row is inserted to table a. In this case, if an INSERT operation is performed on table a in the source instance during synchronization, the data in table b is inconsistent between the source and destination instances. To resolve this problem, you must delete the trigger in the destination instance, so that the data in table b is only synchronized from the source instance. Restrictions in the RENAME TABLE operation The RENAME TABLE operation may result in inconsistent synchronization data. For example, if the object to be synchronized only includes table a and the rename a t o b command is executed in the source instance during synchronization, subsequent operations to the renamed table b are not synchronized to the destination database. To solve this problem, you can synchronize the entire database where table a and table b are stored. Restrictions in DDL synchronization direction To ensure the stability of a two-way synchronization channel, you can synchronize DDL updates on the same table in only one direction. For example, in A-to-B and B-to-A synchronization, you can implement DDL synchronization in either the A-t o-B or B-t o-A direction. If DDL synchronization is configured in one direction, it is not supported in the reverse direction.

##### 4.4.8.5 Configure two-way data synchronization between ApsaraDB RDS for MySQL instances across regions

between ApsaraDB RDS for MySQL instances across regions This topic describes how to configure two-way data synchronization between ApsaraDB RDS for MySQL instances across regions. Prerequisites The source and destination ApsaraDB RDS for MySQL instances are created. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. On the Synchronizat ion T asks page, click Creat e Synchronizat ion T ask in the upper-right
corner.

> Not e
> Source Instance Region: Select the region where the source RDS instance resides.
> Source Instance Type: Select the type of the source instance. In this example, select MySQL.
> Destination Instance Region: Select the region where the destination RDS instance resides.
> Destination Instance Type: Select the type of the destination instance. In this example, select MySQL.
> Synchronization Mode: Select the synchronization mode. In this example, select Two-Way Synchronization.
> Instances to Create: Set the number of instances that you want to create.

4. After you configure the preceding information, click Creat e.
After you create a synchronization instance, go back to the Synchronizat ion T asks page. The new synchronization instance is in the Not Configured state and contains two synchronization tasks. You can configure two-way synchronization for the tasks.
5. Find one of the created synchronization tasks and click Conf igure Synchronizat ion Channel in
the Actions column.
6. Configure the parameters for the data synchronization task.
Synchronization Task Name We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. RDS instance ID You must specify the ID of the Apsara Stack tenant account to which the destination RDS instance belongs. You can then select an RDS instance ID from the Instance ID drop-down list. After you complete the preceding configurations, click Set Whit elist and Next to configure the RDS instance whitelists.
7. Configure the RDS instance whitelists.
In this step, DTS adds the CIDR blocks of DTS servers to the whitelists of the source and destination RDS instances. This ensures that DTS servers can connect to the RDS instances and the data synchronization task can be created. We recommend that you do not remove the CIDR blocks of DTS servers from the whitelists of the RDS instances. This ensures the stability of the data synchronization task. Click Next to create a data synchronization account.
8. Create a data synchronization account in the destination RDS instance.
Create a data synchronization account named dtssyncwriter in the destination RDS instance. Do not delete the account during data synchronization. Otherwise, an interruption occurs.
9. Configure the synchronization policies and select the objects that you want to synchronize.
After you create a data synchronization account, you must configure the synchronization policies and select the objects that you want to synchronize. Exclude DDL Statements Specify whether to synchronize DDL statements in a specific direction. To include DDL statements, select No. To exclude DDL statements, select Yes. If you select No, DTS does not synchronize the DDL operations that are performed on a table in the opposite direction. DML Statements for Synchronization Select the types of DML operations that you want to synchronize. By default, Insert , Updat e, and Delet e are selected. Conflict Resolution Policy Select the resolution policy for synchronization conflicts. By default, T askFailed is selected. For example, if Node A is the primary business center and Node B is a secondary business center, you must give the priority to Node A. You must set the conflict resolution policy in the A-to-B direction to Overwrit e and that in the B-to-A direction to Ignore. Select Objects You can select databases and tables as the objects to be synchronized. If you select an entire database, all schema changes such as the CREATE TABLE and DROP VIEW operations that performed on the objects in the database are synchronized to the destination database. If you select a table, only the DROP TABLE, ALTER TABLE, TRUNCATE TABLE, RENAME TABLE, CREATE INDEX, and DROP INDEX operations that performed on this table are synchronized to the destination database.
10. Configure initial synchronization.
Initial synchronization is the first step to start the synchronization task. During initial synchronization, DTS synchronizes the schemas and data of the required objects from the source instance to the destination instance. The schemas and data are the basis for subsequent incremental synchronization. Initial synchronization includes init ial schema synchronizat ion and init ial f ull dat a synchronizat ion. You must select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion in most cases. If the tables to be synchronized in one direction are also included in the objects to be synchronized in the opposite direction, DTS does not synchronize these tables during initial synchronization.
11. Run a precheck.
After the data synchronization task is configured, DTS performs a precheck. Close the Precheck dialog box after the task passes the precheck. After the task is started, the task list appears. The task is in the Perf orming Init ial Sync state. The duration of the initial synchronization depends on the data volume of the objects that you want to synchronize. After initial synchronization, the task status changes to Synchronizing. This indicates that the data synchronization task is created. After the task is configured in one direction, the source and destination RDS instances of the task in the opposite direction cannot be changed.
12. Repeat steps 5 to 11 to configure the data synchronization task in the opposite direction.

### 4.5 Manage data synchronization instances

instances

#### 4.5.1 Specify the name of an object in the destination instance

destination instance After an object, such as a database or table, is synchronized from the source instance to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature provided by DTS to specify a different name for the object in the destination instance. Notes You can perform this operation only when a data synchronization task is configured and the current process is Select Object s t o Synchronize.

> Not e Do not perform this operation after the data synchronization task is started. Otherwise, the synchronization may fail.

Procedure
1. On the Select Object s t o Synchronize page, move the required objects to the Select ed
section, move the pointer over a database or table, and then click Edit .

> Not e Different database types support different objects. If Edit appears when you move the pointer over the target object, the operation is supported.

2. In the dialog box that appears, specify a name for the object in the destination instance.
Database name mapping In the Edit Dat abase Name dialog box that appears, enter the database name that you want to use in the destination instance. Table name mapping In the Edit T able dialog box that appears, enter the table name that you want to use in the destination instance. Column name mapping In the Edit T able dialog box that appears, enter a new name for each column.

> Not e In this step, you can deselect columns that do not need to be synchronized.

3. Click OK.
4. Configure other parameters that are required for the data synchronization task.

#### 4.5.2 Check the synchronization performance

DTS provides the trend charts of data synchronization tasks based on three performance metrics: bandwidth, synchronization speed (TPS), and synchronization delay. You can view the running status of data synchronization tasks in the DTS console.
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. On the Synchronization Tasks page, click the ID of the data synchronization task that you want to
check. The task details page appears.
4. On the task details page, click Synchronizat ion Perf ormance in the left-side navigation pane.
5. View the trend charts of synchronization performance.
DTS provides the trend charts of data synchronization tasks based on three performance metrics: bandwidth, synchronization speed (TPS), and synchronization delay. Bandwidth: the bandwidth of data that the data writing module pulls from the data pulling module per second. Unit: MB/s. Synchronization speed (TPS): the number of transactions that DTS synchronizes to the destination instance per second. Synchronization delay: the difference between the timestamp of the latest synchronized data in the destination instance and the current timestamp in the source instance. Unit: milliseconds.

#### 4.5.3 Add objects to a data synchronization task

When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to add objects to a data synchronization task in the DTS console. Limits You can modify the required objects only when the data synchronization task is in the Synchronizing or Synchronizat ion Failed state. Start time of data synchronization The time when DTS synchronizes data of new objects depends on whether initial synchronization is specified for the data synchronization task. If initial synchronization is specified, DTS synchronizes schemas and historical data, and then synchronizes incremental data. If initial synchronization is not specified, DTS synchronizes data after incremental data is generated on the source instance. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. Find the data synchronization task and choose More > Modif y Object s t o Synchronize in the
Actions column.
4. On the Select Object s t o Synchronize tab, add objects based on your needs, as shown in Add
objects to a data synchronization task.
5. Click Precheck.
After the task passes the precheck, the objects are added to the data synchronization task. After the objects are added, if initial synchronization is specified for the data synchronization task, the task status changes from Synchronizing to Synchronizing (T he init ial synchronizat ion of t he new object s is being perf ormed.).

> Not e You can click View More to view the initial synchronization progress of the new objects. After the initial synchronization on the new objects is complete, the task status returns to Synchronizing.

#### 4.5.4 Remove objects from a data synchronization task

synchronization task When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to remove objects from a data synchronization task in the DTS console. Limits You can modify the required objects only when the data synchronization task is in the Synchronizing or Synchronizat ion Failed state. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. Find the data synchronization task and choose More > Modif y Object s t o Synchronize in the
Actions column.
4. On the Select Object s t o Synchronize tab, remove objects based on your needs.
5. Click Precheck to run a precheck.

#### 4.5.5 Troubleshoot precheck failures

Before Data Transmission Service (DTS) runs a data synchronization task, DTS performs a precheck. This topic describes the precheck items and how to troubleshoot precheck failures. Source database connectivity Description DTS checks whether DTS servers can connect to the source RDS instance. DTS creates a connection to the source RDS instance by using the JDBC protocol. If the connection fails, the task fails to pass the precheck. Cause of failure DTS does not support data synchronization between RDS instances in the region where the source instance resides. The database account or password of the source instance is invalid. Solution Submit a ticket and contact Alibaba Cloud technical support. Destination database connectivity DTS checks whether DTS servers can connect to the destination RDS instance. DTS creates a connection to the destination RDS instance by using the JDBC protocol. If the connection fails, the task fails to pass the precheck. Cause of failure DTS does not support data synchronization between RDS instances in the region where the destination instance resides. The database account or password of the destination instance is invalid. Solution Submit a ticket and contact Alibaba Cloud technical support. Source database version Description DTS checks whether: i. The database version of the source RDS instance is supported by the data synchronization feature. ii. The database version of the destination RDS instance is the same as the database version of the source RDS instance. Cause of failure The database version of the source RDS instance is earlier than the supported database versions. The data synchronization feature supports the following database versions: MySQL 5.1, 5.5, 5.6, and 5.7. The database version of the destination RDS instance is earlier than the database version of the source RDS instance. Solution If the database version of the source RDS instance is earlier than the supported database versions, upgrade the source RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again. If the database version of the destination RDS instance is earlier than the database version of the source RDS instance, upgrade the destination RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again. Database existence DTS checks whether the destination database already exists in the destination instance. If the destination database does not exist in the destination instance, DTS automatically creates a database. However, DTS fails to create the database and reports a failure under the following circumstances: The database name contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). The character set of the database is not UTF-8, GBK, Latin1, or UTF-8MB4. The account of the destination database does not have the read/write permissions on the source database. If the data source is an RDS instance, the task passes the precheck. Source database permissions DTS checks whether the account of the source database has the required permissions. If the account does not have the required permissions, the task fails to pass the precheck. If the source database is an RDS instance, the task passes the precheck. Destination database permissions Description DTS checks whether the account of the destination database has the required permissions. If the account does not have the required permissions, the task fails to pass the precheck. Cause of failure DTS fails to create a database account in the destination RDS instance. DTS fails to grant the read/write permissions to the database account of the destination RDS instance. Solution Submit a ticket and contact Alibaba Cloud technical support. Object name conflict Description DTS checks object names only if you select initial synchronization for a data synchronization task. DTS checks whether an object that you want to synchronize has the same name as an object in the destination RDS instance. Cause of failure If an object in the destination RDS instance has the same name as the object that you want to synchronize, the task fails to pass the precheck. Solution Remove the conflicting object from the destination database. Then, create a data synchronization task again. Select both Initial Schema Synchronization and Initial Full Data Synchronization. Value of server_id in the source database DTS checks whether the value of the server_id parameter in the source database is set to an integer that is greater than or equal to 2. If the data source is an RDS instance, the task passes the precheck. Whether binary logging is enabled for the source database DTS checks whether the binary logging feature is enabled for the source database. If the binary logging feature is disabled for the source database, the task fails to pass the precheck. If the data source is an RDS instance, the task passes the precheck. Binary log format of the source database DTS checks whether the binary log format of the source database is set to ROW. If the binary log format of the source database is not set to ROW, the task fails to pass the precheck. If the data source is an RDS instance, the task passes the precheck. Integrity of the FOREIGN KEY constraints DTS checks whether the parent tables and child tables that have referential relationships with each other are all included in the required objects. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. Cause of failure One or more child tables are included in the required objects. However, the parent tables that are referenced by the child tables are not included in the required objects. This impairs the integrity of the FOREIGN KEY constraints. Solution The following solutions are available: Create a data synchronization task again and do not synchronize the child tables that fail to pass the precheck. Create a data synchronization task again and add the parent tables to the required objects. Remove the FOREIGN KEY constraints from the child tables that fail to pass the precheck. Then, create a data synchronization task again. Storage engine Description DTS checks whether the required objects use the storage engines that are not supported by the data synchronization feature, such as FEDERATED, MRG_MyISAM, and TokuDB. Cause of failure If the storage engine of a source table is FEDERATED, MRG_MyISAM, or TokuDB, the task fails to pass the precheck. Solution Change the unsupported storage engine to InnoDB and create a data synchronization task again. Character set Description DTS checks whether the required objects use the character sets that are not supported by the data synchronization feature, such as the UCS-2 character set. Cause of failure If the character sets used by the required objects are not supported by the data synchronization feature, the task fails to pass the precheck. Solution Change the unsupported character sets to UTF-8, GBK, or Latin1. Then, create a data synchronization task again. Complicated topologies Description DTS checks whether the topology that you specify for the source and destination RDS instances is supported. Cause of failure The source RDS instance in the current task is being used as the destination instance of another task. The destination RDS instance in the current task is being used as the source or destination instance of another task. The objects that you want to synchronize in the current task are being synchronized by an existing task. The two tasks have the same source and destination RDS instances. Solution If the task that you want to create has the same source and destination RDS instances as an existing task, you can add the required objects to the existing task. You do not need to create another task to synchronize these objects. If the task that you want to create conflicts with an existing task, wait until the existing task is completed before you create a data synchronization task again. Format of the MySQL database password DTS checks whether the format of the password that is used to access the source database is no longer valid. If the data source is an RDS instance, the task passes the precheck.

## 5 Change tracking

### 5.1 Overview

You can use Data Transmission Service (DTS) to track data changes from ApsaraDB RDS for MySQL instances in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. Supported databases User-created MySQL databases or ApsaraDB RDS for MySQL PolarDB-X (formerly known as DRDS) User-created Oracle database Objects for change tracking The objects for change tracking include tables and databases. In change tracking, data changes include data manipulation language (DML) operations and data definition language (DDL) operations. When you configure change tracking, you must select operation types. Change tracking tasks A change tracking task is the basic unit of change tracking and data consumption. To track data changes from an RDS instance, you must create a change tracking task in the DTS console for the RDS instance. The change tracking task pulls data changes from the RDS instance in real time and locally stores the data changes. You can use the DTS SDK to consume the tracked data. You can also create, manage, or delete change tracking tasks in the DTS console.

### 5.2 Create a change tracking instance

instance Before you configure a task to track data changes, you must create a change tracking instance. This topic describes how to create a change tracking instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. In the upper-right corner, click Creat e Change T racking T ask.
4. In the Create DTS Instances dialog box, select a region, and enter the number of change tracking
instances that you want to create.

> Not e In the Create DTS Instances dialog box, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

5. Click Creat e.

### 5.3 Configure change tracking tasks

#### 5.3.1 Track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance

MySQL database or an ApsaraDB RDS for MySQL instance You can use Data Transmission Service (DTS) to track data changes in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance. Prerequisites The version of the MySQL database is 5.1, 5.5, 5.6, or 5.7. Precautions DTS does not track data definition language (DDL) operations that are performed by gh-ost or ptonline-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If the source database is used in another task, for example, it is used in a running data migration task, DTS may track data changes of other objects. In this case, you must use the change tracking client to filter the tracked data. Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click Conf igure Channel in the Act ions
column.
3. Configure the source database.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source | Version | Select a version based on your business requirements: If the source database is a user-created MySQL database, select Old. If the source database is ApsaraDB RDS for MySQL, select New. Not e You can follow the same procedure to configure change tracking tasks when you select Old or New. In this example, select New. |
|   | Instance Type | Select RDS Inst ance. |
|   | Database Type | MySQL is selected by default. |
|   | Instance Region | The region of the source instance. The region is the same as the region that you selected when you created the change tracking task. You cannot change the value of this parameter. |

| Database Section | Parameter | Description |
|---|---|---|
|   | RDS Instance ID | Select the ID of the RDS instance from which you want to track data changes. Not e A read-only instance or temporary instance cannot be used as the source instance for change tracking. |
|   | Database Account | Enter the database account of the source RDS instance. Not e The account must have the REPLICATION SLAVE permission, the REPLICATION CLIENT permission, and the permission to perform SELECT operations on the required objects. If the database engine of the source RDS instance is MySQL 5.5 or MySQL 5.6, you do not need to configure the dat abase account or dat abase password. |
|   | Database Password | Enter the password of the source database account. |
| Consumer Network Type | Network Type | Classic is selected by default. Not e This parameter is available only if the Version parameter is set to New. If you track data changes over internal networks, the network latency is minimal. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Paramet er | Description |
|---|---|
| Required Data Types | Dat a Updat es DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the required data. Not e If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the required objects. For more information, see Modify the objects for change tracking. |

| Paramet er | Description |
|---|---|
| Required Objects | Select tables or databases from the Required Object s section and click the icon to move them to the Select ed section. |

6. In the lower-right corner of the page, click Save and Precheck.

> Not e You can start a change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data. What's next Previous change tracking feature: Run the SDK demo code New change tracking feature: Use a Kafka client to consume tracked data

#### 5.3.2 Track data changes from a PolarDB-X instance

instance You can use Data Transmission Service (DTS) to track data changes in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a PolarDB-X instance. PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). Precautions DTS does not track data definition language (DDL) operations that are performed by gh-ost or ptonline-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If the source database is used in another task, for example, it is used in a running data migration task, DTS may track data changes of other objects. In this case, you must use the change tracking client to filter the tracked data. Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click Conf igure Channel in the Act ions
column.
3. Configure the source database.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | This parameter is set to DRDS Inst ance and cannot be changed. |
|   | Database Type | This parameter is set to DRDS and cannot be changed. |
|   | Instance Region | The region of the source instance. The region is the same as the region that you selected when you created the change tracking task. You cannot change the value of this parameter. |
|   | DRDS Instance ID | Select the ID of the PolarDB-X instance. |
|   | Database Name | Select the ID of the source database in the PolarDB-X instance. |
|   | Database Account | Enter the database account of the PolarDB-X instance. |
|   | Database Password | Enter the password of the source database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Paramet er | Description |
|---|---|
| Required Data Types | Dat a Updat es DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the required data. Not e If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the required objects. For more information, see Modify the objects for change tracking. |

| Paramet er | Description |
|---|---|
| Required Objects | Select tables or databases from the Required Object s section and click the icon to move them to the Select ed section. |

6. In the lower-right corner of the page, click Save and Precheck.

> Not e You can start a change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data.

#### 5.3.3 Track data changes from a user-created Oracle database

Oracle database You can use Data Transmission Service (DTS) to track data changes in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a user-created Oracle database. Prerequisites The version of the user-created Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the user-created Oracle database. For more information, see Supplemental Logging. The user-created Oracle database is running in ARCHIVELOG mode. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Precautions DTS does not track data definition language (DDL) operations that are performed by gh-ost or ptonline-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflict. If the source database is used in another task, for example, it is used in a running data migration task, DTS may track data changes of other objects. In this case, you must use the change tracking client to filter the tracked data. Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you created, and click Conf igure Channel in the Act ions
column.
3. Configure the source database and network type.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | DTS automatically generates a task name. We recommend that you specify an informative name for easy identification. You do not need to use a unique task name. |
| Source Database | Instance Type | Select an instance type based on where the source database is deployed. In this example, select User-Creat ed Dat abase wit h Public IP Address. |
|   | Database Type | This parameter is set to Oracle and cannot be changed. |
|   | Instance Region | The region of the source instance. The region is the same as the region that you selected when you created the change tracking task. You cannot change the value of this parameter. |
|   | Hostname or IP Address | Enter the hostname or IP address of the user-created Oracle database. |
|   | Port Number | Enter the service port number of the user-created Oracle database. |
|   | SID | Enter the system ID (SID) of the user-created Oracle database. |
|   | Database Account | Enter the account of the user-created Oracle database. Not e The account must have the database administrator (DBA) permission. |

|   | ervice | User Guide·Change trackin |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | Enter the password of the source database account. |
| Consumer Network Type | N/A | Classic is selected by default. Not e If you track data changes over internal networks, the network latency is minimal. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Paramet er | Description |
|---|---|
| Required Data Types | Dat a Updat es If you select Data Updates, DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es If you select Schema Updates, DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the tracked data. Not e If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the required objects. For more information, see Modify the objects for change tracking. |
| Required Objects | Select objects from the Required Object s section and click the icon to move the objects to the Select ed section. |

6. In the lower-right corner of the page, click Save and Precheck.

> Not e You can start a change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

7. Close the Precheck dialog box after the following message is displayed: T he precheck is
passed. After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data. What's next

### 5.4 Manage change tracking tasks

#### 5.4.1 Modify the consumption checkpoint

During data consumption, you can modify the consumption checkpoint of a change tracking task based on your business requirements. After you modify the consumption checkpoint, the downstream SDK client will consume the data that is generated after the specified time. Prerequisites A change tracking task is created. For more information, see Track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance (previous version) or Track data changes from a PolarDB-X instance. Procedure
1. Stop all downstream SDK consumption processes.

> Not e We recommend that you perform this operation during off-peak hours to avoid service interruption.

## 2 Log on to the DTS console.

3. In the left-side navigation pane, click Change T racking.
4. Find the change tracking task, move the pointer over the Consumpt ion Checkpoint column, and
then click the icon.
5. In the Modify Consumption Checkpoint dialog box, specify a new consumption checkpoint.

> Not e The selected time range must be within the time range of the tracked data. For more information, see the prompt in the dialog box.

6. Click Modif y.
7. Restart the downstream SDK consumption processes.
The downstream SDK client tracks data changes from the new consumption checkpoint.

#### 5.4.2 Modify the objects for change tracking

DTS allows you to add or remove the objects for change tracking in the consumption process. This topic describes how to modify the objects for change tracking. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. Find the change tracking task, and click Modif y Required Object s in the Act ions column.
4. In the Select Required Object s step, add or remove the objects for change tracking.
Add the objects for change tracking In the Required Object s section, select one or more objects and click the icon to add the objects to the Select ed section. Remove the objects for change tracking In the Select ed section, select one or more objects and click the icon to move the objects to the Required Object s section.
5. In the lower-right corner of the page, click Save and Precheck.

> Not e You can start a change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the
> icon next to each failed item to view details.
> Troubleshoot the issues based on the causes and run a precheck again.

#### 5.4.3 Create a consumer group

You can manage consumer groups of a change tracking task in the DTS console. This topic describes how to create a consumer group. Prerequisites A change tracking task is created. For more information, see Track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance (new version) or Track data changes from a PolarDB-X instance. Note You can create multiple consumer groups (up to 20) in a change tracking instance to repeatedly consume data. A consumer group consumes each message only once, and only one consumer can consume data. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. Find the change tracking task and click the task ID.
4. In the left-side navigation pane, click Consume Dat a.
5. On the Consume Dat a page, click Add Consumer Group in the upper-right corner.
6. In the dialog box that appears, set the parameters for the consumer group.

| Parameter | Description |
|---|---|
| Consumer Group Name | Enter a new name for the consumer group. We recommend that you use an informative name for easy identification. |
| Username | Enter the username of the consumer group. A username must contain one or more of the following character types: uppercase letters, lowercase letters, digits, and underscores ( ). _ The username must be 1 to 16 characters in length. |
| Password | Enter the password that corresponds to the username of the consumer group. A password must contain two or more of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| Confirm Password | Enter the new password again. |

7. Click Creat e.

#### 5.4.4 Manage consumer groups

You can manage consumer groups of a change tracking task in the DTS console. This topic describes how to modify the password of a consumer group and how to delete a consumer group. Prerequisites Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. Find the change tracking task and click the task ID.
4. In the left-side navigation pane, click Consume Dat a.
5. Modify the password of a consumer group or delete a consumer group.
Modify the password of a consumer group i. On the Consume Dat a page, find the target consumer group and click Modif y Password in the Act ions column. ii. In the Modif y Password dialog box that appears, enter the old password and new password, and enter the new password again in the Conf irm Password field.

> Not e
> A password must contain two or more of the following character types: uppercase letters, lowercase letters, digits, and special characters.
> The password must be 8 to 32 characters in length.

iii. Click Modif y. Delete a consumer group

> Not e After a consumer group is deleted, the data in the group will be cleared and cannot be recovered. We recommend that you use caution when performing this operation.

i. On the Consume Dat a page, find the target consumer group and click Delet e in the Act ions column. ii. In the Delet e Consumer Group message that appears, click OK.

### 5.5 Use the SDK to consume tracked data

data

#### 5.5.1 Methods provided by SDK

You can use the SDK demo code that is provided by DTS to consume tracked data. This topic describes the methods that are available for the SDK classes. Methods of the RegionContex class

| Method | Description |
|---|---|
| setAccessKey(accessKey) | Specifies the AccessKey ID of the Alibaba Cloud account to which the source instance belongs. |
| setSecret(AccessKeySecret) | Specifies the AccessKey secret of the Alibaba Cloud account to which the source instance belongs. |
| setUsePublicIp(usePublicIp) | Specifies whether to track data changes over the Internet. Not e DTS can track data changes only over the Internet. Therefore, set the usePublicIp parameter to true . |
| context.setUseBinary(boolean useBinary) | Specifies whether to enable the binary packaging feature. Valid values: True and False. We recommend that you enable this feature to improve consumption performance. |

|   | context.setUseBinary(boolean | Spe valu |
|---|---|---|
| useBinary) |   |   |

| Data Transmission Service | User Guide·Change trackin |
|---|---|

| Method | Description |
|---|---|
| context.setUseDrcNet(boolean useDrcNet) | Specifies whether to enable the network optimization feature. Valid values: True and False. We recommend that you enable this feature to improve consumption performance. |

|   | context.setUseDrcNet(boolean | Spe Vali |
|---|---|---|
| useDrcNet) |   |   |

Methods of the ClusterClient class

|   | Method |   | Description |   |   |
|---|---|---|---|---|---|
|   | void |   | Adds a downstream listener to retrieve data changes from a change tracking instance. Not e The ClusterListener arg0 parameter specifies an object of the ClusterListener class. |   |   |
|   |   | void |   |   |   |
|   | addConcurrentListener(ClusterListe |   |   |   |   |
|   |   |   |   | N |   |
|   | ner arg0) |   |   |   |   |
|   | void askForGUID(String arg0) |   | Retrieves data changes from a change tracking instance. Set the String arg0 parameter to the ID of the change tracking instance. |   |   |
|   | List<ClusterListener> getConcurrentListeners() |   | Queries the list of listeners in a ClusterClient object. The return type is List <ClusterListener> . |   |   |
|   | void start() |   | Starts the SDK client to start change tracking. |   |   |
|   | void stop() |   | Stops the SDK client to stop change tracking. Not e Data pulling and notification callback are performed in the same thread of the SDK client. If the consumption code of the notify() method contains a function that prevents signal interruptions, the stop() function may fail to terminate the SDK client. |   |   |

|   | List<ClusterListener> | Queries the l |   |
|---|---|---|---|
| getConcurrentListeners() |   |   |   |

Methods of the ClusterListener class The `void notify(List<ClusterMessage> arg0)` method specifies the consumption mode of tracked data. When the DTS SDK receives the data, it uses the notify() function to notify a ClusterListener object to consume the data. Then, the SDK displays the data on the screen. Methods of the ClusterMessage class

> Not e Each ClusterMessage object stores the data record of a transaction. Each data record in the transaction is stored by using a Record object.

| Method | Description |
|---|---|

| Method | Description |
|---|---|
| Record getRecord() | Retrieves a change record from a ClusterMessage object. The change record contains an entry in the binary log file, such as a BEGIN, COMMIT, UPDATE, or INSERT operation. |
| void ackAsConsumed | After the data consumption is complete, you must call this method to send an ACK packet to instruct the DTS server to update the consumer offset. This ensures the integrity of the consumed data after an abnormal SDK client restarts. Not e If a downstream SDK client restarts after a breakdown, the client resumes change tracking from the last consumer offset. |

Methods of the Record class The `String getAttribute(String key)` method retrieves the attribute values in a Record object. The following table describes the parameters that are available when you call this method.

| Parameter | Description |
|---|---|
| record id _ | The ID of the record. Not e The record ID may not increment during the change tracking process. |
| instance | The endpoint that is used to connect to the database instance. The format is <IP address>:<Port number>. |
| source type _ | The engine type of the database instance. The value is set to MySQL. |
| source category _ | The type of the record. The value is set to full recorded. _ |
| timestamp | The binlog timestamp that is generated when the SQL statement is executed in the source database. |
| checkpoint | The checkpoint of the binary log file. The format is binlog offset@binlog file . _ _ Not e The binlog offset parameter indicates _ the offset of a record in the binary log file. The binlog file parameter indicates the numerical suffix _ of the binary log file. For example, if the name of a binary log file is mysql-bin.0008, the value of the binlog file _ parameter is 8. |

| Parameter | Description |
|---|---|
| record type _ | The operation type. Valid values: insert, update, delete, replace, ddl, begin, commit, and heartbeat. Not e A heartbeat record indicates the heartbeat table that is defined by DTS. The system generates one heartbeat record per second to detect whether the change tracking instance is running as expected. |
| db | The name of the database. |
| table name _ | The name of the table. |
| record recording _ | The encoding format. |
| primary | The name of the primary key column. If the primary key is a composite key, separate column names with commas (,). |
| fields enc _ | The encoding of each field value. Separate fields with commas (,). Not e If a field value is not of the character type, the encoding of this field value is null. |

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
| int getFieldCount() | Queries the number of fields. |

| Method | Description |
|---|---|
| List<Field> getFieldList() | Queries the definitions of all fields, the pre-change image values, and the post-change image values. For more information, see Methods of the Field class. |
| Boolean isFirstInLogevent() | Checks whether the record is the first transaction log in a large volume of data changes. The return value is True or False. |

Methods of the Field class

| Method | Description |
|---|---|
| String getEncoding() | Obtains the encoding format of the field value. |
| String getFieldname() | Queries the name of the field. |
| Type getType() | Queries the data type of the field. |
| ByteString getValue() | Queries the value of the field. The return type is ByteString. If the field is not specified, the method returns NULL . |
| Boolean isPrimary() | Checks whether the field is a primary key column. The return value is True or False. |

#### 5.5.2 Quick start

This section describes how to use the DTS Java SDK to perform some basic operations. Initialize a RegionContext object A RegionContext object stores the settings of authentication credentials and network access mode. The following code shows how to initialize a RegionContext object.

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

`}` `}` Initialize a Listener object Data consumption is implemented by using an object of the Listener class. After you initialize the ClusterClient object, you must add a Listener object. The Listener object uses the notify() method to receive and consume the tracked data. The following code shows how to display the tracked data on the screen.

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
                      System.out.println(message.getRecord() + ":" + message.getRecord().ge
tTablename() + ":"
                      + message.getRecord().getOpt());
                      // Call the following method to send an ACK packet to the DTS server.
                      message.ackAsConsumed();
```

`}` `}` `}` `}` DTS saves the consumption checkpoints of the SDK to the DTS server. This simplifies disaster recovery during the use of the SDK. The ackAsConsumed() method sends the checkpoint and timestamp of the latest data record that was consumed by the DTS SDK to the DTS server. If the SDK restarts due to an error, the SDK obtains the consumption checkpoint from the DTS server. The SDK resumes data consumption from the checkpoint. This ensures that the SDK does not consume duplicate data. Start the ClusterClient object Use the following code:

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

You can use the DTS SDK to track data changes. DTS records the tracked data changes in a custom format. This topic describes how to parse various types of SQL statements. Parse a DDL statement If a data definition language (DDL) operation is performed in the source database, the operation type of the data record is DDL. The DDL statement is stored in the value of the first column. You can use the following sample code to parse the DDL statement:

```
String ddl_string; Record.Type type=record.getOpt(); if(type.equals(Record.Type.DDL)){
    List<DataMessage.Record.Field> fields = record.getFieldList();
    ddl_string = fields.get(0).getValue().toString();
```

`}` Parse an INSERT statement If an INSERT operation is performed in the source database, the operation type of the data record is INSERT. You can use the following sample code to parse the INSERT statement:

```
StringBuilder insert_string=new StringBuilder(); Record.Type type=record.getOpt(); DataMessage.Record.Field field; StringBuilder FieldName=new StringBuilder(); StringBuilder FieldValue = new StringBuilder(); if(type.equals(Record.Type.INSERT)){
       int i=0;
       List<DataMessage.Record.Field> fields = record.getFieldList();
       for (; i < fields.size(); i++) {
              field = fields.get(i);                                   FieldName.append('`'
+field.getFieldname().toLowerCase()+'`');
              FieldValue.append("'"+field.getValue()+"'");
              if (i ! = fields.size() - 1) {
                      FieldName.append(',');
                      FieldValue.append(',');
```

`}` `}`

```
        insert_string.append("insert "+ record.getTablename()+"("+FieldName.toString()+") v
alues("+FieldValue.toString()+");");
```

`}` Parse an UPDATE statement If an UPDATE operation is performed in the source database, the operation type of the data record is UPDATE. The field values prior to the UPDATE operation are stored in `Record.getFieldList()` entries with even indexes. The field values after the UPDATE operation are stored in Record.getFieldList() entries with odd indexes. If the UPDATE operation is performed on a table that has a primary key, you can use the following sample code to parse the UPDATE statement:

```
StringBuilder update_string=new StringBuilder(); Record.Type type=record.getOpt(); DataMessage.Record.Field field; StringBuilder SetValue = new StringBuilder(); StringBuilder WhereCondition = new StringBuilder(); String ConditionStr; boolean hasPk=false; boolean pkMode=false; boolean hasSet=false; if(type.equals(Record.Type.UPDATE)){
    int i=0;
    DataMessage.Record.Field OldField = null;
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
```

```
    field = NewField;
    if (field.isPrimary()) {
        if (hasPk) {
            WhereCondition.append(" and ");
```

`}`

```
        //where old value
        ConditionStr = getFieldValue(OldField);
        if(ConditionStr==null){                                         WhereCondition.appe
nd("`"+field.getFieldname().toLowerCase()+"`" + " " + "is null");
        }else{
               WhereCondition.append("`"+field.getFieldname().toLowerCase()+"`"+" = "+ "'"+
OldField.getValue()+"'");
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
      SetValue.append("`"+field.getFieldname().toLowerCase()+"`" + " = " + "'"+field.getVal
ue()+"'");
    String setStr = getFieldValue(field);
    hasSet = true;
```

`}`

```
    update_string.append("Update "+record.getTablename() +" Set " + SetValue + " Where "+Wh
ereCondition +";");
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
        if (field.getType() == com.aliyun.drc.client.message.DataMessage.Record.Field.Type.
STRING && field.getEncoding() ! = null && field.getEncoding() ! = "ASCII") {
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

`}` `}` Parse a DELETE statement If a DELETE operation is performed in the source database, the operation type of the data record is DELETE. If the DELETE operation is performed on a table that has a primary key, you can use the following sample code to parse the DELETE statement:

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

`}` Parse a REPLACE statement If a REPLACE operation is performed in the source database, the operation type of the data record is UPDATE or INSERT. If the value specified in the REPLACE statement does not exist, the operation type of the data record is INSERT. If the value specified in the REPLACE statement exists, the operation type of the data record is UPDATE. Parse a BEGIN statement If a BEGIN operation is performed in the source database, the operation type of the data record is BEGIN. You do not need to perform operations on fields because the BEGIN statement does not modify fields. You only need to check that the operation is a BEGIN operation. You can use the following sample code to parse the BEGIN statement:

```
StringBuilder sql_string = new StringBuilder(); Record.Type type = record.getOpt(); if(type.equals(Record.Type.BEGIN)){
        sql_string.append("Begin");
```

`}` Parse a COMMIT statement If a COMMIT operation is performed in the source database, the operation type for the data record is COMMIT. You do not need to perform operations on fields because the COMMIT statement does not modify fields. You only need to check that the operation is a COMMIT operation. You can use the following sample code to parse the COMMIT statement:

```
StringBuilder sql_string = new StringBuilder(); Record.Type type = record.getOpt(); if(type.equals(Record.Type.COMMIT)){
        sql_string.append("commit");
```

`}`

#### 5.5.4 Run the SDK demo code

This section describes how to run the demo code provided by the DTS console.
1. Create an AccessKey.
Your account must pass the AccessKey authentication before you can use an SDK to connect to a subscription channel. Therefore, before using the SDK, you must obtain an AccessKey. For more information, see the "Obt ain an AccessKey" section of the DTS Developer Guide .
2. Install the Java SDK.
The development environment supported by the DTS Java SDK is J2SE Development Kit (JDK) V1.5 or later. For an Eclipse project, you can follow these steps to install the Java SDK: i. Click View Example Code and download the SDK package consumer.jar. ii. Import the JAR package to an Eclipse project as follows: In Eclipse, right-click your project and choose Propert ies > Java Build Pat h > Libraries > Add Ext ernal JARs. Select the path for storing the consumer.jar package consumer.jar. iii. Select the consumer.jar package and click OK. Then you can use the DTS Java SDK in the project.
3. Run the demo code.
DTS provides the SDK demo code. You can copy the demo code by using the View Demo Code option in the DTS console. For an Eclipse project, you can follow these steps to run the demo code: i. Create a class named MainClass in the src directory of the Eclipse project. ii. Open the generated Java file MainClass and delete the code template. iii. Paste the demo code into the MainClass file. iv. Modify the AccessKeyId, AccessKeySecret, and subscription channel ID in the demo code. Change the marked parts in the preceding demo code to the AccessKeyId, AccessKeySecret, and subscription channel ID of your account. You can obtain the subscription channel ID from the DTS console. v. In Eclipse, right-click the demo file and choose Run as > Java Applicat ion to run the demo code.

### 5.6 Use a Kafka client to consume tracked data

tracked data This topic describes how to use the demo code of a Kafka client to consume tracked data. The change tracking feature of the new version allows you to consume tracked data by using a Kafka client from V0.11 to V1.1. Prerequisites A change tracking task is created. For more information, see Track data changes from a user-created MySQL database or an ApsaraDB RDS for MySQL instance (new version) or Track data changes from a PolarDB-X instance. One or more consumer groups are created. For more information, see Create a consumer group. Precautions If you enable auto commit when you use the change tracking feature, some data may be committed before it is consumed. This results in data loss. We recommend that you manually commit data.

> Not e If data fails to be committed due to a fault, you can restart the client to continue consuming data from the last recorded consumer offset. However, duplicate data may be generated during this period. You must manually filter out the duplicate data.

Data is serialized and stored in the Avro format. For more information, see Record.avsc.

> Not e If the client that you use is not a Kafka client, you must parse the tracked data based on the Avro schema.

Regarding the `offsetFotTimes` interface, the search unit of DTS is seconds, and the search unit of native Kafka is milliseconds. Download and run the demo code of the Kafka client Click here to download the demo code of the Kafka client. Download and run the demo code of the Kafka client

| Step | File or directory |
|---|---|
| 1. Use the native Kafka consumer to obtain incremental data from the change tracking instance. | subscribe example- _ master/javaimpl/src/main/java/r ecordgenerator/ |
| 2. Deserialize the image of the incremental data, and obtain attributes such as the pre-image and post-image. | subscribe example- _ master/javaimpl/src/main/java/b oot/MysqlRecordPrinter.java |

| Step | File or directory |
|---|---|
| 3. Convert the dataTypeNumber values in the deserialized data into MySQL or Oracle data types. Not e For more information, see Mappings between MySQL data types and dataTypeNumber values and Mappings between Oracle data types and dataTypeNumber values. | subscribe example- _ master/javaimpl/src/main/java/r ecordprocessor/mysql/ |

Procedure This procedure uses IntelliJ IDEA (Community Edition 2018.1.4 Windows) as an example.
1. Download the demo code of the Kafka client, and then decompress the package.
2. Open IntelliJ IDEA. In the window that appears, click Open.
3. In the dialog box that appears, go to the directory in which the downloaded demo code resides.
Find the pom.xml file.
4. In the dialog box that appears, select Open as Project .
5. On the IntelliJ IDEA page, expand folders to find the demo file of the Kafka client, and double-click
the file. The file name is NotifyDemo.java.
6. Set the parameters in the NotifyDemo.java file.

| Parameter | Description | Method to obtain |
|---|---|---|

|   | Parameter |   |   | Description |   |   |   |   | Method to obtain |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   | USER NAME _ |   |   | The username of the consumer group. Warning If you are not using the Kafka client that is described in this topic, you must specify the username in the following format: <Consumer |   |   |   |   | In the DTS console, click the instance ID, and then click Dat a Consume. You can obtain the Consumer Group ID and the corresponding Account information. Not e The password of the consumer group account is specified when you create a consumer group. |   |
|   |   |   |   |   | Warning If you are not using the Kafka client that is described in this topic, you must specify the username in the following format: <Consumer |   |   |   |   |   |
|   |   |   |   |   |   | <Consumer |   |   | obtain the Consumer Group ID an |   |
|   |   |   |   |   | group account>-<Consumer gr |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | the |   |
|   |   |   |   |   | oup ID> |   | dtste |   |   |   |
|   | PASSWORD NAME _ |   |   | The password of the account. |   |   |   |   |   |   |
|   | SID NAME _ |   |   | The ID of the consumer group. |   |   |   |   |   |   |
|   | GROUP NAME _ |   |   | The name of the consumer group. Set this parameter to the consumer group ID. |   |   |   |   |   |   |
|   | KAFKA TOPIC _ |   |   | The topic of the change tracking task. |   |   |   |   | In the DTS console, click the instance ID. On the T rack Dat a Changes page, you can obtain the t racked t opic, network address, and port number. |   |
|   | KAFKA BROKER UR _ _ L NAME _ |   |   | The network address and port number of the change tracking task. Not e If you track data changes over internal networks, the network latency is minimal. This is applicable if the ECS instance where you deploy the Kafka client belongs to the same VPC or classic network as the change tracking instance. |   |   |   |   |   |   |

| Parameter | Description | Method to obtain |
|---|---|---|
| INITIAL CHECKPOIN _ T NAME _ | The consumer offset of consumed data. The value is a UNIX timestamp. Not e You must save the consumer offset. If the consumption process is interrupted, you can specify the consumer offset on the change tracking client to resume data consumption. This allows you to prevent against data loss. When you start the change tracking client, you can specify the consumer offset to consume data on demand. | When you use the Kafka client to track data changes for the first time, convert the required time point into a UNIX timestamp. |
| USE CONFIG CHEC _ _ KPOINT NAME _ | Default value: true. The default value indicates that the client is forced to consume data from the specified consumer offset. This allows you to retain the data that is received but not processed. | None. |

7. On the top of the IntelliJ IDEA page, choose Run > Run to run the client.

> Not e When you run IntelliJ IDEA for the first time, it loads and installs the relevant dependency.

Execution result The following figure shows that the Kafka client can track data changes in the source database. You can also delete the `//` characters from the //log.info(ret); string in line 25 of the NotifyDemo.java file. Then, run the client again to view the data change information. Mappings between MySQL data types and dataTypeNumber values

| MySQL data type | Value of dataTypeNumber |
|---|---|
| MYSQL TYPE DECIMAL _ _ | 0 |

| ata Transmission Service | User Guide·Change trackin |
|---|---|
| MySQL data type | Value of dataTypeNumber |
| MYSQL TYPE INT8 _ _ | 1 |
| MYSQL TYPE INT16 _ _ | 2 |
| MYSQL TYPE INT32 _ _ | 3 |
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

| ser Guide·Change tracking | Data Transmission Servic |
|---|---|

| MySQL data type | Value of dataTypeNumber |
|---|---|
| MYSQL TYPE BLOB _ _ | 252 |
| MYSQL TYPE VAR STRING _ _ _ | 253 |
| MYSQL TYPE STRING _ _ | 254 |
| MYSQL TYPE GEOMETRY _ _ | 255 |

Mappings between Oracle data types and dataTypeNumber values

| Oracle data type | Value of dataTypeNumber |
|---|---|
| VARCHAR2/NVARCHAR2 | 1 |
| NUMBER/FLOAT | 2 |
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

|   | Data Transmission Service | User Guide·Change trackin | g |
|---|---|---|---|

| Oracle data type | Value of dataTypeNumber |
|---|---|
| TIMESTAMP WITH LOCAL TIME ZONE _ _ _ _ | 231 |
