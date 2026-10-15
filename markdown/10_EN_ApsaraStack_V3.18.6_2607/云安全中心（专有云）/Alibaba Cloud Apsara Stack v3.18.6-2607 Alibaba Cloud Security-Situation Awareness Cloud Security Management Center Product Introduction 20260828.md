---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 26
source_pdf: "dcec4a83029a9799_Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Ma"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E5%AE%89%E5%85%A8%E4%B8%AD%E5%BF%83%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Product Introduction 20260828

## Table of Contents

- 1 What is SOC?
- 2 Benefits
- 3 Service architecture
- 4 Features
- 5 Common scenarios

OC?

## 1 What is SOC?

Apsara Stack Security Security Operations Center (SOC) is a native and integrated security management center that is developed by Alibaba Cloud to manage the overall security operations of Alibaba Cloud hybrid cloud and Apsara Stack. You can use SOC to build a closed-loop security operations system that supports risk prediction, risk identification, defense control, detection and analysis, and response management in the cloud. SOC provides security capabilities to support the security operations of Alibaba Cloud hybrid cloud and Apsara Stack, such as high-risk threat detection, in-depth tracing and evidence collection, comprehensive security assessment, visualized monitoring, automatic response and handling, cloud asset management, and scenario-based operations.

## 2 Benefits

This topic describes the benefits of Security Operations Center (SOC).

**Full data collection to monitor the entire cloud environment**

SOC uses multiple methods to collect data from Apsara Stack Security network elements and third-party security network elements for the operations center, threat monitoring, and risk analysis modules. This way, you can view security risks in your assets from multiple dimensions.

**Comprehensive association analysis to prevent information**

**silos**

SOC uses association analysis methods based on retrieval and aggregation, attack scenarios, attack inference, threat intelligence management, and business scenarios to filter, merge, refine, and correlate risk information. This simplifies security analysis, mitigates the impact of differences in analysis methods, logic, and experience on the effectiveness of security risk identification, and thereby improves the efficiency of cloud security operations.

**Cloud-native security operations center that monitors cloud**

**assets**

SOC creates the profiles of risks on cloud servers and virtual instances, and assesses asset security in a comprehensive manner. Risks are profiled from multiple dimensions, such as security vulnerabilities, Internet exposure, security baseline risks, cyberattacks, asset behavior, and abnormal behavior.

**SOAR for overall security operations**

SOC is integrated with the capabilities of Security Orchestration Automation Response (SOAR). In SOC, human resources, processes, and technologies are combined to improve the efficiency of security operations. When you receive an alert, you can deliver related policies with a few clicks to handle security risks in an efficient manner. rchitecture

## 3 Service architecture

Security Operations Center (SOC) uses a hierarchical architecture that consists of the following layers: data collection, data processing, data analysis, data storage, and data consumption. This facilitates stream processing from the acquisition of raw data to data application. This topic describes the architecture of SOC.

| Operations |   |
|---|---|
| Ce Routine | nter Security |
| ioOpneration Real-ti | sInspectio me ... |

| Threat |   |
|---|---|
| Monit Global | oring Asset |
| Situation Threat | Situation ... |

| Risk |   |
|---|---|
| Ana Threat | lysis Vulnerabi |
| Events Attack | Analysi ... |

| Asset |   |
|---|---|
| Mana Platform | gement Tenant |
| Assets Risk | Assets ... |

| Log |   |
|---|---|
| Manag Log | ement Log |
| Statistics Log | Ingestion Log |

| Data Reports Report Report Tasks Export Report ... | Rule Management Analysis Blocking Rules Rules Alert ... |
|---|---|

**Data**

**Consumption**

Confrontation Situation Profiles Query Forwarding Customization Rules Surface Assessment Association Graph Risk Computing Analysis Identification Hot Data Cold Data

**Data**

**Data**

**Analysis**

**Storage**

Behavior Machine Data Learning Modeling Analysis MetaQ ApsaraDB SLS RDS

**Data**

Data Data Data Data Data Data

**Processing**

Splitting Filtering Parsing Standardization Merging Labeling Operation Network Threat Other

**Data**

System Threat Threat Asset

**Collection**

Logs Logs Logs Logs Intelligence Vulnerabilities Information Data MetaQ SLS ApsaraDB Syslog APIs SLS RDS Apsara Stack Security Network Elements Third-party Security Network

**Data collection layer**

The data collection layer collects raw logs or alert data. Raw logs and security alert data from Apsara Stack Security network elements such as Server Guard, Cloud Firewall, Web Application Firewall (WAF), and Network Detection and Response (NDR) are collected over data tunnels such as MetaQ, Simple Log Service (SLS), ApsaraDB RDS, and APIs. Raw data from third-party security network elements is collected over syslog and SLS.

