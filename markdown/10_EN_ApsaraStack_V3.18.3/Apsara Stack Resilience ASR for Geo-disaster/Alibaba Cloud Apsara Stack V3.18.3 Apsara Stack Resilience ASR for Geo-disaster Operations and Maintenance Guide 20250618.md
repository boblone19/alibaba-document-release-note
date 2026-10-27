---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster Operations and Maintenance Guide 20250618"
product_version: "V3.18.3"
doc_version: "20250618"
pdf_pages: 175
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster Operations and Maintenance Guide 20250618.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E7%81%BE%E5%A4%87%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Geo-disaster%20Operations%20and%20Maintenance%20Guide%2020250618.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Geo-disaster Operations and Maintenance Guide 20250618

## Table of Contents

- 1 Overview
  - 1.1 Purpose
  - 1.2 Requirements
  - 1.3 Usage notes
- 2 Architecture
  - 2.1 Component architecture
  - 2.2 Server roles
- 3 ASR-DR O&M console
  - 3.1 Log on to the O&M console of ASR-DR
  - 3.2 Homepage
  - 3.3 Disaster recovery monitoring
    - 3.3.1 Check cluster status at the cloud platform side
    - 3.3.2 Check cross-cloud network access
    - 3.3.3 Monitor the status of synchronization entities
  - 3.4 Basic capability O&M
    - 3.4.1 Manage cloud service information
    - 3.4.2 Configure the dashboard
  - 3.5 Disaster recovery O&M
    - 3.5.1 Manage synchronization entities
      - 3.5.1.1 Skip a step
      - 3.5.1.2 Reperform a single step
      - 3.5.1.3 Configure throttling
      - 3.5.1.4 Delete an entity from a protection group
      - 3.5.1.5 View the logs of a synchronization entity
    - 3.5.2 Perform a site switchover drill
    - 3.5.3 Perform a site failover
    - 3.5.4 View the execution history of a site disaster recovery plan
  - 3.6 Independent disaster recovery management
    - 3.6.1 Create an independent disaster recovery plan
    - 3.6.2 Perform a failover
    - 3.6.3 Perform a switchover drill
    - 3.6.4 View the details of an independent disaster recovery plan
    - 3.6.5 Disassociate configured nodes from an independent disaster recovery plan
    - 3.6.6 Delete an independent disaster recovery plan
- 4 Common O&M operations
  - 4.1 Log on to a container
  - 4.2 Log on to the ASR-DR metadatabase
- 5 ASR-DR O&M
  - 5.1 Manage logs
    - 5.1.1 View ASR-DR logs
    - 5.1.2 Modify the default log configurations
  - 5.2 Modify the URL of the ASR-DR console
  - 5.3 Stop ASR-DR nodes
  - 5.4 Replace the JAR package
  - 5.5 Manage configurations
- 6 FAQ
  - 6.1 ApsaraDB RDS
    - 6.1.1 How do I add databases and tables to ApsaraDB RDS instances?
    - 6.1.2 How do I manually switch workloads between primary and secondary ApsaraDB RDS instances?
    - 6.1.3 How do I manually resume data synchronization?
  - 6.2 DNS
    - 6.2.1 What do I do if the "rrSet inconsistent" error message appears in DNS logs?
    - 6.2.2 What do I do if the "not found record" error message appears in DNS logs?
    - 6.2.3 What do I do if the "not found zone" error message appears in DNS logs?
  - 6.3 AnalyticDB for MySQL V3.0
    - 6.3.1 What do I do if a reprotection operation fails to be performed?
    - 6.3.2 What do I do if a new synchronization entity fails to be created for a protection group?
    - 6.3.3 How do I precheck a synchronization entity before incremental synchronization?
  - 6.4 PolarDB-X
    - 6.4.1 What do I do if a database fails to be deleted from a secondary instance?
    - 6.4.2 What do I do if an error message indicating that a logical table does not exist appears when ASR-DR queries the schema of the logical table?
    - 6.4.3 How do I modify the ApsaraDB RDS database threshold of PolarDB-X?
    - 6.4.4 What do I do if a data synchronization task between PolarDB-X instances fails to be created?
    - 6.4.5 How do I scale out PolarDB-X instances?
  - 6.5 DTS
    - 6.5.1 How do I view DTS logs?
    - 6.5.2 What do I do if a data synchronization task fails to be created?
      - 6.5.2.1 What do I do if the "The specified Instance SourceEndpoint.InstanceID Not Found" error message appears in DTS logs?
      - 6.5.2.2 What do I do if the "cluster info is null.The input domain and region is invalid" error message appears in DTS logs?
      - 6.5.2.3 What do I do if the "Specified access key is not found" error message appears in DTS logs?
      - 6.5.2.4 What do I do if the "InvalidAppId.NotFound" error message appears in DTS logs?
      - 6.5.2.5 What do I do if the "ram authorized" error message appears in DTS logs?
      - 6.5.2.6 What do I do if the "Data truncation: Data too long for column 'open_api_objects'" error message appears in DTS logs?
    - 6.5.3 What do I do if a precheck fails?
      - 6.5.3.1 What do I do if an error message indicating inconsistent topology appears?
      - 6.5.3.2 What do I do if the "CHECK_ERROR_SRC_USER_PSW" error message appears?
      - 6.5.3.3 What do I do if the "CHECK_ERROR_DEST_USER_PSW" error message appears?
    - 6.5.4 What do I do if the incremental data service is abnormal?
      - 6.5.4.1 What do I do if the incremental data service fails?
    - 6.5.5 What do I do if data synchronization is abnormal?
      - 6.5.5.1 What do I do if the "store delay xxx second(s)" error message appears?
      - 6.5.5.2 What do I do if an error message indicating that DReader fails to connect to DStore appears?
    - 6.5.6 What do I do if a DTS synchronization task is not automatically resumed after network recovery?
    - 6.5.7 How do I prevent binary log loss due to an extended interruption between the primary and secondary databases?
  - 6.6 OSS
    - 6.6.1 How do I manually restore data synchronization between OSS buckets?
    - 6.6.2 What do I do if OSS buckets fail to be protected?
  - 6.7 MaxCompute
    - 6.7.1 Why am I unable to find MaxCompute projects when I configure a synchronization entity in ASR-DR?
  - 6.8 ApsaraMQ
    - 6.8.1 How do I view the message details of primary and secondary ApsaraMQ instances?
    - 6.8.2 How do I reset a consumer offset by running a command?
- 7 FAQ about data consistency verification for products that support DR
  - 7.1 Perform full data verification and synchronization between RDS and PolarDB-X databases
  - 7.2 Track the incremental data of a PolarDB-X instance
  - 7.3 Verify Tablestore data consistency
  - 7.4 Verify MaxCompute data consistency
- 8 Command references
  - 8.1 Use CLISH commands
  - 8.2 Commands
  - 8.3 Synchronization entities
    - 8.3.1 skip-entity
    - 8.3.2 suspend-entity
    - 8.3.3 stepover-entity
    - 8.3.4 reprotect-entity
    - 8.3.5 redo-entity
    - 8.3.6 force-switch
  - 8.4 Cloud Center
    - 8.4.1 del-cloud-instance
    - 8.4.2 del-cloud-center
  - 8.5 Protection groups
    - 8.5.1 create-empty-pg
    - 8.5.2 show-pg-sync-entity
    - 8.5.3 delete-pg-shell
    - 8.5.4 move-sync-entity
  - 8.6 Disaster recovery plans
    - 8.6.1 plan-query
    - 8.6.2 plan-query-ex
    - 8.6.3 plan-force-delete
  - 8.7 VPC
    - 8.7.1 vpc-register-app
    - 8.7.2 vpc-show-registered-app
    - 8.7.3 vpc-remove-registered-app
    - 8.7.4 vpc-grant-access
    - 8.7.5 vpc-show-grant-access
    - 8.7.6 vpc-cancel-grant-access
  - 8.8 PolarDB for Xscale (PolarDB-X)
    - 8.8.1 xdm-clear-data
  - 8.9 AnalyticDB for MySQL V3.0
    - 8.9.1 adb-force-start-sync
  - 8.10 Configurations
    - 8.10.1 param-add-param
    - 8.10.2 param-modify-param
    - 8.10.3 param-query-param
    - 8.10.4 param-refresh-param
    - 8.10.5 param-modify-params
    - 8.10.6 param-query-params
  - 8.11 Alerts
    - 8.11.1 alarm-create
    - 8.11.2 alarm-query
    - 8.11.3 send-alarm-msg
  - 8.12 Alert rules
    - 8.12.1 rule-create
    - 8.12.2 rule-query
    - 8.12.3 rule-switch
    - 8.12.4 rule-update
    - 8.12.5 rule-delete
  - 8.13 Monitored metrics
    - 8.13.1 monitor-item-query
- 9 Appendix
  - 9.1 Look up the Internet domain and intranet domain names
  - 9.2 Look up the DNS address
  - 9.3 Configure DNS forwarding
  - 9.4 Configure DTS parameters
  - 9.5 Configure dedicated lines
    - 9.5.1 AddDCInterConnection
    - 9.5.2 AddExternalConnection

w

## 1 Overview

This topic describes the purpose of, requirements on, and usage notes for performing O&M operations on ASR for Geo-disaster Recovery (ASR-DR). This topic also describes how to seek help.

### 1.1 Purpose

This guide aims to help O&M engineers perform preventive maintenance on ASR for Geodisaster Recovery (ASR-DR) to ensure the stability of the system. O&M engineers can follow the instructions in this guide to handle the system issues that are identified during maintenance. If O&M engineers encounter system issues that are not covered in this guide, they can contact Apsara Stack technical support.

### 1.2 Requirements

O&M engineers must possess IT skills, including the knowledge of computer networks, computer operations, and troubleshooting. O&M engineers must pass the related training and learn the knowledge for ASR for Geodisaster Recovery (ASR-DR). The required knowledge includes the usage and maintenance of the tools for all modules.

> **Important:** During the maintenance, O&M engineers must comply with operation procedures to ensure personal safety and system security. No part of user data may be copied or disseminated in any form or by any means without prior written consent from users.

### 1.3 Usage notes

To ensure system stability and prevent unexpected events, O&M engineers must comply with the following guidelines:

**Hierarchical permission management**

Permissions on networks, devices, systems, and data are granted based on the services and roles of O&M engineers. This prevents system faults that are caused by unauthorized operations.

**System security**

Before O&M engineers perform operations on the system, they must be clearly aware of the impacts of the operations. This ensures that the system is not affected by high-risk operations. O&M engineers must clearly record the details about the issues that are encountered during the operations. This helps troubleshoot the issues.

**Personal safety and data security**

O&M engineers must take measures to ensure safety based on device manuals when they use electrical equipment. O&M engineers must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

O&M engineers can contact Apsara Stack technical support for help during the maintenance. ure

## 2 Architecture

### 2.1 Component architecture

This topic describes the internal and external components on which ASR for Geo-disaster Recovery (ASR-DR) depends.

### 2.2 Server roles

This topic describes the server roles that are used by different services of ASR for Geo-disaster Recovery (ASR-DR). This helps O&M engineers identify faults.

| Project | Cluster | Service | Server role | Description |
|---|---|---|---|---|
|   |   |   | asrdr- backend.backend | Manages the backend services of ASR-DR. |

| Apsara Stack Resilien | ce |   |   |   |
|---|---|---|---|---|
| ASR-DR | asrdrCluster | asrdr-backend |   |   |
|   |   |   | asrdr- backend.dbinit | Initializes the ASR-DR database. |
|   |   |   | asrdr- backend.ServiceT est | Performs testing on backend services of ASR- DR. |
|   |   | asrdr-portal | asrdr-portal.ops- poral | Manages the frontend services of ASR-DR in the Apsara Uni- manager Operations Console. |
|   |   |   | asrdr-portal.portal | Manages the frontend services of ASR-DR in the Apsara Uni- manager Management Console. |

O&M console

## 3 ASR-DR O&M console

The O&M console of ASR for Geo-disaster Recovery (ASR-DR) provides the following features: service O&M, O&M on platform basic capabilities, and disaster recovery O&M.

### 3.1 Log on to the O&M console of ASR-DR

**ASR-DR**

This topic describes how to log on to the O&M console of ASR for Geo-disaster Recovery (ASR- DR).

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: region -id.ops.console.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console. Press
the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

O&M console
3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar, choose **Platform > Disaster Recovery > ASR for Geo-disaster**
**Recovery**.

### 3.2 Homepage

The homepage of the ASR for Geo-disaster Recovery (ASR-DR) O&M console displays information in the following sections: Authorization usage statistics, Node task load statistics, Total number of abnormal synchronization entities, Unassigned task statistics, Bandwidth Usage, and Dedicated Line traffic usage.

> **Important:** When you deploy the ASR-DR O&M console, you must also configure the information about the instances that are connected over Express Connect circuits. Otherwise, data of the instances cannot be displayed in the line charts on the homepage.
> To configure Express Connect circuit-connected instance information, contact Apsara Stack engineers.

O&M console

**Sections**

| Section | Description |
|---|---|
| Authorization usage statistics | Displays the usage of protection groups and synchronization entities in a doughnut chart. The blue color indicates the usage of protection groups. The yellow color indicates the usage of synchronization entities. The numerator represents the used quota and the denominator represents the total authorized quota. |
| Node task load statistics | Displays the number of tasks distributed on each ASR-DR node in a doughnut chart. |
| Total number of abnormal synchronization entities | Displays the number of abnormal synchronization entities based on the statistics of disaster recovery services in a doughnut chart. |
| Unassigned task statistics | Displays the unassigned synchronization tasks in a doughnut chart. |
| Bandwidth Usage | Displays the traffic and bandwidth usage of ApsaraDB RDS and Object Storage Service (OSS) in line charts. |
| Dedicated Line traffic usage | Displays the inbound and outbound traffic usage of the instances that are connected over Express Connect circuits to ASR-DR in line charts. |

### 3.3 Disaster recovery monitoring

O&M console

#### 3.3.1 Check cluster status at the cloud platform side

**platform side**

You can check the status of the platforms at the primary and secondary sites and the cluster status of disaster recovery services. Abnormal check items are reported in the alert statistics and the number of alerts categorized from P1 to P4 levels is counted. The error information is also sent to the alert management module of the Apsara Uni-manager Operations Console.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery Monitoring** > **Cluster Status**
**at Platform Side**.
On the Cluster Status at Platform Side page, the information is displayed in the Alert Statistics, Platform, and Cluster Status for Disaster Recovery Products sections. Alerts are categorized into the following levels: P1: Critical P2: Major P3: Minor P4: Informational

> **Note:** To switch to another primary site, select the primary site from the **Primary Cloud** drop-down list.
> To view the detailed check result of an abnormal check item, move the pointer over the
> icon to the right of the check item status.

#### 3.3.2 Check cross-cloud network access

You can check whether the domain name resolutions are consistent and the networks and ports are connected between the primary and secondary sites.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
O&M console
2. In the left-side navigation pane, choose **Disaster Recovery Monitoring** > **Cross-cloud**
**Network Access**.
On the Cross-cloud Network Access page, view the network connectivity status between the primary and secondary sites.

> **Note:** To switch to another primary site, select the primary site from the **Primary Cloud** drop-down list in the upper-part of the page.
> To switch to another service category, select **Storage Products**, **Database** **Products**, or **Big Data Products** in the upper-part of the page. The network connectivity status between services of the selected category is displayed.
> To view only cloud services whose network connectivity is abnormal, select **View** **Exceptional Entities Only** in the upper-part of the page.

#### 3.3.3 Monitor the status of synchronization entities

**entities**

When you monitor the status of synchronization entities, the metrics of protection groups and cloud services are monitored. The metrics of protection groups include the number of synchronization entities in each protection group, synchronization status, and maximum synchronization latency. The metrics of cloud services include the synchronization status, synchronization latency, and status of primary and secondary instances. If the synchronization status of a protection group is abnormal, an alert is reported. The system counts the number of alerts that are categorized into the P1 to P4 levels. The error information is also sent to the alert management module of the Apsara Uni-manager Operations Console.

**Procedure**

1. Log on to the O&M console of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery Monitoring** > **Synchronization**
**Entity Status**.
The Synchronization Entity Status page displays the alert statistics, protection group names, number of synchronization entities in each protection group, synchronization status, and maximum synchronization latency. O&M console
3. Find a protection group and click **View synchronization entity check results** in the
**Actions** column. In the panel that appears, the following information about each
synchronization entity in the protection group is displayed: synchronization entity name, cloud service, synchronization status, synchronization latency, synchronization latency check result, primary instance status, and secondary instance status.

### 3.4 Basic capability O&M

This topic describes the basic capability O&M features of Apsara Stack Resilience for Geodisaster Recovery (ASR-DR). In the O&M console of ASR-DR, the basic capability O&M features of ASR-DR are categorized into the following modules: cloud information management, parameter management, node management, virtual private cloud (VPC) management, capacity management, and data upgrade. The following table describes the features.

| Module | Description | Remarks | Operation |
|---|---|---|---|
| Cloud information management | You can view the information about all clouds and remove the clouds that you no longer need. | Before you remove a cloud, make sure that the cloud does not contain resources such as protection groups or plans. If you remove a cloud, the information about the cloud is also deleted, including the registered VPC, region configurations, and cloud service configurations. The region configurations include the services that support disaster recovery in the specified region and service status. | Refresh data: Click the icon to refresh data. Change the display mode: Click the icon and select Default or Compact to change the display mode. Customize displayed columns: Click the icon and select the columns that you want to display on the page. Enable or disable the full screen mode: Click the icon to display data in full screen mode. Then, click the icon to disable the full screen mode. |

O&M console

| Parameter management |   | You can dynamically configure service parameters. | N/A | 1. On the Parameter Management page, find the service whose parameters you want to manage and click the corresponding tab. On the tab that appears, configure the parameters as prompted. 2. Click Submit. |
|---|---|---|---|---|
| Node management |   | You can view the information about nodes in your ASR-DR cluster and view unassigned tasks. To view the tasks that are being run on a node, find the node and click Details in the Actions column. | N/A | Click Show unassigned tasks to display the list of unassigned tasks. |
| VPC manag ement | Regist ration inform ation mana geme nt | If a cloud is registered with a VPC, you can view and delete the registration information. If a cloud is not registered with a VPC, you can register the cloud with a VPC. If a VPC authorization error occurs or a VPC fails to be accessed, you can check the validity of the registration information by calling a specific operation to check whether the values of the appId and addressPoolId parameters are still valid. | N/A | Refresh data: Click the icon to refresh data. Change the display mode: Click the icon and select Default or Compact to change the display mode. Customize displayed columns: Click the icon and select the columns that you want to display on the page. Enable or disable the full screen mode: Click the icon to display data in full screen mode. Then, click the icon to disable the full screen mode. |

O&M console

|   | Autho rizatio n inform ation mana geme nt | If a cloud is authorized to be accessed within a VPC, you can view the VPC authorization information. If a cloud is not authorized to be accessed within a VPC, you can authorize the cloud to be accessed within a VPC. | N/A | 1. On the Authorization Information in VPC tab of the VPC Management page, configure the Instance, Region Name, and Instance ID parameters. 2. Click Search. |
|---|---|---|---|---|
| Capacity management |   | You can view the resource usage of protection groups and synchronization entities. | N/A | N/A |
| Data upgrade |   | You can upgrade all data of protection groups and disaster recovery plans. | Existing users are required to upgrade data after a version update. | 1. On the Data Upgrade page, click Data Upgrade. 2. In the message that appears, click OK. 3. Upgrade data as prompted. |

#### 3.4.1 Manage cloud service information

Before you can use Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) in the Apsara Uni-manager Management Console, you must configure the primary and secondary clouds in the Apsara Uni-manager Operations Console. After you add a primary cloud, you must configure the cloud services that support disaster recovery and the addresses of the cloud services for the primary cloud. This way, ASR-DR can perform disaster recovery for resource instances in the primary cloud. This topic describes the configurations for cross-cloud disaster recovery. When you log on to the O&M console of ASR-DR from the Apsara Uni-manager Operations Console for the first time, you must configure the secondary cloud, as shown in the following figure. To configure the secondary cloud, go to the Cloud Information Management page. On the Cloud Information Management page, click **Edit** in the **Disaster Recovery Cloud** section. You can also find the secondary cloud in the All Clouds section and click **Edit** in the **Actions** column. After the secondary cloud is configured, it enters the Running state. For more information about how to configure the parameters, see the table that describes the parameters in the "Procedure" section of this topic. O&M console

**Procedure**

1. Log on to the O&M console of ASR-DR.
2. In the left-side navigation pane, choose **General > Cloud Information Management**.
3. On the Cloud Information Management page, click **Add Cloud**. In the Add Cloud dialog box,
configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Cloud Name | The name of the cloud center. You can customize the name for easy identification. The name must be 4 to 20 characters in length, and can contain letters, digits, hyphens (-), underscores ( ), and periods (.). _ |
| Cloud Edition | The edition of the primary cloud. Valid values: Enterprise Edition and Agile Edition. In this example, Enterprise Edition is selected. |

O&M console

| Cloud Management | The management console of the primary cloud. Valid values: Apsara Uni-manager Management Console: The secondary cloud calls the operations of the Apsara Stack API (ASAPI) to obtain the information about the primary cloud. ASR for Geo-disaster Recovery: The secondary cloud calls the API operations of ASR-DR to obtain the information about the primary cloud. In this example, this value is selected. Note We recommend that you use ASR-DR as the management console of the primary cloud. |
|---|---|
| Cloud Management API Endpoint | If you select Apsara Uni-manager Management Console for the Cloud Management parameter, enter the endpoint of the ASAPI in the primary cloud. If you select ASR for Geo-disaster Recovery for the Cloud Management parameter, enter the endpoint of ASR-DR in the primary cloud. For more information about how to obtain the endpoint of ASR-DR, see Obtain the endpoint of ASR-DR. |
| Operations Administrator AccessKey ID and Operations Administrator AccessKey Secret | The AccessKey ID and AccessKey secret of the account that assumes the operations administrator role to log on to the primary cloud. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. |

4. Click **Verify**. After the verification is passed, click **OK**.
5. Configure cloud services.
i. On the Cloud Information Management page, find the cloud that you want to manage and click **Configuration** in the **Actions** column to go to the **Cloud Service Configuration** page. O&M console ii. In the **Basic Services** section, find the cloud service that you want to configure and click the icon to configure related parameters. The following table describes the parameters.

> **Important:** If you set the Cloud Management parameter to **Apsara Uni-manager** **Management Console**, you must check whether the automatically specified configuration information about each cloud service is correct. For more information about how to obtain the configuration information about each cloud service, see Obtain the configuration information of the primary cloud instance.
> If you set the Cloud Management parameter to **ASR for Geo-disaster** **Recovery**, you do not need to check the automatically specified configuration information about each cloud service. The information is correct.

|   | Cloud service | Parameter | Description |
|---|---|---|---|
|   | Apsara Uni- manager Management Console | ASCM address | The address that is used for single sign-on (SSO), authentication, and resource retrieval. Set this parameter to the value of the ascm-portal.domain variable of the oneService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. |
|   |   | ASAPI Endpoint | The endpoint of the ASAPI. Set this parameter to the value of the asapi.gateway.endpoint variable of the asapi service deployed on the primary cloud. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |
|   |   | ASCM POP Address | The address that is used to call the POP API of the Apsara Uni-manager Management Console. If the cloud is deployed in the central region, the value is in the ascm. {internet-domain} format. If the cloud is deployed in a general region, the value is in the ascm.{region}. {internet-domain} format. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |
|   |   | DTS address | The address that is used to synchronize data between database services. ASR-DR automatically sets the address to the value of the dts.openapi.endpoint variable of the dts-dts service deployed on the primary cloud. You must check whether the value is correct. |

|   | {internet-domain} |
|---|---|

| ascm.{region}. |   |
|---|---|

|   | {internet-domain} |
|---|---|

O&M console

