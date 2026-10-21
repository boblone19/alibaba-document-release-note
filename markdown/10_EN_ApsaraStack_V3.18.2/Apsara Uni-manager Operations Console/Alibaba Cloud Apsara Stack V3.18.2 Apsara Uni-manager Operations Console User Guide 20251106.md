---
title: "Alibaba Cloud Apsara Stack V3.18.2 Apsara Uni-manager Operations Console User Guide 20251106"
product_version: "V3.18.2"
doc_version: "20251106"
pdf_pages: 273
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Apsara Uni-manager Operations Console User Guide 20251106.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/ASO/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Apsara%20Uni-manager%20Operations%20Console%20User%20Guide%2020251106.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Apsara Uni-manager Operations Console User Guide 20251106

## Table of Contents

- 1 Overview
- 2 Get started
  - 2.1 Prepare an operations account
  - 2.2 Log on to the Apsara Uni-manager Operations Console
  - 2.3 Operation platform
- 3 General O&M
  - 3.1 Monitoring and management
  - 3.2 Alerts
    - 3.2.1 Alert overview
    - 3.2.2 Alerts
    - 3.2.3 Alert settings
      - 3.2.3.1 Policy management
      - 3.2.3.2 Alert templates
      - 3.2.3.3 Alert notification
      - 3.2.3.4 Alert masking
      - 3.2.3.5 Masked alerts
      - 3.2.3.6 Alert rule settings
  - 3.3 Inspections
    - 3.3.1 All inspections
    - 3.3.2 Inspection dashboard
    - 3.3.3 Inspection scenarios
    - 3.3.4 Inspection records
    - 3.3.5 Inspection notifications
  - 3.4 Event center
    - 3.4.1 Event list
    - 3.4.2 Event grading
    - 3.4.3 My events
- 4 Platform O&M
  - 4.1 Apsara Infrastructure Management
    - 4.1.1 Resource management
      - 4.1.1.1 Product & Cluster O&M
        - 4.1.1.1.1 List view
          - 4.1.1.1.1.1 Cluster details
          - 4.1.1.1.1.2 Component details
        - 4.1.1.1.2 Panoramic view
      - 4.1.1.2 Machines
        - 4.1.1.2.1 List view
          - 4.1.1.2.1.1 Machine details
        - 4.1.1.2.2 Topology view
      - 4.1.1.3 Resource tags
      - 4.1.1.4 Base machine resource dashboard
    - 4.1.2 Kubernetes cluster management
      - 4.1.2.1 Cluster overview
      - 4.1.2.2 Node management
    - 4.1.3 Hardware O&M
      - 4.1.3.1 HDD repairs
        - 4.1.3.1.1 Preparation
        - 4.1.3.1.2 Repair
        - 4.1.3.1.3 History
      - 4.1.3.2 Machine repairs
    - 4.1.4 O&M tools
      - 4.1.4.1 Task management
      - 4.1.4.2 Service management
      - 4.1.4.3 VM dashboard
      - 4.1.4.4 Dashboard of service registration variables
      - 4.1.4.5 Resource dashboard
      - 4.1.4.6 Basic service monitoring
    - 4.1.5 Web clients
      - 4.1.5.1 Web Client Logon
        - 4.1.5.1.1 Server Logon
        - 4.1.5.1.2 Database logon
        - 4.1.5.1.3 vSwitch logon
      - 4.1.5.2 Account authorization
      - 4.1.5.3 Command management
      - 4.1.5.4 Operation audit
  - 4.2 Capacity management
    - 4.2.1 Capacity overview
    - 4.2.2 Computing capacity
      - 4.2.2.1 ECS capacity
    - 4.2.3 Network capacity
      - 4.2.3.1 SLB Capacity
    - 4.2.4 Storage capacity
      - 4.2.4.1 EBS
      - 4.2.4.2 OSS
      - 4.2.4.3 Tablestore
      - 4.2.4.4 Simple Log Service
      - 4.2.4.5 Apsara File Storage NAS
    - 4.2.5 Base capacity
      - 4.2.5.1 Apsara Infrastructure Management storage capacity
    - 4.2.6 Database capacity
      - 4.2.6.1 RDS
      - 4.2.6.2 ApsaraDB RDS for PostgreSQL
      - 4.2.6.3 ApsaraDB for Redis
      - 4.2.6.4 ApsaraDB for MongoDB
      - 4.2.6.5 AnalyticDB for PostgreSQL
      - 4.2.6.6 PolarDB for PostgreSQL
      - 4.2.6.7 PolarDB-X
      - 4.2.6.8 ApsaraDB for OceanBase
    - 4.2.7 Middleware capacity
      - 4.2.7.1 ApsaraMQ for Kafka
  - 4.3 Control Service Platform
  - 4.4 O&M Change
    - 4.4.1 Log cleanup
      - 4.4.1.1 Rule management
      - 4.4.1.2 Plans
      - 4.4.1.3 Records
    - 4.4.2 Process approval
      - 4.4.2.1 My submission
      - 4.4.2.2 My approval
  - 4.5 Disaster recovery management
  - 4.6 Log center
    - 4.6.1 Log map
    - 4.6.2 Log query
    - 4.6.3 Log transfer
    - 4.6.4 Log monitoring
- 5 Product O&M
- 6 Security management
  - 6.1 Security audit
    - 6.1.1 Operation audit
      - 6.1.1.1 Console-based Audit
      - 6.1.1.2 CLI-based Audit
  - 6.2 Host security
    - 6.2.1 Server Guard User Guide
      - 6.2.1.1 Physical server security
        - 6.2.1.1.1 Create and grant permissions to a security administrator account
        - 6.2.1.1.2 Physical servers
          - 6.2.1.1.2.1 Manage physical server groups
          - 6.2.1.1.2.2 Manage physical servers
        - 6.2.1.1.3 Server fingerprints
          - 6.2.1.1.3.1 Manage listening ports
          - 6.2.1.1.3.2 Manage software versions
          - 6.2.1.1.3.3 Manage processes
          - 6.2.1.1.3.4 Manage account information
          - 6.2.1.1.3.5 Manage scheduled tasks
          - 6.2.1.1.3.6 Set the fingerprint collection frequency
        - 6.2.1.1.4 Intrusion events
          - 6.2.1.1.4.1 Intrusion event types
          - 6.2.1.1.4.2 View and handle alert events
          - 6.2.1.1.4.3 View exceptions related to an alert
          - 6.2.1.1.4.4 Use the file quarantine feature
          - 6.2.1.1.4.5 Configure alerts
        - 6.2.1.1.5 Log retrieval
          - 6.2.1.1.5.1 Supported log sources and fields
          - 6.2.1.1.5.2 Logical operators
          - 6.2.1.1.5.3 Query logs
        - 6.2.1.1.6 Configure security settings for physical servers
  - 6.3 Network security
    - 6.3.1 Network Security Management Center
      - 6.3.1.1 East-west security management
        - 6.3.1.1.1 Policy center
          - 6.3.1.1.1.1 Policy content management
          - 6.3.1.1.1.2 VIP protection
        - 6.3.1.1.2 DNS rules
        - 6.3.1.1.3 Device network access management
  - 6.4 Account security
    - 6.4.1 Linux account management
      - 6.4.1.1 Password management for root user
      - 6.4.1.2 SSH key management
      - 6.4.1.3 System user management
      - 6.4.1.4 Linux account management task
        - 6.4.1.4.1 Task template management
        - 6.4.1.4.2 Task execution records
    - 6.4.2 Account management for cloud services
      - 6.4.2.1 Account ACL control
      - 6.4.2.2 Service boundary
        - 6.4.2.2.1 ACL
  - 6.5 Access control
    - 6.5.1 Security policies
    - 6.5.2 Logon policies
    - 6.5.3 Two-factor authentication
- 7 System settings
  - 7.1 Authorization Information
  - 7.2 Custom settings
  - 7.3 Notification management
    - 7.3.1 Channel management
    - 7.3.2 Push history
  - 7.4 Region coordinate management
  - 7.5 Archives
    - 7.5.1 Backup settings
    - 7.5.2 Backup details
    - 7.5.3 Archive product management
    - 7.5.4 Archiving server settings
- 8 User permissions
  - 8.1 User management
  - 8.2 User group management
  - 8.3 Role management
  - 8.4 Departments
  - 8.5 Regions associated with department region
  - 8.6 Menu settings
- 9 Emergency response
  - 9.1 Watchdog monitoring and alerting
  - 9.2 Scenario Diagnosis
  - 9.3 Emergency plans
- 10 Developer portal

## 1 Overview

This topic describes the management framework of the Apsara Uni-manager Operations Console.

**Management framework of the Apsara Uni-manager Operations**

**Console**

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

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser. We recommend that you use Google Chrome.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and Traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.

### 2.3 Operation platform

This topic describes the operations and features of the sections in the operation platform in the Apsara Uni-manager Operations Console.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Operation Platform**.
3. The following table describes the operations and features of the sections on the Operation
Platform page.

| S/N | Section | Description |
|---|---|---|
| 1 | Region selector | Select a region from the drop-down list to switch the region. This feature helps you manage all regions in a centralized manner. |
| 2 | Top navigation bar | Hover over or click a feature for more options. |
| 3 | Language | Click to switch the language. Simplified Chinese, Traditional Chinese, and English are supported. |
| 4 | Color display mode | Click to set the color mode to light mode or dark mode. |

| 5 | Help center | Click to view online documentation. |
|---|---|---|
| 6 | Message center | Click to view the approval notifications and alert notifications that are not handled on the Approval Messages and Alert Messages tabs. |
| 7 | User center | Click to modify personal information, view version information, or log out. |
| 8 | Overview | View information and perform operations. |

4. The following table describes the items in the **Overview** section.

| Item | Description |
|---|---|
| Resource overview | View the numbers of Product, Rack, Machine, and Network device. |
| BMS Resource Overview | View the data related to bare metal servers (BMS). Resource pool running instance: the bare metal servers that are managed in the resource pool and in the Running state. This data is the same as the data of the Total Resource Pool Instances parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console. Applied Instances: all instances that are applied for by the tenant. The instances cannot be filtered by state. This data is the same as the data of the Total Applied Instances parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console only when the organization type is root. Running Instances: the applied instances that are in the Running state. This data is the same as the data of the Total Running Instances on the Overview page of the BMS console in the Apsara Uni-manager Management Console only when the organization type is root. Images: the total number of custom images and public images in the selected regions. In multi-region scenarios, only when you select multiple same regions, the data is the same as the data of the Image parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console. In single-region scenarios, the data is the same as the data of the Image parameter on the Overview page of the BMS console in the Apsara Uni-manager Management Console. |
| Product Alert Summary | Displays the number of unclosed alerts of each level. |
| Product Alert Trend | Displays the number of alerts of each level and the trend chart. |

| My favorite | Displays the features in the top navigation bar that you added as favorites. If you want to update a feature in or add a feature to the favorite, perform operations in the top navigation bar. |
|---|---|
| Recent Visits | Displays the menu pages that you recently accessed. |
| Server distribution | Displays the distribution of physical servers by CPU and the total number of physical servers. |
| Cloud product server distribution | Displays the distribution of cloud service servers by CPU on the tenant side. |
| To be handled | Displays the content and submission time of the workflows that require your approval. You can click View details in this section to go to the Pending Approval page. The handled in recent week tab displays the content and approval time of the workflows that you approved in the last seven days. |
| Cloud Product Capacity Usage | Displays the capacity of cloud products. |
| Developer portal | Provides quick access to the development platform. For more information, see Open platform. |

## 3 General O&M

### 3.1 Monitoring and management

This topic lists the supported monitoring and management platforms. For more information about O&M operations, see the corresponding product documentation. TianjiMon - CloudMonitor TianjiMon - Grafana

### 3.2 Alerts

This topic describes modules of the alert management feature.

**Positioning**

If exceptions or faults occur in cloud infrastructure or software on the cloud platform, alerts are triggered. The sources of alerts include monitored cloud products, the monitoring system, and objects that are monitored by the monitoring system. After alerts are generated, the alert information is displayed on the Alert Overview, Alerts, and Alert details pages from different dimensions. For example, the total number of alerts for each module of a product is displayed on the Alert Overview page, alerts are converged and the number of alerts is increased on the Alerts page, and the details of an alert is displayed on the Alert details page.

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
|---|---|
| tpcmon | Apsara Stack lightweight monitoring system (TPCMon) |
| dts | Data Transmission Service (DTS) |
| Bcmc# | Zone-disaster recovery system of Apsara Stack Resilience |
| DB | License for Apsara Stack products |
| asapi | Apsara Stack API operations |
| drds | PolarDB-X |
| asrbr-backup | Backup and recovery system of Apsara Stack Resilience |
| ascm | Apsara Uni-manager Management Console |
| dbs-dbs | Database Backup Service (DBS) |
| admin-server | admin-server |
| asd | Apsara Stack Doctor (ASD) |
| sds-management | sds-management |
| bcc | Apsara Bigdata Manager (BCC) |
| aso-inventory | Inventory monitoring system of Apsara Uni-manager Operations Console |
| OcpApiV2 | ApsaraDB for OceanBase |

#### 3.2.1 Alert overview

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

#### 3.2.2 Alerts

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

#### 3.2.3 Alert settings

**Modules**

| Module | Description |
|---|---|
| Policy Management | You can configure alert notification contacts, contact groups, and static parameters. |
| Alert Templates | You can manage alert templates. |
| Alert Notification | You can configure alert notification channels to push alert notifications to parties of interests. |
| Alert Blocking | You can block alerts based on time range, resource ownership, cluster, service, server role, server, alert level, and alert source settings. You can also block specific alerts based on alert IDs. |
| Blocked Alerts | You can view blocked alerts and their details and associated blocking rules. |
| Alert Rule Settings | You can view rules that trigger alerts. |

##### 3.2.3.1 Policy management

The Policy Management module allows you to configure alert contacts, contact groups, and other static parameters.

**Manage contacts**

You can query, add, modify, or delete alert contacts based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. You can perform the following operations:
Query an alert contact In the upper-left corner of the Policy Management page, select the name of the service for which you want to query alert contacts from the Product drop-down list and enter contact names in the Name field. Then, you can view the details of the alert contacts that meet the search conditions. Add an alert contact Click **Add Contact**. In the dialog box that appears, configure parameters and then click
**OK**. The following table describes the parameters that you need to configure.

| Parameter | Description |
|---|---|
| Name | Enter a name for the new alert contact. |
| Role | Select a role for the new alert contact. Valid values: Developer: a developer TAM: an O&M person |
| Product | Select the products for which you want to create the new alert contact. You can select multiple products. |
| Alert Severity | Select alert levels. You can select multiple alert levels. P1: critical P2: major P3: minor P4: reminder |
| Aggregation Dimension | Select an alert push method. Valid values: One By One Product Metrics Machine |

| Duty Hours | Select the start date and end date of the watch-hour of the new alert contact. |
|---|---|
| DingTalk ID | Enter the DingTalk ID of the new alert contact. |
| Email Address | Enter the email address of the new alert contact. |

Modify an alert contact Click **Modify** in the **Operation** column that corresponds to an alert contact. In the dialog box that appears, modify the information and click **OK**. Delete an alert contact Click **Delete** in the **Operation** column that corresponds to an alert contact. In the message that appears, click **OK**.

**Manage contact groups**

You can query, add, modify, or delete alert contact groups based on your business requirements.

**Prerequisites**

Alert contacts are created.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. Click the **Contact Groups** tab.
5. You can perform the following operations:
Query an alert contact group Enter a group name in the search box to view the alert contact groups that meet the search conditions. Add an alert contact group In the upper-left corner of the Policy Management page, click **Add Contact Group**. In the dialog box that appears, configure parameters and then click **OK**. The following table describe the parameters.

| Parameter | Description |
|---|---|
| Group Name | Enter a name for the alert contact group. |
| Description | Enter a description for the alert contact group. |
| Select Contact | Select contacts to add to the contact group. |

Modify an alert contact group Click **Modify** in the **Actions** column that corresponds to an alert contact group. In the dialog box that appears, modify the information and click **OK**. Delete an alert contact group To delete a single contact group, find the contact group and click **Delete** in the
**Actions** column. In the message that appears, click **OK**.
To delete multiple contact groups at a time, select multiple contact groups and click
**Delete** in the lower part of the page. In the message that appears, click **OK**.

**Static Parameter Settings**

You can configure alert-related static parameters based on your business requirements.

**Background information**

The current version does not support new alert configurations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Policy Management**.
4. Click the **Static Parameter Settings** tab.
5. In the upper-left corner of the Policy Management page, enter a parameter code in the
search box to query the settings of static parameters that meet the specified conditions.
6. Find the static parameter that you want to modify and click **Edit** in the **Operation** column.
7. In the **Modify Static Parameters** dialog box, modify parameters and then click **OK**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Parameter Name | Enter a parameter name that is related to the configuration. |
| Parameter Value | Enter a parameter value that corresponds to the parameter name. For example, the default parameter value of the Alarm Time Out parameter name is 5, which indicates 5 days. |
| Description | Enter a description for the configuration. |

##### 3.2.3.2 Alert templates

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

##### 3.2.3.3 Alert notification

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
| Push interface address | The IP address of the push interface. |
| Push interface port | The port number of the push interface. |
| Push interface URL | The URL of the push interface. |
| Push request method | The request method that is used to push alerts. Only theP OST method is supported. |
| Push cycle (minutes) | The interval at which alerts are pushed. Unit: minutes. |
| Number of alerts pushed at a time | The number of alerts that are pushed each time. |

| Push mode | The mode in which alerts are pushed. Valid values: ALL: All alerts are pushed in each push cycle. TOP: Only high priority alerts are pushed in each push cycle. |
|---|---|
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

##### 3.2.3.4 Alert masking

Alert masking allows you to mask alerts reported during a specified period of time, and mask alerts by product, cluster, service, service role, and machine. You can also mask alerts by alert ID.

**Prerequisites**

The permissions on the alert masking menu are obtained.

**Create an alert masking rule**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor & Alarms** > **Alerts** > **Alert Settings**.
3. In the left-side navigation pane, click **Alert Blocking**.
4. In the upper-left corner of the page, click **Create mask rules**. In the dialog box that
appears, configure the filters to mask alerts and click **OK**.

| Parameter | Description |
|---|---|
| Resource attribution | Optional. The name of the product to which the alert to be masked belongs. |
| Cluster | Optional. The name of the cluster to which the alert to be masked belongs. |
| Machine | Optional. The hostname of the Elastic Compute Service (ECS) instance to be masked. |
| Services | Optional. The name of the service to which the alert to be masked belongs. |
| Service role | Optional. The service role of the alert to be masked. |
| Alarm ID | Optional. The ID of the alert to be masked. |

| Alert level | Optional. The level of the alert to be masked. Valid values: P1: critical P2: major P3: minor P4: info |
|---|---|
| Alarm source | Optional. The source of the alert to be masked. |
| Shielding time period | Optional. The time period during which the alert to be masked occurs. |
| Effective status | Required. Specifies whether the masking rule takes effect. |

**Related operations**

**View alert masking rules**

Enter a keyword in the search box to filter masking rules. Fuzzy search is supported. Click **Advanced Search** and filter rules by **Resource attribution**, **Cluster**, **Services**,
**Service role**, and **Machine**.
In the **Effective status** column, filter masking rules that are **Open** or **Close**.

**Modify an alert masking rule**

1. Find the alert masking rule that you want to manage, and click **Edit** in the **Operation**
column.
2. In the dialog box that appears, modify the parameters and click **OK**.

> **Note:** You can enable or disable the alert masking rule by turning on or off the switch in the **Effective status** column.

**Delete an alert masking rule**

1. Find the masking rule that you want to delete and click **Delete** in the **Operation** column.
2. In the message that appears, click **OK**.

##### 3.2.3.5 Masked alerts

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
A dialog box appears. If the masking rule is not deleted, the details of the masking rule are displayed in the dialog box. You can modify the parameters in the dialog box and click **OK**. If the masking rule is deleted, message **Masking rule has been deleted** appears.

##### 3.2.3.6 Alert rule settings

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
|---|---|
| Indicates whether the rule is enabled | Indicates whether the alert rule is enabled. Valid values: Enabled and Disabled. |

5. Find the alert rule that you want to manage and click **Modify Alert Rule** in the **Operation**
column. In the dialog box that appears, modify the following parameters based on your business requirements and then click **Save and Verify**.

| Parameter | Description |
|---|---|
| Enable or Not | Specifies whether to enable the alert rule. |
| Alert Severity | The alert level. |
| Number of times the event is triggered | The number of times that the alert is triggered. |
| Trigger Rule | The alert triggering rule. To prevent the alert rule from becoming invalid, you can change only thresholds and can enter only numbers, including integers and decimals. |

> **Note:** After you modify the rule, the verification takes 3 to 5 minutes. Refresh the list to check whether the rule has taken effect.

6. In the upper-left corner of the Alert Rule Settings page, click **Export** to export alert rules
that are displayed on the page.

### 3.3 Inspections

This topic describes the features related to inspection management.

**Features**

In the Apsara Uni-manager Operations Console, you can perform quick inspections in various inspection scenarios to help maintain the health of your business system and cloud services.

| Feature | Description |
|---|---|
| All inspections | Multiple inspection scenarios are supported, including preset inspection scenarios and custom inspection scenarios. |
| Inspection dashboard | You can view statistics on executed inspection scenarios over a period of time. |

| Inspection settings | You can configure custom inspection scenarios to make inspections more efficient. |
|---|---|
| Inspection records | You can view all inspection records and the corresponding inspection reports. |
| Inspection notifications | You can configure how you want to receive inspection reports and notifications. |

#### 3.3.1 All inspections

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

#### 3.3.2 Inspection dashboard

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

#### 3.3.3 Inspection scenarios

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

#### 3.3.4 Inspection records

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

#### 3.3.5 Inspection notifications

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

### 3.4 Event center

The event center is an event management platform for Apsara Stack and allows you to manage alerts for cloud applications in a centralized manner and grade the alerts. The event center can classify, merge, and grade multiple types of alerts to effectively convert the alerts into events for you to handle and manage. This helps improve the O&M efficiency for Apsara Stack.

**Features**

| Feature | Description |
|---|---|
| Event list | You can obtain and manage events of various levels. For example, you can view details of an event and handle the event. |
| Event grading | An event grading policy is a set of configurations that convert Apsara Stack alerts into events. Each cloud service has its own event grading policy. |
| My events | A quick portal that allows you to handle events on theT o be handled by me and I participated in tabs. |

#### 3.4.1 Event list

On the Event List page, you can obtain and manage events of various levels. For example, you can view details of an event and handle the event.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **Event List**.
3. By default, the Event List page displays events whose **Event Level** is L1, L2, L3, L4, or L5
and **Processing Status** is **Pending response** or **Processing** By default, events in the list are displayed in descending order of start time. The most recent event is displayed at the top of the list. In the upper-right corner of the event list, you can click the icon to adjust the columns to display and their display order.
4. To find the desired event, filter the event list by selecting one or more values from the
**Event Level** and **Processing Status** drop-down lists.You can also click **Advanced Filter**
and filter the event list by **Event ID**, **Event title**, **Event description**, **Start time**,
**Recovery time**, **component**, **service**, **cluster**, and **project**.
5. Click the event title to go to the event details page.
In the upper-right corner of the page, click the icon to copy the page URL. In the upper-right corner of the page, click **Response** to respond to the event.

> **Note:** The **Transfer** and **Statement** buttons appear after the event is responded to.

On the event details page, you can view the event data in sections such as **Basic**
**properties**, **Event Handling**, and **Associated subevents**.

> **Note:** In the **Associated subevents** section, you can perform the following operations:
> In the upper-right corner, select the check box to view only the events that are in the Alarming state.
> Find the desired sub-event and click its title to view the sub-event details on the **Details**, **Alarm history**, and **Original information** tabs. Click **View ASO** **alerts** to go to the **Alert Details** page and view the alert details.

In the **Event trajectory** panel, you can view all trajectory information that is recorded from the start time to the end time of the event.

**What to do next**

**Export a report**

Click **Report export** above the event list to export the event data to your on-premises machine.

**Respond to multiple events at a time**

Select the desired events and click **Batch response** below the event list.

**Close multiple events at a time**

1. Select the desired events and click **Batch order closing** below the event list.
2. Configure the following parameters and click **Confirm**.

| Parameter | Description |
|---|---|
| Valid | Specify whether the event is valid. Valid values: Effective Invalid |
| Cause of the event | Select an event cause. |
| Reason for details | Enter a detailed cause for the event. |
| Processing result | Enter the processing result for the event. |

#### 3.4.2 Event grading

An event grading policy is a set of configurations that convert Apsara Stack alerts into events and is classified by cloud service. Each cloud service has its own event grading policy.

**Feature overview**

The event grading process consists of the following stages:
1. Alert conversion: The system converts different types of alerts into events one by one and
sets event levels.
2. Proportion-based correlation: The system merges events of the same instance category to
generate a new event. The following instance categories are supported: cloud service instances, work and management software instances, and worker node instances. Then, the system sets different event levels based on the proportion of abnormal instances and the importance level of the cloud service.
3. Highest level-based event merging: The system merges multiple events that have the same
event object to generate a new event.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **Event Grading**.
3. In the alert conversion step, click the desired policy.
i. In the policy details panel, view details of the event into which the alert is converted. The details include **Basic information**, **Matching Condition**, and **Grading rules**. ii. Click **Modify** to change the value in the **Event Level** column. Then, click **Save**.
4. In the proportion-based correlation step, click the desired policy.
i. In the policy details panel, view the proportion-based correlation details of the event. The details include **Basic information**, **Matching Condition**, and **Grading rules**.

> **Note:** When a sub-event of a specified level occurs on instances, the system considers the instances abnormal, and sets the level of the event after proportion-based correlation based on the following factors: the proportion of the number of abnormal instances and the importance level of the cloud service to which the instances belong. Cloud services are classified into the following importance levels: A, B, and C. The levels are listed in descending order of priority. When an event is assigned multiple levels based on different proportion-based correlation rules, the system uses the highest level for the event.
> For example, a cloud service whose importance level is B has 10 instances. Four of the instances have Level-5 sub-events, which is identified as a Level-3 event based on a proportion-based correlation rule. Five of the instances have Level-6 sub-events, which is identified as a Level-2 event based on a proportion-based correlation rule. Level 2 is a higher level than Level 3. Therefore, the level of the event generated after the proportion-based correlation is Level 2.

ii. Click **Modify** to add or remove demarcations between the proportion ranges of abnormal instances. You can also click Modify to change the event level that corresponds to a given abnormal instance proportion range. Then, click **Save**.
5. In the highest level-based event merging step, the system merges sub-events of the same
type into an event based on the highest level of the sub-events. The generated event level is equal to the highest level among all sub-event levels.

> **Note:** The rule in this step is fixed. You do not need to configure the rule.

#### 3.4.3 My events

