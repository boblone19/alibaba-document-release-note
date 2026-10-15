---
title: "Apsara Uni-manager Operations Console Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260703"
pdf_pages: 25
source_pdf: "64c07b90c7d37eab_Alibaba Cloud Apsara Stack V3.18.6 Apsara Uni-manager Operations Console Operations and Maintenance "
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%B8%93%E6%9C%89%E4%BA%91%E8%BF%90%E7%BB%B4%E5%B9%B3%E5%8F%B0ASO/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Apsara%20Uni-manager%20Operations%20Console%20Operations%20and%20Maintenance%20Guide%2020260703.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Apsara Uni-manager Operations Console Operations and Maintenance Guide

## Table of Contents

- 1 Overview
- 2 Architecture
  - 2.1 System architecture
  - 2.2 Component architecture
- 3 Alert handling
- 4 Security maintenance
  - 4.1 Account password maintenance
  - 4.2 Log audit
- 5 Troubleshooting
  - 5.1 Establish a fault response mechanism
  - 5.2 Troubleshooting owners
  - 5.3 Troubleshooting
  - 5.4 Troubleshooting
    - 5.4.1 The domain name cannot be accessed after the Apsara Uni-manager O&M console is deployed.
    - 5.4.2 No alert data is displayed in the Apsara Uni-manager O&M console.
    - 5.4.3 The following message is displayed when you log on to the Apsara Uni-manager O&M console: The user has been removed.
    - 5.4.4 A user fails to log on to the SRE Technical Assurance Platform and error 403 is returned
- 6 High-risk operations
- 7 Appendixes
  - 7.1 Common Maintenance Commands
  - 7.2 Common HTTP status codes

## 1 Overview

This topic describes the purposes, requirements, precautions, and technical support for the Apsara Uni-manager Operations Console.

**Purposes**

This guide helps O&M personnel perform preventative maintenance on the Apsara Unimanager Operations Console to make sure that it can stably run for a very long period. O&M personnel can follow the instructions in this guide to handle the system issues that are identified during maintenance. If O&M personnel encounter system issues that are not covered in this guide, they can contact Apsara Stack engineers for technical support.

**Requirements**

O&M personnel must acquire IT skills, including knowledge for computer networks, knowledge for computer operations, issue analysis, and troubleshooting. In addition, O&M personnel must pass the pre-job training and learn the knowledge for the Apsara Stack system. The required knowledge for the system includes but is not limited to system principles, networking, features, and the usage of maintenance tools.

**Important**

Take note that O&M personnel must comply with operation procedures during maintenance to ensure personal safety and system security. User data must be kept strictly confidential and must not be copied or disseminated without the written consent from users.

**Precautions**

To ensure a stable system and avoid unexpected events, you must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of the O&M personnel. This prevents system faults that are caused by unauthorized operations. System security: Before you perform system operations, you must be aware of their impacts. You must clearly record the details about the issues that you encounter during the operations. This helps you troubleshoot and handle the issues. Personal safety and data security You must take safety measures to ensure personal safety based on device manuals when you use electrical equipment. You must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

You can contact Alibaba Cloud technical support for help.

## 2 Architecture

### 2.1 System architecture

The Apsara Uni-manager Operations Console provides unified O&M capabilities for Apsara Stack products. The following figure shows the system architecture of the Apsara Uni-manager Operations Console. Figure 2. Apsara Uni-manager Operations Console system architecture The Apsara Uni-manager Operations Console comprises the following modules: Console: The user interface layer. This module provides an interactive user interface. Rest API: The console and system capabilities modules interact with each other by using the Rest API module. System capabilities: Resource management: allows you to view and manage Apsara Stack resources in product, network, and data center dimensions. Unified alerting: provides a unified alert export and alert outbound configuration capabilities for Apsara Stack platforms. O&M capabilities: provides vertical O&M capabilities such as network, cloud products, storage, and tasks, as well as horizontal security O&M capabilities. System management: Provides system administration capabilities such as security policies, offline backup, log clearing, system configuration, and personal configuration. Inventory management: allows you to view product inventories and provides usage threshold alerting capabilities for various products. The Apsara Uni-manager Operations Console also provides APIs for secondary development by third parties. You can select optional remote O&M capabilities.

### 2.2 Component architecture

