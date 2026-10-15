---
title: "Tenant-side Bastionhost Product Introduction 20260701"
product_version: "V3.18.6"
pdf_pages: 17
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Tenant-side Bastionhost Product Introduction 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E7%A7%9F%E6%88%B7%E4%BE%A7%E5%A0%A1%E5%9E%92%E6%9C%BA%EF%BC%88A%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Tenant-side%20Bastionhost%20Product%20Introduction%2020260701.pdf"
converter: line-classifier (PyMuPDF)
---

# Tenant-side Bastionhost Product Introduction 20260701

Tenant-side Bastionhost Product I

## What is Bastionhost?

Developed by Alibaba Cloud based on years of theoretical and practical experience in O&M security management, Bastionhost provides a platform for centralized security management and audit that controls risks in O&M operations. Bastionhost complies with the requirements of the Multi-Level Protection Scheme (MLPS) and other laws and regulations on O&M audit. Bastionhost adopts the B/S architecture and integrates features including authentication, account management, authorization, and log audit. It supports security monitoring and historical data queries based on multiple character terminal protocols, file transfer protocols, graphic terminal protocols, and remote application protocols.

**User permission management**

Bastionhost supports multiple user roles: super administrator, department administrator, O&M administrator, audit administrator, O&M engineer, auditor, and system administrator. Each user role has different permissions, which can meet compliance requirements for permission management.

**Centralized authorization**

Centralized authorization helps sort out authorization relationship between users and hosts. You can grant permissions on a host to a user, grant permissions on multiple hosts to a user, grant permissions on a host to multiple users, and grant permissions on multiple hosts to multiple users.

**Single sign-on (SSO)**

You can host the usernames and passwords of hosts on Bastionhost. An O&M engineer can click Log On to log in to the required host without the need to enter the username and password.

**Centralized audit**

Bastionhost records all operations and allows you to query the records. Audit logs can be played online, and operation logs can be automatically backed up.

**Automatic password change**

Network management personnel are required to manually update passwords for network devices on a regular basis. The automatic password change feature of Bastionhost can automatically rotate the passwords of assets on a regular basis.

**Command control**

Bastionhost provides command control policies in a centralized manner and allows you to configure command control policies based on different hosts and users. Command control policies support the following actions: command blocking, command blacklist, and command whitelist.

**Ticket**

When an O&M engineer requests permissions from an administrator to access a device, the O&M engineer can submit an O&M ticket and specify the IP address of the device, device account, O&M validity period, and remarks. Then, the administrator is notified of the O&M ticket by email. After the administrator reviews the O&M ticket, the administrator notifies the O&M engineer by email. If the administrator approves the request, the O&M engineer can access the device. Otherwise, the O&M engineer cannot access the device.

**System self-review**

Tenant-side Bastionhost Product I Bastionhost audits the operations that are performed by users and itself, and generates system analysis reports.

| Feature category | Feature | Description |
|---|---|---|
| User management | Management by department | Allows you to manage user data based on the department structure. |
|  | User management | Allows you to create users or import users from templates. |
|  | User synchronization | Supports login to Bastionhost through the following authentication methods: Active Directory (AD), Lightweight Directory Access Protocol (LDAP), and Remote Authentication Dial-In User Service (RADIUS). Multiple AD domains are supported. Automatic AD and LDAP user synchronization is supported. |
|  | Password settings | Allows you to customize password policies, such as the password length, complexity, relevance, unique usernames, unique usernames in reverse order, and expiration alert rules. |
|  | Login methods | Allows you to configure Bastionhost login methods, such as DingTalk and WeCom login by scanning QR codes. |
|  | User login settings | Automatically deactivates users who remain logged off for a long period of time. You can configure a threshold for deactivating such users. |
|  | User security settings | Supports user security policies that define the user validity period, user login time, user login IP address range, and user login MAC address range. |
|  | User roles | Supports multiple user roles, such as super administrators, system administrators, security administrators, security auditors, and regular users. You can also create custom roles. |
|  | Two-factor authentication | Authenticates logins to your bastion host based on dynamic verification codes sent through apps and text messages. |
|  | Authentication method settings | Supports different two-factor authentication modes based on global or different users. Supports multiple authentication methods for a single user at the same time. |