**Data processing layer**

The data processing layer preprocesses the collected raw data in a centralized manner. The preprocessing includes array splitting, invalid data filtering, data format parsing, mapping of standard fields, data deduplication, data merging, and data labeling. After raw data is standardized, the data can be further processed by using other logic such as big data mining, analysis, and storage.

**Data analysis layer**

The data analysis layer focuses on the analytical processing of preprocessed real-time streaming data and non-real-time offline data. Real-time streaming data is synchronized to the Dipper streaming data analysis engine by using MetaQ message queues to complete machine learning, data modeling, and behavior analysis for data standardization. Non-realtime offline data is processed by using scheduled tasks that use security analysis models to conduct graph computing, association analysis, and risk identification.

**Data storage layer**

The data storage layer is used for the distributed storage of standardized data and data analysis results. Standardized data is stored as hot data in SLS, which facilitates data consumption such as statistical analysis, data query, and data mining. New results from streaming and offline data analysis, and asset information, are stored as cold data in ApsaraDB RDS. Data analysis results are displayed in the data consumption layer. rchitecture

**Data consumption layer**

The data consumption layer is used for the application and consumption of analyzed and processed data. This layer directly delivers data services to cloud security operations administrators. The data services include scenario-based security operations, cloud security threat monitoring, network risk analysis, orchestration of risk responses, cloud asset management, log management, and data reports. These data services help security operations administrators perform comprehensive security operations in cloud environments.

## 4 Features

This topic describes the features supported by the Cloud Security Management Center.

| Top-level feature | Second- level feature | Description |
|---|---|---|
| Security posture monitorin g | Security posture monitorin g | Monitor security posture from three perspectives: overall security posture, asset risk posture, and threat risk posture. Supports high-resolution large- screen display. |
|   |   | Overall security posture includes metrics such as the number of organizations, risk index, index trend, top five risky organizations, total number of assets, asset protection rate, distribution of risky assets, statistics and distribution of threat events, and geographic distribution of external attack sources. |
|   |   | Asset risk posture includes metrics such as the distribution of asset risk levels, trend of asset risk changes, top five security vulnerability risks, top five security baseline risks, and top five risky assets. You can drill down into details for security vulnerability risks, security baseline risks, and risky assets. |
|   |   | Threat risk posture includes metrics such as the distribution of threat event severity, trend of threat event changes, distribution of threat types, ATT&CK attack behaviors, distribution of attack phases, and top ten threat events. |
|   |   | Export a security posture snapshot with one click. |
|   |   | Display security posture. Supports high-resolution large-screen display. |
| Operation s Hub | Operation s Hub | Track security alerts by total count, closure rate, action distribution, risk level, data source, alert type distribution, top ten attack source IP addresses, top ten attacked IP addresses, and top five attacked websites. |
|   |   | Aggregate security alerts by time, source IP, destination IP, alert name, alert type, risk level, data source, and organization. Display results in an aggregated list. View detailed evidence for each alert. |
|   |   | Respond to security alerts using the Alibaba Cloud Security OpenAPI. |
|   |   | Filter security alerts by time range, data source, alert type, alert level, and organization. Save filters as quick search conditions. |
|   |   | Turn security alert statistics windows on or off. |

|   |   | Export security alert reports with one click. |
|---|---|---|
|   |   | Issue response tasks and create response policies with one click. |
|   |   | Import and display real-time threat alerts from third-party security products. |
|   | Threat events | View threat events across your cloud environment. Key information includes threat name, threat type, ATT&CK ID, threat description, remediation suggestions, network protocol, source and destination IP addresses and ports, matched threat intelligence, domain names, file names, and process information. |
|   |   | View evidence used to assess threat event risk. Map evidence to Kill Chain stages. Note Added timeline view for attack stages and evidence. |
|   |   | Visualize threat traceability analysis. Reconstruct the attack chain path. Customize and export the visualization layout. |
|   |   | Trace threats to internal and external hosts and cloud instances. View details for related hosts or cloud instances and their security alerts. Note Added statistics for malicious IPs, domain names, and file MD5 hashes that match threat intelligence. View related intelligence details. |
|   |   | Process threat events. Set status and add notes. Automatically analyze IP- based entities, entity sources, threat intelligence tags, and geolocations. Process entities by scenario, scope, and action validity period. |
|   |   | Link actions, issue response tasks, and create response policies with one click. Entities include IP addresses, files, and processes. Built-in response playbooks are available. |
|   |   | Get intelligent response recommendations. Best actions are generated based on risk and context for associated entities. |

