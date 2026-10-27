---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Backup and Recovery User Guide 20250618"
product_version: "V3.18.3"
doc_version: "20250618"
pdf_pages: 161
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Backup and Recovery User Guide 20250618.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E7%81%BE%E5%A4%87%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Backup%C2%A0and%C2%A0Recovery%20User%20Guide%2020250618.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Backup and Recovery User Guide 20250618

## Table of Contents

- 1 What is Apsara Stack Resilience for Backup and Recovery?
- 2 Roles and permissions
- 3 Procedure overview
- 4 Log on to the ASR for Backup and Recovery console
- 5 Query overview statistics
- 6 User guide
- 7 Create a storage pool
- 8 Instance management
  - 8.1 View the instance list
  - 8.2 Change the backup policy of an instance
  - 8.3 View backup durations
- 9 Backup vault
  - 9.1 Create a backup vault
  - 9.2 View data in a backup vault
  - 9.3 Manage backup vaults
  - 9.4 Create a mirror vault
- 10 Backup plans
  - 10.1 Create a backup plan
  - 10.2 View a backup plan
  - 10.3 Start a backup plan
  - 10.4 Perform an immediate backup
  - 10.5 Stop a backup plan
  - 10.6 Modify the configurations of a backup plan
  - 10.7 Modify the backup policy of a backup plan
  - 10.8 View log backup files
  - 10.9 View a backup event
  - 10.10 View the statistics about a backup plan
- 11 Backup records
  - 11.1 Backup flow overview
  - 11.2 View backup records
- 12 Recovery jobs
  - 12.1 Create a routine recovery job
  - 12.2 Start a recovery job
  - 12.3 Stop a recovery job
  - 12.4 View recovery jobs
  - 12.5 View the log of a recovery event
- 13 Backup and recovery of VMware VMs
  - 13.1 Install a backup gateway
  - 13.2 Register a backup gateway
  - 13.3 Create a vCenter
  - 13.4 Create a backup plan for a VM
  - 13.5 Restore a VMware VM
- 14 System management
  - 14.1 Manage storage pool groups
  - 14.2 Manage self-backup
    - 14.2.1 Create a backup policy for metadata
    - 14.2.2 View the backup records of metadata
  - 14.3 Create a disaster recovery job
  - 14.4 Manage authorizations
    - 14.4.1 View license resources
    - 14.4.2 Configure resource quotas for an organization
- 15 O&M Management
  - 15.1 Alert management
    - 15.1.1 View alert records
    - 15.1.2 Mark alerts as read
    - 15.1.3 Delete alert records
  - 15.2 Throttling configuration
  - 15.3 Engine monitoring
  - 15.4 View resource statistics
  - 15.5 View operation logs
  - 15.6 Configure parameters
  - 15.7 Event management
- 16 Best practices of data backup
  - 16.1 Database services
    - 16.1.1 ApsaraDB RDS backups
    - 16.1.2 PolarDB-X 1.0 backups
  - 16.2 File storage services
    - 16.2.1 OSS backups
    - 16.2.2 NAS backups
    - 16.2.3 ECS file backups
    - 16.2.4 ECS instance backups
  - 16.3 Analytics computing services
    - 16.3.1 MaxCompute backups
  - 16.4 Best practices for hybrid cloud backup
    - 16.4.1 Preparations
    - 16.4.2 Hybrid cloud network connections with Express Connect circuits
    - 16.4.3 Create a storage pool
    - 16.4.4 Create a backup vault
    - 16.4.5 Create a backup plan
- 17 FAQ
  - 17.1 How do I delete a storage pool?
  - 17.2 How do I view ECS snapshot sizes?
  - 17.3 What do I do if an error is returned when I log on to the ASR for Backup and Recovery console as a common user?
  - 17.4 What do I do if an AccessKey pair error or an AccessDenied error is returned when I create a storage pool?
  - 17.5 What do I do if the 500 error is displayed on pages of the ASR for Backup and Recovery console?
- 18 Appendix
  - 18.1 Install an HBR agent on an ECS instance
  - 18.2 Preparations for using the storage cascade feature of a backup vault
    - 18.2.1 Introduction to the storage cascade feature of a backup vault
    - 18.2.2 Initialization in the console
  - 18.3 Configure the ASR-BR service-linked role for an organization
  - 18.4 Network limits
  - 18.5 Statistics on the resource set-level resource usage in an organization
  - 18.6 Use the SMB protocol to back up and restore NAS files
    - 18.6.1 Use the SMB protocol to back up NAS files
    - 18.6.2 Use the SMB protocol to restore NAS files
  - 18.7 Cross-region backup

silience for Backup and Recovery ?

## 1 What is Apsara Stack Resilience for Backup and Recovery?

**Resilience for Backup and**

**Recovery?**

ASR for Backup and Recovery is a cloud service that is developed for data backup and recovery on Apsara Stack. ASR for Backup and Recovery supports the data backup and recovery of the following products: ApsaraDB RDS, Object Storage Service (OSS), Elastic Compute Service (files and instances), Apsara File Storage NAS, PolarDB-X V1.0, and MaxCompute.

**Features**

Overview On this page, you can view the real-time status of the system, backup and recovery statistics, resource statistics, backup engine monitoring, and system alerts. This page provides the links for visiting the homepage and product documentation of ASR for Backup and Recovery, usage process, short description of backing up data to Alibaba Cloud public cloud, recommended scenarios, and key concepts. Instances On this page, you can view the status of all instances of various cloud services under a specific organization. For example, you can check whether a backup plan is created for a specific instance. Backup Vaults On this page, you can create and manage backup vaults, including database backup vaults, storage backup vaults, and deduplication backup vaults. The storage media of backup vaults can only be OSS. On this page, you can create backup plans and manage all existing backup plans by organization. On this page, you can view the backup records of an instance. A backup record contains the backup set size, record status, storage location, start time, and expiration time. On this page, you can create and manage recovery jobs. Recovery jobs can be classified into the following types based on the usage scenarios: Routine Recovery, Disaster Recovery, Recovery on Cloud (VMware), and Local Recovery (VMware). On this page, you can manage storage pools, automated backups, disaster recovery, vCenter servers, and resource quotas. On this page, you can view resource statistics and engine metrics and manage throttling configurations, logs, parameter settings, alerts, and events.

## 2 Roles and permissions

ASR for Backup and Recovery supports default system roles and custom roles. This topic describes the logon methods and permissions of four default system roles: operations administrator, organization administrator, resource auditor, and organization resource auditor.

**Roles**

The following table describes the logon methods of different roles.

| Role | Logon method |
|---|---|
| Operations administrator | Log on to the Apsara Uni-manager Management Console as an operations administrator and select the root organization to log on to the ASR for Backup and Recovery console. |
| Organization administrator | Log on to the Apsara Uni-manager Management Console as an organization administrator and select the belonging organization to log on to the ASR for Backup and Recovery console. Log on to the Apsara Uni-manager Management Console as an operations administrator and select a non-root organization to log on to the ASR for Backup and Recovery console. |
| Resource auditor | Log on to the Apsara Uni-manager Management Console as a resource auditor and select an organization to log on to the ASR for Backup and Recovery console. |
| Organization resource auditor | Log on to the Apsara Uni-manager Management Console as an organization resource auditor and select the belonging organization to log on to the ASR for Backup and Recovery console. |

**Permissions**

The following table describes the permissions of different roles on the ASR for Backup and Recovery console.

> **Note:** The operations administrator and resource auditor can perform operations on all organizations.
> The organization administrator and organization resource auditor can perform operations only on the organization to which they belong and the subordinate organizations.

| Feature | Permissio n | Operations administrator | Organization administrator | Resource auditor | Organization resource auditor |
|---|---|---|---|---|---|

| Overvie w | View | Supported | Supported | Supported | Supported |
|---|---|---|---|---|---|
| Cloud instance s | View | Supported | Supported | Supported | Supported |
| Backup vaults | Create | Not supported | Supported | Not supported | Not supported |
|   | View | Supported | Supported | Supported | Supported |
|   | Delete | Not supported | Supported | Not supported | Not supported |
|   | Modify | Supported | Supported | Not supported | Not supported |
|   | Query details | Supported | Supported | Supported | Supported |
| Backup plans | Create | Not supported | Supported | Not supported | Not supported |
|   | Query/Vie w | Supported | Supported | Supported | Supported |
|   | Configure/ Backup now | Not supported | Supported | Not supported | Not supported |
|   | Delete | Not supported | Supported | Not supported | Not supported |
|   | Handle events | Not supported | Supported | Not supported | Not supported |
| Backup records | Query | Supported | Supported | Supported | Supported |
|   | View | Supported | Supported | Supported | Supported |
|   | Delete | Not supported | Supported | Not supported | Not supported |
| Recover y jobs | Create | Not supported | Supported | Not supported | Not supported |
| > Document | Version: 20250618 1 |   |   |   |   |

| SR for Back r Guide·Rol | up and Recovery Us Apsara Stack Resilienc es and permissions |   |   |   |   |
|---|---|---|---|---|---|
|   | Handle events | Not supported | Supported | Not supported | Not supported |
| Alerts | Handle | Supported | Supported | Not supported | Not supported |
| Storage pools | Create | Supported | Not supported | Not supported | Not supported |
|   | Modify | Supported |   |   |   |
|   | Delete | Supported |   |   |   |
| Self- backup records | Create/Mo dify/Cancel | Supported | Not supported | Not supported | Not supported |
|   | Delete | Supported | Not supported | Not supported | Not supported |
| Disaster recovery | Create/Han dle | Supported | Not supported | Not supported | Not supported |
| vCenters | Create | Not supported | Supported | Not supported | Not supported |
| Authoriz ation manage ment | Synchroniz e authorizati on | Supported | Not supported | Not supported | Not supported |
|   | Assign authorizati on | Supported | Supported |   |   |
| O&M manage ment | Configure throttling | Supported | Configure throttling for a gateway used for VMware backup and disaster recovery | Not supported | Not supported |
|   | View engine metrics | Supported | Supported | Supported | Supported |
|   | View resource statistics | Supported | Supported | Supported | Supported |

|   | Manage logs | Supported | Supported | Supported | Supported |
|---|---|---|---|---|---|
|   | Configure parameter s | Supported | Not supported | Not supported | Not supported |
|   | Manage events | Supported | Supported | Not supported | Not supported |

## 3 Procedure overview

This topic describes the procedure of backup and recovery. The following figure shows the backup and recovery procedure. ckup and Recovery console

## 4 Log on to the ASR for Backup and Recovery console

**Backup and Recovery console**

You can go to the ASR for Backup and Recovery console in the Apsara Uni-manager Management Console.

**Prerequisites**

You need to obtain the endpoint of the Apsara Uni-manager Management Console from the deployment personnel. A browser is available. We recommend using Google Chrome.

**Background information**

In cross-region backup and local backup scenarios, the ASR for Backup and Recovery console is deployed in the Central Region. You must log on to the ASR for Backup and Recovery console in the Apsara Uni-manager Management Console.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter. ckup and Recovery console

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.

2. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Account Logon**.
4.
5. In the top navigation bar, select **Products**.
6. In the left-side navigation pane, click **Disaster Recovery and Backup**.
7. In the **Disaster Recovery and Backup** section, choose **Disaster Recovery > ASR for**
**Backup and Recovery**.
s

## 5 Query overview statistics

This topic describes the statistics that are displayed on the Overview page of the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console. The statistics include the realtime status of the backup system, backup records, recovery records, resource statistics, backup status, and system alerts. This helps you quickly understand the overall backup situation.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Overview**.

| Section | Sub-section | Description |
|---|---|---|
|   | Amount of Protected Data | Displays the total amount of source data in the latest successful backup of the instances that have been backed up. For an operations administrator: This section displays the total amount of data in the latest successful backup of all instances that have been backed up. For an organization administrator: This section displays the total amount of data in the latest successful backup of the instances that have been backed up in the current organization. |

s

|   | Number of Instances That Can Be Backed Up | For an operations administrator: This section displays the total number of instances of cloud services for all organizations. For an organization administrator: This section displays the total number of instances of cloud services in the current organization. |
|---|---|---|
| System Overview |   |   |
|   | Backup Network Bandwidth | Displays the transmission rate of backup data configured in the current system. |
|   | Number of Cloud Services That Can Be Backed Up | For an operations administrator: This section displays the number of cloud services that can be backed up in the system. For an organization administrator: This section displays the number of cloud services that can be backed up in the current organization. |
|   | Number of Instances That Have Been Backed Up | For an operations administrator: This section displays the number of all instances that have been backed up. For an organization administrator: This section displays the number of instances that have been backed up in the current organization. |
|   | Bandwidth Utilization | Displays the utilization of the system bandwidth during backup. |
| Backup Statistics for Cloud Services | - | For an operations administrator: This section displays the number of instances that have been backed up and the number of instances that have not been backed up in the system. For an organization administrator: This section displays the number of instances that have been backed up and the number of instances that have not been backed up in the current organization. |
| Backup Status for Cloud Services | - | For an operations administrator: This section collects and displays statistics about the backup status of all cloud services in the system. For an organization administrator: This section collects and displays statistics about the backup status of all cloud services in the current organization. |

s

| Recovery Status for Cloud Services | - | For an operations administrator: This section collects and displays statistics about the recovery status of all cloud services in the system. The recovery status can be Recovered, Recovering, and Recovery Failed. For an organization administrator: This section collects and displays statistics about the recovery status of all cloud services in the current organization. The recovery status can be Successful, In Progress, and Failed. |
|---|---|---|
| Backup Storage Space Statistics | Total Number of Backup Vaults | For an operations administrator: This section displays the total number of backup vaults in the system. For an organization administrator: This section displays the total number of backup vaults in the current organization. |
|   | Used Storage Space/Total Storage Space | For an operations administrator: This section displays the total backup storage space and used storage space in the system. For an organization administrator: This section displays the total backup storage space and used storage space in the current organization. |
|   | Current Usage | Formula: Current usage = Used storage space/Total storage space × 100% For an operations administrator: This section displays the usage of the total backup storage space. For an organization administrator: This section displays the usage of the backup storage space in the current organization. |
|   | Top 5 Backup Vault Usage | For an operations administrator: This section displays the top five backup vaults that have the highest usage in the system. For an organization administrator: This section displays the top five backup vaults that have the highest storage space usage in the current organization. You can click the name of a backup vault to go to the Backup Vaults page to view the details of the vault. For more information, see Backup vault. |

s

| Real-time Backup Jobs | - | Collects and displays statistics about backup jobs in real time. You can click View More to view the details of all backup jobs. For an operations administrator: This section displays the backup status of all real-time backup jobs in the system. For an organization administrator: This section displays the backup status of real-time backup jobs in the current organization. |
|---|---|---|
| Time Consumed by Backup Job | - | Collects and displays statistics about the time consumed by backup jobs. A maximum of 10 backup jobs are displayed. You can click View More to view the time consumed by all backup jobs. For an operations administrator: This section displays the time consumed by all backup jobs in the system. For an organization administrator: This section displays the time consumed by backup jobs in the current organization. |
| Backup Jobs Started in Each Time Range | - | Collects and displays statistics about the number of backup jobs that are started within 24 hours and in the Running, Backup Succeeded, Partially Succeeded, and Failed states. For an operations administrator: This section displays the startup status of all backup jobs in the system. For an organization administrator: This section displays the startup status of backup jobs in the current organization. |
| Continuous Backup Jobs in Each Time Range | - | Collects and displays statistics about the number of backup jobs that are started within 24 hours in the Running state. For an operations administrator: This section displays the total number of backup jobs that are started within 24 hours in the Running state in the system. For an organization administrator: This section displays the number of backup jobs that are started within 24 hours in the Running state in the current organization. |

s

| Alert Preview | - | Displays the number of alerts in total and the number of alerts at four levels in a circular chart: Urgent, Critical, Warning, and Information. Displays the details of all alerts and the details of alerts at four levels in lists: Urgent, Critical, Warning, and Information. You can click different tabs to view the details of alerts at different levels. Note The details of all alerts in the system are displayed when you log on as an operations administrator. The details of all alerts in the organization are displayed when you log on as an organization administrator. |
|---|---|---|

## 6 User guide

The user guide page provides the overview, usage process, best practices, and key concepts of Apsara Stack Resilience for Backup and Recovery (ASR-BR). This page also provides quick access to product documentation.
1. Log on to the ASR-BR console as a backup operations administrator or organization backup
administrator.
2. In the left-side navigation pane, click **User Guide**.
For the backup operations administrator: If you are an organization backup administrator, you can view the following page:

| Module | Description |
|---|---|
| Quick access to the Overview page | Click Go to the home page to go to the Overview page of theA SR-BR console. |
| Quick access to product documentation | Click Product Documentation to view the documentation of ASR-BR. |
| Usage process | If you are a backup operations administrator, you can view the overview of the following processes: synchronizing a license, creating a storage pool, configuring flow control, managing self-backup, and managing alerts. You can also quickly go to the page of the corresponding module. If you are an organization backup administrator, you can view the overview of the following processes: creating a backup vault, creating a backup plan, creating a recovery task, and managing alerts. You can also quickly go to the page of the corresponding module. |
| Back up data to Alibaba Cloud public cloud | You can view the benefits, preparation, and procedure for backing up data to Alibaba Cloud public cloud. |
| Best practices | You can view the best practices for using databases, file storage services, and big data services to back up data. Click Product Documentation to view the corresponding best practices. |
| Key concepts | The links of the key concepts of ASR-BR are provided to allow you to quickly access the corresponding documentation page. |

## 7 Create a storage pool

Storage pool groups are physical clusters where backup data is stored. A storage pool group can contain multiple storage pools that are logically isolated from each other by using AccessKey pairs.

**Prerequisites**

Only operations administrators can create storage pools.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Group**
**Management**.
3. Click **Create Storage Pool Group**. In the **Add Storage Pool Group** dialog box, configure
the parameters and click **OK**.

> **Note:** A maximum of 16 storage pool groups can be created.

| Parameter | Description |
|---|---|

| Storage Pool Group Name | Enter a descriptive name for the storage pool group, such as "Public Cloud Storage Pool Group". Note The name can contain letters, digits, hyphens (-), and underscores ( ). It must be less than 64 characters in length. _ |   |   |   |
|---|---|---|---|---|
| Storage Medium | Valid values: OSS, CDS-OSS, MINIOSS, PanguStor, and SDS. |   |   |   |
| Storage Pool Group Location | The location where the storage pool group resides. Valid values: Local: the current site. Remote: a site in another region. Alibaba Cloud Public Cloud: Alibaba Cloud public cloud. |   |   |   |
| endpoint | The domain name or IP address of the storage medium. Note The endpoint must be accessible. IPv6 addresses are not supported. If a NAT gateway is used and port mapping needs to be added, specify the parameter in the following format: <Endpoint>: <Port> . |   |   |   |
|   |   | <Endpoint>: |   |   |
| Bucket (optional) | The storage capacity of the storage pool group. Unit: TB. Note The sum of the storage capacity of all storage pools in the group must be smaller than this value. Otherwise, storage pools fail to be created. If you leave this parameter empty, the storage capacity is unlimited. |   |   |   |

|   |   | <Port> |
|---|---|---|

4. In the storage pool group list, click the name of the storage pool group.
5. On the page that appears, click **Create Storage Pool**. In the **Add Storage Pool** dialog
box, configure the parameters.

| Parameter | Description |
|---|---|
| Storage Pool Name | Enter a descriptive name for the storage pool group, such as "Public Cloud Storage Pool". Note The name can contain letters, digits, hyphens (-), and underscores ( ). It must be less than 64 characters in length. _ |
| Bucket | The storage capacity of the storage pool. Unit: TB. |
| AccessKey ID | The AccessKey ID of the account that accesses the destination storage. Note The AccessKey ID and AccessKey secret must have the permissions to read and write data. |
| AccessKey Secret | The AccessKey secret of the account that accesses the destination storage. |
| Authorized Organization | Select the level-1 organizations. You can select all level-1 organizations. |

| Recycle Bin | Optional. Specify the name of the recycle bin. This parameter is required if you need to create a deduplication backup vault or a mirror vault in the storage pool. Note When you create a deduplication backup or mirror vault, an existing bucket of the recycle bin is used if any. If no bucket exists, a relevant bucket is created. |
|---|---|
| Storage Pool Description (optional) | The description of the storage pool for easy identification. |

6. Click **OK**.

## 8 Instance management

### 8.1 View the instance list

You can view the status of an instance in the primary cloud center and the backup plans of the instance in the instance list of the Instances page.

**Background information**

An organization administrator can view only the instances of the current organization. An operations administrator can view the instances of all organizations.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Instances**.
3. On the page that appears, click the tab of the service whose instances you want to view.
4. Specify search conditions and click **Search**.
The following table describes the supported search conditions.

| Search condition | Description |
|---|---|
| Organization | Select an organization from the drop-down list to query all instances in the organization. |
| Resource Set | Select a resource set from the drop-down list to query all instances in the resource set. |
| Instance ID | Enter the ID of an instance to search for the instance. |

| Instance Status | Filter instances by status. |
|---|---|

5. In the instance list, view the instance status and the associated backup plans.

**Related operations**

On the Instances page, you can also perform the following operations.

| Operation | Procedure |
|---|---|
| View instance details | 1. Click an instance name or click and then select Details in the Actions column to go to the Instance Details page. 2. View the details of an instance. Backup Records tab: displays all backups of the instance. Log Backup tab: displays the binary log backup records of ApsaraDB RDS instances and PolarDB clusters. Backup Recovery Events tab: displays all events during the backup and restoration of the instance. |
| View backup plans | 1. Click a plan name in the Backup Plan column. 2. View the information, records, logs, events, and statistics of the backup plan. |

### 8.2 Change the backup policy of an instance

**an instance**

You can change the backup plan of an instance. After you change the backup plan, the instance inherits the backup policy that is specified in the new backup plan.

**Prerequisites**

The instance is added to a backup plan.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Instances**.
3. Click the cloud service tab that you want to manage.
4. Select an organization, resource set, and instance status from the corresponding drop-
down lists, enter an instance ID, and then click **Search**.
5. After the instances that match the search conditions are displayed, click the name of a
backup plan in the **Backup Plan** column.
6. On the **Backup Plans** tab, click **Change Policy**.
7. On the backup policy configuration page, reset the backup policy. For more information,
see Create a backup plan.
8. Click **OK**.

### 8.3 View backup durations

Apsara Stack Resilience for Backup and Recovery (ASR-BR) uses a line chart to display the durations of the recent several backups. The durations displayed on the chart help you analyze network congestions and schedule backups to prevent network congestions.

**Prerequisites**

The instance is included in a backup plan.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Instances**.
3. Click the tab of the corresponding instance type.
4. On the Instances page, find the instance whose backup duration you want to view, click the
icon in the **Actions** column, and then select **Backup Duration**.
5. Move the pointer over a position in the chart to view the backup durations. You can also
view the points in time when backups started and ended.
6. (Optional) In the upper-right corner of the page, adjust the number of recent backups that
are displayed in the chart. ASR-BR allows you to view the durations of the recent 10, 20, 30, and 50 backups.

## 9 Backup vault

### 9.1 Create a backup vault

A backup vault is a logical storage space that is planned on a storage pool. A backup vault is an Object Storage Service (OSS) bucket that is used to back up business data.

**Prerequisites**

A storage pool is created. For more information, see Create a storage pool. The backup administrator or operator creating a backup vault must belong to a level-1 organization authorized by the storage pool. Otherwise, the storage pool cannot be viewed.

**Background information**

