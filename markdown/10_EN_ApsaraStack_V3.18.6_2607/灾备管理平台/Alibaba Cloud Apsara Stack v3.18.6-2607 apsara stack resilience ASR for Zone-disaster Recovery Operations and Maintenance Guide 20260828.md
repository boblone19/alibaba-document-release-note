---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Zone-disaster Recovery Operations and Maintenance Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 96
source_pdf: "5fac65ba574bf306_Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Zone-disaster Recovery Opera"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E7%81%BE%E5%A4%87%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20apsara%20stack%20resilience%20ASR%C2%A0for%C2%A0Zone-disaster%C2%A0Recovery%20Operations%20and%20Maintenance%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 apsara stack resilience ASR for Zone-disaster Recovery Operations and Maintenance Guide 20260828

## Table of Contents

- 1 Overview
  - 1.1 Introduction
  - 1.2 O&M architecture
  - 1.3 Roles
- 2 ASR O&M operations
  - 2.1 Getting started
    - 2.1.1 Log on to the ASR console
    - 2.1.2 View platform monitoring metrics
      - 2.1.2.1 Service monitoring
      - 2.1.2.2 Synchronization monitoring
  - 2.2 Core alert handling
    - 2.2.1 Alert items
    - 2.2.2 inspect_db_resource
    - 2.2.3 drei_product
    - 2.2.4 rpo_check
      - 2.2.4.1 Overview
      - 2.2.4.2 rpo_check (ApsaraDB RDS)
      - 2.2.4.3 rpo_check (OSS)
    - 2.2.5 sync_check
      - 2.2.5.1 Overview
      - 2.2.5.2 sync_check (MiddleWareAll)
      - 2.2.5.3 sync_check (minirds-mt/rds)
      - 2.2.5.4 sync_check (SLB)
      - 2.2.5.5 sync_check (Kafka)
      - 2.2.5.6 sync_check (Elasticsearch)
    - 2.2.6 inspect_product_cluster_aplus
    - 2.2.7 inspect_product_cluster_version
    - 2.2.8 inspect_product_variable
    - 2.2.9 inspect_product_cluster_deploy
    - 2.2.10 Appendixes
      - 2.2.10.1 Log on to the Apsara Uni-manager Management Console
      - 2.2.10.2 Log on to the Apsara Uni-manager Operations Console
      - 2.2.10.3 Log on to a container
      - 2.2.10.4 Log on to the xuanyuan database
      - 2.2.10.5 Log on to the Apsara Infrastructure Management console
      - 2.2.10.6 Secondary database rebuild
      - 2.2.10.7 Log on to an abnormal instance
- 3 Cloud service O&M operations
  - 3.1 TianJi
    - 3.1.1 Check the desired state
  - 3.2 DNS
    - 3.2.1 Check data consistency
    - 3.2.2 Check the domain name resolution service
  - 3.3 MiniRDS
    - 3.3.1 Check tasks
    - 3.3.2 Check the DR status of instances
    - 3.3.3 Check the status of instances
  - 3.4 ApsaraDB RDS
    - 3.4.1 Check tasks
    - 3.4.2 Check the DR status of instances
    - 3.4.3 Check the status of instances
  - 3.5 SLB
    - 3.5.1 Check the status of LVSs
    - 3.5.2 Check the status of proxies
    - 3.5.3 Check the status of keyservers
  - 3.6 OSS
    - 3.6.1 Check bucket locations
  - 3.7 ECS
    - 3.7.1 Check the status of NCs
  - 3.8 ASO
    - 3.8.1 Check the traffic
    - 3.8.2 Check alerts
- 4 FAQ
  - 4.1 What do I do if VIPs in the secondary data center are abnormal?
- 5 Appendixes
  - 5.1 View ASR logs
  - 5.2 Log on to a container
  - 5.3 Log on to the tianji-sshtunnel database
  - 5.4 Log on to the oss_meta database
  - 5.5 Log on to the houyi-reg database
  - 5.6 Resolve configuration inconsistency between the primary and secondary tables

## 1 Overview

### 1.1 Introduction

ASR for Zone-disaster Recovery is a cloud platform designed to provide hybrid backup and recovery solutions. This service ensures data security and business continuity for enterprises. ASR stands for Apsara Stack Resilience. This topic describes the objectives, requirements, precautions, and technical support contacts for ASR for Zone-disaster Recovery O&M.

**Objectives**

This manual is designed to help O&M personnel perform preventive maintenance on ASR for Zone-disaster Recovery to ensure the long-term stable operation of the system. The O&M personnel can follow the instructions in this guide to handle system issues that are identified during maintenance. For system issues that are not covered in this guide, the O&M personnel can contact Apsara Stack engineers for technical support.

**Requirements**

The O&M personnel must possess skills and knowledge related to the information technology industry, including computer networking, computer operation, problem analysis, and troubleshooting. The O&M personnel must pass the pre-job training and understand the Apsara Stack system. The required knowledge for the system includes system principles, networking, features, and the usage of maintenance tools.

> **Important:** The O&M personnel must comply with operation procedures during maintenance to ensure personal safety and system security. User data must be kept strictly confidential and must not be copied or disseminated without written consent from users.

**Precautions**

To ensure stable system operation and prevent unexpected events, the O&M personnel must comply with the following guidelines: Hierarchical permission management Permissions on networks, devices, systems, and data are granted based on the services and roles of the O&M personnel. This prevents system faults due to unauthorized operations. System security Before the O&M personnel perform operations on the system, they must be clearly aware of the impacts of the operations. This ensures that the system is not affected by high-risk operations. The O&M personnel must clearly record the details of the issues that are encountered during the operations. This helps O&M engineers troubleshoot the issues. Personal safety and data security The O&M personnel must take measures to ensure safety based on device manuals when electrical equipment is used. The O&M personnel must use secure devices to access the business network. Unauthorized data replication and dissemination are prohibited.

**Technical support**

To obtain help during system maintenance, the O&M personnel can contact Apsara Stack system technical support.

### 1.2 O&M architecture

This topic describes the O&M operations supported by Apsara Stack Resilience (ASR) for Zone-disaster Recovery. ASR for Zone-disaster Recovery allows you to perform the following O&M operations: Platform monitoring: including service monitoring and synchronization monitoring. Service monitoring: allows you to monitor the status of services or components in the primary and secondary data centers, and check the alert information and the services or components that are deployed in active-active mode. Synchronization monitoring: allows you to view the data synchronization latency compliance rate, number of instances with successful synchronization, number of instances with synchronization exceptions, and synchronization latency for instances of ApsaraDB RDS, Object Storage Service (OSS), and Tablestore. Platform check: including environment check and service check. Environment check: allows you to check whether the following check items meet disaster recovery (DR) conditions: Product Configuration Upgrade, Cluster Deployment, Product Version, Product Baseline, DNS Resources, VIP Resources, Database Resources, Conditions of the Network Between Data Centers, and BGP Route. Service check: allows you to check the status of services such as Server Load Balancer (SLB), DNS, and MiniRDS.

### 1.3 Roles

This topic describes the O&M operations that can be performed by different roles of Apsara Stack Resilience (ASR) for Zone-disaster Recovery.

| Logon scenario |   | DR scenario |   |   | Routine scenario |   |
|---|---|---|---|---|---|---|
| Role |   | Advanced O&M | Basic O&M | Visitor | System Admin | Platform Operation administrat or |
| Primary data center | Alert overview | Not supported | Not supported | Not supported | Not supported | Not supported |
|   | Service monitoring | Supported | Supported | Supported | Supported | Supported |
|   | Synchroniz ation monitoring | Not supported | Not supported | Not supported | Not supported | Not supported |
|   | Environme nt check | Supported | Supported | Supported | Supported | Supported |
|   | Service check | Supported | Supported | Supported | Supported | Supported |
| Secondary data center | Alert overview | Supported | Supported | Supported | Supported | Supported |
|   | Service monitoring | Supported | Supported | Supported | Supported | Supported |
|   | Synchroniz ation monitoring | Supported | Supported | Supported | Supported | Supported |
|   | Environme nt check | Supported | Supported | Supported | Supported | Supported |
|   | Service check | Supported | Supported | Supported | Supported | Supported |

## 2 ASR O&M operations

### 2.1 Getting started

#### 2.1.1 Log on to the ASR console

Apsara Stack Resilience (ASR) for Zone-disaster Recovery provides three logon methods for various scenarios, including routine O&M, disaster recovery escape, and tenant operations.

> **Note:** In this document, the Zone-disaster Recovery Management Platform ASR is referred to as the ASR console.

**Prerequisites**

To log on from the Apsara Uni-manager Operations Console, you have obtained the endpoint, username, and password for the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: <region-id>.console.<intranet-domain-id>. For a disaster recovery escape logon, you have obtained the endpoint, username, and password of the ASR console from the deployment personnel or an administrator. If the primary data center fails, log on to the ASR console of the secondary data center. If the secondary data center fails, log on to the ASR console of the primary data center. The two data centers have different domain names. The endpoint of the ASR console for the secondary data center is in the following format: asr-xs-<region-id>.console.<intranet-domain-id>/user/login. The endpoint of the ASR console for the primary data center is in the following format: asr-xm-<region-id>.console.<intranet-domain-id>/user/login. To log on for tenant operation scenarios, you have obtained the service domain name of the Apsara Uni-manager Management Console from the deployment personnel.

**Log on to the Unified O&M platform**

> **Note:** The view that is rendered after you log on to the ASR console for zone-disaster recovery varies based on the permissions configured for your user account in the Apsara Uni- manager Operations Console. If a user account has multiple permissions, the menu items for all corresponding roles are displayed.
> If a user is granted only the disaster recovery monitoring permission in the Apsara Uni-manager Operations Console, the Monitoring Center menu item in O&M mode and the Platform Monitoring and Overview menu items in normal mode are displayed.
> If a user is granted only the disaster recovery drill permission in the Apsara Uni- manager Operations Console, the menu items for the normal mode view and the Monitoring Center menu item for the O&M mode view are displayed.
> If a user is granted only the disaster recovery O&M permission in the Apsara Uni- manager Operations Console, only the feature modules for the O&M mode view are displayed, and you cannot switch to the normal mode view.
> If a user is granted both the disaster recovery monitoring and disaster recovery O&M permissions, or is granted the system administrator permission in the Apsara Uni-manager Operations Console, the features for both normal and O&M modes are displayed, and you can switch between them.

1. Open a web browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese and English are supported.

3. Enter the correct username and password.

> **Note:** Obtain the username and password that are used to log in to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.
> If you enter an invalid password three consecutive times, the system enables the image verification login feature. If you enter an invalid password five consecutive times, the system locks your account. In this case, you can contact the administrator to unlock your account.
> The first time that you log in to the Apsara Uni-manager Operations Console, change the password for your account as prompted.
> To enhance security, make sure that your password meets the following requirements:
> The password contains uppercase and lowercase letters.
> The password contains digits.
> The password contains at least one of the following special characters: ! @ # $ %
> The password is 10 to 20 characters in length.

4. Click **Agree to Private Policy and Log On** .
5. In the top navigation bar, choose **Platform Operation > Disaster recovery**
**management > ASR for Zone-Disaster Recovery**.
6. Click
at the top of the navigation pane on the left to switch between the primary and secondary data centers.
7. (Optional) In the navigation pane on the left, click Normal Mode or O&M Mode to switch
between views.

> **Note:** To switch views, you must have the disaster recovery monitoring, disaster recovery drill, or system administrator permission.

**Disaster recovery escape logon**

> **Important:** By default, the disaster recovery escape logon feature is disabled. To use this logon method, you must first enable the feature and set a logon password. For more information, see Manage escape logon.

1. In your browser's address bar, enter the Zone-Disaster Recovery Management Platform ASR
endpoint and press Enter. If the primary data center fails, log on to the ASR console of the secondary data center. If the secondary data center fails, log on to the ASR console of the primary data center. The two data centers have different domain names. The endpoint of the ASR console for the secondary data center is in the following format: asr-xs-<region-id>.console.<intranet-domain-id>/user/login. The endpoint of the ASR console for the primary data center is in the following format: asr-xm-<region-id>.console.<intranet-domain-id>/user/login.

> **Note:** You can click the language drop-down list in the upper-right corner to switch the language. Simplified Chinese and English are supported.

2. Enter your username and password.

> **Note:** Obtain the username and password to log on to the ASR console from the deployment personnel or an administrator.

