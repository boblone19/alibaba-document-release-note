---
title: "Cloud Security Scanner Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 12
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Scanner Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%EF%BC%88%E9%BB%98%E5%AE%89%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Scanner%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Cloud Security Scanner Product Introduction 20260701

Cloud Security Scanner Product I ty Scanner?

## What is Cloud Security

**Scanner?**

Cloud Security Scanner is an intelligent security product that uses AI to help enterprises proactively identify security risks. It analyzes network environment exposures from the perspective of attackers and continuously discovers security vulnerabilities based on multidimensional assessments of vulnerability risks, high-risk services, and other security weaknesses. Cloud Security Scanner allows enterprises to efficiently respond to the latest security risks, achieve transparent asset control, comprehensively quantify asset security risks, and establish routine security operations.

| Primary feature | Secondary feature | Description |
|---|---|---|
| Today's overview | Today's overview | Supports asset scoring. Asset health is categorized as: High risk: 0-59 Medium risk: 60-69 Low (70–99) Health Supports statistics and visualization for website, host, and domain name assets. Supports statistics and visualization for security vulnerabilities, external exposures, and compliance vulnerabilities. Supports monitoring of asset and risk change trends over the last 7 days. From the perspective of risky assets, supports displaying the top 10 assets with the latest or highest risks. From the perspective of security vulnerabilities, external exposures, and compliance vulnerabilities, supports displaying the top 5 security risks by asset or group. |
|  | Asset analysis | Supports statistical visualization for website and host assets over the last 7, 30, and 90 days. The statistics cover dimensions such as total number of assets, changes in total assets, changes in risky assets, and asset update changes. Supports statistical visualization of the distribution of host port services and website asset status codes. Supports statistics and visualization for the top 5 in dimensions such as host ports, open host ports, vulnerable ports, host services, host asset device types, and operating systems. Supports statistics and visualization for the top 5 in dimensions such as website asset fingerprinting and domain name resolution. |

Cloud Security Scanner Product I

## Features

This topic describes the features of vulnerability scanning.

| Assets |  |  |
|---|---|---|
|  | Website assets | Supports collecting basic information about website assets, such as website addresses, titles, fingerprints, types, and services. It can parse asset IP addresses and status codes, and scan for and count security and compliance vulnerabilities. Displays website asset information in a list. The list includes basic information such as website address, title, fingerprint, type, and service. It also includes parsed information such as IP address, status code, asset group, owner, tags, remarks, source, changes, discovery time, update time, and latest scan time. You can customize the properties displayed in the asset list. Supports filtering and retrieving the asset list by dimensions such as risk level, asset changes, asset type, status code, asset group, owner, asset fingerprint, asset tag, VPC, asset source, WAF detection, asset update time, IP address, and associated domain name. Supports batch operations to change asset groups, owners, and tags. Also supports batch deletion of assets and exporting the asset list. |
|  | Host assets | Supports collecting basic information about host assets, such as host address, asset fingerprint, and liveness status. It can scan for and count security and compliance vulnerabilities. Displays host asset information in a list. The list includes host address, asset fingerprint, liveness status, vulnerability data, number of open ports, asset group, asset update time, owner, asset changes, asset tags, and device type. You can customize the properties displayed in the asset list. Supports filtering and retrieving the asset list by dimensions such as risk level, host service, asset changes, asset group, liveness status, asset fingerprint, VPC, asset tag, port, operating system, owner, asset source, CDN detection, device type, asset risk update time, IP address, and associated domain name. Supports batch operations to change asset groups, owners, and tags. Also supports batch deletion of assets and exporting the asset list. |
|  | Risk analysis | Supports statistical visualization of unfixed and fixed risks over the last 7, 30, and 90 days. Supports statistical visualization of the distribution of vulnerability types. Supports statistics and visualization for the top 5 in dimensions such as CMS application vulnerabilities, O&M security risks, high- risk website assets, high-risk host assets, and weak password risks. |

Cloud Security Scanner Product I