|   |   | Convert threat events into response cases. Import related threat information into the Response Orchestration Center. |
|---|---|---|
|   |   | Filter threat events by time range, source or destination IP, severity, threat type, attack phase, threat name, whether threat intelligence matched, and processing status. Note Added filters for whether threat intelligence matched and processing status. |
|   | Threat investigati on | Investigate all available information for a given time range. Search by IP address or asset name. View matching asset details, network attacks, threat events, vulnerabilities, attack surfaces, and traffic analysis. Drill down into details. |
|   |   | Asset details include the following: Network topology view, asset fingerprint overview, and security group information. Abnormal behavior overview, severity distribution, type distribution, and top five abnormal behaviors. Network attack overview, data source distribution, type distribution, and top five network attacks. Threat event overview, type distribution, and top five threat events. Vulnerability and baseline overview, and top five items. Top five attack paths. Source IP and destination IP traffic statistics. View full details for abnormal behavior, network attacks, threat events, vulnerabilities, attack surfaces, and traffic analysis. |
|   |   | Attacker profile includes total attack count, associated threat events, number of victims, active days, attack sources, attack trends, attack source distribution, victim IP addresses, and attack timeline. |
|   |   | View the last ten search records. Pin frequent searches to the homepage. Add shortcuts for IP addresses, asset names, and asset IDs. |
|   |   | Manually or automatically refresh threat investigation search results. |
|   |   | View total attack count and core asset path count. Jump directly to the core asset list. |
|   |   | Search attack paths by IP address, asset ID, or asset name. |

|   | Managemen oduction·Fea |   |
|---|---|---|
| Risk analysis | Attack surface assessme nt |   |
|   |   | View attack paths in a centralized list. Columns include path name, risk score, number of affected core assets, and path asset information. |
|   |   | View attack paths in 2D or 3D panoramic mode. Show up to five attack paths and their risk information in one chart. Drill down to specific path details. |
|   |   | View attack path details in 2D or 3D mode. Includes basic path information and path diagrams. Specifically: Basic path information includes risk score, asset count distribution, security weakness distribution, and priority remediation suggestions. Path diagrams show assets outside the cloud, security devices, classic networks, and VPCs. Also show shadow IPs outside the cloud, exposed services, vulnerabilities, baselines, and risky accounts along the path. |
|   |   | Path diagrams automatically display risk information. Turn automatic risk display on or off. Risk information includes shadow IPs outside the cloud, exposed services, vulnerabilities, baselines, and risky accounts. |
|   |   | View ECS details in path diagrams. Includes basic and risk information. Basic information includes hostname, IP, importance, organization, and VPC. Risk information includes security vulnerabilities, security baselines, risky accounts, and exposed services. |
|   |   | Search shadow IPs outside the cloud by time, geography, or IP address. |
|   |   | View shadow IPs outside the cloud in a centralized list. Columns include IP, geography, number of connected cloud assets, and first/last discovery time. |
|   |   | View shadow IP details. Includes IP, geography, number of connected cloud assets, first/last discovery time, inbound connection trend chart, destination IP, and traffic information. Process shadow IPs with one click. |
|   |   | Export shadow IP lists. Includes shadow IP, geography, connected cloud assets, first discovery time, and last discovery time. |
|   |   | Search risky security groups by security group name. |
|   |   | View risky security groups in a centralized list. Columns include security group ID/name, organization, resource set, VPC, and inbound rule count. |
|   |   | View risky security group details. Includes VPC ID, security group type, organization, resource set, description, and security group instance list. |

|   |   | Export risky security group lists. Includes security group name, security group ID, organization, resource set, VPC, and inbound rule count. |
|---|---|---|
|   |   | Search exposed assets by exposure method, port, protocol, or server name/IP. |
|   |   | View exposed assets in a centralized list. Columns include server name/IP, organization, resource set, exposure method, exposed service, port, and protocol. |
|   |   | View exposed asset details. Includes basic and risk information. Basic information includes hostname, IP, importance, organization, and VPC. Risk information includes security vulnerabilities, security baselines, risky accounts, and exposed services. |
|   |   | Export exposed asset lists. Includes server name, server IP, organization, resource set, exposure method, exposed service, port, and protocol. |
|   |   | Search risky accounts by account name, root permissions, or server name/IP. |
|   |   | View risky accounts in a centralized list. Shows aggregated account data and details including account name, server name/IP, organization, resource set, weak password, root permissions, and last login time. |
|   | Behavior analysis | Track affected assets, multi-dimensional severity distribution visualizations, and end-to-end lifecycle monitoring of response status for abnormal behaviors detected by behavior analysis models. |
|   |   | Switch between behavior mode and instance mode to suit different scenarios and roles. |
|   |   | In behavior list mode, view behavior name, organization, timestamp range, severity, affected assets, risk score, status, and discovery time. View behavior details. |
|   |   | Behavior details include behavior name, risk score, severity, behavior model, organization, timestamp range, affected assets, remediation suggestions, visual behavior analysis view, and behavior timeline. |
|   |   | In instance list mode, view instance name/ID, organization, timestamp range, type, number of abnormal behaviors, total risk score, and most recent discovery time. |
|   |   | Respond to abnormal behaviors. View associated models and assets. Update status and adjust models. |
|   | Version: 2026 |   |

