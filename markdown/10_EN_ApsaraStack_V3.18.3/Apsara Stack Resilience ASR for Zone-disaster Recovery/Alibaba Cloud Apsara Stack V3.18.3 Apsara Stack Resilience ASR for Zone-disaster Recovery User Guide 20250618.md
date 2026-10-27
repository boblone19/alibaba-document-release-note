---
title: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Zone-disaster Recovery User Guide 20250618"
product_version: "V3.18.3"
doc_version: "20250618"
pdf_pages: 109
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Zone-disaster Recovery User Guide 20250618.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E7%81%BE%E5%A4%87%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Apsara%20Stack%20Resilience%20ASR%C2%A0for%C2%A0Zone-disaster%C2%A0Recovery%20User%20Guide%2020250618.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Apsara Stack Resilience ASR for Zone-disaster Recovery User Guide 20250618

## Table of Contents

- 1 ASR introduction
  - 1.1 What is Apsara Stack Resilience for Zone-disaster Recovery?
  - 1.2 Deployment modes
  - 1.3 Features
- 2 Log on to the ASR console
- 3 Overview
- 4 Platform monitoring
  - 4.1 Usage scenarios
  - 4.2 Monitor products
  - 4.3 Synchronization monitoring
  - 4.4 Use the ASR dashboard
- 5 Platform check
  - 5.1 Check an environment
  - 5.2 Check products
- 6 Disaster recovery drills
  - 6.1 Usage notes
  - 6.2 Drill plans
    - 6.2.1 Custom virtual drills
    - 6.2.2 Predefined drills
  - 6.3 View the drill history
- 7 Disaster recovery
  - 7.1 Disaster recovery
    - 7.1.1 Power outage recovery in the primary data center
      - 7.1.1.1 Failover for power outages of the primary data center
      - 7.1.1.2 Failback for power outages of the primary data center
    - 7.1.2 Network outage recovery in the primary data center
      - 7.1.2.1 Failover for network outages of the primary data center
      - 7.1.2.2 Failback for network outages of the primary data center
    - 7.1.3 Single-service fault recovery
      - 7.1.3.1 Failover for single-service outages
      - 7.1.3.2 Failback for single-service outages
    - 7.1.4 Recovery from power outages or split-brain scenarios of the secondary data center
  - 7.2 Fault simulation
    - 7.2.1 Fault simulation for two data centers-based zone disaster recovery
      - 7.2.1.1 Preparations
      - 7.2.1.2 Apply for an authentication code
      - 7.2.1.3 Check the environment
      - 7.2.1.4 Inject a power outage
        - 7.2.1.4.1 Inject a power outage
        - 7.2.1.4.2 Recover a data center after failovers for power outages
      - 7.2.1.5 Network outage of data centers
        - 7.2.1.5.1 Inject a network outage
        - 7.2.1.5.2 Recover a data center after failovers for network outages
      - 7.2.1.6 Split-brain scenario
        - 7.2.1.6.1 Inject a split-brain scenario
        - 7.2.1.6.2 Recover the environment after failovers for split-brain scenarios
      - 7.2.1.7 Single-product failure
        - 7.2.1.7.1 Inject a single-service outage
        - 7.2.1.7.2 Recover a data center after failovers for single-service outages
    - 7.2.2 Fault simulation for three data centers-based zone disaster recovery
      - 7.2.2.1 Preparations
      - 7.2.2.2 Apply for an authentication code
      - 7.2.2.3 Check the environment
      - 7.2.2.4 Inject a power outage
        - 7.2.2.4.1 Inject a power outage
        - 7.2.2.4.2 Recover a data center after failovers for power outages
      - 7.2.2.5 Network outage of data centers
        - 7.2.2.5.1 Inject a network outage
        - 7.2.2.5.2 Recover a data center after failovers for network outages
      - 7.2.2.6 SPOFs
        - 7.2.2.6.1 Inject a single-connection failure
        - 7.2.2.6.2 Recover the environment after the switchover for the single-connection failure
      - 7.2.2.7 Single-product failure
        - 7.2.2.7.1 Inject a single-product failure
        - 7.2.2.7.2 Recover a data center after failovers for single-service outages
  - 7.3 View the recovery history
- 8 System settings
  - 8.1 Arbitration management
  - 8.2 Alert management
    - 8.2.1 Create an alert rule
    - 8.2.2 Modify an alert rule
    - 8.2.3 View alert records
  - 8.3 Manage leased lines
  - 8.4 Password change
  - 8.5 User management
    - 8.5.1 Add a user
    - 8.5.2 Enable or disable authentication
    - 8.5.3 Delete user information
  - 8.6 Authentication configuration
  - 8.7 Data backup
- 9 Protection groups
  - 9.1 Protection group overview
  - 9.2 Protection group process
    - 9.2.1 Process overview
    - 9.2.2 Create a protection group
    - 9.2.3 Protection group drills
      - 9.2.3.1 Create a drill plan
      - 9.2.3.2 Drill process
    - 9.2.4 Disaster recovery
      - 9.2.4.1 Create a disaster recovery plan
      - 9.2.4.2 Disaster recovery process
- 10 Appendix
  - 10.1 Encryption and backup
  - 10.2 How to obtain the endpoint of ASR for Zone-disaster Recover

## 1 ASR introduction

### 1.1 What is Apsara Stack Resilience for Zone-disaster Recovery?

**Resilience for Zone-disaster**

**Recovery?**

Apsara Stack Resilience (ASR) for Zone-disaster Recovery consists of a primary site and a secondary site. The primary and secondary sites are deployed in the same region but in different zones. This deployment method is used to combat local disasters with a small impact. ASR for Zone-disaster Recovery is adopted on all core cloud products such as networking, cloud computing, database, storage, middleware, and big data products. This can be used in cross-AZ deployment for high availability. When a disaster occurs, your business can be quickly failed over to a secondary AZ. The service domain names of the cloud products remain unchanged. ASR for Zone-disaster Recovery can be deployed in two or three data centers in the same region.

### 1.2 Deployment modes

This topic describes the deployment modes of Apsara Stack Resilience (ASR), which can be deployed in two data centers or three data centers. ASR does not rely on other cloud services. When a data center fails, ASR still provides services. Services can be failed over to ensure business continuity. An ASR system is deployed in each of the primary and secondary data centers to handle different data center-level failures. Two data centers-based zone-disaster recovery: ASR in the primary data center provides services when the secondary data center encounters power and network outages. ASR in the secondary data center provides services when the primary data center fails due to power and network outages and split-brain scenarios. Three data centers-based zone-disaster recovery: ASR in the primary data center handles power and network outages of the secondary data center. ASR in the secondary data center handles power and network outages of the primary data center. Failures of the network links between data centers and the quorum data center failures do not need to be handled. Figure 1. Architecture for ASR deployed in two data centers Figure 2. Architecture for ASR deployed in three data centers

### 1.3 Features

This topic describes the ASR for Zone-disaster Recovery features that the primary and secondary data centers support and the roles used to implement these features. The following table describes the features that the primary and secondary data centers support and the roles used to implement these features.

| Category | Feature | Primary data center | Secondary data center | Role |
|---|---|---|---|---|
| Overview | - | Supported | Supported | Basic O&M Advanced O&M System administrator |
| Platform monitoring | Product monitoring | Supported | Supported | Basic O&M Advanced O&M System administrator |
|   | Synchronization monitoring | Not supported | Supported |   |
|   | ASR dashboard | Not supported | Supported |   |
| Platform check | Environment check | Supported | Supported | Basic O&M Advanced O&M System administrator |
|   | Product check | Supported | Supported |   |
|   | Application for an authentication code | Supported | Supported |   |
|   | Health check | Supported | Supported |   |
|   | Injection of power outages into the primary data center | Not supported | Supported |   |
|   | Injection of power outages into the secondary data center | Supported | Not supported |   |
|   | Injection of network outages into the primary data center | Supported | Not supported |   |

| Fault simulation |   |   |   | Advanced O&M System administrator |
|---|---|---|---|---|
|   | Injection of network outages into the secondary data center | Supported | Not supported |   |
|   | Injection of split- brain scenarios (available only in two data centers-based zone-disaster recovery) | Supported | Not supported |   |
|   | Injection of single-product failures | Supported | Supported |   |
|   | Injection of single- connection failures (available only in three data centers-based zone-disaster recovery) | Supported | Supported |   |
|   | Data center recovery | Supported | Supported |   |
| Disaster recovery drill | Switchover of business by product | Not supported | Supported | Advanced O&M System administrator |
| Disaster recovery | Recovery from split-brain scenarios or secondary data center failures | Supported | Not supported | Advanced O&M System administrator |
|   | Recovery from power outages | Not supported | Supported |   |
|   | Recovery from network outages | Not supported | Supported |   |
|   | Recovery from single-product failures | Not supported | Supported |   |
| 1 | > Docume |   |   | nt Version: 2025061 |

|   | Switchback | Not supported | Supported |   |
|---|---|---|---|---|
|   | Alert management | Supported | Supported | Basic O&M Advanced O&M |
| System settings |   |   |   | System administrator |
|   | Password change | Supported | Supported | Basic O&M Advanced O&M System administrator |
|   | User management | Supported | Supported | System administrator |
|   | Arbitration management | Supported | Supported | System administrator |
|   | Authentication setting | Supported | Supported | Basic O&M Advanced O&M System administrator |
|   | Leased line management | Supported | Supported | Basic O&M Advanced O&M System administrator |
|   | Data synchronization | Supported | Supported | System administrator |
|   | Data backup | Supported | Supported | Advanced O&M System administrator |

nsole

## 2 Log on to the ASR console

ASR for Zone-disaster Recovery provides three logon methods for routine O&M, escape logon, and tenant operation scenarios.

> **Note:** In subsequent documents, the ASR for Zone-disaster Recovery console is referred to as the ASR for Zone-disaster Recovery console.

**Prerequisites**

For routine O&M scenarios, the URL of the Apsara Uni-manager Operations Console and the username and password that are used to log on to the console are obtained from the deployment engineers or an administrator. The URL of the Apsara Uni-manager Operations Console is in the following format: <region-i d>.ops.console.<intranet-domain-id>. For escape logon scenarios, the URL of the ASR for Zone-disaster Recovery console and the username and password that are used to log on to the console are obtained from the deployment engineers or an administrator.

**Note**

If the primary data center fails, you must log on to the ASR console of the secondary data center. If the secondary data center fails, you must log on to the ASR console of the primary data center. The domain names of the two data centers are different. The URL of the ASR for Zone-disaster Recovery console for the secondary data center is in the following format: asr-xs-<region-id>.console.<intranet-domainid>.com/user/login. The URL of the ASR for Zone-disaster Recovery console for the primary data center is in the following format: asr-xm-<region-id>.console.<intranet-domainid>.com/user/login. For tenant operation scenarios, the URL of the Apsara Uni-manager Management Console is obtained from the deployment engineers.

**Routine O&M scenarios**

To perform routine monitoring and inspections on services and environments in the ASR for Zone-disaster Recovery console, you can log on to the Apsara Uni-manager Operations Console first and click the link to go to the ASR console. If you log on as the **System**
**Administrator** role, you can perform platform monitoring, platform check, and virtual drill
tasks. If you log on as the **Product Devops** role, you can perform platform monitoring and platform check tasks.
1. Open your browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the ENTER key. nsole

> **Note:** You can click the current language in the upper-right corner to switch to another language. Simplified Chinese, English, and traditional Chinese are supported.

3. Enter the username and password.

> **Note:** Obtain the username and password that are used to log on to the Apsara Uni- manager Operations Console from a deployment engineer or an administrator.

If you enter an invalid password for three consecutive times, the system enables the image verification logon feature. If you enter an invalid password for five consecutive times, the account is locked. Contact the administrator to activate the account. If this is the first time you log on to the Apsara Uni-manager Operations Console, you must change the password as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains at least one of the following special characters: ! @ # $ % The password is 10 to 20 characters in length.
4. Click **Log In**.
5. In the top navigation bar, choose **Platform > Disaster Recovery > ASR for Zone-**
**disaster Recovery (Primary Data Center)**.
6. In the top navigation bar, choose **Platform > Disaster Recovery > ASR for Zone-**
**disaster Recovery (Secondary Data Center)**.
nsole

**Escape logon scenarios**

