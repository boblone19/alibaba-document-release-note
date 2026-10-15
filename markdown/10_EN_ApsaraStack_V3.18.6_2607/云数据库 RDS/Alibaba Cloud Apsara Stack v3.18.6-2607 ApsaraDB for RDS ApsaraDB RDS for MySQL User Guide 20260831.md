---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 168
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E6%95%B0%E6%8D%AE%E5%BA%93%20RDS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20ApsaraDB%20for%20RDS%20ApsaraDB%20RDS%20for%20MySQL%20User%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 ApsaraDB for RDS ApsaraDB RDS for MySQL User Guide 20260831

es

## Console feature release

**notes**

This topic describes new features and key updates for RDS for MySQL.

**v3.18.6sp-2607**

| Feature overview | Description | References |
|---|---|---|
| Configuration overview for instance creation | When creating an instance, a Configuration Overview panel appears on the right after you set all parameters. Use this panel to review the instance's full configuration. | Create an instance |

## What is ApsaraDB RDS?

ApsaraDB RDS is a stable, reliable, and scalable online database service. Based on the distributed file system and high-performance storage, ApsaraDB RDS provides a set of solutions for disaster recovery, backup, restoration, monitoring, and migration. ApsaraDB RDS supports four database engines, which are MySQL, SQL Server, PolarDB, and PostgreSQL. You can create RDS instances that run these engines to meet your business requirements.

**ApsaraDB RDS for MySQL**

ApsaraDB RDS for MySQL is developed based on AliSQL and provides excellent performance. ApsaraDB RDS for MySQL is a tried and tested solution that handled the high-volume concurrent traffic during Double 11. ApsaraDB RDS for MySQL supports deployment with mixed x86 and ARM clusters. It integrates basic features such as whitelist configuration, backup and restoration, Transparent Data Encryption (TDE), data migration, and management of instances, accounts, and databases. ApsaraDB RDS for MySQL also provides the following advanced features:
**Read-only instance:** In scenarios in which ApsaraDB RDS for MySQL handles a small
number of write requests but a large number of read requests, you can create read-only instances to scale up reading capabilities and increase the application throughput.
**Read/write splitting:** The read/write splitting feature provides a read/write splitting
endpoint. This endpoint enables automatic read/write splitting for a primary RDS instance and all of its read-only RDS instances. An application can connect to the read/write splitting endpoint to read and write data. Write requests are forwarded to the primary RDS instance while read requests are forwarded to read-only RDS instances based on their weights. To increase the reading capability of your database system, you need to only add more readonly RDS instances.
**High availability based on zone-disaster recovery**: RDS for MySQL instances that run
RDS High-availability Edition adopt an HA architecture that consists of a primary node and a secondary node deployed in two different zones within the same region, such as China (Shanghai) Zone A and China (Shanghai) Zone B. The primary node handles read and write requests. The secondary node synchronizes data from the primary node in real time and does not handle requests. When the zone in which the primary node is deployed becomes unavailable due to power outage or network issues, the secondary node is automatically promoted to the primary node within a period ranging from 30 seconds to 5 minutes. The time required for the failover depends on the fault detection and recovery mechanism.

## Instance types

This topic describes the instance types of ApsaraDB RDS for MySQL. Different instance types deliver different performance.

**IOPS**

The maximum IOPS of an ApsaraDB RDS for MySQL instance that uses local disks varies based on the instance type. The maximum IOPS of an ApsaraDB RDS for MySQL instance that uses cloud disks varies based on the instance type and storage capacity. The following formula can be used to calculate the IOPS of an ApsaraDB RDS for MySQL instance that uses cloud disks. The storage capacity is measured in GB.

```
min{1800 + 30 × Storage capacity, 25000}
```

**Note**

If the throughput of an ApsaraDB RDS for MySQL instance reaches the upper limit, the IOPS of the instance also decreases.

**Primary ApsaraDB RDS for MySQL instances**

**High-availability Edition**

| Instanc e family | Suppor ted version | Instance type | Number of CPU cores and memory capacity | Maxim um IOPS | Maxim um numb er of conne ctions | Storage capacity |
|---|---|---|---|---|---|---|
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.t1.small | 1 core, 1 GB | 1,200 | 300 | 5 GB to 2,000 GB |
|   |   | rds.mysql.s1.small | 1 core, 2 GB | 2,000 | 600 |   |
|   |   | rds.mysql.s2.large | 2 cores, 4 GB | 4,000 | 1,200 |   |
|   |   | rds.mysql.s2.xlarge | 2 cores, 8 GB | 6,000 | 2,000 |   |
|   |   | rds.mysql.s3.large | 4 cores, 8 GB | 8,000 | 2,000 |   |
|   |   | rds.mysql.m1.medi um | 4 cores, 16 GB | 14,000 | 4,000 |   |

| General- purpose |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   | rds.mysql.c1.large | 8 cores, 16 GB | 20,000 | 4,000 |   |
|   |   | rds.mysql.c1.xlarge | 8 cores, 32 GB | 28,000 | 8,000 |   |
|   |   | rds.mysql.g2.2xlarg e | 16 cores, 32 GB | 40,000 | 8,000 | 50 GB to 3,000 GB |
| instance family |   |   |   |   |   |   |
|   |   | rds.mysql.c2.xlarge | 16 cores, 64 GB | 40,000 | 16,000 | 5 GB to 3,000 GB |
|   |   | rds.mysql.c2.xlp2 | 16 cores, 96 GB | 40,000 | 24,000 |   |
|   | 5.7 | rds.mysql.c2.2xlarg e | 16 cores, 128 GB | 16,000 | 32,000 |   |
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.g2.3xlarg e | 24 cores, 48 GB | 40,000 | 12,000 | 50 GB to 3,000 GB |
|   |   | rds.mysql.x2.3xlarg e | 24 cores, 48 GB | 50,000 | 12,000 | 50 GB to 2,000 GB |
|   |   | rds.mysql.g4.3xlarg e | 24 cores, 96 GB | 50,000 | 24,000 | 50 GB to 3,000 GB |
|   |   | rds.mysql.g2.4xlarg e | 32 cores, 64 GB | 60,000 | 16,000 |   |
|   |   | rds.mysql.g4.4xlarg e | 32 cores, 128 GB | 60,000 | 32,000 |   |
|   |   | rds.mysql.g2.8xlarg e | 64 cores, 128 GB | 60,000 | 32,000 |   |
|   |   | mysql.x8.medium.2 | 2 cores, 16 GB | 15,000 | 2,500 | 50 GB to 1,000 GB |
|   |   | mysql.x4.large.2 | 4 cores, 16 GB | 30,000 | 2,500 |   |
|   |   | mysql.x8.large.2 | 4 cores, 32 GB | 40,000 | 5,000 |   |

| Dedicat ed instance family | MySQL 5.7 and MySQL 8.0 |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   | mysql.x4.xlarge.2 | 8 cores, 32 GB | 45,000 | 5,000 | 500 GB to 3,000 GB |
|   |   | mysql.x8.xlarge.2 | 8 cores, 64 GB | 50,000 | 10,000 |   |
|   |   | rds.mysql.x2.2xlarg e | 16 cores, 32 GB | 40,000 | 8,000 | 50 GB to 2,000 GB |
|   |   | mysql.x4.2xlarge.2 | 16 cores, 64 GB | 60,000 | 10,000 | 500 GB to 3,000 GB |
|   |   | mysql.x8.2xlarge.2 | 16 cores, 128 GB | 60,000 | 20,000 |   |
|   |   | rds.mysql.x4.3xlarg e | 24 cores, 96 GB | 50,000 | 24,000 | 50 GB to 2,000 GB |
|   |   | rds.mysql.x2.4xlarg e | 32 cores, 64 GB | 60,000 | 16,000 | 50 GB to 3,000 GB |
|   |   | mysql.x4.4xlarge.2 | 32 cores, 128 GB | 80,000 | 20,000 | 1,000 GB to 6,000 GB |
|   |   | rds.mysql.x4.4xlarg e | 32 cores, 128 GB | 60,000 | 32,000 | 50 GB to 3,000 GB |
|   |   | mysql.x8.4xlarge.2 | 32 cores, 256 GB | 100,000 | 40,000 | 1,000 GB to 6,000 GB |
|   |   | rds.mysql.x2.8xlarg e | 64 cores, 128 GB | 60,000 | 32,000 | 50 GB to 3,000 GB |
|   |   | mysql.x8.8xlarge.2 | 64 cores, 512 GB | 150,000 | 80,000 | 1,000 GB to 6,000 GB |
| Dedicat ed host instance family | 5.7 | rds.mysql.st.h43 | 60 cores, 470 GB | 150,000 | 100,00 0 | 1,000 GB to 6,000 GB |
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.st.v52 | 90 cores, 720 GB | 150,000 | 150,00 0 |   |

**Read-only instance**

| Instance family | Supporte d version | Instance type | Number of CPU cores and memory capacity | Maxim um numbe r of connec tions | Storage capacity |
|---|---|---|---|---|---|
| General- purpose instance family | MySQL 5.7 and MySQL 8.0 | rds.mysql.t1.small | 1 core, 1 GB | 300 | 5 GB to 2,000 GB |
|   |   | rds.mysql.s1.small | 1 core, 2 GB | 600 |   |
|   |   | rds.mysql.s2.large | 2 cores, 4 GB | 1,200 |   |
|   |   | rds.mysql.s2.xlarge | 2 cores, 8 GB | 2,000 |   |
|   |   | rds.mysql.s3.large | 4 cores, 8 GB | 2,000 |   |
|   |   | rds.mysql.m1.medium | 4 cores, 16 GB | 4,000 |   |
|   |   | rds.mysql.c1.large | 8 cores, 16 GB | 4,000 |   |
|   |   | rds.mysql.c1.xlarge | 8 cores, 32 GB | 8,000 |   |
|   |   | rds.mysql.c2.xlarge | 16 cores, 64 GB | 16,000 | 5 GB to 3,000 GB |
|   |   | rds.mysql.c2.xlp2 | 16 cores, 96 GB | 24,000 |   |
|   |   | mysqlro.x8.medium.1 | 2 cores, 16 GB | 2,500 | 50 GB to 1,000 GB |
|   |   | mysqlro.x4.large.1 | 4 cores, 16 GB | 2,500 |   |
|   |   | mysqlro.x8.large.1 | 4 cores, 32 GB | 5,000 |   |
|   |   | mysqlro.x4.xlarge.1 | 8 cores, 32 GB | 5,000 |   |

| Dedicated instance | MySQL 5.7 and MySQL |   |   |   |   |
|---|---|---|---|---|---|
|   |   | mysqlro.x8.xlarge.1 | 8 cores, 64 GB | 10,000 | 500 GB to 3,000 GB |
| family | 8.0 |   |   |   |   |
|   |   | mysqlro.x4.2xlarge.1 | 16 cores, 64 GB | 10,000 |   |
|   |   | mysqlro.x8.2xlarge.1 | 16 cores, 128 GB | 20,000 |   |
|   |   | mysqlro.x4.4xlarge.1 | 32 cores, 128 GB | 20,000 |   |
|   |   | mysqlro.x8.4xlarge.1 | 32 cores, 256 GB | 40,000 | 1,000 GB to 6,000 GB |
|   |   | mysqlro.x8.8xlarge.1 | 64 cores, 512 GB | 80,000 |   |
| Dedicated host instance family | 5.7 | rds.mysql.st.h43 | 60 cores, 470 GB | 100,000 | 1,000 GB to 6,000 GB |
|   | MySQL 5.7 and MySQL 8.0 | rds.mysql.st.v52 | 90 cores, 720 GB | 150,000 |   |

console

## Log on to the ApsaraDB

**RDS console**

This topic describes how to log on to the ApsaraDB RDS console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome.

**Procedure**

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

## Quick start

### Limits

To ensure instance stability and security, ApsaraDB RDS for MySQL has specific service limits, as listed in the following table.

| Item | Limits |
|---|---|
| Instance parameters | Instance parameters can be modified by using the ApsaraDB RDS console or API operations. Due to security and stability considerations, only specific parameters can be modified. |
| Root permissions of databases | The root or system administrator permissions are not provided. |
| Database backup | Logical backup can be performed by using the CLI or GUI. Physical backup can be performed only by using the ApsaraDB RDS console or API operations. |
| Database restoration | Logical restoration can be performed by using the CLI or GUI. Physical restoration can be performed only by using the ApsaraDB RDS console or API operations. |
| ApsaraDB RDS for MySQL storage engine | Only InnoDB is supported. To ensure performance and security, we recommend that you use the InnoDB storage engine. The TokuDB storage engine is not supported. Percona no longer provides support for TokuDB, which in extreme cases may lead to bugs that cannot be fixed and impact your workloads. The MyISAM storage engine is not supported Due to the inherent shortcomings of the MyISAM engine, data may be lost. Only specific existing instances use the MylSAM engine. MyISAM engine tables in newly created instances are automatically converted to InnoDB engine tables. The Memory engine is not supported. Newly created Memory tables are automatically converted into InnoDB tables. |
| Database replication | ApsaraDB RDS for MySQL provides a primary/secondary replication architecture. The secondary instances in this replication architecture are hidden and cannot be directly accessed. |
| Instance restart | Instances must be restarted by using the ApsaraDB RDS console or API operations. |
| Account and database management | ApsaraDB RDS for MySQL allows you to manage accounts and databases by using the ApsaraDB RDS console. ApsaraDB RDS for MySQL also allows you to create a privileged account to manage users, passwords, and databases. |
| Standard account | Authorization is not allowed. The ApsaraDB RDS console allows you to manage accounts and databases. Instances that support standard accounts also support privileged accounts. |

| Privileged account | Authorization is allowed on standard accounts. The privileged account cannot be reverted to a standard account. |
|---|---|

### Procedure

ApsaraDB RDS quick start covers the following topics: creating an ApsaraDB RDS instance, configuring an IP address whitelist, creating a database, creating an account, and connecting to the instance. This topic describes how to use ApsaraDB RDS and provides all the necessary information to create an ApsaraDB RDS instance. ApsaraDB RDS for MySQL is used in the example. Typically, after an instance is created, you must perform several operations to make the instance ready for use, as shown in Quick start flowchart. Figure 1. Quick start flowchart Create an instance An instance is a virtual database server on which you can create and manage multiple databases. Configure an IP address whitelist After you create an RDS instance, you must configure IP address whitelists for the RDS instance to allow access from external devices. Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your RDS instance, the workloads on the instance are not affected. Category Attribute Match and Create an account Before you use a database, you must create the database and an account on the ApsaraDB RDS instance. Connect to an ApsaraDB RDS for MySQL instance After you create an ApsaraDB RDS instance, configure an IP address whitelist, and create a database and an account, you can connect to the instance by using a database client.

### Create an instance

This topic describes how to create an instance in the ApsaraDB RDS Console.

**Prerequisites**

An Apsara Stack tenant account is created.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instance List**. On the page that appears, click
**Create an instance**.
3. Configure the following parameters.

| Section | Paramete r | Description |
|---|---|---|
| Basic Configura tion | Organizat ion | The organization to which the instance belongs. |
|   | Resource Set | The resource set to which the instance belongs. |
| Area | Region | The region in which you want to create the instance. Services in different regions cannot communicate over an internal network. After the instance is created, the region cannot be changed. |
|   | Deployme nt Method | ApsaraDB RDS supports Multi-zone Deployment and Single-zone Deployment. You can select the zones for the primary and secondary nodes based on your requirements. |
|   | Primary Node Zone | The zone of the primary node. |
| Document Ver | sion: 20260831 1 |   |

|   | Secondar y Node Zone | The zone of the secondary node. This parameter is available only when you select the Multi-zone Deployment option. |
|---|---|---|
| Specificat ions | Database Engine | The database engine of the instance. Select MySQL. |
|   | Chip Architect ure | The chip architecture of the host on which the instance is deployed. Note If you do not have permissions to select an option, contact the operations administrator to grant the permissions to your account. |
|   | Engine Version | The version of the database engine. Valid values: 8.0 5.7 |
|   | Edition | The edition of the instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Storage Type | The storage type of the instance. Select Local SSD. |
|   | Instance Specificat ions | The specifications of the instance. The maximum number of connections and the maximum IOPS vary based on the memory size. The actual specifications are displayed in the console. For more information, see Instance types in ApsaraDB RDS Product Introduction. You can click AI Specification Recommendation and enter your usage scenario in Apsara Copilot to obtain optimal specification recommendations that balance cost and performance. |
|   | Storage Capacity | The maximum amount of storage that is provisioned to store data files, system files, binary log files, and transaction files in the new ApsaraDB RDS instance. For more information, see Instance types in ApsaraDB RDS Product Introduction. |
|   | Connectio n Type | The connection type of the instance. Valid values: Internet: Instances of this connection type can be connected over the Internet. Internal Network: Instances of this connection type can be connected over an internal network. Note After the instance is created, the value of this parameter cannot be changed. Proceed with caution. |

| Network |   |   |
|---|---|---|
|   | Network Type | The network type of the instance. Valid values: Classic Network: Cloud services in the classic network are not isolated. Unauthorized access to a cloud service can be blocked only by the security group or whitelist of the service. Note Instances that use standard SSDs cannot be deployed in the classic network. VPC: A virtual private cloud (VPC) helps you build an isolated network environment on Apsara Stack. You can customize route tables, CIDR blocks, and gateways in a VPC. We recommend that you select VPC for improved security. |
|   | VPC | The VPC in which you want to create the instance. Note This parameter is required when Network Type is set to VPC. |
|   | vSwitch Zone | The zone in which the vSwitch is located. Note This parameter is available only when Network Type is set to VPC. |
|   | vSwitch | The vSwitch to which the instance is connected. Note This parameter is required when Network Type is set to VPC. |
|   | IP Whitelist | The IP address or CIDR block that is allowed to connect to the instance. |
| Instance Settings | Quantity | The number of instances that you want to create. Default value: 1. |
|   | Instance Name | The name of the instance. It must be 2 to 64 characters in length. It must start with a letter. It can contain letters, digits, hyphens (-), underscores ( ), and _ colons (:). It cannot start with http:// or https://. |

4. Click **Submit**.

### Initialization settings

#### Configure an IP address whitelist for an

**ApsaraDB RDS instance**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are allowed to access the instance to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your ApsaraDB RDS instance, the workloads on the instance are not affected. You can configure a whitelist in two modes: Configure an IP address whitelist: Add IP addresses to allow only specified origins to connect to the ApsaraDB RDS instance. Configure an Elastic Compute Service (ECS) security group: Add an ECS security group for the ApsaraDB RDS instance to allow all ECS instances in the security group to connect to the ApsaraDB RDS instance.

**Usage notes**

**Default group restrictions**: The default whitelist group ( `default` ) can be modified or
cleared, but it cannot be deleted.
**Quantity limits**: A maximum of 1,000 IP addresses or CIDR blocks can be added to a
whitelist. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks (such as `192.168.1.0/24` ) to reduce the number of entries.
**Format requirements**: You must separate multiple IP addresses or CIDR blocks with
commas (,). Do not include spaces before or after the commas.

| dress to the | default |   |
|---|---|---|
| 127.0.0.1 |   |   |
|   |   | . |

**Override mechanism**: After you add any new IP address to the `default` group, the
system automatically removes the default deny rule `127.0.0.1` .
**Prerequisites for network connectivity**: If you want to connect an ECS instance to an
ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type (such as VPC). Otherwise, the connection fails.

**Configure a standard IP address whitelist**

1. 2.
3. In the left-side navigation pane, click **Data Security**.
4. On the **Whitelist Settings** tab, click **Modify**.

**Note**

Click **Create Whitelist** to create a custom group.
5. In the **Modify Whitelist** dialog box, enter the IP addresses or CIDR blocks that are allowed
to connect to your ApsaraDB RDS instance, and then click **OK**. Then, click OK to save the configuration. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.XX range can access your ApsaraDB RDS instance. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

#### Create an account

Detect the language of the input text. Supports automatic recognition of 23 languages. Best suited to short text such as search queries, product titles, and chat messages. Synchronous.

**Endpoint**

```
POST /ai/text/marco/language-detection
```

**Use cases**

Cross-border search -- detect the buyer's search-query language and route to the matching index. Title preprocessing -- detect source language automatically before calling the Text Translation API, so callers do not need to pass `SourceLanguage` . Chat routing -- forward users to native-language agents based on detected language.

**Quick start**

```java
import json data = json.dumps({ "SourceText": "Hello world" }) result = make_signed_request("/ai/text/marco/language-detection", data) print(result["Data"]["DetectedLanguage"]) # en
```

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceText | String | Yes | Text to identify. Up to ~1024 characters recommended; very short inputs (single tokens) have lower accuracy. |

**Response fields**

| Field | Type | Description |
|---|---|---|
| Code | String | Business status. Success when OK; otherwise see Error codes. |

| psaraDB RDS for MySQL User G |   | ApsaraDB for RD |
|---|---|---|

| Field | Type | Description |
|---|---|---|
| Message | String | Business message. |
| RequestId | String | Unique request identifier. |
| Success | Boolean | Whether the call succeeded. |
| Data.DetectedLanguage | String | Detected language code; see "Supported languages" below. |
| Data.UsageMap.RequestCount | Number | Request count for billing reconciliation. |

|   | Data.UsageMap.RequestCount |   |
|---|---|---|

**Response example**

`{`

```json
  "Code": "Success",
  "Message": "ok",
  "RequestId": "21570000-0000-0000-0000-000000000001",
  "Success": true,
  "Data": {
    "DetectedLanguage": "en",
    "UsageMap": { "RequestCount": 1 }
```

`}` `}`

**Supported languages (23)**

| ngali ( bn ), German ( de he ), Indonesian ( id ), It tch ( nl ), Polish ( pl ), Po krainian ( uk ), Urdu ( ur Traditional ( zh-tw ). |   | de |   |
|---|---|---|---|
|   | id |   |   |
|   |   |   | ), It ), Po |
|   | pl |   |   |

|   | es |
|---|---|
| ja |   |

( `fr` ), Hebrew ( `he` ), Indonesian ( `id` ), Italian ( `it` ), Japanese ( `ja` ), Korean ( `ko` ),