Tenant-side Bastionhost Product I

## Features

| Asset management | Tree view | Supports host management in tree view mode and custom asset directory hierarchies to facilitate asset data management. |
|---|---|---|
|  | O&M protocols | Supports common O&M protocols, such as SSH, Telnet, RDP, VNC, FTP, SFTP, Rlogin, and X11. |
|  | O&M applications | Allows you to extend O&M protocols by releasing applications, such as Oracle, MSSQL, MySQL, VMware vSphere Client, browsers, and other client tools. |
|  | Compatible client types | You can use single sign-on (SSO) to call a variety of local client tools: Characters: Xshell, SecureCRT, PuTTY, and MobaXterm. Graphics: RealVNC, TightVNC, and TigerVNC. File transfer: SecureFX, FlashFXP, FileZilla, WinSCP, Xftp, and MobaXterm. Databases: SQL Server Management Studio (SSMS), sqlwb, DBeaver, MySQL Client, DbVisualizer, MySQL Workbench, MySQL Front, PL/SQL, SQL*PLUS, db2cmd, Quest Central, pgAdmin III, PgSQL, KSQL, lsql, dlsql, DM manager, GBaseDataStudio, Toad, Toad for DB2, and Navicat. With the help of these tools, you do not need to use application release servers. |
|  | Multi-cloud asset discovery | Adaptive to multiple cloud environments, including Huawei Cloud, Baidu Cloud, Amazon Web Services, Tencent Cloud, Microsoft Azure, Ucloud, BlueKing, and Qingteng Sentry, and supports synchronization of cloud hosts to bastion hosts. |
|  | LAN asset discovery | Scans local area networks (LANs) for IP addresses of hosts that are not managed on Bastionhost. |
|  | Asset diagnostics | Runs diagnostics on hosts managed on Bastionhost for issues such as connectivity, zombie assets, and disabled assets. |
|  | Asset export encryption | Encrypted exported assets in ZIP. |

Tenant-side Bastionhost Product I

| Database management | Database compatibility | Supports protocols of DB2, Oracle, MySQL, SQL Server, PostgreSQL, KingbaseES, DM, GBase 8a, GBase 8s, HighGo, Redis, and GaussDB. After automatic login, Bastionhost can directly call the database client tool of the on-premises Windows system to perform database O&M, without the need to use jump servers. Supported database client tools include SSMS, sqlwb, DBeaver, MySQL Client, MySQL Workbench, MySQL Front, DbVisualizer, PL/SQL, SQL*PLUS, Toad, Toad for DB2, db2cmd, Quest Central, pgAdmin III, PgSQL, KSQL, lsql, dlsql, DM manager, GBaseDataStudio, and Navicat. |
|---|---|---|
|  | Database command control | Supports database command control, which can block sessions and commands, review actions, and allow actions. |
| Application release requirements | Auto-fill for web applications | Auto-fill for Internet Explorer, Google Chrome, Firefox, and other browsers during application release: Automatically fill in the account username and password for HTTP and HTTPS web devices. |
|  | URL access control | Supports URL blacklists and whitelists for HTTP and HTTPS assets. Unauthorized users are not allowed to redirect to other websites by manually entering URLs. |
| Ticket management | Ticket management | Supports review rules for O&M tickets, password tickets, emergency O&M tickets, command review, O&M review, and O&M tasks. |
| Automatic password change | Automatic password change | Supports automatic password change for Windows servers, network devices, Linux servers, Unix servers, mainstream databases, databases developed by Chinese vendors, and web applications. |
| Policy-based control | Authorization rules | Supports authorization rules at different dimensions, such as user, user group, asset, asset account, and asset directory. You can also specify an effective time period and applicable IP addresses for the authorization rule. |
|  | Host command control | Supports host control policies based on dynamic policy matching. You can also specify an effective time period and applicable IP addresses for the policy. Supports four host command control actions, including allow, close session, block request, and review. Supports parsing and regular expressions for matching host commands against command sets. |

Tenant-side Bastionhost Product I