3. Click **Log on**.
4. In the top navigation bar, click Normal Mode or O&M Mode to switch between views.
5. In the top navigation bar, click a data center to open the corresponding data center page.

**Log on for tenant operations**

To recover individual services or perform disaster recovery drills by application, you can log on to the Apsara Uni-manager Management Console to create protection groups.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

> **Note:** **First login**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forgotten password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your login scenario: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter the six-digit MFA code and click **Authentication**. You have enabled and bound MFA: Enter the six-digit MFA code and click **Authentication**.

> **Note:** For more information about how to bind and enable MFA, see **Security Center** > **MFA** > **Manage MFA** in Apsara Uni-manager Operations Console User Guide.

5. In the top navigation bar, select **Products**.
6. In the navigation pane on the left, click **Disaster Recovery and Backup**.
7. In the **Disaster Recovery and Backup** section, choose **Disaster Recovery > ASR for**
**Zone-disaster Recovery**.

#### 2.1.2 View platform monitoring metrics

##### 2.1.2.1 Service monitoring

This topic describes how to view service monitoring information and the expected results.

**Procedure**

1. Log on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Primary Zone)
console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Monitoring > Product Monitoring**.
3. On the **Product Monitoring** page, view monitoring items such as feature readiness,
primary service location, and inspection results of all services. You can also view the number of disaster recovery (DR) instances and capacity usage of specific services.

> **Note:** When you view monitoring information, make sure that the data is updated to the current time.

**Expected results**

No item is marked in red. If an anomaly exists, troubleshoot the issue based on the error message, or contact Alibaba Cloud technical support to fix the issue.

##### 2.1.2.2 Synchronization monitoring

This topic describes how to monitor data synchronization and view the expected results.

**Monitoring method**

1. Log on to the ASR console in the secondary data center.
2. In the navigation pane on the left, choose **Platform Monitoring** > **Synchronization**
**Monitoring**.
3. On the Synchronization Monitoring page, you can view the data synchronization latency
satisfaction rate, the number of instances with normal synchronization, the number of instances with abnormal synchronization, and the synchronization latency of each instance for RDS, Redis, PolarDB-X 2.0, MongoDB, AnalyticDB for PostgreSQL, OSS. Instances with abnormal synchronization are displayed in red at the top of the instance list.

> **Note:** When you view metric information, ensure that the data update time is current.

**Expected results**

The data synchronization latency satisfaction rate is 100%.

> **Note:** If this requirement is not met, troubleshoot and resolve the synchronization latency issues for the instances marked in red, or submit a ticket to contact Alibaba Cloud technical support.

### 2.2 Core alert handling

#### 2.2.1 Alert items

This topic describes the alert items of Apsara Stack Resilience (ASR) for Zone-disaster Recovery.

| Alert item | Description | Alert level | References |
|---|---|---|---|
| inspect db resourc _ _ e | The connection to the metadabase is abnormal, or the read and write status of the metadabase is read-only. | P2 | inspect db resource _ _ |
| drei product _ | The disaster recovery (DR) capabilities of core base services, such as DNS, Server Load Balancer (SLB), and MiniRDS, are abnormal. | P2 | drei product _ |

| rpo check _ | The synchronization latency of ApsaraDB RDS or Object Storage Service (OSS) exceeds the threshold, or the synchronization is interrupted. | P2 | ApsaraDB RDS: rpo check (ApsaraDB _ RDS) OSS: rpo check (OSS) _ |
|---|---|---|---|
| sync check _ | Anomalies are found during service DR inspection. | P2 | MiddleWareAll: sync check _ (MiddleWareAll) minirds-mt/rds: sync check (minirds- _ mt/rds) TableStore/TableStoreInner: sync check _ (TableStore/TableStoreInner) SLB: sync check (SLB) _ ApsaraMQ for Kafka: sync check _ (Kafka) Elasticsearch: sync check _ (Elasticsearch) |
| inspect product cl _ _ uster aplus _ | Rolling is not performed on cloud service clusters. | P2 | inspect product cluster aplus _ _ _ |
| inspect product cl _ _ uster version _ | Service versions are inconsistent between the primary and secondary data centers. | P2 | inspect product cluster version _ _ _ |
| inspect product va _ _ riable | Fail to pass the service baseline variable check. | P2 | inspect product variable _ _ |
| inspect product cl _ _ uster deploy _ | Specific services are deployed in asymmetric mode. | P2 | inspect product cluster deploy _ _ _ |

#### 2.2.2 inspect_db_resource

This alert is used to check the connectivity and the read and write status of the metadatabase. This alert is triggered if connections to the metadatabase fail or the metadatabase is read-only. This may cause data write failures, and the services that depend on the metadatabase may not run as expected.

**Alert attributes**

| > Document | Version: 202 | 60828 |   |   |   | 1 |
|---|---|---|---|---|---|---|

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| inspect d _ b resour _ ce | inspect d _ b resour _ ce | Bcmc# | P2 | bcmc | The connectivit y or the read and write status of the instance is abnormal. | Every 30 minutes |

**Supported versions**

Apsara Stack V3.14 and later

**Causes**

The connectivity of the instance is abnormal. The read and write status of the instance is abnormal.

**Alert impacts**

Data may fail to be written, and the services that depend on the metadatabase may not run as expected.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose Resources > **Product & Cluster O&M**.
3. On the Product & Cluster O&M page, enter bcmc in the search box. In the search results,
find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
4. On the Services tab, find the **bcmc** service and click its name.
5. In the Components pane, click **Bcmc#**.
6. On the **Resources** tab, find the resource whose name is **asr** and type is **db**. Then, view the
values of the db_host, user, db_password, db_port, and db_name parameters in the
**Resource Application Result** column.
7. Log on to the machine where the alert is reported.
8. Run the following command to check whether the database is accessible:

> **Note:** Run the command to log on to the database in an environment in which a MySQL client is available.

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

The following figure shows a sample output, which indicates that the connection is normal. Proceed based on the actual output.

> **Note:** If the database is inaccessible, contact the ApsaraDB RDS production and R&D team.

9. Execute the following SQL statement to view the read and write status of the database:

```
show global variables like "read_only";
```

The following figure shows a sample output. Proceed based on the actual output. If the value of the **read_only** variable is **ON**, the database is read-only. You must change the read-only status. Execute the following SQL statement to change the read-only status:

```
set global read_only = 0;
```

0. Obtain the name of the abnormal instance based on the alert information.
1. Log on to the ApsaraDB Operations and Maintenance System console.
2. View the detailed error message of the instance. If the database connection failed because
the instance is not started, restart the instance. i. Log on to the host of the abnormal instance. ii. Run the following command to view and record the command used to start the abnormal instance:

```
cat /etc/init.d/mysql | grep ${Port number}
```

The following figure shows a sample output. Proceed based on the actual output. iii. Run the following command to start the abnormal instance:

```
/u01/mysql56/bin/mysqld_safe --defaults-file=/etc/my${Port number}.cnf &
```

iv. Run the following command to check whether the instance is started:

```
ps aux|grep ${Port number}
```

The following figure shows a sample output. Proceed based on the actual output.

> **Note:** If the instance fails to be started, contact the ApsaraDB RDS production and R&D team.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.3 drei_product

This alert is used to check whether MiniRDS instances can be switched over, whether the synchronization between the primary and secondary MiniRDS instances experiences latency, whether single-zone instances exist, and whether the serviceTest# component in a MiniRDS cluster is at desired state. This alert is triggered if one or more of the preceding conditions are true.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| drei prod _ uct | drei prod _ uct | Bcmc# | P2 | minirds- mt | This alert is triggered in one of the following conditions: Fail to connect to instances. The synchronization between the primary and secondary instances experiences latency. Single-zone instances exist. Instances exist in the secondary data center. The serviceTest# component in a MiniRDS cluster is not at desired state. | Every 30 minutes |

**Supported versions**

Apsara Stack V3

**Causes**

This alert is triggered in one of the following conditions: Fail to connect to instances. The synchronization between the primary and secondary instances experiences latency. Single-zone instances exist. Instances exist in the secondary data center. The serviceTest# component in a MiniRDS cluster is not at desired state.

**Alert impacts**

The alert impacts vary based on the alert cause. The following issues may occur: If connections to instances fail, you may not be able to access MiniRDS databases. If the synchronization between the primary and secondary instances experiences high latency, when the primary data center fails, data may be lost. If the serviceTest# component in a MiniRDS cluster is not at desired state, the features of the clusters and your business may be affected.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Instances exist in the secondary data center**

If instances exist in the secondary data center, you do not need to handle the issue. The instances are automatically switched back to the primary data center in the primary zone.

**Single-zone instances exist**

If single-zone instances exist, you must deploy them across two zones.
1. Log into the container.
2. Run the following command in the container to copy the conf.yml.j2 file to the specified
directory:

```bash
docker cp conf.yml.j2 ${Container ID}:/meta/usr/local/rds/rebuild/conf.yml.j2
```

The following code shows the content of conf.yml.j2:

```bash
# conf.yml.j2
db:
  host: {{db_dbaas_host}}
  port: {{db_dbaas_port}}
  user_name: {{db_dbaas_user}}
  password: {{db_dbaas_password}}
  db_name: {{db_dbaas_name}}
cluster:
  cluster_name: {{CLUSTER_NAME}}
  db_type: {{DB_TYPE}}
  db_version: {{DB_VERSION}}
  site_name: {{SITE_NAME}}
  ips: ""
  max_tasks: 10                # The task concurrency.
  ins_names: ""                  # The names of the instances to be rebuilt. Separate
multiple names with commas (,). You must specify this parameter. Otherwise, instances cannot be rebuilt. api:
  rdsapi: {{RDS_API_URL}}
timeout: {{TIMEOUT}}
```

3. Contact Alibaba Cloud technical support to obtain the rebuild files and decompress them.
Copy all the files to the RebuildSlave container.

```bash
docker cp ${Name of a rebuild file}:/usr/local/rds/rebuild/
```

4. After you copy the files to the RebuildSlave container, run the following commands to
restart the RebuildSlave container:

```bash
docker stop ${Container ID} docker start ${Container ID}
```

**Instances cannot be switched over, synchronization between**

**the primary and secondary instances experiences latency, or**

**connections to instances fail**

1. Obtain the name of the abnormal instance based on the alert information.
2. Log on to the ApsaraDB Operations and Maintenance System console.
3. View the detailed error information of the instance.
i. If the instance connection fails, handle the issue by referring to inspect_db_resource. ii. If the synchronization between the primary and secondary instances experiences latency, handle the issue by referring to Rebuild a secondary database. iii. If the instance cannot be switched over, handle the issue by referring to Rebuild a secondary database.

**The serviceTest# component in a MiniRDS cluster is not at**

**desired state**

1. Log on to the Apsara Infrastructure Management console.
2. On the **Product & Cluster O&M** page, check whether the serviceTest# component in the
minirds-maotai cluster is at desired state.
3. If the serviceTest# component is not at desired state, restart the component.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.4 rpo_check

##### 2.2.4.1 Overview

The rpo_check alert is used to check the synchronization latency of ApsaraDB RDS or Object Storage Service (OSS). This alert is triggered if the synchronization latency exceeds the specified threshold or the synchronization is interrupted. The handling method varies based on the service. ApsaraDB RDS: rpo_check (ApsaraDB RDS) OSS: rpo_check (OSS)

##### 2.2.4.2 rpo_check (ApsaraDB RDS)

This alert is used to check the synchronization latency of ApsaraDB RDS disaster recovery (DR) instances. If this alert is triggered, the synchronization latency exceeds the specified threshold or the synchronization is interrupted. This may cause data loss or failover failure. This topic describes the rpo_check alert of ApsaraDB RDS.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| rpo check _ | rpo check _ | Bcmc# | P2 | ApsaraDB RDS | The synchroniz ation latency of an ApsaraDB RDS DR instance exceeds the specified threshold, or the synchroniz ation is interrupted . | 1 minute |

**Supported versions**

Apsara Stack V3.12 and later

**Causes**

When dr_service checks the synchronization latency of an ApsaraDB RDS DR instance, if a connection exception or an SQL execution error occurs and the default recovery point objective (RPO) value is negative, this alert is triggered. The following table describes the causes of this alert.

