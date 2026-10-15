---
title: "ApsaraDB for RDS ApsaraDB RDS for PolarDB User Guide 20260629"
product_version: "V3.18.6"
pdf_pages: 159
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 ApsaraDB for RDS ApsaraDB RDS for PolarDB User Guide 20260629.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93RDS%20/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20ApsaraDB%20for%20RDS%20ApsaraDB%20RDS%20for%20PolarDB%20User%20Guide%2020260629.pdf"
converter: line-classifier (PyMuPDF)
---

# ApsaraDB for RDS ApsaraDB RDS for PolarDB User Guide 20260629

ApsaraDB for RDS ApsaraDB RDS for PolarDB User eSQL (Compatible with Oracle)?

## What is PolarDB for

**PostgreSQL (Compatible with**

**Oracle)?**

This topic outlines the cloud-native database PolarDB for PostgreSQL (Compatible with Oracle). PolarDB for PostgreSQL (Compatible with Oracle) is a stable, secure, and scalable enterprisegrade cloud-native relational database. It is based on the open-source PostgreSQL database and provides enhancements in performance, application solutions, and compatibility. This lets you run Oracle applications directly. You can run various enterprise applications on PolarDB to implement stable and cost-effective services. PolarDB for PostgreSQL (Compatible with Oracle) supports deployment on hybrid x86 and ARM clusters or on hybrid HYGON and Intel clusters. It provides features such as account management, resource monitoring, backup and recovery, and security control. These features are continuously enhanced.

**Architecture diagram**

The following figure shows the service architecture of a dual-node cluster that uses local disks. High availability Primary node Secondary node Copy Data Log Data Log Local Local disk disk

| Operation | Limits |
|---|---|
| Database parameter modification | Not supported. |
| Database replication | The system automatically builds HA databases based on PolarDB streaming replication without user input. Secondary PolarDB instances are hidden and cannot be accessed. |
| Instance restart | You can restart an instance in the console or by calling API operations. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Limits on PolarDB

Before you use PolarDB, you must understand its limits and take the necessary precautions. The following table describes the limits on PolarDB.

| Instance type | Feature | Applicable scenario |
|---|---|---|
| Dedicated | A dedicated cluster occupies all allocated compute resources such as CPUs. The cluster does not share compute resources with other instances that run on the same server. This improves the reliability and stability of the instance. | Scenarios in which databases are the key component of business systems that require high reliability, such as finance, e-commerce, public service, and medium- or large-scale Internet services. |
| Shared | Idle compute resources such as CPUs are shared among instances that run on the same server. Resource sharing allows you to deploy a large number of instances at low costs. | Scenarios in which cost-effectiveness is prioritized. |
| Dedicated host | The maximum dedicated specification is that all resources of a physical host are exclusive to the dedicated specification. | The maximum stability and isolation are provided. Instances of this type are applicable to scenarios in which databases are the key component of business systems, such as finance, e- commerce, public service, and medium- or large-scale Internet services. |

| Edition | Databas e version | Instance family | Code of instance type | CPU and memory | Maximu m connecti ons | Maximu m IOPS | Storage capacity |
|---|---|---|---|---|---|---|---|

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Instance types

This topic describes the instance types of PolarDB. Different instance types deliver different performance.

**PolarDB (High-availability Edition)**

**Note**

For PolarDB, different database versions are supported for different compatibility types. If the **compatibility type** is **PostgreSQL**, only **database version****14** is supported. If the
**compatibility type** is **Oracle**, **database versions****14** and **11.2** are supported.

|  |  | Dedicate d | polardb.x 4.mediu m.2 | 2 CPU cores and 8 GB of memory | 3,300 | 10,000 | 20 GB- 3000 GB (Step size: 5 GB) |
|---|---|---|---|---|---|---|---|
|  |  |  | polardb.x 8.mediu m.2 | 2 CPU cores and 16 GB of memory | 3,300 | 15,000 |  |
|  |  |  | polardb.x 4.large.2 | 4 CPU cores and 16 GB of memory | 3,300 | 20,000 |  |
|  |  |  | polardb.x 8.large.2 | 4 CPU cores and 32 GB of memory | 3,300 | 30,000 |  |
|  |  |  | polardb.x 4.xlarge. 2 | 8 CPU cores and 32 GB of memory | 3,300 | 40,000 |  |
|  |  |  | polardb.x 8.xlarge. 2 | 8 CPU cores and 64 GB of memory | 12,100 | 60,000 |  |
|  |  |  | polardb.x 4.2xlarge .2 | 16 CPU cores and 64 GB of memory | 12,100 | 80,000 |  |
|  |  |  | polardb.x 8.2xlarge .2 | 16 CPU cores and 128 GB of memory | 12,100 | 120,000 |  |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

|  | 14 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  | polardb.x 4.4xlarge .2 | 32 CPU cores and 128 GB of memory | 12,800 | 160,000 | 20 GB- 6000 GB (Step size: 5 GB) |
|  |  |  | polardb.x 8.4xlarge .2 | 32 CPU cores and 256 GB of memory | 25,600 | 240,000 |  |
|  |  |  | polardb.x 4.8xlarge .2 | 64 CPU cores and 256 GB of memory | 25,600 | 320,000 |  |
|  |  |  | polardb.x 8.8xlarge .2 | 64 CPU cores and 512 GB of memory | 12,100 | 240,000 |  |
|  |  |  | polardb.g 4.mediu m.2 | 2 CPU cores and 8 GB of memory | 400 | 10,000 | 20 GB- 3000 GB (Step size: 5 GB) |
|  |  |  | polardb.g 2.large.2 | 4 CPU cores and 8 GB of memory | 800 | 20,000 |  |
|  |  |  | polardb.g 4.large.2 | 4 CPU cores and 16 GB of memory | 2,500 | 20,000 |  |
|  |  |  | polardb.g 2.xlarge. 2 | 8 CPU cores and 16 GB of memory | 1,600 | 40,000 |  |
|  |  |  | polardb.g 4.xlarge. 2 | 8 CPU cores and 32 GB of memory | 5,000 | 40,000 |  |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| High- availab ility Edition Read- only instanc e |  | Shared |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  | polardb.g 2.2xlarge .2 | 16 CPU cores and 32 GB of memory | 3,200 | 80,000 |  |
|  |  |  | polardb.g 4.2xlarge .2 | 16 CPU cores and 64 GB of memory | 10,000 | 80,000 |  |
|  |  |  | polardb.g 2.4xlarge .2 | 32 CPU cores and 64 GB of memory | 6,400 | 160,000 |  |
|  |  |  |  |  |  |  | 20 GB- 6000 GB (Step size: 5 GB) |
|  |  |  | polardb.g 4.4xlarge .2 | 32 CPU cores and 128 GB of memory | 12,800 | 160,000 |  |
|  |  |  | polardb.g 8.4xlarge .2 | 32 CPU cores and 256 GB of memory | 25,600 | 240,000 |  |
|  |  | Dedicate d host | polardb.x 8.12xlarg e.2 | 88 CPU cores and 710 GB of memory | 12,100 | 450,000 |  |
|  |  |  | polardb.x 4.mediu m.2 | 2 CPU cores and 8 GB of memory | 3,300 | 10,000 |  |
|  |  |  | polardb.x 8.mediu m.2 | 2 CPU cores and 16 GB of memory | 3,300 | 15,000 |  |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

|  |  |  | polardb.x 4.large.2 | 4 CPU cores and 16 GB of memory | 3,300 | 20,000 |  |
|---|---|---|---|---|---|---|---|
|  | 14 and 11.2 | Dedicate d |  |  |  |  | 20 GB- 3000 GB (Step size: 5 GB) |
|  |  |  | polardb.x 8.large.2 | 4 CPU cores and 32 GB of memory | 3,300 | 30,000 |  |
|  |  |  | polardb.x 4.xlarge. 2 | 8 CPU cores and 32 GB of memory | 3,300 | 40,000 |  |
|  |  |  | polardb.x 8.xlarge. 2 | 8 CPU cores and 64 GB of memory | 12,100 | 60,000 |  |
|  |  |  | polardb.x 4.2xlarge .2 | 16 CPU cores and 64 GB of memory | 12,100 | 80,000 |  |
|  |  |  | polardb.x 8.2xlarge .2 | 16 CPU cores and 128 GB of memory | 12,100 | 120,000 |  |
|  |  |  | polardb.x 4.4xlarge .2 | 32 CPU cores and 128 GB of memory | 12,800 | 160,000 | 20 GB- 6000 GB (Step size: 5 GB) |
|  |  |  | polardb.x 8.4xlarge .2 | 32 CPU cores and 256 GB of memory | 25,600 | 240,000 |  |
|  |  |  | polardb.x 8.8xlarge .2 | 64 CPU cores and 512 GB of memory | 12,100 | 240,000 |  |
| > Document | Version: 202 | 60629 |  |  |  |  | 1 |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

|  |  | Dedicate d host | polardb.x 8.12xlarg e.2 | 88 CPU cores and 710 GB of memory | 12,100 | 450,000 |  |
|---|---|---|---|---|---|---|---|

ApsaraDB RDS for PolarDB User ApsaraDB for RDS ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Log on to the ApsaraDB

**RDS console**

This topic describes how to log on to the ApsaraDB RDS console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.
1. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
2. Click **Log On**.
3. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable**
**MFA** topic in **Apsara Uni-manager Management Console User Guide** .
4. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Quick Start

### Procedure

ApsaraDB RDS quick start covers the following operations: creating an instance, configuring a whitelist, creating a database, creating an account, and connecting to the instance.

**Flowchart for a PolarDB instance**

If you are using ApsaraDB RDS for the first time, you can start with Limits on PolarDB. The following figure shows the operations that you must perform before you use a PolarDB instance.

### Create an instance

This topic describes how to create a PolarDB instance in the console.

| Section | Paramete r | Description |
|---|---|---|
| Basic configura tion | Organizat ion | The organization to which the instance belongs. |
|  | Resource Set | The resource set to which the instance belongs. |
| Area | Geograph y | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|  | Deploym ent Scenario | Specifies whether to deploy the primary and secondary instances in separate zones. Valid values: Multi-AZ deployment and Single-AZ deployment. If you select Multi-AZ deployment, you must configure the Secondary Node Availability Zone parameter. |
|  | Primary Node Availabili ty Zone | The zone in which the primary instance is deployed. |
|  | Secondar y Node Availabili ty Zone | The zone in which the secondary instance is deployed. This parameter is available only when you set the Deployment Scenario parameter to Multi-AZ deployment. Note If you select the same zone for both the primary and secondary instances, the deployment is equivalent to single-zone deployment. |
|  | Database Type | The database engine of the instance. Select POLARDB. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, click **Create Instance** in the upper-right corner.
3. Configure the following parameters.

| ide·Quick Star |  |  |
|---|---|---|
| Specificat ion Configura tion |  |  |
|  | Chip Architect ure | The chip architecture of the host on which the instance is deployed. Note If you do not have permissions to select an option, contact the operations administrator to grant such permissions to your account. |
|  | Compatib ility | The type of the database engine. PostgreSQL Oracle Syntax Compatibility |
|  | Database Version | The version of the database. Valid values: 14 Note If you set the Compatibility parameter to PostgreSQL, you can select only 14. 11.2 or 14 Note If you set the Compatibility parameter to Oracle Syntax Compatibility, you can select 11.2 or 14. |
|  | Series | The edition of the instance. Valid values: High-availability Edition Read-only instance |
|  | Storage Type | The storage type of the instance. Select Local SSD. |
|  | Open TDE | Specifies whether to enable the Transparent Data Encryption (TDE) feature. Note You cannot disable the TDE feature after it is enabled. |

|  | Encryptio n Algorithm | The encryption algorithm. Default value: aes-256. Valid values: aes-256 sm4 Note This parameter is required if you enable the TDE feature. After the instance is created, the value of this parameter cannot be changed. |
|---|---|---|
|  | Instance specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. |
|  | Storage space | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. |
| Network | Network Connecti on Type | The connection type of the instance. Valid values: Public network connection: Instances of this connection type can be connected over the Internet. Intranet connection: Instances of this connection type can be connected over an internal network. Note After the instance is created, the value of this parameter cannot be changed. Proceed with caution. |
|  | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. |
|  | VPC | The VPC in which you want to create the instance. Note When Network Type is set to Proprietary Network, you must specify this parameter. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

|  | VSwitch | The zone in which the vSwitch is located. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
|---|---|---|
|  | VSwitch | The vSwitch to which the instance is connected. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
|  | IP whitelists | The IP addresses that are allowed to connect to the instance. |
|  | Create Quantity | The number of instances that you want to create. Default value: 1. |
| Instance Settings |  |  |
|  | Instance name | The name of the instance. The name must be 2 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, and the following special characters: -: _ The name cannot start with http:// or https://. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
4. Click **Confirm Order**.

### Configure an IP address

**whitelist**

This topic describes how to configure a whitelist for a PolarDB instance. Only entities that are listed in a whitelist can access your PolarDB instance.

**Background information**

Whitelists make your PolarDB instance more secure and do not interrupt the operations of your PolarDB instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the PolarDB instance.

**Note**

The default IP address whitelist contains only the IP address 127.0.0.1. This indicates that no devices are allowed to access the PolarDB instance. Configure an ECS security group: Add an ECS security group for the PolarDB instance to

| Parameter | Description |
|---|---|
| Database Account | The username of the account must be 2 to 16 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a lowercase letter and end with a lowercase letter or a digit. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User allow ECS instances in the group to connect to the PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

**Note**

You can also click **Create Whitelist** to create a whitelist.
6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that are allowed to
access the instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your PolarDB instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Apsara Stack account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### Create a database and an

**account**

Before you start to use PolarDB, you must create a database and an account for a PolarDB instance. This topic describes how to create a database and an account on a PolarDB instance. You can create privileged and standard accounts on a PolarDB instance. The following section describes how to create a privileged account.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. Click **Create Privileged Account** and configure the following parameters.

| Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ! @ # $ % ^ & * ( ) + - = _ |
|---|---|
| Re-enter Password | Enter the same password again. |

| Parameter | Description |
|---|---|
| Database Account | The username of the account must be 2 to 16 characters in length. It can contain lowercase letters, digits, and underscores ( ). _ It must start with a lowercase letter and end with a lowercase letter or a digit. |
| Password | The password must be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: ! @ # $ % ^ & * ( ) + - _ = |
| Re-enter Password | Enter the same password again. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
6. Click **Create**.

**Create a privileged account**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. Click **Create Privileged Account** and configure the following parameters.
6. Click **OK**.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. Click **Log On to Database** in the upper-right corner of the page.
5. In the **Log on to Database Instance** dialog box of the **DMS** console, check the values of
**Database Type**, **Instance Region**, and **Connection string address**. If the values are
correct, specify the **Database Account** and **Database password** parameters.

| Parameter | Description |
|---|---|
| Database Type | The engine of the database. By default, the engine of the database to be connected is selected. |
| Instance Region | The region where the instance is deployed. By default, the region of the current instance is selected. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is specified. |
| Database Account | The username of the database account. |
| Database password | The password of the database account. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

**Note**

If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For information about how to connect to a host, see Configure an IP address whitelist.
7. The **SQLConsole** page appears after you log on to the instance. Execute a statement in the
following format to create a database: ApsaraDB RDS for PolarDB User ApsaraDB for RDS

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

### Connect to an instance

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an ApsaraDB RDS instance.

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the ApsaraDB RDS instance. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the ApsaraDB RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |
| Username | The name of the privileged account for the ApsaraDB RDS instance. For more information about how to create an privileged account, see Create a database and an account. |
| Password | The password of the privileged account. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User Data Management (DMS) is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational and non-relational databases, such as MySQL, SQL Server, and PostgreSQL. It can also be used to manage Linux servers. You can also use a database client to connect to an ApsaraDB RDS instance. ApsaraDB RDS is fully compatible with PolarDB. You can connect to PolarDB instances in the similar manner as you would connect to an open source PolarDB database. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an ApsaraDB RDS instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Use DMS to log on to a PolarDB instance.

**Use the pgAdmin 4 client to connect to an ApsaraDB RDS**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Start the pgAdmin 4 client.

**Note**

For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows).
3. Right-click **Servers** and choose **Create > Server**, as shown in the following figure.
4. On the **General** tab of the **Create - Server** dialog box, enter the name of the server, as
shown in the following figure.
5. Click the **Connection** tab and enter the information of the instance, as shown in the
following figure.
6. Click **Save**.
7. If the connection information is correct, choose **Servers > Server Name > Databases >**
**postgres**. If the following page appears, the connection is established.

**Important**

The postgres database is the default system database of the ApsaraDB RDS instance. Do not perform operations on this database.

| Section | Configura tion | Description |
|---|---|---|
| Basic configura tion | Organizat ion | The organization to which the instance belongs. |
|  | Resource Set | The resource set to which the instance belongs. |
| Area | Geograph y | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|  | Deploym ent Scenario | Specifies whether to deploy the primary and secondary instances in separate zones. Valid values: Multi-AZ deployment and Single-AZ deployment. If you select Multi-AZ deployment, you must configure the Secondary Node Availability Zone parameter. |
|  | Primary Node Availabili ty Zone | The zone in which the primary instance is deployed. |
|  | Secondar y Node Availabili ty Zone | The zone in which the secondary instance is deployed. This parameter is available only when you set the Deployment Scenario parameter to Multi-AZ deployment. Note If you select the same zone for both the primary and secondary instances, the deployment is equivalent to single-zone deployment. |
|  | Database Type | The database engine of the instance. Select POLARDB. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Instances

### Create an instance

This topic describes how to create a PolarDB instance in the console.
1. Log on to the ApsaraDB for RDS console.
2. On the **Instances** page, click **Create Instance** in the upper-right corner.
3. Configure the following parameters.

| saraDB for RD | ApsaraDB RDS for PolarDB User S Guide·Instance |  |
|---|---|---|
| Specificat ion Configura tion |  |  |
|  | Chip Architect ure | The chip architecture of the host on which the instance is deployed. Note If you do not have permissions to select an option, contact the operations administrator to grant such permissions to your account. |
|  | Compatib ility | You can select a database engine type. PostgreSQL Oracle Syntax Compatibility |
|  | Database Version | The version of the database. Valid values: 14 Note If you set the Compatibility parameter to PostgreSQL, you can select only 14. 11.2 or 14 Note If you set the Compatibility parameter to Oracle Syntax Compatibility, you can select 11.2 or 14. |
|  | Series | The edition of the instance. Valid values: High-availability Edition Read-only instance |
|  | Storage Type | The storage type of the instance. Select Local SSD. |
|  | Open TDE | Specifies whether to enable the Transparent Data Encryption (TDE) feature. Note You cannot disable the TDE feature after it is enabled. |

|  | Encryptio n Algorithm | The encryption algorithm. Default value: aes-256. Valid values: aes-256 sm4 Note This parameter is required if you enable the TDE feature. An instance cannot be modified after it is created. |
|---|---|---|
|  | Instance specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. You can click AI-powered Instance Type Recommendation and enter your scenario in Apsara Assistant to get the best instance type recommendation that balances cost and performance. |
|  | Storage space | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the instance. |
|  | Network Connecti on Type | RDS provides the following two types of endpoints: Public network connection: Instances of this connection type can be connected over the Internet. Intranet connection: Instances of this connection type can be connected over an internal network. Note After the instance is created, the value of this parameter cannot be changed. Proceed with caution. |
|  | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Proprietary Network: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. For security purposes, we recommend that you select the VPC network type. |
|  | VPC | Select your VPC. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
| Network |  |  |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

|  | VSwitch | The zone in which the vSwitch is located. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
|---|---|---|
|  | VSwitch | You can select the vSwitch in the VPC. Note When Network Type is set to Proprietary Network, you must specify this parameter. |
|  | IP whitelists | The IP addresses that are allowed to connect to the instance. |
|  | Create Quantity | The number of instances that you want to create. Default value: 1. |
| Instance Settings |  |  |
|  | Instance name | The name of the instance. The name must be 2 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, and the following special characters: -: _ The name cannot start with http:// or https://. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
4. Click **Confirm Order**.

### Restart an instance

This topic describes how to manually restart an ApsaraDB RDS instance. This applies if the number of connections exceeds a specific threshold or if an instance has performance issues.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the upper-right corner of the page, click **Restart Instance**.

**Important**

When you restart an instance, a network interruption occurs. We recommend that you make appropriate arrangements for your workloads and make sure that your applications are configured with automatic reconnection policies.
5. In the message that appears, click **Confirm**.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS

### Set a maintenance window

This topic describes how to set a maintenance window for an ApsaraDB RDS instance. To ensure the stability of ApsaraDB RDS instances, the backend system performs maintenance of the instances at irregular intervals. The default maintenance window is from 02:00 to 06:00. You can set the maintenance window to the off-peak period of your business to avoid impact on business.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the **Configuration Information** section, click **Configure** to the right of **Maintenance**
**Window**.
5. Select a maintenance window and click **Save**.

**Note**

The maintenance window is in UTC+8. Before the maintenance starts, ApsaraDB RDS sends text messages and emails to the contacts that are associated with your Apsara Stack account. To ensure the stability of the maintenance process, the instance changes to the Maintaining Instance state before the maintenance window. When the instance is in this state, access to data in the database and query operations such as performance monitoring are not affected. However, apart from account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. During the maintenance window, one or two network interruptions may occur. Make sure that you configure automatic reconnection policies for your applications to avoid service disruptions.

### Configure primary/secondary

**switchover**

ApsaraDB RDS provides the primary/secondary switchover feature to ensure the high availability of databases. The primary/secondary switchover is performed when the primary instance becomes unavailable. You can also manually switch your business to the secondary instance. This topic describes how to manually switch over services between a primary instance and its secondary instance.

**Background information**

Data is synchronized in real time between the primary and secondary instances. You can access only the primary instance. The secondary instance serves only as a backup instance and does not allow external access. After the switchover, the original primary instance becomes the secondary instance.

**Note**

During a switchover, a network interruption may occur. Make sure that your applications are configured with automatic reconnection policies. ApsaraDB for RDS ApsaraDB RDS for PolarDB User
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Service Availability**.
5. In the **Availability Information** section, click **Switch Primary/Secondary Instance**.
6. In the **Switch Primary/Secondary Instance** dialog box, click **OK**.

**Note**

During the switchover, operations such as managing databases and accounts and changing network types cannot be performed. Therefore, we recommend that you select Switch Within Maintenance Window. For more information about how to set a maintenance window, see Set a maintenance window.

### Release an instance

This topic describes how to manually release a PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Actions** column corresponding to the instance, click **More** and select **Release**
**Instance** from the drop-down list.

**Note**

After an instance is released, the instance data is immediately deleted. We recommend that you back up the data and download the backup file before you release an instance. For more information, see Back up a PolarDB instance and Download backup files.
4. In the message that appears, click **Confirm**.

### Read-only instance

#### Overview

PolarDB allows you to create read-only instances. In scenarios where PolarDB has a small number of write requests but a large number of read requests, you can create read-only instances to distribute database access loads away from the primary instance. This topic describes the features and limits of read-only instances. If a large number of read requests overwhelm the primary instance, your business may be interrupted. In this case, you can create one or more read-only instances to offload read requests from the primary instance. This scales the read capability of your database system and increases the throughput of your application. ApsaraDB RDS for PolarDB User ApsaraDB for RDS Each read-only instance works in a single-node architecture, where no instances are provided as backups. Data updates of the primary instance are automatically synchronized to all readonly instances immediately after the primary instance completes operations. Read-only instances reside within the same region as the primary instance, but possibly in different zones. The following figure shows the topology of read-only instances. Read-only instances have the following features: Specifications of a read-only instance can be different from those of the primary instance and can be changed at any time, which facilitates elastic scaling. Read-only instances do not require account or database maintenance. Account and database information is synchronized with the primary instance. The whitelists of read-only instances can be configured independently. System performance monitoring is provided. PolarDB provides a variety of optimization recommendations, such as storage engine check, primary key check, large table check, and check for excessive indexes and missing indexes. You can optimize your databases based on the optimization recommendations and specific applications.

#### Create a read-only instance

This topic describes how to create a read-only instance, which you can use to handle large numbers of read requests.

**Precautions**

You can create up to five read-only instances. Backup settings and temporary backup are not supported. Instance restoration is not supported. Data migration to read-only instances is not supported. Database creation and deletion are not supported. Account creation, deletion, authorization, and password changes are not supported. After a read-only instance is created, you cannot restore data by directly overwriting the primary instance with a backup set.

| Item | Parameter | Description |
|---|---|---|
| Area | Region | The region in which you want to create the read- only instance. |
| Specifications | Database Engine | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|  | Engine Version | The version of the database engine, which is the same as that of the primary instance and cannot be changed. |
|  | Edition | Set the value to Read-only. |
|  | Instance Specifications | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|  | Storage Capacity | The storage capacity of the read-only instance. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type and storage capacity as the primary instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| Network | Network Type | The network type of the read-only instance. This must be the same as that of the primary instance and cannot be changed. |
|  | VPC | The VPC in which you want to create the read- only instance. This parameter is required when Network Type is set to VPC. |
|  | vSwitch | The vSwitch in the VPC. This parameter is required when Network Type is set to VPC. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the **Distributed by Instance Role** section on the right side of the **Basic Information**
page, click **Create Read-only Instance**.
4. On the **Create Read-only RDS Instance** page, configure the read-only instance
parameters.
5. After you configure the preceding parameters, click **Submit**.

#### View details of read-only instances

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View details of a read-only instance from the Instances page**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click the ID of a read-only instance. The **Basic Information** page
appears. In the instance list, **Instance Role** of read-only instances is displayed as **Read-only**
**Instance**, as shown in View a read-only instance.

**View details of a read-only instance from the Basic Information**

**page of the primary instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. On the **Basic Information** page, move the pointer over the number below **Read-only**
**Instance** in the **Distributed by Instance Role** section. The ID of the read-only instance is
displayed.
4. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

