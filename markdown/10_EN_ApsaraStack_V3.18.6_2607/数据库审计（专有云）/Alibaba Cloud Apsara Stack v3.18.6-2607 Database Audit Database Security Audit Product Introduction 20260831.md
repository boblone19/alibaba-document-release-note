---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Product Introduction 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 14
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Product Introduction 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AE%A1%E8%AE%A1%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Database%20Audit%20Database%20Security%20Audit%20Product%20Introduction%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Product Introduction 20260831

udit Product Introduction

## Database Security Audit

**Product Introduction**

Database Security Audit supports audit on the process and behavior of accessing selfmanaged databases in the cloud and ApsaraDB services, and supports association with application users for operation audit. It also monitors the risks, status, performance, and statement distribution in real time. Database Security Audit provides a cloud database audit service that can be quickly deployed and easily maintained by using database-based UI languages, intelligent protocol recognition, visualized status display, and interactive risk tracking that supports drill-down.

## Features

This topic describes the features of Database Audit.

| Level 1 features | Secondary Characterist ics | Feature Description |
|---|---|---|
| Group management | IP Address Group | You can create IP address groups. |
|   | Object Group | Object groups can be created and referenced when you configure rules. |
|   | Application user group | Supports creating application user groups. |
|   | Database User Group | You can create database user groups to facilitate database management. |
|   | Time Group | You can create time groups and reference them when you configure rules. |
| Protocol support | ApsaraDB | Supports ApsaraDB services such as PolarDB(Mysql), PolarDB(PostgreSQL), PolarDB-X(Mysql), RDSMySQL, RDSSQLServer, RDSPostgreSQL, RDSMariaDB, RDSMongoDB, OceanBase, AnalyticDB(MySQL), AnalyticDB(PostgreSQL), MaxCompute, and Hologres. |
|   | Chinese- made database | The system supports audit on Chinese-made databases, including KingbaseES, Dameng, Shentong, GBase, and Huawei GaussDB. |
|   | International database | The system supports audit on international mainstream databases, including Oracle, SQL Server, Db2, Informix, PostgreSQL, Sybase ASE, Sybase IQ, MySQL, MongoDB, SAP HANA, Teradata, Cache, MariaDB, and Percona. |
|   | Big data | The system supports audit on big data platforms, including Hive, HBase, Sentry, Impala, HDFS, Elasticsearch, Greenplum, and Redis. |

| Audit information display and search | Session analysis | The system supports session search and session details display, and provides dedicated analysis pages for session information, including online concurrent sessions, active sessions, and failed login sessions. The system supports session statistics collection, search, and analysis based on database access sources, as well as statistical analysis on active sessions and failed sessions within a time period. You can lock a specific session to which an SQL statement belongs and perform a drill-down to obtain all SQL statements within the session lifetime. |
|---|---|---|
|   | Audit information display | The system supports search and analysis in three dimensions: session dimension, statement dimension, and risk dimension. The system records audit information and displays the following detailed information in the audit result: alert level, event occurrence time, client IP address, destination database IP address, operation type, client MAC address, destination database MAC address, client port number, response time, return status, result information, SQL statement, and SQL parameters. |
|   | Search | The system supports statistical analysis based on multiple dimensions. You can perform statistical analysis globally, for a group, or for a single database. The system supports multi-database statistical queries with at least 20 search conditions. |
|   | Statistical analysis | You can perform trend analysis and statistics collection based on multiple dimensions, such as session, risk, and statement distribution, and display the data in charts. |
|   | Statistical comparison | You can create a comparison of statistics across different databases at different intervals. This way, you can visualize the current client access status, database performance, and the number of SQL statements. |
| Audit log backup and recovery | Audit log backup and recovery | Supports automatic backup of audit data to local and remote FTP, SFTP, NFS, and OSS servers. Supports import and export of audit logs and system configurations. Supports high performance and high compression ratio for data backup. |