| Engine | Default value | Cause |
|---|---|---|
| MySQL | -1 | Failed to connect to the secondary database. An error is reported when SQL statements are being executed. The value of Seconds Behind Master is null. _ _ |
| PostgreSQL | -1/-2 | An error is reported when SQL statements are being executed on dbaas. Failed to obtain the account information of aurora. Failed to connect to the secondary database, or the secondary database is unavailable. The value of pglog diff is null. _ |

| MongoDB | -2 | Failed to connect to the primary and secondary databases, or the primary and secondary databases are unavailable. |
|---|---|---|
| Redis | -1/-2 | An error is reported when SQL statements are being executed. Failed to connect to the secondary database. |

**Alert impacts**

If the synchronization latency is in an abnormal state, the following issues may occur: If the synchronization latency is excessively high, a large amount of data may be lost when the primary node fails. Failover fails because the secondary instance cannot be accessed, or the secondary instance is unavailable after failover.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane of the **ApsaraDB Operations and Maintenance System**
**console**, click **System Management**. In the left-side pane that appears, choose **Disaster**
**Recovery Management > Disaster recovery switching**.
4. On the **Disaster recovery switching** page, view the exception details and contact
ApsaraDB RDS O&M engineers to fix the exception. If the DR instance is not started, restart the instance. a. Log on to the server on which the primary node of the DR instance is deployed.

> **Note:** In this example, a MySQL instance is used.

b. Run the following command. If the instance process does not exist, the instance is not started.

```
ps aux | grep ${Port number}
```

c. Run the following command to view and record the command used to start the abnormal instance:

```
cat /etc/init.d/mysql | grep ${Port number}
```

The following figure shows a sample output. Proceed based on your actual output. d. Run the following command to start the abnormal instance:

```
/u01/mysql56/bin/mysqld_safe --defaults-file=/etc/my${Port number}.cnf &
```

e. Run the following command and check whether the instance is started:

```
ps aux | grep ${Port number}
```

The following figure shows a sample output. Proceed based on your actual output.

> **Note:** If the instance fails to be started or other exceptions occur, contact ApsaraDB RDS O&M engineers.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

##### 2.2.4.3 rpo_check (OSS)

This alert is used to check the synchronization latency of Object Storage Service (OSS) disaster recovery (DR) buckets. This alert is triggered if the synchronization latency exceeds the specified threshold or the synchronization is interrupted. This may cause data loss or failover failures. This topic describes the rpo_check alert of OSS.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| rpo check _ | rpo check _ | Bcmc# | P2 | OSS | The synchroniz ation latency of an OSS DR bucket exceeds the specified threshold, or the synchroniz ation is interrupted . | Once a minute |

**Supported versions**

Apsara Stack V3.12 and later

**Causes**

The queries per second (QPS) is excessively high and messages are accumulated.

**Alert impacts**

If the synchronization latency is in an abnormal state, the following issues may occur: If the synchronization latency is excessively high, a large amount of data may be lost when the primary node fails. Failover fails because the secondary instance cannot be accessed, or the secondary instance is unavailable after failover.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

1. Check whether synchronization processes are enabled.
i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara *********************************** , choose Resources > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter oss in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the ************ tab, find the **oss-ocm-server** service and click its name. v. In the Components pane, click **OcmServer#**. vi. On the Instances tab, click ************ in the **Actions** column of an instance and log on to the oss-ocm-server.OcmServer# terminal server. vii. Go to the `/cloud/app/oss-ocm-server/OcmServer#/ocm_server/current` directory. viii. Run the following command to obtain the AccessKey ID and AccessKey secret of OCM_CMD:

```
cat ocm_conf.json | grep -A 10 "accessID"
```

ix. Run the following commands to obtain the value of master_ocm_host:

```
cat ocm_conf.json | grep master_ocm_host
```

x. Replace accessID, accessKey, and master_ocm_host in the following command with the values obtained in the previous steps and run the command:

```
./ocm_cmd config --id=${accessID} --key=${accessKey} --host ${master_ocm_host}
```

xi. Run the following command to check whether the content under the <BucketSyncMeta> tags is as expected:

```
./ocm_cmd gbm bucketName
```

> **Note:** Check items and expected results:
> a. Whether synchronization processes exist: If the <BucketSyncMeta> tags exist,
> synchronization processes exist.
> b. Whether the synchronization direction is as expected: If the <SrcBucket>,
> <SrcLocation>, <DestBucket>, and <DestLocation> tags exist under the <BucketSyncMeta> tags and meet the following conditions, the synchronization direction is as expected.
> a. The values of the <SrcBucket> and <SrcLocation> tags are the same as those of
> the <Name> and <Location> tags under the <BucketMeta> tag.
> b. The values of the <DestBucket> and <DestLocation> tags are the same as those
> of the peer data center.
> c. Whether the synchronization status is normal: Under the <BucketSyncMeta> tag,
> the value of the <SyncStatus> tag is 0 or 1.

Sample output:

```xml
<?xml version="1.0" encoding="UTF-8"?> <BucketMeta>
  <Name>wd-test</Name>
  <Owner>1276207919333070</Owner>
  <Application>file</Application>
  <Location>oss-cn-qingdao-env9b-amtest52002-b</Location>
  <CreateTime>Thu, 17 Dec 2020 06:09:29 GMT</CreateTime>
```

`h` `i`

```
1608534489/C
```

`h` `i`

```xml
  <CacheTime>1608534489</CacheTime>
  <Comment></Comment>
  <Acl>public-read-write</Acl>
  <BucketStatus>ok</BucketStatus>
  <BucketMode>default</BucketMode>
  <RequestPayer>BucketOwner</RequestPayer>
  <BucketPolicy>
    <LogBucket></LogBucket>
    <LogPrefix></LogPrefix>
    <Location>oss-cn-qingdao-env9b-amtest52002-b</Location>
    <DisallowEmptyRefer>false</DisallowEmptyRefer>
    <WhiteReferrerList />
    <CommonHeaderList />
    <AccessAllowedTypeList />
    <MimeTypeConfig>
      <MimeTypeRules />
    </MimeTypeConfig>
    <BucketChargeType>
      <FlowChargeType>PayByTraffic</FlowChargeType>
    </BucketChargeType>
    <CacheControlConfiguration />
    <MaxImageSize>-1</MaxImageSize>
    <UrlRewriteScript></UrlRewriteScript>
    <CompatMask>4</CompatMask>
    <TransferAccType></TransferAccType>
    <SourceProtectSuffix>*</SourceProtectSuffix>
    <IAMPolicy></IAMPolicy>
    <EnableDualCluster>false</EnableDualCluster>
    <IndexFile></IndexFile>
    <ErrorFile></ErrorFile>
    <SysObjectTagsStr></SysObjectTagsStr>
    <DataRedundancyType>0</DataRedundancyType>
    <ObjectHashFunction>NULL</ObjectHashFunction>
    <ObjectOverwriteCond>ALL</ObjectOverwriteCond>
    <AuthorizationConfiguration />
  </BucketPolicy>
  <CORSConfiguration />
  <BucketFlowLimits>
    <MaxQps>-1</MaxQps>
    <MaxSendFlow>-1</MaxSendFlow>
    <MaxRecvFlow>-1</MaxRecvFlow>
    <MaxIntranetQps>-1</MaxIntranetQps>
    <MaxIntranetSendFlow>-1</MaxIntranetSendFlow>
    <MaxIntranetRecvFlow>-1</MaxIntranetRecvFlow>
    <MaxTotalQps>-1</MaxTotalQps>
    <MaxIntranetTotalQps>-1</MaxIntranetTotalQps>
  </BucketFlowLimits>
  <BucketUserQos>
    <MaxHourExtranetSendFlow>-1</MaxHourExtranetSendFlow>
    <MaxDayExtranetSendFlow>-1</MaxDayExtranetSendFlow>
    <MaxHourIntranetSendFlow>-1</MaxHourIntranetSendFlow>
    <MaxDayIntranetSendFlow>-1</MaxDayIntranetSendFlow>
    <StorageCapacity>1073741824</StorageCapacity>
  </BucketUserQos>
<BID>26842</BID>
```

```xml
  <BID>26842</BID>
  <StorageType>standard</StorageType>
  <DualClusterStatus>1</DualClusterStatus>
  <BucketSyncMeta>
    <SyncStatus>1</SyncStatus>
    <SyncSubStatus>0</SyncSubStatus>
    <SyncHistoryStatus>1024</SyncHistoryStatus>
    <SyncAcl>0</SyncAcl>
    <SyncBackupStatus>0</SyncBackupStatus>
    <CreateTime>1608189511</CreateTime>
    <ModifyTime>1608189637</ModifyTime>
    <SrcBucket>wd-test</SrcBucket>
    <SrcLocation>oss-cn-qingdao-env9b-amtest52002-b</SrcLocation>
    <DestBucket>wd-test</DestBucket>
    <DestLocation>oss-cn-qingdao-env9b-d01-a</DestLocation>
    <HistoryCpt></HistoryCpt>
    <HistoryMpartKeyCpt></HistoryMpartKeyCpt>
    <HistoryUploadIdCpt></HistoryUploadIdCpt>
    <HistoryObjectSyncEnabled>true</HistoryObjectSyncEnabled>
    <Type>0</Type>
    <TransferType>0</TransferType>
    <VipProxy></VipProxy>
    <Speed>0</Speed>
    <ScanType>1</ScanType>
    <SubNum>0</SubNum>
    <ScheduleType>0</ScheduleType>
    <ScheduleBandwidth>0</ScheduleBandwidth>
    <RuleId></RuleId>
    <Version>5c665d30e017456e840fa11358f9ff97</Version>
    <NeedPartitionList>false</NeedPartitionList>
    <IsQpsTask>false</IsQpsTask>
    <IgnoreNewFileForHistory>true</IgnoreNewFileForHistory>
  </BucketSyncMeta>
  <BucketSyncMeta>
    <SyncStatus>4</SyncStatus>
    <SyncSubStatus>1</SyncSubStatus>
    <SyncHistoryStatus>768</SyncHistoryStatus>
    <SyncAcl>0</SyncAcl>
    <SyncBackupStatus>0</SyncBackupStatus>
    <CreateTime>1608185369</CreateTime>
    <ModifyTime>1608190889</ModifyTime>
    <SrcBucket>wd-test</SrcBucket>
    <SrcLocation>oss-cn-qingdao-env9b-d01-a</SrcLocation>
    <DestBucket>wd-test</DestBucket>
    <DestLocation>oss-cn-qingdao-env9b-amtest52002-b</DestLocation>
    <HistoryCpt></HistoryCpt>
    <HistoryMpartKeyCpt></HistoryMpartKeyCpt>
    <HistoryUploadIdCpt></HistoryUploadIdCpt>
    <HistoryObjectSyncEnabled>true</HistoryObjectSyncEnabled>
    <Type>0</Type>
    <TransferType>0</TransferType>
    <VipProxy></VipProxy>
    <Speed>0</Speed>
    <ScanType>1</ScanType>
    <SubNum>0</SubNum>
```

```xml
Subu 0/Subu
    <ScheduleType>0</ScheduleType>
    <ScheduleBandwidth>0</ScheduleBandwidth>
    <RuleId></RuleId>
    <Version>b6dbaeb845fb4c23bed94c5d717fa00e</Version>
    <NeedPartitionList>false</NeedPartitionList>
    <IsQpsTask>false</IsQpsTask>
    <IgnoreNewFileForHistory>true</IgnoreNewFileForHistory>
  </BucketSyncMeta>
  <BucketVpcipBindList />
  <Tagging>
    <TagSet />
  </Tagging>
</BucketMeta>
```

2. Check whether the recovery point objective (RPO) of OSS is normal.
i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose Resources > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter oss in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the **Services** tab, find the **oss-chiji-agent** service and click its name. v. In the Components pane, click **ChijiAgent#**. vi. On the Instances tab, click **Terminal** in the **Actions** column of an instance and log on to the oss-chiji-agent.ChijiAgent# terminal server. vii. Run the following command to calculate the RPO of OSS:

```
/apsara/deploy/dsu GetSyncTaskProgress Source location#Destination location#Source bucket#Destination bucket
```

> **Note:** Replace Source location, Destination location, Source bucket, and Destination bucket with the values of the <SrcLocation>, <DestLocation>, <SrcBucket>, and <DestBucket> tags obtained in Step 1.

In the command output, `new file last sync time` indicates the last time when files were synchronized. Obtain the RPO of OSS by subtracting the last synchronization time from the current time. If the synchronization processes are normal and the RPO of OSS is excessively large, the issue is caused because the QPS is excessively high and messages are accumulated. Contact OSS O&M engineers to resolve the issue.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.5 sync_check

