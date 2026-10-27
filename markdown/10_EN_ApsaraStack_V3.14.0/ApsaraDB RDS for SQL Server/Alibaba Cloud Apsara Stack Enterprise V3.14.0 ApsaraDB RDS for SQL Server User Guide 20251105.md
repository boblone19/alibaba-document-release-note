---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB RDS for SQL Server User Guide 20251105"
product_version: "V3.14.0"
doc_version: "20251105"
pdf_pages: 48
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB RDS for SQL Server User Guide 20251105.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.14.0/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20RDS%20for%20SQL%20Server%20User%20Guide%2020251105.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB RDS for SQL Server User Guide 20251105

## Table of Contents

- 1 ApsaraDB RDS for SQL Server Product Lifecycle Announcement
- 2 What is ApsaraDB RDS?
- 3 Log on to the ApsaraDB RDS console
- 4 Quick Start
  - 4.1 Procedure
  - 4.2 Create an instance
  - 4.3 Configure an IP address whitelist
  - 4.4 Connect to an instance
  - 4.5 Create an account
  - 4.6 Create a database
- 5 Instances
  - 5.1 Create an instance
  - 5.2 View basic information of an instance
  - 5.3 Restart an instance
  - 5.4 Change the specifications of an instance
  - 5.5 Set a maintenance window
  - 5.6 Configure primary/secondary switchover
  - 5.7 Release an instance
  - 5.8 Read-only instances
    - 5.8.1 Overview of read-only ApsaraDB RDS for SQL Server instances
    - 5.8.2 Create a read-only ApsaraDB RDS for SQL Server instance
    - 5.8.3 View details of read-only instances
- 6 Accounts
  - 6.1 Create an account
  - 6.2 Reset the password
- 7 Databases
  - 7.1 Create a database
  - 7.2 Delete a database
  - 7.3 Change the character set collation and the time zone of system databases
- 8 Database connection
  - 8.1 Change the endpoint and port number of an instance
  - 8.2 Connect to an instance
- 9 Monitoring and alerting
  - 9.1 Set a monitoring frequency
  - 9.2 View resource and engine monitoring data
- 10 Data security
  - 10.1 Configure an IP address whitelist
  - 10.2 Configure SSL encryption
- 11 Database backup and restoration
  - 11.1 Configure an automatic backup policy
  - 11.2 Manually back up an instance
  - 11.3 Shrink transaction logs
- 12 Migrate full backup data to ApsaraDB RDS for SQL Server

erver Product Lifecycle Announce ment

## 1 ApsaraDB RDS for SQL Server Product Lifecycle Announcement

**Server Product Lifecycle**

**Announcement**

Dear Customer, Apsara Stack ApsaraDB for SQL Server will reach its End of Marketing (EOM) on April 30, 2024. This notice describes the product lifecycle milestones and the replacement solution to support your business innovation and business continuity planning.

| Product Name | Milestone | Description | Date | Replaceme nt Product |
|---|---|---|---|---|
| ApsaraDB for SQL Server | End of Marketing（E OM） | The product will no longer accept new orders or be available for sale. Support for scaling out existing instances will continue. | April 30, 2024 | Deploy a commercial version of SQL Server on an ECS instance |
|   | End of Full Support (EOFS) | New security patches and fault fixes will no longer be released for the product. Support for existing patches and known faults will continue. | July 08, 2025 |   |
|   | End of Service (EOS) | All services and technical support for the product will be discontinued. | July 08, 2026 |   |

Please plan accordingly. If you have any questions, contact Alibaba Cloud. April 2024

## 2 What is ApsaraDB RDS?

ApsaraDB RDS is a stable, reliable, and scalable online database service. Based on the distributed file system and high-performance storage, ApsaraDB RDS provides a set of solutions for disaster recovery, backup, restoration, monitoring, and migration. ApsaraDB RDS supports four database engines, which are MySQL, SQL Server, PolarDB, and PostgreSQL. You can create database instances based on these engines to meet your business requirements. This topic describes the SQL Server engine.

**ApsaraDB RDS for SQL Server**

ApsaraDB RDS for SQL Server provides strong support for a variety of enterprise applications under the high-availability architecture. ApsaraDB RDS for SQL Server can also restore data to a specific point in time, which reduces costs. ApsaraDB RDS for SQL Server provides basic features such as whitelist configuration, backup and restoration, data migration, and management for instances, accounts, and databases. RDS console

## 3 Log on to the ApsaraDB RDS console

**RDS console**

This topic describes how to log on to the ApsaraDB RDS console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key. RDS console

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global identity provider (IdP) is configured in third-party authentication. You can specify a name for the Authorized Login button.

If you need to click Continue multiple times or cannot find the entry to the Apsara Uni-manager Management Console because the browser certificate has expired or HTTPS authentication is enabled in your environment, you must install a valid certificate. Click **Browser certificate installation** in the upper-right corner to open the browser certificate installation guide.
2. Enter your username and password.

> **Note:** Obtain the username and password from an operations administrator.
> The first time you log in to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Log On**.
4. In the top navigation bar, choose **Products** > Database Services > **ApsaraDB RDS**.

## 4 Quick Start

### 4.1 Procedure

ApsaraDB RDS quick start covers the following topics: creating an ApsaraDB RDS instance, configuring an IP address whitelist, creating a database, creating an account, and connecting to the instance. The following figure shows the operations that you must perform before you use an ApsaraDB RDS instance. Figure 1. Quick start flowchart

### 4.2 Create an instance

This topic describes how to create an instance in the ApsaraDB RDS console. An Apsara Stack tenant account is created.
1. Log on to the ApsaraDB RDS console.
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