| ms |   | ), |
|---|---|---|
| ( |   |   |

Malay ( `ms` ), Dutch ( `nl` ), Polish ( `pl` ), Portuguese ( `pt` ), Russian ( `ru` ), Thai ( `th` ),

**Error codes**

Common error codes: `InvalidParameter` (missing or empty `SourceText` ), `InternalError` (system busy). See Error codes for the full reference.

**What's next**

Text Translation API -- translate plain text. Text Correction API -- spelling correction.

#### Create a database

Multimodal-LLM-based cross-platform category-attribute filling. Given source-platform product info (title, source category, description, SKU, attributes, up to 10 images), match the precise target-platform category and fill every required attribute, with a per-attribute confidence and rationale. Synchronous.

**Endpoint**

```
POST /ai/material/category/attribute
```

**Use cases**

1688 → TEMU cross-platform listing where platform categories differ significantly and have complex hierarchical relations (material → wood species → density). Top sellers' bulk publishing, ERP / SaaS integrations, fast SMB single-item listing.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category path. |
| ProductDescription | String | No | Product description. |
| SkuInfo | Object[] | No | SKU list (spec + price per item). |
| ProductAttributes | Object | No | Source-platform attribute key-value pairs. |
| ImageUrls | String[] | No | Up to 10 image URLs. The multimodal model infers attributes from images. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Matched precise category path on the target platform. |
| Data.Attributes | Object[] | Filled attributes. Each item has Name , Value , Confidence (0-100), Reason , and SourceMatched (whether the value reused a source- platform attribute). |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Fans > USB Fans",
    "Attributes": [
      { "Name": "Battery Type", "Value": "Lithium-Ion", "Confidence": 92, "Reason": "Ti
tle and image both indicate rechargeable", "SourceMatched": false },
      { "Name": "Connectivity",  "Value": "USB Type-C",  "Confidence": 88, "Reason": "P
ort visible in image", "SourceMatched": true }
```

`]` `}` `}`

**Error codes**

See Error codes.

**What's next**

Category Match API -- category match alone.

### Connect to an ApsaraDB RDS

**for MySQL instance**

After you complete the initial configuration of your ApsaraDB RDS for MySQL instance, you can connect to it from an Elastic Compute Service (ECS) instance or an on-premises client.

**Background information**

After you Create an instance, Configure an IP address whitelist, and Create an account, you can connect to the ApsaraDB RDS for MySQL instance by using a database client or by configuring the endpoint, port, and account information in your application. If you need to connect an ECS instance to an ApsaraDB RDS instance, you must make sure that both instances are in the classic network or in the same virtual private cloud (VPC), and the IP address of the ECS instance is added to an IP address whitelist of the ApsaraDB RDS instance.

**Connect to an instance from a client**

ApsaraDB RDS for MySQL is fully compatible with open source MySQL. You can connect to an ApsaraDB RDS instance from a database client by using a method similar to the method that is used to connect to an open source MySQL database. In the following example, the HeidiSQL client is used.
1. Start the HeidiSQL client.
2. In the lower-left corner of the Session manager dialog box, click **New**.
3. Enter information about the ApsaraDB RDS instance to which you want to connect. The
following table describes the required parameters.

| Paramet er | Description |
|---|---|
| Networ k type | Select the network type of the ApsaraDB RDS instance to which you want to connect. For example, select MariaDB or MySQL (TCP/IP). |

| Hostna me / IP | Enter the internal or public endpoint of the ApsaraDB RDS instance. If your client is deployed on an ECS instance that is in the same region and has the same network type as the ApsaraDB RDS instance, use the internal endpoint. For example, if the ECS and ApsaraDB RDS instances are both in a VPC located in the China (Hangzhou) region, you can use the internal endpoint of the ApsaraDB RDS instance to create a secure connection. In other scenarios, use the public endpoint. To view the internal and public endpoints and port numbers of the ApsaraDB RDS instance, perform the following operations: i. Log on to the ApsaraDB RDS console. ii. Find the ApsaraDB RDS instance to which you want to connect and click its ID. iii. In the Basic Information section, view the internal and public endpoints and port numbers of the instance. |
|---|---|
| User | Enter the name of the account used to connect to the ApsaraDB RDS instance. |
| Passwor d | Enter the password of the account used to connect to the ApsaraDB RDS instance. |
| Port | If you connect to the instance over an internal network, enter the internal port number of the instance. If you connect to the instance over the Internet, enter the public port number of the instance. |

4. Click **Open**. If the connection information is correct, you can connect to the instance.

## Instances

### Create an instance

This topic describes how to create an ApsaraDB for RDS instance by using the Alibaba Cloud console.

**Prerequisites**

To create an instance, you must have an Alibaba Cloud account.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**, and then click **Create Instance**.
3. Configure the following parameters.

| Category | Paramete r | Description |
|---|---|---|
| Basic configura tions | Organizat ion | The organization that will contain the instance. |
|   | Resource set | The resource set that will contain the instance. |
| Region and zone | Region | The region where the instance is located. Services in different regions cannot communicate over the internal network. You cannot change the region after the instance is created. |
|   | Deployme nt mode | Supported modes include Multi-AZ deployment and Single-AZ deployment. You can select availability zones for the primary and secondary nodes. |
|   | Primary AZ | The availability zone for the instance's primary node. |
|   | Secondar y AZ | The availability zone of the instance's secondary node. This is displayed only when the deployment mode is set to Multi-AZ deployment. |
|   | DB engine | The database engine type. Select MySQL. |
|   | Architect ure | The CPU architecture of the instance. If you receive an "unauthorized" message, ask your operations administrator to grant the required permissions to your account. |

| saraDB RDS fo e·Instances |   |   |
|---|---|---|
| Instance specificat ions |   |   |
|   | Engine version | The database engine version. The following versions are supported: 8.0 5.7 |
|   | Series | The database instance series. For more information, see the Instance Types chapter in ApsaraDB for RDS Product Introduction. |
|   | Storage type | The storage type for the instance. Select local SSD. |
|   | Instance type | The instance type. Different instance types provide different maximum numbers of connections and IOPS. The actual values are shown on the console page. For more information, see the Instance Types chapter in ApsaraDB for RDS Product Introduction. Click AI-Powered Instance Type Recommender and describe your use case to the Apsara AI Assistant to get a recommendation that balances cost and performance. |
|   | Storage space | The amount of storage space for the instance. This space is used for data, system files, binary log (binlog) files, and transaction files. For more information, see the Instance Types chapter in ApsaraDB for RDS Product Introduction. |
| Network | Network connectio n type | ApsaraDB for RDS provides two types of connection endpoints: Public connection: Allows you to access the database from the internet. Internal connection: Allows you to access the database from the internal Alibaba Cloud network. Important You cannot change this setting after the instance is created. |
|   | Network type | The network type for the instance. Supported types include: Classic network: In a classic network, cloud services are not isolated. You must rely on the security group or whitelist policies of each service to block unauthorized access. Virtual Private Cloud: A Virtual Private Cloud (VPC) is an isolated network environment on Alibaba Cloud. You can customize route tables, IP address ranges, and gateways. A VPC is recommended for better security. |
|   | VPC | Select the target VPC. This parameter is required if you setN etwork type to Virtual Private Cloud. |
|   | VSwitch AZ | The availability zone for the VSwitch. This parameter is required if you set Network type to Virtual Private Cloud. |

|   | VSwitch | Select a VSwitch within the VPC. This parameter is required if you set Network type to Virtual Private Cloud. |
|---|---|---|
|   | IP whitelist | A list of IP addresses and CIDR blocks that are allowed to access the instance. |
| Instance settings | Quantity | The number of instances to create. You can create multiple instances at a time. The default value is 1. |
|   | Instance name | The name of the instance. The name must meet the following requirements: Must be 2 to 64 characters long. Must start with a letter or a Chinese character. Can contain only letters, digits, hyphens (-), underscores ( ), and _ colons (:). Must not start with http:// or https://. |

4. On the right side of the page, review your settings in the **Configuration overview** panel.
If your current quota is insufficient, click **Quota Management** to request an increase. For more information, see the "Quota management" chapter of the **Unified Cloud**
**Management Platform User Guide**.
5. After you configure the parameters, click **Submit**.

### View the details of an

**ApsaraDB RDS instance**

This topic describes how to view the details of an ApsaraDB RDS instance, such as its basic information, internal network connection information, status, and configurations.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. Use one of the following methods to go to the **Basic Information** page of an RDS instance:
On the **Instances** page, click the ID of the instance to go to the **Basic Information** page. On the **Instances** page, click **Manage** in the **Actions** column of the instance to go to the
**Basic Information** page.

**References**

For more information about the mappings between MySQL versions of ApsaraDB RDS for MySQL and the MySQL community, see Release notes for AliSQL.

### Restart an instance

This topic describes how to manually restart an ApsaraDB RDS instance. This applies if the number of connections exceeds the specified threshold or if an instance has performance issues.

**Prerequisites**

The instance is in the **Running** state.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click **Restart Instance** in the upper-right corner.

**Note**

When you restart an instance, applications are disconnected from the instance. We recommend that you make appropriate service arrangements before you restart an instance. Proceed with caution.
4. In the Restart Instance message, click **Confirm**.

### Change instance

**specifications**

If the specifications of an ApsaraDB RDS for MySQL instance cannot meet your business requirements, you can change the instance specifications. This topic describes how to change the specifications, such as the instance type and storage capacity.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane of the **ApsaraDB RDS** console, click **Instances**. On the
page that appears, click the ID of the instance that you want to manage or click **Manage** in the **Actions** column of the instance to go to the **Basic Information** page.
3. In the upper-right corner of the **Configuration Information** section, click **Change**
**Specifications**.
4. On the **Change Specifications** page, configure the **Edition**, **Storage Type**, **Instance**
**Type**, **Storage Capacity**, and **Switching Time** parameters.

**Note**

If you set the **Switching Time** parameter to **Specified Time**, you must specify a point in time for the change.
5. Click **Submit**.
6. Confirm the changes and click **OK**.

### Set a maintenance window

This topic describes how to set a maintenance window for an ApsaraDB RDS instance.

**Background information**

To ensure the stability of ApsaraDB RDS instances, the backend system performs maintenance of the instances at irregular intervals. The default maintenance window is from 02:00 to 06:00. You can set the maintenance window to the off-peak period of your business to avoid impact on business.

**Precautions**

To ensure stability of the maintenance process, the instance changes to the **Maintaining**
**Instance** state before the maintenance window. When the instance is in this state, access
to data in the database and query operations such as performance monitoring are not affected. However, except for account and database management and IP address whitelist configuration, modification operations such as upgrade, downgrade, and restart are temporarily unavailable. You may encounter a network interruption during the maintenance window. Make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Configuration Information** section, click **Configure** to the right of **Maintenance**
**Window**.
4. Select a maintenance window and click **Save**.

**Note**

The maintenance window is displayed in UTC+8.

### Change the data replication

**mode**

You can set the data replication mode between primary and secondary ApsaraDB RDS instances to improve database availability.

**Background information**

ApsaraDB RDS supports the following data replication modes: Semi-sync After an application-initiated update is complete on the primary instance, logs are synchronized to all secondary instances. This transaction is considered committed after at least one secondary instance has received the logs, regardless of whether the secondary instance finishes executing the updates specified in the logs. If the secondary instances are unavailable or a network exception occurs between the primary and secondary instances, semi-synchronous replication degrades to the asynchronous mode. Asynchronous When your application initiates a request to add, delete, or modify data, the primary instance responds to your application immediately after it completes the operation. At the same time, the primary instance starts to asynchronously replicate data to its secondary instances. During asynchronous data replication, the unavailability of secondary instances does not affect the operations on the primary instance. Data remains consistent even if the primary instance is unavailable.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Service Availability**.
4. In the upper-right corner of the **Availability Information** section, click **Change Data**
**Replication Mode**.
5. In the dialog box that appears, select a data replication mode and click **OK**.

### Release an instance

When an ApsaraDB RDS for MySQL instance is no longer needed due to business decommissioning, completion of testing, or architecture adjustments, you can manually release the instance through the console.

**Usage notes**

Only instances in the **Running** state can be manually released. After an instance is released, the instance data is immediately deleted. We recommend that you back up your data before you release an instance.

**Procedure**

1.
2. In the left-side navigation pane, click **Instance List**. Find the instance that you want to
manage and click **Release an instance** in the **Operation** column.
3. In the dialog box that appears, read the risk warnings carefully, confirm that you backed up
the data, and then click **Release**.

### Update the minor engine

**version of an instance**

ApsaraDB RDS for MySQL supports both automatic updates and manual updates to the minor engine version of an ApsaraDB RDS for MySQL instance. These updates improve performance, introduce new features, or fix known issues.

**Description**

By default, the minor engine version of your ApsaraDB RDS for MySQL instance is manually updated. You can log in to the ApsaraDB RDS console, go to the **Basic Information** page of your ApsaraDB RDS for MySQL instance, and then view the settings of **Automated Update**
**of Minor Engine Version** in the Configuration Information section.
**Automatic Upgrade**: Each time you log in to the ApsaraDB RDS console and view the
basic information about your ApsaraDB RDS instance, the system queries the minor engine version of the ApsaraDB RDS instance. When a new minor engine version is released, the system automatically updates the minor engine version of your ApsaraDB RDS instance during the specified maintenance window. For more information, see Set a maintenance window.
**Manual Upgrade**: Each time you log in to the ApsaraDB RDS console and view the basic
information about your ApsaraDB RDS instance, the system queries the minor engine version of the ApsaraDB RDS instance. When a new minor engine version is released, the system does not automatically update the minor engine version of your ApsaraDB RDS instance. You can manually update the minor engine version on the **Basic Information** page. For more information, see Manually update the minor engine version.

**Usage notes**

When you update the minor engine version of your ApsaraDB RDS instance, a transient disconnection that lasts approximately 30 seconds may occur. We recommend that you update the minor engine version during off-peak hours or make sure that your application is configured to automatically reconnect to the ApsaraDB RDS instance. After you update the minor engine version of your ApsaraDB RDS instance, you cannot roll the minor engine version of the ApsaraDB RDS instance back to the previous version. After you upgrade the specifications of your ApsaraDB RDS instance, the system updates the ApsaraDB RDS instance to the latest minor engine version.

**Change the settings for Automated Update of Minor Engine**

**Version**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Configuration Information** section of the Basic Information page, click **Settings** to
the right of **Automated Update of Minor Engine Version**.
4. In the dialog box that appears, select **Manual Upgrade** and click **OK**.

**Manually update the minor version**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Configuration Information** section of the page, click **Update Minor Engine**
**Version**.

**Note**

The **Upgrade Minor Engine Version** button is displayed only when a new minor engine version is available.
4. In the dialog box that appears, specify the Update Time parameter and click **OK**.

**FAQ**

**I updated the minor engine version of my ApsaraDB RDS instance but the MySQL**

**version remains unchanged. Why?**

The minor engine version that you updated is the minor engine version of ApsaraDB RDS, but not the MySQL version. To view the minor engine version, you must run the `show variables` like '%rds_release_date%' command.

### Configure instance

**parameters**

This topic describes how to view and modify the values of some parameters and query parameter modification records in the console.

**Precautions**

To ensure the stability of your instance, you can modify only some of the parameters in the console. When you modify a parameter value, refer to the **Modifiable Parameter Value** column on the **Modifiable Parameters** page. Some parameters require an instance restart to take effect. For more information, see the
**Restart Required** column on the **Modifiable Parameters** page. Perform this operation
during off-peak hours and ensure that your application has a reconnection mechanism.

**Configure parameters**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the navigation pane on the left, click **Parameters**.
4. You can perform the following operations:
Export parameters On the Editable Parameters tab, click **Export Parameters**. The parameter settings of the ApsaraDB RDS instance are exported as a TXT file to your computer. Modify parameters in a batch by importing a file i. After you modify parameters in the exported parameter file, click **Import Parameters** and paste the parameter settings to the field. ii. Click **OK**. iii. In the upper-right corner of the page, click **Apply Changes**.

**Note**

If a modified parameter requires an instance restart to take effect, the system prompts you to restart the instance. Perform this operation during off-peak hours and ensure that your application has a reconnection mechanism. If the parameter modifications have not been submitted, you can click **Cancel** to cancel the modifications. Modify a single parameter i. On the **Editable Parameters** tab, find the parameter that you want to modify and click the icon in the **Actual Value** column. ii. Enter a new value based on the value range that is displayed. iii. Click **OK**. iv. In the upper-right corner of the page, click **Apply Changes**.

**Note**

If a modified parameter requires an instance restart to take effect, the system prompts you to restart the instance. Perform this operation during off-peak hours and ensure that your application has a reconnection mechanism. If the parameter modifications have not been submitted, you can click **Cancel** to cancel the modifications.

**View the parameter modification history**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the navigation pane on the left of the page that appears, click **Parameters**.
4. Click the **Parameter Modification History** tab.
5. Select a time range and click **OK**.

**Appendix 1: Parameters that are synchronized to read-only**

**instances**

When you modify the following parameters in a primary RDS for MySQL instance, the modification will automatically apply to the same parameters in the read-only instances of the primary instance. lower_case_table_names

**Note**

You cannot modify this parameter if your ApsaraDB RDS instance runs MySQL 8.0. innodb_large_prefix loose_validate_password_length default_time_zone rpl_semi_sync_slave_enabled

**Note**

If you modify other parameters on a primary instance, you must manually apply the same modifications to its read-only instances.

**Appendix 2: List of modifiable parameters**

| Parameter | Maj or vers ion | Def ault valu e | Value range | Res tart req uire d | Description |
|---|---|---|---|---|---|
| auto increment i _ _ ncrement | 8.0, 5.7 | 1 | [1-65535] | No | The increment value for auto-increment columns. |
| auto increment o _ _ ffset | 8.0, 5.7 | 1 | [1-65535] | No | The offset value for auto-increment columns when auto-increment-increment is not equal to 1. |

| autocommit | 5.7 | ON | [ON\|OFF] |   | No | Autocommit mode: If set to 1, all changes to tables take effect immediately. If set to 0, you must use COMMIT to accept a transaction or ROLLBACK to cancel it. If autocommit is 0 and you change it to 1, MySQL performs an autocommit for any open transaction. Note You cannot manually commit transactions in autocommit mode. To manually commit transactions, first disable autocommit mode for the database ( SET autocommit = OFF; ). |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | SET autocommit = |   |   |
|   |   |   |   |   |   |   | OFF; |   |   |   |
| automatic sp pri _ _ vileges | 8.0, 5.7 | ON | [ON\|OFF] |   | No | When this variable is set to 1 (the default), the server automatically grants the EXECUTE and ALTER ROUTINE privileges to the user who creates a stored procedure if the user cannot execute, alter, or drop the stored procedure. The ALTER ROUTINE privilege is required to drop a procedure. When the stored procedure is dropped, the server also automatically revokes these privileges from the creator. If automatic sp privileges is 0, the server _ _ does not automatically grant or revoke these privileges. |   |   |   |   |
| avoid temporal u _ _ pgrade | 8.0, 5.7 | OFF | [ON\|OFF] |   | No | This variable controls whether ALTER TABLE implicitly upgrades temporal columns (TIME, DATETIME, and TIMESTAMP columns that do not support fractional seconds precision) that are in a pre-5.6.4 format. Upgrading such columns requires the table to be rebuilt, which prevents the use of fast alteration methods for the operation. |   |   |   |   |
| back log _ | 8.0, 5.7 | 300 0 | [0-65535] |   | Yes | The number of outstanding connection requests that MySQL can have. |   |   |   |   |
| binlog cache size _ _ | 8.0, 5.7 | 209 715 2 | [4096- 16777216] |   | No | The size of the cache that holds changes to the binary log for a transaction. |   |   |   |   |

| binlog checksum _ | 8.0, 5.7 | CRC 32 | [CRC32\|NO NE] | Yes | The type of BINLOG CHECKSUM ALG. _ _ Includes a checksum for log events in the binary log. Possible values are NONE and CRC32. The default value is CRC32. |
|---|---|---|---|---|---|
| binlog order com _ _ mits | 8.0, 5.7 | ON | [ON\|OFF] | No | When this variable is enabled on the primary server (the default), transactions are externalized in the same order as they are written to the binary log. If disabled, transactions can be committed in parallel. In some cases, disabling this variable may result in a performance increase. |
| binlog row imag _ _ e | 8.0, 5.7 | full | [full\|minim al] | No | Specifies whether the binary log saves all columns or only the required columns in the binary log image. |
| binlog rows quer _ _ y log events _ _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | The binlog rows query log events _ _ _ _ system variable affects only row-based logging. When enabled, it causes the MySQL Server to write informational log events, such as row query log events, to its binary log. This information can be used for debugging and related purposes. For example, you can obtain the original query issued on the primary server when it cannot be reconstructed from the row updates. |
| binlog stmt cach _ _ e size _ | 8.0, 5.7 | 327 68 | [4096- 16777216] | No | The size of the statement cache for non- transactional storage engines that update the binary log. |
| block encryption _ mode _ | 8.0, 5.7 | "aes - 128- ecb" | ["aes-128- ecb"\|"aes- 192- ecb"\|"aes- 256- ecb"\|"aes- 128- cbc"\|"aes- 192- cbc"\|"aes- 256-cbc"] | No | This variable controls the block encryption mode for block-based algorithms such as AES. It affects the encryption for AES ENCRYPT() and _ AES DECRYPT(). _ |

| bulk insert buffe _ _ r size _ | 8.0, 5.7 | 419 430 4 | [0- 42949672 95] | No | MyISAM uses a special tree-like cache to make bulk inserts such as INSERT... SELECT, INSERT... VALUES (...), (...), ..., and LOAD DATA INFILE faster when adding data to non-empty tables. This variable limits the size of the cache tree in bytes per thread. Setting it to 0 disables this optimization. The default value is 8 MB. |
|---|---|---|---|---|---|
| character set file _ _ system | 8.0, 5.7 | bina ry | [utf8\|latin1 \|gbk\|binary ] | No | The file system character set. This variable is used to interpret string literals that refer to file names, such as in the LOAD DATA INFILE and SELECT...INTO OUTFILE statements and the LOAD FILE() function. These file _ names are converted from character set client to _ _ character set filesystem before the file _ _ is opened. The default value is binary, which means no conversion occurs. For systems that allow multi-byte file names, a different value may be more appropriate. For example, if your system uses UTF-8 to represent file names, set character set filesystem to 'utf8'. _ _ |
| character set ser _ _ ver | 8.0, 5.7 | utf8 | [utf8\|latin1 \|gbk\|gb18 030\|utf8m b4] | Yes | The default character set for the server. |
| collation server _ | 8.0 | utf8 gen _ eral ci _ | [utf8 gene _ ral ci\|utf8 _ mb4 0900 _ ai ci\|utf8 _ _ mb4 gener _ al ci] _ | Yes | The collation for the character set. Modify this parameter with caution. An incompatibility with the character set server parameter will _ _ cause the instance to fail to start. |

| concurrent insert _ | 8.0, 5.7 | 1 | [0\|1\|2] | No | 0: Disables concurrent inserts. 1: (Default) Enables concurrent inserts for MyISAM tables that have no holes. 2: Enables concurrent inserts for all MyISAM tables, even if they have holes. For tables with holes, new rows are inserted at the end of the table if the table is being used by another thread. Otherwise, MySQL acquires a normal write lock and inserts the row into a hole. |
|---|---|---|---|---|---|
| connect timeout _ | 8.0, 5.7 | 10 | [1-3600] | No | The number of seconds that the mysqld server waits for a connection packet before responding with a Bad handshake error. The default value is 5 seconds for MySQL 5.1.23 and earlier, and 10 seconds thereafter. If clients frequently encounter errors such as "Lost connection to MySQL server at 'XXX', system error: errno", increasing the connect timeout value may help. _ |
| default storage e _ _ ngine | 8.0, 5.7 | Inno DB | [InnoDB\|in nodb] | Yes | The default storage engine for new tables. |
| default time zon _ _ e | 8.0, 5.7 | SYS TEM | [SYSTEM\|- 12:00\|- 11:00\|- 10:00\|- 9:00\|- 8:00\|- 7:00\|- 6:00\|- 5:00\|- 4:00\|- 3:00\|- 2:00\|- 1:00\|\+0:0 0\|\+1:00\|\ +2:00\|\+3: 00\|\+4:00\| \+5:00\|\+5 :30\|\+5:45 \|\+6:00\|\+ 6:30\|\+7:0 0\|\+8:00\|\ +9:00\|\+1 0:00\|\+11: 00\|\+12:00 \|\+13:00] | Yes | The default time zone for the database. |

| default week for _ _ mat | 8.0, 5.7 | 0 | [0-7] | No | The default mode value for the WEEK() function. |
|---|---|---|---|---|---|
| delay key write _ _ | 8.0, 5.7 | ON | [ON\|OFF\|A LL] | No | This option applies only to MyISAM tables. It can have one of the following values to affect how the DELAY KEY WRITE table option, which _ _ can be used in CREATE TABLE statements, is handled. OFF: The DELAY KEY WRITE option is _ _ ignored. ON: MySQL honors any DELAY KEY WRITE option specified in a _ _ CREATE TABLE statement. This is the default value. ALL: All newly opened tables are treated as if they were created with the DELAY KEY WRITE option enabled. _ _ Important If you set this variable to ALL, you should not use the MyISAM tables from other programs, such as another MySQL server or myisamchk. Doing so can cause index corruption. |
| delayed insert li _ _ mit | 8.0, 5.7 | 100 | [1- 42949672 95] | No | After inserting delayed insert limit _ _ delayed rows, the INSERT DELAYED handler thread checks for any pending SELECT statements. If there are any, it allows them to execute before continuing to insert delayed rows. |
| delayed insert ti _ _ meout | 8.0, 5.7 | 300 | [1-3600] | No | The number of seconds an INSERT DELAYED handler thread should wait for INSERT statements before terminating. |
| delayed queue si _ _ ze | 8.0, 5.7 | 100 0 | [1- 42949672 95] | No | This is the limit on the number of rows to be queued per table when handling INSERT DELAYED statements. If the queue becomes full, any client that issues an INSERT DELAYED statement must wait until there is space in the queue again. |
| disconnect on ex _ _ pired password _ | 8.0, 5.7 | ON | [ON\|OFF] | Yes | This variable controls how the server handles clients with expired passwords. |

| div precision incr _ _ ement | 8.0, 5.7 | 4 | [0-30] | No | This variable indicates how many digits the scale of the result of a division operation performed with the / operator should be increased. The default value is 4. The minimum and maximum values are 0 and 30, respectively. |
|---|---|---|---|---|---|
| end markers in j _ _ _ son | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether the optimizer JSON output should add end markers. |
| eq range index _ _ _ dive limit _ | 8.0, 5.7 | 100 | [0- 42949672 95] | No | If the number of equality ranges for an index is greater than or equal to this number, the optimizer uses existing index statistics instead of performing an index dive. If set to 0, index dives are always used. |
| event scheduler _ | 8.0 | OFF | [ON\|OFF] | No | Enables the Event Scheduler. Possible values are ON, OFF, and DISABLED (which deactivates the Event Scheduler completely and prevents it from being activated at runtime). |
| explicit defaults _ _ for timestamp _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether the default value for a TIMESTAMP column is the current timestamp. |
| flush time _ | 8.0, 5.7 | 0 | [0- 31536000] | No | If set to a non-zero value, all tables are closed every flush time seconds to free _ up resources and synchronize unflushed data to disk. This option is best used only on systems with minimal resources. |
| ft max word len _ _ _ | 8.0, 5.7 | 84 | [10- 42949672 95] | Yes | The maximum length of a word to be included in a MyISAM FULLTEXT index. |
| ft min word len _ _ _ | 8.0, 5.7 | 4 | [1-3600] | Yes | The minimum length of a word to be included in a FULLTEXT index. |
| ft query expansi _ _ on limit _ | 8.0, 5.7 | 20 | [0-1000] | Yes | The number of top N matches to use when performing a full-text search with WITH QUERY EXPANSION. |
| general log _ | 8.0, 5.7 | OFF | [ON\|OFF] | Yes | Specifies whether the general query log is enabled. The destination for log output is controlled by the log output system _ variable. |

| group concat ma _ _ x len _ | 8.0, 5.7 | 102 4 | [4- 18446744 07370954 752] | No | The maximum result length in bytes allowed for the GROUP CONCAT() _ function. The default value is 1024 bytes. |
|---|---|---|---|---|---|
| host cache size _ _ | 8.0, 5.7 | 644 | [0-65535] | No | The size of the internal host cache. Setting the size to 0 disables the host cache. Changing the cache size at runtime implicitly causes a FLUSH HOSTS operation to clear the host cache and truncate the host cache table. _ |
| innodb adaptive _ _ flushing | 8.0, 5.7 | ON | [ON\|OFF] | No | Determines whether to dynamically adjust the rate of flushing dirty pages in the InnoDB buffer pool based on the workload. The purpose of dynamically adjusting the flush rate is to avoid bursts of I/O activity. |
| innodb adaptive _ _ flushing lwm _ | 8.0, 5.7 | 10 | [0-70] | No | Defines a low watermark, representing a percentage of redo log capacity, at which adaptive flushing is enabled. |
| innodb adaptive _ _ hash index _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | innodb adaptive hash index is a _ _ _ parameter of the InnoDB storage engine used to enable or disable the adaptive hash index. |
| innodb adaptive _ _ max sleep delay _ _ | 8.0, 5.7 | 150 000 | [1- 1000000] | No | innodb thread sleep delay controls how _ _ _ long an InnoDB thread sleeps when there are no waiting events. This parameter allows InnoDB to automatically adjust the value of innodb thread sleep delay based on the _ _ _ current workload to adapt to different load situations. As long as this value is not 0, automatic dynamic adjustment of the innodb thread sleep delay value is _ _ _ enabled, with the maximum value specified by the innodb adaptive max sleep delay _ _ _ _ option. The value is in microseconds. This option can be very useful in busy systems, especially those with more than 16 InnoDB threads. In practice, this option is most valuable in MySQL systems with hundreds or thousands of concurrent connections. |
| innodb autoexte _ nd increment _ | 8.0, 5.7 | 64 | [1-1000] | No | The increment size in megabytes for increasing the size of an auto-extending InnoDB system tablespace file when it becomes full. The default value is 64. |

| innodb autoinc l _ _ ock mode _ | 8.0, 5.7 | 2 | [0\|1\|2] | Yes | The lock mode used for generating auto- increment values. The allowed values are: 0: traditional 1: consecutive 2: interleaved |
|---|---|---|---|---|---|
| innodb buffer po _ _ ol dump at shut _ _ _ down | 8.0, 5.7 | ON | [ON\|OFF] | No | Specifies whether to record the pages cached in the InnoDB buffer pool when the MySQL server is shut down, to shorten the warm-up process at the next restart. It is typically used with innodb buffer pool load at startup. The _ _ _ _ _ innodb buffer pool dump pct option _ _ _ _ defines the percentage of most recently used buffer pool pages to be dumped. |
| innodb buffer po _ _ ol dump pct _ _ | 8.0, 5.7 | 25 | [1-100] | No | Specifies the percentage of most recently used pages to read and dump for each buffer pool. The value range is 1 to 100. The default value is 25. For example, if there are 4 buffer pools, each with 100 pages, and innodb buffer pool dump pct is set to _ _ _ _ 25, the 25 most recently used pages from each buffer pool will be dumped. |
| innodb buffer po _ _ ol instances _ | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 8)} | [1-64] | Yes | The number of regions that the InnoDB buffer pool is divided into. For systems with buffer pools in the multi-gigabyte range, dividing the buffer pool into separate instances can improve concurrency by reducing contention as different threads read and write to cached pages. Each page stored in or read from the buffer pool is randomly assigned to one of the buffer pool instances using a hashing function. Each buffer pool instance manages its own free lists, flush lists, LRUs, and all other data structures connected to a buffer pool, and is protected by its own buffer pool mutex. |

| innodb buffer po _ _ ol load at startu _ _ _ p | 8.0, 5.7 | ON | [ON\|OFF] | Yes | Specifies whether to automatically warm up the buffer pool at MySQL server startup by loading the same pages that were previously saved in the InnoDB buffer pool. It is typically used with innodb buffer pool dump at shutdown. _ _ _ _ _ |
|---|---|---|---|---|---|
| innodb change b _ _ uffering | 8.0, 5.7 | all | [none\|inser ts\|deletes\| changes\|p urges\|all] | No | Specifies whether InnoDB performs change buffering, an optimization that delays write operations to secondary indexes so that I/O operations can be performed sequentially. |
| innodb change b _ _ uffer max size _ _ | 8.0, 5.7 | 25 | [0-50] | No | The maximum size of the InnoDB change buffer as a percentage of the total size of the buffer pool. You may need to increase this value for MySQL servers with heavy insert, update, and delete activity, or decrease it for MySQL servers with unchanging data used for reporting. |
| innodb checksu _ m algorithm _ | 8.0, 5.7 | crc3 2 | [innodb\|crc 32\|none\|st rict innodb _ \|strict crc3 _ 2\|strict no _ ne] | No | Specifies how to generate and verify checksums stored in the disk blocks of InnoDB tablespaces. |
| innodb cmp per _ _ _ index enabled _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Enables compression-related statistics per index in the INFORMATION SCHEMA.INNODB CMP PE _ _ _ R INDEX table. Because the collection of _ these statistics can be expensive, enable this option only on development, test, or secondary instances during performance tuning related to InnoDB compressed tables. |
| innodb commit c _ _ oncurrency | 8.0, 5.7 | 0 | [0-1000] | Yes | The number of threads that can commit at the same time. A value of 0 (the default) allows any number of transactions to commit concurrently. |

| innodb compress _ ion failure thresh _ _ old pct _ | 8.0, 5.7 | 5 | [0-100] | No | Defines the compression failure rate threshold for a table, as a percentage, at which MySQL starts adding padding in compressed pages to avoid expensive compression failures. When this threshold is exceeded, MySQL begins to leave extra free space in each new compressed page, dynamically adjusting the amount of free space up to a percentage of the page size specified by innodb compression pad pct max. A _ _ _ _ value of zero disables the mechanism for monitoring compression efficiency and dynamically adjusting the padding amount. |
|---|---|---|---|---|---|
| innodb compress _ ion level _ | 8.0, 5.7 | 6 | [0-9] | No | Specifies the zlib compression level for InnoDB compressed tables and indexes. Higher values allow you to fit more data onto storage devices but incur more CPU overhead during compression. Lower values can reduce CPU overhead when storage space is not critical or you expect the data to be not particularly compressible. |
| innodb compress _ ion pad pct max _ _ _ | 8.0, 5.7 | 50 | [0-70] | No | Specifies the maximum percentage of free space that can be reserved within each compressed page to provide space for data and modification logs to be reorganized within the page when a compressed table or index is updated and the data may need to be recompressed. This applies only when innodb compression failure threshold p _ _ _ _ ct is set to a non-zero value and the compression failure rate exceeds the cutoff point. |
| innodb concurre _ ncy tickets _ | 8.0, 5.7 | 500 0 | [1- 42949672 95] | No | Determines the number of threads that can enter InnoDB concurrently. A thread is placed in a queue when it tries to enter InnoDB if the number of threads has reached the concurrency limit. When a thread is permitted to enter InnoDB, it is given a number of "tickets" equal to the value of innodb concurrency tickets, _ _ and the thread can enter and leave InnoDB freely until it has used up its tickets. After that, the thread is again subject to the concurrency check (and possible queuing) the next time it tries to enter InnoDB. The default value is 5000. |
| innodb data file _ _ _ purge | 8.0 | ON | [ON\|OFF] | No | Specifies whether to enable the asynchronous file deletion mechanism. |

| innodb data file _ _ _ purge interval _ | 8.0 | 100 | [0-10000] | No | The interval for purging files, in milliseconds. |
|---|---|---|---|---|---|
| innodb data file _ _ _ purge max size _ _ | 8.0 | 128 | [16- 10737418 24] | No | The maximum number of files to purge per operation, in MB. |
| innodb deadlock _ _ detect | 8.0, 5.7 | ON | [ON\|OFF] | No | This option is used to disable deadlock detection. In high-concurrency systems, deadlock detection can cause a slowdown when many threads are waiting for the same lock. Sometimes, it may be more efficient to disable deadlock detection and rely on the innodb lock wait timeout setting for _ _ _ transaction rollback. |
| innodb disable s _ _ ort file cache _ _ | 5.7 | ON | [ON\|OFF] | No | If enabled, disables page caching when InnoDB uses sort files. |
| innodb flush met _ _ hod | 8.0, 5.7 | O DI _ REC T | [fsync\|O D _ SYNC\|little sync\|nosyn c\|O DIREC _ T\|O DIREC _ T NO FSY _ _ NC] | Yes | Defines the method used to flush data to InnoDB data files and log files, which can affect I/O throughput. |
| innodb flush nei _ _ ghbors | 8.0, 5.7 | 0 | [0\|1\|2] | No | Specifies whether flushing a page from the InnoDB buffer pool also flushes other dirty pages in the same extent. |
| innodb flush syn _ _ c | 8.0, 5.7 | ON | [ON\|OFF] | No | The innodb flush sync parameter is _ _ enabled by default, which causes the innodb io capacity setting to be ignored _ _ during bursts of I/O activity at checkpoints. To adhere to the InnoDB background I/O activity limit defined by the innodb io capacity setting, disable _ _ innodb flush sync. _ _ |
| innodb ft cache _ _ _ size | 8.0, 5.7 | 800 000 0 | [1600000- 80000000] | Yes | The memory allocated for the InnoDB FULLTEXT search index cache, in bytes, which holds parsed documents in memory when an InnoDB FULLTEXT index is created. Index insertions and updates are committed to disk only when the innodb ft cache size limit is _ _ _ reached. innodb ft cache size defines _ _ _ the cache size on a per-table basis. |

| innodb ft enable _ _ diag print _ _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether to enable additional full-text search (FTS) diagnostic output. This option is primarily for advanced FTS debugging and is not of interest to most users. The output is printed to the error log and includes informational messages. |
|---|---|---|---|---|---|
| innodb ft enable _ _ stopword _ | 8.0, 5.7 | ON | [ON\|OFF] | No | When creating an InnoDB FULLTEXT index, specifies a set of stopwords to associate with it. If the innodb ft user stopword table option is _ _ _ _ set, stopwords are taken from that table. Otherwise, if the innodb ft server stopword table option _ _ _ _ is set, stopwords are taken from that table. Otherwise, the built-in default set of stopwords is used. |
| innodb ft max to _ _ _ ken size _ | 8.0, 5.7 | 84 | [10-84] | Yes | The maximum length of a word stored in an InnoDB FULLTEXT index. |
| innodb ft min to _ _ _ ken size _ | 8.0, 5.7 | 3 | [0-16] | Yes | The minimum length of a word stored in an InnoDB FULLTEXT index. |
| innodb ft num w _ _ _ ord optimize _ | 8.0, 5.7 | 200 0 | [0-10000] | No | The number of words to process for each OPTIMIZE TABLE operation on an InnoDB FULLTEXT index. Because a large-volume insert or update operation on a table with a full-text search index can require significant index maintenance to merge all changes, you might perform a series of OPTIMIZE TABLE statements, each one continuing where the previous one left off. |
| innodb ft result _ _ _ cache limit _ | 8.0, 5.7 | 200 000 000 0 | [1000000- 42949672 95] | No | The InnoDB full-text search query result cache limit in bytes, per full-text search query or per thread. Intermediate and final InnoDB full-text search query results are processed in memory. Use innodb ft result cache limit to set a size _ _ _ _ limit on the full-text search query result cache to avoid excessive memory consumption in the event of very large InnoDB full-text search query results, such as millions or hundreds of millions of rows. Memory is allocated as needed while processing a full-text search query. If the result cache size limit is reached, an error is returned indicating that the query exceeded the maximum allowed memory. |

| innodb ft sort pll _ _ _ degree _ | 8.0, 5.7 | 2 | [1-16] | Yes | The number of threads used for parallel indexing and tokenizing of text in an InnoDB FULLTEXT index when building the search index. |
|---|---|---|---|---|---|
| innodb ft total c _ _ _ ache size _ | 8.0, 5.7 | 640 000 000 | [32000000 - 16000000 00] | Yes | The total memory allocated for the InnoDB full-text search index cache for all tables, in bytes. Creating multiple tables with FULLTEXT search indexes can consume a significant portion of available memory. innodb ft total cache size defines a _ _ _ _ global memory limit for all full-text search indexes to help avoid excessive memory consumption. If an index operation reaches the global limit, a forced synchronization is triggered. |
| innodb io capacit _ _ y | 8.0, 5.7 | 200 00 | [0- 18446744 07370955 1615] | No | The innodb io capacity parameter sets _ _ an upper limit on the number of I/O operations per second performed by InnoDB background tasks, such as flushing pages from the buffer pool and merging data from the change buffer. |
| innodb io capacit _ _ y max _ | 8.0, 5.7 | 400 00 | [0- 18446744 07370955 1615] | No | If flushing activity falls behind, InnoDB can flush at a higher rate than what innodb io capacity enforces. In this case, _ _ innodb io capacity max defines an _ _ _ upper limit on the number of I/O operations per second performed by InnoDB background tasks. |
| innodb large pre _ _ fix | 5.7 | OFF | [ON\|OFF] | No | Enabling this option allows index key prefixes to be longer than 767 bytes (up to 3072 bytes) for InnoDB tables that use the DYNAMIC and COMPRESSED row formats. |
| innodb lock wait _ _ timeout _ | 8.0, 5.7 | 50 | [1- 10737418 24] | No | The timeout in seconds an InnoDB transaction waits for a row lock before giving up. The default value is 50 seconds. |
| innodb log check _ _ sums | 8.0, 5.7 | ON | [ON\|OFF] | No | Enables or disables checksums for redo log pages. innodb log checksums _ _ replaces innodb log checksum algorithm. _ _ _ |
| innodb log comp _ _ ressed pages _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether images of re- compressed pages are written to the redo log. Re-compression can occur when changes are made to compressed data. |

| innodb log file si _ _ _ ze | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/6, 157 286 400 0)} | [4194304- 10737418 2400] | Yes | Defines the size in bytes of each log file in a log group. |
|---|---|---|---|---|---|
| innodb lru scan _ _ _ depth | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76/8 , 819 2)} | [100- 18446744 07370955 1615] | No | A parameter that influences the algorithm and heuristics for the flush operation of the InnoDB buffer pool. It is intended for performance experts who tune I/O-intensive workloads. It specifies how far down the buffer pool LRU page list the page cleaner thread scans for dirty pages to flush for each buffer pool instance. This is a background operation that is performed once per second. |
| innodb max dirty _ _ pages pct _ _ | 8.0, 5.7 | 75 | [0-99] | No | This is an integer in the range from 0 to 100. The default value is 90 for the built- in InnoDB and 75 for the InnoDB plugin. The main thread in InnoDB tries to write pages from the buffer pool so that the percentage of dirty (not yet written) pages does not exceed this value. |
| innodb max dirty _ _ pages pct lwm _ _ _ | 8.0, 5.7 | 10 | [0-99] | No | Defines a low watermark that represents a percentage of dirty pages at which pre-flushing is enabled to control the dirty page ratio. The default value of 0 disables pre-flushing behavior entirely. |
| innodb max purg _ _ e lag _ | 8.0, 5.7 | 0 | [0- 42949672 95] | No | Defines the maximum length of the purge queue. The default value of 0 means no limit (no delay). |

| innodb max purg _ _ e lag delay _ _ | 8.0, 5.7 | 0 | [0- 10000000] | No | Specifies the maximum delay in microseconds for the delay imposed by the innodb max purge lag configuration _ _ _ option. A non-zero value imposes an upper limit on the delay period based on a formula derived from the innodb max purge lag value. The _ _ _ default value of zero means no upper limit is imposed on the delay interval. |
|---|---|---|---|---|---|
| innodb max und _ _ o log size _ _ | 8.0, 5.7 | 107 374 182 4 | [10485760 - 18446744 07370955 1615] | No | Defines the threshold size for an undo tablespace. If an undo tablespace exceeds the threshold, it can be marked for truncation when innodb undo log truncate is enabled. _ _ _ The default value is 1073741824 bytes (1024 MiB). |
| innodb monitor _ _ disable | 8.0 | Non e | all | No | Disables InnoDB metrics counters. You can query counter data using the INFORMATION SCHEMA.INNODB METRIC _ _ S table. |
| innodb monitor e _ _ nable | 8.0 | Non e | all | No | Enables InnoDB monitor output. When enabled, InnoDB generates detailed runtime information that can be used for performance analysis and troubleshooting. You can view the output using the SHOW ENGINE INNODB STATUS command. |
| innodb old block _ _ s pct _ | 8.0, 5.7 | 37 | [5-95] | No | (InnoDB plugin only) Specifies the approximate percentage of the InnoDB buffer pool to be used for the old block sublist. The value range is 5 to 95. The default value is 37 (i.e., 3/8 of the pool). |

| innodb old block _ _ s time _ | 8.0, 5.7 | 100 0 | [0-1024] | No | (InnoDB plugin only) Specifies how long in milliseconds a block inserted into the old sublist must stay there after its first access before it can be moved to the new sublist. The default value is 0: a block inserted into the old sublist moves immediately to the new sublist on its first access, regardless of how long after insertion the access occurs. If the value is greater than 0, blocks remain in the old sublist until an access occurs at least that many milliseconds after the first access. Unit: milliseconds. |
|---|---|---|---|---|---|
| innodb online alt _ _ er log max size _ _ _ | 8.0, 5.7 | 134 217 728 | [13421772 8- 21474836 47] | No | The maximum size of the modification log file for online index creation. |
| innodb open files _ _ | 8.0, 5.7 | {LE AST( DBIn stan ceCl assC PU* 500, 800 0)} | [1-8192] | Yes | This variable is relevant only when using multiple InnoDB tablespaces. It specifies the maximum number of .ibd files that MySQL can keep open at one time. |
| innodb optimize _ _ fulltext only _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Changes how OPTIMIZE TABLE operates on InnoDB tables, to be temporarily enabled during maintenance operations on InnoDB tables that have a FULLTEXT index. |

| innodb page cle _ _ aners | 8.0, 5.7 | {MI N(In stan ceM emo ryIn GB, 8)} | [1-64] | Yes | The number of page cleaner threads that flush dirty pages from buffer pool instances. Page cleaner threads perform flush list and LRU flushing. A single page cleaner thread was introduced in MySQL 5.6 to offload buffer pool flushing work from the InnoDB main thread. In MySQL 5.7, InnoDB provides support for multiple page cleaner threads. A value of 1 maintains the pre-MySQL 5.7 configuration, where there is one page cleaner thread. When there are multiple page cleaner threads, buffer pool flushing tasks for each buffer pool instance are dispatched to idle page cleaner threads. In MySQL 5.7, the default value of innodb page cleaners _ _ was changed from 1 to 4. If the number of page cleaner threads exceeds the number of buffer pool instances, extra threads will be idle and will not consume CPU resources. The innodb page cleaners variable is _ _ dynamic and can be changed online. |
|---|---|---|---|---|---|
| innodb print all _ _ _ deadlocks | 8.0, 5.7 | OFF | [OFF\|ON] | No | Prints all deadlock information to the MySQL error log (off by default). |
| innodb purge ba _ _ tch size _ | 8.0, 5.7 | 300 | [1-5000] | Yes | Represents the granularity of the change that triggers a purge operation (flushing changed buffer pool blocks to disk), in units of redo log records. |
| innodb purge rse _ _ g truncate frequ _ _ ency | 8.0, 5.7 | 128 | [1-128] | No | Defines the frequency at which the purge system releases rollback segments as a number of times purge is invoked. The undo tablespace cannot be truncated until the rollback segments are released. Typically, the purge system releases rollback segments every 128 times purge is invoked. The default value is 128. Decreasing this value increases the frequency at which the purge thread releases rollback segments. |
| innodb purge thr _ _ eads | 8.0, 5.7 | {MI N(In stan ceM emo ryIn GB, 8)} | [1-32] | Yes | The number of background threads dedicated to InnoDB purge operations. |

| innodb random r _ _ ead ahead _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Enables the random read-ahead technique to optimize InnoDB I/O. |
|---|---|---|---|---|---|
| innodb read ahe _ _ ad threshold _ | 8.0, 5.7 | 56 | [0-1024] | No | (InnoDB plugin only) Controls the sensitivity of InnoDB for linear read- ahead, which is used to prefetch pages into the buffer pool. If InnoDB reads at least innodb read ahead threshold _ _ _ pages sequentially from an extent (64 pages), it initiates an asynchronous read of the entire subsequent extent. |
| innodb read io t _ _ _ hreads | 8.0, 5.7 | 4 | [1-64] | Yes | (InnoDB plugin only) The number of I/O threads for InnoDB read operations. The default value is 4. |
| innodb rollback _ _ on timeout _ | 8.0, 5.7 | OFF | [OFF\|ON] | Yes | By default, InnoDB rolls back only the last statement on a transaction timeout. If --innodb rollback on timeout is _ _ _ specified, a transaction timeout causes InnoDB to abort and roll back the entire transaction (the same behavior as in MySQL 4.1). This variable was added in MySQL 5.1.15. |
| innodb rollback s _ _ egments | 8.0, 5.7 | 128 | [1-128] | No | Defines the number of rollback segments used by InnoDB. |
| innodb sort buffe _ _ r size _ | 8.0, 5.7 | 104 857 6 | [65536- 67108864] | Yes | Specifies the size of the sort buffer used for sorting data during the creation of an InnoDB index. The specified size defines the amount of data read into memory for internal sorting and then written out to disk. This process is called a "run". During the merge phase, a pair of buffers of the specified size are read and merged. A larger setting results in fewer runs and merges. |
| innodb spin wait _ _ delay _ | 8.0, 5.7 | 6 | [0- 42949672 95] | No | The maximum delay for a spin-lock poll. The underlying implementation of this mechanism varies by hardware and operating system combination, so the delay does not correspond to a fixed time interval. |

| innodb stats aut _ _ o recalc _ | 8.0, 5.7 | ON | [ON\|OFF] | No | Causes InnoDB to automatically recalculate persistent statistics after a significant change in the data in a table. The threshold is 10% of the number of rows in the table. This setting applies to tables created when the innodb stats persistent option is _ _ enabled. You can also configure automatic statistics recalculation by specifying STATS PERSISTENT = 1 in a _ CREATE TABLE or ALTER TABLE statement. The amount of sampled data for generating statistics is controlled by the innodb stats persistent sample pages _ _ _ _ configuration option. |
|---|---|---|---|---|---|
| innodb stats met _ _ hod | 8.0, 5.7 | nulls equ _ al | [nulls equ _ al\|nulls un _ equal\|nulls ignored] _ | No | How the server treats NULL values when collecting statistics on the distribution of index values for an InnoDB table. This variable has three possible values: nulls equal, nulls unequal, and _ _ nulls ignored. For nulls equal, all NULL _ _ index values are considered equal and form a single value group of a size equal to the number of NULL values. For nulls unequal, NULL values are _ considered unequal, and each NULL forms a distinct value group of size 1. For nulls ignored, NULL values are _ ignored. |
| innodb stats on _ _ _ metadata | 8.0, 5.7 | OFF | [ON\|OFF] | No | This option applies only when optimizer statistics are configured to be non- persistent. Optimizer statistics are not persisted to disk when innodb stats persistent is disabled or _ _ when individual tables are created or altered with stats persistent=0. _ |

| innodb stats per _ _ sistent | 8.0, 5.7 | ON | [ON\|OFF] | No | Specifies whether InnoDB index statistics are persisted to disk. Otherwise, statistics may be recalculated frequently, which can lead to changes in query execution plans. This setting is stored with each table when it is created. You can set innodb stats persistent at a global level _ _ before creating a table, or use the STATS PERSISTENT clause of the _ CREATE TABLE and ALTER TABLE statements to override the system-wide setting and configure persistent statistics for individual tables. |
|---|---|---|---|---|---|
| innodb stats per _ _ sistent sample p _ _ ages | 8.0, 5.7 | 20 | [0- 42949672 95] | No | The number of index pages to sample when estimating cardinality and other statistics for an index column, such as those calculated by ANALYZE TABLE. Increasing this value can improve the accuracy of index statistics, which can lead to better query execution plans, but increases the I/O load during the execution of ANALYZE TABLE for an InnoDB table. |
| innodb stats sa _ _ mple pages _ | 5.7 | 8 | [1- 42949672 96] | No | (InnoDB plugin only) The number of index pages used for index distribution statistics, such as those calculated by ANALYZE TABLE. The default value is 8. |
| innodb stats tran _ _ sient sample pag _ _ es | 8.0, 5.7 | 8 | [1- 42949672 95] | No | The number of index pages to sample when estimating cardinality and other statistics for an index column, such as those calculated by ANALYZE TABLE. The default value is 8. Increasing this value can improve the accuracy of index statistics, which can lead to better query execution plans, but increases the I/O load when opening an InnoDB table or recalculating statistics. |
| innodb status ou _ _ tput | 8.0, 5.7 | OFF | [ON\|OFF] | No | Enables or disables periodic output from the standard InnoDB Monitor. It is also used in conjunction with innodb status output locks to enable or _ _ _ disable periodic output from the InnoDB Lock Monitor. |

| innodb status ou _ _ tput locks _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Enables or disables the InnoDB Lock Monitor. When enabled, the InnoDB Lock Monitor prints additional information about locks in the SHOW ENGINE INNODB STATUS output and in periodic output printed to the MySQL error log. The periodic output of the InnoDB Lock Monitor is printed as part of the standard InnoDB Monitor output. Therefore, the standard InnoDB Monitor must be enabled for the InnoDB Lock Monitor to periodically print data to the MySQL error log. |
|---|---|---|---|---|---|
| innodb strict mo _ _ de | 8.0, 5.7 | OFF | [ON\|OFF] | No | (InnoDB plugin only) Specifies whether InnoDB returns errors instead of warnings for certain conditions, similar to strict SQL mode. The default value is OFF. For a list of affected conditions, see InnoDB Strict Mode. |
| innodb sync arra _ _ y size _ | 8.0, 5.7 | 128 | [1-1024] | Yes | Defines the size of the mutex/lock wait array. Increasing this value splits the internal data structure used for coordinating threads, which can improve concurrency for workloads with many waiting threads. This setting must be configured at MySQL instance startup and cannot be changed afterward. It is recommended to increase this value for workloads that frequently produce many waiting threads, typically greater than 768. |
| innodb sync spin _ _ loops _ | 8.0, 5.7 | 8. 0: 1 0 0 5. 7: 3 0 | [0- 42949672 95] | No | The number of times a thread waits for an InnoDB mutex to be released before the thread is suspended. |
| innodb table loc _ _ ks | 8.0, 5.7 | ON | [ON\|OFF] | No | If autocommit = 0, InnoDB honors LOCK TABLES; MySQL does not return from LOCK TABLES ... WRITE until all other threads have released their locks on the table. The default value of innodb table locks is 1, which means _ _ that if autocommit = 0, LOCK TABLES causes InnoDB to lock the table internally. |

| innodb thread co _ _ ncurrency | 8.0, 5.7 | 0 | [0-1000] | No | InnoDB tries to keep the number of operating system threads running concurrently within InnoDB less than or equal to the limit given by this variable. Once the number of threads reaches this limit, additional threads are placed in a waiting state, queued for execution (FIFO queue). |
|---|---|---|---|---|---|
| innodb thread sl _ _ eep delay _ | 8.0, 5.7 | 100 00 | [0- 1000000] | No | The time in microseconds (usec) that an InnoDB thread sleeps before joining the InnoDB queue. A value of 0 disables sleep. |
| innodb undo log _ _ _ truncate | 5.7 | OFF | [ON\|OFF] | No | When enabled, undo tablespaces that exceed the threshold defined by innodb max undo log size are marked _ _ _ _ for truncation. |
| innodb write io t _ _ _ hreads | 8.0, 5.7 | 4 | [1-64] | Yes | (InnoDB plugin only) The number of I/O threads for write operations in InnoDB. The default value is 4. |
| interactive timeo _ ut | 8.0, 5.7 | 720 0 | [10-86400] | No | The number of seconds the server waits for activity on an interactive connection before closing it. An interactive client is defined as a client that connects to mysql real connect() using the _ _ CLIENT INTERACTIVE option. _ Unit: seconds. |
| join buffer size _ _ | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76* 128, 262 144) } | [128- 42949672 95] | No | The minimum size of the buffer used for plain index scans, range index scans, and joins that do not use indexes and thus perform full table scans. |
| key cache age t _ _ _ hreshold | 8.0, 5.7 | 300 | [100- 42949672 95] | No | This value controls the demotion of buffers from the hot sublist to the warm sublist of the key cache. A lower value causes demotion to happen faster. The minimum value is 100. The default value is 300. Unit: seconds. |

| key cache block _ _ _ size | 8.0, 5.7 | 102 4 | [512- 16384] | No | The size in bytes of blocks in the key cache. The default value is 1024. Unit: bytes. |
|---|---|---|---|---|---|
| key cache divisio _ _ n limit _ | 8.0, 5.7 | 100 | [1-100] | No | The division point between the hot and warm sublists of the key cache buffer list. The value is the percentage of the buffer list to be used for the warm sublist. The allowed value range is 1 to 100. The default value is 100. |
| lc time names _ _ | 8.0, 5.7 | en _ US | [ja JP\|pt B _ _ R\|en US] _ | No | This variable specifies the locale that controls the language used to display day and month names and abbreviations. This variable affects the output of the DATE FORMAT(), _ DAYNAME(), and MONTHNAME() functions. The locale name is a POSIX- style value, such as 'ja JP' or 'pt BR'. The _ _ default value is 'en US', regardless of _ the system's locale. |
| local infile _ | 8.0, 5.7 | ON | [ON\|OFF] | No | This variable controls the server-side LOCAL capability for LOAD DATA statements. |
| lock wait timeou _ _ t | 8.0, 5.7 | 315 360 00 | [1- 10737418 24] | No | This variable specifies the timeout in seconds for attempts to acquire metadata locks. The allowed value range is from 1 to 31536000 (1 year). The default value is 31536000. |
| log error verbosi _ _ ty | 8.0, 5.7 | 2 | [1-3] | No | The log error verbosity system variable _ _ specifies the verbosity level for handling events intended for the error log. |
| log queries not _ _ _ using indexes _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether to log queries that do not use indexes to the slow query log. |
| log slow admin s _ _ _ tatements | 8.0, 5.7 | OFF | [ON\|OFF] | No | Includes slow administrative statements among the statements written to the slow query log. |
| log throttle queri _ _ es not using ind _ _ _ exes | 8.0, 5.7 | 0 | [0- 42949672 95] | No | If log queries not using indexes is _ _ _ _ enabled, the log throttle queries not using indexes _ _ _ _ _ variable limits the number of such queries that can be written to the slow query log per minute. |

| long query time _ _ | 8.0, 5.7 | 1 | [0.1- 31536000] | No | If a query takes longer than this many seconds, the server increments the Slow queries status variable. If the slow _ query log is enabled, the query is logged to the slow query log file. Unit: seconds. |
|---|---|---|---|---|---|
| loose ccl queue _ _ _ bucket count _ | 8.0, 5.7 | 4 | [1-64] | No | The number of groups when using the CCL queue. |
| loose ccl queue _ _ _ bucket size _ | 8.0, 5.7 | 64 | [1-4096] | No | The maximum concurrency allowed when using the CCL queue. |
| loose ccl queue _ _ _ hot delete _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to enter the CCL queue for a single delete operation under certain conditions. |
| loose ccl queue _ _ _ hot update _ | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to enter the CCL queue for a single update operation under certain conditions. |
| loose collation s _ _ erver | 5.7 | utf8 gen _ eral ci _ | [utf8 bin\|u _ tf8 general _ ci\|latin1 b _ _ in\|latin1 g _ eneral ci\|g _ bk chinese _ ci\|gbk bin _ _ \|utf8mb4 _ general ci\| _ utf8mb4 bi _ n] | Yes | The default collation for the server. |
| loose connection _ control failed co _ _ _ nnections thresh _ old | 8.0 | 3 | [0- 21474836 47] | No | None. |
| loose connection _ control max con _ _ _ nection delay _ | 8.0 | 200 0 | [1000- 21474836 47] | No | None. |
| loose connection _ control min con _ _ _ nection delay _ | 8.0 | 100 0 | [1000- 21474836 47] | No | None. |

| loose ignore ind _ _ ex hint error _ _ | 8.0 | OFF | [ON\|OFF] | No | Controls whether to ignore index hint errors. |
|---|---|---|---|---|---|
| loose information _ schema stats e _ _ _ xpiry | 8.0 | 864 00 | [0- 31536000] | No | The number of seconds before the mysqld server retrieves data from the storage engine and replaces the data in the cache. |
| loose innodb dat _ _ a file purge _ _ | 5.7 | ON | [ON\|OFF] | No | Performs data file purging gradually. |
| loose innodb dat _ _ a file purge inter _ _ _ val | 5.7 | 100 | [0-10000] | No | The time interval in milliseconds between each data file purge operation. |
| loose innodb dat _ _ a file purge max _ _ _ size _ | 5.7 | 512 | [16- 10737418 24] | No | The maximum size in MB for each data file purge operation. |
| loose innodb log _ _ optimize ddl _ _ | 8.0, 5.7 | 8. 2: O N 5. 7: O FF | [ON\|OFF] | No | Reduces redo logging when creating an index or rebuilding a table locally. Setting this to OFF can avoid delays caused by page flushing and allow for concurrent backups. |
| loose innodb log _ _ write ahead siz _ _ _ e | 8.0 | 409 6 | [512- 16384] | No | The unit size for the write-ahead log to avoid read-on-write. It should match the OS cache block I/O size. |
| loose innodb nu _ _ ma interleave _ | 8.0, 5.7 | ON | [ON\|OFF] | Yes | Enables the NUMA interleaved memory policy for allocating the InnoDB buffer pool. When innodb numa interleave is _ _ enabled, the NUMA memory policy of the mysqld process is set to MPOL interleave. After the InnoDB buffer _ pool is allocated, the NUMA memory policy is set back to MPOL DEFAULT. For _ the innodb numa interleave option to be _ _ available, MySQL must be compiled on a NUMA-enabled Linux system. |
| loose innodb par _ _ allel read thread _ _ s | 8.0 | 1 | [0-256] | No | The number of threads for parallel reads. |
| loose innodb rds _ _ faster ddl _ _ | 8.0, 5.7 | ON | [ON\|OFF] | No | A feature switch for faster DDL. |

| loose innodb rds _ _ flashback task _ _ _ enabled | 8.0 | OFF | [ON\|OFF] | No | Specifies whether to roll forward new read views by default. |
|---|---|---|---|---|---|
| loose internal tm _ _ p disk storage e _ _ _ ngine | 5.7 | INN ODB | [INNODB\|M YISAM] | No | The storage engine for on-disk internal temporary tables. |
| loose innodb und _ _ o retention _ | 8.0 | 900 | [0- 42949672 95] | No | The retention period for undo records in seconds. Undo records older than this period cannot be queried. If `loose innodb rds flashback task enabl _ _ _ _ _ ed` is set to OFF, you must also set this parameter to 0. |
| loose innodb und _ _ o space reserved _ _ size _ | 8.0 | 0 | [0- 42949672 95] | No | The size of the reserved undo tablespace in MB. When the loose innodb undo retention parameter _ _ _ is non-zero, this space is used to retain as many undo records as possible. |
| loose innodb und _ _ o space supremu _ _ m size _ | 8.0 | 102 40 | [0- 42949672 95] | No | The maximum disk space that the undo tablespace can occupy, in MB. When the occupied space exceeds this value, the loose innodb undo retention parameter _ _ _ is ignored, and undo records are forcibly purged. |
| loose max execu _ _ tion time _ | 5.7 | 0 | [0- 42949672 95] | No | If the execution time exceeds this value, the statement execution is interrupted. |
| loose max state _ _ ment time _ | 5.7 | 0 | [0- 42949672 95] | No | If the execution time exceeds this value, the statement execution is interrupted. |
| loose multi block _ _ s ddl count _ _ | 8.0 | 0 | [0-1024] | No | The page number of multiple blocks at a time in some DDL queries. |
| loose opt rds en _ _ _ able show slave _ _ _ lag | 8.0, 5.7 | ON | [ON\|OFF] | No | If ON, the show slave lag command is allowed. |
| loose opt rds las _ _ _ t error gtid _ _ | 8.0, 5.7 | ON | [ON\|OFF] | No | If ON, displays Last SQL Error Gtid _ _ _ in the output of show slave status . |

| psaraDB RDS for M ide·Instances | ySQL Us | er G |   |   | ApsaraDB for RD |
|---|---|---|---|---|---|
| loose optimizer s _ _ witch | 5.7 | inde x m _ erge =on ,ind ex _ mer ge u _ nion =on ,ind ex _ mer ge s _ o rt u _ nion =on ,ind ex _ mer ge i _ nter secti on= on,e ngin e co _ n ditio n p _ ush dow n=o n,in dex _ con ditio n p _ ush dow n=o n,mr r =on ,mrr cos _ t ba _ sed =on ,bloc k ne _ sted loo _ p=o n,ba tche d | .* | No. | The optimizer switch parameter controls _ the optimizer behavior. |

|   |   | key _ acc _ ess =off ,mat erial izati on= on,s emij oin= on,l oo sesc an= on,fi rstm atch =on ,sub quer y m _ ateri aliza tion c _ ost _ base d=o n, use _ inde x ex _ tens ions =on |   |   |   |
|---|---|---|---|---|---|
| loose optimizer t _ _ race | 8.0, 5.7 | ena bled =off ,one line _ =off | .* | No | The optimizer trace system variable has _ these switch options: enabled and one line. _ |

| loose optimizer t _ _ race features _ | 8.0, 5.7 | gree dy s _ earc h=o n,ra nge _ opti mize r=o n,dy nam ic ra _ nge =on ,rep eate d su _ bsel ect =on | .* | No | Use the optimizer trace features system _ _ variable to exclude these features from the trail. |
|---|---|---|---|---|---|
| loose password _ _ history | 8.0 | 0 | [0-10] | No | None. |
| loose performanc _ e point iostat int _ _ _ erval | 5.7 | 2 | [0-60] | No | The collection interval for IO statistics, in milliseconds. |
| loose performanc _ e point iostat vol _ _ _ ume size _ | 5.7 | 100 00 | [0-100000] | Yes | The maximum capacity for collecting IO statistics, in slots. |
| loose performanc _ e point lock rwlo _ _ _ ck enabled _ | 5.7 | ON | [ON\|OFF] | No | Enables or disables the performance optimization feature for read/write locks. |
| loose performanc _ e schema accou _ _ nts size _ | 8.0, 5.7 | 100 00 | [-1, 1048576] | Yes | The number of rows in the accounts table. If this variable is 0, Performance Schema does not maintain connection statistics in the accounts table or status variable information in the status by account table. _ _ |
| loose performanc _ e schema digest _ _ s size _ | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of rows in the events statements summary by digest _ _ _ _ table. If this value is exceeded, Performance Schema cannot instrument the digests and increments the Performance schema digest lost status _ _ _ variable. |

| loose performanc _ e schema error _ _ _ size | 8.0 | 0 | [0- 1048576] | Yes | The number of detected server error codes. The default value is the actual number of server error codes. Although this value can be set to any number between 0 and the maximum, its intended use is to be set to the default value (to detect all errors) or 0 (to detect no errors). |
|---|---|---|---|---|---|
| loose performanc _ e schema hosts _ _ _ size | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the hosts table. If this variable is 0, Performance Schema does not maintain connection statistics in the hosts table or status variable information in the status by host table. _ _ |
| loose performanc _ e schema max c _ _ _ ond instances _ | 8.0, 5.7 | 10,0 00 | [-1, 1048576] | Yes | The maximum number of instrumented conditional objects. |
| loose performanc _ e schema max fi _ _ _ le instances _ | 8.0, 5.7 | 100 0 | [-1- 1048576] | Yes | The maximum number of instrumented file objects. |
| loose performanc _ e schema max i _ _ _ ndex stat _ | 8.0, 5.7 | 100 00 | [-1, 1048576] | Yes | The maximum number of indexes for which Performance Schema maintains performance statistics. If this maximum is exceeded, index statistics are lost. Performance Schema then increments the Performance schema index stat lost _ _ _ _ status variable. The default value is autosized based on the value of performance schema max table instanc _ _ _ _ es. |
| loose performanc _ e schema max _ _ _ metadata locks _ | 8.0, 5.7 | 10,0 00 | [-1- 1048576] | Yes | The maximum number of metadata locks that can be instrumented. This value controls the size of the metadata locks _ table. If a metadata lock cannot be instrumented because this maximum value is exceeded, Performance Schema increases the Performance schema metadata lock los _ _ _ _ t status variable. |
| loose performanc _ e schema max _ _ _ mutex instances _ | 8.0, 5.7 | 100 00 | [-1- 10485760 0] | Yes | The maximum number of instrumented mutex objects. |

| loose performanc _ e schema max p _ _ _ repared stateme _ nts instances _ | 8.0, 5.7 | 100 0 | [-1, 4194304] | Yes | The maximum number of rows in the prepared statements instances table. If _ _ a prepared statement cannot be instrumented because this maximum is exceeded, Performance Schema increases the Performance schema prepared stateme _ _ _ nts lost status variable. _ |
|---|---|---|---|---|---|
| loose performanc _ e schema max p _ _ _ rogram instances _ | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of stored programs for which Performance Schema maintains statistics. If this maximum is exceeded, Performance Schema increases the Performance schema program lost _ _ _ status variable. |
| loose performanc _ e schema max r _ _ _ wlock instances _ | 8.0, 5.7 | 100 00 | [-1- 10485760 0] | Yes | The maximum number of instrumented read/write lock (rwlock) objects. |
| loose performanc _ e schema max s _ _ _ ocket instances _ | 8.0, 5.7 | 100 0 | [-1, 1048576] | Yes | The maximum number of instrumented socket objects. |
| loose performanc _ e schema max t _ _ _ able handles _ | 8.0, 5.7 | 100 00 | [-1, 1,048,576] | Yes | The maximum number of open table objects. This value controls the size of the table handles table. If this maximum _ value is exceeded, Performance Schema cannot instrument the table handles. As a result, Performance Schema increases the Performance schema table handles lost _ _ _ _ status variable. |
| loose performanc _ e schema max t _ _ _ able instances _ | 8.0, 5.7 | 100 0 | [-1, 1048576] | Yes | The maximum number of instrumented table objects. |
| loose performanc _ e schema max t _ _ _ able lock stat _ _ | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of tables for which Performance Schema maintains table lock statistics. If table lock statistics are lost because this maximum value is exceeded, Performance Schema increments the `Performance schema table lock stat lo _ _ _ _ _ st` status variable. |

| loose performanc _ e schema max t _ _ _ hread instances _ | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The maximum number of instrumented thread objects. This value controls the size of the threads table. If a thread cannot be instrumented because this maximum value is exceeded, Performance Schema increases the Performance schema thread instances l _ _ _ _ ost status variable. |
|---|---|---|---|---|---|
| loose performanc _ e schema setup _ _ _ actors size _ | 8.0, 5.7 | 100 00 | [-1, 1048576] | Yes | Number of rows in the setup actors _ table. |
| loose performanc _ e schema setup _ _ _ objects size _ | 8.0, 5.7 | 100 00 | [-1- 1048576] | Yes | The number of rows in the setup objects _ table. |
| loose performanc _ e schema users _ _ _ size | 8.0, 5.7 | 100 00 | [-1, 1048576] | Yes | The number of rows in the users table. If this variable is 0, Performance Schema does not maintain connection statistics in the users table or status variable information in the status by user table. _ _ |
| loose rds audit _ _ _ max sql size _ _ | 5.7 | 819 2 | [0-32768] | No | The maximum size of an SQL statement in the RDS audit log. |
| loose rds check _ _ _ core file enabled _ _ | 5.7 | ON | [ON\|OFF] | No | Enable core file checking. |
| loose polarscale _ _ parallel computin _ g ct limit high _ _ _ | 8.0 | 500 000 | [0- 10000000] | No | Pipeline control high-water mark. |
| loose polarscale _ _ parallel computin _ g ct limit low _ _ _ | 8.0 | 500 00 | [0- 2000000] | No | Pipeline control low watermark. |
| loose polarscale _ _ parallel computin _ g order row num _ _ _ | 8.0 | 100, 000 | [10- 10000000] | No | A pipeline exchange unit for the parallel sort operator. |
| loose polarscale _ _ parallel computin _ g read consisten _ _ t | 8.0 | 1 | [0\|1] | No | Enable shared ReadView: 0 (Disable), 1 (Enable). |
| loose polarscale _ _ parallel computin _ g row num _ _ | 8.0 | 100 00 | [10- 200000] | No | The unit that flows through the parallel read operator pipeline. |

| loose polarscale _ _ parallel computin _ g switch _ | 8.0 | 1 | [0\|1] | No | Enable parallel computing: 0 (disabled), 1 (enabled). |
|---|---|---|---|---|---|
| loose polarscale _ _ parallel computin _ g thread num _ _ | 8.0 | 32 | [1-128] | No | The degree of parallelism parameter. |
| loose polarscale _ _ parallel computin _ g trace _ | 8.0 | 0 | [0\|1] | No | Enable trace: 0 (disabled), 1 (enabled). |
| loose rds audit l _ _ _ og event buffer _ _ _ size | 8.0 | 204 8 | [0-32768] | No | The maximum SQL size in the RDS audit log. |
| loose rds kill con _ _ _ nections | 8.0, 5.7 | 20 | [0- 18446744 07370955 1615] | No | Additional connections for the user in rds user with kill option. _ _ _ _ |
| loose rds set co _ _ _ nnection id enab _ _ led | 5.7 | ON | [ON\|OFF] | No | A patch for the Proxy connection ID. |
| loose recycle bin _ _ | 8.0, 5.7 | OFF | [OFF\|ON] | No | The switch for the recycle bin. |
| loose recycle bin _ _ retention _ | 8.0, 5.7 | 604 800 | [86400- 1209600] | No | The retention period for the recycle bin, in seconds. |
| loose recycle sch _ _ eduler | 8.0, 5.7 | OFF | [OFF\|ON] | No | Enables or disables the cleanup thread. |
| loose sql safe up _ _ _ dates | 8.0, 5.7 | Off | [ON\|OFF] | No | If this variable is enabled, an error occurs if an UPDATE or DELETE statement omits a key in the WHERE or LIMIT clause. |
| loose thread poo _ _ l enabled _ | 8.0, 5.7 | ON | [ON\|OFF] | No | Enable or disable the thread pool. |
| loose thread poo _ _ l oversubscribe _ | 8.0, 5.7 | 32 | [10-64] | No | The number of additional active worker threads allowed per group. |
| loose thread poo _ _ l size _ | 8.0, 5.7 | 4 | [1-16] | No | The number of thread groups in the thread pool. |

| loose validate pa _ _ ssword check us _ _ er name _ | 5.7 | ON | [ON\|OFF] | No | When set to ON, the password can be set to the current username. |
|---|---|---|---|---|---|
| loose validate pa _ _ ssword length _ | 8.0, 5.7 | 8 | 8.0: [1- 32] 5.7: [0- 256] | No | The minimum password length. For example, a value of 8 requires the password to be at least 8 characters long. |
| loose validate pa _ _ ssword mixed ca _ _ se count _ | 8.0, 5.7 | 1 | 8.0: [0- 32] 5.7: [0- 256] | No | If the password policy is medium or stronger, validate password requires a _ minimum number of lowercase and uppercase characters. A password must contain at least this number of lowercase characters and at least this number of uppercase characters. |
| loose validate pa _ _ ssword number c _ _ ount | 8.0, 5.7 | 1 | 8.0: [0- 32] 5.7: [0- 256] | No | The number of digits that the password must contain. |

| loose validate pa _ _ ssword policy _ | 5.7 | 1 | [0\|1\|2] | No | This parameter controls the MySQL password policy. It accepts the numeric values 0, 1, and 2, or the corresponding symbolic values LOW, MEDIUM, and STRONG. The 0 or LOW policy is the loosest. It requires passwords to contain at least one character and meet the minimum length specified by validate password length. _ _ The 1 or MEDIUM policy requires passwords to contain at least one lowercase letter, one uppercase letter, one digit, and one special character. Passwords must also meet the minimum length specified by validate password length. _ _ The 2 or STRONG policy is the strictest. It requires passwords to contain at least one lowercase letter, one uppercase letter, one digit, and one special character. Passwords must also meet the minimum length specified by validate password length. This policy _ _ also checks whether the password is in the dictionary file. |
|---|---|---|---|---|---|
| loose validate pa _ _ ssword special c _ _ har count _ | 8.0, 5.7 | 1 | 8.0: [0- 32] 5.7: [0- 256] | No | The number of special characters that the password must contain. |
| low priority upda _ _ tes | 8.0, 5.7 | 0 | [0\|1] | No | If set to 1, all INSERT, UPDATE, DELETE, and LOCK TABLE WRITE statements wait until no pending SELECT or LOCK TABLE READ statements exist on the affected table. This affects only storage engines that use only table-level locking, such as MyISAM, MEMORY, and MERGE. This variable was formerly named sql low priority updates. _ _ _ |
| lower case table _ _ names _ | 5.7 | 1 | [0\|1] | Yes | If this parameter is set to 1, table names are stored in lowercase on the disk, and name comparisons are not case- sensitive. If you use a case-insensitive file system, set this parameter to 2. |

| master verify ch _ _ ecksum | 8.0, 5.7 | OFF | [ON\|OFF] | No | Enabling this variable causes the primary server to check checksums when reading from the binary log. By default, this variable is disabled. When disabled, the primary server verifies events using the event length in the binary log to ensure that only complete events are read. |
|---|---|---|---|---|---|
| max allowed pac _ _ ket | 8.0, 5.7 | 107 374 182 4 | [16384- 10737418 24] | No | The maximum size of one packet, or any generated or intermediate string. Unit: bytes. |
| max binlog cach _ _ e size _ | 8.0, 5.7 | 184 467 440 737 095 475 20 | [4096- 18446744 07370954 7520] | No | The max binlog cache size parameter _ _ _ sets the size of the transaction cache. The session visibility of max binlog cache size matches the _ _ _ visibility of the binlog cache size system _ _ variable. |
| max binlog stmt _ _ cache size _ _ | 8.0, 5.7 | 184 467 440 737 095 475 20 | [4096- 18446744 07370954 7520] | No | If non-transactional statements in a transaction require more memory than this value, the server generates an error. The minimum value is 4096. The maximum and default value is 4 GB on 32-bit platforms and 16 EB (exabytes) on 64-bit platforms. |
| max connect err _ _ ors | 8.0, 5.7 | 100 | [0- 42949672 95] | No | If the number of consecutive, interrupted connection requests from a host exceeds this value, the server blocks that host from making further connections. To unblock a blocked host, flush the host cache. |
| max error count _ _ | 8.0, 5.7 | 64 | [0-65535] | No | The maximum number of error, warning, and informational messages stored for the SHOW ERRORS and SHOW WARNINGS statements. This value is the same as the number of condition areas in the diagnostics area. Therefore, it is also the number of conditions that can be checked using GET DIAGNOSTICS. |
| max execution ti _ _ me | 8.0 | 0 | [0- 42949672 95] | No | If the running time exceeds this value, the statement is interrupted. |

| max heap table _ _ _ size | 8.0, 5.7 | 671 088 64 | [16384- 18446744 07370954 752] | No | This variable sets the maximum size for user-created MEMORY tables. The value of this variable is used to calculate the MAX ROWS value for MEMORY tables. _ Setting this variable has no effect on any existing MEMORY tables unless the table is recreated using a CREATE TABLE statement or modified using an ALTER TABLE or TRUNCATE TABLE statement. A server restart also sets the maximum size of existing MEMORY tables to the global max heap table size value. _ _ _ |
|---|---|---|---|---|---|

| max join size _ _ | 8.0, 5.7 | 8. 0: 1 8 4 4 6 7 4 4 0 7 3 7 0 9 5 5 1 6 1 5 5. 7: 1 8 4 4 6 7 4 4 0 7 3 7 0 9 5 0 0 0 0 0 | [1- 18446744 07370955 1615] | No | Disallows statements that are likely to examine more than max join size rows _ _ for a single-table statement or more than max join size row combinations for a _ _ multi-table statement. It also disallows statements that might perform more than max join size disk lookups. Set this _ _ value to catch statements that do not use keys properly and would likely take a long time to execute. Set this variable if users tend to run joins that are missing a WHERE clause, take a long time, or return millions of rows. |
|---|---|---|---|---|---|
| max length for s _ _ _ ort data _ | 8.0, 5.7 | 102 4 | [0-838860] | No | The cutoff point for the index value size. This determines which file sorting algorithm to use. |
| max points in ge _ _ _ ometry | 8.0, 5.7 | 655 36 | [3- 1048576] | No | The maximum value of the points per circle parameter in the _ _ ST Buffer Strategy() function. _ _ |

| max prepared st _ _ mt count _ | 8.0, 5.7 | 163 82 | [0- 1048576] | No | This variable limits the total number of prepared statements on the server. |
|---|---|---|---|---|---|
| max seeks for k _ _ _ ey | 8.0, 5.7 | 184 467 440 737 095 000 00 | [1- 18446744 07370955 1615] | No | Limits the assumed number of seeks when looking up rows by key. The MySQL optimizer assumes that when scanning an index, the number of key seeks required to find matching rows does not exceed this value, regardless of the actual cardinality of the index. Set this parameter to a low value, such as 100, to force MySQL to prefer indexes over table scans. |
| max sort length _ _ | 8.0, 5.7 | 102 4 | [4- 8388608] | No | The number of bytes to use when sorting data values. The server uses only the first max sort length bytes of each value _ _ and ignores the rest. Therefore, for GROUP BY, ORDER BY, and DISTINCT operations, values that differ only after the first max sort length bytes are _ _ considered equal. |
| max sp recursio _ _ n depth _ | 8.0, 5.7 | 0 | [0-255] | No | The number of times a stored procedure can be called recursively. The default value is 0, which completely disables recursion. The maximum value is 255. |
| max write lock c _ _ _ ount | 8.0, 5.7 | 102 400 | [1-102400] | No | After this number of write locks, some read locks are allowed to run in between. |
| metadata locks c _ _ ache size _ | 5.7 | 102 4 | [1- 1048576] | No | The size of the metadata lock cache. The server uses this cache to avoid creating and destroying synchronization objects. This is especially helpful on systems where these operations are expensive, such as Windows XP. |
| min examined ro _ _ w limit _ | 8.0, 5.7 | 0 | [0- 42949672 95] | No | Queries that examine fewer rows than this value are not recorded in the slow query log. |
| myisam sort buff _ _ er size _ | 8.0, 5.7 | 262 144 | [262144- 16777216] | No | The size of the buffer that is allocated when sorting MyISAM indexes with REPAIR TABLE or creating indexes with CREATE INDEX or ALTER TABLE. |

| mysql native pas _ _ sword proxy use _ _ rs | 8.0, 5.7 | OFF | [ON\|OFF] | No | This variable controls whether the mysql native password built-in _ _ authentication plugin supports proxy users. It has no effect unless the check proxy users system variable is _ _ enabled. |
|---|---|---|---|---|---|
| net buffer length _ _ | 8.0, 5.7 | 163 84 | [1024- 1048576] | No | Each client thread is associated with a connection buffer and a result buffer. Both start at the size specified by net buffer length, but expand up to _ _ max allowed packet bytes as needed. _ _ After each SQL statement, the result buffer shrinks to the size of net buffer length. _ _ |
| net read timeout _ _ | 8.0, 5.7 | 30 | [1- 18446744 07370955 1615] | No | The number of seconds to wait for more data from a connection before aborting the read. |
| net retry count _ _ | 8.0, 5.7 | 10 | [1- 42949672 95] | No | The number of retries for an interrupted read or write on a communication port before the operation is aborted. |
| net write timeou _ _ t | 8.0, 5.7 | 60 | [1- 18446744 07370955 1615] | No | The number of seconds to wait for a block to be written to a connection before aborting the write. |
| ngram token siz _ _ e | 8.0, 5.7 | 2 | [0-20] | Yes | Specifies the n-gram token size for the n- gram full-text resolver. The ngram token size option is read-only _ _ and can be modified only at startup. The default value is 2 (bigram). The maximum value is 10. |
| old passwords _ | 5.7 | 0 | [0\|2] | No | This variable controls the password hashing method that the PASSWORD() function uses. It also affects password hashing for CREATE USER and GRANT statements that specify a password with the IDENTIFIED BY clause. |
| open files limit _ _ | 8.0, 5.7 | 655 35 | [1- 18446744 07370955 1615] | Yes | If this value is not 0, mysqld uses this value to reserve file descriptors with setrlimit(). |

| optimizer prune l _ _ evel | 8.0, 5.7 | 1 | [0\|1] | No | Controls the heuristics applied during query optimization to prune less promising partial plans from the optimizer's search space. A value of 0 disables the heuristics, causing the optimizer to perform an exhaustive search. A value of 1 causes the optimizer to prune plans based on the number of rows retrieved by intermediate plans. |
|---|---|---|---|---|---|
| optimizer search _ depth _ | 8.0, 5.7 | 62 | [0-62] | No | Specifies the maximum search depth for the query optimizer. A value larger than the number of relations in the query produces a better query plan, but takes longer to generate the execution plan. A value smaller than the number of relations in the query returns an execution plan faster, but the resulting plan may be far from optimal. If set to 0, the system automatically selects a reasonable value. |
| optimizer trace li _ _ mit | 8.0, 5.7 | 1 | [0- 42949672 95] | No | The maximum number of displayed optimizer traces. |
| optimizer trace _ _ max mem size _ _ | 8.0, 5.7 | 163 84 | [0- 42949672 95] | No | The maximum cumulative size of stored optimizer traces. |
| optimizer trace o _ _ ffset | 8.0, 5.7 | -1 | [- 21474836 48- 21474836 47] | No | The display offset for the optimizer trail. |
| opt indexstat _ | 8.0 | OFF | [ON\|OFF] | Yes | Specifies whether to enable index statistics. |
| opt tablestat _ | 8.0 | OFF | [ON\|OFF] | Yes | Specifies whether to enable statistics collection for tables. |
| performance poi _ nt iostat interval _ _ | 8.0 | 2 | [0-60] | No | The interval for collecting I/O statistics, in milliseconds. |
| performance poi _ nt iostat volume _ _ size _ | 8.0 | 100 00 | [0-100000] | Yes | The maximum capacity for I/O statistics collection. The unit is the number of slots. |

| performance poi _ nt lock rwlock e _ _ _ nabled | 8.0 | ON | [ON\|OFF] | No | Enables or disables the performance optimization feature for read/write locks. |
|---|---|---|---|---|---|
| performance sch _ ema | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/85 899 345 92, 1)} | [0-1] | Yes | Specifies whether to enable the performance schema. At server startup, set this variable to 1 to enable it or 0 to disable it. |
| preload buffer si _ _ ze | 8.0, 5.7 | 327 68 | [1024- 10737418 24] | No | The size of the buffer allocated for preloading indexes. |
| query alloc block _ _ size _ | 8.0, 5.7 | 819 2 | [1024- 16384] | No | The size of memory blocks that are allocated when objects are created during statement parsing and execution. Unit: bytes. |
| query cache limi _ _ t | 5.7 | 104 857 6 | [1- 1048576] | No | Do not cache results larger than this number of bytes. |
| query cache min _ _ res unit _ _ | 5.7 | 102 4 | [512- 18446744 07370955 1608] | No | The minimum size, in bytes, of a block allocated by the query cache. |
| query cache size _ _ | 5.7 | 0 | [0- 10485760 000] | No | The amount of memory allocated for the query cache. A default value of 0 disables the query cache. Allowed values are multiples of 1024. Other values are rounded to the nearest multiple. Unit: bytes. |

| query cache typ _ _ e | 5.7 | 0 | [0\|1\|2] | Yes | 0: Does not cache or retrieve results. 1: Caches all results except for SELECT SQL NO CACHE queries. _ _ 2: Caches only SELECT SQL CACHE ... _ queries. |
|---|---|---|---|---|---|
| query cache wlo _ _ ck invalidate _ | 5.7 | OFF | [ON\|OFF] | No | Normally, when a client acquires a write lock on a MyISAM table, other clients are not blocked from reading from the table if the query result is in the query cache. Setting this variable to ON causes a write lock to invalidate any queries in the query cache that reference the table. This forces other clients that attempt to access the table to wait while the lock is in effect. |
| query prealloc si _ _ ze | 8.0, 5.7 | 819 2 | [8192- 1048576] | No | The size of the persistent buffer used for statement parsing and execution. This buffer is not released between statements. For complex queries, a larger query prealloc size value can _ _ improve performance by reducing the need for the server to allocate memory during query execution. Unit: bytes. |
| range alloc block _ _ size _ | 8.0, 5.7 | 409 6 | [4096- 18446744 07370955 1615] | No | The size of the block allocated during range optimization. |
| range optimizer _ _ max mem size _ _ | 8.0, 5.7 | 838 860 8 | [0- 18446744 07370955 1615] | No | The memory limit for the range optimizer. A value of 0 means no limit. If the optimizer considers an execution plan that uses the range access method, it estimates the required memory. If the estimate exceeds this limit, the optimizer discards the plan and considers other plans. |
| rds reserved con _ _ nections | 5.7 | 512 | [0-512] | No | The connections reserved for maintenance users. |

| read buffer size _ _ | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 485 76* 128, 262 144) } | [8200- 21474795 52] | No | Each thread that performs a sequential scan of a MyISAM table allocates a buffer of this size in bytes for each table it scans. If the value is not a multiple of 4 KB, it is rounded to the nearest multiple of 4 KB. |
|---|---|---|---|---|---|
| relay log recover _ _ y | 8.0, 5.7 | OFF | [ON\|OFF] | Yes | If enabled, this variable activates the automatic relay log recovery feature as soon as the server starts. This global variable is read-only at runtime. |
| session track gti _ _ ds | 8.0, 5.7 | OFF | [OFF\|OWN _ GTID\|ALL _ GTIDS] | No | Controls the tracker that catches Global Transaction Identifiers (GTIDs) and returns them in the OK packet. Depending on the value of this option, the tracker catches the specified GTID at the end of a transaction and appends it to the OK packet. |
| sha256 password _ proxy users _ _ | 8.0, 5.7 | OFF | [ON\|OFF] | No | This variable controls whether the built- in sha256 password authentication plug- _ in supports proxy users. It has no effect unless the check proxy users system _ _ variable is enabled. |
| show compatibili _ ty 56 _ | 5.7 | OFF | [ON\|OFF] | No | The INFORMATION SCHEMA contains _ tables with information about system and status variables. The Performance Schema tables are designed to replace the INFORMATION SCHEMA tables. _ These tables have been deprecated since MySQL 5.7.6 and will be removed in a future MySQL version. |
| show old tempor _ _ als | 8.0, 5.7 | OFF | [ON\|OFF] | No | Specifies whether the SHOW CREATE TABLE output includes comments to mark temporal columns that use a format from before version 5.6.4. This format applies to TIME, DATETIME, and TIMESTAMP columns that do not support fractional-seconds precision. This variable is disabled by default. If enabled, the SHOW CREATE TABLE output includes comments that mark these temporal columns. |

| slave net timeou _ _ t | 8.0, 5.7 | 60 | [15-300] | No | The number of seconds a secondary server waits for more data from the primary server. If this timeout is exceeded, the secondary server considers the connection broken, stops reading, and attempts to reconnect. |
|---|---|---|---|---|---|
| slave parallel typ _ _ e | 8.0, 5.7 | LOG ICAL CL _ OCK | [DATABAS E\|LOGICAL CLOCK] _ | Yes | This variable specifies the policy that determines which transactions to execute in parallel on the secondary server. This variable has no effect on a secondary server if multi-threading is disabled. When slave preserve commit order=1, only _ _ _ LOGICAL CLOCK can be used. _ |
| slave type conve _ _ rsions | 8.0, 5.7 | Non e | [Supports spaces and the following values: ALL LOSSY _ \| ALL NON L _ _ OSSY \| ALL SIGNE _ D \| ALL UNSIG _ NED] | Yes | Controls the type conversion patterns on the secondary server when using row- based replication. |
| slow launch time _ _ | 8.0, 5.7 | 2 | [1-1024] | No | If creating a thread takes longer than this value in seconds, the server increases the Slow launch threads _ _ status variable. |
| slow query log _ _ | 8.0, 5.7 | ON | [ON\|OFF] | No | Specifies the initial state of the slow query log. Using the --slow-query-log option with no value or a value of 1 enables the log. Not using the option, or using it with a value of 0, disables the log. |
| sort buffer size _ _ | 8.0, 5.7 | 262 144 | [32768- 42949672 95] | No | Each session that must perform a sort allocates a buffer of this size. |
|   |   |   | (REAL AS _ _ FLOAT\|PIP ES AS CO _ _ NCAT\|ANSI QUOTES\|I _ GNORE SP _ |   |   |

| psaraDB for RDS |   |   |   |   | ApsaraDB RDS for MySQL User G uide·Instance |
|---|---|---|---|---|---|
| sql mode _ | 8.0, 5.7 | ONL Y F _ ULL _ GRO UP _ BY,S TRIC T T _ RAN S T _ ABL ES,N O Z _ ERO IN _ _ DAT E,N O Z _ ERO DA _ TE,E RRO R F _ OR _ DIVI SIO N B _ Y Z _ ERO ,NO _ EN GIN E S _ UBS TITU TIO N | ACE\|ONLY _ FULL GRO _ UP BY\|NO _ _ UNSIGNED SUBTRAC _ TION\|NO D _ IR IN CRE _ _ ATE\|ANSI\| NO AUTO _ _ VALUE ON _ ZERO\|NO _ _ BACKSLAS H ESCAPE _ S\|STRICT T _ RANS TAB _ LES\|STRIC T ALL TAB _ _ LES\|NO ZE _ RO IN DAT _ _ E\|NO ZER _ O DATE\|AL _ LOW INVA _ LID DATES _ \|ERROR F _ OR DIVISI _ ON BY ZE _ _ RO\|TRADIT IONAL\|HIG H NOT PR _ _ ECEDENCE \|NO ENGIN _ E SUBSTIT _ UTION\|PAD CHAR TO _ _ FULL LEN _ _ GTH) (,REAL AS _ _ FLOAT\|,PIP ES AS CO _ _ NCAT\|,ANS I QUOTES\|, _ IGNORE SP _ ACE\|,ONLY FULL GRO _ _ UP BY\|,NO _ UNSIGNE _ D SUBTRA _ CTION\|,NO DIR IN C _ _ _ REATE\|,AN SI\|,NO AUT _ O VALUE _ _ ON ZERO\|, _ NO BACKS _ LASH ESC _ APES\|,STRI CT TRANS _ _ TABLES\|,S TRICT ALL _ TABLES\|, _ NO ZERO I _ _ N DATE\|,N _ O ZERO D _ _ ATE\|,ALLO W INVALID _ DATES\|,E _ | No | Defines the SQL syntax that MySQL supports and the types of data validation checks to perform. |

|   |   |   | RROR FOR _ DIVISION _ _ BY ZERO\|, _ TRADITION AL\|,HIGH _ NOT PREC _ EDENCE\|,N O ENGINE _ _ SUBSTITUT ION\|,PAD _ CHAR TO _ _ FULL LENG _ TH)* |   |   |
|---|---|---|---|---|---|
| stored program _ _ cache | 8.0, 5.7 | 256 | [16- 524288] | No | Sets a soft upper limit on the number of cached stored procedures and stored functions for each connection. The server maintains two separate caches, one for stored procedures and one for stored functions. The value of this variable specifies the size of each cache. |
| sync master info _ _ | 8.0, 5.7 | 100 00 | [0- 18446744 07370955 1615] | No | The effect of this variable on a secondary server during replication depends on whether the master info repository parameter is set _ _ to FILE or TABLE. |
| sync relay log in _ _ _ fo | 8.0, 5.7 | 100 00 | [0- 18446744 07370955 1615] | No | Setting this variable takes immediate effect on all replication channels, including running channels. |
| table definition c _ _ ache | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24* 512, 204 8) } | [400- 524288] | No | Specifies the number of table definitions from .frm files that can be stored in the definition cache. If you use many tables, create a larger table definition cache to open tables faster. Unlike the standard table cache, the table definition cache uses less space and no file descriptors. The minimum and default values are both 400. |

| table open cach _ _ e | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24* 256, 204 8) } | [1-524288] | No | The number of open tables for all threads. Increasing this value increases the number of file descriptors that mysqld requires. Check the Opened tables status variable to _ determine whether to increase the table cache. For more information, see Server Status Variables. If the Opened tables _ value is large and you do not use FLUSH TABLES often, increase the table open cache variable value. The _ _ FLUSH TABLES command simply closes and reopens all tables. |
|---|---|---|---|---|---|
| table open cach _ _ e instances _ | 8.0, 5.7 | {LE AST( DBIn stan ceCl ass Me mor y/10 737 418 24, 16)} | [1-64] | Yes | The number of open table cache instances. To improve scalability by reducing contention between sessions, the open table cache can be partitioned into several smaller cache instances. The size of each instance is `table open cache / _ _ table open cache instances`. A session _ _ _ only needs to lock one instance to access it for DML statements. This segments cache access into instances and improves performance for operations that use the cache when many sessions access tables. DDL statements still need to lock the entire cache, but these statements are much less frequent than DML statements. |
| temptable max r _ _ am | 8.0 | 107 374 182 4 | [2097152- 10737418 2400] | No | The maximum amount of memory in bytes that the TempTable storage engine can allocate from RAM before storing data to disk. |

| thread cache siz _ _ e | 8.0, 5.7 | 8. 0: 1 0 0 5. 7: 2 5 6 | [0-16384] | No | Specifies how many threads the server should cache for reuse. When a client disconnects, its thread is placed in the cache if the number of cached threads is less than thread cache size. Thread _ _ requests are fulfilled by reusing threads from the cache when possible. A new thread is created only when the cache is empty. If you have many new connections, increase this variable to improve performance. This setting usually does not offer a significant performance improvement with a good thread implementation. However, if your server receives hundreds of connections per second, set thread cache size high _ _ enough to ensure most new connections use cached threads. Check the difference between the Connections and Threads created status variables to see _ how efficient the thread cache is. |
|---|---|---|---|---|---|
| thread stack _ | 8.0, 5.7 | 262 144 | [131072- 18446744 07370955 1615] | Yes | The stack size for each thread. The default value is 192 KB, or 256 KB for 64-bit systems. This size is sufficient for normal operations. If the thread stack size is too small, it limits the server's ability to handle complex SQL statements, deep recursion in stored procedures, and other memory- consuming operations. |
| tls version _ | 8.0, 5.7 | TLS v1.2 | [TLSv1,TLS v1.1,TLSv1 .2\|TLSv1,T LSv1.1\|TLS v1.2] | Yes | The protocols that the server permits for encrypted connections. The value is a comma-separated list of one or more protocol names. The SSL library used to compile MySQL determines the available protocols. |
| tmp table size _ _ | 8.0, 5.7 | 209 715 2 | [262144- 13421772 8] | No | The maximum size of a temporary table in internal memory. |
| transaction alloc _ block size _ _ | 8.0, 5.7 | 819 2 | [1024- 131072] | No | Increases the amount of memory, in bytes, for each transaction memory pool. For more information, see the description of transaction prealloc size. _ _ |
| transaction isolat _ ion | 8.0, 5.7 | REA D- COM MITT ED | [READ- UNCOMMIT TED\|READ- COMMITTE D\|REPEATA BLE- READ\|SERI ALIZABLE] | No | The default transaction isolation level. |

| transaction preal _ loc size _ | 8.0, 5.7 | 409 6 | [1024- 131072] | No | Each transaction has a memory pool to allocate various transaction-related memory. The initial size of the pool is transaction prealloc size bytes. For each _ _ allocation that fails because of an out of memory error, the pool increases by transaction alloc block size bytes. When _ _ _ a transaction ends, the pool is truncated to transaction prealloc size bytes. _ _ |
|---|---|---|---|---|---|
| updatable views _ _ with limit _ | 8.0, 5.7 | YES | YES \| NO | No | This variable controls whether a view can be updated with a `LIMIT` clause if the view does not contain all columns of the primary key from the underlying table. (Such updates are typically generated by GUI tools). An update can be an `UPDATE` or `DELETE` statement. Here, the primary key refers to a primary key or a unique index in which no column can contain `NULL`. |
| wait timeout _ | 8.0, 5.7 | 864 00 | [1- 31536000] | No | The number of seconds the server waits for activity before closing a non- interactive connection. |

### Read-only instances

#### Overview of read-only instances

ApsaraDB RDS for MySQL allows you to create read-only instances. In scenarios where an instance has a small number of write requests but a large number of read requests, you can create read-only instances to distribute database access loads away from the primary instance. This topic describes the features and limits of read-only instances. To scale up the reading capability and distribute database access loads, you can create one or more read-only instances in a region. Read-only instances can increase the application throughput when a large amount of data is being read. A read-only instance with a single physical node and no backup node uses the native replication capability of MySQL to synchronize changes from the primary instance to all its read-only instances. Read-only instances must be in the same region as the primary instance but do not have to be in the same zone as the primary instance. The following figure shows the topology of read-only instances.
**Read-only instances have the following features**:
Specifications of a read-only instance can be different from those of the primary instance and can be changed at any time. This facilitates elastic scaling. Read-only instances do not require account or database maintenance. Account and database information is synchronized from the primary instance. The whitelists of read-only instances can be independently configured. System performance monitoring is provided. ApsaraDB RDS provides up to 20 system performance monitoring views, including those for disk capacity, IOPS, connections, CPU utilization, and network traffic. You can view the load of instances. ApsaraDB RDS provides a variety of optimization recommendations, such as storage engine check, primary key check, large table check, and check for excessive indexes and missing indexes. You can optimize your databases based on the optimization recommendations and specific applications.

#### Create a read-only instance

You can create read-only instances of different specifications based on your business requirements.

**Precautions**

A maximum of five read-only instances can be created for a primary instance. Backup settings and temporary backup are not supported. Instance restoration is not supported. Data migration to read-only instances is not supported. Database creation and deletion are not supported. Account creation, deletion, authorization, and password changes are not supported. After a read-only instance is created, you cannot restore data by directly overwriting the primary instance with a backup set.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Distributed by Instance Role** section on the right side of the **Basic Information**
page, click **Create Read-only Instance**.
4. On the **Create Read-only RDS Instance** page, configure the read-only instance
parameters.

| Section | Parameter | Description |
|---|---|---|
| Region | Region | The region in which you want to create the read- only instance. |
| Specifications | Database Engine | The database engine of the read-only instance, which is the same as that of the primary instance and cannot be changed. |
|   | Engine Version | The version of the database engine, which is the same as that of the primary instance and cannot be changed. |
|   | Edition | Set the value to Read-only. |
|   | Instance Type | The instance type of the read-only instance. The instance type of the read-only instance can be different from that of the primary instance, and can be changed at any time to facilitate flexible upgrade and downgrade. |
|   | Storage Capacity | The storage capacity of the read-only instance. To ensure sufficient I/O throughput for data synchronization, we recommend that you select at least the same instance type and storage capacity as the primary instance for the read- only instance. Valid values: 20 to 6000. Unit: GB. The value is in 1 GB increments. |
| Network Type | Network Type | The network type of the read-only instance. This must be the same as that of the primary instance and cannot be changed. |
|   | VPC | The VPC in which you want to create the read- only instance. |
|   | vSwitch | The vSwitch in the VPC. |

5. Click **Submit**.

#### View details of read-only instances

This topic describes how to view details of read-only instances. You can go to the Basic Information page of a read-only instance from the Instances page or from the read-only instance list of the primary instance. Read-only instances are managed in the same manner as primary instances. The Basic Information page shows the management operations that can be performed.

**View details of a read-only instance from the Instances page**

1. Log on to the ApsaraDB RDS console.
2. On the **Instances** page, click the ID of a read-only instance. The **Basic Information** page
appears.

**Note**

In the instance list, **Instance Role** of read-only instances is displayed as
**Read-only Instance**.

**View details of a read-only instance from the Basic Information**

**page of the primary instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. On the **Basic Information** page, move the pointer over the number below **Read-only**
**Instances** in the **Distributed by Instance Role** section. The ID of the read-only instance
is displayed.
4. Click the ID of the read-only instance to go to the Basic Information page of the read-only
instance.

### Manage instances in the

**recycle bin**

This topic describes how to recreate or destroy an ApsaraDB RDS instance in the recycle bin.

**Description**

All ApsaraDB RDS for MySQL instances, except for the following instances, are moved to the recycle bin after they are manually released: Instances that are manually released within seven days after they are created.
**Read-only instances** and **Enterprise Edition instances**.

**Recreate an instance**

If you manually release an ApsaraDB RDS instance that runs for more than seven days, backup files of the instance are retained for another eight days. Within the eight-day retention period, you can create another instance and restore data from the backup files to the new instance. After the eight-day retention period elapses, the backup files of the instance are deleted.
1. Log on to the ApsaraDB RDS console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Locked Instances**.
3. Find the released instance and click **Rebuild** in the Actions column.
4. On the **Restore Instance** page, select **Storage Capacity** and **Network Type** for the new
instance and click **Submit**.

**Note**

If you set **Network Type** to **VPC**, you must configure a **virtual private cloud**
**(VPC)** and a **vSwitch**.
Other configurations remain the same as the original instance and cannot be changed.

**Destroy an instance**

You can destroy an ApsaraDB RDS instance that is no longer needed in the recycle bin.

**Warning**

After you destroy an ApsaraDB RDS instance, **all** the backup files of the instance are destroyed, including regular data backup files, archived backup files, and log backup files. The destroyed backup files **cannot be restored**. Proceed with caution.
1. Log on to the ApsaraDB RDS console.
2. In the upper-left corner of the page, select an organization. In the left-side navigation pane,
click **Locked Instances**.
3. Find the released instance and click **Destroy** in the Actions column. In the message that
appears, click **Confirm**.

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

## Accounts

### Language Detection

Detect the language of the input text. Supports automatic recognition of 23 languages. Best suited to short text such as search queries, product titles, and chat messages. Synchronous.

**Endpoint**

```
POST /ai/text/marco/language-detection
```

**Use cases**

Cross-border search -- detect the buyer's search-query language and route to the matching index. Title preprocessing -- detect source language automatically before calling the Text Translation API, so callers do not need to pass `SourceLanguage` . Chat routing -- forward users to native-language agents based on detected language.

**Quick start**

```java
import json data = json.dumps({ "SourceText": "Hello world" }) result = make_signed_request("/ai/text/marco/language-detection", data) print(result["Data"]["DetectedLanguage"]) # en
```

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| SourceText | String | Yes | Text to identify. Up to ~1024 characters recommended; very short inputs (single tokens) have lower accuracy. |

**Response fields**

| Field | Type | Description |
|---|---|---|
| Code | String | Business status. Success when OK; otherwise see Error codes. |
| Message | String | Business message. |
| RequestId | String | Unique request identifier. |
| Success | Boolean | Whether the call succeeded. |

| psaraDB RDS for MySQL User G |   | ApsaraDB for RD |
|---|---|---|

| Field | Type | Description |
|---|---|---|
| Data.DetectedLanguage | String | Detected language code; see "Supported languages" below. |
| Data.UsageMap.RequestCount | Number | Request count for billing reconciliation. |

|   | Data.UsageMap.RequestCount |   |
|---|---|---|

**Response example**

`{`

```json
  "Code": "Success",
  "Message": "ok",
  "RequestId": "21570000-0000-0000-0000-000000000001",
  "Success": true,
  "Data": {
    "DetectedLanguage": "en",
    "UsageMap": { "RequestCount": 1 }
```

`}` `}`

**Supported languages (23)**

| ngali ( bn ), German ( de he ), Indonesian ( id ), It tch ( nl ), Polish ( pl ), Po krainian ( uk ), Urdu ( ur Traditional ( zh-tw ). |   | de |   |
|---|---|---|---|
|   | id |   |   |
|   |   |   | ), It ), Po |
|   | pl |   |   |

| lish ( | en |
|---|---|
| it |   |

|   | es |
|---|---|
| ja |   |

( `fr` ), Hebrew ( `he` ), Indonesian ( `id` ), Italian ( `it` ), Japanese ( `ja` ), Korean ( `ko` ),

| ms |   | ), |
|---|---|---|
| ( |   |   |

Malay ( `ms` ), Dutch ( `nl` ), Polish ( `pl` ), Portuguese ( `pt` ), Russian ( `ru` ), Thai ( `th` ),

**Error codes**

Common error codes: `InvalidParameter` (missing or empty `SourceText` ), `InternalError` (system busy). See Error codes for the full reference.

**What's next**

Text Translation API -- translate plain text. Text Correction API -- spelling correction.

### Reset the password of a

**database account**

You can reset the password of your database account in the ApsaraDB RDS console.

**Prerequisites**

The ApsaraDB RDS instance is in the **Running** state. A database account is created. For information about how to create a database account, see Create an account.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to manage and click **Reset Password** in the Actions
column.
5. In the dialog box that appears, enter and confirm the new password, and then click **OK**.

**Note**

The password must meet the following requirements: It can be 8 to 32 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: !@#$%^&*()_+-= .

### Product Material Optimization

**Pro**

The **best-quality** tier of the one-click cross-platform material optimization service. Given a 1688 product URL, produce TEMU-ready titles, attributes, hero images, SKU images, detail images, and copy. Uses the official Best Quality workflow: full AI capability stack, preserves and localizes brand marketing assets, and emits category-specific assets (e.g., size charts) for apparel. Asynchronous.

**Endpoints**

**Submit optimization task**

```
POST /ai/material/optimization/pro
```

**Query optimization result**

```
POST /ai/material/optimization/pro/result
```

**Use cases**

High ASP, brand merchants, apparel / accessories / beauty / home -- categories that rely on marketing assets. Multi-language, multi-market localization. Scenarios needing category-specific assets (size chart, package weight/dimensions).

**Workflow**

The official Best Quality workflow:
1. Parse the 1688 product URL, extract all assets, diagnose gaps.
2. LLM compliance filtering, SEO keyword optimization, five-point bullets, multi-language
localized rewrite.
3. Images: invoke smart element detection / matting / removal / image translation Pro /
expansion / smart crop / upscale; remove non-compliant elements while **preserving and**
**rewriting marketing copy**.
4. Category-specific assets: apparel size charts, package weight/dimensions, etc.
5. Output a standardized material package via API and / or Excel export.

**Request parameters**

Pro and Lite share the same 31-field schema; the difference is the server-side workflow. See the Smart Image Generation API for the full schema. Pro typically enables `Ability=` `[1,2,3,4,5,6,7]` -- all 7 atomic capabilities.

**Response fields (query)**

Pro adds the following fields on top of Lite:

| Field | Type | Description |
|---|---|---|
| Data.Result.BulletPoints | String[] | Five-point bullets for detail- page selling points. |
| Data.Result.SizeChart | Object | Apparel size chart (when applicable); fields include size / bust / waist / length. |
| Data.Result.PackageInfo | Object | Package weight / dimension info (when applicable). |
| Data.Result.TranslatedImag es | Object[] | Marketing images localized through Image Translation Pro. |

|   | Data.Result.BulletPoints |
|---|---|

|   | Data.Result.TranslatedImag | O |
|---|---|---|
| es |   |   |

Shared fields ( `Status` , `Images` , `Title` , `Attributes` , `CategoryPath` , `UsageMap` ) are the same as Lite.

**Error codes**

See Error codes.

**What's next**

Product Material Optimization Lite -- lowest-cost tier. Smart Image Generation API -- detailed field schema for the 7 atomic capabilities.

### Modify the permissions of an

**account**

You can modify the authorized databases and read/write permissions of standard accounts in the ApsaraDB RDS console based on your business requirements. **The permissions of a**

**privileged account can only be reset to the default settings but cannot be**

**modified.**

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Accounts**.
4. Find the account that you want to manage and click **Change Permissions** in the **Actions**
column.
5. In the panel that appears, adjust the account permissions and click **OK**.
Add or remove authorized databases: Select databases and click **>** or **<**. Set read/write permissions: In the **Authorized Databases** section, you can set the permissions to **Read/Write (DDL + DML)**, **Read-Only**, **DDL Only**, or **DML Only**. If you want to grant the same permissions on multiple databases to the account at a time, click the corresponding permission next to **Set All to** in the upper-right corner of the right-side box.

**Accounts and permissions**

| Accou nt type | Permi ssion type | Operation |   |   |   |   |
|---|---|---|---|---|---|---|
| Privil eged accou nt | None | SELECT | INSERT | UPDATE | DELETE | CREATE |
|   |   | DROP | RELOAD | PROCESS | REFERENCES | INDEX |
|   |   | ALTER | CREATE TEMPORARY TABLES | LOCK TABLES | EXECUTE | REPLICATION SLAVE |
|   |   | REPLICATION CLIENT | CREATE VIEW | SHOW VIEW | CREATE ROUTINE | ALTER ROUTINE |
|   |   | CREATE USER | EVENT | TRIGGER | None | None |
|   | Read- Only | SELECT | LOCK TABLES | SHOW VIEW | PROCESS | REPLICATION SLAVE |
|   |   | REPLICATION CLIENT | None | None | None | None |
|   | Read/ Write (DDL + DML) | SELECT | INSERT | UPDATE | DELETE | CREATE |
|   |   | DROP | REFERENCES | INDEX | ALTER | CREATE TEMPORARY TABLES |
|   |   | LOCK TABLES | EXECUTE | CREATE VIEW | SHOW VIEW | CREATE ROUTINE |
|   |   | ALTER ROUTINE | EVENT | TRIGGER | PROCESS | REPLICATION SLAVE |
|   | nt Version: |   |   |   |   |   |

| Stand ard accou nt |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   |   | REPLICATION CLIENT | None | None | None | None |
|   |   | CREATE | DROP | INDEX | ALTER | CREATE TEMPORARY TABLES |
|   | DDL Only |   |   |   |   |   |
|   |   | LOCK TABLES | CREATE VIEW | SHOW VIEW | CREATE ROUTINE | ALTER ROUTINE |
|   |   | PROCESS | REPLICATION SLAVE | REPLICATION CLIENT | None | None |
|   | DML Only | SELECT | INSERT | UPDATE | DELETE | CREATE TEMPORARY TABLES |
|   |   | LOCK TABLES | EXECUTE | SHOW VIEW | EVENT | TRIGGER |
|   |   | PROCESS | REPLICATION SLAVE | REPLICATION CLIENT | None | None |

### Product Material Optimization

**Lite**

The **lowest-cost** tier of the one-click cross-platform material optimization service. Given a 1688 product URL, produce TEMU-ready titles, attributes, hero images, SKU images, detail images, and copy. Uses the official Lowest Cost workflow: filtering and light processing, no high-cost image translation. Asynchronous.

**Endpoints**

**Submit optimization task**

```
POST /ai/material/optimization/lite
```

**Query optimization result**

```
POST /ai/material/optimization/lite/result
```

**Use cases**

Cross-border listing: 1688 → TEMU broad assortment publishing. High-SKU bulk listing, entry-level AI processing in ERP/SaaS pipelines. High daily volume but lower marketing performance bar. Filter out watermark / non-compliant images and pick clean originals; skip AI generation.

**Workflow**

The end-to-end Lowest Cost workflow:
1. Parse the 1688 product URL: extract title / SKU / hero image / detail images / attributes.
2. Filter text and apply SEO optimization against the TEMU blacklist and compliance rules.
3. Detect watermark / logo / Chinese copy in images; **prefer clean originals and skip**
**image translation** (high-converting marketing-text images may be filtered out).
4. Apply category matching, attribute filling, and multi-language localization to the target
platform.
5. Output a standardized material package; delivered via API and / or Excel export.

**Request parameters**

Lite and Pro share the same 31-field schema; the difference is the server-side workflow. Core fields below; for the full schema see the Smart Image Generation API.

| Parameter | Type | Required | Description |
|---|---|---|---|
| ImageUrl | String | Yes | Image URL (or 1688 product URL parsed by the server). Resolution > 512×512; long side ≤ 1920; short side ≤ 1080; size ≤ 5 MB; png / jpeg / jpg / bmp / webp. |
| Ability | Number[] | Yes | AI capabilities to invoke: 1=element detection, 2=smart matting, 3=smart removal, 4=image translation Pro, 5=image expansion, 6=smart crop, 7=upscale. Lite typically omits 4. |
| TargetPlatform | String | Yes | Target listing platform. Only TEMU is supported today. |
| TargetLanguage | String | No | Target language for text localization. |

| s ( | ObjectDetectElements |   |   | , |
|---|---|---|---|---|
| TargetWidth |   |   |   |   |
|   |   | , |   |   |

| , | UpscaleFactor | , etc.) |
|---|---|---|

semantics as in the Smart Image Generation API.

**Response fields (query)**

| Field | Type | Description |
|---|---|---|
| Data.Status | String | Task state: RUNNING , COMPLETED , FAILED . |

|   | RUNNING |   |
|---|---|---|
| COMPLETED |   |   |

| psaraDB RDS for MySQL User G ide·Accounts |   | ApsaraDB for RD |
|---|---|---|
| Field | Type | Description |
| Data.Result.Images | Object[] | Processed image list (hero, SKU, detail). |
| Data.Result.Title | String | SEO-optimized title. |
| Data.Result.Attributes | Object[] | Target-platform attribute fills. |
| Data.Result.CategoryPath | String | Matched category path on the target platform. |
| Data.Result.UsageMap.Proce ssedImageCount | Number | Images processed (for billing reconciliation). |

|   | Data.Result.CategoryPath |
|---|---|

|   | Data.Result.UsageMap.Proce | Number |
|---|---|---|
| ssedImageCount |   |   |

**Lite vs Pro**

| Dimension | Lite (this API) | Pro |
|---|---|---|
| Workflow | Lowest Cost | Best Quality |
| Marketing copy in images | Images with marketing copy filtered out | Preserved and rewritten |
| Image Translation Pro | Not invoked | Invoked |
| Category-specific assets | None | Yes (size charts, etc.) |
| Best fit | Broad assortment, low ASP, high velocity | Brand, high ASP, high conversion |

**Error codes**

See Error codes.

**What's next**

Product Material Optimization Pro -- best-quality tier. Smart Image Generation API -- detailed field schema for the 7 atomic capabilities.

## Category Match

LLM-based cross-platform category matching. Given source-platform product info, automatically pick the best category on the target listing platform and return the full path, a confidence score, and the rationale. Synchronous. Only `TEMU` is supported today.

**Endpoint**

```
POST /ai/material/category/match
```

**Use cases**

Merchants relisting sourced goods need to map to the correct node in the target platform's category tree. Top sellers' internal bulk pipelines, ERP / SaaS-driven publishing, fast SMB single-item listing.

**Effect showcase**

| Case | Example image |
|---|---|
| 1688 USB fan → TEMU "Home Appliances > Heating, Cooling & Air Quality Appliances > Fans > USB Fans" | USB fan case |
| 1688 bracelet → TEMU "Clothing, Shoes & Jewelry > Women's Fashion > Women's Accessories > Women's Fashion Bracelets..." | Bracelet case |

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category (e.g., full 1688 category path). |
| ProductDescription | String | No | Product description. |
| SkuInfo | String | No | SKU information. |
| ProductAttributes | Object | No | Product attribute key- value pairs. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Full category path on the target platform, separated by > . |
| Data.CategoryName | String | Leaf category name. |
| Data.Confidence | Number | Confidence score (0-100). Recommend human review below 70. |
| Data.Reason | String | Match rationale. |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Heating, Cooling & Air Quality > Fans > USB Fans
```

`",`

```json
    "CategoryName": "USB Fans",
    "Confidence": 95,
    "Reason": "Title contains USB / fan keywords; source category is synonymous."
```

`}` `}`

**Error codes**

See Error codes.

**What's next**

Category Attribute Match API -- fill required attributes within the matched category.

### Category Attribute Match

Multimodal-LLM-based cross-platform category-attribute filling. Given source-platform product info (title, source category, description, SKU, attributes, up to 10 images), match the precise target-platform category and fill every required attribute, with a per-attribute confidence and rationale. Synchronous.

**Endpoint**

```
POST /ai/material/category/attribute
```

**Use cases**

1688 → TEMU cross-platform listing where platform categories differ significantly and have complex hierarchical relations (material → wood species → density). Top sellers' bulk publishing, ERP / SaaS integrations, fast SMB single-item listing.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ProductTitle | String | Yes | Product title. |
| SourceCategory | String | Yes | Source-platform category path. |
| ProductDescription | String | No | Product description. |
| SkuInfo | Object[] | No | SKU list (spec + price per item). |
| ProductAttributes | Object | No | Source-platform attribute key-value pairs. |
| ImageUrls | String[] | No | Up to 10 image URLs. The multimodal model infers attributes from images. |
| TargetPlatform | String | Yes | Listing platform. Only TEMU today. |

|   | ProductDescription |
|---|---|

|   | ProductAttributes |
|---|---|

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.CategoryPath | String | Matched precise category path on the target platform. |
| Data.Attributes | Object[] | Filled attributes. Each item has Name , Value , Confidence (0-100), Reason , and SourceMatched (whether the value reused a source- platform attribute). |

**Response example**

`{`

```json
  "Code": "Success",
  "Data": {
    "CategoryPath": "Home Appliances > Fans > USB Fans",
    "Attributes": [
      { "Name": "Battery Type", "Value": "Lithium-Ion", "Confidence": 92, "Reason": "Ti
tle and image both indicate rechargeable", "SourceMatched": false },
      { "Name": "Connectivity",  "Value": "USB Type-C",  "Confidence": 88, "Reason": "P
ort visible in image", "SourceMatched": true }
```

`]` `}` `}`

**Error codes**

See Error codes.

**What's next**

Category Match API -- category match alone.

### Smart Matting

Automatically detect the salient subject and separate it from the background. Supports transparent / white / custom-color output. Accuracy > 95% for hard cases (hair, translucent objects, fur). Synchronous.

**Endpoint**

```
POST /ai/image/matting
```

**Capability cover**

Smart Matting cover

**Effect comparison**

| Original | After matting |
|---|---|
| Original 1 | After matting 1 |
| Original 2 | After matting 2 |

**Use cases**

Asset retouching -- swap backgrounds, add shadows after isolating the subject. Bulk asset processing -- batch background swaps for ads and posters.

**Core capabilities**

**Precise subject detection** -- > 95% accuracy on hair, transparent, and fur cases.
**Smart edge refinement** -- handles aliased and semi-transparent regions (smoke, glass)
with natural transitions.
**Multi-format output** -- transparent PNG, white background, or custom background color.

**Request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| ImageUrl | String | Yes | Image URL. Resolution > 512×512; long side ≤ 1920; short side ≤ 1080; size ≤ 5 MB; png / jpeg / jpg / bmp / webp. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| BackGroundType | String | Yes | Background type: WHITE BACKGROUND _ , TRANSPARENT , or CUSTOM COLOR _ (combined with BackGroundColor ). |
| BackGroundColor | String | No | Custom background color, 6-digit hex RGB (e.g., FF5733 ). Only when BackGroundType=CUS TOM COLOR . _ |

|   |   | BackGroundType=CUS |   |
|---|---|---|---|
|   | TOM COLOR _ |   |   |

**Response fields**

| Field | Type | Description |
|---|---|---|
| Data.ImageUrl | String | Matted image URL (signed OSS link). |
| Data.UsageMap.ProcessedIma geCount | Number | Images processed (for billing). |

|   | Data.UsageMap.ProcessedIma | Numbe |
|---|---|---|
| geCount |   |   |

**Error codes**

Common: `InvalidParameter` (image exceeds limits), `DownstreamUnavailable` (image download failed). See Error codes.

**What's next**

Smart Image Generation API -- orchestrate matting with the other 6 capabilities asynchronously.

## Size Chart Extraction

Use a multimodal LLM to extract structured size-chart and package-dimension data from

| ColumnNameList |   | t |
|---|---|---|
| n; |   |   |

images. `ColumnNameList` targets specific columns (e.g., Size, Bust, Length) for precise extraction; `LanguageModel` controls output language (Chinese, English, or original). Asynchronous: submit, then poll.

**Endpoints**

**Submit extraction task**

```
POST /ai/image/size-chart/extraction
```

**Query extraction result**

```
POST /ai/image/size-chart/extraction/result
```

**Input example**

Size chart input example

**Use cases**

Apparel category size-chart text-ification. Bulk structuring of package weight / dimension info.

**Request parameters (submit)**

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| ImageUrl | String | Yes |   | URL of the image containing the size chart. |   |   |
| ColumnNameList | String[] | No |   | Target columns to extract (e.g., ["Size", "Bust", "Length"] ). Omit to extract all columns. |   |   |
|   |   |   |   |   | ["Size", "Bust", |   |
|   |   |   |   | "Length"] |   |   |
| LanguageModel | String | No |   | Output language: cn or en . Omit to keep the original language. |   |   |

**Request parameters (query)**

| Parameter | Type | Required | Description |
|---|---|---|---|
| TaskId | String | Yes | Task ID returned by the submit endpoint. |

**Response fields (query)**

The response carries the raw multimodal-model structure (snake_case), which differs from the PascalCase convention used elsewhere: `{`

```json
  "Code": "Success",
  "Data": {
    "message": {
      "<ImageUrl>": {
        "size_chart": [
```

`{`

```json
            "Weight":  { "unit": "kg", "upper_value": 47.5, "lower_value": 40 },
            "Length":  { "unit": "CM", "value": 81 },
            "Size":    { "value": "S" },
            "Waist (stretched)": { "unit": "CM", "value": 58 }
```

`}` `],`

```json
        "intersection_attributes": ["Size", "Length", "Waist (stretched)", "Weight"],
        "size_chart_attributes":   ["Size", "Length", "Waist (stretched)", "Weight"]
```

`}` `},`

```json
    "usageMap": { "ProcessedImageCount": 1 }
```

`}` `}`

| : message.<ImageUrl>.size chart (extracted rows), intersection attributes _ _ tersecting ColumnNameList ), size chart attributes (columns actually _ _ usageMap.ProcessedImageCount (usage). | message.<ImageUrl>.size chart _ |   |   |   | (extracted rows), | intersection attributes _ |
|---|---|---|---|---|---|---|
|   |   | ColumnNameList | ), |   |   |   |
| usageMap.ProcessedImageCount |   |   |   |   |   |   |