##### 2.2.5.1 Overview

The sync_check alert is used to check the disaster recovery (DR) status of DR instances. This alert is triggered if an anomaly is found during the DR inspection of cloud services. The handling method varies based on the service. MiddleWareAll: sync_check (MiddleWareAll) minirds-mt/rds: sync_check (minirds-mt/rds) TableStore/TableStoreInner: sync_check (TableStore/TableStoreInner) Server Load Balancer (SLB): sync_check (SLB) ApsaraMQ for Kafka: sync_check (ApsaraMQ for Kafka) Elasticsearch: sync_check (Elasticsearch)

##### 2.2.5.2 sync_check (MiddleWareAll)

This alert is used to check the disaster recovery (DR) status of MiddleWareAll DR instances. This alert is triggered if an anomaly is found during the DR inspection of MiddleWareAll. This may cause failover failures or undermine the DR capabilities of cloud services that depend on MiddleWareAll. This topic describes the sync_check alert of MiddleWareAll.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | middleWar eAll | An anomaly is reported in the Apsara Stack Resilience (ASR) for Zone- disaster Recovery console during the DR inspection of MiddleWar eAll. | Once a minute |

**Supported versions**

Apsara Stack V3.12 and later

**Causes**

The value of distroThreshold of the vipserver component in MiddleWareAll is the default value 0.7. MiddleWareAll is not at desired state.

**Alert impacts**

If the DR status of MiddleWareAll is abnormal, the following issues may occur: Failover operations fail. The DR capabilities of cloud services that depend on MiddleWareAll are abnormal.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Wrong distroThreshold configuration of the vipserver**

**component**

1. Log on to the middleWare-vipserver.Server# container.
2. Run the following command to view the distroThreshold value. The default value is 0.7.

```bash
curl -s http://vipserver.tbsite.net/vipserver/api/switches | python -m json.tool
```

3. Run the following command to change the distroThreshold value to 0.45:

```json
curl-s"http://${diamond_host}/diamond-server/basestone.do?method=syncUpdateAll"-d 'da taId=com.taobao.vipserver.switches&group=VIPSERVER_GROUP&content= {"distroThreshold":0.45}'
```

> **Note:** To obtain the value of diamond_host, perform the following steps:

i. Log on to the Apsara Infrastructure Management console.

> ii. In the left-side navigation pane of the **Apsara Infrastructure Management**
> **console**, choose Resources > **Product & Cluster O&M**.
> iii. On the Product & Cluster O&M page, enter MiddleWareAll in the search box. In the
> search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
> iv. On the Services tab, find the **middleWare-diamond** service and click its name.
> v. On the **Registration Variables** tab, view the value of diamond_host.

4. Run the following command to verify that the distroThreshold value is 0.45:

```bash
curl -s http://vipserver.tbsite.net/vipserver/api/switches | python -m json.tool
```

**MiddleWareAll not at desired state**

1. Log on to the Apsara Infrastructure Management console.
2. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose Resources > **Product & Cluster O&M**.
3. On the Product & Cluster O&M page, enter MiddleWareAll in the search box. In the search
results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column.
4. On the Services tab, click the name of the service that is not at desired state.
5. In the Components pane, click the abnormal component. On the Instances tab, find the
abnormal instance and choose **Actions** > **Restart** in the **Actions** column.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

##### 2.2.5.3 sync_check (minirds-mt/rds)

This alert is used to check the disaster recovery (DR) status of minirds-mt/rds DR instances. This alert is triggered if an anomaly is found during the DR inspection of minirds-mt/rds. This may cause data loss, failover failures, or instance access exceptions. This topic describes the sync_check alert of minirds-mt/rds.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|

| sync check _ | sync check _ | Bcmc# | P2 | minirds- mt rds | An anomaly is reported in the Apsara Stack Resilience (ASR) for Zone- disaster Recovery console during the DR inspection of minirds- mt/rds. | Once a minute |
|---|---|---|---|---|---|---|

**Supported versions**

Apsara Stack V3.12 and later

**Causes**

Abnormal instance synchronization status Significant data differences between the primary and secondary minirds-mt/rds instances can lead to lengthy or failed synchronization between them. Closed SSH tunnels To execute the failover and DR scripts of specific cloud services, the SSH tunnels from bcmc to the server roles (SRs) of the cloud services must be open so that bcmc can access the SR containers to perform DR inspection and failover operations. The SSH tunnels from bcmc to the SRs of cloud services may be closed due to reasons such as missing or incorrect baseline configurations of SSH tunnels and issues in tianji-sshtunnel. In this case, DR inspection scripts cannot be executed as expected.

**Alert impacts**

If the DR status of minirds-mt/rds is abnormal, the following issues may occur: If the synchronization between the primary and secondary nodes experiences high latency, data may be lost when the primary node fails. Instances cannot be failed over. If the primary node fails, instances cannot be automatically failed over to the secondary node and service availability is affected. Instances cannot be accessed as expected, and the cloud services or applications that depend on the instances cannot run as expected.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Abnormal instance synchronization status**

In this example, ApsaraDB RDS is used.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, click **System Management**.
4. In the **System Management** pane, choose **Disaster Recovery Management** >
**Disaster recovery switching**. In the **Maximum Latency from library** column, view the
latency.

> **Note:** If the value is greater than 0 and smaller than 60, wait for data to be synchronized from the primary database to the secondary database.
> If the value is smaller than -1, contact the technical account manager (TAM) to recreate the secondary database.
> If the value is a large positive integer and does not decrease, contact database O&M engineers for troubleshooting.

**Closed SSH tunnels**

In this example, MiniRDS is used.
1. Check whether the sshd process of the peer MiniRDS service is started.
i. Log on to the MiniRDS container. ii. Run the ps -ef|grep sshd command to view the sshd process. If the ssh process is not started, you can manually run the `/usr/sbin/sshd` command to start the sshd process. If the sshd process does not exist in the container, install the sshd plug-in by running the `yum install sshd` command.
2. Modify the SSH tunnel configurations of the bcmc cluster.
i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose Resources > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter bcmc in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the **Cluster Details** page, click the **Desired State Configuration** tab. v. Modify the `/services/tianji-sshtunnel-` `client/user/SSHTunnelClient/ssh_tunnel_bcmc.conf` file. Add the following information to the file: FromProduct, FromClusterType, FromServerRole, FromService, FromUser, ToProduct, ToClusterType, ToServerRole, ToService, and ToUser. Then, submit the changes.

> **Note:** The values of the FromClusterType and FromServerRole parameters vary based on the region type. For the central region, set the FromClusterType parameter to BcmcCluster and the FromServerRole parameter to Bcmc. For general regions, set the FromClusterType parameter to Bcmc4GeneralCluster and the FromServerRole parameter to Bcmc4General. Sample code:

```
- FromProduct: bcmc
  // FromClusterType: Bcmc4GeneralCluster // Note: For the central region, set
the parameter to BcmcCluster. For general regions, set the parameter to Bcmc4Ge neralCluster.
  // FromServerRole: Bcmc4General // Note: For the central region, set the para
meter to Bcmc. For general regions, set the parameter to Bcmc4General.
  FromClusterType: BcmcCluster
  FromServerRole: Bcmc
  FromService: bcmc
  FromUser: root
  ToProduct: minirds-mt // The cloud service to be connected.
  ToClusterType: maotai_7u // The type of the service cluster to be connected.
  ToServerRole: Aurora // The SR of the cloud service to be connected.
  ToService: minirds-maotai // The service of the cloud service to be
connected.
  ToUser: root
```

3. Verify that the SSH tunnel has been opened.
i. Log on to the bcmc.Bcmc# container.

|   | cat MINIRDS.py \| grep "CURRENT IP LIST" _ _ |
|---|---|
| /home/admin/bcmc/config |   |

shown in the following figure. iii. Run the `ssh <IP address>` command to check whether the IP addresses obtained in the previous step can be reached.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

##### 2.2.5.4 sync_check (SLB)

This alert is used to check the disaster recovery (DR) status of Server Load Balancer (SLB) DR instances. This alert is triggered if an anomaly is found during the DR inspection of SLB. This may cause failover failures and affect traffic forwarding. This topic describes the sync_check alert item of SLB.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | slb | An anomaly is reported in the Apsara Stack Resilience (ASR) for Zone- disaster Recovery console during the DR inspection of SLB. | Once a minute |

**Supported versions**

Apsara Stack V3.12 and later

**Causes**

SSH tunnels are closed. The SSH tunnels from bcmc to the server roles (SRs) of cloud services may be closed due to reasons such as missing or incorrect baseline configurations of SSH tunnels and issues in tianji-sshtunnel. In this case, DR inspection scripts cannot be executed as expected. The SSH tunnels from bcmc to the slb-controller.SlbControlMaster# containers in the primary and secondary data centers must be open. Otherwise, an error is reported. The number of abnormal instances detected is not 0. The issue occurs because the instance settings in the Linux Virtual Server (LVS) on the forwarding plane are inconsistent with the recorded settings in the control database. You must troubleshoot abnormal instances.

**Alert impacts**

If the DR status of SLB is abnormal, the following issues may occur: Instances cannot be failed over. Traffic cannot be forwarded as expected, and the cloud services or applications that depend on SLB cannot run as expected.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Closed SSH tunnels**

1. Check whether the sshd process of the peer SLB service is started.
i. Log on to the SLB container. ii. Run the ps -ef|grep sshd command to view the sshd process. If the ssh process is not started, you can manually run the `/usr/sbin/sshd` command to start the sshd process. If the sshd process does not exist in the container, install the sshd plug-in by running the `yum install sshd` command.
2. Modify the SSH tunnel configurations of the bcmc cluster.
i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose Resources > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter bcmc in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the **Cluster Details** page, click the **Desired State Configuration** tab. v. Modify the `/services/tianji-sshtunnel-` `client/user/SSHTunnelClient/ssh_tunnel_bcmc.conf` file. Add the following information to the file: FromProduct, FromClusterType, FromServerRole, FromService, FromUser, ToProduct, ToClusterType, ToServerRole, ToService, and ToUser. Then, submit the changes.

> **Note:** The values of the FromClusterType and FromServerRole parameters vary based on the region type. For the central region, set the FromClusterType parameter to BcmcCluster and the FromServerRole parameter to Bcmc. For general regions, set the FromClusterType parameter to Bcmc4GeneralCluster and the FromServerRole parameter to Bcmc4General. Sample code:

```
- FromProduct: bcmc
  // FromClusterType: Bcmc4GeneralCluster // Note: For the central region, set
the parameter to BcmcCluster. For general regions, set the parameter to Bcmc4Ge neralCluster.
  // FromServerRole: Bcmc4General // Note: For the central region, set the para
meter to Bcmc. For general regions, set the parameter to Bcmc4General.
  FromClusterType: BcmcCluster
  FromServerRole: Bcmc
  FromService: bcmc
  FromUser: root
  ToProduct: slb // The cloud service to be connected.
  ToClusterType: slb_controller_Cluster // The type of the service cluster to b
e connected.
  ToServerRole: SlbControlMaster // The SR of the service to be connected.
  ToService: slb-controller // The service of the cloud service to be
connected.
  ToUser: root
```

3. Verify that the SSH tunnel has been opened.
i. Log on to the bcmc.Bcmc# container.

|   | cat SLB.py \| grep "slb control master iplist" _ _ _ |
|---|---|
| /home/admin/bcmc/config |   |

controller.SlbControlMaster#, as shown in the following figure. iii. Run the `ssh <IP address>` command to check whether the IP addresses obtained in the previous step can be reached.

**Abnormal instances**

1. Troubleshoot health check issues.
i. Log on to the slb-controller. SlbAg# container. ii. Run the following command to run the health check script. The main health check script is stored in the `/deploy/alimonitor/script` path.

```
python checkHealth.py
```

iii. Check the `/home/slb/ag/slb-test_run.log` log, find the error information, and check the keyword that caused the health check failure.
2. Troubleshoot abnormal load balancers.
i. Log on to the xuanyuan database. ii. Run the following command to check the information about abnormal load balancers. Check whether the load balancers of northbound data are in an abnormal state, such as provisioning, init, or configuring, and whether the current and target version numbers are inconsistent.

```
select * from loadbalancer where current_version != target_version or (status not i n ("active", "deleted")) limit 100;
```