|   |   | Set the address to the value of the dts.check.dns:dts.check.port variable of the dts-dts service deployed on the primary cloud. For DTS Check Address more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. Set the token to the value of the dts.check.token variable of the dts-dts service deployed on the DTS Check primary cloud. For more information about how to obtain Access Token the token, see Obtain the configuration information of the primary cloud instance. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. The address that is used to query the environment information. Set the address to the value of the console.domain variable of the oneService oneConsole service deployed on the primary cloud. For more address information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. The address that is used to register VPCs and connect to PolarDB-X 1.0 instances and ApsaraDB RDS instances that are deployed in VPCs. ASR-DR automatically sets the VPC address address to the value of the vpc- inner.openapi.endpoint variable of the vpc- yaochi service deployed on the primary cloud. You must check whether the value is correct. The address that is used to verify the AccessKey ID and AccessKey secret of a RAM user. Set the address to the value of the ram-openapi.endpoint variable of the ram-ramService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the RAM address primary cloud instance. Important The RAM address must be the address of RAM deployed in the central region. The address that is used to authenticate a RAM user. Set the address to the value of the ram-slave.endpoint RAM Slave variable of the ram-ramService service deployed on Endpoint the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. |   |
|---|---|---|---|
|   |   | DTS Check Address | Set the address to the value of the dts.check.dns:dts.check.port variable of the dts-dts service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |
|   | Data Transmission Service (DTS) |   |   |
|   |   | DTS Check Access Token | Set the token to the value of the dts.check.token variable of the dts-dts service deployed on the primary cloud. For more information about how to obtain the token, see Obtain the configuration information of the primary cloud instance. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |
|   | OneConsole | oneConsole address | The address that is used to query the environment information. Set the address to the value of the console.domain variable of the oneService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. |
|   | Virtual Private Cloud (VPC) | VPC address | The address that is used to register VPCs and connect to PolarDB-X 1.0 instances and ApsaraDB RDS instances that are deployed in VPCs. ASR-DR automatically sets the address to the value of the vpc- inner.openapi.endpoint variable of the vpc- yaochi service deployed on the primary cloud. You must check whether the value is correct. |
|   | Resource Access Management (RAM) | RAM address | The address that is used to verify the AccessKey ID and AccessKey secret of a RAM user. Set the address to the value of the ram-openapi.endpoint variable of the ram-ramService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. Important The RAM address must be the address of RAM deployed in the central region. |
|   |   | RAM Slave Endpoint | The address that is used to authenticate a RAM user. Set the address to the value of the ram-slave.endpoint variable of the ram-ramService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. |

| vpc- |   |
|---|---|

|   | inner.openapi.endpoint |
|---|---|
|   | yaochi |

|   | ram-openapi.endpoint |
|---|---|
| ram-ramService |   |

|   | ram-slave.endpoint |
|---|---|
| ram-ramService |   |

O&M console

|   |   | STS Address | The address that is used to obtain the Security Token Service (STS) token of your Apsara Stack tenant account. Set the address to the value of the sts- openapi.endpoint variable of the ram-ramService service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. Important The STS address must be the address of STS deployed in the central region. |
|---|---|---|---|
|   | ASR-DR | asrdr AK | The AccessKey ID of ASR-DR. You can call Remote System Management (RSM) in the primary cloud to verify the AccessKey pair. For more information, see Obtain an AccessKey pair. |
|   |   | asrdr SK | The AccessKey secret of ASR-DR. You can call RSM in the primary cloud to verify the AccessKey pair. For more information, see Obtain an AccessKey pair. |
|   |   | asrdr api endpoint | The endpoint of the ASR-DR API. Set the endpoint to the value of the asrdr api endpoint variable of the _ _ asrdr-backend service deployed on the primary cloud. This parameter is automatically configured by ASR- DR. You must check whether the value is correct. |
|   |   | AccessKey ID of Account to Log on to ASR-DR | The AccessKey ID of your Apsara Stack tenant account that is used to log on to the ASR-DR console. You can use the AccessKey ID to obtain STS tokens. Set the AccessKey ID to the value of the account.asr.accesskey-id variable. For more information about how to obtain the AccessKey ID, see Obtain the configuration information of the primary cloud instance. |
|   |   | AccessKey Secret of Account to Log on to ASR-DR | The AccessKey secret of your Apsara Stack tenant account that is used to log on to the ASR-DR console. You can use the AccessKey secret to obtain STS tokens. Set the AccessKey secret to the value of the account.asr.accesskey-secret variable. For more information about how to obtain the AccessKey secret, see Obtain the configuration information of the primary cloud instance. |

| sts- |   |
|---|---|

|   | openapi.endpoint |
|---|---|

|   | asrdr api endpoint _ _ |
|---|---|
| asrdr-backend |   |

O&M console

| Apsara Infrastructure Management |   | Apsara Infrastructure | The AccessKey ID that is used to call the POP API of Apsara Infrastructure Management. Set the AccessKey ID to the value of the account.defaultUser.accesskey- id variable. For more information about how to obtain the AccessKey ID, see Obtain the configuration information of the primary cloud instance. |   |   |
|---|---|---|---|---|---|
|   |   | Management | id |   |   |
|   |   | AccessKey ID |   |   |   |
|   |   | Apsara Infrastructure Management AccessKey Secret | The AccessKey secret that is used to call the POP API of Apsara Infrastructure Management. Set the AccessKey secret to the value of the account.defaultUser.accesskey-secret variable. For more information about how to obtain the AccessKey secret, see Obtain the configuration information of the primary cloud instance. |   |   |
|   |   | Apsara Infrastructure Management Endpoint | The endpoint that is used to call the API of Apsara Infrastructure Management to query the status of clusters. ASR-DR automatically sets the endpoint to the value of the api server.endpoint variable of the tianji- _ endpoint service deployed on the primary cloud. You must check whether the value is correct. |   |   |
|   |   |   |   | tianji- |   |
| RSM |   | RSM Endpoint | The endpoint that is used to call the RSM API to conduct network checks. ASR-DR automatically sets the endpoint to the value of the rsm.api.domain variable of the rsm service deployed on the primary cloud. You must check whether the value is correct. |   |   |
| Parthenon |   | Parthenon Endpoint | The endpoint that is used to call the Parthenon API to check the cross-cloud network connectivity of services deployed on the PaaS platform. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. Format: region.api.parthenon.intranet-domain. You must check whether the value is correct based on the region and intranet-domain parameters in the kv.conf configuration file of the Apsara Infrastructure Management cluster that is at desired state. |   |   |

|   |   | api server.endpoint _ |
|---|---|---|
|   | endpoint |   |

iii. In the **Disaster Recovery Services** section, click the icon. In the Add Configuration Information of Cloud Service dialog box, select a cloud service and configure related parameters. The parameters vary based on the selected cloud service. The following table describes the parameters.

| Cloud service | Parameter | Description |
|---|---|---|

O&M console

| Object Storage Service (OSS) | OSS address | The address that is used to call the synchronization operations of OSS and query OSS instances. ASR-DR automatically sets the address to the value of the api-endpoint variable of the oss-server service deployed on the primary cloud. You must check whether the value is correct. |
|---|---|---|
|   | POP Address of OSS Operations and Maintenance System | The address that is used to call the POP API of OSS. ASR-DR automatically sets the address to the value of the pop-api-endpoint variable of the oss-chiji service deployed on the primary cloud. You must check whether the value is correct. |
|   | OSS-POP AK | The AccessKey ID of the opsadmin account that is used to log on to the Apsara Uni-manager Operations Console. The AccessKey ID is verified when ASR-DR calls the POP API of OSS. |
|   | OSS-POP SK | The AccessKey secret of the opsadmin account that is used to log on to the Apsara Uni-manager Operations Console. The AccessKey secret is verified when ASR-DR calls the POP API of OSS. |
|   | PrimaryKey of OSS Proxy User | The UID of the proxy user that is authorized to access OSS buckets. The UID is generated when you create the proxy user in the Apsara Uni- manager Management Console. For more information about how to obtain the UID, see the Configure OSS for disaster recovery topic of Apsara Stack v3.*** Deployment Guide. |
|   | OTS Tunnel Endpoint | The endpoint that is used to call the synchronization operations of the Tablestore Tunnel Service. ASR-DR automatically sets the endpoint to the value of the ocm.pop tablestore endpoint variable of the _ _ TableStoreOCM service deployed on the primary cloud. You must check whether the value is correct. |
|   | PrimaryKey of Level-1 Organization of OTS Proxy | The UID of the level-1 organization that is verified when Tablestore accesses instances deployed on the primary cloud. The UID is generated when you create the level-1 organization in the Apsara Uni-manager Management Console. For more information about how to obtain the UID, see the Configure Tablestore for disaster recovery topic of Apsara Stack v3.*** Deployment Guide. |

|   | pop-api-endpoint |
|---|---|
| oss-chiji |   |

O&M console

| Tablestore Note If you select ASR for Geo-disaster Recovery for the Cloud |   |   |   |   |
|---|---|---|---|---|
|   |   |   | AccessKey ID of Level-1 Organization of OTS Proxy | The AccessKey ID that is verified when Tablestore accesses instances deployed on the primary cloud. The AccessKey ID is generated when you create the level-1 organization in the Apsara Uni- manager Management Console. For more information about how to obtain the AccessKey ID, see the Configure Tablestore for disaster recovery topic of Apsara Stack v3.*** Deployment Guide. |
|   | Note If you select ASR for Geo-disaster Recovery for the Cloud |   |   |   |
|   | Management parameter, a proxy account for Tablestore is automatically registered. In cross- cloud scenarios , the configura tions of the primary and secondar y clouds are registere d after the primary cloud is configure d. You must configure the secondar y cloud before you configure the primary cloud. |   |   |   |
|   |   |   | AccessKey Secret of Level-1 Organization of OTS Proxy | The AccessKey secret that is verified when Tablestore accesses instances deployed on the primary cloud. The AccessKey secret is generated when you create the level-1 organization in the Apsara Uni-manager Management Console. For more information about how to obtain the AccessKey secret, see the Configure Tablestore for disaster recovery topic of Apsara Stack v3.* ** Deployment Guide. |

O&M console

| In cross- region scenarios , the configura tions of the primary and secondar y regions are registere d after the primary region is configure d. You must configure the secondar y region before you configure the primary region. |   |   |
|---|---|---|
|   | OTS OCM Internal Endpoint (for tunnel management) | The endpoint that is used to register a Tablestore proxy account. Set the endpoint to the value of the ocm.endpoint variable of the TableStoreOCM service deployed on the primary cloud. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |

O&M console

|   | ApsaraDB RDS | RDS address | The address that is used to call operations to query ApsaraDB RDS instances and grant permissions. ASR-DR automatically sets the address to the value of the rds.openapi.endpoint variable of the rds- yaochi service deployed on the primary cloud. You must check whether the value is correct. |   |   |
|---|---|---|---|---|---|
|   |   |   |   | rds- |   |
|   | PolarDB-X | PolarDB-X Address | The address that is used to call operations to query PolarDB-X 1.0 instances and grant permissions. ASR-DR automatically sets the address to the value of the prectrl.api variable of the drds-console service deployed on the primary cloud. You must check whether the value is correct. |   |   |
|   | PolarDB | PolarDB Address | The address that is used to call operations to query PolarDB instances and grant permissions. Set the address to the value of the polardb.openapi-vpc.endpoint variable of the polardb-yaochi service deployed on the primary cloud. For more information about how to obtain the address, see Obtain the configuration information of the primary cloud instance. This parameter is automatically configured by ASR-DR. You must check whether the value is correct. |   |   |
|   | ApsaraMQ | MQ Router OnsAddr | The address that is used to call the synchronization operations of ApsaraMQ. ASR-DR automatically sets the address to the value of the router.onsAddr variable of the mq- router service deployed on the primary cloud. You must check whether the value is correct. |   |   |
|   |   | MQ address | The address that is used to call the operations on ApsaraMQ topics. ASR-DR automatically sets the address to the value of the console.domain variable of the mq-console service deployed on the primary cloud. You must check whether the value is correct. |   |   |
|   |   | MQ AK | The AccessKey ID that is verified when ASR-DR calls the ApsaraMQ API. Set the AccessKey ID to the value of the onsInnerApiAccessKey variable of the mq-console service deployed on the primary cloud. For more information about how to obtain the AccessKey ID, see Obtain the configuration information of the primary cloud instance. |   |   |

|   |   | rds.openapi.endpoint |
|---|---|---|
|   | yaochi |   |

|   | prectrl.api |
|---|---|
| drds-console |   |

|   |   | router.onsAddr |
|---|---|---|
|   | router |   |

|   | console.domain |
|---|---|
| mq-console |   |

|   | onsInnerApiAccessKey |
|---|---|
| mq-console |   |

O&M console

|   |   | MQ SK | The AccessKey secret that is verified when ASR- DR calls the ApsaraMQ API. Set the AccessKey secret to the value of the onsInnerApiSecretKey variable of the mq- console service deployed on the primary cloud. For more information about how to obtain the AccessKey secret, see Obtain the configuration information of the primary cloud instance. |
|---|---|---|---|
|   |   | DNS Control Endpoint | The endpoint that is used to call the DNS Control API. Set the endpoint to the value of the dns control.pop domain variable of the _ _ dnsService service deployed on the primary cloud. For more information about how to obtain the endpoint, see Obtain the configuration information of the primary cloud instance. |
|   | Apsara Stack DNS |   |   |
|   |   | DNS address | The address that is used to call the Apsara Stack DNS API. ASR-DR automatically sets the address to the value of the dns universal control.pop domain _ _ _ variable of the dnsService service deployed on the primary cloud. You must check whether the value is correct. |
|   |   | DNS AK | The AccessKey ID of the disaster recovery organization that you created in the Apsara Uni- manager Management Console. The AccessKey ID is verified when ASR-DR calls the Apsara Stack DNS API. |
|   |   | DNS SK | The AccessKey secret of the disaster recovery organization that you created in the Apsara Uni- manager Management Console. The AccessKey secret is verified when ASR-DR calls the Apsara Stack DNS API. |
|   |   | BCC API Address | The address that is used to call the API of Configuration Center of Apsara Big Data Manager (ABM) in the primary cloud. ASR-DR automatically sets the address to the value of the api.endpoint variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. |
|   |   | BCC App | The name of the application in Configuration Center of ABM. ASR-DR automatically sets the name to the value of the maxgraph-app variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. |

|   |   | onsInnerApiSecretKey |
|---|---|---|
|   | console |   |

| mq- |   |
|---|---|

|   | maxgraph-app |
|---|---|
| bcc-web |   |

O&M console

|   | DataWorks | The AppKey of the application in Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-key BCC Key variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. The AuthUserKey information of Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-passwd BCC Password variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. The AuthUser information of Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-user variable of BCC User the bcc-web service deployed on the primary cloud. You must check whether the value is correct. The endpoint that is used to call operations to query ApsaraDB for HBase clusters and grant permissions. ASR-DR automatically sets the endpoint to the value of the ApsaraDB for HBase hbase.openapi.endpoint variable of the Cluster Endpoint hbase-yaochi service deployed on the primary cloud. You must check whether the value is correct. The endpoint that is used to call the operations of Lindorm. ASR-DR automatically sets the endpoint to the value of the lindorm pop endpoint Lindorm Endpoint _ _ variable of the lindorm service deployed on the primary cloud. You must check whether the value is correct. The AccessKey ID that is verified when ASR-DR calls the API of Lindorm Tunnel Service (LTS). Set the AccessKey ID to the value of the LTS Authentication account.asr.accesskey-id variable in the AccessKey ID primary cloud. For more information about how to obtain the AccessKey ID, see Obtain the configuration information of the primary cloud instance. The AccessKey secret that is verified when ASR- DR calls the LTS API. Set the AccessKey secret to the value of the account.asr.accesskey- LTS Authentication secret variable in the primary cloud. For more AccessKey Secret information about how to obtain the AccessKey secret, see Obtain the configuration information of the primary cloud instance. |   |
|---|---|---|---|
|   |   | BCC Key | The AppKey of the application in Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-key variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. |
|   |   | BCC Password | The AuthUserKey information of Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-passwd variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. |
|   |   | BCC User | The AuthUser information of Configuration Center of ABM. ASR-DR automatically sets the value to the value of the maxgraph-user variable of the bcc-web service deployed on the primary cloud. You must check whether the value is correct. |
|   | ApsaraDB for HBase | ApsaraDB for HBase Cluster Endpoint | The endpoint that is used to call operations to query ApsaraDB for HBase clusters and grant permissions. ASR-DR automatically sets the endpoint to the value of the hbase.openapi.endpoint variable of the hbase-yaochi service deployed on the primary cloud. You must check whether the value is correct. |
|   | Lindorm | Lindorm Endpoint | The endpoint that is used to call the operations of Lindorm. ASR-DR automatically sets the endpoint to the value of the lindorm pop endpoint _ _ variable of the lindorm service deployed on the primary cloud. You must check whether the value is correct. |
|   |   | LTS Authentication AccessKey ID | The AccessKey ID that is verified when ASR-DR calls the API of Lindorm Tunnel Service (LTS). Set the AccessKey ID to the value of the account.asr.accesskey-id variable in the primary cloud. For more information about how to obtain the AccessKey ID, see Obtain the configuration information of the primary cloud instance. |
|   |   |   | The AccessKey secret that is verified when ASR- DR calls the LTS API. Set the AccessKey secret to the value of the account.asr.accesskey- secret variable in the primary cloud. For more information about how to obtain the AccessKey secret, see Obtain the configuration information of the primary cloud instance. |
|   |   | LTS Authentication AccessKey Secret | secret |

|   | maxgraph-key |
|---|---|
| bcc-web |   |

|   | maxgraph-passwd |
|---|---|
| bcc-web |   |

|   | lindorm pop endpoint _ _ |
|---|---|
| lindorm |   |

| account.asr.accesskey- |   |
|---|---|

|   |   | ions -DR | Apsara Stack Resilienc |   |   |   |
|---|---|---|---|---|---|---|
|   |   | MongoDB Endpoint | The endpoint that is used to call operations to query ApsaraDB for MongoDB instances and grant permissions. ASR-DR automatically sets the endpoint to the value of the mongodb.openapi- vpc.endpoint variable of the mongodb- yaochi service deployed on the primary cloud. You must check whether the value is correct. |   |   |   |
|   | ApsaraDB for MongoDB |   |   |   |   |   |
|   | KVStore for Redis | Redis Endpoint | The endpoint that is used to call operations to query KVStore for Redis instances and grant permissions. ASR-DR automatically sets the endpoint to the value of the kvstore.openapi- vpc.endpoint variable of the kvstore- yaochi service deployed on the primary cloud. You must check whether the value is correct. |   |   |   |
|   |   |   |   | kvstore.openapi- |   |   |
|   |   |   |   |   | kvstore- |   |
|   | Hologres | Hologres Management Endpoint | The endpoint that is used to call operations to query Hologres instances and grant permissions. ASR-DR automatically sets the endpoint to the value of the holo-manager.endpoint variable of the hologres-init service deployed on the primary cloud. You must check whether the value is correct. |   |   |   |
|   |   | Hologres-POP Endpoint | The endpoint that is used to call the POP API of Hologres. ASR-DR automatically sets the endpoint to the value of the pop holo remote recover dns variable of the _ _ _ _ hologres-init service deployed on the primary cloud. You must check whether the value is correct. |   |   |   |
|   | Elastic Compute Service (ECS) | HDR Address | The address that is used to call the High Availability Disaster Recovery (HDR) API. ASR-DR automatically sets the address to the value of the hdr.openapi.endpoint variable of the cds- bcdr service deployed on the primary cloud. You must check whether the value is correct. |   |   |   |

| mongodb.openapi- |   |
|---|---|

|   |   | vpc.endpoint |
|---|---|---|
|   |   | yaochi |

|   |   | vpc.endpoint |
|---|---|---|
|   |   | yaochi |

|   |   | hdr.openapi.endpoint |
|---|---|---|
|   | bcdr |   |

| cds- |   |
|---|---|

O&M console

| DataHub | DataHub Endpoint | The endpoint that is used to call the DataHub API. ASR-DR automatically sets the endpoint to the value of the datahub frontend.endpoint _ variable of the datahub-frontend service deployed on the primary cloud. You must check whether the value is correct. |
|---|---|---|

iv. After all cloud services are configured, go back to the **Cloud Information Management** page to perform other operations.

**What to do next**

The following table describes the operations that you can perform after a cloud is added.

| Operation | Description |
|---|---|
| Edit the cloud | 1. Find the cloud and click Edit in the Actions column. 2. In the Edit Cloud dialog box, modify the parameters. 3. After you complete the modification, click Verify. After the verification is passed, click OK. |
| Remove the cloud | 1. Find the cloud and click Delete in the Actions column. 2. In the Delete Cloud message, click OK. |

#### 3.4.2 Configure the dashboard

This topic describes how to configure disaster recovery regions displayed on the dashboard. After you configure the regions, the geo-disaster recovery data is displayed on the dashboard.

**Scenarios**

**Geo-disaster recovery**: This solution is widely used in industries such as public services,
energy, transportation, and health and medical insurance. This solution is applicable to the following scenarios: High business continuity is required. Strong data consistency is not required. Regional failure prevention is required. The distance between regions is more than 100 km.
**Three data centers across two regions** : This solution is mainly used in the financial
industry and is applicable to the following scenarios: Prevention of city-level natural disasters is required. Regional failure prevention is required. Near zero synchronization latencies for business-critical data are required. The budget is adequate.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **General > Large-screen Map Configuration**.
O&M console
3. On the Large-screen Map Configuration page, click **Create Disaster Recovery Region**. In
the Create Disaster Recovery Region dialog box, configure the parameters described in the following table.

| Parameter | Description |
|---|---|
| Region ID | The ID of the region that you want to use. |
| Region Name | The name of the region. Example: Hangzhou data center. |
| City | The city in which the region resides. |
| Zone | The ID and name of the zone. This parameter is automatically configured by the system. |

4. Click **OK**.

**Related operations**

After you create a disaster recovery region, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| Edit the disaster recovery region | 1. Find the disaster recovery region and click Edit in the Actions column. 2. In the Edit Disaster Recovery Region dialog box, enter a new region name or select another city. 3. Click OK. |
| Delete the disaster recovery region | 1. Find the disaster recovery region and click Delete in the Actions column. 2. In the message that appears, click OK. |

### 3.5 Disaster recovery O&M

This topic describes the disaster recovery O&M features of Apsara Stack Resilience for Geodisaster Recovery (ASR-DR). The disaster recovery O&M features of ASR-DR are categorized into the synchronization entity management and plan management modules. The following table describes the features.

| Module |   | Description | Remarks |
|---|---|---|---|

O&M console

| Synchronization entity management |   | You can view the list and details of protection groups, delete the protection groups and synchronization entities that you no longer need, view the tasks of each synchronization entity, view the step details of each task, view the run logs of each step, retry a step, and skip a step. | If a step of a task fails, you can retry the step. This way, the task continues to be run from this step. If a step of a task fails multiple times, you can skip the step. This is applicable if the skipped step does not affect subsequent steps. This way, the task continues to be run from the next step. |
|---|---|---|---|
| Plan management | Switchover | You can view the records of drill plans and disaster recovery plans that are run, unbind the plans that are run, view the details and step details of each record, view the run logs of each step, retry a step, skip a step, and skip all steps. | If a step of a plan fails multiple times, you can skip all optional steps. Note This operation is generally performed when the primary site fails. In this case, all steps related to the primary site are skipped at a time. |
|   | Switchback |   |   |
|   | Failover |   |   |
|   | Failback |   |   |

#### 3.5.1 Manage synchronization entities

##### 3.5.1.1 Skip a step

The procedure to skip a single step in the synchronization entity management and plan management sections are the same. This topic describes how to skip a single step in the synchronization entity management section.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, view the synchronization entity information. Find
the synchronization entity that you want to manage and click **Task** in the Actions column. O&M console
5. In the panel that appears, click the plus signs (+) to the left of a task to view the steps of the
task.
6. Find a step that is in the **Failed** state and click **Skip** in the Actions column.
7. After the step is skipped, the step changes to the **Skip** state.

**Related operations**

O&M console On the Protection Group page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| Perform advanced search | 1. Configure the Primary Clouds, Protection Group ID, Protection Group Name, and Synchronization Direction parameters. 2. Click Search to search for a specific protection group. If the filter conditions are incorrect, click Reset to clear the filter conditions. |
| Refresh data | Click the icon to refresh the protection group list. |
| Change the display mode | Click the icon and select the Default or Compact display mode. |
| Customize displayed fields | Click the icon and select the fields that you want to display on the page. |
| Enable the full screen mode | Click the icon to display data in full screen mode. Click the icon to disable the full screen mode. |

##### 3.5.1.2 Reperform a single step

The procedure to reperform a single step in the synchronization entity management and plan management sections are the same. This topic describes how to reperform a single step in the synchronization entity management section.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, view the synchronization entity information. Find
the synchronization entity that you want to manage and click **Task** in the Actions column. O&M console
5. In the panel that appears, click the plus signs (+) to the left of a task to view the steps of the
task.
6. Find a step that is in the **Failed** state and click **Retry** in the Actions column.
7. After the step is reperformed, the step changes to the **Complete** state.

**Related operations**

O&M console On the Protection Group page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| Perform advanced search | 1. Configure the Primary Clouds, Protection Group ID, Protection Group Name, and Synchronization Direction parameters. 2. Click Search to search for a specific protection group. If the filter conditions are incorrect, click Reset to clear the filter conditions. |
| Refresh data | Click the icon to refresh the protection group list. |
| Change the display mode | Click the icon and select the Default or Compact display mode. |
| Customize displayed fields | Click the icon and select the fields that you want to display on the page. |
| Enable the full screen mode | Click the icon to display data in full screen mode. Click the icon to disable the full screen mode. |