**Error codes**

See Error codes.

**What's next**

Size Chart Detection API -- screen images first to save cost before extraction.

### Change the endpoint and port

**number of an instance**

This topic describes how to view and change the endpoint and port number of an ApsaraDB RDS instance.

**View the endpoint and port number**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the **Basic Information** section, view the internal and public endpoints and port
numbers.

**Change the endpoint and port number of an instance**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Connection**.
4. In the upper-right corner of the Database Connection section, click **Change Endpoint**.
5. In the dialog box that appears, set Connection Type, Endpoint, and Port, and then click **OK**.

**Note**

The prefix of an endpoint must be 8 to 64 characters in length and can contain letters, digits, and hyphens (-). It must start with a lowercase letter. The port number must be a value within the range of 1000 to 5999.

### Apply for and release an

**internal endpoint or a public**

**endpoint for an instance**

ApsaraDB RDS supports two types of endpoints: internal endpoints and public endpoints. The initial endpoint type of an ApsaraDB RDS instance depends on the network environment selected during instance creation. You can dynamically adjust the network access policies based on your business requirements. This ensures data security and enhances connection flexibility.

**Apply for an internal endpoint or a public endpoint**

If you set **Network Connection Type** to **Public network connection** when you create an ApsaraDB RDS instance, the database system assigns a public endpoint to the instance, and you can apply for an internal endpoint. Otherwise, the database system assigns an internal endpoint to the instance, and you can apply for a public endpoint. 1. 2.
3. In the left-side navigation pane, click **Database Connection**.
4. Apply for a public or internal endpoint based on your business requirements, and then click
**OK**.
To apply for a public endpoint, click **Apply for Public Endpoint**. To apply for an internal endpoint, click **Apply for Internal Endpoint**.

