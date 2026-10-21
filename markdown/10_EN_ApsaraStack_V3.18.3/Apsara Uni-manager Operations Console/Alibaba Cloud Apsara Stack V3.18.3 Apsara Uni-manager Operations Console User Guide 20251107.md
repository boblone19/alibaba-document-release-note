---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console User Guide 20251107"
product_version: "V3.18.3"
doc_version: "20251107"
pdf_pages: 362
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console User Guide 20251107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Uni-manager%20Operations%20Console%20User%20Guide%2020251107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console User Guide 20251107

## Table of Contents

- 1 Overview
- 2 Get started
  - 2.1 Prepare an operations account
  - 2.2 Log on to the Apsara Uni-manager Operations Console
  - 2.3 Top navigation bar
  - 2.4 Operation platform
- 3 Getting Started
  - 3.1 Overview
  - 3.2 System administrator
    - 3.2.1 Alert management
    - 3.2.2 Inspection management
    - 3.2.3 Archiving management
  - 3.3 Security administrator
    - 3.3.1 Logon management
  - 3.4 Security auditor
    - 3.4.1 Operation log auditing
  - 3.5 Role administrator
    - 3.5.1 User management
- 4 General O&M
  - 4.1 Monitoring management
    - 4.1.1 Cloud platform monitoring
      - 4.1.1.1 Business monitoring for cloud services
        - 4.1.1.1.1 View the monitoring information of cloud services
        - 4.1.1.1.2 Configure business metrics for cloud service monitoring
        - 4.1.1.1.3 Configure alert rules
        - 4.1.1.1.4 Alert history
      - 4.1.1.2 Data dashboard
        - 4.1.1.2.1 View data on the read and write dashboard
        - 4.1.1.2.2 Customize a dashboard
        - 4.1.1.2.3 Configure a data source for dashboards
  - 4.2 Alerts
    - 4.2.1 Alert overview
    - 4.2.2 Alerts
    - 4.2.3 Alert settings
      - 4.2.3.1 Policy management
      - 4.2.3.2 Alert templates
      - 4.2.3.3 Alert notification
      - 4.2.3.4 Alert masking
      - 4.2.3.5 Masked alerts
      - 4.2.3.6 Alert rule settings
  - 4.3 Inspections
    - 4.3.1 All inspections
    - 4.3.2 Inspection dashboard
    - 4.3.3 Inspection scenarios
    - 4.3.4 Inspection records
    - 4.3.5 Inspection notifications
  - 4.4 Event Center
    - 4.4.1 Event list
    - 4.4.2 Event Grading
    - 4.4.3 My events
    - 4.4.4 Event Chart
    - 4.4.5 Configuration Management
- 5 Platform O&M
  - 5.1 Apsara Infrastructure Management
    - 5.1.1 Resource management
      - 5.1.1.1 Product & Cluster O&M
        - 5.1.1.1.1 Cluster details
        - 5.1.1.1.2 Component details
      - 5.1.1.2 Machine management
        - 5.1.1.2.1 Machine details
      - 5.1.1.3 Resource tags
      - 5.1.1.4 Base machine resource dashboard
    - 5.1.2 Platform blueprint
      - 5.1.2.1 Product topology
      - 5.1.2.2 Hardware topology
    - 5.1.3 Kubernetes cluster management
      - 5.1.3.1 Cluster overview
      - 5.1.3.2 Node management
    - 5.1.4 Hardware O&M
      - 5.1.4.1 HDD repairs
        - 5.1.4.1.1 Preparation
        - 5.1.4.1.2 Repair
        - 5.1.4.1.3 Repair history
      - 5.1.4.2 Machine repairs
    - 5.1.5 O&M tools
      - 5.1.5.1 Task management
      - 5.1.5.2 Service management
      - 5.1.5.3 VM dashboard
      - 5.1.5.4 Dashboard of service registration variables
      - 5.1.5.5 Resource dashboard
      - 5.1.5.6 Basic service monitoring
    - 5.1.6 Web clients
      - 5.1.6.1 Web Client Logon
        - 5.1.6.1.1 Server logon
        - 5.1.6.1.2 Database logon
        - 5.1.6.1.3 vSwitch logon
      - 5.1.6.2 Account authorization
      - 5.1.6.3 Command management
      - 5.1.6.4 Operation records
  - 5.2 O&M of management services
  - 5.3 Capacity management
    - 5.3.1 Capacity Overview
    - 5.3.2 Computing capacity
      - 5.3.2.1 ECS
    - 5.3.3 Network capacity
      - 5.3.3.1 SLB
    - 5.3.4 Storage capacity
      - 5.3.4.1 EBS
      - 5.3.4.2 OSS
      - 5.3.4.3 Tablestore
      - 5.3.4.4 Simple Log Service
      - 5.3.4.5 NAS
      - 5.3.4.6 CPFS file system
      - 5.3.4.7 APFS file system
    - 5.3.5 Base capacity
      - 5.3.5.1 Apsara Infrastructure Management Storage Capacity
      - 5.3.5.2 Docker host capacity of Apsara Infrastructure Management
    - 5.3.6 Database capacity
      - 5.3.6.1 RDS
      - 5.3.6.2 ApsaraDB RDS for PostgreSQL
      - 5.3.6.3 Redis
      - 5.3.6.4 MongoDB
      - 5.3.6.5 AnalyticDB for PostgreSQL
      - 5.3.6.6 PolarDB for PostgreSQL
      - 5.3.6.7 PolarDB-X
      - 5.3.6.8 OceanBase
    - 5.3.7 Middleware capacity
      - 5.3.7.1 ApsaraMQ for Kafka
  - 5.4 O&M change
    - 5.4.1 Log cleanup
      - 5.4.1.1 Rule management
      - 5.4.1.2 Plans
      - 5.4.1.3 Records
    - 5.4.2 Plan management
      - 5.4.2.1 Base plans
        - 5.4.2.1.1 Workflow types
        - 5.4.2.1.2 Link types
          - 5.4.2.1.2.1 VM transfer
          - 5.4.2.1.2.2 Docker host switchover
          - 5.4.2.1.2.3 NC scale-in
          - 5.4.2.1.2.4 NC scale-out
          - 5.4.2.1.2.5 Docker host scale-in
          - 5.4.2.1.2.6 Docker host scale-out
          - 5.4.2.1.2.7 Cluster startup and shutdown
    - 5.4.3 Process approval
      - 5.4.3.1 My submission
      - 5.4.3.2 My approval
    - 5.4.4 Version management
      - 5.4.4.1 Package management
      - 5.4.4.2 Product version management
  - 5.5 Disaster recovery management
  - 5.6 Log center
    - 5.6.1 Log map
    - 5.6.2 Log query
    - 5.6.3 Log Dump
    - 5.6.4 Log monitoring
- 6 Product O&M
- 7 Security management
  - 7.1 Security audit
    - 7.1.1 Operation audit
      - 7.1.1.1 Console-based Audit
      - 7.1.1.2 CLI-based Audit
  - 7.2 Security operations
  - 7.3 Host security
    - 7.3.1 Container image management
  - 7.4 Network security
    - 7.4.1 Network Security Management Center
      - 7.4.1.1 East-west security management
        - 7.4.1.1.1 Policy center
          - 7.4.1.1.1.1 Policy content management
          - 7.4.1.1.1.2 Platform VIP security protection
        - 7.4.1.1.2 DNS rules
        - 7.4.1.1.3 Device network access management
  - 7.5 Account security
    - 7.5.1 Linux account management
      - 7.5.1.1 Password management for root users
      - 7.5.1.2 SSH key management
      - 7.5.1.3 System user management
      - 7.5.1.4 Linux account management task
        - 7.5.1.4.1 Task template management
        - 7.5.1.4.2 Task execution records
    - 7.5.2 Account management for cloud services
      - 7.5.2.1 Account ACL control
      - 7.5.2.2 Service boundary
        - 7.5.2.2.1 ACL
  - 7.6 Access control
    - 7.6.1 Security policies
    - 7.6.2 Logon policies
    - 7.6.3 Two-factor authentication
- 8 System settings
  - 8.1 Custom settings
  - 8.2 Authorization Information
  - 8.3 Notification management
    - 8.3.1 Channel management
    - 8.3.2 Push history
  - 8.4 Region coordinate management
  - 8.5 Archiving management
    - 8.5.1 Archiving settings
    - 8.5.2 Archiving details
    - 8.5.3 Management of archived products
    - 8.5.4 Archive server settings
- 9 User permissions
  - 9.1 User management
  - 9.2 User group management
  - 9.3 Role management
  - 9.4 Department management
  - 9.5 Department-region association
  - 9.6 Menu settings
- 10 Emergency response
  - 10.1 Watchdog monitoring and alerting
  - 10.2 Scenario diagnostics
  - 10.3 Emergency plan
  - 10.4 Emergency web terminal
    - 10.4.1 Server logon
    - 10.4.2 Database logon

## 1 Overview

This topic describes the management framework of the Apsara Uni-manager Operations Console.

**Management framework of the Apsara Uni-manager Operations**

Alibaba Cloud Apsara Stack adopts the ISO 20000 standard and references the methods regulated by the Information Technology Service Standards (ITSS) and ITIL frameworks to build the management framework of the Apsara Uni-manager Operations Console. The following figure shows the management framework of the Apsara Uni-manager Operations Console. Figure 1. Apsara Uni-manager Operations Console Based on ITIL and ISO 20000, the management framework of the Apsara Uni-manager Operations Console uses management support tools to adapt to various management modes in a process-oriented, normalized, and standardized manner. This has implemented the systematic management of the overall process of operations services The management framework of the Apsara Uni-manager Operations Console provides the full lifecycle management methods, management standards, management modes, management supporting tools, management objects, and process-based management methods of IT operations services. The Apsara Uni-manager Operations Console defines various entities involved in operations activities and relationships between these entities. Relevant entities are well organized and coordinated based on the Apsara Uni-manager Operations Console and can provide different levels of operations services based on the service agreements.

**Apsara Uni-manager Operations Console**

The Apsara Uni-manager Operations Console is a unified and intelligent O&M platform. In accordance with the Information Technology Infrastructure Library (ITIL) and IT Service Management (ITSM) standards, the operations processes and requirements must be abstract, and automation is implemented by using intelligent operations tools. For customized operations, interfaces and multi-level approval must be used to reduce risks. In the Apsara Uni-manager Operations Console, cloud operations is classified into the following layers: infrastructure, cloud service, and business operations. Based on the operations experience and data accumulated and collected from three layers, Alibaba Cloud Apsara Stack aggregates data collected by the operations platform to the Configuration Management Database (CMDB) of the platform. The Apsara Uni-manager Operations Console consolidates, analyzes, and comprehensively processes the data and integrates rich practical experience and operations capabilities to the platform operations tools. The Apsara Uni-manager Operations Console is designed to be desired state-oriented and uses unified operations tools for the fault discovery and tracking, link display, ITIL process, and self-repaired faults of the platform to realize the ultimate goal of artificial intelligence for IT operations (AIOps). The Apsara Uni-manager Operations Console provides a centralized operations portal that allows you to have a consistent operations experience. The Apsara Uni-manager Operations Console supports interconnections with third-party platforms and provides centralized API operations capabilities to deliver data to third-party systems by using APIs. The Apsara Uni-manager Operations Console performs centralized operations management, such as automated deployments, upgrades, changes, and configurations, on physical devices, operating systems, computing resources, network, storage, databases, middleware, and business applications in the cloud computing environment. The Apsara Uni-manager Operations Console also provides the features of alert monitoring and automatic analysis, diagnosis, and troubleshooting for faults, performance, and configurations. By analyzing, processing, and evaluating the running status and quality of cloud platforms, the Apsara Unimanager Operations Console guarantees the continuous and stable running of cloud computing business applications and provides services and support for O&M processes to build an improved operations service management platform.

**O&M support services**

In addition to tools, process assurance and personnel management are essential to ensure the integrity of operations. Apsara Stack provides on-site development supporting services for major problems, on-site services, expert escort services, business consulting services, and business optimization services. Apsara Stack provides the first-line, second-line, and third-line supporting systems to support platform problems of customers and provides upgrade channels to support urgent problems of customers. As an autonomous and controllable platform, the Apsara Uni-manager Operations Console ensures that technical problems can be effectively solved in a timely manner.

## 2 Get started

### 2.1 Prepare an operations account

Before you perform O&M operations in the Apsara Uni-manager Operations Console, make sure that you have obtained an operations account that has the necessary permissions to perform O&M operations from the role administrator.
1. The role administrator logs on to the Apsara Uni-manager Operations Console.
2. The role administrator creates a role to be assigned to the operations account. For more
information about how to create a role, see Role management.
3. The role administrator creates a department to be assigned to the operations account. For
more information about how to create a department, see Department management.
4. The role administrator creates an operations account and assigns the created role to the
account. For more information, see User management.

> **Note:** If the role administrator wants to perform a more fine-grained permission control on the operations role, the role administrator can create a basic role as specified in **OAM**, grant specific permissions to the role, and then assign the role to the corresponding operations account.

### 2.2 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how users such as O&M engineers log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment personnel or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.

### 2.3 Top navigation bar

This topic describes the features that are provided by the top navigation bar of the Apsara Uni-manager Operations Console. The following table describes the features that are provided by the top navigation bar of the Apsara Uni-manager Operations Console.

| No. | Section | Description |
|---|---|---|
| (1) | Region selector | Select a region from the drop-down list to switch to the region. This section helps you manage all regions in a centralized manner. |
| (2) | Top navigation bar | Move the pointer over or click a feature for more options. |
| (3) | Language | Click to switch the language. Simplified Chinese, traditional Chinese, and English are supported. |
| (4) | Color display mode | Click to set the color mode to light mode or dark mode. |
| (5) | Help center | Click to view online documentation. |
| (6) | Message center | Click to view the approval notifications and alert notifications that are not handled on the Approval Messages and Alert Messages tabs. |
| (7) | User center | Click to modify personal information, view version information, or log off from the current account. |

### 2.4 Operation platform

This topic describes the features that the operation platform of the Apsara Uni-manager Operations Console offers for users with different permissions in single- or multi-region scenarios.

**Operation platform in single-region scenarios**

The following table describes the sections available on the operation platform of a regular user in single-region scenarios.

| Section | Description |
|---|---|
| Global Search | You can globally search for information such as products, clusters, Elastic Compute Service (ECS) resources, machines, network resources, and documentation. Displays the menu pages that you recently accessed. |
| My favorite | Displays the features in the top navigation bar that you added as favorites. If you want to update a feature in or add a feature to the favorite, perform operations in the top navigation bar. Only the newly added six navigation menus are supported. |
| Product Desired State | Displays the total number of products, the number of products that are at desired state, and the number of products that are not at desired state. |
| Services Not Reached Final State | Displays the products that are not at desired state. You can click View More in this section to go to the Product & Cluster O&M page. |

| Asset Data | Displays the numbers of racks, servers, and network devices. |
|---|---|
| Event Overview | Displays the number of events at each level in the last week. |
| Alert Overview | Displays the number of pending alerts at each level and the total number of alerts in the last week. |
| Inspection Overview | Displays the total number of inspection results and the numbers of inspection errors, inspection warnings, and passed inspection results in the last week. |
| BMS Asset Overview | Displays the data related to Bare-metal Management Service (BMS). Instances Running in Resource Pool: the bare metal instances that are managed in the resource pool and in the Running state. This data is the same as the data of the Total Instances in Resource Pool parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console. Applied Instances: all instances that are applied by users on the tenant side. The instances cannot be filtered by state. This data is the same as the data of the Total Applied Instances parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console only when the organization type is root. Running Instances: the applied instances that are in the Running state. This data is the same as the data of the Total Running Instances on the Overview page of the BMS console in the Apsara Uni-manager Management Console only when the organization type is root. Images: the total number of custom images and public images in the selected region. In multi-region scenarios, only when you select multiple same regions, the data is the same as the data of the Total Mirrors parameter on the Overview page of the BMS console in the Apsara Uni- manager Management Console. In single-region scenarios, the data is the same as the data of the Total Mirrors parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console. |
| To be handled | Displays the content and submission time of the workflows that require your approval. You can click View More in this section to go to the Pending Approval page. |
| Cloud Service Capacity | Displays the status of the clusters with capacity alerts. You can clickV iew More in this section to go to the Capacity Overview page. |
| One cloud multi- core server distribution | Displays the distribution of physical servers by CPU and the total number of physical servers. |
| Cloud product server distribution TOP10 | Displays the distribution of top 10 cloud product servers by CPU on the tenant side. You can click View More in this section to go to the Cloud product server distribution panel. |

**Operation platform of a manager**

The following table describes the sections available on the operation platform of a manager who has the permissions of the **platform O&M administrator**.

| Section | Description |
|---|---|
| Abnormal Product | Displays the number of abnormal products and the total number of products, and lists all abnormal products. In the middle part of the operation platform, view the status and distribution of each cloud product. A color of red indicates that the product is abnormal, and a color of gray indicates that the product is normal. Click the name of a product on the left side of the operation platform or in the O&M view in the middle part of the operation platform to view the status of the product, the numbers of critical alerts and major alerts, and the impact on other products. |
| Alert | Displays the numbers of critical alerts and major alerts and the trends of the alerts in the last week. |
| Capacity | Product Statistics: displays the number of products, the number of products for which no capacity alerts are generated, and the number of products with capacity alerts. Early Warning Cluster: displays the status of the clusters with capacity alerts. |
| Assets | Displays the numbers of racks, servers, and network devices. |

| Security Risk | Platform Risk Index: displays the statistics of global risk indicators based on threat events and at-risk assets within an organization. Asset Risk Index: displays the distribution of assets at the high-risk, medium- risk, low-risk, and risk-free levels. Threat event Statistics: displays the distribution and statistics of threat events at the critical, major, suspicious, moderate, and information levels. |
|---|---|

**Operation platform in multi-region scenarios**

Operation platform for international deployments The following table describes the sections available on the operation platform for international deployments in multi-region scenarios.

| Tab | Section | Description |
|---|---|---|
| Multi-region View | Alert Overview | Displays the number of regions in which P1 alerts are generated, the total number of regions, the total number of P1 alerts, and the number of P1 alerts in each region. |
|   | Resource Overview | Displays the total numbers of racks, servers, and network devices, and the numbers of racks, servers, and network devices in each region. |
|   | > Document Version: 2025110 |   |

| sara Uni-manager O nsole |   |   |
|---|---|---|
|   | Quotas and Usage | Displays the capacity and usage of products in all regions or in each region. The data in this section can be filtered by configuring the Product Name parameter. |
| Current-region View |   | Displays the overview data in the current region. For more information, see the Operation platform in single-region scenarios section of this topic. |

Operation platform for non-international deployments The following table describes the sections available on the operation platform for noninternational deployments in multi-region scenarios.

| Tab | Section | Description |
|---|---|---|
|   | Alert Overview | Displays the number of regions in which no alerts are generated, the number of regions in which major alerts are generated, and the total number of major alerts. You can click Details next to data in this section to view the details. |

| sara Uni-manager O nsole |   |   |
|---|---|---|
| Multi-region View |   |   |
|   | Resource Overview | Displays the total numbers of racks, servers, and network devices, and the numbers of racks, servers, and network devices in each region. |
|   | Quotas and Usage | Displays the capacity and usage of products in all regions or in each region. The data in this section can be filtered by configuring the Product Name parameter. |
| Current-region View |   | Displays the overview data in the current region. For more information, see the Operation platform in single-region scenarios section of this topic. |

## 3 Getting Started

### 3.1 Overview

This topic describes the preset roles in the Apsara Uni-manager Operations Console and the common operations of the roles.

**User roles and corresponding permissions**

User roles provide different operation permissions for different users. By default, the system creates system administrators, security administrators, security auditors, and role administrators during initialization. The following table describes the permissions of roles.

| Role | Permissions |
|---|---|
| System administrator | Manages O&M operations across the platform. The O&M operations include monitoring and alerting, platform O&M, and service O&M. |
| Security administrator | Manages security-related O&M operations across the platform, such as security management. |
| Security auditor | Audits, tracks, and analyzes security-related O&M operations across the platform. |
| Role administrator | Manages user permissions across the platform. |

**View user roles**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the upper-right corner of the page, click the profile picture and click **Personal**
**information**.
3. View the information about the roles of the user displayed in the **Role Information**
section.

### 3.2 System administrator

This topic describes common O&M operations performed by system administrators, including alert management and inspection management across the platform.

#### 3.2.1 Alert management

This topic describes how to manage alerts in the Apsara Uni-manager Operations Console.

**Description**

Alerts are triggered if exceptions or faults occur in cloud infrastructure or cloud platform software, or collected monitoring data matches alert rules. Alert sources include monitored cloud services, the monitoring system, and objects that are monitored by the monitoring system.

**Prerequisites**

You have obtained the permissions of a system administrator.
1. The system triggers alerts if collected monitoring data matches alert rules. The alert
information varies based on the alert rule configuration.
2. Log on to the Apsara Uni-manager Operations Console.
3. In the top navigation bar, choose **Monitor&Alarms** > **Alerts** > **Alert Overview**.
On the Alert Overview page, view alert information based on your business requirements, which is analyzed and categorized from the following five perspectives:

| Section | View alert overview information |
|---|---|
| Alerts for Regions | Displays the number and levels of alerts in different regions. The colors displayed on the ring chart indicate different alert levels. A larger area on the ring chart indicates more alerts of the same level. |
| Alert Source | Displays the status of different alert sources. The blue color indicates that the alert source is normal, and the orange color indicates that the alert source is abnormal. |
| Alert Trend | Displays the total number of alerts today and yesterday. Displays the number of alerts generated within the previous seven days and the number of alerts at different levels. |
| Alert Distribution | Displays the number and levels of alerts for different services on the Active P1 Alerts, Full Active Alerts, and Full Alert History tabs. |
| Pending P1 Alerts | Displays the cloud platforms that have pending P1 alerts and the number of corresponding alerts. You can click a category tab to view the services that have pending P1 alerts under the category. |

4. Obtain the information about alerts based on your business requirements.

| Category | Obtain the details of an alert |
|---|---|
| Regional alert | i. In the left-side navigation pane, click Alerts. ii. Click Advanced Filter. Select an alert level from theA lert Level drop-down list to view the corresponding alerts. |
| Alert source | i. In the left-side navigation pane, click Alerts. ii. Click Advanced Filter. Select an alert source from theA lert Source drop-down list to view the corresponding alerts. |

| Alert trend | i. In the left-side navigation pane, click Alerts. ii. Click Advanced Filter. Select a time range from the Alarm start time drop-down list to view the corresponding alerts. |
|---|---|
| Alert distribution | i. On the Alert Overview page, click the Active P1 Alerts, Full Active Alerts, or Full Alert History tab. ii. Click a colored area with a number that corresponds to a service and time range. Then, you are navigated to the Alerts page that displays the corresponding alerts. |
| Pending P1 alert | i. On the Alert Overview page, find the Pending P1 Alerts section and click a category tab. ii. Click a service. Then, you are navigated to the Alerts page that displays the corresponding alerts. |

> **Note:** On the **Alerts** page, you can filter alerts by one of the preceding categories. You can also filter alerts by alert ID or alert status, or by multiple filter conditions.

5. Query the details of an alert.
On the **Alerts** page, you can query the basic information about alerts including **Alert**
**Level**, **Alert Item ID**, **Resource attribution**, **Alert Information**, **Alert Status**, **Alert**
**start time**, **Last alarm time/duration**, **Alerts**, **Extended Attributes**, **Alert Object**,
**Object Type**, and **Alert Source**.
Click the **ID** of an alert to obtain the details of the alert. In the **Basic Information** section, view the basic information about the alert. In the **Extended Information** section, view the extended information about the alert.

> **Note:** Move the pointer over **Details** next to **Alert Details**. The details of the alert are displayed.

In the **State timing diagram** section, view the alert metrics in a chart.
**1 Day**: shows the alert metrics of the day before the alert is triggered.
**1 Week**: shows the alert metrics of the week before the alert is triggered.
In the **Alert Impact** section, view the impacts of the alert. You can view the service roles that may be affected and the corresponding status. In addition, the services, clusters, services, and physical machines to which the service roles belong are displayed.
6. Obtain the solution to the alert based on the related reference and clear the alert.
7. After the alert is cleared, return to the **Alerts** page.
8. Filter the alert by performing the operations in Step 4. If the alert is in the **Close** state, the
alert is handled.

#### 3.2.2 Inspection management

This topic describes how to perform inspections in the Apsara Uni-manager Operations Console.

**Description**

In the Apsara Uni-manager Operations Console, you can perform quick inspections in various inspection scenarios. This helps you maintain the health of your business system and cloud services.

**Prerequisites**

You have obtained the permissions of a system administrator.
1. Log on to the Apsara Uni-manager Operations Console.
2. (Optional) Create a custom inspection scenario.
i. In the top navigation bar, choose **Monitor&Alarms** > **Inspections** > **Inspection**
**Settings**.
ii. On the **Inspection scenario** tab, click **Create a new inspection scenario**. iii. Specify the parameters described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Scene name | Enter a name for the custom inspection scenario. |
| Scenario description | Enter a description for the custom inspection scenario. |
| Configure inspection items | Select inspection items for the custom inspection scenario. After you select inspection items, the details of the inspection items are displayed in the lower part. |

iv. Return to the **Inspection scenario** tab. If the inspection scenario is displayed in the list, the inspection scenario is created.
3. In the top navigation bar, choose **Monitor&Alarms** > **Inspections** > **All Inspections**.
4. After you select an inspection scenario, click **Immediate inspection**. If you want to receive
inspection notifications, click Configuration next to Email notification on the Inspection notice page. Then, click **Execute** to trigger an inspection. You can configure multiple email addresses. Separate email addresses with semicolons (;). If you are prompted that notifications cannot be sent because notification channels are not configured, you can configure a notification channel on the
**Inspection notice**page. If you do not want to receive notifications, you can
directly click **Execute**to trigger an inspection.
5. Wait for the inspection to complete. The progress is displayed on the page. After the
inspection is complete, view the inspection results. In the upper part of the page, view basic information such as **Inspection scenario**,
**Start execution**, **End Execution**, **Initiator**, **Execution Policy**, and **Result**
**suggestion**.
In the **Inspection overview** section, you can view the inspection pass rate, number of inspected items, number of failed items, number of errors, number of warnings, and number of passed items. Click the data that corresponds to an inspection state to view the detailed inspection results of that state. In the **Overview of inspection results completed** section, you can view the inspection results of each inspected service, including the number of errors, number of warnings, and number of passed items. You can click a service to view its inspection result in detail. In the lower part of the page, you can click **Advanced Filter** to view inspection results by **Inspection item type**, **Inspection Status**, **Inspection item name**, and **Inspection**
**item description**.
You can move the pointer over **Inspection parameters** in the **Operation** column that corresponds to an inspection item to view its inspection parameters. You can move the pointer over **Inspection content** in the **Operation** column that corresponds to an inspection item to view its inspection content. You can click a number in the **Inspection results** column that corresponds to an inspection item to view the result in detail in the dialog box that appears. You can click **View report receiving mailbox** in the upper-right corner to view the email address that receives the inspection report. You can click **Export Report** in the upper-right corner to download the inspection report to your on-premises computer.

> **Note:** You can export the inspection report in the JSON format or as an Excel table.

#### 3.2.3 Archiving management

This topic describes how to archive and manage the data of various services in Apsara Distributed File System to ensure the availability of cloud platforms.

**Description**

You can use this module to archive the key metadata of Apsara Stack. The archived metadata is mainly used for quick recovery from Apsara Stack failures.

**Prerequisites**

You have obtained the permissions of a system configuration administrator for the Apsara Uni-manager Operations Console. Only the metadata of Apsara Distributed File System and OPS DNS can be archived. This topic describes how to archive the metadata of Apsara Distributed File System.
1. Make preparations before archiving.
Prepare the following machines: Prepare an independent buffer server as the archive server. If no buffer server is available, select a physical server that has a large disk capacity and good network performance. Otherwise, the security of the archived data cannot be ensured.

> **Note:** Offline archived files cannot be stored on objects to be archived. If no extra physical servers are available and if disk capacity is insufficient in the on-site environment, the system is unable to perform offline archiving. In this case, you must add physical servers or increase disk capacity before the offline archiving.

Prepare a transfer server to store one-time archived data and archived scripts of each service. The network of the archive server must be connected with that of the Docker container where the offline archive service is deployed. This ensures that backup containers in the related clusters of the Apsara Uni-manager Operations Console can log on to the transfer server and archive server by using SSH key pairs, without the need for you to provide the username and password.
2. Collect service information.
You can collect the Apsara Distributed File System information of services to be archived, which helps add the service information to the Apsara Uni-manager Operations Console.

> **Note:** In this topic, service names are customized as oss, ecs, ads, and ots, and the information of these services is collected. The services whose Apsara Distributed File System information you are about to collect are subject to the on-site environment.

i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
iii. In the left-side navigation pane, click **Service Management**. iv. Select **pangu** from the **Service** drop-down list. v. On the **Service Instances** tab, find the cluster that you want to view and click **Instance**
**Details** in the **Actions** column. The service details page appears.
vi. In the **Components** section, click the **PanguMaster#** component. vii. On the **Instances** tab, view and record an IP address of the PanguMaster# component. Record one of the three IP addresses of the PanguMaster# component. viii. Repeat Sub-steps e to g of Step 2 to view and record the Apsara Distributed File System information of each service. The following table lists the recorded results.

| Cluster name | IP address of PanguMaster# | Service name |
|---|---|---|
| AdvanceOssCluster-A-xx | 10.10.10.1 | oss |
| ECS-IO7-A-xx | 10.10.10.2 | ecs |
| ads-A-xx | 10.10.10.3 | ads |
| otsv3 p-A-xx _ | 10.10.10.4 | ots |

> **Note:** You can configure a custom service name. Make sure that the service name is unique and recognizable.

3. Configure the archive server.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **System Config**. iii. In the left-side navigation pane, choose **Archive management** > **Archiving Server**
**Settings**.
iv. Configure the parameters that are described in the following table and then click
**Submit**.

> **Note:** If the #FTPMaster server is deployed in the cluster of the service, the system will automatically fill in the information about the archive server ecs pangu.

| Parameter | Description |
|---|---|
| Archive server address | The IP address of the archive server. The archive server must meet the following requirements: The archive server is an independent physical server. The archive server is managed by the Apsara Infrastructure Management console. The network of the archive server is connected to other servers in Apsara Stack. Apsara Distributed File System cannot be deployed on the server or on the disk where archived metadata is stored. |
| Archive Service listening path | The storage path of archived files on the archive server. Note If the backup path does not start with /apsarapangu, /ASO- backup is added to the beginning of the path by default. The archive service detects new archived files by monitoring the specified folder on the archive server and determines whether the archiving is successful by comparing the Message-Digest Algorithm 5 (MD5) value of the archived file with that of the original file. |
| Archive file cleaning cycle | The actual period of time an archived object is saved. Unit: day. Overdue archived objects are deleted. |

v. In the dialog box that appears, select **I have read the above prompts and confirmed**
**the operation.** and click **OK**.
4. Manage archive services.
i. In the left-side navigation pane, choose Archive management > **Archive Products**. ii. Click **Add products**. In the dialog box that appears, specify the parameters described in the following table and click **OK**.

| Parameter | Description | Example |
|---|---|---|
| Product | Select a service from the drop-down list. pangu opsdns | pangu |
| Script | The name of the archived script. The system automatically selects the script based on the service. | metadata backup.py _ |
| Archive item | Enter the service information collected in Step 2. | ecs pangu _ |
| Error retries | The number of retries after an error occurs. In common cases, this parameter is set to 3. | 3 |

iii. Repeat Sub-step b of Step 4 to add all archive items in sequence.
5. Configure archiving settings.
i. In the left-side navigation pane, choose Archive management > **Archive Settings**. ii. Select the service archive item that you created in Step 4. In the right-side section, configure the parameters described in the following table and click **Modify** to trigger the archiving process.

| Parameter | Description |
|---|---|
| Product Cluster IP Address | The IP address of the actual transfer server. |
| Archive Folder | A folder on the transfer server. You only need to enter a folder path in the field without the need to manually create a folder to store archived files. Example: /apsarapangu/disk8/pangu master bak/product _ _ name pangu/bak. _ |
| Script Execution Folder | A folder on the transfer server. You only need to enter a folder path in the field without the need to manually create a folder to store script executions. Example: /apsarapangu/disk8/pangu master bak/product _ _ name pangu/bin. _ |
| Script Parameters | The execution parameters for the script. You must enter the value in the --ip=xxx.xxx.xxx.xxx format, where the IP address is one of the IP addresses of the PanguMaster# component described in Step 2. |
| Archive Schedule | The archiving schedule. In this example, the value 1 is entered, which specifies that the archiving is performed only once. |
| Archive Schedule Unit | The unit of the archive schedule. Valid values: Day, Hour, and Minute. In this example, Hour is selected to specify that the archiving is performed by hour. |
| Timeout period | The timeout period. Unit: seconds. For this example, set the value to 3600. |

iii. Repeat Sub-step b of Step 5 to configure all archive items of services.
6. View archiving details.
i. In the left-side navigation pane, click **Archive Details**. ii. View the archiving details of an item, including **Product**, **Archive item**, **File name**,
**Start time**, and **Status**. The archiving states include **Not started**, **In progress**,
**Complete**, **Timeout**, and **Failed**.

> **Note:** If the status of an archive item is Complete, you must check whether the MD5 values of the offline archive service and the archive server are consistent with each other. If the values are consistent with each other, the archiving is successful.

### 3.3 Security administrator

This topic describes common O&M operations performed by security administrators, including logon management.

#### 3.3.1 Logon management

This topic describes how to configure methods of logging on to the Apsara Uni-manager Operations Console.

**Description**

The system allows administrators to configure user logon methods based on business requirements, including the logon timeout period, multi-terminal logon settings, account validity period, password policy, logon time, and logon address to improve system security.

**Prerequisites**

You have obtained the permissions of a security administrator for the Apsara Uni-manager Operations Console.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Security**
**Strategy**.
3. On the **Account Policy** tab, specify the parameters described in the following table and
click **Submit**.

| Parameter | Description |
|---|---|
| Timeout Period (Minutes) | Specify a logon timeout period for the current account. If the logon time exceeds the specified time period, the system prompts you that the logon timed out and you need to try to log on again. Valid values: 10 to 180. |
| Multi-Terminal Logon Settings | Specify whether the current account allows simultaneous logon from multiple terminals. |
| ASO account validity period (days) | Specify the validity period of the current account. If the account is expired, the system locks this account and only the security administrator can unlock the account. Valid values: 10 to 365. |
| Account Freeze Policy (Days) | Specify the period during which the current account remains available. If the specified period elapses, the system freezes this account. Valid values: 0: indicates that the account freezing policy is disabled. 10~365 |

| Security Policy Is Valid for Preset Accounts | Specify whether the security policy is valid for preset accounts. Valid values: On: If a security policy expires (for example, the account or password expires), preset accounts cannot log on to the system. We recommend that you set a long validity period. Off: If a security policy expires, preset accounts can still log on to the system. Preset accounts never expire. Default value: Off. |
|---|---|

4. On the **Password policy** tab, specify the parameters described in the following table and
click **Submit**.

| Parameter | Description |
|---|---|
| Minimum Password Length | Specify the minimum number of characters in the password. Valid values: 10 to 20. |
| Required Character Types in Password | Select one or more character types that must be contained in the password. Valid values: Lowercase Letters Uppercase Letters Digits Special Characters |
| Logon Disabled After Password Expires | Specify whether to prohibit the current account from logging on to the system after the password expires. Valid values: Yes No |
| Reminder time before password expiration (days) | Set the time to send a reminder before the password of an account expires. For example, a value of 10 indicates that the expiration reminder is sent 10 days before the password expires when the user logs on. A value of 0 indicates that no reminder is sent. Valid values: 0 to 30. |
| Password Validity Period (Days) | Specify the validity period for the password. If the password expires, the system sends a notification to the user. 0 indicates that the password does not expire. Valid values: 0 to 1095. |
| Password History Check | Specify the number of historical passwords that you cannot reuse. For example, if you set this parameter to 3, the most recent three historical passwords cannot be reused. 0 indicates that all historical passwords can be reused. Valid values: 0 to 24. |

5. Configure a logon policy.
i. In the left-side navigation pane, click **Login Rule**. ii. In the upper part of the page, click **Add Policy**. iii. Configure the parameters described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Policy Name | Enter a name for the logon policy. |
| Policy Effective Period | Specify the dates when the logon policy starts and stops taking effect. |
| Description | Enter a description for the logon policy. |
| Shared scope | Select the scope in which you want to share the logon policy. Only Global Sharing is available. |
| Policy attributes | Valid values: Whitelist Blacklist |
| Policy Effective Time | Select the point in time from which users are allowed for logon. The start time for logon cannot be later than the end time for logon. |
| Policy Expire Time | Select the point in time from which users are not allowed for logon. |
| Login address | Enter the CIDR blocks of the logon policy. If you set the Policy attributes parameter to Whitelist, this parameter specifies the CIDR blocks that are allowed for logon. If you set the Policy attributes parameter to Blacklist, this parameter specifies the CIDR blocks that are prohibited from logging on to the system. Specify CIDR blocks such as 192.168.1.0/24. You can use a 32-bit mask in the CIDR block to indicate a single IP address. CIDR blocks cannot overlap each other. Separate multiple CIDR blocks with commas (,). |

### 3.4 Security auditor

This topic describes common O&M operations performed by security auditors, including operation log auditing.

#### 3.4.1 Operation log auditing

This topic describes how to audit the operation records of users in the console as a security auditor.

**Description**

Security auditors can audit, track, and analyze the operations of users including system administrators and security administrators. On the Console-based Audit and CLI-based Audit pages in the Operation Audit module, you can view the records of CLI-based and GUI-based operations including auditing.

**Prerequisites**

You have obtained the permissions of a security auditor.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Security Audit** > **Operation**
**Audit**.
3. In the left-side navigation pane, click **Console-based Audit**.
4. On the **Console-based Audit** page, perform the following operations based on your
business requirements: View GUI-based operation records. Specify the **Username** and **Time Range** parameters to filter operation records. Export GUI-based operation records.

> **Note:** By default, you can export a maximum of 10,000 records. If you select more than 10,000 records, only the first 10,000 records are exported.

Batch export: Select the operation records that you want to export and click **Batch**
**Export** below the list to export the selected records.
Export all reports: Click **Export** above the list to export all the operation records that are displayed in the list.

### 3.5 Role administrator

This topic describes common O&M operations performed by role administrators, including department management, user management, and role management.

#### 3.5.1 User management

This topic describes how to create a user and grant different permissions to the user.

**Description**

You can create a user and assign the user different roles to meet different requirements for system access control as a role administrator.

**Prerequisites**

You have obtained the permissions of a role administrator for the Apsara Uni-manager Operations Console. A custom role, if required, is created. A logon policy is configured.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. Create a department.
i. In the left-side navigation pane, click **Department Management**. ii. In the catalog tree on the left side, select the department to which you want to add a subdepartment and click **Add Department**. iii. In the Add Department dialog box, enter a new department name and click **OK**. After the department is added, you can view the department in the catalog tree.

> **Note:** The department name can be up to 64 characters in length and can contain lowercase letters, uppercase letters, digits, underscores (_), and hyphens (-).

4. Create a user.
i. In the left-side navigation pane, click **User Management.** ii. On the **Users** tab, click **Add**. iii. Specify the parameters described in the following table and click **OK**. After the user is added, you can view the user in the user list.

| Parameter | Description |
|---|---|
| Username | Enter a name for the user that you want to create. The name can be up to 48 characters in length and can contain digits, letters, and underscores ( ). You can enter email addresses as usernames. _ |
| Password | Enter a password for the user. The password must be 9 to 32 characters in length and must contain lowercase letters, uppercase letters, and digits. |
| Confirm Password | Enter the password again. Make sure that the two passwords that you enter are the same. |
| Logon Policy | Select a logon policy for the user. |
| Role | Select the role that you want to assign to the user. Note You can assign one or more roles to a user. |
| Department | Select the department that you created in Step 3. |

5. Create a user group.
i. In the left-side navigation pane, click **User Group Management**. ii. In the upper part of the page, click **Add**. iii. Specify the parameters described in the following table and click **OK**. After the user group is added, you can view the user group in the user group list.

| Parameter | Description |
|---|---|
| User Group Name | Enter a name for the user group. |
| Department | Select the department that you created in Step 3. |
| Role | Select the role that you want to add for the user group. Note You can add multiple roles for a user group. |

6. Manage the user.
i. On the **User Group management** page, find the user group that you created in Step 5 and click **Manage Users** in the **Actions** column. ii. Click **Add**. In the **Add** dialog box, select the user that you created in Step 4 and click **OK**.

> **Note:** If the user group role and the user role are inconsistent, the permissions of both roles are granted to the user.

iii. In the **Manage Users** dialog box, click **OK**. After the user is added to the user group, the added user is displayed in the **Users** column that corresponds to the user group.

## 4 General O&M

### 4.1 Monitoring management

This topic lists the following consoles for monitoring management: TianjiMon TianjiMon - Grafana Cloud platform dashboard

#### 4.1.1 Cloud platform monitoring

##### 4.1.1.1 Business monitoring for cloud services

###### 4.1.1.1.1 View the monitoring information of cloud services

**services**

This topic describes how to view the basic monitoring information and business metrics of all cloud services in the Apsara Uni-manager Operations Console.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Product Business Monitoring** > **Product**
**Monitoring**.
On the Product Monitoring page, you can perform the following operations based on your business requirements. View the total number of cloud services and the number of cloud services that are not at desired state. View the status of each cloud service. A blue icon indicates that the cloud service is at desired state. An orange icon indicates that the cloud service is not at desired state. Move the pointer over the icon of a cloud service to view the cloud service name. Click the icon to go to the cloud service details page. In the navigation tree of the cloud service details page, all clusters, services, and components of the cloud service are displayed. You can select **Show only Exceptions** to view only abnormal clusters, services, and components. You can select a cluster in the navigation tree to view the status, zone, basic monitoring information, and machine list of the cluster on the right side of the page. In this example, the Apsara Uni-manager Operations Console is used. On the **Basic monitoring** tab, view the monitoring data based on the time and metrics. You can turn on **Auto Refresh** in the upper-right corner to automatically update the monitoring data. On the **Machine List** tab, view the list of hosts in the cluster. You can find the host that you want to manage and click the icon in the **Operation** column to go to the Machine monitoring page. On the Machine monitoring page, view the basic information and monitoring data of the host. You can turn on **Auto Refresh** in the upper-right corner to automatically update the monitoring data. You can select a service in the navigation tree to view the status, cluster, and business monitoring information of the service on the right side of the page. On the **Business monitoring** tab, view the monitoring data based on the time and metrics. You can turn on **Auto Refresh** in the upper-right corner to automatically update the monitoring data. You can select a component in the navigation tree to view the status, cluster, service, basic monitoring information, business monitoring information, and machine list of the component on the right side of the page. On the **Basic monitoring** tab, view the basic monitoring information of the component, including the monitoring data of containers, processes, and Java virtual machines (JVMs).

###### 4.1.1.1.2 Configure business metrics for cloud service monitoring

**service monitoring**

This topic describes how to configure business metrics for monitoring cloud services in the Apsara Uni-manager Operations Console.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Product Business Monitoring** > **Access**
**Configuration**.
4. On the Access Configuration page, click **Create Configuration**. On the Create Access
Configuration page, configure the parameters that are described in the following table and click **Submit**.

| Section | Parameter | Description |
|---|---|---|
| Basic information | Monitoring Item Name | The name of the monitoring item. |
|   | Description | The description of the monitoring item. |
| Acquisition Address | Access Configuration | The type of the access configuration. Valid values: Exporter: configures whitelists for the metrics of cloud services with which Prometheus Exporter is integrated to determine the metrics that can be displayed and alerted. Push Gateway: configures whitelists for the metrics of cloud services that are integrated by using Push Gateway to determine the metrics that can be displayed and alerted. Log: converts the local logs of server roles of cloud services into metrics to report data for effective monitoring and alerting. |
|   | Cloud Products | The cloud service to which the access configuration belongs. |
|   | Service | The service to which the access configuration belongs. |
|   | Components | The component to which the access configuration belongs. |
|   | Metric Path | This parameter takes effect only when you set the Access Configuration parameter to Exporter. The URL of the HTTP API that is used to expose metrics to Prometheus Exporter. |
|   | Port | This parameter takes effect only when you set the Access Configuration parameter to Exporter. The HTTP port that is used to expose metrics to Prometheus Exporter. |
|   | Auth | This parameter takes effect only when you set the Access Configuration parameter to Exporter. The username that is used for authentication by Prometheus. |

|   | Auth password | This parameter takes effect only when you set the Access Configuration parameter to Exporter. The password of the username that is used for authentication by Prometheus. |
|---|---|---|
|   | pod tag selector | This parameter takes effect only when you set the Access Configuration parameter to Exporter. Click Add Entry. In the line that appears, configure the Key and Value parameters to add a pod tag. |
|   | Acquisition Test | This parameter takes effect only when you set the Access Configuration parameter to Exporter or Push Gateway. If you want to add or edit metrics, perform an acquisition test to obtain the metrics that can be integrated. |
|   | Data Source | This parameter takes effect only when you set the Access Configuration parameter to Log. Set the value to Local Log. |
|   | Log Path | This parameter takes effect only when you set the Access Configuration parameter to Log. The path in which local logs are stored. |
|   | Log encoding | This parameter takes effect only when you set the Access Configuration parameter to Log. The encoding format of local logs. |
|   | Classification of indicators | This parameter takes effect only when you set the Access Configuration parameter to Log. The category of metrics. Set the value to Keyword. |

| Indicator Access |   |   |
|---|---|---|
|   | Monitoring indicators | If you set the Access Configuration parameter to Exporter or Push Gateway, you can configure metrics after the acquisition test is passed. Click Add Entry and configure the following parameters for each metric: Indicator Code: the metric that is obtained from the acquisition test. Indicator Name: the name of the metric. Indicator description: the description of the metric. Indicator Type: the type of the metric. Valid values: Guage, Counter, Histogram, and Summary. Aggregation mode: the aggregation mode of the metric. Valid values: Avg, Sum, Min, Max, Group, Std Dev, Std Var, Count, Count Values, Bottomk, Topk, and Quantile. Unit: the unit of the metric. Metrics Aggregation Label: the tags of the metric. Operation: You can remove the metric or move the metric up or down. If you set the Access Configuration parameter to Log, you can click Add Entry and configure the following parameters for each metric: Indicator Code: the monitoring item that you want to configure. Indicator Name: the name of the metric. Keyword: the keyword of the metric. Operation: You can remove the metric or move the metric up or down. Aggregation mode: the aggregation mode of the metric. Set the value to Count. |

**What to do next**

| Operation | Description |
|---|---|
| View access configurations | In the left-side Service Catalog pane, select the cloud service or service that you want to manage. The access configurations of the cloud service or service are displayed on the right side of the page. Click Advanced Filter to filter access configurations. You can configure the Monitoring Item Name and Access Type parameters as filter conditions. In the access configuration list, you can view the monitoring item name, access type, service, and description of each access configuration. |
| Import access configurations | 1. On the Access Configuration page, click Import Configuration in the upper part. 2. In the Import Configuration dialog box, click Upload File. Note You can export access configurations to a file to view the format of the file that you can upload. 3. Select a configuration file and click Open. 4. Click Confirm Import. |
| Modify an access configuration | Note The default access configurations that are generated when you update the baseline version of a cloud service, including hotfixes, cannot be modified. 1. Find the access configuration that you want to modify and clickE dit in the Operation column. 2. On the Edit Access Configuration page, modify the configuration information and click Submit. |

| Copy an access configuration | Note The default access configurations that are generated when you update the baseline version of a cloud service, including hotfixes, cannot be copied. 1. Find the access configuration that you want to copy and clickC opy in the Operation column. 2. On the Copy Access Configuration page, confirm the configuration information and click Submit. |
|---|---|
| Export access configurations | Note The default access configurations that are generated when you update the baseline version of a cloud service, including hotfixes, cannot be exported. Export an access configuration 1. On the Access Configuration page, find the access configuration that you want to export, move the pointer over the icon in the Operation column, and then select Export. 2. In the dialog box that appears, click Download. Export multiple access configurations at a time 1. Select multiple access configurations that you want to export and click Export in the lower part of the page. 2. In the dialog box that appears, click Download. |
| Delete access configurations | Note The default access configurations that are generated when you update the baseline version of a cloud service, including hotfixes, cannot be deleted. Delete an access configuration 1. On the Access Configuration page, find the access configuration that you want to delete, move the pointer over the icon in the Operation column, and then select Delete. 2. In the Delete Configuration message, click Delete. Delete multiple access configurations at a time 1. Select multiple access configurations that you want to delete and click Delete in the lower part of the page. 2. In the Delete Configuration message, click Delete. |

###### 4.1.1.1.3 Configure alert rules

On the Alert Rules page, you can view and manage alert rules for monitoring all cloud services. This topic describes how to configure an alert rule.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Product Business Monitoring** > **Alert Rules**.
4. On the Alert Rules page, click **Create Rules**. On the Create alarm rules page, configure the
parameters that are described in the following table and click **Submit**.

| Section | Parameter | Description |
|---|---|---|
| Basic information | Rule Name | The name of the alert rule. |
|   | Rule Description | The description of the alert rule. |
|   | Cloud Products | The cloud service to which the alert rule belongs. |
|   | Service | The service to which the alert rule belongs. |
|   | Active Cluster | The cluster to which the alert rule applies. |
|   | Alarm level | The severity of the alert that is generated when the alert rule is triggered. Valid values: Emergency Serious Warning Reminder |
|   | Alarm execution cycle | The check interval of the alert rule. Unit: seconds. |

| Alarm Condition | Configuration Method | The method that is used to configure the alert rule. Valid values: Form: configures a rule for a single metric. The rule contains a monitoring item, a metric, and trigger conditions. TianjiMon expression: configures a rule for one or more metrics based on the TianjiMon expression. PromQL expression: configures a rule for one or more metrics based on the PromQL expression. |
|---|---|---|
|   | Monitoring Items | The item to be monitored by the alert rule. |
|   | Monitoring indicators | This parameter takes effect only when you set the Configuration Method parameter to Form. The metric to be monitored by the alert rule. In the Filter Condition section, click Add Entry. In the line that appears, configure the Filter Items and Filter Value parameters. Note You can specify multiple filter conditions that are evaluated by using the AND operator to filter metrics. |
|   | Trigger condition | The conditions that are used to trigger the alert rule. |
| Alarm Period | Effective time | The period during which the alert rule takes effect. You can specify a period of time less than 24 hours. |
|   | Channel Silence Period | The interval between two alerts that are generated when the alert rule is triggered. |

**What to do next**

| Operation | Description |
|---|---|

| View alert rules | In the left-side Service Catalog pane, select the cloud service or service that you want to manage. The alert rules configured for the cloud service or service are displayed on the right side of the page. Click Advanced Filter to filter alert rules. You can configure the Rule Name, Rule Status, Alarm level, Monitoring Items, and Active Cluster parameters as filter conditions. In the alert rule list, you can view the name, description, alert level, monitoring item, and trigger conditions of each alert rule, whether the alert rule is enabled, and the cluster to which the alert rule applies. You can move the pointer over the number in the Active Cluster column to view the name of the cluster. |
|---|---|
| Disable alert rules | Note You can disable only alert rules in the Enabling state. Disable an alert rule 1. Find the alert rule that you want to disable and clickD eactivate in the Operation column. 2. In the Confirm deactivation message, click OK. Disable multiple alert rules at a time 1. Select multiple alert rules that you want to disable and clickD eactivate in the lower part of the page. 2. In the Confirm Mass Deactivation message, click OK. |

| Enable alert rules | Note You can enable only alert rules in the Deactivated state. Enable an alert rule 1. Find the alert rule that you want to enable and clickE nable in the Operation column. 2. In the message that appears, click OK. Enable multiple alert rules at a time 1. Select multiple alert rules that you want to enable and clickE nable in the lower part of the page. 2. In the message that appears, click OK. |
|---|---|
| Modify an alert rule | 1. Find the alert rule that you want to modify and clickE dit in the Operation column. 2. On the Edit Alarm Rules page, modify the parameters and clickS ubmit. |
| Export alert rules | Export an alert rule 1. Find the alert rule that you want to export and clickE xport in the Operation column. 2. In the Create Download dialog box, select a download path and click Download. Export multiple alert rules at a time 1. Select multiple alert rules that you want to export and clickE xport in the lower part of the page. 2. In the Create Download dialog box, select a download path and click Download. |
| Import alert rules | 1. On the Alert Rules page, click Import Rules in the upper part. 2. In the Import Configuration dialog box, click Upload File. Note You can export alert rules to a file to view the format of the file that you can upload. 3. Select a configuration file and click Open. 4. Click Confirm Import. |
| Copy an alert rule | 1. Find the alert rule that you want to copy, move the pointer over the icon in the Operation column, and then select Copy. 2. On the Copy Alarm Rules page, confirm the information about the alert rule and click Submit. |

| Delete alert rules | Delete an alert rule 1. Find the alert rule that you want to delete, move the pointer over the icon in the Operation column, and then select Delete. 2. In the Confirm Delete message, click OK. Delete multiple alert rules at a time 1. Select multiple alert rules that you want to delete and clickD elete in the lower part of the page. 2. In the Confirm Batch Delete message, click OK. |
|---|---|

###### 4.1.1.1.4 Alert history

The Alert History page displayed all the alert information about project monitoring for clusters and services.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Product Business Monitoring** > **Alert History**.
In the left-side **Service Catalog** pane, select the cloud service or service that you want to manage. The corresponding alert trend and alerts are displayed on the right side of the page. In the upper-right corner of the page, select a time range. The alert information of the corresponding time range is displayed in the lower part of the page. Alert Trend: displays the trend of historical alerts within the specified time range. Alert List: displays historical alerts within the specified time range. Click **Advanced Filter** to filter alert rules by alert level, monitoring item, rule name, or cluster to obtain the history of an alert. In the alert list, find the alert that you want to view and click **View Details** in the
**Operation** column. On the panel that appears, view the basic information about the alert
and the corresponding alert rules. In the **Alarm Rules** section, click **Rule Editing**. On the Edit Alarm Rules page, modify the alert rule and click **Submit**.

##### 4.1.1.2 Data dashboard

###### 4.1.1.2.1 View data on the read and write dashboard

**dashboard**

The read and write dashboard displays the impacts of the metrics of Apsara Stack services that are integrated with CloudMonitor or TianjiMon on the Tablestore capacity as well as the capacity usage of these metrics. This topic also describes how to modify the throttling policy for these metrics.

**Prerequisites**

You have the permissions of the cloud platform monitoring administrator.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Data Dashboard** > **Read/Write Dashboard**.
In the upper part of the Read/Write Dashboard page, you can select a time period to check data changes.
**OTS capacity**: displays the following metrics: **Current OTS water level**, **Total QPS**,
**Write success rate**, and **Write delay**.
**Current OTS water level**: the ratio of the current queries per second (QPS) to
the maximum QPS supported in theory.
**Total QPS**: the sum of the QPS of all monitoring systems.
**Write success rate**: the lowest write success rate among all monitoring
systems.
**Write delay**: the highest write latency among all monitoring systems.
**Node statistics**: displays the **Number of physical nodes**, **Number of PaaS nodes**,
and **Nodes** metrics.
**QPS of monitoring system**: displays the QPS for CloudMonitor and TianjiMon to read
data from Tablestore.
**Monitoring system write success rate** : displays the success rate of writing data from
CloudMonitor and TianjiMon to Tablestore.
**Monitoring system write delay** : displays the latency in writing data from CloudMonitor
and TianjiMon to Tablestore. Unit: milliseconds.
**Cloud product write volume**: displays the amount of data written from various cloud
services to monitoring systems. You can click **All monitoring systems** and select CMS or TianjiMon to display the amount of data written to CloudMonitor or TianjiMon.
**Indicator write amount Top10**: displays the top 10 metrics with the highest number of
data writes. This section displays the name, monitoring system, and number of data writes per minute of each metric.

**Modify the throttling policy**

1. On the Read/Write Dashboard page, click **Throttle control** in the upper-right corner.
2. In the Throttle control panel, click **Edit** and modify the settings in the Cloud Product Control
and **Monitoring indicator blacklist** sections. Modify the cloud service control setting Select **Allow adding monitoring metrics** or **Do not add monitoring indicators**. You cannot specify the cloud service to which the throttling policy applies. The throttling policy applies to all cloud services. The setting in the Cloud Product Control section takes effect for all TianjiMon metrics. By default, Allow adding monitoring metrics is selected. If you select Do not add monitoring indicators, the metrics of cloud services can no longer be added to Tablestore. The metrics that are already added to Tablestore are not affected. Add a metric to the metric blacklist If a metric is added to the metric blacklist in the throttling policy, the data of this metric is no longer written to Tablestore. a. Click **Add Indicator**. The **Add indicator blacklist** dialog box appears. b. Configure the **Monitoring Platform** and **Project** parameters and select a metric.

> **Note:** **Monitoring Platform**: the monitoring platform whose metrics you want to add to the metric blacklist. Valid values: CMS and TIANJIMON.
> **Project**: the project in the monitoring platform whose metrics you want to add to the metric blacklist. Example: tjm_tianji. After you select a project, the metrics of the project are displayed. Then, you can select a metric based on the current traffic of metrics.

c. Click **OK**. The selected metric is added to the metric blacklist. Remove a metric from the metric blacklist a. In the metric blacklist, find the metric that you want to remove and click **Remove** in the Operation column. b. In the message that appears, click **Remove**.
3. Click **Save**.

###### 4.1.1.2.2 Customize a dashboard

You can customize a dashboard to display the metrics for business monitoring and application monitoring on the same page in real time. You can drag elements to customize a dashboard in a visualized manner. You can also specify multiple conditions to query data and display the queried data in multiple types of charts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Data Dashboard** > **Custom Dashboard**.
4. On the Custom Dashboard page, click **Create a directory**. In the Create a directory dialog
box, enter a directory name and click **OK**.
5. Click **Create a dashboard**. In the Create a dashboard dialog box, configure the
parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Large disk directory | The directory in which the dashboard is stored. |
| Market Name | The name of the dashboard. |
| Large disk JSON data | The JSON-formatted data of the dashboard. Note The title in the JSON-formatted data overwrites the dashboard name. |
| Whether to convert JSON data | Specifies whether to convert the JSON-formatted data. You can select Grafana JSON data, please convert and use. Note Lossy conversion is performed. If a data source cannot be mapped, the default data source is used. In this case, the system may fail to obtain data from the data source that you specify. Some data transformation and chart configurations are not retained, and manual configurations are required. |

6. Click the name of the dashboard created in Step 5.
7. In the upper-right corner of the page, choose **Create Panel > Create Panel**.
8. On the **Data Configuration** tab in the right-side pane, select a data source.

> **Note:** Click **Add Query**. In the Query 1 section, configure the **service name** and **promQL** **statement** parameters to configure the metrics for data query.

9. On the **Chart Configuration** tab in the right-side pane, configure the parameters that are
described in the following table.

| Parameter | Description |
|---|---|
| Title | The title of the chart. The title is displayed in the upper-left corner of the dashboard panel. |
| Description | The description of the chart. You can move the pointer over the icon to the right of the title to view the description. |

| Chart type | The type of the chart. Valid values: Line Bar Pie Linebar Gauge Heatmap Card Table Note The parameters of a chart vary based on the chart type. For more information, see the following table. |
|---|---|

The following table describes the parameters of different types of charts.

| Chart type | Parameter | Description |
|---|---|---|
|   | Chart elements | Specifies whether the following features are supported: Stacking Smooth curve Online with dots |
|   | X-axis | The x-axis configurations, including the following parameters: Display: specifies whether to display the x-axis. Type: the type of the x-axis. Valid values: Time, Classification, and Time classification. Time format: the format of the time. This parameter is displayed only when you set the Type parameter to Time or Time classification. |

| Line |   |   |
|---|---|---|
|   | Y-axis | The y-axis configurations, including the following parameters: Display: specifies whether to display the y-axis. Numeric type Unit Whether automatic carry is required: specifies whether to enable automatic rounding. This parameter is displayed only when the selected numeric type supports automatic rounding. Type Minimum value Maximum Cardinality: This parameter is displayed only when you set the Type parameter to Logarithm. Index: This parameter is displayed only when you set the Type parameter to Index. Decimal places Note You can click the icon to configure parameters for the y-axis on the right. |
|   | Legend | Display: specifies whether to display the legend. Table type Note If you turn on Table type, you must configure the following parameters: Location Statistical value Display Decimal places |
|   | Auxiliary line | The information about the auxiliary line that helps you better analyze the chart data, including the following parameters: Coordinate axis Numerical value Status Text Text position Text alignment Offset in X direction Offset in Y direction |

|   | Auxiliary area | The information about the auxiliary area. An auxiliary area is used to check whether data points are normal in the specified data range. |
|---|---|---|
|   | Data axis configuration | The information about the data axis. Different metrics can be displayed on the left and right y-axes. |
| Bar | Chart elements | Specifies whether the following features are supported: Display label Vertical column chart Stacking Reverse stacking: This parameter is displayed only when you turn on Stacking. Group stacking Percentage: This parameter is displayed only when you turn on Stacking. |
|   | X-axis | The x-axis configurations, including the following parameters: Display: specifies whether to display the x-axis. Type: the type of the x-axis. Valid values: Classification and Time classification. Time format: the format of the time. This parameter is displayed only when you set the Type parameter to Time classification. |
|   | Y-axis | For more information, see the parameter descriptions of the line chart. |
|   | Legend | For more information, see the parameter descriptions of the line chart. |
|   | Auxiliary line | For more information, see the parameter descriptions of the line chart. |
|   | Auxiliary area | For more information, see the parameter descriptions of the line chart. |
|   | Data axis configuration | For more information, see the parameter descriptions of the line chart. |

| Pie | Chart elements | Specifies whether the following features are supported: Display label Automatic sorting Ring diagram |
|---|---|---|
|   | Legend | For more information, see the parameter descriptions of the line chart. |
| Linebar | Chart elements | Specifies whether the following features are supported: Area Stacking: This parameter is displayed only when you turn on Area. Reverse stacking: This parameter is displayed only when you turn on Stacking. Group stacking Smooth curve Online with dots |
|   | X-axis | For more information, see the parameter descriptions of the line chart. |
|   | Y-axis | For more information, see the parameter descriptions of the line chart. |
|   | Legend | For more information, see the parameter descriptions of the line chart. |
|   | Auxiliary line | For more information, see the parameter descriptions of the line chart. |
|   | Auxiliary area | For more information, see the parameter descriptions of the line chart. |
|   | Data axis configuration | For more information, see the parameter descriptions of the line chart. |
| Gauge | Chart elements | The elements of the chart, including the following parameters: Numeric type Number of scale segments Pointer scale |

| Heatmap | Chart elements | The elements of the chart, including the following parameters: Display label Color scheme Number of colors: This parameter is displayed only when you set the Color scheme parameter to Sequential Color. Minimum value: This parameter is displayed only when you set the Color scheme parameter to Sequential Color, 4 State Color, or 7 State Color. Maximum: This parameter is displayed only when you set the Color scheme parameter to Sequential Color, 4 State Color, or 7 State Color. |
|---|---|---|
|   | X-axis | Display: specifies whether to display the x-axis. |
|   | Y-axis | Display: specifies whether to display the y-axis. |
|   | Legend | Display: specifies whether to display the legend. |
| Card | Chart elements | The elements of the chart, including the following parameters: Number of columns Note If this parameter is not specified, the number of columns is adaptive to the queried data. Separation line |
|   | Data Mapping | Click Add Data Mapping. In the Data Mapping 1 section, configure the following parameters: Numeric type: Valid values: Numerical value and Scope. Numerical value: This parameter is displayed only when you set the Numeric type parameter to Numerical value. Numerical range: This parameter is displayed only when you set the Numeric type parameter to Scope. Text Color |

| Table | Data Mapping | Click Add Data Mapping. In the Data Mapping 1 section, configure the following parameters: Column name Mapping type Mapping relationship: This parameter is not displayed only when you set the Mapping type parameter to Link. Link: This parameter is displayed only when you set the Mapping type parameter to Link. Note Data is retrieved from the table based on the column name in the format of {{a}} or {{a.b}}. For example, if you want to retrieve data from the id column, set this parameter to https://xxx.com? id={{id}}. Decimal: This parameter is displayed only when you set the Mapping type parameter to Progress Bar. Note A decimal number is automatically converted into the percentage format. |
|---|---|---|

0. Optional. On the **Data Transformation** tab in the right-side pane, click **Add Data**
**Transformation** and select **Data Filtering**. In the Data Filtering section, select the
columns that you want to use to filter data.
1. Optional. On the **Data Transformation** tab in the right-side pane, click **Add Data**
**Transformation** and select **Data Column Naming**. In the Data Column Naming section,
you can rename a column.
2. Click **Apply to Dashboard** in the upper-right corner of the page.
3. Optional. In the upper-right corner of the page, choose **Create Panel > Create Row**.
Move the pointer over a row and click the icon to modify the row name. You can also click the icon to delete the row. Click the custom layout drop-down list in the upper-right corner to specify the number of charts that are displayed in each row.
4. Click the
icon to save the dashboard. Click the icon. In the Settings panel, you can configure the basic settings, variables, and JSON mode for the dashboard.

> **Note:** After you create a variable, the **Variable Filtering** button appears in the upper-right corner of the dashboard. You can use the variable filtering feature to filter data on the dashboard. To create a variable, perform the following operations:
> In the Settings panel, click the **Variable** tab in the left-side pane. In the right-side pane, click **Create a variable**. In the dialog box that appears, configure the parameters and click **OK**.

Click the **Last 1 Hour** drop-down list in the upper-right corner to select or customize a time range. Click the icon to manually refresh the charts on the dashboard. Click the icon to enable or disable automatic refresh. Click the icon to display the dashboard in full screen mode.

**What to do next**

| Operation | Description |
|---|---|
| View a dashboard | 1. On the Custom Dashboard page, enter a keyword in the search box in the upper part of the page to search for the directory or dashboard that you want to view. 2. Click the name of the dashboard. |
| Modify a dashboard panel | 1. On the Custom Dashboard page, enter a keyword in the search box in the upper part of the page to search for the dashboard that you want to manage. 2. Click the name of the dashboard. 3. Move the pointer over the upper-right corner of the panel that you want to modify, click the icon, and then select Edit. On the page that appears, you can modify the data configurations, data transformation, and chart configurations of the panel. |
| Copy a dashboard panel | 1. On the Custom Dashboard page, enter a keyword in the search box in the upper part of the page to search for the dashboard that you want to manage. 2. Click the name of the dashboard. 3. Move the pointer over the upper-right corner of the panel that you want to copy, click the icon, and then select Copy. |

| Delete a dashboard panel | 1. On the Custom Dashboard page, enter a keyword in the search box in the upper part of the page to search for the dashboard that you want to manage. 2. Click the name of the dashboard. 3. Move the pointer over the upper-right corner of the panel that you want to delete, click the icon, and then select Delete. 4. In the message that appears, click OK. |
|---|---|
| View the information about a dashboard panel | 1. On the Custom Dashboard page, enter a keyword in the search box in the upper part of the page to search for the dashboard that you want to manage. 2. Click the name of the dashboard. 3. Move the pointer over the upper-right corner of the panel that you want to view, click the icon, and then select View. The View Panel panel appears and displays the information in the JSON format. |
| Modify the directory and name of a dashboard | 1. On the Custom Dashboard page, find the dashboard that you want to modify and click the icon in the Operation column. 2. In the dialog box that appears, modify the parameters and clickO K. |
| Copy a dashboard | 1. On the Custom Dashboard page, find the dashboard that you want to copy and click the icon in the Operation column. 2. In the dialog box that appears, confirm the information about the dashboard and click OK. |
| Delete dashboards | Delete a dashboard 1. On the Custom Dashboard page, find the dashboard that you want to delete and click the icon in the Operation column. 2. In the message that appears, click OK. Delete multiple dashboards at a time 1. Select multiple dashboards that you want to delete and clickB atch deletion in the lower part of the page. 2. In the message that appears, click OK. |
| Move multiple dashboards at a time | 1. On the Custom Dashboard page, select multiple dashboards that you want to move and click Batch move in the lower part of the page. 2. In the dialog box that appears, select the directory to which you want to move the dashboards and click OK. |

| Modify a directory | 1. On the Custom Dashboard page, find the directory that you want to modify and click Edit to the right of the directory name. 2. Enter a directory name and click OK. |
|---|---|
| Delete a directory | 1. On the Custom Dashboard page, find the directory that you want to delete and click Delete to the right of the directory name. 2. In the message that appears, click OK. Note If you delete a directory, all dashboards in the directory are also deleted. Proceed with caution. |

###### 4.1.1.2.3 Configure a data source for dashboards

This topic describes how to add an API data source for dashboards to manage API data services in a visualized manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Monitor Management** >
**Tianjimon**.
3. In the left-side navigation pane, choose **Data Dashboard** > **Dashboard Data Source**.
4. On the Dashboard Data Source page, click **Add a data source**. In the New data source
dialog box, configure the parameters that are described in the following table and click **OK**.

| Parameter | Description |
|---|---|
| Name | The name of the data source. |
| Description | The description of the data source. |
| Request address | The request URL of the data source, such as the domain name or IP address. If a port is available, the URL must contain the port number. Only HTTP is supported. |
| Headers | Click Add. In the line that appears, enter a key and a value. |

**What to do next**

| Operation | Description |
|---|---|
| View the information about a data source | In the upper part of the page, enter a data source name in the search box to search for a data source. In the search results, view the information about the data source. |
| Modify the configurations of a data source | 1. Find the data source that you want to modify and clickC onfiguration in the Operation column. 2. In the Configure data source dialog box, modify the parameters and click OK. |
| Remove a data source | 1. Find the data source that you want to remove and clickD elete in the Operation column. 2. In the Delete message, click OK. |

### 4.2 Alerts

This topic describes modules of the alert management feature.

**Positioning**

If exceptions or faults occur in cloud infrastructure or software on the cloud platform, alerts are triggered. The sources of alerts include monitored cloud products, the monitoring system, and objects that are monitored by the monitoring system. After alerts are generated, the alert information is displayed on the Alert Overview, Alerts, and Alert details pages from different dimensions. For example, the total number of alerts for each module of a product is displayed on the Alert Overview page, alerts are converged and the number of alerts is increased on the Alerts page, and the details of an alert are displayed on the Alert details page.

**Benefits**

The alert management feature allows the system to report alerts or collect monitoring data to match alert rules. This helps manage the alerts of cloud resources in various modules of the cloud platform in a centralized manner and efficiently troubleshoot faults to ensure business stability.

**Modules**

| Module | Description |
|---|---|
| Alert Overview | Displays general information about alerts by region, alert source, alert trend, alert distribution, and cloud product. |
| Alerts | Displays information about all reported alerts, including disabled alerts. You can view the details of an alert, change the alert status, and export alert information on this page. |
| Alert Settings | Provides management features related to alerts, including policy management, alert template, notification management, alert blocking, and alert rule configuration. |

**Alert sources**

The following table lists the sources of alerts:

| Original value | Source |
|---|---|
| tianjimon | Cluster monitoring system (TianjiMon) |
| tpcmon | Apsara Stack lightweight monitoring system (TPCMon) |
| dts | Data Transmission Service (DTS) |
| Bcmc# | Zone-disaster recovery system of Apsara Stack Resilience |
| DB | License for Apsara Stack products |
| drds | PolarDB-X |

| asrbr-backup | Backup and recovery system of Apsara Stack Resilience |
|---|---|
| ascm | Apsara Uni-manager Management Console |
| dbs-dbs | Database Backup Service (DBS) |
| admin-server | admin-server |
| asd | Apsara Stack Doctor (ASD) |
| sds-management | sds-management |
| bcc | Apsara Bigdata Manager (BCC) |
| aso-inventory | Inventory monitoring system of Apsara Uni-manager Operations Console |
| OcpApiV2 | ApsaraDB for OceanBase |

#### 4.2.1 Alert overview

This topic describes the overview of alerts by region, alert source, and cloud service. You can view the details of alerts by region and on a regular basis.

**Prerequisites**

System administrator permissions are granted.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Overview**.
3. The Alert Overview page consists of the following five sections that analyze and collect
statistics on alert information from different perspectives. The **Alerts for Regions** section shows the number of alerts by level for each region. Levels P1 to P4 alerts are displayed in different colors on the ring diagram. A larger area of a color on the ring diagram indicates more alerts of the corresponding level. The **Alert Source** section shows the status of each alert source. Orange indicates that the alert source is abnormal. Blue indicates that the alert source is normal. The **Alert Trend** section shows the number of alerts by date. Colors on each bar represent the alert levels. A darker color indicates a higher alert level. A larger area of a color on a bar indicates more alerts of the corresponding levels. If you move the pointer over a bar, the system shows the numbers of alerts of all levels for the day. The line charts show the trend of different alert levels. The **Alert Distribution** section shows the quantities and levels of alerts of different services from the following dimensions: **Active P1 Alerts**, **Full Active Alerts**, and **Full**
**Alert History**.
A larger color block indicates more alerts of the corresponding level. When you move the pointer over a color block, the system shows the alert level and quantity. The **Pending P1 Alerts** section shows the cloud platforms that have pending P1 alerts and the quantity of corresponding alerts. Each tab is a product category. Click a tab to view the products that have pending P1 alerts and the corresponding alert quantity under the category.

**What to do next**

After you obtain the alert overview information based on your requirements, you can view alert details in the alert list.

#### 4.2.2 Alerts

You can view the details of all current alerts and change the status of alerts if the system does not update the status in a timely manner. You can also specify custom conditions to search for specific alerts and export the alert information in XLSX format.

**Prerequisites**

System administrator permissions are granted.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alerts**.
3. The system enters the **Not Disabled** tab. You can view the unclosed alerts on this tab. The
following information of unclosed alerts is available: **Alert Level**, **Alert Item ID/Name**,
**Resource attribution**, **Alert Status**, **Alert start time**, **Last alarm time/duration**,
**Alerts**, **Extended Attributes**, **Alert Object**, **Object Type**, and **Alert Source**.

> **Note:** You can also switch to the **Disabled** tab to view closed alerts.
> **Alert Level** and **Last alarm time/duration** can be sorted.

4. In the upper part of the page, select **Resource attribution** and enter an alert keyword to
perform a fuzzy search. The keywords include alert IDs, alert information, and extended attributes. You can also click **Advanced Filter** to filter alert data by **Alert Item ID**, **Alert Item**
**Name**, **Alert start time**, **Alert Level**, **Alert Status**, **Alert Source**, **Alert Object**, and
**Object Type**.

> **Note:** On the **Not Disabled** tab, the system does not display the closed alerts by default. However, you can set Alert Status in **Advanced Filter** to filter and display closed alerts. Similarly, on the **Disabled** tab, the system does not display unclosed alerts by default. You can set Alert Status in **Advanced Filter** to filter and display the unclosed alerts.

5. Click **Alert Item ID/Name** of an alert to go to the Alert Details page and view the details of
the alert. In the upper-right corner of the Alert Details page, you can perform the following operations: Click **Handle** or **Close** to change the status of the alert. In the **Basic Information** section, view the basic information about the alert. In the **Extended Information** section, view the extended information about the alert.

> **Note:** Move the pointer over **Details** next to **Detailed alert information**. The details of the alert are displayed.

In the **State timing diagram** section, view the alert monitoring metrics in a chart.
**1 Day**: shows the alert metrics of the day before the alert is triggered.
**1 Week**: shows the alert metrics of the week before the alert is triggered.
In the **Alert impact** section, view the impact of the alert. You can view the service roles that may be affected by the alert and their status. In addition, the services, clusters, products, and physical machines to which the service roles belong are displayed.
6. After an alert is cleared, the system periodically synchronizes the alert status based on the
alert rules. If the system does not update the status of an alert in a timely manner after the alert is cleared, you can manually change the status of the alert to **Processing** or **Closed**. Change the alert status to **Processing**: Single alert: On the **Alerts** page, find the alert whose status you want to change and click **Handle** in the **Actions** column. Then, the alert enters the **Processing** state. Multiple alerts: Select the alerts whose status you want to change and click **Batch**
**Handle** in the lower part of the page. Then, the alerts enter the **Processing** state.
Change the alert status to **Closed**: Single alert: On the **Alerts** page, find the alert whose status you want to change and click **Close** in the **Actions** column. Then, the alert enters the **Closed** state. After you change the status of the alert, the alert is displayed on the **Disabled** tab. Multiple alerts: Select the alerts whose status you want to change and click **Batch**
**Close** in the lower part of the page. Then, the alerts enter the **Closed** state. After you
change the status of the alerts, the alerts are displayed on the **Disabled** tab.
7. In the upper-left corner of the Alerts page, click **Export Report** to export alerts in XLSX
format.

#### 4.2.3 Alert settings

**Modules**

| Module | Description |
|---|---|
| Policy Management | You can configure alert notification contacts, contact groups, and static parameters. |
| Alert Templates | You can manage alert templates. |
| Alert Notification | You can configure alert notification channels to push alert notifications to parties of interests. |
| Alert Blocking | You can block alerts based on time range, resource ownership, cluster, service, server role, server, alert level, and alert source settings. You can also block specific alerts based on alert IDs. |
| Blocked Alerts | You can view blocked alerts and their details and associated blocking rules. |
| Alert Rule Settings | You can view rules that trigger alerts. |

##### 4.2.3.1 Policy management

The Policy Management module allows you to configure alert contacts, contact groups, static parameters, and time-to-live (TTL) of alert data.

**Manage contacts**

You can query, add, modify, or delete alert contacts based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. On the **Contact** tab of the Policy Management page, perform the following operations:
Query an alert contact. In the upper-left corner of the Policy Management page, select the name of the service for which you want to query alert contacts from the Product drop-down list and enter contact names in the Name field. Then, you can view the details of the alert contacts that meet the search conditions. Add an alert contact. Click **Add Contact**. In the dialog box that appears, configure parameters and then click
**OK**. The following table describes the parameters that you need to configure.

| Parameter | Description |
|---|---|
| Name | The name of the alert contact. |
| Role | The role of the alert contact. Valid values: Developer: a developer TAM: an O&M engineer |
| Product | The products for which you want to create the alert contact. You can select one or more products. |
| Alert Severity | The alert levels. You can select one or more alert levels. Valid values: P1: critical P2: major P3: minor P4: reminder |
| Aggregation Dimension | The method of pushing the alert. Valid values: One By One Product Metrics Machine |
| Duty Hours | The start time and end time of the watch-hour of the alert contact. |
| DingTalk ID | The DingTalk ID of the alert contact. |
| Email Address | The email address of the alert contact. |

Modify an alert contact. Click **Modify** in the **Operation** column that corresponds to an alert contact. In the dialog box that appears, modify the information and click **OK**. Delete an alert contact. Click **Delete** in the **Operation** column that corresponds to an alert contact. In the message that appears, click **OK**.

**Manage contact groups**

You can query, add, modify, or delete alert contact groups based on your business requirements.

**Prerequisites**

Alert contacts are created.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. Click the **Contact Groups** tab.
5. You can perform the following operations:
Query an alert contact group. Enter a group name in the search box to view the alert contact groups that meet the search conditions. Add an alert contact group. In the upper-left corner of the Policy Management page, click **Add Contact Group**. In the dialog box that appears, configure parameters and then click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Group Name | The name of the alert contact group. |
| Description | The description of the alert contact group. |
| Select Contact | The contacts to be added to the contact group. |

Modify an alert contact group. Click **Modify** in the **Actions** column that corresponds to an alert contact group. In the dialog box that appears, modify the information and click **OK**. Delete an alert contact group. To delete a single contact group, find the contact group and click **Delete** in the
**Actions** column. In the message that appears, click **OK**.
To delete multiple contact groups at a time, select multiple contact groups and click
**Delete** in the lower part of the page. In the message that appears, click **OK**.

**Static Parameter Settings**

You can configure alert-related static parameters based on your business requirements.

**Background information**

The current version does not support new alert configurations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. Click the **Static Parameter Settings** tab.
5. In the upper part of the Static Parameter Settings tab, enter a parameter code in the
Parameter Code field to search for a static parameter.
6. Find the static parameter that you want to modify and click **Edit** in the **Operation** column.
7. In the **Modify Static Parameters** dialog box, modify parameters and click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Parameter Name | The parameter name that is related to the configuration. |
| Parameter Value | The value of the parameter. For example, you set the Alarm Time Out parameter to 5, which indicates five days. |
| Description | The description of the configuration. |

**TTL of alert data**

By default, alert data is stored for seven days due to the specifications of the base database. If alert data of a product needs to be stored for a longer period of time, you can modify the retention period for the product. However, the alert data size cannot exceed the upper limit.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. On the Policy Management page, click the **Alarm data TTL** tab.
5. In the **Product Configuration** section, click **Add configuration**.
6. In the Product Configuration dialog box, configure the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|
| Product (Alert Source) | The product to which the alert data belongs. |
| Retention Period | The retention period of the alert data of a product. By default, alert data is stored for seven days. Valid values: 7 to 30. |
| Maximum data volume | The maximum alert data size of a product. Up to 300,000 rows of alert data can be stored for a single product. If the alert data size exceeds the upper limit, the data of the earliest day is cleared by default. |

**What to do next**

| Operation | Procedure |
|---|---|
| Modify the alert data configuration of a product | 1. On the Alarm data TTL tab of the Policy Management page, find the alert data configuration of the product and click Modify in the Operation column. 2. In the dialog box that appears, modify the parameters and clickO K. |
| Delete the alert data configuration of a product | 1. On the Alarm data TTL tab of the Policy Management page, find the alert data configuration of the product and click Delete in the Operation column. 2. In the message that appears, click OK. |
| View the change history of the alert data configuration of a product | 1. On the Alarm data TTL tab of the Policy Management page, find the alert data configuration of the product and click Modify a record in the Operation column. 2. In the dialog box that appears, view the change history of the alert data configuration of the product, including Product Name, Storage duration (days), Maximum data volume, Action Type, Operated By, and Modification time. |

**Data dumping**

**Background information**

If you have higher requirements on the retention period or maximum data volume, you can dump the data to Simple Log Service (SLS) at the tenant side.

**Limit**

If SLS is not deployed in the current environment, alert data cannot be dumped.
1. In the Basic configuration section of the Alarm data TTL tab, click the icon next to **Data**
**Dump** to turn on **Data Dump**. By default, Data Dump is turned off.
2. In the Data Dump Settings dialog box, configure the parameters that are described in the
following table and click **OK**.

| Parameter | Description |
|---|---|
| Retention Period (Days) | The retention period of dumped alert data. By default, dumped alert data is stored for 180 days. Valid values: 30 to 720. |
| Product | The product for which you want to dump alert data. |
| ARN | The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role that is used to authorize the alert data dumping task. Contact the organization administrator of your level-1 organization to grant the required permissions to the RAM role. Then, enter the ARN of the RAM role. |
| Region | The ID of the region in which the data center of the alert service resides. |
| Organization | The destination organization to which you want to dump the alert data. The required resources such as SLS projects are created in this organization. If a resource with the same name already exists, make sure that the selected organization is granted the necessary permissions to access the resource. |
| Resource Set | The destination resource set to which you want to dump the alert data. The required resources such as SLS projects are created in this resource set. |

**What to do next**

| Operation | Procedure |
|---|---|
| Disable data dumping | 1. In the Basic configuration section of the Alarm data TTL tab, click the icon next to Data Dump to turn off Data Dump. 2. In the message that appears, click OK. Note After you turn off Data Dump, new alert data is no longer synchronized to SLS at the tenant side. However, the alert data that has been dumped is not affected. |
| View data dumping configurations | 1. In the Basic configuration section of the Alarm data TTL tab, click View Configuration next to Data Dump. 2. In the message that appears, view data dumping configurations. |

##### 4.2.3.2 Alert templates

For Ant Financial Service products that are deployed on the PaaS platform, you can upload alert templates to configure or modify the rules that are used to trigger alerts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Alert Templates**.
4. In the upper-left corner of the page that appears, select a service from the **Service** drop-
down list. You can view detailed information about the service in the lower part of the page. Then, click the template in the Associated Template column to view detailed information about the template.
5. Download alert templates.

> **Note:** For Ant Financial Service products that are deployed on the PaaS platform, use the simple_template.json template.

6. Find the service that you want to manage and click **Import** in the **Operation**. In the
**Import Templates** dialog box, click **Upload and Parse File**. Select the template and click
**Open**. After the template is uploaded, click **OK**.

> **Note:** You can also export alert templates.

##### 4.2.3.3 Alert notification

The alert notification feature allows you to configure alert notification channels and then push alerts to O&M engineers.

**Create a subscription**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Alert Notification**.
4. On the **Subscription** tab, click **Create a subscription**. In the dialog box that appears,
configure parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Channel name | The name of the subscription channel. |
| Subscription language | The language in which you want to receive notifications. Valid values: Chinese and English. |
| Subscription region | By default, the region where the subscription resides is displayed. |
| Severity of Alerts to Push | The severity of alerts that you want to push. You can select multiple values. |

| Push protocol | The protocol that is used to push alerts. OnlyH TTP is supported. |
|---|---|
| Push interface address | The IP address of the push interface. |
| Push interface port | The port number of the push interface. |
| Push interface URL | The URL of the push interface. |
| Push request method | The request method that is used to push alerts. Only theP OST method is supported. |
| Push cycle (minutes) | The interval at which alerts are pushed. Unit: minutes. |
| Number of alerts pushed at a time | The number of alerts that are pushed each time. |
| Push mode | The mode in which alerts are pushed. Valid values: ALL: All alerts are pushed in each push cycle. TOP: Only high priority alerts are pushed in each push cycle. |
| Custom channel fields (JSON format) | The push receiver can use this field to customize an identifier. The field must be in the JSON format. |
| Push switch | Specifies whether to push alerts. If you do not turn on the push switch in the Create a subscription dialog box, you can enable the push feature by turning on the switch in the Push switch column after you configure the subscription channel. |

5. After you configure the push channel and turn on the switch, click the **Push** tab to view the
push records.

**Related operations**

**Modify notification channel settings**

1. Find the notification channel that you want to manage, and click **Modify** in the **Operation**
column.
2. In the dialog box that appears, modify the parameters and click **OK**.

> **Note:** Turn on or turn off the switch in the **Push switch** column to enable or disable the notification channel.

**Check the connectivity of a notification channel**

Find the notification channel that you want to manage and click **Test** in the **Operation** column to check the connectivity of the notification channel.

**Delete a notification channel**

1. Find the notification channel that you want to delete, and then click **Delete** in the
**Operation** column.
2. In the dialog box that appears, click **OK**.

##### 4.2.3.4 Alert masking

The alert masking feature allows you to mask alerts reported during a specific period of time, and mask alerts by product, cluster, service, service role, and machine. You can also mask alerts by alert ID.

**Prerequisites**

The permissions on the alert masking menu are obtained.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Alarm Management** > **Alert**
**Settings**.
3. In the left-side navigation pane, choose Alarm Settings > **Alarm Shielding**.
4. In the upper-left corner of the page, click **Create masking rules**. In the panel that
appears, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Rule creation method | The method to create the alert masking rule. Valid values: Filter creation: If the alert data is associated with a configuration management database (CMDB), we recommend that you use the filter creation method to ensure the validity of the alert masking rule. Manually create: If the alert data of the alerts pushed from alert sources is not associated with a CMDB, you can manually create an alert masking rule. For example, three-party hardware device alerts directly pushed from three-party alert sources are not associated with a CMDB. The alert data includes resource ownership and alert objects. |
| Alert item ID | Optional. The ID of the alert item to which the alert to be masked belongs. |
| Alarm Level | Optional. The level of the alert to be masked. Valid values: P1: critical P2: major P3: minor P4: info |

| Alert Source | Optional. The source of the alert to be masked. |
|---|---|
| Resource ownership | This parameter takes effect only when you set the Rule creation method parameter to Filter creation. Optional. The name of the product to which the alert to be masked belongs. |
| Cluster | This parameter takes effect only when you set the Rule creation method parameter to Filter creation. Optional. The name of the cluster to which the alert to be masked belongs. |
| Service | This parameter takes effect only when you set the Rule creation method parameter to Filter creation. Optional. The name of the service to which the alert to be masked belongs. |
| Server Role | This parameter takes effect only when you set the Rule creation method parameter to Filter creation. Optional. The server role of the alert to be masked. |
| Machine | Optional. The hostname of the Elastic Compute Service (ECS) instance to be masked. |
| Masking period | Optional. The time period during which the alert to be masked occurs. |
| Block Reason | Required. The reason for masking the alert. |
| Effective status | Required. Specifies whether the alert masking rule takes effect. |

**What to do next**

| Operation | Description |
|---|---|

| View alert masking rules | You can view the details of created alert masking rules in the following columns: Resource attribution, Service/Service Role, Cluster/Machine, Alert item ID, Alert level, Alarm source, Shielding time period, Effective status, Rule Source, and Block Reason. You can also click Advanced Filter and then configure the Resource attribution, Cluster, Services, Service role, and Machine parameters to filter rules. |
|---|---|
| Modify an alert masking rule | Note The built-in alert masking rules cannot be modified. 1. Find the alert masking rule that you want to modify and clickE dit in the Actions column. 2. In the panel that appears, modify the parameters and clickO K. |
| Delete an alert masking rule | 1. Find the alert masking rule that you want to delete and clickD elete in the Actions column. 2. In the message that appears, click OK. |

| Import an alert masking rule | 1. In the upper-left corner of the Alarm mask page, clickI mport masking rules. 2. In the dialog box that appears, click Download the mask rule Template. 3. Open the masking rule template on your local device, specify the parameters in the template, and then save it. The following table describes the parameters in the template. Resource attribution: the product on which the alert masking rule takes effect. The value is the same as the corresponding product name in CMDB. Example: ecs and edas. If the alert masking rule takes effect on all products, set this parameter to All. Services: the service on which the alert masking rule takes effect. The value is the same as the corresponding service name in Apsara Infrastructure Management. Example: ecs-houyi. If the alert masking rule takes effect on all services, set this parameter to All. Service role: the server role on which the alert masking rule takes effect. The value is the same as the corresponding server role name in Apsara Infrastructure Management. Example: Apiserver#. If the alert masking rule takes effect on all server roles, set this parameter to All. Cluster: the cluster on which the alert masking rule takes effect. The value is the same as the corresponding cluster name in Apsara Infrastructure Management. Example: ECS-CLOUDOPS-A-010c. If the alert masking rule takes effect on all clusters, set this parameter to All. Machine: the hostname of the machine on which the alert masking rule takes effect. Example: a36a06002.cloud.a06.amtest11. If the alert masking rule takes effect on all machines, set this parameter to All. Alarm ID: the ID of the alert item. If the alert masking rule takes effect on all alert items, set this parameter to All. Alert level: Valid values: 1, 2, 3, and 4. Separate multiple values with commas (,). Example: 1,2. Alarm source: the source of the alert to be masked. Example: tianjimon. Shielding time period: the time period during which the alert to be masked occurs. By default, the value is in UTC+8. Example: 2024-04-03 02:02:02-2024-04-03 02:02:02. Effective status: the status of the alert masking rule. Valid values: Y and N. A value of Y indicates that the rule takes effect. A value of N indicates that the rule does not take effect. ShieldReason: the reason why you want to mask the alert. 4. In the Import masking rules dialog box, click Upload files. 5. Select the saved template, click Open, and then click OK. |
|---|---|

##### 4.2.3.5 Masked alerts

You can view details of masked alerts and the associated alert masking rule.

**Prerequisites**

The permissions to view masked alerts are obtained. At least one alert masking rule is created and the rule is effective.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Blocked Alerts**.
On the page that appears, the following information of the masked alerts is displayed:
**Alert ID**, **Alert resources**, **Alert level**, **Alert message**, **Resource attribution**, **Alert**
**Time**, **Alert source**, and the associated masking rule.
4. Enter a keyword to search for alerts. Fuzzy search is supported. You can also click
**Advanced Search** and filter alerts by **Alert ID**, **Alert level**, **Resource attribution**, **Alert**
**Time**, or **Alert source**.
5. Move the pointer over **Details** in the **Alert resources** column of an alert to view the alert
details, including the product, cluster, service, server role, and host.
6. Find the alert that you want to manage and click **Masking rule** in the **Operation** column.
A dialog box appears. If the masking rule is not deleted, the details of the masking rule are displayed in the dialog box. If the masking rule is deleted, message **Masking rule has been deleted** appears.

##### 4.2.3.6 Alert rule settings

This topic describes how to modify the settings of an alert rule, including the status and triggering conditions of an alert rule, and the number of times an alert rule is triggered. Compared with alert templates that have a complicated modification process, the alert rule setting feature allows you to view alert rule settings in an efficient manner and modify the settings of alert rules with a few clicks.

**Background information**

Alert rules can be configured for only TianjiMon. Only alert rules that contain numbers can be modified. After a verified alert rule takes effect, all alerts that use the rule are affected. If the settings of an alert rule are improperly modified, risks may occur. The risks include a surge in the number of alerts and no generated alerts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Alert Rule Settings**.
4. Click **Advanced Filter** to filter alert rules by **Metric Name**, **Product**, **Cluster**, **Service**,
and **Rule Effectiveness**. The following table lists the parameters of alert rules.

| Parameter | Description |
|---|---|
| Product | The product for which the alert rule is configured. |
| Cluster | The cluster for which the alert rule is configured. |
| Service | The service for which the alert rule is configured. |
| Associated Template | The template with which the alert rule is associated. |
| Metric Name | The name of the metric for which the alert rule is configured. |
| Alert Name | The name of the alert. |
| Alert Trigger Rule | The conditions that are used to trigger the alert rule. |
| Detection Cycle (seconds) | The interval at which the alert rule is executed. Unit: seconds. |
| Last Modified At | The time when the alert rule was last modified. |
| Rule Effectiveness | The status of the alert rule. Valid values: Effective, Ineffective, and Verifying. |
| Indicates whether the rule is enabled | Indicates whether the alert rule is enabled. Valid values: Enabled and Disabled. |

5. Find the alert rule that you want to manage and click **Modify Alert Rule** in the **Operation**
column. In the dialog box that appears, modify the following parameters based on your business requirements and then click **Save and Verify**.

| Parameter | Description |
|---|---|

| Enable or Not | Specifies whether to enable the alert rule. |
|---|---|
| Alert Severity | The alert level. |
| Number of times the event is triggered | The number of times that the alert is triggered. |
| Trigger Rule | The alert triggering rule. To prevent the alert rule from becoming invalid, you can change only thresholds and can enter only numbers, including integers and decimals. |

> **Note:** After you modify the rule, the verification takes 3 to 5 minutes. Refresh the list to check whether the rule has taken effect.

6. In the upper-left corner of the Alert Rule Settings page, click **Export** to export alert rules
that are displayed on the page.

### 4.3 Inspections

This topic describes the features related to inspection management.

**Features**

In the Apsara Uni-manager Operations Console, you can perform quick inspections in various inspection scenarios to help maintain the health of your business system and cloud services.

| Feature | Description |
|---|---|
| All inspections | Multiple inspection scenarios are supported, including preset inspection scenarios and custom inspection scenarios. |
| Inspection dashboard | You can view statistics on executed inspection scenarios over a period of time. |
| Inspection settings | You can configure custom inspection scenarios to make inspections more efficient. |
| Inspection records | You can view all inspection records and the corresponding inspection reports. |
| Inspection notifications | You can configure how you want to receive inspection reports and notifications. |

#### 4.3.1 All inspections

This topic describes the inspections supported by the system in various scenarios. These inspections can help maintain the health of your business system and cloud services. You can perform inspections based on your business requirements.

**Prerequisites**

The system administrator permissions of the Apsara Uni-manager Operations Console are obtained. Custom inspection settings are configured before you enable a custom inspection. For more information, see Inspection scenario configuration.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Inspections** > **All Inspections**.
3. Select an inspection scenario. The system supports quick checks for a variety of inspection
scenarios, including preset scenarios and custom scenarios?. After you select an inspection scenario, you can view the inspection items of the selected scenario. Move the pointer over **Inspection parameters** in the **Operation** column to view the inspection parameters. Move the pointer over **Inspection content** in the **Operation** column to view the inspection content.
4. Click **Immediate inspection**. If you want to receive inspection notifications, click Click to
configure your email information on the Inspection notice page. Then, click **Execute** to trigger an inspection. You can configure multiple email addresses. Separate email addresses with semicolons (;). If you are prompted that notifications cannot be sent because notification channels are not configured, you can configure a notification channel on the
**Inspection notice**page. If you do not want to receive notifications, you can
directly click **Execute**to trigger an inspection.
5. Wait for the inspection to complete. The progress is displayed on the page. If you want to
terminate the inspection, click **Termination**. In the message that appears, click
**Termination**.
6. After the inspection is complete, view the inspection results.
In the upper part of the page, view basic information such as **Inspection scenario**,
**Start execution**, **End execution**, **Initiator**, **Execution Policy**, and **Result**
**suggestion**.
In the **Inspection overview** section, you can view the inspection pass rate, number of inspected items, number of failed items, number of errors, number of warnings, and number of passed items. Click the data corresponding to an inspection status to view the detailed inspection results of that status. In the **Overview of inspection results completed** section, you can view the inspection results of each inspected service, including the number of errors, number of warnings, and number of passed items. You can click a service to view its inspection result in detail. In the lower part of the page, you can click **Advanced Filter** to view inspection results by **Inspection item type**, **Inspection Status**, **Inspection item name**, and **Inspection**
**item description**.
You can move the pointer over **Inspection parameters** in the **Operation** column of an inspection item to view its inspection parameters. You can move the pointer over **Inspection content** in the **Operation** column of an inspection item to view its inspection content. You can click a number in the **Inspection results** column of an inspection item to view the result in detail in the dialog box that appears. You can click **View report receiving mailbox** in the upper-right corner to view the email address that receives the inspection report. You can click **Export Report** in the upper-right corner to download the inspection report to your on-premises computer.

> **Note:** You can export inspection reports in the JSON format or as an Excel table.

**Related operations**

**Perform a scheduled inspection**

1. Select an inspection scenario and click **Scheduled inspection**.
2. Configure the following parameters and click **OK**. Inspections are performed based on the
schedule that you configure.

| Parameter | Description |
|---|---|
| Email settings | Enter the email address that you want to use to receive inspection notifications. You can enter multiple email addresses. Separate the email addresses with semicolons (;). |

| Timing Rule settings | Click Add effective time period and set Effective time and Effective period. Note To delete an effective time and period, click . |
|---|---|

#### 4.3.2 Inspection dashboard

This topic describes how to view statistics on executed inspection scenarios over a period of time.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Inspections** > **Inspection**
**Dashboard**.
3. In the upper-right corner of the page, use the **Time range** drop-down list to specify the
time range to view inspection statistics. You can select **Nearly seven days**, **Nearly a**
**month**, or **Nearly three months**.
4. View the statistics. The page consists of the following sections:
**Inspection task statistics**: You can view statistics on executed inspection tasks in
different states, including **Running**, **Successful Execution**, and **Execution failed**.
**Inspection Result Statistics**: You can view statistics on different results, which fall into
the following categories: **Number of errors**, **Number of warnings**, and **Normal**
**number**.
**Execution top 5-inspection type dimension**: You can view the top five inspection
types in terms of errors and warnings and view the corresponding numbers.
**Exception top 5-inspection subtype dimension** : You can view the top five inspection
subtypes in terms of errors and warnings and view the corresponding numbers.
**Historical trend of inspection execution**: You can select an inspection scenario from
the **Inspection scenario** drop-down list and view the following trends of the scenario:
**Inspection item execution error**, **Inspection item execution warning**, and **The**
**inspection item is executed normally**. You can also move the pointer over a time
node to view the recorded data.

#### 4.3.3 Inspection scenarios

This topic describes how to configure custom inspection scenarios and inspection items to make inspections more efficient.

**Create an inspection scenario**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Inspections** > **Inspection**
**Settings**.
3. On the **Inspection scenario** tab, click **Create a new inspection scenario**. Then
configure the following parameters and click **Submit**.

| Parameter | Description |
|---|---|
| Scene name | Enter a name for the custom inspection scenario. |
| Scenario description | Enter a description for the custom inspection scenario. |
| Configure inspection items | Select inspection items for the custom inspection scenario. After you select inspection items, the details of the inspection items are displayed in the lower part. You can move the pointer over Inspection parameters in the Operation column of an inspection item to view its inspection parameters. You can move the pointer over Inspection content in the Operation column of an inspection item to view its inspection content. You can click Delete in the Operation column of an inspection item to delete the inspection item. |

**Related operations**

**View the details of an inspection scenario**

1. Click **Advanced Filter**. Then, you can filter inspection scenarios by **Inspection scenario**
**name**, **Inspection scenario description**, **Preset or not**, and **Creation time**.
2. Click **Details** in the **Operation** column of the desired inspection scenario.
3. On the **Scenario details** page, view the **Scene name**, **Scenario description**, **Configure**
**inspection items**, and a list of selected inspection items.

**View inspection items**

1. On the **Inspection items** tab, you can view all inspection items.
2. Click **Advanced Filter**. Then, you can filter items by **Inspection item type**, **Inspection**
**item subtype**, **Inspection Method**, **Inspection item name**, **Inspection item**
**description**, and **Preset or not**.
You can move the pointer over **Inspection parameters** in the **Operation** column of an inspection item to view its inspection parameters. You can move the pointer over **Inspection content** in the **Operation** column of an inspection item to view its inspection content.

**Edit an inspection scenario**

> **Note:** Preset inspection scenarios cannot be modified.

1. Find the inspection scenario that you want to modify and click **Edit** in the **Operation**
column.
2. In the dialog box that appears, modify the parameters and click **OK**.

**Delete an inspection scenario**

> **Note:** Preset inspection scenarios cannot be deleted.

1. Click **Delete** in the **Operation** column of the desired inspection scenario.
2. In the dialog box that appears, click **OK**.

**Import an inspection data package**

1. In the upper-right corner of the page, click **Import inspection packets**.
2. In the dialog box that appears, click **Select File**, select the inspection package, and then
click **Open**.
3. In the **Import inspection packets** dialog box, click **Upload** to import the inspection
package. After the inspection package is imported, inspection items of the related product are updated. You can use this feature to improve the inspection capabilities of the platform.
4. Move the pointer over **View** below **Import inspection packets** to obtain the version
information of the package.

#### 4.3.4 Inspection records

The Inspection Records page records all inspection operations performed by a user. You can filter inspection reports and view the report of a specific inspection task.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Inspections** > **Inspection**
**Records**.
3. View all inspection records. You can also click **Advanced Filter** to filter inspection records
by **Inspection scenario**, **Preset or not**, **Task Status**, **Start execution time**, and **End**
**execution time**.
4. Find the inspection record that you want to view and click **Inspection Report** in the
**Operation** column. On the **Inspection Report** page, you can view the detailed inspection
report.

> **Note:** If the **Execution status** column of an inspection record displays **Canceled** or **Failed**, you cannot view the report of the inspection record.

5. On the **Inspection Report** page, you can view all recent inspection reports. By default, the
system displays the inspection report of the most recent inspection. You can also filter inspection reports by time after the inspection scenario.
6. In the upper part of the page, view basic information such as **Inspection scenario**, **Start**
**execution**, **End execution**, **Initiator**, **Execution Policy**, and **Result suggestion**.
7. In the **Inspection overview** section, you can view the inspection pass rate, number of
inspected items, number of failed items, number of errors, number of warnings, and number of passed items. Click the data corresponding to an inspection status to view the detailed inspection results of that status.
8. In the **Overview of inspection results completed** section, you can view the inspection
results of each inspected service, including the number of errors, number of warnings, and number of passed items. You can click a service to view its inspection result in detail.
9. In the lower part of the page, you can click **Advanced Filter** to view inspection results by
**Inspection item type**, **Inspection Status**, **Inspection item name**, and **Inspection**
**item description**.
You can move the pointer over **Inspection parameters** in the **Operation** column of an inspection item to view its inspection parameters. You can move the pointer over **Inspection content** in the **Operation** column of an inspection item to view its inspection content. You can click a number in the **Inspection results** column of an inspection item to view the result in detail in the dialog box that appears.
0. You can click **View report receiving mailbox** in the upper-right corner to view the email
address that receives the inspection report.
1. You can click **Export Report** in the upper-right corner to download the inspection report to
your on-premises computer.

> **Note:** You can export inspection reports in the JSON format or as an Excel table.

#### 4.3.5 Inspection notifications

This topic describes how to configure an email address to receive inspection notifications.

**Prerequisites**

The ANS component is added and a notification channel is configured.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Inspections** > **Inspection**
**Notifications**.
3. In the **Inspection notice** section, click **Configuration**.
4. In the dialog box that appears, configure the **Token** parameter and click **OK**.

**Related operations**

**Update an email address**

1. In the **Inspection notice** section, click **Update**.
2. Update the **Token** parameter and click **OK**.

**Disable a notification channel**

1. In the **Inspection notice** section, click **Close**.
2. In the message that appears, click **OK**.
After you disable a channel, the configured email address is cleared, and inspection results are no longer sent by using the channel.

### 4.4 Event Center

Event center is an event management platform for Apsara Stack and allows you to manage alerts for cloud applications and grade the alerts in a centralized manner. The event center can classify, merge, and grade multiple types of alerts to effectively convert the alerts into events for you to handle and manage. This helps improve the O&M efficiency for Apsara Stack.

**Modules**

| Module | Description |
|---|---|
| Event List | You can obtain and manage events of various levels. For example, you can view details of an event and handle the event. |

| Event Grading | An event grading policy is a set of configurations that convert Apsara Stack alerts into events. Each cloud service has its own event grading policy. |
|---|---|
| My Events | A quick portal that allows you to handle events on theT o be handled by me and I participated in tabs. |
| Event Chart | You can view the information about all cloud platform resources from the cloud service perspective, including the total number and status of cloud service components, the total number of event services, and service event traces. |
| Configuration Management | You can configure O&M modes, service importance level mappings, and event causes in a centralized way. |

#### 4.4.1 Event list

The event list feature is a tool that converges alert data. This allows you to use custom rules to classify and manage alert data, and generate emergency events. On the Event List page, you can query and handle events of various levels in a centralized manner. For example, you can view the details of an event and handle the event.

**Usage notes**

Event Center serves as a tool only for managing alert information about cloud services. You can determine the importance of alert information based on your business requirements. You can also view preset grading rules at the earliest opportunity and go to the Event Grading page to configure custom rules based on your business requirements. Pay attention to the alert information. To help you better perform risk monitoring and emergency response, Alibaba Cloud provides Event Center to manage alert information. This tool uses custom rules to converge, merge, and comprehensively grade all alert information in the Alerts module to generate emergency events. You can configure event grading rules based on the following logic: You can specify importance levels for cloud services. The alerts of key cloud services generate events of a higher level. Events can be graded based on the alert levels of cloud services, the proportion of abnormal instances, and the highest level among multiple alert levels. The alert information of cloud services is graded by instance and instance cluster. Instances include service instances, work software, management software, and worker nodes. Events are classified into the following levels: L1: critical events. When a critical event occurs, the overall features of a cloud platform become unavailable. L2: major events. When a major event occurs, the overall features of a cloud service become unavailable, and a wide range of related hardware and software resources, cloud service instances that are provided, and dependent service instances are abnormal. L3: significant events. When a significant event occurs, the overall features of a cloud service are abnormal, and the overall features of a worker service role cluster are abnormal, or some dependent service instances are abnormal. L4: general events. When a general event occurs, global exceptions occur in the control service of a cloud service, or a few exceptions occur in worker clusters or dependent service instances. L5: routine events. When a routine event occurs, exceptions occur in a single cloud service instance, work software instance, work resource node, or management software instance. Handle the routine event at the earliest opportunity.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **Event List**.
3. By default, the Event List page displays events whose **Event Level** is L1, L2, L3, L4, or L5
and **Processing Status** is **Pending response** or **Processing**. By default, events in the list are displayed in descending order of start time. The most recent event is displayed at the top of the list. In the upper-right corner of the event list, you can click the icon to adjust the columns to display and their display order.
4. To find the event that you want to view, filter the event list by selecting one or more values
from the **Event Level** and **Processing Status** drop-down lists.You can also click
**Advanced Filter** and filter the event list by **Event ID**, **Event title**, **Event description**,
**Start time**, **Recovery time**, **component**, **service**, **cluster**, and **product**.
5. Click the event title to go to the event details page.
In the upper-right corner of the page, click the icon to copy the page URL. In the upper-right corner of the page, click **Mark** to classify and mark events.

> **Note:** You can mark events that are in the Pending response and Processing states. You can repeatedly mark events to overwrite the last mark.

a. Click **Mark**. In the Classification mark dialog box, configure the following parameters: Valid: specifies whether the event is valid. Valid values: Valid and Invalid. Cause of the event: the event cause that you specify when you close the event.

> **Note:** If your event cause is unavailable in the drop-down list, you can configure the event cause on the Configuration Management page in Event Center. For more information, see Configuration Management.

Reason for details: the detailed reason for closing the event. b. Click Confirm. After the event is marked, you can view the mark content on the event details page. In the upper-right corner of the page, click **Response** to respond to the event or to close the event. Respond to the event: Click Response and select **Response event**. Then, the event enters the Processing state. Close the event: Click Response and select **Direct statement**. In the dialog box that appears, configure the parameters and click Confirm. Then, the event enters the Closed state. After you respond to an event, you can **transfer** or **close** the event. On the **Event Details** tab, you can view the event details in sections, such as **Basic**
**properties**, **Event handling**, and **Associated subevents**.
In the **Associated subevents** section, you can perform the following operations: In the upper-right corner, select the check box to view only the events that are in the **Alarming** state. Find the sub-event that you want to view and click the value in the **Title** column. In the panel that appears, you can view the sub-event details on the
**Details**, **Alarm history**, and **Original information** tabs. Click **View ASO**
**alerts** to go to the **Alert Details** page and view the alert details.
In the **Event trajectory** panel, you can view all trajectory information that is recorded from the start time to the end time of the event.

**What to do next**

**Export a report**

Click **Report export** above the event list to export the event data to your on-premises device.

**Respond to multiple events at a time**

Select the events that you want to manage and click **Batch response** below the event list. In the message that appears, click OK.

**Close multiple events at a time**

1. Select the events that you want to manage and click **Batch order closing** below the event
list.
2. In the dialog box that appears, configure the following parameters and click **Confirm**.

| Parameter | Description |
|---|---|
| Valid | Specifies whether the event is valid. Valid values: Valid Invalid |
| Cause of the event | The event cause. |
| Reason for details | The detailed reason for closing the events. |
| Processing result | The processing result for the events. |

#### 4.4.2 Event Grading

An event grading policy is a set of configurations that convert Apsara Stack alerts into events. Event grading policies are classified by cloud service and each cloud service has its own event grading policy.

**Feature overview**

The event grading process consists of the following stages:
1. Alert mapping: Alert levels are mapped to event levels based on the corresponding service
importance levels: A, B, and C. The importance levels are displayed in three columns.
2. Proportion-based correlation: The system merges events of the same instance category to
generate a new event. The levels of events are determined based on the proportion of abnormal instances. The following instance categories are supported: cloud service instances, work and management software instances, and worker node instances.
3. Highest level-based event merging: The system merges multiple events that have the same
event object to generate a new event.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **Event Grading**.
3. In the **Map an Alert to an Event** step, click the desired policy.
i. In the policy details panel, view the details of the event into which the alert is converted. The details include **Basic information**, **Matching Condition**, and **Grading rules**. Move the pointer over the**Note** icon next to the Importance level of cloud product: A, Importance level of cloud product: B, or Importance level of cloud product: C column. The names of services in the non-sales area under the corresponding level are displayed. Click **View Details** to view the importance levels of cloud services. ii. Click **Modify** to modify the event levels that correspond to cloud service importance levels and alert levels. Then, click **Save**.
4. In the **Determine the Level of Instance-grade Events** step, click the desired policy.
i. In the policy details panel, view proportion-based correlation details. The details include
**Basic information**, **Matching Condition**, and **Grading rules**.
ii. Click **Modify** to add or remove demarcations between the proportion ranges of abnormal instances. You can also click Modify to change the event level that corresponds to a given abnormal instance proportion range. Then, click **Save**.
5. In the **Finalize the Event Level** step, the system merges sub-events of the same type into
an event. The generated event level is equal to the highest level among all sub-event levels.

> **Note:** The rule in this step is fixed. You do not need to configure the rule.

#### 4.4.3 My events

On the My event page, you can quickly handle events on the **To be handled by me** and **I**
**participated in** tabs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **My Events**.
3. On the **To be handled by me** tab, you can view all events that you need to handle,
including the events that you have actively responded to and the events that are transferred to you from other accounts. i. You can filter the desired event data by using the **Event Level** drop-down list above the event list. ii. You can click the title of an event to view the event details. iii. You can perform the following operations on events.

| Operation | Description |
|---|---|
|   | After you handle events, you can click Statement to close the events. To close a single event, perform the following operations: a. Find the desired event and click Statement in the Operation column. Alternatively, go to the event details page and click Statement in the upper-right corner. b. Configure parameters in the following figure and click Confirm. |

| Close events | To close multiple events, perform the following operations: a. Select the desired events and click Batch order closing below the event list. b. Configure parameters in the following figure and click Confirm. |
|---|---|

| Transfer events | To transfer a single event, perform the following operations: a. Find the desired event and click Transfer in the Operation column. Alternatively, go to the event details page and click Transfer in the upper-right corner. b. Select a value from the Transferred person drop-down list and click Confirm. To transfer multiple events, perform the following operations: a. Select the desired events and click Batch transfer below the event list. b. Select a value from the Transferred person drop-down list and click Confirm. |
|---|---|

4. On the **I participated in** tab, you can view all events that are in the **Processing** or
**Closed** state.
You can filter the event list by **Event Level** and **Processing Status** to obtain the desired events. You can sort the event list by **Event Level**. To obtain event details, find the desired event and click the event title to go to the details page.

#### 4.4.4 Event Chart

You can view all events of the cloud platform from the perspective of cloud services.

**Prerequisites**

By default, the Event Chart module is not displayed. If you want to display the Event Chart module, click **User Authorities** in the top navigation bar. Then, click Menu Management in the left-side navigation pane to configure the related settings.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **General** > **Event Center** > **Event Chart**.
3. View the events of the cloud platform from the perspective of cloud services.
In the upper-right corner of the page, view the total number of product components, the total number of products that trigger events, and the number of products that trigger events at each severity level. View the status of each cloud service component: A blue icon indicates that the event of a product component is normal, whereas an icon with an event severity level indicates that the event of a product component is abnormal. Move the pointer over the icon of a product component to view the associated product components. Click the icon of a product to go to the Event trajectory page.
4. On the Event trajectory page, view the following information:
The number of events for the cloud service and the number of events at each severity level that are displayed in the upper-right corner of the page. The catalog tree of the event trajectory that is displayed on the left side of the page. The details of the event trajectory, including the information about the component architecture, name, quantity, and status, that are displayed on the right side of the page.
5. If a product reports abnormal events, you can perform the following operations. In this
example, Apsara Uni-manager Operations Console is used. i. On the Event trajectory page, click **ASO Exceptions** in the catalog tree on the left, and then click **View details** to go to the event details page. ii. On the event details page, view the basic information about the event, associated events, and emergency responses for the event in the **Basic properties**, **Associated**
**Event List**, and **Emergency handling operation record** sections.
The service resource topologies for only some abnormal events are provided on the page. You can obtain the relevant information based on specific cloud services on the event details page.

#### 4.4.5 Configuration Management

You can configure O&M modes, service importance level mappings, and event causes in a centralized way.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **EventCenter** > **Configuration**
**Management**.
3. You can configure custom settings described in the following table.

| Section | Description | Procedure |
|---|---|---|

| TianjiMon Alert-Product Mappings | Supplements the information of the cloud services that are deployed in TianjiMon in a containerized manner based on namespaces contained in alerts. | i. Click Edit. ii. Click Add below the content list and turn on Whether to enable. iii. Enter corresponding information in the Parameter ID and Parameter Name fields. Note You can click options in the Operation column to delete, move up, or move down the data of the corresponding parameter. iv. After you specify all parameters, click Save. |
|---|---|---|
| CMS Alert-Product Mappings | Supplements the information about the services based on namespaces contained in all CloudMonitor alerts. |   |
| Causes | Provides cause options that you can select when events are resolved and you are to close events. |   |
| Product Importance Level Mappings | Defines the importance levels of cloud services to affect the final severity levels of events. | i. Click Edit. ii. In the Content List section, configure importance levels for cloud services. Note You can define an importance level for each cloud service. New events are graded based on the importance levels of corresponding services. The importance levels include A, B, and C, which decrease in order. iii. Click Save. |

| CMS Alert Contact Extraction Rules | Parses the specified fields from original CMS alerts to obtain alert contact information. | i. Click Edit. ii. Click Add below the content list and turn on Whether to enable. iii. Enter corresponding information in the Parameter ID and Parameter Name fields. Note You can click options in the Operation column to delete, move up, or move down the data of the corresponding parameter. iv. After you specify all parameters, click Save. |
|---|---|---|

| AOP O & M mode Important This configuration item can be specified only by the super administrator role of OAM. | The mode switch for integrated O&M of enterprise cloud tenants and platforms. | i. Click Edit. ii. Select an O&M mode. Industry Cloud O&M mode: If the cloud platform builder or O&M operator is not the same as the cloud tenant, industry cloud O&M mode is recommended. In industry cloud O&M mode, O&M operations for cloud platforms are performed in ASO, and O&M operations for cloud tenants are performed in Application Operations Platform (AOP) on the tenant side of ASCM. Enterprise Cloud O&M mode: If the cloud platform builder or O&M operator is the same as the cloud tenant, enterprise cloud O&M mode is recommended. In enterprise cloud O&M mode, you can obtain the O&M data of cloud platforms in the AOP on the tenant side of ASCM to perform global and centralized O&M operations for cloud platforms and cloud tenants. iii. Click Save. |
|---|---|---|

## 5 Platform O&M

### 5.1 Apsara Infrastructure Management

**Management**

#### 5.1.1 Resource management

This topic describes modules related to resource management.

**Modules**

| Module | Description |
|---|---|
| Product & Cluster O&M | Displays all resources from the cloud product dimension, including products, clusters, services, and components. |
| Machine Management | Displays machines and the detailed information about machines. |
| Resource Tags | Displays resources that you add to favorites and allows you to use resource tags to manage resources in a centralized manner. You can bind, query, unbind, modify, and export resource tags on this page. |
| Base Machine Resource Dashboard | Displays the total amount of static resources and resource usage from the machine and product dimensions. |

##### 5.1.1.1 Product & Cluster O&M

The Product & Cluster O&M page displays the status and statistical data of products. The statistical data includes the number of clusters, and the hierarchical relationship between products and their related resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. By default, the **Product & Cluster O&M** page appears.
3. On the **Product & Cluster O&M** page, view product status and cluster status. Statistics of
all products deployed on Apsara Infrastructure Management or the PaaS base are displayed.

| No. | Section | Description |
|---|---|---|
| 1 | Overview section | In this section, you can view the total number of products deployed in the current environment and the number of products in each state. The product state can be Ready or Not Ready. Note A product consists of one or multiple clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. |
| 2 | Projects section | In this section, you can view product names, status, instance status, and inspection alerts in a list. You can select a zone to view products and clusters in the zone. You can also perform a quick search for products or clusters. You can select With Inspection Alerts to view products for which inspection alerts are generated. |

The following table describes the parameters in the list.

| Parameter | Description |
|---|---|
| Product | The name of the product. You can click the icon on the left of the product name or clickS how Clusters in the Actions column to view the clusters of the product. You can modify the aliases of clusters for products deployed on Apsara Infrastructure Management and the PaaS base. |
| Status | The state of the product and clusters. You can click the icon next to Status and select Ready or Not Ready to view resources by status. |

| Instance Status | The instance status. A product consists of one or more clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. This column shows the numbers of clusters, service instances, and components in the Ready state of a product, and the corresponding total numbers. You can click an item to view the names and status of resources at all levels. indicates the Ready state. indicates the Not Ready state. Click Cluster, Service, or Component in the Instance Status column to view the cluster composition of the product. Click a cluster name to go to the Cluster Details page. Click a service name or component name to go to the component details page. Note This design facilitates your checks of Not Ready state changes. For example, you fixed a product that is in the Not Ready state. In this case, you can view whether the product is fixed on the current page without going to the details page. |
|---|---|
| Inspection Alerts | The number of inspection items that the product failed in the last inspection task. - indicates that no inspection task is found. The reason may be zero executed inspection task or query failure. 0 indicates that an inspection task is found and the product passed the inspection. Other numbers indicate the number of inspection items that the product failed. You can click the number to view the failed inspection items. |
| Actions | This column provides the Show Clusters operation. The Show Clusters operation provides a further option: Cluster Details. You can click Cluster Details to go to the Cluster Details page. |

###### 5.1.1.1.1 Cluster details

On the cluster details page, you can view the basic information about a cluster, services in a cluster, machines, desired-state configurations, operation records, and resource details.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. By default, the **Product & Cluster O&M** page appears.
3. Go to the cluster details page by using one of the following methods:
In the Projects list, click **Show Clusters** in the Actions column of a product. All clusters of the product are displayed. Find the cluster that you want to view and click **Cluster**
**Details** to go to the cluster details page.
In the Projects list, click the value in the Instance Status column, and then click the name of the cluster that you want to view to go to the cluster details page.
4. View the details of the cluster.

| Section | Description |
|---|---|
|   | Displays the basic information about the cluster, including the cluster status, product, zone, cluster version, and cluster clone parameters. The aliases of clusters deployed on Apsara Infrastructure Management and the PaaS base can be modified. Note An alias can be 0 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). It cannot _ start with a special character or a digit. Click the Edit icon next to Cluster clone parameters to set the clone mode. In the Modify cluster clone parameters dialog box, you can select True clone or FakeClone. Note True clone: When a machine is added to a cluster, the cloning operation is executed. In the desired-state configuration file, the value of Legacy is False. FakeClone: When a machine is added to a cluster, the cloning operation is skipped. In the desired-state configuration file, the value of Legacy is True. Rolling updates can be triggered if a cluster is deployed on Apsara Infrastructure Management or the PaaS base. Warning The rolling updates are performed on all components of the cluster. The rolling updates will restart the components based on a canary release policy. The rolling feature is typically used to update the service registration variables referenced by a program. You can trigger the rolling updates by performing the following operations based on the location where the cluster is deployed: |

| Basic Information | If the cluster is deployed on Apsara Infrastructure Management, click Cluster Rolling in the upper-right corner of the cluster details page. In the Cluster Rolling dialog box, select Terminate or Do Not Terminate for the Whether to terminate the previous rolling task parameter. You can view the task details on the Action History tab. Note Terminate: If a previous rolling task exists, the previous rolling task is terminated and a new rolling task is generated. Do Not Terminate: If a previous rolling task exists, a new rolling task is queued for execution after the previous rolling task is complete. Warning Risks may arise when you terminate a previous rolling task. Proceed with caution. If the cluster is deployed on the PaaS base, clickC luster Rolling in the upper-right corner of the cluster details page. In the Confirmation message, click OK. Clusters deployed on Apsara Infrastructure Management or the PaaS base can be deleted. Warning Cluster deletion is a high-risk operation. Proceed with caution. Consult the Global Transaction Service (GTS) expert support team before you delete a cluster. You need to set a cluster to the pre-deletion state and then delete the cluster. After a cluster is set to the pre-deletion state, the cluster cannot be modified. a. In the upper-right corner of the page, clickD elete Cluster. The Note dialog box appears. b. In the dialog box, click Go to plan details. |
|---|---|
|   | c. You are navigated to the cluster plan details page. For more information, see Workflow types. Note If the cluster is deployed on Apsara Infrastructure Management, you are navigated to the Plan Details: Offline the onTianji product cluster page. If the cluster is deployed on the PaaS base, you are navigated to the Plan Details: Offline the onPaaS product cluster page. |

| Cluster details | The details of clusters deployed on Apsara Infrastructure Management and the PaaS base are different, as shown in the following table. |
|---|---|

| Base | Paramete r | Description |
|---|---|---|
|   | Services | Displays the services deployed in the current cluster and the service status. Click Details in the Actions column to go to the component details page and view the component details. Click Upgrade in the Actions column to update a service. You can update a service by modifying the version of the service template. Click Unpublish in the Actions column to remove a service from the current cluster. Warning Removing a service is a high-risk operation. Proceed with caution. |
|   | Machines | Displays the machines that can be used by the current cluster and the cluster status. Click View or Critical in the Machine Metrics column to view the details of machine metrics. Machine metrics include component metrics, machine metrics, and system service metrics. You can repair and restart physical machines. Click Terminal in the Actions column to log on to a machine. Click Details in the Actions column to go to the machine details page. |

|   | Machine Group | Displays the planning information between machines and components, such as the role of a machine group, machines contained in the machine group, and components that can use the machine group. Click a machine name in the Associated Machines column to view the machine details. Click a component name in the Associated Components column to view the component details. |
|---|---|---|
|   | Desired State Configura tion | Displays the desired-state configuration file of the cluster. Note The desired-state configuration files of clusters deployed on Apsara Infrastructure Management can be modified. You can view the source of the template above the template file content. Move the pointer over the icon to view the details of the template, such as the version, modification description, modification time, and the person who modifies the template. Click Go to Edit next to the template name to go to the Edit Template page. |
|   |   | Displays the change records of the cluster. Click Task Details in the Actions column to go to the task details page. You can view the task details, including the basic information, related clusters, and changes. The Basic Information section displays the task status, submission time, and submitter. The Related Clusters section displays the cluster, product, status, progress, version, submission time, and operations that can be performed. You can click Build Details or Resource Task Details in the Actions column to view the build details or resource task details. The Change Content section consists of Component Changes and Machine Changes tabs. |

| Apsara Infrastr ucture Manag ement |   | On the Component Changes tab, you can terminate, retry, or suspend a task. Click Details in the Actions column to view the task progress of a component. Overview Information: displays the basic information about the component, including Commit Id, Rolling Status, Approval Policy, and Upgrade Plan. In the upper-right corner of the dialog box, click View Details to go to the Rolling Summary page and view the component update details. Go to the Rolling Summary page. In the Overview Information section, you can retry, terminate, or suspend a task. You can perform these operations only on unfinished tasks. The system can monitor and display the service level agreement (SLA) changes. You can view the real-time monitoring status of components. Click View Logs to view SLA monitoring logs. Click Modify SLA Configuration to modify the SLA configuration. |
|---|---|---|
|   | Action History | Note You can view the SLA-related content of services for which the SLA feature is enabled. Click View All to view the component update details. Click Edit Parameter to modify the relevant parameters. Only the parameters for unfinished tasks can be modified. In the Instance Details section, you can add multiple component tasks to the blacklist. Instance Details: displays information such as the change status of component instances, component actions, and metrics. On the Machine Changes tab, you can view the machine name, change type, and status. Click Terminal in the Actions column to go to the logon page and log on to a machine. Click Details in the Actions column to go to the Machine Overview page and view the machine details. Note The Machine Changes tab is displayed only when the value in the Change Type column is Machine Scale-out, Machine Scale- In, Component Scale-out, or Component Unpublishing. Go to the Machine Overview page, which consists of the Basic Information and Details sections. |

|   |   | Basic Information: displays information such as the change status, machine status, machine actions, clusters, and machine metrics. Details: consists of Add to Cluster, Clone, and Deploy Component Instances. Add to Cluster: displays the cluster where the machine resides and the cluster to which you want to add the machine, as shown in the preceding figure. Status: the state of the machine change. Valid values: Failed: The change failed. Cancel: The change task is canceled. For example, the machine scale-in task is submitted when the machine scale-out task is not complete. Doing: The change is in progress. Waiting: The change is waiting to be performed. Done: The change is complete. Current Cluster: the cluster where the machine resides. Destination Cluster: the cluster to which you want to add the machine. Clone: indicates whether the cloning operation is executed when a machine is added to a cluster. The Real Clone and Pseudo-clone modes are provided. Pseudo-clone: The cloning operation is skipped when a machine is added to a cluster. Real Clone: The cloning operation is executed when a machine is added to a cluster. Click Metric. In the dialog box that appears, view the metric details on the Component Metrics, Machine Metrics, and System Service Metrics tabs. Status: For more information, see the status in the Add to Cluster section. System Service: the server role that is relevant to the cloning operation. Current Version: the current version of the server role on the machine. Desired Version: the version of the server role that you want to update to. |
|---|---|---|

|   |   | Deploy Component Instances: displays the components that are deployed on a machine after the machine is added to a cluster. Component: the name of the component. Service: the service to which the component belongs. Status: For more information, see the status in the Add to Cluster section. Click Details in the Status column to view the deployment status of a component. Click View in the Metric column. In the Metric Details dialog box that appears, view the metric details on the Component Metrics, Machine Metrics, and System Service Metrics tabs. Version Current: the current version of the server role on the |
|---|---|---|
|   | Resource Details | machine. Displays the resoDurecseirse rde: qtuh es vt edrs bioyn c oofm thpeo ns enrvtse ri nr otlhee t hclauts yteoru. want to update to. Click Related Version in the Actions column to view the related Creliscoku Vrceer svieornsi oDnisf.ferences in the Actions column to go to the Version Differences page and view the differences between configuration files |
|   | Test Report | of different versions. Displays the test reports of services in the cluster. Click Details in the Actions column to view the details of failed cases, succeeded cases, and skipped cases. |
| PaaS | Services | Displays the services deployed in the current cluster and the service status. Click Details in the Actions column to go to the component details page and view the component details. |
|   | Desired State Configura tion | Displays the desired-state configuration file of the cluster. |

|   | Action History | Displays the change records of the cluster. Click Task Details in the Actions column to view the task details. The Base Info section displays the basic information such as task status, task ID, task message, and start time. The Subtask List section displays the information such as subtask ID, description, status, change object, and execution method. Click Show Parameters in the Actions column to view the task parameters. Click Yaml in the Actions column to view the configuration file. Note Cluster changes mainly refer to the desired state changes, excluding machine operations such as machine repairs in the cluster. |
|---|---|---|
|   | Resource Details | Displays the resources requested by components in the cluster. |

###### 5.1.1.1.2 Component details

This topic describes how to view the basic information and details of components.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. By default, the **Product & Cluster O&M** page appears.
3. Go to the component details page by using one of the following methods:
In the Projects list, click the value in the Instance Status column, and then click the name of the component or service that you want to manage to go to the **component details** page. On the **Services** tab of the **Cluster Details** page, click the name of the service that you want to manage to go to the **component details** page.
4. View the details of a service component. The following figure shows an example.

| No. | Section | Description |
|---|---|---|
| 1 | Components | Displays the list of service components. Click a component to view the basic information and details of the component in the right-side section. |
| 2 | Basic component information | Displays the name, version, status details, and information about the component. Click Component Rolling in the upper-right corner of the page to perform a rolling update on the component. This feature is available for components deployed on the PaaS base. |
| 3 | Component details | Displays the details of the component. The details of components deployed on Apsara Infrastructure Management and the PaaS base are different, as shown in the following table. |

Details of components deployed on Apsara Infrastructure Management and the PaaS base

| Base | Parameter | Description |
|---|---|---|

|   | Instances | Displays the status of the component deployed on the machine, including the version alignment, action in progress, and machine status. Note Version misalignment indicates that the current version is inconsistent with the version set in the desired-state configuration file. This occurs when the version is being updated, fails to be updated, or is to be updated. In the last case, the version specified in the desired-state configuration file is changed, but the component has not been updated. Click Diagnose in the Actions column. Apsara Infrastructure Management diagnoses the causes for version misalignment or the status not being Good. Note Diagnose is displayed only when version misalignment occurs or the value of Status is not Good. Choose Component Information > Metrics in the Actions column to view the details of component metrics, machine metrics, and system service metrics. Choose Component Information > Applications in the Actions column to view the applications and application versions of the component deployed on the machine. Note tianji config is an application that indicates the _ _ configuration file delivered to the machine. The version of tianji config can be used as the version _ _ number of the configuration file. If the configuration file changes, the version number changes. Other applications are user programs. Choose Component Information > Status Details in the Actions column to view the detailed status of the component, such as the status description. Click Terminal in the Actions column to go to thel ogon page and log on to the machine. Choose Actions > Restart in the Actions column to restart the application processes of the component. |
|---|---|---|
|   | Change History | Displays the change tasks related to the component. Click Details in the Actions column to go to the Task Details page and view the task details. |

| Apsa ra Infra struc ture Mana gem ent |   |   |
|---|---|---|
|   | Desired State Configurat ion | Displays the desired-state configurations of the component, including the specialized files. You can modify the desired-state configurations of the component. Note You can view the source template information about a template file above the file content. Move the pointer over the icon to view the details of the template, such as the version, modification description, modification time, and the person who modifies the template. Click Go to Edit next to the template name to go to theE dit Template page. |
|   | Registrati on Variables | Displays the registration variables of the component. The variables can be used by other components, such as the endpoint of a program. |
|   | Resources | Displays the information about the resources requested by the component. Click Related Version in the Actions column to view the related versions of the resource. |
|   | Dependen cy Status | Displays the dependencies of the components. A component depends on the component or components on its right. The following figure shows the component dependencies by using arrowed lines. Display Mode: supports All Components and Not Ready Components. All Components: displays all components in the dependency tree. Not Ready Components: displays the nodes that do not reach the desired state and their leaf nodes in the dependency tree. If all nodes reach the desired state, only the direct dependencies of the root node are displayed. Display Dependency: supports Strongly Dependent and Weakly Dependent. Strongly Dependent: If the dependencies are not ready, the current component cannot be started. Weakly Dependent: If the dependencies are not ready, the current component is still started. However, some features may be affected. |

| PaaS | Workload | Displays the basic workload information about the component. For Deployments, StatefulSets, and DaemonSets workloads, the page displays information about the pods requested by the workloads, and you can log on to the containers deployed on the pods. Click View YAML in the Actions column to view the original configuration and running information about the workload. Click the icon to show the pod list. You can view the key information about each pod in the cluster, including the status, name, container, node name, and namespace. Click Pod Performance Data in the Actions column to view the pod performance data. Click Describe in the Actions column to view the configurations, status, and properties of the pod. Click Terminal in the Actions column to go to the logon page and log on to the machine. Click View Logs in the Actions column to view the logs that are exported from containers deployed in the pod to stdout. |
|---|---|---|
|   | Instances | Displays the pods requested by the workload and the status of Kubernetes nodes. Click Terminal in the Actions column to log on to the machine. |
|   | Desired State Configurat ion | Displays the desired-state configurations of the component. |
|   | Registrati on Variables | Displays the registration variables of the component. The variables can be used by other components, such as the endpoint of a program. |
|   | Resources | Displays the information about the resources requested by the component. |
|   | Dependen cy Status | Displays the dependency data of the component on other components. The Dependency Status module is the same as that of Apsara Infrastructure Management. |

##### 5.1.1.2 Machine management

The Machine Management module allows you to view the basic information about machines and the components deployed on machines.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane, choose Resources > **Machine Management**.
4. The Machines page displays all physical machines and VMs managed by Apsara
Infrastructure Management. Click **Advanced Filter** and specify the Hostname/IP Address, Status, Product, and Cluster parameters. The system filters machines that meet the specified filter conditions. Optional. Click **Publish/Unpublish** above the machine list. On the page that appears, you can deploy or remove a machine. Deploy a machine a. Click the **Machine Publishing** tab. b. Select a product and bucket from the **Product** and **Bucket** drop-down lists. c. Click **Download Schema** to download the machine_list.xlsx file. Enter the machine information based on the requirements in the file.

> **Note:** nodename, Sn, and Ip are the required fields.

d. Click **Select File**. The **Upload Schema** dialog box appears. e. Click **Upload and Parse File** to upload the machine_list.xlsx file. f. After the file is parsed, click **Import**. View the information about the machine on the
**Machine Publishing** tab, including the hostname, IP address, serial number (SN),
and status. Click **Clear** in the Actions column of the machine that you want to manage to remove the machine from the machine list on the page. Click **Details** in the Actions column of the machine that you want to manage to view the details of the machine, such as the data center, rack, and room where the machine resides. g. Click **Batch Publish** in the lower-right corner of the page to deploy multiple machines at a time. Remove a machine

> **Note:** You can remove only machines in the default cluster.

a. Click the **Machine Unpublishing** tab. b. In the **Machines** field, enter the hostname or IP address of the machine that you want to remove. The information about the machine is displayed on the right side of the page. Find the machine that you want to remove and click **Clear** in the Actions column. c. Click **Batch Unpublish** in the lower-right corner of the page to remove multiple machines at a time. Select **Hostname/IP**, **Status**, **Product**, or **Cluster** from the drop-down list, and enter a value in the field to filter the machines that you want to manage.

| Parameter | Description |
|---|---|
| Hostname/IP Address | The hostname and IP address of the machine. |
| Status | The state of the machine. Valid values: Status Abnormal: The state of the machine displayed on Apsara Infrastructure Management is not Good. Ping Failed and No Heartbeat issues are excluded. Ping Failed: The machine cannot be connected to services managed by Apsara Infrastructure Management. No Heartbeat: The machine cannot report heartbeats to services managed by Apsara Infrastructure Management. Scaling In: The machine is being removed from a cluster. Scaling Out: The machine is being added to a cluster. Repairing: A maintenance operation is performed on the machine, such as machine repair. Normal: The machine works as expected. No O&M operations are performed on the machine, and the state of the machine displayed on Apsara Infrastructure Management is Good. In O&M: An O&M operation is performed on the machine, such as restarting the machine or reinstalling the operating system of the machine. |
| Cluster/Prod uct | The cluster and product to which the machine belongs. |
| Machine Metrics | Click the state of the machine that you want to manage in the Machine Metrics column. In the Metric Details dialog box that appears, view the details of component metrics, machine metrics, and system service metrics. |
| Actions | Click Terminal in the Actions column to go to the logon page and log on to the machine to perform related operations. You can also select multiple machines and click Batch Terminal in the lower-left corner of the page. Click Machine Status Dashboard in the Actions column to go to the Machine Status Panel page. You can view the machine information, service processes, and application details. Click Details in the Actions column to go to the machine details page. |

###### 5.1.1.2.1 Machine details

You can view the basic information about machines and the components deployed on the machines.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resource Management**.
3. In the left-side navigation pane, choose Resource Management > **Machines**.
4. On the Machines page, find the machine that you want to view and click **Details** in the
Actions column.
5. On the machine details page, view the status overview, the basic information about the
machine, and the components deployed on the machine. In the upper-right corner of the machine details page, you can perform the following operations: Click **Terminal** to log on to the machine. Click **Machine Status Dashboard** to view the machine information, service processes, and application details. Click **Machine Metrics** to go to the CloudMonitor platform and view the machine monitoring data. This operation is unavailable for VMs. Select **Restart**, **Repair and Clone**, or **Power Off and Repair** from the **Machine**
**Management** drop-down list. This operation is available only for physical machines.
For more information, see the Machine management section of this topic. You can click **Add to Favorites** to add the machine to favorites or click **Remove from**
**Favorites** to remove the machine from favorites. After the machine is added to the
favorites, you can view the machine on the Resource Tags page. Click the icon to generate a file in the XLS format and download the file to your computer. This operation is unavailable for VMs. Click the icon to refresh the page. The **Status Overview** section displays the information such as the status of the machine, Kubernetes node status, and emergency and severe alerts. Click the number below **Emergency/Severe Alarm**to go to the Alerts page.

> **Note:** If the machine status and Kubernetes node status are normal and no emergency or severe alerts are reported, the background of the Status Overview section is in green gradient color.
> When the machine is being scaled in, scaled out, or maintained, the background is in blue gradient color.
> If either the machine status or Kubernetes node status is abnormal or an emergency alert or a severe alert exists, the background is in orange gradient color.

The machine details page displays tabs including **Basic Information**, **Component**
**Deployment Topology**, **Components**, **VM**, **Taints**, and **Labels**.
The **VM** tab is displayed only if a VM exists on the machine.

> The **Taints** and **Labels** tabs are displayed only if the machine is a Kubernetes node.
> **Basic Information**: displays the basic information of the machine.

| Parameter | Description |
|---|---|
| Hostname | The hostname of the machine. Move the pointer over the hostname and click the icon to copy the hostname. |
| IP Address | The IP address of the machine. Move the pointer over the IP address and click the icon to copy the IP address. |
| Alias | The alias of the machine. You can modify the alias of the machine. Note The alias must be 0 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), _ and colons (:). It cannot start with a special character or digit. |

| Cluster | The cluster to which the machine belongs. Click Details next to the cluster name to go to the Cluster Details page and view the cluster details. |
|---|---|
| Product | The product to which the machine belongs. |
| Data Center | The data center where the machine resides. |
| Serial Number | The serial number (SN) of the machine. You can modify the SN of the machine. Note After you modify the SN of a machine, the system verifies the SN within the region. This prevents an SN from being used by two machines at the same time. |
| Model | The machine model. Click Details next to the machine model to view the basic information, location information, and hardware information about the machine. The Hardware Information section displays information such as hard disk, memory, CPU, CPU architecture, and CPU manufacturer. |
| Host | The host where the VM resides. This parameter is displayed only if the machine is a VM. Move the pointer over the name of the host, click Details to go to the host details page, or click Log On to go to the host logon page. |
| Machine Status | Click Status Monitoring next to Machine Status to view the information about component metrics, machine metrics, and system service metrics. Click Task Status next to Machine Status to go to the task details page. Task Status is displayed only when an operation is being performed on the machine. |
| Machine Action | The operation that is being performed on the machine and the operation progress. |
| CPU Manufacturer | The manufacturer of the machine CPU. |

| ide·Platform O&M | Apsara Uni-manager Operations Consol |
|---|---|

| Capacity | The CPU cores and memory capacity of the machine. If the machine is a VM, you can modify the CPU cores and memory capacity. |
|---|---|
| Kubernetes Node Status | This parameter is displayed only if the machine is a Kubernetes node. Click Details next to Kubernetes Node Status to view the details of the node status, including the basic information, operating system, Kubelet, and resource usage. Click Node Performance Data next to Kubernetes Node Status to view the performance analysis chart. |

**Component Deployment Topology**: displays the services and components that are
affected by VMs or physical machines by product and cluster. The card displays the status data of VMs and server roles. The icons on the left of the names of clusters, VMs, machines, services, and components that have not reached the desired state are orange. The icons are blue when clusters, VMs, machines, services, and components have reached the desired state. If the number of cards is less than nine, cards are displayed in three columns and N rows. If the number of cards is greater than eight, cards are displayed in grid layout. Cards are displayed from the upper-left corner in sequence. By default, the information of the first machine in the first cluster is displayed, and the information of other machines is hidden. If you do not select **Only display objects with abnormal status**, the status data of all VMs and server roles is displayed. The drop-down list in the search box on the right side displays the dependencies of clusters, machines, services, and components. After you select a node, the corresponding node in the topology is located and highlighted. Click the icon to unfold the card. Click the icon to fold the card. You can move the pointer over the machine name to view the node status and IP address of the machine. Click the icon next to the node status or click **Details** next to the machine name to go to the machine details page. Click **Terminal** next to the machine name to go to the machine logon page. You can move the pointer over the component name to view the component node status and instance status. Click the icon next to Node Status or Instance Status, or click **Details** next to the component name to go to the component details page.
**Components**: displays the information about components deployed on the machine,
including the component status, actions, and metrics. If the machine is a Kubernetes node, pods that run the components deployed on the PaaS base are displayed. Above the list of components, you can filter components by status, action, action status, and instance name. Click **View** in the Component Metrics column of the desired component to view the information about component metrics, machine metrics, and system service metrics. Click **Restart** in the Actions column of the desired component to restart the component.

> **Note:** You can start only the components deployed on Apsara Infrastructure Management.

Click **Details** in the Actions column of the desired component to go to the component details page and view the component information.
**VM**: displays the VMs that are started on the host machine. The lists displays
information such as the VM status and the products to which VMs belong. This tab is displayed only if the machine is a host machine. Above the list, you can filter VMs by status. Click **Details** in the Actions column of the desired VM to go to the VM details page and view the VM information.
**Taints**: displays the taint information about the Kubernetes node. You can create and
delete taints. This tab is displayed only if the machine is a Kubernetes node. Query a taint: Enter a taint key or value in the Support Key/Value Filtering field above the taint list. The filtered taints are displayed. Create a taint: Click **Add** in the upper-left corner of the tab. In the **Create Taint** dialog box, enter a custom taint key and value, select a taint effect, and then click
**OK**.

> **Note:** **PreferNoSchedule**: Kubernetes avoids scheduling pods that do not tolerate this taint to the node.
> **NoSchedule**: Pods that do not tolerate this taint are not scheduled to the node.
> **NoExecute**: Pods that do not tolerate this taint are evicted from the node if they are already running on the node, and are not scheduled to the node if they are not yet running on the node.

Delete a taint: Click **Delete** in the **Actions** column of the taint that you want to delete. In the **Confirm Deletion** message, click **OK**.
**Labels**: displays the labels of Kubernetes nodes. You can create and delete labels. This
tab is displayed only if the machine is a Kubernetes node. Query a label: Enter a label key or value in the Support Key/Value Filtering field above the label list. The filtered labels are displayed. Create a label: Click **Add** in the upper-left corner of the tab. In the **Create Label** dialog box, enter a custom label key and value and click **OK**. Delete a label: Click **Delete** in the **Actions** column of the label that you want to delete. In the **Confirm Deletion** message, click **OK**.

**Manage**

On the machine details page, click **Machine Management** in the upper-right corner. The management operations include **Restart**, **Repair and Clone**, and **Power Off and Repair**.

| Operation | Procedure |
|---|---|
| Restart | In the upper-right corner of the page, choose Machine Management > Restart. In the message that appears, click OK. |
| Repair and Clone |   |

| User Guide·Platfo | Apsara Uni-manager Operations rm O&M Consol |
|---|---|
|   | Note You can click Repair and Clone or Power Off and Repair based on your business requirements. Click Repair and Clone for machines that must be cloned before the operating system is reinstalled, such as the system disk. Click Power Off and Repair for machines whose issues can be repaired without cloning, such as memory issues. 1. In the upper-right corner of the page, choose Machine Management > Repair and Clone or Power Off and Repair. 2. In the dialog box that appears, enter REPAIR and click OK. 3. On the Basic Information tab of the machine details page,R epair Details appears next to Machine Status. Click Repair Details to go to the machine repair page. 4. Perform a precheck. i. In the Pre-check step, click Execute Pre-check in the upper-right corner. In the message that appears, click OK. The system automatically performs a precheck to ensure that the machine repair can be executed in a secure manner. Note After the precheck is complete, if the task status isf ailed and no blacklisted server role is detected, click Retry in the upper-right corner to retry the precheck. ii. Go to the pre-handle step by using one of the following methods. Method 1: After the precheck is complete, if the task status iss uccess, click Go to Pre-handle in the lower-left corner of the page. In the message that appears, click OK. You are directed to the Pre-handle step. Method 2: After the precheck is complete, if the task status isf ailed and a server role in the blacklist is detected, perform the corresponding operations based on the error message and then click Go to pre-handle in the lower- left corner of the page. In the dialog box that appears, enter Confirm and click OK. 5. Execute prehandling. Click Execute Pre-handle in the upper-right corner. In the message that appears, click OK. Then, the system automatically executes prehandling. Note If the prehandling fails, click Retry in the upper-right corner to try again. 6. Approve the repair. i. After the prehandling task is complete, click Enter Approval Phase in the lower-left corner. In the message that appears, click OK. ii. In the Approve step, view the components that need to be approved and click Approve in the Actions column. |
| Power Off and Repair |   |

|   | iii. In the dialog box that appears, enter APPROVED and click OK. Important Then, Action Status is changed from pending to approved. After Action Status is changed to approved, the action that you specified is automatically executed. Manually setting Action Status to approved instead of using the Decider program is a high-risk operation. Data loss may occur. You must contact technical support for confirmation. 7. Repair the machine. i. After the repair is approved, click Start Repair in the lower-left corner of the page. In the message that appears, click OK. ii. On the page that appears, machine information such as the name, IP, and serial number of the machine and the project to which the machine belongs is displayed. The maintenance personnel can repair the machine offline based on your business requirements. 8. Execute the post-handling task. i. After the machine is repaired, click Go to Post-handle in the lower-left corner. In the message that appears, click OK. ii. In the Post-handle step, click Execute Post-handle in the upper-right corner. In the message that appears, click OK. Note If the post-handling task fails, click Retry in the upper-right corner to try again. |   |   |
|---|---|---|---|
|   |   | Note If the post-handling task fails, click Retry in the upper-right corner to try again. |   |

##### 5.1.1.3 Resource tags

iii. After the post-handling task is complete, click **Complete Repair** in the lowerleft corner of the page. The Resource Tags module allows you to use tags to view and manage resources that you iv. In the dialog box that appears, enter **FINISHREPAIR** and click **OK**. The machine is repaired. pay attention to in a centralized manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane, choose Resources > **Resource Tags**.
4. View the resources that are added to favorites in the Watchlist section.
To add a machine to favorites, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose Resources> **Machine Management**. On the Machines page, find the machine that you want to manage and click Details in the Actions column to go to the machine details page. Then, click **Add to Favorites** in the upper-right corner of the page. After a resource is added to favorites, it is displayed in the Watchlist section on the Resource Tags page. Click the resource to go to the details page of the resource.
5. Perform operations on resources in the Resource List section.
The following table describes the operations.

| Operation | Description |
|---|---|
| View resource tags | You can view the resources that have tags bound. You can also search for resources and tags by resource name, resource type, or tag. |
| Bind tags to a resource | You can bind tags to a resource based on your business requirements. Select the resource that you want to manage and clickB ind Tags. a. In the Bind Tags dialog box, select one or more tags and clickN ext. You can add a tag, delete a tag, or delete multiple tags at a time. b. Select the resource to which you want to bind the tags on the Product View or Data Center View tab. You can select multiple resources. Click Bind. c. Click Close. The tags are bound to the specified resource. |
| Unbind tags from a resource | You can unbind tags from a resource based on your business requirements. Select the resource that you want to manage and click Unbind tags. In the message that appears, click OK. |
| Modify resource tags | You can delete resource tags that you no longer need. Find the resource that you want to manage and click Modify Tags in the Operation column. In the dialog box that appears, click the icon next to the tag that you want to delete, and click OK. |
| Export resource tags | You can export all resource tags in the list. ClickE xport. In the dialog box that appears, select a download URL and click Download. Note If you want to export only specific resource tags, select the resources whose tags you want to export and click Export. In the dialog box that appears, select a download URL and click Download. |

##### 5.1.1.4 Base machine resource dashboard

The base machine resource dashboard displays the resource allocation information from the machine and product dimensions. Resources include CPU, memory, GPU, local dedicated disk, and local shared disk resources. You can view the resource allocation details of a specific machine or product.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane, choose Resources > **Base Machine Resource**
**Dashboard**.
By default, the page displays resource usage from the machine dimension. You can click the icon in the upper part of the page to switch to the product dimension.
4. (Optional) Find the machine that you want to view.
In the **Machines** section, select Machine, Labels, or Taints from the drop-down list and enter a corresponding value in the search box to filter the machine that you want to view. You can also click **Advanced Filter** and configure the Machine, Labels, or Taints parameter to filter the machine that you want to view.
5. The **Machines** section displays the machine resource information, including Allocated CPU,
Allocated Memory, and Allocated GPU.

| Parameter | Description | Example |
|---|---|---|
| Machine | The name and IP address of the machine. | e21j10005.cloud.j10.amtest 98 10.98.2.9 |
| Allocated CPU | The percentage of allocated CPU resources to total available CPU resources, amount of available CPU resources, amount of allocated CPU resources, and overcommit ratio. The overcommit ratio is a parameter that is specified in advance. The amount of available CPU resources is equal to the amount of CPU resources available to the machine multiplied by the overcommit ratio. | 29.54% 1343/396.7 cores (overcommitted 1400%) |
| Allocated Memory | The percentage of allocated memory resources to total available memory resources, amount of available memory resources, amount of allocated memory resources, and overcommit ratio. The overcommit ratio is a parameter that is specified in advance. The amount of available memory resources is equal to the amount of memory resources available to the machine multiplied by the overcommit ratio. | 77.6% 828.1/642.6 GiB (overcommitted 220%) |

| Allocated GPU | The percentage of allocated GPU resources to total available GPU resources, amount of allocated GPU resources, and amount of available GPU resources. - indicates that the machine does not have GPU resources. | 50% 1/2 |
|---|---|---|
| Yoda Disk | The percentage of allocated local dedicated disk space to total available local dedicated disk space, amount of total available space, and amount of allocated space. The total amount of available space refers to the space of all local dedicated disks for the machine. | 26.84% 43.7/11.7 TiB |
| Yoda LVM | The percentage of allocated local shared disk space to total available local shared disk space, amount of total available space, and amount of allocated space. The total amount of available space refers to the space of all local shared disks for the machine. | 11.7% 1.3/0.2 TiB |
| Labels | The labels added to the machine. By default, the number of existing labels for the machine is displayed. Move the pointer over the number of labels to view all the labels of the machine. | Labels: 34 |
| Taints | The taints added to the machine. By default, the number of existing taints for the machine is displayed. Move the pointer over the number of taints to view all the taints of the machine. | Taints: 1 |
| Total Pods | The pods that are scheduled to the node. By default, the number of pods is displayed. Find the machine that you want to manage and click the number in the Total Pods column to view the pod details. In the dialog box that appears, the pods are sorted by product and application name. | 31 |
| Actions | Click Resource Details to go to the resource information page. The page displays the distribution of CPU, memory, GPU, and Yoda LVM resources and the planning of Yoda Disk resources in charts. Yoda LVM refers to local shared disks and Yoda Disk refers to local dedicated disks. Click Machine Details to go to the machine details page and view the machine details. | - |

#### 5.1.2 Platform blueprint

This topic describes the panorama of products and the topological relationships of hardware in a data center.

**Modules**

| Module | Description |
|---|---|
| Product Topology | Displays the topological relationships among products, and the dependencies and ownership of products, services, and components. |
| Hardware Topology | Displays the topological relationships among network devices, racks, and physical machines in a data center. |

##### 5.1.2.1 Product topology

This module displays product status and resource statistics by product in a hierarchy. The information includes the relationships between products and related resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Platform Blueprint**. By default, the **Product topology** page appears.
The Product topology page displays all the cloud products that are deployed in Apsara Stack. You must focus on abnormal products whose icon is displayed in orange. These products may not reach the desired state, or have P1 and P2 alerts that are not handled.

| No. | Section | Description |
|---|---|---|
| 1 | Overview section | In this section, you can view the total number of products deployed in the current environment and the number of products in each state. The product state can be Normal or Exception. |
| 2 | Issue diagnostics section | If multiple products with exceptions exist, the system uses algorithms to automatically display the products that need to be preferentially handled and provides suggestions for troubleshooting issues. The system selects the five most important products with exceptions based on the importance of products and the relationship between products. |

| 3 | Hierarchy section | The hierarchy consists of four layers. The layer at the top shows products on the cloud management platforms, monitoring products, disaster recovery and backup products, and others. These products are displayed above the titles of Uni-manager/Cloud management, Disaster recovery, Monitoring operation, and Others. Other products refer to products that fail to fall into the preceding categories. The next layer shows PaaS products, including middleware, big data, databases, application services, and Internet of Things (IoT) products. The next layer shows IaaS products, including elastic computing, network, storage, and security products. The layer at the bottom shows infrastructure, including common components that enable other cloud products. Note The icon of normal products is displayed in blue. The icon of abnormal products is displayed in orange. When you move the pointer over or click the icon of a cloud product, the system displays the product name, status, alert level, exceptions, and dependencies. Note Move the pointer over or click the icon of a cloud product. Products that are connected by orange lines are the ones on which the current product depends. Move the pointer over or click the icon of a cloud product. Products that are connected by gray lines are affected by the current product. Click Details in the upper-right corner of the message for a product to go to the product details page. For more information, see the following table. |
|---|---|---|

3. Click Details in the upper-right corner of the message for a product to go to the product
details page. The following section describes the topologies of products deployed on Apsara Infrastructure Management and the PaaS base: For products deployed on Apsara Infrastructure Management, the hierarchy of the topology consists of the following levels: product, cluster, service, component, and instance. For products deployed on the PaaS base, the hierarchy of the topology consists of the following levels: product, cluster, service, and component.

| No. | Section | Description |
|---|---|---|
| 1 | Overview section of product relationship | In this section, you can view the product relationships. You can view the current cloud product and cloud products with dependency exceptions. Click a product name next to Dependency exception cloud products to go to the product details page and view the topology of the product. |
| 2 | Issue diagnostics section | In this section, you can view product exceptions and suggestions for troubleshooting issues. Note You can perform aggregation analysis to determine the root causes of why components fail to reach the desired state. This helps locate issues caused by hardware, rolling updates, and instance software. |
| 3 | Overview section | In this section, you can view the total number of products and the number of products in each state. The product state can be Normal or Exception. |
| 4 | Search section | Select Show only status exception objects. The topology displays only abnormal clusters, components, services, and instances. If you clear this check box, all abnormal and normal nodes are displayed. The drop-down list displays the hierarchical relationship among clusters, services, components, and instances. Click a name. The system locates the node in the topology and highlights the node card. |

| 5 | Topology section | The hierarchical relationship among clusters, services, components, and instances in the product is displayed in a topology and each node is displayed as a card. Move the pointer over or click a node card. The system displays the node status, including alerts, details, and logon button. Move the pointer over a product card and click the icon next to Alert if alerts exist. You are navigated to the Alerts page. Alternatively, you can go to the Alerts page by choosing Monitor&Alarms > Alarm Management > Alarm List in the top navigation bar of the Apsara Uni-manager Operations Console. Move the pointer over an instance card and click the icon next to Node status or Instance status to go to the machine details page or component details page to view the corresponding details. Click Details of the node that you want to manage to go to the corresponding cluster details page or component details page. Click Terminal of the node that you want to managet o go to the machine logon page. Note A product consists of one or more clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. |
|---|---|---|

##### 5.1.2.2 Hardware topology

On the Hardware topology page, you can view the topological relationships among the network devices, racks, and physical machines in a data center.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Platform Blueprint**.
3. In the left-side navigation pane, choose **Platform Blueprint > Hardware Topology**.
The topology displays the topological relationships among the network devices, racks, and physical machines in a data center. Network devices include switches such as interconnection switch (ISW), LVS switch (LSW), customer switch (CSW), distribution switch (DSW), and access switch (ASW). Physical machines refer to hosts. You can move the pointer over a physical machine icon and click Details in the pop-up message to view the Docker VMs and could product components that run on the machine.

| No. | Section | Description |
|---|---|---|
| 1 | Overview | In this section, you can view the number of abnormal network devices and physical machines. The number of abnormal devices and the total number of devices are displayed below the name of each device type. The number to the left of the slash indicates the number of abnormal devices and the number to the right of the slash indicates the total number of devices. |
| 2 | Exception statistics | In this section, you can view the number of abnormal network devices and physical machines in a data center. The number of abnormal devices and the total number of devices are displayed next to the name of each device type. The number to the left of the slash indicates the number of abnormal devices and the number to the right of the slash indicates the total number of devices. |
| 3 | Search | If you select Only exception servers and their associated nodes are displayed, the topology shows abnormal nodes, including racks and machines. If you clear this check box, all abnormal and normal nodes are displayed. The drop-down list displays the hierarchical relationships among machines, racks, physical machines, and network devices. Select a name from the drop-down list. The system locates the corresponding node in the topology and highlights the node card. |

| 4 | Topology | You can fold or unfold different hardware groups. By default, the hardware groups at the top are automatically unfolded. If a group is folded, the system displays the number of abnormal devices and the total number of devices in a card. The details are not displayed when you move the pointer over the icon. If a group is unfolded, the system displays the devices and machines in icons. Move the pointer over an icon. In the message that appears, the system displays the device details. Click Details in the message of a device to go to the device details page. Alternatively, log on to the Network Operations Console. In the left-side navigation pane, choose Basic Network > Network Element Management. Then, click the Device Management tab to view the details of the desired device. Click Details in the message of a machine to go to the machine details page. Click Terminal in the message of a machine to go to the machine logon page. Note Blue icons indicate normal nodes. Orange icons indicate abnormal nodes. If the line between two nodes is gray, the device connection is normal. If the line between two nodes is orange, exceptions occur. The line between aggregation nodes is a dashed line. Click View topology in the message of a machine. In the Component deployment topology dialog box, view the services and components that are directly affected by the machine. |
|---|---|---|

#### 5.1.3 Kubernetes cluster management

This topic describes the basic information about Kubernetes clusters and nodes and the resource usage of clusters and nodes.

**Modules**

| Module | Description |
|---|---|

| Cluster Overview | Displays the Kubernetes clusters created and managed by Apsara Infrastructure Management and the resource usage of clusters. |
|---|---|
| Node Management | Displays all Kubernetes nodes managed by Apsara Infrastructure Management. |

##### 5.1.3.1 Cluster overview

You can view the resource usage of O&M Kubernetes clusters, including CPU utilization, memory usage, pod usage, and storage usage of the logical volumes. O&M Kubernetes clusters are the Kubernetes clusters that are created and managed by Apsara Infrastructure Management.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Kubernetes Cluster Management**. By default, the **Kubernetes**
**Cluster Overview** page appears.
3. On the **Kubernetes Cluster Overview** page, view the basic information, resource usage,
and nodes of a cluster.

| Parameter | Description |
|---|---|
| Kubernetes Cluster Overview | Displays the Kubernetes version, registration time, CPU, and memory of the cluster. You can switch clusters by selecting a cluster from the drop-down list in the upper part of the page. |
| Cluster Resource Usage | Displays the CPU utilization, memory usage, pod usage, and storage usage of the logical volume for the cluster. The resource usage data includes the used resources, total available resources, unit, and usage percentage. |

| Nodes | Displays the node details of the cluster. Click Advanced Filter to filter nodes by Name, Label, Taint, Role, or Status. Click Terminal in the Actions column of the node that you want to manage to log on to the machine. Click Machine Status Dashboard in the Actions column of the node that you want to manage to view the machine information, service processes, and application details. Click Node Performance Data in the Actions column of the node that you want to manage to view the performance data of the node. Click Details in the Actions column of the node that you want to manage to go to the Machine Details page and view the details. |
|---|---|

##### 5.1.3.2 Node management

You can view the basic information about nodes deployed on the platform, including the node name, status, IP address, role, resource usage, labels, and taints. You can also view node performance data, log on to a machine, go to the Machine Status Panel page, and view machine details.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Kubernetes Cluster Management**.
3. In the left-side navigation pane, choose Kubernetes Cluster Management > **Node**
**Management**.
4. On the **Kubernetes Nodes** page, view the information about Kubernetes nodes, including
the number of nodes, name, IP address, status, role, number of labels, number of taints, and resource usage of each node.
5. (Optional) In the search box above the node list, search for the node that you want to view.
6. View the node information. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name/IP Address | The name and IP address of the node. |

| Status | The state of the node. Valid values: Ready, Not Ready, and Unknown. |
|---|---|
| Role | The business role of the node. For example, master indicates the primary node and redis1 indicates Node 1 where the Redis service is deployed. |
| Label/Taint | The number of existing labels and taints for the node. The labels and taints determine whether programs can be deployed on the node. |
| Allocated CPU | The percentage of the consumed CPUs to the total CPUs that can be allocated. |
| Allocated Memory | The percentage of the memory usage to the total memory that can be allocated. |
| Local Shared Storage | The percentage of the used storage capacity to the total storage capacity that can be allocated in shared disk resources. |
| Actions | Click Terminal to log on to the machine and perform operations. You can also select multiple nodes and click Batch Terminal in the lower-left corner of the page to log on to multiple machines at a time. Click Machine Status Dashboard to go to the Machine Status Panel page. You can view the basic information about the machine, disk usage, processes deployed on the machine, and details of applications. Click Node Performance Data to go to the Grafana dashboard page and view the resource usage of the node, such as CPU utilization. Click Details to go to the machine details page. |

#### 5.1.4 Hardware O&M

This topic describes how to repair hard disk drives (HDDs) and query machine repair records.

**Modules**

| Module | Description |
|---|---|

| HDD Repairs | You can efficiently and securely complete the entire process of data disk replacement. Preparation: After you initiate an HDD replacement task, you must make preparations for the task, including task reporting, task approving, and HDD unmounting. Repair: After the preparation for HDD replacement is complete, you can start the repair work, including HDD replacement, HDD installation, and inspection. History: You can view all records about HDD repairs, including related machines, HDDs, and repair results. |
|---|---|
| Machine Repair | You can query machine repair records. |

##### 5.1.4.1 HDD repairs

The HDD repair feature allows you to replace data disks. If a fault occurs in a data disk, the system confirms the status of the disk, uninstalls the disk, and then confirms that the business is not affected before performing subsequent operations. After the disk is replaced, the system formats, mounts, and restores the disk to provide the storage capacity.

**Modules**

| Module | Description |
|---|---|
| Preparation | After you initiate a disk replacement task, you must make preparations for it, including task reporting, task approving, and disk unmounting. |
| Repair | After you complete the preparations that are required to replace a disk, you can replace the disk and perform a health check on the new disk. |
| History | You can view a list of all repair records to learn repaired machines and HDDs, and repair results. |

###### 5.1.4.1.1 Preparation

After you initiate a disk replacement task, you must make preparations for it, including task reporting, task approving, and disk unmounting.

**Prerequisites**

If you want to use the disk replacement feature to replace a disk online, the following conditions must be met: The disk is a data disk that is used by Apsara Distributed File System and provides storage capabilities for users. No other files are stored on the disk. Cloud services that support disk replacement, such as Apsara Infrastructure Management, Elastic Compute Service (ECS), and MaxCompute, are deployed on the machine in which the disk resides. The disk is marked as abnormal in Apsara Distributed File System. The system checks and confirms whether the preceding conditions are met during the maintenance. If the preceding conditions are not met, the disk replacement is not triggered or errors are reported during the precheck.

**Background information**

If you ignore the error messages and forcibly replace the disk, data loss may occur. You can use the disk replacement feature to handle only damaged disks that are reported by Apsara Distributed File System. You can use the disk replacement feature to replace only damaged data disks. If you do not replace the disks with new disks, the maintenance process is interrupted. The data disks of Apsara Infrastructure Management, MaxCompute, Object Storage Service (OSS), and Simple Log Service can be repaired.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. By default, the **Disk Repair** page is displayed.
On the **Preparation** tab, you can query disk replacement tasks by progress or machine name.
3. Perform operations based on the task status in different phases.
The preparation process is divided into the following phases: Report, Approval, and Unmounting. The task can be in one of the following states in each of the three phases: not started (displayed in gray), in progress (displayed in blue), completed (displayed in green), and failed (displayed in red). The following table describes the corresponding operations that can be performed in these states.

| Report | Approval | Unmounting | Executable operation |
|---|---|---|---|
| In progress | Not started | Not started | Cancel |
| Completed | Not started | Not started | Start to repair the disk and cancel the task |
| Failed | Not started | Not started | Cancel |
| Completed | In progress | Not started | Select manual approval by clicking Approval Details |
| Completed | Completed | In progress | N/A |

| Completed | Completed | Disk unmounting completed but silence period not ended | N/A |
|---|---|---|---|
| Completed | Completed | Disk unmounting completed and silence period ended | Prepare to replace the disk |

Related operations: Cancel the disk replacement task: Click **Cancel**. In the message that appears, click **OK**. Start to repair the disk: Click **Start Repair**: If a QR code is required for approval, the system pops up the QR code. You can use the DingTalk mini program ASLM Mobile to scan the QR code to obtain the authorization code. Then, enter the authorization code. The system proceeds to the next step after the verification is passed. If a QR code is not required for approval, click **OK** in the dialog box that appears to start to repair the disk. After that, the software enters the automatic approval phase. Manually approve a disk replacement task: If **Approval Details** is displayed in the
**Actions** column, click **Approval Details**. In the dialog box that appears, click **Approval**
in the **actions** column of the service role that you want to manage. In the dialog box that appears, enter **APPROVED** in the Enter APPROVED to confirm your operation field. Then, click **OK**.

> **Important:** Before approval, make sure that business data on the disk is backed up.

Prepare for disk replacement: Click **Prepare for Replacement**. The disk replacement task enters the repair phase and is displayed on the **Repair** tab. The time period displayed below **Unmounting** is the silence period. You can change the disk only if the value is larger than 7 days.

###### 5.1.4.1.2 Repair

After you complete the preparations that are required to replace a disk, you can replace the disk and perform a health check on the new disk.

**Prerequisites**

If you want to use the disk replacement feature to replace a disk online, the following conditions must be met: The disk is a data disk that is used by PANGU and provides storage capabilities to users. No other files are stored on the disk. Cloud services that support disk replacement, such as Apsara Infrastructure Management, Elastic Compute Service (ECS), and ODPS, are deployed on the machine in which the disk resides. The disk is marked as abnormal in PANGU. The preparations that are required to replace the disk are complete. The system checks and confirms whether the preceding conditions are met during the maintenance. If the preceding conditions are not met, the disk replacement is not triggered or errors are reported during the precheck.

**Background information**

If you ignore the error messages and forcibly replace the disk, data loss may occur. You can use the disk replacement feature to handle only damaged disks that are reported by PANGU. You can use the disk replacement feature to replace only damaged data disks. If you do not replace the disks with new disks, the maintenance process is interrupted. The data disks of Apsara Infrastructure Management, ODPS, Object Storage Service (OSS), and Simple Log Service (SLS) can be repaired.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. By default, the **Disk Repair** page appears.
3. Click the **Repair** tab.
You can filter the repair tasks that you want to view by task phase and machine name.
4. Perform operations based on the task status in different phases.
The maintenance process is divided into the following phases: Replacement, Disk Mounting, and Inspection. Replacement: replaces the failed disk. Disk Mounting: checks the basic information about the new disk and perform initialization operations such as formatting and mounting. Inspection: waits for the related business system to check the new disk. After the check is passed, the new disk is used. If the check is not passed, contact technical support to troubleshoot the issue. The task can be in one of the following states in each of the three phases: not started (displayed in gray), in progress (displayed in blue), completed (displayed in green), and failed (displayed in red). The following table describes the corresponding operations that can be performed in these states.

| Disk replacement | Disk mounting | Inspection | Available operation |
|---|---|---|---|
| Not started | Not started | Not started | Start to replace the disk |

| In progress | Not started | Not started | Complete the disk replacement |
|---|---|---|---|
| Completed | In progress | Not started | Replace the disk again |
| Completed | Failed | Not started | Replace the disk again |
| Completed | Completed | In progress | N/A |
| Completed | Completed | Failed | N/A |

Related operations: Start to replace the disk: Click **Start Replacement**. Complete the disk replacement: Click **Complete Replacement**. Replace the disk again: Click **Re-replace Disk**.

###### 5.1.4.1.3 Repair history

This topic describes how to view a list of all repair records. You can view the machines and hard disks that were repaired and their repair results.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M** to go to the **Disk Repair** page.
3. Click the **History** tab.
Search for disk replacement tasks by cluster and status.
4. Find the disk replacement task that you want to manage and click **Action Details** in the
**Actions** column. In the panel that appears, you can view the detailed execution steps of
the task, starting from the report step.

##### 5.1.4.2 Machine repairs

You can view and query machine repair records.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**.
3. In the left-side navigation pane of the page that appears, choose Hardware O&M >
**Machine Repair**.
4. On the WholeMachineMaintenance page, view the machine repair records. You can select
Host Name, Status, Cluster, or Maintenance Method from the drop-down list and enter a value in the search box to filter machine repair records that you want to view. You can also click **Advanced Filter** to filter repair records.
5. The details of the machine repair records are displayed in the list. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| ID | The ID of the machine repair task. |
| Host Name/IP | The hostname and IP address of the machine. |
| Cluster | The cluster to which the machine belongs. |
| Maintenance Method | The method that is used to repair the machine. |
| Status | The state of the machine repair task. Valid values: failed: The machine repair task failed. cancel: The machine repair task is canceled. doing: The machine is being repaired. done: The machine repair task is complete. |
| Start Time | The time when the machine repair task begins. |
| End Time | The time when the machine repair task ends. |
| Actions | For machines that are in the doing state, click Details to go to the repair details page. For machines that are in the failed, canceled, or done state, click Details. The Details panel appears, which displays the points in time of different task steps. |

#### 5.1.5 O&M tools

This topic describes the modules related to O&M tools.

**Modules**

| Module | Description |
|---|---|
| Task Management | Displays the details of tasks running on Apsara Infrastructure Management and the PaaS base. |
| Service Management | Allows you to manage the services deployed on Apsara Infrastructure Management and the corresponding service templates. |
| VM Dashboard | Displays the Docker VMs pulled and managed by Apsara Infrastructure Management in the environment. |
| Service Registration Variable Dashboard | Displays the service variables registered with products and corresponding content. |

| Resource Dashboard | Displays the instances of resources such as DNS and VIPs requested by using Apsara Infrastructure Management. |
|---|---|
| Basic Service Monitoring | Displays the monitoring information about basic services to help identify exceptions. |

##### 5.1.5.1 Task management

You can view the details of tasks running on Apsara Infrastructure Management and the PaaS base.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**. By default, the **Task Dashboard** page appears.
3. The Tianji Tasks tab is displayed by default. Select a time range to view the tasks running
on Apsara Infrastructure Management within the time range. You can click **1 Hour**, **1 Day**, or **1 Week** to quickly select a time range. Click **Details** in the Actions column of the task that you want to manage to go to the **Task**
**Details** page.
Details of a task on Apsara Infrastructure Management

| No. | Section | Description |
|---|---|---|
| 1 | Basic Information | Displays the basic information about the task, such as task name, task status, submitter, submission time, and execution duration. |
| 2 | Related Clusters | Displays the clusters that are related to the task. You can submit a task to change multiple clusters. In most cases, an Apsara Stack task is associated with one cluster. Cluster/Product: the cluster that is changed and the product to which the cluster belongs. Status: the state of the task. Valid values: Failed Terminated Running Paused Succeeded Waiting Progress: the state of the task in progress. In most cases, you must build the task before you submit it. The building states include Waiting, Doing, Done, and Failed. Note Apsara Infrastructure Management calculates the change content based on the desired-state configurations. For example, Apsara Infrastructure Management determines whether to update the version and the destination version. The task change states include Waiting for Change, Changing, Change Completed, and Change Failed. Version/Submission Time: the version and the time when the task is submitted. Actions: Click Build Details to view the components of the cluster, status, and progress. Click Resource Task Details to view the status, ownership, and error message of the resource request task. |
|   |   | Displays the changes of a cluster. Cluster changes include component changes and machine changes. Component Changes: the version change of a component. The version change status of all components is displayed based on services. This section displays the number of components of each service. |

|   |   | Consol |
|---|---|---|
|   |   | Note Different operation buttons are displayed for each task state. The operation buttons include Terminate, Retry, Suspend, and Continue. If the task state is Running, the Terminate and Suspend buttons are displayed. If the task state is Paused, the Continue button is displayed. If the task state is Failed or Terminated, the Retry button is displayed. Make sure that no new tasks are submitted for the current cluster or server role. Click Terminate in the upper-right corner of the list to terminate tasks. Click Retry in the upper-right corner of the list to perform theR etry Upgrade, Force Retry, or Retry Rollback operation. Click Suspend in the upper-right corner of the list to suspend tasks. Click Continue in the upper-right corner of the list to continue tasks. Click the icon on the left of the service name to view the change details of each component. For more information, see the following component change table. |

| 3 | Change Content | Click Details in the Actions column of the component that you want to manage to view the component progress. Overview Information: displays the basic information about the component, such as Commit Id, Rolling Status, Approval Policy, and Upgrade Plan. In the upper-right corner, click View Details to go to the Rolling Summary page and view the component update details. Go to the Rolling Summary page. In the Overview Information section, click Retry, Terminate, or Suspend to retry, terminate, or suspend a task. You can perform the operations only on unfinished tasks. The system can monitor and display the service level agreement (SLA) changes. You can view the real-time monitoring status of components. Click View Logs to view SLA monitoring logs. Click Edit SLA Configuration to modify the SLA configuration. Note You can view the SLA-related content of services for which the SLA feature is enabled. Click View All to view the component update details. Click Edit Parameter to modify the relevant parameters. Only the parameters for unfinished tasks can be modified. In the Instance Details section, you can add multiple component tasks to the blacklist. Instance Details: displays information such as the change status of component instances, component actions, and metrics. Note The Machine Changes tab is displayed only when the change type is Machine Scale-out, Machine Scale-In, Component Scale-out, or Component Unpublishing. Machine Changes: Machine changes in this module refer to machine scaling operations, excluding other operations such as machine repairs. The change content is displayed based on the Machine, Change Type, Status, and Actions columns. Machine: the name of the machine. Change Type: the change type. Valid values: Machine Scale-out, Machine Scale-in, Component Scale-out, and Component Unpublishing. Status: the state of the change. For more information, see the status in the Add to Cluster section. |
|---|---|---|
|   |   | Actions: the actions that you can perform. You can log on to the machine and view the machine details. |

|   |   | Click Terminal in the Actions column to log on to a machine. Click Details in the Actions column to go to theM achine Overview page and view the machine details. Basic Information: displays the following information: Change Status, Machine Status, Machine Action, Cluster, Machine Metrics, and Submission Time. Details: consists of Add to Cluster, Clone, and Deploy Component Instances. Add to Cluster: displays the cluster where the machine resides and the cluster to which you want to add the machine, as shown in the preceding figure. Status: the state of the machine change. Valid values: Failed: The change failed. Cancel: The change task is canceled. For example, the machine scale-in task is submitted when the machine scale-out task is not complete. Doing: The change is in progress. Waiting: The change is waiting to be performed. Done: The change is complete. Current Cluster: the cluster where the machine resides. Destination Cluster: the cluster to which you want to add the machine. |
|---|---|---|

**Component change table**

| Parameter | Description |
|---|---|
| Component | The components of the service. |
| Status | The state of the component. Valid values: Building: The component is being built. Build Failed: The component failed to be built. Waiting: The component is waiting to be changed. Running: The component is being changed. Paused: The change is paused. Rolling Back: The change is being rolled back. Rolling Back Prepared: The rollback is being prepared. Downloading: The program and configurations are being downloaded. Ready: The dependencies are being updated. Download Timeout: The download timed out. Succeeded: The change is complete. Failed: The change failed. Blocked: The component is not updated because the dependencies failed to be changed. Obstructed: The change is blocked by a previous task. Terminated: The task is terminated. Rolling Back Failed: The rollback failed. Rolled Back: The rollback is successful. Resource Checking: The resources are being checked. Resource Apply Failed: The resources failed to be requested. Su Paused: The canary release is paused. If you specify canary release rules, you must specify the interval at which the canary release is paused. Su Binary Paused: The version change is paused when no canary release is performed. Su Failed Paused: The canary release failed. In this case, the change is paused. You must determine whether to resume the change. Precheck: The component update is being prechecked. The precheck is performed before the download. Precheck Failed: The precheck failed. Postcheck: The component is being checked after the task is complete. Postcheck Failed: The post-check failed. |
| Dependency | Displays the dependencies required for component updates. You can update the component only after the dependencies are updated. You can view the dependencies to locate the component on which task blockage occurs. |

| Actions | Click Details in the Actions column to view the change details of the component. |
|---|---|

4. Switch to the PaaS Tasks tab, and select a time range to view the tasks running on the PaaS
base within the specified time range. You can click **1 Hour**, **1 Day**, or **1 Week** to quickly select a time range. Click **Details** in the Actions column of the task that you want to manage to go to the **Task**
**Details** page.
Details of a task on the PaaS base

| Section | Description |
|---|---|
| Base Info | Displays the basic information about the task, including Task ID, Status, Created, Create Time, Start Time, End Time, and Task Message. |

| Subtask List | Displays the information about subtasks, including Id/Description, Status, Describe, Change Object, Create/EndTime, ExecutionMethod, and Actions. Valid values of Status: Created Processing Suspended Completed Failed Terminated Click Cluster in the Change Object column to go to the Cluster Details page. You can also choose Resources > Product & Cluster O&M in the left-side navigation pane and find the cluster to view the cluster details. Click Show Parameters in the Actions column to view the parameters and values. Click Yaml in the Actions column to view the storage configuration information. Move the pointer over the More icon in the Actions column and clickM odify Execution Configuration to modify the configuration of the task. Note Only the configuration of unfinished tasks can be modified. Move the pointer over the More icon in the Actions column and clickA pprove to approve the task. Note Only unfinished tasks can be approved. |
|---|---|

##### 5.1.5.2 Service management

This topic describes how to manage the services deployed on Apsara Infrastructure Management and the corresponding service templates.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, click **Service Management**.
4. On the **Service Management** page, select a service from the **Service** drop-down list.
Then, the instances and templates of the selected service are displayed on the **Service**
**Instances** and **Service Template** tabs.
After you remove the service from all clusters, you can click**Delete Service**to delete the service.
5. On the **Service Instances** tab, the information of each instance is displayed in the **Where**
**Instance In Cluster**, **Status**, and **Component Statistics (Ready/Total)** columns. You
can also click **Instance Details** in the **Actions** column.

| Parameter | Description |
|---|---|
| Where Instance In Cluster | The cluster where the service is deployed and the product to which the cluster belongs. Click the name of a cluster to go to the component details page. On this page, you can view the status details of the one or more components in the cluster. |
| Status | The status of the service instance in the cluster. |
| Component Statistics (Ready/Total) | The status of components under the service. |
| Actions | Click Instance Details to go to the component details page. On this page, you can view the status details of the one or more components in the cluster. |

6. Perform the following operations on the **Service Template** tab:
Click **Create Template** to create a template. The following table describes the parameters.

| Parameter | Description |
|---|---|

| Basic Information | Name: the name of the template. This parameter is required. Group: the group of the template. You can select an existing group or click + Create Group to create a group. Description: the description of the template. This parameter is required. |
|---|---|
| Template Content | Enter a file name or folder name in the search box to filter template files. Click the icon, and then choose Add Folder or Create File. Select the file that you create and click Show Content. In the text box on the right, enter the content of the file and click Preview and Submit. In the Confirm and Submit dialog box that appears, enter the content description and click OK. Submit Description: the description of the template content. Difference File: the differences between the file and the previous file. |

Enter a template name in the Template search box to filter **service templates**. Fuzzy search is supported. The following table describes the parameters in the service template list.

| Parameter | Description |
|---|---|
| Template | The name of the service template. |
| Description | The description of the template content. |
| Group | The group to which the template belongs. |
| Last Modified At | The time when the service template was last modified. |

| References | The number of times the service template is referenced. Click the value in the References column of a service template to go to the template details page. On this page, view the details of the template in different versions that is referenced in clusters. |
|---|---|
| Actions | Click Edit in the Actions column to edit a template. Click Delete in the Actions column to delete a template. Click Operation History in the Actions column to view the operation records of a template, including the description, version, operator, and operation time. Click Version Differences in the Actions column to view the differences between the current version and other versions. Click Deploy Template in the Actions column to deploy a service template. In the Deploy Template panel, perform the following operations: a. Select a version from the Template Version drop-down list, enter description in the Comment field, select the cluster in which you want to deploy the template from the Selectable Cluster section, and then click the icon to add it to the Selected Cluster section. Note You can click Preview in the Actions column of the selected cluster to view the file changes. b. Click Submit. In the Operation Confirm dialog box, check the deployment information and click OK. |

##### 5.1.5.3 VM dashboard

The VM dashboard displays the Docker VMs pulled and managed by Apsara Infrastructure Management in the environment.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, choose O&M Tools > **VM Dashboard**.
4. Enter a value in the search box or click **Advanced Filter** to filter the desired data by **VM**,
**Product**, **Cluster**, **Current Physical Machine**, and **Desired Physical Machine**.
5. View the following information in the **VM dashboard** list.

| Parameter | Description |
|---|---|
| Product | The name of the cloud service. |

| Cluster | The cluster to which the VM belongs. |
|---|---|
| VM | The name of the VM. Click the VM name to go to the machine details page. On this page, you can view the details of the VM. Click Terminal in the VM column to go to the logon page and log on to the VM. |
| Current Physical Machine | The physical machine where a VM resides. Click the name of the physical machine to go to the machine details page. On this page, you can view the details of the physical machine. Click Terminal in the Current Physical Machine column to log on to the physical machine. |
| Desired Physical Machine | The preset physical machine to which you want to migrate the VM. Click the name of the desired physical machine to go to the machine details page. On this page, you can view the details of the physical machine. Click Terminal in the Desired Physical Machine column to log on to the physical machine. |

##### 5.1.5.4 Dashboard of service registration variables

**variables**

You can view the service variables registered with products and the corresponding content.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, choose O&M Tools > **Service Registration Variable**
**Dashboard**.
4. In the upper-right corner of the page, click the download icon to export the configurations in
the list. A file in the **XLSX** format is generated, and the file can be downloaded to your computer by using a browser.
5. In the upper part of the page, enter a value in the search box or click **Advanced Filter** to
filter desired registration variables by **Service Registration**, **Service**, or **Cluster**.
6. In the lower part of the page, view the following information about variables: **Service**,
**Service Registration**, **Cluster**, and **Update Time**.
Click the **show****or****hide** icon in the **Service Registration** column of the service that you want to manage to view or hide the registration information about the service. Click the value in the **Service Registration** column of the service that you want to manage. In the message that appears, view the complete registration information about the service.

##### 5.1.5.5 Resource dashboard

The resource dashboard displays the instances of resources such as Domain Name System (DNS) and virtual IP addresses (VIPs) requested by using Apsara Infrastructure Management.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, choose O&M Tools > **Resource Dashboard**.
4. In the upper-right corner of the page, click the download icon to export the instance list as
a **JSON** file to your local computer by using a browser.
5. Enter a value in the search box to search for resources. You can also click **Advanced Filter**
to filter resources by **name**, **product**, **cluster**, **service**, **component**, **application**, **type**,
**status**, **parameters**, **result**, or their combinations.
6. In the resource list, view information about resources, including **Name**, **Product/Cluster**,
**Component/Application**, **Status**, **Parameters**, **Result**, **Resource ID**, **Reprocess**
**Status**, **Reprocess Message**, **Reprocess Result**, **Business Additional Configuration**,
**Related Versions**, and **Error Message**.
Click the **show and hide** icon in the **Parameters**, **Result**, and **Reprocess Result** columns of the resource that you want to manage to view or hide the resource parameters, resource request result, and second request status. Click the values in the **Parameters**, **Result**, and **Reprocess Result** columns of the resource that you want to manage. In the messages that appear, view the complete information about the resource parameters, resource request result, and second request status.

**Resource information**

| Parameter | Description |
|---|---|
| Name | The name of the resource. |
| Product/Cluster | The product and cluster of the service. |
| Component/Applicatio n | The component and application of the server role. |
| Status | The resource request state. |
| Parameters | The resource request parameters, such as the VIP configuration. |
| Result | The resource request result, such as the endpoint allocated to an ApsaraDB RDS instance and the VIP. |
| Resource ID | The resource ID. |
| Reprocess Status | The state of the second request, which is automatically initiated when the first quest fails. |
| Reprocess Message | The message of the second request, which is automatically initiated when the first quest fails. |
| Reprocess Result | The result of the second request. |
| Business Additional Configuration | The custom configurations that are attached to the resource by the business service. These configurations are not specified by using Apsara Infrastructure Management. |
| Refer Version List | The resource versions that have been used. |
| Error Message | The error message. |

##### 5.1.5.6 Basic service monitoring

You can view the monitoring information about basic services to quickly identify service exceptions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, choose O&M Tools > **Basic Service Monitoring**.
4. On the Basic Service Monitoring page, view the information in the API Status and Tianji Data
Status sections.
**API Status**: displays Console API Status, Tianji API Status, Kubernetes API Status, and
Gateway API Status.
**Tianji Data Status**: displays Data Sync Time and Desired State Calc Time.

#### 5.1.6 Web clients

This topic describes the CLI-based logon and remote O&M features provided by the Web Terminal module. This module also supports blocking and approval of high-risk operations, and allows you to audit all operations.

**Modules**

| Module | Description |
|---|---|
| Web Client Logon | Provides a web client to support the following features: Server Logon: You can query information about servers, VMs, and containers. You can log on to servers, VMs, and containers. Database Logon: You can query the metadatabases requested by services. You can log on to metadatabases. vSwitch Logon: You can query information about vSwitches. You can log on to vSwitches. |
| Account Authorization | Allows you to manage temporary account authorization. |
| Command Management | Allows you to manage CLI commands that are run by using a web client. |

| Operation Records | Allows you to view the O&M operations that are performed by using a web client. |
|---|---|

##### 5.1.6.1 Web Client Logon

Web client logon includes server logon, database logon, and switch logon.

###### 5.1.6.1.1 Server logon

You can search for containers, VMs, and physical machines by different conditions and log on to the containers, VMs, and physical machines to perform O&M operations. You can also log on to the control nodes of OPS1, OPS2, OPS3, and OPS4 to perform O&M operations.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**. The **Server Logon** page appears by default.
3. Log on to the server on the ServerRole login or MachineGroup login tab.
4. Click the ServerRole login tab.
Select a server role name from the **Server Role** drop-down list. Fuzzy search is supported. On the ServerRole login tab, the cluster name, status, and project are displayed above the **Host** section. You can click Login or Log on to the vm host to log on to the VM or host related to the server role.
**Login**: allows you to log on to the VM where the server role is deployed.
**Log on to the vm host** : allows you to log on to the host of the VM where the server
role is deployed.
**Log on to the docker**:
a. Click the icon in the Docker column to refresh the column and try to obtain the docker ID. If **Log on to docker** appears next to the docker ID., the docker ID is obtained.

> **Note:** If the docker ID does not appear after the refresh, the docker ID fails to be obtained. This may occur for the following reasons:
> The status of the container is abnormal.
> The server role is in the process form and does not have a docker container.

b. Click **Log on to docker** to log on to the docker. In the **Docker** column, click **docker logs** and **docker inspection report** to view the logs and inspection report of the container. Log on to the web terminal page and click the node to which you want to log on. You can also click the icon and select an account in the dialog box. By default, the ops account is selected.

> **Note:** If a message indicating that you have not installed the required certificate appears, install a certificate for the corresponding region by following the instructions in the Installation Guide mentioned in the message.

If no account meets your permission requirements, you can apply for a temporary account. a. Select an account type and apply for an account. b. After you submit an account application, wait for the application to be approved. After the application is approved, the account takes effect and can be used to log on to the server.

> **Note:** Click **View Review Progress** to go to the **Workflow details** page and view the approval progress. To go to the Workflow details page, choose **Platform** **Operation > O&M Change > Process Approval** in the top navigation bar. On the My Submission page, click the workflow that you want to view.

Enter Linux commands in the CLI window to perform related operations.

> **Note:** You cannot log on to a server that has a region different from that of the web terminal page. After you switch the region, an error message appears on the web terminal page. Troubleshoot the issue by following the instructions on the page.

Click **File operations** to upload and download files. Click **File Upload**. You can use one of the following methods to upload a file: Click the dotted box. In the dialog box that appears, select the file that you want to upload and click **Open**. Click **Upload** in the **Upload File** dialog box. Drag the file to the dotted box and then click **Upload**. Click **File Download**. The **File Download** dialog box appears. Configure the **File**
**Directory** and **File name** parameters and then click **Download** to download the file
to the default download folder used by your local browser.

> **Note:** The file that you want to upload or download cannot exceed 200 MB in size.

5. Click the MachineGroup login tab.
Select a cluster name from the **Cluster** drop-down list. Fuzzy search is supported. Find the machine that you want to log on to from the machine list and click **Login** in the Machine column. Log on to the web terminal page and click the node to which you want to log on. You can also click the icon, and select an account in the dialog box. By default, the ops account is selected.

> **Note:** If a message indicating that you have not installed the required certificate appears, install a certificate for the corresponding region by following the instructions in the Installation Guide mentioned in the message.

If no account meets your permission requirements, you can apply for a temporary account. a. Select an account type and apply for an account. b. After you submit an account application, wait for the application to be approved. After the application is approved, the account takes effect and can be used to log on to the server.

> **Note:** Click **View Review Progress** to go to the **Workflow details** page and view the approval progress. To go to the Workflow details page, choose **Platform** **Operation > O&M Change > Process Approval** in the top navigation bar. On the My Submission page, click the workflow that you want to view.

Enter Linux commands in the CLI window to perform related operations.

> **Note:** You cannot log on to a server that has a region different from that of the web terminal page. After you switch the region, an error message appears on the web terminal page. Troubleshoot the issue by following the instructions on the page.

Click **File operations** to upload and download files. Click **File Upload**. You can use one of the following methods to upload a file: Click the dotted box. In the dialog box that appears, select the file that you want to upload and click **Open**. Click **Upload** in the **Upload File** dialog box. Drag the file to the dotted box and then click **Upload**. Click **File Download**. The **File Download** dialog box appears. Configure the File Directory and File name parameters and then click **Download** to download the file to the default download folder used by your local browser.

> **Note:** The file that you want to upload or download cannot exceed 200 MB in size.

###### 5.1.6.1.2 Database logon

This topic describes how to log on to databases that are used by server roles of services and perform related operations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**.
3. In the left-side navigation pane, click **Database Logon**.
4. Select a service name from the **Service** drop-down list. Fuzzy search is supported.
5. The lower part of the page displays the databases that are used by all server roles of the
service. Find the database that you want to manage and click **Login** in the **Operation** column.
6. On the page that appears, click the node or the
icon next to the node.

> **Note:** If a message indicating that you have not installed the required certificate appears, install a certificate for the corresponding region by following the instructions in the Installation Guide mentioned in the message.

Enter SQL statements in the CLI window to perform related operations.

> **Note:** You cannot log on to a database that has a region different from that of the web terminal page. After you switch the region, an error message appears on the web terminal page. In this case, troubleshoot the issue by following the on-screen instructions.

###### 5.1.6.1.3 vSwitch logon

You can log on to a vSwitch to perform related operations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**.
3. In the left-side navigation pane, choose Web Terminal > Web Client Logon > **Switch**
**Logon**.
4. Find the vSwitch to which you want to log on and click **Log On** in the **Actions** column.
5. On the page that appears, click the vSwitch or the
icon next to the vSwitch. In the dialog box that appears, enter the username and click OK to log on to the vSwitch.

> **Note:** If a message indicating that you have not installed the required certificate appears, install a certificate for the corresponding region by following the instructions in the Installation Guide mentioned in the message.

Enter the password as prompted. You can log on to the vSwitch only if you enter the correct password. Otherwise, you will log on to the jump server as an ops user. After you log on to the vSwitch, enter Linux commands in the CLI window to perform related operations.

> **Note:** You cannot log on to a vSwitch that has a region different from that of the web terminal page. After you switch the region, an error message appears on the web terminal page. Troubleshoot the issue by following the instructions on the page.

##### 5.1.6.2 Account authorization

You can view the information about temporary account authorization.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**.
3. In the left-side navigation pane, choose Web Terminal > **Account Authorization**.
4. On the Account Authorization page, view and manage temporary account authorization.
5. You can filter information about temporary account authorization by **user** and **status**. The
following table describes the parameters in the user list.

| Parameter | Description |
|---|---|
| User | The name of the user in the Apsara Uni-manager Operation Console. |
| Type | The type of the account. Valid value: SERVER. |

| Logon Account | ops: a regular Linux account that belongs to the ops user group. This account allows you to perform read, write, and execute operations on files based on configured file permissions. We recommend that you use the ops account to perform routine O&M. The super administrators of Open Application Model (OAM) and administrators, auditors, security administrators, and basic O&M engineers of the web console for Apsara Infrastructure Management can use the ops account. audit: a regular Linux account that belongs to the audit user group. This account can be used to run the sudo command to obtain the privileges to run the following commands without providing the password: aureport, auditctl, ausearch, last, lastlog, cat, less, more, head, and tail. This account can also be used to perform the stop auditd and rsyslog operations without providing the password. This account is the owner of the /var/log directory. By default, auditors of the web console for Apsara Infrastructure Management can use the audit account and approve and revoke the temporary permissions of this account. security: a regular Linux account that belongs to the security user group. This account can be used to run the sudo command to obtain the privileges to run the following commands without providing the password: passwd, chown, chmod, chgrp, usermod, chage, and visudo. By default, security administrators of the web console for Apsara Infrastructure Management can use the security account and approve and revoke the temporary permissions of this account. admin: a regular Linux account that belongs to the admin user group. This account can be used to run sudo commands without providing the password and has higher permissions. By default, administrators of the web console for Apsara Infrastructure Management can use the admin account and approve and revoke the temporary permissions of this account. root: a super Linux account with the super administrator permissions on devices. By default, super administrators of OAM can use the root account and approve and revoke the temporary permissions of this account. |
|---|---|
| Status | Authorized: The authorization is within the validity period. Recycled: The permissions are revoked by the account administrator within the validity period of the authorization. Invalid: The authorization expires and is invalid. |
| Authorization Time | The time when the temporary authorization application is approved. |
| Expiration Time | The time when the authorization expires. |
| Actions | The operation that you can perform. Valid value: Reclaim permissions. Note You can revoke permissions when the following conditions are met: The authorization does not expire. The user has the permission to revoke the permissions of the authorized account. For example, only the OAM super administrators can revoke the permissions of the root account. |

##### 5.1.6.3 Command management

You can manage the CLI commands that are run by using web clients.

**Create an access control policy**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**.
3. In the left-side navigation pane, choose Web Terminal > **Command Management**.
4. On the Command Control page, click **Create Policy**.
5. In the **Create a policy** dialog box, configure the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Policy name | The name of the policy. The name can be 2 to 32 characters in length and can contain letters, digits, and hyphens (-). |
| Manage users | The names of the Apsara Uni-manager Operations Console users that are managed by the policy. Enter a keyword to search for the matched users, and select the users that you want to manage from the drop-down list. Alternatively, select all users and exclude specific users. |
| Exclude users | The users to be excluded. This parameter is displayed only if you select All users for the Manage users parameter. Enter a keyword to search for the matched users, and select the users that you want to exclude from the drop-down list. |
| Control dimension | The management dimension. Valid values: Machine dimension and Component container dimensions. |
| Component | This parameter is displayed only if you select Component container dimensions for the Control dimension parameter. The components to be managed. Note You can select All components and exclude specific components. |

| Exclude components | This parameter is displayed only if you select All components for the Component parameter. The components to be excluded. |
|---|---|
| Machine | This parameter is displayed only if you select Machine dimension for the Control dimension parameter. The machines to be managed. Note You can select All Machines and exclude specific machines. |
| Exclude Machines | This parameter is displayed only if you select All Machines for the Machine parameter. The machines to be excluded. |
| Command set type | The type of the command set. Valid values: Blacklist and Whitelist. Note If both the blacklist and whitelist are hit, the blacklist takes precedence. |
| Command set | The set of commands that are used for management. |
| Status | Specifies whether to disable the policy item. |

**More operations**

| Operation | Procedure |
|---|---|
| View a policy | On the Command Control page, search for a policy by name. You can view the information about the policy including the policy name, command set, type of the command set, control dimension, components or machines that are managed, status, and the time when the policy was created. |
| Edit a policy | i. Click Edit in the Actions column of the policy that you want to edit. ii. In the Edit policy dialog box, modify the policy information and click OK. |
| Delete a policy | i. Click Delete in the Actions column of the policy that you want to delete. ii. In the message that appears, click OK. |

| Import a policy | i. Click Import above the policy list. ii. In the Import dialog box, click Upload files. iii. In the dialog box that appears, select the files that you want to upload and click Open. Then, click OK. Note Only .xls and .xlsx files can be imported. |
|---|---|
| Export a policy | Select the policy that you want to export and clickE xport below the policy list to download and view the policy. |

##### 5.1.6.4 Operation records

This topic describes how to view O&M operations performed by using web clients.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**.
3. In the left-side navigation pane, click **Operation Record**.
4. The Operation Record page consists of the following three tabs: Command Records, Upload
and Download Audit, and Playback. By default, the **Command Records** tab appears.

**Command Records**

You can view the operation records of commands that are executed by using web clients.
1. Select a filter condition from the drop-down list and enter a value in the search box. You
can filter command records by Command, Operated At, Machine, and Operated By.
2. Click **Advanced Filter** to filter command records by **Command**, **Operated At**, **Machine**,
**Operated By**, or their combinations.
3. In the command record list, view the following information: **Command**, **Operated By**,
**Operated At**, **Machine/Container**, **Target Type**, **SessionId**, and **Audit Result**.

**Upload and Download Audit**

You can view the information about file uploads and downloads that are performed by using web clients.
1. Click the **Upload and Download Audit** tab.
2. View the information about **Upload Times**, **Download Times**, and the list of uploads and
downloads.
3. The list contains the following information: **Operation Type**, **File Path**, **Operated By**,
**Operated At**, and **Machine/Container**.

**Playback**

You can view the video playbacks of all commands that are executed on a machine.
1. Click the **Playback** tab.
2. Click **Advanced Filter** to filter video records by **Operated At**, **Operated By**, **Machine**, or
their combinations.
3. Click **View** in the **Actions** column of an operation record.
4. In the video playback window, click the
icon to play back the video.

### 5.2 O&M of management services

This topic lists the following O&M platforms for management services: Apsara Stack Inspection System Basic Service Control Configuration Management Database ApsaraDB Operations and Maintenance System (Lite) Apsara Stack Doctor UniConsole Server Insight Base Container O&M Platform API O&M OpenAPI Explorer Operating System O&M Platform Operation and Maintenance Knowledge Base

### 5.3 Capacity management

This topic describes the features related to capacity management.

**Features**

By analyzing the capacity usage of each service and understanding unique usage patterns, you can forecast capacity trends to inform expansion plans and other operational decisions.

| Module | Description |
|---|---|
| Capacity Overview | Displays an overview of the total capacity and any anomalies across each cloud service, facilitating rapid problem identification. |
| Compute Capacity | Displays the capacity usage and trend analysis of compute services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Network Capacity | Displays the capacity usage and trend analysis of network services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Storage Capacity | Displays the capacity usage and trend analysis of storage services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Base Capacity | Displays the capacity usage and trend analysis of Apsara Infrastructure Management general services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Database Capacity | Displays the capacity usage and trend analysis of database services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Middleware Capacity | Displays the capacity usage and trend analysis of middleware services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |

#### 5.3.1 Capacity Overview

This topic describes how to view the overall capacity usage and capacity exceptions in each cloud service to help you quickly identify errors.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Capacity**
**Overview**.
3. On the Capacity Overview page, view data in the following sections.
**Service Statistics**: displays the number of cloud services whose capacities are
connected to the current environment, including **Total Services**, **Current Normal**
**Capacity (Services)**, and **Current Capacity Alert (Services)**.
**Cloud Service Capacity Overview**: displays the numbers of clusters that have
exceptions and clusters that are predicted to have exceptions for custom cloud services. In the upper-right corner of the page, you can click **Custom Cloud Services** to specify custom cloud services to be displayed.

> **Note:** You must specify at least one custom cloud service and can specify up to five custom cloud services.

**Cloud product capacity overview**: displays the capacity overview of all cloud services
in the cluster and capacity dimensions. If clusters that have exceptions or clusters that are predicted to have exceptions exist in a cloud service, **Cluster Capacity Alert** appears in the upper-right corner of the service card. You can click **All clusters**, **Current Capacity Alert (Clusters)**, or **Forecast**
**Capacity Alert (Clusters)** to view details of the relevant clusters.
4. In the upper-right corner of the Capacity Overview page, click **Refresh** to refresh the
capacity overview data.
5. In the upper-right corner of the page, click **Export Capacity Report**, select desired cloud
services, and then click **Export** to export the capacity data to your on-premises machine.

#### 5.3.2 Computing capacity

##### 5.3.2.1 ECS

You can view the Elastic Compute Service (ECS) capacity to obtain the usage and trend of ECS resources. This helps you perform O&M operations based on your business requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Compute Capacity**.
3. In the left-side navigation pane, choose **Compute Capacity > ECS**.
4. In the upper part of the page, view ECS data in the **Capacity Overview** and **Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view **vCPU Capacity**, **GPU Capacity**, and
**Memory Capacity** of all clusters, including the **Total**, **Allocated**, and **Capacity**
**Allocation Rate** parameters.
In the **Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **vCPU**, **Memory**, and **GPU** allocation rates of all clusters or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. On the **Cluster Capacity** tab in the lower part of the page, click **Advanced Filter** to filter
the list by **Cluster**, **Cluster Type**, **Zone**, and **CPU** to obtain the desired capacity data. Click the up and down arrow icon in the **vCPU Allocation Rate**, **Memory Allocation**
**Rate**, or **GPU Allocation Rate** column to sort cluster capacity data in descending order
or ascending order. When the distribution rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Details** in the **Capacity Planning Formula** column of a desired cluster to obtain the detailed capacity planning formula. Click **Export** to export the cluster capacity data to your on-premises machine.
6. On the **Specification Inventory** tab, you can filter the list by **Specification** to query the
specifications of desired instance types. Fuzzy search is supported. Click the up and down arrow icon in the **Instances That Can Be Created** or **Created**
**Instances** column to sort the instance types in ascending or descending order.
Click the name of the **instance type** to view the cluster details within the instance type. Click **Export** to export the specifications and inventory data to your on-premises machine.

#### 5.3.3 Network capacity

##### 5.3.3.1 SLB

You can view the Server Load Balancer (SLB) capacity to obtain the usage and trend of SLB resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Network Capacity**.
3. In the left-side navigation pane, click **SLB**.
4. In the upper-right corner of the page, select the desired cluster. You can select different
clusters to view the capacity data of each cluster.

> **Note:** The clusters that have **slbCluster** in their names are default clusters.
> The clusters that have **slbExtraCluster** in their names are expanded clusters.

5. In the upper part of the page, view data in the **Capacity Overview** and **Cluster**
**Allocation Rate Trend** sections of the SLB cluster.
In the **Capacity Overview** section, you can view **Internet VIP Capacity** and **Internal**
**VIP Capacity** of the cluster, including the **Total**, **Allocated**, and **Capacity Allocation**
**Rate** parameters.
In the **Cluster Allocation Rate Trend** section, you can view the trend chart that shows the **Internet VIP** and **Internal VIP** allocation rates of the cluster within different time periods. Move the pointer over a time node to view the recorded data.
6. In the **Capacity Details** section, view the capacity details of the cluster by selecting the
cluster from the **Cluster** drop-down list. Click **Export** to export the capacity data to your on-premises machine.

#### 5.3.4 Storage capacity

##### 5.3.4.1 EBS

You can view the Elastic Block Storage (EBS) capacity to obtain the usage and trend of EBS resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **EBS**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Usage Trend** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of hybrid clusters and full-flash clusters, including the total capacity, used capacity, and capacity usage. In the **Physical capacity usage trends** section, you can view the trend charts that show the physical capacity usage of all full-flash clusters, all hybrid clusters, or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, filter the list by **Cluster**, **Zone**, **Storage**
**Type**, **Specification**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage**, **Logical Capacity**
**Usage**, or **Inventory Capacity Allocation Rate** column to sort data in ascending or
descending order. Physical capacity: the total physical capacity that is reported by Apsara Distributed File System.

> Logical capacity: the maximum amount of data that you can write into disks.
> Inventory capacity: the total capacity of cloud disks that you can create.

Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.4.2 OSS

You can view the Object Storage Service (OSS) capacity to obtain the usage and availability of OSS resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **OSS**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Usage Trend** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of hybrid clusters, including the total capacity, used capacity, and capacity usage. In the **Physical Capacity Usage Trend** section, you can view the trend charts that show the physical capacity usage of all hybrid clusters or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage** or **Logical Capacity**
**Usage** column to sort data in ascending or descending order.
Physical capacity: the total physical capacity that is reported by Apsara Distributed File System.

> Logical capacity: the maximum amount of data that you can write into disks.

Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.4.3 Tablestore

On the Tablestore page, you can view Tablestore storage capacity. This enables you to understand the usage and availability of relevant resources and perform O&M operations based on your business requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation bar, click **Tablestore**.
4. In the upper part of the displayed page, view data in the following sections: **Physical**
**Capacity Overview** and **Physical Capacity Usage Trend**.
In the **Physical Capacity Overview** section, you can view the capacity data of hybrid clusters, including the total capacity, used capacity, and capacity usage. In the **Physical Capacity Usage Trend** section, you can view the trend charts that show the physical capacity usage of all hybrid clusters or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the lower part of the page that appears, click **Advanced Filter** of the **Capacity Details**
section. You can combine **Cluster**, **Zone**, **Storage Type**, and **CPU** to search for a desired cluster and view its storage capacity details. Click the up and down arrow icon in the **Physical Capacity Usage** or **Logical Capacity**
**Usage** column to sort data in ascending or descending order.
Physical capacity: the total physical capacity reported by the Apsara Distributed File System.

> Logical capacity: the maximum volume of data that can be written onto the disks.

Click **Export** to export the capacity details to your on-premises computer.

##### 5.3.4.4 Simple Log Service

Viewing the Simple Log Service storage capacity helps you gain insights into the current resource usage and residual resources, which allows you to undertake targeted O&M operations that align with actual needs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **Simple Log Service**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Allocation Rate Trend** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of hybrid clusters, including the total capacity, used capacity, and capacity usage. In the **Physical Capacity Usage Trend** section, you can view the trend charts that show the physical capacity usage of all hybrid clusters or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage** or **Logical Capacity**
**Usage** column to sort data in ascending or descending order.
Physical capacity: the total physical capacity reported by the Apsara Distributed File System.

> Logical capacity: the maximum volume of data that can be written onto the disks.

Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.4.5 NAS

Viewing the Apsara File Storage NAS (NAS) storage capacity helps you gain insights into the current resource usage and residual resources, which allows you to undertake targeted O&M operations that align with actual needs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **NAS**.
4. In the upper part of the page, view data in the **Pangu water level overview** and **Pangu**
**water level usage trend** sections.
In the **Pangu water level overview** section, you can view the total capacity, used capacity, and capacity usage of hybrid clusters. In the **Pangu water level usage trend** section, you can view the trend charts that show the capacity usage trend of Apsara Distributed File System for all hybrid clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Pangu water level utilization rate** column to sort data in ascending or descending order. Click **Export** to export the capacity details to your computer.

##### 5.3.4.6 CPFS file system

You can view the capacity data of a Cloud Parallel File Storage (CPFS) file system to understand the used and unused resources of a service. Then, you can perform O&M based on your requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **Apsara File Storage CPFS**.
4. In the upper part of the CPFS Capacity page, view data in the **Physical Capacity**
**Overview** and **Physical capacity usage trends** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of all-flash clusters and hybrid clusters, including the total capacity, used capacity, and capacity usage. In the **Physical capacity usage trends** section, you can view the trend charts that show the physical capacity usage of all all-flash clusters, all hybrid clusters, or a single cluster within different periods of time. Move the pointer over a time node to view the corresponding capacity data.
5. In the **Capacity Details** section of the CPFS Capacity page, click **Advanced Filter** and
search for a cluster by **Cluster**, **Zone**, **Storage Type**, and **CPU**. Click the up or down arrow next to **Physical Capacity Usage**, **Logical Capacity Usage**, or **Inventory Capacity Allocation Rate** to sort data in ascending or descending order. Physical capacity: the total capacity of available hardware.

> Logical capacity: the maximum amount of data that you can write into disks.
> Inventory capacity: the total capacity of disks that you can create.

Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.4.7 APFS file system

You can view the capacity of an Apple File System (APFS) file system to understand the used and unused resources of a service. Then, you can perform O&M based on your requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **Apsara File Storage APFS**.
4. In the upper part of the APFS Capacity page, view data in the **Physical Capacity**
**Overview** and **Physical capacity usage trends** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of all-flash clusters and hybrid clusters, including the total capacity, used capacity, and capacity usage. In the **Physical capacity usage trends** section, you can view the trend charts that show the physical capacity usage of all all-flash clusters, all hybrid clusters, or a single cluster within different periods of time. Move the pointer over a time node to view the corresponding capacity data.
5. In the **Capacity Details** section of the APFS Capacity page, click **Advanced Filter** and
search for a cluster by **Cluster**, **Zone**, **Storage Type**, and **CPU**. Click the up or down arrow next to **Physical Capacity Usage**, **Logical Capacity Usage**, or **Inventory Capacity Allocation Rate** to sort data in ascending or descending order. Physical capacity: the total capacity of available hardware.

> Logical capacity: the maximum amount of data that you can write into disks.
> Inventory capacity: the total capacity of disks that you can create.

Click **Export** to export the capacity data to your on-premises machine.

#### 5.3.5 Base capacity

##### 5.3.5.1 Apsara Infrastructure Management Storage Capacity

#### Storage Capacity

You can view the storage capacity of Apsara Infrastructure Management to obtain the usage and availability of the relevant resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **Capacity** > **Base Capacity**.
3. In the left-side navigation pane, click **Apsara Infrastructure Management Storage**
**Capacity**.
4. In the upper part of the page, view data in the **Pangu water level overview** and **Pangu**
**water level usage trend** sections.
In the **Pangu water level overview** section, you can view the total capacity, used capacity, and capacity usage of all clusters. In the **Pangu water level usage trend** section, you can view the trend charts that show the capacity usage trend of Apsara Distributed File System for all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Pangu water level utilization rate** column to sort data in ascending or descending order. Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.5.2 Docker host capacity of Apsara Infrastructure Management

**Infrastructure Management**

On the Host capacity page, you can view statistics information such as the capacity of all hosts and usage balance information, and the capacity usage list of each scheduling domain. The scheduling domains are divided by Access Switch (ASW).
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Base Capacity**.
3. In the left-side navigation pane, click **Tianji Docker Host Capacity**.
4. In the upper part of the Host capacity page, view the information such as **Machine**, **CPU**
**allocation rate**, **CPU usage**, **Memory allocation rate**, and **Memory usage**.
**Machine**: displays the number of machines in different states and the percentage of
machines in the normal state.
**CPU allocation rate**: displays the number of allocated CPU cores and the CPU allocation
rate.
**CPU usage**: displays the average CPU utilization of all hosts within the last 1 hour.
**Memory allocation rate**: displays the size of allocated memory and the memory
allocation rate.
**Memory usage**: displays the average memory usage of all hosts within the last 1 hour.
5. In the **Average CPU usage trends** section, view the trend charts that show the CPU
allocation rate and CPU utilization within the specified period of time. Move the pointer over a time node to view the corresponding CPU allocation rate and CPU utilization.
6. In the **Average Memory usage trends** section, view the trend charts that show the
memory allocation rate and memory usage within the specified period of time. Move the pointer over a time node to view the corresponding memory allocation rate and memory usage.
7. In the **Scheduling domainCPU usage distribution** section, view the number of
scheduling domains with different CPU utilization. The scheduling domains are divided by ASW. Move the pointer over a node to view the scheduling domains with the corresponding CPU utilization.
8. In the **Scheduling domainMemory usage distribution** section, view the number of
scheduling domains with different memory usage. The scheduling domains are divided by ASW. Move the pointer over a node to view the scheduling domains with the corresponding memory usage.
9. In the **Scheduling domain capacity details** section, select a scheduling domain from the
**Scheduling domain** drop-down list to view the capacity details of the scheduling domain.
Click the up or down arrow next to **CPU allocation rate**, **Memory allocation rate**, **CPU**
**AVG usage**, **Memory AVG usage**, **CPU MAX usage**, or **Memory MAX usage** to sort
data in ascending or descending order. If the allocation rate or average usage exceeds 80%, the corresponding value is highlighted. If the maximum usage exceeds 90%, the corresponding value is highlighted. If the average CPU utilization or average memory usage exceeds 80%, the corresponding value is highlighted. Move the pointer over a number in the **Machine** column to view the hostnames.
0. Find the scheduling domain that you want to view and click **Capacity details** in the
**Operation** column. The capacity details page of the scheduling domain appears.
In the upper part of the capacity details page, view the statistics information about capacity usage in the scheduling domain. For more information, see Step 4 of this topic. In the middle part of the capacity details page, view the capacity information about each host in the scheduling domain. For more information, see Step 5 to Step 8 of this topic. In the **Host capacity details** section of the capacity details page, specify values for the
**HostName/IP** and **Status** parameters to search for a host.
Click the up or down arrow next to **CPU allocation rate**, **Memory allocation rate**,
**CPU AVG usage**, **Memory AVG usage**, **CPU MAX usage**, or **Memory MAX usage**
to sort data in ascending or descending order. If the allocation rate or average usage exceeds 80%, the corresponding value is highlighted. If the maximum usage exceeds 90%, the corresponding value is highlighted. Find the host that you want to manage and click the number in the **VM** column or click
**VM migration** in the **Operation** column. The list of the VMs on the host appears.
Find the VM that you want to manage and click **Initiate migration** in the **Operation** column. In the message that appears, click **OK** to submit the migration task. For more information about migration operations, see VM transfer. You can submit multiple migration tasks at a time. Find the VM that you want to view and click **VM details** in the **Operation** column. You are navigated to the **Basic Information** tab of the machine details page. For more information, see Machine details. Find the host that you want to manage and click **Capacity Change Trend** in the
**Operation** column. You are navigated to the machine monitoring page of the
CloudMonitor console. For more information, see the CloudMonitor documentation.

#### 5.3.6 Database capacity

##### 5.3.6.1 RDS

You can view data on the MySQL capacity page to obtain the usage and availability of ApsaraDB RDS (RDS) resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **RDS**.
4. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the lower part of the page, view the capacity data of RDS based on different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, filter the list by **Logical cluster** and **Capacity**
**Type** to view the desired capacity data.
When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Export** to export the capacity data to your on-premises machine. On the **Specification Inventory** tab, filter the list by **Specification Name** and
**Specification Type** to view details of the desired instance types. Click **Export** to
export the inventory data of the instance types to your on-premises machine.

**Physical Machine Dimension**

Filter the list by **Apsara infrastructure management framework cluster**, **Physical**
**Machine**, **Physical IP**, **Capacity Type**, **Zone**, and **CPU processor** to view the desired
capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

**Apsara Infrastructure Management Framework Cluster Dimension**

Filter the list by **Cluster**, **Zone**, and **CPU processor** to view the desired capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.6.2 ApsaraDB RDS for PostgreSQL

You can view the capacity of the ApsaraDB RDS for PostgreSQL service to obtain the usage and availability of the service resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **ApsaraDB RDS for PostgreSQL**.
4. In the upper-right corner of the page, select **All clusters** or a specific cluster to view the
capacity data.
5. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters or a specific cluster, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster in different time periods. Move the pointer over a time node to view the recorded data.
6. In the lower part of the page, view the capacity data of ApsaraDB RDS for PostgreSQL
based on different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, filter the list by **Logical cluster** and **Capacity**
**Type** to view the desired capacity data.
When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Export** to export the capacity data to your on-premises machine. On the **Specification Inventory** tab, filter the list by **Specification Name** and
**Specification Type** to view details of the desired instance types. Click **Export** to
export the inventory data of the instance types to your on-premises machine.

**Physical Machine Dimension**

Filter the list by **Apsara infrastructure management framework cluster**, **Physical**
**Machine**, **Physical IP**, **Capacity Type**, **Zone**, and **CPU processor** to view the desired
capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

**Apsara Infrastructure Management Framework Cluster Dimension**

Filter the list by **Cluster**, **Zone**, and **CPU processor** to view the desired capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.6.3 Redis

You can view the capacity of the ApsaraDB for Redis service to obtain the usage and availability of the service resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **Redis**.
4. In the upper-right corner of the page, select **All clusters** or a specific cluster to view the
capacity data.
5. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters or a specific cluster, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
6. In the lower part of the page, view the capacity data of ApsaraDB for Redis based on
different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, filter the list by **Logical cluster** and **Capacity**
**Type** to view the desired capacity data.
When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Export** to export the capacity data to your on-premises machine. On the **Specification Inventory** tab, filter the list by **Specification Name** and
**Specification Type** to view details of the desired instance types. Click **Export** to
export the inventory data of the instance types to your on-premises machine.

**Physical Machine Dimension**

Filter the list by **Apsara infrastructure management framework cluster**, **Physical**
**Machine**, **Physical IP**, **Capacity Type**, **Zone**, and **CPU processor** to view the desired
capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

**Apsara Infrastructure Management Framework Cluster Dimension**

Filter the list by **Cluster**, **Zone**, and **CPU processor** to view the desired capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click the up and down arrow icon in the **CPU allocation rate**, **Memory allocation**
**rate**, or **Disk allocation rate** column to sort the cluster capacity data in ascending or
descending order. Click **Export** to export the capacity data to your on-premises machine.

##### 5.3.6.4 MongoDB

You can view the capacity of ApsaraDB for MongoDB to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **MongoDB**.
4. In the upper-right corner of the MongoDB Capacity page, select **All clusters** or a specific
cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the MongoDB Capacity page, view **Capacity Overview** and **Cluster**
**Capacity Allocation Rate Trend**.
In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters or a specific cluster, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
6. In the lower part of the MongoDB Capacity page, view the capacity data of the
corresponding ApsaraDB for MongoDB instance based on different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, you can configure the **Logical cluster** and
**Capacity Type** parameters to obtain capacity data.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click **Export** to export the capacity data to your computer. On the **Specification Inventory** tab, you can filter instance types by **Specification**
**Name** and **Specification Type** and then view the capacity data of the instance types.
You can click **Export** to export the inventory data of the instance types to your computer.

**Physical Machine Dimension**

You can obtain capacity data by **Apsara infrastructure management framework**
**cluster**, **Physical Machine**, **Physical Machine IP**, **Capacity Type**, **Zone**, and **CPU**
**processor**.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

**Apsara Infrastructure Management Framework Cluster Dimension**

You can obtain capacity data by **Cluster**, **Zone**, and **CPU processor**. When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

##### 5.3.6.5 AnalyticDB for PostgreSQL

You can view the capacity of AnalyticDB for PostgreSQL to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **AnalyticDB for PostgreSQL**.
4. In the upper-right corner of the AnalyticDB for PostgreSQL Capacity page, select **All**
**clusters** or a specific cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the AnalyticDB for PostgreSQL Capacity page, view **Capacity**
**Overview** and **Cluster Capacity Allocation Rate Trend**.
In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters or a specific cluster, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
6. In the lower part of the AnalyticDB for PostgreSQL page, view the capacity data of the
corresponding AnalyticDB for PostgreSQL instance based on different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, you can configure the **Logical cluster** and
**Capacity Type** parameters to obtain capacity data.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click **Export** to export the capacity data to your computer. On the **Specification Inventory** tab, you can filter instance types by **Specification**
**Name** and **Specification Type** and then view the capacity data of the instance types.
You can click **Export** to export the inventory data of the instance types to your computer.

**Physical Machine Dimension**

You can obtain capacity data by **Apsara infrastructure management framework**
**cluster**, **Physical Machine**, **Physical Machine IP**, **Capacity Type**, **Zone**, and **CPU**
**processor**.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

**Apsara Infrastructure Management Framework Cluster Dimension**

You can obtain capacity data by **Cluster**, **Zone**, and **CPU processor**. When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

##### 5.3.6.6 PolarDB for PostgreSQL

You can view the capacity of PolarDB for PostgreSQL to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **PolarDB for PostgreSQL**.
4. In the upper-right corner of the PolarDB for PostgreSQL Capacity page, select **All clusters**
or a specific cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the PolarDB for PostgreSQL Capacity page, view **Capacity Overview**
and **Cluster Capacity Allocation Rate Trend**. In the **Capacity Overview** section, you can view the CPU capacity, memory capacity, and disk capacity of all clusters or a specific cluster, including the total capacity, used capacity, and capacity allocation rate. In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
6. In the lower part of the PolarDB for PostgreSQL page, view the capacity data of the
corresponding PolarDB for PostgreSQL instance based on different dimensions.

**Zone Dimension**

On the **Logical Cluster Capacity** tab, you can configure the **Logical cluster** and
**Capacity Type** parameters to obtain capacity data.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click **Export** to export the capacity data to your computer. On the **Specification Inventory** tab, you can filter instance types by **Specification**
**Name** and **Specification Type** and then view the capacity data of the instance types.
You can click **Export** to export the inventory data of the instance types to your computer.

**Physical Machine Dimension**

You can obtain capacity data by **Apsara infrastructure management framework**
**cluster**, **Physical Machine**, **Physical Machine IP**, **Capacity Type**, **Zone**, and **CPU**
**processor**.
When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

**Apsara Infrastructure Management Framework Cluster Dimension**

You can obtain capacity data by **Cluster**, **Zone**, and **CPU processor**. When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU allocation rate**, **Memory allocation rate**, or **Disk allocation**
**rate** columns to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

##### 5.3.6.7 PolarDB-X

You can view the capacity of PolarDB-X to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **PolarDB-X**.
4. View the following information in the upper part of the PolarDB-X Capacity page:
In the **Capacity Overview** section of the page, you can view the CPU capacity and memory capacity of all clusters, including the total capacity, used capacity, and capacity allocation rate.
**PolarDB-X Capacity Allocation Rate Trend**. In this section, you can view the trend
charts of **CPU** and **Memory** allocation rates for all clusters or a specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
5. In the **Capacity Details** section in the lower part of the PolarDB-X Capacity page, view the
capacity details of the clusters by **Cluster** and **CPU**. When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU Allocation Rate** or **Memory Allocation Rate** column to sort the cluster capacity data in ascending or descending order. You can click the name of a cluster to view the details of the physical machines in the cluster. You can click **Export** to export the capacity data to your computer.

##### 5.3.6.8 OceanBase

You can view the capacity of ApsaraDB for OceanBase to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **OceanBase**.
4. In the upper part of the page, view data in the **Top 5 Cluster Resource Allocation Rates**
and **Capacity Allocation Rate Trend** sections. In the **Top 5 Cluster Resource Allocation Rates** section, you can view the rankings of clusters by memory, CPU, and disk allocation rates. In the **Capacity Allocation Rate Trend** section, you can view the trend charts of memory, CPU, and disk allocation rates for clusters within different time periods. Move the pointer over a time node to view the recorded data.
5. In the lower part of the OceanBase Capacity page, view the capacity details of ApsaraDB for
OceanBase. You can click the name of a cluster to view the details of the physical machines in the cluster. When the allocation rate or usage is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU Allocation Rate**, **Memory Allocation Rate**, or **Disk allocation**
**rate** column to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

#### 5.3.7 Middleware capacity

##### 5.3.7.1 ApsaraMQ for Kafka

You can view the capacity of the ApsaraMQ for Kafka service to obtain the usage of the service resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Middleware**
**Capacity**.
3. In the left-side navigation pane, click **ApsaraMQ for Kafka**.
4. In the upper part of the page, view the trend chart that shows the **BYTES_IN** and
**BYTES_OUT** traffic throughput of a specific cluster within different time periods.
5. In the lower part of the page, view the capacity details of all clusters or a specific cluster.
From the **Cluster** drop-down list, select All Clusters or a desired cluster. Click **Export** to export the capacity data to your on-premises machine.

### 5.4 O&M change

This topic describes the modules related to change management.

**Modules**

| Module | Description |
|---|---|
| Log Cleanup | This module clears specific logs in specific containers or physical servers. |
| Process Approval | This module provides approval and management features for O&M workflows. |
| Version Management | This module provides management features for version changes. |

#### 5.4.1 Log cleanup

This topic describes the modules of the log cleanup module. This module allows you to clear logs from a specified container (Docker) or physical machine (virtual machine or bare metal).

**Modules**

| Module | Description |
|---|---|
| Rules | You can manage log cleanup rules by performing operations such as rule import, query, modification, export, and deletion. |
| Plans | You can execute log cleanup plans, including obtaining the usage data of containers or physical servers and clearing log. |
| Records | You can view detailed log cleanup records. |

##### 5.4.1.1 Rule management

This topic describes the process of importing log cleanup rules. If you have already set up log cleanup rules on your on-premises system, you can import one or more rules simultaneously into either containers or physical servers.

**Background information**

Imported rules are added to the existing ones without overwriting, thereby ensuring an incremental update. To verify if a cleanup rule already exists, carefully compare the values of the Product, Service, ServerRole, SrcPath, MatchFile, Threshold, and Method parameters against the rule you want to import. If every value matches within your environment, the rule is in place. If an identical rule is detected, the system will not allow the import of the duplicate rule. Prior to initiating a rule import, you must reach out to technical support to acquire an encryption sequence. After a rule is imported, any special characters including spaces, carriage returns, line breaks, and tabs within the rule are automatically removed. When setting the upper limit of disk space usage in a rule, make sure the range falls between 0% and 100%, and note that the digit preceding the percent sign (%) must be an integer. Failure to adhere to these requirements will result in the rule being automatically excluded during the import process. We recommend that you set the upper limit of disk space usage in a rule to 75%. When importing rules, you must verify that the included cleanup actions have been adequately tested and can function properly. Failure to do so may lead to unexpected exceptions when you execute these rules for log clearance.

**Import rules**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Log Cleanup**.
3. In the left-side navigation pane, click **Rules**.
4. Click the **Container** or **Physical Machines** tab.
5. Click **Import**. Click **Select a file to upload** . Then, select the XLS or XLSX file that you want
to import and click **Open** to import log cleanup rules. Upon importing rules, the corresponding execution plans are generated in an asynchronous manner.

**What to do next**

**Export log cleanup rules**

You can export multiple log cleanup rules from both containers and physical servers in a single batch operation.
1. Click the **Container** tab or the **Physical Machines** tab.
2. To export log cleanup rules from containers or physical servers, perform the following
operations: Export all rules: Click **Export** to export all log cleanup rules. Export a portion of rules: Click **Advanced Filter** to search for the log cleanup rules that you want to export by **Product**, **Service**, or **Server Roles**. Select the log cleanup rules and click **Export** to export them.

> **Note:** By default, the Product, Service, and Server Roles dropdown menus appear empty. Upon your first use, you must input a product, a service, or a server role, and then proceed to choose the relevant cleanup rules based on the conducted search. In subsequent search queries, the system will automatically present all viable choices within the Product, Service, and Server Roles dropdown menus.

**Modify log cleanup rules**

You can modify log cleanup rules to suit your business needs.
1. Click the **Container** tab or the **Physical Machines** tab.
2. Find the log cleanup rule that you want to modify and click **Modify** in the **Actions** column.
3. In the **Modify Log Cleanup Rule** dialog box, configure the **Maximum Disk Usage**
parameter and specify whether to enable **Whether to automatically delete**.

> **Note:** The range for maximum disk usage spans from 0% to 100%. The number preceding the percentage sign (%) must be an integer. We recommend that you set the Maximum Disk Usage parameter to 75%.
> To enable or disable the auto-delete feature for a log cleanup rule, simply toggle the switch in the **Automatic Deletion** column of the rule on the Rule Management page. Alternatively, you can click Enable Automatic Clearance or Turn off automatic cleanup to enable or disable a log cleanup rule.

4. Click **OK**.

> **Note:** To simultaneously enable or disable the auto-delete feature for multiple log cleanup rules, select those rules and click **Enable Automatic Clearance** or **Turn off** **automatic cleanup** in the lower part of the Rule Management page.
> After you modify a log cleanup rule, the system does not automatically adjust the corresponding execution plans associated with the rule. The execution plans stay as previously set. Every day at precisely 02:00:00, the system conducts a cleanup of previous execution plans and creates new plans based on the current settings of your log cleanup rules.

**Delete log cleanup rules**

You can delete log cleanup rules that are no longer required.
1. Click the **Container** tab or the **Physical Machines** tab.
2. Find the log cleanup rule that you want to delete and click **Delete** in the **Actions** column.
3. Confirm the message that appears and click **OK**.

> **Note:** When a log cleanup rule is deleted, the execution plans related to that rule are not removed concurrently. Every day at precisely 02:00:00, the system conducts a cleanup of previous execution plans and creates new plans based on the current settings of your log cleanup rules.

**Obtain execution plans**

1. Click the **Container** tab or the **Physical Machines** tab.
2. Find the log cleanup rule that you want to manage and click **Execution Plans** in the
**Actions** column. On the **Execution Plans** page, view the execution plans associated with
the log cleanup rule.

##### 5.4.1.2 Plans

This topic describes the execution plans of log cleanup rules, including how to query the disk usage of containers or physical machines and how to clear logs in execution plans.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Log Cleanup**.
3. In the left-side navigation pane, click **Plans**.
4. Click the **Containers** or **Physical Machines** tab.
5. In the upper part of the page, filter execution plans by **Product**, **Service**, or **Service Role**.

> **Note:** By default, no options are available in the Product, Service, and Service role drop-down lists. The first time you specify the fields, you must enter a product, service, and server role and select the corresponding search result. In subsequent queries, the system displays all available options in the drop-down lists.

6. Perform the following operations to query the disk usage of containers or physical
machines: Find the execution plan that you want to manage and click **Query Usage** in the **Actions** column. In the message that appears, click **OK**. Then, refresh the page and view the disk usage in the **Disk Usage** column. Select the execution plans that you want to manage and click **Batch Query Usage** in the lower-left part of the page. In the message that appears, click **OK**. Then, refresh the page and view the disk usage in the **Disk Usage** column.
7. Perform the following operations to clear logs in execution plans:
Find the execution plan that you want to manage and click **Execute Clearance** in the
**Actions** column. In the message that appears, click **OK**.
Select the execution plans that you want to manage and click **Batch Clear**. In the message that appears, click **OK**.

> **Note:** The log cleanup operation is an asynchronous operation. If you want to view the log cleanup results, go to the **Records** page.

8. Find the execution plan that you want to manage and click **Cleanup Records** in the
**Actions** column. The **Records** page appears.

##### 5.4.1.3 Records

This topic describes how to view the detailed records of log cleanup operations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Log Cleanup**.
3. In the left-side navigation pane, click **Records**.
4. View the following information at the top of the page.
Each time you perform a log cleanup operation, the values of **Clear Operations**, **Server**
**Roles**, and **Machines** are increased by one.
The value of **Log Files to clear** shows the number of log files that match all the available cleanup rules and that can be cleaned up, rather than the number of log files that have been cleaned up. The value of **Cleared Capacity (GB)** shows the accumulated available space after you clean up logs.
5. Filter cleanup records by a combination of **Product**, **Service**, and **Service Role**.

> **Note:** By default, no options are available in the Product, Service, and Service role drop-down lists. The first time you specify the fields, you must enter a product, service, and server role and select the corresponding search result. In subsequent queries, the system displays all available options in the drop-down lists.

6. Click **View Details** in the **View Details** column of the desired cleanup record to view the
detailed cleanup information.

#### 5.4.2 Plan management

This topic describes the features of plan management.

**Features**

| Feature | Description |
|---|---|
| Base Plans | Displays the preset O&M actions that can be initiated and executed on the base. |

##### 5.4.2.1 Base plans

> The Base Plans page displays the preset O&M actions that can be initiated and executed on the base.

The following types of base plans are supported: Workflow: For more information, see Workflow types. Link: For more information, see Link types.

###### 5.4.2.1.1 Workflow types

Base plans of the workflow type are preset O&M actions that are orchestrated by the process engine. This topic describes how to execute a plan of the workflow type, view execution history of plans, and view the details of a plan.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the Plan List tab, click **Advanced Filter**, select Workflow from the **Plan Type** drop-
down list, and then click **Search** to search for plans of the workflow type.
5. Query the details of a plan.
i. Find the plan that you want to view and click **Details** in the **Actions** column. ii. The **Plan Details** page includes the **Basic Information** section and the **Plan**
**Description**, **Workflow**, **Input Parameters**, **Output Result**, and **Workflow YAML**
tabs. iii. On the **Workflow** tab, find **Container Task** and click **Task YAML** to obtain the YAML information of the task.
6. Execute the plan.
Method 1 a. On the Plan List tab of the Base Plan page, find the plan and click **Execute** in the
**Actions** column.
b. In the dialog box that appears, specify the required parameters and click **Execute**. Method 2 a. On the Plan Details page, click **Execution plan** in the upper-right corner. b. In the dialog box that appears, specify the required parameters and click **Execute**.
7. View the execution history of the plan.
i. On the Plan List tab of the Base Plan page, find the plan and click **History** in the **Actions** column. Alternatively, you can click **Execution History** in the upper-right corner of the Plan Details page. ii. View the execution history of the plan. iii. Find the execution record that you want to view and click **Details** in the **Actions** column. iv. You are redirected to the **Plan Execution History** page, which includes the **Basic**
**Information** section and the **Step**, **Input Parameters**, **Output Result**, and **Workflow**
**Instance YAML** tabs.
v. On the **Step** tab: If the task is in the Complete state, click **Details** of the task to go to the **Task**
**Instance Details** panel.
If the task is in the Failed state, select **Retry** from the **Actions** drop-down list to submit the task again.

**Other operations**

**Obtain the execution history of all plans**

1. On the **Execution History** tab, click **Advanced Filter** to filter execution history of plans
by **ID**, **Plan Name**, **Execution Time**, **Execution Result**, and **Remarks**.
2. Find the execution record and click **Details** in the **Actions** column.
3. You are redirected to the **Plan Execution History** page, which includes the **Basic**
**Information** section and the **Step**, **Input Parameters**, **Output Result**, and **Workflow**
**Instance YAML** tabs.
4. On the **Step** tab:
If the task is in the Complete state, click **Details** of the task to go to the **Task Instance**
**Details** panel.
If the task is in the Failed state, select **Retry** from the **Actions** drop-down list to submit the task again.

###### 5.4.2.1.2 Link types

Base plans of the link type are used to resolve issues in specific O&M scenarios. This topic describes how to execute plans of the link type in different scenarios.

| Scenario | Procedure |
|---|---|
| VM Transfer | VM transfer |
| Primary/Secondary Control Host Switchover | Docker host switchover |
| NC Scale-in | NC scale-in |
| NC Scale-out | NC scale-out |
| Control Host Scale-in | Docker host scale-in |
| Control Host Scale-out | Docker host scale-out |
| Cluster Startup/Shutdown | Cluster startup and shutdown |

###### 5.4.2.1.2.1 VM transfer

This topic describes how to migrate VMs between Docker hosts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Plan**
**Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, click **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for plans of the link type.
5. In the plan list, find the plan whose name is**VM Transfer** and click **Details** in the Actions
column to go to the Plan Details page.
6. The Plan Details page includes two sections: Basic information and Operation and
Maintenance. Basic information: displays the basic information about the plan, including **Plan ID**, **Plan**
**Name**, **Plan type**,**Risk level**,**Version**, and **Scenario description**.
Operation and Maintenance: a. In the upper-right corner, click **Execution plan**. In the **Execute** dialog box, configure the **SOURCE host** and **VM to be migrated** parameters and click **Confirm**. b. Perform a precheck.

> **Note:** You can click **Termination** in the lower part of the page to stop the migration.

a. In the **Pre-Check** step, click **Perform pre-check**. In the message that appears, click
**OK**.

> **Note:** If the check status is **Failed**, move the pointer over the
> icon to view the cause
> of the failure. Click **Retry** in the Operation column to check again.

b. After the precheck is complete, click **Next Step**.

> **Note:** If a VM does not pass the precheck, the **Operation confirmation** dialog box appears. You can select the VM that you want to ignore and click **OK**.

c. Confirm the VM

> **Note:** You can click **Termination** in the lower part of the page to stop the migration.

a. Click **Scheduling trial**. In the **Operation confirmation** dialog box, specify the

**Whether to allow recommend of the destination host to be equal to the**

**source host** parameter, and click **OK**.

> **Note:** If the trial calculation status is **Failed**, move the pointer over the
> icon to
> view the cause of the failure.
> To change the destination host, click **Replace the target host** in the Operation column. In the dialog box that appears, select a host from the **Destination host** drop-down list, and click **Confirm**.

b. Click **Next Step**. d. Perform the migration. Before the migration starts, you can click **Termination** in the lower part of the page to stop the migration. After the migration starts, you cannot stop the migration. You must wait until the migration is complete. a. In the **Perform migration** step, click **Perform migration**. In the message that appears, click **OK**.

> **Note:** If the migration is in the **Failed** state, move the pointer over the
> icon to
> view the cause of the migration failure, and click **Retry** in the Operation column to perform the migration again.
> Click **VM details** in the Operation column to go to the machine details page.

b. When the migration is in the **Passed** state, click **Complete**.

###### 5.4.2.1.2.2 Docker host switchover

This topic describes how to switch over primary and secondary Docker hosts.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **Primary/Secondary Control Host Switchover** plan and
click **Details** in the Actions column to go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
In the Operation and Maintenance section a. You can select the source and destination hosts. b. Click**Submit**to confirm the operation.

###### 5.4.2.1.2.3 NC scale-in

This topic describes how to scale in an SRG of the worker type.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **NC Scale-in** plan and click **Details** in the Actions column to
go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
In the Operation and Maintenance section a. Select the destination cluster and destination SRG, select the machines that you want to scale in from the Available Machines list, and click the icon to add them to the Selected Machines list.

> **Note:** The destination SRG must meet the following requirements:
> It is defined in the cluster desired state file machine_group.conf.
> scalable == true
> The machine group must contain machines other than Docker hosts.

b. Click **Submit** and then confirm the operation. c. The physical machine scale-out task is submitted. You can view the scale-out task in the following way: Choose **Platform O&M >**
**Apsara Infrastructure Management > Resources > Machine Management**.
On the Machines page, click **Advanced Filter**, select In O&M from the **Status** drop-down list, and then click Search to check the scale-in condition.

###### 5.4.2.1.2.4 NC scale-out

This topic describes how to scale out an SRG of the worker type.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **NC Scale-out** plan and click **Details** in the Actions column to
go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
In the Operation and Maintenance section a. You can select Destination Cluster and Destination SRG. The destination SRG must meet the following requirements: It is defined in the cluster desired state file machine_group.conf. scalable == true The machine group must contain machines, so that the system can randomly select one of them as the benchmark machine for scale-out. b. Select machines from the Available Machines list and click the icon to add them to the Selected Machines list. The selected machines must meet the following requirements: They belong to the default cluster. They are in the Good state and have no actions performed. c. Click **Submit** and then confirm the operation. d. The physical machine scale-out task is submitted. You can view the scale-out task in the following way: Choose **Platform O&M >**
**Apsara Infrastructure Management > Resources > Machine Management**.
On the Machines page, click **Advanced Filter**, select In O&M from the **Status** drop-down list, and then click Search to check the scale-out condition.

###### 5.4.2.1.2.5 Docker host scale-in

This topic describes how to scale in the DockerHost#Buffer machine group of the tianji cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **Control Host Scale-in** plan and click **Details** in the Actions
column to go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
In the Operation and Maintenance section a. Select the destination cluster and destination SRG, select the machines that you want to scale in from the Available Machines list, and click the icon to add them to the Selected Machines list. You can only scale in tianji clusters. The machine group must meet the following requirements: It is defined in the cluster desired state file machine_group.conf. scalable == true The name (which is case-insensitive) starts with DockerHost#. b. Click **Submit** and then confirm the operation. c. The Docker host scale-in task is submitted. No running VMs are allowed on the machine to be scaled in. You can view the scale-out task in the following way: Choose **Platform O&M**

**> Apsara Infrastructure Management > Resources > Machine**

**Management**. On the Machines page, click **Advanced Filter**, select In O&M
from the **Status** drop-down list, and then click Search to check the scale-in condition.

###### 5.4.2.1.2.6 Docker host scale-out

This topic describes how to scale out the DockerHost#Buffer machine group of the tianji cluster.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **Control Host Scale-out** plan and click **Details** in the Actions
column to go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
Select the destination cluster and destination SRG, select the machines that you want to scale out from the Available Machines list, and click the icon to add them to the Selected Machines list. Click **Submit** and then confirm the operation. The Docker host scale-out task is submitted. You can view the scale-out task in the following way: Choose **Platform O&M >**
**Apsara Infrastructure Management > Resources > Machine Management**.
On the Machines page, click **Advanced Filter**, select In O&M from the **Status** drop-down list, and then click Search to check the scale-out condition.

###### 5.4.2.1.2.7 Cluster startup and shutdown

This topic describes how to start up and shut down all the software programs and physical machines in a cluster.

**Warning**

This is a high-risk operation and will shut down services. Generally, the shutdown operation must be performed in the required sequence. Contact on-site engineers or GTS for assistance.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **O&M Change** > **Plan Management**.
3. In the left-side navigation pane, click **Base Plans**.
4. On the **Plan List** tab, show **Advanced Filter**, select Link from the **Plan Type** drop-down
list, and then click **Search** to search for linked plans.
5. In the plan list table, find the **Cluster Startup/Shutdown** plan and click **Details** in the
Actions column to go to the Plan Details page.
6. The Plan Details page includes two sections: Basic Information and Operation and
Maintenance. The Basic Information section includes the following fields: **Plan ID**, **Plan Name**, **Plan**
**Type**,**Risk Grade**,**Version**, and **Scene Description**.
In the Operation and Maintenance section You can select the doing,pending,approved, and done states to filter clusters. a. You can click **Add Clusters for Shutdown**. In the Add Clusters for Shutdown dialog box, selectclustersand click**OK**. b. Confirm the operation. c. The shutdown task is submitted. If you shut down the tianji cluster, the environment cannot be connected. You must contact Alibaba Cloud technical support to start the cluster. d. Select the clusters in the cluster list table and then click **Batch Start** to start the clusters. e. Confirm the operation. f. The cluster startup task is submitted.

#### 5.4.3 Process approval

This topic describes the modules of the Process Approval module.

**Modules**

| Module | Description |
|---|---|
| My Submission | You can view the list of O&M workflows that you submitted. You can also query or cancel these workflows. |
| Pending Approval | You can view the O&M workflows that are submitted for your approval. You can also query and approve these O&M workflows. |

##### 5.4.3.1 My submission

On the **My submission** page, you can view the details of O&M workflows that are submitted by the current user. You can also revoke submitted O&M workflows on this page.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Process**
**Approval**.
3. In the left-side navigation pane, click **My Submission**.
4. On the **My submission** page, view a comprehensive list of all O&M workflows that have
been submitted. You can also click **Advanced Filter** to filter workflows by **Workflow order number**,
**Execution status**, **Workflow title**, **Creation time**, and **Belonging products**.
5. Perform the following operations based on your business requirements.

| Operation | Description |
|---|---|

| View the details of an O&M workflow | i. Find the desired O&M workflow and click the order number of the workflow or View details in the Operation column. ii. On the Workflow details page, view the basic information and progress of the workflow. iii. (Optional) In the upper-right corner of the Workflow details page, click View O&M details. You are redirected to the Plan Task details page. On the Plan Task details page, view the O&M details. |
|---|---|
| Cancel an O&M workflow | Note You can cancel an O&M workflow only when the workflow is in the Pending Approval state. i. Find the desired O&M workflow and click Revoke in the Operation column. ii. In the message that appears, click OK. |

##### 5.4.3.2 My approval

The **Pending Approval** page enables users to access and manage O&M workflows awaiting their approval. From this page, users can approve, reject, or delegate these workflows as needed.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Process**
**Approval**.
3. In the left-side navigation pane, click **My Approval**.
4. View a comprehensive list of all O&M workflows pending approval.
You can click **Advanced Filter** to filter workflows by **Workflow order number**,
**Execution status**, **Workflow title**, **Creation time**, and **Belonging products**.
5. Find the O&M workflow that you want to manage and click the order number of the
workflow or **View details** in the **Operation** column to view the basic information and approval progress of the workflow.

> **Important:** You can approve an O&M workflow only when the workflow is in the **Pending** **approval** status.

6. In the **Approval progress** section, approve the O&M workflow.
Approve: Click **Agree**. In the message that appears, click **OK**. Reject: Click **Reject**. In the message that appears, click **OK**. Transfer: Enter your comments and click **Transfer**. In the dialog box that appears, select the user to whom you want to transfer the workflow and click **OK**.
7. (Optional) In the upper-right corner of the workflow details page, click **View O&M details**.
You are redirected to the **Plan Task details** page. On the Plan Task details page, view the O&M details.

#### 5.4.4 Version management

##### 5.4.4.1 Package management

On the Package management page, you can view the details of product packages and patch packages.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Version**
**Management**.
3. In the left-side navigation pane, click **Version Package**.
4. On the **Product Package List** tab of the Package management page, perform the
following operations: View the product package information, including **Exact version**, **Median version**,
**Cloud products**, **Support architecture**, **Deployment form**, and **Import time**.
Specify values for the **Cloud products** and **Median version** parameters to search for a product package. Find the product package that you want to view and click **Details** in the **Operation** column. The details page of the product package appears, including the **Basic**
**information**, **Dependency information**, and **Component details** sections.

> **Note:** In the **Dependency information** section, turn on **Strong Dependency** in the upper-right corner. Then, only the information about strong dependencies is displayed.

5. On the **Patch Package List** tab of the Package management page, perform the following
operations: View the patch package information, including **Patch version**, **Cloud products**,
**Product Version**, **Target service**, **Target component**, **Edited version**, **Support**
**architecture**, and **BuildID**.
Click **Advanced Filter** and search for a patch package by **Cloud products**, **Service**,
**Component**, and **Product Version**.
Find the patch package that you want to view and click **Details** in the **Operation** column to view the details of the patch package.

##### 5.4.4.2 Product version management

On the Product Version Management page, you can view the details of product versions and component versions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **O&M Change** > **Version**
**Management**.
3. In the left-side navigation pane, click **Product Version Management**.
4. On the **Product version list** tab of the Product Version Management page, perform the
following operations: View the product version information, including **Cloud products**, **Use Version**,
**Dependency status quo**, **Component version status**, **Is there a Patch**, and **Update**
**results**.
Click **Advanced Filter** and search for a product version by **Cloud products**,
**Component version status**, **Dependency status quo**, and **Is there a Patch**.
Find the product version that you want to view and click **Details** in the **Operation** column. The details page of the product version appears, including the **Basic**
**information** section and the **Cluster version details**, **Version dependency details**,
and **Component version details** tabs. On the **Cluster version details** tab, find the cluster that you want to view and click
**View clusters** in the **Operation** column to go to the **Cluster Details** page of the
cluster. For more information, see Cluster details. On the Cluster version details tab, find the cluster that you want to view and click **View product packages** in the
**Operation** column to go to the **Product package details** page.
On the **Version dependency details** tab, turn on **Strong Dependency** in the upperright corner. Then, only the information about strong dependencies is displayed. Click
**Click View** in the **Dependency description** column to view the dependency
description. Click **Product Version details** in the **Operation** column to go to the version details page of the dependent cloud product. On the **Component version details** tab, select **Only components with patches**
**are displayed.** in the upper-right corner. Then, the component versions whose value
of **Is there a Patch** is **Yes** are displayed. On the Product version list tab of the Product Version Management page, find the product version that you want to update and click **Update** in the **Operation** column to update the product version. In the upper-right corner of the Product version list tab, click **One-Click Update** to update all product versions.
5. On the **Component version list** tab of the Product Version Management page, perform
the following operations: View the component version information, including **Cloud products**, **Cluster**, **Use**
**Version**, **Service**, **Component**, **Benchmark BuiIdID**, **Current BuiIdID**, **Is there a**
**Patch**, **Component version status**, and **Patch version**.
Click **Advanced Filter** and search for a component version by **Cloud products**,
**Cluster**, **Service**, **Component**, **Is there a Patch**, and **Component version status**.
On the Component version list tab, select **Only components with patches are**
**displayed.** in the upper-right corner. Then, the component versions whose value of **Is**
**there a Patch** is **Yes** are displayed.

### 5.5 Disaster recovery management

**management**

This topic lists the following consoles for disaster recovery management: ASR for zone-disaster recovery ASR for geo-disaster recovery

### 5.6 Log center

This topic describes the features of the log center.

**Purpose**

The log center is designed to collect the logs generated by systems and applications in Apsara Uni-manager and implement the centralized storage and management of logging data. The log center supports real-time log view, search, and tracking, records and analyzes system operations, error messages, warnings, and other important events to help you identify issues, optimize performance, and perform security analysis.

**Application value**

The log center implements centralized collection, storage, and analysis of logging data of separate systems, helps you quickly identify and resolve O&M issues, and improves O&M response speed and business stability.

**Modules**

| Module | Description |
|---|---|
| Log map | This module provides an overview of platform logs, displays the services that are integrated for unified logging, and displays log data. |
| Log viewing | This module allows you to query logs of multiple Apsara services and service roles. This helps you troubleshoot issues. |
| Logging dump | This module allows you to dump the logs of the Apsara base to Simple Log Service or OSS on the tenant side. This helps meet the requirements for security compliance. |
| Water-level monitoring | This module allows you to monitor the log storage usage and traffic data of the base, which facilitates log management. |

#### 5.6.1 Log map

This topic describes how to access Log Map, a tool that visualizes log data from various interconnected services and products.

**Prerequisites**

You are granted the read and write permissions on Log Center.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Map**.
3. In the upper-right corner of the displayed page, view data of the following parameters: **All**
**Involved Products**, **Run Log-specific Products**, and **Operation Log-specific**
**Products**.
4. In the upper part of the displayed page, view the following sections:
**Log Statistics**: shows the total log count for the interconnected products and the count
for each log type.
**Acquisition Type**: shows the count of logs grouped by their respective collection
methods.
5. In the lower part of the displayed page, filter logs by a custom combination of **Products**,
**Service**, **Log Type**, **Log Name**, **Status**, **Acquisition Type**, and **Transfer status**.
6. In the lower part of the displayed page, view the following information: **Product Name**,
**Service**, **Log Type**, **Log Name**, **Storage Type**, **Log storage duration**, **Storage Status**,
**Acquisition Type**, **Ownership account**, **Transfer status**, and **Log Size**.
7. Click **Details** in the **Operation** column of the desired log to go to the log details page.
**Log information**: You can view the settings of **Log Name**, **Log Type**, **Log capacity**
**size**, **Creation time**, **Project**, **LogStore**, **Tags**, **Log Description**, and **Log Status**.
**Document Connection**: For hosted log types, you can view the log collection
configurations that you established for log access. These configurations are displayed for your reference only. In case you wish to revise the log access configurations, you must either change the product baseline settings or navigate to the Apsara Infrastructure Management console to make changes to the definitive configurations of the desired cluster.
**Storage Configuration**: You can view the storage-related configurations for log
access, such as Logstore indexing settings. The configurations are used for reference only. In case you wish to revise the storage-related configurations, you must either change the product baseline settings or navigate to the Apsara Infrastructure Management console to make changes to the definitive configurations of the desired cluster.
**Log attribution**: You can view information such as **Attributable Product**,**Service**
**Name**, **Service Role**, and**Primary account** of the desired log.
**Desensitization Configuration**: You can fully control field-level log desensitization
settings, allowing you to add, view, modify, or remove them as needed. This process ensures that when logs are collected by Simple Log Service, sensitive information in specified fields is securely masked, preventing unauthorized storage or disclosure.
**Edit**: Click **Edit** in the **Operation** column to modify the desired data desensitization
configuration.
**Delete**: Click **Delete** in the **Operation** column of the desired data desensitization
configuration. In the message that appears, confirm the information and click **Delete**.
**Add**: Click **Add** to add a data desensitization configuration. In the dialog box that
appears, configure **Field**, **Type**, **Replace Constant**, **Prefix regular**, and **Content**
**regular**.

| Parameter | Description |
|---|---|
| Field | The fields extracted from the Document Collection configuration, visible in the upper right corner of the log details page. These fields are required to undergo desensitization as part of the log collection process. |
| Type | You can select const or md5. If you select const, sensitive data will be automatically swapped with the content defined in the Replace Constant text box. If you select md5, sensitive data will be transformed into its unique MD5 cryptographic hash, thereby boosting security measures. |
| Replace Constant | The non-changing value that is used to replace sensitive data within the specified field, ensuring confidentiality. |
| Prefix regular | The regular expression that serves to identify the initial part of sensitive data by matching specific patterns. It acts as a search tool to locate and pinpoint sensitive content within the log information. |
| Content regular | The matching rule that establishes the criteria for selecting which data entries should undergo processing or transformation. |

**Machine Status**: You can inspect a registry of machines associated with the present log,
which provides essential details such as machine names, IP addresses, and account information. You can click Retry in the Operation column to facilitate resending the primary account information, as noted in the Log attribution section, to the respective machines. This step is pivotal in verifying and securing the necessary permissions for uninterrupted log collection.

**What to do next**

**Operation records**

You can click **Operation Record** in the **Operation** column of the desired log to open the
**Operation Record** panel where you can view information such as **Operation Name**,
**Operation content**, **Status**, **Operator**, and **Operation time**.

**Enable acquisition**

Enable log collection for a single product: Click **Open acquisition** in the **Operation** column of the desired product. In the message that appears, click **OK** to allow logs to be collected to the Simple Log Service platform. Enable log collection for multiple products: Select multiple products and click **Open**
**Acquisition** in the lower part of the page. In the message that appears, click **OK** to allow
logs to be collected to the Simple Log Service platform.

**Disable acquisition**

Disable log collection for a single product: Click **Close Acquisition** in the **Operation** column of the desired product. In the message that appears, click **OK** to permit logs from being collected to the Simple Log Service platform. Disable log collection for multiple products: Select multiple products and click **Close**
**Acquisition** in the lower part of the page. In the message that appears, click **OK** to permit
logs from being collected to the Simple Log Service platform.

#### 5.6.2 Log query

This topic describes thelog query feature that is designed to facilitate efficient filtering, searching, and in-depth analysis of diverse log data across multiple products. This empowers you to derive valuable insights from logs within complex distributed systems, thereby enabling swift issue identification and resolution.

**Prerequisites**

You are granted the read and write permissions on Log Center.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Query**.
3. Filter log data by a combination of **Products**, **Link TraceId**, **Query Parameters**, **Time**
**range**, **Log Type**, and **Log Name**. When conducting a log query, you must specify
**Products** and **Time range**.
4. View the query results displayed at the bottom of the following page:
On the left side of the page: you can use the navigation pane to input a log name or a server role to narrow down your query scope. On the right side of the page, you can view the following information: **Product Name**,
**Service name**, **Service Role**, **Log Name**, **Number of logs**, and **Number of error**
**logs**. You also input a keyword to pinpoint precise log entries. Additionally, if you select
Show exception logs only, the system displays only logs that record exceptions. You can view the specific content of a log.
**Export List**: You can click this button to export the log content.
**List**: You can click this button to display the desired log content in a list.
**Aggregate**: You can click this button to display the desired log content in an aggregated
manner.
**Details**: You can click this button to navigate to the log details page, where you can
retrieve the full log content.

#### 5.6.3 Log Dump

This topic describes the log transfer feature designed to transfer logs from SLS-Inner to either SLS-Pub or Object Storage Service (OSS). Implementing this feature enables long-term, secure storage of platform-side logs, enhancing platform security and ensuring regulatory compliance.

**Prerequisites**

You are granted the read and write permissions on Log Center.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Dump**.
3. Select the transfer type.
**Offline transfer**: This type enables the offline transfer of service logs from SLS-Inner to
SLS-Pub. This offers a highly efficient solution ideal for archiving logs over extended periods. Once offline transfer is configured, tasks are automatically created based on individual Logstores. These tasks can be viewed and managed on the Task Management tab.
**Real-time synchronization**: This type facilitates the real-time synchronization of
service logs from SLS-Inner to SLS-Pub. However, if the immediate synchronization of desired logs is not required, we recommend that you use the offline transfer method instead. Once real-time synchronization is configured, tasks are automatically created based on individual Logstores. These tasks can be viewed and managed on the Task Management tab.
**OSS archive**: This type involves transferring logs from SLS-Inner to OSS in an offline
mode, where the logs are securely archived in OSS. Once OSS archive is configured, tasks are automatically created based on individual Logstores. These tasks can be viewed and managed on the Task Management tab.

> **Note:** The **Offline transfer** and **OSS archive** methods generate log transfer tasks for the preceding 24 hours, utilizing diverse transfer configurations to ensure comprehensive log management.
> Upon submission of configurations, the **real-time synchronization** method initiates two log transfer tasks, which concurrently transfer logs in real time across two dedicated transfer nodes.

4. On the **Task Management** tab, filter task data by **Products** or **Log Type**. You can view
the following information: **Source Project, Source LogStore**, **Log attribution**
**information**, **Target Organization**, **Target Project**, **Target LogStore**, **Log storage**
**duration**, **Server-side encrypted storage**, and **Transfer status**.
**Related Log List**: You click **Related Log List** in the Log attribution information column
to view **Product Name**, **Service Name**, **Service Role**, **Log Name**, and **Log Type**.
**Operation**: Click **Delete** in the Operation column of the desired task or select multiple
tasks and click **Batch Delete** in the lower part of the page. In the message that appears, confirm the information and click **Delete** to delete the selected one or more tasks.
5. On the **Task List** tab, view the specific transfer tasks created from the transfer
configurations and search for desired tasks by **Products**, **Log Type**, **Time**, or **Status**. The task list provides the following information: **Task ID**, **Source Project**, **Source LogStore**,
**Target Organization**, **Target Project**, **Target LogStore**, **Start Time**, **Status**,
**Progress**, and **Time consuming**. Valid values of **Status** include To be transferred, In
Transfer, Abnormal, Delay, Completed, and Cancelled.
6. Click **New Log Transfer Task**. Log transfer tasks play a vital role in managing and
preserving system logs, ensuring adherence to long-term storage needs and effective log management.

> **Note:** For any given Logstore, you can create only log transfer tasks of identical type to maintain consistency in log management operations. The setup processes for **offline** **transfer**, **real-time synchronization**, and **OSS archive** are alike, featuring similar configuration steps for ease of use.

In the **Select Log** step, search for logs by **Products**, **Log Type**, or **Transfer status**. Select the desired logs and click **Next step** to enter the **Authorization Configuration** step. In the **Authorization Configuration** step, configure **Log storage duration (days)**,
**ARN**, **Geography**, **Organization**, **Resource Set**, and **Log encryption storage**. **ARN**
specifies the Alibaba Cloud Resource Name (ARN) of the RAM role that completes the authorization. Guidance for acquiring the ARN is provided in the Appendix section. During the authorization process, you will need the content of both **Permission Policy** and
**Credit policy**. To easily retrieve these, simply click the **Obtain RAM authorization**
**information** link conveniently placed to the right of the ARN text box. After the
configuration is complete, click **Next step** to enter the **Logstore configuration** step.

| Parameter | Description |
|---|---|
| Log storage duration (days) | The storage duration of logs after they are transferred. The default value is 180 days. |
| ARN | The ARN of the RAM role that authorizes the log transfer task. To obtain the correct ARN, reach out to the administrator of your level-1 organization. Comprehensive instructions for fetching the ARN are included in the Appendix section. Once you have this ARN, enter it into the designated field on the Transfer Destination Storage Configuration page to continue with the setup process. |
| Geography | The region where the data center of Simple Log Service resides. |
| Organization | The destination organization where you intend to transfer your logs. It is within this organization that necessary resources, like Simple Log Service projects and OSS buckets, will be created. When a resource sharing the same name already exists, ensure that the chosen organization is granted the necessary permissions to access that resource. |
| Resource Set | The destination resource set where you intend to transfer your logs. It is within this resource set that necessary resources, like Simple Log Service projects and OSS buckets, will be created. |
| Log encryption storage | Upon enabling log encryption storage, you gain the capability to encrypt your logs either on a Simple Log Service server or an OSS server. Enabling encryption does not restrict console accessibility, but do note that encryption and decryption processes may elevate server workload. Therefore, whether to enable this feature should be decided based on your specific business requirements. |

In the **Logstore configuration** step, preview the settings of the **Project**, **LogStore**,
**Log Details**, **Target Project**, **Target LogStore**, and **Transfer Target Resource**
**Status** parameters. By default, the **Target Project** and **Target LogStore** parameters
are automatically set to match the configurations of the **Project** and **LogStore** parameters prior to transfer. However, if the logs cannot be transferred to a project bearing the same name or if you have unique business requirements, you can manually adjust the settings of the Target Project and Target LogStore parameters to meet your business requirements. Click **Complete Create**. The log transfer task is created.

**Appendix 1: RAM role-based authorization**

1. . Log on to the Apsara Uni-manager Management Console by**

**using the administrator credentials of the respective**

**organization.**

If you are not authorized to perform this operation, contact an administrator of the destination organization (level-1 organization) for assistance.
2. . Create a RAM role and grant the required permissions to the**

**role.**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Enterprise**. In the left-side navigation pane, choose
**Permissions** > **Role Permissions**.
3. Click **Create Role** in the upper-left corner of the displayed page. In the **Advanced**
**Settings** section, click **Create RAM Role & Attach Policy** .
4. Set **Role Name** to log-dump-role and **Description** to RAM role for platform-side log
transfers. Then, click **Next**.
5. In the **Policy Name** field, enter log-dump-policy. Copy the **Permission Policy** content
provided by **Obtain RAM authorization information** on the Transfer destination storage configuration page, paste it in the **Policy Content** text box, and then click **OK**.
6. Search for and select the created policy, and then click **Next** in the lower-right corner of the
page.
7. Copy the Credit Policy content provided by **Obtain RAM authorization information** on
the Transfer destination storage configuration page, paste it in the **Trust Policy** text box, and then click **Next**.
8. Preview and confirm the **Permission Policy** and **Trust Policy** content, and click **Create** in
the lower-right corner.
9. On the Role Permissions page, search for **log-dump-role**. Click the role name to go to the
**RAM Role** tab of the role details page. Click **Create**, select the level-1 organization to
which you want to transfer logs, and then click **OK**.
0. On the details page of the created **RAM role**, copy the corresponding **ARN**, paste it in the
designated field on the Transfer destination storage configuration page, and then complete the authorization.

#### 5.6.4 Log monitoring

This topic describes the real-time log monitoring feature, which enables users to promptly track and receive alerts on log data growth, thereby proactively preventing issues related to storage capacity constraints.

**Prerequisites**

You are granted the read and write permissions on Log Center.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Monitor**.
3. **Log Capacity**
In the upper part of the tab, you can view the **Capacity usage trends** chart, on which information about **Total storage capacity** and **Use storage capacity** is displayed. In the lower part of the tab, you can view information about **Capacity Details**. You can search for specific logs by **product** or **date** to view their respective storage sizes. For every log entry, the following information is displayed: **Date**, **Geography**, **Products**,
**Used (GB)**, **Product available (GB)**, and **Utilization rate (%)**.
4. **Log Traffic**:
In the upper part of the tab, you can view the **Total flow (MB/min)** chart, which visually presents the overall distribution trend of traffic.

> **Note:** You can query the total log traffic based on time, though queries are confined to data from the past seven days.

In the lower part of the tab, you can view information about **Flow details**. You can search for specific logs by **Products**, **Log Type**, or **Time**. For every log entry, the following information is displayed: **SlsProject**, **LogStore**, **Related Products**, **Log**
**Type**, and **Log Traffic**.

> **Note:** Concurrent base logs are stored exclusively in either sls-inner or sls-pub. Prior to transitioning to the sls-pub deployment mode, only sls-inner is displayed.

## 6 Product O&M

This topic lists the products for which you can perform O&M operations in the Apsara Unimanager Operations Console.

| Category | Product |
|---|---|
| Computing | Compute Operations Console |
|   | ECS Diagnosis |
|   | BMS Operations Console |
|   | Container operation console |
| Network | Network Operations Console |
|   | Apsara Network Intelligence |
| Storage | CDS |
|   | Apsara Distributed File System |
|   | EBS |
|   | OSS Storage Operations and Maintenance System |
|   | NAS Storage Operations and Maintenance System |
|   | Tablestore Storage Operations and Maintenance System |
| Database | ApsaraDB Operations and Maintenance System |
|   | DTS |
|   | DRDS Manager |
|   | Data Replication System |

|   | ApsaraDB for OceanBase |
|---|---|
|   | Database Backup |
|   | ApsaraDB Operations and Maintenance System |
| Middleware | Tlog |
|   | Global Transaction Service |
|   | CSB |
| Big data | Apsara Bigdata Manager |
|   | Elasticsearch |
|   | Dataphin |
| Security service | Apsara Stack Security |

t

## 7 Security management

### 7.1 Security audit

This topic lists the following consoles that support security audit: ActionTrail Apsara Stack Security - Security Audit

#### 7.1.1 Operation audit

##### 7.1.1.1 Console-based Audit

You can query the records of operations that are performed in the console by users. By default, the operation records in the previous 24 hours are displayed.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Security Audit** > **Operation**
**Audit**.
3. In the left-side navigation pane, click **Console-based Audit**.
4. On the **Console-based Audit** page, perform the following operations based on your
business requirements: View operation records Specify the **Username** and **Time Range** parameters to filter operation records. Export operation records

> **Note:** You can export a maximum of 10,000 records. If you select more than 10,000 records, only the first 10,000 records are exported.

Batch Export: Select the operation records that you want to export and click **Batch**
**export** below the list to export the selected records.
Export All: Select the check box next to Time and click **Export** above the list to export all the operation records that are displayed on the current page.

##### 7.1.1.2 CLI-based Audit

t You can view the records of operations that are performed in the CLI by users on servers or containers. By default, the operations logs of the previous 24 hours are displayed. You can query the operation records that were generated up to one week ago.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Security Audit** > **Operation**
**Audit**.
3. In the left-side navigation pane, click **CLI-based Audit**.
4. On the **CLI-based Audit** page, perform the following operations based on your business
requirements: Query operation records Select **Log source**, **Linux account**, **Machine/container**, or **Operation Time** and specify a value to view records. You can also click Advanced Filter and specify a combination of the preceding parameters to filter records. Export operation records Select the records that you want to export and click **Export List** to export the selected records. Alternatively, select the check box next to Log source and click Export List to export all records that are displayed on the current page.

> **Note:** You can export a maximum of 10,000 records. If you select more than 10,000 records, only the first 10,000 records are exported.

### 7.2 Security operations

This topic lists the following consoles that support security operations: Security Policy Management Security Operations Center (SOC)

### 7.3 Host security

This topic lists the following host security consoles: Platform Server Guard

#### 7.3.1 Container image management

t Container image management periodically scans container images based on built-in policies and user-defined policies to show the latest verification status.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Host Security** > **Container**
**Image Management**.
3. On the **Container image control** tab, view the container image list or filter container
images by **Machine name**, **Image ID /Image summary**, **Image signature verification**
**result**, **Policy type**, and **Policy source** based on your business requirements.
4. Click **Associated container** in the **Operation** column corresponding to the desired
container image to obtain container information, including **Container ID**, **Container**
**Name**, **Status**, and **Runtime**.

**References**

**Create a custom policy**

1. Click the **Custom policy** tab.
2. Click **Add policy**, configure the parameters described in the following table, and then click
**OK**.

| Parameter | Description |
|---|---|
| Policy name | Enter a name for the custom policy. |
| Policy description | Enter a description for the custom policy. |
| Policy type | Select the type of the custom policy. Valid values: Image summary matching Image name rule matching Image signature |

t

| Image summary | This parameter is available only when you set the Policy type parameter to Image summary matching. Enter an image summary. |
|---|---|
| Prefix | This parameter is available only when you set the Policy type parameter to Image name rule matching. Enter a prefix for the image name rule. |
| Suffix | This parameter is available only when you set the Policy type parameter to Image name rule matching. Enter a suffix for the image name rule. |

**Delete custom policies**

Delete a single custom policy i. Click **Delete** in the **Operation** column of the policy that you want to delete. ii. In the message that appears, click **OK**. Delete multiple custom policies i. Select the custom policies that you want to delete and click **Delete** below the list. ii. In the message that appears, click **OK**.

**Use the image signature tool**

1. Click the **Custom policy** tab.
2. Click **Download the image signature tool** to obtain the sign_tool package.
3. Sign images by using the tool.
i. Log on to the OPS1 node. t ii. Create a docker_info.json file and configure the following parameters. `{`

```json
    "KeyPath":"", // The path of the private key used for the signature. This param
eter is required.
    "Password":"", // The password used to create the private key. This parameter i
s optional.
    "PrivateKeyType": "local", // Set the value to local.
    "SignType": "local", // Set the value to local.
    "WorkerNum":"", // The number of concurrent threads for processing the signatur
```

`e.`

```json
    "SignatureOutPath":"", // The parent directory of the signature file.
```

`}` iii. Create a docker_sign.json file and configure the following parameters. `{`

```
  "nginx.tar":"", // The path of the signature package.
```

`{`

```json
    // Specify the name of the signature file. You must specify
signatureOutputPath. Otherwise, an error is reported.
    "signatureOutputPath": "busybox.sig"
    // The following parameters specify the additional information of the signature
file.
    "product": "yundun-cfw",
    "service": "yundun-icfw",
    "serverrole": "yundun-icfw/ServiceTest",
    "product_commit": "1264f603-bf00-4a76-bf22-190672af7f54",
    "cpu_type": "x86",
    "cicd_task_uuid": "http://cicd.alibaba-inc.com/system/systemTask?
task_uuid=2d88f05c-2d07-4d16-b26b-48b396a60de3"
```

`},`

```
  "centos.tar":"", // The path of the signature package.
```

`{`

```json
    // Specify the name of the signature file. You must specify
signatureOutputPath. Otherwise, an error is reported.
    "signatureOutputPath": "centos.sig"
    "product": "yundun-cfw",
    "service": "yundun-icfw",
    "serverrole": "yundun-icfw/ServiceTest",
    "product_commit": "1264f603-bf00-4a76-bf22-190672af7f54",
    "cpu_type": "x86",
    "cicd_task_uuid": "http://cicd.alibaba-inc.com/system/systemTask?
task_uuid=2d88f05c-2d07-4d16-b26b-48b396a60de3"
```

`}`

```
  .... // Batch signature is supported.
```

`}` t iv. Run the following command to sign the image:

```
./docker_sign -dockerSignConfPath=docker_sign.json dockerInfoConfPath=docker_info.json
```

> **Note:** docker_sign is the file obtained in Step 2.
> docker_info.json is the file created in Step 3.b.
> docker_sign.json is the file created in Step 3.c.

v. Obtain the signature file sig.txt.

```json
{"Sig":"Bye68ji6t********3hJW0ZRRAy1PAvz9wTlD5iSznbyNC5BC+X3GN4Fk7nm/mUosdVuxZo89Nzj6 5e5Yt3pn2sGYvS/0xOJhSyJHI4EIkBTrebqjGT/874zt/POsOAAucwvjbBVOo9eQqiwiTEvOnfeA1R1Yz+eZH L+BUQSBqWn4ZSgxiGUDefXQqPq6eDqDgB6jtj8yJUQkF8wqdck2jWbvlLViL4gZo09Kod5wzqED+1ozvHltlH HycE66ICYEHgh9SjpqwLKPEEsqZTFRMVpwWyJUk3kgs8o8/bqn5nFx9/qCyOrIS3bqtUvhNWLuTGbpDMw==", ersion":"1","Annotations":{"cicd_task_uuid":"http://cicd.alibabainc.com/system/systemTask?task_uuid=2d88f05c-2d07-4d16-b26b- 48b396a60de3","cpu_type":"x86","product":"yundun-cfw","product_commit":"1264f603-bf 00-4a76-bf22-190672af7f54","serverrole":"yundunicfw/ServiceTest","service":"yundun-icfw"}}
```

4. Verify the signature.
Method 1: Start the Docker container a. Replace the string with an environment variable.

```
sig=`cat sig.txt`
```

b. Check whether the environment variable is configured.

```
echo $sig
```

c. Start the container and set the environment variable for the container.

```bash
docker run -d -e apsaraImageSignature=$sig 65ad0d468eb1 ls
```

Method 2: Start a Kubernetes pod t a. Set the env parameters in the spec section of the corresponding container.

```
kind: Deployment apiVersion: apps/v1 metadata:
  name: local-sign-dp
  namespace: default
  annotations:
    kubernetes.io/description: "test local-sign"
spec:
  replicas: 1
  selector:
    matchLabels:
      app: local-sign-pod
  template:
    metadata:
      labels:
        app: local-sign-pod
    spec:
      containers:
        - name: local-sign-containerd
          image: reg.docker.alibaba-inc.com/apsara_stack_system/aliyun-alios7u2-u
nion:1.3
          imagePullPolicy: IfNotPresent
          command:
            - /sbin/init
          env: # Specify the environment variable for the signature of the image.
            - name: apsaraImageSignature # This is a fixed value.
              value:
'{"Sig":"Bye68ji6t********3hJW0ZRRAy1PAvz9wTlD5iSznbyNC5BC+X3GN4Fk7nm/mUosdVuxZo89N 6aw5e5Yt3pn2sGYvS/0xOJhSyJHI4EIkBTrebqjGT/874zt/POsOAAucwvjbBVOo9eQqiwiTEvOnfeA1R1Y eZHQdL+BUQSBqWn4ZSgxiGUDefXQqPq6eDqDgB6jtj8yJUQkF8wqdck2jWbvlLViL4gZo09Kod5wzqED+1o HltlHyTHycE66ICYEHgh9SjpqwLKPEEsqZTFRMVpwWyJUk3kgs8o8/bqn5nFx9/qCyOrIS3bqtUvhNWLuTG DMw==","Version":"1","Annotations":{"cicd_task_uuid":"http://cicd.alibaba-inc.com /system/systemTask?task_uuid=2d88f05c-2d07-4d16-b26b- 48b396a60de3","cpu_type":"x86","product":"yundun-cfw","product_commit":"1264f603bf00-4a76-bf22-190672af7f54","serverrole":"yundunicfw/ServiceTest","service":"yundun-icfw"}}' #The value is obtained in Step 3.e.
```

b. Submit the YAML file of the workload to the Kubernetes cluster.

```bash
kubectl apply -f cosign_deployment.yaml
```

### 7.4 Network security

This topic lists the following network security consoles: Web Application Firewall Vulnerability Scanning Network Detection and Response t

#### 7.4.1 Network Security Management Center

##### 7.4.1.1 East-west security management

###### 7.4.1.1.1 Policy center

###### 7.4.1.1.1.1 Policy content management

You can view and manage the CIDR block whitelist, virtual private cloud (VPC) whitelist, and Server Load Balancer (SLB) whitelist on the Policy Content Management page.

**Background information**

The CIDR block whitelist is used to manage access to virtual IP addresses (VIPs) of classic networks by using AccessKey pairs of Alibaba Cloud accounts. Only users that use CIDR blocks in the whitelist can access VIPs of classic networks and call API operations by using Alibaba Cloud accounts. The VPC whitelist is used to manage access to AnyTunnel VIPs. Only VPCs in the whitelist can access specific AnyTunnel VIPs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Network Security** >
**Network Security Management Center**.
3. In the left-side navigation pane, choose **Security Management** > **Policy Center** >
**Policy Content Management**.
4. On the **CIDR Block Whitelist** tab, perform the following operations:
Add a CIDR block whitelist: click **Add a Whitelist of CIDR Block**, configure the parameters, and then click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| CIDR Block | Enter a CIDR block that you want to add to the whitelist. |
| CIDR Block Type | The type of the CIDR block. Only ipv4 is supported. |

t View the CIDR block whitelist: click **Advanced Filter** and filter CIDR blocks by **CIDR**
**Block** and **IP Address**.
Delete the CIDR block whitelist: Find the CIDR block that you want to delete and click
**Delete** in the **Operation** column. In the message that appears, click **OK**.

> **Note:** You can delete only custom CIDR blocks.

5. On the **VPC Whitelist** tab, perform the following operations:
Add a VPC whitelist: click **Add VPC Whitelist**, configure the parameters, and then click
**OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| VPC ID | Enter the ID of the VPC that you want to add to the VPC whitelist. |
| VPC Name | Enter the name of the VPC that you want to add to the VPC whitelist. |
| CIDR Block | Enter CIDR blocks of the VPC that you want to add to the whitelist. Separate multiple CIDR blocks with commas (,). |
| Product | Enter the product to which the VPC belongs. |

t

| Account Name | Enter the ID of the account to which the VPC belongs. |
|---|---|
| Access Components | Select components that can be accessed by the VPC. You can specify multiple components. pop-inner asapi-inner sls-inner docker-registry |
| Region | Select the region where the VPC whitelist takes effect. |

View the VPC whitelist: Click **Advanced Filter** and filter VPCs by **VPC Name**, **VPC ID**,
**Tunnel ID**, **IP Address**, **VPC Account**, **VPC-Owned Products**, and **Access**
**Components**.
t
6. On the **SLB Backend Mount Range Whitelist** tab, perform the following operations:
View the scope of backend servers that can be attached to the SLB instance on the tenant side. Manage the scope of backend servers that can be attached to the SLB instance on the tenant side: Find the policy that you want to manage and click **Edit** in the **Operation** column. In the dialog box that appears, modify the policy content, and click **OK**.

> **Important:** This operation is risky. Check with the on-site security manager before modify the policy.

The format of the policy attribute is {"$AliUid":["cidr1", "cidr2"]}.

> By default, you can attach only resources that belong to the tenant, such as Elastic Compute Service (ECS) resources. After this, you can attach user resources such as offline data centers and server NC.
> You cannot add the internal address of the cloud platform or CIDR blocks such as 0.0.0.0 or X.0.0.0/8 to the whitelist.

t

###### 7.4.1.1.1.2 Platform VIP security protection

> Platform VIP security protection includes security protection policies for classic network VIPs and AnyTunnel VIPs. This feature is used to limit the access scope of classic network VIPs and AnyTunnel VIPs to avoid security risks caused by excessive open access.

**Background information**

Classic network VIP protection: By using the ACL capability of SLB, classic network VIPs can only be accessed by the base classic network. AnyTunnel VIP protection: For AnyTunnel VIPs provided by the platform, you can configure a VPC whitelist by using the ACL capability of SLB to allow access only from trusted VPCs.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Network Security** >
**Network Security Management Center**.
3. In the left-side navigation pane, choose **East-west Security Management** > **Policy**
**Center** > **VIP Security**.
4. On the **Classic network VIP** tab, perform the operations described in the following table.

| Operation | Description |
|---|---|
| Modify the setting of Classic network VIP control policy status | Click Edit to modify the setting of Classic network VIP control policy status, and then click Save. Valid values of Classic network VIP control policy status: Enable: automatically issues the access control policy to new classic network VIPs. If you set this parameter to Enable, the policy takes effect only for the CIDR blocks in the whitelist. Close: does not issue the access control policy to new classic network VIPs. This setting may incur security risks. Observation mode: checks the sources of requests to all VIPs and blocks abnormal requests. If the system blocks a normal request from the cloud platform network, the system automatically disables the observation mode and sets the VIP status to Disabled. |

t

| View the whitelist policy of a classic network VIP | i. Click Advanced Filter to obtain the whitelist policy information of the classic network VIP by LB ID, VIP IP, VIP ownership, and Status. Note In the Status column, Enabled indicates that the network segment whitelist policy has been issued to the VIP and only networks in the whitelist can access the classic network VIP. Disabled indicates that the network segment whitelist policy has not been issued to the VIP and you cannot restrict the sources of VIP requests. VIP ownership indicates the product, service, and service role that the VPC belongs to, or the Apsara Stack tenant account that the VPC belongs. ii. Click Segment whitelist in the Policy content column of the desired classic network VIP. You are redirected to the CIDR Block Whitelist tab on the Policy Content Management page. |
|---|---|
| Enable the whitelist policy for classic network VIPs | Note If Status of the whitelist policy for a classic network VIP is Disabled and the content in the Description column is not The current VIP has been bound to another ACL policy, and the whitelist policy cannot be issued, you can enable the whitelist policy for the classic network VIP. Enable the whitelist policy for a single classic network VIP: Click Enable in the Operation column of the desired classic network VIP. In the message that appears, confirm the information and click OK. Enable the whitelist policy for multiple classic network VIPs: Select the desired classic network VIPs and click Enable below the list. |

t

| Disable the whitelist policy for classic network VIPs. | Note If Status of the whitelist policy for a classic network VIP is Enabled, you can disable the whitelist policy for the classic network VIP. After you disable the whitelist policy, the classic network VIP does not have security control policies. This poses security risks. Disable the whitelist policy for a single classic network VIP: Click Disable in the Operation column of the desired classic network VIP. In the message that appears, confirm the information and click OK. Disable the whitelist policy for multiple classic network VIPs: Select the desired classic network VIPs and click Disable below the list. |
|---|---|
| View the logs of classic network VIPs. | i. Click View Logs in the Operation column of the desired classic network VIP. ii. Obtain the log information, including Instance ID, Lvs machine IP, Packet loss, Associate VIP, VIP Port, Associate a VPC, and Request time. |
| Disable all existing VIP control policies | Important If you disable all existing VIP control policies, access control policies that have been issued to all VIPs are disabled. This imposes security risks. If you want to re-enable platform VIP security protection after you disable all existing VIP control policies, you must enable it for the LBs one by one. We recommend that you perform this operation with caution. i. Click All existing VIP policies are disabled. ii. In the message that appears, click OK. |

5. On the **AnyTunnel VIP** tab, perform the operations described in the following table.
t

| Operation | Description |
|---|---|
| Modify the setting of AnyTunnel VIP control policy status | Click Edit to modify the setting of AnyTunnel VIP control policy status and click Save. Valid values of AnyTunnel VIP control policy status: Enable: automatically issues the access control policy to new AnyTunnel VIPs. If you set this parameter to Enable, the policy takes effect only for the CIDR blocks in the whitelist. Close: does not issue the access control policy to new AnyTunnel VIPs. This setting may incur security risks. Observation mode: checks the sources of requests to all VIPs and blocks abnormal requests. If the system blocks a normal request from the cloud platform network unexpectedly, the system automatically disables the observation mode and sets the VIP status to Disabled. |
| View the whitelist policy information of AnyTunnel VIPs | Note If an AnyTunnel VIP is enabled, the VIP can be accessed from VPCs and Tiangong in the whitelist. If the AnyTunnel VIP is disabled, the VIP can be accessed only from Tiangong. If a classToAnyTunnel VIP is enabled, the VIP can be accessed from VPCs and Tiangong in the whitelist. If the classToAnyTunnel VIP is disabled, the VIP can be accessed from all VPCs without a whitelist policy. i. Click VPC whitelist in the Policy content column of the desired AnyTunnel VIP. ii. On the VPC Whitelist tab of the Policy Content Management page, obtain the VPC whitelist information. |
| Enable the whitelist policy for AnyTunnel VIPs | Note If Status of the whitelist policy for an AnyTunnel VIP is Disabled, you can enable the whitelist policy for the AnyTunnel VIP. The Enable action allows VPCs in the VPC whitelist to access this AnyTunnel VIP. Enable the whitelist policy for a single AnyTunnel VIP: Click Enable in the Operation column of the desired AnyTunnel VIP. In the message that appears, confirm the information and click OK. Enable the whitelist policy for multiple AnyTunnel VIPs: Select the desired AnyTunnel VIPs and click Enable below the list. |

t

| Disable the whitelist policy for AnyTunnel VIPs | Note If Status of the whitelist policy for an AnyTunnel VIP is Enabled, you can disable the whitelist policy for the AnyTunnel VIP. You cannot disable the whitelist policy for AnyTunnel VIPs of ASAPI and POP. After you disable the whitelist policy for an AnyTunnel VIP, the AnyTunnel VIP does not have security control policies. This poses security risks. Disable the whitelist policy for a single AnyTunnel VIP: Click Disable in the Operation column of the desired AnyTunnel VIP. In the message that appears, confirm the information and click OK. Disable the whitelist policy for multiple AnyTunnel VIPs: Select the desired AnyTunnel VIPs and click Disable below the list. |
|---|---|
| View the access control logs of AnyTunnel VIPs | i. Click View Logs in the Operation column of the desired AnyTunnel VIP control policy. ii. Obtain the log information, including Instance ID, Lvs machine IP, Packet loss, Associate VIP, VIP Port, Associate a VPC, and Request time. |

###### 7.4.1.1.2 DNS rules

This feature is used to manage the forwarding range of common DNS services outside the cloud platform, and to protect and limit the address range of the cloud platform that can be resolved from reasonable sources. For example, you can configure default DNS forwarding rules for ECS instances and platform O&M to prevent security risks.

**Create a rule**

1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Network Security** >
**Network Security Management Center**.
3. In the left-side navigation pane, choose **East-West Security Management** > **DNS Rules**.
4. On the DNS forwarding rules page, click **Edit** to modify the status of the DNS forwarding
rule. After the modification, click **Save**.
**Enable**: enables the DNS forwarding rule.
**Disable**: disables the DNS forwarding rule. If you disable the DNS forwarding rule, the
following operations are not supported.
**Observation Mode**: After you enable the observation mode, the DNS forwarding rule
does not take effect. The system only records forwarding failures of the current rule.
5. Click **Add rules**. In the dialog box that appears, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|

t

| SOURCE Type | The source type of the DNS forwarding rule. Classic Network VPC |
|---|---|
| CIDR Block | The CIDR block of the DNS forwarding rule. |
| Domain Name Range | The domain name range of the DNS forwarding rule. Global All O & M standard scope Tenant standard scope NTP server |
| VPC Name | This parameter takes effect only when you set SOURCE Type to VPC. The name of the VPC. |
| VPC ID | This parameter takes effect only when you set SOURCE Type to VPC. The ID of the VPC. |
| Product | This parameter takes effect only when you set SOURCE Type to VPC. The name of the product. |
| Account Name | This parameter takes effect only when you set SOURCE Type to VPC. The aliUid of the user. |

t
6. Click **Advanced Filter** to filter forwarding rules by **Domain name range**, **Network**
**segment**, **IP address**, **VPC name**, and **VPC ID**.

**What to do next**

**Delete a rule**

> **Note:** The default rules cannot be deleted.

Delete a single rule: Click **Delete** in the **Operation** column of the desired rule. In the dialog box that appears, click **OK**. Batch delete: Select multiple rules and click **Delete** below the list.

**View the logs**

1. Click **View Logs** in the **Operation** column of the desired rule.
2. Obtain the log information, including **Whether to hit the ACL policy** , **Parsing result**,
**Client IP**, **Access time**, and**Access domain name**.
t

###### 7.4.1.1.3 Device network access management

This topic describes how to manage device network access to Apsara Stack.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Network Security** >
**Network Security Management Center**.
3. In the left-side navigation pane, choose **East-west Security Management** > **Device**
**Network Access Management**.
4. On the Device Network Access Management page, you can enable or disable **Illegal**
**equipment check**.

> **Note:** By default, the **Illegal equipment check** feature is enabled. If you want to disable this feature to perform specific operations, contact the security manager. Enable this feature again after the operations are completed. After you disable the illegal equipment check feature, the following operations are not supported:

5. On the **Switch port mapping device information** tab, view the switch port mapping
devices. Click **Advanced Filter** to filter port mapping devices by **Switch name**, **Port**
**Name**, **Port status**, and **Inspection results**.
6. If the **Inspection results** of the switch port mapping device is **Warning** and you want to
trust the device, click **Add Trust** in the **Operation** column. In the dialog box that appears, set the following parameters and click **OK**.

| Parameter | Description |
|---|---|
| Select MAC address | The MAC address that you want to trust. |
| Trust duration | The trust duration. The minimum value is one day. If you select Permanent, the address is permanently trusted. |
| White reason | The reason why the device is trusted. |

t
7. On the **Add a trusted MAC address** tab, click **Add a whitelist**. In the dialog box that
appears, configure the parameters as described in Step 6 and click **OK**.

### 7.5 Account security

#### 7.5.1 Linux account management

##### 7.5.1.1 Password management for root users

On the root Password Management page, you can manage passwords for the root users of all physical servers and Kernel-based Virtual Machines (KVMs) in the Apsara Stack environment, including updating and rotating passwords.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, click **Password Management for Root**.
4. On the **Password management** tab, perform the following operations to view information
about all physical servers and KVMs in the Apsara Stack environment: Query the information about a physical server or KVM. t a. You can filter physical servers or KVMs by **Product**, **Server Name**, **IP**, and **Password**
**status**. The following figure provides an example on the information about physical
servers and KVMs that you can view on the Password management tab. When **Password status** of a physical server or KVM is **Disengaging from the**
**Nano Tube** or **Mismatch**, the **Rotation Period** and **Next Rotation Time**
parameters do not take effect. b. If you click the icon next to a password in the **Password** column, the password is displayed in plaintext for 10 seconds. Update a password To update the password of a physical server or KVM, perform the following operations: Find the desired physical server or KVM and click **Update password** in the **Operation** column. In the Update password dialog box, specify the new password that you want to use for the physical server or KVM in the Password field, enter the password again in the Confirm Password field, and then click **OK**. To update the passwords of multiple physical servers or KVMs at a time, perform the following operations: Select the desired physical servers or KVMs and click **Batch**
**update** in the lower part of the page. In the Update password dialog box, specify the
new password that you want to use for the physical servers or KVMs in the Password field, enter the password again in the Confirm Password field, and then click **OK**.

> **Note:** You can update the password of a physical server or KVM only when **Password status** is **Match** for the physical server or KVM.
> Each password must be 8 to 30 characters in length and must contain digits, lowercase letters, uppercase letters, and special characters. Single quotation marks, double quotation marks, and backticks are not allowed in passwords.
> Make sure that the passwords you enter in the Password and Confirm Password fields are the same.

Configure a password expiration period To configure a password expiration period for a physical server or KVM, perform the following operations: Find the desired physical server or KVM and click **Configuration** in the **Operation** column. In the Configuration Items dialog box, specify a password expiration period and click **OK**. t To configure a password expiration period for multiple physical servers or KVMs at a time, perform the following operations: Select the desired physical servers or KVMs and click **Set Passwords** in the lower part of the page. In the Configuration Items dialog box, specify a password expiration period and click **OK**.

> **Note:** You can configure a password expiration period for a physical server or KVM only when **NORMAL** displays in the Server Name column and **Password** **status** is **Match** for the physical server or KVM.
> The valid password expiration period ranges from 1 to 180 days.

Revise a password To revise the password of a physical server or KVM, perform the following operations: Find the desired physical server or KVM and click **Correct password** in the **Operation** column. In the dialog box that appears, enter the correct password and click **OK**. To revise the passwords of multiple physical servers or KVMs at a time, perform the following operations: Select the desired physical servers or KVMs and click **Batch**
**Revise** in the lower part of the page. In the dialog box that appears, enter the correct
password and click **OK**.

> **Note:** You cannot change the password of a physical server or KVM when **Password** **status** is **Disengaging from the Nano tube** for the physical server or KVM.

5. On the **Change history** tab, view the password update records of all physical servers and
KVMs in the Apsara Stack environment. You can also obtain the password update record of a specific physical server or KVM by specifying **Product**, **Server Name**, **IP**, and **Change**
**Status**.
6. On the **Configuration** tab, view and modify the password configuration policies of physical
servers and KVMs. Click **Submit** to update the configuration policies. The following table describes the parameters that you can configure.

| Parameter | Description |
|---|---|

t

| Password tube switch | This parameter specifies whether to enable password policy configuration. If you turn on this switch, you can modify the password configuration policies for physical servers or KVMs, such as password updates and automatic rotation. If you turn off this switch, you cannot modify the password configuration policies for physical servers or KVMs, such as password updates and automatic rotation. |
|---|---|
| Initial Password | This parameter is available only when Password tube switch is turned on. This parameter specifies the password assigned to a physical server or KVM that is deployed in the Apsara Stack environment. |
| Retry Times | This parameter is available only when Password tube switch is turned on. This parameter specifies the number of retries after a password fails to be updated. |
| Password rotary switch | This parameter is available only when Password tube switch is turned on. This parameter specifies whether to enable automatic password rotation. If you turn on this switch, automatic password rotation is enabled. If you turn off this switch, automatic password rotation is disabled. |
| Default Rotation Period | This parameter is available only when both Password tube switch and Password rotary switch are turned on. You need to configure a period for automatic password rotation and the time for next automatic password rotation. |
| Password Length | This parameter is available only when both Password tube switch and Password rotary switch are turned on. This parameter specifies the length of an automatically rotated password. The password must be 8 to 30 characters in length. |

t

##### 7.5.1.2 SSH key management

This feature allows you to view and manage SSH keys on physical machines, KVMs, and containers in Apsara Stack. This feature allows you to view full keys, query key validation records and usage records, and manage temporary keys.

**Prerequisites**

You have obtained the permissions to manage SSH keys on the hosts. The Tianji-sshtunnel service is in desired state.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, click **SSH Key Management**.
4. On the **Full key** tab, you can filter key fingerprints by **Public key status**, **Private key**
**status**, and **Key fingerprint**. You can search for a key fingerprint by fuzzy search.
t In the **Effective machine** column that corresponds to a key fingerprint, click Public key or Private key. In the panel that appears, you can view the **Public key** and **Private key** information. The public key information includes the **Public key** and **Creation Time**. The Private key information includes **Machine name**, **User**, **Key path**, **Container ID**,
**Status**, and **Creation time**.
Click **Usage record** in the **Operation** column that corresponds to a key fingerprint. In the panel that appears, view the **Source**, **Destination**, and **Usage time** of the key.
5. On the **Temporary Key** tab, create a temporary channel to obtain temporary keys.
Click **Create a temporary channel** . In the dialog box that appears, configure the following parameters and click **Create**.

| Parameter | Description |
|---|---|
| Channel name | The name of the temporary channel. |
| Validity period | Select Start Date and End Date for the temporary channel. |
| Machine definition mode | Select the delineation method of the target machine. Valid values: Product dimension Physical machine dimension Full machines (including physical machines managed by Tianji, dockerVM, and KVM) |
| Product | This field takes effect only when you set Machine definition mode to Product dimension. Fuzzy match is supported. |
| SR | This field takes effect only when you set Machine definition mode to Product dimension. You can select multiple server roles from the drop-down list. |
| Machine name | This field takes effect only when you set Machine Definition mode to Physical machine dimension. The name of the server. Fuzzy match is supported. |

t You can also perform the following related operations:

| Operation | Description |
|---|---|
| View temporary channels | a. Click Advanced Filter to obtain the information of a channel by Channel name, Key fingerprint, Public key status, and Private key status. b. Click the number in the Public key effective machine/expected machine column corresponding to a temporary channel. In the panel that appears, you can view the information of machines whose public keys are effective, including Machine name, Container ID, User, Key path, and Status. |
| Clone a temporary channel | a. Click Clone in the Operation column corresponding to a temporary channel. In the dialog box that appears, you can view a temporary channel with the same configurations. b. Modify the parameters based on your requirements and clickC reate. |
| View execution records | a. Click Execution record in the Operation column corresponding to a temporary channel. b. On the Task Execution Records page, you can obtain the execution record details. |

t

| Modify the validity period | a. Click Modify validity period in the Operation column corresponding to a temporary channel. b. In the Modify validity period dialog box, specify a new validity period for the temporary channel and click OK. The maximum validity period is 90 days. Note When the validity period of a temporary channel expires, you cannot modify the validity period. |
|---|---|

##### 7.5.1.3 System user management

You can manage users, passwords, and SSH keys of Linux operating system on physical servers and containers, including granting, canceling, disabling, enabling, and creating temporary system users.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, choose **System User Management**.
4. On the **Full Users** tab, click **Advanced Filter** to filter system users by **System User**,
**Machine**, **Product**, **Ciphertext password**, **Key fingerprint**, **Key status**, **User trust**
**status**, **Password trust status**, **Key trust status**, **service**, and **sr**.

> **Note:** In the **User status** and **Password status** columns, you can filter users who are **disabled** or **enabled**.
> Click the
> icon in the **Ciphertext password** column. The password of the
> system user is displayed for 10 seconds in plaintext.

t
5. You can also perform the following operations on the Full Users tab:
View the information about secret-free public keys of a system user a. Find the system user that you want to view and click Number of public keys in the
**Secret-free public key** column.
b. In the panel that appears, view the information about the secret-free public keys, including **Public key**, **Key fingerprint**, **Key trust status**, **Key status**, and **Get**
**Time**.
c. In the **Operation** column, click **Disable key** if **Key status** is **Enabled**. In the message that appears, click **OK** to disable the key. In the Operation column, click **Enable key** if
**Key status** is **Disabled**. In the message that appears, click **OK** to enable the key.

> **Note:** Untrusted keys are automatically removed on a regular basis.

d. In the **Operation** column, click **Manage key trust relationships**. In the dialog box that appears, you can set which sr is allowed to trust the key, or cancel the sr that no longer trusts the key. Then, click **OK**.

> **Note:** If **Key trust status** is set to **Platform Trust**, you cannot manage key trust relationships.

View the server role information for the deployment a. Find the system user that you want to view and click **View deployment SR** in the
**Operation** column.
t b. In the panel that appears, view the server role information for the deployment, including the **product**, **service**, **sr**, **User trust status**, and **Password trust status**. c. In the Operation column, click **Trust User** or **Trust Password** to add a user to the trust status. Click **Untrust User** or **Untrust Password** to cancel the trust.

> **Note:** If **User trust status** or **Password trust status** is set to **Platform Trust**, you cannot cancel the trust.
> When performing the trust password operation, the Apsara Uni-manager Operations Console will scan the system users on the machine and verify whether the password meets your expectation, so as to prevent potential risks such as password tampering caused by other reasons.

Disable or enable a system user a. In the **Operation** column that corresponds to a system user, click **Disable user** or
**Enable user**.

> **Note:** If the **User status** is **Enabled**, the **Disable user** operation is supported. If the **User status** is **Disabled**, the **Enable user** operation is supported.

b. In the message that appears, check the information about the **system user**, **physical**
**server**, and **container**, and click **OK**.
Disable or enable the password of a system user a. In the **Operation** column that corresponds to a system user, click **Disable password** or **Enable password**.

> **Note:** The **Disable password** operation is supported if **Password status** is **Enabled**. The **Enable password** operation is supported if **Password status** is **Disabled**.

b. In the message that appears, check the information of the **system user**, and then click
**OK**.
6. On the **Temporary User** tab, you can create temporary users.
Click **Create a temporary user** . In the dialog box that appears, configure parameters and then click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|

t

| Username | Enter a name for the temporary user. |
|---|---|
| User type | Select a user type. Common users sudo user |
| Enable Password | Select whether to enable the password. Yes No |
| Enter Password | This field takes effect only when you set Enable Password to Yes. The password of the temporary user. The password must be 12 to 30 characters in length and must contain at least three types of digits, lowercase letters, uppercase letters, and special characters. |
| Confirm Password | This field takes effect only when you set Enable Password to Yes. Enter the password of the temporary user again. Make sure that the two passwords are the same. |
| Whether to enable SSH keys | Select whether to enable SSH keys. Yes No |
| Description | Enter a description for the temporary user. |
| Validity period | Select a Start Date and End Date for the temporary user. |
| Machine definition mode | Select the delineation method of the machine. Valid values: Product dimension Physical machine dimension Full machines (including physical machines managed by Tianji, dockerVM, and KVM) |
| Product | This field takes effect only when you set Machine definition mode to Product dimension. Fuzzy match is supported. |
| SR | This field takes effect only when you set Machine definition mode to Product dimension. You can select multiple server roles from the drop-down list. |

t

| Machine name | This field takes effect only when you set Machine definition mode to Physical machine dimension. The name of the server. Fuzzy match is supported. |
|---|---|

You can also perform the following related operations:

| Operation | Description |
|---|---|
| View temporary user information | a. Enter a keyword in the Username field to obtain the user information. b. Click the number in the Effective machine/expected machine column that corresponds to the target temporary user. In the panel that appears, you can view the list of effective machines, including Machine name, Container ID, User home directory, and Creation time. |

t

| Clone a temporary user | a. Click Clone in the Operation column that corresponds to the temporary user. In the dialog box that appears, you can view a temporary user with the same configurations. b. Modify the parameters as required and click OK. |
|---|---|
| View the details of a task | a. Find the temporary user that you want to view and clickE xecution details in the Operation column. b. On the Task Execution Records page, you can obtain the execution record details. |
| Configure the validity period of a temporary user | a. Click Set Validity Period in the Operation column that corresponds to a temporary user. b. In the dialog box that appears, modify the validity period of the temporary user and then click OK. The validity period can be up to 90 days. Note When the validity period of a temporary user expires, you cannot modify the validity period. |

##### 7.5.1.4 Linux account management task

###### 7.5.1.4.1 Task template management

A host task template specifies an automatic rotation period for a specified key. The task automatically rotates the key on a regular basis to improve the security of sensitive information such as keys. You can also create a custom rotation task template in advance and trigger the task when key rotation is required. The following types of tasks are supported: global password-free channel removal across regions, SSH key rotation, OPS emergency O&M channel creation, temporary channel creation, and temporary user creation.

**Prerequisites**

You have obtained the permissions to manage host task templates. The Tianji-sshtunnel service has reached the desired state.

**Create a task template**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, choose **Linux Account Management Task** > **Task**
**Template Management**.
4. On the page that appears, click **Create a task template**, configure the parameters
described in the following table, and then click **Next Step**.

| Parameter | Description |
|---|---|

t

| Task Template name | The name of the custom task template. |
|---|---|
| Task type | The type of the rotation task. Only SSH key rotation is supported. |
| Trigger mode | The trigger mode of the rotation task. You can select Manual trigger or Automatic trigger. |
| Trigger cycle | This field is displayed only when you set Trigger mode to Automatic trigger. Specify the cycle and next execution time of the automatic rotation task. Note Valid values: 7 to 365. Unit: days. |
| Cross-Region | Specifies whether to support cross-region rotation tasks. |
| Select SSH key | Enter the SSH key. |

5. In the **Configure task phase** section, select a task phase.

> **Note:** If you set **Trigger mode** to **Manual trigger**, you can specify whether to select the **Grayscale remove the original private key** phase.

t
6. In the **Task template preview** section, check the template information and click **Create**.

**Related operations**

**View a rotation task template**

1. On the Task Template Management page, enter a name in the **Task Template name** field
to query the rotation task. You can view the following information of the rotation task: **Task**
**Template name**, **Task type**, **Task phase**, **Creation time**, **Trigger mode**, and **Next**
**execution time**.
2. To view the details of the rotation task template, click **Details** in the **Operation** column
that corresponds to the rotation task template.

**Modify a rotation task template**

1. On the Task Template Management page, find the task template that you want to modify
and click **Edit** in the **Operation** column.
2. Modify the parameters in the **Basic configuration** section and click **Next Step**.
3. Modify the parameters in the **Configure task phase** section. In the **Task template**
**preview** section, check the template information and click **Update**.

> **Note:** You cannot modify preset rotation task templates.

**Execute a rotation task**

1. On the Task Template Management page, find the task template and click **Execute** in the
**Operation** column.
2. In the message that appears, click **OK**.

**View the execution record of a rotation task**

1. On the Task Template Management page, find the task template and click **Execution**
**record** in the **Operation** column.
2. On the **Task Execution Records** page, you can view all the execution records of the
rotation task template.

###### 7.5.1.4.2 Task execution records

You can view the records of all historical rotation tasks, including global password-free channel removal tasks, OPS emergency O&M channel creation tasks, temporary channel creation tasks, and rotation tasks for updating the SSH keys. You can view all historical key pairs, update operations, and points in time of the updates.

**Prerequisites**

You have obtained the permission to operate the task execution records of the host. t The Tianji-sshtunnel service has reached the desired state.

**Background information**

You may need to manage SSH key pairs across multiple regions. In this case, a rotation task have subtasks. The name of a subtask is suffixed with the region where the SSH key pair is used. You can distinguish subtasks by the suffix. You can also use the subtask name to identify the parent rotation task to which the subtask belongs. A subtask is always synchronized with its parent task in status. The subtask status cannot be manually modified. All execution stages of a parent task are displayed after the task is created. The execution stages of a subtask are fully displayed only after all stages of the parent task are complete. When the parent task is running, you can view only the completed stages and the ongoing stage of the subtask.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, choose **Linux Account Management Task** > **Task**
**Execution Records**.
4. Click **Advanced Filter** to filter execution records by **Task ID**, **Task template ID**, **Task**
**template name**, and **Current execution status**.
5. Find the task execution record that you want to view and click **Details** in the **Operation**
column. In the panel that appears, you can view the details of the task execution record.

**Related operations**

**Pause a rotation task**

> **Note:** You can pause a rotation task when the **Task execution status** is **Running**.

1. Find the rotation task that you want to pause and click **Pause** in the **Operation** column.
2. In the message that appears, click **OK**.

**Continue a rotation task**

> **Note:** If **Task execution status** is **Paused** for a rotation task, you can continue to rotate the task.

1. In the **Operation** column that corresponds to the rotation task, click **Continue**.
2. In the message that appears, click **OK**.

**Roll back a rotation task**

> **Note:** When the task type is **SSH key rotation** (including cross-region tasks) or **Global** **password-free removal** (including cross-region tasks), you can roll back the rotation task.

t
1. Click **Rollback** in the **Operation** column that corresponds to the rotation task.
2. In the dialog box that appears, select a **Rollback type** and click **OK**. A new task is
generated to roll back the key to the target key pair.

> **Note:** You can set the **Rollback type** parameter to **This rollback** or **Initialize** **Rollback**.
> After the rollback, the cloud will have more global access root account keys, which may cause the cloud platform to be in an insecure state. Recycle the root account key timely.

**Perform canary configurations**

If the task type is **SSH key rotation** and the **Grayscale remove the original private**
**key** phase is selected, you can configure canary tasks. For more information, see Task
template management.
1. In the **Operation** column that corresponds to the rotation task, click **Grayscale**
**Configuration**.
2. In the dialog box that appears, configure the following parameters. Then, click **OK**.

> **Important:** The parameters take effect in sequence from top to bottom.
> The current parameters are configured only when the number of machines that have been phased out is the same as the total number.

t

**Obtain an execution instance**

1. Click **Execute an instance** in the **Operation** column that corresponds to the rotation task.
You can also click the ID in the **Task ID** column that corresponds to the rotation task.
2. On the **Task execution instance** page, view the information about the instance based on
the **Target machine**, **Task phase**, and **Current execution status**.
3. Find the instance that you want to view and click **Details** in the **Operation** column. In the
panel that appears, you can view the details of the task execution instance.
4. If **Instance execution status** is **Failed** or **Timeout Failed**, you can perform the following
operations: Click **Retry** in the **Operation** column that corresponds to an instance or select multiple instances and click **Batch retry**. In the message that appears, click **OK** to retry the selected instances. Click **Skip** in the **Operation** column that corresponds to an instance or select multiple instances and click **Batch skip**. In the message that appears, click **OK** to skip the selected instances. t

#### 7.5.2 Account management for cloud services

**services**

##### 7.5.2.1 Account ACL control

A platform account has a wide range of permissions. You can use the account access control list (ACL) control feature to limit the permissions of a platform account to avoid security risks. This way, the account can be used only within the network on the platform.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Cloud**
**Product Account Management**.
3. In the left-side navigation pane, click **Account ACL**.
4. In the upper part of the page, click **Edit** to change the status of the account ACL control
feature.
**Enable**: If you select the value, the system attaches an access control policy to the
AccessKey pair of a new platform account to allow access from CIDR blocks over the classic network. The AccessKey pair can be used only within the range specified by the network whitelist. The access control policy is not attached to existing AccessKey pairs.
**Close**: If you select the value, the system does not attach an access control policy to the
AccessKey pair of a new platform account to allow access from CIDR blocks over the classic network. This incurs security risks.
**Observation Mode**: If you select the value, the system checks sources of the requests
initiated by using the AccessKey pairs of all platform accounts, records the logs of abnormal sources, and then allows the requests.
5. Click **Advanced Filter** and filter the list by **Account ID**, **Account name**, and **Ak** to obtain
the policy information about the desired account.
6. Click **Policy content** in the **Operation** column of the account to obtain the information
about **Network segment whitelist** and **VPC whitelist**. On the **Network segment whitelist** tab, you can filter the list by **Network segment** and **IP address**. On the **VPC whitelist** tab, click **Advanced Filter** and filter the list by **VPC name**, **VPC**
**ID**, **Tunnel ID**, **VPC-owned products**, and **Access Components** to obtain the
information about the desired virtual private cloud (VPC). t

**What to do next**

**Disable access control policies for the AccessKey pairs of**

**platform accounts**

> **Note:** You can disable the access control policy for the AccessKey pair of a platform account if the policy is in the enabled state.
> If you disable the access control policy for the AccessKey pair of a platform account, no security control policy is imposed on the AccessKey pair. The system cannot limit the AccessKey pair based on request sources. This incurs security risks.

To disable an access control policy for an account, perform the following operations: i. Find the account and click **Disable** in the **Operation** column. ii. In the message that appears, confirm the values of the **Account name** and **AK** parameters and click **OK**. To disable access control policies for multiple accounts at a time, select the accounts and click **Disable** below the list.

**Enable access control policies for the AccessKey pairs of**

**platform accounts**

> **Note:** You can enable the access control policy for the AccessKey pair of a platform account if the policy is in the disabled state.
> If you enable the access control policy for the AccessKey pair of a platform account, the AccessKey pair can be used only within the range specified by the network whitelist.

To enable an access control policy for an account, perform the following operations: i. Find the account and click **Enable** in the **Operation** column. ii. In the message that appears, confirm the values of the **Account name** and **AK** parameters and click **OK**. To enable access control policies for multiple accounts at a time, select the accounts and click **Enable** below the list.

**Obtain the logs of blocked requests**

t
1. Find the desired account and click **Intercept logs** in the **Operation** column.
2. View information about the logs of requests that are blocked by the policy. The information
includes **Call Source**, **Client observation mode**, **Authentication method**,
**Authentication AK**, **Request IP**, **VPC ID**, **Authentication result**, **Policy status**, and
**Interception time**.

**Disable existing access control policies for AccessKey pairs**

> **Important:** You can click a button to disable existing access control policies for AccessKey pairs. After the existing access control policies are disabled, the security control capability for the request sources of platform accounts becomes unavailable. This incurs security risks. If you want to enable the account ACL control feature after the existing access control policies are disabled, you must enable the feature for the AccessKey pairs one by one. Therefore, exercise caution before you click the button.

1. Click the button on the left of the Account ID drop-down list above the account list.
2. In the message that appears, click **OK**.

##### 7.5.2.2 Service boundary

###### 7.5.2.2.1 ACL

The Account ACL control page displays the whitelist policies associated with platform accounts. If you want to examine the specifics of an API control policy, simply click its ID.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security** > **Account Security** > **Cloud Product**
**Account Management**.
3. In the left-side navigation pane, choose **Service Boundary** > **Control Policies**.
4. Click **Advanced Filter** and search for desired API control policies by a combination of **API**
**control policy ID**, **uid**, **Policy type**, **Account ownership**, and **Creation time**.
5. Click the ID of the desired API control policy. On the page that appears, you can view the
details of the API control policy. t

###### 7.5.2.2.2 O&M

You can manage the O&M switch for service boundaries.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security** > **Account Security** > **Cloud Product**
**Account Management**.
3. In the left-side navigation pane, choose **Service Boundary** > **O&M**.
4. Click **Edit**, select an option from the **Service boundary O & M switch** drop-down list, and
then click **Save**.
**Enable**: enables service boundary control for all accounts, including the new platform
accounts.
**Close**: disables service boundary control for existing or new platform accounts.
**Observation mode**: authenticates requests sent from new and existing platform
accounts. The system records the failed authentication logs and allows the requests.

### 7.6 Access control

#### 7.6.1 Security policies

You can modify the account policies and password policies of the current account in the Security Policies module.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Security**
**Strategy**.
3. On the **Account Policy** tab, configure the parameters and click **Submit**. The following
table describes the parameters. t

| Parameter | Description |
|---|---|
| Timeout Period (Minutes) | Specify a logon timeout period for the current account. If the logon time exceeds the specified time period, the system prompts you that the logon timed out and you can try to log on again. Valid values: 10 to 180. |
| Multi-Terminal Logon Settings | Specify whether the current account allows simultaneous logon from multiple terminals. |
| ASO account validity period (days) | Specify the validity period of the current account. If the account is expired, the system locks this account and only the security administrator can unlock the account. Valid values: 10 to 365. |
| Account Freeze Policy (Days) | Specify the period during which the current account remains available. If the specified period elapses, the system freezes this account. Valid values: 0: indicates that the account freezing policy is disabled. 10~365 |
| Security Policy Is Valid for Preset Accounts | Specify whether the security policy is valid for preset accounts. On: If a security policy expires (for example, the account or password expires), preset accounts cannot log on to the system. We recommend that you set a long validity period. Off: If a security policy expires, preset accounts can still log on to the system. Preset accounts never expire. Default value: Off. |

t
4. Click the **Password policy** tab, configure the parameters, and click **Submit**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Minimum Password Length | Specify the minimum number of characters in the password. Valid values: 10 to 20. |
| Required Character Types in Password | Select one or more character types that must be contained in the password. Lowercase Letters Uppercase Letters Digits Special Characters |
| Logon Disabled After Password Expires | Specify whether to prohibit the current account from logging on to the system after the password expires. Yes No |
| Reminder time before password expiration (days) | Set the time to send a reminder before the password of an account expires. For example, a value of 10 indicates that the expiration reminder is sent 10 days before the password expires when the user logs on. A value of 0 indicates that no reminder is sent. Valid values: 0 to 30. |

| sara Uni-manager Operations nsole | User Guide·Security manageme |
|---|---|

t

| Password Validity (Days) | Specify the validity period for the password. If the password expires, the system sends a notification to the user. 0 indicates that the password does not expire. Valid values: 0 to 1095. |
|---|---|
| Password History Check | Specify the number of historical passwords that you cannot reuse. For example, if you set this parameter to 3, the most recent three historical passwords cannot be reused. 0 indicates that all historical passwords can be reused. Valid values: 0 to 24. |

#### 7.6.2 Logon policies

As an administrator, you can configure logon policies to manage the logon time and logon IP addresses of users.

**Background information**

The system provides a default policy. You can also configure custom logon policies based on your business requirements to control the read and write permissions of users and improve the security of the system.

**Add a policy**

1. Log on to the Apsara Uni-manager Operations Console.
t
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Logon**
**Policies**.
3. On the Logon Policy page, click **Add Policy**. In the Add Policy dialog box, configure the
parameters and click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the logon policy. |
| Policy Effective Period | The dates when the logon policy starts and stops taking effect. |
| Description | The description of the logon policy. |
| Shared Scope | The scope in which you want to share the logon policy. Set this parameter to Global Sharing. |
| Policy attributes | Whitelist Blacklist |
| The start time when the policy takes effect. | The point in time from which users are allowed for logon. The start time for logon cannot be later than the end time for logon. |
| Policy Effective end time | The point in time from which users are not allowed for logon. |
| Login address | The CIDR blocks of the logon policy. If you set Policy attributes to Whitelist, this parameter specifies the CIDR blocks that are allowed for logon. If you set Policy attributes to Blacklist, this parameter specifies the CIDR blocks that are blocked from logon. Specify CIDR blocks such as 192.168.1.0/24. Use a 32-bit mask in the CIDR block to indicate a single IP address. CIDR blocks cannot overlap each other. Separate multiple CIDR blocks with commas (,). |

t

**Related operations**

**Query a policy**

You can query the information about a logon policy by **policy name**.

**Modify a policy**

1. Find the logon policy that you want to modify and click **Modify** in the **Actions** column.
2. In the Modify policy dialog box, modify the configurations and click **OK**.

**Delete a policy**

1. Find the logon policy that you want to delete and click **Delete** in the **Actions** column.
2. In the message that appears, click **OK**.
t

> **Note:** A logon policy that is bound to a user cannot be deleted. You must unbind the policy before you delete it.

**Disable a policy**

1. Find the logon policy that you want to disable and click **Disable** in the **Actions** column.
2. In the message that appears, click **OK**.

> **Note:** After you disable a logon policy, users that are bound to the policy are not allowed for logon.
> You can disable a logon policy only when **Enable** is displayed in the **Enable** **status** column corresponding to the policy.

**Enable an anti-ransomware policy**

1. Find the logon policy that you want to enable and click **Enable** in the **Actions** column.
2. In the message that appears, click **OK**.

> **Note:** You can enable a logon policy only when **Disable** is displayed in the **Enable status** column corresponding to the policy.

#### 7.6.3 Two-factor authentication

To make user logons more secure, you can configure two-factor authentication for users.

**Background information**

The Apsara Uni-manager Operations Console supports only **multi-factor authentication**
**(MFA)**. After you enable two-factor authentication and add a key, you can use the random
verification code generated by the authentication app for logon. This ensures the security of your account.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Two-**
**factor Authentication**.
3. In the upper part of the Two-factor Authentication page, specify an authentication method.
The following authentication methods are provided:

**MFA**

t Add a key a. In the upper-right corner of the Two-factor Authentication page, click **Add Key**. In the dialog box that appears, specify a username and click **OK**. The specified user is displayed in the user list. b. Click **Add Key** in the **Actions** column. If the **The operation is successful** message occurs, a key is added to the user and **Show Key** is displayed in the **Actions** column. c. If you click **Show Key**, the key is displayed in plaintext. If you click **Hide Key**, the key is displayed in ciphertext. Delete a key a. Find the user for whom you want to delete the key and click **Delete Key** in the
**Actions** column.
b. In the message that appears, click **OK**.

**No Authentication**

If you select **No Authentication**, two-factor authentication is disabled and all two-factor authentication methods become invalid.

## 8 System settings

### 8.1 Custom settings

The feature allows you to customize the login page and platform logo.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, click **Personalized configuration**.
4. Customize the following items:
**Platform Language**: Select the languages that you want the platform to support,
whether to deploy the platform outside China, and the default language of the platform. The following languages are available: Simplified Chinese, Traditional Chinese, and English.
**Appearance and Theme**: Select **Light Color Mode** or **Dark Pattern** for the
**Appearance** parameter and configure the **Theme Color** parameter. You can click the
icon next to Custom swatches to customize the theme color.
**Page Watermark**: Specifies whether to add watermarks to pages.
**Brand Setting**: You can configure the **Browser Ico Icon**, **Platform Logo**, **Platform**
**Name**, **Login Page**, **Version Information**, and **Copyright Notice** in three languages.
5. After the settings are complete, click **Determine**.
6. In the upper-right corner of the page, click **Restore Factory Settings**. In the message
that appears, click **Restore Factory Settings**. The custom settings are restored to the factory settings and take effect after you log on to the Apsara Uni-manager Operations Console again.

**Important**

This operation is irreversible. Proceed with caution.

### 8.2 Authorization Information

> You can view authorization information of services in the Authorization Information module.

**Prerequisites**

You have the administrator permissions. For formal authorization, you must enter the authorization code to view the authorization information. You can obtain the authorization code from the authorization letter appended to the project contract or by contacting the customer business manager (CBM) of your project.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, click **Authorization Information**.
4. On the **Authorization Details** tab, view the authorization information.
In the **Basic Information** section, you can view the authorization information in the current Apsara Stack environment. The following table describes the parameters in the authorization information.

| Parameter | Description |
|---|---|
| Authorization Version | The BP number in the version. You can use this number to associate a project or contract. Fields in the BP number: TRIAL in the version indicates that the trial authorization is used. The trial authorization is valid within 90 days from the date of deployment. FORMAL in the version indicates that the formal authorization is used. The authorization information of the service comes from the signed contract. |
| Authorization Type | The current authorization type and authorization status. The following authorization types are available: Trial Authorization Formal Authorization The following authorization states are available: Not Activated About to Expire Taking Effect Expired Expired/Excess |
| Customer ID | The unique ID of the customer. |
| Instance ID | The ECS instance ID in the deployment planner of the field environment. |
| UID | The unique ID of the user. |
| Cloud Platform Version | The Apsara Stack version of the current cloud platform. |

| Customer Name | The name of the customer who purchased the Apsara Stack service. |
|---|---|
| Authorization Created At | The start time of the authorization. |

You can view the authorization information of cloud services in different regions. The following table describes the authorization details.

| Parameter | Description |
|---|---|
| Product Name | The name of the cloud service. |
| Product Specification Name | The specification of the cloud service. |
| Authorization Mode | The authorization mode of the cloud service. Authorization Mode Subscription Mode Temporary Additional Mode |
| Authorized Quantity | The quantity of the authorized cloud services. |
| Authorization Validity Period | The validity period of the authorization. |
| Actual Authorized Usage | The actual authorized quantity of the cloud services. |
| Validity Period for Software License Update and Technical Support | The validity period of the project. The default validity period of a project is 90 days after the creation. The free trial does not take up your validity period. The remaining validity period is displayed after the formal authorization is used. |

| Authorization Status | The current authorization status of a specification for a service. Activating RENEW Service Expired Specification Quota Exceeded Important If the following items appear in the Authorization Status column of a service, take note of them. RENEW Service Expired: indicates that the customer must renew the subscription as soon as possible. Otherwise, field operations services (including ticket processing) are terminated. Specification Quota Exceeded: indicates that the specifications deployed for a service have exceeded the contract quota, and the customer must scale up the quota as soon as possible. |
|---|---|

5. Click the **Authorization Specifications Details** tab to view the authorization specification
information of services across different data centers or regions. The following table describes the parameters in the authorization specification information.

| Parameter | Description |
|---|---|
| Category | The name of an authorized cloud service. |
| Dimension | The specification name of an authorized service. |
| Used | The total number of existing authorizations of a specification for a service. |

| sara Uni-manager Operation nsole | s User Guide·System setting |
|---|---|

| Issued | The maximum number of authorizations of a specification for a service. Note Move the pointer over the icon to view the available authorization quota. |
|---|---|
| Usage Update Time | The time when the authorization specifications of the service were updated. |
| Status | The current authorization status of a specification for a service. |

6. Click the **Authorization Specification Information** tab to view the statistics on the
authorized specifications of services and the information about services whose actual authorized specifications exceed the quota of authorized specifications. i. You can filter information about the authorized specifications of a specific service by setting **Authorization specification level**, **Region ID/Data Center ID**, **Product**
**Name**, and **Time Range**.
ii. In the **Authorization Specification Information** section, view the statistics on authorized specifications. The statistics include **Maximum Specification Usage Within**
**Current Period**, **Maximum Number Occurred At**, **Minimum Specification Usage**
**Within Current Period**, **Minimum Specifications Occurred At**, and **Average**
**Specification Usage Within Current Period**.
iii. Click the icon in front of a service name to view the authorization specification details of the service on the previous day within a specific time range. The information include
**Authorization specification name**, **Authorized Specification Usage**, **Maximum**
**authorization specifications**, and **Recorded At**.
iv. Click **View More**. In the dialog box that appears, you can view the authorization specification information of the service within the selected time range by date. v. In the **Authorization specification overcount** section, you can view the information about the services whose actual authorized specifications exceed the quota of authorized specifications. vi. Click the icon in front of a service name to view the authorization specification details of the service on the previous day within a specific time range. The information include
**Authorization specification name**, **Authorized Specification Usage**, **Maximum**
**authorization specifications**, and **Recorded At**.
vii. Click **View More**. In the dialog box that appears, you can view the authorization specification overcount of the service within the selected time range by date.

### 8.3 Notification management

#### 8.3.1 Channel management

You can configure channels to send notifications.

**Create a channel**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Settings**.
3. In the left-side navigation pane, choose **Notification Management** > **Channel**
**Management**.
4. Click **Create a channel** and configure the parameters. The following table describes the
parameters.

| Parameter | Description |
|---|---|
| Channel group | Specify a name for the channel group. |
| Channel name | Specify a name for the channel. |
| Channel type | Select the channel type. Valid values: DingTalk Email Webhook |
| DingTalk message push URL | This parameter is available only when you set the Channel type parameter to DingTalk. The URL that a DingTalk robot uses to push notifications. Default value: https://oapi.dingtalk.com/robot/send. |
| Robot AccessToken | This parameter is available only when you set the Channel type parameter to DingTalk. Enter the access token of the DingTalk robot. |
| Robot SecretKey | This parameter is available only when you set the Channel type parameter to DingTalk. Enter the secret key of the DingTalk robot. |
| smtp server address | This parameter is available only when you set the Channel type parameter to Email. Specify the address of the Simple Mail Transfer Protocol (SMTP) server. |
| smtp server port | This parameter is available only when you set the Channel type parameter to Email. Specify the port of the SMTP server. |
| Username | This parameter is available only when you set the Channel type parameter to Email. Specify a username that is used to log on to the SMTP server and send notifications. |
| Password | This parameter is available only when you set the Channel type parameter to Email. Specify the password of the username that is used to log on to the SMTP server and send notifications. |

| Whether to enable StartTLS | This parameter is available only when you set the Channel type parameter to Email. Specify whether to enable StartTLS as the protocol extension for mutual negotiations regarding encryption. |
|---|---|
| Whether to enable StartTLS | This parameter is available only when you set the Channel type parameter to Email. Specify whether to use the Secure Sockets Layer (SSL) protocol to encrypt data transmission. |
| Push URL | This parameter is available only when you set the Channel type parameter to Webhook. Enter the push URL. |
| Custom URL parameters | This parameter is available only when you set the Channel type parameter to Webhook. Specify the URL parameters in a POST request. The following preset parameter mappings are supported: ${contact list}: the list of contacts. _ ${content title}: the content title. _ ${content body}: the content body. _ |
| Custom header | This parameter is available only when you set the Channel type parameter to Webhook. Specify the headers in a POST request. Preset parameter mappings are supported. |
| Request body template (JSON string) | This parameter is available only when you set the Channel type parameter to Webhook. The request body in the POST request. Preset parameter mappings are supported. |
| Message content size (byte) | Enter the maximum number of bytes that can be sent in a message. Maximum value: 8192. |

5. Click **Test** to check the connectivity of the channel.
6. Click **Confirm** to complete the channel configuration.

**Related operations**

**View channel information**

1. In the upper-left corner of the Channel Management page, select **Channel group**,
**Channel name**, **Token**, **Channel type**, or **Channel Status** from the drop-down list, and
then specify a keyword to filter the channel whose information you want to view.
2. Click **Details** in the **Operation** column of the channel.
3. On the channel details page, click **Test** to check the connectivity of the channel.

**Edit channel information**

1. Find the channel whose information you want to modify and click **Edit** in the **Operation**
column of the channel.
2. In the dialog box that appears, modify the parameters and click **Test** to check the
connectivity of the channel.
3. Click **OK** to complete the modification.

**Delete a channel**

1. Find the channel that you want to delete and click **Delete** in the **Operation** column of the
channel.
2. In the message that appears, click **OK**.

#### 8.3.2 Push history

> You can view the message push records of the platform.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Settings**.
3. In the left-side navigation pane, choose **Notification Management** > **Push History**.
4. In the upper part of the page, select **Channel group**, **Channel name**, **Notification**
**source**, **Notification title**, or **Send Status** from the drop-down list. Then, specify the
keyword to search for the push records that you want to view.
5. Alternatively, click **Advanced Filter**, specify the **Channel group**, **Channel name**,
**Notification source**, **Notification title**, and **Send Status** parameters to filter push
records that you want to view.

### 8.4 Region coordinate management

**management**

If multiple regions exist in the current environment, the multi-region configuration administrator and super administrator can add regions. After you add regions, you can switch to different data centers in the same console and view information or perform O&M operations.

**Prerequisites**

Before you add regions, make sure that the following conditions are met: The networks between regions are connected and the regions share accounts that have the same usernames and passwords. You are granted the permissions of a multi-region configuration administrator or a super administrator.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **More > System Config**.
3. In the left-side navigation pane, click **Region Coordinate Management**.
4. In the upper-left corner of the Regions page, click **Add**, configure the parameters, and then
click **OK**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Region Console URL | The console URL of the region. Make sure that the console URL is valid. Otherwise, an error message is returned. |

| Cloud Name | The name of the new data center. |
|---|---|
| Longitude | The geographic longitude of the region. Valid values: 73 to 134. |
| Latitude | The geographic latitude of the region. Valid values: 18 to 53. |

5. After you add regions, you can log on to the Apsara Uni-manager Operations Console by
using a shared account to switch to different regions and perform related operations.

**What to do next**

You can modify the settings of the regions that you added.
1. Find the region that you want to modify and click **Edit** in the **Actions** column.
2. In the dialog box that appears, modify the parameters and click **OK**.

### 8.5 Archiving management

This topic describes the modules related to archiving management.

**Modules**

You can archive the key metadata of Apsara Stack. The archived metadata is used for quick recovery from Apsara Stack failures.

**Prerequisites**

System administrator permissions on the Apsara Uni-manager Operations Console are granted. Only the metadata of Apsara Distributed File System and OPS DNS can be archived.

**Modules**

| Module | Description |
|---|---|
| Archive Settings | You can view archive settings, modify archive settings, and trigger archive operations. |
| Archive Details | You can view archive details, including the archived product, archived item, file name, start time, and archive status. |
| Archive Products | You can view information about archived products, configure products to archive, and manage archived products. |
| Archiving Server Settings | You can configure the archive server for the storage of archive files. |

#### 8.5.1 Archiving settings

This topic describes how to configure archived items of products.

**Prerequisites**

The archive server is configured. Archived products are added. For more information, see Management of archived products.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Archive Settings**.
In the left-side pane of the Archive configuration page, the archived items that you can configure are displayed in a hierarchical tree structure. The root node is a product list and shows the products whose data can be archived in the system.

> **Note:** Only the metadata of Apsara Distributed File System and OpsDNS can be archived.

4. Click the item that you want to archive. In the right-side section, configure the parameters
that are described in the following table and click **Modify** to trigger the archive operation.

> **Note:** If the #FTPMaster server is deployed in the cluster of the product, the system automatically fills in the information about the ecs pangu archive server.

| Parameter | Description |
|---|---|
| Product cluster address | The IP address of the actual transfer server. |
| Archive file storage directory | A folder on the transfer server. You need to only enter a folder path in the field without the need to manually create a folder to store archived files. Example: Directory of Apsara Distributed File System: /apsarapangu/disk8/pangu master bak/Product namepangu/bak _ _ _ OpsDNS directory: /apsarapangu/disk8/opsdns bak/opsdns/bak _ |

| Script execution Directory | A folder on the transfer server. You need to only enter a folder path in the field without the need to manually create a folder to store scripts to be executed. Example: Directory of Apsara Distributed File System: /apsarapangu/disk8/pangu master bak/Product namepangu/bin _ _ _ OpsDNS directory: /apsarapangu/disk8/opsdns bak/opsdns/bak _ |
|---|---|
| Script execution parameters | Required. The execution parameters for the script. You must enter the value in the --ip=xxx.xxx.xxx.xxx format. Apsara Distributed File System: Enter an IP address of the pangu master. OpsDNS: We recommend that you enter --ip=127.0.0.1. |
| Execution cycle | The archiving schedule. In this example, a value of 1 is used, which specifies that the archiving is performed only once. |
| Archive Schedule Unit | The unit of the archiving schedule. Valid values: Day, Time, and Points. In this example, Time is selected, which specifies that the archiving is performed by hour. |
| Timeout | The timeout period. Unit: milliseconds. Default value: 3600. |

5. Repeat the operations in Step 4 to configure all archived items.

**What to do next**

After you configure the archived items, you can view the archiving details and status on the
**Archive details** page.

#### 8.5.2 Archiving details

This topic describes how to view the archiving details of each archived item.

**Prerequisites**

Archiving settings are configured and an archive operation is triggered.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Archive Details**.
4. You can filter archiving information by **Product**, **Archive item**, and **Date**.
5. View the details of an archived item, including **Product**, **Archive item**, **File name**, **Start**
**time**, and **Status**. The archiving states include **Not started**, **In progress**, **Complete**,
**Timeout**, and **Failed**.

> **Note:** If the state of an archived item is **Complete**, check whether the MD5 hash values of the offline archive service and the archive server are consistent with each other. If the values are consistent with each other, the archiving was successful.

#### 8.5.3 Management of archived products

This topic describes how to add archived products.

**Prerequisites**

Only the metadata of Apsara Distributed File System and OpsDNS can be archived. The archive server is configured.

**Archive a product**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click System Config.
3. In the left-side navigation pane, choose **Archive management** > **Archive Products**.
4. Click **Add products**. In the dialog box that appears, add a product and click **OK**.

| Parameter | Description | Example |
|---|---|---|

| Product | The name of the product. Select a product from the drop-down list. pangu opsdns | pangu |
|---|---|---|
| Script | The name of the archived script. The system automatically selects the script based on the product. | metadata backup.py _ |
| Archived Item | The product information to be archived. Note An archived item is the smallest unit for archiving. You can archive the metadata of Apsara Distributed File System for different services, such as ecs pangu, ots pangu, oss pangu, and ads pangu. | ecs pangu _ |
| Retry Times | The number of retries after an error occurs. Default value: 3. | 3 |

5. Repeat the preceding step to add all archived items. In most cases, you need to add
multiple archived items.

**What to do next**

**Modify an archived product item**

1. Click **Modify** in the **Operation** column of the archived item.
2. In the dialog box that appears, modify the parameters and click **OK**.

> **Note:** You can modify only **Retry Times**.

**Delete an archived product item**

1. Click **Delete** in the **Actions** column of the archived item.
2. In the message that appears, click **Reset**.

**What to do next**

After you add all new archived items of a product, the archived items are displayed on the
**Archive configuration** page. You can configure archiving settings for the archived items on
the Archive configuration page.

#### 8.5.4 Archive server settings

This topic describes how to configure the archive server that is used to store archived objects.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Archiving Server**
**Settings**.
4. Configure the parameters that are described in the following table and click **Submit**.

> **Note:** If the #FTPMaster server is deployed in the cluster of the service, the system automatically fills in the information about the ecs pangu archive server.

| Parameter | Description |
|---|---|
| Archive server address | The IP address of the archive server. The archive server must meet the following requirements: The archive server is an independent physical server. The archive server is managed by Apsara Infrastructure Management. The network of the archive server is connected to other servers in Apsara Stack. Apsara Distributed File System cannot be deployed on the server or on the disk where archived metadata is stored. |
| Archive Service listening path | The storage path of archived objects on the archive server. Note If the storage path does not start with /apsarapangu, /ASO- backup is added to the beginning of the path by default. The archive service detects new archived objects by monitoring the specified folder on the archive server and determines whether the archiving is successful by comparing the MD5 hash of the archived object with that of the original file. |
| Archive file cleaning cycle | The actual period of time an archived object is saved. Unit: day. Overdue archived objects are deleted. |

5. In the dialog box that appears, select **I have read the above prompts and confirmed**
**the operation.** and click **OK**.

**What to do next**

After you configure the archive server, you need to add new archived items on the **Archive**
**Products** page.

## 9 User permissions

### 9.1 User management

You can create a user and assign the user different roles to meet different requirements for system access control as an administrator.

**Prerequisites**

You are a role administrator. A department is created. A logon policy is created. If you want to assign a user a custom role, you need to first create the custom role.

**Usage notes**

The opsadmin user is the super administrator of ASO and is the only user that has full management permissions on ASO.

**Create a user**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **User Management**.
4. On the **Users** tab, click **Add**. In the dialog box that appears, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Username | The name for the user that you want to create. The name can be up to 48 characters in length and can contain digits, letters, underscores ( ), hyphens (-), and periods (.). You can enter email _ addresses as usernames. |
| Password | The password for the user. The password must be 10 to 20 characters in length and must contain letters, digits, and special characters. |
| Confirm Password | The password that you enter in the Password field. Make sure that the two passwords that you enter are the same. |
| Display name | Enter a display name for the user. |
| Logon Policy | The logon policy of the user. To create a logon policy, choose Security Management > Access Control > Login Rule in the top navigation bar. |

| Role | The role that you want to assign to the user. To create a role, click User Authorities in the top navigation bar and click Role Management in the left-side navigation pane. Note You can add multiple roles to a user. |
|---|---|
| Department | The department to which the user belongs. To create a department, click User Authorities in the top navigation bar and click Department Management in the left-side navigation pane. |
| Mobile phone | The mobile number of the user that you want to create. |
| Email address | The email address of the user that you want to create. |
| Allowed to Create AccessKey ID | Specifies whether to enable the creation of an AccessKey ID. |

5. After a user is added, you can view the information of the added user on the **Users** tab.

**Related operations**

**Query a user**

1. Click **Advanced Filter**.
2. Specify the **Username**, **Role**, and **Department** parameters and click Search to search for
a specific user.

**Export users**

Select the users to be exported and click **Export** to export the information of the users to your on-premises computer.

> **Note:** If you do not select a user, the information of all the users displayed on the Users tab is exported.

**Import users**

1. Click **Import**.
2. In the Import dialog box, click **Click Here to Upload File** , select the user list file that you
want to upload, and upload the file.

> **Note:** The imported users are imported to a level -1 department.

**Modify a user**

1. Find the user that you want to modify and click **Modify** in the **Actions** column.
2. In the **Modify user** dialog box, modify the parameters and click **OK**.

> **Note:** If you change the department of the user, the user is removed from all user groups that the user is added to, and the roles assigned to the users by the user groups are removed.

**Delete a user**

1. Find the user that you want to delete and click **Delete** in the **Actions** column.
2. In the dialog box that appears, select I have read the above prompts and confirmed the
operation, and then click **OK**.

> **Note:** After you delete a user, the AccessKey pair of the user is disabled, which may cause services or applications that use the AccessKey pair to fail to work as expected.
> After you delete a user, all roles assigned to the user are removed and the user is deleted from all user groups that the user is added to.

3. On the **Recycle Bin** tab, you can view the information of deleted users.

> **Note:** If you want to restore a user, find the user on the **Recycle Bin** tab and click **Recover** in the **Actions** column. In the message that appears, click **OK**.

**Activate a user**

If a user account is frozen because the user does not log on to the Apsara Uni-manager Operations Console within the time period specified by the account freeze policy, you can activate the account as an administrator.
1. Find the account that you want to activate and click **Activate** in the **Actions** column.
2. In the message that appears, click **OK**.

**Change the logon policy for users**

1. Select the users for which you want to modify the logon policy and click **Modify Logon**
**Policy** in the lower part of the page.
2. In the dialog box that appears, specify the **Logon Policy** parameter and click **OK**.

> **Note:** The logon policies of the opsadmin user cannot be modified.

### 9.2 User group management

You can add multiple users to a user group and add a role to the user group as an administrator for centralized management.

**Prerequisites**

You have the administrator permissions. A department has been created.

**Add a user group**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **User Group Management**.
4. Click **Add**. In the dialog box that appears, configure the parameters and click **OK**. The
following table describes the parameters:

| Parameter | Description |
|---|---|
| User Group Name | Enter the name of the user group. |
| Department | Select the department to which the user group belongs. To create a department, click User Authorities in the top navigation bar, click Department Management in the left-side navigation pane, and then click Add Department. |
| Role | Select the role that you want to add to the user group. To create a role, click User Authorities in the top navigation bar, click Role Management in the left-side navigation pane, and then click Create Role. Note You can add multiple roles to a user group. |

**Related operations**

**View user groups**

1. Click **Advanced Filter**.
2. You can filter user groups by **Department**, **Role**, **User Group Name**, and **User Name**.

**Modify a user group**

1. In the user group list, find the user group whose name you want to modify and click **Edit**
**User Group** in the **Actions** column.
2. In the dialog box that appears, modify the **User Group Name** and click **OK**.

**Delete a user group**

1. In the user group list, find the user group that you want to delete and click **Delete User**
**Group** in the **Actions** column.
2. In the message that appears, click **OK**.

**Manage users**

1. In the user group list, find the user group for which you want to manage users and click
**Manage Users** in the **Actions** column.
2. In the dialog box that appears, you can add users to or remove users from the user group.
Add: Click **Add**. In the dialog box that appears, select one or more usernames and click
**OK**.

> **Note:** You can add only users under the department to which the user group belongs.

Delete: Click **Delete** in the **Actions** column to delete the username.
3. Click **OK**.

**Add a role**

If the user group has no roles, you can add roles to the group.
1. In the list of user groups, find the user group whose role you want to modify and click **Add**
**role** in the **Actions** column.
2. In the dialog box that appears, select a role and click **OK**.

> **Note:** You can add multiple roles to a user group.

**Modify the role of a user group**

If a user group has roles, you can modify the roles of the user group.
1. Find the user group that you want to modify and click **Modify User Group Role** in the
**Actions** column.
2. In the dialog box that appears, modify the role and click **OK**.

### 9.3 Role management

A role is a collection of access permissions. You can assign different roles to different users to meet your requirements for system access control. You can set custom roles in the Apsara Uni-manager Operations Console to implement more flexible and efficient permission control.

**Prerequisites**

You are a role administrator. A maximum of 100 basic roles can be created.

**Background information**

Roles are classified into preset roles and custom roles. Preset roles are provided by the system, and you cannot modify or delete them. The following table describes the preset roles and their corresponding permissions.

| Role name | Description |
|---|---|
| System Admin | Manages O&M operations across the platform and has the read and write permissions on the following menus: Monitor&Alarms, Platform Operation, Product Operation, System Config, and User Authorities. |
| System Viewer | Views O&M operations across the platform and has the read-only permissions on the following menus: Monitor&Alarms, Platform Operation, Product Operation, System Config, and User Authorities. |

| Security Admin | Manages security-related O&M operations across the platform. This role has the following permissions: 1. The read and write permissions on the Security Management menu, excluding the Security Audit module. 2. The read and write permissions on the Server Logon and Account Authorization modules. To find the modules, choose Platform Operation > Apsara Infrastructure Management > Web Terminal in the top navigation bar of the Apsara Uni-manager Operations Console. |
|---|---|
| Security Auditor | Audits, tracks, and analyzes security-related O&M operations across the platform. This role has the following permissions: 1. The read and write permissions on the Security Audit module. To find the module, choose Security Management > Security Audit > Apsara Stack Security - Security Audit in the top navigation bar of the Apsara Uni-manager Operations Console. 2. The read and write permissions on the Server Logon, Account Authorization, and Operation Records modules. To find the modules, choose Platform Operation > Apsara Infrastructure Management > Web Terminal in the top navigation bar of the Apsara Uni-manager Operations Console. |
| Role Admin | Manages user permissions across the platform and has the read and write permissions on the User Authorities menu. |
| Role Viewer | Views user permissions across the platform and has the read-only permissions on the User Authorities menu. |
| Platform security administrator | Inherits the permissions of the security administrator and has higher security management permissions, such as managing Container Registry. |
| Platform Operation administrator | Inherits the permissions of the system O&M administrator and manages the personal workbench. |
| CRE/TAM | Has the read-only permissions on all console menus excluding the Security Management menu, and has the read and write permissions on the SRE Technical Assurance Platform. This role is used for on-site O&M. |

**Create a role**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Role Management**.
4. In the upper part of the Roles page, click **Create Role**.
5. In the **Basic Configuration** step, configure the parameters that are described in the
following table and click **Next Step: Console Permissions**.

| Parameter | Description |
|---|---|
| Role Name | The name of the role. |
| Role Description | The description of the role. |

6. In the **Console Permissions** step, configure console permissions for the role. Then, click
**Next Step: Product Permissions**.

> **Note:** You can search for permissions by using the search box in the upper part of this step. You can also select View Authorized Users to view only authorized menus.
> In the upper-right corner of this step, you can click **Select All: Read/Write** or **Select All: Read-only**.

7. In the **Product Permissions** step, configure product permissions for the role. Then, click
**Next Step: Menu Permissions**.

> **Note:** You can search for permissions by using the search box in the upper part of this step. You can also select View Authorized Users to view only authorized menus.
> In the upper-right corner of this step, you can click **Select All: Read/Write** or **Select All: Read-only**.

8. In the **Menu Permissions** step, configure menu permissions for the role and click **Create**.

**What to do next**

**View the details of a role**

1. In the upper part of the Roles page, enter the name of a role to search for the role.
2. Find the role and click the role name. On the **Role Details** page, view the basic
information about the role and the information on the **Console Permissions**, **Product**
**Permissions**, **Menu Permissions**, and **Authorized User** tabs.

> **Note:** If you want to modify a custom role, you can click **Edit** in the upper-right corner of the Role Details page.

3. On the **Authorized User** tab, view the users that are associated with the role.
If you want to associate a user with the role, click **Add Authorized Users**. In the dialog box that appears, enter a username in the **Username** field, select the user, and then click **OK**. If you want to disassociate a user from the role, find the user and click **Remove** in the
**Actions** column. In the message that appears, click **Remove**.

**Modify a custom role**

> **Note:** Preset roles cannot be modified.

1. On the Roles page, find the custom role that you want to modify and click **Edit** in the
**Actions** column.
2. Modify the role permissions by following the same steps for creating a role. Then, click
**Update**.

**Delete a role**

> **Note:** Preset roles cannot be deleted.
> Before you delete a role, make sure that the role is not associated with a user. Otherwise, the role cannot be deleted.

1. On the Roles page, find the custom role that you want to delete and click **Delete** in the
**Actions** column.
2. In the message that appears, click **Delete**.

### 9.4 Department management

The Apsara Uni-manager Operations Console provides a root department by default. You can create, delete, modify, and query departments under the root department. You can also create users and user groups for a department.

**Prerequisites**

You have the administrator permissions. You can create up to five levels of departments. A user other than opsadmin can view only the department to which the user belongs and its subordinate departments (including level-1 departments).

**Create a department**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Department Management**.
4. On the left side of the Departments page, you can view the tree structure of all
departments. You can also view the information about all users and user groups in each department by clicking the department name.
5. In the catalog tree on the left, select the department to which you want to add a sub-
department and click **Add Department** in the right section. In the Add Department dialog box, enter a value in the **Department Name** field, and click **OK**. Then, you can view the created department in the catalog tree. The **Department Name** parameter can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).

**Related operations**

**Modify a department**

1. In the catalog tree on the left, select the department that you want to modify and click
**Modify Department** in the right section.
2. In the dialog box that appears, enter a new department name and click **OK**.

**Delete a department**

> **Note:** Before you delete a department, make sure that no users exist in the department. Otherwise, the department cannot be deleted.

1. In the catalog tree on the left, select the department that you want to delete and click
**Delete Department** in the right section.
2. In the message that appears, click **OK**. The department is then deleted.

**Add users to a department**

1. In the catalog tree on the left, select the department to which you want to add users, click
**Add users** in the right section.
2. In the dialog box that appears, configure the parameters and click **OK**. For more
information about the parameters, see User management. After you add users to a department, you can view the information about the users on the
**User Management** page.

**Add a user group to a department**

1. In the catalog tree on the left, select the department to which you want to add a user
group, click **Add user groups** in the right section.
2. In the dialog box that appears, configure the **user group name**, select a **role**, and then
click **OK**. After you add a user group, you can view the information about the user group on the **User**
**Group Management** page.

### 9.5 Department-region association

**association**

In multi-region scenarios, O&M engineers can associate departments with regions. After a department is associated with a region, users in the department can manage and view resources in the region.

**Background information**

In multi-region scenarios, a region is managed by its administrators. After administrators log on to the Apsara Uni-manager Operations Console from the central region, they can only manage resources in the associated regions. Relationship between departments and regions: A department can be associated with multiple regions. A region can be associated with multiple departments.

**Limits**

Only departments at tier 1 can be associated with regions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Department Region association**.
4. In the left-side Department directory tree, select the department that you want to associate
with regions. In the **Associated Regions** section on the right, select one or more regions that you want to associate with the department.
5. Click **Update Association**.

### 9.6 Menu settings

The Menu Settings module allows you to add, modify, or delete a menu based on your business requirements.

**Usage notes**

A menu supports up to five menu levels.

**Add menu data**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **More > User Authorities**.
3. In the left-side navigation pane, click **Menus**.
4. In the upper part of the Menus page, click **Add Menu Data**, or click **Add Submenu** in the
**Actions** column corresponding to a menu path. In the panel that appears, configure
parameters and click **OK**. The following table describes the parameters that you need to configure.

| Parameter | Description |
|---|---|

| Parent Node ID | Select a parent menu. This parameter does not need to be specified when you add a level-1 menu. |
|---|---|
| Unique Identifier | The unique identifier that is used to invoke functions. We recommend that you specify a unique identifier that contains 5 to 20 characters. |
| Default Display Name | The default display name of the menu. |
| Name in Chinese | The menu name in Chinese. In the Chinese language environment, if the Chinese name of the menu is specified, the default display name of the menu is the specified Chinese name. |
| Name in English | The menu name in English. In the English language environment, if the English name of the menu is specified, the default display name of the menu is the specified English name. |
| Description | The description of the menu. |
| Show or not | Specifies whether to display the menu after it is added. By default, this feature is enabled. |
| Is it a Link | Specifies whether to navigate users to another page when they click the menu. By default, this feature is disabled. |
| URL | This parameter appears if you turn on Is it a link. The URL to which users are navigated when they click the menu. To navigate users to a page of the system, specify the absolute or relative path of the page. To navigate users to a page of a third-party system, specify the absolute path of the page. |
| Link new page to open | This parameter appears if you turn on Is it a link. Specifies whether to open the URL on a new page after users click the menu. By default, this feature is disabled. |
| Current Order | The order of the menu among all menus in the same parent menu. You cannot configure the order in the panel. You can modify the configuration on the Menus page after you create the menu. |

5. After the menu is added, you can view it in the menu list.

**What to do next**

**Modify the menu**

1. In the menu list, find the menu that you want to modify and click **Modify** in the **Actions**
column.
2. In the Edit menu items panel, modify the configurations and click **OK**.
3. In the **Actions** column, click **Move Up** or **Move Down** to change the order of the menu.

**Delete the menu**

1. In the menu list, find the menu that you want to delete and click **Delete** in the **Actions**
column.
2. In the message that appears, click **OK**.

> **Note:** Built-in menus of the system cannot be deleted.

## 10 Emergency response

This topic describes the scenarios in which the emergency response is triggered. When degradation is triggered in the Apsara Uni-manager Operations Console, the console switches to the emergency mode and the emergency page appears.

**Scenario**

1. Log on to the Apsara Uni-manager Operations Console.
2. Degradation is triggered in the Apsara Uni-manager Operations Console, as shown in the
following figure.
3. Click **Enable emergency mode**.
4. Enter a valid username and password, and click **Log In**.

> **Note:** The username and password used to log on to the Apsara Uni-manager Operations Console are the same as those used to switch to the emergency mode of the console.

5. After the Apsara Uni-manager Operations Console switches to the emergency mode, the
emergency response page appears.

### 10.1 Watchdog monitoring and alerting

**alerting**

Some global faults in Apsara Stack, such as MiniRDS faults, faults of the physical network, and OpsDNS faults, may cause exceptions in the Apsara Uni-manager Management Console. This topic describes **watchdog monitoring and alerting**, which is used to monitor and alert the global availability. Watchdog monitoring and alerting can be used to monitor faults that may cause global faults or invalidate the original alert list. Watchdog monitoring and alerting displays**Overview of final state of key products (exception/All SR)** , **Monitoring**
**Status**, and **Alert status** for faults.

> **Note:** The Monitoring Alarm page displays only watchdog monitoring and alerting items. To view other monitoring and alerting items, choose **Monitor&Alarms** > **Alerts** > **Alerts** in the Apsara Uni-manager Operations Console.

**Features**

| Feature | Description |
|---|---|
| Detection of global faults in Apsara Stack | Detects global network faults, and checks whether network components such as Server Load Balancer (SLB), Domain Name System (DNS), gateways, and physical links are normal. Detects global faults of the MiniRDS database in Apsara Stack or faults of major instances. |
| Detection of alert link faults | Detects features in the Apsara Uni-manager Management Console, including homepage logon, user authentication, and alerting. Detects TianjiMon features and sends alerts when data output faults or alert output faults occur. |
| Alert viewing and sending | Supports on-site registration of alert callback gateways to send alerts from the out-of-band network when exceptions are detected. Provides a simple data viewing page. |

1. Log on to theApsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, click **Failure emergency**.
3. In the left-side navigation pane, click **Watchdog Monitoring Alert**.
4. In the **Overview of final state of key products (exception/All SR)** section of the
Monitoring Alarm page, view all server roles and abnormal server roles of each major product.
5. Click the name of a product that has abnormal server role data to view the detailed server
role information.
6. In the **Monitoring status** section, view the check item information, including **Check**
**items**, **Description**, **Check time**, **Status**, and **Error Description**. In the Search for check
items field, enter a keyword to search for a check item. Fuzzy queries are supported.
7. In the **Alert status** section, view the alert information, including **Alert ID**, **Alert**
**information**, **Resource ownership**, **Latest alert time**, and **Number of alarms**. In the
Search for alert ID/alert information field, enter a keyword to search for an alert ID or the related alert information. Fuzzy queries are supported.

### 10.2 Scenario diagnostics

This topic describes the preset fault scenarios. You can select a scenario to trigger a diagnostics plan.
1. Log on to the Apsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, click **Failure emergency**.
3. In the left-side navigation pane, click **Scenario Diagnosis**.
4. On the **Diagnostic plan** tab of the Scenario diagnosis page, view the preset fault
scenarios. In the upper part of the Diagnostic plan tab, enter a plan name keyword in the Search Plan Name field to search for a diagnostics plan. Fuzzy queries are supported. Find the diagnostics plan that you want to manage and click **Execute** in the **Operation** column to view the execution process and result. The following table describes the common preset diagnostics plans.

| Plan name | Description |
|---|---|
| Diagnostics for faults in the Apsara Uni-manager Operations Console or the Apsara Uni-manager Management Console | If the homepage of the Apsara Uni-manager Operations Console or Apsara Uni-manager Management Console is accessible but an error occurs when you log on to the console, you can use this plan for diagnostics. This plan diagnoses terminal servers, AAS, UmmAk, Tair, and MiniRDS. |
| Diagnostics for faults in the management portal | If the management portal is accessible, you can use this plan for diagnostics. This plan diagnoses terminal servers, OpsDNS, Server Load Balancer (SLB), network components, and MiniRDS. |

| Diagnostics for a large number of faults in Apsara Infrastructure Management | This plan diagnoses terminal servers, Docker hosts, MiniRDS, basic services of Apsara Infrastructure Management, and OpsDNS. |
|---|---|
| Diagnostics for terminal servers | This plan diagnoses terminal servers. |
| Diagnostics for Docker hosts | This plan diagnoses Docker hosts. |
| Diagnostics for MiniRDS hosts | This plan diagnoses MiniRDS physical machines. |

5. On the **Execution History** tab, view the diagnostics plans that you executed.
In the upper part of the Execution History tab, enter a plan name keyword in the Search Plan Name field to search for a diagnostics plan. Fuzzy queries are supported. The Execution History tab includes the following fields: **Plan Name**, **Scenario**
**description**, **Execution time**, and **Execution result**.
Find the diagnostics plan that you want to view and click **Details** in the **Operation** column to view the execution process and result.

### 10.3 Emergency plan

This topic describes the preset emergency plans. You can select a scenario to trigger an emergency plan.
1. Log on to the Apsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, click **Failure emergency**.
3. n the left-side navigation pane, click **Emergency plan**.
4. In the **Instance Information** section of the Emergency plan page, view the information
about the instances that are connected to O&M platforms. Click **Link** next to an O&M platform to go to the O&M platform.
5. On the **Emergency plan** tab of the Emergency plan page, view the preset emergency
plans. In the Search Plan Name field, enter a plan name keyword to search for an emergency plan. Fuzzy queries are supported. Find the emergency plan that you want to manage and click **Execute** in the **Operation** column to view the execution process and result. The following table describes the common preset emergency plans.

| Plan name | Description |
|---|---|
| Stop the ops.OpsDnsSlave .dnsslave __ service of Oracle parallel server (OPS) 2 | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in OPS 2. |
| Disable authentication in Apsara Infrastructure Management | You can use this plan to temporarily disable authentication in Apsara Infrastructure Management before you log on to the Apsara Infrastructure Management console to perform O&M operations. |
| Enable authentication in Apsara Infrastructure Management | You can use this plan to temporarily disable authentication in Apsara Infrastructure Management. |
| Disable authentication in ApsaraDB Operations and Maintenance System | You can use this plan to disable authentication in ApsaraDB Operations and Maintenance System (Lite) before you log on to the system by using a local account. |
| Enable authentication in ApsaraDB Operations and Maintenance System | You can use this plan to enable authentication in ApsaraDB Operations and Maintenance System after faults are rectified. |
| Restart AAS and UmmAk | You can use this plan to restart authentication components when the authentication link is abnormal. |

| Restart POP | You can use this plan to restart POP when POP is abnormal. |
|---|---|
| Restart the ops.OpsDnsSlave .dnsslave __ service of OPS 1 | You can use this plan to restart the DNS slave service when the DNS resolution is abnormal in OPS 1. |
| Restart the ops.OpsDnsSlave .dnsslave __ service of OPS 2 | You can use this plan to restart the DNS slave service when the DNS resolution is abnormal in OPS 2. |
| Restart the ops.OpsDnsSlave .dnsslave __ named service in OPS 1 | You can use this plan to restart the DNS slave named service when the DNS resolution is abnormal in OPS 1. |
| Restart the ops.OpsDnsSlave .dnsslave __ named service in OPS 2 | You can use this plan to restart the DNS slave named service when the DNS resolution is abnormal in OPS 2. |
| Stop the ops.OpsDnsSlave .dnsslave __ service in OPS 1 | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in OPS 1. |

6. On the **Execution History** tab, view the emergency plans that you executed.
In the Search Plan Name field, enter a plan name keyword to search for an emergency plan. Fuzzy queries are supported. The Execution History tab includes the following fields: **Plan Name**, **Scenario**
**description**, **Execution time**, and **Execution result**.
Find the emergency plan that you want to view and click **Details** in the **Operation** column to view the execution process and result.

### 10.4 Emergency web terminal

#### 10.4.1 Server logon

On the Server logon page, you can query and log on to servers.
1. Log on to the Apsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, click **Failure emergency**.
3. In the left-side navigation pane, choose **Emergency Web Terminal** > **Server Login**.
4. In the upper part of the Server logon page, view the OPS#1, OPS#2, OPS#3, and OPS#4
management nodes to which you can quickly log on.
5. On the Server logon page, specify values for the **Hostname**, **IP address**, **Product**, and
**Cluster** parameters to search for a server.
6. Find the server that you want to manage and click **Login** in the **Operation** column.
7. Log on to the web terminal page. Click a logon node or the
icon. In the CLI window, enter Linux commands to perform related operations.

#### 10.4.2 Database logon

On the Database logon page, you can query and log on to the metadatabases that are requested by services.
1. Log on to the Apsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, click **Failure emergency**.
3. In the left-side navigation pane, choose **Emergency Web Terminal** > **Database Login****.**
4. On the Database logon page, specify values for the **Service** and **Name** parameters to
search for a metadatabase.
5. Find the metadatabase that you want to manage and click **Login** in the **Operation** column.
6. Log on to the web terminal page. Click a logon node or the
icon and enter SQL statements in the CLI window to perform related operations.
