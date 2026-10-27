---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Stack Security User Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 219
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Stack Security User Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E5%85%B6%E4%BB%96/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Apsara%20Stack%20Security%20User%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Stack Security User Guide 20220928

## Table of Contents

- 1 What is Apsara Stack Security
- 2 Usage notes
- 3 Quick start
  - 3.1 User roles and permissions
  - 3.2 Log on to Apsara Stack Security Center
- 4 Threat Detection Service
  - 4.1 Overview
  - 4.2 Security overview
    - 4.2.1 View security overview information
  - 4.3 Security alerts
    - 4.3.1 View security alerts
    - 4.3.2 Manage quarantined files
    - 4.3.3 Configure security alerts
  - 4.4 Attack analysis
  - 4.5 Cloud service check
    - 4.5.1 Overview
    - 4.5.2 Run cloud service checks
    - 4.5.3 View the check results of configuration assessment for your cloud services and handle the detected risks
  - 4.6 Application whitelist
  - 4.7 Assets
    - 4.7.1 View the security status of a server
    - 4.7.2 View the security status of cloud services
    - 4.7.3 View the details of a single asset
    - 4.7.4 Enable and disable server protection
    - 4.7.5 Perform a quick security check
    - 4.7.6 Manage server groups
    - 4.7.7 Manage asset tags
  - 4.8 Vulnerability scan
    - 4.8.1 Quick start
    - 4.8.2 View the information on the Overview page
    - 4.8.3 Asset management
      - 4.8.3.1 View the results of asset analysis
      - 4.8.3.2 Import assets
      - 4.8.3.3 Manage assets
      - 4.8.3.4 Manage asset availability
      - 4.8.3.5 Manage custom update detection tasks
    - 4.8.4 Risk management
      - 4.8.4.1 Manage vulnerabilities
      - 4.8.4.2 Manage host compliance risks
      - 4.8.4.3 Manage external risks
      - 4.8.4.4 Create a custom risk detection task
    - 4.8.5 Report management
      - 4.8.5.1 Create a report
      - 4.8.5.2 Delete multiple reports at a time
    - 4.8.6 Configuration management
      - 4.8.6.1 Configure overall monitoring
      - 4.8.6.2 Configure basic monitoring
      - 4.8.6.3 Configure web monitoring
      - 4.8.6.4 Configure a whitelist
      - 4.8.6.5 Configure a scan engine for internal assets
  - 4.9 Create a security report
- 5 Server security
  - 5.1 Server security overview
  - 5.2 Server fingerprints
    - 5.2.1 Manage listening ports
    - 5.2.2 Manage software versions
    - 5.2.3 Manage processes
    - 5.2.4 Manage account information
    - 5.2.5 Manage scheduled tasks
    - 5.2.6 Set the fingerprint collection frequency
  - 5.3 Threat protection
    - 5.3.1 Vulnerability management
      - 5.3.1.1 Manage Linux vulnerabilities
      - 5.3.1.2 Manage Windows vulnerabilities
      - 5.3.1.3 Manage Web CMS vulnerabilities
      - 5.3.1.4 Manage urgent vulnerabilities
      - 5.3.1.5 Configure vulnerability management policies
    - 5.3.2 Baseline check
      - 5.3.2.1 Baseline check overview
      - 5.3.2.2 Configure baseline check policies
      - 5.3.2.3 View baseline check results and manage failed check items
  - 5.4 Intrusion prevention
    - 5.4.1 Intrusion events
      - 5.4.1.1 Intrusion event types
      - 5.4.1.2 View and handle detected intrusion events
      - 5.4.1.3 View exceptions related to an alert
      - 5.4.1.4 Use the file quarantine feature
      - 5.4.1.5 Configure security alerts
      - 5.4.1.6 Cloud threat detection
    - 5.4.2 Website tamper-proofing
      - 5.4.2.1 Overview
      - 5.4.2.2 Configure tamper protection
      - 5.4.2.3 View protection status
    - 5.4.3 Configure the anti-virus feature
  - 5.5 Log retrieval
    - 5.5.1 Log retrieval overview
    - 5.5.2 Query logs
    - 5.5.3 Supported log sources and fields
    - 5.5.4 Logical operators
  - 5.6 Settings
    - 5.6.1 Install the Server Guard agent
    - 5.6.2 Manage protection modes
- 6 Physical server security
  - 6.1 Create and grant permissions to a security administrator account
  - 6.2 View the information on the Overview page
  - 6.3 Physical servers
    - 6.3.1 Manage physical server groups
    - 6.3.2 Manage physical servers
  - 6.4 Intrusion detection
    - 6.4.1 Configure policies to identify unusual logons
    - 6.4.2 Handle unusual logons
  - 6.5 Server fingerprints
    - 6.5.1 Configure data refresh frequencies
    - 6.5.2 View listening ports
    - 6.5.3 View running processes
    - 6.5.4 View account information
    - 6.5.5 View software versions
  - 6.6 Log retrieval
    - 6.6.1 Supported log sources and fields
    - 6.6.2 Logical operators
    - 6.6.3 Query logs
  - 6.7 Configure security settings for physical servers
- 7 Application security
  - 7.1 Quick start
  - 7.2 Detection overview
    - 7.2.1 View protection overview
    - 7.2.2 View access information
  - 7.3 Protection logs
    - 7.3.1 View attack detection logs
    - 7.3.2 View HTTP flood protection logs
    - 7.3.3 View system operation logs
    - 7.3.4 View access logs
  - 7.4 Protection configuration
    - 7.4.1 Configure protection policies
    - 7.4.2 Create a custom rule
    - 7.4.3 Configure an HTTP flood protection rule
    - 7.4.4 Configure the HTTP flood whitelist
    - 7.4.5 Manage SSL certificates
    - 7.4.6 Add Internet websites for protection
    - 7.4.7 Add VPC websites for protection
    - 7.4.8 Verify the configurations of a website on your on-premises server
    - 7.4.9 Modify DNS resolution settings
  - 7.5 System management
    - 7.5.1 View the load status of nodes
    - 7.5.2 View the network status of nodes
    - 7.5.3 View the disk status of nodes
    - 7.5.4 Configure alerts
    - 7.5.5 Configure alert thresholds
- 8 Security Operations Center (SOC)
  - 8.1 View the dashboard
  - 8.2 Security Monitoring
    - 8.2.1 View security monitoring data of tenants
    - 8.2.2 View security monitoring data of the Apsara Stack platform
    - 8.2.3 View the global traffic
  - 8.3 Asset Management
    - 8.3.1 View tenant assets
    - 8.3.2 View platform assets
  - 8.4 Log Analysis
    - 8.4.1 View the Log Overview page
    - 8.4.2 View global logs
    - 8.4.3 Log configurations
      - 8.4.3.1 Manage log sources
      - 8.4.3.2 Create a log collection task
      - 8.4.3.3 Manage log collectors
      - 8.4.3.4 Manage storage policies
    - 8.4.4 Security Audit
      - 8.4.4.1 Overview
      - 8.4.4.2 View security audit overview
      - 8.4.4.3 Query audit events
      - 8.4.4.4 View raw logs
      - 8.4.4.5 Manage log sources
      - 8.4.4.6 Policy settings
        - 8.4.4.6.1 Manage audit rules
        - 8.4.4.6.2 Configure alert recipients
        - 8.4.4.6.3 Manage archives of events and logs
        - 8.4.4.6.4 Manage export tasks
        - 8.4.4.6.5 Modify system settings
  - 8.5 Rules
    - 8.5.1 Create an IPS rule for traffic monitoring
    - 8.5.2 Create IDS rules for traffic monitoring
    - 8.5.3 Manage IDS rules for traffic monitoring
    - 8.5.4 Specify custom thresholds for DDoS traffic scrubbing policies and traffic redirection
    - 8.5.5 View Server Guard rules
  - 8.6 Threat intelligence
    - 8.6.1 Enable the service configuration feature
    - 8.6.2 View the Overview page
    - 8.6.3 Search for and view the information about a suspicious or malicious IP address
  - 8.7 Create a report task
  - 8.8 System Configurations
    - 8.8.1 View and manage metrics
    - 8.8.2 Alert settings
      - 8.8.2.1 Configure alert contacts
      - 8.8.2.2 Configure alert notifications
    - 8.8.3 Updates
      - 8.8.3.1 Overview of the system updates feature
      - 8.8.3.2 Enable automatic update check and update rule libraries
      - 8.8.3.3 Manually import an update package and update your service
      - 8.8.3.4 Roll back a rule library
      - 8.8.3.5 View the update history of a rule library
    - 8.8.4 Global configuration
      - 8.8.4.1 Set CIDR blocks for traffic monitoring
        - 8.8.4.1.1 Add a CIDR block for traffic monitoring
        - 8.8.4.1.2 Manage CIDR blocks for traffic monitoring
      - 8.8.4.2 Region settings
        - 8.8.4.2.1 Add a CIDR block for a region
        - 8.8.4.2.2 Manage CIDR blocks for a region
      - 8.8.4.3 Configure whitelists
      - 8.8.4.4 Configure attack blocking policies
      - 8.8.4.5 Block IP addresses
      - 8.8.4.6 Configure custom IP addresses and locations
        - 8.8.4.6.1 Add custom IP addresses and locations
        - 8.8.4.6.2 Manage custom IP addresses and locations
    - 8.8.5 System Monitoring
    - 8.8.6 Inspect services
    - 8.8.7 Remote operations
      - 8.8.7.1 Enable remote operations
    - 8.8.8 Account management
      - 8.8.8.1 View and modify an Apsara Stack tenant account
      - 8.8.8.2 Add an Alibaba Cloud account
- 9 Optional security products
  - 9.1 Anti-DDoS settings
    - 9.1.1 Overview
    - 9.1.2 View and configure DDoS mitigation policies
    - 9.1.3 View DDoS events
  - 9.2 Data Encryption Service
    - 9.2.1 Data Encryption Service overview
    - 9.2.2 Management of Data Encryption Service instances
      - 9.2.2.1 Create a Data Encryption Service instance
      - 9.2.2.2 Configure a Data Encryption Service instance
      - 9.2.2.3 Release a Data Encryption Service instance

curity

## 1 What is Apsara Stack Security

Apsara Stack Security is a solution that protects Apsara Stack assets with a full suite of security features, such as network, server, application, data, and security management. Background information Traditional security solutions for IT services detect attacks on network perimeters. These solutions use hardware products such as firewalls and intrusion prevention systems (IPSs) to protect networks against attacks. With the development of cloud computing, an increasing number of enterprises and organizations use cloud computing services instead of traditional IT services. Cloud computing features low costs, ondemand flexible configuration, and high resource utilization. Cloud computing environments do not have definite network perimeters. As a result, traditional security solutions cannot effectively safeguard cloud assets. With the powerful data analysis capabilities and professional security operations team of Alibaba Cloud, Apsara Stack Security provides integrated security protection services for networks, applications, and servers. Complete security solution Apsara Stack Security consists of Apsara Stack Security Standard Edition and optional security services to provide a comprehensive security solution.

| Security domain | Service name | Description |
|---|---|---|
| Security management | Threat Detection Service (TDS) | Monitors traffic and overall security status to audit and centrally manage assets. |
| Server security | Server Guard | Protects Elastic Compute Service (ECS) instances against intrusions and malicious code. |
|   | Server Security | Protects physical servers against intrusions. |
| Application security | Web Application Firewall (WAF) | Protects web applications against attacks and ensures that mobile and PC users can securely access web applications over the Internet. |
| Network security | Anti-DDoS | Ensures the availability of network links and improves business continuity. |
| Data security | Sensitive Data Discovery and Protection (SDDP) | Prevents data leaks and helps your business system meet compliance requirements. |
| Security O&M service | On-premises security service | Helps you establish and optimize the cloud security system to protect your business system against attacks by using security features of Apsara Stack Security and other Apsara Stack services. |

## 2 Usage notes

Before you log on to Apsara Stack Security Center, you must verify that your computer meets the configuration requirements. For more information about the configuration requirements, see . Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later GmSSL browser that runs the Chrome kernel: V69.0.0 or later |
| Operating system | Windows XP Windows 7 or later macOS |

## 3 Quick start

### 3.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles in Apsara Stack Security Center are provided by default. You cannot add custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see . Default roles in Apsara Stack Security

| Role | Permission |
|---|---|
| System administrator of Apsara Stack Security Center | Manages and configures system settings for Apsara Stack Security Center. The system administrator has permissions to manage Apsara Stack accounts, synchronize data, configure alerts, and configure global settings. |
| Security administrator of Apsara Stack Security Center | Monitors the security status across Apsara Stack and configures security policies for each functional module of Apsara Stack Security. The security administrator has permissions on all features under Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. Not e The permissions on Web Application Firewall (WAF) must be separately assigned. |
| Department security administrator | Monitors the security status of cloud resources in a specific department and configures security policies for each functional module of Apsara Stack Security for this department. The department security administrator has permissions on all features under Threat Detection, Network Security, Application Security, Server Security, Physical Server Security, and Asset Management. In addition, the department security administrator can specify alert notification methods and alert contacts in the department. Not e The permissions on WAF must be separately assigned. |
| Auditor of Apsara Stack Security Center | Conducts security audits across Apsara Stack. The auditor can view audit events and raw logs, configure audit policies, and access all features under Security Audit. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the Creat e a user topic in Apsara Uni-manager Management Console User Guide.

### 3.2 Log on to Apsara Stack Security Center

Center This topic describes how to log on to Apsara Stack Security Center. Prerequisites q Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Securit y > Apsara St ack Securit y.
5. On the Apsara St ack Securit y Cent er page, select Region.
6. Click YD to go to Apsara Stack Security Center.
e

## 4 Threat Detection Service

### 4.1 Overview

This topic introduces the basic concepts related to Threat Detection Service (TDS). TDS provides comprehensive protection for enterprises. It can monitor vulnerabilities, intrusions, web attacks, DDoS attacks, threat intelligence, and public opinions. TDS uses modeling and analysis to obtain key information based on traffic characteristics, host behavior, and host operation logs. In addition, TDS identifies intrusions that cannot be detected by traffic inspection or file scan. You can use the input of cloud analysis models and intelligence data to discover sources and behavior of attacks and assess threats. TDS provides the following features: Overview: provides a security situation overview and information about security screens. Security Alerts: displays security alerts that occur in your business system. Attack Analysis: displays application attacks and brute-force attacks that occur in your system. Cloud Service Check: checks whether risks exist in the configurations of Apsara Stack services. Application Whitelist: allows you to create and apply application whitelist policies to your servers that require special protection. After you create the policies, Apsara Stack Security identifies trusted, suspicious, and malicious programs based on intelligent learning. This prevents unauthorized programs from running. Assets: manages servers and cloud services on Apsara Stack. Security Reports: allows you to configure security report tasks on Apsara Stack.

### 4.2 Security overview

#### 4.2.1 View security overview information

This topic describes how to view security statistics, attack trends, and network traffic information on the Apsara Stack platform. Context The Securit y Overview tab provides an overview of detected security events, the latest threats, and inherent vulnerabilities of the system. A security administrator can view information on the Securit y Overview tab to better understand the security posture of the system. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Overview. On the page that
appears, click the Securit y Overview tab.
3. View the security posture of the Apsara Stack platform.
e Sections on the Security Overview tab

| Section | Description |
|---|---|
| Secure Score | The security score of assets and the number of detected security risks. |
| Asset Status | The total number of assets and the numbers of servers that are not protected, servers that are stopped, and servers that are at risk. |
| Security Detection And Defense Capabilities | The numbers of precise defense events and anti-tampering events over the last 15 days, the time when the antivirus database was last updated, and the time when vulnerability scanning was last performed. This allows you to obtain the defense situation and security status of your assets in real time. |
| Threat statistics | The numbers of alerts that are not handled, vulnerabilities that are not fixed, baseline risks, and attacks. |
| Config Assessment Risks | Risks in the baseline configurations of cloud services. |
| Issue Resolved | Statistics on alerts, vulnerabilities, and baseline risks that have been processed over the last 15 days. The statistics are displayed in a bar and trend chart. |

### 4.3 Security alerts

#### 4.3.1 View security alerts

This topic describes how to view security alerts on the Security Alerts page. e
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Securit y Alert s.
3. (Optional)Set filter conditions for security alerts.
Not e If you want to view all alerts, do not set the conditions.

| Filter condition | Description |
|---|---|
| Severity | The severity level. You can select one or more levels. Valid values: Urgent Warning Notice |
| Alert status | The status of alerts. Valid values: Unhandled Alerts Handled |
| Alert type | The type of alerts. Select All or a specific type. |
| Affected asset group | The affected asset group. Select Asset Group or a specific group. |
| Search for alerts by name or asset | Enter an alert name or a keyword of affected assets to search for alerts. |

4. View security alerts and their details in the list.

#### 4.3.2 Manage quarantined files

This topic describes how to manage threat files that are quarantined by the system. The system deletes a quarantined file 30 days after the file is quarantined. You can restore the file before it is deleted. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Securit y Alert s.
3. In the upper-right corner of the Alert s page, click Quarant ine.
4. In the Quarant ine panel, view the information about a quarantined file, such as the host, path,
status, and operation time.
5. (Optional)If a file is incorrectly quarantined, click Rest ore in the Act ions column to restore the file.
Not ice Before you can restore a quarantined file, make sure that the file is normal and does not bring risks. The restored file is removed from the quarantine and is displayed in the security alert list again. e

#### 4.3.3 Configure security alerts

This topic describes how to configure logon settings and web directories that are scanned. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Securit y Alert s.
3. In the upper-right corner of the page, click Set t ings.
You can perform the following operations: Manage a common logon locat ion. a. On the right side of Login Locat ion, click Add. b. Select a logon location and the servers that are allowed to be logged on to from the location. c. Click OK. Threat Detection Service (TDS) allows you to edit and delet e added logon locations. Find the target logon location and click Edit on the right side to change the servers that are allowed to be logged on to from this location. Find the target logon location and click Delet e on the right side to delete the logon location. e Conf igure advanced logon set t ings. You can specify the IP addresses, accounts, and time periods that are allowed to log on to your assets. After you configure these settings, alerts are triggered if your assets receive logon requests that do not meet the requirements. The procedure to configure advanced logon settings is similar to that to configure common logon locat ions. You can follow the preceding procedure to add, edit , and delet e advanced logon settings. On the right side of Common Login IPs, enable or disable Uncommon IP Alert. After this function is enabled, alerts are triggered if your assets receive logon requests from unauthorized IP addresses. On the right side of Common Logon T ime, enable or disable Uncommon Time Alert. After this function is enabled, alerts are triggered if your assets receive logon requests at unauthorized time. On the right side of Common Login Account s, enable or disable Uncommon Account Alert. After this function is enabled, alerts are triggered if your assets receive logon requests from unauthorized accounts. Add a web direct ory as t he scan t arget . TDS automatically detects web directories on your servers. It performs dynamic and static scans on these directories. You can also manually add web directories for scanning. a. On the right side of Add Scan T arget s, click Add. e b. Enter a valid web directory and select the servers on which the directory is scanned. The web directory is added to the scan list. Not e To ensure performance and efficiency, do not enter a root directory. c. Click OK.

### 4.4 Attack analysis

This topic describes the statistics provided by the attack analysis feature. The statistics include the total number of attacks, distribution of attack types, top five attack sources, top five attacked assets, and an attack list. Background information The attack analysis feature provides basic attack detection and prevention capabilities in Apsara Stack Security Center. We recommend that you optimize firewalls and enhance business security to develop a more fine-grained and in-depth defense system. On the At t ack Awareness page, you can specify a time range to view these attack details. You can view the attack analysis statistics of the current day, last 7 days, or last 15 days. You can also set Time Range to Cust om to view the statistics of a time range within the last 30 days. At t acks: the total number of attacks detected in your assets within a specific time range. At t ack T ype Dist ribut ion: the attack types and the number of attacks for each type. T op 5 At t ack Sources: the top five IP addresses from which the most attacks are launched. T op 5 At t ack Asset s: the top five assets that are attacked the most frequently. At t ack list : the details about each attack. The details include the attack time, source IP address, attacked asset, attack type, and total number of attacks. Not e The attack list displays a maximum of 10,000 attacks. You can specify T ime Range to view details about the attacks that occur over the specified time range. Paramet ers in t he at t ack list

| Parameter | Description |
|---|---|
| Attacked At | The time at which an attack occurs. |
| Attack Source | The source IP address of an attack. |
| Attacked Asset | The name, public IP address, and private IP address of an attacked asset. |
| Attacks | The total number of attacks. |
| Attack Type | The type of an attack. The types of attacks that can be detected include SSH brute-force attacks and remote code execution attacks. |

Search for an attack. e To search for an attack and view the details about the attack, specify search conditions above the attack list. Search conditions include the attack type, attacked asset, source IP address, and port number. View the details of an attacked asset. To view the details about an attacked asset, move the pointer over the name of the attacked asset. Export the attack list. To export and save the attack list to your computer, click the icon in the upper-left corner above the attack list. The attack list is exported to an Excel file.

### 4.5 Cloud service check

#### 4.5.1 Overview

Threat Detection Service (TDS) provides the cloud service check feature. This feature allows you to check for the configuration risks of your Apsara Stack services. This topic describes the features and check items that are supported by the cloud service check feature. Background information The cloud service check feature allows you to perform network access control and data security checks. The checks help you detect configuration risks of your Apsara Stack services and provide repair solutions. You can view the number of Checked it ems enabled on the Cloud Service Check page. Cloud service check list The following table describes the check items.

| Type | Supported item | Description |
|---|---|---|

e

| Type | Supported item | Description |
|---|---|---|
| Data security | PolarDB - Backup configurations | Checks whether the automatic backup feature is enabled for PolarDB. Regular backups help you improve database security. You can restore data if an error occurs in your database. PolarDB supports automatic backup. We recommend that you enable automatic backup to create a backup on a daily basis. |
|   | Container Registry - Repository permission configurations | Checks whether a Container Registry repository is set to private. Container Registry supports public and private repositories. Public repositories allow users to anonymously download images over the Internet. If images in a repository contain sensitive information, we recommend that you set the repository to private. If images in a repository do not contain sensitive information, ignore related alerts. |
|   | OSS - Server-side encryption | Checks whether the data encryption feature is enabled for Object Storage Service (OSS) buckets. OSS supports server-side encryption to secure data that is persistently stored in OSS. We recommend that you enable server- side encryption to protect sensitive data. |
|   | OSS - Sensitive information leakage scans | Checks whether access permissions on sensitive files in OSS buckets are required. |
|   | ApsaraDB RDS - Cross-region backup configurations | Checks whether the cross-region backup feature is enabled for ApsaraDB RDS instances. ApsaraDB RDS for MySQL provides the cross-region backup feature that automatically synchronizes local backup files to OSS buckets in another region. This implements geo-disaster recovery. We recommend that you enable the cross- region backup feature. |
|   | KVStore for Redis - Backup configurations | Checks whether the data backup feature is enabled for KVStore for Redis instances. |
|   | ApsaraDB for MongoDB - SSL encryption | Checks whether SSL encryption is enabled for ApsaraDB for MongoDB databases. We recommend that you enable the SSL encryption feature to improve the security of data links in ApsaraDB for MongoDB databases. |
|   | ApsaraDB for MongoDB - Backup configurations | Checks whether the automatic backup feature is enabled for ApsaraDB for MongoDB databases. Regular backups help you improve database security. You can restore data if an error occurs in your database. ApsaraDB for MongoDB provides automatic backup policies. We recommend that you enable automatic backup to create a backup on a daily basis. |
|   | ECS - Disk encryption | Checks whether encryption is enabled for disks on Elastic Compute Service (ECS) instances. |

|   |   | User Guide·Threat Detection Servi |
|---|---|---|
| Type | Supported item | Description |
|   | ECS - Automatic snapshot policies | Checks whether the automatic snapshot feature is enabled for the disks on ECS instances. The automatic snapshot feature improves the security of ECS instances and supports disaster recovery. |
|   | OSS - Bucket permissions | Checks whether the OSS bucket ACL is set to private. |
|   | OSS - Logging | Checks whether the logging feature is enabled for OSS. |
|   | OSS - Cross-region replication | Checks whether the cross-region replication feature is enabled for OSS. |
|   | ApsaraDB RDS - Database security policies | Checks whether the SQL audit, SSL encrypted transmission, and transparent database encryption features are enabled for ApsaraDB RDS databases. |
|   | ApsaraDB RDS - Backup configurations | Checks whether the data backup feature is enabled for ApsaraDB RDS instances. |
|   | SSL Certificates Service - Expiration check | Checks whether your SSL certificate expires. If your SSL certificate expires, you are not allowed to use SSL Certificates Service. |
|   | ECS - Security group policies | Checks the security group policies of ECS. We recommend that you grant permissions to users based on the principle of least privilege. We also recommend that you specify 0.0.0.0/0 only for the ports that must be open to all services, such as port 80, 443, 22, or 3389. |
|   | OSS - Bucket hotlink protection | Checks whether the hotlink protection feature is enabled for OSS buckets. The OSS hotlink protection feature checks the Referer header to deny access from unauthorized users. We recommend that you enable this feature. |
|   | VPC - DNAT rules | Checks whether a port is open to the Internet. When you create a DNAT rule for a NAT gateway that is deployed in a virtual private cloud (VPC), we recommend that you do not open internal management ports to the Internet. Do not open all ports or an important port, for example, ports 22, 3389, 1433, or 3306, to the Internet. |
|   | Apsara Stack Security - Back-to-origin configuration for Anti-DDoS | Checks whether Anti-DDoS is configured to allow the requests from only Web Application Firewall (WAF) back- to-origin IP addresses. After you set up Anti-DDoS or WAF, you must hide the IP addresses of the backend servers to prevent attacks on the cloud assets. |

e

|   | ion Servic Apsara Stack Securit |   |
|---|---|---|
| Type | Supported item | Description |
| Network access control | Apsara Stack Security - WAF back-to-origin configurations | Checks whether WAF allows requests from only WAF back-to-origin IP addresses. After you set up Anti-DDoS or WAF, you must hide the IP addresses of the backend servers to prevent attacks on the cloud assets. |
|   | SLB - IP address whitelist configurations | Checks the access control configurations of Server Load Balancer (SLB) instances. Checks whether access control is enabled for HTTP and HTTPS services and checks whether 0.0.0.0/0 is added to the IP address whitelist. |
|   | SLB - Open ports | Checks whether SLB opens ports to the Internet for forwarding unnecessary public services. |
|   | ApsaraDB RDS - IP address whitelist configurations | Checks whether a whitelist is configured for ApsaraDB RDS and whether the whitelist contains 0.0.0.0/0. If the whitelist contains 0.0.0.0/0, requests from all IP addresses are allowed. We recommend that you configure the whitelist to allow requests only from specific IP addresses. |
|   | KVStore for Redis - IP address whitelist configurations | Checks whether a whitelist is configured for KVStore for Redis and whether the whitelist contains 0.0.0.0/0. If the whitelist contains 0.0.0.0/0, requests from all IP addresses are allowed. We recommend that you configure the whitelist to allow requests only from specific IP addresses. |
|   | AnalyticDB for PostgreSQL - IP address whitelist configurations | Checks whether a whitelist is configured for AnalyticDB for PostgreSQL and whether the whitelist contains 0.0.0.0/0. If the whitelist contains 0.0.0.0/0, requests from all IP addresses are allowed. We recommend that you configure the whitelist to allow requests only from specific IP addresses. |
|   | PolarDB - IP address whitelist configurations | Checks whether a whitelist is configured for PolarDB and whether the whitelist contains 0.0.0.0/0 . If the whitelist contains 0.0.0.0/0, requests from all IP addresses are allowed. We recommend that you configure the whitelist to allow requests only from specific IP addresses. |
|   | ApsaraDB for MongoDB - IP address whitelist configurations | Checks whether a whitelist is configured for ApsaraDB for MongoDB and whether the whitelist contains 0.0.0.0/0 . If the whitelist contains 0.0.0.0/0, requests from all IP addresses are allowed. We recommend that you configure the whitelist to allow requests only from specific IP addresses. |

e

#### 4.5.2 Run cloud service checks

e Threat Detection Service (TDS) provides the cloud service check feature. This feature allows you to check for security risks in the configurations of your cloud services. This topic describes how to manually run cloud service checks on your cloud services. This topic also describes how to specify a detection interval for periodic automatic checks. Context Apsara Stack Security supports manual checks and periodic automatic checks to scan for security risks in the configurations of cloud services. Manual checks: On the Cloud Service Check page, you can click Check Now to check for security risks in the configurations of your cloud services. Periodic automatic checks: By default, Apsara Stack Security automatically runs checks during the time range `00:00 - 06:00` every other day. You can also customize a time range for periodic automatic checks. This way, you can detect and handle the security risks in the configurations of your cloud services at the earliest opportunity. Manual checks
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click Securit y.In the Securit y
Management section, click T hreat Det ect ion.
3. In the left-side navigation pane, click Cloud Service Check.
4. On the Cloud Service Check page, click Check Now to check whether the configurations of all
your cloud services contain risks and the number of affected assets. Not e Do not perform other operations until the check is complete. After the check is complete, the detected risks are listed based on risk severities in descending order. Automatic checks
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click Securit y.In the Securit y
Management section, click T hreat Det ect ion.
3. In the left-side navigation pane, click Cloud Service Check.
4. In the upper-right corner of the Cloud Plat f orm Conf igurat ion Assessment page, click
Set t ings.
5. In the Set t ings dialog box, configure the Det ect ion Cycle and Det ect ion T ime parameters.
e Det ect ion Cycle: Valid values are Monday to Sunday. You can select multiple values. Det ect ion T ime: Valid values are `24:00 - 06:00` , `06:00 - 12:00` , `12:00 - 18:00` , and `18:00 - 24:00` . You can select only one time range.
6. Click Ok.
During the selected time range, Apsara Stack Security automatically runs checks based on all check items.

#### 4.5.3 View the check results of configuration assessment for your cloud services and handle the detected risks

assessment for your cloud services and handle the detected risks This topic describes how to view the check results of configuration assessment for your cloud services and handle the detected configuration risks in Apsara Stack Security. You can view the check items, details of check items, potential impacts caused by the detected configuration risks, and suggestions on how to handle the detected configuration risks. You can handle the detected configuration risks on the Cloud Service Check page in a centralized manner. View check results
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click Securit y.In the Securit y
Management section, click T hreat Det ect ion.
3. In the left-side navigation pane, click Cloud Service Check.
4. On the Cloud Service Check page, view the details of check results.
e View t he st at ist ics of t he last check You can view the total number of at-risk items and the numbers of risks at different levels in the At -Risk It ems section, and the number of assets on which risks are detected in the Risks section. You can also view the number of disabled check items in the Check Items Not Enabled section, the number of enabled check items in the Checked Items Enabled section, and the time when the check was last performed in the Last Checked At section. View check it ems You can view the information about the check items in the check item list. The information includes the risk severities of check items, the number of affected assets, the types of affected assets, the types of check items, and the time when the check was last performed. View t he det ails of check result s You can click the name of a check item in the Checked It em column to go to the panel that displays the details of the check item. In the panel, you can view the description of the check item, potential impacts caused by the detected risks, and suggestions on how to handle the risks. Handle the detected configuration risks of your cloud services
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click Securit y.In the Securit y
Management section, click T hreat Det ect ion.
3. In the left-side navigation pane, click Cloud Service Check.
4. On the Cloud Service Check page, handle the configuration risks detected on your cloud services.
Verif y t he conf igurat ions af t er modif icat ion e If you have modified the configurations for which risks are detected, find the check item in the check item list and click Verif y in the Actions column to check whether the new configurations are at risk. Add check it ems t o a whit elist If you trust a check item for which risks are detected, find the check item in the check item list and click Whit elist in the Actions column to add the check item to a whitelist. Then, the state of the check item is displayed as Ignored in the Severity/Affected Assets column. Ignored check items are not counted in the total number of at-risk items in the At -Risk It ems section. In the check item list, you can click Remove to remove the ignored check items from the whitelist. Not e Af t er you add a check it em t o t he whit elist , t he risk t hat is det ect ed f or t he check it em is ignored only f or t his t ime. If t he risk is det ect ed again, Apsara St ack Securit y st ill displays t he check result of t his check it em.