To use disaster recovery features such as fault simulation and disaster recovery, follow these steps to log on to the ASR console:
1. In the address bar of your browser, enter the URL of the ASR for Zone-disaster Recovery
console and then press Enter.

**Note**

If the primary data center fails, you must log on to the ASR console of the secondary data center. If the secondary data center fails, you must log on to the ASR console of the primary data center. The domain names of the two data centers are different. The URL of the ASR for Zone-disaster Recovery console for the secondary data center is in the following format: asr-xs-<region-id>.console.<intranet-domainid>.com/user/login. The URL of the ASR for Zone-disaster Recovery console for the primary data center is in the following format: asr-xm-<region-id>.console.<intranet-domainid>.com/user/login.

> **Note:** You can click the language drop-down in the upper-right corner to switch between languages. Simplified Chinese, English, and Traditional Chinese are supported.

2. Enter the username and password that are used to log on to the ASR console.

> **Note:** Obtain the username and password that are used to log on to the ASR for Zone-disaster Recovery console from the deployment engineers or an administrator.

3. Click **Log On**.

**Tenant operation scenarios**

To restore a single service by application and perform disaster recovery drills, you can log on to the Apsara Uni-manager Management Console and create a protection group. nsole
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.

> **Note:** You can click the current language in the upper-right corner to switch to another language.
> The Authorized Login button is displayed only when a global IdP is configured in third-party authentication. You can customize the name of the Authorized Login button based on your requirements.

2. Enter your username and password.

> **Note:** Obtain the username and password for the Apsara Uni-manager Management Console from the operations administrator.
> The first time you log on to the Apsara Uni-manager Management Console, you must change your account password as prompted. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

3. Click **Account Logon**.
4. If your account has multi-factor authentication (MFA) enabled, perform the corresponding
operations in the following scenarios: nsole

**First logon after the administrator enforces MFA**

a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter your account and password as described in Step 2, and click **Account Login**. c. Enter the 6-digit MFA code and click **Authenticate**.

**You have enabled and bound MFA**

Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For more information about how to bind and enable MFA, see Manage multi-factor authentication.
5. In the top navigation bar, select **Products**.
6. In the left-side navigation pane, click **Disaster Recovery and Backup**.
7. In the **Disaster Recovery and Backup** section, choose **Disaster Recovery > ASR for**
**Zone-disaster Recovery**.

## 3 Overview

The Overview page displays the overall disaster recovery capabilities. It allows you to understand the disaster recovery capabilities of your platform more intuitively and quickly. After you log on to the ASR for Zone-disaster Recovery console, you can have a general understanding of the disaster recovery capabilities of your ASR platform. You can view the status of the secondary data center and the network traffic between data centers, predict the duration and results of forced switchovers, and view the usage records of the platform.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-
disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. On the **Overview** page, you can view information such as the status of the data centers,
network traffic between data centers, forced switchover predictions, and instance synchronization status.

> **Note:** The preceding figure is an example of three data centers. The specific content displayed varies with the disaster recovery mode, and the dimensions of the displayed information are the same. The content displayed depends on your actual environment.
> After arbitration management is enabled, the system continuously monitors the data center status. In the event of a data center failure, the system automatically performs a switchover. You can view the disaster recovery records in the console.

The following table describes the information in each section of the preceding figure.

| Section | Description |
|---|---|
| Data Center Status | Displays the role of each data center (primary, secondary, or third), the number of servers in each data center, the name of each data center, and the disaster recovery distribution of product clusters across the data centers. You can click View to go to the Product Monitoring page to view the distribution of products in the data centers and the inspection results. For more information, see Monitor products. |
| Network Traffic Between Data Centers | Displays traffic information within the most recent monitoring period. Click View Details to view the network traffic in the last 1 hour or last 24 hours. Each line indicates a leased line. If No Traffic is displayed on the network cables between data centers, you are navigated to the leased line management page. You need to configure the information about the leased lines. Note The leased line information configured in the system affects the network traffic between data centers. |
| Expected Forced Switchover for Platform | Displays the duration and trend of the forced switchover predicted for the cloud platform. |
| Expected Forced Switchover for Single Product | Displays the predicted durations and results of forced switchovers for all products. The results of forced switchovers can be Succeeded, Failed, Risky, and Timeout. Succeeded: indicates that the forced switchovers of all products will be successful. Failed: indicates that some monitoring items directly lead to the failures of forced switchovers. Risky: indicates that certain monitoring items may affect forced switchovers. Timeout: indicates that the duration of a forced switchover is longer than the predicted duration. |
| Instance Synchronization Status | Displays the RPO information of all instances, including the number of normal instances and the number of abnormal instances (synchronization timeout and synchronization interrupted). |
| Instance Synchronization Details | Displays the instances with continuous abnormal RPO within a week. The displayed instance information includes the instance name, sampling time, and synchronization latency. By default, instances are listed in descending order of synchronization latency. |

| Usage Records | Displays the current disaster recovery capabilities, the last drill (switchover) information, the last alert/monitoring check time, and the disaster recovery usage. Current Disaster Recovery Capabilities: displays the number and proportion of services that have not been switched, and displays the names of the services that have never been switched over. Last Drill (Switchover) Information: displays the number of products participating in the last switchover drill and the time since the last switchover drill. Disaster Recovery Usage (Forced Switchover): displays the usage records of disaster recovery, including the number of forced switchovers of the data center and the number of forced switchovers of a single product. |
|---|---|

## 4 Platform monitoring

### 4.1 Usage scenarios

This topic describes the usage scenarios of platform monitoring and precautions.

**Features**

Platform monitoring consists of three parts: product monitoring, synchronization monitoring, and ASR dashboard. These parts support the following features and check items: The Product Monitoring page displays the disaster recovery mode, service status in the primary, secondary, and quorum data centers, synchronization component status, and failover capabilities by product. The Synchronization Monitoring page displays the data synchronization latency compliance rates of databases and storage products. The ASR Dashboard page allows you to view the metrics of overall business continuity, such as the data synchronization latency compliance rates, drill duration, product status, and recent disaster recovery drills.

**Scenarios**

Routine monitoring: During the daily operations of the cloud platform, you need to regularly inspect various check items. Check before drills: Before switchover and switchback drills, you need to check platform monitoring information. Ensure that monitoring items do not have exceptions.

**Note**

For some products, you need to perform inspections in addition to the product monitoring check. Contact the ASR R&D team to perform inspections before a drill.

### 4.2 Monitor products

Before a switchover or switchback, the total number of products and the number of exceptions are counted by service type. The information about each product, node locations of base components, feature status, and inspection results are displayed in cards. If a product or base component is in an abnormal state, fix the issue before performing the switchover or switchback.

**View the status of products**

Before products are switched over or back, you must check whether the status of the products is normal. If exceptions exist, the **Disaster recovery conditions are not**
**provided for the current product.** message appears when you switch over or back the
products. Switch over or back the products after the exceptions are resolved.
1. Log on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Primary Zone)
console or the ASR for Zone-disaster Recovery (Secondary Zone) console. In the left-side navigation pane, choose **Monitoring > Product Monitoring**.
2. On the **Product Monitoring** tab, check whether abnormal products exist. Click the name
of a product whose status is abnormal to go to the corresponding card in the lower part of the page. The card displays the node location, feature status, and inspection results.
3. Select the product type, product name, primary service location, and product status from
the drop-down lists to filter the monitoring items that meet the conditions. Common exceptions and solutions: SSH tunnel exceptions exist: Check whether products have been deployed and reached the desired state in Apsara Infrastructure Management. If the products are not deployed or have not reached the desired state, resolve this exception first. If the exception persists after the products are deployed and reach the desired state, submit a ticket. ApsaraDB RDS instances that have synchronization latencies exist, and running tasks exist: Log on to ApsaraDB Operations and Maintenance System and check the synchronization status and the task execution status of the instances. The recovery point objective (RPO) of Tablestore is not 0: Reduce the number of requests. Wait 20 minutes for the RPO to recover. If the RPO does not recover over an extended period of time, submit a ticket. The primary or secondary service fails: Check whether products have been deployed and reached the desired state in Apsara Infrastructure Management. If the products are not deployed or have not reached the desired state, resolve this exception at your earliest opportunity. If the exception persists after the products are deployed and reach the desired state, submit a ticket.

**View the status of base components**

Before products are switched over or back, you must check whether the status of the base components is normal. If exceptions exist, the **Disaster recovery conditions are not**
**provided for the current product.** message appears when you switch over or back the
products. Switch over or back the products after the exceptions are resolved.
1. Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-
disaster Recovery (Secondary Zone) console. In the left-side navigation pane, choose
**Monitoring > Product Monitoring**.
2. On the **Base Monitoring** tab, check whether abnormal base components exist. Click the
name of a product whose status is abnormal to go to the corresponding card in the lower part of the page. The card displays the node location, feature status, and inspection results.
3. Select the product name, primary service location, and product status from the drop-down
lists to filter the monitoring items that meet the conditions. Common exceptions and solutions: SSH tunnel exceptions exist: Check whether products have been deployed and reached the desired state in Apsara Infrastructure Management. If the products are not deployed or have not reached the desired state, resolve this exception first. If the exception persists after the products are deployed and reach the desired state, submit a ticket. MiniRDS instances that have synchronization latencies exist, and running tasks exist: Log on to ApsaraDB Operations and Maintenance System and check the synchronization status and the task execution status of the instances. The primary or secondary service fails: Check whether products have been deployed and reached the desired state in Apsara Infrastructure Management. If the products are not deployed or have not reached the desired state, resolve this exception at your earliest opportunity. If the exception persists after the products are deployed and reach the desired state, submit a ticket.

### 4.3 Synchronization monitoring

You can view the Data Synchronization Latency Compliance Rate, Instances with Successful Synchronization, Instances with Synchronization Exceptions, and the Synchronization Latency for instances of ApsaraDB RDS, KVStore for Redis, and OSS.
1. Log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.
2. In the left-side navigation pane, choose **Monitoring** > **Synchronization Monitoring**. The
synchronization monitoring information is displayed. The instances that have synchronization exceptions are displayed in red.

> **Note:** **RDS Monitoring** monitors multiple database services, including ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, PolarDB, and ApsaraDB RDS for PPAS.
> Choose **Settings** > **Alerts** > **Alert Rules** and modify the **Triggering** **Threshold** of the **Data Loss** metric of a product to change the alert threshold.

The following table describes the features that you can use on the Synchronization Monitoring page.

| Feature | Description |
|---|---|
| Data Synchronization Latency Compliance Rate | Displays the percentage of cloud products whose synchronization latency meets the RPO. If the percentage is not 100%, check the instances whose status is Data Synchronization Interrupted or Data Synchronization Timeout and resolve the issue. |
| Search | You can select a specific cloud product and search for a specific instance to view the synchronization information. You can select Instance ID, Instance Name, Current Location, Instance Engine, or Status from the drop-down list. Select Instance ID from the drop-down list, enter an instance ID in the search box, and then click . Select Instance Name from the drop-down list, enter an instance name in the search box, and then click . Select Current Location from the drop-down list, and then select a data center name. The system automatically filters data that meets the conditions. Select Instance Engine from the drop-down list, and then select an instance engine. The system automatically filters data that meets the conditions. Note You can search instances by instance engine only for ApsaraDB RDS. Select Status from the drop-down list, and then select a status, which can be Normal or Abnormal. You can click Advanced Filter to combine multiple query dimensions for search. |

| View instance synchronization information | Click in the Actions column to view the instance synchronization information (RPO) in the last 24 hours, last 6 hours, and last 1 hour. Click in the Actions column to hide the line chart of instance synchronization information. |
|---|---|

### 4.4 Use the ASR dashboard

You can view the metrics of overall business continuity, such as the data synchronization latency compliance rates, drill duration, product status, and recent disaster recovery drills on the Apsara Stack Resilience (ASR) dashboard.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more
information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Monitoring > ASR Dashboard**.

## 5 Platform check

### 5.1 Check an environment

You can check an environment to obtain information such as the versions of services that support disaster recovery (DR), product baselines, Domain Name System (DNS) resources, virtual IP address (VIP) resources, and database resources. After an environment is deployed, you can check the environment to verify that all check items meet DR conditions.
1. Log on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Primary Zone)
console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Platform Check > Environment Check**.
3. On the **Environment Check** page, click **Check Now** in the upper-right corner of each
section to view corresponding check items. Check item descriptions:
**Product Configuration Upgrade**: After services are redeployed or service
configurations are upgraded, rolling must be performed on the services in the primary data center so that ASR can obtain the latest configurations of the data center. Check whether the list of products with configuration upgrades is consistent with the products that are redeployed or whose configurations are upgraded.
**Cluster Deployment**: displays whether products are deployed in symmetric mode,
based on which you can learn about the clusters where the products are deployed.

