---
title: "Apsara Stack Resilience ASR for Geo-disaster User Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 204
source_pdf: "895b48aaec7c2c5b_Alibaba Cloud Apsara Stack V3.18.6 Apsara Stack Resilience ASR for Geo-disaster User Guide 20260701."
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BC%82%E5%9C%B0%E5%AE%B9%E7%81%BEASRDR/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Geo-disaster%20User%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Apsara Stack Resilience ASR for Geo-disaster User Guide 20260701

## Table of Contents

- 1 ASR for Geo-disaster Recovery operations in the Apsara Uni-manager Management Console
  - 1.1 Overview of ASR for Geo-disaster Recovery
  - 1.2 Getting Started
    - 1.2.1 Roles and permissions
    - 1.2.2 Log on to the ASR for Geo-disaster Recovery console
    - 1.2.3 Disaster recovery scenarios
  - 1.3 Overview
  - 1.4 Instance management
    - 1.4.1 View instances
    - 1.4.2 Manage ingress traffic gateway instances
      - 1.4.2.1 Create an ingress traffic gateway instance
      - 1.4.2.2 View the topology of an ingress traffic gateway instance
      - 1.4.2.3 View the monitoring metrics of an ingress traffic gateway instance
  - 1.5 DR for business
    - 1.5.1 Protection Groups
      - 1.5.1.1 Manage protection groups
        - 1.5.1.1.1 Create a protection group
        - 1.5.1.1.2 Perform reprotection
        - 1.5.1.1.3 Protection group details
          - 1.5.1.1.3.1 View the details of a protection group
          - 1.5.1.1.3.2 View a protection entity
          - 1.5.1.1.3.3 View the operations records of a protection group
          - 1.5.1.1.3.4 Delete a protection entity
          - 1.5.1.1.3.5 Change the group of a protected entity
          - 1.5.1.1.3.6 Modify the permissions of read-only accounts
          - 1.5.1.1.3.7 Modify the privileged account of an ApsaraDB RDS instance
          - 1.5.1.1.3.8 Manage protection entity account permissions
          - 1.5.1.1.3.9 Modify the objects to be synchronized
        - 1.5.1.1.4 Add a synchronization entity
          - 1.5.1.1.4.1 Configure disaster recovery for ApsaraDB RDS instances
          - 1.5.1.1.4.2 Configure disaster recovery for PolarDB-X 2.0 instances
          - 1.5.1.1.4.3 PolarDB for MySQL
          - 1.5.1.1.4.4 PolarDB for PostgreSQL
          - 1.5.1.1.4.5 Configure disaster recovery for OSS buckets
          - 1.5.1.1.4.6 Big data products
          - 1.5.1.1.4.7 DNS (Multicloud Integration)
          - 1.5.1.1.4.8 Private domain name resolution (DNS)
          - 1.5.1.1.4.9 Message Queue
          - 1.5.1.1.4.10 Message Queue for Kafka
          - 1.5.1.1.4.11 Configure disaster recovery for Tair (Redis OSS-compatible) instances
          - 1.5.1.1.4.12 Configure disaster recovery for ApsaraDB for MongoDB instances
          - 1.5.1.1.4.13 ECS
          - 1.5.1.1.4.14 DataHub
          - 1.5.1.1.4.15 Ingress gateway AsrIngressGW
          - 1.5.1.1.4.16 API Gateway
        - 1.5.1.1.5 Start a protection group
      - 1.5.1.2 Fail over a protection group
      - 1.5.1.3 Fail back a protection group
      - 1.5.1.4 Stop a protection group
      - 1.5.1.5 Export protection groups
      - 1.5.1.6 Manage protection group topologies
        - 1.5.1.6.1 Manage topology applications
        - 1.5.1.6.2 View an application topology
    - 1.5.2 Manage a plan
      - 1.5.2.1 Overview
      - 1.5.2.2 Manage business disaster recovery plans
        - 1.5.2.2.1 Create a business disaster recovery plan
        - 1.5.2.2.2 Configure drill metrics
        - 1.5.2.2.3 Query a business disaster recovery plan
        - 1.5.2.2.4 Perform a business disaster recovery
        - 1.5.2.2.5 Execute a business disaster recovery drill plan
        - 1.5.2.2.6 View the execution history of a plan
      - 1.5.2.3 Manage a disaster recovery unit namespace
        - 1.5.2.3.1 Create a disaster recovery unit namespace
        - 1.5.2.3.2 Fail over a disaster recovery unit namespace
        - 1.5.2.3.3 Fail back a disaster recovery unit namespace
  - 1.6 Alert management
    - 1.6.1 Configure alert rules
    - 1.6.2 View and export alert information
    - 1.6.3 Configure synchronization latency alert thresholds
  - 1.7 System Management
    - 1.7.1 Cloud instance management
    - 1.7.2 Manage disaster recovery relationships
    - 1.7.3 Manage logs
    - 1.7.4 Hybrid disaster recovery management
  - 1.8 FAQ
    - 1.8.1 What do I do if entities fail to be protected?
    - 1.8.2 Troubleshoot abnormal disaster recovery relationship checks
  - 1.9 Appendix
    - 1.9.1 Create a RAM role
    - 1.9.2 Obtain the AccessKey pair of a personal account of public cloud
    - 1.9.3 View the synchronization logs of MaxCompute
    - 1.9.4 Modify policy configuration
    - 1.9.5 Suspend synchronization entities under a protection group
    - 1.9.6 Obtain an AccessKey pair
    - 1.9.7 Manually synchronize data
    - 1.9.8 Obtain the settings of the primary cloud instance
    - 1.9.9 Customize the data-plane SDK to implement access from multiple endpoints
- 2 O&M console of ASR for Geo-disaster Recovery
  - 2.1 Log on to the O&M console of ASR for Geo-disaster Recovery
  - 2.2 Homepage
  - 2.3 Disaster recovery monitoring
    - 2.3.1 View the cloud platform monitoring
    - 2.3.2 View the protection group monitoring
  - 2.4 Basic capability O&M
    - 2.4.1 Manage cloud product information
    - 2.4.2 Manage a disaster recovery interconnection
    - 2.4.3 Manage a disaster recovery gateway
    - 2.4.4 Configure a dashboard map
  - 2.5 Disaster recovery O&M
    - 2.5.1 Manage synchronization entities
      - 2.5.1.1 Skip a step
      - 2.5.1.2 Reperform a single step
      - 2.5.1.3 Configure throttling
      - 2.5.1.4 Delete an entity from a protection group
      - 2.5.1.5 View the logs of a synchronization entity
    - 2.5.2 Perform a site switchover drill
    - 2.5.3 Perform a site failover
    - 2.5.4 View the execution history of a site disaster recovery plan
  - 2.6 Independent disaster recovery management
    - 2.6.1 Create an independent disaster recovery plan
    - 2.6.2 Perform a failover
    - 2.6.3 Perform a switchover drill
    - 2.6.4 View the details of an independent disaster recovery plan
    - 2.6.5 Disassociate configured nodes from an independent disaster recovery plan
    - 2.6.6 Delete an independent disaster recovery plan
  - 2.7 Appendixes
    - 2.7.1 Look up a DNS address
    - 2.7.2 Configure DNS forwarding
    - 2.7.3 Configure DTS parameters

## 1 ASR for Geo-disaster Recovery operations in the Apsara Uni-manager Management Console

**Recovery operations in the**

**Apsara Uni-manager**

**Management Console**

This topic describes the ASR for Geo-disaster Recovery operations in the Apsara Uni-manager Management Console.

### 1.1 Overview of ASR for Geo-disaster Recovery

**disaster Recovery**

This topic describes the principles and concepts of ASR-DR, along with the functional modules of the off-site disaster recovery management platform.

**Overview of geo-disaster recovery principles**

ASR for Geo-disaster Recovery ASR-DR (Apsara Stack Resilience for Disaster Recovery), abbreviated as ASR-DR, is a cloud platform product that provides disaster recovery capabilities. It currently supports geo-disaster recovery management for Object Storage Service (OSS), ApsaraDB RDS for MySQL 5.6/5.7/8.0, ApsaraDB for PolarDB-O 11.2, PolarDB-X 2.0, PolarDB-M with local disks, PolarDB-PG with local disks, DNS, Message Queue (MQ), ApsaraDB for MongoDB, ApsaraDB for Redis, DataHub, MaxCompute, traffic gateway AsrIngressGW, SLB, and DataWorks. After you create a protection group, ASR for Geo-disaster Recovery establishes a disaster recovery channel between the resources at the primary and secondary sites. Changes to resources at the primary site are asynchronously synchronized to the corresponding resources at the secondary site. If the primary site fails, applications or services are failed over to the secondary site using a failover plan. After the primary site is recovered, the business is failed back to the primary site using a failback plan. This process ensures business continuity.

**Terms**

Protection group: A business object that is protected by ASR for Geo-disaster Recovery. A protection group contains a set of related resources that an application uses. Recovery plan: A predefined, automated workflow for fault scenarios. In the event of a disaster or fault, you can execute the workflow to automatically perform disaster recovery operations on the resources in a protection group and ensure business continuity. Failover: An unplanned transfer of disaster recovery applications from the primary data center to the secondary data center. This is typically caused by an event such as a power loss or network disconnection at the primary data center. Failback: The recovery of a disaster recovery application from the secondary data center to the primary data center after services, such as network or power, are restored in the primary data center. Drill plan: A predefined workflow for drill scenarios. The steps in this workflow are nearly identical to those in the corresponding recovery plan. You can use a drill plan to test a recovery plan and verify its correctness. Switchover: A planned migration of disaster recovery applications from the primary data center to the secondary data center when both data centers are operating normally. Switchback: A planned migration of disaster recovery applications from the secondary data center back to the primary data center when both data centers are operating normally. Recovery Point Objective (RPO): Measured in time, RPO defines the point in time to which systems and data must be restored after a disaster. It indicates the maximum amount of data loss that a system can tolerate. A smaller RPO value indicates a lower tolerance for data loss. Recovery Time Objective (RTO): Measured in time, RTO defines the maximum allowable time to restore information systems or business functions after a disaster. It indicates the maximum service downtime that a system can tolerate. A smaller RTO value indicates a higher urgency for service restoration.

**Feature description**

| Feature module | Description |
|---|---|
| Overview | Displays information such as protection groups, disaster recovery plans, and synchronization entities. |
| Instances | Displays all instances at the production and disaster recovery sites, instance status, and associated protection groups. This helps you quickly obtain instance status within the current cluster and gain an overall understanding of cluster health. |
| DR for Business | Includes configuration of protection groups, business disaster recovery plans, and disaster recovery unit namespaces. |
| Alert Managem ent | Set alert rules for various metrics of protection groups and plans, configure synchronization latency alert thresholds, and send alert notifications to alert contacts. Use these alerts to detect system anomalies and troubleshoot issues promptly. |

| System Managem ent | The core module for centralized permission management. Manage cloud instances, disaster recovery relationships, Hybrid Disaster Recovery, and logs. |
|---|---|
| Dashboar d monitorin g | Displays disaster recovery overview, protection group disaster recovery status, disaster recovery metrics, product synchronization latency, and changes in protection group synchronization latency on a large screen. |

### 1.2 Getting Started

#### 1.2.1 Roles and permissions

This topic describes the permissions of operations administrators, organization administrators, global disaster recovery (DR) administrators, and organization DR administrators.

| Role | Logon method | Permissions |
|---|---|---|
| Operations administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the operations administrator role, such as the admin account. 2. Select the root organization to access the ASR-DR console. | Add primary cloud instances and configure cloud services. Manage DR resources for all cloud services. |
| Organization administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the organization administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator but cannot configure cloud services. Manage DR resources for cloud services only in the current organization and subordinate organizations. |
| Global DR administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the global DR administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator and configure cloud services. Manage DR resources for all cloud services. |

| Organization DR administrator | 1. Log on to the Apsara Uni-manager Management Console by using an account that assumes the organization DR administrator role. 2. Select the corresponding organization to access the ASR-DR console. | Inherit the primary cloud instances that are added by the operations administrator but cannot configure cloud services. Manage DR resources for cloud services only in the current organization and subordinate organizations. |
|---|---|---|

#### 1.2.2 Log on to the ASR for Geo-disaster Recovery console

**Recovery console**

This topic describes how to log on to the ASR for Geo-disaster Recovery console.

**Prerequisites**

The domain name, username, and password are obtained from the deployment personnel of the Apsara Uni-manager Management Console. A web browser is available. We recommend that you use Google Chrome. You are an operations administrator, organization administrator, global disaster recovery administrator, or organization disaster recovery administrator.

**Scenarios**

In cross-cloud disaster recovery scenarios, the ASR for Geo-disaster Recovery console is separately deployed in the primary and secondary clouds. You must log on to the ASR for Geo-disaster Recovery console from the Apsara Uni-manager Management Console of the secondary cloud. The primary cloud acts as the security gateway for API calls during crosscloud disaster recovery. If a failure occurs on the secondary cloud after the business is successfully switched to it, you must log on to the ASR for Geo-disaster Recovery console from the Apsara Uni-manager Management Console of the primary cloud and switch the business back from the secondary cloud back to the ASR for Geo-disaster Recovery console of the primary cloud to ensure business continuity. In cross-region disaster recovery scenarios, the ASR for Geo-disaster Recovery console is deployed in the central region. You need to log on to the ASR for Geo-disaster Recovery console by using the Apsara Uni-manager Management Console in the central region.

> **Note:** The first time you log on to the ASR for Geo-disaster Recovery console, you must make the following initial configurations:

Configure cloud services that support disaster recovery. For more information, see Manage cloud product information. Configure disaster recovery relationships. For more information, see Manage disaster recovery relationships. Configure cloud instances. For more information, see Cloud instance management.

> Configure a RAM role. For more information, see Create a RAM role.
> Configure independent disaster recovery. For more information, see the Manage independent disaster recovery. You need to configure independent disaster recovery only in cross-cloud disaster recovery scenarios. You do not need to configure independent disaster recovery in cross-region disaster recovery scenarios.

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

> **Note:** **First login**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forgotten password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator: a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, select **Products**.
6. In the left-side navigation pane, click **Disaster Recovery and Backup**.
7. In the **Disaster Recovery and Backup** section, choose **Disaster Recovery > ASR for**
**Geo-disaster Recovery**.
8. You are redirected to the ASR for Geo-disaster Recovery console. All data is displayed by
cloud, organization, resource set, and region. The first time you log on to the console, you must configure disaster recovery relationships and cloud instances.

#### 1.2.3 Disaster recovery scenarios

Apsara Stack supports cross-cloud disaster recovery and cross-region disaster recovery. This topic describes two disaster recovery scenarios. Cross-cloud disaster recovery and cross-region disaster recovery: Cross-cloud disaster recovery: Disaster recovery is performed between two cloud instances. If the primary cloud fails, business is failed over to the secondary cloud. Cross-cloud disaster recovery can be implemented in the following modes: Cross-cloud disaster recovery for a single cloud: If the central region of the primary cloud fails, business is failed over to the central region of the secondary cloud. The unit Region in the production cloud supports 1:1 disaster recovery to the central Region in the DR cloud. Cross-cloud disaster recovery for multiple clouds: If multiple primary clouds fail, business is failed over to the central region of the secondary cloud. Three data centers across two regions. Disaster recovery between Apsara Stack and Alibaba Public Cloud (1:1). Cross-region disaster recovery: Disaster recovery is performed across multiple regions within a cloud instance. Cross-region disaster recovery can be implemented in the following modes: If a general region fails, business can be failed over to the central region. Disaster recovery between Cell Regions. Disaster recovery from the central region to a cell region (for service failures only, but not for region-wide power or network outages in the central region). The following table describes the products and features supported in the two disaster recovery scenarios.

| Dis ast er rec ov er y sc en ari os | Disaster recovery types | X86-supported products | ARM-based products | Feature supported by ASR- DR |
|---|---|---|---|---|
|   | Fail over to the central region of the secondary cloud if the central region of the primary cloud fails | ApsaraDB RDS for MySQL 5.6, 5.7, and 8.0 PolarDB-X 2.0: A cloud-native distributed database Cloud-native database PolarDB for PostgreSQL with local disks ApsaraDB for MongoDB ApsaraDB for Redis Object Storage Service (OSS) ECS and EBS Message Queue Apsara Stack DNS MaxCompute and DataWorks DataHub SchedulerX | ApsaraDB RDS for MySQL 8.0 Cloud-native database PolarDB for PostgreSQL with local disks PolarDB-X 2.0 is a cloud-native distributed database. Object Storage Service (OSS) Apsara Stack DNS MaxCompute and DataWorks DataHub SchedulerX |   |

| Cr os s- clo ud dis ast er rec ov er y |   |   |   | Overview, disaster recovery dashboards, instance management, business disaster recovery, log management, alert management, and alert management for synchronization latency |
|---|---|---|---|---|
|   | Multiple productio n clouds use a central region for disaster recovery. | ApsaraDB RDS for MySQL 5.6, 5.7, and 8.0 ApsaraDB for PolarDB- O PolarDB-X 2.0 is a cloud-native distributed database. Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks MongoDB Edition ApsaraDB for Redis Object Storage Service (OSS) Apsara Stack DNS DataHub | ApsaraDB RDS for MySQL 8.0 PolarDB-X 2.0, a cloud-native distributed database Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks Object Storage Service (OSS) Apsara Stack DNS DataHub |   |
|   | Three data centers across two regions | ApsaraDB RDS for MySQL 5.6, 5.7, and 8.0 ApsaraDB for PolarDB- O Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks ApsaraDB for MongoDB ApsaraDB for Redis Object Storage Service (OSS) Message Queue Apsara Stack DNS DataHub MaxCompute DataWorks SchedulerX | ApsaraDB RDS for MySQL 8.0 Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks ApsaraDB for PolarDB-O Object Storage Service (OSS) Message Queue Apsara Stack DNS DataHub MaxCompute DataWorks SchedulerX |   |

| Cr os s- re gio n dis ast er rec ov er y | All modes | ApsaraDB RDS for MySQL 5.6, 5.7, and 8.0 ApsaraDB for PolarDB- O PolarDB-X 2.0 Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks ApsaraDB for MongoDB ApsaraDB for Redis Object Storage Service (OSS) Message Queue MaxCompute and DataWorks (data synchronization only) Apsara Stack DNS DataHub MaxCompute DataWorks SchedulerX | ApsaraDB RDS for MySQL 8.0 PolarDB-X 2.0 is a cloud-native distributed database. Cloud-native distributed database PolarDB-M with local disks Cloud-native database PolarDB for PostgreSQL with local disks ApsaraDB for PolarDB-O Object Storage Service (OSS) Message Queue Apsara Stack DNS DataHub MaxCompute DataWorks SchedulerX | Instance management, business disaster recovery, big data disaster recovery, log management, and alert management |
|---|---|---|---|---|

### 1.3 Overview

The Overview page provides charts and numbers to show the disaster recovery (DR) overview of business. You can view the real-time DR metrics and learn the DR protection group status on this page. This helps improve the efficiency of DR management and the continuity of application business.

**Precautions**

When you log on to the ASR for Geo-disaster Recovery console for the first time, you are promoted to configure a primary cloud instance. See the following figure. All business data can be displayed by organization, resource set, or region.
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

### 1.4 Instance management

#### 1.4.1 View instances

Create the instances that you want to protect on the production and disaster recovery sites. The number and specifications of instances in the protection group must be identical for both the production and disaster recovery sites.
1. Log on to the Apsara Uni-manager Management Console for the production and disaster
recovery sites.
2. Create cloud product instances by following the user guide for each cloud service. The
following table describes the tasks to complete and important notes for creating instances for each product.

| Product | Task | Notes |
|---|---|---|
| ApsaraDB RDS | On the production and disaster recovery sites, create ApsaraDB RDS instances, ApsaraDB RDS accounts, and databases. | The number and specifications of ApsaraDB RDS instances for your services must be identical on the production and disaster recovery sites. The network type of the ApsaraDB RDS instances for your services must be the same on the production and disaster recovery sites. For example, both instances must use VPC networks. You do not need to create databases in the ApsaraDB RDS instances on the disaster recovery site because ASR-DR automatically synchronizes databases from the ApsaraDB RDS instances on the production site. This does not apply to the Agility Edition. Use the same instance names on the production and disaster recovery sites. Associate the names with your service to simplify maintenance. |

| PolarDB for Oracle | On the production and disaster recovery sites, create PolarDB for Oracle instances, initial accounts, databases, and schemas. | Set the Database Version to 11. Set Network Type to VPC. The specifications of the PolarDB for Oracle instances for your services must be identical on the primary and secondary sites. The VPCs to which the primary and secondary PolarDB for Oracle instances belong must be connected, and their CIDR blocks cannot conflict. The initial account is for service-side use. You can create only one standard account for this purpose. A privileged account must be granted the superuser role by an Aurora operations account. The disaster recovery instance can contain only one database and must use the public schema. The wal level parameter for the primary and _ secondary PolarDB for Oracle instances must be set to logical. The commands to query and configure this parameter are as follows: # Connect to the database using the aurora or initial account and execute the following SQL statement show wal level; # Query the _ configuration alter system set wal level = _ logical; # Modify the configuration Use the same instance names on the production and disaster recovery sites. Associate the names with your service to simplify maintenance. |
|---|---|---|

| PolarDB for MySQL | On the production and disaster recovery sites, create PolarDB for MySQL instances, accounts, and databases. | PolarDB for MySQL instances are available with local disks or shared storage. The storage type for your service's PolarDB for MySQL instances must be the same on the production and disaster recovery sites. For example, both instances must use local disks, or both must use shared storage. If the PolarDB for MySQL instances on the production and disaster recovery sites use shared storage, you must request a classic network endpoint and enable binary logging (binlog). Note Enabling binlog restarts the instance, which affects your services. We recommend that you perform this operation during off-peak hours. The number and specifications of the PolarDB for MySQL instances for your services must be identical on the production and disaster recovery sites. The network type of the PolarDB for MySQL instances for your services must be the same on the production and disaster recovery sites. For example, both instances must use VPC networks. The database engine version of the PolarDB for MySQL instances for your services must be the same on the production and disaster recovery sites, such as MySQL 5.7 or MySQL 8.0. You do not need to manually create databases in the PolarDB for MySQL instances on the disaster recovery site because ASR-DR automatically synchronizes databases from the production site. |
|---|---|---|

| PolarDB for PostgreSQL | On the production and disaster recovery sites, create PolarDB for PostgreSQL instances, accounts, databases, and schemas. | The number and specifications of the PolarDB for PostgreSQL instances for your services must be identical on the production and disaster recovery sites. The network type of the PolarDB for PostgreSQL instances for your services must be the same on the production and disaster recovery sites. For example, both instances must use VPC networks. Use the same instance names on the production and disaster recovery sites. Associate the names with your service to simplify maintenance. You do not need to manually create databases in the PolarDB for PostgreSQL instances on the disaster recovery site because ASR-DR automatically synchronizes databases from the production site. |
|---|---|---|
| Cloud-native distributed database PolarDB-X 2.0 | On the production and disaster recovery sites, create PolarDB-X 2.0 instances and accounts. | The number and specifications of the PolarDB- X 2.0 instances for your services must be identical on the production and disaster recovery sites. The network type of the PolarDB-X 2.0 instances must be the same on the production and disaster recovery sites. For example, both instances must use VPC networks. Use the same instance names on the production and disaster recovery sites. Associate the names with your service to simplify maintenance. You do not need to manually create databases in the PolarDB-X 2.0 instances on the disaster recovery site because ASR-DR automatically synchronizes databases from the production site. |
| Object Storage Service (OSS) Note The instance types on the Object Storage Service tab include OSS and CDS-OSS. | On the production and disaster recovery sites, create OSS buckets. | The number of OSS buckets for your services must be identical on the production and disaster recovery sites. In full protection scenarios, the secondary instance must be empty. The versioning feature must be configured identically for the production and disaster recovery instances. A maximum of 20 OSS buckets can be protected. |

| Message Queue (MQ) | On the production and disaster recovery sites, create MQ instances and topics. | The number of MQ instances for your services must be identical on the production and disaster recovery sites. The topic names for MQ must be the same on the production and disaster recovery sites. |
|---|---|---|
| Message Queue for Apache Kafka | On the production and disaster recovery sites, create Kafka instances and topics. | The number of Kafka instances for your services must be identical on the production and disaster recovery sites. The topic names and the number of partitions for Kafka must be the same on the production and disaster recovery sites. |
| Apsara Stack DNS | On the production and disaster recovery sites, create DNS domain names and add resolution records. | The number of global internal domain names for DNS must be identical on the production and disaster recovery sites. The Collection of Record Values in the DNS Settings for the production site DNS domain name must match the Collection of Record Values in the DNS Settings for the disaster recovery site DNS domain name. In the Resolution Settings for the DNS domain name, set the Load Balancing Policy to Weight and configure the service virtual IP addresses (VIPs) for the primary and secondary sites. In the Record Value Set, place the primary site record before the secondary site record. For example, master-host 100, slave-host 0. |
| DNS (Internal) | On the production and disaster recovery sites, create domain names. | The domain name configurations and the number of domain names must be identical on the production and disaster recovery sites. |

| Big Data Computing with MaxCompute | On the production and disaster recovery sites, create MaxCompute projects, Alibaba Cloud accounts for tasks, and computing units. | The number of computing units (CUs) and the storage capacity for MaxCompute must be the same for your services on the production and disaster recovery sites. The project names and the names of the Alibaba Cloud accounts for tasks for MaxCompute must be the same on the production and disaster recovery sites. The project names for DataWorks must be the same for your services on the production and disaster recovery sites. Use the same workspace names for DataWorks and project names for MaxCompute on the production and disaster recovery sites. Associate the names with your service to simplify maintenance. Before you perform incremental synchronization, ensure that the data is consistent between the production and disaster recovery sites. |
|---|---|---|
| SchedulerX | On the production and disaster recovery sites, create SchedulerX applications. | The application names for SchedulerX must be identical on the production and disaster recovery sites. The group IDs for SchedulerX must be identical on the production and disaster recovery sites. |
| ApsaraDB for MongoDB | On the production and disaster recovery sites, create ApsaraDB for MongoDB instances and accounts. | Only replica set and sharded cluster instances that run version 4.0, 4.2, or 4.4 are supported. You must request classic network endpoints for the instances. |
| ApsaraDB for Redis | On the production and disaster recovery sites, create ApsaraDB for Redis instances and accounts. | Only Community Edition 4.0 and 5.0, and Enterprise Edition 5.0 are supported. You must request classic network endpoints for the instances. |
| Elastic Compute Service (ECS) | On the production and disaster recovery sites, create ECS instances, Elastic Block Storage (EBS) disks, and VPCs. | Disks: Only agentless premium performance disks (IO15) are supported. Network: The CIDR blocks of the VPCs where the ECS instances on the production and disaster recovery sites reside cannot conflict. Only single-data center instances are supported. |

| DataHub | On the production and disaster recovery sites, create DataHub instances. | The number of DataHub instances for your services must be identical on the production and disaster recovery sites. The topic names and field names for DataHub must be the same on the production and disaster recovery sites. |
|---|---|---|
| Traffic Gateway AsrIngressGW | On the production and disaster recovery sites, create AsrIngressGW instances. | The production and disaster recovery sites must have the same number of AsrIngressGW instances for your services. The recommended minimum configuration for an ECS instance attached to an AsrIngressGW instance is 2 vCPUs and 4 GiB of memory. The ECS instance must also be attached to an Elastic IP address (EIP). The Server Load Balancer (SLB) instance attached to the AsrIngressGW instance must be in the same VPC as the ECS instance, in a connected VPC, or in the classic network. |
| API Gateway | On the production and disaster recovery sites, create API Gateway instances. | The historical data of the disaster recovery module in the API Gateway instances on the production site must be consistent with the historical data on the disaster recovery site. |