On the My event page, you can quickly handle events on the **To be handled by me** and **I**
**participated in** tabs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms** > **Event Center** > **My Events**.
3. On the **To be handled by me** tab, you can view all events that you need to handle,
including the events that you have actively responded to and the events that are transferred to you from other accounts. i. You can filter the desired event data by using the **Event Level** drop-down list above the event list. ii. You can click the title of an event to view the event details. iii. You can perform the following operations on events.

| Operation | Description |
|---|---|

| Close events | After you handle events, you can click Statement to close the events. To close a single event, perform the following operations: a. Find the desired event and click Statement in the Operation column. Alternatively, go to the event details page and click Statement in the upper-right corner. b. Configure parameters in the following figure and click Confirm. To close multiple events, perform the following operations: a. Select the desired events and click Batch order closing below the event list. b. Configure parameters in the following figure and click Confirm. |
|---|---|

| Transfer events | To transfer a single event, perform the following operations: a. Find the desired event and click Transfer in the Operation column. Alternatively, go to the event details page and click Transfer in the upper-right corner. b. Select a value from the Transferred person drop-down list and click Confirm. To transfer multiple events, perform the following operations: a. Select the desired events and click Batch transfer below the event list. b. Select a value from the Transferred person drop-down list and click Confirm. |
|---|---|

4. On the **I participated in** tab, you can view all events that are in the **Processing** or
**Closed** state.
You can filter the event list by **Event Level** and **Processing Status** to obtain the desired events. You can sort the event list by **Event Level**. To obtain event details, find the desired event and click the event title to go to the details page.

## 4 Platform O&M

### 4.1 Apsara Infrastructure Management

**Management**

#### 4.1.1 Resource management

This topic describes modules related to resource management.

**Modules**

| Module | Description |
|---|---|
| Product & Cluster O&M | Displays all resources from the cloud product dimension, including products, clusters, services, and components. |
| Machine Management | Displays all machines. You can also switch to the data center dimension to view all resources on the cloud platform, including data centers, racks, and machines. |
| Resource Tags | Displays resources that you add to favorites and allows you to use resource tags to manage resources in a centralized manner. You can bind, query, unbind, modify, and export resource tags on this page. |
| Base Machine Resource Dashboard | Displays the total amount of static resources and resource usage from the machine and product dimensions. |

##### 4.1.1.1 Product & Cluster O&M

###### 4.1.1.1.1 List view

The list view displays product status and resource statistics by product in a list. The information includes the number of clusters and the hierarchical relationships between products and their related resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Product & Cluster O&M**.
3. In the **Projects** list, view product status and cluster status. Statistics of all products
deployed on Apsara Infrastructure Management or the PaaS base are displayed.

| No. | Section | Description |
|---|---|---|
| 1 | Mode switching section | In this section, you can switch between the list mode and the hierarchy mode. By default, the list mode is used. You can click the icon to switch to the hierarchy mode. This mode displays the hierarchical relationships between products and their related resources. For more information, see Panoramic view. You can click the icon to switch to the list mode. This mode displays product status and statistics by product in a list. The information includes the number of clusters. |
| 2 | Overview section | In this section, you can view the total number of products deployed in the current environment and the number of products in each state. The product state can be Ready or Not Ready. Note A product consists of one or more clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. |
| 3 | List section | In this section, you can view product names, status, instance status, and inspection alerts in a list. You can select a zone to view products and clusters in the zone. You can also perform a quick search for products or clusters. You can select With Inspection Alerts to view products for which inspection alerts are generated. |

The following table describes the parameters in the list.

| Parameter | Description |
|---|---|

| Product | The name of the product. You can click the icon on the left of the product name or clickS how Clusters in the Actions column to view the clusters of the product. You can modify the aliases of clusters for products deployed on Apsara Infrastructure Management and the PaaS base. |
|---|---|
| Status | The state of the product and cluster. You can click the icon next to Status and select Ready or Not Ready to view resources by status. |
| Instance Status | The instance state. A product consists of one or more clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. This column shows the numbers of clusters, service instances, and components in the Ready state of a product, and the corresponding total numbers. You can click an item to view the names and status of resources at all levels. indicates the Ready state. indicates the Not Ready state. Click Cluster, Service, or Component in the Instance Status column to view the cluster composition of the product. Click a cluster name to go to the Cluster Details page. Click a service name or component name to go to the component details page. Note This design facilitates your checks of Not Ready state changes. For example, you fixed a product that is not in the Not Ready state. In this case, you can view whether the product is fixed on the current page without going to the details page. |
| Inspection Alerts | The number of inspection items that the product failed in the last inspection task. - indicates that no inspection task is found. The reason may be no executed inspection task or query failure. 0 indicates that an inspection task is found and the product passed the inspection. Other numbers indicate the number of inspection items that the product failed. You can click the number to view the failed inspection items. |
| Actions | This column provides the Show Clusters operation. The Show Clusters operation provides a further option: Cluster Details. You can click Cluster Details to go to the Cluster Details page. |

###### 4.1.1.1.1.1 Cluster details

You can view cluster details, services in clusters, machines, desired-state configurations, operation records, and resource details.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Product & Cluster O&M**.
3. Go to the cluster details page by using one of the following methods:
In the Projects list, click **Show Clusters** in the Actions column of a product. All clusters of the product are displayed. Find the cluster that you want to view and click **Cluster**
**Details** to go to the cluster details page.
In the Projects list, click the value in the Instance Status column, and then click the name of the cluster that you want to view to go to the cluster details page.
4. View the details of the cluster.

| Section | Description |
|---|---|
| Basic Information | Displays the basic information about the cluster, including the cluster status, product, zone, cluster version, and cluster clone parameters. The aliases of clusters deployed on Apsara Infrastructure Management and the PaaS base can be modified. Note An alias must be 0 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (-), and colons (:). It cannot _ start with a special character or a digit. Click the edit icon next to Cluster clone parameters to specify the clone mode. In the Modify cluster clone parameters dialog box, you can select True clone or FakeClone. Note True clone: When a machine is added to a cluster, the cloning operation is executed. In the desired-state configuration file, the value of Legacy is False. FakeClone: When a machine is added to a cluster, the cloning operation is skipped. In the desired-state configuration file, the value of Legacy is True. |

|   | Rolling updates can be triggered if a cluster is deployed on the PaaS base. Warning The rolling updates are performed on all components of the cluster. The rolling updates will restart the pods of components based on a canary release policy. The rolling feature is typically used to update the service registration variables referenced by a program. You can perform the pre-deletion operation for a cluster deployed on Apsara Infrastructure Management. Warning Cluster deletion is a high-risk operation. Proceed with caution. Consult the GTS Expert support team before you delete a cluster. You need to set a cluster to the pre-deletion state and then delete the cluster. After a cluster is set to the pre-deletion state, the cluster cannot be modified. |
|---|---|
| Details | The details of clusters deployed on Apsara Infrastructure Management and the PaaS base are different, as shown in the following table. |

| Base | Paramete r | Description |
|---|---|---|
|   | Services | Displays the services deployed in the current cluster and the service status. Click Details in the Actions column to go to the component details page and view the component details. Click Upgrade in the Actions column to update a service. You can update a service by modifying the version of the service template. Click Unpublish in the Actions column to remove a service from the current cluster. Warning Service removal is a high-risk operation. Proceed with caution. |
|   | Machines | Displays the list and status of machines that can be used by the current cluster. Click View in the Machine Metrics column to view the machine metric details. Machine monitoring consists of component monitoring, machine monitoring, and system service monitoring. You can repair and restart physical machines. Click Terminal in the Actions column to log on to a machine. Click Details in the Actions column to go to the Machine Details page. |
|   | Machine Group | Displays the planning information between machines and components, such as the role of a machine group, machines contained in the machine group, and components that can use the machine group. Click a machine name in the Associated Machines column to view the machine details. Click a component name in the Associated Components column to view the component details. |
|   | Desired State Configura tion | Displays the desired-state configuration file of the cluster. Note The desired-state configuration files of clusters deployed on Apsara Infrastructure Management can be modified. |
|   |   | Displays the change records of the cluster. Click Task Details in the Actions column to go to the task details page. You can view the task details, including the basic information, related clusters, and changes. The Basic Information section displays the task status, submission time, and submitter. |

|   | Guide·Platform | O& |
|---|---|---|
|   |   | The Related Clusters section displays the cluster, product, status, progress, version, submission time, and operations that can be performed. You can click Build Details or Resource Task Details in the Actions column to view the build details or resource task details. The Change Content section consists of Component Changes and Machine Changes. On the Component Changes tab, you can terminate, retry, or suspend a task. Click Details in the Actions column to view the task progress of a component. Overview Information: displays the basic information about the component, including Commit Id, Rolling Status, Approval Policy, and Upgrade Plan. In the upper-right corner of the dialog box, click View Details to go to the Rolling Summary page and view the component update details. Go to the Rolling Summary page. In the Overview Information section, you can click Retry, Terminate, or Suspend to retry, terminate, or suspend a task. You can perform the operations only on unfinished tasks. The system can monitor and display the Service Level Agreement (SLA) changes. You can view the real-time monitoring status of components. Click View Logs to view SLA monitoring logs. Click Modify SLA Configuration to modify the SLA configuration. Note You can view the SLA-related content of services for which the SLA feature is enabled. Click View All to view the component update details. Click Edit Parameter to modify the relevant parameters. Only the parameters for unfinished tasks can be modified. In the Instance Details section, you can add multiple component tasks to the blacklist. Instance Details: displays information such as the change status of component instances, component actions, and metrics. On the Machine Changes tab, you can view the machine name, change type, and status. Click Terminal in the Actions column to go to the logon page and log on to a machine. Click Details in the Actions column to go to the Machine Overview page and view the machine details. Note The Machine Changes tab is displayed only when the value in the Change Type column is Machine Scale-out, Machine Scale- In, Component Scale-out, or Component Unpublishing. |
| Apsara Infrastr ucture Manag ement |   |   |

|   | Action History | Go to the Machine Overview page, which consists of the Basic Information and Details sections. Basic Information: displays information such as the change status, machine status, machine actions, clusters, and machine metrics. Details: consists of Add to Cluster, Clone, and Deploy Component Instances. Add to Cluster: displays the cluster where the machine resides and the cluster to which you want to add the machine, as shown in the preceding figure. Status: the state of the machine change. Valid values: Failed: The change failed. Cancel: The change task is canceled. For example, the machine scale-in task is submitted when the machine scale-out task is not complete. Doing: The change is in progress. Waiting: The change is waiting to be performed. Done: The change is complete. Current Cluster: the cluster where the machine resides. Destination Cluster: the cluster to which you want to add the machine. Clone: indicates whether the cloning operation is executed when a machine is added to a cluster. The Real Clone and Pseudo-clone modes are provided. Pseudo-clone: The cloning operation is skipped when a machine is added to a cluster. Real Clone: The cloning operation is executed when a machine is added to a cluster. Click Metric. In the dialog box that appears, view the metric details on the Component Metrics, Machine Metrics, and System Service Metrics tabs. Status: For more information, see the status in the Add to Cluster section. System Service: the server role that is relevant to the cloning operation. Current Version: the current version of the server role on |
|---|---|---|
|   |   | the machine. Desired Version: the version of the server role that you want to update to. |

|   |   | Deploy Component Instances: displays the component instances that are deployed on a machine after the machine is added to a cluster. Component: the name of the component. Service: the service to which the component belongs. Status: For more information, see the status in the Add to Cluster section. Click Details in the Status column to view the deployment status of a component. Click View in the Metric column. In the Metric Details dialog box that appears, view the metric details on the Component Metrics, Machine Metrics, and System Service Metrics tabs. Version Current: the current version of the server role on the machine. Desired: the version of the server role that you want to update to. Click Version Differences in the Actions column to go to the Version Differences page and view the differences between configuration files of different versions. |
|---|---|---|
|   | Resource Details | Displays the resources requested by components in the cluster. Click Related Version in the Actions column to view the related resource versions. |
|   | Test Report | Displays the test reports of services in the cluster. Click Details in the Actions column to view the details of failed cases, succeeded cases, and skipped cases. |
|   | Services | Displays the services deployed in the current cluster and the service status. Click Details in the Actions column to go to the component details page and view the component details. Click Rolling in the Actions column to perform a rolling update. |
|   | Desired State Configura tion | Displays the desired-state configuration file of the cluster. |

| PaaS | Action History | Displays the change records of the cluster. Click Task Details in the Actions column to view the task details. The Base Info section displays the basic information such as task status, task ID, task message, and start time. The Subtask List section displays the information such as subtask ID, description, status, change object, and execution method. Click Show Parameters in the Actions column to view the task parameters. Click Yaml in the Actions column to view the configuration file. Note Cluster changes mainly refer to the desired state changes, excluding machine operations such as machine repairs in the cluster. |
|---|---|---|
|   | Resource Details | Displays the resources requested by components in the cluster. |

###### 4.1.1.1.1.2 Component details

You can view the basic information and details of components.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Product & Cluster O&M**.
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

|   | Instances | Displays the status of the components deployed on the machine, including the version alignment, action in progress, and machine status. Note Version misalignment indicates that the current version is inconsistent with the version set in the desired-state configuration file. This occurs when the version is being updated, fails to be updated, or is to be updated. In the last case, the version specified in the desired-state configuration file is changed, but the component has not been updated. Click Diagnose in the Actions column. Apsara Infrastructure Management diagnoses the causes for version misalignment or the status not being Good. Note Diagnose is displayed only when version misalignment occurs or the value of Status is not Good. Choose Component Information > Metrics in the Actions column to view the details of component monitoring, machine monitoring, and system service monitoring. Choose Component Information > Applications in the Actions column to view the applications and application versions of the component deployed on the machine. Note tianji config is an application that indicates the _ _ configuration file delivered to the machine. The version of tianji config can be used as the version _ _ number of the configuration file. If the configuration file changes, the version number changes. Other applications are user programs. Choose Component Information > Status Details in the Actions column to view the detailed status of the component, such as the status description. Click Terminal in the Actions column to go to thel ogon page and log on to the machine. Choose Actions > Restart in the Actions column to restart the application processes of the component. |
|---|---|---|
|   | Change History | Displays the change tasks related to the component. Click Details in the Actions column to go to the Task Details page and view the task details. |
|   | Desired State Configurat ion | Displays the desired-state configurations of the component, including the specialized files. You can modify the desired-state configurations of the component. |

| Apsa ra Infra struc ture Mana gem ent |   |   |
|---|---|---|
|   | Registrati on Variables | Displays the registration variables of the component. The variables can be used by other components, such as the endpoint of a program. |
|   | Resources | Displays the information about the resources requested by the component. Click Related Version in the Actions column to view the related versions of the resource. |
|   | Dependen cy Status | Displays the dependencies of the components. A component depends on the component or components on its right. The following figure shows the component dependencies by using arrowed lines. Display Mode: supports All Components and Not Ready Components. All Components: displays all components in the dependency tree. Not Ready Components: displays the nodes that do not reach the desired state and their leaf nodes in the dependency tree. If all nodes reach the desired state, only the direct dependencies of the root node are displayed. Display Dependency: supports Strongly Dependent and Weakly Dependent. Strongly Dependent: If the dependencies are not ready, the current component cannot be started. Weakly Dependent: If the dependencies are not ready, the current component is still started. However, some features may be affected. |

| PaaS | Workload | Displays the basic workload information about the component. For Deployments, StatefulSets, and DaemonSets workloads, the page displays information about the pods requested by the workloads, and you can log on to the containers deployed on the pods. Click View YAML in the Actions column to view the original configuration and running information about the workload. Click the icon to show the pod list. You can view the key information about each pod in the cluster, including the status, name, container, node name, and namespace. Click Pod Performance Data in the Actions column to view the pod performance data. Click Describe in the Actions column to view the configurations, status, and properties of the pod. Click Terminal in the Actions column to go to the logon page and log on to the machine. Click View Logs in the Actions column to view the logs exported from containers deployed in the pod to stdout. |
|---|---|---|
|   | Instances | Displays the pods requested by the workload and the status of Kubernetes nodes. Click Terminal in the Actions column to log on to the machine. |
|   | Desired State Configurat ion | Displays the desired-state configurations of the component. |
|   | Registrati on Variables | Displays the registration variables of the component. The variables can be used by other components, such as the endpoint of a program. |
|   | Resources | Displays the information about the resources requested by the component. |
|   | Dependen cy Status | Displays the dependency data of the component on other components. The Dependency Status module is the same as that of Apsara Infrastructure Management. |

###### 4.1.1.1.2 Panoramic view

The panoramic view displays product status and resource statistics by product in a hierarchy. The information includes the relationships between products and related resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Product & Cluster O&M**.
3. Click the
icon to switch to the panoramic view. The panorama view displays all cloud products deployed in Apsara Stack. You must focus on the abnormal products whose icon is orange. These products may not reach the final state (ready state) or have unhandled P1 and P2 alerts.

| No. | Section | Description |
|---|---|---|

| 1 | Mode switching section | In this section, you can switch between the list mode and the hierarchy mode. By default, the list mode is used. Click the icon to switch to the hierarchy mode. This mode displays the hierarchical relationships between products and their related resources. Click the icon to switch to the list mode. This mode displays product status and statistics by product in a list. The information includes the number of clusters. |
|---|---|---|
| 2 | Overview section | In this section, you can view the total number of products deployed in the current environment and the number of products in each state. The product state can be Normal or Exception. |
| 3 | Hierarchy section | The hierarchy consists of four layers. The layer at the top shows products on the cloud management platforms, monitoring products, disaster recovery and backup products, and others. These products are displayed above the titles of Uni-manager/Cloud management, Disaster recovery, Monitoring operation, and Others. Other products refer to products that fail to fall into the preceding categories. The next layer shows PaaS products, including middleware, big data, database, application services, Internet of Things (IoT) products. The next layer shows IaaS products, including elastic computing, network, storage, and security products. The layer at the bottom shows infrastructure, including common components that enable other cloud products. Note The icon of normal products is displayed in blue. The icon of abnormal products is displayed in orange. Click an icon or move the pointer over an icon. The system displays the product name, status, alerts, exceptions, and dependencies. Note Click an icon or move the pointer over an icon. Products connected by orange lines are the ones on which the current product depends. Click an icon or move the pointer over an icon. Products connected by gray lines are affected by the current product. Click Details in the pop-up window that appears to go to the Cloud Product Details page. For more information, see the following table. |

4. Click Details in the upper-right corner of the pop-up window for a product to go to the Cloud
Product Details page. The following section describes the topologies of products deployed on Apsara Infrastructure Management and the PaaS base: For products deployed on Apsara Infrastructure Management, the hierarchy of the topology consists of the following levels: product, cluster, service, component, and instance. For products deployed on the PaaS base, the hierarchy of the topology consists of the following levels: product, cluster, service, and component.

| No. | Section | Description |
|---|---|---|
| 1 | Overview section of product relationship | In this section, you can view the product relationships. You can view the current cloud product and cloud products with dependency exceptions. Click a product name next to Dependency exception cloud products to go to the product details page and view the topology of the product. |
| 2 | Overview section | In this section, you can view the total number of products and the number of products in each state. The product state can be Normal or Exception. |
| 3 | Search section | Select Show only status exception objects. The topology displays only abnormal clusters, components, services, and instances. If you clear this check box, all nodes are displayed in the topology. The drop-down list displays the hierarchical relationship among clusters, services, components, and instances. Click a name. The system locates the node in the topology and highlights the node card. |

| 4 | Topology section | The hierarchical relationship among products, clusters, services, components, and instances is displayed in a topology and each node is displayed as a card. Move the pointer over or click a node card. The system displays the node status, including alerts, details, and logon link. Move the pointer over a product card and click the icon next to Alert if alerts exist. You are redirected to the Monitor&Alarms > Alerts > Alerts page in the Apsara Uni-manager Operations Console. Move the pointer over an instance card and click the icon next to Node status or Instance status to go to the Machine Details page or component details page to view the corresponding details. Click Details of the node that you want to manage to go to the corresponding cluster details page or component details page. Click Terminal of the node that you want to managet o go to the machine logon page. Note A product consists of one or more clusters, service instances, and components, and the product status information is aggregated level by level from components to service instances and then to clusters. |
|---|---|---|

##### 4.1.1.2 Machines

###### 4.1.1.2.1 List view

In a list view, you can view the basic information about machines and the information about components deployed on machines.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Machine Management**.
3. Click the
icon to view the topology of machines in a data center. For more information, see Topology view.
4. The Machines page displays all physical machines and virtual machines (VMs) managed by
Apsara Infrastructure Management. Click **Advanced Filter** and specify Hostname/IP, Status, Product, and Cluster. The system filters machines that meet the filter conditions. Optional. Click **Publish/Unpublish**. On the page that appears, you can deploy or remove a machine. Deploy a machine a. Click the **Machine Publishing** tab. b. Select a product and bucket from the **Product** and **Bucket** drop-down lists. c. Click **Download Schema** to download the machine_list.xlsx file. Enter the machine information based on the requirements in the file.

> **Note:** nodename, Sn, and Ip are mandatory fields.

d. Click **Select File**. The **Upload Schema** dialog box appears. e. Click **Upload and Parse File** to upload the machine_list.xlsx file. f. After the file is parsed, click **Import**. View the information about the machine on the
**Machine Publishing** page, including the hostname, IP address, serial number (SN),
and status. Click **Clear** in the Actions column of the machine that you want to manage to remove the machine from the machine list on the page. Click **Details** in the Actions column of the machine that you want to manage to view the details of the machine, such as the data center, rack, and room where the machine resides. g. Click **Batch Publish** in the lower-right corner of the page. Remove a machine a. Click the **Machine Unpublishing** tab. b. In the **Machines** field, enter the hostname or IP address of the machine that you want to remove. The information about the machine is displayed on the right side of the page. Find the machine that you want to remove and click **Clear** in the Actions column. c. Click **Batch Unpublish** in the lower-right corner of the page. Select **Hostname/IP**, **Status**, **Product**, or **Cluster** from the drop-down list, and enter the corresponding value in the text box to filter the machines that you want to manage.

| Parameter | Description |
|---|---|
| Hostname/IP | The hostname and IP address of the machine. |

| Status | The state of the machine. Valid values: Status Abnormal: The state of the machine displayed on Apsara Infrastructure Management is not Good. Ping Failed and No Heartbeat issues are excluded. Ping Failed: The machine cannot be pinged from services managed by Apsara Infrastructure Management. No Heartbeat: The machine cannot report heartbeats to services managed by Apsara Infrastructure Management. Scaling In: The machine is being removed from a cluster. Scaling Out: The machine is being added to a cluster. Repairing: An O&M operation is being performed on the machine, such as machine repair. Normal: The machine works as expected. No O&M operations are performed on the machine, and the state of the machine displayed on Apsara Infrastructure Management is Good. |
|---|---|
| Cluster/Prod uct | The cluster and product to which the machine belongs. |
| Machine Metrics | Click the state of the machine that you want to manage in the Machine Metrics column. In the Metric Details dialog box that appears, view the details of component metrics, machine metrics, and system service metrics. |
| Actions | Click Terminal in the Actions column of the machine that you want to manage to go to the logon page and log on to the machine to perform related operations. You can also select multiple machines and click Batch Terminal in the lower-left corner of the page. Click Machine Status Dashboard in the Actions column to go to the Machine Status Panel page. You can view the machine information, service processes, and application details. Click Details in the Actions column to go to theM achine Details page. |

###### 4.1.1.2.1.1 Machine details

You can view the basic information about machines and the components deployed on the machines.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Machine Management**.
3. On the Machines page, select a machine and click **Details** in the Actions column.
4. On the **Machine Details** page, view the basic information about the machine and the
components deployed on the machine. The left-side area displays data centers, racks and rooms, physical machines, and virtual machines (VMs) hierarchically. If you select a data center, rack or room, physical machine, or VM, the right-side area displays the corresponding details. The information can be displayed based on machine names and machine aliases. You can filter information by machine name and machine alias.

| Level | Description |
|---|---|
| Data center | The upper-right section displays the name of the data center, the number of racks in the data center, the number of machines (including physical machines and VMs), and the number of abnormal machines (including physical machines and VMs). Click the All Machines or Abnormal Machine tab to view the Product Distribution and Model Distribution information about the data center. |
| Rack and room | The upper-right section displays the name of the rack, the name of the room, the number of machines (including physical machines and VMs), and the number of abnormal machines (including physical machines and VMs). Click the All Machines or Abnormal Machine tab to view the Product Distribution and Model Distribution information about the rack. |

|   | The upper-right section displays the basic information about the physical machine or VM, including the IP address, status, machine action, cluster, data center, serial number (SN), model, Kubernetes node status (if the machine is a Kubernetes node, the node status is displayed), and host (if the machine is a VM, the host is displayed). You can modify the alias and SN of the host. Click Terminal on the right side of the machine name to go to thel ogon page and log on to the machine. Click Machine Status Dashboard on the right side of the machine name to view the machine information, service processes, and application details. Click Machine Metrics on the right side of the machine name to go to the CloudMonitor platform and view the machine monitoring data. This operation is unavailable for VMs. Select Restart, Power Off and Repair, or Repair and Clone from the Machine Management drop-down list on the right side of the machine name. This operation is available only for physical machines. For more information about the steps, see the Machine management section of this topic. Warning Out-of-band restart and machine repairs, including Power Off and Repair and Repair and Clone, are high-risk operations. |
|---|---|
| Physical machines/VMs | Consult the expert team before you perform these operations. Click Refresh on the right side of the machine name to refresh the current page. Click Export on the right side of the machine name. The basic information about the machine is exported to a file in the XLSX format and can be downloaded to your computer by using a browser. Click Details next to Cluster to go to the Cluster Details page and view the cluster details. Click Details next to Model to view the basic information, location information, and hardware information about the machine. The Hardware Information section displays information such as hard disk, memory, CPU, CPU architecture, and CPU manufacturer. Click Details next to Kubernetes Node Status to view the details of the node status, including the basic information, operating system, Kubelet, and resource usage. This operation is available only when the machine is a Kubernetes node. Click the Components, VM, Taints, and Labels tabs in the lower-right section to view the details. |

|   | Components: displays components deployed on the machine, including the component status, actions, and metrics. Click View in the Component Metrics column of the component that you want to manage to view the information about component monitoring, machine monitoring, and system service monitoring. Click Restart in the Actions column of the component that you want to manage to restart the component. Click Details in the Actions column of the component that you want to manage to go to the component details page and view the component information. Note If the machine is a Kubernetes node, pods that run the components deployed on the PaaS base are displayed. You can restart the processes of components that are deployed on Apsara Infrastructure Management. VM: displays the started VMs deployed on the host. VMs are displayed only when the machine is a host. Taints: displays the taint information about the Kubernetes node. You can add and delete taints. The taint information is displayed only when the machine is a Kubernetes node. Click the Taints tab. Click the + icon in the upper-right corner of the tab. In theC reate Taint dialog box that appears, enter the custom taint key and value, select a taint effect, and then click OK. PreferNoSchedule: Kubernetes avoids scheduling pods that do not tolerate this taint to the node. NoSchedule: Pods that do not tolerate this taint are not scheduled to the node. NoExecute: Pods that do not tolerate this taint are evicted from the node if they are already running on the node, and are not scheduled to the node if they are not yet running on the node. Find the taint that you want to manage and clickD elete in the Actions column. |
|---|---|