| audit capability | Audit information | Terminal information of the session: IP, MAC, Port, tool name (program name), operating system user. The host information of the session: IP address, port number, database name (instance name), and business host group. Other information about the session: logon time and session duration. Operation information: operation type (such as DDL, DML, and DCL), operation time, execution duration, operation object (database instance, schema, and table), SQL statement, and SQL error code. The operation scope information: the number of rows affected by the query, modify, and delete operations, and the number of rows returned. Supports result set auditing and records the success and failure of operations. Supports one-way request package audit. |
|---|---|---|
|   | Result set audit by rule | Result sets can be audited based on policies. You can specify result sets to audit sensitive tables to reduce system overheads. |
|   | Long statement audit | Supports the audit of extremely long SQL statements. The length of a single statement can be up to 2 MB. |
| Audit risk monitoring capability | Audit rule and policy | Rule types: access rule, injection, action rule, and password breach You can configure at least 20 conditions for an audit rule. The logical relationship between the conditions of an audit rule can be AND or OR. Statement rule: You can configure rules for trusted statements based on statement templates in a single database. This way, you can create a blacklist or whitelist of statements. |
|   | Audit rule management | You can create global policies. Based on global policies, rules can be set for all databases. You can create policies for a single database to configure trusted statements. This way, you can create a blacklist or whitelist of statements for a single database. You can import and export policies and configure priorities. You can add exception rules to improve policies. The system provides default built-in rules for different databases. |
|   | Database vulnerability exploitation monitoring | The system provides a built-in database vulnerability exploitation rule library to monitor attacks that exploit database vulnerabilities and generate alerts. |
|   | > Document Version: 2026083 |   |

|   | Risk alert | Risk levels: high, medium, and low Alert methods: email and syslog |
|---|---|---|
| Report content | Report content | The system provides at least 40 report models based on multi- database and single-database dimensions, including compliance reports, special reports, and comprehensive reports. The system combines charts and tables to display reports from multiple dimensions, such as the overview, performance, sessions, statements, and risks. The system supports multiple types of reports, such as reports for risky logins, high risks, and client risks. Supported export formats: Word, PDF, and HTML |
|   | Report presentation | The system provides multiple display methods, such as tables, column charts, pie charts, and line charts. |
|   | Report feature | The system supports report push, report preset, and custom reports. |
| Business monitoring | Integration with Cloud Monitor | The system integrates with Cloud Monitor to monitor system resource usage and business metrics. |
| Deployment mode | Bypass agent deployment | The bypass deployment method does not affect the original network, and the failure of the network audit product does not affect the normal operation of the audited system. Self-built database (ECS): directly deployed on the database end of the audited system. Databases provided by cloud service providers (RDS): need to be deployed at the application end that accesses the database of the audited system. |
|   | Data security open platform | You can obtain logs from Data Security and Open Platform. You can obtain logs from the following cloud-native database types: ApsaraDB RDS, Polardlocal (MySQL, Oracle, and Postgres), OceanBase, MaxCompute, and AnalyticDB for PostgreSQL. |

curity Audit?

## What is Database Security

**Audit?**

Data has become a new driver of business decision-making, a new content of trade in goods and services, and even a new means of comprehensive social governance. To ensure the security of important data and the normal operation of databases, Database Security Audit acts as a scout to protect database security, monitor data security, gain insights into data risks, and help users complete security compliance, user behavior analysis, O&M monitoring, risk audit, incident tracing, and security audit in scenarios related to database security. Database Security Audit is an accurate database security audit system based on database protocol parsing and SQL parsing technologies. The system provides the capabilities of comprehensive data behavior audit and timely detection of data risks, which can meet the requirements of data security compliance, risk monitoring and tracing, user behavior analysis, and auxiliary business optimization. The system adopts a browser/server (B/S) architecture. Users can log in to the system by using a browser on a connected terminal over the network. By using an effective database monitoring method, the system monitors the behaviors of accessing and operating databases and the return results to conduct a comprehensive audit. The system provides a security monitoring engine to allow users to customize different audit rules, and generates risk records and alerts for risky database operations such as database collision attacks, high-risk operations, important object queries, database vulnerability exploitations, and SQL injections. The engine also allows users to add trusted statements to a whitelist. The system provides search and statistics collection capabilities to implement user behavior analysis and risk tracing.

## Service architecture

The architecture of Database Security Audit is divided into the traffic capture, protocol parsing, data processing, and system management layers. Table Repair System Repair RMAgent Database Rule Engine Management Management Management Management

**System**

Backup Cleanup Monitoring and System Security Data Export User

**Management**

and Recovery Keep-alive Permission Control Management Management Management

**System**

**System**

**Maintenance**

**Management**

Statement Audit Template Statement Risk Search Risk Alert Audit Data Session System Template Table Search Statistics Statistics Alerting Flow Table

**Data**

Statement Template Behavior Statement Risk System Session Table Risk Table Session Search Report Push