#### 1.4.2 Manage ingress traffic gateway instances

**instances**

##### 1.4.2.1 Create an ingress traffic gateway instance

This topic describes how to create an ingress traffic gateway instance and bind Elastic Compute Service (ECS) and Server Load Balancer (SLB) instances.

**Prerequisites**

In the Apsara Uni-manager Management Console, you have created an ECS instance in the ECS console and created an SLB instance in the SLB console. The ECS and SLB instances meet the following requirements: The recommended minimum configuration of the ECS instance is 2 CPU cores and 4 GB of memory. An elastic IP address (EIP) is associated with the ECS instance. SLB and ECS instances are in the same virtual private cloud (VPC), the VPC where the SLB instance is located is connected to the VPC where the ECS instance is located, or the SLB instance is located in the classic network.
1. Log on to the ASR for Geo-disaster Recovery console. For more information, see Log on to the
ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Primary Region** tab, click **Ingress Gateway for Traffic**.
4. Click **Add**.
5. Select the organization and resource set to which the instance belongs, and specify a name
for the instance.
6. Click **OK**.
7. Find the instance that you want to manage and click **Configurations** in the **Operation**
column.
8. In the ECS Resources section, click **Associate**, select an ECS instance, and then click **OK**.
9. In the SLB Resources section, click **Associate**, select an SLB instance, and then click **OK**.
0. Click **Configurations** in the **Actions** column of the SLB instance and click **Add Entry**.
1. Configure the SLB listener port and traffic gateway port, and click **OK**.
2. On the **Secondary Region** tab, click **Ingress Gateway for Traffic**.
3. Add the same instance and associate it with the ECS instance and SLB instance by following
the preceding steps.

##### 1.4.2.2 View the topology of an ingress traffic gateway instance

**gateway instance**

This topic describes how to view the topology of an ingress traffic gateway instance.

**Prerequisites**

In the Apsara Uni-manager Management Console, an Elastic Compute Service (ECS) instance is created in the ECS console and a Server Load Balancer (SLB) instance is created in the SLB console. An ingress traffic gateway instance is configured and the virtual private cloud (VPC) where the SLB instance is located is connected to the VPC where the ECS instance is located. For more information, see Create an ingress traffic gateway instance.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console. For more
information, see Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **Instances**.
3. Click the **Primary Region** tab, and then click the **Ingress Gateway for Traffic** tab.
4. Find the ingress traffic gateway instance that you want to manage and click
**Configurations** in the Actions column.
5. On the **Basic Settings** tab, view the topology of the ingress traffic gateway instance.

##### 1.4.2.3 View the monitoring metrics of an ingress traffic gateway instance

**traffic gateway instance**

This topic describes how to view the monitoring metrics of an ingress traffic gateway instance.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console. For more
information, see Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, click **Instances**.
3. On the **Primary Region** tab, click **Ingress Gateway for Traffic**.
4. Find the ingress traffic gateway instance that you want to manage and click **Configure** in
the Actions column.
5. On the page that appears, click the **Monitoring** tab. On this tab, view service performance
metrics and host performance metrics.

### 1.5 DR for business

#### 1.5.1 Protection Groups

##### 1.5.1.1 Manage protection groups

You can create, modify, or delete a protection group. You can also add instances to the protection group, view the details of the protection group, and enable reprotection for the protection group.
1. Log on to the ASR-DR console. For more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.

| Parameter | Description |
|---|---|
| Protection Group Status | The status of the protection group. Valid values: Plan Failed: A step for the scheduled job failed to be run. Running Plan: All plans associated with the protection group are being run. Protection Failed: The protection group fails to be created. You can recreate the protection group for the specified instance. Protecting: The link for the protection group is created. Starting Protection: The link for the protection group is being created. Heavy Protection: The link for the protection group is being recreated. Unknown: The system fails to obtain the status of the protection group. Stop: The protection group is stopped. |
| Synchronization Direction | The direction for the protection group. You can determine the data center in which the instances that provide services are deployed based on the direction. Valid values: Forward: The instances that provide services are deployed in the primary cloud. Backward: The instances that provide services are deployed in the secondary cloud. |
| Maximum synchronization delay | The maximum synchronization latency for all entities in the protection group. |

3. Click the
icon in the **Actions** column that corresponds to a protection group to perform the following operations: Click **Details** to view the details of the protection group and manage the instances that are added to the protection group. For more information, see Protection group details. Click **Modify** to modify the name and description of the protection group. Click **Add entity** to add instances to the protection group. For more information, see Add synchronization entities. Click **Modify Drill Metrics** to configure the expected values of metrics such as the data synchronization latency, switchover duration, and switchback duration. Click **Perform Reprotection** to enable reprotection for the protection group that is in the Protection Failed state. Click **Stop Protection** to temporarily stop the synchronization of a protection group or entity.

> **Note:** You cannot delete protection groups that are associated with recovery plans or drill plans.
> After a protection group is deleted, the hot backup channels between the primary and secondary entities of all resources in the protection group are deleted one after another. Cross-cloud synchronization between the primary and secondary entities stops. One-to-one mappings are also deleted.

Click **Delete** to delete a protection group that you no longer require.

###### 1.5.1.1.1 Create a protection group

A protection group is a group of resources on which disaster recovery is implemented in the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console. You can create a protection group for a set of related resources used by an application.

**Background information**

We recommend that you create up to 20 protection groups. Optional. If you want to create an active-active protection group, purchase a corresponding license in advance.
1. Log in to the ASR for Geo-disaster Recovery console. For more information, see Log on to the
ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, click **Create**.
4. On the **Create Protection Group** page, configure the parameters that are described in
the following table.

| Section | Parameter | Description |
|---|---|---|
| Basic Configurations Note This section displays the basic information about the disaster recovery region. | Organizations | The organization to which the protection group data belongs. |
|   | Resource Set | The resource set to which the instance for disaster recovery belongs. |
|   | Disaster Recovery Relationship | The disaster recovery relationship to which the protection group belongs. |
| Protection Group Information | Name | The name of the protection group. You can specify a custom name. The name must be 4 to 40 characters in length and can contain only letters, digits, hyphens (-), underscores ( ), and _ periods (.). |
|   | Synchronization Direction | The switchover direction. If services are provided by the instances at the primary site, select Forward. If services are provided by the instances at the secondary site, select Backward. Note The synchronization direction for the protection group changes based on the completion of switchovers and switchbacks. After switchovers are complete, Forward changes to Backward. After switchbacks are complete, Backward changes to Forward. |
|   | Protection Group Mode | Primary/Secondary: In primary/secondary mode, the primary site provides services. The secondary site replicates data from the primary site in real time, but does not provide services. When the primary site fails, services are failed over to the secondary site. Active-active: In active-active mode, both the primary and secondary sites provide services. Note You can create a protection group in active-active mode only after you purchase a corresponding license. |
|   | > Document Version: 2026070 |   |

|   | Description | The description of the protection group. You can customize the description for easy identification. |
|---|---|---|

5. Click **Submit**. On the **Protection Groups** page, find the protection group that you created,
and click **Create Entity** in the Actions column.
6. Add synchronization entities as prompted.
For more information about how to add synchronization entities for each cloud service, see Add a synchronization entity.

> If you select **Add and Not Start**, the protection group enters the Stopped state after it is created. In this case, no synchronization link is created in the background, and only the **Start Protection Group** operation can be performed on this protection group. If you do not select this check box, the protection group automatically enters the protected state after it is created.

7. Click **OK**. The protection group is created. On the Protection Groups page, click the
icon to view the status of the protection group.

###### 1.5.1.1.2 Perform reprotection

After a failover, the state of a protection group becomes Protect Failed regardless of the state of the primary cloud. In this case, you must perform reprotection for the protection group.

**Prerequisites**

The state of a protection group is Protect Failed after a failover. If the state of a protection group is Protect Failed during initialization, reprotection is not supported.
1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Disaster Recovery (DR) for Business** >
**Protection Groups**.
3. Select **Protect Failed** from the **Protection Group Status** drop-down list. Click **Search**.
4. In the list of protection groups, find the required protection group, click the
icon in the Actions column, and then click **Reprotection**.
5. In the dialog box that appears, click **OK**.

###### 1.5.1.1.3 Protection group details

You can view the details and operation history of a protection group, and manage the instances and associated plans in the protection group.

###### 1.5.1.1.3.1 View the details of a protection group

You can view the details of a protection group to monitor protection entities in the protection group. The details include the synchronization latency information and inspection information about the protection entities.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. In the protection group list, find the protection group that you want to view and click
**Details** in the **Actions** column.

| Parameter | Description |
|---|---|
| Status | Entity states: Protection Started Protection Failed Protected Plan Executed Tightly Protected Plan Failed Stopped Unknown |
| Synchronization Policy | The following synchronization policies are provided: Full: Each time you implement disaster recovery, all existing data is synchronized to the instances in the secondary cloud. Incremental: Only incremental data is synchronized to the instances in the secondary cloud. |
| Priority | The priority specified for the entity in the protection group. |

| Synchronization Direction | The direction in which data is synchronized. Forward indicates that instances in the primary cloud provide services. Backward indicates that instances in the secondary cloud provide services. |
|---|---|
| Initialization Progress | The percentage of synchronized data during the initialization of the entity. |
| Synchronization Latency | The synchronization latency of the entity. |
| RPO Obtained At | The time at which the recovery point objective (RPO) is calculated. The RPO is a metric for synchronization latency. |

4. On the **Protection Group Details** page, find the entity that you want to manage and click
the icon in the Actions column. Then, you can perform the following operations: Click **Details**. On the Entity Details page, you can view the following information about the instances in the primary cloud and the secondary cloud: basic information, monitoring information about synchronization latency, information about additional configurations, and information about availability inspection.

> **Note:** By default, the entity inspection feature is disabled. You can enable the feature in the background. We recommend that you evaluate potential impacts on your services before you enable the feature.

The parameters for basic information and additional configurations vary based on the services of the instances. The following table describes the parameters on the **Entity**
**Details** page by service.

| Cloud service | Parameter | Description |
|---|---|---|
| ApsaraDB RDS | Configure Privileged Account | The username and password of the privileged account for the primary and secondary ApsaraDB RDS instances. |
|   | Read-only Account | The accounts on which ASR- DR has read-only permissions. The accounts are specified when you create the protection group. |
|   | Start Offset for Incremental Synchronization | The offset from which the system starts to synchronize incremental data. |
| PolarDB-X 2.0 | Read-only Account | The accounts on which ASR- DR has read-only permissions. The accounts are specified when you create the protection group. |
| ApsaraMQ | Configure Topic | The list of topics that you want to synchronize. |
| DNS (Multicloud Integration) | Top-level Domain (TLD) | The global domain name that is managed in ASR-DR. |
|   | Record Value | The DNS record. |
|   | TTL | The time-to-live (TTL) value of the DNS record. |
| MaxCompute | MaxCompute Mapping for Synchronization | The MaxCompute projects that you want to synchronize. |
|   | Synchronization Policy | The data synchronization policy of the MaxCompute instance. |
|   | Synchronization Policy | The data synchronization policy of ApsaraDB for MongoDB. |

| Stack Resilience |   |   |
|---|---|---|
| ApsaraDB for MongoDB |   |   |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the source entity at the primary site. |
|   | Configure Read-only Account | If some ApsaraDB for MongoDB accounts are read- only and you do not want them to be granted read/write permissions during a failover, you can configure this parameter to filter the read-only accounts. |
|   | Configure Shard Account | The names and passwords of the shard accounts for instances at the primary and secondary sites. |
| Elastic Compute Service (ECS) | Synchronization Policy | The data synchronization policy of ECS. |
|   | Select a cloud site pair | The site pair that is created in advance in Hybrid Disaster Recovery (HDR). |
|   | Select a zone | The information about the zone that can be used by the primary cloud and the secondary cloud. |
|   | Network Settings | The VPCs, vSwitches, and protection groups where the ECS instances in the primary cloud and the secondary cloud reside. |
|   | Select an HDR protection group | The protection group to be failed over. |
| Tair (Redis OSS-compatible) | Synchronization Policy | The data synchronization policy of KVStore for Redis. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the source entity at the primary site. |

|   | Configure Read-only Account | If some KVStore for Redis accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can use this parameter to filter the read-only accounts. |
|---|---|---|
| DNS within Cloud | Synchronization Policy | The data synchronization policy of the DNS within Cloud instance. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the source entity at the primary site. |
|   | TTL | The period of time during which domain name resolution information can be retained in DNS within Cloud. |
|   | Smart Resolution Policy | Only Weight is supported. |
|   | Record Value | The weight policy, which is in the following format: the IP address to which the domain name maps, space, and weight (0 to 999). You can find the IP address in the Record Value field of Basic Settings. For more information about domain names, see Global internal d omain names in Apsara Stack DNS User Guide. |

The check items vary based on the services of the instances. The following table describes the check items on the **Entity Inspection** page by service.

| Cloud service | Check item |
|---|---|
|   | Check whether the dnsService domain name can be resolved. |

| Stack Resilience |   |
|---|---|
| DNS |   |
|   | Check whether dnsService ICMP packets can be received. |
|   | Check whether dnsService can be connected. |
|   | Check whether access by using dnsService api : ObtainGlobalAuthZoneListRequest is normal. |
|   | Check whether access by using dnsService api: GetInstance is normal. |
| MaxCompute | Check whether the odps-bcc domain name can be resolved. |
|   | Check whether odps-bcc ICMP packets can be received. |
|   | Check whether odps-bcc can be connected. |
|   | Check whether access by using odps api : GetProtectGroupRequest is normal. |
|   | Check whether access by using odps api : listDataworkInstancesRequest is normal. |
|   | Check whether access by using odps api : GepPlanRequest is normal. |
| OSS | Check whether the oss-chiji domain name can be resolved. |
|   | Check whether oss-chiji ICMP packets can be received. |
|   | Check whether oss-chiji can be connected. |
|   | Check whether access by using oss api : GetOcmBucketMetaXmlRequest is normal. |
| ment Version: 20260701 | 3 |

|   | Check whether access by using oss api : GetLocationListRequest is normal. |
|---|---|
| RDS | Check whether the rds-yaochi domain name can be resolved. |
|   | Check whether rds-yaochi ICMP packets can be received. |
|   | Check whether rds-yaochi can be connected. |
|   | Check whether access by using rds api : DescribeAccountsRequest is normal. |
|   | Check whether access by using rds api : DBInstanceIPArrayListRequest is normal. |
|   | Check whether access by using rds api : DescribeDatabases is normal. |
|   | Check whether access by using rds api : getInstance is normal. |
|   | Check whether access by using rds api : getDBInstanceNetInfo is normal. |
| MQ | Check whether the mq domain name can be resolved. |
|   | Check whether mq ICMP packets can be received. |
|   | Check whether mq can be connected. |
|   | Check whether access by using mq api : listInstances is normal. |
|   | Check whether access by using mq api : queryTaskStatus is normal. |
|   | Check whether access by using mq api : listGroups is normal. |

|   | Check whether access by using mq api : listTopics is normal. |
|---|---|
|   | Check whether access by using mq api : listConsumerGroups is normal. |
|   | Check whether access by using mq api : getBaseInstance is normal. |

When an entity fails to be protected because the entity fails to be connected to the underlying services due to errors such as network errors, click **Reprotection**. The system checks the protection state and determines the next state based on the query result. When changes are made to the tables of ApsaraDB RDS instances or databases of the primary and secondary ApsaraDB RDS instances, entities fail to be protected. For more information about recovery methods, see What do I do if entities fail to be protected?

###### 1.5.1.1.3.2 View a protection entity

You can view the logs of a protection entity to identify and analyze the causes of protection failures.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage and
click its name or click **Details** in the **Actions** column.
4. On the **Protection Group Details** page, click the **Protection Entity** tab.
Optional. View the recovery point objective (RPO) of the protection entity during synchronization.

> **Note:** You can view the RPO of only the protection groups whose instance type is OSS or CDS-OSS.

Move the pointer over the value in the Synchronization Latency column to view the RPO. View the details of a protection entity. a. In the protection entity list, find the entity that you want to view, click the icon in the Actions column, and then click **View Details**. b. On the Entity Details page, view the details of the entity. View the logs of a protection entity. a. In the protection entity list, find the entity that you want to view, click the icon in the Actions column, and then click **View Logs**. In the dialog box that appears, view the logs of the primary and secondary instances.

| Parameter | Description |
|---|---|
| Real-time Update | After you turn on Real-time Update, the logs of the instance are updated every 10 seconds. |
| Log Entries | The number of log entries that you want to display on the current page. Valid values: 100, 500, and 1000. |
| Log Level | The log level. Valid values: Message Error Warning |
| Server | The server on which the synchronization link of the entity runs. |

###### 1.5.1.1.3.3 View the operations records of a protection group

**protection group**

This topic describes how to view the historical operations records of a protection group.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Click the name of the desired protection group or click **Details** in the **Actions** column of
the group.
4. On the **Protection Group Details** page, click the **Operation History** tab.
5. To view the historical operations records of the protection group, click **Details** in the
**Actions** column.

###### 1.5.1.1.3.4 Delete a protection entity

You can remove instances from a protection group if the instances no longer require protection implemented based on disaster recovery (DR). After the instances are removed, the instances are no longer protected, and the related link for DR is interrupted.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the **Protection Groups** page, click the name of the desired protection group or click
**Details** in the **Actions** column of the group.
4. On the **Protection Group Details** page, click the **Protection Entity** tab.
5. Find the instance that you want to delete, click the
icon in the **Actions** column, and then click **Delete**.
6. In the message that appears, click **OK**.

###### 1.5.1.1.3.5 Change the group of a protected entity

You can move an instance to a different protection group. This is useful if your business requirements change or if you accidentally add an instance to the wrong group.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left navigation pane, choose **Business****Disaster Recovery** > **Protection Group**.
3. On the **Protection Groups** page, click the name of the target protection group, or click
**Details** in the **Actions** column.
4. On the **Protection Group Details** page, find the target instance, click the
icon in the
**Actions** column, and then click **Migrate Entity**.
5. (Optional) Configure a global domain name and click **Next**.

> **Note:** You must configure a global domain name when you move an entity from a primary/secondary protection group to an active-active protection group.

| Parameter Name | Description |
|---|---|
| Record Name | Enter a custom name for the record value. |
| Domain Name | The system generates a default global domain name that you can use. If you use a custom domain name and no corresponding domain name exists in DNS, you can use the custom domain name directly. If the global domain is a custom domain name that does not exist in DNS, its record value must match the address of the primary and secondary instances. |
| TTL | The Time to Live (TTL) is the duration that the DNS record for the global domain name is cached on a DNS server. The system generates a default TTL. You can change this value. |
| Bind Public (Internet) Address | Selected: Uses the public IP addresses of the primary and secondary instances as the record value. Cleared: Uses the private or VPC IP addresses of the primary and secondary instances as the record value. |

6. Select a new protection group and click **OK**.

> **Note:** The new protection group must have the same production region organization, disaster recovery region organization, and synchronization direction as the current protection group.

###### 1.5.1.1.3.6 Modify the permissions of read-only accounts

**accounts**

If some accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can filter out the read-only accounts.

**Prerequisites**

This feature is supported by ApsaraDB RDS, PolarDB-X 2.0, ApsaraDB for MongoDB, and Tair (Redis OSS-compatible).
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Find the protection group that you want to manage and click its name or click **Details** in
the **Actions** column.
4. On the **Protection Group Details** page, find the instance that you want to manage, click
the icon in the Actions column, and then click **Modify Permission Granted to Read-**
**only Account**.
5. In the **Update Permission Granted to Read-only Account** dialog box, select a database
from the Database drop-down list and enter an account name.
6. Click **OK**.

###### 1.5.1.1.3.7 Modify the privileged account of an ApsaraDB RDS instance

**ApsaraDB RDS instance**

If the privileged account and password of an ApsaraDB RDS instance is modified in the ApsaraDB RDS console, you must modify the privileged account and password of the instance in the ASR for Geo-disaster Recovery console.

**Prerequisites**

This operation is supported only by ApsaraDB RDS instances .
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the **Protection Groups** page, find the protection group that you want to manage and
click its name or click **Details** in the **Actions** column.
4. On the **Protection Group Details** page, find the instance that you want to manage, click
the icon in the **Actions** column, and then click **Modify Privileged Account**.
5. In the **Modify Privileged Accounts for Primary and Secondary Instances** dialog box,
specify a username and a password for the instances on the primary and secondary sites and click **Modify**.

###### 1.5.1.1.3.8 Manage protection entity account permissions

**permissions**

The Manage Accounts feature allows you to view and modify the permissions of the accounts that are used to log on to the primary instance and secondary instance. This helps you manage instances with ease.

**Prerequisites**

The instance is either an AsparaDB RDS instance or a PolarDB-X instance.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Click the name of the desired protection group or click **Details** in the **Actions** column of
the group.
4. On the **Protection Group Details** page, click the **Protected Entity** tab. Find the instance
that you want to manage, click the icon in the **Actions** column, and then click
**Account Management**.
5. On the **Manage Accounts** page, view and modify the read-only permissions or read and
write permissions of database accounts that are used to log on to the primary instance and secondary instance.

###### 1.5.1.1.3.9 Modify the objects to be synchronized

This topic describes how to modify or add databases and synchronize tables for a PolarDB for MySQL instance after it is added to a protection group.

**Prerequisites**

This feature is supported by ApsaraDB RDS, PolarDB-X 2.0, and ApsaraDB for MongoDB instances.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. Find the protection group that you want to manage and click its name or click **Details** in
the **Actions** column.
4. On the **Protection Group Details** page, click the **Protection Entity** tab, find the instance
that you want to modify, click the icon in the **Actions** column, and then select **Modify**
**Synchronization Object**.
5. In the **Modify Synchronization Object** dialog box, select source objects and click the
icon to add them to the Selected Objects section.
6. Click **OK**.

###### 1.5.1.1.4 Add a synchronization entity

After you create a protection group, you must add instances to the protection group before disaster recovery can be implemented. Limits on the number of instances: The maximum total number of instances in all protection groups is 200. The default maximum total number of protected database instances is 60, including ApsaraDB RDS instances associated with PolarDB-X instances, standalone Apsara RDS instances, ApsaraDB for Redis instances, and ApsaraDB for MongoDB instances. If more than 60 database instances need to be protected, DTS needs to be scaled out, so that a maximum of 100 database instances can be protected. The maximum number of protected ApsaraDB for HBase instances is 20. The maximum number of protected Object Storage Service (OSS) buckets is 20. The maximum number of protected Tablestore instances is 20. The maximum number of protected Elastic Compute Service (ECS) instances is 50. The maximum number of protected Message Queue instances is 20. The maximum number of protected Apsara Stack DNS instances is 20. The maximum number of protected MaxCompute projects is 20. The maximum number of protected DataHub instances is 20.

###### 1.5.1.1.4.1 Configure disaster recovery for ApsaraDB RDS instances

**ApsaraDB RDS instances**

This topic describes how to configure disaster recovery for ApsaraDB RDS instances, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An ApsaraDB RDS instance is created on the primary and secondary clouds in the Apsara Uni- manager Management Console. | Full synchronization scenarios: The primary cloud instance has a database that is to be synchronized. The secondary cloud instance has a database with the same name as the database in the primary cloud instance, but the database in the secondary cloud instance does not have tables. Incremental synchronization scenarios: The database and tables to be synchronized exist on both the primary and secondary cloud instances. The names of the database and tables are identical across both instances. The ApsaraDB RDS instance is not associated with a PolarDB-X instance. |
| Internal and public endpoints are obtained for the primary and secondary cloud instances. | For more information, see "Instances" in ApsaraDB for RDS User Guide. |
| A privileged account and a standard account are created for each of the primary and secondary cloud instances. | For more information, see "Accounts" in ApsaraDB for RDS User Guide. |
| A Resource Access Management (RAM) role for Data Transmission Service (DTS) is created for the organization to which the instances belong. | For more information, see Create a RAM role. |

1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **ApsaraDB**
**RDS** tab in the **Instance Type** section. In the entity list on the left, select the IDs of one or
more instances that you want to add and click the icon to add the instances to the entity list on the right. Then, click **Next**.

> **Note:** If a large number of instances are displayed, enter the instance ID in the **Instance ID** field and click **Filter** to filter the instances.
> In the upper-right corner of the page, the maximum number of instances that can be added is displayed.
> You cannot configure synchronization entities for read-only instances. Read-only instances are not displayed in the entity list.

5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
|   | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |

| Basic Settings |   |   |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: The following data is synchronized: all historical data that is generated before the synchronization task is created and data that is generated after the synchronization task is created or from the specified start offset. Incremental: Only data that is generated after the synchronization task is created or from the specified start offset is synchronized. Note The MySQL engine allows you to specify a start offset for incremental data synchronization. The PolarDB engine does not allow you to specify a start offset for incremental data synchronization. |
|   | (Optional) Start Offset for Incremental Synchronization | You must configure this parameter if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR for Geo-disaster Recovery starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the source entity at the primary site. |
|   | Connect over Express Connect Circuit | If the cloud to which the instance belongs is the same as the cloud on which ASR for Geo-disaster Recovery is deployed, Direct Access is used by default. If the cloud to which the instance belongs is different from the cloud on which ASR for Geo- disaster Recovery is deployed, Access over Express Connect Circuit is used by default. Direct Access: ASR for Geo-disaster Recovery accesses the database instance by using a classic network endpoint or a NAT IP address based on the instance type. Access over Express Connect Circuit: ASR for Geo-disaster Recovery accesses the database instance over the specified virtual private cloud (VPC) in the region. |
|   | Connected VPC | You must configure this parameter if you set the Connect over Express Connect Circuit parameter to Access over Express Connect Circuit. |

| Connection Settings |   |   |
|---|---|---|
|   | Primary Instance Account and Secondary Instance Account | The privileged account names and passwords of the primary and secondary instance databases. If you have created a privileged account in the ApsaraDB RDS console, enter that privileged account and password. If no privileged account is created in the ApsaraDB RDS console, ASR for Geo-disaster Recovery creates a privileged account based on the username and password that you enter. Note Privileged accounts are used only to manage the access of standard accounts. If no privileged account exists, ASR for Geo-disaster Recovery automatically creates a privileged account. However, if no privileged account exists for a PolarDB for Oracle cluster, you must manually create a privileged account and use the privileged account as a synchronization account. After you create the account, the password of the account cannot be changed. The name of the standard account for the ApsaraDB RDS instance in the primary cloud must be the same as the name of the standard account for the ApsaraDB RDS instance in the secondary cloud. If the names are different, ASR for Geo-disaster Recovery does not manage these accounts. |
| Select Synchroniza tion Objects | Enable Database Account Synchronization | After you turn on this switch, the database-related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of passwords, and deletion of accounts. |