iii. Run the following command to check whether southbound data is generated. Check whether the southbound data is in the Created state.

```
select * from network_conf where instance_id like '%lb_global_id%' \G
```

iv. Run the following command to check whether binding data is generated. Check the status of LvsGroup and lvs.

```
select * from network_conf_binding where network_conf_instance_id like "%xxxx%" \G
```

> **Note:** In the command, replace xxxx with the instance IDs in the network_conf table.

v. Run the following command to check the events:

```
select * from event where source_instance_id like '%lb_global_id%' \G
```

Print the tree of an event by using the request ID of the event.

```
info admin detail_event event_id ${instance_id}
```

If northbound data exists but network_conf and binding data does not exist, load balancers have failed to be created and the configurations are not delivered to the southbound interface. If northbound data and network_conf data exist but binding data does not exist, load balancers have been created but the configurations are not delivered to the forwarding device. If northbound data exists and network_conf and binding data also exists, load balancers have been created and the configurations have been delivered to the forwarding device.
3. Troubleshoot abnormal virtual IP addresses (VIPs).
i. Log on to the xuanyuan database. ii. Run the following command to check the information about abnormal VIPs: Check whether the VIPs of northbound data are in an abnormal state, such as configuring_fail, configuring, stopping, stopping_fail, starting, or starting_fail, and whether the current and target version numbers are inconsistent

```
select * from vip where current_version != target_version or (status not in ("runni ng","stopped")) limit 100;
```

iii. Run the following command to check whether southbound data is generated. Check whether the southbound data is in the Created state.

```
select * from network_conf where instance_id like '%listener_id%' \G
```

iv. Run the following command to check whether binding data is generated. Check the status of LvsGroup and lvs.

```
select * from network_conf_binding where network_conf_instance_id like "%xxxx%" \G
```

> **Note:** In the command, replace xxxx with the instance IDs in the network_conf table.

v. Run the following command to check the events:

```
select * from event where source_instance_id like '%listener_id%'\G
```

Print the tree of an event by using the request ID of the event.

```
info admin detail_event event_id ${instance_id}
```

If northbound data exists but network_conf and binding data does not exist, VIPs have failed to be created and the configurations are not delivered to the southbound interface. If northbound data and network_conf data exist but binding data does not exist, VIPs have been created but the configurations are not delivered to the forwarding device. If northbound data exists and network_conf and binding data also exists, VIPs have been created and the configurations have been delivered to the forwarding device.
4. Contact SLB O&M engineers to resolve the issue.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

##### 2.2.5.5 sync_check (Kafka)

This alert monitors the disaster recovery status of Kafka disaster recovery instances. It indicates that the Kafka disaster recovery inspection is abnormal, which may cause data loss, prevent instance switchover, or result in instance access exceptions. This document describes the sync_check alert information when the alert product is Kafka.

**Alert properties**

| Alert ID | Metric name | Source | Severity | Alert product | Trigger conditions | Execution cycle |
|---|---|---|---|---|---|---|
| sync check _ | sync check _ | Bcmc# | P2 | kafka | Kafka disaster recovery inspection exception in the ASR console | Once every minute |

**Applicable versions**

Apsara Stack Enterprise V3.16 and later

**Alert causes**

The current Kafka cluster has not been configured for disaster recovery. You need to complete the disaster recovery configuration for the Kafka cluster.

**Alert impacts**

Abnormal Kafka disaster recovery status may cause: Data synchronization is not configured between primary and secondary nodes, which may cause data loss when the primary node fails. The instance cannot perform disaster recovery switchover. Instance access exceptions, causing applications that depend on this instance to run abnormally.

**Handling methods**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Confirm the error message**

In the ASR console **Platform Monitoring** > **Product Monitoring** page, the Kafka **Disaster**
**Recovery Capability**monitoring item shows**No disaster recovery instance**, and the
**Primary Node Location** is **Not Retrieved**.

**Prerequisites**

The environment requires at least 2 Kafka clusters and 2 Replicators, and must meet the following conditions: The 2 Kafka clusters must be distributed in different data centers (different AZs) for primary and secondary nodes. The 2 Replicators must be distributed in different data centers (different AZs) for primary and secondary nodes. The Kafka clusters must first successfully create VIPs, and the VIP types of the two Kafka clusters that need disaster recovery configuration must be consistent. The VIP type can be AnyTunnel or SingleTunnel. If you create a SingleTunnel VIP, you need to ensure that both Kafka clusters select the same VPC.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Middleware > ApsaraMQ for Kafka**.
3. Go to the **Message Queue For Apache Kafka** page, and confirm that the instances meet
the prerequisites in the **Instance List** in the left menu bar.
4. In the **Disaster Recovery Cluster List** in the left menu bar, create a disaster recovery
instance. i. Click **Create Disaster Recovery Cluster**. ii. Enter the **Disaster Recovery Cluster Name** and click **Next**. iii. Select the primary Kafka cluster instance in **Source Kafka Instance**, select the primary Replicator instance in **Source KafkaReplicator Instance**, and click **Next**. iv. Select the secondary Kafka cluster instance in **Target Kafka Instance**, select the secondary Replicator instance in **Target KafkaReplicator Instance**, and click **Create**.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

##### 2.2.5.6 sync_check (Elasticsearch)

This alert monitors the disaster recovery status of Elasticsearch disaster recovery instances. It indicates an abnormality in the Elasticsearch disaster recovery inspection, which may result in data loss, inability to perform disaster recovery switchover, or instance access exceptions. This document describes the sync_check alert information when the alert product is Elasticsearch.

**Alert properties**

| Alert ID | Metric | Source | Severity | Alert product | Trigger conditions | Execution cycle |
|---|---|---|---|---|---|---|

| sync check _ | sync check _ | Bcmc# | P2 | elasticsear ch | Elasticsear ch disaster recovery inspection exception on the ASR console | Once every minute |
|---|---|---|---|---|---|---|

**Applicable versions**

Apsara Stack Enterprise V3.16 and later

**Alert causes**

The current Elasticsearch cluster has not been configured for disaster recovery. You need to complete the disaster recovery configuration for the Elasticsearch cluster.

**Alert impacts**

Elasticsearch disaster recovery status is abnormal, which may lead to: Data synchronization is not configured between primary and secondary nodes, which may cause data loss when the primary node fails. The instance cannot perform disaster recovery switchover. Instance access anomalies, causing applications that depend on this instance to run abnormally.

**Solutions**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

**Confirm the error message**

On the ASR console **Platform Monitoring** > **Product Monitoring** page, the disaster recovery status monitoring for Elasticsearch is abnormal.

**Prerequisites**

You need to create a user named asr_es in the Apsara Uni-manager Operations Console and grant the elasticsearch_read role permission to this user.

**Procedure**

1. Use the asr_es user to log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation** > **Big Data** > **Elasticsearch**.
3. Go to the **ESSEN** console, in the left navigation bar, click **Instance Management**, and
then click **Create Instance**.
4. On the **Basic Configuration** page, select a version and click **Next**.
5. On the **Cluster Configuration** page, fill in the cluster information and click **Next**.
6. On the **Network And System Configuration** page, select **Virtual Private Cloud (any**
**Tunnel)** as the network type, set the logon password, and click **Start Creation**.
7. Follow the above steps to create one cluster in the primary data center and one in the
secondary data center, using the same logon password.
8. On the ops1 machine, run the following command to execute the ES_ha_init.py script.

```bash
# ${masterInstance} represents the primary cluster instanceID; ${slaveInstance} repre
sents the secondary cluster instanceID; ${masterNamespace} represents the namespace o f the primary cluster; ${slaveNamespace} represents the namespace of the secondary cl uster; ${masterIDC} represents the primary data center IDC name; ${slaveIDC} represents the secondary data center IDC name; ${UserDomain} represents the user-defined domain name used to access the ES cluster /home/tops/bin/python ES_ha_init.py -mi ${masterInstance} -si ${slaveInstance} -mn ${ masterNamespace} -sn ${slaveNamespace} -md ${masterIDC} -sd ${slaveIDC} -d ${UserDoma in} Example: /home/tops/bin/python ES_ha_init.py -mi es-a -si es-b -mn xdcr-test-a -sn xd cr-test-b -md amtest17 -sd amtest34 -d es-visit.xdcr-test.intra.env11e.shuguang.com
```

|   | Note Script usage notes: An instance that has already been set as a secondary cluster is not allowed to be set as a primary cluster instance. Domain names that are already bound to an IP address are not allowed to be used by default. You can add the -f parameter to force the use of the specified domain name. To query the current list of disaster recovery instances: /home/tops/bin/python ES ha init.py -a list . _ _ After the incremental deployment of the ES disaster recovery service, if no ES disaster recovery instance has been created, the ASR disaster recovery inspection page may report an error. You can execute the command /home/tops/bin/python ES ha init.py -a init to trigger the initialization of the _ _ datasource config for the relevant database. |
|---|---|
|   | ES ha init.py -a list _ _ |

**Notes**

It is not allowed to create indexes that start with "." or "security-auditlog" (this type of index will not be synchronized). Deleting an index in the secondary data center will trigger synchronization, so it cannot be deleted. However, if an index is deleted in the primary data center, the corresponding index in the secondary data center will also be deleted. The client is required to set the DNS cache to be as short as possible (not exceeding 10 seconds). During power outage failback, you need to perform the following command in the primary data center (before the power outage) to enable the synchronization link and trigger data synchronization in advance, to avoid being blocked in the data synchronization stage during disaster recovery switchover.

```bash
# Enable synchronization link (you can verify on ASR whether the data synchronization
link is configured successfully) ${masterInstance} represents the primary cluster ins tanceID; ${user} represents the secondary cluster instance username; ${password} repr esents the secondary cluster instance password; ${slaveClusterMgmtVip} represents the management domain name of the secondary cluster instance curl -XPOST -u ${user}:${password} ${slaveClusterMgmtVip}:9200/_xdcr/${masterInstance}?excludes=.*,security-auditlog* Kibana white screen operation (primary cluster before power outage): POST /_xdcr/${masterInstance}?excludes=.*,security-auditlog*
# Check data synchronization progress (when the data in the third and fourth columns
of the query result are consistent, it indicates that data synchronization is complet e) ${user} represents the secondary cluster instance username; ${password} represents the secondary cluster instance password; ${slaveClusterMgmtVip} represents the manage ment domain name of the secondary cluster instance curl -u ${user}:${password} ${slaveClusterMgmtVip}:9200/_cat/xdcr? h=repository,index,localGCP,remoteGCP Kibana white screen operation (secondary cluster): GET /_cat/xdcr?h=repository,index,localGCP,remoteGCP
```

During network outage failback, in addition to manually configuring and enabling the synchronization link in the primary data center (before the network outage), you may also need to delete the index in the primary data center to trigger a full synchronization (depending on whether partial data inconsistency between primary and secondary clusters is acceptable on site).

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.6 inspect_product_cluster_aplus

This alert is used to check whether rolling is performed on the clusters in the primary data center for zone-disaster recovery. This alert is triggered if rolling is not performed on specific clusters. This may cause failover failures.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| inspect pro _ duct cluste _ r aplus _ | inspect pro _ duct cluste _ r aplus _ | Bcmc# | P2 | bcmc | Rolling is not performed on specific clusters in the primary data center for zone- disaster recovery. | Every 30 minutes |

**Supported versions**

Apsara Stack V3.14 and later

**Causes**

Rolling is not performed on specific clusters in the primary data center. For all clusters deployed in the secondary data center, except for Elastic Compute Service (ECS) compute clusters and storage clusters, rolling must be performed on the corresponding clusters in the primary data center.

> **Note:** Rolling operations are not required for the clusters deployed only in the primary data center but not in the secondary data center.

**Alert impacts**

If zone-disaster recovery deployment of cloud services is not complete, failover operations fail.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

1. Perform rolling on the primary clusters that have a corresponding secondary cluster and on
which rolling is not performed.

> **Important:** Usage notes:
> Before you perform rolling, make sure that the primary and secondary clusters are at desired state.
> For basic middleware, including middleWareAll, dauthProduct, aliware-taokeeper, and middleware-dncs, you must perform rolling immediately after the services reach desired state.

> You must submit services for rolling based on the specified sequence.
> When rolling is performed on ApsaraMQ for RocketMQ, Object Storage Service (OSS), and Tablestore, transient disconnections occur. Before you perform rolling on these services, obtain a scheduled operation window from the customer.

