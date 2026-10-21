---
title: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for MongoDB Operations and Maintenance Guide 20241115"
product_version: "V3.18.3"
doc_version: "20241115"
pdf_pages: 8
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for MongoDB Operations and Maintenance Guide 20241115.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/MongoDB/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20ApsaraDB%20for%20MongoDB%20Operations%20and%20Maintenance%20Guide%2020241115.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for MongoDB Operations and Maintenance Guide 20241115

## Table of Contents

- 1 Operations Guide
  - 1.1 Service architecture
    - 1.1.1 System architecture
      - 1.1.1.1 Backup system
      - 1.1.1.2 Data migration system
      - 1.1.1.3 Control system
      - 1.1.1.4 Monitoring system
      - 1.1.1.5 Task scheduling system
  - 1.2 ApsaraDB for MongoDB O&M overview
  - 1.3 Log on to the Apsara Uni-manager Operations Console
  - 1.4 Security maintenance
    - 1.4.1 Network security maintenance
    - 1.4.2 Account password maintenance

## 1 Operations Guide

### 1.1 Service architecture

#### 1.1.1 System architecture

##### 1.1.1.1 Backup system

**Automatic backup**

ApsaraDB for MongoDB supports both physical backup and logical backup. You can flexibly configure the backup start time based on the service off-peak hours. All backup files are retained for seven days.

**Temporary backup**

You can initiate a temporary backup as required. The backup files are retained for seven days.

**Log management**

ApsaraDB for MongoDB generates operation logs and allows you to download them. You can use the operation logs for local incremental backup.

**Data backtracking**

ApsaraDB for MongoDB can use backup files and logs to generate a temporary instance for any time point within the past seven days. After verifying that the data in the temporary instance is correct, you can use the temporary instance to restore data to the specified time point. Creating a temporary instance does not affect the running of the current instance. Only one temporary instance can be created for each ApsaraDB for MongoDB instance at a time. A temporary instance is valid for 48 hours. You can create a maximum of 10 temporary instances for an ApsaraDB for MongoDB instance each day.

##### 1.1.1.2 Data migration system

**Database replication between instances**

ApsaraDB for MongoDB allows you to easily migrate databases from one instance to another.

**Data migration to or from ApsaraDB for MongoDB**

ApsaraDB for MongoDB provides a professional tool and a migration wizard to help you migrate data to or from ApsaraDB for MongoDB.

**Backup file download**

ApsaraDB for MongoDB retains backup files for seven days. During this period, you can log on to the ApsaraDB for MongoDB console to download the backup files.

##### 1.1.1.3 Control system

If a host or an instance crashes, the ApsaraDB for MongoDB high-availability (HA) component fails services over within 30 seconds after the exception is detected. This guarantees that applications run properly and ApsaraDB for MongoDB is highly available.

##### 1.1.1.4 Monitoring system

**Performance monitoring**

ApsaraDB for MongoDB provides nearly 20 metrics for system performance monitoring, such as disk capacity, IOPS, connections, CPU utilization, network traffic, TPS, QPS, and cache hit rate. You can obtain the running status information of instances over the past year.

**SQL auditing**

The system records the SQL statements and related information sent to ApsaraDB for MongoDB instances, such as the connection IP address, database name, access account, execution time, and the number of records returned. You can use SQL auditing to locate problems and check instance security.

**Threshold alarms**

ApsaraDB for MongoDB provides alarm SMS notifications in the event of exceptions in instance status or performance. These exceptions can include instance locking, insufficient disk capacity, abnormal IOPS, abnormal number of connections, and over high CPU utilization. You can configure alarm thresholds and up to 50 alarm contacts (of which only five are effective at a time). When a threshold is exceeded in an instance, an SMS notification is sent to the alarm contacts.

**Web operation logs**

The system logs all modification operations in the ApsaraDB for MongoDB console for administrators to check. These logs are retained for a maximum of 30 days.

##### 1.1.1.5 Task scheduling system

You can use the ApsaraDB for MongoDB console or APIs to create or delete instances or switch instances between the intranet and Internet. All instance operations are scheduled, traced, and displayed as tasks.

### 1.2 ApsaraDB for MongoDB O&M overview

**overview**

This topic describes the O&M system of ApsaraDB for MongoDB. The Apsara Uni-manager Management Console provides the following O&M features for ApsaraDB for MongoDB: Instance management: allows you to view instance details, instance logs, and user information. Host management: allows you to view and manage hosts.

### 1.3 Log on to the Apsara Uni-manager Operations Console

**manager Operations Console**

This topic describes how to log on to the Apsara Uni-manager Operations Console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password used to log on to the console are obtained from the deployment personnel or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Open your Chrome browser.
2. In the address bar, enter the endpoint of the Apsara Uni-manager Operations Console.
Press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

3. Enter your username and password.

> **Note:** Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator.

When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. For security reasons, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains the following special characters: ! @ # $ % The password must be 10 to 20 characters in length.
4. Click **Log On**.

### 1.4 Security maintenance

#### 1.4.1 Network security maintenance

Network security maintenance is aimed at ensuring device security and network security.

**Device security**

Check network devices, and enable security management protocols and configurations of devices. Check for up-to-date versions of network device software and update the software to more secure versions in a timely manner. For more information about the security maintenance method, see the product document of each device.

**Network security**

Select the intrusion detection system (IDS) or intrusion prevention system (IPS) based on the network status to check Internet and intranet traffic and defend the network against abnormal behaviors and attacks.

#### 1.4.2 Account password maintenance

Account passwords include the ApsaraDB for MongoDB system and device passwords. To ensure account security, change the system and device passwords periodically, and use passwords that meet the complexity requirements.