| Configure Read-only Account | Database and Read-only Account | The database and the related account of the ApsaraDB RDS instance at the primary or secondary site. During a switchover, ASR for Geo-disaster Recovery grants the ApsaraDB RDS account read/write permissions by default. If some ApsaraDB RDS accounts are read-only and you do not want them to be granted read/write permissions during a switchover, you can configure this parameter to filter out the read-only accounts. |
|---|---|---|
| Global Domain Name Settings Note This paramet er is required only if the Protecti on Group Mode paramet er is set to Active- active. | Record Name | Enter a name for the value of the record. |
|   | Domain Name | A default global domain name is automatically generated, which can be used directly. If the global domain name is a custom domain and no corresponding record exists in the DNS, you can use the name directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, the record value of the global domain name must be consistent between the primary and secondary instances. |
|   | TTL | The period of time that a DNS record can be cached on a DNS server. A default TTL (time-to- live) is generated automatically, which can be modified by users. |
|   | Bind Public Endpoint | If you select this item, the public endpoints of the primary and secondary instances of the synchronization entity are used as the record values in the global domain name. If you do not select this item, the virtual private cloud (VPC) endpoints or internal endpoints of the primary and secondary instance of the synchronization entity are used as the record values. |

After you specify the global domain name, click **Precheck**. If no problem is detected, click
**Next**.
6. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.2 Configure disaster recovery for PolarDB-X 2.0 instances

**PolarDB-X 2.0 instances**

This topic describes how to configure disaster recovery for PolarDB-X V2.0 instances, including prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A PolarDB-X V2.0 instance is created for each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | A PolarDB-X V2.0 instance is created for each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. |
| A database is created for the instance at the primary site. | The database contains tables to be synchronized, and the tables are checked. |

1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, and
click **Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **PolarDB-**
**X V2.0** tab in the **Instance Type** section. In the left-side entity list, select the IDs of one or
more instances that you want to add. Click the icon to add the instances to the rightside entity list. Click **Next**.

> **Note:** You cannot configure synchronization entities for read-only instances. Read-only instances are not displayed in the entity list.

5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|

| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|   | Start Offset for Incremental Synchronization | You must configure this parameter if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR for Geo-disaster Recovery starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site. The entity is used as the hot standby resource of the source entity at the primary site. |
|   | Connect over Express Connect Circuit | If the cloud to which the instance belongs is the same as the cloud on which ASR for Geo-disaster Recovery is deployed, Direct Access is used by default. If the cloud to which the instance belongs is different from the cloud on which ASR for Geo- disaster Recovery is deployed, Access over Express Connect Circuit is used by default. Direct Access: ASR for Geo-disaster Recovery accesses the database instance by using a classic network endpoint or a NAT IP address based on the instance type. Access over Express Connect Circuit: ASR for Geo-disaster Recovery accesses the database instance over the specified virtual private cloud (VPC) in the region. |
|   | Connected VPC | You must configure this parameter if you set the Connect over Express Connect Circuit parameter to Access over Express Connect Circuit. |

| Connection Settings |   |   |
|---|---|---|
|   | Primary Instance Account and Secondary Instance Account | The privileged account names and passwords of the primary and secondary instance databases. If you have created a privileged account in the PolarDB-X V2.0 console, enter that privileged account and password. If no privileged account is created in the PolarDB-X V2.0 console, ASR for Geo-disaster Recovery creates a privileged account based on the username and password that you enter. Note Privileged accounts are used only to manage the access of standard accounts. If no privileged account exists, ASR for Geo-disaster Recovery automatically creates a privileged account. The name of the standard account for the PolarDB-X 2.0 instance in the primary cloud must be the same as the name of the standard account for the PolarDB-X 2.0 instance in the secondary cloud. If the names are different, ASR for Geo-disaster Recovery does not manage these accounts. |
| Select Synchronization Objects | Enable Database Account Synchronization | Important In Apsara Stack V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After this switch is turned on, the database- related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of passwords, and deletion of accounts. |

| Configure Read- only Account | Database and Read- only Account | The database and the corresponding account on the PolarDB-X V2.0 instance at the primary site. During a switchover, ASR for Geo-disaster Recovery automatically grants the PolarDB-X V2.0 account read/write permissions by default. If some PolarDB-X V2.0 accounts are read-only and you do not want them to be granted read/write permissions during a switchover, you can use this parameter to filter these read-only accounts. |
|---|---|---|
| Global Domain Name Settings Note You must configure this parameter only if the mode of the protection group is active-active. | Record Name | The name for the value of the record. You can specify a custom name. |
|   | Domain Name | A default global domain name is automatically generated, which can be used directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, you can use the name directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, the record value of the global domain name must be consistent between the primary and secondary instances. |
|   | TTL | The period of time that a DNS record can be cached on a DNS server. A default time to live (TTL) is generated automatically, which can be modified by users. |
|   | Bind Public Endpoint | If you select this option, the public endpoints of the primary and secondary instances of the synchronization entity are used as the record values in the global domain name. If you do not select this option, the VPC endpoints or internal endpoints of the primary and secondary instances of the synchronization entity are used as the record values. |

After you specify the global domain name, click **Precheck**. If no problem is detected, click
**Next**.
6. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.3 PolarDB for MySQL

This topic describes how to configure disaster recovery for PolarDB instances that use local disks or shared storage.

**Prerequisites**

A PolarDB instance (local disk or shared storage) has been created in the Apsara Uni-manager Management Console for both the primary and standby cloud instances. After you create a PolarDB instance that uses shared storage, you must manually enable binary logging (Binlog). Enabling Binlog restarts the database. Perform this operation during off-peak hours to avoid service interruptions.
1. Log on to the ASR for Geo-disaster Recovery (ASR-DR) console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Groups**.
3. In the **Actions** column of the target protection group, click **Add Entity**.
4. On the **Add Entity** page, set **Instance Type** to **PolarDB**.
5. From the storage type drop-down list, select **PolarDB Local Disk** or **PolarDB Shared**
**Storage**.
6. In the entity list on the left, select the target instance and click the
icon to move it to the entity list on the right. Then, click **Next**.

> **Note:** If many instances exist, you can enter the instance name in the **Instance Name** field and click **Filter** to locate the instance.
> You cannot configure sync entities for read-only instances. Read-only instances are not displayed in the entity list.

7. On the **Select Instance Priority and Resource Mapping** page, click the
icon in the
**Actions** column of the target instance and select **Configure**. Configure the parameters
and click **Next**. The following table describes the parameters.

| Configuration group | Configuration | Description |
|---|---|---|

| Basic configuration | Priority | ASR-DR performs drills or recoveries on resources based on this priority. A smaller value indicates a higher priority. Important Set priorities based on data dependencies. A resource that other resources depend on has a higher priority. |
|---|---|---|
|   | Synchronization policy | Full + Incremental: Synchronizes all historical data from before the sync task was created, and all incremental data generated after the task was created or from a specified point in time. Incremental: Synchronizes only the incremental data generated after the sync task was created or from a specified point in time. |
|   | Incremental sync start offset (Optional) | This parameter is required if you set Synchronization policy to Incremental. Select the date and time from which ASR-DR starts to synchronize incremental data. |
|   | Resource mapping | The target instance at the disaster recovery site. This instance serves as the hot standby resource for the production site instance. |
|   | Connect over a leased line | Specifies the connection method. If the instance and ASR-DR are deployed in the same cloud, the default method is direct access. If they are in different clouds, the default method is leased line access. Direct access: The disaster recovery service connects to the database instance using its classic network address or a NAT address, based on the instance type. Leased line access: The disaster recovery service connects to the database instance using a VPC that you specify in the current region. |
|   | VPC connected to the database | Optional. This parameter is required if you set Connect over a leased line to Leased line access. |

| Connection |   |   |
|---|---|---|
|   | Username and password for the primary and secondary instance accounts | The username and password of the privileged account for the primary and secondary database instances. If a privileged account is already created in the PolarDB console, enter that account's credentials here. If not, ASR-DR creates a privileged account using the username and password that you provide. Note Privileged accounts are used only to manage connections for standard accounts. If a privileged account does not exist, ASR-DR creates one for you. The exception is for PolarDB for PostgreSQL (Compatible with Oracle) instances. For these instances, you must create the privileged account yourself. This account is used for synchronization, and its password cannot be changed. Use the same username for the standard accounts on the source and destination PolarDB instances. |
| configuration |   |   |

| Select synchronization objects | Enable database account synchronization | Important In V3.18.0, the Enable database account synchronization switch is disabled and cannot be enabled. When enabled, database-related accounts are synchronized to the destination instance. New accounts and changes to permission scopes are also continuously synchronized. Note The following operations are not synchronized: creating an account that already exists at the destination, changing a password, and deleting an account. |
|---|---|---|
| Configure read- only account (Optional) | Database and read- only account | The database and corresponding account on the PolarDB instance at the production site. During a switchover, ASR-DR grants the PolarDB account read and write permissions by default. If some PolarDB accounts are read-only and you do not want them to be granted read and write permissions during the switchover, use this setting to filter out those accounts. |
| Global domain name configuration Note This parameter is required only if Protection Group Mode is set to Active- active. | Record name | Enter a custom name for the record. |
|   | Domain name | You can use the default global domain name that is automatically generated. You can use a custom domain name that is not yet configured in DNS. If the global domain is a custom domain name without a corresponding DNS record, its record value must be the address of the primary and secondary instances. |
|   | TTL | The Time to Live (TTL) for the DNS record. The TTL specifies how long the record is cached on a DNS server. A default TTL is generated, which you can modify. |
|   | Bind public (Internet) address | Selected: Uses the public or Internet addresses of the primary and secondary instances as the record value for the global domain name. Not selected: Uses the VPC or internal network addresses of the instances as the record value. |

After you configure the global domain name, click **Precheck**. If no issues are found, click
**Next**.
8. After the configuration is complete, preview the settings. If the settings are correct, click
**Confirm**. On the protection group list page, click the
icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.4 PolarDB for PostgreSQL

This topic describes how to configure disaster recovery for PolarDB for PostgreSQL instances.

**Prerequisites**

A PolarDB for PostgreSQL instance with local disks or shared storage has been created on both the primary and secondary cloud instances in the Apsara Uni-manager Management Console.

**Configuration steps**

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Groups**.
3. For the target protection group, click **Add Entity** in the **Actions** column.
4. On the **Add Entity** page, set the **Instance Type** to **Cloud-native Relational Database**
**PolarDB**.
5. In the **Storage Type** drop-down list, select **PolarDB Local Disk** or **PolarDB Shared Disk**.
In the **Database Type** drop-down list, select a supported database engine.
6. In the entity list on the left, select an instance ID and click the
icon to add the instance to the entity list on the right. Then, click **Next**.

> **Note:** To quickly find a specific instance, enter the instance name in the **Instance** **Name** search box and click **Filter**.
> You cannot configure synchronization entities for read-only instances. Read-only instances are not displayed in the entity list.

7. On the **Select Instance Priority And Resource Mapping** page, click the
icon in the
**Actions** column for the target instance and select **Configure**. Configure the parameters
and click **Next**. The following table describes the parameters.

| Configuration | Configuration | Description |
|---|---|---|

| Basic Settings | Priority | ASR for Geo-disaster Recovery performs drills or recoveries on resources based on this priority. A smaller value indicates a higher priority. Important Set priorities based on data dependencies. Cloud products that are dependencies for other products have higher priorities. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes all historical data from before the sync task was created, and all incremental data generated after the task was created or from a specified time. Incremental: Synchronizes only the incremental data generated after the sync task was created or from a specified time. |
|   | Start Offset for Incremental Synchronization (Optional) | This parameter is required if you set Synchronization Policy to Incremental. Select a date and time. ASR for Geo-disaster Recovery will start to synchronize incremental data from this point in time. |
|   | Resource Mapping | The destination instance at the disaster recovery site. This instance serves as a hot standby resource for the source instance. |
|   | Connect via leased line | If the instance and ASR for Geo-disaster Recovery are deployed in the same cloud, the system uses direct access by default. If they are deployed in different clouds, the system uses leased line access by default. Direct access: The disaster recovery service uses the classic network address or a NAT address to access the database instance, depending on the instance type. Leased line access: The disaster recovery service uses the VPC that you specify in the current region to access the database instance. |
|   | VPC connected to the database | Optional. This parameter is required if you set Connect via leased line to Leased line access. |

| Connection Configuration |   |   |
|---|---|---|
|   | Username and password for the primary and secondary instance accounts | The privileged account username and password for the primary and secondary database instances. If you have already created a privileged account in the PolarDB console, enter the credentials for that account. If you have not created a privileged account in the PolarDB console, ASR for Geo-disaster Recovery creates one based on the username and password you enter. Note Privileged accounts are used only to manage connections for standard accounts. If a privileged account does not exist, ASR for Geo-disaster Recovery creates one for you. This does not apply to PolarDB for Oracle. For PolarDB for Oracle, you must create a privileged account. This account is used for synchronization and its password cannot be changed. Ensure the standard account username is the same on both the source and destination PolarDB instances. |
| Select Synchronization Objects | Enable database account synchronization | Important In version 3.18.0, the Enable database account synchronization switch is disabled and cannot be enabled. When enabled, accounts related to the database are synchronized to the destination instance. New accounts and changes to permission scopes are also continuously synchronized. Note The following operations are not synchronized: creating an account that already exists on the destination instance, changing a password, and deleting an account. |

| Configure Read- only Account (Optional) | Database, Read-only account | The database and its corresponding account on the source PolarDB instance. During a failover, ASR for Geo-disaster Recovery sets the PolarDB account to have read and write permissions by default. If some PolarDB accounts are read-only and you do not want them to be granted read and write permissions during a failover, you can filter out these accounts using this setting. |
|---|---|---|
| Global Domain Name Configuration Note This parameter is required only when Protection Group Mode is set to Active- active. | Record Name | A custom name for the record value. |
|   | Domain Name | You can use the default global domain name that is automatically generated. If you use a custom domain name that is not yet configured in DNS, you can specify it here. If you use a custom domain name that is not yet configured in DNS, the record value for this domain name must be the same as the addresses of the primary and secondary instances. |
|   | TTL | The time to live (TTL) of the DNS record on a DNS server. A default TTL is generated, which you can modify. |
|   | Bind public (Internet) address | Selected: Uses the public or Internet addresses of the primary and secondary instances as the global domain name record value. Not selected: Uses the VPC or internal network addresses of the primary and secondary instances as the record value. |

After you configure the global domain name, click **Precheck**. If no issues are found, click
**Next**.
8. After completing the configuration, preview the settings. If they are correct, click **Confirm**.
On the protection group list page, click the icon to view the status of the protection group. After the protection group is created, the system begins an initialization process. If initialization fails, retry the operation. Once initialization is complete, check the group's status. If the status is Protection Failed, click**Reprotect**.

###### 1.5.1.1.4.5 Configure disaster recovery for OSS buckets

**buckets**

This topic describes how to configure disaster recovery for Object Storage Service (OSS) buckets or CDS-OSS instances, including the prerequisites and procedure.

**Background information**

OSS is divided into OSS 1.0 and CDS-OSS. OSS 1.0 is the original OSS service, and CDS-OSS is a new service form known as cloud-defined storage. You must select the corresponding CDS- OSS cluster when you create a CDS-OSS resource. Unless otherwise specified, the descriptions in this topic apply both to OSS 1.0 and CDS-OSS.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An OSS or CDS-OSS instance is created on each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | The secondary instance must be empty in full protection scenarios. The versioning feature must be either enabled for the instances on both the primary and secondary sites, or disabled on both. The maximum number of protected OSS buckets is 20. |

1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, and
click **Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Object**
**Storage Service** tab in the **Instance Type** section. In the entity list on the left, select the
IDs of one or more instances that you want to add and click the icon to add the instances to the entity list on the right. Then, click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Configuration step | Parameter | Description |
|---|---|---|

| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. Note You cannot specify a start offset for incremental synchronization. |
|   | Synchronization Object | You can leave this parameter empty to synchronize all files or specify a prefix to synchronize files with the prefix. Note The prefix cannot start with a forward slash (/). Separate prefixes with commas (,). You cannot modify the prefix of the synchronization entity after you specify it. |

|   | Synchronization Policy | You can select Add/Change or Add/Delete/Change from the Synchronization Policy drop- down list. |
|---|---|---|
|   | Set Destination to Read- only | If you select this option, during the initialization, switchover, and switchback of the synchronization entity, data cannot be written to the destination OSS bucket. Only read operations are supported. |
|   | Resource Mapping | The destination entity at the secondary site. The entity is used as the hot standby resource of the source entity at the primary site. |
| Global Domain Name Settings Note | Record Name | The name for the value of the record. You can specify a custom name. |
|   | Domain Name | A default global domain name is automatically generated, which can be used directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, you can use the name directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, the record value of the global domain name must be consistent between the primary and secondary instances. |
|   | TTL | The period of time that a DNS record can be cached on a DNS server. A default time to live (TTL) is generated automatically, which can be modified by users. |
| You must configure this parameter only if the mode of the protection group is active-active. |   |   |

|   | Bind Public Endpoint | If you select this option, the public endpoints of the primary and secondary instances of the synchronization entity are used as the record values in the global domain name. If you do not select this option, the virtual private cloud (VPC) endpoints or internal endpoints of the primary and secondary instances of the synchronization entity are used as the record values. |
|---|---|---|

After you specify the global domain name, click **Precheck**. If no problem is detected, click
**Next**.
6. After the configuration is complete, you can preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protection Failed state, click **Reprotect** in the Actions column of the protection group.
> For OSS, when you create a full protection group, you must wait about 90 to 110 minutes before full synchronization actually starts due to product limits.

###### 1.5.1.1.4.6 Big data products

This topic describes how to configure disaster recovery for DataWorks and MaxCompute synchronization entities, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A DataWorks instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console. | Both primary and secondary DataWorks instances have MaxCompute projects and compute units (CUs). Both primary and secondary DataWorks workspaces have the same name. |
| A MaxCompute instance is created in the primary cloud and the secondary cloud by using the Apsara Uni-manager Management Console. | The organization of the cloud account used to execute jobs, number of CUs, storage space of MaxCompute projects, and engine names must be consistent between the primary and secondary MaxCompute projects. The maximum number of protected MaxCompute projects is 20. |

The procedure of configuring disaster recovery for MaxCompute and that for DataWorks are similar. MaxCompute is used in the following example.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the
**MaxCompute** tab in the **Instance Type** section. In the left-side entity list, select the
instance ID. Click the icon to add the instance to the right-side entity list. Click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the instance, click the
icon in the **Actions** column, and then click **Configure**. Configure the parameters based on your business requirements and click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller number indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: synchronizes new data after the synchronization task is created. Note MaxCompute does not support synchronizing new data from a specific offset. |
| Document Version: 20260701 | 6 |   |

|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
|---|---|---|
| MaxCompute Mapping for Synchronization | Source MaxCompute Project and Destination MaxCompute Project | The MaxCompute projects to be synchronized in DataWorks. Note The source project names must be the same as the destination project names in cross-cloud disaster recovery scenarios. |
|   | Synchronization Policy Configurations | Filters out tables, resources, and functions for synchronization. |
| Configure Policy | Timing trigger synchronization | The point in time to trigger synchronization every day. |
|   | Callback Method | The callback method. You can select Manual Business or Manual Business Process. |
|   | Callback Node ID | The ID of the callback node. |
|   | Synchronization Policy for DataWorks Project | The resources to be synchronized from the DataWorks project and the ID of the callback node after the synchronization is triggered. |

6. After the configuration is complete, preview the configurations and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the state is Protect Failed, click **Reprotection**.

###### 1.5.1.1.4.7 DNS (Multicloud Integration)

This topic describes how to configure disaster recovery for the synchronization entities of DNS (Multicloud Integration), including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| The DNS control domains are merged. | The disaster recovery of Apsara Stack DNS ensures the global consistency of domain name resolution through cluster synchronization. In this solution, the tenant-side DNS server serves as a global server loading balancer (GSLB) to route the traffic that is destined for the primary data center to the secondary data center when a fault occurs. The DNS control domains of the primary and secondary data centers are merged to form a complete Raft cluster to ensure that the domain names in the cluster are consistent. You can specify the weights of the domain names to implement traffic switchover. For information about how to merge control domains, see the ASR-DR O&M Guide. |
| The same global domain names and host records are created in the Apsara Uni-manager Management Console at the primary and secondary sites. | The maximum number of protected Apsara Stack DNS instances is 20. |

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **DNS**
**(Multicloud Integration)** tab in the **Instance Type** section. Specify the domain name,
select one or more hosts in the entity list on the left, and click the icon to move the hosts to the entity list on the right. Then, click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. The following table describes the parameters that you can configure.

| Configure step | Parameter | Description |
|---|---|---|
|   | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller value indicates a higher priority. Note The priority for DNS (Multicloud Integration) can be set only to 1. |

| tions in the Apsara Uni- Management Console |   |   |
|---|---|---|
| Basic Settings |   |   |
|   | Synchronization Policy | DNS (Multicloud Integration) supports only Full + Incremental. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Select Domain Name | The DNS domain name that you want to protect. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Configure DNS Record | Host Record | The DNS resolution record. For more information, see "Global internal domain names" in Apsara Stac k DNS User Guide. |
|   | Record Type | CNAME- maps one domain name to another and A- maps a domain name to an IPv4 address are supported. |
|   | TTL | The period during which domain resolution information is retained in DNS (Multicloud Integration). |
|   | Smart Resolution Policy | Only Weight is supported. |
|   | Record Value | Specify a weight policy in the following format: the domain name (fully qualified domain name with a period), space, and weight (0 to 999). For more information about domain names, see Global inter nal domain names in Apsara Stack DNS User Guide. Important Make sure that the domain name of the primary data center precedes the domain name of the secondary data center. |

6. After the configuration is complete, preview the configurations and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the state is Protect Failed, click **Reprotection**.

###### 1.5.1.1.4.8 Private domain name resolution (DNS)

This topic describes how to configure synchronization entities for DNS (Cloud). During a switchover, ASR-DR adjusts the DNS weights of the virtual IP addresses (VIPs) for the global internal domain names.

**Prerequisites**

| Domain names must be created at both the production site and the disaster recovery site. | The configuration and number of domain names at the production site must be identical to those at the disaster recovery site. |
|---|---|

1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Groups**.
3. Click **Add Entity** in the **Actions** column of the target protection group.
4. On the **Add Synchronization Entity** page, set **Instance Type** to **DNS (Cloud)**. Select the
domain names from the list and click the icon to move them to the list on the right. Then, click **Next** to open the **Select Instance Priority and Resource Mapping** page.
5. On the **Select Instance Priority and Resource Mapping** page, in the **Actions** column
for the target instance, click and select **Configure**. Configure the **Basic Settings** and
**DNS Record Settings** as needed. Click **Confirm**, and then click **Next**. The following table
describes the parameters.

| Config | Configuration | Description |
|---|---|---|
| Basic Settings | Priority | ASR-DR performs drills or recoveries on resources based on this priority. A smaller value indicates a higher priority. Note The priority can only be set to 1. |

|   | Synchronization Policy | Only Full Sync + Incremental Sync is supported. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|---|---|---|
|   | Resource Mapping | The domain name of the DNS to be protected. |
| DNS Record Settings | DNS Record Name | Enter a name for the DNS record. The domain name is appended to the record name. |
|   | TTL | The duration for which the domain name resolution information is cached in DNS (Cloud). |
|   | Production Endpoint Record Value | Configure the weight policy for the production endpoint. The format is: domain name, IP address, space, and weight (0 to 999). For the IP address, use the IP from the Record Value column of the host in the basic information. For more information, see "Configure global internal domain names" in the Apsara Stack DNS User Guide. |
|   | Disaster Recovery Endpoint Record Value | Configure the weight policy for the disaster recovery endpoint. The format is: domain name, IP address, space, and weight (0 to 999). For the IP address, use the IP from the Record Value column of the host in the basic information. For more information, see "Configure global internal domain names" in the Apsara Stack DNS User Guid e. |
| Routing Rule Settings | Production Application Endpoint Weight | The percentage of traffic routed to the production application endpoint. Enter an integer from 0 to 100. |
|   | Disaster Recovery Application Endpoint Weight | The percentage of traffic routed to the disaster recovery application endpoint. Enter an integer from 0 to 100. |

6. After you complete the configuration, you can preview it. If the settings are correct, click
**Confirm**. On the Protection Groups page, click the
icon to view the status of the protection group.

> **Note:** After a protection group is created and initialized, check its status. If the status is Protection Failed, perform a **re-protection**.

###### 1.5.1.1.4.9 Message Queue

This topic describes how to configure disaster recovery for Message Queue, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A Message Queue instance, a topic, and a group are created on each of the primary and secondary cloud instances by using the Apsara Uni- manager Management Console. | The Message Queue instances on the primary and secondary cloud instances must have the same name, topic, and group. The maximum number of protected Message Queue (MQ) instances is 20. |

1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Message**
**Queue** tab in the **Instance Type** section. In the left-side entity list, select the instance IDs,
click the icon to add the instances to the right-side entity list, and then click **Next**.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then select **Configure**. Configure **basic settings** and **select a topic** based on your business requirements, and then click **Next**. The following table describes the parameters that you can configure.

| Configuration step | Parameter | Description |
|---|---|---|
|   | Priority | The priority based on which ASR-DR performs drills or recoveries on resources. A smaller number indicates a higher priority. Note The priority for Message Queue can be set only to 2. |

| Basic Settings |   |   |
|---|---|---|
|   | Synchronization Policy | Only Incremental is supported for Message Queue. Incremental means that only incremental data is synchronized to the instances at the secondary site. The synchronization starts when the synchronization entity is created. Note Message Queue does not support synchronizing new data from a specific offset. |
|   | Resource Mapping | The destination entity at the secondary site that is used as the hot standby resource of the primary site entity. |
| Select a topic | Topic Name | The topics to be protected at the primary site. |

6. After the configuration is complete, you can preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.10 Message Queue for Kafka

This topic describes the prerequisites and procedure for configuring disaster recovery for Kafka instances.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| You have created a Kafka instance and a topic on both the primary and secondary cloud instances in the Apsara Uni-manager Management Console. | The topics that require remote disaster recovery on the primary and secondary Kafka instances must have the same name and the same number of partitions. |

1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Groups**.
3. In the **Actions** column of the target protection group, click **Add Entity**.
4. On the **Add Synchronization Entity** page, set **Instance Type** to **Message Queue for**
**Kafka**. In the entity list on the left, select the instance ID of the production site and click
the icon to move the instance to the entity list on the right. Click **Next** to proceed to the **Select Instance Priority and Resource Mapping** page.
5. On the **Select Instance Priority and Resource Mapping** page, click
in the **Actions** column of the target instance and select **Configure**. Configure the **Basic Configurations** and **Select Message Topic** settings as required, and then click **Next**. The following table describes the configurations in detail.

| Config | Configuration | Description |
|---|---|---|
| Basic Configurations | Priority | ASR-DR drills or recovers resources based on this priority. The smaller the number, the higher the priority. Note The priority for Kafka can only be set to 2. |
|   | Synchronization Policy | Full + Incremental Synchronization Incremental Synchronization from a Specific Time Incremental Synchronization from the Latest Offset Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Resource Mapping | The target instance at the disaster recovery site. This instance serves as the hot standby resource for the production site instance. |
| Select topics | Topic name | The message topic on the production site that requires disaster recovery protection. |

| Select Replicator | Select a Replicator in the production region or disaster recovery region | Select a Replicator for both the primary and secondary ends. If no active Replicator exists, click Create to create a resource in Kafka. |
|---|---|---|

6. After the configuration is complete, you can preview the settings. If the settings are correct,
click **Confirm**. On the protection groups page, click the icon to view the status of the protection group.