This topic describes the components of the Apsara Uni-manager Operations Console and their features. The following figure shows the component architecture of the Apsara Uni-manager Operations Console. The following table describes the features of the components in the Apsara Uni-manager Operations Console.

| Service | Server role | Overview |
|---|---|---|
| aso-ecsops | DeployInit# | ECS-related backend services in the IaaS console. |
| aso-ecsops | ApiInit# | ECS-related backend services in the IaaS console. |
| aso-ecsops | DbInit# | ECS-related backend services in the IaaS console. |
| aso-ecsops | SlsInit# | ECS-related backend services in the IaaS console. |
| aso-ecsops | DtsInit# | ECS-related backend services in the IaaS console. |
| aso-ecsops | EcsOps# | ECS-related backend services in the IaaS console. |
| aso-ecsops | AuditConfig# | ECS-related backend services in the IaaS console. |

| aso-emergency | Incident# | Features related to O&M alerts and event management. |
|---|---|---|
| aso-emergency | Inspection# | Features related to O&M inspection. |
| aso-emergency | Notify# | The components related to the outgoing alert event. |
| aso-emergency | init# | Initialize related components. |
| aso-mgr | configInit# | Used for DB and other related initialization. |
| aso-mgr | inventoryOpt# | The capacity prediction algorithm module predicts the future usage trend and warning water level of the capacity. |
| aso-mgr | asmgr# | Responsible for logon, user, organization, menu, permission, inventory, physical platform (CMDB), product O&M management, API internal gateway. |
| aso-mgr | audit# | Black-and-white screen operation logs. |
| aso-mgr | bigbang# | related to scale-out. |
| aso-mgr | blueprint# | Blueprint diagnosis related. |
| aso-monitor | Monitor# | Alert notification, tianjimon template maintenance, and forwarding of alert source traffic. |
| aso-monitor | Tpcmon# | Run the monitoring script of tpcmon. |
| aso-opr | asopr# | Manage physical server passwords, physical server channels, and tasks. |
| aso-slalink | pgmon# | For Storage Operations Center |

## 3 Alert handling

In the Apsara Uni-manager Operations console, choose **Monitor&Alert > Alert**
**Management** to view the alert information in the Apsara Uni-manager Operations console.
For more information about how to handle alerts, see Alerts.

## 4 Security maintenance

### 4.1 Account password maintenance

**maintenance**

This topic describes how to maintain accounts and passwords in the Apsara Uni-manager Operations console. The user account has a validity period, and the password needs to be changed within the specified period. Otherwise, the account will be locked and you cannot log on normally. In the upper-right corner of the page, click the profile picture and select **Personal**
**Information**. On the left side of the page, click **Change Password** to change the account
password of the current user. On the **Account Policies** tab of the **Security Management** > **RAM** > **Security Policies** page, set **Validity Period**.

### 4.2 Log audit

This topic describes the audit methods, log file paths, and log query methods for component logs. After entering the container, find the log file in the following table and view the log details.

| Components | File | Description |
|---|---|---|
| aso-mgr.asmgr | /logs/asomanage- logger/main trace.log _ | asmgr container business-related logs and exception logs |
|   | /logs/asomanage- logger/access trace.log _ | asmgr container access logs |
|   | /logs/asomanage- logger/call trace.log _ | The logs of calling other services related to the asmgr container business. |
| aso- monitor.monitor | /logs/asomonitor- logger/main trace.log _ | Monitor container business-related logs and exception logs |
|   | /logs/asomonitor- logger/access trace.log _ | Monitor container access logs |
|   | /logs/asomonitor- logger/call trace.log _ | Monitor container service-related calls to other services |
|   | /logs/asooperator- logger/main trace.log _ | asopr container business-related logs and exception logs |

| psara Uni-manager Console | Operations Operations and Maintenance Gu de·Security maintenanc |   |
|---|---|---|
| aso-opr.asopr |   |   |
|   | /logs/asooperator- logger/access trace.log _ | asopr container access logs |
|   | /logs/asooperator- logger/call trace.log _ | logs of calling other services related to the asopr container business |

## 5 Troubleshooting

### 5.1 Establish a fault response mechanism

**mechanism**

The maintenance team should establish a sound fault emergency response mechanism to ensure that in the event of a fault or security incident, it can quickly locate and efficiently handle it, minimize the business interruption time, and restore the normal operation of the system in a timely manner.

