---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Transmission Service User Guide 20230625"
product_version: "V3.16.2"
doc_version: "20230625"
pdf_pages: 325
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Transmission Service User Guide 20230625.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230609/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Data%20Transmission%20Service%20User%20Guide%2020230625.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Data Transmission Service User Guide 20230625

## What is DTS?

Data Transmission Service (DTS) is a data service that is provided by Alibaba Cloud. DTS supports data transmission between various types of data sources, such as relational databases and big data systems. Compared with traditional data migration or synchronization tools, DTS provides diverse features and high performance, security, reliability, and ease of use. DTS helps you simplify data transmission and focus on your application development. le

## Log on to the DTS console

This topic describes how to log on to the Data Transmission Service (DTS) console. Google Chrome is used in this example. Prerequisites The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. A browser is available. We recommend that you use the Google Chrome browser. Procedure
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Dat a T ransmission Service.
5. Select an organizat ion and region, and then click DT S.

## Data migration

### Supported databases and

migration types You can use Data Transmission Service (DTS) to migrate data between homogeneous data sources or between heterogeneous data sources. This feature is suitable for the following scenarios: data migration to Alibaba Cloud, data migration between instances within Alibaba Cloud, and database splitting and scale-out. This topic describes the database types, database versions, and migration types that are supported by data migration.

| Source database | Destination database | Migration type |
|---|---|---|
| Self-managed MySQL database Version 5.1, 5.5, 5.6, 5.7, or 8.0 ApsaraDB RDS for MySQL All versions | Self-managed MySQL database Version 5.1, 5.5, 5.6, 5.7, or 8.0 | Schema migration Full data migration Incremental data migration |
|   | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration Incremental data migration |
|   | PolarDB-X (formerly known as DRDS) All versions | Full data migration Incremental data migration |
|   | Self-managed Oracle database (RAC or non-RAC architecture) Versions 9i, 10g, 11g, 12c, 18c, and 19c | Full data migration Incremental data migration |

| Source database | Destination database | Migration type |
|---|---|---|
|   | Self-managed Kafka cluster Versions 0.1 to 2.0 | Schema migration Full data migration Incremental data migration |
| Self-managed SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, 2016, and 2017 Not e DTS does not support SQL Server clusters or SQL Server AlwaysOn availability groups (AOAGs). If the version of the source database is 2005, incremental data migration is not supported. | Self-managed SQL Server database Versions 2005, 2008, 2008 R2, 2012, 2014, 2016, and 2017 Not e DTS does not support SQL Server clusters or SQL Server AOAGs. ApsaraDB RDS for SQL Server Versions 2012, 2014, 2016, and 2017 | Schema migration Full data migration Incremental data migration |
|   | Self-managed Oracle database (RAC or non-RAC architecture) Versions 9i, 10g, 11g, 12c, 18c, and 19c | Schema migration Full data migration Incremental data migration |
|   | PolarDB for Oracle Versions 9.3, 9.6, 10, and 11 | Schema migration Full data migration Incremental data migration |
|   | Self-managed MySQL database Version 5.1, 5.5, 5.6, 5.7, or 8.0 | Schema migration Full data migration Incremental data migration |

| Source database | Destination database | Migration type |
|---|---|---|
| Self-managed Oracle database (RAC or non-RAC architecture) Versions 9i, 10g, 11g, 12c, 18c, and 19c | ApsaraDB RDS for MySQL All versions | Schema migration Full data migration Incremental data migration |
|   | PolarDB-X All versions | Full data migration Incremental data migration |
|   | AnalyticDB for MySQL Version 2.0 | Schema migration Full data migration Incremental data migration |
|   | AnalyticDB for PostgreSQL (formerly known as HybridDB for PostgreSQL) Versions 4.3 and 6.0 | Schema migration Full data migration Incremental data migration |
|   | Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 | Schema migration Full data migration Incremental data migration |
| Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 ApsaraDB RDS for PostgreSQL Versions 9.4 and 10 | Self-managed PostgreSQL database Versions 9.4, 9.5, 9.6, 10.x, 11, and 12 ApsaraDB RDS for PostgreSQL Versions 9.4 and 10 | Schema migration Full data migration Incremental data migration |

| Source database | Destination database | Migration type |
|---|---|---|
| PolarDB for Oracle Versions 9.3, 9.6, 10, and 11 | Self-managed Kafka cluster Versions 0.1 to 2.0 | Incremental data migration |
|   | Self-managed Oracle database (RAC or non-RAC architecture) Versions 9i, 10g, 11g, 12c, 18c, and 19c | Full data migration Incremental data migration |
|   | PolarDB for Oracle Versions 9.3, 9.6, 10, and 11 | Schema migration Full data migration Incremental data migration |
| Self-managed Redis database Version 2.8, 3.0, 3.2, 4.0, or 5.0 | Self-managed Redis database Version 2.8, 3.0, 3.2, 4.0, or 5.0 | Full data migration Incremental data migration |
| Self-managed MongoDB database Versions 3.0, 3.2, 3.4, 3.6, 4.0 and 4.2 | Self-managed MongoDB database Versions 3.0, 3.2, 3.4, 3.6, 4.0 and 4.2 | Full data migration Incremental data migration |
| MaxCompute All versions | Self-managed MySQL database Version 5.1, 5.5, 5.6, 5.7, or 8.0 ApsaraDB RDS for MySQL All versions | Schema migration Full data migration |
| PolarDB-X 2.0 | PolarDB-X 2.0 Not e Make sure that the PolarDB-X 2.0 instances are compatible with MySQL V5.7. AnalyticDB for PostgreSQL | Schema migration Full data migration Incremental data migration |

### Create a data migration instance

Before you configure a task to migrate data, you must create a data migration instance. This topic describes how to create a data migration instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. In the upper-left corner of the Data Migration page, click Creat e T ask.
4. In the panel that appears, select the source and destination regions, and specify the number of data
migration instances that you want to create. In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.
5. Click Purchase Inst ance.

### Configure data migration tasks

#### Migrate data from a self-managed MySQL

database to an ApsaraDB RDS for MySQL instance This topic describes how to migrate data from a self-managed MySQL database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity. Prerequisites The engine version of the self-managed MySQL database is 5.1, 5.5, 5.6, 5.7, or 8.0. To ensure compatibility, the version of the destination ApsaraDB RDS for MySQL database must be the same as or later than the version of the source self-managed MySQL database. The available storage space of the destination ApsaraDB RDS for MySQL database is larger than the total size of the data in the self-managed MySQL database. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | To ensure compatibility, the version of the destination ApsaraDB RDS for MySQL database must be the same as or later than the version of the source self-managed MySQL database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
| Special cases | If the source database is a self-managed MySQL database, take note of the following limits: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Not e If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. |

Migration types Schema migration DTS migrates the schemas of the required objects to the destination instance. DTS supports schema migration for the following types of objects: table, view, trigger, stored procedure, and function. During schema migration, DTS changes the value of the SECURITY attribute in views, stored procedures, and functions from DEFINER to INVOKER. DTS does not migrate user information. Before a user can call views, stored procedures, and functions of the destination database, you must grant the read/write permissions to the user. Full data migration DTS migrates historical data of the required objects from the user-created MySQL database to the destination database in the ApsaraDB RDS for MySQL instance. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination instance. After full data migration is complete, the tablespace of the destination instance is larger than that of the source database. Incremental data migration After full data migration is complete, DTS retrieves binary log files from the user-created MySQL database. Then, DTS synchronizes incremental data from the user-created MySQL database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from a user-created MySQL database to Alibaba Cloud. SQL operations that can be synchronized during incremental data migration

| Operat i on t ype | SQL st at ement |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE TRUNCATE TABLE |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select MySQL. |
|   | Hostname or IP Address | The endpoint that is used to access the self-managed MySQL database. |
|   | Port Number | The service port number of the self-managed MySQL database. Default value: 3306. |
|   | Database Account | The account of the self-managed MySQL database. If you need to perform incremental data migration, the account must have the SELECT permission on the objects to be migrated, the REPLICATION SLAVE permission, the REPLICATION CLIENT permission, and the SHOW VIEW permission. If you need to perform full data migration or schema migration, the account must have the SELECT permission on the objects to be migrated. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The access method of the destination database. Select RDS Inst ance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If an IP address whitelist is configured for the self-managed MySQL database, you must manually add
the CIDR blocks of DTS servers to the IP address whitelist of the database. To obtain the CIDR blocks of DTS servers, click Copy in the dialog box that appears. After you add the CIDR blocks of DTS servers to the whitelist of the database, click Next . If you do not need to configure an IP address whitelist for the self-managed MySQL database, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Migration Types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. If you want to ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Rename databas es and tables | You can use the object name mapping feature to rename the objects that are migrated to the destination instance. For more information, see Object name mapping. |
| Specify the retry time range for failed connecti ons | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

| Paramet er or setting | Description |
|---|---|
| Specify whether to copy tempora ry tables to the destinati on databas e when Data Manage ment (DMS) performs online DDL operatio ns on the source tables | If you use DMS to perform online DDL operations on the source database, you can specify whether to migrate data of temporary tables generated by online DDL operations. Valid values: Yes: DTS migrates the data of temporary tables generated by online DDL operations. Not e If online DDL operations generate a large amount of data, the data migration task may take an extended period of time to complete. No: DTS does not migrate the data of temporary tables generated by online DDL operations. Only the original DDL data of the source database is migrated. Not e If you select No, the tables in the ApsaraDB RDS for MySQL instance may be locked. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is complete. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until the message T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed MySQL

database to a PolarDB-X instance This topic describes how to migrate data from a self-managed MySQL database to a PolarDB-X instance by using Data Transmission Service (DTS). PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). Prerequisites The engine version of the self-managed MySQL database is 5.1, 5.5, 5.6, 5.7, or 8.0. The available storage space of the PolarDB-X instance is larger than the total size of the data in the self-managed MySQL database. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. Incremental DDL operations cannot be migrated. If you perform DDL operations in the source database during incremental data migration, the data migration task fails. If you want to perform DDL operations, we recommend that you perform the operations in the destination database and then perform the same operations in the source database. |

| Category | Description |   |   |
|---|---|---|---|
| Other limits | The storage type of the PolarDB-X instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION ) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |   |   |
|   |   | ROUND(COLUMN,PRECISION |   |
| Special cases | If the source database is a self-managed MySQL database, take note of the following limits: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Not e If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |   |   |

|   | ) |
|---|---|

SQL operations that can be incrementally migrated INSERT, UPDATE, and DELETE Permissions required for database accounts

| Database | Full data migration | Incremental data migration |
|---|---|---|
| Self-managed MySQL database | SELECT permission | REPLICATION SLAVE, REPLICATION CLIENT, SHOW VIEW, and SELECT permissions |
| PolarDB-X instance | Read and write permissions | Read and write permissions |

Procedure
1. Create databases and tables in the destination PolarDB-X instance based on the schemas of the
source tables.
2. Purchase a DTS instance. For more information, see Create a data migration instance.
3. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
4. Configure the source and destination databases. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select MySQL. |
|   | Hostname or IP Address | The endpoint that is used to access the self-managed MySQL database. |
|   | Port Number | The service port number of the self-managed MySQL database. Default value: 3306. |
|   | Database Account | The account of the self-managed MySQL database. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |
|   | Instance Type | The access method of the destination database. Select DRDS Inst ance. |

| r Guide·Data |   |   |
|---|---|---|
|   | migration Data Transmission Servic |   |
| Section | Parameter | Description |
| Destination Database | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Version | The version of the destination PolarDB-X instance. Select 1.0 or 2.0 based on your business requirements. |
|   | DRDS Instance ID | The ID of the destination PolarDB-X instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the PolarDB-X instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Database Password | The password of the database account. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. If an IP address whitelist is configured for the self-managed MySQL database, you must manually add
the CIDR blocks of DTS servers to the IP address whitelist of the database. To obtain the CIDR blocks of DTS servers, click Copy in the dialog box that appears. After you add the CIDR blocks of DTS servers to the whitelist of the database, click Next . If you do not need to configure an IP address whitelist for the self-managed MySQL database, ignore the preceding settings and click Next .
7. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Full Dat a Migrat ion. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Paramet er or setting | Description |
|---|---|
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Rename databas es and tables | You can use the object name mapping feature to rename the objects that are migrated to the destination instance. For more information, see Object name mapping. |
| Specify the retry time range for failed connecti ons | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

8. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from an ApsaraDB RDS for

MySQL instance to a self-managed Oracle database This topic describes how to migrate data from an ApsaraDB RDS for MySQL instance to a self-managed Oracle database by using Data Transmission Service (DTS). DTS supports full data migration and incremental data migration. You can select the two migration types to ensure service continuity of the source ApsaraDB RDS for MySQL instance during data migration. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error _ _ messages are returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Category | Description |   |   |
|---|---|---|---|
| Other limits | Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION ) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |   |   |
|   |   | ROUND(COLUMN,PRECISION |   |

|   | ) |
|---|---|

Permissions required for database accounts

| Migration type | Full data migration | Incremental data migration |
|---|---|---|
| Source ApsaraDB RDS for MySQL instance | Read and write permissions | Read and write permissions |
| Destination Oracle database | Read and write permissions | Read and write permissions on databases |

Procedure
1. Create a data migration instance.
2. Find the data migration instance that you want to manage and click Conf igure Migrat ion T ask in
the Actions column.
3. Optional. Enter a name for the task.
DTS automatically generates a name for each task. Duplicate task names are allowed. You can edit the task name based on your business requirements. We recommend that you specify a descriptive name for easy identification.
4. Configure the source and destination databases. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Source Database | Database Type | The instance type of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source instance resides. |
|   | RDS Instance ID | The ID of the source database. |
|   | Database Account | The database account of the source instance. The account must have the read and write permissions on the source database. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The instance type of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. |
|   | Database Type | The type of the destination database. Select Oracle. |
|   | Hostname or IP Address | The endpoint of the destination database. |
|   | Port Number | The port number of the destination database. Default value: 1521. |
|   | Database Type | The architecture of the destination Oracle database. If you select Non-RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must specify the Service Name parameter. |
|   | Database Account | The account of the destination database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

5. Click T est Connect ivit y and confirm that the test results for both the source and destination
databases are Passed.
6. In the lower-right corner of the page, click Set Whit elist and Next .
7. Select the migration types based on your business requirements. Select one or more objects from the
Source Objects section and click the icon to move the objects to the Select ed Object s section. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. To perform only full data migration, select Full Dat a Migrat ion.
8. Click Precheck and wait until the precheck is complete.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
9. Click Next to start the migration task.
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from an ApsaraDB RDS for

MySQL instance to a self-managed Kafka cluster Kafka is a distributed message queue service that supports high throughput and high scalability. Kafka is widely used for big data analytics such as log collection, monitoring data aggregation, streaming processing, and online and offline analysis. Kafka is an essential service for the big data ecosystem. You can migrate data from a self-managed MySQL database or an ApsaraDB RDS for MySQL instance to a self-managed Kafka cluster by using Data Transmission Service (DTS). The data migration feature allows you to extend message processing capabilities. This topic describes how to migrate data from an ApsaraDB RDS for MySQL instance to a self-managed Kafka cluster by using DTS. Prerequisites The destination Kafka cluster is created and the Kafka version is 0.10 to 2.0. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck and the data migration task cannot be started. Binary logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during full data migration, DTS cannot obtain the binary logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

|   | Category | Description |
|---|---|---|
|   | Other limits | The service port of the Kafka cluster must be accessible over the Internet. You can select only tables as the objects to be migrated. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

Data format The data that is migrated to the Kafka cluster is stored in the Avro format. You must parse the data based on the schema definition of DTS Avro. For more information, visit GitHub. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure a task name.
DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
|   | Database Type | The instance type of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source database resides. |

| a Transmission Ser |   |   |
|---|---|---|
|   | vice User Guide·Data migratio |   |
| Section Source | Parameter | Description |
| Database | RDS Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source instance. The account must have the SELECT permission on the objects to be migrated and the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions. |
|   | Database Password | The password of the database account. |
| Destination Database | Database Type | The instance type of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Kaf ka. |
|   | Hostname or IP Address | The IP address that is used to access the self-managed Kafka cluster. In this example, the public IP address is used. |
|   | Port Number | The service port number of the Kafka cluster. Default value: 9092. |
|   | Database Account | The username that is used to log on to the Kafka cluster. If no authentication is enabled for the Kafka cluster, you do not need to enter the username. |
|   | Database Password | The password of the database account. If no authentication is enabled for the Kafka cluster, you do not need to enter the password. |
|   | Topic | The name of the topic to which data is migrated. Click Get T opic List and select a topic name from the drop-down list. |
|   | Topic That Stores DDL Information | The topic that is used to store the DDL information. Click Get T opic List and select a topic name from the drop-down list. If you do not specify this parameter, the DDL information is stored in the topic that is specified by the T opic parameter. |
|   | Kafka Version | The version of the destination Kafka cluster. Not e You cannot select Kafka 2.0 in the DTS console. If you are using Kafka 2.0, you must select Kafka 1.0. |
|   | Encryption | Specifies whether to encrypt the connection to the destination cluster. Select Non-encrypt ed or SCRAM-SHA-256 based on your business and security requirements. |

|   | tion | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
|   | Use Kafka Schema Registry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. Select the objects to be migrated and the migration types.

| Set t ing | Descript ion |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
|   | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Select the objects to be migrated |   |

| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |
|---|---|

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed SQL

Server database to an ApsaraDB RDS for SQL Server instance This topic describes how to migrate incremental data from a self-managed SQL Server database to an ApsaraDB RDS for SQL Server instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity. Prerequisites The version of the self-managed SQL Server database is 2005, 2008, 2008 R2, 2012, 2014, 2016, or 2017. DTS does not support SQL Server clusters or SQL Server AlwaysOn availability groups (AOAGs). If the version of the source database is 2005, incremental data migration is not supported. To ensure compatibility, the version of the destination instance must be the same as or later than the version of the source instance. The tables to be migrated from the self-managed SQL Server database have primary keys or UNIQUE NOT NULL indexes. Limits

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. The backup mode must be set to Full, and full logical backup must be performed. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | A single data migration task can migrate incremental data from only one database. To migrate incremental data from multiple databases, you must create a data migration task for each database. DTS does not migrate data of the following types: CURSOR, ROWVERSION, SQL VARIANT, _ HIERACHYID, and GEOMETRY. DTS does not migrate heap tables, tables that contain non-clustered indexes, or tables that contain computed columns. To ensure compatibility, the version of the destination instance must be the same as or later than the version of the source instance. To ensure that the latency of incremental data migration is accurate, DTS adds a heartbeat table to the self-managed SQL Server database. The name of the heartbeat table is in the source table name dts mysql heartbeat format. _ _ _ If you perform a primary/secondary switchover on the source and destination databases when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
| Special cases | If the destination instance is an ApsaraDB RDS for SQL Server instance, take note of the following limits: DTS automatically creates a destination database in the ApsaraDB RDS for SQL Server instance. However, if the name of the database to be migrated does not conform to the naming conventions of ApsaraDB RDS, you must manually create a database in the destination ApsaraDB RDS for SQL Server instance before you configure the data migration task. |

Migration types Schema migration DTS migrates the schemas of the required objects from the source database to the destination database. DTS supports schema migration for the following types of objects: table, view, trigger, synonym, SQL stored procedure, SQL function, plan guide, user-defined type, rule, and default. Full data migration DTS migrates historical data of objects from the self-managed SQL Server database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the self-managed SQL Server database to the destination database. Incremental data migration allows you to ensure service continuity when you migrate data from a self-managed SQL Server database to an Alibaba Cloud instance. SQL operations that can be incrementally migrated INSERT, UPDATE, and DELETE If an UPDATE operation updates only the large fields, DTS does not migrate the operation. CREATE TABLE If a CREATE TABLE operation creates a partitioned table or a table that contains functions, DTS does not migrate the operation. ALTER TABLE, including only ADD COLUMN, DROP COLUMN, and RENAME COLUMN DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX Migration process To prevent data migration failures caused by dependencies among objects, DTS migrates the schemas and data from the source SQL Server database in the following order:
1. Migrate the schemas of tables, views, synonyms, user-defined types, rules, defaults, and plan guides.
2. Perform full data migration.
3. Migrate the schemas of SQL stored procedures, SQL functions, triggers, and foreign keys.
4. Perform incremental data migration.
During incremental data migration, we recommend that you do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. Preparations To perform incremental data migration, configure log settings on the self-managed SQL Server database. Skip this step if you do not need to perform incremental data migration.
1. Run the following command in the self-managed SQL Server database to change the recovery model
to full:

```
use master;
```

`GO`

```
ALTER DATABASE <database_name> SET RECOVERY FULL WITH ROLLBACK IMMEDIATE;
```

`GO` Parameter: <database_name>: the name of the source database. Example:

```
use master;
```

`GO`

```
ALTER DATABASE mytestdata SET RECOVERY FULL WITH ROLLBACK IMMEDIATE;
```

`GO`
2. Run the following command to create a logical backup for the source database. Skip this step if you
have already created a logical backup.

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
4. Create a clustered index for each source table. For more information, see Create Clustered Indexes.
Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select SQL Server. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed SQL Server database. |
|   | Port Number | The service port number of the self-managed SQL Server database. Default value: 1433. |
|   | Database Account | The account of the source self-managed SQL Server database. Not e To perform incremental data migration, the account must have the sysadmin permission. To perform schema migration or full data migration, the account must have the SELECT permission on the objects to be migrated. In this example, a self-managed SQL Server database is used as the source database. If your source database is an ApsaraDB RDS for SQL Server instance, you must use a privileged database account. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The instance type of the destination database. Select RDS Inst ance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for SQL Server instance. Not e In this scenario, the destination database can be only a SQL Server database. |

|   | Service User Guide·Data migratio |   |
|---|---|---|
| Section | Parameter | Description |
|   | Database Account | The database account of the destination ApsaraDB RDS for SQL Server instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If a whitelist is configured for the self-managed SQL Server database, you must manually add the
CIDR blocks of DTS servers to the whitelist of the database. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelist of the database, click Next . If you do not need to configure a whitelist for the self-managed SQL Server database, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. If you want to ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |
| Specify whether to copy tempora ry tables to the destinati on databas e when Data Manage ment (DMS) performs online DDL operatio ns on the source tables | If you use DMS to perform online DDL operations on the source database, you can specify whether to migrate data of temporary tables generated by online DDL operations. Valid values: Yes: migrates the temporary tables generated by online DDL operations. Not e If online DDL operations generate a large amount of data, the data migration task may take an extended period of time to complete. No: does not migrate the temporary tables generated by online DDL operations. Only the original DDL data of the source database is migrated. Not e If you select No, the tables in the destination database may be locked. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data between self-managed

Oracle databases This topic describes how to migrate data between self-managed Oracle databases by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all the supported migration types to ensure service continuity. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The engine version of the source Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. To ensure compatibility, the version of the destination Oracle database must be the same as or later than the version of the source Oracle database. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the source Oracle database. For more information, see Supplemental Logging. The source Oracle database is running in ARCHIVELOG mode. Archived log files are accessible and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. The available storage space of the destination Oracle database is larger than the total size of the data in the source Oracle database. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source and destination databases when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

Migration types

| Migrat ion t ype | Descript ion |
|---|---|
| Schema migration | DTS migrates the schemas of the required objects to the destination Oracle database. DTS supports schema migration for the following types of objects: table, view, synonym, trigger, stored procedure, function, package, and user- defined type. Not e If an object contains triggers, the data between the source and destination databases will become inconsistent. |
| Full data migration | DTS migrates historical data of the required objects from the source Oracle database to the destination Oracle database. Not e During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration, DTS retrieves redo log files from the source Oracle database. Then, DTS synchronizes incremental data from the source Oracle database to the destination Oracle database. Incremental data migration allows you to ensure service continuity when you migrate data between Oracle databases. |

Permissions required for database accounts

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source Oracle database | Owner permissions on schemas | Owner permissions on schemas | Permissions of database administrator (DBA) |
| Destination Oracle database | Owner permissions on schemas | Owner permissions on schemas | Owner permissions on schemas |

For more information about how to create an Oracle database account and grant permissions to the database account, see CREATE USER and GRANT. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source Oracle database. |
|   | Port Number | The port number of the source Oracle database. Default value: 1521. |
|   | Instance Type | The architecture of the source database. Select Non-RAC Inst ance or RAC or PDB Inst ance based on the architecture of the source Oracle database. |
|   | SID | The system ID (SID) of the source Oracle database. Not e This parameter is required if you select Non-RAC Inst ance as the instance type. |

| Section | Parameter | Description |
|---|---|---|
|   | Service Name | The server name of the source database. Not e This parameter is required if you select RAC or PDB Inst ance as the instance type. |
|   | Database Account | The account that is used to connect to the source Oracle database. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the destination Oracle database. |
|   | Port Number | The port number of the destination Oracle database. Default value: 1521. |
|   | Instance Type | The architecture of the destination database. Select Non-RAC Inst ance or RAC or PDB Inst ance based on the architecture of the destination Oracle database. |
|   | SID | The SID of the destination Oracle database. Not e This parameter is required if you select Non-RAC Inst ance as the instance type. |
|   | Service Name | The server name of the destination database. Not e This parameter is required if you select RAC or PDB Inst ance as the instance type. |
|   | Database Account | The account that is used to connect to the destination Oracle database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed Oracle

database to an ApsaraDB RDS for MySQL instance This topic describes how to migrate data from a self-managed Oracle database to an ApsaraDB RDS for MySQL instance by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. When you migrate data from a self-managed Oracle database, you can select all the supported migration types to ensure service continuity. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files. Limits

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
| Special cases | If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: Table names in the ApsaraDB RDS for MySQL instance are case-insensitive. If a table name in the source Oracle database contains uppercase letters, ApsaraDB RDS for MySQL converts all uppercase letters to lowercase letters before a table is created. If the source Oracle database contains identical table names that differ only in capitalization, these table names are identified as duplicate. As a result, the "The object already exists" message may be displayed during schema migration. To prevent name conflicts in the destination database, you can use the object name mapping feature to capitalize the table names. For more information, see Object name mapping. DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. |

Migration types Schema migration DTS supports schema migration for tables and indexes. DTS does not support schema migration for the following types of objects: view, synonym, trigger, stored procedure, function, package, and user-defined type. DTS has the following limits on schema migration for tables and indexes: Schema migration of nested tables is not supported. Clustered tables and index-organized tables (IOTs) are converted into common tables in the destination database. Schema migration of function-based indexes, domain indexes, bitmap indexes, and reverse indexes is not supported. Full data migration DTS migrates historical data of the required objects from the user-created Oracle database to the destination ApsaraDB RDS for MySQL instance. Incremental data migration DTS retrieves redo log files from the user-created Oracle database. Then, DTS synchronizes incremental data from the user-created Oracle database to the destination database in the ApsaraDB RDS for MySQL instance. Incremental data migration allows you to ensure service continuity when you migrate data from the user-created Oracle database to the destination database. SQL operations that can be incrementally migrated INSERT, DELETE, and UPDATE CREATE TABLE DTS does not migrate the CREATE TABLE operations that are performed to create tables in which functions are nested. ALTER TABLE, ADD COLUMN, DROP COLUMN, RENAME COLUMN, and ADD INDEX DROP TABLE RENAME TABLE, TRUNCATE TABLE, and CREATE INDEX Data type mappings For more information, see Data type mappings between heterogeneous databases. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |

|   | Service User Guide·Data migratio |   |
|---|---|---|
| Section | Parameter | Description |
|   | Instance Type | The architecture type of the self-managed Oracle database. If you select Non-RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must specify the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The access method of the destination database. Select RDS Inst ance. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for failed connecti ons | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed Oracle

database to a PolarDB for Oracle cluster This topic describes how to migrate data from a self-managed Oracle database to a PolarDB for Oracle cluster by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

Limits on features During schema migration, the reverse indexes and bitmap indexes of the source database are stored as common indexes in the PolarDB for Oracle cluster. During schema migration, partitioned indexes are converted into independent indexes on each partition in the PolarDB for Oracle cluster. Incremental data migration supports only tables that have primary keys or UNIQUE NOT NULL indexes. Data of the LONG type cannot be migrated during incremental data migration. DDL operations that are performed during incremental data migration cannot be migrated to the destination database. DTS does not migrate materialized views. Data type mappings For more information, see Data type mappings between heterogeneous databases. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Instance Type | The access method of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. |

| r Guide·Data | migration | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
| Source Database | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Instance Type | The architecture of the source Oracle database. If you select Non- RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must specify the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select PolarDB-O. |
|   | Domain Name or IP Address | The endpoint of the destination PolarDB for Oracle cluster. |
|   | Port Number | The service port number of the destination PolarDB for Oracle cluster. Default value: 1521. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination PolarDB for Oracle cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to move the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed Oracle

database to a PolarDB-X instance This topic describes how to migrate data from a self-managed Oracle database to a PolarDB-X instance by using Data Transmission Service (DTS). DTS allows you to ensure service continuity when you perform full data migration and incremental data migration. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination instance after a failed data migration task is resumed. |

Migration types Full data migration DTS migrates the historical data of objects from the source Oracle database to the destination database. Incremental data migration After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database. The following SQL operations can be migrated during incremental data migration: INSERT, DELETE, and UPDATE operations. DDL operations cannot be migrated during incremental data migration. Procedure
1. Create databases and tables in the destination PolarDB-X instance based on the schemas of the
source tables. The data types of Oracle and PolarDB-X do not have one-to-one correspondence. You must create the corresponding data types in the destination PolarDB-X instance. For more information, see Data type mappings between heterogeneous databases.
2. Purchase a DTS instance. For more information, see Create a data migration instance.
3. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. In this example, the public IP address of the database is used. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Instance Type | The architecture type of the self-managed Oracle database. If you select Non-RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must specify the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The instance type of the destination database. Select DRDS Inst ance. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | Version | Select 1.0 or 2.0 based on your business requirements. |
|   | DRDS Instance ID | The ID of the destination PolarDB-X instance. |
|   | Database Account | The database account of the destination PolarDB-X instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
7. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. If you want to ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename an object that is migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

8. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed Oracle

database to an AnalyticDB for PostgreSQL instance This topic describes how to migrate data from a self-managed Oracle database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data migration feature allows you to transfer and analyze data with ease. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

Migration types

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of required objects from the source database to the destination database. DTS supports schema migration for the following types of objects: table, index, constraint, function, sequence, and view. Warning In this topic, the source and destination databases are heterogeneous databases. DTS does not ensure that the schemas of the source and destination databases are consistent after schema migration. We recommend that you evaluate the impact of data type conversion on your business. For more information, see Data type mappings between heterogeneous databases. For partitioned tables, DTS discards the partition definitions. You must define partitions in the destination database. |
| Full data migration | DTS migrates the historical data of required objects from the source database to the destination database. Not e During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |

| Migration type | Description |
|---|---|
| Incremental data migration | After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database in real time. DTS can migrate the following SQL operations during incremental data migration: DML operations: INSERT, UPDATE, and DELETE DDL operation: ADD COLUMN Incremental data migration ensures service continuity of self-managed applications during data migration. |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the destination database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this value, you must specify the SID parameter. RAC or PDB Inst ance: If you select this value, you must specify the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | > Document Version: 2023062 |   |

|   | Service | User Guide·Data migratio |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | Select Analyt icDB f or Post greSQL. |
|   | Instance Region | The destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination AnalyticDB for PostgreSQL instance. The account must have the read and write permissions on the instance. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Set t ing | Descript ion |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a self-managed Oracle

database to a self-managed PostgreSQL database This topic describes how to migrate data from a self-managed Oracle database to a self-managed PostgreSQL database by using Data Transmission Service (DTS). Schema migration, full data migration, and incremental data migration ensure service continuity when you perform data migration. Prerequisites A license is purchased for your extension plan of DTS Advanced Edition. The license ensures that a self-managed Oracle database can be used as the source database for data migration. The version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database runs in ARCHIVELOG mode. Archived log files of the Oracle database are accessible, and an appropriate retention period is specified for the archived log files. For more information, see Managing Archived Redo Log Files. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. Requirements for the objects to be migrated: The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be migrated cannot exceed 30 bytes in length. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you perform a primary/secondary switchover on the source and destination databases when the data migration task is running, the task fails. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |

Migration types

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of required objects from the source database to the destination database. DTS can migrate the following objects: tables, views, and indexes. |
| Full data migration | DTS migrates the historical data of required objects from the source database to the destination database. Not e During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | After full data migration is complete, DTS retrieves redo log files from the source Oracle database. Then, DTS migrates incremental data from the source Oracle database to the destination database in real time. DTS can migrate the following SQL operations during incremental data migration: DML operations: INSERT, UPDATE, and DELETE Incremental data migration ensures service continuity of self-managed applications during data migration. |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. In this example, the public IP address of the database is used. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Instance Type | The architecture type of the self-managed Oracle database. If you select Non-RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must specify the Service Name parameter. |
|   | Database Account | The account of the self-managed Oracle database. To perform incremental data migration, the account must have the database administrator (DBA) permissions. To perform schema migration or full data migration, the account must have the owner permissions on schemas. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The instance type of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Post greSQL. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed PostgreSQL database. In this example, the public IP address is entered. |
|   | Port Number | The service port number of the self-managed PostgreSQL database. Default value: 3433. |
|   | Database Name | The name of the self-managed PostgreSQL database to which you want to migrate objects. |

|   | Service | User Guide·Data migratio |
|---|---|---|
| Section | Parameter | Description |
|   | Database Account | The account of the self-managed PostgreSQL database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed Oracle databases, you must manually add the
CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelists of the databases, click Next . If you do not need to configure whitelists for your Oracle databases, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. If you want to ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename an object that is migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data between ApsaraDB RDS for

PostgreSQL instances This topic describes how to migrate data between ApsaraDB RDS for PostgreSQL instances by using Data Transmission Service (DTS). DTS supports schema migration, full data migration, and incremental data migration. You can select all of the supported migration types to ensure service continuity. Prerequisites The network type of both the source and destination ApsaraDB RDS for PostgreSQL instances is Virtual Private Cloud (VPC). Limits

|   | Category | Description |   |   |
|---|---|---|---|---|
|   | Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The data logging feature must be enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, the DTS server stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, the DTS server automatically clears the logs that exceed the limit. Warning If you clear the data logs of the source database during full data migration, the task may fail to migrate incremental data. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the task may fail to migrate incremental data. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |   |   |
|   |   | To ensure that the data migration task runs as expected, you can perform primary/secondary switchover only on an ApsaraDB RDS for PostgreSQL V11 instance during data migration. In this case, you must set the rds failover slot _ _ mode parameter to sync . _ Warning If you perform a primary/secondary switchover on an ApsaraDB RDS for PostgreSQL instance of another version when the data migration task is running, the task fails. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. The name of the source database cannot contain hyphens (-). For example, dts- testdata is not allowed. |   |   |
|   |   |   | rds failover slot _ _ |   |

|   | mode _ |
|---|---|

|   | Category | DTS does not check the validity of metadata such as sequences. You must manually Description check the validity of metadata. |   |   |
|---|---|---|---|---|
|   |   | Data may be inconsistent between the primary and secondary nodes of the source database due to the latency of incremental data migration. Therefore, you must use the primary node as the data source when you migrate data. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of the used tablespace of the destination database is larger than that of the source database. If you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename the table during incremental data migration, you must execute the ALTER TABLE schema.table REPLICA IDE NTITY FULL; statement before you write data to the table. Not e Replace the schema and table variables in the preceding sample statement with your actual schema name and table name. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source database. _ _ Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During incremental data migration, DTS creates a replication slot for the source database. The replication slot is prefixed with dts sync . DTS automatically _ _ clears historical data in the replication slot every 90 minutes to reduce storage usage. Not e If the data migration task is released or fails, DTS automatically clears the replication slot. If a primary/secondary switchover is performed on the source ApsaraDB RDS for PostgreSQL instance, you must log on to the secondary database to manually clear the replication slot. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. After your workloads are switched to the destination database, newly written sequences do not increment from the maximum value of the sequences in the source database. Therefore, you must query the maximum value of the sequences in the source database before you switch your workloads to the destination database. Then, you must specify the queried maximum value as the starting value of the sequences in the destination database. For more information, see the |   |   |
|   |   |   | ALTER TABLE schema.table REPLICA IDE |   |
|   |   | NTITY FULL; |   |   |
|   | Other limits |   |   |   |

| Category | Statements to query the maximum value of the sequences in the source database Description |
|---|---|
|   | section of this topic. |
| Special cases | If the source or destination instance is an ApsaraDB RDS for PostgreSQL instance, take note of the following limits: During data migration, do not modify the endpoint and zone of the ApsaraDB RDS for PostgreSQL instance. Otherwise, the data migration task fails. |

Statements to query the maximum value of the sequences in the source database

```
do language plpgsql $$ declare
  nsp name;
  rel name;
  val int8;
begin
  for nsp,rel in select nspname,relname from pg_class t2 , pg_namespace t3 where t2.relname
space=t3.oid and t2.relkind='S'
  loop
    execute format($_$select last_value from %I.%I$_$, nsp, rel) into val;
    raise notice '%',
    format($_$select setval('%I.%I'::regclass, %s);$_$, nsp, rel, val+1);
  end loop;
end; $$;
```

Data migration process The following table describes how DTS migrates the schemas and data of the source ApsaraDB RDS for PostgreSQL instance. The process prevents data migration failures that are caused by dependencies between objects.

| Data migration process | Description |
|---|---|
| 1. Schema migration | DTS migrates the schemas of tables, views, sequences, functions, user-defined types, rules, domains, operations, aggregates, and stored procedures to the destination database. Not e DTS does not migrate functions that are written in the C programming language. |
| 2. Full data migration | DTS migrates all historical data of objects to the destination database. |
| 3. Schema migration | DTS migrates the schemas of triggers and foreign keys to the destination database. |

| Data migration process | Description |
|---|---|
| 4. Incremental data migration | After full data migration is complete, DTS migrates incremental data of objects to the destination database. Not e In this scenario, DTS can migrate only DML operations for incremental data migration, such as INSERT, DELETE, and UPDATE. Incremental data migration does not support the data of the BIT type. |

Preparations If you want to perform incremental data migration, you must perform the following steps: Log on to the ApsaraDB RDS console. Click the ID of the source ApsaraDB RDS for PostgreSQL instance. In the leftside navigation pane, click Paramet ers. Find the wal_level parameter and change the value of the parameter to logical. Warning After you change the value of the `wal_level` parameter, you must restart the instance to apply the change. We recommend that you evaluate the impact on your business and change the parameter settings during off-peak hours. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | Select the region in which the source ApsaraDB RDS for PostgreSQL instance resides. |
|   | RDS Instance ID | Select the ID of the source ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | Enter the name of the source database. |
|   | Database Account | Enter the database account of the source ApsaraDB RDS for PostgreSQL instance. The account must have the read and write permissions on the source database. |
|   | > Document Version: 2023062 |   |

|   | Service | User Guide·Data migratio |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | Enter the password of the database account. |
| Destination Database | Instance Type | Select RDS Inst ance. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | RDS Instance ID | Select the ID of the destination ApsaraDB RDS for PostgreSQL instance. |
|   | Database Name | Enter the name of the destination database. Not e The name of the destination database can be different from the name of the source database. |
|   | Database Account | Enter the database account of the destination ApsaraDB RDS for PostgreSQL instance. The account must have the read and write permissions on the destination database. |
|   | Database Password | Enter the password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the objects to be migrated and the migration types.

| Setting | Description |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Setting | Description |
|---|---|
| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

6. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. You can troubleshoot the issues based on the causes and run a precheck again.
7. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data between PolarDB for Oracle

clusters This topic describes how to migrate data between PolarDB for Oracle clusters by using Data Transmission Service (DTS). Prerequisites The tables to be migrated from the source PolarDB for Oracle cluster contain primary keys or UNIQUE NOT NULL indexes. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The write-ahead logging (WAL) feature is enabled. WAL logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the WAL logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of WAL logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the WAL logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the WAL logs of the source database are cleared during full data migration, DTS cannot obtain the WAL logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. |

|   |   | Category | Description |
|---|---|---|---|
|   |   |   | A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Not e Replace the schema and table variables in the preceding statement with your actual schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source database. _ _ Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination instance after a failed data migration task is resumed. |
|   |   |   | REPLICA IDENTITY FULL; |
|   |   | Other limits |   |

Migration types

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of the objects to be migrated from the source database to the destination PolarDB for Oracle cluster. DTS supports schema migration for the following types of objects: table, view, synonym, stored procedure, stored function, package, and user-defined type. Import ant In this scenario, DTS does not support triggers. If an object contains triggers, data inconsistency may occur between the source and destination databases. |

| Migration type | Description |
|---|---|
| Full data migration | DTS migrates the historical data of the objects to be migrated from the source database to the destination PolarDB for Oracle cluster. Import ant During schema migration and full data migration, do not perform DDL operations on the objects to be migrated. Otherwise, the objects may fail to be migrated. |
| Incremental data migration | DTS retrieves redo log files from the source database. Then, DTS migrates incremental data from the source database to the destination PolarDB for Oracle cluster. DTS can synchronize DML operations, such as INSERT, UPDATE, and DELETE. DTS cannot synchronize DDL operations. Incremental data migration allows you to ensure service continuity when you migrate data between PolarDB for Oracle clusters. |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. You cannot select PolarDB for Oracle cluster as the instance type. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select PolarDB-O. |
|   | DNS or IP Address | The endpoint of the source PolarDB for Oracle cluster. |
|   | Port Number | The service port number of the source PolarDB for Oracle cluster. Default value: 3433. |
|   | Database Name | The name of the source database. |
|   | Database Account | The initial database account of the source PolarDB for Oracle cluster. |
|   | > Document Version: 2023062 |   |

|   | Service | User Guide·Data migratio |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | The password of the database account. |
|   | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
| Destination Database |   |   |
|   | Database Type | The type of the destination database. Select PolarDB-O. |
|   | DNS or IP Address | The endpoint of the destination PolarDB for Oracle cluster. |
|   | Port Number | The service port number of the destination PolarDB for Oracle cluster. Default value: 1433. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The database account of the destination PolarDB for Oracle cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Set t ing | Descript ion |
|---|---|
| Select migratio n types | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |

| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
|---|---|
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

6. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
7. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a PolarDB for Oracle

cluster to a self-managed Oracle database This topic describes how to migrate data from a PolarDB for Oracle cluster to a self-managed Oracle database by using Data Transmission Service (DTS). Prerequisites The destination Oracle database is created. The schema of the Oracle database is the same as the schema of the source database in the PolarDB for Oracle cluster. This is because DTS does not support schema migration from a PolarDB for Oracle cluster to a self-managed Oracle database. Limits

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The write-ahead logging (WAL) feature is enabled. WAL logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the WAL logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of WAL logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the WAL logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the WAL logs of the source database are cleared during full data migration, DTS cannot obtain the WAL logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: During full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

|   |   | Category | Description |
|---|---|---|---|
|   |   |   | If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. Schema migration is not supported. Before you configure a data migration task, you must create databases and tables in the destination instance based on the databases and tables that you want to migrate. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Not e Replace the schema and table variables in the preceding statement with your actual schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source database. _ _ Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|   |   |   | REPLICA IDENTITY FULL; |
|   |   | Other limits |   |

Permissions required for database accounts

| Migration type | Full data migration | Incremental data migration |
|---|---|---|
| PolarDB for Oracle cluster | Read and write permissions | Read and write permissions |
| Self-managed Oracle database | Read and write permissions | Read and write permissions on databases |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. You cannot select PolarDB for Oracle cluster as the access method. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select PolarDB-O. |
|   | DNS or IP Address | The endpoint of the source PolarDB for Oracle cluster. |
|   | Port Number | The service port number of the source PolarDB for Oracle cluster. Default value: 1521. |
|   | Database Name | The name of the source database. |
|   | Database Account | The account of the source database. The account must have the read and write permissions on the source database. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Oracle. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |

|   | migration | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
|   | Oracle Type | The architecture type of the self-managed Oracle database. If you select Non-RAC Inst ance, you must specify the SID parameter. If you select RAC or PDB Inst ance, you must set the Service Name parameter. |
|   | Database Account | The account of the destination database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Select migratio n types | If you want to perform only full data migration, select Full Dat a Migrat ion. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time range for failed connecti ons | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

6. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
7. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a PolarDB for Oracle

cluster to a self-managed Kafka cluster Kafka is a distributed message queue service that supports high throughput and high scalability. Kafka is widely used for big data analytics such as log collection, monitoring data aggregation, streaming processing, and online and offline analysis. Kafka is an essential service for the big data ecosystem. This topic describes how to migrate data from a PolarDB for Oracle cluster to a self-managed Kafka cluster by using Data Transmission Service (DTS). The data synchronization feature allows you to extend message processing capabilities. Prerequisites The tables to be migrated from the source PolarDB for Oracle cluster contain primary keys or UNIQUE NOT NULL indexes. Limits

|   |   | Category | Description |
|---|---|---|---|
|   |   | Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data from a database, you must enable the write-ahead logging (WAL) feature for the database. The source PolarDB for Oracle cluster must be of the latest version. |
|   |   |   | In this scenario, only incremental data migration is supported. Schema migration and full data migration are not supported. A data migration task can migrate data from only one database. To migrate data from multiple databases, you must create a data migration task for each database. During incremental data migration, if you select a schema as the object to be migrated and create a table in the schema or execute the RENAME statement to rename a table in the schema, you must execute the ALTER TABLE schema.table REPLICA IDENTITY FULL; statement before you write data to the table. Not e Replace the schema and table variables in the preceding statement with your actual schema name and table name. To ensure that the latency of incremental data migration is accurate, DTS creates a heartbeat table named dts postgres heartbeat in the source database. _ _ Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
|   |   |   | REPLICA IDENTITY FULL; |
|   |   | Other limits |   |

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. You cannot select PolarDB for Oracle cluster as the source database. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select PolarDB-O. |
|   | DNS or IP Address | The endpoint of the source PolarDB for Oracle cluster. |
|   | Port Number | The service port number of the source PolarDB for Oracle cluster. Default value: 1521. |
|   | Database Name | The name of the source database. |
|   | Database Account | The privileged account of the source PolarDB for Oracle cluster. |
|   | Database Password | The password of the database account. |
|   | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Kaf ka. |
|   | Hostname or IP Address | The endpoint that is used to connect to the self-managed Kafka cluster. In this example, the public IP address of the self-managed Kafka cluster is specified. |
|   | Port Number | The service port number of the self-managed Kafka cluster. Default value: 9092. |
|   | Database Account | The database account of the self-managed Kafka cluster. If no authentication is enabled for the self-managed Kafka cluster, you do not need to specify this parameter. |

|   | gration Data Transmission Servic |   |
|---|---|---|
| Section | Parameter | Description |
| Destination Database | Database Password | The password of the database account. If no authentication is enabled for the self-managed Kafka cluster, you do not need to specify this parameter. |
|   | Topic | Click Get T opic List next to Topic and select a topic from the drop- down list. |
|   | Kafka Version | The version of the self-managed Kafka cluster. Not e You cannot select Kafka 2.0 in the DTS console. If you are using Kafka 2.0, you must select Kafka 1.0. |
|   | Encryption | Specifies whether to encrypt the connection to the destination Kafka cluster. Select Non-encrypt ed or SCRAM-SHA-256 based on your business and security requirements. |
|   | Whether to Use Kafka schema registry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the migration types and the objects to be migrated.

| Parameter or setting | Description |
|---|---|
| Migration Types | Select Increment al Dat a Migrat ion. |
| Select the objects to be migrated | Select one or more tables from the Available section and click the icon to add the tables to the Select ed section. You can select only tables as the objects to be migrated. |

6. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
7. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data between self-managed

Redis databases This topic describes how to migrate data between self-managed Redis databases by using Data Transmission Service (DTS). Prerequisites The version of the source Redis database is 2.8, 3.0, 3.2, 4.0, or 5.0. The source Redis database uses the standalone architecture rather than the cluster architecture. The `PSYNC` or `SYNC` command can be executed on the source Redis database. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you want to migrate incremental data, make sure that the following requirements are met: The write-ahead logging (WAL) feature is enabled. Data logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during full data migration, DTS cannot obtain the data logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If the data eviction policy maxmemory-policy of the destination database is not set to noeviction , data inconsistency may occur between the source and destination databases. If you run the EVAL or EVALSHA command to call Lua scripts, DTS cannot identify whether these Lua scripts are executed in the destination database. This is because the destination database does not explicitly return the execution results of Lua scripts during incremental data migration. When you run the PSYNC or SYNC command to transfer data of the LIST type, DTS does not perform the FLUSH operation on the existing data in the destination database. As a result, the destination database may contain duplicate data records. If an expiration policy is enabled for specific keys in the source database, these keys may not be deleted at the earliest opportunity after they expire. Therefore, the number of keys in the destination database may be less than that in the source database. You can run the INFO command to view the number of keys in the destination database. Not e The number of keys that do not have the expiration policy enabled or have not expired is the same between the source and destination databases. To ensure compatibility, the version of the destination Redis database must be the same as or later than the version of the source Redis database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
| Special cases | If you perform a primary/secondary switchover on the source or destination self-managed Redis database when the data migration task is running, the task fails. |

Migration types Full data migration: DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration: After full data migration is complete, DTS migrates incremental data from the source database to the destination database in real time. Commands that can be incrementally migrated APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT FLUSHALL and FLUSHDB GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, PSETEX, and PUBLISH RENAME, RENAMENX, RESTORE, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE Before you begin To ensure that incremental data migration tasks run as expected, we recommend that you remove the limit on the replication output buffer for the source database. In this topic, a server that runs on Linux is used in the example. If you perform only full data migration, skip the following steps.
1. Use the redis-cli program to connect to the source database.
You can use the redis-cli program after you install the Redis client. For more information, see Redis community official website.

```
redis-cli -h <host> -p <port> -a <password>
```

<host>: the endpoint that is used to connect to the source database. You can use 127.0.0.1 in this example. <port>: the service port number of the source database. The default port number is 6379. <password>: the password of the source database. Example:

```
redis-cli -h 127.0.0.1 -p 6379 -a Test123456
```

2. Run the following command to remove the limit on the replication output buffer:

```
config set client-output-buffer-limit 'slave 0 0 0'
```

Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure a task name.
DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name.
4. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The access method of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the access method of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select Redis. |
|   | Instance Mode | The architecture of the source database. The value of this parameter is fixed to St andalone and cannot be changed to Cluster. |
|   | Hostname or IP Address | The endpoint that is used to connect to the source database. |
|   | Port Number | The service port number of the source database. Default value: 6379. |
|   | Database Password | Enter the password of the source database. If password verification is disabled for the source database, you do not need to enter the password. |
| Destination Database | Instance Type | The access method of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select Redis. |
|   | Hostname or IP Address | The endpoint that is used to connect to the destination database. |

|   | migration | Data Transmission Servic |
|---|---|---|
|   | Parameter | Description |
| Section |   |   |
|   | Port Number | The service port number of the destination database. Default value: 6379. |
|   | Database Password | The password of the destination database. If password verification is disabled for the destination database, you do not need to enter the password. |

5. In the lower-right corner of the page, click Set Whit elist and Next .
6. If an IP address whitelist is configured for the self-managed Redis database, you must manually add
the CIDR blocks of DTS servers to the IP address whitelist of the database. To obtain the CIDR blocks of DTS servers, click Copy in the dialog box that appears. After you add the CIDR blocks of DTS servers to the IP address whitelist of the database, click Next . If you do not need to configure an IP address whitelist for the self-managed Redis database, ignore the preceding settings and click Next .
7. Select the objects to be migrated and the migration types.

| Paramet er or setting | Description |
|---|---|
| Migration Types | To perform only full data migration, select Full Dat a Migrat ion. To ensure service continuity during data migration, select Full Dat a Migrat ion and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time range for failed connecti ons | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

8. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data between self-managed

MongoDB databases This topic describes how to migrate data between self-managed MongoDB databases by using Data Transmission Service (DTS). Prerequisites The version of the source MongoDB database is 3.0, 3.2, 3.4, 3.6, 4.0, or 4.2. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you need to migrate incremental data, make sure that the following requirements are met: The operation logging feature is enabled. Operation logs are retained for at least seven days during full data migration. You can wait until full data migration is complete, and then clear the operation logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of operation logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the operation logs of the source database during full data migration, the data migration task may fail. For example, full data migration takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the operation logs of the source database are cleared during full data migration, DTS cannot obtain the operation logs generated 24 hours ago. Therefore, the data migration task may fail. Limits on operations to be performed on the source database: If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select full data migration and incremental data migration as the migration types. |

| Category | Description |
|---|---|
| Other limits | If you need to migrate incremental data from a standalone MongoDB database, you must enable the operation logging feature. A standalone MongoDB database contains only a primary node. For more information, see the Preparation for a standalone MongoDB database section of this topic. If the source database uses the sharded cluster architecture, you must configure a data migration task for each shard. To ensure compatibility, the version of the destination MongoDB database must be the same as or later than the version of the source MongoDB database. The admin or local database is not used as the source or destination database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination cluster. After full data migration is complete, the size of used tablespace of the destination cluster is larger than that of the source instance. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after the failed task is resumed. |
| Special cases | If both the source database and destination database are self-managed MongoDB databases, take note of the following items: If you perform a primary/secondary switchover on the source database when the data migration task is running, the task fails. DTS calculates migration latency based on the timestamp of the latest migrated data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the migration latency may be inaccurate. If the latency of the data migration task is excessively high, you can perform a DML operation on the source database to update the latency. Not e If you select an entire database as the object to be migrated, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

Migration types

| Migration type | Description |
|---|---|

| Migration type | Description |
|---|---|
| Full data migration | DTS migrates the historical data of objects from the source database to the destination database. Not e DTS can migrate the following types of objects: database, collection, and index. |
| Incremental data migration | After full data migration is complete, DTS migrates incremental data from the source database to the destination database in real time. Not e DTS can migrate the create and delete operations that are performed on databases, collections, and indexes. DTS can migrate the create, delete, and update operations that are performed on documents. |

Preparation for a standalone MongoDB database If you need to migrate incremental data from a standalone MongoDB database, you must enable the operation logging feature. A standalone MongoDB database contains only a primary node. If you do not need to perform incremental data migration, skip the following steps. When you enable the operation logging feature, the MongoDB service is restarted. We recommend that you perform this operation during off-peak hours.
1. Use Mongo Shell to connect to the source database.
2. Run the following commands to shut down the MongoDB service:

```
use admin db.shutdownServer()
```

3. Run the following command to start the MongoDB service from the backend as a replica set:

```
mongod --port 27017 --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --rep lSet rs0 --bind_ip 0.0.0.0 --auth --fork
```

The database path used by the preceding command is /var/lib/mongodb. The log file path is /var/log/mongodb/mongod.log. You must specify the paths based on your business requirements. The command uses `0.0.0.0` as the associated IP address of the MongoDB service. This allows you to access the database by using a random IP address. After the migration is complete, run the `kill` command to end the process, and start the MongoDB service by using the original configuration file. The command enables authentication. You can access the database only after you pass the authentication.
4. Use Mongo Shell to connect to the source database again.
5. Run the following commands to initialize the replica set:

```
use admin rs.initiate()
```

6. Wait until the role of the current node changes to primary. This indicates that the operation logging
feature is enabled. You can run the `rs.printReplicationInfo()` command to view the status of the operation logging feature. Procedure
1. Purchase a DTS instance. For more information, see Create a data migration instance.
2. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source | Instance Type | The instance type of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. If you select User- Creat ed Dat abase wit h Public IP Address as the instance type of the source database, you do not need to specify the Inst ance Region parameter. |
|   | Database Type | The type of the source database. Select MongoDB. |
|   | Hostname or IP Address | The IP address that is used to access the source database. |

|   | migration | Data Transmission Servic |
|---|---|---|
| Database Section | Parameter | Description |
|   | Port Number | The service port number of the source database. |
|   | Database Name | The name of the authentication database. The database account is created in this database. |
|   | Database Account | The account of the source database. The account must have the read permissions on the source database, admin database, and local database. |
|   | Database Password | The password of the database account. |
| Destinatio n Database | Instance Type | The instance type of the destination database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The destination region that you selected on the buy page. You cannot change the value of this parameter. |
|   | Database Type | The type of the destination database. Select MongoDB. |
|   | Hostname or IP Address | The endpoint that is used to access the destination database. |
|   | Port Number | The service port number of the destination database. |
|   | Database Name | The name of the authentication database. The database account is created in this database. Not e If you want to use the root account, enter admin in the Database Name field. |
|   | Database Account | The account of the destination database. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If the whitelists are configured for your self-managed MongoDB databases, you must manually add
the CIDR blocks of DTS servers to the whitelists of the databases. In the dialog box that appears, click Copy t o Clipboard to obtain the CIDR blocks of DTS servers. After you add the CIDR blocks of DTS servers to the whitelist of the database, click Next . If you do not need to configure a whitelist for the MongoDB database, ignore the preceding settings and click Next .
6. Select the objects to be migrated and the migration types.

| Paramet er | Description |
|---|---|
| Migration type | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. If you want to ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, do not write data to the source database during full data migration. This ensures data consistency between the source and destination databases. |
| Select the objects to be migrated | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

7. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. After the task passes the precheck, click Next .
If Incremental Data Migration is not selected, wait until the migration task is completed. If Incremental Data Migration is selected, the migration task does not automatically stop. In this case, you must wait until T he migrat ion t ask is not delayed appears and manually stop the task.

#### Migrate data from a MaxCompute project

to a MySQL database This topic describes how to migrate data from a MaxCompute project to a MySQL database by using Data Transmission Service (DTS). In this example, an ApsaraDB RDS for MySQL instance is used as the destination instance. Usage notes DTS uses read and write resources of the source and destination databases during full data migration. This may increase the loads of the database servers. If the database performance is unfavorable, the specification is low, or the data volume is large, database services may become unavailable. For example, DTS occupies a large amount of read and write resources in the following cases: a large number of slow SQL queries are performed on the source database, the tables have no primary keys, or a deadlock occurs in the destination database. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. For example, you can migrate data when the CPU utilization of the source and destination databases is less than 30%. DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must manually create a database in the destination instance before you configure the data migration task. For more information about ApsaraDB RDS for MySQL instances and how to create a database in an ApsaraDB RDS for MySQL instance, see the "Create a database" topic in the documentation of ApsaraDB RDS for MySQL. To ensure data consistency, we recommend that you do not write data to the source MaxCompute project during full data migration. If a data migration task fails, DTS automatically resumes the task. Before you switch your workloads to the destination instance, stop or release the data migration task. Otherwise, the data in the source database overwrites the data in the destination instance after the task is resumed. MaxCompute does not support the PRIMARY KEY constraint. If network errors occur, DTS retries the data migration task. In this case, duplicate data records may be migrated to the destination tables that do not have primary keys. DTS cannot migrate incremental data from a MaxCompute project to an ApsaraDB RDS for MySQL instance. To ensure data consistency, we recommend that you do not write data to the source MaxCompute project during data migration. Supported destination database types You can use DTS to migrate data to the following types of MySQL databases: Self-managed database hosted on Elastic Compute Service (ECS) Self-managed database connected over Express Connect, VPN Gateway, or Smart Access Gateway Self-managed database connected over Database Gateway In this topic, an ApsaraDB RDS f or MySQL inst ance is used to describe how to configure a data migration task. You can also follow the procedure to configure data migration tasks for other types of MySQL databases. Migration types

| Migration type | Description |
|---|---|
| Schema migration | DTS migrates the schemas of the required objects to the destination database. DTS supports schema migration for views, tables, and databases. Warning In this topic, the source and destination databases are heterogeneous databases. DTS does not ensure that the schemas of the source and destination databases are consistent after schema migration. We recommend that you evaluate the impact of data type conversion on your business. For more information, see Data type mappings between heterogeneous databases. |
| Full data migration | DTS migrates full data of the required objects to the destination database. Not e During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the used tablespace of the destination database is larger than that of the source database. |

Procedure
1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. In the upper-left corner of the Data Migration page, click Creat e Migrat ion T ask.
4. In the panel that appears, select the source and destination regions, and specify the number of data
migration instances that you want to create. In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.
5. Click Creat e.
6. Find the data migration instance that you created, and click Conf igure Migrat ion T ask in the
Actions column.
7. Configure a task name.
DTS automatically generates a task name. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name.
8. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| Source Database | Instance Type | The instance type of the source database. Select MaxComput e. |
|   | Instance Region | The region in which the source MaxCompute project resides. |
|   | Project | The name of the MaxCompute project. You can view the name of the MaxCompute project on the Project s page in the MaxCompute console. |
| Destination Database | Instance Type | The instance type of the destination database. Select RDS Inst ance. |
|   | Instance Region | The region in which the destination ApsaraDB RDS for MySQL instance resides. |
|   | RDS Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. The account must have read and write permissions on the destination database. |
|   | Database Password | The password of the database account. After you specify the destination database parameters, click T est Connect ivit y next to Dat abase Password to verify whether the specified parameters are valid. |

9. In the lower-right corner of the page, click Set Whit elist and Next .
0. In the lower-right corner of the page, click Next . In this step, the permissions on the MaxCompute
project are granted to the migration account.
1. Select the migration types and the objects to be migrated.

| Setting | Description |
|---|---|
| Select migratio n types | Select Schema Migrat ion and Full Dat a Migrat ion. Not e DTS cannot migrate incremental data from a MaxCompute project to an ApsaraDB RDS for MySQL instance. |

| Setting | Description |
|---|---|
| Select the objects to be migrated | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. By default, after an object is migrated to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are migrated to the destination database. For more information, see Object name mapping. If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Specify the retry time range for a failed connecti on to the source or destinati on databas e | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. |

2. In the lower-right corner of the page, click Precheck.
Import ant Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
3. After the task passes the precheck, click Next .

#### Migrate data from a PolarDB-X 2.0

instance

##### Migrate data between PolarDB-X 2.0 instances

This topic describes how to migrate data between PolarDB-X 2.0 instances by using Data Transmission Service (DTS). Prerequisites The source and destination PolarDB-X 2.0 instances are created and compatible with MySQL 5.7. The available storage space of the destination PolarDB-X 2.0 instance is larger than the total size of the data in the source PolarDB-X 2.0 instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of the PolarDB-X 2.0 instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |

| Category | Description |
|---|---|
| Other limits | The destination PolarDB-X 2.0 instance must be compatible with MySQL 5.7. Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
| Precautions | DTS updates the `dts healthcheck`.`hahealthcheck` table in the source database as _ _ _ _ scheduled to move forward the binary log file position. |

Migration types Schema migration DTS migrates the schemas of objects from the source database to the destination database. Full data migration DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting services of self-managed applications during data migration. Permissions required for database accounts

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| Source PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |
| Destination PolarDB-X 2.0 instance | Read and write permissions |   |   |

SQL operations that can be migrated during incremental data migration

| Operat ion t ype | SQL st at ement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

Create a data migration task
1. Log on to the Data Management (DMS) console.
For more information, see the Log on to the DMS console topic of DMS User Guide.
2. In the top navigation bar, click DT S.
3. In the left-side navigation pane, click Dat a Migrat ion to go to the Dat a Migrat ion T asks page.
The layout and style of the DMS console vary. You may need to click Dat a Migrat ion in the top navigation bar.
4. On the Data Migration Tasks page, click Creat e T ask.
5. In the dialog box that appears, set the Source Dat abase T ype, Dest inat ion Dat abase T ype, and
Quant it y parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select PolarDB-X 2.0. |
| Quant it y | The number of data migration instances that you want to create. |

6. Click Purchase Inst ance.
Configure a data migration task
1. On the Dat a Migrat ion T asks page, find the data migration task that you create and click
Conf igure T ask in the Actions column.
2. Configure the source and destination databases. Set the parameters described in the following
table.

| Section | Parameter | Description |
|---|---|---|
|   | Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Met hod | The access method of the source database. The value is fixed to Alibaba Cloud Inst ance. |

| r Guide·Data migration |   | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
| Source Database | Inst ance Region | The region in which the source PolarDB-X 2.0 instance resides. |
|   | Inst ance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the source PolarDB-X 2.0 instance. For information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase password | The password of the database account. |
| Destination Database | Dat abase T ype | The type of the destination database. Select PolarDB-X 2.0. |
|   | Access Met hod | The access method of the destination database. The value is fixed to Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the destination PolarDB- X 2.0 instance resides. |
|   | Inst ance ID | The ID of the destination PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the destination PolarDB-X 2.0 instance. For information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase password | The password of the database account. |

3. In the lower part of the page, click T est Connect ivit y and Proceed.
If the source or destination database is an Alibaba Cloud instance, such as an ApsaraDB RDS for MySQL or ApsaraDB for MongoDB instance, DTS automatically adds the CIDR blocks of DTS servers to the IP address whitelist of the instance. If the source or destination database is a self-managed database hosted on an Elastic Compute Service (ECS) instance, DTS automatically adds the CIDR blocks of DTS servers to the security group rules of the ECS instance. If the source or destination database is a self-managed database that is deployed in a data center or provided by a third-party cloud service provider, you must manually add the CIDR blocks of DTS servers to the IP address whitelist of the database to allow DTS to access the database. Warning If the CIDR blocks of DTS servers are automatically or manually added to the IP address whitelist of the database or instance, or to the ECS security group rules, security risks may arise. Therefore, before you use DTS to migrate data, you must understand and acknowledge the potential risks and take preventive measures, including but not limited to the following measures: enhance the security of your username and password, limit the ports that are exposed, authenticate API calls, regularly check the whitelist or ECS security group rules and forbid unauthorized CIDR blocks, or connect the database to DTS by using Express Connect, VPN Gateway, or Smart Access Gateway.
4. Configure the parameters described in the following table.
Basic Settings