> **Note:** After a protection group is created, the system performs an initialization. When the initialization is complete, check the status of the protection group. If the status is Protection Failed, perform the **Reprotect** operation.

###### 1.5.1.1.4.11 Configure disaster recovery for Tair (Redis OSS-compatible) instances

**(Redis OSS-compatible) instances**

This topic describes how to configure disaster recovery for Configure disaster recovery for Tair (Redis OSS-compatible) instances, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| A Tair (Redis OSS-compatible) instance is created on each of the primary and secondary cloud instances by using the Apsara Uni-manager Management Console. | In full synchronization scenarios, the primary Tair (Redis OSS-compatible) instance can have data, but the secondary Tair (Redis OSS-compatible) instance cannot have data. |
| An internal endpoint is obtained for each of the primary and secondary Tair (Redis OSS- compatible) instances. | For more information, see the Instance management topics in Tair (Redis OSS- compatible) User Guide. |
| A privileged account and a standard account are created for the primary and secondary cloud instances. | For more information, see the Instance management > Manage database accounts topic in Tair (Redis OSS-compatible) User Guide. |
| A Resource Access Management (RAM) role for Data Transmission Service (DTS) is created for the organization to which the instance belongs. | For more information, see Create a RAM role. |

1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, and
click **Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **KVStore**
**for Redis** tab in the **Instance Type** section. In the left-side entity list, select the IDs of one
or more instances that you want to add. Click the icon to add the instances to the right-side entity list. Click **Next** to go to the **Configure Priority and Resource Mapping** step.
5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. |
|   | Synchronization Policy | Only Full + Incremental is supported. Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Resource Mapping | The destination entity at the secondary site. The entity is used as the hot standby resource of the source entity at the primary site. |
| Connection Settings | Connect over Express Connect Circuit | If the cloud to which the instance belongs is the same as the cloud on which ASR for Geo-disaster Recovery is deployed, Direct Access is used by default. If the cloud to which the instance belongs is different from the cloud on which ASR for Geo- disaster Recovery is deployed, Access over Express Connect Circuit is used by default. Direct Access: ASR for Geo-disaster Recovery accesses the database instance by using a classic network endpoint or a NAT IP address based on the instance type. Access over Express Connect Circuit: ASR for Geo-disaster Recovery accesses the database instance over the specified virtual private cloud (VPC) in the region. |
| Document Versi | on: 20260701 7 |   |

|   | Connected VPC | You must configure this parameter if you set the Connect over Express Connect Circuit parameter to Access over Express Connect Circuit. |
|---|---|---|
| Select Synchroniz ation Objects | Enable Database Account Synchronization | Important In Apsara Stack V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After this switch is turned on, the database-related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of passwords, and deletion of accounts. |
| Configure Read-only Account | Read-only Account | The database and the corresponding account on the Tair (Redis OSS-compatible) instance at the primary or secondary site. During a switchover, ASR for Geo-disaster Recovery automatically grants the Tair (Redis OSS- compatible) account read/write permissions by default. If some Tair (Redis OSS-compatible) accounts are read-only and you do not want them to be granted read/write permissions during a switchover, you can use this parameter to filter out the read-only accounts. |

| Global Domain Name Settings Note You must configur e this parame ter only if the mode of the protecti on group is active- active. | Record Name | The name for the value of the record. You can specify a custom name. |
|---|---|---|
|   | Domain Name | A default global domain name is automatically generated, which can be used directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, you can use the name directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, the record value of the global domain name must be consistent between the primary and secondary instances. |
|   | TTL | The period of time that a DNS record can be cached on a DNS server. A default time to live (TTL) is generated automatically, which can be modified by users. |
|   | Bind Public Endpoint | If you select this option, the public endpoints of the primary and secondary instances of the synchronization entity are used as the record values in the global domain name. If you do not select this option, the VPC endpoints or internal endpoints of the primary and secondary instances of the synchronization entity are used as the record values. |

After you specify the global domain name, click **Precheck**. If no problem is detected, click
**Next**.
6. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protection Failed state, click **Reprotect** in the Actions column of the protection group.

###### 1.5.1.1.4.12 Configure disaster recovery for ApsaraDB for MongoDB instances

**ApsaraDB for MongoDB instances**

This topic describes how to configure disaster recovery for ApsaraDB for MongoDB instances, including the prerequisites and procedure.

**Prerequisites**

| Prerequisite | Description |
|---|---|
| An ApsaraDB for MongoDB instance is created in both the primary and secondary clouds by using the Apsara Uni-manager Management Console. | Full synchronization scenarios: Each database to be synchronized must exist on both the primary and secondary instances under the same name. Crucially, each of these databases on the secondary instance must not contain any collections before the synchronization starts. Incremental synchronization scenarios: The databases and the specific collections to be synchronized must exist on both the primary and secondary instances. The names of the corresponding databases and collections must be identical across both instances. |
| Internal endpoints and external endpoints are obtained for the instances that are deployed in the primary and secondary clouds. | For more information, see the Instance management topics in ApsaraDB for MongoDB User Guide. |
| A Resource Access Management (RAM) role for Data Transmission Service (DTS) is created for the organization to which the instance belongs. | For more information, see Create a RAM role. |

1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, and
click **Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **ApsaraDB**
**for MongoDB** tab in the **Instance Type** section. In the left-side entity list, select the IDs of
one or more instances that you want to add. Click the icon to add the instances to the right-side entity list. Click **Next** to go to the **Configure Priority and Resource Mapping** step.
5. In the **Configure Priority and Resource Mapping** step, find the instance that you want
to manage, click the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Section | Parameter | Description |
|---|---|---|

| Basic Settings | Priority | The priority based on which ASR for Geo- disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependencies has a higher priority. |
|---|---|---|
|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|   | Start Offset for Incremental Synchronization | You must configure this parameter if you set the Synchronization Policy parameter to Incremental. You can specify the date and time from which ASR for Geo-disaster Recovery starts to synchronize incremental data. |
|   | Resource Mapping | The destination entity at the secondary site. The entity is used as the hot standby resource of the source entity at the primary site. |
| Connection Settings Note You must configure this parameter if the instance is a replica set instance. | Connect over Express Connect Circuit | If the cloud to which the instance belongs is the same as the cloud on which ASR for Geo-disaster Recovery is deployed, Direct Access is used by default. If the cloud to which the instance belongs is different from the cloud on which ASR for Geo- disaster Recovery is deployed, Access over Express Connect Circuit is used by default. Direct Access: ASR for Geo-disaster Recovery accesses the database instance by using a classic network endpoint or a NAT IP address based on the instance type. Access over Express Connect Circuit: ASR for Geo-disaster Recovery accesses the database instance over the specified virtual private cloud (VPC) in the region. |
| Document Version: 202607 | 01 8 |   |

|   | Connected VPC | You must configure this parameter if you set the Connect over Express Connect Circuit parameter to Access over Express Connect Circuit. |
|---|---|---|
|   | Database/Synchroniza tion Object | The databases and objects in the ApsaraDB for MongoDB instance to be synchronized from the primary cloud to the secondary cloud. You can also synchronize the entire instance. |
| Select Synchronization Objects |   |   |
|   | Enable Database Account Synchronization | Important In Apsara Stack V3.18.0, the Enable Database Account Synchronization switch is off and cannot be turned on. After this switch is turned on, the database- related accounts are synchronized to the destination site and the new account and permission scope changes related to the databases are continuously synchronized. Note The following operations are not synchronized: creation of an account that is named the same as one in the destination cloud, change of passwords, and deletion of accounts. |
| Configure Read-only Account | Read-only Account | The database and the corresponding account on the ApsaraDB for MongoDB instance at the primary or secondary site. During a switchover, ASR for Geo-disaster Recovery grants the ApsaraDB for MongoDB account read/write permissions by default. If some ApsaraDB for MongoDB accounts are read-only and you do not want them to be granted read/write permissions during a failover, you can use this parameter to filter out the read-only accounts. |

| Configure Shard Account Note You must configure this parameter if the instance is a sharded cluster instance. | Connect over Express Connect Circuit | If the cloud to which the instance belongs is the same as the cloud on which ASR for Geo-disaster Recovery is deployed, Direct Access is used by default. If the cloud to which the instance belongs is different from the cloud on which ASR for Geo- disaster Recovery is deployed, Access over Express Connect Circuit is used by default. Direct Access: ASR for Geo-disaster Recovery accesses the database instance by using a classic network endpoint or a NAT IP address based on the instance type. Access over Express Connect Circuit: ASR for Geo-disaster Recovery accesses the database instance over the specified virtual private cloud (VPC) in the region. |
|---|---|---|
|   | Connected VPC | You must configure this parameter if you set the Connect over Express Connect Circuit parameter to Access over Express Connect Circuit. |
|   | Shard Account and Password for Primary and Secondary Instances | You can select Automatic Application and Manual Entry. Automatic Application: ASR for Geo- disaster Recovery automatically creates accounts if no accounts are created for the instance shards. Manual Entry: You can specify the accounts and passwords if accounts are created for the instance shards. Note The accounts are used by synchronization components to obtain oplogs on the shards. |
|   | Record Name | The name for the value of the record. You can specify a custom name. |

| Global Domain Name Settings |   |   |
|---|---|---|
|   | Domain Name | A default global domain name is automatically generated, which can be used directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, you can use the name directly. If the global domain name is a custom domain name and no corresponding domain name exists in the DNS, the record value of the global domain name must be consistent between the primary and secondary instances. |
| Note You must configure this parameter only if the mode of the protection group is active-active. |   |   |
|   | TTL | The period of time that a DNS record can be cached on a DNS server. A default time to live (TTL) is generated automatically, which can be modified by users. |
|   | Bind Public Endpoint | If you select this option, the public endpoints of the primary and secondary instances of the synchronization entity are used as the record values in the global domain name. If you do not select this option, the VPC endpoints or internal endpoints of the primary and secondary instances of the synchronization entity are used as the record values. |

After you specify the global domain name, click **Precheck**. If no problem is detected, click
**Next**.
6. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the protection group status. If the protection group is in the Protection Failed state, click **Reprotect** in the Actions column of the protection group.

###### 1.5.1.1.4.13 ECS

This topic describes how to configure disaster recovery for Elastic Compute Service (ECS) instances.

**Prerequisites**

| Prerequisites | Description |
|---|---|

| An ECS instance is created in the primary cloud by using the Apsara Uni-manager Management Console. A VPC instance is created in the primary cloud and the secondary cloud by using the Apsara Uni- manager Management Console. | Only premium performance disks (IO15) are supported by the ECS instance. The CIDR blocks of the primary and secondary VPC instances are the same, or can be matched by mapping. |
|---|---|

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step on the **Add synchronization entity** page, click the **Elastic**
**Compute Service** tab in the **Instance Type** section. In the left-side entity list, select the
instance ID. Click the icon to add the instance to the right-side entity list. Click **Next** to go to the **Configure Priority and Resource Mapping** step.
5. In the **Configure Priority and Resource Mapping** step, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. In the Synchronize Configuration dialog box, configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Configurati on step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. You can select only 3, 4, or 5. |

| Note When you click Next after the basic settings are configur ed, ASR- DR checks |   |   |
|---|---|---|
|   | Synchronization Policy | Only Full + Incremental is supported. |
| the HDR authoriz ation status of the primary and seconda ry sites. If the HDR authoriz ation is successf ul, ASR- DR creates an organiza tion mapping . |   |   |
| Select a cloud site pair | Whether to Reuse Site Pairs | If you do not want to reuse site pairs, click Next. If you want to reuse site pairs, select the corresponding cloud site pair and click Next. |

| Select a zone | Select a zone in the production cloud | Select a zone in the primary cloud. |
|---|---|---|
|   | Select a zone in the disaster recovery cloud | Select a zone in the secondary cloud. |
| Network Configurati on | VPC in Production Cloud | Select a VPC created in the primary cloud from the drop- down list. |
|   | vSwitch in Production Cloud | Select a vSwitch created in the primary cloud from the drop-down list. |
|   | Security Group in Production Cloud | Select a protection group created in the primary cloud from the drop-down list. |
|   | VPC in Disaster Recovery Cloud | Select a VPC created in the secondary cloud from the drop-down list. |
|   | vSwitch in Disaster Recovery Cloud | Select a vSwitch created in the secondary cloud from the drop-down list. |
|   | Security Group in Disaster Recovery Cloud | Select a protection group created in the secondary cloud from the drop-down list. |
| Select an HDR protection group | Select an existing HDR protection group | Select a protection group and click Next. |
|   | Create HDR Protection Group | Enter a protection group name, an expected synchronization delay value, and a protection group bandwidth value, and click Next. Note The protection group bandwidth value you entered must be a multiple of 8. |

6. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.14 DataHub

This topic describes how to configure disaster recovery for DataHub, including the prerequisites and procedure.

**Prerequisites**

You have created a DataHub instance and a topic each in the primary and secondary cloud instances in the Apsara Uni-manager Management Console. The DataHub instances in the primary and secondary cloud instances must have the same topic and field.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. On the Protection Groups page, find the protection group that you want to manage, click
**Create Entity** in the **Actions** column.
4. In the Select Instances step of the **Add synchronization entity** wizard, set **Instance**
**Type** to **DataHub**.
5. In the entity list on the left, select the desired instance ID and click the
icon to add the instance to the entity list on the right. Then, click **Next**.
6. On the **Configure Priority and Resource Mapping** page, find the desired instance, click
the icon in the **Actions** column, and then click **Configure**. Configure the parameters based on your business requirements and click **Next**. The following table describes the parameters.

| Configurati on step | Parameter | Description |
|---|---|---|
| Basic Settings | Priority | The priority based on which ASR for Geo-disaster Recovery performs drills or recoveries on resources. A smaller value indicates a higher priority. Important Prioritize cloud services based on the number of dependencies. A service that has more dependents has a higher priority. You can select only 3, 4, or 5. |

|   | Synchronization Policy | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|---|---|---|
| Select Topic | Select Synchronization Mode | The mode to synchronize entities. Example: Fixed. Valid values: Fixed: Make sure that the shards at both sides are consistent. Shards are synchronized in one-to-one mode. When the primary instance is scaled up, you must stop the synchronization task and create an incremental synchronization task again. Round robin: Different numbers of shards can be _ deployed at both sides. Shard scaling does not affect synchronization tasks. Data is synchronized to all shards. |
|   | Select Topic | Select the topics and fields that you want to synchronize. You can select multiple topics and fields and they must have been created on the destination. |

7. After the configuration is complete, preview the configuration and click **OK**. On the
Protection Groups page, click the icon to view the status of the protection group.

> **Note:** After the protection group is created, the system initializes the protection group. After the protection group is initialized, check the status of the protection group. If the protection group is in the Protect Failed state, click **Reprotection**.

###### 1.5.1.1.4.15 Ingress gateway AsrIngressGW

This topic describes the prerequisites and procedure for adding a synchronization entity for an Ingress Gateway.

**Prerequisites**

You have created ingress gateway instances on both the primary and standby cloud instances on the Apsara Uni-manager Management Console. You have attached Elastic Compute Service (ECS) and Server Load Balancer (SLB) resources to the ingress gateway instance and configured the SLB port.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Business Disaster Recovery** > **Protection**
**Group**.
3. In the **Actions** column of the target protection group, click **Create Entity**.
4. On the **Add synchronization entity** page, set **Instance Type** to **Ingress Gateway**
**AsrIngressGW**.
5. In the entity list on the left, select the instance ID for the production site, click the
icon to move the instance to the entity list on the right, and click **Next**.
6. On the **Configure Priority and Resource Mapping** page, in the **Actions** column of the
target instance, click , and then select **Configure**. Configure the parameters and click
**Next**. The following table describes the parameters.

| Item | Parameter |   | Description |
|---|---|---|---|
| Basic Settings | Priority |   | ASR-DR performs drills or recoveries on resources based on this priority. A smaller value indicates a higher priority. Important Sort priorities based on data dependencies. The cloud product that is depended on has a higher priority and can only be assigned 1. |
|   | Synchronization Policy |   | Full + Incremental: Synchronizes historical data before the synchronization task is created and incremental data after the synchronization task is created or from a specified offset. |
|   | Resource Mapping |   | The target instance at the disaster recovery site. This instance serves as the hot standby resource for the production site instance. |
| Applicatio n Settings | Application Name |   | Customize the application name. The name must be 4 to 20 characters in length. |
|   | Ingress Gateway Listener Port |   | Select the same port as the backend port of the SLB instance that is associated with the primary and standby gateway instances. |
|   | Product ion Applica tion Endpoi nt | Addr ess | Enter the IP address or domain name of the production application. |
|   |   | Port | Enter the port number of the production application. |

|   | Disaste r Recover y Applica tion Endpoi nt | Addr ess | Enter the IP address or domain name of the disaster recovery application. |
|---|---|---|---|
|   |   | Port | Enter the port number of the disaster recovery application. |
|   | Enable Health Check |   | Select whether to enable health checks. |
| Health Check Settings |   |   |   |
|   | Check Protocol |   | HTTP and TCP protocols are supported. |
|   | Check Method |   | Select the health check method. This parameter is required only when you select HTTP for Check Protocol. |
|   | Check Path |   | Enter the path for health checks. This parameter is required only when you select HTTP for Check Protocol. |
|   | Check Interval |   | Enter the interval for health checks. |
|   | Check Timeout Period |   | Enter the timeout period for health checks. |

7. Click **Add**, configure routing rules by referring to the following table, and click **Next**.
The system preconfigures a default route. If traffic does not match any custom route, the system uses the default routing rule. If you add the same gateway instance to different synchronization entities that use the same listener port, their default routes must not conflict. If conflicts occur, you must manually modify the default routing rules to differentiate between applications.

| Section | Parameter | Description |
|---|---|---|
|   | Rule Name | Customize the rule name. The name must be 4 to 20 characters in length. |

| R for Geo-disaster tions in the Apsara Management Conso |   |   |
|---|---|---|
| Basic Information |   |   |
|   | Priority | Enter an integer from 1 to 99. A smaller value indicates a higher priority. When multiple routing rules exist, the system processes them based on their priority, from highest to lowest. |
| Condition | Type | Path: routes requests based on the request path. SourceIP: routes requests based on the CIDR block of the request source. Header: routes requests based on the request header. Method: routes requests based on the HTTP request method. |
|   | Matching Rule | Configure the matching rule based on the selected type and the format example on the UI. |
| Route Note The sum of the weights for the production application endpoint and the disaster recovery application endpoint must be 100. | Production Application Endpoint Weight | The weight of traffic for the production application. Enter an integer from 0 to 100. |
|   | Disaster Recovery Application Endpoint Weight | This weight of traffic for the disaster recovery application. Enter an integer from 0 to 100. |

8. After you complete the configuration, preview it. If the configuration is correct, click
**Confirm**. On the protection group list page, click the
icon to view the protection group status.

> **Note:** After the protection group is created, the system starts to initialize it. After the initialization is completed, check the protection group status. If the status is Protection Failed, click **Reprotection**.

###### 1.5.1.1.4.16 API Gateway

This topic describes how to add an API Gateway 2.0 sync entity to a protection group.
1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Groups**.
3. In the **Actions** column of the target protection group, click **Add Entity**.
4. On the **Add Sync Entity** page, set **Instance Type** to **API Gateway**.
5. In the entity list on the left, select the instance ID of the production site. Click the
icon to move the instance to the entity list on the right. Click **Next**.
6. On the **Select Instance Priority and Resource Mapping** page, click
in the **Actions** column of the target instance and select **Configure**. Configure the settings as needed, and then click **Next**. The following table describes the configurations.

| Config | Configuration | Description |
|---|---|---|
| Basic Configura tion | Priority | ASR-DR performs drills or recovery based on this priority. A smaller number indicates a higher priority. Important Sort the priorities based on data dependencies. The cloud product that is depended on has a higher priority and must be set to 1. |
|   | Sync Policy | Incremental: Synchronizes only incremental data that is generated after the synchronization task is created or from a specified offset. |
|   | Resource Mapping | The target instance at the disaster recovery site. This instance serves as a hot standby resource for the production site instance. |

| Global Domain Name Configura tion | Record Name | Enter a custom name for this record value. |
|---|---|---|
|   | Domain Name | The system generates a default global domain name that you can use directly. If the global domain name is a custom domain name and no corresponding domain name exists in DNS, you can use it directly. If the global domain name is a custom domain name that is not in DNS, its record value must match the address of the primary and secondary instances. |
|   | TTL | The time that the global domain name's DNS record is cached on a DNS server. The system generates a default TTL, which you can modify. |
|   | Record Value Collection | If the protection group is in active-passive mode, the value must be 100:0 or 0:100. If the protection group is in active-active mode, you can configure this as needed. |

7. Review the configuration. If it is correct, click **Confirm**. On the protection group list page,
click the icon to view the protection group status.

> **Note:** The system initializes the protection group after it is created. When initialization is complete, check the protection group status. If the status is Protection Failed, perform a **Reprotect** operation.

###### 1.5.1.1.5 Start a protection group

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

##### 1.5.1.2 Fail over a protection group

You can fail over a protection group that you created.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the navigation pane on the left, choose **DR for Business** > **Protection Groups**.
3. In the protection group list, find the protection group that you want to manage, click the
icon in the Actions column, and then click **Switch**.
4. In the dialog box that appears, select an action:
Fail over the protection group: a. Select the **Protection Group Switch** tab. b. Select a switchover type: Drill Switchover Failover c. Click **Precheck**. A precheck verifies the plan without executing it. This increases the success rate of disaster recovery drills. d. Click **Start Switchover**. Switch ingress traffic: a. Select the **Ingress Traffic Switch** tab. b. Select a switchover action.
**Switch Traffic to Primary**: Switches all traffic-class sync entities in the protection
group. All traffic is directed to the production site, and the disaster recovery site stops providing services.
**Switch Traffic to Secondary**: Switches all traffic-class sync entities in the
protection group. All traffic is directed to the disaster recovery site, and the production site stops providing services.
**Recover Traffic**: Fails back all traffic-class sync entities in the protection group. This
restores service so that both the production and disaster recovery sites provide services simultaneously. c. Select whether to perform a forced switchover. When a data center fails, traffic is forcibly switched to an active data center. If the primary data center fails, traffic is switched to the secondary site. If the secondary data center fails, traffic is switched to the primary site. d. Click **Precheck**. A precheck verifies the plan without executing it. This increases the success rate of disaster recovery drills. e. Click **Start Switchover**.

##### 1.5.1.3 Fail back a protection group

You can fail back a protection group that has been failed over.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. In the protection group list, find the desired protection group, click the
icon in the Actions column, and then select **Start Switchback**.
4. In the dialog box that appears, select one of the following options based on your business
requirements:
**Precheck**: A pre-check is performed on the plan without the need to start the plan. This
improves the success rate of disaster recovery drills.
**End-to-End**: The system directly switches back the protection group.
5. Click **OK**.

##### 1.5.1.4 Stop a protection group

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

##### 1.5.1.5 Export protection groups

This topic describes how to export protection group information to your local computer.
1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **Business Disaster Recovery** > **Protection**
**Group**.
3. On the Protection Group page, click **Export** in the upper-left corner.
4. In the dialog box, select a cloud product from the drop-down list.
5. Click **Export**.
6. Select a local path for the download.
7. Click **Download**.

##### 1.5.1.6 Manage protection group topologies

###### 1.5.1.6.1 Manage topology applications

Manage associated topology applications on the protection group topology page.
1. Log in to ASR-DR: Geo-Disaster Recovery Platform. For details, see Log on to the ASR-DR
console.
2. In the left-side navigation pane, choose **Business Disaster Recovery** > **Protection**
**Group**.
3. Click **Topology** in the **Actions** column of the protection group.
4. On the **Topology Application Association** tab of the **Protection Group Details** page,
click **Associated Applications**. You can associate applications under both Primary Application and Secondary Application.
5. In the **Primary Application** or **Secondary Application** dialog box, configure the
application association.

**Other Applications**

| Parameter | Description |
|---|---|
| Application Type | Select Other Applications for Application Type. |
| Application Name | Enter the name of the application. |
| Deploymen t Type | Select a deployment type. Options include ECS, ACK, and Others. |
| ECS Instance | This option is available only when you select ECS for Deployment Type. Select an ECS instance. |

**EDAS Application**

| Parameter | Description |
|---|---|
| Application Type | Select EDAS Application. |
| EDAS Application | Select an EDAS application. |
| Deploymen t Type | The deployment type is determined by the selected application and cannot be modified. |

6. Click **OK**.
7. Perform other operations related to topology application association.

| Operation | Description |
|---|---|
| View an application | On the Topology Application Association tab, view information about associated applications, including manually associated and automatically parsed topology applications. Note The system automatically parses topology applications for microservice- type synchronization entities under the current protection group. |
| Edit an application | i. On the Topology Application Association tab, click Edit in the Actions column of the application. Note You cannot edit automatically parsed topology applications. ii. In the Edit Application dialog box, modify the associated application information. iii. Click OK. |

| Delete an application | i. On the Topology Application Association tab, click Delete in the Actions column of the application. Note You cannot delete automatically parsed topology applications. ii. Click OK. |
|---|---|

###### 1.5.1.6.2 View an application topology

View the application-level disaster recovery topology of a protection group. The topology shows the disaster recovery pairs, data replication direction, data synchronization latency, and application traffic flow.
1. Log in to ASR-DR: Geo-Disaster Recovery Platform. For more information, see Log on to the
ASR-DR console.
2. In the left-side navigation pane, choose **Business Disaster Recovery** > **Protection**
**Group**.
3. Click **Topology** in the **Actions** column of the protection group.
4. On the **Application Topology** tab of the **Protection Group Topology** page, view the
application-level disaster recovery topology. Scroll the mouse wheel to zoom in or out on the topology. The number displayed on a data center in the topology indicates the number of topology applications associated with the current protection group. Click on the data center to open the Edit Application dialog box and go to the application list to associate applications. Click **In Carousel** in the lower-left corner of the topology to pause carousel playback. When paused, click **Suspend Carousel** to resume playback. Click in the upper-right corner of the topology to enter or exit full-screen mode. Click in the upper-right corner of the topology to expand the **Synchronization**
**Latency** panel and view the latency of each synchronization entity.

#### 1.5.2 Manage a plan

You can use a plan to execute a series of jobs in a protection group in sequence. The jobs can be resource switchovers and checks. You can create independent protection group switchover, switchback, failover, and failback plans. You can also create process-based drill plans and download drill reports after the drills are complete.

##### 1.5.2.1 Overview

Plans are categorized into drill plans and recovery plans based on whether the primary cloud fails.

**Context**

Drill plans are run when the primary and secondary clouds work as expected. Recovery plans are run when the primary or secondary cloud fails. Two failover modes are provided based on the fault level: **Minimum RTO** and **Try Minimum RPO**
**(Recommended)**. You can select a failover mode based on your business requirements.
You can also modify the failover plan to change the failover mode. Try Minimum RPO (Recommended): In this mode, a failover is performed at the primary site regardless of whether a global site fault or an application fault occurs. This helps ensure that all data at the primary site is synchronized to the secondary site. If the primary site becomes completely unavailable due to a global site fault, the primary site management interface fails to be called. In this case, this mode is ignored and the failover at the primary site is skipped. Minimum RTO: In this mode, no failover is performed at the primary site regardless of whether a global site fault or an application fault occurs. This helps ensure that services at the secondary site can be quickly restored. The system triggers a failover without waiting for the completion of data synchronization from the primary site to the secondary site. This may cause data inconsistency between primary and secondary sites. Plans can be categorized into failover or switchover plans and failback or switchback plans based on synchronization directions.