|   |   | Filter by timestamp range, organization, severity, processing status, instance name, and behavior name. |
|---|---|---|
|   |   | Cloud product security baselines cover network configuration, data security, access control, security protection, identity authentication, disaster recovery and backup, log audit, and monitoring and alerting. Check cloud products such as ECS, RDS, OSS, and SLB. |
|   |   | View baseline risk items, total affected assets, enabled baseline checks, disabled baseline checks, and latest check time for cloud platform and tenant product configurations. |
|   | Cloud product checks |   |
|   |   | View cloud product security baselines in a centralized list. Columns include baseline name, category, type, risk level, affected assets, latest check time, status, and description. |
|   |   | Drill down into cloud product security baseline details. Includes baseline description, remediation suggestions, and cloud product instances with related baseline configuration risks. |
|   |   | Run manual or scheduled automatic checks for cloud product configuration risks. Configure check cycles, times, resource sets, and baseline items. Validate or whitelist check results. |
|   | Weakness analysis | View non-compliant security configuration baselines for cloud platform and tenant assets. Columns include baseline name, risk type, risk level, affected assets, last discovery time, and organization. View affected asset lists, baseline risk items, and risk item details. |
|   |   | View security vulnerabilities for cloud platform and tenant assets. Columns include vulnerability name, type, remediation priority score, severity, CVE ID, affected assets, last discovery time, and organization. View vulnerability details and affected asset lists. |
|   |   | Calculate remediation priority scores using Server Guard vulnerability factors, impact scope, external exposure, disclosure time, and threat factors. View scores in radar charts. |
|   |   | Remediate, validate, ignore, or whitelist vulnerabilities. |
|   |   | Remediate, validate, or whitelist baselines. |
|   |   | Track vulnerabilities from discovery to closure, including remediation, validation, and closure status. |
|   |   | Filter and export baseline and vulnerability violation information by multiple criteria. |

|   | Traffic analysis | View traffic statistics by organization, application, source IP, destination IP, source port, destination port, traffic source, and traffic destination. Includes total traffic, average traffic trends, application protocol distribution, geographic distribution of traffic sources and destinations, and top five/top ten/top twenty traffic statistics. |
|---|---|---|
|   |   | Filter by timestamp range, organization, application, source or destination IP, and source or destination port. View raw traffic logs. |
|   |   | Add any statistical object from traffic views as a filter condition. Options include adding to the current view, adding to global search, searching in tenant assets, searching in log queries, and searching in threat investigations. |
|   |   | Customize traffic analysis pages. Turn views on or off. Adjust view positions. Export page snapshots with one click. |
| Threat intelligenc e | Overview | Count malicious indicators for IP addresses, domain names, and URLs. Show trends for highly active malicious indicators over the last 30 days. View threat intelligence API usage statistics and API query source distribution. View threat intelligence risk level distribution and top ten active malicious IPs, including IP, activity time, and malicious tags. Note You can now query intelligence sources using the API. |
|   | Threat Intelligenc e Query | View top ten active malicious IPs, top ten active malicious domain names, and top ten file MD5 hashes. Drill down into malicious indicator profiles, including threat level, basic information, IP tags, attack targets, attack count, impact severity, WHOIS, and intelligence sources. |
|   | Intelligenc e Managem ent | View threat intelligence authorization overview. Enable threat intelligence for security products such as SOC, WAF, and NDR. Track threat intelligence data consumption, including data type, update count, malicious judgment statistics, and intelligence tag types. |
|   |   | Import custom threat intelligence in standard format. Query imported intelligence. Note Added support for importing third-party intelligence in standard format. |
|   |   | Delete custom threat intelligence individually or in batches. |

