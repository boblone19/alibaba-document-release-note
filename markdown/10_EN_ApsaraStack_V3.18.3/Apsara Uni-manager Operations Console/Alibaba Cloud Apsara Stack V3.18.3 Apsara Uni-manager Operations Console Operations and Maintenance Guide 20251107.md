---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Operations and Maintenance Guide 20251107"
product_version: "V3.18.3"
doc_version: "20251107"
pdf_pages: 32
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Operations and Maintenance Guide 20251107.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Uni-manager%20Operations%20Console%20Operations%20and%20Maintenance%20Guide%2020251107.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Uni-manager Operations Console Operations and Maintenance Guide 20251107

## Table of Contents

- 1 Overview
- 2 Architecture
  - 2.1 System architecture
  - 2.2 Deployment architecture
  - 2.3 Component architecture
  - 2.4 Server roles
- 3 Alert management
- 4 Security maintenance
  - 4.1 Account and password maintenance
  - 4.2 Log audit
- 5 Troubleshooting
  - 5.1 Establish emergency response mechanisms
  - 5.2 Designate owners for handling various issues
  - 5.3 Troubleshooting
  - 5.4 Troubleshooting
    - 5.4.1 The domain name of the Apsara Uni-manager Operations Console cannot be accessed after deployment
    - 5.4.2 No alert data found in the Apsara Uni-manager Operations Console
    - 5.4.3 A user fails to log on to the Apsara Uni-manager Operations Console because the account is revoked
    - 5.4.4 A user fails to log on to the SRE Technical Assurance Platform and error 403 is returned
- 6 High-risk operations
- 7 Appendixes
  - 7.1 Common maintenance commands
  - 7.2 Common HTTP status codes
  - 7.3 Clear historical alerts

## 1 Overview

This topic describes the purposes, requirements, precautions, and technical support for the Apsara Uni-manager Operations Console.

**Purposes**

This guide helps O&M personnel perform preventative maintenance on the Apsara Unimanager Operations Console to make sure that it can stably run for a very long period. O&M personnel can follow the instructions in this guide to handle the system issues that are identified during maintenance. If O&M personnel encounter system issues that are not covered in this guide, they can contact Apsara Stack engineers for technical support.

**Requirements**

O&M personnel must acquire IT skills, including knowledge for computer networks, knowledge for computer operations, issue analysis, and troubleshooting. In addition, O&M personnel must pass the pre-job training and learn the knowledge for the Apsara Stack system. The required knowledge for the system includes but is not limited to system principles, networking, features, and the usage of maintenance tools.

> **Important:** Take note that O&M personnel must comply with operation procedures during maintenance to ensure personal safety and system security. User data must be kept strictly confidential and must not be copied or disseminated without the written consent from users.

**Precautions**

To ensure a stable system and avoid unexpected events, you must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of the O&M personnel. This prevents system faults that are caused by unauthorized operations. System security: Before you perform system operations, you must be aware of their impacts. You must clearly record the details about the issues that you encounter during the operations. This helps you troubleshoot and handle the issues. Personal safety and data security You must take safety measures to ensure personal safety based on device manuals when you use electrical equipment. You must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

You can contact Alibaba Cloud technical support for help.

## 2 Architecture

### 2.1 System architecture

The Apsara Uni-manager Operations Console provides unified O&M capabilities for Apsara Stack products. The Apsara Uni-manager Operations Console comprises the following modules: Console: The user interface layer. This module provides an interactive user interface. Rest API: The console and system capabilities modules interact with each other by using the Rest API module. System capabilities: Resource management: allows you to view and manage Apsara Stack resources in product, network, and data center dimensions. Unified alerting: provides a unified alert export and alert outbound configuration capabilities for Apsara Stack platforms. O&M capabilities: provides vertical O&M capabilities such as network, cloud products, storage, and tasks, as well as horizontal security O&M capabilities. System management: Provides system administration capabilities such as security policies, offline backup, log clearing, system configuration, and personal configuration. Inventory management: allows you to view product inventories and provides usage threshold alerting capabilities for various products. The Apsara Uni-manager Operations Console also provides APIs for secondary development by third parties. You can select optional remote O&M capabilities. The following figure shows the system architecture of the Apsara Uni-manager Operations Console. Figure 2. System architecture of the Apsara Uni-manager Operations Console

### 2.2 Deployment architecture

This topic describes how components are deployed in the Apsara Uni-manager Operations console. The following table describes the deployment of components in the Apsara Uni-manager Operations Console.

