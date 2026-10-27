---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster User Guide 20250618"
product_version: "V3.18.3"
doc_version: "20250618"
pdf_pages: 103
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster User Guide 20250618.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E7%81%BE%E5%A4%87%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Geo-disaster%20User%20Guide%2020250618.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster User Guide 20250618

## Table of Contents

- 1 ASR for Geo-disaster Recovery
- 2 Getting Started
  - 2.1 Roles and permissions
  - 2.2 Log on to the ASR for Geo-disaster Recovery console
  - 2.3 DR scenarios
- 3 Overview
- 4 ASR dashboard
- 5 Instance management
  - 5.1 Create instances
  - 5.2 View the details of an instance
- 6 DR for business
  - 6.1 Protection Groups
    - 6.1.1 Manage protection groups
      - 6.1.1.1 Create a protection group
      - 6.1.1.2 Perform reprotection
      - 6.1.1.3 Protection group details
        - 6.1.1.3.1 View the details of a protection group
        - 6.1.1.3.2 View the logs of a protection entity
        - 6.1.1.3.3 View the operations records of a protection group
        - 6.1.1.3.4 Delete a protection entity
        - 6.1.1.3.5 Modify the attribution of a protection entity
        - 6.1.1.3.6 Modify the read-only account of an ApsaraDB RDS instance
        - 6.1.1.3.7 Modify the privileged account of an ApsaraDB RDS instance
        - 6.1.1.3.8 Modify table filtering
        - 6.1.1.3.9 Manage protection entity account permissions
      - 6.1.1.4 Add a synchronization entity
        - 6.1.1.4.1 ApsaraDB RDS
        - 6.1.1.4.2 PolarDB-X V1.0
        - 6.1.1.4.3 OSS
        - 6.1.1.4.4 Big data products
        - 6.1.1.4.5 DNS (Multicloud Integration)
        - 6.1.1.4.6 DNS within Cloud
        - 6.1.1.4.7 Message Queue
        - 6.1.1.4.8 KVStore for Redis
        - 6.1.1.4.9 ApsaraDB for MongoDB
        - 6.1.1.4.10 ECS
        - 6.1.1.4.11 DataHub
      - 6.1.1.5 Modify drill metrics
      - 6.1.1.6 Start a protection group
      - 6.1.1.7 Stop a protection group
      - 6.1.1.8 View the synchronization logs of MaxCompute
      - 6.1.1.9 Manually synchronize data
    - 6.1.2 Fail over a protection group
    - 6.1.3 Fail back a protection group
  - 6.2 Manage a plan
    - 6.2.1 Overview
    - 6.2.2 Manage business disaster recovery plans
      - 6.2.2.1 Create a business disaster recovery plan
      - 6.2.2.2 Query a business disaster recovery plan
      - 6.2.2.3 Execute a business DR drill plan
      - 6.2.2.4 View the execution history of a plan
    - 6.2.3 Manage a disaster recovery unit namespace
      - 6.2.3.1 Create a disaster recovery unit namespace
      - 6.2.3.2 Fail over a disaster recovery unit namespace
      - 6.2.3.3 Fail back a disaster recovery unit namespace
- 7 Alert management
  - 7.1 Configure alert rules
  - 7.2 View and export alert information
  - 7.3 Configure synchronization latency alert thresholds
- 8 System Management
  - 8.1 Log management
  - 8.2 Cloud instance management
- 9 Appendix
  - 9.1 Create a RAM role
  - 9.2 Obtain an AccessKey pair
  - 9.3 Obtain the configuration information of the primary cloud instance
  - 9.4 Customize the data-plane SDK to implement access from multiple endpoints

## 1 ASR for Geo-disaster Recovery

**Recovery**

This topic describes the basic principles, terms, and functional modules of ASR for Geodisaster Recovery.

**Overview**

ASR for Geo-disaster Recovery is a cloud service that provides disaster recovery capabilities. ASR for Geo-disaster Recovery can ensure data availability and reliability by using hot back up and disaster recovery solutions for the following services: Object Storage Service (OSS), ApsaraDB RDS for MySQL 5.6, 5.7, and 8.0, PolarDB for Oracle 11.2, PolarDB-X 1.0, Apsara Stack DNS, ApsaraMQ, KVStore for Redis, DataHub, MaxCompute, and DataWorks. After you create a protection group, ASR for Geo-disaster Recovery establishes a hot backup channel between the resources of the primary and secondary sites. Changes to the resources at the primary site are asynchronously synchronized to the corresponding resources at the secondary site in hot backup mode. When the primary site fails, applications or services can be failed over to the secondary site by using a failover plan. After the primary site is recovered, applications or services can be failed back to the primary site by using a failback plan. This way, business continuity is ensured.

**Terms**

Protection group: a business object that is protected by ASR for Geo-disaster Recovery. You can create a protection group for resources used by an application. Recovery plan: a predefined automated workflow to handle faults. When a disaster or fault occurs, the corresponding workflow automatically executes to perform disaster recovery on resources in the protection group to ensure business continuity. Failover: an unplanned transfer of applications from the primary data center to the secondary data center due to a power or network outage in the primary data center. Failback: an unplanned recovery of applications from the secondary data center to the primary data center after a power or network failure is restored on the primary data center. Drill plan: a predefined workflow that is used to perform disaster recovery drills. The steps of a drill plan are similar to those of the corresponding recovery plan. Use drill plans to perform recovery drills and guarantee the effectiveness of recovery plans. Switchover: a planned switch of applications from the primary data center to the secondary data centers when the power and network conditions are normal. Switchback: a planned switch of applications from the secondary data center to the primary data centers when the power and network conditions are normal. Recovery Point Objective (RPO): the maximum amount of data that can be lost after the system and data are recovered from a disaster. The amount of data loss is measured by time. A smaller RPO indicates a smaller acceptable amount of data loss. Recovery Time Objective (RTO): the maximum period of time that is acceptable for the system and business to recover from a disaster. RTO indicates the maximum service downtime that is acceptable. A smaller RTO indicates a higher urgency for recovery of a system service.

**Functional modules**

| Function al module | Description |
|---|---|
| Overview | Displays information such as protection groups, disaster recovery plans, and synchronization entities. |
| Instances | Displays all instances at the primary and secondary sites, the status of instances, and information about the protection groups with which instances are associated. This helps you obtain information about the status of instances in the current cluster and an overview of cluster health. |
| DR for Business | Allows you to configure protection groups, disaster recovery plans, and disaster recovery unit namespaces. |
| Alert Managem ent | Allows you to set alert rules for various metrics of protection groups and plans, configure alert thresholds for synchronization latency, and send alert notifications to alert contacts. The alert notifications help stay updated on system exceptions and troubleshoot issues. |
| System Managem ent | Allows you to manage system permissions in a centralized manner, which helps you manage cloud instances and logs. |
| ASR Dashboar d | Provides an overview of protection groups, recovery plans, drill plans, cloud service protection, and alerts on a dashboard. |

## 2 Getting Started

### 2.1 Roles and permissions

This topic describes the permissions of operations administrators, organization administrators, global disaster recovery (DR) administrators, and organization DR administrators.

| Role | Logon method | Permissions |
|---|---|---|
| Operations administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the operations administrator role, such as the admin account. 2. Select the root organization to access the ASR-DR console. | Add primary cloud instances and configure cloud services. Manage DR resources for all cloud services. |
| Organization administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the organization administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator but cannot configure cloud services. Manage DR resources for cloud services only in the current organization and subordinate organizations. |
| Global DR administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the global DR administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator and configure cloud services. Manage DR resources for all cloud services. |
| Organization DR administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the organization DR administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator but cannot configure cloud services. Manage DR resources for cloud services only in the current organization and subordinate organizations. |

### 2.2 Log on to the ASR for Geo-disaster Recovery console

**disaster Recovery console**

This topic describes how to log on to the ASR for Geo-disaster Recovery console.

**Prerequisites**

The domain name, username, and password are obtained from the deployment personnel of the Apsara Uni-manager Management Console. A web browser is available. We recommend that you use Google Chrome. You are an operations administrator, organization administrator, global disaster recovery administrator, or organization disaster recovery administrator.

**Scenarios**

In cross-cloud disaster recovery scenarios, the ASR for Geo-disaster Recovery console is deployed in the secondary cloud. You need to log on to the ASR for Geo-disaster Recovery console by using the Apsara Uni-manager Management Console in the secondary cloud. In cross-region disaster recovery scenarios, the ASR for Geo-disaster Recovery console is deployed in the central region. You need to log on to the ASR for Geo-disaster Recovery console by using the Apsara Uni-manager Management Console in the central region. In disaster recovery scenarios within a region, you need to log on to the ASR for Geodisaster Recovery console by using the Apsara Uni-manager Management Console of the production center.

> **Note:** The first time you log on to the ASR for Geo-disaster Recovery console, you must make the following initial configurations:
> Configure cloud services that support disaster recovery. For more information, see the "Manage cloud product information" section in ASR for Geo-disaster Recovery O&M Guide.

Configure cloud instances. For more information, see Cloud instance management.

> Configure a RAM role. For more information, see Create a RAM role.
> Configure independent disaster recovery. For more information, see the "Manage independent DR" topics in ASR for Geo-disaster Recovery O&M Guide. You need to configure independent disaster recovery only in cross-cloud disaster recovery scenarios. You do not need to configure independent disaster recovery in cross- region disaster recovery scenarios.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.

2. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Account Logon**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, select **Products**.
6. In the left-side navigation pane, click **Disaster Recovery and Backup**.
7. In the **Disaster Recovery and Backup** section, choose **Disaster Recovery > ASR for**
**Geo-disaster Recovery**.
8. You are redirected to the ASR for Geo-disaster Recovery console. All data is displayed by
organization, resource set, and region. The first time you log on to the console, you must configure a cloud instance.

### 2.3 DR scenarios

Geo-disaster Recovery Enterprise supports cross-cloud disaster recovery (DR) and crossregion DR. This topic describes two DR scenarios. Cross-cloud DR and cross-region DR Cross-cloud DR: DR is performed between two cloud instances. If the primary cloud fails, business is failed over to the secondary cloud. Cross-cloud DR can be implemented in the following modes: Cross-cloud DR for a single cloud: If the central region of the primary cloud fails, business can fail over to the central region of the secondary cloud. Cross-cloud DR for a single cloud: If a general region of the primary cloud fails, business can fail over to the central region of the secondary cloud. Cross-cloud DR for multiple clouds: If multiple primary clouds fail, business can fail over to the central region of the secondary cloud. Three data centers across two regions. Cross-region DR: DR is performed across multiple regions within a cloud instance. Crosscloud DR can be implemented in the following modes: If a general region fails, business can fail over to the central region. If a general region fails, business can fail over to another general region. If the central region fails, business can fail over to a general region. Only DR for business is supported. The following table describes the products and features supported in the two DR scenarios.

## 3 Overview

The Overview page provides charts and numbers to show the disaster recovery (DR) overview of business. You can view the real-time DR metrics and learn the DR protection group status on this page. This helps improve the efficiency of DR management and the continuity of application business.

**Precautions**

When you log on to the ASR for Geo-disaster Recovery console for the first time, you are promoted to configure a primary cloud instance. See the following figure. All business data can be displayed by organization, resource set, or region.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **Overview**.
3. On the **Overview** page, you can view the following information:
The following table describes the information that is displayed in each module of this page.

| Module | Description |
|---|---|
| Maximum Synchronization Latency Overview | Displays the maximum synchronization latency of each cloud service. |
| Protection Group Overview | Displays the total number of protection groups, the number of abnormal protection groups, the total number of synchronization entities, and the number of abnormal entities. |
| Disaster Recovery Plan Overview | Displays the total number of business disaster recovery plans and the total number of site disaster recovery plans. |
| Synchronization Latency Distribution of Synchronized Entities | Displays the synchronization latency distribution in a donut chart. You can click the icon next to the name of a cloud service to switch between cloud services. Lists the names and latency values of TOP 6 Synchronization Latency Values of Synchronized Entities. You can move the pointer over the card and click View More to go to the Synchronized Entities page. |
| Disaster Recovery Plan Execution Data | Includes the Drill History and Failover Records tabs. The Drill History tab displays the latest drill status. The Failover Records tab displays the latest failover status. |
| Protection Group Disaster Recovery Analysis | Lists the statuses of protection groups. You can click View More to go to the Protection Groups page. |