### Change the specifications of

**an instance**

This topic describes how to change the instance type and storage space of a PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the **Configuration Information** section of the **Basic Information** page, click **Change**
**Specifications**.

**Important**

While you change specifications of an instance, a network interruption of about 30 seconds may occur, and most of the operations related to databases, accounts, and network operations cannot be performed. We recommend that you make appropriate arrangements for you workloads before you change specifications.
5. Change specifications based on your business requirements and click **Submit**.

### Set instance parameters

You can use the console to view and modify the values of some parameters and view the parameter modification history.

**Modify parameter values**

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**yp**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Parameter Settings**.
5. You can perform the following operations:
Export parameters Click **Export Parameters** to save the parameter file in TXT format to your local computer. This TXT file contains all parameter values for the instance. Modify parameters in a batch i. After you modify the exported parameter file, click **Import Parameters** and paste the content of the parameter file into the dialog box.

**Note**

Select **Show Modified Parameters Only** to view the modified parameters. ii. Click **OK**. iii. In the upper-right corner, click **Submit Parameters**.

**Note**

If a parameter modification requires an instance restart to take effect, the system prompts you to restart the instance. We recommend that you perform this operation during off-peak hours and make sure that your application has a reconnection mechanism. You can click **Cancel** to discard the modifications before they are submitted. Modify a single parameter i. In the **Modifiable Parameters** list, find the parameter that you want to modify and click the icon in the **Running Parameter Value** column. ii. Enter a parameter value within the displayed value range. iii. Click **OK**.

**Note**

Select **Show Modified Parameters Only** to view the modified parameters. iv. In the upper-right corner, click **Submit Parameters**.

**Note**

If a parameter modification requires an instance restart to take effect, the system prompts you to restart the instance. We recommend that you perform this operation during off-peak hours and make sure that your application has a reconnection mechanism. You can click **Cancel** to discard the modifications before they are submitted.

| Parameter | Maj or vers ion | Def ault valu e | Value range | Res tart req uire d | Description |
|---|---|---|---|---|---|
| archive mod _ e | 14, 11.2 | on | [alway s\|on\|of f] | Yes | ARCHIVELOG mode. In addition to off which disables the mode, two other modes are available: on and always. During normal operations, these two modes are identical. However, when set to always, the WAL archiving process remains enabled even during archive recovery or in standby mode. In always mode, all files restored from the archive or transferred via streaming replication are archived again. |
| auto explain. _ log analyze _ | 14, 11.2 | off | [on\|off ] | No | Controls whether to log the execution plan and analysis information of a query. If you enable this parameter, detailed performance data is provided, but this increases overhead. |
| auto explain. _ log buffers _ | 14, 11.2 | off | [on\|off ] | No | Controls whether to log buffer usage during query execution. If you enable this parameter, you can analyze query performance issues and check whether performance is degraded due to insufficient buffers. |
| auto explain. _ log format _ | 14, 11.2 | text | [text\|x ml\|jso n\|yaml ] | No | Specifies the output format of the query plan logs generated by the auto-explain module. The valid values typically include text (default, plain text format) and json (structured JSON format). This parameter controls the readability or machine parsability of the logs. |
| auto explain. _ log min dura _ _ tion | 14, 11.2 | -1 | [-1- 21474 83647 ] | No | Sets the minimum running time threshold for a query in milliseconds. Queries that exceed this threshold are logged. The default value is -1, which indicates that no queries are logged. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

**View parameter modification history**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Parameter Settings**.
5. Click the **Parameter Modification History** tab.
6. Select a time range and click **OK**.

**Parameter descriptions**