### 5.2 Troubleshooting owners

When monitoring alerts occur on the Apsara Uni-manager Operations Console, onsite O&M personnel must first troubleshoot the issues based on the alerts. If onsite O&M personnel cannot solve the issues, contact Apsara Stack technical support engineers.

### 5.3 Troubleshooting

This topic describes troubleshooting in the Apsara Uni-manager Operations Console. After a system fault is discovered during routine maintenance, O&M personnel can use the O&M feature and system logs in the Apsara Uni-manager Operations Console to view the detailed information of the fault, analyze the causes, and solve the fault. If the faults cannot be fixed, O&M personnel can collect the related information, such as system information and fault symptoms, and contact Apsara Stack engineers for technical support. This way, O&M personnel can fix the faults based on the instructions of the engineers. After the fault is rectified, verify the solution, review the troubleshooting method, and make improvements.

### 5.4 Troubleshooting

#### 5.4.1 The domain name cannot be accessed after the Apsara Uni-manager O&M console is deployed.

**after the Apsara Uni-manager O&M console is**

**deployed.**

This topic describes how to troubleshoot the problem that a domain name cannot be accessed after the Apsara Uni-manager Operations Console is deployed.

**Procedure**

1. Run the following command to check whether the pods in the Apsara Uni-manager
Operations Console are running as expected in the environment corresponding to the domain name: `Running` or `Completed` .

```bash
 kubectl get po -n aso
```

Yes: Perform **Step 2**. If no, contact the back-end technical support engineers of Apsara Uni-manager Operations Console.
2. Log on to the asoconsoleconsole-0 pod and run the following command. The IP address in
the command is the IP address of the container where the pod is located. Check whether the pod is triggered or denied access.

```bash
 curl '127.0.XX.XX'
```

If the results show that requests sent to access the pod are timed out or denied, contact the technical support of the Apsara Uni-manager Operations Console. If requests sent to access the pod are not timed out or denied, contact the technical support of Apsara Infrastructure Management.

#### 5.4.2 No alert data is displayed in the Apsara Uni-manager O&M console.

**Uni-manager O&M console.**

This topic describes how to handle the no-alert data in the Apsara Uni-manager Operations and Maintenance Console. Both the Apsara Uni-manager Operations console and the apsara infrastructure O&M platform portal obtain alert data from TianjiMon. You can check whether tianjiMon generates alert data from the apsara infrastructure O&M platform portal for subsequent processing.

**Procedure**

Check whether alert data exists in the portal of the basic O&M platform of the apsara system. Yes: Contact the technical support engineer of the Apsara Uni-manager Operations Console. No: Contact TianjiMon technical support engineers.

#### 5.4.3 The following message is displayed when you log on to the Apsara Uni-manager O&M console: The user has been removed.

**when you log on to the Apsara Uni-manager**

**O&M console: The user has been removed.**

This topic describes how to troubleshoot an error that indicates that the user has been removed when you log on to the Apsara Uni-manager O&M console.

**Procedure**

1. Log on to the aso_auth database.
2. Run the following command to view the user status and validity period:

```
select * from user where name="test";
```

3. Check whether the user status (statue) is 1.
Yes: Perform **Step 4**. No: update user set statue=1 where name="test"; running the command, change the user status to 1.
4. Run the following command to change the effective time to a date later than the current
day:

```
Update user set validity_date="2026-06-30 15:23:23" where name="test";
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

**List of high-risk operations**

| Menu path | High-risk operation | Impact | How to recover |
|---|---|---|---|
| Platform Operation - Apsara Infrastruct ure Managem ent | In the left-side navigation pane, choose Resources > Product & Cluster O&M. On the Product & Cluster O&M page, click Component in the Instance Status column and select a component to go to the Component Details page. On the Instances tab of a component, restart the component. | The service process is restarted. | Unrecoverable. |
|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click Machine Management in the upper-right corner and select Restart to restart the machine. | The machine is restarted. Services that run on the machine are interrupted. | Unrecoverable. |
|   | In the left-side navigation pane, choose Resources > Machine Management. On the machine details page, click Machine Management in the upper-right corner and select Repair and Clone to repair and clone the machine. | After the repair is complete, the cloning process is triggered. During the process, the machine is shut down and the system on the machine is reinstalled, which may cause data loss on the machine. | Unrecoverable. |
|   | On the Resource Management > Machine Management > Machine Details page, click Machine Operation to Shut Down and Repair. | During the repair process, the machine will experience a shutdown state. If the services running on the machine are not migrated, the service stability may be affected. | Unrecoverable. |

|   | On the Resource Management > Machine Management > Machine Details page, click the Components tab and Restart. | The service process is restarted. | Unrecoverable. |
|---|---|---|---|
|   | In the left-side navigation pane, choose Hardware Maintenance > Hard Disk Maintenance. | If you want to replace a disk, you must back up data from storage-related modules such as Pangu. Forced or misoperation may cause data loss. | Unrecoverable. |
| Platform O&M-O&M services | In the left-side navigation pane, choose Operation Orchestration Service > O&M Jobs. | The script will be executed in the selected physical machine. The influence depends on the script content. | Unrecoverable. |
|   | On the Compute Cluster Operations page, log on to the cluster AG and run the black command. | The influence surface depends on the content of the black screen command. | Unrecoverable. |
| Product O&M- Compute O&M console | On the Compute Server Operations page, create a repair task. | During the operation, the physical opportunity is first offline for maintenance, and then online after the maintenance is completed. ECS instances on the physical machine will be migrated when the physical machine is offline. The migration of ECS instances may have business impacts. | Unrecoverable. |
|   | On the ECS Intelligent Maintenance > ECS O&M Events page, submit a local disk repair order. | After the operation is successful, the corresponding local disk will be taken offline for repair. If the wrong disk is removed, the data of the local disk may be lost. | Unrecoverable. |

|   | On the ECS Intelligent Maintenance > ECS Physical Server Operations page, create a physical server for maintenance. | During the operation, the physical machine is first taken offline for maintenance, and then brought online after the maintenance is completed. When the physical machine is taken offline, the ECS instance on the physical machine will be migrated, and the migration of the ECS instance may have business impacts. | Unrecoverable. |
|---|---|---|---|
|   | On the EBS Cluster Management > Cluster Details page, click the Service Details tab. On the Service Details tab, click Modify Service Flag for the BlockServer, BlockMaster, RiverServer, and RiverCluster service nodes. | Depending on the configuration items of the modification, the service may be unavailable. | Change the configuration to the standard configuration. |
| Product Operation s-Elastic Block Storage Operation s · EBS |   |   |   |
|   | On the EBS Cluster Management > Cluster Details page, click Restart or Master on the Service Details tab. | For a short period of time, the IO of some disks may be affected. A slow IO or IO hang may occur. Note You can only restart /cut machines that are not in the normal state. We recommend that you do not restart /cut machines that are in the normal state. | Unrecoverable. |
|   | On the EBS Common Operations > EBS Active Operations page, perform the following operations on the cluster: Set Oversold Multiples. | This may cause the cluster to fail to create a disk. | Change the value to the standard oversold multiple. |

|   | In the left-side navigation pane, click Common EBS Operations. On the Active EBS Operations page, click Open Cluster for Sale. | If a meeting is held after the cluster is oversold, data writes are disabled. | Disable cluster sales on demand. |
|---|---|---|---|
|   | On the EBS Common Operations > EBS Active Operations page, click Disable Cluster Sales. | This may cause the cluster to fail to create a disk. | Open the cluster for sale as needed. |
| Security Managem ent- Complianc e Support Center- Platform Password Applicatio n | On the Storage Encryption page, turn on Metabase Disk Encryption. | During data encryption, read and write operations cannot be performed. As a result, your business is interrupted. The impact time depends on the amount of data in the database. | Unrecoverable. |
|   | On the Encryption in Transmission > Metabase Access Encryption in Transmission page, turn on Encryption in Transmission. | The applications displayed on the page are Rolling. In normal cases, your business is not affected. | Disable transmission encryption. |
| Managem ent |   |   |   |
|   | On the Network Transmission Encryption > Platform Access Transmission Encryption page, turn on Transmission Encryption. | The applications displayed on the page are Rolling. In normal cases, your business is not affected. | Disable transmission encryption. |
|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > SRS Management. On the Configuration Management tab, modify the SRS security isolation status. | Modifying the security isolation status of the SRS causes a change in the network security protection policies. If the Security Isolation status of SRS is set to On or Automatic, the network connectivity of the cloud platform may be affected. If the SRS security isolation status is disabled, network security risks are introduced. | Restores the SRS security isolation state before the modification. However, this state may still be affected during the restoration. |

|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > SRS Management. On the Configuration Management tab, add or delete an SRS IP address whitelist. | Adding a whitelist may introduce cybersecurity risks. If you delete a whitelist, the IP addresses in the original whitelist may fail to access services in the cloud. | The configuration is restored to the previous configuration. However, it is estimated that it takes 10 minutes for the new configuration to take effect. This may still cause impacts during the restoration. |
|---|---|---|---|
| Security Managem ent- Network Security- Network Security Managem ent Center |   |   |   |
|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > SRS Management. On the Configuration Management tab, add or delete an SRS IP address blacklist. | Adding a blacklist may cause IP addresses in the blacklist to fail to access services in the cloud. Removing the blacklist may introduce cybersecurity risks. | The configuration is restored to the previous configuration. However, it is estimated that it takes 10 minutes for the new configuration to take effect. This may still cause impacts during the restoration. |
|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > SRS Management. On the Configuration Management tab, add or delete SRS isolation. | Adding non-isolated products may introduce cybersecurity risks. If you delete a product without isolating it, the related product services may become unavailable. | The configuration is restored to the previous configuration. However, it is estimated that it takes 10 minutes for the new configuration to take effect. This may still cause impacts during the restoration. |
|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > SRS Management. On the Configuration Management tab, add or delete an SRS bypass baseline. | New bypass products may make related products and services unavailable. Removing bypass products may introduce cybersecurity risks. | The configuration is restored to the previous configuration. However, it is estimated that it takes 10 minutes for the new configuration to take effect. This may still cause impacts during the restoration. |

|   | In the left-side navigation pane, click East-West Security Management > Apsara Infrastructure Management Framework Inward Protection-SRS > Isolation Configuration Management. On the page that appears, add or delete dynamic release configurations. | The new dynamic release configuration may introduce network security risks. If you delete the dynamic release configuration, the related products and services may become unavailable. | The configuration is restored to the previous configuration. However, it is estimated that it takes 10 minutes for the new configuration to take effect. This may still cause impacts during the restoration. |
|---|---|---|---|
|   | In the left-side navigation pane, choose East-West Security Management > PaaS Inbound Protection- East Emperor Bell > East Emperor Bell Configuration. | The ports of all hosts in the PaaS base cluster will be open to addresses outside the cloud, which may introduce network security risks. | Enable host network isolation. |
|   | In the left-side navigation pane, click East-West Security Management > PaaS Intrusion Protection- East Emperor Bell > East Emperor Bell Configuration. On the page that appears, add a CIDR block to the whitelist. | If network isolation is enabled for a host and a CIDR block is added to the whitelist, all ports of the host in the PaaS base cluster are allowed to access the CIDR block. If the CIDR block is untrusted, network security risks may occur. | Deletes an untrusted CIDR block from the whitelist. |
|   | In the left-side navigation pane, click East-West Security Management > PaaS Intrusion Protection- East Emperor Bell > East Emperor Bell Configuration. On the page that appears, delete the CIDR block from the whitelist. | If you enable network isolation for hosts and delete the CIDR block from the whitelist, the CIDR block cannot be used to access the ports of all hosts in the PaaS base cluster. As a result, normal service connections are interrupted. | Add another CIDR block to the whitelist. |
|   | In the left-side navigation pane, choose East-West Security Management > PaaS Inbound Protection- East Emperor Bell > East Emperor Bell Configuration. | If host network isolation is enabled and ports that allow access to hosts are added, the added ports of all hosts in the PaaS clusters can be accessed only from IP addresses or CIDR blocks in the whitelist. If the port that needs to be accessed is not added, your business is interrupted. | Make sure that the CIDR blocks that you trust are included in the whitelist before you modify or add the ports. |

| Security Managem ent - Account Security - Linux Account Managem ent | In the left-side navigation pane, click Password Management for Root. On the page that appears, update passwords on the Password management tab. | The passwords of the accounts for physical machines and kernel-based virtual machines (KVMs) are changed. | Find the original passwords in the password history and restore the passwords to the original passwords. |
|---|---|---|---|
|   | In the left-side navigation pane, click Password Management for Root. On the page that appears, turn off Password tube switch on the Configuration tab. | If you turn off the switch, you cannot update or rotate the passwords of machines in the Apsara Uni-manager Operations Console. If you turn off the switch, the aso-opr container cannot execute jsch commands. In this case, the archive management and log clearing capabilities of the Apsara Uni-manager Operations Console become unavailable. | Turn on Password tube switch to enable password hosting. |
|   | On the Root Password Management page, turn on the Rotation switch on the Configuration tab. | The password rotation operation is performed based on the rotation configuration time of each machine (once every 15 days by default). | Find and recover historical passwords from the password history. |
|   | On the Linux Account Management Tasks > Task Template Management page, run the GlobalTunnelRemoveTask task. | The initial global password- free channel from the OPS machine to all other machines is reclaimed. | The password-free channel from the OPS machine to all physical machines is reconnected. |
|   | On the Linux Account Management Tasks > Task Template Management page, run the GlobalTunnelRotateTask task. | the system rotates the default password-free channel. during the rotation, non-standard machines that depend on the initial key may fail to communicate with each other through ssh. | Re-issue the original key to the machine that has completed the change. |

| User permissio ns | On the Users page, delete the user. | If you delete a user, the user is moved to the recycle bin and the AccessKey pair of the user is disabled. As a result, products or programs that use these AccessKey pair cannot run properly. | Restore the user in the recycle bin. After the user is restored, the AccessKey pair of the RAM user is disabled by default and can be re- enabled. |
|---|---|---|---|
| Avatar- Personal Informatio n | In the Accesskey section, disable or delete the AK/SK. | As a result, callers who use this AK/SK to call OpenAPI may become unavailable. | If you disable an AccessKey pair, you can enable it again. If you delete an AccessKey pair, the AccessKey pair cannot be restored. In this case, replace the deleted AccessKey pair in the code of the services or applications with a new one. |

## 7 Appendixes

### 7.1 Common Maintenance Commands

**Commands**

This topic describes common maintenance commands in the Apsara Uni-manager Operations Console, including commands for logging on to environments and containers, and Kubernetes common commands in Agile PaaS.

**Commands for logging on to environments and containers**

Logon Environment

```bash
kubectl get ingress -n aso
```

Log on to a container

```bash
kubectl get pod -n aso
```

Pods that go to a single container

```bash
kubectl exec -it asoconsoleconsole-0 -n aso /bin/bash
```

**Common commands Kubernetes Agile PaaS**

The host goes to the Kubernetes console.

```python
sudo arkshoot
```

View the service status

```bash
kubectl get po -n ark-system
```

View deployed products

```bash
kubectl get appset -n ark-system
```

View the configuration information of a product

```bash
kubectl get appset -n ark-system aso-0 -oyaml
```

View the stage, status, and configuration information of a service role deployment

```bash
kubectl get appinstance -n ark-system aso-mgr.asmgr -oyaml
```

View the chart deployment workflow status

```
argo get -n ark-system inst-aso-mgr-asmgr-zkgqr ${Revision}
```

View container operational logs

```
argo get -n ark-system aso-mgr.asmgr
```

View the containers running in the Apsara Uni-manager Operations console

```bash
kubectl get po -n aso
```

Viewing Startup Information for a asomgrasmgr-0

```bash
kubectl logs asomgrasmgr-0 -n aso -c dep-init
```

Describe information about a node

```bash
kubectl describe pods asdconsoletaskmanager-0 -n asd
```

View product-specific descriptions

```bash
kubectl describe po podName -n aso
```

Get IP

```bash
kubectl get pods -n asd -o wide
```

View all DNS configurations in your environment

```bash
kubectl get ingress -A
```

View configuration items data

```bash
kubectl get ingress -n asd asdportal-nginx-ingress -o yaml
```

View environment variables

```bash
kubectl get cm ark.cmdb.app.asd-console.taskmanager.expose -n ark-system -oyaml
```

View the Ingress address

```bash
kubectl get ingress -n aso
```

Delete a Pod

```bash
kubectl delete po pod_name -n aso
```

View memory information

```
cat /proc/meminfo
```

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
| 500 | Internal errors in the server |
| 501 | Requested function not supported in the server |
| 510 | Database operation errors |