##### 3.5.1.3 Configure throttling

You can configure throttling only for Object Storage Service (OSS) and ApsaraDB RDS instances.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find a protection group to which OSS or ApsaraDB RDS
instances belong and click **Details** in the **Actions** column.
4. In the synchronization entity list of the **Protection Group Details** page, click **Throttling**
**Configuration** in the **Actions** column.
O&M console
5. In the Throttling Configuration dialog box, configure the parameters described in the following
table and click **OK**.

| Parameter | Description |
|---|---|
| Throttling Dimension | The dimension on which you want to enable throttling. Valid values: Bandwidth: the difference between the highest and lowest frequencies. QPS: the number of requests processed per second. |
| Task Type | The type of the throttling task. Valid values: Incremental Replication: enables throttling only for new data. Historical Replication: enables throttling for all data. Note This parameter is required only when OSS instances are protected. If ApsaraDB RDS instances are protected, you do not need to configure this parameter. |
| Throttling Value (bps) | The custom throttling threshold. |

##### 3.5.1.4 Delete an entity from a protection group

This topic describes how to delete an entity from a protection group.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, find the entity that you want to delete and click
**Delete** in the **Actions** column.
5. In the Delete Synchronization Entity message, click **OK**.

##### 3.5.1.5 View the logs of a synchronization entity

O&M console Logs are generated during disaster recovery drills or actual disaster recovery. This topic describes how to view the logs of a synchronization entity in a protection group.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Synchronization Entity**
**Management**.
3. On the Protection Group page, find the protection group that you want to manage and click
**Details** in the Actions column.
4. On the **Protection Group Details** page, find the entity that you want to manage and click
**Logs** in the **Actions** column.
5. Click **OK** or **Cancel** to close the panel.

#### 3.5.2 Perform a site switchover drill

This topic describes how to associate disaster recovery plans with a switchover drill that simulates the scenario in which all devices at the primary site fail and all business needs to be switched over to the secondary site. During the switchover drill, the associated disaster recovery plans are executed.

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Site Switchover**.
3. Associate one or more disaster recovery plans with the site switchover.
i. On the Site Switchover page, click **Bind Disaster Recovery Plan**. ii. In the Bind Disaster Recovery Plan dialog box, select one or more disaster recovery plans that you want to associate with the site switchover. iii. Click **OK**. The associated disaster recovery plans are displayed on the **Site Switchover** page.
4. Set the execution order.
i. Move the pointer over the number in the Execution Sequence column of a plan and click the icon. ii. Enter an integer from 0 to 9 in the Execution Sequence field. A smaller value indicates a higher execution priority. The plans that have the same priority are executed at the same time. iii. Click **OK**.
5. Start the disaster recovery plans.
i. In the upper-right corner of the Site Switchover page, click **Start All Failovers**. ii. In the Start All Failovers message, click **OK**. iii. All plans start to be executed to switch business from the primary site to the secondary site. iv. After all plans are executed, the plans are ready to be executed for a failback. You can click
**Start Failback** to switch business from the secondary site to the primary site.
v. After all plans are executed for the failback, the business at the primary site works as expected. O&M console

**Related operations**

On the Site Switchover page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|
| View plan details | 1. Click the name of a plan to go to the plan details page. 2. View the details of the plan on the following tabs: On the Plan Steps tab, view the execution steps of the plan. On the Progress tab, view the switchover drill progress. To terminate the switchover drill, click Terminate. In the message that appears, confirm the task that you want to terminate and click Terminate Failover. If an exception occurs but the exception does not affect the switchover drill, click Force Pass. In the message that appears, click Force Pass. On the Associated Protection Group tab, view the protection groups that are associated with the plan and the instances in each protection group. On the Historical Records tab, view the overview of the switchover drill in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO-compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. |
| View a switchover drill summary | On the Historical Records tab of the plan details page, find a switchover drill and click View Drill Summary in the Actions column. |
| Download a switchover drill summary report | On the Historical Records tab of the plan details page, find a switchover drill and click Download Report in the Actions column to save the report to your computer. |
| Disassociate one or more disaster recovery plans from the site switchover | Disassociate multiple disaster recovery plans at a time i. On the Site Switchover page, select the disaster recovery plans that you want to disassociate from the site switchover. ii. In the lower part of the page, click Unbind. iii. In the Batch Unbind message, click OK. Disassociate a single disaster recovery plan i. On the Site Switchover page, find the disaster recovery plan that you want to disassociate from the site switchover and click Unbind in the Actions column. ii. In the Unbind Independent Disaster Recovery message, click OK. |

#### 3.5.3 Perform a site failover

This topic describes how to associate disaster recovery plans with a site failover that is performed when all devices at the primary site fail and all business needs to be switched over to the secondary site. During the site failover, the associated disaster recovery plans are executed. O&M console

**Prerequisites**

A disaster recovery plan is created. For more information, see Create a business disaster recovery plan.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, choose **Disaster Recovery > Site Failover**.
3. Associate one or more disaster recovery plans with the site failover.
i. On the Site Disaster Recovery page, click **Bind Disaster Recovery Plan**. ii. In the Bind Disaster Recovery Plan dialog box, select one or more disaster recovery plans that you want to associate with the site failover. iii. Click OK.
4. Set the execution order.
i. Move the pointer over the number in the Execution Sequence column of a plan and click the icon. ii. Enter an integer from 0 to 9 in the Execution Sequence field. A smaller value indicates a higher execution priority. The plans that have the same priority are executed at the same time. iii. Click **OK**.
5. Start the disaster recovery plans.
i. In the upper-right corner of the Site Switchover page, click **Start All Failovers**. ii. In the Start All Failovers message, click **OK**. iii. All plans start to be executed to switch business from the primary site to the secondary site. iv. After all plans are executed, the plans are ready to be executed for a failback. You can click
**Start Failback** to switch business from the secondary site to the primary site.
v. After all plans are executed for the failback, the business at the primary site works as expected.

**Related operations**

On the Site Disaster Recovery page, you can also perform the operations described in the following table.

| Operation | Description |
|---|---|

O&M console

| View plan details | 1. Click the name of a plan to go to the plan details page. 2. View the details of the plan on the following tabs: On the Plan Steps tab, view the execution steps of the plan. On the Progress tab, view the failover progress. To terminate the failover, click Terminate. In the message that appears, confirm the task that you want to terminate and click Terminate Failover. If an exception occurs but the error does not affect the failover, click Force Pass. In the message that appears, click Force Pass. On the Associated Protection Group tab, view the protection groups that are associated with the plan and the instances in each protection group. On the Historical Records tab, view the overview of the failover in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO- compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. |
|---|---|
| View a failover summary | On the Historical Records tab of the plan details page, find a failover and click View Drill Summary in the Actions column. |
| Download a failover summary report | On the Historical Records tab of the plan details page, find a failover and click Download Report in the Actions column to save the failover report to your computer. |
| Disassociate one or more disaster recovery plans from the site failover | Disassociate multiple disaster recovery plans at a time i. On the Site Disaster Recovery page, select the disaster recovery plans that you want to disassociate from the site failover. ii. In the lower part of the page, click Unbind. iii. In the Batch Unbind message, click OK. Disassociate a single disaster recovery plan i. On the Site Disaster Recovery page, find the disaster recovery plan that you want to disassociate from the site failover and click Unbind in the Actions column. ii. In the Unbind Independent Disaster Recovery message, click OK. |

#### 3.5.4 View the execution history of a site disaster recovery plan

**disaster recovery plan**

This topic describes how to view the steps, progress, associated protection groups, and historical execution records of a site disaster recovery plan.

**Prerequisites**

A site disaster recovery plan for a switchover drill or failover is created.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
O&M console
2. In the left-side navigation pane, choose **Disaster Recovery > Plan Execution History**.

**Note**

Each time a site disaster recovery plan is executed, a record is automatically generated on the **Plan Execution History** page. The records whose names start with AUTO_CREATE_REGION_PLANare automatically generated by the system. View drill records. a. On the Plan Execution History page, click the **Disaster Recovery Drill Records** tab. b. Find the plan that you want to manage and click its name to go to the plan details page. c. View the plan details on the following tabs: **Plan Steps**, **Progress**, **Associated**
**Protection Group**, and **Historical Records**.

| Tab | Description |
|---|---|
| Plan Steps | This tab displays all steps that are performed when the plan is executed for failovers and failbacks. If the plan is in the Completed state, you can click Start Drill on the Plan Steps tab to execute the plan again. If the plan is a drill plan, you can click Change to Recovery Plan on the Plan Step tab and click OK in the message that appears to change the plan type. |
| Progress | a. This tab displays time consumption and detailed progress when the plan is executed for failovers and failbacks. Note To go to the Progress tab, you can also find the plan on the Disaster Recovery Drill Records tab and click Details in the Actions column. b. In the left-side Step section, you can view the time consumed for each step. To view the logs of each step, click View Logs. c. To view the progress details of a step, click the step in the left-side Step section. d. To view the substeps of a step, click the icon to the left of the step name. |
| Associated Protection Group | This tab displays the status of all protection groups associated with the plan and the number of instances in each protection group. |

O&M console

| Historical Records | a. This tab displays the overview of the plan in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO-compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate b. To view the summary of a drill, find the drill in the drill list and click View Drill Summary in the Actions column. Note You can also find the drill on the Disaster Recovery Drill Records tab and click View Drill Summary in the Actions to go to the Summary page. In the Overview section, the information is displayed in the following sections: Drill Success Rate, Protection Group Failover Success Rate, Protection Group Failback Success Rate, RPO- compliant Rate, Failover Duration Compliance Rate, and Failback Duration Compliance Rate. In the Drill Conclusion section, you can view the drill conclusion specified in the Apsara Uni-manager Management Console. On the Failover Duration Rankings and Failback Duration Rankings tabs, the instances are displayed in descending order based on the time consumption. c. To download the report of a drill, find the drill in the drill list and click Download Report in the Actions column to save the report to your computer. You can download a report of a drill only after the plan is in the Completed state and the report is created in the Apsara Uni-manager Management Console. |
|---|---|

View disaster recovery records. a. On the Plan Execution History page, click the **Disaster Recovery Records** tab. b. Find the plan that you want to manage and click its name to go to the plan details page. O&M console c. View the plan details on the following tabs: **Plan Steps**, **Progress**, **Associated**
**Protection Group**, and **Historical Records**.

| Tab | Description |
|---|---|
| Plan Steps | This tab displays all steps that are performed when the plan is executed for failovers and failbacks. If the plan is in the Completed state, you can click Start Drill on the Plan Steps tab to execute the plan again. To start a failover, click Start Failover. In the message that appears, click OK. |
| Progress | a. This tab displays time consumption and detailed progress when the plan is executed for failovers and failbacks. Note To go to the Progress tab, you can also find the plan on the Disaster Recovery Records tab and click Details in the Actions column. b. In the left-side Step section, you can view the time consumed for each step. To view the logs of each step, click View Logs. c. To view the progress details of a step, click the step in the left-side Step section. d. To view the substeps of a step, click the icon to the left of the step name. |
| Associated Protection Group | This tab displays the status of all protection groups associated with the plan and the number of instances in each protection group. |
| Historical Records | This tab displays disaster recovery records. |

### 3.6 Independent disaster recovery management

**management**

This topic describes how to create, view the details of, and delete an independent disaster recovery plan.

#### 3.6.1 Create an independent disaster recovery plan

**plan**

After an independent disaster recovery plan is created, you can perform failovers and switchover drills by using ASR for Geo-disaster Recovery (ASR-DR) only at the secondary site. O&M console

**Prerequisites**

ASR-DR is purchased and deployed at the primary site. The independent disaster recovery feature of ASR-DR is enabled for the primary and secondary sites.

**Procedure**

1. Log on to the O&M console of ASR-DR.
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. On the Independent Disaster Recovery page, click **Create Independent Disaster**
**Recovery**. In the Create Independent Disaster Recovery dialog box, configure the Disaster
Recovery Cloud and Disaster Recovery Region parameters.
4. Click **Create and Configure**. If you want to configure disaster recovery parameters later,
click **Create**.
5. Click **Verify** to verify the input values.
6. After the verification is passed, click **Create and Configure**. You can also click **Create** and
complete the configurations later.
7. After the configurations are complete, the independent disaster recovery plan is in the
**Configuration Completed** state. The following figure shows an example.

#### 3.6.2 Perform a failover

O&M console If a secondary site fails when the site is used to provide services, you can switch the business back to the primary site by using the independent disaster recovery feature. This topic describes how to perform a failover in the O&M console of ASR for Geo-disaster Recovery (ASR- DR). This topic also describes how to view the failover steps and progress.

**Background information**

When a site-level fault, such as network disconnection or power outage, occurs in your secondary site when the site provides services, you can switch the business back to the primary site by using the independent disaster recovery feature. This way, your business continuity is not affected.

**Prerequisites**

An independent disaster recovery plan is created. For more information, see Create an independent disaster recovery task.

**Procedure**

1. Log on to the O&M console of ASR-DR at the secondary site.
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. Perform a failover by using one of the following methods:
Find the independent disaster recovery plan that you want to manage and click **Failover** in the **Actions** column. Find the independent disaster recovery plan that you want to manage and click **View**
**Details** in the **Actions** column. On the page that appears, click **Start Failover** in the
Failover section of the Switching Steps tab.
4. After the failover is started, log on to the O&M console of ASR-DR from the primary site and
view the steps and progress of the failover. For more information, see View the details of an independent disaster recovery plan.

#### 3.6.3 Perform a switchover drill

If ASR for Geo-disaster Recovery (ASR-DR) is deployed on the secondary cloud and your business is switched over to run on the secondary cloud, the business cannot be switched back to the primary cloud when the secondary cloud fails. To resolve this issue, ASR-DR provides the independent disaster recovery feature. You can perform a switchover drill to increase the success rate of a failover.

**Background information**

O&M console When a site-level fault, such as network disconnection or power outage, occurs in your secondary site when the site provides services, you can switch the business back to the primary site by using the independent disaster recovery feature. This way, your business continuity is not affected.

**Prerequisites**

An independent disaster recovery plan is created. For more information, see Create an independent disaster recovery task.

**Procedure**

1. Log on to the O&M console of ASR-DR at the secondary site.
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. Perform a switchover drill by using one of the following methods:
Find the independent disaster recovery plan that you want to manage and click **Drill**
**Switchover** in the **Actions** column.
Find the independent disaster recovery plan that you want to manage and click **View**
**Details** in the **Actions** column. On the Independent Disaster Recovery Details page, click
**Start Drill Switchover** in the Drill Switchover section on the Switching Steps tab.
4. After the switchover drill is started, log on to the Apsara Uni-manager Operations Console
from the primary site and view the steps and progress of the switchover drill. For more information, see View the details of an independent disaster recovery plan.

#### 3.6.4 View the details of an independent disaster recovery plan

**disaster recovery plan**

You can view the steps and progress of failovers and switchover drills at the primary site.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. On the Independent Disaster Recovery page, view independent disaster recovery plans.
4. Find an independent disaster recovery plan and click **View Details** in the **Actions** column.
On the plan details page, view the basic information about the plan and the steps and progress of business switchovers. O&M console

#### 3.6.5 Disassociate configured nodes from an independent disaster recovery plan

**independent disaster recovery plan**

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. On the Independent Disaster Recovery page, find the created independent disaster recovery
plan that you want to manage.
4. Click **Unbind** in the **Actions** column. In the message that appears, click **OK**. After the
configured nodes are disassociated from the independent disaster recovery plan, you can reconfigure or delete the plan.

**Note**

You must disassociate configured nodes from an independent disaster recovery plan in ASR-DR at the secondary site.

#### 3.6.6 Delete an independent disaster recovery plan

**plan**

You can delete only independent disaster recovery plans that are not configured. For example, you can delete an independent disaster recovery plan that is created but not configured or an independent disaster recovery plan from which the configured nodes are disassociated.

**Procedure**

1. Log on to the O&M console of ASR for Geo-disaster Recovery (ASR-DR).
2. In the left-side navigation pane, click **Self Disaster Recovery Management**.
3. On the Independent Disaster Recovery page, find the created independent disaster recovery
plan that you want to delete.
4. Click **Delete** in the **Actions** column. In the message that appears, click **OK**.
O&M operations

## 4 Common O&M operations

### 4.1 Log on to a container

This topic describes how to log on to the Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) container. If you want to log on to another container, the procedure is similar. You need to only obtain the information about the corresponding service and server role.

**Background information**

The following table describes the services and server roles of containers.

| Cloud service | Service name | Server role |
|---|---|---|
| ASR-DR | asrdr | asrdr-backend.backend# |
| POP | webapp-pop | webapp-pop.PopAliyunCom# |
| PolarDB-X | drds-console | drds-console.DrdsConsole# |
| Data Transmission Service (DTS) | dts-dts | dts-dts.DtsPortal# dts-dts.DtsMaster# |
| Object Storage Service (OSS) | oss-chiji | oss-chiji.ChijiOssAll# |

**Procedure**

1. Log on to a terminal server.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. O&M operations iv. In the **Projects** section, enter asrdr in the **Product | Cluster** field. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. v. On the **Services** tab of the cluster details page, find the **asrdr-backend** service and click its name. vi. In the **Components** pane, click **backend#**. On the **Instances** tab, find the server that you want to use and click **Terminal** in the **Actions** column.
2. Run the following command to query the ID of the container:

```bash
docker ps
```

3. Run the following command to access the container:

```bash
docker exec -it <Container ID> /bin/bash
```

O&M operations

### 4.2 Log on to the ASR-DR metadatabase

**metadatabase**

After you obtain the logon information of the ASR for Geo-disaster Recovery (ASR-DR) metadatabase in the Apsara Infrastructure Management console, you can log on to the ASR-DR metadatabase by using a terminal server.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. In the **Projects** section, enter asrdr in the **Product | Cluster** field, find the cluster, and then
click **Cluster Details** in the **Actions** column.
5. On the cluster details page, click the **Resource Details** tab. On this tab, enter **asrdr_v2** in
the Resource Name field, verify that the type of the displayed resource is **db**, and then click the icon in the Resource Application Result column to view the logon information of the database. Record the logon information, close the Resource Application Result dialog box, and then click the icon to hide the database information. O&M operations
6. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara
Stack.
7. Log on to the ASR-DR metadatabase by using the database logon information that you
obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

O&M

## 5 ASR-DR O&M

### 5.1 Manage logs

#### 5.1.1 View ASR-DR logs

You can view detailed error messages in the logs of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR).
1. Log on to the ASR-DR container. For more information, see Log on to a container.
2. Run the following command to access the folder in which logs are stored:

```
cd /opt/tianji/log/
```

3. Run the `ll` command to query a list of log files. The following table describes the log files.

| Log file | Description |
|---|---|
| api.log | Stores the logs of API calls initiated by ASR-DR to access other cloud services. |
| asrdr-audit.log | Stores the audit logs. |
| complete.log | Stores all logs. |
| framework.log | Stores the backend framework logs. |
| gateway.log | Stores the frontend request logs. |
| machine-error.log | Stores the error logs of state machines. |
| machine.log | Stores the state machine logs. |
| service-error.log | Stores the error logs of services. |
| service.log | Stores the service logs. |

4. Select a log file that you want to view based on the date when the logs are generated. The
date is displayed in the ASR-DR console. O&M

> **Note:** If the name of a log file does not contain the date, the logs are generated on the current day.
> If the error message that you want to view does not exist in the logs of the ASR-DR container, you can log on to another container to view operation logs. The procedure for querying logs is similar.

5. Optional. Run the following command to search for specific log information based on the time:

```
/<Time>
```

6. Optional. Run the following command to clear logs. If the space occupied by logs exceeds a
specific threshold, you can run scheduled tasks to clear the logs that you no longer need. Run the crontab -e command to open the crontab file and create scheduled tasks.

```
Add the following CRON expression to clear the logs that have been stored for more than seven days at 01:00 every day: 0 1 * * * find /home/admin/logs/ -mtime +7 -type f -name "*.log*" -exec rm -f {} \;
```

#### 5.1.2 Modify the default log configurations

You can configure the level, output mode, and retention period of logs in the logback file. You can also specify whether to generate logs.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery (ASR-DR) container. For more information, see
Log on to a container.
2. Back up the `/alidata/bin/start` file for rollback if an exception occurs.

```
cp /alidata/bin/start /alidata/bin/start.bak
```

O&M
3. Create the logback-spring.xml file in the /alidata/bin directory to configure logs.

```
cd /alidata/bin vim logback-spring.xml
```

| vim | comma |
|---|---|

4. Run the `vim` command to modify the `/alidata/bin/start` file. Add `--logging.config=`
`<logback-spring.xml>` to the Java startup command. Sample code:

```
Before the modification: java ${JAVA_OPTS} -jar /home/admin/asrdr/web-3.0.0.jar --server.port=8888 -spring.profiles.active=prod & After the modification: java ${JAVA_OPTS} -jar /home/admin/asrdr/web-3.0.0.jar --server.port=8888 -spring.profiles.active=prod --logging.config=/logback-spring.xml &
```

> **Note:** The <logback-spring.xml> variable indicates the path of the log file.

5. Restart the ASR-DR container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you use to log on to the conta
iner. docker restart <Container ID>
```

6. Check whether the logs are generated as expected.

**Rollback**

1. Restore the configurations of the `/alidata/bin/start` file.

```bash
# Restore the /alidata/bin/start file by using the backup file.
mv /alidata/bin/start.bak /alidata/bin/start
```

2. Restart the ASR-DR container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you use to log on to the conta
iner. docker restart <Container ID>
```

### 5.2 Modify the URL of the ASR-DR console

**console**

This topic describes the cause of the error that you cannot log to the ASR for Geo-disaster Recovery (ASR-DR) console from the Apsara Uni-manager Management Console V3.12.0 SP005 to SP007 because the URL of the ASR-DR console is incorrect. This topic also describes how to resolve the error.

**Problem description**

You cannot log to the ASR-DR console from the Apsara Uni-manager Management Console because the URL of the ASR-DR console is incorrect. O&M

**Cause**

If you use the Apsara Uni-manager Management Console V3.12.0 SP005 to SP007, the default URL of the ASR-DR console stored in the database applies to Apsara Uni-manager Management Console V3.13.0. You must modify the URL of the ASR-DR console to be compatible with Apsara Uni-manager Management Console V3.12.0.

**Procedure**

1. Log on to the ASR-DR metadatabase from the Apsara Uni-manager Management Console. For
more information, see Log on to the ASR-DR metadatabase.
2. Run the following command to select the basic database:

```
use basic;
```

3. Run the following command to query the current ASR-DR settings:

```
select * from identifier_info where identifier = 'asrdr'; select * from exposed_resource where identifier='asrdr';
```

4. Run the following command to update the ASR-DR settings:

```
update identifier_info set service = 'asrdr-backend',is_locked = 'y' where identifier='asrdr'; update exposed_resource set exposed_resource = 'asrdr',is_locked='y' where identifier='asrdr'; update exposed_resource set ext_data='' ,default_value='asrdr.$<{#$_INTERNET_DOMAIN}>' where identifier='asrdr';
```

5. Verify that you can log on to the ASR-DR console from the Apsara Uni-manager Management
Console as expected.

### 5.3 Stop ASR-DR nodes

ASR for Geo-disaster Recovery (ASR-DR) is deployed in a three-node cluster. Frontend requests are distributed to a random node by using a load balancer. As a result, the troubleshooting process is complex because you need to troubleshoot issues on three ASR-DR nodes. Therefore, we recommend that you stop two ASR-DR nodes during troubleshooting. This way, the logs are stored in a single-node ASR-DR container.

**Risks**

If a drill or failover plan is running, the operation to stop nodes may lead to node switching and increase the recovery time objective (RTO). Protection groups are run on the same node. If the number of protection groups exceeds 200, the node may be overloaded.

**Method 1: Stop the container**

O&M

> **Note:** If you stop the ASR-DR container, ASR-DR is not at desired state during the check of Apsara Infrastructure Management.

1. Log on to the ASR-DR container. For more information, see Log on to a container.
2. Run the following command to go to the specified directory:

```
cd /cloud/app/asrdr-portal/portal#
```

3. Run the following command to stop the asrdr-backend container:

```
/cloud/tool/tianji/tjc stop asrdr-backend.backend#
```

**Method 2: Terminate the process**

1. Log on to the ASR-DR container. For more information, see Log on to a container.
2. Back up the `/alidata/bin/check_app.sh` file for subsequent rollback.

```
cp /alidata/bin/check_app.sh /alidata/bin/check_appbak.sh
```

3. Modify the `/alidata/bin/check_app.sh` file and change exit $? to `exit 0` .
4. Run the following commands to obtain the process identifier (PID) of the ASR-DR process and
terminate the ASR-DR process:

```
ps aux | grep <ASR-DR process> kill -9 <pid>
```