| Component | Deployment |
|---|---|
| aso-console.console | Cluster deployment. console uses the two-node method. |
| aso-mgr.asmgr | Cluster deployment. asmgr uses the two-node method. |
| aso-opr.asopr | Cluster deployment. asopr uses the two-node method. |
| aso-monitor.monitor | Cluster deployment. monitor uses the two-node method. You can change to the single-node or multi-node method based on business needs. |
| aso-monitor.tpcmon | Cluster deployment. tpcmon uses the single-node method. |
| aso-slalink.diagnosis-api | Cluster deployment. diagnosis- api uses the single-node method. |
| aso-slalink.full link _ | Cluster deployment. full link _ uses the two-node method. |
| aso-slalink.link mapping _ | Cluster deployment. link mapping uses the single- _ node method. |
| aso-slalink.noc | Cluster deployment. noc uses the two-node method. |
| aso-slalink.noc agent _ | Cluster deployment. noc agent _ uses the two-node method. |
| aso-slalink.sla-portal | Cluster deployment. sla-portal uses the two-node method. |
| aso-slalink.sla-thesla | Cluster deployment. sla-portal uses the three-node method. |
| aso-slalink.sla-topo | Cluster deployment. sla-topo uses the two-node method. |
| aso-slalink.sla-topo-dumpper | Cluster deployment. sla-topo- dumpper uses the two-node method. |
| aso-slalink.sla-topo-graphdb | Cluster deployment. sla-topo- graphdb uses the single-node method. |
| aso-slalink.pgmon | Cluster deployment. pgmon uses the single-node method. |
| aso-standalone.standalone | Cluster deployment. standalone uses the two-node method. |

| aso-emergency.stm | Cluster deployment. stm uses the two-node method. |
|---|---|
| aso-stm.incident | Cluster deployment. incident uses the two-node method. |

### 2.3 Component architecture

This topic describes the components of the Apsara Uni-manager Operations Console and their features. The following figure shows the component architecture of the Apsara Uni-manager Operations Console. Figure 1. Component architecture of the Apsara Uni-manager Operations Console The following table describes the features of the components in the Apsara Uni-manager Operations Console.

| Component | Description |
|---|---|
| aso-console.console | The frontend pages of the Apsara Uni-manager Operations Console, used for data display and analysis |

| aso-mgr.asmgr | For managing users, organizations, menus, permissions, inventories, physical platforms, product O&M |
|---|---|
| aso-opr.asopr | For managing physical server passwords, physical server channels, and tasks |
| aso-monitor.monitor | For viewing, importing, and exporting alert monitoring data and alert templates |
| aso-monitor.tpcmon | For executing the monitoring script of tpcmon |
| aso-slalink.diagnosis-api | The gateway of the slalink module, used for distributing requests to slalink subordinate modules |
| aso-slalink.pgmon | For Storage Operations Center |
| aso-slalink.full link _ | The API module for end-to-end monitoring |
| aso-slalink.link mapping _ | For collecting metadata from ECS, RDS, SLB, and VPC in end-to-end monitoring |
| aso-slalink.noc | For automated task orchestration in Network Operations Center |
| aso-slalink.noc agent _ | For network data collection in Network Operations Center |
| aso-slalink.sla-portal | The portal console for SLA and end-to-end diagnostics, used for interaction with the SLA and end-to-end diagnostics modules |
| aso-slalink.sla-thesla | For processing SLA data and querying API data, analyzing time series data, and electing high availability clients |
| aso-slalink.sla-topo | For processing end-to-end diagnostic data and querying API data |
| aso-slalink.sla-topo-dumpper | For collecting end-to-end diagnostic and SLA data |
| aso-slalink.sla-topo-graphdb | For storing data for graph databases on the end- to-end diagnostic server |

| aso-standalone.standalone | For standalone output of the installation package for Apsara Uni-manager Operations Console |
|---|---|
| aso-emergency.stm | For discovering STM events |
| aso-emergency.incident | For managing STM events |

### 2.4 Server roles

This topic describes projects, clusters, services, and server roles in the Apsara Uni-manager Operations Console to facilitate O&M personnel to identify and discover issues. This following table describes projects, clusters, services, and server roles in the Apsara Unimanager Operations Console.

| project | Cluster | Service | Server role | Description |
|---|---|---|---|---|
|   |   | aso-console | aso- console.console | The frontend pages of the Apsara Uni- manager Operations Console, used for data display and analysis |
|   |   | aso-monitor | aso- monitor.monitor | For viewing, importing, and exporting alert monitoring data and alert templates |
|   |   |   | aso- monitor.tpcmon | For executing the monitoring script of tpcmon |
|   |   |   | aso- slalink.diagnosis- api | The gateway of the slalink module |
|   |   |   | aso-slalink.noc | For Network Operations Center |
|   |   |   | aso- slalink.noc agent _ | The data collection agent for Network Operations Center |
|   |   |   | aso- slalink.full link _ | The API module for the slalink module |