| Risk response | Response tasks | Create response tasks. Set task name, organization, task type, priority, problem description, remediation suggestions, deadline, assignee, and notification method. Reference remediation plans from the knowledge base. Note Integrates with playbook approval. Search, manage, and respond to playbook approval tasks. |
|---|---|---|
|   |   | View response task statistics. Includes total tasks, pending tasks, in- progress tasks, completed tasks, completion rate, on-time completion rate, and knowledge base status. |
|   |   | Manage response tasks in a centralized list. Columns include task name, task type, priority, assignee, organization, creation time, task status, and processing status. Update task status. Note Integrates with playbook approval. Search, manage, and respond to playbook approval tasks. |
|   |   | Drill down into response task details. Includes basic information, problem description, remediation suggestions, response records, and management logs. Note Integrates with playbook approval. Search, manage, and respond to playbook approval tasks. |
|   |   | Manage remediation plan knowledge base. Create, edit, and delete plans. View plans in a centralized list. Columns include plan name, plan type, plan status, submitter, organization, and creation time. |
|   | Response records | Filter response records by scope, entity type, linked product, response scenario, and functional module. |
|   |   | View response records in a centralized list. Columns include ID, entity, entity type, response scenario, scope, action validity period, functional module, source, organization, auto-response rule, effective time, expiration time, creation time, update time, and status. View details. |
|   |   | Drill down into response record details. Includes entity, entity type, response scenario, effective time range, notes, and playbook-specific details such as scope, parameters, linked product, creation time, update time, and status. Reverse actions after successful playbooks, such as unblocking. Link directly to playbook details. |

|   | Platform assets | Track total platform assets, offline assets, and assets by risk level. |
|---|---|---|
|   |   | Collect information for physical servers and virtualized assets on the cloud platform, including physical servers, ECS instances, and miniRDS instances. |
|   |   | View physical servers in a list. Columns include server name/IP, organization, risk index, operating system, abnormal behavior, and online status. Tag servers with custom importance and business type labels. |
|   |   | View ECS instances in a list. Columns include server name/IP, host UUID, organization, VPC, risk index, operating system, network attacks, abnormal behavior, security vulnerabilities, security baselines, and online status. Tag instances with custom importance and business type labels. |
|   |   | View miniRDS instances in a list. Columns include server name/IP, region, port, platform, and threat events. Tag instances with custom importance and business type labels. |
|   |   | View asset basics: IP, UID, region, private IP, online status, host UUID, and host alias. |
|   |   | View asset risk profiles. Includes risk index, network attacks, abnormal behavior, security vulnerabilities, and security baselines. Also shows severity distribution, trend, and top five items. |
|   |   | View asset network attack details. Includes attack name, time, type, source IP, destination IP, data source, and status. |
|   |   | View asset abnormal behavior details. Includes behavior name, severity, type, affected assets, data source, status, and last occurrence time. |
|   |   | View asset security vulnerability details. Includes vulnerability name, type, severity, affected assets, CVE ID, remediation priority score, last discovery time, and processing status. |
|   |   | View security baseline details. Includes baseline name, risk level, risk type, affected assets, and last discovery time. |
|   |   | View asset threat event details. Includes threat name, severity, type, attack phase, source IP, destination IP, processing status, first/last attack time, and update time. |
|   |   | Collect asset fingerprint information. Includes AI components, ports, software, processes, accounts, scheduled tasks, middleware, and startup items. |

|   |   | Filter assets by server name/IP or UUID. Export asset lists with one click. |
|---|---|---|
|   |   | View asset process behavior. Includes behavior distribution, top five behaviors, behavior list, and process tree. After locating a process, view its parent and child processes. Highlight the located process. Note Added asset process behavior analysis using UEBA technology to reconstruct process behavior and build process trees. |
|   |   | View process behavior in a list. Columns include time, behavior name, key behavior features (log fields), and process name. Filter by behavior name. Note Added asset process behavior analysis using UEBA technology to reconstruct process behavior and build process trees. |
|   |   | View asset configuration behavior. Includes behavior distribution, top five behaviors, and behavior list. Note Added asset configuration behavior analysis using UEBA technology to reconstruct cloud asset configuration behavior. |
|   |   | View configuration behavior in a list. Columns include behavior name, corresponding ECS log field, and description. Show all critical behaviors detected in the statistical period on a timeline, ordered by occurrence time. Note Added asset configuration behavior analysis using UEBA technology to reconstruct cloud asset configuration behavior. |
|   |   | Track total organizations, total tenant assets, offline assets, and assets by risk level. Also track asset type distribution, newly added assets in the last day, and public-facing asset types. |
|   |   | Collect information for tenant cloud hosts and virtualized assets. Includes ECS, AI assets, containers, RDS, OSS, SLB, EIP, Tunnel, and external hosts. |
|   |   | View ECS instances in a list. Columns include public/private IP, organization, resource set, VPC, risk index, operating system, running status, network attacks, abnormal behavior, security vulnerabilities, security baselines, new status, suspicious security groups, security alerts, vulnerability risks, network attacks, Agent status, snapshots, memory, and disk. Tag instances with custom importance and business type labels. |