### 4.6 Application whitelist

The application whitelist feature prevents unauthorized programs from running on your servers and provides a trusted running environment for your servers. Context The application whitelist feature allows you to apply application whitelist policies to your servers that require special protection. Apsara Stack Security identifies trusted, suspicious, and malicious programs based on the policies. Then, you can add the identified programs to an application whitelist based on your business requirements. This prevents unauthorized programs from running. This feature protects your servers from untrusted and malicious programs and improves resource usage. After you create an application whitelist policy, you can apply it to a server that requires special protection. Then, Apsara Stack Security scans for suspicious or malicious programs on the server and generates alerts for the programs that are not in the application whitelist. e If a program that is not in the application whitelist starts, an alert is generated. The program may be a normal program that is newly started or a malicious program that is inserted into your compromised server. If the program is a normal program, a frequently used program, or a thirdparty program installed by you, we recommend that you add the program to the application whitelist. After you add the program to the application whitelist, Apsara Stack Security no longer generates alerts for this program the next time the program starts. If the program is malicious, we recommend that you immediately delete this program and check whether the configuration files such as cron tasks are tampered with. Step 1: Create an application whitelist policy
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Applicat ion Whit elist s.
3. On the Applicat ion Whit elist page, click the Policies tab.
4. On the App Control page, click the Policies tab. Then, click Creat e Policy.
5. In the Create Policy step of the Creat e Whit elist Policy panel, configure the following
parameters: Policy Name: the name of the application whitelist policy. Int elligent Learning Durat ion: the duration for Apsara Stack Security to perform intelligent learning. Valid values: 1 Day, 3 Days, 7 Days, and 15 Days. The intelligent learning feature uses machine learning to automatically collect and categorize large amounts of alert data. Apsara Stack Security can identify suspicious or malicious processes based on the collected data. Servers f or Int elligent Learning: the servers to which you want to apply the application whitelist policy.
6. Click Next to create the application whitelist policy.
After the application whitelist policy is created, the policy details are displayed in the policy list on the Policies tab. The following table describes the parameters in the list of application whitelist policies.

| Parameter | Description |
|---|---|
| Policy Name | The name of the application whitelist policy. |

| Guide·Threat Detection Se | rvic Apsara Stack Securit |
|---|---|

e

| Parameter | Description |
|---|---|
| Servers | The number of servers to which the application whitelist policy is applied. |
| St at us | The status of the policy. Valid values: Applied: Intelligent learning is complete. The policy has been applied to servers. Pending Conf irmat ion: Intelligent learning is complete. The policy must be confirmed and enabled. After intelligent learning is complete, you must turn on the switch in the Policy St at us column to enable this policy. The policy takes effect only after it is enabled. Apsara Stack Security automatically identifies the programs on your servers as trusted, suspicious, or malicious programs. Paused: Intelligent learning is manually paused. You can click Cont inue in the Actions column to resume intelligent learning. Learning: Intelligent learning is in progress. After an application a whitelist policy is created, Apsara Stack Security automatically performs intelligent learning based on the policy. The status of a new application whitelist policy is Learning. |
| Applicat ions | The number of programs of each type on all servers to which the policy is applied. The program types include trusted, suspicious, and malicious. |
| Act ions | The operations that you can perform on a policy. You can perform the following operations: Apply: Add or remove servers to which the policy is applied in the Apply Whit elist Policy panel. Modif y: Modify the policy in the Modif y Whit elist Policy panel. You can change the values of Policy Name and Int elligent Learning Durat ion, and add or remove the servers on which intelligent learning is automatically performed. Pause Learning: Pause intelligent learning. Cont inue: Resume intelligent learning. After you click Cont inue, the status of the policy changes to Learning. You can view the learning progress of the policy in the St at us column. Delet e: Delete the policy. After the policy is deleted, the servers to which the policy is applied are no longer protected by the policy. |

Step 2: Apply the created application whitelist policy to servers
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Applicat ion Whit elist s.
3. On the Servers tab of the App Control page, click Add Server.
4. In the Add Server panel, configure the following parameters:
Whit elist Policy: Select the created application whitelist policy from the drop-down list. e Event Handling: The default value is Alert , which indicates that Apsara Stack Security generates an alert when a suspicious program is detected. If a program that is not in the application whitelist starts, Apsara Stack Security automatically generates an alert. You can click the number in the Suspicious Event s column to go to the Alert s tab of the server details page and view the alert details. Servers: Select the server to which you want to apply the application whitelist policy. You can select multiple servers. To search for a server, enter the server name in the Servers search box and click the search icon. Fuzzy mat ch is support ed.
5. Click OK. The application whitelist policy is applied to the selected servers.
After the application whitelist is created, you can view the protected servers and the name of the application whitelist policy in the server list on the Servers tab. The Servers tab displays the following information of a protected server: Server Name/IP: the name and IP address of the server to which the application whitelist policy is applied. Whit elist Policy: the name of the application whitelist policy that is applied to the server. Suspicious Event s: the number of programs that are not in the application whitelist and have started. If a suspicious program starts on the server, Apsara Stack Security detects the program and generates an alert. Event Handling: The default value is Alert , which indicates that Apsara Stack Security generates an alert when a suspicious program is detected. If a program that is not in the application whitelist starts, Apsara Stack Security automatically generates an alert. You can click the number in the Suspicious Event s column to go to the Alert s tab of the server details page and view the alert details. Act ions: After you click Delet e in the Act ions column, the application whitelist policy no longer applies to the server. After you click Delete in the Actions column, the application whitelist policy becomes invalid for the server. In this case, if a program that is added to the application whitelist starts on this server, Apsara Stack Security generates an alert. Add a program to or remove a program from an application whitelist After you configure an application whitelist policy for your server, you can view the detailed information in the server list on the Servers tab. The information includes the details of the protected server and the name of the application whitelist policy that is applied to the server. You can click a policy name in the Whit elist Policy column to view the programs running on the server. You can also view the number of trusted, suspicious, and malicious programs and their detailed information. The following information about each program on the server is displayed: T ype: the type of the program. Programs are classified into trusted, suspicious, and malicious programs. Process Name: the name of the program. Hash: the hash function of the program. A hash function is used to identify whether a program is unique. This helps protect servers against malicious programs. Pat h: the file path of the program on the server. Degree of T rust abilit y: the degree of trustability for the program. The value of this parameter is e determined by Apsara Stack Security. Valid values: 0%, 60%, and 100%. The value 0% indicates malicious programs, 60% indicates suspicious programs, and 100% indicates trusted programs. Not e We recommend that you handle the program whose Degree of Trustability is 0% at the earliest opportunity. Act ions: the operations that can be performed on the program. You can determine whether to add the program to the whitelist based on the services deployed on your server. You can perform the following operations: Add t o Whit elist : If you trust the program, add it to the whitelist. Remove f rom Whit elist : After you remove the program from the whitelist, Apsara Stack Security identifies the program as untrusted. If this program starts, Apsara Stack Security generates an alert.

### 4.7 Assets

#### 4.7.1 View the security status of a server

The Assets page displays security information about each protected server. The information includes the virtual private could (VPC) where each server resides, server status, and risk status. This topic describes how to search for specific servers and view the security status of these servers. This topic also describes how to specify search conditions and select the items that you want to display on the Assets page. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server(s) tab of the Assets page, view the security status of each server.
You can perform the following operations: Filt er servers by st at us e In All server, you can view the numbers of all servers, risky servers, unprotected servers, new servers, and servers that are shut down. To view the security information about a server, you can click the name of the server or click Fix in the Act ions column. For more information, see View the details of a single asset. You can click Risky server, Unprot ect ed server, Shut down Server(s), or New Server(s) to view security information about specific servers. Filt er servers by group You can click Server Group to view the numbers of all servers, servers that are at risk, and unprotected servers in each server group. You can also view the total number of server groups. To manage server groups, you can click Manage or Delet e in the Actions column. For more information, see Manage asset groups. You can select a server group and click the number in the Servers, Risk, or Unprot ect ed column to view the security information about specific servers in this group. Filt er servers by VPC ID e You can click VPC to view the numbers of all servers, servers that are at risk, and unprotected servers in each VPC. You can also view the total number of VPCs. You can find a VPC and click the number in the Servers, Risk, or Unprot ect ed column to view the security information about specific servers in this VPC. Filt er servers by t ag In the navigation tree, you can click a tag to view the security information about servers to which the tag is added. Filt er servers by condit ion If you click All Servers, Server Group, VPC, or a tag in the navigation tree, you can specify filter conditions above the right-side list to search for specific servers. Use one filter condition to search for specific servers: You can select a filter condition and select or enter keywords to search for specific servers. The filter conditions include Int ernet IP, Privat e IP, Inst ance name, Syst em, Baseline problems, Vul problems, Alert problems, Risk St at us, Online or Of f line, T ag, Group name, OS, and Is t here a snapshot risk. Not e You can specify multiple filter conditions at a time and specify a Boolean operator for the conditions. The following list describes the Boolean operators: Boolean operators: AND: specifies the AND logical relation for the conditions. OR: specifies the OR logical relation for the conditions. If you want to search for servers that meet at least one of the filter conditions, you must set the Boolean operator to OR. If a filter condition requires you to enter a keyword, you must enter the keyword and click the Search icon. Results are displayed only after you click the Search icon. Use multiple filter conditions to search for specific servers: If you select multiple filter conditions, they are all applied to search for specific servers. You can also click Server Group, VPC, or a tag, and use the search box above the asset list to search for specific servers. Save f requent ly used f ilt er condit ions e You can save the filter conditions that are applied as frequently used search conditions. To save the conditions, click Save above the right-side list, and enter a name in the Save condit ion dialog box. Then, you can select the saved conditions from the Frequent search condit ions drop-down list on the right of the Search icon. Cust omize displayed it ems On the Asset s page, you can click the icon in the upper-right corner. Then, you can select the items that you want to display on the Assets page.

#### 4.7.2 View the security status of cloud services

The Assets page displays the security information about each protected cloud service. The information includes the at-risk services and the types of services such as SLB and NAT Gateway. This topic describes how to configure search conditions to view the security status of cloud services. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Cloud Product tab of the Assets page, view the security status of cloud services.
You can perform the following operations based on your business requirements: Search by asset st at us In the left-side pane of the Cloud Product tab, you can view the numbers of All cloud product and Risky cloud product . You can also view the security status of all cloud services. Click Risky cloud product to view the cloud services that are at risk. You can click the name of the required cloud service or click View in the Actions column that corresponds to a service to view detailed information. For more information, see View the details of a single asset. Search by asset t ype Cloud services are classified into two asset types: SLB NAT Gat eway In the left-side pane of the Cloud Product tab, you can view the number of cloud services of each type. You can click SLB or NAT to view the security status of the required cloud service. Search by t ag e In the T ag section in the left-side pane of the Cloud Product tab, you can view the number of cloud services to which each tag is added. You can click a tag to view the security status of cloud services to which the tag is added. Filt er by search condit ion You can click All cloud product , SLB, or NAT in the left-side pane of the Cloud Product tab and configure search conditions in the search box to search for specific assets. For example, you can click All cloud product and configure search conditions to search for specific assets. Use multiple subconditions to search for specific assets: Select a condition from the drop-down list of the search box on the Cloud Product tab, and select a subcondition or enter a keyword into the search box to search for specific assets. Supported search conditions are Int ernet IP, Inst ance name, Alert problems, Risk St at us, T ag, and Group name. Not e Use multiple filter conditions to search for specific servers: Apply multiple search conditions. You can click SLB, NAT , or a tag specified in the T ag section and configure conditions in the search box on the Cloud Product tab to search for specific assets. You can also click All cloud product , SLB, or NAT and select a tag specified in the T ag section to search for specific assets. Set f requent ly used search condit ions You can save the filter conditions that are applied as frequently used search conditions. Click Save below the search box and enter a name in the Save condit ion dialog box. Then, you can select the saved search condition from the Frequent search conditions drop-down list on the right of the search box.

#### 4.7.3 View the details of a single asset

The Assets page provides details about all assets. These details include basic information, alert management status, baseline check analysis, and asset fingerprints. This topic describes how to view the details of a server or a cloud service. Context The basic information about assets is displayed on the Asset s page. Different types of assets, such as servers and cloud services, are managed in different ways. The following table lists the features that are supported by servers and cloud services on the Asset s page. The following list describes the marks that are used to indicate whether a feature is supported by servers or cloud services: Cross (×): not supported. Tick (√): supported. e

| Feature | Description | Server | Cloud service |
|---|---|---|---|
| Basic Information | Risk state: displays the number of risks detected on an asset. The following types of risks can be detected: Vulnerabilit y Alert Baseline risk | √ | √ (Only alerts can be processe d.) |
|   | Detail: displays the configuration and protection status of an asset. You can specify a group and a tag for the asset. | √ | √ (Asset grouping is not supporte d.) |
|   | Asset investigation: displays asset fingerprints, including ports, software, processes, and accounts. | √ | X |
|   | Vulnerability check: displays the types of vulnerabilities that can be detected. You can specify the types of vulnerabilities that you want to detect for an asset. | √ | X |
|   | Login security setting: displays the configured logon locations, IP addresses, time periods, and accounts. You can manage relevant alerts for an asset. | √ | X |
| Vulnerabilities | Displays the results of vulnerability detection on an asset. | √ | X |
| Alerts | Displays the alerts that are generated for an asset. | √ | √ |
| Baseline Risks | Displays the results of the baseline check on an asset. | √ | X |
| Asset Fingerprints | Displays the details of asset fingerprints for an asset. | √ | X |

Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Asset s page, click the Server(s) or Cloud Product tab.
4. On the Server(s) or Cloud Product tab, find the required asset and click its name.
5. View the details of the asset.
On the asset details page, click the Basic Inf ormat ion, Vulnerabilit ies, Alert s, Baseline Risks, or Asset Fingerprint s tab to view relevant details. The following list describes the details of the asset: Basic Inf ormat ion: This tab consists of sections in which you can view asset details and e manage an asset. Risk St at e: This section displays the numbers of vulnerabilities, alerts, and baseline risks on the asset. You can click the number under Vulnerabilities, Alerts, or Baseline Risks to view the details. Det ail: This section displays information about the asset configuration and security protection settings, and allows you to manage asset tags and groups. Change asset groups Click Group. In the Group dialog box, select a new group and click OK. Modif y t ags Click the icon. In the Add t ag dialog box, select a tag and click OK. You can click the icon in the right of a tag to delete the tag. Asset Invest igat ion: This section displays the fingerprints of an asset. You can click the number under an item to go to the Asset Fingerprint s tab to view the details. Vulnerabilit y check: This section displays vulnerability check items that are enabled or disabled for an asset. You can enable or disable different types of vulnerability checks for the asset. The vulnerabilities include Linux software vulnerabilities, Windows system vulnerabilities, Web CMS vulnerabilities, and urgent vulnerabilities. e Login securit y set t ing: This section allows you to specify approved logon locations, configure advanced logon settings, and turn on or turn off alerting for unapproved IP addresses, time, and accounts. The advanced logon settings include approved IP addresses, time periods, and accounts. You can also specify approved IP addresses, time periods, and accounts for a specific asset. Vulnerabilit ies: This tab displays vulnerabilities detected on an asset. Alert s: This tab displays alerts generated for an asset. Baseline Risks: This tab displays baseline risks of an asset. Asset Fingerprint s: This tab displays the fingerprints, including ports, processes, software, and accounts of an asset. e You can manually collect the latest fingerprints of an asset. a. You can click the Port , Sof t ware, Process, Account , or Scheduled T asks tab. In the upper-right corner, click Collect dat a now. b. In the Collect dat a message, click OK. After the data collection task is submitted, it takes one to five minutes to collect the fingerprints of the required asset. After the data collection task is complete, you can view the latest fingerprints of the asset.

#### 4.7.4 Enable and disable server protection

This topic describes how to enable and disable server protection. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server(s) tab of the page that appears, enable or disable server protection for specified
servers. Enable server prot ect ion Select one or more servers where the agent is in the Close state, and choose More operat ions
> T urn on prot ect ion.

After server protection is enabled, the status in the Agent column changes to Enable. Disable server prot ect ion If you confirm that a server does not require protection from Apsara Stack Security, you can disable protection for the server. Select one or more servers where the agent is in the Enable state, and choose More operat ions > Suspend Prot ect ion. Not e After server protection is disabled, Apsara Stack Security stops protecting your servers. For example, Apsara Stack Security no longer detects vulnerabilities or generates alerts for detected risks. We recommend that you proceed with caution. After server protection is disabled, the status of the agent on your servers changes to Close.

#### 4.7.5 Perform a quick security check

The Server tab of the Assets page allows you to run security checks. You can dispatch security check tasks to scan for vulnerabilities, baseline risks, or webshells, and collect asset fingerprints on a specific server. The asset fingerprints are ports, software, processes, and accounts. This topic describes how to perform a security check on servers. e
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server tab, select one or more servers on which you want to perform a security check.
4. In the lower part of the page, click Securit y check.
5. In the Securit y Check dialog box, select check items.
6. Click OK to start the check.
7. In the message that appears, click OK.
After the security check is complete, the check results are automatically displayed on the details pages of the selected servers.

#### 4.7.6 Manage server groups

This topic describes how to create, modify, delete, and replace server groups. Create a server group
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server(s) tab of the page that appears, click Server Group in the navigation tree.
e Not e By default, the assets that are not grouped are in the Def ault group.
4. Click Add group.
5. In the Add group dialog box, configure parameters for the new group.
To configure the parameters, perform the following steps: i. Enter a name for the new group in the Group name field. e ii. Add servers to the new group. You can add servers in the Default group to the new group. You can also move servers from another group to the new group. To add or move servers, select Def ault or other groups in the Asset Group section, and select or clear the required check boxes in the asset list in the right area of the section.
6. Click OK.
In the server group list, you can view the new group. Modify or delete a server group The following procedure describes how to modify or delete a server group. When you modify a server group, you can rename the group or adjust the servers in the group.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server(s) tab of the page that appears, click Server Group in the navigation tree.
4. Find the server group that you want to modify or delete. In the Actions column, click Manage or
Delet e. You can perform the following operations based on your business requirements: Modif y t he group a. In the Actions column, click Manage. The Group dialog box appears. b. In the Group dialog box, select the group in the Asset Group section. c. In the right area of the section, clear the check boxes that correspond to the required servers in the asset list. d. Click OK. The server group is modified. Delet e t he group In the Actions column, click Delet e. In the message that appears, click OK. Not e After you delete a group, servers in this group are moved to the Def ault group. Replace a server group You can add servers to a server group to manage multiple servers at a time. We recommend that you add the same types of servers to a server group. For example, if you configure a baseline check template, you can specify a server group and apply the template to all servers in the group. You can also filter and view servers based on server groups. To add servers to a specific server group, perform the following steps:
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the Server(s) tab of the page that appears, select one or more servers and click Group in the
lower part of the page.
4. In the Group dialog box, select a new server group.
e
5. Click OK.

#### 4.7.7 Manage asset tags

This topic describes how to add asset importance tags to your assets and how to create, modify, and delete custom tags. Context Apsara Stack Security provides the asset importance tags described in the following table to classify assets. You can select appropriate importance tags for your assets. An asset importance tag is transformed to an asset import ance score. An asset import ance score is used to calculate a vulnerability priority score. You can determine whether to preferentially fix a vulnerability based on the vulnerability priority score. We recommend that you add importance asset tags to core assets. Apsara Stack Security prompts you to fix vulnerabilities based on the importance of each asset. The following table describes the relationships between asset importance tags and asset importance scores.

| Asset importance tag | Asset importance score | Recommendation |
|---|---|---|
| Important Assets | 1.5 | Assets that are related to crucial business or store core business data. Virus intrusion into the assets adversely affects the system and causes major loss. |
| General Assets | 1 | Assets that are related to non-crucial business and are highly replaceable. Virus intrusion into the assets causes less impact on the system. |
| Test Assets | 0.5 | Assets for functional or performance tests, or assets that can cause less impact on the system. |

Not e If you do not add asset importance tags, the General Asset s tag is automatically added to each asset. This tag indicates that the asset importance score is 1. Create a custom tag
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the page that appears, click the Server(s) or Cloud Product tab.
4. In the navigation tree of the Server(s) or Cloud Product tab, click Management on the right of
T ag.
5. In the Add t ag dialog box, enter the tag name in the T ag field.
e
6. In the Asset Group section, select a server group. Then, select the required servers to add the new
tag to the selected servers in the right area of the section.
7. Click OK.
In the asset list of the Server(s) or Cloud Product tab, you can click the icon in the T ag column to add the new tag to an asset. Not e You can add multiple tags to one asset. All tags of an asset are displayed in the T ag column. Modify or delete a custom tag The following procedure describes how to modify or delete a custom tag. When you modify a tag, you can rename the tag or adjust the servers to which the tag is added.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Asset s.
3. On the page that appears, click the Server(s) or Cloud Product tab.
4. On the Server(s) or Cloud Product tab, modify or delete a tag.
Perform the following operations to modify or delete a tag: Modif y a t ag e a. Find the tag that you want to modify and move the pointer over the icon on the right of the tag. b. In the T ag dialog box, enter a new name in the T ag field, add the tag to more servers, or remove the tag from specific servers. c. Click OK. Delet e a t ag Find the tag that you want to delete and click the icon in the Tag column. In the message that appears, click OK.

### 4.8 Vulnerability scan

#### 4.8.1 Quick start

This topic describes how to get started with the vulnerability scan feature. The following procedure shows how to use the vulnerability scan feature:
1. Configure the following detection items and the required cycles based on your environment
requirements: Overall Monitoring: Configure detection features and the monitoring cycle of each detection feature. For more information, see Configure overall monitoring. Basic Monitoring: Configure Weak Password Vulnerability Monitoring, Operation Security Vulnerability Monitoring, CMS Application Vulnerability Monitoring, and Baseline Monitoring. For more information, see Configure basic monitoring. Web Monitoring: Configure the monitoring cycle and the types of web vulnerabilities that you want to monitor. For more information, see Configure web monitoring. Whitelist: Add the assets that do not require detection to the whitelist. For more information, see Configure a whitelist.
2. Import assets that require vulnerability scans.
Import internal assets: Configure a scan engine to import your internal assets in virtual private clouds (VPCs). For more information, see Configure a scan engine for internal assets. Import Internet assets: Import your Internet assets. For more information, see Import assets. e The number of imported assets cannot exceed the specified upper limit.
3. View and confirm the results of vulnerability scans.
View the overall information to obtain the results of vulnerability scans. For more information, see View the information on the Overview page. View and confirm vulnerability risks. For more information, see Manage security vulnerabilities. View and confirm host compliance risks. For more information, see Manage host compliance risks.
4. Generate vulnerability scan reports.
Generate reports to audit the vulnerabilities and baseline risks on assets on a regular basis. For more information, see Create a report.

#### 4.8.2 View the information on the Overview page

This topic describes the overall results of vulnerability scans. Security administrators can understand the vulnerability situation based on the overall results. Context The vulnerability scan feature can identify the following vulnerabilities: web security vulnerabilities, content management system (CMS) application vulnerabilities, weak password vulnerabilities, O&M security vulnerabilities, and baseline security vulnerabilities. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan > Overview.
3. View the overall results of vulnerability scans.

| Section | Description |
|---|---|

e

| Section | Description |
|---|---|
| T oday's at t ent ion | View Asset Overview, Disclosured Risk, and Resolved Risk of the current day. Asset Overview: displays the numbers of hosts, websites, and domain names for the current day and provides a security score for the current assets. The radar chart on the right shows the distribution of web security vulnerabilities, CMS application vulnerabilities, weak password vulnerabilities, O&M security vulnerabilities, and baseline security vulnerabilities. Disclosured Risk: displays the numbers of high-risk vulnerabilities, medium-risk vulnerabilities, and low-risk vulnerabilities, and the total number of these vulnerabilities for the current day. These vulnerabilities are not fixed. The Disclosured Risk Dist ribut ion section on the right displays the distribution of unfixed vulnerabilities. Resolved Risk: displays the numbers of high-risk vulnerabilities, medium- risk vulnerabilities, and low-risk vulnerabilities, and the total number of these vulnerabilities for the current day. These vulnerabilities are fixed. The Resolved Risk Dist ribut ion section on the right displays the distribution of fixed vulnerabilities. |
| Asset Risk T op 5 | View the top five assets that are at risk on the Securit y Vulnerabilit ies and Host Compliance tabs. These assets are displayed by asset or group. |
| Risk Monit oring T rend | View the trend charts of vulnerabilities on the Securit y Vulnerabilit ies and Host Compliance tabs. Fixed and unfixed vulnerabilities are identified by lines in different colors. You can move the pointer over a line to view the numbers of unfixed vulnerabilities and fixed vulnerabilities for the specific day. |
| Asset Monit oring T rend | View the trends in the numbers of protected hosts and websites. Hosts and websites are identified by lines in different colors. You can move the pointer over a line to view the number of protected hosts and websites for the specific day. |
| Risk Asset Ranking List | View the rankings of assets that are at risk on the Lat est Risk and High Risk tabs. |
| Port Service St at ist ics | View the statistics on the Port and Host Service tabs. |

#### 4.8.3 Asset management

##### 4.8.3.1 View the results of asset analysis

e This topic describes how to view the analysis results of websites and hosts. Context The asset analysis feature allows you to view the analysis results of websites and hosts. For the websites, you can view Web Service, Open Source Framework, and Device Type. For the hosts, you can view Host Port, Host Service, and Operation System. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Asset .
4. On the Asset page, click the Asset Analysis tab to view websites.
5. View hosts.
e

##### 4.8.3.2 Import assets

This topic describes how to import Internet assets. Context The vulnerability scan feature works only on imported assets. If you want to scan the vulnerabilities of your assets, you must import your assets. The assets that the feature supports include Internet assets and internal assets. The internal assets refer to the assets in a virtual private cloud (VPC). To import internal assets, you must add a scan engine. For more information, see Configure a scan engine for internal assets. To import Internet assets, perform the operations provided in this topic. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Asset .
4. On the Asset page, click the Asset Import tab to view imported assets.
e
5. Click Asset Import . On the Public net work asset Import page, create an asset import task.
i. In the Import Asset section, select Manual Import and enter the required assets in the field. Then, read and select the disclaimer. You can enter domain names, URLs, IP addresses, and CIDR blocks. You can enter the information about multiple assets at a time. Press Enter after you enter the information about one asset. You cannot enter the information about the assets in VPCs. The number of imported assets must be less than the number of remaining assets supported by the platform. Not e For example, if the number of remaining assets supported by the platform is 100 and 90 assets are entered, all the assets can be scanned. If 110 assets are entered, only 100 assets can be scanned, and the 10 assets that remain cannot be scanned. ii. In the Asset Inf o section, group the imported assets and configure an owner and a tag for the assets. Asset Group: Select a group from the drop-down list. You can click the icon to create, edit, or delete a group. Person in charge: Select an owner from the drop-down list. You can click the icon to create, edit, or delete an owner. Asset T ag: Click Add T ag to add a tag to the imported assets. e iii. In the Import Set section, select the operations that you want to perform after the assets are imported.

| Operation |   | Description |
|---|---|---|
| Asset Discovery | Auto Import subdomains | Automatically queries the subdomain assets of the imported domain names. |
|   | Auto import associated IP | Automatically adds IP address assets that are mapped to the domain names. |
|   | Auto synchro nize tags an d groups | Applies the group and tag of the imported assets to the assets that are discovered by the system. |
| Web Asset | Open WEB M onitoring | Enables the web monitoring feature on the imported website assets. If you want to select the web monitoring rules to use, click the icon. In the dialog box that appears, select the required web monitoring rules. For more information about how to configure web monitoring rules, see Configure web monitoring. |

iv. In the Whit elist section, add the assets that do not need to be scanned. You can enter IP addresses and URLs. If you add more than one asset, you must press Enter after you enter the information about an asset. v. Click Save.
6. Manage the created asset import task.
After the asset import task is created, you can view the task in the task list. You can also perform the following operations on the new asset import task.

| Icon | Description |
|---|---|
|   | View the details, results, and process of the asset import task. |
|   | Delete the asset import task. |

##### 4.8.3.3 Manage assets

This topic describes how to view and manage assets. Context You can view the information about assets in the asset list. If the purpose or owner of an asset changes, security administrators can move the asset to another group or change the owner. e
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerability Scan pane, click Asset .
4. On the Asset page, click the Asset List tab to view assets.
5. Click the Web Asset tab and manage websites.
i. Specify filter conditions to search for specific websites. The filter feature allows you to search for the required websites in a more efficient manner.

| Filter condition | Description |
|---|---|
| Asset T ype | The asset type, such as Internet assets or a specific VPC. |
| Asset Source | The source from which the asset is imported. Valid values: Manual and Syst em Find. |
| Asset Group | The group to which the asset belongs. |
| Web St at us | The status of the website. |
| Person in charge | The owner of the website. |
| Asset Change | The change status of the asset. Valid values: All, New, Updat e, No Updat e, and Of f line. |
| Web Monit oring | The monitoring status of the website. |
| Risk Level | The risk level of the asset. |
| Web Service | The service type and version of the website. |
| WAF Recognit ion | Specifies whether the asset is identified by WAF. |
| Open Source Framework | The open source framework type of the asset. |
| Device T ype | The type of the device. |
| Time range | The time range during which assets are imported. |
| Key information | The crucial information of the asset. The crucial information includes the website, domain name, IP address, title, and tag. |

ii. Click Export to export the asset list to an Excel file. e iii. Select one or more websites that you want to manage. The following table describes the operations that you can perform on websites.

| Action | Description |
|---|---|
| Bat ch Web Monit oring | Allows you to enable or disable web monitoring for multiple websites. Bat ch Open Monit oring: To enable web monitoring for multiple websites, select Batch Open Monitoring from the drop-down list of Batch Web Monitoring. Bat ch St op Monit oring: To disable web monitoring for multiple websites, select Batch Stop Monitoring from the drop-down list of Batch Web Monitoring |
| Change Group | Allows you to change the asset group of multiple assets at a time. |
| Change Person in charge | Allows you to change the owner of multiple assets at a time. |
| Bat ch Delet e | Allows you to delete multiple assets at a time. After the assets are deleted, the assets are not scanned by the vulnerability scan feature. |

6. Click the Host Asset tab and manage the hosts.
e i. Specify filter conditions to search for specific hosts. The filter feature allows you to search for the required hosts in a more efficient manner.

| Filter condition | Description |
|---|---|
| Asset T ype | The asset type, such as Internet assets or a specific VPC. |
| Asset Source | The source from which the asset is imported. Valid values: Manual and Syst em Find. |
| Asset Group | The group to which the asset belongs. |
| Person in charge | The owner of the asset. |
| Asset Change | The change status of the asset. Valid values: All, New, Updat e, No Updat e, and Of f line. |
| Risk Level | The risk level of the asset. Valid values: All, High, Middle, Low, and Securit y. |
| SurviveSt at us | The status of the asset. Valid values: Alive and Close. |
| Operat ion Syst em | The operating system of the host. |
| Host Port | The port of the host. |
| CDN Recognit ion | Specifies whether Content Delivery Network (CDN) is configured for the asset. |
| Host Service | The service of the host. |
| Time range | The time range during which assets are imported. |
| Key information | The crucial information of the asset. The crucial information includes the IP address, host, tag, and domain name. |

ii. Click Export to export the asset list to an Excel file. iii. Select one or more hosts that you want to manage. The following table describes the operations that you can perform on hosts.

| Action | Description |
|---|---|
| Change Group | Allows you to change the asset group of multiple assets at a time. |
| Change Person in charge | Allows you to change the owner of multiple assets at a time. |
| Bat ch Delet e | Allows you to delete multiple assets at a time. After the assets are deleted, the assets are not scanned by the vulnerability scan feature. |

##### 4.8.3.4 Manage asset availability