| aso | asoCluster | aso-slalink |   |   |
|---|---|---|---|---|
|   |   |   | aso- slalink.link mappi _ ng | For listing ECS, RDS, SLB, and VPC instances in the slalink module |
|   |   |   | aso-slalink.sla- portal | The SLA frontend display module |
|   |   |   | aso-slalink.sla- thesla | The SLA backend processing module |
|   |   |   | aso-slalink.sla- topo | The topo backend processing module |
|   |   |   | aso-slalink.sla- topo-dumpper | The data collection agent for topo |
|   |   |   | aso-slalink.sla- topo-graphdb | The storage database for topo |
|   |   |   | aso- slalink.pgmon | For Storage Operations Center |
|   |   | aso-mgr | aso-mgr.asmgr | For managing users, organizations, menus, permissions, inventories, physical platforms, product O&M |
|   |   | aso-opr | aso-opr.asopr | For managing physical server passwords, physical server channels, and tasks |
|   |   | aso-stanalone | aso- standalone.stand alone | For standalone output of the installation package for Apsara Uni- manager Operations Console |
|   |   | aso-emergency | aso- emergency.stm | For discovering STM events |
|   |   |   | aso- emergency.incid ent | For managing STM events |

The following figure shows the call relationship between server roles. Arrows point to the called parties.

## 3 Alert management

In the top navigation bar of the Apsara Uni-manager Operations Console, choose
**Monitor&Alarms > Alarm Overview** to go to the Alarm Management console. In the Alarm
Management console, you can view and handle alerts in the Apsara Uni-manager Operations Console.

## 4 Security maintenance

### 4.1 Account and password maintenance

**maintenance**

This topic describes how to maintain your account and password in the Apsara Uni-manager Operations Console. An account is valid for a specific period of time. You must change the password of your account before the validity period of your account elapses. If you do not change the password as required, the account is locked and cannot be used to log on to the Apsara Uni-manager Operations Console. You can change the password of an account or configure the validity period of an account by performing the following steps: Click the profile image in the upper-right corner of the Apsara Uni-manager Operations Console, and select **Personal information**. On the page that appears, click **Change**
**Password** to change the password of the current account.
In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Security**
**Management** > **Access Control** > **Security Strategy**. On the page that appears,
configure the **ASO account validity period (days)** parameter on the **Account Policy** tab.

### 4.2 Log audit

This topic describes how to audit component logs, log file paths, and log query methods. After you access the container, find the log files listed in the following table to view log details.

| Component | File | Description |
|---|---|---|
| aso-mgr.asmgr | /logs/asomanage- logger/main trace.log _ | The logs and error logs related with asmgr container business |
|   | /logs/asomanage- logger/access trace.log _ | asmgr container access logs |
|   | /logs/asomanage- logger/call trace.log _ | Other service call logs related with asmgr container business |
| aso-monitor.monitor | /logs/asomonitor- logger/main trace.log _ | The logs and error logs related with monitor container business |
|   | /logs/asomonitor- logger/access trace.log _ | monitor container access logs |
|   | /logs/asomonitor- logger/call trace.log _ | Other service call logs related with monitor container business |
| aso-opr.asopr | /logs/asooperator-logger/ main trace.log _ | The logs and error logs related with asopr container business |
|   | /logs/asooperator- logger/access trace.log _ | asopr container access logs |
| 4 | > Document Version: 2025110 |   |

| psara Uni-manager Operations Console |   |   |
|---|---|---|
|   | /logs/asooperator- logger/call trace.log _ | Other service call logs related with asopr container business |

## 5 Troubleshooting

### 5.1 Establish emergency response mechanisms

**mechanisms**

O&M teams must establish emergency response mechanisms, so that services can be recovered in time after errors or security events occur.

### 5.2 Designate owners for handling various issues

**various issues**

When monitoring alerts occur on the Apsara Uni-manager Operations Console, onsite O&M personnel must first troubleshoot the issues based on the alerts. If onsite O&M personnel cannot solve the issues, contact Apsara Stack technical support engineers.

### 5.3 Troubleshooting