| Asset managem ent |   |   |
|---|---|---|
|   |   | View RDS instances in a list. Columns include instance ID, organization, resource set, type, backup status, whitelist IP status (strict/loose), whitelist group, network type, SSL encryption, and TDE encryption. View vulnerability risk details for individual assets. |
|   | Tenant assets |   |
|   |   | View OSS instances in a list. Columns include instance name, organization, resource set, disk usage, new status, access permissions, and referer configuration. View vulnerability risk details for individual assets. |
|   |   | View SLB instances in a list. Columns include ID/name, IP address, organization, resource set, new status, running status, and listening ports. View network attack, abnormal behavior, and vulnerability risk details for individual assets. |
|   |   | View EIP instances in a list. Columns include ID/name, organization, resource set, region, running status, new status, and bandwidth. View network attack, abnormal behavior, and vulnerability risk details for individual assets. |
|   |   | View external hosts in a list. Columns include name/IP, organization, resource set, vendor, region, risk index, operating system, abnormal behavior, security vulnerabilities, security baselines, Agent status, and UUID. View details, fingerprints, abnormal behavior, vulnerability risk, and external exposure for individual assets. |
|   |   | View network topology for ECS instances. Visualize network connections and public-facing paths. Support network troubleshooting, attack surface reduction, and threat traceability. |
|   |   | Link with Alibaba Cloud Apsara Stack CMDB to get application-layer business information. Includes applications, application systems, product lines, and security, importance, availability, and continuity ratings. |
|   |   | Collect asset fingerprint information. Includes AI components, ports, software, processes, accounts, scheduled tasks, middleware, and startup items. |
|   |   | View asset risk profiles. Includes risk index, network attacks, abnormal behavior, security vulnerabilities, security baselines, and external exposure. Also shows severity distribution, trend, and top five items. |
|   |   | View asset network attack details. Includes attack name, time, type, source IP, destination IP, data source, status, product line, application system, and application. |
|   |   | View asset abnormal behavior details. Includes behavior name, severity, type, affected assets, data source, status, last occurrence time, product line, application system, and application. |

|   |   | View asset security vulnerability details. Includes vulnerability name, type, severity, affected assets, CVE ID, remediation priority score, last discovery time, and processing status. |
|---|---|---|
|   |   | View security baseline details. Includes baseline name, risk level, risk type, affected assets, and last discovery time. |
|   |   | Analyze and locate external exposure intelligence. Includes middleware name, type, risk level, version, PID, running user, listening IP, listening port, listening status, listening port protocol, security group ID/name, SLB, DNAT, EIP, and associated vulnerabilities. |
|   |   | Filter assets by multiple criteria. Customize displayed columns. Export asset details with one click. |
|   |   | Set custom synchronization cycles for platform and tenant assets, including ECS, RDS, OSS, SLB, and EIP. |
|   |   | View asset process behavior. Includes behavior distribution, top five behaviors, behavior list, and process tree. Locate processes by PID, process name, or username. Note Added asset process behavior analysis using UEBA technology to reconstruct process behavior and build process trees. |
|   |   | View process behavior in a list. Columns include time, behavior name, key behavior features (log fields), and process name. Filter by behavior name. Note Added asset process behavior analysis using UEBA technology to reconstruct process behavior and build process trees. |
|   |   | View asset configuration behavior. Includes behavior distribution, top five behaviors, and behavior list. Note Added asset configuration behavior analysis using UEBA technology to reconstruct cloud asset configuration behavior. |

|   |   | View configuration behavior in a list. Columns include behavior name, corresponding ECS log field, and description. Show all critical behaviors detected in the statistical period on a timeline, ordered by occurrence time. Note Added asset configuration behavior analysis using UEBA technology to reconstruct cloud asset configuration behavior. |
|---|---|---|
|   |   | View asset behavior baseline information. Cards show the status of associated abnormal behavior models and baseline learning period. |
|   | Log overview | View statistics for total ingested logs, organization distribution, log trends, log level distribution, log source distribution, system type distribution, log type distribution, log type trends, and watched logs. |
|   |   | Customize the overview page. Turn views on or off. Adjust position and size. Change chart types. View and copy query statements for statistical views. |
|   |   | View log statistics by timestamp range and organization. Export page snapshots with one click. |
|   | Log search | Search standardized logs globally. Filter by timestamp range, organization, system category, log source, log type, log subtype, log field, and log content. |
|   |   | Search and aggregate logs using keywords and logical expressions. Support fuzzy keyword matching. Save searches as quick search conditions. Add search results to conditions with one click. Auto-fill query language. Use heuristic query input. |
|   |   | Convert natural language to SPL statements. |
|   |   | View log search results in structured data or Syslog format. Customize visibility of log fields. |
|   |   | Save log search result field configurations. Note Added configurable log search result templates. |
|   |   | Refine search results within a timestamp range. |