|  | Database command control | Supports database command control based on dynamic policy matching. You can also specify an effective time period and applicable IP addresses for the policy. Supports four database command control actions, including allow, close session, block request, and review. Supports SQL parsing and regular expressions for matching database commands against command sets. |
|---|---|---|
|  | O&M | Supports the B/S architecture for Bastionhost O&M. You can use browsers such as Internet Explorer, Google Chrome, Firefox, and Microsoft Edge to open Bastionhost web pages and directly call local O&M client tools, such as mstsc, VNC, Xshell, SecureCRT, PuTTY, WinSCP, FlashFXP, FileZilla, and SecureFX. |
|  | Dedicated O&M clients | Support Bastionhost-dedicated O&M clients based on the C/S architecture for Windows and macOS operating systems. You can log in to Bastionhost by using a dedicated client to perform simple O&M operations and asset management. |
|  | H5 O&M protocols | Supports multiple H5 O&M protocols and methods: SSH, Telnet, Rlogin, RDP, VNC, FTP, SFTP, and X11. You do not need to use on-premises O&M client tools. |
|  | H5 file transfer | In H5 O&M mode, you can use RDP or SSH to transfer files online over a web page, without the need to use third-party client tools. |
|  | H5 session collaboration | The H5 O&M mode supports online session collaboration. O&M engineers can invite Bastionhost users to operate and maintain the same session together. The number of invitees is unlimited, but a single invitation link can invite only one user. |
|  | Session collaboration operations | The session collaboration feature allows you to view collaboration engineers in real time on the O&M page. The initiator can assign control rights online and remove collaboration engineers in real time. Session collaborators can proactively apply for control over the current session, and can manage the session after the session initiator grants the permission. |
|  | Session collaboration audit | During session audit, related O&M information is recorded for collaborative sessions, such as the invitee account, invitation reason, and operations. |
|  | Login from client tools | To log in to Bastionhost from a client, use an on-premises client tool such as Mstsc, Xshell, SecureCRT, PutTTY, WinSCP, and Xftp to log in to Bastionhost and access graphics, characters, SFTP devices, and FTP devices. |

Tenant-side Bastionhost Product I

| O&M methods |  |  |
|---|---|---|
|  | SSH-agent- forwarding | You can log in to the SSH server in SSH-agent-forwarding mode in scenarios where the same private key is used to log in to both Bastionhost and the SSH host. |
|  | SSH login | You can log in to an SSH asset by using a password or a public key, and send environment variables such as O&M user information and O&M source IP addresses to the asset. |
|  | Automatic login to multiple character hosts | Supports login to multiple character devices at the same time: Bastionhost can automatically generate SecurCRT or Xshell batch login files, which enable automatic login to multiple devices from a tool at the same time. |
|  | Batch login | Supports login to multiple host assets that use different protocols at the same time. You can also select a login method for different assets. For example, you can perform H5 O&M on all assets, or perform H5 O&M on Asset A but local O&M on Asset B. |
|  | Batch login mode | Provides an interactive dialog box during batch logins. Then, you can select the default login mode or a custom login mode (uses the same account and O&M protocol). |
|  | Recent O&M | Records the most recent hosts for quick O&M. |
|  | Automatic login to hosts for domain users | In an AD or LDAP environment, AD or LDAP users of Bastion can use their passwords to directly log in to hosts. |
|  | Limits on the number of sessions | Allows you to limit the number of user sessions. You can specify the maximum number of sessions that a user can maintain at a time. |
|  | Session information display | Displays the information about connected sessions of a host. |
|  | Tree view | Displays available O&M hosts in a tree view. You can also classify hosts into different groups and adjust the order of groups. Provides the tree view configured by the administrator so that you do not need to configure a view. |
|  | O&M favorites | Allows you to add frequently used O&M hosts to Favorites so that you can quickly find them. |

Tenant-side Bastionhost Product I