5. If you use Apsara Stack of a version that is earlier than V3.13.0, you must also run the
following command to terminate the NGINX process:

```
ps aux | grep <NGINX process> kill -9 <pid>
```

**Rollback**

**Rollback for method 1**

1. Log on to the ASR-DR container. For more information, see Log on to a container.
O&M
2. Run the following command to go to the specified directory:

```
cd /cloud/app/asrdr-portal/portal#
```

3. Run the following command to stop the asrdr-backend container:

```
/cloud/tool/tianji/tjc stop asrdr-backend.backend#
```

**Rollback for method 2**

1. Replace the `check_app.sh` file with the `/alidata/bin/check_app.sh` file that you backed
up.
2. Restart the asrdr-backend container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you used to log on to the cont
ainer. docker restart <Container ID>
```

### 5.4 Replace the JAR package

If an error occurs, you can replace the original JAR package with a new JAR package after the bugs are fixed in code. This way, the error can be resolved.

**Background information**

The size of a new JAR package increases. The features are not affected. After the original JAR package is replaced, dependency conflicts may occur when you start Spring Boot due to the use of both Log4j and Logback frameworks. In this case, you can delete the `slf4j-log4j12` JAR package from the `BOOT-INF/lib/` directory and compress data to generate a new JAR package.

**Procedure**

1. Log on to the ASR for Geo-disaster Recovery (ASR-DR) container. For more information, see
Log on to a container.
2. Run the following command to back up the `/home/admin/asrdr/web-3.0.0.jar` file:

```
mv /home/admin/asrdr/web-3.0.0.jar /home/admin/web-3.0.0.jar.bak
```

3. Copy the new `web-3.0.0.jar` file to the `/home/admin/asrdr` directory.
4. Restart the ASR-DR container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you used to log on to the cont
ainer. docker restart <Container ID>
```

**Rollback**

1. Log on to the ASR-DR container. For more information, see Log on to a container.
2. Delete the `web-3.0.0.jar` file in the `/home/admin/asrdr` directory.
O&M

```
rm -rf ./web-3.0.0.jar
```

3. Replace the `web-3.0.0.jar` file with the `web-3.0.0.jar.bak` file that you backed up.
4. Restart the ASR-DR container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you used to log on to the cont
ainer. docker restart <Container ID>
```

### 5.5 Manage configurations

This topic describes how to modify the configurations of the disaster recovery services at the secondary site. This topic also describes the system configurations of ASR for Geo-disaster Recovery (ASR-DR).

**Procedure**

1. Log on to the ASR-DR container. For more information, see Log on to a container.
2. Run the following command to go to the configuration directory:

```
cd /home/admin/asrdr/config
```

3. Run the following command to modify a specific configuration file. For more information about
the sample configuration files, see the ASR-DR configurations, Basic service configurations, Configurations of disaster recovery services, and ZooKeeper configurations sections of this topic.

```
vi xxx.yml
```

4. Log on to the ASR-DR metadatabase and run the following command to clear the parameter
configurations. For more information about how to log on to the ASR-DR metadatabase, see Log on to the ASR-DR metadatabase.

```
delete from t_base_param;
```

5. Restart the container.

```bash
# Exit the container if you are in the container.
exit
# Restart the container. The container ID is the ID that you used to log on to the cont
ainer. docker restart <Container ID>
```

O&M
6. Repeat Step 1 to 5 until the configurations are modified in all containers.

**ASR-DR configurations**

O&M

```bash
## The configurations of ASR-DR ##
##################
# The basic information.
baseinfo:
  product-name: asrdr
  service-name: asrdr-backend
 # The endpoint of ASR-DR.
  domain: ${web_server_host}
  # The portal endpoint of ASR-DR.
  portal-domain: ${asrdr_portal_domain}
  version: 3.15.0
# The list of IP addresses of ASR-DR nodes.
node:
  ip: ${node_list}
# The Resource Access Management (RAM) user that is authorized to perform operations on
ASR-DR. user:
  accesskey-id: ${asrdr_aliyun_user_accesskey_id}
  accesskey-secret: ${asrdr_aliyun_user_accesskey_secret}
  id: ${asrdr_aliyun_user_id}
  name: ${asrdr_aliyun_user_mail}
# The service account of ASR-DR.
service:
  use-sts-token: ${use_sts_token:true}
  accesskey-id: ${asr_service_accesskey_id}
  accesskey-secret: ${asr_service_accesskey_secret}
  id: ${asr_service_id}
# The quota limits on the number of service instances and protection groups in ASR-DR.
quota:
  protect-group: 200
  entity: 200
  dts: 60
  oss: 20
  ots: 20
  mq: 20
  dns: 20
  odps: 20
  adb: 20
  ads: 20
application:
  # The maximum synchronization latency. Unit: minutes.
  checkmaxrpo: 30
event:
 # Specify whether the node is a test node.
  test-node: false
  # Specify whether the node is used for load balancing.
  need-do-lb: false
```

O&M

**Basic service configurations**

```bash
region: ${region_id} ans:
  env:
    domain: ${ans_enpoint}
    port: 8010
  test: false
# The parameters related to the secondary site.
ascm:
  env:
    ascm-gateway: ${ascm_gateway}
    ascm-portal: ${ascm_portal}
    user-accesskey-id: ${ascm_default_user_ak}
    user-accesskey-secret: ${ascm_default_user_sk}
    one-console-domain: ${one_console}
  test: false
# Unused parameters.
aso:
  env:
    plat-monitor:
      domain: asoendpoint
      port: 8092
  test: false
### The parameters related to Data Transmission Service (DTS).
dts:
  env:
    domain: ${dts_openapi_endpoint}
  # Specify whether the primary DTS instance is used.
  use-maincloud-dts: false
  test: false
### The parameters related to RAM.
ram:
  env:
    domain: ${ram_endpoint}
    sts-domain: ${sts_endpoint}
  test: false
### The parameters related to Virtual Private Cloud (VPC).
vpc:
  env:
    domain: ${vpc_inner_endpoint}
  test: false
```

**Configurations of disaster recovery services**

```
region: ${region_id}
### The environment of ApsaraDB RDS.
rds:
```

O&M

```bash
  env:
    domain: ${rds_openapi_endpoint}
  test: false
### The environment of PolarDB-X.
drds:
  env:
    domain: ${drds_endpoint}
    zone: ${drds_zone}
    service-accesskey-id: ${drds_ram_ak}
    service-accesskey-secret: ${drds_ram_sk}
  test: false
### The environment of AnalyticDB for MySQL.
ads:
  env:
    domain: ${ads_openapi_endpoint}
  test: false
### The environment of AnalyticDB for MySQL V3.0.
adb3:
  env:
    domain: ${adb3_openapi_endpoint}
  test: false
### The environment of Object Storage Service (OSS).
oss:
  env:
    cloud-type: private
    cloud-id: ${cloud_unique_id}
    domain: ${oss_server_endpoint}
    chiji-domain: ${oss_chiji_endpoint}
    chiji-https-domain: ${oss_chiji_https_endpoint}
    chiji-pop-domain: ${oss_chiji_pop}
    service-accesskey-id: ${default_user_ak}
    service-accesskey-secret: ${default_user_sk}
  test: false
### The environment of Tablestore.
ots:
  env:
    domain: ${ots_ocm_pop_endpoint}
    repmanager-domain: http://${ots_repmanager_endpoint}
  test: false
### The environment of ApsaraMQ.
mq:
  env:
    domain: http://${mq_client_ons_addr}
    ons-address: ${ons_addr}
    user-accesskey-id: ${mq_system_ak}
    user-accesskey-secret: ${mq_system_sk}
    # Specify whether the consumption mode is used. If the consumption mode is not used,
the synchronization mode is used.
    use-consume-mode: false
test:false
```

O&M

```
  test: false
### The environment of Apsara Stack DNS (DNS) on the tenant side.
appdns:
  env:
    domain: ${genesisdns_endpoint}
    user-accesskey-id: ${genesisdns_ak}
    user-accesskey-secret: ${genesisdns_sk}
    gtm_pop_endpoint: ${gtm_pop_endpoint}
  test: false
### The environment of Apsara Big Data Manager (ABM).
bcc:
  env:
    domain: https://${bcc_endpoint}
    app-name: ${bcc_app_name}
    app-user: ${bcc_auth_user}
    app-key: ${bcc_app_key}
    app-password: ${bcc_app_passwd}
  test: false
```

**ZooKeeper configurations**

```
zookeeper:
  asr:
    root: ${zookeeper_node}
  conn:
    timeout: 300000
  executor:
    number: 3
    waitTimeOut: 30000
    ttl: 30000
  server:
    endpoints:
${zookeeper_zk1}:${zookeeper_port},${zookeeper_zk2}:${zookeeper_port},${zookeeper_zk3}:${zoo eper_port} zkui:
    userName: root
    passWord: root
    loginMessage: Please login using username and password.
```

## 6 FAQ

### 6.1 ApsaraDB RDS

#### 6.1.1 How do I add databases and tables to ApsaraDB RDS instances?

**ApsaraDB RDS instances?**

This topic describes how to add databases and tables to ApsaraDB RDS instances during disaster recovery to prevent protection failures.

**Background information**

After you perform a switchover drill, incremental data is synchronized between the primary and secondary ApsaraDB RDS instances. However, Data Transmission Service (DTS) cannot synchronize database schemas during incremental data synchornization. Therefore, if you add databases and tables to ApsaraDB RDS instances, you must manually modify related data of ASR for Geo-disaster Recovery (ASR-DR) and DTS.

**Scenario 1: A database that requires disaster recovery**

**protection is added to the primary ApsaraDB RDS instance**

1. Manually add a database to the secondary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account.

> **Note:** If the ApsaraDB RDS instance runs MySQL 5.7, the synchronization account is asr_sync_account.
> If the ApsaraDB RDS instance runs MySQL 5.6, the synchronization account is dtssyncwriter.

2. Manually add a database to the primary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account. If ASR-DR detects that a database is added to the primary or secondary ApsaraDB RDS instance, the corresponding protection group changes from the **Protecting** state to the
**Protect failed** state.
3. On the Protection Groups page of the ASR-DR console, find the protection group, click the
icon in the Actions column, and then select **Re-protect**. The synchronization entity in the protection group is reprotected. The database is automatically added to the objects to be synchronized and waits to be protected. DTS starts a new subtask to synchronize the new database. The process of completing the subtask and merging the subtask into the original task takes around 20 minutes. You need to check whether the subtask is successfully merged.

**Scenario 2: A database that does not require disaster recovery**

**protection is added to the primary ApsaraDB RDS instance**

In this scenario, you do not need to modify the objects to be synchronized but you need to filter out the database from the ASR-DR database. You must grant the synchronization account the read and write permissions on the new database in the primary and secondary ApsaraDB RDS instances.
1. Manually add a database to the secondary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account.

> **Note:** If the ApsaraDB RDS instance runs MySQL 5.7, the synchronization account is asr_sync_account.
> If the ApsaraDB RDS instance runs MySQL 5.6, the synchronization account is dtssyncwriter.

2. Manually add a database to the primary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account.
3. Filter the database in the ASR-DR console. For more information, see the **Business disaster**
**recovery** > **Modify the conditions to filter tables** topic in ASR-DR User Guide.

> **Note:** You can specify conditions to filter tables in the ASR-DR console of V3.15.0 or later.
> To filter the database in the ASR-DR console whose version is earlier than V3.15.0, perform the following steps:
> i. Log on to the ASR-DR database. For more information, see Log on to the ASR-DR

metadatabase.

> ii. Modify the **rwAccounts** field in **t_am_rdsSyncEntity**. Add `,New database.-.*` to the
> value of the **rwAccounts** field.
> The value of the **rwAccounts** field is in the `Database.Account.*` format. An asterisk (*) indicates that the database is filtered out. Use a hyphen (-) to indicate the account. Separate multiple databases with commas (,).
> iii. Check whether the modification is successful. If the modification is not successful,
> disable ASR-DR and perform the modification again.
> iv. Restart ASR-DR.

**Scenario 3: A database is added to the primary ApsaraDB RDS**

**instance and only specific tables in the database require disaster**

**recovery protection**

1. Manually add a database to the secondary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account.

> **Note:** If the ApsaraDB RDS instance runs MySQL 5.7, the synchronization account is asr_sync_account.
> If the ApsaraDB RDS instance runs MySQL 5.6, the synchronization account is dtssyncwriter.

2. Manually add a database to the primary ApsaraDB RDS instance and create table schemas.
Grant the read and write permissions to the synchronization account.
3. Filter tables in the ASR-DR console. For more information, see the **Business disaster**
**recovery** > **Modify the conditions to filter tables** topic in ASR-DR User Guide.

> **Note:** You can specify conditions to filter tables in the ASR-DR console of V3.15.0 or later.

**Scenario 4: A table that does not require disaster recovery**

**protection is added to a database under protection**

1. Manually create a table in the primary ApsaraDB RDS instance.
2. Stop ASR-DR nodes. For more information, see Stop ASR-DR nodes.

> **Note:** After a table is added, ASR-DR adds the table to the objects to be synchronized as scheduled. DTS adds the table to the objects to be synchronized. To prevent ASR-DR from adding the table to the objects to be synchronized, you must stop ASR-DR nodes.

3. Filter the table in the ASR-DR console. For more information, see the **Business disaster**
**recovery** > **Modify the conditions to filter tables** topic in ASR-DR User Guide.

> **Note:** You can specify conditions to filter tables in the ASR-DR console of V3.15.0 or later.

**Scenario 5: A table that requires disaster recovery protection is**

**added to a database under protection**

After you add a table to the primary ApsaraDB RDS instance, you need to create a table schema on the secondary ApsaraDB RDS instance.

> **Note:** After a table is added, ASR-DR adds the table to the objects to be synchronized as scheduled. DTS adds the table to the objects to be synchronized. In this case, you do not need to modify the ASR-DR configurations.

#### 6.1.2 How do I manually switch workloads between primary and secondary ApsaraDB RDS instances?

**between primary and secondary ApsaraDB RDS**

**instances?**

If an ApsaraDB RDS instance at the primary site and ASR for Geo-disaster Recovery (ASR-DR) fail, you can manually switch your business to an ApsaraDB RDS instance at the secondary site.

**Background information**

If an ApsaraDB RDS instance at the primary site fails, you can perform a failover to switch your business to an ApsaraDB RDS instance at the secondary site. If the ApsaraDB RDS instance at the secondary site fails after the failover, you can perform a failback to switch your business back to the primary ApsaraDB RDS instance. This topic describes how to manually perform a failover. You can perform a failback in a similar way.

**Procedure**

1. Grant the read and write permissions to the account used to access the ApsaraDB RDS
instance at the secondary site. i. Log on to the Apsara Uni-manager Management Console from the secondary site. ii. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**. iii. In the left-side navigation pane, click **Instances**. On the Instance List page, find the secondary ApsaraDB RDS instance and click its name. iv. In the left-side pane of the instance details page, click **Accounts**. v. Find the account and click **Change Permissions** in the **Actions** column. vi. In the **Authorized Databases** section of the Edit Account Permissions panel, select
**Read/Write** for the account.
vii. Click **OK**.
2. Check whether data can be written to the ApsaraDB RDS instance at the secondary site.

#### 6.1.3 How do I manually resume data synchronization?

**synchronization?**

If the primary and secondary ApsaraDB RDS instances are restored but ASR for Geo-disaster Recovery (ASR-DR) fails and cannot be used within a short period of time, you can manually resume data synchronization between the primary and secondary ApsaraDB RDS instances.
1. Grant only the read permissions to the account used to access the secondary ApsaraDB RDS
instance. i. Log on to the Apsara Uni-manager Management Console from the secondary site. ii. In the top navigation bar, choose **Products > Database Services > ApsaraDB RDS**. iii. In the left-side navigation pane, click **Instances**. On the Instance List page, find the secondary ApsaraDB RDS instance and click its name. iv. In the left-side pane of the instance details page, click **Accounts**. v. Find the account and click **Reset Account Permissions** in the **Actions** column. vi. In the Reset Account Permissions dialog box, enter and confirm the password of the account and click **OK**. vii. Find the account and click Change Permissions in the Actions column. In the **Authorized**
**Databases** section of the Edit Account Permissions panel, select **Read-only** for the
account. viii. Click **OK**.
2. Grant the read and write permissions to the account used to access the primary ApsaraDB
RDS instance by referring to Step 1.
3. Log on to the Data Transmission Service (DTS) console from the secondary site and configure
the task to synchronize data from the primary ApsaraDB RDS instance to the secondary ApsaraDB RDS instance. For more information, see the **Data synchronization** > **Configure**
**data synchronization tasks** > **Synchronize data between ApsaraDB RDS for MySQL**
**instances** topic in DTS User Guide.
4. Manually check whether the synchronization task is run as expected and data is synchronized.

### 6.2 DNS

#### 6.2.1 What do I do if the "rrSet inconsistent" error message appears in DNS logs?

**error message appears in DNS logs?**

This topic describes the cause of the "rrSet inconsistent" error message that appears in the logs of an Apsara Stack DNS (DNS) instance. This topic also describes how to resolve the error.

**Problem description**

In the protection group list, the protection group to which the DNS instance belongs is in the
**Protection failed** state. On the Protection Group Details page, **rrSet inconsistent** is
displayed when you view the logs of the DNS instance.

**Cause**

The DNS records are inconsistent between the primary and secondary sites.

**Solution**

1. Log on to the DNS console from the primary site. View the value of the **Record Values**
parameter. i. Find the domain name and click **Configure DNS Records** in the **Actions** column. ii. On the **DNS Settings** page, find the DNS record and click **Modify** in the **Actions** column. iii. View the value of the **Record Values** parameter.
2. Log on to the DNS console from the secondary site. Modify the **Record Values** parameter to
ensure that the record values are consistent with those of the primary site. For more information, see Step 1.
3. Log on to the ASR for Geo-disaster Recovery (ASR-DR) console from the secondary site. On
the **Protection Group Details** page, find the DNS instance and click **Recover** in the Actions column. The protection group enters the **Protected** state.

#### 6.2.2 What do I do if the "not found record" error message appears in DNS logs?

**error message appears in DNS logs?**

This topic describes the cause of the "not found record" error message that appears in the logs of an Apsara Stack DNS (DNS) instance. This topic also describes how to resolve the error.

**Problem description**

In the list of protection groups, the protection group to which the DNS instance belongs is in the
**Protect failed** state. When you view the logs of the DNS instance on the Protection Group
Details page, the **not found record, zoneId: xxx, rrName: xxx, cloudType: xxx** error message is found.

**Cause**

No host record is configured for the domain name of the primary or secondary site. cloudType: the site type. A value of MAIN indicates the primary site. A value of BACKUP indicates the secondary site. zoneId: the ID of the DNS instance. rrName: the name of the host record.

**Solution**

1. Log on to the DNS console from the primary or secondary site based on the value of the
**cloudType** parameter.
2. Find the corresponding domain name and click **Configure DNS Records** in the **Actions**
column.
3. On the **DNS Settings** page, click **Add DNS Record**. In the Add DNS Record dialog box,
configure the parameters to add a host record.

> **Note:** The record values of the primary and secondary sites must be consistent.

4. Log on to the ASR for Geo-disaster Recovery (ASR-DR) console from the secondary site. On
the details page of the protection group, find the synchronization entity, click the icon in the **Actions** column, and then select **Recover**. The protection group enters the **Protecting** state.

#### 6.2.3 What do I do if the "not found zone" error message appears in DNS logs?

**error message appears in DNS logs?**

This topic describes the cause of the "not found zone" error message that appears in the logs of an Apsara Stack DNS (DNS) instance. This topic also describes how to resolve the error.

**Problem description**

In the list of protection groups, the protection group to which the DNS instance belongs is in the
**Protect failed** state. When you view the logs of the DNS instance on the Protection Group
Details page, the **not found zone xxx cloudType: xxx** error message is found.

**Cause**

The domain name is unavailable at the primary or secondary site. cloudType: the site type. A value of MAIN indicates the primary site. A value of BACKUP indicates the secondary site. zone: the name of the DNS instance.

**Solution**

1. Log on to the DNS console from the primary or secondary site based on the value of the
**cloudType** parameter.
2. Create a domain name that is the same as that of the peer.
3. Add a host record and DNS record that are the same as those of the peer.
4. Log on to the ASR for Geo-disaster Recovery (ASR-DR) console from the secondary site. On
the details page of the protection group, find the synchronization entity, click the icon in the **Actions** column, and then select **Recover**. The protection group enters the **Protecting** state.

### 6.3 AnalyticDB for MySQL V3.0

#### 6.3.1 What do I do if a reprotection operation fails to be performed?

**fails to be performed?**

This topic describes the cause of the error that a protection group to which primary and secondary AnalyticDB for MySQL V3.0 instances belong fails to be reprotected. This topic also describes how to resolve the error.

**Problem description**

After the data synchronization between the primary and secondary AnalyticDB for MySQL V3.0 instances is paused, the protection group fails to be reprotected. The protection group is in the
**Protection failed** state.

**Cause**

After data synchronization is restarted, the primary AnalyticDB for MySQL V3.0 instance determines the start offset based on the historical offset from which data synchronization is paused. As a result, data synchronization fails.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, choose **Instance management** > **Instance List**.
4. Search for the primary instance based on the cluster ID and click its name. The value in the
**Instance description** column of this instance is **Exclusive/analyticdb/Master**
**instance/P4**.
5. In the left-side pane of the primary instance details page, click **Basic information**. In the
**Instance information** section, view and record the instance ID, and then click
**Openconsole**.
6. Obtain the ID of the secondary AnalyticDB for MySQL V3.0 instance by referring to Steps 3 and
4.
7. In the console of the primary instance, click **SQL Editor** in the left-side navigation pane. In
the code editor that appears, run the command shown in the following figure. The `gap` `exist` error message appears.

```
replication master start <ID of the secondary AnalyticDB for MySQL V3.0 instance>
```

8. Log on to the ASR for Geo-disaster Recovery (ASR-DR) metadatabase and run the following
command:

```
delete from replication_switch_info;
```

9. In the ASR-DR console, retry the synchronization entity.
i. In the protection group list, find the protection group and click its name. ii. On the **Protection Group Details** page, find the synchronization entity, click the icon in the Actions column, and then click **Retry**.

#### 6.3.2 What do I do if a new synchronization entity fails to be created for a protection group?

**entity fails to be created for a protection**

**group?**

This topic describes the cause of the error that a new synchronization entity that contains primary and secondary AnalyticDB for MySQL V3.0 instances fails to be created for a protection group. This topic also describes how to resolve the error.

**Problem description**

After you delete the original primary and secondary AnalyticDB for MySQL V3.0 instances from a protection group in ASR for Geo-disaster Recovery (ASR-DR)and create a new synchronization entity for the protection group, the protection group changes to the Protection failed state.

**Cause**

Historical tasks are not cleared when you delete the original synchronization entity.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, choose **Instance management** > **Instance List**.
4. Search for the primary AnalyticDB for MySQL V3.0 instance based on the cluster ID and click
its name. The value in the **Instance description** column of this instance is
**Exclusive/analyticdb/Master instance/P4**.
5. In the left-side pane of the primary instance details page, click **Basic information**. In the
**Instance information** section, view and record the instance ID, and then click
**Openconsole**.
6. Obtain the ID of the secondary AnalyticDB for MySQL V3.0 instance by referring to Steps 4 and
5.
7. In the console of the primary AnalyticDB for MySQL V3.0 instance, click **SQL Editor** in the left-
side navigation pane. In the code editor that appears, run the command shown in the following figure. The `gap exist` error message appears.

```
select * from ation_schema.kepler_meta_cluster_replication_task where is_masteinformr = 1 and slave_cluster_name=<ID of the AnalyticDB for MySQL V3.0 secondary instance>
```

If records are returned, the historical tasks are not cleared.
8. Run the following command to clear historical tasks:

```
replication master destroy slave <ID of the secondary AnalyticDB for MySQL V3.0 instance>
```

9. Go to the ASR-DR console and retry the synchronization entity.
i. In the protection group list, find the protection group and click its name. ii. On the **Protection Group Details** page, find the synchronization entity ,click the icon in the Actions column, and then select **Retry**.

#### 6.3.3 How do I precheck a synchronization entity before incremental synchronization?

**entity before incremental synchronization?**

This topic describes how to precheck the primary and secondary AnalyticDB for MySQL V3.0 instances as a synchronization entity before incremental synchronization. Before you can perform an incremental synchronization task, you must check whether full synchronization between the primary and secondary instances is complete.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. Log on to the console of the primary AnalyticDB for MySQL V3.0 cluster.
i. In the left-side navigation pane, choose **Instance management** > **Instance List**. ii. Search for the primary instance based on the cluster ID and click its name. The value in the
**Instance description** column of the primary instance is **Exclusive/analyticdb/Master**
**instance/P4**.
iii. In the left-side pane of the instance details page, click **Basic information**. In the **Instance information** section, view and record the value of the **InstanceID** parameter. iv. Click **Openconsole**.
4. Log on to the console of the secondary AnalyticDB for MySQL V3.0 console and view the
instance ID by referring to Step 3.
5. View the names and status of the primary and secondary AnalyticDB for MySQL V3.0
instances in the corresponding console. i. In the left-side navigation pane, click **SQL Editor**. ii. Select **META** from the **Execution Method** drop-down list. iii. In the **Database** section, click the name of the database whose name starts with **db**. iv. Run the following command and record the values of the `MASTER_CLUSTER_NAME` , `SLAVE_CLUSTER_NAME` , and `STATUS` parameters:

```
select * from cluster_replication_task;
```

To perform incremental synchronization, make sure that the values of the `MASTER_CLUSTER_NAME` and `SLAVE_CLUSTER_NAME` parameters of the primary and secondary instances are the same as the IDs of the primary and secondary instances and the value of the `STATUS` parameter is **FINISH**.

### 6.4 PolarDB-X

#### 6.4.1 What do I do if a database fails to be deleted from a secondary instance?

**deleted from a secondary instance?**

This topic describes how to handle the error that a database fails to be deleted from a secondary PolarDB-X instance.

**Problem description**

A database fails to be deleted from a secondary PolarDB-X instance.

**Cause**

The metadata is not synchronized between the primary and secondary PolarDB-X instances.

**Solution**

Restart the secondary PolarDB-X instance.

#### 6.4.2 What do I do if an error message indicating that a logical table does not exist appears when ASR-DR queries the schema of the logical table?

**indicating that a logical table does not exist**

**appears when ASR-DR queries the schema of**

**the logical table?**

This topic describes the cause of the error message indicating that a logical table does not exist when ASR for Geo-disaster Recovery (ASR-DR) queries the schema of the logical table. This topic also describes how to resolve the error.

**Problem description**

ASR-DR cannot obtain the schema of a created PolarDB-X logical table and an error message indicating that the logical table does not exist appears.

**Cause**

The PolarDB-X metadata is not synchronized.

**Solution**

1. Run the following command to drop the logical table in the PolarDB-X database:

```
drop table if exists <table_name>;
```

> **Note:** Replace <table_name> with the actual table name.

2. Create a new logical table.

#### 6.4.3 How do I modify the ApsaraDB RDS database threshold of PolarDB-X?

**database threshold of PolarDB-X?**

By default, PolarDB-X allows you to create a maximum of 30 ApsaraDB RDS databases. You can modify the value of the CreateDrdsDB parameter in the configuration file to adjust the threshold.
1. Log on to the container to which the `drds-console.DrdsConsole#` server role of PolarDB-X
belongs. For more information, see Log on to a container.
2. Run the following command to go to the directory in which the CreateDrdsDB.xml file is
stored:

```bash
cd /home/admin/pop/apis # Temporary file path.
# or
cd /home/admin/etc/batch/apis/ # Permanent file path. ls | grep CreateDrdsDB vim 2017-10-16-CreateDrdsDB.xml
```

3. Run the `vim` command to modify the `CreateDrdsDB.xml` file and modify the values of the
**CreateDrdsDB** and **maxNumber** parameters.
4. Go to the `/home/admin/pop` directory and run the following command to make the
modifications take effect:

```
java -jar batch.jar
```

#### 6.4.4 What do I do if a data synchronization task between PolarDB-X instances fails to be created?

**task between PolarDB-X instances fails to be**

**created?**

This topic describes how to resolve the error that a data synchronization task between PolarDB- X instances fails to be created or the data synchronization instance cannot be modified.

**Problem description**

A task to synchronize data between PolarDB-X instances fails to be created in ASR for Geodisaster Recovery (ASR-DR). An error message indicating that the DescribeDrdsShardingDbs operation times out appears in the logs.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > DRDS Manager**.
3. In the left-side navigation pane, choose **System Management** > **Parameter**
**Configurations**.
4. On the page that appears, click the **Console** tab.
5. On the Console tab, find the **support_use_rtools_diamond** key and click **Modify** in the
**Actions** column.

> **Note:** If you cannot find this key, perform the following operations to create the key: Click **Create**. In the dialog box that appears, set the **FIRST_KEY** parameter to support_use_rtools_diamond and the **VALUE** parameter to false and click OK.

6. In the dialog box that appears, set the **VALUE** parameter to false. Click **OK**.

#### 6.4.5 How do I scale out PolarDB-X instances?

This topic describes how to scale out PolarDB-X instances that are being protected.
1. Log on to the ASR for Geo-disaster Recovery (ASR-DR) console and make sure that no
switchover, switchback, failover, or failback is running.
2. Log on to the PolarDB-X console from the primary and secondary sites. Perform smooth scale-
outs on the databases of the same names in the primary and secondary instances in a short span of time in random order. After the primary and secondary PolarDB-X instances are smoothly scaled out, results are displayed. The following figure shows an example.
3. In the ASR-DR console, find the protection group to which the primary and secondary
instances belong, record the current recovery point objective (RPO), and then delete the corresponding protected instance from the protection group. If only one protected instance exists in the protection group, delete the protection group and record the deletion time T1.
4. In the PolarDB-X console, perform switchovers for the scale-outs of the primary and secondary
PolarDB-X instances in off-peak hours. After the primary and secondary PolarDB-X 1.0 instances are switched over, results are displayed. The following figure shows an example.
5. In the ASR-DR console, create or select an existing incremental protection group and add the
scaled-out PolarDB-X instances to the group. The synchronization point is calculated by subtracting the RPO time recorded in Step 3 from the deletion time T1 recorded in Step 3. Wait until the PolarDB-X protection entity enters the Protecting state.
6. After you confirm that the data in the primary and secondary PolarDB-X instances is
consistent, log on to the PolarDB-X console from the primary and secondary sites and create cleanup tasks to delete migrated database shards.

### 6.5 DTS

#### 6.5.1 How do I view DTS logs?

To identify the errors related to disaster recovery when you use Data Transmission Service (DTS), you need to view the logs of the master, portal, and node components.

**View master logs**

1. Log on to the container to which the `dts-dts. DtsMaster#` server role belongs. For more
information, see Log on to a container.
2. View the logs in the `/dts/master/logs/master.log` directory.

```bash
# Search for an error by keyword. Most common errors can be queried by keyword.
grep --color=auto -n -e 'keyword' /dts/master/logs/master.log
```

**View portal logs**

1. Log on to the container to which the `dts-dts.DtsPortal#` server role belongs. For more
information, see Log on to a container.
2. View the logs in the `/dts/portal/logs/portal.log` directory.

**View node logs**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > Data Transmission**
**Service**.
3. Obtain the IP address of a node.
i. In the task list, find a synchronization task and click its name. ii. On the task details page, click **Details** in the **Synchronization** section. iii. View the IP address of the node.
4. Log on to the node by using a terminal server or the Apsara Infrastructure Management
console.

```
ssh <IP address of the node>
```

5. View the log and configuration files in the `/cloud/app/dts-`
`dts/DtsNode#/dts_node/current/run/<taskId>` directory.

```
cd /cloud/app/dts-dts/DtsNode#/dts_node/current/run/<taskId>
```

#### 6.5.2 What do I do if a data synchronization task fails to be created?

**task fails to be created?**

##### 6.5.2.1 What do I do if the "The specified Instance SourceEndpoint.InstanceID Not Found" error message appears in DTS logs?

**SourceEndpoint.InstanceID Not Found" error**

**message appears in DTS logs?**

This topic describes the cause of the "The specified Instance SourceEndpoint.InstanceID Not Found" error message that appears in Data Transmission Service (DTS) logs. This topic also describes how to resolve the error.

**Problem description**

Data fails to be synchronized between databases in ASR for Geo-disaster Recovery (ASR-DR). When you query the portal logs of DTS, the `The specified Instance SourceEndpoint.InstanceID` `Not Found` error message is found.

**Cause**

This error is generally caused by invalid configuration of the region_pattern table in DTS. You can troubleshoot the issue by performing the following steps:
1. Log on to the DTS console.
2. In the left-side navigation pane, click **Data Synchronization**.
3. Create a DTS task to synchronize data between ApsaraDB RDS instances. For more
information, see DTS User Guide.
4. In the list of data synchronization tasks, find the task that you created and click **Configure**
**Task** in the **Actions** column.
5. In the **Specify Source and Destination Databases** step, verify that the destination
instance is not displayed in the Instance ID drop-down list in the specified region. The following figure shows an example.

**Solution**

1. Log on to the rmdb database.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the **Projects** section, enter dts in the search field, find the cluster and click **Cluster**
**Details** in the **Actions** column.
v. On the **Resource Details** tab of the cluster details page, find the resource whose name is
**rmdb** and type is **db** and click the
icon in the **Resource Application Result** column to view and record the logon information of the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the rmdb database by using the database logon information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. Check whether the configurations of the region and region_pattern tables are correct. The
following figure shows an example of valid configurations. For more information about how to configure the region and region_pattern tables, see the
**Geo-disaster recovery deployment** topic in Apsara Stack Enterprise Deployment Guide.

```
select * from region_pattern;
```

##### 6.5.2.2 What do I do if the "cluster info is null.The input domain and region is invalid" error message appears in DTS logs?

**input domain and region is invalid" error message**

**appears in DTS logs?**

This topic describes the cause of the "cluster info is null.The input domain and region is invalid" error message that appears in Data Transmission Service (DTS) logs. This topic also describes how to resolve the error.

**Problem description**

Data fails to be synchronized between database services in ASR for Geo-disaster Recovery (ASR- DR). When you view the portal logs of DTS, the following error message appears:

```
[{"success":false,"msg":"cluster info is null.The input domain and region is invalid.","code":404,"data":null}]
```

**Cause**

The configurations of DTS cross-cloud synchronization are invalid.

**Solution**

1. Log on to the rmdb database.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the **Projects** section, enter dts in the search field, find the cluster and click **Cluster**
**Details** in the **Actions** column.
v. On the **Resource Details** tab of the cluster details page, find the resource whose name is
**rmdb** and type is **db** and click the
icon in the **Resource Application Result** column to view and record the logon information of the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the rmdb database by using the database logon information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. Check whether the configurations of the region and region_pattern columns in the data table
are correct. For example, check whether underscores (_) and hyphens (-) are correctly used or whether records are missing. The following figure shows an example of valid configurations. For more information, see the **Configurations of ApsaraDB RDS and PolarDB-X for**
**cross-cloud disaster recovery** topic in Apsara Stack Enterprise Deployment Guide.

```
select * from region_pattern;
```

##### 6.5.2.3 What do I do if the "Specified access key is not found" error message appears in DTS logs?

**not found" error message appears in DTS logs?**

This topic describes how to handle the "Specified access key is not found" error message that is reported in the logs of a Data Transmission Service (DTS) instance.

**Problem description**

ASR for Geo-disaster Recovery (ASR-DR) fails to synchronize data between databases. When you search for the ID of the data synchronization request or **dts console** in the portal logs of the DTS instance, the `Specified access key is not found` error message is found.

**Cause**

If cross-cloud disaster recovery is used, the error message may be reported because the AccessKey pair configured for the secondary site is invalid. If cross-region disaster recovery is used, the error message may be reported because an error occurs when the unmak database is synchronized from the central region to the general region. In this case, you need to only synchronize the unmak database again.

**Cross-cloud disaster recovery scenario**

1. Log on to the container to which the DtsPortal# server role belongs from the primary site. For
more information, see Log on to a container.
2. Check whether the AccessKey pair of the secondary site configured in the
`/dts/portal/application.properties` file is valid. If the AccessKey pair is invalid, enter a valid AccessKey pair.

**Cross-region disaster recovery scenario**

1. Log on to the unmak database of the baseService-umm-ak service in the general region.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the project list, enter baseServiceAll in the search field, find the cluster, and then click
**Cluster Details** in the **Actions** column.
v. On the **Resource Details** tab of the cluster details page, find the resource whose name is
**ummak** and type is **db** and click the
icon in the **Resource Application Result** column to view and record the logon information about the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the ummak database by using the database information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. Run the following command to clear all tables:

```
truncate table ***
```

3. Log on to the Apsara Infrastructure Management console and restart the **baseService-umm-**
**ak.UmmInit#** server role. This way, a DTS task to synchronize ummak database is created.
i. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. ii. In the project list, enter baseServiceAll in the search field, find the cluster, and then click
**Cluster Details** in the **Actions** column.
iii. On the Services tab of the cluster details page, find the **baseService-umm-ak** service and click its name. iv. In the Components section of the service details page, click **UmmInit#**. On the Instances tab of the Information of Component UmmInit# section, find the VM and choose **Actions** >
**Restart** in the **Actions** column.

##### 6.5.2.4 What do I do if the "InvalidAppId.NotFound" error message appears in DTS logs?

**error message appears in DTS logs?**

This topic describes the cause of the "InvalidAppId.NotFound" error message that appears in the portal logs of Data Transmission Service (DTS). This topic also describes how to resolve the error.

**Problem description**

Data fails to be synchronized between databases in ASR for Geo-disaster Recovery (ASR-DR). When you view the portal logs of DTS, the `InvalidAppId.NotFound` error message is found.

**Cause**

Your application is not registered with the virtual private cloud (VPC) in which the secondary database resides.

**Solution**

1. Query the value of the app_id field in the **t_base_vpc_entity** table in the ASR-DR
metadatabase. For more information about how to log on to the ASR-DR metadatabase, see Log on to the ASR-DR metadatabase.
2. Log on to the vpc-controller database.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the project list, enter vpc in the search field, find the cluster, and then click **Cluster**
**Details** in the **Actions** column.
v. On the **Resource Details** tab, find the resource whose name is **vpcregiondb** and type is
**db** and click the
icon in the **Resource Application Result** column to view and record the logon information about the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the vpc-controller database by using the database information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

3. Run the following commands to check whether the app, app_address_pool, app_server, and
app_access tables contain ASR-DR configurations. If the vpc-controller database does not contain ASR-DR configurations, the application registration is expired or failed. In this case, go to Step 4.

```bash
select * from app where app_id='app-9nh4****h1qursq' and is_deleted=0\G;
# If the value of the available_count parameter is 0, the secondary site works as
expected. select * from app_address_pool where app_id='app-9nh4n****1qursq' and is_deleted=0\G;
# The number of Docker containers must be consistent with the number of ASR-DR
application servers. For example, if three Docker containers exist, three servers are r ecorded. select * from app_server where app_id='app-9nh4n****h1qursq' and is_deleted=0\G;
# The mapping IP address and port comprise the endpoint used to access the VPC in the c
lassic network. select * from app_access where app_id='app-9nh4n****h1qursq' and is_deleted=0\G;
```

> **Note:** Replace app_id with the application ID that you obtained in Step 1.

4. Log on to the **dtsdb** database of DTS.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the project list, enter dts in the search field, find the cluster, and then click **Cluster**
**Details** in the **Actions** column.
v. On the **Resource Details** tab, find the resource whose name is **dtsdb** and type is **db** and click the icon in the **Resource Application Result** column to view and record the logon information about the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the dtsdb database by using the database information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

5. Delete the old VPC registration information in the dts_mapping_app, dts_mapping_server, and
dts_mapping_pool tables.
6. Restart the portal, master, node, cm, and DrcSv4mysql services of DTS.

##### 6.5.2.5 What do I do if the "ram authorized" error message appears in DTS logs?

**message appears in DTS logs?**

This topic describes how to handle the "ram authorized" error message that appears in Data Transmission Service (DTS) logs.

**Problem description**

A task to synchronize data between databases fails to be created in ASR for Geo-disaster Recovery (ASR-DR). When you view the portal logs of DTS, the `ram authorized` error message is found.

**Cause**

The service-linked role for DTS is not created in the corresponding organization in the Apsara Uni-manager Management Console.

**Solution**

1. Log on to the Apsara Uni-manager Management Console. In the top navigation bar, click
**Configurations**. In the left-side navigation pane, click **Service-linked Roles**.
2. On the Service-linked Roles page, select `Data Transmission Service` from the Service Name
drop-down list. Check whether the service-linked role for DTS is created in the corresponding organization. If the service-linked role for **DTS** does not exist in the corresponding organization, create the service-linked role in the corresponding organization. For more information, see ASR-DR User Guide. If the service-linked role for DTS exists, contact O&M engineers for technical support.

##### 6.5.2.6 What do I do if the "Data truncation: Data too long for column 'open_api_objects'" error message appears in DTS logs?

**too long for column 'open_api_objects'" error**

**message appears in DTS logs?**

This topic describes how to handle the "Data truncation: Data too long for column 'open_api_objects'" error message that is reported in the logs of a Data Transmission Service (DTS) instance.

**Problem description**

ASR for Geo-disaster Recovery (ASR-DR) fails to synchronize data between database services. When you view the portal logs of the DTS instance, the `Data truncation: Data too long for` `column 'open_api_objects'` error message is found.

**Cause**

The size of the objects to be synchronized exceeds the specified threshold.

**Solution**

1. Log on to the dtsdb database of DTS.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. In the project list, enter dts in the search field, find the cluster, and then click **Cluster**
**Details** in the **Actions** column.
v. On the **Resource Details** tab, find the resource whose name is **dtsdb** and type is **db** and click the icon in the **Resource Application Result** column to view and record the logon information about the database. vi. Log on to a terminal server. For more information, see Log on to a terminal server on Apsara Stack. vii. Log on to the dtsdb database by using the database information that you obtained.

```
mysql -h <host> -P<port> -u<user> -p<password> <dbname>
```

2. Run the following command to modify the value of the open_api_objects column:

```
ALTER TABLE migration_job_param MODIFY open_api_objects MEDIUMTEXT ; ALTER TABLE migration_job MODIFY RESERVED MEDIUMTEXT ;
```

#### 6.5.3 What do I do if a precheck fails?

##### 6.5.3.1 What do I do if an error message indicating inconsistent topology appears?

**inconsistent topology appears?**

This topic describes the cause of the error message indicating inconsistent topology that appears during a Data Transmission Service (DTS) precheck. This topic also describes how to resolve the error.

**Problem description**

When you precheck a synchronization task in the DTS O&M console, the precheck fails and an error message indicating inconsistent topology appears.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > Data Transmission**
**Service**.
3. In the task list, find the synchronization task and click its name.
4. On the task details page, click **Details** in the **Precheck** section.
5. On the **Precheck** page, click the **Check Items** tab. On the Check Items tab, find the topology
check and click Disable in the Actions column.
6. On the **Basic Information** tab, click **Restart** next to the Status parameter.

##### 6.5.3.2 What do I do if the "CHECK_ERROR_SRC_USER_PSW" error message appears?

**"CHECK_ERROR_SRC_USER_PSW" error message**

**appears?**

This topic describes how to handle the "CHECK_ERROR_SRC_USER_PSW'" error message that is reported during a Data Transmission Service (DTS) precheck.

**Problem description**

The precheck of a DTS task fails and the `CHECK_ERROR_SRC_USER_PSW` error message is reported.

**Solution**

1. View the error information in the node logs. For more information, see the "View node logs"
section of the View DTS logs topic.
2. Copy the `console.jar` file in the `/cloud/app/dts-dts/DtsNode#/dts_node/current/jar`
directory to the directory of the DTS task. Run the following commands to obtain the values of the destUsr and destPsw parameters:

```
cp /cloud/app/dts-dts/DtsNode#/dts_node/current/jar/console.jar /cloud/app/dtsdts/DtsNode#/dts_node/current/run/<taskId>/ cd /cloud/app/dts-dts/DtsNode#/dts_node/current/run/<taskId> java -jar console.jar -e -print
```

3. Run the `telnet <destDbInst>` command based on the values of the destDbInst, destUsr, and
destPsw parameters that you obtained in the previous step to check whether the network is connected. If the network connection fails, go to the next step.
4. Restart the portal, master, node, cm, and DrcSv4mysql services of DTS.

##### 6.5.3.3 What do I do if the "CHECK_ERROR_DEST_USER_PSW" error message appears?

**"CHECK_ERROR_DEST_USER_PSW" error message**

**appears?**

This topic describes how to handle the "CHECK_ERROR_DEST_USER_PSW'" error message that is reported when the connectivity test for the destination database fails during a Data Transmission Service (DTS) precheck.

**Problem description**

During the precheck of a DTS task, connectivity test for the destination database fails and the `CHECK_ERROR_DEST_USER_PSW` error message is reported.

**Cause**

The account or password used to log on to the database is incorrect. The CIDR blocks of DTS servers are not added to the whitelist of the database instance. When DTS creates a synchronization task, the CIDR blocks of DTS servers are automatically added to the whitelists of the database instances by default. If the CIDR blocks of DTS servers exist in the whitelist of the source database but not in the whitelist of destination database, the CIDR blocks of DTS servers are not automatically added to the whitelist of the destination database. Therefore, you must add the CIDR blocks of DTS servers to the whitelists of the source and destination databases.

**Solution**

Manually add the CIDR blocks of DTS servers to the whitelists of the source and destination databases. For more information, see the **Configure a whitelist** topic in ApsaraDB for RDS User Guide

#### 6.5.4 What do I do if the incremental data service is abnormal?

**service is abnormal?**

##### 6.5.4.1 What do I do if the incremental data service fails?

**fails?**

This topic describes how to resolve the error that the incremental data service fails.

**Problem description**

1. After you go to the task details page in the Data Transmission Service (DTS) O&M console, the
precheck is complete but the incremental data service fails.
2. Click **Details** in the **Incremental Data Service** section. On the Incremental Data Service
page, view the information displayed on the **DReader** and **DReader** tabs.

**Solution**

1. View the master logs of DTS and check whether the topic_group field is deleted. For more
information, see View master logs.
2. If the topic_group field is deleted according to the logs, restart the incremental data service in
the DTS O&M console. i. Log on to the DTS O&M console. In the task list, find the task and click its name. ii. In the **Incremental Data Service** section of the task details page, click **Details**. iii. On the Incremental Data Service page, click **Restart (Rebuild)** next to the Status parameter.

#### 6.5.5 What do I do if data synchronization is abnormal?

**abnormal?**

##### 6.5.5.1 What do I do if the "store delay xxx second(s)" error message appears?

**second(s)" error message appears?**

This topic describes how to handle the "store delay xxx second(s)" error message that is reported during the synchronization step of a Data Transmission Service (DTS) task.

**Problem description**

The `store delay xxx second(s)` error message is reported during the synchronization step of your DTS task.

**Cause**

No data is written to the source database.

##### 6.5.5.2 What do I do if an error message indicating that DReader fails to connect to DStore appears?

**that DReader fails to connect to DStore appears?**

This topic describes the cause of the error message indicating that DReader fails to connect to DStore that appears when data fails to be synchronized by using Data Transmission Service (DTS). This topic also describes how to resolve the error.

**Problem description**

DTS fails to synchronize data. During the synchronization step, an error message indicating that DReader fails to connect to DStore appears.

**Cause**

The password of the source database is changed. However, the password of the source database configured in the topic of the DTS synchronization task is not automatically updated. As a result, the synchronization fails.

**Solution**

1. Log on to the DTS console.
2. On the Migration Tasks page, find the task and click its name.
3. In the Connection Details section, click **Change Source Instance Password**.
4. In the Change Instance Password dialog box, enter the original and new passwords and click
**OK**.

#### 6.5.6 What do I do if a DTS synchronization task is not automatically resumed after network recovery?

**task is not automatically resumed after**

**network recovery?**

This topic describes the cause of the error that a Data Transmission Service (DTS) synchronization task is not automatically resumed after the network is recovered. This topic also describes how to resolve the error.

**Problem description**

Your DTS synchronization task is not automatically resumed after the network is recovered.

**Solution**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > Data Transmission**
**Service**.
3. In the task list, find the synchronization task and click its name to go to the task details page.
On the task details page, click **Details** in the **Synchronization** section.
4. On the **Synchronization** page, click **Restart** next to the Status parameter.
5. After the DTS synchronization task is resumed, go to the ASR for Geo-disaster Recovery (ASR-
DR) console and reprotect the synchronization entity in the corresponding protection group. i. In the left-side navigation pane, choose **DR for Business** > **Protection Groups**. ii. In the protection group list, find the protection group that you want to manage, click the icon in the Actions column, and then select **Re-protect**.

> **Note:** If the network is interrupted for more than 18 hours, the binary logs may be lost. In this case, you need to create a another synchronization task.

#### 6.5.7 How do I prevent binary log loss due to an extended interruption between the primary and secondary databases?

**an extended interruption between the primary**

**and secondary databases?**

You can modify the retention period of binary logs in the O&M console of ApsaraDB RDS to prevent binary logs from being lost if the primary and secondary databases are interrupted for an extended period of time.

**Background information**