> **Note:** Feature in yellow: This feature is deployed in asymmetric mode but is not required for the secondary cluster. This information can be ignored.
> Feature in red: This feature is deployed in asymmetric mode and is required for the secondary cluster. You need to resolve the issue.

**Product Version**: ASR checks whether the versions of products are consistent between
the primary and secondary data centers. If the versions are inconsistent, ASR shows that the products are abnormal. You must upgrade the product versions to ensure that the versions are the same between the primary and secondary data centers. This way, failover failures caused by inconsistent product versions are prevented.
**Product Baseline**: ASR checks whether the baseline configurations in the environment
are the same as the baseline configurations in Apsara Infrastructure Management. The information shown in the following figure indicates that the baseline check passed. If abnormalities appear, check related configurations.
**DNS Resources**: ASR obtains the DNS resource information of services from Apsara
Infrastructure Management. Then, ASR obtains a VIP that maps a domain name from the resource information, and compares the actual VIP with the VIP obtained from the resource information in Apsara Infrastructure Management. If the two VIPs are inconsistent, the value of the **Comparison Result** column is **Abnormal**. Check and modify corresponding configurations.
**VIP Resources**: ASR obtains the VIP resource information of products from Apsara
Infrastructure Management. Then, ASR queries the actual IP address of a server that corresponds to the VIP from Server Load Balancer (SLB) based on the VIP in resource information, and compares the actual IP address of the server with the list of node controllers (NCs) in the VIP resource information. If the actual IP address and the list of NCs are inconsistent, ASR marks the corresponding RealServer IP value in red. Check and modify corresponding configurations.
**Database Resources**: ASR obtains the database resource information of products from
Apsara Infrastructure Management. Then, ASR connects to the database based on the information and checks the read-only attribute of the primary database. If the primary database is read-only, the value of the **Status** column of the service is **Abnormal** in the ASR console. Modify the configurations of the database.
**Conditions of the Network Between Data Centers** : ASR checks whether switches
can advertise routes of SLB and CIDR blocks of virtual private cloud (VPCs). If abnormalities exist, contact O&M engineers.
**BGP Route**: ASR checks whether switches can advertise routes of OPS-DNS, Apsara
Stack DNS, SLB, and VPC and whether the routes are propagated to Border Gateway Protocol (BGP) peers. If abnormalities exist, contact O&M engineers.

### 5.2 Check products

You can perform product checks to check the status of products that support disaster recovery (DR) before and after failovers and failbacks.
1. Log on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Primary Zone)
console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Platform Check > Product Check**.
3. Click **Check Now** in the upper-right corner of the **Server Load Balancer**, **OpsDNS**, or
**MiniRDS** section to check the status of each product.
If the status of a check item is Unhealthy, check the content in the Error Message column. Troubleshoot problems based on the error message. ls

## 6 Disaster recovery drills

You can perform disaster recovery drills to switch over or back services between the primary and secondary data centers when no power or network outages occur.

### 6.1 Usage notes

Disaster recovery drills are classified into two types: custom drills and predefined drills. Custom drills allow you to select one or more products to perform drills based on your needs. Predefined drills allow you to select all products or a single product to perform drills.

**Overview**

Zone-disaster recovery drills are an important part of the delivery acceptance and periodic inspection of the disaster recovery platform. By performing disaster recovery drills on a regular basis, you can test the capabilities of the disaster recovery platform to handle major issues and improve the disaster recovery response mechanism. If any problems occur during a drill, contact the Apsara Stack disaster recovery R&D team immediately to solve the problems, thereby avoiding affecting the normal operation of your business.

### 6.2 Drill plans

Drill plans are divided into plans for custom drills and predefined drills based on the type of drill. You can create a drill plan based on your actual needs. You can select multiple cloud products for a custom drill. After the drill is complete, the drill data is automatically aggregated and a drill report is generated. You can select a single product or all products to perform a predefined drill.

#### 6.2.1 Custom virtual drills

This topic describes how to run virtual drills to switch over services from the primary data center to the secondary data center when no power or network outages occur and how to switch back services. You can select multiple services to perform a custom drill. After the drill is complete, the drill data is automatically aggregated and a drill report is generated.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery Drill > Drill Plan**.
3. If this is your first time to open the **Drill Plan** page, view the introduction and click **View**
**Drill Plan**.

> **Note:** The next time you go to the **Drill Plan** page, the introduction is no longer displayed. To view the introduction again, click **How do I use the drill feature of Apsara Stack** **Resilience to perform disaster recovery drills?** in the upper-right corner of the **Drill Plan** page.

ls
4. Add a custom drill plan.
i. On the **Custom Drill** tab, click **Add**. ii. On the **Create Custom Drill** page, set **Drill Name**, **Service Type**, and **Drill Service**, click the icon to edit the drill scenario name, and then click **Submit**. If multiple drill scenarios are required, click **+ Add Drill Scenario** and configure the parameters. After the parameters are configured, click **Submit** to open the **Details** page. The following table describes the parameters used to create a custom drill plan.

| Parameter | Description |
|---|---|
| Drill Name | This parameter is required. It specifies the name of the drill plan. The name must be 4 to 40 characters in length and can contain letters, digits, and underscores. |

ls

| Service Type | This parameter is required. It specifies the type of service. Valid values: Database, Monitoring and O&M, Storage, Base, Middleware, and Networking. Note If you select SLB to perform the drill, the SLB service in the primary data center is disabled and the SLB service in the secondary data center is used. In this case, because the ISWs in the primary and secondary data centers use equal-cost multipath (ECMP), all outbound traffic of SLB is from the secondary data center, and the inbound traffic of the primary data center have different sources. If you need to resolve this issue, contact technical support to select an appropriate Internet-side grid connection solution. |
|---|---|
| Drill Service | The services on which you want to perform a custom drill. By default, all services are selected. You can clear the selection as needed. |

> **Note:** Click the
> or
> icon to adjust the execution order of the drill tasks.
> Click the
> icon to delete a drill task.

5. On the **Details** page, click **Start Drill** in the upper-right corner to view the drill execution
process.

> **Important:** After a drill is started, you can terminate the drill. After the drill is terminated, you cannot resume the drill.

Drill tasks are executed in the following phases.

| Stage | Description |
|---|---|

ls

| Analysis | The analysis phase includes Cloud Service Analysis, Business Application Analysis, and Network Analysis. Cloud Service Analysis: analyzes the expected switchover duration, data loss, interruption duration, and business impact based on the cloud services that are selected in the drill plan. Business Application Analysis: analyzes and checks whether the business applications of selected services meet the switchover requirements to ensure that the applications run properly after the switchover. Network Analysis: analyzes and checks whether the networking of selected services meets the switchover requirements. For example, you can check whether the network policy allows access outside the cloud and whether the disaster recovery configurations of the network outside the cloud meet your business requirements. Analyze and check whether the items meet the requirements for disaster recovery based on the disaster recovery configurations and the cloud application architecture. If the items meet the disaster recovery requirements, click Confirmed. |
|---|---|
| Preparati on | Before the switchover, the system checks the health status of disaster recovery services, including Check Disaster Recovery of Cloud Services and Check Desired State of Cloud Services. Click Start Check in the upper-right corner. After the check is complete, click Next. Note If exceptions occur, resolve the issues based on the returned exception information and then perform the switchover. |

ls

| Impleme ntation | Perform Fail Over and Fail Back for each scenario. i. On the Fail Over page, the system automatically checks the disaster recovery capability of cloud services before the switchover. If no exceptions occur, click Start Switchover. Note If exceptions occur, resolve the issues based on the returned exception information and then perform the switchover. ii. You can view the switchover logs during the switchover. After the switchover is complete, click Next. iii. On the Fail Back page, the system automatically checks the disaster recovery capability of cloud services before the switchback. If no exceptions occur, click Fail Back. Note If exceptions occur, resolve the issues based on the returned exception information and then perform the switchback. iv. You can view the switchback logs during the switchback. After the switchback is complete, click Next. |
|---|---|

ls

| Summary | After the drill tasks are complete, the drill data is aggregated and a drill report is automatically generated based on the drill results. You can click Download Report to download the report. Note The report provides detailed information about the drill including the background, objectives, plan, statistics, process, and summary of the drill. This helps you understand the drill results. |
|---|---|

> **Note:** On the **Custom Plan** page, you can view all drill plans. Click **View Details** in the **Actions** column to view the details of a drill plan. Click **Delete** in the **Actions** column to delete a drill plan. You cannot delete a drill plan in the **Executing** state.

#### 6.2.2 Predefined drills

This topic describes how to perform predefined drills to switch over services from the primary data center to the secondary data center when no power or network outages occur and how to switch back services. If you perform a predefined drill, you can select a single service or all services.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery Drill > Drill Plan**.
3. If this is your first time to open the **Drill Plan** page, view the introduction and click **View**
**Drill Plan**.
ls

> **Note:** The next time you go to the **Drill Plan** page, the introduction is no longer displayed. To view the introduction again, click **How do I use the drill feature of Apsara Stack** **Resilience to perform disaster recovery drills?** in the upper-right corner of the **Drill Plan** page.

4. On the **Predefined Plan** tab, select services to perform a drill. You can select a single
service or all services.

> **Note:** If you select SLB to perform the switchover, the SLB service in the primary data center is disabled and the SLB service in the secondary data center is used. In this case, because the ISW in the primary and secondary data centers uses ECMP, all outbound traffic of SLB is from the secondary data center, and the inbound traffic of the primary data center will have different sources. If you need to resolve this issue, contact technical support to select an appropriate Internet-side grid connection solution.

5. On the **Details** page, click **Fail Over** in the upper-right corner.
6. In the **Check Specified Service** dialog box, click **Fail Over**.

> **Note:** If you select ApsaraDB for RDS, the **Enable Engine Switchover** option appears in the dialog box. If you want to switch over a specific engine, enable this option and select the engine. If you want to switch over all engines, disable this option.
> If exceptions occur, view the service status on the **Monitoring** > **Product** **Monitoring** page and contact technical support to resolve the issues.

7. On the **Process** page, view the switchover progress and logs. In the **Result** column, view
the switchover result. ls

> **Note:** Check the status of services after the switchover. Make sure that all services meet the following requirements:
> All services are in the desired state.
> On the **Monitoring** > **Product Monitoring** page, all services are in the normal state.

8. On the **Process** page, click **Fail Back** in the upper-right corner.

> **Important:** Verify that business is switched over and services are available after the switchover. Then, switch back the instances to the primary data center.
> Business may encounter transient connection interruptions in the switchback process.

9. In the **Check Specified Service** dialog box, click **Fail Back**.

> **Note:** If you select ApsaraDB RDS for MySQL, the **Enable Engine Switchover** option appears in the dialog box. If you want to switch back a specific engine, enable this option and select the engine. If you want to switch back all engines, disable this option.
> If the service check has exceptions, view the service status on the **Monitoring** > **Product Monitoring** page and contact technical support to handle the exceptions.

0. In the **Result** column on the **Process** page, view the switchback results.
ls

> **Note:** Verify that business is switched back and services are available after the switchback. Make sure that all services meet the following requirements:
> All services are in the desired state.
> On the **Monitoring** > **Product Monitoring** page, all services are in the normal state.

1. Click **Return** In the upper-right corner to return to the Details page. You can view the drill
history of the product.

### 6.3 View the drill history

This topic describes how to view the history and results of predefined drills and custom drills.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery Drill > Drill History**.

**View custom drill records**

1. On the **Drill History** page, click the **Custom Plan** tab to view the information about
historical custom drills.
2. In the list of drill records, click the
icon to view the details of the switchover and switchback operations. ls
3. Click a drill record name or click **View Details** in the Actions column to view the detailed
execution results of the drill and download the report.
4. Move the pointer over the
icon in the **Products** column to view the cloud services that are involved in the drill.

**View predefined drill records**

1. On the **Drill History** page, click the **Predefined Plan** tab to view the information about
historical predefined drills.
2. In the list of drill records, click a drill name or click **View Details** in the **Actions** column to
view the detailed execution process of the drill.

## 7 Disaster recovery