| Automated tasks | Task orchestration | Supports the automatic orchestration feature, which allows you to orchestrate actions to perform scheduled or periodic automated O&M on assets. Supported actions include file upload, command execution, and file download. The actions are executed in the specified sequence. You can use this feature to perform common O&M tasks, such as upgrades and inspections. |
|---|---|---|
|  | Task orchestration management | During automated orchestration, you can enable or disable a single action, enable or disable manual confirmation after the execution of a single action, and specify whether to push the result by email. |
| Audit management | O&M audit log | Supports online monitoring and real-time blocking on O&M sessions. Supports video playback at a certain speed from 0.5 to 64. Record the following information about O&M sessions: start time, end time, source users, source IP addresses, accessed servers, protocol or application types, commands, and operations such as file uploading, downloading, deletion, and modification. |
|  | Real-time monitoring | Supports real-time monitoring on O&M sessions. Supports real-time monitoring on file transfer sessions. |
|  | RDP transcript | Supports recording, searching, and positioning of RDP screen texts, title windows, keyboard inputs. |
|  | SQL records | Supports auditing on SQL statements used for O&M on mainstream databases, such as DB2, Oracle, MySQL, SQL Server, Postgres, GBase 8a, KingbaseES, and Dameng. |
|  | Self-review on O&M sessions | Allows O&M users to query their O&M audit sessions. This reduces the workload of audit administrators and helps O&M users improve O&M efficiency. |
|  | SSH and SFTP file transfer audit | Stores the sz and rz commands of SSH (ZMODEM transmission) and original files transferred over SFTP or FTP. |
|  | RDP file transfer audit | Stores the original files transferred by using the RDP pasteboard or disk mapping. |

Tenant-side Bastionhost Product I

|  | File retention | Retains uploaded and downloaded files, limits the size of transferred and stored files, and generates SHA1 values for transferred files. |
|---|---|---|
|  | Log archiving | Automatically archives audit data over SFTP or FTP. You can also query whether the data is archived on the page. During the archiving process, you can specify the time for automatic archiving, the speed limit for transmitting archived files, and automatic data deletion after archiving. The archived data can be viewed offline by using a dedicated player. |
| O&M reports | Built-in reports | Provides built-in analysis reports from different dimensions, such as the number of O&M operations, duration, O&M duration, active O&M duration, session size, number of character commands, number of transferred files, number of source IP addresses, and O&M time distribution. You can also view the global values, average values, maximum values, minimum values, data of a single O&M operation, and data of a single session. |
|  | Report templates | Provides various built-in report templates. You can click on a desired line chart for data drilling and analysis, and export data to PDF, DOC, and HTML files. |
|  | Custom reports | Automatically analyzes statistics and generates custom reports based on the conditions that you specify. |
|  | Report subscription | Allows you to subscribe to reports. You can customize the report content and recipients of the subscription and the time interval at which you want the system to send reports. |
|  | Limits on the O&M idle time | Allows you to limit the idle time period for all O&M sessions. |
|  | Protocols and ports | Supports custom ports for the proxy protocols of Bastionhost. |
|  | Limits on source IP addresses | Allows you to allow or block logins from specific IP addresses to Bastionhost. You can configure an IP blacklist or whitelist. |
|  | System configuration backup | Automatically backs up system configuration files to FTP or SFTP servers. You can specify the time interval for backup. |

Tenant-side Bastionhost Product I

| System configuration requirements |  |  |
|---|---|---|
|  | System self- review | Supports self-auditing, including but not limited to the following check items: system status, login logs, user logs, asset logs, policy operation logs, audit logs, configuration logs, maintenance logs, and O&M logs. |
|  | System log reports | Supports system log reports, including but not limited to the following statistical items: login logs, configuration logs, O&M access logs, and ticket reports. You can also export the reports. |
|  | Custom settings | Supports the following system languages: simplified Chinese, English, and traditional Chinese. You can specify whether to allow users to switch languages and customize the logo of the Web management console. |
|  | Alerting | Sends Bastionhost alerts and the Bastionhost status. Sends alert logs through emails, Syslog, and DingTalk. You can also specify log priorities. |
|  | Troubleshootin g | Provides troubleshooting tools such as ping, TCP port probing, UDP port probing, route tracing, and packet capturing by using the tcpdump command. |
|  | Storage management | Supports NFS and CIFS storage. Supports video storage in Object Storage Service (OSS). |
| Deployment requirements | Deployment on dual servers | Supports HA deployment and active-active deployment. Audit data can be automatically synchronized between servers. |

Tenant-side Bastionhost Product I Tenant-side Bastionhost Product I

## Benefits

**Enhances transparency in the operational process**