In V3.16 and later, you can create multiple database backup vaults. In a storage pool, you can create multiple database backup vaults, storage backup vaults, deduplication backup vaults, and Tablestore backup vaults. ApsaraDB RDS, PolarDB, and PolarDB-X 1.0 use the same database backup vault. Organization backup administrators and organization backup operators can create database backup vaults, storage backup vaults, and deduplicating backup vaults.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. On the **Backup Vaults** page, click **Create**.
4. In the **Create Backup Vault** dialog box, set the following parameters.

| Parameter | Description |
|---|---|

| Vault Name | The name of the backup vault. Example: public cloud backup vault. Note We recommend that you specify an informative name. After a backup vault is created, you cannot change its name. The name can only contain lowercase letters, digits, and hyphens (-). The name cannot start with a hyphen (-). The name must be 3 to 35 characters in length. |
|---|---|
| Description (Optional) | The description of the backup vault. |
| Backup Service Type | The type of the service whose data will be backed up in this vault. Valid values: Database: ApsaraDB RDS, PolarDB, and PolarDB-X 1.0 are supported. Storage: OSS, ECS, and NAS are supported. Tablestore: Tablestore is supported. Deduplication: Only MaxCompute is supported. |
| Enable HTTPS | Specify whether to use the HTTP or HTTPS protocol to create the backup vault and back up data to the backup vault. By default, HTTPS is enabled. You can manually disable HTTPS. Note This parameter is valid only when you set the Backup Service Type parameter to Database, Storage , or Tablestore. If no HTTPS port can be connected to OSS, we recommend that you turn off Enable HTTPS. |
| Storage Location | The location where the backup data is stored. Valid values: Local: The backup data is stored in the OSS buckets of the current region. Remote: The backup data is stored in the OSS buckets in another region. Alibaba Cloud Public Cloud: The backup data is stored in the OSS buckets on Alibaba Cloud public cloud. Note If you set the Backup Product Type parameter to Tablestore, you must set Storage Location to Remote. |

| Storage Pool | The storage pool to which the backup vault belongs. |
|---|---|
| Bucket Name | If you specify a bucket, the bucket is used as the backup vault. You must an existing bucket name in OSS here. Note If you do not have permissions to create buckets in the selected storage pool, you must specify this parameter. |
| Storage Capacity | The storage size of the backup vault. Unit: GB. Note The storage size of the backup vault cannot exceed that of the storage pool that it belongs to. |

5. Click **OK**.

> **Note:** If the storage vault fails to be created, the storage resources may be insufficient. You must scale in storage resources before creating it again.

**Execution result**

ASR for Backup and Recovery automatically creates an OSS bucket in the selected storage pool. Then, the storage pool is used to back up your business data.

### 9.2 View data in a backup vault

You can view information about the files in an Object Storage Service (OSS) bucket that is created for a backup vault on a regular basis. This way, you can obtain information about backup and recovery plans and modify the plans at the earliest opportunity.
1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. Find the backup vault that you want to manage in the list of backup vaults, click the
icon in the **Actions** column, and then click **Browse**.
4. In the message that appears, view the following information about the files in the OSS
bucket: names, sizes, and update time.

> **Note:** If the OSS bucket contains folders, you can click the name of a folder to view the file directories in the folder.

5. Click **OK**.

### 9.3 Manage backup vaults

This topic describes how to view, modify, and delete backup vaults.

**Background information**

Backup operations administrators, backup organization administrators, and backup organization operators can modify the name and storage capacity of backup vaults. Organization backup administrators and organization backup operators can delete backup vaults that are not associated with any backup plans, and whose data has expired.

**View the backup vault.**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. In the backup vault list, click a vault name. You can view the basic information, storage
pool usage, and operation records of the backup vault.
4. On the Backup Vault Association Chart tab of the backup vault, you can view the
information about other vaults associated with the backup vault.
5. Click the Mirror Vault tab to view the information of the mirror vault, including
Synchronization Progress, Vault Usage, and Storage Pool Proportion.

**Modify a backup vault**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. In the backup vault list, click the
icon in the **Actions** column and select **Modify**.
4. Change the vault name and storage capacity. Then, click **OK**.

**Delete a backup vault**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. In the backup vault list, click the
icon in the **Actions** column and select **Delete**.
4. In the message that appears, click **OK**.

### 9.4 Create a mirror vault

A mirror vault is a special backup vault that is used to save the data replicas of a backup vault. After a mirror vault is created for a backup vault, the data in the backup vault will be automatically replicated to the mirror vault by using the cross-region and cross-cloud replication capabilities of OSS. This way, backup data is stored in multiple regions. During data restoration, you can choose either the backup vault or the mirror vault to restore the data.

**Background information**

You can create a mirror vault and associate a backup vault with the mirror vault to manage the mirror vault. In the ASR-BR console, you can back up the business data of each cloud service to the backup vault and then synchronize the data from the backup vault to the mirror vault.

**Constraints**

The bucket used by a mirror vault must be an empty bucket. You can create a mirror vault only for a storage pool whose storage medium is OSS, CDS- OSS, or PanguStor. The type of a mirror vault cannot be modified after it is created.

**Prerequisites**

A backup vault is created. For more information, see Create a backup vault. A storage pool is created, and the recycle bin and cross-region and cross-cloud replication authorization information are configured. For more information, see Create a storage pool. The preparations are completed. For more information, see Preparations for using the storage cascade feature of a backup vault.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. On the Backup Vaults page, select **Vault Location**, **Vault Type**, and **Vault Name**, and
then click **Search**.
4. Click the
icon in the **Actions** column and then select **Create Mirror Vault**.
5. Configure the parameters by referring to the descriptions in the following table.

| Parameter | Description |
|---|---|
| Mirror Vault Name/ID | User-defined. You can also set it to the name of a backup vault. After a mirror vault is created, you cannot change its name. The name can only contain lowercase letters, digits, and hyphens (-). The name cannot start with a hyphen (-). The name must be 3 to 35 characters in length. |
| Description | The description of the vault. This parameter is optional. We recommend that the description is the same as that of the backup vault to facilitate maintenance. |
| Backup Service Type | The system automatically fills in the value. |
| Storage Pool | Select a storage pool from the drop-down list. Note If no options are available, create a storage pool. For more information, see Create a storage pool. |

| Bucket Name | If you specify a bucket, the bucket is used as the mirror vault. Note This parameter is required if you do not have the permission to create buckets in the selected storage pool. The specified bucket must be an empty bucket. |
|---|---|
| Storage Space | The value must be greater than or equal to 1,000 GB because the storage space of the mirror vault cannot be smaller than the storage space of the backup vault. |

6. Click **OK**.
After the mirror vault is created, it is displayed in the list on the **Backup Vaults** page.
7. Click the
icon in the **Mirror Vault** column to display the mirror vault list. The number indicates the number of mirror vaults attached to the backup vault. View the basic information and synchronization status of a mirror vault: Click a mirror vault name or bucket name to view the basic information, operation records, backup vault association chart, and mirror vault.

> **Note:** If the **Status** column indicates that the creation or synchronization failed, you can click **Retry** in the **Actions** column to create a mirror vault or synchronize data again.

Modify a mirror vault: a. Click **Edit** in the **Actions** column. The Edit Mirror Vault dialog box appears. b. After you modify the parameter values, click **OK**. Disconnect the mirror vault from the backup vault: a. Click **Disconnect** in the **Actions** column. b. In the message that appears, click **OK**.

> **Note:** If the disconnection fails, the possible reason may be that the data replication link fails to be disconnected due to source OSS exceptions. After the source OSS recovers, data may still be synchronized even though the disconnection in the ASR-BR console fails.
> If the disconnection succeeds, the availability of the backup sets of the mirror vault remains the same as that of the backup vault. When the backup records of the backup vault expire, the backup data of the mirror vault cannot be used for data restoration.

## 10 Backup plans

### 10.1 Create a backup plan

This topic describes how to create a backup plan. After you create a backup plan, ASR for Backup and Recovery regularly backs up data from the specified instance to the backup vault.

**Prerequisites**

You are an organization backup administrator or organization backup operator. Only organization backup administrators and organization backup operators can create backup plans. Backup operations administrators cannot create backup plans. A backup vault is created. For more information, see Create a backup vault. If you want to back up and restore data for MaxCompute instances, the external table feature of MaxCompute is enabled and the MaxCompute Enhancement Pack for Joint Computing (Spark on MaxCompute) is deployed. The Cloud Assistant is installed on the Elastic Compute Service (ECS) instance for which you want to create a backup plan and the Cloud Assistant runs as expected. (Optional) If you want to create a backup plan for a MaxCompute instance, first specify compute units (CUs) dedicated for the backup operations of the instance to ensure that the backup operations does not interfere with ongoing business operations. For more information, see Configure parameters.If you do not specify CUs for the backup operations of the instance, the CUs of the current project are used. A message indicating that no project is running appears when you configure the instance.

**Background information**

ASR for Backup and Recovery allows you to back up ApsaraDB RDS data and metadata such as user information, permissions, and specifications. ASR for Backup and Recovery allows you to back up Apsara File Storage NAS file systems that use the Network File System (NFS) protocol or Server Message Block (SMB) protocol. ASR for Backup and Recovery allows you to back up the metadata of MaxCompute tables, functions, resources, and projects. The metadata includes quota information, cluster information, virtual private cloud (VPC) information, and security information. ASR for Backup and Recovery allows you to backup data of the following AnalyticDB database types: C8, H20, C20, and B7. ASR for Backup and Recovery allows you to back up Tablestore tables whose names do not exceed 100 characters. If you want to back up Tablestore tables whose names exceed 100 characters, contact the ASR for Backup and Recovery R&D team.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, click **Create**.
4. In the **Basic Information** step, configure the parameters and click **Next**. The following
table describes the parameters.

| Parameter | Description |
|---|---|

| Backup Plan Name | The name of the backup plan. Note The name must be 4 to 128 characters in length and can contain only letters, digits, hyphens (-), underscores ( ), and _ periods (.). |
|---|---|
| Description (optional) | The description of the backup plan. We recommend that you enter a description that can help you identify the backup plan. |
| Instance Type | The type of the instance that you want to back up. Note If you want to create a Tablestore backup plan, set the Instance Type to Tablestore. |
| Backup Method | The backup method of the instance. This parameter is available only when you set the Instance Type parameter to Elastic Compute Service. Valid values: Snapshot Backup: backs up an ECS instance or the specified disks of an ECS instance. File Backup: backs up ECS files. |

5. In the **Select Instance** step, select the instance that you want to back up and click **Next**.

> **Note:** Only instances in the **In Use** state can be backed up.
> A backup plan is created for only a single instance.
> You can create only one backup plan for an ApsaraDB RDS, PolarDB, PolarDB-X, or AnalyticDB instance. You cannot create a backup plan for an instance that is in **protected** state.
> An Object Storage Service (OSS) bucket can be added to multiple backup plans simultaneously.
> An Apsara File Storage NAS file system can be added to multiple backup plans simultaneously.
> An ECS instance can be added to a backup plan that uses the Cloud Disk Backup method and a backup plan that uses the File Backup method simultaneously.
> An ECS instance that uses the File Backup method can be added to multiple backup plans simultaneously.
> A Tablestore instance contains multiple tables. If you select the Tablestore instance type, you can view the tables of the instance in the **Tablestore Table** column.

6. (Optional) Select Tablestore tables. This step is required only if you set the **Instance Type**
parameter to **Tablestore** at the **Basic Information** step. i. In the left-side section, select the names of the tables that you want to back up.

> **Note:** You can select only two tables for a Tablestore instance at a time. If you select one or two Tablestore tables, the data of the tables are backed up at the same time. If you select three or more Tablestore tables, the additional tables have to wait in a queue until the system is free to back up them.

ii. Click to add the selected Tablestore tables to the right-side section. iii. Click **Next**.
7. (Optional) In the **Install Client** step, configure the parameters for installing the Hybrid
Backup Recovery (HBR) client, and then click **Next**.

> **Note:** This step is applicable only to ECS instances that use the **File Backup** method.
> The ECS Cloud Assistant is used when installing the HBR client. Make sure that the ECS Cloud Assistant is installed on the ECS instance and is in the normal state.

| Instance type | Parameter | Description |
|---|---|---|
|   | Client Installation Path (optional) | The directory where the HBR client is installed on the ECS instance. Note If you leave this parameter empty, the HBR client is installed in the /root directory. |

|   | Number of CPU Cores on Client | The maximum number of CPU cores that can be used by the HBR client. The system automatically displays the number of CPU cores of the current ECS instance. When the HBR client starts a backup task, the backup task is allocated based on the value you specified for this parameter. Note A larger number of CPU cores indicates that the HBR client uses more resources on the host and has a larger negative impact on the performance of the host. We recommend that you specify a suitable value based on your business requirements. |
|---|---|---|
| ECS (file backup) |   |   |
|   | Max. Number of Worker Threads on Client | The maximum number of threads that can be used by the HBR client. Default value: 10. When the HBR client starts a backup task, the backup task is allocated based on the value you specified for this parameter. Note A larger number of threads indicates that the HBR client uses more resources on the host and has more negative impacts on the performance of the host. We recommend that you specify a suitable value based on your business requirements. |

|   | Client Installation Status (optional) | After you specify Number of CPU Cores on Client and Max. Number of Worker Threads on Client , click Install to install the HBR client. You can click Refresh to refresh the installation status. After the installation status changes to The client is installed., you can perform the next step. The system automatically performs a connectivity test. Note After the HBR client is installed, you can modify the values of Number of CPU Cores on Client and Max. Number of Worker Threads on Client. You can also uninstall the client when it is no longer needed. The right-side section of the Install Client page displays the installation information of the HBR client, including the client installation status, client version number, heartbeat keep-alive time, and the maximum number of CPU cores and threads used by the HBR client. If keepalive does not time out, you can uninstall the client or perform connectivity testing. If keepalive times out, you can uninstall or reinstall the client. If the HBR client has been installed on your ECS instance, the client installation status is "The client is installed." when you create a backup plan for the ECS instance. |
|---|---|---|

8. In the **Configure Instance** step, configure the parameters and click **Next**.

> **Note:** Skip this step if you create a backup plan for an ApsaraDB RDS, PolarDB, Tablestore, or PolarDB-X instance.

| Instance type | Parameter | Description |
|---|---|---|