|   | Labels: displays the labels of Kubernetes nodes. You can add or delete labels. The label information is displayed only when the machine is a Kubernetes node. |
|---|---|

Click the **Labels** tab.

**Machine management**

Click the + icon in the upper-right corner of the tab. In the **Create**
**Label** dialog box that appears, enter the custom label key and
On the Machine Details page, click **Machine Management** in the upper-right corner of the value and click **OK**. basic information section. The management operations include **Restart**, **Repair and Clone**, Find the label that you want to manage and click **Delete** in the and **Power Off and Repair**.
**Actions** column.

| Operation | Procedure |
|---|---|
| Restart | In the upper-right corner of the page, choose Machine Management > Restart. In the message that appears, click OK. |
| Repair and Clone | Note You can click Repair and Clone or Power Off and Repair based on your business requirements. Click Repair and Clone for machines that must be cloned before the operating system is reinstalled, such as the system disk. Click Power Off and Repair for machines that can be repaired without cloning, such as the memory. 1. In the upper-right corner of the page, choose Machine Management > Repair and Clone or Power Off and Repair. 2. In the dialog box that appears, enter REPAIR and click OK. 3. Click Repair Details next to Status to go to the Machine Repair page. 4. Perform the precheck. In the Pre-check step, click Execute Pre-check in the upper-right corner and click OK. The system automatically performs a precheck to ensure that the machine repair can be executed in a secure manner. Note If the precheck fails, click Retry in the upper-right corner to try again. 5. Approve the repair. i. After the precheck is complete, click Enter Approval Phase in the lower-right corner of the page. In the message that appears, click OK. ii. In the Approve step, view the components that need to be approved and click Approve in the Actions column. |

| Power Off and Repair | iii. In the dialog box that appears, enter APPROVED and click OK. Important Then, Action Status is changed from pending to approved. After Action Status is changed to approved, the action that you specified is automatically executed. Manually setting Action Status to approved instead of using the Decider program is a high-risk operation. Data loss may occur. You must contact technical support for confirmation. 6. Repair the machine. i. After the repair is approved, click Start Repair in the lower-right corner of the page. In the message that appears, click OK. ii. On the page that appears, machine information such as the name, IP, and SN of the machine and the project to which the machine belongs is displayed. The maintenance personnel can repair the machine offline based on your business requirements. 7. Perform the post-check. i. After the machine is repaired, click Go to Post-check in the lower-right corner of the page. In the message that appears, click OK. ii. In the Post-check step, click Execute Post-check in the upper-right corner. In the message that appears, click OK. |
|---|---|
|   | Note If the post-check fails, click Retry in the upper-right corner to try again. iii. After the post-check is complete, click Complete Repair in the lower-right corner of the page. iv. In the dialog box that appears, enter FINISHREPAIR and click OK. The machine is repaired. |

###### 4.1.1.2.2 Topology view

The topology displayed on the Data center dimension page helps you understand the topological relationships among the network devices, racks, and physical machines in a data center.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Machine Management**.
3. Click the
icon to switch to the data center dimension. The topology displays the topological relationships among the network devices, racks, and physical machines in a data center. Network devices include ISW, LSW, CSW, DSW, and ASW. Physical machines refer to hosts. You can move the pointer over a physical machine icon and click Details in the pop-up message to view the Docker virtual machines (VMs) and could product components that run on the machine.

| No. | Section | Description |
|---|---|---|
| 1 | Mode switching section | In this section, you can switch between the list mode and the hierarchy mode to view machine information. By default, the list mode is used. Click the icon to switch to the hierarchy mode. This mode displays the topological relationships among network devices, racks, and physical machines in a data center. Click the icon to switch to the list mode. This mode displays the status and clusters of all physical machines and VMs that are managed. |
| 2 | Overview section | In this section, you can view the number of abnormal network devices and physical machines. The number of abnormal devices and the total number of devices are displayed under the name of each device type. The left side indicates the number of abnormal devices and the right side indicates the total number of devices. |
| 3 | Exception statistics section | In this section, you can view the number of abnormal network devices and physical machines in a data center. The number of abnormal devices and the total number of devices are displayed next to the name of each device type. The left side indicates the number of abnormal devices and the right side indicates the total number of devices. |

| 4 | Search section | If you select Only exception servers and their associated nodes are displayed, the topology shows abnormal nodes, including racks and machines. If you clear this check box, all abnormal and normal nodes are displayed. The drop-down list displays the hierarchical relationships among machines, racks, physical machines, and network devices. Select a name from the drop-down list. The system locates the corresponding node in the topology and highlights the node card. |
|---|---|---|
| 5 | Topology section | You can fold or unfold different hardware groups. By default, the hardware groups at the top are automatically unfolded. If a group is folded, the system displays the number of abnormal devices and the total number of devices in the card format. The machine details are not displayed when you move the pointer over a card. If a group is unfolded, the system displays the devices and machines in the icon format. Move the pointer over an icon. In the pop-up message that appears, the system displays the machine details, including the location and cluster. Click Details in the pop-up message of a network device to go to the Network Operations Console. On the page that appears, choose Basic Network > Network Element. Then, click the Device Management tab to view the machine details. Click Details in the pop-up message of a machine to go to the Machine Details page. Click Terminal in the pop-up message of a machine to go to the machine logon page. Note Blue icons indicate normal nodes. Orange icons indicate abnormal nodes. If the connection between two nodes is gray, the device link is normal. If the connection between two nodes is orange, exceptions occur. The connection between aggregation nodes is a dashed line. |

##### 4.1.1.3 Resource tags

The Resource Tags module allows you to use tags to view and manage resources that you care about in a centralized manner.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Resource Tags**.
3. Perform the following operations that are relevant to the My attention module:
Choose **Platform Operation > Apsara Infrastructure Management > Resources**. In the left-side navigation pane of the page that appears, choose **Resources > Machine**
**Management**. On the Machines page, click Details in the Actions column to go to the
Machine Details page. Then, click **Add to Favorites** in the upper-right corner of the page. Go to the Resource tag page and view the node that you add to favorites in the My attention module. Click the node to go to the Machine Details page.
4. Perform the following operations that are relevant to the Resource List module.
The following table describes the relevant operations.

| Operation | Description |
|---|---|
| View resource tags | You can view the list of resources to which tags are bound. You can also search for resources and tags by Resource Name, Resource type, or Tag. |

| Bind tags to resources | You can bind tags to resources based on your business requirements. Select the resource that you want to manage and clickB ind tags. Select tags. You can add, delete, and batch delete tags. Select a resource from the Product View tab or the Data Center View tab. You can select multiple resources. Click Completed to complete the tag binding. |
|---|---|
| Unbind tags from resources | You can unbind tags from resources based on your business requirements. Select the resource that you want to manage and click Unbind tags. In the message that appears, click OK. |
| Modify resource tags | You can delete resource tags that are no longer required. Click Modify tags in the Operation column of the resource that you want to manage. In the dialog box that appears, click the icon next to the tag that you want to delete, and click OK. |
| Export resource tags | You can export all resource tags in the list. ClickE xport. In the dialog box that appears, select a download URL and click Download. Note If you want to export only some of the resource tags, select the resource tags that you want to export and click Export. In the dialog box that appears, select a download URL and click Download. |

##### 4.1.1.4 Base machine resource dashboard

The dashboard displays the resource allocation information from the machine and product dimensions. Resources include CPU, memory, GPU, local dedicated disk, and local shared disk resources. You can view the resource allocation details of a specified machine or product.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**. In the left-side navigation pane of the page that appears,
choose **Resources > Base Machine Resource Dashboard**. By default, the page displays resource allocation from the machine dimension. You can click the icon in the upper part of the page to switch to the product dimension.
3. (Optional) Find the machine that you want to view.
In the **Machines** section, select Machine, Labels, or Taints from the drop-down list and enter a corresponding value in the search box to filter the machine that you want to manage. You can also click **Advanced Filter** and specify Machine, Labels, or Taints to filter the machine that you want to manage.
4. The **Machines** list displays the machine resource information, including Allocated CPU,
Allocated Memory, and Allocated GPU.

| Parameter | description | Example |
|---|---|---|
| Machine | The name and IP address of the machine. | e21j10005.cloud.j10.amtest 98 10.98.2.9 |
| Allocated CPU | The percentage of allocated CPU resources to total available CPU resources, amount of available resources, amount of allocated resources, and overcommit ratio. The overcommit ratio is a parameter specified in advance. The actual amount of resources that can be allocated is equal to the amount of allocatable resources multiplied by the overcommit ratio. | 29.54% 1343/396.7 Cores (Overcommitted 1400%) |
| Allocated Memory | The percentage of allocated memory resources to total available memory resources, amount of available resources, amount of allocated resources, and overcommit ratio. The overcommit ratio is a parameter specified in advance. The actual amount of resources that can be allocated is equal to the amount of allocatable resources multiplied by the overcommit ratio. | 77.6% 828.1/642.6 GiB (Overcommitted 220%) |
| Allocated GPU | The percentage of allocated GPU resources to total available GPU resources, amount of allocated resources, and amount of available resources. - indicates that the machine does not have GPU resources. | 50% 1/2 |

| Yoda Disk | The percentage of allocated local dedicated disk space to total available local dedicated disk space, amount of available space, and amount of allocated space. The total amount of available space refers to the space of all local dedicated disks for the machine. Note Yoda Disk is a kind of local dedicated disk. | 26.84% 43.7/11.7 TiB |
|---|---|---|
| Yoda LVM | The percentage of allocated local shared disk space to total available local shared disk space, amount of available space, and amount of allocated space. The total amount of available space refers to the space of all local shared disks for the machine. Note Yoda LVM is a kind of local shared disk. | 11.7% 1.3/0.2 TiB |
| Labels | The labels added to the machine. By default, the number of existing labels for the machine is displayed. Move the pointer over the number of labels to view all the labels of the machine. | Labels: 34 |
| Taints | The taints added to the machine. By default, the number of existing taints for the machine is displayed. Move the pointer over the number of taints to view all the taints of the machine. | Taints: 1 |
| Total Pods | The pods that are scheduled to the node. By default, the number of pods is displayed. Find the machine that you want to manage and click the number in the Total Pods column to view the pod details. In the dialog box that appears, the pods are sorted by product and application name. | 31 |
| Actions | Click Resource Details to go to the Resource Information page. The page displays the distribution of CPU, memory, GPU, and Yoda Lvm resources and the planning of Yoda Disk resources in charts. Click Machine Details to go to the Machine Details page and view the machine details. |   |

#### 4.1.2 Kubernetes cluster management

This topic describes the basic information about Kubernetes clusters and nodes and the resource usage of clusters and nodes.

**Modules**

| Module | Description |
|---|---|
| Cluster Overview | Displays the Kubernetes clusters created and managed by Apsara Infrastructure Management and the resource usage of clusters. |
| Node Management | Displays all Kubernetes nodes managed by Apsara Infrastructure Management. |

##### 4.1.2.1 Cluster overview

You can view the resource usage of O&M Kubernetes clusters, including CPU utilization, memory usage, pod usage, and storage usage of the logical volumes. O&M Kubernetes clusters are the Kubernetes clusters that are created and managed by Apsara Infrastructure Management.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Kubernetes Cluster Management**. In the left-side navigation pane of
the page that appears, choose **Kubernetes Cluster Management > Cluster Overview**.
3. On the **Kubernetes Cluster Overview** page, view the basic information, resource usage,
and nodes of a cluster.

| GUI element | Description |
|---|---|
| Kubernetes Cluster Overview | Displays the Kubernetes version, registration time, CPU, and memory of the cluster. In the upper-right corner of the page, switch clusters by selecting the clusters from the drop-down list. |

| Cluster Resource Usage | Displays the CPU utilization, memory usage, pod usage, and storage usage of the logical volume for the cluster. The resource usage data includes the used resources, total available resources, unit, and usage percentage. |
|---|---|
| Nodes | Displays the node details of the cluster. Click Advanced Filter to filter nodes by Name, Label, Taint, or Role. Click Terminal in the Actions column of the node that you want to manage to log on to the machine. Click Machine Status Dashboard in the Actions column of the node that you want to manage to view the machine information, service processes, and application details. Click Node Performance Data in the Actions column of the node that you want to manage to view the performance data of the node. Click Details in the Actions column of the node that you want to manage to go to the Machine Details page and view the details. |

##### 4.1.2.2 Node management

You can view the basic information about nodes deployed on the platform, including the node name, status, IP address, role, resource usage, labels, and taints. You can also view node performance data, log on to a node, jump to the Machine Status Panel page, and view machine details.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Kubernetes Cluster Management**. In the left-side navigation pane of
the page that appears, choose **Kubernetes Cluster Management > Node**
**Management**.
3. On the **Kubernetes Nodes** page, view the information about Kubernetes nodes, including
the number of nodes of each type and the name, IP address, status, role, number of labels, number of taints, and resource usage of each node.
4. (Optional) In the search box above the node list, search for the node that you want to view.
5. View the node information. The following table describes the parameters.

| Parameter | Description |
|---|---|

| Name/IP Address | The name and IP address of the node. |
|---|---|
| Status | The state of the node. Valid values: Ready, Not Ready, and Unknown. You can filter machines by Status. |
| Role | The business role of the node. For example, master indicates the primary node and redis1 indicates Node 1 where the Redis service is deployed. |
| Label/Taint | The number of existing labels and taints for the node. The labels and taints determine whether programs can be deployed on the node. |
| Allocated CPU | The percentage of the consumed CPUs to the total CPUs that can be allocated. |
| Allocated Memory | The percentage of the memory usage to the total memory that can be allocated. |
| Local Shared Storage | The percentage of the used storage capacity to the total storage capacity that can be allocated in shared disk resources. |
| Actions | Click Terminal to log on to the machine and perform operations. You can also select multiple machines and click Batch Terminal in the lower-left corner of the page. Click Machine Status Dashboard to go to the Machine Status Panel page. You can view the basic machine information, disk usage, service processes deployed on the machine, and application details. Click Node Performance Data to go to the Grafana dashboard page and view the resource usage information about the node, such as CPU utilization. Click Details to go to the Machine Details page. |

#### 4.1.3 Hardware O&M

This topic describes how to repair hard disk drives (HDDs) and query machine repair records.

**Modules**

| Module | Description |
|---|---|

| HDD Repairs | You can efficiently and securely complete the entire process of data disk replacement. Preparation: After you initiate an HDD replacement task, you must make preparations for the task, including task reporting, task approving, and HDD unmounting. Repair: After the preparation for HDD replacement is complete, you can start the repair work, including HDD replacement, HDD installation, and inspection. History: You can view all records about HDD repairs, including related machines, HDDs, and repair results. |
|---|---|
| Machine Repair | You can query machine repair records. |

##### 4.1.3.1 HDD repairs

The HDD repair feature allows you to replace data disks. If a fault occurs in a data disk, the system confirms the status of the disk, uninstalls the disk, and then confirms that the business is not affected before performing subsequent operations. After the disk is replaced, the system formats, mounts, and restores the disk to provide the storage capacity.

**Modules**

| Module | Description |
|---|---|
| Preparation | After you initiate a disk replacement task, you must make preparations for it, including task reporting, task approving, and disk unmounting. |
| Repair | After you complete the preparations that are required to replace a disk, you can replace the disk and perform a health check on the new disk. |
| History | You can view a list of all repair records to learn repaired machines and HDDs, and repair results. |

###### 4.1.3.1.1 Preparation

After you initiate a disk replacement task, you must make preparations for it, including task reporting, task approving, and disk unmounting.

**Prerequisites**

If you want to use the disk replacement feature to replace a disk online, the following conditions must be met: The disk is a data disk that is used by Apsara Distributed File System and provides storage capabilities to users. No other files are stored on the disk. Cloud services that support disk replacement, such as Apsara Infrastructure Management, Elastic Compute Service (ECS), and ODPS, are deployed on the machine in which the disk resides. The disk is marked as abnormal in Apsara Distributed File System. The system checks and confirms whether the preceding conditions are met during the maintenance. If the preceding conditions are not met, the disk replacement is not triggered or errors are reported during the precheck.

**Background information**

If you ignore the error messages and forcibly replace the disk, data loss may occur. You can use the disk replacement feature to handle only damaged disks that are reported by Apsara Distributed File System. You can use the disk replacement feature to replace only damaged data disks. If you do not replace the disks with new disks, the maintenance process is interrupted. The data disks of Apsara Infrastructure Management, ODPS, Object Storage Service (OSS), and Simple Log Service can be repaired.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. In the left-side navigation pane of the page that
appears, choose **Hardware O&M > HDD Repairs**. By default, the **Preparation** tab appears. You can query disk replacement tasks by progress or machine name.
3. Perform operations based on the task status in different phases.
The preparation process is divided into the following phases: Report, Approval, and Unmounting. The task can be in one of the following states in each of the three phases: not started (displayed in gray), in progress (displayed in blue), completed (displayed in green), and failed (displayed in red). The following table lists the corresponding operations that can be performed in these states.

| Report | Approval | Unmounting | Available operation |
|---|---|---|---|
| In progress | Not started | Not started | Cancel the task |
| Completed | Not started | Not started | Start to repair the disk and cancel the task |
| Failed | Not started | Not started | Cancel the task |
| Completed | In progress | Not started | Select manual approval by clicking Approval Details |
| Completed | Completed | In progress | None |
| Completed | Completed | Disk unmounting completed but silence period not ended | None |

| Completed | Completed | Disk unmounting completed and silence period ended | Prepare to replace the disk |
|---|---|---|---|

Related operations: Cancel the disk replacement task: Click **Cancel**. In the message that appears, click **OK**. Start to repair the disk: Click **Start Repair**: If a QR code is required for approval, the system pops up the QR code. You can use the DingTalk mini program ASLM Mobile to scan the QR code to obtain the authorization code. Then, enter the authorization code. The system proceeds to the next step after the verification is passed. If a QR code is not required for approval, click **OK** in the dialog box that appears to start to repair the disk. After that, the software enters the automatic approval phase. Manually approve a disk replacement task: If **Approval Details** is displayed in the
**Actions** column, click **Approval Details**. In the dialog box that appears, click **Approval**
in the **actions** column of the service role that you want to manage. In the dialog box that appears, enter **APPROVED** in the Enter APPROVED to confirm your operation field. Then, click **OK**.

> **Important:** Before approval, make sure that business data on the disk is backed up.

Prepare for disk replacement: Click **Prepare for Replacement**. The disk replacement task enters the repair phase and is displayed on the **Repair** tab. The time period displayed under **Unmounting** is the silence period. You can change the disk only if the value is larger than 7 days.

###### 4.1.3.1.2 Repair

After you complete the preparations that are required to replace a disk, you can replace the disk and perform a health check on the new disk.

**Prerequisites**

If you want to use the disk replacement feature to replace a disk online, the following conditions must be met: The disk is a data disk that is used by Apsara Distributed File System and provides storage capabilities to users. No other files are stored on the disk. Cloud services that support disk replacement, such as Apsara Infrastructure Management, Elastic Compute Service (ECS), and ODPS, are deployed on the machine in which the disk resides. The disk is marked as abnormal in Apsara Distributed File System. The preparations that are required to replace the disk are complete. The system checks and confirms whether the preceding conditions are met during the maintenance. If the preceding conditions are not met, the disk replacement is not triggered or errors are reported during the precheck.

**Background information**

If you ignore the error messages and forcibly replace the disk, data loss may occur. You can use the disk replacement feature to handle only damaged disks that are reported by Apsara Distributed File System. You can use the disk replacement feature to replace only damaged data disks. If you do not replace the disks with new disks, the maintenance process is interrupted. The data disks of Apsara Infrastructure Management, ODPS, Object Storage Service (OSS), and Simple Log Service can be repaired.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. In the left-side navigation pane of the page that
appears, choose **Hardware O&M > HDD Repairs**.
3. Click the **Repair** tab.
You can query disk replacement tasks by progress or machine name.
4. Perform operations based on the task status in different phases.
The maintenance process is divided into the following phases: Disk Replacement, Disk Formatting & Mounting, and Health Check. Disk Replacement: replaces the failed disk. Disk Formatting & Mounting: checks the basic information about the new disk and perform initialization operations such as formatting and mounting. Health Check: waits for the related business system to check the new disk. After the check is passed, the new disk is used. If the check is not passed, contact technical support to troubleshoot the issue. The task can be in one of the following states in each of the three phases: not started (displayed in gray), in progress (displayed in blue), completed (displayed in green), and failed (displayed in red). The following table describes the corresponding operations that can be performed in these states.

| Disk replacement | Disk formatting and mounting | Health check | Available operation |
|---|---|---|---|
| Not started | Not started | Not started | Start to replace the disk |

| In progress | Not started | Not started | Complete the disk replacement |
|---|---|---|---|
| Completed | In progress | Not started | Replace the disk again |
| Completed | Failed | Not started | Replace the disk again |
| Completed | Completed | In progress | None |
| Completed | Completed | Failed | None |

Related operations: Start to replace the disk: Click **Start Changing**. Complete the disk replacement: Click **Complete Replacement**. Replace the disk again: Click **Re-change Disk**.

###### 4.1.3.1.3 History

You can view a list of all repair records to learn repaired machines and HDDs, and repair results.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. In the left-side navigation pane of the page that
appears, choose **Hardware O&M > HDD Repairs**.
3. Click the **History** tab.
You can view disk replacement tasks by cluster and status.
4. Find the disk replacement task that you want to manage and click **Details** in the **Actions**
column. In the panel that appears, you can view the task execution status, including the details of each step beginning from the report.

##### 4.1.3.2 Machine repairs

You can view and query the machine repair records.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Hardware O&M**. In the left-side navigation pane of the page that
appears, choose **Hardware O&M > Machine Repair**.
3. On the WholeMachineMaintenance page, view the machine repair records. You can select
Host Name, Status, Cluster, or Maintenance Method from the drop-down list to filter machine repair records that you want to view. You can also click **Advanced Filter** to filter repair records.
4. The list displays the details of the machine repair records. The following table describes the
relevant parameters.

| Parameter | Description |
|---|---|
| ID | The task ID. |
| Host Name/IP | The name and IP address of the host. |
| Cluster | The cluster to which the machine belongs. |
| Maintenance Method | The way the machine is repaired. |
| Status | The state of the machine repair. Valid values: failed: The machine repair failed. cancel: The machine repair task is canceled. doing: The machine is being repaired. done: The machine repair task is complete. |
| Start Time | The time when the machine repair task begins. |
| End Time | The time when the machine repair task ends. |
| Actions | Click Details. In the pane that appears, view the corresponding time of each repair step. |

#### 4.1.4 O&M tools

This topic describes the modules related to O&M tools.

**Modules**

| Module | Description |
|---|---|
| Task Management | Displays the details of tasks running on Apsara Infrastructure Management and the PaaS base. |
| Service Management | Allows you to manage the services deployed on Apsara Infrastructure Management and the corresponding service templates. |
| VM Dashboard | Displays the Docker VMs pulled and managed by Apsara Infrastructure Management in the environment. |
| Service Registration Variable Dashboard | Displays the service variables registered with products and corresponding content. |
| Resource Dashboard | Displays the instances of resources such as DNS and VIPs requested by using Apsara Infrastructure Management. |
| Basic Service Monitoring | Displays the monitoring information about basic services to help identify exceptions. |

##### 4.1.4.1 Task management

You can view the details of tasks running on Apsara Infrastructure Management and the PaaS base.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane of the page that appears, choose **O&M Tools > Task**
**Management** to go to the Task Dashboard page.
4. By default, the Tianji Tasks tab appears. Select a time range to view the tasks running on
Apsara Infrastructure Management within the specified time range. You can click **1 Hour**, **1**
**Day**, or **1 Week** to quickly select a time range.
Click **Details** in the Actions column of the task that you want to manage to go to the **Task**
**Details** page.
Details of a task on Apsara Infrastructure Management

| No. | Section | Description |
|---|---|---|
| 1 | Basic Information | Displays basic information about the task, such as task name, task status, submitter, submission time, and execution duration. |

| 2 | Related Clusters | Displays the clusters that are related to the task. You can submit a task to change multiple clusters. In most cases, an Apsara Stack task is associated with one cluster. Cluster/Product: the cluster that is changed and the product to which the cluster belongs. Status: the state of the task. Valid values: Failed Terminated Running Paused Succeeded Waiting Progress: the state of the task in progress. In most cases, you must build the task before you submit it. The building states include Waiting, Doing, Done, and Failed. Note Apsara Infrastructure Management calculates the change content based on the desired-state configurations. For example, Apsara Infrastructure Management determines whether to update the version and the version that is updated to. The task change states include Waiting for Change, Changing, Change Completed, and Change Failed. Version/Submission Time: the version and the time when the task is submitted. Actions: Click Build Details to view the components of the cluster, status, and progress. Click Resource Task Details to view the status, ownership, and error message of the resource request task. |
|---|---|---|
|   |   | Displays the changes of a cluster. Cluster changes include component changes and machine changes. Component Changes: the version change of a component. The version change status of all components is displayed based on services. This section displays the number of components of each service. |

|   |   | Note Different operation buttons are displayed for each task state. The |
|---|---|---|
|   |   | operation buttons include Terminate, Retry, Suspend, and Continue. If the task state is Running, the Terminate and Suspend buttons are displayed. If the task state is Paused, the Continue button is displayed. If the task state is Failed and Terminate, the Retry button is displayed. Make sure that no new tasks are submitted for the current cluster or server role. Click Terminate in the upper-right corner of the list to terminate a task. Click Retry in the upper-right corner of the list to perform theR etry Upgrade, Force Retry, or Retry Rollback operation. Click Suspend in the upper-right corner of the list to suspend a task. Click Continue in the upper-right corner of the list to continue a task. Click the icon on the left of the service name to view the change details of each component. For more information, see the following component change table. |

| 3 | Change Content | Click Details in the Actions column of the component that you want to manage to view the component progress. Overview Information: displays the basic information about the component, such as Commit Id, Rolling Status, Approval Policy, and Upgrade Plan. In the upper-right corner of the page, click View Details to go to the Rolling Summary page and view the component update details. Go to the Rolling Summary page. In the Overview Information section, you can click Retry, Terminate, or Suspend to retry, terminate, or suspend a task. You can perform these operations only on unfinished tasks. The system can monitor and display the Service Level Agreement (SLA) changes. You can view the real-time monitoring status of components. Click View Logs to view SLA monitoring logs. Click Modify SLA Configuration to modify the SLA configuration. Note You can view the SLA-related content of services for which the SLA feature is enabled. Click View All to view the component update details. Click Edit Parameter to modify the relevant parameters. Only the parameters for unfinished tasks can be modified. In the Instance Details section, you can add multiple component tasks to the blacklist. Instance Details: displays information such as the change status of component instances, component actions, and metrics. Note The Machine Changes tab is displayed only when the value in the Change Type column is Machine Scale-out, Machine Scale-In, Component Scale-out, or Component Unpublishing. Machine Changes: Machine changes in this module refer to machine scaling operations, excluding other operations such as machine repairs. The change content is displayed based on the Machine, Change Type, Status, and Actions columns. Machine: the name of the machine. Change Type: the change type. Valid values: Machine Scale-out, Machine Scale-in, Component Scale-out, and Component Unpublishing. Status: the state of the change. For more information, see the status in the Add to Cluster section. Actions: the actions that you can perform. You can log on to the machine and view the machine details. |
|---|---|---|
|   |   | > Document Version: 2025110 |