Submission sequence Rolling operations are performed at the cluster level. We recommend that you submit the operations in sequence. Submit the operations for the next cluster after a success message is returned for the current submission and the rolling of the current cluster starts on Apsara Infrastructure Management. The following table lists the submission sequence for rolling operations of various clusters.

**Important**

Clusters not included in the table can be submitted after the rds clusters are submitted. The bcmc cluster is the last one to be submitted. When rolling operations are performed on MiniRDS, MiniRDS automatically issues a request to recreate secondary instances across data centers. This process does not affect data reading and writing of instances. Therefore, MiniRDS clusters can be submitted first and together with other clusters. It takes a long time to recreate secondary instances and the migration may fail. Field engineers must closely monitor the MiniRDS and ApsaraDB RDS consoles and check whether interrupted or failed migration tasks exist. Handle such tasks at the earliest opportunity.

| No. | Service | Cluster (depending on actual situations) |
|---|---|---|
| 1 | tianji | tianji-A-e68c |
| 2 | minirds-mt | integrator-A-20200212-e682 maotai-A-20200212-e681 |
| 3 | baseServiceAll | StandardCloudCluster-A |
| 4 | webappAll | StandardCloudCluster |
| 5 | vnet | VnetCluster |
| 6 | xnet2 | Xnet2Cluster |
| 7 | ram | BasicCluster |
| 8 | qitian | qitianCluster |

| 9 | opsapi | opsapiCluster |
|---|---|---|
| 10 | tongque | tongqueCluster |
| 11 | asa | asaCluster |
| 12 | aso | asoCluster |
| 13 | slb | slbCluster slb yaochi Cluster _ _ |
| 14 | vpc | vpcAzoneCluster vpcRegionCluster vpcRegionXnetCluster vpcYaochiCluster |
| 15 | ecs | ECS-controller-A-e68d ECS-controller-A-e68f |
| 16 | oss | OssHybridCluster Important If you do not want to configure zone-disaster recovery for all buckets, do not perform rolling on OSS. Contact the OSS R&D team for solutions. |
| 17 | rds | brain kvstore-yaochi maotai nosql-cleaneye pgsql ppassql proxy rds-dr-service rds-yaochi redis |
| 18 | On PaaS services | Depends on the actual On PaaS service. |
| 19 | bcmc | BcmcCluster-A |

Rolling on On Tianji services a. Log on to OPS 1 of the primary data center. b. Run the following commands to update the cluster configurations in the primary data center:

```
cd /apsarapangu/disk3/u_disk/upgrade_tools/tianji_zhuque_sdk ./upgrade_A_to_Aplus.py -z [$ZONE] -p [$PROJECT] -c [$CLUSTER] --tianjiCltConfig [$TIANJICLTCONFIG]
```

Parameter description: $ZONE: the zone of the cluster in the primary data center. $PROJECT: the name of the project of the cluster in the primary data center. $CLUSTER: the name of the cluster in the primary data center. $TIANJICLTCONFIG: the fixed directory of the tianji_clt configuration file. Sample commands:

```
cd /apsarapangu/disk3/u_disk/upgrade_tools/tianji_zhuque_sdk ./upgrade_A_to_Aplus.py -z cn-haikou-xxxx-xxxx-a -p tianji -c tianji-Ac8df --tianjiCltConfig /cloud/data/bootstrap_controller/BootstrapController#/bootstrap_controlle /tianji_dest.conf
```

Rolling on On PaaS services (earlier than V3.17) a. Download the arkctl tool. b. Run the following command to obtain all the On PaaS services in the environment:

```
arkctl product list -iz
```

c. Run the following command to check whether rolling is being performed on a service:

```
arkctl product rolling ${id}
```

> **Note:** id indicates the service ID. Service IDs are obtained in the previous step.

d. Run the following command to check whether the service is in the Ready state:

```
arkctl product list -iz
```

If the service is in the Ready state, deployment is successful. Rolling on On PaaS services (V3.17 and later) a. Download the arkctl tool. b. Run the following command to obtain all the On PaaS services in the environment:

```
arkctl product list -iz
```

c. Run the following command to check whether the value of the haApsaraStack variable is `true` . If the value is true, a success message is returned. If the value is `false` , perform rolling on the service.

```
arkctl dr aplus ${id}
```

> **Note:** id indicates the service ID. Service IDs are obtained in the previous step.

2. Check whether rolling is performed as required. The list of services on which rolling is not
performed is expected to be empty.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.7 inspect_product_cluster_version

This alert is used to check whether service versions are consistent between the primary and secondary data centers. This alert is triggered if service versions are inconsistent between the primary and secondary data centers. This may cause failover failures or feature changes in the cloud services after failover.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|

| inspect pro _ duct cluste _ r version _ | inspect pro _ duct cluste _ r version _ | Bcmc# | P2 | bcmc | Service versions are inconsisten t between the primary and secondary data centers. | Every 30 minutes |
|---|---|---|---|---|---|---|

**Supported versions**

Apsara Stack V3.14 and later

**Causes**

In the zone-disaster recovery scenario, service versions must be consistent between the primary and secondary data centers. Otherwise, an exception is reported.

**Alert impacts**

If service versions are inconsistent, the following issues may occur: Failover operations fail. After the failover, the features of cloud services change.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

For cloud services with different versions deployed in the primary and secondary data centers, contact the technical account manager (TAM) to upgrade the services.

#### 2.2.8 inspect_product_variable

This alert is used to check whether the bcmc-dependent baseline variables that are obtained by using the tianji API are inconsistent with the baseline variables rendered by bcmc. This alert is triggered if the obtained and rendered baseline variables are inconsistent. This may cause failover failures.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|

| inspect pro _ duct varia _ ble | inspect pro _ duct varia _ ble | Bcmc# | P2 | bcmc | The Apsara Stack Resilience (ASR) console shows that the service baseline variable check fails. | Every 30 minutes |
|---|---|---|---|---|---|---|

**Supported versions**

Apsara Stack V3.14 and later

**Causes**

Due to the upgrade or scale-out of cloud services, or the migration of cloud services, the bcmc-dependent baseline variables that are obtained by using the tianji API are inconsistent with the baseline variables rendered by bcmc.

> **Note:** For more information about the bcmc-dependent baseline variables that are obtained by the tianji API, see the `application-conf-opposite.yml` and
> `application-conf.yml` files in the `/opt/tianji/conf.tmpl` directory.
> For more information about baseline variables rendered in bcmc, see the

```
 /alidata/conf/antx.properties  file.
```

**Alert impacts**

Failover operations fail.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

If a service has been scaled out, the baseline variables of bcmc are changed. In this case, you must perform rolling on bcmc and re-render the baseline variables. i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources** > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter bcmc in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the **Cluster Details** page, click the **Desired State Configuration** tab. v. In the kv.conf file, press the Enter key at the end of the last line, and then click**Preview**
**and Submit**.
vi. In the dialog box that appears, click **Submit**. If bcmc should have obtained the variables of a service cluster in the secondary data center but obtained the variables of the corresponding cluster in the primary data center instead, the service may have been incrementally deployed recently. You need to check the serviceid.conf configuration file of the bcmc cluster and delete the corresponding configurations. i. Log on to the Apsara Infrastructure Management console. ii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources** > **Product & Cluster O&M**. iii. On the Product & Cluster O&M page, enter bcmc in the search box. In the search results, find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. iv. On the **Cluster Details** page, click the **Desired State Configuration** tab. v. Delete the configurations of the corresponding service in the serviceid.conf file.

> **Note:** If the alert persists after you perform the preceding steps, submit a ticket to contact technical support.

#### 2.2.9 inspect_product_cluster_deploy

This alert is used to check whether the clusters of cloud services are deployed in symmetric mode in the primary and secondary data centers. This alert is triggered if a cloud service is not deployed in symmetric mode. This may cause failover failures, exceptions in accessing the service, or excessive load on the service.

**Alert attributes**

| Alert ID | Metric | Alert source | Alert level | Service | Trigger condition | Check interval |
|---|---|---|---|---|---|---|
| inspect pro _ duct cluste _ r deploy _ | inspect pro _ duct cluste _ r deploy _ | Bcmc# | P2 | bcmc | The clusters of cloud services are not deployed in symmetric mode in the primary and secondary data centers. | Every 30 minutes |

**Supported versions**

Apsara Stack V3.14 and later

**Causes**

In the zone-disaster recovery scenario, if you want to configure disaster recovery (DR) for a service that does not support asymmetric DR, make sure that the service version is consistent and clusters are deployed in symmetric mode between the primary and secondary data centers. Otherwise, an exception is reported.

> **Note:** The following services support asymmetric DR: ApsaraDB RDS, KVStore for Redis, Object Storage Service (OSS), Elastic Compute Service (ECS), and MaxCompute.

**Alert impacts**

If clusters are not deployed in symmetric mode as required, the following issues may occur: Failover operations fail. After the failover, the service cannot be accessed as expected. After the failover, the service is overloaded.

**Solution**

> **Warning:** If a solution requires that you modify product configurations, you must initiate a production change process to confirm the feasibility and standardization of the solution. Even in an emergency, you must obtain consent from the customer and TAM before you can perform any steps of the solution.

Contact the field technical account manager (TAM) to check whether the service is correctly deployed. If the service is incorrectly deployed, deploy new clusters and check the inspect_product_cluster_deploy item again. If the service is correctly deployed, ignore the exception.

#### 2.2.10 Appendixes

##### 2.2.10.1 Log on to the Apsara Uni-manager Management Console

**Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

2. Enter your username and password.

> **Note:** You need to obtain the username and password from an operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios:

**This is your first time logging on to the Apsara Uni-manager Management**

**Console after MFA is enabled by the administrator.**

a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**.

**You have enabled MFA and bound an MFA device.**

Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For information about how to bind and enable MFA, see Manage MFA.

**What to do next**

**Forget password**

1. If you forget the logon password, click **Forgot Password** below the Password field.
2. On the Forgot Password page, configure the **Account Name** and **Email Address**
parameters, specify the verification code, and then click **Confirm**.

> **Note:** Enter the username of your account in the Account Name field and the email address that was used to create the account in the Email Address field.
> The system sends a link for resetting the password to the email address that you specify.

##### 2.2.10.2 Log on to the Apsara Uni-manager Operations Console

**Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A web browser. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and Traditional Chinese are supported.

3. Enter your username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from the deployment engineer or an administrator.

If you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.

##### 2.2.10.3 Log on to a container

This topic describes how to log on to a container. The Bcmc# container of bcmc is used in this example.

**Procedure**

1. Log on to the terminal.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. On the **Product & Cluster O&M** page, enter bcmc in the search box. v. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. vi. On the Services tab, find the **bcmc** service and click its name. vii. In the Components pane, click **Bcmc#**. On the **Instances** tab, click **Terminal** in the
**Actions** column of an instance.
2. Run the following command to query the ID of the container:

```bash
docker ps
```

3. Run the following command to access the container:

```bash
docker exec -it <Container ID> /bin/bash.
```

##### 2.2.10.4 Log on to the xuanyuan database

This topic describes how to log on to the xuanyuan database of Server Load Balancer (SLB).
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the Product & Cluster O&M page, enter slb in the search box. In the search results, find
slbCluster-A and click **Cluster Details** in the **Actions** column.
5. On the Services tab, find the **slb-controller** service and click its name.
6. In the Components pane, click **SlbControlMaster#**.
7. On the **Resources** tab, find the resource whose name is **xuanyuan** and type is **db**, and
view the values of the db_host, user, db_password, db_port, and db_name parameters in the **Resource Application Result** column.
8. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance.
9. Run the following command to log on to the xuanyuan database. For more information
about the values of the db_host, user, db_password, db_port, and db_name parameters, see Step 7.

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

##### 2.2.10.5 Log on to the Apsara Infrastructure Management console

**Management console**

This topic describes how to log on to the Apsara Infrastructure Management console as a user such as an O&M engineer.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: region-id.ops.asconsole.intranet-domain-id. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni-manager Operations Console from a deployment engineer or an administrator.

If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log On**.
5. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **Resources**.

##### 2.2.10.6 Secondary database rebuild

This topic describes how to rebuild a secondary database to help you better understand the process.

**Procedure**

1. . View the basic information, link type, port, and primary**

**database IP information of the abnormal instance**

