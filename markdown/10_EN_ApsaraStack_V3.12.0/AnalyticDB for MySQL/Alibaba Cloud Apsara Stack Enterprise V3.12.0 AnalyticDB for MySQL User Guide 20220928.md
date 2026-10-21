---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for MySQL User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 140
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for MySQL User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20AnalyticDB%20for%20MySQL%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for MySQL User Guide 20220928

## Table of Contents

- 1 What is AnalyticDB for MySQL?
- 2 Limits
- 3 Quick start
  - 3.1 Log on to the AnalyticDB for MySQL console
  - 3.2 Create a database cluster
  - 3.3 Configure a whitelist
  - 3.4 Create a database account
  - 3.5 Create a database
  - 3.6 Connect to a database cluster
  - 3.7 Apply for a public endpoint
  - 3.8 Synchronize data
- 4 Connect to a database cluster
  - 4.1 Use the MySQL command-line tool to connect to AnalyticDB for MySQL
  - 4.2 Use the code in a business system to connect to AnalyticDB for MySQL
    - 4.2.2 PHP
    - 4.2.3 Python
    - 4.2.4 Druid connection pool
    - 4.2.5 Java
  - 4.3 Enable PrepareStatement for a client in different programming languages
  - 4.4 Use a client to connect to AnalyticDB for MySQL
    - 4.4.1 SQL Workbench/J
    - 4.4.2 DbVisualizer
    - 4.4.3 DBeaver
    - 4.4.4 Navicat
- 5 Manage database clusters
  - 5.1 View monitoring information
  - 5.2 Change specifications
  - 5.3 Delete a cluster
- 6 Backup and restoration
  - 6.1 Back up data
  - 6.2 Restore data
- 7 Diagnostics and optimization
  - 7.1 Use functions related to slow SQL queries
- 8 Account and permission management
  - 8.1 Permission model
  - 8.2 Manage database accounts and permissions
- 9 Data visualization
  - 9.1 Tableau
  - 9.2 QlikView
  - 9.3 FineReport
- 10 Data migration and synchronization
  - 10.1 Use Kettle to synchronize local data to AnalyticDB for MySQL
- 11 SQL manual
  - 11.1 Data types
  - 11.2 Data definition statements
    - 11.2.1 CREATE DATABASE
    - 11.2.2 CREATE TABLE
    - 11.2.3 ALTER TABLE
    - 11.2.4 CREATE VIEW
    - 11.2.5 DROP DATABASE
    - 11.2.6 DROP TABLE
    - 11.2.7 DROP VIEW
  - 11.3 Data manipulation statements
    - 11.3.1 INSERT INTO
    - 11.3.2 REPLACE INTO
    - 11.3.3 INSERT SELECT FROM
    - 11.3.4 REPLACE SELECT FROM
    - 11.3.5 INSERT OVERWRITE INTO SELECT
    - 11.3.6 UPDATE
    - 11.3.7 DELETE
    - 11.3.8 TRUNCATE TABLE
    - 11.3.9 KILL PROCESS
    - 11.3.10 SHOW PROCESSLIST
  - 11.4 SELECT
    - 11.4.1 Syntax
    - 11.4.2 WITH
    - 11.4.3 GROUP BY
    - 11.4.4 HAVING
    - 11.4.5 JOIN
    - 11.4.6 LIMIT
    - 11.4.7 ORDER BY
    - 11.4.8 Subqueries
    - 11.4.9 UNION, INTERSECT, and EXCEPT
  - 11.5 CREATE USER
  - 11.6 GRANT
  - 11.7 REVOKE
  - 11.8 Query users
  - 11.9 RENAME USER
  - 11.10 DROP USER
  - 11.11 SHOW
- 12 System functions
  - 12.1 Aggregate functions
    - 12.1.1 AVG
    - 12.1.2 BIT_AND
    - 12.1.3 BIT_OR
    - 12.1.4 BIT_XOR
    - 12.1.5 COUNT
    - 12.1.6 MAX
    - 12.1.7 MIN
    - 12.1.8 STD/STDDEV
    - 12.1.9 STDDEV_POP
    - 12.1.10 STDDEV_SAMP
    - 12.1.11 SUM
    - 12.1.12 VAR_POP
    - 12.1.13 VAR_SAMP
    - 12.1.14 VARIANCE
  - 12.2 Date and time functions
    - 12.2.1 ADDDATE/DATE_ADD
    - 12.2.2 ADDTIME
    - 12.2.3 CONVERT_TZ
    - 12.2.4 CURDATE
    - 12.2.5 CURTIME
    - 12.2.6 DATE
    - 12.2.7 DATE_FORMAT
    - 12.2.8 SUBDATE/DATE_SUB
    - 12.2.9 DATEDIFF
    - 12.2.10 DAY/DAYOFMONTH
    - 12.2.11 DAYNAME
    - 12.2.12 DAYOFWEEK
    - 12.2.13 DAYOFYEAR
    - 12.2.14 EXTRACT
    - 12.2.15 FROM_DAYS
    - 12.2.16 FROM_UNIXTIME
    - 12.2.17 HOUR
    - 12.2.18 LAST_DAY
    - 12.2.19 LOCALTIME/LOCALTIMESTAMP/NOW
    - 12.2.20 MAKEDATE
    - 12.2.21 MAKETIME
    - 12.2.22 MINUTE
    - 12.2.23 MONTH
    - 12.2.24 MONTHNAME
    - 12.2.25 PERIOD_ADD
    - 12.2.26 PERIOD_DIFF
    - 12.2.27 QUARTER
    - 12.2.28 SEC_TO_TIME
    - 12.2.29 SECOND
    - 12.2.30 STR_TO_DATE
    - 12.2.31 SUBTIME
    - 12.2.32 SYSDATE
    - 12.2.33 TIME
    - 12.2.34 TIME_FORMAT
    - 12.2.35 TIME_TO_SEC
    - 12.2.36 TIMEDIFF
    - 12.2.37 TIMESTAMP
    - 12.2.38 TIMESTAMPADD
    - 12.2.39 TIMESTAMPDIFF
    - 12.2.40 TO_DAYS
    - 12.2.41 TO_SECONDS
    - 12.2.42 UNIX_TIMESTAMP
    - 12.2.43 UTC_DATE
    - 12.2.44 UTC_TIME
    - 12.2.45 UTC_TIMESTAMP
    - 12.2.46 WEEK
    - 12.2.47 WEEKDAY
    - 12.2.48 WEEKOFYEAR
    - 12.2.49 YEAR
    - 12.2.50 YEARWEEK
  - 12.3 String functions
    - 12.3.1 ASCII
    - 12.3.2 BIN
    - 12.3.3 BIT_LENGTH
    - 12.3.4 CHAR
    - 12.3.5 CHAR_LENGTH/CHARACTER_LENGTH
    - 12.3.6 CONCAT
    - 12.3.7 CONCAT_WS
    - 12.3.8 ELT
    - 12.3.9 EXPORT_SET
    - 12.3.10 FIELD
    - 12.3.11 FIND_IN_SET
    - 12.3.12 FORMAT
    - 12.3.13 HEX
    - 12.3.14 INSTR
    - 12.3.15 LEFT
    - 12.3.16 LENGTH/OCTET_LENGTH
    - 12.3.17 LIKE
    - 12.3.18 LOCATE
    - 12.3.19 LOWER/LCASE
    - 12.3.20 LPAD
    - 12.3.21 LTRIM
    - 12.3.22 MAKE_SET
    - 12.3.23 MID
    - 12.3.24 OCT
    - 12.3.25 POSITION
    - 12.3.26 REPEAT
    - 12.3.27 REPLACE
    - 12.3.28 REVERSE
    - 12.3.29 RIGHT
    - 12.3.30 RLIKE/REGEXP
    - 12.3.31 RPAD
    - 12.3.32 RTRIM
    - 12.3.33 SPACE
    - 12.3.34 STRCMP
    - 12.3.35 SUBSTR/SUBSTRING
    - 12.3.36 SUBSTRING_INDEX
    - 12.3.37 TRIM
    - 12.3.38 UPPER/UCASE
  - 12.4 Numeric functions
    - 12.4.1 ABS
    - 12.4.2 ROUND
    - 12.4.3 SQRT
    - 12.4.5 LOG
    - 12.4.6 LOG2
    - 12.4.8 LOG10
    - 12.4.9 POWER/POW
    - 12.4.10 RADIANS
    - 12.4.11 DEGREES
    - 12.4.12 SIGN
    - 12.4.13 CEILING/CEIL
    - 12.4.14 FLOOR
    - 12.4.15 EXP
    - 12.4.16 COS
    - 12.4.17 ACOS
    - 12.4.18 TAN
    - 12.4.19 ATAN
    - 12.4.20 ATAN2
    - 12.4.21 COT
    - 12.4.22 ASIN
    - 12.4.23 SIN
  - 12.5 Arithmetic operators
  - 12.6 Bit functions and operators
  - 12.7 Control flow functions

ySQL?

## 1 What is AnalyticDB for MySQL?

AnalyticDB for MySQL is a real-time online analytical processing (RT-OLAP) service that is developed by Alibaba Cloud to analyze large amounts of data at high concurrency. AnalyticDB for MySQL can analyze hundreds of billions of data records across multiple dimensions within milliseconds and provide you with data-driven insights into your business. Not e OLAP systems are often compared with online transaction processing (OLTP) systems. OLAP systems are ideal for systems that require complex multidimensional queries and analytics on large amounts of data. The OLAP model is commonly adopted in analytical databases. OLTP systems are suitable for transactional processing, and ensures strong atomicity and consistency in data manipulation. The OLTP model supports frequent INSERT and UPDATE operations and is often used for relational database management systems, such as MySQL and Microsoft SQL Server. AnalyticDB for MySQL is an RT-OLAP system that offers the following benefits: Compatible with MySQL, business intelligence (BI) tools, and extract, transform, and load (ETL) tools for easy, cost-effective, and efficient analysis and integration of data. Uses relational models to store data and provides SQL statements to flexibly compute and analyze data. You do not need to create a data model in advance. Uses distributed computing technologies to provide excellent real-time computing capabilities. When AnalyticDB for MySQL processes tens of billions of data records or more, its performance can match or even surpass that of multidimensional online analytical processing (MOLAP) systems. AnalyticDB for MySQL can compute tens of billions of data records within several hundred milliseconds. You can then explore large amounts of data without constraints, instead of viewing data reports based on a predefined logic. Computes hundreds of billions of data records in real time. AnalyticDB for MySQL uses all data generated in your business system for data analysis, rather than sampling a portion of the data. This maximizes the effectiveness of analysis results. Supports a large number of concurrent queries and ensures high system availability through dynamic multi-copy storage and computing technology. Therefore, AnalyticDB for MySQL can serve as a backend system for various products, including user-facing and enterprise-facing products. AnalyticDB for MySQL is used in Internet business systems that have hundreds of thousands to tens of millions of users, such as Data Cube, Taobao Index, Kuaidi Dache, Alimama DMP, and Taobao Groceries. AnalyticDB for MySQL is a real-time computing system that provides rapid and flexible online data analysis and computation.

## 2 Limits

Take note of the following limits before you use AnalyticDB for MySQL.