| Specificat ions |   |   |
|---|---|---|
|   | Database Engine | The database engine of the instance. Select SQLServer. |
|   | Engine Version | The version of the database engine. Valid values: 2012 ent ha: SQL Server 2012 EE _ _ 2012 std ha: SQL Server 2012 SE _ _ 2016 ent ha: SQL Server 2016 EE _ _ 2016 std ha: SQL Server 2016 SE _ _ 2017 ent ha: SQL Server 2017 EE _ _ |
|   | Edition | The edition of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Type | The storage type of the instance. The storage type is automatically set to cloud ssd. |
|   | Instance Type | The instance type of the instance. Memory size determines the maximum number of connections and the input/output operations per second (IOPS). The actual values are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The storage capacity of the instance, which includes the space to store data, system files, binlog files, and transaction files. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| Network | Network Type | The network type of the instance. ApsaraDB RDS instances support the following network types: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. |
|   | VPC | Select a VPC. Note When Network Type is set to VPC, you must specify this parameter. |
|   | vSwitch | Select a vSwitch. Note When Network Type is set to VPC, you must specify this parameter. |
|   | IP Address Whitelist | The IP addresses that are allowed to connect to the instance. |

4. Click **Submit**.

### 4.3 Configure an IP address whitelist

**whitelist**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are used for database access to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

> **Note:** If you want to connect an ECS instance to an ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type. Otherwise, the connection fails.
> You can also click **Create Whitelist** to create an IP address whitelist.

6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that you want to
allow to access your RDS instance and click **OK**. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.xx format can access your RDS instance. If you enter more than one IP address or CIDR block, separate them with commas (,). Do not add spaces preceding or following the commas. Example:

```
 192.168.0.1,172.16.213.9 .
```

If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

> **Note:** If you add a new IP address or CIDR block to the **default** whitelist, the default address 127.0.0.1 is deleted.

### 4.4 Connect to an instance

This topic describes how to use Data Management (DMS) to connect to an ApsaraDB RDS instance.

**Prerequisites**

A database is created. For more information, see Create a database. A database account is created. For more information, see Create an account.
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to DB** in the upper-right corner of the page.
5.
6. Click **Login**.

> **Note:** If you want the browser to remember the password, select **Remember** **password** and click **Login**.
> If you cannot connect to the instance, check the IP address whitelist settings. For more information, see Configure an IP address whitelist.

### 4.5 Create an account

This topic describes how to create an account on an ApsaraDB RDS for SQL Server instance.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. On the right side of the page, click **Create Account**.
6. Enter the information of the account that you want to create.

| Paramete r | Description |
|---|---|
| Database Account | Enter the name of the account. The name must be 2 to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a _ lowercase letter and end with a lowercase letter or digit. |
| Account Type | Privileged Account: You can select the Privileged Account option only if you create an account on your ApsaraDB RDS instance for the first time. Each ApsaraDB RDS instance can have only a single privileged account. The privileged account of an ApsaraDB RDS instance cannot be deleted. Standard Account: You can select the Standard Account option only after a privileged account is created on your ApsaraDB RDS instance. Each ApsaraDB RDS instance can have more than one standard account. You must manually grant permissions on databases to each standard account. |

| Authorize d Database s | Select the authorized databases of the account when the Standard Account type is selected. If no databases are created, you can leave this parameter empty. You can perform the following steps to grant permissions on more than one database to the account: i. In the Unauthorized Databases section, select the databases on which you want to grant permissions to the account. ii. Click Add to add the selected databases to the Authorized Databases section. iii. In the Authorized Databases section, specify the permissions that the account is granted on each authorized database. The permissions can be Read/Write, Read- only, or Owner. You can also click Set All to Read/Write, Set All to Read-only, or Set All to Owner to set the permissions of the account on all authorized databases. Note The account is authorized to create tables, delete tables, and modify schemas in a database only when it has the Owner permission on the database. The account has permissions on all databases and does not require authorization if you select the Privileged Account type. |
|---|---|
| Password | Enter the password of the account. The password must meet the following requirements: The password is 8 to 32 characters in length. The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + - = _ |
| Re-enter Password | Enter the password of the account again. |
| Descripti on | Enter a description that helps identify the account. The description can be up to 256 characters in length. |

7. Click **Create**.

### 4.6 Create a database

This topic describes how to create a database on an ApsaraDB RDS for SQL Server instance in the ApsaraDB RDS console.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
4. In the left-side navigation pane, click **Databases**.
5. In the upper-right corner of the page, click **Create Database**.
6. Configure the parameters for the database that you want to create.

| Paramete r | Description |
|---|---|
| Database Name | Enter the name of the database. The name must be 2 to 64 characters in length. It can contain lowercase letters, digits, underscores ( ), and hyphens (-). It must start _ with a lowercase letter and end with a lowercase letter or digit. |
| Supporte d Character Sets | Select the character set that is supported by the database. You can also selecta ll and then select a character set from the drop-down list that appears. |
| Descripti on | Enter a description of the database to facilitate subsequent management. The description can be up to 256 characters in length. |

7. Click **Create**.

## 5 Instances

### 5.1 Create an instance

This topic describes how to create an instance in the ApsaraDB RDS console.

**Prerequisites**

An Apsara Stack tenant account is created.

**Procedure**

1. Log on to the ApsaraDB RDS console.
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

| Specificat ions |   |   |
|---|---|---|
|   | Instance Name | The name of the instance. The name must be 2 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, and the following special characters: - : _ The name cannot start with http:// or https://. |
|   | Connectio n Type | The connection type of the instance. ApsaraDB RDS instances support the following connection types: Internet: ApsaraDB RDS instances of this connection type can be connected over the Internet. Internal Network: ApsaraDB RDS instances of this connection type can be connected over an internal network. Note The value of this parameter cannot be changed after the instance is created. Proceed with caution. |
|   | Database Engine | The database engine of the instance. Select SQLServer. |
|   | Engine Version | The version of the database engine. Valid values: 2012 ent ha: SQL Server 2012 EE _ _ 2012 std ha: SQL Server 2012 SE _ _ 2016 ent ha: SQL Server 2016 EE _ _ 2016 std ha: SQL Server 2016 SE _ _ 2017 ent ha: SQL Server 2017 EE _ _ |
|   | Edition | The edition of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Type | The storage type of the instance. The storage type is automatically set to cloud ssd. |
|   | Instance Type | The instance type of the instance. Memory size determines the maximum number of connections and the input/output operations per second (IOPS). The actual values are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Capacity | The storage capacity of the instance, which includes the space to store data, system files, binlog files, and transaction files. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Network Type | The network type of the instance. ApsaraDB RDS instances support the following network types: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service is blocked only by the security group or whitelist policy of the service. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. |