1. Log on to the Dukang database management platform.
2. Select **Instance Management** > **Instance List**, and click the instance that you want to
operate to go to the instance details page. If the link type is DNS, log on to the host where the instance is located and run the following command to check whether the parsing is correct. If the parsing fails, contact the product development team for assistance.

```
dig ${domain name}
```

If the link type is LVS, confirm whether the data center IP information is consistent with the primary instance machine IP. If they are inconsistent, stop the operation and contact the product development team for assistance.
2. . Check the read_only parameter of the primary and**

**secondary databases**

1. Log on to the primary database. For more information, see Log on to an abnormal instance.
2. Run the following SQL statement to check the read/write status of the primary database.
i. When the result shows ON, the primary database is abnormal.

```
 show variables like 'read_only';
```

ii. Run the following SQL statement to set the read_only parameter to OFF.

```
 set global read_only = 0;
```

3. Log on to the secondary database.
4. Run the following SQL statement to check the read/write status of the secondary database.
i. When the result shows OFF, the secondary database is abnormal.

```
 show variables like 'read_only';
```

ii. Run the following SQL statement to set the read_only parameter to ON.

```
 set global read_only = 1;
```

3. . Implementation**
1. Log on to the Dukang database management platform.
2. Select **Instance Management** > **Instance List**, and click the instance that you want to
operate.
3. Select **Backup Policy** > **Create Temporary Backup**. In the dialog box that appears,
select **FULL** > **Primary Database Physical Backup** > **Click To View** > **OK**.

> **Note:** The database must not contain MyISAM tables.

4. Click **Backup And Recovery** and confirm that you can see the temporary backup of the
primary database, which indicates that the backup is complete. (This can be completed within 18 hours)
5. At the bottom of the **Basic Information** page, click **Rebuild [Secondary Database**
**Rebuild|Node Rebuild]**. In the dialog box that appears, select **Force Primary Database**
**Backup**, select the corresponding host, and select the rebuild method.

> **Note:** Local rebuild means rebuilding on the host where the original secondary database is located, and cross-machine rebuild means selecting a different host.

6. Click **Submit**.
7. Click **Task Management** and monitor the task progress until the task is complete.
If tasks fail, contact the product and R&D team for assistance.
8. Log on to the abnormal instance.
9. Run the following SQL statement and check the returned result.

```
show slave status\G
```

The system displays a result similar to the following, indicating that the rebuild is successful.

##### 2.2.10.7 Log on to an abnormal instance

This topic describes how to log on to an abnormal instance.

**Procedure**

1. Log on to the ApsaraDB Operations and Maintenance System console.
2. In the left-side navigation pane, choose **Instance management** > **Instance List**. Find the
abnormal instance and click its name to go to the instance details page.
3. In the **Host instance information** section, view and record the hostname, IP address, and
port number of the abnormal instance.
4. Log on to the Apsara Infrastructure Management console.
5. In the left-side navigation pane, choose Resources > Product & Cluster O&M. Find the
cluster that you want to manage and click Cluster Details in the Actions column. On the Machines tab, enter the hostname in the Hostname/IP Address field and click **Terminal** in the search results to manage the abnormal node.
6. Run the following command to log on to the abnormal instance:

```python
sudo my ${port}
```

> **Note:** If you are the root user, you do not need to add `sudo` to the command.

The following figure shows a sample output.
7. If `mysql>` is displayed, you have logged on to the abnormal instance.

## 3 Cloud service O&M operations

**operations**

### 3.1 TianJi

#### 3.1.1 Check the desired state

This topic describes how to check whether services are at desired state in the Apsara Infrastructure Management console and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the **Product & Cluster O&M** page, check whether services in the primary and
secondary data centers are at desired state.

**Expected results**

The number of services that are not at desired state is zero.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

### 3.2 DNS

#### 3.2.1 Check data consistency

This topic describes how to check the consistency of Apsara Stack DNS data and the expected results.

**Procedure**

1. Check the consistency of dnsslave data in the primary data center.
i. Log on to the DnsSlave service container on Terminal Server 1 or Terminal Server 2 in the primary data center. ii. Copy the script localIdc_slave_and_slave_compare.py to the `/root/opsbuild/tools/dataConsistCheck/` directory and run the following command to check the data consistency between Terminal Server 1 and Terminal Server 2 in the primary data center:

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_slave_and_slave_compare.py
```

2. Check the data consistency between etcd and dnsslave in the primary data center.
i. Log on to the ops.OpsDnsSlave# service container in the primary data center. ii. Copy the script localIdc_etcd_and_slave_compare.py to the `/root/opsbuild/tools/dataConsistCheck/` directory and run the following command to check the data consistency between etcd and dnsslave in the primary data center:

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_etcd_and_slave_compare.py
```

3. Check the data consistency between etcd clusters in the primary and secondary data
centers. i. Log on to the ops.OpsDnsSlave# service container in the primary or secondary data center. ii. Copy the script masterIdcEtcd_and_secondIdcEtcd_compare.py to the `/root/opsbuild/tools/dataConsistCheck/` directory and run the following command to check the data consistency between etcd clusters in the primary and secondary data centers:

```
python /root/opsbuild/tools/dataConsistCheck/masterIdcEtcd_and_secondIdcEtcd_compare.py
```

4. Check the data consistency between etcd and dnsslave in the secondary data center.
i. Log on to the ops.OpsDnsSlave# service container in the secondary data center. ii. Copy the script localIdc_etcd_and_slave_compare.py to the `/root/opsbuild/tools/dataConsistCheck/` directory and run the following command to check the data consistency between etcd and dnsslave in the secondary data center:

```
python /root/opsbuild/tools/dataConsistCheck/localIdc_etcd_and_slave_compare.py
```

**Expected results**

1. The following figure shows a sample command output. The number of resource records
(RRs) in the current zone queried from Terminal Server 1 is the same as that queried from Terminal Server 2.

> **Note:** In the command output, rr stands for resource records.
> If the number of RRs in the current zone queried from Terminal Server 1 is inconsistent with that queried from Terminal Server 2, the difference is highlighted in the format of rr:{'ops1':[],'ops2':[]}.
> bcmc-minirds-check is the test domain name of Apsara Stack Resilience (ASR) for Zone-disaster Recovery. If the difference in bcmc-minirds-check is returned and highlighted in the command output, ignore it.

2. The following figure shows a sample command output. The number of RRs in the current
zone queried from the etcd cluster, that queried from Terminal Server 1, and that queried from Terminal Server 2 are the same.

> **Note:** If the number of RRs queried from the etcd cluster is inconsistent with that queried from Terminal Server 1, the difference is highlighted in the format of rr:{'ops1':[],'etcd': []}.

3. The following figure shows a sample command output. The number of RRs in the current
zone queried from the etcd clusters is the same.

> **Note:** If the number of RRs queried from the etcd clusters is inconsistent, the difference is highlighted in the format of rr:{'FirstEtcd':[],'SecondEtcd':[]}.

4. The following figure shows a sample command output. The number of RRs in the current
zone queried from the etcd cluster, that queried from Terminal Server 1, and that queried from Terminal Server 2 are the same.

> **Note:** If the number of RRs queried from the etcd cluster is inconsistent with that queried from Terminal Server 1, the difference is highlighted in the format of rr:{'ops1':[],'etcd': []}.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.2.2 Check the domain name resolution service

**service**

This topic describes how to check whether Apsara Stack DNS can resolve IP addresses and the expected results.

**Procedure**

Run the `dig +short dnsapi1.tbsite.net` command on Terminal Server 1 and Terminal Server 2 in the primary and secondary data centers to check whether an IP address can be resolved.

**Expected results**

The IP address is correctly resolved.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

### 3.3 MiniRDS

#### 3.3.1 Check tasks

This topic describes how to check the status of MiniRDS tasks and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Management and control**

**service operation and maintenance > ApsaraDB Operations and Maintenance**

**System (Lite)**.
3. In the left-side navigation pane, click **Task Management**. On the Task Management page,
select **Interrupted tasks**, **Waiting tasks**, **Temporarily Closed tasks**, **Suspended**
**tasks**, and **Running tasks** in turn from the drop-down list in the upper-left corner and
view the task details.

**Expected results**

No task is displayed when you select **Interrupted tasks**, **Waiting tasks**, **Temporarily**
**Closed tasks**, **Suspended tasks**, and **Running tasks**.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.3.2 Check the DR status of instances

This topic describes how to check the disaster recovery (DR) status of MiniRDS instances and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Management and control**

**service operation and maintenance > ApsaraDB Operations and Maintenance**

**System (Lite)**.
3. In the left-side navigation pane, click **System Management**.
4. In the left-side pane of the **System Management** page, choose **Disaster Recovery**
**Management** > **Disaster recovery switching**. In the instance list, check the instance
status.

**Expected results**

For every instance except dbaas_db, **OK** is displayed in the **Instance available** and
**Switchable** columns, and the value in the **Maximum Latency from library** column is
greater than or equal to 0 and less than 60. For every instance, **Read and write** is displayed in the **Master database information** column and **Read only** is displayed in the **From Library Information** column.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.3.3 Check the status of instances

This topic describes how to check the status of MiniRDS instances and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Management and control**

**service operation and maintenance > ApsaraDB Operations and Maintenance**

**System (Lite)**.
3. In the left-side navigation pane, choose **Instance management** > **Instance List**. In the
instance list, sort instances by the **CPU**, **QPS**, **Connections**, and **Disk Usage** columns in turn to view instance information.

**Expected results**

The values in the **CPU**, **QPS**, **Connections**, and **Disk Usage** columns of all instances are less than or equal to 50%.

> **Note:** If the results are not as expected, we recommend that you perform scale-outs based on your business requirements. You can also submit a ticket to contact Alibaba Cloud technical support.

### 3.4 ApsaraDB RDS

#### 3.4.1 Check tasks

This topic describes how to check the status of ApsaraDB RDS tasks and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, click **Task Management**. On the Task Management page,
select **Interrupted tasks**, **Waiting tasks**, **Temporarily Closed tasks**, **Suspended**
**tasks**, and **Running tasks** in turn from the drop-down list in the upper-left corner and
view the task details.

**Expected results**

No task is displayed when you select **Interrupted tasks**, **Waiting tasks**, **Temporarily**
**Closed tasks**, **Suspended tasks**, and **Running tasks**.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.4.2 Check the DR status of instances

This topic describes how to check the disaster recovery (DR) status of ApsaraDB RDS instances and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, click **System Management**.
4. In the left-side pane of the **System Management** page, choose **Disaster Recovery**
**Management** > **Disaster recovery switching**. In the instance list, check the instance
status.

**Expected results**

For every instance, **OK** is displayed in the **Instance available** and **Switchable** columns, and the value in the **Maximum Latency from library** column is greater than or equal to 0 and less than 60.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.4.3 Check the status of instances

This topic describes how to check the status of ApsaraDB RDS instances and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Databases > ApsaraDB**
**Operations and Maintenance System**.
3. In the left-side navigation pane, choose **Instance management** > **Instance List**. In the
instance list, sort instances by the **CPU**, **QPS**, **Connections**, and **Disk Usage** columns in turn to view instance information.

**Expected results**

The values in the **CPU**, **QPS**, **Connections**, and **Disk Usage** columns of all instances are less than or equal to 50%.

> **Note:** If the results are not as expected, we recommend that you perform scale-outs based on your business requirements. You can also submit a ticket to contact Alibaba Cloud technical support.

### 3.5 SLB

#### 3.5.1 Check the status of LVSs

This topic describes how to check the status of Linux virtual servers (LVSs) and the expected results.

**Procedure**

1. Log on to the slb-controller.SlbAg# container.
2. Run the following command on the CLI:

```
list admin lb_node
```

**Expected results**

All values in the **configuration** column are **Enabled**, and all values in the **online_status** column are **online**.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.5.2 Check the status of proxies

This topic describes how to check the status of proxies and the expected results.

**Procedure**

1. Log on to the slb-controller.SlbAg# container.
2. Run the following command on the CLI:

```
list admin proxy
```

**Expected results**

All values in the **configuration** column are **Enabled**, and all values in the **online_status** column are **online**.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.5.3 Check the status of keyservers

This topic describes how to check the status of keyservers and the expected results.

**Procedure**

1. Log on to the slb-controller.SlbAg# container.
2. Run the following command on the CLI:

```
list admin keyserver
```

**Expected results**

All values in the **status** column are **online**.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

### 3.6 OSS

#### 3.6.1 Check bucket locations

This topic describes how to check whether all buckets are in the location of the primary data center and the expected results.