This chapter describes how to simulate fault injection, failover, data center recovery, and failback to show how Apsara Stack Resilience (ASR) for Zone-disaster Recovery ensures business continuity and verify the disaster recovery capabilities of ASR for Zone-disaster Recovery.

**Disaster recovery process**

From the perspective of the deployment modes, zone-disaster recovery scenarios can be divided into two data centers and three data centers. The following fault scenarios may be involved:

**Fault scenarios of two data centers**

Power outage: The entire power facility of the primary or secondary data center fails, no UPS is available, and all devices are powered off. Network outage: The network devices, optical fibers, or leased lines of the primary or secondary data center for external connections are faulty. Therefore, the data center cannot communicate with external systems outside the cloud. Split-brain: The leased lines or optical fibers between the primary and secondary data centers are faulty. As a result, the primary and secondary data centers cannot communicate with each other. Single-product failure: A product in the primary or secondary data center is faulty and in the abnormal state.

**Fault scenarios of three data centers**

Power outage: The entire power facility of the primary, secondary, or quorum data center fails, no UPS is available, and all devices are powered off. Network outage: The network devices, optical fibers, or leased lines of the primary, secondary, or quorum data center for external connections are faulty. Therefore, the data center cannot communicate with external systems outside the cloud. Single-connection failure: One of the three data centers fails to communicate with the other two data centers. Single-product failure: A product in the primary, secondary, or quorum data center is faulty and in the abnormal state.

### 7.1 Disaster recovery

#### 7.1.1 Power outage recovery in the primary data center

**data center**

This topic describes how to perform platform switchover and switchback in the ASR for Zonedisaster Recovery console to ensure system continuity and reliability when power outages occur in a real primary data center.

##### 7.1.1.1 Failover for power outages of the primary data center

**data center**

This topic describes how to recover online business by starting cloud services in the secondary data center when the primary data center encounters power outages.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchover**.
3. Click the **Power Outage Recovery** tab.
4. Click **Perform Global Switchover**. In the message that appears, click **OK**.

> **Note:** If the failover fails, contact the ASR R&D team for troubleshooting.

##### 7.1.1.2 Failback for power outages of the primary data center

**data center**

This topic describes how to fail back your business to the primary data center after the primary data center is recovered from power outages.

**Prerequisites**

Your business is successfully failed over to the secondary data center. For more information, see Failover for power outages of the primary data center. The primary data center is recovered from power outages.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchback**.
3. Click the **Failback after Power Outage** tab.
4. Click **Perform Global Switchback**. In the message that appears, click **OK**.

> **Note:** If the failback fails, contact the ASR R&D team for troubleshooting.

#### 7.1.2 Network outage recovery in the primary data center

**primary data center**

This topic describes how to perform platform switchover and switchback in the ASR for Zonedisaster Recovery console to ensure system continuity and reliability when network outages occur in a real primary data center.

##### 7.1.2.1 Failover for network outages of the primary data center

**primary data center**

This topic describes how to start cloud services in the secondary data center when the primary data center is disconnected from both the Internet and the secondary data center. This ensures business continuity.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchover**.
3. Click the **Network Outage Recovery** tab.
4. Click **Perform Global Switchover**. In the message that appears, click **OK**.

> **Note:** If the failover fails, contact the ASR R&D team for troubleshooting.

##### 7.1.2.2 Failback for network outages of the primary data center

**primary data center**

This topic describes how to fail back your business to the primary data center after the primary data center is recovered from network outages.

**Prerequisites**

Your business is successfully failed over to the secondary data center. For more information, see Failover for network outages of the primary data center. The primary data center is recovered from network outages.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchback**.
3. Click the **Network Outage** tab.
4. Click **Perform Global Switchback**. In the message that appears, click **OK**.

#### 7.1.3 Single-service fault recovery

This topic describes how to perform platform switchover and switchback in the ASR for Zonedisaster Recovery console to ensure system continuity and reliability when single-service faults occur in a real data center.

##### 7.1.3.1 Failover for single-service outages

This topic describes how to recover online business by starting the corresponding service in the secondary data center when a service in the primary data center fails.

**Prerequisites**

A single-service outage is injected into the primary data center.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchover**.
3. Click the **Single-product Recovery** tab.

> **Note:** During the failover for single-service outage, the synchronization latency might be greater than 0.

4. Select the product or base for which you want to perform a switchover.
5. Click **Execute Switchover for Single Product & Base**. In the message that appears,
click **OK**.

> **Note:** If the failover fails, contact the ASR R&D team for troubleshooting.

##### 7.1.3.2 Failback for single-service outages

This topic describes how to fail back your business to the primary data center after the primary data center is recovered from single-service outages.

**Prerequisites**

Your business is successfully failed over to the secondary data center. For more information, see Failover for single-service outages. The faulty service is recovered.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Switchback.**
3. Click the **Failback after Single-Product Failure** tab.
4. Select the product or base for which you want to perform a switchback.
5. Click **Execute Switchback for Single Product & Base** . In the message that appears,
click **OK**.

> **Note:** If the failback fails, contact the ASR R&D team to locate and solve the problem.

#### 7.1.4 Recovery from power outages or split-brain scenarios of the secondary data center

**brain scenarios of the secondary data center**

This topic describes how to recover online business by starting cloud services in the primary data center when the secondary data center encounters power outages or the network communication between the primary and secondary data centers fails.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Disaster Recovery**.
3. On the **Secondary Data Center Failure** tab, click **Perform a global switch**. In the
message that appears, click **OK**. The failback operation is supported only after the failover is successful.

> **Warning:** If a split-brain scenario occurs, stop Server Load Balancer (SLB) in the secondary data center after business is failed over.

> **Note:** If the failover or failback fails, contact the ASR R&D team for troubleshooting.

### 7.2 Fault simulation

Fault simulation is a testing and verification technique used to evaluate the resilience of a cloud platform in the event of a fault or disaster. It simulates potential system faults by artificially introducing faults to observe and analyze the disaster recovery process of the cloud platform.

**Flowchart**

From the perspective of the deployment modes, zone-disaster recovery scenarios can be divided into two data centers and three data centers. The following fault scenarios may be involved:

**Fault scenarios of two data centers**

Power outage: The entire power facility of the primary or secondary data center is faulty, no UPS is available, and all devices are powered off. Network outage: The network devices, optical fibers, or leased lines of the primary or secondary data center for external connections are faulty. Therefore, the data center cannot communicate with external systems outside the cloud. Split-brain: The leased lines or optical fibers between the primary and secondary data centers are faulty. As a result, the primary and secondary data centers cannot communicate with each other. Single-product fault: A product in the primary or secondary data center is faulty and in the abnormal state.

**Fault scenarios of three data centers**

Power outage: The entire power facility of the primary, secondary, or quorum data center is faulty, no UPS is available, and all devices are powered off. Network outage: The network devices, optical fibers, or leased lines of the primary, secondary, or quorum data center for external connections are faulty. Therefore, the data center cannot communicate with external systems outside the cloud. Single-connection failure: One of the three data centers fails to communicate with the other two data centers. Single-product fault: A product in the primary, secondary, or quorum data center is faulty and in the abnormal state.

> **Note:** Fault simulation refers to manually inject fault types similar to (but not) real disasters in a data center. It is used to verify disaster recovery capabilities and help business personnel quickly get familiar with disaster recovery services.

#### 7.2.1 Fault simulation for two data centers-based zone disaster recovery

**based zone disaster recovery**

You can inject faults to simulate power and network outages of data centers and split-brain scenarios.

##### 7.2.1.1 Preparations

This topic describes the operating environments and logon information you must prepare to inject faults.

| Scenario | Console | Logon information |
|---|---|---|
| Power outage of the primary data center | ASR console for the secondary data center | IP address and password used to log on to the OPS 1 server in the primary data center IP address and password used to log on to the OPS 1 server in the secondary data center Out-of-band account and password |
| Recovery from power outages of the primary data center | ASR console for the secondary data center | IP address and password used to log on to the OPS 2 server in the primary data center |
| Power outage of the primary data center | ASR console for the primary data center | IP address and password used to log on to the OPS 1 server in the primary data center IP address and password used to log on to the OPS 1 server in the secondary data center Out-of-band account and password |
| Recovery from power outages of the secondary data center | ASR console for the primary data center | N/A |
| Network outage of the primary data center | ASR console for the primary data center | N/A |
| Recovery from network outages of the primary data center | ASR console for the primary data center | N/A |
| Network outage of the secondary data center | ASR console for the primary data center | N/A |
| Recovery from network outages of the secondary data center | ASR console for the primary data center | N/A |
| Split-brain scenario | ASR console for the primary data center | N/A |
| Recovery from the split-brain scenario | ASR console for the primary data center | N/A |

##### 7.2.1.2 Apply for an authentication code

Security risks may arise when faults are injected into a data center. You are not allowed to inject faults unless you are authorized. Therefore, you must apply for an authentication code before you inject faults into a data center.

**Prerequisites**

The environment is checked and works as expected. For more information, see Check the environment.

**Procedure**