|   |   | Click Terminal in the Actions column to log on to a machine. Click Details in the Actions column to go to theM achine Overview page and view the machine details. Basic Information: displays the following information: Change Status, Machine Status, Machine Action, Cluster, Machine Metrics, and Submission Time. Details: consists of Add to Cluster, Clone, and Deploy Component Instances. Add to Cluster: displays the cluster where the machine resides and the cluster to which you want to add the machine, as shown in the preceding figure. Status: the state of the machine change. Valid values: Failed: The change failed. Cancel: The change task is canceled. For example, the machine scale-in task is submitted when the machine scale-out task is not complete. Doing: The change is in progress. Waiting: The change is waiting to be performed. Done: The change is complete. Current Cluster: the cluster where the machine resides. Destination Cluster: the cluster to which you want to add the machine. |
|---|---|---|

**Component change table**

| Parameter | Description |
|---|---|
| Component | The components of the service. |
| Status | The state of the component. Valid values: Building: The component is being built. Build Failed: The component failed to be built. Waiting: The component is waiting to be changed. Running: The component is being changed. Paused: The change is paused. Rolling Back: The change is being rolled back. Rolling Back Prepared: The rollback is being prepared. Downloading: The program and configurations are being downloaded. Ready: The dependencies are being updated. Download Timeout: The download timed out. Succeeded: The change is complete. Failed: The change failed. Blocked: The component is not updated because the dependencies failed to be changed. Obstructed: The change is blocked by a previous task. Terminated: The task is terminated. Rolling Back Failed: The rollback failed. Rolled Back: The rollback is successful. Resource Checking: The resources are being checked. Resource Apply Failed: The resources failed to be requested. Su Paused: The canary release is paused. If you specify canary release rules, you must specify the interval at which the canary release is paused. Su Binary Paused: The version change is paused when no canary release is performed. Su Failed Paused: The canary release failed. In this case, the change is paused. You must determine whether to resume the change. Precheck: The component update is being prechecked. The precheck is performed before the download. Precheck Failed: The precheck failed. Postcheck: The component is being checked after the task is complete. Postcheck Failed: The post-check failed. |
| Dependency | Displays the dependencies required for component update. You can update the component only after the dependencies are updated. You can view the dependencies to locate the component on which task blockage occurs. |

| Actions | Click Details in the Actions column to view the change details of the component. |
|---|---|

5. Switch to the PaaS Tasks tab, and select a time range to view the tasks running on thePaaS
base within the specified time range. You can click **1 Hour**, **1 Day**, or **1 Week** to quickly select a time range. Click **Details** in the Actions column of the task that you want to manage to go to the **Task**
**Details** page.
Details of a task on the PaaS base

| Section | Description |
|---|---|
| Base Info | Displays the basic information about the task, including Task ID, Status, Created, Create Time, Start Time, and End Time. |
| Subtask List | Displays the information about the subtask, including Id/Description, Status, Describe, Change Object, Create/EndTime, ExecutionMethod, and Actions. Valid values of Status: Failed Processing Suspended Waiting Completed Click Cluster in the Change Object column to go to the Cluster Details page in Resources > Product & Cluster O&M and view the cluster details. Click Show Parameters in the Actions column to view the parameter names and values. Click Yaml in the Actions column to view the storage configuration information. Click Modify Execution Configuration in the Actions column to modify the configuration of the task. Click Approve in the Actions column to approve the task. |

##### 4.1.4.2 Service management

This topic describes how to manage the services deployed on Apsara Infrastructure Management and the corresponding service templates.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**. In the left-side navigation pane of the page that appears,
choose **O&M Tools > Service Management**.
3. On the **Service Management** page, select a service from the **Service** drop-down list. The
templates and instances of the service are displayed on the **Service Template** and
**Service Instances** tabs.
4. Perform the following operations on the **Service Template** tab:
Click **Create Template** to create a template. The following table describes the template details.

| GUI element | Description |
|---|---|
| Basic Information | Name: the name of the template. This field is required. Group: the group of the template. You can select an existing group or click + Create Group to create a group. Description: the description of the template. This field is required. |
| Template Content | Enter a file name or folder name in the search box to filter template files. Click the icon, and then choose Add Folder or Create File. Select the file that you create and click Show Content. In the text box that appears, enter the content of the file and click Preview and Submit. In the Confirm and Submit dialog box that appears, enter the content description and click OK. Submit Description: the description of the template content. Difference File: the differences between the file and the previous file. |

Enter a template name in the Template search box to filter **service templates**. Fuzzy search is supported. The following table describes the parameters in the service template list.

| Parameter | Description |
|---|---|
| Template | The name of the service template. |
| Description | The description of the template content. |
| Group | The group to which the template belongs. |

| Last Modified At | The time when the service template was last modified. |
|---|---|
| References | The number of times the service template is referenced. Click the value in the References column of the service template that you want to manage to go to the template details page and view the reference details of the template in different versions and clusters. |
| Actions | Click Edit in the Actions column to edit a template. Click Delete in the Actions column to delete a template. Click Operation History in the Actions column to view the operation records of a template, including the description, version, operator, and operation time. Click Version Differences in the Actions column to view the differences between the current version and other versions. |

5. The **Service Instances** tab displays instance information based on **Cluster**, **Product**, and
**Actions**. The following table describes the details.

| Parameter | Description |
|---|---|
| Cluster | The cluster where the service is deployed. Click the cluster name to go to the Cluster Details page and view the cluster details. |
| Product | The product to which the cluster belongs. |
| Actions | Click Details in the Actions column to go to the component details page and view the details of the service components. |

##### 4.1.4.3 VM dashboard

The VM dashboard displays the Docker VMs pulled and managed by Apsara Infrastructure Management in the environment.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane of the page that appears, choose **O&M Tools > VM**
**Dashboard**.
4. Enter a value in the search box or click **Advanced Filter** to filter the desired resource data
by **VM**, **Product**, **Cluster**, **Current Physical Machine**, and **Desired Physical Machine**.
5. The following table describes the parameters related to the **VM dashboard** list.

| Parameter | Description |
|---|---|
| Product | The name of the cloud service. |
| Cluster | The cluster to which the VM belongs. |
| VM | The name of the VM. Click the VM name to go to the Machine Details page. You can view the details of the VM. Click Terminal in the VM column to go to the logon page and log on to the VM. |
| Current Physical Machine | The physical machine where the VM resides. Click the name of the physical machine to go to the Machine Details page. You can view the details of the physical machine. Click Terminal in the Current Physical Machine column to log on to the physical machine. |
| Desired Physical Machine | The preset physical machine to which you want to migrate the VM. Click the name of the desired physical machine to go to the Machine Details page. You can view the details of the physical machine. Click Terminal in the Desired Physical Machine column to log on to the physical machine. |

##### 4.1.4.4 Dashboard of service registration variables

**variables**

You can view the service variables registered with products and corresponding content.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. In the left-side navigation pane, choose O&M Tools > Service Registration Variable
Dashboard.
4. In the upper-right corner of the page, click the download icon to export the configurations in
the list. A file in the **XLSX** format is generated, and the file can be downloaded to your computer by using a browser.
5. In the upper part of the page, enter a value in the search box or click **Advanced Filter** to
filter desired registration variables by **Service Registration**, **Service**, or **Cluster**.
6. In the lower part of the page, view the following information about variables: **Service**,
**Service Registration**, **Cluster**, and **Update Time**.
Click the **show****or****hide** icon in the **Service Registration** column of the service that you want to manage to view or hide the registration information about the service. Click the value in the **Service Registration** column of the service that you want to manage. In the message that appears, view the complete registration information about the service.

##### 4.1.4.5 Resource dashboard

The resource dashboard displays the instances of resources such as Domain Name System (DNS) and virtual IP addresses (VIPs) requested by using Apsara Infrastructure Management.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**

**Management > O&M Tools**

3. In the left-side navigation pane of the page that appears, choose **O&M Tools** **>** **Resource**
**Dashboard**.
4. In the upper-right corner of the page, click the download icon to export the instance list as
a **JSON** file to your local computer by using a browser.
5. In the upper part of the page, enter a value in the search box or click **Advanced Filter** to
filter the desired resource data by **Name**, **Product**, **Cluster**, **Service**, **Component**,
**Application**, **Resource Type**, **Resource Status**, **Parameters**, and **Result**.
6. In the lower part of the page, view the following information: **Name**, **Product/Cluster**,
**Component/Application**, **Resource Status**, **Parameters**, **Result**, **Resource ID**,
**Reprocess Status**, **Reprocess Message**, **Reprocess Result**, **Business Additional**
**Configuration**, **Related Versions**, and **Error Message**.
Click the **show and hide** icon in the **Parameters**, **Result**, and **Reprocess Result** columns of the resource that you want to manage to view or hide the resource parameters, resource request result, and second request status. Click the values in the **Parameters**, **Result**, and **Reprocess Result** columns of the resource that you want to manage. In the messages that appear, view the complete information about the resource parameters, resource request result, and second request status.

**Resource status table**

| Parameter | Description |
|---|---|
| Name | The resource name. |
| Product/Cluster | The product and cluster of the service. |
| Component/Applicatio n | The component and application of the server role. |
| Resource Status | The resource request state. |
| Parameters | The resource request parameters, such as the VIP configuration. |
| Result | The resource request result, such as the endpoint allocated to an ApsaraDB RDS instance and the VIP. |
| Resource ID | The resource ID. |
| Reprocess Status | The state of the second request, which is automatically initiated when the first quest fails. |
| Reprocess Message | The message of the second request, which is automatically initiated when the first quest fails. |
| Reprocess Result | The result of the second request. |

| Business Additional Configuration | The custom configurations that are attached to the resource by the business service. These configurations are not specified by using Apsara Infrastructure Management. |
|---|---|
| Refer Version List | The resource versions that have been used. |
| Error Message | The error message. |

##### 4.1.4.6 Basic service monitoring

You can view the monitoring information about basic services to quickly identify service exceptions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**. In the left-side navigation pane of the page that appears,
choose **O&M Tools > Basic Service Monitoring**.
3. On the Basic Service Monitoring page, view the information in the API Status and Tianji Data
Status sections.
**API Status**: displays Console API Status, Tianji API Status, Kubernetes API Status, and
Gateway API Status.
**Tianji Data Status**: displays Data Sync Time and Desired State Calc Time.

#### 4.1.5 Web clients

This topic describes the CLI-based logon and remote O&M features provided by the Web Terminal module. This module also supports blocking and approval of high-risk operations, and allows you to audit all operations.

**Modules**

| Module | Description |
|---|---|

| Web Client Logon | Provides a web client to support the following features: Server Logon: You can query information about servers, virtual machines (VMs), and containers. You can log on to servers, VMs, and containers. Database Logon: You can query the metadatabases requested by services. You can log on to metadatabases. vSwitch Logon: You can query information about vSwitches. You can log on to vSwitches. |
|---|---|
| Account Authorization | Allows you to manage temporary account authorization. |
| Command Management | Allows you to manage CLI commands that are run by using a web client. |
| Operation Audit | Allows you to audit O&M operations that are performed by using a web client. |

##### 4.1.5.1 Web Client Logon

Web client logon includes server logon, database logon, and switch logon.

###### 4.1.5.1.1 Server Logon

You can search for containers, VMs, and physical machines by different conditions and log on to perform O&M operations. You can also log on to ops1 to ops4 control nodes to perform O&M operations.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal > Web Client Logon > Server Logon**.
3. Log on to the server in the ServerRole login or MachineGroup login tab.
4. Click the ServerRole login tab.
Select a server role name from the **Server Role** drop-down list. Fuzzy search is supported. The cluster name, status, and project are displayed above the **Host** section. You can click Login or Log on to the vm host.
**Login**: log on to the VM where the server role is deployed.
**Log on to the vm host** : log on to the host of the VM where the server role is
deployed. Perform the following steps to log on to the host: Click the icon to refresh the column and try to obtain the docker ID. If the docker ID is obtained, the logon button appears. Click the logon button to log on to the host.

> **Note:** If the docker ID does not appear after the refresh, the docker ID is not obtained. Possible causes:
> The status of the container is abnormal.
> The server role is in the process form and does not have a docker container.

Log on to the web terminal page and click the node that you want to log on. You can also click the icon, and select an account in the dialog box. By default, the ops account is selected. If no accounts meet your permission requirements, you can apply for a temporary account. You can select an account type and apply for an account. After you submit an account application, wait for the application to be approved. After the application is approved, the account takes effect and can be used to log on to the server. Enter Linux commands in the CLI window to perform related operations. Click **File operations** to upload and download files. Click **File Upload**. You can use one of the following methods to upload a file: Click the dotted box. In the dialog box that appears, select the file that you want to upload and click **Open**. Click **Upload** in the **Upload File** dialog box. Drag the file to the dotted box and then click **Upload**. Click **Download File** in the upper-right corner of the CLI window. The **Download**
**File** dialog box appears. Configure the **File Directory** and **File Name** parameters
and then click **Download** to download the file to the default download folder used by your local browser.

> **Note:** The file that you want to upload or download cannot exceed 200 MB in size.

In the **Docker** column, click the relevant links to log on to the container, or view logs and inspection reports of the container.
5. Click the MachineGroup login tab.
Select a cluster name from the **Cluster** drop-down list. Fuzzy search is supported. Find the machine that you want to log on to from the machine list and click **Login** in the Machine column. Log on to the web terminal page and click the node that you want to log on. You can also click the icon, and select an account in the dialog box. By default, the ops account is selected. If no accounts meet your permission requirements, you can apply for a temporary account. You can select an account type and apply for an account. After you submit an account application, wait for the application to be approved. After the application is approved, the account takes effect and can be used to log on to the server. Enter Linux commands in the CLI window to perform related operations. Click **File operations** to upload and download files. Click **File Upload**. You can use one of the following methods to upload a file: Click the dotted box. In the dialog box that appears, select the file that you want to upload and click **Open**. Click **Upload** in the **Upload File** dialog box. Drag the file to the dotted box and then click **Upload**. Click **Download File** in the upper-right corner of the CLI window. The **Download**
**File** dialog box appears. Configure the File Directory and File Name parameters and
then click **Download** to download the file to the default download folder used by your local browser.

> **Note:** The file that you want to upload or download cannot exceed 200 MB in size.

###### 4.1.5.1.2 Database logon

You can log on to databases that are used by server roles of services and perform related operations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**

**Management > Web Terminal**

3. In the left-side navigation pane of the page that appears, choose **Web Terminal > Web**
**Client Logon > Database Logon**.
4. Select a service name from the **Service** drop-down list. Fuzzy search is supported.
5. The lower part of the page displays the databases that are used by all server roles of the
service. Find the database that you want to manage and click **Login** in the **Operation** column.
6. On the page that appears, click the node or the
icon next to the node. Enter SQL statements in the CLI window to perform related operations.

###### 4.1.5.1.3 vSwitch logon

You can log on to a vSwitch to perform related operations.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**. In the left-side navigation pane of the page that appears,
choose **Web Terminal > Web Client Logon > vSwitch Logon**.
3. Find the vSwitch to which you want to log on and click **Log On** in the **Actions** column.
4. On the page that appears, click the vSwitch or the
icon next to the vSwitch. In the dialog box that appears, enter the username and click OK to log on to the vSwitch. Enter the password as prompted. You can log on to the vSwitch only if you enter the correct password. Otherwise, you will log on to the jump server as an ops user. After you log on to the vSwitch, enter Linux commands in the CLI window to perform related operations.

##### 4.1.5.2 Account authorization

You can view the information about temporary account authorization.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**. In the left-side navigation pane of the page that appears,
choose **Web Terminal > Account Authorization**.
3. On the Account Authorization page, view and manage temporary account authorization.
4. You can filter information about temporary account authorization by **User** and **Status**.

| Parameter | Description |
|---|---|
| User | The name of the user in the Apsara Uni-manager Operation Console. |
| Type | The type of the account. Valid value: SERVER. |
| Logon Account | ops: a regular Linux account that belongs to the ops user group. This account allows you to perform read, write, and execute operations on files based on configured file permissions. We recommend that you use the ops account to perform routine O&M. The super administrators of Open Application Model (OAM) and administrators, auditors, security administrators, and basic O&M engineers of the web console for Apsara Infrastructure Management can use the ops account. audit: a regular Linux account that belongs to the audit user group. This account can be used to run the sudo command to obtain the privileges to run the following commands without providing the password: aureport, auditctl, ausearch, last, lastlog, cat, less, more, head, and tail. This account can also be used to perform the stop auditd and rsyslog operations without providing the password. This account is the owner of the /var/log directory. By default, auditors of the web console for Apsara Infrastructure Management can use the audit account and approve and revoke the temporary permissions of this account. security: a regular Linux account that belongs to the security user group. This account can be used to run the sudo command to obtain the privileges to run the following commands without providing the password: passwd, chown, chmod, chgrp, usermod, chage, and visudo. By default, security administrators of the web console for Apsara Infrastructure Management can use the security account and approve and revoke the temporary permissions of this account. admin: a regular Linux account that belongs to the admin user group. This account can be used to run sudo commands without providing the password and has higher permissions. By default, administrators of the web console for Apsara Infrastructure Management can use the admin account and approve and revoke the temporary permissions of this account. root: a super Linux account with the super administrator permissions on devices. By default, super administrators of OAM can use the root account and approve and revoke the temporary permissions of this account. |
| Status | Authorized: The authorization is within the validity period. Recycled: The permissions are revoked by the account administrator within the validity period of the authorization. Invalid: The authorization expires and is invalid. |

| Authorization Time | The time when the temporary authorization application is approved. |
|---|---|
| Expiration Time | The time when the authorization expires. |
| Actions | The operation that you can perform. Valid value: Reclaim permissions. Note You can revoke permissions when the following conditions are met: The authorization does not expire. The user has the permission to revoke the permissions of the authorized account. For example, only the OAM super administrators can revoke the permissions of the root account. |

##### 4.1.5.3 Command management

You can manage the CLI commands that are run by using web clients.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**. In the left-side navigation pane of the page that appears,
choose **Web Terminal > Command Management**.
3. On the Command Control page, view and configure command management policies.
Click **Create Policy**. In the dialog box that appears, configure the required parameters such as Policy Name, Manage users, Control dimension, and Command set to create a policy. Click **Import** to import the policy. Only .xls and .xlsx files can be imported. You can enter a value in the Policy Name search box to search for a policy. The following table describes the parameters in the list.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. The name must be 0 to 32 characters in length and can contain letters, digits, and hyphens (-). |
| Command Set | The set of commands that are used to implement management. |
| Command set type | The type of the command set. Valid values: Blacklist and Whitelist. |
| Manage users | The names of the Apsara Uni-manager Operations Console users that are managed by the policy. Note You can select all users and exclude specific users. |
| Control Dimension | The management dimension. Valid values: Component container dimensions and Machine dimension. |
| Control Components/machine s | The names of the components or the machines that are managed. Note You can select all components and exclude specific components. When you specify the machines that are managed, you can enter the hostnames of machines and separate the hostnames by row. |
| Status | The state of the policy. Valid values: Enable and Close. |
| Creation time | The time when the policy is created. |
| Actions | Click Edit in the Actions column of the policy that you want to manage to modify the policy. Click Delete in the Actions column of the policy that you want to manage to delete the policy. |

Select the policy that you want to manage and click **Export** to download and view the policy.

##### 4.1.5.4 Operation audit

You can audit the O&M operations that are performed by using web clients.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Web Terminal**. In the left-side navigation pane of the page that appears,
choose **Web Terminal > Operation Audit**.
3. The Audit page consists of three tabs: Command Records, Upload and Download Audit, and
Playback. By default, the **Command Records** tab appears.

**Command Records**

You can view the operation records of commands that are executed by using web clients.
1. Select a filter condition from the drop-down list and enter a value in the search box. You
can filter command records by Command, Operated At, Machine, and Operated By.
2. Click **Advanced Filter** to filter command records by **Command**, **Operated At**, **Machine**,
**Operated By**, or their combinations.
3. In the command record list, view the following information: **Command**, **Operated By**,
**Operated At**, **Machine/Container**, **Target Type**, **SessionId**, and **Audit Result**.

**Upload and Download Audit**

You can view the information about file uploads and downloads performed by using web clients.
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
3. Click **View** in the **Actions** column corresponding to an operation record.
4. In the video playback window, click the
icon to play back the video.

### 4.2 Capacity management

This topic describes the features related to capacity management.

**Features**

By analyzing the capacity usage of each service and understanding unique usage patterns, you can forecast capacity trends to inform expansion plans and other operational decisions.

| Module | Description |
|---|---|
| Capacity Overview | Displays an overview of the total capacity and any anomalies across each cloud service, facilitating rapid problem identification. |
| Compute Capacity | Displays the capacity usage and trend analysis of compute services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |

| Network Capacity | Displays the capacity usage and trend analysis of network services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
|---|---|
| Storage Capacity | Displays the capacity usage and trend analysis of storage services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Base Capacity | Displays the capacity usage and trend analysis of Apsara Infrastructure Management general services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Database Capacity | Displays the capacity usage and trend analysis of database services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |
| Middleware Capacity | Displays the capacity usage and trend analysis of middleware services, empowering you to conduct targeted O&M tasks in accordance with your practical requirements. |

#### 4.2.1 Capacity overview

This topic describes how to view the overall capacity usage and capacity exceptions in each cloud service to help you quickly identify errors.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Capacity**
**Overview**.
3. On the Capacity Overview page, view data in the following sections.
**Service Statistics**: displays the cloud service capacity that is connected to your
environment, including **Total Services**, **Current Normal Capacity (Services)**, and
**Current Capacity Alert (Services)**.
**Cloud Service Capacity Overview**: displays the numbers of clusters that have
exceptions and clusters that are predicted to have exceptions for custom cloud services. In the upper-right corner of the page, you can click **Custom Cloud Services** to specify the custom cloud services to be displayed.

> **Note:** You must specify at least one custom cloud service and can specify up to five custom cloud services.

**Cloud product capacity overview**: displays the capacity overview of all cloud services
in the cluster and capacity dimensions. If clusters that have exceptions or clusters that are predicted to have exceptions exist in a cloud service, **Cluster Capacity Alert** appears in the upper-right corner of the service card. You can click **All clusters**, **Current Capacity Alert (Clusters)**, or **Forecast**
**Capacity Alert (Clusters)** to view details of the relevant clusters.
4. In the upper-right corner of the page, click **Refresh** to refresh the capacity overview data.
5. In the upper-right corner of the page, click **Export Capacity Report**, select desired cloud
services, and then click **Export** to export the capacity data to your on-premises machine.

#### 4.2.2 Computing capacity

##### 4.2.2.1 ECS capacity

You can view the Elastic Compute Service (ECS) capacity to obtain the usage and trend of ECS resources. This helps you perform O&M operations based on your business requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Compute Capacity**.
3. In the left-side navigation pane, click **ECS Capacity**.
4. In the upper part of the page, view ECS data in the **Capacity Overview** and **Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view **vCPU Capacity**, **GPU Capacity**, and
**Memory Capacity** of all clusters, including the **Total**, **Allocated**, and **Capacity**
**Allocation Rate** parameters.
In the **Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **vCPU**, **Memory**, and **GPU** allocation rates of all clusters or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. On the **Cluster Capacity** tab in the lower part of the page, click **Advanced Filter** to filter
the list by **Cluster**, **Cluster Type**, **Zone**, and **CPU** to obtain the desired capacity data. Click the up and down arrow icon in the **vCPU Allocation Rate**, **Memory Allocation**
**Rate**, **GPU Allocation Rate**, or **GPU capacity** column to sort the cluster capacity data
in ascending or descending order. When the distribution rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Details** in the **Capacity Planning Formula** column of a desired cluster to obtain the detailed capacity planning formula. Click **Export** to export the cluster capacity data to your on-premises machine.
6. On the **Specification Inventory** tab, you can filter the list by **Specification** to obtain the
desired instance types. Fuzzy search is supported. Click the up and down arrow icon in the **Instances That Can Be Created** or **Created**
**Instances** column to sort the instance types in ascending or descending order.
Click the desired instance type to obtain details of the clusters that use the instance type. Click **Export** to export the inventory data of the instance types to your on-premises machine.

#### 4.2.3 Network capacity

##### 4.2.3.1 SLB Capacity

You can view the Server Load Balancer (SLB) capacity to learn the usage and trend of SLB resources. This helps you perform O&M operations based on your business requirements.
1. Go to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **General** > **Capacity** > **SLB Capacity**.
3. In the upper-right corner of the page, select the target cluster to view the capacity data of
different clusters.

> **Note:** The clusters that have **slbCluster** in their names are default clusters.
> The clusters that have **slbExtraCluster** in their names are expanded clusters.

4. In the upper part of the page, view the **Capacity Overview** and **Cluster Allocation Rate**
**Trend** of the SLB instance.
The **Capacity Overview** section displays the **Internet VIP Capacity** and **Internal VIP**
**Capacity** of the cluster. The information includes the total capacity, allocated capacity,
and capacity allocation rate. When the capacity allocation rate exceeds the warning threshold (80%), the value is highlighted. The warning threshold cannot be customized. The **Cluster Allocation Rate Trend** section displays the trend charts of the allocation rates of public and internal VIPs in different time periods. Move the pointer over a node to view the data of the corresponding time node.
5. In the **Capacity Details** section, you can view the capacity details of the cluster by
**Cluster**. Click **Export** to export the data to your computer.

#### 4.2.4 Storage capacity

##### 4.2.4.1 EBS

You can view the Elastic Block Storage (EBS) capacity to obtain the usage and trend of EBS resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **EBS**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Usage Trend** sections.
In the **Physical Capacity Overview** section, you can view the capacity data of **Hybrid**
**Clusters** and **Full-Flash Clusters**, including the **Total**, **Used**, and **Capacity Usage**
parameters. In the **Physical Capacity Usage Trend** section, you can view the trend chart that shows the physical capacity usage of all full-flash clusters, all hybrid clusters, or a single cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, filter the list by **Cluster**, **Zone**, **Storage**
**Type**, **Specification**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage**, **Physical Capacity**
**Usage (TiB)**, **Logical Capacity Usage**, **Logical Capacity Usage (TiB)**, **Inventory**
**Capacity Allocation Rate**, or **Inventory capacity allocation (TiB)** column to sort the
list in ascending or descending order. Physical capacity: the total physical capacity that is reported by Apsara Distributed File System.