| saraDB RDS fo Guide·Instance |   |   |
|---|---|---|
| Network |   |   |
|   | VPC | Select a VPC. Note When Network Type is set to VPC, you must specify this parameter. |
|   | vSwitch | Select a vSwitch. Note When Network Type is set to VPC, you must specify this parameter. |
|   | IP Address Whitelist | The IP addresses that are allowed to connect to the instance. |

4. Click **Submit**.

### 5.2 View basic information of an instance

**instance**

This topic describes how to view the details of an ApsaraDB RDS instance, such as its basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. Use one of the following methods to go to the **Basic Information** page of an instance:
On the **Instances** page, click the ID of an instance to go to the **Basic Information** page. On the **Instances** page, click **Manage** in the **Actions** column corresponding to an instance to go to the **Basic Information** page.

### 5.3 Restart an instance

This topic describes how to manually restart an ApsaraDB RDS for MySQL instance. This applies if the number of connections exceeds a specific threshold or if an instance has performance issues.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. Click **Restart Instance** in the upper-right corner.

> **Note:** When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.

4. In the Restart Instance message, click **Confirm**.

### 5.4 Change the specifications of an instance

**an instance**

This topic describes how to change specifications such as the instance type and storage space if they do not meet the requirements of your application. When the specification changes take effect, a 30-second network interruption may occur. Business operations that involve databases, accounts, and networks are interrupted. We recommend that you change the specifications during off-peak hours or make sure that your applications are configured with automatic reconnection policies.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Configuration Information** section, click **Change Specifications**.
5. On the **Change Specifications** page, specify **Instance Type** and **Storage Capacity**.
6. After you configure the preceding parameters, click **Submit**.

### 5.5 Set a maintenance window

This topic describes how to set the maintenance window of an ApsaraDB RDS for SQL Server instance. The backend system performs maintenance on the ApsaraDB RDS instance during the maintenance window. This ensures the stability of the ApsaraDB RDS instance. The default maintenance window is from 02:00 (UTC+8) to 06:00 (UTC+8). We recommend that you set the maintenance window to off-peak hours of your business to avoid impacts on your business.

**Background information**

An instance enters the **Maintaining Instance** state before the maintenance window to ensure stability during the maintenance process. When the instance is in this state, access to data in the database and query operations such as performance monitoring are not affected. However, except for account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. During the maintenance window, one or two network interruptions may occur. Make sure that your applications are configured with automatic reconnection policies.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Configuration Information** section, click **Configure** to the right of **Maintenance**
**Window**.
5. Select a maintenance window and click **Save**.

> **Note:** The maintenance window is displayed in UTC+8.

### 5.6 Configure primary/secondary switchover

**switchover**

ApsaraDB RDS provides the primary/secondary switchover feature to ensure the high availability of databases. The primary/secondary switchover is performed when the primary instance becomes unavailable. You can also manually switch your business to the secondary instance.

**Prerequisites**

The instance is in the **Running** state.

**Background information**

An ApsaraDB RDS for SQL Server instance has a secondary instance. Data is synchronized in real time between the primary and secondary instances. You can access only the primary instance. The secondary instance serves only as a backup instance and does not allow external access. If the primary instance cannot be accessed, your business automatically switches over to the secondary instance. After the switchover, the primary instance becomes the secondary instance.

> **Important:** During a switchover, a network interruption may occur. Make sure that your applications are configured with automatic reconnection policies.
> During a switchover, a 1-minute data quality protection mechanism is enabled for data synchronization. If the primary and secondary database states are incorrect or if the latency for data synchronization exceeds 1 minute due to SQL Server errors, the HA system does not automatically perform the primary/secondary switchover. You must determine whether to perform the switchover.
> If an instance is intermittently unavailable due to excessive mirroring event waits, the switchover is not performed. The instance automatically becomes available again.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Service Availability**.
5. In the **Availability Information** section, click **Switch Primary/Secondary Instance**.
6. In the dialog box that appears, click **OK**.

**Result**

After the switchover is complete, the original primary instance becomes the secondary instance for the next primary/secondary switchover.

### 5.7 Release an instance

This topic describes how to manually release an instance.

**Background information**

Only instances in the running state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. Find the instance that you want to release and choose **More > Release Instance**.
3. In the **Release Instance** message, click **Confirm**.

### 5.8 Read-only instances

#### 5.8.1 Overview of read-only ApsaraDB RDS for SQL Server instances

**for SQL Server instances**

This topic provides an overview of read-only ApsaraDB RDS for SQL Server instances. If a large number of read requests overwhelm the primary instance, your business may be interrupted. In this case, you can create one or more read-only instances to offload read requests from the primary instance. This scales the read capability of your database system and increases the throughput of your application.

**Overview**

When a read-only instance is created, the data is replicated from the secondary instance. The data is consistent with that of the primary instance. Data updates of the primary instance are synchronized to all read-only instances.

> **Note:** Only ApsaraDB RDS instances that run SQL Server 2017 EE support read-only instances.
> Each read-only instance works in a single-node architecture, where no instances are provided as backups.

The following figure shows the topology of read-only instances.

**Features**

The specifications of a read-only instance can differ from the specifications of the primary instance, and can be changed at any time. We recommend that you select specifications of a read-only instance that are higher than or equal to those of the primary instance. If the specifications of a read-only instance are lower than those of the primary instance, the read-only instance may have high latency or workloads. Read-only instances do not require database or account maintenance, because their database and account information is synchronized with the primary instance. A read-only instance automatically replicates the IP address whitelists of the primary instance. However, the IP address whitelists for the read-only instance are independent of those of the primary instance. For information about how to modify the whitelists of a readonly instance, see Configure an IP address whitelist. You can monitor up to 20 system performance metrics, such as the disk capacity, input/output operations per second (IOPS), number of connections, CPU utilization, and network traffic.

**Limits**

You can create up to seven read-only instances. You cannot configure backup policies or manually create backups for read-only instances, because these are already configured or created on the primary instance. You cannot create a temporary instance by using a backup set or from a point in time. In addition, you cannot overwrite a read-only instance by using a backup set. After a read-only instance is created, you cannot use a data backup file to restore it in overwrite mode. You cannot migrate data to read-only RDS instances. You cannot create or delete databases on read-only instances. You cannot create or delete accounts, authorize accounts, or change the passwords of accounts on read-only instances.