**Context**

In the failover or switchover process, resources in a protection group in the primary cloud are unavailable, and workloads are switched over to the secondary cloud. Failbacks or switchbacks are a reverse process of failovers or switchovers. In the failback or switchback process, resources in the protection group in the secondary cloud are unavailable, and workloads are switched over to the primary cloud. Failovers and switchovers are available only for a protection group whose synchronization direction is set to Forward. After a failover or switchover is performed, the synchronization direction of the protection group becomes backward. Failbacks and switchbacks are available only for a protection group whose synchronization direction is set to Backward. After a failback or switchback is performed, the synchronization direction of the protection group becomes forward.

##### 1.5.2.2 Manage business disaster recovery plans

This topic describes how to create business disaster recovery plans (including drill plans and recovery plans), how to query business disaster recovery plans, and how to view the execution histories of disaster recovery plans.

###### 1.5.2.2.1 Create a business disaster recovery plan

This topic describes how to create a business disaster recovery plan, including a drill plan and a recovery plan. This topic also describes how to configure execution steps and policies for drills or failovers and failbacks.

**Prerequisites**

You have created a protection group. For more information, see Create a protection group.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **Business Disaster Recovery > Business**
**Disaster Recovery Plan**.
3. Click **Create Disaster Recovery Plan**.
4. In the **Basic Information** step, specify parameters by referring to the following table, and
click **Next**.

| Section | Parameter | Description |
|---|---|---|

| DR Region Informatio n | Organization | Select from the drop-down list the organization to which this plan belongs. It must match the organization displayed at the top of the environment. If you have already selected a specific organization for the environment and that organization has no subordinate organizations, the organization is automatically specified in the drop-down list. If you selected the root organization or another organization that has subordinate organizations for the environment, you must select a specific organization from the Organizations drop-down list. |
|---|---|---|
|   | Resource Set | Select from the drop-down list the resource set to which the instance belongs. It must match the resource set displayed at the top of the environment. If you have already selected a specific resource set for the environment, the resource set is automatically specified in the drop-down list. If you selected all resources of the current organization for the environment, you must select a specific resource set from the Resource Set drop- down list. |
|   | DR Relationship | Select the disaster recovery relationship to which the disaster recovery plan belongs. |
| DR Plan Informatio n | Plan Name | Specify a plan name. It must be 2 to 20 characters in length and can contain letters, digits, underscores ( ), _ hyphens (-), and periods (.). It must start with a letter or digit. |
|   | Plan Type | Specify the purpose of the plan. Valid values: Drill Plan: You can use this plan only for drills. You cannot use it for disaster recovery in the production region. Recovery Plan: You can use this plan for both drills and disaster recovery in the production region. |
|   | Plan Description | Describe the plan in detail. |

5. In the **Select Protection Group** phase, perform the following operations:
i. In the Available Protection Groups section, select the protection groups that require disaster recovery. ii. Click to move the selected protection groups to the Selected Protection Groups section. iii. After confirming that you have added all desired protection groups, select either of the following options for **Quick Sorting Mode**:
**Sequential Execution**: During disaster recovery, the system switches protection
groups one after another in sequence.
**Concurrent Execution**: During disaster recovery, the system switches all protection
groups simultaneously. iv. Click **Next**.
6. In the **Create Plan** phase, you must create a plan respectively for the failover and failback
phases. The system presets a plan based on the protection groups you selected in the previous step. You can confirm or modify the preset plan based on your business requirements. Click **Next**. The following table describes the operations that you can perform on the failover and failback plans.

| Operation | Description |
|---|---|
| Modify failover/ failback steps | a. Click to check whether the settings of After Failover Succeeded and After Failover Failed meet your requirements. If yes, click Confirm. If no, proceed to the next step. b. Set After Failover Succeeded and After Failover Failed as needed. Valid values: Immediately: The next operation is performed immediately after the failover succeeds. Waiting for Fixed Duration: The next operation is performed or the plan is terminated after the specified period of time elapses. Wait for Manual Operation: The subsequent operations must be manually performed after the failover succeeds or fails. c. Click Confirm. |
| Delete the failover/failback step | a. Click . b. In the dialog box that appears, click OK. |
| Add manual checkpoints | a. In the Select Point section on the left side of the page, clickM anual Checkpoint. b. Click + Add step at the bottom of the page. c. Enter check items and select an operation from the After Start drop- down list. d. Click Confirm. |

7. In the **Confirm Information** step, check whether all settings are correct.
If not, click **Previous** to modify the settings. If yes, click **Submit**.

###### 1.5.2.2.2 Configure drill metrics

You can specify a variety of metrics to be collected as drill results. ASR for Geo-disaster Recovery then provides optimization suggestions for unsatisfactory results. This helps you evaluate the performance of your enterprise disaster recovery architecture and quickly discover and solve problems.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the **Business Disaster Recovery Plan** page, enter a plan name and click
.
4. After the protection group that meets the conditions is displayed, click the
icon in the
**Actions** column and select **Configure Drill Metrics**.
5. In the **Modify Expected Values of Drill Metrics** dialog box, click **Add Entry**, modify the
values of the parameters, and click **OK**.

> **Note:** You can click **Add Entry** repeatedly to add multiple cloud services, which must be unique.

###### 1.5.2.2.3 Query a business disaster recovery plan

You can query a disaster recovery plan by production region, plan type, plan name, or plan ID.
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

###### 1.5.2.2.4 Perform a business disaster recovery

After a business recovery plan is created, you can execute a disaster recovery plan. This topic describes how to execute a disaster recovery plan and the usage notes.

> **Important:** In a hybrid disaster recovery scenario, if you cannot log in to Apsara Stack Resilience (ASR) for Geo-disaster Recovery due to a disaster, perform a switchover on the geo- disaster recovery platform of the public cloud. After the disaster is recovered, perform a switchback in the ASR for Geo-disaster Recovery console. To synchronize incremental data from the public cloud to Apsara Stack, click Reset Synchronization Offset in the switchback step to configure the start offset for incremental synchronization. The system automatically initiates the reprotection process for the synchronization entity and creates an incremental synchronization task. After the protection group enters the Protected state, click Next to switch back your business to Apsara Stack.

**Prerequisites**

A recovery plan is created. For more information, see Create a business disaster recovery plan.
1. Log in to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business** > **Disaster Recovery Plan**.
3. In the list of business disaster recovery plans, find the plan that you want to manage, click
the icon in the **Actions** column, and click **Start Failover**.

> **Note:** Before you start a failover, we recommend that you perform a drill to ensure that the plan orchestration and protection group configurations are correct.

4. In the dialog box that is displayed, click **OK**.
5. Go to the disaster recovery plan details page and execute the created plan steps one by
one.

> **Note:** During the failover, you can click **Terminate** on the **Progress** tab to terminate the failover task. Terminated failover tasks cannot be restored. If you want to perform the failover tasks, you must create new failover tasks.
> During the failover, you can click **Force Pass** on the **Progress** tab to skip the current step.
> During the failover, if a step fails, click **Retry** to re-execute the step.
> In hybrid disaster recovery scenarios, when you perform a switchback in the ASR for Geo-disaster Recovery console, click **Reset Synchronization Offset** to configure the start offset for incremental synchronization. This way, the system automatically initiates the reprotection process for the synchronization entity and creates an incremental synchronization task. After the protection group enters the Protected state, click Next to switch back your business to Apsara Stack.

6. After the failover is complete, view the failover result on the **Historical Records** tab.

###### 1.5.2.2.5 Execute a business disaster recovery drill plan

**drill plan**

The Apsara Stack Resilience (ASR) for Geo-disaster Recovery console allows you to execute a drill plan and view the drill process on the plan details page. In addition, you can generate and download the drill report.

**Prerequisites**

You have created a business disaster recovery drill plan. For more information, see Create a business disaster recovery plan.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **Business Disaster Recovery** > **Business**
**Disaster Recovery Plan**.
3. In the drill plan list, click **Start Drill** in the **Actions** column of the target plan.
4. In the dialog box that appears, click **OK**.
5. Go to the drill plan details page and perform drill tasks one by one based on the created
drill plan.

> **Note:** During a drill, you can click **Terminate** and enter a reason to stop the entire drill task. You cannot resume a terminated task. To perform the current drill again, you must create a new drill task.
> During a drill, you can click **Force Pass** to skip the current step.
> During a drill, if a step fails, you can click **Retry** to re-execute the step.

6. After the drill is completed, go to the **Historical Records** tab to view the drill results.
The Drill Overview section displays the following information: Drill Success Rate: includes **Successful Drills**, the **Total Drills**, and the success rate. Protection Group Failover Success Rate: includes **Successful Protection Group**
**Failovers**, **Total Protection Groups**, and the success rate.
Protection Group Failback Success Rate: includes **Successful Protection Group**
**Failbacks**, **Total Protection Groups**, and the success rate.
RPO-compliance Rate: includes **Compliant Instances**, **Total Instances**, and the compliance rate. Failover Duration Compliance Rate: includes **Compliant Instances**, **Total Instances**, and the compliance rate. Failback Duration Compliance Rate: includes **Compliant Instances**, **Total Instances**, and the compliance rate.
7. In the drill list in the lower part of the page, find the drill that you want to view the
summary and click **View Drill Summary** in the **Actions** column.

> **Note:** If a report has been generated for the drill, the **Actions** column displays the **Download** **Report** option.

8. In the **Drill Conclusion** section of the **Summary** page, click **Edit** and enter a conclusion
for the drill. You can click **View Details** in the upper part of the page to view the detected anomalies.
9. In the upper-right corner of the page, click **Generate Report**. The system automatically
generates a drill report. Click **Download Report** to export the report in Microsoft Word format.

###### 1.5.2.2.6 View the execution history of a plan

This topic describes how to view drill records and disaster recovery records on the Plan Execution History page.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Plan**.
3. On the Business Disaster Recovery Plan page, click **Plan Execution History**. Drill records
are displayed in reverse order by drill completion time on the Plan Execution History page.
4. View the disaster recovery drill records.
i. On the **Drill Records** tab, click Advanced Filter. You can view drill records by **Plan**
**Status**, **Drill Conclusion**, or **Disaster Recovery Plan****Name**.
ii. Select a plan state or drill conclusion, or enter a keyword of disaster recovery plan names, and then click the icon. iii. After drill records that meet the specified condition are filtered, view drill summaries or download reports. View details: Click **Details** in the **Actions** column to open the **Progress** page. View a drill summary: Click **View Drill Summary** in the **Actions** column of a drill record to go to the Summary page.
5. View disaster recovery records.
i. Click the **Disaster Recovery Records** tab and click Advanced Filter. You can view disaster recovery records by **Plan Status** or **Disaster Recovery Plan Name**. ii. Select a plan state or enter a keyword of disaster recovery plan names, and then click the icon. iii. Disaster recovery records that meet the specified condition are filtered.

##### 1.5.2.3 Manage a disaster recovery unit namespace

**namespace**

ASR-DR supports two active-active modes: active-active services with active-standby cloud products and active-active services with separated cloud products for read and write operations. Only ApsaraDB RDS and OSS support the active-active services with separated cloud products for read and write operations.

**Mode introduction**

Active-active services with active-standby cloud products: In normal cases, the read and write operations of services at both the primary site and the secondary site are processed by the production instances of synchronization entities. Active-active services with separated cloud products for read and write operations: In normal cases, the write operations of services at both the primary site and the secondary site are processed by the production instances of synchronization entities. Read operations are processed by the cloud products in the nearest data center.

###### 1.5.2.3.1 Create a disaster recovery unit namespace

**namespace**

ASR for Geo-disaster Recovery allows you to bind a disaster recovery unit namespace to a protection group. This ensures that only the synchronization entities in the bound unit namespace are failed over to the secondary site when the primary site fails. A disaster recovery unit namespace can be bound to only one protection group. A synchronization entity can be used by only one disaster recovery unit namespace.

**Prerequisites**

The data-plane SDK is customized. For more information, see Customize the data-plane SDK to implement access from multiple endpoints.

**Scenarios**

**Active-active services and active-standby cloud products**

Services are provided in active-active mode and cloud products work in active-standby mode. The same business system is deployed in two clouds. Under normal circumstances, the read and write operations of the business systems in the two clouds are processed by the cloud products at the primary site. When the primary site fails, the cloud products at the secondary site take over services. All read and write operations of the business systems in the two clouds are failed over to the secondary site.

**Active-active services and separated cloud products for read**

**and write operations**

Services are provided in active-active mode and cloud products work in active-standby mode. Cloud products at the secondary site process read operations only. The same business system is deployed in two clouds. Under normal circumstances, the write operations of the business systems in the two clouds are processed by the cloud products at the primary site. The read operations of the business systems in the two clouds are processed by the cloud products in the nearest data center. When the primary site fails, the cloud products at the secondary site take over services. All read and write operations of the business systems in the two clouds are failed over to the secondary site.
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
|---|---|
| Refresh the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page. |
| Adjust the style for displaying the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page and select Default or Compact to switch the style for displaying the list of disaster recovery unit namespaces. |
| Customize column fields for the list of disaster recovery unit namespaces | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page and select the column fields that you want to display in the list. |
| Display the list of disaster recovery unit namespaces in full screen | Click the icon in the upper-right corner of the Disaster Recovery Unit Namespace page. The list of disaster recovery unit namespaces is displayed in full screen. |

###### 1.5.2.3.2 Fail over a disaster recovery unit namespace

**namespace**

This topic describes how to fail over the protection entities in a protection group by failing over the disaster recovery unit namespace to which the protection group is bound.

**Prerequisites**

The disaster recovery unit namespace is bound to a protection group. For more information, see Create a disaster recovery unit namespace.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Unit**
**Space**.
3. On the **Disaster Recovery Unit Namespace** page, find the desired disaster recovery unit
namespace and click **Failover** in the **Actions** column.
4. In the message that appears, click **OK**.

###### 1.5.2.3.3 Fail back a disaster recovery unit namespace

**namespace**

After the primary data center is recovered, you need to fail the protection entities in the disaster recovery unit namespace that have been failed over to the secondary data center back to the primary data center.

**Prerequisites**

The disaster recovery unit namespace in the primary data center is failed over to the secondary data center. For more information, see Fail over a disaster recovery unit namespace.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **DR for Business > Disaster Recovery Unit**
**Space**.
3. On the **Disaster Recovery Unit Namespace** page, find the desired disaster recovery unit
namespace and click **Failback** in the **Actions** column.
4. In the message that appears, click **OK**.

### 1.6 Alert management

#### 1.6.1 Configure alert rules

The ASR for Geo-disaster Recovery console follows specific rules to send alerts. You can create one or more alert rules.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **Alerts** > **Alert Rules**.
3. Click **Create**.
4. In the **Create Alert Rule** dialog box, configure the parameters. Then, click **OK**.

| Parameter | Description |
|---|---|

| Rule Name | The name of the alert rule. You can customize the name. The name must be 4 to 20 characters in length. |
|---|---|
| Rule Description | The description of the rule. This parameter is optional. |
| Organization | Select the organization to which the instance belongs. Note If you log on by using the organization administrator role or the organization disaster recovery administrator role, the drop-down list displays the organizations that are managed only by you. |
| Metric | i. Select a metric from the first drop-down list. The following metrics are available: Protection Group Status Plan Status Scheduled RTO Protection group synchronization latency ii. Select a condition to trigger alerts from the second drop-down list. iii. Select or enter a value to trigger alerts from the third drop- down list. |
| Alert Level | You can customize an alert level. The following alert levels are available: Alert, Urgent, Warning, Message, and Error. |
| Alert Contact | Select users who receive alerts from the drop-down list. The drop- down list contains users of the organization in the Apsara Uni- manager Management Console. Note If the drop-down list is empty, create users that belong to the organization in the Apsara Uni-manager Management Console. |
| Notification Methods | ASR for Geo-disaster Recovery supports the following notification methods: Email Address: ASR for Geo-disaster Recovery sends emails to alert contacts when the alert rule conditions are met. DingTalk Token: ASR for Geo-disaster Recovery uses DingTalk to notify alert contacts if the alert rule conditions are met. ASO Dashboard: ASR for Geo-disaster Recovery pushes alerts to Alert Monitoring of the Apsara Uni-manager Operations Console if the alert rule conditions are met. |

**Related operations**

After creating alert rules, you can also perform the operations described in the following table.

| Operation | Procedure |
|---|---|
| Query details of an alert rule | Basic query i. Use the rule name, metric, alert level, or rule state as the query predicate. ii. Click the icon. Advanced filter i. Click Advanced Filter. ii. Enter the rule name, metric, alert level, or rule state. iii. Click Search. Click Reset. ASR for Geo-disaster Recovery clears the filter conditions and refreshes the list of alert rules. |
| View the details of an alert rule | 1. On the Alert Rules page, click the icon in the Actions column corresponding to the desired alert rule. 2. Click Details. |
| Modify an alert rule | 1. On the Alert Rules page, click the icon in the Actions column corresponding to the desired alert rule. 2. Click Modify. 3. Click OK. |
| Disable an alert rule | 1. On the Alert Rules page, click the icon in the Actions column corresponding to the desired alert rule. 2. Click Disable. 3. Click OK in the message that appears. The alert rule takes no effect immediately. |
| Delete an alert rule | 1. On the Alert Rules page, click the icon in the Actions column corresponding to the desired alert rule. 2. Select Delete from the drop-down list. 3. In the message that appears, click OK. |

#### 1.6.2 View and export alert information

You can view alert information to obtain abnormality information.
1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Alerts** > **Alert Records**
3. View alert information or set filter conditions.
In the upper part of the page, you can customize the alert conditions. Click the ID of an alert. You can view details of the alert.

#### 1.6.3 Configure synchronization latency alert thresholds

**thresholds**

You can set the synchronization latency alert thresholds for each service. Apsara Stack Resilience for Disaster Recovery (ASR-DR) calculates the threshold for each service and displays the thresholds on the Disaster Recovery (DR) Dashboard page.
1. Log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) console. For
more information, see Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Alerts** > **Synchronization Latency Alert**
**Thresholds**.
3. Configure the synchronization latency alert threshold of each service in seconds. Click **OK**.

> **Note:** This feature is available only in the cross-cloud DR scenario.

### 1.7 System Management

#### 1.7.1 Cloud instance management

Before you can configure a protection group and a disaster recovery plan, you must create a cloud instance. Cloud instances are managed by level-1 organizations. All authorized users in a level-1 organization and its subordinate organizations can configure cloud instances for their organizations. The configured cloud instances are available only in the organizations to which they belong.

**Usage notes**

If you need to only configure disaster recovery between different regions of the current cloud, you need to only configure a secondary cloud instance. The cloud instances you configure are shared only between the level-1 organization and its subordinate organizations to which the instances belong. Users in different level-1 organizations must configure their own cloud instances.

**Prerequisites**

The AccessKey ID and AccessKey secret of an organization are obtained. For more information, see Obtain an AccessKey pair. The AccessKey ID and AccessKey secret of an Apsara Stack instance are obtained. For more information, see Obtain an AccessKey pair. The AccessKey ID and AccessKey secret of a personal account of public cloud are obtained. For more information, see Obtain the AccessKey Pair. The related cloud products are configured. For more information, see Manage cloud product information.

> **Note:** If a public cloud instance is added, the AccessKey ID and AccessKey secret of the ASCM organization account are not required to be obtained.
> When an Apsara Stack instance or public cloud instance is added, the methods for obtaining personal accounts are different. For information about how to obtain an instance, see the corresponding method.

1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **System Management > Cloud Instances**.
3. On the page that appears, click **Add Instance**, select the cloud instances that you want to
add, and then click **Next**.
4. In the dialog box that appears, select options from the Organizations and Resource Set
drop-down lists, specify Tenant Account AccessKey ID and Tenant Account AccessKey Secret, and then click **Submit**. If you configure a public cloud instance, you do not need to enter the AccessKey ID and AccessKey secret of your Alibaba Cloud account. Enter the AccessKey ID and AccessKey secret of the organization you obtained in the Tenant Account AccessKey ID and Tenant Account AccessKey Secret fields. The Tenant Account AccessKey ID and Tenant Account AccessKey Secret parameters need to be specified only once by the cloud instance creator.
5. In the dialog box that appears, enter the AccessKey ID and AccessKey secret of the
personal account you obtained.

> **Note:** Enter the AccessKey ID and AccessKey secret of the personal account you obtained in the **User ************** and **User ****************** fields.

6. Click **Confirm**. Configured is displayed in the User AccessKey Pair column of the cloud
instance. The **User ************** and **User ****************** parameters must be configured for each user. A user can use the cloud instance only after the parameters are configured.

**Related operations**

The following table describes the operations that you can perform after the cloud instance is added.

| Operation | Procedure |
|---|---|
| Query the cloud instance | 1. Select a cloud instance state from the Status drop-down list. 2. Select the Instance Name or Instance ID drop-down list and enter a cloud instance name or cloud instance ID. 3. Click the icon. |
| Modify the cloud instance | 1. Find the disaster recovery region and click Edit in the Actions column. 2. In the Edit Instance dialog box, modify the AccessKey ID and AccessKey secret and click Submit. |
| Delete the cloud instance | 1. Click Delete in the Actions column. 2. In the message that appears, click Delete. |
| Refresh the cloud instance list | Click the icon in the upper-right corner of the All Instances section. |
| Adjust the display style of the cloud instance list | In the upper-right corner of the All Instances section, click the icon and select Default or Compact to display the cloud instance list in the corresponding style. |

| Customize column fields for the cloud instance list | In the upper-right corner of the All Instances section, click the icon and clear the fields that you do not want to display in the list. |
|---|---|

#### 1.7.2 Manage disaster recovery relationships

To perform disaster recovery (DR), you must first add a DR relationship in the ASR-DR console. You can perform DR operations only between regions that have a DR relationship.

**Background information**

You can perform DR management and switchover operations in the production region. A failover to the secondary region occurs only when the production region fails. Disaster recovery relationships are of two types: A DR relationship consists of one production region and one secondary region. This type does not support multi-region DR. For Apsara Stack-to-Apsara Stack DR, you can perform DR operations only in the secondary region. For Apsara Stack-to-public cloud DR, you can perform DR operations in any region. A DR relationship consists of one production region and multiple secondary regions. This type supports multi-region DR, and you can perform DR operations in any region.
1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **System Management** > **Disaster Recovery**
**Relationship Management**.
3. On the **Disaster Recovery Relationship Management** page, click **Add Disaster**
**Recovery Relationship**.

> **Note:** A disaster recovery relationship can have only one production region.
> All other regions are secondary regions.
> For scenarios other than Hybrid Disaster Recovery, the current region must be a secondary region, not a production region.

| Parameter | Description |
|---|---|

| Disaster Recovery Relationship Name |   | A custom name for the disaster recovery relationship. The name must be 5 to 29 characters in length. |
|---|---|---|
| Description |   | A description of the disaster recovery relationship. |
| Current Region Configurati on | Cloud Instance | The cloud instance where the ASR-DR platform that you are logged on to is located. Keep the default value. |
|   | Region | The region where the ASR-DR platform that you are logged on to is located. Keep the default value. |
|   | Regional Role | Select whether the current region is a production region or a secondary region. Production Region: The region where the primary data center is located in the ASR-DR system. Secondary Region: A backup site or data center that ensures business continuity and data recovery when a disaster or failure occurs in the primary production environment. Note For DR relationships other than Hybrid Disaster Recovery, configure the current region as a secondary region. |
| Disaster Recovery Region Configurati on | Cloud Instance | Select a cloud instance. In a DR relationship, a cloud instance can be added multiple times, but each instance must be in a different region. This enables cross-region DR. |
|   | Region | Select the region to which the cloud instance belongs. |
|   | Regional Role | Select Production Region or Secondary Region. This role must be different from the Regional Role of the Current Region Configuration. |

4. Click **OK**.

**Other operations**

After you create a disaster recovery relationship, you can perform the following operations.

| Task Name | Procedure |
|---|---|
| Query a disaster recovery relationship | Enter a DR relationship name and select a production region and a secondary region to filter for matching DR relationships. |

| Check a disaster recovery relationship | 1. Click a DR relationship ID to go to the details page of the DR relationship. 2. Click Recheck for a check item. 3. Wait for the check result. If an exception occurs, click Solution to resolve the exception. Note The system automatically checks the status of the DR relationship every 5 minutes. You can also click Recheck to immediately trigger a status check. |
|---|---|
| Edit a disaster recovery relationship | 1. In the Actions column, click Edit. 2. Modify the DR relationship name and description. 3. Click OK. |
| Disable or enable a disaster recovery relationship | 1. In the Actions column, click Disable/Enable. 2. In the dialog box that appears, click OK. After a DR relationship is disabled, ongoing DR plans continue to run, but no new tasks can be triggered. |
| Delete a disaster recovery relationship | 1. In the Actions column, click Delete. 2. In the dialog box that appears, click Delete. Important A DR relationship is associated with many DR resource objects. Therefore, disable the DR relationship instead of deleting it. If you must delete a DR relationship, first delete all its associated resource objects, such as protection groups and DR plans. |

#### 1.7.3 Manage logs

Operation logs record information about all operations in the system. These operations include the creation, deletion, and execution of protection groups, plans, and instances.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **System Management** > **Logs**.

| Column | Description |
|---|---|
| Module | The modules of the ASR for Geo-disaster Recovery console, such as Drill Plans, Recovery Plans, Instances, Alerts, Protection Groups, and System Management. |
| Alert Level | The log levels, which include Urgent, Alert, Error, Warning, and Message. |
| Operation | The type of operations recorded in logs. |

3. (Optional)
You can filter specific operations logs by user, module, alert level, operation type, start time, or end time.
4. (Optional)
Click **Retry**. ASR for Geo-disaster Recovery clears search conditions and refreshes information of logs in the list.

#### 1.7.4 Hybrid disaster recovery management

Before you can configure a protection group and a disaster recovery plan, you must create a cloud instance. Hybrid cloud instances are managed by level-1 organizations. All authorized users in a level-1 organization and its subordinate organizations can configure cloud instances for their organizations. The configured cloud instances are available only in the organizations to which they belong.

**Background information**

Hybrid cloud disaster recovery refers to disaster recovery between Apsara Stack and public cloud. In this topic, hybrid cloud for disaster recovery consists of Apsara Stack and Alibaba Cloud public cloud.

**Usage notes**

If you need to only configure disaster recovery between different regions of the current cloud, you need to only configure a secondary cloud instance. The cloud instances you configure are shared only between the level-1 organization and its subordinate organizations to which the instances belong. Users in different level-1 organizations must configure their own cloud instances.

**Prerequisites**

The AccessKey ID and AccessKey secret of a personal account are obtained. For more information, see Obtain the AccessKey pair. You have configured related cloud products by referring to Manage cloud product information.
1. Log on to the ASR for Geo-disaster Recovery console.
2. In the left-side navigation pane, choose **System Management > Hybrid Disaster**
**Recovery**.
3. On the page that appears, click **Add Instance**, select the cloud instances that you want to
add, and then click **Next**.
4. Select an organization and a resource set from the drop-down lists and click **Submit**.
5. In the dialog box that appears, enter the AccessKey ID and AccessKey secret of the
personal account you obtained.

> **Note:** Enter the AccessKey ID and AccessKey secret of the personal account you obtained in the **User ************** and **User ****************** fields.

