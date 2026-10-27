---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for PostgreSQL User Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 71
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for PostgreSQL User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20AnalyticDB%20for%20PostgreSQL%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 AnalyticDB for PostgreSQL User Guide 20220928

## Table of Contents

- 1 What is AnalyticDB for PostgreSQL?
- 2 Quick start
  - 2.1 Overview
  - 2.2 Log on to the AnalyticDB for PostgreSQL console
  - 2.3 Create an instance
  - 2.4 Configure a whitelist
  - 2.5 Create an initial account
  - 2.6 Obtain the client tool
  - 2.7 Connect to a database
- 3 Instances
  - 3.1 Reset the password
  - 3.2 View monitoring information
  - 3.3 Switch the network type of an instance
  - 3.4 Restart an instance
  - 3.5 Import data
    - 3.5.1 Import or export data from or to OSS in parallel
    - 3.5.2 Import data from MySQL
    - 3.5.3 Import data from PostgreSQL
    - 3.5.4 Import data by using the \COPY statement
- 4 Databases
  - 4.1 Overview
  - 4.2 Create a database
  - 4.3 Create a partition key
  - 4.4 Construct data
  - 4.5 Query data
  - 4.6 Manage extensions
  - 4.7 Manage users and permissions
  - 4.8 Manage JSON data
  - 4.9 Use HyperLogLog
  - 4.10 Use the CREATE LIBRARY statement
  - 4.11 Create and use the PL/Java UDF
- 5 Table
  - 5.1 Create a table
  - 5.2 Principles and scenarios of row store, column store, heap tables, and AO tables
  - 5.3 Enable the column store and compression features
  - 5.4 Add a field to a column store table and set the default value
  - 5.5 Configure the table partition
  - 5.6 Configure the sort key
- 6 Best practices
  - 6.1 Configure memory and load parameters

ostgreSQL?

## 1 What is AnalyticDB for PostgreSQL?

PostgreSQL? AnalyticDB for PostgreSQL (formerly known as HybridDB for PostgreSQL) is a distributed cloud database service that uses multiple compute nodes to provide massively parallel processing (MPP) data warehousing services. AnalyticDB for PostgreSQL is developed based on the open source Greenplum database project and enhanced by Alibaba Cloud. This service has the following features: Compatible with Greenplum and all tools that support it. Supports OSS, JSON, and HyperLogLog, a probability cardinality estimation algorithm. Supports SQL:2003-compliant syntax and OLAP aggregate functions to provide flexible hybrid analysis. Supports both row store and column store to enhance analytics performance. Leverages data compression technologies to reduce storage costs. Provides online expansion and performance monitoring services to enable DBAs, developers, and data analysts to focus on improving enterprise productivity and creating core business value instead of managing and maintaining large numbers of MPP clusters.

## 2 Quick start

### 2.1 Overview

This topic provides a quick start guide about how to perform management tasks for AnalyticDB for PostgreSQL instances such as creating an instance and logging on to a database. This topic describes how to log on to the AnalyticDB for PostgreSQL console. You can create an instance in the console and then manage the instance. To ensure a secure and stable database, you must add IP addresses or CIDR blocks that are allowed to access the database to a whitelist of the instance before you use the AnalyticDB for PostgreSQL instance. After you create an instance, you must create an initial account to log on to the database. You can use a client that supports PostgreSQL or Greenplum to connect to the database.

### 2.2 Log on to the AnalyticDB for PostgreSQL console

PostgreSQL console This topic describes how to log on to the AnalyticDB for PostgreSQL console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. In the address bar, enter the URL used to access the ASCM console. Press the Enter key.
2. Enter your username and password.
Obtain the username and password for logging on to the console from the operations administrator.

> Not e When you log on to the ASCM console for the first time, you must change the password of your username as prompted. Due to security concerns, your password must meet the minimum complexity requirements: The password must be 8 to 20 characters in length and must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).

3. Click Login to go to the ASCM console homepage.
4. In the top navigation bar, choose Product s > Analyt icDB f or Post greSQL.

### 2.3 Create an instance

You can create an instance in the console and then manage the instance.
1. Log on to the AnalyticDB for PostgreSQL console.
2. In the upper-right corner of the page, click Creat e Inst ance.
3. On the Analyt icDB f or Post greSQL buy page, configure the following parameters.

| Section | Parameter | Description |
|---|---|---|
| Region | Organization | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
|   | Region | The region of the instance. Not e If you need to access the AnalyticDB for PostgreSQL instance from an ECS instance over VPC, you must deploy the instance in the same region and zone as those of the ECS instance. |
|   | Zone | The zone of the instance. |
| Basic Settings | Engine | Currently, only the integrated computing and storage version is supported. |
|   | Engine Version | The engine version of the instance. |
|   | Node Type | The unit of computing resources. Different group types have different storage capacities and computing capabilities. |
|   | Nodes | The number of compute nodes. An instance must contain at least two compute nodes. The performance of an instance scales linearly with the number of compute nodes. |
|   | Network Type | Valid values: Classic Network: Cloud services on a classic network are not isolated from each other. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A VPC helps you to build an isolated network environment in Alibaba Cloud. You can customize the route table, IP address range, and gateway in a VPC. We recommend that you select VPC for enhanced security. You can create a VPC in advance, or change the network type to VPC after instance creation. |

|   | AnalyticDB for PostgreSQ |   |
|---|---|---|
| Section Network | Parameter | Description |
|   | VPC | The VPC where the AnalyticDB for PostgreSQL instance is located. Not e Virtual Private Cloud (VPC): You can use a VPC to build an isolated network environment in Alibaba Cloud. You can customize the route table, IP address range, and gateway in a VPC. |
|   | VSwitch | The VSwitch where the AnalyticDB for PostgreSQL instance is located. |
|   | IP Whitelist | The IP addresses that are allowed to access the instance. |

4. After you have configured the preceding parameters, click Submit .

### 2.4 Configure a whitelist

To ensure a secure and stable database, you must add IP addresses or CIDR blocks that are allowed to access the database to a whitelist.
1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the target instance and click its ID. The Basic Inf ormat ion page appears.
3. In the left-side navigation pane, click Securit y Cont rols. The Securit y Cont rols page appears.
4. On the Whit elist Set t ings tab, click Modif y corresponding to the default whitelist. The Modif y
Group page appears.

> Not e You can also click Clear corresponding to the default whitelist to delete the IP addresses of the default whitelist, and then click Add Group to create a new whitelist.

5. Delete 127.0.0.1 from the default whitelist and enter your IP addresses in the whitelist. The
following table lists the parameters.

| Parameter | Description |
|---|---|
| Whitelist Name | Specify the name of the whitelist. The whitelist name must be 2 to 32 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a lowercase letter and end with a letter or _ digit. The default whitelist cannot be modified or deleted. |

| Parameter | Description |
|---|---|
| IP Addresses | Enter the CIDR blocks or IP addresses that are allowed to access the database. Use commas (,) to separate multiple CIDR blocks or IP addresses. A whitelist can contain IP addresses such as 10.10.10.1 and CIDR blocks such as 10.10.10.0/24. This CIDR block indicates that any IP addresses in the 10.10.10.X format have access to the database. The percent sign (%) or 0.0.0.0/0 indicates that any IP addresses are allowed to access the database. Not ice This configuration is not recommended because it reduces the security of the database. Default whitelists of new instances contain the loopback address 127.0.0.1. This configuration allows no access from external IP addresses. You can add up to 999 IP addresses or CIDR blocks to a whitelist group. |

6. Click OK to create a whitelist.
What's next We recommend that you regularly maintain the whitelist to ensure secure access for AnalyticDB for PostgreSQL. You can click Modif y or Delet e to modify or delete custom whitelists.

### 2.5 Create an initial account

After you create an instance, you must create an initial account to log on to the database.
1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click its ID.
3. In the left-side navigation pane, click Account Management . The Account Management page
appears.
4. In the upper-right corner of the page, click Creat e Account . The Creat e Account page appears.
5. Enter the database account and password, and click OK.

| Parameter | Description |
|---|---|
| Account | The name of the account must be 2 to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must _ start with a letter and end with a letter or digit. |
| New Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| Password | Enter the password again. |

### 2.6 Obtain the client tool

The interface protocol of AnalyticDB for PostgreSQL is compatible with Greenplum Community Edition and PostgreSQL 8.2. Because of this, you can use the Greenplum or PostgreSQL client to connect to AnalyticDB for PostgreSQL.

> Not e
> Apsara Stack is an isolated environment. You must deploy software installation packages to the internal environment.

Graphical client tools AnalyticDB for PostgreSQL users can directly use client tools that support Greenplum, such as SQL Workbench, Navicat Premium, Navicat for PostgreSQL, and pgAdmin III (1.6.3). Command-line client psql (for RHEL 6, RHEL 7, CentOS 6, and CentOS 7) For Red Hat Enterprise Linux (RHEL) and CentOS 6 or 7, you can download the tools from the following addresses and decompress the packages to use them: For RHEL 6 or CentOS 6, click hybriddb_client_package_el6. For RHEL version 7 or CentOS version 7, click hybriddb_client_package_el7. Command-line client psql (for other Linux systems) The compilation methods for client tools applicable to other Linux systems are as follows:
1. Obtain the source code by using one of the following methods:
Obtain the git directory. You must first install the git tool.

```
git clone https://github.com/greenplum-db/gpdb.git cd gpdb git checkout 5d870156
```

Download the code.

```
wget https://github.com/greenplum-db/gpdb/archive/5d87015609abd330c68a5402c1267fc86cb c9e1f.zip unzip 5d87015609abd330c68a5402c1267fc86cbc9e1f.zip cd gpdb-5d87015609abd330c68a5402c1267fc86cbc9e1f
```

2. Use gcc and other compilers.

```
./configure make -j32 make install
```

3. Use psql and pg_dump. The paths of the two tools are as follows:
psql: /usr/local/pgsql/bin/psql pg_dump: /usr/local/pgsql/bin/pg_dump Command-line client psql (for Windows and other systems) For client tools for Windows and other systems, go to the Pivotal website to download HybridDB Client

### 2.7 Connect to a database

The Greenplum Database and AnalyticDB for PostgreSQL are both developed based on PostgreSQL 8.2 and fully compatible with its messaging protocol. AnalyticDB for PostgreSQL users can use tools that support the PostgreSQL 8.2 message protocol, such as libpq, JDBC, ODBC, psycopg2, and pgAdmin III. Context AnalyticDB for PostgreSQL provides psql, a binary program of Red Hat. For more information about the download link, see Obtain the client tool. The Greenplum official website provides an easy-to-install installation package that includes JDBC, ODBC, and libpq. For more information, see Greenplum official documentation.

> Not e
> Apsara Stack is an isolated environment. To access Apsara Stack, you must prepare the necessary software installation packages in advance.
> AnalyticDB for PostgreSQL instances can only be accessed by clients deployed on ECS instances within the same region and zone.

psql psql is a common tool used together with Greenplum, and provides a variety of command functions. Its binary files are located in the bin directory of Greenplum. The procedure is as follows:
1. Connect to AnalyticDB for PostgreSQL by using one of the following methods:
Connection string

```
psql "host=yourgpdbaddress.gpdb.rds.aliyuncs.com port=3432 dbname=postgres user=gpdba ccount password=gpdbpassword"
```

Specified parameters

```
psql -h yourgpdbaddress.gp.aliyun-inc.com -p 3432 -d postgres -U gpdbaccount
```

Parameters: -h: specifies the host address. -p: specifies the port number. -d: specifies the database. The default database is postgres. -U: specifies the user to connect to the database. In psql, you can run the `psql --help` command to view more options. You can run the \? command to view the commands supported in psql.
2. Enter the password to go to the psql shell interface.

```
postgres=>
```

References For more information about the Greenplum psql usage, see psql. AnalyticDB for PostgreSQL also supports psql statements of PostgreSQL. Pay attention to the differences between Greenplum psql and PostgreSQL psql. For more information, see PostgreSQL 8.3.23 Documentation - psql. pgAdmin III pgAdmin III is a PostgreSQL graphical client and can be directly used to connect to AnalyticDB for PostgreSQL. For more information, click here. For more information about other graphical clients, see Obtain the client tool.
1. Download pgAdmin III 1.6.3 or earlier versions.
You can download pgAdmin III 1.6.3 from the PostgreSQL website. PgAdmin III 1.6.3 supports various operating systems, such as Windows, macOS, and Linux.

> Not e AnalyticDB for PostgreSQL is compatible with PostgreSQL 8.2. Therefore, you must use pgAdmin III 1.6.3 or earlier to connect to AnalyticDB for PostgreSQL. pgAdmin 4 and later versions are not supported.

2. Choose File > Add Server.
3. In the New Server Registration dialog box that appears, enter the configuration information.
4. Click OK to connect to AnalyticDB for PostgreSQL.
JDBC JDBC uses the interface provided by PostgreSQL. The download methods are as follows: Click PostgreSQL JDBC Driver to download the official JDBC of PostgreSQL, and then add it to the environment variables. Use the tools provided by the Greenplum website. For more information, see Greenplum Database 4.3 Connectivity Tools for UNIX. The sample code is as follows:

```java
import java.sql.Connection; import java.sql.DriverManager; import java.sql.ResultSet; impor t java.sql.SQLException; import java.sql.Statement; public class gp_conn { public static vo id main(String[] args) { try { Class.forName("org.postgresql.Driver"); Connection db = Driv erManager.getConnection("jdbc:postgresql://mygpdbpub.gpdb.rds.aliyuncs.com:3432/postgres"," mygpdb","mygpdb"); Statement st = db.createStatement(); ResultSet rs = st.executeQuery("sel ect * from gp_segment_configuration;"); while (rs.next()) { System.out.print(rs.getString(1 )); System.out.print(" | "); System.out.print(rs.getString(2)); System.out.print(" | "); Sy stem.out.print(rs.getString(3)); System.out.print(" | "); System.out.print(rs.getString(4)) ; System.out.print(" | "); System.out.print(rs.getString(5)); System.out.print(" | "); Syst em.out.print(rs.getString(6)); System.out.print(" | "); System.out.print(rs.getString(7)); System.out.print(" | "); System.out.print(rs.getString(8)); System.out.print(" | "); System .out.print(rs.getString(9)); System.out.print(" | "); System.out.print(rs.getString(10)); S ystem.out.print(" | "); System.out.println(rs.getString(11)); } rs.close(); st.close(); } c atch (ClassNotFoundException e) { e.printStackTrace(); } catch (SQLException e) { e.printSt ackTrace(); } } }
```

Python Python uses psycopg2 to connect to Greenplum and PostgreSQL. Procedure:
1. Install psycopg2. There are three installation methods in CentOS:
Method 1: Run the `yum -y install python-psycopg2` command. Method 2: Run the `pip install psycopg2` command. Method 3: Run the source code:

```python
yum install -y postgresql-devel* wget http://initd.org/psycopg/tarballs/PSYCOPG-2-6/psycopg2-2.6.tar.gz tar xf psycopg2-2.6.tar.gz cd psycopg2-2.6 python setup.py build sudo python setup.py install
```

2. Run the following commands to set PYTHONPATH and reference it:

```java
import psycopg2
 sql = 'select * from gp_segment_configuration;'
 conn = psycopg2.connect(database='gpdb', user='mygpdb', password='mygpdb', host='mygpd
bpub.gpdb.rds.aliyuncs.com', port=3432)
 conn.autocommit = True
 cursor = conn.cursor()
 cursor.execute(sql)
 rows = cursor.fetchall()
 for row in rows:
     print row
 conn.commit()
 conn.close()
```

A similar output is displayed:

```
(1, -1, 'p', 'p', 's', 'u', 3022, '192.168.2.158', '192.168.2.158', None, None)(6, -1, 'm', 'm', 's', 'u', 3019, '192.168.2.47', '192.168.2.47', None, None)(2, 0, 'p', 'p', ' s', 'u', 3025, '192.168.2.148', '192.168.2.148', 3525, None)(4, 0, 'm', 'm', 's', 'u', 3024, '192.168.2.158', '192.168.2.158', 3524, None)(3, 1, 'p', 'p', 's', 'u', 3023, '19 2.168.2.158', '192.168.2.158', 3523, None)(5, 1, 'm', 'm', 's', 'u', 3026, '192.168.2.1 48', '192.168.2.148', 3526, None)
```

libpq libpq is the C language interface to AnalyticDB for PostgreSQL. You can use the libpq library to access and manage PostgreSQL databases in a C program. You can locate its static and dynamic libraries under the lib directory. For the example programs, visit Example Programs. For more information about libpq, see PostgreSQL 9.4.17 Documentation - Chapter 31. libpq - C Library. ODBC PostgreSQL ODBC is an open-source version based on the GNU Lesser General Public License (LGPL) protocol. You can download it from the PostgreSQL website.
1. Install the driver.

```bash
yum install -y unixODBC.x86_64 yum install -y postgresql-odbc.x86_64
```

2. View the driver configuration.

```bash
cat /etc/odbcinst.ini
# Example driver definitions
# Driver from the postgresql-odbc package
# Setup from the unixODBC package
[PostgreSQL] Description = ODBC for PostgreSQL Driver = /usr/lib/psqlodbcw.so Setup = /usr/lib/libodbcpsqlS.so Driver64 = /usr/lib64/psqlodbcw.so Setup64 = /usr/lib64/libodbcpsqlS.so FileUsage = 1
# Driver from the mysql-connector-odbc package
# Setup from the unixODBC package
[MySQL] Description = ODBC for MySQL Driver = /usr/lib/libmyodbc5.so Setup = /usr/lib/libodbcmyS.so Driver64 = /usr/lib64/libmyodbc5.so Setup64 = /usr/lib64/libodbcmyS.so FileUsage = 1
```

3. Configure the DSN. Replace the `****` in the following code with the corresponding connection
information.

```
[mygpdb] Description = Test to gp Driver = PostgreSQL Database = **** Servername = ****.gpdb.rds.aliyuncs.com UserName = **** Password = **** Port = **** ReadOnly = 0
```

4. Test connectivity.

```
echo "select count(*) from pg_class" | isql mygpdb +---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+ SQL> select count(*) from pg_class +---------------------+
| count               |
+---------------------+
| 388                 |
+---------------------+ SQLRowCount returns 1 1 rows fetched
```

5. After ODBC is connected to the instance, connect the application to ODBC. For more information,
see PostgreSQL ODBC Driver and psqlODBC HOWTO - C#. References Pivotal Greenplum documentation PostgreSQL psqlODBC Compiling psqlODBC on Unix Download ODBC connectors Download JDBC connectors The PostgreSQL JDBC Interface

## 3 Instances

### 3.1 Reset the password

If you forget the password of your database account, you can reset the password in the AnalyticDB for PostgreSQL console.

> Not e We recommend that you change your password periodically to ensure data security.

1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click its ID.
3. In the left-side navigation pane, click Account Management .
4. Click Reset Password in the corresponding Actions column of the account. The Reset Account
Password page appears.
5. After you enter and confirm the new password, click OK.

> Not e The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. We recommend that you do not use a previously used password.

### 3.2 View monitoring information

You can go to the monitoring information page in the console to view the operation status of an instance.
1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click its ID.
3. In the left-side navigation pane, click Monit oring and Alarms. The Monit oring and Alarms page
appears. Specify a duration of time n up to seven days in length to view the metrics for that last n period.

### 3.3 Switch the network type of an instance

instance The default network type of an instance is Virtual Private Cloud (VPC). After an instance is created, you can switch its network type between classic network and VPC as needed. Context AnalyticDB for PostgreSQL supports two network types: classic network and VPC. Both network types use BGP connections, and are independent of the public network of your service provider. These network types only differ in functions, and you can choose a network type based on your requirements. The two network types are applicable to different scenarios: Classic network: IP addresses are allocated by Alibaba Cloud. Classic networks are easy to configure and use. This network type is suitable for users who do not need to perform complex operations, or who only require short deployment cycles. VPC: a logically isolated private network. You can customize the network topology and IP addresses and connect through a leased line. This network type is suitable for advanced users.

> **Warning:** Switching the network type will cause the database service to stop. Proceed with caution.

1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the target instance and click its ID. The Basic Inf ormat ion page appears.
3. In the left-side navigation pane, click Dat abase Connect ion. The Dat abase Connect ion page
appears.
4. In the upper-right corner of the page, click Swit ch t o Classic Net work or Swit ch t o VPC.
5. If you click Swit ch t o VPC, you must select the destination VPC and VSwit ch. Click OK.

> Not e To switch the network type to VPC, a VPC and a VSwitch must exist or be created in the zone where the instance is located.

6. If you click Swit ch t o Classic Net work, click OK in the displayed message.

> Not e After you switch the network type, it takes 3 to 30 minutes for the instance to enter the running state.

### 3.4 Restart an instance

To better meet your needs, AnalyticDB for PostgreSQL automatically updates the database kernel version. When you create an instance, the latest database kernel is used by default. After a new version is released, you can restart your instance to update the database kernel and use its extended features. This topic describes how to restart an instance.

> **Warning:** Restarting an instance will cause the database service to stop. Proceed with caution.

1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click its ID.
3. In the upper-right corner of the page, click Rest art Inst ance.

> Not e The restart process typically takes from 3 to 30 minutes. During the restart period, the instance cannot provide external services. We recommend that you take precautionary measures before restarting instances. After the instance has been restarted and enters the running state, you can access the database.

### 3.5 Import data

#### 3.5.1 Import or export data from or to OSS in parallel

parallel AnalyticDB for PostgreSQL can import or export data from or to OSS tables in parallel by using the OSS external table feature, gpossext. AnalyticDB for PostgreSQL also supports GZIP compression for OSS external tables to reduce file size and storage costs. gpossext can read from and write to TEXT and CSV files, even when they are compressed in GZIP packages. Create an OSS external table extension (oss_ext) To use an OSS external table, you must first create an OSS external table extension in AnalyticDB for PostgreSQL. You must create an extension for each database that you need to access.

| CREATE EXTENSION IF NOT EXISTS oss ext; _ |   |
|---|---|
| DROP EXTENSION IF EXISTS oss ext; _ |   |

Import data in parallel i. Distribute data evenly among multiple OSS files for storage. We recommend that you set the number of OSS files to an integer that is the multiple of the number of compute nodes in AnalyticDB for PostgreSQL. ii. Create a READABLE external table in AnalyticDB for PostgreSQL. iii. Execute the following statement to import data in parallel:

```
INSERT INTO <destination table> SELECT * FROM <external table>
```