**FAQ**

Can I manage the accounts created on the primary instance from its read-only instances? No, although accounts created on the primary instance are replicated to its read-only instances, you cannot manage the accounts on the read-only instances. The accounts have only read permissions on the read-only instances.

#### 5.8.2 Create a read-only ApsaraDB RDS for SQL Server instance

**SQL Server instance**

This topic describes how to create a read-only instance for your primary ApsaraDB RDS for SQL server instance. This allows your database system to process a large number of read requests and increases the throughput of your application. Each read-only ApsaraDB RDS instance is a replica of the primary instance. Data updates on the primary instance are synchronized to all the read-only instances.

**Prerequisites**

The primary instance runs SQL Server 2017 EE.

**Precautions**

You can create read-only instances for the primary ApsaraDB RDS instance. However, you cannot convert existing ApsaraDB RDS instances into read-only instances. While you create a read-only instance, the system replicates data from a secondary instance. Therefore, the operation of your primary instance is not interrupted. You can create up to seven read-only instances. For more information about read-only ApsaraDB RDS instances, see Overview of read-only ApsaraDB RDS for SQL Server instances.

**Create a read-only instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the **Distributed by Instance Role** section on the right side of the page, click **Create**
**Read-only Instance**.
5. Configure the following parameters and click **Submit**.

| Section | Parameter | Description |
|---|---|---|
| Region | Region | The region in which you want to create the instance. |
| Specifications | Database Engine | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Engine Version | The engine version of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Edition | Set the value to Read-only. |
|   | Instance Type | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time to facilitate flexible upgrade and downgrade. For more information, see Instance types in ApsaraDB RDS Product Information. Note To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type as the primary instance for read-only instances. |
|   | Storage Capacity | The storage space of the read-only instance. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type and storage space as the primary instance for the read-only instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
| Network Type | Network Type | The network type of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | VPC | Select a VPC if the network type is set to VPC. |
|   | vSwitch | Select a vSwitch if the network type is set to VPC. |

#### 5.8.3 View details of read-only instances

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances page or the read-only instance list of the primary instance. Read-only instances are managed in the same way as primary instances. The read-only instance management page shows the management operations that can be performed.

**View instance details by using a read-only instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click the ID of a read-only instance. The **Basic Information** page
appears. In the instance list, **Instance Role** of read-only instances is displayed as **Read-only**
**Instance**, as shown in View a read-only instance.
Figure 1. View a read-only instance

**View instance details by using the primary instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. On the **Basic Information** page, move the pointer over the number below **Read-only**
**Instance** in the **Distributed by Instance Role** section. The ID of the read-only instance is
displayed.
5. Click the ID of the read-only instance to go to the read-only instance management page.

## 6 Accounts

### 6.1 Create an account

This topic describes how to create an account on an ApsaraDB RDS for SQL Server instance.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Accounts**.
5. On the right side of the page, click **Create Account**.
6. Enter the information of the account that you want to create.

| Paramete r | Description |
|---|---|
| Database Account | Enter the name of the account. The name must be 2 to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It must start with a _ lowercase letter and end with a lowercase letter or digit. |
| Account Type | Privileged Account: You can select the Privileged Account option only if you create an account on your ApsaraDB RDS instance for the first time. Each ApsaraDB RDS instance can have only a single privileged account. The privileged account of an ApsaraDB RDS instance cannot be deleted. Standard Account: You can select the Standard Account option only after a privileged account is created on your ApsaraDB RDS instance. Each ApsaraDB RDS instance can have more than one standard account. You must manually grant permissions on databases to each standard account. |

| Authorize d Database s | Select the authorized databases of the account when the Standard Account type is selected. If no databases are created, you can leave this parameter empty. You can perform the following steps to grant permissions on more than one database to the account: i. In the Unauthorized Databases section, select the databases on which you want to grant permissions to the account. ii. Click Add to add the selected databases to the Authorized Databases section. iii. In the Authorized Databases section, specify the permissions that the account is granted on each authorized database. The permissions can be Read/Write, Read- only, or Owner. You can also click Set All to Read/Write, Set All to Read-only, or Set All to Owner to set the permissions of the account on all authorized databases. Note The account is authorized to create tables, delete tables, and modify schemas in a database only when it has the Owner permission on the database. The account has permissions on all databases and does not require authorization if you select the Privileged Account type. |
|---|---|
| Password | Enter the password of the account. The password must meet the following requirements: The password is 8 to 32 characters in length. The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + - = _ |
| Re-enter Password | Enter the password of the account again. |
| Descripti on | Enter a description that helps identify the account. The description can be up to 256 characters in length. |

7. Click **Create**.

### 6.2 Reset the password

You can use the ApsaraDB RDS console to reset the password of your database account.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Accounts**.
4. Find an account and click **Reset Password** in the Actions column.
5. In the dialog box that appears, enter and confirm the new password, and then click **OK**.

> **Note:** The password must meet the following requirements:
> The password must be 8 to 32 characters in length.
> The password must contain at least three of the following characters: uppercase letters, lowercase letters, digits, and special characters.
> Special characters include ! @ # $ % ^ & * ( ) _ + - =

## 7 Databases

### 7.1 Create a database

This topic describes how to create a database on an ApsaraDB RDS for SQL Server instance.

**Terms**

Instance: a virtualized database server on which you can create and manage more than one database. Database: a set of data that is stored in an organized manner and can be shared by a number of users. A database provides the minimal redundancy and is independent of applications. In simple words, a database is a data warehouse that is used to store data. Character set: a collection of letters, special characters, and encoding rules that are used in a database.

**Prerequisites**

An ApsaraDB RDS for SQL Server instance is created. For more information, see Create an instance.

**Procedure**

For more information, see Create a database.

### 7.2 Delete a database

This topic describes how to delete a database from an ApsaraDB RDS for SQL Server instance. You can delete a database by using the ApsaraDB RDS console or an SQL statement.

**Use the console to delete a database**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Databases**.
5. Find the database that you want to delete and click **Delete** in the **Actions** column.
6. In the message that appears, click **Confirm**.