| Parameter or setting | Description |
|---|---|
| T ask St ages | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Incremental Data Migration is not selected, we recommend that you do not write data to the source instance during data migration. This ensures data consistency between the source and destination instances. |

| Parameter or setting | Description |
|---|---|
| Processing Mode in Exist ed T arget T able | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Not e You can use the object name mapping feature to rename the tables that are migrated to the destination database. You can use this feature if the source and destination databases contain identical table names and the tables in the destination database cannot be deleted or renamed. For more information, see Object name mapping. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |
| Select t he object s t o be migrat ed | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. |

Advanced Settings

| Paramet er or setting | Description |
|---|---|

| Paramet er or setting | Description |
|---|---|
| Ret ry T ime f or Failed Connec t ion | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click View Det ails next to each failed item. After you troubleshoot the issues based on the causes, you can run a precheck again.
6. After the success rat e becomes 100%, the data migration task starts to run.
You can view the progress of the task on the Data Migration page.

##### Migrate data from a PolarDB-X 2.0 instance to a

MySQL instance This topic describes how to migrate data from a PolarDB-X 2.0 instance to a MySQL instance by using Data Transmission Service (DTS). In this topic, an ApsaraDB RDS for MySQL instance is used as an example. Prerequisites The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The available storage space of the destination ApsaraDB RDS for MySQL instance is larger than the total size of data in the source PolarDB-X 2.0 instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed decreases. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you want to edit the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches, or configure a task to migrate the entire database. If you want to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during the precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform both full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you change the network type of a PolarDB-X 2.0 instance during data migration, contact technical support to change the network connection settings of the data migration instance. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select schema migration, full data migration, and incremental data migration as the migration types. The PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |

| Category | Description |
|---|---|
| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
| Special cases | If the destination database runs on an ApsaraDB RDS for MySQL instance, take note of the following limits: DTS automatically creates a database in the destination ApsaraDB RDS for MySQL instance. However, if the name of the source database is invalid, you must create a database in the destination ApsaraDB RDS for MySQL instance before you configure the data migration task. For more information, see Creat e dat abases and account s f or an ApsaraDB RDS f or MySQL inst ance in the user guide of ApsaraDB RDS for MySQL. |

Migration types Schema migration DTS migrates the schemas of objects from the source database to the destination database. Full data migration DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting services of self-managed applications during data migration. SQL operations that can be migrated during incremental data migration

| Operat ion t ype | SQL st at ement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE Not e RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object and rename the table during data migration, the data of this table is not migrated to the destination database. To prevent this situation, you can select the database to which this table belongs as the object when you configure the data migration task. TRUNCATE TABLE |
|---|---|

Permissions required for database accounts

| Instance type | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| PolarDB-X 2.0 | SELECT permission | SELECT permission | The SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |
| ApsaraDB RDS for MySQL | Read and write permissions |   |   |

Step 1: Create a data migration task
1. Log on to the Data Management (DMS) console.
For more information, see the Log on t o t he DMS console topic of DMS User Guide.
2. In the top navigation bar, click DT S.
3. In the left-side navigation pane, click Dat a Migrat ion to go to the Dat a Migrat ion T asks page.
The layout and style of the DMS console vary. You may need to click Dat a Migrat ion in the top navigation bar.
4. On the Dat a Migrat ion page, click Creat e T ask.
5. In the panel that appears, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | Select PolarDB-X 2.0. |

| a Transmission Service | User Guide·Data migratio |
|---|---|

| Parameter | Description |
|---|---|
| Source Region | Select the region in which the source instance resides. |
| Dest inat ion Dat abase T ype | Select MySQL. |
| Dest inat ion Region | Select the region in which the destination instance resides. |
| Quant it y | Specify the number of data migration instances that you want to create at a time. Default value: 0. |

6. Click Purchase Inst ance.
Step 2: Configure the data migration task
1. In the data migration tasks list, find the data migration task that you created and click Conf igure
T ask in the rightmost column.
2. Configure the source and destination databases. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | T ask Name | The name of the task. DTS automatically generates a task name. We recommend that you specify a descriptive name for easy identification. You do not need to specify a unique task name. |
| Source Dat abase | Dat abase T ype | The type of the source instance. Select PolarDB-X 2.0. |
|   | Access Met hod | The value of this parameter is fixed to Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the source database resides. The region is the source region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Inst ance ID | The ID of the source instance. |
|   | Dat abase Account | The database account of the source instance. For information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase Password | The password of the database account. |
|   | Dat abase T ype | The type of the destination instance. Select MySQL. |
|   | Access Met hod | The value of this parameter is fixed to Public IP Address. |

| r Guide·Data |   |   |
|---|---|---|
|   | migration Data Transmission Servic |   |
| Section | Parameter | Description |
| Dest inat i on Dat abase | Inst ance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data migration instance. You cannot change the value of this parameter. |
|   | Host name or IP Address | The endpoint of the destination instance. |
|   | Port Number | The port number of the destination instance. Default value: 3306. |
|   | Dat abase Account | The database account of the destination instance. For information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase Password | The password of the database account. |

3. In the lower part of the page, click T est Connect ivit y and Proceed.
If the source or destination database is in an instance hosted on Apsara Stack, such as an or ApsaraDB RDS for MySQL instance, DTS automatically adds the CIDR blocks of DTS servers to the IP address whitelist of the instance. If the source or destination database is a self-managed database hosted on an Elastic Compute Service (ECS) instance, DTS automatically adds the CIDR blocks of DTS servers to the security group rules of the ECS instance. If the source or destination database is a selfmanaged database that is deployed in a data center or provided by a third-party cloud service provider, you must manually add the CIDR blocks of DTS servers to the IP address whitelist of the database to allow DTS to access the database.ApsaraDB for MongoDB Warning If the CIDR blocks of DTS servers are automatically or manually added to the IP address whitelist of the database or instance, or to the ECS security group rules, security risks may arise. Therefore, before you use DTS to migrate data, you must understand and acknowledge the potential risks and take preventive measures, including but not limited to the following measures: enhance the security of your username and password, limit the ports that are exposed, authenticate API calls, regularly check the whitelist or ECS security group rules and forbid unauthorized CIDR blocks, or connect the database to DTS by using Express Connect, VPN Gateway, or Smart Access Gateway.
4. Select the objects to be migrated and configure advanced settings.
Basic settings

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| T ask St ages | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source instance during data migration. This ensures data consistency between the source and destination instances. |

| Parameter | Description |
|---|---|
| Processing Mode of Conf lict ing T ables | Precheck and Report Errors: checks whether the destination database contains tables that use the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Not e If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Parameter | Description |
|---|---|
| Select Object s | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be migrated. If you select tables or columns as the objects to be migrated, DTS does not migrate other objects such as views, triggers, or stored procedures to the destination database. |

Advanced settings

| Setting | Description |
|---|---|
| Ret ry T ime f or Failed Connect ions | Specify the retry time range for failed connections. Valid values: 10 to 720. Unit: minutes. Default value: 720. We recommend that you set the retry time range to more than 30 minutes. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e If an instance serves as the source or destination database of multiple data migration tasks, the value that is set later takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click View Det ails next to each failed item. After you troubleshoot the issues based on the causes, you can run a precheck again.
6. After the value of Success Rat e becomes 100%, the data migration task starts to run.
You can view the progress of the task on the Data Migration page.

##### Migrate data from a PolarDB-X 2.0 instance to a

Message Queue for Apache Kafka instance This topic describes how to migrate data from a PolarDB-X 2.0 instance to a Message Queue for Apache Kafka instance by using Data Transmission Service (DTS). Message Queue for Apache Kafka provides extended capabilities to process messages. Prerequisites A PolarDB-X 2.0 instance is created. In the destination Message Queue for Apache Kafka instance, a topic is created to receive the migrated data. The available storage space of the destination Message Queue for Apache Kafka instance is larger than the total size of data in the source PolarDB-X 2.0 instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of the PolarDB-X 2.0 instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |

| Category | Description |
|---|---|
| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |
| Precautions | DTS updates the `dts healthcheck`.`hahealthcheck` table in the source database as _ _ _ _ scheduled to move forward the binary log file position. |

Migration types Schema migration DTS migrates the schemas of objects from the source database to the destination database. Full data migration DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting services of self-managed applications during data migration. Permissions required for database accounts

| Database | Schema migration | Full data migration | Incremental data migration |
|---|---|---|---|
| PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be migrated, REPLICATION SLAVE permission, and REPLICATION CLIENT permission. DTS automatically grants these permissions to the database account. |

SQL operations that can be incrementally migrated

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

Step 1: Create a data migration task
1. Log on to the Data Management (DMS) console.
For more information, see the Log on t o t he DMS console topic of DMS User Guide.
2. In the top navigation bar, click DT S.
3. In the left-side navigation pane, click Dat a Migrat ion to go to the Dat a Migrat ion T asks page.
The layout and style of the DMS console vary. You may need to click Dat a Migrat ion in the top navigation bar.
4. On the Dat a Migrat ion page, click Creat e T ask.
5. In the panel that appears, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
| Source Region | The region in which the source database resides. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select Kaf ka. |
| Dest inat ion Region | The region in which the destination database resides. |
| Quant it y | The number of data migration instances that you want to create at a time. Default value: 0. |

6. Click Purchase Inst ance.
Step 2: Configure the data migration task
1. In the dat a migrat ion t asks list, find the data migration task that you created and click Conf igure
T ask in the rightmost column.
2. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | T ask Name | The name of the task. DTS automatically generates a task name. We recommend that you specify a descriptive name for easy identification. You do not need to specify a unique task name. |
|   | Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |

| r Guide·Data |   |   |
|---|---|---|
|   | migration Data Transmission Servic |   |
| Section | Parameter | Description |
| Source Dat abase | Access Met hod | The access method of the source database. Select Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the source PolarDB-X 2.0 instance resides. |
|   | Inst ance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the source PolarDB-X 2.0 instance. For more information about the permissions that are required for the account, see the Permissions required for database accounts section of this topic. |
|   | Dat abase Password | The password of the database account. |
| Dest inat i on | Dat abase T ype | The type of the destination database. Select Kaf ka. |
|   | Access Met hod | The access method of the destination database. The value of this parameter is fixed to Public IP Address. Not e If you select Public IP Address, you can use a specific IP address to connect to the destination Message Queue for Apache Kafka instance over the classic network. |
|   | Inst ance Region | The region in which the destination Message Queue for Apache Kafka instance resides. |
|   | Host name or IP address | The endpoint of the destination Message Queue for Apache Kafka instance. Not e To obtain an IP address of the Message Queue for Apache Kafka instance, perform the following operations: Log on to the Message Queue for Apache Kafka console and go to the Instance Details page of the Message Queue for Apache Kafka instance. In the Endpoint Inf ormat ion section of the Inst ance Inf ormat ion tab, obtain an IP address from the Default Endpoint parameter. |
|   | Port Number | The service port number of the destination Message Queue for Apache Kafka instance. Default value: 9092. |

| Dat abase Section | Parameter | Description |
|---|---|---|
|   | Dat abase Account | The database account of the destination Message Queue for Apache Kafka instance. Not e If the Message Queue for Apache Kafka instance is a VPC-connect ed instance, you do not need to configure the Dat abase Account or Dat abase Password parameter. |
|   | Dat abase Password | The password of the database account. |
|   | Kaf ka Version | The version of the destination Message Queue for Apache Kafka instance. |
|   | Encrypt ion | Specifies whether to encrypt the connection. Select Non-encrypt ed or SCRAM-SHA-256 based on your business and security requirements. |
|   | T opic | The topic that is used to receive the migrated data. Select a topic from the drop-down list. |
|   | T opic f or st oring DDL | The topic that is used to store the DDL information. Select a topic from the drop-down list. If you do not specify this parameter, the DDL information is stored in the topic that is specified by the T opic parameter. |
|   | Whet her t o use Kaf ka schema regist ry | Specifies whether to use Kafka Schema Registry. Kafka Schema Registry provides a serving layer for your metadata. It provides a RESTful API to store and retrieve your Avro schemas. Valid values: No: does not use Kafka Schema Registry. Yes: uses Kafka Schema Registry. In this case, you must enter the URL or IP address that is registered in Kafka Schema Registry for your Avro schemas. |

3. In the lower part of the page, click T est Connect ivit y and Proceed.
If the source or destination database is in an instance hosted on Apsara Stack, such as an ApsaraDB RDS for MySQL or ApsaraDB for MongoDB instance, DTS automatically adds the CIDR blocks of DTS servers to the IP address whitelist of the instance. If the source or destination database is a selfmanaged database hosted on an Elastic Compute Service (ECS) instance, DTS automatically adds the CIDR blocks of DTS servers to the security group rules of the ECS instance. If the source or destination database is a self-managed database that is deployed in a data center or provided by a third-party cloud service provider, you must manually add the CIDR blocks of DTS servers to the IP address whitelist of the database to allow DTS to access the database. Warning If the CIDR blocks of DTS servers are automatically or manually added to the IP address whitelist of the database or instance, or to the ECS security group rules, security risks may arise. Therefore, before you use DTS to migrate data, you must understand and acknowledge the potential risks and take preventive measures, including but not limited to the following measures: enhance the security of your username and password, limit the ports that are exposed, authenticate API calls, regularly check the whitelist or ECS security group rules and forbid unauthorized CIDR blocks, or connect the database to DTS by using Express Connect, VPN Gateway, or Smart Access Gateway.
4. Select the objects to be migrated and configure advanced settings.
Basic Settings

| Parameter | Description |
|---|---|
| T ask St ages | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Increment al Dat a Migrat ion is not selected, we recommend that you do not write data to the source instance during data migration. This ensures data consistency between the source and destination instances. |
| Processing Mode of Conf lict ing T ables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Not e If the source and destination databases contain tables that have the same names and the tables in the destination database cannot be deleted or renamed, you can use the object name mapping feature to rename the tables that are migrated to the destination database. For more information, see Object name mapping. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Parameter | Description |
|---|---|
| Dat a Format in Kaf ka | The format in which data is stored in the Message Queue for Apache Kafka instance. If you select DT S Avro, data is parsed based on the schema definition of DTS Avro. For more information, visit GitHub. If you select Canal Json, data is parsed into the Canal JSON format. For more information about the parameters that are used to parse data into the Canal JSON format, see the Parameters used to parse data into the Canal JSON format section of this topic. |
| Policy f or Shipping Dat a t o Kaf ka Part it ions | The policy based on which data is migrated to the Message Queue for Apache Kafka instance. |
| Select Object s | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. |
| Rename Databases and Tables | You can use the object name mapping feature to rename the objects that are migrated to the destination instance. For more information, see Object name mapping. Not e If you use the object name mapping feature to rename an object, other objects that are dependent on the object may fail to be migrated. |
| Filter data | Specify WHERE conditions to filter data. For more information, see Specify an SQL condition to filter data. |
| Select the SQL operations to be incrementally migrated | In the Select ed Object s section, right-click an object. In the dialog box that appears, select the DML operations to be incrementally migrated. |

Parameters used to parse data into the Canal JSON format

| Parameter | Description |
|---|---|
| database | The name of the database. |
| es | The time when the operation is performed on the database. The value is a 13-bit UNIX timestamp. Unit: milliseconds. Not e You can use a search engine to obtain a UNIX timestamp converter. |

| Parameter | Description |
|---|---|
| id | The serial number of the operation. |
| isDdl | Indicates whether the operation is a DDL operation. Valid values: true: The operation is a DDL operation. false: The operation is not a DDL operation. |
| mysqlType | The data type of the field. |
| old | The data before update. |
| pkNames | The name of the primary key. |
| sql | The SQL statement that is executed in the query. |
| sqlType | The data type of the field after conversion. For example, the type LONG is converted from UNSIGNED INTEGER and BIGDECIMAL from UNSIGNED LONG. |
| table | The name of the table in the database. |
| ts | The time when the data is written to the destination database. The value is in the 13-bit UNIX timestamp format. Unit: milliseconds. Not e You can use a search engine to obtain a UNIX timestamp converter. |
| type | The operation type. Valid values: DELETE, UPDATE, and INSERT. |

Advanced Settings

| Parameter | Description |
|---|---|
| Ret ry T ime f or Failed Connect ions | Specify the retry time range for failed connections. Valid values: 10 to 720. Unit: minutes. Default value: 720. We recommend that you set the retry time range to more than 30 minutes. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If an instance serves as the source or destination database of multiple data migration tasks, the value that is set later takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, you can click the det ails icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
6. Wait until the Success Rat e becomes 100%. Then, the data migration task starts.

##### Migrate data from a PolarDB-X 2.0 instance to

an AnalyticDB for PostgreSQL instance This topic describes how to migrate data from a PolarDB-X 2.0 instance to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). Prerequisites The source PolarDB-X 2.0 instance is created and compatible with MySQL 5.7. The destination AnalyticDB for PostgreSQL instance is created. For more information, see Create an AnalyticDB for PostgreSQL instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | Bandwidth requirements: The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the data migration speed is affected. The tables to be migrated must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be migrated and you need to modify the tables in the destination database, such as renaming tables or columns, you can migrate up to 1,000 tables in a single data migration task. If you run a task to migrate more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to migrate the tables in batches or configure a task to migrate the entire database. If you need to migrate incremental data, make sure that the following requirements are met: The binary logging feature is enabled. The value of the binlog row image _ _ parameter is set to full. Otherwise, error messages are returned during precheck and the data migration task cannot be started. If you perform only incremental data migration, the binary logs of the source database must be stored for more than 24 hours. If you perform full data migration and incremental data migration, the binary logs of the source database must be stored for at least seven days. Otherwise, Data Transmission Service (DTS) may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After full data migration is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Limits on operations to be performed on the source database: During schema migration and full data migration, do not perform DDL operations to change the schemas of databases or tables. Otherwise, the data migration task fails. If you want to change the network type of the PolarDB-X 2.0 instance during data migration, you must also modify the network connection settings of the data migration task. If you perform only full data migration, do not write data to the source database during data migration. Otherwise, data inconsistency may occur between the source and destination databases. To ensure data consistency, we recommend that you select Schema Migration, Full Data Migration, and Incremental Data Migration as the migration types. The PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |

| Category | Description |
|---|---|
| Other limits | Before you migrate data, evaluate the impact of data migration on the performance of the source and destination databases. We recommend that you migrate data during off-peak hours. During full data migration, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During full data migration, concurrent INSERT operations cause fragmentation in the tables of the destination database. After full data migration is complete, the size of used tablespace of the destination database is larger than that of the source database. DTS attempts to resume data migration tasks that failed within the last seven days. Before you switch workloads to the destination database, you must stop or release the failed tasks. You can also execute the REVOKE statement to revoke the write permissions from the accounts that are used by DTS to access the destination database. Otherwise, the data in the source database overwrites the data in the destination database after a failed task is resumed. |

Migration types Schema migration DTS migrates the schemas of objects from the source database to the destination database. Full data migration DTS migrates the existing data of objects from the source database to the destination database. Incremental data migration After full data migration is complete, DTS migrates incremental data from the source database to the destination database. Incremental data migration allows data to be migrated smoothly without interrupting services of self-managed applications during data migration. SQL operations that can be migrated during incremental data migration

| Operat ion t ype | SQL st at ement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

Create a data migration task
1. Log on to the Data Management (DMS) console.
For more information, see the Log on t o t he DMS console topic of DMS User Guide.
2. In the top navigation bar, click DT S.
3. In the left-side navigation pane, click Dat a Migrat ion to go to the Dat a Migrat ion T asks page.
The layout and style of the DMS console vary. You may need to click Dat a Migrat ion in the top navigation bar.
4. On the Data Migration Tasks page, click Creat e T ask.
5. In the dialog box that appears, set the Source Dat abase T ype, Dest inat ion Dat abase T ype, and
Quant it y parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select Analyt icDB f or Post greSQL. |
| Quant it y | The number of data migration instances that you want to create. |

6. Click Purchase Inst ance.
Configure a data migration task
1. On the Dat a Migrat ion T asks page, find the data migration task that you create and click
Conf igure T ask in the Actions column.
2. Configure the source and destination databases. Set the parameters described in the following
table.

| Section | Parameter | Description |
|---|---|---|
| Source Database | Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Met hod | The access method of the source database. The value is fixed to Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the source PolarDB-X 2.0 instance resides. |
|   | Inst ance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the source PolarDB-X 2.0 instance. For more information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase password | The password of the database account. |
|   | Dat abase T ype | The type of the destination database. Select Analyt icDB f or Post greSQL. |
|   | Access Met hod | The access method of the destination database. The value is fixed to Alibaba Cloud Inst ance. |

| a Transmission Service |   |   |
|---|---|---|
|   | User Guide·Data migratio |   |
| Section | Parameter | Description |
| Destination Database | Inst ance Region | The region in which the destination AnalyticDB for PostgreSQL instance resides. |
|   | Inst ance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Dat abase Account | The database account of the destination AnalyticDB for PostgreSQL instance. For more information about the permissions that are required for the account, see Permissions required for database accounts. |
|   | Dat abase password | The password of the database account. |

3. In the lower part of the page, click T est Connect ivit y and Proceed.
If the source or destination database is an Alibaba Cloud instance, such as an ApsaraDB RDS for MySQL or ApsaraDB for MongoDB instance, DTS automatically adds the CIDR blocks of DTS servers to the IP address whitelist of the instance. If the source or destination database is a self-managed database hosted on an Elastic Compute Service (ECS) instance, DTS automatically adds the CIDR blocks of DTS servers to the security group rules of the ECS instance. If the source or destination database is a self-managed database that is deployed in a data center or provided by a third-party cloud service provider, you must manually add the CIDR blocks of DTS servers to the IP address whitelist of the database to allow DTS to access the database. Warning If the CIDR blocks of DTS servers are automatically or manually added to the IP address whitelist of the database or instance, or to the ECS security group rules, security risks may arise. Therefore, before you use DTS to migrate data, you must understand and acknowledge the potential risks and take preventive measures, including but not limited to the following measures: enhance the security of your username and password, limit the ports that are exposed, authenticate API calls, regularly check the whitelist or ECS security group rules and forbid unauthorized CIDR blocks, or connect the database to DTS by using Express Connect, VPN Gateway, or Smart Access Gateway.
4. Configure the parameters described in the following table.
Basic Settings

| Parameter or setting | Description |
|---|---|

| Parameter or setting | Description |
|---|---|
| T ask St ages | To perform only full data migration, select Schema Migrat ion and Full Dat a Migrat ion. To ensure service continuity during data migration, select Schema Migrat ion, Full Dat a Migrat ion, and Increment al Dat a Migrat ion. Not e If Incremental Data Migration is not selected, we recommend that you do not write data to the source instance during data migration. This ensures data consistency between the source and destination instances. |
| Processing Mode in Exist ed T arget T able | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck, and the data migration task cannot be started. Not e You can use the object name mapping feature to rename the tables that are migrated to the destination database. You can use this feature if the source and destination databases contain identical table names and the tables in the destination database cannot be deleted or renamed. For more information, see Object name mapping. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not migrate data records that have the same primary keys as data records in the destination database. If the source and destination databases have different schemas, only specific columns are migrated or the data migration task fails. |

| Parameter or setting | Description |
|---|---|
| Select t he object s t o be migrat ed | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. |

Advanced Settings

| Paramet er or setting | Description |
|---|---|
| Ret ry T ime f or Failed Connec t ion | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS is reconnected to the source and destination databases within the specified time range, DTS resumes the data migration task. Otherwise, the data migration task fails. Not e If you set different retry time ranges for multiple data migration tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data migration task, DTS performs a precheck. You can start the data migration task only after the task passes the precheck. If the task fails to pass the precheck, click View Det ails next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
6. After the success rat e becomes 100%, the data migration task starts to run.
You can view the progress of the task on the Data Migration page.

### Manage data migration tasks

#### Object name mapping

Data Transmission Service (DTS) provides the object name mapping feature. You can use this feature to change the names of one or more objects that are migrated to the destination instance. This topic describes how to use the object name mapping feature when you configure a data migration task. Limits You can use the object name mapping feature only when a data migration task is configured and the current step is Conf igure Migrat ion T ypes and Object s. Do not use the object name mapping feature after a data migration task is started. Otherwise, data may fail to be migrated. Procedure
1. In the Conf igure Migrat ion T ypes and Object s step, move the required objects to the Select ed
section, move the pointer over a database or table, and then click Edit .
2. In the dialog box that appears, specify a name for the object in the destination instance.
Database name mapping In the Edit Dat abase Name dialog box that appears, enter the database name that you want to use in the destination instance. Table name mapping In the Edit T able dialog box that appears, enter the table name that you want to use in the destination instance. Column name mapping In the Edit T able dialog box that appears, enter a new name for each column. In this step, you can clear the options of columns that do not need to be synchronized.
3. Click OK.
4. Configure other parameters that are required for the data migration task.

#### Specify an SQL condition to filter data

This topic describes how to specify an SQL condition to filter the data of a specific table when you configure a data migration task. The SQL condition takes effect only within the table that you select. DTS migrates only the data that meets the SQL condition to the destination database. This feature is applicable to scenarios such as regular data migration and table partitioning. Limits An SQL condition applies only to full data migration. If you select increment al dat a migrat ion as the migration type, the SQL condition does not filter incremental data. Specify an SQL condition You can specify an SQL condition in the Conf igure Migrat ion T ypes and Object s step when you configure a data migration task. To filter the data of a specific table by using an SQL condition, you must select the table as the object that you want to migrate. You cannot select a database as the object. To specify an SQL condition, perform the following steps. Procedure
1. In the Conf igure Migrat ion T ypes and Object s step, move the pointer over a table in the
Select ed section. The Edit button appears, as shown in Edit button. Edit button
2. Click Edit . The Edit Table dialog box appears.
Modif y an SQL condit ion The SQL conditions in DTS are the same as the standard SQL WHERE conditions for databases. You can use SQL conditions to perform operations and run basic functions. Enter an SQL condition in the text box. For example, you can enter id>1000 to migrate the records whose IDs are greater than 1,000 to the destination instance, as shown in Modify an SQL condition. Modify an SQL condition After the SQL condition is specified, click OK.

#### Troubleshoot a failed data migration task

This topic describes how to troubleshoot a failed data migration task. You can use this feature if your data migration task is in the Migrat ion Failed state during schema migration or full data migration. Troubleshoot a failed task during schema migration DTS supports data migration between heterogeneous data sources. However, if you migrate data of unsupported types to the destination instance during schema migration, the task may fail.
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. Use one of the following methods to troubleshoot the failed task:
Method 1 a. Find the task and click View Cause and Rect if y. b. Troubleshoot the issue based on the cause that is displayed in the View Cause and Rectify message. For example, you can troubleshoot an issue by modifying the schema syntax. c. Click Rest art T ask. Method 2 a. Click the instance ID or task name. b. In the left-side navigation pane, choose Migrat ion Det ails > Schema Migrat ion. c. On the Schema Migrat ion page, find the object that causes the migration failure and click Rect if y in the Status column. d. Troubleshoot the issue based on the cause that is displayed in the Rect if y dialog box. For example, you can troubleshoot an issue by modifying the schema syntax. e. Click Rect if y. If the failure persists, the Rect if y dialog box does not close and shows the failure cause. You must continue troubleshooting based on the failure cause until the troubleshooting is successful. If the troubleshooting is successful, the Schema Migrat ion page appears and the status of the object changes to Finished.
4. If no objects are in the Failed state, DTS proceeds with the data migration task, for example, entering
the full data migration process. Troubleshoot a failed task during full data migration
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Migrat ion.
3. Find the task and click View Cause and Rect if y.
DTS allows you to troubleshoot a task that fails during full data migration due to the following reasons. If a task fails during full data migration due to other reasons, DTS provides only the Ignore option. The object that causes the failure is not migrated to the destination database. The connection to the source or destination database failed or timed out. Troubleshoot the issue, make sure that the connection is successful, and then click Rest art T ask. The storage space of the destination instance is insufficient or the instance is locked. Upgrade the specification of the destination instance or clear the log space, and then click Rest art T ask. MyISAM tables in the source database are corrupted. Troubleshoot the issue in the source database, and then click Rest art T ask.
4. In the dialog box that appears, troubleshoot the issue based on the failure cause.
5. Click Rest art T ask.

### Precheck items

#### Source database connectivity

Data Transmission Service (DTS) checks whether DTS servers can connect to the source database for migration. DTS creates a connection to the source database by using the Java Database Connectivity (JDBC) protocol. If the connection fails, the data migration task fails to pass the connectivity check. The following table describes the possible reasons for a connectivity precheck failure of the source database.

| Check item | Possible reason | Troubleshooting |
|---|---|---|
| JDBC | 1. The username or password of the database account is incorrect, or the IP address or port number of the destination database is incorrect. 2. The database account cannot be used to access the destination database over an endpoint. | 1. Check and correct the connection information about the destination database. 2. Allow access to the destination database over all endpoints. |
| Ping | 1. The network of the service to which the database instance belongs is unavailable. 2. The IP address of the destination database is incorrect. | 1. Check whether the network is available. 2. Check and correct the IP address of the destination database. |
| Telnet | 1. The DTS servers are not allowed to access the destination database. 2. The port number of the destination database is incorrect. | 1. Allow access to the destination database from the public CIDR blocks of the DTS servers. For example, disable the firewall of the service to which the destination database belongs or add the public CIDR blocks of the DTS servers to the whitelist of the destination database. 2. Check and correct the port number of the destination database. |

#### Destination database connectivity

This check item checks whether the Data Transmission Service (DTS) servers can connect to the destination database for migration. DTS creates a connection to the destination database by using the Java Database Connectivity (JDBC) protocol. If the connection fails, the check item fails. The following table describes the possible reasons for a connectivity precheck failure of the destination database.

| Check item | Possible reason | Troubleshooting |
|---|---|---|
| JDBC | 1. The username or password of the database account is incorrect, or the IP address or port number of the destination database is incorrect. 2. The database account cannot be used to access the destination database over an endpoint. | 1. Check and correct the connection information about the destination database. 2. Allow access to the destination database over all endpoints. |
| Ping | 1. The network of the service to which the database instance belongs is unavailable. 2. The IP address of the destination database is incorrect. | 1. Check whether the network is available. 2. Check and correct the IP address of the destination database. |
| Telnet | 1. The DTS servers are not allowed to access the destination database. 2. The port number of the destination database is incorrect. | 1. Allow access to the destination database from the public CIDR blocks of the DTS servers. For example, disable the firewall of the service to which the destination database belongs or add the public CIDR blocks of the DTS servers to the whitelist of the destination database. 2. Check and correct the port number of the destination database. |

#### Binary logging configurations of the source