> Logical capacity: the maximum amount of data that you can write into disks.
> Inventory capacity: the total capacity of cloud disks that you can create.

Click **Export** to export the capacity data to your on-premises machine.

##### 4.2.4.2 OSS

You can view the Object Storage Service (OSS) capacity to obtain the usage and availability of OSS resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **OSS**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Allocation Rate Trend** sections.
In the **Physical Capacity Overview** section, you can view the data of all hybrid clusters, including the **Total**, **Allocated**, and **Capacity Allocation Rate** parameters. In the **Physical Capacity Allocation Rate Trend** section, you can view the trend chart that shows the physical capacity usage of all hybrid clusters or a single hybrid cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage**, **Physical Capacity**
**Usage (TiB)**, **Logical Capacity Usage**, or **Logical Capacity Usage (TiB)** column to
sort the list in ascending or descending order. Physical capacity: the total physical capacity that is reported by Apsara Distributed File System.

> Logical capacity: the maximum amount of data that you can write into disks.

Click **Export** to export the capacity data to your on-premises machine.

##### 4.2.4.3 Tablestore

Viewing Tablestore storage capacity enables you to understand current resource usage and availability. This helps you perform more informed O&M operations.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation bar, click **Tablestore**.
4. In the upper part of the displayed page, view data in the following sections: **Physical**
**Capacity Overview** and **Physical Capacity Usage Trend**.
In the **Physical Capacity Overview** section, you can view the following data of all hybrid clusters: **Total**, **Used**, and **Capacity usage**. In the **Physical Capacity Allocation Trend** section, you can view how the allocation of physical capacity is changing over time for all hybrid clusters or a specific one, with the hover-over feature to reveal detailed capacity metrics for any given node at that point in time.
5. In the lower part of the page that appears, click **Advanced Filter** of the **Capacity Details**
section. You can combine **Cluster**, **Zone**, **Storage Type**, and **CPU** to search for a desired cluster and view its storage capacity details. Click the sort icon in the headers of **Physical Capacity Usage**, **Physical Capacity**
**Usage (TiB)**, **Logical Capacity Usage**, or **Logical Capacity Usage (TiB)** columns to
arrange the list in ascending or descending sequence. Physical capacity: the total physical capacity reported by the Apsara Distributed File System.

> Logical capacity: the maximum volume of data that can be written onto the disks.

Click **Export** to export the capacity details to your on-premises computer.

##### 4.2.4.4 Simple Log Service

Viewing the Simple Log Service storage capacity helps you gain insights into the current resource usage and residual resources, which allows you to undertake targeted O&M operations that align with actual needs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **Simple Log Service**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Allocation Rate Trend** sections.
In the **Physical Capacity Overview** section, view the data of all hybrid clusters, including the **Total**, **Allocated**, and **Capacity Allocation Rate** parameters. In the **Physical Capacity Allocation Rate Trend** section, view the trend chart that shows the physical capacity usage of all hybrid clusters or a single hybrid cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up/down arrow icon in the **Physical Capacity Usage**, **Physical Capacity**
**Usage (TiB)**, **Logical Capacity Usage**, or **Logical Capacity Usage (TiB)** column to
sort the list in ascending or descending order. Physical capacity: the total physical capacity reported by the Apsara Distributed File System.

> Logical capacity: the maximum volume of data that can be written onto the disks.

Click **Export** to export the capacity data to your on-premises machine.

##### 4.2.4.5 Apsara File Storage NAS

Viewing the Apsara File Storage NAS (NAS) storage capacity helps you gain insights into the current resource usage and residual resources, which allows you to undertake targeted O&M operations that align with actual needs.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Storage Capacity**.
3. In the left-side navigation pane, click **NAS**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Allocation Rate Trend** sections.
In the **Physical Capacity Overview** section, you can view the following data of all hybrid clusters: **Total**, **Used**, and **Capacity usage**. In the **Physical Capacity Allocation Rate Trend** section, view the trend chart that shows the physical capacity usage of all hybrid clusters or a single hybrid cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, **Storage Type**, and **CPU** to view the desired capacity data.
Click the up/down arrow icon in the **Physical Capacity Usage**, **Physical Capacity**
**Usage (TiB)**, **Logical Capacity Usage**, or **Logical Capacity Usage (TiB)** column to
sort the list in ascending or descending order. Physical capacity: the total physical capacity reported by the Apsara Distributed File System.

> Logical capacity: the maximum volume of data that can be written onto the disks.

Click **Export** to export the capacity details to your computer.

#### 4.2.5 Base capacity

##### 4.2.5.1 Apsara Infrastructure Management storage capacity

#### storage capacity

You can view the storage capacity of Apsara Infrastructure Management to obtain the usage and availability of the relevant resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform O&M** > **Capacity** > **Base Capacity**.
3. In the left-side navigation pane, click **Apsara Infrastructure Management Storage**
**Capacity**.
4. In the upper part of the page, view data in the **Physical Capacity Overview** and **Physical**
**Capacity Usage Trend** sections.
In the **Physical Capacity Overview** section, you can view the **Total**, **Used Capacity**, and **Capacity Usage** parameters of all clusters. In the **Physical Capacity Usage Trend** section, you can view the trend chart that shows the physical capacity usage trend of all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
5. In the **Capacity Details** section of the page, click **Advanced Filter** and filter the list by
**Cluster**, **Zone**, and **CPU** to view the desired capacity data.
Click the up and down arrow icon in the **Physical Capacity Usage** or **Used Physical**
**Capacity (GB)** column to sort the list in ascending or descending order.
Click **Export** to export the capacity data to your on-premises machine.

#### 4.2.6 Database capacity

##### 4.2.6.1 RDS

You can view data on the MySQL capacity page to obtain the usage and availability of ApsaraDB RDS (RDS) resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **RDS**.
4. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters, including the **Total**, **Used**, and **Capacity allocation**
**rate** parameters.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
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

Filter the list by **Cluster**, **Zone**, and **CPU processor** to view the desired capacity data. When the allocation rate exceeds the water level warning threshold (80%), the value is highlighted. You cannot specify a custom water level warning threshold. Click **Export** to export the capacity data to your on-premises machine.

##### 4.2.6.2 ApsaraDB RDS for PostgreSQL

You can view the capacity of the ApsaraDB RDS for PostgreSQL service to obtain the usage and availability of the service resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **ApsaraDB RDS for PostgreSQL**.
4. In the upper-right corner of the page, select **All clusters** or a specific cluster to view the
capacity data.
5. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters or a specific cluster, including the **Total**, **Used**, and
**Capacity allocation rate** parameters.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster in different time periods. Move the pointer over a time node to view the recorded data.
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

##### 4.2.6.3 ApsaraDB for Redis

You can view the capacity of the ApsaraDB for Redis service to obtain the usage and availability of the service resources. This helps you perform O&M operations based on your business requirements.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **Redis**.
4. In the upper-right corner of the page, select **All clusters** or a specific cluster to view the
capacity data.
5. In the upper part of the page, view data in the **Capacity Overview** and **Cluster Capacity**
**Allocation Rate Trend** sections.
In the **Capacity Overview** section, you can view **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters or a specific cluster, including the **Total**, **Used**, and
**Capacity allocation rate** parameters.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend chart that shows the **Memory**, **CPU**, and **Disk** allocation rates of all clusters or a specific cluster within different time periods. Move the pointer over a time node to view the recorded data.
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

##### 4.2.6.4 ApsaraDB for MongoDB

You can view the capacity of ApsaraDB for MongoDB to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **MongoDB**.
4. In the upper-right corner of the MongoDB Capacity page, select **All clusters** or a specific
cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the MongoDB Capacity page, view **Capacity Overview** and **Cluster**
**Capacity Allocation Rate Trend**.
In the **Capacity Overview** section, you can view the **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters or the specific cluster, including **Total**, **Allocated**, and
**Capacity allocation rate**.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
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

##### 4.2.6.5 AnalyticDB for PostgreSQL

You can view the capacity of AnalyticDB for PostgreSQL to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **AnalyticDB for PostgreSQL**.
4. In the upper-right corner of the AnalyticDB for PostgreSQL Capacity page, select **All**
**clusters** or a specific cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the AnalyticDB for PostgreSQL Capacity page, view **Capacity**
**Overview** and **Cluster Capacity Allocation Rate Trend**.
In the **Capacity Overview** section, you can view the **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters or the specific cluster, including **Total**, **Allocated**, and
**Capacity allocation rate**.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
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

##### 4.2.6.6 PolarDB for PostgreSQL

You can view the capacity of PolarDB for PostgreSQL to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **PolarDB for PostgreSQL**.
4. In the upper-right corner of the PolarDB for PostgreSQL Capacity page, select **All clusters**
or a specific cluster to view the capacity data of all clusters or the specific cluster.
5. In the upper part of the PolarDB for PostgreSQL Capacity page, view **Capacity Overview**
and **Cluster Capacity Allocation Rate Trend**. In the **Capacity Overview** section, you can view the **CPU Capacity**, **Memory Capacity**, and **Disk Capacity** of all clusters or the specific cluster, including **Total**, **Allocated**, and
**Capacity allocation rate**.
In the **Cluster Capacity Allocation Rate Trend** section, you can view the trend charts of **Memory**, **CPU**, and **Disk** allocation rates for all clusters or the specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
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

##### 4.2.6.7 PolarDB-X

You can view the capacity of PolarDB-X to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **PolarDB-X**.
4. View the following information in the upper part of the PolarDB-X Capacity page:
**PolarDB-X Capacity Overview**. In this section, you can view the **CPU Capacity** and
**Memory Capacity** of all clusters, including **Total**, **Allocated**, and **Capacity Allocation**
**Rate**.
**PolarDB-X Capacity Allocation Rate Trend**. In this section, you can view the trend
charts of **CPU** and **Memory** allocation rates for all clusters or a specific cluster in different time periods. Move the pointer over a time node to view the data of the time node.
5. In the **Capacity Details** section in the lower part of the PolarDB-X Capacity page, view the
capacity details of the clusters by **Cluster** and **CPU**. When the allocation rate is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU Allocation Rate** or **Memory Allocation Rate** column to sort the cluster capacity data in ascending or descending order. You can click the name of a cluster to view the details of the physical machines in the cluster. You can click **Export** to export the capacity data to your computer.

##### 4.2.6.8 ApsaraDB for OceanBase

You can view the capacity of ApsaraDB for OceanBase to understand the used and unused resources of the service. Then, you can perform O&M based on your requirements.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Database**
**Capacity**.
3. In the left-side navigation pane, click **OceanBase**.
4. In the upper part of the OceanBase Capacity page, view **Top 5 Cluster Resource**
**Allocation Rates** and **Capacity Allocation Rate Trend**.
In the **Top 5 Cluster Resource Allocation Rates** section, you can view the allocation rates of **CPU** and **Memory**, and the usage of **Disk** of the clusters. In the **Capacity Allocation Rate Trend** section, you can view the trend charts of
**Memory**, **CPU**, and **Disk** allocation rates for the clusters in different time periods. Move
the pointer over a time node to view the data of the time node.
5. In the lower part of the OceanBase Capacity page, view the capacity details of ApsaraDB for
OceanBase. You can click the name of a cluster to view the details of the physical machines in the cluster. When the allocation rate or usage is above the water level warning threshold (80%), the value is highlighted. The water level warning threshold cannot be modified. You can click the **CPU Allocation Rate**, **Memory Allocation Rate**, or **Disk allocation**
**rate** column to sort the cluster capacity data in ascending or descending order.
You can click **Export** to export the capacity data to your computer.

#### 4.2.7 Middleware capacity

##### 4.2.7.1 ApsaraMQ for Kafka

You can view the capacity of the ApsaraMQ for Kafka service to obtain the usage of the service resources.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Capacity** > **Middleware**
**Capacity**.
3. In the left-side navigation pane, click **ApsaraMQ for Kafka**.
4. In the upper part of the page, view the trend chart that shows the **BYTES_IN** and
**BYTES_OUT** traffic throughput of a specific cluster within different time periods.
5. In the lower part of the page, view the capacity details of all clusters or a specific cluster.
From the **Cluster** drop-down list, select All Clusters or a desired cluster. Click the up and down arrow icon in the **Peak value in recent 6 hours**, **Average value**
**in recent 6 hours**, **Peak value for nearly 12 hours**, **Average in the last 12 hours**,
**Peak in the last 48 hours**, **Average in the last 48 hours** column to sort the capacity
data based on inbound traffic in ascending or descending order. Click **Export** to export the capacity data to your on-premises machine.

### 4.3 Control Service Platform

This topic lists the O&M platforms for control services. For more information, see the corresponding product documentation. Apsara Stack Inspection System Basic Service Control Configuration Management Database Apsara Stack Doctor Server Insight Base Container O&M Platform API O&M UniConsole

### 4.4 O&M Change

This topic describes the modules related to change management.

**Modules**

| Module | Description |
|---|---|
| Operation Orchestration Service | This module automates O&M for data centers. GUI-based operations are provided to help you perform O&M operations for resources at scale, simplify O&M management of IT resources, and support full-stack automated O&M of the infrastructure, the Apsara Stack environment, operating systems, and the application layer. |
| Log Cleanup | This module clears specific logs in specific containers or physical servers. |
| Plan Management | This module manages preset O&M actions. |
| Process Approval | This module provides approval and management features for O&M workflows. |

#### 4.4.1 Log cleanup

This topic describes the modules of the log cleanup module. This module allows you to clear logs from a specified container (Docker) or physical machine (virtual machine or bare metal).

**Modules**

| Module | Description |
|---|---|
| Rules | You can manage log cleanup rules by performing operations such as rule import, query, modification, export, and deletion. |
| Plans | You can execute log cleanup plans, including obtaining the usage data of containers or physical servers and clearing log. |
| Records | You can view detailed log cleanup records. |

##### 4.4.1.1 Rule management

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

##### 4.4.1.2 Plans

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

##### 4.4.1.3 Records

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

#### 4.4.2 Process approval

This topic describes the modules of the Process Approval module.

**Modules**

| Module | Description |
|---|---|
| My Submission | You can view the list of O&M workflows that you submitted. You can also query or cancel these workflows. |
| Pending Approval | You can view the O&M workflows that are submitted for your approval. You can also query and approve these O&M workflows. |

##### 4.4.2.1 My submission

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

##### 4.4.2.2 My approval

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

### 4.5 Disaster recovery management

**management**

This topic lists the supported disaster recovery management platforms. For specific O&M operations, see the corresponding product documentation. ASR for zone-disaster recovery ASR for geo-disaster recovery

### 4.6 Log center

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

#### 4.6.1 Log map

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

#### 4.6.2 Log query

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

#### 4.6.3 Log transfer

This topic describes the log transfer feature designed to transfer logs from SLS-Inner to either SLS-Pub or Object Storage Service (OSS). Implementing this feature enables long-term, secure storage of platform-side logs, enhancing platform security and ensuring regulatory compliance.

**Prerequisites**

You are granted the read and write permissions on Log Center.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Log Center** > **Log Dump**.
3. Select the transfer type.
**Offline transfer**: This type enables the offline transfer of logs from SLS-Inner to SLS-Pub,
offering a highly efficient solution ideal for archiving logs over extended periods. Once offline transfer is configured, tasks are automatically created based on individual Logstores. These tasks can be conveniently viewed and managed on the **Task**
**Management** tab.
**Real-time synchronization**: This type facilitates real-time synchronization of product
logs from SLS-Inner to SLS-Pub. However, if immediate synchronization of desired logs is not critical, we recommend that you utilize the offline transfer method instead. Once realtime synchronization is configured, tasks are automatically created based on individual Logstores. These tasks can be conveniently viewed and managed on the **Task**
**Management** tab.
**OSS archive**: This type involves transferring logs from SLS-Inner to OSS in an offline
mode, where the logs are archived securely in OSS. Once OSS archive is configured, tasks are automatically created based on individual Logstores. These tasks can be conveniently viewed and managed on the **Task Management** tab.

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
Transfer, Abnormal, Delay, Completed, Cancelled.
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
| Organization | The destination organization where you intend to transfer your logs. It is within this organization that necessary resources, like Simple Log Service projects and OSS buckets, will be created. When a resource sharing the same name already exists, ensure that the chosen organization is granted with the necessary permissions to access that resource. |
| Resource Set | The destination resource set where you intend to transfer your logs. It is within this resource set that necessary resources, like Simple Log Service projects and OSS buckets, will be created. |
| Log encryption storage | Upon enabling log encryption storage, you gain the capability to encrypt your logs either on a Simple Log Service server or an OSS server. Enabling encryption does not restrict console accessibility, but do note that encryption and decryption processes may elevate server workload. Therefore, whether to enable this feature should be decided based on your specific business requirements. |

In the **Logstore configuration** step, preview the settings of **Project**, **LogStore**, **Log**
**Details**, **Target Project**, **Target LogStore**, and **Transfer Target Resource Status**.
By default, the **Target Project** and **Target LogStore** are automatically set to match the configurations of your original **Project** and **LogStore** prior to transfer. However, if the logs cannot be transferred to a project bearing the same name or if you have unique needs, you can manually adjust the settings for **Target Project** and **Target LogStore** to accommodate your needs. Click **Complete Create**. The log transfer task is created.

**Appendix 1: RAM role-based authorization**

1. . Log on to the Apsara Uni-manager Management Console by**

**using the administrator credentials of the respective**

**organization**

If you are not authorized to perform this operation, reach out to the administrator of the destination organization (level-1 organization) for assistance.
2. . Create a RAM role and grant the required permissions to the**

**role**

1. Log on to the **Apsara Uni-manager Management Console** .
2. In the top navigation bar, click **Enterprise**. In the left-side navigation pane, choose
**Permissions** > **Role Permissions**.
3. Click **Create Role** in the upper-left corner of the displayed page. In the **Advanced**
**Settings** section, click **Create RAM Role & Attach Policy** .
4. Set **Role Name** to log-dump-role and **Description** to RAM role for platform-side log
transfers. Then, click **Next**.
5. In the **Policy Name** field, enter **log-dump-policy**. Copy the **Permission Policy** content
provided by **Obtain RAM authorization information** on the **Transfer Destination**
**Storage Configuration** page, paste it in the **Policy Content** text box, and then click **OK**.
6. Search for and select the created policy, and then click **Next** in the lower-right corner of the
page.
7. Copy the **Credit Policy** content provided by **Obtain RAM authorization information** on
the **Transfer Destination Storage Configuration** page, paste it in the **Trust Policy** text box, and then click **Next**.
8. Preview and confirm the **Permission Policy** and **Trust Policy** content, and click **Create** in
the lower-right corner.
9. On the **Role Permissions** page, search for **log-dump-role**. Click the role name to go to
the **RAM Role** tab of the role details page. Click **Create**, select the level-1 organization to which you want to transfer logs, and then click **OK**.
0. In the details page of the created **RAM role**, copy the corresponding **ARN**, paste it in the
designated field on the **Transfer Destination Storage Configuration** page, and then complete the authorization.

#### 4.6.4 Log monitoring

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

## 5 Product O&M

This topic lists the products for which you can perform O&M operations in the Apsara Unimanager Operations Console. For more information about O&M operations, see Apsara Unimanager Operations Console Operation Guide.

| Category | Product |
|---|---|
| Computing | Compute Operations Console |
|   | ECS Diagnosis |
|   | BMS Operations Console |
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
| > Document Version: 20251106 | 16 |

|   | Database Backup |
|---|---|
|   | ApsaraDB Operations and Maintenance System |
| Middleware | Tlog |
|   | Global Transaction Service |
|   | CSB |
| Big data | Apsara Bigdata Manager |
|   | Elasticsearch |
|   | Dataphin |
| Security service | Apsara Stack Security |

nagement

## 6 Security management

### 6.1 Security audit

#### 6.1.1 Operation audit

##### 6.1.1.1 Console-based Audit

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

##### 6.1.1.2 CLI-based Audit

You can view the records of operations that are performed in the CLI by users on servers or containers. By default, the operations logs of the previous 24 hours are displayed. You can query the operation records that were generated up to one week ago.
1. Log to the Apsara Uni-manager Operations Console.
nagement
2. In the top navigation bar, choose **Security Management** > **Security Audit** > **Operation**
**Audit**.
3. In the left-side navigation pane, click **CLI-based Audit**.
4. On the **CLI-based Audit** page, perform the following operations based on your business
requirements: Query operation records Select **Log source**, **Linux account**, **Machine/container**, or **Operation Time** and specify a value to view records. You can also click Advanced Filter and specify a combination of the preceding parameters to filter records. Export operation records Select the records that you want to export and click **Export List** to export the selected records. Alternatively, select the check box next to Log source and click Export List to export all records that are displayed on the current page.

> **Note:** You can export a maximum of 10,000 records. If you select more than 10,000 records, only the first 10,000 records are exported.

### 6.2 Host security

#### 6.2.1 Server Guard User Guide

##### 6.2.1.1 Physical server security

###### 6.2.1.1.1 Create and grant permissions to a security administrator account

**security administrator account**

The physical server security feature is used to ensure the security of physical servers on the platform side. This feature requires you to use a dedicated security administrator account for the platform. This topic describes how to create and grant permissions to a security administrator account.
1. Log on to the Apsara Uni-manager Management Console as a system administrator.
For more information, see the **"Log on to the Apsara Uni-manager Management**
**Console"** topic of **Apsara Uni-manager Management Console User Guide** .
nagement
2. Create a dedicated organization that is used to manage the security of physical servers,
and obtain the primary key of the organization.

> **Important:** Make sure that the organization is used only to manage the security of physical servers. Do not add Elastic Compute Service (ECS) instances to the organization.

i. Create the dedicated organization. For more information, see **Enterprise Center > Organization Management > Create**
**Organization** in **Apsara Uni-manager Management Console User Guide** .
ii. Obtain the **primary key** of the newly created organization. For more information, see **Enterprise Center > Organization Management > Obtain**
**the AccessKey pair of an organization** in **Apsara Uni-manager Management**
**Console User Guide**.
3. Create a dedicated account to manage the security of physical servers.
For more information, see **Enterprise Center > User Management > System User**
**Management > Create User** in **Apsara Uni-manager Management Console User**
**Guide**.

> **Note:** When you create the account, take note of the following points for the **organization** and **role**:
> In the **Organization** section, select the organization that is created in the previous step.
> In the **Role** section, select **Platform Security Configuration Administrator** and **Security System Configuration Administrator**.

4. Log on to Apsara Stack Security Center by using the newly created account.
For more information, see Log on to Apsara Stack Security Center.
5. Add the **primary key** of the newly created organization to the protection configuration of
physical servers. i. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Global**
**Platform Security** section, click **Alibaba Cloud Security**.
ii. In the left-side navigation pane, click **Global Settings** iii. On the **Global Settings** page, click the **Physical Machine Protection Configurations** tab. iv. Click **Add Account**. nagement v. In the **Add Physical Machine Server Guard Account** dialog box, configure the
**Username** and **Department UID or Primay Key** parameters.
**Username**: Enter the account that you created in Step 3.
**Primary Key**: Enter the primary key that you obtained in Step 2.
vi. Click **Confirm**.

**Result**

After the settings are complete, you can use the dedicated security administrator account that is created in this section to ensure the security of physical servers on the platform side.

###### 6.2.1.1.2 Physical servers

###### 6.2.1.1.2.1 Manage physical server groups

This topic describes how to manage physical server groups. To facilitate the security management of physical servers, you can add the physical servers to groups and view their security events by group.

**Background information**

By default, physical servers do not belong to a server group. You must add your physical servers to a server group. If you delete a group, all the physical servers in the group are retained but no longer belong to a server group.
1. Log on to Apsara Stack Security Center.
For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
nagement
3. In the left-side navigation pane, choose **Physical Server Security > Servers**.
4. In the left-side group pane, manage sever groups.
Create a group. Click the Add Subgroup icon next to **All Servers** or a specific group, enter a group name, and click **OK**.

> **Note:** The system supports a maximum of three levels of groups.

Modify a group. Click the Modify Group Name icon next to the target group, enter a new name, and click
**OK**.
Delete a group. Click the Delete icon next to the target group. In the message that appears, click **OK**.

> **Note:** After you delete a group, all servers in the group are automatically moved to the **default** group.

Sort groups. Click **Manage Groups** to sort groups in descending order by priority.
5. Change the server group of specific physical servers.
i. Select servers from the list on the right. ii. Click **Change Group**. iii. In the Change Group dialog box that appears, select a group from the drop-down list. iv. Click **OK**.

###### 6.2.1.1.2.2 Manage physical servers

This topic describes how to manage servers. On the Servers page, you can view the status of servers protected by Server Guard. nagement
1. Log on to Apsara Stack Security Center.

> **Note:** For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.

2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Servers**.
4. **Optional:**Search for a server.
To view the agent status of a server, enter the server IP address in the search bar, and click
**Search**. Detailed server information, such as security information, is displayed.
5. View the agent status and detailed security information of the server.
Click in the upper-right corner of the page to select the information columns you want to display. The following table lists the information categories.

| Category | Information |
|---|---|
| Basic information | Server IP/Name Tag OS Region |
| Agent status | Agent Status |
| Threat prevention | Vulnerability Baseline Risk |
| Intrusion detection | Unusual Logons Webshells Suspicious Servers |
| Server fingerprints | Processes Ports Root Accounts/Total Accounts |

6. Manage servers.

| Action | Description |
|---|---|
| Change Group | Select servers and click Change Group to add the selected servers to a new group. |
| Modify Tag | Select servers and click Modify Tag to modify tags for the servers. |
| Security Inspection | Select servers and click Security Inspection to select the items to be checked. |
| Delete External Servers | Select external servers, and choose More > Delete External Servers. |

nagement

| Disable Protection | Select the servers whose agent status is Online, and choose More > Disable Protection. This temporarily disables protection for these servers to reduce server resource consumption. |
|---|---|
| Enable Protection | Select the servers whose agent status is Disable Protection, and choose More > Enable Protection. This enables protection for these servers. |

###### 6.2.1.1.3 Server fingerprints

###### 6.2.1.1.3.1 Manage listening ports

This topic describes how to view information about the listening port of a server. The information helps you identify suspicious listening behavior.

**Background information**

This topic is suitable for the following scenarios: Check for servers that listen on a specific port. Check for ports that a specific server listens.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. On the **Asset Fingerprints** page, click the **Port** tab to view **listening ports**, **network**
**protocols**, and server information.
You can search for a port by using the port number, server process name, server name, or server IP address. In the server information list, you can view the **process**, **IP address**, and **latest scan**
**time** of a server.

###### 6.2.1.1.3.2 Manage software versions

This topic describes how to regularly view and collect the software version information about a server. This helps you check your software assets.

**Background information**

This topic covers the following scenarios: Check for software assets that are installed without authorization. Check for outdated software assets. Locate affected assets if vulnerabilities are detected.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. Choose **Server**
**Security > Sever Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. On the page that appears, click the **Software** tab. On the tab, view all the **software**
nagement
**assets** that are in use and the **number of the servers** that use the software assets.
You can search for specific software by using its name, version, installation directory, server name, or IP address.
5. Click software to view the details, such as the software versions and the servers that use
the software. You can click the icon in the upper-right corner to download a software version table to your computer for subsequent asset check.