**Execute an SQL statement to delete a database**

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

> **Note:** If you want the browser to remember the password, select **Remember** **password** and click **Login**.
> If you cannot connect to the instance, check the IP address whitelist settings. For more information, see Configure an IP address whitelist.

7. The **SQLConsole** page appears after you log on to the instance. Execute a statement in the
following format to delete a database:

```
drop database <database name>;
```

> **Note:** If the instance runs SQL Server 2012 or later on RDS High-availability Edition, you can also use the following stored procedure. This stored procedure deletes the specified database, removes the associated image, and closes the connection to the database.

```
EXEC sp_rds_drop_database 'database name'
```

8. Click **execute**.

### 7.3 Change the character set collation and the time zone of system databases

**collation and the time zone of**

**system databases**

This topic describes how to change the character set collation and the time zone of system databases. System databases include master, msdb, tempdb, and model.

**Prerequisites**

The instance runs SQL Server 2012, 2016, or 2017. No database other than system databases exists on the instance.

> **Note:** If you have just deleted databases from the instance, the deletion task may be pending in the secondary instance. Before you change the character set collation and the time zone, make sure that the primary and secondary instances do not contain databases.

**Precautions**

The default character set collation is Chinese_PRC_CI_AS. The default time zone is China Standard Time. You can view the available character set collations and time zones in the console. The instance is in the unavailable state during the change process. It takes about 1 minute to change the time zone, and 2 to 10 minutes to change the character set collation.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Databases**.
5. On the Databases page, click **Change Character Set Collation and Time Zone** .

> **Note:** If you fail to find this button on the page, make sure that the requirements in Prerequisites are met.

6. In the dialog box that appears, select **Time Zone**, **Character Set Collation**, or both of
them, and click **OK**.

**UTC offsets of time zones**

| Time zone | UTC offset | Description |
|---|---|---|
| Afghanistan Standard Time | (UTC+04:30) | Kabul |
| Alaskan Standard Time | (UTC-09:00) | Alaska |
| Arabian Standard Time | (UTC+04:00) | Abu Dhabi, Muscat |
| Atlantic Standard Time | (UTC-04:00) | Atlantic Time (Canada) |
| AUS Central Standard Time | (UTC+09:30) | Darwin |
| AUS Eastern Standard Time | (UTC+10:00) | Canberra, Melbourne, Sydney |
| Belarus Standard Time | (UTC+03:00) | Minsk |
| Canada Central Standard Time | (UTC-06:00) | Saskatchewan |
| Cape Verde Standard Time | (UTC-01:00) | Cabo Verde Is. |
| Cen. Australia Standard Time | (UTC+09:30) | Adelaide |
| Central America Standard Time | (UTC-06:00) | Central America |
| Central Asia Standard Time | (UTC+06:00) | Astana |
| Central Brazilian Standard Time | (UTC-04:00) | Cuiaba |
| Central Europe Standard Time | (UTC+01:00) | Belgrade, Bratislava, Budapest, Ljubljana, Prague |
| Central European Standard Time | (UTC+01:00) | Sarajevo, Skopje, Warsaw, Zagreb |
| Central Pacific Standard Time | (UTC+11:00) | Solomon Islands, New Caledonia |
| Central Standard Time | (UTC-06:00) | Central Time (US and Canada) |
| Central Standard Time (Mexico) | (UTC-06:00) | Guadalajara, Mexico City, Monterrey |
| China Standard Time | (UTC+08:00) | Beijing, Chongqing, Hong Kong, Urumqi |
| E. Africa Standard Time | (UTC+03:00) | Nairobi |
| E. Australia Standard Time | (UTC+10:00) | Brisbane |
| E. Europe Standard Time | (UTC+02:00) | Chisinau |
| E. South America Standard Time | (UTC-03:00) | Brasilia |
| Eastern Standard Time | (UTC-05:00) | Eastern Time (US and Canada) |
| Georgian Standard Time | (UTC+04:00) | Tbilisi |

| GMT Standard Time | (UTC) | Dublin, Edinburgh, Lisbon, London |
|---|---|---|
| Greenland Standard Time | (UTC-03:00) | Greenland |
| Greenwich Standard Time | (UTC) | Monrovia, Reykjavik |
| GTB Standard Time | (UTC+02:00) | Athens, Bucharest |
| Hawaiian Standard Time | (UTC-10:00) | Hawaii |
| India Standard Time | (UTC+05:30) | Chennai, Kolkata, Mumbai, New Delhi |
| Jordan Standard Time | (UTC+02:00) | Amman |
| Korea Standard Time | (UTC+09:00) | Seoul |
| Middle East Standard Time | (UTC+02:00) | Beirut |
| Mountain Standard Time | (UTC-07:00) | Mountain Time (US and Canada) |
| Mountain Standard Time (Mexico) | (UTC-07:00) | Chihuahua, La Paz, Mazatlan |
| US Mountain Standard Time | (UTC-07:00) | Arizona |
| New Zealand Standard Time | (UTC+12:00) | Auckland, Wellington |
| Newfoundland Standard Time | (UTC-03:30) | Newfoundland |
| Pacific SA Standard Time | (UTC-03:00) | Santiago |
| Pacific Standard Time | (UTC-08:00) | Pacific Time (US and Canada) |
| Pacific Standard Time (Mexico) | (UTC-08:00) | Baja California |
| Russian Standard Time | (UTC+03:00) | Moscow, St. Petersburg, Volgograd |
| SA Pacific Standard Time | (UTC-05:00) | Bogota, Lima, Quito, Rio Branco |
| SE Asia Standard Time | (UTC+07:00) | Bangkok, Hanoi, Jakarta |
| China Standard Time | (UTC+08:00) | Kuala Lumpur, Singapore |
| Tokyo Standard Time | (UTC+09:00) | Osaka, Sapporo, Tokyo |
| US Eastern Standard Time | (UTC-05:00) | Indiana (East) |
| UTC | UTC | Coordinated Universal Time |
| UTC-02 | (UTC-02:00) | Coordinated Universal Time-02 |
| UTC-08 | (UTC-08:00) | Coordinated Universal Time-08 |
| UTC-09 | (UTC-09:00) | Coordinated Universal Time-09 |