1. Use an administrator account to log on to the ASR for Zone-disaster Recovery (Primary
Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.

> **Note:** Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console based on the fault injection scenario. For more information, see Preparations.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation >**
**Authentication Code History**.
3. Click **Add**. Configure the Scenario and User parameters and click **Submit**.
The generated authentication code is displayed in the message that appears. Record the authentication code. You must provide the authentication code when you inject faults.

##### 7.2.1.3 Check the environment

To ensure the accuracy of disaster recovery drill results, you must check whether the environment works as expected before you inject faults. If the environment does not work as expected, do not perform further operations.

**Background information**

Health check items differ in fault injection scenarios. Perform health checks as prompted. To implement health checks, perform the following steps.

**Procedure**

1. Use an administrator account to log on to the Apsara Stack Resilience (ASR) for Zone-
disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.

> **Note:** Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console based on the fault injection scenario. For more information, see Preparations.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation >**
**Health Check**.
3. In the Select Data Center step, select **Primary Data Center** or **Secondary Data Center**
from the **Select Data Center** drop-down list.
4. On the **Check Prerequisites** page, enter the environment information as prompted.
5. Click **Next**. After the information is verified, ASR begins to check the status of the switches.
If the status of the switches is abnormal, contact on-site O&M engineers to resolve the abnormalities, or you can ignore the abnormalities based on your requirements.
6. Check information about the servers, including the SNs, out-of-band IP addresses,
hostnames, and power supply. If the status of the servers is abnormal, contact on-site O&M engineers to resolve the abnormalities, or you can ignore the abnormalities based on your requirements. You can also click **View Server Role** to view the server role information about the required server.
7. Click **Complete** to complete the checks.

##### 7.2.1.4 Inject a power outage

###### 7.2.1.4.1 Inject a power outage

This topic describes how to simulate a power outage scenario by shutting down all servers in a data center in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.

> **Note:** To inject a power outage into the primary data center, use an administrator account or an account that is assigned the advanced O&M role to log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.
> To inject a power outage into the secondary data center, use an administrator account or an account that is assigned the advanced O&M role to log on to the ASR for Zone-disaster Recovery (Primary Zone) console.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Select the switch ports you want to disable. You can select **Port for Public Network**
**Connection** and **Port for Physical Connection**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

4. Click **Start**. Enter the obtained authentication code. You are navigated to the Log on to
Terminal Server step. Enter the environment information and click **Submit**.
5. After the environment information is checked, click **Next**.
6. On the **Inject Disaster Recovery Fault** page, select whether to protect data.
**Fail Over**: ASR first fails over Apsara Stack DNS, MiniRDS, and ApsaraDB RDS to the peer
data center to prevent data loss.
**Skip**: ASR shuts down the servers in the current data center. Data may be lost.
7. Optional. In the **Primary Data Center Server** step, view the list of servers that need to be
shut down. If servers that do not need to be shut down exist, enter the server names in the
**Exclude Server** field. Click **Submit**.
8. Click **Start** to shut down the servers.
9. After the servers are shut down, click **Shut Down OPS Servers**.
0. After the fault is injected, click **Complete**.

**What to do next**

After the power outage is injected, verify that your business is switched over and services are available. Then, recover the data center into which the power outage is injected. For more information about how to recover a data center after switchovers for power outages, see Recover a data center after switchovers for power outages.

###### 7.2.1.4.2 Recover a data center after failovers for power outages

**power outages**

This topic describes how to start all servers in a data center in the Apsara Stack Resilience (ASR) console to simulate scenarios of power-up.

**Prerequisites**

Your business is successfully failed over after a power outage, and all services are available.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.

> **Note:** If you injected the power outage in the ASR for Zone-disaster Recovery (Primary Zone) console, log on to the ASR for Zone-disaster Recovery (Primary Zone) console.
> If you injected the power outage in the ASR for Zone-disaster Recovery (Secondary Zone) console, log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. On the **Data Center Disaster Recovery** page, click **Start** to start servers in the data
center.
5. In the process where the system recovers the primary data center after switchovers for
power outages, recover Domain Name System (DNS) after the servers in the primary data center are started. To recover DNS, perform the following operations.

> **Note:** This step is not required for recovering a secondary data center after switchovers for power outages.

i. Enter the IP address and the password that are used to log on to the OPS 2 server from the primary data center. ii. Set the status of dns-master to STANDBY for the faulty data center. iii. Check synchronization logs. iv. Check the dnsapi1 and dnsapi2 field values. v. Add the anycastIp field value. vi. Enable OSPFD or BGPD to advertise routes.
6. Click **Complete** after all servers are started and the system shows that the data center is
recovered.

##### 7.2.1.5 Network outage of data centers

###### 7.2.1.5.1 Inject a network outage

You can simulate network outage scenarios in the Apsara Stack Resilience (ASR) console by interrupting the connections across data centers.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Select the switch ports you want to disable. In the Select the switch ports to be closed step,
you can select **Port for Public Network Connection** and **Port for Public Network**
**Connection**. By default, **Port for Cross-Data Center Circuit** is disabled.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

4. Click **Start**. Enter the obtained authentication code. ASR begins to check the environment
information.
5. After the environment information is checked, click **Next**.
6. On the **Inject Disaster Recovery Fault** page, click **Start** or **Skip** to disable or skip
disabling ports for Internet connections, physical connections, and cross-data center connections.
7. After the fault is injected, click **Complete**.

**What to do next**

After the network outage is injected, verify that business is failed over and services are available. Then, recover the primary data center. For more information about how to recover a data center after failovers for network outages, see Recover a data center after failovers for network outages.

###### 7.2.1.5.2 Recover a data center after failovers for network outages

**network outages**

This topic describes how to simulate the recovery of a data center after a failover for a network outage by recovering network connections across data centers in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

Your business is successfully failed over, and all services are available.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. You can perform the operation only if the information is valid.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. After the information about the switches is checked, click **Next**.
5. In the **Recover Data Center** step, click **Start** or **Skip** to enable or skip enabling Internet
connections, physical connections, and cross-data center connections.
6. When all items are in the **Completed** state, click **Complete**.

##### 7.2.1.6 Split-brain scenario

###### 7.2.1.6.1 Inject a split-brain scenario

This topic describes how to simulate a split-brain scenario by interrupting the connections across data centers in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "escape logon scenarios" section in Escape logon scenarios.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Click **Start**. Enter the obtained authentication code.
ASR checks the environment information.
4. After the information about the switches is checked, click **Next**.
5. In the **Inject Disaster Recovery Fault** step, click **Start**.
6. After the check is complete, click **Complete**.
7. After the fault is injected, click **Complete**.

**What to do next**

After the split-brain scenario is injected, verify that your business is switched over and services are available. Then, recover the environment. For more information about how to recover the environment after switchovers for split-brain scenarios, see Recover the environment after failovers for split-brain scenarios.

###### 7.2.1.6.2 Recover the environment after failovers for split-brain scenarios

**for split-brain scenarios**

You can simulate recovery of the environment for a split-brain scenario in the Apsara Stack Resilience (ASR) console by recovering connections across data centers.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code. A split-brain scenario is injected. For more information, see Inject a split-brain scenario.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. After the information about the switches is checked, click **Next**.
5. On the **Recover Data Center** page, click **Start** to recover connections across data
centers.
6. When all items are in the **Complete** state, click **Complete**.
7. On the recovery result page, click **Complete**.

##### 7.2.1.7 Single-product failure

###### 7.2.1.7.1 Inject a single-service outage

This topic describes how to simulate a single-service outage by shutting down the cluster of a service in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Escape logon scenarios.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Click **Start**. Enter the obtained authentication code and click **OK**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. You can perform the operation only if the information is valid.

4. Enter the environment information as prompted and click **Submit**.
5. Select the service for which you want to inject a failure and the data center in which the
service is deployed. Then, click **Search**. Select the check box of the cluster that you want to shut down. Click **Start**.

> **Note:** If the cluster fails to shut down, click **Retry**.

6. Click **Complete**.
7. Click **Complete**.

**What to do next**

After the single-service outage is injected, verify that your business is failed over and services are available. Then, recover the data center into which the single-service outage is injected. For more information about how to recover a data center after failovers for single-service outages, see Recover a data center after failovers for single-service outages.

###### 7.2.1.7.2 Recover a data center after failovers for single-service outages

**single-service outages**

This topic describes how to simulate the recovery of a data center after the failover for a single-service outage by starting the cluster of a service in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

After a single-service outage occurs, your business is failed over and the services are available.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Escape logon scenarios.

> **Note:** If you injected the single-service outage in the ASR for Zone-disaster Recovery (Primary Zone) console, log on to the ASR for Zone-disaster Recovery (Primary Zone) console.
> If you injected the single-service outage in the ASR for Zone-disaster Recovery (Secondary Zone) console, log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.
3. Click **Start**. Enter the obtained authentication code and click **OK**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. You can perform the operation only if the information is valid.

4. Enter the environment information as prompted and click **Submit**.
5. In the **Recover Data Center** step, click **Start** in the upper-right corner.

> **Note:** If the cluster fails to start, click **Retry**.

6. If the cluster is started, click **Complete**.
7. Click **Complete**.

#### 7.2.2 Fault simulation for three data centers-based zone disaster recovery

**based zone disaster recovery**

You can inject faults to simulate faults such as power and network outages of data centers and single points of failure (SPOFs).

##### 7.2.2.1 Preparations

This topic describes the operating environments and logon information you must prepare for fault injection.

| Scenario | Console | Logon information |
|---|---|---|
| Power outage of the primary data center | ASR console for the secondary data center | IP address and password to log on to the OPS1 server in the primary data center IP address and password to log on to the OPS1 server in the secondary data center IP address and password to log on to the OPS1 server in the quorum data center Out-of-band account and password |
| Recovery from power outages of the primary data center | ASR console for the secondary data center | IP address and password to log on to the OPS2 server in the primary data center |

| Power outage of the secondary data center | ASR console for the primary data center | IP address and password to log on to the OPS1 server in the primary data center IP address and password to log on to the OPS1 server in the secondary data center IP address and password to log on to the OPS1 server in the quorum data center Out-of-band account and password |
|---|---|---|
| Recovery from power outages of the secondary data center | ASR console for the primary data center | None |
| Power outage of the quorum data center | ASR console for the primary data center | IP address and password to log on to the OPS1 server in the primary data center IP address and password to log on to the OPS1 server in the secondary data center IP address and password to log on to the OPS1 server in the quorum data center Out-of-band account and password |
| Recovery from power outages of the quorum data center | ASR console for the primary data center | None |
| Network outage of the primary data center | ASR console for the primary data center | Information about the switches and ports to be disabled |
| Recovery from network outages of the primary data center | ASR console for the primary data center | None |
| Network outage of the secondary data center | ASR console for the primary data center | Information about the switches and ports to be disabled |
| Recovery from network outages of the secondary data center | ASR console for the primary data center | None |
| Single point of failure (SPOF) | ASR console for the primary data center | Information about the switches and ports to be disabled |
| Recovery from SPOF | ASR console for the primary data center | None |

##### 7.2.2.2 Apply for an authentication code

Security risks may arise when faults are injected into a data center. You are not allowed to inject faults unless you are authorized. Therefore, you must apply for an authentication code before you inject faults into a data center.

**Prerequisites**

The environment is checked and works as expected. For more information, see Check the environment.
1. Use an administrator account to log on to the ASR for Zone-disaster Recovery (Primary
Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.

> **Note:** Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console based on the fault injection scenario. For more information, see Preparations.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation >**
**Authentication Code History**.
3. Click **Add**. Configure the Scenario and User parameters and click **Submit**.
The generated authentication code is displayed in the message that appears. Record the authentication code. You must provide the authentication code when you inject faults.

##### 7.2.2.3 Check the environment

To ensure the accuracy of the disaster recovery (DR) drill results, you must check whether the environment works before you inject faults. If the environment does not work as expected, do not perform further operations.

**Background information**

Environment check items differ in fault injection scenarios. Perform environment checks as prompted. This topic describes the common environment check procedure.

**Procedure**

1. Use an administrator account to log on to the Apsara Stack Resilience (ASR) for Zone-
disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.

> **Note:** Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console based on the fault injection scenario. For more information, see Preparations.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation >**
**Health Check**.
3. Select the primary, secondary, or quorum data center from the **Select Data Center** drop-
down list.
4. In the **Check Prerequisites** step, enter the environment information as prompted.
5. Click **Next**. After the information is verified, ASR checks the status of the switches.
If the status of the switches is abnormal, contact O&M engineers to resolve the abnormalities, or you can ignore the abnormalities based on your requirements.
6. ASR checks the information about the servers, including the serial numbers (SNs), out-of-
band IP addresses, hostnames, and power supply. If the status of the servers is abnormal, contact O&M engineers to resolve the abnormalities, or you can ignore the abnormalities based on your requirements. You can also click **View Server Role** to view the server role information about a server.
7. Click **Complete** to complete the check.

##### 7.2.2.4 Inject a power outage

###### 7.2.2.4.1 Inject a power outage

This topic describes how to simulate a power outage scenario by shutting down all servers in a data center in the Apsara Stack Resilience (ASR) console.

**Prerequisites**

The environment information is obtained. For more information, see Preparations. An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.

> **Note:** To inject a power outage into the primary data center, use an administrator account or an account that is assigned the advanced O&M role to log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.
> To inject a power outage into the secondary or quorum data center, use an administrator account or an account that is assigned the advanced O&M role to log on to the ASR for Zone-disaster Recovery (Primary Zone) console.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Select the switch ports that you want to disable. You can select **Port for Public Network**
**Connection** and **Port for Physical Connection**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. You can perform the operation only if the information is valid.

4. Click **Start**. Enter the obtained authentication code. You are navigated to the Log on to
Terminal Server step.
5. Enter the environment information as prompted and click **Submit**.
6. After the environment information is checked, click **Next**.
7. In the **Inject Disaster Recovery Fault** step, select whether to protect data.
**Fail Over**: ASR first switches over MiniRDS and ApsaraDB RDS to the peer data center to
prevent data loss.
**Skip**: ASR shuts down the servers in the current data center. Data may be lost.
8. **Optional.** In the **Primary Data Center Server** section, view the list of servers that need
to be shut down. If servers that do not need to be shut down exist, enter the server names in the **Exclude Server** field. Then, click **Submit**.
9. Click **Start** to shut down the servers.
0. After the servers are shut down, click **Shut Down OPS Servers**.
1. After the fault is injected, click **Complete**.

**What to do next**

After the power outage is injected, verify that your business is failed over and services are available. Then, recover the data center into which the power outage is injected. For more information about how to recover a data center after failovers for power outages, see Recover a data center after failovers for power outages.

###### 7.2.2.4.2 Recover a data center after failovers for power outages

**power outages**

This topic describes how to start all servers in a data center in the Apsara Stack Resilience (ASR) console to simulate scenarios of power-up.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. On the **Data Center Disaster Recovery** page, click **Start** to start servers in the data
center.
5. Recover Domain Name System (DNS) after the servers in the primary data center are
started. To recover DNS, perform the following operations.

> **Note:** This step is unnecessary for the recovery of the secondary data center after switchovers for power outages.

i. Enter the IP address and the password that are used to log on to the OPS 2 server from the primary data center. ii. Check the dnsapi1 and dnsapi2 field values. iii. Add the anycastVip field value. iv. Enable Open Shortest Path First (OSPF) or Border Gateway Protocol (BGP) to advertise routes.
6. Click **Complete** after all servers are started and the system shows that the data center is
recovered.

##### 7.2.2.5 Network outage of data centers

###### 7.2.2.5.1 Inject a network outage

This topic describes how to simulate network outage scenarios in the Apsara Stack Resilience (ASR) console by interrupting the connections across data centers.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Primary Zone) console. For more information, see the "Escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.
3. Select the switch ports you want to disable. In the Select the switch ports to be closed step,
you can select **Port for Public Network Connection** and **Port for Public Network**
**Connection**. By default, **Port for Cross-Data Center Circuit** is disabled.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

4. Click **Start**. Enter the obtained authentication code.
ASR begins to check the environment information.
5. After the environment information is checked, click **Next**.
6. On the **Inject Disaster Recovery Fault** page, click **Start** or **Skip** to disable or skip
disabling ports for Internet connections, physical connections, and cross-data center connections.
7. After the fault is injected, click **Complete**.

###### 7.2.2.5.2 Recover a data center after failovers for network outages

**network outages**

This topic describes how to simulate the recovery of a data center after the failover for a network outage by recovering network connections across data centers in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

Your business is successfully failed over, and all services are available.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. After the information about the switches is checked, click **Next**.
5. In the **Recover Data Center** step, click **Start** or **Skip** to enable or skip enabling Internet
connections, physical connections, and cross-data center connections.

> **Note:** Information such as the names of the switches you want to disable, switch ports, and manufacturers is specified when you inject the fault. You cannot enter the information again.

6. When all items are in the **Completed** state, click **Complete**.

##### 7.2.2.6 SPOFs

Single points of failure (SPOFs) occur when the network connections between two data centers are abnormal. You can simulate SPOF scenarios in the ASR console by interrupting the connections across data centers.

###### 7.2.2.6.1 Inject a single-connection failure

You can simulate a single-connection failure in the Apsara Stack Resilience (ASR) console by interrupting the connections across data centers.

**Prerequisites**

An authentication code is obtained. For more information, see Apply for an authentication code.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Inject**
**Fault**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code.
ASR begins to check the environment information.
4. After the information about the switches is checked, click **Next**.
5. On the **Inject Disaster Recovery Fault** page, set Switch Name, Switch Port, and
Manufacturer. You can add records for multiple switches. Click Submit.
6. Click **Start**.
7. When the status becomes complete, click **fault injection Complete**.
8. After the fault is injected, click **Complete**.

###### 7.2.2.6.2 Recover the environment after the switchover for the single-connection failure

**switchover for the single-connection failure**

You can simulate recovery of the environment after the switchover for a single-connection failure in the Apsara Stack Resilience (ASR) console by recovering connections across data centers.

**Prerequisites**

The single-connection failure is injected.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

3. Click **Start**. Enter the obtained authentication code. The account information does not need
to be verified. ASR checks the environment information before the data center is recovered.
4. After the information about the switches is checked, click **Next**.
5. On the **Recover Data Center** page, click **Start**. The system recovers network connections
across three data centers based on the switch and port information specified when the fault is injected.
6. When all items are in the **Completed** state, click **Complete**.

##### 7.2.2.7 Single-product failure

###### 7.2.2.7.1 Inject a single-product failure

This topic describes how to simulate a single-product failure by shutting down the cluster of a product in the Apsara Stack Resilience (ASR) console.

**Prerequisites**

The authentication code used to simulate the single-product failure is obtained.

**Procedure**

1. Use the administrator account or an account configured with the advanced O&M role to log
on to the ASR console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Fault Simulation** > **Inject Fault**.
3. Click **Start**. Enter the obtained authentication code. Click **OK**.

> **Note:** ASR automatically identifies whether the authentication code and the user information are valid. If the information is invalid, you are not allowed to perform operations.

4. On the **Check Service Health** page, enter the IP addresses and the passwords of the OPS
1 servers for the primary and secondary data centers. Click **Next**.
5. Select the product for which you want to inject a failure and the data center where the
product is deployed. Click **Search**. Select the check box in front of the cluster you want to shut down. Click **Start**.

> **Note:** If the cluster fails to shut down, click **Retry**.

6. Click **Complete**.
7. Click **Complete**.

**What to do next**

After the single-product failure is injected, verify that business is switched over and services are available. Then, recover the primary data center. For more information about how to recover a data center after switchovers for single-product failures, see Recover a data center after switchovers for single-product failures.

###### 7.2.2.7.2 Recover a data center after failovers for single-service outages

**single-service outages**

This topic describes how to simulate the recovery of a data center after the failover for a single-service outage by starting the cluster of a service in the Apsara Stack Resilience (ASR) for Zone-disaster Recovery console.

**Prerequisites**

After a single-service outage occurs, your business is failed over and the services are available.

**Procedure**

1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zonedisaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.

> **Note:** If you injected the single-service outage in the ASR for Zone-disaster Recovery (Primary Zone) console, log on to the ASR for Zone-disaster Recovery (Primary Zone) console.
> If you injected the single-service outage in the ASR for Zone-disaster Recovery (Secondary Zone) console, log on to the ASR for Zone-disaster Recovery (Secondary Zone) console.

2. In the left-side navigation pane, choose **Disaster Recovery > Fault Simulation > Data**
**Center Disaster Recovery**.
3. Click **Start**. Enter the obtained authentication code and click **OK**.

> **Note:** ASR automatically checks whether the authentication code and the user information are valid. You can perform the operation only if the information is valid.

4. Enter the environment information as prompted and click **Submit**.
5. In the **Recover Data Center** step, click **Start** in the upper-right corner.

> **Note:** If the cluster fails to start, click **Retry**.

6. If the cluster is started, click **Complete**.
7. Click **Complete**.

### 7.3 View the recovery history

This topic describes how to view the recovery history. The recovery history records the time for various recovery and failover operations, execution results, logs, and failover duration.
1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the "Escape logon scenarios" section in Escape logon scenarios.
2. In the left-side navigation pane, choose **Disaster Recovery > Recovery History**.
3. View record details.
View log details for power loss disaster recovery and island disaster recovery records. a. Click the icon on the left side of a recovery operation name in the **Switchover**
**Records** section to view the operation time, execution result, and failover duration.
b. Click **Logs** in the Actions column to view the details of recovery logs. View the details of the recovery process. Click **View Details** in the **Actions** column to view the execution process of a recovery record.

## 8 System settings

### 8.1 Arbitration management

In the standard three-data-center deployment scenario, the arbitration service detects whether a real data center-level fault occurs. If so, the arbitration service determines whether the current conditions are met to initiate arbitration switchover and then switches the products and base to a normal data center.

**Constraints**

The arbitration switchover is subject to the following constraints: When the arbitration switchover fails, the arbitration service does not perform a switchover retry and requires human intervention. When the original data center is recovered, the arbitration service does not automatically switch back to the original data center.

**Arbitration process**

Before the arbitration switchover is executed, the arbitration service performs the detection. The following figure shows the entire process of the arbitration service:
1. On the **Arbitration Management** page, you can enable the arbitration service. After ASR
for Zone-disaster Recovery determines that the data center is normal, the arbitration service is enabled.
2. The arbitration service performs the following steps in the detection:
i. Whether the heartbeat of the node service in each data center is normal: If the heartbeat is detected, the data center is normal and the detection ends. If no heartbeat is detected, the next step is performed. ii. Reference product inspection. If exceptions are detected during the inspection of Apsara Infrastructure Management, perform the next step. For more information, see Monitor products. Otherwise, the detection ends. iii. Arbitrated product inspection. If exceptions are detected during the inspection of the middleware service, perform the next detection. Otherwise, the detection ends. iv. ISW connectivity check.
3. When the detection of the arbitration service ends, the arbitration decision phase starts.
The arbitration switchover is initiated only after the following conditions are met: The product in the data center is normal. The RPO of the product is lower than the specified maximum tolerance value. The specified number of arbitration detections is reached.
4. Arbitration switchover: After the arbitration conditions are met, ASR for Zone-disaster
Recovery forcibly switches over the arbitrated product. After the switchover is completed, the prompt is displayed on the page.
5. Wait for the data center recovery: After the arbitration switchover is completed, you must
recover the faulty data center. The entire arbitration process ends after the arbitration service detects that the data center is recovered. However, the arbitration service is still enabled. You must manually disable the arbitration service.

**Prerequisites**

ASR for Zone-disaster Recovery services of the primary and secondary data centers run normally. The inspection results of the arbitration service are normal. The ISW connectivity check of each data center is normal.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-
disaster Recovery (Secondary Zone) console. For more information, see the "escape logon scenarios" section in Log on to the ASR console.
2. In the left-side navigation pane of the **ASR for Zone-disaster Recovery** console, choose
**System Settings > Arbitration Management**.
3. On the **Arbitration Management** page, click **Create Arbitration**. Then, perform the
following steps to configure the parameters to enable the arbitration service.
4. Select a product for arbitration in the **Arbitrated Products** line. Only the selected product
can be forcibly switched over after it is determined that arbitration is required.

> **Note:** By default, the base middleware service is selected.

5. In the **ISW Information** line, click **Add ISW** to add the ISWs of the primary data center,
secondary data center, and third data centers in sequence.
6. In the **Service Execution Attempts** line, specify the number of service inspections. You
can enter an integer that ranges from 1 to 5.
7. If you click **Enable Arbitration**, the system immediately performs a detection. If the
success message is displayed, the arbitration service is enabled.

> **Note:** The data center will be powered off when the data center is relocated. To prevent automatic switchover initiated by the arbitration service, you must disable the arbitration service before the data center is relocated.

**Other operations**

After the arbitration service is enabled, you can perform the following operations:

| Operation | Procedure |
|---|---|
| Modify arbitration | 1. On the Arbitration Management page, click Modify Arbitration. 2. Modify the Execution Attempts parameter or ISW information and click Submit. |
| Disable Arbitration | 1. On the Arbitration Management page, click Disable Arbitration. 2. In the message that appears, click OK. |

### 8.2 Alert management

#### 8.2.1 Create an alert rule

This topic describes how to create an alert rule. After you create an alert rule, an alert is generated if Apsara Stack Resilience (ASR) detects exceptions and the alert rule is met.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery (Secondary Zone) console. For more
information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Settings > Alerts > Alert Rules**.
3. Click **Add**. In the **Create Alert Rule** dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Enable Alert Rule | Specifies whether to enable the alert rule. The alert rule takes effect after being enabled. By default, the alert rule is enabled. |
| Product | The service that you want to monitor. |

| Metric | The monitoring metric. The metric varies based on the service. If the metric shows an exception, ASR generates an alert of the corresponding alert level. The following metrics are supported: Product DR Capability Check: ASR monitors the disaster recovery (DR) capability and data synchronization status of the service. You can also view the DR capability and data synchronization status of the service on the Product Monitoring page of the ASR console. If an abnormality is detected, ASR generates an alert. Product Service Capability Check: ASR checks the basic services of each product and the console health status. You can view the check items of each product on the Product Monitoring page of the ASR console. Primary Node in the Secondary Data Center: If the primary node of ApsaraDB RDS or Simple Log Service resides in the secondary data center, alerts are generated. Note If the primary data center provides services but the primary node resides in the secondary data center, requests are directed to the secondary data center. This results in cross-data center access and affects the response time. Data Loss: ASR checks the instance status and data synchronization latency compliance rate of Object Storage Service (OSS), ApsaraDB RDS, and Tablestore instances. Protection Group Check: ASR checks the status of the protection group on the tenant side, including the synchronization status and latency. Product Configuration Upgrade: If rolling is not performed on services that are redeployed or whose configurations are upgraded, ASR generates an alert. Cluster Deployment: If services in the primary and secondary data centers are deployed in asymmetric mode, ASR generates an alert. Product Version: If the versions of a cloud service deployed in the primary and secondary data centers are inconsistent, ASR generates an alert. Product Baseline: If the content of the baseline configuration file is different from the baseline configurations in Apsara Infrastructure Management, ASR generates an alert. DNS Resources: If Domain Name System (DNS) resources involve an abnormal service when ASR performs environment checks, ASR generates an alert. VIP resources: If virtual IP address (VIP) resources involve an abnormal service when ASR performs environment checks, ASR generates an alert. Database Resources: If database resources involve an abnormal service when ASR performs environment checks, ASR generates an alert. Conditions of the Network Between Data Centers: If abnormalities occur when the routes of CIDR blocks of Virtual Private Cloud (VPC) and Server Load Balancer (SLB) are advertised, ASR generates an alert. BGP Route: If abnormal services exist during Border Gateway Protocol (BGP)-compliant routing when ASR performs environment checks, ASR generates an alert. |
|---|---|

| Triggering Threshold | The triggering threshold for OSS monitoring, RDS monitoring, and Tablestore monitoring on the Synchronization Monitoring page. Note This configuration item is displayed only when you select the Data Loss metric. |
|---|---|
| Detection Cycle | The time interval at which the system detects alerts. Valid values: 1 min, 5 min, 10 min, 15 min, and 30 min. |
| Alert Level | The alert level. Description of alert levels: P1: Critical P2: Severe P3: Warning P4: Info |
| Enable Alert Threshold | Specifies whether to enable the alert threshold. You can enable this feature and specify a threshold. If the number of times that an exception occurs in five consecutive monitoring sessions reaches the specified alert threshold, an alert is reported to the Apsara Uni-manager Operations Console. |

4. Click **OK**.

#### 8.2.2 Modify an alert rule

You can modify alert rules when your requirements change.

**Procedure**

1. Log on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Secondary Zone)
console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Settings > Alerts > Alert Rules**.
3. Find the alert rule that you want to modify and click **Modify** in the **Actions** column.
4. In the **Modify Alert Rule** dialog box, modify the parameters.