###### 6.2.1.1.3.3 Manage processes

This topic describes how to regularly collect the process information on a server and record changes. This way, you can view process information and historical process changes.

**Background information**

This task is suitable for the following scenarios: Check for servers on which a specific process runs. Check for processes that run on a specific server.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. On the page that appears, click the **Process** tab. On the tab, view all running processes
and the number of servers that run these processes. You can search for a process by using the **process name**, **running user**, **startup**
**parameter**, or **server name or IP address**.
5. Click the name of a process to view the details of the process, such as the servers, paths,
and startup parameters.

###### 6.2.1.1.3.4 Manage account information

This topic describes how to regularly collect the account information on a server and record the changes to the accounts. This way, you can check your accounts and view historical changes to your accounts.

**Background information**

You can use the information collected in this topic for the following scenarios: Check for servers on which a specific account is created. Check for accounts that are created on a server.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. On the **Asset Fingerprints** page, click the **Account** tab.
5. View all the logged-on accounts and the numbers of servers on which the accounts are
created. nagement You can search for an account by using the account name, root permissions, server name, or server IP address.
6. Click an account name to view the details, such as the server information, root permissions,
and user group.

###### 6.2.1.1.3.5 Manage scheduled tasks

This topic describes how to view scheduled tasks on servers.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. On the **Asset Fingerprints** page, click the **Scheduled Tasks** tab.
5. View the paths of all tasks and the number of servers that run these tasks.
You can search for a task by using the task path, server name, or IP address.
6. Click a task path to view the details, such as the servers, executed commands, and task
cycles.

###### 6.2.1.1.3.6 Set the fingerprint collection frequency

**frequency**

You can set the frequency at which the data of running processes, system accounts, listening ports, and software versions is collected.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Server Fingerprints**.
4. In the upper-right corner of the **Asset Fingerprints** page, click **Settings**.
5. Select the collection frequency from each drop-down list.
6. Click **OK** to complete the configuration.

###### 6.2.1.1.4 Intrusion events

###### 6.2.1.1.4.1 Intrusion event types

If Server Guard detects sensitive file tampering, suspicious processes, webshells, unusual logons, or malicious processes, it generates alerts. Based on these alerts, you can monitor the security status of your assets and handle potential threats at the earliest opportunity. Apsara Stack Security provides statistics on enabled alerts and defense items. These statistics help you monitor the overall security of your assets. You can view the statistics on the **Intrusions** page.

**Alerts**

The following table describes the alerts. nagement

| Alert | Description |
|---|---|
| Threat intelligence | Identify potential threats to your assets based on the threat intelligence of Apsara Stack Security. Threat intelligence can correlate threat information to analyze and process the information. If threats are detected, threat intelligence can generate alerts. This helps improve the detection efficiency and response speed. Threat intelligence can detect the following items: Malicious domain names Malicious IP addresses IP addresses of dark web services IP addresses of command and control (C&C) servers IP addresses of mining pools Malicious URLs Malicious download sources |
| Unusual Logon | Detect unusual logons to your servers. You can specify approved logon IP addresses, time periods, and accounts. Logons from unapproved IP addresses,time periods, or accounts trigger alerts. You can manually add approved logon locations or configure the system to automatically update approved logon locations. You can also specify assets on which alerts are triggered when unapproved logon locations are detected. Server Guard can detect the following events: Logons to Elastic Compute Service (ECS) instances from unapproved IP addresses Logons to ECS instances from unapproved locations Execution of unusual commands after SSH-based logons to ECS instances Brute-force attacks on SSH passwords of ECS instances |
| Webshell | Use engines developed by Alibaba Cloud to scan common webshell files. Server Guard supports scheduled scan tasks, provides real-time protection, and quarantines webshell files. Server Guard scans the entire web directory early in the morning on a daily basis. A change made to files in the web directory triggers dynamic detection. You can specify the assets on which Server Guard scans for webshells. You can quarantine or ignore detected trojan files. You can also restore the quarantined trojan files. |
| Precision defense | The antivirus feature provides precise protection from common ransomware, DDoS trojans, mining programs, trojans, malicious programs, webshells, and computer worms. |
| Suspicious Account | Detect logons to your assets from unapproved accounts. |
| Cloud threat detection | Detect threats in other cloud services. |
| Persistence | Detect suspicious scheduled tasks on servers and generate alerts when advanced persistent threats (APTs) to the servers are detected. |
| Unusual Network Connection | Detect disconnections or unusual network connections. |
| Suspicious Process | Detect whether suspicious processes exist. |

nagement

| Malicious Process | Scan your servers in real time. An agent is used to collect process information, and the information is uploaded to the cloud for detection. If viruses are detected, alerts are generated. You can handle detected viruses in Apsara Stack Security Center. Server Guard can detect the following malicious activities and processes: Access to malicious IP addresses Mining programs Self-mutating trojans Malicious programs Trojans |
|---|---|
| Sensitive File Tampering | Check whether sensitive files on your servers are maliciously modified. The sensitive files include preloaded configuration files in Linux shared libraries. |
| Other | Detect other types of attacks, such as DDoS attacks. |
| Web Application Threat Detection | Detect intrusions that use web applications. |
| Application intrusion event | Detect intrusions that use system application components. |

###### 6.2.1.1.4.2 View and handle alert events

This topic describes how to view and handle detected alert events on the Intrusions page.

**Background information**

After alert events are detected, the alerts events are displayed on the **Intrusions** page in Apsara Stack Security Center. If the detected alert events are not handled, they are displayed in the **Unhandled Alerts** list on the **Intrusions** page. After the alert events are handled, the status of the alert events changes from **Unhandled Alerts** to **Handled**.

> **Note:** Apsara Stack Security Center retains the records of **Unhandled Alerts** and **Handled** on the **Intrusions** page. By default, the records of **Unhandled Alerts** are displayed.

**View alert events**

1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Intrusions**.
4. On the page that appears, search for or view all alert events. You can also view the details
about the alert events.

**Handle alert events**

1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
nagement
3. In the left-side navigation pane, click **Intrusions**.
4. On the **Intrusions** page, find the alert event that you want to handle and click **Handle** in
the **Actions** column. In the dialog box that appears, configure Process Method and click
**Process Now**.

> **Note:** If the alert event is related to multiple exceptions, the panel that shows alert event details appears after you click **Handle**. You can handle the exceptions in the panel.

**Ignore**: If you ignore the alert event, the status of the alert event changes to **Handled**.
Server Guard no longer generates alerts for the event.
**Add To Whitelist**: If the alert event is a false positive, you can add the alert event to the
whitelist. Then, the status of the alert event changes to **Handled**. Server Guard no longer generates alerts for the event. In the **Handled** list, you can click **Cancel whitelist** to remove the alert event from the whitelist.

> **Note:** When Server Guard generates a false alert on a normal process, this alert is considered a false positive. A common false positive is a **suspicious process** **that sends TCP packets**. The false positive notifies you that suspicious scans on other devices are detected on your servers.

**Batch unhandled**: This method allows you to batch handle multiple alert events. Before
you batch handle multiple alert events, we recommend that you view the details about the alert events.
5. **Optional:**If you confirm that one or more alert events are false positives or need to be
ignored, go to the **Intrusions** page. Then, select the alert events and click **Ignore Once** or
**Whitelist**.

**Export alert events**

1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Intrusions**.
4. In the upper-left corner above the alert event list on the **Intrusions** page, click the
icon to export the list. After the list is exported, the **Done** message appears in the upper-right corner of the Intrusions page.
5. In the **Done** notification of the **Alerts** page, click **Download**.
The alert list is downloaded to your computer.

###### 6.2.1.1.4.3 View exceptions related to an alert

Server Guard supports automatic analysis of exceptions related to an alert. You can click an alert name in the alert list to view and handle all exceptions that are related to the alert. You can also view the results of automatic attack tracing to analyze the exceptions.

**Background information**

Security Center automatically associates alerts with exceptions in real time to detect potential threats. Exceptions related to an alert are listed in chronological order. This allows you to analyze and handle the exceptions to improve the emergency response mechanism of your system. nagement An automatically correlated alert is identified by the icon.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Intrusions**.
4. On the Intrusions page, click the **name of the alert** that you want to handle. The alert
details panel appears.
5. In the alert details panel, view the details and related exceptions of the alert. Then, handle
the exceptions. View alert details You can view the assets that are affected by the alert, the first and latest time when the alert was triggered, and the details about the related exceptions. View affected assets You can move the pointer over the name of an **affected asset** to view the details about the asset. The details include information about all the alerts, vulnerabilities, baseline risks, and asset fingerprints on the asset. View and handle **related exceptions** In the **Related Exceptions** section, you can view the details about all the exceptions that are related to the alert. You can also view suggestions on how to handle the exceptions. Click **Note** to the right of an exception to add a note for the exception. Click the icon to the right of a note to delete the note.

###### 6.2.1.1.4.4 Use the file quarantine feature

Sever Guard can quarantine malicious files. Quarantined files are listed in the Quarantine panel of the Intrusions page. You can restore a quarantined file with a few clicks. However, 30 days after a file is quarantined, the system automatically deletes the file. This topic describes how to view and restore quarantined files.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Intrusions**.
4. In the upper-right corner of the **Intrusions** page, click **Quarantine**.
In the **Quarantine** panel, you can perform the following operations: View information about quarantined files. The information includes server IP addresses, directories in which the files are stored, file status, and modification time. Click **Restore** in the **Actions** column to restore a quarantined file. The restored file appears in the alert list.

###### 6.2.1.1.4.5 Configure alerts

nagement This topic describes how to configure alerts. You can specify approved logon locations and customize web directories to scan.

**Background information**

Server Guard supports advanced logon settings. You can configure more fine-grained logon detection rules. For example, you can specify approved logon IP addresses, logon time ranges, and logon accounts to block unauthorized requests that are sent to your assets.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Intrusions**.
4. In the upper-right corner of the page that appears, click **Settings**.
Configure the parameters on different tabs.

**Add an approved logon location**

a. In the **Login Location** section, click **Management** on the right. b. Select the logon location that you want to specify as the approved logon location and select the servers that allow logons from the specified location. c. Click **Ok**. Server Guard allows you to **edit** or **delete** approved logon locations that you have specified. To change the servers that allow logons from an approved location, find the approved location and click **Edit** on the right. To delete an approved logon location, find the logon location and click **Delete** on the right.

**Configure advanced logon settings**

> **Note:** When you configure advanced logon settings, you can specify the IP addresses, accounts, and time ranges that are allowed for logons to your assets. After the advanced logon settings are configured, Server Guard generates alerts if your assets receive unauthorized logon requests. The procedure of configuring advanced logon settings is similar to the procedure of configuring **Login Location**. You can **add**, **edit**, or **delete** advanced logon settings in a similar manner.

Turn on or turn off Uncommon IP Alert to the right of **Common Login IPs**. If you turn on Uncommon IP Alert and your assets receive logon requests from unapproved IP addresses, alerts are triggered. Turn on or turn off Uncommon Time Alert to the right of **Common Login Time**. If you turn on Uncommon Time Alert and your assets receive logon requests during unapproved time ranges, alerts are triggered. Turn on or turn off Uncommon Account Alert to the right of **Common Login Accounts**. If you turn on Uncommon Account Alert and your assets receive logon requests from unapproved accounts, alerts are triggered.

**Add web directories to scan**

Server Guard automatically scans web directories of data assets in your servers and runs dynamic and static scan tasks. You can also manually add other web directories. a. In the **Add Scan Targets** section, click **Management** on the right. nagement b. Specify a valid web directory and select the servers on which the specified web directory is scanned.

> **Note:** To ensure the scan performance and efficiency, we recommend that you do not specify a root directory.

c. Click **Ok**.

###### 6.2.1.1.5 Log retrieval

###### 6.2.1.1.5.1 Supported log sources and fields

This topic describes the log sources and fields that are supported by the log retrieval feature. The log retrieval feature allows you to query the following types of log sources. You can click a log source link to view the fields that can be retrieved.

| Log source | Description |
|---|---|
| Logon history | Log entries about successful system logons |
| Logs of brute-force attacks | Log entries about failed system logons during brute-force attacks |
| Process snapshot logs | Log entries about processes on a server at a specific point in time |
| Logs of listening port snapshots | Log entries about listening ports on a server at a specific point in time |
| Account snapshot logs | Log entries about account-based logons on a server at a specific point in time |
| Process startup logs | Log entries about process startups on a server |
| Network connection logs | Log entries about active connections from a server to the Internet. |

**Logon history**

The following table describes the fields that you can use to query the logon history.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| warn ip _ | string | The source IP address used for the logon. |
| warn port _ | string | The logon port. |
| warn user _ | string | The username used for the logon. |
| warn type _ | string | The logon type. |

nagement

| warn count _ | string | The number of logon attempts. |
|---|---|---|

**Logs of brute-force attacks**

The following table describes the fields that you can use to query logs of brute-force attacks.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| warn ip _ | string | The source IP address of the attack. |
| warn port _ | string | The target port of the attack. |
| warn user _ | string | The target username of the attack. |
| warn type _ | string | The attack type. |
| warn count _ | string | The number of brute-force attack attempts. |

**Process startup logs**

The following table describes the fields that you can use to query process startup logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| pid | string | The ID of the process. |
| groupname | string | The user group. |
| ppid | string | The ID of the parent process. |
| uid | string | The ID of the user. |
| username | string | The username. |
| filename | string | The file name. |
| pfilename | string | The name of the parent process file. |
| cmdline | string | The command line. |
| filepath | string | The path of the process file. |
| pfilepath | string | The path of the parent process file. |

**Logs of listening port snapshots**

nagement The following table describes the fields that you can use to query logs about listening port snapshots.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| src port _ | string | The listening port. |
| src ip _ | string | The listening IP address. |
| proc path _ | string | The path of the process file. |
| pid | string | The ID of the process. |
| proc name _ | string | The name of the process. |
| proto | string | The protocol. |

**Account snapshot logs**

The following table describes the fields you can use to query account snapshot logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| perm | string | Indicates whether the user has root permissions. |
| home dir _ | string | The home directory. |
| warn time _ | string | The time when a password expiration notification is sent. |
| groups | string | The group to which the user belongs. |
| login ip _ | string | The IP address of the last logon. |
| last chg _ | string | The time when the password was last changed. |
| shell | string | The Linux shell command. |
| domain | string | The Windows domain. |
| tty | string | The logon terminal. |
| account expire _ | string | The time when the account expires. |
| passwd expire _ | string | The time when the password expires. |

nagement

| last logon _ | string | The last logon time. |
|---|---|---|
| user | string | The username. |
| status | string | The account status. Valid values: 0: disabled 1: normal |

**Process snapshot logs**

The following table describes the fields that you can use to query process snapshot logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| path | string | The path of the process file. |
| start time _ | string | The time when the process was started. |
| uid | string | The ID of the user. |
| cmdline | string | The command line. |
| pname | string | The name of the parent process. |
| name | string | The name of the process. |
| pid | string | The ID of the process. |
| user | string | The username. |
| md5 | string | The MD5 hash value of the process file. If the size of the process file exceeds 1 MB, the system does not calculate the MD5 hash value of the process file. |

**Network connection logs**

The following table describes the fields that you can use to query network connection logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| src ip _ | string | The source IP address. |
| src port _ | string | The source port. |

nagement

| proc path _ | string | The path of the process file. |
|---|---|---|
| dst port _ | string | The destination port. |
| proc name _ | string | The name of the process. |
| dst ip _ | string | The destination IP address. |
| status | string | The status. |

###### 6.2.1.1.5.2 Logical operators

The log retrieval feature supports multiple search conditions. You can add multiple logical operators to one search condition for one log source, or combine multiple search conditions for several log sources by using different logical operators. This topic describes the logical operators that are supported in log retrieval. Examples are provided to help you understand these operators. The following table describes the logical operators that are supported in log retrieval. Table 1.

| Logical operator | Description |
|---|---|
| and | Binary operator. This operator is in the format of query 1 and query 2 , which indicates the intersection of the query results of query 1 and query 2 . Note If no logical operators are used for multiple keywords, the default operator is AND. |
| or | Binary operator. This operator is in the format of query 1 or query 2 , which indicates the union of the query results of query 1 and query 2 . |
| not | Binary operator. This operator is in the format of query 1 not query 2 , which indicates the results that match query 1 but do not match query 2 . This format is equivalent to query 1 - query 2 . Note If you use only not query 1 , the log data that does not contain the query results of query 1 is returned. |

|   | query 1 not query 2 |   |
|---|---|---|
| query 1 |   |   |

###### 6.2.1.1.5.3 Query logs

This topic describes how to search for and view physical server logs.
1. Log on to Apsara Stack Security Center.
nagement

> **Note:** For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.

2. In the upper-right corner of Apsara Stack Security Center, click **Security**.In the **Server**
**Security** section, click **Server Guard**.
3. In the left-side navigation pane, click **Log Retrieval**.
4. Specify search conditions.

> **Note:** For more information about log sources, log fields, and logical operators, see Supported log sources and fields and Logical operators.

5. Click **Search** and view the search result.
**Reset**: Click **Reset** to clear the search condition configurations.
**Save Search**: Click **Save Search** to save the search condition configurations which you
can use to search for logs in the future.
**Saved Searches**: Click **Saved Searches** to select and use a search condition that you
saved.

###### 6.2.1.1.6 Configure security settings for physical servers

**servers**

This topic describes how to configure security settings for physical servers. You can enable or disable periodic trojan scans. You can also specify the working mode of the Server Guard agent.
1. Log on to Apsara Stack Security Center.

> **Note:** For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.

2. In the left-side navigation pane, choose **Physical Server Security > Settings**.
3. Enable periodic trojan scans for physical servers.
i. In the Trojan Scan section, click **Manage**. ii. In the All Servers section, select the physical servers on which you want to perform periodic trojan scans. Then, click the rightwards arrow. iii. Click **OK**.
4. On the **Protection First Mode** page, click **Manage** next to Protection Mode.
Configure protection modes for servers. nagement
**Business First Mode**: In this mode, the peak CPU utilization is less than 10%, and the
peak memory usage is less than 50 MB.
**Protection First Mode**: In this mode, the peak CPU utilization is less than 20%, and the
peak memory usage is less than 80 MB.

### 6.3 Network security

#### 6.3.1 Network Security Management Center

##### 6.3.1.1 East-west security management

###### 6.3.1.1.1 Policy center

###### 6.3.1.1.1.1 Policy content management

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

nagement View the CIDR block whitelist: click **Advanced Filter** and filter CIDR blocks by **CIDR**
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

nagement

| Account Name | Enter the ID of the account to which the VPC belongs. |
|---|---|
| Access Components | Select components that can be accessed by the VPC. You can specify multiple components. pop-inner asapi-inner sls-inner docker-registry |
| Region | Select the region where the VPC whitelist takes effect. |

View the VPC whitelist: Click **Advanced Filter** and filter VPCs by **VPC Name**, **VPC ID**,
**Tunnel ID**, **IP Address**, **VPC Account**, **VPC-Owned Products**, and **Access**
**Components**.
nagement
6. On the **SLB Backend Mount Range Whitelist** tab, perform the following operations:
View the scope of backend servers that can be attached to the SLB instance on the tenant side. Manage the scope of backend servers that can be attached to the SLB instance on the tenant side: Find the policy that you want to manage and click **Edit** in the **Operation** column. In the dialog box that appears, modify the policy content, and click **OK**.

> **Important:** This operation is risky. Check with the on-site security manager before modify the policy.

The format of the policy attribute is {"$AliUid":["cidr1", "cidr2"]}.

> By default, you can attach only resources that belong to the tenant, such as Elastic Compute Service (ECS) resources. After this, you can attach user resources such as offline data centers and server NC.
> You cannot add the internal address of the cloud platform or CIDR blocks such as 0.0.0.0 or X.0.0.0/8 to the whitelist.

nagement

###### 6.3.1.1.1.2 VIP protection

> Platform VIP security protection includes classic network VIP and AnyTunnel VIP security protection policies. This feature is used to limit the access scope of classic network VIP and AnyTunnel VIP to avoid security risks caused by excessive open access scope.

**Background information**

Classic network VIP protection: By using the ACL capability of SLB, the classic network VIP can only be accessed by the base classic network. AnyTunnel VIP protection: For AnyTunnel VIPs provided by the platform, you can configure a VPC whitelist by using the ACL capability of SLB to allow access only from trusted VPCs.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Network Security** >
**Network Security Management Center**.
3. In the left-side navigation pane, choose **East-west Security Management** > **Policy**
**Center** > **VIP Security**.
4. On the **Classic network VIP** tab, perform the following operations:
Click **Edit** to modify the **Classic network VIP control policy status**.
**Enable**: automatically issues the access control policy to new classic network VIPs. If
you set this parameter to Enable, only CIDR blocks in the whitelist can be used.
**Close**: does not issue the access control policy to new classic network VIPs. This
setting may incur security risks.
**Observation mode**: checks the sources of all VIPs and blocks abnormal requests. If
the system blocks a normal request from the cloud platform network, the system automatically disables the observation mode and set the VIP status to Disabled. View the whitelist policy of a classic network VIP. a. Click **Advanced Filter** to obtain the whitelist policy information of the classic network VIP by **LB ID**, **VIP IP**, **VPC Ownership**, and **Status**. b. Click **CIDR block whitelist** in the **Policy Content** column corresponding to the desired classic network VIP. You are redirected to the **CIDR block whitelist** tab on the
**Policy Content Management** page.
Enable the whitelist policies for classic network VIPs nagement

> **Note:** When the **Status** of the whitelist policy of the classic network VIP is **Disabled**, and the content in the **Description** column is not **The current VIP has been bound to** **another ACL policy, and the whitelist policy cannot be issued.** You can enable the whitelist policy of the classic network VIP.

Enable the whitelist policy for a single VIP: Click **Enable** in the **Operation**column corresponding to the desired classic network VIP. In the dialog box that appears, confirm the information and click **OK**. Batch enable: Select multiple classic network VIPs and click**Enable**below the list. Disable the whitelist policies for classic network VIPs.

> **Note:** If the **Status** of the whitelist policy of the classic network VIP is **Enabled**, you can disable the whitelist policy of the classic network VIP.
> If you disable the whitelist policy, the classic network VIP does not have security control policies. This poses security risks.

Disable the whitelist policy for a single VIP: Click **Disable** in the **Operation**column corresponding to the desired classic network VIP. In the dialog box that appears, confirm the information and click **OK**. Batch disable: Select multiple classic network VIPs and click**Disable**below the list. View the logs of classic network VIP policies. a. Click **View Logs** in the **Operation** column of the desired classic network VIP control policy. b. Obtain the log information, including **Instance ID**, **Lvs machine IP**, **Packet loss**,
**Associate VIP**, **VIP Port**, **Associate a VPC**, and **Request time**.
Disable all existing VIP control policies.

> **Important:** If you select this option, access control policies issued to all VIPs are disabled. This imposes security risks. If you want to re-enable the VIP security feature after you disable all existing VIP control policies, you must manually enable it for each LB. We recommend that you perform this operation with caution.

a. Click **All existing VIP policies are disabled**. b. In the message that appears, click **OK**.
5. On the **AnyTunnel VIP** tab, perform the following operations:
Click **Edit** to modify the **AnyTunnel VIP control policy status** .
**Enable**: automatically issues the access control policy to new AnyTunnel VIPs. If you
set this parameter to Enable, only CIDR blocks in the whitelist can be used.
**Close**: does not issue the access control policy to new AnyTunnel VIPs. This setting
may incur security risks.
**Observation mode**: checks the sources of all VIPs and blocks abnormal requests. If
the system blocks a normal request from the cloud platform network, the system automatically disables the observation mode and set the VIP status to Disabled. nagement View the whitelist policy information of AnyTunnel VIPs. If the AnyTunnel VIP is enabled, the VIP can be accessed from VPCs and Tiangong in the whitelist. If the AnyTunnel VIP is disabled, the VIP can be accessed from Tiangong. If classToAnyTunnel types of VIPs are enabled, they can be accessed from VPCs and Tiangong in the whitelist. If they are disabled, they can be accessed from all VPCs without a whitelist policy. a. Click **VPC whitelist** in the **Policy content** column of the desired AnyTunnel VIP. b. On the **VPC Whitelist** tab of the **Policy Content Management** page, obtain the VPC whitelist information. Enable whitelist policies for AnyTunnel VIPs.

> **Note:** If the **Status** of the whitelist policy for an AnyTunnel VIP is **Disabled**, you can enable the whitelist policy for the AnyTunnel VIP.
> The Enable action allows VPCs in the VPC whitelist to access this AnyTunnel VIP.

Enable the whitelist policy for a single VIP: Click**Enable** in the **Operation** column corresponding to the desired AnyTunnel VIP. In the dialog box that appears, confirm the information and click **OK**. Batch enable: Select multiple AnyTunnel VIPs and click **Enable**below the list. Disable whitelist policies for AnyTunnel VIPs.

> **Note:** If the **Status** of the whitelist policy for an AnyTunnel VIP is **Enabled**, you can disable the whitelist policy for the AnyTunnel VIP.

You cannot manually disable the anyTunnelVIP of ASAPI and POP. If you disable the whitelist policy for an AnyTunnel VIP, the AnyTunnel VIP does not have security control policies. This poses security risks. Disable the whitelist policy for a single VIP: Click**Disable** in the **Operation** column corresponding to the desired AnyTunnel VIP. In the dialog box that appears, confirm the information and click **OK**. Batch disable: Select multiple AnyTunnel VIPs and click**Disable**below the list. View the access control logs of AnyTunnel VIPs. nagement a. Click **View Logs** in the **Operation** column of the desired AnyTunnel VIP control policy. b. Obtain the log information, including **Instance ID**, **Lvs machine IP**, **Packet loss**,
**Associate VIP**, **VIP Port**, **Associate a VPC**, and **Request time**.

###### 6.3.1.1.2 DNS rules

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
| SOURCE Type | The source type of the DNS forwarding rule. Classic Network VPC |
| CIDR Block | The CIDR block of the DNS forwarding rule. |
| Domain Name Range | The domain name range of the DNS forwarding rule. Global All O & M standard scope Tenant standard scope NTP server |
| VPC Name | This parameter takes effect only when you set SOURCE Type to VPC. The name of the VPC. |
| VPC ID | This parameter takes effect only when you set SOURCE Type to VPC. The ID of the VPC. |

nagement

| Product | This parameter takes effect only when you set SOURCE Type to VPC. The name of the product. |
|---|---|
| Account Name | This parameter takes effect only when you set SOURCE Type to VPC. The aliUid of the user. |

6. Click **Advanced Filter** to filter forwarding rules by **Domain name range**, **Network**
**segment**, **IP address**, **VPC name**, and **VPC ID**.

**What to do next**