**Release an internal endpoint or a public endpoint**

If an endpoint is no longer needed, you can release the endpoint to ensure instance security. 1. 2.
3. In the left-side navigation pane, click **Database Connection**.
4. Release a public or internal endpoint based on your business requirements, and then click
**OK**.
To release a public endpoint, click **Release Public Endpoint**. To release an internal endpoint, click **Release Internal Endpoint**.

**FAQ**

Can I change the endpoints and port numbers of my ApsaraDB RDS instance? You can change only the prefixes and port numbers of the endpoints. For more information, see Change the endpoint and port number of an instance. Can I set the endpoints of my ApsaraDB RDS instance to static IP addresses? No, you cannot set the endpoints of your ApsaraDB RDS instance to static IP addresses. Both primary/secondary switchovers and specification changes may cause changes to the IP addresses. We recommend that you connect to your ApsaraDB RDS instance by using an endpoint. This allows you to minimize the impact on your workloads and eliminates the need to modify the configuration data on your application. How do I connect to my ApsaraDB RDS instance by using a public endpoint? For more information, see Connect to an ApsaraDB RDS for MySQL instance.

### Use DMS to log on to an

**ApsaraDB RDS instance**

This topic describes how to use Data Management (DMS) to log on to an ApsaraDB RDS instance.