This topic describes troubleshooting in the Apsara Uni-manager Operations Console. After a system fault is discovered during routine maintenance, O&M personnel can use the O&M feature and system logs in the Apsara Uni-manager Operations Console to view the detailed information of the fault, analyze the causes, and solve the fault. If the faults cannot be fixed, O&M personnel can collect the related information, such as system information and fault symptoms, and contact Apsara Stack engineers for technical support. This way, O&M personnel can fix the faults based on the instructions of the engineers. After the fault is rectified, verify the solution, review the troubleshooting method, and make improvements.

### 5.4 Troubleshooting

#### 5.4.1 The domain name of the Apsara Uni-manager Operations Console cannot be accessed after deployment

**manager Operations Console cannot be**

**accessed after deployment**

This topic describes how to resolve the issue that the domain name of the Apsara Unimanager Operations Console cannot be accessed after deployment.

**Procedure**

1. In the environment that corresponds to the domain name, run the `kubectl get po -n aso`
command to check whether the pod corresponds to the Apsara Uni-manager Operations Console is in the `Running` or `Completed` . If the pod is in the Running state, perform **Step 2**. If the pod is in the Completed state, contact the technical support of the Apsara Unimanager Operations Console.
2. Log on to the asoconsoleconsole-0 pod and run the `curl '127.0.XX.XX'` command to
check whether requests sent to access the pod are timed out or denied. In the command, 127.0.XX.XX indicates the IP address of the container in the pod. If the results show that requests sent to access the pod are timed out or denied, contact the technical support of the Apsara Uni-manager Operations Console. If requests sent to access the pod are not timed out or denied, contact the technical support of Apsara Infrastructure Management.

#### 5.4.2 No alert data found in the Apsara Uni-manager Operations Console

**manager Operations Console**

The Apsara Uni-manager Operations Console and the Apsara Infrastructure Management portal obtain alert data from TianjiMon. You can log on to the Apsara Infrastructure Management portal and check whether TianjiMon generates alert data.

**Procedure**

Check whether alert data is generated on the Apsara Infrastructure Management portal. If alert data is generated on the Apsara Infrastructure Management portal, contact technical support engineers for the Apsara Uni-manager Operations Console. If no alert data is generated on the Apsara Infrastructure Management portal, contact technical support engineers for TianjiMon.

#### 5.4.3 A user fails to log on to the Apsara Uni-manager Operations Console because the account is revoked

**manager Operations Console because the**

**account is revoked**

This topic describes how to resolve the issue that a user fails to log on to the Apsara Unimanager Operations Console because the account is revoked.

**Procedure**

1. Log on to the aso_auth database.
2. Run the following command to view the status and validity period of the account of the
user:

```
select * from user where name="test";
```

3. Check whether the account status is 1.
If the account status is 1, perform **Step 4**. If the account status is not 1, run the update user set status=1 where name="test"; command to change the account status to 1.
4. Run the following command to change the validity period of the account to a date that is
later than the current day:

```
Update user set validity_date="2019-11-04 15:23:23" where name="test";
```

#### 5.4.4 A user fails to log on to the SRE Technical Assurance Platform and error 403 is returned

**Technical Assurance Platform and error 403**

**is returned**

This topic describes how to resolve the issue that a user fails to log on to the SRE Technical Assurance Platform and error 403 is returned.

**Procedure**

1. Use the security officer account to log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, click **User Authorities**.
3. In the left-side navigation pane, click **Role Management**.
4. On the Roles page, find the role assigned to the account that is used to log on to the SRE
Technical Assurance Platform and click **Edit** in the **Actions** column.
5. In the **Edit Role** dialog box, modify the information, grant the tongque_administrator
permission to the role, and then click **OK**.

## 6 High-risk operations

This topic describes the high-risk operations in the Apsara Uni-manager Operations Console to help you prevent risks that may arise. The operations in the following table are considered high-risk operations in the Apsara Unimanager Operations Console. The high-risk operations may cause great impacts on business stability. If you want to perform a high-risk operation described in the following table, we recommend that you perform it in the maintenance window. In addition, we recommend that you read and understand the impacts of the high-risk operations before you perform the operations.

**High-risk operations**

| Menu path | High-risk operation | Impact | How to recover |
|---|---|---|---|
| Platform Operation - Apsara Infrastruct ure Managem ent | In the left-side navigation pane, choose Resources > Product & Cluster O&M. On the Product & Cluster O&M page, click Component in the Instance Status column and select a component to go to the Component Details page. On the Instances tab of a component, restart the component. | The service process is restarted. | Unrecoverable. |
|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click Machine Management in the upper-right corner and select Restart to restart the machine. | The machine is restarted. Services that run on the machine are interrupted. | Unrecoverable. |
|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click Machine Management in the upper-right corner and select Repair and Clone to repair and clone the machine. | After the repair is complete, the cloning process is triggered. During the process, the machine is shut down and the system on the machine is reinstalled, which may cause data loss on the machine. | Unrecoverable. |