| Log managem |   |   |
|---|---|---|
|   |   | Support multi-log-source query and analysis. Note Depends on SLS multi-logstore association query and analysis. SOC restores multi-log-source query and analysis capabilities for log queries and analysis rules. |
|   |   | Create custom log overview views from search results. Configure view size, icon type, data type, chart name, and X/Y axis names. |
|   |   | Support log chart types: multi-value charts, percentage charts, pie charts, column charts, bar charts, treemap charts, tables, line charts, bubble charts, and area charts. |
|   |   | Set log association query results as watched logs. Export to Excel with one click. |
|   | Platform logs | Search platform audit logs for a specified log source within the audit time range. |
|   |   | Search using keywords. Save search conditions as analysis rules. |
|   |   | Export audit logs to Excel with one click. |
| ent |   |   |
|   | Tenant logs | Search tenant audit logs for a specified organization and log source within the audit time range. |
|   |   | Search using keywords. Save search conditions as analysis rules. |
|   |   | Export audit logs to Excel with one click. |
|   |   | Built-in ingestion for Alibaba Cloud Security network element log sources. Manually configure third-party product log sources via Syslog or SLS. |
|   |   | Use Logtail clients to collect system logs from Windows and Linux. Collect custom application service logs. Configure log directories, directory depth, log files, and filter conditions. |
|   |   | Manage log sources in a list. Calculate total ingested logs per source. Check source online status. Filter by source, system type, and data protocol. |

|   |   | Configure log ingestion conditions. Ingest or skip logs that meet conditions. Note Added log ingestion filtering configuration. |
|---|---|---|
|   | Log configurat ion |   |
|   |   | Built-in log parsing templates for Alibaba Cloud Security network elements: Server Guard, NDR, WAF, Cloud Firewall, Container Security, SSDP, DNS, and NFV Cloud Firewall. Also supports third-party security network elements: Qihoo 360 SkyEye, firewalls, WAFs, QingTeng Cloud Host Security, AnHeng Bastionhost, SiFuDi Bastionhost, DBAudit, and MoAn Vulnerability Scanner. |
|   |   | Create custom log parsing templates for automated third-party log parsing. Supports JSON, JSONArray, JSONCut, JSONArrayCut, grok, and keyValue parsing. Format timestamps, add or remove fields, and use scripts for formatting. |
|   |   | Map standardized log fields using scripts or manual selection. |
|   |   | Smartly analyze log structure during field mapping. Recommend automatic field mapping. |
|   |   | Forward cloud logs to third-party servers using Syslog or Kafka protocols. |
|   |   | Manage log forwarding tasks. Create, edit, and delete tasks. View tasks in a centralized list. Columns include task name, forwarding method, organization, IP and port, and status. Filter by organization and task name. |
|   |   | Create log forwarding tasks. Set task name, forwarding method, organization, logs to forward, and status. |
|   |   | View forwarding details for each log source subtype. Includes log source, log subtype, total logs sent, and data volume sent in the last 24 hours. |
|   |   | Track total reports, daily reports, weekly reports, monthly reports, and custom-cycle reports. Show latest report generation time. |
|   |   | Manage generated reports in a list. Download and delete reports. Filter by time, organization, task type, and task or report name. |
|   |   | Manage report tasks. Create, edit, and delete tasks. View tasks in a list. Columns include task name, task type, report name, organization, latest report generation time, next report generation time, generated report count, and task status. View and download data reports. Send reports. Filter by organization, task type, task status, and task or report name. |