| Not e The data import performance depends on the OSS performance and resources of the AnalyticDB for PostgreSQL instance, such as CPU, I/O, memory, and network resources. To ensure the best import performance, we recommend that you use column store and compression when you create a table. For example, you can specify the following clause: WITH (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, B |   |
|---|---|
|   | WITH (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, B |
| LOCKSIZE=1048576) |   |

documentation on database table creation syntax.

> We recommend that you configure OSS and AnalyticDB for PostgreSQL instances within the same region to implement the best import performance.

Export data in parallel i. Create a WRITABLE external table in AnalyticDB for PostgreSQL. ii. Execute the following statement to export data to OSS in parallel:

```
INSERT INTO <external table> SELECT * FROM <source table>
```

Create OSS external tables

> Not e The syntax to create and use external tables is the same as that of Greenplum Database, except for the syntax of location-related parameters.

```
CREATE [READABLE] EXTERNAL TABLE tablename ( columnname datatype [, ...] | LIKE othertable ) LOCATION ('ossprotocol') FORMAT 'TEXT'
            [( [HEADER]
               [DELIMITER [AS] 'delimiter' | 'OFF']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
           | 'CSV'
            [( [HEADER]
               [QUOTE [AS] 'quote']
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE NOT NULL column [, ...]]
               [ESCAPE [AS] 'escape']
               [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
               [FILL MISSING FIELDS] )]
[ ENCODING 'encoding' ] [ [LOG ERRORS [INTO error_table]] SEGMENT REJECT LIMIT count
       [ROWS | PERCENT] ]
CREATE WRITABLE EXTERNAL TABLE table_name ( column_name data_type [, ...] | LIKE other_table ) LOCATION ('ossprotocol') FORMAT 'TEXT'
               [( [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [ESCAPE [AS] 'escape' | 'OFF'] )]
          | 'CSV'
               [([QUOTE [AS] 'quote']
               [DELIMITER [AS] 'delimiter']
               [NULL [AS] 'null string']
               [FORCE QUOTE column [, ...]] ]
               [ESCAPE [AS] 'escape'] )]
[ ENCODING 'encoding' ] [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ] ossprotocol:
   oss://oss_endpoint prefix=prefix_name
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[true|
false] ossprotocol:
   oss://oss_endpoint dir=[folder/[folder/]...]/file_name
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[true|
false] ossprotocol:
   oss://oss_endpoint filepath=[folder/[folder/]...]/file_name
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[true|
false]
```

Parameters Common parameters

| Parameter | Description |
|---|---|
| Protocol and endpoint | It is in the protocol name://oss endpoint format. The protocol _ name is oss. oss endpoint is the domain name used by users to _ access OSS in a region. Not e You can access the database from a VPC host by using an internal endpoint containing "internal" in the name to avoid generating public traffic. |
| id | The AccessKey ID of the OSS account. |
| key | The AccessKey secret of the OSS account. |
| bucket | The bucket where the data file is located. You must use OSS to create the bucket before data import. |
| prefix | The prefix of the path name corresponding to the data file. Prefixes are directly matched and cannot be controlled by regular expressions. The prefix, filepath, and dir parameters are mutually exclusive and only one parameter can be specified at a time. If you create a READABLE external table for data import, all OSS files that contain the specified prefix will be imported. If you set prefix to test/filename, the following files will be imported: test/filename test/filenamexxx test/filename/aa test/filenameyyy/aa test/filenameyyy/bb/aa If you set prefix to test/filename/, only the following file out of the preceding files will be imported: test/filename/aa if you create a WRITABLE external table for data export, each exported file will have a unique name based on this parameter. Not e One or more files can be exported for each compute node. The names of exported files are in the prefi x tablename uuid.x format. uuid indicates a timestamp in _ _ microseconds as an int64 value. x indicates the node ID. You can use an external table for multiple export operations. Each export operation is assigned to a uuid value. The files exported during each operation share a uuid value. |

| prefi |   |
|---|---|

|   |   | x tablename uuid.x _ _ |
|---|---|---|

| Parameter | Description |   |   |
|---|---|---|---|
| dir | The virtual folder path in OSS. The prefix, filepath, and dir parameters are mutually exclusive and only one parameter can be specified at a time. A folder path must end with a forward slash (/) such as test/myd ir/ . If you use this parameter when creating an external table for data import, all files under the specified virtual directory (except for its subdirectories and contained files) will be imported. Unlike filepath, dir does not require you to specify the names of files in the directory. If this parameter is used in creating an external table for data export, all data will be exported to multiple files within the specified directory. The names of exported files are in the filena me.x format, where x is a digit. The values of x may not be consecutive. |   |   |
|   |   | filena |   |
| filepath | The file name that contains a path in OSS. The prefix, filepath, and dir parameters are mutually exclusive and only one parameter can be specified at a time. You can only specify the filepath parameter when you create a READABLE external table for data import. The file name includes the file path, but not the bucket name. The filename specified for data import must be in the filename or filename.x format. The values of x must be consecutive digits starting from 1. For example, if filepath is set to filename and OSS contains the following files, the imported files include filename, filename.1, and filename.2, but filename.4 is not imported because filename.3 does not exist. filename filename.1 filename.2 filename.4 |   |   |

| test/myd |   |
|---|---|

|   | ir/ |
|---|---|

|   | me.x |
|---|---|

Import mode parameters

| Parameter | Description |
|---|---|
| async | Specifies whether to load data asynchronously. Asynchronous data import is enabled by default. You can set async to false or f to disable asynchronous data import. Enables the worker thread to load data from OSS to accelerate the import performance. The default import mode is asynchronous mode. Asynchronous data import consumes more hardware resources than normal data import. |

| Parameter | Description |
|---|---|
| compressiontype | The compression format of the imported file. Valid values: none: specifies to import files without compressing them. This is the default value. gzip: specifies compress imported files in the GZIP format. Only the GZIP format is supported. |
| compressionlevel | The compression level of the files written to OSS. Valid values: 1 to 9. Default value: 6. |

Export mode parameters

| Parameter | Description |
|---|---|
| oss flush block size _ _ _ | The size of each data block written to OSS. Valid values: 1 MB to 128 MB. Default value: 32 MB. |
| oss file max size _ _ _ | The maximum size of each file written to OSS. If the limit is exceeded, subsequent data is written to another file. Valid values: 8 MB to 4000 MB. Default value: 1024 MB. |
| num parallel worker _ _ | The number of parallel compression threads for data written to OSS. Valid values: 1 to 8. Default value: 3. |

Additionally, you must pay attention to the following items for the export mode: WRITABLE is the keyword of the external table for data export. You must specify this keyword when creating an external table. Only the prefix and dir parameters are supported for data export. The filepath parameter is not supported. You can use the DISTRIBUTED BY clause to write data from compute nodes to OSS based on the specified distribution keys. Ot her common paramet ers The following error-tolerance parameters can be used for data import and export: Error-tolerance parameters

| Parameter | Description |
|---|---|
| oss connect timeout _ _ | The connection timeout period. Unit: seconds. Default value: 10. |
| oss dns cache timeout _ _ _ | The DNS timeout period. Unit: seconds. Default value: 60. |
| oss speed limit _ _ | The minimum rate tolerated. Default value: 1024 bit/s (1 Kbit/s). |
| oss speed time _ _ | The maximum amount of time tolerated. Unit: seconds. Default value: 15. |

If the default values are used for the preceding parameters, a timeout will occur when the transmission rate is lower than 1 Kbit/s for 15 consecutive seconds. For more information, see T roubleshoot ing in OSS SDK reference . The other parameters are compatible with the original external table syntax of Greenplum Database. For more information about the syntax, see Greenplum Database official documentation on external table syntax. These parameters include: FORMAT: indicates the supported file format, such as TEXT and CSV. ENCODING: indicates the data encoding format of a file, such as UTF-8. LOG ERRORS: indicates that the clause can ignore imported erroneous data and write the data to error_table. You can also use the count parameter to specify the error reporting threshold. Examples

```bash
# Create a READABLE external table of OSS.
create readable external table ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        prefix=osstest/example id=XXX
        key=XXX bucket=testbucket compressiontype=gzip')
        FORMAT 'csv' (QUOTE '''' DELIMITER E'\t')
        ENCODING 'utf8'
        LOG ERRORS INTO my_error_rows SEGMENT REJECT LIMIT 5;
create readable external table ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        dir=osstest/ id=XXX
        key=XXX bucket=testbucket')
        FORMAT 'csv'
        LOG ERRORS SEGMENT REJECT LIMIT 5;
create readable external table ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        filepath=osstest/example.csv id=XXX
        key=XXX bucket=testbucket')
        FORMAT 'csv'
        LOG ERRORS SEGMENT REJECT LIMIT 5;
# Create a WRITABLE external table of OSS.
create WRITABLE external table ossexample_exp
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        prefix=osstest/exp/outfromhdb id=XXX
        key=XXX bucket=testbucket') FORMAT 'csv'
        DISTRIBUTED BY (date);
create WRITABLE external table ossexample_exp
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        dir=osstest/exp/ id=XXX
```

```bash
        key=XXX bucket=testbucket') FORMAT 'csv'
        DISTRIBUTED BY (date);
# Create a heap table named example to which you want to import data.
create table example
        (date text, time text, open float,
         high float, low float, volume int)
         DISTRIBUTED BY (date);
# Import data to the example heap table from the ossexample table in parallel.
insert into example select * from ossexample;
# Export data from example to OSS in parallel
insert into ossexample_exp select * from example;
# As shown in the following execution plan, all compute nodes are involved in the task.
# All compute nodes read data from OSS in parallel. AnalyticDB for PostgreSQL performs a re
distribution motion operation to compute the data by using a hash algorithm, and then distr ibutes the data to its compute nodes after computing. After a compute node receives data, i t performs an insert operation to add the data to AnalyticDB for PostgreSQL. explain insert into example select * from ossexample;
                                            QUERY PLAN
------------------------------------------------------------------------------------------- ----
 Insert (slice0; segments: 4)  (rows=250000 width=92)
   ->  Redistribute Motion 4:4  (slice1; segments: 4)  (cost=0.00..11000.00 rows=250000 wid
th=92)
         Hash Key: ossexample.date
         ->  External Scan on ossexample  (cost=0.00..11000.00 rows=250000 width=92)
(4 rows)
# As shown in the following query plan, each compute node exports local data directly to OS
S without redistributing the data. explain insert into ossexample_exp select * from example;
                          QUERY PLAN
---------------------------------------------------------------
 Insert (slice0; segments: 3)  (rows=1 width=92)
   ->  Seq Scan on example  (cost=0.00..0.00 rows=1 width=92)
(2 rows)
```

TEXT and CSV format description The following parameters specify the formats of files read from and written to OSS. You can specify the parameters in the external DDL parameters. \n: a line delimiter or line break for TEXT and CSV files. DELIMITER: specifies the delimiter of columns. If the DELIMITER parameter is specified, the QUOTE parameter must also be specified. Recommended column delimiters include commas (,), vertical bars (|), \t, and other special characters. QUOTE: encloses user data that contains special characters by column. Strings that contain special characters will be enclosed by QUOTE to differentiate user data from the control characters. To optimize the efficiency, it is unnecessary to enclose data such as integers in QUOTE characters. QUOTE cannot be the same string as specified in DELIMITER. The default value of QUOTE is double quotation marks ("). User data that contains QUOTE characters must also contain ESCAPE characters to differentiate user data from machine code. ESCAPE: specifies the escape character. Place an escape character before a special character that needs to be escaped to indicate that it is not a special character. If ESCAPE is not specified, the default value is the same as QUOTE. You can also use other characters as ESCAPE characters such as backslashes (\), which is used by MySQL. Default control characters for TEXT and CSV files Default control characters for TEXT and CSV files

| Control character | TEXT | CSV |
|---|---|---|
| DELIMITER | \t (tab) | , (comma) |
| QUOTE | " (double quotation mark) | " (double quotation mark) |
| ESCAPE | N/A | Same as QUOTE |
| NULL | \N (backslash-N) | Empty string without quotation marks |

> Not e All control characters must be single-byte characters.

SDK troubleshooting The following table lists the error logs generated when an error occurs during the import or export process. Error log information

| Keyword | Description |
|---|---|
| code | The HTTP status code of the error request. |
| error code _ | The error code returned by OSS. |
| error msg _ | The error message returned by OSS. |
| req id _ | The UUID used to identify the request. If you require assistance in solving a problem, you can submit a ticket containing the req id of _ the failed request to OSS developers. |

For more information, see . You can handle timeout-related errors by using parameters related to oss_ext. References Greenplum Database official documentation on external table syntax Greenplum Database official documentation on table creation syntax

#### 3.5.2 Import data from MySQL

You can use the mysql2pgsql tool to migrate tables from MySQL to AnalyticDB for PostgreSQL, Greenplum Database, PostgreSQL, or PPAS. Background information mysql2pgsql connects a source MySQL database to a destination AnalyticDB for PostgreSQL database, queries data to be exported from the MySQL database, and then imports the data to the destination database by using the \COPY statement. The tool supports multi-thread import. Each worker thread imports a part of database tables. To download the binary installation package of mysql2pgsql, click here. To view instructions on source code compilation of mysql2pgsql, click here. Procedure
1. Modify the my.cfg configuration file to configure the connection information of source and
destination databases. i. Modify the connection information of the source MySQL database.

> Not e You must have the read permissions on all user tables.

```
[src.mysql] host = "192.168.1.1" port = "3306" user = "test" password = "test" db = "test" encodingdir = "share" encoding = "utf8"
```

ii. Modify the connection information of the destination PostgreSQL, PPAS, or AnalyticDB for PostgreSQL database.

> Not e You must have the write permissions on the destination table.

```
[desc.pgsql] connect_string = "host=192.168.1.2 dbname=test port=3432 user=test password=pgsql"
```

2. Import data by using mysql2pgsql.

```
./mysql2pgsql -l <tables_list_file> -d -n -j <number of threads> -s <schema of target t able>
```

Parameters

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| -l | Optional. Used to specify a text file that contains tables to be synchronized. If you do not specify this parameter, all the tables in the database that is specified in the configuration file will be synchronized. <tables list file> is the name of a _ _ file that contains a collection of tables to be synchronized and conditions for table queries. The content format is as follows: table1 : select * from table big where column1 < '2016-08-05' _ table2 : table3 table4: select column1, column2 from tableX where column1 ! = 10 table5: select * from table big where column1 >= '2016-08-05' _ |
| -d | Optional. Indicates the table creation DDL statement that creates the destination table but does not synchronize data. |
| -n | Optional. Must be used along with -d to specify that the table partition definition is not included in the DDL statement. |
| -j | Optional. Used to specify the number of threads used for data synchronization. If you do not specify this parameter, five concurrent threads will be used by default. |
| -s | Optional. Used to specify the schema of the destination table. Only one schema at a time can be specified by the command. If you do not specify the parameter, the data is imported into the table under the public schema. |

Typical usage Full dat abase migrat ion
1. Obtain the DDL statements of the corresponding destination table by running the following
command:

```
 ./mysql2pgsql -d
```

2. Create a table in the destination database based on these DDL statements with the distribution
key information added.
3. Run the following command to synchronize all tables:

```
 ./mysql2pgsql
```

This command will migrate the data from all MySQL tables in the database that is specified in the configuration file to the destination database. By default, five concurrent threads are used to read and import data from involved tables. Part ial t able migrat ion
1. Create a new file tab_list.txt and enter the following content:
`t1`

```
t2 : select * from t2 where c1 > 138888
```

2. Run the following command to synchronize the specified t1 and t2 tables (note that for the t2
table, only data that meets the c1 > 138888 condition is migrated):

```
 ./mysql2pgsql -l tab_list.txt
```

#### 3.5.3 Import data from PostgreSQL

You can use the pgsql2pgsql tool to migrate tables across AnalyticDB for PostgreSQL, Greenplum Database, PostgreSQL, and PPAS. Context pgsql2pgsql supports the following features: Full migration across PostgreSQL, PPAS, Greenplum Database, and AnalyticDB for PostgreSQL. Full migration and incremental migration from PostgreSQL or PPAS (version 9.4 or later) to AnalyticDB for PostgreSQL or ApsaraDB RDS for PPAS. You can download the software packages from the dbsync project library. To download the binary installation package of pgsql2pgsql, click here. To view instructions on source code compilation of pgsql2pgsql, click here. Procedure
1. Modify the my.cfg configuration file to configure the connection information of source and
destination databases. i. Modify the connection information of the source PostgreSQL database.

> Not e In the connection information of the source PostgreSQL database, we recommend that you set the user to the owner of the source database.

```
[src.pgsql] connect_string = "host=192.168.0.1 dbname=test port=3432 user=test password=pgsql"
```

ii. Modify the connection information of the local temporary PostgreSQL database.

```
[local.pgsql] connect_string = "host=192.168.0.2 dbname=test port=3432 user=test2 password=pgsql
```

`"` iii. Modify the connection information of the destination PostgreSQL database.

> Not e You must have the write permissions on the destination table.

```
[desc.pgsql] connect_string = "host=192.168.0.2 dbname=test port=3432 user=test3 password=pgsql
```

`"`

> Not e
> If you need to synchronize incremental data, you must have the permissions to create replication slots in the source database.
> PostgreSQL versions 9.4 and later support logic flow replication, meaning that source databases of the versions support incremental migration. The kernel supports logic flow replication only if you configure the following kernel parameters:
> wal_level = logical
> max_wal_senders = 6
> max_replication_slots = 6

2. Use pgsql2pgsql to perform full database migration.

```
 ./pgsql2pgsql
```

By default, the migration program migrates the table data of all users from the source PostgreSQL database to the destination PostgreSQL database.
3. View the status information.
You can view the status information in a single migration process by connecting to the local temporary database. The information is stored in the db_sync_status table, including the start and end time of the full migration, the start time of the incremental migration, and the status of incremental synchronization.

#### 3.5.4 Import data by using the \COPY statement

You can use the \COPY statement to import the data of local text files into AnalyticDB for PostgreSQL databases. The local text files must be formatted, such as files that use commas (,), semicolons (;), or special characters as delimiters. Context Parallel writing of large amounts of data is not available because the \COPY statement writes data in serial using the coordinator node. If you need to import a large amount of data in parallel, you can use the OSS-based data import method. The \COPY statement is a psql instruction. If you use the database statement `COPY` instead of the \COPY statement, you must note that only stdin is supported. This COPY statement does not support file because the root user does not have the superuser permissions to perform operations on files. AnalyticDB for PostgreSQL also allows you to use JDBC to execute the COPY statement. The CopyIn method is encapsulated within JDBC. For more information, see Interface CopyIn. For more information about how to use the COPY statement, see COPY. Procedure
1. Import data by using the following sample code:

```
\COPY table [(column [, ...])] FROM {'file' | STDIN}
     [ [WITH]
       [OIDS]
       [HEADER]
       [DELIMITER [ AS ] 'delimiter']
       [NULL [ AS ] 'null string']
       [ESCAPE [ AS ] 'escape' | 'OFF']
       [NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
       [CSV [QUOTE [ AS ] 'quote']
            [FORCE NOT NULL column [, ...]]
       [FILL MISSING FIELDS]
       [[LOG ERRORS [INTO error_table] [KEEP]
       SEGMENT REJECT LIMIT count [ROWS | PERCENT] ]
\COPY {table [(column [, ...])] | (query)} TO {'file' | STDOUT}
      [ [WITH]
        [OIDS]
        [HEADER]
        [DELIMITER [ AS ] 'delimiter']
        [NULL [ AS ] 'null string']
        [ESCAPE [ AS ] 'escape' | 'OFF']
        [CSV [QUOTE [ AS ] 'quote']
             [FORCE QUOTE column [, ...]] ]
      [IGNORE EXTERNAL PARTITIONS ]
```

## 4 Databases

### 4.1 Overview

The operations based on the Greenplum Database in AnalyticDB for PostgreSQL are the same as those in the Greenplum Database, including schema, supported data types, and user permissions. Except for certain operations exclusive to the Greenplum Database (such as the partition keys and AO tables), you can refer to PostgreSQL for other operations. References Pivotal Greenplum Official Documentation Greenplum 4.3 Best Practices

### 4.2 Create a database

After you log on to the AnalyticDB for PostgreSQL instance, you can execute SQL statements to create databases. Similar to PostgreSQL, in AnalyticDB for PostgreSQL you can execute SQL statements to create databases. For example, after psql is connected to Greenplum, execute the following statements:

```
=> create database mygpdb; CREATE DATABASE => \c mygpdb psql (9.4.4, server 8.3devel) You are now connected to database "mygpdb" as user "mygpdb".
```

### 4.3 Create a partition key

AnalyticDB for PostgreSQL is a distributed database and data is distributed across all the data nodes. You must create partition keys to distribute the data. The partition keys are vital to query performance. Partition keys are used to ensure even dat a dist ribut ion. Proper selection of keys can significantly improve query performance. Specify a partition key In AnalyticDB for PostgreSQL, tables can be distributed across all compute nodes in either hash or random mode. You must specify the partition key when creating a table. Imported data will be distributed to the specific compute node based on the hash value calculated by the partition key.

```
=> create table vtbl(id serial, key integer, value text, shape cuboid, location geometry, c omment text) distributed by (key); CREATE TABLE
```

If you do not specify the partition key (that means a statement without the `distributed by (key)` field), AnalyticDB for PostgreSQL will randomly allocate the ID field by using the round-robin algorithm. Rules for selecting the partition key Select evenly distributed columns or multiple columns to prevent data skew. Select fields commonly used for connection operations, especially for highly concurrent statements. Select the condition columns that feature high concurrency queries and high filterability. Do not use random distribution.

### 4.4 Construct data

In some test scenarios, you must construct data to fill the database.
1. Create a function that generates random strings.

```
CREATE OR REPLACE FUNCTION random_string(integer) RETURNS text AS $body$ SELECT array_to_string(array
                      (SELECT substring('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij
klmnopqrstuvwxyz'
                                        FROM (ceil(random()*62))::int
                                        FOR 1)
                       FROM generate_series(1, $1)), '');
$body$ LANGUAGE SQL VOLATILE;
```

2. Create a partition key.

```
CREATE TABLE tbl(id serial, KEY integer, locate geometry, COMMENT text) distributed by (key);
```

3. Construct data.

```
INSERT INTO tbl(KEY, COMMENT, locate)
 SELECT
     KEY,
     COMMENT,
     ST_GeomFromText(locate) AS locate
 FROM
     (SELECT
         (a + 1) AS KEY,
         random_string(ceil(random() * 24)::integer) AS COMMENT,
         'POINT(' || ceil(random() * 36 + 99) || ' ' || ceil(random() * 24 + 50) || ')'
AS locate
     FROM
         generate_series(0, 99999) AS a)
     AS t;
```

### 4.5 Query data

This topic describes the query statements and how to view the query plans. Query statement sample

```
  => select * from tbl where key = 751;
  | id  | key | value | shape        | locate                                     | comment
```

|

```
  +-----+-----+-------+--------------+--------------------------------------------+--------
--------+
  | 751 | 751 | red   | 01010000000000000000C05B400000000000004A40 | B9hPhjeNWPqV |
  (1 row)
  Time: 513.101 ms
```

View a query plan

```
  => explain select * from tbl where key = 751;
  Gather Motion 1:1  (slice1; segments: 1)  (cost=0.00..1519.28 rows=1 width=53)
    ->  Seq Scan on tbl  (cost=0.00..1519.28 rows=1 width=53)
          Filter: key = 751
  Settings:  effective_cache_size=8GB; gp_statistics_use_fkeys=on
  Optimizer status: legacy query optimizer
```

### 4.6 Manage extensions

You can use extensions to expand database features. AnalyticDB for PostgreSQL enables you to manage extensions. Extension types AnalyticDB for PostgreSQL supports the following extensions: PostGIS: supports geographic information data. MADlib: supports the machine learning function library. fuzzystrmatch: supports the fuzzy matching of strings. orafunc: compatible with some Oracle functions. oss_ext: supports reading data from OSS. hll: collects statistics by using the HyperLogLog algorithm. pljava: supports compiling user-defined functions (UDF) in the PL/Java language. pgcrypto: supports cryptographic hash functions. intarray: supports integer array-related functions, operators, and indexes. Create an extension Execute the following statements to create an extension:

```
CREATE EXTENSION <extension name>; CREATE SCHEMA <schema name>; CREATE EXTENSION IF NOT EXISTS <extension name> WITH SCHEMA <schema name>;
```

> Not e
> Before you create the MADlib extension, you must create the plpythonu extension first.

```
CREATE EXTENSION plpythonu; CREATE EXTENSION madlib;
```

Delete an extension Execute the following statements to delete an extension:

```
DROP EXTENSION <extension name>; DROP EXTENSION IF EXISTS <extension name> CASCADE;
```

> Not e If there are objects dependent on the extension, you must add the CASCADE keyword to delete all dependent objects.

### 4.7 Manage users and permissions

This topic describes how to manage users and permissions in AnalyticDB for PostgreSQL. Manage users The system prompts you to specify an initial username and password when you create an instance. This initial user is the root user. After the instance is created, you can use the root user account to connect to the database. The system also creates superusers such as aurora and replicator for internal management. You can run the \du+ command to view the information of all the users after you connect to the database by using the client tool of PostgreSQL or Greenplum. Example:

```
postgres=> \du+
                                List of roles
  Role name   |            Attributes             | Member of |  Description
--------------+-----------------------------------+-----------+---------------
 root_user    |                               |      | rds_superuser
 ...
```

AnalyticDB for PostgreSQL does not provide superuser permissions, but offers a similar role, RDS_SUPERUSER, which is consistent with the permission system of ApsaraDB RDS for PostgreSQL. The root user (such as root_user in the preceding example) has the permissions of the RDS_SUPERUSER role. You can only identify this permission attribute by viewing the user description. The root user has the following permissions: Can create databases and users and perform actions such as LOGIN, excluding the SUPERUSER permissions. Can view and modify the data tables of other users and perform actions such as SELECT, UPDATE, DELETE, and changing owners. Can view the connection information of other users, cancel their SQL statements, and kill their connections. Can create and delete extensions. Can create other users with RDS_SUPERUSER permissions. Example:

```
CREATE ROLE root_user2 RDS_SUPERUSER LOGIN PASSWORD 'xyz' ;
```

Manage permissions You can manage permissions at the database, schema, and table levels. For example, if you want to grant read permissions on a table to a user and revoke their write permissions, you can execute the following statements:

```
GRANT SELECT ON TABLE t1 TO normal_user1; REVOKE UPDATE ON TABLE t1 FROM normal_user1; REVOKE DELETE ON TABLE t1 FROM normal_user1;
```

### 4.8 Manage JSON data

JavaScript Object Notation (JSON) has become a basic data type in the Internet and IoT fields. For more information about JSON, visit JSON official website. PostgreSQL support for JSON has been well developed. Optimized by Alibaba Cloud, AnalyticDB for PostgreSQL supports the JSON type based on the PostgreSQL syntax. Check whether the current version supports JSON Execute the following statement to check whether the current version supports JSON:

```
 => SELECT '""'::json;
```

If the following output is displayed, it indicates the JSON type is supported and the instance is ready for use. If the operation fails, restart the instance.

```
 json
------
```

`""`

```
(1 row)
```

If the following output is displayed, it indicates the JSON type is not supported.

```
ERROR: type "json" does not exist LINE 1: SELECT '""'::json;
```

^ The preceding command converts data from the string type to the JSON type. PostgreSQL supports operations on JSON data based on this conversion. JSON conversion in the database Database operations include reading and writing. The written data is typically converted from the string type to the JSON type. The contents of a string must meet the JSON standard, such as strings, digits, arrays, and objects. Example: St ring

```
=> SELECT '"hijson"'::json;
 json
-------
 "hijson"
(1 row)
```

`::` is used for explicit type conversion in PostgreSQL, Greenplum, and AnalyticDB for PostgreSQL. The database calls the input function in JSON type during the conversion. Therefore, the JSON format check is performed as follows:

```
=> SELECT '{hijson:1024}'::json; ERROR: invalid input syntax for type json LINE 1: SELECT '{hijson:1024}'::json;
```

^

```
DETAIL: Token "hijson" is invalid. CONTEXT: JSON data, line 1: {hijson...
```

`=>` In the preceding example, `hijson` must be enclosed in double quotation marks ( `"` ) because JSON requires the KEY value to be a string. A syntax error is returned when `{hijson:1024}` is entered. Apart from explicit type conversion, database records can also be converted to JSON. Typically, JSON is not used for a string or a digit, but an object that contains one or more key-value pairs. AnalyticDB for PostgreSQL can support most JSON scenarios after data is converted from the string type to objects. Example:

```json
=> select row_to_json(row('{"a":"a"}', 'b'));
           row_to_json
---------------------------------
 {"f1":"{\"a\":\"a\"}","f2":"b"}
(1 row) => select row_to_json(row('{"a":"a"}'::json, 'b'));
        row_to_json
---------------------------
 {"f1":{"a":"a"},"f2":"b"}
(1 row)
```

You can see the differences between the string and JSON here. The whole record is conveniently converted into the JSON type. JSON data types Object The object is the most frequently used data type in JSON. Example:

```json
=> select '{"key":"value"}'::json;
        json
  -----------------
   {"key":"value"}
  (1 row)
```

Integer and floating point number JSON only supports three data types for numeric values: integer, floating point number, and constant expression. AnalyticDB for PostgreSQL supports all three types.

```
  => SELECT '1024'::json;
   json
  ------
  (1 row)
  => SELECT '0.1'::json;
   json
  ------
   0.1
  (1 row)
```

The following information is required in some special situations:

```json
  => SELECT '1e100'::json;
   json
  -------
   1e100
  (1 row)
  => SELECT '{"f":1e100}'::json;
      json
  -------------
   {"f":1e100}
  (1 row)
```

Extra-long numbers are also supported. Example:

```
  => SELECT '9223372036854775808'::json;
          json
  ---------------------
   9223372036854775808
  (1 row)
```

Array

```
=> SELECT '[[1,2], [3,4,5]]'::json;
         json
  ------------------
   [[1,2], [3,4,5]]
  (1 row)
```

Operators Operat ors support ed by JSON

```
=> select oprname,oprcode from pg_operator where oprleft = 3114;
 oprname |          oprcode
---------+---------------------------
 ->      | json_object_field
 ->>     | json_object_field_text
 ->      | json_array_element
 ->>     | json_array_element_text
 #>      | json_extract_path_op
 #>>     | json_extract_path_text_op
(6 rows)
```

Basic usage

```
=> SELECT '{"f":"1e100"}'::json -> 'f';
 ? column?
----------
 "1e100"
(1 row) => SELECT '{"f":"1e100"}'::json ->> 'f';
 ? column?
----------
 1e100
(1 row) => select '{"f2":{"f3":1},"f4":{"f5":99,"f6":"stringy"}}'::json#>array['f4','f6'];
 ? column?
-----------
 "stringy"
(1 row) => select '{"f2":{"f3":1},"f4":{"f5":99,"f6":"stringy"}}'::json#>'{f4,f6}';
 ? column?
-----------
 "stringy"
(1 row) => select '{"f2":["f3",1],"f4":{"f5":99,"f6":"stringy"}}'::json#>>'{f2,0}';
 ? column?
----------
```

`f3`

```
(1 row)
```

JSON functions Support ed JSON f unct ions

```
postgres=# \df *json*
                                                       List of functions
   Schema   |           Name            | Result data type |                    Argument da
ta types | Type ------------+---------------------------+------------------+------------------------------- ----------------------------+--------
 pg_catalog | array_to_json             | json             | anyarray
| normal
 pg_catalog | array_to_json             | json             | anyarray, boolean
| normal
pgcatalog|jsonarrayelement
|json
|fromjsonjson
elementindex
```

```
 pg_catalog | json_array_element        | json             | from_json json, element_index
integer | normal
 pg_catalog | json_array_element_text   | text             | from_json json, element_index
integer | normal
 pg_catalog | json_array_elements       | SETOF json       | from_json json, OUT value json
| normal
 pg_catalog | json_array_length         | integer          | json
| normal
 pg_catalog | json_each                 | SETOF record     | from_json json, OUT key text,
OUT value json | normal
 pg_catalog | json_each_text            | SETOF record     | from_json json, OUT key text,
OUT value text | normal
 pg_catalog | json_extract_path         | json             | from_json json, VARIADIC path_
elems text[] | normal
 pg_catalog | json_extract_path_op      | json             | from_json json, path_elems tex
t[] | normal
 pg_catalog | json_extract_path_text    | text             | from_json json, VARIADIC path_
elems text[] | normal
 pg_catalog | json_extract_path_text_op | text             | from_json json, path_elems tex
t[] | normal
 pg_catalog | json_in                   | json             | cstring
| normal
 pg_catalog | json_object_field         | json             | from_json json, field_name tex
t | normal
 pg_catalog | json_object_field_text    | text             | from_json json, field_name tex
t | normal
 pg_catalog | json_object_keys          | SETOF text       | json
| normal
 pg_catalog | json_out                  | cstring          | json
| normal
 pg_catalog | json_populate_record      | anyelement       | base anyelement, from_json jso
n, use_json_as_text boolean | normal
 pg_catalog | json_populate_recordset   | SETOF anyelement | base anyelement, from_json jso
n, use_json_as_text boolean | normal
 pg_catalog | json_recv                 | json             | internal
| normal
 pg_catalog | json_send                 | bytea            | json
| normal
 pg_catalog | row_to_json               | json             | record
| normal
 pg_catalog | row_to_json               | json             | record, boolean
| normal
 pg_catalog | to_json                   | json             | anyelement
| normal
(24 rows)
```

Basic usage

```
=> SELECT array_to_json('{{1,5},{99,100}}'::int[]);
  array_to_json
------------------
 [[1,5],[99,100]]
(1 row) => SELECT row_to_json(row(1,'foo'));
```

```json
     row_to_json
---------------------
 {"f1":1,"f2":"foo"}
(1 row) => SELECT json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]');
 json_array_length
------------------- (1 row) => select * from json_each('{"f1":[1,2,3],"f2":{"f3":1},"f4":null,"f5":99,"f6":"stringy"}')
```

q;

```json
 key |   value
-----+-----------
 f1  | [1,2,3]
 f2  | {"f3":1}
 f4  | null
 f5  | 99
 f6  | "stringy"
(5 rows) => select json_each_text('{"f1":[1,2,3],"f2":{"f3":1},"f4":null,"f5":"null"}');
  json_each_text
-------------------
 (f1,"[1,2,3]")
 (f2,"{""f3"":1}")
 (f4,)
 (f5,null)
(4 rows) => select json_array_elements('[1,true,[1,[2,3]],null,{"f1":1,"f2":[7,8,9]},false]');
  json_array_elements
-----------------------
 true
 [1,[2,3]]
 null
 {"f1":1,"f2":[7,8,9]}
 false
(6 rows) create type jpop as (a text, b int, c timestamp); => select * from json_populate_record(null::jpop,'{"a":"blurfl","x":43.2}', false) q;
   a    | b | c
--------+---+---
 blurfl |   |
(1 row) => select * from json_populate_recordset(null::jpop,'[{"a":"blurfl","x":43.2},{"b":3,"c ":"2012-01-20 10:42:53"}]',false) q;
   a    | b |            c
--------+---+--------------------------
 blurfl |   |
        | 3 | Fri Jan 20 10:42:53 2012
(2 rows)
```

Code examples Creat e a t able

```json
create table tj(id serial, ary int[], obj json, num integer); => insert into tj(ary, obj, num) values('{1,5}'::int[], '{"obj":1}', 5); INSERT 0 1 => select row_to_json(q) from (select id, ary, obj, num from tj) as q;
                row_to_json
-------------------------------------------
 {"f1":1,"f2":[1,5],"f3":{"obj":1},"f4":5}
(1 row) => insert into tj(ary, obj, num) values('{2,5}'::int[], '{"obj":2}', 5); INSERT 0 1 => select row_to_json(q) from (select id, ary, obj, num from tj) as q;
                row_to_json
-------------------------------------------
 {"f1":1,"f2":[1,5],"f3":{"obj":1},"f4":5}
 {"f1":2,"f2":[2,5],"f3":{"obj":2},"f4":5}
(2 rows)
```

Join mult iple t ables

```
create table tj2(id serial, ary int[], obj json, num integer); => insert into tj2(ary, obj, num) values('{2,5}'::int[], '{"obj":2}', 5); INSERT 0 1 => select * from tj, tj2 where tj.obj->>'obj' = tj2.obj->>'obj';
 id |  ary  |    obj    | num | id |  ary  |    obj    | num
----+-------+-----------+-----+----+-------+-----------+-----
  2 | {2,5} | {"obj":2} |   5 |  1 | {2,5} | {"obj":2} |   5
(1 row) => select * from tj, tj2 where json_object_field_text(tj.obj, 'obj') = json_object_field_te xt(tj2.obj, 'obj');
 id |  ary  |    obj    | num | id |  ary  |    obj    | num
----+-------+-----------+-----+----+-------+-----------+-----
  2 | {2,5} | {"obj":2} |   5 |  1 | {2,5} | {"obj":2} |   5
(1 row)
```

Use t he JSON f unct ion index

```
CREATE TEMP TABLE test_json (
       json_type text,
       obj json
```

);

```json
=> insert into test_json values('aa', '{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}'); INSERT 0 1 => insert into test_json values('cc', '{"f7":{"f3":1},"f8":{"f5":99,"f6":"foo"}}'); INSERT 0 1 => select obj->'f2' from test_json where json_type = 'aa';
 ? column?
----------
 {"f3":1}
(1 row) => create index i on test_json (json_extract_path_text(obj, '{f4}')); CREATE INDEX => select * from test_json where json_extract_path_text(obj, '{f4}') = '{"f5":99,"f6":"foo" }';
 json_type |                 obj
-----------+-------------------------------------------
 aa        | {"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}
(1 row)
```

> Not e
> JSON data cannot be used as the partition key and does not support JSON aggregate functions.

Example of using Python to access the database:

```java
#! /bin/env python
import time import json import psycopg2 def gpquery(sql):
    conn = None
    try:
        conn = psycopg2.connect("dbname=sanity1x2")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        if conn:
            try:
                conn.close()
            except:
                pass
            time.sleep(10)
        print e
    return None
def main(_):
    sql = "select obj from tj;"
    #rows = Connection(host, port, user, pwd, dbname).query(sql)
    rows = gpquery(sql)
    for row in rows:
        print json.loads(row[0])
if __name__ == '__main__':
    main()
```

### 4.9 Use HyperLogLog

AnalyticDB for PostgreSQL is highly optimized by Alibaba Cloud, and not only has the features of Greenplum Database, but also supports HyperLogLog. It is suitable for industries such as Internet advertising and estimation analysis that require quick estimation of business metrics such as PV and UV. Create a HyperLogLog extension You can execute the following statement to create a HyperLogLog extension:

```
 CREATE EXTENSION hll;
```

Basic types Execute the following statement to create a table containing the hll field:

```
 create table agg (id int primary key,userids hll);
```

Execute the following statement to convert int to hll_hashval:

```
 select 1::hll_hashval;
```

Basic operators The hll type supports =, !=, <>, ||, and #.

```
select hll_add_agg(1::hll_hashval) = hll_add_agg(2::hll_hashval); select hll_add_agg(1::hll_hashval) || hll_add_agg(2::hll_hashval); select #hll_add_agg(1::hll_hashval);
```

The hll_hashval type supports =, !=, and <>.

```
select 1::hll_hashval = 2::hll_hashval; select 1::hll_hashval <> 2::hll_hashval;
```

Basic functions Hash functions such as Hll_hash_boolean, hll_hash_smallint, and hll_hash_bigint.

```
select hll_hash_boolean(true); select hll_hash_integer(1);
```

hll_add_agg: converts the int format to the hll format.

```
 select hll_add_agg(1::hll_hashval);
```

hll_union: aggregates the hll fields.

```
 select hll_union(hll_add_agg(1::hll_hashval),hll_add_agg(2::hll_hashval));
```

hll_set_defaults: sets the precision.

```
 select hll_set_defaults(15,5,-1,1);
```

hll_print: displays debug information.

```
 select hll_print(hll_add_agg(1::hll_hashval));
```

Examples

```
create table access_date (acc_date date unique, userids hll); insert into access_date select current_date, hll_add_agg(hll_hash_integer(user_id)) from ge nerate_series(1,10000) t(user_id); insert into access_date select current_date-1, hll_add_agg(hll_hash_integer(user_id)) from generate_series(5000,20000) t(user_id); insert into access_date select current_date-2, hll_add_agg(hll_hash_integer(user_id)) from generate_series(9000,40000) t(user_id); postgres=# select #userids from access_date where acc_date=current_date;
     ? column?
------------------
 9725.85273370708
(1 row) postgres=# select #userids from access_date where acc_date=current_date-1;
     ? column?
------------------
 14968.6596883279
(1 row) postgres=# select #userids from access_date where acc_date=current_date-2;
     ? column?
------------------
 29361.5209149911
(1 row)
```

### 4.10 Use the CREATE LIBRARY statement

statement AnalyticDB for PostgreSQL introduces the CREATE LIBRARY and DROP LIBRARY statements to allow you to import custom software packages. Syntax

```
CREATE LIBRARY library_name LANGUAGE [JAVA] FROM oss_location OWNER ownername CREATE LIBRARY library_name LANGUAGE [JAVA] VALUES file_content_hex OWNER ownername DROP LIBRARY library_name
```

Parameters

| Parameter | Description |
|---|---|
| library name _ | The name of the library to be installed. If the library to be installed has the same name as an existing library, you must delete the existing library before installing the new one. |
| LANGUAGE [JAVA] | The programming language to be used. Only PL/Java is supported. |
| oss location _ | The location of the package. You can specify the OSS bucket and object names. Only one object can be specified and the specified object cannot be a compressed file. The format is as follows: oss://oss endpoint filepath= _ [folder/[folder/]...]/file name id=userossid _ key=userosskey bucket=ossbucket |
| file content hex _ _ | The content of the file. The byte stream is in hexadecimal notation. For example, 73656c6563742031 indicates the hexadecimal byte stream of "select 1". You can use this syntax to import packages without using OSS. |
| ownername | Specifies the user. |
| DROP LIBRARY | Deletes a library. |

Examples Example 1: Install a JAR package named analytics.jar.

```
create library example language java from 'oss://oss-cn-hangzhou.aliyuncs.com filepath=an alytics.jar id=xxx key=yyy bucket=zzz';
```

Example 2: Import the file content with the byte stream in hexadecimal notation.

```
create library pglib LANGUAGE java VALUES '73656c6563742031' OWNER "myuser";
```

Example 3: Delete a library.

```
drop library example;
```

Example 4: View installed libraries.

```
select name, lanname from pg_library;
```

### 4.11 Create and use the PL/Java UDF

AnalyticDB for PostgreSQL allows you to compile and upload JAR software packages written in PL/Java language, and use these JAR packages to create user-defined functions (UDFs). The PL/Java language supported by AnalyticDB for PostgreSQL is Community Edition PL/Java 1.5.0 and the JVM version is 1.8. This topic describes how to create a PL/Java UDF. For more information about PL/Java examples, see PL/Java code. For more information about the compiling method, see PL/Java documentation. Procedure
1. In AnalyticDB for PostgreSQL, execute the following statement to create a PL/Java extension. You
only need to execute the statement once for each database.

```
create extension pljava;
```

2. Compile the UDF based on your business needs. For example, you can use the following code to
compile the Test.java file:

```java
public class Test
```

`{`

```
     public static String substring(String text, int beginIndex,
               int endIndex)
```

`{`

```
                     try {
                         Process process = null;
                         process = Runtime.getRuntime().exec("ech Test running");
                     } catch (Exception e) {
                        return "" + e;
```

`}`

```
                     return text.substring(beginIndex, endIndex);
```

`}` `}`
3. Compile the manifest.txt file:

```
 Manifest-Version: 1.0
 Main-Class: Test
 Specification-Title: "Test"
 Specification-Version: "1.0"
 Created-By: 1.7.0_99
 Build-Date: 01/20/2016 21:00 AM
```

4. Run the following commands to compile and package the program:

```
javac Test.java
 jar cfm analytics.jar manifest.txt Test.class
```

5. Upload the analytics.jar file generated in step 4 to OSS by using the following OSS console
command.

```
 osscmd put analytics.jar oss://zzz
```

6. In AnalyticDB for PostgreSQL, execute the CREATE LIBRARY statement to import the file to
AnalyticDB for PostgreSQL:

```
create library example language java from 'oss://oss-cn-hangzhou.aliyuncs.com filepath= analytics.jar id=xxx key=yyy bucket=zzz';
```

> Not e You can only use the filepath variable in the CREATE LIBRARY statement to import files one at a time. Additionally, the CREATE LIBRARY statement also supports byte streams to import files without using OSS. For more information, see Use the CREATE LIBRARY statement.

7. In AnalyticDB for PostgreSQL, execute the following statements to create and use the UDF.

```
create table temp (a varchar) distributed randomly;
 insert into temp values ('my string');
 create or replace function java_substring(varchar, int, int) returns varchar as 'Test.
substring' language java;
 select java_substring(a, 1, 5) from temp;
```

## 5 Table

### 5.1 Create a table

You can create tables within your databases. Syntax The complete syntax for creating a table is as follows. Depending on your business needs, not all clauses will be required. Use the clauses that can fulfill your business needs.

```
CREATE [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name ( [ { column_namedata_type [ DEFAULT default_expr ]
   [column_constraint [ ... ]
[ ENCODING ( storage_directive [,...] ) ]
```

`]`

```
   | table_constraint
   | LIKE other_table [{INCLUDING | EXCLUDING}
                      {DEFAULTS | CONSTRAINTS}] ...}
   [, ... ] ]
```

`)`

```
   [ INHERITS ( parent_table [, ... ] ) ]
   [ WITH ( storage_parameter=value [, ... ] )
   [ ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP} ]
   [ TABLESPACE tablespace ]
   [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
   [ PARTITION BY partition_type (column)
       [ SUBPARTITION BY partition_type (column) ]
          [ SUBPARTITION TEMPLATE ( template_spec ) ]
       [...]
    ( partition_spec )
        | [ SUBPARTITION BY partition_type (column) ]
          [...]
    ( partition_spec
      [ ( subpartition_spec
           [(...)]
         ) ]
```

`)` The column_constraint clause can be defined as follows:

```
[CONSTRAINT constraint_name]
   NOT NULL | NULL
   | UNIQUE [USING INDEX TABLESPACE tablespace]
            [WITH ( FILLFACTOR = value )]
   | PRIMARY KEY [USING INDEX TABLESPACE tablespace]
                 [WITH ( FILLFACTOR = value )]
   | CHECK ( expression )
   | REFERENCES table_name [ ( column_name [, ... ] ) ]
            [ key_match_type ]
            [ key_action ]
```

The storage_directive clause of columns can be defined as follows:

```
   COMPRESSTYPE={ZLIB | QUICKLZ | RLE_TYPE | NONE}
    [COMPRESSLEVEL={0-9} ]
    [BLOCKSIZE={8192-2097152} ]
```

The storage_parameter clause of tables can be defined as follows:

```
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   CHECKSUM={TRUE|FALSE}
   COMPRESSTYPE={ZLIB|QUICKLZ|RLE_TYPE|NONE}
   COMPRESSLEVEL={0-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

The table_constraint clause can be defined as follows:

```
   [CONSTRAINT constraint_name]
   UNIQUE ( column_name [, ... ] )
          [USING INDEX TABLESPACE tablespace]
          [WITH ( FILLFACTOR=value )]
   | PRIMARY KEY ( column_name [, ... ] )
                 [USING INDEX TABLESPACE tablespace]
                 [WITH ( FILLFACTOR=value )]
   | CHECK ( expression )
   | FOREIGN KEY ( column_name [, ... ] )
            REFERENCES table_name [ ( column_name [, ... ] ) ]
            [ key_match_type ]
            [ key_action ]
            [ key_checking_mode ]
```

Valid values of key_match_type:

```
    MATCH FULL
  | SIMPLE
```

Valid values of key_action:

```
    ON DELETE
  | ON UPDATE
  | NO ACTION
  | RESTRICT
  | CASCADE
  | SET NULL
  | SET DEFAULT
```

Valid values of key_checking_mode:

```
    DEFERRABLE
  | NOT DEFERRABLE
  | INITIALLY DEFERRED
  | INITIALLY IMMEDIATE
```

Valid values of partition_type:

```
    LIST
  | RANGE
```

The partition_specification clause can be defined as follows:

```
partition_element [, ...]
```

The partition_element clause can be defined as follows:

```
   DEFAULT PARTITION name
  | [PARTITION name] VALUES (list_value [,...] )
  | [PARTITION name]
     START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
  | [PARTITION name]
     END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
[ WITH ( partition_storage_parameter=value [, ... ] ) ] [ TABLESPACE tablespace ]
```

The subpartition_spec or template_spec clause can be defined as follows:

```
subpartition_element [, ...]
```

The subpartition_element clause can be defined as follows:

```
   DEFAULT SUBPARTITION name
  | [SUBPARTITION name] VALUES (list_value [,...] )
  | [SUBPARTITION name]
     START ([datatype] 'start_value') [INCLUSIVE | EXCLUSIVE]
     [ END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE] ]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
  | [SUBPARTITION name]
     END ([datatype] 'end_value') [INCLUSIVE | EXCLUSIVE]
     [ EVERY ([datatype] [number | INTERVAL] 'interval_value') ]