| UTC-11 | (UTC-11:00) | Coordinated Universal Time-11 |
|---|---|---|
| UTC+12 | (UTC+12:00) | Coordinated Universal Time+12 |
| W. Australia Standard Time | (UTC+08:00) | Perth |
| W. Central Africa Standard Time | (UTC+01:00) | West Central Africa |
| W. Europe Standard Time | (UTC+01:00) | Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna |

## 8 Database connection

### 8.1 Change the endpoint and port number of an instance

**number of an instance**

This topic describes how to view and change the endpoint and port number of an instance.

**View the endpoint and port number**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Connection**.
You can view **Internal Endpoint** and **Internal Port** of the instance on the **Database**
**Connection** page. If you apply for a public endpoint, you can also view **Public Endpoint**
and **Public Port**.

**Change the endpoint and port number**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Change Endpoint**.
5. In the **Change Endpoint** dialog box, select a connection type from the **Connection Type**
drop-down list.
6. Set **Endpoint** and **Port**, and click **OK**.

> **Note:** The prefix of an endpoint must be 8 to 64 characters in length and can contain only letters, digits, and hyphens (-). It must start with a lowercase letter.
> The port number must be a value within the range of 1000 to 65534.

### 8.2 Connect to an instance

This topic describes how to use Data Management (DMS) to connect to an ApsaraDB RDS instance.

**Prerequisites**

A database is created. For more information, see Create a database. A database account is created. For more information, see Create an account.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. Click **Log On to DB** in the upper-right corner of the page.
5.
6. Click **Login**.

> **Note:** If you want the browser to remember the password, select **Remember** **password** and click **Login**.
> If you cannot connect to the instance, check the IP address whitelist settings. For more information, see Configure an IP address whitelist.

## 9 Monitoring and alerting

### 9.1 Set a monitoring frequency

This topic describes how to set the monitoring frequency of an ApsaraDB RDS for SQL Server instance.

**Background information**

ApsaraDB RDS provides the following monitoring frequencies: Every 60 seconds Every 300 seconds

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.
5. On the **Resource Monitoring** tab, click **Set Monitoring Frequency**.
6. In the **Set Monitoring Frequency** dialog box, select the required monitoring frequency.
7. Click **OK**.

### 9.2 View resource and engine monitoring data

**monitoring data**

The ApsaraDB RDS console provides a variety of performance metrics to monitor the status of your instances.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Monitoring and Alerts**.
5. On the **Monitoring and Alerts** page, select **Resource Monitoring** or **Engine**
**Monitoring**, and select a time range to view the corresponding monitoring data. The
following table describes the metrics.

| Monitori ng type | Metric | Description |
|---|---|---|

| Resourc e Monitori ng | Disk Space (unit: MB) | The disk usage of the instance, which includes the following items: Instance Size Data Usage Log Size Temporary File Size Other System File Size |
|---|---|---|
|   | IOPS | The number of input/output operations per second (IOPS) for the instance. |
|   | Total Connections | The total number of current connections of the instance. |
|   | MSSQL Instance CPU Utilization (percentage in the operating system) | The CPU utilization of the instance. This includes the CPU utilization for the operating system. Unit: %. |
|   | SQLServer Average Input/Output Traffic | The inbound and outbound traffic of the instance per second. Unit: KB. |
| Engine Monitori ng | Average Transaction Frequency | The number of transactions processed per second. |
|   | Average QPS | The number of SQL statements executed per second. |
|   | Buffer Hit Ratio (%) | The read hit ratio of the buffer pool. |
|   | Page Write Frequency at Check Point | The number of checkpoints written to pages per second. |
|   | Login Frequency | The number of logons to the instance per second. |
|   | Average Frequency of Whole Table Scans | The number of full table scans per second. |
|   | SQL Compilations per Second | The number of SQL statements compiled per second. |
|   | Lock Timeout Times | The number of lock timeouts on the instance per second. |
|   | Deadlock Frequency | The number of deadlocks on the instance per second. |
|   | Lock Wait Frequency | The number of lock waits on the instance per second. |

## 10 Data security

### 10.1 Configure an IP address whitelist

**whitelist**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are used for database access to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. On the **Whitelist Settings** tab, click **Edit** corresponding to the **default** whitelist.

> **Note:** If you want to connect an ECS instance to an ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type. Otherwise, the connection fails.
> You can also click **Create Whitelist** to create an IP address whitelist.

6. In the **Edit Whitelist** dialog box, enter the IP addresses or CIDR blocks that you want to
allow to access your RDS instance and click **OK**. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.xx format can access your RDS instance. If you enter more than one IP address or CIDR block, separate them with commas (,). Do not add spaces preceding or following the commas. Example:

```
 192.168.0.1,172.16.213.9 .
```

If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

> **Note:** If you add a new IP address or CIDR block to the **default** whitelist, the default address 127.0.0.1 is deleted.

### 10.2 Configure SSL encryption

This topic describes how to enhance endpoint security. You can enable Secure Sockets Layer (SSL) encryption and install SSL certificates that are issued by certificate authorities (CAs) to the required application services. SSL is used at the transport layer to encrypt network connections and enhance the security and integrity of communication data. However, SSL increases the response time.

**Precautions**

An SSL CA certificate is valid for one year. You must update the validity period of the SSL CA certificate in your application or client within one year. Otherwise, your application or client that uses encrypted network connections cannot connect to the ApsaraDB RDS instance. SSL encryption may cause a significant increase in CPU utilization. We recommend that you enable SSL encryption only when you want to encrypt connections from the Internet. In most cases, connections that use an internal endpoint do not require SSL encryption. SSL encryption cannot be disabled after it is enabled. Proceed with caution.

**Enable SSL encryption**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Data Security**.
5. Click the **SSL Encryption** tab.
6. In the SSL Settings section, turn on **SSL Encryption**.
7. In the **Configure SSL** dialog box, select the endpoint for which you want to enable SSL
encryption and click **OK**.
8. Click **Download CA Certificate** to download the SSL CA certificate files in a compressed
package. The downloaded package contains three files: P7B file: used to import CA certificates to the Windows operating system. PEM file: used to import CA certificates to other operating systems or applications. JKS file: the Java truststore file. The password is apsaradb. It is used to import the CA certificate chain to Java programs.