**Prerequisites**

An IP address whitelist is configured. For more information about how to configure an IP address whitelist, see Configure an IP address whitelist.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click **Log On to DB** in the upper-right corner of the page.
4. In the **Login instance** dialog box of the **DMS** console, check values of **Database type**,
**Instance Area**, and **Connection string address**. If the information is correct, enter
**Database account** and **Database password**, as shown in the following figure.

| Parameter | Description |
|---|---|
| Database type | The engine of the database. By default, the engine of the database to be connected is displayed. |
| Instance Area | The region where the instance is deployed. By default, the region of the current instance is displayed. |
| Connection string address | The endpoint of the instance. By default, the endpoint of the current instance is displayed. |
| Database account | The account of the database to be connected. |
| Database password | The password of the account used to connect to the database. |

5. Click **Login**.

**Note**

If you want the browser to remember the password, select **Remember**
**password** before you click **Login**.

### Configure the hybrid access

**solution for an instance**

This topic describes how to configure the hybrid access solution for an ApsaraDB RDS instance. This solution allows you to retain both the classic network endpoint and Virtual Private Cloud (VPC) endpoint of your ApsaraDB RDS instance. This way, you can migrate your ApsaraDB RDS instance from the classic network to a VPC without network interruptions.

**Background information**

When you migrate your ApsaraDB RDS instance from the classic network to a VPC, the internal classic network endpoint of the instance changes to the internal VPC endpoint. In this case, the endpoint remains unchanged, but the IP address that is bound to the endpoint changes. This change causes a network interruption of 30 seconds or less, and Elastic Compute Service (ECS) instances located in the classic network can no longer connect to your ApsaraDB RDS instance over an internal network. To facilitate a smooth migration, ApsaraDB RDS provides the hybrid access solution. Hybrid access refers to the ability of your ApsaraDB RDS instance to be connected by both ECS instances located in the classic network and ECS instances located in a VPC. During the validity period of the hybrid access solution, ApsaraDB RDS retains the internal classic network endpoint and generates an internal VPC endpoint. This prevents network interruptions when you migrate your instance from the classic network to a VPC. For security and performance purposes, we recommend that you use only the internal VPC endpoint. You must specify a validity period for the hybrid access solution. When the validity period expires, ApsaraDB RDS releases the internal classic network endpoint and applications are unable to use the endpoint to connect to your instance. Therefore, you must add the internal VPC endpoint to your applications before the validity period expires. This ensures a smooth migration and prevents interruptions to your workloads. For example, assume that a company uses the hybrid access solution to migrate its ApsaraDB RDS instance from the classic network to a VPC. During the validity period of the hybrid access solution, some applications use the internal VPC endpoint to connect to the ApsaraDB RDS instance, whereas the others continue to use the internal classic network endpoint to connect to the instance. When all applications of the company can use the internal VPC endpoint to connect to the instance, the internal classic network endpoint can be released. The following figure demonstrates the scenario.