6. Click **Confirm**. Configured is displayed in the User AccessKey Pair column of the cloud
instance. The **User ************** and **User ****************** parameters must be configured for each user. A user can use the cloud instance only after the parameters are configured.

**Related operations**

The following table describes the operations that you can perform after the hybrid cloud instance is added.

| Operation | Description |
|---|---|
| Query the cloud instance | 1. Select a cloud instance state from the Status drop-down list. 2. Select the Instance Name or Instance ID drop-down list and enter a cloud instance name or cloud instance ID. 3. Click the icon. |
| Delete the cloud instance | 1. Find the disaster recovery region and click Delete in the Actions column. 2. In the message that appears, click Delete. |

| Refresh the cloud instance list | Click the icon in the upper-right corner of the All Instances section. |
|---|---|
| Adjust the display style of the cloud instance list | In the upper-right corner of the All Instances section, click the icon and select Default or Compact to display the cloud instance list in the corresponding style. |
| Customize column fields for the cloud instance list | In the upper-right corner of the All Instances section, click the icon and clear the fields that you do not want to display in the list. |

### 1.8 FAQ

#### 1.8.1 What do I do if entities fail to be protected?

**protected?**

Entities in a protection group may fail to be protected when the number of primary and secondary ApsaraDB RDS databases or Tablestore tables increases or decreases. To resolve this issue, you must manually recover the entities.

| Scenario | Problem description | Solution |
|---|---|---|
| Databases added to a primary ApsaraDB RDS instance | After 15 minutes, the entity exception is detected, and the entity fails to be protected. | Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. Databases are added to the secondary instance. Databases are also added for the link. |
| Databases removed from a primary ApsaraDB RDS instance |   | Remove the corresponding databases from the secondary instance. Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. Databases are removed for the link. |
| Databases added to a secondary ApsaraDB RDS instance |   | Manually remove the added databases. Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. The link remains the same. |
| Databases removed from a secondary ApsaraDB RDS instance |   | Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. The link remains the same. |
| Tables added to a primary Tablestore instance |   | Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. Databases are added to the secondary instance. However, after 15 minutes, the status becomes Protect Failed. Click the Recover button again. Tables are added for the link. |

| Tables removed from a primary Tablestore instance |   | Manually remove the tables from the secondary database. Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. Tables are removed for the link. |
|---|---|---|
| Tables added to a secondary Tablestore instance |   | Manually remove the added tables from the secondary instance. Click the Recover button. After 10 minutes, the status of the entity becomes Protecting. The link remains the same. |
| Tables removed from a secondary Tablestore instance |   | Click the Recover button. The removed tables are added to the secondary instance. After 10 minutes, the status of the entity becomes Protecting. However, after 15 minutes, the status of the entity becomes Protect Failed again. Click the Recover button again. The entity enters the Protecting state. The link returns to the previous state. |

#### 1.8.2 Troubleshoot abnormal disaster recovery relationship checks

**recovery relationship checks**

This topic describes the causes of and solutions for abnormal disaster recovery relationships.

**Background information**

Disaster recovery relationship checks include disaster recovery region availability, peer disaster recovery relationship creation, and disaster recovery interconnection configuration. This topic describes the possible causes and solutions for abnormalities in each check.

**Disaster recovery region availability**

**Possible causes**

The AccessKey permissions of the disaster recovery administrator for the cloud instance are incorrect. Dedicated Cloud or Hybrid Cloud Disaster Recovery scenarios: Apsara Stack disaster recovery scenario: Calls to the management API of the peer cloud fail. Hybrid Disaster Recovery scenario: Calls to the management API of the public cloud fail. Public cloud in a Hybrid Disaster Recovery scenario: If the check on the public cloud fails, it is because no heartbeat signal has been received from the Apsara Stack for a long time.

**Solutions**

Incorrect permission configuration. i. Log on to the remote disaster recovery O&M platform. ii. In the navigation pane on the left, choose **Platform Basic O&M > Cloud Information**
**Management**.
iii. Check whether the AccessKey permissions for the related cloud instance are correct. If they are incorrect, change to the correct AccessKey. That is correct. Please investigate other possible causes. Apsara Stack disaster recovery Check whether the two clouds are interconnected as required. Check the availability of the remote disaster recovery platform service. Hybrid Disaster Recovery Check the availability of the remote disaster recovery platform service. If you use a VPC interconnection solution, confirm that the interconnection is completed as required. If you use an Internet-based solution, confirm that the Apsara Stack can access the Internet.

**Peer disaster recovery relationship created**

**Possible causes**

No peer disaster recovery relationship exists on the peer cloud.

**Solution**

1. Log on to the ASR-DR console.
2. In the navigation pane on the left, choose **System Administration** > **Disaster Recovery**
**Relationship Management**.
3. Click the ID of the abnormal disaster recovery relationship to view its details.
4. In the Actions column for the **Peer disaster recovery relationship created** check, click
**One-Click Repair**.
5. After the repair is complete, a recheck is automatically triggered.

**Disaster recovery interconnection configured**

**Possible causes**

The disaster recovery interconnection is not configured, or its status is abnormal.

**Solution**

See Disaster Recovery Interconnection Management to reconfigure the disaster recovery interconnection relationship.

### 1.9 Appendix

#### 1.9.1 Create a RAM role

For the organization corresponding to the instance to be protected, you must create a Resource Access Management (RAM) role for Data Transmission Service (DTS) and ASR-DR in the Apsara Uni-manager Management Console of the primary and secondary sites.
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

#### 1.9.2 Obtain the AccessKey pair of a personal account of public cloud

**personal account of public cloud**

When you add a public cloud instance, you must configure the AccessKey ID and AccessKey secret of the personal account. This topic describes how to obtain the AccessKey ID and AccessKey Secret of the personal account. The AccessKey secret is displayed only when you create an AccessKey pair, and is unavailable for subsequent queries. This topic describes how to create an *************
**pair**. Save the AccessKey ID and AccessKey secret. They can be used when you configure
the instance on the public cloud. AccessKey IDs are used to identify users. An AccessKey secret is the password used to verify that you have the AccessKey ID.

**Prerequisites**

An AccessKey pair for a RAM user is created by using one of the following accounts: Alibaba Cloud account RAM administrator RAM user that has permissions to create and manage AccessKey pairs
1. Log on to the RAM console.
2. In the left-side navigation pane, choose **Identities > Users**.
3. On the Users page, click the username of a specific RAM user.
4. In the User AccessKeys section of the Authentication tab, click **Create AccessKey**.
5. Read the suggestion for each scenario and select a credential solution based on your
business requirements. If you must create an AccessKey pair, select a scenario, select **I**
**confirm that it is necessary to create an AccessKey**, and then click **Continue**. The
created AccessKey pair can be used in all scenarios.
6. In the **Create *********** dialog box, save the AccessKey ID and AccessKey secret, and
click **OK**.

#### 1.9.3 View the synchronization logs of MaxCompute

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

#### 1.9.4 Modify policy configuration

You can modify the policy configuration for MaxCompute synchronization entities added to a protection group. You can add allowlists and blocklists.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Business Disaster Recovery****> Protection**
**Group**.
3. Click **Details** in the **Actions** column of the protection group.
4. On the **Protection Group Details** page, click the
icon next to the synchronization entity and select **Modify Policy Configuration**.
5. In the **Modify Policy Configuration** dialog box, configure the policy.

| Parameter | Description |
|---|---|
| Source MaxCompute Project/Destination MaxCompute Project | The system displays the source and destination MaxCompute projects. You cannot modify this setting. |
| Synchronization Policy Configurations | Enter the synchronization policy for MaxCompute. |
| Cron Expression | Enter the cron expression. |
| Callback Node Type | You can select Manual Business and Manual Business Process. |
| Callback Node ID | Enter the ID of the callback node. |

| Synchronization Policy for DataWorks Project | Enter the synchronization policy information for the DataWorks project. |
|---|---|

6. Click **OK**.

#### 1.9.5 Suspend synchronization entities under a protection group

**a protection group**

Suspend synchronization entities that you added to the protection group.

**Supported products**

MaxCompute and database synchronization entities can be suspended.
1. Log on to the ASR-DR console.
2. In the left-side navigation pane, choose **Business Disaster Recovery > Protection**
**Group**.
3. Click **Details** in the **Actions** column of the protection group.
4. On the **Protection Group Details** page, click the
icon on the right side of the target entity in the synchronization entity list, and select **Suspend**.
5. In the **Suspend Instance in Protection Group** dialog box, set the end time for
synchronization suspension.
6. Click **OK**.

> **Note:** After suspension succeeds, the entity status changes to Suspending. You can click the
> icon on the right side of the synchronization entity and select **Re-protect**.

#### 1.9.6 Obtain an AccessKey pair

To use Apsara Stack Resilience for Disaster Recovery (ASR-DR), the operations administrator or organization administrator must obtain the AccessKey pair of the personal account or the organization account used for the primary center and secondary center, and configure the corresponding AccessKey pair in ASR-DR.

**Prerequisites**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs of an organization.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

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

#### 1.9.7 Manually synchronize data

By default, data of MaxCompute and DataWorks is synchronized from the primary region to the secondary region based on the scheduled time. To immediately perform computing in the secondary region, you can manually synchronize incremental data to the secondary region.
2. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**.
3. In the protection group list, find the desired protection group and then click **Details** in its
**Actions** column.
4. On the **Protection Group Details** page, click the
icon on the right of the instance and click **Synchronize Incremental Data Now**. Then, the system synchronizes the incremental data of MaxCompute and DataWorks.

#### 1.9.8 Obtain the settings of the primary cloud instance

**cloud instance**

This topic describes how to obtain the settings of a primary cloud instance as an administrator. The information includes the endpoint of each cloud service in the primary cloud.
1. Log in to the Apsara Infrastructure Management console for the primary cloud.
In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation** > **Management and control service operation and maintenance** >
**Infrastructure Management**.
2. In the left-side navigation pane of Apsara Infrastructure Management, choose **O&M Tools**
> **Service Registration Variable Dashboard**.

3. Select **Service** from the drop-down list in the upper-left corner. In the search box, enter a
value displayed in the **Service** column of the following table. Find the service that you want to view, click the icon in the **Service Registration** column, and then click the content. In the Registration Variables dialog box, view the value that corresponds to the parameter in the Key column of the following table. The following table describes the services and keys that correspond to each parameter.

| Product | Parameter | Service | Key |
|---|---|---|---|
| Apsara Uni- manager Management Console | ASCM address | oneService | ascm-portal.domain |
| Data Transmission Service (DTS) | DTS address | dts-dts | dts.openapi.endpoint |
| oneConsole | oneConsole address | oneService | console.domain |
| Virtual Private Cloud (VPC) | VPC address | vpc-yaochi | vpc-inner.openapi.endpoint |
| Apsara Infrastructure Management | Apsara Infrastructure Management Endpoint | tianji-endpoint | api server.endpoint _ |
|   | OSS Operations and Maintenance System Address Without Authentication Information |   | inner-api-endpoint |

| Object Storage Service (OSS) |   | oss-chiji |   |
|---|---|---|---|
|   | OSS Operations and Maintenance System Address with Authentication Information Included |   | inner-secure-api-endpoint |
|   | POP Address of OSS Operations and Maintenance System |   | pop-api-endpoint |
|   | OSS address | oss-server | api-endpoint |
| ApsaraDB RDS | RDS address | rds-yaochi | rds.openapi.endpoint |
| PolarDB-X | PolarDB-X address | drds-console | prectrl.api |
| Message Queue | MQ AK | mq-console | onsInnerApiAccessKey |
|   | MQ SK |   | onsInnerApiSecretKey |
|   | MQ address |   | console.domain |
|   | MQ Router OnsAddr | mq-router | router.onsAddr |
| SchedulerX | SchedulerX POP Address | schedulerx2 | schedulerx2PopDomainName |
|   | SchedulerX Address |   | schedulerx2DomainName |
| Domain Name System (DNS) | DNS Control Endpoint | dnsService | dns control.pop domain _ _ |
|   | DNS address |   | dns universal control.pop domain _ _ _ |
|   | DNS AK |   | genesisdns.global access key _ _ |
| 0 |   |   | > Document Version: 2026070 |

|   | DNS SK |   | genesisdns.global access secret _ _ |
|---|---|---|---|
| DataWorks | BCC API Address | apsara- bigdata- manager | bcc endpoint _ |
|   | BCC App |   | super app name _ _ |
|   | BCC Key |   | super app key _ _ |
|   | BCC Password |   | super account secret key _ _ _ |
|   | BCC User |   | super account account _ _ |
| ApsaraDB for MongoDB | MongoDB Endpoint | mongodb- yaochi | mongodb.openapi.endpoint |
| Redis | Redis Endpoint | kvstore-yaochi | kvstore.openapi.endpoint |
| Elastic Compute Service (ECS) | HDR Address | cds-bcdr | hdr.openapi.endpoint |

4. In the left-side navigation pane, choose Resource Management > **Product & Cluster**
**O&M**.
5. On the **Product & Cluster O&M** page, enter `baseServiceAll` in the search box. In the
search results, find the cluster that you want to manage and click **Cluster Details** in the
**Actions** column.
6. On the **Cluster Details** page, click the **Desired State Configuration** tab.
7. Click the **kv.conf** file and click **Show Content**.
8. Find the values in the **kv.conf** file based on the keys of corresponding products.
The following table describes the mappings between the parameters and keys.

| Product | Parameter | Key |
|---|---|---|
| OSS | OSS-POP AK | account.defaultUser.accesskey-id |
|   | OSS-POP SK | account.defaultUser.accesskey-secret |
| PolarDB- X | PolarDB-X RAM ID | account.drds.id |
|   | PolarDB-X RAM AK | account.drds.accesskey-id |
|   | PolarDB-X RAM SK | account.drds.accesskey-secret |
|   | PolarDB-X Zone value | biz zone _ |
| Apsara Stack Resilienc e (ASR) for Geo- disaster Recovery | AccessKey ID of Account to Log on to ASR-DR | account.asr.accesskey-id |
|   | AccessKey Secret of Account to Log on to ASR-DR | account.asr.accesskey-secret |
| Apsara Infrastruc ture Managem ent | Tianji ak | account.defaultUser.accesskey-id |
|   | Tianji sk | account.defaultUser.accesskey-secret |
| ApsaraDB for Lindorm | LTS Authentication AccessKey ID | account.asr.accesskey-id |
|   | LTS Authentication AccessKey Secret | account.asr.accesskey-secret |

> **Note:** If the key value is displayed in ciphertext, use the following method for decryption:

i. Log in to the container.

> ii. Run the following command to obtain the decrypted value:

```bash
curl --fail --unix-socket /var/run/proxyssl/pssl.sockrest 'http://host/api/v1/configs' -H 'Content-Type: application/octet-stream' -X POS T -d {"<Parameter key>":"<Parameter value in the ciphertext>"}
```

#### 1.9.9 Customize the data-plane SDK to implement access from multiple endpoints

**implement access from multiple endpoints**

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

O&M console of ASR for Geo-disa ster Recovery

## 2 O&M console of ASR for Geo-disaster Recovery

**Geo-disaster Recovery**

This topic describes operations related to ASR for Geo-disaster Recovery in the Apsara Unimanager Operations Console.

### 2.1 Log on to the O&M console of ASR for Geo-disaster Recovery

**ASR for Geo-disaster Recovery**

This topic describes how to log on to the O&M console of ASR for Geo-disaster Recovery.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. O&M console of ASR for Geo-disa ster Recovery

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter your username and password.
O&M console of ASR for Geo-disa ster Recovery

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to unlock the account.

> The first time that you log on to the Apsara Uni-manager Operations Console, change the password for your username as prompted.
> To enhance security, your password must meet the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Platform**
**Operation > Disaster Recovery Management > ASR for Geo-disaster Recovery**.

### 2.2 Homepage

The homepage of the ASR for Geo-disaster Recovery O&M console displays information in the following sections: Authorization usage statistics, Node task load statistics, Total number of abnormal synchronization entities, Unassigned task statistics, Bandwidth Usage, and Dedicated Line traffic usage.

> **Important:** When deploying the ASR for Geo-disaster Recovery O&M console, you must also configure information about the instances that are connected over Express Connect circuits. Otherwise, instance data cannot be displayed in the line charts on the homepage.
> To configure Express Connect circuit-connected instance information, contact Apsara Stack engineers.

O&M console of ASR for Geo-disa ster Recovery

**Parameters**

| Parameter | Description |
|---|---|
| Authorization usage statistics | Displays the usage of protection groups and synchronization entities in a doughnut chart. The blue color indicates the usage of protection groups. The yellow color indicates the usage of synchronization entities. The numerator represents the used quota and the denominator represents the total authorized quota. |
| Node task load statistics | Displays the number of tasks distributed on each ASR for Geo- disaster Recovery node in a doughnut chart. |
| Total number of abnormal synchronization entities | Displays the number of abnormal synchronization entities based on the statistics of disaster recovery services in a doughnut chart. |
| Unassigned task statistics | Displays the unassigned synchronization tasks in a doughnut chart. |
| Bandwidth Usage | Displays the traffic and bandwidth usage of ApsaraDB RDS and Object Storage Service (OSS) in line charts. |
| Dedicated Line traffic usage | Displays the inbound and outbound traffic usage of the instances that are connected over Express Connect circuits to ASR for Geo-disaster Recovery in line charts. |

O&M console of ASR for Geo-disa ster Recovery

### 2.3 Disaster recovery monitoring

#### 2.3.1 View the cloud platform monitoring

Cloud platform monitoring is designed to monitor the disaster recovery status of cloud services, including metrics such as service availability, domain name resolution, and network access. It allows you to quickly switch your cloud platform to another region when a region fails, thereby ensuring business continuity.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console from the
Apsara Uni-manager Operations Console.
2. In the left-side navigation pane, choose **Disaster Recovery Monitoring** > **Cloud**
**Platform Monitoring**.
3. Select a value from the Disaster Recovery Interconnection drop-down list to view the
service inspection information in the selected interconnected regions. O&M console of ASR for Geo-disa ster Recovery
4. Move the pointer over a service to view the check details of the service.
5. Click **View More**. In the panel that appears, view the details of check items.

#### 2.3.2 View the protection group monitoring

This topic describes how to view the check results of synchronization entities in a protection group. O&M console of ASR for Geo-disa ster Recovery
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console from the
Apsara Uni-manager Operations Console.
2. In the left-side navigation pane, choose **Disaster Recovery Monitoring** > **Protection**
**Group Status Monitoring**.
3. Find the protection group that you want to view and click **View Check Results** in the
Actions column. In the panel that appears, view the following information about each synchronization entity in the protection group: synchronization entity name, cloud service, synchronization status, synchronization latency, primary instance status, secondary instance status, and the time when the check was performed.

### 2.4 Basic capability O&M

This topic describes the basic capability O&M features of ASR for Geo-disaster Recovery. In the ASR for Geo-disaster Recovery O&M console, the basic capability O&M features of ASR for Geo-disaster Recovery are categorized into the following modules: cloud information management, parameter management, node management, virtual private cloud (VPC) management, capacity management, and data upgrade. The following table describes the features.

| Functional module | Description | Remark | Operation |
|---|---|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Cloud information management | You can view information about all clouds and remove the instances that you no longer need. | Before you remove an instance, make sure that it does not contain resources such as protection groups or plans. If you remove an instance, its information is also deleted, including the registered VPC, region configurations, and cloud service configurations. The region configurations include the services that support disaster recovery in the specified region and service status. | Refresh data: Click the icon to refresh data. Change the display mode: Click the icon and select Default or Compact to change the display mode. Customize displayed columns: Click the icon and select the columns that you want the system to display on the page. Enable or disable the full screen mode: Click the icon to display data in full screen mode. Then, click the icon to disable the full screen mode. |
|---|---|---|---|
| Parameter management | You can dynamically configure service parameters. | N/A | 1. On the Parameter Management page, find the service whose parameters that you want to manage and click the corresponding tab. On the tab that appears, configure the parameters as prompted. 2. Click Submit. |
| Node management | You can view information about nodes in your ASR for Geo-disaster Recovery cluster and view unassigned tasks. To view the tasks that are being run on a node, find the node and click Details in the Actions column. | N/A | Click Show unassigned tasks to display the list of unassigned tasks. |

O&M console of ASR for Geo-disa ster Recovery

| VPC manag ement | Regist ration infor matio n mana geme nt | If an instance is registered with a VPC, you can view and delete the registration information. If an instance is not registered with a VPC, you can register the cloud with a VPC. If a VPC authorization error occurs or a VPC fails to be accessed, you can check the validity of the registration information by calling a specific operation to determine whether the values of the appId and addressPoolId parameters are still valid. | N/A | Refresh data: Click the icon to refresh data. Change the display mode: Click the icon and select Default or Compact to change the display mode. Customize displayed columns: Click the icon and select the columns that you want the system to display on the page. Enable or disable the full screen mode: Click the icon to display data in full screen mode. Then, click the icon to disable the full screen mode. |
|---|---|---|---|---|
|   | Autho rizatio n infor matio n mana geme nt | If an instance is authorized to be accessed within a VPC, you can view the VPC authorization information. If an instance is not authorized to be accessed within a VPC, you can authorize the instance to be accessed within a VPC. | N/A | 1. On the Authorization Information in VPC tab of the VPC Management page, configure the Instance, Region Name, and Instance ID parameters. 2. Click Search. |
| Disaster recovery gateway management |   | You can manage and configure disaster recovery gateways across clouds. | N/A | For more information, see Manage a disaster recovery gateway. |
| Capacity management |   | You can view the resource usage of protection groups and synchronization entities. | N/A | N/A. |

O&M console of ASR for Geo-disa ster Recovery

| Dashboard map configuration | You can create a disaster recovery region that is displayed on the dashboard. | N/A | For more information, see Configure a dashboard map. |
|---|---|---|---|
| Data upgrade | You can upgrade all data of protection groups and disaster recovery plans. | Existing users are required to upgrade data after a version update. | 1. On the Data Upgrade page, click Data Upgrade. 2. In the Delete Synchronization Entity message, click OK. 3. Upgrade data as prompted. |

#### 2.4.1 Manage cloud product information

Before you use the geo-disaster recovery platform in the Apsara Uni-manager Management Console, you must configure the disaster recovery and production clouds in the Apsara Unimanager Operations Console. After you add a production cloud instance, you must configure the supported disaster recovery products and their endpoints. This allows ASR-DR to perform disaster recovery for resource instances in the production cloud. This topic describes the configurations for a cross-cloud disaster recovery scenario.

**Precautions**

When you first log on to the geo-disaster recovery platform from the Apsara Uni-manager Operations Console, you must configure the disaster recovery cloud as shown in the following figure. Click **Edit** in the **Disaster Recovery Cloud** area, or click **Edit** in the **Actions** column of the list. After the configuration is successful, the status changes to running. For parameter configurations, see the table in the Procedure section.
1. Log on to the geo-disaster recovery Operations and Maintenance (O&M) platform.
2. In the navigation pane on the left, choose **Platform Basic O&M > Cloud Information**
**Management**.
O&M console of ASR for Geo-disa ster Recovery
3. Click **Add Cloud** and configure the parameters as described in the following table.

| Name | Description |
|---|---|
| Cloud Name | A custom name for the cloud center for easy identification. The name must be 4 to 20 bytes in length and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |

O&M console of ASR for Geo-disa ster Recovery

| Cloud Category | Select the cloud category of the production cloud. Agile Edition Enterprise Edition Public Cloud Note If you set Cloud Category to Public Cloud, go toP arameter Configuration Management and modify the parameter values for SYNC CHANNEL. This _ includes the following parameters. `true` indicates enabled and `false` indicates disabled. We recommend that you keep the default values for other parameters: guard::daemonEnabled: Specifies whether to enable protection group status synchronization. recovery::daemonEnabled: Specifies whether to enable data synchronization for disaster recovery plan tasks. resource-sync::resourceSyncEnable: Specifies whether to enable data synchronization for resources such as protection groups and disaster recovery plans. resource-sync::asyncPullEnabled: Allows the public cloud to remotely pull data of cloud instances, protection groups, and disaster recovery plans from Apsara Stack. |
|---|---|
| Cloud Managemen t | Select the management type for the production cloud. SelectG eo-disaster recovery platform. ASCM Management Platform: The disaster recovery cloud calls APIs to obtain information about the production cloud. Geo-disaster recovery platform (Recommended): The disaster recovery cloud calls ASR-DR APIs to obtain information about the production cloud. |
| Managemen t API Endpoint | Enter the value of Management API Endpoint for the peer cloud from the Cloud Information Management menu of the geo-disaster recovery platform. If you set Cloud Category to Public Cloud, enter the value of Management API Endpoint from the Cloud Information Management menu of the geo- disaster recovery platform on the public cloud. |
| AccessKey ID and AccessKey secret | If you set Cloud Category to Agile Edition or Enterprise Edition, enter the AccessKey ID and AccessKey secret of the operations administrator account on the peer cloud. For more information, see Obtain an AccessKey pair. If you set Cloud Category to Public Cloud, create a RAM user with the AliyunASRFullAccess permission on the public cloud, and enter its AccessKey ID and AccessKey secret. |

O&M console of ASR for Geo-disa ster Recovery

| Protocol | Optional. This parameter is required if you set Cloud Category to Public Cloud. Select this to agree to the terms of service for the geo-disaster recovery platform on the public cloud. |
|---|---|

4. Click **Verify**. After the verification is successful, click **OK**.
5. Configure cloud products.
i. In the **Actions** column for the desired cloud, click **Configuration** to go to the **Cloud**
**Product Configuration** page.
ii. In the **Basic Products** area, click the icon for the product and configure the parameters as described in the following table.

> **Important:** If the management type of the cloud instance is **ASCM Management** **Platform**, the default configurations retrieved by the system for the cloud product may be incorrect. You must verify these configurations. For more information about how to obtain the configuration information for each product, see Obtain the configuration information of the production cloud instance.
> If the management type of the cloud instance is **Geo-disaster recovery** **platform**, the default configurations retrieved by the system for the cloud product are accurate and do not need to be verified.

| Product | Name | Description |
|---|---|---|
|   | ASCM address | The endpoint used for single sign-on (SSO), authentication, and resource retrieval. Set this to the value of ascm-portal.domain for the oneService service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |

|   | ascm-portal.domain |
|---|---|
| oneService |   |

|   | console of ASR for ecovery |   |   |   |   |   |
|---|---|---|---|---|---|---|
|   | Apsara Stack Cloud Management (ASCM) |   |   |   |   |   |
|   |   |   | asapi address | The endpoint used to call asapi APIs. Set this to the value of asapi.gateway.endpoint for the asapi service. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   |   |   | ASCM POP Address | The endpoint used to call ASCM POP APIs. For the central region, use the ascm.{ internet-domain} format. For a unit region, use the ascm.{region}.{internet- domain} format. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   |   |   |   |   | ascm.{region}.{internet- |   |
|   |   |   |   | domain} |   |   |
|   | Data Transmission Service (DTS) |   | DTS address | The endpoint used to create synchronization links for database products. Set this to the value of dts.openapi.endpoint for the dts-dts service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   |   |   | DTS Check address | Set this to the value of dts.check.dns:dts.check.port for the dts-dts service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   |   |   | DTS Check interface credential | Set this to the value of dts.check.token for the dts-dts service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   | Product Servitization Foundation |   | oneConsole address | The endpoint used to query environment information. Set this to the value of console.domain for the oneService service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |   |   |
|   | Virtual Private Cloud (VPC) |   | VPC address | The endpoint used to register VPCs and connect to VPC- type PolarDB-X 1.0 and RDS instances. This corresponds to the value of vpc-inner.openapi.endpoint for the vpc-yaochi service in the production cloud. ASR- DR automatically configures this parameter, but you must confirm the value. |   |   |