| Protection Group Disaster Recovery Analysis Details | Displays the synchronization latency of protection groups for a cloud service during switchover or switchback and failover or failback in a line chart. You can view the synchronization latency on the Last 24 Hours, Last 15 Days, Last Month, Last 3 Months, Last 6 Months, and Last Year tabs. You can click the name of a protection group in the Protection Group Name list of the Protection Group Disaster Recovery Analysis section to view Protection Group Disaster Recovery Analysis Details of the protection group. Note The data sampling frequency is low for a long-term time range. Data of a specific period of time may not exist when you view the data of a newly configured protection group by month or by year. |
|---|---|
| Disaster Recovery Analysis of Cloud Product Synchronization Entities | Lists all cloud services and the number of synchronization entities for each cloud service. You can click View More to go to the Synchronized Entities page. |
| Synchronization Entities Disaster Recovery Analysis Details | Displays the synchronization latency distribution of synchronization entities and the average synchronization latency in a line chart. You can view the data on the Last 24 Hours, Last 15 Days, Last Month, Last 3 Months, Last 6 Months, and Last Year tabs. You can move the pointer over the line chart to view the maximum, minimum, median, and average latency values. Note The data sampling frequency is low for a long-term time range. Data of a specific period of time may not exist when you view the data of a newly configured protection group by month or by year. The maximum period during which no data exists is one month. |
| Alert Preview | Displays the number of alerts of the Urgent, Critical, Warning, and Information levels in a donut chart. On the All tab, you can view the details about alerts of all levels. You can click the Urgent, Critical, Warning, or Information tab to view the alerts of the related level. |

## 4 ASR dashboard

The disaster recovery dashboard combines charts and numbers to show the overview of the disaster recovery system. The disaster recovery dashboard can be displayed in the Normal, In Drill, and Faulty states based on the types of scheduled disaster recovery jobs.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **ASR Dashboard**.
On the **Disaster Recovery Dashboard** page, the disaster recovery dashboard is displayed based on different types of disaster recovery plans. When no disaster recovery plans are being executed, the dashboard is displayed in the
**Normal** state.
The following table describes each module on the dashboard.

| Module | Description |
|---|---|
| Alerts in the upper-left part | Displays the latest alert information of the ASR-DR console. The number of protection groups is displayed by period of time. |
| Previous jobs in the lower- left part | Displays the numbers and proportions of successful and failed jobs for switchovers, switchbacks, failovers, and failbacks on donut charts. |
| Protection information in the middle | Displays the proportions of instances in the Protecting, Unprotected, and Protect Failed states. |
| Instances in the upper-right part | Displays the protection information and synchronization latency compliance rate of cloud instances of various types. |

| Protection group synchronization delay distribution in the lower- right part | Displays the number of instances in each protection group and the distribution of maximum synchronization latencies. |
|---|---|

When drill plans are being executed, the dashboard is displayed in the **In Drill** state. The following table describes each module on the dashboard. The modules that are not listed in the table are consistent with those for the Normal state.

| Module | Description |
|---|---|
| Scheduled Job Process in the middle | Displays the failover progress of each scheduled job and the overall progress. |
| RTO of Scheduled Jobs in the lower-right part | Displays the recovery time objective (RTO) of previous jobs and scheduled jobs for which failovers are complete. |

When recovery plans are being executed, the dashboard is displayed in the **Faulty** state. The content displayed for the dashboard in the Faulty state is consistent with that in the In Drill state.

## 5 Instance management

### 5.1 Create instances

You must create instances that you want to protect in the primary and secondary sites. The number and the specifications of instances must be consistent between the primary and secondary sites.
1. Log on to the Apsara Uni-manager Management Console from the primary site. Then, log on
to the Apsara Uni-manager Management Console from the secondary site.
2. Create instances. For more information about how to create instances, see the related
topics in cloud service user guides. The following table describes the operations that you must complete and the items that you must take note of when you create instances for each cloud service.

| Service | Operation | Notes |
|---|---|---|
| ApsaraDB RDS | Create ApsaraDB RDS instances, accounts that are used to connect to the ApsaraDB RDS instances, and databases in the primary and secondary sites. | The number and the specifications of ApsaraDB RDS instances must be consistent between the primary and secondary sites. The network type of ApsaraDB RDS instances must be consistent between the primary and secondary sites. For example, the network type is Virtual Private Cloud (VPC). You do not need to create databases for ApsaraDB RDS instances in the secondary site. ASR for Geo-disaster Recovery synchronizes databases for ApsaraDB RDS instances from the primary site to the secondary site. This item does not apply to Apsara Stack Agility. We recommend that you specify instance names that can help you identify your business and facilitate maintenance. We also recommend that you use the same instance names in the primary and secondary sites. |

| PolarDB-X 1.0 | Create PolarDB-X V1.0 instances and accounts that are used to connect to the instances. Then, associate ApsaraDB RDS instances in the primary and secondary sites. | The number and the specifications of PolarDB- X V1.0 instances must be consistent between the primary and secondary sites. The network type of PolarDB-X V1.0 instances must be consistent between the primary and secondary sites. For example, the network type is VPC. We recommend that you specify instance names that can help you identify your business and facilitate maintenance. We also recommend that you use the same instance names in the primary and secondary sites. You do not need to create databases for PolarDB-X V1.0 instances in the secondary site. ASR for Geo-disaster Recovery synchronizes databases for PolarDB-X V1.0 instances from the primary site to the secondary site. |
|---|---|---|
| OSS Note On the Object Storage Service tab, the instance types in the instance list include Object Storage Service (OSS) and Cloud Defined Storage-Object Storage Service (CDS-OSS). | Create OSS buckets in the primary and secondary sites. | The number of buckets must be consistent between the primary and secondary sites. |
| ApsaraMQ | Create ApsaraMQ instances and topics in the primary and secondary sites. | The number of ApsaraMQ instances must be consistent between the primary and secondary sites. The names of ApsaraMQ topics must be consistent between the primary and secondary sites. |

| Apsara Stack DNS | Create DNS domain names and add DNS records in the primary and secondary sites. | The number of global internal domain names of DNS must be consistent between the primary and secondary sites. The record values configured in the Configure DNS Record step must be consistent between the primary and secondary sites. The value of the Smart Resolution Policy parameter must be set to Weight in the Configure DNS Record step for the primary and secondary sites. If you configure the Record Value parameter, make sure that the record for the primary site precedes the record for the secondary site. Example: master-host 100,slave-host 0. |
|---|---|---|
| DNS within Cloud | Create DNS domain names and add DNS records in the primary and secondary sites. | The number of DNS domain names and the DNS records must be consistent between the primary and secondary sites. The value of the Smart Resolution Policy parameter must be set to Weight in the Configure DNS Record step for the primary and secondary sites. Virtual IP addresses are configured for services at the primary and secondary sites. |
| MaxCompute | Create MaxCompute projects, accounts that are used to run tasks, and compute units (CUs) for the primary and secondary sites. | The number of CUs and the storage capacity must be consistent between the primary and secondary sites. The names of the MaxCompute projects and accounts that are used to run tasks must be consistent between the primary and secondary sites. The names of the DataWorks projects must be consistent between the primary and secondary sites. We recommend that you specify DataWorks and MaxCompute project names that can help you identify your business and facilitate maintenance. We also recommend that you use same project names in the primary and secondary sites. Before you synchronize incremental data, make sure that data is consistent between the primary and secondary sites. |
| KVStore for Redis | Create KVStore for Redis instances and accounts for the primary and secondary sites. | Only KVStore for Redis instances that run Redis 4.0 (Community Edition) or Redis 5.0 (Community Edition or Enhanced Edition (Tair)) are supported. You must apply for classic network endpoints for these instances. |

| ECS | Create ECS instances, EBS disks, and VPCs for the primary and secondary sites. | Only agentless high-performance disks (IO15) are supported. The CIDR blocks of VPCs where the ECS instances of the primary and secondary sites reside do not conflict with each other. Only single-data center instances are supported. |
|---|---|---|
| DataHub | Create DataHub instances for the primary and secondary sites. | The number of DataHub instances must be consistent between the primary and secondary sites. The names of DataHub topics and fields must be consistent between the primary and secondary sites. |

### 5.2 View the details of an instance

**instance**

You can view the instance details of a cloud product in the ASR for Geo-disaster Recovery console.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Instances** page, click the **Primary Region** or **Secondary Region** tab. Click a
product tab.
4. Click the
icon in the **Actions** column that corresponds to the instance and then click
**Details**.
The system displays the cloud product console.

## 6 DR for business

### 6.1 Protection Groups

#### 6.1.1 Manage protection groups

You can create, modify, or delete a protection group. You can also add instances to the protection group, view the details of the protection group, and enable reprotection for the protection group.
1. Log on to the ASR-DR console. For more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.

| Parameter | Description |
|---|---|
| Protection Group Status | The status of the protection group. Valid values: Plan Failed: A step for the scheduled job failed to be run. Running Plan: All plans associated with the protection group are being run. Protection Failed: The protection group fails to be created. You can recreate the protection group for the specified instance. Protecting: The link for the protection group is created. Starting Protection: The link for the protection group is being created. Heavy Protection: The link for the protection group is being recreated. Unknown: The system fails to obtain the status of the protection group. Stop: The protection group is stopped. |
| Synchronization Direction | The direction for the protection group. You can determine the data center in which the instances that provide services are deployed based on the direction. Valid values: Forward: The instances that provide services are deployed in the primary cloud. Backward: The instances that provide services are deployed in the secondary cloud. |

| Maximum synchronization delay | The maximum synchronization latency for all entities in the protection group. |
|---|---|

3. Click the
icon in the **Actions** column that corresponds to a protection group to perform the following operations: Click **Details** to view the details of the protection group and manage the instances that are added to the protection group. For more information, see Protection group details. Click **Modify** to modify the name and description of the protection group. Click **Add entity** to add instances to the protection group. For more information, see Add synchronization entities. Click **Modify Drill Metrics** to configure the expected values of metrics such as the data synchronization latency, switchover duration, and switchback duration. Click **Perform Reprotection** to enable reprotection for the protection group that is in the Protection Failed state. Click **Stop Protection** to temporarily stop the synchronization of a protection group or entity.

> **Note:** You cannot delete protection groups that are associated with recovery plans or drill plans.
> After a protection group is deleted, the hot backup channels between the primary and secondary entities of all resources in the protection group are deleted one after another. Cross-cloud synchronization between the primary and secondary entities stops. One-to-one mappings are also deleted.

Click **Delete** to delete a protection group that you no longer require.

##### 6.1.1.1 Create a protection group

A protection group is a group of resources on which disaster recovery is implemented in the ASR-DR console. You can create a protection group for a set of related resources used by an application.

**Background information**

We recommend that you create no more than 20 protection groups.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, click **Create**.
4. On the **Create Protection Group** page, configure the parameters. The following table
describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Region Information Note The Region Information section displays the information about the secondary region. | Organization | Select the organization to which the protection group data belongs. |
|   | Resource Set | Select the resource set to which the instance for disaster recovery belongs. |
|   | Region | Select the region of the secondary site to which the protection group belongs. |
| Production Cloud Information | Production Cloud Instance | This parameter is automatically specified by the system. You do not need to specify this parameter. |
|   | Primary Region | Select the region of the primary site where the cloud service instance to be protected by the protection group resides. |
|   | Name | The name of the protection group. You can specify a custom name. The name must be 4 to 20 characters in length and can contain only letters, digits, hyphens (-), underscores ( ), and _ periods (.). |

| Protection Group Information |   |   |
|---|---|---|
|   | Synchronization Direction | The direction in which services are failed over. If services are provided by the instances at the primary site, select Forward. If services are provided by the instances at the secondary site, select Backward. Note The synchronization direction for the protection group changes based on the completion of failovers and failbacks. After failovers are complete, Forward changes to Backward. After failbacks are complete, Backward changes to Forward. |
|   | Description | The description of the protection group for easy identification. |

5. Click **OK**. On the **Protection Groups** page, find the protection group that you created,
click the icon in the Actions column, and then click **Add entity**.
6. Follow the on-screen instructions to add synchronization entities.

> **Note:** For more information about how to add synchronization entities for each cloud service, see Add a synchronization entity.
> If you select **Add and Not Start**, the protection group enters the Stopped state after it is created. In this case, no synchronization link is created in the background, and only the **Start Protection Group** operation can be performed on this protection group. If you do not select this check box, the protection group automatically enters the protected state after it is created.

7. Click **OK**. The protection group is created. On the Protection Groups page, click the
icon to refresh the status of the protection group.

##### 6.1.1.2 Perform reprotection

After a failover, the state of a protection group becomes Protect Failed regardless of the state of the primary cloud. In this case, you must perform reprotection for the protection group.

**Prerequisites**

The state of a protection group is Protect Failed after a failover. If the state of a protection group is Protect Failed during initialization, reprotection is not supported.

**Procedure**

1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Select **Protect Failed** from the **Protection Group Status** drop-down list. Click **Search**.
4. In the list of protection groups, find the required protection group, click the
icon in the Actions column, and then click **Reprotection**.
5. In the dialog box that appears, click **OK**.

##### 6.1.1.3 Protection group details

You can view the details and operation history of a protection group, and manage the instances and associated plans in the protection group.

###### 6.1.1.3.1 View the details of a protection group

You can view the details of a protection group to monitor protection entities in the protection group. The details include the synchronization latency information and inspection information about the protection entities.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Find the protection group whose details you want to view, click the
icon in the Actions column, and then click **Details**.