**Limits**

During the validity period of the hybrid access solution, your ApsaraDB RDS instance has the following limits: The network type of the instance cannot be changed to classic network. The instance cannot be migrated to another zone.

**Prerequisites**

The ApsaraDB RDS instance resides in the classic network. Available VPCs and vSwitches exist in the zone where the ApsaraDB RDS instance resides. Your ApsaraDB RDS instance provides an internal endpoint. If no internal endpoint exists, you must apply for one. For more information, see Apply for and release an internal endpoint or a public endpoint for an instance.

**Change the network type from classic network to VPC**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Connection**.
4. On the Instance Connection tab, click **Switch to VPC**.
5. In the Switch to VPC dialog box, select a VPC and a vSwitch and specify whether to retain
the classic network endpoint. Clear or select the **Reserve Original Classic Network Endpoint** check box based on the details described in the following table.

| Action | Description |
|---|---|
| Clear the Reserve Original Classic Network Endpoint check box | The classic network endpoint is not retained and changes to a VPC endpoint. When you change the network type from classic network to VPC, a network interruption of 30 seconds occurs. When this occurs, ECS instances located in the classic network are disconnected from your ApsaraDB RDS instance. |
| Select the Reserve Original Classic Network Endpoint check box | The classic network endpoint is retained, and a new VPC endpoint is generated. In this case, your ApsaraDB RDS instance runs in hybrid access mode. Both ECS instances located in the classic network and ECS instances located in the selected VPC can access your ApsaraDB RDS instance over an internal network. When you change the network type from classic network to VPC, no network interruptions occur. ECS instances located in the classic network are still connected with your ApsaraDB RDS instance until the classic network endpoint expires. Specify the expiration date of the classic network endpoint. Before the classic network endpoint expires, you must add the new VPC endpoint to your applications that run on the ECS instances located in the selected VPC. This allows ApsaraDB RDS to migrate your workloads to the selected VPC without network interruptions. |

6. Add the internal IP addresses of ECS instances located in the selected VPC to an IP address
whitelist of the VPC network type. This allows the ECS instances to connect to your ApsaraDB RDS instance over an internal network. If no IP address whitelists of the VPC network type are available, create one. For more information, see Configure an IP address whitelist.

**Change the expiration date of the internal classic network**

**endpoint**

During the validity period of the hybrid access solution, you can change the expiration date of the classic network endpoint based on your business requirements. The expiration date is immediately recalculated starting from the day when you make the change. For example, assume that the classic network endpoint is configured to expire on August 18, 2017. On August 15, 2017, you increase the validity period of the classic network endpoint by 14 days. In this case, ApsaraDB RDS releases the classic network endpoint on August 29, 2017. To change the expiration date, perform the following operations:
1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Connection**.
4. Click **Change Expiration Time**.
5. In the **Change Expiration Time** dialog box, select an expiration date and click **OK**.

### Change the network type of

**an instance**

This topic describes how to change the network type of an ApsaraDB RDS instance between the classic network and Virtual Private Cloud (VPC).

**Background information**

Classic network: ApsaraDB RDS instances in the classic network are not isolated. To block unauthorized access to these instances, you must configure whitelists. VPC: A VPC is an isolated network environment that provides better security than the classic network. It allows you to customize route tables, CIDR blocks, and gateways. In addition, you can connect your data centers to Alibaba Cloud VPCs through Express Connect circuits or VPN connections, creating a virtual data center to facilitate the migration of applications to the cloud.

**Change the network type from VPC to classic network**

**Usage notes**

After you change the network type from VPC to classic network, the internal endpoint of your ApsaraDB RDS instance remains unchanged. However, the IP address that is associated with the internal endpoint changes. After you change the network type from VPC to classic network, Elastic Compute Service (ECS) instances located in the same VPC as your ApsaraDB RDS instance can no longer connect to your ApsaraDB RDS instance by using the internal endpoint. You must update the endpoint for the applications deployed on the ECS instances. When you change the network type, a network interruption of 30 seconds may occur. To avoid business interruption, we recommend that you change the network type during offpeak hours or make sure that your application is configured to automatically reconnect to the instance.

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Database Connection**.
4. On the right side of the page, click **Switch to Classic Network**.
5. In the message that appears, click **OK**.

**Change the network type from classic network to VPC**

1. 2.
3. In the left-side navigation pane, click **Database Connection**.
4. On the right side of the page, click **Switch to VPC**.
5. In the dialog box that appears, select a VPC and a switch, specify whether to **Retain**
**Original Classic Network Endpoint**, and then click **OK**.
For more information about **Retain Original Classic Network Endpoint**, see Configure the hybrid access solution for an instance.

### Change the VPC and vSwitch

**for an instance**

When your business network plan changes or you need to adjust the network environment of an ApsaraDB RDS instance, you can change the virtual private cloud (VPC) and vSwitch for the instance in the console.

**Prerequisites**

The instance is deployed in a VPC.

**Precautions**

**Transient network disconnections**: The switching process causes a transient network
disconnection of approximately 30 seconds. Ensure that your applications have an automatic reconnection mechanism and perform this operation during off-peak hours.
**VIP changes**: The virtual IP (VIP) changes after the switching. You must use the endpoint
to access the instance. Do not use an IP address for direct connection.
**Cache clearing**: You must clear the client cache promptly after the VIP changes.
Otherwise, the database may become read-only, and write operations will fail.
**Associated services**: Data Management Service (DMS) and Data Transmission Service
(DTS) may be briefly affected by a VIP change. They will automatically recover after the switching is complete. No manual intervention is required.

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Database Connection**. On the page that appears,
click **Switch vSwitch**.
4. Select a VPC and a vSwitch, and then click **OK**.
5. In the message that appears, click **OK**.

## Database proxy

### Configure a dedicated proxy

The dedicated proxy for ApsaraDB RDS for MySQL is a database middleware service built on isolated computing resources. It supports features such as read/write splitting, a connection pool, and consistency level control. The proxy endpoint remains stable for the lifetime of the proxy service, reducing the impact of backend topology changes on your application's connection configuration. By using dedicated proxy resources, you can reduce the risk of multi-tenant interference, scale specifications on demand, and improve both operational efficiency and concurrency.

**Use cases**

Distribute read/write workloads: When your application has significantly more read operations than write operations, you can automatically route read requests to read-only instances to reduce the load on the primary instance. Achieve elastic scaling with zero application changes: During high-traffic events like sales promotions, you can dynamically add or remove read-only instances without changing your application's connection configuration. Meet high-performance and high-stability requirements: If you require resource isolation, high concurrency capacity, and stability for the proxy layer, a dedicated proxy avoids the resource contention risks associated with a shared proxy.

**Usage notes**

| Category | Constraint | Description |
|---|---|---|
| Connection model | 1:N backend connection | A single proxy connection simultaneously consumes one backend connection from the primary instance and one from each read-only instance. The total number of effective connections is limited by the instance with the lowest specifications. We recommend using the same specifications for the primary and read-only instances before enabling the proxy. |
| Parameter consistency | max prepared stmt _ _ _ count | This parameter must have the same value on the primary instance and all read-only instances. Otherwise, prepared statement execution may fail. |
| Feature limitations | SSL/compression protocol | SSL encryption and the MySQL compression protocol are not supported. |
| Routing behavior | Multi- statements/stored procedure | After you execute these types of statements, all subsequent requests on the current connection are routed to the primary instance. To resume read/write splitting, you must disconnect and reconnect. |

| Routing behavior | Hint syntax | The proxy supports /*FORCE MASTER*/ _ and /*FORCE SLAVE*/ hints. These hints take _ precedence over the consistency level and transaction binding. Do not include environment variable statements, such as set names utf8 , in a hint. Doing so can cause routing errors. |
|---|---|---|
| Load distribution | Adding or restarting a read-only instance | The system does not automatically migrate existing connections to a new read-only instance. Only new connections participate in load balancing with the new instance. To apply the change immediately, restart your application or refresh its connection pool. |
| Consistency | Non-transactional reads | In read/write splitting mode, the proxy does not guarantee strong consistency for read requests outside of a transaction. If you require strict read consistency, wrap the relevant operations in a transaction. |
| Monitoring differences | show processlist | Executing this command through the proxy endpoint returns a consolidated view of sessions from all backend instances. |

|   | /*FORCE MASTER*/ _ |
|---|---|
| /*FORCE SLAVE*/ _ |   |

**Enable dedicated proxy**

1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. Click **Enable Now**.

**Modify proxy endpoint and port**

After you enable the dedicated proxy for your ApsaraDB RDS for MySQL instance, your application must connect to the database through the proxy endpoint. 1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, click **Modify Address** or **Modify Port**.
The dedicated proxy currently provides one proxy endpoint, and the read/write splitting feature is bound to this endpoint. Click the copy icon to copy the proxy endpoint to your clipboard.
5. Click **OK**.

**Change proxy instance specification**

1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, set the **Single-node Proxy Instance Specification CPU**
**(Cores)** parameter, and under **Adjustment Plan**, click **Apply**.
The recommended number of proxy nodes is 1/8 of the total CPU cores of the primary instance and all its read-only instances, rounded up. For example, if the primary instance has 8 CPU cores and a read-only instance has 4 CPU cores, the recommended number of proxies is ⌈(8 + 4) / 8⌉ = 2.

**Disable proxy service**

1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. In the upper-right corner of the page, click **Disable Proxy Service**.
5. Click **OK**.

**Important**

After you disable the dedicated proxy service, the proxy endpoint becomes unavailable,
**but the primary instance endpoint is not affected** . If you re-enable the service,
the system assigns a new proxy endpoint. Before disabling the service, switch your application to the primary instance endpoint or another available connection method.

### Configure a connection pool

If connections such as short-lived connections are frequently established between your application and ApsaraDB RDS for MySQL instance or the maximum number of connections that is allowed to the ApsaraDB RDS for MySQL instance is reached, you can use connection pooling of the database proxy feature. Connection pooling can reduce the frequency at which your application connects to the ApsaraDB RDS for MySQL instance, the main thread overhead of the ApsaraDB RDS for MySQL instance, and the total number of connections to the ApsaraDB RDS for MySQL instance. This topic describes the connection pooling feature of the ApsaraDB RDS for MySQL database proxy. This feature does not affect the connection pooling feature on the client side. If your client already supports connection pooling, you can choose not to use the connection pooling feature of the database proxy.

**Select connection pooling**

ApsaraDB RDS for MySQL supports transaction-level connection pooling and session-level connection pooling. You can determine whether to use connection pooling and the type of connection pooling based on your business requirements.

| Connection pooling type | Scenario |
|---|---|
| Transaction-level connection pooling | Short-lived connections are required in workloads, connections are frequently established, and the number of connections reaches the maximum number of connections supported by an ApsaraDB RDS for MySQL instance. Transaction-level connection pooling helps reduce main thread overhead and the total number of connections. |
| Session-level connection pooling | Short-lived connections are required in workloads, and connections are frequently established. However, the limits on transaction-level connection pooling affect your workloads. Session-level connection pooling only reduces main thread overhead. |

| Connection pooling disabled | Persistent connections are required in workloads, a small number of connections are established, and connection pools, such as Druid, DBCP, c3p0, and HikariCP, are used in your applications. |
|---|---|

The following table describes the differences in working principles between transaction-level connection pooling and session-level connection pooling.

| Type | Sessions share backend connections | Time when backend connection s are used | Time when backend connections are reclaimed | Mapping between sessions and backend connections |
|---|---|---|---|---|
| Transa ction- level | Yes | A transaction is being processed. | A transaction is complete. The session may not end. | N:1 |
| Sessio n-level | No | A session is being established | A session ends. | N:N |

**Prerequisites**

The database proxy feature is enabled for your ApsaraDB RDS for MySQL instance.

**Usage notes**

After the connection pooling type is changed, the modification takes effect only for new connections. The connection pooling feature does not support IP-specific permissions for an account. If you enable the connection pooling feature and grant access permissions on a database or a table to an account that uses different IP addresses, a permission error may occur. For example, an account has permissions on database_a when it logs in from the 192.xx.xx.1 IP address, but the account does not have permissions on database_a when it logs in from the 192.xx.xx.2 IP address. In this case, permission errors may occur when the existing connections are reused. The connection pooling feature cannot solve the problem of connection accumulation that is caused by a large number of slow SQL queries. We recommend that you optimize related SQL statements or troubleshoot the issue on the ApsaraDB RDS for MySQL instance.

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, configure the Connection Pool parameter. The following options
are available: Disable (default value) Enable Transaction Connection Pool Enable Session Connection Pool

### Set the consistency level

ApsaraDB RDS for MySQL uses Binlog replication to synchronize data between the primary node and read-only nodes. When a transaction is committed on the primary node, the generated Binlog event is sent to the read-only nodes. The read-only nodes then apply this event to synchronize with the primary node. Although Binlog-based replication ensures eventual consistency, data on read-only nodes may lag under high concurrency or heavy loads, which can lead to inconsistent reads. To address data inconsistency, the ApsaraDB RDS for MySQL database proxy offers three consistency levels: eventual consistency, session consistency, and global consistency.

**Choose a consistency level**

The higher the consistency level (global consistency > session consistency > eventual consistency), the lower the read/write splitting performance. In most cases, session consistency is recommended. It has a minor performance impact and is suitable for most use cases. If your application requires strong consistency across different sessions and has a low write workload, you can choose global consistency.

| Consist ency level | Impact on performanc e | Consisten cy strength | Consistency scope | Use cases |
|---|---|---|---|---|
| Eventual consiste ncy (default) | None | Low | Consistent final state | For applications with weak consistency requirements that aim to reduce the load on the primary node by offloading more read requests to read-only nodes. |
| Session consiste ncy | Medium | Medium | Consistent within a single session | For applications that have consistency dependencies within a single session. |
| Global consiste ncy | High | High | Consistent across sessions | For read-heavy applications that have consistency dependencies between different sessions. |

**Prerequisites**

The database proxy is enabled.

**Usage notes**

When using session consistency or global consistency, the proxy waits for data positions to synchronize (up to the consistent read timeout), which can increase application latency. If a read-only node experiences replication lag, using global consistency can route more read requests to the primary node. This increases the load on the primary node and can further increase application latency.

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Proxy Service** tab, set the **Consistency Level**.
Eventual Consistency (default) Enable Session Consistency Enable Global Consistency

### Read/write splitting

#### Enable read/write splitting

This topic describes the read/write splitting feature. This feature allows ApsaraDB RDS to route read and write requests to the primary and read-only instances based on the dedicated proxy endpoint (also called read/write splitting endpoint).

**Prerequisites**

The database proxy or dedicated proxy feature is enabled. For more information, see Enable dedicated proxy or Enable dedicated proxy. At least one read-only instance is created. For more information about how to create a read-only instance, see Create a read-only instance.

**Background information**

If your database system receives a large number of read requests and a small number of write requests, a single primary ApsaraDB RDS instance may fail to process read requests and your workloads may be interrupted. In this case, you can create one or more read-only ApsaraDB RDS instances to offload read requests from the primary instance and increase the read capability of your database system. For more information, see Create a read-only instance. After you create read-only instances, you can enable read/write splitting. In this case, a read/write splitting endpoint is provided. After you add the endpoint to your application, write requests are routed to the primary instance and read requests are routed to the read-only instances.

**Differences between the read/write splitting endpoint and the**

**internal and public endpoints**

After you enable read/write splitting and add the read/write splitting endpoint to your application, all requests are first routed to this endpoint, and then to the primary and readonly instances based on the request types and the read weights of these instances. If the internal or public endpoint of the primary instance is added to your application, all requests are routed to the primary instance. To implement read/write splitting, you must add the endpoints and read weights of the primary and read-only instances to your application.

**Logic to route requests**

The following requests are routed only to the primary instance: All requests that are used to execute DML statements such as INSERT, UPDATE, DELETE, and SELECT FOR UPDATE. All requests that are used to execute DDL statements, such as the DDL statements that are used to create databases or tables, delete databases or tables, and change schemas or permissions. All requests that are encapsulated in transactions. Requests that are used to call user-defined functions. Requests that are used to run stored procedures. Requests that are used to execute EXECUTE statements. Requests that are used to run multi-statement queries. For more information, see Multistatement. Requests that involve temporary tables. Requests that are used to execute SELECT last_insert_id() statements. All requests that are used to query or reconfigure user variables. Requests that are used to execute SHOW PROCESSLIST statements. Requests that are used to execute KILL statements in SQL. These statements are different from the KILL commands in Linux. The following requests are routed to the primary instance or its read-only instances: Read requests that are not encapsulated in transactions. Requests that are used to execute COM_STMT_EXECUTE statements. The following requests are routed to all the instances: All requests that are used to modify system variables. Requests that are used to execute USE statements. Requests that are used to execute COM_STMT_PREPARE statements. Requests that are used to execute COM_CHANGE_USER, COM_QUIT, and COM_SET_OPTION statements.

**Benefits**

Easier maintenance by using a unified endpoint If you do not enable the read/write splitting feature, you must add the endpoints of the primary and read-only instances to your application. This way, your database system routes write requests to the primary instance and read requests to the read-only instances. If you enable the read/write splitting feature, you can use a dedicated proxy endpoint to implement read/write splitting. After your application is connected to this endpoint, your database system routes read and write requests to the primary and read-only instances based on the read weights of these instances. This reduces maintenance costs. You can also create read-only instances to improve the read capability of your database system. You do not need to modify the configuration data on your application. Higher performance and lower maintenance costs by using a native link You can build your own proxy layer on the cloud to implement read/write splitting. In this case, data needs to be parsed and forwarded by multiple components before the data reaches your database system. As a result, response latencies increase. The read/write splitting feature is embedded in the ApsaraDB RDS ecosystem to reduce response latencies, increase processing speeds, and reduce maintenance costs. Ideal in a variety of use scenarios based on configurable read weights and thresholds You can specify the read weights of the primary and read-only instances. You can also specify the latency threshold for data replication to the read-only instances. High availability based on instance-level health checks The read/write splitting feature enables ApsaraDB RDS to actively check the health status of the primary and read-only instances. If a read-only instance unexpectedly breaks down or its data replication latency exceeds the specified threshold, ApsaraDB RDS stops routing read requests to the instance. ApsaraDB RDS redirects read requests that are destined for the faulty read-only instance to healthy instances in your database system. This ensures service availability in the event of faults on individual read-only instances. After the faulty read-only instance is recovered, ApsaraDB RDS resumes routing read requests to the instance.

**Note**

To avoid single points of failure (SPOFs), we recommend that you create at least two read-only instances.

**Precautions**