[ WITH ( partition_storage_parameter=value [, ... ] ) ] [ TABLESPACE tablespace ]
```

The storage_parameter clause of partitions can be defined as follows:

```
   APPENDONLY={TRUE|FALSE}
   BLOCKSIZE={8192-2097152}
   ORIENTATION={COLUMN|ROW}
   CHECKSUM={TRUE|FALSE}
   COMPRESSTYPE={ZLIB|QUICKLZ|RLE_TYPE|NONE}
   COMPRESSLEVEL={1-9}
   FILLFACTOR={10-100}
   OIDS[=TRUE|FALSE]
```

Parameters The table describes the key parameters for creating a table. Table creation parameters

| Parameter | Description |
|---|---|
| TABLE NAME _ | The name of the table to be created. |
| column name _ | The name of a column to be created in the new table. |
| data type _ | The data type of the column. For columns that contain textual data, set the data type to VARCHAR or TEXT. We do not recommend the CHAR type. |
| DEFAULT default expr _ | Specifies a default value for the column. The system will assign this default value to all columns that do not have a value. The default values can be any variable-free expression. Subqueries or cross-references to other columns in the table are not allowed. The data type of the default expression must match the data type of the column. If a column does not have a default value, the default value is null. |
| ENCODING storage directive _ | Specifies the type of compression and block size for the column data. This clause is valid only for append-optimized, column-oriented tables. Column compression settings are inherited from the table level to the partition level to the sub-partition level. The lowest-level settings have priority over inherited settings. |
| INHERITS | Specifies that all columns in the new table automatically inherit a parent table. You can use INHERITS to create a persistent relationship between the new child table and its parent table. Schema modifications to the parent table are applied to the child table as well. When the parent table is also scanned, the data of the child table is scanned as well. |
| LIKE other table _ | Specifies a table from which the new table automatically copies all column names, data types, NOT NULL constraints, and distribution policies. Storage properties such as append-optimized or partition structure are not copied. Unlike INHERITS, the new table is completely decoupled from the original table after the new table is created. |

| Parameter | Description |
|---|---|
| CONSTRAINT constraint name _ | Configures a column or table constraint. When a constraint is violated, the constraint name will be displayed in the error message. Constraint names can be used to communicate helpful information to client applications. Constraint names that contain spaces must be enclosed by double quotation marks (''). |
| WITH ( storage option=value ) _ | Configures storage options for the table or its indexes. |
| ON COMMIT | The operation that the system performs on the temporary tables at the end of a transaction. Valid values: PRESERVE ROWS: No special action is taken. The data will be retained after the transaction is complete. The data will only be released when the session is disconnected. DELET E ROWS: All rows in the temporary table are deleted. DROP: The temporary table is deleted. |
| TABLESPACE tablespace | Specifies the name of the tablespace in which the new table is to be created. If not specified, the default tablespace of the database is used. |
| DISTRIBUTED BY | Specifies the distribution policy for the database. DISTRIBUTED BY (column, [ ... ] ): specifies the partition key. The system uses hash distribution based on the distribution key. To evenly distribute data, you must set the partition key to the primary key of the table or a unique column or a set of columns. DISTRIBUTED RANDOMLY: distributes data randomly. Not e We recommend that you do not use random distribution. |
| PARTITION BY | Configures the partition key to partition the table. Partitioning large tables improves data access efficiency. To partition a table is to create a top-level (parent) table and multiple lower- level (child) tables. A parent table is always empty when the partition table is created. Data is stored in the lowest-level child tables. In a multi-level partition table, data is only stored in the lowest-level sub-partitions. Valid values: RANGE, LIST, and a combination of the two. |
| SUBPARTITION BY | Configures a multi-level partitioned table. |
| SUBPARTITION TEMPLATE | You can specify a sub-partition template to create sub-partitions (lower-level child tables). This sub-partition template is applied to all parent partitions to ensure the same sub-partition structure. |

Examples Create a table and configure the partition key. The primary key is the default partition key in AnalyticDB for PostgreSQL.

```
CREATE TABLE films ( code char(5) CONSTRAINT firstkey PRIMARY KEY, title varchar(40) NOT NULL, did integer NOT NULL, date_prod date, kind varchar(10), len interval hour to minute
```

);

```
CREATE TABLE distributors ( did integer PRIMARY KEY DEFAULT nextval('serial'), name varchar(40) NOT NULL CHECK (name <> '')
```

); Create a compressed table and configure the partition key.

```
CREATE TABLE sales (txn_id int, qty int, date date) WITH (appendonly=true, compresslevel=5) DISTRIBUTED BY (txn_id);
```

Use sub-partition templates of each level and the default partition to create a three-level partition table.

```
CREATE TABLE sales (id int, year int, month int, day int, region text) DISTRIBUTED BY (id) PARTITION BY RANGE (year)
  SUBPARTITION BY RANGE (month)
    SUBPARTITION TEMPLATE (
       START (1) END (13) EVERY (1),
       DEFAULT SUBPARTITION other_months )
  SUBPARTITION BY LIST (region)
    SUBPARTITION TEMPLATE (
       SUBPARTITION usa VALUES ('usa'),
       SUBPARTITION europe VALUES ('europe'),
       SUBPARTITION asia VALUES ('asia'),
       DEFAULT SUBPARTITION other_regions)
( START (2008) END (2016) EVERY (1),
  DEFAULT PARTITION outlying_years);
```

### 5.2 Principles and scenarios of row store, column store, heap tables, and AO tables

store, column store, heap tables, and AO tables AnalyticDB for PostgreSQL supports row store, column store, heap tables, and AO tables. This topic describes their principles and scenarios. Row store and column store Comparison

| Dimension | Row store | Column store |
|---|---|---|
| Definition | Row store stores data in the form of rows. Each row is a tuple. To read a column, you must deform all of the columns that precede the target column. Because of this, the costs for accessing the first and the last columns are different. | Column store stores data as columns corresponding to a file or a batch of files. The cost of reading any column is the same. However, if you need to read multiple columns, you must access multiple files. The more columns you access, the higher the overheads are. |
| Compression ratio | Low. | High. |
| Cost of reading any column | Columns with larger column numbers cost more. | Same. |
| Vector computing and JIT architecture | Not suitable. Not suitable for batch computation. | Suitable. More efficient when accessing and obtaining statistics of a batch of data. |
| Scenarios | If you need to perform a large number of update and delete operations due to OLTP requirements such as when querying table details where multiple columns are returned, you can use row store. You can use partition tables if you have diversified requirements. For example, if you need to partition the data based on time, you can use row store to query the details of recent data and use column store to obtain more statistics from historical data. | You can use column store if you need data statistics because of the OLAP requirements. If you need a higher compression ratio, you can use column store. |

Heap tables A heap table is heap storage. All changes to the heap table generate redo logs that can be used to restore data by time point. However, heap tables cannot implement logical incremental backup because any data block in the table may be changed and it is not convenient to record the position by using the heap storage. Commit and redo logs are used to ensure reliability when transactions are finished. You can also implement redundancy by building secondary nodes through redo logs. Append-optimized (AO) tables AO tables are used to append data for storage. When you delete the updated data, you can use another bitmap file to mark the row to be deleted and use the bit and offset to determine whether a row is deleted. When the transaction is finished, you must call the fsync function to record the offset of the data block that performs the last write operation. Even if the data block only contains one record, a new data block will be appended for the next transaction. The data block is synchronized to the secondary node for data redundancy. AO tables are not suitable for small transactions because the fsync function is called at the end of each transaction, and this data block will not be reused even if there is space left. AO tables are suitable for OLAP scenarios, batch data writing, high compression ratio, and logical backup that supports incremental backup. During backup, you only need to record the offset from the backup and the bitmap deletion mark for each full backup. Usage scenarios of heap tables When multiple small transactions are handled, use a heap table. When you need to restore data by time point, use a heap table. Usage scenarios of AO tables When you need to use column store, use an AO table. When data is written in batches, use an AO table.

### 5.3 Enable the column store and compression features

compression features If you want to improve performance, speed up data import, or reduce costs for tables with infrequent updates and multiple fields, we recommend that you use column store and compression. This will increase the compression ratio threefold to ensure faster performance and import speed. To enable the column store and compression features, you must specify the column store and compression options when creating a table. For example, you can add the following clause to the CREATE statement to enable the two features. For more information about the table creation syntax, see Create a table.

```
with (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, BLOCKSIZE=10 48576, OIDS=false)
```

> Not e AnalyticDB for PostgreSQL only supports zlib and RLE_TYPE compression algorithms. If you specify the quicklz algorithm, it is automatically converted to zlib.

### 5.4 Add a field to a column store table and set the default value

table and set the default value This topic describes how to add a field to a column store table and set the default value for the field, and how to use the ANALYZE statement to view the impact of updated data on the size of the column store table. Context In a column store table, each column is stored as a file, and two columns in the same row correspond to each other by using the offset. For example, if you add two fields of the INT8 type, you can quickly locate column B from column A by using the offset. When you add the field, AO tables are not rewritten. If an AO table contains the records of deleted data, the added field must be filled with the deleted records before using the offset. Procedure
1. Create three AO column store tables.

```
postgres=# create table tbl1 (id int, info text) with (appendonly=true, blocksize=8192, compresstype=none, orientation=column); NOTICE: Table doesn't have 'DISTRIBUTED BY' clause -- Using column named 'id' as the G reenplum Database data distribution key for this table. HINT: The 'DISTRIBUTED BY' clause determines the distribution of data. Make sure colum n(s) chosen are the optimal data distribution key to minimize skew. CREATE TABLE postgres=# create table tbl2 (id int, info text) with (appendonly=true, blocksize=8192, compresstype=none, orientation=column); NOTICE: Table doesn't have 'DISTRIBUTED BY' clause -- Using column named 'id' as the G reenplum Database data distribution key for this table. HINT: The 'DISTRIBUTED BY' clause determines the distribution of data. Make sure colum n(s) chosen are the optimal data distribution key to minimize skew. CREATE TABLE postgres=# create table tbl3 (id int, info text) with (appendonly=true, blocksize=8192, compresstype=none, orientation=column); NOTICE: Table doesn't have 'DISTRIBUTED BY' clause -- Using column named 'id' as the G reenplum Database data distribution key for this table. HINT: The 'DISTRIBUTED BY' clause determines the distribution of data. Make sure colum n(s) chosen are the optimal data distribution key to minimize skew. CREATE TABLE
```

2. Insert 10 million entries to the first two tables and 20 million entries to the third one.

```
postgres=# insert into tbl1 select generate_series(1,10000000),'test'; INSERT 0 10000000 postgres=# insert into tbl2 select generate_series(1,10000000),'test'; INSERT 0 10000000 postgres=# insert into tbl3 select generate_series(1,20000000),'test'; INSERT 0 20000000
```

3. Analyze the tables and display their sizes.

```
postgres=# analyze tbl1; ANALYZE postgres=# analyze tbl2; ANALYZE postgres=# analyze tbl3; ANALYZE postgres=# select pg_size_pretty(pg_relation_size('tbl1'));
 pg_size_pretty
----------------
 88 MB
(1 row) postgres=# select pg_size_pretty(pg_relation_size('tbl2'));
 pg_size_pretty
----------------
 88 MB
(1 row) postgres=# select pg_size_pretty(pg_relation_size('tbl3'));
 pg_size_pretty
----------------
 173 MB
(1 row)
```

4. Update all the data in the first table. Display the table size after the update. The size is twice as
large as the size before the update.

```
postgres=# update tbl1 set info='test'; UPDATE 10000000 postgres=# analyze tbl1; ANALYZE postgres=# select pg_size_pretty(pg_relation_size('tbl1'));
 pg_size_pretty
----------------
 173 MB
(1 row)
```

5. Add fields to the three tables and set the default values.

```
postgres=# alter table tbl1 add column c1 int8 default 1; ALTER TABLE postgres=# alter table tbl2 add column c1 int8 default 1; ALTER TABLE postgres=# alter table tbl3 add column c1 int8 default 1; ALTER TABLE
```

6. Analyze the tables and view the table sizes.

```
postgres=# analyze tbl1; ANALYZE postgres=# analyze tbl2; ANALYZE postgres=# analyze tbl3; ANALYZE postgres=# select pg_size_pretty(pg_relation_size('tbl1'));
 pg_size_pretty
----------------
 325 MB
(1 row) postgres=# select pg_size_pretty(pg_relation_size('tbl2'));
 pg_size_pretty
----------------
 163 MB
(1 row) postgres=# select pg_size_pretty(pg_relation_size('tbl3'));
 pg_size_pretty
----------------
 325 MB
(1 row)
```

When you add fields to the AO tables, the number of entries in the existing files will prevail. Even if all the entries are deleted, you must initialize the original data in the newly added fields.

### 5.5 Configure the table partition

For fact tables or large-sized tables in the database, we recommend that you configure table partitions. Configure the table partition You can use the table partitioning feature to delete data by using the `ALTER TABLE DROP PARTITION` statement to delete all the data in a partition, and import data by using the `ALTER TABLE EXCHANGE` `PARTITION` statement to add a new data partition on a regular basis. AnalyticDB for PostgreSQL supports range partitioning, list partitioning, and composite partitioning. Range partitioning only supports partitioning by fields of the numeric or datetime data types. The following example shows a table that uses range partitioning.

```
CREATE TABLE LINEITEM ( L_ORDERKEY BIGINT NOT NULL, L_PARTKEY BIGINT NOT NULL, L_SUPPKEY BIGINT NOT NULL, L_LINENUMBER INTEGER, L_QUANTITY FLOAT8, L_EXTENDEDPRICE FLOAT8, L_DISCOUNT FLOAT8, L_TAX FLOAT8, L_RETURNFLAG CHAR(1), L_LINESTATUS CHAR(1), L_SHIPDATE DATE, L_COMMITDATE DATE, L_RECEIPTDATE DATE, L_SHIPINSTRUCT CHAR(25), L_SHIPMODE CHAR(10), L_COMMENT VARCHAR(44) ) WITH (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, BLOCKSIZ E=1048576, OIDS=false) DISTRIBUTED BY (l_orderkey) PARTITION BY RANGE (L_SHIPDATE) (START (date '1992-01-01') INCLUSIVE END (date '2000-01-01' ) EXCLUSIVE EVERY (INTERVAL '1 month' ));
```

Principles of table partitioning The purpose of partitioning is to minimize the amount of data that needs to be scanned during a query, so partitions must be associated with the query conditions. Principle 1: Select the fields related to the query conditions to configure partitions and reduce the amount of data to be scanned. Principle 2: When multiple query conditions exist, configure sub-partitions to further reduce the amount of data to be scanned.

### 5.6 Configure the sort key

A sort key is an attribute of a table. Data on disks is stored in the order of the sort key. Context Sort keys have two major advantages: Speed up and optimize column-store operations. The min and max meta information the system collects seldom overlaps with each other, which features good filterability. Eliminate the need to perform ORDER BY and GROUP BY operations. The data directly read from the disk is ordered as required by the sorting conditions. Create a table

```
Command: CREATE TABLE Description: define a new table Syntax: CREATE [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name ( [ { column_name data_type [ DEFAULT default_expr ] [column_constraint [ ... ] [ ENCODING ( storage_directive [,...] ) ]
```

`]`

```
   | table_constraint
   | LIKE other_table [{INCLUDING | EXCLUDING}
                      {DEFAULTS | CONSTRAINTS}] ...}
   [, ... ] ]
   [column_reference_storage_directive [, ] ]
```

`)`

```
   [ INHERITS ( parent_table [, ... ] ) ]
   [ WITH ( storage_parameter=value [, ... ] )
   [ ON COMMIT {PRESERVE ROWS | DELETE ROWS | DROP} ]
   [ TABLESPACE tablespace ]
   [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
   [ SORTKEY (column, [ ... ] )]
   [ PARTITION BY partition_type (column)
       [ SUBPARTITION BY partition_type (column) ]
          [ SUBPARTITION TEMPLATE ( template_spec ) ]
       [...]
    ( partition_spec )
        | [ SUBPARTITION BY partition_type (column) ]
          [...]
    ( partition_spec
      [ ( subpartition_spec
           [(...)]
         ) ]
```

`)` Examples:

```
create table test(date text, time text, open float, high float, low float, volume int) with (APPENDONLY=true,ORIENTATION=column) sortkey (volume);
```

Sort the table

```
VACUUM SORT ONLY [tablename]
```

Modify the sort key This statement only modifies the catalog and does not sort data. You must execute the `VACUUM SORT` `ONLY` statement to sort the table.

```
ALTER [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name SET SORTKEY (column, [ ... ] )
```

Examples:

```
alter table test set sortkey (high,low);
```

## 6 Best practices

### 6.1 Configure memory and load parameters

parameters You must configure memory and load parameters to improve database stability. Background information AnalyticDB for PostgreSQL is an MPP database with high computational and resource requirements. It consumes all of the resources provided to it, allowing AnalyticDB for PostgreSQL to have higher processing speeds but making it very easy to reach its limits. The worst-case scenario in the event of the CPU, network, or hard disk exceeding its limits is a hardware bottleneck. However, in the event that memory is completely consumed, the database may crash. How to avoid OOM errors Out of memory (OOM) indicates that the system is unable to provide sufficient memory requested by a process. The following prompt appears when OOM errors occur:

```
Out of memory (seg27 host.example.com pid=47093) VM Protect failed to allocate 4096 bytes, 0 MB available
```

Causes Possible causes of the OOM error include: The memory of the database node is insufficient. Kernel parameters related to the memory of the operating system are incorrectly configured. Data skew has occurred, causing a compute node to request a large amount of memory. Query skew has occurred. For example, if the grouping fields of some aggregate or window functions are not distribution keys, the data must be redistributed. After redistribution, data will be skewed in a certain computer node and result in the node requesting a large amount of memory. Solut ions
1. Modify the queries to request less memory.
2. Use the resource queue provided by AnalyticDB for PostgreSQL to limit the number of concurrent
queries. Reduce the number of queries executed within the cluster at the same time to reduce the overall memory requested by the system.
3. Reduce the number of compute nodes deployed on a host. For example, deploy 8 compute nodes
instead of 16 compute nodes on a host with 128 GB of memory. This allows each compute node to use twice the amount of memory compared with the latter.
4. Increase the memory of a host.
5. Set the gp_vmem_protect_limit parameter to limit the maximum VMEM that can be used by a single
compute node. The memory size of a single host and the number of compute nodes deployed on the host determine the maximum memory size that a single compute node can use on average.
6. For SQL statements that have unpredictable memory usage, you can set the statement_mem
parameter in the session to limit the memory usage of a single SQL statement, so as to prevent a single SQL statement from consuming all available memory.
7. Set the statement_mem parameter at the database level to apply to all the sessions in the
database.
8. Use the resource queue to limit the maximum memory usage of the resource group. Add database
users to the resource group to limit the overall memory used by these users. Configure memory-related parameters Properly configuring the operating system, database parameters, and resource queue can effectively reduce the probability of OOM. When calculating the average memory usage of a single compute node on a single host, you must consider both the primary and secondary compute nodes. When the cluster encounters a host failure, the system will switch the service from primary compute nodes to the corresponding secondary compute nodes. During this time, the number of compute nodes on the host will be greater than usual. Therefore, you must consider the number of resources that will be occupied by the secondary compute nodes during failover. The following tables describe how to configure parameters of the operating system kernel and database to avoid OOM. The following table describes the parameter configuration of the operating system kernel. Operating system kernel parameters

| Parameter | Description |
|---|---|
| huge page | Do not configure the huge page parameter of the system. AnalyticDB for PostgreSQL does not support the latest version of PostgreSQL and therefore does not support the huge page feature. The huge page parameter locks a part of the allocated memory. Database nodes will not be able to use this part of the memory. |
| vm.overcommit memory _ | If you use the swap space, set this parameter to 2. If you do not use the swap space, set this parameter to 0. Valid values: 0: The requested memory space cannot exceed the difference between the total memory and the resident set size (RSS). An error is returned only when the memory has been exceeded. 1: Most processes use the malloc function to apply for the memory, but do not use all the memory applied. When this parameter is set to 1, the memory requested by the malloc function will be allocated under any circumstances unless there is not sufficient memory. 2: The swap space is also considered when the system calculates the memory space that can be applied for. You can apply for a large amount of memory even if the swap space is triggered. |

| Parameter | Description |
|---|---|
| overcommit ratio _ | The larger the value, the more memory that process can apply for and the less that will be reserved for the operating system. For the formula used to calculate the memory parameters, see Examples to calculate the memory parameters. When this parameter is set to 2, the memory address that can be applied for cannot exceed swap + memory × overcommit ratio. _ |

The following Database parameters table describes the parameter configuration of the database. Database parameters

| Parameter | Description |
|---|---|
| gp vmem protect limit _ _ _ | Specifies the maximum amount of memory that all processes can apply for on each node. If the value is too large, it may result in a system OOM error or even more serious problems. If the value is too small, SQL statements may not be executed even when the system has enough memory. |
| runaway detector activation _ _ _ percent | Default value: 90. This value is specified as a percentage. When the memory used by any compute node exceeds runaway detector activation percent × gp vmem protect limit/100, the _ _ _ _ _ _ query is terminated to prevent OOM. The termination starts from the query that occupies the maximum memory until the memory reaches a value lower than runaway detector activation percent × gp vmem protect limit/100. _ _ _ _ _ _ You can use the gp toolkit.session level memory consumption view to _ _ _ _ observe the memory usage of each session and runaway information. |

| Parameter | Description |
|---|---|
| statement mem _ | Specifies the maximum amount of memory that a single SQL statement can apply. When the maximum memory is exceeded, spill files are created. Default value: 125. Unit: MB. We recommend that you set this parameter according to the following formula: (gp vmem protect limit × _ _ _ 0.9)/max expected concurrent queries _ _ _ Not e You can specify the statement mem parameter in a session. If _ the current concurrency is low and a session needs to run a query that requires a large amount of memory, you must specify this parameter in the session. Statement mem is suitable for limiting memory usage in low _ concurrency scenarios. If you use statement mem to limit the _ memory for high concurrency scenarios, each query is allocated with a very small amount of memory. As a result, the performance of a small number of queries with high memory requirements in high concurrency scenarios is affected. We recommend that you use the resource queue to limit the maximum memory usage in high concurrency scenarios. |
| gp workfile limit files per q _ _ _ _ _ uery | Specifies the maximum number of spill files that can be created by each query. When the memory requested by the query exceeds the statement mem limit, spill files (also known as work files) are created, _ which is similar to the swap space of the operating system. When the number of spill files used exceeds the limit, the query will be terminated. Default value: 0, which indicates that an unlimited number of spill files can be created. |
| gp workfile compress algori _ _ _ thm | Specifies the compression algorithm for spill files. Valid values: none and zlib. Specifies the compression algorithm. The values optimize storage space or I/O by sacrificing CPU. You can set this parameter when the disk is insufficient or the spill files meet a write bottleneck. |

Examples to calculate the memory parameters The environment is as follows: Host configuration:

```
Total RAM = 256 GB SWAP = 64 GB
```

Four hosts, each deployed with eight primary compute nodes and eight secondary compute nodes. When a host fails, the eight primary compute nodes are distributed to the remaining three hosts. A single host can be deployed with at most three extra primary compute nodes from the failed host. A single host can be deployed with at most 11 primary compute nodes.
1. Calculate the total memory allocated to AnalyticDB for PostgreSQL by the operating system.
Reserve 7.5 GB and 5% of memory for the operating system and calculate the available memory for all applications, and divide the available memory by the empirical coefficient of 1.7.

```
gp_vmem = ((SWAP + RAM) - (7.5 GB + 0.05 × RAM))/1.7
        = ((64 + 256) - (7.5 + 0.05 × 256))/1.7
        = 176
```

2. Use the empirical coefficient of 0.026 to calculate overcommit_ratio.

```
vm.overcommit_ratio = (RAM - (0.026 × gp_vmem))/RAM
                    = (256 - (0.026 × 176))/256
                    =. 982
Set vm.overcommit_ratio to 98.
```

3. Calculate gp_vmem_protect_limit (the protection parameter of the maximum memory usage for
each compute node), and divide gp_vmem by maximum_acting_primary_segments (the number of primary compute nodes to be run on each other host after one host fails).

```
gp_vmem_protect_limit calculation gp_vmem_protect_limit = gp_vmem/maximum_acting_primary_segments
                      = 176/11
                      = 16 GB
                      = 16384 MB
```

Configure the resource queue You can use resource queues to limit the number of concurrent queries and the total memory usage. When a query is running, it is added to the corresponding queue and the resources used are recorded in the queue. The resource limit of the queue is applied to all sessions in the queue. The resource queue in AnalyticDB for PostgreSQL is similar to cgroup in Linux. The syntax to create a resource queue is as follows:

```
Command: CREATE RESOURCE QUEUE Description: create a new resource queue for workload management Syntax: CREATE RESOURCE QUEUE name WITH (queue_attribute=value [, ... ]) where queue_attribute is:
   ACTIVE_STATEMENTS=integer
        [ MAX_COST=float [COST_OVERCOMMIT={TRUE|FALSE}] ]
        [ MIN_COST=float ]
        [ PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX} ]
        [ MEMORY_LIMIT='memory_units' ]
|  MAX_COST=float [ COST_OVERCOMMIT={TRUE|FALSE} ]
        [ ACTIVE_STATEMENTS=integer ]
        [ MIN_COST=float ]
        [ PRIORITY={MIN|LOW|MEDIUM|HIGH|MAX} ]
        [ MEMORY_LIMIT='memory_units' ]
```

The table describes the parameters for creating the resource queue. Resource queue creation parameters

| Parameter | Description |
|---|---|
| ACTIVE STATEMENTS _ | The number of SQL statements that are allowed to run (in the active state) concurrently. The value -1 indicates an unlimited number of SQL statements can run concurrently. |

| Parameter | Description |
|---|---|
| MEMORY LIMIT _ 'memory units kB, MB or _ GB' | Specifies the maximum memory usage allowed by all SQL statements in the resource queue. The value -1 indicates unlimited memory usage, but it is easy to trigger OOM errors because it is limited by the database or system parameters mentioned in the preceding sections. The memory usage of SQL statements is limited by resource queues and parameters. When the gp resqueue memory policy parameter is set to none, the limit is _ _ _ the same as that in the Greenplum databases earlier than version 4.1. When the gp resqueue memory policy parameter is set to auto and you _ _ _ have specified the statement mem parameter for a session or at the _ database level, the allowed memory of a single query will exceed the MEMORY LIMIT of the resource queue. _ Example: => SET statement mem='2GB'; _ => SELECT * FROM my big table WHERE column='value' ORDER BY _ _ id; => RESET statement mem; _ The system parameter max statement mem can limit the maximum _ _ memory usage at the compute node level. The memory requested by a single query cannot exceed max statement mem. _ _ You can modify the statement mem parameter at the session level, but do _ not modify the max statement mem parameter. We recommend that you _ _ specify max statement mem as follows: _ _ (seghost physical memory) / _ _ (average number concurrent queries) _ _ _ When the gp resqueue memory policy parameter is set to eager free, it _ _ _ _ indicates that the query is divided into several stages and that the database allocates the memory requested in the current stage. For example, if a query requests 1 GB of memory in total but only needs 100 MB during each stage, the database will allocate 100 MB of memory to the query. You can use eager free to reduce the possibility of insufficient _ memory for the query. |
| MAX COST float _ | The maximum cost of the queries that are allowed to execute concurrently by the resource group. The cost is the estimated total cost in the SQL execution plan. The value of the parameter can be specified as a floating-point number (such as 100.0) or an exponent (such as 1e+2). A value of -1 indicates the cost is unlimited. |
| COST OVERCOMMIT _ boolean | Specifies whether the limit of max cost can be exceeded when the system is _ idle. The value TRUE indicates the limit can be exceeded. |

| Parameter | Description |
|---|---|
| MIN COST float _ | When the resources requested exceed the limit, the queries are queued. However, when the cost of a query is lower than the min cost, the query can _ run without queuing. |
| PRIORITY= {MIN\|LOW\|MEDIUM\|HIGH\|MA X} | The priority of the current resource queue. When resources are insufficient, CPU resources are allocated to the resource queue with a higher priority. The SQL statements in the resource queue with a higher priority can obtain CPU resources first. We recommend that you allocate users that initiate queries with high real-time requirements to resource queues with higher priority. This parameter is similar to the CPU resource group in the Linux cgroup and the time slice policy of real-time and common tasks. |

Example of modifying resource queue limits:

```
ALTER RESOURCE QUEUE myqueue WITH (MAX_COST=-1.0, MIN_COST= -1.0);
```

Example of putting the user in the resource queue:

```
ALTER ROLE sammy RESOURCE QUEUE poweruser;
```

The following table describes the parameters of resource queues. Resource queue parameters

| Parameter | Description |
|---|---|
| gp resqueue memory policy _ _ _ | Specifies the memory management policy of the resource queue. |
| gp resqueue priority _ _ | Specifies whether to enable query prioritization. Valid values: On. Off. If this parameter is disabled, existing priority settings are not evaluated. |
| gp resqueue priority cpucores _ _ _ _ per segment _ | Specifies the number of CPU cores allocated to each compute node. For example, if an 8-core host is configured with two primary compute nodes, you can set the parameter to 4. If there are no other nodes on the primary node, set the parameter to 8. When the CPU is preempted, the SQL statements running in the resource group with higher priority are allocated with CPU resources first. |

| Parameter | Description |
|---|---|
| gp resqueue priority sweeper i _ _ _ _ nterval | Specifies the interval at which CPU utilization is recalculated for all active statements. The share value is calculated when the SQL statement is executed. You can calculate the share value based on the priority and gp resqueue priority cpucores per segment. _ _ _ _ _ The smaller the value and the more frequent the calculation, the better the result brought by the priority settings and the larger the overhead. |

Tips for configuring resource queues: We recommend that you create a resource queue for each user. The default resource queue of AnalyticDB for PostgreSQL is pg_default. If no queue is created, all users are assigned to pg_default. This operation is not recommended. We recommend that you create a resource queue for each user. Typically, a database user corresponds to a business. Different database users may correspond to different businesses or users, such as business users, analysts, developers, and DBAs. We do not recommend that you use superusers to execute queries. Queries initiated by superusers are only limited by the preceding parameters and not by the resource queue. We do not recommend that you use superusers to execute queries if you want to use resource queues to limit the use of resources. ACTIVE_STATEMENTS indicates the SQL statements that can be executed concurrently within the resource queue. When the cost of a query is lower than the min_cost, the query can run without queuing. You can specify the MEMORY_LIMIT parameter to set the allowed maximum memory usage of all the SQL statements in a resource queue. The statement_mem parameter has higher priority that can break through the limit of resource queues.

> Not e The memory of all resource queues cannot exceed gp_vmem_protect_limit.

You can distinguish businesses by configuring the priorities of resource queues. For example, assume that report forms have top priority, while common businesses and analysts have lower priorities. In this case, you can create three resource queues with the max, high, and medium priorities, respectively. If the number of resources requested at different times vary, you can use the crontab command to adjust the limits of resource queues periodically based on usage patterns. For example, the queue of analysts has top priority during the day, while the queue of forms has lower priority at night. AnalyticDB for PostgreSQL does not support resource limits by time period. Therefore, you can only deploy tasks externally by using the ALTER RESOURCE QUEUE statement. You can use the view provided by gp_toolkit to observe the resource usage of the resource queues.

```
gp_toolkit.gp_resq_activity gp_toolkit.gp_resq_activity_by_queue gp_toolkit.gp_resq_priority_backend gp_toolkit.gp_resq_priority_statement gp_toolkit.gp_resq_role gp_toolkit.gp_resqueue_status
```