e This topic describes how to manage the availability of assets. Context If hosts or websites are used for a long period of time, they may become unavailable due to errors. Availability monitoring allows a security administrator to discover unavailable assets. Then, the security administrator can troubleshoot the issues that cause the assets to become unavailable. Availability monitoring supports the following methods: HTTP monitoring: This method is used to monitor websites. PING monitoring: This method is used to monitor hosts. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Asset .
4. On the Asset page, click the Availabilit y Monit oring tab to view availability monitoring tasks.
5. Create an availability monitoring task.
Availability monitoring supports HTTP monitoring and PING monitoring. To create an HTTP monitoring task, perform the following steps: a. Click Add Monit oring. b. Click the HT T P Monit oring tab. e c. Configure the following parameters.

| Parameter | Description |
|---|---|
| Monit oring Name | The name of the availability monitoring task. |
| Monit oring T arget | The website that you want to monitor. |
| Monit oring Frequency | The interval at which you want to monitor the website. Valid values: 1 Minut e, 5 Minut e, 15 Minut e, and 30 Minut e. |
| Request Met hod | The request method that is used to send HTTP request packets. Valid values: HEAD, GET , POST , and PUT . |
| Alert Set t ing | The policy based on which Apsara Stack Security reports alerts. If one of the following conditions is met, the website is unavailable: Response Time: If the actual response time is greater than the specified value, an exception occurs. Response Status: If an unexpected status code is returned, an exception occurs. |

d. Click Save. To create a PING monitoring task, perform the following steps: a. Click Add Monit oring. b. Click the PING Monit oring tab. e c. Configure the following parameters.

| Parameter | Description |
|---|---|
| Monit oring Name | The name of the availability monitoring task. |
| Monit oring T arget | The host that you want to monitor. |
| Monit oring Frequency | The interval at which you want to monitor the host. Valid values: 1 Minut e, 5 Minut e, 15 Minut e, and 30 Minut e. |
| Alert Set t ing | The policy based on which Apsara Stack Security reports alerts. If one of the following conditions is met, the host is unavailable: Response Time: If the actual response time is greater than the specified value, an exception occurs. Response Status: If an unexpected status code is returned, an exception occurs. |

d. Click Save.
6. Manage more than one availability monitoring task at a time.
You can manage more than one availability monitoring task in the monitoring task list at a time. Start more than one availability monitoring task at a time Select more than one availability monitoring task and choose Bat ch Monit oring Manage > Bat ch Open Monit oring. Stop more than one availability monitoring task at a time Select more than one availability monitoring task and choose Bat ch Monit oring Manage > Bat ch St op Monit oring. Delete more than one availability monitoring task at a time Select more than one availability monitoring task and choose Bat ch Monit oring Manage > Bat ch Delet e Monit oring.

##### 4.8.3.5 Manage custom update detection tasks

This topic describes how to manage custom update detection tasks. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Asset .
4. On the Asset page, click Cust om Updat e Det ect ion to view custom update detection tasks.
5. Create a custom update detection task.
i. Click Add Det ect ion. ii. On the Add Cust om Updat e Det ect ion page, configure the parameters. e

| Parameter | Description |
|---|---|
| Det ect ion Name | The name of the custom update detection task. |
| Det ect ion T arget | The asset that you want to detect. The value is fixed as Public net work asset . a. Click Host Asset or Websit e Asset based on your business requirements. b. Select the assets that you want to detect from the asset list. Not e You can search for assets by Asset Group or IP. |

e

| Parameter | Description |
|---|---|
| Port Range | The range of ports that you want to detect. Valid values: Cust omize, Full Port , T op100, and T op1000. Not e The Port Range parameter appears only after you set the Det ect ion T arget parameter to Host Asset. Cust omize: You can specify custom ports to detect. Full Port : All ports are detected. T op 100: Top 100 ports are detected. T op 1000: Top 1000 ports are detected. |

iii. Click Save.

#### 4.8.4 Risk management

##### 4.8.4.1 Manage vulnerabilities

This topic describes how to view and handle the vulnerabilities that are detected by the vulnerability scan feature. Context On the Securit y Vulnerabilit y tab, security administrators can view the vulnerabilities that are detected by the vulnerability scan feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Risk.
4. On the Risk page, click the Securit y Vulnerabilit y tab to view vulnerabilities.
e Click the Disclosured or Resolved tab to view unfixed vulnerabilities or fixed vulnerabilities. View risk statistics. The statistics include Unf ixed Risks, Recovered Risks, Unconf irmed Risks, Conf irmed Risks, and Ignored Risks.
5. Specify search conditions to view specific vulnerabilities. The conditions include Asset T ype and
Risk Level.
6. Handle vulnerabilities.
Security administrators can analyze and confirm whether the vulnerabilities affect the security of assets based on the vulnerability information. Confirm risks If a vulnerability affects the security of assets, confirm the risk after the security vulnerability is fixed. a. Find the vulnerability and click the icon in the Operat ion column. b. In the drop-down list, select Conf irm Risk. c. In the dialog box that appears, click OK. Ignore risks If a vulnerability is a false positive or does not affect the security of assets, ignore the risk. a. Find the vulnerability and click the icon in the Operat ion column. b. In the drop-down list, select Ignore Risk. c. In the dialog box that appears, click OK.
7. Click Export to export the list of vulnerabilities to your computer.

##### 4.8.4.2 Manage host compliance risks

This topic describes how to view and confirm host compliance risks. Context On the Host Compliance tab, security administrators can view the host compliance issues that are detected by the vulnerability scan feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Risk.
4. On the Risk page, click the Host Compliance tab to view host compliance risks.
You can click the Disclosured or Resolved tab to view unf ixed vulnerabilit ies or f ixed vulnerabilit ies. e
5. Specify conditions to search for host compliance risks based on the conditions. The conditions
include Asset T ype and Risk Level.
6. Handle host compliance risks.
Security administrators can analyze and confirm whether host compliance risks affect the security of assets based on the risk information. Confirm risks If a host compliance risk affects the security of assets, harden the security of hosts and confirm the risk. a. Find the required risk and click the icon in the Act ions column. b. In the drop-down list, select Conf irm Risk. c. In the message that appears, click OK. Ignore risks If a host compliance risk proves to be a false positive or does not affect the security of assets, ignore the risk. a. Find the required risk and click the icon in the Act ions column. b. In the drop-down list, select Ignore Risk. c. In the message that appears, click OK.
7. Click Export to export the list of host compliance risks to your computer.

##### 4.8.4.3 Manage external risks

This topic describes how to view and identify external risks, such as code leaks. Prerequisites A GitHub account is available, and the tokens of the account are obtained. Context On the Ext ernal Risk page, security administrators can use the vulnerability scan feature to check whether the GitHub library has risks of code leaks. e
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan > Risk >
Ext ernal Risk.
3. Click the Code Disclosure tab.
4. Add the assets that you want to monitor.
i. In the Asset Monit oring List section, click T oken set t ing. ii. In the Ent er Git Hub T oken dialog box, enter the tokens. You can enter multiple tokens. Press Enter each time you enter a token. iii. Click Add Asset and select the external assets that you want to monitor.
5. View the assets that have risks of code leaks.
You can view the unfixed and fixed risks on the Resolved and Disclosured tabs.
6. Handle the risks of code leaks.
Security administrators can analyze and check whether the security of the assets is affected based on the risk information. Confirm risks If the risks of code leaks affect the security of your assets, harden the hosts and confirm the risks. Ignore risks If the risks of code leaks prove to be false positives or do not affect the security of your assets, ignore the risks.

##### 4.8.4.4 Create a custom risk detection task

This topic describes how to create a custom risk detection task. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Risk. On the Risk page, click the Cust om Risk Det ect ion tab.
4. On the Custom Risk Detection tab, click Add Det ect ion.
5. On the Add Cust om Risk Det ect ion page, configure the parameters.

| Parameter | Description |
|---|---|
| Det ect ion Name | The name of the custom risk detection task. |
| Det ect ion T arget | The asset on which you want to perform risk detection. The value is fixed as Public net work asset . |
| Emergency Det ect ion | The switch that is used to enable or disable the emergency detection feature. If you enable this feature, you can select emergency detection items from the detection item list. |

| Guide·Threat Detection Se | rvic Apsara Stack Securit |
|---|---|

e

| Parameter | Description |
|---|---|
| Basic Risk Det ect ion | The switch that is used to enable or disable the basic risk detection feature. For more information about how to configure this feature, see Configure basic monitoring. |
| WEB Risk Det ect ion | The switch that is used to enable or disable the web risk detection feature. For more information about how to configure this feature, seeConfigure web monitoring. |

6. Click Save.

#### 4.8.5 Report management

##### 4.8.5.1 Create a report

This topic describes how to create a report. Context A security administrator can create a report to view the security statuses of specific assets during a period of time and implement security measures as required. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan > Report .
3. On the Report page, click the Risk Report tab and then the Add Report tab.
4. Configure the following parameters.
e

| Parameter |   | Description |
|---|---|---|
| Report Cont ent | Report Name | The name of the report that you want to create. |
| Report Range | Asset Inf o | The scope of assets that you want to include in the report. Valid values: Single asset , Asset Group, and All asset s. Single asset : Select an asset. Asset Group: Select an asset group and a tag. Not e After you select an asset group and a tag, the assets in the group that have the selected tag are included in the report. All asset s: Select assets by tag. |
|   | Discovery T ime | The time range in which you want to perform risk detection. |
| Risk Set t ing | Risk Range | The scope of risks that you want to include in the report. Valid values: Resolved Risk and Disclosured Risk. |
|   | Risk T ype | The types of risks that you want to include in the report. Valid values: Securit y Vulnerabilit y and Host Compliance. |

5. Click Creat e.
e Result After the report is created, it appears in the report list on the Report page.

##### 4.8.5.2 Delete multiple reports at a time

This topic describes how to delete multiple reports at a time. Context You can delete multiple reports that are no longer required at a time to save storage space. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan > Report .
3. Click Risk Report .
4. In the report list, select the reports that you want to delete.
5. Click Bat ch Delet e.

#### 4.8.6 Configuration management

##### 4.8.6.1 Configure overall monitoring

This topic describes how to configure overall monitoring for the vulnerability scan feature. Overall monitoring includes Asset Monitoring Configuration, Base Risk Monitoring Configuration, External Risk Monitoring Configuration, and Scan Configuration. Context Overall monitoring allows you to configure detection features and the monitoring cycle for each detection feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan >
Conf igurat ion > Monit oring Conf igurat ion > Overall Monit oring.
3. In the Monit oring St at us section, view the status of overall monitoring.
4. Configure detection features.
Detection features include Asset Monit oring Conf igurat ion, Base Risk Monit oring Conf igurat ion, Ext ernal Risk Monit oring Conf igurat ion, and Scan Conf igurat ion. In this step, the Asset Monit oring Conf igurat ion detection feature is used as an example. e i. Turn on Asset Monitoring Configuration to enable the asset monitoring feature. After the switch is turned on, the switch is in the On state. When in the On state, the switch is blue. After the switch is turned off, the switch is in the Of f state. When in the Off state, the switch is gray. You must turn on Asset Monit oring Conf igurat ion and Base Risk Monit oring Conf igurat ion to enable the two features. External Risk Monitoring Configuration and Scan Configuration are automatically enabled. ii. Configure the following parameters. Asset Monitoring Configuration

| Parameter | Description |
|---|---|
| Monit oring It em | The item that you want to monitor. Valid value: Subdomain Discovery. If you want to import assets, you can set the Import Set parameter to Aut o Import subdomains. Then, subdomains are automatically imported. If you select Subdomain Discovery, Apsara Stack Security regularly discovers subdomains for assets whose Import Set parameter is set to Aut o Import subdomains. |
| Monit oring Cycle | The cycle based on which you want to perform detection. Valid values: cust omizat ion, per week, and per mont h. cust omizat ion: Specify the interval at which you want to perform detection. Unit: days. per week: Specify the days of each week on which you want to perform detection. per mont h: Specify the days of each month on which you want to perform detection. |
| Det ect ion T ime | The time when you want to perform detection. The time varies based on the value of the Monit oring Cycle parameter. If you set the Monit oring Cycle parameter to cust omizat ion, select a time range of the day in which you want to perform detection. If you set the Monit oring Cycle parameter to per week, select the days of each week and the time range in which you want to perform detection. If you set the Monit oring Cycle parameter to per mont h, select the days of each month and the time range in which you want to perform detection. Not e For example, if you set the Monit oring Cycle parameter to per week and select Monday to Sunday and 00:00:00 to 24:00:00 for the Det ect ion T ime parameter, Apsara Stack Security performs detection 24 hours a day, 7 days a week. |

e

| Parameter | Description |
|---|---|
| Port Range | The ports on which you want to perform detection. Valid values: cust omizat ion, Full port , T OP100, and T OP1000. cust omizat ion: Specify the ports to scan. Full port : Scan all ports. T OP100: Scan top 100 ports. You can click Add to add more ports. T OP1000: Scan top 1,000 ports. You can click Add to add more ports. |
| Host Alive Det ect ion Set t ings | The option that is used to check whether a host is running. By default, the ping feature is used to check whether a host is running. If the host has the ping feature disabled, the status of the host is detected based on top 20 ports and custom ports. To specify custom ports, click Set t ings. In the Host Alive Detection Settings dialog box, specify the ports in the Cust om Port field. |

Base Risk Monitoring Configuration

| Parameter | Description |
|---|---|
| Monit oring It em | The item that you want to monitor. Valid values: Weak Password, Common Vulnerabilit ies, Baseline Monit oring, and Host Compliance. Weak Password: Attackers can guess passwords or launch brute- force attacks to crack passwords. Then, the attackers can obtain relevant permissions. If you select this item, weak password vulnerabilities can be identified. Common Vulnerabilit ies: Web security vulnerabilities and CMS application vulnerabilities are included. If you select this item, common vulnerabilities can be identified. Then, you can install patches at the earliest opportunity. Baseline Monit oring: Risks in host configuration and account configuration are detected. Host Compliance: Host compliance risks are detected. |
| Monit oring Cycle | The cycle based on which you want to perform detection. Valid values: cust omizat ion, per week, and per mont h. cust omizat ion: Specify the interval at which you want to perform detection. Unit: days. per week: Specify the days of each week on which you want to perform detection. per mont h: Specify the days of each month on which you want to perform detection. |

e

| Parameter | Description |
|---|---|
| Det ect ion T ime | The time when you want to perform detection. The time varies based on the value of the Monit oring Cycle parameter. If you set the Monit oring Cycle parameter to cust omizat ion, select a time range of the day in which you want to perform detection. If you set the Monit oring Cycle parameter to per week, select the days of each week and the time range in which you want to perform detection. If you set the Monit oring Cycle parameter to per mont h, select the days of each month and the time range in which you want to perform detection. Not e For example, if you set the Monit oring Cycle parameter to per week and select Monday to Sunday and 00:00:00 to 24:00:00 for the Det ect ion T ime parameter, Apsara Stack Security performs detection 24 hours a day, 7 days a week. |

External Risk Monitoring Configuration

| Parameter | Description |
|---|---|
| Monit oring It em | The item that you want to monitor. Valid value: Code Disclosure. If you select Code Disclosure, Apsara Stack Security detects leaked source code of your assets. |
| Monit oring Cycle | The cycle based on which you want to perform detection. Valid values: cust omizat ion, per week, and per mont h. cust omizat ion: Specify the interval at which you want to perform detection. Unit: days. per week: Specify the days of each week on which you want to perform detection. per mont h: Specify the days of each month on which you want to perform detection. |

e

| Parameter | Description |
|---|---|
| Det ect ion T ime | The time when you want to perform detection. The time varies based on the value of the Monit oring Cycle parameter. If you set the Monit oring Cycle parameter to cust omizat ion, select a time range of the day in which you want to perform detection. If you set the Monit oring Cycle parameter to per week, select the days of each week and the time range in which you want to perform detection. If you set the Monit oring Cycle parameter to per mont h, select the days of each month and the time range in which you want to perform detection. Not e For example, if you set the Monit oring Cycle parameter to per week and select Monday to Sunday and 00:00:00 to 24:00:00 for the Det ect ion T ime parameter, Apsara Stack Security performs detection 24 hours a day, 7 days a week. |

Scan Configuration

| Parameter | Description |
|---|---|
| Risk Re-det ect ion | The time at which you want to perform detection again. If risks are detected in specific assets, Apsara Stack Security scans the assets again each day at the time you specify. |
| Asset Scanning Rat e | The scan rate. Valid values: Slow Mode, General Mode, Fast Mode, and T urbo Mode. |
| Risk Scanning Rat e | The scan rate. Valid values: Slow Mode, General Mode, Fast Mode, and T urbo Mode. |
| UserAgent Set t ing | The User-Agent property. |

iii. Click Save.

##### 4.8.6.2 Configure basic monitoring

This topic describes how to configure basic monitoring. Context Basic monitoring includes Weak Password Vulnerability Monitoring, Operation Security Vulnerability Monitoring, CMS Application Vulnerability Monitoring, and Baseline Monitoring. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Conf igurat ion.
e
4. On the Conf igurat ion page, click the Monit oring Conf igurat ion tab.
5. On the Basic Monit oring tab of the Monitoring Configuration tab, click Weak Password
Vulnerabilit y Monit oring to configure rules to monitor weak passwords. By default, all monitoring items on weak passwords use the default weak password library. To disable a monitoring item, perform the following step: Find the required metric and click the icon in the Operat ion column. To enable a monitoring item, perform the following step: Find the required monitoring item and click the icon in the Operat ion column. To specify custom weak passwords for a monitoring item, perform the following steps. In this example, MySQL Weak Password Vulnerabilit y is used. a. In the Def ault Weak Password column, turn off the switch. The switch status changes to . b. In the Operat ion column, click the icon. c. In the Cust omize MySQL Weak Password dialog box, specify custom weak passwords. d. Click Yes. To apply the same custom weak passwords to multiple monitoring items, perform the following steps: a. In the Def ault Weak Password column, turn off the switches for the monitoring items that you want to apply the same custom weak passwords. The switch status changes to . Not e If you want to apply a custom weak password to a monitoring item, you must turn off the switch in the Default Weak Password column of the monitoring item. b. Click T ailored Overall Weak Password. c. In the T ailored Overall Weak Password dialog box, specify custom weak passwords. d. Click Yes.
6. Click Operat ion Securit y Vulnerabilit y Monit oring and configure O&M security vulnerability
monitoring.

| No. | Description |
|---|---|
| 1 | The switch that is used to enable or disable the Operat ion Securit y Vulnerabilit y Monit oring feature. We recommend that you enable this feature to enhance system security. |
| 2 | The switch that is used to enable or disable a monitoring item. You can disable monitoring items based on your business requirements. |

7. Click CMS Applicat ion Vulnerabilit y Monit oring and configure monitoring on content
management system (CMS) application vulnerabilities. e

| No. | Description |
|---|---|
| 1 | The switch that is used to enable or disable the CMS Applicat ion Vulnerabilit y Monit oring feature. We recommend that you enable this feature to enhance system security. |
| 2 | The switch that is used to enable or disable a monitoring item. You can disable monitoring items based on your business requirements. |

8. Click Baseline Monit oring and configure baseline monitoring.
To add a baseline monitoring item, perform the following steps: i. Click Add. ii. In the Add Baseline dialog box, configure the baseline monitoring item. In this example, a baseline monitoring item is added to block Telnet-based access.

| Parameter | Description |
|---|---|
| Baseline Name | The name of the baseline monitoring item. Example: Block Telnet-based access. |
| Baseline Rule | The detection rule that is used by the baseline monitoring item. This rule checks whether hosts use disabled ports or run disabled services. Valid values: Port Disabled: ports that you want to disable. Example: 23. Service Disabled: services that you want to disable. Example: Telnet. |
| Baseline Range | The scope of assets to which the baseline monitoring item can be applied. Valid values: Privat e IP and Nat IP. You must specify this parameter and select specific assets. |

iii. Click OK.

##### 4.8.6.3 Configure web monitoring

This topic describes how to configure web monitoring. Context Web monitoring allows you to configure monitoring items for monitoring web vulnerabilities. You can also configure conditions to block website crawlers. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Conf igurat ion.
4. On the Configuration page, click the Monit oring Conf igurat ion tab and then the Web
e Monit oring tab to view existing rules. Def ault rules are created by the system. You can only view details of the default rules, but cannot modify or delete them.
5. Create a web monitoring rule.
i. Click Add Rule. ii. On the Add Web Monit oring Rule page, configure the following parameters.

| Parameter | Description |
|---|---|
| Rule Name | The name of the web monitoring rule. |
| Monit oring Cycle | The monitoring cycle. Valid values: Cust omizat ion, Per Week, and Per Mont h. Cust omizat ion: Specify the interval at which you want to perform detection. Per Week: Specify the days of each week on which you want to perform detection. Per Mont h: Specify the days of each month on which you want to perform detection. |
| Det ect ion T ime | The time when you want to perform detection. The time varies based on the value of the Monit oring Cycle parameter. If you set the Monit oring Cycle parameter to Cust omizat ion, select a time range of the day in which you want to perform detection. If you set the Monit oring Cycle parameter to Per Week, select the days of each week and the time range in which you want to perform detection. If you set the Monit oring Cycle parameter to Per Mont h, select the days of each month and the time range in which you want to perform detection. Not e For example, if you set the Monit oring Cycle parameter to Per Week and select Monday to Sunday and 00:00:00 to 24:00:00 for the Det ect ion T ime parameter, Apsara Stack Security performs detection 24 hours a day, 7 days a week. |
| Monit oring Opt ions | The type of web vulnerabilities that you want to monitor. Supported operations: Select All, Inverse, and Clear. |
| UserAgent | The User-Agent field of the HTTP request packet. The User-Agent field identifies the application type, operating system, software developer, and version number of the proxy software that initiates requests. |
| Cookies | The cookie parameters. |

|   | Apsara Stack Securit |
|---|---|

e

| Parameter | Description |
|---|---|
| Key Page | The web directories or pages that you want to monitor. |
| Excluded Page | The web directories or pages that you do not want to monitor. |
| Crawler Dept h | The capturing depth of crawlers. Valid values: 10, 15, and 30. |
| URL Numbers | The number of URLs that are used for crawling. Valid values: 500, 1000, and 2000. |
| scanning Frequency | The scan frequency of web monitoring. Valid values: Request 10 T imes Per Second and Request 15 T imes Per Second. |

iii. Click Yes.
6. Manage the web monitoring rule.

| Icon | Description |
|---|---|
|   | Modify the rule. |
|   | Delete the rule. |
| Bat ch Delet e | If you want to delete multiple rules, select the rules you want to delete and click Bat ch Delet e. |

##### 4.8.6.4 Configure a whitelist

This topic describes how to configure a whitelist. Context Apsara Stack Security does not scan the assets that are added to a whitelist. Before you add assets to a whitelist, make sure that the assets are secure. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan.
3. In the Vulnerabilit y Scan pane, click Conf igurat ion.
4. On the Configuration page, click the Monit oring Conf igurat ion tab and then the Whit elist tab
to view the assets that are added to a whitelist. Not e By default, the whitelist feature is enabled. If you do not want to use the whitelist feature, turn off the switch in the upper-right corner.
5. Add assets to a whitelist.
i. Click Add. e ii. In the Add Whit elist dialog box, configure the parameters. If you select Asset Group for the Whit elist parameter, select a group from the second drop-down list. The assets in this group are added to the whitelist. If you select Cust omizat ion for the Whit elist parameter, enter the IP addresses or URLs that you want to add to the whitelist in the field that appears. iii. Click Yes.
6. Manage the assets that are added to a whitelist.
Delete an asset from a whitelist Find the required asset and click the icon in the Operat ion column. Remove multiple assets from a whitelist at a time Select the required assets and click Bat ch Delet e.

##### 4.8.6.5 Configure a scan engine for internal assets

This topic describes how to configure a scan engine for internal assets, such as the assets of a virtual private cloud (VPC). Context You must add a scan engine for a VPC before you can scan for vulnerabilities on the assets of the VPC. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Vulnerabilit y Scan >
Conf igurat ion. On the page that appears, click the Scan Engine Manage tab. Then, click the Privat e-sect or asset s tab.
3. Click the name of the VPC whose assets you want to scan.
4. Click Add Scan Engine.
5. In the Add Scan Engine dialog box, select a vSwitch for the VPC from the vSwit ch drop-down
list.
6. Click OK.

### 4.9 Create a security report

Security reports help monitor the security status of your assets. You can specify the content, types of statistics, and email addresses of recipients to create a security report. This topic describes how to create a security report. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose T hreat Det ect ion > Securit y Report s.
3. On the Report s page, click Creat e Report .
e Not ice In addition to the default security report created by Apsara Stack Security, you can create a maximum of nine security reports.
4. In the Specif y Basic Inf ormat ion step, configure the parameters.
Configure the following parameters: Report Name: Enter a name for the security report. Report T ype: Select a report type from the drop-down list. Valid values: Daily, Weekly, Monthly, and Custom. If you select Custom, you must also set the Dat a Collect ion Period parameter to specify the cycle on which data is collected. Language: Select a natural language for the report. Valid values: 简体中文 and English.
5. Click Next .
6. In the Specif y Report ed Dat a step, select the types of data that you want to view in the
security report. You can select assets, alerts, vulnerabilities, baselines, attacks, and other data related to security operations.
7. Click Save. The security report is created.
You can view the newly created security report on the Report s page.

## 5 Server security

### 5.1 Server security overview

This topic describes how to view the details about the security of servers on the server security overview page of Apsara Stack Security Center. This helps security administrators understand the security status of the servers. The servers refer to servers on the cloud. To view the details about the security of servers, log on to Apsara Stack Security Center and choose Server Securit y > Overview. On the page that appears, you can view detailed information on the following sections: overall statistics, Server Risks, Asset Protection, Operating System Distribution, and Recent Important Security Risks and Intrusions. Overall st at ist ics: This section displays the numbers of security vulnerabilities and security events on servers. For security vulnerabilities, you can view Unhandled Vulnerabilit ies and Baseline Risks. For security events, you can view Unhandled Alert s, Viruses Removed in Last 15 Days, and File T ampering At t empt s Prevent ed in Last 15 Days. Server Risks: This section displays the number of unhandled vulnerabilities, the number of baseline risks, and the distribution of risk levels. Asset Prot ect ion: This section displays the number of protected servers and the number of offline servers. Recent Import ant Securit y Risks and Int rusions: This section displays the recent important risks and events on your servers. You can click a risk or an event to view the details. Operat ing Syst em Dist ribut ion: This section displays your servers by operating system.

### 5.2 Server fingerprints

#### 5.2.1 Manage listening ports

This topic describes how to view the information about the listening port of a server. The information helps you identify suspicious listening behavior. Context This topic is suitable for the following scenarios: Check for servers that listen on a specific port. Check for ports that a specific server listens. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s.
3. On the Asset Fingerprint s page, click the Port tab to view list ening port s, net work prot ocols,
and server information. You can search for a port by using the port number, server process name, server name, or server IP address. In the server information list, you can view the process, IP address, and lat est scan t ime of a server.

#### 5.2.2 Manage software versions

This topic describes how to regularly view and collect the software version information about a server. This helps you check your software assets. Context This topic covers the following scenarios: Check for software assets that are installed without authorization. Check for outdated versions of software assets. Locate affected assets if vulnerabilities are detected. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s. On
the page that appears, click the Sof t ware tab.
3. View all the sof t ware asset s that are in use and the numbers of servers that use the software
assets. You can search for specific software by using its name, version, installation directory, server name, or IP address.
4. Click software to view the details, such as the software versions and the servers that use the
software. You can click the icon in the upper-right corner to download a software version table to your computer for subsequent asset check.

#### 5.2.3 Manage processes

This topic describes how to regularly collect the process information on a server and record changes. This way, you can view process information and historical process changes. Context This task is suitable for the following scenarios: Check for servers on which a specific process runs. Check for processes that run on a specific server. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s. On
the page that appears, click the Process tab.
3. View all running processes and the numbers of servers on which these processes run.
You can search for a process by using the process name, running user, st art up paramet er, or server name or IP address.
4. Click the name of a process to view the details of the process, such as the servers, paths, and
startup parameters.

#### 5.2.4 Manage account information

This topic describes how to regularly collect the account information on a server and record changes to the accounts. This way, you can check your accounts and view historical changes to your accounts. Context You can use the information collected in this topic for the following scenarios: Check for servers on which a specific account is created. Check for accounts that are created on a server. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s. On
the page that appears, click the Account tab.
3. View all the logged-on accounts and the numbers of servers on which the accounts are created.
You can search for an account by using the account name, root permissions, server name, or IP address.
4. Click an account name to view the details, such as the server information, root permissions, and user
group.

#### 5.2.5 Manage scheduled tasks

This topic describes how to view scheduled tasks on servers. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s. On
the page that appears, click the Scheduled T asks tab.
3. View the paths of all tasks and the numbers of servers that run these tasks.
You can search for a task by using the path, server name, or IP address.
4. Click a task path to view the details, such as the servers, executed commands, and task cycles.

#### 5.2.6 Set the fingerprint collection frequency

You can set the frequency at which the data of running processes, system accounts, listening ports, and software versions is collected. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Servers > Server Fingerprint s. In the
upper-right corner of the page that appears, click Set t ings.
3. Select the collection frequency from each drop-down list.
4. Click OK.

### 5.3 Threat protection

#### 5.3.1 Vulnerability management

##### 5.3.1.1 Manage Linux vulnerabilities

This topic describes how to manage Linux vulnerabilities. Context Apsara Stack Security automatically scans the software that is installed on your servers to detect the vulnerabilities provided in the Common Vulnerabilities and Exposures (CVE) list. Apsara Stack Security also sends you alerts about the detected vulnerabilities. In addition, Apsara Stack Security provides commands that you can use to fix vulnerabilities and allows you to verify vulnerability fixes. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Vulnerabilit ies.
On the page that appears, click the Linux Sof t ware tab.
3. View the detected Linux vulnerabilities.
Not e You can search for specific vulnerabilities by using the search and filter features.
4. Click a vulnerability. In the panel that appears, you can view details about the vulnerability and the
servers that are affected by the vulnerability. Not e You can find affected servers by using the search and filter features. Det ail: This tab displays the basic information about the vulnerability, including the name, Common Vulnerability Scoring System (CVSS) score, and description. Pending vulnerabilit y: This tab displays the servers that are affected by the vulnerability.
5. Handle the vulnerability based on its impact.
Actions on vulnerabilities

| Action | Impact |
|---|---|
| Fix | Select this action to fix the vulnerability. |
| Ignore | Select this action to ignore the vulnerability. The system no longer reports alerts for ignored vulnerabilities. |
| Verify | Click Verif y to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or multiple affected servers at a time. To manage a vulnerability for one affected server, find the server and select an action from the Act ions column of the server. To manage a vulnerability for multiple affected servers, select the servers and select an action in the lower-left corner.

##### 5.3.1.2 Manage Windows vulnerabilities

This topic describes how to manage Window vulnerabilities. Context Apsara Stack Security automatically checks whether the latest Microsoft updates are installed on your servers, and notifies you of the detected vulnerabilities. Apsara Stack Security also automatically detects and fixes major vulnerabilities on your servers. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Vulnerabilit ies.
On the page that appears, click the Windows Syst em tab.
3. View the detected Windows vulnerabilities.
Not e You can search for specific vulnerabilities by using the search and filter features.
4. Click a vulnerability. In the panel that appears, you can view details about the vulnerability and the
servers that are affected by the vulnerability. Not e You can find affected servers by using the search and filter features. Det ail: This tab displays the basic information about the vulnerability. Pending vulnerabilit y: This tab displays the servers that are affected by the vulnerability.
5. Handle the vulnerability based on its impact. describes the actions.
Actions on vulnerabilities

| Action | Impact |
|---|---|
| Fix | Select this action to fix the vulnerability. The system caches an official Windows patch in the cloud. Your server can automatically download the patch for updates. |
| Ignore | Select this action to ignore the vulnerability. The system no longer reports alerts for ignored vulnerabilities. |
| Verify | Click Verif y to verify the vulnerability fix. |

