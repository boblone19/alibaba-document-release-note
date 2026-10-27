---
title: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Operations and Maintenance Guide 20250110"
product_version: "V3.18.3"
doc_version: "20250110"
pdf_pages: 9
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Operations and Maintenance Guide 20250110.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/Redis/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20ApsaraDB%20for%20Redis%20Operations%20and%20Maintenance%20Guide%2020250110.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Operations and Maintenance Guide 20250110

## Table of Contents

- 1 Operations Guide
  - 1.1 O&M tools
  - 1.2 System architecture
  - 1.3 Server roles
  - 1.4 Log on to the Apsara Uni-manager Operations Console
  - 1.5 Instance management
  - 1.6 Host management
  - 1.7 Security maintenance
    - 1.7.1 Network security maintenance
    - 1.7.2 Password maintenance

## 1 Operations Guide

### 1.1 O&M tools

The Apsara Uni-manager Operations Console is a unified and intelligent O&M platform. The platform provides the following features to manage ApsaraDB for Redis instances: Instance management: allows you to view instance details, instance logs, and user information. Host management: allows you to view and manage hosts.

### 1.2 System architecture

This topic describes the system components and their purposes.

| Group | Component | Description |
|---|---|---|
| Redis resource services | ServiceTest | Automated regression of KVStore for Redis features. |
|   | AbsCacheServiceAliyu nCom and RedisaPhoenix | The OpenAPI service for KVStore for Redis. |
|   | Location | Initialization of the Location configurations. |
|   | DbInit | DDL and DML configurations used to initialize Redis resource services. |
| Redis services | InitCluster | Initialization of the cluster and host list. |
|   | DbRedis | DB host node initialization, kernel installation, and RPM package management. |
| Redis-Control services | PengineMySQL | The task flow service related to KVStore for Redis. |
|   | RdsApiRedis | API operations related to KVStore for Redis. |
|   | DbInit | DML configurations used to initialize KVStore for Redis. |
|   | DbBootstrap | Deployment of DB host nodes for database services. |
|   | Robot | Automated O&M for database services. |
|   | MessageCenter | The message center service. |
|   | AuroraCluster | The high-availability platform for database services. |
|   | API | The backend core API service. |
|   | Stat-JobWorker | The real executor for scheduled task for various monitoring and inspections. |

| Core services |   |   |
|---|---|---|
|   | Dukang | The O&M platform for database services. |
|   | Brain | Performance collection of earlier-version instances and hosts, and audit log collection of instances. |
|   | BakMaster and Bifrost | To improve the full backup and incremental backup of databases. |
|   | TaskDispatcher | To manage the task flow scheduling service. |
|   | SecGroup | The whitelist service. |
|   | BackendLocation | The cluster and location management services. |
|   | NameService | The name service. |
|   | DBInit | Initialization of metadatabases. |
|   | EnvInit | Initialization of information such as OSS, VPC, and Bakowner. |

### 1.3 Server roles

This topic describes server roles and their respective projects, clusters, and services. This helps O&M personnel identify and locate faults.

> **Note:** You can view server roles by using Cluster Operations in Apsara Infrastructure Management. For more information about Apsara Infrastructure Management, see **Apsara Stack Operations and Maintenance Guide** .

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|
| rds | redis-control | rds-redis- control | Dbinit | The DDL and DML configurations used to initialize KVStore for Redis. |
|   |   |   | McNode | The messaging agent node. |
|   |   |   | PengineRedis | The task flow service related to KVStore for Redis. |
|   |   |   | RdsapiRedis | The API operations related to KVStore for Redis. |
|   | redis 7u _ | rds-redis | DbRedis | The DB host node initialization, kernel installation, and RPM package management. |
|   |   |   | initCluster | The initialization of the cluster and host list. |

### 1.4 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The URL, username, and password that are required to log on to the Apsara Uni-manager Operations Console are obtained from the deployment personnel or administrators. The URL of the Apsara Uni-manager Operations Console is in the format of regionid.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome.

**Procedure**

**Procedure**

1. Open your browser.
2. In the address bar, enter the URL. Then, press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter your username and password.

> **Note:** To obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console, contact the deployment personnel or administrators.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username as prompted. To enhance security, make sure that the password meets the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
4. Click **Log On**.

### 1.5 Instance management

This topic describes how to manage KVStore for Redis instances. You can view instance details and user information.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **O&M**.
3. In the left-side navigation pane, choose **Product Management > RDS**.
4. On the **Instance Management** tab of the RDS page, you can perform the following
operations:

| Operation | Description |
|---|---|
| View the details of an instance | A list of instances that belong to your account is displayed on the Instance Management tab. Click the ID of an instance to view the details of the instance. Note On the Instance Details page, you can click Primary/Secondary Switch and Query History. |
| View the user information of an instance | Find an instance and click User Information in the Actions column. On the User Information page, you can view the user information and key metrics of each instance. |

### 1.6 Host management

This topic describes how to view resource usage and key performance metrics for KVStore for Redis hosts.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **O&M**.
3. In the left-side navigation pane, choose **Product Management > RDS**.
4. On the **Host Management** tab of the RDS page, you can view information of all hosts.
5. Click a hostname to go to the **RDS Instance** page. You can view all instances on this host.

### 1.7 Security maintenance

#### 1.7.1 Network security maintenance

Network security maintenance involves device security and network security.

**Device security**

Check network devices, and enable security management protocols and configurations for these devices. Check software versions of network devices and update them to more secure versions in time. For more information about security maintenance methods, see documents of related devices.

**Network security**

Based on your network conditions, select the intrusion detection system (IDS) or intrusion prevention system (IPS) to detect abnormal Internet and intranet traffic and protect against abnormal behavior and attacks in real time.

#### 1.7.2 Password maintenance

Passwords include system passwords and device passwords in KVStore for Redis. To secure your account, you must periodically change the system and device passwords, and use complex passwords.