|  | Security vulnerabilities | Displays security vulnerability information in unfixed and fixed lists. The lists include risk name, risk address, detection status, processing status, and risk update time. You can customize the properties displayed in the security vulnerability list. Supports viewing detailed information about security vulnerabilities, including vulnerability level, overview, risk description, risk impact, risk details, remediation suggestions, and request and response information. Supports filtering and retrieving the vulnerability list by dimensions such as risk level, asset group, owner, asset tag, detection status, detection type, processing status, risk update time, risk discovery time, risk name, risk address, IP, and tag. Supports actions for security vulnerabilities such as confirming, ignoring, and re-detecting risks. Batch operations and one-click export of the security vulnerability list are also supported. |
|---|---|---|
| Risks |  |  |
|  | Compliance vulnerabilities | Displays compliance vulnerability information in unfixed and fixed lists. The lists include risk name, asset address, application/service, detection status, processing status, and risk update time. You can customize the properties displayed in the compliance vulnerability list. Supports viewing detailed information about compliance vulnerabilities, including an overview, risk description, remediation suggestions, and reference links. Supports filtering and retrieving the vulnerability list by dimensions such as risk level, asset group, owner, detection status, port, asset tag, risk discovery time, risk update time, processing status, and CVE/CNNVD/CNVD. Supports actions for compliance vulnerabilities such as confirming and ignoring risks. Batch operations and one-click export of the compliance vulnerability list are also supported. |
|  | External exposures | Displays information in unfixed and fixed lists, including risk name, risk address, detection status, processing status, risk update time, geographic location, and asset group. You can customize the properties displayed in the external exposure risk list. Supports viewing detailed information about exposure risks, including risk description, risk impact, risk details, and remediation suggestions. Supports filtering and retrieving the exposure list by dimensions such as risk level, asset group, owner, processing status, asset tag, risk discovery time, risk update time, and risk address/IP/tag. Supports actions for external exposure risks such as confirming and ignoring risks. Batch operations and one-click export of the exposure risk list are also supported. |

Cloud Security Scanner Product I

| Tasks | Task list | Displays task information for asset import, risk scan, and asset scan tasks in a list. The list includes task name, task type, asset information, execution mode, task status, creation time, and end time. You can customize the properties displayed in the task list. Supports viewing detailed information about asset discovery tasks, including task status, asset discovery template, task progress, and details of discovered assets. Supports viewing detailed information about risk scan tasks, including task status, risk scan template, task progress, and details of discovered risks. Supports filtering and retrieving the task list by dimensions such as task type, task status, task template, execution mode, creation time, end time, task name, and template name. Supports operations such as executing, stopping, deleting, and re-executing tasks. Batch operations are also supported. |
|---|---|---|
|  | Template list | Supports predefined default templates for risk scans and asset scans. You can also customize templates. Displays template information in a list, including template name, template type, creation time, and organization. Supports viewing and configuring the details of the default risk scan template. Details include template name, basic detection (CMS application vulnerabilities, weak password vulnerabilities, O&M security vulnerabilities, compliance vulnerabilities), web risk detection, user agent, and excluded ports. Supports viewing and configuring the details of the default asset scan template. Details include template name, stateless scanning, scan rate, response wait time, packet loss retransmission count, and virtual IP address (VIP) liveness detection. Supports filtering and retrieving the template list by dimensions such as template type, creation time, and template name. |
| Report list | Report list | Supports three report template types: risk assessment, asset statistics, and risk statistics. You can configure report template properties such as report name, asset scope, risk scope, vulnerability type, risk level, and cover logo. Displays report template information in a list, including report name, report type, time range, export format, creation time, and generation status. Supports filtering and retrieving the report template list by dimensions such as report type and creation time. Supports creating and deleting report templates. |

Cloud Security Scanner Product I