| Object | Naming convention | Limit |
|---|---|---|
| Database name | A database name can be up to 64 characters in length, and can contain letters, digits, and underscores ( ). It must start _ with a lowercase letter and cannot contain consecutive underscores ( ). _ | Do not use analyticdb as the database name. The name analyticdb is reserved for a built- in database. |
| Table name | A table name must be 1 to 127 characters in length, and can contain letters, digits, and underscores ( ). It must start _ with a letter or underscore ( ). _ | A table name cannot contain single quotation marks ('), double quotation marks (''), exclamation points (!), or spaces. A table name cannot be SQL reserved keywords. |
| Column name | A column name must be 1 to 127 characters in length, and can contain letters, digits, and underscores ( ). It must start _ with a letter or underscore ( ). _ | A column name cannot contain single quotation marks ('), double quotation marks (''), exclamation points (!), or spaces. A column name cannot be SQL reserved keywords. |
| Account name | An account name must be 2 to 16 characters in length, and can contain lowercase letters, digits, and underscores ( ). It must start _ with a lowercase letter and end with a lowercase letter or digit. | None |
| Password | A password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + - = _ | None |
| Comment in a table | None | A table comment can be up to 1,024 characters in length. |
| Comment in a column | None | A column comment can be up to 1,024 characters in length. |

| nalyticDB for MySQL |   | User Guide·Limit |
|---|---|---|

| Object | Naming convention | Limit |
|---|---|---|
| Index name | None | An index name can be up to 64 characters in length. |
| Default value of a column | None | The default value of a column can be up to 127 characters in length. |

## 3 Quick start

### 3.1 Log on to the AnalyticDB for MySQL console

MySQL console This topic describes how to log on to the AnalyticDB for MySQL console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Dat abase Services > Analyt icDB f or MySQL.

### 3.2 Create a database cluster

This topic describes how to create an AnalyticDB for MySQL cluster. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. Click Creat e Clust er in the upper-right corner of the Clusters page and configure the parameters.

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| Region | The region where the cluster resides. You cannot change the region after the cluster is created. We recommend that you select a region that is closest to the geographic area of your business to improve access speed and stability. |
| Zone | The zone where the new cluster resides. A zone is an independent physical location within a region. There are no substantial differences between different zones within the same region. |
| Organizat ion | The organization to which the cluster belongs. |
| Resource Set | The resource set of the cluster. |
| Version | Only version 3.0 is supported. |
| Edit ion | Only Basic is supported. |
| Net work T ype | AnalyticDB for MySQL supports two types of networks. VPC: A VPC helps you build an isolated network environment in Apsara Stack. You can customize the route table, CIDR blocks, and gateway of a VPC. We recommend that you select VPC for higher security. Classic Network: Cloud services in the classic network are not isolated. Access control to cloud services in a classic network is implemented by the security groups or whitelist policies of the services. |
| Specif icat ions | The ECU specifications. |
| Node Groups | The number of node groups. By default, each node group consists of three replicas. |
| St orage | The storage space of a node group. |

3. After you configure the preceding parameters, click Submit .

### 3.3 Configure a whitelist

This topic describes how to configure a whitelist for a cluster in the AnalyticDB for MySQL console. Context After you create an AnalyticDB for MySQL cluster, you must configure a whitelist for the cluster to allow external devices to access the cluster. The default whitelist contains only the default IP address 127.0.0.1, which indicates that no devices are allowed to access the cluster. The whitelist can enhance access security of AnalyticDB for MySQL clusters. We recommend that you maintain the whitelist on a regular basis. The whitelist does not affect the normal operation of AnalyticDB for MySQL clusters. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to configure
a whitelist.
4. In the left-side navigation pane, click Dat a Securit y.
5. On the Whit elist Set t ings tab, click Edit to the right of the def ault whitelist.
Not e You can also click Create Whitelist to create a whitelist.
6. In the Edit Whit elist dialog box, delete the default IP address 127.0.0.1, enter the IP addresses or
CIDR blocks that you want to allow, and then click OK. The CIDR block 0.0.0.0/0 indicates that all IP addresses are allowed to access the cluster. Exercise caution when you add this CIDR block. If you enter a CIDR block such as 10.10.10.0/24, any IP addresses in the 10.10.10.X format can access the cluster. If you want to add multiple IP addresses or CIDR blocks, separate multiple entries with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. The whitelist modification takes effect within one minute.

### 3.4 Create a database account

This topic describes the database account types in AnalyticDB for MySQL and how to create database accounts. Account types AnalyticDB for MySQL supports two types of database accounts: privileged accounts and standard accounts. Account types

| Account type | Description |
|---|---|

| Account type | Description |
|---|---|
| Privileged account | You can create and manage privileged accounts only in the console. You can create only one privileged account for a cluster. You can use the privileged account to manage all standard accounts and databases of the cluster. You can use the privileged account of a cluster to disconnect any standard account of the cluster from AnalyticDB for MySQL. A privileged account has more permissions, which allows you to perform fine-grained management operations. For example, you can grant query permissions on different tables to different users. The privileged account in AnalyticDB for MySQL is equivalent to the root account in MySQL. |
| Standard account | You can use only SQL statements to create and manage standard accounts. You can create up to 256 standard accounts for a cluster. You must manually grant a standard account the permissions to access a specific database. You cannot use a standard account to disconnect other accounts from AnalyticDB for MySQL. |

Create a privileged account
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to create a
privileged account.
4. In the left-side navigation pane, click Account s. On the Account s page, click Creat e Account .
5. In the Creat e Account pane, configure the following parameters.

| Parameter | Description |
|---|---|
| Account | The name of the privileged account. The name must be 2 to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a lowercase _ letter and end with a lowercase letter or digit. |
| Account T ype | The type of the account. The value is Privileged Account. This value cannot be changed. |

| Guide·Quick start | AnalyticDB for MySQ |
|---|---|

| Parameter | Description |
|---|---|
| Password | The password of the privileged account. The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + - = _ |
| Conf irm Password | Enter the password of the privileged account again. |
| Descript ion | Optional. The description of the privileged account. |

6. Click OK to create the privileged account.
Create a standard account For more information about how to create a standard account and grant permissions to the standard account, see CREATE USER. What to do next

### 3.5 Create a database

You can use a MySQL client (such as Navicat for MySQL, DBeaver, DbVisualizer, or SQL Workbench/J), application code, or the MySQL command-line tool to connect to an AnalyticDB for MySQL cluster, and execute the CREATE DATABASE statement to create a database. Prerequisites You have connected to a database cluster. For more information, see Connect to a database cluster. Syntax

```
CREATE DATABASE [IF NOT EXISTS] db_name;
```

Example You can execute the following statement to create a database named adb_demo:

```
create database adb_demo;
```

### 3.6 Connect to a database cluster

This topic describes how to connect to an AnalyticDB for MySQL cluster. Prerequisites After you configure a whitelist and create a database account, you can use a MySQL client (such as Navicat for MySQL, DBeaver, DbVisualizer, or SQL Workbench/J), or the MySQL command-line tool to connect to the AnalyticDB for MySQL cluster. For more information, see Configure a whitelist and Create a database account. You can also configure the connection information such as the endpoint, port, and account of an AnalyticDB for MySQL cluster in an application to connect to the cluster. Use the code in an application to connect to AnalyticDB for MySQL C# Configure the Druid connection pool Use the MySQL command-line tool to connect to AnalyticDB for MySQL Use the MySQL command-line tool to connect to AnalyticDB for MySQL Use a client to connect to AnalyticDB for MySQL

### 3.7 Apply for a public endpoint

This topic describes how to use the AnalyticDB for MySQL console to apply for a public endpoint for a cluster. Context You must manually apply for a public endpoint. You can release the public endpoint if you do not need it. The public endpoint applies to the following scenarios: You want to access an AnalyticDB for MySQL cluster on devices that are not deployed in the Alibaba Cloud environment. You want to access an AnalyticDB for MySQL cluster from a region or of a network type that is different from the cluster. Apply for a public endpoint
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to apply for
a public endpoint.
4. In the Net work Inf ormat ion section of the Clust er Inf ormat ion page, click Apply f or Public
Endpoint .
5. In the Apply f or Public Endpoint message, click OK to obtain a public endpoint.
Not e Before you use the public endpoint to access the AnalyticDB for MySQL cluster, you must add the IP address of the device that you use to access the cluster to the whitelist. For more information, see Configure a whitelist. Release a public endpoint
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to release a
public endpoint.
4. On the Clust er Inf ormat ion page, click Release Public Endpoint .
5. In the Release Public Endpoint message, click OK to release the public endpoint.

### 3.8 Synchronize data

To synchronize data in different scenarios, you can use the following data loading solutions provided by AnalyticDB for MySQL: Use Kettle to synchronize data from relational databases, NoSQL databases such as HBase, or Microsoft Office Excel or Access to AnalyticDB for MySQL. Use external tables to import data from OSS to AnalyticDB for MySQL or export data from AnalyticDB for MySQL to OSS. Use the Load Data statement to write local data to AnalyticDB for MySQL. If the data already exists in AnalyticDB for MySQL tables, use the `INSERT INTO...SELECT FROM` statement to synchronize data. cluster

## 4 Connect to a database cluster

### 4.1 Use the MySQL command-line tool to connect to AnalyticDB for MySQL

tool to connect to AnalyticDB for MySQL This topic describes how to use the MySQL command-line tool to connect to an AnalyticDB for MySQL cluster. Syntax

```
mysql -hadb_url -P3306 -uadb_user -padb_password
```

Parameters `adb_url` : the endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can obtain the endpoint of the cluster in the Net work Inf ormat ion section of the Clust er Inf ormat ion page in the Analyt icDB f or MySQL console.

| 3306 | : the . |
|---|---|
| 3306 |   |
| adb user _ |   |

`3306` : the port number of the AnalyticDB for MySQL cluster endpoint. The default port number is `adb_user` : the account used to connect to the AnalyticDB for MySQL cluster. The account can be a privileged account or a standard account that has the required permissions. `adb_password` : the password of the account used to connect to the AnalyticDB for MySQL cluster. Example

```
mysql -ham-bp****.ads.aliyuncs.com -P3306 -utest -pTest123
```

### 4.2 Use the code in a business system to connect to AnalyticDB for MySQL

to connect to AnalyticDB for MySQL

#### 4.2.1 C#

This topic describes how to use the MySQL Connector/NET connector to connect to an AnalyticDB for MySQL cluster. cluster

```
using System; using System.Data; using MySql.Data; using MySql.Data.MySqlClient; namespace adbdemo
```

`{`

```java
    public class Tutorial2
```

`{`

```
        public static void Main()
```

`{`

```
    // server: the endpoint of the AnalyticDB for MySQL cluster to which you want to connec
t. You can obtain the endpoint on the Cluster Information page of the AnalyticDB for MySQL console.
    // UID: the account used to connect to the AnalyticDB for MySQL cluster. AnalyticDB for
MySQL offers the following types of accounts: privileged accounts and standard accounts.
    // database: the name of the database in the AnalyticDB for MySQL cluster.
    // port: the port number of the AnalyticDB for MySQL cluster endpoint.
    // password: the password of the account used to connect to the AnalyticDB for MySQL cl
uster.
            string connStr = "server=... ;UID=...;database=...;port=...;password=... ;SslMo
de=none;";
            MySqlConnection conn = new MySqlConnection(connStr);
            try
```

`{`

```
                Console.WriteLine("Connecting to MySQL...");
                conn.Open();
                string sql = "select c_custkey, c_name from customer limit 1";
                MySqlCommand cmd = new MySqlCommand(sql, conn);
                MySqlDataReader rdr = cmd.ExecuteReader();
                while (rdr.Read())
```

`{`

```
                    Console.WriteLine(rdr[0] + " --- " + rdr[]);
```

`}`

```
                rdr.Close();
```

`}`

```
            catch (Exception ex)
```

`{`

```
                Console.WriteLine(ex.ToString());
```

`}`

```
            conn.Close();
            Console.WriteLine("Done.") ;
```

`}` `}` `}`

#### 4.2.2 PHP

This topic describes how to connect to an AnalyticDB for MySQL cluster in PHP. Precautions If your operating system is Linux, you must install the php-mysql 5.1.x module. cluster If your operating system is Windows, you must install the php_MySQL.dll library. For more information about how to enable PrepareStatement if you use PDO to connect to AnalyticDB for MySQL, see Enable PrepareStatement for a client in different programming languages. Use MySQLi to connect to AnalyticDB for MySQL

```
// am-bp***.ads.aliyuncs.com: the endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can obtain the endpoint on the Cluster Information page of the Analyti cDB for MySQL console. $ads_server_name="am-bp***.ads.aliyuncs.com"; // account_name: the account used to connect to the AnalyticDB for MySQL cluster. AnalyticD B for MySQL offers the following types of accounts: privileged accounts and standard accoun ts. $ads_username="account_name"; // account_password: the password of the account used to connect to the AnalyticDB for MySQ L cluster. $ads_password="account_password"; // db_name: the name of the database in the AnalyticDB for MySQL cluster. $ads_database="db_name"; // 3306: the port number of the AnalyticDB for MySQL cluster endpoint. $ads_port=3306; // Connect to the AnalyticDB for MySQL cluster. $ads_conn=mysqli_connect($ads_server_name,$ads_username,$ads_password,$ads_database, $ads_p ort); $strsql="SELECT user_id FROM my_ads_db.my_first_table limit 20;"; $result=mysqli_query($ads_conn, $strsql); while($row = mysqli_fetch_array($result)) {
 // user_id: the name of the column to be queried.
  echo $row["user_id"] ;
```

`}` Use PDO to connect to AnalyticDB for MySQL cluster

```
// am-bp***.ads.aliyuncs.com: the endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can obtain the endpoint on the Cluster Information page of the Analyti cDB for MySQL console. $ads_server_name = "am-bp***.ads.aliyuncs.com"; // account_name: the account used to connect to the AnalyticDB for MySQL cluster. AnalyticD B for MySQL offers the following types of accounts: privileged accounts and standard accoun ts. $ads_username = "account_name"; // account_password: the password of the account used to connect to the AnalyticDB for MySQ L cluster. $ads_password = "account_password"; // db_name: the name of the database in the AnalyticDB for MySQL cluster. $ads_database = 'db_name'; // 3306: the port number of the AnalyticDB for MySQL cluster endpoint. $ads_port = 3306; $dsn = "mysql:host={$ads_server_name};dbname={$ads_database};port={$ads_port}"; try {
    $dbh = new PDO($dsn, $ads_username, $ads_password);
    echo 'PDO Success !' ;
} catch (PDOException $e) {
    echo 'PDO Connection failed: ' . $e->getCode() ."\n" . $e->getMessage() ."\n". $e->getT
raceAsString();
```

`}`

#### 4.2.3 Python

This topic describes how to use Python MySQLdb to connect to an AnalyticDB for MySQL cluster.

```java
#! /usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
# Create a database connection.
# host: the endpoint or IP address of the AnalyticDB for MySQL cluster to which you want to
connect.
# port: the port number of the AnalyticDB for MySQL cluster endpoint.
# user: the account used to connect to the AnalyticDB for MySQL cluster. AnalyticDB for MyS
QL offers the following types of accounts: privileged accounts and standard accounts.
# passwd: the password of the account used to connect to the AnalyticDB for MySQL cluster.
# db: the name of the database in the AnalyticDB for MySQL cluster.
db = MySQLdb.connect(host='am-bp***.ads.aliyuncs.com', port=3306, user='account_name', pass wd='account_password', db='db_name')
# Use the cursor() method to obtain an operation cursor.
cursor = db.cursor()
# Use the execute() method to execute SQL statements.
cursor.execute("SELECT VERSION()")
# Use the fetchone() method to obtain a data entry.
data = cursor.fetchone() print "Database version : %s " % data
# Close the database connection.
db.close()
```

cluster

#### 4.2.4 Druid connection pool

This topic describes how to use the Java Database Connectivity (JDBC) Druid connection pool to connect to an AnalyticDB for MySQL cluster. Precautions When you use the Druid connection pool to connect to an AnalyticDB for MySQL cluster, we recommend that you set `keepAlive` to true. In this way, you can reuse connections and avoid short-lived connections. Use Druid 1.1.12 or later. Configure the Druid connection pool cluster

```
 <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource" init-method="init" de
stroy-method="close">
     <! -- jdbc_url: the endpoint of the AnalyticDB for MySQL cluster to which you want to
connect. You can obtain the endpoint on the Cluster Information page of the AnalyticDB for MySQL console.-->
     <property name="url" value="${jdbc_url}" />
     <! -- jdbc_user: the account used to connect to the AnalyticDB for MySQL cluster. Anal
yticDB for MySQL offers the following types of accounts: privileged accounts and standard a ccounts. -->
     <property name="username" value="${jdbc_user}" />
     <! -- jdbc_password: the password of the account used to connect to the AnalyticDB for
MySQL cluster. -->
     <property name="password" value="${jdbc_password}" />
     <! -- Set the initial size of the connection pool, and the minimum and maximum numbers
of connections. -->
     <property name="initialSize" value="5" />
     <property name="minIdle" value="10" />
     <property name="maxActive" value="20" />
     <! -- Set the timeout period for obtaining a connection from the connection pool. -->
     <property name="maxWait" value="60000" />
     <! -- Set the interval for detecting idle connections to be closed. Unit: milliseconds
. -->
     <property name="timeBetweenEvictionRunsMillis" value="2000" />
     <! -- Set the minimum validity period of a connection in the connection pool. Unit: mi
lliseconds. -->
     <property name="minEvictableIdleTimeMillis" value="600000" />
     <property name="maxEvictableIdleTimeMillis" value="900000" />
     <property name="validationQuery" value="select 1" />
     <property name="testWhileIdle" value="true" />
      <! -- Specify whether to check the validity of the connection each time you obtain a
connection from the connection pool. A value of true indicates that the validity of the con nection is checked. A value of false indicates that the validity of the connection is not c hecked. -->
     <property name="testOnBorrow" value="false" />
      <! -- Specify whether to check the validity of the connection each time you return a
connection to the connection pool. A value of true indicates that the validity of the conne ction is checked. A value of false indicates that the validity of the connection is not che cked. -->
     <property name="testOnReturn" value="false" />
     <property name="keepAlive" value="true" />
     <property name="phyMaxUseCount" value="100000" />
     <! -- Set the filters to be used for monitoring statistics. -->
     <property name="filters" value="stat" />
 </bean>
```

#### 4.2.5 Java

This topic describes how to use MySQL Connector/J to connect to an AnalyticDB for MySQL cluster. Supported MySQL Connector/J versions AnalyticDB for MySQL supports the following MySQL Connector/J versions: cluster 5.0 series: 5.0.2, 5.0.3, 5.0.4, 5.0.5, 5.0.7, and 5.0.8. 5.1 series: 5.1.1, 5.1.2, 5.1.3, 5.1.4, 5.1.5, 5.1.6, 5.1.7, 5.1.8, 5.1.11, 5.1.12, 5.1.13, 5.1.14, 5.1.15, 5.1.16, 5.1.17, 5.1.18, 5.1.19, 5.1.20, 5.1.21, 5.1.22, 5.1.23, 5.1.24, 5.1.25, 5.1.26, 5.1.27, 5.1.28, 5.1.29, 5.1.31, 5.1.32, 5.1.33, and 5.1.34. Precautions To create MySQL Connector/J connections in Java, you must add the MySQL Connector/J package to your project. You must add the path of the mysql-connector-java-x.x.x.jar file to the value of the `CLASSPATH` variable in your project. Otherwise, you cannot create a MySQL Connector/J connection. Sample code for creating a MySQL Connector/J connection without retries To connect to AnalyticDB for MySQL databases through MySQL Connector/J, you can add the following Java code to your business system:

```java
Connection connection = null; Statement statement = null; ResultSet rs = null; try {
    Class.forName("com.mysql.jdbc.Driver");
    // adb_url: the endpoint of the AnalyticDB for MySQL cluster to which you want to conne
ct. You can obtain the endpoint on the Cluster Information page of the AnalyticDB for MySQL console. The default port number is 3306.
    // db_name: the name of the database in the AnalyticDB for MySQL cluster.
    String url = "jdbc:mysql://adb_url:3306/db_name? useUnicode=true&characterEncoding=UTF-
8";
    Properties connectionProps = new Properties();
    // account_name: the account used to connect to the AnalyticDB for MySQL cluster. Analy
ticDB for MySQL offers the following types of accounts: privileged accounts and standard ac counts.
    connectionProps.put("user", "account_name");
    // account_password: the password of the account used to connect to the AnalyticDB for
MySQL cluster.
    connectionProps.put("password", "account_password");
    connection = DriverManager.getConnection(url, connectionProps);
    statement = connection.createStatement();
    String query = "select count(*) from information_schema.tables";
    rs = statement.executeQuery(query);
    while (rs.next()) {
        System.out.println(rs.getObject(1));
```

`}`

```
} catch (ClassNotFoundException e) {
    e.printStackTrace();
} catch (SQLException e) {
    e.printStackTrace();
} catch (Exception e) {
    e.printStackTrace();
} finally {
    if (rs ! = null) {
        try {
            rs.close();
        } catch (SQLException e) {
```

cluster

```
            e.printStackTrace();
```

`}` `}`

```
    if (statement ! = null) {
        try {
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}`

```
    if (connection ! = null) {
        try {
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}` `}` Sample code for creating a MySQL Connector/J connection with retries When you create a MySQL Connector/J connection, you can configure the following parameters to implement a retry mechanism:

```
public static final int MAX_QUERY_RETRY_TIMES = 3; public static Connection conn = null; public static Statement statement = null; public static ResultSet rs = null; public static void main(String[] args) throws ClassNotFoundException {
    // db_name: the name of the database in the AnalyticDB for MySQL cluster.
    String yourDB = "db_name";
    // account_name: the account used to connect to the AnalyticDB for MySQL cluster. Analy
ticDB for MySQL offers the following types of accounts: privileged accounts and standard ac counts.
    String username = "account_name";
    // account_password: the password of the account used to connect to the AnalyticDB for
MySQL cluster.
    String password = "account_password";
    Class.forName("com.mysql.jdbc.Driver");
    // adb_url: the endpoint of the AnalyticDB for MySQL cluster to which you want to conne
ct. You can obtain the endpoint on the Cluster Information page of the AnalyticDB for MySQL console. The default port number is 3306.
    String url = "jdbc:mysql://adb_url:3306/" + yourDB + "? useUnicode=true&characterEncodi
ng=UTF-8";
    Properties connectionProps = new Properties();
    connectionProps.put("user", username);
    connectionProps.put("password", password);
    String query = "select id from test4dmp.test limit 10";
    int retryTimes = 0;
    // Run automatic retries by using loops.
    while (retryTimes < MAX_QUERY_RETRY_TIMES) {
        try {
getConn(url connectionProps);
```

cluster

```java
            getConn(url, connectionProps);
            execQuery(query);// Run a query.
            break; // If the query is run, exit the loop.
        } catch (SQLException e) {
            System.out.println("Met SQL exception: " + e.getMessage() + ", then go to retry
task ...");
            try {
                if (conn == null || conn.isClosed()) {
                    retryTimes++;
```

`}`

```
            } catch (SQLException e1) {
                if (conn ! = null) {
                    try {
                        conn.close();
                    } catch (SQLException e2) {
                        e.printStackTrace();
```

`}` `}` `}` `}` `}`

```
    // Clear connection resource.
    closeResource();
```

`}`

```
/**
 * Get connection.
```

`*`

```
 * @param url
 * @param connectionProps
 * @throws SQLException
```

`*/`

```
public static void getConn(String url, Properties connectionProps) throws SQLException {
    conn = DriverManager.getConnection(url, connectionProps);
```

`}`

```
/**
 * Query task execution logic.
```

`*`

```
 * @param sql
 * @throws SQLException
```

`*/`

```java
public static void execQuery(String sql) throws SQLException {
    Statement statement = null;
    ResultSet rs = null;
    statement = conn.createStatement();
    for (int i = 0; i < 10; i++) {
        long startTs = System.currentTimeMillis();
        rs = statement.executeQuery(sql);
        int cnt = 0;
        while (rs.next()) {
            cnt++;
            System.out.println(rs.getObject(1) + " ");
```

`}`

```java
        long endTs = System.currentTimeMillis();
        System.out.println("Elapse Time: " + (endTs - startTs));
System.out.println("Rowcount:"+cnt);
```

cluster

```java
        System.out.println(Row count:  + cnt);
        try {
            Thread.sleep(160000);
        } catch (InterruptedException e) {
            e.printStackTrace();
```

`}` `}` `}`

```
/**
 * Close connection resource.
```

`*/`

```
public static void closeResource() {
    if (rs ! = null) {
        try {
            rs.close();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}`

```
    if (statement ! = null) {
        try {
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}`

```
    if (conn ! = null) {
        try {
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}` `}`

### 4.3 Enable PrepareStatement for a client in different programming languages

client in different programming languages Background information In most databases, SQL statements can be preprocessed on the server to improve database performance. AnalyticDB for MySQL databases deliver high performance without preprocessing SQL statements on the server side because these databases have the strong query capability, computing power, and plan cache feature. AnalyticDB for MySQL databases do not support the protocol for preprocessing SQL statements on the server. In most programming languages, you can enable PrepareStatement for a client to prepare statements or interpolate parameters on the client. This topic describes how to enable PrepareStatement for a client in different programming languages. cluster MySQL Connector/J (JDBC) driver You can enable PrepareStatement for the MySQL Connector/J (JDBC) driver when the following condition is met: `useServerPrepStmts=false` . For more information, visit Configuration Properties for Connector/J. Not e If the `useCursorFetch=true` condition is met, the `useServerPrepStmts=false` condition is overwritten and PrepareStatement cannot be enabled. MariaDB Connector/J You can enable PrepareStatement for MariaDB Connector/J if the following condition is met: `useServerPrepStmts=false` . For more information, visit About MariaDB Connector/J. Go MySQL driver You can enable PrepareStatement for the Go MySQL driver if the following condition is met: `interpolateParams=true` . For more information, visit go-sql-driver. PDO You can enable PrepareStatement for PDO if the following condition is met: `PDO::ATTR_EMULATE_PREPARES=TRUE` . For more information, visit setAttribute.

### 4.4 Use a client to connect to AnalyticDB for MySQL

AnalyticDB for MySQL

#### 4.4.1 SQL Workbench/J

SQL Workbench/J is a DBMS-independent, cross-platform SQL query tool. This topic describes how to use SQL Workbench/J to connect to an AnalyticDB for MySQL cluster. Preparations Before you use SQL Workbench/J, complete the following steps: Install the MySQL JDBC driver. Install SQL Workbench/J. Add the IP address of the device on which SQL Workbench/J is installed to the whitelist of the AnalyticDB for MySQL cluster. For more information, see Configure a whitelist. Precautions For more information about how to enable PrepareStatement in SQL Workbench/J, see Enable PrepareStatement for a client in different programming languages. Procedure
1. Start SQL Workbench/J and choose File > Manage Drivers....
cluster Not e If you use SQL Workbench/J for the first time, you must add the JDBC driver and its JAR file. When you use SQL Workbench/J later, you can skip step 2.
2. In the Manage drivers dialog box that appears, select MySQL as the driver, add the JAR file of the
driver, and then click OK.
3. Choose File > Connect window. In the Select Connect ion Prof ile dialog box that appears,
configure the connection parameters as required.

| Parameter |   | Description |   |   |
|---|---|---|---|---|
| New prof ile |   | The name of the connection, which facilitates subsequent management. |   |   |
| Driver |   | The type of the driver. Select MySQL from the drop-down list. |   |   |
| URL |   | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect, including the endpoint, port number, and database name. The format is jdbc:mysql://hostname:port/name _ of database , where: _ hostname : the public endpoint or VPC endpoint of the cluster. port : the port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. name of database : the name of the _ _ database in the cluster. This parameter is optional. |   |   |
|   |   |   | jdbc:mysql://hostname:port/name _ |   |
|   |   | of database _ |   |   |
| Username |   | The account used to connect to the AnalyticDB for MySQL cluster. You can use either of the following accounts: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |   |   |
| Password |   | The password of the account used to connect to the AnalyticDB for MySQL cluster. |   |   |

4. After configuring the preceding parameters, click T est to test connectivity. After the connection
passes the test, click OK to connect to the AnalyticDB for MySQL database.

#### 4.4.2 DbVisualizer

This topic describes how to use DbVisualizer to connect to an AnalyticDB for MySQL cluster. Preparations Before you use DbVisualizer, complete the following steps: cluster Install MySQL Connector/J. Install DbVisualizer. Add the IP address of the device on which DbVisualizer is installed to the whitelist of the AnalyticDB for MySQL cluster. For more information, see Configure a whitelist. Procedure
1. Start DbVisualizer and choose T ools > Connect ion Wizard. In the New Connect ion Wizard
dialog box, enter a name for the connection to facilitate subsequent management.
2. Click Next and select MySQL as the database driver from the drop-down list.
cluster
3. Click Next and configure the connection parameters.

| Parameter | Description |
|---|---|
| Not es | The description of the connection. |
| Dat abase Server | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can view the connection information about the cluster on the Cluster Information page of the AnalyticDB for MySQL console. |
| Dat abase Port | The port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. |
| Dat abase | The name of the database in the AnalyticDB for MySQL cluster. |
| Dat abase Userid | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |

cluster

| Parameter | Description |
|---|---|
| Dat abase Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

4. After you configure the preceding parameters, click Ping Server to test connectivity. After the
connection passes the test, click Finish. After the AnalyticDB for MySQL cluster is connected, you can use DbVisualizer to manage data.

#### 4.4.3 DBeaver

This topic describes how to use DBeaver to connect to an AnalyticDB for MySQL cluster. Context DBeaver is a free and open source database management tool distributed under General Public License (GPL). It is designed for developers and database administrators. DBeaver supports databases that are compatible with Java Database Connectivity (JDBC), such as MySQL, PostgreSQL, Oracle, DB2, SQL Server, and Sybase. DBeaver provides a graphical user interface (GUI), on which you can view database schemas, execute SQL statements and scripts, view and export data, and process binary large object (BLOB) or character large object (CLOB) data. Preparations Before you use DBeaver, complete the following steps: Click here to download and install DBeaver. cluster Install MySQL Connector/J. Add the IP address of the device on which DBeaver is installed to the whitelist of the AnalyticDB for MySQL cluster. For more information, see Configure a whitelist. Procedure
1. Start DBeaver and choose Dat abase > New Connect ion.
2. In the Creat e new connect ion dialog box, select MySQL as the connection type and click Next .
3. On the General tab of the Creat e new connect ion dialog box, configure the connection
parameters.

| Parameter | Description |
|---|---|
| Server Host | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can view the connection information about the cluster on the Cluster Information page of the AnalyticDB for MySQL console. |
| Port | The port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. |
| Dat abase | The name of the database in the AnalyticDB for MySQL cluster. |

| Analy | ticDB for MySQL | User Guide·Connect to a database cluste | r |
|---|---|---|---|

| Parameter | Description |
|---|---|
| User Name | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

4. After you configure the preceding parameters, click T est Connect ion.... After the connection
passes the test, click Finish to connect to the cluster.

#### 4.4.4 Navicat

This topic describes how to use Navicat to connect to an AnalyticDB for MySQL cluster. Context Navicat is a fast, reliable, and cost-effective database management tool designed to simplify database management and reduce costs. Navicat provides a graphical user interface (GUI) for you to create remote connections from the local computer to AnalyticDB for MySQL clusters and manage data. cluster Preparations Before you use Navicat for MySQL, complete the following steps: Click here to download and install Navicat for MySQL. Add the IP address of the device on which Navicat for MySQL is installed to the whitelist of the AnalyticDB for MySQL cluster to which you want to connect. For more information, see Configure a whitelist. Procedure
1. Start Navicat for MySQL and choose File > New Connect ion > MySQL. In the New Connect ion
dialog box, configure the connection parameters.

| Parameter | Description |
|---|---|
| Connect ion Name | The name of the connection. We recommend that you choose an identifiable name to facilitate subsequent management. |
| Host | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can view the connection information about the cluster on the Cluster Information page of the AnalyticDB for MySQL console. |
| Port | The port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. |
| User Name | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

If your operating system is macOS, add the database name after you configure the connection information.
2. Click T est Connect ion. After the connection passes the test, click OK.
The connection to the AnalyticDB for MySQL cluster is created but is not enabled. You must manually enable the connection.
3. Right-click a connect ion name and select Open Connect ion. Right-click a dat abase name to
enable the database connection. Then, you can use Navicat for MySQL to manage data. ers

## 5 Manage database clusters

### 5.1 View monitoring information

You can view cluster monitoring information in real time in the AnalyticDB for MySQL console. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to view
monitoring information.
4. In the left-side navigation pane, click Monit oring Inf ormat ion to view monitoring information of
the cluster. The monitoring information includes CPU utilization, cluster connections, QPS, and query response time.

### 5.2 Change specifications

This topic describes how to change the specifications of AnalyticDB for MySQL clusters. Context Not e You can modify only the number of node groups. ers Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. Click Change Specif icat ions in the Actions column corresponding to the cluster.
4. On the Change Specif icat ions page, set Node Groups and click Submit .

### 5.3 Delete a cluster

You can delete AnalyticDB for MySQL clusters. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. Choose More > Delet e in the Actions column corresponding to the cluster that you want to delete.
4. In the Delet e Clust er message, click OK.

## 6 Backup and restoration

### 6.1 Back up data

AnalyticDB for MySQL uses physical backups (snapshots) to automatically back up data every Tuesday and Friday from 02:00 to 03:00. The backup files are retained for seven days. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to back up
data.
4. In the left-side navigation pane, click Backup and Rest orat ion.
5. Click the Backup Set t ings tab to view the automatic settings.

### 6.2 Restore data

In AnalyticDB for MySQL, the cluster administrator can restore data from backup sets. ation

## 7 Diagnostics and optimization

### 7.1 Use functions related to slow SQL queries

queries AnalyticDB for MySQL provides the slow SQL analysis feature. You can view the trends and statistics of slow query logs and obtain diagnostic analysis and suggestions. Procedure
1. Log on to the AnalyticDB for MySQL console.
2. In the upper-left corner of the page, select the region where the cluster resides.
3. On the Clusters page, click Clust er ID corresponding to the cluster for which you want to view slow
query logs.
4. In the left-side navigation pane, click Query.
You can use one of the following methods to view slow query logs: Slow SQL Trend: displays the trend line chart of the slow query logs. Slow SQL Details: displays the detailed data of the slow query logs. management

## 8 Account and permission management

management

### 8.1 Permission model

Permission levels An AnalyticDB for MySQL cluster supports the following four levels of permission control: `GLOBAL` : cluster-level permissions `DB` : database-level permissions `TABLE` : table-level permissions `COLUMN` : column-level (field) permissions If you want a user to query the data of one specific column in a table, you can grant the `SELECT` permission on the column to the user. Example: `GRANT select (customer_id) ON customer TO 'test` `321'` . Operations and corresponding permissions

| Operation | Required permission | Supported permission level |
|---|---|---|
| SELECT | SELECT | DB TABLE COLUMN |
| INSERT | INSERT | DB TABLE COLUMN |
| INSERT...SELECT...FROM... | INSERT SELECT | DB TABLE COLUMN |
| UPDATE | UPDATE | DB TABLE COLUMN |
| DELETE | DELETE | DB TABLE |
| TRUNCATE TABLE | DROP | DB TABLE |

| U | ser Guide·Account and permission management |   | AnalyticDB for MySQ | L |
|---|---|---|---|---|

| Operation | Required permission | Supported permission level |
|---|---|---|
| ALTER TABLE | ALTER INSERT CREATE | DB TABLE |
| CREATE DATABASE | CREATE | N/A |
| CREATE TABLE | CREATE | DB TABLE |
| SHOW CREATE TABLE | SELECT | DB TABLE |
| DROP DATABASE | DROP | DB |
| DROP TABLE | DROP | DB TABLE |
| CREATE VIEW | CREATE VIEW _ SELECT | DB TABLE To execute the CREATE VIEW REPLACE statement, the DROP permission is also required in addition to the preceding permissions. |
| DROP VIEW | DROP | DB TABLE |
| SHOW CREATE VIEW | SHOW VIEW _ SELECT | DB TABLE |
| CREATE PROCEDURE _ | CREATE ROUTINE _ | N/A |
| DROP PROCEDURE _ | ALTER ROUTINE _ | N/A |
| CREATE EVENT _ | EVENT | N/A |
| DROP EVENT _ | EVENT | N/A |
| CREATE USER/DROP USER/RENAME USER | CREATE USER _ | N/A |
| SET PASSWORD | SUPER | N/A |

| nalyticDB for MySQL |   | User Guide·Account and permission managemen |
|---|---|---|

| Operation | Required permission | Supported permission level |
|---|---|---|
| GRANT/REVOKE | GRANT | N/A |

### 8.2 Manage database accounts and permissions

permissions For more information about how to create a RAM user, see `CREATE USER.` For more information about how to grant permissions to a RAM user, see `GRANT` . For more information about how to revoke the permissions of a RAM user, see `REVOKE` .

|   | RENAME USER |
|---|---|
| DROP USER |   |

For more information about how to modify the name of a database account, see `RENAME USER` . For more information about how to delete a database account, see `DROP USER` .

## 9 Data visualization

### 9.1 Tableau

This topic describes how to use Tableau to connect to an AnalyticDB for MySQL cluster and perform data analytics and visualization. Preparations Before you use Tableau, complete the following steps: Install the MySQL Open Database Connectivity (ODBC) driver. We recommend that you use MySQL Connector/ODBC 3.5.1 or 5.3. Install Tableau 9.0 or later. Procedure
1. Start Tableau and click MySQL in the left-side navigation pane to create a MySQL connection. In
the MySQL dialog box, configure the connection parameters.

| Parameter | Description |
|---|---|
| Server | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. |
| Port | The port number of the AnalyticDB for MySQL cluster endpoint. |
| User Name | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

2. After you configure the preceding parameters, click Log On to connect to the AnalyticDB for
MySQL cluster. Use Tableau In Tableau, you can view the databases on which you have permissions. After you select a database, you can read tables, preview data, and generate visual reports. For more information about how to use Tableau, visit Tableau.

### 9.2 QlikView

This topic describes how to use QlikView to connect to an AnalyticDB for MySQL cluster and build a business intelligence (BI) system. Preparations Before you use QlikView, complete the following steps: Install the MySQL Open Database Connectivity (ODBC) driver. We recommend that you use MySQL Connector/ODBC 3.5.1 or 5.3. Install QlikView 11.20.x. Procedure
1. On the host where QlikView is installed, click Cont rol Panel, and choose Syst em and Securit y >
Administ rat ive T ools > ODBC Dat a Sources. This path may vary with different operating systems. In the ODBC Data Source Administrator dialog box, add a system data source name (DSN) and select MySQL ODBC 5.xx Driver as the data source.

| Parameter | Description |
|---|---|
| Dat a Source Name | The name of the database in the AnalyticDB for MySQL cluster. |
| T CP/IP Server | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. |
| Port | The port number of the AnalyticDB for MySQL cluster endpoint. |
| User | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

2. After you configure the preceding parameters, click T est to test connectivity. After the
connection passes the test, click OK to create the ODBC connection.
3. Start QlikView and choose File > Edit Script . Select the database name specified in Step 1 to test
connectivity.
4. After the database passes the connectivity test, you can use the following SELECT statement to
obtain the data in the AnalyticDB for MySQL database:

```
SELECT * FROM DATABASE_NAME.TABLE_NAME;
```

For example, use the following statement to obtain data from the user_info table:

```
SELECT * FROM adb_database.user_info;
```

Use QlikView After you obtain data from AnalyticDB for MySQL databases, you can use QlikView to perform more operations. For more information about how to use QlikView, visit QlikView.

### 9.3 FineReport

This topic describes how to use FineReport to connect to an AnalyticDB for MySQL cluster and manage reports. Preparations Before you use FineReport, complete the following steps: Install MySQL Connector/J. Install FineReport. Procedure
1. Start FineReport and choose Server > Def ine Dat a Connect ion.
2. In the Def ine Dat a Connect ion dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Dat abase | The type of the database. Select MySQL from the drop-down list. |
| Driver | The type of the driver. Select MySQL JDBC driver from the drop-down list. |
| URL | The connection string of the AnalyticDB for MySQL cluster to which you want to connect. The format is jdbc:mysql://hostname:port . hostname : the public or VPC endpoint of the cluster. port : the port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. |
| User Name | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

3. After you configure the preceding parameters, click T est Connect ion. After the connection
passes the test, click Conf irm to the AnalyticDB for MySQL cluster. Use FineReport After FineReport is connected to the AnalyticDB for MySQL cluster, you can obtain the data in AnalyticDB for MySQL databases and use FineReport to generate reports. For more information about how to use FineReport, visit FineReport. hronization

## 10 Data migration and synchronization

synchronization

### 10.1 Use Kettle to synchronize local data to AnalyticDB for MySQL

data to AnalyticDB for MySQL This topic describes how to use Kettle to synchronize local data to AnalyticDB for MySQL. Excel data is used in the example. Background information Kettle is a popular open source extract-transform-load (ETL) tool used for data collection, conversion, and migration. Kettle supports not only various relational databases and NoSQL databases such as HBase and MongoDB, but also niche data sources such as Microsoft Office Excel and Access. Kettle can support more data sources by using extensions and plug-ins. For more information, visit Kettle. Preparations Before you use Kettle, complete the following steps: Click here to download and install Kettle. Create a database and a table in an AnalyticDB for MySQL cluster. For more information about how to create databases and tables, see Create a database and CREATE TABLE. Add the IP address of the device on which Kettle is installed to the whitelist of the AnalyticDB for MySQL cluster. For more information, see Configure a whitelist. Procedure
1. Start Kettle, and choose File > New > Conversion to create a conversion task.
2. Choose File > New > Dat abase Connect ion to create a database connection for the conversion
task.

| Parameter | Description |
|---|---|
| Connect ion Name | The name of the connection. We recommend that you choose an identifiable name, which facilitates subsequent management. |
| Connect ion T ype | The type of the connection. Select MySQL from the drop-down list. |
| Access | The access mode of the connection. Select Nat ive (JDBC). |

hronization

| Parameter | Description |
|---|---|
| Host Name | The endpoint of the AnalyticDB for MySQL cluster to which you want to connect. You can view the connection information about the cluster on the Cluster Information page of the AnalyticDB for MySQL console. |
| Dat abase Name | The name of the database in the AnalyticDB for MySQL cluster. |
| Port Number | The port number of the AnalyticDB for MySQL cluster endpoint. The default port number is 3306. |
| User Name | The account used to connect to the AnalyticDB for MySQL cluster. You can use one of the following account types: Privileged accounts. Standard accounts that have the permissions to connect to the cluster. |
| Password | The password of the account used to connect to the AnalyticDB for MySQL cluster. |

Not e Do not select Use Result St reaming Cursor when you configure the parameters.
3. After you configure the preceding parameters, click T est . In the Dat abase Connect ion T est
dialog box, follow the prompts to verify if the connection to the database is successful. After the connection passes the test, click OK.
4. In the left-side navigation pane of Kettle, click the Core object s tab, and choose Input > Excel
Input . Drag and drop Excel Input to the workspace.
5. Double-click Excel Input in the workspace. In the Excel Input dialog box, click Browse and Add
to add an Excel file to Select ed Files. Configure parameters on tabs such as Worksheet , Cont ent , and Field, and click Preview to check whether the specified values meet your requirements.
6. In the left-side navigation pane of Kettle, click the Core object s tab, and choose Out put > T able
Out put . Drag and drop Table Output to the workspace.
7. Add a connection line from Excel Input to T able Out put .
8. Double-click T able Out put in the workspace. In the T able Out put dialog box, configure the
parameters. T arget Schema: Enter the name of the AnalyticDB for MySQL database. T arget T able: Enter the name of the table in the AnalyticDB for MySQL database. Select Specif y dat abase f ields. Select Use bat ch updat e f or insert s. hronization On the Database fields tab of the T able Out put dialog box, click Get f ields and Ent er f ield mapping to map columns in the Excel file to those in the AnalyticDB for MySQL table.
9. Click the white arrow to perform the conversion. During this period, you can check the operation
logs and operating statuses. After the data in the Excel file is synchronized to the AnalyticDB for MySQL database, you can use AnalyticDB for MySQL to analyze the data.

## 11 SQL manual

### 11.1 Data types

Data types supported by AnalyticDB for MySQL

| Keyword |   |   |   |   |   | Data type |   |   |   |   | Valid value |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BOOLEAN |   |   |   |   |   | The Boolean type |   |   |   |   | Valid values: 0 and 1 . A value of 0 indicates false. A value of 1 indicates true. A BOOLEAN value is 1 bit in size. |   |   |
| TINYINT |   |   |   |   |   | The tiny integer type |   |   |   |   | Valid values: -128 to 127 . A TINYINT value is 1 byte in size. |   |   |
| SMALLINT |   |   |   |   |   | The small integer type |   |   |   |   | Valid values: -32768 to 32767 . A SMALLINT value is 2 bytes in size. |   |   |
| INT or INTEGER |   |   |   |   |   | The integer type |   |   |   |   | Valid values: -2147483648 to 2147483647 . An INT value is 4 bytes in size. |   |   |
| BIGINT |   |   |   |   |   | The big integer type |   |   |   |   | Valid values: - |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | - |   |
|   |   |   |   |   |   |   |   |   |   |   | 9223372036854775808 to |   |   |
|   |   |   |   |   |   |   |   | integer type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 9223372036854775807 |   |   |
| FLOAT |   |   |   |   |   |   |   |   |   |   | Valid values: - |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | - |   |
|   |   |   |   |   |   |   |   |   |   |   | 3.402823466E+38 to - |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 1.175494351E-38, 0, and |   |   |
|   |   |   |   |   |   | The single-precision floating- point type |   |   | -precision floating- |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 1.175494351E-38 to |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 3.402823466E+38 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Valid values: - |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | - |   |
|   |   |   |   |   |   |   |   |   |   |   | 1.7976931348623157E+308 to - |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 2.2250738585072014E-308, 0, |   |   |
|   |   |   |   |   |   | The double-precision floating- |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | and 2.2250738585072014E-308 |   |   |
| DOUBLE |   | DOUBLE | LE |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | point type |   |   |   |   | to 1.7976931348623157E+308 |   |   |

|   | 0 |
|---|---|
| 1 |   |

|   | 32767 |
|---|---|

| -2147483648 to |   |
|---|---|

|   | 2147483647 |
|---|---|

| Keyword | Data type | Valid value |
|---|---|---|
| DECIMAL(M,D) | The decimal type | M is the maximum precision, and its value range is 1 to 1000 . D is the decimal scale. The value of D must be less than or equal to that of M . |
| VARCHAR | The variable-length string type | A VARCHAR value can be up to 16 MB in size. You do not need to specify the size when you use VARCHAR. |
| DATE | The date type | Valid values: '0001-01-01' to '9999-12-31' . A DATE value is in the 'YYYY-MM-DD' format and is 4 bytes in size. |
| TIME | The time type | Valid values: '00:00:00' to '23:59:59' . A TIME value is in the 'HH:MM:SS' format and is 8 bytes in size. |
| DATETIME | The date and time type | Valid values: '0001-01-01 00:00:00.000' to '9999-12- 31 23:59:59.999' . A DATETIME value is in the 'YYYY- MM-DD HH:MM:SS' format. It is 8 bytes in size and in the UTC format. Not e DATETIME uses UTC time. You cannot change the time zone for DATETIME values. |
| TIMESTAMP | The timestamp type | Valid values: '0001-01-01 00:00:00.000' to '9999-12- 31 23:59:59.999' . A TIMESTAMP value is in the 'YYYY-MM-DD HH:MM:SS' format. It is 4 bytes in size and in the UTC format. Not e TIMESTAMP uses the time zone of the database system by default. You can specify the time zone for each session. |

|   | 1000 |
|---|---|

|   | '9999-12-31' |   |
|---|---|---|

| '00:00:00' to |   |
|---|---|

|   | '23:59:59' |   |
|---|---|---|

|   |   |   | '0001-01-01 |   |   |   |
|---|---|---|---|---|---|---|
|   |   | 00:00:00.000' |   |   |   |   |
|   |   |   |   | to | '9999-12- |   |

| 'YYYY- |   |
|---|---|

|   | MM-DD HH:MM:SS' |
|---|---|

|   |   |   | '0001-01-01 |   |   |   |
|---|---|---|---|---|---|---|
|   |   | 00:00:00.000' |   |   |   |   |
|   |   |   |   | to | '9999-12- |   |

Comparison with MySQL data types

| AnalyticDB for MySQL | MySQL | Difference |
|---|---|---|
| BOOLEAN | BOOL and BOOLEAN | No difference. |
| TINYINT | TINYINT | No difference. |
| SMALLINT | SMALLINT | No difference. |
| INT and INTEGER | INT and INTEGER | No difference. |
| BIGINT | BIGINT | No difference. |
| FLOAT | FLOAT[(M,D)] | No difference. |
| DOUBLE | DOUBLE[(M,D)] | No difference. |
| DECIMAL | DECIMAL | AnalyticDB for MySQL supports a maximum precision of 1,000 digits, while MySQL supports a maximum precision of only 65 digits. |
| VARCHAR | VARCHAR | The VARCHAR type in AnalyticDB for MySQL corresponds to the CHAR, VARCHAR, TEXT, MEDIUMTEXT, and LONGTEXT types in MySQL. |
| DATE | DATE | MySQL supports the value 0000-00-00 , whereas AnalyticDB for MySQL automatically converts the value 0000-00-00 to NULL. |
| TIME | TIME | AnalyticDB for MySQL is precise to the millisecond. MySQL supports custom precision levels. |
| DATETIME | DATETIME | MySQL supports the value 0000-00-00 00:00:00 , whereas AnalyticDB for MySQL automatically converts the value 0000-00-00 00:00:00 to NULL . AnalyticDB for MySQL is precise to the millisecond. MySQL supports custom precision levels. |
| TIMESTAMP | TIMESTAMP | AnalyticDB for MySQL is precise to the millisecond. MySQL supports custom precision levels. |

### 11.2 Data definition statements

#### 11.2.1 CREATE DATABASE

Create a database Not e You can create up to 256 databases in each AnalyticDB for MySQL cluster. Synt ax

```
ATE DATABASE [IF NOT EXISTS] db_name
```

Paramet ers `db_name` : the name of the database. The database name can be up to 64 characters in length, and can contain letters, digits, and underscores (_). It must start with a lowercase letter and cannot contain consecutive underscores (_). Not e Do not use analyticdb as the database name. The name analyticdb is reserved for a built-in database. Example

```
CREATE DATABASE adb_demo;
```

Use a database You can execute the `USE db_name` statement to use a database after it is created. Synt ax

```
USE db_name
```

Example

```
use adb_demo; show tables; +-----------------------------+
|Tables_in_adb_demo           |
+-----------------------------+
|customer                     |
|test_table                   |
```

#### 11.2.2 CREATE TABLE

You can execute the CREATE TABLE statement to create a table in AnalyticDB for MySQL. Syntax

```
CREATE TABLE [IF NOT EXISTS] table_name ({column_name column_type [column_attributes] [ column_constraints ] [COMMENT 'string']
| table_constraints}
[, ... ] ) table_attribute [partition_options] [AS] query_expression COMMENT 'string' column_attributes:
   [DEFAULT default_expr]
   [AUTO_INCREMENT]
column_constraints:
   [{NOT NULL|NULL} ]
   [PRIMARY KEY]
table_constraints:
   [{INDEX|KEY} [index_name] (column_name,...)]
   [PRIMARY KEY [index_name] (column_name,...)]
   [CLUSTERED KEY [index_name] (column_name,...)]
table_attribute:
   DISTRIBUTED BY HASH(column_name,...) | DISTRIBUTED BY BROADCAST
partition_options:
  PARTITION BY
         {VALUE(column_name) | VALUE(date_format(column_name, ?)}
  [LIFECYCLE N]
```

Parameters

| Parameter | Description |
|---|---|
| table name _ | The name of the table. The table name must be 1 to 127 characters in length, and can contain letters, digits, and underscores ( ). The table name must start with a _ letter or underscore ( ). _ Specify the table name in the db name.table name format to distinguish _ _ tables that have the same name across different databases. |
| column name _ | The name of the column. The column name must be 1 to 127 characters in length and can contain letters, digits, and underscores ( ). The table name must start with a _ letter or underscore ( ). _ |
| column type _ | The data type of the column to be added. For more information about the data types supported by AnalyticDB for MySQL, see Data types. |

| Parameter | Description |
|---|---|
| column attributes _ | DEFAULT default expr : the default value of _ the column. Enter an expression without variables, such as current timestamp . _ If this parameter is not specified, the default value is NULL. AUTO INCREMENT : optional. Specifies whether _ the column is an auto-increment column. The data type of an auto-increment column must be BIGINT. This is because AnalyticDB for MySQL provides unique values for an auto-increment column, but these values are not incremented in sequence. |
| column constraints _ | NOT NULL \| NULL : specifies whether the column accepts the NULL value. A value of NOT NULL indicates that the column does not accept the NULL value. A value of NULL indicates that the column accepts the NULL value. Default value: NULL. PRIMARY KEY : the primary key of the column. You can define multiple primary keys in the PRI MARY KEY(column name [, ... ]) format. _ |
| table constraints _ | INDEX\|KEY : the inverted index. AnalyticDB for MySQL automatically creates indexes for whole tables. You do not need to manually create an index. |
| PRIMARY KEY | The index for the primary keys. Only tables with primary keys support the DELETE and UPDATE operations. The primary keys must include the partition key. We recommend that you put the partition key before the primary key combination. |
| CLUSTERED KEY | The clustered index. It defines the columns used for sorting data in the table. The logical order of the key values in the clustered index determines the physical order of the corresponding rows in the table. You can add only one clustered index for each table. For example, clustered key col5 col6 cls index(col5,col6) specifies the _ _ _ col5 col6 clustered index. col5 col6 and col6 col5 are different clustered indexes. |

| NOT NULL \| | NULL |
|---|---|

| NOT |   |
|---|---|

|   | NULL |   |
|---|---|---|

|   | MARY KEY(column name [, ... ]) _ |
|---|---|

|   |   | clustered key |   |   |
|---|---|---|---|---|
|   | col5 col6 cls index(col5,col6) _ _ _ |   |   |   |

| Parameter | Description |
|---|---|
| DISTRIBUTED BY HASH(column name,...) _ | The distribution key of the fact table. The data of the table is distributed based on the hash value of the columns specified by column name . _ AnalyticDB for MySQL allows you to select multiple fields as the partition key. |
| DISTRIBUTED BY BROADCAST | The dimension table. The dimension table is stored on each node of a cluster. For performance reasons, we recommend that you do not store large amounts of data in the dimension table. |
| partition options _ | The options for fact table partitions. AnalyticDB for MySQL manages the lifecycle of tables based on the LIFECYCLE N parameter. That is, AnalyticDB for MySQL only stores N number of partitions. All other partitions are deleted. For example, PARTITION BY VALUE(column name) specifies that the table is _ partitioned based on the column specified by column name . PARTITION BY _ VALUE(DATE FORMAT(column name, '%Y%m%d')) _ _ specifies that the table is partitioned based on the column specified by column name after the _ column is formatted to a date format such as 20190101 . LIFECYCLE 365 specifies that a maximum of 365 partitions can be retained on each node. That is, only data of the last 365 days is stored. When you write data on the 366th day, the data from the first day is deleted. |

|   |   | PARTITION BY |
|---|---|---|
|   | VALUE(column name) _ |   |

|   |   | PARTITION BY |
|---|---|---|
|   | VALUE(DATE FORMAT(column name, '%Y%m%d')) _ _ |   |

Precautions AnalyticDB for MySQL clusters use the UTF-8 encoding format during table creation. This encoding format is equivalent to the utf8mb4 format in MySQL. AnalyticDB for MySQL does not support other encoding formats. You can create up to 256 × Number of node groups tables in an AnalyticDB for MySQL cluster. Examples Create a test table.

```
 create table test (
       id bigint auto_increment,
       name varchar,
       value int,
       ts timestamp
```

`)`

```
       DISTRIBUTED BY HASH(id)
```

The test table is a fact table. The `id` column is an auto-increment column. The distribution key is `id` . The data of the table is distributed based on the hash value of the `id` column. Create a customer table.

```
 CREATE TABLE customer (
    customer_id bigint NOT NULL COMMENT 'Customer ID',
    customer_name varchar NOT NULL COMMENT 'Customer name',
    phone_num bigint NOT NULL COMMENT 'Phone number',
    city_name varchar NOT NULL COMMENT 'City',
    sex int NOT NULL COMMENT 'Gender',
    id_number varchar NOT NULL COMMENT 'ID card number',
    home_address varchar NOT NULL COMMENT 'Home address',
    office_address varchar NOT NULL COMMENT 'Office address',
    age int NOT NULL COMMENT 'Age',
    login_time timestamp NOT NULL COMMENT 'Logon time',
    PRIMARY KEY (login_time,customer_id,phone_num)
  )  DISTRIBUTED BY HASH(customer_id)
  PARTITION BY VALUE(DATE_FORMAT(login_time, '%Y%m%d')) LIFECYCLE 30
  COMMENT 'Customer information table';
```

The customer table is a fact table. In the table, the distribution key is `customer_id` . The partition key is `login_time` . `login_time` , `customer_id` , and `phone_num` form the primary key combination.

#### 11.2.3 ALTER TABLE

You can execute the ALTER TABLE statement to modify a table. Not e You cannot modify the data type of a column in AnalyticDB for MySQL. Syntax

```
ALTER TABLE table_name
    ADD COLUMN (column_name column_definition,...)
  | ADD {INDEX|KEY} [index_name] (column_name,...)
  | ADD CLUSTERED [INDEX|KEY] [index_name] (column_name,...)
  | DROP COLUMN column_name
  | DROP {INDEX|KEY} index_name
  | DROP CLUSTERED [INDEX|KEY] index_name
  | MODIFY COLUMN column_name column_definition
  | RENAME new_table_name
  | TRUNCATE PARTITION {partition_names | ALL}
```

Add a column Synt ax

```
ALTER TABLE db_name.table_name ADD column_name data_type;
```

Example Add the `province` column of the `VARCHAR` type to the customer table.

```
ALTER TABLE adb_demo.customer ADD COLUMN province varchar comment 'Province';
```

Delete a column Synt ax

```
ALTER TABLE db_name.table_name DROP column_name data_type;
```

Example Delete the `province` column of the `VARCHAR` type from the customer table. Modify the comments of a column Synt ax

```
ALTER TABLE db_name.table_name MODIFY COLUMN column_name data_type comment 'new_comment';
```

Example Modify the `COMMENT` of the `province` column to the province where the customer locates in the customer table.

```
ALTER TABLE adb_demo.customer MODIFY COLUMN province varchar comment 'Province where the cu stomer locates';
```

Change the value constraint for a column from NOT NULL to NULL Not e You can change the value constraint only from NOT NULL to NULL, but not from NULL to NOT NULL. Synt ax

```
ALTER TABLE db_name.table_name MODIFY COLUMN column_name data_type {NULL}
```

Example

| Change the value of the | province | column to | NULL | in the customer tab |
|---|---|---|---|---|
| ALTER TABLE adb demo.customer MODIFY COLUMN province varchar NULL; _ |   |   |   |   |

Change the default value of a column Synt ax

```
ALTER TABLE db_name.table_name MODIFY COLUMN column_name data_type DEFAULT 'default'
```

Example Change the default value of the `sex` column to `0` (indicating male) in the customer table.

```
ALTER TABLE adb_demo.customer MODIFY COLUMN sex int(11) NOT NULL DEFAULT 0;
```

Add a clustered index Not e You can add only one clustered index for each table. Synt ax

```
ALTER TABLE db_name.table_name ADD CLUSTERED KEY index_name(column_name1,column_name2); ALTER TABLE db_name.table_name ADD CLUSTERED KEY index_name(column_name1);
```

Example Create a clustered index for the `customer_id` and `id_number` columns in the customer table.

```
ALTER TABLE adb_demo.customer ADD CLUSTERED KEY c_k(customer_id, id_number);
```

Delete a clustered index Synt ax

```
ALTER TABLE db_name.table_name DROP CLUSTERED KEY index_name;
```

Example Delete the clustered index of the customer table.

```
ALTER TABLE adb_demo.customer DROP CLUSTERED KEY c_k;
```

#### 11.2.4 CREATE VIEW

You can execute the CREATE VIEW statement to create a view. Syntax

```
CREATE VIEW view_name AS select_stmt
```

Parameters `view_name` : the name of the view to create. You can prefix the view name with the database name to distinguish views with the same name in different databases. `select_stmt` : the data source of the view. Example Create a view named v and set its data source to the customer table.

```
CREATE VIEW adb_demo.v AS SELECT * FROM customer;
```

#### 11.2.5 DROP DATABASE

You can execute the DROP DATABASE statement to delete a database. Syntax

```
DROP DATABASE db_name;
```

Not e Before you delete a database, you must first delete the tables in the database. Example

```
use adb_demo2; +------------------------------+ show tables; +------------------------------+
|Tables_in_adb_demo2           |
+------------------------------+
| test2                        |
+------------------------------+ drop table test2; drop database adb_demo2;
```

#### 11.2.6 DROP TABLE

You can execute the DROP TABLE statement to delete a table. Syntax

```
DROP TABLE db_name.table_name;
```

Not e When you execute this statement, both the table data and schema are deleted. Example

```
DROP TABLE adb_demo.customer;
```

#### 11.2.7 DROP VIEW

You can execute the DROP VIEW statement to delete a view. Syntax

```
DROP VIEW [IF EXISTS] view_name, [, view_name] ...
```

Parameters `view_name` : the name of the view to delete. You can prefix the view name with the database name to distinguish views with the same name in different databases. Example Delete the view named v.

```
DROP VIEW v;
```

### 11.3 Data manipulation statements

#### 11.3.1 INSERT INTO

You can execute the `INSERT INTO` statement to insert data to a table. If a primary key is the same as an existing one in the records, the new record is not inserted. This statement is equivalent to the `INSERT IGNORE INTO` statement. Syntax

```
INSERT [IGNORE]
     INTO table_name
     [( column_name [, ...] )]
     [VALUES]
     [(value_list[, ...])]
     [query];
```

Parameters `IGNORE` : optional. Specifies that a new record is not inserted if the primary key of the record is the same as that of an existing record.

| column name _ |   |
|---|---|
| query | : insert |

`column_name` : optional. The name of the column. `query` : inserts one or more records queried from another table to this table. Precautions If the column names are not specified, the sequence of the columns in the data to be inserted must be the same as that specified in the CREATE TABLE statement. Example Create the customer and courses tables.

```
CREATE TABLE customer (
  customer_id bigint NOT NULL COMMENT 'Customer ID',
  customer_name varchar NOT NULL COMMENT 'Customer name',
  phone_num bigint NOT NULL COMMENT 'Phone number',
  city_name varchar NOT NULL COMMENT 'City',
  sex int NOT NULL COMMENT 'Gender',
  id_number varchar NOT NULL COMMENT 'ID card number',
  home_address varchar NOT NULL COMMENT 'Home address',
  office_address varchar NOT NULL COMMENT 'Office address',
  age int NOT NULL COMMENT 'Age',
  login_time timestamp NOT NULL COMMENT 'Logon time',
  PRIMARY KEY (login_time,customer_id,phone_num)
)DISTRIBUTED BY HASH(customer_id) PARTITION BY VALUE(DATE_FORMAT(login_time, '%Y%m%d')) LIFECYCLE 30 COMMENT 'Customer information table'; CREATE TABLE courses( id bigint AUTO_INCREMENT PRIMARY KEY, name varchar(20) NOT NULL, grade varchar(20) default 'Grade 3', submission_date timestamp)DISTRIBUTED BY HASH(id)
```

Insert a record to the customer table.

```
INSERT INTO customer(customer_id,customer_name,phone_num,city_name,sex,id_number,home_add ress,office_address,age,login_time) values (002367,'Alan','13678973421','Hangzhou',0,'987300','West Lake','Cloud Town',23,'2018-03-0 2 10:00:00');
```

Insert multiple records to the customer table.

```
INSERT INTO customer(customer_id,customer_name,phone_num,city_name,sex,id_number,home_ad dress,office_address,age,login_time) values customer values(002367,'Tom','13678973421','Hangzhou',0,'987300','West Lake','Cloud Town' ,23,'2018-03-02 10:00:00'),(002368,'Alex','13878971234','Hangzhou',0,'987300','West Lake' ,'Cloud Town',28,'2018-08-01 11:00:00'),(002369,'Eric','13968075284','Hangzhou',1,'987300 ','West Lake','Cloud Town',35,'2018-09-12 08:11:00');
```

Insert multiple records to the customer table without specifying the column names.

```
INSERT INTO customer values(002367,'Tom','13678973421','Hangzhou',0,'987300','West Lake','Cloud Town',23,'2018 -03-02 10:00:00'),(002368,'Alex','13878971234','Hangzhou',0,'987300','West Lake','Cloud T own',28,'2018-08-01 11:00:00'),(002369,'Eric','13968075284','Hangzhou',1,'987300','West L ake',Cloud Town',35,'2018-09-12 08:11:00');
```

Insert a record to the courses table.

```
insert into courses (name,submission_date) values("Jams",NOW());
```

#### 11.3.2 REPLACE INTO

You can execute the `REPLACE INTO` statement to insert data to a table by overwriting the existing data in real time. The system first checks whether the primary key of a record to be inserted is the same as that of an existing record. If they are the same, the system deletes the existing record and inserts the new record. Otherwise, the system only inserts the new record. Syntax

```
REPLACE INTO table_name [(column_name,...)] VALUES ({Constant|NULL|DEFAULT},...),(...),...
```

Example Insert a record to the customer table by specifying the column names in the `REPLACE INTO` statement.

```
REPLACE INTO customer(customer_id,customer_name,phone_num,city_name,sex,id_number,home_ad dress,office_address,age,login_time) values (002367,'Alan','13678973421','Hangzhou',0,'9 87300','West Lake','Cloud Town',23,'2018-03-02 10:00:00');
```

Insert multiple records to the customer table without specifying the column names.

```
REPLACE INTO customer values(002367,'Tom','13678973421','Hangzhou',0,'987300','West Lake' ,'Cloud Town',23,'2018-03-02 10:00:00'),(002368,'Alex','13878971234','Hangzhou',0,'987300 ','West Lake','Cloud Town',28,'2018-08-01 11:00:00'),(002369,'Eric','13968075284','Hangzh ou',1,'987300','West Lake','Cloud Town',35,'2018-09-12 08:11:00');
```

#### 11.3.3 INSERT SELECT FROM

You can execute the `INSERT SELECT FROM` statement to copy records from one table to another. Syntax

```
INSERT INTO table_name [( column_name [, ...] )]query;
```

Parameters `column_name` : the name of the column. If you want to copy data in only some columns of the source table to the target table, the columns specified in the SELECT clause must have the same sequence and data types as those specified in the INSERT clause. `query` : the `SELECT FROM TABLE` or `SELECT FROM VIEW` statement. Example Copy data only in the specified columns of the customer table to the new_customer table by specifying the column names.

```
INSERT INTO new_customer (customer_id, customer_name, phone_num)
    SELECT customer_id, customer_name, phone_num FROM customer
    WHERE customer.customer_name = 'Alan';
```

Copy data in all columns of the customer table to the new_customer table and do not specify the column names.

```
INSERT INTO new_customer
  SELECT customer_id,customer_name,phone_num,city_name,sex,id_number,home_address,office_
address,age,login_time)
  FROM customer
  WHERE customer.customer_name = 'Alan';
```

#### 11.3.4 REPLACE SELECT FROM

You can execute the `REPLACE SELECT FROM` statement to copy records from one table to another by overwriting existing data in real time. The system first checks whether the primary key of a record to be inserted is the same as that of an existing record. If they are the same, the system deletes the existing record and inserts the new record. If they are not the same, the system inserts the new record. Syntax

```
REPLACE INTO table_name [(column_name,...)]query;
```

Parameter

| query | : the | SELECT FROM TABLE |
|---|---|---|
| column name : the name of the co _ |   |   |

`query` : the `SELECT FROM TABLE` or `SELECT FROM VIEW` statement. `column_name` : the name of the column. If you want to copy data in only some columns of the source table to the target table, the columns specified in the SELECT clause must have the same sequence and data types as those specified in the REPLACE clause. Precautions The target table to which the records are inserted must exist before you execute the `REPLACE SELECT` `FROM` statement. Example Copy data only in the specified columns of the customer table to the new_customer table by specifying the column names.

```
REPLACE INTO new_customer (customer_id, customer_name, phone_num)
  SELECT customer_id, customer_name, phone_num
  FROM customer
  WHERE customer.customer_name = 'Alan';
```

#### 11.3.5 INSERT OVERWRITE INTO SELECT

You can execute the `INSERT OVERWRITE INTO SELECT` statement to insert multiple records to a table at a time. Syntax

```
INSERT OVERWRITE INTO table_name [(column_name,...)] SELECT select_statement FROM from_statement
```

Precautions The target table to which the records are inserted must exist before you execute the `INSERT OVERW` `RITE INTO SELECT` statement.

| INSERT OVERWRITE INTO SELECT |   |   |
|---|---|---|
| able after the | INSERT OVERWRITE IN |   |

The existing data in the target table will not change before the `INSERT OVERWRITE INTO SELECT` statement is completed. The system writes data to the target table after the `INSERT OVERWRITE IN` `TO SELECT` statement is completed. If you execute the `INSERT OVERWRITE INTO SELECT` statement to insert a primary key that is the same as an existing one in the records, the new record is not inserted.

#### 11.3.6 UPDATE

You can execute the `UPDATE` statement to update data in a table. Syntax

```
UPDATE table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
```

Precautions The table on which you execute the `UPDATE` statement must have a primary key. Example Change the name of the customer who has the `customer_id ='2369'` attribute to Claire in the customer table.

```
update customer set customer_name ='Claire' where customer_id ='2369';
```

#### 11.3.7 DELETE

You can execute the DELETE statement to delete records from a table. Syntax

```
 DELETE FROM table_name[ WHERE condition ]
```

Precautions The table on which you execute the `DELETE` statement must have a primary key. You cannot use the alias of a table to execute the `DELETE` statement. If you need to delete all records of a table or all partitions, we recommend that you use the `TRUNCA` `TE TABLE` or `TRUNCATE PARTITION` statement, instead of the `DELETE` statement. Example Delete the record where `name` is Alex from the customer table.

```
DELETE FROM customer WHERE customer_name='Alex';
```

Delete the records where age is less than 18 from the customer table.

```
DELETE FROM customer WHERE age<18;
```

#### 11.3.8 TRUNCATE TABLE

You can execute the `TRUNCATE TABLE` statement to clear the data of a table or specified partitions in a table. Syntax Clear the data of a table.

```
TRUNCATE TABLE db_name.table_name;
```

Clear the data of specified partitions in a table.

```
TRUNCATE TABLE db_name.table_name PARTITION partition_name;
```

The data type of partition names is BIGINT. You can execute the following SQL statement to obtain the names of all partitions in a table:

```
select partition_name from information_schema.partitions where table_name = 'your_table_n ame' order by partition_name desc limit 100;
```

Precautions When you execute the `TRUNCATE TABLE` statement to clear the data of a table, the table schema is not deleted. Example Clear the data of the customer table.

```
TRUNCATE TABLE adb_demo.customer;
```

Clear the data of specified partitions in the customer table.

```
TRUNCATE TABLE adb_demo.customer partition 20170103,20170104,20170108
```

#### 11.3.9 KILL PROCESS

You can execute the `KILL PROCESS` statement to terminate a running process. Syntax

```
KILL PROCESS process_id
```

Parameters `process_id` : the ID of the process to terminate. You can query the process ID by executing the SHOW PROCESSLIST statement and checking the ProcessId field. Permission You can execute the `KILL PROCESS` statement to terminate the running processes under your account. The privileged account can grant the PROCESS permission to a standard account by using the `GRANT` statement. The standard account can then terminate the running processes of all accounts in the cluster.

```
GRANT process on *.* to account_name;
```

#### 11.3.10 SHOW PROCESSLIST

You can execute the `SHOW PROCESSLIST` statement to view the running processes. Not e You can also execute the `INFORMATION_SCHEMA PROCESSLIST` statement to view the running processes. Syntax

```
SHOW [FULL] PROCESSLIST
```

Response parameters The following response parameters are returned after you execute the `SHOW FULL PROCESSLIST` or `SHOW PROCESSLIST` statement: Id: the ID of the process. `ProcessId` : the unique ID of the task. This parameter is required when you execute the KILL PROCESS statement. `User` : the current account. `Host` : the hostname of the client that sends the SHOW PROCESSLIST statement, which consists of the IP address and port number.

| DB : the datab Command : the c |   |
|---|---|
| sleep | query |

`DB` : the database to which the process is connected. `Command` : the command that is executed in the current connection. The command types include `sleep` , `query` , and `connect` .

| connect |   | . |
|---|---|---|
| n the | Command |   |

`State` : the execution status of the SQL statement in the current connection. `Info` : the SQL statement. Not e If you do not specify the `FULL` keyword, you can view only the first 100 characters of the `Info` field in each record. Permission You can execute the `SHOW PROCESSLIST` statement to view the processes running under your account. A privileged account can grant the PROCESS permission to a standard account by using the GRANT statement. The standard account can then view the running processes of all accounts in the cluster.

```
GRANT process on *.* to account_name;
```

### 11.4 SELECT

#### 11.4.1 Syntax

You can use the SELECT statement to query data from one or more tables. The syntax is as follows:

```
[ WITH with_query [, ...] ] [ ALL | DISTINCT ] select_expr [, ...] [ FROM table_reference [, ...] ] [ WHERE condition ] [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ] [ HAVING condition] [ WINDOW window_name AS (window_spec) [, window_name AS (window_spec)] ...] [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ] [ ORDER BY {column_name | expr | position} [ASC | DESC], ... [WITH ROLLUP]] [LIMIT {[offset,] row_count | row_count OFFSET offset}]
```

`table_reference` : the data source from which data is queried. The source can be a table, view, associative table, or subquery. Table names and column names are not case-sensitive. If a table name or column name contains keywords or space characters, you can quote the table name or column name with backticks (``). WHERE You can enter a `BOOLEAN` expression in the `WHERE` keyword to query data records that meet the specified condition. For example, you can execute the following statement to query the information of the customer whose `customer_id` is 2368.

```
SELECT * FROM CUSTOMER where customer_id=2368;
```

ALL and DISTINCT You can use the ALL and DISTINCT keywords to specify whether duplicate rows are retained in the query result. The default value is ALL, indicating that all rows are returned. The DISTINCT keyword indicates that duplicate rows are deleted in the query result.

```
SELECT col1, col2 FROM t1;SELECT DISTINCT col1, col2 FROM t1;
```

The following methods show you how to use other keywords.

#### 11.4.2 WITH

This topic describes how to use the WITH clause in a SELECT statement. You can use the WITH clause to define subqueries by using common table expressions (CTEs) in a SELECT statement. The subqueries defined in the WITH clause can be referenced in the SELECT statement. The WITH clause can be used to flatten nested queries or simplify subqueries. Each subquery is performed only once in the SELECT statement. This improves the query performance. Not e A CTE is a named temporary result set, and is valid only in a single SQL statement, such as a SELECT, INSERT, and DELETE statement. A CTE is valid only during the period when the SQL statement is executing. Precautions A CTE can be followed by a SQL statement, such as a SELECT, INSERT, or UPDATE statement, or other CTEs in the same WITH clause. Separate multiple CTEs with commas ( `,` ). Otherwise, the CTEs will not take effect. The paging feature is not supported in a CTE. Use the WITH clause The following queries are equivalent:

```
SELECT a, b FROM (SELECT a, MAX(b) AS b FROM t GROUP BY a) AS x; WITH x AS (SELECT a, MAX(b) AS b FROM t GROUP BY a) SELECT a, b FROM x;
```

The WITH clause can be used to define multiple subqueries.

```
  t1 AS (SELECT a, MAX(b) AS b FROM x GROUP BY a),
  t2 AS (SELECT a, AVG(d) AS d FROM y GROUP BY a)
  SELECT t1.*, t2. *
  FROM t1 JOIN t2 ON t1.a = t2.a;
```

After a subquery is defined, other subqueries following this subquery in the same WITH clause can reference this subquery.

```
  x AS (SELECT a FROM t),
  y AS (SELECT a AS b FROM x),
  z AS (SELECT b AS c FROM y)
  SELECT c FROM z;
```

#### 11.4.3 GROUP BY

You can use the `GROUP BY` clause to group the query result. You can use the `GROUPING SETS` , `CUBE` , and `ROLLUP` options in the `GROUP BY` clause to display the grouping result in different forms. Syntax

```
GROUP BY expression [, ...]
```

GROUPING SET S

| GROUPING SETS |   | o |
|---|---|---|
| ual to the | UNION |   |

The `GROUPING SETS` option is used to specify multiple `GROUP BY` conditions for one query, which is equal to the `UNION` of multiple `GROUP BY` clauses.

```
SELECT origin_state, origin_zip, destination_state, sum(package_weight) FROM shipping GROUP BY GROUPING SETS (
    (origin_state),
    (origin_state, origin_zip),
    (destination_state));
```

The preceding statement is equal to the following statement:

```
SELECT origin_state, NULL, NULL, sum(package_weight) FROM shipping GROUP BY origin_state UNION ALL SELECT origin_state, origin_zip, NULL, sum(package_weight) FROM shipping GROUP BY origin_state, origin_zip UNION ALL SELECT NULL, NULL, destination_state, sum(package_weight) FROM shipping GROUP BY destination_state;
```

CUBE The `CUBE` option is used to list all possible grouping sets.

```
SELECT origin_state, destination_state, sum(package_weight) FROM shipping GROUP BY origin_state, destination_state WITH CUBE
```

The preceding statement is equal to the following statement:

```
SELECT origin_state, destination_state, sum(package_weight) FROM shipping GROUP BY GROUPING SETS (
    (origin_state, destination_state),
    (origin_state),
    (destination_state),
    ())
```

ROLLUP The `ROLLUP` option is used to list the grouping sets in a hierarchical manner.

```
SELECT origin_state, origin_zip, sum(package_weight) FROM shipping GROUP BY ROLLUP (origin_state, origin_zip)
```

The preceding statement is equal to the following statement:

```
SELECT origin_state, origin_zip, sum(package_weight) FROM shipping GROUP BY GROUPING SETS ((origin_state, origin_zip), (origin_state), ())
```

Precautions You must use standard aggregate functions such as `SUM` , `AVG` , and `COUNT` to specify the columns that are not used for grouping. Otherwise, the `GROUP BY` clause does not take effect. The `GROUP BY` clause must contain all the columns and non-aggregate expressions specified for the SELECT statement. Example The following statement contains two aggregate expressions. The first aggregate expression uses the SUM function, and the second uses the COUNT function. The LISTID and EVENTID columns are the columns that are used for grouping.

```
select listid, eventid, sum(pricepaid) as revenue, count(qtysold) as numtix from sales group by listid, eventid order by 3, 4, 2, 1 limit 5; listid | eventid | revenue | numtix -------+---------+---------+-------- 89397 | 47| 20.00 | 1 106590 | 76 | 20.00 | 1 124683 | 393 | 20.00 | 1 103037 | 403 | 20.00 | 1 47685 | 429 | 20.00 | 1 (5 rows)
```

You can also use the sequence numbers to reference columns in the GROUP BY clause. For example, you can modify the preceding statement as follows:

```
select listid, eventid, sum(pricepaid) as revenue, count(qtysold) as numtix from sales group by 1,2 order by 3, 4, 2, 1 limit 5; listid | eventid | revenue | numtix -------+---------+---------+-------- 89397 | 47 | 20.00 | 1 106590 | 76 | 20.00 | 1 124683 | 393 | 20.00 | 1 103037 | 403 | 20.00 | 1 147685 | 429 | 20.00 | 1
```

#### 11.4.4 HAVING

You can use the HAVING clause with the GROUP BY clause and aggregate functions to display groups that only meet certain conditions after grouping and aggregation. Syntax

```
[ HAVING condition ]
```

Precautions The columns that you reference in the HAVING clause must be used for grouping or contain an aggregate function. The HAVING clause must be used together with aggregate functions and the GROUP BY clause to display groups that only meet certain conditions after grouping based on GROUP BY. Example Group records in the CUSTOMER table and query the records whose account balance is greater than the specified value.

```
SELECT count(*), mktsegment, nationkey,
       CAST(sum(acctbal) AS bigint) AS totalbal
FROM customer GROUP BY mktsegment, nationkey HAVING sum(acctbal) > 5700000 ORDER BY totalbal DESC; _col0 | mktsegment | nationkey | totalbal -------+------------+-----------+----------
  1272 | AUTOMOBILE |        19 |  5856939
  1253 | FURNITURE  |        14 |  5794887
  1248 | FURNITURE  |         9 |  5784628
  1243 | FURNITURE  |        12 |  5757371
  1231 | HOUSEHOLD  |         3 |  5753216
  1251 | MACHINERY  |         2 |  5719140
  1247 | FURNITURE  |         8 |  5701952
```

#### 11.4.5 JOIN

Syntax

```
join_table:
    table_reference [INNER] JOIN table_factor [join_condition]
  | table_reference {LEFT|RIGHT|FULL} [OUTER] JOIN table_reference join_condition
  | table_reference CROSS JOIN table_reference [join_condition])
table_reference:
    table_factor
  | join_table
table_factor:
    tbl_name [alias]
  | table_subquery alias
  | ( table_references )
join_condition:
    ON expression
```

Example

```
select catgroup1, sold, unsold from (select catgroup, sum(qtysold) as sold from category c, event e, sales s where c.catid = e.catid and e.eventid = s.eventid group by catgroup) as a(catgroup1, sold) (select catgroup, sum(numtickets)-sum(qtysold) as unsold from category c, event e, sales s, listing l where c.catid = e.catid and e.eventid = s.eventid and s.listid = l.listid group by catgroup) as b(catgroup2, unsold) on a.catgroup1 = b.catgroup2 order by 1;
```

#### 11.4.6 LIMIT

You can use the LIMIT clause to specify the maximum number of rows to return in a query. Typically, you must specify one or two numbers in the LIMIT clause. The first number specifies the number of rows to skip from the beginning, and the second number specifies the maximum number of rows to return. Example Query the orders table and limit the number of rows to return to five by using the LIMIT clause.

```
SELECT orderdate FROM orders LIMIT 5; ------------o_orderdate -------------
 1996-04-14
 1992-01-15
 1995-02-01
 1995-11-12
 1992-04-26
```

Query the customer table and return the information of the third customer to the seventh customer sorted by the creation date.

```
SELECT * FROM customer ORDER BY create_date LIMIT 2,5;
```

#### 11.4.7 ORDER BY

You can use the ORDER BY clause to sort the query result. Each expression in the ORDER BY clause consists of column names or the sequence numbers (starting from 1) of columns. Syntax

```
[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ] [ LIMIT { count | ALL } ]
```

#### 11.4.8 Subqueries

The following example shows how to query the top ten sellers in ticket sales. The WHERE clause defines a table subquery, and the result of the subquery consists of multiple rows and one column. Not e The result of a table subquery can contain multiple rows and columns.

```
select firstname, lastname, cityname, max(qtysold) as maxsold from users join sales on users.userid=sales.sellerid where users.city not in(select venuecity from venue) group by firstname, lastname, city order by maxsold desc, city desc limit 10; firstname | lastname | cityname | maxsold -----------+----------+----------------+--------- Noah | Guerrero | Worcester | 8 Isadora | Moss | Winooski | 8 Kieran | Harrison | Westminster | 8 Heidi | Davis | Warwick | 8 Sara | Anthony | Waco | 8 Bree | Buck | Valdez | 8 Evangeline | Sampson | Trenton | 8 Kendall | Keith | Stillwater | 8 Bertha | Bishop | Stevens Point | 8 Patricia | Anderson | South Portland | 8
```

#### 11.4.9 UNION, INTERSECT, and EXCEPT

You can use the UNION, INTERSECT, and EXCEPT operators to combine multiple query result sets to a single result set. Syntax y

```
query { UNION [ ALL ] | INTERSECT | EXCEPT | MINUS } query
```

Parameters `UNION` : returns the union of two result sets. `UNION ALL` : returns the union of two result sets where duplicate rows are retained. The `ALL` keyword indicates that the duplicate rows are retained after the `UNION` calculation.

| INTERSECT : retur |   |   |   |
|---|---|---|---|
| EXCEPT \| |   | MINUS |   |
| The | MINUS |   | opera |

`INTERSECT` : returns the intersection of two result sets. `EXCEPT` | `MINUS` : returns rows that appear in the first result set, but not in the other result set. The `MINUS` operator is equivalent to the `EXCEPT` operator. Calculation sequence The `UNION` and `EXCEPT` operators are left-associative. That is, if you do not use parentheses () to change the calculation sequence, the calculation starts from left to right. For example, in the following statement, the `UNION` operator returns the union of T1 and T2. Then the `EXCEPT` operator returns the rows that appear only in the union returned by the `UNION` operator, but not T3.

```
 select * from t1
  union
  select * from t2
  except
  select * from t3
  order by c1;
```

In the same statement, the `INTERSECT` operator is prioritized over the `UNION` and `EXCEPT` operators. For example, the following statement finds the intersection of T2 and T3, and then the union of the intersection and T1.

```
 select * from t1
  union
  select * from t2
  intersect
  select * from t3
  order by c1;
```

You can use parentheses () to change the calculation sequence of these operators. For example, the following statement finds the union of T1 and T2, and then the intersection of the union and T3.

```
(select * from t1
  union
  select * from t2)
  intersect
  (select * from t3)
  order by c1;
```

### 11.5 CREATE USER

You can execute the CREATE USER statement to create an account. Syntax

```
    [if not exists] user [auth_option] [, [if not exists] user [auth_option]] ...
```

Precautions To create an account by executing the CREATE USER statement, you must have the `CREATE_USER` permission. Examples Create an account named account2 and set the password to Account2.

```
CREATE USER if not exists 'account2' IDENTIFIED BY 'Account2';
```

### 11.6 GRANT

You can execute the GRANT statement to grant permissions to an account. Syntax

```
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON priv_level
    TO user [auth_option]
    [WITH {GRANT OPTION}]
```

Parameters `priv_type` : the type of permission to grant. `column_list` : optional. If the `priv_type` parameter is set to `SELECT` , you can enter the names of columns to grant the `SELECT` permission on these columns. `priv_level` : the level of the permission to grant. `*. *` : the cluster level. `db_name. *` : the database level. `db_name.table_name` or `table_name` : the table level. Precautions To grant permissions to the other accounts by executing the `GRANT` statement, you must have the `GRANT OPTION` permission. Examples Grant the cluster-level `all` permission to account2.

```
GRANT all ON *. * TO 'account2';
```

Grant the database-level `all` permission to account3.

```
GRANT all ON adb_demo. * TO 'account3';
```

Execute the GRANT statement to create and grant permissions to an account. For example, create an account with the cluster-level data manipulation permissions.

```
GRANT insert,select,update,delete on *.* to 'test'@'%' identified by 'Testpassword1';
```

Create an account with the database-level data manipulation permissions.

```
GRANT insert,select,update,delete on adb_demo.* to 'test123' identified by 'Testpassword1 23';
```

Create an account that has the `SELECT` permission on the specified columns.

```
GRANT select (customer_id, sex) ON customer TO 'test321' identified by 'Testpassword321';
```

### 11.7 REVOKE

You can execute the REVOKE statement to revoke permissions from an account. Syntax

```
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    FROM user
```

Parameters `priv_type` : the type of permission to revoke. `column_list` : optional. If the `priv_type` parameter is set to `SELECT` , you can enter the names of columns to revoke the `SELECT` permission on these columns. `priv_level` : the level of the permission to revoke. `*. *` : the cluster level. `db_name. *` : the database level. `db_name.table_name` or `table_name` : the table level. Precautions To revoke permissions from other accounts by executing the REVOKE statement, you must have the `GRANT OPTION` permission. Examples Revoke the database-level `all` permission of account3.

```
REVOKE all ON adb_demo. * FROM 'account3';
```

### 11.8 Query users

AnalyticDB for MySQL is compatible with MySQL databases. AnalyticDB for MySQL provides a built-in database named MySQL, which stores user information, permission information, and stored procedures of AnalyticDB for MySQL. You can execute a SELECT statement to query user information of AnalyticDB for MySQL. Precautions In AnalyticDB for MySQL, only the privileged account can query user information. The privileged account in AnalyticDB for MySQL is equivalent to the root account in MySQL. Example

```
USE MYSQL; SELECT User, Host, Password FROM mysql.user; +---------+-----+--------------------------+
| User    | Host| Password                 |
+---------+-----+--------------------------+
| account1|  %  | *61f3777f02386598cd***** |
| account2|  %  | *0fe79c07e168cabc99***** |
```

### 11.9 RENAME USER

You can execute the RENAME USER statement to modify the name of an account. Syntax

```
RENAME USER old_user TO new_user [, old_user TO new_user] ...
```

Examples

```
RENAME USER account2 TO account_2; SELECT User, Host, Password FROM mysql.user; +----------+-----+----------------------- -+
| User     | Host| Password                |
+----------+-----+-------------------------+
| account2 | %   | *61f3777f02386598cda****|
| account_2| %   | *0fe79c07e168cabc99b****|
```

### 11.10 DROP USER

You can execute the DROP USER statement to delete an account. Syntax

```
DROP USER [if exists] user [, [if exists] user] ...
```

Precautions To delete an account by executing the DROP USER statement, you must have the `CREATE_USER` permission. Examples

```
DROP USER account_2;
```

### 11.11 SHOW

SHOW DATABASES You can execute the SHOW DATABASES statement to view the databases. Synt ax

```
SHOW DATABASES [EXTRA];
```

You can specify the `EXTRA` parameter to view extra information about the databases, such as the IDs of the creators and the connection information. Examples

```
SHOW DATABASES EXTRA; +--------------------+
| Database           |
+--------------------+
| adb_demo           |
| MYSQL              |
| INFORMATION_SCHEMA |
| adb_demo2          |
```

SHOW TABLES Synt ax You can execute the SHOW TABLES statement to view the tables in the current database.

```
SHOW TABLES [IN db_name];
```

Examples

```
SHOW TABLES IN adb_demo; +------------------------------+
| Tables_in_adb_demo           |
+------------------------------+
| customer                     |
| customer2                    |
| new_customer                 |
| test_table                   |
| v                            |
```

SHOW COLUMNS You can execute the SHOW COLUMNS statement to view the columns in a table. Synt ax

```
SHOW COLUMNS IN db_name.table_name;
```

Examples

```
SHOW COLUMNS IN adb_demo.test_table;
```

SHOW CREATE TABLE You can execute the SHOW CREATE TABLE statement to view the statement that is used to create a table. Synt ax

```
SHOW CREATE TABLE db_name.table_name;
```

Examples

```
SHOW CREATE TABLE adb_demo.customer;
```

SHOW GRANTS You can execute the SHOW GRANTS statement to view the permissions that are granted to the current account. Synt ax

```
SHOW GRANTS;
```

## 12 System functions

This topic describes the system functions supported by AnalyticDB for MySQL.

### 12.1 Aggregate functions

The aggregate functions described in this topic use the testtable table as test data.

```
create table testtable(a int) distributed by hash(a); insert into testtable values (1),(2),(3);
```

#### 12.1.1 AVG

This function calculates the average value of all input values.

```
AVG(bigint x) AVG(double x) AVG(float x)
```

Return value type: DOUBLE.

```
  select avg(a) from testtable;
  +--------+
  | avg(a) |
  +--------+
  |    2.0 |
```

#### 12.1.2 BIT_AND

This function returns the result of bitwise AND of all bits in the parameter.

```
BIT_AND(float x) BIT_AND(bigint x) BIT_AND(double x)
```

Return value type: BIGINT.

```
  select bit_and(a) from testtable;
  +------------+
  | bit_and(a) |
  +------------+
  |          0 |
```

#### 12.1.3 BIT_OR

This function returns the result of bitwise OR of all bits in the parameter.

```
BIT_OR(float x) BIT_OR(bigint x) BIT_OR(double x)
```

Return value type: BIGINT.

```
  select bit_or(a) from testtable;
  +----------------------------+
  |          bit_or(a)         |
  +----------------------------+
  |           3                |
```

#### 12.1.4 BIT_XOR

This function returns the result of bitwise XOR of all bits in the parameter.

```
BIT_XOR(double x) BIT_XOR(bigint x) bit_xor(float x)
```

Return value type: BIGINT.

```
  select bit_xor(a) from testtable;
  +----------------------------+
  |          bit_xor(a)        |
  +----------------------------+
  |          0                 |
```

#### 12.1.5 COUNT

This function counts the number of records.

```
COUNT([distinct|all] value x)
```

Description: distinct and all specify whether to exclude duplicate records in the counting process. The default value is all, indicating that all records are counted. If distinct is specified, only records with distinct values are counted. Return value type: BIGINT.

```
  select count(distinct a) from testtable;
  +-------------------+
  | count(DISTINCT a) |
  +-------------------+
  |                 3 |
```

#### 12.1.6 MAX

This function returns the maximum value of all input values.

```
MAX(value x)
```

Description: value can be of any data type. However, data of the BOOLEAN type is not supported in the calculation. If the value for a row in the specified column is null, this row is ignored. Return value type: LONG.

```
  select max(a) from testtable;
  +--------+
  | max(a) |
  +--------+
  |      3 |
```

#### 12.1.7 MIN

This function returns the minimum value of all input values.

```
MIN(value x)
```

Description: value can be of any data type. However, data of the BOOLEAN type is not supported in the calculation. If the value for a row in the specified column is null, this row is ignored. Return value type: LONG.

```
  select min(a) from testtable;
  +--------+
  | min(a) |
  +--------+
  |      1 |
```

#### 12.1.8 STD/STDDEV

This function returns the sample standard deviation of all input values.

```
STD(double x) STD(bigint x) STDDEV(double x) STDDEV(bigint x)
```

Return value type: DOUBLE.

```
  select std(a) from testtable;
  +-------------------+
  | std(a)            |
  +-------------------+
  | 0.816496580927726 |
```

#### 12.1.9 STDDEV_POP

This function returns the population standard deviation of all input values.

```
STDDEV_POP(double x) STDDEV_POP(bigint x)
```

Return value type: DOUBLE.

```
  select stddev_pop(a) from testtable;
  +----------------------------+
  |    stddev_pop(a)           |
  +----------------------------+
  |    0.816496580927726       |
```

#### 12.1.10 STDDEV_SAMP

This function returns the population standard deviation for a group of integers, decimals, or floatingpoint numbers.

```
STDDEV_SAMP(double x) STDDEV_SAMP(bigint x)
```

Return value type: DOUBLE.

```
  select stddev_samp(a) from testtable;
  +----------------------------+
  |     stddev_samp(a)         |
  +----------------------------+
  |         1.0                |
```

#### 12.1.11 SUM

This function calculates the sum of all input values.

```
SUM(double x) SUM(float x) SUM(bigint x)
```

Return value type: BIGINT.

```
  select sum(a) from testtable;
  +----------------------------+
  |         sum(a)             |
  +----------------------------+
  |          6                 |
```

#### 12.1.12 VAR_POP

This function returns the population variance for a group of integers, decimals, or floating-point numbers.

```
VAR_POP(double x) VAR_POP(bigint x)
```

| o use the | VARIANCE() |   |
|---|---|---|
| VARIANCE() |   | function i |

found, `VAR_POP()` returns the value NULL. Return value type: DOUBLE.

```
  select var_pop(a)  from testtable;
  +----------------------------+
  |         var_pop(a)         |
  +----------------------------+
  |   0.6666666666666666       |
```

#### 12.1.13 VAR_SAMP

This function returns the sample variance for a group of integers, decimals, or floating-point numbers.

```
VAR_SAMP(double x) VAR_SAMP(bigint x)
```

Return value type: DOUBLE.

```
  select var_samp(a)  from testtable;
  +----------------------------+
  |         var_samp(a)        |
  +----------------------------+
  |            1.0             |
```

#### 12.1.14 VARIANCE

This function returns the population variance for a group of integers, decimals, or floating-point numbers.

```
VARIANCE(double x) VARIANCE(bigint x)
```

Description: The `VARIANCE()` function is an extension to standard SQL and can be replaced by the standard SQL function `VAR_POP()` . If no matches are found, `VARIANCE()` returns the value NULL. Return value type: DOUBLE.

```
  select variance(a)  from testtable;
  +----------------------------+
  |         variance(a)        |
  +----------------------------+
  |    0.6666666666666666      |
```

### 12.2 Date and time functions

#### 12.2.1 ADDDATE/DATE_ADD

This function adds an interval to a specified date.

```
ADDDATE(date,INTERVAL expr unit) ADDDATE(expr,days)
```

Description: Valid values of unit: second, minute, hour, day, month, year, minute_second, hour_second, hour_minute, day_second, day_minute, day_hour, and year_month. Default value of unit: day. days and expr: This function returns the value of expr plus days. Parameter types:

```
  adddate(date, INTERVAL expr unit)
  adddate(timestamp, INTERVAL expr unit)
  adddate(datetime, INTERVAL expr unit)
  adddate(varchar, INTERVAL expr unit)
  adddate(date, varchar)
  adddate(date, bigint)
  adddate(datetime, bigint)
  adddate(datetime, varchar)
  adddate(timestamp, varchar)
  adddate(timestamp, bigint)
  adddate(varchar, bigint)
  adddate(varchar, varchar)
```

Return value type: DATE.

```
  select adddate(date '2001-1-22',interval '3' day);
  +----------------------------------------------+
  | adddate(DATE '2001-1-22', INTERVAL  '3' DAY) |
  +----------------------------------------------+
  | 2001-01-25                                   |
```

```
  select adddate(timestamp '2001-1-22',interval '3' day);
  +---------------------------------------------------+
  | adddate(TIMESTAMP '2001-1-22', INTERVAL  '3' DAY) |
  +---------------------------------------------------+
  | 2001-01-25 00:00:00                               |
  select adddate(datetime '2001-1-22',interval '3' day);
  +--------------------------------------------------+
  | adddate(DATETIME '2001-1-22', INTERVAL  '3' DAY) |
  +--------------------------------------------------+
  | 2001-01-25 00:00:00                              |
  select adddate('2001-1-22',interval '3' day);
  +-----------------------------------------+
  | adddate('2001-1-22', INTERVAL  '3' DAY) |
  +-----------------------------------------+
  | 2001-01-25                              |
  select adddate(datetime '2001-1-22',interval '3' second);
  +-----------------------------------------------------+
  | adddate(DATETIME '2001-1-22', INTERVAL  '3' SECOND) |
  +-----------------------------------------------------+
  |                                 2001-01-22 00:00:03 |
```

#### 12.2.2 ADDTIME

This function adds time to a specified time. That is, this function returns the result of expr1 plus expr2.

```
ADDTIME(expr1,expr2)
```

Parameter types:

```
  addtime(date,varchar)
  addtime(time,varchar)
  addtime(datetime,varchar)
  addtime(timestamp,varchar)
  addtime(varchar,varchar)
```

Return value type: VARCHAR.

```
  select addtime(date '1998-01-01','01:01:01');
  +----------------------------------------+
  | addtime(DATE '1998-01-01', '01:01:01') |
  +----------------------------------------+
  | 1998-01-01 01:01:01                    |
```

#### 12.2.3 CONVERT_TZ

This function converts the value of dt from from_tz to to_tz and returns the result.

```
CONVERT_TZ(dt,from_tz,to_tz)
```

Parameter types:

```
  convert_tz(varchar, varchar, varchar)
```

Return value type: DATETIME.

```
  select convert_tz('2004-01-01 12:00:00','+00:00','+10:00');
  +-------------------------------------------------------+
  | convert_tz('2004-01-01 12:00:00', '+00:00', '+10:00') |
  +-------------------------------------------------------+
  |                                   2004-01-01 22:00:00 |
```

#### 12.2.4 CURDATE

This function returns the current date.

```
CURDATE()
```

Return value type: DATE.

```
  select curdate;
  +------------+
  | curdate()  |
  +------------+
  | 2019-05-25 |
```

#### 12.2.5 CURTIME

This function returns the current time.

```
CURTIME()
```

Return value type: TIME.

```
  select curtime();
  +--------------+
  | curtime()    |
  +--------------+
  | 14:39:22.109 |
```

#### 12.2.6 DATE

This function returns the date part of a date or datetime expression.

```
DATE(expr)
```

Parameter types:

```
  date(timestamp)
  date(datetime)
  date(varchar)
```

Return value type: DATE.

```
  select date(timestamp '2003-12-31 01:02:03');
  +---------------------------------------+
  | date(TIMESTAMP '2003-12-31 01:02:03') |
  +---------------------------------------+
  | 2003-12-31                            |
```

#### 12.2.7 DATE_FORMAT

This function returns a date as a string in the specified format.

```
DATE_FORMAT(date,format)
```

Description: The following table describes the format specifiers.

| Specifier | Description |
|---|---|
| %a | The abbreviation of a day of a week. Valid values: Sun to Sat. |
| %b | The abbreviation of a month name. Valid values: Jan to Dec. |
| %c | The month in numeric format. Valid values: 0 to 12. |
| %d | The day of the month in numeric format. Valid values: 00 to 31. |
| %e | The day of the month in numeric format. Valid values: 0 to 31. |
| %f | The microseconds. Valid values: 000000 to 999999. |
| %H | The hour. Valid values: 00 to 23. |
| %h | The hour. Valid values: 01 to 12. |
| %I | The hour. Valid values: 01 to 12. |
| %i | The minutes in numeric format. Valid values: 00 to 59. |

| r Guide·System functions | AnalyticDB for MySQ |
|---|---|

| Specifier | Description |
|---|---|
| %j | The day of the year. Valid values: 001 to 366. |
| %k | The hour. Valid values: 0 to 23. |
| %l | The hour. Valid values: 1 to 12. |
| %M | The name of the month. Valid values: January to December. |
| %m | The month in numeric format. Valid values: 00 to 12. |
| %p | The abbreviation of a time period in 12-hour format. Valid values: AM and PM. |
| %r | The time in 12-hour format (hh:mm:ss AM or hh:mm:ss PM). |
| %S | The seconds. Valid values: 00 to 59. |
| %s | The seconds. Valid values: 00 to 59. |
| %T | The time in 24-hour format (hh:mm:ss). |
| %v | The week number. Monday is the first day of a week. This specifier applies to WEEK() mode 3 and is used with %x. |
| %W | The name of the weekday. Valid values: Sunday to Saturday. |
| %x | The year of the week in numeric format. Monday is the first day of a week. This specifier is used with %v, and the value contains four digits. |
| %Y | The year of the week in numeric format. The value contains four digits. |
| %y | The year of the week in numeric format. The value contains two digits. |
| %% | The percent sign (%). |
| %x | x, for any "x" not listed above. |

Parameter types:

```
    date_format(timestamp, varchar)
  date_format(varchar, varchar)
  date_format(datetime, varchar)
  date_format(date, varchar)
```

Return value type: VARCHAR.

```
  select date_format(timestamp '2019-05-27 13:23:00', '%W %M %Y')as result;
  +-----------------+
  | result          |
  +-----------------+
  | Monday May 2019 |
```

#### 12.2.8 SUBDATE/DATE_SUB

This function returns the value of date minus the specified INTERVAL.

```
DATE_SUB(date,INTERVAL expr unit)
```

Description: Valid values of unit: second, minute, hour, day, month, year, minute_second, hour_second, hour_minute, day_second, day_minute, day_hour, and year_month. Default value of unit: day. Parameter types:

```
  subdate(date, INTERVAL expr unit)
  subdate(timestamp, INTERVAL expr unit)
  subdate(datetime, INTERVAL expr unit)
  subdate(varchar, INTERVAL expr unit)
  subdate(date, bigint)
  subdate(date, varchar)
  subdate(datetime, bigint)
  subdate(datetime, varchar)
  subdate(timestamp, bigint)
  subdate(timestamp, varchar)
  subdate(varchar, bigint)
  subdate(varchar, varchar)
```

Return value type: DATE.

```
  select date_sub(date '2001-1-22',interval '3' day);
  +-----------------------------------------------+
  | date_sub(DATE '2001-1-22', INTERVAL  '3' DAY) |
  +-----------------------------------------------+
  | 2001-01-19                                    |
```

#### 12.2.9 DATEDIFF

This function returns the number of days between expr1 and expr2.

```
DATEDIFF(expr1,expr2)
```

Parameter types:

```
 datediff(varchar, varchar)
  datediff(datetime, varchar)
  datediff(varchar, datetime)
  datediff(datetime, datetime)
  datediff(varchar, timestamp)
  datediff(timestamp, timestamp)
  datediff(timestamp, varchar)
  datediff(date, date)
  datediff(date, varchar)
  datediff(varchar, date)
```

Return value type: BIGINT.

```
 select datediff('2007-12-31 23:59:59','2007-12-30');
  +-----------------------------------------------+
  | datediff('2007-12-31 23:59:59', '2007-12-30') |
  +-----------------------------------------------+
  |                                             1 |
```

#### 12.2.10 DAY/DAYOFMONTH

This function returns the day in date. Valid values: `[1,31]` .

```
DAY(date) DAYOFMONTH(date)
```

Parameter types:

```
  dayofmonth(timestamp)
  dayofmonth(datetime)
  dayofmonth(date)
  dayofmonth(time)
  dayofmonth(varchar)
```

Return value type: BIGINT.

```
select dayofmonth(timestamp '2007-02-03 12:23:09');
  +---------------------------------------------+
  | dayofmonth(TIMESTAMP '2007-02-03 12:23:09') |
  +---------------------------------------------+
  |                                           3 |
```

#### 12.2.11 DAYNAME

This function returns the day of the week for a date, such as Monday.

```
DAYNAME(date)
```

Parameter types:

```
  dayname(timestamp)
  dayname(datetime)
  dayname(date)
  dayname(varchar)
```

Return value type: VARCHAR.

```
  select dayname(timestamp '2007-02-03 00:00:00');
  +------------------------------------------+
  | dayname(TIMESTAMP '2007-02-03 00:00:00') |
  +------------------------------------------+
  | Saturday                                 |
```

#### 12.2.12 DAYOFWEEK

This function returns the weekday index for a date. For example, the weekday indexes for Sunday, Monday, and Saturday are 1, 2, and 7, respectively.

```
DAYOFWEEK(date)
```

Parameter types:

```
  dayofweek(timestamp)
  dayofweek(datetime)
  dayofweek(date)
  dayofweek(varchar)
```

Return value type: BIGINT.

```
  select dayofweek(timestamp '2007-02-03 00:00:00');
  +--------------------------------------------+
  | dayofweek(TIMESTAMP '2007-02-03 00:00:00') |
  +--------------------------------------------+
  |                                          7 |
```

#### 12.2.13 DAYOFYEAR

This function returns the day of the year for a date. Valid values: `[1,366]` .

```
DAYOFYEAR(date)
```

Parameter types:

```
  dayofyear(timestamp)
  dayofyear(datetime)
  dayofyear(date)
  dayofyear(varchar)
```

Return value type: BIGINT.

```
  select dayofyear(timestamp '2007-02-03 00:12:12');
  +--------------------------------------------+
  | dayofyear(TIMESTAMP '2007-02-03 00:12:12') |
  +--------------------------------------------+
  |                                         34 |
```

#### 12.2.14 EXTRACT

This function returns a part of a date or time, which is specified by unit. For example, this function can return the year, month, day, hour, or minute of a date or time.

```
EXTRACT(unit FROM date)
```

Valid values of unit: second, minute, hour, day, month, year, minute_second, hour_second, hour_minute, day_second, day_minute, day_hour, and year_month. Supported parameter types: VARCHAR, TIMESTAMP, DATETIME, and TIME. Return value type: BIGINT.

```
  select extract(second from '2019-07-02 00:12:34');
  +-------+
  | _col0 |
  +-------+
  |    34 |
```

#### 12.2.15 FROM_DAYS

This function returns a DATE value based on the parameter N indicating the number of days.

```
FROM_DAYS(N)
```

Parameter types:

```
  from_days(varchar)
  from_days(bigint)
```

Return value type: DATE.

```
  select from_days(730669);
  +-------------------+
  | from_days(730669) |
  +-------------------+
  | 2000-07-03        |
```

#### 12.2.16 FROM_UNIXTIME

This function returns a Unix timestamp in the specified format.

```
FROM_UNIXTIME(unix_timestamp[,format])
```

Description: The format parameter conforms to the format in the DATE_FORMAT function. Parameter types:

```
  from_unixtime(varchar, varchar)
  from_unixtime(varchar)
  from_unixtime(double, varchar)
  from_unixtime(double)
```

Return value type: DATETIME.

```
 select from_unixtime('1447430881','%Y %M %h:%i:%s %x');
  +--------------------------------------------------+
  | from_unixtime('1447430881', '%Y %M %h:%i:%s %x') |
  +--------------------------------------------------+
  | 2015 November 12:08:01 2015                      |
```

#### 12.2.17 HOUR

This function returns the hour part of a specified time.

```
HOUR(time)
```

Parameter types:

```
  hour(timestamp)
  hour(datetime)
  hour(date)
  hour(time)
  hour(varchar)
```

Return value type: BIGINT.

```
  select hour(timestamp '2019-12-07 10:05:03');
  +---------------------------------------+
  | hour(TIMESTAMP '2019-12-07 10:05:03') |
  +---------------------------------------+
  |                                    10 |
```

#### 12.2.18 LAST_DAY

This function returns the last day of the month for a date or datetime.

```
LAST_DAY(date)
```

Parameter types:

```
  last_day(varchar)
  last_day(timestamp)
  last_day(datetime)
  last_day(date)
```

Return value type: DATE.

```
  select last_day('2003-02-05');
  +------------------------+
  | last_day('2003-02-05') |
  +------------------------+
  | 2003-02-28             |
```

#### 12.2.19 LOCALTIME/LOCALTIMESTAMP/NOW

This function returns the current timestamp.

```
localtime localtime() localtimestamp localtimestamp() now()
```

Return value type: DATETIME.

```
  select now();
  +---------------------+
  | now()              |
  +---------------------+
  | 2019-05-25 00:28:37 |
```

#### 12.2.20 MAKEDATE

This function returns a date based on the year and dayofyear parameters.

```
MAKEDATE(year,dayofyear)
```

Parameter types:

```
  makedate(bigint, bigint)
  makedate(varchar, varchar)
```

Return value type: DATE.

```
  select makedate(2011,31), makedate(2011,32);
  +--------------------+--------------------+
  | makedate(2011, 31) | makedate(2011, 32) |
  +--------------------+--------------------+
  | 2011-01-31         | 2011-02-01         |
```

#### 12.2.21 MAKETIME

This function returns a time based on the hour, minute, and second parameters.

```
MAKETIME(hour,minute,second)
```

Parameter types:

```
  maketime(bigint, bigint, bigint)
  maketime(varchar, varchar, varchar)
```

Return value type: TIME.

```
  select maketime(12,15,30);
  +----------------------+
  | maketime(12, 15, 30) |
  +----------------------+
  | 12:15:30             |
```

#### 12.2.22 MINUTE

This function returns the minute part of a specified time.

```
MINUTE(time)
```

Parameter types:

```
  minute(timestamp)
  minute(datetime)
  minute(date)
  minute(time)
  minute(varchar)
```

Return value type: BIGINT.

```
  select minute(timestamp '2008-02-03 10:05:03');
  +-----------------------------------------+
  | minute(TIMESTAMP '2008-02-03 10:05:03') |
  +-----------------------------------------+
  |                                       5 |
```

#### 12.2.23 MONTH

This function returns the month for a date.

```
MONTH(date)
```

Parameter types:

```
  month(timestamp)
  month(datetime)
  month(date)
  month(time)
  month(varchar)
```

Return value type: BIGINT.

```
  select month(timestamp '2008-02-03 00:00:00');
  +----------------------------------------+
  | month(TIMESTAMP '2008-02-03 00:00:00') |
  +----------------------------------------+
  |                                      2 |
```

#### 12.2.24 MONTHNAME

This function returns the full name of the month for a date.

```
MONTHNAME(date)
```

Parameter types:

```
  monthname(timestamp)
  monthname(datetime)
  monthname(date)
  monthname(varchar)
```

Return value type: VARCHAR.

```
  select monthname(datetime '2008-02-03 00:00:00');
  +-------------------------------------------+
  | monthname(DATETIME '2008-02-03 00:00:00') |
  +-------------------------------------------+
  | February                                  |
```

#### 12.2.25 PERIOD_ADD

This function adds N months to period P.

```
PERIOD_ADD(P,N)
```

Parameter types:

```
  period_add(bigint, bigint)
  period_add(varchar, varchar)
  period_add(varchar, bigint)
```

Return value type: BIGINT.

```
  select period_add(200801,2);
  +-----------------------+
  | period_add(200801, 2) |
  +-----------------------+
  |                200803 |
```

#### 12.2.26 PERIOD_DIFF

This function returns the number of months between periods P1 and P2.

```
PERIOD_DIFF(P1,P2)
```

Parameter types:

```
  period_diff(bigint, bigint)
  period_diff(varchar, varchar)
```

Return value type: BIGINT.

```
  select period_diff(200802,200703);
  +-----------------------------+
  | period_diff(200802, 200703) |
  +-----------------------------+
  |                          11 |
```

#### 12.2.27 QUARTER

This function returns the quarter of the year for a date. Valid values: `[1,4]` .

```
QUARTER(date)
```

Parameter types:

```
  quarter(datetime)
  quarter(varchar)
  quarter(timestamp)
  quarter(date)
```

Return value type: BIGINT.

```
  select quarter(datetime '2008-04-01 12:12:12');
  +-----------------------------------------+
  | quarter(DATETIME '2008-04-01 12:12:12') |
  +-----------------------------------------+
  |                                       2 |
```

#### 12.2.28 SEC_TO_TIME

This function converts seconds to time.

```
SEC_TO_TIME(seconds)
```

Parameter types:

```
  sec_to_time(bigint)
  sec_to_time(varchar)
```

Return value type: TIME.

```
  select sec_to_time(2378);
  +-------------------+
  | sec_to_time(2378) |
  +-------------------+
  | 00:39:38          |
```

#### 12.2.29 SECOND

This function returns the second part of a specified time. Valid values: `[0,59]` .

```
SECOND(time)
```

Parameter types:

```
  second(timestamp)
  second(datetime)
  second(date)
  second(time)
  second(varchar)
```

Return value type: BIGINT.

```
  select second(timestamp '2019-03-12 12:13:14');
  +-----------------------------------------+
  | second(TIMESTAMP '2019-03-12 12:13:14') |
  +-----------------------------------------+
  |                                      14 |
```

#### 12.2.30 STR_TO_DATE

This function converts a string to a date or datetime in the specified format.

```
STR_TO_DATE(str,format)
```

Parameter types:

```
  str_to_date(varchar, varchar)
```

Return value type: DATETIME.

```
  select str_to_date('2017-01-06 10:20:30','%Y-%m-%d %H:%i:%s') as result;
  +---------------------+
  | result              |
  +---------------------+
  | 2017-01-06 10:20:30 |
```

#### 12.2.31 SUBTIME

This function subtracts expr2 from expr1.

```
SUBTIME(expr1,expr2)
```

Parameter types:

```
  subtime(date, varchar)
  subtime(datetime, varchar)
  subtime(timestamp, varchar)
  subtime(time, varchar)
  subtime(varchar, varchar)
```

Return value type: DATETIME.

```
  select subtime(date '2018-10-31','0:1:1');
  +-------------------------------------+
  | subtime(DATE '2018-10-31', '0:1:1') |
  +-------------------------------------+
  |                 2018-10-30 23:58:59 |
```

#### 12.2.32 SYSDATE

This function returns the system time.

```
SYSDATE()
```

Return value type: DATETIME.

```
 select sysdate();
  +---------------------+
  | sysdate()           |
  +---------------------+
  | 2019-05-26 00:47:21 |
```

#### 12.2.33 TIME

This function returns the time in expr as a string.

```
TIME(expr)
```

Parameter types:

```
  time(varchar)
  time(datetime)
  time(timestamp)
```

Return value type: VARCHAR.

```
  select time('2003-12-31 01:02:03');
  +-----------------------------+
  | time('2003-12-31 01:02:03') |
  +-----------------------------+
  | 01:02:03                    |
```

#### 12.2.34 TIME_FORMAT

This function returns time as a string in the specified format.

```
TIME_FORMAT(time,format)
```

Description: The format parameter conforms to the format in the DATE_FORMAT function. Parameter types:

```
  time_format(varchar, varchar)
  time_format(timestamp, varchar)
  time_format(datetime, varchar)
  time_format(time, varchar)
  time_format(date, varchar)
```

Return value type: VARCHAR.

```
  select time_format('12:00:00', '%H %k %h %I %l');
  +-------------------------------------------+
  | time_format('12:00:00', '%H %k %h %I %l') |
  +-------------------------------------------+
  | 12 12 12 12 12                            |
```

#### 12.2.35 TIME_TO_SEC

This function converts time to seconds.

```
TIME_TO_SEC(time)
```

Parameter types:

```
  time_to_sec(varchar)
  time_to_sec(datetime)
  time_to_sec(timestamp)
  time_to_sec(date)
  time_to_sec(time)
```

Return value type: BIGINT.

```
  select time_to_sec(datetime '2009-12-12 22:23:00');
  +---------------------------------------------+
  | time_to_sec(DATETIME '2009-12-12 22:23:00') |
  +---------------------------------------------+
  |                                       80580 |
```

#### 12.2.36 TIMEDIFF

This function subtracts expr2 from expr1.

```
TIMEDIFF(expr1,expr2)
```

Parameter types:

```
  timediff(time, varchar)
  timediff(time, time)
  timediff(varchar, varchar)
```

Return value type: DATETIME.

```
  select timediff(time '12:00:00','10:00:00');
  +---------------------------------------+
  | timediff(TIME '12:00:00', '10:00:00') |
  +---------------------------------------+
  | 02:00:00                              |
```

#### 12.2.37 TIMESTAMP

This function returns expr as a datetime value.

```
TIMESTAMP(expr)
```

Parameter types:

```
  timestamp(date)
  timestamp(varchar)
```

Return value type: DATETIME.

```
  select timestamp(date '2019-05-27');
  +------------------------------+
  | timestamp(DATE '2019-05-27') |
  +------------------------------+
  | 2019-05-27 00:00:00          |
```

#### 12.2.38 TIMESTAMPADD

This function adds interval to datetime_expr.

```
TIMESTAMPADD(unit,interval,datetime_expr)
```

Description: unit specifies the unit of interval. Valid values of unit: second, minute, hour, day, week, month, quarter, and year. Parameter types:

```
  timestampadd(varchar, varchar, timestamp)
  timestampadd(varchar, bigint, timestamp)
  timestampadd(varchar, varchar, date)
  timestampadd(varchar, bigint, date)
  timestampadd(varchar, varchar, datetime)
  timestampadd(varchar, bigint, datetime)
  timestampadd(varchar, varchar, varchar)
  timestampadd(varchar, bigint, varchar)
```

Return value type: DATETIME.

```
 select timestampadd(second,'1',timestamp '2003-01-02 12:12:12')as result;
  +---------------------+
  | result              |
  +---------------------+
  | 2003-01-02 12:12:13 |
```

#### 12.2.39 TIMESTAMPDIFF

This function subtracts datetime_expr2 from datetime_expr1. unit specifies the unit of the result.

```
TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2)
```

Description: Valid values of unit: second, minute, hour, day, week, month, quarter, and year. Use this function in the same way as the TIMESTAMPADD function. Parameter types:

```
  timestampdiff(varchar, timestamp, timestamp)
  timestampdiff(varchar, date, date)
  timestampdiff(varchar, datetime, datetime)
  timestampdiff(varchar, varchar, varchar)
```

Return value type: BIGINT.

```
  select timestampdiff(second,datetime '2003-02-01 10:12:13',datetime '2003-05-01 10:12:1
3')as result;
  +---------+
  | result  |
  +---------+
  | 7689600 |
```

#### 12.2.40 TO_DAYS

This function returns the number of days since year 0 based on date.

```
TO_DAYS(date)
```

Parameter types:

```
  to_days(date)
  to_days(time)
  to_days(varchar)
  to_days(timestamp)
  to_days(datetime)
```

Return value type: BIGINT.

```
  select to_days(date '2018-12-12');
  +----------------------------+
  | to_days(DATE '2018-12-12') |
  +----------------------------+
  |                     737405 |
```

#### 12.2.41 TO_SECONDS

This function returns the number of seconds since year 0 based on expr.

```
TO_SECONDS(expr)
```

Parameter types:

```
  to_seconds(date)
  to_seconds(datetime)
  to_seconds(timestamp)
  to_seconds(varchar)
  to_seconds(time)
```

Return value type: BIGINT.

```
   select to_seconds(date '2019-09-08');
  +-------------------------------+
  | to_seconds(DATE '2019-09-08') |
  +-------------------------------+
  |                   63735120000 |
```

#### 12.2.42 UNIX_TIMESTAMP

UNIX_TIMESTAMP returns the Unix timestamp for the current time in seconds since `'1970-01-01` `00:00:00'` UTC.

```
UNIX_TIMESTAMP([date])
```

| iption: | UNIX TIMESTAMP(date) _ |   |
|---|---|---|
| '1970-01-01 00:00:00' |   | UTC. |

Description: `UNIX_TIMESTAMP(date)` returns the Unix timestamp for the date parameter in seconds Parameter types:

```
 unix_timestamp()
  unix_timestamp(varchar)
  unix_timestamp(timestamp)
  unix_timestamp(date)
  unix_timestamp(datetime)
```

Return value type: BIGINT.

```
  select unix_timestamp();
  +------------------+
  | unix_timestamp() |
  +------------------+
  |       1558935850 |
```

#### 12.2.43 UTC_DATE

This function returns the UTC date.

```
UTC_DATE()
```

Return value type: VARCHAR.

```
  select utc_date();
  +------------+
  | utc_date() |
  +------------+
  | 2019-05-27 |
```

#### 12.2.44 UTC_TIME

This function returns the UTC time.

```
UTC_TIME()
```

Return value type: VARCHAR.

```
   select utc_time();
  +------------+
  | utc_time() |
  +------------+
  | 05:53:19   |
```

#### 12.2.45 UTC_TIMESTAMP

This function returns the UTC timestamp.

```
utc_timestamp()
```

Return value type: VARCHAR.

```
  select utc_timestamp();
  +---------------------+
  | utc_timestamp()     |
  +---------------------+
  | 2019-05-27 05:55:15 |
```

#### 12.2.46 WEEK

This function returns the week number for date, which is the week to which date belongs in the year.

```
WEEK(date[,mode])
```

Description: date specifies the date for which you want to obtain the week number. mode is an optional parameter that specifies the logic for calculating the week number. It allows you to specify whether the week starts from Monday or Sunday. The returned value ranges from 0 to 52 or from 1 to 53. The following table describes the formats that mode supports.

| Mode | First day of the week | Range |
|---|---|---|
| 0 | Sunday | 0 to 53 |
| 1 | Monday | 0 to 53 |
| 2 | Sunday | 1 to 53 |
| 3 | Monday | 1 to 53 |
| 4 | Sunday | 0 to 53 |
| 5 | Monday | 0 to 53 |
| 6 | Sunday | 1 to 53 |
| 7 | Monday | 1 to 53 |

Parameter types:

```
 week(varchar)
  week(varchar, bigint)
  week(date)
  week(date, bigint)
  week(datetime)
  week(datetime, bigint)
  week(timestamp)
  week(timestamp, bigint)
```

Return value type: BIGINT.

```
  select week('2019-05-27');
  +--------------------+
  | week('2019-05-27') |
  +--------------------+
  |                 21 |
```

#### 12.2.47 WEEKDAY

This function returns the weekday for date. The result is an integer indicating the weekday. The mapping is as follows: `0 = Monday` , `1 = Tuesday` , and `6 = Sunday` .

```
WEEKDAY(date)
```

Parameter types:

```
  weekday(timestamp)
  weekday(datetime)
  weekday(date)
  weekday(varchar)
```

Return value type: BIGINT.

```
  select weekday(timestamp '2019-05-27 00:09:00');
  +------------------------------------------+
  | weekday(TIMESTAMP '2019-05-27 00:09:00') |
  +------------------------------------------+
  |                                        0 |
```

#### 12.2.48 WEEKOFYEAR

This function returns the calendar week for date. Valid values: `[1, 53]` .

```
WEEKOFYEAR(date)
```

Parameter types:

```
  weekofyear(timestamp)
  weekofyear(datetime)
  weekofyear(date)
  weekofyear(varchar)
```

Return value type: BIGINT.

```
  select weekofyear(timestamp '2019-05-27 09:00:00');
  +---------------------------------------------+
  | weekofyear(TIMESTAMP '2019-05-27 09:00:00') |
  +---------------------------------------------+
  |                                          22 |
```

#### 12.2.49 YEAR

This function returns the year for date.

```
YEAR(date)
```

Parameter types:

```
  year(timestamp)
  year(datetime)
  year(date)
  year(time)
  year(varchar)
```

Return value type: BIGINT.

```
  select year(timestamp '2019-05-27 00:00:00');
  +---------------------------------------+
  | year(TIMESTAMP '2019-05-27 00:00:00') |
  +---------------------------------------+
  |                                  2019 |
```

#### 12.2.50 YEARWEEK

This function returns the year and week for a date.

```
YEARWEEK(date) YEARWEEK(date,mode)
```

Description: The year in the result may be different from the year in the date parameter for the first and the last week of the year. mode works in the same way as mode in the WEEK function. For the single-parameter syntax, the value of mode is 0. Parameter types:

```
  yearweek(timestamp)
  yearweek(timestamp, bigint)
  yearweek(datetime)
  yearweek(datetime, bigint)
  yearweek(date, bigint)
  yearweek(date)
  yearweek(varchar)
  yearweek(varchar, bigint)
```

Return value type: BIGINT.

```
 select yearweek(timestamp '2019-05-27 00:00:00');
  +-------------------------------------------+
  | yearweek(TIMESTAMP '2019-05-27 00:00:00') |
  +-------------------------------------------+
  |                                    201921 |
```

### 12.3 String functions

#### 12.3.1 ASCII

This function returns the decimal ASCII code of the str character or the leftmost character in the string str.

```
ASCII(varchar str)
```

Return value type: BIGINT.

```
  select ascii('2');
  +------------+
  | ascii('2') |
  +------------+
  |         50 |
```

#### 12.3.2 BIN

This function returns the binary string of the integer N.

```
BIN(bigint N)
```

Description: If N is null, null is returned. Return value type: VARCHAR.

```
  select bin(12);
  +---------+
  | bin(12) |
  +---------+
  | 1100    |
```

#### 12.3.3 BIT_LENGTH

This function returns the length of the string str, measured in bits.

```
BIT_LENGTH(varchar str)
```

Return value type: BIGINT.

```
  select bit_length('text');
  +--------------------+
  | bit_length('text') |
  +--------------------+
  |                 32 |
```

#### 12.3.4 CHAR

This function returns a string of decimal ASCII codes of the integers N1, N2, and so on.

```
CHAR(bigint N1, bigint N2...)
```

Return value type: VARBINARY.

```
  select char(97,110,97,108,121,116,105,99,100,98);
  +----------------------------------------------------+
  | char(97, 110, 97, 108, 121, 116, 105, 99, 100, 98) |
  +----------------------------------------------------+
  | analyticdb                                         |
```

#### 12.3.5 CHAR_LENGTH/CHARACTER_LENGTH

This function returns the length of the string str, measured in characters.

```
CHAR_LENGTH(varchar str)
```

Return value type: BIGINT.

```
  select char_length('China');
  +---------------------+
  | char_length('China') |
  +---------------------+
  |                   2 |
```

#### 12.3.6 CONCAT

This function concatenates strings. If any of the parameters is null, null is returned.

```
concat(varchar str1, ..., varchar strn)
```

Return value type: VARCHAR.

```
  select concat('aliyun', ', ', 'analyticdb');
  +--------------------------------------+
  | concat('aliyun', ', ', 'analyticdb') |
  +--------------------------------------+
  | aliyun, analyticdb                   |
```

#### 12.3.7 CONCAT_WS

This function concatenates strings and separates them with delimiters. The separator parameter specifies the delimiter. Parameters whose value is null are not included in the final string.

```
concat_ws(varchar separator, varchar str1, ..., varchar strn)
```

Return value type: VARCHAR.

```
  select concat_ws(',', 'First name', 'Second name', 'Last Name')as result;
  +----------------------------------+
  | result                           |
  +----------------------------------+
  | First name,Second name,Last Name |
```

#### 12.3.8 ELT

This function returns the string specified by the integer N.

```
ELT(bigint N, varchar str1, varchar str2, varchar str3,...)
```

If N is less than 1 or greater than the number of the specified strings, null is returned. Return value type: VARCHAR.

```
  select elt(4, 'Aa', 'Bb', 'Cc', 'Dd');
  +--------------------------------+
  | elt(4, 'Aa', 'Bb', 'Cc', 'Dd') |
  +--------------------------------+
  | Dd                             |
```

#### 12.3.9 EXPORT_SET

This function returns a string in which the strings on and off are placed based on the bits 0 or 1 from right to left (from low-order to high-order) in the binary value of the bits integer.

```
EXPORT_SET(bigint bits, varchar on, varchar off[, varchar separator[, bigint number_of_bits ]])EXPORT_SET(bigint bits, varchar on, varchar off[, varchar separator[, bigint number_of_b its]])
```

Description: The string on is placed for bit 1, and the string off is placed for bit 0. These strings are separated by delimiters. The default delimiter is a comma (,). The number_of_bits parameter specifies the number of bits that are checked. Default value: 64. If the value of the number_of_bits parameter is greater than 64, the parameter is silently clipped to 64. The same value is returned when the number_of_bits parameter is set to -1 or 64. Return value type: VARCHAR.

```
  select export_set(5,'1','0',',',2);
  +---------------------------------+
  | export_set(5, '1', '0', ',', 2) |
  +---------------------------------+
  | 1,0                             |
```

#### 12.3.10 FIELD

This function returns the position of the string str in the strings such as str1, str2, and str3. If the string str is not found, 0 is returned.

```
field(varchar str, varchar str1, varchar str2, varchar str3,...)
```

Return value type: BIGINT.

```
  select field('Bb', 'Aa', 'Bb', 'Cc', 'Dd', 'Ff');
  +-------------------------------------------+
  | field('Bb', 'Aa', 'Bb', 'Cc', 'Dd', 'Ff') |
  +-------------------------------------------+
  |                                         2 |
```

#### 12.3.11 FIND_IN_SET

This function returns the position of the string str in the string list strlist.

```
FIND_IN_SET(varchar str, varchar strlist)
```

Description: If str is not found in strlist or strlist is empty, 0 is returned. If either str or strlist is null, null is returned. Return value type: BIGINT.

```
  select find_in_set('b','a,b,c,d');
  +-----------------------------+
  | find_in_set('b', 'a,b,c,d') |
  +-----------------------------+
  |                           2 |
```

#### 12.3.12 FORMAT

This function formats the integer X to the `#,###,###. ##` format rounded to D decimal places, and returns the result as a string.

```
format(double X, bigint D)
```

Description: If D is 0, the result has no decimal point or fractional part. Return value type: BIGINT.

```
    select format(12332.123456, 4)as result1, format(12332.1,4)as result2, format(12332.2
,0)as result3;
    +-------------+-------------+---------+
    | result1     | result2     | result3 |
    +-------------+-------------+---------+
    | 12,332.1235 | 12,332.1000 | 12,332  |
```

#### 12.3.13 HEX

This function returns the hexadecimal string of the integer N, or returns a string consisting of the hexadecimal values of all characters in the string str.

```
HEX(bigint N) HEX(varchar str)
```

Return value type: VARCHAR.

```
  select hex(16);
  +---------+
  | hex(16) |
  +---------+
  | 10      |
```

#### 12.3.14 INSTR

This function returns the position of the first occurrence of the substring substr in the string str.

```
INSTR(varchar str, varchar substr)
```

Return value type: BIGINT.

```
  select instr('foobarbar', 'bar');
  +---------------------------+
  | instr('foobarbar', 'bar') |
  +---------------------------+
  |                         4 |
```

#### 12.3.15 LEFT

This function returns the leftmost len characters of the string str.

```
LEFT(varchar str, bigint len)
```

Description: If str or len is null, null is returned. Return value type: VARCHAR.

```
  select left('foobarbar', 5);
  +-----------------------------+
  | left('foobarbar', 5) |
  +-----------------------------+
  | fooba                       |
```

#### 12.3.16 LENGTH/OCTET_LENGTH

This function returns the length of the string str.

```
length(varchar str)
```

Return value type: BIGINT.

```
  select length('aliyun');
  +------------------+
  | length('aliyun') |
  +------------------+
  |                6 |
```

#### 12.3.17 LIKE

The LIKE operator is used to match the string expression with the string pattern. If the two strings match, 1 is returned. Otherwise, 0 is returned.

```
expression [ NOT ] LIKE pattern [ESCAPE 'escape_char']
```

Description: The string pattern can contain the following wildcard characters: %: matches strings in any length. _: matches a single character. escape_char: escapes the percent signs (%) and underscores (_) in the string pattern. The percent signs (%) and underscores (_) following the escape character are not used as wildcard characters. Return value type: BIGINT.

```
  select 'David!' like 'David_' as result1, 'David!' not like 'David_' as result2,  'Davi
d!' like '%D%v%' as result3;
  +---------+---------+---------+
  | result1 | result2 | result3 |
  +---------+---------+---------+
  |       1 |       0 |       1 |
```

#### 12.3.18 LOCATE

This function returns the position of the first occurrence of substring substr in string str, or returns the position of the first occurrence of the substring substr in the string str, starting at position pos.

```
LOCATE(varchar substr, varchar str) LOCATE(varchar substr, varchar str, bigint pos)
```

Description: If substr is not found in str, 0 is returned. If substr or str is null, null is returned. Return value type: BIGINT.

```
  select locate('bar', 'foobarbar');
  +----------------------------+
  | locate('bar', 'foobarbar') |
  +----------------------------+
  |                          4 |
```

#### 12.3.19 LOWER/LCASE

This function converts the string str to lowercase.

```
lower(varchar str)
```

Return value type: VARCHAR.

```
  select lower('Aliyun');
  +-----------------+
  | lower('Aliyun') |
  +-----------------+
  | aliyun          |
```

#### 12.3.20 LPAD

This function returns the string str, left-padded with the string padstr to a length of len characters.

```
lpad(varchar str, bigint len, varchar padstr)
```

Description: If str is longer than len, the return value is shortened to len characters. Return value type: VARCHAR.

```
  select lpad('Aliyun',9,'#');
  +------------------------+
  | lpad('Aliyun', 9, '#') |
  +------------------------+
  | ###Aliyun              |
```

#### 12.3.21 LTRIM

This function removes the leading space characters of the string str.

```
LTRIM(varchar str)
```

Return value type: VARCHAR.

```
  select ltrim('  abc');
  +----------------+
  | ltrim('  abc') |
  +----------------+
  | abc            |
```

#### 12.3.22 MAKE_SET

This function returns a set value (a string containing substrings separated by delimiters) consisting of the string that have the corresponding bit in the bits set.

```
MAKE_SET(bits, str1, str2,...)
```

Description: The string str1 corresponds to bit 0 and the string str2 corresponds to bit 1. The same rule applies to the rest numbers. The strings whose value is null are not included in the final string. Return value type: VARCHAR.

```
  select make_set(5,'hello','nice','world');
  +---------------------------------------+
  | make_set(5, 'hello', 'nice', 'world') |
  +---------------------------------------+
  | hello,world                           |
```

#### 12.3.23 MID

This function returns a substring that contains len characters in length from the string str, starting from the pos position.

```
MID(varchar str, bigint pos, bigint len)
```

Return value type: VARCHAR.

```
  select mid('Quadratically',5,6);
  +----------------------------+
  | mid('Quadratically', 5, 6) |
  +----------------------------+
  | ratica                     |
```

#### 12.3.24 OCT

This function returns the octal string of the integer N.

```
OCT(bigint N)
```

Description: If N is null, null is returned. Return value type: VARCHAR.

```
  select oct(12);
  +---------+
  | oct(12) |
  +---------+
  | 14      |
```

#### 12.3.25 POSITION

This function returns the position of the first occurrence of the substring substr in the string str, starting from position 1. If substr is not found in str, 0 is returned.

```
POSITION(varchar substr IN varchar str)
```

Return value type: BIGINT.

```
  select position('bar' in 'foobarbar');
  +----------------------------+
  | locate('bar', 'foobarbar') |
  +----------------------------+
  |                          4 |
```

#### 12.3.26 REPEAT

This function repeats the string str for count times.

```
REPEAT(varchar str, bigint count)
```

If count < 1, an empty string is returned. If str or count is null, null is returned. Return value type: VARCHAR.

```
  select repeat('a', 3);
  +----------------+
  | repeat('a', 3) |
  +----------------+
  | aaa            |
```

#### 12.3.27 REPLACE

This function replaces all occurrences of the string from_str in the string str with the string to_str.

```
REPLACE(varchar str, varchar from_str, varchar to_str)
```

Return value type: VARCHAR.

```
  select replace('WWW.aliyun.com', 'W', 'w');
  +-------------------------------------+
  | replace('WWW.aliyun.com', 'W', 'w') |
  +-------------------------------------+
  | www.aliyun.com                      |
```

#### 12.3.28 REVERSE

This function returns the string str with the order of the characters reversed.

```
REVERSE(varchar str)
```

Return value type: VARCHAR.

```
  select reverse('123456');
  +-------------------+
  | reverse('123456') |
  +-------------------+
  | 654321            |
```

#### 12.3.29 RIGHT

This function returns the rightmost len characters from the string str.

```
RIGHT(varchar str, bigint len)
```

Description: If str or len is null, null is returned. Return value type: VARCHAR.

```
  select right('abc',3);
  +------------------------+
  | presto_right('abc', 3) |
  +------------------------+
  | abc                    |
```

#### 12.3.30 RLIKE/REGEXP

This function matches the expression string with the pattern string, which is a regular expression. If the two strings match, 1 is returned. Otherwise, 0 is returned.

```
expression RLIKE pattern expression REGEXP pattern
```

If expression or pattern is null, null is returned. Return value type: BIGINT.

```
  select 'Michael!' regexp '.*';
  +-------------------------------+
  | regexp_like('Michael!', '. *') |
  +-------------------------------+
  |                             1 |
```

#### 12.3.31 RPAD

This function returns the string str, right-padded with the string padstr to a length of len characters.

```
rpad(varchar str, bigint len, varchar padstr)
```

If str is longer than len, the return value is shortened to len characters. Return value type: VARCHAR.

```
  select rpad('Aliyun',9,'#');
  +------------------------+
  | rpad('Aliyun', 9, '#') |
  +------------------------+
  | Aliyun###              |
```

#### 12.3.32 RTRIM

This function removes the trailing space characters of the string str.

```
RTRIM(varchar str)
```

Return value type: VARCHAR.

```
  select rtrim('barbar   ');
  +--------------------+
  | rtrim('barbar   ') |
  +--------------------+
  | barbar             |
```

#### 12.3.33 SPACE

This function returns a string consisting of a specified number of space characters.

```
SPACE(bigint N)
```

Return value type: VARCHAR.

```
  select concat("#", space(6), "#");
  +----------------------------+
  | concat('#', space(6), '#') |
  +----------------------------+
  | #      #                   |
```

#### 12.3.34 STRCMP

If the string str1 is the same as the string str2, 0 is returned. If the string str1 is smaller than the string str2 based on the current sort order, -1 is returned. Otherwise, 1 is returned.

```
STRCMP(varchar str1, varchar str2)
```

Return value type: BIGINT.

```
  select strcmp('text', 'text2');
  +-------------------------+
  | strcmp('text', 'text2') |
  +-------------------------+
  |                      -1 |
```

#### 12.3.35 SUBSTR/SUBSTRING

```
SUBSTRING(varchar str, bigint pos) SUBSTRING(varchar str FROM pos) SUBSTRING(varchar str, bigint pos, bigint len) SUBSTRING(varchar str FROM pos FOR len)
```

Description: SUBSTRING(varchar str, bigint pos) or SUBSTRING(varchar str FROM pos): returns the substring starting from the pos position to the end of the string. If pos < 0, the beginning of the substring is pos characters from the end of the string. SUBSTRING(varchar str, bigint pos, bigint len) or SUBSTRING(varchar str FROM pos FOR len): returns a substring that contains len characters in length from the string, starting from the pos position. If pos < 0, the beginning of the substring is pos characters from the end of the string. Return value type: VARCHAR.

```
  select substr('helloworld', 6);
  +-------------------------+
  | substr('helloworld', 6) |
  +-------------------------+
  | world                   |
```

#### 12.3.36 SUBSTRING_INDEX

This function returns the substring before the last occurrence of the delim delimiter in the str string.

```
SUBSTRING_INDEX(varchar str, varchar delim, bigint count)
```

Description: If count > 0, this function returns all the characters to the left of the last delim delimiter. If count < 0, this function returns all the characters to the right of the last delim delimiter. The SUBSTRING_INDEX function performs a case-sensitive match when searching for the delim delimiter. Return value type: VARCHAR.

```
  select substring_index('www.aliyun.com', '.', 2);
  +-------------------------------------------+
  | substring_index('www.aliyun.com', '.', 2) |
  +-------------------------------------------+
  | www.aliyun                                |
```

#### 12.3.37 TRIM

This function removes the leading and trailing space characters or other specified characters from a string.

```
TRIM([remstr FROM] str) TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)
```

Return value type: VARCHAR.

```
  select trim('  bar   ');
  +------------------+
  | trim('  bar   ') |
  +------------------+
  | bar              |
```

#### 12.3.38 UPPER/UCASE

This function converts the string str to uppercase.

```
upper(varchar str)
```

Return value type: VARCHAR.

```
  select upper('Aliyun');
  +-----------------+
  | upper('Aliyun') |
  +-----------------+
  | ALIYUN          |
```

### 12.4 Numeric functions

#### 12.4.1 ABS

This function returns the absolute value of x.

```
abs(tinyint x) abs(smallint x) abs(int x) abs(bigint x) abs(float x) abs(double x) abs(decimal x)
```

Return value types: LONG, DECIMAL, and DOUBLE.

```
  select abs(4.5);
  +----------+
  | abs(4.5) |
  +----------+
  |      4.5 |
```

#### 12.4.2 ROUND

This function rounds the parameter x. d specifies the number of decimal places. The default value of d is 0. The rounding algorithm changes based on the data type of x.

```
round(tinyint x) round(smallint x) round(int x) round(bigint x) round(float x) round(double x) round(x, d)
```

Description: If x is null, null is returned. If d > 0, the parameter is rounded to the specified decimal place. If d = 0, the parameter is rounded to the nearest integer. If d < 0, digits to the left of the decimal point of the parameter are rounded. Return value types: LONG, DECIMAL, and DOUBLE.

```
  select round(4);
  +----------+
  | round(4) |
  +----------+
  |        4 |
```

#### 12.4.3 SQRT

This function returns the square root of x.

```
sqrt(double x)
```

Return value type: DOUBLE.

```
  select sqrt(4.222);
  +-------------------+
  | sqrt(4.222)       |
  +-------------------+
  | 2.054750593137766 |
```

#### 12.4.4 LN

This function returns the natural logarithm of x.

```
ln(double x)
```

Return value type: DOUBLE.

```
  select ln(2.718281828459045);
  +-----------------------+
  | ln(2.718281828459045) |
  +-----------------------+
  |                   1.0 |
```

#### 12.4.5 LOG

If called with one parameter, this function returns the natural logarithm of x. If called with two parameters, this function returns the logarithm of y to the base x. Return value type: DOUBLE.

```
  select log(16);
  +-------------------+
  | log(16)           |
  +-------------------+
  | 2.772588722239781 |
```

#### 12.4.6 LOG2

This function returns the base-2 logarithm of the parameter. Return value type: DOUBLE.

```
  select log2(8.7654);
  +-------------------+
  | log2(8.7654)      |
  +-------------------+
  | 3.131819928389146 |
```

#### 12.4.7 PI

This function returns the value of Pi.

```
pi()
```

Return value type: DOUBLE.

```
  select pi();
  +-------------------+
  | pi()              |
  +-------------------+
  | 3.141592653589793 |
```

#### 12.4.8 LOG10

This function returns the base-10 logarithm of the parameter.

```
log10(double x)
```

Return value type: DOUBLE.

```
  select log10(100.876);
  +--------------------+
  | log10(100.876)     |
  +--------------------+
  | 2.0037878529824615 |
```

#### 12.4.9 POWER/POW

This function returns the value of x raised to the power of y.

```
power(double x, double y) pow(double x, double y)
```

Return value type: DOUBLE.

```
  select power(1.2,3.4);
  +-------------------+
  | power(1.2, 3.4)   |
  +-------------------+
  | 1.858729691979481 |
```

#### 12.4.10 RADIANS

This function converts degrees to radians.

```
radians(double x)
```

Return value type: DOUBLE.

```
  select radians(60.0);
  +--------------------+
  | radians(60.0)      |
  +--------------------+
  | 1.0471975511965976 |
```

#### 12.4.11 DEGREES

This function converts radians to degrees.

```
degrees(double x)
```

Return value type: DOUBLE.

```
  select degrees(1.3);
  +-------------------+
  | degrees(1.3)      |
  +-------------------+
  | 74.48451336700703 |
```

#### 12.4.12 SIGN

This function returns the sign of x.

```
sign(smallint x) sign(tinyint x) sign(int x) sign(bigint x) sign(float x) sign(double x) sign(decimal x)
```

Return value type: LONG.

```
  select sign(12);
  +----------+
  | sign(12) |
  +----------+
  |        1 |
```

#### 12.4.13 CEILING/CEIL

This function returns the minimum integer value that is greater than the value of x.

```
ceiling(tinyint x) ceiling(smallint x) ceiling(int x) ceiling(bigint x) ceiling(float x) ceiling(double x)
```

Return value types: LONG, DECIMAL, and DOUBLE.

```
  select ceiling(4);
  +------------+
  | ceiling(4) |
  +------------+
  |          4 |
```

#### 12.4.14 FLOOR

This function returns the maximum integer value that is less than the value of x.

```
floor(tinyint x) floor(smallint x) floor(int x) floor(bigint x) floor(float x) floor(double x)
```

Return value types: LONG, DECIMAL, and DOUBLE.

```
  select floor(4.5);
  +------------+
  | floor(4.5) |
  +------------+
  |        4.0 |
```

#### 12.4.15 EXP

This function returns the value of e (the base of natural logarithms) raised to the power of x.

```
exp(double x)
```

Return value type: DOUBLE.

```
  select exp(4.5);
  +-------------------+
  | exp(4.5)          |
  +-------------------+
  | 90.01713130052181 |
```

#### 12.4.16 COS

This function returns the cosine of x.

```
cos(double x)
```

Return value type: DOUBLE.

```
  select cos(1.3);
  +---------------------+
  | cos(1.3)            |
  +---------------------+
  | 0.26749882862458735 |
```

#### 12.4.17 ACOS

This function returns the arc cosine of x.

```
acos(double x)
```

Description: If x > 1 or x < -1, null is returned. Return value type: DOUBLE.

```
  select acos(0.5);
  +--------------------+
  | acos(0.5)          |
  +--------------------+
  | 1.0471975511965979 |
```

#### 12.4.18 TAN

This function returns the tangent of x.

```
tan(double x)
```

Return value type: DOUBLE.

```
  select tan(8);
  +--------------------+
  | tan(8)             |
  +--------------------+
  | -6.799711455220379 |
```

#### 12.4.19 ATAN

This function returns the arc tangent of x.

```
atan(double x)
```

Return value type: DOUBLE.

```
  select atan(0.5);
  +--------------------+
  | atan(0.5)          |
  +--------------------+
  | 0.4636476090008061 |
```

#### 12.4.20 ATAN2

This function returns the arc tangent of the result of x divided by y.

```
atan2(double x, double y) atan(double x, double y)
```

Return value type: DOUBLE.

```
  select atan2(0.5,0.3);
  +--------------------+
  | atan2(0.5, 0.3)    |
  +--------------------+
  | 1.0303768265243125 |
```

#### 12.4.21 COT

This function returns the cotangent of x.

```
cot(double x)
```

Return value type: DOUBLE.

```
  select cot(1.234);
  +---------------------+
  | cot(1.234)          |
  +---------------------+
  | 0.35013639786701445 |
```

#### 12.4.22 ASIN

This function returns the arc sine of x.

```
asin(double x)
```

Return value type: DOUBLE.

```
  select asin(0.5);
  +--------------------+
  | asin(0.5)          |
  +--------------------+
  | 0.5235987755982989 |
```

#### 12.4.23 SIN

This function returns the sine of x.

```
sin(double x)
```

Return value type: DOUBLE.

```
  select sin(1.234);
  +--------------------+
  | sin(1.234)         |
  +--------------------+
  | 0.9438182093746337 |
```

### 12.5 Arithmetic operators

+ Description: This operator is used for addition.

```
  select 3+5;
  +-------+
  | _col0 |
  +-------+
  |     8 |
```

- Description: This operator is used for subtraction.

```
  select 3-5;
  +-------+
  | _col0 |
  +-------+
  |    -2 |
```

* Description: This operator is used for multiplication.

```
  select 3*pi();
  +------------------+
  | _col0            |
  +------------------+
  | 9.42477796076938 |
```

/ Description: This operator is used for division.

```
  select 3/pi();
  +-------------------+
  | _col0             |
  +-------------------+
  | 0.954929658551372 |
```

DIV Description: This operator is used for division. The decimal part of the result is discarded.

```
  select 3 div pi();
  +-------+
  | _col0 |
  +-------+
  |     0 |
```

% or MOD Description: This operator returns the remainder of one argument divided by the other argument.

```
  select 3 mod pi();
  +-------+
  | _col0 |
  +-------+
  |   3.0 |
```

- Description: This operator converts a positive number to a negative number or a negative number to a positive number.

```
  select - 2;
  +-------+
  | _col0 |
  +-------+
  |    -2 |
```

### 12.6 Bit functions and operators

BIT_COUNT Description: This function converts the parameter to a binary value, and then returns the number of bits that are set to 1 in the value. Return value type: BIGINT.

```
  select bit_count(2);
  +--------------+
  | bit_count(2) |
  +--------------+
  |            1 |
```

& Description: This function is used for bitwise AND. Return value type: BIGINT.

```
  select 12 & 15;
  +---------------------+
  | bitwise_and(12, 15) |
  +---------------------+
  |                  12 |
```

~ Description: This function inverts all bits. Return value type: BIGINT.

```
  select 2 & ~1;
  +--------------------------------+
  | bitwise_and(2, bitwise_not(1)) |
  +--------------------------------+
  |                              2 |
```

|
Description: This function is used for bitwise OR. Return value type: BIGINT.

```
  select 29 | 15;
  +--------------------+
  | bitwise_or(29, 15) |
  +--------------------+
  |                 31 |
```

^ Description: This function is used for bitwise XOR. Return value type: BIGINT.

```
  select 1 ^ 10;
  +--------------------+
  | bitwise_xor(1, 10) |
  +--------------------+
  |                 11 |
```

>>(BITWISE_RIGHT_SHIFT)

```
bitwise_right_shift(double x, double y) bitwise_right_shift(varchar x, varchar y) bitwise_right_shift(bigint x, bigint y)
```

Description: This function shifts a value to the right. Return value type: BIGINT.

```
  select 3 >> 2;
  +---------------------------+
  | bitwise_right_shift(3, 2) |
  +---------------------------+
  |                         0 |
```

<<(BITWISE_LEFT_SHIFT)

```
bitwise_left_shift(double x, double y) bitwise_left_shift(varchar x, varchar y) bitwise_left_shift(bigint x, bigint y)
```

Description: This function shifts a value to the left. Return value type: BIGINT.

```
  SELECT 3 << 2;
  +--------------------------+
  | bitwise_left_shift(3, 2) |
  +--------------------------+
  |                       12 |
```

### 12.7 Control flow functions

The control flow functions described in this topic use the conditiontest table as test data.

```
create table conditiontest(a int) distributed by hash(a); insert into conditiontest values (1),(2),(3); SELECT * FROM conditiontest; +---+
| a |
+---+
| 2 |
| 1 |
| 3 |
```

CASE

```
CASE expression
    WHEN value THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```

Description: A simple CASE expression checks each value from left to right, and returns the result for the first value that is equal to the expression. If no match is found, result is returned.

```
  SELECT a,
      CASE a
       WHEN 1 THEN 'one'
            WHEN 2 THEN 'two'
            ELSE 'three'
        END as caseresult
  FROM conditiontest;
  +---+------------+
  | a | caseresult |
  +---+------------+
  | 2 | two        |
  | 1 | one        |
  | 3 | three      |
CASE
    WHEN condition THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
```

Description: An advanced CASE expression calculates conditions from left to right, and returns the result for the first condition that is TRUE. If no condition is TRUE, result is returned.

```
   SELECT a,
          CASE a
            WHEN a=1 THEN 'one1'
            WHEN a=2 THEN 'two2'
            ELSE 'three3'
        END as caseresult
  FROM conditiontest;
  +---+------------+
  | a | caseresult |
  +---+------------+
  | 1 | one1       |
  | 3 | three3     |
  | 2 | three3     |
```

IF

```
if(condition, true_value)
```

Description: If the condition is true, true_value is returned. Otherwise, null is returned.

```
  SELECT IF((2+3)>4,5);
  +-------+
  | _col0 |
  +-------+
  |     5 |
```

```
if(condition, true_value, false_value)
```

Description: If the condition is true, true_value is returned. Otherwise, false_value is returned.

```
  SELECT IF((2+3)<5,5,6);
  +-------+
  | _col0 |
  +-------+
  |     6 |
```

IFNULL

```
IFNULL(expr1,expr2)
```

Description: If expr1 is not null, expr1 is returned. Otherwise, expr2 is returned.

```
  SELECT IFNULL(NULL,2);
  +-------+
  | _col0 |
  +-------+
  |     2 |
  SELECT IFNULL(1,0);
  +-------+
  | _col0 |
  +-------+
  |     1 |
```

NULLIF

```
NULLIF(expr1,expr2)
```

Description: If expr1 is equal to expr2, null is returned. Otherwise, expr1 is returned.

```
  SELECT NULLIF (2,1);
  +-------+
  | _col0 |
  +-------+
  |     2 |
  SELECT NULLIF (2,2);
  +-------+
  | _col0 |
  +-------+
  | NULL  |
```