You can manage a vulnerability for one or multiple affected servers at a time. To manage a vulnerability for one affected server, select an action from the Act ions column of the server. To manage a vulnerability for multiple affected servers, select the servers and select an action in the lower-left corner.

##### 5.3.1.3 Manage Web CMS vulnerabilities

This topic describes how to manage Web CMS vulnerabilities. Context The Web CMS vulnerability detection feature obtains information about the latest vulnerabilities and provides patches in the cloud. This helps you detect and fix vulnerabilities. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Vulnerabilit ies.
On the page that appears, click the Web CMS tab.
3. View vulnerabilities.
Not e You can search for specific vulnerabilities by using the search and filter features.
4. Click a vulnerability. In the panel that appears, you can view details about the vulnerability and
servers that are affected by the vulnerability. Not e You can find affected servers by using the search and filter features.
5. Handle the vulnerability based on its impact. describes the actions.
Actions on vulnerabilities

| Action | Description |
|---|---|
| Fix | If you select this action, the system replaces the web files affected by the vulnerability on your server to fix the Web CMS vulnerability. Not e Before you fix the vulnerability, we recommend that you back up the web files affected by the vulnerability. For more information about the paths of the web files, click Details in the Actions column. |
| Verify | After a vulnerability is fixed, you can click Verif y to verify the fix. If you do not manually verify the fix of a vulnerability, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected servers at a time. To manage a vulnerability for one affected server, find the server and select an action in the Act ions column of the asset. To manage a vulnerability for multiple affected servers, select the servers and select an action in the lower-left corner.

##### 5.3.1.4 Manage urgent vulnerabilities

This topic describes how to manage urgent vulnerabilities. Context Apsara Stack Security automatically detects vulnerabilities on servers, such as the unauthorized Redis access vulnerability and Struts S2-052 vulnerability, and generates vulnerability alerts. After you fix a vulnerability, you can also check whether the fix is successful. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Vulnerabilit ies.
On the page that appears, click the Emergency tab.
3. View all vulnerabilities.
You can search for a specific vulnerability by using the search and filter features.
4. Click a vulnerability. In the panel that appears, view the details in the following sections: Det ails,
Suggest ions, and Af f ect ed Asset s. You can find affected servers by using the search and filter features.
5. Handle the vulnerability based on the impact of the vulnerability. describes the actions that you
can use to handle the vulnerability. Follow the instructions to manually fix the vulnerabilities on the Emergency tab. Actions on vulnerabilities

| Action | Description |
|---|---|
| Ignore | Select this action to ignore the vulnerability. The system no longer reports alerts for ignored vulnerabilities. |
| Verify | Click Verif y to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected servers at a time. To manage a vulnerability for one affected server, find the server and select an action from the Act ions column of the server. To manage a vulnerability for multiple affected servers, select the servers and select an action in the lower-left corner.

##### 5.3.1.5 Configure vulnerability management policies

You can enable or disable automatic detection for different types of vulnerabilities and enable vulnerability detection for specific servers. You can also set a time duration for which invalid vulnerabilities are retained and configure a vulnerability whitelist. Context A vulnerability whitelist allows you to exclude vulnerabilities from the detection list. You can add multiple vulnerabilities in the vulnerability list to the whitelist. The system does not detect vulnerabilities that are added to the whitelist. You can manage the vulnerability whitelist on the vulnerability settings page. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Vulnerabilit ies.
3. In the upper-right corner, click Set t ings to configure vulnerability management policies.
Select a vulnerability type and enable or disable detection for vulnerabilities of this type. Click Manage next to a vulnerability type and specify the servers on which vulnerabilities of this type are detected. Select a time duration during which invalid vulnerabilities are retained. For example, you can select 7 days, 30 days, or 90 days. Not e If you do not take an action on a detected vulnerability, the system determines that the alert is invalid. The system deletes the vulnerability after the specified duration. Select the vulnerability severities for scanning. High: Vulnerabilities of this severity must be fixed as soon as possible. Medium: Vulnerabilities of this severity can be fixed later. Low: Vulnerabilities of this severity are less urgent and can be fixed later. Select vulnerabilities in the whitelist and click Remove to enable the system to detect these vulnerabilities and generate alerts for these vulnerabilities.

#### 5.3.2 Baseline check

##### 5.3.2.1 Baseline check overview

The baseline check feature automatically checks the security configurations on servers and provides detailed check results and suggestions for baseline reinforcement. After you enable the baseline check feature, Apsara Stack Security automatically checks for risks related to the operating systems, accounts, databases, passwords, and security compliance configurations of your servers, and provides reinforcement suggestions. For more information, see Baselines. By default, a full baseline check is automatically performed from 00:00 to 06:00 every day. You can create and manage scan policies for baseline checks. When you create or modify a policy, you can specify the baselines, interval, and time period, and select the servers to which you want to apply this policy. For more information, see Add a custom baseline check policy. Precautions By default, the following baselines are disabled. To check these baselines, make sure that these baselines do not affect your business and select them when you customize a scan policy. Baselines related to weak passwords for specific applications such as MySQL, PostgreSQL, and SQL Server Not e If these baselines are enabled, the system attempts to log on to servers with weak passwords. The logon attempts consume server resources and generate a large number of logon failure records. Baselines related to China classified protection of cybersecurity Baselines related to the Center for Internet Security (CIS) standard Baselines

| Category | Baseline |
|---|---|
| High risk exploit | High risk exploit - CouchDB unauthorized access high exploit risk High risk exploit - Docker unauthorized access high vulnerability risk High risk exploit - Elasticsearch unauthorized access high exploit vulnerability risk High risk exploit - Memcached unauthorized access high exploit vulnerability risk High risk exploit - Apache Tomcat AJP File Read/Inclusion Vulnerability High risk exploit - ZooKeeper unauthorized access high exploit vulnerability risk |

| Category | Baseline |
|---|---|
|   | Security baseline check against the Alibaba Cloud standard: Alibaba Cloud Standard-Aliyun Linux 2 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 6 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 7 Security Baseline Check Alibaba Cloud Standard - Debian Linux 8 Security Baseline Alibaba Cloud Standard - Redhat Linux 6 Security Baseline Check Alibaba Cloud Standard - Redhat Linux 7 Security Baseline Check Alibaba Cloud Standard - Ubuntu Security Baseline Check Alibaba Cloud Standard - Windows Server 2008 R2 Security Baseline Check Alibaba Cloud Standard - Windows 2012 R2 Security Baseline Alibaba Cloud Standard - Windows 2016/2019 R2 Security Baseline |
|   | Security baseline check against the CIS standard: Alibaba Cloud Aliyun Linux 2 CIS Benchmark CIS CentOS Linux 6 LTS Benchmark CIS CentOS Linux 7 LTS Benchmark CIS Debian Linux 8 Benchmark CIS Ubuntu Linux 14 LTS Benchmark CIS Ubuntu Linux 16/18 LTS Benchmark CIS Microsoft Windows Server 2008 R2 Benchmark CIS Microsoft Windows Server 2012 R2 Benchmark CIS Microsoft Windows Server 2016/2019 R2 Benchmark |

| Category CIS and China's Protection of | Baseline |
|---|---|
| Cybersecurity | Baseline check on compliance of China classified protection of cybersecurity level III: Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level III CentOS Linux 6 Baseline for China classified protection of cybersecurity-Level III CentOS Linux 7 Baseline for China classified protection of cybersecurity-Level III Debian Linux 8 Baseline for China classified protection of cybersecurity-Level III Redhat Linux 6 Baseline for China classified protection of cybersecurity-Level III Redhat Linux 7 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 10 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 11 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 12 Baseline for China classified protection of cybersecurity-Level III Ubuntu 14 Baseline for China classified protection of cybersecurity- Level III Waiting for Level 3-Ubuntu 16/18 compliance regulations inspection China's Level 3 Protection of Cybersecurity - Windows Server 2008 R2 Compliance Baseline Check Windows 2012 R2 Baseline for China classified protection of cybersecurity-Level III Windows 2016/2019 R2 Baseline for China classified protection of cybersecurity-Level III |

| Category | Baseline |
|---|---|
| Best security practices | Alibaba Cloud Standard-Aliyun Linux 2 Security Baseline Check Alibaba Cloud Standard - Apache Security Baseline Check Alibaba Cloud Standard - CentOS Linux 6 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check Alibaba Cloud Standard - Debian Linux 8 Security Baseline Alibaba Cloud Standard - IIS 8 Security Baseline Check Alibaba Cloud Standard - Memcached Security Baseline Check Alibaba Cloud Standard - MongoDB 3.x Security Baseline Check Alibaba Cloud Standard - Mysql Security Baseline Check Alibaba Cloud Standard - Nginx Security Baseline Check Alibaba Cloud Standard - Redhat Linux 6 Security Baseline Check Alibaba Cloud Standard - Redhat Linux 7 Security Baseline Check Alibaba Cloud Standard - Redis Security Baseline Check Alibaba Cloud Standard - Ubuntu Security Baseline Check Alibaba Cloud Standard - Windows Server 2008 R2 Security Baseline Check Alibaba Cloud Standard - Windows 2012 R2 Security Baseline Alibaba Cloud Standard - Windows 2016/2019 R2 Security Baseline Alibaba Cloud Standard-Apache Tomcat Security Baseline |
| Weak password | Weak Password-MongoDB Weak Password baseline(support version 2. X) Weak password - Ftp login weak password baseline Weak password - Linux system login weak password baseline Weak password - MongoDB login weak password baseline Weak password - SQL Server DB login weak password baseline Weak password - Mysql DB login weak password baseline Weak password - Mysql DB login weak password baseline(Windows version) Weak password - PostgreSQL DB login weak password baseline Weak password - Redis DB login weak password baseline Weak password - rsync login weak password baseline Weak password - svn login weak password baseline |

##### 5.3.2.2 Configure baseline check policies

This topic describes how to create, modify, and delete baseline check policies and how to specify baseline check levels. Context By default, the baseline check feature uses the def ault policy to check the baseline risks of assets. You can also customize baseline check policies based on your business requirements. For example, you can customize a baseline check policy to check the compliance with China classified protection of cybersecurity-Level II.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Baseline
Check.
3. In the upper-right corner of the page that appears, click Manage Policies. In the Manage Policies
panel, create, modify, or delete a baseline check policy. You can also modify the default policy. In the upper-right corner of the panel, click Creat e Policy to customize a baseline check policy. Then, click Ok.

| Parameter | Description |
|---|---|
| Policy Name | Enter a policy name. |
| Schedule | Set the time interval for scheduled scan tasks to 1 Day(s), 3 Day(s), 7 Day(s), or 30 Day(s). Then, select one of the following time ranges for scheduled scan tasks: 00:00 to 06:00, 06:00 to 12:00, 12:00 to 18:00, and 18:00 to 24:00. |
| Check It ems | Select the baseline items that need to be checked from the following categories: High risk exploit, Container security, CIS and China's Protection of Cybersecurity, Best security practices, and Weak password. |
| Servers | Select the server groups to which you want to apply the baseline check policy. Not e By default, newly purchased servers are classified into the Def ault group under Asset Groups. To apply this policy to new servers, select Def ault . |

Click Edit or Delet e next to the new policy to modify or delete it. Not e You cannot restore a policy after you delete it. Find the Def ault policy and click Edit in the Act ions column to modify the server groups to which the default policy is applied. Not e You cannot delete the default policy or modify the baseline items of the default policy. You can only modify the server groups to which the default policy is applied. In the lower part of the Manage Policies panel, specify the baseline check levels. Valid values: High, Medium, and Low.
4. Click Ok.

##### 5.3.2.3 View baseline check results and manage failed check items

check items Apsara Stack Security Center provides detailed baseline check results and suggestions on how to manage failed check items. This topic describes how to view baseline check results and manage failed check items in Apsara Stack Security Center. The check results include affected assets, checked items, and suggestions. View the summary of baseline check results
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Baseline
Check.
3. In the upper part of the Baseline Check page, view the summary of baseline check results. You can
filter data by policy. You can select a policy from the Select Policy drop-down list to view the following information: Checked Servers: The number of servers on which the baseline check runs. These servers are specified in the selected baseline check policy. Check It ems: The number of check it ems specified in the selected baseline check policy. Last Pass Rat e: The pass rate of the last baseline check. If the number below Last Pass Rat e is green, the pass rate of the checked servers is high. If the number is red, a large number of failed check items have been detected on the checked servers. We recommend that you view the check result details and manage the failed check items. View all baselines 1.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Baseline
Check.
3. Select All from the Select Policy drop-down list.
The Baseline Check page displays details about all baselines, including Baseline, Checked It em, Failed It ems/Af f ect ed Servers, Cat egory, and Last Check. Not e You can also select a baseline check policy from the Select Policy drop-down list to view the baselines specified in this policy. View details about a baseline 1.
2. In the left-side navigation pane, choose Server Securit y > T hreat Prevent ion > Baseline
Check.
3. In the Baseline column, click a baseline to view its details.
4. In the details panel, manage the failed check items.
Find the asset that you want to manage and click View in the Act ions column to open the At - Risk It ems panel. View details about a failed check item
1. Find the baseline that you want to manage and click it. In the panel that appears, find the asset
that you want to manage and click View in the Act ions column to view failed check items. You can view the check items of the asset and the statuses of the check items. The status can be Passed or Failed. 2. Not e We recommend that you follow the suggestions to manage check items whose status is Failed at the earliest opportunity, especially high-risk check items. Manage failed check items In the At-Risk Items panel, manage failed check items. Add check it ems t o t he whit elist If you want to disable alerts for a check item, click Whit elist to add the check item to the whitelist. Check items in the whitelist do not trigger alerts. Not e You can also select multiple check items and click Whit elist in the lower-left corner to add the check items to the whitelist at a time. Remove check it ems f rom t he whit elist If you want to enable alerts for a check item in the whitelist, you can click Remove to remove the check item from the whitelist. You can remove one or more check items from the whitelist at a time. After a check item is removed from the whitelist, the check item triggers alerts again. Verif y t he f ix of a f ailed check it em If you do not manually perform the verification, Apsara Stack Security automatically verifies the fix based on the detection interval specified in the policy.

### 5.4 Intrusion prevention

#### 5.4.1 Intrusion events

##### 5.4.1.1 Intrusion event types

If the Server Security feature detects sensitive file tampering, webshells, unusual logons, suspicious processes, and malicious processes, it generates alerts. Based on these alerts, you can monitor the security status of your assets and handle potential threats at the earliest opportunity. Apsara Stack Security provides statistics based on alerts. This helps you understand the overall protection situation. To view statistics on alerts, you must choose Server Securit y > Int rusion Prevent ion > Int rusions. Alert types The following table describes the alert items.

| Alert type | Description |
|---|---|
| T hreat int elligence | Identify potential threats in assets based on the threat intelligence of Apsara Stack Security. Threat intelligence can correlate threat information to help you analyze and process the information. If threats are detected, alerts are reported. This helps improve the detection efficiency and response speed. Intelligence types include the following items: Malicious domain names Malicious IP addresses IP addresses of dark web services IP addresses of command and control (C&C) servers IP addresses of mining pools Malicious URLs Malicious download sources |
| Unusual Logon | Detect unusual logons to your servers. You can specify approved logon IP addresses, time periods, and accounts. Logons from disapproved IP addresses, accounts, or time periods trigger alerts. You can manually add approved logon locations or configure the system to automatically update approved logon locations. You can also specify assets on which alerts are triggered when disapproved logon locations are detected. Apsara Stack Security can detect the following events: Logons to Elastic Compute Service (ECS) instances from disapproved IP addresses Logons to ECS instances from disapproved locations Execution of unusual commands after SSH-based logons to ECS instances Brute-force attacks on SSH passwords of ECS instances |

| Alert type | Description |
|---|---|
| Webshell | Use engines developed by Alibaba Cloud to scan common webshell files. Apsara Stack Security supports scheduled scan tasks, provides real-time protection, and quarantines webshell files. Apsara Stack Security scans the entire web directory early in the morning on a daily basis. A change made to files in the web directory triggers dynamic detection. You can specify the assets on which Apsara Stack Security scans for webshells. You can quarantine, restore, or ignore detected trojan files. |
| Precision def ense | The ant ivirus feature provides precise protection against common ransomware, DDoS trojans, mining programs, trojans, malicious processes, webshells, and computer worms. |
| Suspicious Account | Detect logons to your assets from disapproved accounts. |
| Cloud t hreat det ect ion | Detect threats in other cloud services. |
| Persist ence | Detect suspicious scheduled tasks on servers and generates alerts when advanced persistent threats (APTs) on the servers are detected. |
| Unusual Net work Connect ion | Detect disconnections or suspicious network connections. |
| Suspicious Process | Detect whether suspicious processes exist. |
| Malicious Process | Detect your servers in real time. An agent is used to collect process information, and the information is uploaded to the cloud for detection. You can manage detected viruses in Apsara Stack Security Center. Apsara Stack Security can detect the following malicious activities and processes: Accesses from malicious IP addresses Mining programs Self-mutating trojans Malicious programs Trojans |
| Sensit ive File T ampering | Check whether sensitive files on your server are maliciously modified. The sensitive files include preloaded configuration files in Linux shared libraries. |
| Ot her | Detect other types of attacks, such as DDoS attacks. |
| Web Applicat ion T hreat Det ect ion | Detect server intrusions that use web applications. |
| Applicat ion int rusion event | Detect server intrusions that use system application components. |

##### 5.4.1.2 View and handle detected intrusion events

This topic describes how to view and handle detected intrusion events on the Intrusions page. Background information After intrusion events are detected, the intrusion events are displayed on the Intrusions page. You can choose Server Securit y > Int rusion Prevent ion > Int rusions to go to the Intrusions page. If the intrusion events are not handled, they are displayed in the Unhandled Alert s list on the Int rusions page. After the intrusion events are handled, the status changes from Unhandled Alert s to Handled. Not e Apsara Stack Security retains the records of Unhandled Alert s and Handled on the Int rusions page. By default, the records of Unhandled Alert s are displayed. View intrusion events
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. On the page that appears, search for or view intrusion events. You can also view the details about
the events. Handle intrusion events
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. On the Int rusions page, find the intrusion event that you want to handle and click Process in the
Act ions column. In the dialog box that appears, set Process Method and click Process Now. Not e If the intrusion event contains multiple correlated exceptions, on the page that appears after you click Process, you can handle the exceptions. Ignore: If you ignore the intrusion event, the status of the intrusion event changes to Handled. Server Guard no longer generates alerts for the event. Add T o Whit elist : If the intrusion event is a false positive, you can add the intrusion event to the whitelist. Then, the status of the intrusion event changes to Handled. Server Guard no longer generates alerts for the event. In the Handled list, you can click Cancel whit elist to remove a specific intrusion event from the whitelist. Not e A false positive indicates that Server Guard has generated a false alert on a normal process. A common false positive is a suspicious process t hat sends T CP packet s. The false positive notifies you that suspicious scans on other devices are detected on your servers. Bat ch unhandled: This method allows you to handle multiple intrusion events at a time. Before you handle multiple intrusion events at a time, we recommend that you view the details of the intrusion events.
4. (Optional)If you confirm that one or more intrusion events are false positives or need to be ignored,
go to the Int rusions page. Then, select the intrusion events and click Ignore Once or Whit elist . Export intrusion events
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. In the upper-left corner above the intrusion event list on the Int rusions page, click the
icon to export the list. After the list is exported, the Done message appears in the upper-right corner.
4. In the Done notification of the Alert s page, click Download.
The alert list is downloaded to your computer.

##### 5.4.1.3 View exceptions related to an alert

Server Guard supports automatic analysis of exceptions related to an alert. You can click an alert in the alert list to view and manage all exceptions that are related to the alert. You can also view the results of automatic attack tracing to analyze and handle the exceptions. Context Security Center automatically associates alerts with exceptions in real time to detect potential threats. Exceptions related to an alert are listed in chronological order. This allows you to analyze and handle the exceptions to improve the emergency response mechanism of your system. An automatically correlated alert is identified by the icon. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. On the Intrusions page, click the name of t he alert that you want to manage. The alert details
panel appears.
4. In the alert details panel, view the details and related exceptions of the alert. Then, handle the
exceptions. View alert details You can view the assets that are affected by the alert, the first and latest time when the alert was triggered, and the details about the related exceptions. View affected assets You can move the pointer over the name of an af f ect ed asset to view the details about the asset. The details include information about all the alerts, vulnerabilities, baseline risks, and asset fingerprints on the asset. View and manage relat ed except ions In the Relat ed Except ions section, you can view the details about all the exceptions that are related to the alert. You can also view suggestions on how to handle the exceptions. Click Not e to the right of an exception to add a note for the exception. Click the icon to the right of a note to delete the note.

##### 5.4.1.4 Use the file quarantine feature

Sever Guard can quarantine malicious files. Quarantined files are listed in the quarantine box on the Intrusions page. The system automatically deletes a quarantined file 30 days after the file is quarantined. You can restore a quarantined file with a few clicks before the file is deleted. This topic describes how to view and restore quarantined files. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. In the upper-right corner of the Int rusions page, click Quarant ine.
In the Quarant ine panel, you can perform the following operations: View information about quarantined files. The information includes server IP addresses, paths that store the files, file status, and modification time. Click Rest ore in the Act ions column to remove a file from the quarantine box. The restored file appears in the alert list again.

##### 5.4.1.5 Configure security alerts

This topic describes how to configure security alerts, which allows you to specify approved logon locations and custom web directories to scan. Context Server Guard supports advanced logon settings. You can configure more fine-grained logon detection rules. For example, you can specify approved logon IP addresses, logon time, and logon accounts to block unauthorized requests sent to your assets. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Int rusions.
3. In the upper-right corner, click Set t ings.
Configure parameters on different tabs. Add an approved logon locat ion a. In the Login Locat ion section, click Management on the right. b. Select the logon location that you want to add and select the servers that allow logons from the added location. c. Click OK. Server Guard allows you to edit or delet e approved logon locations. Find a specific logon location and click Edit on the right to change the servers that allow logons from this location. Find a specific logon location and click Delet e on the right to delete the logon location. Conf igure advanced logon set t ings Not e When you configure advanced logon settings, you can specify the IP addresses, accounts, and time ranges that are allowed for logons to your assets. After the advanced logon settings are configured, Server Guard sends you alerts if your assets receive unauthorized logon requests. The procedure of configuring advanced logon settings is similar to that of configuring Login Locat ion. You can add, edit , or delet e advanced logon settings in a similar way. Turn on or turn off Uncommon IP Alert to the right of Common Login IPs. If you turn on Uncommon IP Alert and your assets receive logon requests from unauthorized IP addresses, alerts are triggered. Turn on or turn off Uncommon Time Alert to the right of Common Login T ime. If you turn on Uncommon Time Alert and your assets receive logon requests in unauthorized time ranges, alerts are triggered. Turn on or turn off Uncommon Account Alert to the right of Common Login Account s. If you turn on Uncommon Account Alert and your assets receive logon requests from unauthorized accounts, alerts are triggered. Add web direct ories t o scan Server Guard automatically scans web directories of data assets in your servers and runs dynamic and static scan tasks. You can also manually add other web directories. a. In the Add Scan T arget s section, click Management on the right. b. Specify a valid web directory and select the servers on which the specified web directory is scanned. Not e To ensure the scan performance and efficiency, we recommend that you do not specify a root directory. c. Click OK.

##### 5.4.1.6 Cloud threat detection

The cloud threat detection feature provided by Server Guard is integrated with widely-used antivirus engines. The feature detects viruses based on large amounts of threat intelligence data provided by Alibaba Cloud and the exception detection model designed by Alibaba Cloud. This model is designed based on machine learning and deep learning. This way, the cloud threat detection feature can provide full-scale and dynamic antivirus protection to safeguard your servers. The cloud threat detection feature scans hundreds of millions of files on a daily basis and protects millions of servers on the cloud. Detection capabilities The cloud threat detection feature uses the Server Guard agent to collect process information and scans the retrieved data for viruses in the cloud. If a malicious process is detected, you can stop the process and quarantine the source files. The cloud threat detection feature provides the following capabilities: Deep learning engine developed by Alibaba Cloud: The deep learning engine is built on deep learning technology and a large number of attack samples. The engine detects malicious files on the cloud and automatically identifies potential threats to supplement traditional antivirus engines. Cloud sandbox developed by Alibaba Cloud: The cloud sandbox feature allows you to simulate cloud environments and monitor attacks launched by malicious samples. The cloud sandbox feature automatically detects threats and offers dynamic analysis and detection capabilities based on big data analytics and machine learning modeling techniques. Int egrat ion wit h major ant ivirus engines: The cloud threat detection feature is integrated with major antivirus engines and updates its virus library in real time. T hreat int elligence det ect ion: The cloud threat detection feature works with the exception detection module to detect malicious processes and operations based on threat intelligence data provided by Alibaba Cloud Security. Detectable virus types The cloud threat detection feature is developed based on the security technologies and expertise of Alibaba Cloud. The feature provides end-to-end security services, including threat intelligence collection, data masking, threat identification, threat analysis, and malicious file quarantine and restoration. You can quarantine and restore files that contain viruses in the Security Center console. The cloud threat detection feature can detect the following types of viruses.

| Virus | Description |
|---|---|
| Mining program | A mining program consumes server resources and mines cryptocurrency without authorization. |
| Computer worm | A computer worm uses computer networks to replicate itself and spread to a large number of computers within a short period of time. |
| Ransomware | Ransomware, such as WannaCry, uses encryption algorithms to encrypt files and prevent users from accessing the files. |
| Trojan | A trojan is a program that allows an attacker to access information about servers and users, gain control of the servers, and consume system resources. |
| DDoS trojan | A DDoS trojan hijacks servers and uses zombie servers to launch DDoS attacks, which interrupts your service. |
| Backdoor | A backdoor is a malicious program injected by an attacker. Then, the attacker can use the backdoor to control the server or launch attacks. |
| Computer virus | A computer virus inserts malicious code into normal programs and replicates the code to infect the whole system. |
| Malicious program | A malicious program may pose threats to system and data security. |

Benefits Self -developed and cont rollable: The cloud threat detection feature is based on deep learning, machine learning, and big data analytics with a large number of attack and defense practices. The feature uses multiple detection engines to dynamically protect your assets against viruses. Light weight : The cloud threat detection feature consumes only 1% of CPU resources and 50 MB of memory. Dynamic: The cloud threat detection feature dynamically retrieves startup logs of processes to monitor the startup of viruses. Easy t o manage: You can manage all servers and view their status at any time in the Security Center console. Threat detection limits Apsara Stack Security Center allows you to detect and process security alerts, scan for and fix vulnerabilities, analyze attacks, and check security settings. Apsara Stack Security Center can analyze alerts and automatically trace attacks. This allows you to protect your assets. Apsara Stack Security supports a wide range of protection features. We recommend that you install the latest system patches on your assets. We also recommend that you use security services, such as Cloud Firewall and Web Application Firewall (WAF), to better protect your assets against attacks. Not e Attacks and viruses are evolving, and security breaches may occur in various business environments. We recommend that you use the alerting, vulnerability detection, baseline check, and configuration assessment features provided by Apsara Stack Security to better protect your assets against attacks.

#### 5.4.2 Website tamper-proofing

##### 5.4.2.1 Overview

Tamper protection monitors website directories in real time, restores modified files or directories, and protects websites from trojans, hidden links, and uploads of violent and illicit content. Background information To make illegal profits or conduct business attacks, attackers exploit vulnerabilities in websites to insert illegal hidden links and tamper with the websites. Defaced web pages affect normal user access and may lead to serious economic losses, damaged brand reputation, or political risks. Tamper protection allows you to add Linux and Windows processes to the whitelist and update protected files in real time. How tamper protection works The Security Center agent automatically collects the list of processes that attempt to modify files in the protected directories of the protected servers. It identifies unusual processes and file changes in real time and blocks unusual processes. The alert list is displayed on the Tamper Protection page. You can view unusual file changes, the corresponding processes, and the number of attempts made by each process in the alert list. If a file is modified by a trusted process, you can add the process to the whitelist. After the process is added to the whitelist, tamper protection no longer blocks the process. In scenarios where the content of websites, such as news and education websites, is frequently modified, the whitelist saves you the effort of frequently enabling and disabling tamper protection. Versions of operating systems and kernels supported by tamper protection

| OS | Supported operating system version | Supported kernel version |
|---|---|---|
| Windows | Windows Server 2008 and later | All versions |
| CentOS | 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, and 7.6 | 2.6.32-x 3.10.0-x |
| Ubuntu | 14, 16, and 18 | 3.13.0-32-generic 3.13.0-86-generic 4.4.0-62-generic 4.4.0-63-generic 4.4.0-93-generic 4.4.0-151-generic 4.4.0-117-generic 4.15.0-23-generic 4.15.0-42-generic 4.15.0-45-generic 4.15.0-52-generic |

Not e The preceding table lists kernel versions supported by tamper protection. Servers that use an unsupported kernel version cannot use tamper protection. Make sure that your server uses a supported kernel version. If a kernel version is not supported, you must upgrade it to a supported version. Otherwise, you cannot add processes to the whitelist. Before you upgrade the server kernel, back up your asset data.

##### 5.4.2.2 Configure tamper protection

The Server Security feature allows you to configure tamper protection for web pages. Limits For each server, you can add a maximum of 10 directories for protection. If you want to add directories that are on a Windows server, the directories must meet the following requirements: The size of each directory does not exceed 20 GB. Each directory contains no more than 2,000 folders. The number of directory levels does not exceed 20. The size of each file does not exceed 3 MB. If you want to add directories that are on a Linux server, the directories must meet the following requirements: The size of each directory does not exceed 20 GB. Each directory contains no more than 3,000 folders. The number of directory levels does not exceed 20. The size of each file does not exceed 3 MB. Before you add a directory for protection, make sure that the directory meets the preceding requirements. We recommend that you exclude file formats that do not require protection, such as LOG, PNG, JPG, M P4, AVI, and MP3. Multiple file formats can be separated by semicolons (;).
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > File T amper
Prot ect ion.
3. On the T amper Prot ect ion page, click Add Servers f or Prot ect ion.
4. In the Add Servers f or Prot ect ion panel, select a server that you want to protect.
5. Click Next to go to the Add Direct ory step.
6. In the Add Direct ory step, configure the parameters.
Select a protection mode. The settings of other parameters vary based on the protection mode. You can select Whit elist Mode or Blacklist Mode. In whitelist mode, tamper protection is enabled for the specified directories and file formats. In blacklist mode, tamper protection is enabled for the subdirectories, file formats, and files that are not specified. By default, Whitelist Mode is selected. The following table describes the parameters that you must configure if you select Whitelist Mode.

| Parameter | Description |
|---|---|
| Protected Directory | Enter the path of the directory that you want to protect. Not e Servers that run Linux or Windows operating systems use different path formats. Enter a valid directory path based on the type of your operating system. |
| Protected File Formats | Select file formats that you want to protect from the drop-down list, such as js, html, xml, and jpg. |
| Local Backup Directory | The default path in which backup files of the protected directories are stored. By default, Apsara Stack Security assigns /usr/local/aegis/bak to Linux servers and C:\Program Files (x86)\Alibaba\Aegis\bak to Windows servers. You can change the default path based on your business requirements. |

The following table describes the parameters that you must configure if you select Blacklist Mode.

| Parameter | Description |
|---|---|
| Protected Directory | Enter the path of the directory that you want to protect. |
| Excluded Sub- Directories | Enter the subdirectories that you do not want to protect. Click Add Sub-Direct ory to add more subdirectories. Apsara Stack Security does not provide tamper protection for files in the excluded subdirectories. |
| Excluded File Formats | Select file formats that you do not want to protect from the drop-down list. Valid values: log, t xt , and ldb. Apsara Stack Security does not provide tamper protection for the files in the excluded formats. |
| Excluded Files | Enter the path of the files for which you do not want to protect. Click Add File to add more files. Apsara Stack Security does not provide tamper protection for the excluded files. |