| Parameter | Description |
|---|---|
| Enable Alert Rule | Specifies whether to enable the alert rule. The alert rule takes effect after being enabled. By default, the alert rule is enabled. |
| Triggering Threshold | The triggering threshold for OSS monitoring, RDS monitoring, and Tablestore monitoring on the Synchronization Monitoring page. Note This configuration item is displayed only when you select the Data Loss metric. |
| Detection Cycle | The time interval at which the system detects alerts. Valid values: 1 min, 5 min, 10 min, 15 min, and 30 min. |
| Alert Level | Select an alert level. Description of alert levels: P1: Critical P2: Severe P3: Warning P4: Info |
| Enable Alert Threshold | Specifies whether to enable the alert threshold. You can enable this feature and specify a threshold. If the number of times that an exception occurs in five consecutive monitoring sessions reaches the specified alert threshold, an alert is reported to the Apsara Uni- manager Operations Console. |

5. Click **OK**.

#### 8.2.3 View alert records

This topic describes how to view existing alerts for zone-disaster recovery on the Alert Records page. You must handle the alerts at the earliest opportunity.
1. Use an administrator account or an account that is assigned the advanced O&M role to log
on to the Apsara Stack Resilience (ASR) for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Settings > Alerts > Alert Records**.
3. On the **Alert Records** page, you can perform the following operations:
Search for alerts by service name, metric, status, start time, end time, or alert level. Move the pointer over the **Alert Details** column to view the detailed information of an alert. View abnormality information: a. Search for alerts that are in the **Unhandled** state. b. Click **View Details** in the **Actions** column of an alert. You are navigated to the Product Monitoring or Product Check page, on which you can view detailed abnormality information. Handle alerts that are in the **Unhandled** state at the earliest opportunity. After the corresponding abnormality is resolved, the alert enters the **Handled** state. Click **Ignore** in the **Actions** column of an alert to ignore the alert.