> **Note:** When the JKS file is used in Java, you must modify the default JDK security configuration in JDK 7 and JDK 8. Open the
> `/jre/lib/security/java.security` file on the host where your application resides, and modify the following configurations:

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.dis abledAlgorithms=MD2, RSA keySize < 1024
```

> If you do not modify the JDK security configuration, the following error is reported. Typically, other similar errors are also caused by invalid Java security configurations.

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

**Configure an SSL CA certificate**

After you enable SSL encryption, configure the SSL CA certificate on your application or client before they can connect to the ApsaraDB RDS instance. This section describes how to configure an SSL CA certificate. MySQL Workbench and Navicat are used in the example. For more information, see the instructions for the other applications or clients.

**Configure a certificate on MySQL Workbench**

1. Start MySQL Workbench.
2. Choose **Database > Manage Connections**.
3. Enable **Use SSL** and import the SSL CA certificate files.

**Configure a certificate on Navicat**

1. Start Navicat.
2. Right-click the database and select **Edit Connection**.
3. Click the **SSL** tab. Select the path of the PEM-formatted CA certificate, as shown in the
following figure.
4. Click **OK**.

> **Note:** If the `connection is being used` error is reported, the previous session is still connected. Restart Navicat.

5. Double-click the database to test whether the database is connected.

**Update the validity period of an SSL CA certificate**

> **Note:** **Update Validity** causes the ApsaraDB RDS instance to restart. Proceed with caution.
> After you **update the validity period**, you must download and configure the SSL CA certificate again.

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
4. In the left-side navigation pane, click **Data Security**.
5. Click the **SSL Encryption** tab.
6. Click **Update Validity**.
7. In the message that appears, click **OK**.
estoration

## 11 Database backup and restoration

**restoration**

### 11.1 Configure an automatic backup policy

**backup policy**

Automatic backup supports full physical backups. ApsaraDB RDS automatically backs up data based on pre-configured policies. This topic describes how to configure a policy for automatic backup.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. On the **Backup and Restoration** page, click the **Backup Settings** tab.
6. Click **Edit**.
7. In the dialog box that appears, configure the automatic backup policy.

| Parameter | Description |
|---|---|
| Data Retention Period | The number of days for which you want to retain data backup files. Valid values: 7 to 730. Default value: 7. |
| Backup Cycle | The cycle based on which you want to create a backup. You can select one or more days within a week. Note For data security purposes, we recommend that you back up your ApsaraDB RDS instance at least twice a week. |
| Backup Time | The period of time for which you want to back up data. Unit: hours. |
| Backup Frequency | The frequency at which you want to back up logs. The following options are available: Same as Data Backup Every 30 Minutes The total size of log backup files remains the same regardless of the backup frequency. |

8. Click **OK**.

### 11.2 Manually back up an instance

This topic describes how to manually back up an ApsaraDB RDS instance. estoration
1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. On the **Basic Information** page, click **Back Up Instance** in the upper-right corner.
5. In the **Back Up Instance** dialog box, select **Automatic Backup** or **Full Backup** from the
**Select Backup Mode** drop-down list.

> **Note:** ApsaraDB RDS supports the following backup methods:
> **Automatic Backup**: After you select Automatic Backup, the system immediately performs an incremental or full backup based on the instance.
> **Full Backup**: After you select Full Backup, the system immediately performs a full backup.

6. Click **OK**.

**Result**

After the backup is complete, you can view the backup task on the **Data Backup** tab of the
**Backup and Restoration** page.

### 11.3 Shrink transaction logs

ApsaraDB RDS for SQL Server allows you to shrink transaction logs to reduce the log file size.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the target instance.
3. Click the instance ID or click **Manage** in the Actions column corresponding to the instance
to go to the **Basic Information** page.
4. In the left-side navigation pane, click **Backup and Restoration**.
5. In the upper-right corner of the page, click **Shrink Transaction Log**. In the message that
appears, click **OK**.

> **Note:** The shrinkage takes about 20 minutes to complete. ApsaraDB RDS for SQL Server shrinks transaction logs during each backup.

to ApsaraDB RDS for SQL Server

## 12 Migrate full backup data to ApsaraDB RDS for SQL Server

**to ApsaraDB RDS for SQL**

**Server**

This topic describes how to migrate full backup files of an on-premises database from Object Storage Service (OSS) to ApsaraDB RDS for SQL Server.

**Prerequisites**

Your ApsaraDB for RDS instance has sufficient storage space. If the space is insufficient, you must increase it before you migrate data to the instance. The destination database on your ApsaraDB for RDS instance has a different name from the on-premises database. A privileged account is created on your ApsaraDB for RDS instance. For more information, see Create an account. An Object Storage Service (OSS) bucket is created in the region where your ApsaraDB for RDS instance is created. For more information, see Create buckets in the **OSS User Guide**. The DBCC CHECKDB statement is executed, and the execution result indicates that no allocation or consistency errors occur.

> **Note:** If no allocation or consistency errors occur, the following execution result is returned:

```
... CHECKDB found 0 allocation errors and 0 consistency errors in database 'xxx'. DBCC execution completed. If DBCC printed error messages, contact your system adm inistrator.
```

**Precautions**

Full backup files cannot be migrated to an ApsaraDB for RDS instance of an earlier SQL Server version. For example, if the on-premises database runs SQL Server 2016 and your ApsaraDB for RDS instance runs SQL Server 2012, you cannot migrate full backup files of the on-premises database to your ApsaraDB for RDS instance. Differential or log backup files are not supported. The names of full backup files cannot contain special characters, such as `at signs (@) and` vertical bars (|) . If the file names contain special characters, the migration fails. After the service account of your ApsaraDB for RDS instance is granted the access permission on the OSS bucket, the system creates a role named **AliyunRDSImportRole** in RAM. Do not modify or delete this role. Otherwise, you cannot download full backup files when you migrate data to your ApsaraDB for RDS instance. In this case, you must reauthorize the service account of your ApsaraDB for RDS instance. Before the migration is complete, do not delete the backup files from the OSS bucket. Otherwise, the migration fails. The names of backup files can be suffixed only with bak, diff, trn, or log. If you do not use the script in this topic to generate a backup file, you must name the backup file by using one of the following suffixes: bak: indicates a full backup file. diff: indicates a differential backup file. trn or log: indicates a log backup file. to ApsaraDB RDS for SQL Server

**Back up the on-premises database**

> **Note:** Before you perform a full backup, stop writing data to the on-premises database. The data written during the backup process is not backed up.

1. Download the backup script. Double-click the backup script to open it by using the Microsoft
SQL Server Management Studio (SSMS) client.
2. Configure the following parameters.

| Parameter | Description |
|---|---|
| @backup databases l _ _ ist | The databases that you want to back up. Separate them with semicolons (;) or commas (,). |
| @backup type _ | The backup type. Valid values: FULL: full backup DIFF: differential backup LOG: log backup |
| @backup folder _ | The directory in which you want to store the backup files on your computer. If the specified directory does not exist, the system creates a directory. |
| @is run _ | Specifies whether to perform a backup. Valid values: 1: performs a backup. 0: performs no backup but a check. |

3. Run the backup script.

**Upload full backup files to the OSS bucket**

After the on-premises database is backed up, you must upload full backup files to the OSS bucket. You can use one of the following methods: Use the OSS console If the size of backup files is smaller than 5 GB, you can upload the files in the OSS console. For more information, see Upload objects in the **OSS User Guide**. Call an OSS API operation You can call an OSS API operation to upload the full backup files in resumable mode. For more information, see Multipart upload-relevant operations in the **OSS Developer Guide**.

**Create a migration task**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. In the upper-right corner of the page, click **Migrate OSS Backup Data to RDS** .
5. Click **Next** twice until the Import Data step appears.
6. Configure the following parameters.

| Parameter | Description |
|---|---|

to ApsaraDB RDS for SQL Server

| Database Name | Enter the name of the destination database on your ApsaraDB for RDS instance. Note The name of the database must meet the requirements of SQL Server. |
|---|---|
| OSS Bucket | Select the OSS bucket that stores the backup files. |
| OSS Subfolder Name | Enter the name of the OSS subfolder that stores the backup files. |
| OSS File | Click the search icon to search for backup files by using the prefix-based fuzzy match. The system displays the name, size, and update time of each backup file. Select the backup file that you want to migrate to your ApsaraDB for RDS instance. |
| Cloud Migration Method | One-time Full Backup File Migration: uploads full backup data to your ApsaraDB for RDS instance. Select this option if you want to migrate only a single full backup file. |

7. Click **OK**.
Wait for the migration task to complete. You can click **Refresh** to view the latest status of the migration task. If the migration fails, fix the error based on the message displayed in the Task Description column. For more information, see Common errors.

**View the migration task**

In the left-side navigation pane, click **Backup and Restoration**. Click the **Backup Data**
**Upload History** tab. The system displays the migration tasks in the last week.

**Common errors**

Each record of a migration task contains a task description, which helps you identify the error cause and fix the error. The following list describes common errors: A database with the same name as the on-premises database exists on your ApsaraDB for RDS instance. Error message: The database (xxx) is already exist on RDS, please backup and drop it, then try again. Cause: The on-premises database is named the same as an existing database on your ApsaraDB for RDS instance. For data security purposes, ApsaraDB RDS for SQL Server does not allow such a database to be migrated. Solution: If you need to overwrite the database in your ApsaraDB for RDS instance with the on-premises database, you must back up the database, delete it from your ApsaraDB for RDS instance, and then migrate the on-premises database to your ApsaraDB for RDS instance. A differential backup file is used. Error message: Backup set (xxx.bak) is a Database Differential backup, we only accept a FULL Backup. Cause: The file that you uploaded is a differential backup file, but not a full backup file. The migration solution for full backup data supports only full backup files. A log backup file is used. Error message: Backup set (xxx.trn) is a Transaction Log backup, we only accept a FULL Backup. Cause: The file that you uploaded is a log backup file, but not a full backup file. The migration solution for full backup data supports only full backup files. to ApsaraDB RDS for SQL Server The backup file fails the verification. Error message: Failed to verify xxx.bak, backup file was corrupted or newer edition than RDS. Cause: The backup file is damaged, or the on-premises database runs an SQL Server version later than your ApsaraDB for RDS instance. For example, if the on-premises database runs SQL Server 2016 and your ApsaraDB for RDS instance runs SQL Server 2012, the error message is returned. Solution: If the backup file is damaged, perform a full backup on the on-premises database again. If the database engine version does not meet the requirements, select an ApsaraDB for RDS instance that runs the same version as or a later version than the on-premises database. DBCC CHECKDB fails to be executed. Error message: DBCC checkdb failed. Cause: Allocation or consistency errors occurred in the on-premises database. Solution: Execute the following statement in the on-premises database.

> **Note:** Data loss may occur when you use this statement to fix errors.

```
DBCC CHECKDB (DBName, REPAIR_ALLOW_DATA_LOSS) WITH NO_INFOMSGS, ALL_ERRORMSGS
```

The remaining storage space of your ApsaraDB for RDS instance is insufficient. (1) Error message: Not Enough Disk Space for restoring, space left (xxx MB) < needed (xxx MB). Cause: The remaining storage space of your ApsaraDB for RDS instance does not meet the migration requirements. Solution: Increase the storage space of your ApsaraDB for RDS instance. The remaining storage space of your ApsaraDB for RDS instance is insufficient. (2) Error message: Not Enough Disk Space, space left xxx MB < bak file xxx MB. Cause: The remaining storage space of your ApsaraDB for RDS instance is smaller than the size of the backup file. Solution: Increase the storage space of your ApsaraDB for RDS instance. No privileged account exists. Error message: Your RDS doesn't have any init account yet, please create one and grant permissions on RDS console to this migrated database (XXX). Cause: No privileged account is created on your ApsaraDB for RDS instance, and the database permissions are not granted to accounts. However, when this error message is returned, the backup file has been restored to your ApsaraDB for RDS instance, and the migration task is successful. Solution: Create a privileged account. For more information, see Create an account.