| ide·Server security | Apsara Stack Securit |
|---|---|
| Parameter | Description |
| Local Backup Directory | The default path in which backup files of the protected directories are stored. By default, Apsara Stack Security assigns /usr/local/aegis/bak to Linux servers and C:\Program Files (x86)\Alibaba\Aegis\bak to Windows servers. You can change the default path based on your business requirements. |

7. Click Enable Prot ect ion.
After you enable this feature for a server, the server is displayed on the Management tab of the T amper Prot ect ion page. Not e By default, tamper protection is in the Of f state for the server. To enable tamper protection for the server, you must t urn on the switch in the Protection column on the T amper Prot ect ion page.
8. On the T amper Prot ect ion page, find the server that you add. Then, click the Management tab
and turn on the switch in the Prot ect ion column to enable protection for the server. Not e By default, tamper protection is in the Of f state for the server. To enable tamper protection for the server, you must turn on the switch in the Protection column on the T amper Prot ect ion page. After tamper protection is enabled, the status of the server changes to Running. Not e If the status of the server is Except ion, move the pointer over Except ion in the Status column to view the cause and click Ret ry to enable tamper protection again. What to do next After you enable tamper protection for a server, you can go to the Alert s page and select Webpage Tampering from the alert type drop-down list to view the alerts generated upon tampering events. Not e Tamper protection does not take effect immediately after you configure the protected directory, and you can still write files to the directory. In this case, you must go to the Management page, disable Prot ect ion for the server where the directory is located, and then enable Prot ect ion again. Handling suggestions for abnormal protection states

| State | Description | Suggestion |
|---|---|---|
| Initializing | Tamper protection is being initialized. | If this is your first time enabling tamper protection for a server, the protection status becomes Init ializing. Tamper protection will be enabled in a few seconds. |

| psara Stack Security |   | User Guide·Server securit |
|---|---|---|
| State | Description | Suggestion |
| Running | Tamper protection is enabled and running as expected. | None. |
| Exception | An error occurred when tamper protection was enabled. | Move the pointer over Except ion in the Status column to view the exception cause and click Retry. |
| Not Initialized | Web tamper protection is disabled. | T urn on the switch in the Protection column to enable tamper protection. |

##### 5.4.2.3 View protection status

This topic describes how to view the status of tamper protection for your assets. Context The tamper protection feature monitors changes to the files in website directories in real time and blocks suspicious file changes. To view the status of and details about the tamper protection feature, you must log on to Apsara Stack Security Center and choose Server Securit y > Int rusion Prevent ion
> File T amper Prot ect ion. The following information is displayed:

Tamper protection overview You can view the numbers of files that are changed on the current day and in the last 15 days, the number of protected servers, and the number of protected directories. Distribution of protected file types Protected file types include TXT, PNG, MSI, and ZIP. You can also add more types of files for tamper protection based on your business requirements. Not e All types of files for tamper protection can be added. Top five files This section shows the names and paths of the top five files that are ranked based on the number of changes to files in descending order in the last 15 days. Tamper protection alerts This section lists the alerts generated for blocked suspicious changes to files for your assets. You can view details about the alerts, including the severity, alert name, affected assets, paths of files with suspicious changes, and protection status. If an alert is reported more than 100 times, we recommend that you handle the alert at your earliest opportunity. Only alerts at the Medium level are displayed in the console. Only alerts in the Def ended state are displayed. These alerts are triggered when the tamper protection feature blocks suspicious processes that attempt to modify files without authorization.

#### 5.4.3 Configure the anti-virus feature

Server Guard provides the anti-virus feature. This feature allows you to customize settings for virus and webshell detection. Detect and remove viruses The anti-virus feature can automatically quarantine common Internet viruses, such as common trojans, ransomware, mining programs, and DDoS trojans. Apsara Stack Security experts check and verify all the automatically quarantined viruses to ensure a minimum false positive rate. If the virus blocking feature is disabled, Server Guard generates alerts when viruses are detected. You must manually manage detected viruses in Apsara Stack Security Center. We recommend that you enable the virus blocking feature to improve the security of your servers.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Virus
Def ence.
3. On the Ant i-virus tab, click Scan.
4. In the dialog box that appears, select the servers that you want to scan.
5. Click Scan.
6. On the Ant i-virus page, click the Real-t ime prot ect ion tab and enable the virus blocking
feature. After the virus blocking feature is enabled, Server Guard automatically quarantines common viruses that are detected. Quarantined viruses are listed on the Alerts page. To filter quarantined viruses, you can select the Precision def ense type. Detect and remove webshells
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Int rusion Prevent ion > Virus
Def ence.
3. Specify servers for webshell detection.
i. In the Webshell Det ect ion section, click Manage. ii. Select the servers for which you want to enable webshell detection. iii. Click OK to complete the configuration.

### 5.5 Log retrieval

#### 5.5.1 Log retrieval overview

The log retrieval function provided by Server Security allows you to manage logs scattered in various systems of Apsara Stack in a centralized manner, so that you can easily identify the causes of issues that occur on your servers. The log retrieval function supports storage of logs for 180 days and query of logs generated within 30 days. Benefits The log retrieval function provides the following benefits: End-t o-end log ret rieval plat f orm: Allows you to retrieve logs of various Apsara Stack services in a centralized manner and trace issues easily. Cloud-based SaaS service: Allows you to query logs on all servers in Apsara Stack without additional installment and deployment. Supports TB-level data retrieval. It also allows you to add a maximum of 50 inference rules (Boolean expressions) in a search condition and obtain full-text search results within several seconds. Supports a wide range of log sources. Supports log shipping, which allows you to import security logs to Log Service for further analysis. Scenarios You can use log retrieval to meet the following requirements: Securit y event analysis: When a security event is detected on a server, you can retrieve the logs to identify the cause and assess the damage and affected assets. Operat ion audit : You can audit the operation logs on a server to identify high-risk operations and serious issues in a meticulous way. Supported log types Log types

| Log type | Description |
|---|---|
| Logon history | Log entries about successful system logons |
| Brute-force attack | Log entries about system logon failures that are generated during brute-force attacks |
| Process snapshot | Log entries about processes on a server at a specific time |
| Listening port snapshot | Log entries about listening ports on a server at a specific time |
| Account snapshot | Log entries about account logon information on a server at a specific time |
| Process initiation | Log entries about process initiation on a server |
| Network connection | Log entries about active connections from a server to external networks |

#### 5.5.2 Query logs

This topic describes how to search for and view server logs. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Log Ret rieval.
3. Specify search conditions.

| Search condition | Description |
|---|---|
| Log source | The log source that you want to query. For more information, see Log sources. |
| Field | The field that is recorded for the log source. For more information, see Log sources. |
| Keyword | The keyword of the field. |
| Logical operator | The equality operator. |
| + | The inference rules in a search condition for a log source. |
| Add conditions | The search conditions for different log sources. |

4. Click Search and view the search result.
Reset : Click Reset to clear the search condition configurations. Save Search: Click Save Search to save the search condition configurations which you can use to search for logs in the future. Saved Searches: Click Saved Searches to select and use a search condition that you saved.

#### 5.5.3 Supported log sources and fields

This topic describes the log sources and fields that are supported by the log retrieval feature. The log retrieval feature allows you to query the following types of log sources. You can click a log source link to view the fields that can be retrieved.

| Log source | Description |
|---|---|
| Logon history | Log entries about successful system logons |
| Logs of brute-force attacks | Log entries about failed system logons during brute-force attacks |
| Process snapshot logs | Log entries about processes on a server at a specific point in time |
| Logs of listening port snapshots | Log entries about listening ports on a server at a specific point in time |

| psara Stack Security | User Guide·Server securit |
|---|---|

| Log source | Description |
|---|---|
| Account snapshot logs | Log entries about account-based logons on a server at a specific point in time |
| Process startup logs | Log entries about process startups on a server |
| Network connection logs | Log entries about active connections from a server to the Internet. |

Logon history The following table describes the fields that you can use to query the logon history.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| warn ip _ | string | The source IP address used for the logon. |
| warn port _ | string | The logon port. |
| warn user _ | string | The username used for the logon. |
| warn type _ | string | The logon type. |
| warn count _ | string | The number of logon attempts. |

Logs of brute-force attacks The following table describes the fields that you can use to query logs of brute-force attacks.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| warn ip _ | string | The source IP address of the attack. |
| warn port _ | string | The target port of the attack. |
| warn user _ | string | The target username of the attack. |
| warn type _ | string | The attack type. |
| warn count _ | string | The number of brute-force attack attempts. |

Process startup logs The following table describes the fields that you can use to query process startup logs.

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

Logs of listening port snapshots The following table describes the fields that you can use to query logs about listening port snapshots.

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

Account snapshot logs The following table describes the fields you can use to query account snapshot logs.

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
| last logon _ | string | The last logon time. |
| user | string | The username. |
| status | string | The account status. Valid values: 0: disabled 1: normal |

Process snapshot logs The following table describes the fields that you can use to query process snapshot logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |

| U | ser Guide·Server security |   | Apsara Stack Securit | y |
|---|---|---|---|---|

| Field | Data type | Description |
|---|---|---|
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

Network connection logs The following table describes the fields that you can use to query network connection logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| src ip _ | string | The source IP address. |
| src port _ | string | The source port. |
| proc path _ | string | The path of the process file. |
| dst port _ | string | The destination port. |
| proc name _ | string | The name of the process. |
| dst ip _ | string | The destination IP address. |
| status | string | The status. |

#### 5.5.4 Logical operators

The log retrieval feature supports multiple search conditions. You can add multiple logical operators to one search condition for one log source, or combine multiple search conditions for several log sources by using different logical operators. This topic describes the logical operators that are supported in log retrieval. Examples are provided to help you understand these operators. The following table describes the logical operators that are supported in log retrieval. Logical operators

| Logical operator | Description |
|---|---|
| and | Binary operator. This operator is in the format of query 1 and query 2 , which indicates the intersection of the query results of query 1 and query 2 . Not e If no logical operators are used for multiple keywords, the default operator is AND. |
| or | Binary operator. This operator is in the format of query 1 or query 2 , which indicates the union of the query results of query 1 and query 2 . |
| not | Binary operator. This operator is in the format of query 1 not query 2 , which indicates the results that match query 1 but do not match query 2 . This format is equivalent to query 1 - query 2 . Not e If you use only not query 1 , the log data that does not contain the query results of query 1 is returned. |

|   | query 1 or query 2 |   |
|---|---|---|
| query 1 |   |   |
|   |   | query 2 |

### 5.6 Settings

#### 5.6.1 Install the Server Guard agent

This topic describes how to install the Server Guard agent. Context To use the protection services provided by Server Guard, you must install the Server Guard agent on the operating system of your server. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Server Set t ings > Client
Inst allat ion.
3. (Optional)On the Client Installation page, click the Client t o be inst alled tab to view the number
of servers on which the Server Guard agent is not installed. On this tab, you can also view the information about the servers. You can specify the operating system type, IP address, or server name to search for a server.
4. Click the Client Inst allat ion Guide tab.
5. Obtain and install the Server Guard agent based on the operating system type of your server.
Windows a. In the left-side pane of the page, click Click t o download to download the installation package to your computer. b. Upload the installation package to your server. For example, you can use an FTP client to upload the installation package to your server. c. Run the installation package on your server as an administrator. Not e If you install the agent on a server that is not in Alibaba Cloud, you are prompted to enter the installation verification key. You can find the installation verification key on the Client Installation Guide tab. Linux a. In the right-side pane of the page, select Alibaba Cloud Server or Non-Alibaba Server. b. Select the installation command for your 32-bit or 64-bit operating system and click Copy to copy the command. c. Log on to your Linux server as an administrator. d. Run the installation command on your Linux server to download and install the Server Guard agent.

#### 5.6.2 Manage protection modes

This topic describes how to manage protection modes for each server to improve the efficiency and security of the server. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Server Securit y > Server Set t ings > Prot ect ion Mode.
3. On the Protection Mode page, click Manage.
Configure protection modes for servers. Business First Mode: The peak CPU utilization is less than 10%, and the peak memory usage is less than 50 MB. Prot ect ion First Mode: The peak CPU utilization is less than 20%, and the peak memory usage is less than 80 MB.
4. Click OK.

## 6 Physical server security

### 6.1 Create and grant permissions to a security administrator account

security administrator account The physical server security feature is used to ensure the security of physical servers on the platform side. This feature requires you to use a dedicated security administrator account for the platform. This topic describes how to create and grant permissions to a security administrator account. Procedure
1. Log on to the Apsara Uni-manager Management Console as a system administrator.
For more information, see the "Log on t o t he Apsara Uni-manager Management Console" topic of Apsara Uni-manager Management Console User Guide.
2. Create a dedicated organization that is used to manage the security of physical servers, and obtain
the primary key of the organization. Not ice Make sure that the organization is used only to manage the security of physical servers. Do not add Elastic Compute Service (ECS) instances to the organization. i. Create the dedicated organization. For more information, see Ent erprise Cent er > Organizat ion Management > Creat e Organizat ion in Apsara Uni-manager Management Console User Guide. ii. Obtain the primary key of the newly created organization. For more information, see Ent erprise Cent erOrganizat ion Management Obt ain t he AccessKey pair of an organizat ion in Apsara Uni-manager Management Console User Guide.
3. Create a dedicated account to manage the security of physical servers.
For more information, see Ent erprise Cent er > User Management > Syst em User Management > Creat e User in Apsara Uni-manager Management Console User Guide. Not e When you create the account, take note of the following points for the organizat ion and role: In the Organizat ion section, select the organization that is created in the previous step. In the Role section, select Plat f orm Securit y Conf igurat ion Administ rat or and Securit y Syst em Conf igurat ion Administ rat or.
4. Log on to Apsara Stack Security Center by using the newly created account.
For more information, see Log on to Apsara Stack Security Center.
5. Add the primary key of the newly created organization to the protection configuration of
physical servers. i. In the left-side navigation pane, choose Securit y Management Cent er (SOC) > Syst em Conf igurat ion > Global Set t ings. ii. On the Global Set t ings page, click the Physical Server Prot ect ion tab. iii. Click Add Account . iv. In the Add Account dialog box, specify the Username and Primary Key parameters. Username: Enter the account that you created in Step 3. Primary Key: Enter the primary key that you obtained in Step 2. v. Click OK. Result After you complete the configuration, the Physical Server Securit y feature appears in the left-side navigation pane of Apsara Stack Security. Then, you can use the account created in this topic to maintain the security of physical servers.

### 6.2 View the information on the Overview page

Overview page Security administrators can view the security status of all physical servers on the Overview page of Apsara Stack Security. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Overview.
3. On the Overview page, view the security status of your physical servers.
Security event statistics: displays the numbers of security events on the physical servers. Security events include unusual logons, webshells, and server exceptions. Event s: displays the trends of security events on the physical servers. A security event is an intrusion event that is detected on a physical server. Prot ect ion St at us: displays the number of physical servers that are protected and the number of offline physical servers. Recent Import ant Event s: displays the recent important security events that are detected on the physical servers. You can click a security event to view its details.

### 6.3 Physical servers

#### 6.3.1 Manage physical server groups

This topic describes how to manage physical server groups. To facilitate the security management of physical servers, you can add the physical servers to groups and view their security events by group. Context By default, physical servers do not belong to a server group. You must add your physical servers to a server group. If you delete a group, all the physical servers in the group are retained but no longer belong to a server group. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Servers.
3. In the left-side group pane, manage sever groups.
Create a group. Click the Add Subgroup icon next to All Servers or a specific group, enter a group name, and click OK. Not e The system supports a maximum of three levels of groups. Modify a group. Click the Modify Group Name icon next to the target group, enter a new name, and click OK. Delete a group. Click the Delete icon next to the target group. In the message that appears, click OK. Not e After you delete a group, all servers in the group are automatically moved to the def ault group. Sort groups. Click Manage Groups to sort groups in descending order by priority.
4. Change the server group of specific physical servers.
i. Select servers from the list on the right. ii. Click Change Group. iii. In the Change Group dialog box that appears, select a group from the drop-down list. iv. Click OK.

#### 6.3.2 Manage physical servers

This topic describes how to manage servers. On the Servers page, you can view the status of servers protected by Server Guard. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Servers.
3. (Optional)Search for a server.
To view the agent status of a server, enter the server IP address in the search bar, and click Search. Detailed server information, such as security information, is displayed.
4. View the agent status and detailed security information of the server.
Click in the upper-right corner of the page to select the information columns you want to display. The following table lists the information categories.

| Category | Information |
|---|---|
| Basic information | Server IP/Name Tag OS Region |
| Agent status | Agent Status |
| Threat prevention | Vulnerability Baseline Risk |
| Intrusion detection | Unusual Logons Webshells Suspicious Servers |
| Server fingerprints | Processes Ports Root Accounts/Total Accounts |

5. Manage servers.

| Action | Description |
|---|---|
| Change Group | Select servers and click Change Group to add the selected servers to a new group. |
| Modify Tag | Select servers and click Modif y T ag to modify tags for the servers. |
| Security Inspection | Select servers and click Securit y Inspect ion to select the items to be checked. |

| Guide·Physical server security | Apsara Stack Securit |
|---|---|

| Action | Description |
|---|---|
| Delete External Servers | Select ext ernal servers, and choose More > Delet e Ext ernal Servers. |
| Disable Protection | Select the servers whose agent status is Online, and choose More > Disable Prot ect ion. This temporarily disables protection for these servers to reduce server resource consumption. |
| Enable Protection | Select the servers whose agent status is Disable Prot ect ion, and choose More > Enable Prot ect ion. This enables protection for these servers. |

### 6.4 Intrusion detection

#### 6.4.1 Configure policies to identify unusual logons

logons This topic describes how to configure logon security. You can set approved locations, IP addresses, time periods, and accounts for logons. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Int rusion Det ect ion.
3. Click the Unusual Logons tab.
4. Click Logon Securit y in the upper-right corner of the page.
5. Set approved logon locations.
To add an approved logon location, follow these steps: i. Click Add. ii. Select a logon location from the drop-down list. iii. Specify the servers on which the selected logon location takes effect. Click All Servers to select specific servers. Click Server Groups to select servers by group. iv. Click OK. Not e Click Modif y or Delet e to modify or delete an approved logon location.
6. Set approved logon IP addresses.
Turn on the Disapproved IP Alert switch. The switch is turned on if it turns green. To add an approved logon IP address, follow these steps: i. Click Add. ii. In the Specif y an Approved Logon IP section, enter an IP address. iii. Specify the servers on which the specified IP address takes effect. Click All Servers to select specific servers. Click Server Groups to select servers by group. iv. Click OK. Click Modif y or Delet e to modify or delete an approved logon IP address.
7. Set approved logon time periods.
Turn on the Disapproved T ime Alert switch. The switch is turned on if it turns green. To add an approved logon time period, follow these steps: i. Click Add. ii. In the Specif y an Approved Logon Durat ion section, specify a time period. iii. Specify the servers on which the specified logon time period takes effect. Click All Servers to select specific servers. Click Server Groups to select servers by group. iv. Click OK. Click Modif y or Delet e to modify or delete an approved logon time period.
8. Set approved accounts.
Turn on the Disapproved Account Alert switch. The switch is turned on if it turns green. To add an approved account, follow these steps: i. Click Add. ii. In the Specif y an Approved Account section, enter an account. iii. Select the servers on which the specified account takes effect. Click All Servers to select specific servers. Click Server Groups to select servers by group. iv. Click OK. Click Modif y or Delet e to modify or delete an approved account. What's next After you configure policies to identify unusual logons, you can view and handle unusual logons on the Unusual Logons tab. For more information, see Handle unusual logons.

#### 6.4.2 Handle unusual logons

This topic describes how to handle unusual logons. The unusual logons include logons from disapproved locations or IP addresses, logons by using brute-force attacks or disapproved accounts, and logons at a disapproved time. Context For more information about the policies that are configured to identify unusual logons, see Configure policies to identify unusual logons.
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Int rusion Det ect ion.
3. Click the Unusual Logons tab.
4. (Optional)Specify the filter conditions to locate unusual logons. The filter conditions include
Asset , Alert T ype, and St at us. Not e If you skip this step, all unusual logons appear in the event list.
5. In the event list, view and handle unusual logons.
Check whether an unusual logon is a false positive. If the unusual logon is a false positive, click Ignore. If the unusual logon is not a false positive, harden the security of the physical server and click Ignore. To harden the security of the physical server, you can specify a more complex password, fix vulnerabilities, or check configuration items.

### 6.5 Server fingerprints

#### 6.5.1 Configure data refresh frequencies

You can configure the frequencies at which the data of running processes, system accounts, listening ports, and software versions is collected and refreshed. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Server Fingerprint s.
3. In the upper-right corner of the Server Fingerprints page, click Conf igure.
4. In the Conf igure dialog box, configure the data refresh frequencies for the listening ports, running
processes, system accounts, and software versions.
5. Click OK.

#### 6.5.2 View listening ports

Apsara Stack Security regularly collects information about listening ports on a server.
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Server Fingerprint s.
3. Click the List ening Port tab.
4. (Optional)Specify Port Number and Process Name. Then, click Search to search for the specified
port or process. Not e If you skip this step, all listening ports appear in the port list.
5. In the port list, view Port Number, Net work Prot ocol, and Servers.
6. Click a port number to view the information about the assets and processes that are associated
with the port.

#### 6.5.3 View running processes

Apsara Stack Security regularly collects the process information of a server. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Server Fingerprint s.
3. Click the Running Process tab.
4. (Optional)Specify Process Name and User and click Search to search for the specified process or
user. Not e If you skip this step, all processes appear in the process list.
5. In the process list, view Process Name and Servers.
6. Click the name of a running process to view the information about the assets, paths, and running
users that are associated with the process.

#### 6.5.4 View account information

Apsara Stack Security regularly collects the account information of a server. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Server Fingerprint s.
3. Click the Account Inf ormat ion tab.
4. (Optional)Specify Username and click Search to search for the specific account.
Not e If you skip this step, all accounts appear in the account list.
5. In the account list, view Account and Servers.
6. Click the name of an account to view the information about the assets and user groups that are
associated with the account. You can also check whether the account has root permissions

#### 6.5.5 View software versions

This topic describes how to view the information about the software versions of physical servers. The information facilitates the management of software assets. Context This topic covers the following scenarios: Check for software assets that are installed without authorization. Check for outdated versions of software assets. Find affected assets if vulnerabilities are detected. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Server Fingerprint s.
3. Click the All Versions tab.
4. (Optional)Specify Sof t ware Name, Version Name, and Sof t ware Inst allat ion Pat h. Then, click
Search to search for specific software. Not e If you skip this step, all software appears in the software list.
5. In the software list, view the information in the Sof t ware Name and Host s columns.
6. Click the name of the software to view the host, version, and installation directory of the software.

### 6.6 Log retrieval

#### 6.6.1 Supported log sources and fields

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

Logon history The following table describes the fields that you can use to query the logon history.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |
| warn ip _ | string | The source IP address used for the logon. |
| warn port _ | string | The logon port. |
| warn user _ | string | The username used for the logon. |
| warn type _ | string | The logon type. |
| warn count _ | string | The number of logon attempts. |

Logs of brute-force attacks The following table describes the fields that you can use to query logs of brute-force attacks.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |

| Field | Data type | Description |
|---|---|---|
| warn ip _ | string | The source IP address of the attack. |
| warn port _ | string | The target port of the attack. |
| warn user _ | string | The target username of the attack. |
| warn type _ | string | The attack type. |
| warn count _ | string | The number of brute-force attack attempts. |

Process startup logs The following table describes the fields that you can use to query process startup logs.

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

Logs of listening port snapshots The following table describes the fields that you can use to query logs about listening port snapshots.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |

| psara Stack Security |   | User Guide·Physical server securit |
|---|---|---|
| Field | Data type | Description |
| IP | string | The IP address of the server. |
| src port _ | string | The listening port. |
| src ip _ | string | The listening IP address. |
| proc path _ | string | The path of the process file. |
| pid | string | The ID of the process. |
| proc name _ | string | The name of the process. |
| proto | string | The protocol. |

Account snapshot logs The following table describes the fields you can use to query account snapshot logs.

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

| ser Guide·Physical server security |   | Apsara Stack Securit |
|---|---|---|

| Field | Data type | Description |
|---|---|---|
| last logon _ | string | The last logon time. |
| user | string | The username. |
| status | string | The account status. Valid values: 0: disabled 1: normal |

Process snapshot logs The following table describes the fields that you can use to query process snapshot logs.

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

Network connection logs The following table describes the fields that you can use to query network connection logs.

| Field | Data type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address of the server. |

| psara Stack Security |   | User Guide·Physical server securit |
|---|---|---|
| Field | Data type | Description |
| src ip _ | string | The source IP address. |
| src port _ | string | The source port. |
| proc path _ | string | The path of the process file. |
| dst port _ | string | The destination port. |
| proc name _ | string | The name of the process. |
| dst ip _ | string | The destination IP address. |
| status | string | The status. |

#### 6.6.2 Logical operators

The log retrieval feature supports multiple search conditions. You can add multiple logical operators to one search condition for one log source, or combine multiple search conditions for several log sources by using different logical operators. This topic describes the logical operators that are supported in log retrieval. Examples are provided to help you understand these operators. The following table describes the logical operators that are supported in log retrieval. Logical operators

| Logical operator | Description |
|---|---|
| and | Binary operator. This operator is in the format of query 1 and query 2 , which indicates the intersection of the query results of query 1 and query 2 . Not e If no logical operators are used for multiple keywords, the default operator is AND. |
| or | Binary operator. This operator is in the format of query 1 or query 2 , which indicates the union of the query results of query 1 and query 2 . |
| not | Binary operator. This operator is in the format of query 1 not query 2 , which indicates the results that match query 1 but do not match query 2 . This format is equivalent to query 1 - query 2 . Not e If you use only not query 1 , the log data that does not contain the query results of query 1 is returned. |

|   | query 1 or query 2 |   |
|---|---|---|
| query 1 |   |   |
|   |   | query 2 |

#### 6.6.3 Query logs

This topic describes how to search for and view physical server logs. Procedure
1. Log on to Apsara Stack Security Center by using an Apsara Stack tenant account.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Log Ret rieval.
3. Specify search conditions.
Not e For more information about log sources, log fields, and logical operators, see Supported log sources and fields and Inference rules and logical operators.
4. Click Search and view the search result.
Reset : Click Reset to clear the search condition configurations. Save Search: Click Save Search to save the search condition configurations which you can use to search for logs in the future. Saved Searches: Click Saved Searches to select and use a search condition that you saved.

### 6.7 Configure security settings for physical servers

### physical servers

This topic describes how to configure security settings for physical servers. You can enable or disable periodic trojan scans. You can also specify the working mode of the Server Guard agent. Procedure
1. Log on to Apsara Stack Security Center.
Not e For more information about the Apsara Stack tenant account, see Create and grant permissions to a security administrator account.
2. In the left-side navigation pane, choose Physical Server Securit y > Set t ings.
3. Enable periodic trojan scans for physical servers.
i. In the Trojan Scan section, click Manage. ii. In the All Servers section, select the physical servers on which you want to perform periodic trojan scans. Then, click the rightwards arrow. iii. Click OK.
4. On the Prot ect ion First Mode page, click Manage next to Protection Mode.
Configure protection modes for servers. Business First Mode: In this mode, the peak CPU utilization is less than 10%, and the peak memory usage is less than 50 MB. Prot ect ion First Mode: In this mode, the peak CPU utilization is less than 20%, and the peak memory usage is less than 80 MB.

## 7 Application security

### 7.1 Quick start

This topic helps you get started with the features of Web Application Firewall (WAF). WAF uses intelligent semantic analysis algorithms to identify web attacks. WAF also uses a learning model to enhance its analysis capabilities and meet your daily security protection requirements without relying on traditional rule libraries. The following content describes the procedure for using WAF:
1. Customize WAF protection rules.
WAF provides default protection policies. You can also customize policies that suit your business requirements. For more information about how to configure protection policies, see Configure protection policies. For more information about how to configure custom rules, see Create a custom rule. For more information about how to configure HTTP flood protection rules, see Configure an HTTP flood protection rule.
2. Add websites that you want to protect.
WAF can protect Internet websites and virtual private cloud (VPC) websites. For more information about how to add an Internet website to WAF for protection, see Add an Internet website for protection. For more information about how to add a VPC website to WAF for protection, see Add a VPC website for protection.
3. Configure Domain Name System (DNS) resolution.
For more information about how to change the DNS-resolved source IP address for a website to a virtual IP address assigned by WAF, see Modify DNS resolution settings.
4. View WAF protection results.
For more information about how to view the protection overview, see View protection overview. For more information about how to view the service access information, see View Web service access information. For more information about how to view the detection logs for web attacks, see View attack detection logs. For more information about how to view the detection logs for HTTP flood attacks, see View HTTP flood protection logs.

### 7.2 Detection overview

#### 7.2.1 View protection overview

This topic describes how to view the Web Application Firewall (WAF) protection overview. Context The Detection Overview page displays information such as the statistics of previous attacks, the geographical distribution of attackers, the total number of requests, and the number of blocked requests. You can also view details about the attacks. This way, you can customize rules to protect your web services. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose St at ist ic > Det ect ion Overview.
4. On the Det ect ion Overview page, view data on the St at ist ics wit hin Last 24 Hours and
St at ist ics wit hin Last 30 Days tabs. Total Requests Displays the total number of requests. Attack times Displays the total number of attacks. Blocked Requests Displays the number of blocked requests. Attacker Geographical Distribution Displays the distribution of attackers on a map. You can select a map of China or a map of the world. Initiate Attack IP appears most frequently (Display TOP 5) Displays the top five IP addresses from which the most attacks are launched in a bar chart. The xaxis indicates the numbers of requests. The y-axis indicates the IP addresses. Distribution of Attack Types (Display TOP 5) Displays the distribution of the top five attack types and the number of attacks of each type in a bar chart. Most Attacked Websites (Display TOP 5) Displays the top five attacked websites and the number of attacks on each website in a bar chart.

#### 7.2.2 View access information

This topic describes how to view access information about web services. Context Web Application Firewall (WAF) monitors the access of web services. This way, security administrators can analyze the service access information to detect vulnerabilities and improve security of the services. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose St at ist ic > Access St at us Monit or.
4. Filter access records to view details.

### 7.3 Protection logs

#### 7.3.1 View attack detection logs

This topic describes how to view attack detection logs. Context These logs allow you to analyze attacks on your web services. You can update the protection policies and custom rules, and fix the web service vulnerabilities based on the analysis results. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Det ect ion Logs > At t ack Det ect ion Logs.
4. Click Filt er, specify filter conditions, and then click OK.
If you specify multiple conditions, they are evaluated by using a logical AND. The system returns the required logs only when all the conditions are met.
5. View the attack detection logs.

#### 7.3.2 View HTTP flood protection logs

This topic describes how to view HTTP flood protection logs. Context These logs allow you to analyze HTTP flood attacks on your web services. In addition, you can update the HTTP flood protection rules and HTTP flood whitelist, and fix the web service vulnerabilities based on the analysis results. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Det ect ion Logs > HT T P Flood Det ect ion Logs.
4. Click Filt er, specify filter conditions, and then click OK.
Not e If you specify multiple conditions, they are evaluated by using a logical AND. The system returns the required logs only when all the conditions are met.
5. View the HTTP flood detection logs.
The blocked HTTP flood attacks, related rules, and attack time are displayed.

#### 7.3.3 View system operation logs

This topic describes how to view system operation logs. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree, choose Det ect ion Logs > Syst em operat ion log.
4. View the system operation logs.
The usernames, content, IP addresses, and creation time are displayed.

#### 7.3.4 View access logs

This topic describes how to view access logs. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Det ect ion Logs > Access Log.
4. Click Filt er, specify filter conditions, and then click OK.
If you specify multiple conditions, they are evaluated by using a logical AND. The system returns the required logs only when all the conditions are met.
5. View the access logs.
The requested addresses, destination IP addresses, source IP addresses, methods, response status codes, and time are displayed.