|   | vpc-inner.openapi.endpoint |
|---|---|
| vpc-yaochi |   |

O&M console of ASR for Geo-disa ster Recovery

|   | Resource Access Management (RAM) | RAM address | The endpoint used to authenticate the AccessKey ID and AccessKey secret of a RAM user. Set this to the value of ram-openapi.endpoint for the ram-ramService service. For more information, see Obtain the configuration information of the production cloud instance. Important You must configure the RAM address for the central region. |   |   |   |
|---|---|---|---|---|---|---|
|   |   | RAM Slave address | The endpoint used to implement RAM authentication. Set this to the value of ram-slave.endpoint for the ram-ramService service. For more information, see Obtain the configuration information of the production cloud instance. |   |   |   |
|   |   | STS address | The endpoint used to obtain a temporary token for an Alibaba Cloud account. Set this to the value of sts- openapi.endpoint for the ram-ramService service. For more information about how to obtain the parameter, see Obtain the configuration information of the production cloud instance. Important You must configure the Security Token Service (STS) address for the central region. |   |   |   |
|   |   |   |   |   | sts- |   |
|   |   |   |   | ram-ramService |   |   |
|   |   | asrdr AK | The AccessKey ID of the account requested by asrdr. It is used to run check commands by calling Remote System Management (RSM) in the production cloud. For more information, see Obtain an AccessKey pair. |   |   |   |
|   |   | asrdr SK | The AccessKey secret of the account requested by asrdr. It is used to run check commands by calling RSM in the production cloud. For more information, see Obtain an AccessKey pair. |   |   |   |
|   |   | asrdr api endpoint | The endpoint used to call ASR-DR OpenAPI. Set this to the value of asrdr api endpoint for the asrdr- _ _ backend service. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |   |

|   | openapi.endpoint |
|---|---|

| asrdr- |   |
|---|---|

|   | backend |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

|   | Geo-disaster recovery platform (ASR- DR) |   |   |   |
|---|---|---|---|---|
|   |   |   | asrdr osssync api endpoint | The endpoint used to call the OpenAPI of the asrdr- osssync service of ASR-DR. Set this to the value of asrdr-osssync for the asrdr-osssync service. ASR-DR automatically configures this parameter, but you must confirm the value. Note For an incremental AsrOssSyncServiceCluster, you must roll the ASR-DR cluster again for ASR-DR to automatically configure this parameter. |
|   |   |   | asrdr resource endpoint | The endpoint used to obtain resource plans from ASR- DR. Set this to the value of asrdr resource endpoint for the asrdr service. _ _ ASR-DR automatically configures this parameter, but you must confirm the value. |
|   |   |   | asrdr service account AK | The AccessKey ID of the asrdr service account, used for STS temporary token calls. Set this to the value of account.asr.accesskey-id . For more information, see Obtain the configuration information of the production cloud instance. |
|   |   |   | asrdr service account SK | The AccessKey secret of the asrdr service account, used for STS temporary token calls. Set this to the value of account.asr.accesskey-secret . For more information, see Obtain the configuration information of the production cloud instance. |
|   | Apsara Infrastructure Management |   |   | The AccessKey ID required to call Tianji POP APIs. Set this to the value of account.defaultUser.accesskey- id . For more information, see Obtain the configuration information of the production cloud instance. |
|   |   |   | Tianji AK | id |
|   |   |   | Tianji SK | The AccessKey secret required to call Tianji POP APIs. Set this to the value of account.defaultUser.accesskey-secret . For more information, see Obtain the configuration information of the production cloud instance. |
|   |   |   | Tianji endpoint | The endpoint used to call the OpenAPI of Tianji to obtain cluster status information. Set this to the value of api server.endpoint for the tianji-endpoint _ service. ASR-DR automatically configures this parameter, but you must confirm the value. |

| asrdr- |   |
|---|---|

| account.defaultUser.accesskey- |   |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Remote System Management (RSM) |   | RSM address | The endpoint used to call the OpenAPI of RSM to execute network check commands. Set this to the value of rsm.api.domain for the rsm service. ASR-DR automatically configures this parameter, but you must confirm the value. |
|---|---|---|---|
| Parthenon |   | Parthenon Endpoint | The endpoint that is used to call the Parthenon API to check the cross-cloud network connectivity of products deployed on the PaaS platform. ASR for Geo-disaster Recovery automatically configures this parameter, but you must confirm it. Parthenon Endpoint format: region.api.parthenon.intranet-domain. Confirm the values of region and intranet-domain in the kv.conf file in the desired state configuration of the Apsara Infrastructure Management cluster. |
| Server Load Balancer (SLB) |   | SLB API Address | The endpoint used to call SLB APIs to modify the status of an instance's virtual IP address (VIP). ASR-DR automatically configures this parameter, but you must confirm the value. The value of the SLB API address is service:slb-controller:slb.api.domain . |
|   |   | DEFAULT AK | The AccessKey ID required to call SLB APIs. Set this to the value of account.defaultUser.accesskey-id . For more information, see Obtain the configuration information of the production cloud instance. |
|   |   |   | The AccessKey secret required to call SLB APIs. Set this to the value of account.defaultUser.accesskey- secret . For more information, see Obtain the configuration information of the production cloud instance. |
|   |   | DEFAULT SK | secret |
|   |   | SLB OPS API Address | The endpoint used to call SLB OPS APIs to get the load balancing ID of an instance and the user ID of the instance owner. ASR-DR automatically configures this parameter, but you must confirm the value. The value of the SLB OPS API address is service:slb-ops- api:slb ops api dyn url . _ _ _ _ |

| account.defaultUser.accesskey- |   |
|---|---|

|   |   | service:slb-ops- |
|---|---|---|
|   | api:slb ops api dyn url _ _ _ _ |   |

iii. In the **Disaster Recovery Products** area, click the icon, select a disaster recovery product type, and configure the parameters for the selected product type as described in the following table.

| Product | Name | Description |
|---|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Object Storage Service (OSS) | OSS address | The endpoint used to call OSS synchronization APIs and query OSS instances. Set this to the value of api-endpoint for the oss- server service in the production cloud. ASR- DR automatically configures this parameter, but you must confirm the value. |
|---|---|---|
|   | POP address of OSS Storage Operations and Maintenance System | The endpoint used to call OSS POP APIs. Set this to the value of pop-api-endpoint for the oss-chiji service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   | OPS-Admin AK | The AccessKey ID that is verified when ASR-DR calls OSS POP APIs. Enter the AccessKey ID of the opsadmin account for the Apsara Uni- manager Operations Console. |
|   | OPS-Admin SK | The AccessKey secret that is verified when ASR- DR calls OSS POP APIs. Enter the AccessKey secret of the opsadmin account for the Apsara Uni-manager Operations Console. |
|   | OSS proxy user PK | The permission to authorize a proxy user to access a bucket. For more information about how to obtain the UID, see the Product disaster recovery configuration > OSS disaster recovery configuration section in the Apsara Stack v3.*** Deployment Guide. Enter the UID of the proxy user created in the Apsara Uni-manager Management Console. |
| Tablestore Note If the cloud management type is ASRDR, the information of the Tablestore proxy's Alibaba Cloud account is automatically registered. | OTS Tunnel service address | The endpoint used to call the synchronization APIs of Tablestore in the Tunnel architecture. Set this to the value of ocm.pop tablestore endpoint for the _ _ TableStoreOCM service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   | OTS proxy Alibaba Cloud account PK | Authorizes the Tablestore product to access instances on the production site. For more information about how to obtain this, see the Product disaster recovery configuration > OTS disaster recovery configuration section in the Apsara Stack v3.*** Deployment Guide. Enter the UID of the proxy's level-1 organization created in the Apsara Uni-manager Management Console. |

|   | server |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

|   | In a cross- cloud scenario , configuri ng the producti on cloud registers the |   |   |   |
|---|---|---|---|---|
|   |   |   | OTS Proxy's Alibaba Cloud Account AK | Authorizes the Tablestore product to access instances on the production site. For more information about how to obtain this, see the Product disaster recovery configuration > OTS disaster recovery configuration section in the Apsara Stack v3.*** Deployment Guide. Enter the AccessKey ID of the proxy's level-1 organization created in the Apsara Uni-manager Management Console. |
| configur ations for both clouds. The configur ation order must be: disaster recovery cloud > producti on cloud. In a cross- region scenario , configuri ng the producti on region registers the configur ations for both regions. The configur ation order must be: disaster recovery region > producti on region. | configur ations for both clouds. The configur ation order must be: disaster recovery cloud > producti on cloud. In a cross- region scenario , configuri ng the producti on region registers the configur ations for both regions. The configur ation order must be: disaster recovery region > producti on region. |   | OTS proxy Alibaba Cloud account SK | Authorizes the Tablestore product to access instances on the production site. For more information about how to obtain this, see the Product disaster recovery configuration > OTS disaster recovery configuration section in the Apsara Stack v3.*** Deployment Guide. Enter the AccessKey secret of the proxy's level- 1 organization created in the Apsara Uni- manager Management Console. |
|   |   |   | OTS OCM internal address | Used to register the information of the Tablestore proxy's Alibaba Cloud account. Set this to the value of ocm.endpoint for the TableStoreOCM service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |

O&M console of ASR for Geo-disa ster Recovery

| AnalyticDB for MySQL 3.0 | ADB 3.0 address | The endpoint used to call APIs for querying ADB 3.0 instances, granting permissions, and other operations. Set this to the value of adb.openapi.endpoint for the analyticdb-yaochi service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|---|---|---|
| ApsaraDB RDS | RDS address | The endpoint used to call APIs for querying RDS instances, granting permissions, and other operations. Set this to the value of rds.openapi.endpoint for the rds- yaochi service in the production cloud. ASR- DR automatically configures this parameter, but you must confirm the value. |
| Cloud-native distributed database PolarDB-X | PolarDB-X address | The endpoint used to call APIs for querying PolarDB-X 1.0 instances, granting permissions, and other operations. Set this to the value of prectrl.api for the drds-console service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
| PolarDB | PolarDB address | The endpoint used to call APIs for querying PolarDB instances, granting permissions, and other operations. Set this to the value of polardb.openapi-vpc.endpoint for the polardb-yaochi service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. ASR-DR automatically configures this parameter, but you must confirm the value. |
| Message Queue (MQ) | Supported product type | Select MQ. |
|   | MQ Router OnsAddr address | The endpoint used to call MQ synchronization APIs. Set this to the value of router.onsAddr for the mq-router service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   | MQ address | The endpoint used to call MQ topic operation APIs. Set this to the value of console.domain for the mq-console service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |

|   |   | rds.openapi.endpoint |
|---|---|---|
|   | yaochi |   |

O&M console of ASR for Geo-disa ster Recovery

|   |   | onsInnerApi | The AccessKey ID that is verified when ASR-DR calls MQ APIs. Set this to the value of onsInnerApiAccessKey for the mq- console service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |
|---|---|---|---|
|   | Message Queue for Apache Kafka | KafkaPop management address | The endpoint used to call the POP management APIs of Kafka. Set this to the value of kafka- openapi.endpoint for the alibaba-kafka- console service in the production cloud. ASR- DR automatically configures this parameter, but you must confirm the value. |
|   | API Gateway | API Gateway address | The endpoint used to call API Gateway APIs. Set this to the value of cop pop api domain biz for the csb- _ _ _ _ cop-cop-cop-console service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   | DNS (Domain Name System) | DNS CONTROL address | The endpoint used to call DNS Control APIs. Set this to the value of dns control.pop domain for the _ _ dnsService service in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |
|   |   | DNS address | The endpoint used to call DNS operation APIs. Set this to the value of dns universal control.pop domain for _ _ _ the dnsService service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   |   | DNS AK | The AccessKey ID that is verified when ASR-DR calls DNS APIs. Enter the AccessKey ID of the disaster recovery organization in the Apsara Uni-manager Management Console. |
|   |   | DNS SK | The AccessKey secret that is verified when ASR- DR calls DNS APIs. Enter the AccessKey secret of the disaster recovery organization in the Apsara Uni-manager Management Console. |

|   |   | onsInnerApiAccessKey |
|---|---|---|
|   | console |   |

|   | kafka- |   |
|---|---|---|
| alibaba-kafka- |   |   |

|   |   | openapi.endpoint |
|---|---|---|
| ement s |   |   |
|   |   | console |

|   |   | cop pop api domain biz _ _ _ _ |
|---|---|---|
|   | cop-cop-cop-console |   |

O&M console of ASR for Geo-disa ster Recovery

| SchedulerX | SchedulerX pop address | The endpoint used to call APIs related to SchedulerX synchronization links. Set this to the schedulerx2PopDomainName address of SchedulerX in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|---|---|---|---|---|
|   | SchedulerX Address | The endpoint used to call APIs for querying SchedulerX instances, setting read/write permissions, and other operations. Set this to the schedulerx2DomainName address of SchedulerX in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
| DataWorks | BCC API address | The Configuration Center BCC API of Apsara Bigdata Manager in the production cloud. Set this to the value of api.endpoint for the bcc-web service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   | BCC App | The Configuration Center AppName of Apsara Bigdata Manager in the production cloud. Set this to the value of maxgraph-app for the bcc-web service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   | BCC Key | The Configuration Center AppKey of Apsara Bigdata Manager in the production cloud. Set this to the value of maxgraph-key for the bcc-web service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   | BCC Password | The Configuration Center AuthUserKey of Apsara Bigdata Manager in the production cloud. Set this to the value of maxgraph- passwd for the bcc-web service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |
|   |   |   | maxgraph- |   |
|   | BCC User | The Configuration Center AuthUser of Apsara Bigdata Manager in the production cloud. Set this to the value of maxgraph-user for the bcc-web service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |   |

| rd | passwd |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

|   | ApsaraDB for HBase | HBase address | The endpoint used to call APIs for querying HBase instances, granting permissions, and other operations. Set this to the value of hbase.openapi.endpoint for the hbase- yaochi service. ASR-DR automatically configures this parameter, but you must confirm the value. |
|---|---|---|---|
|   | Lindorm Multi- model Database | Lindorm address | The endpoint used to call Lindorm operation APIs. Set this to the value of lindorm pop endpoint for the lindorm _ _ service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   |   | LTS authentication AK | The AccessKey ID that is verified when ASR-DR calls Lindorm Tunnel Service (LTS) APIs. Set this to the value of account.asr.accesskey-id in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |
|   |   | LTS authentication SK | The AccessKey secret that is verified when ASR- DR calls LTS APIs. Set this to the value of account.asr.accesskey-secret in the production cloud. For more information, see Obtain the configuration information of the production cloud instance. |
|   | ApsaraDB for MongoDB | MongoDB address | The endpoint used to call APIs for querying MongoDB instances, granting permissions, and other operations. Set this to the value of mongodb.openapi-vpc.endpoint for the mongodb-yaochi service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   | ApsaraDB for Redis | Redis address | The endpoint used to call APIs for querying Redis instances, granting permissions, and other operations. Set this to the value of kvstore.openapi-vpc.endpoint for the kvstore-yaochi service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |
|   |   | Hologres management address | The endpoint used to call APIs for querying Hologres instances, granting permissions, and other operations. Set this to the value of holo- manager.endpoint for the hologres-init service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |

|   |   | hbase.openapi.endpoint |
|---|---|---|
|   | yaochi |   |

|   | holo- |
|---|---|
| hologres-init |   |

|   | manager.endpoint |
|---|---|

|   | or Geo-disaster User G console of ASR for Geo ecovery |   |   |   |
|---|---|---|---|---|
|   | Interactive Analysis of Hologres |   |   |   |
|   |   | Hologres-pop address | The endpoint used to call Hologres-pop APIs. Set this to the value of pop holo remote recover dns for the _ _ _ _ hologres-init service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |
|   | Elastic Compute Service (ECS) | HDR address | The endpoint used to call High Dynamic Range (HDR) APIs. Set this to the value of hdr.openapi.endpoint for the cds- bcdr service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |
|   | DataHub | DataHub Address | The endpoint used to call DataHub APIs. Set this to the value of datahub frontend.endpoint _ for the datahub-frontend service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |
|   | Cloud-native distributed database PolarDB-X 2.0 | PolarDB-X 2.0 Address | The endpoint used to call PolarDB-X 2.0 APIs. Set this to the value of polarx.openapi.endpoint for the apsaradb-polarx-engine-openapi service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |
|   | Ingress Gateway | ECS POP API Address | The endpoint used to call ECS APIs. Set this to the value of ecs.openapi.endpoint for the ecs-yaochi service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |
|   |   | SLB POP API Address | The endpoint used to call SLB APIs. Set this to the value of slb.api.domain for the slb- controller service in the production cloud. ASR-DR automatically configures this parameter, but you must confirm the value. |   |

|   | ecs.openapi.endpoint |
|---|---|
| ecs-yaochi |   |

|   |   | slb.api.domain |
|---|---|---|
|   | controller |   |

iv. After you configure all products, return to the **Cloud Information Management** page to perform other operations.

**Related operations**

After you add a cloud, you can also perform the following operations.

| Task Name | Procedure |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Edit Cloud | 1. Click Edit in the Actions column. 2. In the dialog box that appears, modify the parameter values. 3. After you complete the modification, click Verify. After the verification is successful, click OK. |
|---|---|
| Delete a cloud | 1. Click Delete in the Actions column. 2. In the message that appears, click OK. |

#### 2.4.2 Manage a disaster recovery interconnection

**interconnection**

This topic describes how to create an interconnection between regions to implement crossregion disaster recovery.
1. Log in to the Apsara Stack Resilience (ASR) for Geo-disaster Recovery console from the
Apsara Uni-manager Operations Console.
2. In the left-side navigation pane, choose **General > Disaster Recovery Interconnection**
**Management**.
3. On the Disaster recovery Interconnection Management page, click **New Disaster**
**Recovery interconnection**. In the dialog box that appears, configure parameters as
prompted. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Disaster recovery interconnection name | The name for the disaster recovery interconnection. You can specify a custom name. |
| Description | The description of the disaster recovery interconnection. |
| Regions with Disaster Recovery Interconnections Configured | The regions to be interconnected for disaster recovery. Specify at least two regions, one as the primary region, the other as the secondary region. |

O&M console of ASR for Geo-disa ster Recovery

| Services with Disaster Recovery Interconnections Configured | The cloud services for disaster recovery interconnection. The system automatically identifies the cloud services that support disaster recovery in the specified interconnected regions. Use the default value. |
|---|---|

4. Click **Submit**.

**What to do next**

| Operation | Procedure |
|---|---|
| Start interconnection | Click Unicom in the Operation column of the disaster recovery interconnection. If the interconnection fails, click Retry to perform a reconnection. |
| View details of the disaster recovery interconnection | Click Details in the Operation column of the disaster recovery interconnection. In the dialog box that appears, view the basic information and connection status of the services in the interconnected regions. |
| Modify the disaster recovery interconnection | 1. Click Edit in the Operation column of the disaster recovery interconnection. 2. In the dialog box that appears, modify settings as needed, and then click Submit. |
| Delete the disaster recovery interconnection | 1. Click Delete in the Operation column of the disaster recovery interconnection. 2. In the message that appears, click OK. |

#### 2.4.3 Manage a disaster recovery gateway

This topic describes how to configure peer gateway information across clouds to establish a disaster recovery relationship and a network connection between two cross-cloud ends.

**Background information**

For security purpose, API operations in control domains cannot be called across clouds. They are encapsulated and registered into POP to form an independent disaster recovery gateway, improving API operation management efficiency and providing API operations for other disaster recovery services.
1. Log on to the ASR for Geo-disaster Recovery O&M console.
O&M console of ASR for Geo-disa ster Recovery
2. In the left-side navigation pane, choose **Basic Platform O&M > Disaster Recovery**
**Gateway**. The disaster recovery regions among which a disaster recovery relationship is
established are displayed.
3. Click **Add ACL** to configure the requester information as described in the following table,
and then click **Next**. Access Control List (ACL) defines and manages inbound and outbound data packets to ensure that network traffic meets security policies and access control requirements.

| Parameter | Description |
|---|---|
| Requester Product | The cloud service that you want to connect to the requester cloud. Example: ASR for Geo- disaster Recovery. |
| Requester CIDR Block | The CIDR block where the API operation of the requester cloud service resides. It is in the format of *.*.*.*/mask. Example: 192.168.1.0/24. |
| Requester UID | The UID of the AccessKey pair of the requester user. You can obtain the UID from user information in the requester. |

O&M console of ASR for Geo-disa ster Recovery
4. In the **Manage Action Permissions** step, select services in the destination end and then
click **Next**.
5. Click **Submit**.

**Related operations**

| Operation | Procedure |
|---|---|
| View the ACL. | 1. Click View ACL in the Actions column corresponding to a region. 2. Click Details in the Actions column. |
| Modify ACL | 1. Click View ACL in the Actions column corresponding to a region. 2. Click Modify in the Actions column. 3. Select another action and then click Submit. |
| Delete ACL | 1. Click View ACL in the Actions column corresponding to a region. 2. Click Delete in the Actions column. 3. In the message that appears, click OK. |

#### 2.4.4 Configure a dashboard map

This topic describes how to configure disaster recovery regions displayed on a dashboard. After configuration, the geo-disaster recovery data is displayed on the dashboard.

**Scenarios**

O&M console of ASR for Geo-disa ster Recovery
**Geo-disaster recovery**: This solution is widely used in industries such as public services,
energy, transportation, and health and medical insurance. This solution is applicable to the following scenarios: High business continuity is required. Strong data consistency is not required. Regional fault prevention is required. The distance between regions is more than 100 km.
**Three data centers across two regions** : This solution is mainly used in the financial
industry and is applicable to the following scenarios: Prevention of city-level natural disasters is required. Regional fault prevention is required. Near zero synchronization latencies for business-critical data are required. The budget is adequate.
1. Log on to the ASR for Geo-disaster Recovery O&M console.
2. In the left-side navigation pane, choose **Basic Platform O&M > > Dashboard Map**
**Configuration**.
3. On the Dashboard Map Configuration page, click **Create Disaster Recovery Region**. In
the Create Disaster Recovery Region dialog box, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region that you want to use. |
| Region Name | The name of the region. Example: Hangzhou data center. |
| City | The city in which the region resides. |
| Zone | The zone of the region. The system automatically generates zone names. |

4. Click **OK**.

**Related operations**

After you create a disaster recovery region, you can also perform the operations described in the following table.

| Operation | Procedure |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Query the disaster recovery region | Enter region and zone names, and select a city from the drop-down list. The system automatically filters the matched disaster recovery region. |
|---|---|
| Edit the disaster recovery region | 1. Find the disaster recovery region and click Edit in the Actions column. 2. In the Edit Disaster Recovery Region dialog box, enter a new region name or select another city. 3. Click OK. |
| Delete the disaster recovery region | 1. Find the disaster recovery region and click Delete in the Actions column. 2. In the message that appears, click OK. |

### 2.5 Disaster recovery O&M

This topic describes the disaster recovery O&M features of ASR for Geo-disaster Recovery. The disaster recovery O&M features of ASR for Geo-disaster Recovery are categorized into the synchronization entity management and plan management modules. The following table describes the modules.

| Module |   | Description | Remark |
|---|---|---|---|
| Synchronization entity management |   | You can view the list and details of protection groups, delete the protection groups and synchronization entities that you no longer need, view the tasks of each synchronization entity, view the step details of each task, view the run logs of each step, retry a step, and skip a step. | If a step of a task fails, you can retry the step. This way, the task continues to be run from this step. If a step of a task fails multiple times, you can skip the step. This is applicable if the skipped step does not affect subsequent steps. This way, the task continues to be run from the next step. |
| Plan management | Drill switchover | You can view the records of drill plans and disaster recovery plans that are run, unbind the plans that are run, view the details and step details of each record, view the running logs of each step, retry a step, skip a step, and skip all steps. | If a step of a plan fails multiple times, you can skip all optional steps. Note This operation is generally performed when the primary site fails. In this case, all steps related to the primary site are skipped at a time. |
|   | Drill switchback |   |   |
|   | Fault switchover |   |   |
|   | Fault switchback |   |   |

O&M console of ASR for Geo-disa ster Recovery

#### 2.5.1 Manage synchronization entities

##### 2.5.1.1 Skip a step

The procedure to skip a single step in the synchronization entity management and plan management sections are the same. This topic describes how to skip a single step in the synchronization entity management section.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, view the synchronization entity information. Find
the synchronization entity that you want to manage and click **Task** in the Actions column.
5. In the panel that appears, click the plus signs (+) to the left of a task to view the steps of
the task.
6. Find a step that is in the **Failed** state and click **Skip** in the Actions column.
7. After the step is skipped, the step changes to the **Skip** state.
O&M console of ASR for Geo-disa ster Recovery

**Related operations**

On the Protection Group page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| Perform advanced search | 1. Configure the Primary Clouds, Protection Group ID, Protection Group Name, and Synchronization Direction parameters. 2. Click Search to search for a specific protection group. If the filter conditions are incorrect, click Reset to clear the filter conditions. |
| Refresh data | Click the icon to refresh the protection group list. |
| Change the display mode | Click the icon and select the Default or Compact display mode. |

O&M console of ASR for Geo-disa ster Recovery

| Customize displayed fields | Click the icon and select the fields that you want to display on the page. |
|---|---|
| Enable the full screen mode | Click the icon to display data in full screen mode. Click the icon to disable the full screen mode. |

##### 2.5.1.2 Reperform a single step

The procedure to reperform a single step in the synchronization entity management and plan management sections are the same. This topic describes how to reperform a single step in the synchronization entity management section.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, view the synchronization entity information. Find
the synchronization entity that you want to manage and click **Task** in the Actions column.
5. In the panel that appears, click the plus signs (+) to the left of a task to view the steps of
the task.
6. Find a step that is in the **Failed** state and click **Retry** in the Actions column.
O&M console of ASR for Geo-disa ster Recovery
7. After the step is reperformed, the step changes to the **Complete** state.

**Related operations**

On the Protection Group page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| Perform advanced search | Configure the Primary Clouds, Protection Group ID, Protection Group Name, and Synchronization Direction parameters. |
| Refresh data | Click the icon to refresh the protection group list. |
| Change the display mode | Click the icon and select the Default or Compact display mode. |
| Customize columns | Click the icon and select the columns that you want to display on the page. |

O&M console of ASR for Geo-disa ster Recovery

##### 2.5.1.3 Configure throttling

You can configure throttling only for instances of the Object Storage Service (OSS), ApsaraDB RDS, Distributed ApsaraDB RDS DRDS, ApsaraDB Redis, or ApsaraDB MongoDB.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find a protection group to which OSS, ApsaraDB RDS,
ApsaraDB RDS DRDS, ApsaraDB Redis, or ApsaraDB MongoDB instance belong and click
**Details** in the **Actions** column.
4. In the synchronization entity list of the **Protection Group Details** page, click **Throttling**
**Configuration** in the **Actions** column.
5. In the Throttling Configuration dialog box, specify the parameters described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| Throttling Dimension | The dimension on which you want to enable throttling. Valid values: Bandwidth: the difference between the highest and lowest frequencies. QPS: the number of requests processed per second. |
| Task Type | The type of the throttling task. Valid values: Incremental Replication: enables throttling only for new data. Historical Replication: enables throttling for all data. Note This parameter is required only when OSS instances are protected. If other types of the instances are protected, you do not need to configure this parameter. |
| Throttling Value (bps) | The custom throttling threshold. |