By default, ApsaraDB RDS retains binary logs for 18 hours. You can modify the backup policy of binary logs in the O&M console of ApsaraDB RDS.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, choose **Instance management** > **Instance List**. On the
Instance List page, find the instance that you want to manage and click its name.
4. In the left-side navigation pane of the instance details page, click **Backup policy**.
5. In the **BINLOGBackup ID** section, click **ModifyBINLOGBackup policy**. In the Modify the
Binlog backup policy dialog box, configure the **Local Retention Period** parameter.
6. Click **Submit**.

### 6.6 OSS

#### 6.6.1 How do I manually restore data synchronization between OSS buckets?

**synchronization between OSS buckets?**

If the primary and secondary Object Storage Service (OSS) buckets are restored but ASR for Geo-disaster Recovery (ASR-DR) fails and cannot be restored in a short period of time, you need to manually restore data synchronization between the OSS buckets.
1. Log on to the OSS console.
Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose
**Products** > **Storage** > **Object Storage Service**.
2. In the left-side navigation pane, click Buckets. On the Buckets page, find the OSS bucket that
you want to manage and click its name.
3. Manually create a cross-cloud synchronization rule.

> **Note:** Skip this step if a cross-cloud synchronization rule is created.

i. On the bucket details page, click the **Basic Settings** tab. In the **Cross-cloud Replication** section, click **Enable Replication**. ii. In the Cross-cloud Replication panel, configure the parameters that are described in the following table.

| Parameter | Description |
|---|---|
| Region | The region in which the source bucket resides. |
| Source Bucket | The name of the source bucket. |
| Destination Cloud | The name of the destination cloud. |
| Destination Cloud Address | The location of the destination cloud. |
| Destination bucket | The name of the destination bucket. |
| Object to Replicate | The objects that you want to synchronize. Valid values: All Objects in Source Bucket: All objects within the source bucket are synchronized to the destination bucket. Objects with Specified Prefix: Only objects whose names contain one of the specified prefixes are synchronized to the destination bucket. You can click Add to add up to 10 prefixes. |
| Replication Policy | The synchronization policy. Add/Change: Only newly added and changed data is synchronized from the source bucket to the destination bucket. Add/Delete/Change: All changes to data including creation, modification, and deletion of objects are synchronized from the source bucket to the destination bucket. |
| Replicate Historical Data | Specifies whether to synchronize historical data that is generated before you enable cross-cloud replication. Valid values: Yes: Historical data is synchronized to the destination bucket. No: Only objects that are uploaded or updated after cross-cloud replication is enabled are synchronized to the destination bucket. |

iii. Click **OK** to save your settings. Wait about 3 minutes for the synchronization rule to change from the **Starting** state to the
**Running** state.
4. Check whether the data in the primary and secondary buckets is consistent.

#### 6.6.2 What do I do if OSS buckets fail to be protected?

**protected?**

This topic describes how to resolve the error that Object Storage Service (OSS) buckets fail to be protected. If OSS buckets fail to be protected, you can troubleshoot the issue by performing the following steps:
1. Check whether a task is created to synchronize data between the primary and secondary OSS
buckets. If no data synchronization task exists, search for the `getAddBucketReplicationRequest` keyword in the logs of Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR) to check whether a data synchronization task is created. If the data synchronization task fails to be created, contact the research and development (R&D) engineers of ASR-DR.
2. Check whether the OSS endpoints configured in ASR-DR are correct. For more information
about how to configure OSS endpoints, see ASR-DR User Guide.
3. Check whether chiji is of V3.10 hotfix or later.

> **Note:** V3.10 hotfix fixes the issues related to the acceleration operation of OSS.

i. Log on to the container to which the **oss-chiji.ChijiOssAll#** server role belongs. For more information, see Log on to a container. ii. View the configuration of the `setHistorySyncStatus` parameter in the `/home/admin/admin_portal/ocm/ocm_cmd` file. The following figure shows a valid configuration. If the configuration is valid, proceed to the next step. iii. Exit the container. Query the logs that contain the same request ID as that stored in the ASR-DR logs in the `/cloud/log/oss-chiji/ChijiOssAll#/chiji_oss_all/logs` directory on the primary site. We recommend that you pay attention to the logs of the
**ReplCloudService** class.
If the following information is displayed in the logs, the chiji version may not meet the requirement:

```json
{ "msg": "[system error] Failed to run cmd reload_sync_worker.py --sbucket=asrdr-32 1e-01 --slocation=oss-cn-****-d02-a --dbucket=asrdr-33e-10 --dlocation=oss-cn-****d01-a! ERRORMSG = (255)exception run dsu failed!\n\n, pls contact chiji support, req uest_id: 601ef3f7-4cc3-****8f2c4cf22fbf", "code": -1, "format_version": "1.0", "success": false, "request_id": "601ef3f7-****-8f2c4cf22fbf", "value": {} }
```

4. If the chiji version meets the requirement, check the logs of the acceleration operation. If
success is displayed in the logs but the 200 error code is returned, contact the OSS team for technical support.

### 6.7 MaxCompute

#### 6.7.1 Why am I unable to find MaxCompute projects when I configure a synchronization entity in ASR-DR?

**projects when I configure a synchronization**

**entity in ASR-DR?**

This topic describes how to resoleve the error that no MaxCompute project can be found when you configure a synchronization entity in ASR for Geo-disaster Recovery (ASR-DR).

**Problem description**

After you select the primary and secondary DataWorks workspaces when you configure a synchronization entity on ASR-DR, no MaxCompute project can be found. The following figure shows an example.

**Cause**

To enable disaster recovery, make sure that MaxCompute and DataWorks meet the following requirements: The names of the primary and secondary DataWorks workspaces must be consistent. The names of the primary and secondary MaxCompute projects and accounts that are used to run tasks must be consistent.

**Solution**

1. Configure the names of the primary and secondary DataWorks workspaces to ensure
consistency. For more information, see DataWorks User Guide.
2. Configure the names of the primary and secondary MaxCompute projects and accounts that
are used to run tasks to ensure consistency. For more information, see MaxCompute User Gui de.

### 6.8 ApsaraMQ

#### 6.8.1 How do I view the message details of primary and secondary ApsaraMQ instances?

**primary and secondary ApsaraMQ instances?**

This topic describes the cause of the error that you cannot view the message details of primary and secondary ApsaraMQ instances by using ASR for Geo-disaster Recovery (ASR-DR)). This topic also describes how to resolve the error.

**Problem description**

You cannot view the message consumption and synchronization details of primary and secondary ApsaraMQ instances by using ASR-DR.

**Cause**

ASR-DR does not provide the feature to view the message consumption and synchronization details of primary and secondary ApsaraMQ instances.

**Solution**

1. Log on to the container to which the mq-broker.DeployBroker# server role belongs from the
primary and secondary sites. For more information, see Log on to a container.
2. Run the following command to view the message consumption and synchronization details.

```
sh rmq/bin/mqadmin consumerProgress -g <Instance ID>%< groupId> -t <Instance ID>%< topic>
```

The following table describes the parameters of the primary ApsaraMQ instance.

| Parameter | Description |
|---|---|
| Broker Offset | All messages on the primary site. |
| Consumer Offset | All consumed messages. |
| Diff | The unconsumed messages. |
| LastTime | The time when messages were last consumed. |
| Diff Total | The total number of unconsumed messages. |

#### 6.8.2 How do I reset a consumer offset by running a command?

**running a command?**

After your business is switched from a primary ApsaraMQ instance to a secondary ApsaraMQ instance, if the consumer offset of the secondary ApsaraMQ instance is 0 or the consumer offset of the secondary ApsaraMQ instance is significantly different from that of the primary ApsaraMQ instance, you must reset the consumer offset.

**Problem description**

After you switch your business from a primary ApsaraMQ instance to a secondary ApsaraMQ instance in Apsara Stack Resilience for Geo-disaster Recovery (ASR-DR), a consumer on the secondary site consumes a large number of messages that have been consumed. The consumer offset of the secondary ApsaraMQ instance is 0 or the consumer offset of the secondary ApsaraMQ instance is significantly different from that of the primary ApsaraMQ instance. For more information about how to query a consumer offset, see How do I view the message details of primary and secondary ApsaraMQ instances?

**Cause**

The consumer offset fails to be reset. The consumer offset of the primary instance is not synchronized to the secondary instance. When messages start to be synchronized, the consumer on the secondary site consumes a large number of messages that have been consumed.

**Solution**

1. Log on to the container to which the mq-broker.DeployBroker# server role belongs from the
primary and secondary instances. For more information, see Log on to a container.
2. Run the following command to reset the consumer offset:

```
sh rmq/bin/mqadmin resetOffsetByTime -g <Instance ID>%<groupId> -f true -s now -t <Instance ID>%<topic>
```

ut data consistency verification f or products that support DR

## 7 FAQ about data consistency verification for products that support DR

**verification for products that**

**support DR**

This topic describes the solutions to data loss and inconsistencies caused by failures in the failover process.

### 7.1 Perform full data verification and synchronization between RDS and PolarDB-X databases

**and synchronization between RDS**

**and PolarDB-X databases**

You can use Data Transmission Service (DTS) of the secondary data center to perform full verification of data in the RDS and PolarDB-X databases and correct data discrepancies.

**Background information**

> **Important:** A full data verification traverses all data of the RDS and PolarDB-X databases. This operation is resource-intensive. We recommend that you contact on-site O&M engineers to perform the operation during off-peak hours.

1. Log on to the Apsara Uni-manager Operations Console of the secondary data center.
2. In the top navigation bar, choose **Product Operation > Databases > Data Transmission**
**Service**.
3. Find the DTS synchronization task in the task list in the **DTS O&M console**. Click the task
name.
4. On the **Task Details** page, click **Full Data Verification** in the upper-right corner.
5. On the **Create Verification Task** page, configure the parameters. Retain the default values
for parameters except for the **Correction Enabled** and **Thread Count** parameters.

> **Note:** **Correction Enabled**: enables this option to correct discrepancies found.
> **Thread Count**: the number of parallel verification threads. We recommend that you specify less than 5 threads to prevent excessive load on the database.

6. Click **Create**.
7. On the **Tasks** page, click the name of the verification task that you created in the preceding
step.
8. On the **Task Details** page, click **Details** in the **Consistency Verification** section to view the
basic information about the consistency verification. On the **Basic Information** page, click **Modify** in the **Running Parameters** section to modify the command line parameters. The following table describes the parameters. ut data consistency verification f or products that support DR

| Parameter | Full name | Description |
|---|---|---|
| -c | --config | Required. Specifies the path to the configuration file. |
| -x | --fix | Enables data verification and correction. Note If you want to correct data discrepancies, you must configure this parameter. By default, this parameter is disabled. |
| -a | --server | Reports progress and discrepancy information to the DTS metadata database. By default, this parameter is disabled. |
| -l | --log | Specifies the path for log files, discrepancy records, and correction SQL. The default value is the directory in which the program is located. |
| -b | --batch | Specifies the size of data slices. Default value: 3000. We recommend that you retain the default value. |
| -A | --againbatch | Specifies the size of the recheck slice. Default value: 300. We recommend that you retain the default value. |
| -m | --max | Specifies the maximum number of discrepancies allowed for a single table. If the number of discrepancies exceeds this value, the table is not verified. Default value: 10000. Note If you verify consistency between heterogeneous data sources, we recommend that you increase the value. |
| -p | --process | Specifies the number of threads in the validation thread pool. The number is the same as the number of connections. Default value: 4. We recommend that you set the value to 2 in cloud environments and to 7 in non-cloud environments. |
| -n | --nokey | Specifies the data amount threshold for table verification. Only tables without unique indexes whose data amount is smaller than the threshold is verified. RDS implicit indexes are treated as unique indexes. If you specify an excessively large value for this parameter, slow SQL queries may occur. Default value: 10000. |
| -U | --upload | Works together with the -a parameter to specify the maximum number of discrepancies to upload to the DTS metadata database. Default value: 300. |

ut data consistency verification f or products that support DR

| -jobId | --jobId | Specifies the job ID of the verification task, which is the unique ID of the DTS task. |
|---|---|---|
| -encrypt | --encrypt | Encrypts the configuration file by using DTS encryption. The parameter is used together with the -jobId parameter. |
| -L | --level | Works together with the -x parameter to specify the correction level. Separates multiple correction levels with forward slashes (/). Example: insert/update/delete. |
| -ignore | --ignore | This parameter is not supported. This parameter is used to ignore levels, such as source/target/diff. |
| -multiple | --multiple | Uses an equality query on the destination database, which is suitable for data verification from sharded tables to a single table. This parameter cannot verify multiple data sources. |
| -trim | --trim | Ignores trailing spaces when comparing strings. By default, this parameter is disabled. |
| -singleindex | --singleindex | Performs verification by using a single index, which is suitable for scenarios in which the first field of a composite index has high distinctiveness. By default, this parameter is disabled. If you enable this option in Oracle, the query performance can be significantly improved. |
| -avoidCycle | --avoidCycle | Works together with the -x parameter to prevent cyclic corrections. By default, this parameter is disabled. |
| -d | --diff | Verifies the discrepancies from the previous check. |
| -record | --record | Verifies the discrepancies recorded in the previous database check. |

9. Views the verification results on the **Verification Objects** tab of the **Consistency**
**Verification**.

> **Note:** To view the differences between tables, click the
> icon in the **Diff Row** column.

You can also view the verification results in logs. The following table describes the logs.

| Scenario | Log path | Remarks |
|---|---|---|

ut data consistency verification f or products that support DR

| Query the details of the inconsistencies | Host on which DTS runs/log directory of the verification program/diff | On master: logs records that exist only in the source database. Only the indexes are printed. On slave: logs records that exist only in the destination database. Only the indexes are printed. Different: logs records in which the index is the same in the source and destination databases but differences exist in the fields or data types. Only indexes that have different fields and their data types are printed. |
|---|---|---|
| Query and correct SQL statements | Host on which DTS runs/log directory of the verification program/sql | None. |
| Query current inconsistencies | Host on which DTS runs/log directory of the verification program/fullcheck.log | If the verification progress is slow and the inconsistency results are not reported, you can search for WARN in this log. The log records the primary keys of the differing records, which can be used to manually compare the source and destination databases. |
| Query specific running records and error information | Host on which DTS runs/log directory of the verification program/fullcheck.log | If you want to view the execution details of the corresponding SQL statements, add the-g parameter to the command line. All executed SQL statements are printed in the log. |

### 7.2 Track the incremental data of a PolarDB-X instance

**PolarDB-X instance**

You can create a change tracking task for a PolarDB-X instance in the Data Transmission Service (DTS) console of the secondary data center to track the incremental data of the PolarDB- X instance.

**Procedure**

1. Log on to the DTS console of the secondary data center.
2. In the left-side navigation pane, click **Change Tracking**.
3. In the upper-right corner, click **Create Change Tracking Task**. In the Create DTS Instances
dialog box, select a region and an instance type and enter the number of change tracking instances that you want to create.

> **Note:** In the Create DTS Instances dialog box, you can view the total number of instances, the number of existing instances, and the number of instances that can be created.

ut data consistency verification f or products that support DR
4. Click **Create**.
5. Find the change tracking instance that you created, and click **Configure Channel** in the
Actions column.
6. Configure the source database.

| Section | Parameter | Description |
|---|---|---|
| N/A | Task Name | The task name that is automatically generated by DTS. We recommend that you specify a name that can help you identify the task. You do not need to specify a unique task name. |
| Source Database | Instance Type | The instance type of the source database. The value of this parameter is fixed to DRDS Instance. |
|   | Database Type | The type of the source database. The value of this parameter is fixed to DRDS. |
|   | Instance Region | The region in which the source database resides. The region is the source region that you selected when you created the change tracking instance. You cannot change the value of this parameter. |
|   | DRDS Instance ID | The ID of the source PolarDB-X instance. |
|   | Database Name | The name of the source database in the PolarDB-X instance. |
|   | Database Account | The database account of the PolarDB-X instance. |
|   | Database Password | The password of the database account. |

7. In the lower part of the page, click **Test Connectivity and Proceed**.
8. Select the data change types and objects.

| Parameter or setting | Description |
|---|---|

ut data consistency verification f or products that support DR

| Required Data Types | Data Update DTS tracks data updates of the selected objects, including INSERT, DELETE, and UPDATE operations. Schema Update DTS tracks the create, delete, and modify operations that are performed on all object schemas of the source instance. You must use the change tracking client to filter the data that you want to track. Note You can track data changes only at the table level. You cannot change the objects of an existing change tracking task. If you want to track the data changes of tables that are not included in the selected objects, you must create another change tracking task for the tables. |
|---|---|
| Required Objects | Select tables from the Required Objects section and click the icon to move the tables to the Selected section. |
| Retry Time for Failed Connections | If DTS fails to connect to the source database, DTS automatically retries within the following 12 hours. You can specify the retry time range based on your business requirements. If DTS is reconnected to the source database instance within the specified time range, DTS resumes the change tracking task. Otherwise, the change tracking task fails. Note You are charged when DTS retries a connection. We recommend that you specify the retry time range based on your business requirements or release the DTS instance immediately after the source database instance is released. |

9. 0.

### 7.3 Verify Tablestore data consistency

**consistency**

You can create an external table on MaxCompute and import Tablestore data to MaxCompute. Then, use a script to check whether the data is consistent.

**Background information**

Perform the following operations in the primary and secondary centers:

**Operations in MaxCompute**

1. Log on to the MaxCompute console.
In the top navigation bar of the Apsara Uni-manager Management Console, choose **Products**
**> Big Data Computing > MaxCompute**.
2. Create an account used to run tasks.
i. In the left-side navigation pane, click Task Accounts. On the upper-right part, click **Create**
**Account**.
ii. In the Create Account dialog box, configure the Name and Organization parameters. Then, click **OK**. ut data consistency verification f or products that support DR
3. Create a quota group.
i. In the left-side navigation pane, click Quota Groups. In the upper-right part, click **Create**. ii. Configure the parameters. Then, click Submitted.

> **Note:** For more information about the parameter descriptions, see MaxCompute User Guide.

4. Create a project.
i. In the left-side navigation pane, click Projects. In the upper-right part, click **Create**
**MaxCompute Project**.
ii. On the page that appears, configure the parameters and click Submitted.

> **Note:** For more information about the parameter descriptions, see MaxCompute User Guide.

**Query the number of data entries of a Tablestore table in**

**DataWorks**

1. Log on to the DataWorks console.
In the top navigation bar of the Apsara Uni-manager Management Console, choose **Products**
**> Big Data Computing > DataWorks**.
2. **(Optional)** The first time you use DataWorks for the first time, add a MaxCompute engine.
i. In the top navigation bar, click the icon. ut data consistency verification f or products that support DR ii. In the left-side navigation pane, click **Project Management**. In the **Computing Engine**
**information** section, select the MaxCompute project.
3. On the DataStudio page of DataWorks, create a workflow.
4. Create a foreign table.
i. In the left-side navigation pane, click the created workflow, right-click **MaxCompute**, and then choose **Create > ODPS SQL**. ii. In the Create Node dialog box, enter the node name, select the required folder, and then click **Submit**. iii. Create a MaxCompute table. Associate the table with a Tablestore table. ut data consistency verification f or products that support DR

```
set odps.sql.hive.compatible=true; set odps.sql.external.table.enable=true; CREATE EXTERNAL TABLE IF NOT EXISTS ots_external_table (--(1) id string, name string
```

`)`

```
STORED BY 'com.aliyun.odps.TableStoreStorageHandler'-- (2) WITH SERDEPROPERTIES (-- (3) 'tablestore.columns.mapping'=':id, :name',-- (4) 'tablestore.table.name'='test'-- (5)
```

`)`

```
LOCATION 'tablestore://<your_AccessKeyID>:<your_AccessKeySecret>@<YOUR_ENDPOINT>';-- (6) select count(*) as sum from ots_external_table;
```

| Number | Parameter | Description |
|---|---|---|
| (1) | id string, name string | The fields for the table. |
| (2) | com.aliyun.odps.TableStoreSto rageHandler | StorageHandler is a built-in feature of MaxCompute that allows you to process Tablestore data. StorageHandler defines the interaction between MaxCompute and Tablestore. MaxCompute implements related logic. |
| (3) | SERDEPROPERITES | The operation that provides parameter options. The tablestore.columns.mapping and tablestore.table.name parameters are required for TableStoreStorageHandler. |
| (4) | tablestore.columns.mapping | Required. The columns of the Tablestore table to be accessed by MaxCompute. The columns include the primary key columns and attribute columns. If a colon (:) is included in the name of a column, the column is a primary key column of the Tablestore table. In this example, :vid and :gt are primary key columns of the Tablestore table. Other columns are attribute columns. You must specify all primary key columns of the table in Tablestore when you specify the mapping. You need to only specify the attribute columns that MaxCompute accesses. You do not need to specify all attribute columns. |

ut data consistency verification f or products that support DR

| (5) | tablestore.table.name | The name of the Tablestore table to be accessed. If the specified name of the Tablestore table does not exist, an error occurs. MaxCompute does not create Tablestore tables. |
|---|---|---|
| (6) | LOCATION | The information about the Tablestore instance to be accessed. The information includes the AccessKey ID, AccessKey secret, and endpoint. |

5. Click the
icon to execute the script. You can view the number of data entries in the Tablestore table in the primary data center.
6. Perform the preceding steps in the secondary data center to check whether the number of
data entries is consistent between the secondary and primary data centers.

### 7.4 Verify MaxCompute data consistency

**consistency**

To verify MaxCompute data consistency, submit a ticket to obtain the verification tool from the R&D team. Use the tool to create and run a MaxCompute data consistency verification task.

**Procedure**

1. Create a MaxCompute data consistency verification task.
Call the /task/create API to create a MaxCompute data consistency verification task. ut data consistency verification f or products that support DR `{`

```json
 "srcRegionId": "cn-wulan-env200-d01",
 "srcInstanceId": "",
 "srcVpcId": "",
 "srcIp": "service.cn-wulan-env200-d01.odps.inter.env200.shuguang.com",
 "srcPort": 80,
 "srcAccountName": "nUYGMfdPj5Pz27Bn",
 "srcPassword": "0udAuvuQmUyFCOJknUcMbxVQMBdhgg",
 "dstRegionId": "cn-qingdao-env33-d01",
 "dstInstanceId": "",
 "dstVpcId": "",
 "dstIp": "service.cn-qingdao-env33-d01.odps.env33.com",
 "dstPort": 80,
 "dstAccountName": "6a3F0hFBKZow1iBK",
 "dstPassword": "qIGHPdTxdGOPBBi7Qh9FljXJfod5ty",
 "productName": "ODPS",
 "compareObjectList": [
```

`{`

```json
 "dbName": "consistency_test",
 "compareTables": [
```

`{`

```json
 "tableName": "t_1m"
```

`},` `{`

```json
 "tableName": "t_10m"
```

`},` `{`

```json
 "tableName": "t_100m"
```

`},` `{`

```json
 "tableName": "t_1g"
```

`},` `{`

```json
 "tableName": "t_10g"
```

`},` `{`

```json
 "tableName": "t_100g"
```

`}` `]` `}` `],`

```json
 "timeout": 600000,
 "taskType": "STANDARD"
```

`}` If a result as shown in the following figure is returned, the task is created. ut data consistency verification f or products that support DR
2. Start the task.
Call the /task/start API to start the task. `{`

```json
 "taskId" : 253687010591954944
```

`}` If a result as shown in the following figure is returned, the task is started. If you call the /task/start API when the task is in the running or archived state, the following result is returned:
3. View the execution result of the task. The following table describes the execution results.

| Result | Description | Response |
|---|---|---|

ut data consistency verification f or products that support DR

| Task successfully completed | The task was successfully executed, the consistency check was successful, and all sub-steps were finished. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": true, "taskStatus": "FINISHED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692183383554, "costTime": 254385, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FINISHED" } ], "detailLog": "" } } } |
|---|---|---|

ut data consistency verification f or products that support DR

| Task failed due to timeout | The task failed because it exceeded the time limit. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692185149634, "costTime": 60714, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "RUNNING" } ], "detailLog": "Timeout" } } } |
|---|---|---|

ut data consistency verification f or products that support DR

| Pre-check failed due to missing table | The task failed during pre- check because the destination table schema failed to be retrieved. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692185454492, "costTime": 6246, "stepStatus": [ { "stepName": "PRECHECK", "status": "FAILED" }, { "stepName": "CHECKROWCOUNT", "status": "" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "Failed to obtain the destination table schema." } } } |
|---|---|---|

ut data consistency verification f or products that support DR

| Task failed due to row count mismatch | The row count check (CHECKROWCOUNT) detected a discrepancy in the number of rows between the source and destination tables. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692196225091, "costTime": 16451, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FAILED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "Destination table: t 1m, data _ rows: 4095, inconsistent with source data rows: 4096" } } } |
|---|---|---|

ut data consistency verification f or products that support DR