When you change the specifications of your ApsaraDB RDS instance or its read-only instances, a service interruption may occur. After you create a read-only instance, only the requests over new connections can be routed to the read-only instance. The dedicated proxy endpoint does not support SSL encryption. The dedicated proxy endpoint does not support compression. If a dedicated proxy endpoint is used to connect to your database system, all the requests that are encapsulated in transactions are routed to the primary instance. If a dedicated proxy endpoint is used to implement read/write splitting, the read consistency of the requests that are not encapsulated in transactions cannot be ensured. If you require read consistency for these requests, you can encapsulate these requests in transactions. If a dedicated proxy endpoint is used for connection, the `SHOW PROCESSLIST` statement returns a result set for each query. The result set consists of the query results from the primary and read-only instances. If the short-lived connection optimization feature is enabled, the `SHOW PROCESSLIST` statement may return idle connections. If you execute multi-statements or stored procedures, the read/write splitting feature is disabled and all subsequent requests over the current connection are routed to the primary ApsaraDB RDS instance. To enable the read/write splitting feature again, you must close the current connection and establish a new connection. The dedicated proxy feature supports the `/*FORCE_MASTER*/` and `/*FORCE_SLAVE*/` hints. However, requests that contain hints have the highest route priorities and are not constrained by consistency or transaction limits. Before you use these hints, you must check whether these hints are suitable for your workloads. A hint cannot contain statements that change environment variables. An example is `/*FORCE_SLAVE*/ set names` utf8; . Otherwise, an error may occur in the subsequent procedure.

**Prerequisite**

A read-only instance is created for the primary instance. For more information, see Create a read-only instance.

**Enable read/write splitting**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Read/Write Splitting** tab, click **Enable now**.
5. Configure the parameters described in the following table.

| Paramete r | Description |
|---|---|
| Latency Threshold | The maximum latency that is allowed for data replication from the primary instance to its read-only instances. If the latency of data replication to a read-only instance exceeds the specified threshold, ApsaraDB RDS stops routing read requests to the instance. This applies even if the instance has a high read weight. Valid values: 0 to 7200. Unit: seconds. The read-only instances may replicate data from the primary instance at a specific latency due to SQL statement execution limits. We recommend that you set this parameter to a value that is greater than or equal to 30. |

| Read Weight Distributi on | The read weight of each instance in your database system. A higher read weight indicates more read requests to process. For example, assume that your primary instance has three attached read-only instances, and the read weights of the primary and read-only instances are 0, 100, 200, and 200. In this case, your primary instance processes only write requests, and the three read-only instances process all of the read requests at a ratio of 1:2:2. Automatic Distribution: Your database system assigns a read weight to each instance based on the instance specifications. After you create a read-only instance, your database system assigns a read weight to the read-only instance and adds the read-only instance to the read/write splitting link. Customized Distribution: You must manually specify the read weight of each instance. Valid values: 0 to 10000. After you create a read-only instance, ApsaraDB RDS sets the read weight of the read-only instance to 0. You must manually modify the read weight of the created read-only instance. |
|---|---|

6. Click **OK**.

#### Configure read/write splitting

This topic describes how to configure the latency threshold and specify read weights for an ApsaraDB RDS instance in the ApsaraDB RDS console.

**Prerequisites**

Read/write splitting is enabled. For more information, see Enable read/write splitting.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Database Proxy**.
4. On the **Read/Write Splitting** tab, click **Configure Read/Write Splitting**.
5. Configure the parameters described in the following table.

| Paramete r | Description |
|---|---|
| Latency Threshold | The maximum latency that is allowed for data replication from the primary instance to the read-only instances. If the latency at which a read-only instance replicates data from the primary instance exceeds the value of this parameter, the system no longer routes read requests to the read-only instance regardless of the read weight of the read-only instance. Valid values: 0 to 7200. Unit: seconds. The read-only instances may replicate data from the primary instance at a specific latency. The latency varies based on the statuses of the SQL statements that are executed. We recommend that you set this parameter to a value that is greater than or equal to 30. |

| Read Weight Distributi on | The method that is used to assign read weights. A higher read weight indicates that more read requests need to be processed. For example, three read-only instances are attached to the primary instance, the read weight of the primary instance is 0, and the read weights of the three read-only instances are 100, 200, and 200. In this case, the primary instance processes only write requests, and the three read-only instances process all read requests based on the 1:2:2 ratio. Automatic Distribution: The system automatically assigns a read weight to each instance in your database system based on the specifications of each instance. After you create a read-only instance, the system automatically assigns a read weight to the read-only instance and adds the read-only instance to the read/write splitting link. Customized Distribution: You must specify a read weight for each instance in your database system. Valid values: 0 to 10000. After you create a read-only instance, ApsaraDB RDS sets the read weight of the read-only instance to 0 by default. You must manually modify the read weight of the created read-only instance. |
|---|---|

6. Click **OK**.

#### Disable read/write splitting

This topic describes how to disable the read/write splitting feature of an ApsaraDB RDS instance in the ApsaraDB RDS console.

**Prerequisites**

Read/write splitting is enabled. For more information, see Enable read/write splitting.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Instance List**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
4. On the **Read/Write Splitting** tab, click **Disable Read/Write Splitting**.
5. In the message that appears, click **Confirm**.

## Monitoring and alerts

### View monitoring data

ApsaraDB RDS for MySQL allows you to view performance monitoring data for system resources, engines, and deployments to track the running status of instances.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Monitoring and Alerts**.
4. On the **Monitoring and Alerts** page, select **Resource Monitoring**, **Engine Monitoring**,
or **Deploy Monitoring**, and then specify a time range to view the corresponding monitoring data. The following table describes each monitoring item.

**Resource monitoring**

| Monitoring item | Description |
|---|---|
| Disk Space | The disk space usage of the instance, including the total disk, data, log, temporary file, and system file space usage. Unit: MB. |
| IOPS | The number of I/O requests per second for the instance. Unit: requests/s. |
| Total Connections | The current connection status of the instance, showing the number of active and total connections. |
| CPU Utilization and Memory Usage | The CPU and memory utilization of the instance, excluding the resources that the operating system occupies. |
| Network Traffic | The inbound and outbound traffic per second for the instance. Unit: KB/s. |

**Engine monitoring**

| Monitoring item | Description |
|---|---|
| Transactions per Second (TPS)/Queries per Second (QPS) | The average number of transactions per second and the average number of SQL statements executed per second. |
| InnoDB Buffer Pool Read Hit Ratio, Usage Ratio, and Dirty Block Ratio | The read hit ratio, usage, and dirty block ratio of the InnoDB buffer pool. |

| InnoDB Read/Write Volume | The amount of data that InnoDB reads and writes per second. Unit: KB. |
|---|---|
| InnoDB Buffer Pool Requests | The number of read and write operations that InnoDB performs per second. |
| InnoDB Log Reads/Writes/fsync Operations | The number of physical writes to the log file, the number of log write requests, and the number of completed fsync operations to the log file per second for InnoDB. |
| Temporary Tables Automatically Created on Hard Disk when MySQL Statements are Executed | The number of temporary tables that the database automatically creates on disk when it executes SQL statements. |
| MySQL COMDML _ | The number of SQL statements that the database executes per second, including: Insert, Delete, Insert Select, Replace, Replace Select, Select, and _ _ Update. |
| MySQL RowDML _ | The number of row-level operations that InnoDB performs per second, including: The number of physical writes to the log file per second. The number of rows read, inserted, updated, and deleted from InnoDB tables per second. |
| MyISAM Reads and Writes | The number of operations that MyISAM performs per second, including: The number of read and write operations from the buffer pool per second. The number of read and write operations from the disk per second. |
| MyISAM Key Buffer Read/Write/Usage Ratio | The average usage, read hit ratio, and write hit ratio of the MyISAM Key Buffer per second. |
| MySQL Thread Status | The thread status information of the MySQL instance, including the number of currently connected threads (Threads connected) and _ the number of active threads executing queries (Threads running). _ |
| Redo Log Size Written by InnoDB per second | The amount of data that the InnoDB storage engine writes to the redo log per second. This metric evaluates the transaction write frequency and data change intensity. Unit: bytes/s. |
| MySQL ROW LOCK _ _ | The InnoDB row lock statistics. This metric evaluates lock contention. |

| MySQL SelectScan _ | The query scan statistics that MySQL executes per second. This metric evaluates whether queries use indexes effectively. |
|---|---|

**Deployment monitoring**

| Monitoring item | Description |
|---|---|
| Replication Thread Status of Secondary Instances | The replication thread status of the secondary node, including: I/O thread: 1 indicates a normal status, and 0 indicates a lost thread. SQL thread: 1 indicates a normal status, and 0 indicates a lost thread. |
| Replication Latency of Secondary Instances | The replication latency of the secondary node. Unit: seconds. |

### Configure an alert rule

This topic describes how to create alert rules in the ApsaraDB RDS console. This allows you to identify and handle exceptions at the earliest opportunity.

**Procedure**

1. Log on to the ApsaraDB RDS console.
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

## Data security

### Configure an IP address

**whitelist**

After you create an ApsaraDB RDS instance, you must add the IP addresses or CIDR blocks that are allowed to access the instance to the IP address whitelist of the instance to ensure database security and reliability.

**Background information**

Whitelists make your ApsaraDB RDS instance more secure. We recommend that you maintain whitelists on a regular basis. When you configure IP address whitelists for your ApsaraDB RDS instance, the workloads on the instance are not affected. You can configure a whitelist in two modes: Configure an IP address whitelist: Add IP addresses to allow only specified origins to connect to the ApsaraDB RDS instance. Configure an Elastic Compute Service (ECS) security group: Add an ECS security group for the ApsaraDB RDS instance to allow all ECS instances in the security group to connect to the ApsaraDB RDS instance.

**Usage notes**

**Default group restrictions**: The default whitelist group ( `default` ) can be modified or
cleared, but it cannot be deleted.
**Quantity limits**: A maximum of 1,000 IP addresses or CIDR blocks can be added to a
whitelist. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks (such as `192.168.1.0/24` ) to reduce the number of entries.
**Format requirements**: You must separate multiple IP addresses or CIDR blocks with
commas (,). Do not include spaces before or after the commas.

| dress to the | default |   |
|---|---|---|
| 127.0.0.1 |   |   |
|   |   | . |

**Override mechanism**: After you add any new IP address to the `default` group, the
system automatically removes the default deny rule `127.0.0.1` .
**Prerequisites for network connectivity**: If you want to connect an ECS instance to an
ApsaraDB RDS instance by using an internal endpoint, make sure that the two instances are in the same region and have the same network type (such as VPC). Otherwise, the connection fails.

**Configure a standard IP address whitelist**

1. 2.
3. In the left-side navigation pane, click **Data Security**.
4. On the **Whitelist Settings** tab, click **Modify**.

**Note**

Click **Create Whitelist** to create a custom group.
5. In the **Modify Whitelist** dialog box, enter the IP addresses or CIDR blocks that are allowed
to connect to your ApsaraDB RDS instance, and then click **OK**. Then, click OK to save the configuration. If you enter a CIDR block such as 10.10.10.0/24, all IP addresses in the 10.10.10.XX range can access your ApsaraDB RDS instance. If you click **Add Internal IP Addresses of ECS Instances**, the IP addresses of all ECS instances that are created within the current Alibaba Cloud account appear. Then, you can select the IP addresses and add them to an IP address whitelist.

### Configure SSL encryption

This topic describes how to make data transmission more secure by configuring Secure Sockets Layer (SSL) encryption. You must enable SSL encryption and install SSL certificates that are issued by certificate authorities (CAs) to the required applications. SSL is used to encrypt connections at the transport layer and enhance the security and integrity of the transmitted data. However, SSL encryption increases the round-trip time.

**Prerequisites**

Your ApsaraDB RDS instance runs one of the following MySQL versions and RDS editions: MySQL 8.0 on RDS High-availability Edition (with local SSDs) MySQL 5.7 on RDS High-availability Edition (with local SSDs)

**Usage notes**

An SSL certificate remains valid for one year. Before the used SSL certificate expires, you must update the validity period of the SSL certificate. If you do not update the expired SSL certificate, the RDS instance still runs as expected and no security risks occur. However, your application cannot establish encrypted connections to the RDS instance. When the certificate is about to expire, Alibaba Cloud will notify you by sending emails or internal messages. You can view the internal messages on the Event Center page. SSL encryption may cause a sharp increase in CPU utilization. We recommend that you enable SSL encryption only if you want to encrypt the connections that are established to the public endpoint of your RDS instance. In most cases, connections that are established to the internal endpoint of your cluster are secure and do not require SSL encryption. SSL encryption is not supported for the connections to the read/write splitting endpoint of your RDS instance. If you disable SSL encryption, your RDS instance restarts. Proceed with caution.

**Enable SSL encryption**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. In the **SSL Settings** section, turn on **SSL Encryption**.
6. In the **Configure SSL Encryption** dialog box, select the endpoint for which you want to
enable SSL encryption and click **OK**.
7. Click Download CA Certificate to download the SSL CA certificate files in a compressed
package. The file that you downloaded is a package that contains the following files: P7B file: contains the server CA certificate that can be imported into a Windows operating system. PEM file: a CA certificate file that is used for an operating system or application that is not Windows-based. JKS file: an SSL certificate file that is stored in the Java-supported truststore. You can use this file to import the SSL certificate files from an SSL certificate chain into Java-based applications. The default password is apsaradb.

**Note**

If the JKS file is used in Java, you must modify the default JDK security configuration in JDK 7 and JDK 8. Open the `/jre/lib/security/java.security` file on the host where your application resides and modify the following configurations:

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224 jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

If you do not modify these configurations, the following error is reported. In most cases, other similar errors are also caused by invalid Java security configurations:

```
javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm c onstraints
```

**Configure an SSL certificate**

After SSL encryption is enabled, you must configure an SSL certificate on your application or client to connect to your RDS instance. In this topic, MySQL Workbench and Navicat are used as examples. If you want to use other applications or clients, see the related instructions. Perform the following steps to configure an SSL certificate on MySQL Workbench:
1. Start MySQL Workbench.
2. Choose **Database > Manage Connections**.
3. In the **Connection** section, click the **SSL** tab and configure the following parameters.
①: Enable **Use SSL**. ②: Import the SSL CA certificate file. Configure a certificate on Navicat
1. Start Navicat.
2. Right-click the database and select **Edit Connection**.
3. Click the **SSL** tab. Select the path of the PEM-formatted CA certificate and complete the
required settings based on the following figure.
4. Click **OK**.

**Note**

If the `connection is being used` error message is displayed, the previous session remains connected. In this case, you must restart Navicat.
5. Double-click the database to test whether the database is connected.

**Update the validity period of an SSL CA certificate**

**Note**

The **Update Validity** operation causes your RDS instance to restart. Proceed with caution.
1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. Click **Update Validity**.

**Disable SSL encryption**

**Note**

When you disable SSL encryption, your RDS instance restarts. In this case, the system triggers a primary/secondary switchover to reduce the impacts on your workloads. We still recommend that you disable SSL encryption during off-peak hours. Disabling SSL encryption enhances access performance but reduces security for the RDS instance. We recommend that you disable SSL encryption only in secure environments.
1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SSL** tab.
5. In the **SSL Settings** section, turn off **SSL Encryption**. In the message that appears, click
**OK**.

### Configure TDE

Transparent Data Encryption (TDE) allows you to perform real-time I/O encryption and decryption on data files. Data is encrypted before it is written to the disk and is decrypted when it is read from the disk to the memory. After you enable TDE for your RDS instance, the size of data files in your RDS instance does not increase. You can use TDE without the need to modify the configurations of your application.

**Prerequisites**

Your ApsaraDB RDS instance runs the RDS High-availability Edition with local disks. Key Management Service (KMS) is activated. If KMS is not activated, you can activate it as prompted when you enable TDE.

**Background information**

The key that is used for TDE is created and managed by KMS. ApsaraDB RDS does not provide the key or certificates that are required for TDE. In some zones, you can use an automatically generated key or a custom key that is generated from your own key material. After you select a key, you must authorize your RDS instance to use that key.

**Usage notes**

When TDE is being enabled, your ApsaraDB RDS instance is restarted and all services are disconnected. Make appropriate service arrangements before you enable TDE. Proceed with caution. After you enable TDE, you cannot disable TDE. After you enable TDE, you cannot change the key that is used for TDE. After you enable TDE, you must decrypt the data on your RDS instance if you want to restore the data to an on-premises database. For more information, see Decrypt a table. After you enable TDE, the CPU utilization of your RDS instance significantly increases. If you use an existing custom key for TDE, take note of the following information: If you disable the key, configure a plan to delete the key, or delete the key material, the key becomes unavailable. If your RDS instance restarts after you revoke the key, your RDS instance becomes unavailable. You must use an Alibaba Cloud account or an account to which the AliyunSTSAssumeRoleAccess policy is attached.

**Note**

For more information, see topics about key management in **Key Management**
**Service > User Guide**.

**Use a key that is automatically generated by Alibaba Cloud**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **TDE** tab.
5. In the **TDE Settings** section, turn on **TDE Status**.
6. In the dialog box that appears, select **Use Automatically Generated Key** and click **OK**.

**Note**

If the instance runs MySQL 5.7 on RDS High-availability Edition, you can select one of the following encryption methods: SM4 encryption AES_256_CBC encryption

**Use an existing custom key**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, find the instance
that you want to manage and click the ID of the instance or click **Manage** in the **Actions** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click Data Security.
4. Click the **TDE** tab.
5. In the **TDE Settings** section, turn on **TDE Status**.
6. In the dialog box that appears, select **Use an existing custom key** and click **OK**.

**Note**

If you do not have a custom key, you need to click **go to the KMS console** to create a CMK and import your own key material. For more information, see the **Create a key** section in **Key Management ServiceKey Management Service > User Guide**.

**Encrypt a table**

Log in to the database and execute the following statement to encrypt a table: MySQL 5.7 or MySQL 8.0

```
alter table <tablename> encryption='Y';
```

**Decrypt a table**

Execute the following statement to decrypt a table that is encrypted by using TDE: MySQL 5.7 or MySQL 8.0

```
alter table <tablename> encryption='N';
```

**FAQ**

After I enable TDE, can I use common database tools such as Navicat? Yes, after you enable TDE, you can use common database tools such as Navicat. After I enable TDE, why is my data still in plaintext? After you enable TDE, your data is stored in ciphertext. However, when the data is queried, it is decrypted and loaded in plaintext to the memory. A: TDE encrypts backup files to prevent data leaks. Before you restore the data of your ApsaraDB RDS instance from an encrypted backup file to your computer, you must decrypt the file. For more information, see the "Decrypt a table" section of this topic.

### Use the SQL audit feature

This topic describes how to use the SQL audit feature on an ApsaraDB RDS for MySQL instance. You can use the SQL audit feature to view the details about the SQL statements that are executed on your ApsaraDB RDS instance and audit the SQL statements on a regular basis. The SQL audit feature does not affect instance performance.

**Background information**

**Important**

You cannot view records generated before you enable the SQL audit feature. You can view the incremental data of your ApsaraDB RDS for MySQL instance in SQL audit logs or binary logs. However, these two methods differ in the following aspects:
**SQL audit logs** are similar to audit logs in MySQL. They record all DML and DDL operations
by using network protocol analysis. SQL audit does not parse the actual parameter values. If a large number of SQL statements are executed to query data, a small amount of data may be lost. The incremental data obtained by using this method may be inaccurate.
**Binary logs** record all add, delete, and modify operations that are performed in the
database and the incremental data that is used to restore data. Binary logs are temporarily stored in your instance after they are generated. The system transfers full binary log files to an Object Storage Service (OSS) bucket on a regular basis. The binary log files are stored in the OSS bucket for seven days. If data is being written to a binary log file, the file cannot be transferred. Therefore, after you click **Upload Binlogs** on the **Backup and**
**Restoration** page, some binary log files are not uploaded to the OSS bucket. You can use
this method to obtain accurate incremental data. However, you cannot use this method to obtain real-time logs.

**Usage notes**

By default, SQL audit is enabled. SQL audit logs are retained for seven days. The retention period of SQL audit log files is one hour. The system automatically deletes the SQL audit log files that are stored for longer than one hour. In the SQL audit feature, the maximum length of a single SQL statement is 4 KB.

**Disable the SQL audit feature**

If you no longer require the SQL audit feature, you can disable the feature to reduce costs.
1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Click **Export File** to export the SQL audit logs to your on-premises machine.
6. After the logs are exported, click **Disable SQL Auditing**.
7. In the message that appears, click **OK**.

**Important**

After the SQL audit feature is disabled, all SQL audit logs, including historical SQL audit logs, are deleted. Before you disable the SQL audit feature, we recommend that you export the SQL audit logs to your on-premises machine.

**Enable the SQL audit feature**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Click **Enable SQL Auditing**.
6. In the message that appears, click **OK**.
After you enable the SQL audit feature, you can query SQL statements based on filter criteria such as the time, database, user, and keyword.

**Change the storage location of audit logs**

By default, audit logs are stored in SLS-inner. You can switch them to an accessible SLS-PUB based on your business requirements.
1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Data Security**.
4. Click the **SQL Audit** tab.
5. Turn on the Enable Log Storage to SLS-PUB switch and click **OK**.

**Important**

The change cannot be reversed. Proceed with caution.

## Service availability

### Switch workloads between

**primary and secondary ApsaraDB**

**RDS instances**

This topic describes how to switch workloads between a primary ApsaraDB RDS for MySQL instance and its secondary instance. ApsaraDB RDS for MySQL supports both manual switchover and automatic switchover. After a switchover is complete, the primary ApsaraDB RDS for MySQL instance becomes the secondary instance.

**Feature overview**

ApsaraDB RDS for MySQL supports both manual switchover and automatic switchover.
**Automatic switchover**: By default, the automatic switchover feature is enabled. If the
primary ApsaraDB RDS for MySQL instance becomes faulty, ApsaraDB RDS automatically switches workloads over to the secondary instance.
**Manual switchover**: You can manually switch workloads between the primary and
secondary ApsaraDB RDS for MySQL instances at any time.

**Usage notes**

Data is synchronized between the primary and secondary ApsaraDB RDS instances in real time. The secondary instance serves only as a read-only instance or standby. We recommend that you do not modify the data of the secondary instance. If you modify the data of the secondary instance, the data of the primary instance may be accidentally deleted or overwritten, which may irreparably impact your workloads. If the secondary ApsaraDB RDS instance serves as a read-only instance, the secondary instance serves as the new primary instance after a primary/secondary switchover. We recommend that you plan the read and write workloads for the new primary instance before the switchover. We recommend that you reserve and plan resources in advance. During a switchover, your services may be interrupted. Make sure that your application is configured to automatically reconnect to the instance. If the primary ApsaraDB RDS instance is attached with read-only instances, the read-only instances need to re-establish the connections that are used for data replication and synchronize incremental data after a switchover. As a result, data synchronization to the read-only instances has a latency of a few minutes.

**Manually perform a primary/secondary switchover**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Service Availability**.
4. On the right side of the page, click **Switch Primary/Secondary Instance**.

**Note**

You may encounter one or two service interruptions during a switchover. Make sure that your application is configured to automatically reconnect to the instance.
5. In the dialog box that appears, configure the switchover time (**Switch Immediately** or
**Within Specified Time RangeCurrent Settings**), and then click **OK**.

### Change the data replication

**mode**

ApsaraDB RDS for MySQL allows you to change the data replication mode between the primary and secondary instances to meet the database availability and performance requirements of different business scenarios.

**Prerequisites**

The instance series is the High-Availability Edition.

**Data replication modes**

ApsaraDB RDS for MySQL supports the following two data replication modes:

**Semi-synchronous**

After the primary instance completes an update initiated by an application, it synchronously transmits logs to the secondary instance. The transaction commits once the secondary instance receives the log, without waiting for the secondary instance to apply the logs. When the secondary instance becomes unavailable or a network exception occurs between the primary and secondary instances, the semi-synchronous mode falls back to the asynchronous mode. Applicable scenario: We recommend the semi-synchronous mode for services that require high data consistency.

**Asynchronous**

When an application initiates an update request, the primary instance responds immediately after completing the operation and asynchronously replicates data to the secondary instance. The unavailability of the secondary instance does not affect operations on the primary instance. When the primary instance becomes unavailable, data inconsistency between the primary and secondary instances may occur briefly. Applicable scenario: You can select the asynchronous mode for services that require high response speed.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Service Availability**.
4. On the right side of the page, click **Change Data Replication Mode**.
5. In the pop-up dialog box, select a data replication mode and click **OK** twice in succession.
ation

## Database backup and

**restoration**

### Configure automatic backup

Automatic backup of ApsaraDB RDS supports full physical backups. ApsaraDB RDS automatically backs up data based on pre-configured policies. This topic describes how to configure a policy for automatic backup.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instance List page, find the
instance that you want to manage and click the ID of the instance or click **Management** in the **Operation** column to go to the **Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. Click the **Backup Settings** tab.
5. Click **Edit** and configure the following parameters.

**Note**

To ensure data security, the system compares the new backup cycle and time with the original settings and selects the most recent point in time to back up the data. Therefore, the next backup may still be performed based on the original backup cycle and time. For example, assume that the scheduled backup cycle and time are set to 19:00-20:00 every Wednesday. If you modify the backup cycle and time to 19:00-20:00 every Thursday before the scheduled backup occurs, the system still backs up data at the original scheduled time of 19:00-20:00 on Wednesday.

| Parameter | Description |
|---|---|
| Data Retention Period | The number of days for which data backup files are retained. Valid values: 7 to 730. Default value: 7. |
| Backup Cycle | The backup cycle. You can select one or more days within a week. |
| Backup Time | A period of time within a day. Unit: hours. We recommend that you back up data during off-peak hours. |
| Retention Period | The retention period of regular backup (hot backup) and whether to retain the data for a long time before the instance is released. Note Data backup sets that are retained for more than 730 days will be automatically converted to archived backups (cold backup). The retention period of archived backups is at least 30 days. |

ation

| Log Backup | Specifies whether to enable log backup. Important If you disable log backup, all the log backup files are deleted and you cannot restore data to a specific point in time. |
|---|---|
| Log Backup Retention Period | The number of days for which log backup files are retained. Valid values: 7 to 730. Default value: 7. |

6. Click **Save**.

### Manually back up an instance

Manual backup of ApsaraDB RDS supports both full physical and logical backups. This topic describes how to manually back up an ApsaraDB RDS instance.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. Click **Back Up Instance** in the upper-right corner.
4. In the dialog box that appears, set the backup mode and backup policy and then click **OK**.

**Note**

The following backup modes are available: Physical backup: directly backs up all files in all databases. Logical backup: extracts data from the databases by using SQL statements and backs up the data in the text format. If you select logical backup, you must select one of the following backup policies: Instance Backup: backs up the entire instance. Single-Database Backup: backs up one of the databases on the instance.

### Download data backup files

**and log backup files**

This topic describes how to download unencrypted data backup files and log backup files in the ApsaraDB RDS console to archive the files and restore data to an on-premises database.

**Limits**

| Database engine | Download of data backup files | Download of log backup files |
|---|---|---|

ation

| MySQL 5.7 on RDS High- availability Edition | Supported | Supported |
|---|---|---|
| MySQL 8.0 on RDS High- availability Edition | Supported | Supported |

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. In the left-side navigation pane, click **Instances**. On the Instances page, click the ID of the
instance that you want to manage, or click **Manage** in the **Actions** column to go to the
**Basic Information** page.
3. In the left-side navigation pane, click **Backup and Restoration**.
4. Click the Data Backup or Log Backup tab.
To download data backup files, click the **Data Backup** tab. To download log backup files, click the **Log Backup** tab.
5. Select a time range to which you want to restore the instance.
6. Find the data backup file or log backup file that you want to download, and click **Download**
**Instance Backup** or **Download** in the **Actions** column.

**Note**

If the Download button is unavailable, check whether the requirements in the Limits section are met. If you want to download data backup file and use the backup file to restore data, we recommend that you select the data backup file created closest to the point in time when the required data exists. If the log backup file is used to restore the data of your RDS instance to an onpremises database, take note of the following items: The instance ID of the log backup file must be the same as the instance ID of the backup set that you select. The start time of the log backup file must be later than the end time of the backup set that you select and earlier than the point in time to which you want to restore the data of your RDS instance.
7. In the dialog box that appears, click **Download**.

| Download method | Description |
|---|---|
| Download button | Use a browser to download the backup file. |

ation

| Download URL | Copy the download URL. If you want to use other tools to download the file, use this method. |
|---|---|

**Note**

If you use a Linux operating system, you can run the following command to download the file:

```
wget -c '<Download URL of the backup file>' -O <File name>
```