| Parameter | Description |
|---|---|
| Status | The following entity states are provided: Protection Started Protection Failed Protected Plan Executed Tightly Protected Plan Failed Stopped Unknown |

| Synchronization Policy | The following synchronization policies are provided: Full: Each time you implement disaster recovery, all existing data is synchronized to the instances in the secondary cloud. Incremental: Only incremental data is synchronized to the instances in the secondary cloud. |
|---|---|
| Priority | The priority specified for the entity in the protection group. |
| Synchronization Direction | The direction in which data is synchronized. Forward indicates that instances in the primary cloud provide services. Backward indicates that instances in the secondary cloud provide services. |
| Initialization Progress | The percentage of synchronized data during the initialization of the entity. |
| Synchronization Latency | The synchronization latency of the entity. |
| RPO Obtained At | The time at which the recovery point objective (RPO) is calculated. The RPO is a metric for synchronization latency. |

4. On the **Protection Group Details** page, find the required entity and click the
icon in the Actions column. Then, you can perform the following operations: Click **Details**. On the Entity Details page, you can view the following information about the instances in the primary cloud and the secondary cloud: basic information, monitoring information about synchronization latency, information about additional configurations, and information about availability inspection.

> **Note:** By default, the entity inspection feature is disabled. You can enable the feature in the background. We recommend that you evaluate potential impacts on your services before you enable the feature.

The parameters for basic information and additional configurations vary based on the services of the instances. The following table describes the parameters on the **Entity**
**Details** page by service.

| Service | Parameter | Description |
|---|---|---|
| ApsaraDB RDS | Configure Privileged Account | The username and password of the privileged account for the primary and secondary ApsaraDB RDS instances. |
|   | Filtered Tables | The databases and tables that do not need to be protected. You can select these databases and tables for ApsaraDB RDS in the primary cloud when you create a protection group. |
|   | Read-only Account | The accounts on which ASR for Geo-disaster Recovery has read-only permissions. The accounts are specified when you create the protection group. |
|   | Start Offset for Incremental Synchronization | The offset from which the system starts to synchronize incremental data. |
|   | Configure Privileged Account | The username and password of the privileged account for the primary and secondary PolarDB for Oracle clusters. |

| Stack Resilience |   |   |
|---|---|---|
| PolarDB for Oracle |   |   |
|   | Synchronized Table | The databases, schemas, or tables that you want to synchronize. |
|   | Start Offset for Incremental Synchronization | The offset from which the system starts to synchronize incremental data. |
| PolarDB-X | Configuration Information | The password that is used to log on to the PolarDB-X instance from the secondary cloud. |
|   | Filtered Tables | The databases and tables that do not need to be protected. You can select these databases and tables for PolarDB-X in the primary cloud when you create a protection group. |
|   | Read-only Account | The accounts on which ASR for Geo-disaster Recovery has read-only permissions. The accounts are specified when you create the protection group. |
|   | Start Offset for Incremental Synchronization | The offset from which the system starts to synchronize incremental data. |
| AnalyticDB for MySQL V3.0 | Configure Account for Synchronization | The username and password for the account that is used for synchronization between the primary and secondary instances. |
|   | Start Offset for Incremental Synchronization | The offset from which the system starts to synchronize incremental data. |
| Message Queue | Configure Topic | The list of topics that you want to synchronize. |
| DNS (Multicloud Integration) | Top-level Domain (TLD) | The global domain name that is managed in ASR for Geo- disaster Recovery. |
|   | Record Value | The DNS record. |
| ment Version: 20250618 | 3 |   |

| Geo-disaster User Guide· business |   |   |
|---|---|---|
|   | TTL | The time-to-live (TTL) value of the DNS record. |
| MaxCompute | MaxCompute Mapping for Synchronization | The MaxCompute projects that you want to synchronize. |
|   | Synchronization Policy | The data synchronization policy of the MaxCompute instance. |
| ApsaraDB for MongoDB | Synchronization Policy | The data synchronization policy of ApsaraDB for MongoDB. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|   | Configure Read-only Account | If some ApsaraDB for MongoDB accounts are read- only and you do not want them to be granted read/write permissions during a failover, you can configure this parameter to filter the read-only accounts. |
|   | Configure Shard Account | The names and passwords of the shard accounts for instances at the primary and secondary sites. |
| Elastic Compute Service (ECS) | Synchronization Policy | The data synchronization policy of ECS. |
|   | Select a cloud site pair | The site pair that is created in advance in Hybrid Disaster Recovery (HDR). |
|   | Select a zone | The information about the zone that can be used by the primary cloud and the secondary cloud. |
|   | Network Settings | The VPCs, vSwitches, and protection groups where the ECS instances in the primary cloud and the secondary cloud reside. |
|   | > Document Version: 2025061 |   |

|   | Select an HDR protection group | The protection group to be failed over. |
|---|---|---|
|   | Synchronization Policy | The data synchronization policy of KVStore for Redis. |
| KVStore for Redis |   |   |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|   | Configure Read-only Account | If some KVStore for Redis accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can use this parameter to filter the read-only accounts. |
| DNS within Cloud | Synchronization Policy | The data synchronization policy of the DNS within Cloud instance. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|   | TTL | The period of time during which domain name resolution information can be retained in DNS within Cloud. |
|   | Smart Resolution Policy | Only Weight is supported. |
|   | Record Value | The weight policy in the following format: the IP address to which the domain name maps, space, and weight (0 to 999). You can find the IP address in the Record Value field of Basic Settings. For more information about domain names, see Global internal d omain names in Apsara Stack DNS User Guide. |

The check items vary based on the services of the instances. The following table describes the check items on the **Entity Inspection** page by service.

| Service | Check item |
|---|---|
| Apsara Stack DNS | Check whether the dnsService domain name can be resolved. |
|   | Check whether dnsService ICMP packets can be received. |
|   | Check whether dnsService can be connected. |
|   | Check whether access by using dnsService api : ObtainGlobalAuthZoneListRequest is normal. |
|   | Check whether access by using dnsService api : GetInstance is normal. |
| TableStore | Check whether the ots-ocm domain name can be resolved. |
|   | Check whether ots-ocm ICMP packets can be received. |
|   | Check whether ots-ocm can be connected. |
|   | Check whether access by using ots api : GetInstance is normal. |
|   | Check whether access by using ots api : Client DescribeTable is normal. |
| MaxCompute | Check whether the odps-bcc domain name can be resolved. |
|   | Check whether odps-bcc ICMP packets can be received. |
|   | Check whether odps-bcc can be connected. |

|   | Check whether access by using odps api : GetProtectGroupRequest is normal. |
|---|---|
|   | Check whether access by using odps api : listDataworkInstancesRequest is normal. |
|   | Check whether access by using odps api : GepPlanRequest is normal. |
| OSS | Check whether the oss-chiji domain name can be resolved. |
|   | Check whether oss-chiji ICMP packets can be received. |
|   | Check whether oss-chiji can be connected. |
|   | Check whether access by using oss api : GetOcmBucketMetaXmlRequest is normal. |
|   | Check whether access by using oss api : GetLocationListRequest is normal. |
| PolarDB-X | Check whether the drds-manager domain name can be resolved. |
|   | Check whether drds-manager ICMP packets can be received. |
|   | Check whether drds-manager can be connected. |
|   | Check whether access by using drds api : DescribeInstanceAccountsRequest is normal. |
|   | Check whether access by using drds api : DescribeDrdsInstanceRequest is normal. |
|   | Check whether access by using drds api : DescribeInstanceState is normal. |
| ment Version: 20250618 | 3 |

|   | Apsara Stack Resilienc |
|---|---|
|   | Check whether the rds-yaochi domain name can be resolved. |
|   | Check whether rds-yaochi ICMP packets can be received. |
| ApsaraDB RDS |   |
|   | Check whether rds-yaochi can be connected. |
|   | Check whether access by using rds api : DescribeAccountsRequest is normal. |
|   | Check whether access by using rds api : DBInstanceIPArrayListRequest is normal. |
|   | Check whether access by using rds api : DescribeDatabases is normal. |
|   | Check whether access by using rds api : getInstance is normal. |
|   | Check whether access by using rds api : getDBInstanceNetInfo is normal. |
| AnalyticDB for MySQL V3.0 | Check whether the adb3 domain name can be resolved. |
|   | Check whether adb3 ICMP packets can be received. |
|   | Check whether adb3 can be connected. |
|   | Check whether access by using ad3 api : getLinkState is normal. |
|   | Check whether access by using ad3 api : getInstanceReplild is normal. |
|   | Check whether access by using ad3 api : isInstanceEmpty is normal. |

|   | Check whether access by using ad3 api : getInstanceInfo is normal. |
|---|---|
|   | Check whether access by using ad3 api : getPhysicallpList is normal. |
|   | Check whether access by using ad3 api : getClassicNetInfo is normal. |
|   | Check whether access by using ad3 api : getNetInfo is normal. |
|   | Check whether access by using ad3 api : listAdb3Instances is normal. |
| Message Queue | Check whether the mq domain name can be resolved. |
|   | Check whether mq ICMP packets can be received. |
|   | Check whether mq can be connected. |
|   | Check whether access by using mq api : listInstances is normal. |
|   | Check whether access by using mq api : queryTaskStatus is normal. |
|   | Check whether access by using mq api : listGroups is normal. |
|   | Check whether access by using mq api : listTopics is normal. |
|   | Check whether access by using mq api : listConsumerGroups is normal. |
|   | Check whether access by using mq api : getBaseInstance is normal. |

When an entity fails to be protected because the entity fails to be connected to the underlying services due to errors such as network errors, click **Reprotection**. The system checks the protection state and determines the next state based on the query result. When changes are made to the tables of Tablestore instances or databases of the primary and secondary ApsaraDB RDS instances, entities fail to be protected. For more information about recovery methods, see What do I do if entities fail to be protected?

###### 6.1.1.3.2 View the logs of a protection entity

You can view the logs of a protection entity to help find and analyze the causes of protection failures.

**Procedure**

1. Log on to the ASR-DR console
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, click the name of the desired protection group. You can also
click the icon in the Actions column of the desired protection group and click **Details**.
4. On the **Protection Group Details** page, find the desired instance, click the
icon in the Actions column, and then click **View Logs**.

| Parameter | Description |
|---|---|
| Real-time Update | After you turn on Real-time Update, the logs of the instance are updated every 10 seconds. |
| Log Entries | The number of log entries that you want to display on the current page. Valid values: 100, 500, and 1000. |
| Log Level | The log level. Valid values: Message Error Warning |
| Server | The node where the protection entity runs. |

###### 6.1.1.3.3 View the operations records of a protection group

**protection group**

This topic describes how to view the historical operations records of a protection group.
1. Log on to the Apsara Stack Resilience for Disaster Recovery (ASR-DR) console
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. On the Protection Groups page, click the name of the desired protection group. You can also
find the desired protection group, click the icon in the Actions column, and then click
**Details**.
4. On the **Protection Group Details** page, click the **Operation History** tab.
5. To view the historical operations records of the protection group, click **Details** in the
**Actions** column.

###### 6.1.1.3.4 Delete a protection entity

You can remove instances from a protection group if the instances no longer require protection implemented based on disaster recovery (DR). After the instances are removed, the instances are no longer protected, and the related link for DR is interrupted.
1. Log on to the Apsara Stack Resilience for Disaster Recovery (ASR-DR) console
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. On the **Protection Groups** page, click the name of the desired protection group. You can
also find the desired protection group, click the icon in the **Actions** column, and then click **Details**.
4. On the **Protection Group Details** page, click the **Protection Entity** tab.
5. Find the instance that you want to delete, click the
icon in the **Actions** column, and then click **Delete**.
6. In the dialog box that appears, click **OK**.

###### 6.1.1.3.5 Modify the attribution of a protection entity

**entity**

You may need to adjust the business to which an instance belongs. You may select an unnecessary instance when you create a protection group. In these scenarios, you can modify the attribution of the instances in a protection group and move the instances to another protection group.
1. Log on to the Apsara Stack Resilience for Disaster Recovery (ASR-DR) console
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. On the **Protection Groups** page, click the name of the desired protection group. You can
also find the desired protection group, click the icon in the **Actions** column, and then click **Details**.
4. On the **Protection Group Details** page, find the desired instance, click the
icon in the
**Actions** column, and then click **Migrate Entity**.
5. Select a new protection group and click **OK**.

> **Note:** Make sure that the primary and secondary organizations, synchronization direction, and synchronization policy are consistent between the protection group that you select and the previous protection group.

###### 6.1.1.3.6 Modify the read-only account of an ApsaraDB RDS instance

**ApsaraDB RDS instance**

If some ApsaraDB RDS accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can filter the read-only accounts.

**Prerequisites**

Only ApsaraDB RDS and PolarDB-X instances support this operation.

**Procedure**