### 7.4 Protection configuration

#### 7.4.1 Configure protection policies

This topic describes how to configure Web Application Firewall (WAF) protection policies. Context WAF provides a default protection policy. You can also customize protection policies to suit your business requirements. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Prot ect ion Conf igurat ion > Websit e
Prot ect ion Policies.
4. Click Add a prot ect ion policy. In the panel that appears, specify Policy name and click Conf irm.
5. In the Operat ion column of the new protection policy, click the
icon to view or edit the policy.

| Parameter | Description |
|---|---|
| Decode | Select algorithms that you want to use to decode the requests. |
| At t ack Det ect ion Modules | Specify the types of attacks that you want to detect and the risk levels of attacks that you want to block. |
| Block Opt ions | Specify the HTTP status code and image that you want WAF to return when it blocks an attack. |
| HT T P Response Processing | Specify Enable HT T P response processing and Response Det ect ion Max Body Size. |
| HT T P Request Body Det ect ion | Specify Response Det ect ion Max Body Size. |
| Det ect ion T imeout | Specify Enable Det ect ion T imeout and T imeout T hreshold. |

For example, perform the following steps to configure modules in the At t ack Det ect ion Modules section: i. Move the pointer over a specific module in the At t ack Det ect ion Modules section. In this example, move the pointer over SQL Inject ion Det ect ion Module and click the modif y icon. ii. In the SQL Inject ion Det ect ion Module panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Enabled | Specify whether to enable the detection module. |
| Blocking T hreshold | Valid values: Not Forbid, Only ForbidHigh Risk, ForbidMedium or High Risk, and Forbid All. |
| Record T hreshold | Valid values: Not record, Onlyrecord High Risk, recordMedium or High Risk, and record All. |
| Det ect Non-Inject ed SQL | Specify whether to enable detection for NoSQL injection vulnerabilities. |

iii. Click OK.
6. Manage protection policies.
To delete a protection policy, select the protection policy. Then, in the upper-right corner, choose More > Delet e Select ed Prot ect ion Policies. In the message that appears, click OK. Not e You cannot delete the default protection policy.

#### 7.4.2 Create a custom rule

This topic describes how to create a custom rule for Web Application Firewall (WAF). Context You can create custom rules to meet different requirements for intrusion detection. You can create, edit, or delete custom rules as an administrator. You can use custom rules to filter out requests that meet specific conditions. Multiple custom rules are evaluated by using a logical OR. If two custom rules use the same conditions but trigger different actions such as blocking traffic or allowing traffic, WAF runs the first rule. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Prot ect ion Conf igurat ion >
Cust omized Rules.
4. In the upper-right corner, click Add Rule. In the Add Cust omized Rules panel, configure the
parameters. Parameters used to create a custom rule

| Parameter | Description |
|---|---|

| Parameter | Description |
|---|---|
| T ype | The operating mode of the rule. Valid values: Block, Allow, Monit or, and Det ect ion module cont rol. Block: If an HTTP request meets the conditions of the rule, the HTTP request is blocked. Allow: If an HTTP request meets the conditions of the rule, the HTTP request is allowed. Monit or: If an HTTP request meets the conditions of the rule, the HTTP request is recorded and allowed. Det ect ion module cont rol |
| Comment | The remarks about the rule. We recommend that you enter the purpose of the rule. |
| Risk level | The risk level. Valid values: No t hreat , Low Risk, Medium Risk, and High Risk. |
| Mat ching Pat t ern | The conditions that trigger the rule. Click Add Pat t ern to specify more than one condition. Multiple conditions are evaluated by using a logical AND. The custom rule takes effect only when all conditions are met. |
| Apply t o Websit es | The websites that you want the rule to protect. |
| Log Recording Opt ion | Specifies whether to record a log when the rule is triggered. The default value is Enable Log Recording. After Log Recording Option is set to Enable Log Recording, all interception events are recorded in the intrusion detection logs. |
| At t ack T ype | The type of attack that you want the rule to block. |
| Expirat ion T ime | The time at which the rule expires. |

5. Click Conf irm.
6. Manage custom rules.
Edit a rule. To edit a rule, click the icon in the Act ions column. Enable a rule. To enable a rule that is disabled, select the rule and choose More > Enable Select ed Rules. Disable a rule. To disable a rule that is enabled, select the rule and choose More > Disable Select ed Rules. Export a rule. To export a rule, select the rule and choose More > Export Select ed Rules. Delete a rule. To delete a rule that you no longer need, select the rule and choose More > Delet e Select ed Rules.

#### 7.4.3 Configure an HTTP flood protection rule

This topic describes how to configure an HTTP flood protection rule. Context An HTTP flood attack is a type of DDoS attack that targets the application layer. Attackers use proxy servers or zombies to overwhelm targeted web servers by sending a large number of HTTP requests. Create an HTTP flood protection rule
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Prot ect ion Conf igurat ion > HT T P
Flood Det ect ion.
4. Click Add Rule. The Add HT T P Flood Det ect ion Rules panel appears.
5. Configure parameters and click Conf irm.

| Parameter | Description |
|---|---|
| Rule Mode | The action on requests after the HTTP flood protection rule is triggered. Valid values: Blocking Mode and Observe. Blocking Mode: limits the requests that trigger the HTTP flood protection rule. Observe: records the requests that trigger the HTTP flood protection rule, but does not limit the requests. |

| Parameter | Description |
|---|---|
| Rule T ypes | The type of the HTTP flood protection rule. Valid values: Rest rict Users by Policy and Rest rict Known Users. The difference between the two types is determined by whether requests of users are initiated from a specific IP address or in a specific session. Rest rict Users by Policy: limits requests that meet all the configuration items of the HTTP flood protection rule. Configuration items include Rest rict ion T rigger T hreshold, Rest rict ed URL Address, Rest rict ion Mode, Rest rict ion T ime, and St at ist ical Range of Visit s in the Advanced section. Rest rict Known Users: limits requests that are initiated from specific IP addresses or in specific sessions based on the HTTP flood protection rule. To achieve this purpose, you must configure the IP address or session list and the limit mode. After you configure the list, the HTTP flood protection rule limits requests based on the list. |
| Rule Name | The name of the HTTP flood protection rule. |
| T arget T ype | The type of source for requests that are limited. Valid values: IP and SESSION. Not e If you set T arget T ype to SESSION, you can apply the HTTP protection rule only to a website whose User Ident if icat ion is set to WAF User Syst em. For more information, see Add an Internet website for protection. |
| Rest rict ion T rigger T hreshold | If you set Rule T ypes to Rest rict Users by Policy, you must configure the triggering conditions for the HTTP flood protection rule. |
| Rest rict ed URL Address | If you set Rule T ypes to Rest rict Users by Policy, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Pref ix URL Record all IP addresses |
| Rest rict ed IP List or Rest rict ed SESSION List | If you set Rule T ypes to Rest rict Known Users, you must enter the IP addresses or sessions from which you want to limit requests based on the setting of T arget T ype. You can enter only one IP address or session in each line. |

| Parameter | Description |
|---|---|
| Rest rict ed URL Address | If you set Rule T ypes to Rest rict Known Users, you must specify the URL addresses that are protected based on the HTTP flood protection rule. URL Pref ix URL Rest rict user access t o all addresses |
| Rest rict ion Mode | The mode in which the HTTP flood protection rule limits requests. Valid values: Forbidden: The rule blocks specific sources from accessing the specified URL address. Frequency cont rol: The rule limits the frequency at which specific sources access the specified URL address. |
| Rest rict ion T ime | The time at which the action specified in the HTTP flood protection rule takes effect. |
| St at ist ical Range of Visit s | If you set Rule T ype to Rest rict Users by Policy, you can specify the range of data records to limit requests in the Advanced section. Statistics Full Access Data: If you select this option, the frequency of requests is limited when the requests are forwarded to WAF and meet the HTTP flood protection rule, regardless of which data records the requests access. This decreases system performance. Statistics TOP Access Data: If you select this option, the frequency of requests is limited when the requests meet the preceding conditions and access the top 100 data records. This option helps minimize the decrease in system performance. You can select this option when the number of accessed data records is larger than 100. Note that the top 100 data records are measured based on real-time monitoring. |

Manage HTTP flood protection rules
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the rule list, manage existing HTTP flood protection rules. Modification is allowed.
Search for a rule. Click Filt er. In the Filt er It em panel, specify filter conditions. Enable a rule. Select a rule that is in the Disabled state and choose More > Enable Select ed Rules. Disable a rule. Select a rule that is in the Enabled state and choose More > Disable Select ed Rules. Delete a rule. Select a rule and choose More > Delet e Select ed Rules.

#### 7.4.4 Configure the HTTP flood whitelist

This topic describes how to configure the HTTP flood whitelist. Context If a request source is trusted, you can add this request source to the HTTP flood whitelist to allow all requests from this source. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Prot ect ion Conf igurat ion > HT T P
Flood Det ect ion.
4. On the HT T P Flood Det ect ion Whit elist tab, click Add Whit elist It em, add a trusted request
source, and then click Conf irm.

| Parameter | Description |
|---|---|
| T ype | Select the type of the request source. Valid values: IP and SESSION. |

| Parameter | Description |
|---|---|
| IP or SESSION | Specify the IP addresses or sessions based on the setting of T ype. You can enter only one IP address or session in each line. |
| Comment | Enter remarks for the request source. |

5. Manage request sources in the whitelist.
Search for a request source in the whitelist. Click Filt er. In the panel that appears, specify a filter condition or click Add Filt er It em to specify more filter conditions. Remove a request source from the whitelist. Select the request source and choose More > Delet e Select ed It ems.

#### 7.4.5 Manage SSL certificates

This topic describes how to upload or delete SSL certificates. Context After you upload an SSL certificate on the SSL Cert if icat e Management page, you can select this certificate when you add an HTTPS website for protection on the Prot ect ion Sit e Management page. Not e When you add an HTTPS website for protection on the Prot ect ion Sit e Management page, you must select the SSL certificate that corresponds to the domain name of the HTTPS website. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Prot ect ion Conf igurat ion > SSL Cert if icat e Management .
4. Upload a new certificate.
i. Click Upload SSL Cert if icat e. ii. In the Name field, enter a name f or t he new cert if icat e. We recommend that you enter the domain name for easier management. Not e If your Certificate Authority (CA) certificate and private key are in the same file, select Include privat e key in cert if icat e f ile. iii. In the File section, upload the CA certificate file and private key file. iv. Specify Cert if icat e Password. v. Click Conf irm.
5. (Optional)Delete the uploaded SSL certificate.
If an uploaded SSL certificate expires, you can delete it. i. In the SSL certificate list, select the certificate that you want to delete. ii. Choose More > Delet e select ed SSL cert if icat e. iii. In the message that appears, click OK.

#### 7.4.6 Add Internet websites for protection

This topic describes how to add Internet websites to Web Application Firewall (WAF). Context WAF can protect the following types of websites: Internet websites. Virtual Private Cloud (VPC) websites. For more information about how to add VPC websites to WAF, see Add a VPC website for protection. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Prot ect ion Conf igurat ion > Prot ect ion Sit e Management . On the page that appears,
click the Int ernet Websit es tab.
4. In the upper-right corner, click Add a sit e. The Add Protected Site panel appears.
5. In the Monitoring Information step, configure parameters and click Next .
Specify the Internet website that you want WAF to protect. WAF can protect both HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Prot ect ed Websit e Name | The name of the website that you want WAF to protect. |
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard. If you specify multiple domain names, separate them with commas (,). |
| Port Set t ings | The port that WAF listens on. If the website supports HTTPS requests, select Enable SSL and upload an HTTPS certificate. If the website can be accessed over multiple ports, click Add a group of port s to add the required ports. |

| Parameter | Description |
|---|---|
| Cert Set t ing | The HTTPS certificate of the website. Valid values: Upload a New Certificate and Choose an Existing Certificate. Upload a New Certificate: If the HTTPS certificate of the website has not been uploaded to WAF, select this option. By default, the HTTPS certificate and private key are separately uploaded. If you select Include privat e key in cert if icat e f ile, upload only one file that contains both the HTTPS certificate and private key. Choose an Existing Certificate: If the HTTPS certificate of the website has been uploaded to WAF, select this option. Then, select the required HTTPS certificate from the drop-down list. Not e This parameter is required only if you select Enable SSL next to the list ening port field. |
| Name | The name of the HTTPS certificate. Not e This parameter is required only if you select Enable SSL next to the list ening port field. |
| File | The HTTPS certificate and private key. By default, the HTTPS certificate and private key are separately uploaded. If you select Include privat e key in cert if icat e f ile next to Name, upload only one file that contains both the HTTPS certificate and private key. Not e This parameter is required only if you select Enable SSL next to the list ening port field. |
| Virtual IP | The IP address type and virtual IP address. Not e You can select an IPv6 address as the virtual IP address for WAF. By default, WAF provides 10 virtual IP addresses. You can add more virtual IP addresses based on your business requirements. Not e A virtual IP address is available only for the department to which the creator of the virtual IP address belongs. |

6. In the Request Processing Method step, configure parameters and click Next .

| Response mode | Parameter | Description |
|---|---|---|
| Forward t o Backend Server | Load Balancing Algorit hm | The algorithm for load balancing. Valid values: Weight ed Round Robin, Source Address Hash, and Least Connect ions Met hod. |
|   | Backend Server Address | The address of the origin server to which WAF forwards inbound traffic. Valid values: Fill in t he back-t o- source address and Ret urn t o t he back-t o-source inst ance. Fill in t he back-t o-source address: Enter the address of the origin server. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorit hm. Ret urn t o t he back-t o-source inst ance: Enter the address of a specific ECS or SLB instance. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorit hm. |
|   | X-Forwarded-For | The pass-through mode of the actual source IP address. The X-Forwarded-For (XFF) header is used to identify the actual source IP address of an HTTP client. The header is used for traffic forwarding services, such as HTTP proxy and load balancing. |

| Response mode | Parameter | Description |
|---|---|---|
| Redirect | Response St at us Code | The HTTP status code that WAF returns when it redirects inbound traffic to a specified address. Valid values: 301, 302, and 307. 301: The requested page is permanently moved to another URL. 302: The requested page is temporarily moved to another URL. The requester must continue to use the original URL for future requests. 307: The requested page is temporarily moved to another URL. The requester must continue to use the original URL for future requests. |
|   | Redirect address | The destination URL for redirection. |
| Respond wit h Specif ied Cont ent | Response St at us Code | The HTTP status code that WAF returns when it returns specified content. Valid values: 200, 404, and 503. |
|   | Response | The content to return. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

7. In the Protection Policy step, configure parameters and click Next. Then, go to the Finish step.
Not e You can configure a protection policy only if you set Request Processing Met hod to Forward t o Backend Server.

| Parameter | Description |
|---|---|
| Prot ect ion Policy | Select a WAF protection policy. For more information, see Configure protection policies. |
| User Ident if icat ion | Specify whether to enable the user identification feature. Not e If you enabled HTTP flood protection for the protected website and set T arget T ype to SESSION when you configured the HTTP flood protection rule, you must set User Ident if icat ion to WAF User Syst em. |

#### 7.4.7 Add VPC websites for protection

This topic describes how to add Virtual Private Cloud (VPC) websites to Web Application Firewall (WAF) for protection. Context WAF can protect the following types of websites: Internet websites. For more information about how to add an Internet website for protection, see Add an Internet website for protection. VPC websites. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF > Prot ect ion
Conf igurat ion > Prot ect ion Sit e Management . On the page that appears, click the VPC Websit es tab.
3. In the upper-right corner, click Add a sit e. The Add Prot ect ed Sit e panel appears.
4. In the Monitoring Information step, configure parameters and click Next .
Specify the VPC website that you want WAF to protect. WAF can protect both HTTP and HTTPS websites.

| Parameter | Description |
|---|---|
| Prot ect ed Websit e Name | The name of the website that you want WAF to protect. |

| Parameter | Description |
|---|---|
| Domain Name | The domain name of the website. You can use an asterisk (*) as a wildcard. If you specify multiple domain names, separate them with commas (,). |
| Port Set t ings | The port that WAF listens on. If the website supports HTTPS requests, select Enable SSL and upload an HTTPS certificate. If the website can be accessed over multiple ports, click Add a group of port s to add the specific ports. |
| Cert Set t ings | The HTTPS certificate of the website. Valid values: Upload a New Cert if icat e and Choose an Exist ing Cert if icat e. Not e Specify this parameter only if you select Enable SSL next to Port Set t ings. Upload a New Cert if icat e: If the HTTPS certificate used by the website has not been uploaded to WAF, select this option. By default, the HTTPS certificate and private key are separately uploaded. If you select Include privat e key in cert if icat e f ile, upload only a file that contains both the HTTPS certificate and private key. Choose an Exist ing Cert if icat e: If the HTTPS certificate used by the website is uploaded to WAF, select this option. Then, select the specific HTTPS certificate from the drop-down list. |
| Name | The name of the HTTPS certificate. Not e Specify this parameter only if you select Enable SSL next to Port Set t ings and set Cert Setting to Upload a New Certificate. |
| File | The HTTPS certificate and private key to upload. By default, the HTTPS certificate and private key are separately uploaded. If you select Include privat e key in cert if icat e f ile next to Name, upload only a file that contains both the HTTPS certificate and private key. Not e Specify this parameter only if you select Enable SSL next to Port Set t ings and set Cert Setting to Upload a New Certificate. |

5. In the set up VPC step, configure parameters and click Next .

| Parameter | Description |
|---|---|
| Prot ect ed VPC | The VPC to which the website belongs. |
| Virt ual Swit ch | The vSwitch associated with the specified VPC. |
| Creat e Virt ual IP Met hod | The method to create a virtual IP address. Valid values: Select an exist ing virt ual IP and Creat e virt ual IP. |
| VPC Virt ual IP | If you set Creat e Virt ual IP Met hod to Select an exist ing virt ual IP, select an existing virtual IP address from the VPC Virt ual IP drop-down list. If you set Creat e Virt ual IP Met hod to Creat e virt ual IP, click Click t o Creat e Vip next to VPC Virt ual IP to generate a virtual IP address. |

6. In the Request Processing Method step, configure parameters and click Next .

| Response mode | Parameter | Description |
|---|---|---|
|   | Load Balancing Algorit hm | The algorithm for load balancing. Valid values: Weight ed Round Robin, Source Address Hash, and Least Connect ions Met hod. |

|   | ity Apsara Stack Securit |   |
|---|---|---|
| Guide·Application secur |   |   |
| Response mode | Parameter | Description |
| Forward t o Backend Server | Backend Server Address | The IP address of the origin server to which WAF forwards inbound traffic. Valid values: Fill in t he back-t o-source address and Ret urn t o t he back- t o-source inst ance. Fill in t he back-t o-source address: Enter the address of the origin server. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorit hm. Ret urn t o t he back-t o-source inst ance: Enter the address of a specific Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance. If you enter multiple addresses, load balancing is performed based on the specified load balancing algorit hm. |
|   | X-Forwarded-For | The passthrough mode of the actual source IP address. The X-Forwarded-For (XFF) header is used to identify the actual source IP address of an HTTP client. The header is used for request forwarding services, such as HTTP proxy and load balancing. |
| Redirect | Response St at us Code | The HTTP status code that WAF returns when it forwards inbound traffic to a specified address. Valid values: 301, 302, and 307. 301: The requested page is permanently moved to another URL. 302: The requested page is temporarily moved to another URL. The requester must continue to use the original URL for future requests. 307: The requested page is temporarily moved to another URL. The requester must continue to use the original URL for future requests. |
|   | Redirect address | The required URL for redirection. |
| Respond wit h Specif ied Cont ent | Response St at us Code | The HTTP status code that WAF returns when it returns specified content. Valid values: 200, 404, and 503. |
|   | Response | The content to return. For example, you can upload an image for the Response parameter. If a user visits the website, WAF returns the uploaded image. |

7. In the Protection Policy step, configure parameters and click Next. Then, go to the Finish step.

| Parameter | Description |
|---|---|
| Prot ect ion Policy | Select a WAF protection policy. For more information, see Configure protection policies. |
| User Ident if icat ion | Specify whether to enable the user identification feature. |

#### 7.4.8 Verify the configurations of a website on your on-premises server

your on-premises server This topic describes how to verify the configurations of a website on your on-premises server. Context Before you use Web Application Firewall (WAF) to scrub traffic destined for a website, we recommend that you verify the configurations of the website on your on-premises server. After you add the virtual IP address and the domain of a website to the hosts file on your on-premises server, the request to access the domain from a local browser passes through WAF first. Procedure
1. Log on to Apsara Stack Security Center.
2. Add the virtual IP address and domain name to the hosts file on your on-premises server.
If your computer runs Windows 7, the hosts file is stored in the following path: C:\Windows\Syst em32\drivers\etc\hosts. i. Open the hosts file by using a text editor, such as Notepad. ii. Add the following content to the end of the file: <The virtual IP address that is assigned by WAF ><Protected domain name>. Not e The IP address preceding the domain name is the virtual IP address that is assigned by WAF.
3. Ping the protected domain name from your on-premises server.
The returned IP address must be the virtual IP address that is assigned by WAF in the hosts file. If the returned IP address is still the IP address of the origin server, refresh the local Domain Name System (DNS) cache.
4. Enter the domain name in the address bar of your browser and press Enter.
If the access configurations on WAF are correct, you can visit the website.
5. Verify the protection capability of WAF.
Simulate a web attack request and check whether WAF blocks the request. For example, add /?alert(xss) after the URL. If you try to visit www.example.com/? `alert(xss)` , WAF is expected to block the request.

#### 7.4.9 Modify DNS resolution settings

This topic describes how to modify the Domain Name System (DNS) resolution settings to connect your website to Web Application Firewall (WAF). Context Before you can modify the DNS resolution settings, you must verify the settings on your computer and make sure that the settings are correct. Then, the traffic destined for your website can be redirected to WAF after you modify the settings. The domain name of a protected website may not be resolved by a DNS provider. For example, a website may use a Server Load Balancer (SLB) instance to connect to the Internet. In this case, you can perform the following operation to protect the website by using WAF: Specify the virtual IP address that WAF assigns to your website as the back-to-origin IP address of the SLB instance. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Prot ect ion Conf igurat ion >
Prot ect ion Sit e Management .
4. Find the website whose DNS resolution settings you want to modify and click the
icon in the Operat ion column.
5. On the Basic Inf ormat ion tab, record the virtual IP address assigned to the website.
6. Log on to the console of the DNS provider and find the DNS resolution settings for the domain
name of the website. Then, change the IP address in the A record to the virtual IP address assigned to the website. Not e We recommend that you set the TTL to 600 seconds in DNS resolution settings. The larger the TTL is, the longer it takes to synchronize and update DNS records.

### 7.5 System management

#### 7.5.1 View the load status of nodes

This topic describes how to view the load status of Web Application Firewall (WAF) nodes. The status information includes CPU utilization and memory usage. You can identify faults based on the status and check whether scale-out or scale-up is required. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Syst em Inf o > Node st at us.
4. On the Payload St at us tab, view the load status of WAF nodes.
In the Payload Status section, you can view the CPU utilization and memory usage of WAF nodes. In the CPU usage and Memory usage sections, you can view the changes in CPU utilization and memory usage over a specific period of time.

#### 7.5.2 View the network status of nodes

This topic describes how to view the network status of Web Application Firewall (WAF) nodes. The status information includes network I/O, traffic detection status, and traffic forwarding status. Node network status
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. Choose Syst em Inf o > Node st at us.
4. Click the Node Net work St at us tab.
5. View the network I/O of WAF nodes.
Traffic detection status
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF > Syst em Inf o > Node
st at us.
3. Click the Det ect ion St at us tab.
4. View the traffic detection status of WAF nodes.
Traffic forwarding status
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF > Syst em Inf o > Node
st at us.
3. Click the Forward St at us tab.
4. View the traffic forwarding status of WAF nodes.

#### 7.5.3 View the disk status of nodes

This topic describes how to view the disk status of Web Application Firewall (WAF) nodes. You can identify faults based on the status and check whether scale-out or scale-up is required.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Syst em Inf o > Node st at us.
4. Click the Disk St at us tab to view the disk status of WAF nodes.
In the Disk Status section, you can view the disk I/O and disk usage of WAF nodes. In the Read and Writ e sections, you can view the changes in disk reads and writes over a specific period of time.

#### 7.5.4 Configure alerts

This topic describes how to add a syslog server to Web Application Firewall (WAF). After the syslog server is added, WAF alert logs can be pushed to the syslog server over the syslog protocol. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF.
3. In the left-side navigation tree of the WAF page, choose Syst em Set t ings > Syslog
Conf igurat ion.
4. On the Alarm Service Conf igurat ion tab, click Add alarm service.
5. In the Add Alarm Service panel, configure parameters.

| Parameter | Description |
|---|---|
| Syslog Server | The IP address and port number of the syslog server. |

| Guide·Application security | Apsara Stack Securit |
|---|---|
| Parameter | Description |
| RFC | The Request for Comments (RFC) document that defines the syslog protocol. Valid values: RFC3164 and RFC5424. |
| Protocol | The transmission protocol. Valid values: T CP and UDP. |
| Comment | The description of the syslog server. This information facilitates subsequent identification and management. |
| General | The type of alert. Valid values: System Management and System Monitor and Alarm. |
| Security | The module whose alert logs are sent to the syslog server. |

6. Click Conf irm. The newly added syslog server appears in the list of the Alarm Service Configuration
tab.
7. Find the newly added syslog server and click the
icon in the Operat ion column to test whether alerts are sent. If a message appears, indicating that the alert test is successful, the syslog server is added. If an error message appears, WAF cannot connect to the syslog server.

#### 7.5.5 Configure alert thresholds

This topic describes how to configure alert thresholds. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Applicat ion Securit y > WAF. On the page that appears,
choose Syst em Set t ings > Syslog Conf igurat ion.
3. Click the Alarm T hresholdConf igurat ion tab and click the
icon next to the threshold that you want to modify.
4. In the panel that appears, specify the threshold.

| Threshold | Description |
|---|---|
| Queries per second | If queries per second exceed this threshold, alerts are sent. If this threshold is set to 0, no alerts are sent. |
| Number of new connections | If a large number of new connections exist, no alerts are sent. |
| CPU usage is too high | If CPU utilization exceeds this threshold in a specific period of time, alerts are sent. |
| Memory usage is too high | If memory usage exceeds this threshold in specific a period of time, alerts are sent. |
| Disk usage is too high | If disk usage exceeds this threshold, alerts are sent. |

5. Click OK.
ter (SOC)

## 8 Security Operations Center (SOC)

(SOC)

### 8.1 View the dashboard

This topic describes how to view the overall security information about the Apsara Stack network environment. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Overview.
3. In the upper-right corner of the Dashboard page, select a time range from the T ime St at ist ics
drop-down list. Valid values: Last 24 Hours, Last 7 Days, and Last 30 Days.
4. View the overall security information.
The Dashboard page displays the following information: New Blocked At t acks, New Alert s, New Vulnerabilit ies, and Prot ect ed Depart ment s T op 5 At t acked Depart ment s, T op 5 Securit y Alert Depart ment s T o Be Handled, and T op 5 Vulnerabilit y Depart ment s T o Be Handled Securit y T rend, which supports a switchover between Tenant and Platform Lat est Securit y Alert s and Alert T ypes Lat est At t acks and At t ack T ypes ECS Prot ect ion St at e, New Asset s, and Prot ect ed Asset s

### 8.2 Security Monitoring

ter (SOC)

#### 8.2.1 View security monitoring data of tenants

This topic describes how to view the security monitoring data of tenants on the Attack Protections, Security Alerts, and Vulnerabilities tabs. Attack Protections
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > T enant Securit y Monit oring.
3. On the At t ack Prot ect ions tab, view all attack events.
You can specify search conditions to search for attack events based on the following table.

| Search condition | Description |
|---|---|
| Department | The department to which the assets affected by the attack belong. |
| Data source | The data source. |
| Status | The attack status. |
| Attack type | The attack type. |
| Start time and end time | The time range to query the attack event. |
| Attack name or asset keyword | The attack name or the keywords of affected assets. |

4. View details in the attack event list.
5. Click the icons in the upper-left corner to refresh or export the list.
The following list describes how to perform the operations: Click the icon to refresh the attack event list. Click the icon to export the attack event list.
6. Find an attack event. In the Actions column, block requests from a specific IP address, create a tag
for the event, or view logs and details of the event. The following list describes how to perform the operations: Block requests from a specific IP address: Click Block IP Addresses. In the Block IP Addresses dialog box, configure parameters to block requests from a specific IP address. For more information, see Block IP Addresses. In the upper-right corner, click View Blocked IPs to view details about the blocked IP addresses. Create a tag: Click T ag. In the Cust omize T ag dialog box, create a tag for the attack event and click OK. ter (SOC) View logs: Click View Log. On the Cloud T enant Logs tab of the Log Audit page, view the logs of tenants. View details: Click Det ails to view the details of the attack event. Security Alerts
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > T enant Securit y Monit oring. On the page that appears, click the Securit y Alert s tab.
3. (Optional)Specify search conditions.
Not e If you want to view all security alerts, skip this step.

| Search condition | Description |
|---|---|
| Department | The department to which the assets affected by the alert belong. |
| Data source | The data source. |
| Level | The alert level. You can select one or more alert levels. Valid values: Urgency Warning Reminder |
| Status | The alert status. |
| Type | The alert type. You can select All Alert T ypes or a specific alert type. |
| Start time and end time | The time range to query the alert. |
| Alert name or asset keyword | The alert name or the keywords of affected assets. |

4. View details in the security alert list.
5. Click the icons in the upper-left corner to refresh or export the list.
The following list describes how to perform the operations: Click the icon to refresh the security alert list. Click the icon to export the security alert list. Vulnerabilities ter (SOC)
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > T enant Securit y Monit oring. On the page that appears, click the Vulnerabilit ies tab.
3. Click the Vulnerabilit ies or Server Conf igurat ions tab.
Vulnerabilit ies: provides vulnerability information. Server Conf igurat ions: provides information about server baseline risks.
4. Specify search conditions.
Not e If you want to view all vulnerabilities or server baseline risks, skip this step.

| Search condition | Description |
|---|---|
| Department | The department to which the assets affected by the vulnerability or server baseline risk belong. |
| Level | The level of the vulnerability or server baseline risk. |
| Type | The type of the vulnerability or server baseline risk. |
| Status | The status of the vulnerability or server baseline risk. |
| Start time and end time | The time range to query the vulnerability or server baseline risk. |
| Vulnerability or risk name, asset keyword, or CVE ID keyword | The name of the vulnerability or server baseline risk, or the keywords of affected assets or CVE IDs. |

5. Click the icons in the upper-left corner to refresh or export the list of vulnerabilities or server
baseline risks. The following list describes how to perform the operations: Click the icon to refresh the list of vulnerabilities or server baseline risks. Click the icon to export the list of vulnerabilities or server baseline risks.

#### 8.2.2 View security monitoring data of the Apsara Stack platform

Apsara Stack platform This topic describes how to view the security monitoring data of the Apsara Stack platform on the Attack Protections, Security Alerts, and Vulnerabilities tabs. ter (SOC) Attack Protections
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > Plat f orm Securit y Monit oring.
3. On the At t ack Prot ect ions tab, view all attack events.
You can specify search conditions to search for attack events based on the following table.

| Search condition | Description |
|---|---|
| Data source | The data source. |
| Status | The attack status. |
| Attack type | The attack type. |
| Start time and end time | The time range to query the attack event. |
| Attack name or asset keyword | The attack name or the keywords of affected assets. |