|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click Machine Management in the upper-right corner and select Power Off and Repair to shut down and repair the machine. | During the repair process, the machine is temporarily shut down. The stability of the services that run on the machine is affected if the services are not completely migrated to other machines. | Unrecoverable. |
|---|---|---|---|
|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click the Components tab. On this tab, click Restart in the Actions column to restart a component. | The service process is restarted. | Unrecoverable. |
|   | In the left-side navigation pane, choose Hardware O&M > HDD Repairs. On the Disk Repair page, repair disks. | If you want to replace a disk, you must back up the data on the disk in storage of Apsara Stack such as PANGU. If you perform the repair operations accidentally or by force, your data on the disk may be lost. | Unrecoverable. |
| Platform Operation - O&M Change | In the left-side navigation pane, choose Operation Orchestration Service > O&M Resources > O&M Jobs. On the O&M Jobs page, create an O&M job and run the job. | The script for the job is run on the selected physical machine. The impact of the job varies based on the script content. | Unrecoverable. |
| System Config - Archive managem ent | In the left-side navigation pane, choose Archive management > Archiving Server Settings. On the Archive server configuration page, set the Archive server address and Archive Service listening path parameters to the values that conflict with other server IP addresses and service listening paths. | The files on the host of the related cloud service whose server IP address or service listening path conflicts with the value of the Archive server address or Archive Service listening path parameter may be overwritten. In this case, the cloud service cannot run as expected. | Unrecoverable. |
|   | In the left-side navigation pane, click Computing Cluster O&M. Log on to the AG of a cluster and run commands in the CLI. | The impact of the operation depends on the commands that are run in the CLI. | Unrecoverable. |

| psara Uni-ma onsole |   |   |   |
|---|---|---|---|
| Product Operation - Compute Operation s Console |   |   |   |
|   | In the left-side navigation pane, click Computing Server O&M. On the Computing Server O&M page, create a task for a machine to deactivate and maintain the machine. | When the task is performed, the physical machine is deactivated for maintenance and is then activated after the maintenance is complete. When the machine is deactivated, ECS instances that run on the machine are migrated, which may interrupts the services. | Unrecoverable. |
|   | In the left-side navigation pane, choose ECS Intelligent O&M > ECS O&M Event. On the Proactive O&M page, submit a repair ticket for a local disk. | After the ticket is submitted, the local disk becomes offline for repairing. If you select the wrong disk, data on the disk may be lost. | Unrecoverable. |
|   | In the left-side navigation pane, choose ECS Intelligent O&M > ECS Physical Machine O&M. On the Physical Machine Maintenance page, create a physical machine maintenance task. | When the task is performed, the physical machine is deactivated for maintenance and is then activated after the maintenance is complete. When the physical machine is deactivated, ECS instances that run on the machine are migrated, which may interrupts the services. | Unrecoverable. |
|   | In the left-side navigation pane, click EBS Clusters. On the Service Details tab of the cluster details page, modify the service flag for the BlockServer, BlockMaster, RiverServer, or RiverCluster service node. | The service may become unavailable depending on the modified configuration items. | Change the configuration to the standard configuration. |

|   | In the left-side navigation pane, click EBS Clusters. On the Service Details tab of the cluster details page, restart the BlockServer or RiverCluster service node, or switch to the master node of the BlockServer or RiverCluster service node. | The I/O operations of some disks may be delayed or suspended. Note You can restart abnormal machines or switch to the master node of abnormal machines. For machines in normal states, we recommend that you do not perform the preceding operations on them. | Unrecoverable. |
|---|---|---|---|
| Product Operation - EBS |   |   |   |
|   | In the left-side navigation pane, choose EBS Routine O&M > EBS Proactive O&M. On the EBS Proactive O&M page, select Set the cluster oversold multiple from the Common O&M drop- down list and configure other parameters. Then, perform O&M on the cluster. | Disks cannot be created for the cluster. | Change the value to the standard oversold multiple. |
|   | In the left-side navigation pane, choose EBS Routine O&M > EBS Proactive O&M. On the EBS Proactive O&M page, select Open cluster sale from the Common O&M drop-down list and configure other parameters. Then, perform O&M on the cluster. | If you perform this operation when the cluster resources are oversold, data writing to the cluster may be prohibited. | Disable cluster sale based on your business requirements. |