|   | OSS Prefix (optional) | Click Browse. On the Browse Directory page, select the directory that you want to back up. The Browse Directory displays the directories of the bucket. You can select the objects that you want to back up from the bucket. Note If you leave this parameter empty, all objects in the bucket are backed up. The value of OSS Prefix are separated by and end with forward slashes (/). The value cannot contain the following characters: angle brackets (<>), backslashes (\), vertical bars (\|), colons (:), quotation marks ("), asterisks (*), and question marks (?). If a bucket contains a large number of objects, we recommend that you create multiple backup plans for the bucket and specify a portion of the objects in the bucket for each backup plan. |
|---|---|---|
|   | Backup File Filtering Policy | The filtering policy of files that you want to back up. Valid values: All: backs up all files that meet the prefix conditions specified in OSS Prefix. By Time Range: backs up objects whose last modification time is within the specified time range. By Last Days: backs up objects that are last modified in the specified last few days. Note The last modification time of an object is the start time of its last backup cycle. |
|   | Time Range for File Filtering | If you set Backup File Filtering Policy to By Time Range, you must specify the start time and end time of the time range. Note Only objects whose last modification time falls within the specified time range are backed up. The time range cannot be left empty. |
|   | Filter Files in Recent Days | If you set Backup File Filtering Policy to By Last Days, you must specify a specific number for Filter Files in Recent Days. |

| Object Storage Service (OSS) |   |   |
|---|---|---|
|   | Number of Concurrent Backups | The number of concurrent reads and writes. When you create a backup plan for objects in an OSS bucket, you can specify the maximum number of concurrent reads from the source and concurrent writes to the destination. We recommend that you configure the number of concurrent backups based on the number and average size of objects in the bucket. If you set this parameter to Default, the system uses the minimum number of concurrent backups. Note The system automatically recommends the appropriate number of concurrent backups based on the throttling policy and the number and average size of objects in the bucket. |
|   | Inventory function | This parameter is available when you set the Instance Type parameter to CDS-OSS in Step 4. After you enable the inventory feature, ASR for Backup and Recovery creates a Resource Access Management (RAM) role that has the read and write permissions on OSS to configure and generate OSS inventory lists. When you create a backup plan for objects in an OSS bucket, the OSS inventory feature is used to back up data from the OSS bucket. Note After you enable the inventory feature, OSS inventory lists are used to obtain incremental objects in a bucket. You do not need to traverse the objects in the bucket. If your bucket has more than 100 million objects, we recommend that you enable the OSS inventory feature. |
|   | Bucket | This parameter is available only when the inventory feature is enabled. The bucket where OSS inventory lists are stored. |
|   | Inventory Report storage path | This parameter is available only when the inventory feature is enabled. The directory in which OSS inventory lists are generated. If you do not configure this parameter, OSS inventory lists are generated in the root directory. |
|   | Inventory cleanup policy | This parameter is available only when the inventory feature is enabled. The policy that is used to clear OSS inventory lists after each backup. The default policy is to delete all inventory lists after a backup. Note Three policies are supported: delete all inventory lists after backup, delete the current inventory lists after backup, and do not delete inventory lists. |

|   | OSS Endpoint (optional) | The endpoint that you want to use to read data from the OSS bucket. You can use a custom endpoint to read data from a source OSS bucket. To specify a custom endpoint, select Custom from the OSS Endpoint drop-down list. We recommend that you use a non-business OSS endpoint for backup. Note If you leave this parameter empty, the system uses the default OSS endpoint to read data from a source OSS bucket. The system automatically estimates the required backup traffic based on the throttling policy. Make sure that the backup traffic will not affect the business traffic. If you use a custom endpoint for the backup plan, make sure that the custom endpoint can be used to read data from the source bucket. |
|---|---|---|
|   | Backup Estimation | The estimated backup speed, first full backup time, and subsequent incremental backup time are displayed. |
| ECS (snapshot backup) | Backup Type | Complete Backup: backs up the entire ECS instance. Cloud Disk Backup As Specified: backs up the specified disks of an ECS instance. If you set the Backup Type parameter to Cloud Disk Backup As Specified, click Browse to select one or more cloud disks based on your business requirements. |
|   | Forcibly Create Snapshot- consistent Group | Disabled (default): creates a snapshot-consistent group first. If the snapshot-consistent group fails to be created because the creation conditions are not met or due to or other causes, a standard snapshot is created. Enabled: forcibly creates a snapshot-consistent group. If the snapshot-consistent group fails to be created because the creation conditions are not met or due to or other causes, a standard snapshot is not created and the backup fails. Note Do not enable this feature unless otherwise specified. |
|   | File Path | The path of the files that you want to back up. For more information, see the tooltip in the user interface. |
|   | Objects | Valid values: Include All: backs up all files in the path. Exclude: backs up all files in the path except those specified by the Files parameter. Include: backs up the files specified by the Files parameter. |

| ECS (file backup) |   |   |
|---|---|---|
|   | Files | The files included in or excluded from the backup plan, depending on the option that is selected for Objects. For more information, see the tooltip in the user interface. |
|   | Traffic Threshold (optional) | An optional parameter for setting traffic throttling for a specified period of time when you back up data from a production center to a backup vault. For more information, see the tooltip in the user interface. You can set different traffic thresholds for peak hours and off- peak hours based on your business requirements. For example, you can set a high traffic threshold for off-peak hours and a low traffic threshold for peak hours to maximize the use of your bandwidth. |
| NAS | File Path | The absolute path of the NAS file to be backed up. The wildcard * is not supported. |
|   | Number of Concurrent Backups | The maximum number of backup processes that can run simultaneously to back up data from the source to the destination. Select the number of concurrent backups based on the number and average size of NAS files. |
| MaxCompute | Source Resource | Specify whether to back up a table or project. Valid values: Table Backup: backs up a single table or multiple tables. Project Backup: backs up all tables, resources, and functions in a project. You can specify the tables, resources, and functions that you want to back up by configuring a whitelist or blacklist. |
|   | Temporary Table Prefix (optional) | The name must be 1 to 128 bytes in length, and can contain letters, digits, and underscores ( ). We recommend that you _ start the name with a letter. |
|   | Backup Gateway | Select the backup gateway from the drop-down list: Default Policy: The system selects a backup gateway of the HBR service to execute the backup plan based on the workloads specified by each customer. Other Backup Gateway: You can also select another registered backup gateway. |

| VMware Cloud on Alibaba Cloud |   |   |
|---|---|---|
|   | Transmissio n Mode | LAN-fee Backup Data Transmission (default): hot-mounts the disk that you want to back up to the backup gateway and transmits backup data over a non-LAN network. LAN refers to the local area network. LAN-based Backup Data Transmission: transmits backup data over a LAN. Note If the vCenter does not support LAN-free data transmission, the system automatically switches to the LAN mode. |
|   | Snapshot Type | Standard Snapshot: uses VMware software snapshots to perform common backup. System Silent Snapshot (default): uses VMware Tools to perform silent backup. Note If VMware Tools cannot be mounted or is not installed, the system automatically switches to the standard snapshot mode for backups. |

9. In the **Backup Policy** step, configure the backup policy and click **Next**.

> **Note:** The parameters of the backup policy vary based on the instance type. You can configure the parameters based on the on-screen instructions.

The following table describes the backup policy parameters.

| Parameter | Description |
|---|---|

| Backup Policy | The backup policies vary based on the instance type. Full: All data in the database is backed up based on the specified cycle. If you select this policy, only the data that is backed up at the point in time when the backup is created can be restored. This policy is available only when you set the Instance Type parameter to RDS. Full Data and Logs: All data in the database is backed up based on the specified cycle. In addition, incremental data is backed up during the interval between backup cycles. If you select this policy, the data that is backed up at all points in time can be restored. This policy is available only when you set the Instance Type parameter to ApsaraDB RDS, PolarDB, or PolarDB-X. Incremental: The first backup is a full backup and the subsequent backups are incremental backups. This policy is available only when you set the Instance Type parameter to OSS. If you set Instance Type to OSS, the subsequent backups after the first backup are incremental backups at the object level. Full (Data Deduplication): All data in the database is backed up based on the specified cycle. Data is deduplicated during the backup process. This policy is available only when you set the Instance Type parameter to ECS (file backup) or NAS. Incremental (Deduplication): The first backup is a full backup and the subsequent backups are incremental backups. When an incremental backup is performed, ASR for Backup and Recovery deduplicates data by bucket. This policy is available only when you set the Instance Type parameter to MaxCompute. Full and Incremental: You can perform full backups and incremental backups based on the specified intervals. This policy is available only when you set the Instance Type parameter to ECS (cloud disk backup). |
|---|---|
| Backup Mode | This policy is available only when you set the Instance Type parameter to PolarDB-X. Valid values: Fast Backup: This mode ensures data consistency only in a single ApsaraDB RDS database. We recommend that you select this mode for routine backups. Consistent Backup: This mode ensures data consistency in all databases within a PolarDB-X instance. We recommend that you select this mode for industries that have high requirements for data consistency or for online core transactions. Important We recommend that you perform consistent backups during off-peak hours. The system locks distributed transactions within seconds during a consistent backup. This may cause sub-second response time. |

| Cycle | Run by Week: This type of cycle is available only if you set the Instance Type parameter to RDS. Run By Day: This type of cycle is available only if you set the Instance Type parameter to OSS, ECS (file backup), NAS, or MaxCompute. |
|---|---|
| Select the Day of the Week | The day of the week when you want to perform a backup. If you want to select multiple days, we recommend that you select the days that are at regular intervals. For example, you can select Monday, Thursday, and Sunday. Note This policy is available only when you set the Instance Type parameter to RDS. For data availability, we recommend that you select at least two days each week. If you set Backup Policy to Full Data and Logs, we recommend that you select a maximum of two days of a week. This consumes less bandwidth and storage space. |
| Interval (Incremental) | The time interval between two backups. This parameter is available only when you set the Instance Type parameter to OSS, NAS, ECS (cloud disk backup), or MaxCompute and set the Backup Policy parameter to Incremental. Note The system automatically estimates the number of days that are required for the first full backup of the OSS instance and recommends a backup interval that is greater than the specified value of this parameter. |
| Time Interval (Incremental) | The time interval between two incremental backups. This parameter is available only when you set the Instance Type parameter to Elasticsearch and the Backup Policy parameter to Full and Incremental. |
| Time Interval (Full) | This parameter is available only when you set the Instance Type parameter to Elasticsearch and the Backup Policy parameter to Full and Incremental. The time interval between two full backups. Set Interval (Full) to a value greater than the value of Interval (Incremental) |
| Interval (Full [Data Deduplication] ) | This parameter is available only when you set the Instance Type parameter to ECS (file backup) and the Backup Policy parameter to Full (Data Deduplication). |

| Backup Time (Increment) | The time when the backup is performed for the first time. The subsequent incremental backups are performed at the specified intervals. We recommend that you schedule the first backup task to happen at off-peak hours. Note This parameter is available only if you set the Instance Type parameter to OSS, RDS, ECS (file backup), PolarDB-X, or MaxCompute. You must set the Backup Time parameter to at least one hour after the current time. If you set the Backup Time parameter to less than one hour after the current time, the instance may not be backed up on the same day. Instead, it will be backed up during the next backup cycle. |
|---|---|
| Storage Location | The location to which the data is backed up. You cannot select bothR emote and Alibaba Cloud Public Cloud. Valid values: Local: The data is backed up to a backup vault of the production center. Remote: The data is backed up to a backup vault of a remote data center. Alibaba Cloud Public Cloud: The data is backed up to a backup vault of Alibaba Cloud public cloud. |
| Backup Vault (Local) | This parameter is available only if you set the Instance Type parameter to OSS, NAS, MaxCompute, or ECS (file backup). The local backup vault to which you want to back up the data. If you do not find the backup vault that you want to use, click Create Backup Vault to create one. |
| Retention Period (Days) (Local) | The maximum number of days for which backup data is retained in an on- premises backup vault. The default value is 7. You can enter an integer from 7 to 730. Note Expired backup data will be deleted. |
| Backup Vault (Remote) | This parameter is available only when you set the Instance Type parameter to OSS, NAS, MaxCompute, RDS, PolarDB, or ECS (file backup). The backup vault in a remote data center. If you cannot find the backup vault that you want, click Create Backup Vault to create one. |
| Retention Period (Days) (Remote) | The maximum number of days for which backup data is retained in a remote backup vault. The default value is 7. You can enter an integer from 7 to 1460. Note Expired backup data will be deleted. |

| Backup Vault (Public Cloud) | The backup vault in Alibaba Cloud public cloud to which you want to back up the data. If you cannot find the backup vault that you want, click Create Backup Vault to create one. |
|---|---|
| Retention Period (Days)/Data Backup Retention Period (Days) (Public Cloud) | The maximum number of days for which backup data is retained in a backup vault that is deployed in Alibaba Cloud public cloud. The default value is 7. You can enter an integer from 7 to 1460. Note Expired backup data will be deleted. |
| Enable Log Backup | By default, this parameter is disabled. After you enable this parameter, log data is retained. Note If local log backup is disabled, the remote log backup must be disabled. |
| Log Backup Retention Period (Days) | This parameter is required if you turn on Enable Log Backup. The value of this parameter must be less than or equal to the value of theD ata Backup Retention Period (Days) parameter. |

The following table describes the backup policy parameters for the disks of ECS instances.

| Step | Parameter | Description |
|---|---|---|
| Backup Policy (Local) | Cycle (Full) | You can specify the interval at which the disks of ECS instances are backed up. The interval is measured in days or hours. Valid values: RUN By Day: The disks are backed up at intervals of specified days. By Hour: The disks are backed up at intervals of specified hours. |
|   | Time Interval | The time interval between two backups. If you set the Cycle (Full) parameter to RUN By Day, the interval is measured in days. If you set the Cycle (Full) parameter to By Hour, the interval is measured in hours. |
|   | Backup Time | The time when the backup is performed for the first time. The subsequent incremental backups are performed at the specified intervals. We recommend that you schedule the first backup task to happen at off-peak hours. |

|   | Retention period (day) | The maximum number of days for which backup data is retained in a local backup vault. For example, if you set this parameter to 7, the backup data of the last 7 days is retained. Backup data that is generated more than 7 days ago is deleted. |
|---|---|---|
|   | Backup Policy | The backup policy for a remote backup vault. Valid values: Incremental: The first backup is a full backup, and subsequent backups are incremental backups. Full and Incremental: You can perform full backups and incremental backups based on the specified intervals. |
| Backup Policy (Remote) |   |   |
|   | Time Interval (Incremental) | The value of this parameter is the same as the value of the Time Interval parameter in the Backup Policy (Local) step. |
|   | Cycle (Full) | This parameter is available only when you set the Backup Policy parameter to Full and Incremental. Only Run by Day is supported. Use the default value. |
|   | Time Interval (Full) | This parameter is available only when you set the Backup Policy parameter to Full and Incremental. You can specify the number of days between full backups. The minimum value is 7. By default, the interval for incremental backups is the same as the value of the Time Interval parameter in the Backup Policy (Local) step |
|   | Backup Time | The system automatically inputs the value. Use the default value. |
|   | Backup Vault (Remote) | The backup vault in a remote data center. If you do not find the backup vault that you want, click Create Backup Vault to create one. |
|   | Retention Period (Days) (Remote) | The maximum number of days for which backup data is retained in a remote backup vault. |

0. Confirm your backup settings and click **Submit**. You can select Start Now based on your
business requirements. If you select **Start Now**, the backup plan is immediately started after it is created. The system backs up the instances that are specified in the plan based on your settings. If you clear **Start Now**, you must manually start the backup plan after it is created. For more information, see Start a backup plan.

### 10.2 View a backup plan

This topic describes how to view a backup plan. You can view the status of the backup plan and the result of the last backup task.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Plans**.
3. Search for a backup plan. You can use the following search conditions: Primary
Organization, Resource Set, Plan Name, Plan Status, Instance Type, Instance ID, and Instance Name. The following table describes the parameters of a backup plan.

| Parameter | Description |
|---|---|
| Plan Status | The status of the backup plan. Valid values: Creating: The backup plan is being created. Created: The backup plan has been created and is being started. Running: The backup plan is running, and the instance is waiting for backup. Backing Up: The instance in the backup plan is being backed up. Not Started: The backup plan is not started. Stopped: The backup plan is stopped. Stopping: The backup plan is being stopped. Deleted: The instance in the backup plan is physically deleted. |
| Last Backup Result | The result of the last backup task. Valid values: Successful Backing Up Failure Not Started None Note If the value of Last Backup Result is None, the backup plan is started but no backup tasks are performed. |

> **Note:** By default, the backup plans of VMware VMs are not displayed in the backup plan list. If you want to view the backup plans of VMware VMs, you can select **VMware** from the **Instance Type** drop-down list and click **Search**.

### 10.3 Start a backup plan

If you do not select Start Now when you create a backup plan, you must manually start the backup plan.

**Prerequisites**

The value of **Plan Status** is **Not Started** or **Stopped**.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, select **Not Started** or **Stopped** from the **Plan Status** drop-
down list, and click **Search**.
4. Find the backup plan that you want to start, click the
icon in the **Actions** column, and then click **Start**.

### 10.4 Perform an immediate backup

**backup**

If a periodic backup fails or the data of your instance is significantly changed, we recommend that you perform an immediate backup to ensure data security.
1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, search for the backup plan that you want to use. You can
specify the following search conditions: a primary organization, a resource set, a plan name, a plan state, an instance type, an instance ID, and an instance name.
4. In the list of backup plans, find the backup plan that you want to use, click the
icon in the **Actions** column, and then click **Back up Now**.
5. In the message that appears, click **OK**. Then, the status of the backup plan changes to
**Backing Up**.

### 10.5 Stop a backup plan

This topic describes how to stop a backup plan. If you no longer want to execute an applied backup plan, you can stop it.

**Prerequisites**

Only backup plans in the Backing Up or Running state can be stopped.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, find the desired backup plan. You can use search conditions to
search for the desired backup plan.
4. In the backup plan list, find the backup plan that you want to stop, click the
icon in the
**Actions** column, and then click **Stop**.

> **Note:** Stopped backup plans do not consume license resources.

### 10.6 Modify the configurations of a backup plan

**a backup plan**

If you want to add or delete resources from a backup plan for an Object Storage Service (OSS), Elastic Compute Service (ECS), Apsara File Storage NAS, or MaxCompute instance, you can modify the configurations of the backup plan. This topic describes how to modify the configurations of a backup plan.

**Procedure**

1. Log on to the ASR for Backup and Recovery console as an organization backup
administrator.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, search for a backup plan by using search conditions.
4. Click the name of the backup plan.
5. On the **Overview** tab of the page that appears, click **Configure** in the **Backup**
**Information** section.
6. Configure the parameters for an instance and click **OK**.

> **Note:** The parameters that are provided on the Overview tab vary based on the instance type. You can configure the parameters as prompted.

### 10.7 Modify the backup policy of a backup plan

**backup plan**

This topic describes how to modify the backup policy of a backup plan. A backup policy includes the backup policy name, backup time, retention type, and maximum retention period of backup data.

**Procedure**

1. Log on to the ASR-BR console as an organization administrator.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, search for a backup plan by using search conditions.
4. Click the name of the backup plan.
5. In the **Backup Policy** section of the **Overview** tab, click **Change Policy**.
6. Modify the parameters of the backup policy and click **Submit**.

> **Note:** The parameters that are provided on the Overview tab vary based on the instance type. You can configure the parameters as prompted.

### 10.8 View log backup files

You can view the log files of ApsaraDB RDS instances and PolarDB clusters that are backed up in the current region or across regions.

**Background information**

The **Log Backup** tab is only available on the backup plan details page of ApsaraDB RDS instances and PolarDB clusters. Data is available on the Log Backup tab only when you create a backup plan for an ApsaraDB RDS instance and set the Backup Policy parameter to **Full Data and Logs**.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, find the backup plan that you want to view. You can use
search conditions to search for the backup plan.
4. Click the name of the backup plan.
5. Click the **Log Backup** tab to view the log files that are backed up in the current region or
across regions.

> **Note:** Data is available on the **Log Backup** tab only when you set the Backup Policy parameter to **Full Data and Logs**.

### 10.9 View a backup event

You can view the log of events that are executed in a backup plan.
1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, find the backup plan that you want to view. You can use
search conditions to search for the backup plan.
4. Click the name of the backup plan.
5. Click the **Source Log** tab. On the tab, configure the **Start Time**, **End Time**, or **Event**
**Status** search conditions, and click **Search**.
6. Click **Log** in the **Actions** column to view the log of the event.
7. Click the
icon to the left of the event to view sub-events and their statuses. Click the icon to the right of a sub-event to view the sub-event log.

**Successful**

**Canceled**

This status is displayed when a sub-event is canceled.
**Failed**, **Timed Out**, and **Stop**
If a sub-event is in one of the preceding states, you can click the icon next to the subevent to retry the sub-event.

> **Important:** This operation is an event O&M operation. If the most recent event is successfully executed, do not perform the retry operation for the previous event.

**Waiting for start**, **Execution in progress**, and **Synchronizing**
If a sub-event is in one of the preceding states, you can click the icon to the right of the sub-event to cancel it.

> **Important:** This operation is an event O&M operation. This operation is irreversible. Proceed with caution.

### 10.10 View the statistics about a backup plan

**backup plan**

This topic describes how to view the statistics about a backup plan on the Statistics tab in the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console. The statistics include the durations and success rates of the last several backups that are performed based on a backup plan.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, find the backup plan whose statistics you want to view. You
can use search conditions to search for the backup plan.
4. Click the name of the backup plan.
5. On the page that appears, click the **Statistics** tab.

> **Note:** On the Statistics tab, you can view the durations and success rates of the backups performed based on the backup plan. By default, the durations and success rates of the last 10 backups are displayed. You can also view the durations and success rates of the last 20, 30, or 50 backups.

## 11 Backup records

### 11.1 Backup flow overview

The Backup Flow Overview tab shows the overall storage usage, and the historical storage usage in the current region, other regions, and Alibaba Cloud public cloud.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Backup Records**.
3. On the page that appears, click the **Backup Flow Overview** tab.
In the tree map chart, you can view the total data size, and the data size of backups stored in the current region, different regions, and Alibaba Cloud public cloud. Data under protection is accounted for the data amounts, and instances that have been backed up are accounted for the instance numbers. The bar chart shows the storage usage in the current region, other regions, and Alibaba Cloud public cloud over the past 3, 6, and 12 months.

### 11.2 View backup records

You can view the details of a backup record, including the corresponding backup set data. You can also delete backup records.

**Background information**

Operations administrators can view backup record details and the corresponding backup set data but cannot delete backup records. Organization administrators can view backup record details and the corresponding backup set data, and delete backup records. The local and remote backup records of ApsaraDB RDS instances and the local backup records and backup failure records of PolarDB for Xscale (PolarDB-X) instances can only be viewed. The remote records of PolarDB-X and the backup records of Object Storage Service (OSS), Apsara File Storage NAS, Elastic Compute Service (ECS), and MaxCompute can be deleted, and the backup set data in the backup records can be viewed. The backup data volume or backup set size is displayed for storage instances such as Object Storage Service (OSS), Apsara File Storage NAS, and Elastic Compute Service (ECS) instances.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click the **Backup Records** tab.
3. On the **Backup Records** page, click the **Backup Records** tab.
To view the backup records of a backup plan, perform the following steps: a. In the left-side navigation pane, click **Backup Plans**. b. On the **Backup Plans** page, find the backup plan whose backup records you want to view. You can use search conditions to search for the backup plan. c. Click the name of the backup plan. d. On the page that appears, click the **Backup Records** tab. To view the backup records of an instance, perform the following steps: a. In the left-side navigation pane, click **Instances**. b. On the **Instances** page, find the instance whose backup records you want to view. You can use search conditions to search for the instance. c. Click the icon in the **Actions** column and then click **Details**. d. On the page that appears, click the **Backup Records** tab.
4. Specify search conditions and click **Search**.
You can view the instance name, instance type, backup set size, backup status, backup start time, duration, task progress, storage location of backup records (local or remote), and backup method.

> **Note:** You cannot view the size of the backup files of a failed backup task.

5. Click **Details** in the **Actions** column to view the details of the backup record, including the
backup configurations.

> **Note:** You can browse the backup file size or delete a backup record only when the **Record** **Status** is **Successful** or **Partially Successful**.

Click **Browse** to view the corresponding backup set and the size of backup files stored in the backup set. Click **Delete** to delete the backup record and the data stored in backup sets.

> **Note:** In the Record Browsing dialog box of a PolarDB-X cluster that is backed up across regions, information about the databases and tables in the corresponding backup set is displayed.
> In the Record Browsing dialog box of an OSS, Apsara File Storage NAS, and ECS (file backup) instance, the first and last backup files of each backup set are displayed. You can click the names of the files to view all files in the backup set.
> The Browse operation is not supported by an Apsara File Storage NAS file system and an ECS (file backup) instance that has more than 3 million files and whose backup records exceed 900 GB.
> In the Record Browsing dialog box of an ECS (instance backup) instance, the metadata of each disk is displayed.
> In the Record Browsing dialog box of a MaxCompute instance, the information about the tables, resources, and functions stored in the backup set is displayed.

## 12 Recovery jobs

### 12.1 Create a routine recovery job

This topic describes how to create a routine recovery job. You can use routine recovery jobs to recover data that is accidentally deleted.

**Prerequisites**

You are an organization backup administrator. Only organization backup administrators can create routine recovery jobs. A backup plan is created and the first backup of the instance that you want to recover is completed.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. Click **Create**.
4. In the **Basic Information** step, configure the parameters and click **Next**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Recovery Job Name | The name must be 4 to 20 bytes in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Description | Optional. We recommend that you enter a description to help you identify the job. |
| Instance Type | The type of the instance that you want to recover. |
| Recovery Job Type | In this scenario, select Routine Recovery. |
| Recovery Method | The recovery method. This parameter is available only when you set the Instance Type parameter to ECS. Valid values: Snapshot Recovery: This recovery method is available only when the backup method of the ECS instance is snapshot backup. File Recovery: This recovery method is available only when the backup method of the ECS instance is file backup. |

5. In the **Select Instance** step, select an instance from the **Backup Instance** drop-down list,
and then click **Next**.

> **Note:** The **backup instance** list shows only the instances that have been backed up.

6. In the **Select Record** step, select a **backup record** or a **specific point in time** for
recovery. Then, click **Next**. Select Backup Record: Click the **Select Backup Record** tab. On the Select Backup Record tab, click **Select** in the **Actions** column, and select the record of the backup that you want to recover. By Time Node: On the **By Time Node** tab, click **Select** in the **Actions** column. Specify a point in time to which you want to recover the instance.

> **Note:** Only ApsaraDB RDS instances and PolarDB clusters can be recovered to a specific point in time.
> For PolarDB-X 1.0 remote records, Object Storage Service (OSS), Apsara File Storage NAS, ECS, and MaxCompute backup records, click **Browse** when you select a record to view the data stored in the backup record.

7. In the **Configure Instance** step, click **Configure** in the **Actions** column. In the dialog box
that appears, configure the parameters, click **OK**, and then click **Next**. The following table describes the parameters in the Configure Instance step for ApsaraDB RDS and PolarDB-X 1.0 instances.

| Section | Parameter | Description |
|---|---|---|
| Basic Information | Recovery Method | Default value: Created. The default value cannot be changed. For this recovery method, an instance is created in the primary cloud center. |
|   | Region | The region in which the new instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Zone | The zone in which the new instance resides in the primary cloud center. |
|   | Organization | The organization to which the new instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the new instance belongs in the primary cloud center. |
|   | Instance Name | The name of the new instance. We recommend that you specify an informative name. ASR for Backup and Recovery automatically creates the instance in the primary cloud center. The name must be 2 to 64 bytes in length and can contain letters, digits, hyphens (-), and underscores ( ). _ It must start with a letter. |

| Network Type | Connection | The network connection mode of the new instance. By default, the network connection mode of the backup instance is used. The value of this parameter cannot be changed |
|---|---|---|
|   | Network Type | The network type of the new instance. Classic Network: Alibaba Cloud services in the classic network are not isolated. Access control to the services in the classic network is implemented by using the security groups or whitelist policies of the services. VPC: A virtual private cloud (VPC) helps you build an isolated network environment in Apsara Stack. If you set the Network Type parameter to VPC, you must specify a VPC and a vSwitch. |
|   | VPC | The VPC in which the new instance that you want to recover resides. This parameter is available only when you set the Network Type parameter to VPC. |
|   | vSwitch Zone ID | The Zone ID of the vSwitch to which the new instance that you want to recover belongs. This parameter is available only when you set the Network Type parameter to VPC. |
|   | vSwitch | The vSwitch to which the new instance that you want to recover belongs. This parameter is available only when you set the Network Type parameter to VPC. |
| Specifications |   | By default, the specifications of the backup instance are used. The specifications cannot be modified. |
| RDS Note This parameter is available only when you set the Instance Type parameter to PolarDB-X 1.0. | Database Type | Default value: mysql. This value cannot be modified. |
|   | Specifications | The instance type of the instance. Note The instance type of the new instance must be the same as that of the backup instance. |
|   | Storage Capacity | The storage space of the instance. Unit: GB. |

The following table describes the parameters in the Configure Instance step for instances of the OSS and Apsara File Storage NAS types.

| Section | Parameter | Description |
|---|---|---|
| Basic Information | Recovery Method | The recovery method. Valid values: Created: An instance is created in the primary cloud center. Overwritten: The original instance is overwritten after recovery. |
|   | Region | The region in which the new instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Organization | The organization to which the new instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the new instance belongs in the primary cloud center. |
|   | Bucket Name or File System Name | If you set the Recovery Method parameter to Overwritten, select the instance that you want to overwrite in the primary cloud center. If you set the Recovery Method parameter to Created, specify an informative instance name. ASR for Backup and Recovery automatically creates the instance in the primary cloud center. The instance name must be 3 to 35 bytes in length and can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit. |
|   | Destination Prefix | The name of the OSS directory. This parameter is available only when you set the Instance Type parameter to OSS. OSS automatically creates the directory and recovers objects in your OSS bucket to the directory. If you leave this parameter empty, the objects are recovered to the root directory of your OSS bucket. |
|   | File Path | The path of the file that you want to recover. This parameter is available only when you set the Instance Type parameter to NAS. |

|   | Objects | The recovery rules. This parameter is available only if the Instance Type parameter is set to OSS. Valid values: Include All: All files in the path specified by the File Path parameter are recovered. Include: Only the files specified by the Files parameter are recovered. Exclude: The files that are not included in the files specified by the Files parameter are recovered. |
|---|---|---|
| Recovery Rule |   |   |
|   | Files | The folder names or file names. You can specify only one name in each line. This parameter is required only when you set the Object parameter to Include or Exclude. |

|   | Restore File Time Range | If you set the Instance Type parameter to OSS and want to recover objects whose last modification time falls within a specific time range in the backup set, configure the Recovery start time and Recovery end time parameters. Note Objects that are last modified within the specified time range are recovered when ASR for Backup and Recovery runs the recovery job. If you specify only the recovery start time, objects last modified within the time range from the specified start time to the current time are recovered from the backup set. If you specify both the recovery start time and end time, objects last modified within the time range are recovered from the backup set. If you do not specify a time range for recovery, all objects in the backup set are recovered. |
|---|---|---|
|   | Restore Concurrency Configuration | If you set the Instance Type parameter to OSS, you can specify the number of concurrent reads and writes based on your bandwidth. |
| Specifications |   | By default, the specifications of the backup instance are used. The specifications cannot be modified. |

The following table describes the parameters in the Configure Instance step for the recovery of ECS file backup.

| Section | Parameter | Description |
|---|---|---|
| Destination | Recovery Method | Default value: Overwrite Recovery. The default value cannot be changed. |
|   | Region | The region in which the new instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Zone | The zone in which the new instance resides in the primary cloud center. |
|   | Organization | The organization to which the new instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the new instance belongs in the primary cloud center. |
|   | Destination Instance | The instance that you want to overwrite in the primary cloud center. |
|   | File Path | Click Select and select the path of the file that you want to recover. |
| Install Client | Client Installation Status | The installation status of the Hybrid Backup Recovery (HBR) client. If the status is The client is not installed., click Install. Then, the system automatically installs the client. |
|   | Client Installation Path | The installation path of the HBR client on the ECS instance. Note If you leave this parameter empty, the system automatically installs the HBR client to the root directory. If the value of Client Installation Status is The client is installed., the installation path of the client is displayed. |
|   | Client Version | The version of the installed client. If the value of Client Installation Status is The client is not installed., the value of this parameter is -. |
| Document Versio | n: 20250618 6 |   |

|   | Keep-alive Timeout | The keep-alive timeout of the installed client. If the value of Client Installation Status is The client is not installed., the value of this parameter is -. |
|---|---|---|
| Recovery Rule | Objects | The recovery rules. Valid values: Include All: All files in the path specified by the File Path parameter are recovered. Include: Only the files specified by the Files parameter are recovered. Exclude: The files that are not included in the files specified by the Files parameter are recovered. |
|   | Files | Click Browse to select a folder or a file. This parameter is available only when you set the Object parameter to Include or Exclude. |

The following table describes the parameters for the recovery of ECS snapshot backup.

| Section | Parameter | Description |
|---|---|---|
| Recovery Rule | Recovery Rule | The recovery rule depending on the backup plan: Complete Recovery Specified Disk Recovery i. Click Edit in the Actions column. ii. Select a disk type from the drop-down list and click OK. |
|   | Recovery Method | Default value: Created. The default value cannot be changed. For this recovery method, an instance is created in the primary cloud center. |
|   | Region | The region in which the new instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Zone | The zone in which the new instance resides in the primary cloud center. |
|   | Organization | The organization to which the new instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the new instance belongs in the primary cloud center. |

| Basic Information |   |   |
|---|---|---|
|   | Instance Name | The name of the instance. This parameter is available only when you set the Recovery Rule parameter to Complete Recovery. We recommend that you specify a name that can help you identify the instance. ASR for Backup and Recovery automatically creates the instance in the primary cloud center. The name must be 2 to 64 bytes in length and can contain letters, digits, hyphens (-), underscores ( ), and _ colons (:). It must start with a letter. |
|   | Hostname | The hostname of the instance. This parameter is available only when you set the Recovery Rule parameter to Complete Recovery. We recommend that you specify an informative hostname for easy identification. |
|   | Destination ECS Instance | Select the instance to which the disk is attached. This parameter is available only when you set the Recovery Rule parameter to Specified Disk Recovery. |
| Network Type Note This parameter is available only when you set the Recovery Rule parameter to Complete Recovery. | Network Type | The network type of the instance. It is automatically set to VPC. |
|   | VPC | The VPC in which the new instance that you want to recover resides. |
|   | vSwitch | The vSwitch to which the new instance that you want to recover belongs. |
|   | Security Group | The security group to which the ECS instance belongs. |
|   | Private IP Address | Enter a private IP address. The IP address must be within the CIDR block of the selected vSwitch. |
| Specifications | Instance Edition | Select the instance from the drop-down list. |
|   | Instance Type | Select the instance type of the instance. |
|   | Image Type | Select the image to be used. Valid values: Public image Custom image Shared custom image |

|   | Public Image/Custom Image/Shared Custom Image | Select an image depending on the image type. Note If the image exists on the current page, fuzzy search is supported. If the image does not exist on the current page, enter the full image name and press the Enter key to search for it. |
|---|---|---|

The following table describes the parameters for the recovery of MaxCompute clusters.

| Section | Parameter | Description |
|---|---|---|
| Basic Information | Recovery Method | Valid values: Created and Overwritten. Overwritten: For non-partitioned tables, the tables are deleted and then recreated. For partitioned tables, the partitions are deleted and then recreated. |
|   | Region | The region in which the new instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Organization | The organization to which the new instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the new instance belongs in the primary cloud center. |
|   | Instance Name | We recommend that you specify a name that can help you identify the instance. ASR for Backup and Recovery automatically creates the instance in the primary cloud center. The name must be 2 to 64 bytes in length and can contain letters, digits, and underscores ( ). It must start _ with a letter. |
|   | Cluster | Select the MaxCompute cluster that you want to recover. |
| Basic Configuration | Recovery Content | Table Recovery: Select one or more tables. Project Recovery: By default, all data of the TABLE, RESOURCE, and FUNCTION types in the backup record is recovered. |

8. Specify whether to immediately start the recovery job based on your business
requirements, confirm your recovery settings, and then click **Submit**. If you select **Start Now**, the recovery job immediately starts after it is created. If you clear **Start Now**, the recovery job does not immediately start after it is created. You can manually start the recovery job. For more information, see Start a recovery job.

### 12.2 Start a recovery job

This topic describes how to start a recovery job. If you do not select **Start Now** when you create a recovery job, you must manually start the job.

**Prerequisites**

The recovery job is in the **Not Started** state.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. On the **Recovery Jobs** page, enter **Not Started** in the **Job Status** search box and click
**Search**.
4. In the recovery job list, find the recovery job that you want to start, click the
icon in the
**Actions** column, and then click **Start**.

### 12.3 Stop a recovery job

This topic describes how to stop a recovery job. You can stop a recovery job only when the job is in the **Recovering** state.

**Prerequisites**

The recovery job that you want to stop is in the **Recovering** state.

**Impact**

If you stop a recovery job that is in the Recovering state, the recovery fails. However, the failure does not affect other operations.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. On the **Recovery Jobs** page, enter **Recovering** in the **Job Status** search box and click
**Search**.
4. In the recovery job list, find the recovery job that you want to stop, click the
icon in the
**Actions** column, and then click **Stop**.

### 12.4 View recovery jobs

This topic describes how to view the status and details of a recovery job and the details of each restored instance.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. On the Recovery Jobs page, search for a recovery job by using the following search
conditions: Job Name, Recovery Type, Instance Type, and Job Status. In the recovery job list, view the type, creation time, and status of the recovery job, and the type of the restored instance.
4. Click the name of the recovery job to view the details of the job. The details include the
basic information about the recovery job and the restored instance, and the execution result of the recovery job.
5. Find a restored instance, click the
icon in the **Actions** column, and then click Details.

### 12.5 View the log of a recovery event

**event**

You can view the recovery event log of a restored instance on the details page of the corresponding recovery job.
1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. On the Recovery Jobs page, configure the Job Name, Recovery Type, Instance Type, or Job
Status search conditions and click Search to search for a recovery job whose log you want to view.
4. Click the name of the recovery job.
5. Click the **Recovery Events** tab. On the Recovery Events tab, query logs by start time, end
time, or event status.
6. In the **Actions** column, click **Log** to view the log details.
7. Click the
icon to the left of the event to view the sub-events and their statuses. Click the icon to the right of a sub-event to view the sub-event log.

**Successful**

**Canceled**

This status is displayed when a sub-event is canceled.
**Failed**, **Timed Out**, and **Stop**
If a sub-event is in one of the preceding states, you can click the icon next to the subevent to retry the sub-event.

> **Important:** This operation is an event O&M operation. If the most recent event is successfully executed, do not perform the retry operation for the previous event.

**Waiting for start**, **Execution in progress**, and **Synchronizing**
If a sub-event is in one of the preceding states, you can click the icon to the right of the sub-event to cancel it. If you cancel the sub-event, its status changes to **Canceled**.

> **Important:** This operation is an event O&M operation. This operation is irreversible. Proceed with caution.

VMware VMs

## 13 Backup and recovery of VMware VMs

**VMware VMs**

### 13.1 Install a backup gateway

This topic describes how to install a backup gateway in VMware ESXi by using an OVA file.

**Prerequisites**

The asrbr-vmware-appliance.ova file that is used to install the backup gateway is downloaded.

**Background information**

The Apsara Stack Resilience for Backup and Recovery (ASR-BR) console supports only vCenter Server versions 5.5, 6.0, 6.5, and 6.7. A backup gateway is a virtual machine (VM) that is installed in vCenter Server. The backup gateway uses RabbitMQ to communicate with the hbr-console component and calls vCenter API operations to create snapshots, back up data, and recover data. Backup gateways are required for VM backup, local recovery, on-cloud recovery, and cloud migration.

**Procedure**

1. Enter the IP address of VMware ESXi in a browser, enter the logon username and password,
and then click **Log in**.
2. In the left-side navigation pane, click **Virtual Machines** and then click **Create/Register**
**VM**.
3. In the **New virtual machine** dialog box, select **Deploy a virtual machine from an OVF**
**or OVA file** and click **Next**.
VMware VMs
4. Enter a name for the VM, select the OVA file **asrbr-vmware-appliance.ova**, and then click
**Next**.
5. Select a storage type and datastore, and click **Next**.
6. Use the default settings in the **Deployment options** step, and click **Next**.
VMware VMs
7. In the **Additional settings** step, configure the parameters and click **Next**.
8. In the **Ready to complete** step, click **Finish**.
9. In the **Recent tasks** section, view the task status. If the task is in the **Completed**
**successfully** state, the VM is deployed.
VMware VMs
0. After the VM is deployed, start the VM.

### 13.2 Register a backup gateway

This topic describes how to register a backup gateway. Before you can register a backup gateway, you must obtain the activation code of the gateway from the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.

**Obtain the activation code**

1. Log on to the ASR-BR console as an organization administrator.
2. In the left-side navigation pane, choose **System Management** > **vCenters**.
3. Click **Activation Code** to view the activation code.

**Register a backup gateway**

1. In the address bar of your browser, enter the endpoint of the virtual machine (VM) where
the backup gateway resides. The endpoint is in the format of `<IP address>:8011` .
2. In the Register dialog box, set the following parameters.

| Parameter | Description |
|---|---|

VMware VMs

| Host Address | The IP Address that you obtained from the View Activation Code dialog box. |
|---|---|
| Host Port | The IP Port that you obtained from the View Activation Code dialog box. |
| Activation Code | The Activation Code that you obtained from the View Activation Code dialog box. |

> **Note:** If DNS is not configured for vCenter Server or Apsara Stack, you must enter an IP address for Host Address.

3. Click **OK**.

### 13.3 Create a vCenter

You can use vCenter to manage VMware virtual machines (VMs). This topic describes how to create a vCenter.

**Prerequisites**

VMware VMs are backed up.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console as an
organization administrator.
2. In the left-side navigation pane, choose **System Management** > **vCenters**.
3. Click **Create**.
4. In the **Create vCenter** dialog box, set the following parameters.

| Parameter | Description |
|---|---|

VMware VMs

|   | IP Address | The IP address of the vCenter. |   |
|---|---|---|---|
|   | Username | The username that you can use to log on to the vCenter. The username is in the Username for single sign-on@Domain name for single sign-on format. |   |
|   |   |   | Username for single sign-on@Domain |
|   |   | name for single sign-on |   |
|   | Password | The password that you can use to log on to the vCenter. The value is the single sign-on (SSO) password that you specify on the SSO page. |   |

5. Click **OK**.

### 13.4 Create a backup plan for a VM

**VM**

This topic describes how to create a backup plan for a VMware VM. You can use the backup plan to back up the disk data of the VMware VM to a backup vault.
1. Log on to the ASR for Backup and Recovery console as an organization administrator.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the Backup Plans page, click **Create**.
4. In the **Basic Information** step, configure the parameters and click **Next**.
5. In the **Select Instance** step, select the required vCenter ID, select the VM that you want to
back up, and then click the icon. Click **Next**. VMware VMs
6. In the **Configure Instance** step, configure the parameters in the following table and click
**Next**.

| Parameter | Description |
|---|---|
| Backup Gateway | Select the backup gateway client from the drop-down list. Valid values: Default Policy: The system selects a backup gateway of the HBR service to execute the backup plan based on the workloads specified by each customer. Other Backup Gateway: You can also select another backup gateway that has been registered. |
| Transmission Mode | LAN-free Backup Data Transmission (default): If you select Lan-Free, the disk that you want to back up is hot mounted on the backup gateway, and data is transferred over a storage area network (SAN) instead of a local area network (LAN). LAN-based Backup Data Transmission: Data is backed up over a LAN. Note If the SAN network is not supported in the vCenter, the system automatically switches to the LAN mode. |
| Snapshot Type | Standard Snapshot: uses VMware software snapshots to perform common backup. System Silent Snapshot (default): uses VMware Tools for silent backup. Note If VMware Tools cannot be mounted or is not installed, the standard snapshot mode is automatically used in backup. |

7. In the **Backup Policy** step, configure the parameters in the following table and click **Next**.
VMware VMs

> **Note:** If the full backup task coincides with an incremental backup task, the full backup task is executed first.

| Backup policy | Parameter | Description |
|---|---|---|
| Full | Time Interval | The interval (days) to perform a backup task. You must enter an integer. |
|   | Backup Time | The time to perform a backup task. |
|   | Backup Vault | The backup vault in a remote data center. If you do not find the backup vault that you want to use, click Create Backup Vault to create one. |
|   | Retention Period (Days) | The maximum number of days for which backup data is retained in an on-premises backup vault. For example, if you set this parameter to 7, the backup data of the last 7 days is retained. Backup data that is generated more than 7 days ago is deleted. |
| Incremental | Cycle | You can specify the interval at which the data backed up. The interval is measured in days or hours. Valid values: By Day: The data is backed up at intervals of specified days. By Hour: The data is backed up at intervals of specified hours. |
|   | Time Interval | The interval to perform a backup task. You must enter an integer. Unit: day or hour |
|   | Backup Time | The time to perform a backup task. |

VMware VMs

> **Note:** If you want to configure an incremental backup policy, you need to make sure that Changed Block Tracking (CBT) is enabled on the VM. For information about how to enable CBT, see Changed Block Tracking (CBT) on virtual machines (1020128).

8. Confirm your backup settings, select Start Now based on your business requirements, and
then click **Submit**. If you select **Start Now**, the backup plan is immediately started after it is created. The system backs up the instances that are specified in the plan based on your settings. If you clear **Start Now**, you must manually start the backup plan after it is created. For more information, see Start a backup plan.

### 13.5 Restore a VMware VM

If a VMware VM is faulty, you can restore the VMware VM to an Elastic Compute Service (ECS) instance or an on-premises vCenter Server instance by using the backup records of the VM.
1. Log on to the ASR for Backup and Recovery console as an organization administrator.
2. In the left-side navigation pane, click **Recovery Jobs**.
3. On the Backup Plans page, click **Create**.
4. In the **Basic Information** step, set the parameters and click **Next**.

| Parameter | Description |
|---|---|
| Recovery Job Name | The name of the restoration job. The name must be 4 to 20 characters in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Description | The informative description of the restoration job for identification. |
| Instance Type | The instance type of the restoration job. In this example, select VMware Cloud Server. |
| Recovery Job Type | The type of the restoration job. Valid values: Local Recovery and Recovery on Cloud. Local Recovery: restores the VMware VM to an on-premises vCenter Server instance. Recovery on Cloud: restores the VMware VM to an Apsara Stack ECS instance. |

5. In the **Select Instance** step, select an instance, click the
icon, and then click **Next**.

> **Note:** The **Instances** list shows only the instances that have been backed up.

VMware VMs
6. In the **Select Record** step, click the **Select Backup Record** tab and click **Select** in the
**Actions** column. In the dialog box that appears, select the backup record that you want to
use and click OK. Then, click **Next**.
7. In the **Configure Instance** step, click **Configure** in the **Actions** column. In the dialog box
that appears, configure the parameters, click **OK**, and then click **Next**. The following table describes the parameters that you must configure if you set **Recovery**
**Job Type** to **Recovery on Cloud**.

| Category | Parameter | Description |
|---|---|---|
| Basic Information | Region | The region in which the ECS instance resides in the primary cloud center. The value of this parameter cannot be changed. |
|   | Organization | The organization to which the ECS instance belongs in the primary cloud center. |
|   | Resource Set | The resource set to which the ECS instance belongs in the primary cloud center. |
|   | Zone | The zone in which the ECS instance resides in the primary cloud center. |
|   | Hostname | The hostname. Enter a descriptive hostname that is easy to identify. |
|   | Name | The instance name. Enter a descriptive name that is easy to identify. ASR for Backup and Recovery automatically creates an ECS instance in the primary cloud center. The name must be 2 to 128 characters in length and can contain letters, digits, hyphens (-), underscores ( ), _ periods (.), and colons (:). The name must start with a letter. |
| Network Type | Classic Network/VPC | The network type of the new instance. Classic Network: Alibaba Cloud services in the classic network are not isolated. Access control to the services in the classic network is implemented by using the security groups or whitelist policies of the services. VPC: A virtual private cloud (VPC) helps you build an isolated network environment in Apsara Stack. If you set the Network Type parameter to VPC, you must specify a VPC and a vSwitch. |
|   | vSwitch | The vSwitch to which the ECS instance belongs in the primary cloud center. |

VMware VMs

|   | Security Group | The security group to which the ECS instance belongs. |
|---|---|---|
|   | Private IP Address | Enters a private IP address. The IP address must be within the CIDR block of the selected vSwitch. |
| Specifications | Instance Generation | Selects an ECS instance generation from the drop-down list. |
|   | Instance Type | The specifications of the ECS instance. |
|   | Disk Category | Selects the disk type of the ECS instance based on your business requirements. Ultra Disk: suitable for scenarios that require stable and persistent storage and moderate performance. Standard SSD: suitable for scenarios that require high I/O performance. Premium Performance Disk: suitable for small and medium-sized applications and relational databases such as MySQL and SQL Server that require high data reliability and moderate performance. Standard Performance Disk: suitable for business scenarios in which data access is infrequent and the I/O load is minimal. |
|   | Restart System After Recovery | Specifies whether to restart the system after restoration. |
|   | Create System Image | Specifies whether to create a system image. If you turn on Create System Image, the system creates an image based on the data of all disks of the ECS instance in the primary cloud center. The disks include the system and data disks. |

The following table describes the parameters that you must configure if you set **Recovery**
**Job Type** to **Local Recovery**.

| Parameter | Description |
|---|---|
| vCenter Address | The destination vCenter Server address for VM restoration. |
| Address for Recovery | The destination address for VM restoration. |

VMware VMs

| Compute node | The compute node used by the restored VM. |
|---|---|
| Location | The location where the restored VM is stored. |
| Network Location | The network where the restored VM resides. |

8. Verify the basic information and the configurations of the instance to which the VM is
restored and click **Submit**. You can select or clear Start Now based on your business requirements. If you select **Start Now**, the restoration job is immediately started after it is created. If you clear **Start Now**, the restoration job is not started after it is created. You must manually start the restoration job. For more information, see Start a restoration job.

## 14 System management

### 14.1 Manage storage pool groups

This topic describes how to create, modify, and delete storage pool groups and storage pools.

**Create a storage pool group and storage pool**

Create a storage pool group and a storage pool. Fore more information, see Create a storage pool.

**Note**

Storage pools that are created in Apsara Stack earlier than V3.18.1 are merged into storage pool groups based on their endpoints. The names of the storage pool groups are in the following format: AUTO_MERGE_STORAGE_POOL_GROUP_id.

**Modify a storage pool**

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. On the page that appears, click the name of a storage pool group.
4. Click the
icon in the **Actions** column corresponding to a storage pool and click **Edit**.
5. In the **Edit Storage Pool** dialog box, modify the parameters and click **OK**, including
****************, ********************, **Storage Pool Name**, **Bucket**, **************
**Organization**, **Storage Pool Description**.

**Delete a storage pool**

> **Note:** Only storage pools that are not associated with backup vaults can be deleted. Therefore, to delete a storage pool, you must first delete the backup plan, then delete the backup vault, and finally delete the storage pool.

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. On the page that appears, click the name of a storage pool group.
4. On the Storage Pools page, click the
icon in the **Actions** column and select **Delete**.
5. In the message that appears, click **OK**.

**Modify a storage pool group**

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. On the page that appears, click the
icon in the **Actions** column and select **Edit**.
4. In the **Edit Storage Pool Group** dialog box, modify the name and storage capacity limit of
the storage pool group and click **OK**.

**Delete a storage pool group**

> **Note:** Only storage pool groups that do not contain storage pools can be deleted.

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. On the page that appears, click the
icon in the **Actions** column and select **Delete**.
4. In the message that appears, click **OK**.

### 14.2 Manage self-backup

#### 14.2.1 Create a backup policy for metadata

You can create a self-backup policy to periodically back up the metadata of the backup system to a storage pool. If data in the backup system is lost or damaged, you can use the backup metadata restore the data at the earliest opportunity.
1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Self-backup**
**Management**.
3. On the Self-backup Management page, click the **Backup Policy** tab and click **Create**.
Then, configure the following parameters.

| Parameter | Description |
|---|---|
| Backup Cycle | Specify the interval at which the backup is performed. You can select one of the following units from the drop-down list on the right side: Hours and Days. Note The minimum value is 10 minutes. |
| Storage Duration | Specify the retention period of the backup metadata in the storage pool. We recommend that you set this parameter to 7 days. Important If data is stored longer than the specified retention period, the data is automatically deleted. |

| Storage Pool | Select a storage pool. If no storage pools exist, clickC reate Storage on the right side to create a storage pool. For more information, see Create a storage pool. |
|---|---|
| Bucket | Enter the name of the bucket that is used to store the backup metadata in the specified storage pool. Important Record the name of the bucket for future use. When you create a restoration job of the Recovery on Cloud type, you must enter the name of the bucket. |

4. Click **Create**.

#### 14.2.2 View the backup records of metadata

You can view the details of the backup records of metadata. The details include the time when the backup started and ended, the expiration time of the backup data, the status of the backup task, the size of the backup set, and the name of the backup file.
1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console as an
operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Self-backup**
**Management**.
3. On the Self-backup Management page, click the **Backup Records** tab. On the Backup
Records tab, you can view the details of the backup records of metadata. The details include the time when the backup started and ended, the expiration time of the backup data, the status of the backup task, the size of the backup set, and the name of the backup file.
4. (Optional). If you want to delete a backup record and its backup set, find the backup record
and click **Delete** in the **Actions** column. In the message that appears, click **OK**.

> **Note:** You can perform the deletion operation only when you log on to the console as an operations administrator.

### 14.3 Create a disaster recovery job

**job**

If you have a primary cloud and a secondary cloud, and the primary cloud fails, rendering ASR-BR on the primary cloud unavailable, you can deploy ASR-BR on another cloud system or on the secondary cloud and use the disaster recovery feature to restore the backup data stored in the secondary cloud. Disaster recovery jobs do not interrupt the cloud backup and restoration features.

**Scenarios**

You can use the disaster recovery feature only in the following two scenarios: You need to restore backup data from the storage pool in another region to the secondary Apsara Stack system. The primary cloud system becomes unavailable and requires data recovery.

**Prerequisites**

Before a disaster recovery job, a self-backup management policy needs to be configured, and the metadata of ASR-BR needs to be backed up in the storage pool in another region. In addition, the OSS endpoint, AccessKey pair, and the bucket ID used to stored ASR-BR metadata need to be recorded, so that the metadata used to recover ASR-BR can be obtained when a disaster recovery job is needed.

**Procedure**

1. Create a disaster recovery job.
i. Log on to the ASR-BR console as an operations administrator. ii. In the left-side navigation pane, choose **System Management** > **Disaster Recovery**. iii. On the **Disaster Recovery** page, click **Create**. iv. In the **Recover Metadata** dialog box, select a **storage pool** from the drop-down list and specify an OSS bucket in which ASR-BR metadata is stored for the **bucket** parameter. Then, click **Retrieve**. Select the metadata backup from which you want to perform the recovery and then click **Start**. After you click Start, a recovery file record in the **Queueing** state is generated in the
**Disaster Recovery** list.
v. When the metadata is being recovered, the status of the job is changed from **Queueing** to **Running**. vi. After the metadata is recovered, the **Procedure** is changed from **ASR-BR metadata**
**recovery** to **Organizational Revision** and status is changed to **Running**.
2. Revise the organization.
i. When the procedure is **Organizational Revision**, click the icon in the **Actions** column and click **Modify Organization**. ii. In the **Organizational Revision** dialog box, select the desired destination organization. By default, the organization with the same name is matched.

> **Note:** The source and destination organizations must fully match each other.

iii. Click **OK**. The **procedure** of the job changes from **Organizational Revision** to **Metadata**
**revision** and the status changes to **Queueing**.
iv. When the metadata revision starts, the status changes to **Running**. When the metadata revision is completed, the procedure changes from **Metadata revisions** to **Disaster**
**recovery of user data**.
v. Then the organization administrator of each organization needs to perform data disaster recovery.
3. Perform data disaster recovery for each organization.
i. Log on to the ASR-BR console as an organization administrator. ii. In the left-side navigation pane, click **Recovery Jobs**. iii. On the **Recovery Jobs** page, click **Create**. iv. On the **Basic Information** step of the wizard, configure the name of the recovery job, select the instance type to be recovered, and set Recovery Job Type to **Disaster**
**Recovery**. Then, click **Next**.
v. On the **Select Instance** page, select the instances in the **Instances** list, click the icon, and then click **Next**.

> **Note:** The **Instances** list shows only the instances that have been backed up.

vi. On the **Select Record** step, select **Select Backup Record** and click **Next**. Click the Select Backup Record tab. In the Actions column, click Select to select the target backup records.

> **Note:** During the disaster recovery, backup records whose storage location is Local may fail.

vii. In the **Configure Instance** step, click **Configure** in the **Actions** column to configure the required parameters. For more information, see Create a routine recovery job. Click **OK** and then click **Next**. viii. Specify whether to immediately start the recovery job based on your business requirements, confirm your recovery settings, and then click **Submit**. If you select **Start Now**, the recovery job is immediately started after it is created. If you clear **Start Now**, the recovery job does not start immediately after it is created. You can manually start the recovery job. For more information, see Start a recovery job.
4. Complete the disaster recovery job.
i. After the instances of each organization are recovered, log on to the ASR-BR console as an operations administrator. For more information, see Log on to the ASR for Backup and Recovery console. ii. In the left-side navigation pane, choose **System Management** > **Disaster Recovery**. iii. Click the icon in the **Actions** column and click **End Task**. The procedure changes to **Clearing Data**, and the status changes to **Queueing**. iv. When data clearing starts, the status changes to **Running**. When data clearing is completed, the entire disaster recovery process is ended. The procedure changes to **End**
**of disaster recovery**. The status changes to **Completed**.

### 14.4 Manage authorizations

#### 14.4.1 View license resources

If the system notifies you of insufficient licenses or failure of backing up specific instance types during your use of ASR-BR, you can check whether related licenses have been obtained.
1. Log on to the ASR-BR console.
2. In the left-side navigation pane, choose **System Management** > **Authorization**.
3. On the **Authorization Statistics** tab of the Authorization page, you can view information
such as the type of license resources, Total Authorized Amount, Used Resource, and Remaining Resource. The following table describes the license resources.

| Authorization specification name | Description | Calculation method of used license resources |
|---|---|---|
| Storage Authorization (General Purpose) | The backup capacity for storage services. | The total data size of the backup plans in the Running and Backing Up states for Object Storage Service (OSS), Elastic Compute Service (ECS) files, ECS instances, Apsara File Storage NAS, VMware, and MaxCompute. Note If you have separately purchased the license resource of big data or ECS instances, the license resource is preferentially used. If you do not purchase the license resource of big data or ECS instances, you can still use the license resource to create backup plans for MaxCompute and ECS instances. |
| Storage Instance (ECS Server) | The backup capacity for ECS instances and cloud disks. | The total amount of backup data generated based on the backup plans that are in the Running or Backing Up state and for which the Backup Method parameter is set to Cloud Disk Backup. |
| Big Data | The backup capacity for MaxCompute. | The total amount of backup data generated based on the backup plans that are in the Running or Backing Up state and are created for a MaxCompute project. |

| Database Authorization | The storage capacity of backup sets for ApsaraDB RDS and PolarDB-X. | The used storage of backup sets for both RDS and PolarDB-X instances whose backup plans are in the Running or Backing Up state. |
|---|---|---|
| Unified Backup Management Console | Specifies whether backup across regions is allowed. If you do not purchase the license resource, you can back up data only on your computer. | No limits are set for the amount of backup data. |

4. If you have applied for a new quota, click **Sync License** to update the latest license
resources to the ASR-BR console.

#### 14.4.2 Configure resource quotas for an organization

**organization**

This topic describes how to configure resource quotas for an organization as an operations manager. Proper quota configurations and management prevent excess resource consumption by some organizations and consequent resource shortages for other organizations. By default, Apsara Stack Resilience for Backup and Recovery (ASR-BR) does not limit the quantity of resources that an organization can consume.

**Background information**

When an organization consumes 80% of its resource quota for a service, ASR-BR generates a resource usage alert. When an organization consumes 100% of its resource quota for a service, ASR-BR provides limited backup capabilities for the service and generates a resource usage alert. The organization cannot create a new backup plan and initiate an existing backup plan as scheduled or immediately for the service. To prevent existing backup plans from being interrupted, we recommend that you perform the following steps: Increase quotas for the service as an operations administrator. Stop some of the existing backup plans for the service to release resources.

**Procedure**

1. Log on to the ASR-BR console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Authorization**.
3. Click the **Authorization Allocation** tab.
4. Select the organization from the **Organization** drop-down list and click **Search**. View the
resource quota, current usage, and remaining resource quota for each authorization type in your organization.
5. Click **Authorization** in the **Operation** column.
6. In the **Configure Authorization** dialog box, configure a resource quota for each
authorization type and click **OK**.

## 15 O&M Management

### 15.1 Alert management

#### 15.1.1 View alert records

This topic describes how to view alert records and handle related alerts.

**Background information**

An operations administrator can view all alert records in Apsara Stack Resilience for Backup and Recovery (ASR-BR). An organization administrator can view alert records in this organization.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, choose **O&M Management > Alerts**.
3. (Optional) You can click the
icon in the top navigation bar to view the latest five alerts. Click **View More** to view more alert records on the **Alert List** page.

> **Note:** A red dot on the
> icon indicates that you have unread alert records.

4. On the **Alert List** page, query alert records by **Alert Level**, **Alert Object**, **Business Type**,
and **Organization**. View the alert content in the **Alert Content** column.

#### 15.1.2 Mark alerts as read

You can mark handled alerts as read. After alerts are marked as read, the system no longer sends notifications for the alerts.

**Background information**

If a red dot appears on the icon in the top navigation bar, unread alerts exist.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, choose **O&M Management > Alerts**.
3. Specify search conditions to search for an alert. The following search conditions are
supported: **Alert Level**, **Alert Object**, **Business Type**, and **Organization**.
4. Find the alert, click the
icon in the **Actions** column, and then select **Mark As Read**.
5. In the **Mark as Read** message, click **OK**.
6. (Optional) To mark multiple alerts as read at a time, perform the following steps:
i. Select multiple alerts and click **Batch Read** in the upper-left corner of the alert list. ii. In the **Batch Read** message, click **OK**.

#### 15.1.3 Delete alert records

You can delete alert records that have been processed.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, choose **O&M Management > Alerts**.
3. On the Alert List page, query alert records by **Alert Level**, **Alert Object**, **Business Type**,
or **Organization**.
4. Find the alert record that you want to delete, click the
icon in the **Actions** column, and then select **Delete**.
5. In the **Delete** message, click **OK**.
6. (Optional) Delete alert records in batches. To delete alert records in batches, perform the
following steps: i. Select the alert records that you want to delete and click **Delete** in the upper-left corner of the alert list. ii. In the **Batch Delete Messages** message, click **OK**.

### 15.2 Throttling configuration

You can configure throttling thresholds to control the traffic when source instances back up data to backup vaults by time period. You can configure throttling for cloud services and VMware virtual machines (VMs). You can compare the configured throttling threshold with the current traffic to determine whether scale-out is required.

**Background**

The throttling service supports only physical throttling. If multiple backup engines are deployed on a physical server, the backup engines compete for traffic transmission resources. To resolve this issue, ASR for Backup and Recovery provides time-based throttling capabilities that allow you to set different throttling thresholds for different engines to stagger traffic peaks with customer services, thereby ensuring the normal operation of all services. Operations administrators can configure throttling for cloud services, and organization administrators can configure throttling for VMware VMs.

**Configure throttling for cloud services**

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **O&M** > **Throttling Configurations**.
3. On the **Cloud Service** tab, click **Modify Configurations**, configure the parameters, and
then click **Submit**.
4. Click the
icon in the upper-right corner of the Throttling Threshold Configuration section to hide the throttling settings. Click the icon in the upper-right corner again to display the Throttling Threshold Configuration section.
5. After you click **Modify configuration**, a
icon appears next to the time period. You can click the icon to modify an existing time period. You can also click **Add Time Period** to add a new time period. After you complete the configurations, click **OK** to view the throttling information of each time period.

> **Note:** The throttling configurations for different time periods do not affect each other. The throttling configurations of different storage pools do not affect each other.

| Parameter | Description |
|---|---|
| Throttling Threshold for Database Products | The maximum throughput when the production center transfers database product data to backup engines. This is an optional parameter. Valid values: [1, Number of backup engines × 2560]. Unit: MB/s. Note The value of this parameter cannot be larger than the total throttling thresholds for storage pool groups nor the value of the Total Bandwidth parameter. |

| Throttling Threshold of Other Services | The maximum throughput when the production center transfers data of products other than database products to backup engines. This is an optional parameter. Valid values: [1, Number of backup engines × 2560]. Unit: MB/s. |
|---|---|
| Total Bandwidth | The maximum throughput when the production center backs up data to backup engines. ASR-BR ensures that the total bandwidth of all backup tasks is not larger than this value. This is a required parameter. Valid values: [1, Number of backup engines × 2560]. Unit: MB/s. |
| Storage pool group traffic thresholds | The maximum throughput when the production center backs up data to backup engine storage pools. This is an optional parameter. Valid values: [1, Number of backup engines × 2560]. Unit: MB/s. Note The total thresholds of all storage pool groups cannot be larger than the Total Bandwidth value but must be larger than theT hrottling Threshold for Database Products value. |

**Configure throttling for VMware VMs**

1. Log on to the ASR for Backup and Recovery console as an organization administrator.
2. In the left-side navigation pane, choose **O&M** > **Throttling Configurations**.
3. On the **VMware** tab, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Version | Retain the default value. |
| Traffic Threshold | Specify the thresholds for upload and download traffic in specific time ranges when you back up VMware data from the primary cloud center to the secondary cloud center. The value is in the HH:MM-HH:MM- UKB\|HH:MM-HH:MM-DKB format. Note HH:MM-HH:MM specifies the time range for throttling. U specifies the upload traffic. D specifies the download traffic. For example, 09:00-22:00-U512 indicates that the threshold of upload traffic is 512 KB/s from 09:00 to 22:00. |
| Enable | If you turn off the switch, no limits are imposed on traffic when you back up data from a production center to a backup vault. |

|   | UKB\|HH:MM-HH:MM-DKB |
|---|---|

### 15.3 Engine monitoring

You can use the engine monitoring feature to view traffic, CPU, memory, and load statistics. This way, you can adjust your cloud services at the earliest opportunity when traffic spikes occur.
1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **O&M** > **Engine Monitoring**.

> **Note:** The Engine Monitoring page displays the monitoring data of the previous hour.
> If **Enable automatic refresh** is turned on, the system automatically refreshes monitoring data every 60 seconds. If Enable automatic refresh is turned off, you can select a time range and a host and then click **Search** to query the monitoring data of the host of a backup engine in the specified time range.

3. You can view the inbound and outbound traffic of the hosts of the HBR-agent and Gulltoppr
backup engines on the **Traffic Monitoring** page.
4. You can view the average and maximum CPU utilization of the backup engines on the **CPU**
**Monitoring** page.
5. You can view the average and maximum memory usage of the backup engines on the
**Memory Monitoring** page.
6. You can view the average and maximum load usage of the backup engines every 1 minute,
every 5 minutes, and every 15 minutes on the **Load Monitoring** page. You can select
**Average Usage** or **Maximum Usage** from the **Load Options** drop-down list.

### 15.4 View resource statistics

This topic describes how to view the storage space usage and the number of backup plans of vault resources and organization resources.

**Background information**

Operations administrators can view the resource statistics of all organizations. Organization administrators can view only the resource statistics of their own organizations.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, choose **System Management** > **Resource Statistics**.
3. On the page that appears, click **Vault Resources**, select a date, and then click **Search**.
You can perform the same method when you click **Organization Resources** instead of Vault Resources on the page that appears. The following table describes the parameters of vault resources.

| Parameter | Description |
|---|---|
| Vault Name | The name of the backup vault. |

| Space Usage | The size of storage space that is used by the backup vault. The value that is enclosed in parentheses () specifies the size of incremental storage space that is used on the current day. |
|---|---|
| Organization | The organization that uses the backup vault. |
| Resource Set | The resource set that uses the backup vault. |
| Backup Plans | The number of backup plans that use the backup vault. |

The following table describes the parameters of organization resources.

| Parameter | Description |
|---|---|
| Organization | The name of an organization. |
| Space Usage | The size of the backup vault that is used by the backup instances in the organization. The value that is enclosed in parentheses () specifies the size of incremental storage space that is used on the current day. |
| Instances | The number of instances that are included in the backup plans of the organization. |
| Backup Plans | The number of backup plans in the organization. |

### 15.5 View operation logs

This topic describes how to view operation logs in the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console. The operation logs record all operations that are performed to create, delete, and execute backup plans and recovery jobs.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, choose **O&M** > **Logs**.
3. Query logs by user, module, operation level, operation type, start time, or end time. The
following table describes the parameters of the logs.

| Parameter | Description |
|---|---|
| Module | The module of the ASR-BR system. |

| Operation Level | The severity of the log. Valid values: Urgent, Alert, Error, Warning, and Message. |
|---|---|
| Operation Type | The types of operations that are recorded in the log. |

### 15.6 Configure parameters

When you create a MaxCompute backup plan in the ASR for Backup and Recovery console whose version is earlier than 3.14, you must also create a project. In the ASR for Backup and Recovery console V3.14 or later, the operations administrator can configure the project to run MaxCompute backups. This simplifies configuration and facilitates centralized management.

**Background information**

To configure a project for backup plans, you must have the permissions of operations administrators. If you do not configure a project, the current backup instance is used as the project. The **Parameter Configuration Module** is only supported for MaxCompute instances. Quotas serve as a computing resource pool of MaxCompute. They provide the CPU and memory resources that are required for computing jobs, such as MaxCompute SQL jobs, MapReduce jobs, Spark jobs, Mars jobs, and Machine Learning Platform for AI (PAI) jobs.

**Prerequisites**

The MaxCompute client installation package (GitHub) is installed. If no installation package is available, contact the backup R&D team. A MaxCompute V2.0 instance is created and the following data type parameters of the project for backup plans are configured: setproject odps.sql.type.system.odps2=true; : enables MaxCompute V2.0 data types. setproject odps.sql.decimal.odps2=true; : enables the DECIMAL type in MaxCompute V2.0. setproject odps.sql.hive.compatible=false; : disables Hive-compatible data types.

**Procedure**

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **O&M** > **Parameter Configuration.**
3. Select a **MaxCompute instance** from the drop-down list and click **Add**.

> **Note:** Fuzzy search is supported when you enter the MaxCompute instance name. If the MaxCompute instance cannot be added because MaxCompute V2.0 data types are not used, perform the following steps to modify the instance data type.

4. (Optional) Modify the version of MaxCompute data types.
i. Configure the MaxCompute client. a. After you install the MaxCompute client installation package, the **bin**, **conf**, **lib**, and
**plugins** folders are created.
b. Open the **conf** folder and configure the **odps_config.ini**file. In the **odps_config.ini** file, lines that start with a number sign (#) are comments. The following table describes the required parameters.

| Parameter | Description | How to obtain |
|---|---|---|
| project name _ | The name of the MaxCompute project that you want to access. | a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, click Products. c. In the left-side navigation pane, click Big Data Computing. d. In the Big Data Computing section, choose Data Computing and Analytics > MaxCompute. e. In the left-side navigation pane, click Projects. On the Projects page, select the MaxCompute instance that you want to occupy a CU quota. |
| access id _ | The AccessKey ID of the MaxCompute instance. | a. Log on to the Apsara Uni-manager Management Console. b. In the top navigation bar, click Enterprise > Resources > Organizations. c. Enter the name of your organization in the search box and click Management Accesskey to obtain the AccessKey pair. |
| access key _ | The AccessKey secret of the MaxCompute instance. |   |

| end point _ | The endpoint of MaxCompute. | a. Log on to the Apsara Uni-manager Operations Console. b. In the top navigation bar, choose Platform > Apsara Infrastructure Management > Resources. c. In the left-side navigation pane of Apsara Infrastructure Management, choose O&M Tools > Service Registration Variable Dashboard. d. Select Service from the drop-down list, enter the odps-service-frontend in the search box, and then click . e. Click in the Service Registration column, and then click the value to display the result in a separate page. Find the odps frontend server.endpoint value _ _ and record it. f. The end point value is in the format of _ http://The value recorded in the preceding st ep/api. Example: http://service.cn-qingdao- xxx-d01.odps.intra.xxx.shuguang.com/api. |
|---|---|---|

ii. Modify the data types of the MaxCompute instance. a. Log on to the project for the MaxCompute instance. b. Run the following commands to modify the data types: a. setproject odps.sql.type.system.odps2=true; : enables MaxCompute V2.0 data types. b. setproject odps.sql.decimal.odps2=true; : enables the DECIMAL type in MaxCompute V2.0. c. setproject odps.sql.hive.compatible=false; : disables Hive-compatible data types. c. If OK is returned, your modification is successful. iii. Run the following command to check whether your modification takes effect:

```
 setproject;
```

a. The modified values are displayed. If the displayed values are consistent with the values that you specify, your modification takes effect.

> **Note:** The preceding figure shows the sample result of the command. Check whether your modification takes effect.

5. On the **Parameters** page of the **ASR for Backup and Recovery** console, select a
MaxCompute instance again and click **Add**.

### 15.7 Event management

You can use the event management feature to view all event records.

**Background**

Organization administrators can manage and view the events that they initiated. Operations administrator can manage and view all events in the system.

**Procedure**

1. Log on to the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console.
2. In the left-side navigation pane, choose **O&M Management** > **Events**.
3. You can configure the **Event Type**, **Event Status**, **Start Time**, or **End Time** search
conditions to search for specific events.
4. Find the event whose log you want to view and click **Log** in the **Actions** column.
5. Click the
icon to the left of an event to view sub-events and their statuses.
6. Click the
icon to the right of a sub-event to view the sub-event log.

**Successful**

**Canceled**

This status is displayed when a sub-event is canceled.
**Failed**, **Timed Out**, and **Stopped**
If a sub-event is in one of the preceding states, you can click the icon next to the subevent to retry the sub-event.

> **Important:** This operation is an event O&M operation. If the most recent event is successfully executed, do not perform the retry operation for the previous event.

**Waiting for start**, **Execution in progress**, and **Synchronizing**

**g**

**p**

**g**

**y**

**g**

If a sub-event is in one of the preceding states, you can click the icon to the right of the sub-event to cancel it. If you cancel the sub-event, its status changes to **Canceled**.

> **Important:** This operation is an event O&M operation. This operation is irreversible. Proceed with caution.

ackup

## 16 Best practices of data backup

**backup**

### 16.1 Database services

#### 16.1.1 ApsaraDB RDS backups

This topic describes the backup policies and speed of ApsaraDB RDS.

**Backup policy configuration**

**Backup policies**

ApsaraDB RDS supports the following types of backup policies: The full backup mode allows you to recover data only to the points in time when a backup is created. You can select a mode based on your business requirements. The full backup plus log backup mode allows you to recover data to a specific point in time.

> **Note:** We recommend that you select the full backup plus log backup mode for ApsaraDB RDS and specify two days a week to execute a full backup. This helps you save bandwidth and storage capacity and ensure utmost data security.

**Backup time**

If you want to back up multiple ApsaraDB RDS instances, we recommend that you do not specify the backup time of all ApsaraDB RDS instances to the same day.

> **Note:** You can perform 5 to 6 backup tasks at the same time to maximize bandwidth utilization.

We recommend that you back up your ApsaraDB RDS instance during off-peak hours.

> **Note:** ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances are backed up from secondary databases. ApsaraDB RDS for SQL Server instances are backed up from primary databases.

If you want to perform a backup on the current day, set the start time of the backup task to at least 10 minutes later than the current time.

**Data retention time**

If both local backup and cross-region backup are configured for ApsaraDB RDS, we recommend that you set the local backup retention period to 7 days and the remote retention period to more than 30 days. You can specify the remote retention period based on the importance of your business data.

**Backup speed**

ackup A cross-region backup of an ApsaraDB RDS instance is performed based on the following steps:
1. Perform an intra-region backup and upload the backup files to the OSS bucket in the same
region as the ApsaraDB RDS instance. The maximum speed of a single backup task is 55 MBit/s.
2. Perform a cross-region backup and copy the backup files from the OSS bucket in the same
region as the ApsaraDB RDS instance to an OSS bucket in another region. The following section describes the speed at which data is replicated across regions. If you do not configure Maximum Traffic Threshold in the Apsara Stack Resilience for Backup and Recovery (ASR-BR) console, the upload speed for a single upload task is 40 Mbit/s. If you set Maximum Traffic Threshold to a value greater than or equal to 400 MBit/s, the upload speed of a single task is 40 Mbit/s. If you set Maximum Traffic Threshold to a value less than 400 MBit/s, the upload speed of a single task is the result of dividing the specified speed by 10.

**Throttling scenarios**

The following scenarios require throttling: You want to back up large amounts of data for ApsaraDB RDS instances, OSS buckets, and Apsara File Storage NAS file systems. If more than six backup tasks are performed at the same time, you must limit the bandwidth that can be allocated to backup tasks.

#### 16.1.2 PolarDB-X 1.0 backups

This topic describes the backup policies and speed of PolarDB for Xcale (PolarDB-X) 1.0.

**Backup policy configuration**

**Backup policies**

PolarDB-X 1.0 supports the following backup modes: Fast Backup and Consistent Backup. Fast Backup: This mode ensures data consistency only in a single database. Consistent Backup: In this mode, the system locks distributed transactions within seconds, which may cause sub-second response time. Therefore, we recommend that you perform this operation during off-peak hours. The Consistent Backup mode only supports backup from data sets.

> **Note:** The Fast Backup mode is suitable for regular backup and restoration. The Consistent Backup mode is suitable for core online transaction scenarios and other scenarios that have high requirements for data consistency.

**Backup time**

For data security purposes, we recommend that you back up your data at least twice a week to ensure that you have recoverable data sets.

> **Note:** If you want to perform a backup on the current day, set the start time of the backup task at least 10 minutes later than the current time.

ackup

**Data retention time**

We recommend that you set the local backup retention period to 7 days. You can specify the remote retention period based on the importance of your business data. We recommend that you set the remote retention period to more than 30 days.

**Backup speed**

For more information, see the "Backup speed" section of the ApsaraDB RDS backups topic.

**Throttling scenarios**

For more information, see the "Throttling scenarios" section of the ApsaraDB RDS backups topic.

### 16.2 File storage services

#### 16.2.1 OSS backups

This topic describes the backup speed and throttling scenarios of Object Storage Service (OSS).

**Backup speed and configuration**

The performance of an OSS backup task depends on the file size and the number of allowed concurrent tasks. The following table describes the recommended number of concurrent tasks for different file sizes:

| Average file size | Concurrency configuration | Backup speed |
|---|---|---|
| < 64 KB | 128 reads and 256 writes | < 110 MB |
| 64 KB‒128 KB | 128 reads and 128 writes | 100 MB‒350 MB |
| 128 KB‒256 KB | 64 reads and 128 writes | 150 MB‒350 MB |
| 256 KB‒512 KB | 64 reads and 64 writes | 200 MB‒450 MB |
| 512 KB‒2 MB | 32 reads and 32 writes | 300 MB‒400 MB |
| > 2 MB | 8 reads and 32 writes (Default) | > 100 MB |

The backup cycle is estimated based on the backup speed. If you want to back up a large number of OSS objects, you can split an instance into multiple backup plans by specifying the prefix and creation time of the OSS objects in the instance. This helps improve the backup scanning efficiency. For OSS instances, only the first backup is a full backup. The subsequent backups are incremental backups that are performed through deduplication. ackup For Cloud Defined Storage - Object Storage Service (CDS-OSS) instances, the inventory feature can be used to improve the efficiency of incremental backups. If you want to back up a bucket that has more than 100 million objects, we recommend that you enable the inventory feature.

**Throttling scenarios**

Independent streams must be established for backup tasks to prevent interruptions to your business. OSS backups are subject to the upper limit (5 GB) of traffic routed by Server Load Balancer (SLB). Therefore, we recommend that you perform the following operations: For Apsara Stack V3.16 and later, when you back up OSS buckets, you can create an independent virtual IP address (VIP) for OSS buckets and specify the VIP for the Endpoint parameter when you create a backup plan. This ensures that your business is not affected by backups. The throttling policy for backups can be specified based on the actual bandwidth.

#### 16.2.2 NAS backups

This topic describes the backup speed and throttling scenarios of Apsara File Storage NAS.

**Backup speed**

Only the Network File System (NFS) protocol is supported for backups of Apsara File Storage NAS file systems. We recommend that you create up to 8 million files and subdirectories in a directory for each Apsara File Storage NAS backup task. The backup speed of Apsara File Storage NAS depends on the file size. The backup cycle must be configured based on the actual data volume and backup speed. The following table describes the backup speeds of different file sizes:

| File size | Average processing speed | Backup data volume per day (24 hours) |
|---|---|---|
| 32 KB | 13 MB/s | 1 TB |
| 64 KB | 21 MB/s | 1.73 TB |
| 256 KB | 53 MB/s | 4.36 TB |
| 512 KB | 82 MB/s | 6.75 TB |
| 1 MB | 138 MB/s | 11.37 TB |

**Throttling scenarios**

The throttling policy for backups can be specified based on the actual bandwidth.

#### 16.2.3 ECS file backups

This topic describes the backup speed of Elastic Compute Service (ECS) file backups.

**Backup speed**

ackup The backup speed varies based on the type of disk. Premium performance disks and ultra disks have similar backup speeds, while standard performance disks and standard SSDs have similar backup speeds. The backup speed of premium performance disks and ultra disks are higher than that of standard performance disks and standard SSDs. ECS resources are occupied during file backup. The following table shows the backup speed and resource usage.

| Average file size | Transmission speed | CPU usage | CPU usage after the speed is throttled to 10 MB |
|---|---|---|---|
| 32 KB | 19 MBit/s | 100%–240% | 40%–70% |
| 64 KB | 27 MBit/s | 200%–240% | 32%–60% |
| 256 KB | 92 MBit/s | 160%–240% | 16%–40% |
| >=512 KB | 120 MBit/s | 160%/240% | 16%–28% |

When you create an ECS backup plan:
1. If no throttling policies are specified, make sure that the specifications of an ECS instance
are at least 4 cores and 4G memory. If an ECS instance has less than 4 cores, the backup speed of ECS files must be limited to 10 MB/s.
2. The backup memory usage must be limited to 1–2 GB to ensure that the ECS instance has
at least 1 GB of idle memory.

#### 16.2.4 ECS instance backups

This topic describes the remote dump speed of Elastic Compute Service (ECS) instance backups.

**Remote dump speed**

To back up an ECS instance, Elastic Block Storage (EBS) is used to create a snapshot of the ECS instance and store the snapshot to an Object Storage Service (OSS) bucket in the same region. Then, the snapshot is cloned to a cross-region storage. The snapshot backup speed of an EBS 1.0 disk is 13 MBit/s, and the snapshot backup speed of a disk in a Cloud Defined Storage - Elastic Block Storage (CDS-EBS) cluster is 32 MBit/s. The remote dump speed is 90 MBit/s. When you configure a backup policy, the backup policy is estimated based on the actual backup data volume.

### 16.3 Analytics computing services

#### 16.3.1 MaxCompute backups

This topic describes the backup practices of MaxCompute. When the data of a MaxCompute instance is backed up, the data is split into multiple 256 MB shards. Each shard is uploaded to a backup vault as a task and each task is executed on a compute node. ackup Each task occupies 0.7 quotas of MaxCompute, and the upload speed is 2–3 MBit/s. On average, the upload speed of each quota is 3.6 MBit/s. If the number of concurrent tasks exceeds the quotas of MaxCompute, the tasks are queued for execution. For example, if two physical machines are used for data backup, the maximum throughput of MaxCompute backup is approximately 300 MBit/s. More physical machines indicate higher throughput.

### 16.4 Best practices for hybrid cloud backup

**cloud backup**

#### 16.4.1 Preparations

You can use Apsara Stack Resilience for Backup and Recovery (ASR-BR) to back up data from Apsara Stack to Object Storage Service (OSS) on Alibaba Cloud public cloud.

**Prerequisites**

An Alibaba Cloud public cloud account is created. A virtual private cloud (VPC) on Alibaba Cloud public cloud is created. An Express Connect circuit on Alibaba Cloud public cloud is created. Object Storage Service (OSS) on Alibaba Cloud public cloud is activated. Apsara Stack DNS is activated. Redirection for endpoints of OSS on Alibaba Cloud public cloud is enabled in Apsara Stack OpsDNS.

**Network connection**

**Configure resolution for public endpoints**

When the system backs up data from Apsara Stack to the public cloud, ASR-BR, which is deployed in the classic network, calls OSS API operations through the endpoint of public cloud OSS to write the data to OSS. Therefore, resolution for public endpoints needs to be enabled on OpsDNS.

> **Note:** By default, this feature is not enabled on OpsDNS. You need to contact technical support, who will evaluate the security risks and determine whether to enable this feature on your cloud system.

**Border protection for Apsara Stack**

ASR-BR is deployed in the classic network. To ensure security, you need to deploy firewalls outside the border of your Apsara Stack system and configure SNAT rules. For more information, see Network limits. In addition to the class network endpoints, you also need to configure OpsDNS so that your Apsara Stack system can access Alibaba Cloud public cloud services.

**Connect the Apsara Stack system and the public cloud**

ackup
1. Create a virtual border router (VBR) on the public cloud, so that the Apsara Stack system
can be connected to the public cloud VPC.
2. Activate OSS and Alibaba Cloud DNS PrivateZone in the public cloud VPC, so that API
operations can be called.
3. Use an Express Connect circuit to connect the Apsara Stack system and the VBR, and
deploy a firewall to protect the Apsara Stack system.
4. ASR-BR is deployed in the Apsara Stack system. OpsDNS is used to resolve the OSS
endpoint, and the backup data is written to OSS in the public cloud through the Express Connect circuit.

**Note**

For more information, see the "Operations on Alibaba Cloud public cloud" section of the Hybrid cloud network connections with Express Connect circuits topic.

#### 16.4.2 Hybrid cloud network connections with Express Connect circuits

**with Express Connect circuits**

This topic describes how to connect Apsara Uni-manager to Alibaba Cloud public cloud by using Express Connect circuits. After you connect Apsara Uni-manager to Alibaba Cloud public cloud, Apsara Uni-manager can call the API operations of public cloud services.

**Prerequisites**

An Alibaba Cloud account is created. A virtual private cloud (VPC) in Alibaba Cloud public cloud is created. An Express Connect circuit in Alibaba Cloud public cloud is created. Apsara Stack DNS is activated. ackup

**Background information**

After you connect Apsara Uni-manager to Alibaba Cloud public cloud, the following capabilities are available: The Apsara Stack DNS server forwards the domain name of a public cloud service to a private zone in the public cloud VPC for resolution. Apsara Uni-manager accesses the API endpoint in the public cloud VPC tby using Express Connect circuits.

> **Note:** The IP addresses in this topic are provided only for reference. You can specify the IP addresses based on your business requirements.

**Operations in Alibaba Cloud public cloud**

1. Create a dedicated connection over an Express Connect circuit. For more information, see
Create and manage a dedicated connection over an Express Connect circuit.
2. Create a virtual border router (VBR). For more information, seeCreate and manage a
dedicated connection over an Express Connect circuit.
3. Create a Border Gateway Protocol (BGP) peer and enter the IP address of the BGP peer in
Apsara Stack. For more information, see Configure and manage BGP.
4. Create a Cloud Enterprise Network (CEN) instance and configure PrivateZone for the
instance. For more information, see Configure PrivateZone.
5. Log on to the Alibaba Cloud DNS console and add the private zone that you configured in
the previous step. For more information, seeCreate a private zone and add a DNS record to the private zone..

**Note**

The value in the **Records** column is the number of DNS records of the corresponding private zone. Click the name of the private zone that you want to manage. The Resolution Settings page appears, on which you can create a DNS record for the private zone. ackup
6. In the Alibaba Cloud DNS console, associate the private zone for which you configured a
VPC. For more information, see Associate or disassociate a VPC.
7. Call API operations over the internal network
After all configurations are complete, you can call the API operations of public cloud services in Apsara Uni-manager.

**Operations on Apsara Stack**

1. Configure the routing mode of Apsara Stack Inter-connection Switch (ISW).
Static routing Run the following command on ISW:

```
ip route-static [$IP] [$IP_Prefix] [$GW_IP] preference 10 ------ Route the traffic from the CIDR blocks of the public cloud service and private zone to the public clo ud endpoint.
```

**Note**

[$IP]: the CIDR blocks of the public cloud service and private zone. [$IP_Prefix]: the subnet mask of the destination CIDR blocks. [$GW_IP]: the IP address of the public cloud endpoint. BGP routing If ISW communicates with Alibaba Cloud public cloud by using BGP, you must configure the routing of the hybrid cloud management platform address segment on the private cloud side and the routing of the cloud service and private zone address segment on the public cloud side.
2. Configure Apsara Stack DNS.
i. Log on to the Domains console. ii. In the left-side navigation pane, click**Internal Domain Names**. iii. Click**Forwarding Settings**. iv. Click**Add Domain Name**and configure the following parameters.

| Parameter | Description |
|---|---|
| Global Forwarding Domain Name | Enter the endpoint of the API operation of the public cloud service. The endpoint is the same as the endpoint that is configured for the private zone. |
| Forwarding Mode | Select a forwarding mode. |
| Destination IP Address | Enter the IP address of the DNS server used by PrivateZone. |

#### 16.4.3 Create a storage pool

ackup This topic describes how to create a storage pool whose storage location is in Alibaba Cloud public cloud.

**Prerequisites**

The network connection is established. For more information, see Preparations. Object Storage Service (OSS) on Alibaba Cloud public cloud is activated, and the account has the following permissions:

```
oss:PutBucket oss:ListObjects oss:GetBucketAcl oss:GetBucketInfo oss:GetBucketLifecycle oss:PutBucketLifecycle oss:DeleteBucketLifecycle oss:ListMultipartUploads oss:PutObject oss:GetObject oss:DeleteObject oss:ListParts oss:RestoreObject oss:AbortMultipartUpload
```

Only backup operations administrators can create storage pools.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. Click **Create Storage Pool Group**. In the **Add Storage Pool Group** dialog box, configure
the parameters and click **OK**.

> **Note:** A maximum of 16 storage pool groups can be created.

ackup

| Parameter | Description |   |   |   |
|---|---|---|---|---|
| Storage Pool Group Name | Enter a descriptive name for the storage pool group, such as "Public Cloud Storage Pool Group". Note The name can contain letters, digits, hyphens (-), and underscores ( ). It must be less than 64 characters in length. _ |   |   |   |
| Storage Medium | Valid values: OSS, CDS-OSS, MINIOSS, PanguStor, and SDS. |   |   |   |
| Storage Pool Group Location | The location where the storage pool group resides. Valid values: Local: the current site. Remote: a site in another region. Alibaba Cloud Public Cloud: Alibaba Cloud public cloud. |   |   |   |
| endpoint | The domain name or IP address of the storage medium. Note The endpoint must be accessible. IPv6 addresses are not supported. If a NAT gateway is used and port mapping needs to be added, specify the parameter in the following format: <Endpoint>: <Port> . |   |   |   |
|   |   | <Endpoint>: |   |   |

|   |   | <Port> |
|---|---|---|

ackup

| Bucket (optional) | The storage capacity of the storage pool group. Unit: TB. Note The sum of the storage capacity of all storage pools in the group must be smaller than this value. Otherwise, storage pools fail to be created. If you leave this parameter empty, the storage capacity is unlimited. |
|---|---|

4. In the storage pool group list, click the name of the storage pool group.
5. On the page that appears, click **Create Storage Pool**. In the **Add Storage Pool** dialog
box, configure the parameters.

| Parameter | Description |
|---|---|
| Storage Pool Name | Enter a descriptive name for the storage pool group, such as "Public Cloud Storage Pool". Note The name can contain letters, digits, hyphens (-), and underscores ( ). It must be less than 64 characters in length. _ |
| Storage Capacity | The storage capacity of the storage pool. Unit: TB. |

ackup

| AccessKey ID | The AccessKey ID of the account that accesses the destination storage. Note The AccessKey ID and AccessKey secret must have the permissions to read and write data. |
|---|---|
| AccessKey Secret | The AccessKey secret of the account that accesses the destination storage. |
| Authorized Organization | Select the level-1 organizations. You can select all level-1 organizations. |
| Recycle Bin | Optional. Specify the name of the recycle bin. This parameter is required if you need to create a deduplication backup vault or a mirror vault in the storage pool. Note When you create a deduplication backup or mirror vault, an existing bucket of the recycle bin is used if any. If no bucket exists, a relevant bucket is created. |
| Storage Pool Description (optional) | The description of the storage pool for easy identification. |

6. Then, click **OK**.

#### 16.4.4 Create a backup vault

This topic describes how to create a backup vault whose storage location is in Alibaba Cloud public cloud.

**Prerequisites**

A storage pool is created. For more information, see Create a storage pool. The backup administrator or operator creating a backup vault must belong to a level-1 organization authorized by the storage pool. Otherwise, the storage pool cannot be viewed.

**Background information**

Only one backup vault of the database class can be created for each storage pool and cannot be modified after it is created. You can create multiple storage backup vaults and deduplicating backup vaults in a storage pool. ApsaraDB RDS and PolarDB for Xscale (PolarDB-X) 1.0 use the same database backup vault. Organization backup administrators and organization backup operators can create database backup vaults, storage backup vaults, and deduplicating backup vaults.

**Procedure**

ackup
1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Vaults**.
3. On the **Backup Vaults** page, click **Create**.
4. In the **Create Backup Vault** dialog box, set the following parameters.

| Parameter | Description |
|---|---|

ackup

| Vault Name | Specify the name of the backup vault. Example: public cloud backup vault. Note We recommend that you specify an informative name. After a backup vault is created, you cannot change its name. The name can only contain lowercase letters, digits, and hyphens (-). The name cannot start with a hyphen (-). The name must be 3 to 35 characters in length. |
|---|---|
| Description (optional) | Specify the description of the backup vault. |
| Backup Service Type | The type of the service whose data will be backed up in this vault. Database: ApsaraDB RDS, PolarDB, and PolarDB-X 1.0 are supported. Storage: OSS, ECS, and NAS are supported. Tablestore: Tablestore backup is supported. Data Deduplication: Only MaxCompute is supported. |
| Enable HTTPS | Specify whether to use the HTTP or HTTPS protocol to create the backup vault and back up data to the backup vault. By default, HTTPS is enabled. You can manually disable HTTPS. Note This parameter is required only when you set the Backup Service Type parameter to Database, Storage Class, or Tablestore. If the HTTPS port of OSS is not reachable, we recommend that you turn off Enable HTTPS. |
| Storage Location | The location where the backup data is stored. Valid values: Local: The backup data is stored in the OSS buckets of the current region. Remote: The backup data is stored in the OSS buckets across regions. Alibaba Cloud Public Cloud: The backup data is stored in the OSS buckets on Alibaba Cloud public cloud. Note If you set the Backup Service Type to Tablestore, you must set the Storage Location parameter to Remote. |
| Storage Pool | The storage pool to which the backup vault belongs. |

ackup

| Bucket Name | If you specify a bucket, the bucket is used as the backup vault. The bucket name must be an existing bucket name in OSS. Note If you do not have permissions to create buckets in the selected storage pool, you must specify this parameter. |
|---|---|
| Storage Capacity | The storage size of the backup vault. Unit: GB. Note The storage size of the backup vault cannot exceed that of the storage pool that it belongs to. |

5. Then, click **OK**.

> **Note:** If the backup vault fails to be created, the storage resources may be insufficient. Expand the storage repository in a timely manner before creating it again.

**Execution result**

ASR for Backup and Recovery automatically creates an OSS bucket in the selected storage pool. Then, the OSS bucket is used to back up your business data.

#### 16.4.5 Create a backup plan

This topic describes how to create a backup plan. After you create a backup plan, ASR for Backup and Recovery regularly backs up data from the specified instance to the backup vault.

**Prerequisites**

You are an organization backup administrator or organization backup operator. Only organization backup administrators and organization backup operators can create backup plans. Backup operations administrators cannot create backup plans. A backup vault is created. For more information, see Create a backup vault. If you want to back up and restore data for MaxCompute instances, the external table feature of MaxCompute is enabled and the MaxCompute Enhancement Pack for Joint Computing (Spark on MaxCompute) is deployed. The Cloud Assistant is installed on the Elastic Compute Service (ECS) instance for which you want to create a backup plan and the Cloud Assistant runs as expected. (Optional) If you want to create a backup plan for a MaxCompute instance, first specify compute units (CUs) dedicated for the backup operations of the instance to ensure that the backup operations does not interfere with ongoing business operations. For more information, see Configure parameters.If you do not specify CUs for the backup operations of the instance, the CUs of the current project are used. A message indicating that no project is running appears when you configure the instance.

**Background information**

ackup ASR for Backup and Recovery allows you to back up ApsaraDB RDS data and metadata such as user information, permissions, and specifications. ASR for Backup and Recovery allows you to back up Apsara File Storage NAS file systems that use the Network File System (NFS) protocol or Server Message Block (SMB) protocol. ASR for Backup and Recovery allows you to back up the metadata of MaxCompute tables, functions, resources, and projects. The metadata includes quota information, cluster information, virtual private cloud (VPC) information, and security information. ASR for Backup and Recovery allows you to backup data of the following AnalyticDB database types: C8, H20, C20, and B7. ASR for Backup and Recovery allows you to back up Tablestore tables whose names do not exceed 100 characters. If you want to back up Tablestore tables whose names exceed 100 characters, contact the ASR for Backup and Recovery R&D team.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, click **Create**.
4. In the **Basic Information** step, configure the parameters and click **Next**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Backup Plan Name | The name of the backup plan. Note The name must be 4 to 128 characters in length and can contain only letters, digits, hyphens (-), underscores ( ), and _ periods (.). |
| Description (optional) | The description of the backup plan. We recommend that you enter a description that can help you identify the backup plan. |
| Instance Type | The type of the instance that you want to back up. Note If you want to create a Tablestore backup plan, set the Instance Type to Tablestore. |
| Backup Method | The backup method of the instance. This parameter is available only when you set the Instance Type parameter to Elastic Compute Service. Valid values: Snapshot Backup: backs up an ECS instance or the specified disks of an ECS instance. File Backup: backs up ECS files. |

5. In the **Select Instance** step, select the instance that you want to back up and click **Next**.
ackup

> **Note:** Only instances in the **In Use** state can be backed up.
> A backup plan is created for only a single instance.
> You can create only one backup plan for an ApsaraDB RDS, PolarDB, PolarDB-X, or AnalyticDB instance. You cannot create a backup plan for an instance that is in **protected** state.
> An Object Storage Service (OSS) bucket can be added to multiple backup plans simultaneously.
> An Apsara File Storage NAS file system can be added to multiple backup plans simultaneously.
> An ECS instance can be added to a backup plan that uses the Cloud Disk Backup method and a backup plan that uses the File Backup method simultaneously.
> An ECS instance that uses the File Backup method can be added to multiple backup plans simultaneously.
> A Tablestore instance contains multiple tables. If you select the Tablestore instance type, you can view the tables of the instance in the **Tablestore Table** column.

6. (Optional) Select Tablestore tables. This step is required only if you set the **Instance Type**
parameter to **Tablestore** at the **Basic Information** step. i. In the left-side section, select the names of the tables that you want to back up.

> **Note:** You can select only two tables for a Tablestore instance at a time. If you select one or two Tablestore tables, the data of the tables are backed up at the same time. If you select three or more Tablestore tables, the additional tables have to wait in a queue until the system is free to back up them.

ii. Click to add the selected Tablestore tables to the right-side section. iii. Click **Next**.
7. (Optional) In the **Install Client** step, configure the parameters for installing the Hybrid
Backup Recovery (HBR) client, and then click **Next**.

> **Note:** This step is applicable only to ECS instances that use the **File Backup** method.
> The ECS Cloud Assistant is used when installing the HBR client. Make sure that the ECS Cloud Assistant is installed on the ECS instance and is in the normal state.

| Instance type | Parameter | Description |
|---|---|---|

ackup

| ECS (file backup) | Client Installation Path (optional) | The directory where the HBR client is installed on the ECS instance. Note If you leave this parameter empty, the HBR client is installed in the /root directory. |
|---|---|---|
|   | Number of CPU Cores on Client | The maximum number of CPU cores that can be used by the HBR client. The system automatically displays the number of CPU cores of the current ECS instance. When the HBR client starts a backup task, the backup task is allocated based on the value you specified for this parameter. Note A larger number of CPU cores indicates that the HBR client uses more resources on the host and has a larger negative impact on the performance of the host. We recommend that you specify a suitable value based on your business requirements. |
|   | Max. Number of Worker Threads on Client | The maximum number of threads that can be used by the HBR client. Default value: 10. When the HBR client starts a backup task, the backup task is allocated based on the value you specified for this parameter. Note A larger number of threads indicates that the HBR client uses more resources on the host and has more negative impacts on the performance of the host. We recommend that you specify a suitable value based on your business requirements. |

ackup

|   | Client Installation Status (optional) | After you specify Number of CPU Cores on Client and Max. Number of Worker Threads on Client , click Install to install the HBR client. You can click Refresh to refresh the installation status. After the installation status changes to The client is installed., you can perform the next step. The system automatically performs a connectivity test. Note After the HBR client is installed, you can modify the values of Number of CPU Cores on Client and Max. Number of Worker Threads on Client. You can also uninstall the client when it is no longer needed. The right-side section of the Install Client page displays the installation information of the HBR client, including the client installation status, client version number, heartbeat keep-alive time, and the maximum number of CPU cores and threads used by the HBR client. If keepalive does not time out, you can uninstall the client or perform connectivity testing. If keepalive times out, you can uninstall or reinstall the client. If the HBR client has been installed on your ECS instance, the client installation status is "The client is installed." when you create a backup plan for the ECS instance. |
|---|---|---|

8. In the **Configure Instance** step, configure the parameters and click **Next**.

> **Note:** Skip this step if you create a backup plan for an ApsaraDB RDS, PolarDB, Tablestore, or PolarDB-X instance.

| Instance type | Parameter | Description |
|---|---|---|

ackup

|   | OSS Prefix (optional) | Click Browse. On the Browse Directory page, select the directory that you want to back up. The Browse Directory displays the directories of the bucket. You can select the objects that you want to back up from the bucket. Note If you leave this parameter empty, all objects in the bucket are backed up. The value of OSS Prefix are separated by and end with forward slashes (/). The value cannot contain the following characters: angle brackets (<>), backslashes (\), vertical bars (\|), colons (:), quotation marks ("), asterisks (*), and question marks (?). If a bucket contains a large number of objects, we recommend that you create multiple backup plans for the bucket and specify a portion of the objects in the bucket for each backup plan. |
|---|---|---|
|   | Backup File Filtering Policy | The filtering policy of files that you want to back up. Valid values: All: backs up all files that meet the prefix conditions specified in OSS Prefix. By Time Range: backs up objects whose last modification time is within the specified time range. By Last Days: backs up objects that are last modified in the specified last few days. Note The last modification time of an object is the start time of its last backup cycle. |
|   | Time Range for File Filtering | If you set Backup File Filtering Policy to By Time Range, you must specify the start time and end time of the time range. Note Only objects whose last modification time falls within the specified time range are backed up. The time range cannot be left empty. |
|   | Filter Files in Recent Days | If you set Backup File Filtering Policy to By Last Days, you must specify a specific number for Filter Files in Recent Days. |

ackup

| Object Storage Service (OSS) |   |   |
|---|---|---|
|   | Number of Concurrent Backups | The number of concurrent reads and writes. When you create a backup plan for objects in an OSS bucket, you can specify the maximum number of concurrent reads from the source and concurrent writes to the destination. We recommend that you configure the number of concurrent backups based on the number and average size of objects in the bucket. If you set this parameter to Default, the system uses the minimum number of concurrent backups. Note The system automatically recommends the appropriate number of concurrent backups based on the throttling policy and the number and average size of objects in the bucket. |
|   | Inventory function | This parameter is available when you set the Instance Type parameter to CDS-OSS in Step 4. After you enable the inventory feature, ASR for Backup and Recovery creates a Resource Access Management (RAM) role that has the read and write permissions on OSS to configure and generate OSS inventory lists. When you create a backup plan for objects in an OSS bucket, the OSS inventory feature is used to back up data from the OSS bucket. Note After you enable the inventory feature, OSS inventory lists are used to obtain incremental objects in a bucket. You do not need to traverse the objects in the bucket. If your bucket has more than 100 million objects, we recommend that you enable the OSS inventory feature. |
|   | Bucket | This parameter is available only when the inventory feature is enabled. The bucket where OSS inventory lists are stored. |
|   | Inventory Report storage path | This parameter is available only when the inventory feature is enabled. The directory in which OSS inventory lists are generated. If you do not configure this parameter, OSS inventory lists are generated in the root directory. |
|   | Inventory cleanup policy | This parameter is available only when the inventory feature is enabled. The policy that is used to clear OSS inventory lists after each backup. The default policy is to delete all inventory lists after a backup. Note Three policies are supported: delete all inventory lists after backup, delete the current inventory lists after backup, and do not delete inventory lists. |

ackup

|   | OSS Endpoint (optional) | The endpoint that you want to use to read data from the OSS bucket. You can use a custom endpoint to read data from a source OSS bucket. To specify a custom endpoint, select Custom from the OSS Endpoint drop-down list. We recommend that you use a non-business OSS endpoint for backup. Note If you leave this parameter empty, the system uses the default OSS endpoint to read data from a source OSS bucket. The system automatically estimates the required backup traffic based on the throttling policy. Make sure that the backup traffic will not affect the business traffic. If you use a custom endpoint for the backup plan, make sure that the custom endpoint can be used to read data from the source bucket. |
|---|---|---|
|   | Backup Estimation | The estimated backup speed, first full backup time, and subsequent incremental backup time are displayed. |
| ECS (snapshot backup) | Backup Type | Complete Backup: backs up the entire ECS instance. Cloud Disk Backup As Specified: backs up the specified disks of an ECS instance. If you set the Backup Type parameter to Cloud Disk Backup As Specified, click Browse to select one or more cloud disks based on your business requirements. |
|   | Forcibly Create Snapshot- consistent Group | Disabled (default): creates a snapshot-consistent group first. If the snapshot-consistent group fails to be created because the creation conditions are not met or due to or other causes, a standard snapshot is created. Enabled: forcibly creates a snapshot-consistent group. If the snapshot-consistent group fails to be created because the creation conditions are not met or due to or other causes, a standard snapshot is not created and the backup fails. Note Do not enable this feature unless otherwise specified. |
|   | File Path | The path of the files that you want to back up. For more information, see the tooltip in the user interface. |
|   | Objects | Valid values: Include All: backs up all files in the path. Exclude: backs up all files in the path except those specified by the Files parameter. Include: backs up the files specified by the Files parameter. |

ackup

| ECS (file backup) |   |   |
|---|---|---|
|   | Files | The files included in or excluded from the backup plan, depending on the option that is selected for Objects. For more information, see the tooltip in the user interface. |
|   | Traffic Threshold (optional) | An optional parameter for setting traffic throttling for a specified period of time when you back up data from a production center to a backup vault. For more information, see the tooltip in the user interface. You can set different traffic thresholds for peak hours and off- peak hours based on your business requirements. For example, you can set a high traffic threshold for off-peak hours and a low traffic threshold for peak hours to maximize the use of your bandwidth. |
| NAS | File Path | The absolute path of the NAS file to be backed up. The wildcard * is not supported. |
|   | Number of Concurrent Backups | The maximum number of backup processes that can run simultaneously to back up data from the source to the destination. Select the number of concurrent backups based on the number and average size of NAS files. |
| MaxCompute | Source Resource | Specify whether to back up a table or project. Valid values: Table Backup: backs up a single table or multiple tables. Project Backup: backs up all tables, resources, and functions in a project. You can specify the tables, resources, and functions that you want to back up by configuring a whitelist or blacklist. |
|   | Temporary Table Prefix (optional) | The name must be 1 to 128 bytes in length, and can contain letters, digits, and underscores ( ). We recommend that you _ start the name with a letter. |
|   | Backup Gateway | Select the backup gateway from the drop-down list: Default Policy: The system selects a backup gateway of the HBR service to execute the backup plan based on the workloads specified by each customer. Other Backup Gateway: You can also select another registered backup gateway. |

ackup

| VMware Cloud on Alibaba Cloud |   |   |
|---|---|---|
|   | Transmissio n Mode | LAN-fee Backup Data Transmission (default): hot-mounts the disk that you want to back up to the backup gateway and transmits backup data over a non-LAN network. LAN refers to the local area network. LAN-based Backup Data Transmission: transmits backup data over a LAN. Note If the vCenter does not support LAN-free data transmission, the system automatically switches to the LAN mode. |
|   | Snapshot Type | Standard Snapshot: uses VMware software snapshots to perform common backup. System Silent Snapshot (default): uses VMware Tools to perform silent backup. Note If VMware Tools cannot be mounted or is not installed, the system automatically switches to the standard snapshot mode for backups. |

9. In the **Backup Policy** step, configure the backup policy and click **Next**.

> **Note:** The parameters of the backup policy vary based on the instance type. You can configure the parameters based on the on-screen instructions.

The following table describes the backup policy parameters.

| Parameter | Description |
|---|---|

ackup

| Backup Policy | The backup policies vary based on the instance type. Full: All data in the database is backed up based on the specified cycle. If you select this policy, only the data that is backed up at the point in time when the backup is created can be restored. This policy is available only when you set the Instance Type parameter to RDS. Full Data and Logs: All data in the database is backed up based on the specified cycle. In addition, incremental data is backed up during the interval between backup cycles. If you select this policy, the data that is backed up at all points in time can be restored. This policy is available only when you set the Instance Type parameter to ApsaraDB RDS, PolarDB, or PolarDB-X. Incremental: The first backup is a full backup and the subsequent backups are incremental backups. This policy is available only when you set the Instance Type parameter to OSS. If you set Instance Type to OSS, the subsequent backups after the first backup are incremental backups at the object level. Full (Data Deduplication): All data in the database is backed up based on the specified cycle. Data is deduplicated during the backup process. This policy is available only when you set the Instance Type parameter to ECS (file backup) or NAS. Incremental (Deduplication): The first backup is a full backup and the subsequent backups are incremental backups. When an incremental backup is performed, ASR for Backup and Recovery deduplicates data by bucket. This policy is available only when you set the Instance Type parameter to MaxCompute. Full and Incremental: You can perform full backups and incremental backups based on the specified intervals. This policy is available only when you set the Instance Type parameter to ECS (cloud disk backup). |
|---|---|
| Backup Mode | This policy is available only when you set the Instance Type parameter to PolarDB-X. Valid values: Fast Backup: This mode ensures data consistency only in a single ApsaraDB RDS database. We recommend that you select this mode for routine backups. Consistent Backup: This mode ensures data consistency in all databases within a PolarDB-X instance. We recommend that you select this mode for industries that have high requirements for data consistency or for online core transactions. Important We recommend that you perform consistent backups during off-peak hours. The system locks distributed transactions within seconds during a consistent backup. This may cause sub-second response time. |

ackup

| Cycle | Run by Week: This type of cycle is available only if you set the Instance Type parameter to RDS. Run By Day: This type of cycle is available only if you set the Instance Type parameter to OSS, ECS (file backup), NAS, or MaxCompute. |
|---|---|
| Select the Day of the Week | The day of the week when you want to perform a backup. If you want to select multiple days, we recommend that you select the days that are at regular intervals. For example, you can select Monday, Thursday, and Sunday. Note This policy is available only when you set the Instance Type parameter to RDS. For data availability, we recommend that you select at least two days each week. If you set Backup Policy to Full Data and Logs, we recommend that you select a maximum of two days of a week. This consumes less bandwidth and storage space. |
| Interval (Incremental) | The time interval between two backups. This parameter is available only when you set the Instance Type parameter to OSS, NAS, ECS (cloud disk backup), or MaxCompute and set the Backup Policy parameter to Incremental. Note The system automatically estimates the number of days that are required for the first full backup of the OSS instance and recommends a backup interval that is greater than the specified value of this parameter. |
| Time Interval (Incremental) | The time interval between two incremental backups. This parameter is available only when you set the Instance Type parameter to Elasticsearch and the Backup Policy parameter to Full and Incremental. |
| Time Interval (Full) | This parameter is available only when you set the Instance Type parameter to Elasticsearch and the Backup Policy parameter to Full and Incremental. The time interval between two full backups. Set Interval (Full) to a value greater than the value of Interval (Incremental) |
| Interval (Full [Data Deduplication] ) | This parameter is available only when you set the Instance Type parameter to ECS (file backup) and the Backup Policy parameter to Full (Data Deduplication). |

ackup

| Backup Time (Increment) | The time when the backup is performed for the first time. The subsequent incremental backups are performed at the specified intervals. We recommend that you schedule the first backup task to happen at off-peak hours. Note This parameter is available only if you set the Instance Type parameter to OSS, RDS, ECS (file backup), PolarDB-X, or MaxCompute. You must set the Backup Time parameter to at least one hour after the current time. If you set the Backup Time parameter to less than one hour after the current time, the instance may not be backed up on the same day. Instead, it will be backed up during the next backup cycle. |
|---|---|
| Storage Location | The location to which the data is backed up. You cannot select bothR emote and Alibaba Cloud Public Cloud. Valid values: Local: The data is backed up to a backup vault of the production center. Remote: The data is backed up to a backup vault of a remote data center. Alibaba Cloud Public Cloud: The data is backed up to a backup vault of Alibaba Cloud public cloud. |
| Backup Vault (Local) | This parameter is available only if you set the Instance Type parameter to OSS, NAS, MaxCompute, or ECS (file backup). The local backup vault to which you want to back up the data. If you do not find the backup vault that you want to use, click Create Backup Vault to create one. |
| Retention Period (Days) (Local) | The maximum number of days for which backup data is retained in an on- premises backup vault. The default value is 7. You can enter an integer from 7 to 730. Note Expired backup data will be deleted. |
| Backup Vault (Remote) | This parameter is available only when you set the Instance Type parameter to OSS, NAS, MaxCompute, RDS, PolarDB, or ECS (file backup). The backup vault in a remote data center. If you cannot find the backup vault that you want, click Create Backup Vault to create one. |
| Retention Period (Days) (Remote) | The maximum number of days for which backup data is retained in a remote backup vault. The default value is 7. You can enter an integer from 7 to 1460. Note Expired backup data will be deleted. |

ackup

| Backup Vault (Public Cloud) | The backup vault in Alibaba Cloud public cloud to which you want to back up the data. If you cannot find the backup vault that you want, click Create Backup Vault to create one. |
|---|---|
| Retention Period (Days)/Data Backup Retention Period (Days) (Public Cloud) | The maximum number of days for which backup data is retained in a backup vault that is deployed in Alibaba Cloud public cloud. The default value is 7. You can enter an integer from 7 to 1460. Note Expired backup data will be deleted. |
| Enable Log Backup | By default, this parameter is disabled. After you enable this parameter, log data is retained. Note If local log backup is disabled, the remote log backup must be disabled. |
| Log Backup Retention Period (Days) | This parameter is required if you turn on Enable Log Backup. The value of this parameter must be less than or equal to the value of theD ata Backup Retention Period (Days) parameter. |

The following table describes the backup policy parameters for the disks of ECS instances.

| Step | Parameter | Description |
|---|---|---|
| Backup Policy (Local) | Cycle (Full) | You can specify the interval at which the disks of ECS instances are backed up. The interval is measured in days or hours. Valid values: RUN By Day: The disks are backed up at intervals of specified days. By Hour: The disks are backed up at intervals of specified hours. |
|   | Time Interval | The time interval between two backups. If you set the Cycle (Full) parameter to RUN By Day, the interval is measured in days. If you set the Cycle (Full) parameter to By Hour, the interval is measured in hours. |
|   | Backup Time | The time when the backup is performed for the first time. The subsequent incremental backups are performed at the specified intervals. We recommend that you schedule the first backup task to happen at off-peak hours. |

ackup

|   | Retention period (day) | The maximum number of days for which backup data is retained in a local backup vault. For example, if you set this parameter to 7, the backup data of the last 7 days is retained. Backup data that is generated more than 7 days ago is deleted. |
|---|---|---|
|   | Backup Policy | The backup policy for a remote backup vault. Valid values: Incremental: The first backup is a full backup, and subsequent backups are incremental backups. Full and Incremental: You can perform full backups and incremental backups based on the specified intervals. |
| Backup Policy (Remote) |   |   |
|   | Time Interval (Incremental) | The value of this parameter is the same as the value of the Time Interval parameter in the Backup Policy (Local) step. |
|   | Cycle (Full) | This parameter is available only when you set the Backup Policy parameter to Full and Incremental. Only Run by Day is supported. Use the default value. |
|   | Time Interval (Full) | This parameter is available only when you set the Backup Policy parameter to Full and Incremental. You can specify the number of days between full backups. The minimum value is 7. By default, the interval for incremental backups is the same as the value of the Time Interval parameter in the Backup Policy (Local) step |
|   | Backup Time | The system automatically inputs the value. Use the default value. |
|   | Backup Vault (Remote) | The backup vault in a remote data center. If you do not find the backup vault that you want, click Create Backup Vault to create one. |
|   | Retention Period (Days) (Remote) | The maximum number of days for which backup data is retained in a remote backup vault. |

0. Confirm your backup settings and click **Submit**. You can select Start Now based on your
business requirements. If you select **Start Now**, the backup plan is immediately started after it is created. The system backs up the instances that are specified in the plan based on your settings. If you clear **Start Now**, you must manually start the backup plan after it is created. For more information, see Start a backup plan.

## 17 FAQ

### 17.1 How do I delete a storage pool?

**pool?**

A storage pool is a physical cluster that stores backup data. Therefore, you cannot delete a storage pool directly. This topic describes how to delete a storage pool.

**Solution**

Only storage pools that are not associated with backup vaults can be deleted. Therefore, to delete a storage pool, you must first delete the backup plan, then delete the backup vault, and finally delete the storage pool.

> **Important:** After the storage pool is deleted, features related to the storage pool are unavailable. Proceed with caution.

**Procedure**

1. **Delete the backup plan**.
i. Log on to the ASR for Backup and Recovery console as an organization administrator. ii. In the left-side navigation pane, click **Backup Plans**. iii. Enter the name for the backup plan in the Plan Name field, select **Stopped** from the Plan Status drop-down list, and then click **Search**. iv. Click the icon in the **Actions** column and then click **Delete**. v. In the message that appears, click **OK**.
2. **Delete the backup vault**.
i. In the left-side navigation pane, click **Backup Vaults**. ii. Enter the backup vault name in the Vault Name field and click **Search**. iii. Click the icon in the **Actions** column and then click **Delete**. iv. In the message that appears, click **OK**.
3. **Delete the storage pool**.
i. Log on to the ASR for Backup and Recovery console as an operations administrator. ii. In the left-side navigation pane, choose **System Management > Storage Pool**
**Groups**.
iii. Enter the name of the storage pool group to which the storage pool belongs in the Storage Pool Group Name field and click **Search**. iv. Click the name of the storage pool group in the **Storage Pool Group** column to go to the
**Storage Pool Management** page.
v. Find the storage pool, click in the Actions column, and then click **Delete**. vi. In the message that appears, click **OK**.

> **Note:** To delete a storage pool group, make sure that all storage pools in the group have been deleted.

### 17.2 How do I view ECS snapshot sizes?

**sizes?**

This topic describes how to view the sizes of ECS snapshots to help you plan the sizes of OSS buckets.

**Procedure**

1. Log on to the ASR for Backup and Recovery console.
2. In the left-side navigation pane, click **Backup Plans**.
3. On the **Backup Plans** page, click the name of the backup plan for an ECS instance to go to
the backup plan details page appears.
4. Click the **Backup Records** tab. The backup records of all instances in the backup plan are
displayed.
5. Click
to view the following information of the backup record: **Backup Set Size**, **Disk**
**Backup Status**, **Data Backup Type**, and **Storage Location**.

### 17.3 What do I do if an error is returned when I log on to the ASR for Backup and Recovery console as a common user?

**returned when I log on to the ASR**

**for Backup and Recovery console**

**as a common user?**

This topic describes how to bind a role to a common user after you create a common user to obtain the permissions of the role.

**Problem description**

An error is returned indicating that I am not authorized to do so when I log on to the ASR for Backup and Recovery console as a common user.

**Cause**

A common user does not have the permissions to log on to the ASR for Backup and Recovery console or view the pages. For more information about roles and corresponding permissions, see Roles and permissions.

**Solution**

1. Log on to the Apsara Uni-manager Management Console as an operations administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Users > Users**.
4. Select the organization to which the common user belongs from the drop-down list, enter
the name of the common user in the search box, and then click .
5. Find the common user, click
in the **Actions** column, and select **Authorize**.
6. Select a role for the common user and grant the corresponding permissions to the common
user. For more information, see Roles and Permissions.

> **Note:** You can select multiple roles for the common user.

7. Click **OK**.

**Verification**

1. Log on to the ASR for Backup and Recovery console as the common user that has been
granted proper permissions.
2. Check whether you can log on to the console.
You can log on to the console, but no data is displayed on pages. Switch to the organization to which the common user belongs and then check whether data is displayed on pages. If no data is displayed, check whether any data is generated. If an error is displayed when you log on to the console, contact the backup R&D team for troubleshooting.

### 17.4 What do I do if an AccessKey pair error or an AccessDenied error is returned when I create a storage pool?

**pair error or an AccessDenied**

**error is returned when I create a**

**storage pool?**

This topic describes how to troubleshoot errors when you create a storage pool

**Problem description**

I cannot create a storage pool after I log on the console as an Operations administrator with the root role bound. An AccessKey pair error or an AccessDenied error is returned.

**Cause**

The **************** or ******************** entered when you create the storage pool is incorrect. You must enter the **************** and ******************** of the destination storage and have the permissions to read and write the storage. Therefore, you must first obtain the correct AccessKey ID and AccessKey secret of the destination storage (OSS, CDS-OSS, MINIOSS, PanguStor, or SDS).

**Solution**

**Note**

Because ASR for Backup and Recovery supports the backup storage using the OSS protocol, you can use ossutil to verify whether the AccessKey ID and AccessKey secret have the permissions to read and write OSS.
1. Download and install ossutil. For more information, see Install ossutil.
2. Upload ossutil to the asrbr-backup docker in the StandardAsrbrCluster的asrbr-
backup.Backup# VM.
3. Run the following command to modify the permissions:
chmod +x ossutil
4. Run the following command to configure the ossutil connection destination and verify the
network connectivity: ./ossutil config Specify the OSS endpoint, AccessKey ID, and AccessKey secret for the ossutil connection. (You can upload ossutil to the asrbr-backup docker to verify the network connectivity from the ASR for Backup and Recovery console to the destination storage.)
5. Use ossutil to run the following command to determine the permissions:

```
./ossutil64 ls [-s] [--limited-num] [--marker]
```

| Parameter | Description |
|---|---|
| -s | Specifies that only bucket names are listed. |
| --limited-num | Specifies the maximum number of buckets to list. You can specify this parameter together with the marker parameter to display returned results by page. |
| --marker | Specifies the position from which the list operation starts. Buckets whose names are alphabetically after the value of marker are listed. |

If no error is returned, the AccessKey ID and AccessKey secret meet the permission requirements and can be used normally. If an error is returned, the AccessKey ID and AccessKey secret do not have the permission to access OSS. Select an appropriate AccessKey pair and perform the preceding steps to verify the permissions. Ensure that no error is returned before you can enter the AccessKey pair for creating a storage pool.

**Verification**

> **Note:** The following steps require the precondition that a storage pool group is created. If not, create a storage pool group first. For more information, see Create a storage pool.

1. Log on to the ASR for Backup and Recovery console as an operations administrator.
2. In the left-side navigation pane, choose **System Management** > **Storage Pool Groups**.
3. Enter a storage pool group name in the search box and click **Search**.
4. Find the storage pool group and click **Add Storage Pool** in the **Actions** column.
5. Configure the parameters.

| Parameter | Description |
|---|---|
| Storage Pool Name | A descriptive name for the storage pool group, such as "Public Cloud Storage Pool". Note The name can contain letters, digits, hyphens (-), and underscores ( ). It must be less than 64 characters in length. _ |
| Storage Capacity | The storage capacity of the storage pool. Unit: TB. |
| AccessKey ID | The AccessKey ID of the account that accesses the destination storage. Note The AccessKey ID and AccessKey secret must have the permissions to read and write data. |
| AccessKey Secret | The AccessKey secret of the account that accesses the destination storage. |
| Authorized Organization | Select the level-1 organizations. You can select all level-1 organizations. |

| Recycle Bin | Optional. Specify the name of the recycle bin. This parameter is required if you need to create a deduplication backup vault or a mirror vault in the storage pool. Note When you create a deduplication backup or mirror vault, an existing bucket of the recycle bin is used if any. If no bucket exists, a relevant bucket is created. |
|---|---|
| Storage Pool Description (optional) | The description of the storage pool for easy identification. |

6. Then, click **OK**.
If the storage pool is created, the problem is solved. If the storage pool cannot be created, contact the backup R&D team for troubleshooting.

### 17.5 What do I do if the 500 error is displayed on pages of the ASR for Backup and Recovery console?

**is displayed on pages of the ASR**

**for Backup and Recovery console?**

This topic describes how to troubleshoot the 500 error on pages of the ASR for Backup and Recovery console.

**Problem description**

The 500 error is displayed in the menu section of pages and the menus cannot be displayed normally.

**Cause**

The HBR service is abnormal.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform > Resources** to access the Apsara
Infrastructure Management console.
3. In the left-side navigation pane, choose **Resources > Product & Cluster O&M**.
4. Enter ASRBR in the **Product | Cluster** search box on the **Product & Cluster O&M** page,
find the cluster, and then click **Cluster Details** in the Actions column.
5. On the **Cluster Details** page, click **hbr-console** service.
6. Click the Instance /IP Address to go to the **Machine Details** page.
7. Click **Restart** in the Actions column for the **Console#** component.
8. In the **Confirmation** dialog box that appears, enter **RESTART** and click **OK**.
9. After the hbr-console service is restarted, check whether the page is displayed normally by
performing the steps in Verification.

**Verification**

1. Log on to the ASR for Backup and Recovery console using the current account. For more
information, see Log on to the ASR for Backup and Recovery console.
2. Click any menu to access the page and check whether 500 error is displayed on the page.
If the page is displayed normally, the problem is solved. If the 500 error is returned, contact the backup R&D team for troubleshooting.

## 18 Appendix

### 18.1 Install an HBR agent on an ECS instance

**ECS instance**

This topic describes how to install a Hybrid Backup Recovery (HBR) agent on an Elastic Compute Service (ECS) instance in the primary cloud.

**Background information**

You must install an HBR agent on the ECS instance for which you want to perform remote backup or restoration in the primary cloud.

**Procedure**

1. Obtain the endpoint of the HBR service.
i. Log on to the Apsara Uni-manager Operations Console in the secondary cloud. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane, choose **O&M Tools** > **Basic Data Management** >
**Base Meta Data Management** > **Service Registration Variable Dashboard**.
iv. Select **Service** from the drop-down list in the upper-left corner, enter rds-ddr-proxy and hbr-rabbitmq respectively in the search box, and then click the search icon. v. Click the icon in the **Service Registration** column of the **rds-ddr-proxy** service and then click the content in the **Service Registration** column. The Registration Variables dialog box appears. In the Registration Variables dialog box, you can view the value of the
**asr.resource.domain** service registration variable.
vi. Click the icon in the **Service Registration** column of the **hbr-rabbitmq** service and then click the content in the **Service Registration** column. The Registration Variables dialog box appears. In the Registration Variables dialog box, you can view the value of the
**hbr.rabbitmq.domain** service registration variable.
2. Download the installation package of the HBR agent for the ECS instance from the primary
cloud. In Linux, run the following command to download the installation package:

```bash
curl -O --basic -u guest:guest http://<hbr_resource_host>/download/<hbragent_filename>
```

> **Note:** Replace the value of hbr_resource_host with the value of **asr.resource.domain** that you obtained in Step 1.
> Replace the value of hbragent_filename with the name of the installation package of the HBR agent.
> Package name in a 32-bit operating system: hbr-install-2.0.0-linux-32bit.tar.gz
> Package name in a 64-bit operating system: hbr-install-2.0.0-linux-64bit.tar.gz

In Windows, enter the following URL in the address bar of your browser to download the installation package:

```xml
<hbr_resource_host>/download/<hbragent_filename>
```

In the dialog box that appears, enter the username and password. In this example, the username is guest and the password is guest.

> **Note:** Replace the value of hbr_resource_host with the value of **asr.resource.domain** that you obtained in Step 1.
> Replace the value of hbragent_filename with the name of the installation package of the HBR agent.
> Package name in a 32-bit operating system: hbr-install-2.0.0-windows-32bit.zip
> Package name in a 64-bit operating system: hbr-install-2.0.0-windows-64bit.zip

3. Decompress the installation package.
4. Install the HBR agent.
In Linux, run the following command:

```
./setup -m ApsaraStack -h<hbr_amqp_host>
```

In Windows, run the following command:

```xml
<hbragent_filename> /TYPE=ApsaraStack /host= <hbr_amqp_host>/SUPPRESSMSGBOXES /VERY SILENT
```

> **Note:** Replace the value of hbr_amqp_host with the value of **hbr.rabbitmq.domain** that you obtained in Step 1.
> Replace the value of hbragent_filename with the name of the installation package of the HBR agent.
> Package name in a 32-bit operating system: hbr-install-2.0.0-windows-32bit.zip
> Package name in a 64-bit operating system: hbr-install-2.0.0-windows-64bit.zip

5. Check whether the HBR service runs as expected.
In Linux, run the following command to check the status of the HBR service:

```
ps aux | grep hbr
```

In Windows, start Task Manager and check whether the **hybridbackup** service is in the
**Running** state.

### 18.2 Preparations for using the storage cascade feature of a backup vault

**storage cascade feature of a**

## backup vault

This chapter provides the introduction, network requirements, constraints, and initialization operations for using the storage cascade feature of a backup vault.

#### 18.2.1 Introduction to the storage cascade feature of a backup vault

**feature of a backup vault**

A backup vault is a logical storage space planned on a storage pool to store backup data. The storage cascade feature allows you to create a remote mirror vault for a backup vault based on your backup requirements. The data in the backup vault is automatically replicated to the mirror vault by using cross-region and cross-cloud replication capabilities of OSS. This way, backup data is stored in multiple locations. You can select either the backup vault or the mirror vault to restore data.

**Network conditions**

Ensure that the related ASR-BR components are connected to multiple OSS buckets. For more information, see Application-backup vault mapping. Based on the requirements of the cross-region and cross-cloud replication features of OSS, ensure network connectivity and normal data replication between multiple OSS buckets. Cross-region replication of OSS: You can perform this operation based on your on-site network environments and the multi-region network connection solution. Cross-cloud replication of OSS: Make sure that the OSS bucket in the source cloud can access the OSS bucket in the destination cloud through the endpoint and data can be replicated. If you use DNS rules to configure network connectivity for data replication, ensure that DNS products are deployed in the source cloud, and DNS domain name-based forwarding rules and network connectivity are configured on the tenant-side DNS and OpsDNS in the source cloud. For more information about DNS configuration rules and rollback solutions, you can submit a ticket to consult the relevant technical support personnel. If you use other methods to implement network connectivity for cross-region data replication of OSS, re-evaluate the network connectivity solution based on on-site conditions and security requirements of the customer.

**Constraints**

The related ASR-BR components are connected to multiple OSS buckets, the OSS buckets at both ends of data replication are connected, and cross-region and cross-cloud replication can be used normally. For more information, see Application-backup vault mapping. For cross-region replication, you need to enter the information about the two storage pools to which the backup vault and mirror vault belong in the ASR-BR console, including the cloud name, cloud region, and location. For cross-cloud replication, you need to enter the cloud name, cloud region, location, and UID of the proxy user. Before you use a backup vault to create a mirror vault, you must configure the recycle bins for the storage pools where the backup and mirror vaults reside. Only OSS 1.0, CDS-OSS, and PanguStor support cross-cloud and cross-region replication. MiniOSS and SDS do not support cross-cloud or cross-region replication. In addition, data on OSS 1.0 can only be replicated to OSS 1.0. Data can be replicated between CDS-OSS and PanguStor. At the backup vault end, if OSS 1.0 and CDS-OSS clusters exist and data migration is enabled, the storage cascade feature is not supported. If the storage cascade feature is required, submit a ticket to contact the R&D team to provide a solution.

#### 18.2.2 Initialization in the console

To ensure that data can be synchronized from a backup vault to a mirror vault, you need to perform manual configurations once, which is also called initialization. Cross-region synchronization involves the source and destination ends. The initialization steps at the source and destination ends are different. Check whether an environment belongs to the source or destination end to prevent misoperations.

**Initialization at the destination end (mirror vault)**

1. Create a proxy user and grant permissions at the destination end.

> **Note:** This step is required only for cross-cloud replication.

i. Log on to the Apsara Uni-manager Management Console at the destination end. ii. In the top navigation bar, choose **Enterprise > Permissions > Role Permissions**. iii. Click **Create Custom Role**. iv. Enter a role name. Keep the default values for other parameters. v. Expand Advanced Settings and click **Create RAM Authorization**. vi. Enter a role name and retain the default values for other parameters. Then, click **Create**
**and Configure RAM Authorization**.
vii. Click the **Permissions** tab. Then, click **Add Policy**. viii. Click **Create Policy**. In the Create Policy dialog box, specify a policy name and copy the following content to the Policy Content field. `{`

```json
 "Version": "1",
 "Statement": [
```

`{`

```json
 "Effect": "Allow",
 "Action": "oss:*",
 "Resource": [
 "acs:oss:*:*:*"
```

`]` `}` `]` `}` ix. Then, click **OK**. x. Select the policy that you created in the previous step and click **OK**.
2. Create a user group.

> **Note:** Skip the following steps for PanguStor because PanguStor has only users and no user groups.

i. In the left-side navigation pane, choose **Users > User Groups**. ii. On the User Groups page, click **Create a user group**. iii. Specify the user group name and organization. The values of the Role Permissions parameter must include the RAM role created in the previous step. iv. Click **OK**.
3. Create a proxy user.
i. In the left-side navigation pane, choose **Users > Users**. ii. On the Users page, click **Create a user**. iii. Select the organization that is selected in the previous step. Specify other parameters based on your business requirements. iv. Click **OK**. The system creates an AccessKey pair. Record the AccessKey pair, which will be used later. v. Click **View Details** in the **Actions** column of the created user. vi. View and record the UID of the user, which will be used later. vii. Find the user, click in the **Actions** column, and then select **User Group**
**Management**. On the page that appears, click **Add to User Group**.

> **Note:** Skip the following steps for PanguStor because PanguStor has only users and no user groups.

viii. Select the user group created in the previous step and click **OK**.
4. Configure permissions for the proxy user.
i. Log on to the Apsara Uni-manager Operations Console at the destination end. ii. In the top navigation bar, choose **Product Operation > Storage > OSS Storage**
**Operations and Maintenance System**.
iii. In the left-side navigation pane, choose **Service O&M - OSS > OCM List**
**Management**.
iv. Click **Add**. In the Add list dialog box, enter the UID of the proxy user saved in the previous step, select **as_sync_admin** from the **type** drop-down list, and then click **Add**. In the dialog box that appears, click **Yes**.
5. Obtain the cloud parameters.
i. In the left-side navigation pane, choose **Service O&M - OSS > Synchronization**
**Management > Cross-Cloud Synchronization**.
ii. Select a cluster and click **View Parameters of the Current Cloud** . iii. Copy and save the values of the following four parameters for each cluster: Name of Ben Duo Yun, Ben Duo Cloud Region, Ben Duoyun Region domain name, and Location.

> **Note:** You need to record the parameter values for each cluster.

6. Configure cross-region and cross-cloud replication authorization in the ASR-BR console.
i. Log on to the Apsara Uni-manager Management Console at the destination end. ii. In the top navigation bar, choose **Products > Disaster Recovery > ASR for Backup**
**and Recovery**.
iii. In the left-side navigation pane, choose **System Management > Storage Pool**
**Groups**.
iv. Find the storage pool that you want to manage at the destination end, and click **Cross-**
**region/Cross-cloud Replication Authorization** in the **Actions** column.
v. Enter the cloud name, cloud region, location, and the UID of the proxy user at the destination end, and then click**OK**.

**Note**

For the destination end of cross-region replication, the UID of the proxy user is not required. For the destination end of cross-cloud replication, the UID of the proxy user is required.

**Initialization at the source end (backup vault)**

1. Log on to the Apsara Uni-manager Operations Console at the source end.
2. In the top navigation bar, choose **Product Operation > Storage > OSS Storage**
**Operations and Maintenance System**.
3. In the left-side navigation pane, choose **Service O&M - OSS > Synchronization**
**Management > Cross-Cloud Synchronization**.
4. Click **Create**. In the dialog box that appears, enter the values of Name of Ben Duo Yun, Ben
Duo Cloud Region, Ben Duoyun Region domain name, and Location of each cluster and the AccessKey pair saved at the destination end.

> **Note:** The parameter values of each cluster obtained at the destination end must be added at the source end.

5. Log on to the Apsara Uni-manager Management Console at the source end.
6. In the top navigation bar, choose **Products > Disaster Recovery > ASR for Backup**
**and Recovery**.
7. In the left-side navigation pane, choose **System Management > Storage Pool Groups**.
8. Click **Cross-region/Cross-cloud Replication Authorization** in the **Actions** column.
9. Enter the cloud name, cloud region, and location at the source end, and then click**OK**.

### 18.3 Configure the ASR-BR service-linked role for an organization

**service-linked role for an**

**organization**

This topic describes how to configure the service-linked role Apsara Stack Resilience for Backup and Recovery (ASR-BR) for an organization.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Configurations**.
3. In the left-side navigation pane, click **Service-linked Roles**.
4. On the **Service-linked Roles** page, click **Create Service-linked Role**.
5. On the page that appears, select **ASR-BR** from the **Service Name** drop-down list and
select the name of the organization for which you want to configure the service-linked role from the **Authorized Organization Name** drop-down list.
6. Click **OK**.

### 18.4 Network limits

You must make sure that the internal network of the customer and Apsara Stack can communicate with each other.

### 18.5 Statistics on the resource set-level resource usage in an organization

**set-level resource usage in an**

**organization**

ASR for Backup and Recovery collects and pushes the backup data of the previous day by instance at 1:00 every morning. The backup data size of each instance for each service is collected and displayed on the Metering Management page of the Apsara Uni-manager Management Console by organization and resource set.

**Background information**

ASR for Backup and Recovery backs up data of cloud services at specified intervals. In addition, ASR for Backup and Recovery also pays attention to the amount of data backed up. In order to provide better backup experience, ASR for Backup and Recovery displays data on the Metering Management page to provide unified usage statistics.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Operations > Resource Operations**.
3. In the left-side navigation pane, click **Metering Management**.
4. Select **ASR for Backup and Recovery** from the Cloud Service drop-down list, set the
organization, resource set, and other search conditions, and then click **Search**.

> **Note:** Usage statistics are collected by tenant. The principle of least privilege is employed. Unauthorized access to usage statistics of other tenants is not allowed.

### 18.6 Use the SMB protocol to back up and restore NAS files

**up and restore NAS files**

#### 18.6.1 Use the SMB protocol to back up NAS files

**files**

**Prerequisites**

A Windows Elastic Compute Service (ECS) instance is available in the region where you create a Server Message Block (SMB) file system. Linux is not highly compatible with the SMB protocol. Therefore, Linux backup engines do not support the use of an SMB file system for data backup. An SMB file system is created and the mount target of the file system is obtained. The network is available. The IP address of the Windows ECS instance is in the whitelist of the SMB file system and the ECS instance can access the SMB file system. TCP port 445 is enabled for the Windows ECS instance to access the SMB file system. If port 445 is disabled, you must add a rule to a security group of the ECS instance for the port. For ASR for Backup and Recovery, backing up an SMB file system is to back up a shared file system mounted on an ECS instance.

**Procedure**

**Note**

You need to perform the following environment preparation steps only once when you mount file systems on a Windows ECS instance. You do not need to perform them each time you mount an SMB file system on the Windows ECS instance.
1. Prepare the environment.
i. Log on to the Apsara Uni-manager Management Console. ii. Connect to the ECS instance by using Virtual Network Console (VNC) Viewer or a remote connection method. iii. Enable the Workstation service. a. Choose **All Programs > Accessories > Run** or press Win+R. Then, enter services.msc to open the Services window. b. Make sure that the Workstation service is in the **Started** state and the startup type is
**Automatic**. By default, the Workstation service is in the Started state.
c. Enable the TCP/IP NetBIOS Helper service. a. On the **Network and Sharing Center** page, click the active network connection. b. Select **Properties**. In the Connection Properties dialog box, double-click **Internet**
**Protocol Version 4 (TCP/IPv4)**. In the Internet Protocol Version 4 (TCP/IPv4)
Properties dialog box, click **Advanced**. c. In the **Advanced TCP/IP Settings** dialog box, choose **WINS > Enable NetBIOS**
**over TCP/IP**.
d. Choose **All Programs > Accessories > Run** or press Win+R. Then, enter services.msc to open the Services window. e. Make sure that the TCP/IP NetBIOS Helper service is in the **Started** state and the startup type is **Automatic**. By default, the TCP/IP NetBIOS Helper service is in the Started state.
2. Mount an SMB file system.
i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Storage > Apsara File Storage NAS**. iii. In the left-side navigation pane, choose **File System > File Systems**. iv. On the **File System List** page, click **Create File System**. v. Specify the File System Name parameter. Set **Protocol Type** to **SMB**. Other parameters are automatically configured. Then, click **Submit**. vi. Click **Manage** in the **Actions** column and click **Mount Targets**. vii. Click **Add Mount Target**, configure the parameters, and then click **OK**. Then, record the mount command.
3. Manually mount the file system.
i. Mount the file system. a. Connect to the ECS instance. b. Open the Command Prompt and run the following command to mount the SMB file system:

```
net use Z: \\file-system-id.region.nas.aliyuncs.com\myshare
```

| Parameter | Description |
|---|---|
| Z | The drive letter. If a conflict occurs in drive Z, or if multiple NAS file systems are mounted to drive Z, the NAS file system is mounted to the next drive in reverse alphabetic order. |
| file-system-id.region.nas.aliyuncs.com | The domain name of the mount target. The domain name is automatically generated when you create the mount target. Replace the domain name with the actual value. Alternatively, you can click the destination file system, and then click Mount Targets. Move the pointer over the icon in the mount target column to obtain the domain name of the mount target. |
| myshare | The name of the shared SMB directory. You cannot change the name. |

ii. Check whether the SMB file system is mounted. a. Run the following command:

```
net use
```

b. If a command output that is similar to the following information appears, the file system is mounted. Then, you can access the SMB file system on the ECS instance and perform read and write operations on the file system.
4. Install a backup client for the Windows ECS instance.
i. Log on to the Apsara Uni-manager Management Console. ii. In the top navigation bar, choose **Products > Disaster Recovery > ASR for Backup**
**and Recovery**.
iii. In the left-side navigation pane, click **Backup Plans**. iv. On the **Backup Plans** page, click **Create**. v. On the Backup Plans page, click Create. In the **Basic Information** step, set **Instance**
**Type** to **Elastic Compute Service**, set **Backup Method** to **File Backup**, and then click
**Next**.
vi. In the **Select Instance** step, select an ECS instance and click **Next**. vii. In the **Install Client** step, select the installation path and click **Install**. viii. After the backup client is installed, you can check whether the backup client is successfully installed and started based on the directory where the backup client is installed and the services started in the ECS instance. Click **Next**.
5. Grant the backup client the permissions to back up SMB files.
i. Connect to the ECS instance. ii. Press Win+R. In the Run dialog box, enter services.msc and click **OK**. iii. Find Alibaba Cloud Hybrid Backup Service in the service list. Right-click the service and select **Properties**. iv. In the dialog box that appears, click the **Log On** tab. v. Select **This account**, click Browse, and then enter the account and password. Click OK. The account must have the following permissions. Full access to the NAS file system Administrative rights Permissions to log on as a service

**Note**

For more information, see How do I select a component and account when I install a cloud backup client . vi. Restart the Alibaba Cloud Hybrid Backup Service.
6. Proceed to Step 4 to create an SMB NAS backup plan.
i. In the **Configure Instance** step, set Source Path to \\file-systemid.region.nas.aliyuncs.com\myshare. ii. Click **Next** and configure the backup policy. For more information, see Create a backup plan. Configure data according to the configuration wizard until the backup plan is created.
7. On the **Backup History** tab, you can view the backup results.

#### 18.6.2 Use the SMB protocol to restore NAS files

**files**

When you use the Server Message Block (SMB) protocol to restore NAS files, we recommend that you mount a new SMB file system on the ECS instance for data restoration because ECS instances support only overwritten recovery. This prevents data loss caused by overwriting the data of the original SMB file system by the backup data.

**Prerequisites**

In the region where you create an SMB file system, a Windows ECS instance is available. Linux is not highly compatible with the SMB protocol. Therefore, Linux backup engines do not support the use of an SMB file system for data backup. An SMB file system is created and the mount target of the file system is obtained. The network is available. The IP address of the Windows ECS instance is in the whitelist of the SMB file system and the ECS instance can access the SMB file system. TCP port 445 is enabled for the Windows ECS instance to access the SMB file system. If port 445 is disabled, you must add a rule to a security group of the ECS instance for the port. For ASR-BR, backing up an SMB file system is to back up a shared file system mounted on the corresponding ECS instance. When you use the SMB protocol to restore NAS files, we recommend that you mount a new SMB file system on the ECS instance for data restoration, because ECS instances support only overwritten recovery. This prevents data loss caused by overwriting the data of the original SMB file system by the backup data.

**Procedure**

1. Log on to the ASR-BR console.
2. In the left-side navigation pane, click **Recovery Jobs**. On the Recovery Jobs page, click
**Create**.
3. In the **Basic Information** step, configure the parameters and click **Next**.

| Parameter | Description |
|---|---|
| Recovery Job Name | The name must be 4 to 20 bytes in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Description | Optional. We recommend that you enter a description to help you identify the job. |
| Instance Type | Select Elastic Compute Service. |
| Recovery Job Type | In this scenario, select Routine Recovery. |
| Recovery Method | Cloud disk recovery: This recovery method is available only when the backup method of the ECS instance is cloud disk backup. File Recovery: This recovery method is available only when the backup method of the ECS instance is file backup. |

4. In the **Select Instance** step, select the instance that you want to restore and click **Next**.
5. In the **Select Record** step, select a previous backup record and click **OK**.
6. In the **Configure Instance** step, configure the destination instance and client. Then, click
**Next**.
i. In the **Destination** step, select the destination instance. Click **Next**. ii. In the **Client Installation** step, if the ECS instance on which the SMB file system is mounted does not have a backup client installed, you must install the backup client. After the installation is complete, click **Next**. iii. In the **File Recovery Rules** step, enter the local path for storing the restored file. click
**Next**.
7. The recovery job is created. After the recovery job is executed, you can view the recovery
results. For more information, see View recovery jobs.

### 18.7 Cross-region backup

**Limits on ASR for Backup and Recovery**

**Limits on database backup**

After Transparent Data Encryption (TDE) is enabled, ApsaraDB RDS for SQL Server does not support recovery. After TDE is enabled, ApsaraDB RDS for SQL Server does not support cross-region recovery and cloud rebuilding recovery. When RDS, PolarDB-X, and AnalyticDB for MySQL V3.0 use the local backup records for recovery, make sure that the original instance is not deleted.

**Limits on storage backup**

When you create an OSS recovery task, a new bucket is created. By default, the capacity of the original backup bucket is used. However, no storage space is consumed. Each Apsara File Storage NAS backup task can contain up to 50 million files. The total number of files and subdirectories cannot be greater than 8 million in a single directory. The data backup size of Elastic Compute Service (ECS) files depends on the memory capacity. If 4 GB of system memory is available, up to 1 million files or 8 TB of data can be backed up. We recommend that you use a dual-core 64-bit CPU and more than 8 GB of available memory to back up ECS files. To back up tens of millions of files, we recommend that you use 16 GB of available memory.

**Limits on OSS**

ASR for Backup and Recovery cannot back up VPC OSS. If an authorization policy is configured for the OSS bucket that you want to back up, make sure that the authorization policy allows ASR for Backup and Recovery to read objects in the OSS bucket. For backing up a dynamic object (on which the append write, multipart upload, or overwrite operation is performed during the backup process) in OSS: For a small file (less than 25 MB), if the file is updated during the backup process and the ETag is inconsistent during backup, the system tries to back up the updated file. The backup result depends on the amount of data that is actually backed up. For a large file (more than 25 MB), the file is split into several parts and then read and backed up. If the file is updated during the backup process and the ETag is inconsistent during backup, the backup result depends on the amount of data that is actually backed up. The unchanged parts are backed up in best-effort mode. The continuous parts that have been backed up are stored in the backup vault and considered as successful backup. The backup job regards the whole file as successful backup. The updated parts are no longer backed up this time and will be backed up the next time a backup job is triggered.

**Limits on MaxCompute backup**

The foreign table feature must be enabled. Make sure that you have purchased the MaxCompute Enhancement Pack for Joint Computing.

**Limits on backup of the entire ECS or disks**

Crash consistency is supported only for disks. You cannot establish logical volume management (LVM) or SoftRAID across disks. Encrypted disks cannot be backed up or recovered. A maximum of 64 local snapshots can be retained. If you manually create a snapshot during disk backup, the backup may fail. A snapshot-consistent group supports snapshots of up to 16 disks and a maximum of 32 TB of data.