4. View details in the attack event list.
5. Click the icons in the upper-left corner to refresh or export the list.
The following list describes how to perform the operations: Click the icon to refresh the attack event list. Click the icon to export the attack event list.
6. Find an attack event. In the Actions column, block requests from a specific IP address, create a tag
for the event, or view logs and details of the event. The following list describes how to perform the operations: Block requests from a specific IP address: Click Block IP Addresses. In the Block IP Addresses dialog box, configure parameters to block requests from a specific IP address. For more information, see Block IP Addresses. In the upper-right corner, click View Blocked IPs to view details about the blocked IP addresses. Create a tag: Click T ag. In the Cust omize T ag dialog box, create a tag for the attack event and click OK. View logs: Click View Logs. On the Cloud Plat f orm Logs tab of the Log Audit page, view the logs of the platform. View details: Click Det ails to view the details of the attack event. Security Alerts
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > Plat f orm Securit y Monit oring. On the page that appears, click the Securit y ter (SOC) Alert s tab.
3. (Optional)Specify search conditions.
Not e If you want to view all security alerts, skip this step.

| Search condition | Description |
|---|---|
| Data source | The data source. |
| Level | The alert level. You can select one or more alert levels. Valid values: Urgency Warning Reminder |
| Status | The alert status. |
| Type | The alert type. You can select All Alert T ypes or a specific alert type. |
| Start time and end time | The time range to query the alert. |
| Alert name or asset keyword | The alert name or the keywords of affected assets. |

4. View details in the security alert list.
5. Click the icons in the upper-left corner to refresh or export the list.
The following list describes how to perform the operations: Click the icon to refresh the security alert list. Click the icon to export the security alert list. Vulnerabilities
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > Plat f orm Securit y Monit oring. On the page that appears, click the Vulnerabilit ies tab and the Plat f orm Baseline tab.
3. Specify search conditions.
Not e If you want to view all baseline risks of the platform, skip this step.

| Search condition | Description |
|---|---|
| Level | The level of the baseline risk. |

ter (SOC)

| OC) |   |
|---|---|
| Search condition | Description |
| Type | The type of the baseline risk. |
| Status | The status of the baseline risk. |
| Start time and end time | The time range to query the baseline risk. |
| Risk name or asset keyword | The risk name or the keywords of affected assets. |

4. Click the icons in the upper-left corner to refresh or export the list of platform baseline risks.
The following list describes how to perform the operations: Click the icon to refresh the list of platform baseline risks. Click the icon to export the list of platform baseline risks.

#### 8.2.3 View the global traffic

This topic describes how to view the global traffic, including the average traffic, peak traffic, overall traffic trends, traffic of tenants, and traffic of platforms. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Securit y
Monit oring > Global T raf f ic Analysis.
3. On the Global T raf f ic Analysis page, view the global traffic.
You can view the following information on this page: View the average traffic and peak traffic a. In the upper-right corner of the Global T raf f ic Analysis page, select a time range and traffic direction. Valid values of time ranges: Last 6 Hours, Last 24 Hours, and Last 7 Days. Valid values of traffic directions: Inbound and Out bound. b. In the upper-left corner of the Global Traffic Analysis page, view the average and peak traffic of the specified traffic direction within the specified time range. View traffic trends a. In the upper-right corner of the Global T raf f ic Analysis page, select a traffic type. b. View the overall traffic trends of each traffic type within the specified time range. View the traffic of tenants on the T enant T raf f ic tab View the traffic of platforms on the Plat f orm T raf f ic tab ter (SOC)

### 8.3 Asset Management

#### 8.3.1 View tenant assets

This topic describes how to view the assets of users. The assets include Elastic Compute Service (ECS) instances, ApsaraDB RDS instances, Object Storage Service (OSS) buckets, Server Load Balancer (SLB) instances, and elastic IP addresses (EIPs). Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Asset
Management > T enant Asset s.
3. Select the required service. Example: Elast ic Comput e Service (ECS).
4. Specify search conditions to view a specific asset.
Not e If you want to view all assets, skip this step.

| Search condition | Description |
|---|---|
| Department | The department to which the asset belongs. |
| VPC | The virtual private cloud (VPC) to which the asset belongs. |
| Status | The running status of the asset. |
| New | Specifies whether the asset to query is newly added. |
| Server name or IP address | The keywords of the asset name. |

5. View asset information in the asset list.

#### 8.3.2 View platform assets

This topic describes how to view the assets of the platform. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Asset
Management > Plat f orm Asset s.
3. Specify search conditions to view a specific asset.
Not e If you want to view all assets, skip this step.
4. View asset information in the asset list.
ter (SOC)

### 8.4 Log Analysis

#### 8.4.1 View the Log Overview page

This topic describes how to view the logs that are displayed in the widgets on the Log Overview page. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Overview.
3. On the Log Overview page, view the widgets of the logs.
You can perform the following operations to modif y or delet e the widgets on the Log Overview page: To modify a widget, click Modif y in the upper-right corner of the widget. a. In the Modif y dialog box, reconfigure the Chart T ype, Cat egory, and Value parameters. When you configure the Cat egory and Value parameters, take note of the following points: Cat egory: If you set Chart T ype to Bar Chart , Line Chart , Pie Chart , or Sheet , you must specify this parameter. Value: If you set Chart T ype to Pie Chart or Individual Value Plot , you must specify this parameter. b. Click Ref resh to preview the widget in the right side of the Modify dialog box. c. Above the widget, enter a new name to rename the widget. d. Click OK. The widget is updated on the Log Overview page. To delete a widget, click Delet e in the upper-right corner of the widget. The widgets on the Log Overview page are created on the Log Audit page. To create a widget, click Please go t o t he log audit page t o add a chart in the Add cust om visualizat ion chart section in the lower part of the Log Overview page. On the Log Audit page, create a custom widget. For more information, see View global logs.

#### 8.4.2 View global logs

This topic describes how to view global logs. Global logs are classified into logs of tenants, logs of the platform, and logs of data centers based the department to which the logs belong. View a log widget
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Audit .
3. Click the tab on which you want to view the logs of a department. For example, if you want to
view the logs of tenants, click the Cloud T enant Logs tab.
4. Specify search conditions and click the
icon. Then, you can view the logs that meet the search conditions in the sections of log distribution chart and log list. ter (SOC)

| Search condition | Description |
|---|---|
| Department | If you want to view the logs of a tenant, you can specify this search condition. Select the department to which the tenant belongs. |
| Log source | Select the type of the system from which you want to collect the logs, the name of the system from which you want to collect the logs, and the log type from the drop-down list. |
| Duration | Select the time range within which you want to collect the logs. Valid values: Last 15 Minut es, Last 30 Minut es, Last 24 Hours, Last 7 Days, Last 30 Days, and Cust om. |
| Start time and end time | Specify the start and end time within which you want to collect the logs. |
| Log content | Enter the log content in the search box. If you want to save the search conditions as frequently used search conditions, click Save Search Condit ion. If you want to use these frequently used search conditions, click Hist orical Records. Then, you can view the logs that meet the search conditions. |

If you want to search for logs by using JSON domain-specific language (DSL) statements, click Advanced Search. In the Advanced Search dialog box, enter JSON DSL statements and click Submit . Create a log widget
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Audit .
3. Click the tab on which you want to view the logs of a department. For example, if you want to
view the logs of tenants, click the Cloud T enant Logs tab.
4. In the lower part of the Log Audit page, click the Visualizat ion tab.
5. On the Visualizat ion tab, configure parameters in the Chart section.

| Parameter | Description |
|---|---|
| Chart T ype | The type of widget that you want to display on the Overview page. Valid values: Bar Chart , Line Chart , Pie Chart , Individual Value Plot , and Sheet . |
| Cat egory | This parameter is required only if you select Bar Chart , Line Chart , Pie Chart , or Sheet for Chart T ype. The type of item that you want to display in the horizontal axis or the column header of the widget. |

ter (SOC)

| Parameter | Description |
|---|---|
| Value Cat egory | The type of item that you want to display in the vertical axis or the row header of the widget. |
| Value T ype | The type of value that you want to display in the widget. Valid values: count , max, min, avg, sum, unique count , and median. _ If you want to display multiple value types in the widget, click Add Value Field. Then, you can configure the Value Cat egory and Value T ype parameters. |

6. In the upper-left corner of the preview section on the Visualization tab, enter a name for the
widget.
7. Click Updat e.
After the widget is created, you can view the widget on the Log Overview page. To configure the content to be displayed in the log list, you can perform the following steps: In the lower part of the Log Audit page, click the Log tab. Then, click the icon. To export the log list, click the icon.

#### 8.4.3 Log configurations

##### 8.4.3.1 Manage log sources

This topic describes how to view and manage the log sources that are connected to Security Operations Center (SOC).
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Conf igurat ions.
3. Click the Log Sources tab. On the Log Sources tab, view the overview log information and log
list. This tab provides the following information: In the upper section of the Log Sources tab, you can view the total volume of log data and the total number of connected log sources. In the upper-right corner above the log source list, you can specify conditions to search for specific log sources.

| Search condition | Description |
|---|---|
| Access syst em t ype | The type of the source system in the log source that is connected to SOC. Valid values: Host , St orage, Applicat ion, Net working, Dat a, Securit y, and Ot her. |
| Log T ype | The type of log that is collected by SOC. Valid values: Operat ions Log, Operat ional Log, Alert Log, and Ot hers. |