| Configuration management | Scan rules | Provides 86 scan metrics for CMS application vulnerabilities, covering mainstream application services such as Cisco, F5, Kibana, NGINX, SMTP, Spring, Spark, ThinkPHP, Tomcat, WebLogic, and WordPress. Provides 87 scan metrics for O&M security vulnerabilities, covering mainstream application services such as Cisco, DNS, Docker, F5, Git, Hadoop, IIS, JBoss, Jenkins, Kafka, Juniper, Microsoft Windows RDP, MySQL, NGINX, XAMPP, Tomcat, SVN, and Spring. Provides 24 scan metrics for weak passwords, including various weak password vulnerabilities such as MySQL weak passwords, MongoDB unauthorized access, and SSH weak passwords. You can customize these metrics and enable or disable the default weak password check. |
|---|---|---|
|  | Task management | Provides a centralized view of all task types, including information such as task name, task type, priority, and number of subtasks. |
|  | System info | Supports update records for the vulnerability database. |
|  | O&M detection | Supports using ping, curl, and telnet commands to test an IP address or domain name to verify if a vulnerability exists. |
|  | Log auditing | Supports log auditing for events such as system operations, scan task executions, and report exports. The audit log includes event description, log type, event IP, time of occurrence, and event result. You can retrieve and query audit logs based on time, IP, and event. You can also download audit log reports and clear audit logs. |
|  | Engine management | Provides a switch to automatically import assets from EIP and SLB instances. Supports adding and deleting scan engines. Displays engine information, number of engines, and engine status (running or abnormal). |

Cloud Security Scanner Product I

| Benefit | Description |
|---|---|
| Empower enterprises with transparent asset exposure management. | Cloud Security Scanner uses intelligent asset discovery technology to discover edge assets and unknown assets of an organization from the perspective of attackers. It uses a built-in fingerprint library to identify exposed assets from both attack and defense perspectives, enabling transparent attack exposure management. This allows enterprises to analyze their business health status from the perspective of attackers and proactively harden at-risk assets. |
| Helps enterprises shorten their response time to N-day vulnerabilities. | Cloud Security Scanner provides a comprehensive vulnerability response process, ensuring timely handling of N-day vulnerabilities. By aggregating asset risks and streamlining vulnerability retesting and remediation, it helps enterprises track the entire lifecycle of risk mitigation in real time. |
| Provides accurate and comprehensive security risk quantification. | Cloud Security Scanner analyzes network system vulnerabilities from the perspective of attackers and performs unified risk assessments across multiple dimensions. It correlates asset data, attributes, events, and vulnerability library information to identify exposed risks, and uses weighted scoring to quantify the risks. |
| Provides continuous asset inspection and discovery. | Cloud Security Scanner uses asset discovery and intelligent asset classification to actively probe unknown networks and passively monitor known networks. This enables continuous, automated asset discovery, including edge assets, helping enterprises quantify risks, visualize their assets, and establish routine security operations. Cloud Security Scanner also provides multi-dimensional views of asset topology, lifecycle, newly discovered assets, port updates, service changes, and other information. |

Cloud Security Scanner Product I

## Benefits

Cloud Security Scanner automates the O&M of Apsara Stack assets and risk management for enterprises. It automatically, quickly, and accurately discovers unknown assets based on known assets and detects vulnerabilities across all assets. It also comprehensively assesses the security posture of publicly exposed business, services, applications, and data. This provides enterprises with faster, more comprehensive, and more intelligent management of their Apsara Stack assets and asset security. Cloud Security Scanner Product I

## Scenarios

Cloud Security Scanner automates the O&M of IT assets and risk management for enterprises. It automatically, quickly, and accurately discovers unknown assets in enterprises based on their known assets and detects vulnerabilities across all assets. It also comprehensively assesses the security posture of publicly exposed business, services, applications, and data of enterprises and monitors the changes of their exposed services and assets in real time. This provides enterprises with faster, more comprehensive, and more intelligent management of their IT assets and asset security risks.

**Overall asset security construction**

Facilitate hierarchical and categorized management of customer assets, enrich assessment metrics, improve security assessment mechanisms, strengthen the network security architecture both within and outside of Apsara Stack, and provide real-time monitoring and prevention of asset security risks.

**Routine risk monitoring**

Automate the monitoring of Apsara Stack asset risks, including automated asset detection, intelligent asset discovery, risk correlation analysis, and vulnerability retesting and verification. This enables 24/7 identification of assets and vulnerabilities visible on both internal and external networks, improving asset governance efficiency. Continuous vulnerability verification minimizes redundant alerts and ensures accuracy.

**Asset security and compliance operations**

Comply with Multi-Level Protection Scheme (MLPS) 2.0 specifications and meet classified protection requirements for network security. Provide technical security scanning and visualization tools to reduce information security risks, enhance security protection capabilities, and help enterprises fulfill their network information security responsibilities.