| Task failed due to data mismatch | The data check (CHECKDATA) detected a mismatch between the data in the source and destination tables. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "FAILED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692196609544, "costTime": 15402, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FAILED" } ], "detailLog": "The checksum for table t 1m _ does not match: source checksum 6ab792ad, destination checksum c9256398." } } } |
|---|---|---|

**Related operations**

ut data consistency verification f or products that support DR

| Operation | Description | Response |
|---|---|---|

ut data consistency verification f or products that support DR

| Retry a task | This operation re-executes a failed task. When the /task/retry API is called, only the sub-tasks that did not start are executed. When you perform the retry operation, the system creates the t 1m table in the source to match _ the table in the destination. The system calls the /task/retry API to retry the task. In this example, the task status is successful and the duration is 13778 milliseconds, which is the time used to verify the data consistency of the t 1m table. _ This indicates that the retry operation is successful. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": true, "taskStatus": "FINISHED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692197074880, "costTime": 13778, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "FINISHED" }, { "stepName": "CHECKDATA", "status": "FINISHED" } ], "detailLog": "" } } } Sample result: { "timestamp": 1692201556515, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/retry" } |
|---|---|---|

ut data consistency verification f or products that support DR

| Stop a task | You can perform this operation only if the task is in the RUNNING state. Start a task and call the /task/stop API. The task enters the STOPPED state during the CHECKROWCOUNT substep. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "STOPPED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692198894885, "costTime": 7747, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "STOPPED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "stopped" } } } Sample result: { "timestamp": 1692201618671, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/stop" } |
|---|---|---|

ut data consistency verification f or products that support DR

| Delete a task | You can call the /task/delete API to delete a task only if the task is not in the RUNNING state. The operation transitions the task to the ARCHIVED state. | { "result": "SUCCESS", "code": "200", "nodeHost": "U-6MXK0F1Q-1934.local", "nodeIp": "127.0.0.1", "data": { "task": { "taskId": 253687010591954944, "success": false, "taskStatus": "ARCHIVED", "checkTotal": 0, "successTotal": 0, "failTotal": 0, "startTime": 1692198894885, "costTime": 7747, "stepStatus": [ { "stepName": "PRECHECK", "status": "FINISHED" }, { "stepName": "CHECKROWCOUNT", "status": "STOPPED" }, { "stepName": "CHECKDATA", "status": "" } ], "detailLog": "stopped" } } } Sample result: { "timestamp": 1692201760347, "status": 500, "error": "Internal Server Error", "message": "The status of consistency is invalid", "path": "/asr-web/task/delete" } |
|---|---|---|

d references

## 8 Command references

### 8.1 Use CLISH commands

When the ASR for Geo-disaster Recovery system encounters issues and the ASR for Geo-disaster Recovery console is inaccessible, you can use CLISH commands to perform background operations.

> **Warning:** Before you use a CLISH command, make sure that you understand the effects and consequences of the command.
> Command-line operations involve risks. Proceed with caution. You can perform command- line operations only if an error occurs in the ASR for Geo-disaster Recovery system and cannot be resolved in the console.

1. Log on to the container in which the ASR-DR service is running. For more information, see Log
on to a container.
2. Go to the CLISH directory and launch the CLISH interactive shell.

```
cd /alidata/bin/ java -jar clish-3.0.0.jar
```

3. Enter the commands that you want to run.

### 8.2 Commands

This topic describes ASR for Geo-disaster Recovery O&M commands.

| Parameter | Description |
|---|---|
| skip-entity | Skips a synchronization entity in the current plan execution. |
| suspend-entity | Suspends a synchronization entity. |
| stepover-entity | Skips a synchronization entity in the current step of the plan execution. |
| reprotect-entity | Performs reprotection for a synchronization entity. |
| redo-entity | Performs a retry on a synchronization entity. |
| force-switch | Performs a forced switchover for a synchronization entity. |

d references

| Parameter | Description |
|---|---|
| del-cloud-instance | Removes the association between a user and a cloud instance. |
| del-cloud-center | Deletes a cloud center. |

| Parameter | Description |
|---|---|
| create-empty-pg | Creates an empty protection group. |
| show-pg-sync-entity | Views the synchronization entities contained in a specified protection group. |
| delete-pg-shell | Deletes a protection group |
| move-sync-entity | Relocates a synchronization instance to a specified protection group. |

| Parameter | Description |
|---|---|
| plan-query | Queries the details of a disaster recovery plan. |
| plan-query-ex | Queries the details of a disaster recovery plan task. |
| plan-force-delete | Forcibly deletes a disaster recovery plan, including plans that are running. |

| Parameter | Description |
|---|---|
| vpc-register-app | Registers an application with a Virtual Private Cloud (VPC) instance. |

|   | ASR for Geo-disaster Operations |
|---|---|

d references

| Parameter | Description |
|---|---|
| vpc-show-registered-app | Queries applications that are registered with a VPC instance. |
| vpc-remove-registered-app | Unregisters an application from a VPC instance. |
| vpc-grant-access | Grants access permissions on a VPC instance. |
| vpc-show-grant-access | Queries the authorized list of a VPC instance. |
| vpc-cancel-grant-access | Revokes the access of a disaster recovery instance to a VPC instance. |

**PolarDB-X instances**

| Parameter | Description |
|---|---|
| xdm-clear-data | Cleans up data of a PolarDB-X instance. |

**AnalyticDB for MySQL V3.0 databases**

| Parameter | Description |
|---|---|
| adb-force-start-sync | Forcibly starts a synchronization link. |

| Parameter | Description |
|---|---|
| param-add-param | Adds configurations. |
| param-modify-param | Modifies configurations. |
| param-query-param | Queries configurations |
| param-refresh-param | Refreshes configurations. |
| param-modify-params | Modifies the configurations of a service. |

| nd Maintenance Guide·Comman references | Apsara Stack Resilienc |
|---|---|

| Parameter | Description |
|---|---|
| param-query-params | Queries the configurations of a service. |

| Parameter | Description |
|---|---|
| alarm-create | Creates an alert. |
| alarm-query | Queries alert information. |
| send-alarm-msg | Sends alerts. |

| Parameter | Description |
|---|---|
| rule-create | Creates an alert rule. |
| rule-query | Queries an alert rule. |
| rule-switch | Enables or disables an alert rule. |
| rule-update | Modifies an alert rule. |
| rule-delete | Deletes an alert rule. |

| Parameter | Description |
|---|---|
| monitor-item-query | Queries monitored metrics. |

### 8.3 Synchronization entities

#### 8.3.1 skip-entity

You can use the skip-entity command to skip a synchronization entity in the current plan execution. d references

**Syntax**

```
skip-entity [-eid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -eid | Yes | The ID of the synchronization entity. |

**Examples**

```
skip-entity -eid 5e81a414-4d88-4de3-9921-f1ef51f******
```

#### 8.3.2 suspend-entity

You can use the suspend-entity command to suspend a synchronization entity.

**Syntax**

```
suspend-entity [-eid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -eid | Yes | The ID of the synchronization entity. |

**Examples**

```
suspend-entity -eid 45eadd00-68a4-462d-85fb-c81bb******
```

#### 8.3.3 stepover-entity

You can use the stepover-entity command to skip a synchronization entity in the current step of the plan execution.

**Syntax**

```
stepover-entity [-eid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|

d references

| Parameter | Required | Description |
|---|---|---|
| -eid | Yes | The ID of the synchronization entity. |

**Examples**

```
stepover-entity -eid 45eadd00-68a4-462d-85fb-c81bb******
```

#### 8.3.4 reprotect-entity

You can use the reprotect-entity to perform reprotection for a synchronization entity.

**Syntax**

```
reprotect-entity [-eid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -eid | Yes | The ID of the synchronization entity. |

**Examples**

```
reprotect-entity -eid 45eadd00-68a4-462d-85fb-c81bbd******
```

#### 8.3.5 redo-entity

You can use the redo-entity command to perform a retry on a synchronization entity.

**Syntax**

```
redo-entity [-eid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -eid | Yes | The ID of the synchronization entity. |

**Examples**

```
redo-entity -eid 45eadd00-68a4-462d-85fb-c81bbd******
```

d references

#### 8.3.6 force-switch

You can use the force-switch command to perform a forced switchover for a synchronization entity.

**Syntax**

```
force-switch [-sid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -sid | Yes | The ID of the synchronization entity. |

**Examples**

```
force-switch -sid 45eadd00-68a4-462d-85fb-c81bb******
```

### 8.4 Cloud Center

#### 8.4.1 del-cloud-instance

You can use the del-cloud-instance command to remove the association between a user and a cloud instance.

**Syntax**

```
del-cloud-instance [-uid] string [-cid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -uid | Yes | The ID of the user. |
| -cid | Yes | The ID of the cloud instance. |

**Examples**

```
del-cloud-instance -uid 5003 -cid bc982df6-f193-4aab-a6e2-b8b240******
```

#### 8.4.2 del-cloud-center

d references You can use the del-cloud-center command to delete a cloud center.

**Syntax**

```
del-cloud-center [-cid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -cid | Yes | The ID of the cloud center. |

**Examples**

```
del-cloud-center -cid e6671a7c-26af-4737-b930-1b37a5******
```

### 8.5 Protection groups

#### 8.5.1 create-empty-pg

You can use the create-empty-pg command to create an empty protection group.

**Syntax**

```
create-empty-pg [-pname] string [-morgid] int [-borgid] int [-mcid] string [-bcid] string [-mrid] string [-brid] string [-d] string [-D] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pname | Yes | The name of the protection group. |
| -morgid | Yes | The organization ID of the primary site. |
| -borgid | Yes | The organization ID of the secondary site. |
| -mcid | Yes | The ID of the primary site. |
| -bcid | Yes | The ID of the secondary site. |
| -mrid | Yes | The region ID of the primary site. |

|   |   | ASR for Geo-disaster Operations |
|---|---|---|

d references

| Parameter | Required | Description |
|---|---|---|
| -brid | Yes | The region ID of the secondary site. |
| -d | Yes | The synchronization direction. Valid values: FORWARD REVERSE |
| -D | Yes | The description of the protection group. |

**Examples**

```
create-empty-pg -pname pgClish -morgid 30 -borgid 3 -mcid d132c3b0-4299-4d0a-9962- 350***** -bcid 61f1f331-76df-43be-8bf2-856e75d***** -mrid cn-qingdao-*****-d01 -brig cn-q ingdao-*****-d01 -d FORWARD -D testGroupBuileby****
```

#### 8.5.2 show-pg-sync-entity

You can use the show-pg-sync-entity command to view the synchronization entities contained in the specified protection group.

**Syntax**

```
show-pg-sync-entity [-pgId] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pgId | Yes | The ID of the protection group. |

**Examples**

```
show-pg-sync-entity -pgId 0f0cc4dc-c95f-47cb-b8b4-1a72e2******
```

#### 8.5.3 delete-pg-shell

You can use the delete-pg-shell command to delete a protection group without deleting the associated synchronization instances. The synchronization instances become orphaned.

**Syntax**

```
delete-pg-shell [-pgId] string
```

**Parameters**

d references

| Parameter | Required | Description |
|---|---|---|
| -pgId | Yes | The ID of the protection group. |

**Examples**

```
delete-pg-shell -pgId cb973344-3a7d-49f5-8517-6245bd******
```

#### 8.5.4 move-sync-entity

You can use the move-sync-entity command to migrate a synchronization entity to a protection group.

**Syntax**

```
move-sync-entity [-sid] string [-pgId] string [-p] int
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pgId | Yes | The ID of the protection group. |
| -sid | Yes | The ID of the synchronization entity. |
| -p | Yes | The priority. |

**Examples**

```
move-sync-entity -sid 5e81a414-4d88-4de3-9921-f1ef51f***** -pgId 472481ee-717c-41bc-b3b8- 192631f***** -p 3
```

### 8.6 Disaster recovery plans

#### 8.6.1 plan-query

You can use the plan-query command to query the details of a disaster recovery plan.

**Syntax**

**plan-query [-pid] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|

d references

| -pid | Yes | The ID of the disaster recovery plan. |
|---|---|---|

**Examples**

**plan-query -pid 375c09d5-e803-4770-a3ec-fa4358**

#### 8.6.2 plan-query-ex

You can use the plan-query-ex command to query the execution details of a disaster recovery plan.

**Syntax**

**plan-query-ex [-pid] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pid | Yes | The ID of the disaster recovery plan. |

**Examples**

**plan-query-ex -pid 375c09d5-e803-4770-a3ec-b37fa4**

#### 8.6.3 plan-force-delete

You can use the plan-force-delete command to forcibly delete a disaster recovery plan regardless of the running status.

**Syntax**

```
plan-force-delete [-pid] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pid | Yes | The ID of the disaster recovery plan. |

**Examples**

```
plan-force-delete -pid f67e0b29-519a-433d-bf8f-b38fb4******
```

### 8.7 VPC

#### 8.7.1 vpc-register-app

To enable ASR for Geo-disaster Recovery to access a Virtual Private Cloud (VPC) instance, you can use the vpc-register-app command to register ASR for Geo-disaster Recovery with the VPC instance. d references

**Syntax**

```
vpc-register-app [-c] string [r] string [-ips] strings
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -r | Yes | The ID of the region. |
| -ips | Yes | The IP address that you want to register with the VPC. Specify the IP address in the JSON array format. |

**Examples**

```
vpc-register-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-******-***-d01 -ips []
```

#### 8.7.2 vpc-show-registered-app

You can use the vpc-show-registered-app command to query information about applications registered with a Virtual Private Cloud (VPC) instance.

**Syntax**

```
vpc-show-registered-app [-c] string [-r] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -r | Yes | The ID of the region. |

**Examples**

```
vpc-show-registered-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-*****-***-d01
```

#### 8.7.3 vpc-remove-registered-app

You can use the vpc-remove-registered-app command to unregister an application from a Virtual Private Cloud (VPC) instance. d references

**Syntax**

```
vpc-remove-registered-app [-c] string [-r] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -r | Yes | The ID of the region. |

**Examples**

```
vpc-remove-registered-app -c ff28e461-fbec-449e-8d33-94d7f0****** -r cn-*****-***-d01
```

#### 8.7.4 vpc-grant-access

You can use the vpc-grant-access command to grant access permissions on a Virtual Private Cloud (VPC) instance.

**Syntax**

```
vpc-grant-access [-v] string [-i] string [-p] string [-r] string [-c] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -v | Yes | The ID of the VPC. |
| -i | Yes | The ID of the protected instance. |
| -p | Yes | The port of the protected instance. |
| -r | Yes | The ID of the region. |
| -c | Yes | The ID of the cloud instance. |

**Examples**

```
vpc-grant-access -v vpc-7qc0ujuxfw838m9n****** -i rm-7qcv3h8q497****** -p 3306 -r cn-**** *-***-d01 -c a37eb466-cc43-4347-9e96-5685dbc*****
```

d references

#### 8.7.5 vpc-show-grant-access

You can use the vpc-show-grant-access command to query the authorized list of a Virtual Private Cloud (VPC) instance.

**Syntax**

```
vpc-show-grant-access [-c] string [-i] string [-r] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -i | Yes | The ID of the protected instance. |
| -r | Yes | The ID of the region. |

**Examples**

```
vpc-show-grant-access -c a37eb466-cc43-4347-9e96-5685dbc1**** -i rm-7qcv3h8q497****** -r cn-*****-***-d01
```

#### 8.7.6 vpc-cancel-grant-access

You can use the vpc-show-grant-access command to revoke the access of a protected instance to a Virtual Private Cloud (VPC) instance.

**Syntax**

```
vpc-cancel-grant-access [-c] string [-v] string [-i] string [-p] string [-r] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -v | Yes | The VPC ID. |
| -i | Yes | The ID of the protected instance. |
| -p | Yes | The port of the protected instance. |

|   | Apsara Stack Resilience |   | ASR for Geo-disaster Operations and Maintenance Guide·Comma d reference | n s |
|---|---|---|---|---|

| Parameter | Required | Description |
|---|---|---|
| -r | Yes | The ID of the region. |

**Examples**

```
vpc-cancel-grant-access -c a37eb466-cc43-4347-9e96-5685dbc1**** -v vpc- 7qc0ujuxfw838m9n****** -i rm-7qcv3h8q497****** -p 3306 -r cn-*****-***-d01
```

### 8.8 PolarDB for Xscale (PolarDB-X)

#### 8.8.1 xdm-clear-data

You can use the xdm-clear-data command to clean up data of a PolarDB-X instance.

**Syntax**

```
xdm-clear-data [-c] string [-r] string [-i] string [-t] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -c | Yes | The ID of the cloud instance. |
| -r | Yes | The region ID. |
| -i | Yes | The instance ID of the cloud service. |
| -t | Yes | The type of cloud service instance. |

**Examples**

```
xdm-clear-data -c a37eb466-cc43-4347-9e96-5685dbc1**** -r cn-*****-****-d01 -i rm- 7qczre4wb67****** -t ADB
```

### 8.9 AnalyticDB for MySQL V3.0

#### 8.9.1 adb-force-start-sync

You can use the adb-force-start-sync command to forcibly start a synchronization link. d references

**Syntax**

```
adb-force-start-sync [-r] string [-c] string [-i] string [-pk] string [-oppId] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -r | Yes | The region ID. |
| -c | Yes | The ID of the cloud instance. |
| -i | Yes | The ID of the protected instance. |
| -pk | Yes | The primary key of the user. |
| -oppId | Yes | The ID of the destination cluster. |

**Examples**

```
adb-force-start-sync -i drdsusrzl1****** -r cn-*****-***-d01 -c a624e61c-c37e-4771-be06-1 d725cd2**** -pk 1223333 -oppId 6aYxs
```

### 8.10 Configurations

#### 8.10.1 param-add-param

You can use the param-add-param command to add configurations for a service.

**Syntax**

```
param-add-param [-pdn] string [-pn] string [-pv] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pdn | Yes | The name of the service. |
| -pn | Yes | The attribute name. |
| -pv | Yes | The attribute value. |

d references

**Examples**

```
param-add-param -pdn OSS -pn timeout -pv 10000
```

#### 8.10.2 param-modify-param

You can use the param-modify-param command to modify the configurations of a service.

**Syntax**

```
param-modify-param [-pdn] string [-pn] string [-pv] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pdn | Yes | The name of the service. |
| -pn | Yes | The attribute name. |
| -pv | Yes | The attribute value. |

**Examples**

```
param-modify-param -pdn OSS -pn timeout -pv 60000
```

#### 8.10.3 param-query-param

You can use the param-query-param command to query the configurations of a service.

**Syntax**

```
param-query-param [-pdn] string [-pn] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pdn | Yes | The name of the service. |
| -pn | Yes | The attribute name. |

**Examples**

```
param-query-param -pdn OSS -pn timeout
```

d references

#### 8.10.4 param-refresh-param

You can use the param-refresh-param command to refresh the configurations of a service.

**Syntax**

```
param-refresh-param [-pdn] string [-pn] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pdn | Yes | The name of the service. |
| -pn | Yes | The attribute name. |

**Examples**

```
param-refresh-param -pdn OSS -pn timeout
```

#### 8.10.5 param-modify-params

You can use the param-query-params command to modify the configurations of a product.

**Syntax**

```
param-modify-params [-pj] string
```

**Parameters**

| Parameter |   | Required | Description |   |
|---|---|---|---|---|
| -pj |   |   | A JSON array of all property values of the product. Format: [{"product":"Product name","params": |   |
|   |   |   |   | [{"product":"Product name","params": |
|   |   | Yes | {"Config item":"Config info","Config |   |
|   |   |   | item":"Config info"}}] |   |

**Examples**

```json
param-modify-params -pj '[{"product":"oss","params": {"apiRetryCount":"5","apiRetryDelay":"40000"}}]'
```

d references

#### 8.10.6 param-query-params

You can use the param-query-params command to query all configurations of a service.

**Syntax**

```
param-query-params [-pdn] string
```

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -pdn | Yes | The name of the service. |

**Examples**

```
param-query-params -pdn OSS
```

### 8.11 Alerts

#### 8.11.1 alarm-create

You can use the alarm-create command to create an alert.

**Syntax**

**alarm-create [-r] string [-alarmObjId] string [-c] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -r | Yes | The ID of the alert rule. |
| -alarmObjId | Yes | The information about the alert objects. Specify the alert objects in the JSON array format. Format: [\"objectId1\",\"objectId2\"] |
| -c | Yes | The alert content. |

**Examples**

**alarm-create -r 72b079c4-ce56-45cb-8dae- -alarmObjId [\"ef894d5d-3dee-4e6a-**

**b989-e946ede\"] -c test**

#### 8.11.2 alarm-query

You can use the alarm-query command to query alert information.

**Syntax**

d references

**alarm-query [-n] string [--monitorId] string [-alarmObjName] string [-l] string [-st]**

**string [-et] string [-c] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -n | No | The name of the alert rule. |
| --monitorId | No | The ID of the monitored metric. |
| -alarmObjName | No | The name of the object that is monitored by the alert. |
| -l | No | The alert severity. Valid values: 1: FATAL 2: ERROR 3: WARNING 4: INFO |
| -st | No | The time when the alert occurred. Specify the time in the UNIX timestamp format. Unit: milliseconds. Note You can use related tools to convert the time into a Unix timestamp. |
| -et | No | The time when the alert was cleared. Specify the time in the UNIX timestamp format. Unit: milliseconds. |
| -c | No | The ID of the cloud instance. |

**Examples**

**alarm-query -n testRule --monitorId PROTECT_STATE -l 2 -alarmObjName otsTest -st**

**"2021-11-25 00:00:00" -et "2021-11-25 23:59:59" -c 6ca60a24-2d3d-4221-b5d3-**

**b7998d5**

#### 8.11.3 send-alarm-msg

You can use the send-alarm-msg command to send alerts to alert contacts.

**Syntax**

**send-alarm-msg [--monitorId] string [-l] string [-alarmObjName] string [-lookAddr]**

**string [-c] string [--notifyType] string [--notifyUserIds] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| --monitorId | Yes | The ID of the monitored metric. |

d references

| -l | Yes | The alert severity. Valid values: 1: FATAL 2: ERROR 3: WARNING 4: INFO |
|---|---|---|
| -alarmObjName | Yes | The name of the object that is monitored by the alert. |
| -lookAddr | Yes | The address at which you can find information about the alarm. |
| -c | Yes | The alert content. |
| --notifyType | Yes | The notification method. Specify the notification method in the JSON array format. Valid values: ASO ANS DING _ ANS EMAIL _ ANS SMS _ |
| --notifyUserIds | Yes | The primary key of the alert contact. Specify the primary key in the JSON array format. |

**Examples**

**send-alarm-msg --monitorId PROTECT_STATE -l 2 -alarmObjName testObj -lookAddr**

**WWW.example.COM -c example --notifyType [\"ANS_EMAIL\"] --notifyUserIds**

**[\"2638888\"]**

### 8.12 Alert rules

#### 8.12.1 rule-create

You can use the rule-create command to create an alert rule.

**Syntax**

**rule-create [-n] string [-c] string [--deptId] string [--monitorId] string [-o] string [-v]**

**string [-d] string [-l] string [--notifyUserIds] string [--notifyType] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -n | Yes | The name of the alert rule. |
| -c | Yes | The ID of the cloud instance. |
| --deptId | Yes | The organization ID. |
| --monitorId | Yes | The ID of the monitored metric. |
| -o | Yes | The comparison operator, such as an equal sign (=). |

d references

| -v | Yes | The value against which the monitored metric is compared. |
|---|---|---|
| -d | Yes | The description of the alert rule. |
| -l | Yes | The alert severity. Valid values: 1: FATAL 2: ERROR 3: WARNING 4: INFO |
| --notifyUserIds | Yes | The alert contacts. Specify the alert contacts in the JSON array format. |
| --notifyType | Yes | The notification method. Specify the notification method in the JSON array format. Valid values: ASO ANS DING _ ANS EMAIL _ ANS SMS _ |

**Examples**

**rule-create -n testRule -c 6ca60a24-2d3d-4221-b5d3-b7998d5 --deptId 3 --**

**monitorId PROTECT_STATE -o = -v PROTECT_FAIL -d Alert description -l 2 --**

**notifyUserIds [\"ExampleUser\"] --notifyType [\"ANS_EMAIL\"]**

#### 8.12.2 rule-query

You can use the rule-query command to query an alert rule.

**Syntax**

**rule-query [-n] string [-l] string [--deptId] string [--monitorId] string [-s] string [-c]**

**string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -n | Yes | The name of the alert rule. |
| -l | No | The alert severity. Valid values: 1: FATAL 2: ERROR 3: WARNING 4: INFO |
| --deptId | No | The organization ID. |
| --monitorId | No | The ID of the monitored metric. |
| -s | No | The status of the rule. Valid values: STOPPED RUNNING |

d references

| -c | No | The ID of the cloud instance. |
|---|---|---|

**Examples**

**rule-query -n testRule -s RUNNING -l 2 --deptIds [\"20\"] --monitorId PROTECT_STATE -**

**c 6ca60a24-2d3d-4221-b5d3-b79982c4**

#### 8.12.3 rule-switch

You can use the rule-switch command to enable or disable an alert rule.

**Syntax**

**rule-switch [-rid] string [-s] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -rid | Yes | The ID of the alert rule. |
| -s | Yes | Specifies whether to enable or disable the rule. RUNNING: enables the rule. STOPPED: disables the rule. |

**Examples**

**rule-switch -rid 72b079c4-ce56-45cb--71b94f7e6f9c -s STOPPED**

#### 8.12.4 rule-update

You can use the rule-update command to update an alert rule.

**Syntax**

**rule-update [-r] string [-n] string [--deptId] string [--monitorId] string [-o] string] [-v]**

**string [-d] string [-l] string [--notifyUserIds] string [--notifyType] string [-u] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -r | Yes | The ID of the alert rule. |
| -n | Yes | The name of the alert rule. |
| --deptId | Yes | The organization ID. |
| --monitorId | Yes | The ID of the monitored metric. |
| -o | Yes | The comparison operator, such as an equal sign (=). |
| -v | Yes | The value against which the monitored metric is compared. |
| -d | Yes | The description of the alert rule. |

d references

| -l | Yes | The alert severity. Valid values: 1: FATAL 2: ERROR 3: WARNING 4: INFO |
|---|---|---|
| --notifyUserIds | Yes | The alert contacts. Specify the alert contacts in the JSON array format. |
| --notifyType | Yes | The notification method. Specify the notification method in the JSON array format. Valid values: ASO ANS DING _ ANS EMAIL _ ANS SMS _ |
| -u | Yes | The user ID. |

**Examples**

**rule-update -n testRuleNew --deptId 20 --monitorId PROTECT_STATE -o = -v**

**PROTECT_FAIL -d Alert description -l 2 --notifyUserIds [\"testUser\"] --notifyType**

**[\"ANS_EMAIL\"] -r 76df66ad-ecdb-4b35-ac50-931e886 -u 123456789**

#### 8.12.5 rule-delete

You can use the rule-delete command to delete an alert rule.

**Syntax**

**rule-delete [-r] string [-u] string**

**Parameters**

| Parameter | Required | Description |
|---|---|---|
| -r | Yes | The ID of the alert rule. |
| -u | Yes | The user ID. |

**Examples**

**rule-delete -r 9c8bdc83-3a32-4ae0--e8b7b1c31124 -u 123456789**

### 8.13 Monitored metrics

#### 8.13.1 monitor-item-query

You can use the monitor-item-query command to query the monitored metrics.

**Syntax**

**Examples**

x

## 9 Appendix

### 9.1 Look up the Internet domain and intranet domain names

**and intranet domain names**

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the **Projects** page, enter `baseServiceAll` in the search box and click **Cluster Details** in
the **Actions** column.
5. On the **Cluster Details** page, click the **Desired State Configuration** tab.
6. Select the **kv.conf** file and click **Show Content**.
7. Obtain the Internet domain and intranet domain names from the **kv.conf** file.

### 9.2 Look up the DNS address

This topic describes how to look up the Domain Name System (DNS) address.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. Enter dnsProduct in the search box and find the cluster in the **Products** list. Click **Cluster**
**Details** in the **Actions** column.
x
5. Click the **Desired State Configuration** tab and select the

```
 services/dnsService/user/dns.conf  file.
```

6. Click **Show Content**. The value of the AnycastVip field is the IP address of the DNS name
server, which is the same as the ServerIP value shown on the DNS management interface.

> **Note:** The first two IP addresses in the internetIps field are the source IPs used by the DNS service to forward requests. In most cases, two IPs are bound to the bindServerRole containers.

### 9.3 Configure DNS forwarding

When you set up a primary-secondary disaster recovery system between two clouds, you must configure Domain Name System (DNS) at the primary and secondary sites. Make sure that DNS queries can be smoothly forwarded across the system. This topic describes how to configure DNS forwarding.

**Important**

To configure DNS forwarding from opsDns to dnsProduct at the primary site, you must modify the tianji configuration file and roll update the tianji cluster. The risk of automated configuration is high. We recommend that you manually perform the configuration modification and roll update. Automate the configuration of other settings.

**Prerequisites**

A network connection is established between the primary and secondary sites. x The primary site is successfully deployed and the DNS configuration file is generated in the container.

> **Note:** If the prerequisites are not met, see the "Manually configure DNS forwarding" section in this topic.

**Automate configuration of DNS forwarding at the two sites**

1. Obtain the AccessKey ID (AK) and AccessKey secret (SK) and pop_ops_vip of the operations
administrator at the primary site. i. Log on to the Apsara Uni-manager Operations Console as an operations administrator. ii. Click in the upper-right corner of the page and then click **Personal information**. iii. Obtain the AK and SK of the operations administrator. iv. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
v. On the **Product & Cluster O&M** page, enter webappAll in the search box to find the StandardCloudCluster cluster. vi. Click **Cluster Details** in the **Actions** column of the StandardCloudCluster cluster. On the cluster details page, click **Resource Details**. x vii. View the pop-vip-ops resource details and click the value in the Resource Application Result column to obtain and save the value of vip_ip.

> **Note:** If the pop-vip-ops of the primary site changes, you must roll update the asrdr cluster of the primary site again.

Run the following command in the ASR-DR container of the secondary site: Replace pop_vip_ops, ops_admin_ak, ops_admin_sk with the values obtained in the preceding steps. The DNS forwarding rules and IP address whitelists from the primary site to the secondary site are configured, and the DNS forwarding rules and IP address whitelists from the secondary site to the primary site are configured.

```
python alidata/bin/dns/auto_config_dns.py asrdr -v {pop_vip_ops} -a {ops_admin_ak} -s {ops_admin_sk}
```

viii. Obtain the content of the /home/admin/asrdr/config/dns/dns_conf.{regionId}.ops file of the local ASR-DR container.
2. Add a forwarding rule from OPS-DNS to DNS of the local cloud tenant.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. On the **Product & Cluster O&M** page, enter tianji in the search box to search for the tianji cluster. iv. Click **Cluster Details** in the **Actions** column of the cluster. On the cluster details page, click **Desired State Configuration**. x v. Enter dns_zone.conf.jj2 in the search box on the left and click Show Content to add the dns_conf.{regionId}.ops content obtained in Step 1 to the file. Content format:

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
i. Log on to the Apsara Uni-manager Operations console, choose **Security Management >**
**Network Security > Network Security Management Center**.
ii. In the left-side navigation pane, choose **East-west Security Management > DNS Rules**. iii. Log on to the Apsara Uni-manager Management console and choose **Products >**

**Networking > Cloud Network > Alibaba Cloud DNS**

x iv. On the **DNS within Cloud** page, click the **Global Forwarding Configurations** tab. v. The tianji cluster is rolled and the dns_zone.conf.jj2 file is fixed.

**Manually configure DNS forwarding**

1. Copy the DNS configuration file named dns_conf.{des_region} in the
/home/admin/asrdr/config/dns/ directory at the primary site to the /home/admin/asrdr/config/dns/ directory on the ASR-DR container at the secondary site. (If ASR-DR is not deployed at the primary site, place the configuration file in the specified directory based on the predefined format and naming convention.)
2. Run the following command in the ASR-DR container of the secondary site:

```bash
python /alidata/bin/dns/auto_config_dns.py manual -r des_region
# The des_region parameter specifies the destination region.
```

The operation is performed in the ASR-DR container of the secondary site. Only the DNS forwarding rules and IP address whitelists from the secondary site to the primary site are configured.
3. Obtain the content in the /home/admin/asrdr/config/dns/dns_conf.{regionId}.ops file of the
local ASR-DR.
4. Repeat the preceding steps in the ASR-DR container of the primary site.
5. Add a forwarding rule from OPS-DNS to DNS of the local cloud tenant.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. On the **Product & Cluster O&M** page, enter tianji in the search box to search for the tianji cluster. iv. Click **Cluster Details** in the **Actions** column of the cluster. On the cluster details page, click **Desired State Configuration**. x v. Enter dns_zone.conf.jj2 in the search box on the left and click **Show Content** to add the dns_conf.{regionId}.ops content obtained in Step 3 to the file. Content format:

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
6. Check the execution result.
i. Log on to the Apsara Uni-manager Operations console, choose **Security Management >**
**Network Security > Network Security Management Center**.
ii. In the left-side navigation pane, choose **East-west Security Management > DNS Rules**. iii. Log on to the Apsara Uni-manager Management console and choose **Products >**
**Networking > Cloud Network > Alibaba Cloud DNS**.
x iv. On the **DNS within Cloud** page, click the **Global Forwarding Configuration** tab. v. The tianji cluster is rolled and the dns_zone.conf.jj2 file is fixed.

### 9.4 Configure DTS parameters

If you configure a primary/secondary disaster recovery solution between two clouds, you must configure Data Transmission Service (DTS) for database products. This topic describes how to configure DTS.

**Prerequisites**

A network connection is established between the primary and secondary sites. ASR for Geo-disaster Recovery (ASR-DR) is deployed at the primary site and a DTS SQL template file is generated in the container.

**Note**

If the prerequisites are not met, manually configure local DTS.

**Automatically configure local DTS**

1. Obtain the AccessKey ID (AK) and AccessKey secret (SK) and pop_ops_vip of the operations
administrator at the primary site. i. Log on to the Apsara Uni-manager Operations Console as an operations administrator. ii. Click in the upper-right corner of the page and then click **Personal Information**. iii. Obtain the AK and SK of the operations administrator. iv. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
v. On the **Product & Cluster O&M** page, enter webappAll in the search box to find the StandardCloudCluster cluster. x vi. Click **Cluster Details** in the **Actions** column of the StandardCloudCluster cluster. On the cluster details page, click **Resource Details**. vii. View the ops resource details, click the value in the Resource Application Result column, and then save the value of vip_ip.
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

x

```
select * from region_list where REGIONS like '%Region ID%'\G select * from dts_region_info where region = 'Region ID'\G
```

**Manually configure local DTS**

> **Note:** If the ASR-DR container at the secondary site cannot access the VIP for asrdr-backend-ops applied for by the asrdr-backend at the primary site, we recommend that you manually configure local DTS.

x
1. Copy the DTS SQL template /home/admin/asrdr/config/dts/dts_conf.{des_region} from the
asrdr container at the primary site to the /home/admin/asrdr/config/dts/ directory in the asrdr container at the secondary site.
2. Run the following command in the ASR-DR container of the secondary site:

```bash
python alidata/bin/dts/dts_new/auto_config_dts.py manual -r {des_region}
# The des_region parameter specifies the destination region.
```

When the script is executed, {current_region} is automatically replaced. During the execution, the SQL statements that are executed are returned.
3. Run the following commands in the DTS database at the secondary side to view information
about the DTS database:

```
select * from region_pattern where pattern_expression = '^Region ID'\G select * from config where config_code = 'cross_cloud_internet_check_flag'; select * from region_list where REGIONS like '%Region ID%'\G
```

x

```
select * from dts_region_info where region = 'Region ID'\G
```

### 9.5 Configure dedicated lines

When you deploy ASR for Geo-disaster Recovery, you must configure dedicated lines. Otherwise, no data is available on the line chart on the homepage. To configure dedicated lines, perform the following steps: x
1. Download the scriptsto your computer and decompress the scripts
2. Execute the sudo sgvpn con -e 128E -f command to connect to the VPN. For information about
the connection procedure, see sgvpn documentation.

**Note**

If you directly import the data to the environment, no VPN connection is required.
3. Configure nrm_domain
i. Go to the Xterm > Environment Metadata Query section, select the destination environment, and then enter baseService-network-base in the service search box to query the value. ii. Replace the placeholder in the domain.py file with the nrm_domain value obtained in the preceding step. x
4. Import the DCI and interconnect dedicated line data.

> **Note:** Import DCI dedicated line data to the Connections/DCInterConnections.json file in the JSON format. Import interconnection dedicated line data to the Connections/ExternalConnections.json file in the JSON format.
> DCI and interconnection data can be in object or array format.

For information about the parameters, see AddDCInterConnection and AddExternalConnection. x
5. Execute the python importConnections2db.py script.
x

#### 9.5.1 AddDCInterConnection

**Description**

Creates a data center interconnection (DCI) dedicated line.

**URL**

http://{nrm_endpoint}/nbs/api/AddDCInterConnection

**Request method**

GET/POST

**Product**

Nbs

**Version**

2021-02-19

**Request parameters**

| Parameter | Type | Required | Example | Description | Remarks |
|---|---|---|---|---|---|
| Name | str | Yes | test | The name of the DCI dedicated line. |   |
| ConnectTyp e | str | Yes | InterDo main | The type of the DCI dedicated line. | InterDomain: inter- region dedicated line IntraDomain: intra- region dedicated line |
| Region | str | Yes | cn- qingdao -env66- d01 | The region in which the DCI dedicated line access device is located. |   |

x

| Idc | str | Yes | amtest1 1 | The data center in which the access device of the DCI dedicated line is located. |   |
|---|---|---|---|---|---|
| LineOperato r | str | No | test | The operator of the DCI dedicated line. |   |
| AccessDevic eId | str | Yes | ASW-A3- 5- H09.AM TEST66 | The border network device that is used to access the DCI dedicated line. |   |
| PhysicalPort | str | Yes | Port-01 | The physical port used for DCI dedicated line access. |   |
| PortType | str | Yes | test | The type of the physical port. | A manual input is required. |
| Bandwidth | Int | No | 10000 | The access bandwidth. Unit: M |   |
| ConnectMod e | str | Yes | DirectCo nnect | The interconnection type on both sides of the dedicated line. | DirectConnect: direct connection Firewall: connection through a firewall |
| FwMode | str | No | CloudFir ewall | The type of the firewall. | If a connection through a firewall is specified, specify the firewall type based on your business requirements. CloudFirewall UserFirewall Other |
| FwName | str | No | test | The name of the firewall. | If a connection through a firewall is specified, specify the firewall name based on your business requirements. |

x

| FwDesc | str | No | test | The remarks for the firewall. | If a connection through a firewall is specified, specify the remarks for the firewall based on your business requirements. |
|---|---|---|---|---|---|
| PeerRegion | str | No | cn- qingdao -env- d02 | The peer region. | If you set the ConnectType parameter to InterDomain, you must specify the peer region. |
| PeerIdc | str | No | amtest6 6 | The peer data center. | If you set the ConnectType parameter to InterDomain, you must specify the peer data center. |
| PeerAccess DeviceId | str | Yes | CSW- VM-VPC- G1- 1.AMTES T66 | The peer device. |   |
| PeerPhysica lPort | str | Yes | port 02 _ | The physical port of the peer device. |   |
| PeerPortTyp e | str | Yes | test | The type of the physical port on the peer device. |   |
| LocalIp | str | Yes | 192.168 .1.1/30 | The local IP address. | The route mode in the IP address/mask format. Example: 1.1.X.X/30. |
| PeerIp | str | Yes | 192.168 .1.2/30 | The peer IP address. | The route mode in the IP address/mask format. Example: 1.1.X.X/30. |
| ConnectStat us | int | Yes | 1 | Specifies whether to enable the DCI dedicated line. | 1: enables the DCI dedicated line. 0: disables the DCI dedicated line. |
| Description | str | No | xxxxxxx | Remarks | Records non-standard information. |

**Response parameters**

x

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E1******** | The request ID. |
| Success | bool | true/false | Indicates whether the request was successful. |
| Code | str | 0 | The custom response status code. |
| Message | str | success | The message. |

**Examples**

**Sample requests**

> http://127.0.0.1:5050/nbs/api/AddDCInterConnection?
> Name=LIGANG_03&ConnectType=LocalCity&Region=cn-qingdao-env66-
> d01&Idc=amtest11&LineOperator=china&AccessDeviceId=ASW-A3-5-H09.AMTEST66&PhysicalPort=Port-
> 04&PortType=unkown&Bandwidth=10000&ConnectMode=Firewall&FwMode=CloudFirewall&FwName=firewall-
> 01&FwDesc=test for firewall&PeerIdc=amtest66&PeerAccessDeviceId=CSW-VM-VPC-G1-

1.AMTEST66&PeerPhysicalPort=Port-

> 002&PeerPortType=unkown&LocalIp=1.1.X.X/30&PeerIp=192.168.1.2/30&ConnectStatus=1&Description=just
> for test!!!&PeerRegion=cn-qingdao-env-d02

**Sample success responses**

> {
> "Code": "0",
> "Message": "success",
> "RequestId": "bc56d938-e1b7-412c-a665-ba9a6f4a3ef5",
> "Success": true
> }

**No data/operation failed**

> {
> "Message": "no data/update/delete",
> "Code": "4002",
> "RequestId": "d006a01a-3d87-4971-a3fc-bb4cb2823799",
> "Success": true
> }

**Exceptions**

40x,50x x

> {
> "Code": "InternalError",
> "Message": "The request processing has failed: [Errno 32] Broken pipe",
> "RequestId": "2554a594-41a2-4346-93ac-5ac179f8b70f",
> "Success": false,
> "cost": 1,
> "eagleEyeTraceId": "2554a594-41a2-4346-93ac-5ac179f8b70f",
> "errCode": "ASO_NETWORK_INTERNALERROR",
> "errMessage": "An exception occurs. Check the backend service.",
> "errTitle": "An exception occurs.",
> "requestURI": "/slalink/fulllink/classic/idcinfo/IDCList",
> "responseVersion": "v1",
> "serviceRole": "baseServiceAll.baseService-network-base.nrm#",
> "success": false
> }

**Note**

The Success field in the response indicates whether the request was successful. Even if the Success field is true, you must check whether the Data field is an empty list or an array ([]). You can check the Code field to determine whether to render data. If the value of the Code field is "0," the data list is returned with data. If the value of the Code field is not "0," the data list is empty and the Data field does not exist. POP does not support downloading files by using an API. To export or download a file, you must directly access the API URL.

**Error codes**

| HttpCode | Error code | Error message |
|---|---|---|
| 40x | ParameterError | Invalid parameter format. |
| 40x | MissingParameter | One or more required parameters are not specified. |
| 500 | InternalError | An internal processing error occurs. |
| 400 | UniqueError | A unique constraint is violated. |
| 400 | DBError | A data read/write error occurs. |
| 400 | Existing | The data already exists. |
| 400 | NotExisting | The data does not exist. |

#### 9.5.2 AddExternalConnection

x

**Description**

Creates an interconnection dedicated line.

**URL**

http://{nrm_endpoint}/nbs/api/AddDCInterConnection

**Request method**

GET/POST

**Product**

Nbs

**Version**

2021-02-19

**Request parameters**

| Parameter | Type | Re qui red | Example | Description | Remarks | ASR for Geo-disaster Recovery-specific description |
|---|---|---|---|---|---|---|
| Name | str | Yes | test | The name of the interconnecti on dedicated line. |   | You can specify a name based on your business requirements. |
| ConnectT ype | str | Yes | toInternet | The interconnecti on type. | toIdc toInternet | resilience (default) |
| Region | str | Yes | cn- qingdao- env66-d01 | The region in which the dedicated line access device is located. |   | The region ID of the secondary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| Idc | str | Yes | amtest11 | The data center in which the dedicated line access device is located. |   | The information of the secondary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| LineOpera tor | str | No | test | The operator of the dedicated line. |   | The parameter can be left empty. |

x

| AccessDe viceId | str | Yes | ASW-A3-5- H09.AMTES T66 | The border network device that is used to access the dedicated line. |   | The border network device of the secondary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
|---|---|---|---|---|---|---|
| PhysicalP ort | str | Yes | Port-01 | The physical interface used for the dedicated line. |   | The physical interface of the secondary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| PortType | str | No | test | The physical interface type. | A manual input is required. | This parameter can be left empty. |
| Bandwidt h | Int | No | 10000 | The access bandwidth. Unit: M |   | This parameter can be left empty. |
| ConnectM ode | str | Yes | DirectConn ect | The interconnecti on type on both sides of the dedicated line. | DirectConnect : direction connection Firewall: connection through a firewall | Default: DirectConnect |
| FwMode | str | No | CloudFirew all | The firewall type. | If a connection through a firewall is specified, specify the firewall type based on your business requirements. CloudFirewall UserFirewall Other | This parameter can be left empty. |

x

| FwName | str | No | test | The name of the firewall. | If a connection through a firewall is specified, specify the firewall name based on your business requirements. | This parameter can be left empty. |
|---|---|---|---|---|---|---|
| FwDesc | str | No | test | The remarks for the firewall. | If a connection through a firewall is specified, specify the remarks for the firewall based on your business requirements. | This parameter can be left empty. |
| PeerRegio n | str | No | cn- qingdao- env-d02 | The peer region. | If you set the ConnectType parameter to InterDomain, you must specify the peer region. | The region ID of the primary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| PeerIdc | str | No | amtest66 | The peer data center. | If you set the ConnectType parameter to InterDomain, you must specify the peer data center. | The ID of the primary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| PeerAcces sDeviceId | str | Yes | CSW-VM- VPC-G1- 1.AMTEST6 6 | The peer device. |   | The name of the primary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |
| PeerPhysi calPort | str | Yes | port 02 _ | The physical port of the peer device. |   | The physical port of the primary data center. If a single data center is used, the information of the primary and secondary data centers is the same. |

x

| PeerPortT ype | str | No | test | The type of the physical port on the peer device. |   | This parameter can be left empty. |
|---|---|---|---|---|---|---|
| LocalIp | str | No | 192.168.1. 1/30 | The local IP address. | The route mode in the IP address/mask format. Example: 1.1.X.X/30. | Make sure that the format is correct. |
| PeerIp | str | No | 192.168.2. 2/30 | The peer IP address. | The route mode in the IP address/mask format. Example: 1.1.X.X/30. | Make sure that the format is correct. |
| ConnectSt atus | int | Yes | 1 | Specifies whether to enable the dedicated line. | 1: enables the dedicated line. 0: disables the dedicated line. | Default: 1 |
| Descriptio n | str | No | xxxxxxx | Remarks | Records non- standard information. | This parameter can be left empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11E****** | The request ID |
| Success | bool | true/false | Indicates whether the request was successful. |
| Code | str | 0 | The custom response status code. |
| Message | str | success | The message. |

**Examples**

**Sample requests**

x

```
 http://127.0.0.1:5050/nbs/api/AddExternalConnection?
Name=LIGANG_01&ConnectType=toInternet&Region=cn-qingdao-envd01&Idc=amtest11&LineOperator=china&AccessDeviceId=ASW-A3-4-H09.AMTEST66&PhysicalPort=Port- 01&PortType=unkown&Bandwidth=10000&ConnectMode=Firewall&FwMode=CloudFirewall&FwName=firewall- 01&FwDesc=test for firewall&PeerAccessDeviceId=HSW-02&PeerPhysicalPort=Port- 002&PeerPortType=unkown&LocalIp=1.1.X.X/30&ConnectStatus=1&Description=just for test !!!
```

**Sample success responses**

`{`

```json
  "Code": "0",
  "Message": "success",
  "RequestId": "bc56d938-e1b7-412c-a665-ba9a6*******",
  "Success": true
```

`}`

**No data/operation failed**

`{`

```json
  "Message": "no data/update/delete",
  "Code": "4002",
  "RequestId": "d006a01a-3d87-4971-a3fc-bb4cb2******",
  "Success": true
```

`}`
**Abnormal responses**40x, 50x
`{`

```json
  "Code": "InternalError",
  "Message": "The request processing has failed: [Errno 32] Broken pipe",
  "RequestId": "2554a594-41a2-4346-93ac-5ac17******",
  "Success": false,
  "cost": 1,
  "eagleEyeTraceId": "2554a594-41a2-4346-93ac-5ac179f******",
  "errCode": "ASO_NETWORK_INTERNALERROR",
 "errMessage": "An exception occurs. Check the backend service.",
 "errTitle": "An exception occurs.",
  "requestURI": "/slalink/fulllink/classic/idcinfo/IDCList",
  "responseVersion": "v1",
  "serviceRole": "baseServiceAll.baseService-network-base.nrm#",
  "success": false
```

`}` x

**Note**

The Success field in the response indicates whether the request was successful. Even if the Success field is true, you must check whether the Data field is an empty list or an array ([]). You can check the Code field to determine whether to render data. If the value of the Code field is "0," the data list is returned with data. If the value of the Code field is not "0," the data list is empty and the Data field does not exist. POP does not support download. To export or download an object, you must directly access the API URL.

**Error codes**

| HttpCode | Error code | Error message |
|---|---|---|
| 40x | ParameterError | Invalid parameter format. |
| 40x | MissingParameter | One or more required parameters are not specified. |
| 500 | InternalError | An internal processing error occurs. |
| 400 | UniqueError | A unique constraint is violated. |
| 400 | DBError | A data read/write error occurs. |
| 400 | Existing | A data read/write error occurs. |
| 400 | NotExisting | The data already exists. |