1. Log on to the Apsara Stack Resilience for Disaster Recovery (ASR-DR) console
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. On the Protection Groups page, click the name of the desired protection group. You can also
find the desired protection group, click the icon in the Actions column, and then click
**Details**.
4. On the **Protection Group Details** page, find the desired instance, click the
icon in the Actions column, and then click **Modify Permission Granted to Read-only Account** .
5. In the **Update Permission Granted to Read-only Account** dialog box, select a database
from the Database drop-down list and enter an account name.
6. Click **OK**.

###### 6.1.1.3.7 Modify the privileged account of an ApsaraDB RDS instance

**ApsaraDB RDS instance**

If the privileged account and password of an ApsaraDB RDS instance is modified in the ApsaraDB RDS console, you must modify the privileged account and password of the instance in the Apsara Stack Resilience for Disaster Recovery (ASR-DR) console.

**Prerequisites**

Only ApsaraDB RDS instances, PolarDB-X instances, and PolarDB for Oracle clusters support this operation.

**Procedure**

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. On the **Protection Groups** page, click the name of the desired protection group. You can
also find the desired protection group, click the icon in the **Actions** column, and then click **Details**.
4. On the **Protection Group Details** page, find the desired instance, click the
icon in the
**Actions** column, and then click **Modify Privileged Account**.
5. In the **Modify Privileged Accounts for Primary and Secondary Instances** dialog box,
specify the username and password for the instances at the primary and secondary sites, and click **Modify**.

###### 6.1.1.3.8 Modify table filtering

If you add databases or tables that do not require disaster recovery to the instance in a protection group, you must modify table filtering.

**Prerequisites**

The instance is either an ApsaraDB RDS instance or a PolarDB-X instance.

**Procedure**

1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Click the name of the protection group. You can also click the
icon in the Actions column which corresponds to the required protection group and click **Details**.
4. On the **Protection Group Details** page, click the
icon in the **Actions** column which corresponds to the required instance and click **Modify Filtered Table**.
5. In the **Update Filtered Table** dialog box, specify the databases and tables that do not
need disaster recovery in the primary site instance, and then click **OK**.

###### 6.1.1.3.9 Manage protection entity account permissions

**permissions**

The Manage Accounts feature allows you to view and modify the permissions of the accounts that are used to log on to the primary instance and secondary instance. This helps you manage instances with ease.

**Prerequisites**

The instance is either an AsparaDB RDS instance or a PolarDB-X instance.

**Procedure**

1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Click the name of the protection group that you want to manage. You can also click the
icon in the **Actions** column that corresponds to the protection group and click
**Details**.
4. On the **Protection Group Details** page, click the **Protected Entity** tab. Find the instance
that you want to manage, click the icon in the **Actions** column, and then click
**Account Management**.
5. On the **Manage Accounts** page, view and modify the read-only permissions or read and
write permissions of database accounts that are used to log on to the primary instance and secondary instance.

##### 6.1.1.4 Add a synchronization entity

After you create a protection group, you must add instances to the protection group before disaster recovery can be implemented. Limits on the number of instances: The maximum total number of instances in all protection groups is 200. The default maximum total number of protected database instances is 60, including ApsaraDB RDS instances associated with PolarDB-X instances, standalone Apsara RDS instances, ApsaraDB for Redis instances, and ApsaraDB for MongoDB instances. If more than 60 database instances need to be protected, DTS needs to be scaled out, so that a maximum of 100 database instances can be protected. The maximum number of protected ApsaraDB for HBase instances is 20. The maximum number of protected Object Storage Service (OSS) buckets is 20. The maximum number of protected Tablestore instances is 20. The maximum number of protected Elastic Compute Service (ECS) instances is 50. The maximum number of protected Message Queue instances is 20. The maximum number of protected Apsara Stack DNS instances is 20. The maximum number of protected MaxCompute projects is 20. The maximum number of protected DataHub instances is 20.

###### 6.1.1.4.1 ApsaraDB RDS

This topic describes how to configure disaster recovery for ApsaraDB RDS, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An ApsaraDB RDS instance is created on the primary and secondary cloud instances in the Apsara Uni-manager Management Console. | Full synchronization scenarios: The primary cloud instance has a database that is to be synchronized. The secondary cloud instance has a database with the same name as the database in the primary cloud instance, but the database does not have tables. If the secondary cloud instance has databases or tables other than the database or table to be synchronized, you must configure the databases or tables in Filtered Tables. Incremental synchronization scenarios: Both the primary and secondary cloud instances have the database and table to be synchronized, and the database name and table name in the primary and secondary cloud instances are the same. If the secondary cloud instance has databases or tables other than the database or table to be synchronized, you must configure the databases or tables in Filtered Tables. The ApsaraDB RDS instance is not associated with a PolarDB-X instance. |
| Internal and public endpoints are obtained for the primary and secondary cloud instances. | For more information, see "Instances" in ApsaraDB for RDS User Guide. |

| A privileged account and a standard account are created for each of the primary and secondary cloud instances. | For more information, see "Accounts" in ApsaraDB for RDS User Guide. |
|---|---|
| A RAM role for Data Transmission Service (DTS) is created for the organization to which the instances belong. | For more information, see Create a RAM role. |

**Procedure**

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then select **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **ApsaraDB**
**RDS** tab in the **Instance Type** section. In the left-side entity list, select the desired
instance IDs, click the icon to move the instances to the right-side entity list, and then click **Next**.

> **Note:** You cannot configure synchronization entities for read-only instances. Read-only instances are not displayed in the entity list.

5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configurati on step | Parameter | Description |
|---|---|---|
|   | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |

|   | Synchronization Policy | Full + Incremental: The following data is synchronized: all historical data that is generated before the synchronization task is created and data that is generated after the synchronization task is created or from the specified start offset. Incremental: Only data that is generated after the synchronization task is created or from the specified start offset is synchronized. Note The MySQL engine allows you to specify a start offset for incremental data synchronization. The PolarDB engine does not allow you to specify a start offset for incremental data synchronization. |
|---|---|---|
| Basic Settings |   |   |
|   | (Optional) Start Offset for Incremental Synchronization | This parameter is required if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR- DR starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the source entity at the primary site. |

| Configure Privileged Account | Primary Instance Account and Secondary Instance Account | The privileged account names and passwords of the primary and secondary instance databases. If you have created a privileged account in the ApsaraDB RDS console, enter that privileged account and password. If no privileged account is created in the ApsaraDB RDS console, ASR-DR creates a privileged account based on the username and password that you enter. Note Privileged accounts are used only to manage the access of standard accounts. If no privileged account exists, ASR-DR automatically creates a privileged account. However, if no privileged account exists for a PolarDB for Oracle cluster, you must manually create a privileged account and use the privileged account as a synchronization account. After you create the account, the password of the account cannot be changed. The name of the standard account for the ApsaraDB RDS instance in the primary cloud must be the same as the name of the standard account for the ApsaraDB RDS instance in the secondary cloud. If the names are different, ASR-DR does not manage these accounts. |
|---|---|---|

| (Optional) Configure Table Filtering | Database and Configure Table Filtering | Databases and tables that do not need to be protected by disaster recovery in ApsaraDB RDS at the primary site or the secondary site. Note If you enter an asterisk (*) in the Configure Table Filtering field, the current database is filtered out. You can also select Filter Database to filter out the current database. |
|---|---|---|
| Select Tables | Enable Database Account Synchronization | After you turn on this switch, the database-related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of passwords, and deletion of accounts. |
| Configure Read-only Account | Database and Read-only Account | The database and the related account of the ApsaraDB RDS instance at the primary or secondary site. During a failover, ASR-DR grants the ApsaraDB RDS account read/write permissions by default. If some ApsaraDB RDS accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can configure this parameter to filter out the read-only accounts. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.2 PolarDB-X V1.0

This topic describes how to configure disaster recovery for PolarDB-X V1.0 instances, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A PolarDB-X instance is created for each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | The PolarDB-X instances on the primary and secondary cloud instances are associated with the same number of ApsaraDB RDS instances. The PolarDB-X instance on the secondary cloud instance does not contain any databases. The specifications of PolarDB-X instances are consistent between the primary and secondary cloud instances. The ApsaraDB RDS instances associated with the PolarDB-X instances on the primary and secondary cloud instances are not associated with other PolarDB-X instances. Data Definition Language (DDL) changes to tables and databases cannot be synchronized. A RAM role for Data Transmission Service (DTS) is created. For more information, see Create a RAM role.Create a RAM role |
| A database is created for the instance at the primary site. | The database contains tables to be synchronized, and the tables are checked. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then click **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **PolarDB**
tab in the **Instance Type** section. In the left-side entity list, select an instance ID, click the icon to move the instance to the right-side entity list, and then click **Next**.

> **Note:** You cannot configure synchronization entities for read-only instances. Read-only instances are not displayed in the entity list.

5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then select **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|   | (Optional) Start Offset for Incremental Synchronization | This parameter is required if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR-DR starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |

| (Optional) Configure Table Filtering | Database and Configure Table Filtering | Databases and tables that do not require disaster recovery protection in the PolarDB-X instance at the primary site. Note If you enter an asterisk (*) in the Configure Table Filtering field, the current database is filtered out. You can also select Filter Database to filter out the current database. |
|---|---|---|
| Synchronization Object | Enable Database Account Synchronization | Important In V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After you turn on this switch, the database- related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one at the destination site, change of passwords, and deletion of accounts. |
| Configure Password | Password | The password of the PolarDB-X database at the secondary site. |
| (Optional) Configure Read- only Account | Database and Read- only Account | The database and the corresponding account on the PolarDB-X instance at the primary site. During a failover, ASR-DR automatically grants this account read/write permissions by default. If some PolarDB-X accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can use this parameter to filter out these read-only accounts. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.3 OSS

This topic describes how to configure disaster recovery for Object Storage Service (OSS) or CDS-OSS, including the prerequisites and procedure.

**Background information**

OSS is divided into OSS 1.0 and CDS-OSS. OSS 1.0 is the original OSS service, CDS-OSS is a new service form known as cloud-defined storage. You must select the corresponding CDS- OSS cluster when you create a CDS-OSS resource. Unless otherwise specified, the descriptions in this topic apply both to OSS 1.0 and CDS-OSS.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An OSS or CDS-OSS instance is created on each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | The secondary instance must be empty in full protection scenarios. The maximum number of protected OSS buckets is 20. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then click **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Object**
**Storage Service** tab in the **Instance Type** section. In the left-side entity list, select the
desired instance ID, click the icon to move the instance to the right-side entity list, and then click **Next**.
5. On the **Configure Priority and Resource Mapping** page, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. Configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|

| Basic Settings | Priority | The priority based on which ASR- DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. Note You cannot specify a start offset for incremental synchronization. |
|   | Synchronization Object | You can leave this parameter empty to synchronize all files or specify a prefix to synchronize files with the prefix. Note The prefix cannot start with a forward slash (/). Separate prefixes with commas (,). You cannot modify the prefix of the synchronization entity after you specify it. |
|   | Synchronization Policy | Set Synchronization Policy to Add/Change or Add/Delete/Change. |
|   | > Document Version: 2025061 |   |

|   | Resource Mapping | Select the destination entity at the secondary site. The entity is used as the hot standby resource of the primary site entity. |
|---|---|---|

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protect Failed state, click **Reprotection**.
> For OSS, when you create a full protection group, you must wait about 90 to 110 minutes before full synchronization actually starts due to product limits.

###### 6.1.1.4.4 Big data products

This topic describes how to configure disaster recovery for DataWorks and MaxCompute synchronization entities, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A DataWorks instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console. | Both primary and secondary DataWorks instances have MaxCompute projects and compute units (CUs). Both primary and secondary DataWorks workspaces have the same name. |
| A MaxCompute instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console. | The organization of the cloud account used to execute jobs, number of CUs, storage space of MaxCompute projects, and engine names must be consistent between the primary and secondary MaxCompute projects. The maximum number of protected MaxCompute projects is 20. |

**Procedure**

The procedure of configuring disaster recovery for MaxCompute and that for DataWorks are similar. MaxCompute is used in the following example.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Find the desired protection group, click the
icon in the **Actions** column, and then select
**Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the
**MaxCompute** tab in the **Instance Type** section. In the left-side entity list, select the
instance IDs, click the icon to move the instances to the right-side entity list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller number indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: synchronizes new data after the synchronization task is created. Note MaxCompute does not support synchronizing new data from a specific offset. |
|   | > Document Version: 2025061 |   |

|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|---|---|---|
| MaxCompute Mapping for Synchronization | Source MaxCompute Project and Destination MaxCompute Project | The MaxCompute projects to be synchronized in DataWorks. Note The source project names must be the same as the destination project names in cross-cloud disaster recovery scenarios. |
|   | Synchronization Policy Configurations | Filters out tables, resources, and functions for synchronization. |
| Configure Policy | Timing trigger synchronization | The point in time to trigger synchronization every day. |
|   | Callback Method | The callback method. You can select Manual Business or Manual Business Process. |
|   | Callback Node ID | The ID of the callback node. |
|   | Synchronization Policy for DataWorks Project | The resources to be synchronized from the DataWorks project and the ID of the callback node after the synchronization is triggered. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the state is Protect Failed, click **Reprotection**.