**Procedure**

1. Log on to the oss_meta database.
2. Execute the select cluster,location from location_table; statement to query the
clusters in the location of the primary data center.
3. Execute the `select name,location from oss_meta_bucket where location <>"{Primary data`
center location}"; statement to query the buckets that are not in the location of the primary data center.

**Expected results**

No result is found.

> **Note:** If no result is found, all buckets are in the location of the primary data center.
> If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

### 3.7 ECS

#### 3.7.1 Check the status of NCs

This topic describes how to check the status of node controllers (NCs) and the expected results.

**Procedure**

1. Log on to the houyi-reg database of Elastic Compute Service (ECS).
2. Execute the select id,ip,status,hostname,biz_status from nc; statement to query the
status of all NCs.

**Expected results**

All values in the biz_status column are free.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

### 3.8 ASO

#### 3.8.1 Check the traffic

This topic describes how to check the status and traffic of network device ports, and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Product Operation > Networking > Network**
**Operations Console**.
3. In the left-side navigation pane, choose **Basic Network** > **Network Element**
**Management**.
4. In the device list, click the name of the inter-connection switch (ISW) or micro switch (MSW)
that you want to manage.
5. View the management and operation status of ports.
6. Click a port name to view the port traffic.

**Expected results**

The management and operation status of all ports are **Up** and traffic is normal.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

#### 3.8.2 Check alerts

This topic describes how to view alerts in the Apsara Uni-manager Operations Console and the expected results.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Monitor&Alarms > Alarm Management > Alarm**
**Overview**.
3. View the alert details.

**Expected results**

No alert is displayed.

> **Note:** If the results are not as expected, troubleshoot the issue or submit a ticket to contact Alibaba Cloud technical support to fix the issue.

## 4 FAQ

### 4.1 What do I do if VIPs in the secondary data center are abnormal?

**secondary data center are**

**abnormal?**

This topic describes how to view the IP addresses recorded in the primary and secondary data centers and how to handle exceptions.

**Problem description**

The virtual IP addresses (VIPs) in the secondary data center are abnormal. Some nodes can be reached by PING messages, whereas others cannot be reached by PING messages and related VIPs cannot be found during service O&M.

**Cause**

The number of IP addresses displayed in the value of the nc_list parameter on the Resource Dashboard page of the Apsara Infrastructure Management console is greater than the number of real server IP addresses displayed in the Apsara Stack Resilience (ASR) for Zonedisaster Recovery console. The number of IP addresses displayed in the value of the nc_list parameter on the Resource Dashboard page of the Apsara Infrastructure Management console is less than the number of real server IP addresses displayed in the ASR for Zone-disaster Recovery console. The number of IP addresses displayed in the value of the nc_list parameter on the Resource Dashboard page of the Apsara Infrastructure Management console is the same as the number of real server IP addresses displayed in the ASR for Zone-disaster Recovery console. The comparison result is abnormal.

**Solution**

1. View the IP addresses in the ASR for Zone-disaster Recovery console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Disaster recovery**
**management > ASR for Zone-disaster Recovery (Secondary Zone)**.
iii. In the left-side navigation pane, choose **Platform Check > Environment Check**. iv. In the **VIP Resources** section, find the resource named **remotemock** and move the pointer over the value in the **RealServer IP** column.
2. View and record the IP addresses on the Resource Dashboard page.
i. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
ii. In the left-side navigation pane, choose **O&M Tools > Resource Dashboard**. iii. On the **Resource Dashboard** page, select **Cluster** from the drop-down list, enter ECS in the search box, and then click the icon. iv. Find the service to which the remotemock resource belongs and whose type is vip in the Name column, and click the eye icon in the Result column. Click the value that appears to view the IP addresses in the value of the nc_list parameter. If the number of IP addresses displayed in the value of the nc_list parameter in the Apsara Infrastructure Management console is greater than the number of IP addresses that ASR for Zone-disaster Recovery queries from Server Load Balancer (SLB), check whether the excess IP addresses belong to the service in the Apsara Infrastructure Management console. If so, add the excess IP addresses to SLB. If the number of IP addresses displayed in the value of the nc_list parameter in the Apsara Infrastructure Management console is less than the number of IP addresses that ASR for Zone-disaster Recovery queries from SLB, check whether the missing IP addresses belong to the service in the Apsara Infrastructure Management console. If so, an error has occurred in resource application. Contact the team of Apsara Infrastructure Management to troubleshoot the issue. If the number of IP addresses displayed in the value of the nc_list parameter in the Apsara Infrastructure Management console is the same as the number of IP addresses that ASR for Zone-disaster Recovery queries from SLB, contact the team of the service in which the exception occurs to troubleshoot the issue.
3. Add real servers.

**Warning**

Before you add or remove real servers, you must confirm the operation with the team of the service or the customer to which the VIPs belong. If the operation is confirmed and approved, the operation generally does not impact business. However, if the operation is not expected but performed, the business may be interrupted. After the operation is confirmed and approved, contact the SLB team to help add or remove real servers.

**Verify the results**

1. Log on to the Apsara Uni-manager Operations Console.
2.
3. In the left-side navigation pane, choose **Platform Check > Environment Check**.
4. In the **VIP Resources** section, check whether the value in the **Comparison Result** column
is Normal. If the comparison result is normal, the issue is resolved.

| If the comparison result is abnormal, contact the team of the service in which the |   |
|---|---|
| exception occurs to troubleshoot the issue. |   |

## 5 Appendixes

### 5.1 View ASR logs

This topic describes the directories in which the logs of Apsara Stack Resilience (ASR) for Zone-disaster Recovery are stored and how to view the logs.

**Procedure**

1. Log on to the bcmc.Bcmc# container.
2. Obtain the directory of the log file that you want to view from the following table.

| Log file | Description |
|---|---|
| /home/admin/bcmc/logs/error.log | Stores bcmc error logs. |
| /home/admin/bcmc/logs/info.log | Stores bcmc run logs. |
| /home/admin/bcmc/logs/scripts/script.log | Stores the run logs of bcmc scripts. |
| /home/admin/bcmc/scripts/{Service name}/logs/{Service name} synccheck.log _ | Stores the script inspection logs of a service. |
| /home/admin/bcmc/scripts/{Service name}/logs/{Service name} switch.log _ | Stores the switchover logs of a service. |

> **Note:** A log file whose name does not contain a date stores the logs generated for the current day.

3. View logs. In this example, bcmc error logs are viewed.
i. Run the `cd /home/admin/bcmc/logs/` command to go to the directory in which the logs are stored. ii. Run the `ll` command to query all files in the directory. iii. Run the `vim error.log` command to query the error log details. iv. Run the `/2022-12-15 00:04:03` command to query the log details at the specified time.

> **Note:** Replace the time based on your business requirements.

v. Run the `:q` command to exit the log details page.

### 5.2 Log on to a container

This topic describes how to log on to a container. The Bcmc# container of bcmc is used in this example.

**Procedure**

1. Log on to the terminal.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
iii. In the left-side navigation pane of the **Apsara Infrastructure Management console** , choose **Resources > Product & Cluster O&M**. iv. On the **Product & Cluster O&M** page, enter bcmc in the search box. v. Find the cluster that you want to manage and click **Cluster Details** in the **Actions** column. vi. On the Services tab, find the **bcmc** service and click its name. vii. In the Components pane, click **Bcmc#**. On the **Instances** tab, click **Terminal** in the
**Actions** column of an instance.
2. Run the following command to query the ID of the container:

```bash
docker ps
```

3. Run the following command to access the container:

```bash
docker exec -it <Container ID> /bin/bash.
```

### 5.3 Log on to the tianji-sshtunnel database

**database**

This topic describes how to log on to the tianji-sshtunnel database.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the Product & Cluster O&M page, enter tianji in the Product | Cluster field. Find the
primary cluster and click **Cluster Details** in the **Actions** column.
5. On the Services tab, find the **tianji-sshtunnel** service and click its name.
6. In the Components pane, click **SSHTunnelMaster#**.
7. On the **Resources** tab, find the resource whose name is **sshtunnel** and type is **db** and
view the values of the db_host, user, db_password, db_port, and db_name parameters in the **Resource Application Result** column.
8. On the **Instances** tab, find an instance and click **Terminal** in the **Actions** column.
9. Run the following command to log on to the tianji-sshtunnel database. For more information
about the values of the db_host, user, db_password, db_port, and db_name parameters, see Step 7.

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 5.4 Log on to the oss_meta database

**database**

This topic describes how to log on to the oss_meta database. 1.LogontotheApsaraUni-managerOperationsConsole.
1. Log on to the Apsara Unimanager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the Product & Cluster O&M page, enter oss in the search box. In the search results, find
the primary cluster and click **Cluster Details** in the **Actions** column.
5. On the Services tab, find the **oss-ocm-server** service and click its name.
6. In the Components pane, click **DBInit#**.
7. On the **Resources** tab, find the resource whose name is **oss_meta** and type is **db**, and
view the values of the db_host, user, db_password, db_port, and db_name parameters in the **Resource Application Result** column.
8. On the **Instances** tab, click **Terminal** in the **Actions** column of an instance.
9. Run the following command to log on to the oss_meta database. For more information
about the values of the db_host, user, db_password, db_port, and db_name parameters, see Step 7.

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 5.5 Log on to the houyi-reg database

**database**

This topic describes how to log on to the houyi-reg database of Elastic Compute Service (ECS).
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > Resources**.
3. In the left-side navigation pane of the **Apsara Infrastructure Management console** ,
choose **Resources > Product & Cluster O&M**.
4. On the Product & Cluster O&M page, enter ecs in the Product | Cluster field. Find the ECS-
controller-A cluster and click **Cluster Details** in the **Actions** column.
5. On the Services tab, find the **ecs-houyi** service and click its name.
6. In the Components pane, click**Regionmaster#**.
7. On the **Resources** tab, find the resource whose name is **houyi_reg** and type is **db** and
view the values of the db_host, user, db_password, db_port, and db_name parameters in the **Resource Application Result** column.
8. On the **Instances** tab, find an instance and click **Terminal** in the **Actions** column.
9. Run the following command to log on to the houyi_reg database. For more information
about the values of the db_host, user, db_password, db_port, and db_name parameters, see Step 7.

```
mysql -h${db_host} -u${user} -p${db_password} -P${db_port} -D${db_name}
```

### 5.6 Resolve configuration inconsistency between the primary and secondary tables

**inconsistency between the primary**

**and secondary tables**

This topic describes how to resolve configuration inconsistency between the primary and secondary tables, such as the inconsistency in the MaxVersions, time to live (TTL), and Stream configurations.

**Background information**

**Inconsistency in the MaxVersions or TTL configuration**

This inconsistency is generally caused because you modify the MaxVersions or TTL configuration after you create a table and during business operation. If the MaxVersions or TTL configured for the primary cluster is smaller than that configured for the secondary cluster, more data is stored in the secondary cluster. A TTL value of -1 specifies that data never expires. In this case, you can directly modify the MaxVersions or TTL configuration of the secondary cluster. If the MaxVersions or TTL configured for the primary cluster is greater than that configured for the secondary cluster, incomplete data is stored in the secondary cluster. A TTL value of -1 specifies that data never expires. In this case, you must decide whether to perform full synchronization or directly modify the MaxVersions or TTL configuration of the secondary cluster.

**Inconsistency in the Stream configuration**

This inconsistency is generally caused because the Stream feature is enabled for the primary cluster for incremental export tasks and disabled for the secondary cluster. In this case, you can directly enable the Stream feature for the secondary cluster.

**Prerequisites**

The following operations are complete:
1. Log on to the TableStore.PortalAgServer# terminal server of the ots cluster.
2. Decompress the new_ots_replication_tool.tar.gz package as the admin user.

**Procedure**

1. Go to the `new_ots_replication_tool` directory.
2. Run the following command to modify the configurations of the secondary cluster:

> **Note:** You must specify an instance name and a table name in the command. You can modify the configurations of one table each time. Only the configurations of the secondary cluster are modified. The configurations of the primary cluster are not affected.

```
./rep_checker.py sync_table_meta_for_secondary Instance name Table name
```

Sample output:

```
$./rep_checker.py sync_table_meta_for_secondary lt-ots-test00 test001 secondary cluster: ots-ssd-B-20210813-00a6, table: _tBTC6DyGWKYBrHKstl#test001, set T TL to 86400000 OK!
```