**Delete a rule**

> **Note:** The default rules cannot be deleted.

nagement Delete a single rule: Click **Delete** in the **Operation** column of the desired rule. In the dialog box that appears, click **OK**. Batch delete: Select multiple rules and click **Delete** below the list.

**View the logs**

1. Click **View Logs** in the **Operation** column of the desired rule.
2. Obtain the log information, including **Whether to hit the ACL policy** , **Parsing result**,
**Client IP**, **Access time**, and**Access domain name**.

###### 6.3.1.1.3 Device network access management

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

nagement

| Trust duration | The trust duration. The minimum value is one day. If you select Permanent, the address is permanently trusted. |
|---|---|
| White reason | The reason why the device is trusted. |

7. On the **Add a trusted MAC address** tab, click **Add a whitelist**. In the dialog box that
appears, configure the parameters as described in Step 6 and click **OK**.

### 6.4 Account security

#### 6.4.1 Linux account management

##### 6.4.1.1 Password management for root user

You can use the Root Password Management page to manage passwords of root users of all physical servers and Kernel-based Virtual Machines (KVMs) in the Apsara Stack environment, including updating and rotating passwords.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, click **Password Management for Root**.
4. On the **Password management** tab, perform the following operations to view information
about all physical servers and Kernal-based Virtual Machines (KVMs) in the Apsara Stack environment: Query the information about a physical server or KVM. nagement a. Filter machines by **Product**, **Server Name**, and **IP**. The following figure provides an example on the information about physical servers and KVMs that you can view on the Password management tab. b. If you click the icon next to a password in the **Password** column, the password is displayed in plaintext for 10 seconds. Update a password To update the password of a physical server or KVM, perform the following operations: Find the physical server or KVM for which you want to update the password and click
**Update password** in the **Operation** column. In the Update password dialog box,
specify the new password that you want to use for the physical server or KVM twice and click **OK**. To update the passwords of multiple physical servers or KVMs at a time, perform the following operations: Select multiple physical servers or KVMs for which you want to update the passwords and click **Batch update** in the lower part of the page. In the Update password dialog box, specify the new password that you want to use for the physical servers or KVMs twice and click **OK**.

> **Note:** The password must be 8 to 30 bits in length and must contain digits, lowercase letters, uppercase letters, and special characters.
> Make sure that the same password is entered twice.

Configure a password expiration period To configure the password expiration period for a physical server or KVM, perform the following operations: Find the physical server or KVM for which you want to configure the password expiration period and click **Configuration** in the **Operation** column. In the Configuration Items dialog box, specify a password expiration period and click **OK**. To configure the password expiration periods for multiple physical servers or KVMs at a time, perform the following operations: Select multiple physical servers or KVMs for which you want to configure the password expiration periods and click **Set Passwords** in the lower part of the page. In the Configuration Items dialog box, specify a password expiration period and click **OK**.

> **Note:** The valid password expiration period ranges from 1 day to 180 days.

5. On the **Password history** tab, view the password update records of all physical servers
and KVMs in the Apsara Stack environment. nagement You can obtain the password history of a machine by configuring the **Product**, **Server**
**Name**, and **IP** parameters. If you click the
icon next to a password in the **Password** column, the password is displayed in plaintext for 10 seconds.
6. On the **Configuration** tab, view and modify the password configuration policies of physical
servers and KVMs. Click **Submit** to update the configuration policies. The following table describes the parameters that you can configure.

| Parameter | Description |
|---|---|
| Enable Password Policy Configuration | Specifies whether to enable password policy configuration. If you turn on this switch, you can modify the configuration policy of server or KVM passwords, such as password updates and automatic rotation. If you turn off this switch, you cannot modify the configuration policy of server or KVM passwords, such as password updates and automatic rotation. |
| Initial Password | The password that is assigned to a physical server or a KVM when the server or KVM is deployed in the Apsara Stack environment. |
| Password Length | The maximum length of an automatically updated password. |
| Retry Times | The number of retries after the password fails to be updated. |
| Password rotation switch | Specifies whether to enable automatic password rotation. If you turn on this switch, automatic password rotation is enabled. If you turn off this switch, automatic password rotation is disabled. |

nagement

##### 6.4.1.2 SSH key management

This feature allows you to view and manage SSH keys on physical machines, KVMs, and containers in Apsara Stack. This feature allows you to view full keys, query key validation records and usage records, and manage temporary keys.

**Prerequisites**

You have obtained the permissions to manage SSH keys on the hosts. The Tianji-sshtunnel service is in desired state.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, click **SSH Key Management**.
4. On the **Full key** tab, you can filter key fingerprints by **Public key status**, **Private key**
**status**, and **Key fingerprint**. You can search for a key fingerprint by fuzzy search.
In the **Effective machine** column that corresponds to a key fingerprint, click Public key or Private key. In the panel that appears, you can view the **Public key** and **Private key** information. The public key information includes the **Public key** and **Creation Time**. The Private key information includes **Machine name**, **User**, **Key path**, **Container ID**,
**Status**, and **Creation time**.
Click **Usage record** in the **Operation** column that corresponds to a key fingerprint. In the panel that appears, view the **Source**, **Destination**, and **Usage time** of the key.
5. On the **Temporary Key** tab, create a temporary channel to obtain temporary keys.
nagement Click **Create a temporary channel** . In the dialog box that appears, configure the following parameters and click **Create**.

| Parameter | Description |
|---|---|
| Channel name | The name of the temporary channel. |
| Validity period | Select Start Date and End Date for the temporary channel. |
| Machine definition mode | Select the delineation method of the target machine. Valid values: Product dimension Physical machine dimension Full machines (including physical machines managed by Tianji, dockerVM, and KVM) |
| Product | This field takes effect only when you set Machine definition mode to Product dimension. Fuzzy match is supported. |
| SR | This field takes effect only when you set Machine definition mode to Product dimension. You can select multiple server roles from the drop-down list. |
| Machine name | This field takes effect only when you set Machine Definition mode to Physical machine dimension. The name of the server. Fuzzy match is supported. |

nagement You can also perform the following related operations:

| Operation | Description |
|---|---|
| View temporary channels | a. Click Advanced Filter to obtain the information of a channel by Channel name, Key fingerprint, Public key status, and Private key status. b. Click the number in the Public key effective machine/expected machine column corresponding to a temporary channel. In the panel that appears, you can view the information of machines whose public keys are effective, including Machine name, Container ID, User, Key path, and Status. |
| Clone a temporary channel | a. Click Clone in the Operation column corresponding to a temporary channel. In the dialog box that appears, you can view a temporary channel with the same configurations. b. Modify the parameters based on your requirements and clickC reate. |
| View execution records | a. Click Execution record in the Operation column corresponding to a temporary channel. b. On the Task Execution Records page, you can obtain the execution record details. |

nagement

| Modify the validity period | a. Click Modify validity period in the Operation column corresponding to a temporary channel. b. In the Modify validity period dialog box, specify a new validity period for the temporary channel and click OK. The maximum validity period is 90 days. Note When the validity period of a temporary channel expires, you cannot modify the validity period. |
|---|---|

##### 6.4.1.3 System user management

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

nagement
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
nagement b. In the panel that appears, view the server role information for the deployment, including the **product**, **service**, **sr**, **User trust status**, and **Password trust status**. c. In the Operation column, click **Trust User** or **Trust Password** to add a user to the trust status. Click **Untrust User** or **Untrust Password** to cancel the trust.

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

nagement

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

nagement

| Machine name | This field takes effect only when you set Machine definition mode to Physical machine dimension. The name of the server. Fuzzy match is supported. |
|---|---|

You can also perform the following related operations:

| Operation | Description |
|---|---|
| View temporary user information | a. Enter a keyword in the Username field to obtain the user information. b. Click the number in the Effective machine/expected machine column that corresponds to the target temporary user. In the panel that appears, you can view the list of effective machines, including Machine name, Container ID, User home directory, and Creation time. |

nagement

| Clone a temporary user | a. Click Clone in the Operation column that corresponds to the temporary user. In the dialog box that appears, you can view a temporary user with the same configurations. b. Modify the parameters as required and click OK. |
|---|---|
| View the details of a task | a. Find the temporary user that you want to view and clickE xecution details in the Operation column. b. On the Task Execution Records page, you can obtain the execution record details. |
| Configure the validity period of a temporary user | a. Click Set Validity Period in the Operation column that corresponds to a temporary user. b. In the dialog box that appears, modify the validity period of the temporary user and then click OK. The validity period can be up to 90 days. Note When the validity period of a temporary user expires, you cannot modify the validity period. |

##### 6.4.1.4 Linux account management task

###### 6.4.1.4.1 Task template management

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

nagement

| Task Template name | The name of the custom task template. |
|---|---|
| Task type | The type of the rotation task. Only SSH key rotation is supported. |
| Trigger mode | The trigger mode of the rotation task. You can select Manual trigger or Automatic trigger. |
| Trigger cycle | This field is displayed only when you set Trigger mode to Automatic trigger. Specify the cycle and next execution time of the automatic rotation task. Note Valid values: 7 to 365. Unit: days. |
| Cross-Region | Specifies whether to support cross-region rotation tasks. |
| Select SSH key | Enter the SSH key. |

5. In the **Configure task phase** section, select a task phase.

> **Note:** If you set **Trigger mode** to **Manual trigger**, you can specify whether to select the **Grayscale remove the original private key** phase.

nagement
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

###### 6.4.1.4.2 Task execution records

You can view the records of all historical rotation tasks, including global password-free channel removal tasks, OPS emergency O&M channel creation tasks, temporary channel creation tasks, and rotation tasks for updating the SSH keys. You can view all historical key pairs, update operations, and points in time of the updates.

**Prerequisites**

You have obtained the permission to operate the task execution records of the host. nagement The Tianji-sshtunnel service has reached the desired state.

**Background information**

You may need to manage SSH key pairs across multiple regions. In this case, a rotation task have subtasks. The name of a subtask is suffixed with the region where the SSH key pair is used. You can distinguish subtasks by the suffix. You can also use the subtask name to identify the parent rotation task to which the subtask belongs. A subtask is always synchronized with its parent task in status. The subtask status cannot be manually modified. All execution stages of a parent task are displayed after the task is created. The execution stages of a subtask are fully displayed only after all stages of the parent task are complete. When the parent task is running, you can view only the completed stages and the ongoing stage of the subtask.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Account Security** > **Linux**
**Account Management**.
3. In the left-side navigation pane, choose **Linux Account Management Task** > **Task**
**Execution Records**.
4. Click **Advanced Filter** to filter execution records by **Task ID**, **Task template ID**, **Task**
**Template name**, and **Current execution status**.
5. Find the task execution record that you want to view and click **Details** in the **Operation**
column. In the panel that appears, you can view the details of the task execution record.

**Related operations**

**Pause a rotation task**

> **Note:** You can pause a rotation task when the **Task execution status** is **Running**.

1. Find the rotation task that you want to pause and click **Pause** in the **Operation** column.
2. In the message that appears, click **OK**.

**Continue a rotation a task**

nagement

> **Note:** If the **Task execution status** is **Paused**, you can continue to rotate the task.

1. In the **Operation** column that corresponds to the rotation task, click **Continue**.
2. In the message that appears, click **OK**.

**Roll back a rotation task**

> **Note:** When the task type is **SSH key rotation** (including cross-region tasks) or **Global** **password-free removal** (including cross-region tasks), you can roll back the rotation task.

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

nagement

**Obtain an execution instance**

1. Click **Execute an instance** in the **Operation** column that corresponds to the rotation task.
You can also click the ID in the **Task ID** column that corresponds to the rotation task.
2. On the **Task execution instance** page, view the information about the instance based on
the **Target machine**, **Task phase**, and **Current execution status**.
3. Find the instance that you want to view and click **Details** in the **Operation** column. In the
panel that appears, you can view the details of the task execution instance.

> **Note:** If the **Instance execution status** is **Failed** or **Timeout Failed**, you can perform the following operations:
> Click **Retry** in the **Operation** column. In the message that appears, click **OK** to retry the selected task instance.
> Click **Skip** in the **Operation** column. In the message that appears, click **OK** to skip the current task execution instance.

nagement

#### 6.4.2 Account management for cloud services

**services**

##### 6.4.2.1 Account ACL control

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
information about the desired virtual private cloud (VPC). nagement

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

nagement
1. Find the desired account and click **Intercept logs** in the **Operation** column.
2. View information about the logs of requests that are blocked by the policy. The information
includes **Call Source**, **Client observation mode**, **Authentication method**,
**Authentication AK**, **Request IP**, **VPC ID**, **Authentication result**, **Policy status**, and
**Interception time**.

**Disable existing access control policies for AccessKey pairs**

> **Important:** You can click a button to disable existing access control policies for AccessKey pairs. After the existing access control policies are disabled, the security control capability for the request sources of platform accounts becomes unavailable. This incurs security risks. If you want to enable the account ACL control feature after the existing access control policies are disabled, you must enable the feature for the AccessKey pairs one by one. Therefore, exercise caution before you click the button.

1. Click the button on the left of the Account ID drop-down list above the account list.
2. In the message that appears, click **OK**.

##### 6.4.2.2 Service boundary

###### 6.4.2.2.1 ACL

The Account ACL control page displays the whitelist policies associated with platform accounts. If you want to examine the specifics of an API control policy, simply click its ID.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security** > **Account Security** > **Cloud Product**
**Account Management**.
3. In the left-side navigation pane, choose **Service Boundary** > **Control Policies**.
4. Click **Advanced Filter** and search for desired API control policies by a combination of **API**
**control policy ID**, **uid**, **Policy type**, **Account ownership**, and **Creation time**.
5. Click the ID of the desired API control policy. On the page that appears, you can view the
details of the API control policy. nagement

###### 6.4.2.2.2 O&M

You can manage the O&M switch for service boundaries.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security** > **Account Security** > **Cloud Product**
**Account Management**.
3. In the left-side navigation pane, choose **Service Boundary** > **O & M switch**.
4. Click **Edit**, select the status of the **Service boundary O & M switch**, and then click **Save**.
**Enable**: enables service boundary control for all accounts, including the new platform
accounts.
**Close**: disables service boundary control for existing or new platform accounts.
**Observation mode**: authenticates requests sent from new and existing platform
accounts. The system records the failed authentication logs and allows the requests.

### 6.5 Access control

#### 6.5.1 Security policies

You can modify the account policies and password policies of the current account in the Security Policies module.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Security**
**Strategy**.
3. On the **Account Policy** tab, configure the parameters and click **Submit**. The following
table describes the parameters. nagement

| Parameter | Description |
|---|---|
| Timeout Period (Minutes) | Specify a logon timeout period for the current account. If the logon time exceeds the specified time period, the system prompts you that the logon timed out and you can try to log on again. Valid values: 10 to 180. |
| Multi-Terminal Logon Settings | Specify whether the current account allows simultaneous logon from multiple terminals. |
| ASO account validity period (days) | Specify the validity period of the current account. If the account is expired, the system locks this account and only the security administrator can unlock the account. Valid values: 10 to 365. |
| Account Freeze Policy (Days) | Specify the period during which the current account remains available. If the specified period elapses, the system freezes this account. Valid values: 0: indicates that the account freezing policy is disabled. 10~365 |
| Security Policy Is Valid for Preset Accounts | Specify whether the security policy is valid for preset accounts. On: If a security policy expires (for example, the account or password expires), preset accounts cannot log on to the system. We recommend that you set a long validity period. Off: If a security policy expires, preset accounts can still log on to the system. Preset accounts never expire. Default value: Off. |

nagement
4. Click the **Password policy** tab, configure the parameters, and click **Submit**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Minimum Password Length | Specify the minimum number of characters in the password. Valid values: 10 to 20. |
| Required Character Types in Password | Select one or more character types that must be contained in the password. Lowercase Letters Uppercase Letters Digits Special Characters |
| Logon Disabled After Password Expires | Specify whether to prohibit the current account from logging on to the system after the password expires. Yes No |
| Reminder time before password expiration (days) | Set the time to send a reminder before the password of an account expires. For example, a value of 10 indicates that the expiration reminder is sent 10 days before the password expires when the user logs on. A value of 0 indicates that no reminder is sent. Valid values: 0 to 30. |

| sara Uni-manager Operations nsole User Guide·Security ma gement |   |
|---|---|

| Password Validity (Days) | Specify the validity period for the password. If the password expires, the system sends a notification to the user. 0 indicates that the password does not expire. Valid values: 0 to 1095. |
|---|---|
| Password History Check | Specify the number of historical passwords that you cannot reuse. For example, if you set this parameter to 3, the most recent three historical passwords cannot be reused. 0 indicates that all historical passwords can be reused. Valid values: 0 to 24. |

#### 6.5.2 Logon policies

As an administrator, you can configure logon policies to manage the logon time and logon IP addresses of users.

**Background information**

The system provides a default policy. You can also configure custom logon policies based on your business requirements to control the read and write permissions of users and improve the security of the system.

**Add a policy**

1. Log on to the Apsara Uni-manager Operations Console.
nagement
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

nagement

**Related operations**

**Query a policy**

You can query the information about a logon policy by **policy name**.

**Modify a policy**

1. Find the logon policy that you want to modify and click **Modify** in the **Actions** column.
2. In the Modify policy dialog box, modify the configurations and click **OK**.

**Delete a policy**

1. Find the logon policy that you want to delete and click **Delete** in the **Actions** column.
2. In the message that appears, click **OK**.
nagement

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

#### 6.5.3 Two-factor authentication

To make user logons more secure, you can configure two-factor authentication for users.

**Background information**

The Apsara Uni-manager Operations Console supports only **Google two-factor**
**authentication**. After you enable two-factor authentication and add a key, you can use the
random verification code generated by the authentication app for logon. This ensures the security of your account.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Security Management** > **Access Control** > **Two-**
**factor Authentication**.
3. In the upper part of the Two-factor Authentication page, specify an authentication method.
The following authentication methods are provided:

**Google two-factor authentication**

nagement Add a key a. In the upper-right corner of the Two-factor Authentication page, click **Add Key**. In the dialog box that appears, specify a username and click **OK**. The specified user is displayed in the user list. b. Click **Add Key** in the **Actions** column. If the **The operation is successful** message occurs, a key is added to the user and **Show Key** is displayed in the **Actions** column. c. If you click **Show Key**, the key is displayed in plaintext. If you click **Hide Key**, the key is displayed in ciphertext. Delete a key a. Find the user for whom you want to delete the key and click **Delete Key** in the
**Actions** column.
b. In the message that appears, click **OK**.

**No authentication**

If you select **No Authentication**, two-factor authentication is disabled and all two-factor authentication methods become invalid. ngs

## 7 System settings

### 7.1 Authorization Information

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

ngs

| Authorization Type | The current authorization type and authorization status. The following authorization types are available: Trial Authorization Formal Authorization The following authorization states are available: Not Activated About to Expire Taking Effect Expired Expired/Excess |
|---|---|
| Customer ID | The unique ID of the customer. |
| Instance ID | The ECS instance ID in the deployment planner of the field environment. |
| UID | The unique ID of the user. |
| Cloud Platform Version | The Apsara Stack version of the current cloud platform. |
| Customer Name | The name of the customer who purchased the Apsara Stack service. |
| Authorization Created At | The start time of the authorization. |

You can view the authorization information of cloud services in different regions. The following table describes the authorization details.

| Parameter | Description |
|---|---|
| Product Name | The name of the cloud service. |

ngs

| Product Specification Name | The specification of the cloud service. |
|---|---|
| Authorization Mode | The authorization mode of the cloud service. Authorization Mode Subscription Mode Temporary Additional Mode |
| Authorized Quantity | The quantity of the authorized cloud services. |
| Authorization Validity Period | The validity period of the authorization. |
| Actual Authorized Usage | The actual authorized quantity of the cloud services. |
| Validity Period for Software License Update and Technical Support | The validity period of the project. The default validity period of a project is 90 days after the creation. The free trial does not take up your validity period. The remaining validity period is displayed after the formal authorization is used. |
| Authorization Status | The current authorization status of a specification for a service. Activating RENEW Service Expired Specification Quota Exceeded Important If the following items appear in the Authorization Status column of a service, take note of them. RENEW Service Expired: indicates that the customer must renew the subscription as soon as possible. Otherwise, field operations services (including ticket processing) are terminated. Specification Quota Exceeded: indicates that the specifications deployed for a service have exceeded the contract quota, and the customer must scale up the quota as soon as possible. |

5. Click the **Authorization Specifications Details** tab to view the authorization specification
information of services across different data centers or regions. ngs The following table describes the parameters in the authorization specification information.

| Parameter | Description |
|---|---|
| Category | The name of an authorized cloud service. |
| Dimension | The specification name of an authorized service. |
| Used | The total number of existing authorizations of a specification for a service. |
| Issued | The maximum number of authorizations of a specification for a service. Note Move the pointer over the icon to view the available authorization quota. |
| Usage Update Time | The time when the authorization specifications of the service were updated. |
| Status | The current authorization status of a specification for a service. |

6. Click the **Authorization Specification Information** tab to view the statistics on the
authorized specifications of services and the information about services whose actual authorized specifications exceed the quota of authorized specifications. i. You can filter information about the authorized specifications of a specific service by setting **Authorization specification level**, **Region ID/Data Center ID**, **Product**
**Name**, and **Time Range**.
ngs ii. In the **Authorization Specification Information** section, view the statistics on authorized specifications. The statistics include **Maximum Specification Usage Within**
**Current Period**, **Maximum Number Occurred At**, **Minimum Specification Usage**
**Within Current Period**, **Minimum Specifications Occurred At**, and **Average**
**Specification Usage Within Current Period**.
iii. Click the icon in front of a service name to view the authorization specification details of the service on the previous day within a specific time range. The information include
**Authorization specification name**, **Authorized Specification Usage**, **Maximum**
**authorization specifications**, and **Recorded At**.
iv. Click **View More**. In the dialog box that appears, you can view the authorization specification information of the service within the selected time range by date. v. In the **Authorization specification overcount** section, you can view the information about the services whose actual authorized specifications exceed the quota of authorized specifications. ngs vi. Click the icon in front of a service name to view the authorization specification details of the service on the previous day within a specific time range. The information include
**Authorization specification name**, **Authorized Specification Usage**, **Maximum**
**authorization specifications**, and **Recorded At**.
vii. Click **View More**. In the dialog box that appears, you can view the authorization specification overcount of the service within the selected time range by date.

### 7.2 Custom settings

The feature allows you to customize the login page and platform logo.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **More > System Config**.
3. In the left-side navigation pane, click **Custom Settings**.
4. Customize the following items:
**Platform Language**: Select the languages that you want the platform to support and the
default language of the platform. The following languages are available: Simplified Chinese, Traditional Chinese, and English.
**Appearance and Theme**: Select the color mode of the **Appearance** (**Light Color**
**Mode**, **Dark Pattern**) and **Theme Color**.
**Page Watermark**: Specifies whether to add watermarks to pages.
**Brand Setting**: You can configure the **Browser Ico Icon**, **Platform Logo**, **Platform**
**Name**, **Login Page**, **Version Information**, and **Copyright Notice** in three languages.
ngs
5. After the settings are complete, click **Determine**.
6. In the upper-right corner of the page, click **Restore Factory Settings**. In the message
that appears, click **Restore Factory Settings**. The custom settings are restored to the factory settings and take effect after you log on to the Apsara Uni-manager Operations Console again.

**Important**

This operation is irreversible. Proceed with caution.

### 7.3 Notification management

#### 7.3.1 Channel management

You can configure channels to send notifications.

**Create a channel**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Settings**.
3. In the left-side navigation pane, choose **Notification Management** > **Channel**
**Management**.
4. Click **Create a channel** and configure the parameters. The following table describes the
parameters. ngs

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

ngs

| Whether to enable StartTLS | This parameter is available only when you set the Channel type parameter to Email. Specify whether to enable StartTLS as the protocol extension for mutual negotiations regarding encryption. |
|---|---|
| Whether to enable StartTLS | This parameter is available only when you set the Channel type parameter to Email. Specify whether to use the Secure Sockets Layer (SSL) protocol to encrypt data transmission. |
| Push URL | This parameter is available only when you set the Channel type parameter to Webhook. Enter the push URL. |
| Custom URL parameters | This parameter is available only when you set the Channel type parameter to Webhook. Specify the URL parameters in a POST request. The following preset parameter mappings are supported: ${contact list}: the list of contacts. _ ${content title}: the content title. _ ${content body}: the content body. _ |
| Custom header | This parameter is available only when you set the Channel type parameter to Webhook. Specify the headers in a POST request. Preset parameter mappings are supported. |
| Request body template (JSON string) | This parameter is available only when you set the Channel type parameter to Webhook. The request body in the POST request. Preset parameter mappings are supported. |
| Message content size (byte) | Enter the maximum number of bytes that can be sent in a message. Maximum value: 8192. |

ngs
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

ngs
1. Find the channel that you want to delete and click **Delete** in the **Operation** column of the
channel.
2. In the message that appears, click **OK**.

#### 7.3.2 Push history

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

### 7.4 Region coordinate management

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

ngs

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

### 7.5 Archives

This topic describes the modules related to archive management.

**Modules**

You can archive the key metadata of Apsara Stack. The archived metadata is used for quick recovery from Apsara Stack failures.

**Prerequisites**

ngs System administrator permissions on ASO are granted. Only the metadata of Apsara Distributed File System and OPS DNS can be archived.

**Modules**

| Module | Description |
|---|---|
| Archive Settings | You can view archive settings, modify archive settings, and trigger archive operations. |
| Archive Details | You can view archive details, including the archived product, archived item, file name, start time, and archive status. |
| Archive Products | You can view information about archived products, configure products to archive, and manage archived products. |
| Archiving Server Settings | You can configure the archive server for the storage of archive files. |

#### 7.5.1 Backup settings

This topic describes how to configure archived items.

**Prerequisites**

The archive server is configured. Archive products are added. For more information, see Archive product management.
1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Archive Settings**.
On the left side of the page, the items that you can configure are displayed in a hierarchical tree-like structure. The root node is a product list and shows the products whose data can be archived in the system.

> **Note:** Only the metadata of Apsara Distributed File System and OPS DNS can be archived.

4. Click the item that you want to archive. In the right-side section, configure the following
information and click **Modify** to trigger the archive operation.

> **Note:** If the #FTPMaster server is deployed in the cluster of the service, the system automatically fills in the archive information of ecs pangu
> .

ngs

| GUI element | Description |
|---|---|
| Product Cluster IP Address | The IP address of the actual transfer server. |
| Archive Folder | A folder on the transfer server. You only need to enter a folder in the field without manually creating a folder to store archive files. Example: pangu: /apsarapangu/disk8/pangu master bak/product namepangu/bak _ _ _ opsdns: /apsarapangu/disk8/opsdns bak/opsdns/bak _ |
| Script Execution Folder | A folder on the transfer server. You only need to enter a folder in the field without manually creating a folder to store scripts to be executed. Example: pangu: /apsarapangu/disk8/pangu master bak/product namepangu/bin _ _ _ opsdns: /apsarapangu/disk8/opsdns bak/opsdns/bak _ |