###### 6.1.1.4.5 DNS (Multicloud Integration)

This topic describes how to configure disaster recovery for the synchronization entities of DNS (Multicloud Integration), including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| The DNS control domains are merged. | The disaster recovery of Apsara Stack DNS ensures the global consistency of domain name resolution through cluster synchronization. In this solution, the tenant-side DNS server serves as a global server loading balancer (GSLB) to route the traffic that is destined for the primary data center to the secondary data center when a fault occurs. The DNS control domains of the primary and secondary data centers are merged to form a Raft cluster to ensure that the domain names in the cluster are consistent. You can specify the weights of the domain names to implement traffic switchover. For information about how to merge control domains, see the ASR-DR O&M Guide. |
| The same global domain names and host records are created in the Apsara Uni-manager Management Console at the primary and secondary sites. | The maximum number of protected DNS instances is 20. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then select **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **DNS**
**(Multicloud Integration)** tab in the **Instance Type** section. Specify a domain name,
select a host record in the left-side list, click the icon to move the host record to the right-side list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then select **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Note The priority for DNS (Multicloud Integration) can be set only to 1. |
|   | Synchronization Policy | DNS (Multicloud Integration) supports only Full + Incremental. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Select Domain Name | The DNS domain name that you want to protect. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Configure DNS Record | Host Record | The DNS resolution record. For more information, see "Global internal domain names" in Apsara Stac k DNS User Guide. |
|   | Record Type | CNAME- maps one domain name to another and A- maps a domain name to an IPv4 address are supported. |
|   | TTL | The period during which domain resolution information is retained in DNS (Multicloud Integration). |
|   | Smart Resolution Policy | Only Weight is supported. |

|   | Record Value | Specify a weight policy in the following format: the domain name (fully qualified domain name with a period), space, and weight (0 to 999). For more information about domain names, see Global inter nal domain names in Apsara Stack DNS User Guide. Important Make sure that the domain name of the primary data center precedes the domain name of the secondary data center. |
|---|---|---|

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.6 DNS within Cloud

This topic describes how to configure disaster recovery for the synchronization entities of DNS within Cloud. During failovers, ASR-DR adjusts the DNS weights that correspond to the virtual IP addresses in global internal domain names.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group to which you want to add a
synchronization entity, click the icon in the **Actions** column, and then select **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **DNS**
**within Cloud** tab in the **Instance Type** section. Specify a domain name, select a host
record in the left-side list, click the icon to move the host record to the right-side list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then select **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Note The priority for DNS within Cloud can be set only to 1. |
|   | Synchronization Policy | DNS within Cloud supports only Full + Incremental. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Select Domain Name | The DNS domain name that you want to protect. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Configure DNS Record | Host Record | The DNS resolution record. |
|   | Record Type | CNAME- maps one domain name to another and A- maps a domain name to an IPv4 address are supported. |
|   | TTL | The period during which domain resolution information is retained in DNS within Cloud. |
|   | Smart Resolution Policy | Only Weight is supported. |

|   | Record Value | Specify a weight policy in the following format: the IP address to which the domain name maps, space, and weight (0 to 999). You can find the IP address in the Record Value field of Basic Settings. For more information about domain names, see "Global internal domain names" in Aps ara Stack DNS User Guide. Important Make sure that the domain name of the primary data center precedes the domain name of the secondary data center. |
|---|---|---|

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

8. Optional. Modify a DNS resolution record. If the DNS resolution record is inconsistent
between the primary data center and secondary data center, perform the following steps: i. On the Instances page, find the desired domain name, click the icon in the Actions column, and then select **View Details** to go to the **Global Domain Names** page of the DNS within Cloud console. ii. Find the desired domain name, click **Configure DNS Record** in the **Actions** column, and then click **Modify** in the **Actions** column on the page that appears. iii. In the Modify DNS Record dialog box, modify the weight values in the **Record Values** section and click **OK**. Wait about 1 minute for the modifications to take effect.

###### 6.1.1.4.7 Message Queue

This topic describes how to configure disaster recovery for Message Queue, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|

| A Message Queue instance, a topic, and a group are created on each of the primary and secondary cloud instances by using the Apsara Uni- manager Management Console. | The Message Queue instances on the primary and secondary cloud instances have the same name, topic, and group. When you create the instances, the default settings are retained except the instance name and description. The maximum number of protected Message Queue instances is 20. |
|---|---|

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then click **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Message**
**Queue** tab in the **Instance Type** section. In the left-side entity list, select the instance IDs,
click the icon to add the instances to the right-side entity list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then select **Configure**. Configure **basic settings** and **select a topic** based on your business requirements, and then click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller number indicates a higher priority. Note The priority for Message Queue can be set only to 2. |

|   | Synchronization Policy | Only Incremental is supported for Message Queue. Incremental means that only incremental data is synchronized to the instances at the secondary site. The synchronization starts when the synchronization entity is created. Note Message Queue does not support synchronizing new data from a specific offset. |
|---|---|---|
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Select a topic | Topic Name | The topics to be protected at the primary site. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.8 KVStore for Redis

This topic describes how to configure disaster recovery for KVStore for Redis, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A KVStore for Redis instance is created on each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | In full synchronization scenarios, the primary KVStore for Redis instance can have data, but the secondary KVStore for Redis instance cannot have data. |

| An internal endpoint is obtained for each of the primary and secondary KVStore for Redis instances. | For more information, see "Instance management" topics in KVStore for Redis User Guide. |
|---|---|
| A privileged account and a standard account are created for the primary and secondary cloud instances. | For more information, see the Instance management > Manage database accounts topic in KVStore for Redis User Guide. |
| A RAM role for Data Transmission Service (DTS) is created for the organization to which the instances belong. | For more information, see Create a RAM role. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group, click the
icon in the **Actions** column, and then click **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **ApsaraDB**
**for Redis** tab in the **Instance Type** section. In the left-side entity list, select an instance
ID, click the icon to move the instance to the right-side entity list, and then click
**Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configurati on step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |

|   | Synchronization Policy | Only Full + Incremental is supported. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|---|---|---|
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Synchroniz ation Object | Enable Database Account Synchronization | Important In V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After you turn on this switch, the database-related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The new account exists at the destination site. The operations of changing the password and deleting the account are not synchronized to the destination site. |
| Configure Read-only Account | Read-only Account | The database and the corresponding account on the KVStore for Redis instance at the primary or secondary site. During a failover, ASR-DR automatically grants the account read/write permissions by default. If some KVStore for Redis accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can use this parameter to filter out the read-only accounts. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group you created.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.9 ApsaraDB for MongoDB

This topic describes how to configure disaster recovery for ApsaraDB for MongoDB instances.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An ApsaraDB for MongoDB instance is created in both the primary and secondary clouds by using the Apsara Uni-manager Management Console. | Full synchronization scenarios: The primary and secondary instances contain databases to be synchronized that are named the same. Collections cannot be synchronized. Incremental synchronization scenarios: The primary and secondary instances contain databases and collections to be synchronized that are named the same. |
| Internal endpoints and external endpoints are obtained for the instances that are deployed in the primary and secondary clouds. | For more information, see the Instance management topics in ApsaraDB for MongoDB User Guide. |
| A RAM role for Data Transmission Service (DTS) is created for the organization to which the instance belongs. | For more information, see Create a RAM role. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the page that appears, find the desired protection group, click the
icon in the **Actions** column, and then select **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **ApsaraDB**
**for MongoDB** tab in the **Instance Type** section. In the left-side entity list, select the ID of
the primary site instance, click the icon to move the instance to the right-side entity list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, click the
icon in the **Actions** column of the instance and click **Configure**. Configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuratio n step | Parameter | Description |
|---|---|---|

| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|   | (Optional) Start Offset for Incremental Synchronization | This parameter is required if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR-DR starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|   | Database/Synchronizatio n Object | Select the databases and objects in the ApsaraDB for MongoDB instance to be synchronized from the primary cloud to the secondary cloud. You can also synchronize the entire instance. |

| Objects to be synchronized |   |   |
|---|---|---|
|   | Enable Database Account Synchronization | Important In Apsara Stack V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After this switch is turned on, the accounts of the databases are synchronized to the destination cloud, and incremental synchronization is performed for creation of new accounts and changes of permissions. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of password, and deletion of accounts. |
| Configure Read-only Account | Read-only Account | Select databases and accounts for the ApsaraDB for MongoDB instance in the primary or secondary cloud. During a failover, ASR-DR grants all accounts read and write permissions by default. If you do not want specific accounts to be granted write permissions, you can specify these accounts in this parameter so that the system grants them read permissions only. |
| Configure Shard Account | Shard Account for Secondary Instance/Shard Account for Primary Instance | If the instance is a sharded cluster instance, you need to specify the account username and passwords of the shards of the instance in the primary and secondary clouds. You can select Automatic Application and Manual Entry. Automatic Application: ASR-DR automatically creates accounts if no accounts have been created for the instance shards. Manual Entry: You can specify the accounts if accounts exist for the instance shards. Note The accounts are used by synchronization components to obtain oplogs on the shards. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.10 ECS

This topic describes how to configure disaster recovery for Elastic Compute Service (ECS) instances.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An ECS instance is created in the primary cloud by using the Apsara Uni-manager Management Console. A virtual private cloud (VPC) instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console. A site pair, a Hybrid Disaster Recovery (HDR) protection group, and a vSwitch are created by using HDR. | Only premium performance disks (IO15) are supported by the ECS instance. The CIDR blocks of the primary and secondary VPC instances are the same, or can be matched by mapping. For more information about HDR operations, see the HDR documentation. |

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group to which you want to add a
synchronization entity, click the icon in the **Actions** column, and then click **Add entity**.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Elastic**
**Compute Service** tab in the **Instance Type** section. In the left-side entity list, select an
instance ID of the primary site, click the icon to move the instance to the right-side entity list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configurati on step | Parameter | Description |
|---|---|---|
| Basic Settings Note When you click Next after the basic settings are configur ed, ASR- DR checks the HDR authoriz ation status of the primary and seconda ry sites. If the HDR authoriz ation is successf ul, ASR- DR creates an organiza tion mapping . | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. You can select only 3, 4, or 5. |
|   | Synchronization Policy | Only Full + Incremental is supported. |
| Select a cloud site pair | Whether to Reuse Site Pairs | If you do not want to reuse site pairs, click Next. If you want to reuse site pairs, select the corresponding cloud site pair and click Next. |

| Select a zone | Select a zone in the production cloud | Select a zone in the primary cloud. |
|---|---|---|
|   | Select a zone in the disaster recovery cloud | Select a zone in the secondary cloud. |
| Network Settings | VPC in Production Cloud | Select a VPC created in the primary cloud from the drop- down list. |
|   | vSwitch in Production Cloud | Select a vSwitch created in the primary cloud from the drop-down list. |
|   | Security Group in Production Cloud | Select a protection group created in the primary cloud from the drop-down list. |
|   | VPC in Disaster Recovery Cloud | Select a VPC created in the secondary cloud from the drop-down list. |
|   | vSwitch in Disaster Recovery Cloud | Select a vSwitch created in the secondary cloud from the drop-down list. |
|   | Security Group in Disaster Recovery Cloud | Select a protection group created in the secondary cloud from the drop-down list. |
| Select an HDR protection group | Select an existing HDR protection group | Select a protection group and click Next. |
|   | Create HDR Protection Group | Enter a protection group name, an expected synchronization delay value, and a protection group bandwidth value, and click Next. Note The protection group bandwidth value you entered must be a multiple of 8. |

6. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 6.1.1.4.11 DataHub

This topic describes how to configure disaster recovery for DataHub, including the prerequisites and procedure.

**Prerequisites**

A virtual private cloud (VPC) instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console. For more information, see Log on to the
ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the desired protection group, click the
icon in the
**Actions** column, and then click **Add entity**.
4. In the Select Instances step of the **Add synchronization entity** wizard, set **Instance**
**Type** to **DataHub**.
5. In the entity list on the left, select the desired instance ID and click the
icon to add the instance to the entity list on the right. Then, click **Next**.
6. On the **Configure Priority and Resource Mapping** page, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. Configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Config | Parameter | Constraint |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value specifies a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. You can select only 3, 4, or 5. |

|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|---|---|---|
| Select Topic | Select Synchronization Mode | The mode to synchronize entities. Example: Fixed. Valid values: Fixed: Make sure that the shards at both sides are consistent. Shards are synchronized in one-to-one mode. When the primary instance is scaled up, you must stop the synchronization task and create an incremental synchronization task again. Round robin: Different numbers of shards can be _ deployed at both sides. Shard scaling does not affect synchronization tasks. Data is synchronized to all shards. |
|   | Select Topic | Select the topics and fields that you want to synchronize. You can select multiple topics and fields and they must have been created on the destination. |