|   | In the left-side navigation pane, choose EBS Routine O&M > EBS Proactive O&M. On the EBS Proactive O&M page, select Closing of cluster sale from the Common O&M drop-down list and configure other parameters. Then, perform O&M on the cluster. | Disks cannot be created for the cluster. | Enable cluster sale based on your business requirements. |
|---|---|---|---|
| Security Managem ent - Security Complianc e Center - Platform Password Applicatio n Managem ent | In the left-side navigation pane, choose Storage Encryption > Disk Encryption for Metadatabase. On the page that appears, enable database encryption for services. | During data encryption, the read and write operations cannot be performed. Otherwise, service interruptions occur. The duration of a service interruption varies based on the amount of data in the database. | Unrecoverable. |
|   | In the left-side navigation pane, choose Network Transmission Encryption> Transmission Encryption for Metadatabase Access. On the page that appears, enable transmission encryption for applications. | The displayed applications enter the Rolling state. In most cases, services are not interrupted. | Disable transmission encryption. |
|   | In the left-side navigation pane, choose Network Transmission Encryption> Transmission Encryption for Platform Access. On the page that appears, enable transmission encryption for applications. | The displayed applications enter the Rolling state. In most cases, services are not interrupted. | Disable transmission encryption. |
|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > SRS Management. On the SRS management page, change the status in the SRS Security Isolation Status Configuration section of the Configuration Management tab. | If you change the SRS security isolation status, the network security protection policies change. If you set the SRS security isolation status to Enable or Automatic Mode, the network connectivity of the platform may be affected. If you set the SRS security isolation status to Close, network security risks may occur. | Change the SRS security isolation status to the original value. However, your business may be affected when the status is being changed. |

|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > SRS Management. On the SRS management page, add or delete IP address whitelists in the SRS IP Address Whitelist Configuration section of the Configuration Management tab. | If you add IP address whitelists, network security risks may occur. If you delete an IP address whitelist, services in the cloud may fail to be accessed from the IP addresses in the whitelist. | Restore the original whitelist configurations. However, the new configurations take effect in 10 minutes. During the period, your business may still be affected. |
|---|---|---|---|
| Security Managem ent - Network Security - Network Security Managem ent Center |   |   |   |
|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > SRS Management. On the SRS management page, add or delete IP address blacklists in the SRS IP Blacklist Settings section of the Configuration Management tab. | If you add an IP address blacklist, services in the cloud may fail to be accessed from the IP addresses in the blacklist. If you delete IP address blacklists, network security risks may occur. | Restore the original blacklist configurations. However, the new configurations take effect in 10 minutes. During the period, your business may still be affected. |
|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > SRS Management. On the SRS management page, add or delete isolation-free products in the SRS Isolation-free Product Settings section of the Configuration Management tab. | If you add isolation-free products, network security risks may occur. If you delete isolation- free products, the services of the corresponding products cannot be accessed. | Restore the original isolation-free product configurations. However, the new configurations take effect in 10 minutes. During the period, your business may still be affected. |
|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > SRS Management. On the SRS management page, add or delete bypass baselines in the SRS Bypass Baseline Settings section of the Configuration Management tab. | If you add bypass baselines, the services of the corresponding products cannot be accessed. If you delete bypass baselines, network security risks may occur. | Restore the original bypass baseline configurations. However, the new configurations take effect in 10 minutes. During the period, your business may still be affected. |
|   | In the left-side navigation pane, choose East-west Security Management > SRS Management > Isolation Configuration Management. On the Isolation Configuration Management page, add or delete dynamic allow settings. | If you add dynamic allow settings, network security risks may occur. If you delete dynamic allow settings, the services of the corresponding products cannot be accessed. | Restore the original dynamic allow settings. However, the new settings take effect in 10 minutes. During the period, your business may still be affected. |

|   | In the left-side navigation pane, choose East-west Security Management > Donghuangzhong > Donghuangzhong Settings. On the Donghuang clock configuration page, disable host network isolation. | If you disable host network isolation, the ports of all hosts in the PaaS clusters can be accessed from public IP addresses, which may cause network security risks. | Enable host network isolation. |
|---|---|---|---|
|   | In the left-side navigation pane, choose East-west Security Management > Donghuangzhong > Donghuangzhong Settings. On the Donghuang clock configuration page, add CIDR blocks to the whitelist. | If host network isolation is enabled and a CIDR block is added to the whitelist, the ports of all hosts in the PaaS clusters can be accessed from IP addresses in the CIDR block. If the CIDR block is untrusted, network security risks may occur. | Delete untrusted CIDR blocks from the whitelist. |
|   | In the left-side navigation pane, choose East-west Security Management > Donghuangzhong > Donghuangzhong Settings. On the Donghuang clock configuration page, delete CIDR blocks from the whitelist. | If host network isolation is enabled and a CIDR block is deleted from the whitelist, the ports of all hosts in the PaaS clusters cannot be accessed from IP addresses in the CIDR block. In this case, your business is interrupted. | Add the CIDR block to the whitelist. |
|   | In the left-side navigation pane, choose East-west Security Management > Donghuangzhong > Donghuangzhong Settings. On the Donghuang clock configuration page, add ports to allow access to hosts. | If host network isolation is enabled and ports that allow access to hosts are added, the added ports of all hosts in the PaaS clusters can be accessed only from IP addresses or CIDR blocks in the whitelist. If the port that needs to be accessed is not added, your business is interrupted. | Make sure that the CIDR blocks that you trust are included in the whitelist before you modify or add the ports. |

