---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL User Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 259
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL User Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%8E%9F%E7%94%9F%E6%95%B0%E6%8D%AE%E4%BB%93%E5%BA%93AnalyticDB/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20AnalyticDB%20for%20MySQL%20AnalyticDB%20for%20PostgreSQL%20User%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 AnalyticDB for MySQL AnalyticDB for PostgreSQL User Guide 20260828

## Kernel version release

**notes**

This topic details the kernel version releases for AnalyticDB for PostgreSQL.

**Note**

For details on the updates, see the **hotfix release notes**, specifically the **AnalyticDB**
**for PostgreSQL** section.

**Release date: July 30, 2026**

Release v3.18.6r-paas-polardb-hotfeature-SP009 includes the following kernel versions for AnalyticDB for PostgreSQL:

| Product | Engine version | Minor kernel version |
|---|---|---|
| AnalyticDB for PostgreSQL | 7.0 | 7.2.1.12 |
|   | 7.0 Vector Edition | 7.2.1.12 |
|   | 6.0 | 6.6.2.20 |
|   | 6.0 Vector Edition | 6.6.2.20 |

reSQL?

## What is AnalyticDB for

**PostgreSQL?**

AnalyticDB for PostgreSQL is a distributed cloud database service that uses multiple compute nodes to provide massively parallel processing (MPP) data warehousing. AnalyticDB for PostgreSQL is developed based on the open source Greenplum database project and enhanced by Alibaba Cloud. This service has the following features: Compatible with Greenplum and all tools that support Greenplum. Supports Object Storage Service (OSS), JSON, and HyperLogLog, which is a probabilistic algorithm for cardinality estimation. Supports SQL:2003-compliant syntax and Online Analytical Processing (OLAP) aggregate functions to provide flexible hybrid analysis. Supports both row store and column store to enhance analytics performance. Supports data compression to reduce storage costs. Provides online scaling and performance monitoring to enable database administrators (DBAs), developers, and data analysts to focus on improving enterprise productivity and creating core business value instead of managing and maintaining large numbers of MPP clusters.

## Instance specifications

This topic describes the instance specifications supported by AnalyticDB for PostgreSQL.

**Differences between integrated storage mode and reserved**

**storage mode and their use scenarios**

| Mode | Recommended scenario |
|---|---|
| Integrated storage mode | Scenarios that have small business scale, simple architecture, development and testing tasks, and fixed-ratio workloads but require high performance. |
| Reserved storage mode | Scenarios that have large data volumes and require elastic resources, production data warehouses, cost optimization, and long-term operation. |

**Integrated storage mode**

**Instance specifications for engine version 4.3**

| Type | Specificatio n | Number of nodes | Memory size | CPU | Storage capacity |
|---|---|---|---|---|---|
| 1x2 SSD | gpdb.group.s egsdx2 | ["2","4","6","8 ","12"] | 16 GB | 2 Core | 160G |
| 1x16 SSD | gpdb.group.s egsdx16 | ["2","4","6","8 "] | 128 GB | 16 Core | 1280G |
| 4x4 SSD | gpdb.group.s egsd4cx4 | ["2","4","6","8 ","12","16","2 4","32"] | 128 GB | 16 Core | 1280G |
| 4x4SX SSD | gpdb.group.s egsd4cx4SX | ["2","4","6","8 ","12","24","3 2"] | 128 GB | 16 Core | 2560G |
| 4x4S3X SSD | gpdb.group.s egsd4cx4S3X | ["2","4","6","8 ","12","24","3 2"] | 128 GB | 16 Core | 3840G |

**Instance specifications for engine version 6.0**

| > Document Vers | ion: 20260828 |   |   |   | 1 |
|---|---|---|---|---|---|

| Type | Specificatio n | Number of nodes | Memory size | CPU | Storage capacity |
|---|---|---|---|---|---|
| 4x4 SSD | gpdb.group.s egsd4cx4 | ["2","4","6","8 ","12","16","2 4","32"] | 128 GB | 16 Core | 1280G |
| 4x4SX SSD | gpdb.group.s egsd4cx4SX | ["2","4","6","8 ","12","24","3 2"] | 128 GB | 16 Core | 2560G |
| 4x4S3X SSD | gpdb.group.s egsd4cx4S3X | ["2","4","6","8 ","12","24","3 2"] | 128 GB | 16 Core | 3840G |
| 8cx2 SSD | gpdb.group.s egsd8cx2 | ["2","4","6","8 ","12","16","2 4","32"] | 128 GB | 16 Core | 1280G |
| 8cx2SX SSD | gpdb.group.s egsd8cx2SX | ["2","4","6","8 ","12","16","2 4","32"] | 128 GB | 16 Core | 2560G |
| 8cx2S3X SSD | gpdb.group.s egsd8cx2S3X | ["2","4","6","8 ","12","16","2 4","32"] | 128 GB | 16 Core | 3840G |

**Reserved storage mode**

**Engine version 6.0**

| Type | Specification | CPU | Memory size | Storage capacity |
|---|---|---|---|---|
| 2 Cores, 16 GB (Low Concurrency) | 2C16G | 2 Core | 16 GB | 160G |
| 4 Cores, 32 GB (Medium Concurrency) | 4C32G | 4 Core | 32 GB | 160G |
| 8 Cores, 64 GB (High Concurrency) | 8C64G | 8 Core | 64 GB | 640G |

| 16 Cores, 128 GB (Ultra-High Concurrency) | 16C128G | 16 Core | 128 GB | 1280G |
|---|---|---|---|---|

**Engine version 6.0 vector**

| Type | Specification | CPU | Memory size | Storage capacity |
|---|---|---|---|---|
| 8 Cores, 64 GB (High Concurrency) | 8C64G | 8 Core | 64 GB | 640G |
| 16 Cores, 128 GB (Ultra-High Concurrency) | 16C128G | 16 Core | 128 GB | 1280G |
| 32 Cores, 256 GB (Ultra-high Concurrency) | 32C256G | 32 Core | 256 GB | 2560G |
| 64 Cores, 512 GB (Ultra-high Concurrency) | 64C512G | 64 Core | 512 GB | 5120 GB |

## Quick start

### Log in to the AnalyticDB for

**PostgreSQL console**

This topic describes how to log in to the AnalyticDB for PostgreSQL console.

**Prerequisites**

The URL of the console that is obtained from the deployment personnel. A supported browser is used. We recommend that you use Google Chrome.
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

**Note**

**First login**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

**Forgotten password**

If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.
3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging in to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator:**

a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the 6-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device:**

Enter the 6-digit MFA verification code and click **Authenticate**.

**Note**

For more information about how to enable MFA and bind an MFA device, see the
**Manage MFA** topic in Apsara Uni-manager Management Console User Guide.
5. In the top navigation bar, click **Products** and choose **Database Services > AnalyticDB**
**for PostgreSQL**.

### Create an instance

The first step is to create an AnalyticDB for PostgreSQL instance. You can quickly create an instance in the console.
1. Log on to the AnalyticDB for PostgreSQL console.
2. In the upper-left corner of the page, click **Create Instance**.
3. On the **AnalyticDB for PostgreSQL** instance creation page, configure the following
parameters.

| Category | Parameter | Description |
|---|---|---|
| Region | Organization/res ource set | The instance's organization and resource set. |
|   | Region/Primary AZ | Select the region and primary availability zone for the AnalyticDB for PostgreSQL instance. Note To access the instance from an ECS instance in a VPC, the AnalyticDB for PostgreSQL instance must be in the same region and availability zone as the ECS instance. |
|   | Deployment method | Select Single-AZ Deployment or Multi-AZ Deployment. |
|   | Secondary AZ | The secondary availability zone for the AnalyticDB for PostgreSQL instance. Note This parameter is displayed only when Deployment method is set to Multi-AZ Deployment. |
|   | Instance resource type | Select Compute and Storage Integrated Mode or Storage Reserved Mode. |
|   | Chip architecture | Select the chip architecture for the instance. Supported architectures include Intel (x86), Hygon (x86), Phytium (ARM), and Kunpeng (ARM). The available options depend on the hardware in your deployment environment and are displayed on the page. |

|   | Engine version | Select the engine version. Note Version 6.0 is available when Instance resource type is set to Compute and Storage Integrated Mode. Versions 6.0, 6.0 Vector Edition, 7.0, and 7.0 Vector Edition are available when Instance resource type is set to Storage Reserved Mode. |
|---|---|---|
| Basic configurations |   |   |
|   | Compute specification mode | You can select Shared Mode or Dedicated Mode. Note This parameter is displayed only when Instance resource type is set to Storage Reserved Mode. |
|   | Number of master nodes | The value is fixed at 1. You can add more master nodes after the instance is created. For more information, see Change Configurations. Note This parameter is displayed only when Instance resource type is set to Storage Reserved Mode. |
|   | Compute node specifications | This defines the unit of compute resources. Different specifications offer different storage capacity and compute performance. |
|   | Number of compute nodes | Select the number of compute nodes. Adding nodes scales performance linearly. Value range: 2 to 640. |
|   | Compute node capacity | The compute node capacity cannot be changed. The specific capacity depends on the node specifications. The ratio of vCPU cores to memory to storage capacity is 1:8:80. For example, if a compute node has 2 vCPUs and 16 GiB of memory, its storage capacity is 160 GB. Note This parameter is displayed only when Instance resource type is set to Storage Reserved Mode. |

|   | Storage medium | The value is fixed at local SSD. Note This parameter is displayed only when Instance resource type is set to Storage Reserved Mode. |
|---|---|---|
|   | Network type | AnalyticDB for PostgreSQL instances support the following network types: Classic Network: Cloud services in a Classic Network are not isolated at the network layer. You must rely on the security groups or whitelists of individual cloud services to block unauthorized access. VPC: A Virtual Private Cloud (VPC) allows you to build an isolated network environment on Alibaba Cloud. You can customize the route tables, IP address ranges, and gateways in the VPC. VPC is recommended for enhanced security. You can create a VPC in advance, or change the network type to a VPC after you create the instance. |
|   | IP type | IPv4: Assigns only an IPv4 address. This suits IPv4-only network environments. IPv4/IPv6 dual stack: Assigns both IPv4 and IPv6 addresses. This suits hybrid network scenarios where clients use both IPv4 and IPv6. After you enable this option, configure an IPv6 whitelist to control access permissions for IPv6 addresses. Note To configure this parameter, you must enable the IPv6 toggle switch. For more information, see the "Enable the IPv6 toggle switch" section in the Operations Guide. If you see messages such as "Unauthorized," see Authorize SLB for a tenant organization. |
|   | VPC | The VPC where the AnalyticDB for PostgreSQL instance resides. Note This parameter is displayed only when Network type is set to VPC. |

| Network |   |   |
|---|---|---|
|   | VSwitch | The VSwitch where the AnalyticDB for PostgreSQL instance resides. Note This parameter is displayed only when Network type is set to VPC. |
|   | Secondary AZ VSwitch | The VSwitch in the secondary availability zone where the AnalyticDB for PostgreSQL instance resides. Note This parameter is displayed only when Deployment method is set to Multi-AZ Deployment and Network type is set to VPC. |
|   | IPv4 whitelist | Add IPv4 addresses to allow them to access the instance. Note Use RFC private IP address ranges for VPC CIDR blocks, such as 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. |

|   | IPv6 whitelist | Add IPv6 addresses to allow them to access the instance. Note IPv6 whitelist addresses support the following formats: An IPv6 address consists of eight groups of 16- bit hexadecimal values separated by colons (:), for example, 2001:0db8:0000:0000:0000:0000:0000:0001. Shorthand notation is supported, such as 2001:db8::1, where consecutive groups of zeros can be replaced by a double colon (::), but only once. Specify a prefix length, which is an integer from 0 to 128 after a forward slash (/), to define an IP address range. Example: 2001:db8::/32. fc00::/7: A Unique Local Address (ULA) range, similar to the 192.168.0.0/16 range in IPv4. This is for private network use only. (Recommended) ::/0: Represents all IPv6 addresses. This is not recommended for production environments. fe80::/10: A Link-Local Address range, similar to the 169.254.x.x range in IPv4. It is used for auto-configuration and direct communication between devices on the same local network. This is not recommended. |
|---|---|---|

4. Before you create the instance, review your configuration in the **Configuration Overview**
panel on the right to ensure that it meets your requirements. If your quota is insufficient, click **Quota Management** to adjust it. For more information, see the **Quota Management** chapter in the **Unified Cloud Management Platform User**
**Guide**.
5. After you configure the parameters, click **Submit**.

### Configure a whitelist

To ensure the security and stability of a database, you must add IP addresses or CIDR blocks that are allowed to access the database to a whitelist.
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
4. On the **Whitelist Settings** page, you can perform the following operations:

**Add a whitelist group**

a. Click **Add a whitelist Group**. b. In the **New name adding list groups (up to 50 groups supported)** panel, configure the parameters.

| Parameter | Description |
|---|---|

| Group name | The group name must be 2 to 32 characters in length. It can contain lowercase letters, digits, and underscores ( ) and must start _ with a lowercase letter and end with a lowercase letter or a digit. |
|---|---|
| Type | You can select IPv4 or IPv6. |
| Whitelist within a group | Take note of the following requirements when you add IP addresses to the whitelist: Separate multiple IP addresses with commas (,). A maximum of 1,000 unique IP addresses can be added. You can specify IP addresses in the following formats: IPv4: 10.23.12.24 (specific IPv4 address) or 10.23.12.24/24 (CIDR block with a prefix length ranging from 1 to 32). IPv6: 2001:db8::1 (specific IPv6 address) or 2001:db8::/32 (CIDR block with a prefix length ranging from 1 to 128). Note If you enter a CIDR block whose prefix length is 0, such as 0.0.0.0/0 or ::/0, all IP addresses are allowed to access the instance. This poses a high security risk. Proceed with caution. Examples Allow a single IPv6 address: 2001:db8:85a3::8a2e:370:7334 Allow an IPv6 CIDR block: 240e:390:a100::/44 Allow all IP addresses (high risk): ::/0 or 0.0.0.0/0 |
| Import file (.txt) | You can import IP addresses in batches. |

| Load the private IP addresses of ECS instances | a. Click Import ECS Internal IP Address. b. Select IP addresses based on your business requirements. Note To find the Elastic Compute Service (ECS) instance to which a specific IP address is assigned, you can move the pointer over the IP address. Then, the system displays the ID and name of the ECS instance to which the IP address is assigned. |
|---|---|

c. Click **OK**.

**Modify IP addresses in a whitelist**

a. Click **Edit** in the Operation column. b. In the Edit a whitelist Group panel, add or remove IP addresses or CIDR blocks in the
**Whitelist within a group** section.

**Note**

You cannot modify the **Group name**. c. Click **OK**.

**Delete a whitelist group**

**Note**

The default whitelist group cannot be deleted. a. Find the whitelist group that you want to delete and click **Delete** in the Operation column. b. In the **Delete a whitelist Group** message, click **OK**.

**Note**

We recommend that you maintain your whitelists on a regular basis to ensure the security of AnalyticDB for PostgreSQL.

### Create a database account

This topic describes how to create a database account for an AnalyticDB for PostgreSQL instance.

**Background information**

AnalyticDB for PostgreSQL provides the following types of database accounts: Privileged account: an account that has all permissions on all databases. The first account created for an instance in the console is a privileged account. Standard accounts: accounts that have all permissions only on their authorized databases.

**Note**

Permissions include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER.

**Precautions**

Before you use databases in an AnalyticDB for PostgreSQL instance, you must create a privileged account. Standard accounts cannot be created by using the console. For information about how to create standard accounts, see the "Execute SQL statements to create accounts" section of this topic. After you create a privileged account for an instance, you cannot delete the privileged account.
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Account Management**.
4. Click **Create Account**.
5. In the **Create Account** panel, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Account | The name of the privileged account. The name can contain lowercase letters, digits, and underscores ( ). _ The name must start with a lowercase letter and end with a lowercase letter or a digit. The name cannot start with gp. The name must be 2 to 16 characters in length. |
| New Password | The password of the privileged account. The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - = _ The password must be 8 to 32 characters in length. |
| Confirm Password | Enter the password of the account again. |

6. Click **OK**.

**Important**

After the account is created, you can click **Reset Password** in the
**Actions** column to modify the account password. To ensure data security, we
recommend that you change your password on a regular basis and do not use passwords that you have used before.

**Execute SQL statements to create accounts**

Before you execute SQL statements to create accounts, you must connect to a database. For more information, see Connect to a database. Create a privileged account.

```
CREATE ROLE <Account name> WITH LOGIN ENCRYPTED PASSWORD <Password> RDS_SUPERUSER;
```

Example:

```
CREATE role admin0 WITH LOGIN ENCRYPTED PASSWORD '111111' rds_superuser;
```

Create a standard account.

```
CREATE ROLE <Account name> WITH LOGIN ENCRYPTED PASSWORD <'Password'>;
```

Example:

```
CREATE role test1 WITH LOGIN ENCRYPTED PASSWORD '111111';
```

### Obtain client tools

The interface protocol of AnalyticDB for PostgreSQL is compatible with Greenplum Community Edition and PostgreSQL 8.2. You can use the Greenplum or PostgreSQL client to connect to AnalyticDB for PostgreSQL.

**Note**

Apsara Stack is an isolated environment. You must deploy software installation packages to the internal environment.

**Graphical client tools**

AnalyticDB for PostgreSQL users can directly use client tools that support Greenplum, such as SQL Workbench, Navicat Premium, and Navicat for PostgreSQL.

**Command-line client psql (for RHEL 6, RHEL 7, CentOS 6, and**

**CentOS 7)**

For Red Hat Enterprise Linux (RHEL) 6, RHEL 7, CentOS 6, and CentOS 7, download the tool from the following links and then decompress the package: RHEL 6 or CentOS 6: hybriddb_client_package_el6 RHEL 7 or CentOS 7: hybriddb_client_package_el7

**Command-line client psql (for other Linux systems)**

For other Linux systems, perform the following operations to compile the client tools:
1. Obtain the source code by using one of the following methods:
Obtain the code from the git directory. You must first install the git tool.

```
git clone https://github.com/greenplum-db/gpdb.git cd gpdb git checkout 5d870156
```

Download the code.

```
wget https://github.com/greenplumdb/gpdb/archive/5d87015609abd330c68a5402c1267fc86cbc9e1f.zip unzip 5d87015609abd330c68a5402c1267fc86cbc9e1f.zip cd gpdb-5d87015609abd330c68a5402c1267fc86cbc9e1f
```

2. Use GCC or other compilers to compile the code.

```
./configure make -j32 make install
```

3. Obtain the psql and pg_dump tools from the following paths:
psql: /usr/local/pgsql/bin/psql pg_dump: /usr/local/pgsql/bin/pg_dump

**Command-line client psql (for Windows and other systems)**

For Windows and other systems, go to the Pivotal website to download HybridDB Client.

### Connect to a database

Greenplum Database and AnalyticDB for PostgreSQL are both developed based on PostgreSQL 8.2 and fully compatible with its message protocol. AnalyticDB for PostgreSQL users can use tools that support the PostgreSQL 8.2 message protocol, such as libpq, Java Database Connectivity (JDBC), Open Database Connectivity (ODBC), and psycopg2.

**Background information**

AnalyticDB for PostgreSQL provides psql, a binary program of Red Hat. For more information about the download link, see Obtain client tools. The Greenplum official website provides an easy-to-install installation package that includes JDBC, ODBC, and libpq. For more information, see Greenplum official documentation.

**Note**

Apsara Stack is an isolated environment. To access Apsara Stack, you must prepare the necessary software installation packages in advance. By default, AnalyticDB for PostgreSQL instances can be accessed only by clients that are deployed on Elastic Compute Service (ECS) instances within the same region and zone.

**DMS**

Data Management (DMS) allows you to manage relational databases such as MySQL, SQL Server, PostgreSQL, PPAS, and Petadata, online transaction processing (OLTP) databases such as PolarDB-X, online analytical processing (OLAP) databases such as AnalyticDB and Data Lake Analytics (DLA), and NoSQL databases such as MongoDB and Redis. DMS offers an integrated solution to manage data, schemas, and servers. You can also use DMS to authorize users, audit security, view BI charts and data trends, track data, and optimize performance. This section describes how to use DMS to connect to an AnalyticDB PostgreSQL instance.
1. Log on to the Log in to the AnalyticDB for PostgreSQL console.
2. **Optional:**Create an AnalyticDB PostgreSQL instance. For more information, see Create an
instance. If an AnalyticDB PostgreSQL instance has already been created, skip this step.
3. Find the instance that you want to manage and click its instance ID.
4. **Optional:**Create a database account. For more information, see Create a database
account. If an initial account has already been created, you can use this account to connect to the instance.
5. In the upper-right corner of the Basic Information page, click **Log On to Database**.
6. In the **Log On to Database Instance** dialog box, specify the **Database Account** and
**Database password** parameters, and then click **Login**.

**psql**

psql is a common tool used together with Greenplum, and provides a variety of command functions. Its binary files are located in the bin directory of Greenplum. To use psql, perform the following steps:
1. Use one of the following methods to connect to an instance:
Connection string

```
psql "host=yourgpdbaddress.gpdb.rds.aliyuncs.com port=3432 dbname=postgres user=gpd baccount password=gpdbpassword"
```

Specified parameters

```
psql -h yourgpdbaddress.gp.aliyun-inc.com -p 3432 -d postgres -U gpdbaccount
```

Parameters: -h: the host address. -p: the port number used to connect to the database. -d: the name of the database. The default value is postgres. -U: the account used to connect to the database. You can run the `psql --help` command to view more options. You can also run \? to view the commands supported in psql.
2. Enter the password to go to the psql shell interface.

```
postgres=>
```

References For more information about the Greenplum psql usage, see psql. AnalyticDB for PostgreSQL also supports psql for PostgreSQL. Take note of the differences of psql commands between Greenplum and PostgreSQL. For more information, see PostgreSQL 8.3.23 Documentation - psql.

**JDBC**

Download the official JDBC of PostgreSQL. Then, add it to the environment variables. Sample code:

```java
import java.sql.Connection; import java.sql.DriverManager; import java.sql.ResultSet; import java.sql.SQLException; import java.sql.Statement; public class gp_conn {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver");
            Connection db =
DriverManager.getConnection("jdbc:postgresql://mygpdbpub.gpdb.rds.aliyuncs.com:3432/postg s",
                    "mygpdb", "mygpdb");
            Statement st = db.createStatement();
            ResultSet rs = st.executeQuery(
                    "select * from gp_segment_configuration;");
            while (rs.next()) {
                System.out.print(rs.getString(1));
                System.out.print(" | ");
                System.out.print(rs.getString(2));
                System.out.print(" | ");
                System.out.print(rs.getString(3));
                System.out.print(" | ");
                System.out.print(rs.getString(4));
                System.out.print(" | ");
                System.out.print(rs.getString(5));
                System.out.print(" | ");
                System.out.print(rs.getString(6));
                System.out.print(" | ");
                System.out.print(rs.getString(7));
                System.out.print(" | ");
                System.out.print(rs.getString(8));
                System.out.print(" | ");
                System.out.print(rs.getString(9));
                System.out.print(" | ");
                System.out.print(rs.getString(10));
                System.out.print(" | ");
                System.out.println(rs.getString(11));
```

`}`

```
            rs.close();
            st.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
```

`}` `}` `}`

**Python**

Python uses psycopg2 to connect to Greenplum and PostgreSQL. Perform the following operations:
1. Install psycopg2. Use one of the following methods to install psycopg2 in CentOS:
Method 1: Run the following command:

```bash
yum -y install python-psycopg2
```

Method 2: Run the following command:

```
pip install psycopg2
```

Method 3: Run the following source code:

```python
yum install -y postgresql-devel* wget http://initd.org/psycopg/tarballs/PSYCOPG-2-6/psycopg2-2.6.tar.gz tar xf psycopg2-2.6.tar.gz cd psycopg2-2.6 python setup.py build sudo python setup.py install
```

2. Run the following command to set PYTHONPATH and reference it:

```java
import psycopg2
 sql = 'select * from gp_segment_configuration;'
 conn = psycopg2.connect(database='gpdb', user='mygpdb', password='mygpdb', host='myg
pdbpub.gpdb.rds.aliyuncs.com', port=3432)
 conn.autocommit = True
 cursor = conn.cursor()
 cursor.execute(sql)
 rows = cursor.fetchall()
 for row in rows:
     print row
 conn.commit()
 conn.close()
```

An output similar to the following one is displayed:

```
(1, -1, 'p', 'p', 's', 'u', 3022, '192.**.**.158', '192.**.**.158', None, None)(6, -1 , 'm', 'm', 's', 'u', 3019, '192.**.**.47', '192.**.**.47', None, None)(2, 0, 'p', 'p ', 's', 'u', 3025, '192.**.**.148', '192.**.**.148', 3525, None)(4, 0, 'm', 'm', 's', 'u', 3024, '192.**.**.158', '192.**.**.158', 3524, None)(3, 1, 'p', 'p', 's', 'u', 30 23, '192.**.**.158', '192.**.**.158', 3523, None)(5, 1, 'm', 'm', 's', 'u', 3026, '19 2.**.**.148', '192.**.**.148', 3526, None)
```

**libpq**

libpq is the C language interface to AnalyticDB for PostgreSQL. You can use the libpq library to access and manage PostgreSQL databases in a C program. You can find its static and dynamic libraries in the lib directory. For more information about example programs, see Example Programs. For more information about libpq, see PostgreSQL 9.4.17 Documentation - Chapter 31. libpq - C Library.

**ODBC**

PostgreSQL ODBC is an open source version based on the GNU Lesser General Public License (LGPL) protocol. You can download it from the PostgreSQL website.
1. Install the driver.

```bash
yum install -y unixODBC.x86_64 yum install -y postgresql-odbc.x86_64
```

2. View the driver configurations.

```
cat /etc/odbcinst.ini
```

Sample code:

```bash
# Example driver definitions
# Driver from the postgresql-odbc package
# Setup from the unixODBC package
[PostgreSQL] Description = ODBC for PostgreSQL Driver = /usr/lib/psqlodbcw.so Setup = /usr/lib/libodbcpsqlS.so Driver64 = /usr/lib64/psqlodbcw.so Setup64 = /usr/lib64/libodbcpsqlS.so FileUsage = 1
# Driver from the mysql-connector-odbc package
# Setup from the unixODBC package
[MySQL] Description = ODBC for MySQL Driver = /usr/lib/libmyodbc5.so Setup = /usr/lib/libodbcmyS.so Driver64 = /usr/lib64/libmyodbc5.so Setup64 = /usr/lib64/libodbcmyS.so FileUsage = 1
```

3. Configure the data source name (DSN). Replace `****` in the following code with the
corresponding connection information:

```
[mygpdb] Description = Test to gp Driver = PostgreSQL Database = **** Servername = ****.gpdb.rds.aliyuncs.com UserName = **** Password = **** Port = **** ReadOnly = 0
```

4. Test the connectivity.

```
echo "select count(*) from pg_class" | isql mygpdb
```

The following information is returned if the connectivity test passes:

```
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
```

Test whether the database runs normally.

```
SELECT count(*) FROM pg_class;
```

The following information is returned if the database runs normally:

```
+---------------------+
| count               |
+---------------------+
| 388                 |
+---------------------+ SQLRowCount returns 1 1 rows fetched
```

5. After the ODBC driver is connected to the database, connect your application to the driver.
For more information, see PostgreSQL ODBC driver and psqlODBC HOWTO - C#.

**References**

Pivotal Greenplum official documentation PostgreSQL psqlODBC Compiling psqlODBC on Unix Download ODBC connectors Download JDBC connectors The PostgreSQL JDBC Interface

## Instances

### Reset the password of an

**account**

If you forget the password of your database account in the AnalyticDB for PostgreSQL console, you can reset the password.

**Note**

To ensure data security, we recommend that you change your password on a regular basis.
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Account Management**.
4. Find an account and click **Reset Password** in the **Actions** column.
5. In the **Modify Account** panel, enter a new password in **New Password** and **Confirm**
**Password**.
The password must meet the following requirements: The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) _ + - = The password is 8 to 32 characters in length.
6. Click **OK**.

### Manage the endpoints of an

**instance**

This topic describes how to view the internal endpoint and port number and how to apply to and release a public endpoint for an AnalyticDB for PostgreSQL instance.

**View the internal endpoint and port number**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Database Connection**.
4. In the **Connection Information** section, view the internal endpoint and port number of the
instance.

**Apply for a public endpoint**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Apply for Public Endpoint** to the right of **Public Endpoint**.

**Release a public endpoint**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Release Public Endpoint** to the right of **Public Endpoint**.
5. In the **Release Public Endpoint** message, click **OK**.

**Enable or disable IPv6**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Database Connection**.
4. In the connection information section, turn on or off the switch in the **IPv6 Enabled**
column.

**Important**

After you disable IPv6, the services that access the database by using an IPv6 address are disconnected from the database and interrupted. Before you proceed, make sure that no service is connected to the database by using an IPv6 address.
5. Click **OK**.

### Change the specifications of

**an instance**

This topic describes how to change specifications for an instance in storage included mode or reserved storage mode.

**Storage included mode**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click **Change Specifications** in the
**Actions** column.
3. Select new values for **Compute Group Specifications** and **Compute Groups**.
4. Click **Submit**.

**Warning**

When the specifications of an instance are being changed, no data can be read from or written to the instance. Perform the specification change operation during an appropriate period of time.

**Reserved storage mode**

Change the specifications of the coordinator node:
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click **Change Master Node**
**Specifications** in the **Actions** column.
3. Select a new value for **Master Nodes**.
4. Click **Submit**.

**Warning**

When the specifications of coordinator nodes are being changed, DDL operations may be blocked. Perform the specification change operation during an appropriate period of time. Change the specifications of compute nodes:
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click **Change Compute Node**
**Specifications** in the **Actions** column.
3. Select new values for **Compute Group Specifications** and **Compute Nodes**.
4. Click **Submit**.

**Warning**

When the specifications of compute nodes are being changed, no data can be read from or written to the instance. Perform the specification change operation during an appropriate period of time.

### Restart an instance

When the number of connections of an instance reaches the upper limit or the instance has performance issues, you can restart the instance.

**Precautions**

The restart process takes about 3 to 30 minutes. During the restart period, the instance cannot provide external services. We recommend that you take precautionary measures before you restart the instance. After the instance is restarted and enters the running state, you can access the instance.
1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the upper-right corner of the page, click **Restart Instance**.
4. In the **Restart Instance** message, click **OK**.

**Warning**

The database service may be interrupted when you restart an instance. Proceed with caution.

### Release an instance

This topic describes how to manually release an AnalyticDB for PostgreSQL instance.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the upper-right corner of the page, click **Instance Management** > **Release Instance**.
4. On the **Release Instance** page, click **Release**.

**Warning**

After an instance is released, all of its data is deleted. Back up your data before you release an instance.

### Configure SQL audit

AnalyticDB for PostgreSQL allows you to use the SQL audit feature to view SQL details and audit SQL queries on a regular basis. The SQL audit feature does not affect instance performance.

**Storage included mode**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane of the Basic Information page, click **Security Controls**.
4. Click the **SQL Audit** tab.
5. **Optional:**Click **Enable SQL Audit**.
If you have enabled SQL audit, skip this step.
6. On the **SQL Audit** tab, query SQL information based on conditions such as the time range,
database, user, and keyword.

**Note**

You can click **Disable SQL Audit** to disable the SQL audit feature.

**Reserved storage mode**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane of the Basic Information page, click **SQL Audit**.
4. On the **SQL Audit** page, query SQL information based on conditions such as the database,
execution duration, time range, database user, source IP address, execution status, operation category, operation type, and statement.

**Note**

You can click the icon to export SQL information from the current page.

### SSL encryption

To enhance data transmission security, you can enable SSL encryption for your instances. SSL encryption can encrypt network connections at the transport layer. This improves data security and ensures data integrity.

**Precautions**

SSL encryption is supported only for instances in **reserved storage mode**.

**Enable SSL encryption**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
4. Click the **SSL** tab.
5. On the **SSL** tab, turn on **SSL Encryption**.
6. In the **Enable SSL Encryption** message, click **OK**.

**Note**

If you modify the status of SSL encryption, your instance restarts. We recommend that you perform this operation during off-peak hours.

**Update the validity of an SSL certificate**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
4. Click the **SSL** tab.
5. On the **SSL** tab, click **Update Validity** to the right of **SSL Encryption**.
6. In the **Update SSL Certificate Validity** message, click **OK**.

**Note**

If you modify the status of SSL encryption, your instance restarts. We recommend that you perform this operation during off-peak hours.

**Disable SSL encryption**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Data Security > Whitelist Settings**.
4. Click the **SSL** tab.
5. On the **SSL** tab, turn off **SSL Encryption**.
6. In the **Disable SSL Encryption** message, click **OK**.

**Note**

If you modify the status of SSL encryption, your instance restarts. We recommend that you perform this operation during off-peak hours.

### Update the minor engine

**version**

To better meet your requirements, the minor engine version of AnalyticDB for PostgreSQL is updated on a regular basis. When you create an instance, the latest database engine version is used by default. After a new version is released, you can update your instance to the new version and use its extended features. This topic describes how to update the minor engine version of an instance.

**Precautions**

When you update the minor engine version of an instance, the instance restarts and is unavailable during the restart. We recommend that you update the minor engine version during off-peak hours.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the upper-right corner of the **Basic Information** page, click **Upgrade Minor Version**.
4. In the **Upgrade Minor Version** message, click **OK**.

**Note**

Minor version updates take 3 to 15 minutes to complete. When an instance is being updated, it is unavailable. We recommend that you prepare in advance before you update the instance. After the update is complete, the instance enters the Running state and you can access the instance databases.
5. After you complete the preceding steps, check the state of the instance. If the update is
complete, the instance enters the **Running** state. Otherwise, the instance remains in the
**Upgrading version** state.
Before the update, the system checks the minor engine version of your instance. If the latest minor version is used, the system skips the update and restart operations.

### Label

This topic describes how to create and delete tags.

**Limits**

You can bind a maximum of 20 tags to each instance, and the tag keys must be unique. The same tag key is overwritten. You can set up to 50 instances at a time for batch tag binding. The tag information of different regions is independent. If a tag is unbound from an instance, the tag is deleted.

**Create a tag**

1. Log on to the AnalyticDB for PostgreSQL console.
2. In the upper-left corner of the console, select the region where the instance is located.
3. Find the instance to which you want to add tags and click the icon in the **Tags** column.
4. In the **Edit Tag** dialog box, set **Tag Key** and **Tag Value** and click **OK**.

**Note**

If you want to add multiple tags, repeat this step.

**Delete a tag**

You can delete the tags of an instance if the instance is modified or no longer needs the tags.

**Note**

You can unbind a maximum of 20 tags at a time. If a tag is unbound from an instance, the tag is deleted.
1. Log on to the AnalyticDB for PostgreSQL console.
2. Find the instance from which you want to unbind tags and click the icon in the **Tags**
column.
3. In the **Edit Tag** dialog box, delete the tag group and click **OK**.

### Set instance parameters

You can view and modify the values of some parameters in the console, and query parameter modification records.

**Modify parameter values**

1. Log in to the AnalyticDB for PostgreSQL console.
2. On the Instances page, click the ID of the target instance. The **Basic Information** page
appears.
3. In the left-side navigation pane, click **Parameters**.
4. In this case, you can perform the following operations:
Modify a single parameter i. In the **Modifiable Parameters** section, find the parameter that you want to modify and click in the **Parameter Value** column. ii. Enter a value based on the value range that appears. iii. Click **OK**. iv. In the upper-right corner of the page, click **Submit**.

**Note**

If you need to restart the instance for the modified parameters to take effect, the system prompts you whether to restart the instance. We recommend that you perform this operation during off-peak hours and make sure that your application is configured to reconnect to the instance. If you want to cancel the modification, click **Cancel**.

**View parameter modification records**

1. Log in to the AnalyticDB for PostgreSQL console.
2. On the Instances page, click the ID of the target instance. The **Basic Information** page
appears.
3. In the left-side navigation pane, click **Parameters**.
4. Click the **Change History** tab.
5. Select a time range to query the modification records, then click **Query**.

### Import data

#### Import data from or export data to

**OSS in parallel**

AnalyticDB for PostgreSQL allows you to import data from or export data to Object Storage Service (OSS) tables in parallel by using the OSS external table feature (also called gpossext). AnalyticDB for PostgreSQL also supports GZIP compression for OSS external tables to reduce the file size and storage costs. gpossext can read from and write to TEXT and CSV files, even when they are compressed in GZIP packages. Create an OSS external table plug-in (oss_ext) To use an OSS external table, you must first create an OSS external table plug-in in AnalyticDB for PostgreSQL. You must create a plug-in for each database that you need to access. To create the plug-in, execute the CREATE EXTENSION IF NOT EXISTS oss_ext; statement. To delete the plug-in, execute the DROP EXTENSION IF EXISTS oss_ext; statement. Import data in parallel i. Distribute data evenly into multiple files in OSS. We recommend that you set the number of OSS files to an integer that is the multiple of the number of compute nodes in AnalyticDB for PostgreSQL. ii. Create a READABLE external table in AnalyticDB for PostgreSQL. iii. Execute the following statement to import data in parallel:

```
INSERT INTO <Destination table> SELECT * FROM <External table>
```

**Note**

The data import performance depends on the OSS performance and resources of AnalyticDB for PostgreSQL instances, such as CPU, I/O, memory, and network resources. To ensure the best import performance, we recommend that you use column store and compression when you create a table. For example, you can

|   | WITH (APPENDONLY=true, ORIENTATION=column, |
|---|---|
| COMPRESSTYPE=zlib, COMPRESSLEVEL=5, BLOCKSIZE=1048576) |   |

see CREATE TABLE. To ensure the best import performance, we recommend that you configure OSS and AnalyticDB for PostgreSQL within the same region. Export data in parallel i. Create a WRITABLE external table in AnalyticDB for PostgreSQL. ii. Execute the following statement to export data to OSS in parallel:

```
INSERT INTO <External table> SELECT * FROM <Source table>
```

Create OSS external tables

**Note**

The syntax to create and use external tables is the same as that of Greenplum Database, except for the syntax of location-related parameters.

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
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[t
rue|false] ossprotocol:
   oss://oss_endpoint dir=[folder/[folder/]...]/file_name
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[t
rue|false] ossprotocol:
   oss://oss_endpoint filepath=[folder/[folder/]...]/file_name
    id=userossid key=userosskey bucket=ossbucket compressiontype=[none|gzip] async=[t
rue|false]
```

**Parameters**

Table 1. Common parameters

| Parameter | Description |
|---|---|
| Protocol and endpoint | This parameter is in the protocol name://oss endpoint _ format. The protocol name is oss. oss endpoint is the domain _ name that is used to access OSS in a region. Note You can access the database from a Virtual Private Cloud (VPC) host by using an internal endpoint that contains "internal" in the name to avoid generating public traffic. |
| id | The AccessKey ID of the OSS account. |
| key | The AccessKey secret of the OSS account. |
| bucket | The bucket where the data file is located. You must use OSS to create the bucket before you import data. |
| prefix | The prefix of the path name corresponding to the data file. Prefixes are directly matched and cannot be controlled by regular expressions. The prefix, filepath, and dir parameters are mutually exclusive. Only one of the parameters can be specified at a time. If you create a READABLE external table for data import, all OSS files that contain the specified prefix are imported. If you set prefix to test/filename, the following files are imported: test/filename test/filenamexxx test/filename/aa test/filenameyyy/aa test/filenameyyy/bb/aa If you set prefix to test/filename/, only the following file out of the preceding files is imported: test/filename/aa If you create a WRITABLE external table for data export, each exported file has a unique name based on this parameter. Note One or more files can be exported for each compute node. The names of exported files are in the prefix tablename uuid.x format. uuid indicates a _ _ timestamp in microseconds as an int64 value. x indicates the node ID. You can use an external table for multiple export operations. Each export operation is assigned a uuid value. The files exported during each operation share a uuid value. |

| dir | The virtual folder path in OSS. The prefix, filepath, and dir parameters are mutually exclusive. Only one of the parameters can be specified at a time. A folder path must end with a forward slash (/). Example: test/mydir/ . If you use this parameter when you create an external table for data import, all files in the specified virtual directory (except for its subdirectories and contained files) are imported. The dir parameter is different from the filepath parameter and does not require you to specify the names of files in a directory. If you use this parameter when you create an external table for data export, all data is exported as multiple files within the specified directory. The names of exported files are in the filename.x format, where x indicates a number. The values of x may not be consecutive. |
|---|---|
| filepath | The file name that contains a path in OSS. The prefix, filepath, and dir parameters are mutually exclusive. Only one of the parameters can be specified at a time. You can specify only the filepath parameter when you create a READABLE external table for data import. The file name includes the file path, but not the bucket name. The file name that is specified for data import must be in the filename or filename.x format. The values of x must be consecutive numbers that start from 1. For example, if filepath is set to filename and OSS contains the following files, the imported files include filename, filename.1, and filename.2, but not filename.4 because filename.3 does not exist. filename filename.1 filename.2 filename.4 |

Table 2. Import mode parameters

| Parameter | Description |
|---|---|
| async | Specifies whether to enable asynchronous data import. By default, asynchronous data import is enabled. You can set async to false or f to disable asynchronous data import. You can enable the worker thread to load data from OSS to accelerate the import performance. By default, asynchronous data import is used. Asynchronous data import consumes more hardware resources than normal data import. |

| compressiontype | The compression format of the imported files. Default value: none. Valid values: none: The import files are not compressed. gzip: The imported files are compressed in the GZIP format. Only the GZIP format is supported. |
|---|---|
| compressionlevel | The compression level of the files that are written to OSS. Valid values: 1 to 9. Default value: 6. |

Table 3. Export mode parameters

| Parameter | Description |
|---|---|
| oss flush block size _ _ _ | The size of each data block that is written to OSS. Valid values: 1 to 128. Default value: 32. Unit: MB. |
| oss file max size _ _ _ | The maximum size for each file that is written to OSS. If the limit is exceeded, subsequent data is written to another file. Valid values: 8 to 4000. Default value: 1024. Unit: MB. |
| num parallel worker _ _ | The number of parallel compression threads for data that is written to OSS. Valid values: 1 to 8. Default value: 3. |

For data export, take note of the following items: WRITABLE is the keyword of the external table for data export. You must specify this keyword when you create an external table. Only the prefix and dir parameters are supported for data export. The filepath parameter is not supported. You can use the DISTRIBUTED BY clause to write data from compute nodes to OSS based on the specified distribution keys.

**Other common parameters**

The following table describes the fault-tolerance parameters that can be used for data import and export. Table 4. Fault-tolerance parameters

| Parameter | Description |
|---|---|
| oss connect timeout _ _ | The connection timeout period. Default value: 10. Unit: seconds. |
| oss dns cache timeout _ _ _ | The Alibaba Cloud DNS timeout period. Default value: 60. Unit: seconds. |
| oss speed limit _ _ | The minimum rate tolerated. Default value: 1024 bit/s (1 Kbit/s). |
| oss speed time _ _ | The maximum amount of time tolerated. Default value: 15. Unit: seconds. |

When the default values are used for the preceding parameters, a timeout occurs if the transmission rate is lower than 1 Kbit/s for 15 consecutive seconds. For more information, see Error handling in the C-SDK part of **Object Storage Service Developer Guide**. The other parameters are compatible with the external table syntax of Greenplum Database. For more information about the syntax, see CREATE EXTERNAL TABLE. The following parameters are included: FORMAT: the supported file format, such as TEXT and CSV. ENCODING: the data encoding format of a file, such as UTF-8. LOG ERRORS refers to improperly imported data that can be ignored and is instead written to error_table. You can also use the count parameter to specify the error reporting threshold.

**Examples**

1. Create an OSS external table named ossexample to import data.

```
CREATE READABLE EXTERNAL TABLE ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        prefix=osstest/example id=XXX
        key=XXX bucket=testbucket compressiontype=gzip')
        FORMAT 'csv' (QUOTE '''' DELIMITER E'\t')
        ENCODING 'utf8'
        LOG ERRORS INTO my_error_rows SEGMENT REJECT LIMIT 5;
CREATE READABLE EXTERNAL TABLE ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        dir=osstest/ id=XXX
        key=XXX bucket=testbucket')
        FORMAT 'csv'
        LOG ERRORS SEGMENT REJECT LIMIT 5;
CREATE READABLE EXTERNAL TABLE ossexample
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        filepath=osstest/example.csv id=XXX
        key=XXX bucket=testbucket')
        FORMAT 'csv'
        LOG ERRORS SEGMENT REJECT LIMIT 5;
```

2. Create an OSS external table to which data is exported.

```
CREATE WRITABLE EXTERNAL TABLE ossexample_exp
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        prefix=osstest/exp/outfromhdb id=XXX
        key=XXX bucket=testbucket') FORMAT 'csv'
        DISTRIBUTED BY (date);
CREATE WRITABLE EXTERNAL TABLE ossexample_exp
        (date text, time text, open float, high float,
        low float, volume int)
        location('oss://oss-cn-hangzhou.aliyuncs.com
        dir=osstest/exp/ id=XXX
        key=XXX bucket=testbucket') FORMAT 'csv'
        DISTRIBUTED BY (date);
```

3. Create a heap table named example to which you want to import data.

```
CREATE TABLE example
        (date text, time text, open float,
         high float, low float, volume int)
         DISTRIBUTED BY (date);
```

4. Import data to the example heap table from the ossexample table in parallel.

```
INSERT INTO example SELECT * FROM ossexample;
```

5. Export data from the example heap table to OSS in parallel.

```
INSERT INTO ossexample_exp SELECT * FROM example;
```

6. Execute an execution plan. The following execution plan shows that all compute nodes are
involved in the task.

```
EXPLAIN INSERT INTO example SELECT * FROM ossexample;
```

All compute nodes read data from OSS in parallel. AnalyticDB for PostgreSQL performs a redistribution motion operation to compute the data by using a hash algorithm, and then distributes the data to its compute nodes after computing. After a compute node receives data, it performs an INSERT operation to add the data to AnalyticDB for PostgreSQL. The following information is returned:

```
                                            QUERY PLAN
------------------------------------------------------------------------------------- --------
 Insert (slice0; segments: 4)  (rows=250000 width=92)
   ->  Redistribute Motion 4:4  (slice1; segments: 4)  (cost=0.00..11000.00 rows=25
0000 width=92)
         Hash Key: ossexample.date
         ->  External Scan on ossexample  (cost=0.00..11000.00 rows=250000
width=92) (4 rows) EXPLAIN INSERT INTO ossexample_exp SELECT * FROM example;
```

The following execution plan shows that each compute node directly exports data to OSS without redistributing the data. The following information is returned:

```
                          QUERY PLAN
---------------------------------------------------------------
 Insert (slice0; segments: 3)  (rows=1 width=92)
   ->  Seq Scan on example  (cost=0.00..0.00 rows=1 width=92)
(2 rows)
```

**TEXT and CSV format description**

The following parameters specify the formats of files read from and written to OSS. You can specify the parameters in the external DDL parameters. \n: the line feed for TEXT and CSV files. DELIMITER: the delimiter of columns. If the DELIMITER parameter is specified, the QUOTE parameter must also be specified. Recommended column delimiters include commas (,), vertical bars (|), and special characters such as \t. QUOTE: encloses user data that contains special characters by column. Strings that contain special characters must be enclosed by QUOTE to differentiate user data from control characters. To optimize the efficiency, it is unnecessary to enclose data such as integers in QUOTE characters. QUOTE characters cannot be the same as those specified by DELIMITER. The default value of QUOTE is a pair of double quotation marks (""). User data that contains QUOTE characters must also contain ESCAPE characters to differentiate user data from machine code. ESCAPE: the escape character. Place an escape character before a special character that needs to be escaped to indicate that it is not a special character. If ESCAPE is not specified, the default value is the same as QUOTE. You can also use other characters such as backslashes (\) as ESCAPE characters, which is used by MySQL.

**Default control characters for TEXT and CSV files**

Table 5. The following table describes the default control characters for TEXT and CSV files.

| Control character | TEXT | CSV |
|---|---|---|
| DELIMITER | Tab (\t) | Comma (,) |
| QUOTE | double quotation mark (") | double quotation mark (") |
| ESCAPE | N/A | Same as QUOTE |
| NULL | Backslash plus N (\N) | Empty string without quotation marks |

**Note**

All control characters must be single-byte characters.

**SDK troubleshooting**

The following Error log information table lists the error logs generated when an error occurs during the import or export process. Table 6. Error log information

| Keyword | Description |
|---|---|
| code | The HTTP status code of the error request. |
| error code _ | The error code returned by OSS. |
| error msg _ | The error message returned by OSS. |
| req id _ | The UUID used to identify the request. If you require assistance in solving a problem, you can submit a ticket that contains the req id value of the failed request. _ |

You can handle timeout-related errors by using parameters related to oss_ext.

**References**

CREATE EXTERNAL TABLE CREATE TABLE

#### Import data from MySQL

You can use the mysql2pgsql tool to migrate tables from MySQL to AnalyticDB for PostgreSQL, Greenplum Database, PostgreSQL, or Postgres Plus Advanced Server (PPAS).

**Background information**

mysql2pgsql connects to both the source MySQL database and the destination AnalyticDB for PostgreSQL database. The tool retrieves the data that you want to export from the source MySQL database, and uses a COPY statement to import the data to the destination database. This tool supports simultaneous data import over multiple threads. Each worker thread imports data from specific database tables. You can download the binary installation package of mysql2pgsql. You can view instructions on source code compilation of mysql2pgsql.

**Procedure**

1. Modify the my.cfg configuration file to configure the connection information of source and
destination databases. i. Modify the connection information of the source MySQL database.

**Note**

You must have the read permissions on all user tables.

```
[src.mysql] host = "192.168.1.1" port = "3306" user = "test" password = "test" db = "test" encodingdir = "share" encoding = "utf8"
```

ii. Modify the connection information of the destination PostgreSQL, PPAS, or AnalyticDB for PostgreSQL database.

**Note**

You must have the write permissions on the destination table.

```
[desc.pgsql] connect_string = "host=192.168.1.2 dbname=test port=3432 user=test password=pgsql"
```

2. Use mysql2pgsql to import data.

```
./mysql2pgsql -l <tables_list_file> -d -n -j <number of threads> -s <schema of target able>
```

Table 1. Parameters

| Parameter | Description |
|---|---|

| -l | Optional. This parameter is used to specify a text file that contains tables to be synchronized. If you do not specify this parameter, all the tables in the database that is specified in the configuration file are synchronized. <tables list file> specifies the name of a file that contains a collection of _ _ tables to be synchronized and conditions for table queries. You can specify the file content in the following format: table1 : select * from table big where column1 < '2016-08-05' _ table2 : table3 table4: select column1, column2 from tableX where column1 != 10 table5: select * from table big where column1 >= '2016-08-05' _ |
|---|---|
| -d | Optional. This parameter indicates the table creation DDL statement that creates the destination table but does not synchronize data. |
| -n | Optional. This parameter must be used together with -d to specify that the table partitioning definition is not included in the DDL statement. |
| -j | Optional. This parameter is used to specify the number of threads that are used for data synchronization. If you do not specify this parameter, five concurrent threads are used. |
| -s | Optional. This parameter is used to specify the schema of the destination table. Only a single schema can be specified at a time by the command. If you do not specify this parameter, the data is imported to the table under the public schema. |

**Typical usage**

**Full database migration**

1. Run the following command to obtain the DDL statements of the corresponding destination
table:

```
 ./mysql2pgsql -d
```

2. Create a table in the destination database based on these DDL statements with the
distribution key information added.
3. Run the following command to synchronize all tables:

```
 ./mysql2pgsql
```

This command migrates the data from all MySQL tables in the database that is specified in the configuration file to the destination database. By default, five concurrent threads are used to read and import data from involved tables.

**Partial table migration**

1. Create a file named tab_list.txt and enter the following content:
`t1`

```
t2 : select * from t2 where c1 > 138888
```

2. Run the following command to synchronize the specified t1 and t2 tables. For the t2 table,
only data that meets the c1 > 138888 condition is migrated.

```
 ./mysql2pgsql -l tab_list.txt
```

#### Import data from PostgreSQL

You can use the pgsql2pgsql tool to migrate tables across AnalyticDB for PostgreSQL, Greenplum Database, PostgreSQL, and Postgres Plus Advanced Server (PPAS).

**Background information**

pgsql2pgsql supports the following features: Full migration across PostgreSQL, PPAS, Greenplum Database, and AnalyticDB for PostgreSQL. Full migration and incremental migration from PostgreSQL or PPAS (version 9.4 or later) to AnalyticDB for PostgreSQL or PPAS. You can perform the following operations in the dbsync project library: Download the binary installation package of pgsql2pgsql. View instructions on source code compilation of pgsql2pgsql.

**Procedure**

1. Modify the my.cfg configuration file to configure the connection information of source and
destination databases. i. Modify the connection information of the source PostgreSQL database.

**Note**

In the connection information of the source PostgreSQL database, we recommend that you set the user to the owner of the source database.

```
[src.pgsql] connect_string = "host=192.168.0.1 dbname=test port=3432 user=test password=pgsql"
```

ii. Modify the connection information of the self-managed PostgreSQL database.

```
[local.pgsql] connect_string = "host=192.168.0.2 dbname=test port=3432 user=test2 password=pgsql"
```

iii. Modify the connection information of the destination PostgreSQL database.

**Note**

You must have the write permissions on the destination table.

```
[desc.pgsql] connect_string = "host=192.168.0.2 dbname=test port=3432 user=test3 password=pgsql"
```

**Note**

If you want to synchronize incremental data, you must have the permissions to create replication slots in the source database. PostgreSQL 9.4 and later support logic flow replication. Therefore, source databases of these versions support incremental data migration. A kernel supports logic flow replication only after you configure the following parameters: wal_level = logical max_wal_senders = 6 max_replication_slots = 6
2. Use pgsql2pgsql to perform full database migration.

```
 ./pgsql2pgsql
```

By default, the migration program migrates the table data of all users from the source PostgreSQL database to the destination PostgreSQL database.
3. View the status information.
You can view the status information in a single migration process by connecting to the selfmanaged database. The status information is stored in the db_sync_status table and includes the start and end time of full data migration, the start time of incremental data migration, and the status of incremental data synchronization.

#### Use the COPY statement to import

**data**

You can use the \copy command to import data from local text files to AnalyticDB for PostgreSQL instances. Local text must be properly formatted and include necessary delimiters such as commas (,), semicolons (;), or special characters.

**Background information**

Large amounts of data cannot be written in parallel because the \copy command writes data in series by using the coordinator node. If you need to import large amounts of data in parallel, you can use the data import method based on Object Storage Service (OSS). The \copy command is a psql instruction. If you use the database statement `COPY` instead of the \copy command, be aware that only stdin is supported. The COPY statement does not support files because the root user does not have the superuser permissions to perform operations on files. AnalyticDB for PostgreSQL also allows you to use Java Database Connectivity (JDBC) to execute the COPY statement. The CopyIn method is encapsulated within JDBC. For more information, see Interface CopyIn. For more information about how to use the COPY statement, see COPY.

**Procedure**

Execute the following COPY statement to import data:

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

## Databases

### Overview

Basically, you can use AnalyticDB for PostgreSQL in the same manner as you use Greenplum Database. They have the same schemas, supported data types, and user permission requirements. Except for specific operations that are exclusive to Greenplum Database such as those on distribution keys and append-optimized (AO) tables, all operations are the same as those of the open source PostgreSQL.

**References**

Pivotal Greenplum official documentation GP 4.3 Best Practice Greenplum数据分布黄金法则

### Create a database

After you connect to an AnalyticDB for PostgreSQL instance, you can execute SQL statements to create databases. As in PostgreSQL, you can execute SQL statements to create databases in AnalyticDB for PostgreSQL. For example, after the **psql** client is used to connect to AnalyticDB for PostgreSQL, execute the following statement:

```
CREATE DATABASE mygpdb;
```

View database information.

```
\c mygpdb
```

The following information is returned:

```
You are now connected to database "mygpdb" as user "mygpdb".
```

### Create a distribution key

AnalyticDB for PostgreSQL is a distributed database service where data is distributed across all the data nodes. You must create distribution keys to distribute data in AnalyticDB for PostgreSQL. Distribution keys are vital to query performance. Distribution keys are used to ensure even data distribution. Appropriate selection of keys can significantly improve query performance.

**Specify a distribution key**

In AnalyticDB for PostgreSQL, the data of a table can be distributed across all compute nodes in hash or random mode. When you create a table, you must specify a distribution key. Imported data is distributed to specific compute nodes based on the hash value calculated by using the distribution key.

```
CREATE TABLE vtbl(id serial, key integer, value text, shape cuboid, location geometry, comment text) DISTRIBUTED BY (key);
```

If you do not specify a distribution key in the DISTRIBUTED BY clause, AnalyticDB for PostgreSQL distributes data by id field by using the round-robin algorithm.

**Rules for selecting a distribution key**

Select evenly distributed columns or multiple columns to prevent data skew. Select fields that are commonly used for connection operations, especially for highly concurrent statements. Select conditional columns that feature high concurrency queries and high filterability. Do not use random distribution.

### Construct data

In some test scenarios, you must construct data to fill the database.
1. Create a function that generates random strings.

```
CREATE OR REPLACE FUNCTION random_string(integer) RETURNS text AS $body$ SELECT array_to_string(array
                      (SELECT
substring('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                                        FROM (ceil(random()*62))::int
                                        FOR 1)
                       FROM generate_series(1, $1)), '');
$body$ LANGUAGE SQL VOLATILE;
```

2. Create a partition key.

```
CREATE TABLE tbl(id serial, KEY integer, locate geometry, COMMENT text) distributed b y (key);
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
         'POINT(' || ceil(random() * 36 + 99) || ' ' || ceil(random() * 24 + 50) || '
)' AS locate
     FROM
         generate_series(0, 99999) AS a)
     AS t;
```

### Query data

This topic describes the query statements and how to view the query plans.

**Sample query statement**

```
SELECT * FROM tbl WHERE key = 751;
```

The following information is returned:

```
  | id  | key | value | shape        | locate                                     | comme
nt |
  +-----+-----+-------+--------------+--------------------------------------------+------
---------+
  | 751 | 751 | red   | 01010000000000000000C05B400000000000004A40 | B9hPhjeNWPqV |
  (1 row)
  Time: 513.101 ms
```

**View a query plan**

```
EXPLAIN SELECT * FROM tbl WHERE key = 751;
```

The following information is returned:

```
  Gather Motion 1:1  (slice1; segments: 1)  (cost=0.00..1519.28 rows=1 width=53)
    ->  Seq Scan on tbl  (cost=0.00..1519.28 rows=1 width=53)
          Filter: key = 751
  Settings:  effective_cache_size=8GB; gp_statistics_use_fkeys=on
  Optimizer status: legacy query optimizer
```

### Manage extensions

You can use extensions to expand database features. AnalyticDB for PostgreSQL enables you to manage extensions.

**Supported extensions**

AnalyticDB for PostgreSQL supports the following extensions: PostGIS: processes geographic data. MADlib: provides a machine learning function library. fuzzystrmatch: implements fuzzy match of strings. orafunc: provides compatibility with some Oracle functions. oss_ext: reads data from Object Storage Service (OSS). HyperLogLog: collects statistics. PL/Java: compiles user-defined functions (UDFs) in PL/Java. pgcrypto: provides cryptographic functions. IntArray: provides integer array-related functions, operators, and indexes.

**Create an extension**

Execute the following statements to create an extension:

```
CREATE EXTENSION <extension name>; CREATE SCHEMA <schema name>; CREATE EXTENSION IF NOT EXISTS <extension name> WITH SCHEMA <schema name>;
```

**Note**

Before you create a MADlib extension, you must create a plpythonu extension.

```
CREATE EXTENSION plpythonu; CREATE EXTENSION madlib;
```

**Delete an extension**

Execute the following statements to delete an extension.

```
DROP EXTENSION <extension name>; DROP EXTENSION IF EXISTS <extension name> CASCADE;
```

**Note**

If an object depends on an extension that you want to delete, you must add the CASCADE keyword to delete the object.

### Manage users and

**permissions**

This topic describes how to manage users and permissions in AnalyticDB for PostgreSQL.

**Manage users**

The system prompts you to specify an initial username and password when you create an instance. This initial user is the root user. After the instance is created, you can use the root user to connect to a database. The system also creates superusers such as aurora and replicator for internal management. You can run the \du+ command to view the information of all the users after you connect to the database by using the client tool of PostgreSQL or Greenplum. Sample output:

```
                                List of roles
  Role name   |            Attributes             | Member of |  Description
--------------+-----------------------------------+-----------+---------------
 root_user    |                               |      | rds_superuser
 ...
```

AnalyticDB for PostgreSQL does not provide superuser permissions but offers a similar role RDS_SUPERUSER. This is consistent with the permission system of ApsaraDB RDS for PostgreSQL. The root user, such as root_user in the preceding sample output, has the permissions of the RDS_SUPERUSER role. This permission attribute can be identified only by viewing the user description. The root user has the following permissions: Create databases and users and perform operations such as LOGIN, excluding the SUPERUSER permissions. View and modify the data tables of other users and perform operations such as SELECT, UPDATE, DELETE, and changing owners. View the connection information of other users, cancel their SQL statements, and kill their connections. Create and delete plug-ins. Create other users with RDS_SUPERUSER permissions. Example:

```
CRATE ROLE root_user2 RDS_SUPERUSER LOGIN PASSWORD 'xyz' ;
```

**Manage permissions**

You can manage permissions at the database, schema, and table levels. For example, if you want to grant read permissions on a table to a user and revoke write permissions, you can execute the following statements:

```
GRANT SELECT ON TABLE t1 TO normal_user1; REVOKE UPDATE ON TABLE t1 FROM normal_user1; REVOKE DELETE ON TABLE t1 FROM normal_user1;
```

### Manage real-time materialized

**views**

AnalyticDB for PostgreSQL provides real-time materialized views. Compared with non-realtime materialized views, real-time materialized views can implement automatic refresh in response to data changes without the need to execute REFRESH statements. A real-time materialized view can be automatically updated with changes made to its base tables. Real-time materialized views of AnalyticDB for PostgreSQL support only statementlevel automatic refresh. When an INSERT, COPY, UPDATE, or DELETE statement is executed on a base table, real-time materialized views created on this base table are updated in real time to ensure strong data consistency.

**Note**

In this mode, the write performance of base tables may be reduced. We recommend that you do not create more than five real-time materialized views on the same base table. For more information about materialized views, see CREATE MATERIALIZED VIEW.

**Statement-level refresh**

When a statement is executed on a base table, real-time materialized views created on this base table are updated in real time to ensure data consistency. Such statements include INSERT, COPY, UPDATE, and DELETE. Real-time materialized views are updated based on the following logic: The database engine first updates base tables, and then updates their materialized views. If base tables fail to be updated, no data changes are made to their materialized views. If materialized views fail to be updated, no data changes are made to their base tables and an error is returned for the executed statement. For an explicit transaction that starts with the BEGIN TRANSACTION statement and ends with the COMMIT statement, after base tables are updated, data changes are also made to their materialized views in this transaction. If AnalyticDB for PostgreSQL uses the default READ COMMITTED isolation level, updates of materialized views are invisible to other transactions before this transaction is committed. If this transaction is rolled back, base tables and their materialized views are also rolled back.

**Limits**

AnalyticDB for PostgreSQL imposes the following limits on the query statements that are used to create real-time materialized views: If a query statement contains JOIN operations, only INNER JOIN can be used to join tables. OUTER JOIN or SELF JOIN is not supported. Query statements can contain most filtering and projection operations. Only the following aggregate operations are supported in a query statement: COUNT, SUM, AVG, MAX, and MIN. The HAVING clause is not supported. Complex statements such as those that contain subqueries and common table expressions (CTEs) are not supported. After you create a real-time materialized view on a base table, DDL statements that you execute on the base table are subject to the following limits: When you execute the TRUNCATE statement on the base table, the real-time materialized view is not synchronously updated. You must manually refresh the real-time materialized view or create another materialized view. You must specify the CASCADE option to execute the DROP TABLE statement on the base table. ALTER TABLE statements on the base table cannot be used to delete or modify fields referenced by the materialized view. Real-time materialized views are subject to the following limits: Real-time materialized views are supported for standard and partitioned heap tables, but not for append-optimized (AO) tables.

**Scenarios**

We recommend that you use real-time materialized views in the following scenarios: The number of rows or columns in the query results is much smaller than that of the base tables. For example, the query statement may contain a WHERE clause that effectively narrows down the results or may contain an aggregate function that consolidates multiple values into a single value. Large amounts of computations are required to obtain the query results of the following operations: Semi-structured data analysis Aggregate operations that take a long time to complete Base tables are not frequently changed. Real-time materialized views can be used in all scenarios where materialized views are suitable. Compared with non-real-time materialized views, real-time materialized views are highly consistent with their base tables. When a base table changes, its real-time materialized views synchronously change with minimal performance cost. However, when you use non-real-time materialized views, you must manually update them each time their base tables change. Therefore, when large amounts of data are changed on a base table or a streaming update is performed, real-time materialized views have great advantages over non-real-time materialized views.

**Disadvantages of real-time materialized views**

Real-time materialized views are similar to indexes maintained in real time. They can significantly optimize query performance but also reduce write performance. When you create a real-time materialized view that contains only a single table, the write performance of the related database is reduced because the data in the materialized view must be synchronously updated. The write latency can be up to three times longer compared with writing data to the base table but not updating the materialized view. We recommend that you do not create more than five real-time materialized views on the same base table. Batch data writes help reduce the maintenance overhead of real-time materialized views. When you execute COPY or INSERT statements, we recommend that you increase the number of batch processed rows within a single statement. This significantly reduces the maintenance overhead of real-time materialized views. When the query statement used to create a real-time materialized view contains a JOIN clause to join two tables, you must optimize the write performance of the real-time materialized view. If you do not have relevant experience or encounter low performance when you test the execution, we recommend that you use a real-time materialized view that contains only a single table. The following suggestions are available in scenarios where two tables are joined: Use the join key of each base table as their respective distribution keys. Create an index for the join key of each base table.

**Create or delete a real-time materialized view**

Execute the following `CREATE INCREMENTAL MATERIALIZED VIEW` statement to create a realtime materialized view named `mv` :

```
CREATE INCREMENTAL MATERIALIZED VIEW mv AS SELECT * FROM base WHERE id > 40;
```

Execute the following `DROP MATERIALIZED VIEW` statement to delete the `mv` materialized view:

```
DROP MATERIALIZED VIEW mv;
```

**Examples**

1. Execute the following statement to create a base table:

```
CREATE TABLE test (a int, b int) DISTRIBUTED BY (a);
```

2. Execute the following statement to create a real-time materialized view:

```
CREATE INCREMENTAL MATERIALIZED VIEW mv AS SELECT * FROM TEST WHERE b > 40 DISTRIBUTE D BY (a);
```

3. Execute the following statement to insert data to the base table:

```
INSERT INTO test VALUES (1, 30), (2, 40), (3, 50), (4, 60);
```

4. Execute the following statement to view data in the base table:

```
SELECT * FROM test;
```

The following information is returned:

```
 a | b
---+----
 1 | 30
 2 | 40
 3 | 50
 4 | 60
(4 rows)
```

5. Execute the following statement to view data in the materialized view:

```
SELECT * FROM mv;
```

The following information is returned, which indicates that the materialized view is updated:

```
 a | b
---+----
 3 | 50
 4 | 60
(2 rows)
```

### Manage JSON data

JSON has become a basic data type in the Internet and IoT fields. For more information about JSON, visit JSON official website. PostgreSQL provides full support for JSON. AnalyticDB for PostgreSQL is optimized by Alibaba Cloud to support the JSON type based on the PostgreSQL syntax.

**Check whether the current version supports JSON**

Execute the following statement to check whether the current version supports JSON:

```
SELECT '""'::json;
```

If the following information is returned, the JSON type is supported and the instance is ready for use. If the operation fails, restart the instance.

```
 json
------
```

`""`

```
(1 row)
```

If the following information is returned, the JSON type is not supported:

```
ERROR: type "json" does not exist LINE 1: SELECT '""'::json;
```

^ The preceding statement converts data from the string type to the JSON type. PostgreSQL supports operations on JSON data based on this conversion.

**JSON conversion in the database**

Database operations include reading and writing. The written data is typically converted from the string type to the JSON type. The contents of a string must meet the JSON standard, such as strings, digits, arrays, and objects. Example:

**String**

```
SELECT '"hijson"'::json;
```

The following information is returned:

```
 json
-------
 "hijson"
(1 row)
```

`::` is used for explicit type conversion in PostgreSQL, Greenplum, and AnalyticDB for PostgreSQL. The database calls the input function of the JSON type during the conversion. Therefore, JSON format check is performed. Example:

```
SELECT '{hijson:1024}'::json;
```

The following error information is returned:

```
ERROR: invalid input syntax for type json LINE 1: SELECT '{hijson:1024}'::json;
```

^

```
DETAIL: Token "hijson" is invalid. CONTEXT: JSON data, line 1: {hijson...
```

In the preceding example, `hijson` must be enclosed in double quotation marks ( `"` ) because JSON requires the KEY value to be a string. A syntax error is returned when `{hijson:1024}` is entered. Apart from explicit type conversion, database records can also be converted to JSON. Typically, JSON is not used for a string or a digit, but an object that contains one or more keyvalue pairs. AnalyticDB for PostgreSQL can support most JSON scenarios after data is converted from the string type to the object type. Example:

```
SELECT row_to_json(row('{"a":"a"}', 'b'));
```

The following information is returned:

```json
           row_to_json
---------------------------------
 {"f1":"{\"a\":\"a\"}","f2":"b"}
(1 row) SELECT row_to_json(row('{"a":"a"}'::json, 'b'));
```

The following information is returned:

```json
        row_to_json
---------------------------
 {"f1":{"a":"a"},"f2":"b"}
(1 row)
```

You can see the differences between the string and JSON. The entire record is converted to the JSON type.

**JSON data types**

Object The object is the most frequently used data type in JSON. Example:

```json
SELECT '{"key":"value"}'::json;
        json
  -----------------
   {"key":"value"}
  (1 row)
```

Integer and floating point number JSON supports only three data types for numeric values: integer, floating-point number, and constant expression. AnalyticDB for PostgreSQL supports the three types.

```
SELECT '1024'::json;
```

The following information is returned:

```
   json
  ------
  (1 row)
SELECT '0.1'::json;
```

The following information is returned:

```
   json
  ------
   0.1
  (1 row)
```

The following information is required in special situations:

```
SELECT '1e100'::json;
```

The following information is returned:

```
   json
  -------
   1e100
  (1 row)
```

```
SELECT '{"f":1e100}'::json;
```

The following information is returned:

```json
      json
  -------------
   {"f":1e100}
  (1 row)
```

Extra-long numbers are also supported. Example:

```
SELECT '9223372036854775808'::json;
```

The following information is returned:

```
          json
  ---------------------
   9223372036854775808
  (1 row)
```

Array

```
SELECT '[[1,2], [3,4,5]]'::json;
```

The following information is returned:

```
         json
  ------------------
   [[1,2], [3,4,5]]
  (1 row)
```

**Operators**

**Operators supported by JSON**

```
SELECT oprname,oprcode FROM pg_operator WHERE oprleft = 3114;
```

The following information is returned:

```
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

**Basic usage**

```
SELECT '{"f":"1e100"}'::json -> 'f';
```

The following information is returned:

```
 ?column?
----------
 "1e100"
(1 row) SELECT '{"f":"1e100"}'::json ->> 'f';
```

The following information is returned:

```
 ?column?
----------
 1e100
(1 row) SELECT '{"f2":{"f3":1},"f4":{"f5":99,"f6":"stringy"}}'::json#>array['f4','f6'];
```

The following information is returned:

```
 ?column?
-----------
 "stringy"
(1 row) SELECT '{"f2":{"f3":1},"f4":{"f5":99,"f6":"stringy"}}'::json#>'{f4,f6}';
```

The following information is returned:

```
 ?column?
-----------
 "stringy"
(1 row) SELECT '{"f2":["f3",1],"f4":{"f5":99,"f6":"stringy"}}'::json#>>'{f2,0}';
```

The following information is returned:

```
 ?column?
----------
```

`f3`

```
(1 row)
```

**JSON functions**

**Supported JSON functions**

```
\df *json*
```

The following information is returned:

```
                                                       List of functions
   Schema   |           Name            | Result data type |                    Argument
data types | Type ------------+---------------------------+------------------+----------------------------- ----------------------------+--------
 pgcatalog | arraytojson             | json             | anyarray
```

```
pg_
```

`g`| `y_` `_j`
|`j`
|
`y` `y`

```
| normal
 pg_catalog | array_to_json             | json             | anyarray, boolean
| normal
 pg_catalog | json_array_element        | json             | from_json json, element_ind
ex integer | normal
 pg_catalog | json_array_element_text   | text             | from_json json, element_ind
ex integer | normal
 pg_catalog | json_array_elements       | SETOF json       | from_json json, OUT value
json | normal
 pg_catalog | json_array_length         | integer          | json
| normal
 pg_catalog | json_each                 | SETOF record     | from_json json, OUT key tex
t, OUT value json | normal
 pg_catalog | json_each_text            | SETOF record     | from_json json, OUT key
text, OUT value text | normal
 pg_catalog | json_extract_path         | json             | from_json json, VARIADIC pa
th_elems text[] | normal
 pg_catalog | json_extract_path_op      | json             | from_json json, path_elems
text[] | normal
 pg_catalog | json_extract_path_text    | text             | from_json json, VARIADIC pa
th_elems text[] | normal
 pg_catalog | json_extract_path_text_op | text             | from_json json, path_elems
text[] | normal
 pg_catalog | json_in                   | json             | cstring
| normal
 pg_catalog | json_object_field         | json             | from_json json, field_name
text | normal
 pg_catalog | json_object_field_text    | text             | from_json json, field_name
text | normal
 pg_catalog | json_object_keys          | SETOF text       | json
| normal
 pg_catalog | json_out                  | cstring          | json
| normal
 pg_catalog | json_populate_record      | anyelement       | base anyelement, from_json
json, use_json_as_text boolean | normal
 pg_catalog | json_populate_recordset   | SETOF anyelement | base anyelement, from_json
json, use_json_as_text boolean | normal
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

**Basic usage**

```
SELECT array_to_json('{{1,5},{99,100}}'::int[]);
```

The following information is returned:

```
  array_to_json
------------------
 [[1,5],[99,100]]
(1 row) SELECT row_to_json(row(1,'foo'));
```

The following information is returned:

```json
     row_to_json
---------------------
 {"f1":1,"f2":"foo"}
(1 row) SELECT json_array_length('[1,2,3,{"f1":1,"f2":[5,6]},4]');
```

The following information is returned:

```json
 json_array_length
------------------- (1 row) SELECT * FROM json_each('{"f1":[1,2,3],"f2": {"f3":1},"f4":null,"f5":99,"f6":"stringy"}') q;
```

The following information is returned:

```
 key |   value
-----+-----------
 f1  | [1,2,3]
 f2  | {"f3":1}
 f4  | null
 f5  | 99
 f6  | "stringy"
(5 rows) SELECT json_each_text('{"f1":[1,2,3],"f2":{"f3":1},"f4":null,"f5":"null"}');
```

The following information is returned:

```
  json_each_text
-------------------
 (f1,"[1,2,3]")
 (f2,"{""f3"":1}")
 (f4,)
 (f5,null)
(4 rows) SELECT json_array_elements('[1,true,[1,[2,3]],null,{"f1":1,"f2":[7,8,9]},false]');
```

The following information is returned:

```json
  json_array_elements
-----------------------
 true
 [1,[2,3]]
 null
 {"f1":1,"f2":[7,8,9]}
 false
(6 rows) CREATE TYPE jpop AS (a text, b int, c timestamp); SELECT * FROM json_populate_record(null::jpop,'{"a":"blurfl","x":43.2}', false) q;
```

The following information is returned:

```
   a    | b | c
--------+---+---
 blurfl |   |
(1 row) SELECT * FROM json_populate_recordset(null::jpop,'[{"a":"blurfl","x":43.2},{"b":3,"c" :"2012-01-20 10:42:53"}]',false) q;
```

The following information is returned:

```
   a    | b |            c
--------+---+--------------------------
 blurfl |   |
        | 3 | Fri Jan 20 10:42:53 2012
(2 rows)
```

**Code examples**

**Create a table**

Create a table and insert data into the table.

```
CREATE TABLE tj(id serial, ary int[], obj json, num integer); INSERT INTO tj(ary, obj, num) VALUES('{1,5}'::int[], '{"obj":1}', 5);
```

Query information from the table.

```
SELECT row_to_json(q) FROM (select id, ary, obj, num from tj) AS q;
```

The following information is returned:

```json
                row_to_json
-------------------------------------------
 {"f1":1,"f2":[1,5],"f3":{"obj":1},"f4":5}
(1 row)
```

Insert data into the table.

```
INSERT INTO tj(ary, obj, num) VALUES('{2,5}'::int[], '{"obj":2}', 5);
```

Query information from the table.

```
SELECT row_to_json(q) FROM (select id, ary, obj, num from tj) AS q;
```

The following information is returned:

```json
                row_to_json
-------------------------------------------
 {"f1":1,"f2":[1,5],"f3":{"obj":1},"f4":5}
 {"f1":2,"f2":[2,5],"f3":{"obj":2},"f4":5}
(2 rows)
```

**Join multiple tables**

Create a table and insert data into the table.

```
CREATE TABLE tj2(id serial, ary int[], obj json, num integer); INSERT INTO tj2(ary, obj, num) VALUES('{2,5}'::int[], '{"obj":2}', 5);
```

Query information from the table.

```
SELECT * FROM tj, tj2 where tj.obj->>'obj' = tj2.obj->>'obj';
```

The following information is returned:

```
 id |  ary  |    obj    | num | id |  ary  |    obj    | num
----+-------+-----------+-----+----+-------+-----------+-----
  2 | {2,5} | {"obj":2} |   5 |  1 | {2,5} | {"obj":2} |   5
(1 row)
```

Query information from the table.

```
SELECT * FROM tj, tj2 WHERE json_object_field_text(tj.obj, 'obj') = json_object_field_text(tj2.obj, 'obj');
```

The following information is returned:

```
 id |  ary  |    obj    | num | id |  ary  |    obj    | num
----+-------+-----------+-----+----+-------+-----------+-----
  2 | {2,5} | {"obj":2} |   5 |  1 | {2,5} | {"obj":2} |   5
(1 row)
```

**Use the JSON function index**

Create a table and insert data into the table.

```
CREATE TEMP TABLE test_json (
       json_type text,
       obj json
```

);

```
INSERT INTO test_json VALUES('aa', '{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}'); INSERT INTO test_json VALUES('cc', '{"f7":{"f3":1},"f8":{"f5":99,"f6":"foo"}}');
```

Query information from the table.

```
SELECT obj->'f2' FROM test_json WHERE json_type = 'aa';
```

The following information is returned:

```json
 ?column?
----------
 {"f3":1}
(1 row)
```

Create an index in the table.

```
CREATE INDEX i ON test_json (json_extract_path_text(obj, '{f4}'));
```

Query information from the table.

```
SELECT * FROM test_json where json_extract_path_text(obj, '{f4}') = '{"f5":99,"f6":"foo"}';
```

The following information is returned:

```
 json_type |                 obj
-----------+-------------------------------------------
 aa        | {"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}
(1 row)
```

**Note**

JSON data cannot be used as the distribution key and does not support JSON aggregate functions. The following example demonstrates how to use Python to access the database:

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
def main():
    sql = "select obj from tj;"
    #rows = Connection(host, port, user, pwd, dbname).query(sql)
    rows = gpquery(sql)
    for row in rows:
        print json.loads(row[0])
if __name__ == "__main__":
    main()
```

### Use HyperLogLog

AnalyticDB for PostgreSQL is highly optimized by Alibaba Cloud. It has the features of Greenplum Database and supports HyperLogLog. AnalyticDB for PostgreSQL is suited for industries such as Internet advertising and estimation analysis that require quick estimation of business metrics such as page views (PVs) and unique visitors (UVs).

**Create a HyperLogLog plug-in**

Execute the following statement to create a HyperLogLog plug-in:

```
CREATE EXTENSION hll;
```

**Basic types**

Execute the following statement to create a table that contains the hll field:

```
CREATE TABLE agg (id int primary key,userids hll);
```

Execute the following statement to convert int to hll_hashval:

```
SELET 1::hll_hashval;
```

**Basic operators**

The hll type supports =, !=, <>, ||, and #.

```
SELECT hll_add_agg(1::hll_hashval) = hll_add_agg(2::hll_hashval); SELECT hll_add_agg(1::hll_hashval) || hll_add_agg(2::hll_hashval); SELECT #hll_add_agg(1::hll_hashval);
```

The hll_hashval type supports =, !=, and <>.

```
SELECT 1::hll_hashval = 2::hll_hashval; SELECT 1::hll_hashval <> 2::hll_hashval;
```

**Basic functions**

Hash functions such as hll_hash_boolean, hll_hash_smallint, and hll_hash_bigint.

```
SELECT hll_hash_boolean(true); SELECT hll_hash_integer(1);
```

hll_add_agg: converts the int format to the hll format.

```
SELECT hll_add_agg(1::hll_hashval);
```

hll_union: aggregates the hll fields.

```
SELECT hll_union(hll_add_agg(1::hll_hashval),hll_add_agg(2::hll_hashval));
```

hll_set_defaults: sets the precision.

```
SELECT hll_set_defaults(15,5,-1,1);
```

hll_print: displays debugging information.

```
SELECT hll_print(hll_add_agg(1::hll_hashval));
```

**Examples**

1. Create a test table.

```
CREATE TABLE access_date (acc_date date unique, userids hll);
```

2. Insert test data into the table.

```
INSERT INTO access_date SELECT current_date, hll_add_agg(hll_hash_integer(user_id)) F ROM generate_series(1,10000) t(user_id); INSERT INTO access_date SELECT current_date-1, hll_add_agg(hll_hash_integer(user_id)) FROM generate_series(5000,20000) t(user_id); INSERT INTO access_date SELECT current_date-2, hll_add_agg(hll_hash_integer(user_id)) FROM generate_series(9000,40000) t(user_id);
```

3. View the test results of the HyperLogLog plug-in.

```
select #userids from access_date where acc_date=current_date;
```

The following information is returned:

```
     ?column?
------------------
 9725.85273370708
(1 row)
```

```
select #userids from access_date where acc_date=current_date-1;
```

The following information is returned:

```
     ?column?
------------------
 14968.6596883279
(1 row) select #userids from access_date where acc_date=current_date-2;
```

The following information is returned:

```
     ?column?
------------------
 29361.5209149911
(1 row)
```

### Use the CREATE LIBRARY

**statement**

AnalyticDB for PostgreSQL introduces the CREATE LIBRARY and DROP LIBRARY statements to help you import custom software packages.

**Syntax**

```
CREATE LIBRARY library_name LANGUAGE [JAVA] FROM oss_location OWNER ownername CREATE LIBRARY library_name LANGUAGE [JAVA] VALUES file_content_hex OWNER ownername DROP LIBRARY library_name
```

Table 1. Parameters

| Parameter | Description |
|---|---|
| library name _ | The name of the library that you want to install. If the library that you want to install has the same name as an existing library, you must delete the existing library before you install the new one. |
| LANGUAGE [JAVA] | The programming language that you want to use. Only PL/Java is supported. |
| oss location _ | The location of the package. You can specify the Object Storage Service (OSS) bucket and object names. Only one object can be specified and the specified object cannot be a compressed file. Sample format: oss://oss endpoint filepath= _ [folder/[folder/]...]/file name id=userossid _ key=userosskey bucket=ossbucket |

| file content hex _ _ | The content of the file. The byte stream is in hexadecimal notation. For example, 73656c6563742031 indicates the hexadecimal byte stream of "select 1". You can use this syntax to import packages without the need to use OSS. |
|---|---|
| ownername | The user. |
| DROP LIBRARY | Deletes a library. |

**Examples**

Example 1: Install a JAR package named analytics.jar.

```
create library example language java from 'oss://oss-cn-hangzhou.aliyuncs.com filepat h=analytics.jar id=xxx key=yyy bucket=zzz';
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

### Create and use a PL/Java UDF

AnalyticDB for PostgreSQL allows you to compile and upload JAR software packages that are written in PL/Java language, and use these JAR packages to create user-defined functions (UDFs). AnalyticDB for PostgreSQL supports PL/Java 1.5.0 and JVM 1.8. This topic describes how to create a PL/Java UDF. For more information about PL/Java examples, see PL/Java code. For more information about the compiling method, see PL/Java documentation.

**Procedure**

1. In AnalyticDB for PostgreSQL, execute the following statement to create a PL/Java
extension. You need only to execute the statement once for each database.

```
create extension pljava;
```

2. Compile the UDF based on your business requirements. For example, you can use the
following code to compile the Test.java file:

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
                         process = Runtime.getRuntime().exec("echo Test running");
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

5. Upload the analytics.jar file generated in Step 4 to Object Storage Service (OSS) by using
the following OSS console command:

```
 osscmd put analytics.jar oss://zzz
```

6. In AnalyticDB for PostgreSQL, execute the CREATE LIBRARY statement to import the file to
AnalyticDB for PostgreSQL.

```
create library example language java from 'oss://oss-cn-hangzhou.aliyuncs.com filepat h=analytics.jar id=xxx key=yyy bucket=zzz';
```

**Note**

You can only use the filepath variable in the CREATE LIBRARY statement to import files one at a time. The CREATE LIBRARY statement also supports byte streams to import files without the need to use OSS. For more information, see Use the CREATE LIBRARY statement.
7. In AnalyticDB for PostgreSQL, execute the following statements to create and use the UDF:

```
create table temp (a varchar) distributed randomly;
 insert into temp values ('my string');
 create or replace function java_substring(varchar, int, int) returns varchar as 'Tes
t.substring' language java;
 select java_substring(a, 1, 5) from temp;
```

## Table

### Create a table

You can create tables within your databases.

**Syntax**

The following statement shows how to create a table. Not all clauses are required. Use the clauses that can fulfill your business needs.

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

`)` Definition of the **column_constraint** clause:

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

Definition of the **storage_directive** clause of columns:

```
   COMPRESSTYPE={ZLIB | QUICKLZ | RLE_TYPE | NONE}
    [COMPRESSLEVEL={0-9} ]
    [BLOCKSIZE={8192-2097152} ]
```

Definition of the **storage_parameter** clause of tables:

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

Definition of the **table_constraint** clause:

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

Valid values of **key_match_type**:

```
    MATCH FULL
  | SIMPLE
```

Valid values of **key_action**:

```
    ON DELETE
  | ON UPDATE
  | NO ACTION
  | RESTRICT
  | CASCADE
  | SET NULL
  | SET DEFAULT
```

Valid values of **key_checking_mode**:

```
    DEFERRABLE
  | NOT DEFERRABLE
  | INITIALLY DEFERRED
  | INITIALLY IMMEDIATE
```

Valid values of **partition_type**:

```
    LIST
  | RANGE
```

Definition of the **partition_specification** clause:

```
partition_element [, ...]
```

Definition of the **partition_element** clause:

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

Definition of the **subpartition_spec** or **template_spec** clause:

```
subpartition_element [, ...]
```

Definition of the **subpartition_element** clause:

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

Definition of the **storage_parameter** clause:

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

**Parameters**

The Table creation parameters table describes the key parameters for creating a table. Table 1. Table creation parameters

| Parameter | Description |
|---|---|
| TABLE NAME _ | The name of the table that you want to create. |
| column name _ | The name of a column that you want to create in the table. |
| data type _ | The data type of the column. For columns that contain textual data, set the data type toV ARCHAR or TEXT. We recommend that you do not use theC HAR type. |
| DEFAULT default expr _ | Specifies a default value for the column. The system assigns this default value to all columns that do not have a value. The default value can be a variable-free expression. Subqueries or cross-references to other columns in the table are not allowed. The data type of the default expression must match the data type of the column. If a column does not have a default value, this parameter is left empty. |
| ENCODING storage directive _ | Specifies the compression type and block size for the column data. This clause is valid only for append-optimized, column-oriented tables. Column compression settings are inherited from the table level to the partition level and then to the sub-partition level. The lowest-level settings have the highest priority. |
| INHERITS | Configures all columns in the new table to automatically inherit a parent table. You can use INHERITS to create a persistent relationship between the new child table and its parent table. Schema modifications to the parent table are applied to the child table as well. When the parent table is also scanned, the data of the child table is scanned as well. |
| LIKE other table _ | Specifies a table from which the new table automatically copies all column names, data types, NOT NULL constraints, and distribution policies. Storage properties such as append-optimized or partition structure are not copied. Unlike INHERITS, the new table is completely decoupled from the original table after the new table is created. |
| CONSTRAINT constraint name _ | Configures a column or table constraint. If a constraint is violated, the constraint name is displayed in the error message. Constraint names can be used to communicate helpful information to client applications.Constraint names that contain spaces must be enclosed by double quotation marks (''). |

| WITH ( storage option=value ) _ | Configures storage options for the table or its indexes. |
|---|---|
| ON COMMIT | The operation that the system performs on the temporary tables at the end of a transaction. Valid values: PRESERVE ROWS: No special action is taken. The data is retained after the transaction is complete. The data is released only when the session is disconnected. DELETE ROWS: All rows in the temporary table are deleted. DROP: The temporary table is deleted. |
| TABLESPACE tablespace | Specifies the name of the tablespace in which you want to create the new table. If this parameter is not specified, the default tablespace of the database is used. |
| DISTRIBUTED BY | Configures the distribution policy for the database. DISTRIBUTED BY (column, [ ... ] ): specifies the distribution key. The system distributes data based on the distribution key. To evenly distribute data, you must set the distribution key to the primary key of the table or a unique column or a set of columns. DISTRIBUTED RANDOMLY: randomly distributes data. Note We recommend that you do not use random distribution. |
| PARTITION BY | Configures a partition key to partition the table. Partitioning large tables improves data access efficiency. To partition a table is to create a top-level (parent) table and multiple lower-level (child) tables. After a partition table is created, its parent table is always empty. Data is stored in the lowest-level child tables. In a multi- level partition table, data is stored only in the lowest-level sub-partitions. Valid values: RANGE, LIST, and a combination of the two. |
| SUBPARTITION BY | Configures a multi-level partition table. |
| SUBPARTITION TEMPLATE | Specifies a sub-partition template to create sub-partitions (lower-level child tables). This ensures that all parent partitions have the same sub-partition structure. |

**Examples**

Create a table and configure a distribution key. By default, a primary key is used as a distribution key in AnalyticDB for PostgreSQL.

```
CREATE TABLE films ( code char(5) CONSTRAINT firstkey PRIMARY KEY, title varchar(40) NOT NULL, did integer NOT NULL, date_prod date, kind varchar(10), len interval hour to minute
```

);

```
CREATE TABLE distributors ( did integer PRIMARY KEY DEFAULT nextval('serial'), name varchar(40) NOT NULL CHECK (name <> '')
```

); Create a compressed table and configure a distribution key.

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

### Principles and scenarios of

**row store, column store, heap**

**tables, and AO tables**

AnalyticDB for PostgreSQL supports row store, column store, heap tables, and appendoptimized (AO) tables. This topic describes their principles and scenarios.

**Row store and column store**

Table 1. Comparison

| Dimension | Row store | Column store |
|---|---|---|
| Definition | Row store stores data in the form of rows. Each row is a tuple. To read a column, you must deform all of the columns that precede it. Therefore, the costs for accessing the first and the last columns are different. | Column store stores data as columns. Each column corresponds to a file or a batch of files. The cost of reading each column is the same. However, if you want to read multiple columns, you must access multiple files. The more columns you access, the higher the overheads are. |
| Compression ratio | Low. | High. |
| Cost of reading a column | The higher the column number, the higher the cost of reading the column. | Same. |
| Vector computing and JIT architecture | Not suitable. Not suitable for batch computing. | Suitable. More efficient when you access and collect statistics of a batch of data. |
| Scenarios | If you need to perform a large number of update and delete operations due to online transaction processing (OLTP) requirements such as when you query table details where multiple columns are returned, you can use row store. You can use partition tables if you have complex requirements. For example, if you want to partition data based on time, you can use row store to query the details of recent data and use column store to obtain more statistics from historical data. | You can use column store if you need data statistics because of online analytical processing (OLAP) requirements. If you want a higher compression ratio, you can use column store. |

**Heap tables**

A heap table is heap storage. All changes to the heap table generate redo logs that can be used to restore data by point in time. However, heap tables cannot implement logical incremental backup because all data blocks in the tables can be changed and it is inconvenient to record the position by using heap storage. Commit and redo logs are used to ensure reliability when transactions are finished. You can also implement redundancy by using secondary nodes through redo logs.

**AO tables**

AO tables are used to append data for storage. When you delete the updated data, you can use another bitmap file to mark the row that you want to delete and then use the offset of the bit to determine whether the row was deleted. When the transaction is finished, you must call the fsync() function to record the offset of the data block that performs the last write operation. Even if the data block contains only a single record, a new data block is appended for the next transaction. The data block is synchronized to the secondary node for data redundancy. AO tables are not suitable for small transactions because the fsync() function is called at the end of each transaction. This data block is not reused even if space is left. AO tables are suitable for OLAP scenarios, batch data writing, high compression ratio, and logical backup that supports incremental backup. During backup, you need only to record the offset from the backup and the bitmap deletion mark for each full backup.

**Use scenarios of heap tables**

When multiple small transactions are handled, use a heap table. When you need to restore data by point in time, use a heap table.

**Use scenarios of AO tables**

When you want to use column store, use an AO table. When data is written in batches, use an AO table.

### Enable the column store and

**compression features**

If you want to improve performance, speed up data import, or reduce costs for tables that have infrequent updates and multiple fields, we recommend that you use column store and compression. These features increase the compression ratio by up to threefold to ensure high performance and speed up data import. To enable the column store and compression features, you must specify the column store and compression options when you create a table. For example, you can add the following clause to the CREATE statement to enable these features. For more information about the table creation syntax, see Create a table.

```
with (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, BLOCKSIZ E=1048576, OIDS=false)
```

**Note**

AnalyticDB for PostgreSQL supports only zlib and RLE_TYPE compression algorithms. If you specify the quicklz algorithm, it is automatically converted to zlib.

### Add a field to a column-

**oriented table and set the default**

**value**

This topic describes how to add a field to a column-oriented table and set the default value for the field, and how to use the ANALYZE statement to view the impact of updated data on the size of the column-oriented table.

**Background information**

In a column-oriented table, each column is stored as a file, and two columns in the same row correspond to each other by using an offset. For example, if you add two fields of the INT8 type, you can quickly locate column B from column A by using the offset. When you add a field, append-optimized (AO) tables are not rewritten. If an AO table contains the records of deleted data, the added field must be filled with the deleted records before the offset can be used.

**Procedure**

1. Create three append-optimized column-oriented (AOCO) tables.

```
CREATE TABLE tbl1 (id int, info text) WITH (appendonly=true, blocksize=8192, compress type=none, orientation=column); CREATE TABLE tbl2 (id int, info text) WITH (appendonly=true, blocksize=8192, compress type=none, orientation=column); CREATE TABLE tbl3 (id int, info text) WITH (appendonly=true, blocksize=8192, compress type=none, orientation=column);
```

2. Insert 10 million entries to the first two tables and 20 million entries to the third one.

```
INSERT INTO tbl1 SELECT generate_series(1,10000000),'test'; INSERT INTO tbl2 SELECT generate_series(1,10000000),'test'; INSERT INTO tbl3 SELECT generate_series(1,20000000),'test';
```

3. Analyze the tables and query the table sizes.
Execute the following statements to analyze each table:

```
ANALYZE tbl1; ANALYZE tbl2; ANALYZE tbl3;
```

Execute the following statements to query the size of each table:

```
SELECT pg_size_pretty(pg_relation_size('tbl1'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 88 MB
(1 row) SELECT pg_size_pretty(pg_relation_size('tbl2'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 88 MB
(1 row)
```

```
SELECT pg_size_pretty(pg_relation_size('tbl3'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 173 MB
(1 row)
```

4. Update all the data in the first table. Query the table size after the update. The size is twice
as large as the size before the update. Execute the following statement to update all the data in the first table:

```
UPDATE tbl1 SET INFO='test';
```

Execute the following statement to analyze the first table again:

```
ANALYZE tbl1;
```

Execute the following statement to query the size of the first table:

```
SELECT pg_size_pretty(pg_relation_size('tbl1'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 173 MB
(1 row)
```

5. Add fields to the three tables and set the default values.

```
ALTER TABLE tbl1 ADD column c1 int8 default 1; ALTER TABLE tbl2 ADD column c1 int8 default 1; ALTER TABLE tbl3 add column c1 int8 default 1;
```

6. Analyze the tables and query the table sizes.
Execute the following statements to analyze each table:

```
ANALYZE tbl1; ANALYZE tbl2; ANALYZE tbl3;
```

Execute the following statements to query the size of each table:

```
SELECT pg_size_pretty(pg_relation_size('tbl1'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 325 MB
(1 row) SELECT pg_size_pretty(pg_relation_size('tbl2'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 163 MB
(1 row) SELECT pg_size_pretty(pg_relation_size('tbl3'));
```

The following information is returned:

```
 pg_size_pretty
----------------
 325 MB
(1 row)
```

When you add fields to the AO tables, the number of entries in the existing tables prevails. Even if all the entries are deleted, new fields are added to the original data.

### Configure table partitions

For fact tables and large-sized tables in a database, we recommend that you configure table partitions.

**Configure table partitions**

You can use the table partitioning feature to add and remove data based on table partitions

| ALTER TABLE DROP PARTITION | sta |
|---|---|

the data in a partition, and use the `ALTER TABLE EXCHANGE PARTITION` statement to import data to a new data partition. AnalyticDB for PostgreSQL supports range partitioning, list partitioning, and composite partitioning. Range partitioning supports only the numeric or datetime data types of fields. The following example shows how to use range partitioning in a table:

```
CREATE TABLE LINEITEM ( L_ORDERKEY BIGINT NOT NULL, L_PARTKEY BIGINT NOT NULL, L_SUPPKEY BIGINT NOT NULL, L_LINENUMBER INTEGER, L_QUANTITY FLOAT8, L_EXTENDEDPRICE FLOAT8, L_DISCOUNT FLOAT8, L_TAX FLOAT8, L_RETURNFLAG CHAR(1), L_LINESTATUS CHAR(1), L_SHIPDATE DATE, L_COMMITDATE DATE, L_RECEIPTDATE DATE, L_SHIPINSTRUCT CHAR(25), L_SHIPMODE CHAR(10), L_COMMENT VARCHAR(44) ) WITH (APPENDONLY=true, ORIENTATION=column, COMPRESSTYPE=zlib, COMPRESSLEVEL=5, BLOC KSIZE=1048576, OIDS=false) DISTRIBUTED BY (l_orderkey) PARTITION BY RANGE (L_SHIPDATE) (START (date '1992-01-01') INCLUSIVE END (date '2000-01 -01') EXCLUSIVE EVERY (INTERVAL '1 month' ));
```

**Principles of table partitioning**

The purpose of partitioning is to minimize the amount of data to be scanned during a query. Therefore, partitions must be associated with the query conditions. Principle 1: Select the fields that are related to the query conditions to configure partitions and reduce the amount of data to be scanned. Principle 2: If multiple query conditions exist, configure sub-partitions to further reduce the amount of data to be scanned.

### Configure the sort key

A sort key is an attribute of a table. Data on disks is stored in the order of the sort key.

**Background information**

Sort keys have two major advantages: Speed up and optimize column-store operations. The min and max meta information the system collects seldom overlaps with each other, which features good filterability. Eliminate the need to perform ORDER BY and GROUP BY operations. The data directly read from the disk is ordered as required by the sorting conditions.

**Create a table**

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

`)`

**Examples:**

```
create table test(date text, time text, open float, high float, low float, volume int) with(APPENDONLY=true,ORIENTATION=column) sortkey (volume);
```

**Sort the table**

```
VACUUM SORT ONLY [tablename]
```

**Modify the sort key**

This statement only modifies the catalog and does not sort data. You must execute the `VACUUM SORT ONLY` statement to sort the table.

```
ALTER [[GLOBAL | LOCAL] {TEMPORARY | TEMP}] TABLE table_name SET SORTKEY (column, [ ... ] )
```

Examples:

```
alter table test set sortkey (high,low);
```

## Vector analysis

AnalyticDB for PostgreSQL provides vector analysis to help you implement approximate search and analysis of unstructured data. This topic describes the capabilities and benefits of vector analysis.

**Introduction to vector databases**

In real-world scenarios, most data is presented in the form of unstructured data, such as images, audio, videos, and text. Unstructured data exponentially grows with the emergence of applications in fields such as smart cities, short videos, personalized product recommendation, and visual product search. To process unstructured data, AI technologies are used to extract features from the unstructured data, convert the features into feature vectors, and then analyze and retrieve the feature vectors. The databases that can store, analyze, and retrieve feature vectors are called vector databases. Vector databases use the vector index technology to quickly retrieve feature vectors. In most cases, vector indexes are used for approximate nearest neighbor search (ANNS). The purpose of vector indexes is to search for the nearest neighbor data and return the most accurate results to improve search efficiency. Compared with traditional databases, vector databases implement highly efficient data search with an acceptable compromise in accuracy. Two methods are available to apply ANNS vector indexes to the production environment: Build a **dedicated vector database** that provides the ANNS vector index service to help create vector indexes and retrieve data. Integrate ANNS vector indexes into traditional structured databases to build a **database**
**management system (DBMS) that provides the vector search capability**.
AnalyticDB for PostgreSQL vector databases are a type of DBMS that integrates the in-house
**FastANN** vector engine. AnalyticDB for PostgreSQL vector databases also provide end-to-end
database capabilities such as ease of use, transaction processing, high availability, and high scalability.

**How it works**

To implement vector analysis, vector databases use AI algorithms to extract features from unstructured data and then use feature vectors to identify the unstructured data. The distance between vectors is used to measure the similarity between unstructured data. AnalyticDB for PostgreSQL uses a massively parallel processing (MPP) architecture to implement vector search and analysis. You can use SQL statements to retrieve unstructured data and perform correlation analysis of structured and unstructured data.

**Scenarios**

You can use AnalyticDB for PostgreSQL vector analysis in the following intelligent application scenarios: Reverse image search. You can search for images that are similar to a specified image. Video search. You can search for video images that are similar to a specified video image. Voiceprint search. You can search for audio files that are similar to a specified audio file based on voiceprint recognition. Recommendation system. Suitable features can be recommended based on user characteristics. Text search. You can search for texts that are similar to a specified text based on semantics. Q&A chatbots that are built in combination with large language models. File deduplication. You can remove duplicate files based on the fingerprint of a specified file.

**Benefits**

AnalyticDB for PostgreSQL vector databases use the in-house FastANN vector engine to provide the vector analysis capability. Vector analysis is widely used in various fields such as Alibaba Group data mid-end, e-commerce, new retail, Alibaba Cloud City Brain, and Tongyi Qianwen Q&A service. Compared with other vector databases, AnalyticDB for PostgreSQL vector databases provide the following advantages: Hybrid analysis of structured and unstructured data AnalyticDB for PostgreSQL vector databases use the capabilities of traditional databases to implement hybrid analysis of structured, semi-structured, and unstructured data and utilize structured and semi-structured indexing capabilities in an efficient manner. Two-way retrieval based on vector search and full-text search AnalyticDB for PostgreSQL vector databases support vector indexes and full-text indexes, and can use vector search and full-text search to implement two-way retrieval. This significantly improves the retrieval accuracy of vector data. Real-time data update and query AnalyticDB for PostgreSQL vector databases support streaming import and real-time building of vector data. Ease of use AnalyticDB for PostgreSQL vector databases are easy to use after you create an instance and support standard SQL syntax. This significantly simplifies the development process. Cost-effectiveness AnalyticDB for PostgreSQL vector databases can compress FP32 data to the FP16 format. This reduces storage costs by 50%. AnalyticDB for PostgreSQL vector databases also build vector indexes on the segmented paging storage, and can utilize the cache-based swapping mechanism based on the shared buffer of PostgreSQL. This way, AnalyticDB for PostgreSQL can store vector indexes that exceed the available memory size.

### Overview

AnalyticDB for PostgreSQL provides vector analysis to help you implement approximate search and analysis of unstructured data. This topic describes the capabilities and benefits of vector analysis.

**Introduction to vector databases**

In real-world scenarios, most data is presented in the form of unstructured data, such as images, audio, videos, and text. Unstructured data exponentially grows with the emergence of applications in fields such as smart cities, short videos, personalized product recommendation, and visual product search. To process unstructured data, AI technologies are used to extract features from the unstructured data, convert the features into feature vectors, and then analyze and retrieve the feature vectors. The databases that can store, analyze, and retrieve feature vectors are called vector databases. Vector databases use the vector index technology to quickly retrieve feature vectors. In most cases, vector indexes are used for approximate nearest neighbor search (ANNS). The purpose of vector indexes is to search for the nearest neighbor data and return the most accurate results to improve search efficiency. Compared with traditional databases, vector databases implement highly efficient data search with an acceptable compromise in accuracy. Two methods are available to apply ANNS vector indexes to the production environment: Build a **dedicated vector database** that provides the ANNS vector index service to help create vector indexes and retrieve data. Integrate ANNS vector indexes into traditional structured databases to build a **database**
**management system (DBMS) that provides the vector search capability**.
AnalyticDB for PostgreSQL vector databases are a type of DBMS that integrates the in-house
**FastANN** vector engine. AnalyticDB for PostgreSQL vector databases also provide end-to-end
database capabilities such as ease of use, transaction processing, high availability, and high scalability.

**How it works**

To implement vector analysis, vector databases use AI algorithms to extract features from unstructured data and then use feature vectors to identify the unstructured data. The distance between vectors is used to measure the similarity between unstructured data. AnalyticDB for PostgreSQL uses a massively parallel processing (MPP) architecture to implement vector search and analysis. You can use SQL statements to retrieve unstructured data and perform correlation analysis of structured and unstructured data.

**Scenarios**

You can use AnalyticDB for PostgreSQL vector analysis in the following intelligent application scenarios: Reverse image search. You can search for images that are similar to a specified image. Video search. You can search for video images that are similar to a specified video image. Voiceprint search. You can search for audio files that are similar to a specified audio file based on voiceprint recognition. Recommendation system. Suitable features can be recommended based on user characteristics. Text search. You can search for texts that are similar to a specified text based on semantics. Q&A chatbots that are built in combination with large language models. File deduplication. You can remove duplicate files based on the fingerprint of a specified file.

**Benefits**

AnalyticDB for PostgreSQL vector databases use the in-house FastANN vector engine to provide the vector analysis capability. Vector analysis is widely used in various fields such as Alibaba Group data mid-end, e-commerce, new retail, Alibaba Cloud City Brain, and Tongyi Qianwen Q&A service. Compared with other vector databases, AnalyticDB for PostgreSQL vector databases provide the following advantages: Hybrid analysis of structured and unstructured data AnalyticDB for PostgreSQL vector databases use the capabilities of traditional databases to implement hybrid analysis of structured, semi-structured, and unstructured data and utilize structured and semi-structured indexing capabilities in an efficient manner. Two-way retrieval based on vector search and full-text search AnalyticDB for PostgreSQL vector databases support vector indexes and full-text indexes, and can use vector search and full-text search to implement two-way retrieval. This significantly improves the retrieval accuracy of vector data. Real-time data update and query AnalyticDB for PostgreSQL vector databases support streaming import and real-time building of vector data. Ease of use AnalyticDB for PostgreSQL vector databases are easy to use after you create an instance and support standard SQL syntax. This significantly simplifies the development process. Cost-effectiveness AnalyticDB for PostgreSQL vector databases can compress FP32 data to the FP16 format. This reduces storage costs by 50%. AnalyticDB for PostgreSQL vector databases also build vector indexes on the segmented paging storage, and can utilize the cache-based swapping mechanism based on the shared buffer of PostgreSQL. This way, AnalyticDB for PostgreSQL can store vector indexes that exceed the available memory size.

### Usage of the vector search

**engine**

#### Enable or disable vector search engine

**optimization**

AnalyticDB for PostgreSQL performs significant engine parameter optimization for vector database scenarios. To use vector search engine optimization, you must enable the feature in the console. This topic describes how to enable or disable vector search engine optimization.

**Scenarios**

In vector analysis scenarios such as AI-generated content (AIGC) and vector search, we recommend that you enable vector search engine optimization. In mainstream analysis, data warehousing, and real-time data warehousing scenarios, we recommend that you disable vector search engine optimization.

**Prerequisites**

An AnalyticDB for PostgreSQL instance in elastic storage mode is created. The minor version of the instance is 6.3.10.18 or later. You cannot enable or disable vector search engine optimization for AnalyticDB for PostgreSQL instances of V7.x.x.x. The compute node specifications of the instance are 4 cores and 32 GB or higher. If your instance does not meet the requirement, upgrade node specifications of your instance.

**Usage notes**

Vector search engine optimization consumes large amounts of memory resources of your instance and significantly decreases the concurrency of queries. Make sure that you have learned the impact before you enable vector search engine optimization.

**Warning**

After you enable or disable vector search engine optimization, your instance restarts. During the restart, your instance is unavailable. We recommend that you perform this operation during off-peak hours and make sure that your application can automatically reconnect to the instance.

**Procedure**

1. Log on to the AnalyticDB for PostgreSQL console.
2. In the upper-left corner of the console, select a region.
3. Find the instance that you want to manage and click the instance ID.
4. In the **Basic Information** section, click **Enable Optimization** next to **Vector Search**
**Engine Optimization**.
5. In the message that appears, click **OK**.
To disable vector search engine optimization, click **Disable Optimization** next to **Vector**
**Search Engine Optimization**.

#### Access vector databases

##### Use SQL statements to access vector

## databases

After you enable the vector search engine optimization feature, you can use SQL statements to access AnalyticDB for PostgreSQL vector databases. This topic describes how to use Java, Python, and C code to access vector databases.

**Java**

You can use the Java Database Connectivity (JDBC) driver of PostgreSQL or Greenplum to connect to AnalyticDB for PostgreSQL vector databases. For more information, see JDBC. Make sure that the PostgreSQL JDBC driver is available. If you use Maven, you can add the following dependencies to the pom.xml file:

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.5</version>
</dependency>
```

The following sample code provides an example on how to use Java code to access vector databases:

```java
import java.sql.Connection; import java.sql.DriverManager; import java.sql.ResultSet; import java.sql.Statement; public class GreenplumSample {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://yourhost:yourport/yourdbname";
        String user = "yourusername";
        String password = "yourpassword";
        try {
            // Load the driver.
            Class.forName("org.postgresql.Driver");
            // Create a connection.
            Connection con = DriverManager.getConnection(url, user, password);
            // Create a query statement.
            Statement st = con.createStatement();
            // Execute the query statement.
            String query = "SELECT * FROM yourtable LIMIT 10";
            ResultSet rs = st.executeQuery(query);
            // Obtain the query result.
            while(rs.next()) {
                // For example, the result set contains at least one column of the
string type.
                String resultColumn = rs.getString(1);
                System.out.println(resultColumn);
```

`}`

```
            // Disable resources.
            rs.close();
            st.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
```

`}` `}` `}`

**Python**

You can use psycopg2 to connect to AnalyticDB for PostgreSQL vector databases and Python code to import and query vector data. For more information, see Python. The following sample code provides an example on how to use Python code to access vector databases:

```java
import psycopg2 from psycopg2 import pool
# Create a connection pool.
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    user='your_username',
password='yourpassword',
```

```
    password
your_password,
    host='your_host',
    port='your_port',
    database='your_database'
```

`)`

```python
# Check whether the connection is alive.
def is_connection_alive(conn):
    try:
        conn.cursor().execute("SELECT 1")
    except (psycopg2.OperationalError, psycopg2.InterfaceError):
        return False
    return True
# Obtain the connection object from the connection pool.
def get_connection():
    conn = connection_pool.getconn()
    while not is_connection_alive(conn):
        conn = connection_pool.getconn()
    return conn
# Release the connection object to the connection pool.
def release_connection(conn):
    connection_pool.putconn(conn)
# Use the connection object to execute a query statement.
def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if query.startswith("SELECT"):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None
    except (psycopg2.DatabaseError, psycopg2.InterfaceError) as e:
        print(f"Error executing query: {e}")
        conn.rollback()
        result = None
    cursor.close()
    release_connection(conn)
    return result
# Examples
# Query data.
select_query = "SELECT * FROM your_table" result = execute_query(select_query) if result:
    print(result)
# Insert data.
insert_query = "INSERT INTO your_table (column1, column2) VALUES ('value1', 'value2')" execute_query(insert_query)
```

```bash
# Update data.
update_query = "UPDATE your_table SET column1 = 'new_value' WHERE column2 = 'value2'" execute_query(update_query)
# Delete data.
delete_query = "DELETE FROM your_table WHERE column1 = 'value1'" execute_query(delete_query)
```

You can use libpg to connect to AnalyticDB for PostgreSQL vector databases and C code to import and query vector data. For more information, see libpq. The following sample code provides an example on how to use C code to access vector databases:

```
#include <stdio.h>
#include <stdlib.h>
#include <libpq-fe.h>
int main() {
    const char *conninfo;
    PGconn *conn;
    PGresult *res;
    int nFields;
    int i, j;
    // Specify a connection string.
    conninfo = "dbname=yourdbname user=yourusername host=yourhostname port=yourport pas
sword=yourpassword";
    // Create a connection.
    conn = PQconnectdb(conninfo);
    // Check the connection status.
    if (PQstatus(conn) != CONNECTION_OK) {
        fprintf(stderr, "Connection failed: %s", PQerrorMessage(conn));
        PQfinish(conn);
        exit(1);
```

`}`

```
    // Execute a query statement.
    res = PQexec(conn, "SELECT * FROM yourtablename LIMIT 10");
    // Check whether a correct result set is returned.
    if (PQresultStatus(res) != PGRES_TUPLES_OK) {
        fprintf(stderr, "Failed to return data from the SELECT statement: %s",
PQerrorMessage(conn));
        PQclear(res);
        PQfinish(conn);
        exit(1);
```

`}`

```
    // Obtain the number of fields.
    nFields = PQnfields(res);
```

```
    // Display each row of data.
    for (i = 0; i < PQntuples(res); i++) {
        for (j = 0; j < nFields; j++) {
            printf("%s = %s", PQfname(res, j), PQgetvalue(res, i, j));
```

`}`

```
        printf("\n");
```

`}`

```
    // Clear data.
    PQclear(res);
    // Close the connection.
    PQfinish(conn);
    return 0;
```

`}`

**References**

For information about how to use other language code to access AnalyticDB for PostgreSQL vector databases, see Use pgvector-compatible vector search.

##### Use API operations to access vector

## databases

###### Java

The AnalyticDB for PostgreSQL API encapsulates the vector-related DDL and DML operations of AnalyticDB for PostgreSQL. You can use API operations to manage vector data. This topic describes how to use API operations to import and query vector data by calling an SDK.

**Prerequisites**

An AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode is created. For more information, see Create an instance. Vector search engine optimization is enabled. For more information, see Enable or disable vector search engine optimization. A privileged account is created. For more information, see Create and manage database accounts.

**Procedure**

1. Initialize the vector database.
2. Create a namespace.
3. Create a collection.
4. Upload vector data.
5. Retrieve vector data.

**Initialize the vector database**

Before you use vector search, you must initialize the knowledgebase database and the fulltext search feature. The following sample code provides an example on how to 调用call an API operation:

```java
InitVectorDatabaseRequest request = new InitVectorDatabaseRequest(); request.setDBInstanceId("gp-bp1c62r3l489****"); request.setManagerAccount("myaccount"); request.setManagerAccountPassword("myaccount_password"); request.setRegionId("ap-southeast-1"); InitVectorDatabaseResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response));
```

For information about the relevant parameters, see InitVectorDatabase.

**Create a namespace**

Namespaces are used to separate schemas. Before you use vectors, you must create at least one namespace or use the public namespace. The following sample code provides an example on how to 调用call an API operation:

```java
CreateNamespaceRequest request = new CreateNamespaceRequest(); request.setDBInstanceId("gp-bp1c62r3l489****"); request.setManagerAccount("myaccount"); request.setManagerAccountPassword("myaccount_password"); request.setNamespace("vector_test"); request.setNamespacePassword("vector_test_password"); request.setRegionId("ap-southeast-1"); CreateNamespaceResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response));
```

For information about the relevant parameters, see CreateNamespace. After you create a namespace, you can query the corresponding schema in the knowledgebase database of the instance.

```
SELECT schema_name FROM information_schema.schemata;
```

**Create a collection**

Collections are used to store vector data and are separated by namespaces. The following sample code provides an example on how to 调用call an API operation:

```java
Map<String,String> metadata = new HashMap<>(); metadata.put("title", "text"); metadata.put("link", "text"); metadata.put("content", "text"); metadata.put("pv", "int"); List<String> fullTextRetrievalFields = Arrays.asList("title", "content"); CreateCollectionRequest request = new CreateCollectionRequest(); request.setDBInstanceId("gp-bp1c62r3l489****"); request.setManagerAccount("myaccount"); request.setManagerAccountPassword("myaccount_password"); request.setNamespace("vector_test"); request.setCollection("document"); request.setDimension(10L); request.setFullTextRetrievalFields(StringUtils.join(fullTextRetrievalFields, ",")); request.setMetadata(new Gson().toJson(metadata)); request.setParser("zh_ch"); request.setRegionId("ap-southeast-1"); CreateCollectionResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response));
```

After you create a collection, you can query the corresponding table in the knowledgebase database of the instance.

```
SELECT tablename FROM pg_tables WHERE schemaname='vector_test';
```

**Upload vector data**

Upload the prepared embedding vector data to the corresponding collection. The following sample code provides an example on how to 调用call an API operation:

```java
UpsertCollectionDataRequest request = new UpsertCollectionDataRequest(); request.setDBInstanceId("gp-bp1c62r3l489****"); request.setCollection("document"); request.setNamespace("vector_test"); request.setNamespacePassword("vector_test_password"); request.setRegionId("ap-southeast-1"); List<UpsertCollectionDataRequest.UpsertCollectionDataRequestRows> rows = new ArrayList< >(); UpsertCollectionDataRequest.UpsertCollectionDataRequestRows row = new UpsertCollectionDataRequest.UpsertCollectionDataRequestRows(); row.setId("0CB55798-ECF5-4064-B81E-FE35B19E01A6"); row.setVector(Arrays.asList(0.2894745251078251,0.5364747050266715,0.1276845661831275,0.22 8871956822372,0.7009319238651552,0.40267406135256123,0.8873626696379067,0.124852595577493 0.9115507046412368,0.2450859133174706)); Map<String, String> rowsMetadata = new HashMap<>(); rowsMetadata.put("title", "Test document"); rowsMetadata.put("content","Test content"); rowsMetadata.put("link","http://127.0.0.1/document1"); rowsMetadata.put("pv","1000"); row.setMetadata(rowsMetadata); rows.add(row); request.setRows(rows); UpsertCollectionDataResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response));
```

For information about the relevant parameters, see UpsertCollectionData. After you upload vector data, you can query the data in the knowledgebase database of the instance.

```
SELECT * FROM vector_test.document;
```

**Retrieve vector data**

Use the prepared vectors or full-text search fields to retrieve vector data. The following sample code provides an example on how to 调用call an API operation:

```java
QueryCollectionDataRequest request = new QueryCollectionDataRequest(); request.setDBInstanceId("gp-bp1c62r3l489****"); request.setCollection("document"); request.setNamespace("vector_test"); request.setNamespacePassword("vector_test_password"); request.setContent("Test"); request.setFilter("pv > 10"); request.setTopK(10L); request.setVector(Arrays.asList(0.7152607422256894,0.5524872066437732,0.1168505269851303, 704130971473022,0.4118874999967596,0.2451574619214022,0.18193414783144812,0.3050522957905 1,0.24846180714868163,0.0549715380856951)); request.setRegionId("ap-southeast-1"); QueryCollectionDataResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response));
```

Sample result: `{`

```json
  "Matches": {
    "match": [
```

`{`

```json
        "Id": "0CB55798-ECF5-4064-B81E-FE35B19E01A6",
        "Metadata": {
          "title":"Test document",
          "content":"Test content",
          "link":"http://127.0.0.1/document1",
          "pv":"1000"
```

`},`

```json
        "Values": [
           0.2894745251078251,
           0.5364747050266715,
           0.1276845661831275,
           0.22528871956822372,
           0.7009319238651552,
           0.40267406135256123,
           0.8873626696379067,
           0.1248525955774931,
           0.9115507046412368,
           0.2450859133174706
```

`]` `}` `]` `},`

```json
  "RequestId": "ABB39CC3-4488-4857-905D-2E4A051D0521",
  "Status": "success"
```

`}`

**References**

向量检索 Perform vector search

###### Go

The AnalyticDB for PostgreSQL API encapsulates the vector-related DDL and DML operations of AnalyticDB for PostgreSQL. You can use API operations to manage vector data. This topic describes how to use API operations to import and query vector data by calling Alibaba Cloud SDK for Go.

**Prerequisites**

An instance that uses elastic storage mode has been created. Vector search engine optimization has been enabled. A privileged account has been created. If you use a Resource Access Management (RAM) user, the required permissions must be granted to the RAM user. For more information, see Python SDK examples.

**Procedure**

1. Initialize the vector database.
2. Create a namespace.
3. Create a collection.
4. Upload vector data.
5. Retrieve vector data.

**Initialize the vector database**

Before you use vector search, you must initialize the knowledgebase database and the fulltext search feature. The following sample code provides an example on how to 调用call an API operation:

```java
package main import (
 "fmt"
 "os"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 gpdb "github.com/aliyun/alibaba-cloud-sdk-go/services/gpdb"
```

`)`

```
func main() {
 config := sdk.NewConfig()
 // Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBAB
A_CLOUD_ACCESS_KEY_SECRET are set.
 credential :=
credentials.NewAccessKeyCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv( "ALIBABA_CLOUD_ACCESS_KEY_SECRET"))
 /* use STS Token
 credential :=
credentials.NewStsTokenCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.Getenv("ALIBABA_CLOUD_SECURITY_TOKEN"))
```

`*/`

```
    client, err := gpdb.NewClientWithOptions("cn-qingdao", config, credential)
 if err != nil {
  panic(err)
```

`}`

```
 request := gpdb.CreateInitVectorDatabaseRequest()
 request.Scheme = "https"
 request.DBInstanceId = "gp-bp1c62r3l489****"
  request.RegionId = "cn-qingdao"
 request.ManagerAccount = "myaccount"
 request.ManagerAccountPassword = "myaccount_password"
 response, err := client.InitVectorDatabase(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}` For information about the relevant parameters, see InitVectorDatabase.

**Create a namespace**

Namespaces are used to separate schemas. Before you use vectors, you must create at least one namespace or use the public namespace. The following sample code provides an example on how to 调用call an API operation:

```java
package main import (
 "fmt"
 "os"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 gpdb "github.com/aliyun/alibaba-cloud-sdk-go/services/gpdb"
```

`)`

```
func main() {
 config := sdk.NewConfig()
 // Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBAB
A_CLOUD_ACCESS_KEY_SECRET are set.
 credential :=
credentials.NewAccessKeyCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv( "ALIBABA_CLOUD_ACCESS_KEY_SECRET"))
 /* use STS Token
 credential :=
credentials.NewStsTokenCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.Getenv("ALIBABA_CLOUD_SECURITY_TOKEN"))
```

`*/`

```
    client, err := gpdb.NewClientWithOptions("cn-qingdao", config, credential)
 if err != nil {
  panic(err)
```

`}`

```
 request := gpdb.CreateCreateNamespaceRequest()
 request.Scheme = "https"
 request.DBInstanceId = "gp-bp1c62r3l489****"
  request.RegionId = "cn-qingdao"
 request.ManagerAccount = "myaccount"
 request.ManagerAccountPassword = "myaccount_password"
 request.Namespace = "vector_test"
 request.NamespacePassword = "vector_test_password"
 response, err := client.CreateNamespace(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}` For information about the relevant parameters, see CreateNamespace. After you create a namespace, you can query the corresponding schema in the knowledgebase database of the instance.

```
SELECT schema_name FROM information_schema.schemata;
```

**Create a collection**

Collections are used to store vector data and are separated by namespaces. The following sample code provides an example on how to 调用call an API operation:

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 gpdb "github.com/aliyun/alibaba-cloud-sdk-go/services/gpdb"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
 config := sdk.NewConfig()
 // Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBAB
A_CLOUD_ACCESS_KEY_SECRET are set.
 credential :=
credentials.NewAccessKeyCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv( "ALIBABA_CLOUD_ACCESS_KEY_SECRET"))
 /* use STS Token
 credential :=
credentials.NewStsTokenCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.Getenv("ALIBABA_CLOUD_SECURITY_TOKEN"))
```

`*/`

```
 client, err := gpdb.NewClientWithOptions("cn-qingdao", config, credential)
 if err != nil {
  panic(err)
```

`}`

```
 request := gpdb.CreateCreateCollectionRequest()
 request.Scheme = "https"
 request.DBInstanceId = "gp-bp1c62r3l489****"
  request.RegionId = "cn-qingdao"
 request.ManagerAccount = "myaccount"
 request.ManagerAccountPassword = "myaccount_password"
 request.Namespace = "vector_test"
 request.Collection = "document"
 request.Dimension = requests.NewInteger(10)
```

```
 request.FullTextRetrievalFields = ","
 request.Parser = "zh_ch"
 request.Metadata = "{\"pv\": \"text\",\"link\": \"text\",\"content\":
\"text\",\"title\": \"text\"}"
 response, err := client.CreateCollection(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}` After you create a collection, you can query the corresponding table in the knowledgebase database of the instance.

```
SELECT tablename FROM pg_tables WHERE schemaname='vector_test';
```

**Upload vector data**

Upload the prepared embedding vector data to the corresponding collection. The following sample code provides an example on how to 调用call an API operation:

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 gpdb "github.com/aliyun/alibaba-cloud-sdk-go/services/gpdb"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
 config := sdk.NewConfig()
 // Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBAB
A_CLOUD_ACCESS_KEY_SECRET are set.
 credential :=
credentials.NewAccessKeyCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv( "ALIBABA_CLOUD_ACCESS_KEY_SECRET"))
 /* use STS Token
 credential :=
credentials.NewStsTokenCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.Getenv("ALIBABA_CLOUD_SECURITY_TOKEN"))
```

`*/`

```
 client, err := gpdb.NewClientWithOptions("cn-qingdao", config, credential)
 if err != nil {
  panic(err)
```

`}`

```
 request := gpdb.CreateUpsertCollectionDataRequest()
 request.Scheme = "https"
 request.DBInstanceId = "gp-bp1c62r3l489****"
  request.RegionId = "cn-qingdao"
 request.Collection = "document"
 request.Namespace = "vector_test"
 request.NamespacePassword = "vector_test_password"
 request.Rows = &[]gpdb.UpsertCollectionDataRows{
```

`{`

```
   Id: "0CB55798-ECF5-4064-B81E-FE35B19E01A6",
   Metadata: gpdb.UpsertCollectionDataRowsMetadata{
    Pv: "1000",
    Link: "http://127.X.X.1/document1",
    Content: "Test content",
    Title: "Test document",
```

`},`

```
   Vector: &
[]number{requests.NewInteger(0.2894745251078251),requests.NewInteger(0.5364747050266715), quests.NewInteger(0.1276845661831275)},
```

`},` `}`

```
 response, err := client.UpsertCollectionData(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}` For information about the relevant parameters, see UpsertCollectionData. After you upload vector data, you can query the data in the knowledgebase database of the instance.

```
SELECT * FROM vector_test.document;
```

**Retrieve vector data**

Use the prepared vectors or full-text search fields to retrieve vector data. The following sample code provides an example on how to 调用call an API operation:

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 gpdb "github.com/aliyun/alibaba-cloud-sdk-go/services/gpdb"
```

```
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
 config := sdk.NewConfig()
 // Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBAB
A_CLOUD_ACCESS_KEY_SECRET are set.
 credential :=
credentials.NewAccessKeyCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv( "ALIBABA_CLOUD_ACCESS_KEY_SECRET"))
 /* use STS Token
 credential :=
credentials.NewStsTokenCredential(os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.Getenv("ALIBABA_CLOUD_SECURITY_TOKEN"))
```

`*/`

```
 client, err := gpdb.NewClientWithOptions("cn-qingdao", config, credential)
 if err != nil {
  panic(err)
```

`}`

```
 request := gpdb.CreateQueryCollectionDataRequest()
 request.Scheme = "https"
 request.DBInstanceId = "gp-bp1c62r3l489****"
  request.RegionId = "cn-qingdao"
 request.Collection = "document"
 request.Namespace = "vector_test"
 request.NamespacePassword = "vector_test_password"
 request.Content = "Test"
 request.Filter = "pv > 10"
 request.TopK = requests.NewInteger(10)
 request.Vector = &
[]number{requests.NewInteger(0.7152607422256894),requests.NewInteger(0.5524872066437732), quests.NewInteger(0.1168505269851303)}
 response, err := client.QueryCollectionData(request)
 if err != nil {
  fmt.Print(err.Error())
```

`}`

```
 fmt.Printf("response is %#v\n", response)
```

`}` Sample result: `{`

```json
    "Matches": {
        "match": [{
            "Id": "0CB55798-ECF5-4064-B81E-FE35B19E01A6",
            "Metadata": {
                "title": "Test document",
                "content": "Test content",
                "link": "http://127.X.X.1/document1",
                "pv": "1000"
```

`},`

```json
            "Values": [0.2894745251078251, 0.5364747050266715, 0.1276845661831275,
0.22528871956822372, 0.7009319238651552, 0.40267406135256123, 0.8873626696379067, 0.124 8525955774931, 0.9115507046412368, 0.2450859133174706]
```

`}]` `},`

```json
    "RequestId": "ABB39CC3-4488-4857-905D-2E4A051D0521",
    "Status": "success"
```

`}`

###### Python 3

The AnalyticDB for PostgreSQL API encapsulates the vector-related DDL and DML operations of AnalyticDB for PostgreSQL. You can use API operations to manage vector data. This topic describes how to use API operations to import and query vector data by calling AnalyticDB for PostgreSQL SDK for Python 3.

**Prerequisites**

An instance that uses elastic storage mode has been created. Vector search engine optimization has been enabled. A privileged account has been created. If you use a Resource Access Management (RAM) user, the required permissions must be granted to the RAM user. For more information, see Python SDK examples.

**Procedure**

1. Install AnalyticDB for PostgreSQL SDK for Python 3.
2. Initialize the client.
3. Initialize the vector database.
4. Create a namespace.
5. Create a collection.
6. Upload vector data.
7. Retrieve vector data.

**Install AnalyticDB for PostgreSQL SDK for Python 3**

If you do not specify an SDK version, the latest version of AnalyticDB for PostgreSQL SDK for Python 3 is automatically installed. Sample code:

```
pip install alibabacloud_gpdb20160503 pip install alibabacloud_tea_openapi
```

You can install a specific version of AnalyticDB for PostgreSQL SDK for Python 3. In this

|   | alibabacloud gpdb20160503 _ |
|---|---|
| alibabacloud tea openapi _ _ |   |

```
pip install alibabacloud_gpdb20160503==3.5.0 pip install alibabacloud_tea_openapi==0.3.8
```

**Initialize the client**

Initialize the client that is used to access the AnalyticDB for PostgreSQL API. Sample code:

```java
from alibabacloud_tea_openapi import models as open_api_models from alibabacloud_gpdb20160503.client import Client import os ALIBABA_CLOUD_ACCESS_KEY_ID = os.environ['ALIBABA_ACCESS_KEY_ID'] ALIBABA_CLOUD_ACCESS_KEY_SECRET = os.environ['ALIBABA_ACCESS_KEY_SECRET'] ADBPG_INSTANCE_ID = os.environ['ADBPG_INSTANCE_ID'] ADBPG_INSTANCE_REGION = os.environ['ADBPG_INSTANCE_REGION'] def get_client():
    config = open_api_models.Config(
        access_key_id=ALIBABA_CLOUD_ACCESS_KEY_ID,
        access_key_secret=ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

`)`

```
    config.region_id = ADBPG_INSTANCE_REGION
    return Client(config)
```

Environment variables: ALIBABA_ACCESS_KEY_ID: the AccessKey ID that is used to access the AnalyticDB for PostgreSQL API. ALIBABA_ACCESS_KEY_SECRET: the AccessKey secret that is used to access the AnalyticDB for PostgreSQL API. ADBPG_INSTANCE_ID: the ID of the AnalyticDB for PostgreSQL instance. ADBPG_INSTANCE_REGION: the region of the AnalyticDB for PostgreSQL instance.

**Initialize the vector database**

Before you use vector search, you must initialize the knowledgebase database and the fulltext search feature. The following sample code provides an example on how to call an API operation:

```python
from alibabacloud_gpdb20160503 import models as gpdb_20160503_models def init_vector_database(account, account_password):
    request = gpdb_20160503_models.InitVectorDatabaseRequest(
        region_id=ADBPG_INSTANCE_REGION,
        dbinstance_id=ADBPG_INSTANCE_ID,
        manager_account=account,
        manager_account_password=account_password
```

`)`

```python
    response = get_client().init_vector_database(request)
    print(f"init_vector_database response code: {response.status_code}, body:
{response.body}") if __name__ == '__main__':
    init_vector_database("testacc", "Test1234")
# output: body:
# {
#    "Message":"success",
#    "RequestId":"FC1E0318-E785-1F21-A33C-FE4B0301B608",
#    "Status":"success"
# }
```

For information about the relevant parameters, see InitVectorDatabase.

**Create a namespace**

Namespaces are used to separate schemas. Before you use vectors, you must create at least one namespace or use the public namespace. The following sample code provides an example on how to call an API operation:

```python
def create_namespace(account, account_password, namespace, namespace_password):
    request = gpdb_20160503_models.CreateNamespaceRequest(
        region_id=ADBPG_INSTANCE_REGION,
        dbinstance_id=ADBPG_INSTANCE_ID,
        manager_account=account,
        manager_account_password=account_password,
        namespace=namespace,
        namespace_password=namespace_password
```

`)`

```python
    response = get_client().create_namespace(request)
    print(f"create_namespace response code: {response.status_code}, body:
{response.body}") if __name__ == '__main__':
    create_namespace("testacc", "Test1234", "ns1", "Ns1password")
# output: body:
# {
#    "Message":"success",
#    "RequestId":"78356FC9-1920-1E09-BB7B-CCB6BD267124",
#    "Status":"success"
# }
```

For information about the relevant parameters, see CreateNamespace. After you create a namespace, you can query the corresponding schema in the knowledgebase database of the instance.

```
SELECT schema_name FROM information_schema.schemata;
```

**Create a collection**

Collections are used to store vector data and are separated by namespaces. The following sample code provides an example on how to call an API operation:

```python
def create_collection(account,
                      account_password,
                      namespace,
                      collection,
                      metadata: str = None,
                      full_text_retrieval_fields: str = None,
                      parser: str = None,
                      embedding_model: str = None,
                      dimension: int = None,
                      metrics: str = None,
                      hnsw_m: int = None,
                      pq_enable: int = None,
                      external_storage: int = None,):
    request = gpdb_20160503_models.CreateCollectionRequest(
        region_id=ADBPG_INSTANCE_REGION,
        dbinstance_id=ADBPG_INSTANCE_ID,
        manager_account=account,
        manager_account_password=account_password,
        namespace=namespace,
        collection=collection,
        metadata=metadata,
        full_text_retrieval_fields=full_text_retrieval_fields,
        parser=parser,
        dimension=dimension,
        metrics=metrics,
        hnsw_m=hnsw_m,
        pq_enable=pq_enable,
        external_storage=external_storage
```

`)`

```python
    response = get_client().create_collection(request)
    print(f"create_collection response code: {response.status_code}, body:
{response.body}") if __name__ == '__main__':
    metadata = '{"title":"text", "content": "text", "page":"int"}'
    full_text_retrieval_fields = "title,content"
    dimension = 8
    create_collection("testacc", "Test1234", "ns1", "dc1",
                               metadata=metadata,
full_text_retrieval_fields=full_text_retrieval_fields,
                               dimension=dimension)
# output: body:
# {
#    "Message":"success",
#    "RequestId":"7BC35B66-5F49-1E79-A153-8D26576C4A3E",
#    "Status":"success"
# }
```

After you create a collection, you can query the corresponding table in the knowledgebase database of the instance.

```
SELECT tablename FROM pg_tables WHERE schemaname='vector_test';
```

**Upload vector data**

Upload the prepared embedding vector data to the corresponding collection. The following sample code provides an example on how to call an API operation:

```python
def upsert_collection_data(namespace,
                           namespace_password,
                           collection,
                           rows):
    request = gpdb_20160503_models.UpsertCollectionDataRequest(
        region_id=ADBPG_INSTANCE_REGION,
        dbinstance_id=ADBPG_INSTANCE_ID,
        namespace=namespace,
        namespace_password=namespace_password,
        collection=collection,
        rows=rows,
```

`)`

```json
    response = get_client().upsert_collection_data(request)
    print(f"upsert_collection_data response code: {response.status_code}, body:
{response.body}") if __name__ == '__main__':
    rows = []
    rows.append(gpdb_20160503_models.UpsertCollectionDataRequestRows(
        id="0CB55798-ECF5-4064-B81E-FE35B19E01A6",
        metadata={
            "page": 1,
            "content": "Test content",
            "title": "Test document"
```

`},`

```
        vector=[0.2894745251078251, 0.5364747050266715, 0.14858841010401188,
0.42140750105351877,
                0.5780346820809248, 0.1145475372279496, 0.04329004329004329, 0.432467964
93549741]
```

`))`

```bash
    upsert_collection_data("ns1", "Ns1password", "dc1", rows)
# output: body:
# {
#    "Message":"success",
#    "RequestId":"8FEE5D1E-ECE8-1F2F-A17F-48039125CDC3",
#    "Status":"success"
# }
```

For information about the relevant parameters, see UpsertCollectionData. After you upload vector data, you can query the data in the knowledgebase database of the instance.

```
SELECT * FROM vector_test.document;
```

**Retrieve vector data**

Use the prepared vectors or full-text search fields to retrieve vector data. The following sample code provides an example on how to call an API operation:

```python
from typing import List def query_collection_data(namespace,
                          namespace_password,
                          collection,
                          top_k,
                          content: str = None,
                          filter_str: str = None,
                          include_values: bool = None,
                          metrics: str = None,
                          vector: List[float] = None):
    request = gpdb_20160503_models.QueryCollectionDataRequest(
        region_id=ADBPG_INSTANCE_REGION,
        dbinstance_id=ADBPG_INSTANCE_ID,
        namespace=namespace,
        namespace_password=namespace_password,
        collection=collection,
        top_k=top_k,
        content=content,
        filter=filter_str,
        include_values=include_values,
        metrics=metrics,
        vector=vector,
```

`)`

```python
    response = get_client().query_collection_data(request)
    print(f"query_collection_data response code: {response.status_code}, body:
{response.body}") if __name__ == '__main__':
    content = "test query"
    vector = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    query_collection_data("ns1", "Ns1password", "dc1", 5, content=content,
vector=vector)
# output:
# query_collection_data response code: 200, body:{'Matches': {'match': [{'Id': '0CB5579
8-ECF5-4064-B81E-FE35B19E01A6', 'Metadata': {'source': 1, 'page': '1', 'title': 'Test d ocument', 'content': 'Test content'}, 'Score': 0.7208109110736349, 'Values': {'value': [0.28947452, 0.5364747, 0.1485884, 0.4214075, 0.5780347, 0.114547536, 0.043290045, 0.7] }}]}, 'RequestId': '709E2C82-FE25-1722-9DBB-00AD0F85ABBB', 'Status': 'success'}
```

#### Create a vector table

This topic describes how to create a vector table. The used syntax is fully compatible with SQL:1999 and partially compatible with SQL:2003.

**Prerequisites**

Vector search engine optimization is enabled. For more information, see Enable or disable vector search engine optimization.

**Syntax**

The syntax for creating a vector table is the same as the syntax for creating a heap table in AnalyticDB for PostgreSQL. The vector column (VECTORTYPE) in the table is represented by an array and supports the following types: `SMALLINT[]` , `FLOAT2[]` , and `REAL(FLOAT4)[]` . A table supports multiple vector columns.

```
CREATE TABLE [TABLE_NAME]
```

`(`

```
    C1 DATATYPE,
    C2 DATATYPE,
    ......,
    CN VECTORTYPE,
    PRIMARY KEY (one or more columns)
) DISTRIBUTED BY (C1);
```

**Examples**

Create a heap table named `FACE_TABLE` . `C1` is the primary key column, and `C2` is the vector column.

```
CREATE TABLE FACE_TABLE (
    C1 INT,
    C2 REAL[] NOT NULL,
    C3 TIMESTAMP NOT NULL,
    C4 VARCHAR(20) NOT NULL,
    PRIMARY KEY (C1)
) DISTRIBUTED BY (C1);
```

#### Create a vector index

In search scenarios that involve large amounts of data or require fast data access, such as database query optimization, machine learning, data mining, image and video search, and spatial data query, you can create vector indexes to accelerate vector search. This way, you can accelerate data analysis, optimize search jobs, and improve the query performance and response efficiency of the system.

**Background information**

AnalyticDB for PostgreSQL vector databases use the FastANN vector search engine to implement the mainstream Hierarchical Navigable Small World (HNSW) algorithm. The FastANN vector search engine uses the segmented paging storage of PostgreSQL and stores only the vector column pointers in indexes to significantly reduce the storage that is occupied by vector indexes. The vector search engine uses the product quantization (PQ) feature to reduce the dimensionality of high-dimensional vectors. This way, low-dimensional vectors are stored in indexes to reduce index lookups when you insert or query vectors and improve vector search performance.

**Syntax**

```
CREATE INDEX [INDEX_NAME] ON [SCHEMA_NAME].[TABLE_NAME] USING ANN(COLUMN_NAME) WITH (DIM=<DIMENSION>,
      DISTANCEMEASURE=<MEASURE>,
      HNSW_M=<M>,
      HNSW_EF_CONSTRUCTION=<EF_CONSTURCTION>,
      PQ_ENABLE=<PQ_ENABLE>,
      PQ_SEGMENTS=<PQ_SEGMENTS>,
      PQ_CENTERS=<PQ_CENTERS>,
      EXTERNAL_STORAGE=<EXTERNAL_STORAGE>);
```

Parameters: INDEX_NAME: the name of the index. SCHEMA_NAME: the name of the schema or namespace. TABLE_NAME: the name of the table. COLUMN_NAME: the name of the vector index column. The following table describes other vector index parameters.

| Vector index parameter | Requi red | Description | Defa ult | Value range |
|---|---|---|---|---|
| DIM | Yes | The number of vector dimensions. This parameter is used to check vectors when vectors are inserted. If the number of vector dimensions does not match, the system displays an error message. | 0 | [1, 8192] |
|   |   | The distance or similarity measurement. Valid values: L2: uses the squared Euclidean distance function to create indexes. This measurement is suitable for image similarity search scenarios. Formula: |   |   |

|   |   | IP: uses the negative inner product distance function to create indexes. This measurement is used to replace cosine similarity after vector normalization. Formula: |   |   |
|---|---|---|---|---|
| DISTANCEMEASURE | No | COSINE: uses the cosine distance function to create indexes. This measurement is suitable for text similarity search scenarios. Formula: Note If you set the DISTANCEMEASURE parameter to IP or COSINE, make sure that the minor version of the AnalyticDB for PostgreSQL instance is 6.3.10.18 or later. For information about how to view and update the minor version, see Update the minor version of an instance. To achieve the best performance, we recommend that you store the normalized vector data in databases and use the inner product distance measurement to create indexes. When you use the inner product distance measure to create indexes, you can also query the Euclidean distance and cosine similarity. For more information, see Perform vector search. For information about user- defined functions (UDFs) for vector search, see the "References" section of this topic. | L2 | (L2, IP, COSINE) |
| 3 |   | > Docu | ment Ver | sion: 2026082 |

| HNSW M _ | No | The maximum number of neighbors for the HNSW algorithm. | 32 | [10, 1000] |
|---|---|---|---|---|
| HNSW EF CONSTRUC _ _ TION | No | The size of the candidate set when the HNSW algorithm is used to create indexes. | 600 | [40, 4000] |
| PQ ENABLE _ | No | Specifies whether to enable the PQ feature for dimensionality reduction. The PQ feature uses existing vector sample data for training. If the number of rows of data is less than 500,000, we recommend that you do not specify this parameter. | 0 | [0, 1] |
| PQ SEGMENTS _ | No | The number of segments that are used in the K-means clustering algorithm after you enable the PQ feature. This parameter takes effect only if you set the PQ ENABLE parameter to 1. _ If the DIM parameter divided by eight is an integer, you do not need to specify this parameter. Otherwise, you must specify this parameter. The value of the PQ SEGMENTS _ parameter must be greater than 0. The DIM parameter divided by the PQ SEGMENTS parameter must be _ an integer. | 0 | [1, 256] |
| PQ CENTERS _ | No | The number of centroids that are used in the K-means clustering algorithm after you enable the PQ feature. This parameter takes effect only if you set the PQ ENABLE parameter to 1. _ | 2048 | [256, 8192] |

| EXTERNAL STORAGE _ | No | Specifies whether to use the memory mapping technology to create HNSW indexes. Valid values: 0: uses segmented paging storage to create indexes. This method uses the shared buffer of PostgreSQL for caching and supports the DELETE and UPDATE operations. 1: uses the memory mapping technology to create indexes. This method supports marked deletions of indexes and allows you to perform a small number of DELETE and UPDATE operations for AnalyticDB for PostgreSQL instances of V6.6.2.3 or later. | 0 | [0, 1] |
|---|---|---|---|---|

**Example**

In this example, a text knowledge base is used. An article in the knowledge base is split into chunks, converted into embedding vectors, and then stored in a database. The following table describes the fields that are contained in a table named chunks.

| Field | Data type | Description |
|---|---|---|
| id | SERIAL | The serial number. |
| chunk | VARCHAR(1024) | The text chunk. |
| intime | TIMESTAMP | The time when the article is stored in the database. |
| url | VARCHAR(1024) | The URL of the article to which the text chunk belongs. |
| feature | REAL[] | The embedding vector of the text chunk. |

1. Create a table to store vectors.

```
CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    chunk VARCHAR(1024),
    intime TIMESTAMP,
    url VARCHAR(1024),
    feature REAL[]
) DISTRIBUTED BY (id);
```

2. Set the storage mode of the vector column to **PLAIN** to reduce data scanning costs and
achieve higher performance.

```
ALTER TABLE chunks ALTER COLUMN feature SET STORAGE PLAIN;
```

3. Create a vector index for the vector column.

```
-- Create a vector index based on the Euclidean distance. CREATE INDEX idx_chunks_feature_l2 ON chunks USING ann(feature) WITH (dim=1536, dista ncemeasure=l2, hnsw_m=64, pq_enable=1); -- Create a vector index based on the inner product distance. CREATE INDEX idx_chunks_feature_ip ON chunks USING ann(feature) WITH (dim=1536, dista ncemeasure=ip, hnsw_m=64, pq_enable=1); -- Create a vector index based on the cosine similarity. CREATE INDEX idx_chunks_feature_cosine ON chunks USING ann(feature) WITH (dim=1536, d istancemeasure=cosine, hnsw_m=64, pq_enable=1);
```

**Note**

You can create multiple vector columns in each vector table and multiple vector indexes on each vector column. To avoid invalid indexes, you must create vector indexes based on your business requirements. The vector search methods must match the vector indexes that are created by using the corresponding distance measurements. For example, the `<->` operator works with the vector index created by using the Euclidean distance, the `<#>` operator works with the vector index created by using the inner product distance, and the `<=>` operator works with the vector index created by using the cosine similarity. If the operators do not work with the corresponding vector indexes, the vector search method is downgraded to exact search (bruteforce search). Use the `ANN` access method that is provided by the FastANN vector search extension. If you enable the **vector search engine optimization** feature for an AnalyticDB for PostgreSQL instance, the FastANN vector search extension is automatically created in the AnalyticDB for PostgreSQL instance.

|   | You must specify an operator class or define a default operator class |
|---|---|
| for the data type |   |

**optimization** feature is not enabled for the AnalyticDB for PostgreSQL instance.
In this case, enable the feature and try again. For more information, see Enable or disable vector search engine optimization.
4. Create an index for structured data columns to accelerate hybrid search.

```
CREATE INDEX ON chunks(intime);
```

**Index creation modes**

You can create vector indexes in one of the following modes: Streaming mode Create an empty table and then create a vector index for the table. This way, the streaming index is created in real time when you import vector data. This mode is suitable for realtime vector search scenarios. However, you cannot quickly import vector data in this mode. Asynchronous mode Create an empty table, import vector data to the table, and then create a vector index for the imported vector data. This mode is suitable for scenarios in which you want to import large amounts of vector data.

**Note**

AnalyticDB for PostgreSQL allows you to concurrently create vector indexes in asynchronous mode. You can use the Grand Unified Configuration (GUC) parameter
**fastann.build_parallel_processes** to specify the number of concurrent index creation
processes. For example, you can create an index in asynchronous mode by using Data Management (DMS). Sample code:

```
-- For example, an AnalyticDB for PostgreSQL instance whose compute node specifications are 8 cores and 32 GB memory is used. -- To prevent timeout errors, set the statement_timeout and idle_in_transaction_session_timeout parameters to 0. -- Set the fastann.build_parallel_processes parameter to 8 to ensure that the CPU resou rces of compute nodes are fully utilized. The value of the fastann.build_parallel_processes parameter must be the same as the number of CPU cores in the compute node specifications. -- In DMS, you must specify values for parameters in the same line as the index creatio n statement. SET statement_timeout = 0;SET idle_in_transaction_session_timeout = 0;SET fastann.build_parallel_processes = 8;CREATE INDEX ON chunks USING ann(feature) WITH (dim=1536, distancemeasure=cosine, hnsw_m=64, pq_enable=1);
```

You can create an index in asynchronous mode by using the psql tool. Sample code:

```
-- For example, an AnalyticDB for PostgreSQL instance whose compute node specifications are 8 cores and 32 GB memory is used. -- Step 1: Store the following content in the create_index.sql file: SET statement_timeout = 0; SET idle_in_transaction_session_timeout = 0; SET fastann.build_parallel_processes = 8; CREATE INDEX ON chunks USING ann(feature) WITH (dim=1536, distancemeasure=cosine, hnsw_ m=64, pq_enable=1); -- Step 2: Run the following command to create an index in parallel: psql -h gp-xxxx-master.gpdb.rds.aliyuncs.com -p 5432 -d dbname -U username -f create_in dex.sql
```

**Important**

If other services are running on the AnalyticDB for PostgreSQL instance, you cannot set the number of concurrent index creation processes to the number of CPU cores in the compute node specifications.

**References**

Supported vector functions

| 17 |   |   | > Documen | t Version: 2026082 |
|---|---|---|---|---|

| Purpose | Vector function | Data type of the return value | Description | Supported data type |
|---|---|---|---|---|
|   | l2 distance _ | DOUBLE PRECISION | Calculates the rooted Euclidean distance between two vectors. This function is used to measure the distance between two vectors and suitable for image similarity search scenarios. Important For AnalyticDB for PostgreSQL instances of V6.3.10.17 or earlier, the l2 distance _ function calculates the squared Euclidean distance. For AnalyticDB for PostgreSQL instances of V6.3.10.18 or later, the l2 distance _ function calculates the rooted Euclidean distance. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

|   | inner product dis _ _ tance | DOUBLE PRECISION | Calculates the inner product distance between two vectors, which is equivalent to cosine similarity after vector normalization. This function is used to replace cosine similarity after vector normalization. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|---|---|---|---|---|
|   | cosine similarity _ | DOUBLE PRECISION | Calculates the cosine similarity between two vectors. This function is used to measure the similarity between two vectors based on the direction regardless of the actual length of the vectors. Valid values of the cosine similarity: -1 to 1. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
| Calculation |   |   |   |   |
|   | dp distance _ | DOUBLE PRECISION | Calculates the dot product distance, which is the same as the inner product distance. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

|   | hm distance _ | INTEGER | Calculates the Hamming distance, which is the number of bit positions at which the corresponding bits in the two binary strings are different. | INT[] |
|---|---|---|---|---|
|   | vector add _ | SMALLINT[], FLOAT2[], or FLOAT4[] | Calculates the sum of two vector arrays. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | vector sub _ | SMALLINT[], FLOAT2[], or FLOAT4[] | Calculates the difference between two vector arrays. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | vector mul _ | SMALLINT[], FLOAT2[], or FLOAT4[] | Calculates the product of two vector arrays. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | vector div _ | SMALLINT[], FLOAT2[], or FLOAT4[] | Calculates the quotient of two vector arrays. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | vector sum _ | INT or DOUBLE PRECISION | Calculates the sum of all elements in a vector array. | SMALLINT[], INT[], FLOAT2[], FLOAT4[], REAL[], and FLOAT8[] |
|   | vector min _ | INT or DOUBLE PRECISION | Calculate the minimum value among all elements in a vector array. | SMALLINT[], INT[], FLOAT2[], FLOAT4[], REAL[], and FLOAT8[] |

|   | vector max _ | INT or DOUBLE PRECISION | Calculates the maximum value among all elements in a vector array. | SMALLINT[], INT[], FLOAT2[], FLOAT4[], REAL[], and FLOAT8[] |
|---|---|---|---|---|
|   | vector avg _ | INT or DOUBLE PRECISION | Calculates the average value of all elements in a vector array. | SMALLINT[], INT[], FLOAT2[], FLOAT4[], REAL[], and FLOAT8[] |
|   | vector norm _ | DOUBLE PRECISION | Calculates the norm of a vector array. | SMALLINT[], INT[], FLOAT2[], FLOAT4[], REAL[], and FLOAT8[] |
|   | vector angle _ | DOUBLE PRECISION | Calculates the angle between two vector arrays. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | l2 squared dista _ _ nce | DOUBLE PRECISION | Sorts vectors based on the squared Euclidean distance. This function requires fewer calculations than the sorting method based on the rooted Euclidean distance. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

| Sorting |   |   |   |   |
|---|---|---|---|---|
|   | negative inner p _ _ roduct distance _ | DOUBLE PRECISION | Sorts vectors based on the negative inner product distance. This function is used to sort vectors based on the inner product distance in descending order. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|   | cosine distance _ | DOUBLE PRECISION | Sorts vectors based on the cosine distance. This function is used to sort vectors based on the cosine similarity in descending order. Valid values of the cosine distance: 0 to 2. Formula: | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

**Important**

Only AnalyticDB for PostgreSQL instances of V6.6.1.0 or later support the following vector functions: vector_add, vector_sub, vector_mul, vector_div, vector_sum, vector_min, vector_max, vector_avg, vector_norm, and vector_angle. For information about how to view the minor version of an AnalyticDB for PostgreSQL instance, see View the minor version of an instance. Examples of vector functions:

```
-- Euclidean distance SELECT l2_distance(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Inner product distance SELECT inner_product_distance(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Cosine similarity SELECT cosine_similarity(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Dot product distance SELECT dp_distance(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Hamming distance SELECT hm_distance(array[1,0,1,0]::int[], array[0,1,0,1]::int[]); -- Sum of two vector arrays SELECT vector_add(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Difference between two vector arrays SELECT vector_sub(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Product of two vector arrays SELECT vector_mul(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Quotient of two vector arrays SELECT vector_div(array[1,1,1,1]::real[], array[2,2,2,2]::real[]); -- Sum of all elements in a vector array SELECT vector_sum(array[1,1,1,1]::real[]); -- Minimum value among all elements in a vector array SELECT vector_min(array[1,1,1,1]::real[]); -- Maximum value among all elements in a vector array SELECT vector_max(array[1,1,1,1]::real[]); -- Average value of all elements in a vector array SELECT vector_avg(array[1,1,1,1]::real[]); -- Norm of a vector array SELECT vector_norm(array[1,1,1,1]::real[]); -- Angle between two vector arrays SELECT vector_angle(array[1,1,1,1]::real[], array[2,2,2,2]::real[]);
```

Supported vector operators

| Vector operator | Calculation | Sorting | Supported data type |
|---|---|---|---|
| <-> | Calculates the squared Euclidean distance between two vectors. The result is equivalent to the result of the l2 squared distance _ _ function. | Sorts vectors based on the squared Euclidean distance in ascending order. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

| <#> | Calculates the negative inner product distance between two vectors. The result is equivalent to the result of the negative inner produc _ _ t distance function. _ | Sorts vectors based on the dot product distance in descending order. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
|---|---|---|---|
| <=> | Calculates the cosine distance between two vectors. The result is equivalent to the result of the cosine distance _ function. | Sorts vectors based on the cosine similarity in descending order. | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
| + | Calculates the sum of two vectors. | None | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
| - | Calculates the difference between two vectors. | None | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
| * | Calculates the product of two vectors. | None | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |
| / | Calculates the quotient of two vectors. | None | SMALLINT[], FLOAT2[], FLOAT4[], and REAL[] |

**Important**

Only AnalyticDB for PostgreSQL instances of V6.6.1.0 or later support the following vector operators: `+` , `-` , `*` , and `/` . For information about how to view the minor version of an AnalyticDB for PostgreSQL instance, see View the minor version of an instance. Examples of vector operators:

```
-- Euclidean distance SELECT array[1,1,1,1]::real[] <-> array[2,2,2,2]::real[] AS score; -- Inner product distance SELECT array[1,1,1,1]::real[] <#> array[2,2,2,2]::real[] AS score; -- Cosine distance SELECT array[1,1,1,1]::real[] <=> array[2,2,2,2]::real[] AS score; -- Sum of two vectors SELECT array[1,1,1,1]::real[] + array[2,2,2,2]::real[] AS value; -- Difference between two vectors SELECT array[1,1,1,1]::real[] - array[2,2,2,2]::real[] AS value; -- Product of two vectors SELECT array[1,1,1,1]::real[] * array[2,2,2,2]::real[] AS value; -- Quotient of two vectors SELECT array[1,1,1,1]::real[] / array[2,2,2,2]::real[] AS value;
```

#### Import vector data

AnalyticDB for PostgreSQL uses standard SQL for all vector write operations. Use INSERT for small batches during development or incremental ingestion, and COPY for bulk loading large datasets.

**Insert rows**

Use the INSERT statement to add individual rows or small batches to a vector table. Vector columns accept two equivalent formats:

```
-- ARRAY[] format INSERT INTO chunks VALUES (default, 'xxx', '2023-05-04', 'aaa.bbb.ccc/xxx.pdf', ARRAY[0.1, 0.2, 0.1, 0.3, ... 0.9]::real[]); -- {} format INSERT INTO chunks VALUES (default, 'xxx', '2023-05-04', 'aaa.bbb.ccc/xxx.pdf', '{0.1, 0.2, 0.1, 0.3, ... 0.9}');
```

Both formats produce identical results and can be used interchangeably.

**Load data in bulk**

For large datasets, use COPY instead of INSERT. COPY bypasses row-by-row processing and loads data significantly faster.

```
COPY chunks (id, content, created_at, source, embedding) FROM '/path/to/data.csv' WITH (FORMAT CSV, HEADER true);
```

**What's next**

Create a vector index Query vector data

#### Perform vector search

AnalyticDB for PostgreSQL provides the exact search method that compares the distance or similarity between all vectors and the approximate index search method that uses Hierarchical Navigable Small World (HNSW) indexes. The approximate index search method returns results faster than the exact search method.

**Exact search**

The exact search method is a brute-force search method that compares the distance or similarity between all vectors. This method results in low response speeds but can achieve a 100% recall rate. You can perform exact search based on the Euclidean distance, inner product distance, or cosine similarity. Euclidean distance

```
SELECT ID, l2_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) as score FRO M <TABLE_NAME> ORDER BY l2_squared_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) LIMIT <TOPK>;
```

Inner product distance

```
SELECT ID, inner_product_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) a s score FROM <TABLE_NAME> ORDER BY negative_inner_product_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) LIM IT <TOPK>;
```

Cosine similarity

```
SELECT ID, cosine_similarity(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) as sco re FROM <TABLE_NAME> ORDER BY cosine_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) LIMIT <TOPK>;
```

Parameters: score: the Euclidean distance, inner product distance, or cosine similarity. Vectors are sorted by Euclidean distance in ascending order, or by inner product distance or cosine similarity in descending order. <VECTOR_COLUMN_NAME>: the name of the vector column. <TABLE_NAME>: the name of the vector table. <TOPK>: the number of top result sets.

**Approximate index search**

The approximate index search method uses HNSW indexes to search data. This method works fast but returns approximate results at a recall rate of more than 99%.

**Syntax**

You can perform approximate index search based on the Euclidean distance, inner product distance, or cosine similarity.

**Note**

Only AnalyticDB for PostgreSQL instances of V6.3.10.18 or later support approximate index search based on the inner product distance or cosine similarity. Make sure that the minor version of your AnalyticDB for PostgreSQL instance is V6.3.10.18 or later. For information about how to view and update the minor version, see Update the minor engine version. Euclidean distance

```
SELECT ID, l2_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) as score FRO M <TABLE_NAME> ORDER BY <VECTOR_COLUMN_NAME> <-> array[1,2,3...N]::float4[] LIMIT <TO PK>;
```

Inner product distance

```
SELECT ID, inner_product_distance(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) a s score FROM <TABLE_NAME> ORDER BY <VECTOR_COLUMN_NAME> <#> array[1,2,3...N]::float4[] LIMIT <TOPK>;
```

Cosine similarity

```
SELECT ID, cosine_similarity(<VECTOR_COLUMN_NAME>, array[1,2,3...N]::float4[]) as sco re FROM <TABLE_NAME> ORDER BY <VECTOR_COLUMN_NAME> <=> array[1,2,3...N]::float4[] LIM IT <TOPK>;
```

**Note**

The parameter descriptions in approximate index search are the same as those in exact search. If no indexes are created or no parameters are configured for the FastANN vector search engine, the approximate index search is downgraded to exact search. When you use a vector index, you must specify or omit **ASC** in the **ORDER BY** clause. To sort vectors by distance in descending order, or to sort the results of vector index search by using another column, specify the vector index search as a subquery and add an **ORDER BY** clause to the parent query. When you use a vector index, you must specify an operator such as `<->` , `<#>` , or `<=>` in the ORDER BY clause. In addition, the `<->` , `<#>` , or `<=>` operator must work with a vector index that is created by using the corresponding distance measurement. This way, you can use the vector index to accelerate queries. For information about the supported operators and how to use the operators, see Create a vector index.

**Examples**

In this example, a text knowledge base is used. You can use the vector index search method to search for the source articles of a text. Sample statement:

```
SELECT id, chunk, intime, url FROM chunks ORDER BY
    feature <=> array[10,2.0,..., 1536.0]::real[]
LIMIT 100;
```

You can execute an **EXPLAIN** statement to check the execution plan of the query. In the following sample execution plan, `Ann Index Scan` indicates that a vector index is used.

```
QUERY PLAN -------------------------------------------------
 Limit
   ->  Gather Motion 3:1  (slice1; segments: 3)
         Merge Key: ((feature <=> $0))
          ->  Limit
               ->  Ann Index Scan using feature_idx on chunks
                Order By: (feature <=> $0)
 Optimizer: Postgres query optimizer
```

If you want to search for the source articles of a text within the last month, you can use the integrated search method. Sample statement:

```
SELECT id, chunk, intime, url FROM chunks WHERE
    intime > '2023-04-01' AND intime <= '2023-05-01'
ORDER BY
    feature <=> array[10,2.0,..., 1536.0]::real[]
LIMIT 100;
```

**References**

**SQL optimization for vector search**

This section describes SQL optimization for vector search. After you create a vector table, you can create multiple vector indexes for a vector column based on your business requirements. The SQL statement and the involved index must match. For example, the `<->` operator can work with only indexes that are created by using the Euclidean distance, the `<#>` operator can work with only indexes that are created by using the inner product distance, and the `<=>` operator can work with only indexes that are created by using the cosine similarity.

```
CREATE TABLE test_table (
    id serial primary key,
    feature real[]
) distributed by (id); CREATE INDEX idx_test_table_feature_l2 ON test_table USING ann(feature) WITH (dim=768, distancemeasure=l2, hnsw_m=64, pq_enable=1); CREATE INDEX idx_test_table_feature_ip ON test_table USING ann(feature) WITH (dim=768, distancemeasure=ip, hnsw_m=64, pq_enable=1); CREATE INDEX idx_test_table_feature_cosine ON test_table USING ann(feature) WITH (dim=7 68, distancemeasure=cosine, hnsw_m=64, pq_enable=1);
```

If you do not want to return the score value of the vector distance, you can execute the following SQL statements to query vector data:

```
-- Search vector data based on the Euclidean distance. SELECT id FROM test_table ORDER BY feature <-> array[1,2,3 ... 768]::real[] LIMIT topk; -- Search vector data based on the inner product distance. SELECT id FROM test_table ORDER BY feature <#> array[1,2,3 ... 768]::real[] LIMIT topk; -- Search vector data based on the cosine similarity. SELECT id FROM test_table ORDER BY feature <=> array[1,2,3 ... 768]::real[] LIMIT topk;
```

If you want to return the score value of the vector distance, you can use the sort result of the vector index to calculate the actual score value of the vector distance. This avoids a complete vector distance calculation process and reduces the amount of time required for calculation. Sample statements:

```
-- Search vector data based on the Euclidean distance. SELECT t.id as id, sqrt(t.score) as score FROM
  (SELECT id, feature <-> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t;
-- Search vector data based on the inner product distance. SELECT t.id as id, (-1 * t.score) as score FROM
  (SELECT id, feature <#> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t;
-- Search vector data based on the cosine similarity. SELECT t.id as id, (1.0 - t.score) as score FROM
  (SELECT id, feature <=> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t;
```

If you want to return results that are filtered based on a score range, you can execute the following SQL statements to query vector data. The statements use the sort result of the vector index to calculate the final score value of the vector distance. This reduces the amount of time required for calculation.

```
-- Search vector data based on the Euclidean distance. SELECT t.id as id, sqrt(t.score) as score FROM
  (SELECT id, feature <-> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t
WHERE score < 100; -- Search vector data based on the inner product distance. SELECT t.id as id, (-1 * t.score) as score FROM
  (SELECT id, feature <#> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t
WHERE score > 10; -- Search vector data based on the cosine similarity. SELECT t.id as id, (1.0 - t.score) as score FROM
  (SELECT id, feature <=> array[1,2,3 ... 768]::real[] as score
   FROM test_table
   ORDER BY score LIMIT topk) t
WHERE score > 0.5;
```

**Engine parameters related to vector search**

| Engine parameter | Description | Defaul t value | Valid value |
|---|---|---|---|
| fastann.build parallel proc _ _ esses | The number of processes that are built in parallel by using vector indexes. The value of this parameter varies based on the database specifications. | 4 | [1, 64] |
| fastann.pq amp _ | The amplification factor of vector search result sets when product quantization (PQ) is used to reduce the dimensionality of high- dimensional vectors. You can use this parameter to test the recall rate. | 10 | [1, 1000] |
| fastann.hnsw max scan p _ _ _ oints | The maximum number of scan points when HNSW indexes are used for vector search. You can use this parameter to quickly end the search and test the recall rate. | 6000 | [1, 6000000] |
| fastann.hnsw ef search _ _ | The size of search candidate sets when HNSW indexes are used for vector search. You can use this parameter to test the recall rate. | 400 | [10, 10000] |

You can configure the preceding parameters for sessions.

#### Use the FLOAT2 data type to compress

**vector storage**

Vector workloads store high-dimensional arrays for every image, audio file, or text embedding processed. At scale, those arrays consume substantial disk space. AnalyticDB for PostgreSQL provides the FLOAT2 data type to store vector columns at half the space of FLOAT4, with minimal impact on search accuracy. Normalize vectors to the range [0, 1] before running vector search. Values outside the FLOAT2 range (-65519.99 to 65519.99) are stored as `Infinity` or `-Infinity` , which produces inaccurate distances.

**How FLOAT2 works**

FLOAT2 implements the IEEE 754 binary16 (half-precision) format. Each value occupies 2 bytes instead of the 4 bytes used by FLOAT4, giving a storage compression ratio of 0.5 for vector columns.

**Format layout**

| Field | Width |
|---|---|
| Sign bit | 1 bit |
| Exponent | 5 bits |
| Significand | 11 bits (10 explicitly stored) |

The 10-bit significand provides approximately 3.311 decimal digits of precision (log10(2¹¹) ≈ 3.311).

**Representative values**

```
0 01111 0000000000 = 1 0 01111 0000000001 = 1 + 2⁻¹⁰ = 1.0009765625 (smallest number greater than 1) 1 10000 0000000000 = -2 0 11110 1111111111 = 65504 (max half precision) 0 00001 0000000000 = 2⁻¹⁴ ≈ 6.10352 × 10⁻⁵ (smallest positive normal) 0 00000 1111111111 = 2⁻¹⁴ - 2⁻²⁴ ≈ 6.09756 × 10⁻⁵ (greatest subnormal) 0 00000 0000000001 = 2⁻²⁴ ≈ 5.96046 × 10⁻⁸ (smallest positive subnormal) 0 00000 0000000000 = 0 1 00000 0000000000 = -0 0 11111 0000000000 = infinity 1 11111 0000000000 = -infinity 0 01101 0101010101 = 0.333251953125 ≈ 1/3
```

1/3 rounds down due to the odd number of bits in the significand — the same behavior as double precision.

**FLOAT2 to FLOAT4 conversion**

The system converts between FLOAT2 and FLOAT4 by shifting bits and adjusting the exponent base (15 for FLOAT2, 127 for FLOAT4, a difference of 112). To convert from FLOAT2 to FLOAT4:
1. Shift the sign bit left by 16 bits.
2. Add 112 to the exponent base (15 to 127), then shift the exponent left by 13 bits.
3. Shift the significand left by 13 bits.
The inverse operations apply when converting from FLOAT4 to FLOAT2. Two conversion algorithms are available:

| Algorithm | Throughput |
|---|---|
| C program (software) | 1 element at a time |
| AVX + SSE2 (hardware) | 4 elements at a time |

Hardware-accelerated conversion requires Advanced Vector Extensions (AVX) and Streaming SIMD Extensions 2 (SSE2) on the host machine. Because vector search uses index traversal rather than full scans, only a small number of entries are converted per query.

**Precision and value range**

**Precision loss:** FLOAT2 storage introduces a small amount of precision loss acceptable for
vector search. For example, 1.3 is retrieved as 1.2998, and 5.6 is retrieved as 5.60156.
**Value range:** FLOAT2 accepts values from -65519.99 to 65519.99. Values above 65519 are
stored as `Infinity` ; values below -65519 are stored as `-Infinity` .
**Normalization requirement:** Normalize vectors to [0, 1] before vector search.
Unnormalized vectors can produce distances that exceed the FLOAT2 value range, leading to inaccurate results.

**Storage savings**

Each FLOAT2 vector element occupies 2 bytes, compared to 4 bytes for FLOAT4. A table with 10,000 rows of 1,024-dimensional vectors illustrates the difference:

```
-- Create comparison tables CREATE TABLE TAB1(A FLOAT4[]); CREATE TABLE TAB2(A FLOAT2[]); -- Insert 10,000 rows of 1,024-dimensional vectors INSERT INTO TAB1 SELECT GEN_RAND_F2_ARR(1, 1024) FROM GENERATE_SERIES(1, 10000); INSERT INTO TAB2 SELECT GEN_RAND_F2_ARR(1, 1024) FROM GENERATE_SERIES(1, 10000); -- Check sizes SELECT PG_SIZE_PRETTY(PG_RELATION_SIZE('tab1')); -- Result: 45 MB SELECT PG_SIZE_PRETTY(PG_RELATION_SIZE('tab2')); -- Result: 21 MB
```

The FLOAT2 table uses 21 MB — roughly half the 45 MB used by the FLOAT4 table.

**Create a table with FLOAT2 vectors**

FLOAT2 is an internal data type. The system handles type conversions and operators automatically.

```
CREATE TABLE [TABLE_NAME] (
    C1 INT,
    C2 FLOAT2[],
    C3 VARCHAR(20),
    PRIMARY KEY(C1)
) DISTRIBUTED BY(C1);
```

The `C2` column stores FLOAT2 vectors.
**Example:** Create a table named `FACE_TABLE` with a FLOAT2 vector column.

```
CREATE TABLE FACE_TABLE (
    C1 INT PRIMARY KEY,
    C2 FLOAT2[],
    C3 VARCHAR(20)
) DISTRIBUTED BY (C1);
```

**Insert data**

Insert FLOAT2 arrays using any of the following methods. The system automatically converts REAL and FLOAT4 arrays to FLOAT2.

```
-- Explicit FLOAT2 array INSERT INTO FACE_TABLE (C1, C2, C3)
    VALUES (1, ARRAY[1.3, 2.4, 5.6]::FLOAT2[], 'name1');
-- REAL array (auto-converted to FLOAT2) INSERT INTO FACE_TABLE (c1, c2, c3)
    VALUES (2, ARRAY[3.4, 6.1, 7.6]::REAL[], 'name2');
-- FLOAT4 array (auto-converted to FLOAT2) INSERT INTO FACE_TABLE (c1, c2, c3)
    VALUES (3, ARRAY[9.5, 1.2, 0.6]::FLOAT4[], 'name3');
```

**Query data**

```
SELECT * FROM FACE_TABLE;
```

Expected output:

```
 c1 |           c2            |  c3
----+-------------------------+-------
  1 | {1.2998,2.40039,5.60156}  | name1
  2 | {3.40039,6.10156,7.60156} | name2
  3 | {9.5,1.2002,0.600098}     | name3
```

**Conversion functions**

Use `array_f16_to_f32` and `array_f32_to_f16` to convert between FLOAT2 and FLOAT4 arrays.

| Function | Description |
|---|---|
| array f16 to f32(arr) _ _ _ | Converts a FLOAT2 array to FLOAT4 |
| array f32 to f16(arr) _ _ _ | Converts a FLOAT4 array to FLOAT2 |

**Performance benchmark** — 10,000 rows x 1,024 dimensions on a machine with AVX and
SSE2:

```
\TIMING -- FLOAT4 to FLOAT2 SELECT ARRAY_F32_TO_F16(a) FROM TAB1; -- Time: 5998.832 ms (approx. 6 s) -- FLOAT2 to FLOAT4 SELECT ARRAY_F16_TO_F32(a) FROM TAB2; -- Time: 5507.388 ms (approx. 5.5 s)
```

**Distance calculation**

Use `L2_DISTANCE` to calculate Euclidean distance between FLOAT2 vectors. Mixed FLOAT2 and FLOAT4 operands are supported.

```
-- FLOAT2 vs FLOAT2 SELECT L2_DISTANCE(
    ARRAY[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]::FLOAT2[],
    ARRAY[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]::FLOAT2[]
```

);

```
-- FLOAT4 vs FLOAT2 (mixed) SELECT L2_DISTANCE(
    ARRAY[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]::FLOAT4[],
    ARRAY[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]::FLOAT2[]
```

);

**Use case: facial recognition**

Security systems store captured facial data daily and search for matches based on facial images. The following steps show how to use FLOAT2 for this workflow.
1. Create a table to store facial data.

```
CREATE TABLE FACE_TABLE (
    C1 INT PRIMARY KEY,  -- Face ID
    C2 FLOAT2[],         -- Face vector
    C3 VARCHAR(20)       -- Face name
) DISTRIBUTED BY(C1);
```

2. Create an Approximate Nearest Neighbor (ANN) index on the vector column.

```
CREATE INDEX FACE_TABLE_IDX ON FACE_TABLE USING ANN(C2) WITH(dim=10);
```

3. Insert facial data.

```
INSERT INTO FACE_TABLE (C1, C2, C3)
    VALUES (1, ARRAY[1.3, 2.4, 5.6]::FLOAT2[], 'name1');
INSERT INTO FACE_TABLE (c1, c2, c3)
    VALUES (2, ARRAY[3.4, 6.1, 7.6]::REAL[], 'name2');
INSERT INTO FACE_TABLE (c1, c2, c3)
    VALUES (3, ARRAY[9.5, 1.2, 0.6]::FLOAT4[], 'name3');
```

4. Run a vector search using the `<->` distance operator.

```
SELECT * FROM FACE_TABLE ORDER BY C1 <-> ARRAY[2.81574,9.84361,8.07218]::FLOAT2[] LIMIT 10;
```

`ARRAY[2.81574,9.84361,8.07218]::FLOAT2[]` is the query face vector. The database returns the closest matches from the table.

### Use AnalyticDB for

**PostgreSQL sparse vectors**

If you want to store vectors whose most elements are zero in an efficient manner, you can create a sparse vector table instead of a dense vector table, to reduce storage space. This topic describes how to use sparse vectors in an AnalyticDB for PostgreSQL vector database. You can create a sparse vector table, create a sparse vector index, use sparse vectors to perform search, and use sparse and dense vectors to perform hybrid search.

**Overview**

In most cases, vectors are classified into dense vectors and sparse vectors in vector databases. A sparse vector contains a large number of zero values. Among tens of thousands of dimensions, only few dimensions have non-zero values. When you use sparse vectors to perform search, each sparse vector represents a document, in which each dimension specifies a keyword in a dictionary or vocabulary and each dimension value specifies the importance of a keyword in the document. If the sparse vectors are generated by using the BM25 algorithm, the dimension values contain the number of keyword matches, keyword occurrence frequency, and other text relevance factors. In machine learning and natural language processing (NLP) technologies, storing vector data by using ordinary arrays or lists results in wasted storage space. In this case, sparse vectors are introduced to efficiently store and process vector data. In most cases, you can use sparse vectors to specify text, images, or other types of data. The data structure of sparse vectors can significantly reduce storage usage and computing resource usage for storing and processing high-dimensional data. The following figure shows the difference between dense vectors and sparse vectors.

**Prerequisites**

An AnalyticDB for PostgreSQL instance of V6.6.2.3 or later is created. For more information, see Create an instance. The vector search engine optimization feature is enabled for the AnalyticDB for PostgreSQL instance. For more information, see Enable or disable vector search engine optimization.

**Use sparse vectors**

**Create a sparse vector table**

**Syntax**

```
CREATE TABLE <SparseVectorTable>
```

`(`

```
    id int PRIMARY KEY,
    description text,
    ...,
    sparse_vector svector(MAX_DIM),
)DISTRIBUTED BY (id);
```

**Parameters:**

SparseVectorTable: the name of the sparse vector table. sparse_vector: the name of the sparse vector column. The value of the column is of the SVECTOR type. MAX_DIM: the maximum number of sparse vector dimensions, which is not the number of dimensions that have non-zero values.

**Example**

Create a sparse vector table named svector_test.

```
-- Create a table that contains a sparse vector column. CREATE TABLE <svector_test>(
    id bigint,
    type int,
    tag varchar(10),
    document text,
    sparse_features svector(250000)
) DISTRIBUTED BY (id); -- Set the storage mode of the sparse vector column to PLAIN. ALTER TABLE <svector_test> ALTER COLUMN sparse_features SET storage plain;
```

**Note**

PLAIN mode: PostgreSQL uses The Oversized-Attribute Storage Technique (TOAST) to store large objects, large field values, or data that cannot be contained within a regular data page. TOAST facilitates efficient storage and access to data. If you set the storage mode of a column to PLAIN, data in the column is not compressed or broken up. Data is stored within a single row and not moved to a TOAST table. In most cases, the PLAIN storage mode is used to process small field values to prevent additional overheads caused by TOAST. You can also use the PLAIN storage mode to process data types that support efficient storage, such as integers and small text fields.

**Create a sparse vector index**

**Syntax**

Sparse vector indexes support only the inner product distance metric. Sparse vector indexes do not support the product quantization (PQ) feature or the memory mapping technology. Syntax:

```
CREATE INDEX <idx_sparse_vector> ON MyTable USING vector_index (sparse_vector_column); WITH (DISTANCEMEASURE=IP,
      HNSW_M=$M,
      HNSW_EF_CONSTRUCTION=$EF_CONSTURCTION);
```

**Parameters:**

idx_sparse_vector: the name of the sparse vector index. DISTANCEMEASURE: the name of the distance metric. To prevent errors, set the value to IP. HNSW_M and HNSW_EF_CONSTRUCTION: For information about the parameters, see Create a vector index.

**Example**

In this example, the svector_test sparse vector table is used to create sparse vector indexes.

```
-- Create B-tree indexes for structured fields in hybrid search. If a structured field is of the ARRAY type, you can also create a generalized inverted index (GIN) index for the field. CREATE INDEX svector_test(type); CREATE INDEX svector_test(tag); -- Create a Hierarchical Navigable Small World (HNSW) index for the sparse vector colum
```

`n.`

```
CREATE INDEX ON svector_test USING ANN(sparse_features) WITH(DISTANCEMEASURE=IP,HNSW_M=64,pq_enable=0,external_storage=0);
```

**Representation of sparse vector data**

AnalyticDB for PostgreSQL allows you to use the SVECTOR type to represent sparse vector data. The SVECTOR type supports strings in the JSON format. You can use the indices field to specify the index array (non-negative integers) and the values field to specify the value array (floating-point numbers). The following example describes a 20-dimensional sparse vector:

**Example of sparse vector data**

```
[0, 0, 1.1, 0, 0, 0, 2.2, 0, 0, 3.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

**Representation of sparse vector data**

```json
{"indices":[2, 6, 9], "values":[1.1, 2.2, 3.3]}
```

**Parameters:**

indices:[2, 6, 9] specifies that the dimension numbers of non-zero values in the sparse vector are 2, 6, and 9. values:[1.1, 2.2, 3.3] specifies that the non-zero values in the sparse vector are 1.1, 2.2, and 3.3. In an AnalyticDB for PostgreSQL vector database, you can use ::svector to convert a string into the SVECTOR type. Sample statement:

```json
postgres=# SELECT '{"indices":[2, 6, 9], "values":[1.1, 2.2, 3.3]}'::svector; svector -------------------------------------------- {"indices":[2,6,9],"values":[1.1,2.2,3.3]} (1 ROW)
```

**Import sparse vector data**

You can use the INSERT or COPY statement to import sparse vector data. In this example, the svector_test sparse vector table and the INSERT statement are used to import sparse vector data.

```
-- Insert sparse vector data. INSERT INTO svector_test VALUES (1, 1, 'a', 'xxx', '{"indices":[2, 6, 9], "values":[1.1 , 2.2, 3.3]}'::svector); INSERT INTO svector_test VALUES (2, 2, 'b', 'xxx', '{"indices":[50, 100, 200], "values" :[2.1, 3.2, 4.3]}'::svector); INSERT INTO svector_test VALUES (3, 3, 'b', 'xxx', '{"indices":[150, 60, 90], "values": [5, 1e3, 1e-3]}'::svector);
```

**Use sparse vectors to perform search**

**Syntax**

For sparse vector tables, sparse vector indexes support only the inner product distance metric. Sparse vector search can be divided into exact search and approximate search. Syntax:

**Exact search**

```
SELECT id, inner_product(<sparse_vector>, '{"indices":[1,2,..], "values": [1.1,2.2...]}'::svector) AS score FROM <SparseVectorTable> ORDER BY negative_inner_product(<sparse_vector>, '{"indices":[1,2,..], "values":[1.1,2.2...]}'::svector) LIMIT <topk>;
```

**Parameters:**

sparse_vector: the name of the sparse vector column. SparseVectorTable: the name of the sparse vector table. topk: the top k elements from the result set that you want to obtain.

**Approximate search**

```
SELECT id, inner_product(<sparse_vector>, '{"indices":[1,2,..], "values": [1.1,2.2...]}'::svector) AS score FROM <SparseVectorTable> ORDER BY <sparse_vector> '{"indices":[1,2,..], "values":[1.1,2.2...]}'::svector LIMIT <topk>;
```

**Parameters:**

sparse_vector: the name of the sparse vector column. SparseVectorTable: the name of the sparse vector table. topk: the top k elements from the result set that you want to obtain.

**Example**

In this example, the svector_test sparse vector table is used to perform sparse vector search.

**Sparse vector search**

```
SELECT id, sparse_features, '{"indices":[2,60,50], "values":[2,0.01, 0.02]}' <#> sparse_features AS score FROM svector_test ORDER BY score LIMIT 3;
```

**Search result**

```
   id   |                 sparse_features                 |        score
--------+-------------------------------------------------+---------------------
      3 | {"indices":[60,90,150],"values":[1000,0.001,5]} |                 -10
      1 | {"indices":[2,6,9],"values":[1.1,2.2,3.3]}      |   -2.20000004768372
      2 | {"indices":[50,100,200],"values":[2.1,3.2,4.3]} | -0.0419999957084656
(3 ROWS)
```

**Note**

You can use the fastann.sparse_hnsw_max_scan_points and fastann.sparse_hnsw_ef_search parameters to modify the recall rate of sparse vector search. For more information, see the "Appendixes" section of this topic.

**Use dense and sparse vectors to perform hybrid search**

Create a table named HYBRID_SEARCH_TEST that contains dense and sparse vectors to perform hybrid search. Sample statements for creating the table:

```
-- Create a table for hybrid search. CREATE TABLE IF NOT EXISTS HYBRID_SEARCH_TEST (
   id integer PRIMARY key,
   corpus text,
   filter integer,
   dense_vector float4[],
   sparse_vector svector(250003)
) distributed BY (id); -- Set the storage mode of the sparse vector column to PLAIN. ALTER TABLE hybrid_search_test ALTER COLUMN dense_vector SET storage plain; ALTER TABLE hybrid_search_test ALTER COLUMN sparse_vector SET storage plain;
```

Sample statements for creating indexes:

```
-- Create a structured index. CREATE INDEX ON hybrid_search_test(FILTER); -- Create a dense vector index. CREATE INDEX ON hybrid_search_test USING ANN(dense_vector) WITH(DISTANCEMEASURE=IP, DIM =1024, HNSW_M=64, HNSW_EF_CONSTRUCTION=600, EXTERNAL_STORAGE=1); -- Create a sparse vector index. CREATE INDEX ON hybrid_search_test USING ANN(sparse_vector) WITH(DISTANCEMEASURE=IP, HN SW_M=64, HNSW_EF_CONSTRUCTION=600);
```

Sample statements for performing dense vector search, sparse vector search, and hybrid search:

```
-- Dense vector search + filter SELECT id, corpus FROM hybrid_search_test WHERE FILTER IN (0, 100, 200, 300, 400, 500, 600, 700, 800, 900) ORDER BY dense_vector <#> ARRAY[1,2,3,...,1024]::float4[] LIMIT 100
```

;

```
-- Sparse vector search + filter SELECT id, corpus FROM hybrid_search_test WHERE FILTER IN (0, 100, 200, 300, 400, 500, 600, 700, 800, 900) ORDER BY sparse_vector <#> '{"indices":[1,2,..], "values":[1.1,2.2. ..]}'::svector LIMIT 100; -- Hybrid search + filter WITH combined AS ( (SELECT id, corpus, inner_product_distance(dense_vector, ARRAY[1,2,3,...,1024]::float4[]) AS dist1, sparse_vector <#> '{"indices":[1,2,..], "val ues":[1.1,2.2...]}'::svector AS dist2 FROM hybrid_search_test WHERE FILTER IN (0, 100, 200, 300, 400, 500, 600, 700, 800, 900) ORDER BY dist2 LIMIT 100)
  UNION ALL
(SELECT id, corpus, inner_product(sparse_vector, '{"indices":[1,2,..], "values":[1.1,2. 2...]}'::svector) AS dist1, dense_vector <#> ARRAY[1,2,3,...,1024]::float4[] AS dist2 F ROM hybrid_search_test WHERE FILTER IN (0, 100, 200, 300, 400, 500, 600, 700, 800, 900) ORDER BY dist2 LIMIT 100 ) ) SELECT DISTINCT first_value(id) OVER (PARTITION BY id) AS id, first_value(corpus) OV ER (PARTITION BY id) AS corpus, MAX(dist1 - dist2) OVER (PARTITION BY id) AS dist FROM combined ORDER BY dist DESC LIMIT 100;
```

**Appendixes**

**Engine parameters related to sparse vector search**

| Engine parameter related to sparse vector search | Description | Default value | Valid value |
|---|---|---|---|

| fastann.sparse hnsw _ _ max scan points _ _ | The maximum number of scan points when you use HNSW indexes to perform sparse vector search. This parameter terminates search in advance. You can use this parameter to test the recall rate. | 8000 | [1, 8000000] |
|---|---|---|---|
| fastann.sparse hnsw e _ _ f search _ | The size of search candidate sets when you use HNSW indexes to perform sparse vector search. You can use this parameter to test the recall rate. | 400 | [10, 10000] |

**Note**

You can configure the preceding parameters for sessions.

**Supported vector functions for sparse vectors**

| Purpose | Vector function | Data type of the return value | Description | Supported data type |
|---|---|---|---|---|
|   | l2 distance _ | DOUBLE PRECISION | Calculates the rooted Euclidean distance between two sparse vectors. This function is used to measure the distance between two sparse vectors. | SVECTOR |

| Calculation | inner product _ | DOUBLE PRECISION | Calculates the inner product distance between two vectors, which is equivalent to cosine similarity after vector normalization. This function is used to replace cosine similarity after vector normalization. | SVECTOR |
|---|---|---|---|---|
|   | dp distance _ | DOUBLE PRECISION | Calculates the dot product distance, which is the same as the inner product distance. | SVECTOR |
|   | cosine similarity _ | DOUBLE PRECISION | Calculates the cosine similarity between two sparse vectors. This function is used to measure the similarity between two sparse vectors based on the direction regardless of the actual length of the sparse vectors. Valid values of the cosine similarity: -1 to 1. | SVECTOR |
|   | svector add _ | SVECTOR | Calculates the sum of two sparse vectors. | SVECTOR |
|   | svector sub _ | SVECTOR | Calculates the difference between two sparse vectors. | SVECTOR |
|   | svector mul _ | SVECTOR | Calculates the product of two sparse vectors. | SVECTOR |

|   | svector norm _ | DOUBLE PRECISION | Calculates the norm of a sparse vector. | SVECTOR |
|---|---|---|---|---|
|   | svector angle _ | DOUBLE PRECISION | Calculates the angle between two sparse vectors. | SVECTOR |
| Sorting | l2 squared dista _ _ nce | DOUBLE PRECISION | Sorts vectors based on the squared Euclidean distance. This function requires fewer calculation than the sorting method based on the rooted Euclidean distance. | SVECTOR |
|   | negative inner p _ _ roduct | DOUBLE PRECISION | Sorts vectors based on the negative inner product distance. This function is used to sort vectors in descending order based on the inner product distance. | SVECTOR |
|   | cosine distance _ | DOUBLE PRECISION | Sorts vectors based on the cosine distance. This function is used to sort vectors in descending order based on the cosine similarity. Valid values of the cosine distance: 0 to 2. | SVECTOR |

**Examples of vector functions**

```json
-- Euclidean distance SELECT l2_distance('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"ind ices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Inner product distance SELECT inner_product('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"i ndices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Cosine similarity SELECT l2_distance('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"ind ices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Vector sum SELECT svector_add('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"ind ices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Vector subtraction SELECT svector_sub('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"ind ices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Vector multiplication SELECT svector_mul('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{"ind ices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector); -- Squared Euclidean distance SELECT l2_squared_distance('{"indices":[1,2,3,4,5,6], "values": [1,2,3,4,5,6]}'::svector, '{"indices":[1,2,3,4,5,6], "values": [2,3,4,5,6,7]}'::svector); -- Negative inner product distance SELECT negative_inner_product('{"indices":[1,2,3,4,5,6], "values": [1,2,3,4,5,6]}'::svector, '{"indices":[1,2,3,4,5,6], "values": [2,3,4,5,6,7]}'::svector); -- Cosine distance SELECT cosine_distance('{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector, '{ "indices":[1,2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector);
```

**Supported vector operators for sparse vectors**

| Operator | Calculation | Sorting | Supported data type |
|---|---|---|---|
| <-> | Calculates the squared Euclidean distance between two vectors. The result is equivalent to the result of the l2 squared distance _ _ function. | None | SVECTOR |

| <#> | Calculates the negative inner product distance between two vectors. The result is equivalent to the result of the negative inner produc _ _ t function. | Sorts vectors in descending order based on the dot product distance. | SVECTOR |
|---|---|---|---|
| <#> | Calculates the cosine distance between two vectors. The result is equivalent to the result of the cosine distance _ function. | None | SVECTOR |
| + | Calculates the sum of two sparse vectors. | None | SVECTOR |
| - | Calculates the difference between two sparse vectors. | None | SVECTOR |
| * | Calculates the product of two sparse vectors. | None | SVECTOR |

**Examples of vector operators**

```
-- Squared Euclidean distance SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector <-> '{"indices":[1, 2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS score; -- Negative inner product distance SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector <#> '{"indices":[1, 2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS score; -- Cosine distance SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector <=> '{"indices":[1, 2,3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS score; -- Sum of two vectors SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector + '{"indices":[1,2, 3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS value; -- Difference between two vectors SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector + '{"indices":[1,2, 3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS value; -- Product of two vectors SELECT '{"indices":[1,2,3,4,5,6], "values":[1,2,3,4,5,6]}'::svector * '{"indices":[1,2, 3,4,5,6], "values":[2,3,4,5,6,7]}'::svector AS value;
```

### Use pgvector-compatible

**vector search**

pgvector is an open source PostgreSQL extension for vector similarity search. You can use the pgvector extension to create vector indexes and perform similarity calculation and queries between vectors in scenarios such as vector similarity search, recommendation systems, and clustering analysis.

**Prerequisites**

Before you use pgvector-compatible vector search, make sure that the following requirements are met: The minor version of an AnalyticDB for PostgreSQL V6.0 instance is 6.6.1.0 or later. For information about how to view the minor version of an AnalyticDB for PostgreSQL instance, see View the minor version of an instance. The vector search engine optimization feature is enabled for the AnalyticDB for PostgreSQL V6.0 instance. For more information, see Enable or disable vector search engine optimization.

**pgvector-compatible vector search**

AnalyticDB for PostgreSQL vector databases are fully compatible with the read and write operations of vector tables that use the pgvector extension to perform vector search. You need to only modify the SQL syntax for creating indexes. If your business uses the pgvector extension to perform vector search, you can seamlessly migrate your business to AnalyticDB for PostgreSQL vector databases after slightly modifying business code. Compared with the vector search method based on the pgvector extension, the pgvector-compatible vector search method of AnalyticDB for PostgreSQL vector databases provides the following advantages: AnalyticDB for PostgreSQL vector databases are fully compatible with the SQL syntax of the pgvector extension and can reuse pgvector-supported language clients. The pgvector extension is used on standalone PostgreSQL databases, whereas AnalyticDB for PostgreSQL vector databases use a distributed architecture to process more vector data. AnalyticDB for PostgreSQL vector databases use the FastANN vector search engine that is developed in-house by Alibaba Cloud to provide better performance than the pgvector extension. For more information, see Performance tests for vector analysis. AnalyticDB for PostgreSQL vector databases can use execution plans and operators to perform hybrid search, whereas the pgvector extension does not support hybrid search. The pgvector extension can use only partitions to perform simple search. AnalyticDB for PostgreSQL vector databases use the FLOAT2 type to compress vector tables and provide the product quantization (PQ) feature to compress vector indexes. As a result, AnalyticDB for PostgreSQL vector databases require lower storage costs than the pgvector extension.

**Create a vector table**

You can create a pgvector-compatible vector table by using the same syntax for creating ordinary vector tables in AnalyticDB for PostgreSQL. You need to only change the vector columns from the array type, such as `SMALLINT[]` , `FLOAT2[]` , or `FLOAT4[]` , to the VECTOR type that is supported by the pgvector extension. Each pgvector-compatible vector table supports multiple vector columns.

**Syntax**

```
CREATE TABLE [TABLE_NAME]
```

`(`

```
    C1 DATATYPE,
    C2 DATATYPE,
    ......,
    CN VECTOR(DIM),
    PRIMARY KEY(C1 [,C2,...CN])
) DISTRIBUTED BY (C1);
```

The CN parameter specifies the vector columns, which are of the VECTOR type. The DIM parameter specifies the vector dimension.

**Example**

Create a vector table named FACE_TABLE. Specify C1 as the primary key, and C2 and C3 as the vector columns.

```
CREATE TABLE FACE_TABLE (
    C1 INT,
    C2 VECTOR(512) NOT NULL,
    C3 VECTOR(1536) NOT NULL,
    C4 TIMESTAMP NOT NULL,
    C5 VARCHAR(20) NOT NULL,
    PRIMARY KEY (C1)
) DISTRIBUTED BY (C1);
```

**Create a vector index**

You can create a vector index for a pgvector-compatible vector table in AnalyticDB for PostgreSQL by using the syntax of the FastANN vector search engine, which is different from the syntax of the pgvector extension.

**Syntax**

```
CREATE INDEX [INDEX_NAME] ON [SCHEMA_NAME].[TABLE_NAME] USING ANN(COLUMN_NAME) WITH (DIM=<DIMENSION>,
      DISTANCEMEASURE=<MEASURE>,
      HNSW_M=<M>,
      HNSW_EF_CONSTRUCTION=<EF_CONSTURCTION>,
      PQ_ENABLE=<PQ_ENABLE>,
      PQ_SEGMENTS=<PQ_SEGMENTS>,
      PQ_CENTERS=<PQ_CENTERS>,
      EXTERNAL_STORAGE=<EXTERNAL_STORAGE>;
```

The VECTOR type that is supported by the pgvector extension already contains the dimension information. When you create a vector index, you do not need to specify the DIM parameter. For information about other parameters, see Create a vector index.

**Example**

Create vector indexes for the FACE_TABLE vector table.

```
-- Create three types of vector indexes on the C2 column. CREATE INDEX idx_c2_l2 ON FACE_TABLE USING ann(C2) WITH (distancemeasure=l2, hnsw_m=64, pq_enable=1); CREATE INDEX idx_c2_ip ON FACE_TABLE USING ann(C2) WITH (distancemeasure=ip, hnsw_m=64, pq_enable=1); CREATE INDEX idx_c2_cosine ON FACE_TABLE USING ann(C2) WITH (distancemeasure=cosine, hn sw_m=64, pq_enable=1); -- Create three types of vector indexes on the C3 column. CREATE INDEX idx_c3_l2 ON FACE_TABLE USING ann(C3) WITH (distancemeasure=l2, hnsw_m=64, pq_enable=1); CREATE INDEX idx_c3_ip ON FACE_TABLE USING ann(C3) WITH (distancemeasure=ip, hnsw_m=64, pq_enable=1); CREATE INDEX idx_c3_cosine ON FACE_TABLE USING ann(C3) WITH (distancemeasure=cosine, hn sw_m=64, pq_enable=1);
```

In this example, multiple vector indexes are created on multiple vector columns. To prevent invalid indexes, you must create vector indexes based on your business requirements.

**Import vector data**

You can import vector data to a pgvector-compatible vector table by using the same syntax of the pgvector extension. For example, execute the following INSERT statement to insert data into the FACE_TABLE table:

```
INSERT INTO FACE_TABLE values (1, '[1,2,3 ... 512]', '[1,2,3 ... 1536]', '2023-12-29 00:00:00', 'aaa.bbb.ccc/face1.jpg');
```

**Vector search**

You can perform vector search on a pgvector-compatible vector table by using the same syntax of the pgvector extension. The engine parameters related to the recall rate of vector search are the same as the parameters of AnalyticDB for PostgreSQL vector databases. For more information, see Perform vector search. For example, execute the following statements to perform vector search on the FACE_TABLE table:

```
-- Perform exact search based on the Euclidean distance. SELECT C1 FROM FACE_TABLE ORDER BY vector_l2_squared_distance(C2, '[1,2,3 ... 512]') LI MIT 10; -- Perform exact search based on the inner product distance. SELECT C1 FROM FACE_TABLE ORDER BY vector_negative_inner_product(C2, '[1,2,3 ... 512]') LIMIT 10; -- Perform exact search based on the cosine similarity. SELECT C1 FROM FACE_TABLE ORDER BY cosine_distance(C2, '[1,2,3 ... 512]') LIMIT 10; -- Perform approximate index search based on the Euclidean distance. SELECT C1 FROM FACE_TABLE ORDER BY C2 <-> '[1,2,3 ... 512]' LIMIT 10; -- Perform approximate index search based on the inner product distance. SELECT C1 FROM FACE_TABLE ORDER BY C2 <#> '[1,2,3 ... 512]' LIMIT 10; -- Perform approximate index search based on the cosine similarity. SELECT C1 FROM FACE_TABLE ORDER BY C2 <=> '[1,2,3 ... 512]' LIMIT 10;
```

You created vector indexes based on the Euclidean distance, inner product distance, and cosine similarity on the C2 column of the FACE_TABLE table. You can use the approximate index search method to match the vector indexes. When you use the approximate index search method, make sure that the `<->` , `<#>` , and `<=>` operators work with the vector indexes that are created by using the corresponding distance metric. If the operators do not work with the vector indexes, the approximate index search is downgraded to exact search.

**SQL optimization for vector search**

If you want to return the score value of the vector distance, you can execute the following statements to improve performance. To reduce the amount of time required for calculation, use the sort result of the vector index to calculate the final score value of the vector distance. Sample statements:

```
-- Search vector data based on the Euclidean distance. SELECT t.C1 as C1, sqrt(t.score) as score FROM
  (SELECT C1, C2 <-> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t;
-- Search vector data based on the inner product distance. SELECT t.C1 as C1, (-1 * t.score) as score FROM
  (SELECT C1, C2 <#> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t;
-- Search vector data based on the cosine similarity. SELECT t.C1 as C1, (1.0 - t.score) as score FROM
  (SELECT C1, C2 <=> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t;
```

In the vector search results, the score value indicates the squared Euclidean distance, inner product distance, or cosine similarity. If you want to return results that are filtered based on a score range, you can execute the following statements to improve performance. To reduce the amount of time required for calculation, use the sort result of the vector index to calculate the final score value of the vector distance. Sample statements:

```
-- Search vector data based on the Euclidean distance. SELECT t.C1 as C1, sqrt(t.score) as score FROM
  (SELECT C1, C2 <-> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t
WHERE score < 100; -- Search vector data based on the inner product distance. SELECT t.C1 as C1, (-1 * t.score) as score FROM
  (SELECT C1, C2 <#> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t
WHERE score > 10; -- Search vector data based on the cosine similarity. SELECT t.C1 as id, (1.0 - t.score) as score FROM
  (SELECT C1, C2 <=> '[1,2,3 ... 512]' as score
   FROM FACE_TABLE
   ORDER BY score LIMIT topk) t
WHERE score > 0.5;
```

**Hybrid search**

You can perform hybrid search on a pgvector-compatible vector table by using the same syntax for performing hybrid search on ordinary vector tables in AnalyticDB for PostgreSQL. For more information, see Use hybrid search. For example, execute the following statement to perform hybrid search on the FACE_TABLE table:

```
SELECT C1 FROM FACE_TABLE WHERE
  C4 > '2023-10-01 00:00:00' AND C4 < '2024-01-01 00:00:00'
ORDER BY
  C2 <-> '[1,2,3 ... 512]'
LIMIT 10;
```

**Adaptation of the open source code repository**

This section describes how to adapt the business application code that uses the pgvector extension to AnalyticDB for PostgreSQL vector databases by performing a simple modification. In this example, an open source large language model (LLM) application development platform named Dify is used. The adaptation involves the following modifications: Comment out the installation of the pgvector extension. AnalyticDB for PostgreSQL vector databases are compatible with the read and write operations of vector tables that use the pgvector extension, but do not use the pgvector extension. You do not need to install the pgvector extension on AnalyticDB for PostgreSQL vector databases. When you create AnalyticDB for PostgreSQL vector databases, the FastANN vector search engine is automatically installed. You need to only comment out the installation of the pgvector extension. Sample code:

```python
# The code is stored in the api/core/rag/datasource/vdb/pgvector/pgvector.py path.
def _create_collection(self, dimension: int):
    cache_key = f"vector_indexing_{self._collection_name}"
    lock_name = f"{cache_key}_lock"
    WITH redis_client.lock(lock_name, timeout=20):
        collection_exist_cache_key = f"vector_indexing_{self._collection_name}"
        if redis_client.get(collection_exist_cache_key):
            RETURN
        WITH self._get_cursor() AS cur:
            # Comment out the installation of the pgvector extension.
            #cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute(SQL_CREATE_TABLE.format(table_name=self.table_name,
dimension=dimension))
            # TODO: CREATE index https://github.com/pgvector/pgvector?tab=readme-ov-
file#indexing
        redis_client.set(collection_exist_cache_key, 1, ex=3600)
```

Modify the method that is used to create vector tables. AnalyticDB for PostgreSQL vector databases are built based on PostgreSQL 9.4 and do not support the **USING heap** syntax when tables are created. AnalyticDB for PostgreSQL uses a distributed database structure and requires distribution keys. Sample code:

```bash
# The code is stored in the api/core/rag/datasource/vdb/pgvector/pgvector.py path.
SQL_CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS {table_name} (
    id uuid PRIMARY KEY,
    text text NOT NULL,
    meta jsonb NOT NULL,
    embedding vector({dimension}) NOT NULL
) USING heap; """
# Change the preceding table creation statement to the following statement:
SQL_CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS {table_name} (
    id uuid PRIMARY KEY,
    text text NOT NULL,
    meta jsonb NOT NULL,
    embedding vector({dimension}) NOT NULL
) DISTRIBUTED BY (id); """
```

Modify the method that is used to create vector indexes. AnalyticDB for PostgreSQL vector databases use the FastANN vector search engine to implement vector search, but do not use the pgvector extension. The syntax that is used to create vector indexes in AnalyticDB for PostgreSQL, especially the index keyword, is different from the syntax that is used in the pgvector extension. You must use the syntax of AnalyticDB for PostgreSQL vector databases to create indexes. Sample code:

```python
# The code is stored in the api/core/rag/datasource/vdb/pgvector/pgvector.py path.
# Add an SQL statement for creating a vector index. You can also create an index in t
he database. SQL_CREATE_INDEX = """ CREATE INDEX ON {table_name} USING ann(embedding) WITH (HNSW_M=16, HNSW_EF_CONSTRUCTION=500, PQ_ENABLE=1); """ def _create_collection(self, dimension: int):
    cache_key = f"vector_indexing_{self._collection_name}"
    lock_name = f"{cache_key}_lock"
    WITH redis_client.lock(lock_name, timeout=20):
        collection_exist_cache_key = f"vector_indexing_{self._collection_name}"
        if redis_client.get(collection_exist_cache_key):
            RETURN
        WITH self._get_cursor() AS cur:
            # Comment out the installation of the pgvector extension.
            #cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
            cur.execute(SQL_CREATE_TABLE.format(table_name=self.table_name,
dimension=dimension))
            # TODO: CREATE index https://github.com/pgvector/pgvector?tab=readme-ov-
file#indexing
            # Create a vector index for an AnalyticDB for PostgreSQL vector database.
            cur.execute(SQL_CREATE_INDEX.format(table_name=self.table_name))
        redis_client.set(collection_exist_cache_key, 1, ex=3600)
```

**Appendixes**

**Language clients that are supported by the pgvector extension**

| Programming language | URL of the client library code |
|---|---|
| C | pgvector-C |
| C++ | pgvector-cpp |
| Go | pgvector-go |
| Java, Kotlin, Groovy, and Scala | pgvector-java |
| PHP | pgvector-php |
| Python | pgvector-python |

| Rust | pgvector-rust |
|---|---|

You can use multiple language clients that are supported by the pgvector extension to access AnalyticDB for PostgreSQL vector databases. You need to only modify the SQL statements related to vector indexes.

**Supported vector functions**

| Purpose | Vector function | Data type of the return value | Description | Supported data type |
|---|---|---|---|---|
| Calculation | l2 distance _ | DOUBLE PRECISION | Calculates the rooted Euclidean distance between two vectors. This function is used to measure the distance between two vectors. | VECTOR |
|   | inner product _ | DOUBLE PRECISION | Calculates the inner product distance between two vectors, which is equivalent to cosine similarity after vector normalization. This function is used to replace cosine similarity after vector normalization. | VECTOR |
|   | cosine similarity _ | DOUBLE PRECISION | Calculates the cosine similarity between two vectors. This function is used to measure the similarity between two vectors based on the direction regardless of the actual length of the vectors. Valid values of the cosine similarity: -1 to 1. | VECTOR |

|   | vector dims _ | INTEGER | Calculates the dimensions of a vector. | VECTOR |
|---|---|---|---|---|
|   | vector norm _ | DOUBLE PRECISION | Calculates the norm of a vector. | VECTOR |
|   | vector add _ | VECTOR | Calculates the sum of two vectors. | VECTOR |
|   | vector sub _ | VECTOR | Calculates the difference between two vectors. | VECTOR |
|   | vector mul _ | VECTOR | Calculates the product of two vectors. | VECTOR |
|   | vector angle _ | DOUBLE PRECISION | Calculates the angle between two vectors. | VECTOR |
|   | vector l2 squared dis _ _ _ tance | DOUBLE PRECISION | Sorts vectors based on the squared Euclidean distance. This function requires fewer calculation than the sorting method based on the rooted Euclidean distance. | VECTOR |
| Sorting |   |   |   |   |
|   | vector negative inner _ _ product _ | DOUBLE PRECISION | Sorts vectors based on the negative inner product distance. This function is used to sort vectors based on the inner product distance in descending order. | VECTOR |

|   | cosine distance _ | DOUBLE PRECISION | Sorts vectors based on the cosine distance. This function is used to sort vectors based on the cosine similarity in descending order. Valid values of the cosine distance: 0 to 2. | VECTOR |
|---|---|---|---|---|

For information about the vector distance formulas, see Create a vector index. Examples of vector functions:

```
-- Euclidean distance SELECT l2_distance('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Inner product distance SELECT inner_product('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Cosine similarity SELECT cosine_similarity('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Vector dimensions SELECT vector_dims('[1,1,1,1]'::vector); -- Vector norm SELECT vector_norm('[1,1,1,1]'::vector); -- Vector sum SELECT vector_add('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Vector subtraction SELECT vector_sub('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Vector multiplication SELECT vector_mul('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Vector angle SELECT vector_angle('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Squared Euclidean distance SELECT vector_l2_squared_distance('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Negative inner product distance SELECT vector_negative_inner_product('[1,1,1,1]'::vector, '[2,2,2,2]'::vector); -- Cosine distance SELECT cosine_distance('[1,1,1,1]'::vector, '[2,2,2,2]'::vector);
```

**Supported vector operators**

| Operator | Calculation | Sorting | Supported data type |
|---|---|---|---|

| <-> | Calculates the squared Euclidean distance between two vectors. The result is equivalent to the result of the l2 squared distance _ _ function. | Sorts vectors based on the squared Euclidean distance in ascending order. | VECTOR |
|---|---|---|---|
| <#> | Calculates the negative inner product distance between two vectors. The result is equivalent to the result of the negative inner produc _ _ t distance function. _ | Sorts vectors based on the dot product distance in descending order. | VECTOR |
| <=> | Calculates the cosine distance between two vectors. The result is equivalent to the result of the cosine distance _ function. | Sorts vectors based on the cosine similarity in descending order. | VECTOR |
| + | Calculates the sum of two vectors. | None | VECTOR |
| - | Calculates the difference between two vectors. | None | VECTOR |
| * | Calculates the product of two vectors. | None | VECTOR |

Examples of vector operators:

```
-- Squared Euclidean distance SELECT '[1,1,1,1]'::vector <-> '[2,2,2,2]'::vector AS score; -- Negative inner product distance SELECT '[1,1,1,1]'::vector <#> '[2,2,2,2]'::vector AS score; -- Cosine distance SELECT '[1,1,1,1]'::vector <=> '[2,2,2,2]'::vector AS score; -- Sum SELECT '[1,1,1,1]'::vector + '[2,2,2,2]'::vector AS value; -- Subtraction SELECT '[1,1,1,1]'::vector - '[2,2,2,2]'::vector AS value; -- Multiplication SELECT '[1,1,1,1]'::vector * '[2,2,2,2]'::vector AS value;
```

### Use hybrid search

If you want to search for structured and unstructured data at the same time, you can use the hybrid search feature of AnalyticDB for PostgreSQL vector databases. Hybrid search supports structured field filtering, semi-structured field filtering, and two-way retrieval based on vector search and full-text search.

**Overview**

Approximate nearest neighbor search (ANNS) vector indexes can handle only unstructured data search. In actual production environments, you may be required to search structured and unstructured data at the same time. For example, you want to query whether specific persons appear in a specific area within a specific time range. The time range and area range may be structured data, and human faces may be stored as unstructured data. To meet these requirements, AnalyticDB for PostgreSQL provides the hybrid search feature for structured and unstructured data. Most hybrid search solutions in the industry store structured data in database systems and unstructured data in vector search systems. Search results from the two types of systems are intersected to find the common matches. Then, the intersected results are aggregated to obtain the final result. This method extracts amplified results (quantity = amplification factor × top K) from vector search systems and then uses structured indexes to filter the results. However, structured indexes may filter out a large number of results, failing to meet the requirements for retrieving the top K results. The following section describes how hybrid search works by using structured and unstructured fields.

**How hybrid search works**

AnalyticDB for PostgreSQL integrates the FastANN vector search engine into databases as an index extension and allows you to perform vector search by using structured and semistructured indexes at the same time. You can use the ranked-biased overlap (RBO) cost estimation rules of the optimizer to generate different execution plans to search for structured and unstructured data at the same time. The following example shows how hybrid search works: Assume that you want to search for the top 100 items that have the highest similarity to a specified image, fall within a price range of USD 100 to USD 200, and were put on sale within the last month. Sample statements to create a table and indexes:

```
CREATE TABLE products (
    id serial primary key,
    name varchar(256),
    price real,
    inTime timestamp,
    url varchar(256),
    feature real[]
```

);

```
-- Set the storage mode of the vector column to PLAIN. ALTER TABLE products ALTER COLUMN feature SET STORAGE PLAIN; -- Create a B-tree index for structured columns. CREATE INDEX ON products(price, intime); -- Create a vector index for the vector column. CREATE INDEX ON products USING ann(feature) WITH (dim=512); -- Collect statistics to generate an optimal execution plan for hybrid search. ANALYZE products;
```

Sample statement to perform hybrid search:

```
SELECT id, price FROM products WHERE
    price > 100 AND price <=200
    AND inTime > '2019-03-01 00:00:00' AND inTime <= '2019-03-31 00:00:00'
ORDER BY
    feature <-> array[10,2.0,..., 512.0]
LIMIT 100;
```

AnalyticDB for PostgreSQL can generate three categories of execution plans based on whether an index is created for the structured condition columns (price and inTime) and the selectivity of structured conditions. To meet performance and retrieval requirements, AnalyticDB for PostgreSQL selects an optimal execution plan.

**Category 1: Brute-force query**

The system obtains all rows that meet the structured conditions, sorts the rows by vector distance, and then displays 100 rows of data that have the smallest distance. This execution plan provides a recall rate of 100% but returns query results at a low speed, especially when large amounts of data are queried or a large number of rows meet the structured conditions. Sample execution plan:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------
 LIMIT
     ->  Gather Motion 3:1  (slice1; segments: 3)
         Merge Key: (l2_squared_distance($0, feature))
             ->  LIMIT
                 ->  Sort
                     Sort Key: (l2_squared_distance($0, feature))
                     ->  Index Scan using products_price_idx on products
                         Index Cond: the filter condition for the price column.
                         Filter: the filter condition for the time column.
 Optimizer: Postgres query optimizer
```

**Category 2: Pure vector search and structured filtering**

The system uses a vector index to query N rows of data that have the highest similarity to a specified image, and then filters the data based on the structured conditions. This execution plan provides a fast query speed. However, if the structured conditions result in a low selectivity, the final output may contain fewer rows than expected. Sample execution plan:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------
 LIMIT
    ->  Gather Motion 3:1  (slice1; segments: 3)
        Merge Key: ((feature <-> $0))
            ->  LIMIT
                ->  Ann Index Scan using products_feature_idx on products
                    ORDER BY: (feature <-> $0)
                    Filter: the filter condition for the price and time columns.
 Optimizer: Postgres query optimizer
```

**Category 3: Hybrid search that combines vector search and structured filtering**

This execution plan combines the advantages of the preceding two execution plans. It uses indexes to query data and prevents the possibility of fewer data results. If a structured condition column is indexed and the index type supports bitmaps, this execution plan can use other indexes to generate bitmaps. This accelerates hybrid search. Sample execution plan:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------
 LIMIT
     ->  Gather Motion 3:1  (slice1; segments: 3)
         Merge Key: ((feature <-> $0))
         ->  LIMIT
             ->  Fusion Ann Scan
                 ->  Bitmap Index Scan on products_price_idx
                     Index Cond: the filter condition for the price column.
                     ->  Ann Index Scan with filter using products_feature_idx on prod
ucts
                         ORDER BY: (feature <-> $0)
                         Filter: the filter condition for the time column.
 Optimizer: Postgres query optimizer
```

The display of the Fusion Ann Scan or Ann Index Scan with filter node indicates that hybrid search is used in this execution plan. Ann Index Scan with filter: This node pushes filter conditions down to a vector index so that you can use the filter conditions and the index. Fusion Ann Scan: This node is displayed when specific structured condition columns are indexed. This node can accelerate the calculation of structured conditions by generating a bitmap as a left subtree and pushing the bitmap down to the vector index as a right subtree. When a Fusion Ann Scan node is displayed, the right subtree may be Ann Index Scan or Ann Index Scan with filter. If the Ann Index Scan node is displayed, only the bitmap is pushed down. If the Ann Index Scan with filter node is displayed, filter conditions other than the bitmap are pushed down.

**Usage methods**

Hybrid search of AnalyticDB for PostgreSQL vector databases supports structured field filtering, semi-structured field filtering, and two-way retrieval based on vector search and fulltext search. You can use one of the following methods to implement hybrid search: Vector search combined with structured field filtering. Data types of all structured fields are supported, including BIGINT, BOOLEAN, BYTEA, CHAR, VARCHAR, INTEGER, FLOAT, DOUBLE, DATE, SMALLINT, TIMESTAMP, and SERIAL. The structured fields can help accelerate hybrid search by creating default B-tree indexes. For more information, see Data types. Vector search combined with semi-structured field filtering. Data types of all semistructured fields are supported, including JSON, JSONB, and ARRAY. The structured fields can help accelerate hybrid search by creating GIN indexes. For more information, see Operations on JSON & JSONB data types and ARRAY type. Two-way retrieval based on vector search and full-text search.全文检索的详细内容请参见如何使用AnalyticDB PostgreSQL 版实现“一站式全文检索”业务。 For information about how structured fields accelerate queries, see the "How hybrid search works" section of this topic. The following examples demonstrate how to perform hybrid search by using semi-structured field filtering and how to perform two-way retrieval based on vector search and full-text search.

**Use semi-structured field filtering in hybrid search**

Assume that a securities company has a database named **stock_analysis_chunks** that contains stock analysis articles. The following table describes the fields that are contained in the database.

| Field | Data type | Description |
|---|---|---|
| id | serial | The serial number. |
| chunk | varchar(1024) | The text chunk that is a part of the stock analysis article. |
| release time _ | timestamp | The release time of the stock analysis article. |
| stock id list _ _ | char(10)[] | The IDs of the stocks that are involved in the stock analysis article. |
| url | varchar(1024) | The URL of the article to which the text chunk belongs. |
| feature | real[] | The embedding vector of the text block. |

1. Create a text database table named **stock_analysis_chunks**.

```
CREATE TABLE stock_analysis_chunks (
    id serial primary key,
    chunk varchar(1024),
    release_time timestamp,
    stock_id_list integer[],
    url varchar(1024),
    feature real[]
) distributed by (id);
```

2. Set the storage mode of the vector column to PLAIN.

```
ALTER TABLE stock_analysis_chunks ALTER COLUMN feature SET STORAGE PLAIN;
```

3. Create a vector index for the vector column.

```
CREATE INDEX ON stock_analysis_chunks USING ann(feature) WITH (dim=1536, distancemeasure=cosine, hnsw_m=64, pq_enable=1);
```

4. Create indexes for the structured and semi-structured columns associated with hybrid
search.

```
-- Create a B-tree index for the structured column. CREATE INDEX ON stock_analysis_chunks(release_time); -- Create a GIN index for the semi-structured column. CREATE INDEX ON stock_analysis_chunks USING gin(stock_id_list);
```

5. Collect statistics.

```
ANALYZE stock_analysis_chunks;
```

6. Perform hybrid search.
To query the stock analysis articles that were released within the last month and contain specific text content, execute the following statement:

```
SELECT id, url, cosine_similarity(feature, array[1.0, 2.0, ..., 1536.0]::real[]) as s core FROM stock_analysis_chunks WHERE release_time >= '2023-07-18 00:00:00' AND release_time <= '2023-08-18 00:00:00' AND stock_id_list @> ARRAY['BABA', 'AAPL', 'MSFT', 'AMZN'] ORDER BY feature <=> array[1.0, 2.0, ..., 1536.0]::real[] LIMIT 10;
```

**Two-way retrieval based on vector search and full-text search**

Two-way retrieval allows you to retrieve data by using vector search and full-text search at the same time. In most cases, the vector search method alone can achieve a high recall rate for vector similarity retrieval. However, inappropriate embedding models or complex queries may cause generated vectors to be far away from the data to be retrieved. In this case, the use of the vector search method alone cannot achieve the desired effect. To increase the recall rate, you can use the two-way retrieval method. This method retrieves data by using vector search and full-text search at the same time, and then refines the initial query results by ranking, filtering, and aggregating the retrieved vectors. AnalyticDB for PostgreSQL supports both high-performance vector search and high-performance full-text search, which allows you to achieve two-way retrieval of vector and text data. AnalyticDB for PostgreSQL allows you to use two one-way searches (vector search and fulltext search) in a single query to implement two-way retrieval. Example:
1. Create a table.

```
-- vector: the vector column. to_tsvector: the full-text tokenizer column. CREATE TABLE IF NOT EXISTS documents(
                id TEXT,
                docname TEXT,
                title TEXT,
                vector real[],
                text TEXT,
                to_tsvector TSVECTOR);
```

2. Set the storage mode of the vector column to PLAIN.

```
ALTER TABLE documents ALTER COLUMN vector SET STORAGE PLAIN;
```

3. Create a vector index for the vector column.

```
CREATE INDEX ON documents USING ann(vector) WITH (dim=1024, distancemeasure=cosine, h nsw_m=64, pq_enable=1);
```

4. Create a GIN index for the full-text tokenizer column.

```
CREATE INDEX ON documents USING gin(to_tsvector);
```

5. Create a dependency function.

```
CREATE OR REPLACE FUNCTION public.to_tsquery_from_text(txt text, lang regconfig DEFAU LT 'english'::regconfig)
 RETURNS tsquery
 LANGUAGE sql
 IMMUTABLE STRICT
AS $function$ SELECT to_tsquery(lang, COALESCE(string_agg(split_part(word, ':', 1), '
| '), '')) FROM (SELECT unnest(string_to_array(to_tsvector(lang, txt)::text, ' ')) AS
word) AS words_only;$function$
```

6. Perform two-way retrieval.

```
 WITH combined AS (
```

`(`

```
     SELECT
        id,
        docname,
        text,
        cosine_similarity(densevec,array{embedding}::real[]) AS similarity,
        1 as source
     FROM
        documents
     ORDER BY vector <=> array[10,2.0,..., 1024.0]
     LIMIT 10
```

`)`

```
   UNION ALL
```

`(`

```
     SELECT
        id,
        docname,
        text,
        ts_rank(to_tsvector, to_tsquery_from_text('{query.query}', 'zh_cn'), 32) as s
imilarity,
        2 as source
     FROM
        documents
     WHERE to_tsvector@@to_tsquery_from_text('{query.query}', 'zh_cn')
     ORDER BY similarity desc
     LIMIT 10
```

`)` `)`

```
SELECT id, docname, title, text, MAX(similarity) as similarity,
                BIT_OR(source) as source
                FROM combined
                GROUP BY id
                ORDER BY similarity DESC;
```

In the `UNION` clause, the first part uses vector search to retrieve 10 rows of data and the second part uses full-text search to retrieve 10 rows of data. Then, the data results are deduplicated based on the `id` column. Finally, the preceding two-way retrieval statement returns 20 or fewer rows of data.

### Performance tests for vector

**analysis**

This topic describes performance tests for vector analysis in AnalyticDB for PostgreSQL.

**Test environment**

To prevent errors caused by network fluctuations, make sure that an AnalyticDB for PostgreSQL instance and an Elastic Compute Service (ECS) instance are deployed in the same virtual private cloud (VPC).

**AnalyticDB for PostgreSQL specifications**

| Engine version | Node specifications of High- performance Edition | Number of compute nodes | Storage capacity of compute nodes | Storage type of compute nodes |
|---|---|---|---|---|
| v6.6.1.0 | 16C64G | 4 | 1000 GB | PL1 Enterprise SSD (ESSD) |
|   | 8C32G |   |   |   |
|   | 4C16G |   |   |   |

**ECS specifications**

| CPU | Memory | Disk storage |
|---|---|---|
| 16 cores | 32 GB | 2 TB |

**Preparations**

**Prepare a test environment**

1. Install Python 3.8 or later on your on-premises device.
2. Download the ann-benchmarks test tool of AnalyticDB for PostgreSQL to your on-premises
device. Click ann-benchmarks to obtain the installation package.
3. Run the following command to install the dependencies of the ann-benchmarks test tool:

```
pip install -r requirements.txt
```

4. Install Docker of a version later than 20. For more information, see Install Docker Desktop
on Linux.
5. Run the following command to build a test image:

```
python install.py --proc 4 --algorithm adbpg
```

**Prepare a test dataset**

Download a dataset and store the dataset in the data directory of the ann-benchmarks project.

| Dataset | Numbe r of dimensi ons | Number of samples | Metric function | Dataset parameter | Download link |
|---|---|---|---|---|---|
| GIST | 960 | 1,000,000 | L2 similarity | gist-960-euclidean | GIST |
| SIFT-10M | 128 | 10,000,000 | L2 similarity | sift-128-euclidean | SIFT-10M |
| SIFT-100M | 128 | 100,000,000 | L2 similarity | sift100m-128-euclidean | SIFT-100M |
| Deep | 96 | 10,000,000 | Cosine similarity | deep-image-96-angular | Deep |
| Cohere | 768 | 1,000,000 | L2 similarity | cohere-768-euclidean | Cohere |
| Dbpedia | 1536 | 1,000,000 | Cosine similarity | dbpedia-openai-1000k- angular | Dbpedia |
| Glove | 200 | 1,180,000 | Cosine similarity | glove-200-angular | Glove |

**Test procedure**

**Step 1: Configure the connection information of the test tool**

Enter configuration information in the `ann_benchmarks/algorithms/adbpg/module.py` file of the test tool.

```bash
# The internal endpoint of the AnalyticDB for PostgreSQL instance.
self._host = 'gp-bp10ofhzg2z****-master.gpdb.rds.aliyuncs.com'
# The port number of the AnalyticDB for PostgreSQL instance.
self._port = 5432
# The database name of the AnalyticDB for PostgreSQL instance.
self._dbname = '<database_name>'
# The database account of the AnalyticDB for PostgreSQL instance.
self._user = '<user_name>'
# The password of the database account.
self._password = '<your_password>'
```

**Step 2: Configure test parameters**

Use the test dataset to edit the `ann_benchmarks/algorithms/adbpg/config.yml` file of the test tool.

```
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 12}]
        query_args: [[
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 1},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 5},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 10},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 15},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 20},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 25},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 30},
        {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 50}]]
```

`arg_groups` : the parameters related to index creation. For information about how to create a vector index, see Create a vector index.

| Parameter | Description |
|---|---|
| M | The M parameter that is used to create a Hierarchical Navigable Small World (HNSW) index. Greater values indicate longer construction time and higher construction precision. |

| efConstruction | The parameter that is used to determine the search quality. |   |   |
|---|---|---|---|
| parallel build _ | The parallelism that is used to create the index. In most cases, set this parameter to the number of CPU cores of compute nodes. |   |   |
| external storage _ | The policy that is used to cache indexes. Valid values: 1: mmap. 0: shared buffer. _ |   |   |
| pq enable _ | Specifies whether to enable the product quantization (PQ) feature. Valid values: 1: yes. 0: no. |   |   |
| pq segments _ | The number of compute nodes that are used for PQ. In most cases, set this parameter to the number of dimensions divided by 8 . |   |   |
|   |   | number of dimensions |   |

|   | divided by 8 |
|---|---|

`query_args` : the search-related parameters.

| Parameter | Description |
|---|---|
| ef search _ | The number of nearest neighbors that are used for HNSW index search. |
| max scan points _ _ | The maximum number of samples examined in a scan. |
| pq amp _ | The PQ amplification factor. If you do not enable the PQ feature, this parameter does not take effect. |
| parallel | The number of concurrent queries. This parameter takes effect only in batch mode. |

During the test, you can modify the preceding parameters to ensure a 95% recall rate. AnalyticDB for PostgreSQL provides the following reference configurations for the preceding test datasets. You can select the parameter configuration for a specific test dataset.

```bash
# for sift 128 10m
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
module:annbenchmarksalgorithmsadbpg
```

```bash
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 700, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 700, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 700, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 700, p q_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 700, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 700, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 700, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 700, p q_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 700, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 700, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 700, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 700, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 700, p q_amp: 10, parallel: 50}]]
# for gist 960
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 120}]
        query_args: [[ {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 2000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 25}, {ef_search: 4 00, maxscanpoints: 2000, pqamp: 10, parallel: 30}, {efsearch: 400, maxscanpoints:
```

`,` `_` `_p`

```
,pq_
```

`p` `,``p`

```
},{
```

`_` `,` `_` `_p`

```bash
2000, pq_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 120}]
        query_args: [[ {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 2000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 2000, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 120}]
        query_args: [[ {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 2000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 2000, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 2000, pq_amp: 10, parallel: 50}]]
# for deep 96
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 12}]
        query_args: [[ {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1200, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1200, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 12}]
        query_args: [[ {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1200, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1200, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 50}]]
      wopq_sb:
```

```bash
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 12}]
        query_args: [[ {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1200, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1200, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1200, pq_amp: 10, parallel: 50}]]
# for sift 128 100M
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1800, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1800, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1800, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1800, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 16}]
        query_args: [[ {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 1}
, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 5}, {ef_search: 400, ma x_scan_points: 1800, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel : 20}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 25}, {ef_search: 4 00, max_scan_points: 1800, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 1800, pq_amp: 10, parallel: 50}]]
# for glove 200
```

```bash
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 25}]
        query_args: [[ {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 1
}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 5}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 30 000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, pa rallel: 20}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 25}, {ef_se arch: 400, max_scan_points: 30000, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan _points: 30000, pq_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 25}]
        query_args: [[ {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 1
}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 5}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 30 000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, pa rallel: 20}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 25}, {ef_se arch: 400, max_scan_points: 30000, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan _points: 30000, pq_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 25}]
        query_args: [[ {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 1
}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 5}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 30 000, pq_amp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, pa rallel: 20}, {ef_search: 400, max_scan_points: 30000, pq_amp: 10, parallel: 25}, {ef_se arch: 400, max_scan_points: 30000, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan _points: 30000, pq_amp: 10, parallel: 50}]]
# for cohere 768
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 96}] [[{f
```

`h` `i``t`

```
lll
```

`1}`

```bash
        query_args: [[ {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 600, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 600, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 600, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 600, p q_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 96}]
        query_args: [[ {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 600, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 600, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 600, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 600, p q_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 96}]
        query_args: [[ {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 600, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 600, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 600, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 600, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 600, p q_amp: 10, parallel: 50}]]
# for dbpedia 1536
float:
  any:
  - base_args: ['@metric']
    constructor: ADBPG
    disabled: false
    docker_tag: ann-benchmarks-adbpg
    module: ann_benchmarks.algorithms.adbpg
    name: adbpg
    run_groups:
      pq_mmap:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
1, pq_enable: 1, pq_segments: 192}]
        query_args: [[ {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 425, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 425, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 425, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 425, p q_amp: 10, parallel: 50}]]
      pq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 1, pq_segments: 192}]
        query_args: [[ {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s canpoints:425 pqamp:10 parallel:10} {efsearch:400 maxscanpoints:425 pqa
```

```
can_points: 425, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 425, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 425, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 425, p q_amp: 10, parallel: 50}]]
      wopq_sb:
        arg_groups: [{M: 64, efConstruction: 600, parallel_build: 16, external_storage:
0, pq_enable: 0, pq_segments: 192}]
        query_args: [[ {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 1},
{ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 5}, {ef_search: 400, max_s can_points: 425, pq_amp: 10, parallel: 10}, {ef_search: 400, max_scan_points: 425, pq_a mp: 10, parallel: 15}, {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 20} , {ef_search: 400, max_scan_points: 425, pq_amp: 10, parallel: 25}, {ef_search: 400, ma x_scan_points: 425, pq_amp: 10, parallel: 30}, {ef_search: 400, max_scan_points: 425, p q_amp: 10, parallel: 50}]]
```

**Step 3: Test the search recall rate**

After you configure the preceding parameters, run the following command to test the recall rate:

```
nohup python run.py --algorithm adbpg --dataset <Dataset> --runs 1 --timeout 990000
> annbenchmark_deep.log 2>&1 &
```

**Note**

Replace the value of the dataset parameter with the actual test dataset. After the test is complete, run the following command to query the recall rate test result:

```
python plot.py --dataset <Dataset> --recompute
```

Sample output:

```
0: ADBPG(m=64, ef_construction=600, ef_search=400, max_scan_point=500, pq_amp=10) recall: 0.963 qps: 126.200 1: ADBPG(m=64, ef_construction=600, ef_search=400, max_scan_point=1000, pq_amp=10) recall: 0.992 qps: 122.665
```

Check whether the recall rate meets your business requirements. If not, modify the parameters and re-execute the test.

**Step 4: Test the search performance**

After you obtain a recall rate that meets your business requirements, you can perform performance tests in the same manner that you perform the recall rate test. You must enable the batch mode to check the concurrency performance.

```
nohup python run.py --algorithm adbpg --dataset <Dataset> --runs 1 --timeout 990000 -batch > annbenchmark_deep.log 2>&1 &
```

After the test is complete, open the `annbenchmark_deep.log` file to check the queries per second (QPS), average response time (RT), and P99 RT parameters based on different concurrency conditions.

```
2023-12-20 17:31:39,297 - INFO - query using 25 parallel worker 0 cost 9.50 s, qps 315.92, mean rt 0.00317, p99 rt 0.00951 2023-12-20 17:31:49,097 - INFO - QPS: 7653.155 2023-12-20 17:31:49,113 - INFO - query using 30 parallel worker 0 cost 13.87 s, qps 216.36, mean rt 0.00462, p99 rt 0.04298 2023-12-20 17:32:03,260 - INFO - QPS: 6361.819 2023-12-20 17:32:03,281 - INFO - query using 50 parallel worker 0 cost 20.78 s, qps 144.36, mean rt 0.00693, p99 rt 0.02735 2023-12-20 17:32:24,385 - INFO - QPS: 7107.920
```

**Test results**

This section describes the performance test results of different datasets based on different AnalyticDB for PostgreSQL vector database configurations. In the performance tests, the recall rate is set to 95% and the top 10 search results are obtained. The following table describes the index creation modes.

| Index creation mode | Description | Applicable scenario |
|---|---|---|
| PQ + mmap | Uses the mmap policy to cache and persistently store vector indexes and the PQ method to compress vector codes and accelerate vector computing. | Scenarios that involve more than 500,000 data entries and do not require data updates or deletes. |
| PQ + shared buffer _ | Uses the shared buffer policy of _ PostgreSQL to cache vector indexes and the PQ method to compress vector codes and accelerate vector computing. | Scenarios that involve more than 500,000 data entries and require data updates and deletes. |
| noPQ + shared buffer _ | Uses the shared buffer policy of _ PostgreSQL to cache vector indexes, and does not use the PQ method to compress vector codes and accelerate vector computing. | Scenarios that involve fewer than 500,000 data entries. |

**Instance specifications: 16 cores and 64 GB memory × 4**

**compute nodes**

**Dataset: GIST L2 (960 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 261 | 1 | 242 | 3 | 4 |
|   | 5 | 1068 | 4 | 6 |
|   | 10 | 1673 | 5 | 7 |
|   | 15 | 2158 | 6 | 7 |
|   | 20 | 2492 | 7 | 13 |
|   | 25 | 2405 | 9 | 19 |
|   | 30 | 2423 | 11 | 24 |
|   | 50 | 2453 | 19 | 43 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 505 | 1 | 161 | 5 | 7 |
|   | 5 | 771 | 5 | 8 |
|   | 10 | 1111 | 8 | 10 |
|   | 15 | 1380 | 10 | 12 |
|   | 20 | 1395 | 13 | 23 |
|   | 25 | 1422 | 16 | 31 |
| > Document Version | : 20260828 17 |   |   |   |

|   | 30 | 1412 | 20 | 39 |
|---|---|---|---|---|
|   | 50 | 1450 | 34 | 70 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 2000` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1102 | 1 | 130 | 7 | 10 |
|   | 5 | 425 | 11 | 14 |
|   | 10 | 678 | 14 | 16 |
|   | 15 | 901 | 16 | 19 |
|   | 20 | 963 | 20 | 31 |
|   | 25 | 979 | 24 | 38 |
|   | 30 | 978 | 30 | 48 |
|   | 50 | 969 | 51 | 98 |

**Dataset: Deep1B cosine (96 × 10,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|

| 1515 | 1 | 451 | 2 | 2 |
|---|---|---|---|---|
|   | 5 | 2279 | 2 | 3 |
|   | 10 | 4059 | 2 | 5 |
|   | 15 | 6274 | 2 | 5 |
|   | 20 | 8198 | 2 | 5 |
|   | 25 | 8347 | 3 | 6 |
|   | 30 | 8411 | 3 | 8 |
|   | 50 | 8178 | 6 | 22 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2824 | 1 | 361 | 2 | 3 |
|   | 5 | 1439 | 3 | 4 |
|   | 10 | 2261 | 4 | 5 |
|   | 15 | 2958 | 5 | 6 |
|   | 20 | 3164 | 6 | 11 |
|   | 25 | 3168 | 7 | 15 |
|   | 30 | 3170 | 9 | 19 |
| > Document Version | : 20260828 17 |   |   |   |

|   | 50 | 3156 | 15 | 36 |
|---|---|---|---|---|

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 1200`

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 3141 | 1 | 423 | 2 | 2 |
|   | 5 | 1240 | 3 | 4 |
|   | 10 | 2453 | 4 | 4 |
|   | 15 | 3144 | 4 | 6 |
|   | 20 | 3322 | 6 | 11 |
|   | 25 | 3332 | 7 | 15 |
|   | 30 | 3350 | 8 | 19 |
|   | 50 | 3347 | 14 | 35 |

**Dataset: SIFT L2 (128 × 100,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 16
```

Search parameters: `ef_search: 400, max_scan_points: 2100, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 441 | 2 | 6 |
|   | 5 | 2222 | 2 | 6 |

| nalyticDB for MySQ | AnalyticDB for PostgreSQL User L uide·Vector analysi |   |   |   |
|---|---|---|---|---|
| 8805 |   |   |   |   |
|   | 10 | 3528 | 2 | 7 |
|   | 15 | 4679 | 3 | 8 |
|   | 20 | 5358 | 3 | 9 |
|   | 25 | 5426 | 4 | 10 |
|   | 30 | 5527 | 5 | 15 |
|   | 50 | 5904 | 8 | 30 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 16
```

Search parameters: `ef_search: 400, max_scan_points: 2100, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 14763 | 1 | 282 | 3 | 4 |
|   | 5 | 1180 | 4 | 5 |
|   | 10 | 1769 | 5 | 7 |
|   | 15 | 2298 | 6 | 8 |
|   | 20 | 2438 | 8 | 14 |
|   | 25 | 2510 | 9 | 18 |
|   | 30 | 2472 | 12 | 22 |
|   | 50 | 2467 | 20 | 42 |

**Dataset: GloVe cosine (200 × 1,180,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 378 | 1 | 174 | 5 | 8 |
|   | 5 | 905 | 5 | 7 |
|   | 10 | 1431 | 6 | 9 |
|   | 15 | 1891 | 7 | 9 |
|   | 20 | 1921 | 10 | 21 |
|   | 25 | 1880 | 13 | 26 |
|   | 30 | 1862 | 15 | 32 |
|   | 50 | 1998 | 24 | 50 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 83 | 11 | 14 |
|   | 5 | 351 | 14 | 20 |
|   | 10 | 495 | 20 | 25 |

| 715 |   |   |   |   |
|---|---|---|---|---|
|   | 15 | 635 | 23 | 29 |
|   | 20 | 628 | 31 | 50 |
|   | 25 | 613 | 40 | 67 |
|   | 30 | 605 | 49 | 83 |
|   | 50 | 576 | 86 | 151 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 0, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 891 | 1 | 52 | 18 | 24 |
|   | 5 | 233 | 21 | 30 |
|   | 10 | 335 | 29 | 45 |
|   | 15 | 430 | 34 | 48 |
|   | 20 | 437 | 45 | 77 |
|   | 25 | 426 | 58 | 101 |
|   | 30 | 416 | 71 | 124 |
|   | 50 | 405 | 123 | 215 |

**Dataset: Cohere L2 (768 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 285 | 1 | 317 | 2 | 3 |
|   | 5 | 1450 | 2 | 4 |
|   | 10 | 2177 | 4 | 5 |
|   | 15 | 2812 | 4 | 6 |
|   | 20 | 3275 | 5 | 9 |
|   | 25 | 3485 | 6 | 14 |
|   | 30 | 3657 | 7 | 18 |
|   | 50 | 3619 | 13 | 35 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 223 | 4 | 4 |
|   | 5 | 996 | 4 | 6 |
|   | 10 | 1548 | 6 | 7 |
|   | 15 | 2006 | 7 | 8 |

| 518 |   |   |   |   |
|---|---|---|---|---|
|   | 20 | 2141 | 8 | 15 |
|   | 25 | 2081 | 11 | 22 |
|   | 30 | 2160 | 13 | 27 |
|   | 50 | 2039 | 24 | 51 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 0, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 701 | 1 | 357 | 2 | 3 |
|   | 5 | 641 | 7 | 9 |
|   | 10 | 1019 | 9 | 10 |
|   | 15 | 1330 | 10 | 13 |
|   | 20 | 1431 | 13 | 20 |
|   | 25 | 1437 | 16 | 26 |
|   | 30 | 1449 | 20 | 33 |
|   | 50 | 1445 | 34 | 66 |

**Dataset: Dbpedia cosine (1,536 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 1, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1120 | 1 | 122 | 7 | 8 |
|   | 5 | 548 | 8 | 14 |
|   | 10 | 727 | 12 | 16 |
|   | 15 | 940 | 15 | 16 |
|   | 20 | 1011 | 18 | 30 |
|   | 25 | 1022 | 23 | 38 |
|   | 30 | 1019 | 28 | 50 |
|   | 50 | 1022 | 47 | 93 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1642 | 1 | 110 | 8 | 9 |
|   | 5 | 512 | 9 | 16 |
|   | 10 | 666 | 14 | 18 |
|   | 15 | 830 | 17 | 18 |
|   | 20 | 911 | 21 | 32 |
|   | 25 | 919 | 26 | 41 |
| 85 | > Document Version: 2026082 |   |   |   |

|   | 30 | 922 | 31 | 52 |
|---|---|---|---|---|
|   | 50 | 915 | 53 | 97 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 16,`

```
external_storage: 0, pq_enable: 0, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1130 | 1 | 308 | 2 | 6 |
|   | 5 | 575 | 7 | 9 |
|   | 10 | 939 | 10 | 11 |
|   | 15 | 1197 | 11 | 13 |
|   | 20 | 1295 | 14 | 22 |
|   | 25 | 1323 | 17 | 28 |
|   | 30 | 1328 | 21 | 36 |
|   | 50 | 1315 | 37 | 68 |

**Instance specifications: 8 cores and 32 GB memory × 4**

**compute nodes**

**Dataset: GIST L2 (960 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 681 | 1 | 252 | 3 | 5 |
|   | 5 | 868 | 5 | 7 |
|   | 10 | 1312 | 7 | 11 |
|   | 15 | 1305 | 11 | 22 |
|   | 20 | 1343 | 14 | 30 |
|   | 25 | 1323 | 18 | 37 |
|   | 30 | 1352 | 21 | 47 |
|   | 50 | 1305 | 37 | 70 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1349 | 1 | 123 | 7 | 10 |
|   | 5 | 423 | 11 | 13 |
|   | 10 | 582 | 16 | 27 |
|   | 15 | 611 | 24 | 44 |
|   | 20 | 603 | 32 | 59 |
|   | 25 | 605 | 40 | 76 |
| 87 | > Document Version: 2026082 |   |   |   |

|   | 30 | 596 | 49 | 99 |
|---|---|---|---|---|
|   | 50 | 594 | 83 | 151 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 2000` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2158 | 1 | 92 | 10 | 11 |
|   | 5 | 365 | 13 | 15 |
|   | 10 | 532 | 18 | 28 |
|   | 15 | 546 | 26 | 44 |
|   | 20 | 558 | 35 | 63 |
|   | 25 | 554 | 44 | 78 |
|   | 30 | 556 | 53 | 94 |
|   | 50 | 543 | 91 | 170 |

**Dataset: Deep1B cosine (96 × 10,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|

| 2781 | 1 | 559 | 1 | 2 |
|---|---|---|---|---|
|   | 5 | 2340 | 2 | 3 |
|   | 10 | 3973 | 2 | 4 |
|   | 15 | 4087 | 3 | 8 |
|   | 20 | 3705 | 5 | 18 |
|   | 25 | 3966 | 6 | 18 |
|   | 30 | 4083 | 7 | 20 |
|   | 50 | 4163 | 11 | 39 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 5658 | 1 | 333 | 2 | 3 |
|   | 5 | 1196 | 4 | 5 |
|   | 10 | 1685 | 5 | 11 |
|   | 15 | 1740 | 8 | 18 |
|   | 20 | 1745 | 11 | 25 |
|   | 25 | 1754 | 14 | 30 |
|   | 30 | 1755 | 17 | 38 |
| 89 | > Document Version: 2026082 |   |   |   |

|   | 50 | 1733 | 28 | 64 |
|---|---|---|---|---|

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 1200` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 6456 | 1 | 354 | 2 | 3 |
|   | 5 | 1292 | 3 | 4 |
|   | 10 | 1758 | 5 | 11 |
|   | 15 | 1779 | 8 | 18 |
|   | 20 | 1767 | 11 | 26 |
|   | 25 | 1778 | 13 | 33 |
|   | 30 | 1768 | 16 | 40 |
|   | 50 | 1770 | 28 | 64 |

**Dataset: SIFT L2 (128 × 10,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 16
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 523 | 1 | 2 |

| nalyticDB for Postgr ide·Vector analysis | eSQL User G AnalyticDB for MySQ |   |   |   |
|---|---|---|---|---|
| 1613 |   |   |   |   |
|   | 5 | 2568 | 1 | 3 |
|   | 10 | 4500 | 2 | 4 |
|   | 15 | 5174 | 2 | 6 |
|   | 20 | 5045 | 3 | 11 |
|   | 25 | 4846 | 5 | 16 |
|   | 30 | 4873 | 6 | 23 |
|   | 50 | 4445 | 11 | 32 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 4023 | 1 | 345 | 2 | 3 |
|   | 5 | 1169 | 4 | 5 |
|   | 10 | 1601 | 6 | 12 |
|   | 15 | 1632 | 9 | 21 |
|   | 20 | 1630 | 12 | 27 |
|   | 25 | 1604 | 15 | 33 |
|   | 30 | 1579 | 18 | 45 |
|   | 50 | 1536 | 32 | 53 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 5164 | 1 | 371 | 2 | 3 |
|   | 5 | 1238 | 3 | 5 |
|   | 10 | 1605 | 6 | 12 |
|   | 15 | 1615 | 9 | 20 |
|   | 20 | 1531 | 12 | 31 |
|   | 25 | 1585 | 15 | 36 |
|   | 30 | 1531 | 19 | 45 |
|   | 50 | 1517 | 32 | 71 |

**Dataset: GloVe cosine (200 × 1,180,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 150 | 6 | 7 |
|   | 5 | 638 | 7 | 9 |

| nalyticDB for Postgr ide·Vector analysis |   |   |   |   |
|---|---|---|---|---|
| 884 |   |   |   |   |
|   | 10 | 894 | 11 | 20 |
|   | 15 | 898 | 16 | 31 |
|   | 20 | 890 | 22 | 45 |
|   | 25 | 894 | 27 | 54 |
|   | 30 | 877 | 34 | 66 |
|   | 50 | 874 | 57 | 110 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1537 | 1 | 75 | 13 | 16 |
|   | 5 | 250 | 19 | 25 |
|   | 10 | 321 | 30 | 51 |
|   | 15 | 310 | 48 | 83 |
|   | 20 | 301 | 66 | 115 |
|   | 25 | 289 | 86 | 153 |
|   | 30 | 274 | 109 | 192 |
|   | 50 | 252 | 197 | 346 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 0, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1804 | 1 | 41 | 23 | 34 |
|   | 5 | 164 | 30 | 47 |
|   | 10 | 216 | 46 | 82 |
|   | 15 | 211 | 70 | 123 |
|   | 20 | 209 | 95 | 168 |
|   | 25 | 209 | 119 | 207 |
|   | 30 | 207 | 144 | 254 |
|   | 50 | 200 | 248 | 434 |

**Dataset: Cohere L2 (768 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
|   | 1 | 323 | 2 | 3 |
|   | 5 | 1153 | 3 | 5 |
|   | 10 | 1767 | 5 | 9 |

| nalyticDB for Postgr ide·Vector analysis |   |   |   |   |
|---|---|---|---|---|
| 688 |   |   |   |   |
|   | 15 | 1801 | 7 | 16 |
|   | 20 | 1921 | 9 | 22 |
|   | 25 | 1886 | 12 | 33 |
|   | 30 | 1820 | 16 | 38 |
|   | 50 | 1900 | 25 | 72 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1224 | 1 | 198 | 5 | 7 |
|   | 5 | 561 | 8 | 10 |
|   | 10 | 838 | 11 | 19 |
|   | 15 | 819 | 17 | 33 |
|   | 20 | 835 | 23 | 42 |
|   | 25 | 839 | 29 | 52 |
|   | 30 | 835 | 35 | 68 |
|   | 50 | 834 | 59 | 107 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters:

| M: 64, efConstruction: 600, parallel build: 8, external storage: 0, pq enable: 0, _ _ _ |   |
|---|---|

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1411 | 1 | 130 | 7 | 8 |
|   | 5 | 532 | 8 | 10 |
|   | 10 | 777 | 12 | 20 |
|   | 15 | 795 | 18 | 32 |
|   | 20 | 798 | 24 | 46 |
|   | 25 | 810 | 30 | 57 |
|   | 30 | 812 | 36 | 67 |
|   | 50 | 815 | 61 | 108 |

**Dataset: Dbpedia cosine (1,536 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 1, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2214 | 1 | 125 | 7 | 9 |
|   | 5 | 374 | 12 | 15 |
|   | 10 | 506 | 18 | 30 |
|   | 15 | 504 | 28 | 51 |

|   | 20 | 509 | 38 | 69 |
|---|---|---|---|---|
|   | 25 | 500 | 49 | 90 |
|   | 30 | 507 | 58 | 104 |
|   | 50 | 509 | 97 | 169 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 7651 | 1 | 87 | 10 | 12 |
|   | 5 | 314 | 14 | 18 |
|   | 10 | 443 | 21 | 33 |
|   | 15 | 448 | 32 | 53 |
|   | 20 | 445 | 44 | 76 |
|   | 25 | 444 | 55 | 99 |
|   | 30 | 447 | 66 | 119 |
|   | 50 | 450 | 110 | 192 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 8,`

```
external_storage: 0, pq_enable: 0, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2206 | 1 | 128 | 7 | 8 |
|   | 5 | 484 | 9 | 11 |
|   | 10 | 729 | 12 | 19 |
|   | 15 | 748 | 19 | 34 |
|   | 20 | 782 | 24 | 44 |
|   | 25 | 783 | 31 | 57 |
|   | 30 | 794 | 37 | 65 |
|   | 50 | 787 | 62 | 122 |

**Instance specifications: 4 cores and 16 GB memory × 4**

**compute nodes**

**Dataset: GIST L2 (960 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2014 | 1 | 237 | 3 | 5 |
|   | 5 | 630 | 7 | 13 |
|   | 10 | 645 | 15 | 27 |
|   | 15 | 650 | 22 | 44 |

|   | 20 | 642 | 30 | 57 |
|---|---|---|---|---|
|   | 25 | 634 | 39 | 70 |
|   | 30 | 622 | 47 | 98 |
|   | 50 | 621 | 79 | 147 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 120
```

Search parameters: `ef_search: 400, max_scan_points: 2000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 2934 | 1 | 119 | 7 | 11 |
|   | 5 | 275 | 17 | 29 |
|   | 10 | 292 | 33 | 60 |
|   | 15 | 282 | 52 | 93 |
|   | 20 | 286 | 69 | 121 |
|   | 25 | 284 | 87 | 154 |
|   | 30 | 280 | 106 | 188 |
|   | 50 | 276 | 180 | 328 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 2000` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 4468 | 1 | 87 | 11 | 13 |
|   | 5 | 244 | 20 | 32 |
|   | 10 | 263 | 37 | 64 |
|   | 15 | 261 | 57 | 100 |
|   | 20 | 269 | 73 | 130 |
|   | 25 | 268 | 92 | 163 |
|   | 30 | 267 | 111 | 196 |
|   | 50 | 266 | 188 | 327 |

**Dataset: Deep1B cosine (96 × 10,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 1, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 6696 | 1 | 520 | 1 | 2 |
|   | 5 | 1679 | 2 | 5 |
|   | 10 | 1832 | 5 | 12 |
|   | 15 | 1908 | 7 | 18 |
|   | 20 | 1899 | 10 | 28 |

|   | 25 | 1920 | 12 | 33 |
|---|---|---|---|---|
|   | 30 | 1910 | 15 | 39 |
|   | 50 | 1904 | 26 | 66 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 12
```

Search parameters: `ef_search: 400, max_scan_points: 1200, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 11677 | 1 | 302 | 3 | 4 |
|   | 5 | 814 | 6 | 11 |
|   | 10 | 858 | 11 | 23 |
|   | 15 | 870 | 17 | 34 |
|   | 20 | 870 | 22 | 48 |
|   | 25 | 864 | 28 | 57 |
|   | 30 | 866 | 34 | 70 |
|   | 50 | 848 | 58 | 119 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 1200` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 14657 | 1 | 301 | 3 | 4 |
|   | 5 | 821 | 6 | 11 |
|   | 10 | 885 | 11 | 22 |
|   | 15 | 890 | 16 | 34 |
|   | 20 | 898 | 22 | 45 |
|   | 25 | 896 | 27 | 56 |
|   | 30 | 891 | 33 | 67 |
|   | 50 | 885 | 56 | 112 |

**Dataset: SIFT L2 (128 × 10,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 4,`

```
external_storage: 1, pq_enable: 1, pq_segments: 16
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 3004 | 1 | 577 | 1 | 2 |
|   | 5 | 1846 | 2 | 5 |
|   | 10 | 2085 | 4 | 12 |
|   | 15 | 2523 | 5 | 14 |
|   | 20 | 2599 | 7 | 18 |

|   | 25 | 2573 | 9 | 24 |
|---|---|---|---|---|
|   | 30 | 2349 | 12 | 35 |
|   | 50 | 2437 | 20 | 53 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 16
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 6409 | 1 | 356 | 2 | 3 |
|   | 5 | 966 | 5 | 10 |
|   | 10 | 1025 | 9 | 19 |
|   | 15 | 974 | 15 | 32 |
|   | 20 | 1041 | 19 | 39 |
|   | 25 | 1032 | 24 | 49 |
|   | 30 | 981 | 30 | 69 |
|   | 50 | 987 | 50 | 104 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 16, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0
```

Search parameters: `ef_search: 400, max_scan_points: 1000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 9058 | 1 | 365 | 2 | 4 |
|   | 5 | 960 | 5 | 10 |
|   | 10 | 938 | 10 | 21 |
|   | 15 | 961 | 15 | 32 |
|   | 20 | 1034 | 19 | 40 |
|   | 25 | 1005 | 24 | 52 |
|   | 30 | 1013 | 29 | 59 |
|   | 50 | 986 | 52 | 101 |

**Dataset: GloVe cosine (200 × 1,180,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 1, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10`

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1810 | 1 | 127 | 7 | 11 |
|   | 5 | 340 | 14 | 26 |
|   | 10 | 341 | 29 | 54 |
|   | 15 | 343 | 43 | 83 |
|   | 20 | 340 | 58 | 109 |

|   | 25 | 341 | 73 | 141 |
|---|---|---|---|---|
|   | 30 | 342 | 87 | 165 |
|   | 50 | 343 | 145 | 265 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 3234 | 1 | 72 | 13 | 19 |
|   | 5 | 167 | 29 | 52 |
|   | 10 | 158 | 62 | 115 |
|   | 15 | 172 | 82 | 167 |
|   | 20 | 147 | 135 | 237 |
|   | 25 | 143 | 174 | 306 |
|   | 30 | 140 | 213 | 374 |
|   | 50 | 128 | 390 | 663 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0, pq_segments: 25
```

Search parameters: `ef_search: 400, max_scan_points: 30000, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|

| 3571 | 1 | 40 | 24 | 35 |
|---|---|---|---|---|
|   | 5 | 104 | 47 | 87 |
|   | 10 | 98 | 101 | 186 |
|   | 15 | 95 | 156 | 279 |
|   | 20 | 96 | 210 | 368 |
|   | 25 | 96 | 260 | 458 |
|   | 30 | 96 | 310 | 544 |
|   | 50 | 96 | 542 | 933 |

**Dataset: Cohere L2 (768 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 1, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 1603 | 1 | 208 | 4 | 7 |
|   | 5 | 504 | 9 | 17 |
|   | 10 | 543 | 17 | 32 |
|   | 15 | 543 | 27 | 50 |
|   | 20 | 522 | 37 | 76 |
|   | 25 | 540 | 45 | 83 |
| > Document Version | : 20260828 20 |   |   |   |

|   | 30 | 542 | 54 | 97 |
|---|---|---|---|---|
|   | 50 | 535 | 92 | 166 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 3679 | 1 | 199 | 4 | 6 |
|   | 5 | 501 | 9 | 18 |
|   | 10 | 578 | 16 | 31 |
|   | 15 | 555 | 26 | 52 |
|   | 20 | 548 | 35 | 73 |
|   | 25 | 555 | 44 | 85 |
|   | 30 | 559 | 53 | 97 |
|   | 50 | 555 | 89 | 163 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0, pq_segments: 96
```

Search parameters: `ef_search: 400, max_scan_points: 600, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|

| 2768 | 1 | 131 | 7 | 9 |
|---|---|---|---|---|
|   | 5 | 369 | 13 | 21 |
|   | 10 | 406 | 24 | 43 |
|   | 15 | 410 | 36 | 65 |
|   | 20 | 413 | 48 | 84 |
|   | 25 | 408 | 60 | 107 |
|   | 30 | 408 | 73 | 136 |
|   | 50 | 409 | 121 | 213 |

**Dataset: Dbpedia cosine (1,536 × 1,000,000)**

**Index creation mode: PQ + mmap**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 1, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 4700 | 1 | 111 | 8 | 14 |
|   | 5 | 249 | 19 | 31 |
|   | 10 | 230 | 42 | 77 |
|   | 15 | 240 | 61 | 104 |
|   | 20 | 236 | 83 | 150 |
|   | 25 | 241 | 102 | 173 |
| > Document Version | : 20260828 20 |   |   |   |

|   | 30 | 238 | 124 | 214 |
|---|---|---|---|---|
|   | 50 | 239 | 208 | 376 |

**Index creation mode: PQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 1, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|
| 15958 | 1 | 101 | 9 | 14 |
|   | 5 | 209 | 22 | 36 |
|   | 10 | 217 | 45 | 77 |
|   | 15 | 210 | 70 | 127 |
|   | 20 | 211 | 93 | 168 |
|   | 25 | 216 | 114 | 191 |
|   | 30 | 215 | 138 | 244 |
|   | 50 | 214 | 232 | 411 |

**Index creation mode: noPQ + shared_buffer**

Index creation parameters: `M: 64, efConstruction: 600, parallel_build: 4,`

```
external_storage: 0, pq_enable: 0, pq_segments: 192
```

Search parameters: `ef_search: 400, max_scan_points: 425, pq_amp: 10` The following table describes the test results.

| Index creation time (s) | Query concurrency | QPS | Average RT (ms) | P99 RT (ms) |
|---|---|---|---|---|

| 4541 | 1 | 230 | 3 | 8 |
|---|---|---|---|---|
|   | 5 | 383 | 12 | 19 |
|   | 10 | 393 | 24 | 43 |
|   | 15 | 389 | 37 | 66 |
|   | 20 | 386 | 51 | 89 |
|   | 25 | 381 | 64 | 115 |
|   | 30 | 385 | 77 | 138 |
|   | 50 | 389 | 127 | 229 |

### Case: Build an image-based

**search system**

This topic describes how to use an AnalyticDB for PostgreSQL vector database to build an image-based search system.

**Background information**

Image-based search is commonly used in our life. If you want a beautiful dress or a pair of favorite sneakers shown on TV, you can take an image and then upload the image to Taobao to quickly find the product. If you want to know the name of a movie, you can paste a screenshot of the movie in the image search box of a search engine. Image-based search allows you to quickly find images of a person from a large number of human images. In addition to the image-based search feature that is provided by search engines, you can use the vector retrieval feature that is provided by AnalyticDB for PostgreSQL vector databases to build an image-based search system based on SQL syntax.

**Overview of image-based search**

Image-based search is also called reverse image search. It is a content-based image retrieval technique. The image-based search system can return records that are the closest in content to the image to be queried from large numbers of images. For example, if you provide an image that contains a product, the image-based search system returns images that contain a major object the same to or similar to the product. If you provide an image that contains a human face, the image-based search system returns images that share similar facial features with the human face. Image-based search relies on two core modules: Feature extraction module: extracts visual features from the source image to obtain a highdimensional feature vector. The closer the feature vector of an image is to the feature vector of the source image, the more similar the image is to the source image. Vector retrieval module: finds and returns the k records that are the closest to the query vector from large numbers of feature vectors.

**Image feature extraction**

Popular feature extraction algorithms use deep learning models such as Visual Geometry Group (VGG), ResNet, and Transformer as the backbone network and then use different methods to generate features. Three methods are commonly used to generate features: Method 1: Use the previous layer of the classification layer in a classification model such as VGG as the output features. This is the simplest method and does not produce a high recall rate in image-based search scenarios. Method 2: Perform special pooling operations such as Regional Maximum Activation of Convolutions (RMAC) and GeM on the features in the intermediate layer of a model, and then decrease dimensions of the features. Method 3: Use a specific loss function to train a pre-trained model on a dataset to extract features. For example, a product feature extraction model needs to be trained on a dataset of similar products to extract visual features of different products in a more accurate way. You can select a method that is suitable to your business scenario to extract image features and generate feature vectors.

**Vector retrieval**

Vector retrieval is also called nearest neighbor search (NNS). It finds and returns the k records that are the closest to the query vector from large numbers of feature vectors. You can calculate the distances between the query vector and all vectors in the database and then sort the distance results. However, this method is time-consuming and cannot meet requirements for large amounts of data. In actual application scenarios, approximate nearest neighbor (ANN) search is commonly used to return data that is probably nearest to the query vector in a fast but less accurate manner. You can use one of the following methods to perform ANN search: Based on locality-sensitive hashing (LSH) Based on product quantization Based on images

**Use an AnalyticDB for PostgreSQL vector database to search by**

**image**

**Step 1: Extract feature vectors**

In this example, the following tools are used: Programming language: Python 3.8. Deep learning framework: Pytorch. Dataset: CIFAR100. The dataset consists of 100 categories, each containing 600 images. Network: pre-trained SqueezeNet. SqueezeNet is lightweight and produces feature vectors of 1,000 dimensions.

**Note**

We recommend that you use Jupyter Notebook to run the following code.
1. Create a Python environment.

```bash
# We recommend that you use Anaconda to create a Python environment.
conda create -n adbpg_env python=3.8 conda activate adbpg_env pip install torchvision pip install matplotlib pip install psycopg2cffi
```

2. Download and preprocess the CIFAR100 dataset.

```java
import torch import torchvision from torchvision.transforms import (
    Compose,
    Resize,
    CenterCrop,
    ToTensor,
    Normalize
```

`)`

```
preprocess = Compose([
    Resize(256),
    CenterCrop(224),
    ToTensor(),
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
```

`])`

```json
DATA_DIRECTORY = "/Users/XXX/Desktop/vector/CIFAR" datasets = {
    "CIFAR100": torchvision.datasets.CIFAR100(DATA_DIRECTORY, transform=preprocess, d
ownload=True)
```

`}`
3. (Optional) Query the downloaded dataset.

```java
import numpy as np import matplotlib.pyplot as plt from mpl_toolkits.axes_grid1 import ImageGrid def show_images_from_full_dataset(dset, num_rows, num_cols, indices):
    im_arrays = np.take(dset.data, indices, axis=0)
    labels = map(dset.classes.__getitem__, np.take(dset.targets, indices))
    fig = plt.figure(figsize=(10, 10))
    grid = ImageGrid(
        fig,
        111,
        nrows_ncols=(num_rows, num_cols),
        axes_pad=0.3)
    for ax, im_array, label in zip(grid, im_arrays, labels):
        ax.imshow(im_array)
        ax.set_title(label)
        ax.axis("off")
dataset = datasets["CIFAR100"] show_images_from_full_dataset(dataset, 4, 8, [i for i in range(0, 32)])
```

4. Use the Squeezenet1_1 model to generate feature vectors of all images in batches and
store them in a feature vector file. In this example, `/Users/XXX/Desktop/vector/features/CIFAR100/features` is the path of the feature vector file.

```python
# Prepare data.
BATCH_SIZE = 100 dataloader = torch.utils.data.DataLoader(dataset, batch_size=BATCH_SIZE)
# Download the model.
model = torchvision.models.squeezenet1_1(pretrained=True).eval()
# Extract the feature vectors and write them to the features_file_path file.
features_file_path = "/Users/XXX/Desktop/vector/features/CIFAR100/features" feature_file = open(features_file_path, 'w') img_id = 0 for batch_number, batch in enumerate(dataloader):
    with torch.no_grad():
        batch_imgs = batch[0]  # 0: images
        batch_labels = batch[1]  # 1: labels
        vector_values = model(batch_imgs).tolist()
        for i in range(len(vector_values)):
            img_label = dataset.classes[batch_labels[i].item()]
            # print(img_label)
            feature_file.write(str(img_id) + "|" + img_label + "|")
            vector_value = vector_values[i]
            assert len(vector_value) == 1000
            for j in range(len(vector_value)):
                if j == 0:
                    feature_file.write("{")
                    feature_file.write(str(vector_value[j]) + ",")
                elif j == len(vector_value) - 1:
                    feature_file.write(str(vector_value[j]))
                    feature_file.write("}")
                else:
                    feature_file.write(str(vector_value[j]) + ",")
            feature_file.write("\n")
            img_id = img_id + 1
        print("finished extract feature vector for batch: ", batch_number)
feature_file.close()
```

The feature vectors of an image are displayed in the following format:

```
[2.67548513424756,2.186723470687866,2.376999616622925,2.3993351459503174,2.833254337310
```

`1,`

```
4.141584873199463,1.0177937746047974,2.0199387073516846,2.436871512298584,1.46583878993 80, 4,10.196249008178711,3.3932418823242188,6.087968826293945,7.661309242248535,7.660053730 098, 6,5.481011390686035,7.513026237487795,5.552321434020996,4.685927867889404,5.63507032394 92,...]
```

**Step 2: Import data to an AnalyticDB for PostgreSQL vector**

**database and query the data**

1. Create a table and then create a vector index in the table. In this example, the psycopg2cffi
library of Python is used to connect to the vector database.

**Important**

If you want to enable the vector feature for your database, 提交工单 submit a ticket.

```java
import os import psycopg2cffi
# Configure the temporary environment variables.
# os.environ["PGHOST"] = "XX.XXX.XX.XXX"
# os.environ["PGPORT"] = "XXXXX"
# os.environ["PGDATABASE"] = "adbpg_test"
# os.environ["PGUSER"] = "adbpg_test"
# os.environ["PGPASSWORD"] = "adbpg_test"
connection = psycopg2cffi.connect(
    host=os.environ.get("PGHOST", "XX.XXX.XX.XXX"),
    port=os.environ.get("PGPORT", "XXXXX"),
    database=os.environ.get("PGDATABASE", "adbpg_test"),
    user=os.environ.get("PGUSER", "adbpg_test"),
    password=os.environ.get("PGPASSWORD", "adbpg_test")
```

`)`

```bash
cursor = connection.cursor()
# Specify an SQL statement to create a table.
create_table_sql = """ CREATE TABLE IF NOT EXISTS public.image_search (
    id INTEGER NOT NULL,
    class TEXT,
    image_vector REAL[],
    PRIMARY KEY(id)
) DISTRIBUTED BY(id); """
# Specify an SQL statement to change the storage format of the vector column to PLAIN
```

`.`

```bash
alter_vector_storage_sql = """ ALTER TABLE public.image_search ALTER COLUMN image_vector SET STORAGE PLAIN; """
# Specify an SQL statement to create a vector index.
create_indexes_sql = """ CREATE INDEX ON public.image_search USING ann (image_vector) WITH (dim = '1000', hnsw _m = '100', pq_enable='0'); """
# Execute the preceding SQL statements.
cursor.execute(create_table_sql) cursor.execute(alter_vector_storage_sql) cursor.execute(create_indexes_sql) connection.commit()
```

2. Import the feature vectors of the images that are contained in the dataset to the table.

```java
import io
# Define a generator function to process the data in the file line by line.
def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
# Specify a COPY statement to import data.
copy_command = """ COPY public.image_search (id, class, image_vector) FROM STDIN WITH (DELIMITER '|'); """
# Prepare the feature vector file.
features_file_path = "/Users/XXX/Desktop/vector/features/CIFAR100/features"
# Execute the COPY statement.
modified_lines = io.StringIO(''.join(list(process_file(features_file_path)))) cursor.copy_expert(copy_command, modified_lines) connection.commit()
```

3. Search for images based on the feature vector of an image contained in the feature vector
file. In this example, the image whose ID is 4999 is used.

```python
def query_analyticdb(collection_name, vector_name, query_embedding, top_k=20):
    # Specify an SQL statement to return images whose feature vectors are the closest
to the query vector and calculate the similarity to the query vector.
    query_sql = f"""
    SELECT id, class, l2_distance({vector_name},Array{query_embedding}::real[]) AS si
milarity
    FROM {collection_name}
    ORDER BY {vector_name} <-> Array{query_embedding}::real[]
    LIMIT {top_k};
    """
    # Execute the preceding SQL statement.
    connection = psycopg2cffi.connect(
        host=os.environ.get("PGHOST", "XX.XXX.XX.XXX"),
        port=os.environ.get("PGPORT", "XXXXX"),
        database=os.environ.get("PGDATABASE", "adbpg_test"),
        user=os.environ.get("PGUSER", "adbpg_test"),
        password=os.environ.get("PGPASSWORD", "adbpg_test")
```

`)`

```python
    cursor = connection.cursor()
    cursor.execute(query_sql)
    results = cursor.fetchall()
    return results
  # Select a piece of data as the query vector.
def select_feature(file_path, expect_id):
    with open(file_path, 'r') as file:
        for line in file:
            datas = line.split('|')
            if datas[0] == str(expect_id):
                vec = '[' + datas[2][1:-2] + ']'
                return vec
    raise ValueError(f"no id = {expect_id}")
file_path = "/Users/lizhenjing/Desktop/vector/features/CIFAR100/features"
# Select an image whose ID is 4999.
query_vector = select_feature(file_path, 4999)
# Display this image.
# show_images_from_full_dataset(dataset, 1, 1, [4999], figsize=(1, 1))
# print(query_vector)
# Execute the query to display the query results.
results = query_analyticdb("image_search", "image_vector", query_vector)
```

The following figure shows the image whose ID is 4999.
4. Display the images corresponding to the query results.

**Note**

AnalyticDB for PostgreSQL vector databases provide the ANN search feature to accelerate the query.

```python
# Obtain the image IDs from the query results in the previous step.
indices = [] for item in results:
    indices.append(item[0])
print(indices)
# Display the images.
show_images_from_full_dataset(dataset, 4, 5, indices)
```

The following figures show the returned images.

### Case: Build a text semantic

**retrieval system**

AnalyticDB for PostgreSQL's vector database lets you build a text semantic retrieval system that finds documents by meaning rather than exact keyword matches. This tutorial walks through a complete example: vectorizing a 10,000-entry text corpus, indexing it in AnalyticDB for PostgreSQL, and running semantic similarity queries against it. By the end, you will have: Vectorized a real-world text corpus using a sentence embedding model Stored vectors and created an approximate nearest neighbor (ANN) index in AnalyticDB for PostgreSQL Queried the database to retrieve the most semantically similar texts This tutorial creates a table ( `public.articles` ) and an index in your database. Clean-up code is provided at the end to drop them when you are done.

**How it works**

Text semantic retrieval has two phases.

**Phase 1 — Text vectorization and index creation**

A machine learning (ML) model converts each text into a feature vector — a numeric representation that captures the text's meaning. Texts with similar meanings produce similar vectors in the embedding space. Once vectorized, texts and their feature vectors are stored in AnalyticDB for PostgreSQL, and a vector index is built to accelerate similarity queries.

**Phase 2 — Vector retrieval**

At query time, the same ML model converts the query text into a vector. AnalyticDB for PostgreSQL's vector engine then uses the index to find the stored texts whose feature vectors are most similar to the query vector and returns them ranked by similarity.

**Prerequisites**

Before you begin, ensure that you have: An AnalyticDB for PostgreSQL instance with connection credentials (host, port, database name, username, and password) Conda installed for managing Python environments Internet access to download the Quora dataset from Hugging Face

**Step 1: Set up the Python environment**

Create a dedicated Conda environment with Python 3.8 and install all required packages.

```bash
# Create a Python 3.8 virtual environment
conda create -n adbpg_text_env python=3.8
# Activate the environment
conda activate adbpg_text_env
# Install required packages
pip install psycopg2==2.9.3 pip install wget==3.2 pip install pandas==1.2.4 pip install datasets==2.12.0 sentence-transformers==2.2.2 pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
```

On macOS, if you see `Error: pg_config executable not found` when installing psycopg2, install PostgreSQL client libraries first:

```
brew install postgresql pip install psycopg2==2.9.3
```

**Step 2: Preprocess data**

This tutorial uses the Quora dataset from Hugging Face, which contains approximately 400,000 question pairs. The example loads 10,000 entries and extracts unique question texts to build the corpus.

**Download the dataset**

```python
from datasets import load_dataset dataset = load_dataset('quora', split='train[0:10000]') print(dataset[0])
```

Each entry has two fields: `questions` — contains `id` (serial numbers) and `text` (the question texts) for a pair of questions `is_duplicate` — whether the two questions have the same meaning ( `True` or `False` ) Sample output:

```json
{'questions':
     {'id': [1, 2],
      'text': ['What is the step by step guide to invest in share market in india?', 'W
hat is the step by step guide to invest in share market?']
```

`},`

```json
 'is_duplicate': False
```

`}`

**Extract feature vectors**

The following steps extract a unique list of questions, convert each to a feature vector, and save everything to a CSV file.
1. Extract all questions and remove duplicates.

```python
sentences = [] for data in dataset['questions']:
    sentences.extend(data['text'])
# Remove duplicate questions
sentences = list(set(sentences)) print('\n'.join(sentences[1:5])) print(len(sentences))
```

Sample output (unique sentence count):

```
How can I know if my spouse is cheating? Can a snake kill a rabbit? How i get hair on bald head? How can I get my name off the first page on Google search? 19413
```

2. Load the embedding model and encode the sentences. This tutorial uses `all-MiniLM-L6-`
`v2` — a lightweight sentence embedding model that produces high-quality semantic representations. It outputs 384-dimensional vectors, which determines the `dim` value used when creating the vector index in the next step.

```java
from sentence_transformers import SentenceTransformer import torch model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu') model
```

Model details:

```json
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer
model: BertModel
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'po
oling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Normalize()
```

`)` The model truncates input text beyond 256 tokens and produces 384-dimensional vectors.
3. Encode each sentence and save the results to a CSV file.

```java
import pandas as pd vectors = [] for sentence in sentences:
    vector = model.encode(sentence)
    # Format vectors as '{0.04067..., ..., -0.01296...}' for import into AnalyticDB f
or PostgreSQL
    vector_str = "{" + ", ".join(str(x) for x in vector.tolist()) + "}"
    vectors.append(vector_str)
# Generate sequential IDs
ids = [i + 1 for i in range(len(sentences))]
# Combine into a DataFrame and save
df = pd.DataFrame({'ID': ids, 'Sentences': sentences, 'Vectors': vectors}) df.to_csv('sentences_vectors.csv', index=False)
```

The output CSV ( `sentences_vectors.csv` ) has three columns: `ID` , `Sentences` , and

```
 Vectors .
```

**Step 3: Create a table and vector index**

1. Connect to the database and verify the connection.

```java
import os import psycopg2
# Set connection parameters as environment variables before running:
# os.environ["PGHOST"] = "xxx.xxx.xxx.xxx"
# os.environ["PGPORT"] = "58894"
# os.environ["PGDATABASE"] = "postgres"
# os.environ["PGUSER"] = "vector_test"
# os.environ["PGPASSWORD"] = "password"
connection = psycopg2.connect(
    host=os.environ.get("PGHOST", "localhost"),
    port=os.environ.get("PGPORT", "5432"),
    database=os.environ.get("PGDATABASE", "postgres"),
    user=os.environ.get("PGUSER", "user"),
    password=os.environ.get("PGPASSWORD", "password")
```

`)`

```python
cursor = connection.cursor() cursor.execute("SELECT 1;") result = cursor.fetchone() if result == (1,):
    print("Connection successful!")
else:
    print("Connection failed.")
```

2. Create the table and vector index. The index parameters control retrieval quality and build
cost:

| Parameter | Value | Description |   |   |
|---|---|---|---|---|
| dim | 384 | Must match the model's output dimension. all-MiniLM-L6- v2 produces 384-dimensional vectors. |   |   |
|   |   |   | all-MiniLM-L6- |   |
| hnsw m _ | 100 | Number of connections per node in the HNSW graph. Higher values improve recall but increase memory usage and index build time. |   |   |
| pq enable _ | 0 | Disables product quantization. Set to 1 to compress vectors and reduce memory at the cost of some recall accuracy. |   |   |

|   | v2 |
|---|---|

```bash
# Create the articles table with a REAL[] vector column
# SET STORAGE PLAIN prevents PostgreSQL from compressing or toasting the vector colum
```

`n,`

```bash
# which is required for ANN index scans to work correctly.
create_table_sql = ''' CREATE TABLE IF NOT EXISTS public.articles (
    id INTEGER NOT NULL,
    sentence TEXT,
    vector REAL[],
    PRIMARY KEY(id)
) DISTRIBUTED BY(id); ALTER TABLE public.articles ALTER COLUMN vector SET STORAGE PLAIN; '''
# Create an ANN vector index on the vector column
create_indexes_sql = ''' CREATE INDEX ON public.articles USING ann (vector) WITH (dim = '384', hnsw_m = '100', pq_enable='0'); ''' cursor.execute(create_table_sql) cursor.execute(create_indexes_sql) connection.commit()
```

3. Import data from the CSV file.

```java
import io
# Read the CSV file line by line using a generator
def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
# Use COPY FROM STDIN to bulk-load the CSV into the table
copy_command = ''' COPY public.articles (id, sentence, vector) FROM STDIN WITH (FORMAT CSV, HEADER true, DELIMITER ','); ''' modified_lines = io.StringIO(''.join(list(process_file('sentences_vectors.csv')))) cursor.copy_expert(copy_command, modified_lines) connection.commit()
```

**Step 4: Query similar texts**

With data loaded, use the vector engine to retrieve the texts most semantically similar to a query. The `query_analyticdb` function below encodes a query string, then runs a SQL query using: `dp_distance(vector_col, query_vector)` — computes the dot-product distance between vectors (higher score = more similar) `<->` operator — used in the `ORDER BY` clause to rank results by vector distance

```python
def query_analyticdb(collection_name, query, query_embedding, top_k=20):
    vector_col = "vector"
    query_sql = f"""
    SELECT id, sentence, dp_distance({vector_col},Array{query_embedding}::real[]) AS si
milarity
    FROM {collection_name}
    ORDER BY {vector_col} <-> Array{query_embedding}::real[]
    LIMIT {top_k};
    """
    connection = psycopg2.connect(
        host=os.environ.get("PGHOST", "localhost"),
        port=os.environ.get("PGPORT", "5432"),
        database=os.environ.get("PGDATABASE", "postgres"),
        user=os.environ.get("PGUSER", "user"),
        password=os.environ.get("PGPASSWORD", "password")
```

`)`

```python
    cursor = connection.cursor()
    cursor.execute(query_sql)
    results = cursor.fetchall()
    connection.close()
    return results
# Encode the query and retrieve the top 10 most similar sentences
query = "What courses must be taken along with CA course?" query_vector = model.encode(query) print('query: {}'.format(query)) query_results = query_analyticdb('articles', query, query_vector.tolist(), 10) for i, result in enumerate(query_results):
    print(f"{i + 1}. {result[1]} (Score: {round(result[2], 2)})")
```

Sample output:

```
query: What courses must be taken along with CA course?
1. What courses must be taken along with CA course? (Score: 1.0)
2. What is the best combination of courses I can take up along with CA to enhance my ca
reer? (Score: 0.81)
3. Is it possible to do CA after 12th Science? (Score: 0.66)
4. What are common required and elective courses in philosophy? (Score: 0.56)
5. What are common required and elective courses in agriculture? (Score: 0.56)
6. Which course is better in NICMAR? (Score: 0.53)
7. Suggest me some free online courses that provides certificates? (Score: 0.52)
8. I have only 2 months for my CA CPT exams how do I prepare? (Score: 0.51)
9. I want to crack CA CPT in 2 months. How should I study? (Score: 0.5)
10. How one should know that he/she completely prepare for CA final exam? (Score: 0.48)
```

You can continue to select other texts that you want to query. After you query texts, you can delete the document library and the index to release resources.

**Clean up**

After testing, drop the table and index to release resources.

```
drop_table_sql = '''DROP TABLE public.articles;''' cursor.execute(drop_table_sql) connection.commit() connection.close()
```

## Backup and restoration

### Feature overview

AnalyticDB for PostgreSQL provides periodic base backups and log backups to protect against data loss.

**How it works**

AnalyticDB for PostgreSQL uses base backups and log backups to restore an instance to a specific point in time and ensure the status and data consistency of a distributed instance.
**Base backup**: backs up all database data. A base backup compresses a snapshot of all
instance data and stores the snapshot to offline storage media. The base backup does not block your read and write operations. The operation logs generated during the base backup are also backed up to ensure the integrity of the base backup.
**Log backup** (also called incremental backup): backs up log files generated from an
instance and stores them to offline storage media. Log files record the DML and DDL operations that are performed on databases. AnalyticDB for PostgreSQL uses a full base backup and continuous log backups to restore data at a specific point in time to a new instance and ensure data security. After the base backup data is restored, all nodes execute the data change statements recorded in the log backup files in sequence until the point in time for restoration. The point in time ensures consistency among all nodes when the data restoration of each node is complete.

**Scenarios**

The backup and restoration feature can be used in the following scenarios: Instance data is lost for reasons such as accidental changes. The source instance data is corrupted or unavailable. An instance needs to be cloned with the same data. The instance specifications except for the number of nodes need to be changed.

**Limits**

Data can be restored from the source instance only when the source instance has at least one backup set in the successful state. The backup and restoration feature is supported only for instances in reserved storage mode.

### Back up data

This topic describes how to view backup data and modify backup settings in AnalyticDB for PostgreSQL.

**View and modify backup settings**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Backup and Restoration** page, click the **Backup Settings** tab to view backup
settings.
5. To modify the backup settings, click **Modify Backup Settings**.
6. In the **Backup Settings** panel, configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Data Backup Retention Period (Days) | The retention period of data backups. Unit: day. Valid values: 1 to 7. Data backups can be retained for up to seven days during public preview. |
| Data Backup Cycle | The backup cycle. Select at least one day of the week for data backups. |
| Data Backup Time | The time range within which you want to create a data backup. Example: 05:00-06:00. We recommend that you back up data during off-peak hours. |
| Restore Point Settings | Specifies whether to enable point-in-time restore. If this feature is disabled, data cannot be restored by point in time. |
| Restore Point Frequency | The frequency at which you want to perform point-in-time restore. Valid values: Hourly Every 2 Hours Every 4 Hours Every 8 Hours |

7. Click **OK**.

**View base backup sets**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Data Backup** tab, view base backup sets.
Base backup data indicates a full copy of all database data. Base backup data is stored in Object Storage Service (OSS) and retained for seven days by default. The Data Backup tab displays a copy of base backup data in each row, including **Backup**
**Start Time**, **Backup End Time**, **Backup Status** (**Success** or **Failure**), **Backup Size**, and
**Consistency Point in Time**. **Consistency Point in Time** indicates the point in time to
which you can restore instance data to ensure data consistency among databases.

**View restore points in time**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Backup and Restoration** page, click the **Restore Points** tab.
5. On the **Restore Points** tab, view restore points in time.
A restore point in time indicates the point in time to which you can restore instance data. The name and timestamp of each restore point in time are displayed on this tab, as shown in the preceding figure. You can restore instance data to a restore point in time.

**View log backups**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. On the **Backup and Restoration** page, click the **Log Backup** tab.
5. On the **Log Backup** tab, view log backups.
Log files record all data changes to databases. You can restore an instance to a previous state by using its corresponding log files. All log files are stored in OSS.

### Restore data

This topic describes how to restore backup data to a new instance in AnalyticDB for PostgreSQL.

**Usage notes**

The storage capacity of the destination instance must be greater than or equal to that of the source instance. The amount of time that is consumed by instance data restoration varies based on the volume of data that is stored in the source instance. In most cases, the data of an instance is restored within a few hours.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. Click the **Data Backup** or **Restore Points** tab. Find a backup that you want to use to
restore data and click **Restore** in the **Actions** column.
5. On the **AnalyticDB for PostgreSQL Clone** page, configure the parameters. The following
table describes the parameters.

| Setting | Parameter | Description |
|---|---|---|
| Area | Organization | The organization to which the destination instance belongs. You do not need to modify the parameter value. |
|   | Resource Set | The resource set to which the destination instance belongs. You do not need to modify the parameter value. |
| Document Version: | 20260828 23 |   |

| alyticDB for Postgre e·Backup and resto |   |   |
|---|---|---|
| ea |   |   |
|   | Region | The region in which the destination AnalyticDB for PostgreSQL instance resides. You do not need to modify the parameter value. |
|   | Zone name | The zone of the destination AnalyticDB for PostgreSQL instance. |
| Instance information | Source Instance | The source instance whose data you want to restore. |
|   | Source Type | The mode that is used to restore data. It is automatically set to Backup Set. |
|   | Backup Set | The point in time to which you want to restore data. |
| Basic Settings | Instance Resource Type | The resource type of the destination instance. It is automatically set to the resource type of the source instance. |
|   | Chip Architecture | The chip architecture of the host on which the destination instance is deployed. You do not need to modify the parameter value. |
|   | Master Nodes | The number of master nodes. It is automatically set to 1. After you create an instance, you can add more master nodes to the instance. For more information, see Change the specifications of an instance. |
|   | Compute Group Specifications | Specifications for each compute group. The storage space and compute capability of a compute group vary based on the specified specifications. |
|   | Compute Nodes | The number of compute nodes. It is automatically set to the number of compute nodes of the source instance. |
|   | Compute Node Capacity | The capacity of compute nodes. It is related to the compute node specifications and cannot be modified. The CPU cores, memory size, and storage capacity are in a ratio of 1:8:80. For example, if the compute node specifications are 2 cores and 16 GB of memory, the storage capacity is 160 GB. |
|   | Storage Medium | The storage type of the destination instance. It is automatically set to Local SSD. |
| Network | Network Type | The network type of the destination AnalyticDB for PostgreSQL instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by using security groups or whitelists. VPC ID: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can specify custom route tables, CIDR blocks, and gateways within a VPC. We recommend that you select VPC for improved security. You can create a VPC in advance, or change the network type to VPC after the instance is created. |

|   | VPC | The VPC in which the destination AnalyticDB for PostgreSQL instance resides. Note This parameter is available only when Network Type is set to VPC ID. |
|---|---|---|
|   | vSwitch | The vSwitch of the destination AnalyticDB for PostgreSQL instance. Note This parameter is available only when Network Type is set to VPC ID. |
|   | IP Address Whitelist | The IP addresses that are allowed to access the destination AnalyticDB for PostgreSQL instance. |

6. Click **Submit**.

## Performance monitoring

### Monitoring and alerting

#### View instance monitoring information

This topic describes how to view the instance monitoring information about an AnalyticDB for PostgreSQL instance.

**Usage notes**

The instance monitoring feature is supported only for instances in reserved storage mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Monitoring and Alerts > Instance Monitoring**.
The **Instance Monitoring** page consists of the following sections:

**Instance Status section**

Displays the status information about the instance, including the **Status**, **Instance**
**Storage Status**, **Instance Health Status**, **Instance Storage Usage**, **Instance**
**Connection Status**, **Maximum Coordinator Node Storage Usage**, and **Maximum**
**Compute Node Storage Usage** parameters.

**Performance and load section**

Displays the performance and load information about the instance in the **Coordinator**
**Node Connections**, **Compute Node Connections**, **Instance Storage Used (MB)**,
**Compute Nodes**, **Temporary Disk File Size (MB)** , **Abnormal Coordinator Nodes**,
**Healthy Coordinator Nodes**, **Abnormal Compute Nodes**, **Compute Nodes in Non-**
**synchronous State**, **Compute Nodes in Synchronous State**, **Coordinator Nodes in**
**Non-synchronous State**, **Coordinator Nodes in Synchronous State**, **Compute**
**Nodes with Normal Roles**, **Compute Nodes with Converted Roles**, **Coordinator**
**Nodes with Normal Roles**, **Healthy Compute Nodes**, **Blocked Queries for**
**Instance**, **Queuing Queries for Instance** , **Active Connections for Instance**, **Active**
**Queries for Instance**, **Idle Connections for Instance**, and **Instance Storage Usage**
**(%)** charts.
4. **Optional.** Select a **time range** to view the corresponding metrics.

**Note**

The interval between the start time and the end time cannot exceed seven days.

#### View node monitoring information

This topic describes how to view the node monitoring information about an AnalyticDB for PostgreSQL instance.

**Usage notes**

The instance monitoring feature is supported only for instances in reserved storage mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Monitoring and Alerts > Node Monitoring**.
The **Node Monitoring** page consists of the following section and tabs:
**Node Status** section
Displays the node status information about the instance, including the **Coordinator**
**Node Health Status**, **Compute Node Connection Health Status** , **Coordinator**
**Node Connection Health Status**, and **Compute Node Storage Status** parameters.
**Coordinator Nodes** tab
Displays the status information about coordinator nodes in the **CPU Utilization (%)** and
**Memory Usage (%)** charts.
**Compute Nodes** tab
Displays the status information about compute nodes in the **CPU Utilization (%)**,
**Storage Used (MB)**, **Storage Usage (%)**, **Memory Usage (%)**, **Read IOPS**, and
**Write IOPS** charts.
4. **Optional.** Select a **time range** to view the metrics.
You can set Time Range to Recent 1 Hour, Recent 6 Hours, Recent 1 Day, Recent 7 Days, or a custom time range.

**Note**

The interval between the start time and the end time of the custom time range cannot exceed seven days.

### Monitoring and alerting

AnalyticDB for PostgreSQL provides the monitoring and alerting feature to help you view the running status of instances.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
The following metrics are displayed on the **Monitoring and Alerts** page:
**Monitoring Summary** tab
On this tab, you can view **CPU Utilization and Memory Usage (%)** , **Total**
**Connections of Coordinate Node**, **Disk Bandwidth**, and **Disk Usage (MB)**.
**Compute Group Monitoring** or **Compute Node Monitoring** tab
The **Compute Group Monitoring** tab appears if the instance is in storage included mode. The **Compute Node Monitoring** tab appears if the instance is in reserved storage mode. On this tab, you can view **CPU Utilization and Memory Usage (%)** , **Write IOPS**, **Read**
**IOPS**, and **Disk Usage (MB)**.
4. **Optional:**Select a time range to view metrics within the specified period. The following
options are available for **Time Range**:
**1 Hour**: You can view metrics within the last hour.
**1 Day**: You can view metrics within the last day.
**Custom time range**: You can view metrics within a custom time range. The time range
cannot be longer than seven days.

### Diagnostics and optimization

#### Instance status overview

AnalyticDB for PostgreSQL provides an Overview page for the diagnostics and optimization feature. You can view the connection status, cluster status, and storage status of an instance on this page.

**Usage notes**

The instance monitoring feature is supported only for instances in reserved storage mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Diagnostics and Optimization > Overview**.
On the left side of the **Overview** page, the status information is listed. On the right side of the page, metrics of the instance are displayed in line charts. Status information

| Section | Metric | Description |
|---|---|---|
| Connection Status | Connection Status of Coordinator Node | The connection status of coordinator nodes. The following colors indicate different states: Red: The node connection usage is greater than or equal to 95%. Yellow: The node connection usage is greater than or equal to 90% and less than 95%. Green: The node connection usage is less than 90%. Note The connection usage of coordinator nodes is the highest connection usage among all coordinator nodes. |
|   | Connection Status of Compute Node | The connection status of compute nodes. The following colors indicate different states: Red: The node connection usage is greater than or equal to 95%. Yellow: The node connection usage is greater than or equal to 90% and less than 95%. Green: The node connection usage is less than 90%. Note The connection usage of compute nodes is the highest connection usage among all compute nodes. |

| Cluster Status | Running Status | The status of the instance. |
|---|---|---|
|   | Instance Health Status | The health status of the instance. The following colors indicate different states: Red: One or more coordinator nodes or compute nodes are unavailable. Green: All nodes are available. |
|   | Instance Connection Status | The connection status of the instance. The following colors indicate different states: Red: The instance connection usage is greater than or equal to 95%. Yellow: The instance connection usage is greater than 90% and less than or equal to 95%. Green: The instance connection usage is less than or equal to 90%. Note The instance connection usage is the highest connection usage among all coordinator and compute nodes. |
|   | Coordinator Node Status | The health status of coordinator nodes. The following colors indicate different states: Red: Both the primary and standby coordinator nodes are unavailable. Yellow: The primary or standby coordinator node is unavailable. Green: Both the primary and standby coordinator nodes are available. |
|   | Compute Node Status | The health status of compute nodes. The following colors indicate different states: Red: All compute nodes are unavailable. Yellow: At least half of all compute nodes are unavailable. Green: All compute nodes are available. |
| Storage Status | Instance Storage Status | The storage status of the instance. The following colors indicate different states: Red: The instance storage usage is greater than or equal to 90%. In this case, the instance is locked. Yellow: The instance storage usage is greater than or equal to 70% and less than 90%. Green: The instance storage usage is less than 70%. |
|   | Maximum Storage Usage of Coordinator Node | The maximum storage usage of coordinator nodes. Unit: %. |
| cument Version: 202608 | 28 23 |   |

|   | Maximum Storage Usage of Compute Node | The maximum storage usage of compute nodes. Unit: %. |
|---|---|---|

Line charts The following metrics are displayed in line charts: **SQL**, **Connections**, **Instance**
**Storage Usage (%)**, **Coordinator Nodes**, and **Compute Nodes**. You can move the
pointer over each line chart to view the details.

#### Use the O&M Assistant feature

AnalyticDB for PostgreSQL provides an O&M Assistant page for the diagnostics and optimization feature. You can view data bloat, data skew, and index statistics on this page.

**Usage notes**

The instance monitoring feature is supported only for instances in reserved storage mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Diagnostics and Optimization > O&M**
**Assistant**.
The **O&M Assistant** page consists of three tabs: **Data Bloat**, **Data Skew**, and **Index**
**Statistics**.

**Data Bloat tab**

**Note**

The Data Bloat tab lists tables that are larger than 1 GB in size.

| Parameter | Description |
|---|---|
| Database Name | The name of the database. |
| Schema Name | The name of the schema. |
| Table Name | The name of the partitioned table. |
| Table Type | The storage type of the table, such as heap table or append- optimized (AO) table. |
| Expected Table Size | The expected size of the table. Unit: bytes. The expected table size is the size thatA nalyticDB for PostgreSQL calculates without bloat. |

| Actual Table Size | The actual size of the table. Unit: bytes. |
|---|---|
| Bloat Table Size | The bloat size of the table. It indicates the amount of space that can be released. Unit: bytes. |
| Bloat Coefficient | The coefficient of data bloat. It is calculated by using the following formula: Bloat coefficient = Number of dead rows/Number of active rows. Note UPDATE and DELETE operations may cause dead rows because AnalyticDB for PostgreSQL uses the multiversion concurrency control (MVCC) policy. |
| Last Diagnosed At | The time when the most recent DELETE, INSERT, or UPDATE operation was performed on the table. |

**Data Skew tab**

**Note**

The Data Skew tab lists tables that are larger than 1 GB in size.

| Parameter | Description |
|---|---|
| Database Name | The name of the database. |
| Schema Name | The name of the schema. |
| Table Name | The name of the table. |
| Owner | The owner of the table. |
| Table Size | The size of the table. |
| Skew Ratio | The skew ratio of the table, which is written as a percentage. A greater value indicates more severe data skew. A less value indicates less impact on query performance. A value of 0 indicates that no data skew exists. The skew ratio can be calculated by using the following formula: Skew ratio = 1 - (Average table size among all nodes/Maximum table size among all nodes). |

| Distribution Key | The distribution key of the table. |
|---|---|
| Last Diagnosed At | The time when the most recent DELETE, INSERT, or UPDATE operation was performed on the table. |

**Index Statistics tab**

**Note**

The Index Statistics tab displays indexes that are larger than 100 MB in size.

| Parameter | Description |
|---|---|
| Database Name | The name of the database. |
| Schema Name | The name of the schema. |
| Table Name | The name of the table. |
| Index Size | The size of the index. Unit: bytes. |
| Index Scans | The total number of index scans. |
| Index-scanned Rows | The total number of index-scanned rows. |
| Index Name | The name of the index. |
| Last Diagnosed At | The time when the most recent DELETE, INSERT, or UPDATE operation was performed on the table. |

#### Query analysis

AnalyticDB for PostgreSQL provides the query analysis feature. You can view SQL execution plans and statistics for query analysis and optimization. This topic describes how to use the query analysis feature.

**Usage notes**

The instance monitoring feature is supported only for instances in reserved storage mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left-side navigation pane, choose **Diagnostics and Optimization > Query**
**Analysis**.
4. In the upper-right corner of the page, select a database, a filter condition, and a time range
to view query execution information. The Query Analysis page provides the following sections to display query execution information:

**Query execution swimlane diagram**

Each color block in the swimlane diagram indicates a query execution process. You can move the pointer over each color block to view execution information about the query and click **Details** to go to the **Query Properties** page. For more information about the
**Query Properties** page, see the "Query Properties page" section of this topic.

**SQL queries**

Each row of information in the query list indicates a query execution process. The information about query execution is displayed in the list. You can click **Diagnose** in the
**Actions** column to go to the **Query Properties** page. For more information about the
**Query Properties** page, see the "Query Properties page" section of this topic.
The following table describes the information that is contained in the SQL query list.

| Parameter | Description |
|---|---|
| SQL Statement | The SQL statement of the query. |
| Start Time | The start time of the query. |
| Query ID | The unique ID of the query. |
| Session ID | The session ID of the query. |
| Database | The name of the database that you want to query. |
| Status | The state of the query. Valid values: Completed Running |
| Duration | The total amount of time consumed for the query. Unit: seconds. |
| Username | The user who executes the query. |

You can click **Download** to download the information to your computer.

**Query Properties page**

The **Query Properties** page consists of three tabs: **Query Statement**, **Execution Plan**
**Text**, and **Execution Plan Tree**.

**Query Statement tab**

The **Query Statement** tab provides the SQL query statement.

**Execution Plan Text tab**

The **Execution Plan Text** tab provides the execution plan that is obtained from the EXPLAIN statement.

**Execution Plan Tree tab**

The **Execution Plan Tree** tab provides a tree chart to show the execution plan. The execution plan tree is displayed on the left side, and the operator execution statistics are displayed on the right side. You can click each operator card in the tree to view statistics of the operator. By default, the line below each operator card shows the execution duration proportion of the operator among all operators, and all operators are listed in the upper-right corner of the tab as sorted by execution duration. You can also sort operators by memory usage, amount of disk read data, disk read duration, amount of transmitted data, or data transmission duration and calculate the total sum of proportions. The following table describes the operator execution statistics.

| Parameter | Description |
|---|---|
| Operator Name | A combination of the name and ID of the operator. It is unique in a plan tree. |
| Type ID | The type ID of the operator. |
| Type | The type name of the operator. This value does not have to be unique in a plan tree. |
| Output Rows | The number of rows of data output by the operator to its upper- level operator. |
| Input Rows | The number of rows of data read by the operator from its lower- level operator or disk. |
| Memory Used by Execution | The amount of memory used by execution of the operator. Note This amount of memory is measured only for the Sort, Hash, and Hash Aggregate operators and ignored for other operators. This is because the execution of other operators occupies only a small amount of memory. |
| Execution Duration | The amount of time consumed to execute the operator. |
| Amount of Disk Read Data | The total amount of data read by the operator from disks. Note This amount of data includes the raw data read by the Scan operator and the data spilled by other operators due to insufficient memory. |
| Disk Read Duration | The amount of time consumed by the operator to read data from disks. |
| Amount of Transmitted Data | The total amount of data transmitted between Motion operators. |
| Data Transmission Duration | The amount of time consumed to transmit data between Motion operators. |

#### Lock diagnostics

When a query runs for an extended period without returning results, it may be waiting for a lock to be released. The lock diagnostics feature helps you quickly identify and analyze lock contention within your database.

**Limitations**

The lock diagnostics feature is currently available only for instances in storage reservation mode.

**Procedure**

1. Log in to the AnalyticDB for PostgreSQL console.
2. Find the instance that you want to manage and click the instance ID.
3. In the left navigation bar, select **Diagnostics And Optimization > Query Analysis**.
4. Click the **Lock Diagnostics** tab.
5. On the **Lock Diagnostics** page, you can filter lock diagnostic information by **Keyword**,
**Username**, **Database**, **Filter Condition**, and **Query Time**.
The lock diagnostics list displays the following information:

| Parameter | Description |
|---|---|
| SQL | The SQL text of the query statement. |
| Start Time | The start time of the query statement. |
| Process ID | The ID of the process that uniquely identifies the query statement. |
| Session ID | The ID of the session that contains the query statement. |
| Database | The database on which the query statement is executed. |
| Status | The state of the query statement. |
| Wait Duration | The waiting duration of the query statement. |
| Username | The database account that executes the query statement. |

6. Click **Diagnose** in the **Operation** column of the target diagnostic information to view **Lock**
**Wait Properties** and **Lock Diagnostic Details**.
**Lock Wait Properties**: This section displays the **Process ID**, **Username**, **Database**,
**Start Time**, **Wait Duration**, and **Status**.
**Lock Diagnostic Details**: This is the core of the analysis. It identifies both the blocked
query and the blocking query, showing their respective **Process ID**, **Username**, and
**Query Statement**.

**Note**

SQL statements in the **Resource Wait** state are not supported by this diagnostic tool.

**Optimization method**

If your query does not return results for an extended period of time and the Lock Diagnostics tab shows that the query is in the lock wait state, you have two options: either wait for the system to automatically execute your query after the preceding queries are complete, or manually cancel or terminate the blocking queries. Use the following method to cancel or terminate a blocking query.

**Note**

Only a privileged account that has superuser permissions can cancel or terminate queries. Cancel a query Use this method only when the session that contains the query is actively running. The database will perform a clean rollback of the transaction, which may take some time.

```
SELECT pg_cancel_backend(<Process_ID>);
```

Terminate a query Use this method if the blocking session is already idle or if `pg_cancel_backend` fails. This is a more forceful method.

```
SELECT pg_terminate_backend(<Process ID>);
```

## Cloud Monitor

### View performance metrics

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

### Alert history

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

### Alert rules

#### Create an alert rule

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

#### Manage alert rules

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

## Best practices

### Configure memory and load

**parameters**

To improve database stability, you must configure memory and load parameters.

**Background information**

AnalyticDB for PostgreSQL is a massively parallel processing (MPP) database service with high computational and resource requirements. AnalyticDB for PostgreSQL consumes all of its resources. This allows AnalyticDB for PostgreSQL to reach high processing speeds but makes it very easy to exceed its limits. When CPU, network, or hard disk resources are exhausted, you may encounter hardware bottlenecks. However, databases may not respond if memory resources are overused.

**How to avoid OOM errors**

Out of memory (OOM) indicates that the system is unable to provide sufficient memory requested by a process. The following prompt appears when OOM errors occur:

```
Out of memory (seg27 host.example.com pid=47093) VM Protect failed to allocate 4096 byt es, 0 MB available
```

**Causes**

OOM errors may occur due to the following causes: Database nodes do not have sufficient memory. Kernel parameters related to the memory of the operating system are incorrectly configured. Data skew has occurred. This causes a compute node to request a large amount of memory. Query skew has occurred. For example, if the grouping fields of specific aggregate or window functions are not distribution keys, the data must be redistributed. After the data is redistributed, data is skewed on a specific computer node and the node may request a large amount of memory.

**Solutions**

1. Modify the queries to request less memory.
2. Use a resource queue of AnalyticDB for PostgreSQL to limit the number of concurrent
queries. Reduce the number of concurrent queries that are executed on the instance to reduce the overall memory requested by the system.
3. Reduce the number of compute nodes deployed on a host. For example, you can deploy 8
compute nodes instead of 16 on a host that has 128 GB of memory to allow each compute node to utilize twice as much memory.
4. Increase the memory of a host.
5. Set the gp_vmem_protect_limit parameter to limit the maximum VMEM that can be used by
a single compute node. The memory size of a single host and the number of compute nodes deployed on the host determine the maximum memory size that a single compute node can use on average.
6. For SQL statements that have unpredictable memory usage, you can set the
statement_mem parameter in the session to limit the memory usage of a single SQL statement. This prevents a single SQL statement from consuming all available memory.
7. Set the statement_mem parameter at the database level to apply the parameter to all the
sessions in the database.
8. Use the resource queue of AnalyticDB for PostgreSQL to limit the maximum memory usage
of the resource group. Add database users to the resource group to limit the total memory used by these users.

**Configure memory-related parameters**

You can properly configure the operating system, database parameters, and resource queue to reduce the probability of OOM. When you calculate the average memory usage of a single compute node on a single host, you must consider both the primary and secondary compute nodes. If the cluster encounters a host failure, the system switches the service from primary compute nodes to the corresponding secondary compute nodes. At this time, the number of compute nodes on the host is greater than usual. Therefore, you must consider the amount of resources occupied by the secondary compute nodes during failover. The following tables describe how to configure parameters for the operating system kernel and database to avoid OOM. The following Operating system kernel parameters table describes the parameter configuration of the operating system kernel. Table 1. Operating system kernel parameters

| Parameter | Description |
|---|---|
| huge page | Do not configure the huge page parameter of the system.A nalyticDB for PostgreSQL does not support the latest version of PostgreSQL and therefore does not support the huge page feature. The huge page parameter locks a part of the allocated memory. Database nodes are not able to use this part of the memory. |
| vm.overcommit memory _ | If you use the swap space, set this parameter to 2. If you do not use the swap space, set this parameter to 0. Valid values: 0: The requested memory space cannot exceed the difference between the total memory and the resident set size (RSS). An error is returned only when the memory space has been exceeded. 1: Most processes use the malloc() function to request memory, but do not use all of the requested memory. When this parameter is set to 1, the memory requested by the malloc() function is allocated in all circumstances unless the memory is not sufficient. 2: The swap space is also considered when the system calculates the memory space that can be requested. You can request a large amount of memory even if the swap space is triggered. |
| overcommit ratio _ | The larger the value is, the more memory the process can request. However, less space is reserved for the operating system. For more information about the formula that is used to calculate the memory parameters, see the "Examples to calculate the memory parameters" section of this topic. When this parameter is set to 2, the memory that can be requested cannot exceed swap + memory × overcommit ratio. _ |

The following Database parameters table describes the parameter configuration of the database. Table 2. Database parameters

| Parameter | Description |
|---|---|
| gp vmem protect limit _ _ _ | The maximum amount of memory that all processes can request on each node. If the value is too large, it may result in a system OOM error or even more serious problems. If the value is too small, SQL statements may not be executed even when the system has enough memory. |
| runaway detector activatio _ _ n percent _ | Default value: 90. Unit: %. When the amount of memory used by a compute node exceeds runaway detector activation percent × _ _ _ gp vmem protect limit/100, the query is terminated to prevent OOM. _ _ _ The query remains stopped until the memory usage reaches a value lower than runaway detector activation percent × _ _ _ gp vmem protect limit/100. _ _ _ You can use the gp toolkit.session level memory consumption view to _ _ _ _ observe the memory usage of each session and runaway information. |
| statement mem _ | The maximum amount of memory that a single SQL statement can request. When the maximum memory is exceeded, spill files are created. Default value: 125. Unit: MB. We recommend that you set this parameter based on the following formula: (gp vmem protect limit * 0.9) / _ _ _ max expected concurrent queries _ _ _ Note You can specify the statement mem parameter in a _ session. If few concurrent queries exist and if the session needs to execute a query that requires a large amount of memory, you must specify this parameter in the session. The statement mem parameter is suitable for limiting _ memory usage in low concurrency scenarios. If you use statement mem to limit the memory for high concurrency _ scenarios, each query is allocated with a very small amount of memory. As a result, the performance of a small number of queries with high memory requirements in high concurrency scenarios is affected. We recommend that you use the resource queue to limit the maximum memory usage in high concurrency scenarios. |

| gp workfile limit files per q _ _ _ _ _ uery | The maximum number of spill files that can be created by each query. When the amount of memory requested by the query exceeds the statement mem limit, spill files (also known as work files) are created. _ Spill files are similar to the swap space of the operating system. When the number of spill files used exceeds the limit, the query is terminated. The default value is 0, which indicates that an unlimited number of spill files can be created. |
|---|---|
| gp workfile compress algori _ _ _ thm | The compression algorithm for spill files. Valid values: NONE and ZLIB. This parameter can optimize storage space or I/O by sacrificing CPU performance. You can set this parameter when the disk space is insufficient or when the spill files encounter a write bottleneck. |

**Examples to calculate the memory parameters**

The following environment configurations are used in the examples: Host configuration:

```
Total RAM = 256GB SWAP = 64GB
```

Four hosts, each deployed with eight primary compute nodes and eight secondary compute nodes. If a host fails, the eight primary compute nodes are distributed to the remaining three hosts. A single host can be deployed with a maximum of three extra primary compute nodes from the failed host. A single host can be deployed with a maximum of 11 primary compute nodes.
1. Calculate the total memory allocated to AnalyticDB for PostgreSQL by the operating
system. Reserve 7.5 GB and 5% of memory for the operating system and calculate the available memory for all applications. Then, divide the available memory by an empirical coefficient of 1.7.

```
gp_vmem = ((SWAP + RAM) - (7.5 GB + 0.05 × RAM))/1.7
        = ((64 + 256) - (7.5 + 0.05 * 256)) / 1.7
        = 176
```

2. Use an empirical coefficient of 0.026 to calculate an ideal value for the overcommit_ratio
parameter.

```
vm.overcommit_ratio = (RAM - (0.026 * gp_vmem)) / RAM
                    = (256 - (0.026 * 176)) / 256
                    = .982
Set vm.overcommit_ratio to 98.
```

3. Calculate the gp_vmem_protect_limit parameter by dividing gp_vmem by
maximum_acting_primary_segments. The maximum_acting_primary_segments parameter indicates the number of primary compute nodes to be run on each host after one host fails.

```
gp_vmem_protect_limit calculation gp_vmem_protect_limit = gp_vmem / maximum_acting_primary_segments
                      = 176 / 11
                      = 16GB
                      = 16384MB
```

**Configure resource queues**

You can use resource queues of AnalyticDB for PostgreSQL to limit the number of concurrent queries and the total memory usage. While a query is being executed, it is added to the corresponding queue and the resources used are recorded in the queue. The resource limit of the queue applies to all sessions in the queue. The resource queue in AnalyticDB for PostgreSQL is similar to cgroup in Linux. The following syntax demonstrates how to create a resource queue:

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

The Resource queue creation parameters table describes the parameters for creating the resource queue. Table 3. Resource queue creation parameters

| Parameter | Description |
|---|---|
| ACTIVE STATEMENTS _ | The number of SQL statements that can be concurrently executed (in the active state). A value of -1 indicates that an unlimited number of SQL statements can be concurrently executed. |

| MEMORY LIMIT _ 'memory units kB, MB or _ GB' | The maximum memory usage allowed by all SQL statements in the resource queue. A value of -1 indicates unlimited memory usage. However, it is easy to trigger OOM errors because it is limited by the database or system parameters mentioned in the preceding sections. The memory usage of SQL statements is limited by resource queues and parameters. When the gp resqueue memory policy parameter is set to none, the _ _ _ limit is the same as that in versions of Greenplum Database earlier than 4.1. When the gp resqueue memory policy parameter is set to auto and _ _ _ you have specified the statement mem parameter for a session or at _ the database level, the allowed memory of a single query exceeds the MEMORY LIMIT value of the resource queue. _ Example: SET statement mem='2GB'; _ SELECT * FROM my big table WHERE column='value' ORDER BY _ _ id; RESET statement mem; _ The system parameter max statement mem can limit the maximum _ _ memory usage at the compute node level. The memory requested by a single query cannot exceed max statement mem. _ _ You can modify the statement mem parameter at the session level, but _ do not modify the max statement mem parameter. We recommend _ _ that you specify max statement mem in the following formula: _ _ (seghost physical memory) / _ _ (average number concurrent queries) _ _ _ When the gp resqueue memory policy parameter is set to eager free, _ _ _ _ the database allocates the memory by stage. For example, if a query requests 1 GB of memory in total but needs only 100 MB during each stage, the database allocates 100 MB of memory to the query. You can use eager free to reduce the possibility of insufficient memory for the _ query. |
|---|---|
| MAX COST float _ | The maximum cost of the queries that can be concurrently executed by the resource group. The cost is the estimated total cost in the SQL execution plan. The value of the parameter can be specified as a floating-point number such as 100.0 or an exponent such as 1e+2. A value of -1 indicates that the cost is not limited. |
| COST OVERCOMMIT _ boolean | Specifies whether the limit of max cost can be exceeded while the system _ is idle. A value of TRUE indicates that the limit can be exceeded. |
| MIN COST float _ | When the resources requested exceed the limit, the queries are queued. However, if the cost of a query is less than the min cost value, the query _ can be executed without being queued. |

| PRIORITY= {MIN\|LOW\|MEDIUM\|HIGH \|MAX} | The priority of the current resource queue. When resources are insufficient, CPU resources are allocated to the resource queue that has a higher priority. The SQL statements in the resource queue that has a higher priority can obtain CPU resources first. We recommend that you allocate users that initiate queries with high real-time requirements to resource queues that have higher priorities. This parameter is similar to the time slice policy that is used in CPU resource groups in a Linux cgroup to schedule real-time and common tasks. |
|---|---|

Example of modifying resource queue limits:

```
ALTER RESOURCE QUEUE myqueue WITH (MAX_COST=-1.0, MIN_COST= -1.0);
```

Example of putting a user in a resource queue:

```
ALTER ROLE sammy RESOURCE QUEUE poweruser;
```

Table 4. Resource queue parameters

| Parameter | Description |
|---|---|
| gp resqueue memory policy _ _ _ | The memory management policy of the resource queue. |
| gp resqueue priority _ _ | Specifies whether to enable query prioritization. Valid values: ON: enables query prioritization. OFF: disables query prioritization. If query prioritization is disabled, the existing priority settings are not evaluated. |
| gp resqueue priority cpucores _ _ _ per segment _ _ | The number of CPU cores allocated to each compute node. For example, if an 8-core host is configured with two primary compute nodes, you can set the parameter to 4. If no other nodes exist on the primary node, set the parameter to 8. When the CPU is preempted, the SQL statements that are executed in a higher-priority resource group are allocated with CPU resources first. |
| gp resqueue priority sweeper _ _ _ interval _ | The interval at which CPU utilization is recalculated for all active statements. The share value is calculated when the SQL statement is executed. You can calculate the share value based on the priority and gp resqueue priority cpucores per segment. _ _ _ _ _ The smaller the interval and the more frequent the calculation, the better the results achieved by the priority settings and the larger the overhead. |

Tips for configuring resource queues: We recommend that you create a resource queue for each user. The default resource queue of AnalyticDB for PostgreSQL is pg_default. If no queue is created, all users are assigned to pg_default. This operation is not recommended. We recommend that you create a resource queue for each user. Typically, a database user corresponds to a business operation. Different database users may correspond to different business operations or users, such as business users, analysts, developers, and DBAs. We recommend that you do not use superusers to execute queries. Queries initiated by superusers are limited only by the preceding parameters and not by the resource queue. If you want to use resource queues to limit the use of resources, we recommend that you do not use superusers to execute queries. ACTIVE_STATEMENTS indicates the SQL statements that can be concurrently executed within a resource queue. When the cost of a query is lower than the minimum cost specified by min_cost, the query can be executed without being queued. You can specify the MEMORY_LIMIT parameter to set the allowed maximum memory usage of all the SQL statements in a resource queue. The statement_mem parameter has a higher priority that can break through the limit of resource queues.

**Note**

The memory of all resource queues cannot exceed gp_vmem_protect_limit. You can distinguish different business operations by configuring the priorities of resource queues. For example, you can give report-related business operations a top priority while giving common business operations and analysis lower priorities. In this case, you can create three resource queues that have the max, high, and medium priorities, respectively. If the number of resources requested at different periods of time varies, you can run the crontab command to periodically adjust the limits of resource queues based on usage patterns. For example, you can give the queue of analysis a higher priority in the day and the queue of report-related business operations a higher priority at night. AnalyticDB for PostgreSQL does not allow you to configure resource limits by period of time. Therefore, you can only externally deploy tasks by using the ALTER RESOURCE QUEUE statement. You can use the view provided by gp_toolkit to view the resource usage of the resource queues.

```
gp_toolkit.gp_resq_activity gp_toolkit.gp_resq_activity_by_queue gp_toolkit.gp_resq_priority_backend gp_toolkit.gp_resq_priority_statement gp_toolkit.gp_resq_role gp_toolkit.gp_resqueue_status
```

## Appendix

### Authorize a tenant

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