7. In the **Configure Drill Metrics** step, set the **Expected Value of Maximum**
**Synchronous Latency (s)**, **Expected Value of Switchover Duration (s)**, and
**Expected Value of Switchback Duration (s)** parameters and click **Next**.
8. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

##### 6.1.1.5 Modify drill metrics

You can specify a variety of metrics to be collected as drill results. ASR-DR then provides optimization suggestions for unsatisfactory results. This helps you evaluate the performance of your enterprise disaster recovery architecture and quickly discover and solve problems.

**Prerequisites**

A protection group is created. For more information, see Create a protection group.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business > Protection Groups**.
3. On the **Protection Groups** page, set the Protection Group Name, Synchronization
Direction, and Protection Group Status parameters, and then click **Search**.
4. After the protection group that meets the conditions is displayed, click the
icon in the
**Actions** column and select **Modify Drill Metrics**.
5. In the **Modify Expected Values of Drill Metrics** dialog box, modify the values of the
parameters and click **OK**.

##### 6.1.1.6 Start a protection group

This topic describes the prerequisites, features, and procedure for starting a protection group.

**Prerequisites**

The protection group is in the **Stop** state.

**Features**

When you start a protection group, the synchronization entity information is automatically filled in and cannot be modified by default. When you configure the synchronizations, you can modify only the Synchronization Policy. Other parameters cannot be modified.

> **Important:** When the Synchronization Policy is changed from Incremental to Full, the secondary instance must have no data. Otherwise, you must manually clear the data on the secondary instance, or the verification fails.

If you start a protection group, the synchronization of all entities in the protection group starts. After the synchronization entities are started, the entities are in the **Starting Protection** state. Synchronization links are created and data synchronization is performed in the background. The entities enter the **Protecting** or **Protect Failed** state based on the results of subsequent jobs.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Find a protection group in the **Stop** state, click the
icon on the right of the protection group, and then click **Start Protection Group**.
4. On the **Select Instances** page, click **Next**.
5. On the **Configure Priority and Resource Mapping** page, click the
icon in the Actions column and select **Configure** to configure synchronization information.
6. After you finish configuring the synchronization information, click **Next**.

> **Note:** You can modify only the Synchronization Policy. Other parameters cannot be modified.
> When Synchronization Policy is set to Incremental, you can modify the Synchronized From parameter for ApsaraDB RDS, PolarDB-X, and AnalyticDB for MySQL. You can modify the Synchronization Object and Synchronization Policy parameters for Object Storage Service (OSS).

7. Click **OK** to start the protection group.

##### 6.1.1.7 Stop a protection group

This topic describes the scenario and procedure for stopping a protection group.

**Scenario**

If you want to temporarily stop the synchronization of a protection group or protection entity, you can stop the protection group.

> **Note:** After the protection group is stopped, the synchronization links between the primary and secondary entities stop, but the synchronization entities in the protection group still exist.
> If you stop a protection group, the synchronization of all entities in the protection group stops.
> For a stopped protection group, you can perform only the **Start Protection Group** operation. You can query the information of the synchronization entities, such as **Details** and **Logs**.
> A stopped protection group can be used to create plans, but the created plans cannot be started.

**Prerequisites**

The protection group is in the Protection Failed or Protecting state. The protection group is not involved in a running drill plan or recovery plan.
1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. In the list of protection groups, click the
icon on the right of the protection group that you want to stop and then click **Stop Protection**.
4. Click the name of the protection group. Alternatively, click the
icon in the Actions column of the protection group and then click **Details**. Confirm that the synchronization entities are in the **Stop** state.

##### 6.1.1.8 View the synchronization logs of MaxCompute

**MaxCompute**

MaxCompute logs contain more information when compared with entity logs, which helps locate and analyze the causes of protection failures.
1. Log on to the ASR-DR console. For more information, see Log on to the ASR for Geo-disaster
Recovery console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Click the
icon in the Actions column that corresponds to the required protection group and select **Details** from the shortcut menu.
4. On the **Protection Group Details** page, click the
icon in the Actions column that corresponds to the required instance and select **MaxCompute Logs** from the shortcut menu. You can view the Apsara Bigdata Manager (ABM) logs of the instance at the primary and secondary sites.

##### 6.1.1.9 Manually synchronize data

By default, data of MaxCompute and DataWorks is synchronized from the primary region to the secondary region based on the scheduled time. To immediately perform computing in the secondary region, you can manually synchronize incremental data to the secondary region.
1. Log on to the ASR-DR console. For more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Click the
icon in the Actions column that corresponds to the required protection group and select **Details** from the shortcut menu.
4. On the **Protection Group Details** page, click the
icon on the right of the instance and click **Synchronize Incremental Data Now**. Then, the system synchronizes the incremental data of MaxCompute and DataWorks.

#### 6.1.2 Fail over a protection group

You can fail over a protection group that you created.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.

**Procedure**

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the **Business Disaster Recovery Plan** page, enter a plan name and click
.
4. After the protection group that meets the conditions is displayed, click the
icon in the
**Actions** column and select **Start Switchover**.
5. In the dialog box that appears, select either of the following options based on your business
requirements:
**Precheck**: A pre-check is performed on the plan without the need to start the plan. This
improves the success rate of disaster recovery drills.
**End-to-End Link**: The protection group is directly failed over.
6. Click **OK**.

#### 6.1.3 Fail back a protection group

You can fail back a protection group that has been failed over.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the **Business Disaster Recovery Plan** page, enter a plan name and click
.
4. After the protection group that meets the specified condition is displayed, click the
icon in the **Actions** column and click **Start Switchback**.
5. In the dialog box that appears, select either of the following options based on your business
requirements: Precheck: You can perform a pre-check on the plan without the need to start the plan. This improves the success rate of disaster recovery drills. End-to-End Link: You can directly fail back the protection group.
6. Click **OK**.

### 6.2 Manage a plan

You can use a plan to execute a series of jobs in a protection group in sequence. The jobs can be resource switchovers and checks. You can create independent protection group switchover, switchback, failover, and failback plans. You can also create process-based drill plans and download drill reports after the drills are complete.

#### 6.2.1 Overview

Plans are categorized into drill plans and recovery plans based on whether the primary cloud fails.

**Context**

Drill plans are run when the primary and secondary clouds work as expected. Recovery plans are run when the primary or secondary cloud fails. Two failover modes are provided based on the fault level: **Minimum RTO** and **Try Minimum RPO**
**(Recommended)**. You can select a failover mode based on your business requirements.
You can also modify the failover plan to change the failover mode. Try Minimum RPO (Recommended): In this mode, a failover is performed at the primary site regardless of whether a global site fault or an application fault occurs. This helps ensure that all data at the primary site is synchronized to the secondary site. If the primary site becomes completely unavailable due to a global site fault, the primary site management interface fails to be called. In this case, this mode is ignored and the failover at the primary site is skipped. Minimum RTO: In this mode, no failover is performed at the primary site regardless of whether a global site fault or an application fault occurs. This helps ensure that services at the secondary site can be quickly restored. The system triggers a failover without waiting for the completion of data synchronization from the primary site to the secondary site. This may cause data inconsistency between primary and secondary sites. Plans can be categorized into failover or switchover plans and failback or switchback plans based on synchronization directions.

**Context**

In the failover or switchover process, resources in a protection group in the primary cloud are unavailable, and workloads are switched over to the secondary cloud. Failbacks or switchbacks are a reverse process of failovers or switchovers. In the failback or switchback process, resources in the protection group in the secondary cloud are unavailable, and workloads are switched over to the primary cloud. Failovers and switchovers are available only for a protection group whose synchronization direction is set to Forward. After a failover or switchover is performed, the synchronization direction of the protection group becomes backward. Failbacks and switchbacks are available only for a protection group whose synchronization direction is set to Backward. After a failback or switchback is performed, the synchronization direction of the protection group becomes forward.

#### 6.2.2 Manage business disaster recovery plans

**plans**

This topic describes how to create business disaster recovery plans (including drill plans and recovery plans), how to query business disaster recovery plans, and how to view the execution histories of disaster recovery plans.

##### 6.2.2.1 Create a business disaster recovery plan

This topic describes how to create a business disaster recovery plan, which includes a drill plan and a recovery plan. This topic also describes how to configure the execution steps and policies for dills or failovers and failbacks.

**Prerequisites**

A protection group is created. For more information, see Create a protection group.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the page that appears, click **Create Disaster Recovery Plan**.
4. In the **Basic Information** step, set the parameters based on the descriptions in the
following table and click **Next**.

| Section | Parameter | Description |
|---|---|---|

| DR Region Informatio n | Organizations | Select the organization to which the plan belongs from the drop-down list, which is the same as the organization selected for the current environment. If a specific organization has been selected for the environment and the organization does not have subordinate organizations, the organization is automatically specified in the drop-down list. If the root organization or another organization that has subordinate organizations is selected for the environment, you must select a specific organization from the Organizations drop-down list. |
|---|---|---|
|   | Resource Set | Select the resource set to which the instance belongs from the drop-down list, which is the same as the resource set selected for the environment. If a specific resource set has been selected for the environment, the resource set is automatically specified in the drop-down list. If all resource sets of the current organization are selected for the environment, you must select a specific resource set from the Resource Set drop- down list. |
|   | Region | The region of the secondary site where the instance is located. The system automatically specifies the region. |
| Productio n Region Informatio n | Primary Instance | The production cloud instance for which you want to perform disaster recovery. The system automatically specifies the instance. |
|   | Production Region | Select the region of the primary site where the instance is located from the drop-down list. |
| DR Plan Informatio n | Plan Name | The name of the disaster recovery plan. The name must be 2 to 20 characters in length and can contain letters, digits, underscores ( ), hyphens (-), and periods (.). It _ must start with a letter or digit. |
|   | Plan Type | The purpose of the plan. Valid values: Drill Plan: This plan can only be used for drills and cannot be used for disaster recovery in the production region. Recovery Plan: This plan can be used for both drills and disaster recovery in the production region. |
|   | Plan Description | The detailed description of the plan. |

5. In the **Select Protection Groups** step, perform the following operations:
i. In the Available Protection Groups section, select the protection groups for which you want to perform disaster recovery. ii. Click the icon to move the selected protection groups to the Selected Protection Groups section. iii. After you confirm that all desired protection groups are added, select either of the following options for **Quick Sorting Mode**: Sequential Execution: During disaster recovery, protection groups are failed over in sequence. Concurrent Execution: During disaster recovery, all protection groups are failed over at the same time. iv. Click **Next**.
6. In the **Create Plan** step, you need to create a plan for the failover and failback phases. The
system presets a plan based on the protection groups you selected in the previous step. You can confirm or modify the plan based on your business requirements. Click **Next**. The following table describes the operations that you can perform on the failover and failback plans.

| Operation | Procedure |
|---|---|
| Modify the failover or failback plan | a. Click the icon to check whether the settings of After Failover Succeeded and After Failover Failed meet requirements. If the settings meet requirements, click Confirm. If the settings do not meet requirements, proceed to the next step. b. Set After Failover Succeeded and After Failover Failed based on your business requirements. Valid values: Immediately: The next operation is performed immediately after the failover succeeds. Waiting for Fixed Duration: The next operation is performed or the plan is terminated after the specified period of time elapses. Wait for Manual Operation: The subsequent operations must be manually performed after the failover succeeds or fails. c. Click Confirm. |
| Delete the failover or failback plan | a. Click the icon. b. In the message that appears, click OK. |

| Add manual checkpoints | a. In the Select Point section on the left side of the page, clickM anual Checkpoint. b. Click + Add Step at the bottom of the page. c. Enter check items and select an option from the After Start drop-down list. d. Click Confirm. Note Manual checkpoints take effect only during failovers. You need to manually check whether the site is recovered. |
|---|---|

7. In the **Confirm Information** step, check whether all settings are correct.
If some settings are incorrect, click **Previous** to modify the settings. If all settings are correct, click **Submit**.

##### 6.2.2.2 Query a business disaster recovery plan

You can query a disaster recovery plan by production region, plan type, plan name, or plan ID.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the Business Disaster Recovery Plan page, select **Plan Type**, **Disaster Recovery Plan**
**Name**, or **Disaster Recovery Plan ID** from the drop-down list.
4. The query condition varies based on the selected dimension. See the following table.

| Dimension | Condition |
|---|---|
| Plan Type | Select Drill Plan or Recovery Plan from the drop-down list. |
| Disaster Recovery Plan Name | Enter the name of the disaster recovery plan that you want to query and click the icon. |
| Disaster Recovery Plan ID | Enter the ID of the disaster recovery plan that you want to query and click the icon. |

> **Note:** You can also click Advanced Filter and specify multiple dimensions.
> i. Click **Advanced Filter**.
> ii. Select a plan type and then enter the name and ID of the disaster recovery plan that
> you want to query.
> iii. Click **Search**.

##### 6.2.2.3 Execute a business DR drill plan

The ASR-DR console allows you to execute a drill plan and view the drill process on a GUI. In addition, you can generate a drill report and download the report with one click.

**Prerequisites**