### 8.3 Manage leased lines

After leased lines are configured, the network traffic between the devices in data centers is displayed on the **Overview** page. This allows you to view data transmission between the devices in different data centers.

**Prerequisites**

Leased lines are created before you perform a batch import. To create a leased line, perform the following steps: Log on to the Apsara Uni-manager Operations Console. Then, choose
**Product Operation > Networking > Network Operations Console** to go to the
**Network Operations Console**. In the left-side navigation pane, choose **Basic Network >**
**Leased Line Management > Leased Line Instances** to create a leased line.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery (Primary Zone) console or the ASR for Zone-
disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Settings > Leased Line Management**.
3. Add leased line information.
Adds a single leased line. a. Click **Create Leased Line**. b. Configure the parameters, which are described in the following table.

| Parameter | Description | Parameter configuration |
|---|---|---|
| Current Device | Indicates the name of the local device for data transmission. | User-defined. Example: ISW- VM-G1-1.AMTEST82. |
| Current Port | Indicates the number of the outbound or inbound port on the local device for data transmission. | User-defined. Example: 10GE1/0/6. |
| Peer Device | Indicates the name of the peer device for data transmission. | User-defined. Example: ISW- VM-G1-1.AMTEST82. |
| Peer Port | Indicates the number of the outbound or inbound port on the peer device for data transmission. | User-defined. Example: 10GE1/0/6. |
| Current Data Center | Indicates the name of the data center where the local device resides. | User-defined. Example: amtest1. |
| Peer Data Center | Indicates the name of the data center where the peer device resides. | User-defined. Example: amtest2. |
| Bandwidth (Mbit/s) | Indicates the maximum rate of direct data transmission between the local and peer devices. Unit: Mbit/s. | Enter a value based on the actual data transmission rate. Example: 100. |

c. Click **OK**. Add leased lines in batches. a. Click **Import**. b. In the **Import Leased Line** dialog box, select the leased lines that you want to add. c. Click **OK**.

**Related operations**

After you configure leased line information, you can perform the following operations.

| Operation | Procedure |
|---|---|

| Customize column fields | 1. Click in the upper-right corner of the page. 2. Select the column fields to be displayed and clear the column fields that do not need to be displayed. 3. Click Reset to restore the default settings and select all column fields. |
|---|---|
| Modify leased line information | 1. Click Modify in the Actions column. 2. Modify the parameter values as required. 3. Click OK. |
| Delete a leased line | 1. Click Delete in the Actions column. 2. In the message that appears, click OK. |

### 8.4 Password change

To ensure account security, we recommend that you change your logon password on a regular basis.

**Procedure**