| Security Managem ent - Account Security - Linux Account Managem ent | In the left-side navigation pane, click Password Management for Root. On the page that appears, update passwords on the Password management tab. | The passwords of the accounts for physical machines and kernel-based virtual machines (KVMs) are changed. | Find the original passwords in the password history and restore the passwords to the original passwords. |
|---|---|---|---|
|   | In the left-side navigation pane, click Password Management for Root. On the page that appears, turn off Password tube switch on the Configuration tab. | If you turn off the switch, you cannot update or rotate the passwords of machines in the Apsara Uni-manager Operations Console. If you turn off the switch, the aso-opr container cannot execute jsch commands. In this case, the archive management and log clearing capabilities of the Apsara Uni-manager Operations Console become unavailable. | Turn on Password tube switch to enable password hosting. |
|   | In the left-side navigation pane, click Password Management for Root. On the page that appears, turn on Password rotary switch on the Configuration tab. | The passwords for all machines are rotated at the default interval of 15 days. | Find the original passwords in the password history and restore the passwords to the original passwords. |
|   | In the left-side navigation pane, choose Linux Account Management Task > Task Template Management. On the Task Template Management page, run the GlobalTunnelRemoveTask task. | The initial global password- free tunnels from the OPS machine to all other machines are removed. | Create password-free tunnels from the OPS machine to all other machines again. |

|   | In the left-side navigation pane, choose Linux Account Management Task > Task Template Management. On the Task Template Management page, run the GlobalTunnelRotateTask task. | The default password-free tunnels are rotated. During the rotation, machines that use the non-standard initial keys cannot be connected over SSH in a password- free manner. | Issue the initial keys to the machines after the rotation. |
|---|---|---|---|
| User Authoritie s | In the left-side navigation pane, click User Management. On the User Management page, delete users. | Deleted users are moved to the recycle bin. The AccessKey pairs of the users are disabled. Services or applications that use the AccessKey pairs of the users cannot run as expected. | Restore the users from the recycle bin. After users are restored, the AccessKey pairs of the users are disabled by default. You can enable the AccessKey pairs of the users. |
| Personal informatio n page | In the Accesskey section, disable or delete an AccessKey pair. | Services or applications that use the AccessKey pair to call API operations cannot run as expected. | If you disable an AccessKey pair, you can enable it again. If you delete an AccessKey pair, the AccessKey pair cannot be restored. In this case, replace the deleted AccessKey pair in the code of the services or applications with a new one. |

## 7 Appendixes

### 7.1 Common maintenance commands

**commands**

This topic describes the commands that are commonly used in the maintenance of the Apsara Uni-manager Operations Console.

**Commands used to log on to the environment and containers**

Log on to the environment:

```bash
kubectl get ingress -n aso
```

. Log on to the container:

```bash
kubectl get pod -n aso
```

. Get a shell to the single-container pod:

```bash
kubectl exec -it asoconsoleconsole-0 -n aso /bin/bash
```

**Common commands for K8S in Apsara Stack Agility PaaS**

Log on to the K8S console from a host:

```python
sudo arkshoot
```

View the service status:

```bash
kubectl get po -n ark-system
```

. View the deployed products:

```bash
kubectl get appset -n ark-system
```

. View the configuration of products:

```bash
kubectl get appset -n ark-system aso-0 -oyaml
```

. View the stage, status, and configuration information of service role deployment:

```bash
kubectl get appinstance -n ark-system aso-mgr.asmgr -oyaml
```

. View the workflow status of chart deployment:

```
argo get -n ark-system inst-aso-mgr-asmgr-zkgqr ${Revision}
```

. View the operational logs of a container:

```
argo get -n ark-system aso-mgr.asmgr
```

. View the container on which the Apsara Uni-manager Operations Console is running:

```bash
kubectl get po -n aso
```