A drill plan for business disaster recovery (DR) is created. For more information, see Create a business disaster recovery plan.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Disaster Recovery Plan**.
3. In the drill plan list, find the desired drill plan and click **Start Drill** in the **Actions** column.
4. In the message that appears, click **OK**.
5. On the drill plan details page, perform the drill tasks one by one based on the created drill
plan.

> **Note:** During the drill, you can click **Terminate** and specify a reason to stop the current drill task. Terminated drill tasks cannot be recovered. If you want to perform these drill tasks again, you must create new drill tasks.
> During the drill, you can also click **Force Pass** to skip the current task.

6. After the drill is complete, view the drill result on the **Historical Records** tab.
The Drill Overview section shows the following information: Drill Success Rate: includes **Successful Drills**, **Total Drills**, and the drill success rate. Protection Group Switchover Success Rate: includes **Successful Protection Group**
**Switchover Acts**, **Total Protection Group Switchover Acts**, and the switchover
success rate. Protection Group Switchback Success Rate: includes **Successful Protection Group**
**Switchback Acts**, **Total Protection Group Switchback Acts** , and the switchback
success rate. RPO-compliant Rate: includes **Compliant Instances**, **Total Instances**, and the compliance rate. Switchover Duration Compliance Rate: includes **Compliant Instances**, **Total Instances**, and the compliance rate. Switchback Duration Compliance Rate: includes **Compliant Instances**, **Total**
**Instances**, and the compliance rate.
7. Click **View Drill Summary** in the **Actions** column of a drill record to view the summary.

> **Note:** The **Download Report** option is displayed in the **Actions** column of a generated report.

8. Go to the **Drill Summary** page. In the**Drill Conclusion**section, click**Edit**to enter a
conclusion for the drill.
9. In the upper-right corner of the page, click **Generate Report**. The system automatically
generates a drill report. Click **Download Report** to export the report in Microsoft Office Word format.

##### 6.2.2.4 View the execution history of a plan

This topic describes how to view drill records and disaster recovery records on the Plan Execution History page.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the Business Disaster Recovery Plan page, click **Plan Execution History**. Drill records
are displayed in reverse order by drill completion time on the Plan Execution History page.
4. View drill records.
i. On the **Drill Records** tab, click Advanced Filter. You can view drill records by **Plan**
**Status**, **Drill Conclusion**, or **Disaster Recovery Plan Name**.
ii. Select a plan state or drill conclusion, or enter a keyword of disaster recovery plan names, and then click the icon. iii. After drill records that meet the specified condition are filtered out, view drill summaries or download reports. View a drill summary: Click **View Drill Summary** in the **Actions** column of a drill record to go to the Summary page. Download a report: After a drill report is generated, click **Download Report** in the
**Actions** column on the Historical Records tab to download the report.
5. View disaster recovery records.
i. Click the **Disaster Recovery Records** tab and click Advanced Filter. You can view disaster recovery records by **Plan Status** or **Disaster Recovery Plan Name**. ii. Select a plan state or enter a keyword of disaster recovery plan names, and then click the icon. iii. Disaster recovery records that meet the specified condition are filtered out.

#### 6.2.3 Manage a disaster recovery unit namespace

**namespace**

ASR-DR supports two active-active modes: active-active services with active-standby cloud products and active-active services with separated cloud products for read and write operations. Only ApsaraDB RDS and OSS support the active-active services with separated cloud products for read and write operations.

**Mode introduction**

Active-active services with active-standby cloud products: In normal cases, the read and write operations of services at both the primary site and the secondary site are processed by the production instances of synchronization entities. Active-active services with separated cloud products for read and write operations: In normal cases, the write operations of services at both the primary site and the secondary site are processed by the production instances of synchronization entities. Read operations are processed by the cloud products in the nearest data center.

##### 6.2.3.1 Create a disaster recovery unit namespace

ASR for Geo-disaster Recovery allows you to bind a disaster recovery unit namespace to a protection group. This ensures that only the synchronization entities in the bound unit namespace are failed over to the secondary site when the primary site fails. A disaster recovery unit namespace can be bound to only one protection group. A synchronization entity can be used by only one disaster recovery unit namespace.

**Prerequisites**

The data-plane SDK is customized. For more information, see Customize the data-plane SDK to implement access from multiple endpoints.

**Scenarios**

**Active-active services and active-standby cloud products**

Services are provided in active-active mode and cloud products work in active-standby mode. The same business system is deployed in two clouds. Under normal circumstances, the read and write operations of the business systems in the two clouds are processed by the cloud products at the primary site. When the primary site fails, the cloud products at the secondary site take over services. All read and write operations of the business systems in the two clouds are failed over to the secondary site.

**Active-active services and separated cloud products for read**

**and write operations**

Services are provided in active-active mode and cloud products work in active-standby mode. Cloud products at the secondary site process read operations only. The same business system is deployed in two clouds. Under normal circumstances, the write operations of the business systems in the two clouds are processed by the cloud products at the primary site. The read operations of the business systems in the two clouds are processed by the cloud products in the nearest data center. When the primary site fails, the cloud products at the secondary site take over services. All read and write operations of the business systems in the two clouds are failed over to the secondary site.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Unit**
**Space**.
3. On the page that appears, click **Create Disaster Recovery Unit Namespace** and set the
required parameters. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Organizations | Select the organization to which the disaster recovery unit namespace belongs. |
| Resource Set | Select the resource set to which the disaster recovery unit namespace belongs. |
| Disaster Recovery Unit Namespace Name | The name of the disaster recovery unit namespace. The name must be 3 to 64 characters in length and start with a letter. It can also contain digits, underscores ( ), and hyphens (-). _ |
| Purpose | The purpose of the disaster recovery unit namespace. |
| Remarks | Other information about the disaster recovery unit namespace. This parameter is optional. |

4. Bind the disaster recovery unit namespace to a protection group.
Click **Create Only**. a. After the disaster recovery unit namespace is created, it is displayed on the Disaster Recovery Unit Namespace page. Click **Bind Protection Group** in the **Actions** column of the disaster recovery unit namespace. b. Select the desired protection group and click **OK**. Click **Create & Bind Protection Group** . a. Select the desired protection group and click **OK**.

**Related operations**

The following table describes the operations that you can perform on the disaster recovery unit namespace you created.

| Operation | Procedure |
|---|---|
| Query the disaster recovery unit namespace | Basic filter: i. On the Disaster Recovery Unit Namespace page, select Protection Group or Disaster Recovery Unit Namespace from the drop-down list, and then enter the name of a protection group or the name of a disaster recovery unit namespace. ii. Click the icon. The disaster recovery unit namespace that meets the specified condition is displayed. Advanced filter: On the Disaster Recovery Unit Namespace page, click Advanced Filter. Enter the name of a disaster recovery unit namespace and the name of a protection group. Click Search. |
| Refresh the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page. |
| Adjust the style for displaying the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page and select Default or Compact to switch the style for displaying the list of disaster recovery unit namespaces. |
| Customize column fields for the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page and select the column fields that you want to display in the list. |
| Display the list of disaster recovery unit namespaces in full screen | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page. The list of disaster recovery unit namespaces is displayed in full screen. |

##### 6.2.3.2 Fail over a disaster recovery unit namespace

**namespace**

This topic describes how to fail over the protection entities in a protection group by failing over the disaster recovery unit namespace to which the protection group is bound.

**Prerequisites**

The disaster recovery unit namespace is bound to a protection group. For more information, see Create a disaster recovery unit namespace.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Unit**
**Space**.
3. On the **Disaster Recovery Unit Namespace** page, find the desired disaster recovery unit
namespace and click **Failover** in the **Actions** column.
4. In the message that appears, click **OK**.

##### 6.2.3.3 Fail back a disaster recovery unit namespace

**namespace**

After the primary data center is recovered, you need to fail the protection entities in the disaster recovery unit namespace that have been failed over to the secondary data center back to the primary data center.

**Prerequisites**

The disaster recovery unit namespace in the primary data center is failed over to the secondary data center. For more information, see Fail over a disaster recovery unit namespace.

**Procedure**

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Unit**
**Space**.
3. On the **Disaster Recovery Unit Namespace** page, find the desired disaster recovery unit
namespace and click **Failback** in the **Actions** column.
4. In the message that appears, click **OK**.

## 7 Alert management

### 7.1 Configure alert rules

The ASR for Geo-disaster Recovery console follows specific rules to send alerts. You can create one or more alert rules.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **Alerts** > **Alert Rules**.
3. Click **Create**.
4. In the **Create Alert Rule** dialog box, configure the parameters. Then, click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | The name of the alert rule. You can customize the name. The name must be 4 to 20 characters in length. |
| Rule Description | The description of the rule. This parameter is optional. |
| Organization | Select the organization to which the instance belongs. Note If you log on by using the organization administrator role or the organization disaster recovery administrator role, the drop-down list displays the organizations that are managed only by you. |
| Metric | i. Select a metric from the first drop-down list. The following metrics are available: Protection Group Status Plan Status Scheduled RTO Protection group synchronization latency ii. Select a condition to trigger alerts from the second drop-down list. iii. Select or enter a value to trigger alerts from the third drop- down list. |
| Alert Level | You can customize an alert level. The following alert levels are available: Alert, Urgent, Warning, Message, and Error. |

| Alert Contact | Select users who receive alerts from the drop-down list. The drop- down list contains users of the organization in the Apsara Uni- manager Management Console. Note If the drop-down list is empty, create users that belong to the organization in the Apsara Uni-manager Management Console. |
|---|---|
| Notification Methods | ASR for Geo-disaster Recovery supports the following notification methods: Email Address: ASR for Geo-disaster Recovery sends emails to alert contacts when the alert rule conditions are met. DingTalk Token: ASR for Geo-disaster Recovery uses DingTalk to notify alert contacts if the alert rule conditions are met. ASO Dashboard: ASR for Geo-disaster Recovery pushes alerts to Alert Monitoring of the Apsara Uni-manager Operations Console if the alert rule conditions are met. |

5. (Optional) After the alert rule is created, you can go to the **Alert Rules** page, click the
icon in the Actions column of the alert rule, and then perform the following operations based on your business requirements: Select **Stop** to stop the alert rule. Select **Change** to modify the alert rule. Select **Delete** to delete the alert rule. Select **View Details** to view the basic information and operation information of the alert rule.
6. (Optional) On the **Alert Rules** page, click **Reset**. ASR for Geo-disaster Recovery clears the
filter conditions and refreshes the list of alert rules.

### 7.2 View and export alert information

**information**

You can view alert information to obtain abnormality information.

**Procedure**

1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Alerts** > **Alert Records**
3. View alert information or set filter conditions.
In the upper part of the page, you can customize the alert conditions. Click the ID of an alert. You can view details of the alert.

### 7.3 Configure synchronization latency alert thresholds

**latency alert thresholds**

You can set the synchronization latency alert thresholds for each service. Apsara Stack Resilience for Disaster Recovery (ASR-DR) calculates the threshold for each service and displays the thresholds on the Disaster Recovery (DR) Dashboard page.
1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Alerts** > **Synchronization Latency Alert**
**Thresholds**.
3. Configure the synchronization latency alert threshold of each service in seconds. Click **OK**.

> **Note:** This feature is available only in the cross-cloud DR scenario.

## 8 System Management

### 8.1 Log management

Operation logs record information about all operations in the system. These operations include the creation, deletion, and execution of protection groups, plans, and instances.

**Procedure**

1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **System Management** > **Logs**.

| Parameter | Description |
|---|---|
| Module | The modules of the ASR-DR system, such as Drill Plans, Recovery Plans, Instances, Alerts, Protection Groups, and System Management. |
| Alert Level | The log levels, which include Urgent, Alert, Error, Warning, and Message. |
| Operation Type | The types of operations recorded in logs. |

3. (Optional)
You can filter specific operations logs by user, module, alert level, operation type, start time, or end time.
4. (Optional)
Click **Retry**. ASR-DR clears search conditions and refreshes information of logs in the list.

### 8.2 Cloud instance management

Before you can configure a protection group and a disaster recovery plan, you must create a cloud instance. Cloud instances are managed by level-1 organizations. All authorized users in a level-1 organization and its subordinate organizations can configure cloud instances for their organizations. The configured cloud instances are available only in the organizations to which they belong.

**Usage notes**

If you need to only configure disaster recovery between different regions of the current cloud, you need to only configure a secondary cloud instance. The cloud instances you configure are shared only between the level-1 organization and its subordinate organizations to which the instances belong. Users in different level-1 organizations must configure their own cloud instances.

**Prerequisites**

The AccessKey ID and AccessKey secret of an organization are obtained. For more information, see Obtain an AccessKey pair. The AccessKey ID and AccessKey secret of a personal account are obtained. For more information, see Obtain an AccessKey pair. You have configured related cloud products by referring to the "Manage cloud product information" section in ASR-DR O&M Guide.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **System Management > Cloud Instances**.
3. On the page that appears, click **Add Instance**, select the cloud instances that you want to
add, and then click **Next**.
4. In the dialog box that appears, select an option from the Resource Set drop-down list,
specify Tenant Account AccessKey ID and Tenant Account AccessKey Secret, and then click
**Submit**.