ngs

| Script Parameters | Required. The execution parameters for the script. You must enter the value in the --ip=xxx.xxx.xxx.xxx format. pangu: Enter any IP address of the pangu master. opsdns: We recommend that you enter --ip=127.0.0.1. |
|---|---|
| Archive Schedule | The archive schedule. In this example, a value of 1 is entered to specify that the archive is performed only once. |
| Archive Schedule Unit | The unit of the archive schedule. Valid values: Day, Hour, and Minute. In this example, Hour is selected to specify that the archive is performed by hour. |
| Timeout period | The timeout period. Unit: milliseconds. Default value: 3600. |

5. Repeat the preceding step to configure all items.

**What to do next**

After you configure the items, you can view the archive details and status on the **Archive**
**Details** page.

#### 7.5.2 Backup details

This topic describes how to view the archive details of each archived item.

**Prerequisites**

Archive settings are configured and an archive operation is triggered.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Backup Details**.
4. You can filter archive information by **Product**, **Archive item**, and **Start time**.
5. View the archive details of an item, including the **Product**, **Archived Item**, **File Name**,
**Start At**, and **Status**. The archive status includes **Not started**, **In progress**, **Complete**,
**Timeout**, and **Failed**.
ngs

> **Note:** If the status of an archived item is **Complete**, you must check whether the Message- Digest Algorithm 5 (MD5) values of the offline archive service and the archive server are consistent with each other. If the values are consistent with each other, the archive was successful.

#### 7.5.3 Archive product management

This topic describes how to add archive products.

**Prerequisites**

Only the metadata of Apsara Distributed File System and OPS DNS can be archived. The archive server is configured.

**Archive a product**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click System Config.
3. In the left-side navigation pane, choose **Archive management** > **Archive Products**.
4. Click **Add products**. In the dialog box that appears, add a product and click **OK**.

| Parameter | Description | Example |
|---|---|---|
| Product | The name of the product. Select a product from the drop-down list. pangu opsdns | pangu |
| Script | The name of the archive script. The system automatically selects the script based on the product. | metadata backup.py _ |

ngs

| Archived Item | The product information to be archived. Note An archived item is the smallest unit for archiving. You can archive the metadata of Apsara Distributed File System for different services, such as ecs pangu, ots pangu, oss pangu, and ads pangu. | ecs pangu _ |
|---|---|---|
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
**Archive Settings** page. You can configure archive settings for the archived items on the
Archive Settings page.

#### 7.5.4 Archiving server settings

This topic describes how to configure the archive server that is used to store archive files.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **System Config**.
3. In the left-side navigation pane, choose **Archive management** > **Archiving Server**
**Settings**.
4. Configure the parameters that are described in the following table and then click **Submit**.
ngs

> **Note:** If the #FTPMaster server is deployed in the cluster of the service, the system automatically fills in the archive server information of ecs pangu
> .

| Parameter | Description |
|---|---|
| Archive Server IP Address | The IP address of the archive server. The archive server must meet the following requirements: The archive server is an independent physical server. The archive server is managed by the Apsara Infrastructure Management console. The network of the archive server is connected to other servers in Apsara Stack. Apsara Distributed File System cannot be deployed on the server or on the disk where archive metadata is stored. |
| Backup Server Monitoring Path | The storage path of archive files on the archive server. Note If the backup path does not start with /apsarapangu, /ASO- backup is added to the beginning of the path by default. The archive service detects new archive files by monitoring the specified folder on the archive server and determines whether an archive is successful by comparing the MD5 value of the archive file with that of the original file. |
| Archive Retention Period | The actual period of time an archive file is saved. Overdue archive files are deleted. |

5. In the dialog box that appears, select **I have read the above prompts and confirmed**
**the operation.** and click **OK**.
ngs

**What to do next**

After you configure the archive server, you need to add new archived items on the **Archive**
**Products** page.
ions

## 8 User permissions

### 8.1 User management

You can create a user and assign the user different roles to meet different requirements for system access control as an administrator.

**Prerequisites**

You are a role administrator. A department is created. A logon policy is created. If you want to assign a user a custom role, you need to first create the custom role.

**Usage notes**

The opsadmin user is the super administrator of ASO and is the only user that has full management permissions on ASO.

**Add a user**

1. Go to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Users**.
4. On the **Users** tab, click **Add**. In the dialog box that appears, configure the following
parameters and click **OK**.

| Parameter | Description |
|---|---|
| Username | The name for the user that you want to create. The name can be up to 48 characters in length and can contain digits, letters, underscores ( ), hyphens (-), and periods (.). You can enter email _ addresses as usernames. |
| Password | The password for the user. The password must be 10 to 20 characters in length and must contain letters, digits, and special characters. |
| Confirm Password | The password that you enter in the Password field. Make sure that the two passwords that you enter are the same. |
| Display name | Enter a display name for the user. |
| Logon Policy | The logon policy of the user. To create a logon policy, choose Security Management > Access Control > Logon Policies in the top navigation bar. |

ions

| Role | The role that you want to assign to the user. To create a role, click User Authorities in the top navigation bar and click Roles in the left-side navigation pane. Note You can add multiple roles to a user. |
|---|---|
| Department | The department to which the user belongs. To create a department, click User Authorities in the top navigation bar and click Departments in the left-side navigation pane. |
| Mobile phone | The mobile number of the user that you want to create. |
| Email address | The email address of the user that you want to create. |
| Allowed to Create AccessKey ID | Specifies whether to allow the user to create AccessKey IDs. |

ions
5. After a user is added, you can view the information of the added user on the **User**
**Management** page.

**Related operations**

**Query a user**

1. Click **Advanced Filter**.
2. Specify the **Username**, **Role**, and **Department** parameters and click Search to search for
a specific user. ions

**Export users**

Select the users to be exported and click **Export** to export the information of the users to your on-premises computer.

> **Note:** If you do not select a user, the information of all the users displayed on the page is exported.

**Import users**

1. Click **Import**.
2. In the Import dialog box, click **Click Here to Upload File** , select the user list file that you
want to upload, and upload the file.

**Modify a user**

1. Find the user that you want to modify and click **Modify** in the **Actions** column.
2. In the **Modify user** dialog box, modify the parameters and click **OK**.

**Delete a user**

1. Find the user that you want to delete and click **Delete** in the **Actions** column.
2. In the message that appears, select I have read and above prompts and confirmed the
operation, and then click **OK**.

> **Note:** After you delete a user, the AccessKey pair of the user is disabled, which may cause services or applications that use the AccessKey pair to fail to work as expected.

3. On the **Recycle Bin** tab, you can view the information of deleted users.

> **Note:** If you want to restore a user, find the user on the **Recycle Bin** tab and click **Recover** in the **Actions** column.

**Activate a user**

If a user account is frozen because the user does not log on to the Apsara Uni-manager Operations Console within the time period specified by the account freeze policy, you can activate the account as an administrator.
1. Find the account that you want to activate and click **Activate** in the **Actions** column.
2. In the message that appears, click **OK**.

**Change the logon policy for users**

1. Select the users for which you want to modify the logon policy and click **Modify Logon**
**Policy** in the lower part of the page.
2. In the dialog box that appears, specify the **Logon Policy** parameter and click **OK**.
ions

> **Note:** The logon policy of the opsadmin user cannot be modified.

### 8.2 User group management

You can add multiple users to a user group and add a role to the user group as an administrator for centralized management.

**Prerequisites**

You have the administrator permissions. A department has been created.

**Add a user group**

1. Go to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **User Authorities**.
3. In the left-side navigation pane, click **User Groups**.
4. Click **Add**. In the dialog box that appears, configure the parameters and click **OK**. The
following table describes the parameters:

| Parameter | Description |
|---|---|
| User Group Name | Enter the name of the user group. |
| Department | Select the department to which the user group belongs. You can choose User Permissions > Department Management and create a department. |
| Role | Select the role that you want to add to the user group. You can choose User Permissions > Roles and create a role. Note You can add multiple roles to a user group. |

ions

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
2. In the dialog box that appears, you can add users to or delete users from the user group.
Add: Click **Add**. In the dialog box that appears, select one or more usernames and click
**OK**.
ions Delete: Click **Delete** in the **Actions** column to delete the username.
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

### 8.3 Role management

A role is a collection of access permissions. You can assign different roles to different users to meet your requirements for system access control. You can set custom roles in the Apsara Uni-manager Operations Console to implement more flexible and efficient permission control.

**Prerequisites**

You are a role administrator. You want to create 100 or fewer basic roles.

**Background information**

Roles are classified into preset roles and custom roles. Preset roles are provided by the system, and you cannot modify or delete them. The following table describes the system preset roles and their corresponding menu permissions.

| Role name | Duty | Menu permission |
|---|---|---|
| System Admin | Manages the O&M operations across the platform. | Monitor & Alarms Platform Operation Product Operation System Config User Authorities |
| System Viewer | Views the O&M operations across the platform. |   |

ions

| Security Admin | Manages the security related O&M operations across the platform. | Security Management Security Operations Data Security Host Security Network Security Account Security Access Control Platform Operation Apsara Infrastructure Management |
|---|---|---|
| Security Auditor | Audits, tracks, and analyzes security related O&M operations across the platform. | Security Management Security Audit Platform O&M Apsara Infrastructure Management |
| Role Admin | Manages user permissions across the platform. | User Authorities |
| Role Viewer | Views user permissions across the platform. |   |

**Create a role**

1. Log to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Roles**.
4. In the upper part of the page, click **Create Role**.
5. In the **Basic Configurations** step, configure the following parameters and click **Next**
**Step: Console Permissions**.

| Parameter | Description |
|---|---|
| Role Name | The name of the role. |
| Role Description | The description of the role. |

ions
6. In the **Console Permissions** step, configure console permissions for the role. Then, click
**Next Step: Product Permissions**.

> **Note:** You can search for permissions by using the search box in the upper part of the page. You can also click View Authorized Users to view only authorized menus.

7. In the **Product Permissions** step, configure product permissions for the role. Then, click
**Next Step: Menu Permissions**.

> **Note:** You can search for permissions by using the search box in the upper part of the page. You can also click View Authorized Users to view only authorized menus.

ions
8. In the **Menu Permissions** step, configure menu permissions for the role and click **Create**.

**Related operations**

**View a role**

1. In the upper part of the role list, you can enter a role name in the search box to view a
specific role. ions
2. Click the name of the role. On the **Role Details** page, you can view the role information in
detail. This page provides four tabs: **Console Permissions**, **Product Permissions**, **Menu**
**Permissions**, and **Authorized User**.

> **Note:** If you want to modify the role, you can click **Edit** in the upper-right corner of the page.

3. On the **Authorized User** tab, view the users that are associated with the role.
If you want to associate a user with the role, click **Add Authorized Users**. In the dialog box that appears, enter a **username** in the box, select the user, and then click **OK**. If you want to disassociate a user from the role, click **Remove** in the **Actions** column of the user. In the message that appears, click **Remove**.

**Modify a role**

> **Note:** Preset roles cannot be modified.

1. Find the role that you want to modify and click **Edit** in the **Actions** column.
2. Modify the role permissions by following the same steps for creating a role and click
**Update**.
ions

**Delete a role**

> **Note:** Preset roles cannot be deleted.
> Before you delete a role, make sure that the role is associated with any user. Otherwise, the role cannot be deleted.

1. Find the role that you want to delete and click **Delete** in the **Actions** column.
2. In the dialog box that appears, click **OK**.

### 8.4 Departments

The Apsara Uni-manager Operations Console provides a root department by default. You can add, delete, modify, and query departments under the root department. You can also create users and user groups for a department.

**Prerequisites**

You have the administrator permissions. You can create up to five levels of departments.

**Add a department**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **User Authorities**.
3. In the left-side navigation pane, click **Departments**.
4. On the left side of the Departments page, you can view the tree structure of all
departments. You can also view the information about all users and user groups in each department by clicking the department name.
5. In the catalog tree on the left, select the department to which you want to add a sub-
department and click **Add Department** in the right section. In the Add Department dialog box, enter a value in the **Department Name** field, and click **OK**. Then, you can view the created department in the catalog tree. The **Department Name** parameter can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). ions

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
**Users** page.

**Add a user group to a department**

1. In the catalog tree on the left, select the department to which you want to add a user
group, click **Add user groups** in the right section.
2. In the dialog box that appears, configure the **user group name**, select a **role**, and then
click **OK**. After you add a user group, you can view the information about the user group on the **User**
**Groups** page.
ions

### 8.5 Regions associated with department region

**department region**

In multi-region scenarios, O&M engineers can associate departments with regions. After a department is associated with a region, users in the department can manage and view resources in the region.

**Background information**

In multi-region scenarios, a region is managed by its administrators. After administrators log on to the Apsara Uni-manager Operations Console from the central region, they can only manage resources in the associated regions. Relationship between departments and regions: A department can be associated with multiple regions. A region can be associated with multiple departments.

**Limits**

Only departments at tier 1 can be associated with regions.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **More > User Authorities**.
3. In the left-side navigation pane, choose **Department-region Association**.
4. In the left-side Department directory tree, select the department that you want to associate
with regions. In the **Associated Regions** section on the right, select one or more regions that you want to associate with the department.
5. Click **Update Association**.

### 8.6 Menu settings

The Menu Settings module allows you to add, modify, or delete a menu based on your business requirements.

**Usage notes**

A menu supports up to five menu levels.

**Add menu data**

1. Log on to the Apsara Uni-manager Operations Console.
ions
2. In the top navigation bar, choose **More > User Authorities**.
3. In the left-side navigation pane, click **Menus**.
4. In the upper part of the Menus page, click **Add Menu Data**, or click **Add Submenu** in the
**Actions** column corresponding to a menu path. In the panel that appears, configure
parameters and click **OK**. The following table describes the parameters that you need to configure.

| Parameter | Description |
|---|---|
| Parent Node ID | Select a parent menu. This parameter does not need to be specified when you add a level-1 menu. |
| Unique Identifier | The unique identifier that is used to invoke functions. We recommend that you specify a unique identifier that contains 5 to 20 characters. |
| Default Display Name | The default display name of the menu. |
| Name in Chinese | The menu name in Chinese. In the Chinese language environment, if the Chinese name of the menu is specified, the default display name of the menu is the specified Chinese name. |
| Name in English | The menu name in English. In the English language environment, if the English name of the menu is specified, the default display name of the menu is the specified English name. |
| Description | The description of the menu. |
| Show or not | Specifies whether to display the menu after it is added. By default, this feature is enabled. |
| Is it a Link | Specifies whether to navigate users to another page when they click the menu. By default, this feature is disabled. |
| URL | This parameter appears if you turn on Is it a link. The URL to which users are navigated when they click the menu. To navigate users to a page of the system, specify the absolute or relative path of the page. To navigate users to a page of a third-party system, specify the absolute path of the page. |
| Link new page to open | This parameter appears if you turn on Is it a link. Specifies whether to open the URL on a new page after users click the menu. By default, this feature is disabled. |

ions

| Current Order | The order of the menu among all menus in the same parent menu. You cannot configure the order in the panel. You can modify the configuration on the Menus page after you create the menu. |
|---|---|

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

esponse

## 9 Emergency response

This topic describes the scenarios in which the emergency response is triggered. When degradation is triggered in the Apsara Uni-manager Operations Console, the console switches to the emergency mode and the emergency page appears.

**Scenario**

1. Log on to the Apsara Uni-manager Operations Console.
2. Degradation is triggered in the Apsara Uni-manager Operations Console, as shown in the
following figure.
3. Click **Enable Emergency Mode**.
4. Enter the correct username and password, and click **Log On**.

> **Note:** The account and password used to log on to the Apsara Uni-manager Operations Console are the same as those used to switch to the emergency mode.

esponse
5. After the console switches to the emergency mode, the emergency response page appears.

### 9.1 Watchdog monitoring and alerting

**alerting**

Some global faults in Apsara Stack, such as faults in the MiniRDS, physical network, and OpsDNS, may cause exceptions in the Apsara Uni-manager Management Console. This topic describes **Watchdog monitoring and alerting**, which is used to monitor and alert the global availability. Watchdog monitoring and alerting can be used to monitor faults that may cause global faults or invalidate the original alert list. Watchdog monitoring and alerting displays**Final Status Overview of Major Products (Abnormal/All SRs)** , **Monitoring**
**Status**, and **Alert Status** for faults.
esponse

> **Note:** This page only displays watchdog monitoring and alerting items. For information about other monitoring and alerting items, choose **Monitor&Alerts** > **Alerts** > **Alerts** in the Apsara Uni-manager Operations Console.

**Features**

| Feature | Description |
|---|---|
| Detection of global faults in Apsara Stack | Detects global network faults, and checks whether network components such as server load balancers (SLBs), Domain Name System (DNS), gateways, and physical links are normal. Detects global faults of the MiniRDS database in Apsara Stack or faults of major instances. |
| Detection of alert link faults | Detects features in the Apsara Uni-manager Management Console, including homepage logon, user authentication, and alerting. Detects TianjiMon features sends alerts when data output faults or alarm output faults occur. |
| Alert viewing and sending | Supports on-site registration of alarm callback gateways to send alarms from the out-of-band network when exceptions are detected. Provides a simple data viewing page. |

1. Log on to theApsara Uni-manager Operations Console in emergency mode.
2. In the top navigation bar, choose**Emergency Response**>**Watchdog Monitoring &**
**Alerting**.
3. In the**Final Status Overview of Major Products (Abnormal/All SRs)**section**,** view all
SRs and abnormal SRs of each major product. Click the name of a product that has abnormal SR data to view the detailed SR information.
4. In the**Monitoring Status**section:
In theSearch for check items, enter a check item keyword to filter check items. Fuzzy search is supported. As shown in the following figure, the **Monitoring Status**is displayed by**Check Items**,
**Description**,**Check Time**, **Status**, and **Error Description**.
esponse
5. In the**Alert Status**section:
In the Search Alert ID/Information field, enter a keyword to search for alert ID or information. Fuzzy search is supported. As shown in the following figure, the data is displayed by**Alert ID**, **Alert Information**,
**Resource Ownership**, **Last Alert Time**, and **Number of Alerts****.**

### 9.2 Scenario Diagnosis

This topic describes the preset fault scenarios. You can select a scenario to trigger a diagnostics plan.
1. Log on to the Apsara Uni-manager Operations Console in the emergency mode.
2. In the top navigation bar, choose **Emergency Response** > **Scenario Diagnostics.**
3. On the **Scenario Diagnostics** page, perform the following operations:
**Diagnostics Plan:**Common fault scenarios are provided. You can click**Execute**to trigger
the corresponding scenario. In the search plan name field, enter a keyword to filter plans. Fuzzy search is supported. As shown in the following figure, **diagnostics plans**include the following fields:**Plan**
**Name**, **Scenario Description**, and **Operation****.**
On the **Diagnostics Plan** tab, click **Execute** in the Actions column. You can view the execution process and result. esponse The following table describes common preset plans.

| Plan Name | Description |
|---|---|
| Diagnostics for faults in Apsara Uni- manager Operations Console or Apsara Uni-manager Management Console | If the homepage of the Apsara Uni-manager Operations Console or Apsara Uni-manager Management Console is accessible but you cannot log on, you can use this plan for diagnostics. This plan diagnoses terminal servers, AAS, UmmAk, Tair, and MiniRDS. |
| Diagnostics for faults in the management portal. | If the management portal is accessible, you can use this plan for diagnostics. This plan diagnoses terminal servers, opsDNS, SLBs, network components, and MiniRDS. |
| Diagnostics for a large number of faults in the Apsara Infrastructure Management Framework. | This plan diagnoses terminal servers, DockerHost, MiniRDS, Apsara Infrastructure Management Framework basic services, and OpsDNS. |
| Diagnostics for terminal servers | This plan diagnoses terminal servers. |
| Diagnostics for DockerHost | This plan diagnoses DockerHost. |
| Diagnostics for MiniRDS hosts | This plan diagnoses MiniRDS physical machines. |

**Execution History**: Diagnostics plans that you executed are displayed on the Execution
History tab. In thesearch plan name field, enter a plan name keyword to filter plans that are executed or being executed. Fuzzy search is supported. As shown in the following figure, the execution history includes the following fields: **Plan**
**Name**, **Scenario Description**, **Execution Time**, **Execution Result**, and **Actions**.
On the **Execution History** tab, find the plan that you want to manage and click **Details** in the Actions column.

### 9.3 Emergency plans

This topic describes the preset emergency plans. You can select a scenario to trigger an emergency plan.
1. Log on to the Apsara Uni-manager Operations Console in the emergency mode.
2. In the top navigation bar, choose **Emergency Response** > **Emergency Plans****.**
3. On the **Emergency Plans** page, you can perform the following operations:
esponse
**Instance Information****:**The information about instances that are connected to the O&M
platforms. You can click the**link**after an O&M platform to go to the O&M platform.
**Emergency Plans**: preset**emergency plans** are provided. You can click **Execute** to
trigger an emergency plan. In the search plan name field, enter a keyword to filter plans. Fuzzy search is supported. As shown in the following figure, the emergency plans include the following fields: **Plan**
**Name**, **Scenario Description**, **Operation**.
On the **Emergency Plans** tab, find the emergency plan that you want to manage and click **Execute** in the Actions column to view the execution process and results. The following table describes common preset plans.

| Plan Name | Description |
|---|---|
| Stop the ops.OpsDnsSlave .dnsslave service __ of the OPS 2 server | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in the OPS 2 server. |
| Disable authentication in the Apsara Infrastructure Management Framework | You can use this plan to temporarily disable authentication in the Apsara Infrastructure Management Framework before you log on to the Apsara Infrastructure Management Framework Console to perform O&M operations. |
| Enable authentication in the Apsara Infrastructure Management Framework | You can use this plan to temporarily disable authentication in the Apsara Infrastructure Management Framework. |
| Disable authentication in the ApsaraDB Operations and Maintenance System | You can use this plan to disable the authentication in MiniRDS ApsaraDB Operations and Maintenance System before you log on to the system by using a local account. |
| Enable authentication in the ApsaraDB Operations and Maintenance System | You can use this plan to enable authentication in the ApsaraDB Operations and Maintenance System after faults are rectified. |
| Restart AAS and UmmAk | You can use this plan to restart authentication components when the authentication link is abnormal. |
| Restart POP | You can use this plan to restart POP when POP is abnormal. |

esponse

| Restart the ops.OpsDnsSlave .dnsslave __ service of the OPS 1 server | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in the OPS 1 server. |
|---|---|
| Restart the ops.OpsDnsSlave .dnsslave __ service of the OPS 2 server | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in the OPS 2 server. |
| Restart the ops.OpsDnsSlave .dnsslave __ named service in the OPS 1 server | You can use this plan to stop the DNS slave named service when the DNS resolution is abnormal in the OPS 1 server. |
| Restart the ops.OpsDnsSlave .dnsslave __ named service in the OPS 2 server | You can use this plan to stop the DNS slave named service when the DNS resolution is abnormal in the OPS 2 server. |
| Stop the ops.OpsDnsSlave .dnsslave service __ in the OPS 1 server | You can use this plan to stop the DNS slave service when the DNS resolution is abnormal in the OPS 1 server. |

**Execution History**: **Emergency plans** that you executed are displayed on the Execution
History tab. In the search plan name field, enter a plan name keyword to filter plans that are executed or being executed. Fuzzy search is supported. As shown in the following figure, **Execution History** includes the following fields: **Plan**
**Name**, **Scenario Description**, **Execution Time**, **Execution Result**, **Actions**.
On the **Execution History** tab, find the plan that you want to manage and click **Details** in the Actions column. As shown in the following figure, the details page shows the execution process and results. In this example, an executed emergency plan is displayed. ortal

## 10 Developer portal

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **Operation Platform**.
3. In the **Developer portal** section at the bottom of the page, you can use the shortcuts.

| Menu | Description |
|---|---|
| Homepag e | On the API Integration tab, you can view the API operations ofP opular Services and Recent Calls. You can also list API operations by services and search for API and SDK documents by entering keywords. |
| API Integrati on | Includes Documentation, API Debugging, API Change History, and SDK Examples. Documentation: provides API references of cloud services. API Debugging: allows you to debug API operations. API Change History: records the change history of cloud service API operations. SDK Examples: allows you to view and download the SDK demos that are used to call API operations. |
| Call Statistics | Includes Call Overview, API Calls, and Statistical Reports. For more information, see Step 4. Call Overview: displays the call trends and error distribution. API Calls: allows you to view API calls of cloud services. Statistical Reports: allows you to create statistical report tasks based on your business requirements. After a statistical report task is created, you can view the task states and report details at any time. This helps you understand your business. You can also start, stop or delete report tasks. |
| Best Practices | Apsara Stack provides a series of templates based on Terraform to help you manage cloud resources in a standardized manner. |

4. You can view the following items on the **Call Statistics** tab.

**Call Overview**

ortal
**Call Trend**: You can view the **Total Calls**, **Errors**, and **Error Rate** information within
the specified **Call Date** range. The number of calls to each cloud service is displayed in a bar chart. Move the pointer over the bar chart to view **the number of successful**
**calls** and **the number of failed calls** .
**Error Distribution**: You can view the distribution of API errors based on filter
conditions such as **Call Date**, **Cloud Service**, and **API Version**.
**Call Statistics**: You can filter the call statistics of the API operations by **Service**, **API**
**Name**, and **Call Time**. The statistics include **API Name**, **Product Name**, **Number of**
**Calls**, **Average Call Time**, and **Success Rate**.
The **Called At** range must be within seven days.

> Click **Call Source Distribution** in the **Actions** column to view the **AccessKey** ID and the source service of an API operation.

ortal

**Statistical Reports**

ortal Create a statistical report: Click **Create Statistical Report**, set the following parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Task Name | The name of the new statistical report. |
| Interval | The interval at which the statistical task recurs. Valid values: 1 Hour 6 Hours 12 Hours 24 Hours |
| Data Source | The source of the statistics. Valid values: opsapi-sls pop-sls |
| Statistical Policy | Set the value to Keyword Retrieval. |
| Keyword | Click Add Entry and enter a key-value pair. |
| Custom Aggregation Policy | Select an aggregation policy from the drop-down list. |

ortal View the statistical reports. a. Find the statistics report that you want to view and click **View Report** in the **Actions** column. b. The execution history of a report task is displayed. You can click **View Details** in the
**Actions** column to view the report details, including **Basic Information**, **Matching**
**Info**, and **Time Distribution**.
Start a statistical task: In the **Actions** column, click **Start**. If **Task Status** is **Running**, the task is started.

> **Note:** If **Task Status** is **Canceled**, you can start the task.

Stop a statistical task: Find the statistical task and click **Stop** in the **Actions** column. If
**Task Status** is **Canceled**, the task is stopped.

> **Note:** If **Task Status** is **Running**, you can stop the task.

Delete a statistical task: Find the statistical task and click **Delete** in the **Actions** column. In the message that appears, click **OK**.