The -c option enables resumable download. The -O option saves the downloaded file by using a specified name. We recommend that you use the file name contained in the download URL. If the URL contains more than one parameter, we recommend that you enclose the URL in a pair of single quotation marks (').

### Upload binlogs

**Background information**

This topic describes how to upload binlog files to Object Storage Service (OSS).

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Backup and Restoration** to go to the **Backup and**
**Restoration** page.
4. In the upper-right corner of the page, click **Upload Binlogs**.
5. In the message that appears, click **Confirm**.

### Database recovery

Database recovery is the process of creating a new clone instance by copying the data and settings from a primary instance. A clone instance is primarily used to recover the primary instance's data or to create multiple identical instances.

**Prerequisites**

When you create a clone instance, the primary instance must meet the following conditions: The primary instance is in the **Running** state. No migration tasks are in progress. Both data backup and log backup are enabled. To clone an instance from a backup set, the primary instance must have at least one completed backup set. ation

**Background information**

You can create a clone instance from a backup set or to a specific point in time. A clone instance copies only the content of the primary instance, not the content of any read-only instances associated with the primary instance. The copied content includes the database information, account information, and instance settings of the primary instance, such as whitelist, backup, parameter, and threshold alert settings. The clone instance must have the same database type as the primary instance. However, other settings can differ, such as series, availability zone, network type, instance specification, and storage space. When creating a clone instance to restore data, select an instance specification and storage space larger than those of the primary instance to prevent long recovery times caused by performance limitations. The clone instance must have the same account type as the primary instance, but you can change the account passwords for the clone instance.

**Procedure**

1.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **Backup and Recovery**.
4. In the backup list, find the target backup set, click **Restore** in the **Actions** column, and
then click **OK** in the confirmation dialog box.
5. On the **RDS Restore** page, set the following parameters.

| Category | Parameter | Description |
|---|---|---|
| Region and zone | Region | Regions are isolated, and their internal networks are not interconnected. The region cannot be changed after the instance is created. |
|   | Deploymen t mode | Select Multi-AZ deployment or Single-AZ deployment. For Multi-AZ deployments, you can specify the availability zones for the primary and secondary nodes. |
|   | Primary availability zone | The availability zone where the primary node of the instance is located. |
|   | Secondary availability zone | The availability zone where the secondary node of the instance is located. This parameter is available only if you select Multi-AZ deployment. |
| Database recovery | Restore method | The method for restoring the primary instance's data. Valid values: By point in time By backup set |
|   | Restore time | Select the point in time to restore to. This parameter is required if Restore method is set to By point in time. |
| Document Vers | ion: 20260831 15 |   |

| e·Database ba on |   |   |
|---|---|---|
|   | Backup set | Select the backup set to restore from. This parameter is required if Restore method is set to By backup set. |
| Instance configurat ion | Instance name | The name of the clone instance. |
|   | Database type | The type of the database. This parameter cannot be modified. |
|   | Database version | The version of the database. This parameter cannot be modified. |
|   | Series | The series of the database. See the console for available options. |
|   | Storage type | The storage type of the database. See the console for available options. |
|   | Instance specificatio n | The specification of the clone instance. To avoid long recovery times, select an instance specification and storage space larger than those of the primary instance. |
|   | Storage space | Storage space includes space for data, system files, binlog files, and transaction files. See the console for the available storage space. For certain instance specifications with dedicated resources, such as those with dedicated local SSDs, the storage space is determined by the instance specification. |
| Network settings | Network type | RDS instances support the following network types: classic network: Access control relies on security groups and whitelists. Virtual Private Cloud: A Virtual Private Cloud (VPC) allows you to build an isolated network environment on Alibaba Cloud. VPCs support custom route tables, IP address ranges, and gateways. We recommend that you use a VPC for enhanced security. |
|   | VPC | Select the target VPC. Required when Network type is set to Virtual Private Cloud. |
|   | vSwitch | Select a vSwitch in the VPC. Required when Network type is set to Virtual Private Cloud. |

ation
6. Configure the parameters and click **Submit**.

## CloudDBA

### Introduction to DAS

Database Autonomy Service (DAS) is a cloud service that uses machine learning and expert experience to automate perception, healing, optimization, O&M, and security for databases. DAS simplifies database management and prevents service failures that are caused by manual operations. This way, DAS helps ensure that the database service of users runs in a stable, secure, and efficient manner.

**Features**

ApsaraDB RDS for MySQL leverages the core capabilities of DAS to deeply integrate intelligent diagnostics and autonomy services into the ApsaraDB RDS console. It offers the following features to provide a one-stop database management experience: Perform quick diagnostics Allows you to view resource usage, basic instance information, and a comprehensive performance overview. You can also initiate diagnostics to quickly identify database anomalies. Session Management Supports real-time monitoring, analysis, and intervention of active sessions on database instances. It allows you to view abnormal sessions (such as long-running uncommitted transactions), export or terminate sessions, and integrate with autonomous capabilities like 10-second SQL analysis, SQL throttling, and SQL optimization. These features help you quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation. Real-time monitoring Allows you to view visualized charts and tables generated from key operational metrics collected at high frequencies. This feature is designed to help database administrators (DBAs) and developers gain insights into the real-time loads of database instances, quickly locate the root cause of performance jitters, and assess the resource usage of database instances. Lock analysis When database issues such as deadlocks, transaction blocking, or metadata lock (MDL) waits occur, you can use the lock analysis feature to visually diagnose lock-wait relationships. This helps quickly identify the root cause of blocking and the dependency chain, which significantly improves troubleshooting efficiency and ensures the stability and high availability of database services. Storage Analysis Allows you to view the storage usage and the number of remaining days for which storage is available on a database instance. This feature also allows you to view the storage usage of a specified table, tablespace fragments, and diagnostic results on the database. Dashboard Allows you to view performance metrics, such as TPS, QPS, and throughput, of an instance. You can view performance metrics in different ways. For example, you can view the performance metrics within a specific time period, compare performance metrics collected during different time periods, or customize the performance metrics you want to view. View slow query logs Allows you to view slow query log trends, statistical information, and execution details. It also provides optimization recommendations and allows you to export historical data, helping you quickly locate and resolve performance bottlenecks. Diagnostic reports Allows you to generate instance health assessment reports manually or on a schedule. By analyzing health scores, slow SQL queries, and resource bottlenecks, this feature identifies potential risks and assists with manual troubleshooting and performance optimization. Currently, this feature can only assess the status of database instances and display the identified issues. It does not provide any optimization suggestions. You need to troubleshoot the issues based on the generated report.

### Diagnostics and analysis

#### Perform quick diagnostics

After you log in to the ApsaraDB RDS console and go to the Diagnostics page of Database Autonomy Service (DAS), you can view resource usage, basic instance information, and a comprehensive performance overview. You can also initiate diagnostics to quickly identify database anomalies.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**.
4. On the **Diagnostics** tab, you can view the following information.
Current resource usage: You can view the CPU, memory, IOPS, storage, and connection usage of the current instance. Database basic information: You can view the database engine, source, and specifications of the current instance. Database performance: You can view the risks, alerts, slow SQL queries, and deadlocks related to the current instance within the specified time period. This helps you quickly identify anomalies.

**Note**

You can click **Create Reports** in the upper-right corner of the database view to diagnose the database. After the diagnostic is complete, you can click **View History** to view the historical diagnostics.

#### Session Management

After you log in to the ApsaraDB RDS console and navigate to the Session Management page of Database Autonomy Service (DAS), you can perform real-time monitoring, analysis, and intervention of active sessions on database instances. It allows you to view abnormal sessions (such as long-running uncommitted transactions), export or terminate sessions, and integrate with autonomous capabilities like 10-second SQL analysis, SQL throttling, and SQL optimization. These features help you quickly locate performance bottlenecks, blocking sources, and high-risk operations to ensure stable and efficient database operation.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**. On the
**Session Management** tab, perform the following operations:

**Instance sessions**

**View abnormal sessions**

Click **Anomaly Detection**. In the pop-up dialog box, you can view abnormal sessions that the system identifies, including sessions that have not submitted transactions for a long period of time and sessions that occupy excessive resources. You can click **Optimize** or **End** to handle these sessions.

**View key metrics**

Move the pointer over **Active session**, **Maximum Execution Duration**, **CPU**
**Utilization**, or **Connection Usage** to view the detailed information and trend in the pop-
up window.

**Other core features**

**10s SQL analysis**: Click **10s SQL Analysis** in the upper-right corner to view SQL
execution statistics, slow SQL queries, and SQL overview information within the previous 10 seconds, helping you identify transient performance issues.
**SQL throttling**: Click **SQL Throttling** to go to the **SQL Throttling** page. On this
page, you can configure throttling rules to automatically throttle abnormal or high-load SQL queries to prevent system exhaustion. For more information, see the **SQL**
**throttling** section.
**Optimization**: Click **Optimize** to optimize the sessions of the desired instance. For
more information, see the **SQL optimization** section.
**Export active sessions**.
**End sessions**: To terminate a session, you must enter the database account and
password for authentication. You can also use a database account with the permissions to terminate the sessions created by using other database accounts, such as a privileged account.

**Note**

In the **User** column of a session, you can view the database account that is used to create the session. Click **End Session History** to query the operation records of all terminated sessions, including the task ID, start time, and end time. This facilitates tracing and auditing.

**Session statistics**

**View session statistics**

You can view summarized session information by user, access source, or database, including the total number of sessions, the total number of ongoing sessions, and the longest session duration.

**Export session statistics**

You can export session statistics by summary, user, access source, or database.

#### Real-time monitoring

After you log in to the ApsaraDB RDS console and navigate to the instance performance page of Database Autonomy Service (DAS), you can view visualized charts and tables generated from key operational metrics collected at high frequencies. This feature is designed to help database administrators (DBAs) and developers gain insights into the real-time loads of database instances, quickly locate the root cause of performance jitters, and assess the resource usage of database instances.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**. Click the
**Real-time Monitoring** tab. The system automatically loads real-time data. You can switch
between the **Real-time Charts** and **Real-time Tables** views. For more information, see
**View switching and advanced operations** in this topic.

**Core metric interpretation**

Based on the console interface (this topic uses MySQL as an example; metrics for databases such as PostgreSQL may differ, so refer to the actual display in the console), real-time performance covers the following four monitoring dimensions. The following table below provides a detailed explanation of each metric along with O&M recommendations:

**BInstance basic instance information overview**

| Modu le | Metric | Description and O&M recommendations |
|---|---|---|
| Serve r Iinfor matio n | Version/Uptime | Displays the database kernel version (such as 8.0.36 ) and the cumulative uptime of the instance. Use this information to verify environment consistency and instance stability. |
| Conn ection Iinfor matio n | Maximum Cconnections/Cu rrent Cconnections/Act ive Cconnections | Format example: 1200 / - / 3 . Maximum Cconnections: Tthe maximum number of connections that the instance allows. Current Cconnections: Tthe total number of established TCP connections. Active Cconnections: Tthe number of connections that are currently executing SQL statements. Note If the number of current connections approaches the upper limit, watch for connection storms. If the number of active connections is much lower than the number of current connections, a large number of idle connections may be consuming resources. |

| Buffer Pool | Total Ppages/IdleFree pPage Percentageratio/ Dirty Ppage Percentageratio | Displays the InnoDB buffer pool status. Idle PFree page Percentageratio: Iindicates the remaining memory space. Dirty Ppage Percentageratio: Iindicates the volume of data pending flush to disk. A high percentageratio may reduce flush efficiency and cause I/O jitter. |
|---|---|---|

**Throughput, load, and deep engine metrics**

| Categ ory | Metric name | Description | O&M analysis and recommendations |
|---|---|---|---|
| Throu ghput | QPS \| TPS | QPS: The average number of SQL statements executed per second. TPS: The average number of transactions per second. | Trend analysis: A sudden increase typically corresponds to a business peak. Exception troubleshooting: If QPS or TPS drops while CPU usage rises, lock waits or slow SQL query blocking usually exists. |
| DML distrib ution | DML Eexecutio ns count | select: The number of SELECT statements executed per second. insert: The number of INSERT statements executed per second. update: The number of UPDATE statements executed per second. delete: The number of DELETE statements executed per second. | Business profiling: Identify whether the workload is read-heavy or write-heavy to help formulate an index optimization policy, such as adjusting the read/write splitting architecture. |
| Conne ction sessio ns | Connectio ns | Active Sessionsconnections: The number of open connections that are in an active statuse. Total Cconnections: The total number of open connections. | Bottleneck identification: Monitor the peaks of active connections. If the number of active sessionconnections remains high for an extended period, check for long-running transactions or unreleased application connections. |
| Cache efficie ncy | InnoDB CacheBuff er Pool | Cache Hhit Rratio: The ratioproportion of data read from memory. Cache Uusage: The occupancy ratio of the buffer pool. | Performance key: The hit ratio should be close to 100%. A low hit ratio means that a large number of requests fall through to the disk (physical reads), which causes a sharp performance drop. Consider increasing the buffer pool size or optimizing SQL queries. |

| Data access | InnoDB Raccessed rows | rows read: The number of _ InnoDB rows read per second. rows inserted: The number of _ InnoDB rows inserted per second. rows updated: The number of _ InnoDB rows updated per second. rows deleted: The number of _ InnoDB rows deleted per second. | Index optimization: If rows read is _ extremely high but the returned result set is small, a full table scan exists and you must add an appropriate index. |
|---|---|---|---|
| I/O reads and writes | Logical Rreads/ and pPhysical Rreads | Logical Rreads: The number of logical reads per second (read from the buffer pool). Physical Rreads: The number of physical reads per second (read from the disk). | I/O bottleneck: A surge in physical reads severely degrades performance and typically results from cold data access, an insufficient buffer pool, or missing indexes. |
| Lock conte ntion | Average Lrow lock Thold time for InnoDB Row-level Locking | The unit is typically milliseconds (ms), which reflects the average time to acquire a lock. | Concurrency conflicts: A higher value indicates more intense contention between transactions, which may cause timeout errors on the application side. |
| Lock waits | WInnoDB row lock waits for InnoDB Row-level Locking | Average Waits for InnoDB Rrow-level Llocking waits: The average number of row lock waits within the statistics period. Current Waits for InnoDB Rrow-level Llocking waits: The number of row lock waits at the current moment. | Blocking source: If this curve is not zero, blocking exists. Use the session management feature to locate the blocker and terminate the abnormal session. |
| Temp orary resour ces | Temporary Ttables and Ffiles | Temporary Ttables: The number of temporary tables created. Temporary Ffiles: The number of temporary files created. | SQL optimization: Frequent creation of on-disk temporary files severely degradesslows down SQL performancequeries. This typically occurs because sort buffer size is _ _ insufficient or a lack ofmissing indexes prevents index-based sorting. |
| Excep tion monit oring | Slow Qqueries | Slow Qqueries: The difference in the number of slow queries between two adjacent collection points, which represents the slow query increment within that time period. | Root cause correlation: A sudden increase in slow queries often directly causes CPU spikes and slow responses. Capture the slow query log immediately for analysis. |

| Netwo rk bandw idth | Network Ttraffic | Total Ttraffic, Iinbound Ttraffic, and Ooutbound Ttraffic. | Bandwidth limits: If outbound traffic reaches the instance bandwidth limit, connection timeouts or packet loss occur. If inbound traffic is abnormal, check for large field writes or potential attacks. |
|---|---|---|---|

**View switching and advanced operations**

**Comparison between real-time charts and real-time tables**

**Real-time charts**: Suitable for observing trends, peaks and valleys, and correlations
between multiple metrics (for example, whether CPU usage rises synchronously when QPS increases).
**Real-time tables**: Suitable for viewing exact metric values at a specific point in time,
which facilitates baseline data recording and detailed data comparison. Each row in the table represents a sampling point in time, and each column corresponds to the specific value of a metric.
**Data download**: On the **Real-time Tables** tab, click the **Download** button in the
upper-right corner of the page to export the current report data to your local device.

**Note**

Some database engines (MongoDB and Redis) do not support the report download feature. The actual availability depends on what the console displays.

**Parameter description**

Click **Metric Description** in the upper-left corner of the page to view the specific definition of each metricmonitoring item, allowing you towhich helps you interpret data more accurately.

**Pause and resume**

The upper-right corner displays the remaining refresh count. You can manually control the automatic refresh frequency of the page, or click **Pause** to freeze the statuse at a specific moment for detailed analysis during troubleshooting.

**Usage recommendations**

Establish a baseline: During stable business periods, observe and record normal QPS, TPS, and CPU usage as a benchmark for subsequent fault comparison. Perform correlation analysis: Avoid viewing a single metric in isolation. For example, when QPS drops, immediately check whether InnoDB row lock waits increase or slow queries increase, and observe forwhether physical reads show abnormal fluctuations in physical reads. Watch for spikes: Sudden spikes in charts typically correspond to specific business events (such as scheduled jobs starts or flash sales). Cross-referencing the timestampCorrelating the point in time with business logs helps you quickly locate the issue.

#### Lock analysis

When database issues such as deadlocks, transaction blocking, or metadata lock waits occur, you can use the lock analysis feature provided by Database Autonomy Service (DAS) to visually diagnose lock-wait relationships. This helps quickly identify the root cause of blocking and the dependency chain, which significantly improves troubleshooting efficiency and ensures the stability and high availability of database services.

**Introduction**

The lock analysis feature allows you to perform multi-dimensional analysis on deadlocks, transaction blocking, and metadata lock waits on a database instance.
**Recent deadlock analysis**: DAS analyzes the most recent deadlock log in the output of
the `SHOW ENGINE INNODB STATUS` statement. If multiple deadlocks have occurred, DAS analyzes only the most recent deadlock.
**Other lock analysis**: DAS analyzes the metadata lock and transaction blocking in the
current sessions of your database instance in real time based on the data in

```
 information_schema  and  performance_schema .
```

Metadata lock analysis: DAS deduces the lock wait relationships and generates the corresponding diagram based on the data in tables such as the `information_schema.processlist` table. Transaction blocking analysis: DAS analyzes the transaction blocking relationship and generates the corresponding diagram based on the data in the

| information schema.processlist _ | , | information schema.innodb trx _ _ |   |   | , and |
|---|---|---|---|---|---|
|   |   |   | or |   |   |

tables. Data in the information_schema.innodb_lock_waits table is used for database instances that run MySQL 5.6 or MySQL 5.7, and data in the performance_schema.data_lock_waits table is used for database instances that run MySQL 8.0.

**Procedure**

1. 2.
3. In the left-side navigation pane, click **Autonomy Service > Diagnostics**. On the **Lock**
**Analysis** tab:

**Deadlock analysis**

i. **Analyze the most recent deadlock** On the **Recent Deadlock Analysis** tab, click **Create Analysis Task**.

**Note**

If multiple deadlocks have occurred, DAS analyzes only the most recent deadlock and retains the deadlock data. ii. **View details** a. After the diagnostic task is complete, select a time range and click **View Details** in the
**Details** column of the diagnostic task list under recent deadlock analysis to view the
results of deadlock diagnostic tasks that were triggered during the time range. b. In the panel that appears, you can view the deadlock details.

**Other lock analysis**

i. **Initiate other lock analysis and diagnostics** On the **Recent Deadlock Analysis** tab, click **Create Analysis Task**. ii. **View details** a. Click the icon before an analysis result to expand the metadata lock wait and transaction blocking analysis information. b. Click **View Details**. The details of the transaction lock are displayed.

#### Storage Analysis

After you log in to the ApsaraDB RDS console and navigate to the Storage Analysis page of Database Autonomy Service (DAS), you can view the storage usage and the number of remaining days for which storage is available on a database instance. This feature also allows you to view the storage usage of a specified table, tablespace fragments, and diagnostic results on the database.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostics**. On the
**Storage Analysis** tab, you can perform the following operations:
On the **Storage Analysis** tab, click the **Storage Overview** tab. You can view data such as the storage overview, exception list, storage trend, and tablespaces. On the **Storage Analysis** tab, click the **Data Space** tab. You can view the storage usage of each database and tablespace. Click the name of a tablespace to view the fields and indexes of the tablespace.

### Dashboard

After you log in to the ApsaraDB RDS console and navigate to the Dashboard page of Database Autonomy Service (DAS), you can view performance metrics, such as TPS, QPS, and throughput, of the instance. You can view performance metrics in different ways. For example, you can view the performance metrics within a specific time period, compare performance metrics collected during different time periods, or customize the performance metrics you want to view.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Dashboard**.
On the **Performance Trends** tab, you can view the trends of changes in the TPS, QPS, and sessions. You can also click **More Metrics** to customize the metrics you want to view.

**Note**

Click the icon next to the name of a metric to view its description. On the **Performance Trend Comparison** tab, select two time periods to compare the performance metrics collected within the specified time periods. On the **Custom Charts** tab, you can centrally display and manage the desired performance metrics in one chart by customizing performance charts. This simplifies troubleshooting.

**Note**

You must create a dashboard if this is the first time you use **custom charts**.

### View slow query logs

After you log in to the ApsaraDB RDS console and navigate to the Slow Query Logs page of Database Autonomy Service (DAS), you can view slow query log trends, statistical information, and execution details. It also provides optimization recommendations and allows you to export historical data, helping you quickly locate and resolve performance bottlenecks.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Slow Query Logs**.
In the **Slow Log Trend** section, view the slow query log trend of the instance. Click the **Slow Log Statistics** tab to view slow log details for a specified time range and optimize the slow SQL statements. The instances of some database types do not support the SQL optimization feature. Refer to the actual features available in the console. For the instances of ApsaraDB RDS for MySQL and PolarDB for MySQL Primary/Secondary Edition, click the **Optimize** button in the Actions column of the slow SQL record that you want to mange. The record is highlighted in blue to help you quickly locate the SQL statement being analyzed in a large number of slow SQL statements. This highlight persists after you close the optimization window and automatically shifts to the new record when you optimize another slow SQL statement. Click the **Slow Log Details** tab to view the execution details of slow query logs.

### Diagnostic reports

After you log in to the ApsaraDB RDS console and navigate to the Diagnostic Reports page of Database Autonomy Service (DAS), you can generate operational status assessment reports of the instance manually or at a scheduled time. By analyzing health scores, slow SQL queries, and resource bottlenecks, this feature identifies potential risks and assists with manual troubleshooting and performance optimization. Currently, this feature can only assess the status of database instances and display the identified issues. It does not provide any optimization suggestions. You need to troubleshoot the issues based on the generated reports.

**Suggestions**

Periodically generate diagnostic reports: We recommend that you configure the system to automatically generate daily diagnostic reports for production instances and formulate performance baselines. Use slow SQL query optimization: Pay close attention to the top 10 slow SQL queries and high-risk SQL queries, and optimize them promptly. Focus on changes in health scores: If the health score consistently drops, check resource configurations or look for performance bottlenecks caused by business growth.

**Procedure**

1. 2.
3. In the left-side navigation pane, choose **Autonomy Services > Diagnostic Reports**. On
this page, you can perform the following operations:

**Manually initiate a diagnostic**

Click **Create Reports**. In the dialog box that appears, select a time range (Last 1 Hour, Last 3 Hours, Last 6 Hours, Last 12 Hours, or Last 24 Hours) and click **Confirmation**. The system immediately starts the diagnostic task.

**Automatically generate diagnostic reports at a scheduled**

**time**

Click **Auto-generating Report Settings**, select **Scheduled Trigger**, select days and a specific time, and then click **OK**.

**Note**

Due to system scheduling and resource usage, diagnostic reports may be generated with a delay. The actual time prevails.

**View diagnostic report details**

The list on the page shows all available diagnostic reports. Click **View Report** in the Actions column of a diagnostic report to go to the details page. The report displays the following information: instance health status, active sessions, top 10 slow SQL queries, high-risk SQL queries, top 5 tablespaces, redundant indexes, lock analysis, and performance trends. In the upper-right corner of the diagnostic report page, click **Deduction Details** to view the health score deduction details.

**Download a diagnostic report**

Click **View Report** to go to the diagnostic report details page. Then, click **Download** to download the report to your on-premises machine for archiving or sharing.

## Log management

ApsaraDB RDS lets you query error logs, slow query log details, slow query log summaries, and primary/secondary switchover logs in the console for troubleshooting and performance analysis.

**Procedure**

1. Log on to the ApsaraDB RDS console.
2. On the **Instance List** page, find the instance that you want to manage.
3. In the left-side navigation pane, click **log management**.
4. On the **log management** page, select the tab for the desired log type, set a custom time
range, and then click **OK**. The following table describes the supported log types.

| Log type | Description |
|---|---|
| Error log | Records database errors from the last 15 days. |
| Slow query log details | Records SQL statements from the last 15 days that took longer than 1 second to execute. Similar statements are deduplicated. You can view and export the log data for any 7-day period within this time frame. |
| Slow query log summary | Aggregates statistics for SQL statements from the last 15 days that took longer than 1 second to execute. You can view these statistics for any 7-day period within this time frame. |
| Primary/second ary switchover log | Records switchovers between primary and secondary instances. This feature is available only for MySQL High-availability Edition instances. |

MySQL data

## Use mysqldump to

**migrate MySQL data**

This topic describes how to use mysqldump to migrate data from an on-premises database to an ApsaraDB RDS for MySQL instance.

**Prerequisites**

An ECS instance is created.

**Background information**

mysqldump is easy to use but requires extensive downtime. This tool is suitable for scenarios where the amount of data is small or extensive downtime is allowed. ApsaraDB RDS for MySQL is fully compatible with the native database service. The procedure of migrating data from the original database to an ApsaraDB RDS for MySQL instance is similar to that of migrating data from one MySQL server to another. Before you migrate data, you must create an account that is used to migrate data from the on-premises MySQL database. You must grant the read and write permissions on the onpremises MySQL databases to the account.

**Procedure**

1. Run the following command to create a migration account for the on-premises database:

```
 CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

Parameter description: username: the name of the account to be created. host: the host from which the account is authorized to log on to the on-premises MySQL database. If you want to allow access from a local host, set this parameter to **localhost**. If you want to allow access from all hosts, set this parameter to a percent sign (**%**). password: the password of the account. For example, you can run the following command to create an account with the username
**William** and the password **Changme123**. The account is authorized to log on to the on-
premises MySQL database from all hosts.

```
 CREATE USER 'William'@'%' IDENTIFIED BY 'Changme123';
```

2. Run the following command to grant permissions to the migration account in the on-
premises database:

```
 GRANT SELECT ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; GRANT
REPLICATION SLAVE ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION; GRANT REPLICATION SLAVE ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;
```

Parameter description: privileges: the operation permissions granted to the account, such as SELECT, INSERT, and UPDATE. To authorize the account to perform all operations, set this parameter to
**ALL**.
databasename: the name of the on-premises MySQL database. If you want to grant all database permissions to the account, set this parameter to an asterisk (*). tablename: the name of the table whose data you want to migrate. If you want to grant all table permissions to the account, set this parameter to an asterisk (*). username: the name of the account. host: the host from which the account is authorized to log on to the on-premises MySQL MySQL data database. If you want to allow access from a local host, set this parameter to **localhost**. If you want to allow access from all hosts, set this parameter to a percent sign (**%**). WITH GRANT OPTION: authorizes the account to use the GRANT statement. This parameter is optional. For example, you can execute the following statement to grant all permissions on tables and databases to the **William** account. The account is authorized to log on to the database from all hosts.

```
 GRANT ALL ON *. * TO 'William'@'%';
```

3. Use the data export tool of mysqldump to export data from the database as a data file.

**Important**

Do not update data during data export. In this step, only data is exported. Stored procedures, triggers, and functions are not exported.

```
 mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob
dbName --skip-triggers > /tmp/dbName.sql
```

Parameter description: localIp: the IP address of the host where the on-premises MySQL database resides. userName: the account that is used to migrate data from the on-premises MySQL database. dbName: the name of the on-premises MySQL database. /tmp/dbName.sql: the name of the exported data file.
4. Use mysqldump to export stored procedures, triggers, and functions.

**Important**

Skip this step if no stored procedures, triggers, or functions are used in the database. When stored procedures, triggers, and functions are exported, you must remove the DEFINER to ensure compatibility with ApsaraDB RDS for MySQL.

```
 mysqldump -h localIp -u userName -p --opt --default-character-set=utf8 --hex-blob
dbName -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/triggerProcedure.sql
```

Parameter description: localIp: the IP address of the host where the on-premises MySQL database resides. userName: the account that is used to migrate data from the on-premises MySQL database. dbName: the name of the on-premises MySQL database. /tmp/triggerProcedure.sql: the name of the exported stored procedure file.
5. Upload the data file and stored procedure file to the ECS instance.
In this example, the files are uploaded to the following paths:

```
 /tmp/dbName.sql
 /tmp/triggerProcedure.sql
```

6. Log on to the ECS console and import both the data file and the stored procedure file to the
destination ApsaraDB RDS for MySQL instance.

**Note**

For information about how to log on to the ECS instance, see topics in the
**Connect to an instance** section of ECS User Guide.

| mysql -h intranet4example.mysql.rds.aliyuncs.com –u userName -p dbName < |   |
|---|---|

MySQL data

```
 mysql -h intranet4example.mysql.rds.aliyuncs.com -u userName -p dbName <
/tmp/triggerProcedure.sql
```

Parameter description: intranet4example.mysql.rds.aliyuncs.com: the endpoint of the ApsaraDB RDS for MySQL instance. An internal endpoint is used in this example. userName: the migration account of the ApsaraDB RDS for MySQL database. dbName: the name of the on-premises MySQL database from which you want to import data. /tmp/dbName.sql: the name of the data file that you want to import. /tmp/triggerProcedure.sql: the name of the stored procedure file that you want to import.