**Note**

Enter the AccessKey ID and AccessKey secret of the organization you obtained in the Tenant Account AccessKey ID and Tenant Account AccessKey Secret fields. The Tenant Account AccessKey ID and Tenant Account AccessKey Secret parameters need to be configured only once by the user who created the cloud instance.
5. In the dialog box that appears, enter the AccessKey ID and AccessKey secret of the
personal account you obtained.

> **Note:** Enter the AccessKey ID and AccessKey secret of the personal account you obtained in the **User ************** and **User ****************** fields.

6. Click **Confirm**. Configured is displayed in the User AccessKey Pair column of the cloud
instance.

**Note**

The **User ************** and **User ****************** parameters must be configured for each user. A user can use the cloud instance only after the parameters are configured.

**Related operations**

The following table describes the operations that you can perform after the cloud instance is added.

| Operation | Procedure |
|---|---|
| Query the cloud instance | 1. Select a cloud instance state from the Status drop-down list. 2. Select the Instance Name or Instance ID drop-down list and enter a cloud instance name or cloud instance ID. 3. Click the icon. |
| Modify the cloud instance | 1. Click Edit in the Actions column. 2. In the Edit Instance dialog box, modify the AccessKey ID and AccessKey secret and click Submit. |
| Delete the cloud instance | 1. Click Delete in the Actions column. 2. In the message that appears, click Delete. |

| Refresh the cloud instance list | Click the icon in the upper-right corner of the All Instances section. |
|---|---|
| Adjust the display style of the cloud instance list | In the upper-right corner of the All Instances section, click the icon and select Default or Compact to display the cloud instance list in the corresponding style. |
| Customize column fields for the cloud instance list | In the upper-right corner of the All Instances section, click the icon and clear the fields that you do not want to display in the list. |
| Display the cloud instance list in full screen | In the upper-right corner of the All Instances section, click the icon to display the cloud instance list in full screen. |

## 9 Appendix

### 9.1 Create a RAM role

For the organization corresponding to the instance to be protected, you must create a Resource Access Management (RAM) role for Data Transmission Service (DTS) and ASR-DR in the Apsara Uni-manager Management Console of the primary and secondary sites.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console from the primary site.
2. In the top navigation bar, click **Configuration**. In the left-side navigation pane of the
**Configuration** page, click **RAM Role**.
3. Create a **DTS** role for the organization corresponding to the ApsaraDB RDS instance to be
protected. i. Click **Create RAM Role**. ii. On the **Create RAM Role** page, select the organization corresponding to the ApsaraDB RDS instance to be protected from the **Organization Name** drop-down list and select
**DTS** from the **Service Name** drop-down list to create a RAM role.
iii. Click **OK**.
4. Create a **Data Transmission Service** role for the organizations corresponding to the
PolarDB-X instance to be protected and PolarDB instance to be protected. For more information, see Step 3.
5. Create an **ASR-DR** role for the organizations corresponding to the instances to be
protected. For more information, see Step 3.
6. Log on to the Apsara Uni-manager Management Console from the secondary site. Repeat
the preceding steps to create a RAM role for the secondary site.

### 9.2 Obtain an AccessKey pair

To use Apsara Stack Resilience for Disaster Recovery (ASR-DR), the operations administrator or organization administrator must obtain the AccessKey pair of the personal account or the organization account used for the primary center and secondary center, and configure the corresponding AccessKey pair in ASR-DR.

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs of an organization.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane of the **Enterprise** page, click **Organizations**.
4. In the organization navigation tree, click the
icon next to an organization name.
5. Select **AccessKey** from the drop-down list.
6. In the message that appears, obtain the AccessKey pair of the organization.

> **Note:** An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization.

**Obtain the AccessKey pair of ASR-DR**

Use the following procedure to obtain the AccessKey pair of ASR-DR:
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. Enter asrdr in the search box and click **Cluster Details**.
5. On the Cluster Details page, click the **Resource Details** tab. Find the resource of the
**accesskey** type, and click the
icon in the **Resource Application Result** column of the resource to view the AccessKey pair of ASR-DR.

### 9.3 Obtain the configuration information of the primary cloud instance

**information of the primary cloud**

**instance**

This topic describes how to obtain the specified information that is used to configure a primary cloud instance as an administrator. The information includes the endpoint of each cloud service in the primary cloud.
1. Log on to the Apsara Infrastructure Management console for the primary cloud.
In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
> **Platforms** > **Infrastructure Management**.

2. In the left-side navigation pane, choose **O&M Tools** > **Basic Data Management** > **Base**
**Metadata Management**>**Service Registration Variable Dashboard**.
3. Select **Service** from the drop-down list in the upper-left corner. In the search box, enter the
value of the **Service** column based on the product that is described in the following table. Click the icon in the **Service Registration** column of the service in the search results and click the content. In the Registration Variables dialog box, view the value that corresponds to the Key column in the following table. The following table describes the services and keys that correspond to each parameter.

| Product | Configuration item | Service | Key |
|---|---|---|---|
| Apsara Uni- manager Management Console | Apsara Uni- manager Management Console Endpoint | oneService | ascm-portal.domain |
| DTS | DTS Endpoint | dts-dts | dts.openapi.endpoint |

| oneConsole | oneConsole endpoint | oneService | console.domain |
|---|---|---|---|
| VPC | VPC Endpoint | vpc-yaochi | vpc-inner.openapi.endpoint |
| TIANJI | Tianji Endpoint | tianji-endpoint | api server.endpoint _ |
| RSM | RSM Endpoint | rsm | rsm.api.domain |
| OSS | OSS Operations and Maintenance System Endpoint Without Authentication Information | oss-chiji | inner-api-endpoint |
|   | OSS Operations and Maintenance System Endpoint With Authentication Information Included |   | inner-secure-api-endpoint |
|   | POP Endpoint of OSS Operations and Maintenance System |   | pop-api-endpoint |
|   | OSS Endpoint | oss-server | api-endpoint |
|   | Tablestore Endpoint |   | ocm.pop endpoint _ |
|   | OCM Internal Endpoint |   | ocm.endpoint |
|   | Tablestore Endpoint |   | ocm.pop tablestore endpoint _ _ |
|   | Replication Endpoint |   | repmanager.endpoint |

|   | e |   | ASR for Geo-disaster User Guide Appendi |
|---|---|---|---|
| Tablestore |   | TableStoreOC M |   |
|   | ocm admin accessKeyId |   | ocm.admin accessid _ |
|   | ocm admin accessKeySecr et |   | ocm.admin accesskey _ |
|   | super accessKeyId |   | ocm.super ots accessid _ _ |
|   | super accessKeySecr et |   | ocm.super ots accesskey _ _ |
| GTM | GTM Endpoint | dns-global- traffic-manage | gtm.pop domain _ |
| RDS | ApsaraDB RDS Endpoint | rds-yaochi | rds.openapi.endpoint |
| PolarDB-X | PolarDB-X Endpoint | drds-console | prectrl.api |
| RAM | RAM Endpoint | ram- ramService | ram-openapi.endpoint |
|   | STS Endpoint |   | sts-openapi.endpoint |
|   | RAM Slave Endpoint |   | ram-slave.endpoint |
| ApsaraMQ | ApsaraMQ AccessKey ID | mq-console | onsInnerApiAccessKey |
|   | ApsaraMQ AccessKey Secret |   | ******************** |
|   | ApsaraMQ Endpoint |   | console.domain |
| Document Version: | 20250618 9 |   |   |

|   | AccessKey Router OnsAddr | mq-router | router.onsAddr |
|---|---|---|---|
| DNS | DNS Control Endpoint | dnsService | dns control.pop domain _ _ |
|   | DNS Endpoint |   | dns universal control.pop domain _ _ _ |
|   | DNS AccessKey ID |   | genesisdns.global access key _ _ |
|   | DNS AccessKey Secret |   | genesisdns.global access secret _ _ |
| DataWorks | BCC API Endpoint | apsara- bigdata- manager | bcc endpoint _ |
|   | BCC App |   | super app name _ _ |
|   | BCC Key |   | super app key _ _ |
|   | BCC Password |   | super account secret key _ _ _ |
|   | BCC User |   | super account account _ _ |
| HBase | ApsaraDB for HBase Endpoint | hbase-yaochi | hbase.openapi.endpoint |
| LINDORM | Lindorm Endpoint | lindorm | lindorm pop endpoint _ _ |
| MongoDB | ApsaraDB for MongoDB Endpoint | mongodb- yaochi | mongodb.openapi.endpoint |
| Redis | KVStore for Redis Endpoint | kvstore-yaochi | kvstore.openapi.endpoint |
| Hologres | Hologres Control Endpoint | hologres-init | holo-manager.endpoint |
| 0 |   |   | > Document Version: 2025061 |

| sara Stack Resilienc | e |   | ASR for Geo-disaster User Guide Appendi |
|---|---|---|---|
|   | Hologres-POP Endpoint |   | pop holo remote recover dns _ _ _ _ |
| ECS | HDR Endpoint | cds-bcdr | hdr.openapi.endpoint |

4. In the left-side navigation pane, click **Product & Cluster O&M**.
5. On the **Projects** page, enter `baseServiceAll` in the search box and click **Cluster Details**
in the **Actions** column.
6. On the **Cluster Details** page, click the **Desired State Configuration** tab.
7. Select the **kv.conf** file and click **Show Content**.
8. Find the value in the **kv.conf** file by using the keys of corresponding products.
The following table describes the mappings between the parameters and keys.

| Product | Configuration item | Key |
|---|---|---|
| OSS | OSS-POP AccessKey ID | account.defaultUser.accesskey-id |
|   | OSS-POP AccessKey Secret | account.defaultUser.accesskey-secret |
| PolarDB- X | PolarDB-X RAM ID | account.drds.id |
|   | PolarDB-X RAM AccessKey ID | account.drds.accesskey-id |
|   | PolarDB-X RAM AccessKey Secret | account.drds.accesskey-secret |
|   | PolarDB-X Zone value | biz zone _ |
| ASR for Geo- disaster Recovery | AccessKey ID of Account to Log on to ASR for Geo- disaster Recovery | account.asr.accesskey-id |
|   | AccessKey Secret for Logging on to ASR for Geo- disaster Recovery | account.asr.accesskey-secret |

| TIANJI | Tianji AccessKey ID | account.defaultUser.accesskey-id |
|---|---|---|
|   | Tianji AccessKey Secret | account.defaultUser.accesskey-secret |
| LINDORM | LTS Authentication AccessKey ID | account.asr.accesskey-id |
|   | LTS Authentication AccessKey Secret | account.asr.accesskey-secret |

> **Note:** If the key value is displayed in ciphertext, use the following method for decryption:

i. Log on to the container.

> ii. Run the following command to obtain the decrypted value:

```bash
curl --fail --unix-socket /var/run/proxyssl/pssl.sockrest 'http://host/api/v1/configs' -H 'Content-Type: application/octet-stream' -X POS T -d {"<Parameter key>":"<Parameter value in ciphertext>"}
```

### 9.4 Customize the data-plane SDK to implement access from multiple endpoints

**to implement access from multiple**

**endpoints**

Only ApsaraDB RDS and OSS support separated processing of read and write operations.

**Prerequisites**

The data-plane SDK package is ready.

**Custom content**

1. Introduce the SDK that implements access from multiple endpoints to your business
system.

```xml
<dependency>
 <groupId>com.aliyun.asrdr</groupId>
 <artifactId>asrdr-sdk-all</artifactId>
 <version>2.2.0.SNAPSHOT</version>
</dependency>
```

2. Modify cloud product configurations.

```bash
# Configuration item before modification
rdsEndpoint=region-shanghai-rds-instance1.com
# Configuration item after modification
rdsEndpoint=dr-master-a1://rds-instance1.com;dr-master-a2://rds-instance2.com
```

3. Modify the application code.
Support access from multiple endpoints. Add the java process startup parameter -Ddreventcenter=asrdr-xxx.com - Ddrstrategy=2idc3center.

```bash
# Startup parameters before modification
java -server -Xms4096m -Xmx4096m -Xmn2048m -Xss512k -XX:MetaspaceSize=512m -XX:MaxMetaspaceSize=1024m -XX:SurvivorRatio=8 -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:+CMSClassUnloadingEnabled -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/admin/logs/java_pid.hprof -jar /home/admin/asrdr/web-3.0.0.jar
# Startup parameters after modification
java -server -Xms4096m -Xmx4096m -Xmn2048m -Xss512k -XX:MetaspaceSize=512m -XX:MaxMetaspaceSize=1024m -XX:SurvivorRatio=8 -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:+CMSClassUnloadingEnabled -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/home/admin/logs/java_pid.hprof -jar /home/admin/asrdr/web-3.0.0.jar -Ddreventcenter=asrdr-xxx.com -Ddrstrategy=2idc3center
```