|   |   | Reports support HTML format. |
|---|---|---|
| Report managem ent | Report managem ent |   |
|   |   | Create one-time, daily, weekly, monthly, and custom-cycle report tasks. Set task name, description, type, report name, data range, template, format, storage duration, status, send time, recipients, and delivery method. Reference built-in and custom report templates. |
|   |   | Manage report templates. Built-in templates include security risk templates. Create, edit, delete, and copy custom templates. View templates in a list. Columns include template name, type, organization, creation time, and update time. Filter by organization, template type, and template name. |
|   |   | Built-in security risk templates generate reports with security risk overview, network attack risk analysis, abnormal behavior risk analysis, security vulnerability risk analysis, and security baseline risk analysis. |
|   |   | Create custom report templates. Set template name, description, and content. Content includes security risk overview, network attack risk analysis, abnormal behavior risk analysis, security vulnerability risk analysis, and security baseline risk analysis. Configure top five/top ten/top twenty/top thirty risk information and risk levels. |
|   | Behavior models | Initialize abnormal behavior analysis models using a clear guided page. Improve user experience and reduce system load. |
|   |   | Configure abnormal behavior analysis models in the UI. Create, manage, and update custom models. Build and update instance behavior baselines automatically. Detect behaviors outside normal operation ranges. Display abnormal behaviors and notify relevant personnel. |
|   |   | Built-in association analysis rules include threat name, threat level, threat type, ATT&CK ID, threat description, and remediation suggestions. |
|   |   | Create custom association analysis rules. Configure threat name, threat level, threat type, ATT&CK ID, association timing, associated objects, association conditions, rule execution cycle, threat description, and remediation suggestions. |
|   |   | Create custom search analysis rules. Configure log range, search conditions, time period, rule execution cycle, threat description, and remediation suggestions. |
|   |   | Custom association conditions support three timing modes: unordered match in same period, ordered match in same period, and ordered match across periods. Associate using log range, analysis threshold, aggregated fields, and associated threat intelligence. |

| Policy managem ent | Analysis rules |   |
|---|---|---|
|   |   | Custom association conditions support contains, does not contain, equals, does not equal, belongs to, does not belong to, and regular expression matching. |
|   |   | Quickly validate custom association analysis rules. View matching log counts to verify rule effectiveness. |
|   |   | Manage association analysis rules in a list. Filter by threat level, threat type, and threat name. Import and export custom rules. Delete custom rules in batches. |
|   |   | Copy analysis rules to other organizations. Note Added permission to share current rules with other organizations. |
|   |   | Drag and drop multiple association conditions to reorder them. Retain all configured content after dragging. |
|   | Response policies | Configure response policies for threat events, security alerts, security vulnerabilities, and security baselines. Support DingTalk and email notifications. |
|   |   | Link security alerts to automated responses. For matching alerts, link WAF or NDR to block source IPs or source IPs to host machines. |
|   |   | Link threat events to automated responses. For matching events, link WAF or NDR to block entity IPs. Configure whitelists for linked responses. |
|   |   | Create response policies. Set policy name, description, scope, conditions, alert objects, alert methods, and alert interval. |
|   |   | Manage response policies in a list. Filter by policy name, type, response method, and organization. |
| Operation s managem ent | Storage managem ent | Set maximum log storage duration for built-in storage. Configure data cleanup notifications. Send warnings via DingTalk or email. |
|   | Organizati on authorizat ion | SLR authorization lets organizations grant the Cloud Security Management Center access to cloud assets and related security data. Global administrators can authorize on behalf of organizations, or organizations can self-authorize. View authorization status. |

scenarios

## 5 Common scenarios

Security Operations Center (SOC) is suitable for building security frameworks in cloud environments such as the industry cloud, Alibaba Gov Cloud, and co-built cloud. SOC supports scenario-based operations of cloud computing networks across sectors, including the public service sector, finance, energy, state-owned enterprises, and national ministries and commissions.

**Global and centralized security operations**

In the context of migration to the cloud due to digital transformation and network protection initiatives, an ecosystem for network security is necessary to ensure continuous, stable, and secure business growth. SOC is suitable for integrating data from security network elements in the ecosystem. This allows SOC to facilitate comprehensive security operations from a global perspective.

**APT detection and handling**

Driven by political and economic purposes, cyberattacks persist and constantly evolve. Defense against traditional information security risks and novel threats specific to cloud network environments is required. Novel threats such as advanced persistent threats (APTs) are characterized by their targeted, stealthy, prolonged, and organized nature. To detect and handle APTs, you must use emerging network security technologies and perform comprehensive association analysis based on discrete data to implement security policies.

**Asset security management in the cloud**

After an enterprise or institution migrates critical workloads to the cloud, Internet-facing services must be provided in a continuous, high-quality, and secure manner. In this case, the running status, network conditions, and security status of cloud servers and virtual assets that host the critical workloads must be properly monitored and managed.

**Security operations and management of tenants**

A tenant is an independent virtual private cloud (VPC) on a cloud platform. If application risks exist in the cloud computing resources of a tenant, the security of the cloud platform and other tenants may be affected. A tenant must be responsible for its security, and the operator of the cloud platform is responsible for its security operations and management. Meanwhile, the operator must monitor and control the assets and business of the tenant to ensure network security of the cloud platform and other tenants.

**Centralized audit of network logs and security logs**

The current network security system accommodates multiple security service providers and security services due to two factors. First, regulatory requirements such as policy and compliance requirements require centralized audit and long-term storage of network logs and security logs for more than 180 days. Second, based on the shift-left security approach, the system supports storage and backup of logs for business systems to prevent log tampering and deletion.