| Stack Security | User Guide·Security Operations Ce ter (SOC |
|---|---|

| Search condition | Description |
|---|---|
| Access mode | The mode that is used to collect logs. Valid values: Cust om and Built -in. |
| St at us | The status of the log source that is connected to SOC. Valid values: On and Of f . In the log source list, find a log source and click the icon in the St at us column to set the log source to on or off. In the Tips message, click OK. |

4. Find a log source and click Modif y in the Actions column.
5. In the Edit dialog box, configure the Storage Days and View Permissions parameters. Then, click OK.

##### 8.4.3.2 Create a log collection task

This topic describes how to create a log collection task. Prerequisites If you use Logtail to collect logs, make sure that the following conditions are met: The Logtail agent is installed. A server group for which you want to configure Logtail is created. For more information, see Manage log collectors.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Conf igurat ions.
3. On the Log Conf igurat ions page, click the Log Access T ask tab.
4. On the Log Access T ask tab, click Add.
5. In the Conf igure Log Source step of the Creat e T ask wizard, configure parameters and click
Next .

| Parameter | Description |
|---|---|
| T ask Name | The name of the log collection task. |
| Access Syst em Name | The name of the source system from which you want to collect the logs. Example: Windows operating system. |
| Access Syst em T ype | The type of the source system from which you want to collect the logs. Valid values: Host , St orage, Applicat ion, Net working, Dat a, Securit y, and Ot her. |
| Log Source Name | The subtype of the log type. |
| Log T ype | The type of log that you want to collect. Valid values: Operat ions Log, Operat ional Log, Alert Log, and Ot hers. |

ter (SOC)

| Parameter | Description |
|---|---|
| Source | The department to which the logs belong. Valid values: Cloud T enant , Cloud Plat f orm, and On-Premises Dat a Cent er. |

6. In the left-side navigation tree of the Conf igure Access Met hod step, select a data source type,
configure parameters, and then click Next . Valid values of Data Source Type: Syslog, SLS, and Logtail. If you select Syslog, you must configure the following parameters.

| Parameter | Description |
|---|---|
| IP Address | The IP address or CIDR block used to report syslog logs. |
| Prot ocol | The network protocol used when the logs are collected. Valid values: UDP and T CP. |
| Access Syst em T ype | The type of source system from which you want to collect the logs. Valid values: Host , Applicat ion, Net working, and Ot her. |
| Keyword | The keyword of log data. |

If you select SLS, you must configure the following parameters.

| Parameter | Description |
|---|---|
| Log Project | The name of the project in Log Service. |
| Log St ore | The name of the Logstore in Log Service. |
| Endpoint | The endpoint used to connect to the project in a specific region. |
| accessKey | The AccessKey ID of your account used to access Log Service. |
| secret Key | The AccessKey secret of your account used to access Log Service. |

If you select Logtail, you must configure the following parameters.

| Parameter | Description |
|---|---|
| Name | The name of the log collector. |
| Log t ype | The type of log that you want to collect. Valid values: JSON, Apsara, Separat or, and Regular Expression. |
| Log Pat t ern | The format of log file names. Example: access*.log. |
| Log Pat h | The path used to store the logs that you want to collect. Absolute paths and relative paths are supported. You can use wildcards in relative paths. |
| Log Sample | A sample log entry from the logs that you want to collect. |

| Stack Security | User Guide·Security Operations Ce ter (SOC |
|---|---|

| Parameter | Description |
|---|---|
| Regular Expression t o Mat ch First Log Ent ry | After you enter the sample log ent ry, click Generat e Aut omat ically. A regular expression is generated to match the first line of the log entry. |
| Regular Expression | Click Regular Expression. In the Generat e Regular Expression dialog box, select the fields that you want to extract and click Generat e Regular Expression. After the regular expression is generated, click OK. |
| Dat e Format | The date format that is automatically generated based on the extracted time fields. |
| Apply t o Server Group | The server group for which you want to configure Logtail. |

7. In the Parse and Normalize Dat a step, configure parameters and click Next .

| Parameter | Description |
|---|---|
| Dat a acquisit ion met hod | The method used to obtain the sample log entry. Valid values: Aut omat ically Obt ain and Manual Input . |
| Dat a Sample | If you select Manual Input as the data acquisition method, you must enter the sample log entry. |
| Resolver | The parser, which can be selected based on the sample log entry. Valid values: JSON and jsonArray. |
| Ext ract Values | The content that can be extracted from the logs. Click Add Field. In the Add Field dialog box, configure the Original Ext ract Key, Original Ext ract Value, Enrich Dat a, and T arget T ype parameters. Then, click OK. Valid values of Enrich Dat a: Ret ain Original Field, T ag Field, Delet e Field, Rename Field, Aut omat ically Fill Syst em T ime, Assign Value t o Const ant , and Assign Value t o Variable. |

8. In the Generat e T ask step, configure the Log Source Name, St orage Durat ion, and View
Permissions parameters.
9. Click Save.
After the log collection task is created, the task appears in the list of log collection tasks. You can publish, modify, or delete the task in the Actions column of the task. Publish: After the log collection task is created, logs are not automatically collected. You must click Publish. After the task is published, the icon appears in the Access St at us column of the task. ter (SOC) You can click the switch in the Access St at us column to change the status of the log collection task. Edit : You can click Edit to change the configurations in the Parse and Normalize Dat a and Generat e T ask steps. You cannot change the data source type or log collector. Delet e: If you no longer need the log collection task, you can click Delet e in the Actions column of the task.

##### 8.4.3.3 Manage log collectors

Before you can use Logtail to collect logs, you must install the Logtail agent, add log collectors, and create server groups. This topic describes how to install the Logtail agent, add log collectors, and create server groups. Install the Logtail agent If the Logtail agent has been installed, the system automatically uninstalls the existing version of the Logtail agent, deletes the /usr/local/ilogtail directory, and then reinstalls the Logtail agent. After the new version of the Logtail agent is installed, it automatically runs, and a startup application is added to the registry.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Conf igurat ions.
3. On the Log Conf igurat ions page, click the Collect ors tab.
4. Install the Logtail agent.
On the Collect ors tab, install the Logtail agent based on the operating system of the server and the installation method that is supported by the Logtail agent. If the server runs a Linux operating system and the Logtail agent supports manual installation, perform the following steps: a. In the Linux Operat ing Syst ems section, click Download Inst allat ion Package and determine whether to download a 32-bit or 64-bit installation file to your computer. b. Log on to the server as an administrator. Then, run the installation command to install the Logtail agent. If the server runs a Windows operating system and the Logtail agent supports manual installation, perform the following steps: a. In the Windows Operat ing Syst ems section, click Download Inst allat ion Package to download the installation file to your computer. b. Upload the installation file to the server. For example, you can use an FTP client to upload the installation file to the server. c. Run the installation file on the server as an administrator. After the Logtail agent is installed, it automatically runs, and a startup application is added to the registry. Add a log collector
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
ter (SOC) Log Conf igurat ions.
3. In the Collect ors section, click Add Collect or.
4. In the Add Collect or dialog box, configure the following parameters and click OK.

| Parameter | Description |
|---|---|
| Collect or IP Address | The IP address of the source whose logs you want to collect. |
| Server Name | The name of the server where the Logtail agent is installed. |
| Operat ing Syst em | The operating system of the server where the Logtail agent is installed. |

After the log collector is added, you can view the information of the log collector in the Collect ors section. The information includes Collect or IP Address and Server Name. Create a server group
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Conf igurat ions.
3. In the Server Groups section, click Creat e Server Group.
4. In the Creat e Server Group dialog box, configure the following parameters and click OK.

| Parameter | Description |
|---|---|
| Server Group Name | The name of the server group. |
| IP Addresses | The IP addresses of the servers that you want to add to the server group. To add a server to the server group, perform the following steps: i. In the Ungrouped Servers section, select the server that you want to add to the group. ii. Click the icon to add the server to the Servers t o Be Grouped section. |

After the server group is created, you can view basic information of the server group in the Server Groups section. If you want to view detailed information of a server group or delete a server group, perform the following steps: Find the server group. Then, click Det ails in the Actions column to view the detailed information of the server group. Find the server group. Then, click Delet e in the Actions column to delete the server group.

##### 8.4.3.4 Manage storage policies

This topic describes how to view and configure storage policies for logs.
1. Log on to Apsara Stack Security Center.
ter (SOC)
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Log Conf igurat ions.
3. On the Log Conf igurat ions page, click the Policies tab.
4. On the Policies tab, view the storage policy for logs.
5. Click Modif y.
6. On the Policies tab, configure parameters such as the storage periods for logs and monitoring
data. Then, click Modif y.

| Section | Parameter | Description |
|---|---|---|
| Log St orage (Advanced) | Maximum Log Size | The upper limit of the storage space that can be used to store logs. |
|   | Maximum Storage Period | The maximum number of days during which logs can be stored. |
| Securit y Monit oring Dat a St orage (Advanced) | ApsaraDB RDS Storage Period | The maximum number of days during which monitoring data can be stored. |

#### 8.4.4 Security Audit

##### 8.4.4.1 Overview

A security audit refers to the systemic and independent inspection and verification of activities and behavior in the computer network environment. Delegated by property owners and authorized by management authorities, professional auditors give their assessments according to relevant laws and regulations. When the administrator needs to backtrack system operations, the administrator can perform a security audit. Security audits are long-term security management activities throughout the lifecycle of cloud services. The security audit feature of Apsara Stack Security can collect system security data, analyze weaknesses in system operations, report audit events, and classify audit events into important, moderate, and low risk levels. The security administrator views and analyzes audit events to continuously improve the system and ensure the security and reliability of cloud services.

##### 8.4.4.2 View security audit overview

This topic describes how to view the summarized information about security audit. Context The Overview tab provides reports on the raw log trend, audit event trend, audit risk distribution, and security event distribution. The reports are displayed in run charts or pie charts to help security administrators analyze the trend of risks in your cloud services. On the Overview tab, security administrators can check the number of log entries and the storage usage in a specific time range. ter (SOC)
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Overview tab.
3. On the Overview tab, view the audit summary for the last seven days.
Trends of Raw Log This chart displays the trend of logs generated by physical servers, network devices, ApsaraDB RDS instances, Elastic Compute Service (ECS) instances, and API calls in the last seven days. Security administrators can analyze the trend to check whether the number of log entries is at a normal level. Audit Events This chart displays the trend of audit events that are generated by physical servers, network devices, ApsaraDB RDS instances, ECS instances, and API calls in the last seven days. Security administrators can analyze the trend to check whether the number of audit events is at a normal level. Audit Risk Distribution This chart displays the percentage distribution of audit events at different risk levels in the last seven days. Risk levels are important, moderate, and low. Security administrators can analyze the trend to check whether the audit events are at acceptable risk levels. Security Issue Distribution This chart displays the percentage distribution of different event types in the last seven days. Security administrators can analyze this chart to check for the most frequent audit events and identify high-risk events to improve security protection. Log Size This chart displays the volume of online logs and offline logs. If these logs consume many storage resources, we recommend that you back up required audit logs and delete unnecessary logs. Audit Log Size This chart displays the size of logs for each audit type. ter (SOC)
4. View the audit summary in a specific time range.
i. Specify End T ime as the end of the time range to query. ii. In Audit T ype, select the audit types to query. iii. Click View to view the audit summary in the last seven days before the specified end time.

##### 8.4.4.3 Query audit events

This topic describes how to query audit events. Context On the Audit Query tab, you can view the details of audit events, including the log creation time, audit type, audit object, action type, risk level, and log content. The system matches the logs that are collected by a security audit module with audit rules. If the log content matches the regular expression in an audit rule, an audit event is reported. For more information about audit rules, see Add an audit policy. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Audit Query tab.
3. On the Audit Query tab, configure query conditions to view audit events within the specified time
range. Basic query a. Configure Audit T ype, Audit T arget , Act ion T ype, Risk Level, and Not if y. b. Specify a time range to query. c. In the Full-T ext Search search box, enter a keyword. d. Click Search. Advanced query In addition to the basic query conditions, you can configure advanced query conditions. a. Configure basic query conditions. b. Click Advanced Search. ter (SOC) c. Below Filt er Condit ion, configure User, T arget , Act ion, Result , and Cause. d. Click Save.
4. Click Export to export the audit events.
Download the exported file for analysis. For more information, see Manage export tasks.

##### 8.4.4.4 View raw logs

This topic describes how to view raw audit logs. Context On the Raw Log tab, you can view the raw logs generated by a running audit object. Raw logs contain information that is required for debugging. Security administrators can use these raw logs to troubleshoot system failures. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Raw Log tab.
3. On the Raw Log tab, configure query conditions to view the log summary chart and raw logs
within a specific time range. i. Specify Audit T ype and Audit T arget . ii. Enter a keyword. iii. Specify a time range to query. iv. Click Search.
4. Click Export to export the data.
Download the exported file for analysis. For more information, see Manage export tasks.

##### 8.4.4.5 Manage log sources

This topic describes how to view and manage log sources. Context You can view the number of log entries by log type or log source. You can also specify whether to display logs. The Log Types sub-tab provides the number of all log entries for a specific audit object of a specific device instance. The Log Sources sub-tab provides the number of log entries for all audit objects of a specific device instance. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Log Sources tab.
3. Click the Log T ypes tab and view the number of log entries for each audit object.
ter (SOC) You can view the number of log entries that are recorded on the current day and the number of log entries that are recorded during the last 30 days for each audit object. If you do not want to display the log entries for an audit object, perform the following steps: i. Find the audit object and click Hide in the Act ions column. ii. In the Note message, click Conf irm. Not e The process that is used to display the log entries for an audit object is similar to the process that is used to hide the log entries.
4. Click the Log Sources sub-tab and view the number of log entries for each device instance.
You can view the number of log entries that are recorded on the current day and the number of log entries that are recorded during the last 30 days for each device instance. If you do not want to display the log entries for an audit object from a specific device instance, perform the following steps: i. Find the device instance and click Hide in the Act ions column. ii. In the Note message, click Conf irm. Not e The process that is used to display the log entries for an audit object is similar to the process that is used to hide the log entries.

##### 8.4.4.6 Policy settings

###### 8.4.4.6.1 Manage audit rules

This topic describes how to create, modify, or delete an audit rule. Context If a log entry matches an audit rule, an audit event is reported. You can specify regular expressions in an audit rule to match log entries. A regular expression defines a matching pattern for character strings and can be used to check whether a string contains a specific substring. The following table provides examples about the pattern.

| Regular expression | Description |
|---|---|
| ^\d{5,12}$ | Matches the consecutive numbers from the fifth number to the twelfth number. |
| load file\( _ | Matches the "load file(" string. _ |

The security audit module defines the default audit rule based on the string that is generated in the log. This applies when an audit event is reported. The security administrator can also customize audit rules based on the string that is generated in the log. This applies when the system encounters an attack. ter (SOC)
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Policies tab.
3. On the Policies tab, click the Audit Rules sub-tab.
4. Create an audit rule.
i. Click New in the upper-right corner. ii. In the Add Policy dialog box, configure parameters. iii. Click Add. The system sends an alert email to the specified alert recipient after you create an audit rule. This applies if one string in an audit log of the specified audit type, audit object, or risk level matches the regular expression of the audit rule.
5. Manage audit rules.
You can create, query, disable, enable, and delete audit rules. Query audit rules Specify Audit T ype and Audit T arget . Enter a keyword in the search box and click Search. ter (SOC) Disable an audit rule Find the audit rule that you want to disable and click Disable in the Act ions column. Enable an audit rule Find the audit rule that has been disabled and click Enable in the Act ions column. Delete an audit rule Find the audit rule that you want to delete and click Delet e in the Act ions column. Not e You can delete only custom rules.

###### 8.4.4.6.2 Configure alert recipients

This topic describes how to configure the recipients of alerts on audit events. Context You can add an alert recipient by entering an email address that can be used to receive alerts on audit events. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Policies tab.
3. On the Policies tab, click the Alert Set t ings sub-tab.
4. Create an alert recipient.
i. Click New. ii. In the Add Alert Recipient dialog box, configure parameters. iii. Click Conf irm. ter (SOC)
5. Manage alert recipients.
Search for alert recipients Specify Audit T ype, Audit T arget , and Risk Level, enter the keyword of the email address, and then click Search. Delete alert recipients Find the email address that you want to delete and click Delet e in the Actions column.

###### 8.4.4.6.3 Manage archives of events and logs

This topic describes how to query and download the archives of audit events and raw logs. Context You can download the archives of events and logs to analyze audit events. This ensures the security of the Apsara Stack environment. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Policies tab.
3. On the Policies tab, click the Archiving sub-tab.
4. Query the archives of events and logs.
i. Specify Audit T ype and Archiving T ype. ii. Specify a time range to query. iii. Click Search.
5. Find the file where the archive information is stored and click Download in the Act ions column to
save the archive file to your on-premises machine.

###### 8.4.4.6.4 Manage export tasks

This topic describes how to download or delete exported audit events and logs. Context You can export audit events or logs on the Audit Query or Raw Log tab of the Security Audit page. After you export audit events or logs, you can manage the export tasks on the Exporting sub-tab. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Policies tab.
3. On the Policies tab, click the Export ing sub-tab.
4. View the created export tasks.
ter (SOC)
5. Click Download to download audit events or logs to your on-premises server.
6. Click Delet e to delete the export task.

###### 8.4.4.6.5 Modify system settings

This topic describes how to configure system parameters for security audit. Context You can configure system parameters to specify the maximum number of system alerts per day and the maximum number of audits per day for raw logs. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Log Analysis >
Securit y Audit . On the page that appears, click the Policies tab.
3. On the Policies tab, click the Syst em Set t ings sub-tab.
4. Find the configuration item that you want to modify and click Edit in the Act ions column.
5. Enter a required value in the Value column and click Conf irm in the Actions column.

### 8.5 Rules

#### 8.5.1 Create an IPS rule for traffic monitoring

This topic describes how to create an intrusion prevention system (IPS) rule for traffic monitoring in Cloud Firewall. Cloud Firewall has built-in IPS rules. This topic describes how to customize IPS rules based on your business requirements and network environment. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Rules.
3. On the Rules page, click the Cloud Firewall IPS Rules tab.
4. Click Creat e Rule.
5. In the Creat e Rule panel, configure parameters.
ter (SOC)

| Parameter | Description |
|---|---|
| Rule Name | The name of the IPS rule. We recommend that you enter an informative name for easy management. |
| Rules Engine | The rules engine that you want to use. Valid values: Basic Policies and Virt ual Pat ches. |
| At t ack T ype | The type of attack to be detected by the rule. |
| Severit y | The level of the severity. Valid values: Low, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability to be listed in the rule. Not e CVE provides a list of the public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Applicat ion | The name of the attacked application. |
| Rule Mode | The mode of the rule. Valid values: Packet and T raf f ic. |
| Direct ion | The direction of traffic to be monitored by the rule. Valid values: Inbound and Out bound, Inbound, and Out bound. |
| Rule Cont ent | The content of the rule, which must be specified by using the Snort syntax. Not e To prevent negative impact on your business, make sure that you enter valid content for the rule. |
| Rule Descript ion | The description of the rule. We recommend that you enter information such as the purpose or impact of the rule. |
| Descript ion | The remarks for the rule. We recommend that you enter information such as the purpose or impact of the rule. |

6. Click OK.

#### 8.5.2 Create IDS rules for traffic monitoring

This topic describes how to create intrusion detection system (IDS) rules for traffic monitoring. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Rules.
3. On the Rules page, click the T raf f ic Monit oring IDS Rules tab.
ter (SOC)
4. Click Creat e Rule.
5. In the Creat e Rule panel, configure the following parameters.

| Parameter | Description |
|---|---|
| Rule Name | The name of the IPS rule. We recommend that you enter a name that can help you identify and manage the IPS rule in an efficient manner. |
| Rules Engine | The rules engine that you want to use. Valid values: Basic Policies and Virt ual Pat ches. |
| At t ack T ype | The type of the attack that you want to detect by using the IPS rule |
| Severit y | The severity of the attack. Valid values: Low, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability that you want to add to the rule. Not e CVE provides a list of public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Applicat ion | The name of the attacked application. |
| Rule Mode | The mode of the IPS rule. Valid values: Packet and T raf f ic. |
| Direct ion | The direction of traffic that you want to monitor by using the IPS rule. Valid values: Inbound and Out bound, Inbound, and Out bound. |
| Rule Cont ent | The content of the IPS rule. You must use the Snort syntax to specify the content. Not e To prevent a negative impact on your business, make sure that the content you enter for the IPS rule is valid. |
| Rule Descript ion | The description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |
| Descript ion | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |

6. Click OK.

#### 8.5.3 Manage IDS rules for traffic monitoring

This topic describes how to view, enable, and disable intrusion detection system (IDS) rules for traffic monitoring. Context ter (SOC) On the T raf f ic Monit oring IDS Rules tab, you can view the built-in and custom IDS rules. It can also be used to enable or disable the rules based on your business requirements.
1. Log on to Apsara Stack Security Center.
2. In the upper-right corner of Apsara Stack Security Center, click Securit y. Choose Global Plat f orm
Securit y > Alibaba Cloud Securit y.
3. On the Rules page, click the T raf f ic Monit oring IDS Rules tab.
4. Manage IDS rules for traffic monitoring.
In the IDS rule list, you can view rule details, enable rules, and disable rules. View rule details Find the rule whose details you want to view and click Det ails in the Act ions column to view the rule details. Enable a rule Find the rule that you want to enable and turn on the switch in the Enable or not column to change the status of the rule from Disable to Enable. Disable a rule If a rule is not suitable for your business, you can disable the rule. Find the rule that you want to disable and turn off the switch in the Enable or not column to change the status of the rule from Enable to Disable.

#### 8.5.4 Specify custom thresholds for DDoS traffic scrubbing policies and traffic redirection

scrubbing policies and traffic redirection This topic describes how to specify custom thresholds for DDoS traffic scrubbing policies and traffic redirection. Default thresholds are provided. If you want to specify custom thresholds, perform the following steps: Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Rules.
3. Specify a custom threshold for a DDoS traffic scrubbing policy.
i. Click the AliGuard Rules tab to open the Scrubbing Policy tab. ii. Find the policy for which you want to specify a custom threshold and click Modif y T hreshold in the Act ions column. iii. In the Modif y T hreshold dialog box, enter a threshold value. iv. Click OK.
4. Specify a custom threshold for traffic redirection.
i. Click the AliGuard Rules tab and the Rerout e T hreshold tab. ii. Find a specific rule and click Modif y T hreshold in the Act ions column. iii. In the Modif y T hreshold dialog box, enter threshold values. ter (SOC) iv. Click OK.

#### 8.5.5 View Server Guard rules

This topic describes how to view the operations of Server Guard rules. You can view the list of vulnerabilities, baselines, and host exceptions. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Rules. On the
page that appears, click the Server Guard Rules tab.
3. In the overview section, you can view the total number of vulnerabilit y libraries, number of
baselines, and number of host except ions as well as the available engines.
4. View the vulnerability list.
i. Click the Vulnerabilit ies tab. ii. In the overview section, you can view the total number of Linux vulnerabilit ies, total number of Windows vulnerabilit ies, total number of Web-CMS vulnerabilit ies, and total number of urgent vulnerabilit ies. iii. Specify search conditions to view the vulnerabilities that meet the search conditions. Not e If you want to view all vulnerabilities, skip this step. In the vulnerability list, you can view the vulnerabilit y name, CVE ID, vulnerabilit y t ype, syst em, updat e t ime, and st at us.
5. View the baseline list.
i. Click the Baselines tab. ii. In the overview section, you can view the numbers of baseline types and check items. iii. Specify search conditions to view the baselines that meet the search conditions Not e If you want to view all baselines, skip this step. In the baseline list, you can view the baseline t ype, check it em cat egory, check it em name, risk level, updat e t ime, and st at us.
6. View the host exception list.
i. Click the Server Except ions tab. ii. In the overview section, you can view the number of rule alert subcat egories, number of webshells, and number of malicious viruses. iii. Specify search conditions to view the host exceptions that meet the search conditions. Not e If you want to view all exceptions, skip this step. In the host exception list, you can view the subcat egory name, rule cat egory, risk level, updat e t ime, source, and st at us. ter (SOC)

### 8.6 Threat intelligence

#### 8.6.1 Enable the service configuration feature

The threat intelligence module integrates threat monitoring and big data analysis. This can be used to obtain the latest information about developments in the threat intelligence field. After you enable the service configuration feature, the system starts to monitor and collect threat intelligence. This topic describes how to enable the service configuration feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > T hreat
Int elligence > Service Conf igurat ion .
3. On the Service Conf igurat ion page, view the data types and descriptions on the Situation
Awareness and Web application firewall tabs.
4. Click the tab where you want to enable threat monitoring and turn on Act ivat ion st at us.
After you turn on Act ivat ion st at us, the system starts to monitor and collect threat intelligence for the data types listed on the tab. What's next After you enable the service configuration feature, choose Securit y Operat ions Cent er (SOC) > T hreat Int elligence. On the Overview page, you can view the overall situation and statistics of threats during the last 30 days. For more information, see View the Overview page.

#### 8.6.2 View the Overview page

The Overview page displays the overall situation and statistics of threats to your assets over the last 30 days. Prerequisites The service conf igurat ion feature is enabled. For more information, see Enable the service configuration feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > T hreat
Int elligence > Overview.
3. On the Overview page, view the statistics and threats that are detected on Apsara Stack services
by the threat intelligence module. On the Overview page, you can perform the following operations: View T ot al malicious met ric int elligence In the T ot al malicious met ric int elligence section of the Overview page, view the information about the detected threats on Apsara Stack services. The information includes the number of malicious IP addresses, malicious domain names, and malicious URLs. ter (SOC) View T hreat t rends in t he last 30 days Search for an IP address to check whether the IP address is malicious. Enter the IP address that you want to check in the search box in the upper-right corner of the IP Report page and click the icon. To view the details of the IP address, choose Securit y Operat ions Cent er (SOC) > T hreat Int elligence > IP Address Search. On the page that appears, click the IP Report tab. For more information, see Search for an IP address. View T op 10 act ive IP malicious addresses In the T op 10 act ive IP malicious addresses section of the Overview page, view the information about the top 10 malicious IP addresses. The information includes IP address, First malicious observat ion, Last malicious observat ion, and Malicious label.

#### 8.6.3 Search for and view the information about a suspicious or malicious IP address

a suspicious or malicious IP address The threat intelligence module allows you to search for threat intelligence. This module helps you handle suspicious or malicious IP addresses at the earliest opportunity. Prerequisites The service conf igurat ion feature is enabled. For more information, see Enable the service configuration feature. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > T hreat
Int elligence > IP Address Search.
3. In the search box on the Search page, enter the suspicious or malicious IP address that you want
to query and click the icon.
4. On the IP Report page, view T hreat Level, Basic Inf ormat ion, T hreat Overview, IP Det ails,
and At t ack Risk Level Analysis of the IP address. You can view the following information on the IP Report page: T hreat Level: View the threat level of the suspicious or malicious IP address. The threat intelligence module classifies IP addresses into three threat levels. The levels are normal, suspicious, and high-risk. If the IP address is identified as high-risk, we recommend that you handle the IP address at the earliest opportunity. Basic Inf ormat ion: View the basic information about the suspicious or malicious IP address. The basic information includes the server in a data center, Abstract Syntax Notation One (ASN.1), country and city to which the IP address belongs, and the number of domain names for the IP address. View the statistics of the suspicious or malicious IP address. You can view T hreat Overview, IP Det ails, and T hreat Det ails of the IP address. ter (SOC) The T hreat Overview tab displays T op 5 At t ack Pref erence, At t ack Number, and At t ack Level Analysis of the IP address. The IP Det ails tab displays WHOIS and IP reverse check inf ormat ion of the IP address. The T hreat Det ails tab displays the t hreat t ag list of the IP address. The list contains specific information. The information includes the intelligence source, time when the IP address is detected for the first time, time when the IP address is active for the last time, and threat tag.

### 8.7 Create a report task

This topic describes how to create a report task. After you create a report task, the system sends reports on a regular basis. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Report
Management .
3. On the Report Management page, click Creat e Report .
4. In the Creat e Report dialog box, configure parameters.

| Parameter | Description |
|---|---|
| Report Name | The name of the report task. We recommend that you enter information such as the report purpose for easier identification and management. |
| Task Type | The type of the task. Valid values: Daily Report , Weekly Report , and Mont hly Report . |
| Department | The department related to the report. |

| Guide·Security Operations | Cen Apsara Stack Securit |
|---|---|

ter (SOC)

| Parameter | Description |
|---|---|
| Email Box | The email address of the report recipient. If you enter more than one email address, separate the email addresses with commas (,). |

5. Click Conf irm.
Result In the report task list, you can view, edit, and delete the newly created report tasks.

### 8.8 System Configurations

#### 8.8.1 View and manage metrics

Apsara Stack Security Center allows you to monitor security services. This helps find performance bottlenecks at the earliest opportunity. Then, you can scale out, scale up, or downgrade services to prevent system failures. This topic describes how to view the information about security services in Apsara Stack Security Center and how to manage metrics. View information about overall system monitoring
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Securit y Monit oring.
3. On the Overall Syst em Monit oring tab, view the overall information about security services in
Apsara Stack Security Center and the list of monitored security services. In the upper-left corner of the Overall Syst em Monit oring tab, you can view the overall information about security services. Services: the total number of security services monitored in Apsara Stack Security Center. Monit oring It ems: the total number of metrics. Abnormal It ems: the number of metrics whose status is abnormal. In the list of monitored security services, you can view the following information. ter (SOC)

| Parameter | Description |
|---|---|
| Services | The security service monitored in Apsara Stack Security Center. |
| Met rics | The monitoring indicator for the monitored security service. |
| Descript ion | The description of the monitoring indicator. |
| Monit oring It ems | The total number of metrics that belong to the monitoring indicator. |
| Abnormal It ems | The number of metrics whose status is abnormal, and the number of metrics at each urgency level. The urgency levels are indicated by different colors. The red color indicates a critical exception, the orange color indicates an important exception, and the blue color indicates a moderate exception. |
| St at e | The status of the monitoring indicator. |

4. Click Det ails in the Act ions column of a monitoring indicator. In the Monit oring det ails panel,
view the details of metrics that belong to the monitoring indicator. In the upper-left corner of the Monit oring det ails panel, you can view the overall information about the metrics. T ot al Monit oring It ems: the total number of metrics that belong to the monitoring indicator. Normal It ems: the number of metrics in the normal state. Abnormal It ems: the number of metrics in the abnormal state. In the metric list, you can view the following information.

| Parameter | Description |
|---|---|
| Monit oring It ems | The name of the metric. |

| Guide·Security Operations | Cen Apsara Stack Securit |
|---|---|

ter (SOC)

| Parameter | Description |
|---|---|
| Adjust Alert T hreshold | The threshold for the metric. If the value of the metric reaches the threshold and lasts for the specified period of time, the status of the metric becomes abnormal. |
| Durat ion | The period of time. If the value of the metric reaches the threshold and lasts for the specified period of time, the status of the metric becomes abnormal. |
| Monit oring Level | The urgency level displayed when the status of the metric becomes abnormal. |
| St at us | The status of the metric. |
| Alert Not if icat ions | The switch of the alert notification feature. You can turn on or off the switch in the Alert Not if icat ions column based on your business requirements. If the icon appears in the Alert Notifications column, a notification is sent when the status of the metric becomes abnormal. |

Manage metrics
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Securit y Monit oring.
3. On the Overall Syst em Monit oring tab, find a monitoring indicator and click Det ails in the
Act ions column.
4. In the Monit oring det ails panel, find a metric and click Modif y T hreshold, Handle, or Adjust
Alert Durat ion in the Act ions column to manage the metric. You can perform the following operations on the metric: Modif y T hreshold: In the Modif y T hreshold dialog box, modify the threshold and click OK. After the threshold is modified, an alert is generated when the value of the metric reaches the new threshold. Handle: You can configure the status of the metric based on your business requirements. If you do not want to handle the alert generated from the metric, select Ignore from the drop-down list. The status of the metric becomes Ignored. After you handle the alert generated from the metric, select Handled from the drop-down list. The status of the metric becomes handled. ter (SOC) Adjust Alert Durat ion: In the Adjust Alert Durat ion dialog box, modify the period of time and click OK. When the value of the metric reaches the threshold and lasts for the specified period of time, the status of the metric becomes abnormal.

#### 8.8.2 Alert settings

##### 8.8.2.1 Configure alert contacts

This topic describes how to configure and manage alert contacts. Context Apsara Stack Security sends alert notifications to alert contacts by text message, email, or DingTalk. When the detected information matches an alert rule, Apsara Stack Security sends an alert notification to the alert contacts. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Alert Set t ings. On the page that appears, click the Alert Recipient tab.
3. Click Add Recipient .
4. Enter the contact information and click OK.
5. Manage alert contacts.
In the contact list, find a contact and click Edit in the Actions column to edit the contact information.

##### 8.8.2.2 Configure alert notifications

This topic describes how to configure the alert notification method for security events on tenants or platforms. Context In the Alert s section, security administrators can configure the alert notification method for security ter (SOC) events. When a security event occurs, the system notifies the alert contacts by email, text message, or DingTalk. For more information about how to configure alert contacts, see Set alert recipients. Alerts on tenants
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Alert Set t ings. On the page that appears, click the T enant Alert s tab.
3. In the Alert s section, select notification methods for each security event.
4. Click Conf irm.
Alerts on the platform
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Alert Set t ings. On the page that appears, click the Plat f orm Alert s tab.
3. In the Alert s section, select notification methods for each security event.
4. Click Conf irm.

#### 8.8.3 Updates

##### 8.8.3.1 Overview of the system updates feature

The system updates feature allows you to manually or automatically update the Apsara Stack Security and rule libraries for up-to-date protection. The supported package import method depends on the Apsara Stack network environment. If Apsara Stack is connected to the Internet, you can choose Aut omat ically Download Updat e Packages. If Apsara Stack is not connected to the Internet, you can choose Manually Import Updat e Packages. The following table lists the update statuses of a rule library. Update statuses of a rule library ter (SOC)

| Status | Description |
|---|---|
| To Be Updated | Indicates that a new version of the rule library is available for update. |
| Updating | Indicates that the rule library is being downloaded from Alibaba Cloud for update. |
| Updated | Indicates that the rule library has been updated. |
| Update Failed | Indicates that the rule library failed to be updated. |

##### 8.8.3.2 Enable automatic update check and update rule libraries

libraries This topic describes how to enable automatic download of update packages and update rule libraries. Context If the Apsara Stack environment can connect to the Internet, you can enable automatic download of update packages to update the rule libraries. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Updat es.
3. Turn on Aut o Updat e Conf igurat ion to enable automatic download of update packages.
After this switch is turned on, the system automatically downloads update packages on a regular basis.
4. Update a rule library.
You can update one or more rule libraries at a time. Update multiple rule libraries at a time Click Bat ch Updat e in the upper-right corner to update all rule libraries. Update a single rule library a. Click the tab of the rule type that you want to update. For example, click Server Securit y. b. In the Act ions column, click Updat e.

##### 8.8.3.3 Manually import an update package and update your service

your service This topic describes how to manually import an update package and update your service. Prerequisites The security administrator has obtained the offline update package. ter (SOC) Context If the Apsara Stack environment cannot connect to the Internet, you can update a rule library after you import an offline update package. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Updat es.
3. Manually import an update package.
i. Click Import Updat e Package next to Manual Updat e in the upper-left corner. ii. In the Import Updat e Package dialog box, click Browse to select an offline update package that is downloaded to your on-premises server. iii. Click Conf irm.
4. Update a rule library.
You can update one or more rule libraries at a time. Update multiple rule libraries at a time Click Bat ch Updat e in the upper-right corner to update all rule libraries. Update a single rule library a. Click the tab of the rule type that you want to update. For example, click Server Securit y. b. Click Updat e in the Act ions column.

##### 8.8.3.4 Roll back a rule library

This topic describes how to roll a rule library back to a previous version. Context If an error occurs with an updated rule library, you can roll the library back to a previous version to avoid service interruption. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Updat es.
3. Click the tab of the rule library that you want to roll back. Example: Server Securit y
4. In the Actions column for the rule library, choose More > Roll Back.
5. In the Version Rollback dialog box, click Conf irm.

##### 8.8.3.5 View the update history of a rule library

This topic describes how to view the update history of a rule library. Context ter (SOC) You can view the update history of a rule library. If an error occurs with the latest version, you can locate the issue and roll back the rule library to an earlier version.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Updat es.
3. Click the tab of the specific rule library. Example: Server Securit y.
4. In the Act ions column of a rule library, click Hist ory.
On the Previous Updat es page, you can view the update history of the rule library. Click Det ails to view the details of an update package.

#### 8.8.4 Global configuration

##### 8.8.4.1 Set CIDR blocks for traffic monitoring

###### 8.8.4.1.1 Add a CIDR block for traffic monitoring

This topic describes how to add a Classless Inter-Domain Routing (CIDR) block for traffic monitoring. Network Traffic Monitoring System of Apsara Stack Security monitors the traffic of a specific CIDR block. Context CIDR blocks are configured for Network Traffic Monitoring System. Security administrators can change the CIDR blocks for monitoring based on business requirements. The settings of CIDR blocks apply only to a data center that is deployed in the region to which the specific CIDR block belongs. Not e Changes to CIDR block settings immediately take effect without the intervention of security administrators. If you add the same CIDR block on the traffic collection CIDR block setting page and region setting page, make sure that you select the same region on both pages. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the T raf f ic Collect ion IP Range tab.
3. Click Add.
4. In the Add CIDR Block f or Monit oring dialog box, configure parameters.
ter (SOC) CIDR Block: Enter a CIDR block for traffic monitoring. Not e Take note that the CIDR block that you entered must be valid and unique. Region: Select the region of the data center.
5. Click Conf irm.

###### 8.8.4.1.2 Manage CIDR blocks for traffic monitoring

This topic describes how to modify or delete Classless Inter-Domain Routing (CIDR) blocks for traffic monitoring. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the T raf f ic Collect ion IP Range tab.
3. Select a region, enter the CIDR block that you want to query, and then click Search.
View the information about the CIDR block for traffic monitoring and the region in the search result.
4. In the Act ions column, manage a CIDR block for traffic monitoring.
Modify the CIDR block for traffic monitoring Click Modif y to modify the region of the CIDR block for traffic monitoring. Delete the CIDR block for traffic monitoring Click Delet e to delete the CIDR block for traffic monitoring.

##### 8.8.4.2 Region settings

###### 8.8.4.2.1 Add a CIDR block for a region

This topic describes how to add Classless Inter-Domain Routing (CIDR) blocks for regions that are detected and reported by using Server Guard. Context ter (SOC) Region settings are used for region detection of the Server Guard agent. Server Guard servers automatically detect and match the regions of servers based on the IP address information that is reported by the Server Guard agent. Not e You can change the region of a CIDR block. After the region is modified, you must also modify the region for all assets in the CIDR block on the Asset Overview page. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the Region tab.
3. Click Add.
4. In the Add CIDR Block dialog box, configure parameters.
CIDR Block: Enter a CIDR block for the region. Not e Enter a valid CIDR block. You cannot enter a CIDR block that has been configured for the region. Region: Select a region.
5. Click Conf irm.

###### 8.8.4.2.2 Manage CIDR blocks for a region

This topic describes how to modify or delete Classless Inter-Domain Routing (CIDR) blocks for a region. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the Region tab.
3. Select a region, enter the CIDR block that you want to modify or delete, and then click Search.
You can view the information about the CIDR block for the region in the search result.
4. In the Act ions column, click Modify or Delete to manage the CIDR block for the region.
Modify the CIDR block for the region ter (SOC) Click Modif y to modify the CIDR block for the region. Delete the CIDR block for the region Click Delet e to delete the CIDR block for the region.

##### 8.8.4.3 Configure whitelists

This topic describes how to configure the whitelist for the feature that blocks brute-force attacks in Server Guard and the following whitelists in Threat Detection Service (TDS). The whitelists contain IP addresses allowed by server brute-force attack blocking, IP addresses allowed by application attack blocking, and IP addresses allowed by web attack blocking. Context If a normal request is regarded as an attack by the attack blocking feature of TDS or the unusual logon detection feature of Server Guard, you can add the source IP address of the request to a whitelist to avoid further false positives. Not e Make sure that the IP addresses in the whitelist are trusted. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the Whit elist tab.
3. Click Add.
4. In the Add t o Whit elist dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| Source IP | Enter a source IP address or Classless Inter-Domain Routing (CIDR) block. |
| Username | Enter the name of the user who creates the whitelist. |

|   | ter (SOC |
|---|---|
| Parameter | Description |
| Type | Brut e-Force At t ack Blocking Whit elist : Server Guard does not generate alerts for brute-force attacks or unusual logons from the IP addresses that are contained in this whitelist. BWAF Whit elist : The attack blocking feature does not generate alerts for the web attacks from the IP addresses that are contained in this whitelist. Servers wit h Brut e-Force At t ack Permissions: The attack blocking feature does not generate alerts for the brute-force attacks from the IP addresses that are contained in this whitelist. IPs wit h Applicat ion At t ack Permissions: The traffic from the IP addresses in this whitelist is not detected as suspicious application attack traffic. |

5. Click OK.
If you want to delete an existing whitelist, click Delet e in the Actions column. In the Delet e Whit elist message, click Conf irm.

##### 8.8.4.4 Configure attack blocking policies

This topic describes how to enable web attack blocking and brute-force attack blocking. Context The attack blocking features protect your servers against web attacks and brute-force attacks. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings > Region.
3. Turn on or off the switches in the Actions column to enable or disable Web At t ack Blocking or
Brut e-Force At t ack Blocking. Not e In the Actions column, a red switch indicates a disabled feature and a green switch indicates an enabled feature. After you disable the blocking feature for an attack type, Apsara Stack Security Center generates only alerts for this type of attacks.

##### 8.8.4.5 Block IP addresses

ter (SOC) This topic describes how to manually block requests for a specific IP address with a few clicks.
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings.
3. On the Global Set t ings page, click the Block IP Addresses tab.
4. In the upper-right corner of the tab, click Add.
5. In the Add dialog box, configure parameters.

| Parameter | Description |
|---|---|
| IP protocol | Specify the protocol type. Valid values: IPv4 and IPv6. |
| Source IP | Enter the source IP address that you want to block. |
| Destination IP | Enter the destination IP address that you want to block. |
| Destination Port | Enter the destination port that is used with the specified destination IP address. |
| Blocking Duration | Select a time range during which you want to block requests. Valid values: 1 Day, 7 Days, and 30 Days. |
| Type | Select the blocking mode. Valid values: Whit elist and Blacklist . |
| Remarks | Enter the reason for blocking. |

6. Click Conf irm.
ter (SOC)

##### 8.8.4.6 Configure custom IP addresses and locations

###### 8.8.4.6.1 Add custom IP addresses and locations

This topic describes how to add custom IP addresses and locations. You can customize internal IP addresses based on your network plan. After you configure the internal IP addresses, IP addresses from the public address library do not match the addresses outside China. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the Cust om IP Locat ion tab.
3. Click Add.
If you want to add multiple IP addresses and locations at a time, click Bat ch Upload (.t xt ). This can be used to import multiple IP addresses and locations as a template.
4. In the Add dialog box, configure parameters.
5. Click OK.

###### 8.8.4.6.2 Manage custom IP addresses and locations

This topic describes how to modify and delete custom IP addresses and locations. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Global Set t ings. On the page that appears, click the Cust om IP Locat ion tab.
3. In the Act ions column, manage custom IP addresses and locations.
To modify a custom IP address and a location: Click Modif y. In the Modif y dialog box, modify the custom geographic location. To delete a custom IP address and a location: Click Delet e. In the Delet e message, click OK.

#### 8.8.5 System Monitoring

#### 8.8.6 Inspect services

This topic describes how to inspect services such as Cloud Firewall and Network Traffic Monitoring System in Apsara Stack Security Center. You can monitor the status and features of the services.
1. Log on to Apsara Stack Security Center.
ter (SOC)
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Syst em Monit oring.
3. In the Syst em Inspect ion section of the Net work Securit y tab, inspect the services in the
inspection list. To inspect a single service or multiple services at a time, perform the following operations: Inspect multiple services at a time: In the Syst em Inspect ion section, click One-click Inspect ion to inspect all services in the inspection list. Inspect a single service: In the Syst em Inspect ion section, click Inspect Now in the Act ions column of the service that you want to inspect. After the services are inspected, the status of the services changes to Complet e in the Inspect ion St at us column.
4. View the inspection results.
You can view the following information about a service: In the inspection list, view the service name, last inspection time, number of inspection items, number of inspection items whose status is normal, number of inspection items whose status is abnormal, and inspection status. Click Det ails in the Act ions column of a service. In the Inspect ion Result Det ails panel, view the number of inspection items whose status is normal, number of inspection items whose status is abnormal, and details of each item. Click Download in the Act ions column of a service. Download the inspection results to your computer as prompted for backup and reference.

#### 8.8.7 Remote operations

##### 8.8.7.1 Enable remote operations

This topic describes how to enable remote operations. Context The remot e operat ions feature provides remote security operations and rules operations. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Remot e O&M.
3. On the Remot e O&M page, turn on the switch to enable remote operations.
ter (SOC) Not e If the switch turns green, the feature is enabled.
4. Select the departments for which you want to enable remote operations.
i. Click Updat e to the right of Enabled Depart ment s. ii. In the Updat e Enabled Depart ment s dialog box, click the Depart ment drop-down list to select the departments for which you want to enable remote operations. iii. Click OK. Not e After you perform these operations, the security logs of departments specified by Enabled Depart ment s are encrypted and uploaded to Apsara Stack Security Center.
5. Select fields to encrypt and upload for remote operations.
If you select Required Nonsensit ive Fields, the system encrypts and uploads the data. If you select Available Fields and Masking, the system masks the data before it encrypts and uploads the data.

#### 8.8.8 Account management

##### 8.8.8.1 View and modify an Apsara Stack tenant account

This topic describes how to view and modify the information about your Apsara Stack tenant account that is bound to the system. Context ter (SOC) All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. You can modify the account information. Proceed with caution. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Account s. On the page that appears, click the Apsara St ack Account tab.
3. Modify the information about your Apsara Stack tenant account.
i. In the Actions column, click Modif y. ii. In the Change Account dialog box, modify the account information. iii. Click Conf irm.
4. View the details of your Apsara Stack tenant account.
Click Det ails to view the details of your Apsara Stack tenant account. ter (SOC)

##### 8.8.8.2 Add an Alibaba Cloud account

This topic describes how to add an Alibaba Cloud account in Apsara Stack Security Center. After you add the account, you can use features in a hybrid cloud. Context After you add an Alibaba Cloud account in Apsara Stack Security Center, you can manage the Anti- DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security Center. This way, you can use features in a hybrid cloud. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Securit y Operat ions Cent er (SOC) > Syst em
Conf igurat ions > Account s. On the page that appears, click the Public Cloud Account tab.
3. On the Feat ure Int egrat ion tab, click Add.
4. In the Add Account dialog box, enter the information about your Alibaba Cloud account and
select Alibaba Cloud services to use. ter (SOC) Enter the AccessKey ID and AccessKey secret of your Alibaba Cloud account. Select Alibaba Cloud services to use. Valid values: Ant i-DDoS Pro, Web Applicat ion Firewall, and both.
5. Click Conf irm.
Result After the account is added, it is displayed on the Public Cloud Account tab. To modify or delete the account, you can click Modif y or Delet e in the Actions column. ts

## 9 Optional security products

### 9.1 Anti-DDoS settings

#### 9.1.1 Overview

In Distributed Denial of Service (DDoS) attacks, attackers exploit the client-server model to combine multiple computers into a platform that can launch attacks on one or more targets. This greatly increases the threat of attacks. Common DDoS attack types include: Net work-layer at t acks: A typical example is UDP reflection attacks, such as NTP flood. These attacks use heavy traffic to congest the network of the victim, disabling proper responses to user requests. T ransport -layer at t acks: Typical examples include SYN flood and connection flood. These attacks consume a large number of connection resources of a server to cause denial of service. Session-layer at t acks: A typical example is SSL flood. These attacks consume the SSL session resources of a server to cause denial of service. Applicat ion-layer at t acks: Typical attack types include DNS flood, HTTP flood, and game zombie attacks. These attacks consume a large amount of application processing resources of a server to cause denial of service. Apsara Stack Security can redirect, scrub, and re-inject attack traffic to protect your server against DDoS attacks and ensure normal business operations. Not e Apsara Stack Security cannot scrub the traffic between internal networks.

#### 9.1.2 View and configure DDoS mitigation policies

policies This topic describes how to view and configure DDoS mitigation policies. Anti-DDoS provides default DDoS mitigation policies and DDoS traffic scrubbing policies. Context After an alert threshold of DDoS traffic for an IP address is set, an alert is triggered when traffic to the IP address reaches the threshold. The alert threshold for an IP address must be set based on the traffic volume. An abnormally large traffic volume may indicate DDoS attacks. We recommend that you set an alert threshold to a value slightly higher than the peak traffic volume. Apsara Stack Security supports a global alert threshold, alert threshold for a specific CIDR block, and alert threshold for an IP address. Global alert threshold: You cannot set a global alert threshold. It is automatically set when Apsara Stack Security is initialized. Alert threshold for a specific CIDR block: You can set an alert threshold for a specific CIDR block based on its traffic volume. CIDR block-specific alert thresholds allow you to control the traffic to each CIDR block. ts
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Net work Securit y > Policy Conf igurat ion > DDoS
Def ense Policy.
3. View and customize DDoS mitigation policies.

| Operation | Description |
|---|---|
| View the default policy | Move the pointer over the icon next to Built-in Default Policy in the preceding figure to view the default DDoS mitigation policy. |
| Customize a policy | Click View to view CIDR block-specific policies. Click +Add to customize a DDoS mitigation policy for a CIDR block. |

To customize a policy for a CIDR block, perform the following steps: i. Click +Add next to Cust om Mode. ii. In the Set T hresholds f or Alert s dialog box, configure the parameters.

| Parameter | Description |
|---|---|
| CIDR Block | The CIDR block for which the alert thresholds are used. |
| Bandwidth Threshold | The alert threshold for bandwidth usage in a data center. When the sum of inbound and outbound traffic reaches this threshold, DDoS detection is triggered. Set this parameter to a value slightly higher than the peak traffic volume. We recommend that you set the value to 100 or higher. Unit: Mbit/s. |
| Packets Threshold | The alert threshold for the packet rate in a data center. When the sum of inbound and outbound packet rates reaches this threshold, DDoS detection is triggered. Set this parameter to a value slightly higher than the peak packet rate. We recommend that you set the value to 20000 or higher. Unit: packets per second (PPS). |

iii. Click OK.
4. In the DDoS Scrubbing Def ense St rat egy section, click View to view DDoS traffic scrubbing
ts policies.

#### 9.1.3 View DDoS events

This topic describes how to view DDoS events. Context During or after traffic scrubbing, Apsara Stack Security reports security events to Apsara Stack Security Center. Procedure
1. Log on to Apsara Stack Security Center.
2. In the left-side navigation pane, choose Net work Securit y > Net work Prot ect ion.
3. View anti-DDoS statistics.
4. (Optional)In the DDoS Scrubbing List section, specify search conditions and click Search.
Not e If you need to view all traffic scrubbing events, skip this step. ts

| Search condition | Description |
|---|---|
| IP address | The IP address that was under a DDoS attack. |
| Trigger | The metric that exceeds the configured alert threshold in the DDoS attack traffic. |
| State | Scrubbing: indicates that traffic scrubbing is in progress. Scrubbing Complete: indicates that traffic scrubbing is complete. |
| Start time and End time | The start time and end time of DDoS traffic scrubbing. |

5. In the DDoS Scrubbing List section, view details about DDoS traffic scrubbing events.

### 9.2 Data Encryption Service

#### 9.2.1 Data Encryption Service overview

Data Encryption Service is an encryption solution in the cloud. The underlying layer of the service uses hardware cryptographic devices that are tested and certified by the Office of the State Commercial Cryptography Administration (OSCCA). The service uses virtualization technologies to help you meet compliance and regulatory requirements in data security. This helps ensure the confidentiality of business data in the cloud. Data Encryption Service allows you to manage keys in a secure and reliable manner and ensures reliable data encryption and decryption by using various encryption algorithms. The following figure shows the communication mode used by Data Encryption Service. Elastic Compute Service (ECS) instances and hardware security modules (HSMs) must be in the same virtual private cloud (VPC). Feat ures Data Encryption Service provides the following features: Key management: allows you to store and use keys in a secure manner, generate sub-keys by using multiple components, and import and export keys by using secure packets. Data encryption: supports all cryptographic algorithms that are approved for use in mainland China and some globally used algorithms. Message authentication code (MAC) calculation: supports multiple MAC algorithms that are defined in the China Financial Integrated Circuit (IC) Card Specifications. PBOC for short. Transaction authentication: verifies the authorization request cryptogram (ARQC) and generates the authorization response cryptogram (ARPC) based on PBOC 2.0 and 3.0. ts

#### 9.2.2 Management of Data Encryption Service instances

instances

##### 9.2.2.1 Create a Data Encryption Service instance

This topic describes how to create a Data Encryption Service instance. Context Before you can use Data Encryption Service, you must create an instance. Procedure
1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, choose Securit y > Dat a Encrypt ion Service. On the page that
appears, click Data Encryption Service.
3. On the Dat a Encrypt ion Service page, click Creat e Inst ance.
4. On the page that appears, specify Region, Net work T ype, Manuf act urer, and Device Model.
5. Click Creat e Inst ance.

##### 9.2.2.2 Configure a Data Encryption Service instance

This topic describes how to configure a Data Encryption Service instance. Context You can use a Data Encryption Service instance only in a virtual private cloud (VPC). After you create a Data Encryption Service instance, you must configure a VPC and a private IP address for the instance. Procedure
1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, choose Securit y > Dat a Encrypt ion Service. On the page that
appears, click Data Encryption Service.
3. On the Data Encryption Service page, find the instance that you create and click Conf igure in the
Operat ion column.
4. In the Conf igure IP dialog box, configure the following parameters.

| Parameter | Description |
|---|---|
| VPC network ID | Select a VPC. The instance and your Elastic Compute Service (ECS) instances must reside in the same VPC. |
| VPC subnet | Select a VPC subnet. |
| Allocate private IP address | Specify a private IP address. The private IP address must be within the CIDR block that is specified by VPC subnet . |

5. Click OK.
ts

##### 9.2.2.3 Release a Data Encryption Service instance

This topic describes how to release a Data Encryption Service instance. Context The number of Data Encryption Service instances that you can create in Data Encryption Service is limited. If you no longer need an instance, you can release the instance. Procedure
1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, choose Securit y > Dat a Encrypt ion Service. On the page that
appears, click Data Encryption Service.
3. On the Dat a Encrypt ion Service page, find the instance that you want to release and click
Release in the Operat ion column.
4. In the message that appears, click OK.