| auto explain. _ log nested s _ _ tatements | 14, 11.2 | off | [on\|off ] | No | Controls whether to log the execution plans of nested SQL statements, such as statements in functions or subtransactions. If you set this parameter to on, the execution plans of these statements are also logged, which helps you perform in-depth analysis of performance issues. |
|---|---|---|---|---|---|
| auto explain. _ log timing _ | 14, 11.2 | on | [on\|off ] | No | Controls whether to include timing information for each query step in the output of auto-explain. If you set this parameter to on, the running time is recorded. If you set it to off, timing information is not recorded. The default value is typically on. |
| auto explain. _ log triggers _ | 14, 11.2 | off | [on\|off ] | No | Controls whether to include trigger execution information in the auto explain log. If you set this _ parameter to on, the execution details of triggers are recorded, which helps you analyze the impact of triggers on query performance. The default value is off. |
| auto explain. _ log verbose _ | 14, 11.2 | off | [on\|off ] | No | Controls whether to include detailed plan information in the auto-explain output. If you set this parameter to on, more detailed query execution plans are recorded, including extra information for each node. The default value is off. |
| auto explain. _ sample rate _ | 14, 11.2 | 1 | [0-1] | No | Sets the probability for the auto-explain module to sample execution plans. This controls the logging frequency. The value ranges from 0 to 1, where 0 means no sampling and 1 means logging every time. |
| autovacuum _ max workers _ | 11.2 | 5 | [5-20] | Yes | Specifies the maximum number of autovacuum processes that can run at the same time, excluding the autovacuum launcher. |
| autovacuum _ vacuum cost _ delay _ | 14, 11.2 | 0 | [-1- 100] | No | Defines the time interval in milliseconds that the autovacuum process pauses after each cleanup operation. This is used to control the impact of cleanup on system performance. |
| autovacuum _ vacuum cost _ limit _ | 14, 11.2 | 100 00 | [-1- 10000 ] | No | Sets the cost limit for a single autovacuum operation. This is used to balance the impact of cleanup tasks on system performance. |
| checkpoint c _ ompletion ta _ rget | 11.2 | 0.9 | [0.0- 1.0] | No | Controls the completion target for checkpoint write operations. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| checkpoint ti _ meout | 11.2 | 300 | [1- 86400 ] | No | The maximum time between automatic WAL checkpoints. If you specify a value without a unit, the unit is seconds. |
|---|---|---|---|---|---|
| cron.polar all _ ow superuse _ r task _ | 11.2 | on | [on\|off ] | No | Allows pg cron to execute tasks as a superuser. _ |
| datestyle | 14 | 'ISO, YMD ' | ^'(MD Y\|ISO\| Postgr es\|SQL \|Germ an\|YM D\|... | No | Defines the display format for dates and times, and the default rules for parsing input. It affects the output style of dates, such as ISO, SQL, or Postgres, and the order of months and days, such as MDY or DMY. |
| dblink.polar _ auto port m _ _ apping | 11.2 | off | [on\|off ] | No | Specifies whether to enable automatic port mapping for DBLink. |
| dblink.polar _ connection c _ heck | 11.2 | off | [on\|off ] | No | Specifies whether to enable connection checking for DBLink. |
| dbms job.dat _ abase name _ | 11.2 | 'post gres' | ^'\w+' $ | Yes | The name of the database where dbms job tasks _ are stored. |
| default trans _ action deferr _ able | 14, 11.2 | off | [on\|off ] | No | Sets whether default transactions can be deferred. This controls whether transactions are allowed to be deferred in read-only mode to optimize performance. |
| default with _ _ oids | 14, 11.2 | 1 4: of f 1 1. 2: on | [on\|off ] | No | Determines whether to include an OID column by default when you create a new table. |
| default with _ _ rowids | 11.2 | on | [on\|off ] | No | Specifies whether to create new tables that support ROWID (OID with an index) by default. |
| enable partit _ ionwise aggr _ egate | 14, 11.2 | on | [on\|off ] | No | Controls whether to enable partition-wise aggregate operations. If you set this parameter to on, PostgreSQL attempts to perform aggregation on each partition of a partitioned table separately, which may improve query performance. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| enable partit _ ionwise join _ | 14, 11.2 | on | [on\|off ] | No | Controls whether to enable partition-wise join optimization. If you set this parameter to on, PostgreSQL attempts to perform more efficient join operations on partitioned tables to improve query performance. |
|---|---|---|---|---|---|
| extra float d _ _ igits | 14, 11.2 | 0 | [-15-3] | No | Controls the number of extra precision digits displayed for floating-point number types, such as float4 and float8. A negative value reduces precision, and a positive value increases precision. This affects the display format of floating-point numbers. |
| hot standby _ _ feedback | 11.2 | off | [on\|off ] | No | Controls whether a hot standby server provides feedback to the primary server to prevent long- running queries from causing rows on the primary server to be locked for too long. |
| idle in trans _ _ action sessio _ n timeout _ | 14, 11.2 | 360 000 0 | ^(0\| [1- 9]\d\d\ d\|\d{5 ,9}\|1\ d{9}\| 2000... | No | Sets the timeout for idle transaction sessions. Sessions that exceed this time are automatically terminated. |
| idle session _ _ timeout | 14 | 864 000 00 | [0- 21474 83647 ] | No | Sets the maximum duration for an idle session before it is automatically terminated. |
| jit | 14, 11.2 | off | [on\|off ] | No | Controls whether PostgreSQL enables the Just-In- Time (JIT) compilation feature to accelerate query execution. A value of on enables the feature, and off disables it. |
| lock timeout _ | 14, 11.2 | 0 | ^(0\| [1- 9]\d\d\ d\|\d{5 ,9}\|1\ d{9}\| 2000... | No | Sets the timeout for acquiring a lock in a single database transaction. If the time is exceeded, the attempt is aborted and an error is reported. The unit is milliseconds. A value of 0 means no timeout. |
| log connecti _ ons | 14, 11.2 | off | [on\|off ] | No | Controls whether to log client connection and disconnection events in the PostgreSQL log file. |
| log disconne _ ctions | 14, 11.2 | off | [on\|off ] | No | Controls whether the PostgreSQL database logs client disconnection information. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| log min dura _ _ tion stateme _ nt | 14, 11.2 | 1 4: 1 0 0 0 1 1. 2: 5 0 0 0 | [-1- 21474 83647 ] | No | Logs SQL statements whose running time exceeds the specified number of milliseconds. This is used to identify slow queries. A value of 0 logs all statements, and -1 logs none. |
|---|---|---|---|---|---|
| log stateme _ nt | 14, 11.2 | ddl | [none\| ddl\|m od\|all] | No | Controls which SQL statements are logged by PostgreSQL. You can set this parameter to one of the following values: none: No SQL statements are logged. ddl: Only data definition language (DDL) statements are logged, such as CREATE, ALTER, and DROP. mod: All data modification statements, such as INSERT, UPDATE, and DELETE, and DDL statements are logged. all: All SQL statements are logged. |
| log temp file _ _ s | 14, 11.2 | 100 000 | [-1- 21474 83647 ] | No | Sets the threshold for logging the size of temporary files in kilobytes. When the size of a temporary file, such as a file generated by a sort or hash operation, exceeds this value, PostgreSQL logs the related information. A value of -1 indicates that no information about temporary files is logged. |
| log timezone _ | 14, 11.2 | 1 4: U T C 1 1. 2: P R C | ^'(((U TC)(-) {0,1} (\d\|[1- 9]\d\|1( [0-5... | No | Sets the time zone used in PostgreSQL log records to standardize the display of log times. The default value is typically the system time zone. |
| max parallel _ maintenanc _ e workers _ | 11.2 | 2 | [0- 1024] | No | Sets the maximum number of parallel processes for each maintenance operation. |
| max parallel _ workers _ | 11.2 | 8 | [0- 512] | No | Sets the maximum number of workers that the system can support for parallel operations. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| max parallel _ workers per _ _ gather _ | 11.2 | 2 | [0- 512] | No | Sets the maximum number of parallel processes for each executor node. |
|---|---|---|---|---|---|
| min parallel _ _ index scan s _ _ ize | 14, 11.2 | 64 | [0- 71582 7882] | No | Sets the minimum table size required for a parallel index scan. Tables smaller than this size do not use parallel scans. |
| min parallel _ _ table scan si _ _ ze | 14, 11.2 | 102 4 | [0- 71582 7882] | No | Sets the minimum table size that can be processed in parallel for a table scan. |
| old snapshot _ threshold _ | 14, 11.2 | -1 | [-1- 86400 ] | Yes | Controls the expiration time threshold for old snapshots. Snapshots that exceed this time are cleaned up to prevent excessive resource consumption. A negative value, such as -1, disables automatic cleanup. The unit is minutes. |
| pg bigm.ena _ ble recheck _ | 11.2 | on | [on\|off ] | No | Specifies whether to recheck if heap tuples fetched from the index match the query. |
| pg bigm.gin _ _ key limit _ | 11.2 | 0 | [0- 21474 83647 ] | No | Sets the maximum number of bigram keys allowed for a GIN index search. |
| pg bigm.simi _ larity limit _ | 11.2 | 0.3 | [0.0- 1.0] | No | Sets the similarity threshold used by the =% operator. |
| pg stat state _ _ ments.enabl e superuser _ _ track | 11.2 | off | [on\|off ] | No | Specifies whether to enable the tracking feature of pg stat statements and record SQL _ _ statements executed by superusers. |
| polar case s _ _ ensitive for _ _ columnref | 11.2 | off | [on\|off ] | No | Enables compatibility with Oracle's case-sensitive mode for columns. |
| polar comp _ _ custom plan _ tries _ | 11.2 | 5 | [-1- 100] | No | Sets the maximum number of custom plans that the planner considers. |
| polar comp _ _ dynatune | 11.2 | 0 | [0- 100] | Yes | Sets the PolarDB utilization percentage. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| polar comp _ _ dynatune pr _ ofile | 11.2 | oltp | [oltp\|r eporti ng\|mix ed] | Yes | Sets the workload mode for dynatune. |
|---|---|---|---|---|---|
| polar comp _ _ enable pruni _ ng | 1.2 | off | [on\|off ] | No | Enables the early exclusion feature of the planner for partitioned tables. |
| polar comp r _ _ edwood date _ | 11.2 | on | [on\|off ] | No | Sets whether the behavior of the DATE type is similar to TIMESTAMP. |
| polar comp r _ _ edwood grea _ test least _ | 11.2 | on | [on\|off ] | No | Sets whether the behavior of the GREATEST and LEAST functions should follow the Redwood or PostgreSQL standard. |
| polar comp r _ _ edwood raw _ names _ | 11.2 | on | [on\|off ] | No | Specifies whether the Redwood interface directly returns the raw object names stored in the PostgreSQL system catalog. |
| polar comp r _ _ edwood strin _ gs | 11.2 | on | [on\|off ] | No | Treats NULL as an empty string when concatenating with TEXT values. |
| polar comp _ _ stmt level tx _ _ | 11.2 | on | [on\|off ] | No | Allows error processing to continue without a transaction abort. |
| polar empty _ string is nul _ _ _ l enable _ | 11.2 | on | [on\|off ] | No | Specifies whether to treat empty strings as NULL, similar to Oracle. |
| polar enable _ inline cte _ _ | 11.2 | on | [on\|off ] | No | Specifies whether to allow the planner to inline common table expressions (CTEs). |
| polar enable _ cic on parti _ _ _ tioned | 14 | on | [on\|off ] | No | Controls whether to enable Constraint Exclusion on partitioned tables. If you set this parameter to on, the optimizer automatically skips unnecessary partition scans based on partition constraints, which improves query performance. If you set it to off, this feature is disabled. The default value is typically on. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| polar enable _ convert or t _ _ _ o union all _ _ | 14 | off | [on\|off ] | No | Controls whether to optimize OR conditions in SQL queries by converting them to the UNION ALL format. Enabling this feature can improve query performance in specific scenarios but may increase the complexity of the query plan. on: Enables the conversion. off: Disables the conversion. This is the default value. |
|---|---|---|---|---|---|
| polar enable _ create table _ _ as bulk ins _ _ _ ert | 14 | on | [on\|off ] | No | Specifies whether to enable the optimization feature for bulk inserts using the CREATE TABLE AS statement. |
| polar enable _ ddl replicati _ _ on | 14 | on | [on\|off ] | No | Specifies whether to enable the replication feature for data definition language (DDL) operations. If you enable this parameter, DDL operations on the primary node are synchronously replicated to the secondary node to ensure table schema consistency between the primary and secondary nodes. |
| polar enable _ pgstat in sh _ _ _ ared storage _ | 14, 11.2 | on | [on\|off ] | No | Specifies whether to enable the feature of saving PostgreSQL performance statistics in shared storage. |
| polar enable _ union all nu _ _ _ ll coerce _ | 11.2 | on | [on\|off ] | No | Enables type coercion for NULL values in UNION ALL operations. |
| polar failove _ r slot mode _ _ | 11.2 | sync | [sync\| async\| off] | No | None. |
| polar idle in _ _ twophase ti _ _ meout | 11.2 | 0 | [0- 21474 83647 ] | No | Sets the maximum allowed idle time in the non- transactional execution phase of a two-phase commit protocol (2PC) transaction. |
| polar mini fl _ _ ogindex loca _ l buffers _ | 11.2 | 204 80 | [8- 10737 41823 ] | No | Sets the number of local buffers for the mini flashback log index for each flashback table operation. Each buffer is 8 KB in size. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| polar mini xl _ _ ogindex loca _ l buffers _ | 11.2 | 102 40 | [8- 10737 41823 ] | No | Sets the number of local buffers for the mini WAL log index for each flashback table operation. Each buffer is 16 KB in size. |
|---|---|---|---|---|---|
| polar plsql e _ _ nable holdab _ le refcursor _ | 11.2 | on | [on\|off ] | No | Allows plsql to hold a reference cursor (refcursor) by default. |
| polar px dop _ _ per node _ _ | 11.2 | 3 | [1- 128] | No | Sets the maximum number of parallel worker processes that can be executed concurrently on each node in a PolarDB for PostgreSQL database. |
| polar enable _ px _ | 14 | off | [on\|off ] | No | Specifies whether to enable the parallel execution feature. |
| polar num p _ _ arts for pts _ _ | 14 | 32 | [-1- 21474 83647 ] | No | Specifies the number of partitions for parallel transmission in PolarDB. This affects the efficiency and resource allocation of parallel processing. |
| polar px dop _ _ per node _ _ | 14 | 3 | [1- 128] | No | The degree of parallelism (DOP) per node. This controls the number of parallel execution threads for queries on each node in PolarDB for PostgreSQL. A higher value can improve query performance but also increases resource consumption. |
| polar px ena _ _ ble adps _ | 14 | off | [on\|off ] | No | Specifies whether to enable the Advanced Data Processing Service (ADPS) feature of PolarDB to optimize complex queries and large-scale data processing performance. The value is of Boolean type (on/off). |
| polar px ena _ _ ble create ta _ _ ble as _ | 14 | on | [on\|off ] | No | Specifies whether to enable the feature of creating tables using the CREATE TABLE AS statement. |
| polar px ena _ _ ble cte _ | 14 | on | [on\|off ] | No | Specifies whether to enable optimization support for common table expressions (CTEs). |
| polar px ena _ _ ble cte shar _ _ ed scan _ | 14 | on | [on\|off ] | No | Controls whether to enable shared scan optimization for common table expressions (CTEs) to improve query performance. |
| polar px ena _ _ ble explain _ _ all stat _ | 14 | off | [on\|off ] | No | If you enable this parameter, the EXPLAIN command displays statistics for all nodes. This is used to analyze and optimize query plans. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| polar px ena _ _ ble join pref _ _ etch inner _ | 14 | on | [on\|off ] | No | Controls whether to enable the inner table prefetch feature in parallel join operations to optimize query performance. |
|---|---|---|---|---|---|
| polar px ena _ _ ble left inde _ _ x nestloop j _ _ oin | 14, 11.2 | 1 4: of f 1 1. 2: on | [on\|off ] | No | Controls whether to enable the Left Index Nestloop Join optimization strategy. If you set this parameter to on, this optimization method is allowed to improve query performance. If you set it to off, this feature is disabled. |
| polar px ena _ _ ble partition _ | 14, 11.2 | on | [on\|off ] | No | Specifies whether to enable the partitioned table feature. If you enable this parameter, parallel query optimization for partitioned tables is supported. |
| polar px ena _ _ ble partition _ hash _ | 14 | on | [on\|off ] | No | Enables or disables the hash distribution feature for partitioned tables to optimize parallel query performance for large-scale partitioned tables. |
| polar px ena _ _ ble plpgsql _ | 14 | on | [on\|off ] | No | Specifies whether to enable PL/pgSQL language support. If you set this parameter to on, you can use PL/pgSQL to write stored procedures and functions in PolarDB for PostgreSQL. |
| polar px ena _ _ ble prepare _ _ statement | 14 | on | [on\|off ] | No | Specifies whether to enable the Prepare Statement feature to optimize query execution efficiency. |
| polar px ena _ _ ble pre opti _ _ mizer check _ | 14 | on | [on\|off ] | No | Controls whether to enable pre-optimizer checks for additional logical validation and optimization preparation before query optimization. |
| polar px ena _ _ ble procedur _ e | 14 | on | [on\|off ] | No | Specifies whether to enable the feature of executing stored procedures in parallel in PolarDB. |
| polar px ena _ _ ble result ha _ _ sh filter _ | 14 | on | [on\|off ] | No | Controls whether to enable the result hash filtering feature to optimize query execution performance. |
| polar px ena _ _ ble spi read _ _ _ all namespa _ ces | 14 | off | [on\|off ] | No | Specifies whether to allow reading data from all namespaces through the SPI interface. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| polar px ena _ _ ble subquery _ | 14 | on | [on\|off ] | No | Controls whether to enable parallel execution optimization for subqueries. If you set this parameter to on, subqueries are processed in parallel to improve performance. If you set it to off, this feature is disabled. |
|---|---|---|---|---|---|
| polar px ena _ _ ble tableless _ scan _ | 14 | off | [on\|off ] | No | Specifies whether to enable the tableless scan feature to optimize query performance. |
| polar px ena _ _ ble window f _ _ unction | 14 | on | [on\|off ] | No | Enables or disables the window function feature in PolarDB for PostgreSQL. |
| polar px ign _ _ ore function _ | 14, 11.2 | '157 4,15 75,1 576, 176 5,30 78,4 032' | ^'[1- 9]\d*(, [1- 9]\d*)* ?'$ | No | Controls whether to ignore the execution of certain functions. This is typically used in debugging or optimization scenarios. |
| polar px inte _ _ rconnect tra _ nsmit timeo _ ut | 14 | 360 0 | [1- 7200] | No | Sets the timeout for communication transmission between PolarDB PX nodes. This controls the maximum waiting time for data transmission. |
| polar px ma _ _ x slices _ | 14 | 50 | [0- 21474 83647 ] | No | Controls the maximum number of slices in a parallel query. This affects the granularity and resource allocation of parallel execution. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| polar px opti _ _ mizer bitma _ pscan factor _ | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Adjusts the cost factor for bitmap scans in the PolarDB parallel query optimizer. This affects the selection priority of bitmap scans in the query plan. A larger value makes the optimizer more likely to choose other scan methods. |
|---|---|---|---|---|---|
| polar px opti _ _ mizer enable _ brinscan _ | 14 | on | [on\|off ] | No | Specifies whether to enable optimizer support for BRIN index scans. If you set this parameter to on, the optimizer is allowed to consider using BRIN indexes to accelerate queries. If you set it to off, the optimizer ignores BRIN indexes. |
| polar px opti _ _ mizer enable _ crossproduc _ t | 14 | off | [on\|off ] | No | Specifies whether to enable the cross-product optimizer feature. |
| polar px opti _ _ mizer enable _ dynamicind _ exscan | 14 | on | [on\|off ] | No | Specifies whether to enable the dynamic index scan optimizer feature. |
| polar px opti _ _ mizer enable _ dynamicsha _ reindexscan | 14 | on | [on\|off ] | No | Enables or disables the optimizer's dynamic shared index scan feature to improve query performance. |
| polar px opti _ _ mizer enable _ dynamictabl _ escan | 14 | on | [on\|off ] | No | Specifies whether to enable the dynamic table scan optimizer feature. |
| polar px opti _ _ mizer enable _ groupagg _ | 14 | on | [on\|off ] | No | Controls whether to enable the Group Aggregate feature in the PolarDB parallel execution optimizer. If you set this parameter to on, group aggregation operations are executed in parallel to improve performance. If you set it to off, this feature is disabled. The default value is typically on. |
| polar px opti _ _ mizer enable _ hashagg _ | 14 | on | [on\|off ] | No | Controls whether to enable the hash-based aggregation optimization strategy. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| polar px opti _ _ mizer enable _ hashjoin _ | 14 | on | [on\|off ] | No | Controls whether to enable the hash join optimizer. If you set this parameter to on, the optimizer is allowed to use the hash join algorithm. If you set it to off, hash join optimization is disabled. |
|---|---|---|---|---|---|
| polar px opti _ _ mizer enable _ indexonlysc _ an | 14 | on | [on\|off ] | No | Controls whether to enable the Index-Only Scan optimization strategy. If you set this parameter to on, the optimizer considers using index-only scans to improve query performance. If you set it to off, the optimizer disables this strategy. The default value is typically on. |
| polar px opti _ _ mizer enable _ indexscan _ | 14 | on | [on\|off ] | No | Specifies whether to enable the index scan optimizer. This controls whether to consider using index scans during query optimization. |
| polar px opti _ _ mizer enable _ lasj notin _ _ | 14 | on | [on\|off ] | No | Specifies whether to enable optimizer support for Left Anti Semi Join (LASJ) and NOT IN subqueries. |
| polar px opti _ _ mizer enable _ like to rang _ _ _ e rewrite _ | 14 | off | [on\|off ] | No | Controls whether to enable the optimization feature that rewrites LIKE expressions into range queries. If you set this parameter to on, Postgres attempts to convert LIKE to a more efficient range scan operation to improve query performance. |
| polar px opti _ _ mizer enable _ mergejoin _ | 14 | on | [on\|off ] | No | Controls whether to enable the Merge Join feature in the optimizer. If you set this parameter to on, the optimizer is allowed to choose merge join as part of the query execution plan. |
| polar px opti _ _ mizer enable _ motion bro _ _ adcast | 14 | on | [on\|off ] | No | Specifies whether to enable the broadcast data distribution optimization strategy. If you set this parameter to on, the optimizer considers using the broadcast method to transmit data in the query plan. This is suitable for certain distributed query scenarios. |
| polar px opti _ _ mizer enable _ motion gat _ _ her | 14 | on | [on\|off ] | No | Specifies whether to enable the Motion Gather operation in the optimizer to optimize data transmission in distributed queries. |
| polar px opti _ _ mizer enable _ motion redi _ _ stribute | 14 | on | [on\|off ] | No | Enables or disables the optimizer's data redistribution optimization feature. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| polar px opti _ _ mizer enable _ nestloopjoin _ | 14 | on | [on\|off ] | No | Controls the enabling or disabling of the NestLoop Join optimizer in the PolarDB for PostgreSQL kernel. |
|---|---|---|---|---|---|
| polar px opti _ _ mizer enable _ partition sel _ _ ection | 14 | on | [on\|off ] | No | Controls whether to enable the partition selection optimization feature for partitioned tables. |
| polar px opti _ _ mizer enable _ seqscan _ | 14 | on | [on\|off ] | No | Specifies whether to enable the sequential scan optimization strategy. |
| polar px opti _ _ mizer enable _ seqsharesca _ n | 14 | on | [on\|off ] | No | Specifies whether to enable optimizer support for shared sequential scans. |
| polar px opti _ _ mizer enable _ shareindexs _ can | 14 | on | [on\|off ] | No | Specifies whether to enable the shared index scan optimizer feature. |
| polar px opti _ _ mizer enable _ sort _ | 14 | on | [on\|off ] | No | Specifies whether to enable the sorting feature in the optimizer. |
| polar px opti _ _ mizer indexo _ nlyscan fact _ or | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Controls the optimizer's preference for Index- Only Scans when evaluating index scan costs. A higher value makes the optimizer more likely to choose an index scan. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| polar px opti _ _ mizer indexs _ can factor _ | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | An optimizer parameter that controls the cost of index scans. It is used to adjust the priority of index scans in the query plan. A larger value increases the cost of index scans, which may cause the optimizer to prefer other scan methods. |
|---|---|---|---|---|---|
| polar px opti _ _ mizer nestlo _ op factor _ | 14, 11.2 | 102 4.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Controls the cost factor for nested loop joins. This affects the optimizer's preference for nested loop joins. A higher value makes the optimizer more likely to choose other join methods. |
| polar px opti _ _ mizer remov _ e superfluou _ s order _ | 14 | on | [on\|off ] | No | Controls whether the optimizer removes superfluous sort operations to improve query performance. |
| polar px opti _ _ mizer share _ _ indexscan fa _ ctor | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Controls the cost factor in shared index scans for the parallel query optimizer. This affects the optimizer's choice of index scan method. A larger value makes the optimizer less likely to use shared index scans. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| polar px opti _ _ mizer share _ _ tablescan fa _ ctor | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Controls the optimization factor for table scan sharing in parallel queries. This affects the allocation strategy for table scans during parallel execution. A larger value favors shared scans, while a smaller value favors independent scans. |
|---|---|---|---|---|---|
| polar px opti _ _ mizer sort fa _ _ ctor | 14, 11.2 | 1.0 | 14: [0- 999 999 999 999. 0] 11.2 : [0.0 - 214 748 364 7.0] | No | Adjusts the optimization factor for sort operations during execution plan generation in PolarDB for PostgreSQL. |
| polar px repl _ _ ay wait slee _ _ p time _ | 11.2 | 10 | [1- 21474 83647 ] | No | Controls the duration that a process enters hibernation when it needs to wait during physical log (PX) replay. |
| polar px wai _ _ t lock timeo _ _ ut | 14 | 180 000 0 | [0- 21474 83647 ] | No | Sets the timeout for waiting for locks in PolarDB parallel execution (PX). The unit is milliseconds. A lock wait timeout error is triggered after the timeout to avoid prolonged blocking. |
| postgres fdw _ .polar conne _ ction check _ | 11.2 | off | [on\|off ] | No | Specifies whether to enable RDS connection checking. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| shared prelo _ ad libraries _ | 14 | 'pola r vfs _ ,pola r wo _ rker, pg s _ tat s _ tate men ts,au th d _ e lay,a uto _ expl ain,z hpar ser, plugi n de _ bug ger, pola r m _ o nitor prel _ oad, pg p _ ath man ' | ^'(pol ar vfs, _ polar _ worker ) (,\w+) *'$ | Yes | Specifies a list of shared libraries to preload when the PostgreSQL instance starts. These libraries typically contain extensions or plugins. Separate multiple library names with commas. After you set this parameter, the related features take effect for the entire database cluster. Note Changing this parameter requires a restart of the PostgreSQL service. |
|---|---|---|---|---|---|
| ssl min prot _ _ ocol version _ | 14 | TLSv 1.2 | [TLSv1 \|TLSv1 .1\|TLS v1.2\|T LSv1.3 ] | No | Specifies the minimum version of the TLS protocol that PostgreSQL allows when establishing an SSL-VPN connection with a client. |
| statement ti _ meout | 14, 11.2 | 0 | ^(0\| [1- 9]\d{3 ,8}\|1\ d{9}\| 20000 00000 )... | No | Sets the maximum time that a single database query is allowed to run. The query is forcibly terminated if it exceeds this time. The unit is milliseconds. The default value is 0, which means no limit. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| synchronous commit _ | 14 | off | [local\|r emote write\| _ remot e appl _ y\|on... | No | Controls whether a transaction commit waits for the Write-Ahead Logging (WAL) records to be synchronized to the disk or a synchronous standby server. This ensures data durability and consistency. The valid values include the following: on: Ensures that each commit waits for the WAL records to be written to storage. off: Does not wait for WAL records to be written. This may cause the loss of some committed transactions. local: Waits only for the local WAL write to complete. remote write: Waits for at least one _ synchronous standby server to receive the WAL records. remote apply: Waits for at least one _ synchronous standby server to apply the WAL records. |
|---|---|---|---|---|---|
| temp file lim _ _ it | 14, 11.2 | 1 4: 1 0 0 G B 1 1. 2: 5 2 4 2 8 8 0 0 0 | 14: [-1- 214 748 364 7] 11.2 : [- 1- 104 857 600 0] | No | Controls the maximum size of temporary files that a single query can create. If you specify a value without a unit, the unit is kilobytes. If the limit is exceeded, the query is canceled. A value of -1 indicates no limit. This parameter is used to prevent temporary files from exhausting disk space. |
|  |  |  | ^'(((U TC)(-) {0,1} (\d\|[1- 9]\d\|1( [0- 5]\d\|6[ 0- 7])))\| ((GMT) (-) {0,1} (\d\|[1- 9]\d\|1( [0- 5]\d\|6[ 0- 7])))\|C ST6CD |  |  |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

|  |  |  | T\|Pola nd\|Kw ajalein \|MST\| NZ\|Uni |  |  |
|---|---|---|---|---|---|
| timezone | 14, 11.2 | 1 4: U T C 1 1. 2: P R C | versal\| Libya\| Turkey \|EST5 EDT\|G reenwi ch\|NZ- CHAT\| MET\|P ortuga l\|GMT- 0\|CET\| Eire\|P ST8PD T\|Jama ica\|GM T\|Zulu \|Japan\| ROC\|G B- Eire\|R OK\|Na vajo\|Si ngapo re\|posi xrules\| GB\|ES T\|GMT 0\|Hon gkong\| PRC\|Ir an\|MS T7MD T\|WET \|W- SU\|UC T\|Cub a\|Egyp t\|EET\|I srael\| UTC\|H ST\|Icel and)'$ | No | Sets the time zone for the database, which affects the display and storage of timestamps. The default value is typically the system time zone. |
| track commi _ t timestamp _ | 14, 11.2 | off | [on\|off ] | Yes | Specifies whether to record the commit timestamp of transactions. If you enable this parameter, you can query the commit time of transactions, but this increases storage overhead. The default value is off. |
| vacuum defe _ r cleanup ag _ _ e | 14, 11.2 | 0 | [0- 10000 00] | No | Specifies the number of transactions by which the cleanup of dead tuples is deferred in a VACUUM operation. This is used to reduce cleanup conflicts caused by concurrent transactions. The value can be 0 or a positive integer. The default value is 0, which means immediate cleanup. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| wal level _ | 14, 11.2 | logic al | [mini mal\|re plica\|l ogical] | Yes | Controls the level of information written to the Write-Ahead Logging (WAL) log. This determines the availability of replication and recovery features. Common values include minimal (least information), replica (supports replication), and logical (supports logical decoding). |
|---|---|---|---|---|---|
| work mem _ | 11.2 | 409 6 | [4096- 52428 8] | No | Sets the maximum amount of memory that a query operation, such as a sort or hash table, can use before it writes to temporary disk files. If you specify a value without a unit, the unit is kilobytes. |
| zdb.curl verb _ ose | 11.2 | off | [on\|off ] | No | Enables the verbose mode of libcurl. |
| zdb.default e _ lasticsearch _ url | 11.2 | '' | None | No | The default Elasticsearch URL that ZomboDB should use if one is not specified on the index. |
| zdb.default r _ eplicas | 11.2 | 0 | [0- 32768 ] | No | The default number of replicas for an index. |
| zdb.default r _ ow estimate _ | 11.2 | 250 0 | [-1- 21474 83647 ] | No | The default row estimate that ZDB should use. |
| zdb.ignore vi _ sibility | 11.2 | off | [on\|off ] | No | Specifies whether queries should adhere to visibility rules. |
| zdb.log level _ | 11.2 | deb ug1 | [debu g5\|de bug4\| debug 3\|deb ug2\|d ebug1 \|info\|n otice\| warnin g\|log] | No | The ZomboDB log level. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

### Manage tags

If you have a large number of instances, you can create multiple tags and add the tags to the instances. Then, you can query instances by tag. This topic describes how to manage tags.

**Usage notes**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS A tag consists of a key-value pair. Each key must be unique for an Alibaba Cloud account in a region. This limit does not apply to the values of keys. You can add up to 20 tags to an instance. If a tag is removed from an instance and is not added to other instances, the tag is automatically deleted.

**Add tags**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, enter the tag key and tag value and click **OK**.

**Filter clusters by tag**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click **Advanced Filter**.
3. You can search for your instance by **Instance ID /Name**, **VIP**, and **Tag Filtering**. Select a
tag from the **Filter by Tag** drop-down list.
4. After you select a tag, the instance list displays all instances that are bound with the tag.

**View tags added to a cluster**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, if a small number of tags are added to an instance, the
corresponding tags are displayed in the Tag column. If a large number of tags are added to an instance, move the pointer over the icon in the **Tag** column to view all the tags that are added to the instance.

**Remove a tag**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the required instance and click the
icon in the **Tag** column.
3. In the **Edit Tags** dialog box, click the
icon to the right of the tag and click **OK**.

| Parameter | Description |
|---|---|
| Host name/address | The internal endpoint of the ApsaraDB RDS instance. For more information about how to view the internal endpoint, see View and modify the internal endpoint and port number. |
| Port | The internal port number that is used to connect to the ApsaraDB RDS instance. For more information about how to view the internal port number, see View and modify the internal endpoint and port number. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Database connection

### Connect to an instance

This topic describes how to use Data Management (DMS) or the pgAdmin 4 client to connect to an ApsaraDB RDS instance.

**Background information**

You can log on to DMS from the ApsaraDB RDS console and then connect to an ApsaraDB RDS instance. Data Management (DMS) is a data management service that integrates data, schema, and server management, access security, BI charts, data trends, data tracking, and performance optimization. DMS can be used to manage relational and non-relational databases, such as MySQL, SQL Server, and PostgreSQL. It can also be used to manage Linux servers. You can also use a database client to connect to an ApsaraDB RDS instance. ApsaraDB RDS is fully compatible with PolarDB. You can connect to PolarDB instances in the similar manner as you would connect to an open source PolarDB database. In this topic, the pgAdmin 4 client is used to connect to an ApsaraDB RDS instance.

**Use DMS to connect to an ApsaraDB RDS instance**

For more information about how to use DMS to connect to an ApsaraDB RDS instance, see Use DMS to log on to a PolarDB instance.

**Use the pgAdmin 4 client to connect to an ApsaraDB RDS**

1. Add the IP address of the pgAdmin client to an IP address whitelist of the ApsaraDB RDS
instance. For more information about how to configure a whitelist, see Configure an IP address whitelist.
2. Start the pgAdmin 4 client.

**Note**

For information about how to download the pgAdmin 4 client, visit pgAdmin 4 (Windows).
3. Right-click **Servers** and choose **Create > Server**, as shown in the following figure.
4. On the **General** tab of the **Create - Server** dialog box, enter the name of the server, as
shown in the following figure.
5. Click the **Connection** tab and enter the information of the instance, as shown in the
following figure.

| Username | The name of the privileged account for the ApsaraDB RDS instance. For more information about how to create an privileged account, see Create a database and an account. |
|---|---|
| Password | The password of the privileged account. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
6. Click **Save**.
7. If the connection information is correct, choose **Servers > Server Name > Databases >**
**postgres**. If the following page appears, the connection is established.

**Important**

The postgres database is the default system database of the ApsaraDB RDS instance. Do not perform operations on this database.

### Use DMS to log on to a

**PolarDB instance**

This topic describes how to use Data Management (DMS) to log on to a PolarDB instance.

**Prerequisites**

The IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist.
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

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
6. Click **Login**.

**Note**

If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

### Change the network type of

**an instance**

This topic describes how to switch a PolarDB instance between the classic network type and the virtual private cloud (VPC) network type.

**Background information**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS Classic network: PolarDB instances in the classic network are not isolated. To block unauthorized access to these instances, you must configure IP address whitelists or security groups. VPC: Each VPC is an isolated virtual network. We recommend that you select the VPC type because it is more secure than the classic network. You can configure route tables, CIDR blocks, and gateways in a VPC. You can also connect your data center to a VPC by using Express Connect circuits or virtual private networks (VPNs). The data center and the VPC comprise a virtual data center. You can use the virtual data center to migrate your workloads to the cloud with no downtime.

**Change the network type from VPC to classic network**

Precautions After you change the network type from VPC to classic network, the internal endpoint of your PolarDB instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, Elastic Compute Service (ECS) instances located in the same VPC as your PolarDB instance can no longer connect to your PolarDB instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. When you change the network type, a network interruption of 30 seconds may occur. To avoid business interruption, change the network type during off-peak hours or make sure that your application is configured to automatically reconnect to the instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to Classic**
**Network**.
6. In the message that appears, click **OK**.

**Note**

After the network type is changed to classic network, only ECS instances within the classic network can connect to the PolarDB instance by using the internal endpoint. You must configure the internal endpoint for the ECS instances.
7. Configure a whitelist to allow ECS instances within the classic network to connect to the
PolarDB instance by using the internal endpoint.

**Change the network type from classic network to VPC**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. In the upper-right corner of the Database Connection section, click **Switch to VPC**.
6. In the Switch to VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**Note**

Select a VPC. We recommend that you select the VPC where your ECS instances are deployed. Otherwise, the ECS instances cannot communicate with the PolarDB instance over the internal network. Select a vSwitch. If no vSwitches are available in the selected VPC, create one in the same zone where the PolarDB instance is deployed. For more information, see Create a vSwitch in Quick Start of **VPC User Guide**. **> > >** Clear or select **Reserve original classic endpoint**.

**Clear the option**

The classic network endpoint is not retained and changes to a VPC endpoint. When you change the network type from classic network to VPC, a transient connection that lasts approximately 30 seconds occurs and ECS instances that reside in the classic network are immediately disconnected from the PolarDB instance.

**Select the option**

The classic network endpoint is retained, and a new VPC endpoint is generated. In this case, the PolarDB instance runs in hybrid access mode. Classic network-housed ECS instances and VPC-housed ECS instances can connect to the PolarDB instance over an internal network. For more information, see Configure the hybrid access solution for an instance. When you change the network type from classic network to VPC, no transient connection occurs. The connection between each classic network-housed ECS instance and the PolarDB instance remains available until the classic network endpoint expires. To migrate your business to the VPC without interruption, you must add the VPC endpoint to access the ECS instances before the classic network endpoint expires. Seven days before the classic network endpoint expires, the system sends a text message to the phone number bound to your Apsara Stack account every day. For more information, see Configure the hybrid access solution for an instance.
7. Add the private IP address of the required VPC-hosted ECS instance to an IP address
whitelist of the VPC network type on the PolarDB instance. This way, the ECS instance can access the PolarDB instance over an internal network. If no IP address whitelists of the VPC network type are available, create one.

**Note**

If you retain the classic network endpoint, add the VPC endpoint to the ECS instances before the classic network endpoint expires. If you do not retain the classic network endpoint, connections between ECS instances in the classic network and the PolarDB instance over the internal network are interrupted. You must add the new endpoint to ECS instances in the VPC immediately after the network type is changed. ApsaraDB RDS for PolarDB User ApsaraDB for RDS

### Configure the hybrid access

**solution for an instance**

This topic describes how to configure the hybrid access solution for a PolarDB instance. This solution allows you to migrate your PolarDB instance from the classic network to a virtual private cloud (VPC) without network interruptions.

**Prerequisites**

The PolarDB instance resides in the classic network. Available VPCs and vSwitches exist in the zone in which the PolarDB instance resides.

**Background information**

When you migrate your PolarDB instance from the classic network to a VPC, the internal classic network endpoint of the instance changes to the internal VPC endpoint. In this case, the endpoint remains unchanged, but the IP address that is bound to the endpoint changes. This change causes a transient connection that lasts 30 seconds or less, and Elastic Compute Service (ECS) instances located in the classic network can no longer connect to your PolarDB instance over an internal network. To facilitate a smooth migration, PolarDB provides the hybrid access solution. Hybrid access indicates that your PolarDB instance can be connected by both ECS instances in the classic network and ECS instances in VPCs. If you use the hybrid access solution, PolarDB retains the internal classic network endpoint and generates an internal VPC endpoint. This prevents transient connections when you migrate your PolarDB instance from the classic network to a VPC. For security and performance purposes, we recommend that you use only the internal VPC endpoint. You must specify a validity period for the hybrid access solution. When the hybrid access solution expires, PolarDB releases the internal classic network endpoint and applications are unable to use the endpoint to connect to your PolarDB instance. You must add the internal VPC endpoint to your applications before the hybrid access solution expires. This ensures a smooth migration and prevents interruptions to your workloads. For example, assume that a company uses the hybrid access solution to migrate its PolarDB instance from the classic network to a VPC. During the validity period of the hybrid access solution, some applications use the internal VPC endpoint to connect to the PolarDB instance, whereas the others continue to use the internal classic network endpoint to connect to the instance. When all applications of the company can use the internal VPC endpoint to connect to the instance, the internal classic network endpoint can be released. The following figure demonstrates the scenario. ApsaraDB for RDS ApsaraDB RDS for PolarDB User During the validity period of the hybrid access solution, your PolarDB instance has the following limits: The network type of the PolarDB instance cannot be changed to classic network. The PolarDB instance cannot be migrated to another zone.

**Change the network type from classic network to VPC**

For more information, see Change the network type from classic network to VPC.

**Change the expiration date of the internal classic network**

During the validity period of the hybrid access solution, you can change the expiration date of the classic network endpoint based on your business requirements. The expiration date is immediately recalculated starting from the day when you make the change. For example, the classic network endpoint is configured to expire on August 18, 2017. On August 15, 2017, you extend the validity period of the classic network endpoint by 14 days. In this case, PolarDB releases the classic network endpoint on August 29, 2017. To change the expiration date, perform the following operations:
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the **Instance Connection** tab, click **Change Expiration Time**.
6. In the **Change Expiration Time** dialog box, select an expiration date and click **OK**.

### View and modify the internal

**endpoint and port number**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS You must use the internal endpoint and port number to access a PolarDB instance. This topic describes how to view and change the internal endpoints and port numbers of a PolarDB instance in the console.

**View the internal endpoint and port number**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the **Basic Information** section, view the internal and public endpoints and port
numbers.

**Note**

The endpoints and port numbers are displayed only after you configure an IP address whitelist or security group for the PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Database Connection**.
5. On the right side of the page, click **Change Endpoint**.
6. In the dialog box that appears, set **Connection Type** to **Internal Endpoint**.
7. Modify the endpoint prefix and port number and then click **OK**.

**Note**

The prefix of an endpoint must be 8 to 64 characters in length and can contain only letters, digits, and hyphens (-). It must start with a lowercase letter. The port number must be within the range of 1000 to 5999. ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**FAQ**

Q: Do I need to modify the endpoint or port number in my application after I modify the endpoint or port number of an instance? A: Yes, you must modify the endpoint or port number in the application after you have modified them. Otherwise, the application cannot connect to databases of the instance. Q: Does the modification of the endpoint take effect immediately? Do I need to restart the instance? A: No, you do not need to restart the instance. The modification takes effect immediately.

| Account type | Description |
|---|---|
| Privileged account | You can create and manage privileged accounts in the ApsaraDB RDS console or by calling API operations. You can create multiple privileged accounts for each instance. The privileged accounts of an instance have the permissions to manage all standard accounts and databases that are created on the instance. A privileged account allows you to manage more permissions in a fine-grained manner based on your business requirements. For example, you can grant each standard account the permissions to query specific tables. A privileged account has the permissions to disconnect all standard accounts of the instance on which the privileged account is created. |
| Standard account | You can create and manage standard accounts in the ApsaraDB RDS console, by calling API operations, or by using SQL statements. You can create multiple standard accounts for each instance. You must grant the permissions on specific databases to standard accounts. A standard account does not have the permissions to create, manage, or disconnect other accounts of the instance on which the standard account is created. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Accounts

### Create an account

Before you start to use PolarDB, you must create an account for a PolarDB instance. This topic describes how to create an account on a PolarDB instance.

**Account types**

You can create privileged and standard database accounts in PolarDB. The following table describes the account types.

**Usage notes**

You can create multiple privileged accounts and standard accounts in the ApsaraDB RDS console. You can also create and manage standard accounts by using SQL statements. Before you can migrate data from an on-premises database to a PolarDB instance, you must create a database and an account on the PolarDB instance. Make sure that the created database has the same properties as the on-premises database. In addition, make sure that the created account has the same permissions on the created database as the account that is authorized to manage the on-premises database. We recommend that you follow the principle of least privilege (PoLP) and grant the read and write permissions to accounts based on your business requirements. You can create multiple databases accounts and grant each account only the permissions to access the data of specified databases. This way, you can implement fine-grained permission management. If an account does not need to write data to a database, we recommend that you grant only the read permissions on the database to the account. For security purposes, we recommend that you specify strong passwords for the accounts and change the passwords on a regular basis.

| Parameter | Description |
|---|---|
| Database Account | The username of the account must be 2 to 16 characters in length. The username can contain lowercase letters, digits, and underscores ( ). _ The username must start with a letter and end with a letter or a digit. |
| Account Type | PolarDB supports two types of accounts: privileged accounts and standard accounts. A privileged account has all operation permissions on all databases. Standard accounts have all operation permissions only on their authorized databases. Note The permitted operations include SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, and TRIGGER. |
| New Password | The password is 8 to 32 characters in length. The password contains three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ % ^ & * ( ) + - _ = |
| Confirm Password | Enter the password of the account again. |
| Description | Optional. You can enter description to make the account easier to identify. The description can be up to 256 characters in length. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**Create a privileged account or a standard account**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. On the Accounts page, click Create Account and configure the following parameters.
6. Click **OK**.

### Reset the password of an

**account**

This topic describes how to use the ApsaraDB RDS console to reset the password of your account if you forget the password. ApsaraDB RDS for PolarDB User ApsaraDB for RDS
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the **Actions** column corresponding to the account, click **Reset Password**.
6. In the dialog box that appears, enter and confirm the new password, and then click **OK**.

**Note**

The password must meet the following requirements: It can be 8 to 32 characters in length. It can contain at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. It can contain the following special characters: !@#$%^&*()_+-=

### Lock or unlock an account

This topic describes how to lock or unlock an account on a PolarDB cluster.
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. In the left-side navigation pane of the page that appears, click **Accounts**.
6. Click **Lock** in the **Actions** column corresponding to the account.

**Note**

Wait a few minutes. When the **Status** column displays **Locking**, the account is locked. If you want to use the account again, click **Unlock** in the **Actions** column.

### Delete an account

You can delete a database account in the console.

**Prerequisites**

You can use the console to delete privileged and standard accounts that are no longer used.
1. Log on to the ApsaraDB RDS console.
ApsaraDB for RDS ApsaraDB RDS for PolarDB User
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. Find the account that you want to delete and click **Delete** in the Actions column.
6. In the message that appears, click **OK**.

**Note**

Accounts in the **Processing** state cannot be deleted.

| Parameter | Description |
|---|---|
| Database type | The engine of the database. By default, the engine of the database to be connected is displayed. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Databases

### Create a database

Before you start to use PolarDB, you must create a database on a PolarDB instance. This topic describes how to create a database on a PolarDB instance.

**Prerequisites**

A PolarDB instance is created. For more information, see Create an instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. Click **Log On to Database** in the upper-right corner of the page.
5. In the **Login instance** dialog box of the **DMS** console, check values of **Database type**,
**Instance Area**, and **Connection string address**. If the information is correct, enter
**Database account** and **Database password**, as shown in the following figure.

| Instance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
|---|---|
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database account | The account of the database to be connected. |
| Database password | The password of the account used to connect to the database. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

**Note**

If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
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

### Delete a database

This topic describes how to delete a database in the PolarDB instance.
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

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
6. Click **Login**. If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

**Note**

If a message prompts you that the connection fails, the problem may be caused by an improperly configured whitelist. Reconfigure the whitelist in the console. For more information, see Configure an IP address whitelist.
7. The **SQLConsole** page appears after you log on to the instance. Execute the following
statement to delete a database:

```
drop database <database name>;
```

8. Click **execute**.

| Metric | Description |
|---|---|
| Memory usage | The memory usage of the instance. |
| CPU utilization | The CPU utilization of the instance. |
| IOPS | The number of input/output operations per second (IOPS) for the data and log disks of the instance. |
| Local storage | The used local storage space of the instance. |
| Network | The volume of data received and sent by the instance. |
| Network retransmissions | The number of network retransmissions for the instance. |
| Connections | The total, active, waiting, and idle connections for the instance. |
| Rows scanned | The number of rows read, inserted, updated, returned, and deleted per second by the instance. |
| TPS | The number of transactions per second (TPS) processed by the instance. |
| Duration of the longest current transaction | The duration of the longest-running current transaction on the instance. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Monitoring and alerts

### View monitoring data

PolarDB provides a wide range of performance metrics. This topic describes how to view resource monitoring data in the ApsaraDB RDS console.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Monitoring and Alerts**.
5. On the **Monitoring** tab, select the time range to query the corresponding monitoring data.
The following table lists the specific metrics.

| Latency | The latency in primary node sending, secondary node replay, and logical replication for the instance. |
|---|---|
| Slow SQL statements | Information about slow SQL statements on the instance. |
| Long-running transactions | The number of long-running transactions on the instance. |
| Two-phase long-running transactions | The number of two-phase long-running transactions on the instance. |

| Parameter | Description |
|---|---|
| Cloud product selection | Select ApsaraDB RDS or ApsaraDB RDS (New). Note ApsaraDB RDS supports the MySQL, SQL Server, PolarDB for Oracle, and PostgreSQL engines, uses the acs rds dashboard namespace for _ _ monitoring data, and provides collection periods that range from 60 to 300 seconds. ApsaraDB RDS (New) supports only the MySQL, PolarDB for Oracle, and PostgreSQL engines, uses the acs rds dashboard _ _ namespace for monitoring data, and provides a more stable collection period of 60 seconds. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

### Configure an alert rule

This topic describes how to create alert rules in the ApsaraDB RDS console. This allows you to identify and handle exceptions at the earliest opportunity.
1. Log in to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Alerts** tab, click **Alert Rule Settings**.
5. On the **Alert Rule** page, click **Create an alert rule**.
6. In the **Create an alert rule** panel, configure the following parameters and click **OK**.

| Resource scope | The resources to which the alert rule applies. Valid values: Instance dimension: Select one or more instances in the resource set of the current organization. Resource set dimension: Select a resource set in the current organization and region. Apply grouping dimensions: Select an application group in the current organization and region. All resources: The alert rule applies to all resources of the specified cloud service. |
|---|---|
| Resource Selection | The resources to be associated with the alert rule. Select one or more resources based on the selected resource scope. |
| Alarm rule description | The trigger conditions of the alert rule. If the monitoring data meets the specified conditions, the alert rule is triggered. To configure the trigger conditions, perform the following steps: i. Click Rule description. ii. In the Rule description panel, configure the Rule name, Monitoring Metrics, Metric dimension, and Threshold and alarm level parameters. Note The Metric dimension parameter is displayed only if you set the Resource scope parameter to Instance dimension. iii. Click Confirm. |
| Silence channel period | The mute period after which Cloud Monitor resends an alert notification before the alert is cleared. Valid values: 5 minutes, 15 minutes, 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, and 24 hours. An alert is triggered if the conditions of an alert rule are met. Cloud Monitor does not resend an alert notification when the alert is triggered within the mute period. If the alert is not cleared after the mute period ends, Cloud Monitor resends alert notifications. For example, if you set the Silence channel period parameter to 12 hours, Cloud Monitor resends alert notifications only if the alert still persists after 12 hours. |
| Effective time | The period during which the alert rule takes effect Cloud Monitor checks whether the monitoring data triggers the alert rule only during the effective period. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| Alarm callback | The callback URL to which Cloud Monitor sends alert notifications by using the POST request method. Note Cloud Monitor sends HTTP POST requests to push alert notifications to the specified URL. Only HTTP URLs are supported. IP addresses are not supported. |
|---|---|
| No data processing method | Specify how Cloud Monitor acts when no alert is triggered. Valid values: No processing: Cloud Monitor does not perform any operations when no alert is triggered. Send no data alarm: Cloud Monitor sends the corresponding notifications to contacts when no alert is triggered. |
| Alarm contact | The alert contacts or alert contact groups to which Cloud Monitor sends alert notifications. By default, the value of this parameter is a dummy user used to test whether the alert rule is effective. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Data security

### Configure an IP address

**whitelist**

This topic describes how to configure a whitelist for a PolarDB instance. Only entities that are listed in a whitelist can access your PolarDB instance.

**Background information**

Whitelists make your PolarDB instance more secure and do not interrupt the operations of your PolarDB instance when you configure whitelists. We recommend that you perform maintenance on your whitelists on a regular basis. To configure a whitelist, perform the following operations: Configure a whitelist: Add IP addresses to allow them to connect to the PolarDB instance.

**Note**

The default IP address whitelist contains only the IP address 127.0.0.1. This indicates that no devices are allowed to access the PolarDB instance. Configure an ECS security group: Add an ECS security group for the PolarDB instance to allow ECS instances in the group to connect to the PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

**Note**

You can also click **Create Whitelist** to create a whitelist.
6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that are allowed to
access the instance and click **OK**. The following section describes the rules: If you enter the CIDR block 10.10.10.0/24 in the IP Addresses field, all IP addresses in the 10.10.10.X format can access your PolarDB instance. If you enter more than one IP address or CIDR block, you must separate them with commas (,). Do not add spaces before or after the commas. Example: 192.168.0.1,172.16.213.9. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances created within your Apsara Stack account are displayed. You can select the required IP addresses to add them to the IP address whitelist.

### Configure SQL audit

This topic describes how to configure the SQL audit feature to audit SQL executions and check the details. SQL audit does not affect instance performance.

**Precautions**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS The SQL Audit feature does not affect instance performance. SQL audit logs are retained for 30 days. Log files exported from the SQL Audit feature are retained for two days. The system automatically deletes files that are retained for longer than two days. The SQL Audit feature is disabled by default. You must manually enable this feature. You cannot view logs that were generated before the SQL Audit feature was enabled.

**Enable SQL audit**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Data Security**. The **Data Security** page appears.
5. Click the **SQL Audit** tab.
6. Click **Enable SQL Audit** or **Enable now**.
7. In the message that appears, click **Confirm**.

**Note**

After you enable the SQL Audit feature, you can query SQL information based on conditions such as the time, DB, user, and keyword.

**Disable SQL audit**

You can disable SQL audit when it is no longer needed. To disable SQL audit, perform the following steps:

**Important**

When you disable the SQL Audit feature, all SQL audit records, including historical logs, are cleared. Before you disable this feature, you must export and save the audit logs to your local computer.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Data Security**. The **Data Security** page appears.
5. Click the **SQL Audit** tab.
6. Click **Disable SQL Audit**.
7. In the message that appears, click **Confirm**.

**Change the storage location for audit logs**

By default, audit logs are stored in SLS-inner. You can switch the storage location to an accessible SLS-PUB project.
1. Log on to the ApsaraDB RDS console.
ApsaraDB for RDS ApsaraDB RDS for PolarDB User
2. In the navigation pane on the left, click **Instance List**. Click the ID of the target instance or
click **Manage** in the **Actions** column of the instance. The **Basic Information** page appears.
3. In the left-side menu bar, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Enable the storage of audit logs in SLS-PUB.

**Important**

This action cannot be undone. Proceed with caution.

### Configure SSL encryption

This topic describes how to enhance endpoint security. You can enable Secure Sockets Layer (SSL) encryption and install SSL certificates that are issued by certificate authorities (CAs) to the required application services. SSL is used at the transport layer to encrypt network connections and enhance the security and integrity of communication data. However, SSL increases the response time.

**Precautions**

An SSL certificate is valid for one year. You must Update the validity period of an SSL certificate and then download and configure the certificate again. Otherwise, the client that uses encrypted network connections cannot connect to the ApsaraDB RDS instance. SSL encryption may cause a significant increase in CPU utilization. We recommend that you enable SSL encryption only when you need to encrypt connections from the Internet. In most cases, connections that use an internal endpoint do not require SSL encryption. If you disable SSL encryption, the ApsaraDB RDS instance restarts. Proceed with caution.

**Enable SSL encryption and download an SSL certificate**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the page that appears, click the **SSL Encryption** tab. Turn on **SSL Encryption**.
6. In the **Configure SSL** dialog box, select the endpoint for which you want to enable SSL
encryption and click **OK**.
7. After the state of SSL encryption is displayed as **Enabled**, click **Download CA Certificate**.
The downloaded file is a package that contains the following files: P7B file: contains the server CA certificate that can be imported into a Windows operating system. PEM file: used to import CA certificates to other operating systems or applications. JKS file: the Java truststore file. The password is apsaradb. It is used to import the CA certificate chain to Java programs. ApsaraDB RDS for PolarDB User ApsaraDB for RDS

**Note**

When the JKS file is used in Java, you must modify the default JDK security configurations in JDK 7 and JDK 8. Open the `jre/lib/security/java.security` file on the server that connects to your database and modify the following configurations:

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

If you do not modify these configurations, the following error is reported. In most cases, other similar errors are also caused by invalid Java security configurations:

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

**Update the validity period of an SSL certificate**

After you change the endpoint that has SSL encryption enabled or when the SSL certificate is about to expire, you must update the validity period of the SSL certificate. This section describes how to update the validity period of an SSL certificate.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the page that appears, click the **SSL Encryption** tab. Click **Update Validity**.
6. In the **Update SSL Certificate Validity** message, click **OK**.

**Note**

The update of the validity period causes the ApsaraDB RDS instance to restart. Proceed with caution.
7. After the validity period of the certificate is updated, download and configure the certificate
again.

**Note**

For more information about how to download a certificate, see Step 7 in the "Enable SSL encryption and download an SSL certificate" section.

**Disable SSL encryption**

**Note**

If you disable SSL encryption, the ApsaraDB RDS instance restarts. We recommend that you disable SSL encryption during off-peak hours. After you disable SSL encryption, access performance increases, but security decreases. We recommend that you disable SSL encryption only in secure environments.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
ApsaraDB for RDS ApsaraDB RDS for PolarDB User
4. In the left-side navigation pane, click **Data Security**.
5. On the page that appears, click the **SSL Encryption** tab. Turn off **SSL Encryption**.
6. In the **Configure SSL** message, click **OK**.

### Configure TDE

PolarDB provides the Transparent Data Encryption (TDE) feature. TDE encrypts and decrypts data files in real time. It encrypts data files when they are written to disks, and decrypts data files when they are loaded to the memory from disks. TDE does not increase the size of data files. You can use TDE without the need to make changes to applications.

**Background information**

TDE performs data-at-rest encryption at the database layer. This prevents potential attackers from bypassing the database to read sensitive information from storage. TDE can encrypt sensitive data within tablespaces and data stored in disks and backups. TDE also automatically decrypts data to plaintext for applications and users that have passed the database authentication. The operating system and unauthorized users are not allowed to access the encrypted data in plaintext form. The key used for TDE is created and managed by Key Management Service (KMS). PolarDB does not provide the key or certificates that are required for encryption. You can use the keys automatically generated by Apsara Stack, or you can authorize your PolarDB instance to use custom data keys generated from your own key materials.

**Precautions**

You cannot disable TDE after it is enabled. You can enable TDE only when you create an instance. In I/O bound workload scenarios, TDE may affect database performance after it is enabled. If you use an existing custom key for encryption, take note of the following items: If you disable a key, set a key deletion plan, or delete the key materials, the key becomes unavailable. After you revoke the key that is authorized for a PolarDB instance, the instance becomes unavailable after it is restarted. You must use an Apsara Stack tenant account or an account that has the AliyunSTSAssumeRoleAccess permission.
1. Log in to the ApsaraDB RDS console.
2. On the **Instances** page, click **Create Instance** in the upper-right corner.
3. On the **Create Instance** page, set **Enable TDE** to Yes.

**Note**

For more information about how to create an instance, see Create an instance.
4. Click **Submit**.

**View the TDE status**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS
4. In the left-side navigation pane, click **Data Security**.
5. On the page that appears, click the **TDE** tab. View **TDE Status**.

| Database engine | Data backup | Log backup |
|---|---|---|
| PolarDB | Supports full physical backup. | Write-ahead logs (WALs) are compressed and uploaded immediately after they are generated. Each log takes up 16 MB of storage space. On-premises logs are deleted within 24 hours. |

| Paramete r | Description |
|---|---|
| Data Retention Period | The number of days for which you want to retain data backup files. Valid values: 7 to 730. Default value: 7. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Backup and recovery

### Back up a PolarDB instance

This topic describes how to back up a PolarDB instance. You can configure a backup policy that is used to automatically back up your PolarDB instance. If you do not configure a backup policy, the default backup policy is used. You can also manually back up your PolarDB instance.

**Precautions**

Do not perform data definition language (DDL) operations during a backup. If you do so, the backup may fail due to table locks. We recommend that you back up your PolarDB instance during off-peak hours. If your PolarDB instance has a large volume of data, a backup may require a long period of time. Backup files are retained for a specific retention period. We recommend that you download the required backup files to your computer before they are deleted.

**Backup description**

**Configure a backup policy to automatically back up your**

ApsaraDB RDS automatically backs up your instance based on the specified backup policy.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. On the **Backup and Restoration** page, click the **Backup Settings** tab and click **Edit**.
6. In the dialog box that appears, configure the following parameters and click **OK**. The
following table lists the parameters.

| Backup Cycle | The cycle to create backups. You can select one or more days of the week. Note To ensure data security, we recommend that you back up your PolarDB instance at least twice a week. |
|---|---|
| Backup Time | The period of time for which you want to back up data. Unit: hours. |
| Log backup | Specifies whether to enable the log backup feature. Important If you disable this feature, all log backup files are deleted and your instance cannot be restored to previous points in time |
| Log Retention Period | The number of days for which you want to retain log backup files. Valid values: 7 to 730. Default value: 7. The log retention period must be less than or equal to the data retention period. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

**Manually back up your PolarDB instance**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the upper-right corner of the page, click **Back Up Instance**.
5. Select the backup mode and backup policy, and click **OK**.

**Note**

The backup mode is **Full Backup** and the backup policy is **Instance**
**Backup**.
6. In the upper-right corner, click the
icon to view the task progress displayed in the
**Task Progress** list.

**Note**

You cannot download backup files to your computer.

**FAQ**

1. Q: Can I disable data backup for a PolarDB instance?
A: No, you cannot disable the data backup feature of your PolarDB instance. However, you can reduce the backup frequency to at least twice a week. The data retention period must be within the range of 7 to 730 days.
2. Q: Can I disable log backup for a PolarDB instance?
A: Yes, you can disable the log backup feature of your PolarDB instance. You can log on to the ApsaraDB RDS console and navigate to the Backup Settings tab to disable the log backup feature of your instance. RDS lets you download unencrypted data backups and log backups. You can archive these files or use them to restore data to a local database.

### Download backup files

| Download method | Description |
|---|---|
| Download button | Downloads the backup file directly using your browser. |
| Download address | Copies the download address. Use this address to download the backup file with other tools. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Backup and Restoration** to go to the **Backup**
**and Restoration** page.
5. Click the tab for the backup type that you want to download:
For a data backup, click the **Data Backups** tab. For a log backup, click the **Log Backups** tab.
6. Select a time range, find the target data backup or archived log, and then click **Download**
**Instance Backup** or **Download** in the **Actions** column.

**Note**

If you are restoring data, select the data backup file that is closest in time to the desired recovery point. If you use a log backup to restore data to a local database, note the following: The instance ID of the log backup must match the instance ID of the data backup. The start time of the log backup must be after the timestamp of the data backup and before the desired recovery point.
7. In the dialog box that appears, select a download method.

**Note**

To download the file on a Linux system, run the following command:

```
wget -c '<Backup file download URL>' -O <File name>
```

The -c option enables resumable downloads. The -O option saves the downloaded file with the specified name. We recommend that you use the original file name from the URL. If the URL contains multiple parameters, enclose the URL in single quotation marks (') to prevent download failures.

| Category | Configura tion | Description |
|---|---|---|
| Region | Region | The region where the instance resides. |
| Database Restorati on | Restorati on Method | By Time Point: You can restore data to any point in time within the log backup retention period. To view or change the log backup retention period, see Backup data. By Backup Set Note The By Time Point option is available only if log backup is enabled. |
|  | Restorati on Time | Select a point in time to restore the database. This parameter is available when you set Restoration Method to By Time Point. |
|  | Backup Set | Select a backup set for the database. This parameter is available when you set Restoration Method to By Backup Set. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

### Data restoration

Restoring data for PolarDB creates a clone instance. The clone instance is an exact copy of the primary instance, including its data and settings.

**Prerequisites**

The source instance must meet the following requirements: The instance status is Running. No migration tasks are in progress. To restore data to a point in time, log backup must be enabled. To restore data from a backup set, the source instance must have at least one backup set.

**Restore PolarDB data**

1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Backup and Recovery**.
5. On the **Data Backup** tab, find the backup you want to restore. In the **Actions** column, click
**Restore**.
6. In the **Restore** dialog box, click **OK**.
7. Set the following parameters:

| Specificat ion Configura tion | Instance Name | The name of the instance. |
|---|---|---|
|  | Database Type | The type of the database. This is fixed to POLARDB. |
|  | Database Version | The version of the database. This is fixed to the database version of the current instance. |
|  | Series | The series of the instance. |
|  | Storage Class | The storage class of the instance. The available options are displayed in the console. |
|  | Instance Type | The type of the instance. Different memory sizes correspond to different maximum connections and input/output operations per second (IOPS). The available options are displayed in the console. For more information, see Instance types. |
|  | Storage Space | Storage space includes space for data, system files, binary logging (binlog) files, and transaction files. You can select a storage space from 20 GB to 3,000 GB in 5 GB increments. |
| Network Type | Network Type | The instance supports the following network types: Classic Network: Alibaba Cloud services in a classic network are not isolated from each other. You can only use security groups or whitelists of the services to block unauthorized access. Virtual Private Cloud (VPC): A VPC helps you build an isolated network environment on Alibaba Cloud. You can customize the route tables, IP address ranges, and gateways in the VPC. Select VPC for better security. Note If you select Virtual Private Cloud, select a VPC and a VSwitch. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
8. Click **Submit** and wait for the restoration to complete.

| Query Items | Description |
|---|---|
| Error Logs | Records the database running errors that occurred over the last 30 days. |
| Slow Query Logs | Records SQL statements within the last 30 days that took longer than 1 second to execute. Duplicated SQL statements are removed. |
| Primary/Secondary Switching Logs | Records logs for primary and secondary instance switches. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Manage logs

The primary/secondary switching logs of a PolarDB instance can be used for troubleshooting. This topic describes how to manage logs of a PolarDB instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **Logs**.
5. On the **Log Management** page, click the **Error Logs**, **Slow Query Logs**, or
**Primary/Secondary Switching Logs** tab, select a time range, and then click **Query**.
ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## CloudDBA

### Introduction to CloudDBA

CloudDBA is a cloud service for database self-detection, self-repair, self-optimization, selfmaintenance, and self-security based on machine learning and expertise. CloudDBA helps you ensure stable, secure, and efficient databases without worrying about the management complexity and service failures caused by manual operations.

**Features**

In PolarDB, CloudDBA provides the following features: View statistics for sessions, and analyze and optimize SQL statements. View real-time performance information for an instance. View storage overviews, trends, anomalies, tablespaces, and data spaces. Slow SQL statements View slow log trends and statistics.

### Session Manager

CloudDBA provides the Session Manager feature for RDS instances. You can use this feature to view and manage sessions of a target instance.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **CloudDBA > Quick Diagnostics**.
5. Click the **Session Manager** tab.

**Note**

For more information, see the "Instance Session" chapter in the **Database Autonomy**
**Service (DAS) > User Guide**.

### Real-time performance

CloudDBA provides a real-time performance feature for ApsaraDB RDS. This feature lets you view the performance of an instance in real time.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **CloudDBA > Quick Diagnostics**.
5. Click the **Real-time Performance** tab.

**Note**

For more information, see the "Real-time performance" topic in the **Database**
**Autonomy Service (DAS) > User Guide**.

### Storage analysis

CloudDBA provides the storage analysis feature for ApsaraDB RDS. This feature helps you promptly detect storage anomalies in your database to maintain its stability.

**Background information**

The storage analysis feature shows the storage overview and available days of storage for a database instance. It also shows the storage usage, storage fragmentation, and anomaly diagnosis for specific tables.
1. Log in to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click the instance ID or click **Management** in the Operation column to go to the **Basic**
**Information** page.
4. In the navigation pane on the left, click **CloudDBA > Quick Diagnostics**.
5. Click the **Storage Analysis** tab.

**Note**

For more information, see the Storage Analysis chapter in the **Database Autonomy**
**Service (DAS) > User Guide**.

### Slow query logs

In PolarDB, CloudDBA provides the slow query logs feature. This feature allows you to view the trends and execution details of slow queries and obtain optimization suggestions for your PolarDB instance.
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, choose **CloudDBA > Slow Query Logs**.

**Note**

For more information, see Slow query logs in **Database Autonomy**
**Service User Guide**.

| Plugin name | PostgreSQ L 14 | PostgreSQ L 11 | Description |
|---|---|---|---|
| address standard _ izer | 3.3.7 | 3.3.4 | Provides address standardization. |
| address standard _ izer data us _ _ | 3.3.7 | 3.3.4 | Provides address standardization data for the United States. |
| AGE | 1.5.0 | - | A graph database extension that lets you query graphs using the Cypher language. |
| bloom | 1 | 1 | Provides an index access method based on Bloom filters. |
| btree gin _ | 1.3.1 | 1.3 | Provides sample GIN operator classes that implement B-tree-equivalent behavior for multiple data types and all enum types. |
| btree gist _ | 1.6.1 | 1.5 | Provides sample GiST operator classes that implement B-tree-equivalent behavior for multiple data types and all enum types. |
| citext | 1.6 | 1.5 | Provides a case-insensitive string type. |
| cube | 1.5 | 1.4 | Provides a data type to represent multidimensional cubes. |
| dblink | 1.2 | 1.2 | Manages tables across databases. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Extensions

This topic describes the extensions and extension versions supported by PolarDB.

**Note**

This topic lists the extensions and their versions that are supported by different PolarDB kernel versions. This information helps you quickly determine which extensions are supported by your instance. For more information about supported extensions, you can run the following command in your database.

```
SELECT * FROM pg_available_extensions;
```

| decoderbufs | 0.1.0 | 0.1.0 | Outputs data compatible with the Debezium platform based on the Protocol Buffers protocol. |
|---|---|---|---|
| dict int _ | 1 | 1 | An example of an add-on dictionary template for full-text search. |
| earthdistance | 1.1 | 1.1 | Provides two different methods to calculate great-circle distances on the surface of the Earth. |
| encdb | 1.1.14 | 1.1.13 | Provides features for confidential databases. |
| encdb btree _ | 1.0.0 | 1.0.0 | Accelerates ciphertext queries on confidential databases. |
| fuzzystrmatch | 1.1 | 1.1 | Determines the similarity and distance between strings. |
| ganos address st _ _ andardizer | 7.4 | 6.8 | A toponym standardization extension based on the PAGC standard. |
| ganos address st _ _ andardizer data _ _ us | 7.4 | 6.8 | A toponym standardization data extension for the United States based on the PAGC standard. |
| ganos geometry _ | 7.4 | 6.8 | Provides computation and analysis features for spatial geometry types. |
| ganos geometry _ _ pyramid | 7.4 | 6.8 | Used for fast display of 2D spatial geometry big data. |
| ganos geometry _ _ sfcgal | 7.4 | 6.8 | Provides extended features for the spatial geometry sfcgal extension. |
| ganos geometry _ _ topology | 7.4 | 6.8 | Provides computation and analysis features for spatial geometry types. |
| ganos networkin _ g | 7.4 | 6.8 | Provides computation and analysis features for spatial geometry network types. |
| ganos pointcloud _ | 7.4 | 6.8 | Provides storage, computation, and analysis features for point clouds. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| ganos pointcloud _ geometry _ | 7.4 | 6.8 | Provides storage, computation, and analysis features for point clouds. |
|---|---|---|---|
| ganos raster _ | 7.4 | 6.8 | Provides storage, computation, and analysis features for spatial raster data. |
| ganos spatialref _ | 7.4 | 6.8 | Provides computation and analysis features for spatial references. |
| ganos tiger geoc _ _ oder | 7.4 | 6.8 | Provides support for the USCB Tiger data type. |
| ganos trajectory _ | 7.4 | 6.8 | Provides computation and analysis features for Ganos moving object data (MOD). |
| hll | 2.17 | 2.17 | Quickly estimates business metrics, such as page views (PV) and unique visitors (UV). |
| hstore | 1.8 | 1.5 | Stores key-value pairs within a single PostgreSQL value. |
| hypopg | 1.4.0 | 1.3.1 | Creates hypothetical indexes. |
| imgsmlr | 1 | - | Supports similar image search. |
| intagg | 1.1 | 1.1 | Provides an integer aggregator and an enumerator. |
| intarray | 1.5 | 1.2 | Provides useful functions and operators to manipulate integer arrays that do not contain null values. |
| ip4r | 2.4 | 2.4 | Enables support for IP address range types in PostgreSQL. |
| isn | 1.2 | 1.2 | Validates input against a hard-coded prefix list and is also used to join numbers on output. |
| ltree | 1.2 | 1.1 | Represents labels for data stored in a hierarchical tree-like structure. |
| mysql fdw _ | 1.2 | 1.1 | Reads data from and writes data to MySQL databases. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| oss fdw _ | 1.1 | 1.1 | Reads data from and writes data to OSS. |
|---|---|---|---|
| pase | 0.0.1 | 0.0.1 | Performs efficient vector retrieval. |
| pg bigm _ | 1.2 | 1.2 | Creates a 2-gram GIN index to accelerate the full- text search process. |
| pg buffercache _ | 1.5 | 1.3 | Provides a method to inspect the shared buffer in real time. |
| polar concurrenc _ y control _ | - | 1 | Performs concurrency control for SQL statements. |
| polar tde utils _ _ | 1 | 1 | An extension for batch encryption and decryption using transparent data encryption (TDE). |
| pg cron _ | 1.5 | 1.2 | Sets scheduled tasks. |
| pg freespacemap _ | 1.2 | 1.2 | Examines the free space map (FSM). |
| pg jieba _ | 1.1.0 | 1.1.0 | Performs tokenization for Chinese full-text search. |
| pg pathman _ | 1.5 | 1.5 | A high-performance extension for partitioned tables. |
| pg hint plan _ _ | 1.4.1 | 1.3.7 | Changes the default execution plan of PostgreSQL using hints in special comments. |
| pg profile _ | 4.1 | - | Collects statistics on resource-intensive activities. |
| pg repack _ (storage cleanup) | 1.5.1-1 | 1.5.0-1 | Cleans up tablespaces online. |
| pg prewarm _ | 1.2 | 1.2 | Provides a convenient way to load data into the operating system buffer or the PostgreSQL buffer. |
| pg sphere _ | 1 | 1 | Provides spherical data types, functions, operators, and indexes for PostgreSQL. |
| pg stat kcache _ _ | 2.2.1 | 2.2.1 | Collects statistics on system read and write operations. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| pg stat statemen _ _ ts | 1.9.2 | 1.6 | Provides a method to track execution statistics for all SQL statements that are executed by a server. |
|---|---|---|---|
| pg trgm _ | 1.6 | 1.4 | Provides functions and operators to determine the similarity of alphanumeric text, and index operator classes to support fast searches for similar strings. |
| pgaudit | 1.6.2 | 1.3.3 | Provides detailed session and object audit logging. |
| pgcrypto | 1.3 | 1.3 | Provides cryptographic functions for PostgreSQL. |
| pgrouting | 3.4.2 | 3.4.2 | Provides computation and analysis features for spatial geometry networks. |
| pgrowlocks | 1.2 | 1.2 | Provides a function to display row lock information for a specified table. |
| pgstattuple | 1.5 | 1.5 | Provides various functions to obtain tuple-level statistics. |
| pgvector | 0.8.0 | 0.5.0 | An extension for high-dimensional vector similarity search. |
| pldebugger | 1.1 | 1.1 | A debugger extension for stored procedures. |
| plperl | 1 | 1 | Provides the Perl procedural language. |
| plpgsql | 1 | 1 | Provides the SQL procedural language. |
| pltcl | 1 | 1 | Provides the Tcl procedural language. |
| plv8 | - | 2.3.15 | A trusted JavaScript language extension. |
| postgis | 3.3.7 | 3.3.4 | A PostGIS extension for spatial geographic information. |
| postgis sfcgal _ | 3.3.7 | 3.3.4 | A PostGIS SFCGAL extension for spatial geographic information. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

| postgis tiger geo _ _ coder | 3.3.7 | 3.3.4 | A PostGIS extension for spatial geographic information related to TIGER data. |
|---|---|---|---|
| postgis topology _ | 3.3.7 | 3.3.4 | A PostGIS extension for spatial geographic information related to topology data. |
| q3c | - | 2.0.0 | Used for spatial indexing on a sphere. |
| rdkit | - | 3.8 | Supports features such as cheminformatics and chemical molecule retrieval. |
| roaringbitmap | 0.5 | 0.5 | Uses bitmap functionality to improve query performance. |
| rum | 1.3 | - | Provides high-speed full-text retrieval. |
| sequential uuid _ | 1.0.2 | 1.0.2 | A UUID generator with a sequential pattern. |
| smlar | 1 | 1 | Calculates the similarity between two arrays of the same type. |
| sslinfo | 1.2 | 1.2 | Provides information about the SSL Certificate provided by the current client. |
| tablefunc | 1 | 1 | Multiple table-returning functions are supported. |
| tds fdw _ | 2.0.2 | 2.0.2 | Queries data from other types of databases. |
| timescaledb | 2.16.1 | 1.7.1 | Supports automatic sharding, efficient writes, retrieval, and near real-time aggregation for time series data. |
| tsm system rows _ _ | 1 | 1 | Provides the SYSTEM ROWS table sampling _ method. |
| tsm system time _ _ | 1 | 1 | Provides the SYSTEM TIME table sampling _ method. |
| unaccent | 1.1 | 1.1 | A text search dictionary that removes accents (diacritical marks) from lexemes. |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

| uuid-ossp | 1.1 | 1.1 | Provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms. |
|---|---|---|---|
| varbitx | 1.1 | 1.1 | Supports various BIT operations. |
| wal2json | 2.6 | 2.5 | Outputs logical log files in JSON format. |
| xml2 | 1.1 | 1.1 | Provides XPath query and XSLT features. |
| zhparser | 1 | 1 | Provides full-text search for Chinese. |
| zombodb | - | 4 | Provides powerful text indexing and analysis features. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## PolarDB driver

### Download the driver

This topic provides links for downloading the drivers that allow your applications to connect to PolarDB instances. You can download and install a driver in this topic. The driver allows your application to access a PolarDB instance.

**Drivers**

JDBC: PolarDB-O-JDBC.zip For more information about how to use the PolarDB Java Database Connectivity (JDBC) driver to connect to a PolarDB instance, see RDS PolarDB JDBC. .NET: polardb_oracle_.net.zip For more information about how to use the PolarDB .NET driver to connect to a PolarDB instance, see RDS PolarDB .NET. OCI: polardb_oracle_oci.tar For more information about how to use the Oracle Call Interface (OCI) driver to connect to a PolarDB instance, see RDS PolarDB OCI. ODBC: polardb_oracle_odbc_for_x86_64.tar.gz polardb_oracle_odbc_for_arm_64.tar.gz polardb_oracle_odbc_for_win_64.7z polardb_oracle_odbc_for_win_32.7z For more information about how to use the Open Database Connectivity (ODBC) driver to connect to a PolarDB instance, see RDS PolarDB OCI. PolarTools: Download the package for PolarTools. Decompress the package and install PolarTools.

### RDS PolarDB JDBC

This topic describes how to use the PolarDB Java Database Connectivity (JDBC) driver to connect Java applications to PolarDB clusters.

**Prerequisites**

An account is created for a PolarDB cluster. For more information, see Create a database and an account.

**Usage notes**

| polardb-jdbc16.jar | JAR file. For Java 7, d |
|---|---|
|  | polardb-jdbc18.jar |
| Java 8, download the |  |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User JDBC is a Java API that is used to connect Java applications to databases. PolarDB JDBC is developed based on open source PostgreSQL JDBC. PolarDB JDBC uses PostgreSQL protocols for LAN communications. PolarDB JDBC allows Java applications to connect to databases by using standard and database-independent Java code. The JDBC driver uses version 3.0 of the PostgreSQL protocol. JDBC V4.0 is compatible with Java 6. JDBC V4.1 is compatible with Java 7. JDBC V4.2 is compatible with Java 8.

**Download the package of the JDBC driver**

Download the JDBC driver Alibaba Cloud provides three versions of the JDBC driver. Select the version based on the Java

**Configure the JDBC driver**

Before you use the JDBC driver in your Java application, add the path of the JDBC driver to `CLASSPATH` . For example, if the path of the JDBC driver is /usr/local/polardb/share/java/, run the following command to add the JDBC driver path to the `CLASSPATH` :

```
export CLASSPATH=$CLASSPATH:/usr/local/polardb/share/java/<Name of the JAR file.jar>
```

Examples:

```
export CLASSPATH=$CLASSPATH:/usr/local/polardb/share/java/polardb-jdbc18.jar
```

Run the following command to view the current JDBC version:

```
#java -jar <Name of the JAR file.jar>
```

Examples:

```
java -jar polardb-jdbc18.jar
```

Sample output:

```
POLARDB JDBC Driver 42.2.5.2.0
```

**Set up a Java project by using Maven**

If your Java project is set up by using Maven, run the following command to install the PolarDB JDBC driver package in your repository:

```
 mvn install:install-file -DgroupId=com.aliyun -DartifactId=<Name of the JAR file> -Dve
rsion=1.1.2 -Dpackaging=jar -Dfile=/usr/local/polardb/share/java/<Name of the JAR file. jar>
```

Examples:

```
 mvn install:install-file -DgroupId=com.aliyun -DartifactId=polardb-jdbc18 -Dversion=1.
1.2 -Dpackaging=jar -Dfile=/usr/local/polardb/share/java/polardb-jdbc18.jar
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS Add the following dependency to the pom.xml file of your project:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId><Name of the JAR file></artifactId>
    <version>1.1.2</version>
</dependency>
```

Examples:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>polardb-jdbc18</artifactId>
    <version>1.1.2</version>
</dependency>
```

**Hibernate**

If your project uses Hibernate to connect to a PolarDB database, specify the driver class and dialect for the database in your Hibernate configuration file named `hibernate.cfg.xml` .

**Note**

Only Hibernate 3.6 and later versions support PostgresPlusDialect.

```xml
<property name="connection.driver_class">com.aliyun.polardb.Driver</property> <property name="connection.url">jdbc:polardb://pc-
***.o.polardb.rds.aliyuncs.com:1521/polardb_test</property>
<property name="dialect">org.hibernate.dialect.PostgresPlusDialect</property>
```

**Druid connection pools**

By default, Druid 1.1.24 and later support the PolarDB JDBC driver. You do not need to configure the `driver name` and `dbtype` parameters. For Druid versions earlier than 1.1.24, configure the `driver name` and `dbtype` parameters in an explicit way. The following code provides an example:

```
dataSource.setDriverClassName("com.aliyun.polardb.Driver"); dataSource.setDbType("postgresql");
```

**Note**

Druid versions earlier than 1.1.24 are not adapted to PolarDB. Therefore, you must set `dbtype` to `postgresql` . For more information about how to encrypt database passwords in a Druid connection pool, see Database password encryption.

**Adapt to Activiti**

If your application uses the Activiti framework for business process management (BPM), the following error message may appear when you initialize PolarDB data sources. ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
couldn't deduct database type from database product name 'POLARDB Database Compatible w ith Oracle'
```

The reason is that Activiti provides built-in mappings between database versions and database types. However, in the built-in mappings, the database version is not mapped to PolarDB. To resolve this issue, you can configure the `SpringProcessEngineConfiguration` child class to reload `buildProcessEngine` to the child class. You must specify the database type in an explicit way. The following code provides an example:

```java
package com.aliyun.polardb; import org.activiti.engine.ProcessEngine; import org.activiti.spring.SpringProcessEngineConfiguration; public class PolarDBSpringProcessEngineConfiguration extends SpringProcessEngineConfiguration {
    public PolarDBSpringProcessEngineConfiguration() {
        super();
    }
    @Override
    public ProcessEngine buildProcessEngine() {
        setDatabaseType(DATABASE_TYPE_POSTGRES);
        return super.buildProcessEngine();
    }
}
```

Save the `SpringProcessEngineConfiguration` child class in your project and use the child class in the configuration file to load configurations. Then, initialize the engine. Example:

```xml
<bean id="processEngineConfiguration" class="com.aliyun.polardb.PolarDBSpringProcessEngineConfiguration">
      <property name="dataSource" ref="dataSource"/>
      <property name="transactionManager" ref="transactionManager"/>
      <property name="databaseSchemaUpdate" value="true"/>
      <!-- Other configurations are omitted. -->
</bean>
```

**Load the PolarDB JDBC driver**

You can run the following command to load the PolarDB JDBC driver:

```
Class.forName("com.aliyun.polardb.Driver");
```

**Example**

```java
package com.aliyun.polardb; import java.sql.Connection; import java.sql.Driver; import java.sql.DriverManager; importjavasqlResultSet;
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```java
import java.sql.ResultSet; import java.sql.SQLException; import java.sql.Statement; import java.util.Properties; /**
 * POLARDB JDBC DEMO
 * <p>
 * Please make sure the host ip running this demo is in you cluster's white list.
```

`*/`

```java
public class PolarDBJdbcDemo {
  /**
   * Replace the following information.
```

`*/`

```java
  private final String host = "***.o.polardb.rds.aliyuncs.com";
  private final String user = "***";
  private final String password = "***";
  private final String port = "1921";
  private final String database = "db_name";
  public void run() throws Exception {
    Connection connect = null;
    Statement statement = null;
    ResultSet resultSet = null;
    try {
      Class.forName("com.aliyun.polardb.Driver");
      Properties props = new Properties();
      props.put("user", user);
      props.put("password", password);
      String url = "jdbc:polardb://" + host + ":" + port + "/" + database;
      connect = DriverManager.getConnection(url, props);
      /**
       * create table foo(id int, name varchar(20));
```

`*/`

```java
      String sql = "select id, name from foo";
      statement = connect.createStatement();
      resultSet = statement.executeQuery(sql);
      while (resultSet.next()) {
        System.out.println("id:" + resultSet.getInt(1));
        System.out.println("name:" + resultSet.getString(2));
      }
    } catch (Exception e) {
      e.printStackTrace();
      throw e;
    } finally {
      try {
        if (resultSet != null)
          resultSet.close();
        if (statement != null)
          statement.close();
        if (connect != null)
          connect.close();
```

|  | Paramete r |  | Description |  | Configuration |
|---|---|---|---|---|---|
|  | URL prefix |  | jdbc:polardb:// |  | The prefix of the URL. All the prefixes of the PolarDB instance URLs are jdbc:polardb://. |
|  | Endpoint |  | pc- |  | The endpoint of the PolarDB cluster. For more information about how to view the endpoint, see View or apply for an endpoint in PolarDB User Guide. |
|  |  |  |  | pc- | The endpoin |
|  |  |  | ***.o.polardb.rds.aliyu |  |  |
|  |  |  |  |  | inform |
|  |  |  | ncs.com |  |  |
|  | Port |  | 1521 |  | The port of the PolarDB cluster. Default value: 1521. |
|  | Database |  | polardb test _ |  | The name of the database to which you want to connect. |
|  | The username. |  | test |  | The username that is used to connect to the PolarDB cluster. |
|  | Password |  | Pw123456 |  | The password for the username of the PolarDB cluster. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
      } catch (SQLException e) {
        e.printStackTrace();
        throw e;
      }
    }
  }
  public static void main(String[] args) throws Exception {
    PolarDBJdbcDemo demo = new PolarDBJdbcDemo();
    demo.run();
  }
}
```

In JDBC, a database is typically represented by a URL. The following code provides an example:

```
jdbc:polardb://pc-***.o.polardb.rds.aliyuncs.com:1521/polardb_test? user=test&password=Pw123456
```

Before you run a query on a database, you must create a `Statement` , `PreparedStatment` , or `CallableStatement` object. In the preceding example, a `Statement` object is created. In the following sample code, a `PreparedStatment` object is created: ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```java
PreparedStatement st = conn.prepareStatement("select id, name from foo where id > ?"); st.setInt(1, 10); resultSet = st.executeQuery(); while (resultSet.next()) {
    System.out.println("id:" + resultSet.getInt(1));
    System.out.println("name:" + resultSet.getString(2));
}
```

The following code provides an example on how to use `CallableStatement` to process a stored procedure:

```java
String sql = "{?=call getName (?, ?, ?)}"; CallableStatement stmt = conn.prepareCall(sql); stmt.registerOutParameter(1, java.sql.Types.INTEGER); //Bind IN parameter first, then bind OUT parameter int id = 100; stmt.setInt(2, id); // This would set ID as 102 stmt.registerOutParameter(3, java.sql.Types.VARCHAR); stmt.registerOutParameter(4, java.sql.Types.INTEGER); //Use execute method to run stored procedure. stmt.execute(); //Retrieve name with getXXX method String name = stmt.getString(3); Integer msgId = stmt.getInt(4); Integer result = stmt.getInt(1); System.out.println("Name with ID:" + id + " is " + name + ", and messegeID is " + msgId + ", and return is " + result);
```

To create the stored procedure `getName` that is used in the preceding example, run the following command:

```
CREATE OR REPLACE FUNCTION getName(
    id        In      Integer,
    name      Out     Varchar2,
    result    Out     Integer
  ) Return Integer
```

`Is`

```
  ret     Int;
Begin
  ret := 0;
  name := 'Test';
  result := 1;
  Return(ret);
End;
```

### RDS PolarDB .NET

ApsaraDB for RDS ApsaraDB RDS for PolarDB User This topic describes how to use the ADO.NET Data Provider for PolarDB (PolarDB .NET) driver to connect C# applications to a PolarDB instance.

**Prerequisites**

An account is created for a PolarDB instance. For more information, see Create an account.

**Background information**

PolarDB .NET is a driver that allows you to use applications in programming languages such as C#, Visual Basic, and F# to connect to PolarDB databases. The PolarDB .NET driver is compatible with Entity Framework Core and Entity Framework 6.x. You can use PolarDB .NET in conjunction with Entity Framework to develop applications in an efficient manner. The current driver uses the PostgreSQL 3.0 protocol and is compatible with .NETFramework 4.x and .NET Core 2.x. Entity Framework is an object-relational mapping (ORM) framework that is widely adopted in the .NET platform. Entity Framework and Language-Integrated Query (LINQ) technologies provide a quick method for you to develop backend C# applications. The PolarDB .NET driver provides the .dll files of Entity Framework 5 (EF5) and Entity Framework 6 (EF6), and the .dll files are applicable to PolarDB. This helps you use Entity Framework. For more information about Entity Framework, visit the official website of Entity Framework.

**Install the PolarDB .NET driver**

1. Download the package of the POLARDB .NET driver.
2. Decompress the package of the PolarDB .NET driver.

```
unzip polardb_oracle_.net.zip
```

3. Import the driver to the Visual Studio project.
Add the following content to the <Project> node of sample. csproj or the GUI of Visual Studio.

```xml
<Project>
  ...
  <ItemGroup>
    <Reference Include="POLARDB.POLARDBClient, Version=4.0.4.1, Culture=neutral, Publ
icKeyToken=5d8b90d52f46fda7">
      <HintPath>${your path}\POLARDB.POLARDBClient.dll</HintPath>
    </Reference>
  </ItemGroup>
  ...
</Project>
```

The Samples directory contains the polardb-sample.sql file and multiple sample project files. The following procedure shows how to run these sample projects.
1. Connect to your database. For more information, see Connect to an instance.
2. Run the following command to create a project named `sampledb` .

```
CREATE DATABASE sampledb;
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS
3. Import the databases, tables, data, and functions that are required for testing to database

```
 sampledb .
\i ${your path}/polardb-sample.sql
```

4. After the data is imported, write C # code.
The following sample code shows how to query, update, and call stored procedures.

```
using System; using System.Data; using POLARDB.POLARDBClient;
```

`/*`

```
 * This class provides a simple way to perform DML operation in POLARDB
```

*

```
 * @revision 1.0
```

`*/`

```
namespace POLARDBClientTest {
    class SAMPLE_TEST
    {
        static void Main(string[] args)
        {
            POLARDBConnection conn = new
POLARDBConnection("Server=localhost;Port=5432;User Id=polaruser;Password=password;Database=sampledb");
            try
            {
                conn.Open();
                //Simple select statement using POLARDBCommand object
                POLARDBCommand POLARDBSeletCommand = new POLARDBCommand("SELECT
EMPNO,ENAME,JOB,MGR,HIREDATE FROM EMP",conn);
                POLARDBDataReader SelectResult =  POLARDBSeletCommand.ExecuteReader();
                while (SelectResult.Read())
                {
                    Console.WriteLine("Emp No" + " " + SelectResult.GetInt32(0));
                    Console.WriteLine("Emp Name" + " " + SelectResult.GetString(1));
                    if (SelectResult.IsDBNull(2) == false)
                        Console.WriteLine("Job" + " " + SelectResult.GetString(2));
                    else
                        Console.WriteLine("Job" + " null ");
                    if (SelectResult.IsDBNull(3) == false)
                        Console.WriteLine("Mgr" + " " + SelectResult.GetInt32(3));
                    else
                        Console.WriteLine("Mgr" + "null");
                    if (SelectResult.IsDBNull(4) == false)
                        Console.WriteLine("Hire Date" + " " +
SelectResult.GetDateTime(4));
                    else
                        Console.WriteLine("Hire Date" + " null");
                    Console.WriteLine("---------------------------------");
}
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
                }
                //Insert statement using POLARDBCommand Object
                SelectResult.Close();
                POLARDBCommand POLARDBInsertCommand = new POLARDBCommand("INSERT INTO
EMP(EMPNO,ENAME) VALUES((SELECT COUNT(EMPNO) FROM EMP),'JACKSON')",conn);
                POLARDBInsertCommand.ExecuteScalar();
                Console.WriteLine("Record inserted");
                //Update  using POLARDBCommand Object
                POLARDBCommand  POLARDBUpdateCommand = new POLARDBCommand("UPDATE EMP
SET ENAME ='DOTNET' WHERE EMPNO < 100",conn);
                POLARDBUpdateCommand.ExecuteNonQuery();
                Console.WriteLine("Record has been updated");
                POLARDBCommand POLARDBDeletCommand = new POLARDBCommand("DELETE FROM
EMP WHERE EMPNO < 100",conn);
                POLARDBDeletCommand.CommandType= CommandType.Text;
                POLARDBDeletCommand.ExecuteScalar();
                Console.WriteLine("Record deleted");
                try
                {
                    POLARDBCommand callable_command = new
POLARDBCommand("emp_query(:p_deptno,:p_empno,:p_ename,:p_job,:p_hiredate,:p_sal)", co nn);
                    callable_command.CommandType = CommandType.StoredProcedure;
                    callable_command.Parameters.Add(new
POLARDBParameter("p_deptno",POLARDBTypes.POLARDBDbType.Numeric,10,"p_deptno",ParameterD ection.Input,false ,2,2,System.Data.DataRowVersion.Current,20));
                    callable_command.Parameters.Add(new POLARDBParameter("p_empno", PO
LARDBTypes.POLARDBDbType.Numeric,10,"p_empno",ParameterDirection.InputOutput,false ,2 ,2,System.Data.DataRowVersion.Current,7369));
                    callable_command.Parameters.Add(new POLARDBParameter("p_ename", PO
LARDBTypes.POLARDBDbType.Varchar,10,"p_ename",ParameterDirection.InputOutput,false ,2 ,2,System.Data.DataRowVersion.Current,"SMITH"));
                    callable_command.Parameters.Add(new POLARDBParameter("p_job", POLA
RDBTypes.POLARDBDbType.Varchar,10,"p_job",ParameterDirection.Output,false ,2,2,System .Data.DataRowVersion.Current,null));
                    callable_command.Parameters.Add(new POLARDBParameter("p_hiredate",
POLARDBTypes.POLARDBDbType.Date,200,"p_hiredate",ParameterDirection.Output,false ,2,2 ,System.Data.DataRowVersion.Current,null));
                    callable_command.Parameters.Add(new POLARDBParameter("p_sal", POLA
RDBTypes.POLARDBDbType.Numeric,200,"p_sal",ParameterDirection.Output,false ,2,2,Syste m.Data.DataRowVersion.Current,null));
                    callable_command.Prepare();
                    callable_command.Parameters[0].Value = 20;
                    callable_command.Parameters[1].Value = 7369;
                    POLARDBDataReader result = callable_command.ExecuteReader();
                    int fc = result.FieldCount;
                    for(int i=0;i<fc;i++)
                        Console.WriteLine("RESULT["+i+"]="+
Convert.ToString(callable_command.Parameters[i].Value));
                    result.Close();
                }
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
                catch(POLARDBException exp)
                {
                    if(exp.ErrorCode.Equals("01403"))
                        Console.WriteLine("No data found");
                    else if(exp.ErrorCode.Equals("01422"))
                        Console.WriteLine("More than one rows were returned by the que
ry");
                    else
                        Console.WriteLine("There was an error Calling the procedure. \
nRoot Cause:\n");
                    Console.WriteLine(exp.Message.ToString());
                }
                //Prepared statement
                string updateQuery  = "update emp set ename = :Name where empno = :ID"
;
                POLARDBCommand Prepared_command = new POLARDBCommand(updateQuery,
conn);
                Prepared_command.CommandType = CommandType.Text;
                Prepared_command.Parameters.Add(new POLARDBParameter("ID", POLARDBType
s.POLARDBDbType.Integer));
                Prepared_command.Parameters.Add(new POLARDBParameter("Name", POLARDBTy
pes.POLARDBDbType.Text));
                Prepared_command.Prepare();
                Prepared_command.Parameters[0].Value = 7369;
                Prepared_command.Parameters[1].Value = "Mark";
                Prepared_command.ExecuteNonQuery();
                Console.WriteLine("Record Updated...");
            }
            catch(POLARDBException exp)
            {
                Console.WriteLine(exp.ToString() );
            }
            finally
            {
                conn.Close();
            }
        }
    }
}
```

**Connection string parameters**

Applications must provide connection strings to connect to databases. The connection strings include the host, username, and password parameters. Connection strings are in the keyword1=value; keyword2=value; format, and are caseinsensitive. You can use double quotation marks (") to enclose the values that contain special characters, such as semicolons (;). The current driver supports the following connection string parameters.

| Paramete r | Example | Description |
|---|---|---|
| Host | localhost | The endpoint of the PolarDB instance. For more information about how to view the endpoint, see View or apply for an endpoint in PolarDB User Guide. |
| Port | 1521 | The port of the PolarDB instance. Default value: 1521. |
| Database | sampledb | The name of the database to be connected. |
| Username | polaruser | The username of the account in the PolarDB instance. |
| Password | password | The password of the account. |

| Parameter | Description |
|---|---|
| application name _ | The name of the application. |
| search path _ | The search path of the schema. |
| client encoding _ | The client code. |
| timezone | The time zone of the session. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User Other parameters.

### RDS PolarDB ODBC

This topic describes how to use the Open Database Connectivity (ODBC) driver to connect a Unix or Windows application to a PolarDB-O instance.

**Prerequisites**

An account is created in PolarDB. For information about how to create accounts in PolarDB, see Create a database and an account. The Windows system is Windows 7 or later and Windows 7 Service Pack 1 is installed. For a UNIX or Linux OS, make sure that the following tools are installed: Libtool 1.5.10 or later unixODBC-devel libpq For 32-bit x86 UNIX or Linux, download PolarDB-ODBC_Linux_X86_32.tar.gz. For 64-bit x86 UNIX or Linux, download PolarDB-ODBC_Linux_X86_64.tar.gz. For 64-bit ARM UNIX or Linux, download PolarDB-ODBC_Linux_arm_64.tar.gz. For 64-bit x86 Windows, download PolarDB-ODBC_Windows_x86_64.7z. For 32-bit x86 Windows, download PolarDB-ODBC_Windows_x86_32.7z.

**Download and install the ODBC driver**

1. Download the ODBC driver.
2. Install the ODBC driver.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS

**Note**

After you decompress the package, you can use the ODBC driver without installation. Run the following command to decompress the package:

```
tar -zxvf polardb_oracle_odbc.tar.gz
```

**Install an ODBC driver in Windows**

1. Download the installation package of the driver that is suitable for the architecture and
version of your OS. For more information, see Download the driver.
2. Extract the installation package.
3. Run the `install.bat` file as an administrator, and then press a random key to exit.
4. **Optional:**To uninstall the ODBC driver, run the `uninstall.bat` file.

**Use the ODBC driver to connect to PolarDB from a Windows**

**server**

1. In **Control Panel**, open **Administrative Tools**.
2. On the **Administrative Tools** page, find and run **ODBC Data Sources**.
3. In the **ODBC Data Source Administrator** dialog box, click **Add**.
4. Select **POLARDB (UNICODE)** as the driver for the data source, and then click **Finish**.
5. In the dialog box that appears, configure the following parameters.

| Parameter | Description |
|---|---|
| Date Source | The name of the data source. |
| Description | The description of the data source. |
| Datebase | The name of the database that you want to connect. |
| SSL Mode | Specifies whether to enable SSL-based encryption. |
| Server | The endpoint of the destination database. |
| Prot | The port of the destination database. Default value: 1521. |
| User Name | The account of the database. |
| Password | The password of the account. |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User
6. Click **Save**.

**Install the ODBC driver in Unix or Linux**

1. Download an ODBC driver based on the architecture and version of your OS. For more
information, see Download the driver.
2. Install the ODBC driver.

**Note**

After you decompress the package, you can use the ODBC driver without installation. Run the following command to decompress the package:

```
tar -zxvf polardb_oracle_odbc.tar.gz
```

**Use the ODBC driver to connect to PolarDB from a UNIX or**

**Linux server**

1. Install Libtool on the Linux server. The version of Libtool must be 1.5.1 or later.

```bash
yum install -y libtool
```

2. Install unixODBC-devel on the Linux server.

| Compile the sample test. The following test files are generated: | Test1 | and | Test2 | . |
|---|---|---|---|---|
| make |  |  |  |  |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```bash
yum install -y unixODBC-devel
```

3. Edit the `odbcinst.ini` file in the /etc directory.

```
vim /etc/odbcinst.ini
```

4. Add the following content to the `odbcinst.ini` file:

```
[POLARDB] Description = ODBC for POLARDB Driver = /root/target/lib/unix/polar-odbc.so Setup = /root/target/lib/unix/libodbcpolarS.so Driver64 = /root/target/lib/unix/polar-odbc.so Setup64 = /root/target/lib/unix/libodbcpolarS.so Database = <Name of the database> Servername = <Endpoint of the database> Password = <Password> Port = <Port number> Username = <Username> Trace = yes TraceFile = /tmp/odbc.log FileUsage = 1
```

**Note**

In the preceding sample code, replace /root with the actual path of the `target` folder.
5. Connect to PolarDB.

```
$isql -v POLARDB +---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+ SQL>
```

**Examples for UNIX or Linux**

The following example shows how to run the `Test1` and `Test2` files.
1. Open the `samples` folder in the ODBC driver folder.

```
cd samples
```

3. Run `Test1` and `Test2` .
ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
./Test1
## Run Test1.
./Test2
## Run Test2.
```

**Note**

`Test1` contains an example in which add, delete, update, and query operations are performed. `Test2` contains an example in which cursors and output parameters are used. The following sample code is only a snippet of the source code. To view the complete source code, check the `Test1` and `Test2` files in the `samples` folder of the ODBC driver package. Sample code of Test1:

```
... int main(int argc, char* argv[]) {
    /*Initialization*/
    RETCODE rCode;
    HENV *hEnv = (HENV*)malloc(sizeof(HENV));
    HDBC *hDBC = (HDBC*)malloc(sizeof(HDBC));
    HSTMT *hStmt = (HSTMT*)malloc(sizeof(HSTMT));
    Connect("POLARDB","user","",&hEnv,&hDBC);
    rCode = SQLAllocStmt(*hDBC,hStmt);
    rCode = SQLAllocHandle(SQL_HANDLE_STMT,*hDBC,hStmt);
    /*Add, delete, modify, and query operations*/
    ExecuteInsertStatement(&hStmt,(UCHAR*) "INSERT INTO EMP(EMPNO,ENAME) VALUES((SELECT
COUNT(EMPNO) FROM EMP),'JACKSON')");
    ExecuteUpdate(&hStmt,(UCHAR*) "UPDATE EMP SET ENAME='ODBC Test' WHERE EMPNO < 100")
;
    ExecuteDeletStatement(&hStmt,(UCHAR*) "DELETE FROM EMP WHERE EMPNO<100");
    ExecuteSimple_Select(&hStmt,(UCHAR*) "SELECT EMPNO,ENAME,JOB,MGR,HIREDATE FROM EMP
where empno = 7369");
    /*Disconnection*/
    Disconnect(&hEnv,&hDBC,&hStmt);
    /*clean up*/
    free(hEnv);
    free(hDBC);
    free(hStmt);
    return 0;
}
```

Sample code for Test2: ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
int main(int argc, char* argv[]) {
    /*Definition*/
    RETCODE rCode;
    SQLUSMALLINT a;
    SQLINTEGER Num1IndOrLen;
    SQLSMALLINT iTotCols = 0;
    int j;
    SDWORD cbData;
    /*Initialization*/
    HENV *hEnv = (HENV*)malloc(sizeof(HENV));
    HDBC *hDBC = (HDBC*)malloc(sizeof(HDBC));
    HSTMT *hStmt = (HSTMT*)malloc(sizeof(HSTMT));
    HSTMT *hStmt1 = (HSTMT*)malloc(sizeof(HSTMT));
    /**Establish a connection**/
    Connect("POLARDB","user","***",&hEnv,&hDBC);
    rCode = SQLAllocStmt(*hDBC,hStmt);
    rCode = SQLAllocStmt(*hDBC,hStmt1);
    rCode = SQLAllocHandle(SQL_HANDLE_STMT,*hDBC,hStmt);
    rCode = SQLAllocHandle(SQL_HANDLE_STMT,*hDBC,hStmt1);
    /*begin*/
    ExecuteSimple_Select(&hStmt1,(UCHAR*) "BEGIN;");
    /*prepare*/
    RETCODE rc = SQLPrepare((*hStmt),(SQLCHAR*)"{ call
refcur_inout_callee2(?,?)}",SQL_NTS);
    rc = SQLBindParameter((*hStmt),1, SQL_PARAM_INPUT_OUTPUT,
SQL_C_CHAR,SQL_REFCURSOR,0, 31,
                strName, 31, &Num1IndOrLen);
    rc = SQLBindParameter((*hStmt),2, SQL_PARAM_INPUT_OUTPUT,
SQL_C_CHAR,SQL_REFCURSOR,0, 31,
                    &strName1, 31, &Num1IndOrLen);
    Num1IndOrLen=0;
    /*execute*/
    rc = SQLExecute((*hStmt));
    if(rc == SQL_SUCCESS || rc == SQL_SUCCESS_WITH_INFO)
    {
        printf("\nstrName _________ = %s\n",strName);
        printf("\nstrName 1_________ = %s\n",strName1);
    }
    printf("\n First Cursor as OUT Parameter \n")   ;
```

This topic describes how to use the PolarDB Oracle Call Interface (OCI) driver to connect to PolarDB.

### PolarDB OCI

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**Prerequisites**

An account is created on a PolarDB cluster. For more information, see Create a database and an account. The server operating system is 64-bit Linux or Windows. The development kit of the Oracle OCI driver is installed.

**Background information**

PolarDB OCI is the native C language interface to databases of PolarDB. You can use PolarDB OCI to build other language-specific interfaces, including PolarDB Java Database Connectivity (JDBC), PolarDB .Net, and PolarDB Open Database Connectivity (ODBC). It allows you to execute query statements and make SQL function calls for PolarDB databases. The current driver version is PostgreSQL 3.0. polardb_oracle_oci.tar Decompress the driver package and import the driver files to environment variables. This allows you to find the correct location of the driver when you compile a demo. You can use the following methods to manually import the driver files to the environment variables in Linux and Windows: Linux i. Copy the libpolaroci.so.10.2, libiconv.so.2, and libpq.so.5.11 files to the /usr/lib directory. ii. Create a symbolic link.

```
ln -s /usr/lib/libpolaroci.so.10.2 /usr/lib/libpolaroci.so ln -s /usr/lib/libiconv.so.2 /usr/lib/libiconv.so ln -s /usr/lib/libpq.so.5.11 /usr/lib/libpq.so ln -s /usr/lib/libpq.so.5.11 /usr/lib/libpq.so.5
```

iii. Set environment variables in Linux.

```
export LD_LIBRARY_PATH= /usr/lib
```

**Note**

If the libiconv.so files already exist in your system, you can directly use these files. You can also follow the instructions in the libiconv documentation to download, compile, and install libiconv, and then use the compiled .so files. In Linux, the libiconv.so files provided by the PolarDB OCI driver are for reference only. Windows i. Configure environment variables. Most IDEs in Windows is capable of importing the paths of linked files. In this topic, Visual Studio 2019 is used to illustrate how to import the paths of linked files, as shown in the following figure. ApsaraDB RDS for PolarDB User ApsaraDB for RDS ii. On the properties tab of the project, add additional library directories. Then, add the .dll files in the driver directory to **Additional Library Directories**.

**Write code**

The following code example shows how to write code. The demo `polardb_demo` in the sample directory is used in the example.

```
/* ============================================================================
 * Copyright (c) 2004-2019 POLARDB Corporation. All Rights Reserved.
 * ===========================================================================
```

`*/`

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <oci.h>
#ifdef WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif
/* Define a macro to handle errors */
#define HANDLE_ERROR(x,y) check_oci_error(x,y)
#define DATE_FMT "DAY, MONTH DD, YYYY"
#define DATE_LANG "American"
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
sword ConvertStringToDATE( char *datep, char *formatp, dvoid *datepp ); /* A Custom Routine to handle errors, */ /* this demonstrates the Error/ Exception Handling in OCI */ void check_oci_error (dvoid * errhp, sword status);
```

`/*`

```
 * <<<<<<<<<<<<<<<<<<< FUNCTION PROTOTYPES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```

`*/`

```
/* Initialize & Allocate all handles */ void initHandles (OCISvcCtx **, OCIServer **, OCISession **, OCIError **,
         OCIEnv **);
/* logon to the database and begin user-session */ void logon (OCISvcCtx **, OCIServer **, OCISession **, OCIError **,
       OCIEnv **, text *, text *, text *);
/* Create required table(s) */ void create_table (OCISvcCtx *, OCIError *, OCIEnv *); /* prepare data for our examples */ void prepare_data (OCISvcCtx *, OCIError *, OCIEnv *); /* create procedures/functions to demonstrate in the example */ void create_stored_procs (OCISvcCtx *, OCIError *, OCIEnv *); /* select and print data by iterating through resultSet */ void select_print_data (OCISvcCtx *, OCIError *, OCIEnv *); /* demonstrate calling stored procedures and retrieving values */ /* proc1 demonstrates IN OUT */ void call_stored_proc1 (OCISvcCtx *, OCIError *, OCIEnv *); /* proc2 demonstrates OUT */ void call_stored_proc2 (OCISvcCtx *, OCIError *, OCIEnv *); /* drop required table(s) */ void drop_table (OCISvcCtx *, OCIError *, OCIEnv *); void drop_stored_procs (OCISvcCtx *, OCIError *, OCIEnv *); /* clean-up main handles before exit */ void cleanup (OCISvcCtx **, OCIServer **, OCISession **, OCIError **, OCIEnv **);
```

`/*`

```
 * <<<<<<<<<<<<<<<<<<<<<<<<< END OF FUNCTION PROTOYPES<<<<<<<<<<<<<<<<<<<<<<<<<<
```

`*/` ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
/* <<<<<<<<<< Global Variables */ ub4 init_mode = OCI_DEFAULT; ub4 auth_mode = OCI_CRED_RDBMS; /* <<<<<<<<<< End Global Variables */ int main (void) {
```

`/*`

```
   * Declare Handles, a typical OCI program would need atleast
   * following handles Enviroment Handle Error Handle Service Context
   * Handle Server Handle User Session (Authentication Handle)
```

`*/`

```
  /* Enviroment */
  OCIEnv *envhp;
  /* Error */
  OCIError *errhp;
  /* Service Context */
  OCISvcCtx *svchp;
  /* Server */
  OCIServer *srvhp;
  /* Session(authentication) */
  OCISession *authp;
```

`/*`

```
   * End of Handle declaration
```

`*/` `/*`

```
   * Declare local variables,
```

`*/`

```
  text *username = (text *) "parallels";
  text *passwd = (text *) "";
```

`/*`

```
   * Oracle Instant Client Connection String
```

`*/`

```
  text *server = (text *) "//localhost:5432/postgres";
```

`/*`

```
   * Initialize and Allocate handles
```

`*/`

```
  initHandles (&svchp, &srvhp, &authp, &errhp, &envhp);
```

`/*` ApsaraDB for RDS ApsaraDB RDS for PolarDB User `/*`

```
   * logon to the database
```

`*/`

```
  logon (&svchp, &srvhp, &authp, &errhp, &envhp, username, passwd, server);
```

`/*`

```
   * Create table(s) required for this example
```

`*/`

```
  create_table (svchp, errhp, envhp);
```

`/*`

```
   * insert data into table
```

`*/`

```
  prepare_data (svchp, errhp, envhp);
```

`/*` `*/`

```
  create_stored_procs (svchp, errhp, envhp);
```

`/*`

```
   * select and print data by iterating through simple resultSet
```

`*/`

```
  select_print_data (svchp, errhp, envhp);
```

`/*`

```
   * demonstrate calling stored procedures and retrieving values
```

`*/`

```
  call_stored_proc1 (svchp, errhp, envhp);
```

`/*`

```
   * demonstrate OUT parameters
```

`*/`

```
  call_stored_proc2 (svchp, errhp, envhp);
```

`/*`

```
   * Drop table(s) used in this example
```

`*/`

```
  drop_table (svchp, errhp, envhp);
```

`/*`

```
   * Drop stroed procedures & functions used in this example
```

`*/`

```
  drop_stored_procs (svchp, errhp, envhp);
```

`/*`

```
   * clean up resources
```

`*/`

```
  cleanup (&svchp, &srvhp, &authp, &errhp, &envhp);
  return 0;
} /* A Custom Routine to handle errors, */
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
/* this demonstrates the Error/ Exception Handling in OCI */ void check_oci_error (dvoid * errhp, sword status) {
  text errbuf[512];
  sb4 errcode;
  if (status == OCI_SUCCESS)
    {
      return;
    }
  switch (status)
    {
    case OCI_SUCCESS_WITH_INFO:
      printf ("OCI_SUCCESS_WITH_INFO:\n");
      OCIErrorGet (errhp, (ub4) 1, (text *) 0, &errcode,
           errbuf, (ub4) sizeof (errbuf), OCI_HTYPE_ERROR);
      printf ("%s", errbuf);
      break;
    case OCI_NEED_DATA:
      printf ("Error - OCI_NEED_DATA\n");
      break;
    case OCI_NO_DATA:
      printf ("Error - OCI_NO_DATA\n");
      break;
    case OCI_ERROR:
      printf ("Error - OCI_ERROR:\n");
      OCIErrorGet (errhp, (ub4) 1, (text *) 0, &errcode,
           errbuf, (ub4) sizeof (errbuf), OCI_HTYPE_ERROR);
      printf ("%s", errbuf);
      break;
    case OCI_INVALID_HANDLE:
      printf ("Error - OCI_INVALID_HANDLE\n");
      break;
    case OCI_STILL_EXECUTING:
      printf ("Error - OCI_STILL_EXECUTING\n");
      break;
    case OCI_CONTINUE:
      printf ("Error - OCI_CONTINUE\n");
      break;
    default:
      break;
    }
```

`/*`

```
   * exit app
```

`*/`

```
  exit((int)status);
} /* Initialize & Allocate required handles */ void initHandles (OCISvcCtx ** svchp, OCIServer ** srvhp, OCISession ** authp,
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
         OCIError ** errhp, OCIEnv ** envhp)
{
```

`/*`

```
   * Now Starts the Section where we have to initialize & Allocate
   * basic handles. This is a compulsory setup or initilization which
   * is required before we can proceed to logon and work with the
   * database. This initialization and prepration will include the
   * following steps
```

*

```
   * 1. Initialize the OCI (OCIInitialize()) 2. Initialize the
   * Environment (OCIEnvInit()) 3. Initialize & Allocate Error Handle
   * 4. Initialize & Allocate Service Context Handle 5. Initialize &
   * Allocate Session Handle 6. Initialize & Allocate Server Handle
```

*

```
   * As per the new versions of OCI , instead of using OCIInitialize()
   * and OCIEnvInit(), we can do this with one API Call called
   * OCIEnvCreate().
```

`*/` `/*`

```
   * Initialize OCI
```

`*/`

```
  if (OCIInitialize (init_mode, (dvoid *) 0,
             (dvoid * (*)(dvoid *, size_t)) 0,
             (dvoid * (*)(dvoid *, dvoid *, size_t)) 0,
             (void (*)(dvoid *, dvoid *)) 0) != OCI_SUCCESS)
    {
      printf ("ERROR: failed to initialize OCI\n");
      exit (1);
    }
```

`/*`

```
   * Initialize Enviroment.
```

`*/`

```
  HANDLE_ERROR (*envhp,
        OCIEnvInit (&(*envhp), OCI_DEFAULT, (size_t) 0,
                (dvoid **) 0));
```

`/*`

```
   * Initialize & Allocate Error Handle
```

`*/`

```
  HANDLE_ERROR (*envhp,
        OCIHandleAlloc (*envhp, (dvoid **) & (*errhp),
                OCI_HTYPE_ERROR, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Initialize & Allocate Service Context Handle
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIHandleAlloc (*envhp, (dvoid **) & (*svchp),
                OCI_HTYPE_SVCCTX, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Initialize & Allocate Session Handle
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS `*/`

```
  HANDLE_ERROR (*errhp,
        OCIHandleAlloc (*envhp, (dvoid **) & (*authp),
                OCI_HTYPE_SESSION, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Initialize & Allocate Server Handle
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIHandleAlloc (*envhp, (dvoid **) & (*srvhp),
                OCI_HTYPE_SERVER, (size_t) 0, (dvoid **) 0));
} void logon (OCISvcCtx ** svchp, OCIServer ** srvhp, OCISession ** authp,
       OCIError ** errhp, OCIEnv ** envhp, text * username, text * passwd,
       text * server)
{
```

`/*`

```
   * Now Starts our Logon to the Database Server which includes two
   * steps
```

*

```
   * 1. Attaching to the Server 2. Starting or Begining of the Session
```

*

```
   * This is the complex logon. The easy ways to logon is to avoid
   * server attach and session begin and simply use OCILogon() or
   * OCILogon2() and then logoff using OCILogoff()
```

`*/` `/*`

```
   * Attach to the server
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIServerAttach (*srvhp, *errhp, server,
                 (ub4) strlen ((char *) server),
                 OCI_DEFAULT));
```

`/*`

```
   * The following code will start a session but before we start a
   * session we have to 1. Set the Server Handle which is now attached
   * into Service Context Handle 2. Set the Username and password into
   * Session Handle
```

`*/` `/*`

```
   * Set the Server Handle into Service Context Handle
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIAttrSet (*svchp, OCI_HTYPE_SVCCTX,
                (dvoid *) (*srvhp), (ub4) 0, OCI_ATTR_SERVER,
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
                *errhp));
```

`/*`

```
   * Set the username and password into session handle
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIAttrSet (*authp, OCI_HTYPE_SESSION,
                (dvoid *) username,
                (ub4) strlen ((char *) username),
                OCI_ATTR_USERNAME, *errhp));
  HANDLE_ERROR (*errhp,
        OCIAttrSet (*authp, OCI_HTYPE_SESSION, (dvoid *) passwd,
                (ub4) strlen ((char *) passwd), OCI_ATTR_PASSWORD,
                *errhp));
```

`/*`

```
   * Now FINALLY Begin our session
```

`*/`

```
  HANDLE_ERROR ((*errhp),
        OCISessionBegin (*svchp, *errhp,
                 *authp, auth_mode, OCI_DEFAULT));
  printf ("********************************************\n");
  printf ("Milestone  : Logged on as --> '%s'\n", username);
  printf ("********************************************\n");
```

`/*`

```
   * After we Begin our session we will have to set the Session
```

`*/` `/*`

```
   * (authentication) handle into Service Context Handle
```

`*/`

```
  HANDLE_ERROR (*errhp,
        OCIAttrSet (*svchp, OCI_HTYPE_SVCCTX,
                (dvoid *) (*authp), (ub4) 0,
                OCI_ATTR_SESSION, *errhp));
} /* Create table(s) required for this example */ void create_table (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *stmhp;
  text *create_statement =
    (text *)"CREATE TABLE OCISPEC \n (ENAME VARCHAR2(20)\n, MGR NUMBER\n, HIREDATE DATE
)";
  ub4 status = OCI_SUCCESS;
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/` ApsaraDB RDS for PolarDB User ApsaraDB for RDS `*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the Create statement
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp,
                create_statement,
                strlen ((const char *) create_statement),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
```

`/*`

```
   * Execute the Create Statement
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN CREATING TABLE(S)\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Table(s) Successfully created\n");
      printf ("********************************************\n");
    }
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
} /* prepare data for our examples */ void prepare_data (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *stmhp;
  text *insstmt =
    (text *)
    "INSERT INTO OCISPEC (ename,mgr, hiredate) VALUES (:ENAME,:MGR, CAST(:HIREDATE AS t
imestamp))";
  OCIBind *bnd1p = (OCIBind *) 0;    /* the first bind handle   */
  OCIBind *bnd2p = (OCIBind *) 0;    /* the second bind handle */
  OCIBind *bnd3p = (OCIBind *) 0;    /* the third bind handle   */
  ub4 status = OCI_SUCCESS;
  int i = 0;
  char *ename[3] = { "SMITH", "ALLEN", "KING" };
  sword mgr[] = { 7886, 7110, 7221 };
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  char *date_buffer[3] = { "02-AUG-07", "02-APR-07", "02-MAR-07" };
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the insert statement
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp, insstmt,
                (ub4) strlen ((char *) insstmt),
                (ub4) OCI_NTV_SYNTAX, (ub4) OCI_DEFAULT));
```

`/*`

```
   * In this loop we will bind data from the arrays to insert multi
   * rows in the database a more elegant and better way to do this is
   * to use Array Binding (Batch Inserts). POLARDB OCI Replacement
   * Library WILL support Array Bindings even if it is not used here
   * right now
```

`*/`

```
  for (i = 0; i < 3; i++)
    {
```

`/*`

```
       * Bind Variable for ENAME
```

`*/`

```
      HANDLE_ERROR (errhp,
            OCIBindByName (stmhp, &bnd1p, errhp, (text *) ":ENAME",
                   -1, (dvoid *) ename[i],
                   (sb4) strlen (ename[i]) + 1, SQLT_STR,
                   (dvoid *) 0, 0, (ub2 *) 0, (ub4) 0,
                   (ub4 *) 0, OCI_DEFAULT));
```

`/*`

```
       * Bind Variable for MGR
```

`*/`

```
      HANDLE_ERROR (errhp,
            OCIBindByName (stmhp, &bnd2p, errhp, (text *) ":MGR",
                   -1, (dvoid *) & mgr[i], sizeof (mgr[i]),
                   SQLT_INT, (dvoid *) 0, 0, (ub2 *) 0,
                   (ub4) 0, (ub4 *) 0, OCI_DEFAULT));
```

`/*`

```
       * Bind Variable for HIREDATE
```

`*/`

```
      HANDLE_ERROR (errhp,
            OCIBindByName (stmhp, &bnd3p, errhp, (text *) ":HIREDATE",
                   -1, (dvoid *)  date_buffer[i],
                   strlen(date_buffer[i])+1, SQLT_STR, (dvoid *) 0, 0,
                   (ub2 *) 0, (ub4) 0, (ub4 *) 0,
                   OCIDEFAULT));
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS _ `/*`

```
       * Execute the statement and insert data
```

`*/`

```
      if ((status = OCIStmtExecute (svchp, stmhp, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN INSERTING DATA\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
    }
  OCITransCommit (svchp, errhp, (ub4) 0);
  printf ("********************************************\n");
  printf
    ("MileStone : Data Sucessfully inserted \n & Committed via Transaction\n");
  printf ("********************************************\n");
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
} /* Create Stored procedures and functions to be used in this example */ void create_stored_procs (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
```

`/*`

```
   * This function created 2 stored procedures and one stored function
   * 1. StoredProcedureSample1 - is to exhibit exeucting procedure and
   * recieving values from an IN OUT parameter 2.
   * StoredProcedureSample2 - is to exhibit executing procedure and
   * recieving values from an OUT parameter 3. StoredProcedureSample3 -
   * is to exhibit executing a function and recieving the value
   * returned by the function in a Callable Statement way
```

`*/`

```
  OCIStmt *stmhp;
  OCIStmt *stmhp2;
  OCIStmt *stmhp3;
  text *create_statement =
    (text *)"CREATE OR REPLACE PROCEDURE StoredProcedureSample1\n (mgr1 int, ename1 IN
OUT varchar2)\n is\nbegin\ninsert into ocispec (mgr, ename) values (7990,'STOR1');\nename1 := 'Successful';\n end;\n";
  text *create_statement2 =
    (text *)"CREATE OR REPLACE PROCEDURE StoredProcedureSample2\n(mgr1 int, ename1 varc
har2,eout1 OUT varchar2)\nis\nbegin\ninsert into ocispec(mgr,ename) values (7991, 'STOR 2');\neout1 := 'Successful';\n end;";
  text *create_statement3 =
    (text *)"CREATE OR REPLACE FUNCTION f1\nRETURN VARCHAR2\nis\nv_Sysdate
DATE;\nv_charSysdate VARCHAR2(20);\nbegin\nSELECT TO_CHAR(SYSDATE, 'dd-mon-yyyy') into v_charSysdate FROM DUAL;\n return(v_charSysdate);\nend;";
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  ub4 status = OCI_SUCCESS;
```

`/*`

```
   * Initialize & Allocate Statement Handles
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp2,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp3,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the Create statements
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp,
                create_statement,
                strlen ((const char *) create_statement),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp2, errhp, create_statement2,
                strlen ((const char *) create_statement2),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp3, errhp, create_statement3,
                strlen ((const char *) create_statement3),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
```

`/*`

```
   * Execute the Create Statement SampleProcedure1
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN CREATING PROCEDURE 1\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 1 Successfully created\n");
      printf ("********************************************\n");
    }
```

`/*` ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
   * Execute the Create Statement Sample Procedure2
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp2, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN CREATING PROCEDURE 2\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 2 Successfully created\n");
      printf ("********************************************\n");
    }
```

`/*`

```
   * Execute the Create Statement Sample Procedure3
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp3, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN CREATING PROCEDURE 3\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 3 Successfully created\n");
      printf ("********************************************\n");
    }
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp2, OCI_HTYPE_STMT));
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp3, OCI_HTYPE_STMT));
} /* select and print data by iterating through resultSet */ void select_print_data (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  /* Statement */
  OCIStmt *stmhp;
  /* Define */
  OCIDefine *define;
  /* Buffer for employee Name */
  char ename_buffer[10] ;
  /* Buffer for mgr */
sordmgrbffer
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  sword mgr_buffer;
  /*Buffer for hiredate */
  char hire_date[20];
```

`/*`

```
   * a simple select statement
```

`*/`

```
  text * sql_statement =
      (text *) "select ename,mgr,hiredate from ocispec";
```

`/*`

```
   * additional local variables
```

`*/`

```
  ub4 rows = 1;
  ub4 fetched = 1;
  ub4 status = OCI_SUCCESS;
  sb2 null_ind_ename = 0;
  /* null indicator for ename */
  sb2 null_ind_mgr = 0;
  /* null indicator for mgr */
  sb2 null_ind_hiredate = 0;
  /* null indicator for hiredate */
```

`/*`

```
   * Now we are going to start the Milestone of a Simple Query of the
   * database and loop through the resultSet This would include
   * following steps
```

*

```
   * 1. Initialize and Allocate the Statement Handle 2. Prepare the
   * Statement 3. Define Output variables to recieve the output of the
   * select statement 4. Execute the statement 5. Fetch the resultset
   * and Print values
```

* `*/`

```
memset( ename_buffer, 0, sizeof(ename_buffer) ); memset( hire_date, 0, sizeof(hire_date) );
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the statement
```

`*/`

```
HANDLEERROR(errhp,
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp,
                sql_statement,
                strlen ((const char *) sql_statement),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
```

`/*`

```
   * Bind a String (OCIString) variable on position 1. Datatype used
   * SQLT_VST
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIDefineByPos (stmhp, &define, errhp,
                (ub4) 1, ename_buffer, 10,
                (ub2) SQLT_STR, &null_ind_ename, 0, 0,
                OCI_DEFAULT));
```

`/*`

```
   * Bind a Number (OCINumber) variable on position 2. Datatype used
   * SQLT_VNU
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIDefineByPos (stmhp, &define, errhp,
                (ub4) 2, &mgr_buffer, sizeof (sword),
                (ub2) SQLT_INT, &null_ind_mgr, 0, 0,
                OCI_DEFAULT));
```

`/*`

```
   * Bind a Date (OCIDate) variable on position 3. Datatype used
   * SQLT_ODT
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIDefineByPos (stmhp, &define, errhp,
                (ub4) 3, hire_date, 20,
                (ub2) SQLT_STR, &null_ind_hiredate, 0, 0,
                OCI_DEFAULT));
```

`/*`

```
   * Execute the simple SQL Statement
```

`*/`

```
  status = OCIStmtExecute (svchp, stmhp, errhp,
               rows, (ub4) 0, NULL, NULL, OCI_DEFAULT);
```

`/*`

```
   * Print the Resultset
```

`*/`

```
  if (status == OCI_NO_DATA)
    {
```

`/*`

```
       * indicates didn't fetch anything (as we're not array
       * fetching)
```

`*/` ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
      fetched = 0;
    }
  else
    {
      HANDLE_ERROR (errhp, status);
    }
  if (fetched)
    {
```

`/*`

```
       * print string
```

`*/`

```
      if (null_ind_ename == -1)
    printf ("name -> [NULL]\t");
      else
    printf ("name -> [%s]\t",  ename_buffer);
```

`/*`

```
       * print number by converting it into int
```

`*/`

```
      if (null_ind_mgr == -1)
    printf ("mgr -> [NULL]\n");
      else
    {
      printf ("mgr -> [%d]\n", mgr_buffer);
    }
      if (null_ind_hiredate == -1)
    printf ("hiredate -> [NULL]\n");
      else
    {
      printf ("hiredate -> [%s]\n",hire_date );
    }
```

`/*`

```
       * loop through the resultset one by one through
       * OCIStmtFetch()
```

`*/` `/*`

```
       * untill we find nothing
```

`*/`

```
      while (1)
    {
      status = OCIStmtFetch (stmhp, errhp,
                 rows, OCI_FETCH_NEXT, OCI_DEFAULT);
      if (status == OCI_NO_DATA)
        {
```

`/*`

```
           * indicates couldn't fetch anything
```

`*/`

```
          break;
        }
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
      else
        {
          HANDLE_ERROR (errhp, status);
        }
```

`/*`

```
       * print string
```

`*/`

```
      if (null_ind_ename == -1)
        printf ("name -> [NULL]\t");
      else
        printf ("name -> [%s]\t", ename_buffer);
```

`/*`

```
       * print number by converting it into int
```

`*/`

```
      if (null_ind_mgr == -1)
        printf ("mgr -> [NULL]\n");
      else
        {
        printf ("mgr -> [%d]\n", mgr_buffer);
        }
```

`/*`

```
       * print date after converting to text
```

`*/`

```
      if (null_ind_hiredate == -1)
        printf ("hiredate -> [NULL]\n");
      else
        {
          printf ("hiredate -> [%s]\n", hire_date);
        }
    }
    }
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
} void call_stored_proc1 (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *p_sql;
  OCIBind *p_Bind1 = (OCIBind *) 0;
  OCIBind *p_Bind2 = (OCIBind *) 0;
  char field2[20];
```

`/*`

```
   * char field3[20];
```

`*/`

```
  sword field1 = 3;
  text *mySql = (text *) "Begin StoredProcedureSample1(:MGR, :ENAME); END";
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  memset( field2, 0, sizeof(field2) );
  strcpy( field2, "Entry 3" );
  printf ("*************************************************\n");
  printf ("Example 1 - Using an IN OUT Parameter\n");
  printf ("*************************************************\n");
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & p_sql,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (p_sql, errhp, mySql,
                (ub4) strlen ((char *)mySql), OCI_NTV_SYNTAX,
                OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIBindByPos (p_sql, &p_Bind1, errhp, 1,
                  (dvoid *) & field1, sizeof (sword),
                  SQLT_INT, 0, 0, 0, 0, 0, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIBindByPos (p_sql, &p_Bind2, errhp, 2,
                  field2, (sizeof (field2)),
                  SQLT_STR, 0, 0, 0, 0, 0, OCI_DEFAULT));
  printf (" Field2 Before:\n");
  printf (" size ---> %d\n", sizeof (field2));
  printf (" length ---> %d\n", strlen (field2));
  printf (" value ---> %s\n", field2);
  HANDLE_ERROR (errhp,
        OCIStmtExecute (svchp, p_sql, errhp, (ub4) 1, (ub4) 0,
                (OCISnapshot *) NULL, (OCISnapshot *) NULL,
                (ub4) OCI_COMMIT_ON_SUCCESS));
  printf (" Field2 After:\n");
  printf (" size ---> %d\n", sizeof (field2));
  printf (" length ---> %d\n", strlen (field2));
  printf (" value ---> %s\n", field2);
  HANDLE_ERROR (errhp, OCIHandleFree (p_sql, OCI_HTYPE_STMT));
} void call_stored_proc2 (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *p_sql;
OCIBid* Bid1 (OCIBid*)0
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
  OCIBind *p_Bind1 = (OCIBind *) 0;
  OCIBind *p_Bind2 = (OCIBind *) 0;
  OCIBind *p_Bind3 = (OCIBind *) 0;
  char field2[20] = "Entry 3";
  char field3[20];
  sword field1 = 3;
  text *mySql =
    (text *) "Begin StoredProcedureSample2(:MGR, :ENAME, :EOUT); END";
  memset( field2, 0, sizeof(field2) );
  strcpy( field2, "Entry 3" );
  memset( field3, 0, sizeof(field3) );
  printf ("*************************************************\n");
  printf ("Example 2 - Using an OUT Parameter\n");
  printf ("*************************************************\n");
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & p_sql,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (p_sql, errhp, mySql,
                (ub4) strlen ((char *)mySql), OCI_NTV_SYNTAX,
                OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIBindByPos (p_sql, &p_Bind1, errhp, 1,
                  (dvoid *) & field1, sizeof (sword),
                  SQLT_INT, 0, 0, 0, 0, 0, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIBindByPos (p_sql, &p_Bind2, errhp, 2,
                  field2, strlen (field2) + 1,
                  SQLT_STR, 0, 0, 0, 0, 0, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIBindByPos (p_sql, &p_Bind3, errhp, 3,
                  field3, 20,
                  SQLT_STR, 0, 0, 0, 0, 0, OCI_DEFAULT));
  printf (" Field3 Before:\n");
  printf (" size ---> %d\n", sizeof (field3));
  printf (" length ---> %d\n", strlen (field3));
  printf (" value ---> %s\n", field3);
HANDLEERROR(errhp
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  HANDLE_ERROR (errhp,
        OCIStmtExecute (svchp, p_sql, errhp, (ub4) 1, (ub4) 0,
                (OCISnapshot *) NULL, (OCISnapshot *) NULL,
                (ub4) OCI_COMMIT_ON_SUCCESS));
  printf (" Field3 After:\n");
  printf (" size ---> %d\n", sizeof (field3));
  printf (" length ---> %d\n", strlen (field3));
  printf (" value ---> %s\n", field3);
  HANDLE_ERROR (errhp, OCIHandleFree (p_sql, OCI_HTYPE_STMT));
} /* drop table(s) required for this example */ void drop_table (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *stmhp;
  text *statement = (text *)"DROP TABLE OCISPEC";
  ub4 status = OCI_SUCCESS;
```

`/*`

```
   * Initialize & Allocate Statement Handle
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the drop statement
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp,
                statement, strlen ((const char *) statement),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
```

`/*`

```
   * Execute the drop Statement
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN DROPING TABLE(S)\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Table(s) Successfully Dropped\n");
      printf ("********************************************\n");
    }
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
}
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
} void drop_stored_procs (OCISvcCtx * svchp, OCIError * errhp, OCIEnv * envhp) {
  OCIStmt *stmhp;
  OCIStmt *stmhp2;
  OCIStmt *stmhp3;
  text *create_statement = (text *)"DROP PROCEDURE StoredProcedureSample1";
  text *create_statement2 = (text *)"DROP PROCEDURE StoredProcedureSample2";
  text *create_statement3 = (text *)"DROP FUNCTION  f1";
  ub4 status = OCI_SUCCESS;
  OCITransCommit( svchp, errhp, OCI_DEFAULT );
```

`/*`

```
   * Initialize & Allocate Statement Handles
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp2,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
  HANDLE_ERROR (errhp,
        OCIHandleAlloc (envhp, (dvoid **) & stmhp3,
                OCI_HTYPE_STMT, (size_t) 0, (dvoid **) 0));
```

`/*`

```
   * Prepare the Create statements
```

`*/`

```
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp, errhp,
                create_statement,
                strlen ((const char *) create_statement),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp2, errhp, create_statement2,
                strlen ((const char *) create_statement2),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
  HANDLE_ERROR (errhp,
        OCIStmtPrepare (stmhp3, errhp, create_statement3,
                strlen ((const char *) create_statement3),
                OCI_NTV_SYNTAX, OCI_DEFAULT));
```

`/*`

```
   * Execute the Create Statement SampleProcedure1
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN DROPPING PROCEDURE 1\n");
      HANDLE_ERROR (errhp, status);
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 1 Successfully dropped\n");
      printf ("********************************************\n");
    }
```

`/*`

```
   * Execute the Create Statement Sample Procedure2
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp2, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN DROPPING PROCEDURE 2\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 2 Successfully dropped\n");
      printf ("********************************************\n");
    }
```

`/*`

```
   * Execute the Create Statement Sample Procedure3
```

`*/`

```
  if ((status = OCIStmtExecute (svchp, stmhp3, errhp,
                   (ub4) 1, (ub4) 0, NULL, NULL, OCI_DEFAULT)) < OCI_SUCCESS)
    {
      printf ("FAILURE IN DROPPING PROCEDURE 3\n");
      HANDLE_ERROR (errhp, status);
      return;
    }
  else
    {
      printf ("********************************************\n");
      printf ("MileStone : Sample Procedure 3 Successfully dropped\n");
      printf ("********************************************\n");
    }
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp, OCI_HTYPE_STMT));
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp2, OCI_HTYPE_STMT));
  HANDLE_ERROR (errhp, OCIHandleFree (stmhp3, OCI_HTYPE_STMT));
} /* Clean your mess up */ void cleanup (OCISvcCtx ** svchp, OCIServer ** srvhp, OCISession ** authp,
     OCIError ** errhp, OCIEnv ** envhp)
```

| Parameter | Example | Description |
|---|---|---|
| text *username | (text *) "postgres" | The username of the PolarDB instance. |
| text *passwd | (text *) "" | The password for the username of the PolarDB instance. |
| text *server | (text *) "//localhost:5432" | The endpoint and port of the PolarDB instance. |

|  |  | (text *) |  |
|---|---|---|---|
|  | "//localhost:5432" |  |  |

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
{
```

`/*`

```
   * log off
```

`*/`

```
  HANDLE_ERROR (*errhp, OCISessionEnd (*svchp, *errhp, *authp, OCI_DEFAULT));
  printf ("logged off\n");
```

`/*`

```
   * detach from server
```

`*/`

```
  HANDLE_ERROR (*errhp, OCIServerDetach (*srvhp, *errhp, OCI_DEFAULT));
  printf ("detached form server\n");
```

`/*`

```
   * free up handles
```

`*/`

```
  HANDLE_ERROR (*errhp, OCIHandleFree (*authp, OCI_HTYPE_SESSION));
  /* free session handle */
  *authp = 0;
  HANDLE_ERROR (*errhp, OCIHandleFree (*srvhp, OCI_HTYPE_SERVER));
  /* free server handle */
  *srvhp = 0;
  HANDLE_ERROR (*errhp, OCIHandleFree (*svchp, OCI_HTYPE_SVCCTX));
  /* free service context */
  *svchp = 0;
  HANDLE_ERROR (*errhp, OCIHandleFree (*errhp, OCI_HTYPE_ERROR));
  /* free error handle */
  *errhp = 0;
  OCIHandleFree (*envhp, OCI_HTYPE_ENV);
  /* free environment handle */
  *envhp = 0;
  printf ("free'd all handles\n");
}
```

In the preceding code example, you must replace the following parameters with the connection information of your PolarDB instance.

**Note**

For more information about the Oracle native OCI driver, visit OCI: Introduction.

**Compile code**

Linux ApsaraDB for RDS ApsaraDB RDS for PolarDB User i. Modify the Makefile file to dynamically link to the path where the polaroci.so file is located. The following content is an example of the Makefile file:

```bash
# ============================================================================
# Copyright (c) 2004-2012 PolarDB Corporation. All Rights Reserved.
# ===========================================================================
# Makefile to build C testcases for OCILib
```

#

```
CC=gcc CFLAGS=-Wall -g -I$(ORACLE_HOME)/ -L $(POLARDBOCI_LIB) -lpolardboci -lpq -liconv SAMPLES = polardb_demo all: $(SAMPLES) %:%.o
    $(CC) $(CFLAGS) -o $@
clean:
    rm -rf $(SAMPLES)
```

Link ORACLE_HOME to the directory instantclient_12_1/sdk/include of the oracle oci header file that is downloaded from the driver directory. Link POLARDBOCI_LIB to the directory where the libpolardboci.so, libpq.so, and libiconv.so files are located. ii. Run the following command to compile the code:

```
make
```

Windows Visual Studio is used in the example. i. Add the path of the oracle oci development package in the driver directory to **C/C++ >**
**General > Attachment Include Directories**.
ii. Add the paths of polardboci.dll and polardboci.lib in the driver directory to **Linker >**
**General > Additional Library Directories**.
ApsaraDB RDS for PolarDB User ApsaraDB for RDS iii. Enter polardboci.lib in **Linker > Input > Additional Dependencies**. ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**Examples**

The following executable file is obtained after polardb_demo is compiled:

```
********************************************
Milestone : Logged on as --> 'parallels'
********************************************
********************************************
MileStone : Table(s) Successfully created
********************************************
********************************************
MileStone : Data Sucessfully inserted
 & Committed via Transaction
********************************************
********************************************
MileStone : Sample Procedure 1 Successfully created
********************************************
********************************************
MileStone : Sample Procedure 2 Successfully created
********************************************
********************************************
MileStone : Sample Procedure 3 Successfully created
********************************************
name -> [SMITH] mgr -> [7886] hiredate -> [2007-08-02 00:00:00] name -> [ALLEN] mgr -> [7110] hiredate -> [2007-04-02 00:00:00] name -> [KING] mgr -> [7221] hiredate -> [2007-03-02 00:00:00]
*************************************************
Example 1 - Using an IN OUT Parameter
*************************************************
 Field2 Before:
 size ---> 20
 length ---> 7
 value ---> Entry 3
 Field2 After:
 size ---> 20
 length ---> 10
 value ---> Successful
*************************************************
Example 2 - Using an OUT Parameter
*************************************************
 Field3 Before:
 size ---> 20
 length ---> 0
 value --->
 Field3 After:
 size ---> 20
 length ---> 10
 value ---> Successful
********************************************
MileStone : Table(s) Successfully Dropped
********************************************
********************************************
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
MileStone : Sample Procedure 1 Successfully dropped
********************************************
********************************************
MileStone : Sample Procedure 2 Successfully dropped
********************************************
********************************************
MileStone : Sample Procedure 3 Successfully dropped
********************************************
logged off detached form server free'd all handles
```

### PolarDB PHP

This topic describes how to connect a PHP client to a PolarDB cluster.

**Prerequisites**

An account is created for a PolarDB instance. For more information, see Create an account.

**Prepare the environment in Windows**

1. Download and install WampServer. For more information, visit WampServer official website.
2. Start the PostgreSQL plug-in.
i. Modify the `php.ini` file. ii. Remove semicolons (;) from the following code. Before removing semicolons:

```
;extension=php_pgsql.dll ;extension=php_pdo_pgsql.dll
```

After removing semicolons:

```
extension=php_pgsql.dll extension=php_pdo_pgsql.dll
```

3. Copy the `libpq.dll` file from the C:\wamp\bin\php\php5.3.5 directory to the
C:\windows\system32\ directory. Note: php5.3.5 is used in this example, and the actual directory varies based on your client version.
4. Restart the Apache service.

**Prepare the environment in Linux**

1. Install the `php-pgsql.x86_64` driver.

```bash
sudo yum install php-pgsql.x86_64
```

2. Modify the `php.ini` file.

```
vim /etc/php.ini
```

3. Add the following content to the `php.ini` file.

```
extension=php_pgsql.so
```

| Parameter | Example | Description |
|---|---|---|
| host | "host=xxxxxx" | The endpoint of the PolarDB cluster. For more information about how to view the endpoint, see View or apply for an endpoint in PolarDB User Guide. |
| port | "port=1521" | The port of the PolarDB cluster. |
| dbname | "dbname=xxxx" | The name of the database to be connected. |
| credentials | "user=xxx password=xxxx" | The username and password used to log on to the PolarDB cluster. |

|  |  | "user=xxx |
|---|---|---|
| s | password=xxxx" |  |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**Connect to PolarDB**

After you prepare the environment in Windows or Linux, you can run a PHP script to connect to the PolarDB cluster. The following sample code shows how to use PHP to connect to the PolarDB cluster.

```
<?php
 $host    = "host=xxxx";
 $port    = "port=xxxx";
 $dbname   = "dbname=xxxx";
 $credentials = "user=xxxx password=xxxxx";
 $db = pg_connect( "$host $port $dbname $credentials" );
 if(!$db){
  echo "Error : Unable to open database\n";
 } else {
  echo "Opened database successfully\n";
 }
 $sql =<<<EOF
  select * from pg_roles;
EOF;
 $ret = pg_query($db, $sql);
 if(!$ret){
  echo pg_last_error($db);
 } else {
  echo "Records created successfully\n";
 }
 $results = pg_fetch_all($ret);
 print_r($results);
 pg_close($db);
```

?> In the preceding sample code, the connection information of PolarDB consists of parameters, such as `host` , `port` , `dbname` , and `credentials` , as shown in the following table. For more information about PHP APIs, see PHP documentation. ApsaraDB RDS for PolarDB User ApsaraDB for RDS

## Compatibility for Oracle

In this topic, examples are used to help you understand terms and concepts in PolarDB, so that you can smoothly migrate data from Oracle to PolarDB databases and efficiently use the databases for development. The operations described in this topic are based on a model that demonstrates the basic PolarDB operations, such as database creation, table creation, and user management. The following figure shows the data model: To simulate an environment similar to Oracle, the following example creates a database named orcl_polardb, a role named scott in the orcl_polardb database, and a schema named scott.

**Use psql to connect to a database**

```
 psql -h polardbaddress.polardb.rds.aliyuncs.com -p 3433 -U myuser -d template1
```

**CREATE DATABASE**

Create a database named `orcl_polardb` :

```
CREATE DATABASE orcl_polardb;
```

Connect to the `orcl_polardb` database:

```
\c orcl_polardb
```

**CREATE ROLE**

```
CREATE ROLE scott LOGIN PASSWORD 'scott123';
```

|  |  | Note If scott is not added to the myuser role before you execute ALTER SCHEMA scott OWNER TO scott , the following permission error is displayed: ERROR:must be member of role "scott" For security reasons, remove scott from the myuser user after the statement is executed. This improves security. |
|---|---|---|
|  |  | OWNER TO scott |

| ALTER SCHEMA scott |  |  |
|---|---|---|
|  | ERROR:must be member |  |

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**CREATE SCHEMA**

Create a schema:

```
CREATE SCHEMA scott;
```

Add scott to the myuser role:

```
GRANT scott TO myuser;
```

Change the owner of the schema:

```
ALTER SCHEMA scott OWNER TO scott;
```

Remove scott from the myuser role:

```
REVOKE scott FROM myuser;
```

**Connect to the orcl_polardb database**

**Note**

The following operations must be performed by using the scott account. Otherwise, the created tables and objects do not belong to scott and permission errors may occur.

```
./psql -h polardbaddress.polardb.rds.aliyuncs.com -p 3433 -U scott -d orcl_polardb
```

**CREATE TABLE**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
CREATE TABLE dept (
   deptno          NUMBER(2) NOT NULL CONSTRAINT dept_pk PRIMARY KEY,
   dname           VARCHAR2(14) CONSTRAINT dept_dname_uq UNIQUE,
   lock            VARCHAR2(13)
); CREATE TABLE emp (
  empno           NUMBER(4) NOT NULL CONSTRAINT emp_pk PRIMARY KEY,
  ename           VARCHAR2(10),
  job             VARCHAR2(9),
  mgr             NUMBER(4),
  hiredate        DATE,
  sal             NUMBER(7,2) CONSTRAINT emp_sal_ck CHECK (sal > 0),
  comm            NUMBER(7,2),
  deptno          NUMBER(2) CONSTRAINT emp_ref_dept_fk
                  REFERENCES dept(deptno)
); CREATE TABLE jobhist (
  empno           NUMBER(4) NOT NULL,
  startdate       DATE NOT NULL,
  enddate         DATE,
  job             VARCHAR2(9),
  sal             NUMBER(7,2),
  comm            NUMBER(7,2),
  deptno          NUMBER(2),
  chgdesc         VARCHAR2(80),
  CONSTRAINT jobhist_pk PRIMARY KEY (empno, startdate),
  CONSTRAINT jobhist_ref_emp_fk FOREIGN KEY (empno)
      REFERENCES emp(empno) ON DELETE CASCADE,
  CONSTRAINT jobhist_ref_dept_fk FOREIGN KEY (deptno)
      REFERENCES dept (deptno) ON DELETE SET NULL,
  CONSTRAINT jobhist_date_chk CHECK (startdate <= enddate)
);
```

**CREATE OR REPLACE VIEW**

```
CREATE OR REPLACE VIEW salesemp AS
   SELECT empno, ename, hiredate, sal, comm FROM emp WHERE job = 'SALESMAN';
```

**CREATE SEQUENCE**

```
CREATE SEQUENCE next_empno START WITH 8000 INCREMENT BY 1;
```

**INSERT INTO**

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK'); INSERT INTO dept VALUES (20,'RESEARCH','DALLAS'); INSERT INTO dept VALUES (30,'SALES','CHICAGO'); INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON'); INSERT INTO emp VALUES (7369,'SMITH','CLERK',7902,'17-DEC-80',800,NULL,20); INSERT INTO emp VALUES (7499,'ALLEN','SALESMAN',7698,'20-FEB-81',1600,300,30); INSERT INTO emp VALUES (7521,'WARD','SALESMAN',7698,'22-FEB-81',1250,500,30); INSERT INTO emp VALUES (7566,'JONES','MANAGER',7839,'02-APR-81',2975,NULL,20); INSERT INTO emp VALUES (7654,'MARTIN','SALESMAN',7698,'28-SEP-81',1250,1400,30); INSERT INTO emp VALUES (7698,'BLAKE','MANAGER',7839,'01-MAY-81',2850,NULL,30); INSERT INTO emp VALUES (7782,'CLARK','MANAGER',7839,'09-JUN-81',2450,NULL,10); INSERT INTO emp VALUES (7788,'SCOTT','ANALYST',7566,'19-APR-87',3000,NULL,20); INSERT INTO emp VALUES (7839,'KING','PRESIDENT',NULL,'17-NOV-81',5000,NULL,10); INSERT INTO emp VALUES (7844,'TURNER','SALESMAN',7698,'08-SEP-81',1500,0,30); INSERT INTO emp VALUES (7876,'ADAMS','CLERK',7788,'23-MAY-87',1100,NULL,20); INSERT INTO emp VALUES (7900,'JAMES','CLERK',7698,'03-DEC-81',950,NULL,30); INSERT INTO emp VALUES (7902,'FORD','ANALYST',7566,'03-DEC-81',3000,NULL,20); INSERT INTO emp VALUES (7934,'MILLER','CLERK',7782,'23-JAN-82',1300,NULL,10); INSERT INTO jobhist VALUES (7369,'17-DEC-80',NULL,'CLERK',800,NULL,20,'New Hire'); INSERT INTO jobhist VALUES (7499,'20-FEB-81',NULL,'SALESMAN',1600,300,30,'New Hire'); INSERT INTO jobhist VALUES (7521,'22-FEB-81',NULL,'SALESMAN',1250,500,30,'New Hire'); INSERT INTO jobhist VALUES (7566,'02-APR-81',NULL,'MANAGER',2975,NULL,20,'New Hire'); INSERT INTO jobhist VALUES (7654,'28-SEP-81',NULL,'SALESMAN',1250,1400,30,'New Hire'); INSERT INTO jobhist VALUES (7698,'01-MAY-81',NULL,'MANAGER',2850,NULL,30,'New Hire'); INSERT INTO jobhist VALUES (7782,'09-JUN-81',NULL,'MANAGER',2450,NULL,10,'New Hire'); INSERT INTO jobhist VALUES (7788,'19-APR-87','12-APR-88','CLERK',1000,NULL,20,'New Hire '); INSERT INTO jobhist VALUES (7788,'13-APR-88','04-MAY-89','CLERK',1040,NULL,20,'Raise'); INSERT INTO jobhist VALUES (7788,'05-MAY-90',NULL,'ANALYST',3000,NULL,20,'Promoted to A nalyst'); INSERT INTO jobhist VALUES (7839,'17-NOV-81',NULL,'PRESIDENT',5000,NULL,10,'New Hire'); INSERT INTO jobhist VALUES (7844,'08-SEP-81',NULL,'SALESMAN',1500,0,30,'New Hire'); INSERT INTO jobhist VALUES (7876,'23-MAY-87',NULL,'CLERK',1100,NULL,20,'New Hire'); INSERT INTO jobhist VALUES (7900,'03-DEC-81','14-JAN-83','CLERK',950,NULL,10,'New Hire' ); INSERT INTO jobhist VALUES (7900,'15-JAN-83',NULL,'CLERK',950,NULL,30,'Changed to Dept 30'); INSERT INTO jobhist VALUES (7902,'03-DEC-81',NULL,'ANALYST',3000,NULL,20,'New Hire'); INSERT INTO jobhist VALUES (7934,'23-JAN-82',NULL,'CLERK',1300,NULL,10,'New Hire');
```

**ANALYZE**

```
ANALYZE dept; ANALYZE emp; ANALYZE jobhist;
```

`IS`

```
  v_empno         NUMBER(4);
  v_ename         VARCHAR2(10);
CURSORempcurIS
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
  CURSOR emp_cur IS
      SELECT empno, ename FROM emp ORDER BY empno;
BEGIN
  OPEN emp_cur;
  DBMS_OUTPUT.PUT_LINE('EMPNO    ENAME');
  DBMS_OUTPUT.PUT_LINE('-----    -------');
  LOOP
      FETCH emp_cur INTO v_empno, v_ename;
      EXIT WHEN emp_cur%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE(v_empno || '     ' || v_ename);
  END LOOP;
  CLOSE emp_cur;
END;
```

`--`

```
-- Procedure that selects an employee row given the employee -- number and displays certain columns.
```

`--`

```
  p_empno         IN  NUMBER
```

) `IS`

```
  v_ename         emp.ename%TYPE;
  v_hiredate      emp.hiredate%TYPE;
  v_sal           emp.sal%TYPE;
  v_comm          emp.comm%TYPE;
  v_dname         dept.dname%TYPE;
  v_disp_date     VARCHAR2(10);
BEGIN
  SELECT ename, hiredate, sal, NVL(comm, 0), dname
      INTO v_ename, v_hiredate, v_sal, v_comm, v_dname
      FROM emp e, dept d
      WHERE empno = p_empno
        AND e.deptno = d.deptno;
  v_disp_date := TO_CHAR(v_hiredate, 'MM/DD/YYYY');
  DBMS_OUTPUT.PUT_LINE('Number    : ' || p_empno);
  DBMS_OUTPUT.PUT_LINE('Name      : ' || v_ename);
  DBMS_OUTPUT.PUT_LINE('Hire Date : ' || v_disp_date);
  DBMS_OUTPUT.PUT_LINE('Salary    : ' || v_sal);
  DBMS_OUTPUT.PUT_LINE('Commission: ' || v_comm);
  DBMS_OUTPUT.PUT_LINE('Department: ' || v_dname);
EXCEPTION
  WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('Employee ' || p_empno || ' not found');
  WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('The following is SQLERRM:');
      DBMS_OUTPUT.PUT_LINE(SQLERRM);
      DBMS_OUTPUT.PUT_LINE('The following is SQLCODE:');
      DBMS_OUTPUT.PUT_LINE(SQLCODE);
END;
```

`--`

```
-- department number and employee number or name. Returns -- employee number and name as IN OUT parameters and job, -- hire date, and salary as OUT parameters.
```

`--` ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  p_deptno        IN     NUMBER,
  p_empno         IN OUT NUMBER,
  p_ename         IN OUT VARCHAR2,
  p_job           OUT    VARCHAR2,
  p_hiredate      OUT    DATE
  p_sal           OUT    NUMBER
```

) `IS`

```
BEGIN
  SELECT empno, ename, job, hiredate, sal
      INTO p_empno, p_ename, p_job, p_hiredate, p_sal
      FROM emp
      WHERE deptno = p_deptno
        AND (empno = p_empno
         OR  ename = UPPER(p_ename));
END;
```

`--`

```
-- Procedure to call 'emp_query_caller' with IN and IN OUT -- parameters. Displays the results received from IN OUT and -- OUT parameters.
```

`--` `IS`

```
  v_deptno        NUMBER(2);
  v_empno         NUMBER(4);
  v_ename         VARCHAR2(10);
  v_job           VARCHAR2(9);
  v_hiredate      DATE;
  v_sal           NUMBER;
BEGIN
  v_deptno := 30;
  v_empno  := 0;
  v_ename  := 'Martin';
  emp_query(v_deptno, v_empno, v_ename, v_job, v_hiredate, v_sal);
  DBMS_OUTPUT.PUT_LINE('Department : ' || v_deptno);
  DBMS_OUTPUT.PUT_LINE('Employee No: ' || v_empno);
  DBMS_OUTPUT.PUT_LINE('Name       : ' || v_ename);
  DBMS_OUTPUT.PUT_LINE('Job        : ' || v_job);
  DBMS_OUTPUT.PUT_LINE('Hire Date  : ' || v_hiredate);
  DBMS_OUTPUT.PUT_LINE('Salary     : ' || v_sal);
EXCEPTION
  WHEN TOO_MANY_ROWS THEN
      DBMS_OUTPUT.PUT_LINE('More than one employee was selected');
  WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('No employees were selected');
END;
```

**CREATE FUNCTION**

```
CREATE OR REPLACE FUNCTION emp_comp (
  p_sal           NUMBER,
  p_comm          NUMBER
)RETURNNUMBER
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
) RETURN NUMBER
```

`IS`

```
BEGIN
  RETURN (p_sal + NVL(p_comm, 0)) * 24;
END;
```

`--`

```
-- Function that gets the next number from sequence, 'next_empno', -- and ensures it is not already in use as an employee number.
```

`--`

```
CREATE OR REPLACE FUNCTION new_empno RETURN NUMBER
```

`IS`

```
  v_cnt           INTEGER := 1;
  v_new_empno     NUMBER;
BEGIN
  WHILE v_cnt > 0 LOOP
      SELECT next_empno.nextval INTO v_new_empno FROM dual;
      SELECT COUNT(*) INTO v_cnt FROM emp WHERE empno = v_new_empno;
  END LOOP;
  RETURN v_new_empno;
END;
```

`--`

```
-- EDB-SPL function that adds a new clerk to table 'emp'. This function -- uses package 'emp_admin'.
```

`--`

```
CREATE OR REPLACE FUNCTION hire_clerk (
  p_ename         VARCHAR2,
  p_deptno        NUMBER
) RETURN NUMBER
```

`IS`

```
  v_empno         NUMBER(4);
  v_ename         VARCHAR2(10);
  v_job           VARCHAR2(9);
  v_mgr           NUMBER(4);
  v_hiredate      DATE;
  v_sal           NUMBER(7,2);
  v_comm          NUMBER(7,2);
  v_deptno        NUMBER(2);
BEGIN
  v_empno := new_empno;
  INSERT INTO emp VALUES (v_empno, p_ename, 'CLERK', 7782,
      TRUNC(SYSDATE), 950.00, NULL, p_deptno);
  SELECT empno, ename, job, mgr, hiredate, sal, comm, deptno INTO
      v_empno, v_ename, v_job, v_mgr, v_hiredate, v_sal, v_comm, v_deptno
      FROM emp WHERE empno = v_empno;
  DBMS_OUTPUT.PUT_LINE('Department : ' || v_deptno);
  DBMS_OUTPUT.PUT_LINE('Employee No: ' || v_empno);
  DBMS_OUTPUT.PUT_LINE('Name       : ' || v_ename);
  DBMS_OUTPUT.PUT_LINE('Job        : ' || v_job);
  DBMS_OUTPUT.PUT_LINE('Manager    : ' || v_mgr);
  DBMS_OUTPUT.PUT_LINE('Hire Date  : ' || v_hiredate);
  DBMS_OUTPUT.PUT_LINE('Salary     : ' || v_sal);
  DBMS_OUTPUT.PUT_LINE('Commission : ' || v_comm);
  RETURN v_empno;
EXCEPTION WHENOTHERSTHEN
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
  WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('The following is SQLERRM:');
      DBMS_OUTPUT.PUT_LINE(SQLERRM);
      DBMS_OUTPUT.PUT_LINE('The following is SQLCODE:');
      DBMS_OUTPUT.PUT_LINE(SQLCODE);
      RETURN -1;
END;
```

`--`

```
-- PostgreSQL PL/pgSQL function that adds a new salesman -- to table 'emp'.
```

`--`

```
CREATE OR REPLACE FUNCTION hire_salesman (
  p_ename         VARCHAR,
  p_sal           NUMERIC,
  p_comm          NUMERIC
) RETURNS NUMERIC AS $$ DECLARE
  v_empno         NUMERIC(4);
  v_ename         VARCHAR(10);
  v_job           VARCHAR(9);
  v_mgr           NUMERIC(4);
  v_hiredate      DATE;
  v_sal           NUMERIC(7,2);
  v_comm          NUMERIC(7,2);
  v_deptno        NUMERIC(2);
BEGIN
  v_empno := new_empno();
  INSERT INTO emp VALUES (v_empno, p_ename, 'SALESMAN', 7698,
      CURRENT_DATE, p_sal, p_comm, 30);
  SELECT INTO
      v_empno, v_ename, v_job, v_mgr, v_hiredate, v_sal, v_comm, v_deptno
      empno, ename, job, mgr, hiredate, sal, comm, deptno
      FROM emp WHERE empno = v_empno;
  RAISE INFO 'Department : %', v_deptno;
  RAISE INFO 'Employee No: %', v_empno;
  RAISE INFO 'Name       : %', v_ename;
  RAISE INFO 'Job        : %', v_job;
  RAISE INFO 'Manager    : %', v_mgr;
  RAISE INFO 'Hire Date  : %', v_hiredate;
  RAISE INFO 'Salary     : %', v_sal;
  RAISE INFO 'Commission : %', v_comm;
  RETURN v_empno;
EXCEPTION
  WHEN OTHERS THEN
      RAISE INFO 'The following is SQLERRM:';
      RAISE INFO '%', SQLERRM;
      RAISE INFO 'The following is SQLSTATE:';
      RAISE INFO '%', SQLSTATE;
      RETURN -1;
END;
```

**CREATE RULE**

ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
CREATE OR REPLACE RULE salesemp_i AS ON INSERT TO salesemp DO INSTEAD
  INSERT INTO emp VALUES (NEW.empno, NEW.ename, 'SALESMAN', 7698,
      NEW.hiredate, NEW.sal, NEW.comm, 30);
CREATE OR REPLACE RULE salesemp_u AS ON UPDATE TO salesemp DO INSTEAD
  UPDATE emp SET empno    = NEW.empno,
                 ename    = NEW.ename,
                 hiredate = NEW.hiredate,
                 sal      = NEW.sal,
                 comm     = NEW.comm
      WHERE empno = OLD.empno;
CREATE OR REPLACE RULE salesemp_d AS ON DELETE TO salesemp DO INSTEAD DELETE FROM emp WHERE empno = OLD.empno;
```

**CREATE TRIGGER**

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

```
CREATE OR REPLACE TRIGGER user_audit_trig
  AFTER INSERT OR UPDATE OR DELETE ON emp
DECLARE
  v_action        VARCHAR2(24);
BEGIN
  IF INSERTING THEN
      v_action := ' added employee(s) on ';
  ELSIF UPDATING THEN
      v_action := ' updated employee(s) on ';
  ELSIF DELETING THEN
      v_action := ' deleted employee(s) on ';
  END IF;
  DBMS_OUTPUT.PUT_LINE('User ' || USER || v_action || TO_CHAR(SYSDATE,'YYYY-MM-DD'));
END; CREATE OR REPLACE TRIGGER emp_sal_trig
  BEFORE DELETE OR INSERT OR UPDATE ON emp
  FOR EACH ROW
DECLARE
  sal_diff       NUMBER;
BEGIN
  IF INSERTING THEN
      DBMS_OUTPUT.PUT_LINE('Inserting employee ' || :NEW.empno);
      DBMS_OUTPUT.PUT_LINE('..New salary: ' || :NEW.sal);
  END IF;
  IF UPDATING THEN
      sal_diff := :NEW.sal - :OLD.sal;
      DBMS_OUTPUT.PUT_LINE('Updating employee ' || :OLD.empno);
      DBMS_OUTPUT.PUT_LINE('..Old salary: ' || :OLD.sal);
      DBMS_OUTPUT.PUT_LINE('..New salary: ' || :NEW.sal);
      DBMS_OUTPUT.PUT_LINE('..Raise     : ' || sal_diff);
  END IF;
  IF DELETING THEN
      DBMS_OUTPUT.PUT_LINE('Deleting employee ' || :OLD.empno);
      DBMS_OUTPUT.PUT_LINE('..Old salary: ' || :OLD.sal);
  END IF;
END;
```

**BEFORE row-level triggers in partitioned tables**

When you update data across partitions, PostgreSQL and Oracle use different trigger behaviors. PostgreSQL: The triggers of multiple partition tables are run. Oracle: The relevant triggers are run only once. By default, PolarDB for PostgreSQL (Compatible with Oracle) is compatible with the trigger behavior of Oracle.

**Note**

Statement-level triggers are used in the same way as standard tables. Setting `polar_compatible_oracle_trigger` to off indicates that PolarDB for PostgreSQL (Compatible with Oracle) uses the trigger behavior of PostgreSQL. The triggers of multiple partition tables are run.

```
SET polar_compatible_oracle_trigger = off;
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS Example:

```
create trigger t before insert or update or delete on parted
  for each row execute function trigger_function();
insert into parted values (1, 1, 'uno uno v1'); NOTICE: parted_1: BEFORE ROW INSERT update parted set a = 2; NOTICE: parted_1: BEFORE ROW UPDATE NOTICE: parted_1: BEFORE ROW DELETE NOTICE: parted_2: BEFORE ROW INSERT delete from parted; NOTICE: parted_2: BEFORE ROW DELETE
```

Setting `polar_compatible_oracle_trigger` to on indicates that PolarDB for PostgreSQL (Compatible with Oracle) uses the trigger behavior of Oracle. The relevant triggers are run only once.

```
SET polar_compatible_oracle_trigger = on;
```

Example:

```
insert into parted values (1, 1, 'uno uno v1'); NOTICE: parted_1: BEFORE ROW INSERT update parted set a = 2; NOTICE: parted_1: BEFORE ROW UPDATE delete from parted; NOTICE: parted_2: BEFORE ROW DELETE
```

**CREATE PACKAGE**

```
CREATE OR REPLACE PACKAGE emp_admin
```

`IS`

```
  FUNCTION get_dept_name (
      p_deptno        NUMBER
  ) RETURN VARCHAR2;
  FUNCTION update_emp_sal (
      p_empno         NUMBER,
      p_raise         NUMBER
  ) RETURN NUMBER;
      p_empno         NUMBER,
      p_ename         VARCHAR2,
      p_job           VARCHAR2,
      p_sal           NUMBER,
      p_hiredate      DATE,
      p_comm          NUMBER,
      p_mgr           NUMBER,
      p_deptno        NUMBER
  );
      p_empno         NUMBER
  );
END emp_admin;
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

**CREATE PACKAGE BODY**

`--`

```
-- Package body for the 'emp_admin' package.
```

`--`

```
CREATE OR REPLACE PACKAGE BODY emp_admin
```

`IS` `--`

```
  --  Function that queries the 'dept' table based on the department
  --  number and returns the corresponding department name.
```

`--`

```
  FUNCTION get_dept_name (
      p_deptno        IN NUMBER
  ) RETURN VARCHAR2
```

`IS`

```
      v_dname         VARCHAR2(14);
  BEGIN
      SELECT dname INTO v_dname FROM dept WHERE deptno = p_deptno;
      RETURN v_dname;
  EXCEPTION
      WHEN NO_DATA_FOUND THEN
          DBMS_OUTPUT.PUT_LINE('Invalid department number ' || p_deptno);
          RETURN '';
  END;
```

`--`

```
  --  Function that updates an employee's salary based on the
  --  employee number and salary increment/decrement passed
  --  as IN parameters.  Upon successful completion the function
  --  returns the new updated salary.
```

`--`

```
  FUNCTION update_emp_sal (
      p_empno         IN NUMBER,
      p_raise         IN NUMBER
  ) RETURN NUMBER
```

`IS`

```
      v_sal           NUMBER := 0;
  BEGIN
      SELECT sal INTO v_sal FROM emp WHERE empno = p_empno;
      v_sal := v_sal + p_raise;
      UPDATE emp SET sal = v_sal WHERE empno = p_empno;
      RETURN v_sal;
  EXCEPTION
      WHEN NO_DATA_FOUND THEN
          DBMS_OUTPUT.PUT_LINE('Employee ' || p_empno || ' not found');
          RETURN -1;
      WHEN OTHERS THEN
          DBMS_OUTPUT.PUT_LINE('The following is SQLERRM:');
          DBMS_OUTPUT.PUT_LINE(SQLERRM);
          DBMS_OUTPUT.PUT_LINE('The following is SQLCODE:');
          DBMS_OUTPUT.PUT_LINE(SQLCODE);
          RETURN -1;
  END;
```

`--`

```
  --  Procedure that inserts a new employee record into the 'emp' table.
```

ApsaraDB RDS for PolarDB User ApsaraDB for RDS `--`

```
      p_empno         NUMBER,
      p_ename         VARCHAR2,
      p_job           VARCHAR2,
      p_sal           NUMBER,
      p_hiredate      DATE,
      p_comm          NUMBER,
      p_mgr           NUMBER,
      p_deptno        NUMBER
```

) `AS`

```
  BEGIN
      INSERT INTO emp(empno, ename, job, sal, hiredate, comm, mgr, deptno)
          VALUES(p_empno, p_ename, p_job, p_sal,
                 p_hiredate, p_comm, p_mgr, p_deptno);
  END;
```

`--`

```
  --  Procedure that deletes an employee record from the 'emp' table based
  --  on the employee number.
```

`--`

```
      p_empno         NUMBER
```

) `AS`

```
  BEGIN
      DELETE FROM emp WHERE empno = p_empno;
  END;
END;
```

ApsaraDB for RDS ApsaraDB RDS for PolarDB User

## Management functions

You cannot use superuser accounts to manage database objects of PolarDB. Therefore, PolarDB provides management functions to help you use the various features. This topic describes how to use the management functions. You must use the root account of PolarDB to run management functions. The root account is a management account specified when an instance is created and has the CREATEDB, CREATEROLE, and LOGIN permissions. rds_manage_extension This function allows you to manage plug-ins. You can use this function to create and delete plug-ins supported by PolarDB. ApsaraDB RDS for PolarDB User ApsaraDB for RDS

```
rds_manage_extension(operation text, pname text, schema text default NULL,logging boo l default false)
  operation: The parameter value is create or drop.
  pname: the name of the supported plug-in.
  schema: the target plug-in mode.
  logging: the log information when the plug-in is created.
  The following plug-ins are supported:
  pg_stat_statements
  btree_gin
  btree_gist
  chkpass
  citext
  cube
  dblink
  dict_int
  earthdistance
  hstore
  intagg
  intarray
  isn
  ltree
  pgcrypto
  pgrowlocks
  pg_prewarm
  pg_trgm
  postgres_fdw
  sslinfo
  tablefunc
  tsearch2
  unaccent
  postgis
  postgis_topology
  fuzzystrmatch
  postgis_tiger_geocoder
  plperl
  pltcl
  plv8
  "uuid-ossp"
  plpgsql
  oss_fdw
  Examples:
  1. Create the dblink plug-in.
      select rds_manage_extension('create','dblink');
  2. Delete the dblink plug-in.
      select rds_manage_extension('drop','dblink');
```

rds_pg_stat_activity() This function returns the information of all connected sessions, which is similar to the pg_stat_activity view. rds_pg_stat_statements() This function encapsulates the pg_stat_statements view. You can use this function to view slow SQL statements within your permissions. ApsaraDB for RDS ApsaraDB RDS for PolarDB User Performance analysis functions The functions allow you to analyze the real-time performance of PolarDB instances and are similar to Automatic Workload Repository (AWR) of Oracle.

```
  1. rds_truncsnap()
  Description: The function is used to delete stored snapshots.
  2 rds_get_snaps()
  Description: The function is used to obtain the information of stored snapshots.
  3 rds_snap()
  Description: The function is used to generate a real-time snapshot.
  4 rds_report(beginsnap bigint, endsnap bigint)
  Description: The function is used to generate a performance analysis report based o
n snapshots that you specify.
  Example: The following statements generate a performance analysis report based on s
napshots.
  SELECT * FROM rds_truncsnap(); // Delete stored snapshots.
  SELECT * from rds_snap(); // Generate a snapshot.
  SELECT * from rds_snap(); // Generate a snapshot.
  SELECT * from rds_snap(); // Generate a snapshot.
  SELECT * FROM rds_get_snaps(); // Obtain the IDs of the generated snapshots, which
are 1, 2, and 3.
  SELECT * FROM edbreport(1, 3); // Generate a performance analysis report based on t
he snapshot 1 and snapshot 3.
```

Session termination functions

```
 rds_pg_terminate_backend(upid int)
  rds_pg_cancel_backend(upid int)
  The functions are similar to the native pg_terminate_backend and pg_cancel_backend
functions. The functions provided by PolarDB cannot manage sessions established by th e superuser account.
  Example: The following statement terminates session 123456.
  select rds_pg_cancel_backend(123456);
```

VPD functions Virtual Private Database (VPD) is an encapsulation that is compatible with the DBMS_RLS package and uses the same parameters as DBMS_RLS uses.

```
1. rds_drop_policy is similar to DBMS_RLS.DROP_POLICY.
  2. rds_enable_policy is similar to DBMS_RLS.ENABLE_POLICY.
  3. rds_add_policy is similar to DBMS_RLS.ADD_POLICY.
```

For more information about VPD functions, see Using Oracle Virtual Private Database to Control Data Access.