Multiple individuals perform O&M tasks on hosts each day. An administrator has limited visibility into the operations performed by O&M engineers on the assets, which may include potential violations or errors. Monitoring the operations of external personnel in real-time is also challenging. This lack of oversight makes it difficult to identify the responsible party when an O&M security incident occurs. Bastionhost provides comprehensive O&M audit and supports real-time monitoring during O&M. After an O&M session ends, you can replay videos to audit all O&M operations.

**Reduces costs of asset account management**

A larger number of hosts indicates a larger number of host accounts. A single host may have multiple accounts. A host account may be shared among multiple individuals. An individual may have permissions on multiple host accounts. Different individuals may simultaneously have permissions on multiple host accounts. As a result, administrators cannot track the relationship between accounts and individuals, and concerns regarding potential data leaks arise due to the presence of temporary accounts. Bastionhost allows you to manage assets and asset accounts. You can configure authorization rules to manage asset O&M permissions and reduce management costs. You can also configure multiple access control policies to prevent unauthorized access.

**Improves O&M efficiency**

As the number of host accounts continues to increase, the management and regular change of passwords have become challenging tasks for administrators. Ensuring password complexity and periodic changes are essential. However, manual changes can significantly increase workload. Various host types require different login methods. For Linux and UNIX operating systems, character client tools are required, while the Windows operating system requires remote desktop connection tools. Web systems can be accessed by using browsers, and databases require database client tools in most cases. Bastionhost provides multiple O&M methods. You can directly access assets by using web pages or by using Bastionhost Assistant for access from on-premises clients. Bastionhost helps O&M engineers perform operations on multiple assets. This greatly improves O&M efficiency.

**Controls high-risk O&M operations**

O&M engineers may perform unintentional operations that cause data loss or service failures. Attackers can also remotely access hosts and engage in data theft or tampering. To ensure precise control, administrators must implement refined policies across multiple hosts to control intentional and unintentional high-risk operations. Bastionhost allows you to configure command control policies to block sensitive operations, such as high-risk command execution, that may occur in real time during O&M. You can adjust the policies based on your business requirements to control high-risk operations in an efficient manner.

**Meets compliance requirements**

Currently, numerous standards, laws, and regulations, in and outside China, mandate organizations to establish audit systems for security management. The systems must ensure that audit information is secure, comprehensive, accessible, and unique. Multi-Level Protection Scheme (MLPS) requires user identification, permission isolation, data audit, log records, and audit reports. Tenant-side Bastionhost Product I The ISO 27001 standard mandates organizations to record user access, incidents, and information security events to investigate and collect evidence for security incidents. The Sarbanes-Oxley (SOX) Act mandates organizations to establish and enforce suitable policies to ensure the reliability and trustworthiness of financial statement data. Enterprise internal control standards mandate enterprises to adhere to the requirements. This helps enhance and standardize internal control practices and improve risk prevention capabilities. Tenant-side Bastionhost Product I

## Scenarios

**Centralized management of assets to resolve scattered asset**

**issues**

Bastionhost can manage multiple types of assets, such as hosts, databases, and applications. Bastionhost can automatically discover assets, host asset accounts, and manage different asset access permissions to prevent unauthorized access.

**Various O&M methods for complex scenarios such as**

**automated O&M**

Bastionhost adapts to the O&M habits of different O&M engineers. Bastionhost is compatible with various client tools, including Xshell, SecureCRT, MobaXTerm, Microsoft Terminal Services Client (MSTSC), VNC Viewer, Putty, winscp, flashFXP, SecureFX, and OpenSSH. Bastionhost also supports the following O&M methods: Web page-based O&M: suitable for O&M engineers who prefer to use web pages to log in to hosts. Client-based O&M: suitable for O&M engineers who prefer to use local client tools to access Bastionhost and then connect to the required hosts. Bastionhost supports batch O&M tasks and can simultaneously execute scripts and commands on multiple hosts. This improves O&M efficiency.

**Comprehensive O&M management and audit to meet internal**

**audit and compliance requirements**

Bastionhost supports features, such as user identity authentication, access permission management, and O&M operation audit, to help enterprises build internal audit processes and comply with classified protection requirements.