database Whether binary logging is enabled in the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether binary logging is enabled in the source database. If binary logging is disabled in the source database, the check result is Failed. Troubleshooting: Run the `log_bin=mysql_bin` command to modify the configuration file of the source database. Restart the source database and run a precheck again. Binary log format of the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the binary log format is set to ROW in the source database. If the binary log format is not set to ROW in the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_format=ROW` command in the source database and run a precheck again. We recommend that you restart the MySQL process. Otherwise, data loss may occur because sessions will continue to be written in a non-ROW mode. Binary log files in the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether specific binary log files are removed from the source database. If binary log files in the source database are incomplete, the check result is Failed. Troubleshooting: Run the `PURGE BINARY LOGS TO 'The name of the first binary log file that is` `not deleted'` command in the source database and run a precheck again. To find the binary log files that are removed from the source database, click the info icon next to the failed item. In the View Det ails dialog box, the names of deleted binary log files are displayed. Parameter binlog_row_image of the source database This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of the binlog_row_image parameter in the source database is set to FULL. This parameter indicates whether the full image is recorded. If the full image is not recorded in binary log files of the source database, the check result is Failed. Troubleshooting: Run the `set global binlog_row_image=FULL` command in the source database and run a precheck again.

#### Integrity of the FOREIGN KEY constraints

DTS checks whether the parent table on which a child table depends is included in the selected objects. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. If the parent table on which a child table depends is not included in the selected objects, the check result is Failed. Troubleshooting: Do not migrate the child tables that cause the check failure. To do this, remove these child tables from the selected objects and run a precheck again. Migrate the parent tables rather than the child tables. To do this, add the parent tables to the selected objects and run a precheck again. Delete the foreign key dependencies between the parent and child tables in the source database and run a precheck again.

#### Existence of FEDERATED tables

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the source database contains storage engines that are not supported by incremental data migration. Incremental data migration does not support the FEDERATED and MRG_MyISAM storage engines. If t he FEDERAT ED st orage engine is used by specif ic t ables in t he source dat abase, the check result is Failed. If t he MRG_MyISAM st orage engine is used by specif ic t ables in t he source dat abase, the check result is Failed. Solution: Remove the tables that use the FEDERATED or MRG_MyISAM storage engine from the selected objects. Then, create a separate migration task to perform schema migration and full data migration for these tables.

#### Permissions

Source database permissions DTS checks whether the account of the source database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks. Destination database permissions DTS checks whether the account of the destination database has the required permissions to perform data migration. For information about the permissions that are required by each type of database, see the topics about how to configure data migration tasks.

#### Object name conflict

DTS checks whether the destination database contains objects that have the same names as the objects to be migrated. If the destination database contains objects that have the same names as the objects to be migrated, the check result is Failed. This causes migration failure. If the check result is Failed, an error message is displayed indicating that an object in the destination database has the same name as an object to be migrated. Troubleshooting: Use the object name mapping feature to map the conflicting object name to an object with a different name in the destination database. In the destination database, delete or rename the object that has the same name as the object to be migrated. Remove the conflicting object from the objects to be migrated.

#### Schema existence

This check item checks whether the database to be migrated exists in the destination instance. If the database does not exist in the destination instance, Data Transmission Service (DTS) automatically creates one. However, the check fails if DTS cannot automatically create the database in the following scenarios: The name of the database to be migrated contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). Cause of failure: The name of the source database is invalid. Troubleshooting: On the Databases page of the RDS console, create a database that meets requirements, and grant the migration account the read and write permissions on the new database. Use the database name mapping feature of DTS to map the source database to the new database. Then, perform a precheck again. The character set of the database to be migrated is not UTF-8, GBK, Latin1, or UTF-8MB4. Cause of failure: The character set of the source database is not supported. Troubleshooting: On the Databases page of the RDS console, create a database that meets requirements, and grant the migration account the read and write permissions on the new database. If the new database and the database to be migrated have different names, you can use the database name mapping feature of DTS to map the database to be migrated to the new database. Then, perform a precheck again. The migration account of the destination database has no read and write permissions on the database to be migrated. Cause of failure: You are not authorized to perform operations on the source database. Troubleshooting: On the Accounts tab of the Databases page in the RDS console, grant the migration account the read and write permissions on the database to be migrated. Then, perform a precheck again.

#### Value of server_id in the source database

This item is checked only when you migrate incremental data between MySQL databases. DTS checks whether the value of server-id in the source database is set to an integer greater than 1. If the check result is Failed, run the `set global server_id='An integer greater than 1'` command in the source database and perform a precheck again.

#### Source database version

DTS checks whether the version of the source database is supported. The table Source database types and versions lists the source database versions that are supported by DTS. Source database types and versions

| Source database type | Supported version |
|---|---|
| MySQL | 5.0, 5.1, 5.5, 5.6, and 5.7. Only 5.1, 5.5, 5.6, and 5.7 are supported for incremental data migration. |

If the check result is Failed, you must upgrade or downgrade the source database to a supported version before you perform a precheck again.

### Data type mappings between

heterogeneous databases Heterogeneous databases support different data types. During schema migration, Data Transmission Service (DTS) converts the data types of the source database into those of the destination database. This topic describes the data type mappings in detail to help you evaluate the impact of data migration on your business. Migrate data from an ApsaraDB RDS for MySQL instance or a selfmanaged MySQL database The following table describes the data type mappings between MySQL and heterogeneous databases. The source instance can be a PolarDB for MySQL cluster, an ApsaraDB RDS for MySQL instance, or a selfmanaged MySQL database. The destination instance can be an AnalyticDB for MySQL cluster or an AnalyticDB for PostgreSQL instance. If the value range of the data to be migrated from the source instance exceeds the range supported by DTS, the accuracy of the data migrated to the destination instance decreases.

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
|   | BIGINT[(M)] | -9223372036854775808 to 9223372036854775807 |   |
|   | BIGINT[(M)] [UNSIGNED] | 0 to 18446744073709551615 . |   |
| Decimal | DECIMAL[(M[,D])] | M: 0 to 65 D: 0 to 30 |   |
|   | FLOAT(p) | 1.175494351E-38 ~ 3.402823466E+38 |   |
|   | DOUBLE[(M,D)] | 2.2250738585072014E- 308 ~ 1.7976931348623157E+ 308 |   |
| 57 |   |   |   |

| Type | Data type of the source instance | Value range | Data type of a Message Queue for Apache Kafka instance or a self- managed Kafka cluster |
|---|---|---|---|
| Date and time | DATE | 1000-01-01 to 9999-12- 31 Not e The format is YYYY- MM-DD, in UTC. |   |
|   | DATETIME[(fsp)] | 1000-01-01 00:00:00.000000 to 9999-12-31 23:59:59.999999 Not e The format is YYYY- MM-DD hh:mm:ss[.fraction] , in UTC. |   |
|   | TIMESTAMP[(fsp)] | 1970-01-01 00:00:01.000000 to 2038-01-19 03:14:07.999999 Not e The format is YYYY- MM-DD hh:mm:ss[.fraction] , in UTC. |   |
|   |   |   | Consistent with the data types of MySQL |
|   | TIME[(fsp)] | -838:59:59.000000 to 838:59:59.000000 Not e The format is hh:mm:ss[.fraction] , in UTC. |   |
|   | YEAR[(4)] | 1901 to 2155, or 0000 |   |
|   | CHAR[(M)] | 0 to 255 characters |   |
|   | VARCHAR(M) | 0 to 65,535 characters |   |

| User Guide·Data migration |   |   |   |
|---|---|---|---|
| Type | Data type of the source instance | Value range | Data type of a Message Queue for Apache Kafka instance or a self- managed Kafka cluster |
| String | BINARY[(M)] | 0 to 255 bytes |   |
|   | VARBINARY(M) | 0 to 65,535 bytes |   |
|   | TINYBLOB | 255 (2^8 - 1) bytes |   |
|   | TINYTEXT | 255 (2^8 - 1) characters |   |
|   | BLOB | 65,535 (2^16 - 1) bytes |   |
|   | TEXT | 65,535 (2^16 - 1) characters |   |
|   | MEDIUMBLOB | 16,777,215 (2^24 - 1) bytes |   |
|   | MEDIUMTEXT | 16,777,215 (2^24 - 1) characters |   |
|   | LONGBLOB | 4,294,967,295 or 4 GB (2^32 - 1) bytes |   |
|   | LONGTEXT | 4,294,967,295 or 4 GB (2^32 - 1) characters |   |
|   | ENUM('value1','value2',.. .) | An ENUM column can have a maximum of 65,535 distinct elements. |   |
|   | SET('value1','value2',...) | A SET column can have a maximum of 64 distinct elements. |   |
| Spatial | GEOMETRY | Geometry values of any type |   |
|   | POINT | N/A |   |
|   | LINESTRING | N/A |   |
|   | POLYGON | N/A |   |
|   | MULTIPOINT | N/A |   |
|   | MULTILINESTRING | N/A |   |
|   | MULTIPOLYGON | N/A |   |

| Type | Data type of the source instance | Value range | Data type of a Message Queue for Apache Kafka instance or a self- managed Kafka cluster |
|---|---|---|---|
|   | GEOMETRYCOLLECTION | A collection of geometry values of any type |   |
| JSON | JSON | N/A |   |

Migrate data from an Oracle database The following table describes the data type mappings between a self-managed Oracle database and heterogeneous databases. The destination instance can be a self-managed MySQL database, a PolarDB for MySQL cluster, an AnalyticDB for MySQL cluster, an AnalyticDB for PostgreSQL instance, or a PolarDB for Oracle cluster. If the value range of the data to be migrated from the source instance exceeds the range supported by DTS, the accuracy of the data migrated to the destination instance decreases.

| Type | Data type of Oracle | Value range | Data type of MySQL or PolarDB-X | Data type of AnalyticDB for PostgreSQL | Data type of PolarDB for Oracle |
|---|---|---|---|---|---|
| Numeric | NUMBER(p,s) | 1 to 22 bytes. The argument p indicates precision. Valid values: 1 to 38. The argument s indicates scale. Valid values: -84 to 127. | DECIMAL[(p[,s]) ] | DECIMAL \| TINYINT \| SMALLINT \| INTEGER \| BIGINT | NUMBER(p,s) |
|   | FLOAT(p) | 1 to 22 bytes. The variable p indicates a pointer. Valid values: 1 to 126, in units of bits. | DOUBLE | DOUBLE PRECISION | DOUBLE PRECISION |
|   | BINARY FLOAT _ | A 32-bit floating-point number (4 bytes) | DECIMAL(65,8) | DOUBLE PRECISION | REAL |

|   | igration Data Transmission Servic |   |   |   |   |
|---|---|---|---|---|---|
| Type | Data type of Oracle | Value range | Data type of MySQL or PolarDB-X | Data type of AnalyticDB for PostgreSQL | Data type of PolarDB for Oracle |
|   | BINARY DOUBL _ E | A 64-bit floating-point number (8 bytes) | DOUBLE | DOUBLE PRECISION | DOUBLE PRECISION |
|   | DATE | N/A | DATETIME | TIMESTAMP(0) | DATE |
|   | TIMESTAMP [(fractional se _ conds precisio _ n)] | N/A | DATETIME[(frac tional second _ s precision)] _ | TIMESTAMP | TIMESTAMP [(fractional se _ conds precisio _ n)] |
|   | TIMESTAMP [(fractional se _ conds precisio _ n)] WITH TIME ZONE | N/A | DATETIME[(frac tional second _ s precision)] _ | TIMESTAMP WITH TIME ZONE | TIMESTAMP [(fractional se _ conds precisio _ n)] WITH TIME ZONE |
| Date and time |   |   |   |   |   |
|   | TIMESTAMP [(fractional se _ conds precisio _ n)] WITH LOCAL TIME ZONE | N/A | DATETIME[(frac tional second _ s precision)] _ | TIMESTAMP WITH TIME ZONE | TIMESTAMP [(fractional se _ conds precisio _ n)] WITH TIME ZONE |
|   | INTERVAL YEAR [(year precisio _ n)] TO MONTH | N/A | Not supported | VARCHAR(32) | INTERVAL |
|   | INTERVAL DAY [(day precision _ )] TO SECOND [(fractional se _ conds precisio _ n)] | N/A | Not supported | VARCHAR(32) | INTERVAL |
|   | CHAR [(size [BYTE \| CHAR])] | 2,000 bytes | CHAR[(n)] | CHAR | CHAR [(size [BYTE \| CHAR])] |
|   | NCHAR[(size)] | 2,000 bytes | NATIONAL CHAR[(n)] | VARCHAR | NCHAR[(size)] |

| Type | Data type of Oracle | Value range | Data type of MySQL or PolarDB-X | Data type of AnalyticDB for PostgreSQL | Data type of PolarDB for Oracle |
|---|---|---|---|---|---|
| String | VARCHAR2(size [BYTE \| CHAR]) | If MAX STRING S _ _ IZE is set to EXTENDED, the maximum size is 32,767 bytes. If MAX STRING S _ _ IZE is set to STANDARD, the maximum size is 4,000 bytes. | VARCHAR(n) | VARCHAR | VARCHAR2(size [BYTE \| CHAR]) |
|   | NVARCHAR2(si ze) | If MAX STRING S _ _ IZE is set to EXTENDED, the maximum size is 32,767 bytes. If MAX STRING S _ _ IZE is set to STANDARD, the maximum size is 4,000 bytes. | NATIONALVAR CHAR[(n)] | VARCHAR | NVARCHAR2(si ze) |
|   | LONG | The maximum size is 2 GB (2^31 - 1). | LONGTEXT | TEXT | LONG |
|   | RAW(size) | The maximum size is 32,767 bytes or 2,000 bytes. | VARBINARY(20 00) | BYTEA | RAW(size) |
|   | LONG RAW | The maximum size is 2 GB. | LONGBLOB | BYTEA | LONG RAW |
|   | CLOB | The maximum size is (4 GB - 1) × DB BLOCK SIZE _ _ . | LONGTEXT | TEXT | CLOB |

|   | igration Data Transmission Servic |   |   |   |   |
|---|---|---|---|---|---|
| Type | Data type of Oracle | Value range | Data type of MySQL or PolarDB-X | Data type of AnalyticDB for PostgreSQL | Data type of PolarDB for Oracle |
|   | NCLOB | The maximum size is (4 GB - 1) × DB BLOCK SIZE _ _ . | LONGTEXT | TEXT | CLOB |
|   | BLOB | The maximum size is (4 GB - 1) × DB BLOCK SIZE _ _ . | LONGBLOB | BYTEA | BLOB |
|   | BFILE | The maximum size is 4 GB. | Not supported | Not supported | Not supported |
| JSON | JSON | The maximum size is 32 MB. | Not supported | JSON | JSON |
| ROWID | ROWID | 64 characters | Not supported | OID | VARCHAR |
| Spatial | Customization required | Not supported |   |   |   |

Destination instance: MySQL or PolarDB-X If a field of the CHAR data type in the source database is greater than 255 bytes in length, DTS converts this field to the VARCHAR(n) data type in the destination database. MySQL does not support the following Oracle data types: BFILE, INTERVAL YEAR TO MONTH, and INTERVAL DAY TO SECOND. Therefore, DTS does not convert these data types during schema migration. If a table to be migrated contains these data types, schema migration fails. You must make sure that the columns of these data types are excluded from the objects to be migrated. The TIMESTAMP data type of MySQL databases does not contain the time zone information. However, the TIMESTAMP WITH TIME ZONE and TIMESTAMP WITH LOCAL TIME ZONE data types in Oracle databases provide the time zone information. Therefore, DTS converts the values of the latter two data types to UTC time in the destination database. Destination instance: AnalyticDB for PostgreSQL If an Oracle data type is not supported by AnalyticDB for PostgreSQL, DTS converts the data type to BYTEA. If the conversion fails, DTS sets the field value to NULL.

## Data synchronization

### Supported database types, initial

synchronization types, and

### synchronization topologies

You can use Data Transmission Service (DTS) to synchronize data between various data sources. This topic describes the database types, initial synchronization types, and synchronization topologies that are supported by DTS.

| Source database type | Destination database type | Initial synchronization type | Synchronizatio n topology |
|---|---|---|---|
| Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 ApsaraDB RDS for MySQL Version 5.6, 5.7 or 8.0 | Self-managed MySQL database Version 5.1, 5.5, 5.6, or 5.7 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n Two-way synchronizatio n |
|   | ApsaraDB RDS for MySQL Version 5.6, 5.7 or 8.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n Two-way synchronizatio n |
|   | AnalyticDB for MySQL Version 2.0 or 3.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
|   | AnalyticDB for PostgreSQL Version 4.3 or 6.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
|   | Datahub | Initial schema synchronization | One-way synchronizatio n |

|   | Data Transmission Servic |   |   |
|---|---|---|---|
| Source database type | Destination database type | Initial synchronization type | Synchronizatio n topology |
|   | MaxCompute | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
| PolarDB-X (formerly known as DRDS) | PolarDB-X | Initial full data synchronization | One-way synchronizatio n |
|   | Datahub | Initial schema synchronization | One-way synchronizatio n |
|   | AnalyticDB for MySQL Version 2.0 or 3.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
| Self-managed PostgreSQL database Version 9.4, 9.5, 9.6, 10.x, 11, or 12 ApsaraDB RDS for PostgreSQL Version 9.4 or 10 | AnalyticDB for PostgreSQL Version 4.3 or 6.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
| Self-managed Db2 database DB2 for LUW | AnalyticDB for PostgreSQL Version 4.3 or 6.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n |
| Self-managed Oracle database in a RAC or non-RAC architecture Version 9i, 10g, 11g, 12c, 18c, or 19c | DataHub All versions | Initial schema synchronization | One-way synchronizatio n |
| ApsaraDB for Redis Version 4.0 or 5.0 | ApsaraDB for Redis Version 4.0 or 5.0 | Initial schema synchronization Initial full data synchronization | One-way synchronizatio n Two-way synchronizatio n |

### Create a data synchronization

instance Before you configure a task to synchronize data, you must create a data synchronization instance. This topic describes how to create a data synchronization instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. Click Creat e T ask.
4. In the panel that appears, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Source Inst ance Region | The region in which the source instance resides. Not e You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Source Inst ance T ype | The type of the source database. For more information about supported types of source databases, see Database types, initial synchronization types, and synchronization topologies. |
| Dest inat ion Inst ance Region | The region in which the destination instance resides. Not e You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Dest inat ion Inst ance T ype | The type of the destination database. For more information about supported types of destination databases, see Database types, initial synchronization types, and synchronization topologies. |
| Synchronizat ion Mode | The mode in which data is synchronized. For more information about the supported synchronization modes, see Database types, initial synchronization types, and synchronization topologies. |
| Inst ances t o Creat e | The number of data synchronization instances that you want to create at a time. |

In this panel, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.
5. Click Creat e.

### Synchronization topologies

The data synchronization feature supports multiple types of synchronization topologies. You can plan your data synchronization instances based on your business requirements. This topic describes the synchronization topologies that are supported by Data Transmission Service (DTS) and how to use these topologies. One-way synchronization To ensure data consistency for one-way synchronization, we recommend that you perform only read operations on the objects in the destination instance. Do not perform write operations on the objects.

| Topology type | Topology | Description |
|---|---|---|
| One-way one- to-one synchronizatio n |   | N/A |
| One-way one- to-many synchronizatio n |   | You must purchase multiple data synchronization instances to implement one-way one-to- many synchronization. For example, if you want to synchronize data from Instance A to Instance B, Instance C, and Instance D, you must purchase three data synchronization instances. |

| Topology type | Topology | Description |
|---|---|---|
| One-way cascade synchronizatio n |   | You must purchase multiple data synchronization instances to implement one-way cascade synchronization. For example, if you want to synchronize data from Instance A to Instance B and then from Instance B to Instance C, you must purchase two data synchronization instances. |
| One-way many-to-one synchronizatio n |   | You must purchase multiple data synchronization instances to implement one-way many- to-one synchronization. For example, if you want to synchronize data from Instance B, Instance C, and Instance D to Instance A, you must purchase three data synchronization instances. Not e To ensure data consistency, you must select different objects to synchronize for these data synchronization instances. |

Two-way synchronization DTS supports two-way synchronization only between two MySQL databases or ApsaraDB for Redis databases.

| Topology type | Topology | Description |
|---|---|---|
| Two-way one- to-one synchronizatio n |   | To ensure data consistency, make sure that data records with the same primary key, business primary key, or unique key are updated on only one of the source and destination instances. |

### Configure data synchronization

tasks

#### Configure between ApsaraDB RDS for

MySQL instances This topic describes how to configure one-way data synchronization between ApsaraDB RDS for MySQL instances by using Data Transmission Service (DTS). Prerequisites The source and destination ApsaraDB RDS for MySQL instances are created. Limits

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Category | Description |
|---|---|
| Other limits | To ensure compatibility, the version of the destination ApsaraDB RDS for MySQL database must be the same as or later than the version of the source ApsaraDB RDS for MySQL database. DTS supports initial schema synchronization for triggers. However, data inconsistency may occur due to triggers. We recommend that you delete the triggers of the source database to prevent data inconsistency caused by the triggers. Limits on RENAME TABLE operations during data synchronization: RENAME TABLE operations may cause data inconsistency between the source and destination databases. For example, if you select a table as the object to be synchronized and rename the table during data synchronization, the data of this table is not synchronized to the destination database. To prevent this situation, you can select the database to which this table belongs as the object to be synchronized when you configure the data synchronization task. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |
| Other limits | Take note of the following items when you configure two-way data synchronization between MySQL instances: To configure two-way data synchronization, you must purchase basic plans for cross-cloud data synchronization and two-way data synchronization. DTS supports two-way data synchronization only between two MySQL databases. DTS does not support two-way data synchronization between multiple MySQL databases. Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. When DTS runs a two-way data synchronization task, DTS creates a database named dts in the destination database to prevent circular synchronization. When the task is running, do not modify the dts database. |

Supported synchronization topologies DTS supports one-way data synchronization and two-way synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized

| Operatio n type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, DELETE, and REPLACE |
| DDL | ALTER TABLE and ALTER VIEW CREATE FUNCTION, CREATE INDEX, CREATE PROCEDURE, CREATE TABLE, and CREATE VIEW DROP INDEX and DROP TABLE RENAME TABLE TRUNCATE TABLE |

Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type and Destination Instance Type parameters to MySQL, and set the Synchronization Mode parameter to One-Way Synchronizat ion.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Instance Details | Instance Type | The access method of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. Not e If the database engine of the source ApsaraDB RDS for MySQL instance is MySQL 5.6, you do not need to configure the Dat abase Account and Dat abase Password parameters. |
|   | Database Password | The password of the database account. |
| ocument Version: | 20230625 17 |   |

|   | hronization Data Transmission Servic |   |
|---|---|---|
| Section | Parameter | Description |
|   | Encryption | The encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
|   | Instance Type | The access method of the destination database. Select RDS Inst ance. |
|   | Instance Region | The region in which the destination instance resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
| Destination Instance Details |   |   |
|   | Instance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the destination ApsaraDB RDS for MySQL instance. Not e If the database engine of the destination ApsaraDB RDS for MySQL instance is MySQL 5.6, you do not need to configure the Dat abase Account and Dat abase Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | The encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the destination ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the processing mode of conflicting tables and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|

| Parameter or setting | Description |
|---|---|
| Processing Mode in Existed Target Table | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Select the objects to be synchronized | Select a database or tables as the objects to be synchronized from the Available section and click the icon to add the objects to the Select ed section. Not e If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |

| Parameter or setting | Description |
|---|---|
| Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
| Specify whether to copy temporary tables to the destination database when DMS performs online DDL operations on the source tables | If you use DMS to perform online DDL operations on the source database, you can specify whether to synchronize temporary tables generated by online DDL operations. Yes: DTS synchronizes the data of temporary tables generated by online DDL operations. Not e If online DDL operations generate a large amount of data, the data synchronization task may take an extended period of time to complete. No: DTS does not synchronize the data of temporary tables generated by online DDL operations. Only the original DDL data of the source database is synchronized. Not e If you select No, the tables in the ApsaraDB RDS for MySQL instance may be locked. |
| Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

6. In the lower-right corner of the page, click Next .
7. Configure initial synchronization.
Initial synchronization includes initial schema synchronization and initial full data synchronization. If you select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion, DTS synchronizes the schemas and historical data of the objects to be synchronized before DTS synchronizes incremental data.
8. In the lower-right corner of the page, click Precheck.
You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, you can click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from an ApsaraDB RDS

for MySQL instance to a MaxCompute project This topic describes how to synchronize real-time data from an ApsaraDB RDS for MySQL instance to a MaxCompute project by using Data Transmission Service (DTS). This facilitates real-time data analysis. Features DTS supports real-time data synchronization from an ApsaraDB RDS for MySQL instance to a MaxCompute project within the same Alibaba Cloud account. DTS supports RDS instances that can be accessed over the classic network or a virtual private cloud (VPC). Objects to be synchronized You can select only tables as the objects to be synchronized. Synchronization process The synchronization process consists of two stages:
1. Initial full data synchronization.
In this stage, all existing data of the ApsaraDB RDS for MySQL instance is synchronized to the MaxCompute project. Data in each table is synchronized and stored independently to a full baseline table in the MaxCompute project. The default name of the full baseline table is source table name_base. For example, if the source table is named t1, the full baseline table in the destination MaxCompute project is named t1_dts_base. When you configure the data synchronization task, you can modify the prefix of the table name in the destination MaxCompute project.
2. Incremental data synchronization.
In this stage, the incremental data that is generated in the ApsaraDB RDS for MySQL instance is synchronized to the MaxCompute project in real time. The incremental data is stored in incremental data tables in MaxCompute. Each source table corresponds to an incremental data table. The default name of an incremental data table in MaxCompute is source table name_log. When you configure the data synchronization task, you can modify the prefix of the table name in the destination MaxCompute project. Incremental data tables store both the incremental data and specific metadata. Schema design describes the schema of an incremental data table. Schema design

| record id _ | operation fl _ ag | utc timestamp _ | before fla _ g | after fla _ g | col 1 | ... | colN |
|---|---|---|---|---|---|---|---|
| 1 | I | 1476258462 | N | Y | 1 | ... | JustInsert |
| 2 | U | 1476258463 | Y | N | 1 | ... | JustInsert |
| 2 | U | 1476258463 | N | Y | 1 | ... | JustUpdate |
| 3 | D | 1476258464 | Y | N | 1 | ... | JustUpdate |

In the preceding table: record_id: the unique ID of an incremental log entry. The ID auto-increments for each new log entry. If an UPDATE operation is performed on a data record, DTS generates two log entries for an INSERT operation and a DELETE operation. The values of the record_id field in the two log entries are the same. operation_flag: the operation type of the incremental log entry. Valid values: I: an INSERT operation D: a DELETE operation U: an UPDATE operation dts_utc_timestamp: the operation timestamp of the incremental log. It is also the timestamp of the binary log file for the UPDATE record. The timestamp is in the UTC format. before_flag: indicates whether the column values that follow the incremental log entry are preupdate values. Valid values: Y and N. The value of the before_flag field is Y if the column values that follow the log entry are pre-update values. The value of the before_flag field is N if the column values are post-update values. after_flag: indicates whether the column values that follow the incremental log entry are postupdate values. Valid values: Y and N. The value of the after_flag field is N if the column values that follow the log entry are pre-update values. The value of the after_flag field is Y if the column values are post-update values. The before_flag and after_flag fields of an incremental log entry are defined based on the operation type. INSERT operation

| record i _ d | operation fla _ g | utc timestamp _ | before flag _ | after fla _ g | co l1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 1 | I | 1476258462 | N | Y | 1 | .. . | JustInser t |

For an INSERT operation, the column values that follow an incremental log entry are the newly inserted record values (post-update values). Therefore, the value of the before_flag field is N and the value of the after_flag field is Y. UPDATE operation

| record id _ | operation fla _ g | utc timestamp _ | before flag _ | after fla _ g | co l1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 2 | U | 1476258463 | Y | N | 1 | .. . | JustInsert |
| 2 | U | 1476258463 | N | Y | 1 | .. . | JustUpdat e |

When an UPDATE operation is performed, two incremental log entries are generated. The two incremental log entries have the same values for the record_id, operation_flag, and dts_utc_timestamp fields. The first log entry records the pre-update values, so the value of the before_flag field is Y and the value of the after_flag field is N. The second log entry records the post-update values, so the value of the before_flag field is N and the value of the after_flag field is Y. DELETE operation

| record i _ d | operation fla _ g | dts utc timestam _ _ p | before fla _ g | after fla _ g | c ol 1 | .. . | colN |
|---|---|---|---|---|---|---|---|
| 3 | D | 1476258464 | Y | N | 1 | .. . | JustUpdat e |

For a DELETE operation, the column values that follow an incremental log entry are the deleted record values (pre-update values). Therefore, the value of the before_flag field is Y and the value of the after_flag field is N. For each table synchronized from an ApsaraDB RDS for MySQL instance to a MaxCompute project, a full baseline table and an incremental data table are generated in the MaxCompute project. To retrieve the full data of a specific table at a specific point in time in the MaxCompute project, you must merge the corresponding full baseline table and incremental data table. The merging procedure is described later. Limits

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
| Other limits | Only tables can be selected as the objects to be synchronized. MaxCompute does not support PRIMARY KEY constraints. If network errors occur, DTS may synchronize duplicate data records to MaxCompute. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

Configure a data synchronization task This section describes how to configure a task for synchronizing data from an ApsaraDB RDS for MySQL instance to a MaxCompute project in real time.
1. Create a data synchronization instance.
When you create a data synchronization instance, set Source Dat abase T ype to MySQL, Dest inat ion Dat abase T ype to MaxComput e, and Synchronizat ion T opology to One-Way Synchronizat ion.
2. Find the data synchronization instance that you want to manage and click Conf igure T ask in the
Act ions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The instance type of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. Not e If the database engine of the source ApsaraDB RDS for MySQL instance. is MySQL 5.5 or MySQL 5.6, you do not need to configure the Dat abase Account and Dat abase Password parameters. |
|   | Database Password | The password of the database account. |
|   | Encryption | Specifies whether to encrypt the connection to the source instance. Select Non-encrypt ed or SSL-encrypt ed based on your business requirements. If you select SSL-encrypt ed, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
| Destination Database | Database Type | The instance type of the destination instance. This parameter is set to MaxComput e and cannot be changed. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the MaxCompute project. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. In the lower-right corner of the page, click Next . In this step, permissions for the MaxCompute project
are granted to the synchronization account.
6. Select the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|
| Partition Definition of Incremental Data Table | Select the partition names based on your business requirements. |
| Initial Synchronization | Valid values: Initial Schema Synchronization and Initial Full Data Synchronization. Select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion. In this case, DTS synchronizes the schemas and historical data of the objects and then synchronizes incremental data. |
| Select the objects to be synchronized | Select one or more tables from the Available section and click the icon to move the tables to the Select ed section. Not e You can select tables from multiple databases as the objects to be synchronized. By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |
| Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is not available and you cannot configure name mapping for tables or columns. |

| Parameter or setting | Description |
|---|---|
| Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |
| Whether to enable new additional column rules | After DTS synchronizes data to MaxCompute, DTS adds additional columns to the destination table. If the names of additional columns are the same as the names of existing columns in the destination table, data synchronization fails. Select Yes or No to specify whether you want to enable new naming rules for additional columns. Warning Before you specify this parameter, check whether additional columns have the same names as the existing columns in the destination table. |

In this step, you need to configure the initial synchronization and select the tables to be synchronized. i. Select the initial synchronization types Two options are available for initial synchronization: Initial Schema Synchronization and Initial Full Data Synchronization. During initial schema synchronization, DTS creates a table that has the same schema as the table to be synchronized in the MaxCompute project. During initial full data synchronization, DTS replicates all the existing data in the table to be synchronized to the MaxCompute project. We recommend that you select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion when you configure the data synchronization task. ii. Select the tables to be synchronized You can select only tables as objects to be synchronized rather than the entire database. Each table to be synchronized corresponds to a full baseline table and an incremental data table in the MaxCompute project. To modify the name of a table, click Edit next to the table to open the Edit Table Name dialog box, as shown in the following figure. Edit Table Name
7. Click Precheck to start a precheck.
After the precheck is successful, click Close and start the data synchronization task. After the task is started, the task list appears. The task is in the Perf orming init ial synchronizat ion state. The duration of the initial synchronization depends on the data volume of the objects that you want to synchronize. After the initial synchronization is complete, the data synchronization task enters the Synchronizing state. The synchronization channel between the source and destination instances is established. When the data synchronization task is in the Synchronizing state, you can query the full baseline table and incremental data table in MaxCompute, as shown in the following figure. Query table information You have configured the task for synchronizing data from an ApsaraDB RDS for MySQL instance to a MaxCompute project in real time. Merge a full baseline table and an incremental data table This section describes how to retrieve the full data of a table at a specific point in time from the full baseline table and incremental data table in the MaxCompute project. You can use SQL statements to merge the two tables. After you merge the full baseline table and incremental data table in MaxCompute by using SQL statements, you can obtain the full data at a specific point in time. The following sample code shows the SQL statements that you can run to merge the two tables:

```
insert overwrite table result_storage_table select col1,
       col2,
       colN
  from(
select row_number() over(partition by t.primary_key_column
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, after_
flag, col1,col2,colN
  from(
select incr.record_id, incr.operation_flag, incr.after_flag, incr.col1, incr.col2,incr.colN
  from table_log incr
 where utc_timestamp< timestmap
 union all
select 0 as record_id, 'I' as operation_flag, 'Y' as after_flag, base.col1, base.col2,base. colN
  from table_base base) t) gt
where record_num=1
  and after_flag='Y'
```

Take note of the following variables in the preceding code: result_storage_table: the name of the table that stores the merged data. col1, col2, colN: the names of the columns in the table to be merged. primary_key_column: the name of the primary key column in the table to be merged. table_log: the name of the incremental data table. table_base: the name of the full baseline table. timestamp: the timestamp when the full data to be merged is generated. In the preceding example, the jiangliu_test_20161010_base table is the full baseline table that corresponds to the jiangliu_test table. The jiangliu_test_20161010_log table is the incremental data table that corresponds to the jiangliu_test table. Schema design describes the schema of the jiangliu_test table. Schema design You can run the following SQL statements in MaxCompute to query the full data of the jiangliu_test table at the 1476263486 time:

```
insert overwrite table jiangliu_test_1476263486 select id,
       name
  from(
select row_number() over(partition by t.id
 order by record_id desc, after_flag desc) as row_number, record_id, operation_flag, after_
flag, id, name
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

You can also use DataWorks to add full data merging nodes before you perform further computing and analysis. After full data is merged, downstream computing and analysis nodes can be automatically triggered. You can set an interval for periodic offline data analysis. After that, you have configured the task for synchronizing data from an ApsaraDB RDS for MySQL instance to a MaxCompute project in real time and merged the full data of tables.

#### Synchronize data from an ApsaraDB RDS

for MySQL instance to an AnalyticDB for MySQL cluster AnalyticDB for MySQL is a real-time online analytical processing (OLAP) service that is developed by Alibaba Cloud for online data analysis with high concurrency. This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for MySQL cluster by using Data Transmission Service (DTS). After you synchronize data, you can use AnalyticDB for MySQL to build internal business intelligence (BI) systems, interactive query systems, and real-time report systems. Prerequisites The tables that you want to synchronize from the ApsaraDB RDS for MySQL instance contain primary keys. The destination AnalyticDB for MySQL cluster has sufficient storage space. Limits

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Category | Description |
|---|---|
| Other limits | Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. Due to the limits of AnalyticDB for MySQL clusters, if the disk space usage of the nodes in an AnalyticDB for MySQL cluster exceeds 80%, latency occurs in the data synchronization task and error messages are returned. We recommend that you estimate the required disk space based on the objects to be synchronized. You must make sure that the destination cluster has sufficient storage space. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

SQL operations that can be synchronized DDL operations: CREATE TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE, ADD COLUMN, and DROP COLUMN DML operations: INSERT, UPDATE, and DELETE We recommend that you do not change the data type of fields in the source table during data synchronization. Otherwise, DTS generates an error message and stops the data synchronization task. Data type mappings The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-to-one correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table describes the data types that DTS can convert.

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL V3.0 |
|---|---|
| BIGINT UNSIGNED | DECIMAL(20,0) |

| ata Transmission Service | User Guide·Data synchronizatio |
|---|---|
| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL V3.0 |
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
| MULTIPOINT | VARBINARY |
| MULTIPOLYGON | VARBINARY |
| NUMBERIC | DECIMAL |

| ser Guide·Data synchronization | Data Transmission Servic |
|---|---|

| Data type of ApsaraDB RDS for MySQL | Data type of AnalyticDB for MySQL V3.0 |
|---|---|
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

Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type parameter to MySQL, the Destination Instance Type parameter to Analyt icDB, and the Synchronization Mode parameter to One-Way Synchronizat ion.
2. On the Synchronization Task page, find the data synchronization instance that your created and click
Conf igure T ask in the Act ions column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Instance Type | The access method of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source instance resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |

|   | rvice | User Guide·Data synchronizatio |
|---|---|---|
| a Transmission Se |   |   |
| Section | Parameter | Description |
| Source Instance Details | Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. The account must have the SELECT permission on the objects to be synchronized and the REPLICATION CLIENT, REPLICATION SLAVE, and SHOW VIEW permissions. Not e If the database engine of the source ApsaraDB RDS for MySQL instance. is MySQL 5.5 or MySQL 5.6, you do not need to configure the Dat abase Account and Dat abase Password parameters. |
|   | Database Password | The password of the database account of the source ApsaraDB RDS for MySQL instance. |
|   | Encryption | The encryption method. If you select SSL-encrypt ed, you must enable SSL encryption for the ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
| Destination Instance Details | Instance Type | The value of this parameter is fixed to Analyt icDB and cannot be changed. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Version | The version of the destination AnalyticDB for MySQL cluster. Select 3.0. |
|   | Database | The ID of the destination AnalyticDB for MySQL cluster. |
|   | Database Account | The database account of the destination AnalyticDB for MySQL cluster. The account must have the read and write permissions on the destination database. |
|   | Database Password | The password of the database account of the destination AnalyticDB for MySQL cluster. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|
| Initial Synchronization | You need to select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion by default. After the precheck is complete, DTS synchronizes the schemas and data of the objects to be synchronized from the source instance to the destination instance. The schemas and data are the basis for subsequent incremental data synchronization. |

| Parameter or setting | Description |   |   |
|---|---|---|---|
| Processing Mode in Existed Target Table | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur between the source and destination databases, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |   |   |
| Merge Multi Tables | Specifies whether to merge tables. If you select Yes, DTS adds the dts dat __ _ a source column to each table to store data sources. In this case, DDL _ operations cannot be synchronized. If you select No, DDL operations can be synchronized. By default, No is selected. Not e If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. |   |   |
|   |   | dts dat __ _ |   |
| Synchronization Type | Select the types of operations that you want to synchronize based on your business requirements. All operation types are selected by default. Not e Only the INSERT, UPDATE, DELETE, and ADD COLUMN operations can be synchronized. |   |   |

|   | a source _ |
|---|---|

| Parameter or setting | Description |
|---|---|
| Select the objects to be synchronized | Select a database or tables as objects from the Available section and click the icon to add the objects to the Select ed section. Not e If you select a database as the object to be synchronized, all schema changes in the database are synchronized to the destination database. By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to change the names of the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |
| Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
| Specify whether to copy temporary tables to the destination database when DMS performs online DDL operations on the source tables | If you use DMS to perform online DDL operations on the source database, you can specify whether to migrate data of temporary tables generated by online DDL operations. If you select Yes, DTS migrates the data of temporary tables generated by online DDL operations. Not e If online DDL operations generate a large amount of data, the data migration task may take an extended period of time to complete. If you select No, DTS does not migrate the data of temporary tables generated by online DDL operations. Only the original DDL data of the source database is migrated. Not e If you select No, the tables in the AnalyticDB for MySQL cluster may be locked. |
| Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

6. Click Next : Advanced Set t ings.

| Paramet er | Descript ion |
|---|---|
| Ret ry T ime f or Failed Connect ion | The retry time range for failed connections. If the source or destination database fails to be connected after the data synchronization task is started, DTS immediately retries a connection within the time range. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |
| Conf igure ET L | Specifies whether to configure the extract, transform, and load (ETL) feature. Yes: configures the ETL feature. You can enter data processing statements in the code editor. For more information, see Configure ETL in a data synchronization task. No: does not configure the ETL feature. |

7. Specify a type for the tables that you want to synchronize to the destination database.
After you select Init ial Schema Synchronizat ion, you must specify the t ype, primary key column, and part it ion key column for the tables that you want to synchronize to the AnalyticDB for MySQL cluster.
8. In the lower-right corner of the page, click Precheck.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from an ApsaraDB RDS

for MySQL instance to an AnalyticDB for PostgreSQL instance This topic describes how to synchronize data from an ApsaraDB RDS for MySQL instance to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature allows you to transfer and analyze data with ease. Prerequisites The tables that you want to synchronize from the source database contain primary keys. The destination AnalyticDB for PostgreSQL instance is created. Limits

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Category | Description |
|---|---|
| Other limits | Requirements for the objects to be synchronized: You can select only tables as the objects to be synchronized. DTS does not synchronize data of the following data types: BIT, VARBIT, GEOMETRY, ARRAY, UUID, TSQUERY, TSVECTOR, and TXID SNAPSHOT. _ Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source instance. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

SQL operations that can be synchronized DML operations: INSERT, UPDATE, and DELETE DDL operations: ALTER TABLE, ADD COLUMN, DROP COLUMN, and RENAME COLUMN The CREATE TABLE and DROP TABLE operations are not supported. If you want to synchronize data from a new table, you can add the table to the selected objects. For more information, see Add objects to a data synchronization task. Term mapping

| Term in ApsaraDB RDS for MySQL | Term in AnalyticDB for PostgreSQL |
|---|---|
| Database | Schema |
| Table | Table |

Create a data structure in the destination instance You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source instance. Configure a data synchronization task
1. Create a data synchronization instance.
When you create the data synchronization instance, select MySQL as the source instance type, Analyt icDB f or Post greSQL as the destination instance type, and One-way Synchronizat ion as the synchronization topology.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Database Type | The instance type of the source database. Select RDS Inst ance. |
|   | Instance Region | The region in which the source instance resides. |
|   | Instance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Encryption | Specifies whether to encrypt the connection to the source instance. Select Non-encrypt ed or SSL- encrypt ed based on your business requirements. Not e If you select SSL-encrypt ed, you must enable SSL encryption for the source ApsaraDB RDS for MySQL instance before you configure the data synchronization task. |
| Destination Database | Database Type | The instance type of the destination database. This parameter is set to Analyt icDB f or Post greSQL. |
|   | Instance Region | The region in which the destination instance resides. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |

|   |   | User Guide·Data synchronizatio |
|---|---|---|
| Destination Database Section | Parameter | Description |
|   | Database Account | The database account of the destination AnalyticDB for PostgreSQL instance. Not e The database account must have the SELECT, INSERT, UPDATE, DELETE, COPY, TRUNCATE, and ALTER TABLE permissions. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Wait until the synchronization account is created. Then, click Next .
6. Configure the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|
| Initial Synchronization | Select Init ial Full Dat a Synchronizat ion. Not e DTS synchronizes the historical data of the objects from the source instance to the destination instance. The historical data is the basis for subsequent incremental synchronization. |

| Parameter or setting | Description |
|---|---|
| Processing Mode of Conflicting Tables | Pre-check and int ercept (Selected by default) Checks the Schema Name Conf lict item and returns an error message if the destination table contains data. Clear T arget T able Skips the Schema Name Conf lict item during the precheck and clears the data in destination tables before initial full data synchronization. If you want to synchronize your business data after the data synchronization task is tested, you can select this mode. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data consistency is not ensured, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Synchronization Type | Insert Updat e Delet e Alt erT able Not e Select the types of operations that you want to synchronize based on your business requirements. |
| Select the objects to be synchronized | You can select only tables as the objects to be synchronized. You can use the object name mapping feature to rename the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. Not e The CREATE TABLE operation is not supported. To synchronize data from a new table, you must add the table to the selected objects. For more information, see Add objects to a data synchronization task. |

| Parameter or setting | Description |
|---|---|
| Specify whether to rename objects | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Name bat ch change option is not available and you cannot configure name mapping for tables or columns. |
| Specify whether to copy temporary tables to the destination database when DMS performs online DDL operations on the source tables | If you use DMS to perform online DDL operations on the source database, you can specify whether to synchronize temporary tables generated by online DDL operations. Yes: DTS synchronizes the data of temporary tables generated by online DDL operations. Not e If online DDL operations generate a large amount of data, the data synchronization task may take an extended period of time to complete. No: DTS does not synchronize the data of temporary tables generated by online DDL operations. Only the original DDL data of the source database is synchronized. Not e If you select No, the tables in the destination database may be locked. |
| Specify the retry time range for a failed connection to the source or destination database | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

| Parameter or setting | Description |
|---|---|
| Enclose Object Names in Quotation Marks | Specifies whether to enclose object names in quotation marks. If you select Yes and the following conditions are met, DTS encloses object names in single quotation marks (') or double quotation marks (") during schema synchronization and incremental data synchronization. The business environment of the source database is case-sensitive, and the database name contains both uppercase and lowercase letters. A source table name does not start with a letter and contains characters other than letters, digits, and special characters. Not e A source table name can contain only the following special characters: underscores ( ), number signs (#), and dollar _ signs ($). The names of the schemas, tables, or columns that you want to synchronize are keywords of the destination database, reserved keywords, or invalid characters. Not e If you select Yes, after DTS synchronizes data to the destination database, you must specify the object name in quotation marks to query the object. |

7. In the lower-right corner of the page, click Next : Precheck and St art T ask.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
8. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from a self-managed

PostgreSQL database to an AnalyticDB for PostgreSQL instance This topic describes how to synchronize data from a self-managed PostgreSQL database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature provided by DTS allows you to transfer and analyze data with ease. Prerequisites The source self-managed PostgreSQL database and the destination AnalyticDB for PostgreSQL instance are created. The available storage space of the AnalyticDB for PostgreSQL instance is larger than the total size of the data in the self-managed PostgreSQL database. Limits

|   | Category | Description |
|---|---|---|
|   | Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for data logs must be met: The wal level parameter is set to logical. _ Data logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the data logs generated in the source database after the DTS task is run. Not e DTS stores up to 50 GB of data logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the data logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the data logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the data logs generated 24 hours ago. As a result, the data synchronization task may fail. |
|   |   | DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source self-managed PostgreSQL database. Requirements for the objects to be synchronized: You can select only tables as the objects to be synchronized. DTS does not synchronize data of the following data types: BIT, VARBIT, GEOMETRY, ARRAY, UUID, TSQUERY, TSVECTOR, and TXID SNAPSHOT. _ A single data synchronization task can synchronize data from only one database. To synchronize data from multiple databases, you must create a data synchronization task for each database. During data synchronization, if you select a schema as the object to be synchronized, take note of the following limits: If you create a table in the schema or run the RENAME command to rename the table, you must execute the ALTER TABLE schema.table REPL ICA IDENTITY FULL; statement before you write data to the table. This ensures data consistency. Not e Replace the schema and table variables in the preceding sample statement with the actual schema name and table name. |
|   |   | ICA IDENTITY FULL; |

| Category | To ensure that the latency of data synchronization is accurate, DTS adds a heartbeat table Description named dts postgres heartbeat to the source database. _ _ |
|---|---|
| Other limits | During data synchronization, DTS creates a replication slot in the source database to replicate data. The replication slot is prefixed with dts sync . DTS automatically clears _ _ historical data in the replication slot every 90 minutes to reduce storage usage. Not e If the data synchronization task is released or fails, DTS automatically clears the replication slot. If the source database is an ApsaraDB RDS for PostgreSQL instance and a primary/secondary switchover is performed on the instance, you must log on to the secondary database to clear the replication slot. |
|   | Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

SQL operations that can be synchronized DML operations: INSERT, UPDATE, and DELETE Before you begin DTS does not synchronize the schemas of the objects to be synchronized from the source database to the destination database. You must create a database, schema, or table in the destination AnalyticDB for PostgreSQL instance based on the data structure of the source self-managed PostgreSQL database. Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, select the Source Instance Type parameter to Post greSQL, the Destination Instance Type parameter to Analyt icDB f or Post greSQL, and the Synchronization Mode parameter to One-way Synchronizat ion.
2. On the Synchronization Tasks page, find the data synchronization instance that you created and click
Conf igure T ask in the Act ions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronization Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Instance Details | Instance Type | The access method of the source database. Select the access method based on the deployment location of the source database. In this example, User-Creat ed Dat abase Connect ed Over Express Connect , VPN Gat eway, or Smart Access Gat eway is selected. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Peer VPC | The ID of the virtual private cloud (VPC) that is connected to the self-managed PostgreSQL database. |
|   | Database Type | The type of the source database. The value of this parameter is fixed to Post greSQL. |
|   | IP Address | The server IP address of the self-managed PostgreSQL database. |
|   | Port Number | The service port number of the self-managed PostgreSQL database. |
|   | Database Name | The name of the self-managed PostgreSQL database. |
|   | Database Account | The account of the self-managed PostgreSQL database. The account must have the superuser permissions. |
|   | Database Password | The password of the database account. |
|   | Instance Type | The access method of the destination database. The value of this parameter is fixed to Analyt icDB f or Post greSQL. You do not need to specify this parameter. |

|   | nization Data Transmission Servic |   |
|---|---|---|
| r Guide·Data synchro |   |   |
| Section | Parameter | Description |
| Destination Instance Details | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The initial database account of the AnalyticDB for PostgreSQL instance or the database account that has the RDS SUPERUSER _ permission. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If an IP address whitelist is configured for the self-managed PostgreSQL database, you must
manually add the CIDR blocks of DTS servers to the IP address whitelist of the database. To obtain the CIDR blocks of DTS servers, click Copy in the dialog box that appears. After you add the CIDR blocks of DTS servers to the IP address whitelist of the database, click Next . If you do not need to configure an IP address whitelist for the self-managed PostgreSQL database, ignore the preceding settings and click Next .
6. Configure the synchronization policy and the objects to be synchronized.

| Section | Parameter or setting | Description |
|---|---|---|
|   | Initial Synchronization | By default, Init ial Full Dat a Synchronizat ion is selected. After the precheck, DTS synchronizes historical data of the objects to be synchronized from the source database to the destination instance. The data is the basis for subsequent incremental synchronization. |

| Section | Parameter or setting | Description |
|---|---|---|
|   | Processing Mode in Existed Target Table | Pre-check and int ercept Checks the Schema Name Conf lict item and generates an error message if the destination table contains data. By default, this mode is selected. Clear Dat a Skips the Schema Name Conf lict item during the precheck and clears the data in destination tables before initial full data synchronization. If you want to synchronize your business data after the data synchronization task is tested, you can select this mode. Ignore Skips the check for empty destination tables during the precheck and adds data to the existing data during initial full data synchronization. If you want to synchronize data from multiple tables to one table, you can select this mode. Warning If you select Ignore, data inconsistency may occur, and your business may be exposed to risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Set the synchronization policy |   |   |
|   | Synchronization Type | Valid values: Insert Updat e Delet e Not e Select the types of operations that you want to synchronize based on your business requirements. |
| ocument Version: 20 | 230625 20 |   |

| Section | Parameter or setting | Description |
|---|---|---|
| Select the objects to be synchronized | Select the objects to be synchronized | You can select only tables as the objects to be synchronized. You can use the object name mapping feature to rename the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |
|   | Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
|   | Filter data to be synchronized | You can specify WHERE conditions to filter data. For more information, see Use SQL conditions to filter data. Import ant Filter conditions do not take effect on incremental data. |
| Others | Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 720 minutes (12 hours). You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

7. In the lower-right corner of the page, click Precheck.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
8. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial full data synchronization.

#### Synchronize data between PolarDB-X

instances PolarDB-X is formerly known as Distributed Relational Database Service (DRDS). It is compatible with the MySQL protocol and syntax, and supports automatic sharding, online smooth scaling, auto scaling, and transparent read/write splitting. This topic describes how to synchronize data between PolarDB-X instances by using Data Transmission Service (DTS). Prerequisites The tables to be synchronized contain primary keys. Limits Warning For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X instance, see Limits and usage notes for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |
|   | The storage type of the PolarDB-X instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. You must create databases and tables in the destination instance based on the schemas of the objects to be synchronized in the source instance. This is because |

| Data Transmission Serv | ice User Guide·Data synchronizatio |
|---|---|
| Category | DTS does not support initial schema synchronization between PolarDB-X instances. Description Before you synchronize data, evaluate the impact of data synchronization on the |
| Other limits | performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, synchronization latency and stability issues may occur when you synchronize data from the source PolarDB-X instance to the destination instance. We recommend that you use the following solution to configure data synchronization tasks. For more information about the benefits of this solution, see Solutions of data synchronization from a PolarDB-X instance. You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Not e Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X instance and you want to synchronize data from the PolarDB-X instance to an AnalyticDB for MySQL instance, we recommend that you configure three data synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance B, and you want to synchronize data between the two PolarDB-X instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to source PolarDB-X Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. We recommend that you do not change the network type of the PolarDB-X instances during data synchronization. |

| Category | De | scription Not e If you change the network type of a PolarDB-X instance during |   |
|---|---|---|---|
|   | data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. During data synchronization, do not upgrade or downgrade the PolarDB-X instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. We recommend that you do not use tools such as gh-ost or pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. | data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. |   |

Supported synchronization topologies DTS supports the following synchronization topologies: one-way one-to-one synchronization, oneway one-to-many synchronization, one-way cascade synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized INSERT, UPDATE, and DELETE Before you begin Create databases and tables in the destination PolarDB-X instance based on the schemas of the objects in the source PolarDB-X instance. This is because DTS does not support init ial schema synchronizat ion between PolarDB-X instances. During init ial schema synchronizat ion, DTS synchronizes the schemas of the objects to be synchronized from the source database to the destination database. Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type and Destination Instance Type parameters to DRDS, and set the Synchronization Mode parameter to One-Way Synchronizat ion.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Instance Details | Instance Type | The value of this parameter is fixed to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region in which the source instance resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | The ID of the source PolarDB-X instance. |
| Destination Instance Details | Instance Type | The value of this parameter is fixed to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region in which the source instance resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Version | The version of the destination PolarDB-X instance. |
|   | DRDS Instance ID | The ID of the destination PolarDB-X instance. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|
| Select the objects to be synchronized | Select one or more tables from the Available section and click the icon to add the tables to the Select ed section. Not e You can select only tables as the objects to be synchronized. By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |

| Parameter or setting | Description |
|---|---|
| Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
| Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

6. Click Next .
7. Specify whether to perform initial full data synchronization.
During init ial f ull dat a synchronizat ion, DTS synchronizes the historical data of the objects to be synchronized from the source database to the destination database. If you do not select Initial Full Data Synchronization, DTS does not synchronize the historical data.
8. In the lower-right corner of the page, click Precheck.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from a PolarDB-X

instance to an AnalyticDB for MySQL cluster This topic describes how to synchronize data from a PolarDB-X instance to an AnalyticDB for MySQL cluster by using Data Transmission Service (DTS). Limits Warning For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X instance, see Limits and usage notes for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. Limits on operations to be performed on the source database: The storage type of the PolarDB-X instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. We recommend that you do not change the network type of the PolarDB-X instance during data synchronization. Not e If you change the network type of a PolarDB-X instance during data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. When the data synchronization task is running, do not upgrade or downgrade the PolarDB-X instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. |
|   | If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, synchronization latency and stability issues may occur when you |

| User Guide·Data synch | ronization Data Transmission Servic |
|---|---|
| Category | synchronize data from the source PolarDB-X instance to the destination instance. Description We recommend that you use the following solution to configure data |
| Other limits | synchronization tasks. For more information about the benefits of this solution, see Solutions of data synchronization from a PolarDB-X instance. You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Not e Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X instance and you want to synchronize data from the PolarDB-X instance to an AnalyticDB for MySQL instance, we recommend that you configure three data synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance B, and you want to synchronize data between the two PolarDB-X instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to source PolarDB-X Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. Prefix indexes cannot be synchronized. If the source database contains prefix indexes, data may fail to be synchronized. Due to the limits of AnalyticDB for MySQL, if the disk space usage of nodes in an AnalyticDB for MySQL cluster exceeds 80%, the data synchronization task is delayed and an error is returned. We recommend that you estimate the required disk space based on the objects to be synchronized. You must make sure that the destination cluster has sufficient storage space. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination |

| Category | database is larger than that of the source database. Description We recommend that you do not use tools such as gh-ost or pt-online-schema- |
|---|---|
|   | change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |

Supported synchronization topologies DTS supports the following synchronization topologies: one-way one-to-one synchronization, oneway one-to-many synchronization, and one-way many-to-one synchronization. For more information, see Synchronization topologies. SQL operations that can be synchronized INSERT, UPDATE, and DELETE Data type mappings The data types of ApsaraDB RDS for MySQL and AnalyticDB for MySQL do not have one-to-one correspondence. During initial schema synchronization, DTS converts the data types of the source database into those of the destination database. The following table describes the data types that DTS can convert.

| Dat a t ype of ApsaraDB RDS f or MySQL | Dat a t ype of Analyt icDB f or MySQL V3.0 |
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

| MULTIPOINT | VARBINARY |
|---|---|
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

Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type parameter to DRDS, the Destination Instance Type parameter to Analyt icDB, and the Synchronization Mode parameter to One-Way Synchronizat ion.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Instance Type | The access method of the source database. The value of this parameter is fixed to DRDS Inst ance and cannot be changed. |

| r Guide·Data sync | hronization | Data Transmission Servic |
|---|---|---|
| Section | Parameter | Description |
| Source Instance Details | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | The ID of the source PolarDB-X instance. |
| Destination Instance Details | Instance Type | The access method of the destination database. The value of this parameter is fixed to Analyt icDB and cannot be changed. |
|   | Instance Region | The region in which the destination instance resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Version | The version of the destination AnalyticDB for MySQL cluster. Select 3.0. |
|   | Database | The ID of the destination AnalyticDB for MySQL cluster. |
|   | Database Account | The database account of the destination AnalyticDB for MySQL cluster. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the synchronization policy and the objects to be synchronized.

| Section | Parameter or setting | Description |
|---|---|---|
|   | Initial Synchronization | You must select both Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion by default. After the precheck is complete, DTS synchronizes the schemas and data of the objects to be synchronized from the source database to the destination database. The schemas and data are the basis for subsequent incremental data synchronization. |

| Section | Parameter or setting | Description |
|---|---|---|
|   | Processing Mode in Existed Target Table | Pre-check and Int ercept : checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schema, DTS does not synchronize the data records that have the same primary keys as the data records in the destination database during initial full data synchronization. However, DTS synchronizes these data records during incremental data synchronization. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Set the synchronizat ion policy |   |   |
|   | Merge Multi Tables | Specifies whether to merge multiple tables. If you select Yes, DTS adds the dts data source column to __ _ _ each table to store data sources. In this case, DDL operations cannot be synchronized. If you select No, DDL operations can be synchronized. By default, No is selected. Not e If you set this parameter to Yes, all the selected source tables in the task are merged into a destination table. If you want to merge only specific source tables, you can create two data synchronization tasks. |
|   | Synchronization Type | The types of operations that you want to synchronize. Valid values: Insert Updat e Delet e |

| Section | Parameter or setting | Description |
|---|---|---|
| Select the objects to be synchronize d | N/A | Select one or more tables to be synchronized from the Available section and click the icon to add the tables to the Select ed section. Not e You can select only tables as the objects to be synchronized. You can use the object name mapping feature to rename the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |
| Rename Databases and Tables | N/A | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
| Retry Time for Failed Connection | N/A | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

6. Click Next .
7. Specify a type for the tables that you want to synchronize to the destination database.
After you select Init ial Schema Synchronizat ion, you must specify the t ype, primary key column, and part it ion key column for the tables that you want to synchronize to the AnalyticDB for MySQL cluster.
8. In the lower-right corner of the page, click Precheck.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from a PolarDB-X

instance to a DataHub project This topic describes how to synchronize data from a PolarDB-X instance to a DataHub project by using Data Transmission Service (DTS). After you synchronize data, you can use big data services such as Realtime Compute to analyze data in real time. Prerequisites A DataHub project is created to receive the synchronized data. Limits Warning For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X instance, see Limits and usage notes for synchronizing data between PolarDB-X instances.

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to _ row. The binlog row image parameter is set to full. Otherwise, error messages _ _ are returned during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. Limits on operations to be performed on the source database: The storage type of the PolarDB-X instance must be ApsaraDB RDS for MySQL (private custom RDS instance). PolarDB for MySQL cannot be used as the storage type. We recommend that you do not change the network type of the PolarDB-X instances during data synchronization. Not e If you change the network type of a PolarDB-X instance during data synchronization, you must submit a ticket to make the network modification take effect for the data synchronization instance. During data synchronization, do not upgrade or downgrade the PolarDB-X instance, migrate frequently accessed tables, change shard keys, or perform DDL operations on source objects. Otherwise, the data synchronization task fails. |
|   | If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, synchronization latency and stability issues may occur when you synchronize data from the source PolarDB-X instance to the destination instance. We recommend that you use the following solution to configure data synchronization tasks. For more information about the benefits of this solution, see |

| Data Transmission Serv | ice User Guide·Data synchronizatio |
|---|---|
| Category | Solutions of data synchronization from a PolarDB-X instance. Description You can configure a data synchronization task for each ApsaraDB RDS for MySQL |
| Other limits | instance that is attached to the source PolarDB-X instance. When you configure the data synchronization tasks, you must map the names of the databases and tables in the ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance to the names of the databases and tables in the destination instance. This way, many-to-one synchronization is implemented. Not e Example 1: If three ApsaraDB RDS for MySQL instances are attached to a PolarDB-X instance and you want to synchronize data from the PolarDB-X instance to an AnalyticDB for MySQL instance, we recommend that you configure three data synchronization tasks to synchronize data from each ApsaraDB RDS for MySQL instance to the destination AnalyticDB for MySQL instance. During the task configuration, you must map the names of the databases and tables in the three ApsaraDB RDS for MySQL instances to the names of databases and tables in the AnalyticDB for MySQL instances to implement many-to-one synchronization. Example 2: If three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance A, three ApsaraDB RDS for MySQL instances are attached to PolarDB-X Instance B, and you want to synchronize data between the two PolarDB-X instances, we recommend that you configure three data synchronization tasks to synchronize data from each source ApsaraDB RDS for MySQL instance to each destination ApsaraDB RDS for MySQL instance. During the task configuration, you must map the names of databases and tables in the source ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination ApsaraDB RDS for MySQL instances. If N ApsaraDB RDS for MySQL instances are attached to source PolarDB-X Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X Instance A to a destination instance. We recommend that you estimate the number of data synchronization tasks in advance and purchase enough expansion plans. Only tables can be selected as the objects to be synchronized. Initial full data synchronization is not supported. DTS does not synchronize historical data of the objects to be synchronized from the source PolarDB-X instance to the destination DataHub project. DTS does not synchronize DDL operations. If you perform a DDL operation on the source PolarDB-X instance during data synchronization, data fails to be synchronized. To solve this issue, you must modify the related topic in the destination DataHub project and then restart the data synchronization task. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. |
| Document Version: 2 | 0230625 22 |

| Category | We recommend that you do not use tools such as gh-ost or pt-online-schema- Description change to perform DDL operations on source tables during data synchronization. |
|---|---|
|   | Otherwise, data synchronization may fail. |

SQL operations that can be synchronized INSERT, UPDATE, and DELETE Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type parameter to DRDS, the Destination Instance Type parameter to Dat ahub, and the Synchronization Mode parameter to One-Way Synchronizat ion.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronizatio n Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Instance Details | Instance Type | The type of the source database. The value of this parameter is fixed to DRDS Inst ance and cannot be changed. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | The ID of the source PolarDB-X instance. |
| Destination Instance Details | Instance Type | The type of the destination database. This parameter is fixed to Dat aHub and cannot be changed. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the DataHub project to which data is synchronized. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the synchronization policy and the objects to be synchronized.

| Parameter or setting | Description |
|---|---|
| Initial Synchronization | Select Init ial Schema Synchronizat ion. Not e After you select Init ial Schema Synchronizat ion, DTS synchronizes the schemas of the objects such as tables to the destination DataHub project. |
| Select the objects to be synchronized | Select one or more objects from the Available section and click the icon to add the objects to the Select ed section. Not e You can select only tables as the objects to be synchronized. You can use the object name mapping feature to rename the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |
| Rename Databases and Tables | Specifies whether to rename the databases and tables in batches based on your business requirements. For more information, see Specify the name of an object in the destination instance. Import ant If the object that you last select to synchronize is a database, the Change Dat abase and T able Names option is unavailable and you cannot use the object name mapping feature for tables or columns. |
| Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 12 hours. You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |
| Whether to enable new additional column rules | After DTS synchronizes data to DataHub, DTS adds additional columns to the destination table. If the names of additional columns are the same as the names of existing columns in the destination table, data synchronization fails. Select Yes or No to specify whether to enable new naming rules for additional columns. Warning Before you specify this parameter, check whether additional columns have the same names as the existing columns in the destination table. |

6. In the lower-right corner of the page, click Precheck.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
7. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.

#### Synchronize data from a self-managed Db2

for LUW database to an AnalyticDB for PostgreSQL instance This topic describes how to synchronize data from a self-managed Db2 for LUW database to an AnalyticDB for PostgreSQL instance by using Data Transmission Service (DTS). The data synchronization feature provided by DTS allows you to transfer and analyze data with ease. Prerequisites The source self-managed Db2 for LUW database and the destination AnalyticDB for PostgreSQL instance are created. The available storage space of the AnalyticDB for PostgreSQL instance is larger than the total size of the data in the self-managed Db2 for LUW database. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The server on which the source database is deployed must have a sufficient outbound bandwidth. Otherwise, the data synchronization speed decreases. The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you want to edit the tables in the destination database, such as renaming tables or columns, you can synchronize up to 1,000 tables in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. The following requirements for data logs must be met: The data logging feature is enabled. Otherwise, error messages are returned during precheck and the data synchronization task cannot be started. If you perform only incremental data synchronization, the data logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the data logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the data logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of data logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. |
| Other limits | Schema synchronization is not supported. Before you configure a data synchronization task, you must create databases and tables in the destination instance based on the databases and tables that you want to synchronize. DTS synchronizes incremental updates from a self-managed Db2 for LUW database to the destination database based on the Change Data Capture (CDC) replication technology of Db2 for LUW. However, the CDC replication technology has its own limits. For more information, see General data restrictions for SQL Replication. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost and pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

| Category | Description |
|---|---|
| Special cases | The source database is a self-managed Db2 for LUW database. Therefore, you must take note of the following items: If you perform a primary/secondary switchover on the source database when the data synchronization task is running, the task fails. DTS calculates synchronization latency based on the timestamp of the latest synchronized data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the synchronization latency may be inaccurate. If the latency of the data synchronization task is excessively high, you can perform a DML operation on the source database to update the latency. Not e If you select an entire database as the object to be synchronized, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

SQL operations that can be synchronized DML operations: INSERT, UPDATE, and DELETE Before you begin Create database accounts and grant permissions to the accounts. Self-managed Db2 for LUW database: the database administrator permissions (DBADM authority). AnalyticDB for PostgreSQL instance: read and write permissions on the destination database. Enable the archive logging feature for the self-managed Db2 for LUW database. Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, set the Source Instance Type parameter to DB2, the Destination Instance Type parameter to Analyt icDB f or Post greSQL, and the Synchronization Mode parameter to One-Way Synchronizat ion.
2. On the Synchronization Tasks page, find the data synchronization instance that you created and click
Conf igure T ask in the Act ions column.
3. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | Synchronization Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
|   | Instance Type | The access method of the source database. In this example, User-Creat ed Dat abase wit h Public IP Address is selected. |

| a Transmission Servic | e | User Guide·Data synchronizatio |
|---|---|---|
| Section | Parameter | Description |
| Source Instance Details | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Database Type | The type of the source database. The value of this parameter is fixed to DB2. |
|   | Hostname or IP Address | The endpoint of the self-managed Db2 for LUW database. |
|   | Port Number | The service port number of the self-managed Db2 for LUW database. |
|   | DB2 Edition | The version of the self-managed Db2 for LUW database. Select DB2 f or LUW. |
|   | Database Name | The name of the source database. |
|   | Database Account | The account of the self-managed Db2 for LUW database. The account must have the superuser permissions. |
|   | Database Password | The password of the database account. |
| Destination Instance Details | Instance Type | The access method of the destination database. The value of this parameter is fixed to Analyt icDB f or Post greSQL. You do not need to specify this parameter. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Instance ID | The ID of the destination AnalyticDB for PostgreSQL instance. |
|   | Database Name | The name of the destination database. |
|   | Database Account | The initial database account of the AnalyticDB for PostgreSQL instance or the database account that has the RDS SUPERUSER _ permission. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. If an IP address whitelist is configured for the self-managed Db2 for LUW database, you must
manually add the CIDR blocks of DTS servers to the IP address whitelist of the database. To obtain the CIDR blocks of DTS servers, click Copy in the dialog box that appears. After you add the CIDR blocks of DTS servers to the IP address whitelist of the database, click Next . If you do not need to configure an IP address whitelist for the self-managed Db2 for LUW database, ignore the preceding settings and click Next .
6. Configure the synchronization policy and the objects to be synchronized.

| Section | Parameter or setting | Description |
|---|---|---|
| Set the synchronization policy | Initial Synchronization | Select Init ial Schema Synchronizat ion and Init ial Full Dat a Synchronizat ion. After the precheck, DTS synchronizes historical data of the objects to be synchronized from the source database to the destination instance. The data is the basis for subsequent incremental synchronization. |
|   | Processing Mode in Existed Target Table | Pre-check and int ercept Checks the Schema Name Conf lict item and generates an error message if the destination table contains data. By default, this mode is selected. Clear T arget T able Clear data of the destination table during the precheck. Ignore Skips the check for empty destination tables during the precheck and adds data to the existing data during initial full data synchronization. If you want to synchronize data from multiple tables to one table, you can select this mode. |
|   | Synchronization Type | The type of operations that you want to synchronize. Valid values: Insert Updat e Delet e Not e Select the types of operations that you want to synchronize based on your business requirements. |
| Select the objects to be synchronized | Select the objects to be synchronized | You can select only tables as the objects to be synchronized. You can use the object name mapping feature to rename the columns that are synchronized to the destination database. For more information, see Specify the name of an object in the destination instance. |
|   | Rename Databases and Tables | You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |
| 3 | > Document Version: 2023062 |   |

|   | e | User Guide·Data synchronizatio |
|---|---|---|
| Section | Parameter or setting | Description |
| Others | Retry Time for Failed Connection | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 720 minutes (12 hours). You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |

7. In the lower-right corner of the page, click Next .
8. Configure the primary key column and dist ribut ion column of the schema and click Precheck in
the lower-right corner of the page. Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. Troubleshoot the issues based on the causes and run a precheck again.
9. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial full data synchronization. If the task is running and a data record is written to the source table, the data record is automatically synchronized to the destination table.

#### Synchronize data from a self-managed

Oracle database to a DataHub project DataHub is a real-time data distribution platform that is designed to process streaming data. You can publish and subscribe to streaming data in DataHub and distribute the data to other platforms. DataHub allows you to analyze and use streaming data with ease. This topic describes how to synchronize data from a self-managed Oracle database to a DataHub project by using Data Transmission Service (DTS). After you synchronize data, you can use big data services such as Realtime Compute for Apache Flink to analyze the data in real time. Prerequisites The engine version of the self-managed Oracle database is 9i, 10g, 11g, 12c, 18c, or 19c. The self-managed Oracle database is running in ARCHIVELOG mode. Archived log files are accessible, and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The destination DataHub project is created. For more information, see Create a project in DataHub Us er Guide. Limits

| Category | Description |
|---|---|
| Limits on the source database | Requirements for the objects to be synchronized: The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If the version of your Oracle database is 12c or later, the names of the tables to be synchronized cannot exceed 30 bytes in length. If you select tables as the objects to be synchronized and you want to edit the tables in the destination database, such as renaming tables or columns, you can synchronize up to 1,000 tables in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. If the self-managed Oracle database is an Oracle Real Application Cluster (RAC) database, you can use only a single virtual IP address (VIP) rather than a Single Client Access Name (SCAN) IP address when you configure the data synchronization task. After you specify the VIP, node failover of the Oracle RAC database is not supported. The following requirements must be met: The redo logging and archive logging features must be enabled. If you perform only incremental data synchronization, the redo logs and archive logs of the source database must be stored for more than 24 hours. If you perform both schema synchronization and incremental data synchronization, the redo logs and archive logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the redo logs and archive logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the schema synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of redo logs and archive logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. If you perform a primary/secondary switchover on the source database when the data synchronization task is running, the task fails. |

| Category | Description |
|---|---|
| Other limits | You can configure a data synchronization task for this scenario only in the DTS console of the new version. The objects of initial schema synchronization must be tables. Warning In this scenario, DTS does not support triggers. We recommend that you delete the triggers of the source database to prevent data inconsistency caused by the triggers. Full data synchronization is not supported. DTS does not synchronize historical data of the required objects from the source database to the destination DataHub project. Only tables can be selected as the objects to be synchronized. We recommend that you do not use tools such as gh-ost and pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. DTS calculates synchronization latency based on the timestamp of the latest synchronized data in the destination database and the current timestamp in the source database. If no DML operation is performed on the source database for an extended period of time, the synchronization latency may be inaccurate. If the latency of the data synchronization task is excessively high, you can perform a DML operation on the source database to update the latency. Not e If you select an entire database as the object to be synchronized, you can create a heartbeat table. The heartbeat table is updated or receives data every second. |

Supported synchronization topologies One-way one-to-one synchronization One-way one-to-many synchronization One-way many-to-one synchronization SQL operations that can be synchronized INSERT, UPDATE, and DELETE Permissions required for database accounts

| Database | Required permissions | References |
|---|---|---|

| Database | Required permissions | References |
|---|---|---|
| Self-managed Oracle database | Permissions of database administrator (DBA) | CREATE USER and GRANT Import ant If you need to synchronize data from an Oracle database but the DBA permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account. |

Enable logging and grant fine-grained permissions to an Oracle database account Import ant If you need to synchronize data from an Oracle database but the DBA permissions cannot be granted to the database account, you can enable archive logging and supplemental logging, and grant fine-grained permissions to the account.
1. Enable archive logging and supplemental logging.

| Log type | Procedure |
|---|---|
| Archive logging | Execute the following statements to enable archive logging: shutdown immediate; startup mount; alter database archivelog; alter database open; archive log list; |

| Log type | Procedure |
|---|---|
| Supplemental logging | Enable supplemental logging at the database or table level based on your business requirements: Not e You can enable database-level supplemental logging to ensure the stability of DTS tasks. You can enable table-level supplemental logging to reduce the disk usage of the source Oracle database. Enable database-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Execute the following statement to enable primary key and unique key supplemental logging at the database level: alter database add supplemental log data (primary key,unique index) columns; Enable table-level supplemental logging a. Execute the following statement to enable minimal supplemental logging: alter database add supplemental log data; b. Enable table-level supplemental logging by using one of the following methods: Execute the following statement to enable primary key supplemental logging at the table level: alter table table name add supplemental log data (primary _ key) columns; Execute the following statement to enable table-level supplemental logging for all columns: alter table tb name add supplemental log data (all) columns ; _ |

2. Grant fine-grained permissions to an Oracle database account.
Oracle 9i to 11g

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the accoun
```

`t.`

```
create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; -- system tables grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct;
```

Oracle 12c to 19c (tenant mode)

```bash
# Switch to the pluggable database (PDB). Create a database account, such as rdsdt_dtsa
cct, and grant permissions to the account. ALTER SESSION SET container = ORCLPDB1; create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct;
```

|   | grant select any table to rdsdt dtsacct; _ grant select any transaction to rdsdt dtsacct; _ -- v$log privileges grant select on v $log to rdsdt dtsacct; _ _ -- v$logfile privileges grant select on v $logfile to rdsdt dtsacct; _ _ -- v$archived log privileges _ grant select on v $archived log to rdsdt dtsacct; _ _ _ -- v$parameter privileges grant select on v $parameter to rdsdt dtsacct; _ _ -- v$database privileges grant select on v $database to rdsdt dtsacct; _ _ -- v$active instances privileges _ grant select on v $active instances to rdsdt dtsacct; _ _ _ -- v$instance privileges grant select on v $instance to rdsdt dtsacct; _ _ -- v$logmnr contents privileges _ grant select on v $logmnr contents to rdsdt dtsacct; _ _ _ grant select on sys.USER$ to rdsdt dtsacct; _ grant select on SYS.OBJ$ to rdsdt dtsacct; _ grant select on SYS.COL$ to rdsdt dtsacct; _ grant select on SYS.IND$ to rdsdt dtsacct; _ grant select on SYS.ICOL$ to rdsdt dtsacct; _ grant select on SYS.CDEF$ to rdsdt dtsacct; _ grant select on SYS.CCOL$ to rdsdt dtsacct; _ grant select on SYS.TABPART$ to rdsdt dtsacct; _ grant select on SYS.TABSUBPART$ to rdsdt dtsacct; _ grant select on SYS.TABCOMPART$ to rdsdt dtsacct; _ -- V$PDBS privileges grant select on V $PDBS to rdsdt dtsacct; _ _ # Switch to the container database (CDB). Create a database account and grant permissio ns to the account by using one of the following methods: ALTER SESSION SET container = CDB$ROOT; # Method 1: Create a global account that starts with C##, such as C##rdsdt dtsacct, and _ grant permissions to the account. If you use this method, you must contact the O&M engi neers of DTS. create user C##rdsdt dtsacct IDENTIFIED BY rdsdt dtsacct; _ _ grant create session to C##rdsdt dtsacct; _ grant connect to C##rdsdt dtsacct; _ grant resource to C##rdsdt dtsacct; _ grant select on v $logmnr contents to C##rdsdt dtsacct; _ _ _ grant LOGMINING to C##rdsdt dtsacct; _ grant EXECUTE CATALOG ROLE to C##rdsdt dtsacct; _ _ _ grant execute on sys.dbms logmnr to C##rdsdt dtsacct; _ _ # Method 2: Create a database account, such as rdsdt dtsacct, and grant permissions to _ the account. If you use this method, you must modify the default parameters of the Orac le database. alter session set " ORACLE SCRIPT"=true; _ _ create user rdsdt dtsacct IDENTIFIED BY rdsdt dtsacct; _ _ grant create session to rdsdt dtsacct; _ grant connect to rdsdt dtsacct; _ grant select on v $logmnr contents to rdsdt dtsacct; _ _ _ grant LOGMINING TO rdsdt dtsacct; _ grant EXECUTE CATALOG ROLE to rdsdt dtsacct; _ _ _ grant execute on sys dbms logmnr to rdsdt dtsacct; |   |
|---|---|---|

```
grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

Oracle 12c to 19c (non-tenant mode)

```bash
# Create a database account, such as rdsdt_dtsacct, and grant permissions to the accoun
```

`t.`

```
create user rdsdt_dtsacct IDENTIFIED BY rdsdt_dtsacct; grant create session to rdsdt_dtsacct; grant connect to rdsdt_dtsacct; grant resource to rdsdt_dtsacct; grant select on V_$LOGMNR_LOGS to rdsdt_dtsacct; grant select on all_objects to rdsdt_dtsacct; grant select on all_tab_cols to rdsdt_dtsacct; grant select on dba_registry to rdsdt_dtsacct; grant select any table to rdsdt_dtsacct; grant select any transaction to rdsdt_dtsacct; -- v$log privileges grant select on v_$log to rdsdt_dtsacct; -- v$logfile privileges grant select on v_$logfile to rdsdt_dtsacct; -- v$archived_log privileges grant select on v_$archived_log to rdsdt_dtsacct; -- v$parameter privileges grant select on v_$parameter to rdsdt_dtsacct; -- v$database privileges grant select on v_$database to rdsdt_dtsacct; -- v$active_instances privileges grant select on v_$active_instances to rdsdt_dtsacct; -- v$instance privileges grant select on v_$instance to rdsdt_dtsacct; -- v$logmnr_contents privileges grant select on v_$logmnr_contents to rdsdt_dtsacct; grant select on sys.USER$ to rdsdt_dtsacct; grant select on SYS.OBJ$ to rdsdt_dtsacct; grant select on SYS.COL$ to rdsdt_dtsacct; grant select on SYS.IND$ to rdsdt_dtsacct; grant select on SYS.ICOL$ to rdsdt_dtsacct; grant select on SYS.CDEF$ to rdsdt_dtsacct; grant select on SYS.CCOL$ to rdsdt_dtsacct; grant select on SYS.TABPART$ to rdsdt_dtsacct; grant select on SYS.TABSUBPART$ to rdsdt_dtsacct; grant select on SYS.TABCOMPART$ to rdsdt_dtsacct; grant LOGMINING TO rdsdt_dtsacct; grant EXECUTE_CATALOG_ROLE to rdsdt_dtsacct; grant execute on sys.dbms_logmnr to rdsdt_dtsacct;
```

To create a global account that starts with C## for a multitenant CDB$ROOT in Oracle 12c to 19c (tenant mode), you must contact the O&M engineers to modify some parameters. Procedure
1. Create a data synchronization instance.
When you create the data synchronization instance, select Oracle as the source instance type, Dat aHub as the destination instance type, and One-way Synchronizat ion as the synchronization topology.
2. Find the data synchronization instance that you created and click Conf igure T ask in the Actions
column.
3. Configure the source and destination instances.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. Select User-Creat ed Dat abase wit h Public IP Address. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Database Type | The value of this parameter is fixed to Oracle. |
|   | Hostname or IP Address | The endpoint or IP address that is used to connect to the self- managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. Default value: 1521. |
|   | Instance Type | Non-RAC Inst ance: If you select this value, you must specify the SID parameter. RAC or PDB Inst ance: You cannot select this option because RAC instances are not supported. |
|   | Database Account | The account of the self-managed Oracle database. |
|   | Database Password | The password of the database account. |
| Destination Database | Instance Type | The value of this parameter is fixed to Dat aHub. |
|   | Instance Region | The region in which the destination database resides. The region is the destination region that you selected when you created the data synchronization instance. You cannot change the value of this parameter. |
|   | Project | The name of the DataHub project . |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Configure the synchronization policy and the objects to be synchronized.

| Setting | Description |
|---|---|
| Select the initial synchronization types | Select Init ial Schema Synchronizat ion. Not e After you select Init ial Schema Synchronizat ion, DTS synchronizes the schemas of the objects such as tables to the destination DataHub project. |
| Select the objects to be synchronized | Select one or more objects from the Source Object s section and click the icon to move the objects to the Select ed Object s section. Not e You can select only tables as the objects to be synchronized. By default, after an object is synchronized to the destination database, the name of the object remains unchanged. You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |
| Specify whether to rename objects | You can use the object name mapping feature to rename the objects that are synchronized to the destination instance. For more information, see Specify the name of an object in the destination instance. |
| Specify the retry time for a failed connection to the source instance or destination instance | By default, if DTS fails to connect to the source or destination database, DTS retries within the next 720 minutes (12 hours). You can specify the retry time range based on your business requirements. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. |
| Whether to enable the new naming rules for additional columns | After DTS synchronizes data to DataHub, DTS adds additional columns to the destination topic. If the names of additional columns are the same as the names of existing columns in the destination topic, data synchronization fails. Select Yes or No to specify whether you want to enable new naming rules for additional columns. Warning Before you set this parameter, check whether additional columns and existing columns in the destination topic have name conflicts. |

6. In the lower-right corner of the page, click Next : Precheck and St art T ask.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
7. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
Then, DTS performs initial synchronization.
8. Wait until the initial synchronization is complete and the data synchronization task enters the
Synchronizing state. You can view the status of the data synchronization task on the Dat a Synchronizat ion page. Schema of a DataHub topic When DTS synchronizes incremental data to a DataHub topic, DTS adds additional columns to store metadata. The following figure shows the schema of a DataHub topic. In this example, `id` , `name` , and `address` are data fields. DTS adds the `dts_` prefix to data fields because the naming rules of the previous version for additional columns are used. The following table describes the additional columns in the DataHub topic.

| Previous additional column name | New additional column name | Data type | Description |
|---|---|---|---|

|   |   | Previous additional column name |   |   |   |   |   |   |   | New additional column name |   |   |   |   |   | Data type | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | dts record _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | The unique ID of the incremental log entry. Not e By default, the ID auto- increments for each new log entry. In disaster recovery scenarios, rollback may occur, and the ID may not auto-increment. Therefore, some IDs may be duplicated. If an UPDATE operation is performed, DTS generates two incremental log entries to record the pre-update and post-update values. The values of the dts record _ _ id field in the two incremental log entries are the same. |
|   |   |   | dts record _ |   |   |   |   |   |   |   | new dts sync dts rec _ _ _ _ |   |   |   |   | Strin |   |
|   |   | id _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ord id _ |   |   |   |   |   |   |   |
|   |   | dts operat _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | The operation type. Valid values: I: an INSERT operation D: a DELETE operation U: an UPDATE operation |
|   |   |   | dts operat _ |   |   |   |   |   |   |   | new _ |   |   |   | dts sync dts ope _ _ _ | String |   |
|   |   | ion flag _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ration flag _ |   |   |   |   |   |   |   |
|   |   | dts instan _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | The server ID of the database. The value is null . The actual value is not displayed. This ensures database security. |
|   |   |   | dts instan _ |   |   |   |   |   |   |   | n |   | ew dts sync dts ins _ _ _ _ |   |   | String |   |
|   |   | ce id _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | tance id _ |   |   |   |   |   |   |   |
|   |   | dts db nam _ _ |   |   |   |   |   |   |   | new dts sync dts db _ _ _ _ _ name |   |   |   |   |   | String | The name of the database. |
|   |   |   | dts db nam _ _ |   |   |   |   |   |   |   | new dts sync dts db _ _ _ _ _ |   |   |   |   | St |   |
|   |   | e |   |   |   |   |   |   |   | name |   |   |   |   |   |   |   |
|   |   | dts table _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | The name of the table in the database. |
|   |   |   | dts table _ _ |   |   |   |   |   |   |   |   | new dts sync dts tab _ _ _ _ |   |   |   | String |   |
|   |   | name |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | le name _ |   |   |   |   |   |   |   |
|   |   | dts utc ti _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | The operation timestamp, in UTC. It is also the timestamp of the redo log file. |
|   |   |   | dts utc ti _ _ |   |   |   |   |   |   |   | new |   |   | dts sync dts utc _ _ _ _ |   | String |   |
|   |   | mestamp |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | timestamp _ |   |   |   |   |   |   |   |
|   |   | dts before _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | Indicates whether the column values are pre-update values. Valid values: Y and N. |
|   |   |   | dts before _ |   |   |   |   |   |   |   | n |   | ew dts sync dts bef _ _ _ _ |   |   | String |   |
|   |   | flag _ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ore flag _ |   |   |   |   |   |   |   |
|   |   | dts after _ _ |   |   |   |   |   |   |   |   |   |   |   |   |   | String | Indicates whether the column values are post-update values. Valid values: Y and N. |
|   |   |   | dts after _ _ |   |   |   |   |   |   |   |   | new dts sync dts aft _ _ _ _ |   |   |   | String |   |
|   |   | flag |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | er flag _ |   |   |   |   |   |   |   |

| dts record _ _ |   |
|---|---|

|   |   | id |
|---|---|---|

Additional information about the dts_before_flag and dts_after_flag fields The values of the `dts_before_flag` and `dts_after_flag` fields in an incremental log entry vary with different operation types: INSERT operation For an INSERT operation, the column values are the newly inserted record values (post-update values). The value of the `dts_before_flag` field is N, and the value of the `dts_after_flag` field is Y. UPDATE operation DTS generates two incremental log entries for an UPDATE operation. The two incremental log entries have the same values for the `dts_record_id` , `dts_operation_flag` , and `dts_utc_timestamp` fields. The first log entry records the pre-update values. Therefore, the value of the `dts_before_flag` field is Y, and the value of the `dts_after_flag` field is N. The second log entry records the postupdate values. Therefore, the value of the `dts_before_flag` field is N, and the value of the `dts_` `after_flag` field is Y. DELETE operation For a DELETE operation, the column values are the deleted record values (pre-update values). The value of the `dts_before_flag` field is Y, and the value of the `dts_after_flag` field is N.

#### Synchronize data between ApsaraDB for

Redis instances You can use Data Transmission Service (DTS) to perform one-way or two-way data synchronization between ApsaraDB for Redis instances. This feature is applicable to scenarios such as resource migration or resource merging and business architecture adjustment. Prerequisites If the source ApsaraDB for Redis instance is a Community Edition instance, the engine version is 4.0 or 5.0. If the source ApsaraDB for Redis instance is an Enhanced Edition (Tair) instance, the engine version is 5.0. The engine version of the destination ApsaraDB for Redis instance can be 4.0 or 5.0. The engine version of the destination ApsaraDB for Redis instance must be the same as or later than that of the source ApsaraDB for Redis instance. Before you synchronize data between two ApsaraDB for Redis instances that use different engine versions, check the compatibility of the two versions. The source ApsaraDB for Redis instance is deployed in a virtual private cloud (VPC). SSL encryption is disabled for the source ApsaraDB for Redis instance. The available storage space of the destination ApsaraDB for Redis instance is larger than the total size of the data in the source ApsaraDB for Redis instance. ApsaraDB for Redis Enhanced Edition (Tair) is integrated with more Redis modules than ApsaraDB for Redis Community Edition. To ensure compatibility between the source and destination instances, if the source instance is an Enhanced Edition (Tair) instance, the destination instance must be an Enhanced Edition (Tair) instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The collections to synchronize must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. To ensure the synchronization quality, DTS adds the following key to the source database: DTS REDIS TIMESTAMP HEARTBEAT. This key is used to record the time _ _ _ when data is synchronized to the destination database. To ensure the stability of data synchronization, we recommend that you increase the value of the repl-backlog-size parameter in the redis.conf file. The following requirements for append-only file (AOF) logging must be met: The AOF logging feature must be enabled. If you perform only incremental data synchronization, the AOF logs of the source database must be stored for more than 24 hours. If you perform both full data synchronization and incremental data synchronization, the AOF logs of the source database must be stored for at least seven days. Otherwise, DTS may fail to obtain the AOF logs, and your data synchronization task may fail. In exceptional circumstances, data inconsistency or loss may occur. After the full data synchronization is complete, you can set the retention period to more than 24 hours. Make sure that you set the retention period of AOF logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. Not e This limit is not applied to ApsaraDB for Redis instances. If an expiration policy is enabled for specific keys in the source database, these keys may not be deleted at the earliest opportunity after they expire. Therefore, the number of keys in the destination database may be less than that in the source database. You can run the INFO command to view the number of keys in the destination database. If the data eviction policy ( maxmemory-policy ) of the destination database is not set to noeviction , data inconsistency may occur between the source and destination databases. |

| Category | Description |
|---|---|
| Other limits | During data synchronization, if the number of shards in the source ApsaraDB for Redis instance is increased or decreased, or if you change the database specifications, such as scaling up the memory capacity, you must reconfigure the data synchronization task. To ensure data consistency, we recommend that you clear the data that has been synchronized to the destination database before you reconfigure the data synchronization task. During data synchronization, if the endpoint of the source ApsaraDB for Redis instance is changed, you must contact Alibaba Cloud technical support to update the change at the earliest opportunity. Otherwise, the AOF logs are reset and you must reconfigure the data synchronization task. To ensure compatibility, make sure that the version of the destination database is the same as or later than that of the source database. If the version of the destination database is earlier than that of the source database, database compatibility issues may occur. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During data synchronization, we recommend that you use only DTS to write data to the destination database. This prevents data inconsistency between the source and destination databases. For example, if you use tools other than DTS to write data to the destination database, data loss may occur in the destination database when you use Data Management (DMS) to perform online DDL operations. |

SQL operations that can be synchronized

| Edition | SQL operation |
|---|---|

| Edition | SQL operation |
|---|---|
| ApsaraDB for Redis Community Edition | APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, and PSETEX RENAME, RENAMENX, RESTORE, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE SWAPDB and UNLINK (These two commands can be synchronized only if the engine version of the source instance is Redis 4.0.) |
| ApsaraDB for Redis Enhanced Edition (Tair) | APPEND BITOP, BLPOP, BRPOP, and BRPOPLPUSH DECR, DECRBY, and DEL EVAL, EVALSHA, EXEC, EXPIRE, and EXPIREAT GEOADD and GETSET HDEL, HINCRBY, HINCRBYFLOAT, HMSET, HSET, and HSETNX INCR, INCRBY, and INCRBYFLOAT LINSERT, LPOP, LPUSH, LPUSHX, LREM, LSET, and LTRIM MOVE, MSET, MSETNX, and MULTI PERSIST, PEXPIRE, PEXPIREAT, PFADD, PFMERGE, and PSETEX RENAME, RENAMENX, RPOP, RPOPLPUSH, RPUSH, and RPUSHX SADD, SDIFFSTORE, SELECT, SET, SETBIT, SETEX, SETNX, SETRANGE, SINTERSTORE, SMOVE, SPOP, SREM, and SUNIONSTORE UNLINK, ZADD, ZINCRBY, ZINTERSTORE, ZREM, ZREMRANGEBYLEX, ZUNIONSTORE, ZREMRANGEBYRANK, and ZREMRANGEBYSCORE |

PUBLISH operations cannot be synchronized. If you run the EVAL or EVALSHA command to call Lua scripts, DTS cannot identify whether these Lua scripts are executed on the destination instance. This is because the destination instance does not explicitly return the execution results of Lua scripts during incremental data synchronization. When DTS runs the SYNC or PSYNC command to transfer data of the LIST type, DTS does not clear the existing data in the destination instance. As a result, the destination instance may contain duplicate data records. Step 1: Create a data synchronization task
1. Log on to the DMS console of the new version. For more information, see Log on to the DTS console.
2. In the top navigation bar, choose DT S > Dat a Synchronizat ion.
3. On the Data Synchronization page, click Creat e T ask.
4. In the dialog box that appears, set the required parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select Redis. |
| Source Region | The region in which the source instance resides. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select Redis. |
| Dest inat ion Region | The region in which the destination instance resides. |
| Synchronizat ion T opology | The synchronization topology of the data synchronization task. Select One- way Synchronizat ion or T wo-way Synchronizat ion based on your business requirements. Not e You can select T wo-way Synchronizat ion only when the source and destination instances reside in the same region. |
| Quant it y | The number of data synchronization instances that you want to create at a time. Default value: 0. |

5. Click Purchase Inst ance.
Step 2: Configure the source and destination databases
1. On the Dat a Synchronizat ion page, find the data synchronization task that you create and click
Conf igure T ask in the Actions column.
2. Configure the source and destination databases. The following table describes the parameters.

|   | Section | Parameter | Description |
|---|---|---|---|
|   | N/A | T ask Name | The name of the task. DTS automatically generates a task name. We recommend that you specify a descriptive name for easy identification. You do not need to specify a unique task name. |
|   | Source Dat abase | Dat abase T ype | The type of the source database. Select Redis. |
|   |   | Access Met hod | The access method of the source database. Select Alibaba Cloud Inst ance. |
|   |   | Inst ance Region | The region in which the source ApsaraDB for Redis instance resides. |
|   |   | Replicat e Dat a Across Alibaba Cloud Account s | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, No is selected. |
|   |   | Inst ance ID | The ID of the source ApsaraDB for Redis instance. |
|   |   | Dat abase Password | The database account of the source ApsaraDB for Redis instance. The account must have the read permissions on the source database. If you forget the password, you can reset the password. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. Not e This parameter is optional and can be left empty if no database password is set for the source Redis database. |
|   | Dest inat i on Dat abase | Dat abase T ype | The type of the destination database. Select Redis. |
|   |   | Access Met hod | The access method of the destination database. Select Alibaba Cloud Inst ance. |
|   |   | Inst ance Region | The region in which the destination ApsaraDB for Redis instance resides. |
|   |   | Inst ance ID | The ID of the destination ApsaraDB for Redis instance. |

|   | account username>:<Password> |
|---|---|

|   | Section | Parameter | Description |
|---|---|---|---|
|   |   | Dat abase Password | The database account of the destination ApsaraDB for Redis instance. The account must have the read and write permissions on the destination database. If you use the default account, whose username is the same as the instance ID, you can enter only the password. If you use a custom account, specify the password in the <Custom account username>:<Password> format. Example: testaccount:Test1234. |

|   | account username>:<Password> |
|---|---|

3. In the lower part of the page, click T est Connect ivit y and Proceed.
4. Select objects for the task and configure advanced settings.
Basic Set t ings

| Paramet er | Description |
|---|---|
| T ask St ages | By default, Full Dat a Synchronizat ion and Increment al Dat a Synchronizat ion are selected. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination instance. The historical data serves as the basis for subsequent incremental synchronization. Not e Full data synchronization is supported only for ApsaraDB for Redis Enhanced Edition (Tair) instances. |

| Paramet er | Description |
|---|---|
| Process ing Mode of Conf lict ing T ables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur, and your business may be exposed to potential risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |
| Select Object s | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. Not e You can select only databases as the objects to be synchronized. You cannot select keys as the objects to be synchronized. |

Advanced Set t ings

| Paramet er | Description |
|---|---|

| Paramet er | Description |
|---|---|
| Ret ry T ime f or Failed Connec t ion | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, click View Det ails next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again. After the success rate becomes 100%, the data synchronization task starts to run. You can view the progress of the task on the Data Synchronization page.

#### Configure two-way data synchronization

between RDS instances

##### Overview

DTS supports two-way real-time data synchronization between RDS instances on any two clouds. This section describes how to use DTS to create a two-way synchronization task between two ApsaraDB RDS for MySQL instances for active geo-redundancy, geo-disaster recovery, and other scenarios.

##### Supported synchronization statements

Two-way synchronization between ApsaraDB RDS for MySQL instances supports all DML updates (including INSERT, UPDATE, and DELETE) and the following DDL updates: ALTER TABLE, ALTER VIEW, ALTER FUNCTION, and ALTER PROCEDURE CREATE DATABASE, CREATE SCHEMA, CREATE INDEX, CREATE TABLE, CREATE PROCEDURE, CREATE FUNCTION, CREATE TRIGGER, CREATE VIEW, and CREATE EVENT DROP FUNCTION, DROP EVENT, DROP INDEX, DROP PROCEDURE, DROP TABLE, DROP TRIGGER, and DROP VIEW RENAME TABLE and TRUNCATE TABLE To ensure the stability of a two-way synchronization channel, you can synchronize DDL updates on the same table in only one direction. For example, for two-way synchronization, you must enable DDL synchronization in either the At o-B or B-t o-A direction. If DDL synchronization is configured in one direction, it is not supported in the reverse direction. You can only perform DML synchronization.

##### Detect and resolve conflicts

To ensure data consistency, for two-way synchronized instances, make sure that records with the same primary key, business primary key, or unique key are updated only on one of the instances. If you unexpectedly update a record with the same primary key, business primary key, or unique key on both instances that are two-way synchronized, a synchronization conflict occurs. To maximize the stability of two-way synchronized instances, DTS supports detecting and resolving data conflicts. Considerations During two-way synchronization, the system time of the source and destination instances may not be the same. Additionally, synchronization delays may occur. For these reasons, DTS cannot guarantee that its conflict detection mechanism can completely prevent data conflicts. You must refactor certain business logic to ensure that records of the same primary key, business primary key, or unique key are updated only on one of the instances that are two-way synchronized. Supported conflict types Currently, DTS supports detecting the following conflict types: Uniqueness conflicts caused by INSERT operations A uniqueness conflict occurs when the synchronization of an inserted row violates the unique constraint. For example, if two instances in two-way synchronization insert a record with the same primary key value at almost the same time, one of the inserted records fails to be synchronized because a record with the same primary key value already exists in the destination instance. Inconsistent records caused by UPDATE operations Update conflicts occur in the following scenarios: The records to be updated do not exist in the destination instance. If the records to be updated do not exist, DTS automatically changes the UPDATE operation to the INSERT operation and inserts these records to the destination instance. In this case, duplicate unique key values may occur. The primary keys or unique keys of the records to be updated conflict with each other. A DELETE operation is made on non-existent records A delete conflict occurs when the records to be deleted do not exist in the destination instance. In this case, DTS automatically ignores the DELETE operation regardless of the conflict resolution policy that you have configured. Supported conflict resolution policies For the preceding synchronization conflicts, DTS provides the following resolution policies. You can select a conflict resolution policy as required when configuring two-way synchronization. TaskFailed: The synchronization task reports an error and automatically exits the process in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task reports an error and automatically exits the process. The task enters a failed state and you must manually resolve the conflict. This method is the default conflict resolution policy. Ignore: The records in the destination instance are used in case of a conflict. When the synchronization encounters a conflict of the preceding types, the synchronization task skips the current synchronization statement and continues the process. The records in the destination instance are used. Overwrite: The conflict records in the destination instance are overwritten in case of a conflict. When the synchronization encounters a conflict of the preceding types, the conflict records in the destination instance are overwritten.

##### Synchronization restrictions

This section describes the restrictions in cross-cloud data synchronization using DTS. Restrictions in data sources Currently, only ApsaraDB RDS for MySQL instances support two-way synchronization. Other heterogeneous data sources do not support two-way synchronization. The destination instance cannot be an RDS instance that runs in standard access mode and has only a public network address. Restrictions in synchronization architecture Currently, DTS only supports two-way synchronization between two ApsaraDB RDS for MySQL instances. Two-way synchronization between more than two instances is not supported. Feature restrictions Incompatible with triggers When you synchronize an entire database and the database contains a trigger that updates the synchronization table, the synchronized data may be inconsistent. For example, the object to be synchronized is database A that contains table a and table b. Table a has a trigger that inserts a row to table b after the row is inserted to table a. In this case, if an INSERT operation is performed on table a in the source instance during synchronization, the data in table b is inconsistent between the source and destination instances. To resolve this problem, you must delete the trigger in the destination instance, so that the data in table b is only synchronized from the source instance. Restrictions in the RENAME TABLE operation The RENAME TABLE operation may result in inconsistent synchronization data. For example, if the object to be synchronized only includes table a and the rename a t o b command is executed in the source instance during synchronization, subsequent operations to the renamed table b are not synchronized to the destination database. To solve this problem, you can synchronize the entire database where table a and table b are stored. Restrictions in DDL synchronization direction To ensure the stability of a two-way synchronization channel, you can synchronize DDL updates on the same table in only one direction. For example, in A-to-B and B-to-A synchronization, you can implement DDL synchronization in either the A-t o-B or B-t o-A direction. If DDL synchronization is configured in one direction, it is not supported in the reverse direction.

##### Configure two-way data synchronization

between ApsaraDB RDS for MySQL instances across regions This topic describes how to configure two-way data synchronization between ApsaraDB RDS for MySQL instances across regions by using Data Transmission Service (DTS). Prerequisites Basic plans for cross-cloud data synchronization and two-way data synchronization are purchased. The source and destination ApsaraDB RDS for MySQL instances are created. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. The _ binlog row image parameter is set to full. Otherwise, error messages are returned _ _ during the precheck and the data synchronization task cannot be started. Binary logs are retained for at least seven days during initial full data synchronization. You can wait until initial full data synchronization is complete, and then clear the binary logs generated in the source database after the DTS task is run. Not e To ensure data security, DTS stores up to 50 GB of binary logs that are generated within the last 24 hours. If the limit is exceeded, DTS automatically clears the cached logs. Warning If you clear the binary logs of the source database during initial full data synchronization, the data synchronization task may fail. For example, initial full data synchronization takes more than 24 hours due to a large amount of data in the source database and abnormal writing in the destination database. In this case, if the binary logs of the source database are cleared during initial full data synchronization, DTS cannot obtain the binary logs generated 24 hours ago and the data synchronization task may fail. |

| Category | Description |
|---|---|
| Other limits | To ensure compatibility, we recommend that you use the same engine versions for the source and destination MySQL databases. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost or pt-online-schema-change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. If you use only DTS to write data to the destination database, you can use Data Management (DMS) to perform online DDL operations on source tables during data synchronization. Warning If you use tools other than DTS to write data to the destination database, we recommend that you do not use DMS to perform online DDL operations. Otherwise, data loss may occur in the destination database. |
| Special cases | Take note of the following items when you configure two-way data synchronization between MySQL instances: DTS supports two-way data synchronization only between two MySQL databases. DTS does not support two-way data synchronization between multiple MySQL databases. Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. When DTS runs a two-way data synchronization task, DTS creates a database named dts in the destination database to prevent circular synchronization. When the task is running, do not modify the dts database. |

Procedure
1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. On the Dat a Synchronizat ion page, click Creat e T ask. In the panel that appears, configure
parameters to create a data synchronization instance.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select MySQL. |

| Parameter | Description |
|---|---|
| Source Region | The region in which the source instance resides. Not e You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select MySQL. |
| Dest inat ion Region | The region in which the destination instance resides. Not e You cannot change the value of this parameter after you purchase the data synchronization instance. Exercise caution when you configure this parameter. |
| Synchronizat ion T opology | The synchronization topology of the data synchronization instance. Select T wo-way Synchronizat ion. |
| Quant it y | The number of data synchronization instances that you want to create at a time. |

4. After you configure the parameters, click Purchase Inst ance. In the message that appears, click OK.
After you create a data synchronization instance, go back to the Data Synchronization page. The new data synchronization instance is in the Not Configured state and contains two data synchronization tasks. You can configure data synchronization tasks in the forward and reverse directions.
5. Find the data synchronization task in the forward direction and click Conf igure T ask.
When you configure the data synchronization task in the forward direction, the data synchronization task in the reverse direction cannot be configured.
6. Configure the source and destination databases.

| Section | Parameter | Description |
|---|---|---|
| N/A | T ask Name | The name of the task. DTS automatically generates a task name. We recommend that you specify an informative name to identify the task. You do not need to specify a unique task name. |
|   | Dat abase T ype | The type of the source database. Select MySQL. |

| a Transmission Service |   |   |
|---|---|---|
|   | User Guide·Data synchronizatio |   |
| Section | Parameter | Description |
| Source Dat abase | Access Met hod | The access method of the source database. Select Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the source ApsaraDB RDS for MySQL instance resides. |
|   | Replicat e Dat a Across Alibaba Cloud Account s | Specifies whether to synchronize data across Alibaba Cloud accounts. In this example, Yes is selected. |
|   | Alibaba Cloud Account | The ID of the Alibaba Cloud account to which the source instance belongs. |
|   | RAM Role Name | The name of the Resource Access Management (RAM) user that is configured by the Alibaba Cloud account to which the source instance belongs. |
|   | RDS Inst ance ID | The ID of the source ApsaraDB RDS for MySQL instance. |
|   | Dat abase Account | The database account of the source ApsaraDB RDS for MySQL instance. |
|   | Database Password | The password of the database account. |
|   | Encrypt ion | Specifies whether to encrypt the connection to the source instance. Select Non-encrypt ed or SSL- encrypt ed based on your business requirements. In this example, Non-encrypt ed is selected. |
| Dest inat ion Dat abase | Dat abase T ype | The type of the destination database. Select MySQL. |
|   | Access Met hod | The access method of the destination database. Select Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the destination ApsaraDB RDS for MySQL instance resides. |
|   | RDS Inst ance ID | The ID of the destination ApsaraDB RDS for MySQL instance. |
|   | Dat abase Account | The database account of the destination ApsaraDB RDS for MySQL instance. |
|   | Dat abase Password | The password of the database account. |
|   | Encrypt ion | Specifies whether to encrypt the connection to the destination instance. Select Non-encrypt ed or SSL- encrypt ed based on your business requirements. In this example, Non-encrypt ed is selected. |

7. In the lower part of the page, click T est Connect ivit y and Proceed.
DTS automatically adds the CIDR blocks of DTS servers in the source or destination region to the whitelist of the source or destination instance. After data synchronization is complete, we recommend that you remove the CIDR blocks of DTS servers from the whitelists.
8. Select the objects to be migrated and configure advanced settings.
Basic Set t ings

| Setting | Description |
|---|---|
| Task Stages | By default, Increment al Dat a Synchronizat ion is selected. You must also select Schema Synchronizat ion and Full Dat a Synchronizat ion. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination cluster. The historical data is the basis for subsequent incremental synchronization. |

| Setting | Description |
|---|---|
| Processing Mode of Conflicting Tables | Precheck and Report Errors: checks whether the destination database contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Not e You can use the object name mapping feature to rename the tables that are synchronized to the destination database. You can use this feature if the source and destination databases contain identical table names and the tables in the destination database cannot be deleted or renamed. For more information, see Specify the name of an object in the destination instance. Ignore Errors and Proceed: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore Errors and Proceed, data inconsistency may occur and your business may be exposed to potential risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |

| Setting | Description |
|---|---|
| Exclude DDL Statements | Yes: does not synchronize DDL operations. No: synchronizes DDL operations. Import ant Limits on DDL synchronization directions: To ensure the stability of two-way data synchronization, you can synchronize DDL operations only in the forward direction. |
| Conflict Resolution Policy | The resolution policy for synchronization conflicts. By default, T askFailed is selected. You can select a conflict resolution policy based on your business requirements. T askFailed (When a conflict occurs, an error is reported and the task is terminated.) The default conflict resolution policy. If a conflict occurs during data synchronization, the synchronization task reports an error and exits. The task enters a failed state and you must manually resolve the conflict. Ignore (When a conflict occurs, the conflicting record in the destination instance is used.) If a conflict occurs during data synchronization, the synchronization task ignores the current statement and continues. The conflicting records in the destination database are used. Overwrit e (Conflicting records in the destination instance are overwritten.) If a conflict occurs during data synchronization, the conflicting records in the destination database are overwritten. |
| Source Object s | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be synchronized. If you select tables or columns as the objects to be synchronized, DTS does not synchronize other objects such as views, triggers, or stored procedures to the destination database. |
| Select ed Object s | To rename an object that you want to synchronize to the destination instance, right-click the object in the Select ed Object s section. For more information, see Specify the name of an object in the destination instance. For more information about how to specify WHERE conditions to filter data, see Use SQL conditions to filter data. To select the DML and DDL operations to be synchronized, right-click the object in the Select ed Object s section and select the DML and DDL operations to be synchronized. |

Advanced set t ings

| Setting | Description |
|---|---|
| Specify the retry time for a failed connection to the source instance or destination instance | The retry time range for failed connections. If a data synchronization task is disconnected, DTS immediately retries a connection within the specified time range. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the retry time range to more than 30 minutes. If DTS reconnects to the source and destination databases within the specified time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. When DTS retries a connection, you are charged for the data migration task. We recommend that you specify the retry time range based on your business requirements. You can also release the data migration task at your earliest opportunity after the source and destination instances are released. |

9. In the lower part of the page, click Next : Save T ask Set t ings and Precheck.
0. Wait until the Success Rat e value becomes 100%. Then, click Back.
1. After the data synchronization task in the forward direction is initialized, you can configure the data
synchronization task in the reverse direction. For more information about how to configure the task, see Steps 5 to 10.

#### Synchronize data between PolarDB-X 2.0

instances This topic describes how to synchronize data between PolarDB-X 2.0 instances by using Data Transmission Service (DTS). Prerequisites The source and destination PolarDB-X 2.0 instances are created and compatible with MySQL 5.7. The available storage space of the destination PolarDB-X 2.0 instance is larger than the total size of the data in the source PolarDB-X 2.0 instance. Limits

| Category | Description |
|---|---|

| Category | Description |
|---|---|
| Limits on the source database | The tables to be synchronized must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, the destination database may contain duplicate data records. If you select tables as the objects to be synchronized and you want to edit the tables in the destination database, such as renaming tables or columns, you can synchronize up to 1,000 tables in a single data synchronization task. If you run a task to synchronize more than 1,000 tables, a request error occurs. In this case, we recommend that you configure multiple tasks to synchronize the tables in batches or configure a task to synchronize the entire database. The following requirements for binary logs must be met: Binary logging is enabled on the Calculation layer and Storage layer tabs in the PolarDB-X console. For more information, see the Paramet er set t ings topic of PolarDB-X User Guide. The binlog row image parameter is set to full. Otherwise, _ _ error messages are returned during the precheck and the data synchronization task cannot be started. If you perform only incremental data synchronization, the binary logs of the source database are retained for at least 24 hours. If you perform both full data synchronization and incremental data synchronization, the binary logs of the source database are retained for at least seven days. After full data synchronization is complete, you can set the retention period to more than 24 hours. Otherwise, DTS may fail to obtain the binary logs and the task may fail. In exceptional circumstances, data inconsistency or loss may occur. Make sure that you set the retention period of binary logs based on the preceding requirements. Otherwise, the Service Level Agreement (SLA) of DTS does not guarantee service reliability or performance. The source PolarDB-X 2.0 instance must be compatible with MySQL 5.7. |
| Other limits | The destination PolarDB-X 2.0 instance must be compatible with MySQL 5.7. Before you synchronize data, evaluate the impact of data synchronization on the performance of the source and destination databases. We recommend that you synchronize data during off-peak hours. During initial full data synchronization, DTS uses the read and write resources of the source and destination databases. This may increase the loads on the database servers. During initial full data synchronization, concurrent INSERT operations cause fragmentation in the tables of the destination database. After the initial full data synchronization is complete, the size of used tablespace of the destination database is larger than that of the source database. We recommend that you do not use tools such as gh-ost and pt-online-schema- change to perform DDL operations on source tables during data synchronization. Otherwise, data synchronization may fail. |

SQL operations that can be synchronized

| Operation type | SQL statement |
|---|---|
| DML | INSERT, UPDATE, and DELETE |

Permissions required for database accounts

| Database | Schema synchronization | Full data synchronization | Incremental data synchronization |
|---|---|---|---|
| Source PolarDB-X 2.0 instance | SELECT permission | SELECT permission | SELECT permission on the objects to be synchronized, REPLICATION SLAVE permission, and REPLICATION CLIENT permission |
| Destination PolarDB-X 2.0 instance | Read and write permissions on the objects to be synchronized |   |   |

Step 1: Create a data synchronization task
1. Log on to the Data Management (DMS) console.
For more information, see the Log on to the DMS console topic of DMS User Guide.
2. In the top navigation bar, click DT S.
3. In the left-side navigation pane, click Dat a Migrat ion to go to the DT S console.
The layout and style of the DMS console may be different from those of the DMS console described in this topic. To go to the DTS console, you may need to choose DTS > Dat a Synchronizat ion in the top navigation bar.
4. On the Dat a Synchronizat ion page, click Creat e T ask.
5. In the panel that appears, configure the parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Source Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
| Source Region | The region in which the source instance resides. |
| Dest inat ion Dat abase T ype | The type of the destination database. Select PolarDB-X 2.0. |
| Dest inat ion Region | The region in which the destination instance resides. |
| Quant it y | The number of data synchronization instances that you want to create at a time. Default value: 0. |

6. Click Purchase Inst ance.
Step 2: Configure the data synchronization task
1. In the dat a synchronizat ion t asks list, find the data synchronization task that you created and
click Conf igure T ask in the rightmost column.
2. Configure the source and destination databases. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| N/A | T ask Name | The name of the task. DTS automatically generates a task name. We recommend that you specify a descriptive name for easy identification. You do not need to specify a unique task name. |
| Source Dat abase | Dat abase T ype | The type of the source database. Select PolarDB-X 2.0. |
|   | Access Met hod | The value of this parameter is fixed to Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the source PolarDB-X 2.0 instance resides. |
|   | Inst ance ID | The ID of the source PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the source PolarDB-X 2.0 instance. The account must have the SELECT permission on the objects to be synchronized, the REPLICATION CLIENT permission, and the REPLICATION SLAVE permission. |
|   | Dat abase Password | The password of the database account. |
| Dest inat i on Dat abase | Dat abase T ype | The type of the destination database. Select PolarDB-X 2.0. |
|   | Access Met hod | The value of this parameter is fixed to Alibaba Cloud Inst ance. |
|   | Inst ance Region | The region in which the destination PolarDB-X 2.0 instance resides. |
|   | Inst ance ID | The ID of the destination PolarDB-X 2.0 instance. |
|   | Dat abase Account | The database account of the destination PolarDB-X 2.0 instance. The account must have the read and write permissions on the destination PolarDB-X 2.0 instance. |
|   | Dat abase Password | The password of the database account. |

3. In the lower part of the page, click T est Connect ivit y and Proceed.
4. Select objects for the task and configure advanced settings.
Basic Set t ings

| Paramet er | Description |
|---|---|

| Paramet er | Description |
|---|---|
| T ask St ages | By default, Increment al Dat a Synchronizat ion is selected. You must also select Schema Synchronizat ion and Full Dat a Synchronizat ion. After the precheck is complete, DTS synchronizes the historical data of selected objects from the source instance to the destination cluster. The historical data is the basis for subsequent incremental synchronization. |

| Paramet er | Description |
|---|---|
| Process ing Mode of Conf lict ing T ables | Precheck and Report Errors: checks whether the destination instance contains tables that have the same names as tables in the source database. If the source and destination databases do not contain tables that have identical table names, the precheck is passed. Otherwise, an error is returned during the precheck and the data synchronization task cannot be started. Not e You can use the object name mapping feature to rename the tables that are synchronized to the destination database. You can use this feature if the source and destination databases contain identical table names and the tables in the destination database cannot be deleted or renamed with ease. For more information, see Specify the name of an object in the destination instance. Ignore: skips the precheck for identical table names in the source and destination databases. Warning If you select Ignore, data inconsistency may occur between the source and destination databases and your business may be exposed to risks. If the source and destination databases have the same schemas, and a data record has the same primary key value as an existing data record in the destination database: During full data synchronization, DTS does not synchronize the data record to the destination database. The existing data record in the destination database is retained. During incremental data synchronization, DTS synchronizes the data record to the destination database. The existing data record in the destination database is overwritten. If the source and destination databases have different schemas, initial data synchronization may fail. In this case, only specific columns are synchronized, or the data synchronization task fails. |

| Paramet er | Description |
|---|---|
| Select Object s | Select one or more objects from the Source Object s section and click the icon to add the objects to the Select ed Object s section. Not e You can select columns, tables, or databases as the objects to be synchronized. If you select tables or columns as the objects to be synchronized, DTS does not synchronize other objects such as views, triggers, or stored procedures to the destination database. |

Advanced set t ings

| Paramet er | Description |
|---|---|
| Ret ry T ime f or Failed Connec t ion | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 120. We recommend that you set the parameter to a value greater than 30. If DTS reconnects to the source and destination databases within the specified retry time range, DTS resumes the data synchronization task. Otherwise, the data synchronization task fails. Not e If you set different retry time ranges for multiple data synchronization tasks that have the same source or destination database, the shortest retry time range that is set takes precedence. |

5. In the lower part of the page, click Next : Precheck and St art T ask.
Before you can start the data synchronization task, DTS performs a precheck. You can start the data synchronization task only after the task passes the precheck. If the task fails to pass the precheck, you can click the det ails icon next to each failed item to view details. You can troubleshoot the issues based on the causes and run a precheck again. After the value of Success Rat e becomes 100%, the data synchronization task starts to run. You can view the progress of the task on the Data Synchronization page.

### Manage data synchronization

instances

#### Specify the name of an object in the

destination instance After an object, such as a database or table, is synchronized from the source instance to the destination instance, the name of the object remains unchanged. You can use the object name mapping feature provided by DTS to specify a different name for the object in the destination instance. Notes You can perform this operation only when a data synchronization task is configured and the current process is Select Object s t o Synchronize. Do not perform this operation after the data synchronization task is started. Otherwise, the synchronization may fail. Procedure
1. On the Select Object s t o Synchronize page, move the required objects to the Select ed section,
move the pointer over a database or table, and then click Edit . Different database types support different objects. If Edit appears when you move the pointer over the target object, the operation is supported.
2. In the dialog box that appears, specify a name for the object in the destination instance.
Database name mapping In the Edit Dat abase Name dialog box that appears, enter the database name that you want to use in the destination instance. Table name mapping In the Edit T able dialog box that appears, enter the table name that you want to use in the destination instance. Column name mapping In the Edit T able dialog box that appears, enter a new name for each column. In this step, you can deselect columns that do not need to be synchronized.
3. Click OK.
4. Configure other parameters that are required for the data synchronization task.

#### Use SQL conditions to filter data

When you select the objects to be synchronized in a data synchronization task, you can specify SQL conditions to filter data. Only the data that meets the specified conditions is synchronized to the destination database. This feature is applicable to scenarios such as regular data synchronization and table partitioning. Prerequisites A data synchronization task is being configured. The current step is Select Object s t o Synchronize. For more information about how to create and configure a data synchronization task, see configuration examples in Data Transmission Service (DTS) documentation. Limits You can filter the fields only in the current table. Cross-table filtering is not supported. If the source database is a self-managed PostgreSQL database or an ApsaraDB RDS for PostgreSQL instance, filter conditions do not take effect on incremental data. Procedure
1. In the Select Object s t o Synchronize step, move the required objects to the Select ed section,
move the pointer over a table, and then click Edit .
2. In the Edit T able Name dialog box, enter one or more SQL conditions in the Filt er Condit ions field.
An SQL condition is a standard SQL WHERE statement. The following operators are supported: `=` , != , `<` , `>` , and `in` . Only the data that meets the WHERE condition is synchronized to the destination database. In this example, `orderid>100` is entered. You can specify a time condition in an SQL WHERE statement. However, you must make sure that the specified time condition is valid. For example, to filter incremental data

| create time>'2020- _ |   |
|---|---|

created since 2020, you must enter `create_time>'2020-01-01'` or `create_time>'2020-` `01-01 00:00:00'` . You cannot enter `create_time>'2020'` .

|   | 01-01 00:00:00' |
|---|---|

You can use single quotation marks (') in an SQL condition if necessary. For example, you can enter `address in('hangzhou','shanghai')` .
3. Click Verif y to check whether the syntax is valid.
If the syntax is valid, the Inf ormat ion message shows that t he validat ion is passed. If the syntax is invalid, the Error message appears. In this case, you must modify the condition based on the instructions.
4. Click OK.
5. Configure other parameters that are required for the data synchronization task.

#### Add objects to a data synchronization task

When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to add objects to a data synchronization task in the DTS console. Limits You can modify the required objects only when the data synchronization task is in the Synchronizing or Synchronizat ion Failed state. Start time of data synchronization The time when DTS synchronizes data of new objects depends on whether initial synchronization is specified for the data synchronization task. If initial synchronization is specified, DTS synchronizes schemas and historical data, and then synchronizes incremental data. If initial synchronization is not specified, DTS synchronizes data after incremental data is generated on the source instance. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. Find the data synchronization task and choose More > Modif y Object s t o Synchronize in the
Actions column.
4. On the Select Object s t o Synchronize tab, add objects based on your needs, as shown in Add
objects to a data synchronization task. Add objects to a data synchronization task
5. Click Precheck.
After the task passes the precheck, the objects are added to the data synchronization task. After the objects are added, if initial synchronization is specified for the data synchronization task, the task status changes from Synchronizing to Synchronizing (T he init ial synchronizat ion of t he new object s is being perf ormed.). You can click View More to view the initial synchronization progress of the new objects. After the initial synchronization on the new objects is complete, the task status returns to Synchronizing.

#### Remove objects from a data

synchronization task When a data synchronization task is running, you can add objects to the task or remove objects from the task. This topic describes how to remove objects from a data synchronization task in the DTS console. Limits You can modify the objects only when a data synchronization task is in the incremental data synchronization phase and not in the Modifying Objects state. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Dat a Synchronizat ion.
3. On the page that appears, find the instance that you want to manage and click Reselect Object s in
the Actions column. For instances that failed to run, choose
> Reselect Object s.
4. On the Select Object s t o Synchronize tab, remove objects based on your needs.
5. Click Precheck to run a precheck.

#### Troubleshoot precheck failures

Before Data Transmission Service (DTS) runs a data synchronization task, DTS performs a precheck. This topic describes the precheck items and how to troubleshoot precheck failures. Source database connectivity DTS checks whether DTS servers can connect to the source RDS instance. DTS creates a connection to the source RDS instance by using the JDBC protocol. If the connection fails, the task fails to pass the precheck. Cause of failure DTS does not support data synchronization between RDS instances in the region where the source instance resides. The database account or password of the source instance is invalid. Solution Submit a ticket and contact Alibaba Cloud technical support. Destination database connectivity DTS checks whether DTS servers can connect to the destination RDS instance. DTS creates a connection to the destination RDS instance by using the JDBC protocol. If the connection fails, the task fails to pass the precheck. Cause of failure DTS does not support data synchronization between RDS instances in the region where the destination instance resides. The database account or password of the destination instance is invalid. Solution Submit a ticket and contact Alibaba Cloud technical support. Source database version DTS checks whether: i. The database version of the source RDS instance is supported by the data synchronization feature. ii. The database version of the destination RDS instance is the same as the database version of the source RDS instance. Cause of failure The database version of the source RDS instance is earlier than the supported database versions. The data synchronization feature supports the following database versions: MySQL 5.1, 5.5, 5.6, and 5.7. The database version of the destination RDS instance is earlier than the database version of the source RDS instance. Solution If the database version of the source RDS instance is earlier than the supported database versions, upgrade the source RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again. If the database version of the destination RDS instance is earlier than the database version of the source RDS instance, upgrade the destination RDS instance to MySQL 5.6 or 5.7 in the RDS console. Then, create a data synchronization task again. Database existence DTS checks whether the destination database already exists in the destination instance. If the destination database does not exist in the destination instance, DTS automatically creates a database. However, DTS fails to create the database and reports a failure under the following circumstances: The database name contains characters other than lowercase letters, digits, underscores (_), and hyphens (-). The character set of the database is not UTF-8, GBK, Latin1, or UTF-8MB4. The account of the destination database does not have the read and write permissions on the source database. If the data source is an RDS instance, the task passes the precheck. Source database permissions DTS checks whether the account of the source database has the required permissions. If the account does not have the required permissions, the task fails to pass the precheck. If the source database is an RDS instance, the task passes the precheck. Destination database permissions DTS checks whether the account of the destination database has the required permissions. If the account does not have the required permissions, the task fails to pass the precheck. Cause of failure DTS fails to create a database account in the destination RDS instance. DTS fails to grant the read/write permissions to the database account of the destination RDS instance. Solution Submit a ticket and contact Alibaba Cloud technical support. Object name conflict DTS checks object names only if you select initial synchronization for a data synchronization task. DTS checks whether an object that you want to synchronize has the same name as an object in the destination RDS instance. Cause of failure If an object in the destination RDS instance has the same name as the object that you want to synchronize, the task fails to pass the precheck. Solution Remove the conflicting object from the destination database. Then, create a data synchronization task again. Select both Initial Schema Synchronization and Initial Full Data Synchronization. Value of server_id in the source database DTS checks whether the value of the server_id parameter in the source database is set to an integer that is greater than or equal to 2. If the data source is an RDS instance, the task passes the precheck. Whether binary logging is enabled for the source database DTS checks whether the binary logging feature is enabled for the source database. If the binary logging feature is disabled for the source database, the task fails to pass the precheck. If the data source is an RDS instance, the task passes the precheck. Whether the binlog format is ROW in the source database DTS checks whether the binary log format of the source database is set to ROW. If the binary log format of the source database is not set to ROW, the task fails to pass the precheck. If the data source is an RDS instance, the task passes the precheck. Integrity of the FOREIGN KEY constraints DTS checks whether the parent tables and child tables that have referential relationships with each other are all included in the required objects. The precheck allows DTS to protect the integrity of the FOREIGN KEY constraints. Cause of failure One or more child tables are included in the required objects. However, the parent tables that are referenced by the child tables are not included in the required objects. This impairs the integrity of the FOREIGN KEY constraints. Solution The following solutions are available: Create a data synchronization task again and do not synchronize the child tables that fail to pass the precheck. Create a data synchronization task again and add the parent tables to the required objects. Remove the FOREIGN KEY constraints from the child tables that fail to pass the precheck. Then, create a data synchronization task again. Storage engine DTS checks whether the required objects use the storage engines that are not supported by the data synchronization feature, such as FEDERATED, MRG_MyISAM, and TokuDB. Cause of failure If the storage engine of a source table is FEDERATED, MRG_MyISAM, or TokuDB, the task fails to pass the precheck. Solution Change the unsupported storage engine to InnoDB and create a data synchronization task again. Character set DTS checks whether the required objects use the character sets that are not supported by the data synchronization feature, such as the UCS-2 character set. Cause of failure If the character sets used by the required objects are not supported by the data synchronization feature, the task fails to pass the precheck. Solution Change the unsupported character sets to UTF-8, GBK, or Latin1. Then, create a data synchronization task again. Complicated topologies DTS checks whether the topology that you specify for the source and destination RDS instances is supported. Cause of failure The source RDS instance in the current task is being used as the destination instance of another task. The destination RDS instance in the current task is being used as the source or destination instance of another task. The objects that you want to synchronize in the current task are being synchronized by an existing task. The two tasks have the same source and destination RDS instances. Solution If the task that you want to create has the same source and destination RDS instances as an existing task, you can add the required objects to the existing task. You do not need to create another task to synchronize these objects. If the task that you want to create conflicts with an existing task, wait until the existing task is completed before you create a data synchronization task again. Format of the MySQL database password DTS checks whether the format of the password that is used to access the source database is no longer valid. If the data source is an RDS instance, the task passes the precheck.

### Best practices for data

synchronization from PolarDB-X instances

#### Limits and usage notes for synchronizing

data between PolarDB-X instances PolarDB-X does not provide binary logs. To ensure data quality, we recommend that you take note of the limits when you perform business design, business development, and O&M changes. Overview Limits on the business design Limits on the database architecture Limits on O&M changes Potential risks on data quality Suggestions to ensure data quality Limits on the business design All tables must have primary keys. Otherwise, data inconsistency may occur in data synchronization because the destination database may contain duplicate data records. We recommend that you do not use the global secondary indexes (GSIs) of PolarDB-X because they are updated asynchronously. If you use GSIs, DTS can ensure only eventual consistency of data. The databases that you want to synchronize cannot be deployed in mixed mode. The mixed mode refers to a mode in which both the unit mode and the copy mode are used). In unit mode, users perform read and write operations in their respective unit nodes. Two-way synchronization is implemented between the databases in each unit node and those in the central node. In copy mode, users write data to the databases in the central node. The data is then synchronized to the databases in each unit node. If you configure two-way synchronization between PolarDB-X instances and use underlying MySQL databases, fields of the FLOAT or DOUBLE type are not supported in business tables. If the business tables have fields of the FLOAT or DOUBLE type, convert the field type to DECIMAL. If you configure one-way synchronization between PolarDB-X instances, fields of the FLOAT or DOUBLE type are supported in business tables. DTS does not allow you to synchronize objects such as stored procedures, triggers, functions, views, and events in data synchronization between PolarDB-X instances. DTS does not support initial schema synchronization between PolarDB-X instances. You must manually create objects such as databases and tables in the destination database. Make sure that the available storage capacities in PolarDB-X instances are sufficient for business expansion. If the version of the MySQL databases attached to a PolarDB-X instance is 5.7 or 8.0, you cannot configure a change tracking task for the PolarDB-X instance. Instead, you must configure a change tracking task for each MySQL database attached to the PolarDB-X instance. Limits on the database architecture An ApsaraDB RDS for MySQL instance that is attached to a PolarDB-X instance cannot be attached to another PolarDB-X instance. The ApsaraDB RDS for MySQL instances attached to the source PolarDB-X instance must have the same specifications as those attached to the destination PolarDB-X instance. For example, if the source PolarDB-X instance has four ApsaraDB RDS for MySQL instances, the destination PolarDB-X instance must have four ApsaraDB RDS for MySQL instances whose specifications are the same as those in the source PolarDB-X instance. The sharding rule of the source PolarDB-X instance must be the same as that of the destination PolarDB-X instance. Otherwise, no data synchronization task can be created. You can synchronize only business tables between Polar-X instances. You cannot synchronize metadata tables or system tables between PolarDB-X instances. Limits on O&M changes

| Change type | Description | Impact and solution |
|---|---|---|
| PolarDB-X instances | Change a sharding rule. For example, change the shard key of a database or table, or change the number of shards. | Not supported. You must perform the following steps to recreate a data synchronization task: 1. Stop and delete the original data synchronization task. 2. Wait until the changes are complete in the source database. Then, clear the data that has been synchronized to the destination database. 3. Configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. |
|   | Change the number of instances at the storage layer. For example, scale out instances or migrate frequently-accessed tables. |   |

| Change type | Description | Impact and solution |
|---|---|---|
| Storage | Change the specifications of instances and switch workloads at the storage layer. | Data synchronization is not affected. |
|   | Change parameter settings. | The parameter settings of the source and destination databases must be the same. To change the parameter settings of instances at the storage layer, you must make sure that new parameters do not affect previous parameters. Not e If you are not sure about the impact of changing parameter settings, you can contact technical support of Database Expert Service. |
|   | Change backup and recovery policies, and enable auditing and diagnostics for instances at the storage layer. | The change takes effect only on the current instance and does not affect other instances with replication relationships. |
| DTS tasks | Perform DDL operations. | If you configure data synchronization tasks for ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance, the tasks may be delayed after you perform DDL operations. This is caused by the implementation logic of MySQL. |
| DDL operations at the database or table level | Add tables. | Not supported. You must perform the following steps: 1. After you perform DDL operations to create tables in the destination database, perform the same DDL operations to create tables in the source database. 2. Add the new tables to the objects of the data synchronization task. You can write data to the source database only after the preceding operations are complete. If you select tables as the objects of the data synchronization task, you must add the new tables to the synchronization queues on the source and destination instances at the storage layer. |

| Change type | Description | Impact and solution |
|---|---|---|
|   | Add fields, add secondary indexes, delete indexes, and modify indexes (except for replacing secondary indexes with unique indexes). | If you configure a data synchronization task for a PolarDB-X instance, you must perform DDL operations in the destination database, and then perform the same DDL operations in the source database. If you configure data synchronization tasks for ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance, DTS automatically synchronizes the operations that you perform. The following operations can be synchronized: Add fields, add secondary indexes, delete indexes, and modify indexes (except for replacing secondary indexes with unique indexes). |
|   | Perform other DDL operations. | Only the preceding DDL operations are supported. |
| Switchover | Perform a switchover. | Before you perform a switchover, make sure that the DTS task is not delayed. Otherwise, data quality issues occur. |
|   | Perform a failover that meets the requirements of recovery point objective (RPO). Not e RPO represents the maximum amount of data that can be lost after a recovery from a failure. RPO is measured by time. Warning Failover: If the source instance or the data center where the source instance resides fails, you can switch workloads to a backup system. A failover is a lossy operation. | If a failure such as network interruption, an equipment failure, or a data center failure occurs and the data synchronization task is delayed, you may need to perform a failover. In this case, if the difference between the time when the last data entry is synchronized to the destination database and the time when the failure occurs is less than the RPO, you can perform a failover to recover your business. For example, if the RPO is 5 minutes, the quality of the data within the 5 minutes cannot be ensured after you perform a failover. You may need to revise the data to ensure consistency. Not e To query the time when the last data entry is synchronized to the destination database, refer to the documentation about task management. |

|   | Change type Not e |   | Description | Impact and solution |
|---|---|---|---|---|
|   | Switchover: After you use DTS to migrate or synchronize data from the source database to the destination database, you switch workloads from the source |   | Perform a failover that does not meet the requirements of RPO. | The data synchronization task may be delayed due to the following causes: A large number of DDL operations are performed in the source database, a network failure occurs, and the performance of the destination database is unfavorable. In this case, if the data center fails and the difference between the time when the last data entry is synchronized to the destination database and the time when the failure occurs is greater than the RPO, we recommend that you wait until the data center recovers before you perform a failover. For example, if the RPO is 5 minutes, the quality of the data within the 5 minutes cannot be ensured after you perform a failover. You may need to revise the data to ensure consistency. |
| P So b | database to ottheential risk destination mdea ctahbaansgee.s or s etween the sourc | s on data quality witchover operations may cause data quality issues such as schema inconsistency e and destination databases. |   |   |

If data latency occurs between the primary and secondary databases of the source instance, the data written to the primary database is not updated to the secondary database in a timely manner. In this case, if you perform a primary/secondary switchover in the source instance, DTS uses the secondary database of the source instance as the source database for data synchronization. As a result, the data that is not updated to the secondary database is lost. If the DTS task is resumed from a network failure after you perform a switchover, DTS attempts to synchronize the data generated before the failure occurs. This mechanism prevents data loss in the destination database. In this case, if the destination tables do not have primary keys, data will be inconsistent between the source and destination databases. If the destination tables have primary keys, data may not be consistent when DTS implements the retry mechanism, but data will remain consistent after the retry ends. The data synchronization task may be delayed due to network failures and DDL operations. The data synchronization task may be delayed or interrupted due to changes to the source database, unfavorable performance of the destination database, and schema inconsistency. Alibaba Cloud cannot solve the preceding issues. You must recreate a DTS task or adjust the source and destination databases. Suggestions to ensure data quality You must perform all DDL operations with caution. All DDL operations must be confirmed by the technical engineers to comply with the preceding limits. Do not directly perform DDL operations in your program code.

#### Solutions of data synchronization from a

PolarDB-X instance Data Transmission Service (DTS) supports data synchronization from a source PolarDB-X instance to a destination instance. However, if more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, we recommend that you do not directly configure a data synchronization task for the source PolarDB-X instance. If you do so, you may encounter a performance bottleneck or stability risks. This may affect your business. To ensure good performance and high stability of data synchronization, we recommend that you configure a data synchronization task for each ApsaraDB RDS for MySQL instance attached to the source PolarDB-X instance. Prerequisites You have read the Limits and usage notes for synchronizing data between PolarDB-X instances topic and understood the relevant conventions and usage notes. Synchronization solutions

| Solutio n | Configuration | Description |
|---|---|---|
| Solutio n 1 | You can configure a data synchronization task for each ApsaraDB RDS for MySQL instance that is attached to the source PolarDB-X instance. You must map the names of databases and tables in the ApsaraDB RDS for MySQL instances to the names of databases and tables in the destination instance. Compared with Solution 2, this solution ensures good performance and high stability of data synchronization. Import ant If you use this solution, you can select only tables as the objects to be synchronized. | If you require better performance and higher stability, we recommend that you use this solution. This solution has no limits on the number of ApsaraDB RDS for MySQL instances that are attached to the source PolarDB-X instance. |
| Solutio n 2 | You can directly configure a data synchronization task for the source PolarDB-X instance. If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, the performance and stability of data synchronization may deteriorate to the extent that your business may be affected. | If you use this solution, make sure that no more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance. Otherwise, the performance and stability of data synchronization may deteriorate. |

Comparison between the two solutions

| Comparison item | Solution 1 | Solution 2 |
|---|---|---|
| Performance | This solution requires you to configure multiple data synchronization tasks. This way, this solution multiplies the performance of data synchronization and ensures the feasibility of writing a large amount of data from a PolarDB-X instance. | This solution supports only one data synchronization task for the source PolarDB-X instance. If a large amount of data is written to the source PolarDB-X instance by the business side, a performance bottleneck may occur during data synchronization. |

| Comparison item | Solution 1 | Solution 2 |
|---|---|---|
| Stability | This solution ensures high stability. If a data synchronization task that you configure for one of the ApsaraDB RDS for MySQL instances fails, data synchronization tasks for other ApsaraDB RDS for MySQL instances are not affected. You need to only recover the failed data synchronization task. | This solution provides medium stability. If the data synchronization task for the source PolarDB-X instance fails, data synchronization fails. |
| Ease of use | You must configure multiple data synchronization tasks. This complicates the configuration process. You must configure database and table name mapping for each task. You must map the names of databases and tables in the ApsaraDB RDS for MySQL instances to the names of the databases and tables in the destination instance. | You need to only configure one data synchronization task. This simplifies the configuration process. |
| Resource usage | This solution requires multiple data synchronization instances. | This solution requires only one data synchronization instance. |

Synchronization of DDL operations In most cases, data synchronization from a source PolarDB-X instance does not support the synchronization of DDL operations. If you synchronize DDL operations during a data synchronization task, data may fail to be written to the destination instance. To prevent this problem, you can take one of the following measures:
1. Release the data synchronization task.
2. Clear the destination database.
3. Reconfigure the data synchronization task.
However, in a few cases, you can synchronize DDL operations during data synchronization from a source PolarDB-X instance. The following table describes the details of these cases.

| Case | Supported operation |
|---|---|
| You use Solution 1 and select tables as the objects to be synchronized. | You can add tables to the objects that you select for the data synchronization task. You can also add columns to or remove columns from the objects. However, you can perform these operations only during data synchronization between PolarDB-X instances. To do this, perform the following steps: i. Add columns to or remove columns from the objects that you select for the data synchronization task. ii. Add or remove columns in the destination database, and then perform the same operations in the source database. When DTS detects that a column already exists in the destination database, DTS ignores the error and does not display a write failure. |

| Case | Supported operation |
|---|---|
| You use Solution 2 and select entire databases as the objects to be synchronized. | You can only add tables to the objects. To do this, you must add tables in the destination database, and then perform the same operations in the source database. You cannot add or remove columns. Warning If you add a column to the database of the source PolarDB-X instance, some physical tables at the underlying layer may contain the column, whereas some physical tables do not contain the column. When DTS executes the assembled SQL statement, DTS may fail to find the column or lose the data in the column. |
| You use Solution 2 and do not select entire databases as the objects to be synchronized. | You can only add tables to the objects. To do this, perform the following steps: i. Add tables to the objects that you select for the data synchronization task. ii. Add tables in the destination database, and then perform the same operations in the source database. You cannot add or remove columns. |

## Change tracking

### Overview

You can use Data Transmission Service (DTS) to track data changes from ApsaraDB RDS for MySQL instances in real time. This feature applies to the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. Supported databases User-created MySQL databases or ApsaraDB RDS for MySQL PolarDB-X (formerly known as DRDS) User-created Oracle database Objects for change tracking The objects for change tracking include tables and databases. In change tracking, data changes include data manipulation language (DML) operations and data definition language (DDL) operations. When you configure change tracking, you must select operation types. Change tracking tasks A change tracking task is the basic unit of change tracking and data consumption. To track data changes from an RDS instance, you must create a change tracking task in the DTS console for the RDS instance. The change tracking task pulls data changes from the RDS instance in real time and locally stores the data changes. You can use the DTS SDK to consume the tracked data. You can also create, manage, or delete change tracking tasks in the DTS console.

### Create a change tracking

instance Before you configure a task to track data changes, you must create a change tracking instance. This topic describes how to create a change tracking instance in the Data Transmission Service (DTS) console. Procedure
1. Log on to the DTS console. For more information, see Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. In the upper-right corner, click Creat e Change T racking T ask.
4. In the Create DTS Instances dialog box, select a region, and enter the number of change tracking
instances that you want to create. In the Create DTS Instances dialog box, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.
5. Click Creat e.

### Configure change tracking tasks

#### Track data changes from an ApsaraDB RDS

for MySQL instance Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from an ApsaraDB RDS for MySQL instance. Prerequisites The database version of the source instance is MySQL 5.6, 5.7, or 8.0. Limits

|   | Category | Description |
|---|---|---|
|   | Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The following requirements for binary logs must be met: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck, and the change tracking task cannot be started. A read-only instance or temporary instance cannot be used as the source instance for change tracking. |
|   |   | Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt- online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |
|   | Other limits |   |

Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you want to configure and click Conf igure T ask in the
Act ions column.
3. Configure the source database.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source instance. Select RDS Inst ance. |
|   | Database Type | The type of the source database. The value of this parameter is set to MySQL and cannot be changed. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | RDS Instance ID | The ID of the ApsaraDB RDS for MySQL instance from which you want to track data changes. Not e A read-only instance or temporary instance cannot be used as the source instance for change tracking. |

| Section | Parameter | Description |
|---|---|---|
|   | Database Account | The database account of the source ApsaraDB RDS for MySQL instance. Not e The account must have the SELECT permission on the objects for change tracking, the REPLICATION SLAVE permission, and the REPLICATION CLIENT permission. If the database engine of the source ApsaraDB RDS for MySQL instance is MySQL 5.6, you do not need to configure the Dat abase Account and Dat abase Password parameters. |
|   | Database Password | The password of the database account. |
| Consumer network type | Network Type | The network type of the change tracking instance. Classic If you select Classic, no other configurations are required. VPC If you select VPC, you must specify the VPC and vSwit ch parameters. Not e If your change tracking client is deployed on a local server, you can select Classic or VPC. If you track data changes over internal networks, the network latency is minimal. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Paramet er or setting | Description |
|---|---|
| Required Data Types | Dat a Updat es DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Not e If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the selected objects. For more information, see Modify the objects for change tracking. |
| Required Objects | Select tables or databases from the Required Object s section and click the icon to move them to the Select ed section. |

| Paramet er or setting | Description |
|---|---|
| Specify the retry time for a failed connecti on to the source instance or destinati on instance | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS is reconnected to the source databases within the specified retry time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. Not e If you set different retry time ranges for multiple change tracking tasks that have the same source database, the shortest retry time range that is set takes precedence. |

6. In the lower-right corner of the page, click Save and Precheck.
Before you can start the change tracking task, DTS performs a precheck. You can start the change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
7. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data. What's next Previous change tracking feature: Run the SDK demo code New change tracking feature: Use a Kafka client to consume tracked data

#### Track data changes from a PolarDB-X

instance Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a PolarDB-X instance by using DTS. Limits Warning For more information about the limits of which you need to take note when you use DTS to synchronize data from a PolarDB-X instance, see Limits and usage notes for synchronizing data between PolarDB-X instances.

|   | Category | Description |
|---|---|---|
|   | Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The ApsaraDB RDS for MySQL instances attached to the PolarDB-X instance must meet the following requirements for binary logs: The binary logging feature is enabled. The binlog format parameter is set to row. _ The binlog row image parameter is set to full. Otherwise, error messages are _ _ returned during the precheck, and the change tracking task cannot be started. |
|   | Other limits | If more than two ApsaraDB RDS for MySQL instances are attached to the source PolarDB-X instance, latency and stability issues may occur when you track data changes from the PolarDB-X instance. We recommend that you configure multiple change tracking tasks to track data changes from the ApsaraDB RDS for MySQL instances attached to the source PolarDB-X instance. If N ApsaraDB RDS for MySQL instances are attached to source PolarDB-X Instance A, you must create N data synchronization tasks to synchronize data from PolarDB-X Instance A to a destination instance. We recommend that you estimate the number of change tracking tasks in advance and purchase enough expansion plans. Limits on the objects for change tracking: You can track data changes only at the table level. After the change tracking task is configured, the objects for change tracking cannot be reselected. If you want to track the data changes of tables that are not included in the selected objects, you must create another change tracking task for the tables. Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt- online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If you perform a primary/secondary switchover on the source database when the change tracking task is running, the task fails. When the change tracking task is running, do not scale out or scale in the capacity of the source instance, migrate frequently accessed tables, change shards, or perform DDL operations. Otherwise, the change tracking task fails or data inconsistency occurs. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |

Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you want to configure and click Conf igure T ask in the
Act ions column.
3. Configure the source database.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. The value of this parameter is set to DRDS Inst ance and cannot be changed. |
|   | Database Type | The type of the source database. The value of this parameter is set to DRDS and cannot be changed. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | The ID of the source PolarDB-X instance. |
|   | Database Name | The name of the source database in the PolarDB-X instance. |
|   | Database Account | The database account of the PolarDB-X instance. |
|   | Database Password | The password of the database account. |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Parameter or setting | Description |
|---|---|
| Required Data Types | Dat a Updat es DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Not e You can track data changes only at the table level. After the change tracking task is configured, the objects for change tracking cannot be reselected. If you want to track the data changes of tables that are not included in the selected objects, you must create another change tracking task for the tables. |
| Required Objects | Select tables from the Required Object s section and click the icon to move them to the Select ed section. |
| Specify the retry time range for a failed connection to the source database | By default, if DTS fails to connect to the source database, DTS retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source databases within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. |

6. In the lower-right corner of the page, click Save and Precheck.
Before you can start the change tracking task, DTS performs a precheck. You can start the change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
7. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data.

#### Track data changes from a self-managed

Oracle database Data Transmission Service (DTS) allows you to track data changes from databases in real time. You can use the change tracking feature in the following scenarios: lightweight cache updates, business decoupling, asynchronous data processing, and synchronization of extract, transform, and load (ETL) operations. This topic describes how to track data changes from a self-managed Oracle database. Prerequisites The engine version of the self-managed Oracle database is 9i, 10g, or 11g. Real Application Cluster (RAC) instances are not supported. Supplemental logging, including SUPPLEMENTAL_LOG_DATA_PK and SUPPLEMENTAL_LOG_DATA_UI, is enabled for the self-managed Oracle database. For more information, see Supplemental Logging. The self-managed Oracle database is running in ARCHIVELOG mode. Archived log files are accessible, and a suitable retention period is set for archived log files. For more information, see Managing Archived Redo Log Files. Limits

|   | Category | Description |
|---|---|---|
|   | Limits on the source database | The server to which the source database belongs must have sufficient outbound bandwidth. Otherwise, the change tracking speed decreases. The source tables must have PRIMARY KEY or UNIQUE constraints, and all fields must be unique. Otherwise, part of the tracked data changes may be duplicate. The data logging feature must be enabled. Otherwise, error messages are returned during the precheck and the change tracking task cannot be started. |
|   |   | Make sure that the precision settings for columns of the FLOAT or DOUBLE data type meet your business requirements. DTS uses the ROUND(COLUMN,PRECISION) function to retrieve values from columns of the FLOAT or DOUBLE data type. If you do not specify a precision, DTS sets the precision for columns of the FLOAT data type to 38 digits and the precision for columns of the DOUBLE data type to 308 digits. DTS does not track the DDL operations that are performed by using gh-ost or pt- online-schema-change. Therefore, the change tracking client may fail to write the consumed data to the destination tables due to schema conflicts. If you perform a primary/secondary switchover on the source database when the change tracking task is running, the task fails. If the source database is used in another task such as a data migration task that is running, DTS may track the data changes of other objects. In this case, you must manually filter the tracked data on the change tracking client. |
|   | Other limits |   |

Procedure
1. Create a change tracking instance.
2. Find the change tracking instance that you want to configure and click Conf igure T ask in the
Act ions column.
3. Configure the source database and network type.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that DTS automatically generates. We recommend that you specify a descriptive name that makes it easy to identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. In this example, User- Creat ed Dat abase wit h Public IP Address is selected. |
|   | Database Type | The type of the source database. The value of this parameter is set to Oracle and cannot be changed. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | Hostname or IP Address | The hostname or IP address of the self-managed Oracle database. |
|   | Port Number | The service port number of the self-managed Oracle database. |
|   | SID | The system ID (SID) of the self-managed Oracle database. |
|   | Database Account | The account of the self-managed Oracle database. Not e The account must have the database administrator (DBA) permissions. |
| ocument Versi | on: 20230625 30 |   |

|   | e tracking Data Transmission Servic |   |
|---|---|---|
| Section | Parameter | Description |
|   | Database Password | The password of the database account. |
|   | Network Type | The network type of the change tracking instance. Classic If you select Classic, no other configurations are required. VPC If you select VPC, you must configure the VPC and vSwit ch parameters. Not e If your change tracking client is deployed on a local server, you can select Classic or VPC. If you track data changes over internal networks, the network latency is minimal. |
| Consumer network type |   |   |

4. In the lower-right corner of the page, click Set Whit elist and Next .
5. Select the data change types and objects.

| Paramet er or setting | Description |
|---|---|
| Required Data Types | Dat a Updat es DTS tracks data updates of the selected objects, including the INSERT, DELETE, and UPDATE operations. Schema Updat es DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data to be tracked. Not e If you select a database as the object, DTS tracks data changes of all objects, including new objects in the database. If you select a table as the object, DTS tracks only data changes of this table. In this case, if you want to track data changes of another table, you must add the table to the selected objects. For more information, see Modify the objects for change tracking. |

| Paramet er or setting | Description |
|---|---|
| Required Objects | Select tables or databases from the Required Object s section and click the icon to move them to the Select ed section. |
| Specify the retry time range for a failed connecti on to the source databas e | The retry time range for failed connections. Valid values: 10 to 1440. Unit: minutes. Default value: 720. We recommend that you set the parameter to a value greater than 30. If DTS is reconnected to the source databases within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. |

6. In the lower-right corner of the page, click Save and Precheck.
Before you can start the change tracking task, DTS performs a precheck. You can start the change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.
7. Close the Precheck dialog box after the following message is displayed: T he precheck is passed.
After the change tracking task is configured, DTS performs initial change tracking, which takes about 1 minute. After the initial change tracking is complete, you can consume the tracked data. What's next Use a Kafka client to consume tracked data

### Manage change tracking tasks

#### Modify the consumption checkpoint

During data consumption, you can modify the consumption checkpoint of a change tracking task based on your business requirements. After you modify the consumption checkpoint, the downstream SDK client will consume the data that is generated after the specified time. Prerequisites A change tracking task is created. For more information, see Track data changes from an ApsaraDB RDS for MySQL instance, Track data changes from a PolarDB-X instance or Track data changes from a selfmanaged Oracle database. Procedure
1. Stop all downstream SDK consumption processes.
We recommend that you perform this operation during off-peak hours to avoid service interruption.
2. Log on to the DTS console.
3. In the left-side navigation pane, click Change T racking.
4. Find the change tracking task, move the pointer over the Consumpt ion Checkpoint column, and
then click the icon.
5. In the Modify Consumption Checkpoint dialog box, specify a new consumption checkpoint.
The selected time range must be within the time range of the tracked data. For more information, see the prompt in the dialog box.
6. Click Modif y.
7. Restart the downstream SDK consumption processes.
The downstream SDK client tracks data changes from the new consumption checkpoint.

#### Modify the objects for change tracking

DTS allows you to add or remove the objects for change tracking in the consumption process. This topic describes how to modify the objects for change tracking. Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. Find the change tracking task, and click Modif y Required Object s in the Act ions column.
4. In the Select Required Object s step, add or remove the objects for change tracking.
Add the objects for change tracking In the Required Object s section, select one or more objects and click the icon to add the objects to the Select ed section. Remove the objects for change tracking In the Select ed section, select one or more objects and click the icon to move the objects to the Required Object s section.
5. In the lower-right corner of the page, click Save and Precheck.
Before you can start the change tracking task, DTS performs a precheck. You can start the change tracking task only after the task passes the precheck. If the task fails to pass the precheck, click the icon next to each failed item to view details. After you troubleshoot the issues based on the causes, run a precheck again.

#### Create a consumer group

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

| r Guide·Change | tracking Data Transmission Servic |
|---|---|

| Parameter | Description |
|---|---|
| Username | Enter the username of the consumer group. A username must contain one or more of the following character types: uppercase letters, lowercase letters, digits, and underscores ( ). _ The username must be 1 to 16 characters in length. |
| Password | Enter the password that corresponds to the username of the consumer group. A password must contain two or more of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. |
| Confirm Password | Enter the new password again. |

7. Click Creat e.

#### Manage consumer groups

You can manage consumer groups of a change tracking task in the DTS console. This topic describes how to modify the password of a consumer group and how to delete a consumer group. Prerequisites Create a consumer group Procedure
1. Log on to the DTS console.
2. In the left-side navigation pane, click Change T racking.
3. On the Change Tracking page, find the change tracking task for which you want to add a consumer
group and click the task ID.
4. In the left-side navigation pane, click Consume Dat a.
5. Modify the password of a consumer group or delete a consumer group.
Modify the password of a consumer group i. On the Consume Dat a page, find the target consumer group and click Modif y Password in the Act ions column. ii. In the Modif y Password dialog box that appears, enter the old password and new password, and enter the new password again in the Conf irm Password field. A password must contain two or more of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password must be 8 to 32 characters in length. iii. Click Modif y. Delete a consumer group After a consumer group is deleted, the data in the group will be cleared and cannot be recovered. We recommend that you use caution when performing this operation. i. On the Consume Dat a page, find the target consumer group and click Delet e in the Act ions column. ii. In the Delet e Consumer Group message that appears, click OK.

### Use the SDK to consume tracked

data

#### Methods provided by SDK

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

| User Guide·Change tracking | Data Transmission Servic |
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

Methods of the ClusterListener class The `void notify(List<ClusterMessage> arg0)` method specifies the consumption mode of tracked data. When the DTS SDK receives the data, it uses the notify() function to notify a ClusterListener object to consume the data. Then, the SDK displays the data on the screen. Methods of the ClusterMessage class Each ClusterMessage object stores the data record of a transaction. Each data record in the transaction is stored by using a Record object.

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

#### Quick start

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

#### Parse tracked SQL statements

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

#### Run the SDK demo code

This topic describes how to run the SDK demo code that is provided by the Data Transmission Service (DTS) console.
1. Create an AccessKey.
Your account must pass the AccessKey authentication before you use an SDK to connect to a change tracking instance. Therefore, you must obtain an AccessKey pair before you use the SDK. For more information, see the Obt ain an AccessKey pair topic of the DTS Developer Guide.
2. Install the SDK for Java.
The development environment supported by the DTS SDK for Java is J2SE Development Kit (JDK) V1.5 or later. The following steps provide an example on how to install the SDK for Java: i. Click View Sample Code and download the SDK package consumer.jar. ii. In the following example, the jar package is imported to an Eclipse project. In Eclipse, right-click your project and select Propert ies. Click Java Build Pat h on the left, and then click the Libraries tab. Click Add Ext ernal JARs. Locate the path in which the consumer.jar file is stored and add theconsumer.jar file to the project. iii. Select the consumer.jar package and click OK. After you perform the preceding steps, you can use the SDK for Java in the project.
3. Run the SDK demo code.
DTS provides the SDK demo code. You can copy the demo code by using the View Sample Code feature in the DTS console. In the following example, the SDK demo code is run in an Eclipse project. i. Create a class named MainClass in the src directory of the Eclipse project. ii. Open the generated Java file MainClass and delete the code template. iii. Paste the demo code into the MainClass file. iv. Modify the AccessKey ID, the AccessKey secret, and the ID of the change tracking instance in the demo code. The following figure shows the sample code. Sample code Replace the marked parts in the preceding sample code with the AccessKey ID, the AccessKey secret, and the ID of the change tracking instance of your account. Log on to the DTS console to obtain the ID of the change tracking instance. In the left-side navigation pane, click Change T racking to go to the Change Tracking Tasks page. On the page that appears, find the instance that you want to manage and click the ID of the instance in the ID/Name column. v. In Eclipse, right-click the demo file and choose Run As > Java Applicat ion to run the demo code.

### Use a Kafka client to consume

tracked data This topic describes how to use the demo code of a Kafka client to consume tracked data. The change tracking feature of the new version allows you to consume tracked data by using a Kafka client from V0.11 to V1.1. Prerequisites A change tracking task is created. For more information, see Track data changes from an ApsaraDB RDS for MySQL instance, Track data changes from a PolarDB-X instance or Track data changes from a self-managed Oracle database. One or more consumer groups are created. For more information, see Create a consumer group. Precautions If you enable auto commit when you use the change tracking feature, some data may be committed before it is consumed. This results in data loss. We recommend that you manually commit data. If data fails to be committed due to a fault, you can restart the client to continue consuming data from the last recorded consumer offset. However, duplicate data may be generated during this period. You must manually filter out the duplicate data. Data is serialized and stored in the Avro format. For more information, see Record.avsc. If the client that you use is not a Kafka client, you must parse the tracked data based on the Avro schema. Regarding the `offsetFotTimes` interface, the search unit of DTS is seconds, and the search unit of native Kafka is milliseconds. Download and run the demo code of the Kafka client Click here to download the demo code of the Kafka client. Download and run the demo code of the Kafka client

| Step | File or directory |
|---|---|
| 1. Use the native Kafka consumer to obtain incremental data from the change tracking instance. | subscribe example- _ master/javaimpl/src/main/java/r ecordgenerator/ |
| 2. Deserialize the image of the incremental data, and obtain attributes such as the pre-image and post-image. | subscribe example- _ master/javaimpl/src/main/java/b oot/MysqlRecordPrinter.java |
| 3. Convert the dataTypeNumber values in the deserialized data into MySQL or Oracle data types. Not e For more information, see Mappings between MySQL data types and dataTypeNumber values and Mappings between Oracle data types and dataTypeNumber values. | subscribe example- _ master/javaimpl/src/main/java/r ecordprocessor/mysql/ |

Procedure This procedure uses IntelliJ IDEA (Community Edition 2018.1.4 Windows) as an example.
1. Download the demo code of the Kafka client, and then decompress the package.
2. Open IntelliJ IDEA. In the window that appears, click Open.
3. In the dialog box that appears, go to the directory in which the downloaded demo code resides. Find
the pom.xml file.
4. In the dialog box that appears, select Open as Project .
5. On the IntelliJ IDEA page, expand folders to find the demo file of the Kafka client, and double-click
the file. The file name is NotifyDemo.java.
6. Set the parameters in the NotifyDemo.java file.

| Parameter |   |   | Description |   |   |   |   | Method to obtain |   |
|---|---|---|---|---|---|---|---|---|---|
| USER NAME _ |   |   | The username of the consumer group. Warning If you are not using the Kafka client that is described in this topic, you must specify the username in the following format: <Consumer g |   |   |   |   | In the DTS console, click the instance ID, and then click Dat a Consume. You can obtain the Consumer Group ID and the corresponding Account information. Not e The password of the consumer group account is specified when you create a consumer group. |   |
|   |   |   |   | Warning If you are not using the Kafka client that is described in this topic, you must specify the username in the following format: <Consumer g |   |   |   |   |   |
|   |   |   |   |   | <Consumer g |   |   | and then click Dat a Consume. You |   |
|   |   |   |   | roup account>-<Consumer grou |   |   |   |   |   |
|   |   |   |   |   |   |   |   | o |   |
|   |   |   |   | p ID> |   | dtstest- |   |   |   |
| PASSWORD NAME _ |   |   | The password of the account. |   |   |   |   |   |   |
| SID NAME _ |   |   | The ID of the consumer group. |   |   |   |   |   |   |
| GROUP NAME _ |   |   | The name of the consumer group. Set this parameter to the consumer group ID. |   |   |   |   |   |   |
| KAFKA TOPIC _ |   |   | The topic of the change tracking task. |   |   |   |   | In the DTS console, click the instance ID. On the T rack Dat a Changes page, you can obtain the t racked t opic, network address, and port number. |   |
| KAFKA BROKER UR _ _ L NAME _ |   |   | The network address and port number of the change tracking task. Not e If you track data changes over internal networks, the network latency is minimal. This is applicable if the ECS instance where you deploy the Kafka client belongs to the same VPC or classic network as the change tracking instance. |   |   |   |   |   |   |

| Parameter | Description | Method to obtain |
|---|---|---|
| INITIAL CHECKPOIN _ T NAME _ | The consumer offset of consumed data. The value is a UNIX timestamp. Not e You must save the consumer offset. If the consumption process is interrupted, you can specify the consumer offset on the change tracking client to resume data consumption. This allows you to prevent against data loss. When you start the change tracking client, you can specify the consumer offset to consume data on demand. |   |
|   |   | When you use the Kafka client to track data changes for the first time, convert the required time point into a UNIX timestamp. |
| USE CONFIG CHECK _ _ POINT NAME _ | Default value: true. The default value indicates that the client is forced to consume data from the specified consumer offset. This allows you to retain the data that is received but not processed. | None. |

7. On the top of the IntelliJ IDEA page, choose Run > Run to run the client.
When you run IntelliJ IDEA for the first time, it loads and installs the relevant dependency. Execution result The following figure shows that the Kafka client can track data changes in the source database. You can also delete the `//` characters from the //log.info(ret); string in line 25 of the NotifyDemo.java file. Then, run the client again to view the data change information. Mappings between MySQL data types and dataTypeNumber values

| MySQL data type | Value of dataTypeNumber |
|---|---|
| MYSQL TYPE DECIMAL _ _ | 0 |

| ser Guide·Change tracking | Data Transmission Servic |
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

| ata Transmission Service | User Guide·Change trackin |
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

|   | User Guide·Change tracking | Data Transmission Servic | e |
|---|---|---|---|

| Oracle data type | Value of dataTypeNumber |
|---|---|
| TIMESTAMP WITH LOCAL TIME ZONE _ _ _ _ | 231 |