O&M console of ASR for Geo-disa ster Recovery

##### 2.5.1.4 Delete an entity from a protection group

This topic describes how to delete an entity from a protection group.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, find the entity that you want to delete and click
**Delete** in the **Actions** column.
5. In the Delete Synchronization Entity message, click **OK**.

##### 2.5.1.5 View the logs of a synchronization entity

Logs are generated during disaster recovery drills or actual disaster recovery. This topic describes how to view the logs of a synchronization entity in a protection group.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, find the entity that you want to manage and click
**Logs** in the **Actions** column.
5. Click **OK** or **Cancel** to close the panel.

#### 2.5.2 Perform a site switchover drill

This topic describes how to associate disaster recovery plans with a switchover drill that simulates the scenario in which all devices at the primary site fail and all business needs to be switched over to the secondary site. During the switchover drill, the associated disaster recovery plans are executed.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Site Disaster Recovery**
**Drill**.
3. Associate one or more disaster recovery plans with the site switchover.
i. On the Site Switchover page, click **Bind Disaster Recovery Plan**. ii. In the Bind Disaster Recovery Plan dialog box, select one or more disaster recovery plans that you want to associate with the site switchover. O&M console of ASR for Geo-disa ster Recovery iii. Click **OK**. The associated disaster recovery plans are displayed on the **Site Switchover** page.
4. Set the execution order.
i. Move the pointer over the number in the Execution Sequence column of a plan and click the icon. ii. Enter an integer from 0 to 9 in the Execution Sequence field. A smaller value indicates a higher execution priority. The plans that have the same priority are executed at the same time. iii. Click **OK**.
5. Start the disaster recovery plans.
i. In the upper-right corner of the Site Switchover page, click **Start All Failovers**. ii. In the Start All Failovers message, click **OK**. iii. All plans start to be executed to switch business from the primary site to the secondary site. iv. After all plans are executed, the plans are ready to be executed for a failback. You can click **Start Failback** to switch business from the secondary site to the primary site. v. After all plans are executed for the failback, the business at the primary site works as expected.

**Related operations**

On the Site Switchover page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| View plan details | 1. Click the name of a plan to go to the plan details page. 2. View the details of the plan on the following tabs: On the Plan Steps tab, view the execution steps of the plan. On the Progress tab, view the failover progress. To terminate the failover, click Terminate. In the message that appears, confirm the task that you want to terminate and click Terminate Failover. If an exception occurs but the error does not affect the failover, click Force Pass. In the message that appears, click Force Pass. On the Associated Protection Group tab, view the protection groups that are associated with the plan and the instances in each protection group. On the Historical Records tab, view the overview of the switchover drill in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, Synchronization Latency Compliance Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. |

O&M console of ASR for Geo-disa ster Recovery

| View a failover summary | On the Historical Records tab of the plan details page, find a failover and click View Drill Summary in the Actions column. |
|---|---|
| Download a failover summary report | On the Historical Records tab of the plan details page, find a failover and click Download Report in the Actions column to save the failover report to your computer. |
| Disassociate one or more disaster recovery plans from the site switchover | Disassociate multiple disaster recovery plans at a time i. On the Site Switchover page, select the disaster recovery plans that you want to disassociate from the site switchover. ii. In the lower part of the page, click Unbind. iii. In the Start All Failovers message, click OK. Disassociate a single disaster recovery plan i. On the Site Switchover page, find the disaster recovery plan that you want to disassociate from the site switchover and click Unbind in the Actions column. ii. In the Unbind Independent Disaster Recovery message, click OK. |

#### 2.5.3 Perform a site failover

This topic describes how to associate disaster recovery plans with a site failover that is performed when all devices at the primary site fail and all business needs to be switched over to the secondary site. During the site failover, the associated disaster recovery plans are executed.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.

> **Note:** This operation does not support hybrid disaster recovery.

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Site Disaster Recovery**.
3. Associate one or more disaster recovery plans with the site failover.
i. On the Site Disaster Recovery page, click **Bind Disaster Recovery Plan**. ii. In the Bind Disaster Recovery Plan dialog box, select one or more disaster recovery plans that you want to associate with the site failover. iii. Click OK.
4. Set the execution order.
i. Move the pointer over the number in the Execution Sequence column of a plan and click the icon. O&M console of ASR for Geo-disa ster Recovery ii. Enter an integer from 0 to 9 in the Execution Sequence field. A smaller value indicates a higher execution priority. The plans that have the same priority are executed at the same time. iii. Click **OK**.
5. Start the disaster recovery plans.
i. In the upper-right corner of the Site Switchover page, click **Start All Failovers**. ii. In the Start All Failovers message, click **OK**. iii. All plans start to be executed to switch business from the primary site to the secondary site. iv. After all plans are executed, the plans are ready to be executed for a failback. You can click **Start Failback** to switch business from the secondary site to the primary site. v. After all plans are executed for the failback, the business at the primary site works as expected.

**Related operations**

On the Site Disaster Recovery page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| View plan details | 1. Click the name of a plan to go to the plan details page. 2. View the details of the plan on the following tabs: On the Plan Steps tab, view the execution steps of the plan. On the Progress tab, view the failover progress. To terminate the failover, click Terminate. In the message that appears, confirm the task that you want to terminate and click Terminate Failover. If an exception occurs but the error does not affect the failover, click Force Pass. In the message that appears, click Force Pass. On the Associated Protection Group tab, view the protection groups that are associated with the plan and the instances in each protection group. On the Historical Records tab, view the overview of the switchover drill in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, Synchronization Latency Compliance Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. |
| View a failover summary | On the Historical Records tab of the plan details page, find a failover and click View Drill Summary in the Actions column. |
| Download a failover summary report | On the Historical Records tab of the plan details page, find a failover and click Download Report in the Actions column to save the failover report to your computer. |

O&M console of ASR for Geo-disa ster Recovery

| Disassociate one or more disaster recovery plans from the site failover | Disassociate multiple disaster recovery plans at a time i. On the Site Disaster Recovery page, select the disaster recovery plans that you want to disassociate from the site failover. ii. In the lower part of the page, click Unbind. iii. In the Unbind Independent Disaster Recovery message, click OK. Disassociate a single disaster recovery plan i. On the Site Disaster Recovery page, find the disaster recovery plan that you want to disassociate from the site failover and click Unbind in the Actions column. ii. In the Unbind Independent Disaster Recovery message, click OK. |
|---|---|

#### 2.5.4 View the execution history of a site disaster recovery plan

**disaster recovery plan**

This topic describes how to view the steps, progress, associated protection groups, and historical execution records of a site disaster recovery plan.

**Prerequisites**

A site disaster recovery plan for a switchover drill or failover is created.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Plan Execution History**.
Each time a site disaster recovery plan is executed, a record is automatically generated on the **Plan Execution History** page. The records whose names start with AUTO_CREATE_REGION_PLAN are automatically generated by the system. View drill records. a. On the Plan Execution History page, click the **Disaster Recovery Drill Records** tab. b. Find the plan that you want to manage and click its name to go to the plan details page. c. View the plan details on the following tabs: **Plan Steps**, **Progress**, **Associated**
**Protection Group**, and **Historical Records**.

| Tab | Description |
|---|---|

O&M console of ASR for Geo-disa ster Recovery

| Plan Steps | This tab displays all steps that are performed when the plan is executed for failovers and failbacks. If the plan is in the Completed state, you can click Start Drill on the Plan Steps tab to execute the plan again. If the plan is a drill plan, you can click Change to Recovery Plan on the Plan Step tab and click OK in the message that appears to change the plan type. |
|---|---|
| Progress | a. This tab displays time consumption and detailed progress when the plan is executed for failovers and failbacks. Note To go to the Progress tab, you can also find the plan on the Disaster Recovery Drill Records tab and click Details in the Actions column. You can view the duration and detailed progress of the switchover /switchback of the plan. b. In the left-side Step section, you can view the time consumed for each step. To view the logs of each step, click View Logs. c. To view the progress details of a step, click the step in the left-side Step section. d. To view the substeps of a step, click the icon to the left of the step name. |
| Associated Protection Group | This tab displays the status of all protection groups associated with the plan and the number of instances in each protection group. |

O&M console of ASR for Geo-disa ster Recovery

| Historical Records | a. This tab displays the overview of the plan in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO-compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. b. To view the summary of a drill, find the drill in the drill list and click View Drill Summary in the Actions column. Note You can also find the drill on the Disaster Recovery Drill Records tab and click View Drill Summary in the Actions to go to the Summary page. In the Overview section, the information is displayed in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO- compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. In the Drill Conclusion section, you can view the drill conclusion specified in the Apsara Uni-manager Management Console. On the Failover Duration Rankings and Failback Duration Rankings tabs, the instances are displayed in descending order based on the time consumption. c. To download the report of a drill, find the drill in the drill list and click Download Report in the Actions column to save the report to your computer. You can download a report of a drill only after the plan is in the Completed state and the report is created in the Apsara Uni-manager Management Console. |
|---|---|

View disaster recovery records. a. On the Plan Execution History page, click the **Disaster Recovery Records** tab. b. Find the plan that you want to manage and click its name to go to the plan details page. O&M console of ASR for Geo-disa ster Recovery c. View the plan details on the following tabs: **Plan Steps**, **Progress**, **Associated**
**Protection Group**, and **Historical Records**.

| Tab | Description |
|---|---|
| Plan Steps | This tab displays all steps that are performed when the plan is executed for failovers and failbacks. If the plan is in the Completed state, you can click Start Drill on the Plan Steps tab to execute the plan again. To start a failover, click Start Failover. In the message that appears, click OK. |
| Progress | a. This tab displays time consumption and detailed progress when the plan is executed for failovers and failbacks. Note To go to the Progress tab, you can also find the plan on the Disaster Recovery Records tab and click Details in the Actions column. You can view the duration and detailed progress of the switchover /switchback of the plan. b. In the left-side Step section, you can view the time consumed for each step. To view the logs of each step, click View Logs. c. To view the progress details of a step, click the step in the left-side Step section. d. To view the substeps of a step, click the icon to the left of the step name. |
| Associated Protection Group | This tab displays the status of all protection groups associated with the plan and the number of instances in each protection group. |
| Historical Records | This tab displays disaster recovery records. |

### 2.6 Independent disaster recovery management

**management**

This topic describes how to create, view the details of, and delete an independent disaster recovery plan. O&M console of ASR for Geo-disa ster Recovery

#### 2.6.1 Create an independent disaster recovery plan

**recovery plan**

After an independent disaster recovery plan is created, you can perform failovers and switchover drills by using ASR for Geo-disaster Recovery (ASR-DR) only at the secondary site.

**Prerequisites**

ASR-DR is purchased and deployed at the primary site. The independent disaster recovery feature of ASR-DR is enabled for the primary and secondary sites.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. On the Independent Disaster Recovery page, click **Create Independent Disaster**
**Recovery**. In the Create Independent Disaster Recovery dialog box, specify the Disaster
Recovery Cloud and Disaster Recovery Region parameters.
4. Click **Create and Configure**. If you want to configure disaster recovery parameters later,
click **Create**.
5. Click **Verify** to verify the input values.
6. After the verification is passed, click **Create and Configure**. You can also click **Create**
and complete the configurations later.
7. After the configurations are complete, the independent disaster recovery plan is in the
**Configuration Completed** state. The following figure shows an example.
O&M console of ASR for Geo-disa ster Recovery

#### 2.6.2 Perform a failover

If a secondary site fails when the site is used to provide services, you can switch the business back to the primary site by using the independent disaster recovery feature. This topic describes how to perform a failover in the O&M console of ASR for Geo-disaster Recovery (ASR-DR). This topic also describes how to view the failover steps and progress.

**Background information**

When a site-level fault, such as network disconnection or power outage, occurs in your secondary site when the site provides services, you can switch the business back to the primary site by using the independent disaster recovery feature. This way, your business continuity is not affected.

**Prerequisites**

An independent disaster recovery plan is created and configured. For more information, see Create an independent disaster recovery plan.
1. Log on to the O&M console of ASR-DR at the secondary site.
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. Perform a failover by using one of the following methods:
Find the independent disaster recovery plan that you want to manage and click **Failover** in the **Actions** column. Find the independent disaster recovery plan that you want to manage and click **View**
**Details** in the **Actions** column. On the page that appears, click **Start Failover** in the
Failover section of the Switching Steps tab. O&M console of ASR for Geo-disa ster Recovery
4. After the failover is started, log on to the O&M console of ASR-DR from the primary site and
view the steps and progress of the failover. For more information, see View the details of an independent disaster recovery plan.

#### 2.6.3 Perform a switchover drill

If ASR for Geo-disaster Recovery (ASR-DR) is deployed on the secondary cloud and your business is switched over to run on the secondary cloud, the business cannot be switched back to the primary cloud when the secondary cloud fails. To resolve this issue, ASR-DR provides the independent disaster recovery feature. You can perform a switchover drill to increase the success rate of a failover.

**Background information**

When a site-level fault, such as network disconnection or power outage, occurs in your secondary site when the site provides services, you can switch the business back to the primary site by using the independent disaster recovery feature. This way, your business continuity is not affected.

**Prerequisites**

An independent disaster recovery plan is created. For more information, see Create an independent disaster recovery task.
1. Log in to the O&M console of ASR for Geo-disaster Recovery at the secondary site.
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. Perform a switchover drill by using one of the following methods:
Find the independent disaster recovery plan that you want to manage and click **Drill**
**Switchover** in the **Actions** column.
Find the independent disaster recovery plan that you want to manage and click **View**
**Details** in the **Actions** column. On the Independent Disaster Recovery Details page, click
**Start Drill Switchover** in the Drill Switchover section on the Switching Steps tab.
O&M console of ASR for Geo-disa ster Recovery
4. After the switchover drill is started, log on to the Apsara Uni-manager Operations Console
from the primary site and view the steps and progress of the switchover drill. For more information, see View the details of an independent disaster recovery plan.

#### 2.6.4 View the details of an independent disaster recovery plan

**disaster recovery plan**

You can view the steps and progress of failovers and switchover drills at the primary site.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. On the Independent Disaster Recovery page, view independent disaster recovery plans.
4. Find an independent disaster recovery plan and click **View Details** in the **Actions** column.
On the plan details page, view the basic information about the plan and the steps and progress of business switchovers.

#### 2.6.5 Disassociate configured nodes from an independent disaster recovery plan

**independent disaster recovery plan**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. On the Independent Disaster Recovery page, find the created independent disaster
recovery plan that you want to manage. O&M console of ASR for Geo-disa ster Recovery
4. Click **Unbind** in the **Actions** column. In the message that appears, click **OK**. After the
configured nodes are disassociated from the independent disaster recovery plan, you can reconfigure or delete the plan. You must disassociate configured nodes from an independent disaster recovery plan in ASR-DR at the secondary site.

#### 2.6.6 Delete an independent disaster recovery plan

**recovery plan**

You can delete only independent disaster recovery plans that are not configured. For example, you can delete an independent disaster recovery plan that is created but not configured or an independent disaster recovery plan from which the configured nodes are disassociated.
1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Independent Disaster Recovery**.
3. On the Independent Disaster Recovery page, find the created independent disaster
recovery plan that you want to manage.
4. Click **Delete** in the **Actions** column. In the message that appears, click **OK**.

### 2.7 Appendixes

#### 2.7.1 Look up a DNS address

This topic describes how to look up a Domain Name System (DNS) address.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. Enter dnsProduct in the search box and find the cluster in the **Products** list. Then, click
**Cluster Details** in the **Actions** column.
O&M console of ASR for Geo-disa ster Recovery
5. Click the **Desired State Configuration** tab and select the

```
 services/dnsService/user/dns.conf  file.
```

6. Click **Show Content**. The value of the AnycastVip field is the IP address of the DNS name
server, which is the same as the ServerIP value shown on the DNS management page.

> **Note:** The first two IP addresses in the internetIps field are the source IPs used by the DNS service to forward requests. In most cases, two IPs are bound to the bindServerRole containers.

#### 2.7.2 Configure DNS forwarding

When you set up a primary-secondary disaster recovery system between two clouds, you must configure Domain Name System (DNS) at the primary and secondary sites. Make sure that DNS queries can be smoothly forwarded across the system. This topic describes how to configure DNS forwarding.

**Important**

To configure DNS forwarding from opsDns to dnsProduct at the primary site, you must modify the tianji configuration file and roll update the tianji cluster. The risk of automated configuration is high. We recommend that you manually perform the configuration modification and roll update. Automate the configuration of other settings.

**Prerequisites**

O&M console of ASR for Geo-disa ster Recovery A network connection is established between the primary and secondary sites. The primary site is successfully deployed and the DNS configuration file is generated in the container.

> **Note:** If the prerequisites are not met, see the "Manually configure DNS forwarding" section in this topic.

**Automate configuration of DNS forwarding at the two sites**

1. Obtain the AccessKey ID (AK) and AccessKey secret (SK) and pop_ops_vip of the operations
administrator at the primary site. i. Log on to the Apsara Uni-manager Operations Console as an operations administrator. ii. Click in the upper-right corner of the page and then click **User Information**. iii. Obtain the AK and SK of the operations administrator. iv. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
v. On the **Product & Cluster O&M** page, enter webappAll in the search box to find the StandardCloudCluster cluster. vi. Click **Cluster Details** in the **Actions** column of the StandardCloudCluster cluster. On the cluster details page, click **Resource Details**. O&M console of ASR for Geo-disa ster Recovery vii. View the pop-vip-ops resource details and click the value in the Resource Application Result column to obtain and save the value of vip_ip.

> **Note:** If the pop-vip-ops of the primary site changes, you must roll update the asrdr cluster of the primary site again.

Run the following command in the ASR-DR container of the secondary site: Replace pop_vip_ops, ops_admin_ak, ops_admin_sk with the values obtained in the preceding steps. The DNS forwarding rules and IP address whitelists from the primary site to the secondary site are configured, and the DNS forwarding rules and IP address whitelists from the secondary site to the primary site are configured.

```
python alidata/bin/dns/auto_config_dns.py asrdr -v {pop_vip_ops} -a {ops_admin_ak} -s {ops_admin_sk}
```

viii. Obtain the content of the /home/admin/asrdr/config/dns/dns_conf.{regionId}.ops file of the local ASR-DR container.
2. Add a forwarding rule from OPS-DNS to DNS of the local cloud tenant.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
iii. On the **Product & Cluster O&M** page, enter tianji in the search box to search for the tianji cluster. iv. Click **Cluster Details** in the **Actions** column of the cluster. On the cluster details page, click **Desired State Configuration**. O&M console of ASR for Geo-disa ster Recovery v. Enter dns_zone.conf.jj2 in the search box on the left and click Show Content to add the dns_conf.{regionId}.ops content obtained in Step 1 to the file. Content format:

```
zone_forwarders:
  -zone: the Internet domain of the peer cloud
    forwarders:
    - the DNS nameserver address of the local cloud tenant
    - the DNS nameserver address of the local cloud tenant
  -zone: the intranet domain of the peer cloud
    forwarders:
    - the DNS nameserver address of the local cloud tenant
    - the DNS nameserver address of the local cloud tenant
```

vi. Click **Preview and Submit**. vii. Click **Cluster Rolling**. viii. After the tianji cluster is rolled, use one of the following methods for the tianji configuration to take effect: Enter the dnsslave container of ops1 and ops2 and execute the /root/opsbuild/deploy.py command. Before you execute the command, shut down the BGP process. Otherwise, the named service is restarted during the execution of the deploy.py script, which may result in a temporary unavailability of domain name resolution of the cloud platform. In most cases, the downtime lasts a few seconds and has a minimal impact. However, the deploy.py script may get stuck. We recommend that you shut down the BGP process before you execute the command. To stop the BGP process, execute the ps aux | grep bgp command to list all processes related to BGP and then execute the kill -9 command to stop the BGP process. Restart the DnsSlave# nodes one by one. (Make sure that each DnsSlave node restarts and reaches its final state before you proceed to the next node.) If the primary cloud is set up with dual data centers for zone-disaster recovery, you must configure forwarding rules in data center B. Then, perform the preceding steps for the tianji configuration to take effect.
3. Check the execution result.
i. Log on to the Apsara Uni-manager Operations console, choose **Security Management**
**> Network Security > Network Security Management Center**.
O&M console of ASR for Geo-disa ster Recovery ii. In the left-side navigation pane, choose **East-west Security Management > DNS**
**Rules**.
iii. Log on to the Apsara Uni-manager Management console and choose **Products >**
**Networking > Cloud Network > Alibaba Cloud DNS**.
iv. On the **DNS within Cloud** page, click the **Global Forwarding Configuration** tab. v. The tianji cluster is rolled and the dns_zone.conf.jj2 file is fixed.

**Manually configure DNS forwarding**

1. Copy the DNS configuration file named dns_conf.{des_region} in the
/home/admin/asrdr/config/dns/ directory at the primary site to the /home/admin/asrdr/config/dns/ directory on the ASR-DR container at the secondary site. (If ASR-DR is not deployed at the primary site, place the configuration file in the specified directory based on the predefined format and naming convention.)
2. Run the following command in the ASR-DR container of the secondary site:

```bash
python /alidata/bin/dns/auto_config_dns.py manual -r des_region
# The des_region parameter specifies the destination region.
```

The operation is performed in the ASR-DR container of the secondary site. Only the DNS forwarding rules and IP address whitelists from the secondary site to the primary site are configured. O&M console of ASR for Geo-disa ster Recovery
3. Obtain the content in the /home/admin/asrdr/config/dns/dns_conf.{regionId}.ops file of the
local ASR-DR.
4. Repeat the preceding steps in the ASR-DR container of the primary site.
5. Add a forwarding rule from OPS-DNS to DNS of the local cloud tenant.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. On the **Product & Cluster O&M** page, enter tianji in the search box to search for the tianji cluster. iv. Click **Cluster Details** in the **Actions** column of the cluster. On the cluster details page, click **Desired State Configuration**. v. Enter dns_zone.conf.jj2 in the search box on the left and click Show Content to add the dns_conf.{regionId}.ops content obtained in Step 3 to the file. Content format:

```
zone_forwarders:
  -zone: the Internet domain of the peer cloud
    forwarders:
    - the DNS nameserver address of the local cloud tenant
    - the DNS nameserver address of the local cloud tenant
  -zone: the intranet domain of the peer cloud
    forwarders:
    - the DNS nameserver address of the local cloud tenant
    - the DNS nameserver address of the local cloud tenant
```

O&M console of ASR for Geo-disa ster Recovery vi. Click **Preview and Submit**. vii. Click **Cluster Rolling**. viii. After the tianji cluster is rolled, use one of the following methods for the tianji configuration to take effect: Enter the dnsslave container of ops1 and ops2 and execute the /root/opsbuild/deploy.py command. Before you execute the command, shut down the BGP process. Otherwise, the named service is restarted during the execution of the deploy.py script, which may result in a temporary unavailability of domain name resolution of the cloud platform. In most cases, the downtime lasts a few seconds and has a minimal impact. However, the deploy.py script may get stuck. We recommend that you shut down the BGP process before you execute the command. To stop the BGP process, execute the ps aux | grep bgp command to list all processes related to BGP and then execute the kill -9 command to stop the BGP process. Restart the DnsSlave# nodes one by one. (Make sure that each DnsSlave node restarts and reaches its final state before you proceed to the next node.) If the primary cloud is set up with dual data centers for zone-disaster recovery, you must configure forwarding rules in data center B. Then, perform the preceding steps for the tianji configuration to take effect.
6. Check the execution result.
i. Log on to the Apsara Uni-manager Operations console, choose **Security Management**
**> Network Security > Network Security Management Center**.
ii. In the left-side navigation pane, choose **East-west Security Management > DNS**
**Rules**.
iii. Log on to the Apsara Uni-manager Management console and choose **Products >**
**Networking > Cloud Network > Alibaba Cloud DNS**.
iv. On the **DNS within Cloud** page, click the **Global Forwarding Configuration** tab. O&M console of ASR for Geo-disa ster Recovery v. The tianji cluster is rolled and the dns_zone.conf.jj2 file is fixed.

#### 2.7.3 Configure DTS parameters

If you configure a primary/secondary disaster recovery solution between two clouds, you must configure Data Transmission Service (DTS) for database products. This topic describes how to configure DTS.

**Prerequisites**

A network connection is established between the primary and secondary sites. ASR for Geo-disaster Recovery (ASR-DR) is deployed at the primary site and a DTS SQL template file is generated in the container. If the prerequisites are not met, manually configure local DTS.

**Automatically configure local DTS**

1. Obtain the AccessKey ID (AK) and AccessKey secret (SK) and pop_ops_vip of the operations
administrator at the primary site. i. Log on to the Apsara Uni-manager Operations Console as an operations administrator. ii. Click in the upper-right corner of the page and then click **User Information**. iii. Obtain the AK and SK of the operations administrator. iv. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
v. On the **Product & Cluster O&M** page, enter webappAll in the search box to find the StandardCloudCluster cluster. O&M console of ASR for Geo-disa ster Recovery vi. Click **Cluster Details** in the **Actions** column of the StandardCloudCluster cluster. On the cluster details page, click **Resource Details**. vii. View the ops resource details, click the value in the Resource Application Result column, and then save the value of vip_ip.
2. Log on to the ASR-DR container of the secondary site. For more information, see Log on to a
container.
3. Run the following command in the ASR-DR container of the secondary site:

```
python alidata/bin/dts/dts_new/auto_config_dts.py asrdr -v {pop_ops_vip} -a {ops_admin_ak} -s {ops_admin_sk}
```

Replace the pop_ops_vip, ops_admin_ak, and ops_admin_sk parameters with the values obtained from the preceding steps. After the script is executed, relevant information about the primary site is inserted into the DTS database at the secondary site.
4. Run the following commands in the DTS database at the secondary site to view information
about the DTS database:

```
select * from region_pattern where pattern_expression = '^Region ID'\G select * from config where config_code = 'cross_cloud_internet_check_flag';
```

O&M console of ASR for Geo-disa ster Recovery

```
select * from region_list where REGIONS like '%Region ID%'\G select * from dts_region_info where region = 'Region ID'\G
```

**Manually configure local DTS**

> **Note:** If the ASR-DR container at the secondary site cannot access the VIP for asrdr-backend-ops applied for by the asrdr-backend at the primary site, we recommend that you manually configure local DTS.

O&M console of ASR for Geo-disa ster Recovery
1. Copy the DTS SQL template /home/admin/asrdr/config/dts/dts_conf.{des_region} from the
asrdr container at the primary site to the /home/admin/asrdr/config/dts/ directory in the asrdr container at the secondary site.
2. Run the following command in the ASR-DR container of the secondary site:

```bash
python alidata/bin/dts/dts_new/auto_config_dts.py manual -r {des_region}
# The des_region parameter specifies the destination region.
```

When the script is executed, {current_region} is automatically replaced. During the execution, the SQL statements that are executed are returned.
3. Run the following commands in the DTS database at the secondary site to view information
about the DTS database:

```
select * from region_pattern where pattern_expression = '^Region ID'\G select * from config where config_code = 'cross_cloud_internet_check_flag'; select * from region_list where REGIONS like '%Region ID%'\G
```

O&M console of ASR for Geo-disa ster Recovery

```
select * from dts_region_info where region = 'Region ID'\G
```