1. Use an administrator account to log on to the ASR for Zone-disaster Recovery (Primary
Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the Escape logon scenarios section of the "Log on to the ASR console" topic.
2. In the left-side navigation pane, choose **Settings > Change Password**.
3. Enter the original and new passwords as prompted and click **Submit**.

| Parameter | Description |
|---|---|
| Current Password | Enter the current logon password of the administrator account. |
| New Password | Enter a new logon password for the administrator account. |
| Confirm Password | Enter the new logon password again. |

> **Note:** The password must be 12 to 20 characters in length and can contain the following types of characters:
> Digits
> Letters
> Special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

### 8.5 User management

Administrators can log on to ASR to manage users by adding users, deleting users, and disabling authentication.

#### 8.5.1 Add a user

The administrator can add user accounts that can be used to log on to the Apsara Stack Resilience (ASR) console.

**Procedure**

1. Log on to the ASR console as the administrator.
2. In the left-side navigation pane, choose **Settings > Users**.
3. Click **Add**.
4. Configure parameters. Click **Submitted**.

| Parameter | Description |
|---|---|
| Username | The name of the user you want to create. The username must be 4 to 10 characters in length and can contain letters or digits. |
| Password | The password of the user. The password must be 12 to 20 characters in length and can contain digits, letters, and special characters. |
| Confirm Password | Enter the password again. |
| User Role | The role of the user, which can be the basic O&M or advanced O&M role. The two roles have the following differences: The advanced O&M role has permissions to simulate fault injection, perform virtual drills, recover business for contingencies, view the details of platform monitoring, check platform health, manage alerts, change passwords, and configure authentication. The basic O&M role has permissions to view the details of platform monitoring, check platform health, manage alerts, change passwords, and configure authentication. |

#### 8.5.2 Enable or disable authentication

Administrators can turn on or turn off authentication for common users.
1. Log on to the ASR console as an administrator.
2. In the left-side navigation pane, choose **Settings > Users**.
3. Turn on **Authentication** corresponding to the target user.

> **Note:** By default, authentication is disabled for users. Users can turn on Enable Authentication on the Authentication page.

#### 8.5.3 Delete user information

To better guarantee the security of the ASR console, you must maintain ASR users on a regular basis.

**Procedure**

1. Log on to the ASR console as an administrator.
2. In the left-side navigation pane, choose **Settings > Users**.
3. Click **Delete** in the Actions column corresponding to the target user.

### 8.6 Authentication configuration

To ensure the security of logons, you can configure authentication. After authentication is enabled, users must use a Universal Serial Bus (USB) key to perform authentication when they log on to the Apsara Stack Resilience (ASR) console.

**Procedure**

1. Use an administrator account to log on to the ASR for Zone-disaster Recovery (Primary
Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see Log on to the ASR console.
2. In the left-side navigation pane, choose **Settings > Authentication Settings**.
3. Insert your USB key and click **Bind** or **Rebind**.
4. In the **Select Certificate** dialog box, select a certificate.
The serial number (SN) of the USB key is bound to the current account.
5. Click **Add IP Address**. Enter the IP address and the port number. Click **Add**.

> **Note:** At least one available IP address must be added to verify the USB key when you enable authentication for the first time.

6. Turn on **Enable Authentication**.

### 8.7 Data backup

You can back up data such as user accounts and alert rules that are configured in the Apsara Stack Resilience (ASR) console to an Object Storage Service (OSS) bucket. You can restore the data to the ASR console as required with a few clicks.

**Procedure**

1. Use an administrator account to log on to the ASR for Zone-disaster Recovery (Primary
Zone) console or the ASR for Zone-disaster Recovery (Secondary Zone) console. For more information, see the DR scenarios section of the "Log on to the ASR console" topic.
2. In the left-side navigation pane, choose **Settings > Data Backup**.
3. Click **Back Up**. In the message that appears, click **OK**. ASR backs up data such as user
accounts and alert rules to an OSS bucket.

> **Note:** To restore the data from OSS to the ASR console, click **Recover**. In the message that appears, click **OK**.

## 9 Protection groups

### 9.1 Protection group overview

A protection group is a tenant-side feature that allows you to restore a single service by application and perform disaster recovery drills.

**Overview**

1. Log on to the ASR for Zone-disaster Recovery console in tenant mode.
2. On the **Protection Group Overview** page, you can view the statistics of protection groups
in the current organization, resource set, and region. On the left side of the top navigation bar, you can change the organization, resource set, and region.

**Functional modules**

A protection group allows you to restore a service by application and perform disaster recovery drills in addition to basic capabilities available on the cloud platform. When you create a protection group, you can add business-related instances to the protection group. A protection group contain instances of cloud products such as databases, middleware, and ECS (as an HDR protection group). You can create a drill plan (hot switchover) or disaster recovery plan (forced switchover) based on the protection group. A protection group refines the switchover granularity of cloud products to allow users in different organizations to flexibly manage instances. Instances of the following products can be added to protection groups: ApsaraDB RDS, KVStore for Redis, OSS, and ECS.

> **Note:** A protection group can be associated with one drill plan and one disaster recovery plan, but either the drill plan or the disaster recovery plan associated with the same protection group can be executed at a time. Before you start another plan, you must terminate the current plan.
> For ApsaraDB RDS and OSS, protection groups directly correspond to instances. For ECS, protection groups correspond to HDR protection groups. You can add multiple HDR protection groups to a protection group in ASR.
> In versions earlier than 3.18.3, OSS disaster recovery only supports the instance switchover within the first OSS cluster. If you select instanceS other than the first OSS cluster when you create a protection group, an error is reported during the switchover.
> You must create HDR protection groups in the HDR console before you add HDR protection groups to a protection group in ASR.

| Functiona l module | Description |
|---|---|
| Protectio n Group Overview | Displays statistics for the number of protection groups, instances, drills, and disaster recovery plans. Charts are also provided. |
| Protectio n Groups | Displays a list of protection groups. You can add, delete, and view the details of protection groups. The information about each protection group is displayed. By default, the list includes the following columns: Protection Group Name, Description, Inspection Status, Organization, Resource Set, Created At, and Modified At. You can click Details in the Actions column to view details of a protection group. You can search for protection groups by specifying Protection Group Name, Inspection Status, or Protected Instance. Search is automatically triggered when you change filter conditions. On the Protection Group Details page, you can modify a protection group that is not associated with a drill plan or a disaster recovery plan. Note You cannot delete or modify a protection group if it is associated with a drill plan or a disaster recovery plan. If a protection group is not displayed on the Protection Groups page after it is created, check whether the selected organization and resource set on the left side of the top navigation bar are the same as those selected when you create the protection group. Only the protection groups that belong to the current organization are displayed in the list. Click the icon in the upper right corner of the list to modify the columns of the list and their order. |

| Protectio n Group Drills (hot switchover ) | Drill Plans: a list of drill plans. You can create, modify, and delete drill plans and view their details. You can also start, access, and terminate a drill. Note You cannot modify or delete a drill plan when it is being executed. After a drill is terminated, you cannot start the drill again. Drill History: a list of the execution processes of each drill plan. |
|---|---|
| Disaster Recovery (forced switchover ) | Disaster Recovery Plans: a list of disaster recovery plans. You can create, modify, and delete disaster recovery plans and view their details. You can also start, access, and terminate a disaster recovery drill. Note You cannot modify or delete a disaster recovery plan when it is being executed. After a disaster recovery plan is terminated, you cannot start the disaster recovery plan again. Disaster Recovery Records: a list of the execution processes of each disaster recovery plan. |

### 9.2 Protection group process

#### 9.2.1 Process overview

Protection groups of the ASR for Zone-disaster Recovery solution are mainly used for instance-level drills and disaster recovery. You can select instances based on your business applications and create protection groups to include them. You can create drill plans to perform disaster recovery drills. If your business fails, you can use a disaster recovery plan (forced switchover) to perform disaster recovery. The following figure shows the process how a protection group is used in the ASR for Zone-disaster Recovery solution.

#### 9.2.2 Create a protection group

**Scenarios**

A protection group allows you to restore a single service by application and perform disaster recovery drills based on the basic capabilities available on the cloud platform. In a protection group, you can add instances of cloud products such as databases, middleware, and ECS (as HDR protection groups). You can create drill plans (hot switchover) or emergency plans (forced switchover) for protection groups. A protection group refines the switchover granularity of cloud products to allow users in different organizations to flexibly manage instances. Instances of the following products can be added to protection groups: ApsaraDB RDS, KVStore for Redis, OSS, and ECS.

**Prerequisites**

The instances that you want to protect are created. The organizations to which the instances belong are authorized to access Apsara Stack Resilience (ASR) resources.
1. Log on to the ASR for Zone-disaster Recovery console in tenant mode.
2. In the left-side navigation pane, click **Protection Groups**. On the page that appears, click
**Create Protection Group**.
3. Select **Organization** and **Resource Set**, specify the **Protection Group Name** and
**Description** parameters, and then click **Next**.
4. Select **Product** and **Instance ID/Name** to select the instances that you want to add to the
protection group, confirm that the required instances are selected, and then click **Submit**.
5. In the message that appears, click **OK**.

> **Note:** The system automatically queries **Instance ID/Name** based on the organization information. If you do not find the ID or name of the instance, you can switch **Organization** in the top navigation bar.
> An instance can be added to only one protection group.

6. After you submit the protection group information, the **Protection Group Details** page
appears. You can view the basic information and inspection status of the protection group.
7. Click **Modify** to modify the details of the protection group.

> **Note:** You can **modify** or **delete** a protection group only when the protection group is not associated with any plan.

#### 9.2.3 Protection group drills

##### 9.2.3.1 Create a drill plan

**Scenarios**

On the condition of without affecting your business, you can create drill plans to simulate the switchover and switchback among protection groups, so that you can quickly implement switchover when a disaster occurs to improve business continuity.

**Prerequisites**

Protection groups are created. For more information, see Create a protection group.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery console in tenant mode.
2. In the left-side navigation pane, choose **Protection Group Drills** > **Drill Plans**.
3. On the **Drill Plans** page, click **Create Plan**.
4. In the Basic Information step, set **Organization**, **Resource Set**, **Protection Group**
**Name**, **Plan Name**, and **Plan Description**, and then click **Next**.
5. In the **Recovery Procedure** step, add the instances in the associated protection group to
the recovery step based on your business requirements. Click the + or - icon in the lowerleft corner to add or delete a step. Click **Submit** to go to the next step to select execution mode.
6. Select an execution mode and then click **OK**.

> **Note:** Automatic: Each phase of the instance execution step in the protection group recovery plan is automatically executed based on the orchestrated step. An instance exception blocks subsequent steps.
> Manual: Each phase of the instance execution step in the protection group recovery plan is manually executed based on the scheduled step. After the plan is executed on an instance, you must click **Execute**. An instance exception blocks subsequent steps.

7. After you submit your settings, the **Drill Plan Details** page appears. You can view the
basic information, recovery steps, and instances that are not added to the associated protection group. You also can click **Start Drill** or **Access Drill** in the upper-right corner of the page.

##### 9.2.3.2 Drill process

The drill process consists of five steps: **switchover check**, **switchover**, **switchback check**,
**switchback**, and **recovery check**. Switchover is from the primary data center to the
secondary data center. Switchback is from the secondary data center to the primary data center. In the drill process, the **switchover check**, **switchback check**, and **recovery check** steps are automatically performed when you enter the check phase. You must manually perform the switchover and switchback steps. You can click Complete only when the last step is complete. Furthermore, you must click Complete to finish a drill before you can perform another drill.

> **Note:** Sometimes the instance is already in the destination data center, but an exception is displayed on the page. This is only a prompt in the current phase. In the actual switchover, if the instance is already in the destination data center, the switchover will not be performed again.

**Prerequisites**

A drill plan is created, and the protection group associated with the current plan is not in an emergency process.

**Procedure**

1. In the left-side navigation pane, choose **Protection Group Drills** > **Drill Plans**.
2. Find the drill plan and click **Details** in the Actions column. The **Drill Plan Details** page
appears. In the upper-right corner of the page, click **Start Drill**.
3. The **Drill Process** page is displayed and the **Switchover Check** step starts.

> **Note:** An exception occurs in the following case: the current primary node position of the instance is different from the start point of the switchover direction, the synchronization status is abnormal, or the synchronization delay is longer than expected. Forced switchover is supported even if the check result is abnormal. An error message is prompted when you start the next step.

> **Important:** If you continue switchover when the check result is abnormal, the switchover may fail and the instance may become unavailable.

4. The **switchover** step follows the **switchover check** step. The instances involved in the
plan are switched over from the primary data center to the secondary data center in the scheduled order. You must manually click **Execute** to trigger the switchover.

> **Note:** If a step fails, you can retry the current step or retry the instances one by one. If an instance fails to be switched over, you can also forcibly skip the step.

5. After the **switchover** step is complete, ASR for Zone-disaster Recovery automatically
performs the **switchback check**.

> **Note:** If the protection group contains HDR protection groups, reverse synchronization is established in the switchback check step.

6. After the **switch-back check** step is complete, you must manually **switch back** the
instances involved in the plan from the secondary data center to the primary data center in the scheduled order. In switchback, the same operation as in switchover is performed in the reverse direction.
7. The **recovery check** is performed automatically after the switchback. Then, the whole
process ends. You can view the drill history on the **Drill Records** page.

#### 9.2.4 Disaster recovery

##### 9.2.4.1 Create a disaster recovery plan

**Scenarios**

A disaster recovery plan is used to recover business when a data center fails.

**Prerequisites**

In the ASR for Zone-disaster Recovery console, relevant instances are switched over to the secondary data center. The basic capabilities of the cloud platform are available.

**Procedure**

1. Log on to the ASR for Zone-disaster Recovery console in tenant mode.
2. In the left-side navigation pane, choose **Disaster Recovery** > **Disaster Recovery Plan**.
3. On the **Disaster Recovery Plans** page, click **Create Plan**.
4. In the Basic Information step, set **Organization**, **Resource Set**, **Protection Group**
**Name**, **Plan Name**, and **Plan Description**. Then, click **Next**.
5. In the **Recovery Procedure** step, add the instances in the associated protection group to
the recovery step based on your business requirements. Click the + or - icon in the lowerleft corner to add or delete a step. Click **Submit** to go to the next step to select an execution mode.
6. Select an execution mode and then click **OK**.

> **Note:** Automatic: Each phase of the instance execution step in the protection group recovery plan is automatically executed based on the orchestrated step. An instance exception blocks subsequent steps.
> Manual: Each phase of the instance execution step in the protection group recovery plan is manually executed based on the scheduled step. After the plan is executed on an instance, you must click **Execute**. An instance exception blocks subsequent steps.

7. After you submit your settings, the **Disaster Recovery Plan Details** page appears. You
can view the basic information, recovery steps, and instances that are not added to the associated protection group. You also can click **Start Failover** or **Enter Failover** in the upper-right corner of the page.

##### 9.2.4.2 Disaster recovery process

A disaster recovery process consists of five steps: **Switchover Check**, **Switchover**,
**Switchback Check**, **Switchback**, and **Recovery Check**. Switchover is from the primary
data center to the secondary data center. Switchback is from the secondary data center to the primary data center. A complete protection plan includes both the switchover and switchback. In a disaster recovery process, the **Switchover check**, **Switchback check**, and
**Recovery Check** steps are automatically performed when you enter the check phase. You
must manually perform the switchover and switchback steps. You can click Complete only when the last step is complete. Furthermore, you must click Complete to finish a disaster recovery process before you can perform another disaster recovery process.

> **Note:** Sometimes the instance is already in the destination data center, but an exception is displayed on the page. In this case, you must check whether the instance is already in the destination data center. If yes, the switchover will not be performed again.

**Prerequisites**

A disaster recovery plan is created, and the protection group associated with the current plan is not in a drill process.

**Procedure**

1. In the left-side navigation pane, choose **Disaster Recovery** > **Disaster Recovery Plan**.
2. Find the disaster recovery plan and click **Details** in the Actions column. The **Disaster**
**Recovery Plan Details** page appears. In the upper-right corner of the page, click **Start**
**Failover**.
3. The **Failover Process** page is displayed and the **Switchover Check** step starts.

> **Note:** An exception occurs in the following case: the current primary node position of the instance is different from the start point of the switchover direction, the synchronization status is abnormal, or the synchronization delay is longer than expected. Forced switchover is supported even if the check result is abnormal. An error message is prompted when you start the next step.

> **Important:** If you continue a switchover when the check result is abnormal, the switchover may fail and the instance may become unavailable.

4. The **switchover** step follows the **switchover check** step. The instances involved in the
plan are switched over from the primary data center to the secondary data center in the scheduled order. You must manually click **Execute** to trigger the switchover.

> **Note:** If a step fails, you can retry the current step or retry the instances one by one. If an instance fails to be switched over, you can also forcibly skip the step.

5. After the **switchover** step is complete, ASR automatically performs the **switchback**
**check**.

> **Note:** If the protection group contains HDR protection groups, reverse synchronization is established in the switchback check step.

6. After the **switchback check** step is complete, you must manually **switch back** the
instances involved in the plan from the secondary data center to the primary data center in the scheduled order. In the switchback, the same operation as in the switchover is performed in the reverse direction.
7. The **Recovery Check** is performed automatically after the switchback. Then, the whole
process ends. You can view historical disaster recovery plans on the **Disaster Recovery**
**Records** page.

## 10 Appendix

### 10.1 Encryption and backup

Apsara Stack Resilience (ASR) ensures the security of user data by using key encryption and offline backup. ASR generates audit logs to record system security events and activities, prevent internal data misuse, track suspicious behaviors, and identify potential security threats and attacks. Key encryption: ASR stores logon passwords in the database by using the MD5 algorithm.

**Note**

Other data such as configurations and personnel information is not encrypted. Audit logs: ASR sends operation logs to Apsara Stack Security for auditing. Logs are stored in SLS-Inner.

**Note**

Docker logs are not backed up. Offline backup: ASR uses mysqldump to back up database data offline every 12 hours. The backup data is stored in Object Storage Service (OSS) and deleted after 5 days.

### 10.2 How to obtain the endpoint of ASR for Zone-disaster Recover

**of ASR for Zone-disaster Recover**

This topic describes how to obtain the endpoint when you log on to the ASR for Zone-disaster Recover console for the first time.

**Prerequisites**

Make sure that you have obtained the endpoint of the Apsara Uni-manager Operations Console, and the username and password used for logging on to the console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform > Apsara Infrastructure Management >**
**Resources**.
3. In the left-side navigation pane of **Apsara Infrastructure Management**, choose **O&M**
**Tools > Resource Dashboard**.
4. On the Resource Dashboards page, select **Name** from the drop-down list, enter bcmc-
domain, and then click .
5. Click the
in the Result column, and then click the value to display the result in a separate page. Record and save the value of the dns field.
6. View and save the endpoint of another data center in the same way as in the previous step.

> **Note:** asr-xs.cn represents the endpoint of the secondary data center and asr-xm-cn represents the endpoint of the primary data center.

7. For more information about logging on to the ASR for Zone-disaster Recovery console, see
Log on to the ASR console.