. View the startup information about asomgrasmgr-0:

```bash
kubectl logs asomgrasmgr-0 -n aso -c dep-init
```

. View the details of a node:

```bash
kubectl describe pods asdconsoletaskmanager-0 -n asd
```

. View the description of a product:

```bash
kubectl describe po podName -n aso
```

. View the IP address:

```bash
kubectl get pods -n asd -o wide
```

. View all DNS settings in the environment:

```bash
kubectl get ingress -A
```

. View configuration items:

```bash
kubectl get ingress -n asd asdportal-nginx-ingress -o yaml
```

. View environment variables:

```bash
kubectl get cm ark.cmdb.app.asd-console.taskmanager.expose -n ark-system -oyaml
```

. View the ingress address:

```bash
kubectl get ingress -n aso
```

Delete a pod:

```bash
kubectl delete po pod_name -n aso
```

. View the memory information:

```
cat /proc/meminfo
```

.

### 7.2 Common HTTP status codes

This topic describes the common HTTP status codes and their types in the Apsara Unimanager Operations Console.

**HTTP status code types**

HTTP status codes can be divided into five types based on the first digit: 1xx: informational response. The request was received, continuing process. 2xx: successful. The request was received, understood, and accepted. 3xx: redirection. Further action needs to be taken in order to complete the request. 4xx: client error. The request contains bad syntax or cannot be fulfilled. 5xx: server error. The server cannot identify an invalid request.

**Common HTTP status codes**

| HTTP status code | Description |
|---|---|
| 200 | Successful response |
| 404 | Resources not found |
| 400 | Bad request, such as syntax errors |
| 401 | Request authorization failed |
| 402 | Cookie verification failed |
| 403 | Forbidden request |
| 404 | Files, queries, or URLs not found |
| 406 | Account not activated |
| 409 | Resource already exists |
| 418 | Verification code invalid |
| 419 | Service authorization failed |
| 420 | Signature data check failed |
| 421 | Certificate check failed |
| 422 | Random does not exist |
| 423 | SN and account mismatch |
| 424 | Username or ID does not match |
| 425 | Service does not exist |
| 426 | Authentication does not exist |
| 427 | Authentication failed |

| 428 | Request from the Apsara Infrastructure Management failed |
|---|---|
| 500 | Internal errors in the server |
| 501 | Requested function not supported in the server |
| 510 | Database operation errors |

### 7.3 Clear historical alerts

This topic describes how to clear the historical alerts of the Apsara Uni-manager Operation Console.

**Issue**

P1 alerts generated by Apsara Infrastructure Management are automatically synchronized to the alert management system of the Apsara Uni-manager Operation Console. When Apsara Infrastructure Management clears an alert and returns to the normal state, the corresponding alert in Apsara Uni-manager Operation Console may not be cleared within the expected time period.

**Cause**

Alerts generated by Apsara Infrastructure Management are synchronized to the Apsara Unimanager Operation Console on a 30-second basis. However, the Apsara Uni-manager Operation Console clears alerts on a 3-day basis. If Apsara Infrastructure Management clears an alert and returns to the normal state within a short period, the corresponding alert on the Apsara Uni-manager Operation Console may not be cleared in a timely manner.

**Supported versions**

The solution described in this topic is applicable to Apsara Stack V3.14.0 and earlier versions.

**Solution**

1. Log on to a VM and run the following command to obtain the information required to log on
to the aso_platmonitor database:

```
db=aso_platmonitor;clear;curl -s http://127.0.0.1:7070/api/v3/column/service.res.result|awk -F '": "' '{print $2}'|awk -F '"' '/db_password/&&/"'$db'/{v=$44;V=$40;if(length($44)>20){V=$44;v=$16};s="mysql -h"V" -u"$36" -p"$4" -D"v" -P"$12;gsub("\\\\","",s);print s}'
```

2. Log on to the aso_platmonitor database and run the following command to clear alerts
related to the specified metric on the Apsara Uni-manager Operation Console:

```
delete from event where metric_name="Alert Metric";
```

3. Run the following commands to clear all alerts on the Apsara Uni-manager Operation
Console:

```
truncate table event; truncate table history_alert;
```

4. Log on to the Apsara Infrastructure Management Console.
5. In the top navigation bar, choose **Operations** > **Cluster Operations**. On the **Cluster**
**Operations** page, choose **Monitoring** > **Cluster Operation and Maintenance Center**
in the **Actions** column corresponding to the cluster.
6. Select **Monitor#** for **Service Role**, and then click **Restart Server Role** in the **Actions**
column corresponding to the machine.