**Processing**

Statistics Search Statistics Template Audit Log

**Data Indexing**

**Data Statistics**

**Data**

**Data**

**Import**

**Export**

Data Breach Password Breach Injection Vulnerability Trust Planning Access High-risk Exploitation Control Operation

**Protocol**

**Rules Engine**

**Parsing**

**Database Protocol**

**SQL Rewrite**

**SQL Parsing**

**Parsing**

**Traffic Capture**

**Deployment**

**Modes**

**Data**

Integrated Hardware Virtualization Software Bypass Mirroring RMAgent Local Audit

**Capture**

and Software Deployment Image Deployment Deployment

**Traffic capture layer**

The traffic capture layer accesses the traffic to be audited, filters out the traffic that does not need to be audited, and captures the traffic that needs to be audited. RMAgent is used for traffic capture in Apsara Stack. If the environment does not support traffic mirroring on the switch, you must install RMAgent on the database server or on a server that directly accesses the database. The agent captures local traffic for database access and sends it to Database Security Audit.

**Protocol parsing layer**

The protocol parsing layer calls Network Protocol Processor (NPP) to parse the captured database traffic. For an SQL statement obtained from protocol parsing, NPP rewrites the statement to generate a statement template, and parses the SQL statement. For all audit elements, NPP makes a reasonable information integration to ensure the completeness of audit elements. The R&D team of Database Security Audit has rich experience in kernel development for large databases. After dozes of years of polishing, Database Security Audit supports accurate and comprehensive database protocol analysis. As an important module of NPP, its rules engine identifies and processes all risks and trust rules.

**Data processing layer**

The audit data is sent to the data center and stored in multiple tables. The system regularly collects statistics from the audit data by minute, hour, or day. The full-text indexing mechanism is adopted to support queries in huge amounts of data, and the query results can be generated within a few seconds for hundreds of millions of data records. The audit result can be sent by using email, syslog, or Security Operations Center (SOC).

**System management layer**

Database Security Audit provides a variety of auxiliary capabilities, such as table repair, system repair, data backup cleanup and recovery, monitoring, and keep-alive, to further ensure the normal operation of databases. The web console provides many system management capabilities, such as database management and rule management.

## Common scenarios

**Compliance**

Database Security Audit meets classified protection requirements such as database operation audit and log retention in compliance with laws such as the Cybersecurity Law and Data Security Law.

**Security event tracing**

Database Security Audit provides database operation records and post-event analysis from multiple dimensions such as statement, session, IP address, database user, business user, response time, and number of affected rows. It serves as a reliable tracking basis and source for security events. Based on the accurate association between SQL behavior and business users, Database Security Audit allows you to associate the business staff with database access behavior to effectively investigate and determine the accountability.

**Database performance diagnostics**

Database Security Audit displays the database status, database access traffic, concurrent throughput, and SQL statement response speed in real time. It analyzes inefficient statements and frequently used statements to help O&M engineers diagnose the performance.

**Webshell program detection**

Database Security Audit provides the SQL learning and SQL whitelist capabilities to perform SQL modeling for business systems. Based on the modeling of legal system behavior, Database Security Audit generates alerts in real time when it detects the startup of webshell programs hidden in software systems. This reduces losses caused by data leaks.

**Database attack response**

Database Security Audit provides database risk alerting and supports policy configuration and real-time alerting for risky behavior such as SQL injections, database vulnerability attacks, excessive data downloads, and dangerous SQL statements (such as the DELETE statement without a WHERE clause).

## Deployment mode

This topic describes the deployment mode of Database Security Audit. Database Security Audit supports agent-based deployment. The RMAgent component is deployed on a database server (or the server of an application system that accesses the database) to collect the traffic of the server network interface controller (NIC) or local loopback traffic to complete data collection, and delivers the captured database traffic to the specified audit device through the NIC allocated by the server. The audit device uses a builtin and independent process to receive and parse the collected database traffic to complete the audit operation. The system supports multi-agent deployment, batch installation, and centralized management.
**Usage notes**:
If RMAgent is deployed on an application server, the system can audit only the operations of the application system accessing the database. If RMAgent is deployed on a database server, the system can collect traffic of the server NIC and local loopback traffic. RMAgent only captures and transmits data to the audit device, and does not affect the system load of the server on which the agent is deployed. RMAgent provides high compatibility and can be installed on mainstream operating systems such as CentOS, Red Hat, Solaris, and AIX.
