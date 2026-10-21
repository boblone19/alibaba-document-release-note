---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 222
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Cloud%20Native%20Distributed%20Database%20PolarDB-X%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Cloud Native Distributed Database PolarDB-X User Guide 20220928

## Table of Contents

- 1 What is PolarDB-X?
- 2 Quick start
- 3 Log on to the PolarDB-X console
- 4 Instance management
  - 4.1 Create a PolarDB-X instance
  - 4.2 Change specifications
  - 4.3 Read-only PolarDB-X instances
    - 4.3.1 Overview
    - 4.3.2 Create a read-only PolarDB-X instance
    - 4.3.3 Manage a read-only PolarDB-X instance
    - 4.3.4 Release a read-only PolarDB-X instance
  - 4.4 Restart a PolarDB-X instance
  - 4.5 Release a PolarDB-X instance
  - 4.6 Recover data
    - 4.6.1 Backup and recovery
    - 4.6.2 Configure an automatic backup policy
    - 4.6.3 Configure local logs
    - 4.6.4 Manual backup
    - 4.6.5 Recover data
    - 4.6.6 SQL flashback
      - 4.6.6.1 Overview
      - 4.6.6.2 Generate a recovery file
      - 4.6.6.3 Rollback SQL statements and original SQL statements
      - 4.6.6.4 Exact match and fuzzy match
    - 4.6.7 Table recycle bin
      - 4.6.7.1 Overview
      - 4.6.7.2 Enable the table recycle bin
      - 4.6.7.3 Recover tables
      - 4.6.7.4 Delete tables from the recycle bin
      - 4.6.7.5 Disable the table recycle bin
  - 4.7 Set parameters
  - 4.8 SQL audit and analysis
    - 4.8.1 Description
    - 4.8.2 Enable SQL audit and analysis
    - 4.8.3 Log fields
    - 4.8.4 Log analysis
    - 4.8.5 Log reports
  - 4.9 Monitor PolarDB-X instances
    - 4.9.1 View monitoring information
    - 4.9.2 Monitoring metrics
    - 4.9.3 How metrics work
    - 4.9.4 Prevent performance problems
      - 4.9.4.1 Example 1: PolarDB-X CPU utilization
      - 4.9.4.2 Example 2: Logical RT and physical RT
      - 4.9.4.3 Example 3: Logical QPS and physical QPS
      - 4.9.4.4 Example 4: High memory usage
  - 4.10 View the instance version
- 5 Account management
  - 5.1 Basic concepts
  - 5.2 Create an account
  - 5.3 Reset password
  - 5.4 Modify account permissions
  - 5.5 Delete an account
- 6 Database management
  - 6.1 Create a database
  - 6.2 View a database
  - 6.3 Perform smooth scale-out
  - 6.4 View database monitoring information
  - 6.5 Set the IP address whitelist
  - 6.6 Delete a database
  - 6.7 Fix database shard connections
- 7 Custom control commands
  - 7.1 Overview
  - 7.2 Help statements
  - 7.3 Statements for viewing rules and node topologies
  - 7.4 SQL tuning statements
  - 7.5 Statistics query statements
  - 7.6 SHOW PROCESSLIST and KILL commands
  - 7.7 SHOW PROCESSLIST and KILL commands in earlier versions
- 8 Custom hints
  - 8.1 Introduction to hints
  - 8.2 Read/write splitting
  - 8.3 Specify a timeout period for an SQL statement
  - 8.4 Specify a database shard to run an SQL statement
  - 8.5 Scan all or some of database shards and table shards
  - 8.6 INDEX HINT
- 9 PolarDB-X 5.2 hints
  - 9.1 Introduction to hints
  - 9.2 Read/write splitting
  - 9.3 Prevent the delay from a read-only ApsaraDB RDS for MySQL instance
  - 9.4 Specify a timeout period for an SQL statement
  - 9.5 Specify a database shard to run an SQL statement
  - 9.6 Scan all database shards and table shards
- 10 Distributed transactions
  - 10.1 Distributed transactions based on MySQL 5.7
  - 10.2 Distributed transactions based on MySQL 5.6
- 11 DDL operations
  - 11.1 DDL statements
  - 11.2 CREATE TABLE statement
    - 11.2.1 Overview
    - 11.2.2 Create a single-database non-partition table
    - 11.2.3 Create a non-partition table in database shards
    - 11.2.4 Create table shards in database shards
    - 11.2.5 Use the primary key as the shard key
    - 11.2.6 Create a broadcast table
    - 11.2.7 Other attributes of the MySQL CREATE TABLE statement
  - 11.3 ALTER TABLE statement
  - 11.4 DROP TABLE statement
  - 11.5 FAQ about DDL statements
  - 11.6 DDL functions for sharding
    - 11.6.1 Overview
    - 11.6.2 HASH
    - 11.6.3 UNI_HASH
    - 11.6.4 RIGHT_SHIFT
    - 11.6.5 RANGE_HASH
    - 11.6.8 WEEK
    - 11.6.9 MMDD
    - 11.6.10 YYYYMM
    - 11.6.11 YYYYWEEK
    - 11.6.12 YYYYDD
    - 11.6.13 YYYYMM_OPT
    - 11.6.14 YYYYWEEK_OPT
    - 11.6.15 YYYYDD_OPT
- 12 Automatic protection of high-risk SQL statements
- 13 PolarDB-X sequence
  - 13.1 Overview
  - 13.2 Explicit sequence usage
  - 13.3 Implicit sequence usage
  - 13.4 Limits and precautions for sequences
- 14 Best practices
  - 14.1 Select a shard key
  - 14.2 Select the number of shards
  - 14.3 Basic concepts of SQL optimization
  - 14.4 SQL optimization methods
    - 14.4.1 Overview
    - 14.4.2 Single-table SQL optimization
    - 14.4.3 JOIN query optimization
    - 14.4.4 Subquery optimization
  - 14.5 Select connection pools for an application
  - 14.6 Connections to PolarDB-X instances
  - 14.7 Perform instance upgrade
  - 14.8 Perform scale-out
  - 14.9 Troubleshoot slow SQL statements in PolarDB-X
    - 14.9.1 Details about a low SQL statement
    - 14.9.2 Locate slow SQL statements
    - 14.9.3 Locate nodes with performance loss
    - 14.9.4 Troubleshoot the performance loss
  - 14.10 Handle DDL exceptions
  - 14.11 Efficiently scan PolarDB-X data
- 15 Appendix: PolarDB-X terms

## 1 What is PolarDB-X?

Cloud Native Distributed Database PolarDB-X is a middleware service independently developed by Alibaba Group for scale-out of single-instance relational databases. It is compatible with Distributed Relational Database Service (DRDS). Compatible with the MySQL protocol, PolarDB-X 1.0 supports most MySQL data manipulation language (DML) and data definition language (DDL) syntax. It provides the core capabilities of distributed databases, such as database sharding, table sharding, smooth scaleout, configuration changing, and transparent read/write splitting. PolarDB-X features lightweight (stateless), flexibility, stability, and high efficiency, and provides you with O&M capabilities throughout the lifecycle of distributed databases. PolarDB-X 1.0 is mainly used for operations on large-scale online data. By partitioning data in specific business scenarios, PolarDB-X maximizes the operation efficiency, meeting the requirements of online businesses on relational databases. Problems solved Capacit y bot t leneck of single-inst ance dat abases: As the data volume and access volume increase, traditional single-instance databases encounter great challenges that cannot be completely solved by hardware upgrades. Distributed solutions use multiple instances to work jointly, effectively resolving the bottlenecks of data storage capacity and access volumes. Dif f icult scale-out of relat ional dat abases: Due to the inherent attributes of distributed databases, data can be stored to different shards through smooth data migration, supporting the dynamic scale-out of relational databases.

## 2 Quick start

This topic describes how to get started with Cloud Native Distributed Database PolarDB-X. A PolarDB-X 1.0 instance is physically a distributed cluster that consists of multiple PolarDB-X 1.0 server nodes and underlying storage instances. A PolarDB-X 1.0 database is a logical concept and only contains metadata. Specific data is stored in the physical database of the underlying storage instance. To get started with PolarDB-X 1.0, follow these steps:
1. Create a PolarDB-X instance.
2. Create a database.
To create a database in a PolarDB-X 1.0 instance, you must select one or more ApsaraDB RDS for MySQL instances as the data storage nodes. If no RDS instance exists, create one first. For more information about how to create and manage ApsaraDB RDS for MySQL instances, see User Guide o f RDS .
3. After a PolarDB-X 1.0 database is created, you also need to create tables in the PolarDB-X 1.0
database like in a single-instance database. However, the syntax is different, mainly in the expression of data partitioning information in the PolarDB-X 1.0 table creation statement. For more information about how to create a table, see Table creation syntax. console

## 3 Log on to the PolarDB-X console

console This topic describes how to log on to the Cloud Native Distributed Database PolarDB-X console by using Google Chrome. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

> Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click Log On.
4. In the top navigation bar, choose Product s > Dist ribut ed Relat ional Dat abase Service.

## 4 Instance management

### 4.1 Create a PolarDB-X instance

To use PolarDB-X 1.0, you must first create an instance. This topic describes how to create a PolarDB-X 1.0 instance.
1. Log on to the PolarDB-X console.
2. On the page that appears, click Creat e Inst ance in the upper-right corner.
3. On the Creat e DRDS Inst ance page, set parameters as required.
describes the parameters. Parameters for creating a PolarDB-X instance

| Type | Parameter | Description |
|---|---|---|
| Region | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
|   | Region | The region where the instance resides. Services in different regions are not interconnected over the internal network. After the instance is created, the region cannot be changed. |
|   | Zone | The zone where the instance resides. |
| Basic Set t ings | Inst ance T ype | The type of the instance. Select an instance type from the options available on the page. |
|   | Inst ance Edit ion | The edition of the instance. Valid values: Standard Enterprise Starter |
|   | Inst ance Specif icat ions | The specifications of the instance. The rules vary with instance editions. Select the instance specifications from the options available on the page. |

| Type | Parameter | Description |
|---|---|---|
| Net work | Net work T ype | The network type of the instance. PolarDB-X 1.0 instances support the following network types: Classic Net work: Cloud services on a classic network are not isolated from each other. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize routing tables, IP address ranges, and gateways in a VPC. We recommend that you select VPC for higher security. Select VPC for Network Type, and then set VPC and VSwit ch. Not e Make sure that the PolarDB-X 1.0 instance has the same network type as the Elastic Compute Service (ECS) instance to which you want to connect. If the PolarDB-X and ECS instances have different network types, they cannot communicate over an internal network. |
| T ype |   |   |

4. Click Submit .
After the instance is created, it appears in the instance list and its status changes to Running. An instance name uniquely identifies a PolarDB-X 1.0 instance.

### 4.2 Change specifications

When you use PolarDB-X 1.0, you can change the specifications of a PolarDB-X 1.0 instance as needed. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. On the Basic Information page, click Upgrade or Downgrade in the Common Operat ions section
to access the Change Specifications page.

> Not e Alternatively, on the DRDS Inst ance Management page, choose More > Downgrade from the Act ions column of the target instance.

5. On the Change Specifications page, set Instance Edition and Instance Specifications, and then click
Submit . After a few minutes, you can view the new specifications of the instance in the instance list.

> Not e Specifications downgrade leads to transient disconnections between applications and PolarDB-X 1.0 within a short period of time. Make sure that your applications can be automatically reconnected.

### 4.3 Read-only PolarDB-X instances

#### 4.3.1 Overview

Read-only PolarDB-X 1.0 instances are extension and supplement to primary PolarDB-X 1.0 instances and are compatible with SQL query syntax of primary PolarDB-X 1.0 instances. Features Read-only and primary PolarDB-X 1.0 instances can share the same replica of data. You can perform complex data query and analysis directly on read-only or primary ApsaraDB RDS for MySQL instances. Multiple instance types are provided to handle highly concurrent access requests and reduce the response time (RT) for complex queries. Resource isolation alleviates the load pressure on the primary instances and reduces the link complexity of the business architecture. It reduces the O&M and budget costs, eliminating the need for additional data synchronization. Instance type Concurrent read-only inst ances: For high-concurrency and high-traffic simple queries or offline data extraction, resource isolation protects you against highly concurrent queries, ensuring the stability of online business links.

> Not e For the businesses with primary PolarDB-X 1.0 instances, concurrent read-only instances can be used in the following scenarios:
> High-concurrency and high-traffic simple queries are performed.
> Data is extracted offline.

Limits Primary and read-only PolarDB-X 1.0 instances must be in the same region, but they can be in different zones. A read-only PolarDB-X 1.0 instance must belong to a primary PolarDB-X 1.0 instance. Before creating a read-only instance, you must create a primary instance. After you create a database on the primary instance, the database is replicated to the read-only instance. If you delete the database from the primary instance, the corresponding database on the read-only instance is also deleted. You are not allowed to migrate data to read-only PolarDB-X 1.0 instances. You are not allowed to create or delete databases in PolarDB-X 1.0 read-only instances. PolarDB-X 1.0 read-only instances cannot be cloned. PolarDB-X 1.0 read-only instances support data definition language (DDL) statements but do not support data manipulation language (DML) statements for data modification.

#### 4.3.2 Create a read-only PolarDB-X instance

This topic describes how to create a read-only Cloud Native Distributed Database PolarDB-X (PolarDB- X) instance. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. On the Basic Information page, click Creat e DRDS Read-only Inst ance in the Related Instances
section.
5. Set Region, Basic Settings, and Network Type, and then click Submit .
Parameters for creating a read-only PolarDB-X instance

| Type | Parameter | Description |
|---|---|---|
| Region | Region | The region where the read-only instance resides. Services in different regions are not interconnected over the internal network. After the instance is created, the region cannot be changed. |
|   | Zone | The zone where the read-only instance resides. |
| Basic Set t ings | Inst ance T ype | The type of the read-only instance. Select an instance type from the options available on the page. |
|   | Inst ance Edit ion | The edition of the read-only instance. Valid values: Starter Standard Enterprise |
|   | Inst ance Specif icat ions | The specifications of the read-only instance. The rules vary with instance editions. Select the instance specifications from the options available on the page. |
|   | Descript io n | The description of the read-only instance. We recommend that you provide an informative description to simplify future management operations. |
| Net work T ype | Net work T ype | The network type of the read-only instance. PolarDB-X 1.0 instances support the following network types: Classic Net work: Cloud services on a classic network are not isolated from each other. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize routing tables, IP address ranges, and gateways in a VPC. We recommend that you select VPC for higher security. Select VPC for Network Type, and then set VPC and VSwit ch. Not e Make sure that the PolarDB-X 1.0 instance has the same network type as the Elastic Compute Service (ECS) instance to which you want to connect. If the PolarDB-X and ECS instances have different network types, they cannot communicate over an internal network. |

6. It takes several minutes to create the instance. Please wait. After the instance is created, it appears
in the instance list in the PolarDB-X 1.0 console.

#### 4.3.3 Manage a read-only PolarDB-X instance

Read-only PolarDB-X 1.0 instances are managed in a similar way as primary instances. However, databases cannot be created or deleted on the read-only instance management page. Databases on read-only instances are created or deleted with databases on primary instances. In the PolarDB-X 1.0 console, you can go to the read-only instance management page in two ways. Manage a read-only PolarDB-X instance by its ID
1. Log on to the PolarDB-X console.
2. On the DRDS Inst ance Management page, find the target read-only instance.
3. Click the target instance ID or choose More > Manage from the Actions column of the target
read-only instance to access the Basic Inf ormat ion page. Manage a read-only PolarDB-X instance by the ID of its primary instance
1. Log on to the PolarDB-X console.
2. On the DRDS Inst ance Management page, find the target primary instance.
3. Click the target instance ID or choose More > Manage from the Actions column of the target
primary instance to access the Basic Inf ormat ion page.
4. On the Basic Inf ormat ion page, move the pointer over the number of read-only instances in the
Relat ed Inst ances section to view the ID of the read-only PolarDB-X instance.
5. Click the ID of the target read-only PolarDB-X instance. The Basic Inf ormat ion page of the read-
only instance appears.

#### 4.3.4 Release a read-only PolarDB-X instance

If you no longer need a read-only PolarDB-X 1.0 instance, you can release it. Prerequisites The read-only instance must be in the Running state. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. In the PolarDB-X instance list, find the target instance, and choose More > Release from the
Actions column.

> Not ice You cannot recover the PolarDB-X instances that have been released. Exercise caution when you perform this operation.

4. In the Release DRDS Inst ance dialog box, click OK.

### 4.4 Restart a PolarDB-X instance

This topic describes how to restart a PolarDB-X 1.0 instance. Prerequisites The PolarDB-X instance must be in the Running state. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. Click Rest art Inst ance in the upper-right corner.
5. In the Rest art Inst ance dialog box, click OK.

> Not ice Restarting a PolarDB-X instance terminates all its connections. Make appropriate service arrangements before you restart a PolarDB-X instance. Exercise caution when you perform this operation.

### 4.5 Release a PolarDB-X instance

This topic describes how to release a running PolarDB-X instance in the PolarDB-X 1.0 console. Prerequisites All databases on the PolarDB-X instance have been deleted. The PolarDB-X instance must be in the Running state. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. In the PolarDB-X instance list, find the target instance, and choose More > Release from the
Actions column.
4. In the Release DRDS Inst ance dialog box, click OK.

> **Warning:** After the PolarDB-X instance is released, data is not deleted from its attached ApsaraDB RDS for MySQL instances. However, a released PolarDB-X instance cannot be restored. Exercise caution when you perform this operation.

### 4.6 Recover data

#### 4.6.1 Backup and recovery

PolarDB-X 1.0 allows you to back up data of instances and databases and recover them by using the backup data. Instances can be automatically and manually backed up in a quick or consistent manner. The instance recovery capability restores data to the new PolarDB-X 1.0 and ApsaraDB RDS for MySQL instances based on the existing backup set. Backup methods For different scenarios, PolarDB-X 1.0 provides quick backup and consistent backup, as well as corresponding recovery capabilities. The following table compares the two backup methods.

| Method | Scenario | Advantage | Disadvantage |
|---|---|---|---|
| Quick backup | It applies to routine backup and recovery scenarios. | It provides faster data backup and recovery. It supports recovery at any time based on backup sets. It supports all PolarDB-X 1.0 instance versions. | It ensures data consistency only at a single ApsaraDB RDS for MySQL instance but not global data consistency in database and table sharding scenarios. |
| Consistent backup | It applies to backup and recovery for online core transaction businesses and the financial industry with a high- consistency requirement. | It ensures global data consistency in database and table sharding scenarios. | It provides slower backup and recovery. It supports recovery based on backup sets but not at any time. It is supported only for PolarDB-X 1.0 5.3.8 and later. During the backup, distributed transactions are locked within seconds for PolarDB- X 1.0 instances. During the locking process, SQL execution response time (RT) may vary by milliseconds. Therefore, we recommend that you perform consistent backup during off- peak hours. |

Limits The PolarDB-X 1.0 automatic backup policy is disabled by default. You must manually enable it. The log backup capability of PolarDB-X 1.0 depends on underlying ApsaraDB RDS for MySQL instances. Therefore, the log backup policy configured in the PolarDB-X 1.0 console is automatically synchronized to all underlying ApsaraDB RDS for MySQL instances. After the policy is configured, do not modify it in the ApsaraDB for RDS console. The backup and recovery feature of PolarDB-X 1.0 depends on log backups. We recommend that you enable the log backup policy by default to avoid invalid backup sets. Data definition language (DDL) operations cannot be performed during the backup process. During the backup, the underlying ApsaraDB RDS for MySQL instances of the PolarDB-X 1.0 instance must be normal to avoid a backup failure. Consistent backup and recovery is only supported by PolarDB-X 1.0 5.3.8 and later versions. All tables must have primary keys to ensure data accuracy during data backup and recovery. During consistent backup, distributed transactions are locked within seconds for PolarDB-X 1.0 instances. During the locking process, the execution of non-transactional SQL statements and singleinstance transactions are not affected, but the committing of distributed transactions is blocked and the SQL execution RT may vary by milliseconds. We recommend that you perform consistent backup during off-peak hours. Due to the inventory of PolarDB-X 1.0 and ApsaraDB RDS for MySQL, PolarDB-X 1.0 automatically adjusts the instance type and zone during instance recovery. We recommend that you confirm and adjust the instance type and zone after recovery.

#### 4.6.2 Configure an automatic backup policy

PolarDB-X 1.0 provides the automatic backup feature. This topic describes how to configure an automatic backup policy. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > Backup and Recovery.
5. On the page that appears, choose Backup Policy > Edit .
6. In the Backup Policy dialog box, set parameters as needed, and click OK.

#### 4.6.3 Configure local logs

You can use local logs with the backup and recovery feature or the SQL flashback feature of PolarDB-X 1.0 to accurately recover an instance or a database to the desired time point. This topic describes how to configure local logs. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > Backup and Recovery.
5. On the page that appears, click the Local Log Set t ings tab and then click Edit .
6. In the Local Binlog Set t ings dialog box, set parameters as needed, and click OK.

> Not ice The local log settings are applied to all underlying ApsaraDB RDS for MySQL instances.

#### 4.6.4 Manual backup

PolarDB-X 1.0 also provides the manual backup capability, so that you can back up data at any time. This topic describes how to manually back up instances and databases. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > Backup and Recovery.
5. On the page that appears, click Dat a Backup on the right.
6. In the dialog box that appears, set Backup Method and Backup Level.
Backup Method can be set to Fast Backup and Consist ent Backup. For more information about differences between the two methods, see Backup methods.

> Not ice If you select Consistent Backup, distributed transactions are locked within seconds and the response time (RT) may vary by sub-seconds. Therefore, we recommend that you perform this operation during off-peak hours.

Backup Level can be set to Inst ance Backup or Dat abase Backup. You can select Inst ance Backup to back up the entire instance, or select Dat abase Backup to back up a database as needed.
7. Click OK.

#### 4.6.5 Recover data

You can use the data recovery feature of PolarDB-X 1.0 to recover an instance or a database to the time when the backup is created. You can perform this operation at any time. This topic describes how to recover the data of an instance or a database to a specific point in time. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > Backup and Recovery.
5. On the page that appears, click Dat a Recovery (Original Clone Inst ance) on the right.
6. Select a recovery method
By T ime: Recover data to the selected point in time. You must set Rest orat ion T ime and Recovery Level. By Backup Set : Recover data from the selected backup file.

> Not e You can also click Recover in the Actions column of the target backup set to recover data by backup set

7. Click Precheck to check whether a valid backup set is available for data recovery. If the precheck
fails, the data cannot be restored.
8. Click Enable to access the order confirmation page.
9. Confirm the order details and then click Enable to recover the data. You can view the data
recovery progress in T ask Progress in the upper-right corner of the page.

#### 4.6.6 SQL flashback

##### 4.6.6.1 Overview

PolarDB-X 1.0 provides the SQL flashback feature to recover data of particular rows. When you mistakenly run an SQL statement such as INSERT, UPDATE, or DELETE on PolarDB-X 1.0, provide the relevant SQL information to match the event in the binary log file and generate the corresponding recovery file. You can download the file and recover data as needed. SQL flashback automatically chooses f uzzy mat ch or exact mat ch to locate lost data caused by the error. For more information, see Exact match and fuzzy match and Rollback SQL statements and original SQL statements. Features Easy-to-use: SQL flashback allows you to retrieve the lost data by entering required information about the corresponding SQL statement. Fast and lightweight: Regardless of the backup policy of ApsaraDB RDS for MySQL instances, you only need to enable log backup before an SQL statement error occurs. Flexible recovery: Rollback SQL statements and original SQL statements are available for different scenarios. Exact match: SQL flashback supports exact match of data about the corresponding SQL statement, which improves precision of data recovery. Limits SQL flashback depends on the binary log retention time and the log backup feature of ApsaraDB RDS for MySQL must be enabled. Binary log files can be retained only for a certain period. Use SQL flashback to generate files for recovery as soon as possible when an error occurs. The recovery files generated by SQL flashback are retained for seven days by default, and you need to download these files as soon as possible. The following conditions must be met for SQL flashback exact match: The PolarDB-X 1.0 instance version is 5.3.4-15378085 or later. The version of the ApsaraDB RDS for MySQL instance used by the PolarDB-X 1.0 database is 5.6 or later. SQL flashback exact match is enabled before the error SQL statement is executed. The TRACE_ID information for the error SQL statement is provided. To ensure the precision of data recovery, the exact match feature is enabled by default for the database created in a PolarDB-X 1.0 instance of 5.3.4-15378085 or later. After this feature is enabled, SQL execution information is included in the binary log file by default, which requires more storage space for ApsaraDB RDS for MySQL instances. If you need to use the exact match feature, we recommend that you upgrade PolarDB-X 1.0 before enabling the feature. For more information, see Enable exact match.

##### 4.6.6.2 Generate a recovery file

Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > SQL Flashback. The SQL Flashback
page appears.
5. On the SQL Flashback page, enter the basic information about a mistaken SQL statement,
including Database, Time Range, Table Name, TRACE_ID, and SQL Statement Type. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Database | The database where the mistaken SQL statement was executed. |
| Time Range | The time range during which the mistaken SQL statement was executed. The start time is earlier than the start time when the mistaken SQL statement was executed, whereas the end time is later than the time when the execution of the mistaken SQL statement ended. To ensure efficient recovery, we recommend that you limit the time range to five minutes. |
| Table Name | The name of the table on which the mistaken SQL statement was executed. This parameter is optional. |
| TRACE ID _ | The unique TRACE ID that PolarDB-X 1.0 allocates for each executed SQL _ statement. You can obtain the TRACE ID of the mistaken SQL statement by using _ the SQL audit feature of PolarDB-X 1.0. |
| SQL Statement Type | The type of the mistaken SQL statement. Valid values: INSERT UPDATE DELETE |

6. Click Precheck. The system checks whether a binary log file exists within the specified time range.
For more information about binary log files, see Configure local logs.

> Not e
> If no binary log file exists within specified the time range, the precheck fails and the system cannot recover the data for you.
> If a binary log file exists within the specified time range, the precheck is successful and you can go to the next step.

7. Set SQL Statement Type for Recovery to Rollback SQL or Original SQL St at ement . For more
information about differences between the two methods, see Rollback SQL statements and original SQL statements.
8. Click Generat e SQL to generate an SQL flashback task. The statuses of the SQL flashback tasks
that are running on the current instance appear at the bottom of the page. What's next After an SQL flashback task is completed, the task information such as the exact match status and the number of recovered rows appears. You can click Download next to the target SQL flashback task to download the corresponding recovery file.

> Not ice By default, the recovery file is retained for seven days. Download it as soon as possible.

##### 4.6.6.3 Rollback SQL statements and original SQL statements

statements To support different business scenarios, PolarDB-X 1.0 SQL flashback provides rollback SQL statements and original SQL statements. Before generating an SQL statement for recovering data, you must select a corresponding recovery method based on your scenario. Recovery methods

| Recovery method | Description | Example |
|---|---|---|

| Recovery method | Description | Example |
|---|---|---|
| Rollback SQL statement | Traverses the events in the binary log file in reverse order to reverse the INSERT, UPDATE, and DELETE events. The reverse of INSERT is equivalent to DELETE. The reverse of DELETE is equivalent to INSERT. The reverse of UPDATE is equivalent to the value before UPDATE. | UPDATE Employee SET title = 'Developer' WHERE emp id = '5' _ UPDATE Employee SET title = 'Designer' WHERE emp id = '4' _ |
| Original SQL statement | Traverses the events in the binary log file in order to mirror all records of the INSERT, UPDATE, and DELETE events. An INSERT mirror is equivalent to INSERT. A DELETE mirror is equivalent to INSERT. An UPDATE mirror is equivalent to the value before INSERT. | INSERT INTO Employee(emp id,emp name,titl _ _ e,leader id) _ values('4','Mary','Designer','2') INSERT INTO Employee(emp id,emp name,titl _ _ e,leader id) _ values('5','Ralph','Developer','2') |

##### 4.6.6.4 Exact match and fuzzy match

SQL flashback supports exact mat ch and f uzzy mat ch for binary log events. You do not need to select a match policy. SQL flashback automatically detects and selects the optimal match policy, and notifies you when the flashback task is completed.

| Match mode | Description | Advantage | Disadvantage |
|---|---|---|---|

| Match mode | Description | Advantage | Disadvantage |
|---|---|---|---|
| Exact match | The system performs exact match on the event of a mistaken SQL statement in the binary log file and generates a recovery file. | The recovery file contains only data that is deleted or modified by the mistaken SQL statement. You can use the file directly to ensure the precision and efficiency of data recovery. | The following requirements must be met: The PolarDB-X 1.0 instance is Version 5.3.4-15378085 or later. The version of the ApsaraDB RDS for MySQL instance used by the PolarDB-X 1.0 database is Version 5.6 or later. You have enabled exact match of SQL flashback before the mistaken SQL statement is executed. You must provide the TRACE ID of the _ mistaken SQL statement. |
| Fuzzy match | The system matches the information about the mistaken SQL statement in the binary log file, including the time range, table name, and SQL statement type. Then, the system generates a recovery file. | Fuzzy match is supported for all instances, regardless of the instance version or parameter settings. | Data that is deleted or modified by the mistaken SQL statement cannot be accurately matched. The recovery file contains data changes made by other business SQL operations. You must filter the required data. |

Enable exact match

> Not e Fuzzy match is enabled by default.

1. Log on to PolarDB-X 1.0console, and go to the parameter settings page of the specified instance.
For more information, see Set parameters.
2. Change the value of ENABLE_SQL_FLASHBACK_EXACT _MAT CH to ON.

#### 4.6.7 Table recycle bin

##### 4.6.7.1 Overview

The table recycle bin of PolarDB-X 1.0 allows you to recover mistakenly deleted tables. After the table recycle bin is enabled for your PolarDB-X 1.0 database, the tables that are deleted by using the DROP TABLE statement are moved to the recycle bin and are no longer visible to you. After the tables are moved to the recycle bin for two hours, they are automatically cleared and cannot be recovered. You can view, recover, and clear the deleted tables in the recycle bin. Limits and notes The table recycle bin feature is only supported by PolarDB-X 1.0 5.3.3-1670435 and later. For more information, see View the instance version. The table recycle bin is disabled for your PolarDB-X 1.0 database by default. For more information about how to enable it, see Enable the table recycle bin. The table recycle bin of PolarDB-X 1.0 does not support the recovery of tables deleted by the TRUNCATE TABLE command. Tables in the recycle bin still occupy the storage space of ApsaraDB RDS for MySQL before they are automatically cleared. To release the storage space as soon as possible, you can access the recycle bin to manually delete them.

##### 4.6.7.2 Enable the table recycle bin

This topic describes how to enable the table recycle bin. Prerequisites An ApsaraDB RDS for MySQL database has been created in the PolarDB-X 1.0 instance. For more information, see Create a database. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > T able Recycle Bin. The T able
Recycle Bin page appears.
5. At the top of the T able Recycle Bin page, click the tab of the database for which the table
recycle bin needs to be enabled.
6. Click Enabled.
7. In the dialog box that appears, click OK.

##### 4.6.7.3 Recover tables

This topic describes how to recover your tables from the table recycle bin. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > T able Recycle Bin. The T able
Recycle Bin page appears.
5. At the top of the T able Recycle Bin page, click the tab of the database for which you want to
recover a table.
6. Click Recover in the Act ions column of the target table.

##### 4.6.7.4 Delete tables from the recycle bin

This topic describes how to delete unnecessary tables from the table recycle bin. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > T able Recycle Bin. The T able
Recycle Bin page appears.
5. At the top of the T able Recycle Bin page, click the tab of the database in which you want to
clear a table.
6. Click Delet e in the Act ions column of the target table.

> Not e To clear all tables from the table recycle bin, click Empt y Recycle Bin on the tab of the corresponding database.

##### 4.6.7.5 Disable the table recycle bin

If you no longer need the table recycle bin, you can disable it. This topic describes how to disable the table recycle bin. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Dat a Recovery > T able Recycle Bin. The T able
Recycle Bin page appears.
5. At the top of the T able Recycle Bin page, click the tab of the database for which the table
recycle bin needs to be disabled.
6. Click Disable to disable the table recycle bin for the database.

### 4.7 Set parameters

PolarDB-X 1.0 allows you to set parameters for instances and databases. You can view and modify parameter values in the PolarDB-X 1.0 console as needed.

> Not e You cannot set parameters for read-only instances.

Procedure
1. Log on to the PolarDB-X console.
2. On the DRDS Inst ance Management page, find the target instance.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Diagnost ics and Opt imizat ion > Paramet er Set t ings.
Click the Instance or Database tab to view parameters that you can modify for instances and databases, respectively. For more information about the parameters, see Description.
5. Click
next to the parameter you want to modify, enter the target value, and then click OK.
6. Click Submit in the upper-right corner to commit the new value.

> Not e To undo parameter modification, click Cancel in the upper-right corner.

Description

| Parameter | Level | Description |
|---|---|---|
| Slow SQL threshold | Instance | The threshold for slow SQL statements. SQL statements whose thresholds exceed this threshold are recorded in logical slow SQL logs. |
| Logical idle link timeout | Instance | The logical timeout period of the idle connection between user applications and PolarDB-X 1.0 (unit: ms). |
| Maximum package size | Instance | The maximum network packet for the interaction between user applications and PolarDB-X 1.0 (unit: byte). |
| Instance memory pool size limit | Instance | The maximum size of the memory pool for an instance. If the memory usage on an instance exceeds the value, an error is reported and the query ends. |
| Whether to prohibit all table deletion/update | Database | Specifies whether to disable all table deletion or update. |
| Whether to open the recycle bin | Database | Specifies whether to enable the recycle bin for storing deleted logical tables of PolarDB-X 1.0. |
| Temporary table size | Database | The size of the temporary table used during distributed queries in PolarDB-X 1.0 (unit: row). |
| Number of join tables | Database | The maximum number of table shards that can be combined by JOIN when you query multiple table shards in a database. |

| C P | loud Native Distribute olarDB-X | d Database | User Guide·Instance managemen | t |
|---|---|---|---|---|

| Parameter | Level | Description |
|---|---|---|
| Physical SQL timeout | Database | The timeout period of SQL statements for interaction between PolarDB-X 1.0 and ApsaraDB RDS for MySQL (unit: ms). The value 0 indicates the timeout period is not limited. |
| SQL exact flashback switch | Database | Specifies whether to support SQL flashback exact match. It is disabled by default. After it is enabled, information about query execution is added to the binary log file used by the PolarDB-X 1.0 database. |
| Whether to enable logical INFORMATION SCH _ EMA query | Database | Specifies whether to enable logical INFORMATION SCHEMA _ query (not relying on the shadow database but returning the aggregation results of logical databases and tables). When it is disabled, the original status is restored (relying on the shadow database and returning the physical database and table information). |
| Transaction log cleanup start time period | Database | The period during which transaction log cleanup starts at a random time. |
| Library-level memory pool size limit | Database | The maximum size of the database-level memory pool. When the memory usage of a PolarDB-X 1.0 database exceeds this value, an error is reported and the query terminates. The value - 1 indicates no limit. |
| Query-level memory pool size limit | Database | The maximum size of the query-level memory pool. When the memory usage of a query exceeds this value, an error is reported and the query terminates. The value -1 indicates no limit. |
| Whether CBO is enabled | Database | Specifies whether to enable the cost-based optimizer (CBO), including features such as Join Reorder and Hash Join. |
| Default degree of parallelism | Database | It controls whether to start Parallel Query, and the degree of parallelism after Parallel Query is started. This parameter takes effect only when CBO is enabled. The value -1 indicates that the policy is automatically selected. The value 0 indicates that the policy is disabled. |
| Whether to enable the asynchronous DDL engine | Database | Specifies whether to enable the data definition language (DDL) engine. If you disable it, the execution logic of the original DDL engine remains. |
| Whether to enable pure asynchronous- mode under asynchronous DDL engine | Database | Specifies whether to enable the asynchronous-only mode when the asynchronous DDL engine is enabled. Enabled: The execution status is returned immediately after the client connects to PolarDB-X 1.0 and executes the DDL statement. Only asynchronous DDL management statements can be used to view the execution status. Disabled: The synchronous mode remains. Specifically, the execution status is returned only after the client completes executing the DDL statement. |

| Parameter | Level | Description |
|---|---|---|
| Maximum number of physical tables allowed to be created in a single physical database | Database | The maximum number of table shards that can be created in a database shard. If both database shards and table shards exist, the number of table shards cannot exceed this value. |
| INFORMATION SCH _ EMA.TABLES queries whether statistics are aggregated | Database | Specifies whether to aggregate statistics of INFORMATION SCHEMA.TABLES queries. To ensure the _ performance, the statistics are not aggregated by default. |
| Maximum number of physical sharding links | Database | The maximum number of connections between PolarDB-X 1.0 and a single ApsaraDB RDS for MySQL database shard. |
| Minimum number of physical sharding links | Database | The minimum number of connections between PolarDB-X 1.0 and a single ApsaraDB RDS for MySQL database shard. |
| Physical idle link timeout | Database | The idle time of the connection between PolarDB-X 1.0 and ApsaraDB RDS for MySQL (unit: minute). |

### 4.8 SQL audit and analysis

#### 4.8.1 Description

Cloud Native Distributed Database PolarDB-X (PolarDB-X) combines the SQL audit and analysis feature with Log Service (SLS). This feature not only audits historical SQL records, but also provides real-time diagnosis and analysis of SQL execution status, performance metrics, and security risks. You can enable SQL audit and analysis in the PolarDB-X console. Benefits Easy operation: SQL audit and analysis can be enabled with easy configuration to help you audit and analyze SQL logs in real time. Lossless performance: Pulling SQL log files from PolarDB-X nodes and uploading these logs to SLS in real time does not affect instance performance. Trace to historical issues: This feature supports importing historical SQL logs to trace issues. Real-time analysis: This feature provides real-time SQL analysis and an out-of-the-box report center based on SLS. This feature also supports custom reports and drill-down analysis, and helps you understand the execution status, performance, and security risks of databases. Real-time alerts: This feature supports real-time monitoring and alerts based on customized metrics to ensure timely response to critical business exceptions. Limits and instructions You must activate Alibaba Cloud SLS to use the SQL audit and analysis feature. SQL audit logs are saved for 30 days by default. You can modify the log storage time as needed. Do not delete or modify the default settings for the project, Logstore, index, or dashboard that are created by SLS. SLS updates and upgrades the SQL log audit feature from time to time. The indexes and default reports of the exclusive Logstore are also automatically updated. The maximum length of a single SQL statement is 5 MB. Scenarios Troubleshoot SQL problems After the SQL audit and analysis feature is enabled, you can quickly search SQL logs to locate and troubleshoot problems. For example, to check whether a DROP operation is performed, you can perform the following query:

```
sql_type: Drop
```

The query result contains information such as the SQL execution time, user, and IP address of the client that runs the SQL statement. Analyze costly SQL templates In most applications, SQL statements are dynamically generated based on several templates, with different parameters. The real-time analysis feature of SLS allows you to obtain the list of costly SQL statements in the current database. For example, execute the following query:

```
| SELECT sql_code as "SQL template ID",
round(total_time * 1.0 /sum(total_time) over() * 100,2) as "execution time share (%)", execute_times as "number of execution times", round(avg_time) as "average execution time", round(avg_rows) as "average number of affected rows", CASE WHEN length(sql) > 200 THEN concat(substr(sql, 1, 200), '......') ELSE trim(lpad(sq l, 200,$) end as "sample SQL" FROM (SELECT sql_code, count(1) as execute_times, sum(response_time) as total_time, avg(response_time) as avg_time, avg(affect_rows) as avg_rows, arbitrary(sql) as sql FROM log GROUP BY sql_code) ORDER BY "execution time share (%)" des c limit 10
```

The search result contains the SQL template ID, ratio of response time of the statement generated from the template in the total response time of SQL statements, number of executions, average execution time, average number of affected rows, and sample SQL statement. You can find and optimize the most costly SQL templates in the application based on the analysis result. Collect log statistics To help you analyze issues, PolarDB-X combines the SQL audit and analysis feature with SLS and provides out-of-the-box reports. You can diagnose and analyze the running status, performance, and potential security risks of databases in real time.

#### 4.8.2 Enable SQL audit and analysis

The SQL audit and analysis feature is disabled by default. You can manually enable it in the PolarDB-X 1.0 console. By default, you can perform only audit and analysis on the log data generated after the SQL audit and analysis feature is enabled. You can also import a portion of historical data. Prerequisites The SQL audit and analysis feature depends on Log Service (SLS). You must activate SLS before you use this feature. Procedure
1. Log on to the SLS console. For more information, see Log ServiceUser Guide > Quick St art > Log
on t o t he Log Service console.
2. Select the organization to which the PolarDB-X 1.0 instance belongs.

> Not e The logon account must be consistent with the logon account of PolarDB-X 1.0.

3. Click SLS to go to the Log Service page.
4. Log on to the PolarDB-X console.
5. Find the target instance in the instance list.
6. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
7. In the left-side navigation pane, choose Diagnost ics and Opt imizat ion > SQL Audit and
Analysis.
8. In the left-side section, select the database for which you want to enable the SQL audit and
analysis feature.
9. On the SQL Audit and Analysis page, turn on the switch next to SQL Audit Log St at us of
Current Dat abase on the right.

> Not e On the SQL Audit and Analysis page, you can also turn on the switch of SQL Audit and Analysis next to the target database in the left-side section.

10. Confirm whether to import historical data.

> Not e By default, you can analyze and audit only the logs that are generated after the SQL audit and analysis feature is enabled. If you find the historical data of the PolarDB-X 1.0 database is modified but the SQL audit and analysis feature is not enabled, you can import historical data and include historical logs in the audit and analysis scope to trace data tampering. PolarDB-X 1.0 dynamically checks the scope of historical data that can be imported based on the log storage on the PolarDB-X 1.0 instance. Logs within seven days can be imported.
> If you need to import historical data, enable Import Hist orical Dat a or Not , specify the backtrace start time and end time, and then click Enable.
> If you do not need to import historical data, click Enable.

What's next Every time you use the SQL audit and analysis feature, you must repeat the preceding steps.

#### 4.8.3 Log fields

This topic describes the log fields in SQL audit and analysis.

| Field | Description | Supported version |
|---|---|---|
| topic __ __ | The log topic in the format of drds audit log {instance i _ _ _ _ d name { db name} , such as _ _ drds audit log drdsxyzabcd _ _ _ demo drds db . _ _ _ | All versions |
| instance id _ | The ID of the PolarDB-X 1.0instance. | All versions |
| db name _ | The name of the PolarDB-X 1.0 database | All versions |
| user | The user name used to run the SQL statement. | All versions |
| client ip _ | The IP address of the client that accessed the PolarDB-X 1.0 instance. | All versions |
| client port _ | The port of the client that accessed the PolarDB-X 1.0 instance. | All versions |
| sql | The executed SQL statement. | All versions |

|   |   | drds audit log {instance i _ _ _ _ |   |   |
|---|---|---|---|---|
| pic __ | d name { db name} _ _ |   |   |   |
|   |   |   | , such as |   |
|   | demo drds db _ _ _ |   |   |   |

| Field | Description | Supported version |
|---|---|---|
| trace id _ | The trace ID of the SQL statement when it was executed. If a transaction was executed, it is tracked by an ID that consists of the trace ID, a hyphen, and a number, for example, drdsabcdxyz-1 and drdsabcdxyz-2 . | All versions |
| sql code _ | The hash value of the template SQL statement. | All versions |
| hint | The hint that was used to execute the SQL statement. | All versions |
| table name _ | The name of the table involved in the query. Separate multiple tables by commas (,). | All versions |
| sql type _ | The type of the SQL statement. Valid values: SELECT, INSERT, UPDATE, DELETE, SET, ALTER, CREATE, DROP, TRUNCATE, REPLACE, and Other. | All versions |
| sql type detail _ _ | The name of the SQL parser. | All versions |
| sql time _ | The start time for the execution of the SQL statement. The time follows the yyyy-MM-dd HH:mm:ss.SSS format. | All versions |
| response time _ | The response time. Unit: milliseconds. | Version 5.3.4-15378085 and later |
| affect rows _ | The number of rows returned when the SQL statement was executed. The number of rows affected when the INSERT, DELETE, or UPDATE statement was executed. | Version 5.3.4-15378085 and later |
| fail | Indicates whether an error occurred in the execution of the SQL statement. Valid values: 0: successful 1: failed | Version 5.3.4-15378085 and later |

|   |   | yyyy-MM-dd | All v |
|---|---|---|---|
|   | HH:mm:ss.SSS |   |   |

#### 4.8.4 Log analysis

The SQL audit and analysis feature is based on Log Service (SLS) and provides powerful log analytics capabilities. This topic describes SQL statements for log analysis in common scenarios and provides relevant examples. After the SQL audit and analysis feature is enabled, you can perform audit and analysis on SQL log files by using the query and analysis syntax of SLS on the SQL Audit and Analysis page. Based on the query and analysis syntax of SLS, you can find problematic SQL statements on the Log Analysis tab and analyze the SQL statement execution status, performance metrics, and security issues of PolarDB-X 1.0. For more information about the query and analysis syntax of SLS, see Log Service User Guide > Query and Analysis > Query Synt ax and Funct ions > Query Synt ax. Precautions All the audit logs of PolarDB-X 1.0 databases in the same region are written to the same Logstore in SLS. Therefore, by default, the SQL Audit and Analysis page provides the filter conditions based on __topic__, to ensure that the searched SQL log files are from PolarDB-X 1.0. Therefore, all the statements provided in this topic must be used after the existing filter conditions. An example is shown in the following figure: The ① part is the default filter condition. The ② part is the additional filter condition. Find problematic SQL statements Fuzzy search For example, to query SQL statements that contain the "34" keyword, enter the following content in the search box:

```
 and sql: 34
```

The result is shown in the following figure. Field search Based on built-in index fields, the SQL audit and analysis feature also supports field-based search. For example, to query SQL statements of the Drop type, execute the following statement:

```
and sql_type:Drop
```

The result is shown in the following figure. Multi-condition search You can use the "and" and "or" keywords to perform a multi-condition search. For example, you can query the delete operation on the rows whose id is 34:

```
and sql:34 and sql_type: Delete
```

Search based on numeric comparison affect_rows and response_time in the index filed are numeric values and support comparison operators. For example, you can query the SQL INSERT statements whose response_time is greater than 1s.

```
 and response_time  > 1507 and sql_type: Insert
```

For example, you can query the SQL statement that deletes more than 100 rows of data:

```
 and affect_rows  > 100 and sql_type: Delete
```

Analysis of the SQL statement execution status This section introduces the statements used to query the SQL statement execution status in PolarDB-X 1.0. Failure rate of SQL statement execution Execute the following statement to query the failure rate of SQL statement execution:

```
| SELECT sum(case when fail = 1 then 1 else 0 end) * 1.0 / count(1) as fail_ratio
```

The result is shown in the following figure. If your business is sensitive to the error rate of SQL statement execution, you can customize the alert information based on the query result. Click Save as Alert in the upper-right corner of the page. In the alert settings shown in the preceding figure, the number of log entries that have an error rate of SQL statement execution greater than 0.01 within 15 minutes is checked within every 15 minutes. You can also customize alerts as needed. Total number of rows returned by SELECT statements Execute the following statement to query the cumulative number of rows queried by SELECT statements:

```
  and sql_type: Select | SELECT sum(affect_rows)
```

SQL statement type distribution Execute the following statement to query the SQL statement type distribution:

```
  | SELECT  sql_type, count(sql) as times GROUP BY sql_type
```

IP address distribution of SQL independent users Execute the following statement to query the distribution of IP addresses of independent users who execute SQL statements:

```
 | SELECT  user, client_ip, count(sql) as times GROUP BY user, client_ip
```

SQL performance analysis This section describes typical SQL statements for SQL performance analysis. Average response time of SELECT statements Execute the following statement to query the average response time of SELECT statements:

```
 and sql_type: Select | SELECT avg(response_time)
```

Distribution of SQL statement response time Execute the following statement to query the distribution of SQL statement response time:

```
 and response_time > 0 | select case when response_time <=10 then '<=10 ms when response_
time > 10 and response_time <= 100 then '10~100 ms when response_time > 100 and response_ time <= 1000 then '100 ms ~ 1s 'When response_time > 1000 and response_time <= 10000 then '1s ~ 10s' when response_time > 10000 and response_time <= 60000 then '10s ~ 1 min'> 1 mi n' end as latency_type, count(1) as cnt group by latency_type order by latency_type DESC
```

The preceding query shows the distribution of SQL statement execution time based on a given time range. You can adjust the time range to obtain finer-grained results. Top 50 slow SQL statements Execute the following statement to query slow SQL statements:

```
 | SELECT date_format(from_unixtime(__time__), '%m/%d %H:%i:%s') as time, user, client_ip
, client_port, sql_type, affect_rows, response_time, sql ORDER BY response_time desc LIM IT 50
```

The following figure shows the result, which includes the SQL statement execution time, user name, IP address, port number, SQL statement type, number of affected rows, response time, and text of SQL statements. Top 10 costly SQL templates In most applications, SQL statements are dynamically generated based on several templates, and only the parameters are different. You can find, analyze, and optimize the costly SQL templates based on template IDs. Enter the following query statement:

```
| SELECT sql_code as "SQL template ID", round(total_time * 1.0 /sum(total_time) over() *
100, 2) as "response time share (%)" ,execute_times as "number of executions", round(avg_ time) as "average response time", round(avg_rows) as "average number of affected rows", C ASE WHEN length(sql) > 200 THEN concat(substr(sql, 1, 200℃, '......') ELSE trim(lpad(sql , 200,'hour) end as "sample SQL" FROM (SELECT sql_code, count(1) as execute_times, sum(re sponse_time) as total_time, avg(response_time) as avg_time, avg(affect_rows) as avg_rows, arbitrary(sql) as sql FROM log GROUP BY sql_code) ORDER BY "execution time share (%)" des c limit 10
```

The statistics include the SQL template ID, percentage of response time of the statement generated from the template in the total response time of SQL statements, number of executions, average response time, average number of affected rows, and sample SQL statement. For better display effect, each page displays 200 entries. In the preceding query result, statements are ranked by the response time share. However, you can rank the statements by the average response time or the number of executions to troubleshoot relevant issues. Average transaction response time For SQL statements within the same transaction, the preset trace_id field prefixes are the same, and the suffixes are '-' followed by sequence numbers. trace_id of non-transactional SQL statements does not contain '-'. Based on this, you can analyze the performance of transactions.

> Not e Transaction analysis is less efficient than other query operations because it involves prefix matching.

For example, execute the following statement to query the average response time of transactions:

```
 | SELECT  sum(response_time) / COUNT(DISTINCT substr(trace_id, 1, strpos(trace_id, '-')
- 1)) where strpos(trace_id, '-') > 0
```

Top 10 slow transactions You can query the list of slow transactions by response time of transactions. Use the following statement:

```
| SELECT substr(trace_id, 1, strpos(trace_id, '-') - 1) as "transaction ID" , sum(respons
e_time) as "response time" where strpos(trace_id, '-') > 0 GROUP BY substr(trace_id, 1, s trpos(trace_id, '-') - 1) ORDER BY "response time" DESC LIMIT 10
```

Based on this, you can use the transaction ID to search for all the SQL statements under the transaction and analyze the specific causes of slow execution. Use the following statement:

```
 and trace_id: db3226a20402000*
```

Top 10 transactions with batch operations Based on the number of rows affected by SQL statements in a transaction, you can obtain the list of transactions that contain batch operations. Use the following statement:

```
| SELECT substr(trace_id, 1, strpos(trace_id, '-') - 1) as "transaction ID" , sum(affect_
rows) as "number of affected rows" where strpos(trace_id, '-') > 0 GROUP BY substr(trace_ id, 1, strpos(trace_id, '-') - 1) ORDER BY "number of affected rows" DESC LIMIT 10
```

SQL security analysis This section provides typical query statements for SQL security analysis. Distribution of types of failed SQL statements

```
 and fail > 0 | select sql_type, count(1) as "number of errors" group by sql_type
```

High-risk SQL statements High-risk SQL statements are of the Drop or Truncate type. You can also add more conditions as needed.

```
 and sql_type: Drop OR  sql_type: Truncate
```

SQL batch delete events

```
 and affect_rows > 100 and sql_type: Delete | SELECT date_format(from_unixtime(__time__),
'%m/%d %H:%i:%s') as time, user, client_ip, client_port, affect_rows, sql ORDER BY affec t_rows desc LIMIT 50
```

#### 4.8.5 Log reports

Based on Log Service (SLS), the SQL audit and analysis feature of PolarDB-X 1.0 provides out-of-thebox report centers, including the Operation Center, Performance Center, and Security Center. This feature allows you to fully understand the performance status, performance metrics, and potential security risks of your PolarDB-X 1.0 databases. After Enable SQL audit and analysis, click the Log Report s tab on the current page. You can view the reports pages provided by SLS, including Operat ion Cent er, Perf ormance Cent er, and Securit y Cent er.

> Not e
> All the audit logs of PolarDB-X 1.0 databases in the same region are written to the same Logstore in SLS. Therefore, when you view the reports of the current PolarDB-X 1.0 database, filter conditions based on the __topic__:drds_audit_log_ instance id_database name are added by default, which indicates that you are viewing the data of the current database. For example, `drds_audit_log_drdsxyzabcd_demo_drds_db` .
> If the version of the PolarDB-X 1.0 instance is earlier than Version 5.3.4-15378085, the relevant fields are missing from SQL logs. For more information about log fields, see Log fields. The Log Reports tab provides only a simplified version of Operation Center. To use a full version of reports, upgrade the instance to the latest version.

View reports Statistics in the charts on the Log Reports tab are generated for different time periods. You can change the time range as needed. You can change the time range for all charts or a single chart. Click the time selector (position ① in the figure). In the dialog box that appears, you can change the time range of all the charts on the current page. Click the time selector of a chart (position ② in the figure) to modify the time range of the chart. Operation Center Operation Center shows the metrics, distribution, and trends of SQL statement execution in PolarDB-X 1.0 databases.

| Item | Type | Default time range | Description |
|---|---|---|---|
| PV (SQL Execution Count) | Single value | 1 Hour (Relative) | The number of SQL statement executions |
| UV (Unique User/IP) | Single value | 1 Hour (Relative) | The number of unique user-IP groups |
| Malicious IP Count | Single value | 1 Hour (Relative) | The number of malicious IP addresses. For more information about the definition of malicious IP addresses, see security detection functions. |
| Execution Errors | Single value | 1 Hour (Relative) | The number of SQL statements with execution errors |
| Table Count with Execution | Single value | 1 Hour (Relative) | The total number of tables operated by SQL statements |
| Total Inserted Rows | Single value | 1 Hour (Relative) | The total number of rows inserted by INSERT statements |
| Total Updated Rows | Single value | 1 Hour (Relative) | The total number of rows updated by UPDATE statements |
| Total Deleted Rows | Single value | 1 Hour (Relative) | The total number of rows deleted by DELETE statements |
| Total Read Rows | Single value | 1 Hour (Relative) | The total number of rows returned by SELECT statements |
| SQL Types (Non Table Based) | Single value | 1 Hour (Relative) | The types of SQL statements used for non-table operations, such as SHOW VARIABLES LIKE |
| SQL Execution Trend | Column chart | 1 Hour (Relative) | The distribution trend of SQL statement executions and the distribution trend of failed SQL statements |
| Operated Tables | Flow diagram | 1 Hour (Relative) | The distribution of tables operated by SQL statements |

| loud Native Distributed Da olarDB-X | tabase | User G | uide·Instance managemen |
|---|---|---|---|

| Item | Type | Default time range | Description |
|---|---|---|---|
| SQL Type | Flow diagram | 1 Hour (Relative) | The distribution of SQL statement types by time |
| User Distribution | Pie chart | 1 Hour (Relative) | The distribution of users who execute SQL statements |
| SQL Type Distribution | Area chart | 1 Hour (Relative) | The percentage of SQL statement types in the current time range |
| Tables with Most Operations (Top 50) | Table | 1 Hour (Relative) | The list of top tables by the number of operations, including table names and the number of operations such as read, delete, update, and insert |
| SQL Type (World) | Map | 1 Hour (Relative) | The distribution of IP addresses of clients that execute the SQL statements, on the world map |
| SQL Type (China) | Map | 1 Hour (Relative) | The distribution of IP addresses of clients that execute the SQL statements, on the map of China |

Performance Center Performance Center shows performance metrics, the distribution of slow and fast SQL statements, and the distribution and sources of costly SQL statements in PolarDB-X 1.0 databases.

| Item | Data type | Default time range | Description |
|---|---|---|---|
| Peak SQL Execution Traffic | Single value | 1 Hour (Relative) | The maximum number of SQL statements executed per second |
| Peak Select Traffic | Single value | 1 Hour (Relative) | The maximum number of rows returned by SELECT statements per second |
| Peak Insert Traffic | Single value | 1 Hour (Relative) | The maximum number of rows inserted by INSERT statements per second |

| U | ser Guide·Instance manag | ement | Cloud N | ative Distributed Database PolarDB- | X |
|---|---|---|---|---|---|

| Item | Data type | Default time range | Description |
|---|---|---|---|
| Peak Update Traffic | Single value | 1 Hour (Relative) | The maximum number of rows updated by UPDATE statements per second |
| Peak Delete Traffic | Single value | 1 Hour (Relative) | The maximum number of rows deleted by DELETE statements per second |
| Average Response Time | Single value | 1 Hour (Relative) | The average response time of SQL statements |
| Select SQL | Single value | 1 Hour (Relative) | The average number of SELECT statements executed per second |
| Insert SQL | Single value | 1 Hour (Relative) | The average number of INSERT statements executed per second |
| Update SQL | Single value | 1 Hour (Relative) | The average number of UPDATE statements executed per second |
| Delete SQL | Single value | 1 Hour (Relative) | The average number of DELETE statements executed per second |
| Select/Update Traffic Trend | Line chart | 1 Hour (Relative) | The distribution of rows affected by the SELECT and UPDATE statements over time |
| SQL Execution Time Distribution | Pie chart | 1 Hour (Relative) | The distribution of execution time of SQL statements |
| Slow SQL Table Distribution | Pie chart | 1 Hour (Relative) | The distribution of tables targeted by slow SQL statements whose response time exceeds 1s |
| Slow SQL User Distribution | Pie chart | 1 Hour (Relative) | The distribution of users who execute slow SQL statements with response time of more than 1s |

| Item | Data type | Default time range | Description |
|---|---|---|---|
| Slow SQL Type Distribution | Pie chart | 1 Hour (Relative) | The distribution of types of slow SQL statements whose response time exceeds 1s |
| Slow SQL (Top 50) | Table | 1 Hour (Relative) | The table of slow SQL statements whose response time exceeds 1s, including the time, client, response time, PolarDB-X 1.0 instance, database, table, user, affected rows, SQL type, and SQL text |
| SQL Template Execution Time Top 20 | Table | 1 Hour (Relative) | Statistics of the execution status of the SQL statements in the template based on the specified SQL template, including the SQL template ID, response time share, number of executions, average response time, average number of affected rows, and sample SQL statement |
| Transaction Affected Rows Top 20 | Table | 1 Hour (Relative) | The table of top 20 transaction-by the number of affected rows, including the transaction ID and the number of affected rows |
| Transaction Executed Time Top 20 | Table | 1 Hour (Relative) | The table of top 20 transactions by response time, including the transaction ID and the number of affected rows |

Security Center Security Center shows failed and malicious SQL statement executions in PolarDB-X 1.0 databases, and the details, distribution, and trends of malicious SQL batch delete and update events.

| Item | Type | Default time range | Description |
|---|---|---|---|

| Item | Type | Default time range | Description |
|---|---|---|---|
| Error Count | Single value | 1 Hour (Relative) | The number of failed SQL statement executions |
| Batch Delete Events | Single value | 1 Hour (Relative) | The number of SQL statements for batch delete events (more than 100 rows) |
| Batch Update Events | Single value | 1 Hour (Relative) | The number of SQL statements for batch update events (more than 100 rows) |
| Malicious SQL Executions | Single value | 1 Hour (Relative) | The number of malicious SQL statement executions (Drop and Truncate) |
| Malicious IP Count | Single value | 1 Hour (Relative) | The number of malicious IP addresses. For more information about the definition of malicious IP addresses, see security detection functions. |
| Error Distribution | Area chart | 1 Hour (Relative) | The distribution of types of failed SQL statements |
| Distribution of Client with Errors | Map | 1 Hour (Relative) | The distribution of clients for failed SQL statements on the map of China |
| Client with Most Errors | Table | 1 Hour (Relative) | The table of clients on which the execution of SQL statements failed, including the IP address, number of errors, type of failed SQL statement, and sample failed SQL statement |
| Malicious SQL Executions | Table | 1 Hour (Relative) | The table of malicious SQL statement executions, including the time, IP address, SQL, PolarDB-X 1.0 instance ID, database, table, and user |

| Item | Type | Default time range | Description |
|---|---|---|---|
| Batch Delete Events (Top 50) | Table | 1 Hour (Relative) | The table of top SQL batch delete events, including the earliest execution time, most recent execution time, PolarDB-X 1.0 instance ID, database, table, number of executions, average number of deleted rows, average response time, and sample SQL statement |
| Batch Update Events (Top 50) | Table | 1 Hour (Relative) | The table of top SQL batch update events, including the earliest execution time, most recent execution time, PolarDB-X 1.0 instance ID, database, table, number of executions, average number of updated rows, average response time, and sample SQL statement |

### 4.9 Monitor PolarDB-X instances

#### 4.9.1 View monitoring information

PolarDB-X 1.0 provides multi-dimensional monitoring. This topic describes how to view monitoring information in the PolarDB-X 1.0 console. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. On the Basic Inf ormat ion page, choose Monit oring and Alert s > Inst ance Monit oring in the
left-side navigation pane.
5. On the Inst ance Monit oring page, select a monitoring dimension and the corresponding metrics
to view details. For more information about metrics, see Monitoring metrics.

#### 4.9.2 Monitoring metrics

Instance monitoring is divided into resource monitoring and engine monitoring. Engine monitoring metrics are classified into metrics at the PolarDB-X 1.0 instance level and metrics at the PolarDB-X 1.0 database level. When some engine monitoring metrics are abnormal, you can directly check the metrics of each database to locate the database with performance problems. The following table describes the metrics of these two types in details.

| Monitoring item | Category | Description | Data collection cycle | Data retention period | Description |
|---|---|---|---|---|---|
| CPU Utilization (%) | Resource monitoring | The average CPU utilization of PolarDB-X 1.0 server nodes. | 1 minute | 3 days | - |
| Memory Usage (%) | Resource monitoring | The memory usage of JVM Old Generation on PolarDB-X 1.0 server nodes. | 1 minute | 3 days | Memory usage fluctuations are normal. |
| Inbound Traffic (Kbps) | Resource monitoring | The total inbound network traffic of PolarDB-X 1.0 server nodes. | 1 minute | 3 days | Inbound network traffic is generated when ApsaraDB RDS for MySQL returns data to PolarDB-X 1.0. |
| Outbound Traffic (Kbps) | Resource monitoring | The total outbound network traffic of PolarDB-X 1.0 server nodes. | 1 minute | 3 days | Outbound network traffic is generated when a PolarDB-X 1.0 instance sends a physical SQL statement to an AparaDB RDS for MySQL instance or a PolarDB-X 1.0 instance returns data to an application. |

| Monitoring item | Category | Description | Data collection cycle | Data retention period | Description |
|---|---|---|---|---|---|
| Logical QPS | Engine monitoring | The total number of SQL statements processed per second on PolarDB-X 1.0 server nodes. | 5 seconds | 7 days | - |
| Physical QPS | Engine monitoring | The total number of SQL operations sent from PolarDB-X 1.0 server nodes to ApsaraDB RDS for MySQL per second. | 5 seconds | 7 days | One logical SQL statement can be partitioned into multiple physical SQL statements. |
| Logical RT (ms) | Engine monitoring | The average response time (RT) for processing each SQL statement by PolarDB-X 1.0. | 5 seconds | 7 days | If a logical SQL statement is partitioned into physical SQL statements for delivery, the logical RT of the SQL statement contains the RT of the physical SQL statements. |
| Physical RT (ms) | Engine monitoring | The average RT for transmitting SQL statements from PolarDB- X 1.0 to ApsaraDB RDS for MySQL. | 5 seconds | 7 days | - |
| Connections | Engine monitoring | The total number of connections established between an application and PolarDB-X 1.0. | 5 seconds | 7 days | The connections from PolarDB- X 1.0 to ApsaraDB RDS for MySQL are not included. |

| Monitoring item | Category | Description | Data collection cycle | Data retention period | Description |
|---|---|---|---|---|---|
| Active Threads | Engine monitoring | The number of threads that are used by PolarDB-X 1.0 to run SQL statements. | 5 seconds | 7 days | - |

#### 4.9.3 How metrics work

Before analyzing metrics, you need to understand the execution process of SQL statements on PolarDB-X 1.0. PolarDB-X 1.0 SQL execution flowchart In the entire SQL execution process, the execution status of steps 2 through 4 is reflected in various metrics of PolarDB-X 1.0. In step 2, SQL parsing, optimization, and execution consume CPU resources. A more complex SQL statement (with a complex structure or ultra-long length) consumes more CPU resources. You can run the T RACE command to trace the SQL execution process. You can see the time consumed by an SQL statement during optimization. The longer time consumed indicates a higher CPU utilization. In step 3, the delivery and execution of physical SQL statements consume I/O resources. You can analyze the execution status of physical SQL statements based on metrics such as logical queries per second (QPS), physical QPS, logical response time (RT), and physical RT. For example, if the physical QPS is low and the physical RT is high, the current ApsaraDB RDS for MySQL instance is processing SQL statements very slowly. You need to check the performance of the ApsaraDB RDS for MySQL instance. In step 5, the SQL execution results are processed and integrated. These operations convert the execution results of physical SQL statements. In most cases, only SQL metadata is converted, which consumes few resources. However, the CPU utilization is high for steps such as `heap sort` . For more information about how to determine the consumption of SQL statements at this stage, see Details about a low SQL statement.

#### 4.9.4 Prevent performance problems

##### 4.9.4.1 Example 1: PolarDB-X CPU utilization

Performance metrics change with the system business traffic. The following describes the CPU utilization in two common cases: An application has a shopping spree activity at 09:00 every morning. Therefore, the traffic of the system increases significantly at this time point. According to the monitoring data, the CPU utilization of the PolarDB-X 1.0 instance increased from 20% to about 80% from about 09:00, with the traffic peak lasting about 10 minutes. CPU utilization-1 The system traffic keeps increasing with an application until it reaches a plateau. The monitored CPU utilization of the PolarDB-X 1.0 instance also reflects this change. CPU utilization-2 When the load on the PolarDB-X 1.0 instance changes with the business, you must pay close attention to the changes in metrics. If the CPU utilization exceeds the threshold, you must upgrade the PolarDB-X 1.0 specifications to alleviate the performance pressure. You can set alert rules for instances in the PolarDB-X 1.0 console. When the average CPU utilization exceeds the preset threshold, the system sends short messages to the corresponding contacts. You can set the CPU utilization threshold as needed. We recommend that you set it to 80%.

##### 4.9.4.2 Example 2: Logical RT and physical RT

You can observe the difference between the logical response time (RT) and physical RT. Logical RT refers to the time from when a PolarDB-X 1.0 instance receives a logical SQL statement to when it returns data to an application. Physical RT refers to the time from when a PolarDB-X 1.0 instance sends a physical SQL statement to an ApsaraDB RDS for MySQL instance to when it receives the data returned by the ApsaraDB RDS for MySQL instance. If a logical SQL statement is partitioned into one or more physical SQL statements, the logical RT is greater than or equal to the physical RT. Ideally, PolarDB-X 1.0 performs only a few operations on the data returned by ApsaraDB RDS for MySQL. Therefore, logical RT is slightly longer than physical RT. Under special circumstances, physical SQL queries are run fast, while logical SQL queries take a long time to run. In this case, the logical RT and physical RT are as follows. Logical RT Physical RT As shown in the preceding figures, the change trends of logical RT and physical RT in the two monitoring charts are basically the same, while logical RT fluctuates between 10 ms and 20 ms and physical RT fluctuates between 2 ms and 5 ms. This means that PolarDB-X 1.0 has a heavy load, which can be solved by upgrading the PolarDB-X 1.0 configuration. If both the logical RT and physical RT are high, you can upgrade the ApsaraDB RDS for MySQL configuration or optimize SQL statements on the ApsaraDB RDS for MySQL instance.

##### 4.9.4.3 Example 3: Logical QPS and physical QPS

You can observe the difference between the logical queries per second (QPS) and physical QPS. According to the monitoring data, the logical QPS and physical QPS have the same trends, but the difference between the two is relatively large and in a certain proportion. Logical QPS Physical QPS Physical QPS As shown in the preceding figures, logical QPS fluctuates between 80 and 150, and physical QPS fluctuates between 700 and 1,200. The reason is that PolarDB-X 1.0 generates physical SQL statements based on logical SQL statements. The ratio of logical SQL statements to physical SQL statements is not necessarily 1:1. For example, a PolarDB-X 1.0 logical table is created by using the following statement:

```
CREATE TABLE drds_user (id int, name varchar(30)) dbpartition by hash(id);
```

When the query condition contains the database shard key, PolarDB-X 1.0 pushes the logical SQL statement down to the ApsaraDB RDS for MySQL instance for execution. According to the execution plan, the number of physical SQL statements is 1:

```
mysql> explain select name from drds_user where id = 1; +---------------------------+-------------------------------------------------------------- -----------+--------+
| GROUP_NAME                | SQL
| PARAMS |
+---------------------------+-------------------------------------------------------------- -----------+--------+
|     SANGUAN_BSQT_0001_RDS | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`id` = 1) | {} | +---------------------------+-------------------------------------------------------------- -----------+--------+
```

When the query does not contain the database shard key, PolarDB-X 1.0 partitions the logical SQL statement into multiple physical SQL statements. The following execution plan shows that there are eight physical SQL statements:

```
mysql> explain select name from drds_user where name = 'LiLei'; +----------- ---------------+-------------------------------------------------------------- -------------------+--------+
| GROUP_NAME                | SQL
| PARAMS |
+---------------------------+-------------------------------------------------------------- -------------------+--------+
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} |
| SANGUAN_BSQT_0001_RDS     | select `drds_user`.`name` from `drds_user` where (`drds_user`
.`name` = 'LiLei') | {} | +---------------------------+-------------------------------------------------------------- -------------------+--------+ 8 rows in set (0.06 sec)
```

Logical or physical QPS indicates the total number of logical or physical SQL statements processed per unit of time. When most SQL statements in the system contain the shard key, the ratio of logical QPS to physical QPS is close to 1:1. If the difference between the logical and physical QPS is too large, many SQL statements of the current application do not contain the shard key. In this case, check the SQL statements of the application to improve performance.

##### 4.9.4.4 Example 4: High memory usage

The overly high memory usage of the PolarDB-X 1.0 instance is mostly caused by the large number of SQL queries in your application and the overlarge result set that is returned. If the memory usage of your PolarDB-X 1.0 instance remains at about 100%, perform the Restart a PolarDB-X instance operations to locate and optimize the slow SQL queries of your application.

### 4.10 View the instance version

This topic describes two ways that you can use to view the version of a PolarDB-X 1.0 instance. View the instance version in the console
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the Conf igurat ion Inf ormat ion section, view the value of Current Version.
View the instance version by using the version() function Connect to the PolarDB-X 1.0 instance by using the MySQL command line and execute the `SELECT` `version()` statement to view the version of the PolarDB-X 1.0 instance.

```
mysql> select version(); +-----------------------------+
| VERSION()                   |
+-----------------------------+
| 5.6.29-TDDL-5.1.28-1320920  |
+-----------------------------+ 1 row in set (0.00 sec)
```

In the preceding statement, 5.1.28-1320920 indicates the version of the PolarDB-X 1.0 instance.

## 5 Account management

### 5.1 Basic concepts

This topic describes the terms of the PolarDB-X 1.0 account and permission system. The usage of the account and permission system in PolarDB-X 1.0 is the same as in MySQL. PolarDB-X supports statements such as `GRANT` , `REVOKE` , `SHOW GRANTS` , `CREATE USER` , `DROP USER` , and `SET PASSWORD` . PolarDB-X allows you to grant permissions at the database and table levels, but does not allow you to grant permissions at the global or column level. For more information about the MySQL account and permission system, see MySQL Documentation.

> Not ice Accounts created by using `CREATE USER` in PolarDB-X 1.0 exist only in the PolarDB-
> X 1.0 instance and will not be synchronized to the backend ApsaraDB RDS for MySQL instances.

Account An account is specified by the user name and hostname in the username@'host' format. Accounts with the same user name but different hostnames are different accounts. For example, lily@30.9.73.96 and lily@30.9.73.100 are two different accounts, and their passwords and permissions may be different. After a database is created in the PolarDB-X 1.0 console, the system automatically creates two system accounts for the database: the administrator account and read-only account. These two accounts are built-in accounts. You cannot delete them or modify their permissions. The administrator account name is the same as the database name. For example, if the database name is easydb, the administrator account name is also easydb. The read-only account name is the database name suffixed with _RO. For example, if the database name is easydb, the read-only account name is easydb_RO. Assume that the dreamdb and andordb databases are available. Based on the preceding rules, the dreamdb database contains the administrator account named dreamdb and the read-only account named dreamdb_RO, while the andordb database contains the administrator account named andordb and the read-only account named andordb_RO. Account rules Each administrator account has all permissions. Only the administrator account can create accounts and grant permissions. Other accounts can only be created and granted permissions by the administrator account. The administrator account is bound to a database and does not have permissions on other databases. It can access only the bound database, and cannot grant permissions of other databases to an account. For example, the easydb administrator account can connect only to the easydb database, and can grant only the permissions of the easydb database or tables in the easydb database to an account. A read-only account has only the SELECT permission. User name rules User names are case-insensitive. A user name must be 4 to 20 characters in length. A user name must start with a letter. A user name can contain uppercase letters, lowercase letters, and digits. Password rules A password must be 6 to 20 characters in length. A password can contain letters, digits, and special characters that include the at sign (@), number sign (#), dollar sign ($), percent sign (%), caret (^), ampersand (&), plus sign (+), equal sign (=). Hostname matching rules A hostname must be an IP address. It can contain underscores (_) and wildcards (%). An underscore (_) indicates a character and a wildcard (%) indicates zero or more characters. Hostnames that contain wildcards must be quoted with single quotation marks ('), for example, lily@'30.9. %.%' and `da`

```
vid@'%' .
```

If two user names in the system can be used to log on to the database, the user name with the longest prefix (the longest IP segment excluding wildcards) prevails. For example, if the `david@'30.9` `.12_.234'` and david@'30.9.1%.234' user names are available in the system, use `david@'30.9.1`

|   | .12 .234' _ |   |
|---|---|---|
| 2 .234' _ |   | to |

`2_.234'` to log on from the 30.9.127.234 host as david. When you enable the virtual private cloud (VPC) access feature for a host, the IP address of the host changes. To avoid invalid configurations in the account and permission system, set the hostname to '%' to match an IP address. Permissions Permission support by level Global permission (not supported) Database-level permission (supported) Table-level permission (supported) Column-level permission (not supported) Subprogram-level permission (not supported) Permissions Eight table-associated basic permissions are supported: `CREATE` , `DROP` , `ALTER` , `INDEX` , `INSERT` , `DELETE` , `UPDATE` , and `SELECT` . The `TRUNCATE` statement requires the table-level DROP permission. The `REPLACE` statement requires the table-level INSERT and DELETE permissions. The `CREATE INDEX` and `DROP INDEX` statements require the table-level INDEX permission. The `CREATE SEQUENCE` statement requires the database-level CREATE permission. The `DROP SEQUENCE` statement requires the database-level DROP permission. The `ALTER SEQUENCE` statement requires the database-level ALTER permission. The `INSERT ON DUPLICATE UPDATE` statement requires the table-level INSERT and UPDATE permissions. Permission rules Permissions are bound to an account ( `username@'host'` ) rather than a user name ( `username` ). An error occurs if the table does not exist during authorization. The database permissions are listed by level in descending order: global permissions (not supported), database-level permissions, table-level permissions, and column-level permissions (not supported). A granted higher-level permission overwrites a lower-level permission. If you remove the higher-level permission, the lower-level permission is also removed. USAGE authorization is not supported.

### 5.2 Create an account

This topic describes how to create a PolarDB-X 1.0 account in the PolarDB-X 1.0 console and by using SQL statements. Prerequisites You have created or added a database. For more information, see Create a database. Create an account in the console
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Account
Management .
5. On the Account Management page, click Creat e Account in the upper-right corner.
6. Set the following parameters.

| Parameter | Description |
|---|---|
| Database Account | Enter a name for the account. The account name must meet the following requirements: The name must be 4 to 20 characters in length. The name must start with a letter and end with a letter or digit. The name can contain uppercase letters, lowercase letters, digits, and underscores ( ). _ |
| New Password | Enter a password for the account. The password must meet the following requirements: The password must be 8 to 32 characters in length. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include exclamation marks (!). @#$%^&*() +-= _ |
| Confirm New Password | Enter the password again. |

|   | Cloud Native Distributed Database |
|---|---|

| Parameter | Description |
|---|---|
| Authorize Databases | You can grant permissions on one or more databases to the account. i. From the left-side section, select one or more databases. Then click Add to add them to the right-side section. ii. In the right-side section, select Read/Writ e, Read-only, DDL Only, or DML Only for the specified database. Not e You can also grant permissions on multiple added databases by clicking Set All t o Read-only, Set All t o DDL Only, Set All t o DML Only, or Set All t o Read/Writ e in the upper-right corner of the right-side section. The buttons in the upper-right corner change after you click them. For example, after you click Set All t o Read-only, this button is changed to Set All t o DDL Only. |

Create an account by using the command line Use the following syntax rule:

```
CREATE USER user_specification [, user_specification] ...
  user_specification: user [ auth_option ]
  auth_option: IDENTIFIED BY 'auth_string'
```

For example: Create an account whose name is lily and password is 123456 and which can be used to log on only from 30.xx.xx.96.

```
CREATE USER lily@30.xx.xx.96 IDENTIFIED BY '123456';
```

Create an account that is named david, has no password, and can be used to log on from all hosts.

```
CREATE USER david@'%';
```

### 5.3 Reset password

When you use PolarDB-X 1.0, you can reset the password of your database account in the PolarDB-X 1.0 console or by using the command line.

> Not e
> Accounts that have root permissions cannot be deleted or modified.
> For data security, we recommend that you change your password on a regular basis.

Reset the password in the console
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Account
Management .
5. Find the target account and click Reset Password.
6. In the Reset Account Password dialog box, set New Password and Conf irm New Password.

> Not e The password must meet the following requirements:
> The password must be 8 to 32 characters in length.
> The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
> Special characters include the following characters:
> ! @#$%^&*()_+-

7. After you confirm that the password is correct, click OK.
Reset the password by using the command line Use the following syntax rule:

```
    SET PASSWORD FOR user = password_option
    password_option: {
        PASSWORD('auth_string')
```

`}` For example: Change the password of the lily@30.xx.xx.96 account to 123456.

```
SET PASSWORD FOR lily@30.xx.xx.96 = PASSWORD('123456')
```

### 5.4 Modify account permissions

You can modify the account permissions of your instances at any time when you use PolarDB-X 1.0. Precautions Privileged accounts cannot be modified. In the console, you can grant only DML, DDL, read-only, and read/write permissions to standard accounts. If you need more fine-grained authorization, use the command line. Modify account permissions in the console
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Account
Management .
5. Find the target account and click Modif y Permission.
6. In the Modif y Permissions dialog box, grant or remove the permissions on one or more
databases to or from the account. Add databases: From the left-side section, select one or more databases. Then click Add to add them to the right-side section. Remove databases: From the right-side section, select one or more databases. Then click Remove to move the databases to the left-side section. Modify permissions on added databases: In the right-side section, select Read/Writ e, Read-only, DDL Only or DML Only for the specified database.

> Not e You can also grant permissions on multiple added databases by clicking Set All t o Read-only, Set All t o DDL Only, Set All t o DML Only, or Set All t o Read/Writ e in the upper-right corner of the right-side section.
> The buttons in the upper-right corner change after you click them. For example, after you click Set All t o Read-only, this button is changed to Set All t o DDL Only.

7. After the configuration is complete, click OK.
GRANT statement Use the following syntax rule:

```
GRANT
    priv_type[, priv_type] ...
    ON priv_level
    TO user_specification [, user_specification] ...
    [WITH GRANT OPTION]
priv_level: {
  | db_name.*
  | db_name.tbl_name
  | tbl_name
```

`}`

```
user_specification:
    user [ auth_option ]
auth_option: {
    IDENTIFIED BY 'auth_string'
```

`}`

> Not ice
> If the account in the GRANT statement does not exist and no IDENTIFIED BY information is provided, an error message is returned, which indicates that the account does not exist.
> If the account specified in the GRANT statement does not exist but the IDENTIFIED BY information is provided, the account is created and granted with the specified permission.

For example, in the easydb database, create an account named david, which can be used to log on from all hosts and has all the permissions on easydb. Method 1: Create an account and then grant permissions to the account.

```
CREATE USER david@'%' IDENTIFIED BY 'your#password'; GRANT ALL PRIVILEGES ON easydb.* to david@'%';
```

Method 2: Create an account and grant permissions to the account by executing a statement.

```
GRANT ALL PRIVILEGES ON easydb.* to david@'%' IDENTIFIED BY 'your#password';
```

In the easydb database, create an account named hanson, which can be used to log on from all hosts and has all the permissions on the easydb.employees table.

```
GRANT ALL PRIVILEGES ON easydb.employees to hanson@'%' IDENTIFIED BY 'your#password';
```

In the easydb database, create an account named hanson, which can be used to log on only from 192.xx.xx.10 and has the INSERT and SELECT permissions on the easydb.emp table.

```
GRANT INSERT,SELECT ON easydb.emp to hanson@'192.xx.xx.10' IDENTIFIED BY 'your#password';
```

In the easydb database, create a read-only account named actro, which can be used to log on from all hosts.

```
GRANT SELECT ON easydb.* to actro@'%' IDENTIFIED BY 'your#password';
```

REVOKE statement Use the following syntax rule: Delete specific permissions from an account: Delete the permissions at a certain level from an account. The permission level is specified by priv_level.

```
REVOKE
    priv_type
      [, priv_type] ...
    ON priv_level
    FROM user [, user] ...
```

Delete all permissions from an account: Delete all permissions from the account at the database and table levels.

```
REVOKE ALL PRIVILEGES, GRANT OPTION
    FROM user [, user] ...
```

For example: Delete the CREATE, DROP, and INDEX permissions from hanson@'%' on the easydb.emp table.

```
REVOKE CREATE,DROP,INDEX ON easydb.emp FROM hanson@'%';
```

Delete all permissions from the lily@30.xx.xx.96 account.

```
REVOKE ALL PRIVILEGES,GRANT OPTION FROM lily@30.xx.xx.96;
```

> Not ice GRANT OPTION must be added to the statement for compatibility with MySQL.

SHOW GRANTS statement Use the following syntax rule:

```
SHOW GRANTS[FOR user@host];
```

Query all permissions:

```
SHOW GRANTS;
```

Query the permissions of an account:

```
SHOW GRANTS FOR user@host;
```

### 5.5 Delete an account

You can delete an account in the Cloud Native Distributed Database PolarDB-X (PolarDB-X) console or by using the command line. Delete an account in the PolarDB-X console

> Not e You can delete only standard accounts that are created in the console.

1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Account
Management .
5. Find the target account and click Delet e.
6. In the Delet e Account dialog box, click OK.
Delete an account by using the command line Use the following syntax rule:

```
DROP USER user [, user] ...
```

For example: Delete the lily@30.xx.xx.96 account.

```
DROP USER lily@30.xx.xx.96;
```

## 6 Database management

### 6.1 Create a database

After you create a PolarDB-X 1.0 instance, you must create a database that contains one or more ApsaraDB RDS for MySQL instances. You can create a database in four steps. Prerequisites You have created an ApsaraDB RDS for MySQL instance in the same department of PolarDB-X 1.0. You have granted the Resource Access Management (RAM) permission. For more information, see ASC M Console User Guide for the RAM topic.
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. On the Basic Inf ormat ion page, click Creat e Dat abase in the upper-right corner.
5. In the Ent er Basic Inf ormat ion step, enter the following information.

| Parameter | Description |
|---|---|
| Partition Mode | Select Horizont al Part it ioning. |
| Database Name | Specify a name for the PolarDB-X 1.0 database. The name must meet the following requirements: It must be 2 to 24 characters in length. It must start with a letter and end with a letter or digit. It can contain lowercase letters, digits, and underscores ( ). _ It must be unique on the PolarDB-X instance. |
| Character Set | Select utf8, gbk, latin1, or utf8mb4. |
| DRDS Link Password | Set the connection password for the PolarDB-X 1.0 database. The rules are listed in the following content: The password must be 8 to 30 characters in length. The password must contain at least three of the following types: uppercase letters, lowercase letters, numbers, and underscores ( ). _ |
| Confirm Password | Enter the password again. |

6. Click Next .
7. In the Select RDS Inst ance step, you can click the Buy New RDS Inst ance or Use Exist ing RDS
Inst ance tab. i. Buy New RDS Inst ance: Click the Buy New RDS Inst ance tab. ii. Select St orage T ype, Edit ion, Inst ance Specif icat ions, St orage Capacit y, Zone, and Quant it y. iii. Click Next . i. Use Exist ing RDS Inst ance: Click the Use Exist ing RDS Inst ance tab. ii. In the left-side section, click the ApsaraDB RDS for MySQL instances to be added. iii. Click to move the selected instances to the Select ed RDS Inst ances section on the right. iv. Click Next .
8. After all prechecks are passed in the Precheck step, click Next .

> Not e If a precheck fails, rectify the configuration as prompted.

9. In the Preview step, click Next . Wait until the database is created.

### 6.2 View a database

After the database is created, you can view the basic information of the database on the Database Management page in the console. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Dat abase
Management .
5. Find the target database, and click Manage in the Actions column. The Basic Inf ormat ion page
of the database appears.

> Not e On the Basic Inf ormat ion page, you can delete the database or reset the password.

What's next PolarDB-X 1.0 is fully compatible with the MySQL protocol. You can use Command Line URL on the MySQL client to connect to the PolarDB-X 1.0 instance and enter the user name and password to log on to the PolarDB-X 1.0 database. When you use the MySQL client, note the following points:

> Not e
> MySQL clients of some earlier versions have limits on the user name length, which cannot exceed 16 characters. The PolarDB-X 1.0 database name and user name are the same. If the database name exceeds 16 characters in length, an error is reported.
> When you use the MySQL client, you must add the `-c` parameter to the HINT command. In
> PolarDB-X 1.0, an annotation is used to implement HINT. If the `-c` parameter is not
> added, the annotation is lost and the HINT of PolarDB-X 1.0 is lost.

### 6.3 Perform smooth scale-out

When the underlying storage of the logical database reaches the physical bottleneck, for example, when the remaining disk space is about 30%, you can smoothly scale it out to improve the performance. The smooth scale-out process is divided into four steps: configuration > migration > switchover > cleanup. Configuration

> Not e In smooth scale-out, ApsaraDB RDS for MySQL instances are added, and some source database shards are migrated to the new ApsaraDB RDS for MySQL instances. In this way, the overall data storage capacity is increased and the number of requests that a single ApsaraDB RDS for MySQL instance needs to process is reduced.

1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Dat abase
Management .
5. Find the target database, and click Manage. in the Actions column The Basic Inf ormat ion page
of the database appears.
6. In the left-side navigation pane, choose Conf igurat ion and Management > Scale-out
Management .
7. In the upper-right corner of the Scale-out Management page, click Scale Out .
8. Select Smoot h Scale-out , and then click Next .
9. After all prechecks are passed in the Precheck step, click Next .

> Not e If a precheck fails, rectify the configuration as prompted.

10. In the Select RDS Inst ance step, you can click the Buy New RDS Inst ance or Use Exist ing RDS
Inst ance tab. i. Buy New RDS Inst ance: Click the Buy New RDS Inst ance tab. ii. Select St orage T ype, Edit ion, Inst ance Specif icat ions, St orage Capacit y, Zone, and Quant it y. iii. Click Next . i. Use Exist ing RDS Inst ance: Click the Use Exist ing RDS Inst ance tab. ii. In the left-side section, click the ApsaraDB RDS for MySQL instances to be added. iii. Click to move the selected instances to the Select ed RDS Inst ances section on the right. iv. Click Next .
11. In the Preview step, click St art Scale-out .

> Not e By default, the console evenly distributes the physical database shards to the ApsaraDB RDS for MySQL instances you added. You can also manually add or delete physical database shards to or from the new ApsaraDB RDS for MySQL instances.

12. Click the
icon in the upper-right corner to view the progress of the scale-out task. Migration Some physical database shards are migrated during smooth scale-out. The migration does not change the data in the source database and therefore does not affect online services. Before the switchover, you can cancel the smooth scale-out operation by using a rollback.

> Not e
> This is because before the switchover, the current scale-out operation does not have a real impact on the data in the source database.
> During scale-out, the binary log files of the source RDS instance are not cleaned, which may result in insufficient disk space. Therefore, you must reserve sufficient disk space on the source ApsaraDB RDS for MySQL instance. Generally, the remaining disk space needs to be more than 30%. If the disk space cannot be guaranteed, you can submit a ticket to expand the storage space of the ApsaraDB RDS for MySQL instance.
> To reduce the pressure of read operations on the source RDS instance, perform scale-out when the load on the source ApsaraDB RDS for MySQL instance is low.
> During the scale-out, do not submit data description language (DDL) tasks in the console or connect to the PolarDB-X 1.0 instance to directly run DDL statements. Otherwise, the scale- out task may fail.
> Make sure that all tables in the source database have primary keys before scale-out.

After historical data and incremental data are migrated, the migration progress reaches 100%. Then, you can swit ch the read/write traffic to the new ApsaraDB RDS for MySQL instance or roll back to cancel this scale-out. Switchover The switchover task switches the read/write traffic to the new ApsaraDB RDS for MySQL instance. The whole process takes three to five minutes. During the switchover process, the service is not affected except for one or two transient disconnections. Perform the switchover during off-peak hours.
1. In the upper-right corner of the Basic Inf ormat ion page, click the
icon. The T ask Progress dialog box appears.
2. In the T ask Progress dialog box, click Swit ch Over and then click OK.
During the switchover process, a switchover task is generated and appears in the task progress.
3. After the switchover is completed, the Clean Up button appears in the T ask Progress dialog box.
Cleanup In this step, the migrated database shards are deleted from the source ApsaraDB RDS for MySQL instance.
1. After switchover is completed, click Clean Up next to the target task.
2. Click OK. A cleanup task appears in the Task Progress dialog box.

> Not e
> The cleanup task is an asynchronous task. You can view the execution status in the Task Progress dialog box.
> After the cleanup task is completed, the smooth scale-out process ends. The new ApsaraDB RDS for MySQL instance becomes the storage node of the PolarDB-X 1.0 logical database.
> You can implement smooth scale-out by migrating physical database shards. If no further scale-out is allowed after the number of database shards exceeds the capacity of a single ApsaraDB RDS for MySQL instance, you can submit a ticket to apply for increasing the number of database shards and scaling out the database. In this case, calculation based on the hash algorithm is performed again to reallocate data.
> The cleanup task deletes database shards that are no longer used after the current scale-out. You can back up the database shards before you run the cleanup task.
> The cleanup operation brings pressure to databases. We recommend that you perform this operation during off-peak hours.

### 6.4 View database monitoring information

information PolarDB-X 1.0 displays the historical monitoring information of a PolarDB-X 1.0 database in two dimensions: data metrics and query time. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Monit oring and Alert s > Dat abase Monit oring.
5. Select the target dat abase, and then set Dat a Indexes and Query T ime. You can see the
corresponding monitoring information. Not e For more information about instance-level monitoring, see View monitoring information.

### 6.5 Set the IP address whitelist

PolarDB-X 1.0 provides the access control feature. Only IP addresses in the whitelist of a database can be used to access the database. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Dat abase
Management .
5. Find the target database, and click Manage in the Actions column. The Basic Inf ormat ion page
of the database appears.
6. On the Basic Inf ormat ion page of the database, choose Dat a Securit y > Whit elist Set t ings in
the left-side navigation pane.
7. On the Whitelist Settings page, click Manually Modif y.
8. Enter the IP addresses that are allowed to access the database, and click OK.

> Not e
> The following formats are supported in the whitelist:
> Single IP addresses, for example, 192.168.1.1.
> IP addresses in CIDR format, for example, 192.168.1.1/24.
> IP addresses that includes an asterisk (*) as a wildcard, for example, 192.168.1. *. This example indicates that access is allowed from a host with an IP address in the range from 192.168.1.1 to 192.168.1.254.
> IP range, for example, 192.168.1.1-192.168.1.254.
> If you need to add multiple IP addresses or IP ranges, separate them with commas (,) and do not use spaces before and after the commas, for example, 192.168.0.1,172.16.213.9.

### 6.6 Delete a database

This topic describes how to delete a database in the Cloud Native Distributed Database PolarDB-X (PolarDB-X) console. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Dat abase
Management .
5. Find the target database and click Delet e.

> **Warning:** You cannot recover databases that have been deleted. Exercise caution when you perform this operation.

6. In the Delet e Dat abase dialog box, click OK.

### 6.7 Fix database shard connections

Context When you use a PolarDB-X 1.0 instance, you must access ApsaraDB RDS for MySQL. If the network configuration of the connected ApsaraDB RDS for MySQL instance changes, for example, if the zone is switched or the network type is changed from classic network to VPC, the network connection between the PolarDB-X 1.0 instance and the ApsaraDB RDS for MySQL instance is broken. As a result, the PolarDB- X 1.0 instance cannot access the ApsaraDB RDS for MySQL instance. In this case, you must manually fix the database shard link in the PolarDB-X 1.0 console to restore the network connection from the PolarDB-X 1.0 instance to the ApsaraDB RDS for MySQL instance. Procedure
1. Log on to the PolarDB-X console.
2. Find the target instance in the instance list.
3. Click the target instance ID or choose More > Manage from the Actions column of the instance to
access the Basic Inf ormat ion page.
4. In the left-side navigation pane, choose Conf igurat ion and Management > Dat abase
Management .
5. Find the target database, and click Manage in the Actions column. The Basic Inf ormat ion page
of the database appears.
6. In the Short cut s section, click Fix Dat abase Shard Connect ions.
7. In the dialog box that appears, click OK.
ds

## 7 Custom control commands

PolarDB-X 1.0 provides a series of auxiliary SQL commands to help you conveniently use PolarDB-X 1.0.

### 7.1 Overview

PolarDB-X 1.0 provides unique auxiliary statements for you to use and maintain PolarDB-X 1.0. Syntax description: The identifier provided by the user is in [] and optional content is in (). In addition, this document applies to the current version. If some statements are unavailable, the version is earlier than required.

### 7.2 Help statements

This topic describes all the auxiliary SQL commands of PolarDB-X 1.0 and their descriptions. SHOW HELP statements: ds

```
mysql> show help; +-----------------------------------------+------------------------------------------------ ---------+---------------------------------------------+
| STATEMENT                               | DESCRIPTION
| EXAMPLE                                     |
+-----------------------------------------+------------------------------------------------ ---------+---------------------------------------------+
| show rule                               | Report all table rule
|                                             |
| show rule from TABLE                    | Report table rule
| show rule from user                         |
| show full rule from TABLE               | Report table full rule
| show full rule from user                    |
| show topology from TABLE                | Report table physical topology
| show topology from user                     |
| show partitions from TABLE              | Report table dbPartition or tbPartition columns
| show partitions from user                   |
| show broadcasts                         | Report all broadcast tables
|                                             |
| show datasources                        | Report all partition db threadPool info
|                                             |
| show node                               | Report master/slave read status
|                                             |
| show slow                               | Report top 100 slow sql
|                                             |
| show physical_slow                      | Report top 100 physical slow sql
|                                             |
| clear slow                              | Clear slow data
|                                             |
| trace SQL                               | Start trace sql, use show trace to print profil
ing data | trace select count(*) from user; show trace |
| show trace                              | Report sql execute profiling info
|                                             |
| explain SQL                             | Report sql plan info
| explain select count(*) from user           |
| explain detail SQL                      | Report sql detail plan info
| explain detail select count(*) from user    |
| explain execute SQL                     | Report sql on physical db plan info
| explain execute select count(*) from user   |
| show sequences                          | Report all sequences status
|                                             |
| create sequence NAME [start with COUNT] | Create sequence
| create sequence test start with 0           |
| alter sequence NAME [start with COUNT]  | Alter sequence
| alter sequence test start with 100000       |
| drop sequence NAME                      | Drop sequence
| drop sequence test                          |
+-----------------------------------------+------------------------------------------------ ---------+---------------------------------------------+ 20 rows in set (0.00 sec)
```

ds

### 7.3 Statements for viewing rules and node topologies

node topologies SHOW RULE [FROM tablename] Usage notes:

| show rule | : shows the part |
|---|---|
| show rule from tablename |   |

`show rule` : shows the partitioning status of each logical table in a database. `show rule from tablename` : shows the partitioning status of a specified logical table in a database. The following describes the meanings of important columns: BROADCAST: indicates whether the table is a broadcast table. 0 indicates "No" and 1 indicates "Yes". DB_PARTITION_KEY: indicates the database shard key. If no database shards exist, the parameter value is NULL. DB_PARTITION_POLICY: indicates the database sharding policy. Options are Hash and date policies such as YYYYMM, YYYYDD, and YYYYWEEK. DB_PARTITION_COUNT: indicates the number of database shards. TB_PARTITION_KEY: indicates the table shard key. If no table shards exist, the parameter value is NULL. TB_PARTITION_POLICY: indicates the table sharding policy. Options are Hash and date policies such as MM, DD, MMDD, and WEEK. TB_PARTITION_COUNT: indicates the number of table shards.

```
mysql> show rule; +------+--------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME   | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+--------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | dept_manager |         0 |                  | NULL                | 1
|                  | NULL                | 1                  |
|    1 | emp          |         0 | emp_no           | hash                | 8
| id               | hash                | 2                  |
|    2 | example      |         0 | shard_key        | hash                | 8
|                  | NULL                | 1                  |
+------+--------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 3 rows in set (0.01 sec)
```

SHOW FULL RULE [FROM tablename] You can run this SQL statement to view the sharding rules of logical tables in a database. It displays more detailed information than the SHOW RULE command. The following describes the meanings of important columns: BROADCAST: indicates whether the table is a broadcast table. 0 indicates "No" and 1 indicates "Yes". ds JOIN_GROUP: a reserved field. ALLOW_FULL_TABLE_SCAN: indicates whether to allow data querying when no table shard key is specified for database or table sharding. If this parameter is set to True, each physical table is scanned to find data that meets the condition, which is a full table scan. DB_NAME_PATTERN: The value 0 between {} in DB_NAME_PATTERN is a placeholder. When the SQL statement is run, this value is replaced by the value of DB_RULES_STR, with the number of digits unchanged. For example, if the value of DB_NAME_PATTERN is SEQ_{0000}_RDS and the value of DB_RULES_STR is [1,2,3,4], four DB_NAME values are generated: SEQ_0001_RDS, SEQ_0002_RDS, SEQ_0003_RDS, and SEQ_0004_RDS. DB_RULES_STR: indicates the database sharding rule. TB_NAME_PATTERN: The value 0 between {} in TB_NAME_PATTERN is a placeholder. When the SQL statement is run, this value is replaced by the value of TB_RULES_STR, with the number of digits unchanged. For example, if the value of TB_NAME_PATTERN is table_{00} and the value of TB_RULES_STR is [1,2,3,4,5,6,7,8], eight tables are generated: table_01, table_02, table_03, table_04, table_05, table_06, table_07, and table_08. TB_RULES_STR: indicates the table sharding rule. PARTITION_KEYS: indicates a set of database and table shard keys. When database sharding and table sharding coexist, the database shard key is placed before the table shard key. DEFAULT_DB_INDEX: indicates the database shard in which a single database and a single table are stored.

```
mysql> show full rule; +------+--------------+-----------+------------+-----------------------+------------------- ---------------------------------+-----------------------------------------------------+--- --------------+------------------------------------+----------------+---------------------- ----------------------------+
| ID   | TABLE_NAME   | BROADCAST | JOIN_GROUP | ALLOW_FULL_TABLE_SCAN | DB_NAME_PATTERN
| DB_RULES_STR                                        | TB_NAME_PATTERN | TB_RULES_STR
| PARTITION_KEYS | DEFAULT_DB_INDEX                                 |
+------+--------------+-----------+------------+-----------------------+------------------- ---------------------------------+-----------------------------------------------------+--- --------------+------------------------------------+----------------+---------------------- ----------------------------+
|    0 | dept_manager |         0 | NULL       |                     0 | SEQ_TEST_148776778
0814RGKKSEQ_TEST_WNJG_0000_RDS | NULL | de pt_manager | NULL | NULL | SEQ_TEST_148776778081 4RGKKSEQ_TEST_WNJG_0000_RDS |
|    1 | emp          |         0 | NULL       |                     1 | SEQ_TEST_148776778
0814RGKKSEQ_TEST_WNJG_{0000}_RDS | ((#emp_no,1,8#).longValue().abs() % 8) | em p_{0} | ((#id,1,2#).longValue().abs() % 2) | emp_no id | SEQ_TEST_148776778081 4RGKKSEQ_TEST_WNJG_0000_RDS |
|    2 | example      |         0 | NULL       |                     1 | SEQ_TEST_148776778
0814RGKKSEQ_TEST_WNJG_{0000}_RDS | ((#shard_key,1,8#).longValue().abs() % 8).intdiv(1) | ex ample | NULL | shard_key | SEQ_TEST_148776778081 4RGKKSEQ_TEST_WNJG_0000_RDS | +------+--------------+-----------+------------+-----------------------+------------------- ---------------------------------+-----------------------------------------------------+--- --------------+------------------------------------+----------------+---------------------- ----------------------------+ 3 rows in set (0.01 sec)
```

ds SHOW TOPOLOGY FROM tablename You can run this SQL statement to view the topology of a specified logical table, that is, the database shards to which data in the logical table is partitioned and the table shards in each database shard.

```
mysql> show topology from emp; +------+--------------------------------------------------+------------+
| ID   | GROUP_NAME                                       | TABLE_NAME |
+------+--------------------------------------------------+------------+
|    0 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0000_RDS | emp_0      |
|    1 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0000_RDS | emp_1      |
|    2 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0001_RDS | emp_0      |
|    3 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0001_RDS | emp_1      |
|    4 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0002_RDS | emp_0      |
|    5 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0002_RDS | emp_1      |
|    6 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0003_RDS | emp_0      |
|    7 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0003_RDS | emp_1      |
|    8 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0004_RDS | emp_0      |
|    9 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0004_RDS | emp_1      |
|   10 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0005_RDS | emp_0      |
|   11 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0005_RDS | emp_1      |
|   12 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0006_RDS | emp_0      |
|   13 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0006_RDS | emp_1      |
|   14 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0007_RDS | emp_0      |
|   15 | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0007_RDS | emp_1      |
+------+--------------------------------------------------+------------+ 16 rows in set (0.01 sec)
```

SHOW PARTITIONS FROM tablename You can run this SQL statement to view the set of database shard keys and table shard keys, which are separated by commas (,). If the final result contains two values, both database sharding and table sharding are performed. The first value is the database shard key and the second value is the table shard key. If only one value is returned, only database sharding is performed. This value is the database shard key.

```
mysql> show partitions from emp; +-----------+
| KEYS      |
+-----------+
| emp_no,id |
+-----------+ 1 row in set (0.00 sec)
```

SHOW BROADCASTS You can run this SQL statement to view the list of broadcast tables. ds

```
mysql> show broadcasts; +------+------------+
| ID   | TABLE_NAME |
+------+------------+
|    0 | brd2       |
|    1 | brd_tbl    |
+------+------------+ 2 rows in set (0.01 sec)
```

SHOW DATASOURCES You can run this SQL statement to view the information about the underlying storage, including the database name, database group name, connection URL, user name, storage type, read/write weight, and connection pool information. The following describes the meanings of important columns: SCHEMA: indicates the database name. GROUP: indicates the database group name. Grouping aims to manage multiple groups of databases that have identical data, such as the primary and secondary databases after data replication through ApsaraDB RDS for MySQL. It is mainly used for read/write splitting and primary/secondary switchovers. URL: indicates the connection information of the underlying ApsaraDB RDS for MySQL instance. TYPE: indicates the type of the underlying storage. Currently, only ApsaraDB RDS for MySQL instances are supported. READ_WEIGHT: indicates the read weight of the database. When the primary ApsaraDB RDS for MySQL instance is under a heavy load of many read requests, you can use the read/write splitting function of PolarDB-X 1.0 to distribute the read traffic. PolarDB-X 1.0 automatically identifies the read and write traffic. It directs the write traffic to the primary ApsaraDB RDS for MySQL instance and the read traffic to all ApsaraDB RDS for MySQL instances based on the configured weight. WRITE_WEIGHT: indicates the write weight. For more information, see READ_WEIGHT.

```
mysql> show datasources; +------+----------------------------+------------------------------------------------+----- ---------------------------------------------+--------------------------------------------- -------------------------------------+-----------+-------+------+------+------+------------ --+----------+--------------+---------------+---------------------------------------------- +-------------+--------------+
| ID   | SCHEMA                     | NAME                                           | GROU
P | URL
| USER      | TYPE  | INIT | MIN  | MAX  | IDLE_TIMEOUT | MAX_WAIT | ACTIVE_COUNT | POOLING
_COUNT | ATOM | READ_WEIGHT | WRITE_WEIGHT | +------+----------------------------+------------------------------------------------+----- ---------------------------------------------+--------------------------------------------- -------------------------------------+-----------+-------+------+------+------+------------ --+----------+--------------+---------------+---------------------------------------------- +-------------+--------------+
|    0 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0000_iiab_1 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0000_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0000 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0000_iiab |
10 | 10 |
|    1 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0001_iiab_2 | SEQ_
TEST1487767780814RGKKSEQTESTWNJG0001RDS|jdb l//d1 80k 83t63l
```

`l` `d` ds

```
TEST_1487767780814RGKKSEQ_TEST_WNJG_0001_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0001 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0001_iiab |
10 | 10 |
|    2 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0002_iiab_3 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0002_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0002 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0002_iiab |
10 | 10 |
|    3 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0003_iiab_4 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0003_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0003 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0003_iiab |
10 | 10 |
|    4 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0004_iiab_5 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0004_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0004 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0004_iiab |
10 | 10 |
|    5 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0005_iiab_6 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0005_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0005 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0005_iiab |
10 | 10 |
|    6 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0006_iiab_7 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0006_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0006 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0006_iiab |
10 | 10 |
|    7 | seq_test_1487767780814rgkk | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0007_iiab_8 | SEQ_
TEST_1487767780814RGKKSEQ_TEST_WNJG_0007_RDS | jdbc:mysql://rds1ur80kcv8g3t6p3ol.mysql.rds. aliyuncs.com:3306/seq_test_wnjg_0007 | jnkinsea0 | mysql | 0 | 24 | 72 | 15
| 5000     | 0            | 1             | rds1ur80kcv8g3t6p3ol_seq_test_wnjg_0007_iiab |
10 | 10 | +------+----------------------------+------------------------------------------------+----- ---------------------------------------------+--------------------------------------------- -------------------------------------+-----------+-------+------+------+------+------------ --+----------+--------------+---------------+---------------------------------------------- +-------------+--------------+ 8 rows in set (0.01 sec)
```

SHOW NODE You can run this SQL statement to view the accumulative number of read and write operations and accumulative read/write weights of a physical database. The following describes the meanings of important columns: MASTER_READ_COUNT: indicates the accumulative number of read-only queries processed by the primary ApsaraDB RDS for MySQL instance. SLAVE_READ_COUNT: indicates the accumulative number of read-only queries processed by the secondary ApsaraDB RDS for MySQL instances. MASTER_READ_PERCENT: indicates the actual percentage of read-only queries processed by the primary ApsaraDB RDS for MySQL instance, not the configured percentage. ds SLAVE_READ_PERCENT: indicates the actual percentage of read-only queries processed by the secondary ApsaraDB RDS for MySQL instances, not the configured percentage.

> Not e
> Read-only queries in transactions are sent to the primary ApsaraDB RDS for MySQL instance.
> The `MASTER_READ_PERCENT` and `SLAVE_READ_PERCENT` fields indicate the accumulative
> historical data. After the read/write weight ratio has been changed, these values do not immediately reflect the latest read/write weight ratio, which appears after a long period of time has passed.

```
mysql> show node; +------+--------------------------------------------------+-------------------+------------ ------+---------------------+--------------------+
| ID   | NAME                                             | MASTER_READ_COUNT | SLAVE_READ_
COUNT | MASTER_READ_PERCENT | SLAVE_READ_PERCENT | +------+--------------------------------------------------+-------------------+------------ ------+---------------------+--------------------+
| 0    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0000_RDS |                12 |
0 | 100% | 0% |
| 1    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0001_RDS |                 0 |
0 | 0% | 0% |
| 2    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0002_RDS |                 0 |
0 | 0% | 0% |
| 3    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0003_RDS |                 0 |
0 | 0% | 0% |
| 4    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0004_RDS |                 0 |
0 | 0% | 0% |
| 5    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0005_RDS |                 0 |
0 | 0% | 0% |
| 6    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0006_RDS |                 0 |
0 | 0% | 0% |
| 7    | SEQ_TEST_1487767780814RGKKSEQ_TEST_WNJG_0007_RDS |                 0 |
0 | 0% | 0% | +------+--------------------------------------------------+-------------------+------------ ------+---------------------+--------------------+ 8 rows in set (0.01 sec)
```

### 7.4 SQL tuning statements

SHOW [FULL] SLOW [WHERE expr] [limit expr] SQL statements that take more than 1 second to execute are slow SQL statements. Slow logical SQL statements are the slow SQL statements sent from an application to a PolarDB-X 1.0 instance. `SHOW SLOW` : You can run this SQL statement to view the 100 slowest logical SQL queries that are recorded since the PolarDB-X 1.0 instance is started or the last time when `CLEAR SLOW` is executed.

> Not e The recorded 100 slowest SQL queries are stored in the PolarDB-X 1.0 system. When the PolarDB-X instance is restarted or executes `CLEAR SLOW` , these queries will be discarded.

ds `SHOW FULL SLOW` : You can run this SQL statement to view all the slow logical SQL queries that are recorded and persisted to the built-in database of the PolarDB-X 1.0 instance since the PolarDB-X instance is started. The upper limit for the number of records is specified in the specifications of the PolarDB-X instance. The PolarDB-X 1.0 instance scrolls to delete the earliest slow SQL statements. If the specifications of the PolarDB-X instance is 4-core 4 GB, a maximum of 10,000 slow SQL statements can be recorded, including slow logical and physical SQL statements. If the specifications of the PolarDB-X instance is 8-core 8 GB, a maximum of 20,000 slow SQL statements can be recorded, including slow logical and physical SQL statements. The same rule applies to other specifications. The following describes the meanings of important columns: HOST: the IP address of the host from which the SQL statement is sent. START_TIME: the time when the SQL statement starts to be executed. EXECUTE_TIME: the time when the SQL statement is executed. AFFECT_ROW: For data manipulation language (DML) statements, this parameter indicates the number of affected rows. For query statements, this parameter indicates the number of returned records.

```
mysql> show slow where execute_time > 1000 limit 1; +-----------+---------------------+--------------+------------+-----------+
| HOST      | START_TIME          | EXECUTE_TIME | AFFECT_ROW | SQL       |
+-----------+---------------------+--------------+------------+-----------+
| 127.0.0.1 | 2016-03-16 13:02:57 |         2785 |          7 | show rule |
+-----------+---------------------+--------------+------------+-----------+ 1 row in set (0.02 sec)
```

SHOW [FULL] PHYSICAL_SLOW [WHERE expr] [limit expr] SQL statements that take more than 1 second to execute are slow SQL statements. Slow logical SQL statements are the slow SQL statements sent from an application to a PolarDB-X 1.0 instance. `SHOW SLOW` : You can run this SQL statement to view the 100 slowest logical SQL queries that are recorded since the PolarDB-X 1.0 instance is started or the last time when `CLEAR SLOW` is executed.

> Not e The recorded 100 slowest SQL queries are stored in the PolarDB-X 1.0 system. When the PolarDB-X instance is restarted or executes `CLEAR SLOW` , these queries will be discarded.

`SHOW FULL SLOW` : You can run this SQL statement to view all the slow logical SQL queries that are recorded and persisted to the built-in database of the PolarDB-X 1.0 instance since the PolarDB-X instance is started. The upper limit for the number of records is specified in the specifications of the PolarDB-X instance. The PolarDB-X 1.0 instance scrolls to delete the earliest slow SQL statements. If the specifications of the PolarDB-X instance is 4-core 4 GB, a maximum of 10,000 slow SQL statements can be recorded, including slow logical and physical SQL statements. If the specifications of the PolarDB-X instance is 8-core 8 GB, a maximum of 20,000 slow SQL statements can be recorded, including slow logical and physical SQL statements. The same rule applies to other specifications. The following describes the meanings of important columns: GROUP_NAME: the name of the group to which the database that executes the SQL statement belongs. START_TIME: the time when the SQL statement starts to be executed. EXECUTE_TIME: the time when the SQL statement is executed. ds AFFECT_ROW: For data manipulation language (DML) statements, this parameter indicates the number of affected rows. For query statements, this parameter indicates the number of returned records.

```
mysql> show physical_slow; +----------------+-----------------------------------+---------------------+--------------+ ------------------+-------------------------+------------------------+------------+-------- ---------+
| GROUP_NAME     | DBKEY_NAME                        | START_TIME          | EXECUTE_TIME |
SQL_EXECUTE_TIME | GETLOCK_CONNECTION_TIME | CREATE_CONNECTION_TIME | AFFECT_ROW | SQL
```

|

```
+----------------+-----------------------------------+---------------------+--------------+ ------------------+-------------------------+------------------------+------------+-------- ---------+
| TDDL5_00_GROUP | db218249098_sqa_zmf_tddl5_00_3309 | 2016-03-16 13:05:38 |         1057 |
1011 | 0 | 0 | 1 | select sleep(1) | +----------------+-----------------------------------+---------------------+--------------+ ------------------+-------------------------+------------------------+------------+-------- ---------+ 1 row in set (0.01 sec)
```

CLEAR SLOW You can run this SQL statement to clear the 100 slowest logical SQL queries and the 100 slowest physical SQL queries that are recorded since the PolarDB-X 1.0 instance is started or the last time when `CLEAR SLOW` is executed.

> Not e Both `SHOW SLOW` and `SHOW PHYSICAL_SLOW` can be executed to display the 100
> slowest SQL statements. If `CLEAR SLOW` has not been executed for a long time, these SQL
> statements may have been recorded a long time ago. Therefore, after SQL tuning statements are executed, we recommend that you execute `CLEAR SLOW` . After the system runs for a while, check
> the tuning results of slow SQL statements.

```
mysql> clear slow; Query OK, 0 rows affected (0.00 sec)
```

EXPLAIN SQL You can run this SQL statement to view the execution plan of a specified SQL statement in the PolarDB- X 1.0. Note that this SQL statement is not truly executed. Example: You can run this SQL statement to view the execution plan of the SQL `select * from doctest` statement. The doctest table is stored in database shards according to values in the id column. According to the execution plan, the SQL statement will be routed to each database shard for execution, and the execution results will be aggregated. ds

```
mysql> explain select * from doctest; +------------------------------------------------+--------------------------------------+-- ------+
| GROUP_NAME                                     | SQL                                  | P
ARAMS | +------------------------------------------------+--------------------------------------+-- ------+
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0000_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0001_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0002_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0003_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0004_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0005_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0006_RDS | select `doctest`.`id` from `doctest` | {
} |
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0007_RDS | select `doctest`.`id` from `doctest` | {
} | +------------------------------------------------+--------------------------------------+-- ------+ 8 rows in set (0.00 sec)
```

You can run this SQL statement to view the execution plan of the SQL `select * from doctest where` `id = 1` statement. The doctest table is stored in database shards according to values in the id column. According to the execution plan, the PolarDB-X instance will calculate a specified database shard based on the shard key, which is id, directly route the SQL statement to the database shard, and aggregate the execution results.

```
mysql> explain select * from doctest where id = 1; +------------------------------------------------+----------------------------------------- ------------------------+--------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ------------------------+--------+
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0001_RDS | select `doctest`.`id` from `doctest` whe
re (`doctest`.`id` = 1) | {} | +------------------------------------------------+----------------------------------------- ------------------------+--------+ 1 row in set (0.01 sec)
```

EXPLAIN DETAIL SQL You can run this SQL statement to view the execution plan of a specified SQL statement in the PolarDB- X 1.0. Note that this SQL statement is not truly executed. ds

```
mysql> explain detail select * from doctest where id = 1; +------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------+--------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------+--------+
| DOCTEST_1488704345426RCUPDOCTEST_CAET_0001_RDS | Query from doctest as doctest
    keyFilter:doctest.id = 1
    queryConcurrency:SEQUENTIAL
    columns:[doctest.id]
    tableName:doctest
    executeOn:DOCTEST_1488704345426RCUPDOCTEST_CAET_0001_RDS
 | NULL   |
+------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------+--------+ 1 row in set (0.02 sec)
```

EXPLAIN EXECUTE SQL You can run this SQL statement to view the execution plan of underlying storage. This statement is equivalent to the MySQL EXPLAIN statement.

```
mysql> explain execute select * from tddl_mgr_log limit 1; +----+-------------+--------------+------+---------------+------+---------+------+------+-- -----+
| id | select_type | table        | type | possible_keys | key  | key_len | ref  | rows | E
xtra | +----+-------------+--------------+------+---------------+------+---------+------+------+-- -----+
|  1 | SIMPLE      | tddl_mgr_log | ALL  | NULL          | NULL | NULL    | NULL |    1 | N
ULL | +----+-------------+--------------+------+---------------+------+---------+------+------+-- -----+ 1 row in set (0.07 sec)
```

TRACE SQL and SHOW TRACE You can run these SQL statements to view the execution results of an SQL statement. Note that you must use TRACE SQL and SHOW TRACE together. The difference between TRACE SQL and EXPLAIN SQL is that TRACE SQL is truly executed. For example, you can run these statements to view the execution results of the select 1 statement. ds

```
mysql> trace select 1; +---+
| 1 |
+---+
| 1 |
+---+ 1 row in set (0.03 sec) mysql> show trace; +------+----------+----------------+-----------------------------------+---------------+--- -----------------------+------+-----------+--------+
| ID   | TYPE     | GROUP_NAME     | DBKEY_NAME                        | TIME_COST(MS) | CO
NNECTION_TIME_COST(MS) | ROWS | STATEMENT | PARAMS | +------+----------+----------------+-----------------------------------+---------------+--- -----------------------+------+-----------+--------+
|    0 | Optimize | DRDS           | DRDS                              | 3             | 0.
00 | 0 | select 1 | NULL |
|    1 | Query    | TDDL5_00_GROUP | db218249098_sqa_zmf_tddl5_00_3309 | 7             | 0.
15 | 1 | select 1 | NULL | +------+----------+----------------+-----------------------------------+---------------+--- -----------------------+------+-----------+--------+ 2 rows in set (0.01 sec)
```

CHECK TABLE tablename You can run this SQL statement to check a data table. This SQL statement is mainly used when a table failed to be created by using a data definition language (DDL) statement. If the data table is a table shard, this SQL statement allows you to check whether any underlying physical table shard is missing and whether the columns and indexes of the underlying physical table are consistent. If the data table is a single-database non-partition table, this SQL statement allows you to check whether this table exists.

```
mysql> check table tddl_mgr_log; +------------------------+-------+----------+----------+
| TABLE                  | OP    | MSG_TYPE | MSG_TEXT |
+------------------------+-------+----------+----------+
| TDDL5_APP.tddl_mgr_log | check | status   | OK       |
+------------------------+-------+----------+----------+ 1 row in set (0.56 sec) mysql> check table tddl_mg; +-------------------+-------+----------+----------------------------------------+
| TABLE             | OP    | MSG_TYPE | MSG_TEXT                               |
+-------------------+-------+----------+----------------------------------------+
| TDDL5_APP.tddl_mg | check | Error    | Table 'tddl5_00.tddl_mg' doesn't exist |
+-------------------+-------+----------+----------------------------------------+ 1 row in set (0.02 sec)
```

SHOW TABLE STATUS [LIKE 'pattern' | WHERE expr] You can run this SQL statement to obtain the information about a table. This command aggregates the data of all underlying physical table shards. ds The following describes the meanings of important columns: NAME: indicates the name of the table. ENGINE: indicates the storage engine of the table. VERSION: indicates the version of the storage engine of the table. ROW_FORMAT: indicates the format of the rows in the table. Valid values include Dynamic, Fixed, and Compressed. The value Dynamic indicates that the row length is variable, for example, is a VARCHAR or BLOB field. The value Fixed indicates that the row length is constant, for example, is a CHAR or INTEGER field. ROWS: indicates the number of rows in the table. AVG_ROW_LENGTH: indicates the average number of bytes in each row. DATA_LENGTH: indicates the data volume of the entire table, in bytes. MAX_DATA_LENGTH: indicates the maximum volume of data that can be stored in the table. INDEX_LENGTH: indicates the size of the disk space occupied by indexes. CREATE_TIME: indicates the time when the table was created. UPDATE_TIME: indicates the time when the table was last updated. COLLATION: indicates the default character set and character sorting rule of the table. CREATE_OPTIONS: indicates all the other options specified when the table was created.

```
mysql> show table status like 'multi_db_multi_tbl'; +--------------------+--------+---------+------------+------+----------------+------------- +-----------------+--------------+-----------+----------------+-----------------------+---- ---------+------------+-----------------+----------+----------------+---------+
| NAME               | ENGINE | VERSION | ROW_FORMAT | ROWS | AVG_ROW_LENGTH | DATA_LENGTH
| MAX_DATA_LENGTH | INDEX_LENGTH | DATA_FREE | AUTO_INCREMENT | CREATE_TIME           | UPD
ATE_TIME | CHECK_TIME | COLLATION | CHECKSUM | CREATE_OPTIONS | COMMENT | +--------------------+--------+---------+------------+------+----------------+------------- +-----------------+--------------+-----------+----------------+-----------------------+---- ---------+------------+-----------------+----------+----------------+---------+
| multi_db_multi_tbl | InnoDB |      10 | Compact    |    2 |          16384 |       16384
|               0 |        16384 |         0 |         100000 | 2017-03-27 17:43:57.0 | NUL
L | NULL | utf8_general_ci | NULL | | | +--------------------+--------+---------+------------+------+----------------+------------- +-----------------+--------------+-----------+----------------+-----------------------+---- ---------+------------+-----------------+----------+----------------+---------+ 1 row in set (0.03 sec)
```

The combination of the SHOW TABLE STATUS statement and the PolarDB-X 1.0 SCAN hint allows you to view the data volume of each physical table shard.

```
mysql> /! TDDL:SCAN='multi_db_multi_tbl'*/show table status like 'multi_db_multi_tbl'; +----------------------+--------+---------+------------+------+----------------+----------- --+-----------------+--------------+-----------+----------------+---------------------+---- ---------+------------+-----------------+----------+----------------+---------+------------ --+
| Name                 | Engine | Version | Row_format | Rows | Avg_row_length | Data_lengt
h | Max_data_length | Index_length | Data_free | Auto_increment | Create_time | Upd ate_time | Check_time | Collation | Checksum | Create_options | Comment | Block_forma t | +----------------------+--------+---------+------------+------+----------------+-----------
```

ds

```
--+-----------------+--------------+-----------+----------------+---------------------+---- ---------+------------+-----------------+----------+----------------+---------+------------ --+
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    1 |          16384 |       1638
4 | 0 | 16384 | 0 | 2 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|
ds
|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_1 | InnoDB |      10 | Compact    |    0 |              0 |       1638
4 | 0 | 16384 | 0 | 1 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
| multi_db_multi_tbl_0 | InnoDB |      10 | Compact    |    1 |          16384 |       1638
4 | 0 | 16384 | 0 | 3 | 2017-03-27 17:43:57 | NUL L | NULL | utf8_general_ci | NULL | | | Original
```

|

```
+----------------------+--------+---------+------------+------+----------------+----------- --+-----------------+--------------+-----------+----------------+---------------------+---- ---------+------------+-----------------+----------+----------------+---------+------------ --+ 16 rows in set (0.04 sec)
```

### 7.5 Statistics query statements

SHOW [FULL] STATS You can run this SQL statement to view the overall statistics. The statistics are instantaneous values. Note that the results of `SHOW FULL STATS` vary with the version. The following describes the meanings of important columns: QPS: the number of queries per second (QPS) sent from an application to the PolarDB-X 1.0 instance. These queries are usually called logical QPS. RDS_QPS: the number of QPS sent from the PolarDB-X 1.0 instance to an ApsaraDB RDS for MySQL instance. These queries are usually called physical QPS. ERROR_PER_SECOND: the total number of errors that occur on the PolarDB-X instance per second. These errors include SQL syntax errors, primary key conflicts, system errors, and connectivity errors. VIOLATION_PER_SECOND: the number of conflicts that occur on primary keys or unique keys per second. MERGE_QUERY_PER_SECCOND: the number of queries processed on multiple tables through database sharding and table sharding per second. ACTIVE_CONNECTIONS: the number of active connections to the PolarDB-X instance. CONNECTION_CREATE_PER_SECCOND: the number of connections that are created for the PolarDB-X instance per second. RT(MS): the time to respond to an SQL query sent from an application to the PolarDB-X 1.0 instance. This response time (RT) is usually called logical RT. RDS_RT(MS): the time to respond to an SQL query sent from the PolarDB-X 1.0 instance to an ApsaraDB RDS for MySQL instance. This RT is usually called physical RT. NET_IN(KB/S): the amount of inbound traffic of the PolarDB-X 1.0 instance per second. NET_OUT(KB/S): the amount of outbound traffic of the PolarDB-X 1.0 instance per second. THREAD_RUNNING: the number of threads that are running in the PolarDB-X instance. HINT_USED_PER_SECOND: the number of SQL queries that contain hints and are processed by the ds PolarDB-X instance per second. HINT_USED_COUNT: the total number of SQL queries that contain hints and have been processed by the PolarDB-X instance since startup. AGGREGATE_QUERY_PER_SECCOND: the number of aggregate SQL queries processed by the PolarDB- X instance per second. AGGREGATE_QUERY_COUNT: the total number of aggregate SQL queries that have been processed by the PolarDB-X instance. TEMP_TABLE_CREATE_PER_SECCOND: the number of temporary tables created in the PolarDB-X instance per second. TEMP_TABLE_CREATE_COUNT: the total number of temporary tables that have been created in the PolarDB-X instance since startup. MULTI_DB_JOIN_PER_SECCOND: the number of multi-database JOIN queries processed by the PolarDB- X instance per second. MULTI_DB_JOIN_COUNT: the number of multi-database JOIN queries that have been processed by the PolarDB-X instance since startup. ds

```
mysql> show stats; +------+---------+----------+-------------------+------------------+----------------------- -+--------------------+--------+------------+--------------+---------------+---------------
```

`-+`

```
| QPS  | RDS_QPS | SLOW_QPS | PHYSICAL_SLOW_QPS | ERROR_PER_SECOND | MERGE_QUERY_PER_SECOND
| ACTIVE_CONNECTIONS | RT(MS) | RDS_RT(MS) | NET_IN(KB/S) | NET_OUT(KB/S) | THREAD_RUNNING
```

|

```
+------+---------+----------+-------------------+------------------+----------------------- -+--------------------+--------+------------+--------------+---------------+---------------
```

`-+`

```
| 1.77 |    1.68 |     0.03 |              0.03 |             0.02 |                   0.00
|                  7 | 157.13 |      51.14 |       134.49 |          1.48 |              1
```

|

```
+------+---------+----------+-------------------+------------------+----------------------- -+--------------------+--------+------------+--------------+---------------+---------------
```

`-+`

```
1 row in set (0.01 sec) mysql> show full stats; +------+---------+----------+-------------------+------------------+----------------------+ ------------------------+--------------------+------------------------------+--------+----- -------+--------------+---------------+----------------+----------------------+------------ -----+----------------------------+-----------------------+------------------------------+- ------------------------+--------------------------+---------------------+-------+--------- +-------------+------------+
| QPS  | RDS_QPS | SLOW_QPS | PHYSICAL_SLOW_QPS | ERROR_PER_SECOND | VIOLATION_PER_SECOND |
MERGE_QUERY_PER_SECOND | ACTIVE_CONNECTIONS | CONNECTION_CREATE_PER_SECOND | RT(MS) | RDS_R T(MS) | NET_IN(KB/S) | NET_OUT(KB/S) | THREAD_RUNNING | HINT_USED_PER_SECOND | HINT_USED_CO UNT | AGGREGATE_QUERY_PER_SECOND | AGGREGATE_QUERY_COUNT | TEMP_TABLE_CREATE_PER_SECOND | T EMP_TABLE_CREATE_COUNT | MULTI_DB_JOIN_PER_SECOND | MULTI_DB_JOIN_COUNT | CPU | FREEMEM | FULLGCCOUNT | FULLGCTIME | +------+---------+----------+-------------------+------------------+----------------------+ ------------------------+--------------------+------------------------------+--------+----- -------+--------------+---------------+----------------+----------------------+------------ -----+----------------------------+-----------------------+------------------------------+- ------------------------+--------------------------+---------------------+-------+--------- +-------------+------------+
| 1.63 |    1.68 |     0.03 |              0.03 |             0.02 |                 0.00 |
0.00 | 6 | 0.01 | 157.13 | 51.14 | 134. 33 | 1.21 | 1 | 0.00 | 54 | 0.00 | 663 | 0.00 | 512 | 0.00 | 516 | 0.09% | 6.96% | 76446 | 21326906 | +------+---------+----------+-------------------+------------------+----------------------+ ------------------------+--------------------+------------------------------+--------+----- -------+--------------+---------------+----------------+----------------------+------------ -----+----------------------------+-----------------------+------------------------------+- ------------------------+--------------------------+---------------------+-------+--------- +-------------+------------+ 1 row in set (0.01 sec)
```

SHOW DB STATUS ds You can run this SQL statement to view the capacity and performance information of a physical database. All the returned values indicate the real-time information. The capacity information is obtained from the ApsaraDB RDS for MySQL system table, and therefore may be different from the actual capacity information. The following describes the meanings of important columns: NAME: the PolarDB-X 1.0 internal tag that represents a logical PolarDB-X 1.0 database corresponding to the database shard. The value is different from the name of the logical PolarDB-X 1.0 database. CONNECTION_STRING: the information about a connection from the PolarDB-X instance to the database shard. PHYSICAL_DB: the name of the database shard. The `TOTAL` row indicates the total amount of capacity of all the database shards corresponding to the logical PolarDB-X 1.0 database. SIZE_IN_MB: the size of the space occupied by the data in the database shard. Unit: MB. RATIO: the ratio of the data volume of the database shard to the total data volume of the current logical PolarDB-X 1.0 database. THREAD_RUNNING: the number of threads that are running in the ApsaraDB RDS for MySQL instance to which the physical database belongs. The meaning of this parameter is the same as that of the THREAD_RUNNING parameter returned by the MySQL `SHOW GLOBAL STATUS` command. For more information, see MySQL official documentation.

```
mysql> show db status; +------+---------------------------+--------------------+-------------------+------------+- -------+----------------+
| ID   | NAME                      | CONNECTION_STRING  | PHYSICAL_DB       | SIZE_IN_MB |
RATIO | THREAD_RUNNING | +------+---------------------------+--------------------+-------------------+------------+- -------+----------------+
|    1 | drds_db_1516187088365daui | 100.100.64.1:59077 | TOTAL             |  13.109375 |
100% | 3 |
|    2 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0000 |   1.578125 |
12.04% | |
|    3 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0001 |     1.4375 |
10.97% | |
|    4 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0002 |     1.4375 |
10.97% | |
|    5 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0003 |     1.4375 |
10.97% | |
|    6 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0004 |   1.734375 |
13.23% | |
|    7 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0005 |   1.734375 |
13.23% | |
|    8 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0006 |   2.015625 |
15.38% | |
|    9 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0007 |   1.734375 |
13.23% | | +------+---------------------------+--------------------+-------------------+------------+- -------+----------------+
```

SHOW FULL DB STATUS [LIKE {tablename}] ds You can run this SQL statement to view the capacity and performance information of a table shard in a physical database, which is also called a database shard. All the returned values indicate the real-time information. The capacity information is obtained from the ApsaraDB RDS for MySQL system table, and therefore may be different from the actual capacity information. The following describes the meanings of important columns: NAME: the PolarDB-X 1.0 internal tag that represents a logical PolarDB-X 1.0 database corresponding to the database shard. The value is different from the name of the logical PolarDB-X 1.0 database. CONNECTION_STRING: the information about a connection from the PolarDB-X instance to the database shard. PHYSICAL_DB: the name of the database shard. If the LIKE keyword is used for filtering in the statement, the TOTAL row indicates the total amount of capacity of the database shard. If the LIKE keyword is not used for filtering in the statement, the TOTAL row indicates the total amount of capacity of all database shards. PHYSICAL_TABLE: the name of the table shard in the database shard. If the LIKE keyword is used for filtering in the statement, the TOTAL row indicates the total amount of capacity of the table shard. If the LIKE keyword is not used for filtering in the statement, the TOTAL row indicates the total amount of capacity of all table shards in the database shard. SIZE_IN_MB: the size of the space occupied by the data in the database shard. Unit: MB. RATIO: the ratio of the data volume of the table shard to the total data volume of all the table shards obtained through filtering. THREAD_RUNNING: the number of threads that are running in the ApsaraDB RDS for MySQL instance to which the physical database belongs. The meaning of this parameter is the same as that of the THREAD_RUNNING parameter returned by the MySQL `SHOW GLOBAL STATUS` command. For more information, see MySQL official documentation.

```
mysql> show full db status like hash_tb; +------+---------------------------+--------------------+-------------------+-------------- --+------------+--------+----------------+
| ID   | NAME                      | CONNECTION_STRING  | PHYSICAL_DB       | PHYSICAL_TABL
E | SIZE_IN_MB | RATIO | THREAD_RUNNING | +------+---------------------------+--------------------+-------------------+-------------- --+------------+--------+----------------+
|    1 | drds_db_1516187088365daui | 100.100.64.1:59077 | TOTAL             |
|     19.875 | 100%   | 3              |
|    2 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0000 | TOTAL
|    3.03125 | 15.25% |                |
|    3 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0000 | hash_tb_00
|   1.515625 | 7.63%  |                |
|    4 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0000 | hash_tb_01
|   1.515625 | 7.63%  |                |
|    5 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0001 | TOTAL
|        2.0 | 10.06% |                |
|    6 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0001 | hash_tb_02
|   1.515625 | 7.63%  |                |
|    7 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0001 | hash_tb_03
|   0.484375 | 2.44%  |                |
|    8 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0002 | TOTAL
|    3.03125 | 15.25% |                |
|    9 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0002 | hash_tb_04
|   1.515625 | 7.63%  |                |
```

|

```
10|drdsdb1516187088365daui|100100641:59077|drdsdbxzip0002|hashtb05
```

ds

```
|   10 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0002 | hash_tb_05
|   1.515625 | 7.63%  |                |
|   11 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0003 | TOTAL
|   1.953125 | 9.83%  |                |
|   12 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0003 | hash_tb_06
|   1.515625 | 7.63%  |                |
|   13 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0003 | hash_tb_07
|     0.4375 | 2.2%   |                |
|   14 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0004 | TOTAL
|    3.03125 | 15.25% |                |
|   15 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0004 | hash_tb_08
|   1.515625 | 7.63%  |                |
|   16 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0004 | hash_tb_09
|   1.515625 | 7.63%  |                |
|   17 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0005 | TOTAL
|   1.921875 | 9.67%  |                |
|   18 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0005 | hash_tb_11
|   1.515625 | 7.63%  |                |
|   19 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0005 | hash_tb_10
|    0.40625 | 2.04%  |                |
|   20 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0006 | TOTAL
|    3.03125 | 15.25% |                |
|   21 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0006 | hash_tb_12
|   1.515625 | 7.63%  |                |
|   22 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0006 | hash_tb_13
|   1.515625 | 7.63%  |                |
|   23 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0007 | TOTAL
|      1.875 | 9.43%  |                |
|   24 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0007 | hash_tb_14
|   1.515625 | 7.63%  |                |
|   25 | drds_db_1516187088365daui | 100.100.64.1:59077 | drds_db_xzip_0007 | hash_tb_15
|   0.359375 | 1.81%  |                |
+------+---------------------------+--------------------+-------------------+-------------- --+------------+--------+----------------+
```

### 7.6 SHOW PROCESSLIST and KILL commands

commands

> Not e
> If the version of PolarDB-X 1.0 is 5.1.28-1408022 or later, PolarDB-X 1.0 support the SHOW PROCESSLIST and KILL commands for both logical and physical connections. For more information, see this topic.

If the version of PolarDB-X 1.0 is earlier than 5.1.28-1408022, PolarDB-X 1.0 support the SHOW PROCESSLIST and KILL commands only for physical connections. For more information, see SHOW PROCESSLIST and KILL commands in earlier versions. SHOW PROCESSLIST command ds In a PolarDB-X 1.0 instance, you can run the `SHOW PROCESSLIST` command to view information such as connections to the PolarDB-X 1.0 instance and SQL statements that are being executed in the PolarDB- X instance. Syntax

```
SHOW [FULL] PROCESSLIST
```

Examples

```
mysql> SHOW PROCESSLIST\G
     ID: 1971050
   USER: admin
   HOST: 111.111.111.111:4303
     DB: drds_test
COMMAND: Query
   TIME: 0
  STATE:
   INFO: show processlist
1 row in set (0.01 sec)
```

The following describes the meanings of the fields in the result set: ID: the ID of the connection. The value is a long-type number. USER: the name of the user who sets up the connection. HOST: the IP address and port number of the host that sets up the connection. DB: the name of the database accessed by the connection. COMMAND: the usage state of the connection. Currently, this field can be set to the following values: Query: the current connection is executing an SQL statement. Sleep: the current connection is idle. TIME: the duration when the connection is in the current state: When the value of COMMAND is Query, this field indicates how long the SQL statement has been being executed on the connection. When the value of COMMAND is Sleep, this field indicates how long the connection has been in the idle state. STATE: currently, no meaning has been assigned for this field. The value is constantly empty. INFO: When the value of COMMAND is Query, this field indicates the content of the SQL statement that is being executed on the connection. If the FULL parameter is not specified, a maximum of the first 30 characters of the SQL statement are returned. If the FULL parameter is specified, a maximum of the first 1000 characters of the SQL statement are returned. When the value of COMMAND is other values, this field is meaningless and left empty. SHOW PHYSICAL_PROCESSLIST command In a PolarDB-X 1.0 instance, you can run the SHOW PHYSICAL_PROCESSLIST command to view information about all the SQL statements that are being executed on underlying ApsaraDB RDS for MySQL instances. ds Syntax

```
SHOW [FULL] PHYSICAL_PROCESSLIST
```

When an SQL statement is excessively long, the responses of the `SHOW PHYSICAL_PROCESSLIST` command may be truncated. In this case, you can run the `SHOW FULL PHYSICAL_PROCESSLIST` command to obtain the complete SQL statement. The meaning of each column in the responses is equivalent to that in the responses of the `SHOW` `PROCESSLIST` command. For more information, see SHOW PROCESSLIST Syntax.

> Not e Different from ApsaraDB RDS for MySQL, the PolarDB-X 1.0 instance returns a string instead of a number in the ID column of a physical connection.

```
mysql> SHOW PHYSICAL_PROCESSLIST\G
*************************** 1. row ***************************
           ID: 0-0-521414
         USER: tddl5
           DB: tddl5_00
      COMMAND: Query
         TIME: 0
        STATE: init
         INFO: show processlist
*************************** 2. row ***************************
           ID: 0-0-521570
         USER: tddl5
           DB: tddl5_00
      COMMAND: Query
         TIME: 0
        STATE: User sleep
         INFO: /*DRDS /88.88.88.88/b67a0e4d8800000/ */ select sleep(1000)
2 rows in set (0.01 sec)
```

KILL command The KILL command is used to terminate an SQL statement that is being executed. The PolarDB-X 1.0 instance connects to an ApsaraDB RDS for MySQL instance by using the username created by the PolarDB-X 1.0 instance on the ApsaraDB RDS for MySQL instance. Therefore, if you directly connect to the ApsaraDB RDS for MySQL instance, you do not have the permission to run the KILL command on a request initiated by the PolarDB-X 1.0 instance. To terminate an SQL statement that is being executed on the PolarDB-X 1.0 instance, you must use tools such as the MySQL command line and to connect to the PolarDB-X 1.0 instance, and then run the KILL command on the PolarDB-X 1.0 instance. Syntax

```
KILL PROCESS_ID | 'PHYSICAL_PROCESS_ID' | 'ALL'
```

The KILL command can be used in the following ways: Run `KILL PROCESS_ID` to terminate a specified logical SQL statement. ds The PROCESS_ID parameter is obtained from the ID column in the responses of the `SHOW [FULL] PRO` `CESSLIST` command. Running the `KILL PROCESS_ID` command in the PolarDB-X 1.0 instance will terminate both logical and physical SQL statements that are being executed on this connection, and disconnect this connection. The PolarDB-X 1.0 instance does not support the `KILL QUERY` command. Run `KILL 'PHYSICAL_PROCESS_ID'` to terminate a specified physical SQL statement. The PHYSICAL_PROCESS_ID parameter is obtained from the ID column in the responses of the `SHOW P` `HYSICAL_PROCESS_ID` command.

> Not e The PHYSICAL_PROCESS_ID column is a string instead of a number. Therefore, the PHYSICAL_PROCESS_ID parameter must be enclosed in single quotation marks (') in the KILL command.

Examples:

```
 mysql> KILL '0-0-521570';
 Query OK, 0 rows affected (0.01 sec)
```

Run `KILL 'ALL'` to terminate all the physical SQL statements that are executed by the PolarDB-X 1.0 instance in the current logical database. When the underlying ApsaraDB RDS for MySQL instance is overloaded due to some SQL statements, you can use the `KILL 'ALL'` command to terminate all the physical SQL statements that are being executed in the current logical PolarDB-X 1.0 database. All physical SQL statements indicated by PROCESS that meet the following conditions can be terminated by running `KILL 'ALL'` : The value of the User parameter for the physical SQL statement indicated by PROCESS is a username created by the PolarDB-X 1.0 instance in the ApsaraDB RDS for MySQL instance. The physical SQL statement indicated by PROCESS is executing a query. In other words, the value of COMMAND is Query.

### 7.7 SHOW PROCESSLIST and KILL commands in earlier versions

commands in earlier versions

> Not e
> If the version of PolarDB-X 1.0 is 5.1.28-1408022 or later, PolarDB-X 1.0 support the SHOW PROCESSLIST and KILL commands for both logical and physical connections. For more information, see SHOW PROCESSLIST and KILL commands.
> If the version of PolarDB-X 1.0 is earlier than 5.1.28-1408022, PolarDB-X 1.0 only supports the SHOW PROCESSLIST and KILL commands for physical connections. For more information, see this topic.

SHOW PROCESSLIST command ds In a PolarDB-X 1.0 instance, you can run the `SHOW PROCESSLIST` command to view information about all the SQL statements that are being executed on the ApsaraDB RDS for MySQL instances. Syntax

```
SHOW [FULL] PROCESSLIST
```

| , the responses of the | SHOW PROCESSLIST |   |
|---|---|---|
| SHOW FULL PROCESSLIST |   | command to obt |

SQL statement. The meaning of each column in the responses is equivalent to that in the responses of the `SHOW` `PROCESSLIST` statement. For more information, see SHOW PROCESSLIST Syntax.

```
mysql> SHOW PROCESSLIST\G
*************************** 1. row ***************************
           ID: 0-0-521414
         USER: tddl5
           DB: tddl5_00
      COMMAND: Query
         TIME: 0
        STATE: init
         INFO: show processlist
    ROWS_SENT: NULL
ROWS_EXAMINED: NULL
    ROWS_READ: NULL
*************************** 2. row ***************************
           ID: 0-0-521570
         USER: tddl5
           DB: tddl5_00
      COMMAND: Query
         TIME: 0
        STATE: User sleep
         INFO: /*DRDS /88.88.88.88/b67a0e4d8800000/ */ select sleep(1000)
    ROWS_SENT: NULL
ROWS_EXAMINED: NULL
    ROWS_READ: NULL
2 rows in set (0.01 sec)
```

KILL You can execute the KILL statement to terminate an SQL statement that is being executed. The PolarDB-X 1.0 instance connects to an ApsaraDB RDS for MySQL instance by using the username created by the PolarDB-X 1.0 instance on the ApsaraDB RDS for MySQL instance. Therefore, if you directly connect to the ApsaraDB RDS for MySQL instance, you are not authorized to execute the KILL statement to terminate a request initiated by the PolarDB-X 1.0 instance. To terminate an SQL statement that is being executed on the PolarDB-X 1.0 instance, you must use tools to connect to the PolarDB-X 1.0 instance. You can use tools such as the MySQL command line and . Then, execute the KILL statement on the PolarDB-X 1.0 instance. Syntax ds

```
KILL 'PROCESS_ID' | 'ALL'
```

The KILL command can be used in the following ways: Run `KILL 'PROCESS_ID'` to terminate a specified SQL statement. The PROCESS_ID parameter is obtained from the ID column in the responses of the `SHOW PROCESSLIS` `T` command.

> Not e Different from ApsaraDB RDS for MySQL, the PolarDB-X 1.0 instance returns a string instead of a number in the ID column. Therefore, the PROCESS_ID parameter must be enclosed in single quotation marks (') in the KILL command.

Examples

```
 mysql> KILL '0-0-521570';
 Query OK, 0 rows affected (0.01 sec)
```

Run `KILL 'ALL'` to terminate all the SQL statements executed by the PolarDB-X 1.0 instance in the current logical database. When the underlying ApsaraDB RDS for MySQL instance is overloaded due to several SQL statements, you can use the `KILL 'ALL'` command to terminate all the SQL statements that are being executed in the current logical PolarDB-X 1.0 database. All SQL statements indicated by PROCESS that meet the following conditions can be terminated by running `KILL 'ALL'` : The value of the User parameter for the physical SQL statement indicated by PROCESS is a username created by the PolarDB-X 1.0 instance in the ApsaraDB RDS for MySQL instance. The physical SQL statement indicated by PROCESS is executing a query, which means that the value of COMMAND is Query. PolarDB-X 1.0 instances in earlier versions do not support the `KILL 'ALL'` command. An error will be reported if this command is being executed in these instances. To resolve this problem, you can upgrade the version of the PolarDB-X 1.0 instance.

## 8 Custom hints

Not e This topic is applicable to PolarDB-X 1.0 5.3 and later. For earlier versions, see PolarDB-X 5.2 hints.

### 8.1 Introduction to hints

As a supplement to the SQL syntax, hints play a critical role in relational databases. They allow you to influence execution plans of SQL statements by using relevant syntax, to specially optimize the SQL statements. PolarDB-X 1.0 also provides special hint syntax. For example, if you know the target data is stored in table shards in certain database shards and you need to route the SQL statement directly to the database shards for execution, you can use custom hints provided by PolarDB-X 1.0.

```
SELECT /*+TDDL:node('node_name')*/ * FROM table_name;
```

In the preceding SQL statement, the part between `/*` and `*/` , namely, `+TDDL:node('node_name')` , is a PolarDB-X 1.0 hint. The hint specifies the ApsaraDB RDS for MySQL database shard where the SQL statement is to be executed.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, if you need to run an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ , add the -c parameter to _ the logon command, because PolarDB-X 1.0 hints are based on the MySQL Comment Syntax. Otherwise, the client deletes the PolarDB-X 1.0 hint and then sends the SQL statement to the server for execution, which causes the hint to fail to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

PolarDB-X hint syntax Basic syntax

```
 /*+TDDL: hint_command [hint_command ...] */
 /! +TDDL: hint_command [hint_command ...] */
```

PolarDB-X 1.0 hints are based on the MySQL Comment Syntax. The hint statements are located between `/*` and `*/` or between /! and `*/` , and must begin with `+TDDL:` . The `hint_command` parameter indicates a PolarDB-X 1.0 hint command related to the specific operation. Multiple `hint_command` parameters are separated by spaces. Examples

```bash
# Query the names of physical tables in each database shard.
/*+TDDL:scan()*/SHOW TABLES;
# Route the query to database shard 0000 of a read-only ApsaraDB RDS for MySQL instance.
/*+TDDL:node(0) slave()*/SELECT * FROM t1;
```

| ple, | /*+TDDL:scan()*/ |   |   |
|---|---|---|---|
| +TDDL: |   | . The | scan() |

| and | /*+TDDL:node(0) slave()*/ |   |   |   |
|---|---|---|---|---|
| node(0) |   | , and | slave() | functi |

commands. Hint commands are separated by spaces. Use one hint in an SQL statement: PolarDB-X 1.0 allows you to use hints in data manipulation language (DML), data definition language (DDL), and data access language (DAL) statements. The following describes the syntax in detail. For all statements that support hints, you can specify a hint at the beginning of the statements, for example:

```
/*+TDDL: ... */ SELECT ... /*+TDDL: ... */ INSERT ... /*+TDDL: ... */ REPLACE ... /*+TDDL: ... */ UPDATE ... /*+TDDL: ... */ DELETE ... /*+TDDL: ... */ CREATE TABLE ... /*+TDDL: ... */ ALTER TABLE ... /*+TDDL: ... */ DROP TABLE ... /*+TDDL: ... */ SHOW ... ...
```

For DML statements, you can specify a hint behind the first keyword of the statements, for example:

```
SELECT /*+TDDL: ... */ ... INSERT /*+TDDL: ... */ ... REPLACE /*+TDDL: ... */ ... UPDATE /*+TDDL: ... */ ... DELETE /*+TDDL: ... */ ... ...
```

> Not e Different hints may be applicable to different syntaxes. For more information about the applicable syntaxes, see the documentation of hint commands.

Use multiple hint commands in an SQL statement: PolarDB-X 1.0 allows you to use multiple hint commands in SQL statements that contain hints.

```
SELECT /*+TDDL:node(0) slave()*/ ... ;
```

PolarDB-X 1.0 has the following limitations on the use of multiple hint commands:

```bash
# A single SQL statement cannot contain multiple hint statements.
SELECT /*+TDDL:node(0)*/ /*+TDDL:slave()*/ ... ;
# An SQL statement that contains a hint cannot contain duplicate hint commands.
SELECT /*+TDDL:node(0) node(1)*/ ... ;
```

PolarDB-X hint classification PolarDB-X 1.0 hints are classified into the following major categories according to operation types:

### 8.2 Read/write splitting

PolarDB-X 1.0 provides transparent read/write splitting at the application layer. Data synchronization between primary and read-only ApsaraDB RDS for MySQL instances has a delay of several milliseconds. If you need to read changed data immediately after the primary ApsaraDB RDS for MySQL instance is changed, you must ensure that the SQL statement for reading data is routed to the primary ApsaraDB RDS for MySQL instance. To meet this demand, PolarDB-X 1.0 provides custom hints for read/write splitting, to route SQL statements to a specified primary or read-only ApsaraDB RDS for MySQL instance. Not e This topic is applicable to PolarDB-X 1.0 5.3 and later. For earlier versions, see Read/write splitting. Syntax

```
/*+TDDL:
    master()
    | slave()
```

`*/` With this custom hint, you can specify whether to run an SQL statement on a primary or read-only ApsaraDB RDS for MySQL instance. With the custom hint `/*+TDDL:slave()*/` , if a primary ApsaraDB RDS for MySQL instance is configured with multiple read-only ApsaraDB RDS for MySQL instances, the PolarDB-X 1.0 instance randomly selects a read-only ApsaraDB RDS for MySQL instance based on its weight, to run the SQL statement.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples Specify a primary ApsaraDB RDS for MySQL instance to run an SQL statement:

```
SELECT /*+TDDL:master()*/ * FROM table_name;
```

After the custom hint `/*+TDDL:master()*/` is added behind the first keyword in the SQL statement, this SQL statement is routed to the primary ApsaraDB RDS for MySQL instance for execution. Specify a read-only ApsaraDB RDS for MySQL instance to run an SQL statement:

```
SELECT /*+TDDL:slave()*/ * FROM table_name;
```

After the custom hint `/*+TDDL:slave()*/` is added behind the first keyword in the SQL statement, this SQL statement is randomly routed to a read-only ApsaraDB RDS for MySQL instance based on the allocated weight. Note The custom hints for read-write splitting are only applicable to read SQL statements for nontransactional data. SQL statements for transactional data and write SQL statements are still routed to the primary ApsaraDB RDS for MySQL instance for execution. The PolarDB-X 1.0 hint `/*+TDDL:slave()*/` allows you to route the SQL statement randomly to a read-only ApsaraDB RDS for MySQL instance based on the configured weight for execution. If no read-only ApsaraDB RDS for MySQL instance is available, no error is reported. Instead, the primary ApsaraDB RDS for MySQL instance is selected to run the SQL statement.

### 8.3 Specify a timeout period for an SQL statement

SQL statement In PolarDB-X 1.0, the SQL statements for PolarDB-X 1.0 instances and ApsaraDB RDS for MySQL instances are timed out after 900 seconds (which can be adjusted) by default. However, for some slow SQL statements, the execution duration may exceed 900 seconds. For these slow SQL statements, PolarDB- X 1.0 provides a custom hint to adjust their timeout periods. You can use this custom hint to adjust the SQL execution duration as needed. Not e This topic is applicable to PolarDB-X 1.0 5.3 and later. For earlier versions, see Specify a timeout period for an SQL statement. Syntax The syntax of the PolarDB-X 1.0 hint for specifying a timeout period for an SQL statement is as follows:

```
/*+TDDL:SOCKET_TIMEOUT(time)*/
```

The `SOCKET_TIMEOUT` parameter is measured in milliseconds. With this custom hint, you can adjust the timeout period for the SQL statement based on business requirements.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples Set the timeout period of an SQL statement to 40 seconds:

```
/*+TDDL:SOCKET_TIMEOUT(40000)*/SELECT * FROM t_item;
```

> Not e A longer timeout period causes database resources to be occupied for a longer period of time. If excessive SQL statements are executed over a long time within the same period, a large number of database resources may be consumed. This will make users unable to use PolarDB-X properly. In this case, we need to use this custom hint to optimize the SQL statements that take a long time to execute.

### 8.4 Specify a database shard to run an SQL statement

an SQL statement When running SQL commands in a PolarDB-X 1.0 instance, you may find that some SQL statements are not supported by the PolarDB-X 1.0 instance. In this case, you can use the `NODE HINT` provided by PolarDB-X 1.0, to route the SQL statements to one or more database shards for execution. In addition, if you need to query the data in a specified database shard or the data in a specified table shard in a known database shard, you can use the `NODE HINT` to directly route the SQL statement to the database shard for execution. Not e This topic is applicable to PolarDB-X 1.0 5.3 and later. For earlier versions, see Specify a database shard to run an SQL statement. Syntax The `NODE HINT` allows you to specify a database shard by using a shard name, to run the SQL statement in the database shard. A shard name uniquely identifies a database shard in a PolarDB-X 1.0 instance. You can run the SHOW NODE statement to obtain the shard name. Specify a database shard by using a shard name, to run an SQL statement This custom hint allows you to specify one or more database shards to run an SQL statement.

> Not e If the hint for specifying a database shard is used in an INSERT statement that contains a sequence for the target table, the sequence will not take effect. For more information, see Limits and precautions for sequences.

Specify one database shard to run an SQL statement:

```
/*+TDDL:node('node_name')*/
```

Specifically, `node_name` indicates the shard name. This PolarDB-X 1.0 hint enables you to route the SQL statement to the database shard specified by `node_name` . Specify multiple database shards to run an SQL statement:

```
/*+TDDL:node('node_name'[,'node_name1','node_name2'])*/
```

You can specify multiple shard names in the parameters and route the SQL statement to multiple database shards for execution. Separate multiple shard names with commas (,).

|   | Not e When this custom hint is used, the PolarDB-X 1.0 instance directly routes the SQL statement to the specified database shards for execution. Therefore, the specified shard names in the SQL statement must correspond to existing database shards. The NODE HINT can be used in data manipulation language (DML), data definition language (DDL), and data access language (DAL) statements. PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples The following shows the responses of the SHOW NODE statement for a logical database named `drds_test` in a PolarDB-X 1.0 instance.

```
mysql> SHOW NODE\G
*************************** 1. row ******************
                 ID: 0
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS
  MASTER_READ_COUNT: 212
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 2. row ******************
                 ID: 1
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0001_RDS
  MASTER_READ_COUNT: 29
   SLAVEREADCOUNT: 0
```

`S` `_`

```
_COU
```

`:``0`

```
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 3. row ******************
                 ID: 2
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0002_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 4. row ******************
                 ID: 3
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0003_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 5. row ******************
                 ID: 4
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0004_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 6. row ******************
                 ID: 5
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0005_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 7. row ******************
                 ID: 6
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0006_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 8. row ******************
                 ID: 7
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0007_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
8 rows in set (0.02 sec)
```

As you can see, each database shard has the `NAME` attribute, which indicates the shard name corresponding to the database shard. Each shard name uniquely corresponds to one database shard name. For example, the shard name `DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0003_RDS` corresponds to the database shard name `drds_test_vtla_0003` . Therefore, after obtaining the shard name, you can use the PolarDB-X 1.0 hint to specify the corresponding database shard to run the SQL statement. Specify database shard 0 to run an SQL statement:

```
SELECT /*TDDL:node('DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS')*/ * FROM table_n ame;
```

Specify multiple database shards to run an SQL statement:

```
SELECT /*TDDL:node('DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS','DRDS_TEST_147347 1355140LRPRDRDS_TEST_VTLA_0006_RDS')*/ * FROM table_name;
```

This SQL statement will be executed in the database shards whose shard names are `DRDS_TEST_1473`

```
471355140LRPRDRDS_TEST_VTLA_0000_RDS and DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0006_R
```

`DS` . View the execution plan of an SQL statement in database shard 0:

```
/*TDDL:node('DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS')*/ EXPLAIN SELECT * FROM table_name;
```

### 8.5 Scan all or some of database shards and table shards

shards and table shards In addition to routing an SQL statement to one or more database shards for execution, PolarDB-X 1.0 provides the `SCAN HINT` to scan all or some of database shards and table shards. With the `SCAN` `HINT` , you can route an SQL statement to each database shard at a time. For example, you can view all the table shards in a specified database shard or view the data volume of each physical table of a specified logical table. Not e This topic is applicable to PolarDB-X 1.0 5.3 and later. For earlier versions, see Scan all database shards and table shards. With the SCAN HINT, you can specify the following SQL execution manners: Run an SQL statement in all table shards in all database shards. Run an SQL statement in all table shards in a specified database shard. Run an SQL statement in the specified table shard in the specified database shard by calculating the name of the physical table based on conditions. Run an SQL statement in the specified table shard in the specified database shard by explicitly specifying the name of the physical table. The `SCAN HINT` can be used in data manipulation language (DML) statements, data definition language (DDL) statements, and some data access language (DAL) statements.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Syntax

```bash
# SCAN HINT
# Route an SQL statement to all table shards in all database shards.
SCAN()
# Route an SQL statement to all table shards in a specified database shard.
SCAN(NODE="node_list") # Specify the database shard.
# Route an SQL statement to the specified table shard in the specified database shard by ca
lculating the name of the physical table based on conditions. SCAN(
  [TABLE=]"table_name_list"          # Specify the name of the logical table.
  , CONDITION="condition_string"     # Calculate the names of physical databases based on t
he content of TABLE and CONDITION.
  [, NODE="node_list"] )             # Filter the results obtained based on the content of
CONDITION, to retain only the results of the specified physical database.
# Route an SQL statement to the specified table shard in the specified database shard by ex
plicitly specifying the name of the physical table. SCAN(
  [TABLE=]"table_name_list"          # Specify the name of the logical table.
  , REAL_TABLE=("table_name_list")   # Specify the name of the physical table. The same phy
sical table names are applied to all physical databases.
  [, NODE="node_list"] )             # Filter the results obtained based on the content of
CONDITION, to retain only the results of the specified physical database.
# Specify physical table names or logical table names.
table_name_list:
    table_name [, table_name]...
# Specify physical databases by using GROUP_KEY and GROUP_INDEX, which can be obtained by r
unning the SHOW NODE statement. node_list:
    {group_key | group_index} [, {group_key | group_index}]...
# Run an SQL WHERE statement. When using this syntax, you must specify conditions for each
table, for example, t1.id = 2 and t2.id = 2. condition_string:
    where_condition
```

Examples Run the following SQL statement in all table shards in all database shards:

```
SELECT /*+TDDL:scan()*/ COUNT(1) FROM t1
```

After this statement is executed, the SQL statement is routed to all the physical tables corresponding to the logical table `t1` , and the result sets are merged and returned. Run the following SQL statement in all table shards in specified database shards:

```
SELECT /*+TDDL:scan(node='0,1,2')*/ COUNT(1) FROM t1
```

After this statement is executed, all physical tables corresponding to the logical table `t1` in database shards 0000, 0001, and 0002 are calculated, the SQL statement is routed to the physical tables, and the result sets are merged and returned. Run the following SQL statement in specified table shards based on conditions:

```
SELECT /*+TDDL:scan('t1', condition='t1.id = 2')*/ COUNT(1) FROM t1
```

After this statement is executed, all physical tables that correspond to the logical table `t1` and meet the conditions are calculated, the SQL statement is routed to the physical tables, and the result sets are merged and returned. Run the following SQL JOIN statement in the specified table shards based on conditions:

```
SELECT /*+TDDL:scan('t1, t2', condition='t1.id = 2 and t2.id = 2')*/ * FROM t1 a JOIN t2 b ON a.id = b.id WHERE b.name = "test"
```

After this statement is executed, all physical tables that correspond to the logical tables `t1` and `t2` and meet the conditions are calculated, the SQL statement is routed to the physical tables, and the result sets are merged and returned.

> Not ice Before using this custom hint, you must ensure that the logical tables t1 and t2 are partitioned into the same number of database shards and the same number of table shards. Otherwise, the database shards calculated by the PolarDB-X 1.0 instance based on the conditions are different, and an error will be returned.

Run the following SQL statement in the specified table shards in database shards by explicitly specifying the names of the physical tables:

```
SELECT /*+TDDL:scan('t1', real_table=("t1_00", "t1_01"))*/ COUNT(1) FROM t1
```

After this statement is executed, the SQL statement is routed to the table shards t1_00``t1_01 in all database shards, and the result sets are merged and returned. Run the following SQL JOIN statement in the specified table shards in database shards by explicitly specifying the names of the physical tables:

```
SELECT /*+TDDL:scan('t1, t2', real_table=("t1_00,t2_00", "t1_01,t2_01"))*/ * FROM t1 a JO IN t2 b ON a.id = b.id WHERE b.name = "test";
```

After this statement is executed, the SQL statement is routed to the table shards `t1_00` , `t2_00` , `t1_01` , and `t2_01` in all database shards, and the result sets are merged and returned.

### 8.6 INDEX HINT

PolarDB-X 1.0 supports global secondary indexes. The INDEX hint allows you to obtain query results from a specified GSI. The INDEX hint takes effect only for SQL SELECT statements.

> Not e This custom hint is applicable to only MySQL 5.7 and later and PolarDB-X 1.0 5.4.1 and later.

Syntax

```bash
# FORCE INDEX
tbl_name [[AS] alias] [index_hint] index_hint:
    FORCE INDEX({index_name})
# INDEX()
/*+TDDL:
    INDEX({table_name | table_alias}, {index_name})
```

`*/` PolarDB-X 1.0 INDEX hint can be used in two ways:

| FORCE INDEX() |   |
|---|---|
| INDEX() | : In thi |

`FORCE INDEX()` : This syntax is the same as that of MySQL FORCE INDEX. `INDEX()` : In this syntax, a global secondary index is specified using a table name (or alias) and an index name. This hint does not take effect in the following cases: The query does not contain the specified table name or alias. The specified global secondary index is not in the specified table.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples

```
CREATE TABLE t_order (
 `id` bigint(11) NOT NULL AUTO_INCREMENT,
 `order_id` varchar(20) DEFAULT NULL,
 `buyer_id` varchar(20) DEFAULT NULL,
 `seller_id` varchar(20) DEFAULT NULL,
 `order_snapshot` longtext DEFAULT NULL,
 `order_detail` longtext DEFAULT NULL,
 PRIMARY KEY (`id`),
 GLOBAL INDEX `g_i_seller`(`seller_id`) dbpartition by hash(`seller_id`),
 UNIQUE GLOBAL INDEX `g_i_buyer` (`buyer_id`) COVERING(`seller_id`, `order_snapshot`)
  dbpartition by hash(`buyer_id`) tbpartition by hash(`buyer_id`) tbpartitions 3
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by hash(`order_id`);
```

Specify the global secondary index `g_i_seller` by using FORCE INDEX in the FROM clause:

```
 SELECT a.*, b.order_id
   FROM t_seller a
     JOIN t_order b FORCE INDEX(g_i_seller) ON a.seller_id = b.seller_id
   WHERE a.seller_nick="abc";
```

Specify the global secondary index `g_i_buyer` by using INDEX+table alias:

```
/*+TDDL:index(a, g_i_buyer)*/ SELECT * FROM t_order a WHERE a.buyer_id = 123
```

## 9 PolarDB-X 5.2 hints

### 9.1 Introduction to hints

As a supplement to the SQL syntax, hints play a critical role in relational databases. They allow you to affect execution plans of SQL statements by using relevant syntax, to specially optimize the SQL statements. Overview of PolarDB-X hints PolarDB-X 1.0 provides special hint syntax. For example, if you know the target data is stored in table shards in certain database shards and you need to route the SQL statement directly to the database shards for execution, you can use custom hints provided by PolarDB-X 1.0.

```
/! TDDL:NODE IN('node_name', ...) */SELECT * FROM table_name;
```

In the preceding SQL statement, the part between /! and `*/` , namely, `TDDL:node` `in('node_name', ...)` , is a PolarDB-X 1.0 hint. The hint specifies the ApsaraDB RDS for MySQL database shard where the SQL statement is to be executed.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

PolarDB-X hint syntax Basic syntax:

```
/! TDDL:hint command*/
```

PolarDB-X 1.0 hints are based on MySQL Comment Syntax. Therefore, an SQL statement that contains a PolarDB-X 1.0 hint is located between /! and `*/` , and must begin with `TDDL:` . The `hint` `command` indicates a PolarDB-X 1.0 hint command related to the specific operation. For example, a PolarDB-X 1.0 hint is added to the following SQL statement to display the name of each database shard.

```
/! TDDL:SCAN*/SHOW TABLES;
```

In this SQL statement, /! TDDL:SCAN*/ is the PolarDB-X 1.0 hint that begins with `TDDL:` , and `SCAN` is a PolarDB-X 1.0 hint command.

### 9.2 Read/write splitting

PolarDB-X 1.0 provides transparent read/write splitting at the application layer. Data synchronization between primary and read-only ApsaraDB RDS for MySQL instances has a delay of several milliseconds. If you need to read changed data immediately after the primary ApsaraDB RDS for MySQL instance is changed, you must ensure that the SQL statement for reading data is routed to the primary ApsaraDB RDS for MySQL instance. To meet this demand, PolarDB-X 1.0 provides custom hints for read/write splitting, to route SQL statements to a specified primary or read-only ApsaraDB RDS for MySQL instance. Syntax

```
/! TDDL:MASTER|SLAVE*/
```

With this custom hint, you can specify whether to run an SQL statement on a primary or read-only ApsaraDB RDS for MySQL instance. With the custom hint /!TDDL:SLAVE*/ , if a primary ApsaraDB RDS for MySQL instance is configured with multiple read-only ApsaraDB RDS for MySQL instances, the PolarDB-X 1.0 instance randomly selects a read-only ApsaraDB RDS for MySQL instance based on its weight, to run the SQL statement.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples Specify a primary ApsaraDB RDS for MySQL instance to run an SQL statement:

```
/! TDDL:MASTER*/SELECT * FROM table_name;
```

After the custom hint /! TDDL:MASTER*/ is added at the beginning of the SQL statement, this SQL statement is routed to the primary ApsaraDB RDS for MySQL instance for execution. Specify a read-only ApsaraDB RDS for MySQL instance to run an SQL statement:

```
/! TDDL:SLAVE*/SELECT * FROM table_name;
```

After the custom hint /! TDDL:SLAVE*/ is added at the beginning of the SQL statement, this SQL statement is randomly routed to a read-only ApsaraDB RDS for MySQL instance based on the allocated weight. Considerations The custom hints for read/write splitting are only applicable to read SQL statements for nontransactional data. SQL statements for transactional data and write SQL statements are still routed to the primary ApsaraDB RDS for MySQL instance. When you use the `/*+TDDL:slave()*/` hint, the PolarDB-X 1.0 instance routes the SQL statement randomly to a read-only ApsaraDB RDS for MySQL instance based on the allocated weight. If no readonly ApsaraDB RDS for MySQL instance is available, no error is reported. Instead, the primary ApsaraDB RDS for MySQL instance is selected to execute the SQL statement.

### 9.3 Prevent the delay from a read-only ApsaraDB RDS for MySQL instance

only ApsaraDB RDS for MySQL instance Normally, if you have configured a read-only ApsaraDB for RDS instance for the primary ApsaraDB RDS for MySQL instance of a logical database in a PolarDB-X 1.0 instance and set read traffic for both the primary and read-only ApsaraDB RDS for MySQL instances, PolarDB-X 1.0 routes SQL statements to the primary and read-only ApsaraDB RDS for MySQL instances based on the read/write ratio. However, if asynchronous data replication between the primary and read-only ApsaraDB RDS for MySQL instances has a high delay, an error is reported or error results are returned when PolarDB-X routes the SQL statements to the read-only ApsaraDB RDS for MySQL instance. To address this issue, the PolarDB-X instance provides a custom hint to cut off the delay of the readonly instance. Specifically, based on the maximum delay of primary/secondary replication, PolarDB-X determines whether to route the SQL statement to the primary or the read-only ApsaraDB RDS for MySQL instance. Syntax

```
/! TDDL:SQL_DELAY_CUTOFF=time*/
```

With this custom hint, you can specify the value of `SQL_DELAY_CUTOFF` . When the value of SQL_DELAY (primary/secondary replication delay of ApsaraDB RDS for MySQL) for the read-only ApsaraDB RDS for MySQL instance reaches or exceeds the value of `time` (which is measured in seconds), the SQL statement is routed to the primary ApsaraDB RDS for MySQL instance.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples Set the primary/secondary replication delay to 5 seconds:

```
/! TDDL:SQL_DELAY_CUTOFF=5*/SELECT * FROM table_name;
```

In this SQL statement, the value of `SQL_DELAY_CUTOFF` is set to 5. Therefore, when the value of `SQ` `L_DELAY` for the read-only ApsaraDB RDS for MySQL instance reaches or exceeds 5 seconds, the SQL statement is routed to the primary ApsaraDB RDS for MySQL instance. Use the custom hint for delay cutoff with other custom hints:

```
/! TDDL:SLAVE AND SQL_DELAY_CUTOFF=5*/SELECT * FROM table_name;
```

The custom hint for cutting off the delay of the read-only ApsaraDB RDS for MySQL instance can be used with other hints. By default, the SQL query request is routed to a read-only ApsaraDB RDS for MySQL instance. However, when the primary/secondary replication delay reaches or exceeds 5 seconds, the SQL query request is routed to the primary ApsaraDB RDS for MySQL instance.

### 9.4 Specify a timeout period for an SQL statement

SQL statement In PolarDB-X 1.0, the SQL statements for PolarDB-X 1.0 instances and ApsaraDB RDS for MySQL instances are timed out after 900 seconds (which can be adjusted) by default. However, for some slow SQL statements, the execution duration may exceed 900 seconds. For these slow SQL statements, PolarDB- X 1.0 provides a custom hint to adjust their timeout periods. You can use this custom hint to adjust the SQL execution duration as needed. Syntax The syntax of the PolarDB-X 1.0 hint for specifying a timeout period for an SQL statement is as follows:

```
/! TDDL:SOCKET_TIMEOUT=time*/
```

The `SOCKET_TIMEOUT` parameter is measured in milliseconds. With this custom hint, you can adjust the timeout period for the SQL statement based on business requirements.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples Set the timeout period of an SQL statement to 40 seconds:

```
/! TDDL:SOCKET_TIMEOUT=40000*/SELECT * FROM t_item;
```

> Not e A longer timeout period causes database resources to be occupied for a longer period of time. If excessive SQL statements are executed over a long time within the same period, a large number of database resources may be consumed. This will make users unable to use PolarDB-X properly. In this case, we need to use this custom hint to optimize the SQL statements that take a long time to execute.

### 9.5 Specify a database shard to run an SQL statement

an SQL statement When running SQL commands in a PolarDB-X 1.0 instance, you may find that some SQL statements are not supported by the PolarDB-X 1.0 instance. In this case, you can use the custom hint provided by PolarDB-X 1.0 to route the SQL statements to one or more database shards for execution. In addition, if you need to query the data in a specified database shard or the data in a specified table shard, you can use the custom hint to directly route the SQL statement to the database shard for execution. Syntax This custom hint allows you to specify a database shard by using a shard name or the value of the database shard key, to run an SQL statement in the database shard. A shard name uniquely identifies a database shard in a PolarDB-X 1.0 instance. You can run the `SHOW NODE` command to obtain the shard name.

> Not e If the hint for specifying a database shard is used in an INSERT statement that contains a sequence for the target table, the sequence will not take effect. For more information, see Limits and precautions for sequences.

Specify a database shard by using a shard name, to run an SQL statement This custom hint allows you to specify one or more database shards to run an SQL statement. Specify one database shard to run an SQL statement:

```
/! TDDL:NODE='node_name'*/
```

Specifically, `node_name` indicates the shard name. This PolarDB-X 1.0 hint enables you to route the SQL statement to the database shard specified by `node_name` . Specify multiple database shards to run an SQL statement:

```
/! TDDL:NODE IN ('node_name'[,'node_name1','node_name2'])*/
```

The `IN` keyword is used to specify multiple shard names. This custom hint allows you to route the SQL statement to multiple database shards. Separate multiple shard names with commas (,).

> Not e When this custom hint is used, the PolarDB-X 1.0 instance directly routes the SQL statement to the specified database shards for execution. Therefore, the specified shard names in the SQL statement must correspond to existing database shards.

Specify a database shard by using the value of the database shard key, to run an SQL statement

```
/! TDDL:table_name.partition_key=value [and table_name1.partition_key=value1]*/
```

In this PolarDB-X 1.0 hint, `table_name` indicates the name of a logical table, and this table is a partitioned table. In addition, `partition_key` indicates a shard key, and `value` indicates the value specified for the shard key. In this custom hint, you can use the `and` keyword to specify the shard keys of multiple partitioned tables. When this PolarDB-X 1.0 hint is used, the PolarDB-X 1.0 instance calculates the database shards and table shards where the SQL statement is to be executed, and routes the SQL statement to the corresponding database shards.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples The following shows the responses of the `SHOW NODE` statement for a logical database named `drds_test` in a PolarDB-X 1.0 instance.

```
mysql> SHOW NODE\G
*************************** 1. row ******************
                 ID: 0
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS
  MASTER_READ_COUNT: 212
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 2. row ******************
                 ID: 1
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0001_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 3. row ******************
                 ID: 2
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0002_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 4. row ******************
                 ID: 3
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0003_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
```

```
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 5. row ******************
                 ID: 4
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0004_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 6. row ******************
                 ID: 5
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0005_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 7. row ******************
                 ID: 6
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0006_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
*************************** 8. row ******************
                 ID: 7
               NAME: DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0007_RDS
  MASTER_READ_COUNT: 29
   SLAVE_READ_COUNT: 0
MASTER_READ_PERCENT: 100%
 SLAVE_READ_PERCENT: 0%
8 rows in set (0.02 sec)
```

As you can see, each database shard has the `NAME` attribute, which indicates the shard name corresponding to the database shard. Each shard name uniquely corresponds to one database shard

| DRDS TEST 1473471355140LRPRDRDS TEST VTLA 0003 RDS _ _ _ _ _ _ |   |   |
|---|---|---|
| name | drds test vtla 0003 _ _ _ | . Therefore, after obtaining |

name, you can use the PolarDB-X 1.0 hint to specify the corresponding database shard to run the SQL statement. Specify database shard 0 to run an SQL statement:

```
/! TDDL:NODE='DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS'*/SELECT * FROM table_na me;
```

Specify multiple database shards to run an SQL statement:

```
/! TDDL:NODE IN('DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS','DRDS_TEST_14734713 55140LRPRDRDS_TEST_VTLA_0006_RDS')*/SELECT * FROM table_name;
```

This SQL statement will be executed in the database shards whose shard names are `DRDS_TEST_1473`

```
471355140LRPRDRDS_TEST_VTLA_0000_RDS and DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0006_R
```

`DS` . View the execution plan of an SQL statement in a specified database shard:

```
/! TDDL:NODE='DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_0000_RDS'*/EXPLAIN SELECT * FROM table_name;
```

After this SQL statement is executed, the execution plan of the `SELECT` statement in the database shard corresponding to the shard name `DRDS_TEST_1473471355140LRPRDRDS_TEST_VTLA_000` `0_RDS` will be returned. Specify a database shard by using the value of the database shard key, to run an SQL statement: PolarDB-X 1.0 does not support subqueries in the `SET` clause of an `UPDATE` statement, because a shard key must be specified for `UPDATE` statements in PolarDB-X 1.0. To address this issue, PolarDB-X 1.0 provides a custom hint to route the statement to a database shard for execution. For example, the following shows the CREATE TABLE statement for creating two logical tables t1 and t2, which are partitioned into table shards in database shards:

```
CREATE TABLE `t1` (
    `id` bigint(20) NOT NULL,
    `name` varchar(20) NOT NULL,
    `val` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by hash(`id`) tbpartition by hash(`nam
e`) tbpartitions 3
  CREATE TABLE `t2` (
    `id` bigint(20) NOT NULL,
    `name` varchar(20) NOT NULL,
    `val` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by hash(`id`) tbpartition by hash(`nam
e`) tbpartitions 3
```

The following SQL statement is to be executed for the two tables:

```
UPDATE t1 SET val=(SELECT val FROM t2 WHERE id=1) WHERE id=1;
```

If this statement is directly executed in a PolarDB-X 1.0 instance, an error will be returned indicating that this statement is not supported. In this case, you can add the PolarDB-X 1.0 hint to this SQL statement before submitting it to the PolarDB-X 1.0 instance for execution. The SQL statements are as follows:

```
/! TDDL:t1.id=1 and t2.id=1*/UPDATE t1 SET val=(SELECT val FROM t2 WHERE id=1) WHERE id=1
```

; This statement will be routed to database shards of `t1` , with the `id` of the database shards being 1. You can run the following `EXPLAIN` command to view the execution plan of this SQL statement:

```
  mysql> explain /! TDDL:t1.id=1 and t2.id=1*/UPDATE t1 SET val=(SELECT val FROM t2 WHERE
id=1) WHERE id=1\G
  *************************** 1. row ***************************
  GROUP_NAME: TEST_DRDS_1485327111630IXLWTEST_DRDS_IGHF_0001_RDS
         SQL: UPDATE `t1_2` AS `t1` SET `val` = (SELECT val FROM `t2_2` AS `t2` WHERE `id
` = 1) WHERE `id` = 1
      PARAMS: {}
  *************************** 2. row ***************************
  GROUP_NAME: TEST_DRDS_1485327111630IXLWTEST_DRDS_IGHF_0001_RDS
         SQL: UPDATE `t1_1` AS `t1` SET `val` = (SELECT val FROM `t2_1` AS `t2` WHERE `id
` = 1) WHERE `id` = 1
      PARAMS: {}
  *************************** 3. row ***************************
  GROUP_NAME: TEST_DRDS_1485327111630IXLWTEST_DRDS_IGHF_0001_RDS
         SQL: UPDATE `t1_0` AS `t1` SET `val` = (SELECT val FROM `t2_0` AS `t2` WHERE `id
` = 1) WHERE `id` = 1
      PARAMS: {}
  3 rows in set (0.00 sec)
```

According to the result set of the `EXPLAIN` command, the SQL statement is rewritten into three statements, which are then routed to the database shards for execution. You can further specify a table shard by using the value of the table shard key, to narrow the execution scope of the SQL statement to a specified table shard.

```
  mysql> explain /! TDDL:t1.id=1 and t2.id=1 and t1.name='1'*/UPDATE t1 SET val=(SELECT v
al FROM t2 WHERE id=1) WHERE id=1\G
  *************************** 1. row ***************************
  GROUP_NAME: TEST_DRDS_1485327111630IXLWTEST_DRDS_IGHF_0001_RDS
         SQL: UPDATE `t1_1` AS `t1` SET `val` = (SELECT val FROM `t2_1` AS `t2` WHERE `id
` = 1) WHERE `id` = 1
      PARAMS: {}
  1 row in set (0.00 sec)
```

> Not e Before using this custom hint, you must ensure that the logical tables t1 and t2 are partitioned into the same number of database shards and the same number of table shards. Otherwise, the database shards calculated by the PolarDB-X 1.0 instance based on the conditions are different, and an error will be returned.

### 9.6 Scan all database shards and table shards

table shards In addition to routing an SQL statement to one or more database shards for execution, PolarDB-X 1.0 provides a custom hint to allow you to scan all database shards and table shards. With this custom hint, you can route an SQL statement to each database shard at a time. For example, you can use this custom hint to view all the table shards in a specified database shard. In addition, you can use this custom hint to view the data volume of table shards in each database shard corresponding to a specified logical table. Syntax With this PolarDB-X 1.0 hint, you can route an SQL statement to all database shards for execution and route an SQL statement to all database shards to perform an operation on a specified logical table. Route an SQL statement to all database shards for execution:

```
/! TDDL:SCAN*/
```

Perform an operation on a specified logical table:

```
/! TDDL:SCAN='table_name'*/
```

The `table_name` parameter indicates the name of a logical table in the logical database of a PolarDB-X 1.0 instance. This custom hint is provided for table shards in database shards. Ensure that the value of `table_name` is the name of a table shard in database shards.

|   | Not e PolarDB-X 1.0 hints can be in the formats of /*+TDDL:hint command*/ and /! +TDDL:hin _ t command*/ . _ In the MySQL command-line client, you may need to execute an SQL statement that contains a PolarDB-X 1.0 hint in the format of /*+TDDL:hint command*/ . In this case, add the -c _ parameter to the logon command. Otherwise, the client deletes the PolarDB-X 1.0 hint before it sends the SQL statement to the server for execution because the PolarDB-X 1.0 hint is in the format of a MySQL comment. In this case, the hint fails to take effect. For more information, see MySQL Client Options. |   |   |
|---|---|---|---|
|   |   | /! +TDDL:hin |   |
|   | t command*/ _ |   |   |

Examples View the data volume of a specified broadcast table in each database shard:

```
/! TDDL:SCAN*/SELECT COUNT(1) FROM table_name
```

In this SQL statement, `table_name` indicates a broadcast table. This hint causes the PolarDB-X instance to route the SQL statement to each database shard for execution. Therefore, the result sets include the total data volume of the broadcast table `table_name` in all database shards. This statement allows you to conveniently check whether the data of a broadcast table is normal. Scan a single-database non-partition logical table:

```
/! TDDL:SCAN*/SELECT COUNT(1) FROM table_name
```

| QL | select count(1) from table name _ |   |
|---|---|---|
| table name _ |   | parameter indicates a lo |

This hint causes the PolarDB-X instance to route the SQL `select count(1) from table_name` statement to each database shard for execution. The `table_name` parameter indicates a logical table in a logical database of a PolarDB-X 1.0 instance. Before using this hint, ensure that each database shard contains the table shard `table_name` . In other words, the table shard `table_name` is a logical table that is only partitioned into database shards, but not partitioned into table shards. Otherwise, an error that indicates that the table is not found will be returned. Scan a partitioned logical table in database shards:

```
/! TDDL:SCAN='table_name'*/SELECT COUNT(1) FROM table_name
```

When executing this statement, the PolarDB-X 1.0 instance first calculates all the database shards and table shards corresponding to the logical table `table_name` , and then generates a COUNT clause for each table shard in each database shard. View the execution plans of all database shards:

```
/! TDDL:SCAN='table_name'*/EXPLAIN SELECT * FROM table_name;
```

## 10 Distributed transactions

### 10.1 Distributed transactions based on MySQL 5.7

on MySQL 5.7

> Not e
> When you use MySQL 5.7 or later and PolarDB-X 1.0 5.3.4 or later, XA distributed transactions are automatically enabled. The user experience of the XA distributed transactions is the same as that of single-database transactions in MySQL. No special commands are required to enable XA distributed transactions.

When you use MySQL and a PolarDB-X instance in other versions, see Distributed transactions based on MySQL 5.6. How it works When you use MySQL 5.7 or later, the PolarDB-X 1.0 instance processes distributed transactions based on the XA protocol by default. Use method The user experience of distributed transactions in a PolarDB-X 1.0 instance is the same as that of singledatabase transactions in MySQL, for example, in terms of the following commands: `SET AUTOCOMMIT=0` : Start a transaction. `COMMIT` : Commit the current transaction. `ROLLBACK` : Roll back the current transaction. If the SQL statement in a transaction involves only a single shard, the PolarDB-X 1.0 instance routes the transaction directly to the ApsaraDB RDS for MySQL instance as a single-database transaction. If the SQL statement in the transaction is to modify the data of multiple shards, the PolarDB-X 1.0 instance automatically upgrades the current transaction to a distributed transaction.

### 10.2 Distributed transactions based on MySQL 5.6

on MySQL 5.6 How it works The XA protocol for MySQL 5.6 is not mature. Therefore, the PolarDB-X 1.0 instance independently implements two-phase commit (2PC) transaction policies for distributed transactions. When you use MySQL 5.7 or later, we recommend that you use XA transaction policies.

> Not e The distributed transactions described in this topic are intended for users who use MySQL 5.6 or PolarDB-X 1.0 earlier than 5.3.4. When you use MySQL 5.7 or later and a PolarDB-X 1.0 instance in 5.3.4 or later, see Distributed transactions based on MySQL 5.7.

Use method If a transaction involves multiple database shards, you must declare the current transaction as a distributed transaction. If a transaction involves only a single database shard, you do not need to enable distributed transactions, but can process the transaction as a single-database transaction in MySQL. No additional operations are required. To enable distributed transactions, do as follows: After transactions are enabled, run `SET drds_transaction_policy = '...'` . To enable 2PC transactions in the MySQL command-line client, run the following statements:

```
SET AUTOCOMMIT=0; SET drds_transaction_policy = '2PC'; -- We recommend that you use MySQL 5.6 to run this com mand. .... -- Here, you can run your business SQL statement. COMMIT; -- You can alternatively write ROLLBACK.
```

To enable 2PC transactions by using the Java database connectivity (JDBC) API, write the code as follows:

```
conn.setAutoCommit(false); try (Statement stmt = conn.createStatement()) {
    stmt.execute("SET drds_transaction_policy = '2PC'");
```

`}`

```
// ... Here, you can run your business SQL statement. conn.commit(); // You can alternatively write rollback().
```

FAQ Q: How can I use PolarDB-X 1.0 distributed transactions in the Spring framework? A: If you enable transactions by using the Spring `@Transactional` annotation, you can enable PolarDB-X 1.0 distributed transactions by extending the transaction manager. Sample code:

```java
import org.springframework.jdbc.datasource.DataSourceTransactionManager; import org.springframework.transaction.TransactionDefinition; import javax.sql.DataSource; import java.sql.Connection; import java.sql.SQLException; import java.sql.Statement; public class DrdsTransactionManager extends DataSourceTransactionManager {
    public DrdsTransactionManager(DataSource dataSource) {
        super(dataSource);
```

`}`

```java
    @Override
    protected void prepareTransactionalConnection(Connection con, TransactionDefinition def
inition) throws SQLException {
        try (Statement stmt = con.createStatement()) {
            stmt.executeUpdate("SET drds_transaction_policy = '2PC'"); // A 2PC transaction
is used as an example.
```

`}` `}` `}` After that, instantiate the preceding class in the Spring configuration. For example, you can write the code as follows:

```
<bean id="drdsTransactionManager" class="my.app.DrdsTransactionManager">
     <property name="dataSource" ref="yourDataSource" />
</bean>
```

To enable PolarDB-X 1.0 distributed transactions for a class, you can add the `@Transactional("drdsTransactionManager")` annotation.

## 11 DDL operations

### 11.1 DDL statements

The data definition language (DDL) statement CREATE TABLE in a PolarDB-X 1.0 instance is similar to that in a MySQL database, and is extended based on the syntax in a MySQL database. To create a table shard in a PolarDB-X 1.0 instance, you must specify the table sharding manner and the database

| ing manner in the | drds partition options _ _ |   |   |   |   | paramete |
|---|---|---|---|---|---|---|
| TBPARTITION BY |   | , | TBPARTITIONS | , and | BROADCAST |   |

Currently, you can run a DDL statement in the following ways: Run the DDL statement through the MySQL command-line client, for example, by using MySQL command lines, Navicat, or MySQL Workbench. Connect to the specified PolarDB-X 1.0 instance by using program code and then call the DDL statement for execution. For the syntax of the CREATE TABLE statement in a MySQL database, see MySQL CREATE TABLE Statement.

### 11.2 CREATE TABLE statement

#### 11.2.1 Overview

This topic describes the syntax, clauses, parameters, and basic methods for creating a table by using a data definition language (DDL) statement.

> Not e PolarDB-X 1.0 instances do not allow you to directly create a database by using a DDL statement. To create a database, you can Log on to the PolarDB-X console. For the information about how to create a database, see Create a database.

Syntax

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [drds_partition_options]
    [partition_options]
drds_partition_options:
    DBPARTITION BY
        HASH([column])
        [TBPARTITION BY
            { HASH(column)
            | {MM|DD|WEEK|MMDD}(column)}
          [TBPARTITIONS num]
```

`]` Clauses and parameters for database and table sharding `DBPARTITION BY hash(partition_key)` : This parameter specifies the shard key and the sharding algorithm for database sharding. Database sharding by time is not supported. TBPARTITION BY { HASH(column) | {MM|DD|WEEK|MMDD}(column) : (Optional) This parameter specifies the method of mapping data to a physical table. The value is the same as that of DBPARTITION BY by default. `TBPARTITIONS num` : (Optional) This parameter specifies the number of physical tables to be created in each database shard. The default value is 1. If no table sharding is required, you do not need to specify this parameter.

#### 11.2.2 Create a single-database non-partition table

table This topic describes how to create a single-database non-partition table. Create a single-database non-partition table

```
CREATE TABLE single_tbl(
  id int,
  name varchar(30),
  primary key(id)
```

); According to the node topology of the logical table, you can see that a single-database non-partition logical table is created in database 0.

```
mysql> show topology from single_tbl; +------+------------------------------------------------------------------+------------+
| ID   | GROUP_NAME                                                       | TABLE_NAME |
+------+------------------------------------------------------------------+------------+
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | single_tbl |
+------+------------------------------------------------------------------+------------+ 1 row in set (0.01 sec)
```

Specify parameters You can also specify the `select_statement` parameter when creating a a single-database nonpartition table. If you need to create table shards, you cannot specify this parameter.

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]
    select_statement
```

For example, you can run the following statement to create a single-database non-partition table single_tbl2 to store the data from the single_tbl table. In this case, no sharding is required.

```
CREATE TABLE single_tbl2(
  id int,
  name varchar(30),
  primary key(id)
) select * from single_tbl;
```

#### 11.2.3 Create a non-partition table in database shards

shards This topic describes how to create a non-partition table in database shards. Assume that eight database shards have been created. You can run the following command to create a non-partition table in the database shards by calculating the hash function based on the userId shard key.

```
CREATE TABLE multi_db_single_tbl(
  id int,
  name varchar(30),
  primary key(id)
) dbpartition by hash(id);
```

According to the node topology of the logical table, you can see that a table shard is created in each database shard. In other words, the table is only distributed to database shards.

```
mysql> show topology from multi_db_single_tbl; +------+------------------------------------------------------------------+---------------- -----+
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+---------------- -----+
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | multi_db_single
_tbl |
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | multi_db_single
_tbl |
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0002_RDS | multi_db_single
_tbl |
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0003_RDS | multi_db_single
_tbl |
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0004_RDS | multi_db_single
_tbl |
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS | multi_db_single
_tbl |
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0006_RDS | multi_db_single
_tbl |
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | multi_db_single
_tbl | +------+------------------------------------------------------------------+---------------- -----+ 8 rows in set (0.01 sec)
```

#### 11.2.4 Create table shards in database shards

This topic describes how to create table shards in database shards in different sharding manners. Use HASH for sharding Use RANGE_HASH for sharding Use date functions for sharding In the following examples, it is assumed that eight database shards have been created. Use HASH for sharding Create a table that is partitioned into table shards in database shards, with each database shard containing three physical tables. The database sharding process calculates the hash by using id as the shard key, and the table sharding process calculates the hash by using bid as the shard key. Specifically, a hash operation is performed on the data of the table based on the id column, to distribute the data to multiple database shards. Then, a hash operation is performed on the data in each database shard based on the bid column, to distribute the data to the three physical tables.

```
CREATE TABLE multi_db_multi_tbl(
  id int auto_increment,
  bid int,
  name varchar(30),
  primary key(id)
) dbpartition by hash(id) tbpartition by hash(bid) tbpartitions 3;
```

According to the node topology of the logical table, you can see that three table shards are created in each database shard.

```
mysql> show topology from multi_db_multi_tbl; +------+------------------------------------------------------------------+---------------- -------+
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+---------------- -------+
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | multi_db_multi_
tbl_00 |
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | multi_db_multi_
tbl_01 |
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | multi_db_multi_
tbl_02 |
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | multi_db_multi_
tbl_03 |
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | multi_db_multi_
tbl_04 |
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | multi_db_multi_
tbl_05 |
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0002_RDS | multi_db_multi_
tbl_06 |
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0002_RDS | multi_db_multi_
tbl_07 |
|    8 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0002_RDS | multi_db_multi_
tbl_08 |
|    9 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0003_RDS | multi_db_multi_
tbl_09 |
|   10 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0003_RDS | multi_db_multi_
tbl_10 |
|   11 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0003_RDS | multi_db_multi_
tbl_11 |
|   12 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0004_RDS | multi_db_multi_
tbl_12 |
|   13 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0004_RDS | multi_db_multi_
tbl_13 |
|   14 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0004_RDS | multi_db_multi_
tbl_14 |
|   15 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS | multi_db_multi_
tbl_15 |
|   16 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS | multi_db_multi_
tbl_16 |
|   17 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS | multi_db_multi_
tbl_17 |
```

|

```
18|S
```

`G` `S`

```
1231488766060743C
```

`S` `G` `S` `S`|

```
lidb
```

`l``i`

```
|   18 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0006_RDS | multi_db_multi_
tbl_18 |
|   19 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0006_RDS | multi_db_multi_
tbl_19 |
|   20 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0006_RDS | multi_db_multi_
tbl_20 |
|   21 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | multi_db_multi_
tbl_21 |
|   22 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | multi_db_multi_
tbl_22 |
|   23 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | multi_db_multi_
tbl_23 | +------+------------------------------------------------------------------+---------------- -------+ 24 rows in set (0.01 sec)
```

According to the sharding rule of the logical table, you can see that both database sharding and table sharding use the hash function, except that the database shard key is id and the table shard key is bid.

```
mysql> show rule from multi_db_multi_tbl; +------+--------------------+-----------+------------------+---------------------+--------- -----------+------------------+---------------------+--------------------+
| ID   | TABLE_NAME         | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTI
TION_COUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+--------------------+-----------+------------------+---------------------+--------- -----------+------------------+---------------------+--------------------+
|    0 | multi_db_multi_tbl |         0 | id               | hash                | 8
| bid              | hash                | 3                  |
+------+--------------------+-----------+------------------+---------------------+--------- -----------+------------------+---------------------+--------------------+ 1 row in set (0.01 sec)
```

Use RANGE_HASH for sharding Requirements The shard key must be a character or a number. Routing method Calculate a hash value based on the last N digits of any shard key, and then calculate the route by using RANGE_HASH. The number N is the third parameter in the function. For example, during calculation of the RANGE_HASH(COL1, COL2, N) function, COL1 is preferentially selected and then truncated to obtain the last N digits for calculation. If COL1 does not exist, COL2 is selected and truncated for calculation. Scenarios RANGE_HASH is applicable to scenarios where two shard keys are used for sharding but only the value of one shard is used for SQL query. Assume that a PolarDB-X 1.0 database is partitioned into eight physical databases. Our customer has the following requirements: i. The order table of each service needs to be partitioned into database shards by buyer ID and order ID. ii. The query is executed based on either the buyer ID or order ID as the condition. In this case, you can run the following DDL statement to create the order table:

```
create table test_order_tb (
           id int,
           seller_id varchar(30) DEFAULT NULL,
           order_id varchar(30) DEFAULT NULL,
           buyer_id varchar(30) DEFAULT NULL,
           create_time datetime DEFAULT NULL,
           primary key(id)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by RANGE_HASH(buyer_id, order_id, 10)
tbpartition by RANGE_HASH(buyer_id, order_id, 10) tbpartitions 3;
```

> Not e
> Neither of the two shard keys can be modified.
> Data insertion fails if the two shard keys point to different database shards or table shards.

Use date functions for sharding In addition to using the hash function as the sharding algorithm, you can also use the date functions MM, DD, WEEK, and MMDD as the table sharding algorithms. For more information, see the following examples: Create a table that is partitioned into table shards in database shards. The database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates DAY_OF_WEEK through the WEEK(actionDate) function and then partitions the table into table shards based on the actionDate column, with one week counted as seven days. For example, if the value in the actionDate column is 2017-02-27, which is on Monday, the value obtained by calculating the WEEK(actionDate) function is 2. In this case, the record is stored in table shard 2, because 2 % 7 = 2. This table shard is located in a database shard and is named user_log_2. For another example, if the value in the actionDate column is 2017-02-26, which is on Sunday, the value obtained by calculating the WEEK(actionDate) function is 1. In this case, the record is stored in table shard 1, because 1 % 7 = 1. This table shard is located in a database shard and is named user_log_1.

```
CREATE TABLE user_log( userId int, name varchar(30), operation varchar(30), actionDate DATE ) dbpartition by hash(userId) tbpartition by WEEK(actionDate) tbpartitions 7;
```

According to the node topology of the logical table, you can see that seven table shards are created in each database shard, because one week is counted as seven days in the function. The responses are very long, and therefore are omitted by using an ellipsis (...).

```
mysql> show topology from user_log; +------+------------------------------------------------------------------+------------+
| ID   | GROUP_NAME                                                       | TABLE_NAME |
+------+------------------------------------------------------------------+------------+
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_0 |
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_1 |
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_2 |
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_3 |
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_4 |
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_5 |
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log_6 |
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_0 |
|    8 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_1 |
|    9 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_2 |
|   10 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_3 |
|   11 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_4 |
|   12 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_5 |
|   13 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log_6 |
...
|   49 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_0 |
|   50 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_1 |
|   51 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_2 |
|   52 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_3 |
|   53 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_4 |
|   54 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_5 |
|   55 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log_6 |
+------+------------------------------------------------------------------+------------+ 56 rows in set (0.01 sec)
```

According to the sharding rule of the logical table, you can see that the database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates the WEEK function by using actionDate as the shard key.

```
mysql> show rule from user_log; +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | user_log   |         0 | userId           | hash                | 8
| actionDate       | week                | 7                  |
+------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 1 row in set (0.00 sec)
```

According to the specified database and table shard key parameters, you can see the specific physical table in the specific physical database to which the SQL statement is routed. View the route of the SQL statement Create a table that is partitioned into table shards in database shards. The database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates MONTH_OF_YEAR through the MM(actionDate) function and then partitions the table into table shards based on the actionDate column, with one year counted as 12 months. For example, if the value in the actionDate column is 2017-02-27, the value obtained by calculating the MM(actionDate) function is 02. In this case, the record is stored in table shard 02, because 02 % 12 = 02. This table shard is located in a database shard and is named user_log_02. For another example, if the value in the actionDate column is 2016-12-27, the value obtained by calculating the MM(actionDate) function is 12. In this case, the record is stored in table shard 00, because 12 % 12 =
00. This table shard is located in a database shard and is named user_log_00.

```
CREATE TABLE user_log2( userId int, name varchar(30), operation varchar(30), actionDate DATE ) dbpartition by hash(userId) tbpartition by MM(actionDate) tbpartitions 12;
```

According to the node topology of the logical table, you can see that 12 table shards are created in each database shard, because one year is counted as 12 months in the function. The responses are very long, and therefore are omitted by using an ellipsis (...).

```
mysql> show topology from user_log2; +------+------------------------------------------------------------------+--------------
```

`+`

```
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_00
```

|

```
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_01
```

|

```
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_02
```

|

```
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_03
```

|

```
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_04
```

|

```
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_05
```

|

```
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_06
```

|

```
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_07
```

|

```
|    8 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_08
```

|

```
|    9 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_09
```

|

```
|   10 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_10
```

|

```
|   11 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log2_11
```

|
|

```
12|SANGUANTEST1231488766060743ACTJSANGUANTEST123WVVP0001RDS|userlog200
```

```
|   12 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_00
```

|

```
|   13 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_01
```

|

```
|   14 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_02
```

|

```
|   15 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_03
```

|

```
|   16 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_04
```

|

```
|   17 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_05
```

|

```
|   18 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_06
```

|

```
|   19 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_07
```

|

```
|   20 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_08
```

|

```
|   21 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_09
```

|

```
|   22 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_10
```

|

```
|   23 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0001_RDS | user_log2_11
```

|

```
...
|   84 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_00
```

|

```
|   85 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_01
```

|

```
|   86 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_02
```

|

```
|   87 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_03
```

|

```
|   88 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_04
```

|

```
|   89 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_05
```

|

```
|   90 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_06
```

|

```
|   91 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_07
```

|

```
|   92 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_08
```

|

```
|   93 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_09
```

|

```
|   94 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_10
```

|

```
|   95 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log2_11
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
96 rows in set (0.02 sec)
```

According to the sharding rule of the logical table, you can see that the database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates the MM function by using actionDate as the shard key.

```
mysql> show rule from user_log2; +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | user_log2  |         0 | userId           | hash                | 8
| actionDate       | mm                  | 12                 |
+------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 1 row in set (0.00 sec)
```

Create a table that is partitioned into table shards in database shards. The database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates DAY_OF_MONTH through the DD(actionDate) function and then partitions the table into table shards, with one month counted as 31 days. For example, if the value in the actionDate column is 2017-02-27, the value obtained by calculating the DD(actionDate) function is 27. In this case, the record is stored in table shard 27, because 27 % 31 = 27. This table shard is located in a database shard and is named user_log_27.

```
CREATE TABLE user_log3( userId int, name varchar(30), operation varchar(30), actionDate DATE ) dbpartition by hash(userId) tbpartition by DD(actionDate) tbpartitions 31;
```

According to the node topology of the logical table, you can see that 31 table shards are created in each database shard, because one month is counted as 31 days in the function. The responses are very long, and therefore are omitted by using an ellipsis (...).

```
mysql> show topology from user_log3; +------+------------------------------------------------------------------+--------------
```

`+`

```
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_00
```

|

```
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_01
```

|

```
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_02
```

|

```
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_03
```

|

```
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_04
```

|

```
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_05
```

|

```
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_06
```

|

```
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_07
```

|

```
|    8 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_08
```

|

```
|    9 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_09
```

|

```
|   10 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_10
```

|

```
|   11 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_11
```

|

```
|   12 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_12
```

|

```
|   13 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_13
```

|

```
|   14 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_14
```

|

```
|   15 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_15
```

|

```
|   16 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_16
```

|

```
|   17 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_17
```

|

```
|   18 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_18
```

|

```
|   19 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_19
```

|

```
|   20 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_20
```

|

```
|   21 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_21
```

|

```
|   22 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_22
```

|

```
|   23 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_23
```

|

```
|   24 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_24
```

|

```
|   25 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_25
```

|

```
|   26 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_26
```

|

```
|   27 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_27
```

|

```
|   28 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_28
```

|

```
|   29 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_29
```

|

```
|   30 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log3_30
```

|

```
...
|  237 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_20
```

|

```
|  238 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_21
```

|

```
|  239 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_22
```

|

```
|  240 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_23
```

|

```
|  241 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_24
```

|

```
|  242 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_25
```

|

```
|  243 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_26
```

|

```
|  244 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_27
```

|

```
|  245 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_28
```

|

```
|  246 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_29
```

|

```
|  247 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log3_30
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
248 rows in set (0.01 sec)
```

According to the sharding rule of the logical table, you can see that the database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates the DD function by using actionDate as the shard key.

```
mysql> show rule from user_log3; +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | user_log3  |         0 | userId           | hash                | 8
| actionDate       | dd                  | 31                 |
+------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 1 row in set (0.01 sec)
```

Create a table that is partitioned into table shards in database shards. The database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates DAY_OF_YEAR % 365 through the MMDD(actionDate) tbpartitions 365 function and then partitions the table into 365 physical tables, with one year counted as 365 days. For example, if the value in the actionDate column is 2017-02-27, the value obtained by calculating the MMDD(actionDate) function is 58. In this case, the record is stored in table shard 58. This table shard is located in a database shard and is named user_log_58.

```
CREATE TABLE user_log4( userId int, name varchar(30), operation varchar(30), actionDate DATE ) dbpartition by hash(userId) tbpartition by MMDD(actionDate) tbpartitions 365;
```

According to the node topology of the logical table, you can see that 365 table shards are created in each database shard, because one year is counted as 365 days in the function. The responses are very long, and therefore are omitted by using an ellipsis (...).

```
mysql> show topology from user_log4; +------+------------------------------------------------------------------+--------------
```

`-+`

```
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+--------------
```

`-+`

```
...
| 2896 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_341
```

|

```
| 2897 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_342
```

|

```
| 2898 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_343
```

|

```
| 2899 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_344
```

|

```
| 2900 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_345
```

|

```
| 2901 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_346
```

|

```
| 2902 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_347
```

|

```
| 2903 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_348
```

|

```
| 2904 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_349
```

|

```
| 2905 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_350
```

|

```
| 2906 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_351
```

|

```
| 2907 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_352
```

|

```
| 2908 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_353
```

|

```
| 2909 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_354
```

|

```
| 2910 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_355
```

|

```
| 2911 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_356
```

|

```
| 2912 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_357
```

|

```
| 2913 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_358
```

|

```
| 2914 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_359
```

|

```
| 2915 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_360
```

|

```
| 2916 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_361
```

|

```
| 2917 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_362
```

|

```
| 2918 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_363
```

|

```
| 2919 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log4_364
```

|

```
+------+------------------------------------------------------------------+--------------
```

`-+`

```
2920 rows in set (0.07 sec)
```

According to the sharding rule of the logical table, you can see that the database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates the MMDD function by using actionDate as the shard key.

```
mysql> show rule from user_log4; +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | user_log4  |         0 | userId           | hash                | 8
| actionDate       | mmdd                | 365                |
+------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 1 row in set (0.02 sec)
```

Create a table that is partitioned into table shards in database shards. The database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates DAY_OF_YEAR % 10 through the MMDD(actionDate) tbpartitions 10 function and then partitions the table into 10 physical tables, with one year counted as 365 days.

```
CREATE TABLE user_log5( userId int, name varchar(30), operation varchar(30), actionDate DATE ) dbpartition by hash(userId) tbpartition by MMDD(actionDate) tbpartitions 10;
```

According to the node topology of the logical table, you can see that 10 table shards are created in each database shard, because one year is counted as 365 days in the function and the table data is routed to 10 physical tables. The responses are very long, and therefore are omitted by using an ellipsis (...).

```
mysql> show topology from user_log5; +------+------------------------------------------------------------------+--------------
```

`+`

```
| ID   | GROUP_NAME                                                       | TABLE_NAME
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
|    0 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_00
```

|

```
|    1 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_01
```

|

```
|    2 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_02
```

|

```
|    3 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_03
```

|

```
|    4 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_04
```

|

```
|    5 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_05
```

|

```
|    6 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_06
```

|

```
|    7 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_07
```

|

```
|    8 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_08
```

|

```
|    9 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0000_RDS | user_log5_09
```

|

```
...
|   70 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_00
```

|

```
|   71 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_01
```

|

```
|   72 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_02
```

|

```
|   73 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_03
```

|

```
|   74 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_04
```

|

```
|   75 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_05
```

|

```
|   76 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_06
```

|

```
|   77 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_07
```

|

```
|   78 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_08
```

|

```
|   79 | SANGUAN_TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0007_RDS | user_log5_09
```

|

```
+------+------------------------------------------------------------------+--------------
```

`+`

```
80 rows in set (0.02 sec)
```

According to the sharding rule of the logical table, you can see that the database sharding process calculates the hash by using userId as the shard key, and the table sharding process calculates the MMDD function by using actionDate as the shard key, and then routing the table data to 10 physical tables.

```
mysql> show rule from user_log5; +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
| ID   | TABLE_NAME | BROADCAST | DB_PARTITION_KEY | DB_PARTITION_POLICY | DB_PARTITION_C
OUNT | TB_PARTITION_KEY | TB_PARTITION_POLICY | TB_PARTITION_COUNT | +------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+
|    0 | user_log5  |         0 | userId           | hash                | 8
| actionDate       | mmdd                | 10                 |
+------+------------+-----------+------------------+---------------------+--------------- -----+------------------+---------------------+--------------------+ 1 row in set (0.01 sec)
```

#### 11.2.5 Use the primary key as the shard key

When no shard key is specified for the sharding algorithm, the system uses the primary key as the shard key by default. The following illustrates how to use the primary key as the database shard key and the table shard key. Use the primary key as the database shard key

```
CREATE TABLE prmkey_tbl( id int, name varchar(30), primary key(id) ) dbpartition by hash();
```

Use the primary key as the database shard key and the table shard key

```
CREATE TABLE prmkey_multi_tbl( id int, name varchar(30), primary key(id) ) dbpartition by hash() tbpartition by hash() tbpartitions 3;
```

#### 11.2.6 Create a broadcast table

The BROADCAST clause is used to specify a broadcast table to be created. A broadcast table is replicated to each database shard and data consistency is ensured between the database shards by using a synchronization mechanism with a delay of several seconds. This feature allows you to route a JOIN operation from a Cloud Native Distributed Database PolarDB-X (PolarDB-X) instance to an underlying ApsaraDB RDS for MySQL instance to prevent the JOIN operation from being performed in multiple databases. Overview describes how to optimize SQL statements by using broadcast tables. The following is an example statement for creating a broadcast table:

```
CREATE TABLE brd_tbl(
  id int,
  name varchar(30),
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 BROADCAST;
```

#### 11.2.7 Other attributes of the MySQL CREATE TABLE statement

TABLE statement When creating table shards in database shards, you can also specify other attributes of the table shards in the MySQL CREATE TABLE statement. For example, you can specify other attributes as follows:

```
CREATE TABLE multi_db_multi_tbl(
  id int,
  name varchar(30),
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by hash(id) tbpartition by hash(id) tbpart itions 3;
```

### 11.3 ALTER TABLE statement

The syntax of the ALTER TABLE statement used to modify a table is as follows:

```
ALTER [ONLINE|OFFLINE] [IGNORE] TABLE tbl_name
    [alter_specification [, alter_specification] ...]
    [partition_options]
```

In a PolarDB-X 1.0 instance, you can use this data definition language (DDL) statement to perform routine DDL operations, such as adding a column, adding an index, and modifying a data definition. For more information about the syntax, see MySQL ALTER TABLE Statement.

> Not e If you need to modify a table shard, you are not allowed to modify the shard key.

Add a column:

```
ALTER TABLE user_log
  ADD COLUMN idcard varchar(30);
```

Add an index:

```
ALTER TABLE user_log
  ADD INDEX idcard_idx (idcard);
```

Delete an index:

```
ALTER TABLE user_log
  DROP INDEX idcard_idx;
```

Modify a field:

```
ALTER TABLE user_log
  MODIFY COLUMN idcard varchar(40);
```

### 11.4 DROP TABLE statement

The syntax of the DROP TABLE statement used to delete a table is as follows:

```
DROP [TEMPORARY] TABLE [IF EXISTS]
    tbl_name [, tbl_name] ...
    [RESTRICT | CASCADE]
```

The DROP TABLE statement in a PolarDB-X 1.0 instance is the same as the DROP TABLE statement in a MySQL database. After the statement is executed, the system automatically deletes the corresponding physical table. For more information about the syntax, see MySQL DROP TABLE Statement. For example, you can run the following statement to delete the user_log table:

```
DROP TABLE user_log;
```

### 11.5 FAQ about DDL statements

What can I do if an error occurs during table creation? Data definition language (DDL) statements in a PolarDB-X 1.0 instance are processed in a distributed manner. If an error occurs, the structures of all table shards are inconsistent from each other. Therefore, you need to perform manual cleanup. Perform the following steps:
1. Check the basic error descriptions provided by the PolarDB-X 1.0 instance, such as syntax errors. If
the error message is too long, the system will prompt you to call the SHOW WARNINGS command to view the failure cause of each database shard.
2. Run the SHOW TOPOLOGY command to view the topology of physical tables.

```
SHOW TOPOLOGY FROM multi_db_multi_tbl; +------+-----------------+-----------------------+
| ID   | GROUP_NAME      | TABLE_NAME            |
+------+-----------------+-----------------------+
|    0 | corona_qatest_0 | multi_db_multi_tbl_00 |
|    1 | corona_qatest_0 | multi_db_multi_tbl_01 |
|    2 | corona_qatest_0 | multi_db_multi_tbl_02 |
|    3 | corona_qatest_1 | multi_db_multi_tbl_03 |
|    4 | corona_qatest_1 | multi_db_multi_tbl_04 |
|    5 | corona_qatest_1 | multi_db_multi_tbl_05 |
|    6 | corona_qatest_2 | multi_db_multi_tbl_06 |
|    7 | corona_qatest_2 | multi_db_multi_tbl_07 |
|    8 | corona_qatest_2 | multi_db_multi_tbl_08 |
|    9 | corona_qatest_3 | multi_db_multi_tbl_09 |
|   10 | corona_qatest_3 | multi_db_multi_tbl_10 |
|   11 | corona_qatest_3 | multi_db_multi_tbl_11 |
+------+-----------------+-----------------------+ 12 rows in set (0.21 sec)
```

3. Run the `CHECK TABLE tablename` command to check whether the logical table has been created.
For example, the following response indicates that a physical table corresponding to the logical table multi_db_multi_tbl failed to be created.

```
mysql> check table multi_db_multi_tbl; +-------------------------------------------------+-------+----------+----------------- ----------------------------------------------------------+
| TABLE                                           | OP    | MSG_TYPE | MSG_TEXT
```

|

```
+-------------------------------------------------+-------+----------+----------------- ----------------------------------------------------------+
| andor_mysql_qatest. multi_db_multi_tbl | check | Error    | Table 'corona_qatest_0. m
ulti_db_multi_tbl_02' doesn't exist | +-------------------------------------------------+-------+----------+----------------- ----------------------------------------------------------+ 1 row in set (0.16 sec)
```

4. Continue to create or delete the table in idempotent mode to create or delete the remaining
physical tables.

```
CREATE TABLE IF NOT EXISTS table1 (id int, name varchar(30), primary key(id)) dbpartition by hash(id); DROP TABLE IF EXISTS table1;
```

What can I do if I failed to create an index or add a column? The method for handling the failure in creating an index or adding a column is similar to that for the failure in creating a table. For more information, see Handle DDL exceptions.

### 11.6 DDL functions for sharding

#### 11.6.1 Overview

PolarDB-X 1.0 is a database service that supports both database sharding and table sharding. Support for PolarDB-X 1.0 database sharding and table sharding The following table lists the support for database sharding and table sharding in PolarDB-X 1.0data definition language (DDL) sharding functions.

| Sharding function | Description | Support for database sharding | Support for table sharding |
|---|---|---|---|
| HASH | Performs a simple modulus operation. | Yes | Yes |
| UNI HASH _ | Performs a simple modulus operation. | Yes | Yes |
| RIGHT SHIFT _ | Shifts the value to the right. | Yes | Yes |
| RANGE HASH _ | Performs double hashing. | Yes | Yes |
| MM | Performs hashing by month. | No | Yes |
| DD | Performs hashing by date. | No | Yes |
| WEEK | Performs hashing by week. | No | Yes |
| MMDD | Performs hashing by month and date. | No | Yes |
| YYYYMM | Performs hashing by year and month. | Yes | Yes |
| YYYYWEEK | Performs hashing by year and week. | Yes | Yes |
| YYYYDD | Performs hashing by year and date. | Yes | Yes |
| YYYYMM OPT _ | Performs optimized hashing by year and month. | Yes | Yes |
| YYYYWEEK OPT _ | Performs optimized hashing by year and week. | Yes | Yes |
| YYYYDD OPT _ | Performs optimized hashing by year and date. | Yes | Yes |

> Not e When using database sharding and table sharding in PolarDB-X 1.0, note the following:
> In a PolarDB-X 1.0 instance, the sharding method of a logical table is defined jointly by a sharding function and a shard key. The sharding function contains the number of shards to be created and the routing algorithm. The shard key also specifies the MySQL data type of the shard key.
> When the database sharding function is the same as the table sharding function and the database shard key is the same as the table shard key in a PolarDB-X 1.0 instance, the same sharding method is used for database sharding and table sharding. This allows the PolarDB- X 1.0 instance to uniquely locate one physical table in a physical database based on the value of the shard key.
> If the database sharding method and the table sharding method of a logical table are different and an SQL query does not contain both database shard key and table shard key, the PolarDB-X 1.0 instance scans all database shards or all table shards when processing the SQL query.

Support for data types of PolarDB-X DDL sharding functions Different PolarDB-X 1.0 DDL sharding functions support different data types. The following table lists the support for various data types in PolarDB-X 1.0 sharding functions (√ indicates supported and × indicates not supported). Support for data types in PolarDB-X 1.0 DDL sharding functions Syntax description for PolarDB-X DDL sharding functions PolarDB-X 1.0 is compatible with the CREATE TABLE statement in MySQL, and additionally provides the `drds_partition_options` keyword to support database sharding and table sharding:

```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [drds_partition_options]
    [partition_options]
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [drds_partition_options]
    [partition_options]
    select_statement
drds_partition_options:
    DBPARTITION BY
        { {HASH|YYYYMM|YYYYWEEK|YYYYDD|YYYYMM_OPT|YYYYWEEK_OPT|YYYYDD_OPT}([column])}
        [TBPARTITION BY
            { {HASH|MM|DD|WEEK|MMDD|YYYYMM|YYYYWEEK|YYYYDD|YYYYMM_OPT|YYYYWEEK_OPT|YYYYDD_O
PT}(column)}
          [TBPARTITIONS num]
```

`]`

#### 11.6.2 HASH

Requirements The shard key must be an integer or a string. This sharding function has no requirements on the version of a PolarDB-X 1.0 instance. It supports all PolarDB-X instances by default. Routing method When the HASH function is run by using different shard keys for database sharding and table sharding, perform the remainder operation on the value of the database shard key based on the number of database shards. If the value of the shard key is a string, the string is converted to a hash value before route calculation. For example, HASH('8') is equivalent to 8 % D, where D indicates the number of database shards. When the HASH function is run by using the same shard key for both database sharding and table sharding, perform the remainder operation on the value of the shard key based on the total number of table shards. For example, assume that two database shards are created, each database shard contains four table shards, table shards 0 to 3 are stored in database shard 0, and table shards 4 to 7 are stored in database shard 1. If a key value is 15, the key value 15 is distributed to table shard 7 in database shard 1, because 15 % (2 x 4) = 7. Scenarios HASH is applicable when database sharding is implemented by user ID or order ID. HASH is also applicable when the shard key is a string. Examples If you need to create a non-partition table in database shards by using the HASH function based on the ID column, you can use the following CREATE TABLE statement:

```
create table test_hash_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by HASH(ID);
```

Precautions The HASH is a simple modulus operation. The output distribution of the HASH function can be even only when the values in the partition column are evenly distributed.

#### 11.6.3 UNI_HASH

Requirements The shard key must be an integer or a string. The version of the PolarDB-X 1.0 instance must be 5.1.28-1508068 or later. For more information about the PolarDB-X 1.0 release notes, see View the instance version. Routing method When the UNI_HASH function is used for database sharding, perform a remainder operation on the value of the database shard key based on the number of database shards. If the value of the shard key is a string, the string is converted to a hash value before route calculation. For example, HASH('8') is equivalent to 8 % D, where D indicates the number of database shards. When the UNI_HASH function is run by using the same shard key for both database sharding and table sharding, perform the remainder operation on the value of the database shard key based on the number of database shards first (this step is different from that in the HASH function). Then, the data is evenly distributed to the table shards in the database shard. Scenarios UNI_HASH is applicable when database sharding is implemented by user ID or order ID. UNI_HASH is also applicable when the shard key is an integer or a string. UNI_HASH can be used when the following conditions are met: Two logical tables need to be partitioned into different numbers of table shards in database shards based on the same shard key. In addition, the two tables are frequently joined by using a JOIN statement based on the shard key. Comparison with HASH When you use the UNI_HASH function to create a non-partition table in database shards, the routing method is the same as that used in the HASH function. Specifically, the route is calculated by performing the remainder operation on the key value of the database shard key based on the number of database shards. When the UNI_HASH function is run by using the same shard key for both database sharding and table sharding, as the number of table shards changes, the database shard route calculated based on the same key value may also change. When the UNI_HASH function is run by using the same shard key for both database sharding and table sharding, the database shard route calculated based on the same key value is always the same regardless of the number of table shards. If two logical tables need to be partitioned into different table shards in database shards based on the same shard key, when the two tables are joined by using the HASH function based on the shard key, multi-database join may occur. However, when the two tables are joined by using the UNI_HASH function based on the shard key, multi-database join does not occur. Assume that you have two database shards and two logical tables, and each database shard in logical table a stores one table shard and each database shard in logical table b stores two table shards. The following figures separately show the results of a JOIN query for logical tables a and b after the HASH function is used for sharding and the results of a JOIN query for logical tables a and b after the HASH function is used for sharding. Comparison between HASH and UNI_HASH Examples If you need to create four table shards in each database shard by using the UNI_HASH function based on the ID column, you can run the following CREATE TABLE statement:

```
create table test_hash_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by UNI_HASH(ID) tbpartition by UNI_HASH(ID) tbpartitions 4;
```

Precautions The UNI_HASH is a simple modulus operation. The output distribution of the UNI_HASH function can be even only when the values in the shard column are evenly distributed.

#### 11.6.4 RIGHT_SHIFT

Requirements The shard key must be an integer. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Shift the value of the database shard key to the right by a specified number of binary digits, and then perform the remainder operation on the obtained integer based on the number of database shards or table shards. In particular, you can specify the number of shifted digits by running a data definition language (DDL) statement. Scenarios RIGHT_SHIFT is applicable to improve the evenness of the hash results when the lower-digit parts of most shard key values are very similar to each other but the higher-digit parts vary greatly. Assume that four shard key values are available: 12340000, 12350000, 12460000, and 12330000. The four lower digits of the four values are all 0000. Directly hashing the values of the shard keys outputs poor results. However, if you run the RIGHT_SHIFT(shardKey, 4) statement to shift the values of the shard keys to the right by four digits, to obtain 1234, 1235, 1246, and 1233, the hashing results are improved. Examples If you need to use the ID column as a shard key and shift the values of the ID column to the right by four binary digits to obtain hash values, you can run the following CREATE TABLE statement:

```
create table test_hash_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by RIGHT_SHIFT(id, 4) tbpartition by RIGHT_SHIFT(id, 4) tbpartitions 2;
```

Precautions The number of shifted digits cannot exceed the number of digits occupied by the integer.

#### 11.6.5 RANGE_HASH

Requirements The shard key must be a character or a number. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Calculate the hash value based on the last N digits of any shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes the route computing. The number N is the third parameter in the function. For example, during calculation of the RANGE_HASH(COL1, COL2, N) function, COL1 is preferentially selected and then truncated to obtain the last N digits for calculation. If COL1 does not exist, COL2 is selected and truncated for calculation. Scenarios RANGE_HASH is applicable to scenarios where a table needs to be partitioned by two shard keys but query is performed only based on the value of one shard key. Examples Assume that a PolarDB-X 1.0 database is partitioned into eight physical databases. Our customer has the following requirements: The order table of a business needs to be partitioned into database shards by buyer ID and order ID. The query is executed based on either the buyer ID or order ID as the condition. In this case, you can run the following DDL statement to create the order table:

```
create table test_order_tb (
    id int,
    buyer_id varchar(30) DEFAULT NULL,
    order_id varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    dbpartition by RANGE_HASH(buyer_id,order_id, 10)
    tbpartition by RANGE_HASH (buyer_id,order_id, 10) tbpartitions 3;
```

Precautions Neither of the two shard keys can be modified. Data insertion fails if the two shard keys point to different database shards or table shards.

#### 11.6.6 MM

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. MM is only applicable to table sharding. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Perform the remainder operation based on the month that corresponds to the time value of the database shard key to obtain the table shard subscript. Scenarios MM can be used to partition tables by month. The table shard name indicates a specific month. Examples Assume that we need to perform database sharding by ID, perform table sharding for the create_time column by month, and map every month to a physical table. The data definition language (DDL) statement is as follows:

```
create table test_mm_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by HASH(id) tbpartition by MM(create_time) tbpartitions 12;
```

Precautions When you partition tables with MM, ensure that each database shard has no more than 12 table shards because a year has 12 months.

#### 11.6.7 DD

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. DD is only applicable to table sharding. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Perform the remainder operation based on the day of the month that corresponds to the time value of the database shard key to obtain the table shard subscript. Scenarios DD can be used to partition tables based on a specified number of days in a month, that is, a date. The subscript of the table shard name indicates the day in a month. A month has 31 days at most. Examples Assume that we need to perform database sharding by ID, perform table sharding for the create_time column by day, and map every day to a physical table. The data definition language (DDL) statement is as follows:

```
create table test_dd_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by HASH(id) tbpartition by DD(create_time) tbpartitions 31;
```

Precautions When you partition tables with DD, ensure that each database shard has no more than 31 table shards because a month has 31 days at most.

#### 11.6.8 WEEK

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. WEEK is only applicable to table sharding. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Perform the remainder operation based on the day of a week that corresponds to the time value of the database shard key to obtain the table shard subscript. Scenarios WEEK can be used to partition tables based on days in a week. The subscript of the table shard name corresponds to each day of a week, from Monday to Sunday. Examples Assume that we need to perform database sharding by ID, perform table sharding for the create_time column by week, and map every day of a week (from Monday to Sunday) to a physical table. The data definition language (DDL) statement is as follows:

```
create table test_week_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by HASH(name) tbpartition by WEEK(create_time) tbpartitions 7;
```

Precautions When you partition tables with WEEK, ensure that each database shard has no more than seven table shards because a week has seven days.

#### 11.6.9 MMDD

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. MMDD is only applicable to table sharding. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Perform the remainder operation based on the number of days in a year that corresponds to the time value of the database shard key to obtain the table sharding subscript. Scenarios MMDD can be used to partition tables based on the number of days in a year that corresponds to a date in that year. The subscript of the table shard name indicates the day in that year, with a maximum of 366 days in a year. Examples Assume that we need to perform database sharding by ID, create tables for the create_time column by date (month-day), and map every day of a year to a physical table. The data definition language (DDL) statement is as follows.

```
create table test_mmdd_tb (
    id int,
    name varchar(30) DEFAULT NULL,
    create_time datetime DEFAULT NULL,
    primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by HASH(name) tbpartition by MMDD(create_time) tbpartitions 365;
```

Precautions When you partition tables with MMDD, ensure that each database shard has no more than 366 table shards because a year has 366 days at most.

#### 11.6.10 YYYYMM

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Calculate the hash value based on the year and months of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. For example, YYYYMM('2012-12-31 12:12:12') is equivalent to (2012 x 12 + 12) % D, where D indicates the number of database shards. Scenarios YYYYMM can be used to partition databases by year and month. We recommend that you use YYYYMM with tbpartition YYYYMM(ShardKey). Assume that a PolarDB-X 1.0 database is partitioned into eight physical databases. Our customer has the following requirements: Perform database sharding for a service by year and month. Distribute data from every month within two years to a separate table shard. Distribute a query with the database and table shard keys to a physical table shard of a physical database shard. The preceding requirements can be met by using YYYYMM. For the requirement of distributing data from every month within two years to a table shard (that is, one table shard stores the data of one month), create at least 24 physical table shards because a year has 12 months. Create three physical table shards for each database shard because the PolarDB-X 1.0 instance contains eight database shards. The data definition language (DDL) statement is as follows.

```
create table test_yyyymm_tb (
        id int,
        name varchar(30) DEFAULT NULL,
        create_time datetime DEFAULT NULL,
        primary key(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    dbpartition by YYYYMM(create_time)
    tbpartition by YYYYMM(create_time) tbpartitions 3;
```

Precautions YYYYMM does not support distributing data from every month in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle over months (for example, a cycle exists between 2012-03 and 2013-03), data from the same month may be routed to the same database or table shard, depending on the actual number of table shards.

#### 11.6.11 YYYYWEEK

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Calculate the hash value based on the year and weeks of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. For example, YYYYWEEK('2012-12-31 12:12:12') is equivalent to (2013 x 52 + 1) % D, with the date 2012-12-31 falling on the first week of 2013, where D indicates the number of database shards. Scenarios YYYYWEEK can be used to partition databases by year and the number of weeks in a year. We recommend that you use YYYYWEEK with tbpartition YYYYWEEK(ShardKey). Assume that a PolarDB-X 1.0 database is partitioned into eight physical databases. Our customer has the following requirements: Perform database sharding for a service by year and by week. Distribute data from every week within two years to a separate table shard. Distribute a query with the database and table shard keys to a physical table shard of a physical database shard. The preceding requirements can be met by using YYYYWEEK. For the requirement of distributing data from every week within two years to a table shard (that is, one table shard stores the data of one week), create at least 106 physical table shards because a year has roughly 53 weeks (rounded). Create 14 physical table shards for each database shard because the PolarDB-X 1.0 instance contains eight database shards (14 x 8 = 112 > 106). We recommend that the number of table shards be an integer multiple of the number of database shards. The data definition language (DDL) statement is as follows:

```
create table test_yyyymm_tb (
        id int,
        name varchar(30) DEFAULT NULL,
        create_time datetime DEFAULT NULL,
        primary key(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    dbpartition by YYYYWEEK(create_time)
    tbpartition by YYYYWEEK(create_time) tbpartitions 14;
```

Precautions YYYYWEEK does not support distributing data from every week in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle over weeks (for example, a cycle exists between the first week of 2012 and the first week of 2013), data from the same week after a cycle may be routed to the same database shard or table shard, depending on the actual number of table shards.

#### 11.6.12 YYYYDD

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Routing method Calculate the hash value based on the year and days of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. For example, YYYYDD('2012-12-31 12:12:12') is equivalent to (2012 x 366 + 365) % D, with 2012-12-31 as the 365th day of 2012, where D indicates the number of database shards. Scenarios Database sharding is performed by year and the number of days in a year. We recommend that you use YYYYDD with tbpartition YYYYDD(ShardKey). Assume that a PolarDB-X 1.0 database is partitioned into eight physical databases. Our customer has the following requirements: Perform database sharding for a service by year and day. Distribute data from every week within two years to a separate table shard. Distribute a query with the database and table shard keys to a physical table shard of a physical database shard. The preceding requirements can be met by using YYYYDD. For the requirement of distributing data from every day within two years to a table shard (that is, one table shard stores the data of one day), create at least 732 physical table shards because a year has up to 366 days. Create 92 physical table shards for each database shard because the PolarDB-X 1.0 instance contains eight database shards (732/8 = 91.5, rounded to 92). We recommend that the number of table shards be an integer multiple of the number of database shards. The data definition language (DDL) statement is as follows:

```
create table test_yyyydd_tb (
        id int,
        name varchar(30) DEFAULT NULL,
        create_time datetime DEFAULT NULL,
        primary key(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    dbpartition by YYYYDD(create_time)
    tbpartition by YYYYDD(create_time) tbpartitions 92;
```

Precautions YYYYDD does not support distributing data from every day in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle of a specific date (for example, a cycle exists between 2012-03-01 and 2013-03-01), data from the same date may be routed to the same database shard or table shard, depending on the actual number of table shards.

#### 11.6.13 YYYYMM_OPT

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The year and month of user data increase naturally over time, rather than randomly. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Optimizations Compared with YYYYMM, YYYYMM_OPT maintains the even distribution of data among ApsaraDB RDS for MySQL instances as the timeline increases. For example, assume that two ApsaraDB RDS for MySQL instances are attached to a PolarDB-X 1.0 instance, with 16 database shards. DB0 to DB7 shards are located on one ApsaraDB RDS for MySQL instance, and DB8 to DB15 shards are located on the other ApsaraDB RDS for MySQL instance. The following figure shows the mappings when YYYYMM and YYYYMM_OPT are used for database sharding, respectively. Comparison between YYYYMM and YYYYMM_OPT YYYYMM_OPT distributes data evenly to each ApsaraDB RDS for MySQL instance, helping to maximize the performance of each ApsaraDB RDS for MySQL instance. How to choose between YYYYMM and YYYYMM_OPT: YYYYMM_OPT can be used to distribute data evenly to each ApsaraDB RDS for MySQL instance if the time of service data generation increases sequentially and the data volume does not differ much between the time points. YYYYMM is applicable if the time of data generation increases randomly rather than sequentially. Routing method Calculate the hash value based on the year and months of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. The hash calculation based on the database and table shard key considers the data distribution among the ApsaraDB RDS for MySQL instances that connect to the PolarDB-X 1.0 instances. Scenarios Databases and tables need to be partitioned by year and month, respectively. Data must be evenly distributed to each ApsaraDB RDS for MySQL instance that connects to the PolarDB-X 1.0 instance. The time of the shard key increases sequentially rather than randomly, and the data volume is relatively average from month to month. For example, the number of monthly journal logs increases every month, and the log data is not concentrated on the same ApsaraDB RDS for MySQL instance. Precautions YYYYMM_OPT does not support distributing data from every month in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle over months (for example, a cycle exists between 2012-03 and 2013-03), data from the same month may be routed to the same database or table shard, depending on the actual number of table shards.

#### 11.6.14 YYYYWEEK_OPT

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Optimizations Compared with YYYYWEEK, YYYYWEEK_OPT maintains the even distribution of data among ApsaraDB RDS for MySQL instances as the timeline increases. The effect is similar to YYYYMM_OPT. YYYYWEEK_OPT distributes data evenly to each ApsaraDB RDS for MySQL instance, helping to maximize the performance of each ApsaraDB RDS for MySQL instance. How to choose between YYYYWEEK and YYYYWEEK_OPT: YYYYWEEK_OPT can be used to distribute data evenly to each ApsaraDB RDS for MySQL instance if the time of service data increases sequentially and the data volume does not differ much between time points. YYYYWEEK is applicable if the time of data generation increases randomly rather than sequentially. Routing method Calculate the hash value based on the year and weeks of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. The hash calculation based on the database and table shard key considers the data distribution among the ApsaraDB RDS for MySQL instances that connect to the PolarDB-X 1.0 instances. Scenarios Databases and tables are partitioned by year and week, respectively. Data must be evenly distributed to each ApsaraDB RDS for MySQL instance that connects to the PolarDB-X 1.0 instance. The time of the shard key increases sequentially rather than randomly, and the data volume is relatively average from week to week. For example, the number of weekly journal logs increases every week, and the log data is not concentrated on the same ApsaraDB RDS for MySQL instance. Precautions YYYYWEEK_OPT does not support distributing data from every week in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle over weeks (for example, a cycle exists between the first week of 2012 and the first week of 2013), data from the same week after a cycle may be routed to the same database shard or table shard, depending on the actual number of table shards.

#### 11.6.15 YYYYDD_OPT

Requirements The shard key must be of the DATE, DATETIME, or TIMESTAMP type. The version of the PolarDB-X 1.0 instance must be 5.1.28-1320920 or later. For more information, see View the instance version. Optimizations Compared with YYYYDD, YYYYDD_OPT maintains the even distribution of data among ApsaraDB RDS for MySQL instances as the timeline increases. The effect is similar to YYYYMM_OPT. YYYYDD_OPT distributes data evenly to each ApsaraDB RDS for MySQL instance, helping to maximize the performance of each ApsaraDB RDS for MySQL instance. How to choose between YYYYDD and YYYYDD_OPT: YYYYDD_OPT can be used to distribute data evenly to each ApsaraDB RDS for MySQL instance if the time of service data generation increases sequentially and the data volume does not differ much between time points. YYYYDD is applicable if the time of data generation increases randomly rather than sequentially. Routing method Calculate the hash value based on the year and days of the year in the time value of the database shard key and then perform the remainder operation on the hash value based on the number of database shards. This completes route computing. The hash calculation based on the database and table shard key considers the data distribution among the ApsaraDB RDS for MySQL instances that connect to the PolarDB-X 1.0 instances. Scenarios Databases and tables need to be partitioned by year and by day, respectively. Data must be evenly distributed to each ApsaraDB RDS for MySQL instance that connects to the PolarDB-X 1.0 instance. The time of the shard key increases sequentially rather than randomly, and the data volume is relatively average from day to day. For example, the number of daily journal logs increases every day, and the log data is not concentrated on the same ApsaraDB RDS for MySQL instance. Precautions YYYYDD_OPT does not support distributing data from every day in every year to a separate table shard. Instead, the number of table shards must be fixed. After a cycle of a specific date (for example, a cycle exists between 2012-03-01 and 2013-03-01), data from the same date may be routed to the same database shard or table shard, depending on the actual number of table shards. high-risk SQL statements

## 12 Automatic protection of high-risk SQL statements

high-risk SQL statements In PolarDB-X 1.0, the data manipulation language (DML) statements are the same as MySQL statements. We recommend that you include the shard key in the SELECT and UPDAT E statements of PolarDB-X 1.0. The INSERT statement of PolarDB-X 1.0 must include the shard key and a non-null key value. By default, PolarDB-X 1.0 disables full-table deletion and updating to prevent misoperation. The following statements are prohibited by default: A DELETE statement without the WHERE or LIMIT condition An UPDATE statement without the WHERE or LIMIT condition If you need to perform full-table deletion or update, you can temporarily skip this limit by using the following hint:

```
HINT: /! TDDL:FORBID_EXECUTE_DML_ALL=false*/
```

Examples Full-table deletion is intercepted by default.

```
mysql> delete from tt; ERR-CODE: [TDDL-4620][ERR_FORBID_EXECUTE_DML_ALL] Forbid execute DELETE ALL or UPDATE ALL sql. More: [http://middleware.alibaba-inc.com/faq/faqByFaqCode.html?faqCode=TDDL-4620]
```

The operation is successful if the following HINT is added:

```
mysql> /! TDDL:FORBID_EXECUTE_DML_ALL=false*/delete from tt; Query OK, 10 row affected (0.21 sec)
```

Full-table update is intercepted by default.

```
mysql> update tt set id = 1; ERR-CODE: [TDDL-4620][ERR_FORBID_EXECUTE_DML_ALL] Forbid execute DELETE ALL or UPDATE ALL sql. More: [http://middleware.alibaba-inc.com/faq/faqByFaqCode.html?faqCode=TDDL-4620]
```

The operation is successful if the following HINT is added:

```
mysql> /! TDDL:FORBID_EXECUTE_DML_ALL=false*/update tt set id = 1; Query OK, 10 row affected (0.21 sec)
```

This limit does not apply to DELETE or UPDATE statements that contain the WHERE or LIMIT condition.

```
mysql> delete from tt where id = 1; Query OK, 1 row affected (0.21 sec)
```

## 13 PolarDB-X sequence

### 13.1 Overview

A PolarDB-X 1.0 sequence (a 64-digit number of the signed BIGINT type in MySQL) is used to create a globally unique and sequentially incremental numeric sequence, such as values of primary key columns and unique key columns. PolarDB-X 1.0 sequences are used in the following two ways: Explicit sequences are created and maintained by using sequence-specific data definition language (DDL) syntax and can be used independently. The sequence value can be retrieved by using `select` seq.nextval; , where `seq` indicates the sequence name. Implicit sequences are used to automatically fill in primary keys with AUTO_INCREMENT defined and are automatically maintained by PolarDB-X 1.0.

> Not ice PolarDB-X 1.0 creates implicit sequences only after AUTO_INCREMENT is defined for partitioned tables and broadcast tables. This is not the case for non-partition tables. The AUTO_INCREMENT value of a non-partition table is created by ApsaraDB RDS for MySQL.

Types and features of PolarDB-X sequences Currently, three types of PolarDB-X sequences are supported.

| Type (abbreviat ion) | Globally unique | Consecuti ve | Monotoni cally increasing | Monotoni cally increasing within the same connectio n | Non- single point | Date types | Readabilit y |
|---|---|---|---|---|---|---|---|
| Group sequenc e (GROUP) | Yes | No | No | Yes | Yes | All integer types | High |
| T ime- based sequenc e (T IME) | Yes | No | Monotoni cally increasing at the macro level and non- monotoni cally increasing at the micro level | Yes | Yes | Only BIGINT | Low |

| Type (abbreviat ion) | Globally unique | Consecuti ve | Monotoni cally increasing | Monotoni cally increasing within the same connectio n | Non- single point | Date types | Readabilit y |
|---|---|---|---|---|---|---|---|
| Simple sequenc e (SIMPLE) | Yes | Yes | Yes | Yes | No | All integer types | High |

Concept s: Consecut ive: If the current value is n, the next value must be n + 1. If the next value is not n + 1, it is nonconsecutive. Monot onically increasing: If the current value is n, the next value must be a number greater than n. Single point : The risk of a single point of failure (SPOF) exists. Monot onically increasing at t he macro level and non-monot onically increasing at t he micro level: An example of this is `1, 3, 2, 4, 5, 7, 6, 8, ...` Such a sequence is monotonically increasing at the macro level and non-monotonically increasing at the micro level. Group sequence (GROUP, used by default) Feat ures A group sequence is a globally unique sequence with natural numeric values, which are not necessarily consecutive or monotonically increasing. If the sequence type is not specified, PolarDB-X 1.0 uses the group sequence type by default. Advant ages: A group sequence is globally unique and provides excellent performance, preventing single points of failure (SPOFs). Disadvant ages: A group sequence may contain nonconsecutive values, which may not necessarily start from the initial value and do not cycle. Implement at ion The values of a group sequence are created by multiple nodes to ensure high availability. The values in a segment are nonconsecutive if the values are not all used, such as in the case of disconnection. Time-based sequence (TIME) Feat ures A time-based sequence consists of a t imest amp, node ID, and serial number. It is globally unique and automatically increments at the macro level. Value updates are database-independent and not persistently stored in databases. Only names and types are stored in databases. This delivers good performance to time-based sequences, which create values like 776668092129345536, 776668098018148352, 776668111578333184, and 776668114812141568.

> Not ice Sequence values must be of t he BIGINT t ype when used in the auto-increment columns of tables.

Advant ages: Time-based sequences are globally unique with good performance. Disadvant ages: The values of a time-based sequence are nonconsecutive. The START WITH, INCREMENT BY, MAXVALUE, and CYCLE or NOCYCLE parameters are invalid for time-based sequences. Simple sequence (SIMPLE) Feat ures Only simple sequences support the START WITH, INCREMENT BY, MAXVALUE, and CYCLE or NOCYCLE parameters. Advant ages: Simple sequences are globally unique and monotonically increasing with consecutive values. Disadvant ages: Simple sequences are prone to SPOFs, poor performance, and bottlenecks. Use them with caution. Implement at ion Each sequence value must be persistently stored. Scenarios Group sequences, time-based sequences, and simple sequences are globally unique and can be used in primary key columns and unique index columns. We recommend that you use group sequences. Use only simple sequences for services that strongly depend on consecutive sequence values. Pay attention to sequence performance. We recommend that you use time-based sequences if you have high requirements for sequence performance, the amount of data inserted to tables is small, and large sequence values are acceptable. It is CPU-bound with no requirements on computing lock, database dependence, or persistent storage. The following example shows how to create a sequence with a start value value of 100000 and a step of 1. A simple sequence creates globally unique, consecutive, and monotonically increasing values, such as 100000, 100001, 100002, 100003, 100004, ..., 200000, 200001, 200002, 200003... Simple sequences are persistently stored. Even after services are restarted upon an SPOF, values are still created consecutively from the breakpoint. However, simple sequences have poor performance because each value is persistently stored once it is created. A group sequence may create values like 200001, 200002, 200003, 200004, 100001, 100002, 100003...

> Not ice
> The start value of a group sequence is not necessarily the same as the START WITH value (which is 100000 in this example) but is invariably greater than this value. In this example, the start value is 200001.
> A group sequence is globally unique but may contain nonconsecutive values, for example, when a node is faulty or the connection that only uses partial values is closed. The group sequence in this example contains nonconsecutive values because the values between 200004 and 100001 are missing.

A t ime-based sequence may create values like 776668092129345536, 776668098018148352, 776668111578333184, 776668114812141568...

### 13.2 Explicit sequence usage

This topic describes how to use data definition language (DDL) statements to create, modify, delete, and query sequences and how to retrieve the values of explicit sequences. Create a sequence Synt ax:

```
CREATE [ GROUP | SIMPLE | TIME ] SEQUENCE <name> [ START WITH <numeric value> ] [ INCREMENT BY <numeric value> ] [ MAXVALUE <numeric value> ] [ CYCLE | NOCYCLE ]
```

Paramet er descript ion:

| Parameter | Description | Applicable To |
|---|---|---|
| ST ART WT IH | The initial sequence value. If it is not set, the default value is 1. | Simple sequence and group sequence |
| INCREMENT BY | The increment (or interval value or step) of each sequence increase. If it is not set, the default value is 1. | Simple Sequence |
| MAXVALUE | The maximum sequence value. If it is not specified, the default value is the maximum value of the signed BIGINT type. | Simple Sequence |
| CYCLE or NOCYCLE | Indicates whether to repeat the sequence value which starts from the value specified by START WITH after the sequence value reaches the maximum value. If it is not specified, the default value is NOCYCLE. | Simple Sequence |

> Not e
> If the sequence type is not specified, the group sequence type is used by default.
> INCREMENT BY, MAXVALUE, and CYCLE or NOCYCLE do not take effect for group sequences.
> START WITH, INCREMENT BY, MAXVALUE, and CYCLE or NOCYCLE do not take effect for time- based sequences.
> Group sequences are nonconsecutive. The START WITH parameter only provides reference for group sequences. T he st art value of a group sequence is not necessarily t he same as t he ST ART WIT H value but is invariably great er t han t his value.

Example 1: Create a group sequence. Method 1:

```
mysql> CREATE SEQUENCE seq1; Query OK, 1 row affected (0.27 sec)
```

Method 2:

```
mysql> CREATE GROUP SEQUENCE seq1; Query OK, 1 row affected (0.27 sec)
```

Example 2: Create a time-based sequence.

```
mysql> CREATE TIME SEQUENCE seq1; Query OK, 1 row affected (0.27 sec)
```

Example 3: Create a simple sequence with a start value of 1,000, a step size of 2, and a maximum value of 99999999999, which does not repeat after increasing to the maximum value.

```
mysql> CREATE SIMPLE SEQUENCE seq2 START WITH 1000 INCREMENT BY 2 MAXVALUE 99999999999 NOCY CLE; Query OK, 1 row affected (0.03 sec)
```

Modify a sequence PolarDB-X 1.0 allows you to modify sequences in the following ways: For simple sequences, change the values of START WITH, INCREMENT BY, MAXVALUE, and CYCLE or NOCYCLE. For group sequences, change the value of START WITH. Convert the sequence type to another. Synt ax:

```
ALTER SEQUENCE <name> [ CHANGE TO GROUP | SIMPLE | TIME ] START WITH <numeric value> [ INCREMENT BY <numeric value> ] [ MAXVALUE <numeric value> ] [ CYCLE | NOCYCLE ]
```

Paramet er descript ion:

| Parameter | Description | Applicable To |
|---|---|---|
| ST ART WIT H | The initial sequence value. If it is not set, the default value is 1. | Simple sequence and group sequence |
| INCREMENT BY | The increment (or interval value or step) of each sequence increase. If it is not set, the default value is 1. | Simple Sequence |
| MAXVALUE | The maximum sequence value. If it is not specified, the default value is the maximum value of the signed BIGINT type. | Simple Sequence |

| Parameter | Description | Applicable To |
|---|---|---|
| CYCLE or NOCYCLE | Indicates whether to repeat the sequence value which starts from the value specified by START WITH after the sequence value reaches the maximum value. If it is not specified, the default value is NOCYCLE. | Simple Sequence |

> Not e
> Group sequences are nonconsecutive. The START WITH parameter only provides reference for group sequences. T he st art value of a group sequence is not necessarily t he same as t he ST ART WIT H value but is invariably great er t han t his value.
> If you set START WITH when modifying a simple sequence, the START WITH value takes effect immediately. The next automatically generated sequence value starts from the new START WITH value. For example, if you change the START WITH value to 200 when the sequence value increases to 100, the next automatically generated sequence value starts from 200.
> Before changing the START WITH value, you need to analyze the existing sequence values and the speed of creating sequence values to avoid conflicts. Exercise caution when you modify the START WITH value.

For example, change the start value of the simple sequence seq2 to 3000, the step size to 5, and the maximum value to 1000000. The sequence value repeats after increasing to the maximum value.

```
mysql> ALTER SEQUENCE seq2 START WITH 3000 INCREMENT BY 5 MAXVALUE 1000000 CYCLE; Query OK, 1 row affected (0.01 sec)
```

Convert the sequence type to another.

| CHANGE TO <sequence type> _ |   |   |
|---|---|---|
| ecify the | CHANGE TO | clause i |

| lause of | ALTER SEQUENCE |   |   | . |
|---|---|---|---|---|
| ALTER SEQUENCE |   | , the | START WITH |   |

added to avoid forgetting to specify the start value and get duplicate values. If the `CHANGE TO` clause is not specified, it is not required to add the START WITH parameter. Example: Convert a group sequence to a simple sequence.

```
mysql> ALTER SEQUENCE seq1 CHANGE TO SIMPLE START WITH 1000000; Query OK, 1 row affected (0.02 sec)
```

Delete a sequence Synt ax:

```
DROP SEQUENCE <name>
```

Example:

```
mysql> DROP SEQUENCE seq3; Query OK, 1 row affected (0.02 sec)
```

Query sequences Synt ax:

```
SHOW SEQUENCES
```

Example: The TYPE column lists the abbreviations of sequence types.

```
mysql> SHOW SEQUENCES; +------------+---------------------+--------------+------------+---------------------+----- --+--------+
| NAME       | VALUE               | INCREMENT_BY | START_WITH | MAX_VALUE           | CYCL
E | TYPE | +------------+---------------------+--------------+------------+---------------------+----- --+--------+
| AUTO_SEQ_1 | 91820513            | 1            | 91820200   | 9223372036854775807 | N
| SIMPLE |
| AUTO_SEQ_4 | 91820200            | 2            | 1000       | 9223372036854775807 | Y
| SIMPLE |
| seq_test   | N/A                 | N/A          | N/A        | N/A                 | N/A
| TIME   |
| AUTO_SEQ_2 | 100000              | N/A          | N/A        | N/A                 | N/A
| GROUP  |
| AUTO_SEQ_3 | 200000              | N/A          | N/A        | N/A                 | N/A
| GROUP  |
+------------+---------------------+--------------+------------+---------------------+----- --+--------+ 5 rows in set (0.01 sec)
```

Retrieve a sequence value Synt ax:

```
< sequence name >.NEXTVAL
```

Example:

```
SELECT sample_seq.nextVal FROM dual; +--------------------+
| SAMPLE_SEQ.NEXTVAL |
+--------------------+
|             101001 |
+--------------------+ 1 row in set (0.04 sec)
```

You can also write SAMPLE_SEQ.nextVal as a value to the SQL statement:

```
mysql> INSERT INTO some_users (name,address,gmt_create,gmt_modified,intro) VALUES ('sun',SA MPLE_SEQ.nextVal,now(),now(),'aa'); Query OK, 1 row affected (0.01 sec)
```

> Not e If you set the AUTO_INCREMENT parameter when creating a table, you do not need to specify an auto-increment column when running the INSERT statement. The auto-increment column is automatically maintained by PolarDB-X 1.0.

Retrieve sequence values in batches Synt ax:

```
SELECT < sequence name >.NEXTVAL FROM DUAL WHERE COUNT = < numeric value >
```

Example:

```
SELECT sample_seq.nextVal FROM dual WHERE count = 10; +--------------------+
| SAMPLE_SEQ.NEXTVAL |
+--------------------+
|             101002 |
|             101003 |
|             101004 |
|             101005 |
|             101006|
|             101007 |
|             101008 |
|             101009 |
|             101010 |
|             101011 |
+--------------------+ 10 row in set (0.04 sec)
```

### 13.3 Implicit sequence usage

After AUTO_INCREMENT is set for a primary key, the primary key is automatically filled in by using a sequence which is maintained by PolarDB-X 1.0. CREATE TABLE The standard CREATE TABLE syntax is extended to add the sequence type for auto-increment columns. If the type keyword is not specified, the default type is GROUP. Sequence names automatically created by PolarDB-X 1.0 and associated with tables are all prefixed with AUTO_SEQ_ and followed by the table names.

```xml
CREATE TABLE <name> (
   <column> ... AUTO_INCREMENT [ BY GROUP | SIMPLE | TIME ],
   <column definition>,
   ...
) ... AUTO_INCREMENT=<start value>
```

SHOW CREATE TABLE The sequence type is displayed for the auto-increment column of a table shard or broadcast table.

```
SHOW CREATE TABLE <name>
```

Examples If AUTO_INCREMENT is set but the sequence type is not specified when a table is created, a group sequence is used by default. Example 1 When creating a table, set AUTO_INCREMENT and specify a time-based sequence as the primary key value. Example 2 ALTER TABLE Currently, ALT ER T ABLE cannot be used to change the sequence type but can be used to change the initial value. To modify the implicit sequence type in a table, use the SHOW SEQUENCES command to find the sequence names and types, and then use the ALT ER SEQUENCE command to modify the sequences.

```
ALTER TABLE <name> ... AUTO_INCREMENT=<start value>
```

> Not ice If a PolarDB-X 1.0 sequence is used, exercise caution when modifying the start value of AUTO_INCREMENT. You need to carefully evaluate the already generated sequence values and the speed of generating new sequence values to prevent conflicts.

### 13.4 Limits and precautions for sequences

sequences This topic describes the limits and precautions for sequences. Limits and precautions When a time-based sequence is used in the auto-increment column of a table, the column must be of the BIGINT type.

| START WITH |   | must |
|---|---|---|
| When the | INSERT |   |

`START WITH` must be set when the sequence is changed to another type. When the `INSERT` statement is executed on a PolarDB-X 1.0 database in non-partition mode where only one ApsaraDB RDS for MySQL database is bound or on a database in partition mode that has only one table but no broadcast table, PolarDB-X 1.0 automatically optimizes and sends the statement, and bypasses the part of the optimizer that allocates the sequence value. In this case, `I` `NSERT INTO ... VALUES (seq.nextval, ...)` is not supported. We recommend that you use the ApsaraDB RDS for MySQL auto-increment column feature instead. If the hint for a specific database shard is used by the `INSERT` statement such as `INSERT INTO ..` . VALUES … or INSERT INTO … SELECT… and the target table uses a sequence, PolarDB-X 1.0 bypasses the optimizer and directly sends the statement so that the sequence does not take effect. The target table creates an ID by using the auto-increment feature of the ApsaraDB RDS for MySQL table. The auto-increment ID allocation method for the same table must be kept consistent, which may be based on PolarDB-X 1.0 sequences or the auto-increment column of the ApsaraDB RDS for MySQL. If both of the two allocation methods are used for the same table, duplicate IDs may be created and making location difficult. Troubleshoot primary key conflicts Assume that data is directly written to ApsaraDB RDS for MySQL and that the related primary key value is not the sequence value created by PolarDB-X 1.0. If PolarDB-X 1.0 automatically creates a primary key and writes it to the database, this primary key may conflict with that of the directly written data. This problem can be resolved as follows:
1. View the existing sequences by using the PolarDB-X 1.0-specified SQL statement. The sequence

| AUTO SEQ _ _ |   | is an imp |
|---|---|---|
| he | AUTO INCREMENT _ |   |

prefixed with `AUTO_SEQ_` is an implicit sequence. This sequence is generated when a table is

```
mysql> SHOW SEQUENCES; +-------------------------+-------+--------------+------------+-----------+-------+---- ---+
| NAME                    | VALUE | INCREMENT_BY | START_WITH | MAX_VALUE | CYCLE | TYP
E | +-------------------------+-------+--------------+------------+-----------+-------+---- ---+
| AUTO_SEQ_timeseq_test   | N/A   | N/A          | N/A        | N/A       | N/A   | TIM
E |
| AUTO_SEQ_xkv_shard_tbl1 | 0     | N/A          | N/A        | N/A       | N/A   | GRO
UP |
| AUTO_SEQ_xkv_shard      | 0     | N/A          | N/A        | N/A       | N/A   | GRO
UP | +-------------------------+-------+--------------+------------+-----------+-------+---- ---+ 3 rows in set (0.04 sec)
```

2. For example, if the t_item table contains conflicts and its primary key is ID, then retrieve the
maximum primary key value of this table from PolarDB-X 1.0:

```
mysql> SELECT MAX(id) FROM t_item; +-----------+
| max(id)   |
+-----------+
| 8231 |
+-----------+ 1 row in set (0.01 sec)
```

3. Update the related value in the PolarDB-X 1.0 sequence table to a value greater than 8231, such as
9000. Then, no error is returned for the auto-increment primary key created by the subsequent INSERT statement.

```
mysql> ALTER SEQUENCE AUTO_SEQ_USERS START WITH 9000; Query OK, 1 row affected (0.01 sec)
```

## 14 Best practices

### 14.1 Select a shard key

A shard key is a field for database sharding and table sharding, which is used to create sharding rules during horizontal partitioning. PolarDB-X 1.0 partitions a logical table horizontally into the physical database shards on each ApsaraDB RDS for MySQL instance based on the shard key. The primary principle of sharding is to identify the business logic-specific subject of data in a table as much as possible and confirm that most (or core) database operations are performed based on this subject. Then, use the subject-related field as the shard key to perform database sharding and table sharding. The business logic-specific subject is related to business scenarios. The following typical scenarios include business logic-specific subjects that can be used as shard keys: User-oriented Internet applications are operated to meet user requirements. Users are the business logic-specific subject and the user-related field can be used as the shard key. Seller-oriented e-commerce applications are operated to meet seller requirements. Sellers are the business logic-specific subject and the seller-related field can be used as the shard key. Game-oriented applications are operated to meet gamer requirements. Gamers are the business logic-specific subject and the gamer-related field can be used as the shard key. Internet of Vehicles (IoV) applications are operated based on vehicle information. Vehicles are the business logic-specific subject and the vehicle-related field can be used as the shard key. Tax-oriented applications are operated based on taxpayer information to provide frontend services. Taxpayers are the business logic-specific subject and the taxpayer-related field can be used as the shard key. In other scenarios, you can also use the appropriate subject of business logic as the shard key. For example, in a seller-oriented e-commerce application, the following single table must be horizontally partitioned:

```
CREATE TABLE sample_order (
  id INT(11) NOT NULL,
  sellerId INT(11) NOT NULL,
  trade_id INT(11) NOT NULL,
  buyer_id INT(11) NOT NULL,
  buyer_nick VARCHAR(64) DEFAULT NULL,
  PRIMARY KEY (id)
```

`)` The sellerId field is used as the shard key because seller is the business logic-specific subject. In the case of database sharding but no table sharding, the distributed data definition language (DDL) statement for table creation is as follows:

```
CREATE TABLE sample_order (
  id INT(11) NOT NULL,
  sellerId INT(11) NOT NULL,
  trade_id INT(11) NOT NULL,
  buyer_id INT(11) NOT NULL,
  buyer_nick VARCHAR(64) DEFAULT NULL,
  PRIMARY KEY (id)
) DBPARTITION BY HASH(sellerId)
```

If no business logic-specific subject can be used as the shard key, use the following methods to select an appropriate shard key: Determine the shard key based on the distribution and access of data. Distribute the data in a table to different physical database shards and table shards as evenly as possible. This method is applicable to scenarios with massive analytical queries, in which query concurrency stays at 1. Determine the shard key for database sharding and table sharding by combining fields of the numeric (string) type and time type. This method is applicable to log retrieval. For example, a log system records all user operations and needs to horizontally partition the following single log table:

```
CREATE TABLE user_log (
  userId INT(11) NOT NULL,
  name VARCHAR(64) NOT NULL,
  operation VARCHAR(128) DEFAULT NULL,
  actionDate DATE DEFAULT NULL
```

`)` You can combine the user identifier with the time field to create a shard key for partitioning the table by week. The distributed DDL statement for table creation is as follows:

```
CREATE TABLE user_log (
  userId INT(11) NOT NULL,
  name VARCHAR(64) NOT NULL,
  operation VARCHAR(128) DEFAULT NULL,
  actionDate DATE DEFAULT NULL
) DBPARTITION BY HASH(userId) TBPARTITION BY WEEK(actionDate) TBPARTITIONS 7
```

For more information about shard key selection and table shard forms, see DDL statements.

> Not ice Avoid using hotspot data as the shard key if possible.

### 14.2 Select the number of shards

PolarDB-X 1.0 supports horizontal partitioning of databases and tables. Eight physical database shards are created on each ApsaraDB RDS for MySQL instance by default, and one or more physical table shards can be created on each physical database shard. The number of table shards is also called the number of shards. Generally, we recommend that each physical table shard contain no more than 5 million rows of data. Generally, you can estimate the data growth in one to two years. Divide the estimated total data size by the total number of physical database shards, and then divide the result by the recommended maximum data size of 5 million, to obtain the number of physical table shards to be created on each physical database shard:

```
Number of physical table shards in each physical database shard = CEILING(Estimated total d ata size/(Number of ApsaraDB RDS for MySQL instances x 8)/5,000,000)
```

Therefore, when the calculated number of physical table shards is equal to 1, only database sharding needs to be performed, that is, a physical table shard is created in each physical database shard. If the calculation result is greater than 1, we recommend that you perform both database sharding and table sharding, that is, there are multiple physical table shards in each physical database shard. For example, if a user estimates that the total data size of a table will be about 0.1 billion rows two years later and the user has four ApsaraDB RDS for MySQL instances, then according to the preceding formula:

```
Number of physical table shards in each physical database shard = CEILING(100,000,000/(4 x 8)/5,000,000) = CEILING(0.625) = 1
```

The result is 1, so only database sharding is needed, that is, one physical table shard is created in each physical database shard. If only one ApsaraDB RDS for MySQL instance is used in the preceding example, the formula is as follows:

```
Number of physical table shards in each physical database shard = CEILING(100,000,000/(1 x 8)/5,000,000) = CEILING(2.5) = 3
```

The result is 3, so we recommend that you create three physical table shards in each physical database shard.

### 14.3 Basic concepts of SQL optimization

optimization PolarDB-X 1.0 is an efficient and stable distributed relational database service that processes distributed relational computing. PolarDB-X 1.0 optimizes SQL statements differently from singleinstance relational databases such as MySQL. PolarDB-X focuses on the network I/O overheads in a distributed environment and pushes SQL operations down to the underlying database shards (such as ApsaraDB RDS for MySQL) for execution, thereby reducing the network I/O overheads and improving the SQL execution efficiency. PolarDB-X 1.0 provides commands for obtaining the SQL execution information to help SQL optimization, for example, EXPLAIN commands for obtaining SQL execution plans and TRACE commands for obtaining SQL execution processes and overheads. This topic describes the basic concepts and common commands related to SQL optimization in PolarDB-X 1.0. Execution plan An SQL execution plan (or execution plan) is a set of ordered operation steps generated to access data. In PolarDB-X 1.0, the execution plan is divided into the execution plan at the PolarDB-X 1.0 layer and the execution plan at the ApsaraDB RDS for MySQL layer. Execution plan analysis is an effective way to optimize SQL statements. Through execution plan analysis, you can know whether PolarDB-X 1.0 or ApsaraDB RDS for MySQL has generated optimal execution plans for SQL statements and whether further optimization can be made. During SQL statement execution, based on the basic information of the SQL statement and related tables, the PolarDB-X 1.0 optimizer determines on which database shards the SQL statement should be executed, and the specific SQL statement form, execution policy, and data merging and computing policy for each database shard. This process optimizes SQL statement execution and generates execution plans at the PolarDB-X 1.0 layer. The execution plan at the ApsaraDB RDS for MySQL layer is the native MySQL execution plan. PolarDB-X 1.0 provides a set of EXPLAIN commands to display execution plans at different levels or with different levels of detail. The following table briefly describes the EXPLAIN commands in PolarDB-X 1.0. EXPLAIN command description

| Command | Description | Example |
|---|---|---|
| EXPLAIN { SQL } | Displays the summary execution plan of SQL statements at the PolarDB-X 1.0 layer, including the database shards on which the SQL statement is run, physical statements, and general parameters. | EXPLAIN SELECT * FROM test |
| EXPLAIN DETAIL { SQL } | Displays the detailed execution plans of SQL statements at the PolarDB-X 1.0 layer, including the statement type, concurrency, returned field information, physical tables, and database groups. | EXPLAIN DETAIL SELECT * FROM test |
| EXPLAIN EXECUTE { SQL } | Displays the execution plan of the underlying ApsaraDB RDS for MySQL instance, which is equivalent to the EXPLAIN statement of MySQL. | EXPLAIN EXECUTE SELECT * FROM test |

Execution plan at the PolarDB-X 1.0 layer The following table describes the fields in the results returned for the execution plan at the PolarDB-X 1.0 layer. Description of fields in execution plans at the PolarDB-X 1.0 layer

| Field | Description |
|---|---|

| Field | Description |
|---|---|
| GROUP NAME _ | The name of the PolarDB-X 1.0 database shard. The suffix identifies the specific database shard. The value is consistent with the result of the SHOW NODE command. |
| SQL | The SQL statement run on this database shard. |
| PARAMS | The SQL statement parameters used when PolarDB-X 1.0 communicates with ApsaraDB RDS for MySQL over the Prepare protocol. |

The SQL field can be in two forms:
1. If an SQL statement does not contain the following parts, the execution plan is displayed as an SQL
statement: Aggregate function involving multiple database shards. Distributed JOIN queries involving multiple shards. Complex subqueries. Examples:

```
mysql> EXPLAIN SELECT * FROM test; +----------------------------------------------+--------------------------------------- -----+--------+
| GROUP_NAME                                   | SQL
| PARAMS |
+----------------------------------------------+--------------------------------------- -----+--------+
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0000_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0001_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0002_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0003_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0004_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0005_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0006_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} |
| TESTDB_1478746391548CDTCTESTDB_OXGJ_0007_RDS | select `test`.`c1`,`test`.`c2` from `t
est` | {} | +----------------------------------------------+--------------------------------------- -----+--------+ 8 rows in set (0.04 sec)
```

The group names displayed in the GROUP_NAME field can be found in the returned result of SHOW NODE:

```
mysql> SHOW NODE; +----+----------------------------------------------+-------------------+-------------- ----+---------------------+--------------------+
| ID | NAME                                         | MASTER_READ_COUNT | SLAVE_READ_CO
UNT | MASTER_READ_PERCENT | SLAVE_READ_PERCENT | +----+----------------------------------------------+-------------------+-------------- ----+---------------------+--------------------+
| 0  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0000_RDS |                69 |
0 | 100% | 0% |
| 1  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0001_RDS |                45 |
0 | 100% | 0% |
| 2  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0002_RDS |                30 |
0 | 100% | 0% |
| 3  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0003_RDS |                29 |
0 | 100% | 0% |
| 4  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0004_RDS |                11 |
0 | 100% | 0% |
| 5  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0005_RDS |                 1 |
0 | 100% | 0% |
| 6  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0006_RDS |                 8 |
0 | 100% | 0% |
| 7  | TESTDB_1478746391548CDTCTESTDB_OXGJ_0007_RDS |                50 |
0 | 100% | 0% | +----+----------------------------------------------+-------------------+-------------- ----+---------------------+--------------------+ 8 rows in set (0.10 sec)
```

2. Execution plans that cannot be expressed by SQL statements can be expressed by PolarDB-X 1.0 in
custom format. Examples:

```
mysql> EXPLAIN DETAIL SELECT COUNT(*) FROM test; +------------------------------------------------+----------------------------------+-- ------+
| GROUP_NAME                                     | SQL                              | P
ARAMS | +------------------------------------------------+----------------------------------+-- ------+
| TEST_DB_1478746391548CDTCTEST_DB_OXGJ_0000_RDS | Merge as test
    queryConcurrency:GROUP_CONCURRENT
    columns:[count(*)]
    executeOn: TEST_DB_1478746391548CDTCTEST_DB_OXGJ_0000_RDS
        Query from test as test
            queryConcurrency:SEQUENTIAL
            columns:[count(*)]
            tableName:test
            executeOn: TEST_DB_1478746391548CDTCTEST_DB_OXGJ_0000_RDS
        Query from test as test
            queryConcurrency:SEQUENTIAL
            columns:[count(*)]
            tableName:test
            executeOn: TEST_DB_1478746391548CDTCTEST_DB_OXGJ_0001_RDS
        ... ...
        Query from test as test
            queryConcurrency:SEQUENTIAL
            columns:[count(*)]
            tableName:test
            executeOn: TEST_DB_1478746391548CDTCTEST_DB_OXGJ_0007_RDS
| NULL   |
+------------------------------------------------+----------------------------------+-- ------+ 1 row in set (0.00 sec)
```

executeOn in the SQL statement field indicates the database shard on which the SQL statement is run. PolarDB-X 1.0 finally merges the results returned by the database shards. Execution plans at the ApsaraDB RDS for MySQL layer The execution plans at the ApsaraDB RDS for MySQL layer are the same as the native MySQL execution plan. For more information, see official MySQL documentation. One PolarDB-X 1.0 logical table may consist of multiple table shards distributed in different database shards. Therefore, you can view the execution plans at the ApsaraDB RDS for MySQL layer in multiple ways.
1. View the execution plan of an ApsaraDB RDS for MySQL database shard.
If the query condition contains a shard key, directly run the EXPLAIN EXECUTE command to display the execution plan on the corresponding database shard. Examples:

```
mysql> EXPLAIN EXECUTE SELECT * FROM test WHERE c1 = 1; +----+-------------+-------+-------+---------------+---------+---------+-------+------+ -------+
| id | select_type | table | type  | possible_keys | key     | key_len | ref   | rows |
Extra | +----+-------------+-------+-------+---------------+---------+---------+-------+------+ -------+
|  1 | SIMPLE      | test  | const | PRIMARY       | PRIMARY | 4       | const |    1 |
NULL | +----+-------------+-------+-------+---------------+---------+---------+-------+------+ -------+ 1 row in set (0.04 sec)
```

> Not ice If an SQL statement involves multiple shards (for example, its condition does not contain a shard key), the EXPLAIN EXECUTE command returns an execution plan on a random ApsaraDB RDS for MySQL database shard.

To view the execution plan of an SQL statement on a specified database shard, you can add a hint. Examples:

```
mysql> /! TDDL:node='TESTDB_1478746391548CDTCTESTDB_OXGJ_0000_RDS'*/EXPLAIN SELECT * FR OM test; +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+
| id | select_type | table | type | possible_keys |  key  | key_len |  ref  | rows | Ex
tra | +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+
|  1 | SIMPLE      | test  | ALL  | NULL          | NULL  | NULL    | NULL  |    2 | NU
LL | +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+ 1 row in set (0.04 sec)
```

2. View the execution plans of all ApsaraDB RDS for MySQL database shards.
You can run SCAN HINT to display the execution plans of SQL statements on all database shards:

```
mysql> /! TDDL:scan='test'*/EXPLAIN SELECT * FROM test; +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+
| id | select_type | table | type | possible_keys |  key  | key_len |  ref  | rows | Ex
tra | +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+
|  1 | SIMPLE      | test  | ALL  | NULL          | NULL  | NULL    | NULL  |    2 | NU
LL |
|  1 | SIMPLE      | test  | ALL  | NULL          | NULL  | NULL    | NULL  |    3 | NU
LL | +----+-------------+-------+------+---------------+-------+---------+-------+------+--- ----+ 2 rows in set (0.08 sec)
```

> Not ice

i. In hint mode, PolarDB-X 1.0 only replaces the table names in case of database or table sharding, and then directly sends the logical SQL statement to ApsaraDB RDS for MySQL for execution. It will not process the result. ii. Execution plans obtained by using an EXPLAIN command are generated by static analysis and are not actually executed in databases. TRACE command The TRACE command in PolarDB-X 1.0 can track the SQL execution process and the overheads in each stage. It can be used together with the execution plan to facilitate SQL statement optimization. The TRACE command contains two related commands: TRACE and SHOW TRACE, which must be used together.

### 14.4 SQL optimization methods

#### 14.4.1 Overview

This topic describes the SQL optimization principles and methods for optimizing different types of SQL statements in PolarDB-X 1.0. Basic principles of SQL optimization In PolarDB-X 1.0, SQL computing that can be performed by ApsaraDB RDS for MySQL instances is called push-down computing. Push-down computing reduces data transmission, decreases overheads at the network layer and PolarDB-X 1.0 layer, and improves the execution efficiency of SQL statements. Therefore, the basic principle for SQL statement optimization in PolarDB-X 1.0 is as follows: Push down as many computations as possible to ApsaraDB RDS for MySQL instances. Push-down computations include: JOIN connections

| , such as WHERE or HAVING condition puting, such as COUNT and GROUP BY ORDER BY uch as DISTINCT ting, such as the NOW() function | WHERE | or | HAVING |   | condition |
|---|---|---|---|---|---|
|   |   |   |   | GROUP BY |   |

Sorting, such as `ORDER BY` Subqueries

> Not ice The preceding list only describes possible forms of push-down computations. It does not mean that all clauses or conditions or combinations of clauses or conditions can be pushed down for computing.

SQL statements of different types and containing different conditions can be optimized in different ways. The following uses some examples to describe how to optimize SQL statements: Filter condition optimization Optimization of the number of returned rows for a query Grouping and sorting optimization Optimization of push-down JOIN queries Optimization of distributed JOIN queries

#### 14.4.2 Single-table SQL optimization

Single-table SQL optimization must follow the following principles: Make sure that the SQL statements contain the shard key. Use an equivalence condition for the shard key whenever possible. If the shard key is an IN condition, the number of values after IN should be as small as possible (far fewer than the number of shards, and remain unchanged as the business grows). If SQL statements do not contain a shard key, use only one of DISTINCT, GROUP BY, and ORDER BY in the same SQL statement. Filter condition optimization PolarDB-X 1.0 partitions data horizontally by the shard key. Therefore, the filter condition must contain the shard key as much as possible so that PolarDB-X 1.0 can push queries down to specific database shards based on the shard key values, to avoid scanning all tables in the PolarDB-X 1.0 instance. For example, the shard key of the test table is c1. If the filter condition does not contain this shard key, full table scan is performed:

```
mysql> SELECT * FROM test WHERE c2 = 2; +----+----+
| c1 | c2 |
+----+----+
|  2 |  2 |
+----+----+ 1 row in set (0.05 sec)
```

The corresponding execution plan is as follows:

```
mysql> EXPLAIN SELECT * FROM test WHERE c2 = 2; +------------------------------------------------+----------------------------------------- ---------------------------+--------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ---------------------------+--------+
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0004_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0007_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0005_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0002_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0003_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0006_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0000_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0001_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c2` = 2) | {} | +------------------------------------------------+----------------------------------------- ---------------------------+--------+ 8 rows in set (0.00 sec)
```

The smaller the value range of the filter condition that contains the shard key, the faster the PolarDB-X 1.0 query speed. For example, a query on the test table contains a range filter condition with the shard key c1:

```
mysql> SELECT * FROM test WHERE c1 > 1 AND c1 < 4; +----+----+
| c1 | c2 |
+----+----+
|  2 |  2 |
|  3 |  3 |
+----+----+ 2 rows in set (0.04 sec)
```

The corresponding execution plan is as follows:

```
mysql> EXPLAIN SELECT * FROM test WHERE c1 > 1 AND c1 < 4; +------------------------------------------------+----------------------------------------- ---------------------------------------------------+--------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ---------------------------------------------------+--------+
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0002_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where ((`test`.`c1` > 1) AND (`test`.`c1` < 4)) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0003_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where ((`test`.`c1` > 1) AND (`test`.`c1` < 4)) | {} | +------------------------------------------------+----------------------------------------- ---------------------------------------------------+--------+ 2 rows in set (0.00 sec)
```

The equivalence condition is executed faster than the range condition. Examples:

```
mysql> SELECT * FROM test WHERE c1 = 2; +----+----+
| c1 | c2 |
+----+----+
|  2 |  2 |
+----+----+ 1 row in set (0.03 sec)
```

The corresponding execution plan is as follows:

```
mysql> EXPLAIN SELECT * FROM test WHERE c1 = 2; +------------------------------------------------+----------------------------------------- ---------------------------+--------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ---------------------------+--------+
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0002_RDS | select `test`.`c1`,`test`.`c2` from `tes
t` where (`test`.`c1` = 2) | {} | +------------------------------------------------+----------------------------------------- ---------------------------+--------+ 1 row in set (0.00 sec)
```

In addition, if you want to insert data into a table shard, the inserted field must contain a shard key. For example, the data inserted into the test table contains the shard key c1:

```
mysql> INSERT INTO test(c1,c2) VALUES(8,8); Query OK, 1 row affected (0.07 sec)
```

Optimization of the number of returned rows for a query When PolarDB-X 1.0 runs a query that contains LIMIT [ offset,] row_count, PolarDB-X actually reads records before offset in order and directly discards them. In this way, when the value of offset is large, the query is slow even if the value of row_count is small. For example, run the following SQL statement:

```
SELECT * FROM sample_order ORDER BY sample_order.id LIMIT 10000, 2
```

Although only the 10000th and 10001st records are returned, it takes about 12 seconds to run the SQL statement because PolarDB-X 1.0 actually reads 10,002 records.

```
mysql> SELECT * FROM sample_order ORDER BY sample_order.id LIMIT 10000,2; +--------------+------------+--------------+--------------+------------+
| id           | sellerId   | trade_id     | buyer_id     | buyer_nick |
+--------------+------------+--------------+--------------+------------+
| 242012755468 | 1711939506 | 242012755467 | 244148116334 | zhangsan   |
| 242012759093 | 1711939506 | 242012759092 | 244148138304 | wangwu     |
+--------------+------------+--------------+--------------+------------+ 2 rows in set (11.93 sec)
```

The corresponding execution plan is as follows:

```
mysql> EXPLAIN SELECT * FROM sample_order ORDER BY sample_order.id LIMIT 10000,2; +------------------+-------------+------------+
| GROUP_NAME       | SQL         | PARAMS     |
+------------------+-------------+------------+
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0004_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0007_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0005_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0002_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0003_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0006_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0000_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0001_RDS | select `sample_order`.`id`,`sample_order
`.`sellerId`,`sample_order`.`trade_id`,`sample_order`.`buyer_id`,`sample_order`.`buyer_nick ` from `sample_order` order by `sample_order`.`id` asc limit 0,10002 | {} | +-------------------+---------------------------+--------+ 8 rows in set (0.01 sec)
```

To optimize the preceding SQL statement, find the ID set, and use IN to match the actual records. The modified SQL query is as follows:

```
SELECT * FROM sample_order o WHERE o.id IN (
      SELECT id
      FROM sample_order
      ORDER BY id
      LIMIT 10000, 2 )
```

The purpose is to cache IDs in the memory first (on the premise that the number of IDs is small). If the shard key of the sample_order table is an ID, PolarDB-X 1.0 can also push down such an IN query to different database shards through rule-based calculation, avoiding full table scan and unnecessary network I/O operations. Observe the effect of the modified SQL query:

```
mysql> SELECT *
    -> FROM sample_order o
    -> WHERE o.id IN ( SELECT id FROM sample_order ORDER BY id LIMIT 10000,2 );
+--------------+------------+--------------+--------------+------------+
| id           | sellerId   | trade_id     | buyer_id     | buyer_nick |
+--------------+------------+--------------+--------------+------------+
| 242012755468 | 1711939506 | 242012755467 | 244148116334 | zhangsan   |
| 242012759093 | 1711939506 | 242012759092 | 244148138304 | wangwu     |
+--------------+------------+--------------+--------------+------------+ 2 rows in set (1.08 sec)
```

The execution time is significantly reduced from 12 seconds to 1.08 seconds. The corresponding execution plan is as follows:

```
mysql> EXPLAIN SELECT *
    -> FROM sample_order o
    -> WHERE o.id IN ( SELECT id FROM sample_order ORDER BY id LIMIT 10000,2 );
+------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------+ --------+
| GROUP_NAME                                     | SQL
| PARAMS |
+------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------+ --------+
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0002_RDS | select `o`.`id`,`o`.`sellerId`,`o`.`trad
e_id`,`o`.`buyer_id`,`o`.`buyer_nick` from `sample_order` `o` where (`o`.`id` IN (10002)) | {} |
| SEQPERF_1478746391548CDTCSEQPERF_OXGJ_0001_RDS | select `o`.`id`,`o`.`sellerId`,`o`.`trad
e_id`,`o`.`buyer_id`,`o`.`buyer_nick` from `sample_order` `o` where (`o`.`id` IN (10001)) | {} | +------------------------------------------------+----------------------------------------- ------------------------------------------------------------------------------------------+ --------+ 2 rows in set (0.03 sec)
```

Grouping and sorting optimization In PolarDB-X 1.0, if an SQL query must use all of DISTINCT, GROUP BY, and ORDER BY, try to ensure that the fields after DISTINCT, GROUP BY, and ORDER BY are the same and the fields are shard keys. In this way, only a small amount of data is returned for the SQL query. This minimizes the network bandwidth consumed by distributed queries and removes the need to retrieve a large amount of data and sort the data in a temporary table, thereby maximizing the system performance.

#### 14.4.3 JOIN query optimization

JOIN queries in PolarDB-X 1.0 are classified into push-down JOIN queries and non-push-down JOIN queries (distributed JOIN queries). The optimization policies for these two types of JOIN queries are different. Optimize push-down JOIN queries Push-down JOIN queries are classified into the following types: JOIN queries between single tables (non-partition tables). The tables involved in the JOIN query contain the shard key in the filter condition and use the same sharding algorithm (that is, the data calculated by the sharding algorithm is distributed to the same shard). Tables involved in the JOIN query use the shard key as the JOIN condition and use the same sharding algorithm. JOIN query between broadcast tables (or small table broadcast) and table shards. In PolarDB-X 1.0, optimize JOIN queries to push-down JOIN queries that can be executed on database shards. Take a JOIN query between a broadcast table and table shards as an example. The broadcast table is used as the JOIN driving table (the left table in the JOIN query is called the driving table). The PolarDB-X 1.0 broadcast table stores the same data in each database shard. When the broadcast table is used as the JOIN driving table, the JOIN query between this broadcast table and table shards can be converted into single-database JOIN queries and combined for computing to improve query performance. For example, a JOIN query is performed on the following three tables, among which the sample_area table is the broadcast table, and the sample_item and sample_buyer tables are table shards. The query execution time is about 15s:

```
mysql> SELECT sample_area.name
    -> FROM sample_item i JOIN sample_buyer b ON i.sellerId = b.sellerId JOIN sample_area a
ON b.province = a.id
    -> WHERE a.id < 110107
    -> LIMIT 0, 10;
+------+
| name |
+------+
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
+------+ 10 rows in set (14.88 sec)
```

If you adjust the JOIN query order and move the broadcast table to the farthest left as the JOIN driving table, the JOIN query is pushed down to a single database shard in the PolarDB-X 1.0 instance:

```
mysql> SELECT sample_area.name
    -> FROM sample_area a JOIN sample_buyer b ON b.province = a.id JOIN sample_item i ON i.
sellerId = b.sellerId
    -> WHERE a.id < 110107
    -> LIMIT 0, 10;
+------+
| name |
+------+
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
|  BJ  |
+------+ 10 rows in set (0.04 sec)
```

The query execution time decreases from 15 seconds to 0.04 seconds, which is a significant improvement to the query performance.

> Not ice The broadcast table achieves data consistency through the synchronization mechanism on database shards, with a latency of several seconds.

Optimize distributed JOIN queries If a JOIN query cannot be pushed down (that is, the JOIN condition and filter condition do not contain the shard key), PolarDB-X 1.0 must complete part of the computing in the query. Such a query is a distributed JOIN query. Tables in a distributed JOIN query are classified into two types based on the data size: Small table: A table that contains a small amount of data (less than 100 data records or less data than other tables) that is involved in JOIN computing after filtering. Large table: A table that contains a large amount of data (more than 100 data records or more data than other tables) that is involved in JOIN computing after filtering. In most cases, Nested Loop and its derived algorithms are used in JOIN computing at the PolarDB-X 1.0 layer. If sorting is required for JOIN queries, the Sort Merge algorithm is used. When the Nested Loop algorithm is used, a smaller data size in the left table in a JOIN query indicates a smaller number of queries performed by PolarDB-X 1.0 on the right table. If the right table has indexes or contains a small amount of data, the JOIN query is even faster. In PolarDB-X 1.0, the left table of a distributed JOIN query is called the driving table. To optimize a distributed JOIN query, use a small table as the driving table and set as many filter conditions as possible for the driving table. Take the following distributed JOIN query as an example. The query takes about 24 seconds:

```
mysql> SELECT t.title, t.price
    -> FROM sample_order o,
    ->      ( SELECT * FROM sample_item i WHERE i.id = 242002396687 ) t
    -> WHERE t.source_id = o.source_item_id AND o.sellerId < 1733635660;
+----------------------------------+--------+
| title                            | price  |
+----------------------------------|--------+
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
+----------------------------------+--------+ 10 rows in set (23.79 sec)
```

The preceding JOIN query is an INNER JOIN query, with the actual size of the intermediate data involved in JOIN computing unknown. In this case, perform COUNT() on the o table and t table respectively to obtain the actual data size. For the o table, o.sellerId < 1733635660 in the WHERE condition is only related to the o table. Then, extract and add it to the COUNT() condition of the o table. The following query result is returned:

```
mysql> SELECT COUNT(*) FROM sample_order o WHERE o.sellerId < 1733635660; +----------+
| count(*) |
+----------+
|   504018 |
+----------+ 1 row in set (0.10 sec)
```

The intermediate result of the o table contains about 500,000 records. Similarly, the t table is a subquery, which can be extracted directly for the COUNT() query:

```
mysql> SELECT COUNT(*) FROM sample_item i WHERE i.id = 242002396687; +----------+
| count(*) |
+----------+
|        1 |
+----------+ 1 row in set (0.01 sec)
```

The intermediate result of the t table contains only one record. Therefore, the o table is a large table and the t table is a small table. Use the small table as the driving table of the distributed JOIN query. The result of the adjusted JOIN query is as follows:

```
mysql> SELECT t.title, t.price
    -> FROM ( SELECT * FROM sample_item i WHERE i.id = 242002396687 ) t,
    ->      sample_order o
    -> WHERE  t.source_id = o.source_item_id AND o.sellerId < 1733635660;
+----------------------------------+--------+
| title                            | price  |
+----------------------------------|--------+
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
| Sample Item for Distributed JOIN | 239.00 |
+----------------------------------+--------+ 10 rows in set (0.15 sec)
```

The query execution time decreases from about 24 seconds to 0.15 seconds, with the query performance significantly improved.

#### 14.4.4 Subquery optimization

When optimizing an SQL statement that contains subqueries, push the subqueries down to database shards as much as possible to reduce the computing workload at the PolarDB-X 1.0 layer. For this purpose, you can try two optimization methods: Rewrite subqueries into multi-table JOIN queries, and optimize the JOIN queries. Use the shard key in the JOIN condition or filter condition so that PolarDB-X 1.0 can push the query down to a specific database shard to avoid full table scan. The following subquery is used as an example:

```
SELECT o. * FROM sample_order o WHERE NOT EXISTS
     (SELECT sellerId FROM sample_seller s WHERE o.sellerId = s.id)
```

Rewrite the subquery into a JOIN query:

```
SELECT o. * FROM sample_order o LEFT JOIN sample_seller s ON o.sellerId = s.id WHERE s.id IS NULL
```

### 14.5 Select connection pools for an application

application A database connection pool is used to manage database connections in a centralized manner, so as to improve application performance and reduce database loads. Reuse resources: Connections can be reused to avoid high performance overheads caused by frequent connection creation and release. Resource reuse can also improve the system stability. Improve t he syst em response ef f iciency: After the connection initialization is complete, all requests can directly use the existing connections, which avoids the overheads of connection initialization and release and improves the system response efficiency. Avoid connect ion leakage: The connection pool forcibly revokes connections based on the preset de-allocation policy to avoid connection resource leakage. We recommend that you use a connection pool to connect applications and databases for service operations. For Java programs, we recommend that you use the Druid connection pool. The following is an example of standard Druid Spring configuration:

```
    <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource" init-method="init"
destroy-method="close">
        <property name="driverClassName" value="com.mysql.jdbc.Driver" />
        <! -- Basic attributes URL, user, and password -->
        <property name="url" value="jdbc:mysql://ip:port/db? autoReconnect=true&amp;rewrite
BatchedStatements=true&amp;socketTimeout=30000&amp;connectTimeout=3000" />
        <property name="username" value="root" />
        <property name="password" value="123456" />
        <! -- Configure the initial size, minimum value, and maximum value -->
        <property name="maxActive" value="20" />
        <property name="initialSize" value="3" />
        <property name="minIdle" value="3" />
        <! -- maxWait indicates the time-out period for obtaining the connection -->
        <property name="maxWait" value="60000" />
        <! -- timeBetweenEvictionRunsMillis indicates the interval for detecting idle conne
ctions to be closed, in milliseconds -->
        <property name="timeBetweenEvictionRunsMillis" value="60000" />
        <! -- minEvictableIdleTimeMillis indicates the minimum idle time of a connection in
the connection pool, in milliseconds-->
        <property name="minEvictableIdleTimeMillis" value="300000" />
        <! -- SQL statement used to check whether connections are available -->
        <property name="validationQuery" value="SELECT 'z'" />
        <! -- Whether to enable idle connection check -->
        <property name="testWhileIdle" value="true" />
        <! -- Whether to check the connection status before obtaining a connection -->
        <property name="testOnBorrow" value="false" />
        <! -- Whether to check the connection status before releasing a connection -->
        <property name="testOnReturn" value="false" />
    </bean>
```

### 14.6 Connections to PolarDB-X instances

instances When an application connects to a PolarDB-X 1.0 instance for operation, there are two types of connections from the perspective of the PolarDB-X 1.0 instance: Frontend connection: a connection established by an application to the logical database in the PolarDB-X 1.0 instance. Backend connection: a connection established by a node in a PolarDB-X 1.0 instance to a physical database in a backend ApsaraDB RDS for MySQL instance. PolarDB-X 1.0 instance connection diagram Frontend connection Theoretically, the number of frontend connections is limited by the available memory size and the number of network connections to the nodes of the PolarDB-X 1.0 instance. However, in actual application scenarios, when an application connects to a PolarDB-X 1.0 instance, the nodes of the PolarDB-X instance usually manage a limited number of connections to perform requested operations, and do not maintain a large number of concurrent persistent connections (for example, tens of thousands of concurrent persistent connections). Therefore, the number of frontend connections that a PolarDB-X 1.0 instance can accept can be considered to be unlimited. Considering that the number of frontend connections is unlimited and a large number of idle connections are allowed, this method applies to scenarios where a large number of servers are deployed and need to maintain their connections to the PolarDB-X 1.0 instance.

> Not e Although the number of frontend connections is considered as unlimited, operation requests obtained from frontend connections are actually executed by internal threads of the PolarDB-X 1.0 instance through backend connections. Due to the limited number of internal threads and backend connections, the total number of concurrent requests that can be processed by the PolarDB-X 1.0 instance is limited.

Backend connection Each node of a PolarDB-X 1.0 instance creates a backend connection pool to automatically manage and maintain the backend connections to the physical databases in the ApsaraDB RDS for MySQL instance. Therefore, the maximum number of connections in the backend connection pool of a PolarDB- X 1.0 instance is directly related to the maximum number of connections supported by the ApsaraDB RDS for MySQL instance. You can use the following formula to calculate the maximum number of connections in the backend connection pool of a PolarDB-X 1.0 instance:

```
Maximum number of connections in a backend connection pool of a PolarDB-X 1.0 instance = FL OOR (Maximum number of connections in an ApsaraDB RDS for MySQL instance/Number of physical database shards in the ApsaraDB RDS for MySQL instance/Number of nodes on the PolarDB-X 1.0 instance)
```

For example, a user has purchased an ApsaraDB RDS for MySQL instance and a PolarDB-X 1.0 instance of the following types: The ApsaraDB RDS for MySQL instance has eight physical database shards, four cores, and 16 GB memory, supporting a maximum number of 4,000 connections. The PolarDB-X 1.0 dedicated instance has 32 cores and 32 GB memory, with each PolarDB-X 1.0 node having two cores and 2 GB memory (that is, the instance has 16 PolarDB-X 1.0 nodes). You can use the following formula to calculate the maximum number of connections in the backend connection pool of the PolarDB-X 1.0 instance:

```
Maximum number of connections in the backend connection pool of the PolarDB-X 1.0 instance = FLOOR (4000/8/16) = FLOOR (31.25) = 31
```

> Not e

The calculation result of the preceding formula is the maximum number of connections in the backend connection pool of the PolarDB-X 1.0 instance. In actual use, to reduce the connection pressure on the ApsaraDB RDS for MySQL instance, the PolarDB-X 1.0 instance adjusts the maximum number of connections in the backend connection pool to make it smaller than the upper limit. We recommend that you create databases in a PolarDB-X 1.0 instance on a dedicated ApsaraDB RDS for MySQL instance. Do not create databases for other applications or PolarDB-X 1.0 instances on the dedicated ApsaraDB RDS for MySQL instance. Relationship between frontend and backend connections After an application establishes frontend connections to a PolarDB-X 1.0 instance and sends SQL statement execution requests, the PolarDB-X 1.0 nodes process the requests asynchronously and obtain backend connections through the internal backend connection pool, and then run optimized SQL statements on one or more physical databases. PolarDB-X 1.0 nodes process requests asynchronously and frontend connections are not bound to backend connections. Therefore, a small number of backend connections can process a large number of requests for short transactions and simple queries from many concurrent frontend connections. This is why you need to focus on the queries per second (QPS) in PolarDB-X 1.0, rather than the number of concurrent connections. Although the number of frontend connections is considered to be unlimited, the maximum number of connections maintained in the backend connection pool of a PolarDB-X 1.0 instance is limited. For more information, see "Backend connections." Therefore, note the following points in actual application scenarios: Avoid long or large transactions in applications. These transactions occupy many or even all backend connections when they are not committed or rolled back for a long time, which reduces the overall concurrent processing capability and increases the response time (RT). Monitor and optimize or remove slow SQL queries run in the PolarDB-X 1.0 instance, to prevent them from occupying too many backend connections. Otherwise, the PolarDB-X 1.0 instance or the ApsaraDB RDS for MySQL instance is under greater processing pressure, which may lead to reduced concurrent processing capability, increased RT, or higher SQL execution failure rate due to execution timeout. For troubleshooting and optimization of slow SQL queries, see Troubleshoot slow SQL statements in PolarDB-X and Overview. Under normal use of connections and execution of queries, if the maximum number of connections in the backend connection pool of the PolarDB-X 1.0 instance is reached, contact Customer Services for assistance.

### 14.7 Perform instance upgrade

Database performance can be measured by the response time (RT) and queries per second (QPS). RT reflects the performance of a single SQL statement. This type of performance problem can be solved through SQL optimization. PolarDB-X 1.0 upgrade expands the capacity to improve performance, and is suitable for database access services with low latency and high QPS. The performance of a PolarDB-X 1.0 instance depends on the performance of PolarDB-X 1.0 and ApsaraDB RDS for MySQL. Insufficient performance of any PolarDB-X 1.0 or ApsaraDB RDS for MySQL node can create a bottleneck in the overall performance. This topic describes how to observe the performance metrics of a PolarDB-X 1.0 instance and upgrade the PolarDB-X instance to solve the performance bottleneck. For more information about how to determine the performance of an ApsaraDB RDS for MySQL instance and upgrade the ApsaraDB RDS for MySQL instance, see the ApsaraDB RDS for MySQL documentation. Determine the performance bottleneck of a PolarDB-X 1.0 instance The QPS and CPU performance of a PolarDB-X 1.0 instance are in positive correlation. When a PolarDB-X 1.0 instance encounters a performance bottleneck, the CPU utilization of the PolarDB-X instance remains high. Observe t he CPU ut ilizat ion
1. On the Basic Inf ormat ion page of the PolarDB-X instance, choose Monit oring and Alert s >
Inst ance Monit oring from the left-side navigation pane.
2. On the Instance Monitoring page, select a monitoring dimension and the corresponding metrics to
view details. If the CPU utilization exceeds 90% or remains above 80%, the PolarDB-X instance faces a performance bottleneck. If there is no bottleneck for the ApsaraDB RDS for MySQL instance, the current PolarDB-X 1.0 instance specifications cannot meet the QPS performance requirements of the business. In this case, the PolarDB-X instance needs to be upgraded. For more performance-related service monitoring scenarios and methods for configuring the PolarDB-X 1.0 CPU utilization alert. Upgrade PolarDB-X 1.0 QPS is an important metric for determining whether the PolarDB-X 1.0 instance specifications can meet the business requirements. Each type of instance specifications corresponds to a reference QPS value. Some special SQL statements require more computing (such as temporary table sorting and aggregate computing) in PolarDB-X 1.0. In this case, the QPS supported by each PolarDB-X 1.0 instance is lower than the standard value in its type. PolarDB-X 1.0 upgrade improves the processing performance of a PolarDB-X instance by adding nodes to share the QPS. As PolarDB-X 1.0 nodes are stateless, this upgrade method linearly improves the performance of PolarDB-X 1.0 instances. For example, service A requires QPS of about 15 thousand. The current PolarDB-X 1.0 instance has a 4core virtual CPU (vCPU), 4 GB memory, and two nodes, supporting QPS of only 10 thousand. After finding that the CPU utilization of the PolarDB-X 1.0 instance remains high, we upgraded the instance to 8-core vCPU and 8 GB memory, with each node handling about 4,000 QPS. Then, the performance meets service requirements, and the CPU utilization also drops to a reasonable level, as shown in the following figure. PolarDB-X 1.0 upgrade For more information about how to upgrade a PolarDB-X instance, see Change specifications.

### 14.8 Perform scale-out

In PolarDB-X 1.0, smooth scale-out improves the overall performance by increasing the number of ApsaraDB RDS for MySQL instances. You can increase the number of ApsaraDB RDS for MySQL instances through PolarDB-X 1.0 smooth scale-out to increase the PolarDB-X 1.0 database capacity when the following conditions are met: 1. The input/output operations per second (IOPS), CPU utilization, disk space, and other metrics of the ApsaraDB RDS for MySQL instance reach their bottlenecks. 2. The bottlenecks cannot be removed through SQL optimization or ApsaraDB RDS for MySQL upgrade (for example, the disk has been upgraded to the top configuration). PolarDB-X 1.0 smooth scale-out reduces the pressure on the original ApsaraDB RDS for MySQL instance by migrating database shards to the new ApsaraDB RDS for MySQL instance. For example, before scaleout, all the eight databases are deployed in one ApsaraDB RDS for MySQL instance. After scale-out, the eight databases are deployed in two ApsaraDB RDS for MySQL instances, and the pressure on a single ApsaraDB RDS for MySQL instance is significantly reduced, as shown in the following figure. PolarDB-X 1.0 scale-out After multiple scale-out operations, if the number of ApsaraDB RDS for MySQL instances is equal to the number of database shards, you need to create another PolarDB-X 1.0 instance and ApsaraDB RDS for MySQL databases with the expected capacity, and then migrate data to further increase the data capacity. This process is complex. We recommend that you consider the data growth expected in the next two to three years and plan the number of ApsaraDB RDS for MySQL instances properly when creating a PolarDB-X 1.0 database. Determine whether scale-out is required You can determine whether PolarDB-X 1.0 smooth scale-out is required based on three ApsaraDB RDS for MySQL metrics: IOPS, CPU utilization, and disk space. You can view these metrics in the ApsaraDB RDS for MySQL console. For more information, see the ApsaraDB RDS for MySQL documentation. IOPS and CPU utilization If you find that the IOPS or CPU utilization remains above 80% for a long time or you frequently receive alerts, follow these steps:
1. Optimize SQL statements. Generally, you can solve the high CPU utilization problem by this method.
2. If the problem persists, upgrade the ApsaraDB RDS for MySQL instance. For more information, see
the ApsaraDB RDS for MySQL documentation.
3. When the CPU utilization or IOPS exceeds the threshold, you can set read-only databases to share
the load on the primary database. However, read/write splitting affects read consistency. For more information, see the Read/write splitting documentation.
4. If the problem persists, scale out the PolarDB-X 1.0 instance.
Disk space ApsaraDB RDS for MySQL has the following types of disk space:
1. Data space: the space occupied by data. The space usage continues increasing as more data is
inserted. We recommend that you keep the remaining disk space above 30%.
2. System file space: the space occupied by shared tables and error log files.
3. Binary log file space: the space occupied by binary logs generated during database operation. The
more update transactions there are, the larger the occupied space is. Whether scale-out is required depends on the data space. When the data space is about to or expected to exceed the disk capacity, you can distribute the data to the databases on multiple ApsaraDB RDS for MySQL instances through scale-out. Scale-out risks and precautions PolarDB-X 1.0 scale-out consists of four steps: conf igurat ion > migrat ion > swit chover > cleanup. For more information, see the Perform smooth scale-out documentation. Note the following points before scale-out: To reduce the pressure of read operations on the source ApsaraDB RDS for MySQL instance, perform scale-out when the load on the source ApsaraDB RDS for MySQL instance is low. During scale-out, do not submit data definition language (DDL) tasks in the console or connect to the PolarDB-X 1.0 instance to directly run DDL SQL statements. Otherwise, the scale-out task may fail. Scale-out requires that the source database table have a primary key. If the source database does not have a primary key, add one first. During scale-out, the read and write traffic is switched to the new ApsaraDB RDS for MySQL instance. The switchover process takes three to five minutes. We recommend that you perform a switchover during off-peak hours. Scale-out does not affect the PolarDB-X 1.0 instance before the switchover. Therefore, you can cancel the scale-out through rollback before the switchover. Scale-out creates pressure on databases. We recommend that you perform this operation during off-peak hours.

### 14.9 Troubleshoot slow SQL statements in PolarDB-X

statements in PolarDB-X

#### 14.9.1 Details about a low SQL statement

PolarDB-X 1.0 defines an SQL statement that takes more than 1 second to run as a slow SQL statement. Slow SQL statements in PolarDB-X 1.0 are classified into slow logical SQL statements and slow physical SQL statements. In PolarDB-X 1.0, an SQL statement is run step by step on PolarDB-X 1.0 and ApsaraDB RDS for MySQL nodes. Large execution loss on any node will result in slow SQL statements. Slow logical SQL statements are slow SQL statements sent by an application to PolarDB-X 1.0. Slow physical SQL statements are slow SQL statements sent by PolarDB-X 1.0 to ApsaraDB RDS for MySQL. Syntax

```
SHOW FULL {SLOW | PHYSICAL_SLOW} [WHERE where_condition]
                                 [ORDER BY col_name [ASC | DESC], ...]
                                 [LIMIT {[offset,] row_count | row_count OFFSET offset}]
```

Description The `SHOW FULL SLOW` command shows slow logical SQL statements, that is, SQL statements sent by an application to PolarDB-X 1.0. The result set of the `SHOW FULL SLOW` command contains the following columns: TRACE_ID: the unique identifier of the SQL statement. A logical SQL statement and the physical SQL statements generated by the logical SQL statement have the same TRACE_ID. The TRACE_ID is also sent as a comment to ApsaraDB RDS for MySQL. HOST: the IP address of the client that sends the SQL statement.

> Not ice The client IP address may not be obtained when the network type is Virtual Private Cloud (VPC).

START_TIME: the time when PolarDB-X 1.0 starts running the SQL statement. EXECUTE_TIME: the time consumed by PolarDB-X 1.0 to run the SQL statement. AFFECT_ROW: the number of records returned or the number of rows affected by the SQL statement. SQL: the statement that is run. The `SHOW FULL PHYSICAL_SLOW` command shows the slow physical SQL statements, that is, SQL statements sent by PolarDB-X 1.0 to ApsaraDB RDS for MySQL. The result set of `SHOW FULL PHYSICAL_SLOW` contains the following columns: TRACE_ID: the unique identifier of the SQL statement. A logical SQL statement and the physical SQL statements generated by the logical SQL statement have the same TRACE_ID. The TRACE_ID is also sent as a comment to ApsaraDB RDS for MySQL. GROUP_NAME: the name of a database group. Grouping aims to manage multiple groups of databases with identical data, such as the primary and secondary databases after data replication through ApsaraDB RDS for MySQL, which are mainly used for read/write splitting and primary/secondary switchover. DBKEY_NAME: the name of the database shard on which the SQL statement is run. START_TIME: the time when PolarDB-X 1.0 starts running the SQL statement. EXECUTE_TIME: the time consumed by PolarDB-X 1.0 to run the SQL statement. SQL_EXECUTE_TIME: the time consumed by PolarDB-X 1.0 to call ApsaraDB RDS for MySQL to run this SQL statement. GETLOCK_CONNECTION_TIME: the time that PolarDB-X 1.0 takes to get connections from the connection pool. If the value is large, the ApsaraDB RDS for MySQL connections have been exhausted. This is typically due to a large number of slow SQL statements. You can log on to the corresponding ApsaraDB RDS for MySQL instance and run SHOW PROCESSLIST for troubleshooting. CREATE_CONNECTION_TIME: the time consumed by PolarDB-X 1.0 to establish a connection to ApsaraDB RDS for MySQL. If the value is large, it is largely because the ApsaraDB RDS for MySQL instance is overloaded or faulty. AFFECT_ROW: the number of records returned or the number of rows affected by the SQL statement. SQL: the statement that is run. Example 1 The following example describes how to locate the execution of a slow SQL statement on PolarDB-X 1.0 and between PolarDB-X 1.0 and ApsaraDB RDS for MySQL.
1. You can use certain conditions, such as the execution time and SQL string match, to obtain the
specified slow SQL statement:

```
mysql> show full slow where `SQL` like '%select sleep(50)%'; +-----------------+-----------+-------------------------+--------------+------------+-- ----------------+
| TRACE_ID        | HOST      | START_TIME              | EXECUTE_TIME | AFFECT_ROW | S
QL | +-----------------+-----------+-------------------------+--------------+------------+-- ----------------+
| ae0e565b8c00000 | 127.0.0.1 | 2017-03-29 19:28:43.028 |        50009 |          1 | s
elect sleep(50) | +-----------------+-----------+-------------------------+--------------+------------+-- ----------------+ 1 row in set (0.02 sec)
```

2. Based on the TRACE_ID of the slow logical SQL statement, run `SHOW FULL PHYSICAL_SLOW` to
obtain the physical execution information of this SQL statement.

```
mysql> show full physical_slow where trace_id = 'ae0e565b8c00000'; +-----------------+----------------------------------------------------+--------------- --------------------------------+------------------------+--------------+-------------- ----+-------------------------+------------------------+------------+------------------
```

`+`

```
| TRACE_ID        | GROUP_NAME                                         | DBKEY_NAME
| START_TIME             | EXECUTE_TIME | SQL_EXECUTE_TIME | GETLOCK_CONNECTION_TIME |
CREATE_CONNECTION_TIME | AFFECT_ROW | SQL | +-----------------+----------------------------------------------------+--------------- --------------------------------+------------------------+--------------+-------------- ----+-------------------------+------------------------+------------+------------------
```

`+`

```
| ae0e565b8c00000 | PRIV_TEST_1489167306631PJAFPRIV_TEST_APKK_0000_RDS | rdso6g5b6206sd
q832ow_priv_test_apkk_0000_nfup | 2017-03-29 19:27:53.02 | 50001 | 50 001 | 0 | 0 | 1 | select sleep(50)
```

|

```
+-----------------+----------------------------------------------------+--------------- --------------------------------+------------------------+--------------+-------------- ----+-------------------------+------------------------+------------+------------------
```

`+`

```
1 row in set (0.01 sec)
```

3. In the SQL statement details and slow SQL statement records of the ApsaraDB RDS for MySQL
instance, you can query the execution information of this SQL statement on the ApsaraDB RDS for MySQL instance based on TRACE_ID. Slow query logs Example 2 This example describes how to locate the original SQL statement in PolarDB-X 1.0 based on the slow SQL statement located in ApsaraDB RDS for MySQL.
1. Based on the slow SQL query log in ApsaraDB RDS for MySQL, TRACE_ID of the slow SQL statement
is ae0e55660c00000.
2. Based on the TRACE_ID obtained in Step 1, run `SHOW FULL PHYSICAL_SLOW` to obtain the physical
execution information of this SQL statement.

```
mysql> show full physical_slow where trace_id = 'ae0e55660c00000'; +-----------------+----------------------------------------------------+--------------- --------------------------------+-------------------------+--------------+------------- -----+-------------------------+------------------------+------------+-----------------
```

`-+`

```
| TRACE_ID        | GROUP_NAME                                         | DBKEY_NAME
| START_TIME              | EXECUTE_TIME | SQL_EXECUTE_TIME | GETLOCK_CONNECTION_TIME |
CREATE_CONNECTION_TIME | AFFECT_ROW | SQL | +-----------------+----------------------------------------------------+--------------- --------------------------------+-------------------------+--------------+------------- -----+-------------------------+------------------------+------------+-----------------
```

`-+`

```
| ae0e55660c00000 | PRIV_TEST_1489167306631PJAFPRIV_TEST_APKK_0000_RDS | rdso6g5b6206sd
q832ow_priv_test_apkk_0000_nfup | 2017-03-29 19:27:37.308 | 10003 | 1 0001 | 0 | 0 | 1 | select sleep(10)
```

|

```
+-----------------+----------------------------------------------------+--------------- --------------------------------+-------------------------+--------------+------------- -----+-------------------------+------------------------+------------+-----------------
```

`-+`

```
1 row in set (0.02 sec)
```

#### 14.9.2 Locate slow SQL statements

Generally, you can locate a slow SQL statement in two ways: Obtain historical information about slow SQL statements from slow SQL statement records, or run `SHOW PROCESSLIST` to display the real-time execution information about slow SQL statements. You can troubleshoot slow SQL statements as follows:
1. Locate slow SQL statements.
2. Locate nodes with performance loss.
3. Troubleshoot the performance loss.

|   | Not e During troubleshooting, we recommend that you use the MySQL command line mysql -hIP -PPORT -uUSER -pPASSWORD -c to create the connection. Be sure to add -c to prevent the MySQL client from filtering out the comments (default operation) and therefore affecting the execution of HINT. |
|---|---|
|   | -hIP -PPORT -uUSER -pPASSWORD -c |

View slow SQL statement records Run the following command to query top 10 slow SQL statements. This command can query logical SQL statements in PolarDB-X 1.0. One logical SQL statement corresponds to SQL statements of one or more databases or tables of the ApsaraDB RDS for MySQL instance. For more information, see Details about a low SQL statement.

```
mysql> SHOW SLOW limit 10; +-----------------+--------------+-------------------------+--------------+------------+- ----------------------------------------------------------------+
| TRACE_ID        | HOST         | START_TIME              | EXECUTE_TIME | AFFECT_ROW |
SQL | +-----------------+--------------+-------------------------+--------------+------------+- ----------------------------------------------------------------+
| ac3133132801001 | xx.xxx.xx.97 | 2017-03-06 15:48:32.330 |       900392 |         -1 |
select detail_url, sum(price) from t_item group by detail_url; | ...... +-----------------+--------------+-------------------------+--------------+------------+- ----------------------------------------------------------------+ 10 rows in set (0.01 sec)
```

View real-time SQL execution information If the execution of an SQL statement is slow in the current server, run SHOW PROCESSLIST to view the real-time SQL execution information in the current PolarDB-X 1.0 database. The value in the TIME column indicates how long the current SQL statement has been run.

```
mysql> SHOW PROCESSLIST WHERE COMMAND ! = 'Sleep'; +---------------+-----------+--------------------+-------------+---------+--------------- --------------------------------------------------------+-------------------------------- ----------------------------------------------------------------------+-----------+------ ---------+-----------+
| ID            | USER      | DB                 | COMMAND     | TIME    | STATE
| INFO
| ROWS_SENT | ROWS_EXAMINED | ROWS_READ |
+---------------+-----------+--------------------+-------------+---------+--------------- --------------------------------------------------------+-------------------------------- ----------------------------------------------------------------------+-----------+------ ---------+-----------+
| 0-0-352724126 | ifisibhk0 | test_123_wvvp_0000 | Query       |     13  | Sending data
| /*DRDS /42.120.74.88/ac47e5a72801000/ */select `t_item`.`detail_url`,SUM(`t_item`.`pric
e`) from `t_i | NULL | NULL | NULL |
| 0-0-352864311 | cowxhthg0 | NULL               | Binlog Dump |     17  | Master has sen
t all binlog to slave; waiting for binlog to be updated | NULL
|      NULL |          NULL |      NULL |
| 0-0-402714795 | ifisibhk0 | test_123_wvvp_0005 | Alter       |     114 | Sending data
| /*DRDS /42.120.74.88/ac47e5a72801000/ */ALTER TABLE `Persons` ADD `Birthday` date
|      NULL |          NULL |      NULL |
...... +---------------+-----------+--------------------+-------------+---------+--------------- --------------------------------------------------------+-------------------------------- ----------------------------------------------------------------------+-----------+------ ---------+-----------+ 12 rows in set (0.03 sec)
```

The following describes each column: ID: the ID of the connection. USER: the user name of the database shard in which this SQL statement is run. DB: the specified database. If no database is specified, the value is NULL. COMMAND: the type of the command being executed. SLEEP indicates an idle connection. For more information about other commands, see MySQL thread information documentation. TIME: the elapsed execution time of the SQL statement, in seconds. STATE: the current execution status. For more information, see MySQL thread status documentation. INFO: the SQL statement being executed. The SQL statement may be too long to be displayed completely. You can derive the complete SQL statement based on information such as service parameters. In the current example, the following slow SQL statement is identified:

```
ALTER TABLE `Persons` ADD `Birthday` date
```

#### 14.9.3 Locate nodes with performance loss

When you locate a slow SQL statement in slow SQL statement records or real-time SQL execution information, you can run the TRACE command to trace the running time of the SQL statement in PolarDB-X 1.0 and ApsaraDB RDS for MySQL to locate the bottleneck. The TRACE command actually runs the SQL statement, records the time consumed on all nodes, and returns the execution result. For more information about TRACE and other control commands, see Help statements.

> Not e The PolarDB-X 1.0 TRACE command needs to maintain the context information of the connection. Some GUI clients may use connection pools, which results in command exceptions. Therefore, we recommend that you use the MySQL command line to run the TRACE command.

Run the following command for the identified slow SQL statement:

```
mysql> trace select detail_url, sum(distinct price) from t_item group by detail_url;
    +---------------+---------------+
    | detail_url    | sum(price)    |
    +---------------+---------------+
    | www.xxx.com   | 1084326800.00 |
    | www.xx1.com   | 1084326800.00 |
    | www.xx2.com   | 1084326800.00 |
    | www.xx3.com   | 1084326800.00 |
    | www.xx4.com   | 1084326800.00 |
    | www.xx5.com   | 1084326800.00 |
    ......
    +---------------+---------------+
    1 row in set (7 min 2.72 sec)
```

After the TRACE command is run, run SHOW TRACE to view the result. You can identify the bottleneck of the slow SQL statement based on the time consumption of each component.

```
 mysql> SHOW TRACE;
    +------+------------+--------------+---------------------------------------------------
-------+----------------------------------------------+---------------+-------------------- ------+------+----------------------------------------------------------------------------- -----------------------------------------------------------------+--------+
    | ID   | TIMESTAMP  | TYPE         | GROUP_NAME
```

```
| DBKEY_NAME                                   | TIME_COST(MS) | CONNECTION_TIME_COST(MS) |
ROWS | STATEMENT
| PARAMS |
    +------+------------+--------------+---------------------------------------------------
-------+----------------------------------------------+---------------+-------------------- ------+------+----------------------------------------------------------------------------- -----------------------------------------------------------------+--------+
    |    0 |      0.000 | Optimize     | DRDS
| DRDS                                         | 2             | 0.00                     |
0 | select detail_url, sum(price) from t_item group by detail_url
| NULL   |
    |    1 | 423507.342 | Merge Sorted | DRDS
| DRDS                                         | 411307        | 0.00                     |
8 | Using Merge Sorted, Order By (`t_item`.`detail_url` asc )
| NULL   |
    |    2 |      2.378 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
03_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0003_hbpz | 15 | 1.59
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    3 |      2.731 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
00_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0000_hbpz | 11 | 1.78
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    4 |      2.933 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
04_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0004_hbpz | 15 | 1.48
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    5 |      3.111 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
01_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0001_hbpz | 15 | 1.56
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    6 |      3.323 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
07_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0007_hbpz | 15 | 1.54
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    7 |      3.496 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
06_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0006_hbpz | 18 | 1.30
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    8 |      3.505 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
05_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0005_hbpz | 423507 | 1.97
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |    9 |      3.686 | Query        | TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_00
02_RDS | rdso6g5b6206sdq832ow_test_123_wvvp_0002_hbpz | 14 | 1.47
|    1 | select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by
`t_item`.`detail_url` order by `t_item`.`detail_url` asc | NULL |
    |   10 | 423807.906 | Aggregate    | DRDS
| DRDS                                         | 1413          | 0.00                     |
1 | Aggregate Function (SUM(`t_item`.`price`)), Group By (`t_item`.`detail_url` asc )
| NULL   |
    +------+------------+--------------+---------------------------------------------------
-------+----------------------------------------------+---------------+-------------------- ------+------+-----------------------------------------------------------------------------
```

```
-----------------------------------------------------------------+--------+
    11 rows in set (0.01 sec)
```

In the returned results of SHOW TRACE, you can determine which node has a long execution time based on the values (in milliseconds) in the TIME_COST column. You can also see the corresponding GROUP_NAME (that is, the PolarDB-X 1.0 or ApsaraDB RDS for MySQL node) and the STATEMENT column information (that is, the SQL statement being executed). By checking whether the value of GROUP_NAME is PolarDB-X 1.0, you can determine whether the slow node exists in PolarDB-X 1.0 or ApsaraDB RDS for MySQL. According to the preceding results, the Merge Sorted action on the PolarDB-X 1.0 node and the TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS node of ApsaraDB RDS for MySQL take a lot of time.

#### 14.9.4 Troubleshoot the performance loss

Slow nodes may exist on the PolarDB-X 1.0 or ApsaraDB RDS for MySQL instance. Troubleshoot the fault accordingly after the cause is determined. Solution for slow PolarDB-X 1.0 nodes When the `GROUP_NAME` of a slow node is in the PolarDB-X 1.0 instance, check whether time-consuming computing operations such as Merge Sorted, Temp Table Merge, and Aggregate exist during SQL statement execution. If so, rectify it. For more information, see Overview. Solution for slow ApsaraDB RDS for MySQL nodes When the slow node is on the ApsaraDB RDS for MySQL instance, check the execution plan of this SQL statement on the ApsaraDB RDS for MySQL instance. In PolarDB-X 1.0, you can run /! TDDL:node={GROUP_NAME}*/ EXPLAIN to check the SQL execution plan of an ApsaraDB RDS for MySQL instance. The execution plan displays the SQL execution process information, including inter-table association and index information. The detailed process is as follows:

| GROUP NAME _ | , asse |
|---|---|

1. Based on `GROUP_NAME` , assemble the HINT: /! TDDL:node='TEST_123_1488766060743ACTJSANGUAN

```
_TEST_123_WVVP_0005_RDS'*/ .
```

2. Combine the assembled HINT and the statement prefixed by EXPLAIN to form a new SQL statement
and run it. The EXPLAIN command does not actually run. It only displays the execution plan of the SQL statement. The following example describes how to query the execution plan of the identified slow node.

```
    mysql> /! TDDL:node='TEST_123_1488766060743ACTJSANGUAN_TEST_123_WVVP_0005_RDS'*/ EXPLAI
N select `t_item`.`detail_url`,SUM(distinct `t_item`.`price`) from `t_item` group by `t_it em`.`detail_url` order by `t_item`.`detail_url` asc;
    +----+-------------+--------+------+---------------+-----+---------+-----+---------+---
------------------------------+
    | id | select_type | table  | type | possible_keys | key | key_len | ref | rows    | Ex
tra |
    +----+-------------+--------+------+---------------+-----+---------+-----+---------+---
------------------------------+
    |  1 | SIMPLE      | t_item | ALL  | NULL          |NULL | NULL    | NULL| 1322263 | Us
ing temporary; Using filesort |
    +----+-------------+--------+------+---------------+-----+---------+-----+---------+---
------------------------------+
    1 row in set (0.01 sec)
```

When the preceding SQL statement is run in ApsaraDB RDS for MySQL, the message Using temporary; `Using filesort` is returned. It indicates that low SQL statement execution is caused by improper use of the index. In this case, you can correct the index and run the SQL statement again.

### 14.10 Handle DDL exceptions

When you run any data definition language (DDL) commands of PolarDB-X 1.0, PolarDB-X performs the corresponding DDL operation on all table shards. Failures can be divided into two types:
1. A DDL statement fails to be executed in a database shard. DDL execution failure in any database
shard may result in inconsistent table shard structures.
2. The system does not respond for a long time after a DDL statement is executed. When you perform
a DDL statement on a large table, the system may make no response for a long time due to the long execution time of the DDL statement in a database shard. Execution failures in database shards may occur for various reasons. For example, the table you want to create already exists, the column you want to add already exists, or the disk space is insufficient. No response for a long time is generally caused by the long execution time of a DDL statement in a database shard. Taking ApsaraDB RDS for MySQL as an example, the DDL execution time depends mostly on whether the operation is an in-place (directly modifying the source table) or copy (copying data in the table) operation. An in-place operation only requires modification of metadata, while a copy operation reconstructs the whole table and also involves log and buffer operations. To determine whether a DDL operation is an in-place or copy operation, you can view the returned value of "rows affected" after the operation is completed. Example: Change the default value of a column (this operation is very fast and does not affect the table data at all):

```
Query OK, 0 rows affected (0.07 sec)
```

Add an index (this operation takes some time, but "0 rows affected" indicates that the table data is not replicated):

```
Query OK, 0 rows affected (21.42 sec)
```

Change the data type of column (this operation takes a long time and reconstructs all data rows in the table):

```
Query OK, 1671168 rows affected (1 min 35.54 sec)
```

Therefore, before executing a DDL operation on a large table, perform the following steps to determine whether the operation is a fast or slow operation:
1. Copy the table structure to generate a cloned table.
2. Insert some data.
3. Perform the DDL operation on the cloned table.
4. Check whether the value of "rows affected" is 0 after the operation is completed. A non-zero
value means that this operation reconstructs the entire table. In this case, you need to perform this operation in off-peak hours. Solution for failures PolarDB-X 1.0 DDL operations distribute all SQL statements to all database shards for parallel execution. Execution failure on any database shard does not affect the execution on other database shards. In addition, PolarDB-X 1.0 provides the CHECK TABLE command to check the structure consistency of the table shards. Therefore, failed DDL operations can be performed again, and errors reported on database shards on which the operations have been executed do not affect the execution on other database shards. Make sure that all table shards ultimately have the same structure. Procedure f or handling DDL operat ion f ailures
1. Run the CHECK T ABLE command to check the table structure. If the returned result contains only
one row and the status is normal, t he t able st at uses are consist ent . In this case, go to Step 2. Otherwise, go to Step 3.
2. Run the SHOW CREAT E T ABLE command to check the table structure. If the displayed table
structure is the same as the expected structure after the DDL statement is run, the DDL statement is run. Otherwise, go to Step 3.
3. Run the SHOW PROCESSLIST command to check the statuses of all SQL statements being
executed. If any ongoing DDL operations are detected, wait until these operations are completed, and then perform Steps 1 and 2 to check the table structure. Otherwise, go to Step 4.
4. Perform the DDL operation again on PolarDB-X 1.0. If the Lock conf lict error is reported, go to
Step 5. Otherwise, go to Step 3.
5. Run the RELEASE DBLOCK command to release the DDL operation lock, and then go to Step 4.
The procedure is as follows:
1. Check the table structure consistency
Run the CHECK TABLE command to check the table structure. When the returned result contains only one row and the displayed status is OK, t he t able st ruct ures are consist ent .

> Not ice If no result is returned after you run CHECK TABLE, retry by using the CLI.

```
mysql> check table `xxxx`; +----------------------------+-------+----------+----------+
| TABLE                      | OP    | MSG_TYPE | MSG_TEXT |
+----------------------------+-------+----------+----------+
| TDDL5_APP.xxxx             | check | status   | OK       |
+----------------------------+-------+----------+----------+ 1 row in set (0.05 sec)
```

2. Check the table structure
Run the SHOW CREATE TABLE command to check the table structure. If t able st ruct ures are consist ent and correct , the DDL statement has been run.

```
mysql> show create table `xxxx`; +---------+---------------------------------------------------------------------------- --------------------------------------+
| Table   | Create Table
```

|

```
+---------+---------------------------------------------------------------------------- --------------------------------------+
|  xxxx   | CREATE TABLE `xxxx` (
`id` int(11) NOT NULL DEFAULT '0', `NAME` varchar(1024) NOT NULL DEFAULT '', PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 dbpartition by hash(`id`) tbpartition by hash(`id` ) tbpartitions 3 | +---------+---------------------------------------------------------------------------- --------------------------------------+ 1 row in set (0.05 sec)
```

3. Check the SQL statements being executed.
If some DDL statement executions are slow and no response is received for a long time, you can run the SHOW PROCESSLIST command to check the status of all SQL statements being executed.

```
mysql> SHOW PROCESSLIST WHERE COMMAND ! = 'Sleep'; +---------------+-----------+--------------------+-------------+---------+------------- ----------------------------------------------------------+---------------------------- --------------------------------------------------------------------------+-----------+ ---------------+-----------+
| ID            | USER      | DB                 | COMMAND     | TIME    | STATE
| INFO
| ROWS_SENT | ROWS_EXAMINED | ROWS_READ |
+---------------+-----------+--------------------+-------------+---------+------------- ----------------------------------------------------------+---------------------------- --------------------------------------------------------------------------+-----------+ ---------------+-----------+
| 0-0-352724126 | ifisibhk0 | test_123_wvvp_0000 | Query       |      15 | Sending data
| /*DRDS /xx.xxx.xx.88/ac47e5a72801000/ */select `t_item`.`detail_url`,SUM(`t_item`.`pr
ice`) from `t_i | NULL | NULL | NULL |
| 0-0-352864311 | cowxhthg0 | NULL               | Binlog Dump |      13 | Master has s
ent all binlog to slave; waiting for binlog to be updated | NULL
|      NULL |          NULL |      NULL |
| 0-0-402714566 | ifisibhk0 | test_123_wvvp_0005 | Query       |      14 | Sending data
| /*DRDS /xx.xxx.xx.88/ac47e5a72801000/ */select `t_item`.`detail_url`,`t_item`.`price`
from `t_i | NULL | NULL | NULL |
| 0-0-402714795 | ifisibhk0 | test_123_wvvp_0005 | Alter       |     114 | Sending data
| /*DRDS /xx.xxx.xx.88/ac47e5a72801000/ */ALTER TABLE `Persons` ADD `Birthday` date
|      NULL |          NULL |      NULL |
...... +---------------+-----------+--------------------+-------------+---------+------------- ----------------------------------------------------------+---------------------------- --------------------------------------------------------------------------+-----------+ ---------------+-----------+ 12 rows in set (0.03 sec)
```

The value in the TIME column indicates the number of seconds that the command has been executed. If a command execution is too slow, as shown in the figure, you can run the KILL '0-0- 402714795' command to cancel the slow command.

> Not ice In PolarDB-X 1.0, one logical SQL statement corresponds to multiple statements on database shards. Therefore, you may need to kill multiple commands to stop a logical DDL statement. You can determine the logical SQL statement to which a command belongs based on the INFO column in the SHOW PROCESSLIST result set.

4. Handle the lock conflict error
PolarDB-X 1.0 adds a database lock before performing a DDL operation and releases the lock after the operation. The KILL DDL operation may not release the lock. If you perform the DDL operation again, the following error message will be returned:

```
Lock conflict , maybe last DDL is still running
```

In this case, run RELEASE DBLOCK to release the lock. After the command is canceled and the lock is released, run the DDL statement again during off-peak hours or when the service is stopped. Other problems Clients cannot display the modified table structures. To enable some clients to obtain table structures from system tables (such as COLUMNS or TABLES), PolarDB-X 1.0 creates a shadow database in database shard 0 on your ApsaraDB RDS for MySQL instance. The shadow database name must be the same as the name of your PolarDB-X 1.0 logical database. It stores all table structures and other information in the user database. The client obtains the PolarDB-X 1.0 table structure from the system table of the shadow database. During the processing of DDL exceptions, the table structure may be modified normally in the user database but not in the shadow database due to some reasons. In this case, you need to connect to the shadow database and perform the DDL operation on the table again in the database.

> Not ice The CHECK TABLE command does not check whether the table structure in the shadow database is consistent with that in the user database.

### 14.11 Efficiently scan PolarDB-X data

PolarDB-X 1.0 supports efficient data scanning and uses aggregate functions for statistical summary during full table scan. The following describes common scanning scenarios: Scan of t ables wit hout dat abase or t able shards: PolarDB-X 1.0 transmits the original SQL statement to the backend ApsaraDB RDS for MySQL database for execution. In this case, PolarDB-X 1.0 supports any aggregate functions. Non-f ull t able scan: PolarDB-X 1.0 transmits the original SQL statement to each single ApsaraDB RDS for MySQL database for execution. For example, when the shard key in the WHERE clause is Equal, non-full table scan is performed. In this case, PolarDB-X also supports any aggregate functions. Full t able scan: Currently, the supported aggregate functions are COUNT, MAX, MIN, and SUM. In addition, LIKE, ORDER BY, LIMIT, and GROUP BY are also supported during full table scan. Parallel scan of all t able shards: If you need to export data from all databases, you can run the SHOW command to view the table topology and scan all table shards in parallel. For more information, see the following section. Traverse tables by using a hint
1. Run the SHOW TOPOLOGY FROM TABLE_NAME command to obtain the table topology.

```
mysql:> SHOW TOPOLOGY FROM DRDS_USERS; +------+-------------------+--------------+
| ID   | GROUP_NAME        | TABLE_NAME   |
+------+-------------------+--------------+
|    0 | DRDS_00_RDS       | drds_users   |
|    1 | DRDS_01_RDS       | drds_users   |
+------+-------------------+--------------+ 2 rows in set (0.06 sec)
```

By default, the non-partition table is stored in database shard 0.
2. Traverse each table for TOPOLOGY.
i. Run the current SQL statement in database shard 0.

```
/! TDDL:node='DRDS_00_RDS'*/ SELECT * FROM DRDS_USERS;
```

ii. Run the current SQL statement in database shard 1.

```
/! TDDL:node='DRDS_01_RDS'*/ SELECT * FROM DRDS_USERS;
```

> Not ice We recommend that you run `SHOW TOPOLOGY FROM TABLE_NAME` to obtain the
> latest table topology before each scan.

Scan data in parallel PolarDB-X 1.0 allows you to run mysqldump to export data. However, if you want to scan data faster, you can establish multiple sessions for each table shard to scan tables in parallel.

```
mysql> SHOW TOPOLOGY FROM LJLTEST; +------+----------------+------------+
| ID   | GROUP_NAME     | TABLE_NAME |
+------+----------------+------------+
|    0 | TDDL5_00_GROUP | ljltest_00 |
|    1 | TDDL5_00_GROUP | ljltest_01 |
|    2 | TDDL5_00_GROUP | ljltest_02 |
|    3 | TDDL5_01_GROUP | ljltest_03 |
|    4 | TDDL5_01_GROUP | ljltest_04 |
|    5 | TDDL5_01_GROUP | ljltest_05 |
|    6 | TDDL5_02_GROUP | ljltest_06 |
|    7 | TDDL5_02_GROUP | ljltest_07 |
|    8 | TDDL5_02_GROUP | ljltest_08 |
|    9 | TDDL5_03_GROUP | ljltest_09 |
|   10 | TDDL5_03_GROUP | ljltest_10 |
|   11 | TDDL5_03_GROUP | ljltest_11 |
+------+----------------+------------+ 12 rows in set (0.06 sec)
```

As shown above, the table has four database shards, and each database shard has three table shards. Run the following SQL statement to operate on the table shards of the TDDL5_00_GROUP database:

```
/! TDDL:node='TDDL5_00_GROUP'*/ select * from ljltest_00;
```

> Not e TDDL5_00_GROUP in HINT corresponds to the GROUP_NAME column in the execution results of the SHOW TOPOLOGY command. In addition, the table name in the SQL statement is the table shard name.

At this time, you can establish up to 12 sessions (corresponding to 12 table shards respectively) to process data in parallel. ms

## 15 Appendix: PolarDB-X terms

This topic lists common terms of PolarDB-X 1.0 for your reference.

| Term | Description | Remarks |
|---|---|---|
| Cloud Native Distributed Database PolarDB- X | PolarDB-X 1.0 is a distributed database service that was independently developed by Alibaba to solve the bottlenecks of single-instance database services. PolarDB-X 1.0 is compatible with MySQL protocols and syntax. It supports automatic sharding, smooth scale-out, auto scaling, and transparent read/write splitting, and provides O&M capabilities for distributed databases throughout their entire lifecycle. | - |
| TDDL | Taobao Distributed Data Layer (TDDL) was developed by Alibaba and has become a preferred component for nearly 1,000 core applications of Alibaba. | - |
| PolarDB-X 1.0 Console | PolarDB-X 1.0 Console is designed for database administrators (DBAs) to isolate resources as required and perform operations, such as instance management, database and table management, read/write splitting configuration, smooth scale- out, monitoring data display, and IP address whitelist. | - |
| DRDS Manager | DRDS Manager is designed for global O&M personnel and DBAs to manage all PolarDB-X 1.0 resources and monitor the system. | - |
| PolarDB-X 1.0 Server | PolarDB-X 1.0 Server is the service layer of PolarDB-X 1.0. Multiple server nodes make up a server cluster to provide distributed database services, including the read/write splitting, routed SQL execution, result merging, dynamic database configuration, and globally unique ID (GUID). | - |
| Load balancer | PolarDB-X 1.0 server nodes are stateless, and therefore requests can be randomly routed to any PolarDB-X 1.0 server node. The load balancer is used to complete this task. Server Load Balancer (SLB) is used for overall output by Apsara Stack. VIPServer is typically used for Alibaba middleware output. | - |
| Diamond | Diamond manages the configuration and storage of PolarDB-X 1.0. It provides the configuration functions for storage, query, and notification. In PolarDB-X 1.0, Diamond stores the source data of databases, and configuration data including the sharding rules, and switches. | - |
| Data Replication System | Data Replication System migrates and synchronizes data for PolarDB-X 1.0. Its core capabilities include full data migration and incremental data synchronization. Its derived features include smooth data import, smooth scale-out, and global secondary index. Data Replication System requires the support of ZooKeeper and PolarDB-X 1.0 Rtools. | - |

ms

| Term | Description | Remarks |
|---|---|---|
| PolarDB-X 1.0 instance (PolarDB- X 1.0 instance) | A PolarDB-X 1.0 instance consists of multiple PolarDB-X 1.0 server nodes. A PolarDB-X 1.0 instance can contain multiple PolarDB-X 1.0 databases. | - |
| PolarDB-X 1.0 instance ID (PolarDB-X 1.0 instance ID) | An instance ID uniquely identifies an PolarDB-X 1.0 instance. | - |
| Number of nodes on a PolarDB-X 1.0 instance | The number of PolarDB-X 1.0 server nodes in a PolarDB-X 1.0 instance. | - |
| VIP | The virtual IP addresses (VIPs) of the load balancer can be classified as: 1. Public VIP, which is accessible from the Internet. It is used for testing. 2. Private VIP, which is accessible only from the Alibaba Cloud internal network. | - |
| VPC | Virtual Private Cloud (VPC) is generally used on Alibaba Cloud. | - |
| Region | A region is a geographical location, such as East China. This concept is generally used for Alibaba Cloud. | - |
| Azone | A physical area with independent power grids and networks within one region, such as Hangzhou Zone A. This concept is generally used for Alibaba Cloud. | - |
| Logical SQL statement | A logical SQL statement is an SQL statement sent from an application to PolarDB-X 1.0. | - |
| Physical SQL statement | A physical SQL statement is an SQL statement obtained after PolarDB-X 1.0 parses a logical SQL statement and sends it to ApsaraDB RDS for MySQL for execution. | Logical SQL statements and physical SQL statements may be the same or different. Logical and physical SQL statements may be in a one-to- one or one-to- many mapping. |
| QPS | The queries per second (QPS) is the average number of logical SQL statements executed by PolarDB-X 1.0 per second in a statistical period, | instead of the number of transactions. Most control statements, such as COMMIT and SET, are not counted in QPS. |

ms

| Term | Description | Remarks |
|---|---|---|
| RT | The response time (RT) is the average response time (in milliseconds) of logical SQL statements executed by PolarDB-X 1.0 in a statistical period. The RT of an SQL statement is calculated as follows: (Time when PolarDB-X 1.0 writes the last packet of the result set) - (Time when PolarDB-X 1.0 receives the SQL statement) | - |
| Physical QPS | The physical QPS is the average number of physical SQL statements that PolarDB-X 1.0 executes on ApsaraDB RDS for MySQL per second in a statistical period. | - |
| Physical RT | The physical RT is the average response time (in milliseconds) of physical SQL statements executed by PolarDB-X 1.0 on ApsaraDB RDS for MySQL in a statistical period. The RT of a physical SQL statement is calculated as follows: (Time when PolarDB-X 1.0 receives the result set returned by ApsaraDB RDS for MySQL) - (Time when PolarDB-X 1.0 starts to obtain the connection to ApsaraDB RDS for MySQL) | This includes the time of establishing a connection to ApsaraDB RDS for MySQL or obtaining a connection from the connection pool, the network transmission time, and the time of executing the SQL statement by ApsaraDB RDS for MySQL. |
| Connections | The number of connections established between the application and PolarDB-X 1.0, | instead of the number of connections established between PolarDB- X 1.0 and ApsaraDB RDS for MySQL. |
| Inbound traffic | The network traffic generated when the application sends SQL statements to PolarDB-X 1.0. | This traffic is irrelevant to the traffic used for interaction between PolarDB- X 1.0 and ApsaraDB RDS for MySQL. |

ms

| Term | Description | Remarks |
|---|---|---|
| Outbound traffic | The network traffic generated when PolarDB-X 1.0 sends the result set to the application. | This traffic is irrelevant to the traffic used for interaction between PolarDB- X 1.0 and ApsaraDB RDS for MySQL. |
| Number of active threads (ThreadRunning) | The number of threads running on a PolarDB-X 1.0 instance. This parameter can be used to indicate the load of the PolarDB- X 1.0 instance. | - |
| Global | The total monitoring data of all databases on a PolarDB-X 1.0 instance. | - |
| Memory usage | The Java Virtual Machine (JVM) memory usage of a PolarDB-X 1.0 server process. | - |
| Total memory usage | The memory usage of the machine where the PolarDB-X 1.0 server node is located. | This metric is available only when PolarDB-X 1.0 servers are deployed on ECS instances. Generally, this metric is used for Alibaba Cloud. |
| CPU utilization | The CPU utilization of the machine where a PolarDB-X 1.0 server node is located. | This metric is available only when PolarDB-X 1.0 servers are deployed on ECS instances. Generally, this metric is used for Alibaba Cloud. |
| System load | The load of the machine where a PolarDB-X 1.0 server node is located. | This metric is available only when PolarDB-X 1.0 servers are deployed on ECS instances. Generally, this metric is used for Alibaba Cloud. |

ms

| Term | Description | Remarks |
|---|---|---|
| Service port | The port used by PolarDB-X 1.0 servers to provide MySQL-based services to external applications. | Generally, the port number is 3306. However, when multiple PolarDB- X 1.0 nodes (mostly physical machines) are deployed on one machine, the port number will change accordingly. |
| Management port | The port used by PolarDB-X 1.0 servers to provide management application program interfaces (APIs). | Generally, the port number is the service port number plus 100. |
| Start time | The time when PolarDB-X 1.0 servers start. | - |
| Running time | The continuous running time of the PolarDB-X 1.0 servers since the last startup time. | - |
| Total memory size | The maximum JVM memory size of a PolarDB-X 1.0 server node. | - |
| Memory usage | The JVM memory that is already used by the PolarDB-X 1.0 server nodes. | - |
| Number of nodes | Required. The number of machines. A PolarDB-X 1.0 instance is essentially a PolarDB-X 1.0 cluster, and the number of nodes refers to the number of machines in the cluster. | - |
| Instance type | Required. The type of the instance, including dedicated and shared instances. A dedicated instance works in the exclusive mode. A shared instance works in the multi-tenant mode, which is generally used in Alibaba Cloud. | - |
| Machine type | Required. The type of the machine where a PolarDB-X server node is deployed. Valid values are Auto-selected, PHY, and ECS. The PolarDB-X 1.0 inventory is divided into physical machine inventory and virtual machine inventory according to the type of machines where the PolarDB-X servers are deployed. The two types cannot be mixed because their deployment and O&M methods are different. | - |
| AliUid | Required. The UID of the instance. In Apsara Stack, this ID is provided by the account system in the deployment environment. | - |
| Backend port | The backend port of the VIP. For a PolarDB-X 1.0 server node, this port is the service port of machine where the PolarDB-X server node is deployed. | - |

| ser Guide·Appendix: ms | PolarDB-X ter Cloud Native | Distributed Database PolarDB- |
|---|---|---|

| Term | Description | Remarks |
|---|---|---|
| Frontend port | The frontend port of the VIP for user access. Each VIP has a set of frontend ports and backend ports. The VIP forwards data from frontend ports to backend ports. | - |
| Private network/Internet | The network type of the VIP. Valid values: Internet: the public VIP, which is accessible from the Internet. Private network: the private VIP (including VPC VIP), which is accessible from private networks. | - |
| lbId | The ID of an SLB instance, which is the unique ID of VIP. A VIP is managed based on this ID. | - |
| Forwarding mode | The port forwarding mode of the VIP. The following modes are supported: FNAT: This mode is recommended when the backend machine is a virtual machine or VPC needs to be supported. NAT: This mode can be selected when the backend machine is a physical machine. Currently, this mode is only used on Alibaba Cloud. Open FNAT: This mode is applicable only to Alibaba Cloud. | - |
| VPC ID | The ID of the destination VPC, that is, the VPC to be accessed. | - |
| VSwitch ID | The ID of the destination VSwitch, which determines the CIDR block where the VPC VIP of the instance is in. | - |
| APPName | The app name of the destination PolarDB-X 1.0 database. Each PolarDB-X 1.0 database has a corresponding app name for loading configurations. | - |
| UserName | The user name used to log on to the destination PolarDB-X 1.0 database. | - |
| DBName | The name of the destination PolarDB-X 1.0 database you want to log on to. | - |
| IP address whitelist | Only the IP addresses specified in the IP address whitelist can access the PolarDB-X 1.0 instance. | - |

ms

| Term | Description | Remarks |
|---|---|---|
| Read-only instance | ApsaraDB RDS for MySQL instances where physical databases reside are divided into the following two types based on whether data can be written into the instances: Primary instance: Both read and write requests are allowed on such an instance. In Apsara Stack, ApsaraDB RDS for MySQL is supported. In Alibaba Cloud, ApsaraDB for RDS is supported. Read-only instance: Only read requests are allowed on such an instance. In Apsara Stack, ApsaraDB RDS for MySQL is supported. In Alibaba Cloud, ApsaraDB for RDS is supported. | - |
| Read SQL statement | A type of SQL statements used to read data, such as the SELECT statement. PolarDB-X 1.0 determines whether an SQL statement is a read-only SQL statement when it is not in a transaction. If the SQL statement is in a transaction, PolarDB-X treats it as a write SQL statement during read/write splitting. | - |
| Read/write splitting | If read-only ApsaraDB RDS for MySQL instances exist, you can configure in the PolarDB-X 1.0 console to allocate read SQL statements to the primary and read-only instances proportionally. PolarDB-X 1.0 automatically identifies the type of SQL statements and allocates them proportionally. | - |
| Smooth scale-out | On the basis of horizontal partitioning, the data distribution on ApsaraDB RDS for MySQL instances is dynamically adjusted for scale-out. Generally, scale-out is completed asynchronously without any modification to the business code. | - |
| Broadcast of small tables | You can synchronize the data in a single table in a database to all database shards in advance, to convert the cross-database JOIN query into a JOIN query that can be completed on physical databases. | - |
| Horizontal partitioning | Horizontal partitioning distributes the data rows originally stored in one table to multiple tables based on specified rules to achieve horizontal linear scaling. | - |
| Partition mode | This mode allows you to create multiple database shards on an ApsaraDB RDS for MySQL instance. These database shards make up a PolarDB-X 1.0 database. In this mode, all PolarDB-X 1.0 functions can be used. | - |
| Non-partition mode | In this mode, a database that has been created on an ApsaraDB RDS for MySQL instance is used as a PolarDB-X 1.0 database. In this mode, only PolarDB-X 1.0 read/write splitting is allowed, while other PolarDB-X 1.0 features such as database sharding and table sharding are not allowed. | - |
| Imported database | An existing database on the ApsaraDB RDS for MySQL instance selected for creating a PolarDB-X 1.0 database. This is a unique concept for the creation of a PolarDB-X database. | - |

| ser Guide·Appendix: ms | PolarDB-X ter Cloud Native | Distributed Database PolarDB- |
|---|---|---|

| Term | Description | Remarks |
|---|---|---|
| Read policy | The ratio of read SQL statements assigned by PolarDB-X 1.0 to the primary and read-only ApsaraDB RDS for MySQL instances. | - |
| Full table scan | If no shard field is specified in a SQL statement, PolarDB-X 1.0 runs the SQL statement on all table shards and summarizes the results. You can disable this function because of its high overheads. | - |
| Shard key | A column in a logical table. PolarDB-X 1.0 routes data and SQL statements to a physical table based on this column. | - |
| Data import | The operation of importing data from an existing ApsaraDB RDS for MySQL instance to a PolarDB-X 1.0 database. | - |
| Full data migration | The operation of migrating all existing records from a database to PolarDB-X 1.0. An offset is recorded before full migration starts. | - |
| Offset | In a MySQL binary log file, each row represents a data change operation. The position of a line in the binary log file is called an offset. | - |
| Incremental data migration | The operation of reading all MySQL binary log records from the recorded offset, converting them into SQL statements, and then running them in PolarDB-X 1.0. Incremental migration continues before the switchover. | - |
| Switchover | A step of data import and smooth scale-out, which writes all the remaining incremental records from MySQL binary logs to PolarDB-X 1.0. | - |
| Cleanup | The last step of smooth scale-out, which cleans redundant data and configurations generated during smooth scale-out. | - |
| Heterogeneous indexing | For table shards of a PolarDB-X 1.0 database, the WHERE condition of a SQL statement for query must contain the shard key whenever possible. In this way, PolarDB-X 1.0 routes the query request to a specific database shard, improving the query efficiency. If the WHERE condition of the SQL statement does not contain the shard key, PolarDB-X 1.0 performs a full table scan. PolarDB-X 1.0 provides heterogeneous indexing to solve this problem. The data in a database shard or table shard of a PolarDB-X 1.0 instance is fully or partially synchronized to another table based on different shard keys. The destination table to which the data is synchronized is called a heterogeneous index table. | - |
| PolarDB-X sequence | A PolarDB-X 1.0 sequence (a 64-digit number of the BIGINT data type in MySQL) aims to ensure that the data (for example, PRIMARY KEY and UNIQUE KEY) in the defined unique field is globally unique and in ordered increments. | - |

ms

| Term | Description | Remarks |
|---|---|---|
| PolarDB-X 1.0 hint | To facilitate PolarDB-X 1.0 usage, PolarDB-X 1.0 defines some hints to specify special actions. | - |
