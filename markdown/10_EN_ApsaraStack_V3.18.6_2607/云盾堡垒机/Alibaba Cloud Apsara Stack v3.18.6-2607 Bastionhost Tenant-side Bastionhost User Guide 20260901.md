---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Bastionhost Tenant-side Bastionhost User Guide 20260901"
product_version: "V3.18.6_2607"
doc_version: "20260901"
pdf_pages: 149
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Bastionhost Tenant-side Bastionhost User Guide 20260901.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%91%E7%9B%BE%E5%A0%A1%E5%9E%92%E6%9C%BA/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Bastionhost%20Tenant-side%C2%A0Bastionhost%20User%20Guide%2020260901.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Bastionhost Tenant-side Bastionhost User Guide 20260901

## Introduction

**Overview**

Bastionhost provides a centralized management solution based on the account, authentication, authorization, and audit. Bastionhost supports identity management, authorization management, two-factor authentication, real-time session monitoring and disconnection, audit video playback, and query of high-risk commands. This enhances the security of O&M management. Bastionhost can help meet the requirements of various laws, regulations, and policies, including the requirements of classified protection, China Banking and Insurance Regulatory Commission (CBIRC), China Securities Regulatory Commission (CSRC), PCI Security Standards Council (PCI SSC), and internal management of enterprises.

**User roles and permissions**

This topic describes the user roles and permissions of Bastionhost.

| Permission | Super administrat or | System administrat or | Security administrat or | Security auditor | Regular user |
|---|---|---|---|---|---|
| O&M | √ | - | - | - | √ |
| Tickets | √ | - | √ (Only ticket review is supported.) | - | √ (Only ticket applications are supported.) |
| Overview | √ | √ | √ | √ | - |
| Users | √ | √ | - | - | - |
| Assets | √ | - | √ | - | - |
| Accounts | √ | - | √ | - | - |
| Authorization | √ | - | √ | - | - |
| Policies | √ | - | √ | - | - |
| Audit | √ | - | - | √ | - |
| Configuration s | √ | √ | - | - | - |

| System settings | √ | √ | - | - | - |
|---|---|---|---|---|---|

### Overview

Bastionhost provides a centralized management solution based on the account, authentication, authorization, and audit. Bastionhost supports identity management, permission management, two-factor authentication, real-time session monitoring and disconnection, audit video playback, and query of high-risk commands. This enhances the security of O&M management. Bastionhost can help meet the requirements of various laws, regulations, and policies, including the requirements of classified protection, China Banking and Insurance Regulatory Commission (CBIRC), China Securities Regulatory Commission (CSRC), PCI Security Standards Council (PCI SSC), and internal management of enterprises.

### Usage limits

This topic describes the usage limits of Bastionhost.

**Network limits**

You need to ensure the connectivity between clients and the bastion host and between the bastion host and servers. Security group authorization limits: A virtual private cloud (VPC) allows a maximum of 20 security group authorization rules. Exceeding this limit may result in authorization failures between the bastion host and ECS groups, which affects O&M access. Ensure that the number of security group authorization rules does not exceed the limit, or manually configure access rules using IP addresses. . A bastion host does not support direct public network access. A standard DNAT solution must be used for translation. For more information, see **User Guide > Best practices >**
**Configure a DNAT entry to access a bastion host over the Internet**. .
The maximum internal bandwidth for the virtual IP address (VIP) of a single bastion host is 5 Gbit/s.

**Concurrency performance limits**

Concurrency performance limits vary based on the edition and specifications of a bastion host. To maintain stable operations, ensure that your concurrent sessions remain within the specified limits. Exceeding these thresholds may result in service lag, unavailability, or interruptions. For more information about the concurrency performance of specific instance specifications, see configurations in the console or submit a ticket.

**Important**

If a session contains multiple TCP connections, each TCP connection consumes a concurrent session quota. In RDP-based O&M, a single connection consumes more underlying resources than an SSH-based session.

**Environment Limits for SSH O&M Auditing**

A bastion host supports SSH auditing exclusively for standard bash, zsh, ksh, and dash shells. Assets running non-standard shells may experience compatibility issues with O&M and audit command extraction.

**Limits on the length of bastion host usernames**

Due to the limits of clients, a bastion host username cannot exceed 63 characters in length during RDP-based O&M. If a username exceeds 63 characters in length, you can perform only web-based O&M on a server. We recommend that you keep the username within 63 characters.

**Limits on client versions**

The following table lists supported client tools for the bastion host single sign-on (SSO) tool. Using unsupported clients may lead to connection failures or functional unavailability.

**Supported client tools for the SSO tool**

| Protoco l | Operating system (architecture) | Supported client version for BS O&M | Supported client version for CS O&M |
|---|---|---|---|
| SSH | Windows | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 |
|   | Linux x86 | PuTTY: 0.70 | PuTTY: 0.70 |
|   | Linux ARM | PuTTY: 0.73 | PuTTY: 0.73 |
|   | macOS (x86/M1/M2) | ZOC: 8.06.3 iTerm2: 3.4.22 | ZOC: 8.06.3 iTerm2: 3.4.22 |
| Rlogin | Windows | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 |
|   | Linux x86 | PuTTY: 3.24 | PuTTY: 0.73 |
|   | Linux ARM | PuTTY: 0.70 | PuTTY: 0.73 |
|   | macOS (x86/M1/M2) | ZOC: 8.06.3 iTerm2: 3.4.22 | ZOC: 8.06.3 iTerm2: 3.4.22 |
| Telnet | Windows | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 | Xshell: 7.0 SecureCRT: 8.1.0 PuTTY: 0.8 |
|   | Linux x86 | PuTTY: 3.24 | PuTTY: 0.73 |

| enant-side e·Introduct |   |   |   |
|---|---|---|---|
|   | Linux ARM | PuTTY: 0.70 | PuTTY: 0.70 |
|   | macOS (x86/M1/M2) | ZOC: 8.06.3 | ZOC: 8.06.3 |
| FTP | Windows | Xftp: 7.0 WinSCP: 5.21.7 FileZilla: 3.66.5 FlashFXP: 5.4.0 SecureFX: 8.1.0 MobaXterm: 24.0 | Xftp: 7.0 WinSCP: 5.21.7 FileZilla: 3.66.5 FlashFXP: 5.4.0 SecureFX: 8.1.0 MobaXterm: 24.0 |
|   | Linux x86 | FileZilla: 3.69 | FileZilla: 3.69 |
|   | Linux ARM | FileZilla: 3.39 | FileZilla: 3.39 |
|   | macOS (x86/M1/M2) | FileZilla: 3.66.1 | FileZilla: 3.66.1 |
| SFTP | Windows | Xftp: 7.0 WinSCP: 5.21.7 FileZilla: 3.66.5 FlashFXP: 5.4.0 SecureFX: 8.1.0 MobaXterm: 24.0 | Xftp: 7.0 WinSCP: 5.21.7 FileZilla: not supported FlashFXP: 5.4.0 SecureFX: not supported MobaXterm: 24.0 |
|   | Linux x86 | FileZilla: 3.69 | FileZilla: 3.69 |
|   | Linux ARM | FileZilla: 3.39 | FileZilla: 3.39 |
|   | macOS (x86/M1/M2) | FileZilla: 3.66.1 | FileZilla: 3.66.1 |
| RDP | Windows | mstsc: 10.0.1 | mstsc: 10.0.1 |
|   | Linux x86 | Remmina: 1.4.2 xfreerdp: 2.11 | Remmina: 1.4.2 xfreerdp: 2.11 |

|   | Linux ARM | Remmina: 1.4.10 xfreerdp: 2.0.0 | Remmina: 1.4.10 xfreerdp: 2.0.0 |
|---|---|---|---|
|   | macOS (x86/M1/M2) | Microsoft Remote Desktop app: 10.8.4 | Microsoft Microsoft Remote Desktop app:10.8.4 |
| X11 | Windows | TigerVNC: 1.13 RealVNC: 7.10.0 TightVNC: 2.8.81 | Not supported |
|   | Linux x86 | VNC Viewer: 7.13 |   |
|   | Linux ARM | VNC Viewer |   |
|   | macOS (x86/M1/M2) | RealVNC: 7.5.1 |   |
| VNC | Windows | TigerVNC: 1.13 RealVNC: 7.10.0 TightVNC: 2.8.81 | Not supported |
|   | Linux x86 | VNC Viewer: 7.13 |   |
|   | macOS (x86/M1/M2) | RealVNC: 7.5.1 |   |

| SQL Server | Windows | SSMS: 17.9.1 DBeaver: 24.0.0 Navicat Premium: 15.0 Navicat for SQL Server: 12.0 SqlDbx Professional: 6.16 DbVisualizer: 24.2.1 Note SSMS V18 and later support only tunnel O&M. You cannot modify the session title in SSMS, SQLWB, and SqlDbx Professional. | Not supported |
|---|---|---|---|
|   | Linux x86 | DbVisualizer: 24.1.6 |   |
|   | Linux ARM | DbVisualizer: 24.3.3 |   |
|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 |   |
| MySQL | Windows | MySQL Workbench DbVisualizer: 9.5.7 DBeaver: 24.0 MySQLFront: 6.0 Navicat Premium: 15.0 Navicat for MySQL: 12.0 HeidiSQL: 11.3.0 | Not supported |
|   | Linux x86 | DbVisualizer: 24.1.6 DBeaver: 23.3 |   |
|   | Linux ARM | DbVisualizer: 24.3.3 |   |
| 6 |   |   | > Document Version: 2026090 |

|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 |   |
|---|---|---|---|
|   | Windows | Toad: 12.1.0 PL/SQL Developer: 14.0.6 (with a driver of 19c and a client of 19c) DbVisualizer: 24.2 DBeaver: 24.0 Navicat Premium: 15.0 Navicat for Oracle: 12.0.29 SQLDbx Professional: 6.16 SQL Developer: 20 |   |
| Oracle |   |   | PL/SQL Developer: 14.0.6 (with a driver of 19c and a client of 19c) DbVisualizer: 24.2 DBeaver: 24.0 Navicat Premium: 15.0 |
|   | Linux x86 | DbVisualizer: 24.1.6 DBeaver: 23.3 | Not supported |
|   | Linux ARM | DbVisualizer: 24.3.3 | Not supported |
|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 | Not supported |
| Db2 | Windows | DbVisualizer: 9.5.7 DBeaver: 24.0 Toad for DB2: 7.10 db2cmd: 11.5.8 Quest Central: 4.8.1 | Not supported |
|   | Linux x86 | DbVisualizer: 24.1.6 DBeaver: 23.3 |   |
|   | Linux ARM | DbVisualizer: 24.3.3 |   |
|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 |   |

| PostgreS QL | Windows | DbVisualizer: 9.5.7 DBeaver: 24.0 Navicat Premium: 15.0 SqlDbx Professional: 6.16 Navicat for PostgreSQL: 16.3.3 pgAdmin 3: 1.8.4 | Not supported |
|---|---|---|---|
|   | Linux x86 | DbVisualizer: 24.1.6 DBeaver: 23.3 |   |
|   | Linux ARM | DbVisualizer: 24.3.3 |   |
|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 |   |
| Kingbas eES | Windows | DbVisualizer: 9.5.7 KStudio: 2.0 | Not supported |
|   | Linux x86 | DbVisualizer: 24.1.6 |   |
|   | Linux ARM | DbVisualizer: 24.3.3 |   |
|   | macOS (x86/M1/M2) | DbVisualizer: 24.1.6 |   |
| DM Databas e | Windows | DbVisualizer: 9.5.7 | Not supported |
| GBase 8s | Windows | GBase Data Studio: 8.5.24 (This version encounters the same issue in both direct connection and BS O&M, whereas version 9.5.2 works correctly.) DBeaver: 24.0 DbVisualizer: 24.2.1 | Not supported |
| GBase 8s | Windows | GBase Data Studio: 8.5.24 DbVisualizer: 24.2.1 | Not supported |
| MariaDB | Windows | DBeaver: 24.0 | Not supported |

| TiDB | Windows | DBeaver: 24.0 | Not supported |
|---|---|---|---|
| GaussDB | Windows | DBeaver: 24.0 TPDSS: 2.23 | Not supported |
| Informix | Windows | DBeaver: 24.0 | Not supported |
| Redis | Windows | Another Redis Desktop Manager: 1.66.6 | Not supported |
| MongoD B | Windows | MongoDB Compass: 1.43.4 | Not supported |
| HighGo | Windows | HGDB Developer: 6.1 DBeaver: 24 | Not supported |
|   | Linux x86 | HGDB Developer: 6.1 |   |

**OSes supported by application servers**

| Operating system | Version |
|---|---|
| Windows | Windows Server 2016 Windows Server 2019 Datacenter |
| Linux | UOS V20 Server (x86 and ARM versions) Kylin V10 (x86 and ARM versions) Anolis OS (x86 and ARM versions) |

**Note**

You need to prepare the system version and license of the application publishing server.

### User roles and permissions

This topic describes the user roles and permissions of Bastionhost.

| Permission | Super administrat or | System administrat or | Security administrat or | Security auditor | Regular user |
|---|---|---|---|---|---|

| O&M | √ | - | - | - | √ |
|---|---|---|---|---|---|
| Tickets | √ | - | √ (Only ticket review is supported.) | - | √ (Only ticket applications are supported.) |
| Overview | √ | √ | √ | √ | - |
| Users | √ | √ | - | - | - |
| Assets | √ | - | √ | - | - |
| Accounts | √ | - | √ | - | - |
| Authorization | √ | - | √ | - | - |
| Policies | √ | - | √ | - | - |
| Audit | √ | - | - | √ | - |
| Configuration s | √ | √ | - | - | - |
| System settings | √ | √ | - | - | - |

### Log on to the Apsara Uni-

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, you must obtain the endpoint of the console from the deployment personnel. To configure the Cloud Security system, you must log on with a global organization security administrator account. We recommend that you use the Google Chrome browser.

**Procedure**

1. In the address bar of your browser, enter the endpoint of the Apsara Uni-manager
Management Console and press Enter.
2. Enter the correct username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

**First logon**

The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. Follow the instructions to complete the password change. For security purposes, the password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ! @ # $ %

**Forgot password**

If you forgot your password, click Forgot Password and enter the username of your account, the email address that was used to create your account, and the verification code. Then, a URL is sent to the specified email address. You can click the URL to reset the password.
3. Click **Log On**.
4. If your account has MFA (Multi-Factor Authentication) enabled, perform the following
operations based on your scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the instructions to bind an MFA device. b. Re-enter your username and password as described in Step 2, and click **Log On**. c. Enter the 6-digit MFA code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter the 6-digit MFA code and click **Authenticate**.

**Note**

For information about how to bind and enable MFA, see the **Security Center** >
**Multi-factor Authentication** > **Manage Multi-factor Authentication** section in
the Apsara Uni-manager Management Console User Guide.

## Create a bastion host

This topic describes how to create a bastion host.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **O&M Audit** > **Tenant-side Bastionhost**.
3. On the **Tenant-side Bastionhost** page**,** select a region from the **Region** drop-down list
**and** click **Access with Authorized Role.**
4. Click **Create Instance** and configure the parameters.

| Parameter | Description |
|---|---|
| Organization | The organization to which the bastion host belongs. It cannot be modified after the bastion host is created. |
| Resource Set | The resource set to which the bastion host belongs. It cannot be modified after the bastion host is created. |
| VPC ID | The virtual private cloud (VPC) to which the bastion host belongs. It cannot be modified after the bastion host is created. Important After the bastion host is created, make sure that access rules are configured for all security groups in the VPC to allow access from the bastion host. Otherwise, the bastion host may fail to access the Elastic Compute Service (ECS) instance. |
| Support for High Availability | Disabled: The disaster recovery feature is disabled. Single Data Center: Disaster recovery in a single data center is supported. Dual Data Center: The system automatically detects the environment. This option is displayed when the system supports two data centers. |

| vSwitch ID | The ID of the vSwitch to which the bastion host belongs. It cannot be modified after the bastion host is created. Important The bare metal dedicated vSwitch is dimmed and cannot be selected. Different scenarios require varying numbers of IP addresses. Make sure that the vSwitch has sufficient IP addresses. This ensures that the bastion host can be created and upgraded. A standalone bastion host requires two IP addresses. A single-data center high-availability deployment requires three IP addresses. A dual-data center high-availability deployment requires two vSwitches. One vSwitch requires one IP address, and the other vSwitch requires two IP addresses. |
|---|---|
| Edition | Select a specification based on the number of your assets. Valid values: Basic Edition (Assets: Less Than 200) Standard Edition (Up to 600 Assets) Advanced Edition (Up to 2,000 Assets) Premium Edition (Up to 5,000 Assets) |
| Asset Quota | Select the number of authorized assets. When you create a bastion host, you can specify the maximum number of assets that can be managed by the bastion host. The total number of assets that can be managed by your bastion host depends on the value that you specify for the Asset Quota parameter when you create the bastion host. To increase or decrease the asset quota for a bastion host, log in to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Product Operation > Security O&M > Cloud Shield Operations Center. In the left-side navigation pane, choose Cloud Services > OEM O&M > Permissions. On the page that appears, specify the minimum asset quota. For more information, see the Security Administrator Guide. |

5. Click **OK**.

## Log on to Bastionhost

### Log in to Bastionhost from the

**Apsara Uni-manager Management**

**Console**

This topic describes how to log in to Bastionhost from the Apsara Uni-manager Management Console.

**Important**

After a bastion host is initialized, log in to the bastion host from a browser at your earliest opportunity to change the initial password of the admin user.

**Procedure**

1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **O&M Audit** > **Tenant-side Bastionhost**.
3. On the **Tenant-side Bastionhost** page**,** select a region from the **Region** drop-down list
**and** click **Access with Authorized Role.**

### Log on to Bastionhost from a

**browser**

This topic describes how to log on to Bastionhost.

**Prerequisites**

The client that you use can access Bastionhost. The access address of Bastionhost is obtained from the system deployment personnel. The username and password of Bastionhost are obtained from the system deployment personnel. The following table describes the basic roles in Bastionhost.

| Role | Description |
|---|---|
| Super administrator | Super administrator: admin. Note If you use the super administrator admin, you must log on to Bastionhost from Apsara Stack Security Center. For more information, see Log on to Bastionhost from Apsara Stack Security Center. |

| Audit administrator | An audit administrator can use this account to audit O&M operations. This account is created by the super administrator on the User page. |
|---|---|
| System administrator | A system administrator can use this account to manage Bastionhost. This account is created by the super administrator on the User page. |
| O&M engineer | An O&M engineer can use this account to manage hosts. This account is created by the super administrator on the User page. |

**Procedure**

1. Open a browser. We recommend that you use Microsoft Edge, Google Chrome 69, or Firefox
65 or later.
2. In the address bar of the browser, enter the https://IP address of Bastionhost and press the
Enter key.
3. Enter the username and password and click **Login**.

**Note**

The first time you use admin to log on to Bastionhost, you are redirected to the password change page. Before you can access Bastionhost, you must change your password. If password change upon next logon is configured for other users, the users must change passwords the first time they log on to Bastionhost. The first time you log on to Bastionhost, we recommend that you specify an email address or a mobile phone number. If you forget your password, you can retrieve your password by using the email address or mobile phone number.
4. **Optional**. If two-factor authentication is configured, enter a verification code and click
**Confirm**.

## Introduction to the

### homepage

**Overview**

The homepage is a visual, concise, and easy-to-use web page, which contains five major sections, as shown in the following figure. The following table describes the features of each section.

| No. | Section | Description |
|---|---|---|
| ① | Service name | Displays the logo of Alibaba Cloud. This section is displayed only when you log on to Bastionhost from a browser. |
| ② | Console switchover section | Provides an icon to switch between the personal workbench and management console. |
| ③ | User information section | Provides quick entry points for viewing remote tasks and internal messages, managing personal information about the current logon user, changing the password of the user, switching between languages, and downloading tools. This section is displayed only when you log on to Bastionhost from a browser. |
| ④ | System menus | Provides entry points to configure various management features, which allows users to switch between different menus. |

| ⑤ | Operation section | Provides sub-feature menus, configuration items, operations, and displays the results of various features. |
|---|---|---|

**Manage personal information**

In the user information section, click the user information and select **Personal Information** to go to the Information page of the personal workbench. You can change the name, mobile phone number, and email address of the current logon user. You can also bind a one-time password (OTP) device, a Client/Server (C/S) logon password, an SSH public key, an SSH private key, and a Pretty Good Privacy (PGP) public key to the user. image.png

**Change the password**

1. In the user information section, click the user information and select **Change Password**.
image.png
2. Enter the original password and the new password. Then, confirm the new password and
click **Confirm**. image.png

**Switch between languages**

In the user information section, click the user information and select a language next to
**Switch Language**.
image.png

**Download tools**

1. In the user information section, click the user information and select **Download Tool**.
2. On the **Tool** page, download O&M audit tools, such as Bastionhost Assistant and the Google
Chrome plug-in of auto-fill scripts for web applications. image.png

**Log off from Bastionhost**

In the user information section, click the user information and select **Log Off**. In the message that appears, click **Confirm**. image.png

**View remote tasks**

In the user information section, click the icon. In the pane that appears, view the list of ongoing remote tasks. Click the Historical Tasks tab to view the list of historical remote tasks and task execution results. You can click **View All** to go to the **Logs > Operation Logs** page of the personal workbench to view the operation logs of all tasks. image.png

**View internal messages**

In the user information section, click the icon to go to the **Logs > Internal Messages** page of the personal workbench. On the Internal Messages page, you can view internal messages about ticket review, alerts, and operation logs.

**Note**

If you cannot receive internal messages, check whether internal message delivery is enabled and recipients are configured on the **System > Monitor or Alert >**
**Notifications** page in the management console.

## Management console

### Overview

The Overview page displays information such as the number of users, number of assets, number of accounts, authorization rules, O&M data, licenses, and system running status.

### Users

#### Manage users

##### Create and manage a department

This topic describes how to create, search for, and delete a department. This topic also describes how to modify the information about a department.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. On the **Department** tab, manage a department.

**Create a sub department**

By default, the system creates a root department. You can create nine levels of sub departments under the root department.
1. On the **Department** tab, move the pointer over the name of the department that you want
to manage, click the icon, and then select **Create Sub-department**.
2. Enter a name for the sub department and then click the tick (√) icon.

**Change the name of a department**

1. On the **Department** tab, move the pointer over the name of the department that you want
to manage, click the icon, and then select **Rename**.
2. Enter a new name for the department and then click the tick (√) icon.

**Search for a department**

On the **Department** tab, enter the keyword of a department name and press the Enter key or click the icon to search for the department.

**Delete a department**

On the **Department** tab, move the pointer over the name of the department that you want to manage, click the icon, and then select **Delete Department**.

**Change the level of a department**

By default, you cannot change the level of the root department. You can drag sub departments to a node to change the levels of the sub departments. On the **Department** tab, drag the sub department that you want to manage and to a destination department.

##### Create users

This topic describes how to create one or more users.

**Go to the User Management page**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. On the left side of the User Management page, click the **Department** tab. Then, create one
or more users.

**Create a single user**

1. In the **User** section on the right side of the page, click **Create**.
2. In the **Create User** panel, configure the parameters and click **Confirm**. The following table
describes the parameters.

| Parameter | Description |
|---|---|
| Username | The custom username that is used to identify the user. The username must be unique and can be up to 50 characters in length. |
| Name | The name of the user. The name can be up to 50 characters in length. |
| Platform Role | The role of the user. Different roles have different permissions. The system provides the following roles: super administrator, system administrator, security administrator, security auditor, and regular user. If the roles do not meet your requirements, you can choose Configuration > Role Configuration in the left-side navigation pane. On the Role Configuration page, create custom roles. |
| Department | The department to which the user belongs. |

| Authentication Source | The authentication mode that is used when the user logs on to Bastionhost. If you configure multiple authentication modes and the user passes the verification in one of the authentication modes, the user is allowed to log on to Bastionhost. Local Authentication: The user is verified by using the password. AD: The user is verified by using a remote Active Directory (AD) server. You can create multiple AD server instances. LDAP: The user is verified by using a remote Lightweight Directory Access Protocol (LDAP) server. RADIUS: The user is verified by using a remote Remote Authentication Dial-In User Service (RADIUS) server. CAS: The user is verified by using a Central Authentication Service (CAS) server. SAML: The user is verified by using a Security Assertion Markup Language (SAML) server. JWT: The user is verified by using a JSON Web Token (JWT) server. DING TALK: The user is verified by using DingTalk. _ WECHAT WORK: The user is verified by using WeCom. _ You must enable and configure each authentication server on the Authentication Source tab of the Configuration > User Configuration page. |
|---|---|
| Local Password | If you set the Authentication Source parameter to Local Authentication, you must configure a logon password for the user. You can click Automatic Generation to obtain a random password. You can also enter a password in the field based on the password complexity requirements. |
| You must change the password upon next logon | If you set the Authentication Source parameter to Local Authentication and select this option, the user must change the password the first time the user logs on to Bastionhost from a browser. |
| The password is sent to the specified email address or mobile phone number | If you set the Authentication Source parameter to Local Authentication and select this option, the system sends the password to the email address or mobile phone number of the user. If you want the system to send the password to the email address of the user, make sure that email server settings are complete and the email address is specified for the user. If you want the system to send the password to the mobile phone number of the user, make sure that the settings of a text message gateway are complete and the mobile phone number is specified for the user. |
| Synchronization Source | The synchronization source of the user, which is used to synchronize the user on the remote AD or LDAP server to Bastionhost. You must enable and configure an AD server or LDAP server on the Authentication Source tab of the Configuration > User Configuration page. |

| Security Configuration | Status: Enable: The user is allowed to log on to Bastionhost. Disable: The user is not allowed to log on to Bastionhost. Multi-factor Authentication: Follow System: The multi-factor authentication (MFA) configuration of the system is used. Custom: The selected MFA modes are used. If you configure multiple MFA modes and the user passes the verification in one of the modes, the user is allowed to log on to Bastionhost. Validity Period: Configure the validity period during which the user can log on to Bastionhost. The user cannot log on to Bastionhost outside the validity period. |
|---|---|
| User Group | The user group to which the user belongs. |
| Email Address | The email address of the user, which is used to receive system notifications and verification codes. If the user forgets the password, the user can reset the password by using the email address. We recommend that you specify at least an email address or a mobile phone number. |
| Mobile Phone Number |   |
| Remark | The remarks about the user. |
| Custom Attribute | The custom attributes of the user. This section is available only if you configure custom attributes on the Custom Attribute tab of the Configuration > User Configuration page. |

**Import multiple users at a time**

1. In the **User** section on the right side of the page, choose **Create > Import User**.
2. In the **Import** dialog box, click **Download Template File**.
3. Complete the template file as described in the file, and click **Select File** to upload the
template file.
4. Configure the parameters and click **Import**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Update User with Same Name | If you select this option, imported users overwrite existing users with the same username. If you clear this option, users with the same usernames as existing users are not imported. |

| After the import, the password is automatically sent to the specified email address or mobile phone number. | If you select this option, after a user is imported, the password is automatically sent to the email address or mobile phone number of the user. If you want the system to send the password to the email address of the user, make sure that email server settings are complete and the email address is specified for the user. If you want the system to send the password to the mobile phone number of the user, make sure that the settings of a text message gateway are complete and the mobile phone number is specified for the user. |
|---|---|

**Synchronize users from a remote server**

You can synchronize users from an AD or LDAP server to Bastionhost. In the left-side navigation pane, choose **Configuration > User Configuration**. On the
**Authentication Source** tab, add an AD server or LDAP server and select **Synchronous**
**Creation** next to **Create User** to synchronize users that are created on the server to
Bastionhost.

**What to do next**

Modify one or more users: To modify a single user, click the **Department** tab on the left side of the page. In the
**User** section, find the user that you want to manage and click **Edit** in the **Actions**
column. In the Modify User panel, modify the user information and click **Confirm**. To modify multiple users at a time, click the **Department** tab on the left side of the page. In the **User** section, select the users that you want to manage and click **Edit** above the user list. In the Batch Modify Users panel, modify the user information and click **Confirm**. Disable or enable a user: After you disable a user, the user cannot log on to Bastionhost from a browser. If a user is disabled, you must manually enable the user before the user can log on to Bastionhost from a browser. Click the **Department** tab on the left side of the page. In the **User** section, select the user that you want to manage and click **Disable** or **Enable** above the user list. In the message that appears, click Confirm. Unlock a user: If a user is locked due to multiple logon failures or inactive status for an extended period of time, you must manually unlock the user before the user can log on to Bastionhost. Click the **Department** tab on the left side of the page. In the **User** section, select the user that you want to manage and click **Unlock** above the user list. In the message that appears, click Confirm. Delete a user: Click the **Department** tab on the left side of the page. In the **User** section, select the user that you want to manage and click **Delete** above the user list. In the message that appears, click Confirm.

##### Search for users

This topic describes how to search for users in the current department or user group.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. In the User section of the **Department** or **User Group** tab, click **Open**, enter the search
conditions, and then click **Search**. Click **Reset** to clear the search conditions. Click **Save** to save the current search conditions as saved search conditions. You can use the saved search conditions to search for users in an efficient manner.

##### Export users

This topic describes how to export user information to your computer.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. In the User section of the **Department** or **User Group** tab, click the
icon.
5. In the **Export** dialog box, configure the Export Range and Encryption Password parameters
and click **Export**. All: exports all user information. Selected: exports information about the selected users. You must select the assets before you click Export. The encryption password is used to encrypt the ZIP file when you export the file. This ensures the security of the file. We recommend that you specify an encryption password.

##### Create and manage a user group

This topic describes how to create and manage a user group.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. On the **User Group** tab, manage a user group.

**Create a user group**

1. On the **User Group** tab, click the
icon.
2. In the **Create User Group** panel, configure the Name and Department parameters and
click **Confirm**.

**Modify a user group**

1. On the **User Group** tab, move the pointer over the user group that you want to manage,
click the icon, and then select **Edit**.
2. In the **Modify User Group** panel, enter a new name for the user group and click **Confirm**.

**Search for a user group**

On the **User Group** tab, enter the keyword of a user group name, and then press the Enter key or click the icon to search for the user group.

**Delete a user group**

On the **User Group** tab, move the pointer over the user group that you want to manage, click the icon, and then select **Delete**.

**Add a user to a user group (method 1)**

1. On the **User Group** tab, select the user that you want to manage and click **Join Group** in
the **User** section.
2. In the **Join User Group** panel, select the user group to which you want to add the user and
click **Confirm**.

**Add a user to a user group (method 2)**

1. On the **User Group** tab, select the user group that you want to manage and click **Add**
**User Group Member** in the **User** section.
2. In the **Select User** panel, select a user and click **Confirm**.

**Remove a user from a user group**

On the **User Group** tab, select a user and click **Remove from Group** in the **User** section.

##### Configure fields of the user list

Bastionhost allows you to flexibly configure the fields that are displayed in the user list.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > User Management**.
4. Click the **Department** or **User Group** tab on the left side of the page. In the User section,
click the icon. Select the fields that you want to display and click **Confirm**.

#### Manage OTP tokens

##### Import a token file

This topic describes how to import a token file.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > OTP Management**.
4. Click **Import Token** to select and upload a token file from your computer.

**What to do next**

After you import a token file, you can perform the following operations: Disable a token: Select the token that you want to manage and click **Disable** above the token list. Enable a token: Select the token that you want to manage and click **Enable** above the token list. Report the loss of a token: Select the token that you want to manage and click **Mark as**
**Lost** above the token list.
Unbind a token: Select the token that you want to manage and click **Unbind** above the token list. Delete a token: Select the token that you want to manage and click **Delete** above the token list.

##### Search for a token

This topic describes how to search for a token that meets the search conditions.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > OTP Management**.
4. Enter or select a search condition in a search field and click **Search**.

##### Bind a token to a user

After you create a token, you must authorize the token file to the user.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > OTP Management**.
4. Find the token that you want to manage and click **Bind User** in the **Actions** column.
5. In the **Select User** panel, select a user and click **Confirm**.

##### Synchronize a token

If a time difference exists between Bastionhost and your one-time password (OTP) device and you cannot obtain a password in real time, you can synchronize a token.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > OTP Management**.
4. Find the token that you want to manage and click **Synchronize Token** in the **Actions**
column.
5. In the **Synchronize Token** dialog box, enter the current and next tokens obtained from
the OTP device and click **Confirm**.

#### Third-party OTP token management

##### Import a token

This topic describes how to import a third-party One-Time Password (OTP) token.

**Prerequisites**

The **third-party OTP SERVER** is configured in the **Detailed Configuration** section of the

**Management Console > Configuration > User Configuration > Multi-factor**

**Authentication** tab.

**Import a token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. In the upper-left corner of the page, click **Import Token**.
5. In the **Import Token** panel, select the serial number of the token to be imported and click
**Confirm**.
6. Return to the token list to view the token you imported.

##### Bind a token to a user

After a token is imported, you need to bind it to a user. After the binding is complete, the user can use the token to log in. This topic describes how to bind a token to a user.

**Prerequisites**

The third-party OTP SERVER is set to JN TASS. For more information, see **Configure MFA** in
**Management console > Configuration > User configuration** of this user guide.

**Bind a token to a user**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. Find the token that you want to manage and click **Bind User** in the **Actions** column.
5. On the **Select User** tab, select the user to which you want to bind the token and click **OK**.
After the binding is complete, the value of **Binding Status** is **Bound**.

##### Unbind a token

This topic describes how to unbind a token from a user. After the token is unbound, the user can no longer use the token to log in.

**Unbind a token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. In the token list, select the token that you want to unbind and click **Unbind** above the list.
5. In the **Unbind** dialog box, confirm the settings and click **OK**.

##### Report the loss of a token

This topic describes how to report the loss of a token. After a token is reported as lost, it cannot be used until the administrator re-enables it.

**Report the loss of a token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. In the token list, select the token that you want to report as lost and click **Report Loss**
above the list.
5. In the message that appears, confirm the information and click **OK**.

##### Disable/Enable a token

This topic describes how to enable or disable a token.

**Enable or disable a token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. In the token list, select a token that you want to manage and click **Enable** or **Disable**
above the list.
5. In the **Enable** or **Disable** message, confirm the settings and click **OK**.

##### Delete a token

This topic describes how to delete a token.

**Delete a token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **User > Third OTP Token Management**.
4. In the token list, select the token that you want to delete and click **Delete** above the list.
5. In the **Delete** message, confirm the settings and click **OK**.

### Assets

#### Manage assets

You can use nodes to implement hierarchical asset management.

**Create a node**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Asset > Asset Management**.
4. In the **Node** section, move the pointer over the name of the node that you want to manage,
click the icon, and then select **Create Child Node**.
5. Enter a name for the child node in the field that appears and click the
icon on the right to create the child node. To change the level of a node, move the pointer over the node and drag the node to the destination node. To change the name of a node, move the pointer over the node name, click the icon, and then select **Rename**. Then, you can enter a new name. To delete a node, move the pointer over the node name, click the icon, and then select
**Delete Node**. In the Delete Node message, click Confirm.

**Create one or more assets**

**Create a single asset**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Asset > Asset Management**.
4. In the **Assets** section, click **Create**. In the **Create Asset** panel, select an asset template
and click **Next**.
5. In the **Asset Information** step, configure the parameters and click **Next**. The following
table describes the parameters.

| Parameter | Description |
|---|---|
| Asset Type | The type of the asset. Valid values: Regular Asset, Domain Control, and Domain Member. |
| Asset Name | The name of the asset, which is used only for identification. The name can be up to 30 characters in length. |
| IP or Domain | The IP address of the asset. You can configure an IPv4 address, an IPv6 address, or a domain name. |
| Network | The network to which the asset belongs. Default value: default. |
| Node | The node to which the asset belongs. |

| Remark | The remarks of the asset. |
|---|---|
| Custom Attribute | The custom attributes of the asset. You can create custom attributes. |

6. Configure an account and click **Confirm**.
To create an account, click **Add**. In the **Add Asset Account** panel, configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Account Type | The type of the account. Valid values: Local Account and Domain Account. Domain Account is available only if you select Domain Control for the Asset Type parameter in the Asset Information step. Only Local Account is available for other asset types. |
| Account Name | The name of the account. The name can be up to 64 characters in length. |
| Privileged Account | If you select this check box, the account is identified as a privileged account and can be used in the following scenarios: You can use the privileged account to change the password of a regular account. If the account uses the SSH protocol, the password of the account can be automatically changed. If the password fails to be automatically changed, you can use the privileged account to change the password. If the account uses the RDP protocol, you must use the privileged account to change the password of the account. If you create an account whose protocol is SSH or RDP for an asset on Bastionhost, Bastionhost uses the privileged account to create the same account on the asset. If you delete the account of an asset from Bastionhost, Bastionhost uses the privileged account to log on to the asset to delete the account. You can use the privileged account to log on to the asset and identify other accounts of the asset. You can use the privileged account to obtain the information about other accounts of the asset. |
| Password | The password of the account. |
| Apply to Service | The protocol that the account uses. You can select multiple protocols. |
| SSH Key | If you set Apply to Service to SSH, you can select an SSH key for the account. Make sure that an SSH key is created in advance. |

| Connected To | If you set Apply to Service to ORACLE, you must select a connection property. |
|---|---|
| Automatic Password Change | If you select Yes, automatic password change is enabled for the account. If you select No, automatic password change is disabled for the account. |
| Password Change Script | The custom password change script for the account. |
| Switch From | If you set Apply to Service to SSH or TELNET, you must select a connection property. |
| Custom Attribute | The custom attributes of the account. |

**Import multiple assets and asset accounts at a time**

You can import multiple assets and asset accounts at a time.
1. In the **Asset** section, choose **Create > Import Asset**.
2. In the **Import** dialog box, click **Download Template File**.
3. Follow the instructions in the file to complete the template file. Then, click **Select File** to
upload the template file.
4. Configure the parameters based on your business requirements and click **Import**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Overwrite Host with Same Name | If you select this check box and the name and IP address of an imported asset are the same as the name and IP address of an existing asset on Bastionhost, the imported asset overwrites the existing asset. If you do not select this check box and the name and IP address of an imported asset are the same as the name and IP address of an existing asset on Bastionhost, the asset is not imported. |
| Immediately Change Password After Import | If you select this option, the password of the imported account is immediately changed. |

**Import an asset source**

1. In the **Asset** section, choose **Create > Import Asset Source**.
2. On the **Create Asset Source** page of the **Asset Discovery** page, create an asset source
and import assets.

**Modify the information about one or more assets**

**Modify the information about an asset**

Modify the configurations of an asset i. In the **Asset** section, find the asset that you want to manage and click **Edit** in the
**Actions** column.
ii. On the **Configure** tab, modify the parameters in the Basic Information and Advanced Configuration sections, and click **Save**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Asset Type | The type of the asset. Valid values: Regular Asset, Domain Control, and Domain Member. |
| Asset Name | The name of the asset. |
| IP or Domain | The IP address of the asset. You can configure an IPv4 address, an IPv6 address, or a domain name. |
| Network | The network to which the asset belongs. |
| Node | The node to which the asset belongs. |
| Remark | The remarks of the asset. |
| Custom Attribute | The custom attributes of the account. |
| System Code | The system code. |
| Account Switch Command | The switch command for secondary logon of the account. You can configure this parameter for accounts that use the SSH and Telnet protocols. After you use the associated account to log on to an asset, Bastionhost automatically runs this command to log on to the asset by using the account. |

Modify protocols of an asset i. In the **Asset** section, find the asset that you want to manage and click **Edit** in the
**Actions** column.
ii. On the **Service** tab, modify the port number and parameters of each protocol, enable or disable a protocol, and then click **Save**. The following table describes the parameters.

| Protocol | Parameter | Description |
|---|---|---|
| SSH | Port number | Default value: 22. |

| SFTP | Port number | Default value: 22. |
|---|---|---|
| RDP | Port number | Default value: 3389. |
| TELNET | Port number | Default value: 23. |
| RLOGIN | Port number | Default value: 513. |
| VNC | Port number | Default value: 5900. |
| FTP | Port number | Default value: 21. |
| ORACLE | Port number | Default value: 1521. |
| KINGBASE | Port number | Default value: 54321. |
| DM | Port number | Default value: 5236. |
| PostgreSQL | Port number | Default value: 5432. |
| DB2 | Port number | Default value: 5000. |
| SQLServer | Port number | Default value: 1433. |
| MySQL | Port number | Default value: 3306. |
| HTTP/HTTPS | URL | By default, the value of the parameter is empty. |
| X11 | Port number | Default value: 22. |
| Custom TCP | Port number | Default value: 0. |

Modify the information about an asset account i. In the **Asset** section, find the asset that you want to manage and click **Edit** in the
**Actions** column.
ii. On the **Account** tab, create, delete, or change an asset account. Click **Create**. In the **Add Asset Account** panel, configure the parameters and click
**Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Account Type | The type of the account. Valid values: Local Account and Domain Account. Domain Account is available only if you select Domain Control for the Asset Type parameter in the Asset Information step. Only Local Account is available for other asset types. |
| Account Name | The name of the account. The name can be up to 64 characters in length. |
| Privileged Account | If you select this check box, the account is identified as a privileged account and can be used in the following scenarios: You can use the privileged account to change the password of a regular account. If the account uses the SSH protocol, the password of the account can be automatically changed. If the password fails to be automatically changed, you can use the privileged account to change the password. If the account uses the RDP protocol, you must use the privileged account to change the password of the account. If you create an account whose protocol is SSH or RDP for an asset on Bastionhost, Bastionhost uses the privileged account to create the same account on the asset. If you delete the account of an asset from Bastionhost, Bastionhost uses the privileged account to log on to the asset to delete the account. You can use the privileged account to log on to the asset and identify other accounts of the asset. You can use the privileged account to obtain the information about other accounts of the asset. |
| Password | The password of the account. |
| Apply to Service | The protocol that the account uses. You can select multiple protocols. |
| SSH Key | If you set Apply to Service to SSH, you can select an SSH key for the account. Make sure that an SSH key is created in advance. |
| Connected To | If you set Apply to Service to ORACLE, you must select a connection property. |
| Automatic Password Change | If you select Yes, automatic password change is enabled for the account. If you select No, automatic password change is disabled for the account. |
| Password Change Script | The custom password change script for the account. |

| Switch From | If you set Apply to Service to SSH or TELNET, you must select a connection property. |
|---|---|
| Custom Attribute | The custom attributes of the account. |
| Account Password Verification | If the account already exists for the asset, click Account Password Verification to check whether the password is valid. |

**Modify the information about multiple assets at a time**

1. In the **Asset** section, select the asset that you want to manage and click **Edit** above the
asset list.
2. In the **Batch Edit Asset** panel**,** modify the asset information and click **Confirm**. The
following table describes the asset information.

| Parameter | Description |
|---|---|
| Network | The network to which the asset belongs. Default value: default. |
| Node | The node to which the asset belongs. |
| System Code | The system code. |
| Account Switch Command | The switch command for secondary logon of the account. You can configure this parameter for accounts that use the SSH and Telnet protocols. After you use the associated account to log on to an asset, Bastionhost automatically runs this command to log on to the asset by using the account. |
| Remark | The remarks of the asset. |
| Custom Attribute | The custom attributes of the account. |

**Export domain names**

1. In the **Asset** section, click the
icon.
2. In the **Export** dialog box, configure the Export Range and Encryption Password parameters
and click **Export** to export the asset information to your computer. The encryption password is used to decrypt the ZIP file. This ensures the security of the file. We recommend that you specify an encryption password. All: exports all asset information. Selected: exports the information about the selected assets. Select the assets before you click Export

#### Manage asset diagnostics tasks

This topic describes how to create an asset diagnostics task and how to manage it.

**Create an asset diagnostics task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Assets > Asset Diagnosis**.
4. Click the
icon. In the **Create Asset Health Check Task** panel, configure the basic task information and click **Next**.
5. Select check items and click **Next**.
6. Select the asset scope for diagnostics and click **Confirm**.

**What to do next**

Modify the asset diagnostics task: Move the pointer over the task and click **Edit**. Delete the asset diagnostics task: Move the pointer over the task and click **Delete**. Execute the asset diagnostics task: Move the pointer over the task and click **Immediately**
**Execute**.
View or modify the default configurations of asset diagnostics tasks: Click the icon. In the
**Asset Health Check Task Default Configuration**panel, view or modify the default
configurations of asset diagnostics tasks.

#### Discover assets

You can synchronize remote assets to Bastionhost to manage the assets in a centralized manner. Bastionhost allows you to discover and synchronize assets in LANs.

**Create an asset source**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Assets > Asset Discovery**.
4. Click the
icon. In the **Create Asset Source** panel, configure the parameters and click
**Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | Enter the name of the asset source. |
| Type | Set the value to LAN, which specifies that the asset source scans assets within the destination CIDR block. |

| Automatic Synchronization | After you turn on this switch, the asset source periodically synchronizes remote assets based on the specified synchronization interval. |
|---|---|
| Network | Select the network to which the synchronized assets belong. If no networks are available, click Create to go to the Network Management page to create a LAN. |
| Destination CIDR Block | Configure the destination CIDR block within which the asset source scans assets. The mask of the CIDR block must be greater than or equal to 24 bits. |
| Synchronize To | Select the node to which the synchronized assets belong in the current project. |
| Synchronous Creation | If you select this option, the synchronized assets are automatically managed by Bastionhost. If you do not select this option, you must manually manage the assets. |
| Synchronous Deletion | If you select this option, the assets that belong to the network of the asset source in the project are automatically deleted if the assets are not detected. Proceed with caution. |

**Synchronize assets**

If the automatic synchronization feature is enabled for an asset source, Bastionhost periodically synchronizes remote assets based on the specified synchronization interval. You can also manually synchronize the assets. In the **Asset Source** section, select an asset source and click **Synchronize**.

**View the information about the automatically synchronized**

**assets**

If you select Synchronous Creation for an asset source, you can view information about the most recent assets that are automatically synchronized. In the **Asset Source** section, select an asset source. In the **Latest Automatic**
**Synchronization Status** section, you can view the information about the most recent assets
that are automatically synchronized. You can also click **Recently Added** to view the assets that are created for this synchronization.

**Manage an asset**

If you do not select Synchronous Creation for an asset source, you can manually manage the assets. In the **Asset Source** section, select an asset source and click **Unmanaged**. The unmanaged assets list is displayed. Select an asset and click **Manage**.

**Ignore an asset**

If you do not want to manage a synchronized asset and you want the asset to be removed from the unmanaged asset list, you can use the ignore feature. In the **Asset Source** section, select an asset source and click **Unmanaged**. The unmanaged assets list is displayed. Select the asset and click **Ignore** to ignore the asset.

#### Manage tags

This topic describes how to create and manage a tag.

**Create a tag**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Assets > Asset Management**.
4. Click **Create**. In the **Create new tag** panel, enter a tag name, select the object to be
bound to the tag, and then click **Confirm**. You can select assets or asset accounts as the object.

**Add a tag to assets**

**Add a tag to an asset**

1. In the left-side navigation pane, choose **Assets** > **Asset Management**.
2. Find the asset that you want to manage and click **Edit** in the **Actions** column.
3. In the **Basic Information** section, select a tag and click **Save**.

**Add a tag to multiple assets**

1. In the left-side navigation pane, choose **Assets** > **Asset Management**.
2. Select the assets that you want to manage and choose **More > Bind tag** above the asset
list.
3. In the Select Tag panel, select the tag that you want to add to the assets and click
**Confirm**.

**Add a tag to accounts**

**Add a tag to an account**

1. In the left-side navigation pane, choose **Account > Account Management**.
2. Find the account that you want to manage and click **Edit** in the **Actions** column.
3. In the **Basic Information** section, select a tag and click **Save**.

**Add a tag to multiple accounts**

1. In the left-side navigation pane, choose **Account > Account Management**.
2. Select the accounts that you want to manage and choose **More > Bind tag** above the
account list.
3. In the Select Tag panel, select the tag that you want to add to the accounts and click
**Confirm**.

**What to do next**

To modify a tag, click **Edit** in the **Actions** column of the tag. To delete a tag, select the tag and click **Delete** above the tag list.

#### Configure a remote client

If the client tools or protocols, such as HTTPS, are not supported by Bastionhost and you want to use Bastionhost to perform O&M and audit operations, you can use a remote client to specify an application server.

**Create a remote client**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Asset > Remote Client**.
4. On the **Remote Client** tab, click **Create**.
5. In the **Create Remote Client** panel, configure the parameters and click **Confirm**.
To modify a remote client, find the remote client that you want to manage on the
**Remote Client** tab, and click **Edit** in the **Actions** column.
To delete a remote client, find the remote client that you want to manage on the **Remote**
**Client** tab, and click **Delete**.

**Create an application server**

You must enable RDP for the asset that is used as application server.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Asset > Remote Client**.
4. On the **Application Server** tab, click **Create**.
5. In the **Create Application Server** panel, select the type of the application server, select
an asset, and then click **Create Application Server**. i. To modify an application server, find the application server that you want to manage on the **Application Server** tab, and click **Edit** in the **Actions** column. ii. To delete an application server, find the application server that you want to manage on the **Application Server** tab, and click **Delete** in the **Actions** column.

**Deploy an application server**

1. On the **Application Server** tab, find the application server that you want to manage and
click **Deploy** in the **Actions** column.
2. Click **Generate Command**, follow the instructions to complete the configurations, and
then click **Confirm**.

**Synchronize an account on an application server**

1. On the **Application Server** tab, find the application server that you want to manage and
click **Synchronize Account** in the **Actions** column.
2. In the **Synchronize Account** panel, click **Synchronize** to automatically create an account
for Bastionhost users on the application server.

### Accounts

#### Manage accounts

##### Create a local account

This topic describes how to create a local account.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Management**.
4. Click **Create**. In the **Create Account** panel, select the asset that you want to manage and
click **Next**.
5. Configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Account Type | The type of the account. Valid values: Local Account and Domain Account. Domain Account is available only if you select Domain Control for the Asset Type parameter in the Asset Information step. Only Local Account is available for other asset types. |
| Account Name | The name of the account. The maximum length is 64 characters. |
| Privileged Account | If you select this check box, the account is identified as a privileged account and can be used in the following scenarios: You can use the privileged account to change the password of a regular account. If the account uses the SSH protocol, the password of the account can be automatically changed. If the password fails to be automatically changed, you can use the privileged account to change the password. If the account uses the RDP protocol, you must use the privileged account to change the password of the account. If you create an account whose protocol is SSH or RDP for an asset on Bastionhost, Bastionhost uses the privileged account to create the same account on the asset. If you delete the account of an asset from Bastionhost, Bastionhost uses the privileged account to log on to the asset to delete the account. You can use the privileged account to log on to the asset and identify other accounts of the asset. You can use the privileged account to obtain the information about other accounts of the asset. |
| Password | The password of the account. |
| Apply to Service | The protocol that the account uses. You can select multiple protocols. |
| SSH Key | If you set Apply to Service to SSH, you can select an SSH key for the account. |

| Connected To | If you set Apply to Service to ORACLE, you must select a connection property. |
|---|---|
| Automatic Password Change | If you select Yes, automatic password change is enabled for the account. If you select No, automatic password change is disabled for the account. |
| Password Change Script | The custom password change script for the account. |
| Custom Attribute | The custom attributes of the account. |

**What to do next**

To modify the information about an account, find the account and click **Edit** in the **Actions** column. Then, click **Save**. To delete multiple accounts, select the accounts and click **Delete** above the account list.

##### Create or delete a remote account

You can manage accounts of remote assets on Bastionhost.

**Create a remote account**

If you create an account for an asset on Bastionhost, the same account can be created on the asset. You can create accounts for assets that support the following protocols: SSH, RDP, MySQL, Oracle, and SQL Server. Make sure that you create a privileged account on Bastionhost whose protocol is the same as the protocol of the asset.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Management**.
4. Select a local account and choose **More > Create Remote Account**.
5. In the message that appears, click **Confirm**.

**Delete a remote account**

You can delete a remote account by using Bastionhost. You can create accounts for assets that support the following protocols: SSH, RDP, MySQL, Oracle, and SQL Server. Make sure that you create a privileged account on Bastionhost whose protocol is the same as the protocol of the asset. Only the remote account is deleted. The local account on Bastionhost is not deleted.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Management**.
4. Select a local account and choose **More > Delete Remote Account**.
5. In the message that appears, click **Confirm**.

##### View asset accounts by category

This topic describes how to view asset accounts by category.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Management**.
4. In the left-side section of the Account Management page, click the category that you want
to manage to view the account list or protocol list and the number of accounts. Click an account or a protocol to view the account information.

##### View account logs

This topic describes how to view account logs.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Management**.
4. Find the account that you want to manage and click **Edit** in the **Actions** column.
5. On the **Logs** tab, view the operation logs of the account.
Find an operation log and click **Details** to view the details of the log.

#### Diagnose accounts

Bastionhost supports regular and manual check of account status. Bastionhost can detect abnormal asset accounts and provides handling measures. Accounts of different protocols support different check items. For more information, see the following table. A tick (√) indicates that the check item is supported, a vertical bar (l).indicates that the check item is supported when a privileged account of the same protocol exists, and a hyphen (-) indicates that the check item is not supported.

| Prot ocol | Wea k pass wor d | Pass wor d unc han ged for a long time | Inva lid pass wor d or key | Unm ana ged pass wor d or key | Acc ount who se pass wor d can not be cha nge d | Red und ant acco unt | Per miss ion cha nge s | Zom bie acco unt | Expi red acco unt | Acc ount who se pass wor d expi res | Lock ed acco unt |
|---|---|---|---|---|---|---|---|---|---|---|---|

| SSH | √ | √ | √ | √ | √ | l | l | l | l | l | l |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TELN ET | √ | √ | √ | √ | √ | - | - | - | - | - | - |
| RDP | √ | √ | √ | √ | √ | l | l | l | l | l | l |
| ORA CLE | √ | √ | √ | √ | √ | l | - | - | - | - | - |
| KING BAS E | √ | √ | √ | √ | √ | - | - | - | - | - | - |
| DM | √ | √ | √ | √ | √ | - | - | - | - | - | - |
| Post greS QL | √ | √ | √ | √ | √ | - | - | - | - | - | - |
| DB2 | √ | √ | √ | √ | √ | - | - | - | - | - | - |
| SQL Serv er | √ | √ | √ | √ | √ | l | - | l | - | - | - |
| MyS QL | √ | √ | √ | √ | √ | l | - | - | - | l | - |

##### Configure a custom policy for diagnostic

### tasks

This topic describes how to configure a custom policy for diagnostic tasks.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Diagnostics**.
4. Click the
icon. In the **Default Configuration of Diagnostics Tasks** panel, configure the parameters and click **Confirm**.

| Parameter | Description |
|---|---|

| Password Strength | Minimum Password Length | The minimum length of a password. Valid values: 10 to 128. | If a password does not meet one or more requirements, the password is identified as a weak password. |
|---|---|---|---|
|   | Password Complexity | The required numbers of digits, letters, and special characters in a password. Valid values: 0 to 10. |   |
|   | Maximum Number of Same Characters in Password | The maximum number of occurrences of a character in a password. Valid values: 2 to 10. |   |
|   | Do not use the following passwords | The characters that cannot be used in a password. |   |
| Other Configurations | Number of Days without Password Change | The maximum number of days that a password can remain unchanged. | If the number of days exceeds the value of this parameter, the password is considered unchanged for a long period of time. |
|   | Number of Days without Logon | The maximum number of consecutive days that an account is not used for logon. | If the number of days exceeds value of this parameter, the account is identified as an inactive account. |

##### Create a diagnostic task

This topic describes how to create a diagnostic task.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Diagnostics**.
4. Click the
icon. In the **Create Diagnostics Task** panel, configure the Task Name and First Executed At parameters, and then click **Next**. The following table describes the parameters.

| Parameter | Description |
|---|---|

| Task Name | The name of the diagnostic task, which is used only for identification. The names must be unique in a project. |
|---|---|
| Execution Method | The execution method. Valid values: Manual: You can manually execute the diagnostic task based on your business requirements. Automatic: Configure the First Executed At parameter. Then, Bastionhost starts to execute the diagnostic task at the specified point in time. If you select Recurrence, you must specify a task execution interval. Then, Bastionhost executes the task based on the specified interval. |

5. Select check items in the following table and click **Next.**

| Parameter | Description |
|---|---|
| Check Items | Weak Password: If the password of the detected account does not meet the password complexity policy that is configured for the task, the account is considered an account with a weak password. Password Unchanged for a Long Time: If the password of the detected account is not changed for more than the specified number of days for unchanged passwords, the account is considered an account whose password is not changed for a long time. Permission Change: If the permissions of a Linux or Windows account on an asset are changed, the account is considered a permission-changed account. Invalid Password or Key: If the password or key of the detected account is invalid on Bastionhost, the account is considered an account whose password or key is invalid. Unmanaged Password or Key: If no passwords or keys of the detected account is managed on Bastionhost, the account is considered an account whose passwords or keys are unmanaged. Zombie Account: If the detected account has not logged on to the asset for more than the specified number of days, the account is considered a zombie account. Redundant Account: If the detected account does not exist on the asset, the account is considered a redundant account. Expired Account: If the detected account on the asset has expired, the account is considered an expired account. Account with Expired Password: If the password of the detected account on the asset has expired, the account is considered an account whose password has expired. Locked Account: If the detected account is locked on the asset, the account is considered an locked account. Account Disallowing Password Change: If automatic password change is disabled for the detected account on Bastionhost, the account is considered an account whose password cannot be changed. |

| Password Strength | If you select Weak Password, you must specify a password complexity policy. Valid values: Default and Custom. Default: Reuse the configurations of the custom policy for diagnostic tasks. Custom: Configure a custom password complexity policy. For more information, see the parameter descriptions in the "Configure a custom policy for diagnostic tasks" topic. |
|---|---|
| Number of Days without Password Change | If you select Password Unchanged for a Long Time, you must specify the maximum number of days that a password is allowed to remain unchanged. Default: Reuse the configurations of the custom policy for diagnostic tasks. Custom: Specify a custom value for this parameter. |
| Automatic deletion | If you select Zombie Account or Redundant Account, you can specify whether to automatically delete detected zombie accounts or redundant accounts. |
| Number of Days without Logon | If you select Zombie Account, you must specify the maximum number of consecutive days that an account remains unlogged. Default: Reuse the configurations of the custom policy for diagnostic tasks. Custom: Configure a custom value for this parameter. |

##### Execute a diagnostic task

This topic describes how to execute a diagnostic task.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Diagnostics**.
4. Move the pointer over the task and click **Immediately Execute**. In the message that
appears, click Confirm to execute the task. Move the pointer over the task that is being executed and click **Stop**. In the message that appears, click Confirm to stop the task. If the Execution Method parameter is set to **Automatic**, the system automatically executes the task at the specified time.

##### View a diagnostic task

This topic describes how to view the information about a diagnostic task.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Diagnostics**.
4. Click the diagnostic task that you want to manage. On the **Diagnostics Result** tab, view
the most recent diagnostic result of the task, including the scanning status, automatically deleted accounts, account security status, account status, and scanned accounts. Click the number of each item to view specific information about the item. Click **Details**. In the **Account Details** panel, view the basic information, check items, and check results of the account. Click **Record** to view the diagnostic details of the account.

##### Manage an account diagnostic scope

This topic describes how to configure an account diagnostic scope.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Diagnostics**.
4. Click an account diagnostic task. On the **Diagnostics Scope** tab, click **Add Account**.
5. In the **Select Account** panel, select an account and click **Confirm**.

#### Discover accounts

##### Create a discovery task

You can use a privileged account to discover other accounts that use the same protocol as the privileged account and add the accounts to Bastionhost for management. This topic describes how to create a discovery task.

**Prerequisites**

The asset account has a privileged account that uses the same protocol as the asset account. You can discover asset accounts that use the SSH, RDP, MySQL, Oracle, and SQL Server protocols.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Discovery**.
4. Click the
icon. In the **Create Discovery Task** panel, configure the parameters and click
**Next**.

| Parameter | Description |
|---|---|
| Task Name | The name of the discovery task, which is used only for identification. The name must be unique in a project. |

| Execution Method | The execution method. Valid values: Manual: You can manually execute the discovery task based on your business requirements. Automatic: Configure the First Executed At parameter. Bastionhost starts to execute the discovery task at the specified time. If you select Recurrence, you must also specify a task execution interval. Then, Bastionhost executes the task based on the specified interval. |
|---|---|
| Automatic Management | After you turn on this switch, the unmanaged accounts are automatically added to Bastionhost for management after the task is executed. |

5. Select the asset that you want to manage and click **Confirm**.

**What to do next**

**Edit a discovery task**

**Note**

You cannot edit a discovery task that is in the pending or executing state.
1. Move the pointer over the task that you want to manage and click **Edit**.
2. In the **Modify Discovery Task** panel, edit the task.

**Delete a discovery task**

Move the pointer over the task that you want to manage and click **Delete**. You can also select the task and click **Delete** below the task list.

##### Execute a discovery task

This topic describes how to execute a discovery task.

**Automatic execution**

If you set the Execution Method parameter to Automatic when you create a task, the system executes the task at the specified time.

**Manual execution**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Discovery**.
4. Execute one or more tasks.
To execute a task, move the pointer over the task and click **Immediately Execute**. In the Immediately Execute message, click Confirm. To execute multiple tasks at a time, select the tasks and click **Immediately Execute**. In the Batch Immediately Execute message, click Confirm.

**Stop a discovery task**

Move the pointer over the task that you want to manage and click **Stop**. You can also select the discovery task and click **Stop** below the task list.

##### Add accounts for management

If automatic management is not enabled for a discovery task, you must manually add the discovered accounts to Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Account Discovery**.
4. Click the task that you want to manage. On the **Discovery Result** tab, select the
unmanaged accounts and click **Manage**.

#### Manage passwords

##### View accounts associated with password

**change tasks**

Bastionhost allows you to manage accounts that are associated with password change tasks. This topic describes how to view accounts that are associated with password change tasks.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, view accounts that are associated with
password change tasks from different dimensions in the All Accounts section. You can also view accounts that are associated with password change tasks by status in the Account section.
**Pending**: displays the accounts whose passwords are pending for changing.
**Executing**: displays the accounts whose passwords are being changed.
**Modified**: displays the accounts whose passwords are changed or verified, or whose
historical passwords are restored.
**Modification failed**: displays the accounts whose passwords failed to be changed or
verified, or whose historical passwords failed to be restored.
**To Be Executed**: displays the accounts that are associated with password change tasks
but no password change tasks are executed.
**Canceled**: displays the accounts that are associated with stopped password change
tasks.

##### Immediately change the password

This topic describes how to change the password of an account.

**Retry password change tasks**

If an account is associated with multiple password change tasks and the password of the account is changed at least once, and you do not want to change the passwords of other accounts that are associated with the password change tasks, you can retry the password change tasks for accounts whose passwords you want to change.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, select the account that you want to manage
and choose **Immediately Change Password** > **Retry**.
5. In the message that appears, click **Confirm**.

**Create a password change task**

If you want to immediately change the passwords of specific accounts that are associated with a password change task, but the password change task does not meet your business requirements, you can create another password change task.
1. On the **Account for Password Change** tab, select the account that you want to manage
and choose **Immediately Change Password** > **Create Plan**.
2. In the **Create Password Change Plan** panel, configure the parameters and click
**Confirm**.

**Stop a password change task**

After a password change task is started, if the task is in the pending state, you can manually stop the password change task.

**Important**

You cannot stop a password change task that is being executed. If you stop a password change task that is not in the pending state, the password may be lost.
1. On the **Account for Password Change** tab, select the account whose password change
task is in the **Pending** state and click **Stop**.
2. In the message that appears, click **Confirm**.

##### Verify the password of an account

This topic describes how to verify the password of an account.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, find the account that you want to manage
and choose **More > Verify Password** in the **Actions** column.
5. In the **Verify Password** dialog box, enter the password and click **Confirm**.

##### Download historical passwords

This topic describes how to export the historical and current passwords of an account.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, find the account that you want to manage
and choose **More > Download Historical Passwords** in the **Actions** column.
5. In the **Download Password** dialog box, enter an encryption password and click **Export**.
The encryption password is used to decrypt the ZIP file. This ensures the security of the file. We recommend that you specify an encryption password.

##### Download password change history

This topic describes how to export the password change history for an account.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, find the account that you want to manage
and choose **More > Download password change history** in the **Actions** column.
5. In the **Download password change history** dialog box, enter an encryption password
and click **Export**. The encryption password is used to decrypt the ZIP file when you open the file. This ensures the security of the file. We recommend that you specify an encryption password.

##### Restore a password

This topic describes how to restore a password.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, find the account that you want to manage
and choose **More > Restore Password** in the **Actions** column.
5. In the **Restore Password** message, click **Confirm**.
If the password is lost due to repeated power outages and network failures during the execution of the password change task, make sure that the server exists and is connected as expected before you restore the password.

##### Export the password of an account

This topic describes how to export the password of an account to your computer.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Account for Password Change** tab, select the account that you want to manage
and click **Export Password** above the account list.
5. In the **Export Password** dialog box, enter an encryption password and click **Export**.
The encryption password is used to decrypt the ZIP file. This ensures the security of the file. We recommend that you specify an encryption password.

##### Configure a password change task

**Use the default configurations of the password change policy**

You can use the default password policy, backup policy, and backup mode.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Password Change Plan** tab, click the
icon.
5. In the **Default Policy Configuration** panel, click **Confirm**.

**Create a password change task**

1. On the **Password Change Plan** tab, click the
icon.
2. In the **Create Password Change Plan** panel, configure the parameters and click
**Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Execution Method | Select the execution mode of the password change task. Valid values: Manual: You can manually execute the password change task based on your business requirements. Automatic: You must configure the First Executed At parameter. If you select Recurrence, you must also configure a task execution interval. Then, Bastionhost executes the task based on your configurations. |
| Password Policy | Select the policy for generating a new password. Valid values: Default Policy: A new password is generated based on the default password policy. Custom: You must configure a password policy. |
| Name | Enter the name of the password change task, which is used only for identification. The name must be unique in a project. |

| Backup Policy | Select the backup policy for the previous and new passwords. Valid values: No Backup: does not back up the previous and new passwords. Default Policy: uses the default backup policy. For more information about the default backup policy, see the "Use the default configurations of the password change policy" section of this topic. Custom Policy: You must configure a backup policy. |
|---|---|

**Manage an account associated with a password change task**

**Associate an account with a password change task**

1. On the **Password Change Plan** tab, click the task that you want to manage. In the right-
side section, click **Associate Account**.
2. In the **Associate Account** panel, select the account and click **Confirm**.

**Dissociate an account with a password change task**

1. On the **Password Change Plan** tab, click the task that you want to manage.
2. In the right-side section, select the required account and click **Disassociate**.
3. In the **Disassociate** message, click **Confirm**.
4. In the **Associate Account** panel, select another account and click **Confirm**.

##### Complex password-change accounts

This topic describes how to create and manage complex password-change accounts.

**Create a complex password-change account**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Management**.
4. On the **Complex Password Change Account** tab, click **Create**.
5. In the **Basic Settings** step, configure the parameters described in the following table and
click **Next**.

| Parameter | Description |
|---|---|
| Name | The name of the complex password-change account. It is used only for identification. The names of complex password-change accounts in the same project must be unique. |
| Source Account | Select an asset account. The system uses the complex password-change process to change the password of this account and pushes the new password to other applications based on the process. A source account can be associated with only one complex password-change account and cannot be changed after it is saved. |

| System Parameters | The built-in parameters of the system, which can be used to change the password and push scripts. |
|---|---|
| Custom Parameters | User-defined parameters, which can be used to change the password and push scripts. In the same complex password-change account, the parameter names must be unique in System Parameters, in Custom Parameters, or between System Parameters and Custom Parameters. |

6. Click the
icon, configure the password change information, and then click **OK**.

| Parameter | Description |
|---|---|
| Password Change Method | The password change method. Valid values: Follow the original account configuration and Remote Execution Script. Follow the original account configuration: Use the password change method of the source account. Remote Execution Script: Use the subsequently configured execution account to change the password by remotely executing scripts. |
| Execution Account | Select an asset account of the RDP or SSH service. The system uses this account to execute remote scripts. The number of times that the same asset account can be used as the execution account is not limited. |
| Script Command | The user-defined remote password-change script. |

7. Click the
icon. In the **Password Push** section, click **Parallel Task**. In the panel that appears, configure the information about the subtask and click **Confirm**. A maximum of 9 password push processes and 10 parallel tasks are supported.

| Parameter | Description |
|---|---|
| Type | Only Remote Execution Script is supported. |
| Execution Account | Select an asset account of the RDP or SSH service. The system uses this account to execute remote scripts. The number of times that the same asset account can be used as the execution account is not limited. |
| Script Command | The user-defined remote push script. |

8. Click **Confirm**.

**Related operations**

Change a complex password-change account: On the **Complex Password Change**
**Account** tab, find the account that you want to modify and click **Edit** in the **Actions**
column. Copy a complex password-change account: On the **Complex Password Change Account** tab, find the account that you want to copy and click **Copy** in the **Actions** column. Delete a complex password-change account: On the **Complex Password Change**
**Account** tab, find the account that you want to delete and click **Delete** above the account
list. Download historical passwords of a complex password-change account: On the **Complex**
**Password Change Account** tab, find the account whose historical passwords you want to
download and click **Download Historical Passwords** in the **Actions** column. In the dialog box that appears, enter the encryption password of the exported file and click **Export**. The encryption password is used to decrypt the exported ZIP file when you open the file. This ensures the security of the file. We recommend that you specify an encryption password. Retry a password change plan: On the **Complex Password Change Account** tab, select the account that you want to manage and choose **Immediately Change Password >**
**Retry** above the account list.
Create a password change plan: On the **Complex Password Change Account** tab, select the account that you want to manage and choose **Immediately Change Password >**
**Create Plan** above the account list.
Stop a password change: On the **Complex Password Change Account** tab, select the account that you want to manage and click **Stop** above the account list. View the execution history: On the **Complex Password Change Account** tab, find the account that you want to view and click **Execution History** in the **Latest Execution**
**Record** column.

#### Manage keys

You can manage all SSH keys in a centralized manner.

**Create a key**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Key Management**.
4. Click **Create**. In the **Create Key** panel, configure the parameters and click **Confirm**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of the custom SSH key. |
| Generation Method | Valid values: Manually Record: You must manually enter the SSH private key and the encryption password of the SSH key pair. Then, Bastionhost generates an SSH public key. Automatic Generation: Bastionhost generates an SSH key pair, including an SSH public key and an SSH private key, based on the values of the Encryption Algorithm, Key Length, Encryption Token, and Confirm Encryption Password parameters. |

**Associate a key with an account**

You can associate a key with an asset account that uses the SSH protocol. Then, this account can access the asset by using the SSH key.
1. In the key list, find the key that you want to manage and click **Associate Account** in the
**Actions** column.
2. In the **Associate Host Account** panel, select the account that you want to manage and
click **Associate Account**.

**Dissociate a key from an account**

1. In the key list, find the key that you want to manage and click the number in the
**Associated Accounts** column.
2. In the **Associated Host Account** panel, select the account that you want to manage and
click **Disassociate**.

**View a public key**

In the key list, find the key that you want to manage and click **View Public Key** in the
**Actions** column.

**Modify a key**

1. In the key list, find the key that you want to manage and click **Edit** in the **Actions** column.
2. In the **Modify Key** panel, modify the configurations and click **Confirm**.

**Delete a key**

1. In the key list, select the key that you want to manage and click **Delete** above the key list.
2. In the message that appears, click **Confirm**.

### Authorization

#### Manage authorization rules

##### Perform operations on the Rule View tab

You can create an authorization rule to grant permissions to users on the accounts of assets in the system.

**Create one or more authorization rules**

**Create an authorization rule**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Authorize > Authorization Rule**.
4. On the **Rule View** tab, click **Create**.
5. In the **Create Rule** panel, configure the parameters and click **Confirm**. The following table
describes the parameters.

| Parameter | Description |
|---|---|

| Rule Name | The name of the rule, which is used only for identification. |
|---|---|
| Rule Validity Period | Permanent: The rule never expires. Custom: Specify a validity period for the rule. The rule is valid only during the specified period of time. |
| Automatically deleted at 00:00 the next day after expiration | If you specify a validity period for the rule and select this option, the system automatically deletes the rule at 00:00 on the next day after the validity period ends. |
| Authorized Users | The Bastionhost users or user groups to which you want to grant asset operation and management permissions. All Users: grants the permissions to all users in the user list. User/User Group: grants the permissions only to the selected users or user groups. Click Add and select Add User or Add User Group. In the Select User or Select User Group panel, select the users or user groups that you want to add and click Confirm. To remove the selected user or user group, select a user or user group and click Delete. Rule: grants the permissions only to users who meet the conditions of the rule. Make sure that you created custom attributes on the Configure > User Configuration > Custom Attribute tab in the management console. Click Add. In the Add Rule panel, configure the attribute, matching mode, and value, and click Confirm. You can add multiple attributes. If you add multiple attributes, the permissions are granted only to users who match all attributes. Find an attribute and click Edit to modify the attribute of the rule. Find an attribute and click Delete to remove the attribute from the rule. |

| Authorize Assets | The assets on which you want to grant permissions to users. All Assets: grants permissions on all assets in the asset list to the selected users. Asset/Asset Node: grants permissions on specific assets or asset nodes to the selected users. Click Add and select Add Asset or Add User Asset Node. In the Select Asset or Select Asset Node panel, select the assets or asset nodes and click Confirm. To remove the selected asset or asset node, select an asset or asset node and click Delete. Rule: grants permissions only on the assets or asset nodes that meet the conditions of the rule to the selected users. Make sure that you created custom attributes on the Configure > User Configuration > Custom Asset Attribute tab in the management console. Click Add. In the Add Rule panel, configure the attribute, matching mode, and value, and click Confirm. You can add multiple attributes. If you add multiple attributes, the permissions are granted only to users who match all attributes. Find an attribute and click Edit to modify the attribute of the rule. Find an attribute and click Delete to remove the attribute from the rule. |
|---|---|
| Authorize Accounts | The accounts on which you want to grant permissions to users. All Accounts: grants permissions on all accounts of the selected assets to the selected users. Account: grants permissions on specific accounts of the selected assets to the selected users. Enter the username of an account and press the Enter key. You can enter multiple usernames. If you enter an invalid username, click the icon to remove the username. Rule: grants permissions only on the accounts of the selected assets that meet the conditions of the rule to the selected users. Make sure that you created custom attributes on the Configure > User Configuration > Custom Account Attribute tab in the management console. Click Add. In the Add Rule panel, configure the attribute, matching mode, and value, and click Confirm. You can add multiple attributes. If you add multiple attributes, the permissions are granted only to users who match all attributes. Find an attribute and click Edit to modify the attribute of the rule. Find an attribute and click Delete to remove the attribute from the rule. |

| Authorize Services | The protocols of the accounts on which you want to grant permissions to users. All Services: grants permissions on the accounts that use any protocol of the selected assets to the selected users. Service: grants permissions on the accounts that use specific protocols of the selected assets to the selected users. Click the field and select the protocols based on your business requirements. You can select multiple protocols. If you no longer require a protocol, click the icon to remove the protocol. |
|---|---|

**Import multiple authorization rules at a time**

You can use the built-in template to create multiple authorization rules at a time.
1. On the **Rule View** tab, choose **Create > Import Rule**.
2. In the dialog box that appears, click **Download Template File** to save the template file to
your computer.
3. Open the template file on your computer, enter authorization rules based on the description
and field requirements in the file, and then save the file.
4. Click **Select File** and select the file. Then, click **Import** to upload the file.
If you select **Overwrite Rule with Same Name** and the name of an authorization rule in the file is the same as the name of an existing authorization rule in the system, the authorization rule in the file overwrites the authorization rule in the system.

**Enable an authorization rule**

If an authorization rule is disabled, you must enable the rule for the rule to take effect. On the **Rule View** tab, select a rule that is in the **Disable** state and click **Enable** above the rule list.

**Disable an authorization rule**

If you disable an authorization rule, the authorization rule becomes invalid. If you want the authorization rule to take effect, you must re-enable the authorization rule. On the **Rule View** tab, select the rule that you want to manage and click **Disable** above the rule list.

**Export authorization rules**

You can export multiple authorization rules at a time.
1. On the **Rule View** tab, click the
icon.
2. In the **Export** dialog box, configure the Export Range and Encryption Password parameters
and click **Export** to export the authorization rules to your computer. The encryption password is used to encrypt the ZIP file when you open the file. This ensures the security of the file. We recommend that you specify an encryption password. All: exports all authorization rules. Selected: exports the selected authorization rules. You must select authorization rules before you click Export.

**Delete an authorization rule**

On the **Rule View** tab, select the rule that you want to manage and click **Delete** above the rule list.

##### Perform operations on the Member View

**tab**

You can view authorized assets by user.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Authorize > Authorization Rule**.
4. On the **Member View** tab, click a user. All assets and asset accounts on which the user
has permissions are displayed in the right-side section. You can click **Export** below the user list to export all users and the assets and asset accounts on which the users have permissions. You can click the icon in the asset list to export the assets and asset accounts on which the selected user has permissions. You can enter the username or name of a user and press the Enter key in the user list to search for the user. You can enter an asset name, IP address, account name, or authorization rule, or select a protocol in the asset list, and click **Search** to search for an asset or asset account. You can click an authorization rule to modify the rule.

##### Perform operations on the Asset View tab

You can view the authorized users, asset accounts, and authorization rules by asset.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Authorize > Authorization Rule**.
4. On the **Asset View** tab, click an asset. All users and asset accounts that have permissions
on the asset are displayed in the right-side section. You can click **Export** in the asset list to export all assets, and the users and asset accounts that have permissions on the asset. You can click the icon in the user list to export the users and asset accounts that have permissions on the asset. You can enter an asset name or IP address and press the Enter key in the asset list to search for the required asset. You can enter the username, name, account, and authorization rule, or select a protocol in the user list, and then click **Search** to search for a user or an asset account. You can click an authorization rule to modify the rule.

#### Manage pre-authorization rules

This topic describes how to create and manage pre-authorization rules.

**Overview**

You can create pre-authorization rules to limit the assets that can be applied for in O&M tickets, password tickets, and emergency O&M tickets. If pre-authorization rules are created, all users can apply only for pre-authorized assets.

**Create a pre-authorization rule**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Authorize > Authorization Rules**.
4. On the Pre-authorization Rule page, click **Create**. On the Create Pre-authorization Rule
page, configure the parameters that are described in the following table and click **Confirm**.

| Parameter | Description |
|---|---|
| Rule Name | The name of the rule, which is used only for identification. |
| Validity Period | Permanent: The rule never expires. Custom: Specify a validity period for the rule. The rule is valid only during the specified period of time. |
| Automatically deleted at 00:00 the next day after expiration | If you specify a validity period for the rule and turn on this switch, the system automatically deletes the rule at 00:00 on the next day after the validity period ends. |
| Authorize Users | The Bastionhost users or user groups to which you want to grant asset operation and management permissions. Valid values: All Users: grants the permissions to all users in the user list. Designated user: grants the permissions only to the selected users or user groups. Click Add and select Add User or Add User Group. In the Select User or Select User Group panel, select one or more users or user groups and click Confirm. To remove selected users or user groups, select one or more users or user groups and click Delete. |

| Authorized Asset | The assets whose permissions you want to grant to users. Assets: grants the permissions on specific assets to the selected users. Click Add and select Add Asset. In the Select Asset panel, select one or more assets and click Confirm. To remove selected assets, select one or more assets and click Delete. |
|---|---|
| Authorized accounts | The asset accounts whose permissions you want to grant to users. Accounts: grants the permissions on specific asset accounts to the selected users. Click Add and select Add Account. In the Select Account panel, select one or more accounts and click Confirm. To remove selected accounts, select one or more accounts and click Delete. |
| Authorized asset directories | The asset directories whose asset permissions you want to grant to users. Asset directories: grants the permissions on assets and their accounts in the selected asset directories to the selected users. Click Add and Select Add Asset Directory. In the Select Asset Directory panel, select one or more asset directories and click Confirm. This way, all assets and their accounts in the selected asset directories are selected. To remove selected asset directories, select one or more asset directories and click Delete. |
| Authorized asset tags | The tags added to assets whose permissions you want to grant to users. Asset tags: grants the permissions on assets to which the selected tags are added to the selected users. Click Add and Select Add Asset Tag. In the Select Tag panel, select one or more tags and click Confirm. This way, all assets to which the selected tags are added are selected. To remove selected tags, select one or more tags and click Delete. |

| Authorized account tags | The tags added to asset accounts whose permissions you want to grant to users. Account tags: grants the permissions on asset accounts to which the selected tags are added to the selected users. Click Add and Select Add Account Tag. In the Select Tag panel, select one or more tags and click Confirm. This way, all asset accounts to which the selected tags are added are selected. To remove selected tags, select one or more tags and click Delete. |
|---|---|
| Authorized dynamic account groups | The dynamic account groups whose object permissions you want to grant to users. Dynamic account groups: grants the permissions on matched objects in the selected dynamic account groups to the selected users. Click Add and Select Add Dynamic Account Group. In the Select Dynamic Account Group panel, select one or more dynamic account groups and click Confirm. This way, all matched objects in the selected dynamic account groups are selected. To remove selected dynamic account groups, select one or more dynamic account groups and click Delete. |

**What to do next**

Enable pre-authorization rules: On the **Pre-authorization Rule** page, select one or more rules that you want to manage and click **Enable** above the rule list. In the message that appears, click Confirm. Disable pre-authorization rules: On the **Pre-authorization Rule** page, select one or more rules that you want to manage and click **Disable** above the rule list. In the message that appears, click Confirm. Delete pre-authorization rules: On the **Pre-authorization Rule** page, select one or more rules that you want to manage and click **Delete** above the rule list. In the message that appears, click Confirm.

#### Manage review rules

After you create a review rule, Bastionhost automatically initiates a review process when an applicant creates a ticket or a task, or triggers a control policy. After the application is approved, the applicant can obtain the required permissions to perform subsequent operations.

**Create a review rule**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. Choose **Authorization** > **Approval Rules**.
4. Click **Create**. In the **Create Approval Rule** panel, configure the parameters and click
**Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of the review rule, which is used only for identification. The name must be unique. |
| Priority | The priority of the review rule. Valid values: 1 to 99. A larger value specifies a higher priority. |
| Approval Process | You can configure reviewers. Add multiple review nodes Click Add Process to create sub review nodes in sequence. You can create up to five sub review nodes. Add one or more reviewers Click Add. In the Select User panel, select the users that you want to add as reviewers and click Add. You can add multiple reviewers to a node. The number of reviewers is unlimited. Remove a reviewer Click the icon next to the name of a reviewer to remove the reviewer. Delete a review node Click the icon in the upper-right corner of the review node to delete the review node. |

| Object to Be Approved | The objects on which the review rule takes effect. The objects include users, user groups, custom rules, assets, asset nodes, and matching rules. To create a custom rule for users or assets, select Rule and click Add. In the Add Rule panel, configure the parameters and click Confirm. To delete a custom rule from users or assets, click Delete. To add users or user groups, select User/User Group and choose Add > Add User or Add > Add User Group. In the panel that appears, select the users or user groups that you want to add and click Confirm. To remove a user or a user group, select the user or user group and click Delete. To add assets or asset nodes, select Asset/Asset Node and choose Add > Add Asset or Add > Add Asset Node. In the panel that appears, select the assets or asset nodes that you want to add and click Confirm. To remove an asset or asset node, select the asset or asset node and click Delete. |
|---|---|

**Modify a review rule**

1. In the review rule list, find the rule that you want to manage and click **Edit** in the **Actions**
column.
2. In the **Modify Approval Rule** panel, modify the review rule.

**Delete a review rule**

In the review rule list, select the rule that you want to manage and click **Delete** above the review rule list.

#### Configure the unauthorized logon

**feature**

The unauthorized logon review list displays the authorization relationships between users and assets that are automatically collected by the system after unauthorized users successfully log on to Bastionhost. Users who have the permissions to review unauthorized logons can approve and create authorization relationships among assets and users. This way, manual authorization is not required when the users log on to the assets to perform O&M operations.

**Procedure**

By default, the unauthorized logon feature is disabled. To use this feature, you must select
**Allow Unauthorized Logons from Web** on the **Configure > Asset Configuration >**
**O&M Configuration** tab.
If you want to display authorization relationships in the unauthorized logon review list, you must select **Collect Unauthorized Logons** on the **Configure > Asset Configuration >**
**O&M Configuration** tab.
If you want to collect the account passwords or private keys of assets with unauthorized logons, you must select **Collect Passwords of Host Accounts** on the **Configure >**
**Asset Configuration > O&M Configuration** tab**.**
If you select the Automatically create authorization rules option on the **Configure > Asset**
**Configuration > O&M Configuration** tab, the system automatically reviews the
unauthorized logons and creates O&M rules. If you want to review unauthorized logons, do not select this option.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Authorize > Unauthorized Logon**.
4. Select an unauthorized logon review record and click **Authorize** to complete the
authorization.

**Delete an unauthorized logon review record**

In the unauthorized logon review list, select an unauthorized logon review record and click
**Delete** to delete the record.

#### Manage dynamic objects

After you specify matching conditions for a dynamic object, the dynamic object can be bound to the matched assets, accounts, and services based on the specified matching conditions. When the Bastionhost is initialized, a dynamic object named ALL is created by default.

**Create a dynamic account group**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. Choose **Authorize > Dynamic Objects**.
4. On the **Dynamic Account Group** tab, click **Create**. On the Create Dynamic Account Group
page, configure parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of a custom approval rule, which is used only for identification. The name must be unique. |

| Matching Condition | Specify matching conditions from the asset, account, and service aspects. Assets Match all assets: If you want the account group to dynamically match all assets, select All Assets. Match specific assets: If you want the account group to dynamically match specific assets, select Assets/Asset Directory/Rule and choose Add > Add Asset. In the Select Asset panel, select the assets to be dynamically matched. Match specific asset directories: If you want the account group to dynamically match specific asset directories, select Assets/Asset Directory/Rule and choose Add > Add Asset Directory. In the Select Asset Directory panel, select the asset directories to be dynamically matched. Match specific asset rules: If you want the account group to dynamically match specific asset rules, select Assets/Asset Directory/Rule and choose Add > Add Asset Rule. In the Create Rule panel, configure the Attribute, Match Mode, and Value parameters to create rules. Only custom attributes and Tag are available for the Attribute parameter. Supported match modes are equal to, not equal to, include, and exclude. Account Match all accounts: If you want the account group to dynamically match all accounts, select All Accounts. Match any account: If you want the account group to dynamically match any account, select <any> account. If you select this option, a regular user can perform O&M on any account after entering a valid account name and password. Match specific accounts: If you want the account group to dynamically match specific accounts, select Account Name, enter an account name, and then press the Enter key to save the account. You can specify multiple account names. The account names cannot be duplicate. Match specific account rules: If you want the account group to dynamically match specific account rules, select Rule and click Create. In the Create Rule panel, configure the Attribute, Match Mode, and Value parameters to create rules. Only custom attributes and Tag are available for the Attribute parameter. Supported match modes are equal to, not equal to, include, and exclude. Service Match all services: If you want the account group to dynamically match all services, select All Services. Match specific services: If you want the account group to dynamically match specific services, select Service and select one or more services from the drop-down list. |
|---|---|

**What to do next**

Edit a dynamic account group: On the **Dynamic Account Group** tab, find the account group that you want to manage and click **Edit** in the **Actions** column. Delete a dynamic account group: On the **Dynamic Account Group** tab, select the account group that you want to manage and click **Delete** above the list.

**Create a dynamic user group**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. Choose **Authorize > Dynamic Objects**.
4. On the **Dynamic User Group** tab, click **Create**. On the Create Dynamic User Group page,
configure parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of a custom approval rule, which is used only for identification. The name must be unique. |
| Matching Condition | Specify matching conditions from the user aspect. Only All Users is available. |

**What to do next**

Edit a dynamic user group: On the **Dynamic User Group** tab, find the user group that you want to manage and click **Edit** in the **Actions** column. Delete a dynamic user group: On the **Dynamic User Group** tab, select the user group that you want to manage and click **Delete** above the list.

### Policies

#### Configure an access control policy

You can configure an access control policy to restrict access authentication, terminal logons, and auditing.

**Create an access control policy**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Policy > Access Control**.
4. Click **Create**. In the **Create Policy** panel, configure the parameters and click **Confirm**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Status | The status of the policy. |
| Policy Name | The name of the policy, which is used only for identification. The name must be unique. |
| Priority | The priority of the policy. Valid values: 1 to 99. A smaller value specifies a higher priority. |

**Modify an access control policy**

1. In the access control policy list, find the policy that you want to manage and click **Edit** in
the **Actions** column.
2. In the **Modify Policy** panel**,** modify the policy.

**Enable an access control policy**

If a policy is disabled, you must enable the policy to allow the policy to take effect. In the access control policy list, select a policy that is in the **Disable** state and click **Enable** above the list.

**Disable an access control policy**

In the access control policy list, select a policy that is in the **Enable** state and click **Disable** above the list.

**Delete an access control policy**

In the access control policy list, select the policy that you want to manage and click **Delete** above the list.

#### Configure a host command control

**policy**

You can configure a host command control policy to configure host commands.

**Create a host command control policy**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Policy > Host Command Control**.
4. Click **Create**. In the **Create Policy** panel, configure the parameters and click **Confirm**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy, which is used only for identification. The name must be unique. |
| Priority | The priority of the policy. Valid values: 1 to 99. A smaller value specifies a higher priority. |
| Status | The status of the policy. |

| Action | The action that you want to perform after a command is matched during O&M. Valid values: Allow: If a command is matched, run the command. Close Session: If a command is matched, close the session. Block Request: If a command is matched, block the command. |
|---|---|
| Log Level | The level of a command that is displayed in logs when the command is matched during O&M. Valid values: Prompt: If a command is matched, the level of the command is displayed as info in logs. Low Risk: If a command is matched, the level of the command is displayed as low risk in logs. Medium Risk: If a command is matched, the level of the command is displayed as medium risk in logs. High Risk: If a command is matched, the level of the command is displayed as high risk in logs. Invalid: If a command is matched, the level of the command is displayed as invalid in logs. |
| Match Mode | The match mode. Valid values: Wildcard Character and Regular Expression Match. |
| Command | The command set. Each command must be unique. |

**Modify a host command control policy**

1. In the host command control policy list, find the policy that you want to manage and click
**Edit** in the **Actions** column.
2. In the **Modify Policy** panel**,** modify the policy.

**Enable a host command control policy**

If a policy is disabled, you must enable the policy to allow the policy to take effect. In the host command control policy list, select a policy that is in the **Disable** state and click
**Enable** above the list.

**Disable a host command control policy**

In the host command control policy list, select a policy that is in the **Enable** state and click
**Disable** above the list.

**Delete a host command control policy**

In the command control policy list, select the policy that you want to manage and click
**Delete** above the list.

#### Configure a database command control

**policy**

You can configure a database command control policy to control database commands.

**Create a database command control policy**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Policy > Database Command Control**.
4. Click **Create**. In the **Create Policy** panel, configure the parameters and click **Confirm**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy, which is used only for identification. The name must be unique. |
| Priority | The priority of the policy. Valid values: 1 to 99. A smaller value specifies a higher priority. |
| Status | The status of the policy. |
| Actions | The action that you want to perform if a command is matched during O&M. Valid values: Allow: runs the command. Close Session: closes the session. Block Request: blocks the command. |
| Log Level | The level of a command that is displayed in logs if the command is matched during O&M. Valid values: Prompt: If a command is matched, the level of the command is displayed as info in logs. Low Risk: If a command is matched, the level of the command is displayed as low risk in logs. Medium Risk: If a command is matched, the level of the command is displayed as medium risk in logs. High Risk: If a command is matched, the level of the command is displayed as high risk in logs. Invalid: If a command is matched, the level of the command is displayed as invalid in logs. |

| Match Mode | The match mode. Valid values: Wildcard Character and Regular Expression Match. |
|---|---|
| Command | The command set. Each command must be unique. |

**Modify a database command control policy**

1. In the list of database command control policies, find the policy that you want to manage
and click **Edit** in the **Actions** column.
2. In the **Modify Policy** panel**,** modify the policy.

**Enable a database command control policy**

If a policy is disabled, you must enable the policy to allow the policy to take effect. In the database command control policy list, select a policy that is in the **Disable** state and click **Enable** above the list.

**Disable a database command control policy**

In the list of database command control policies, select a policy that is in the **Enable** state and click **Disable** above the list.

**Delete a database command control policy**

In the list of database command control policies, select the policy that you want to manage and click **Delete** above the list.

### Auditing

You can view and manage online sessions and review historical sessions. You can also retrieve events by type, view O&M reports by dimension, and view, search for, and export operation logs.

#### Manage online sessions

You can classify online sessions by O&M user, O&M asset, and protocol. You can also play back, block, view, and search for online sessions.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Audit > Online Sessions**.

**Common search conditions**

| Search condition | Description |
|---|---|
| Project | Select the project to which the online session belongs. |

| IP or Domain | Enter the IP address or domain name of the online session. |
|---|---|
| Source IP Address | Enter the source IP address of the online session. |
| Service | Select the protocol of the online session from the drop-down list. |
| Access Control Policy Name | Enter the name of an access control policy for the online session. |
| Authorization Rule Name | Enter the name of an authorization rule for the online session. |

**Types of online sessions**

**O&M User**

After you click the **O&M User** tab, online sessions are classified by O&M user. After you select a user, the online session list on the right side displays only the online sessions of the **selected user**. Click the **sorting** icon to sort the sessions in different ways.

**O&M Asset**

After you click the **O&M Asset** tab, online sessions are classified by O&M asset. After you select an asset, the online session list on the right side displays only the online sessions of the **selected asset**.

**Service**

After you click the **Service** tab, online sessions are classified by protocol. After you select a protocol, the online session list on the right side displays only the online sessions of the **selected protocol**.

**Play back an online session**

In the online session list, find the online session that you want to manage and click **Playback** in the **Actions** column. The browser displays a new online session window and plays back the online session. The right side of the window displays session details.

**Block an online session**

In the online session list, find the online session that you want to manage and click **Block** in the **Actions** column.

**View online session details**

In the online session list, find the online session that you want to manage and click **Details** in the **Actions** column.

#### Manage historical sessions

You can review, play back, search for, and download historical sessions.

**Review a historical session**

If a green dot is displayed in the Review Status column, the session is **reviewed**. If a gray dot is displayed in the Review Status column, the session is **not reviewed**.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Audit > Historical Sessions**.
4. The following table describes different review methods for historical sessions.

| Review method | Description |
|---|---|
| Play back a session and the session is automatically reviewed. | In the Actions column, click Playback. After you play back the session, the session is marked as reviewed. |
| Review multiple sessions at a time. | Select multiple sessions and click Mark as Reviewed. The selected sessions are marked as reviewed. |
| Review all sessions. | Click Review All to mark all sessions as reviewed. |

**Export historical sessions**

Click the icon in the upper-left corner of the page to download the historical session list.

#### Query an event

You can classify sessions into various events for quick query. Search for and view an event
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Audit > Event Retrieval**.
4. Select an event type based on your business requirements.
You can search for events of the Character Command, Graphic Text, File Transfer, and Database Command types.

**Export an event**

Click a tab based on your business requirements. On the tab, click **Export Records**.

#### Manage ticket records

This topic describes how to view and export ticket records.

**Search for and view ticket records**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Audit > Ticket Records**.
4. Specify filter conditions and click **Search**.

**Export ticket records**

In the upper-right corner of the ticket list, click the icon.

### Reports

#### Manage custom reports

If the built-in O&M reports and system reports do not meet your requirements, you can create custom reports. The data sources supported by custom reports include users, assets, accounts, historical sessions, and operation logs.

**Create a custom report**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Reports > Custom Reports**.
4. Click **Create**. In the Select Data Source step, enter a template name, select a data source,
configure the Filter Conditions parameter, and then click **Next**.
5. In the **Field List** section of the **Template Configuration** step, drag one or more fields to
the Statistical Dimension and Statistical indicator sections. When you drag fields to the Statistical indicator section, the Modify Statistical indicator dialog box appears. In this dialog box, configure the display method and statistical method, and then click **Confirm**. Click **Display Settings** to specify the sorting method and display quantity. Click **Refresh**
**Preview** to view the data of the custom report.
For specific fields, you must specify the statistic level when you drag them to the Statistical Dimension section. Examples: For the Department field of the user data source, you must specify the department level for statistics. For the Asset Directory field of the asset data source, you must specify the asset directory level for statistics. The display method of statistical indicators can be Numerical Value or Column Summary Percentage. The statistical methods of statistical indicators vary based on the field type: Statistical method for fields of the string type: Count. Statistical methods for fields of the numeric type: Count, Average, Sum, Maximum Value, and Minimum Value. Statistical methods for fields of the time type: Count, Maximum Value, and Minimum Value. Some statistical indicators support classification statistics. Valid values of the display quantity in the display settings are 1 to 50. The default value is 10. The data that exceeds the display quantity limit is inducted into other items.

**What to do next**

**Modify a custom report**

Find the template that you want to modify, and click **Edit** in the **Actions** column.

**Preview a custom report**

Find the template that you want to preview, and click **Preview** in the **Actions** column.

**Export a custom report**

Find the template that you want to export, and click **Export** in the **Actions** column.

**Delete a custom report**

Select the template that you want to delete, and click **Delete** above the template list.

#### View O&M reports

You can view O&M reports from different dimensions.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Reports > O&M Reports**.
4. On the O&M Report page, view the O&M status.
Overview: View the total numbers and distributions of different items. O&M Duration: View the O&M duration of each protocol in different time periods. O&M Times: View the number of O&M sessions of each protocol in different time periods. Session Size: View the size of O&M sessions for each protocol in different time periods. Source IP Address: View the number of source IP addresses in different time periods. Transferred Files: View the number of transferred files in different time periods. Character Commands: View the number of SSH, Telnet, and Rlogin commands in different time periods. Activity Duration: View the duration of O&M operations over different protocols in different time periods.

#### System reports

Bastionhost provides a system report to visualize O&M trends from various perspectives.

**View the system report**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Reports > System Reports**.
4. View various data statistics in the system report.

**Export the system report**

In the upper-right corner of the page, click **Export**. You can export the system report as a DOCX or PDF file.

#### Manage report subscriptions

You can create a report subscription to send O&M reports, system reports, global comprehensive analysis reports, and custom reports to specific users at the scheduled time. Reports can be sent only by emails. Make sure that the email service and email addresses are configured for the specified users to receive emails.

**Create a report subscription**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Reports > Report Subscription**.
4. Click **Create Subscription**. In the Create Report Subscription panel, turn on Status,
configure the Subscription Name, Subscription content, Sending Period, and Notification Method parameters, click **Add** to add users as recipients, and then click **Confirm**.

**Send reports**

You can immediately send reports in a subscription to the specified users. Select a subscription in the subscription list and click **Send** above the list.

**Disable, enable, and delete a subscription**

Select a subscription in the subscription list and click Disable, Enable, or Delete above the list

### Configurations

#### Manage a project

Bastionhost allows you to manage assets, accounts, and authorization rules by project.

**Background information**

After you install Bastionhost, a project named default is automatically created.

**View the default project**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Project Management**.
4. On the Project Management page, view the default project.

#### Manage cloud drives

You can create a cloud drive and authorize a user to use the cloud drive.

**Note**

In standalone mode, you can create a cloud drive of the local storage, SFTP storage, or NFS storage type. In high availability mode, you can create a cloud drive of the SFTP storage or NFS storage type. The local storage type is not supported.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Settings > Disk Management**.
4. Click **Create new network disk**, select a storage type and configure the basic
information about the cloud drive. Authorize a user to use the cloud drive, and then click
**Confirm**.

#### Configure user settings

You can configure authentication security settings and multi-factor authentication settings. You can also manage authentication sources and custom attributes.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > User Configuration**.

**Configure authentication security settings**

On the **Authentication Security** tab, configure the parameters. The following table describes the parameters.

| Parameter |   | Description |
|---|---|---|
| Log On | Logon timed out | If a user is inactive for the specified period of time, theL ogon Expired dialog box appears. Then, the user must log on to Bastionhost again. |
|   | Verification Code | If you turn on this switch, a user must enter a verification code when the user logs on to Bastionhost from a browser. If the specified validity period ends, the verification code becomes invalid. Click Refresh to obtain a new verification code. If you set the validity period to 0, the verification code does not expire. |
|   | Multi-point logon | If you turn on this switch, a user can log on to Bastionhost from multiple locations at the same time. |
|   | Disable Admin | If you turn on this switch, the admin user cannot log on to Bastionhost from a browser by using the local authentication method. |
| The user is locked | Logon failed | If a user consecutively enters an invalid password five times within 30 minutes, the user is automatically locked for 30 minutes. After the user is automatically unlocked, the user can log on to Bastionhost again. |
| 8 | > Document Version: 2026090 |   |

| astionhost |   |   |
|---|---|---|
|   | Inactive for an extended period | If you turn on the switch, the system automatically disables a user when the system detects that the user has not logged on to the system for the specified period of time. |
| Password Policy | Length | The length of a password. The password must be 10 to 64 characters in length. |
|   | Complexity | The minimum numbers of digits, letters, and special characters in a password. |
|   | Relevance | The number of previous passwords that cannot be reused. Valid values: 0 to 10. The value 0 specifies that history password check is not performed. |
|   | The password must not be the same as the username | If you select this check box, the new password cannot be the same as the username. |
|   | The password must not be the same as the username in reverse order | If you select this check box, the new password cannot be the same as the username in reverse order. |
|   | Password Validity Period | The validity period of a password. A user can log on to Bastionhost by using the password only within the validity period of the password. Valid values: 0 to 360. Default value: 90. Unit: days. The value 0 specifies that the password does not expire. |
|   | Alert Before Expiration | The number of days to send an email before a password expires. If you set this parameter to 7, the system sends an email to the user 7 days before the password expires to notify the user of password expiration and change. Valid values: 0 to the validity period of the password. Default value: 7. Unit: days. The value 0 specifies that no emails are sent. |
|   | Status | The status of the policy. |
|   | Name | The name of the policy, which is used only for identification. The name must be unique. |
|   | Priority | The priority of the review rule. Valid values: 1 to 99. A larger value specifies a higher priority. |

|   | Logon IP Address Restriction | The source IP addresses. You can configure the whitelist and blacklist for source IP addresses. If you select The following IP addresses in the blacklist are denied and enter IP addresses or CIDR blocks in the field of the Logon IP Address Restriction section, the access requests from the IP addresses or CIDR blocks are blocked. If you select The following IP addresses in the whitelist are allowed and enter IP addresses or CIDR blocks in the field of the Logon IP Address Restriction section, the access requests from only the IP addresses or CIDR blocks are allowed. |
|---|---|---|
| Access Control Policy Click Add. In the Create Access Control Policy panel, configure the parameters. |   |   |
|   | Logon Time Restriction | The periods of time during which user logons are allowed and blocked. |
|   | Valid MAC Range for Logon | The source MAC addresses. You can configure the whitelist and blacklist for source MAC addresses. This feature is supported only if Internet Explorer is used. If you select The following MAC addresses in the blacklist are denied and enter MAC addresses in the field of the Valid MAC Range for Logon section, the access requests from the MAC addresses are blocked. If you select The following MAC addresses in the whitelist are allowed and enter MAC addresses in the field of the Valid MAC Range for Logon section, the access requests from only the MAC addresses are allowed. |
|   | Scope of Application | The effective scope of the policy. The scope includes users, user groups, and departments. To add a department, select a department from the drop- down list. You can select one or more departments. To delete a department, click the cross (x) icon next to a department name. To add users or user groups, select User/User Group and choose Add > Add User or Add > Add User Group. In the panel that appears, select the users or user groups and click Confirm. To delete a user or user group, select the user or user group and click Delete. |

**Configure authentication methods**

Bastionhost supports the following authentication methods: local, Remote Authentication Dial In User Service (RADIUS), Active Directory (AD), Lightweight Directory Access Protocol (LDAP), Central Authentication Service (CAS), and Security Assertion Markup Language 2.0 (SAML 2.0).

**Configure the local authentication method**

|   | Important After you disable the local authentication method, users cannot log on to Bastionhost by using a password. Proceed with caution. |   |
|---|---|---|

On the **Authentication Source** tab, enable or disable the local authentication method in the Local Authentication section.

**Configure the RADIUS authentication method**

You can create a RADIUS server to authenticate users who want to log on to Bastionhost. RADIUS is a protocol commonly used for network authentication and authorization. A RADIUS server receives the connection request of a user, authenticates the user, and then returns the required configuration information to the user. On the **Authentication Source** tab, click RADIUS. In the **Configure RADIUS** panel, configure a RADIUS server and click **Test Connectivity**. After the test succeeds, click **Save**.

| Parameter | Description |
|---|---|
| Status | The switch to enable or disable the RADIUS authentication method. Users can use the RADIUS authentication method only after you enable the method. |
| Authentication Source Name | The name of the authentication method, which is used only for identification. The name must be unique. |
| Server Address | The IP address of the RADIUS server. |
| Port | The port of the RADIUS server. |
| Authentication Key | The authentication key of the RADIUS server. |
| NAS Identifier | The identifier of the RADIUS server, which is the nastype field in the configuration file of the RADIUS server. If the configuration file does not contain the nastype field, enter the IP address of Bastionhost. |
| Validation Mode | The authentication mode of the RADIUS server. Username + Password: If a user wants to log on to Bastionhost, the user must enter the username and password and pass the authentication of the RADIUS server. Username + Dynamic Token: If a user wants to log on to Bastionhost, the user must enter the username and a dynamic password and pass the authentication of the RADIUS server. Username + Dynamic Token + Token PIN: If a user wants to log on to Bastionhost, the user must enter the username, a dynamic password, and the token PIN code, and pass the authentication of the RADIUS server. |
|   | A dynamic password can be obtained from the authenticator that is bound to the RADIUS server. The token PIN code is the PIN code that is configured on the RADIUS server. |

| A local user is automatically created and bound after the authentication is passed | If you select this check box and a user that passes the authentication of the RADIUS server does not exist in Bastionhost, the user is automatically created in Bastionhost. |
|---|---|
| Default User Role | The role of the user that is automatically created in Bastionhost after the user passes the authentication of the RADIUS server. |

**Configure the AD authentication method**

You can create one or more AD servers to authenticate users who want to log on to Bastionhost. On the **Authentication Source** tab, click AD. In the **Configure AD** panel, configure the parameters to create an AD server and click **Test Connectivity**. The following table describes the parameters. After the test succeeds, click **Save**.

| Parameter | Description |
|---|---|
| Authentication Source Name | The name of the authentication method, which is used only for identification. The name must be unique. |
| Server Address | The IP address of the AD server. |
| Domain | The domain name of the AD server. |
| Port | The port number of the AD server. If you select SSL, data is transmitted over SSL. This ensures higher security. |
| Base DN | The root node of the AD server, which is the start directory to query when the AD server receives an authentication request. For example, dc=test,dc=com indicates that the user is obtained from the root node of the domain test.com server. |
| A local user is automatically created and bound after the authentication is passed | If you select this check box and a user that passes the authentication of the AD server does not exist in Bastionhost, the user is automatically created in Bastionhost. |
| Verify User Base DN during Logon Authentication | If you select this check box, when an AD-authenticated user logs on to Bastionhost, the system checks whether the base distinguished name (DN) configured during user synchronization is the same as the base DN of the user on the current AD server. |
| Automatic Synchronization | If you turn on the switch, the system synchronizes user information from the AD server to Bastionhost based on the specified synchronization cycle. |

| Username | The username and password of the user on the AD server. You can also leave the password parameter empty. |
|---|---|
| Password |   |
| Filter | The filter conditions. Users that meet the conditions are synchronized to Bastionhost. |
| Synchronization Content | The synchronization operation. Synchronize To: Select the department to which the users synchronized from the AD server belong in Bastionhost. Synchronous Creation: If a synchronized department, user group, or user does not exist in Bastionhost, the department, user group, or user is automatically created in Bastionhost. Synchronous Update: If you select this check box and the synchronized user information in Bastionhost is different from the user information on the AD server, the user information in Bastionhost is updated based on the user information on the AD server. This feature requires that the AD authentication method is configured for the user. Synchronous Deletion: If you select this option and a user that exists in Bastionhost does not exist on the AD server, the user is deleted from Bastionhost. This feature requires that the AD authentication method is configured for the user. Disable User: If you select this option and a user that exists in Bastionhost does not exist on the AD server, the user is disabled in Bastionhost. This feature requires that the AD authentication method is configured for the user. No Change: If you select this option and a user that exists in Bastionhost does not exist on the AD server, the user is retained in Bastionhost. This feature requires that the AD authentication method is configured for the user. |
| Default User Role | The role of the user that is automatically created in Bastionhost after the user passes the authentication of the AD server. |
| Mapping Relationship | The mapping between local user attributes in Bastionhost and user attributes on the AD server. By default, the mapping between usernames exists. Click Add to add user attributes such as the name, email address, mobile phone number, and description. |

Enable or disable an AD server: After you add an AD server, it is disabled by default. Before you can use the AD server, you must manually enable the server. If you no longer use the AD server, you must manually disable the server. You can turn on the switch in the
**Configure AD** panel to enable or disable an AD server.
Manually synchronize users: If automatic synchronization is enabled, users on the AD server are periodically synchronized based on the specified synchronization cycle. If automatic synchronization is disabled, click AD. In the **Configure AD** panel, click
**Synchronize Users** in the Actions column. Then, users are immediately synchronized from
the AD server to Bastionhost. The synchronized users are displayed on the **User**
**Management** page.

**Configure the LDAP authentication method**

LDAP is a common access protocol for directory services on the Internet. An LDAP server is used to query and update LDAP directories, including user account directories. An LDAP server can effectively solve user account issues of various network services. On the **Authentication Source** tab, click LDAP. In the **Configure LDAP** panel, configure an LDAP server and click **Test Connectivity**. After the test succeeds, click **Save** or **Save and**
**Synchronize**.
Save: Save only the configured LDAP server information. Save and Synchronize: Save the configured LDAP server information and manually synchronize the departments, user groups, and users on the LDAP server to Bastionhost based on the configured synchronization content.

| Parameter | Description |
|---|---|
| Status | The switch to enable or disable the LDAP authentication method. Users can use the LDAP authentication method only after you enable the method. |
| Authentication Source Name | The name of the authentication method, which is used only for identification. The name must be unique. |
| Server Address | The IP address of the LDAP server. |
| Port | The port of the LDAP server. |
| Base DN | The root node of the LDAP server, which is the start directory to query when the LDAP server receives an authentication request. For example, dc=test,dc=com indicates that the user is obtained from the root node of the domain test.com server. |
| A local user is automatically created and bound after the authentication is passed | If you select this check box and a user that passes the authentication of the LDAP server does not exist in Bastionhost, the user is automatically created in Bastionhost. |
| Verify User Base DN during Logon Authentication | If you select this check box, when an LDAP-authenticated user logs on to Bastionhost, the system checks whether the base DN configured during user synchronization is the same as the base DN of the user on the current LDAP server. |
| Automatic Synchronization | If you turn on the switch, the system synchronizes user information from the LDAP server to Bastionhost based on the specified synchronization cycle. |

| Username | The username and password of the user on the LDAP server. You can also leave the password parameter empty. |
|---|---|
| Password |   |
| Filter | The filter conditions. Users that meet the conditions are synchronized to Bastionhost. |
| Synchronization Content | The synchronization operation. Synchronize To: Select the department to which the users synchronized from the LDAP server belong in Bastionhost. Synchronous Creation: If a synchronized department, user group, or user does not exist in Bastionhost, the department, user group, or user is automatically created in Bastionhost. Synchronous Update: If you select this check box and the synchronized user information in Bastionhost is inconsistent with the user information on the LDAP server, the user information in Bastionhost is updated based on the user information on the LDAP server. This feature requires that the LDAP authentication method is configured for the user. Synchronous Deletion: If you select this option and a user that exists in Bastionhost does not exist on the LDAP server, the user is deleted from Bastionhost. This feature requires that the LDAP authentication method is configured for the user. Disable User: If you select this option and a user that exists in Bastionhost does not exist on the LDAP server, the user is disabled in Bastionhost. This feature requires that the LDAP authentication method is configured for the user. No Change: If you select this option and a user that exists in Bastionhost does not exist on the LDAP server, the user is retained in Bastionhost. This feature requires that the LDAP authentication method is configured for the user. |
| Default User Role | The role of the user that is automatically created in Bastionhost after the user passes the authentication of the LDAP server. |
| Mapping Relationship | The mapping between local user attributes in Bastionhost and user attributes on the LDAP server. By default, the mapping between usernames exists. Click Add to add user attributes such as the name, email address, mobile phone number, and description. |

**Configure the CAS authentication method**

If you enable the CAS authentication method, a user requires only one authentication by the CAS server by using the username and password. Then, the user can access other mutually trusted application systems without the need for logons. On the **Authentication Source** tab, click CAS. In the **Configure CAS** panel, configure the parameters to create an CAS server and click Test Connectivity. The following table describes the parameters. After the test succeeds, click **Save**.

| Parameter | Description |
|---|---|
| Status | The switch to enable or disable the CAS authentication method. Users can use the CAS authentication method only after you enable the method. |
| Authentication Source Name | The name of the authentication method, which is used only for identification. The name must be unique. |
| Authentication Source Logo | The custom logo of the CAS server. Click Upload Image and select an image from your computer. |
| CAS Version | The version of the CAS server. Valid values: CAS2.0 and CAS3.0. |
| CAS URI Prefix | The URL of the CAS server. |
| CAS Logon URL | The URL of the CAS server for single sign-on (SSO). If a CAS- authenticated user who does not log on to the CAS server and Bastionhost wants to log on to Bastionhost from a browser, the user is redirected to this URL for logon. |
| CAS Server Certificate | The certificate of the CAS server. Click Upload Certificate, select a PEM certificate file from your computer, and then upload the file to Bastionhost. |
| A local user is automatically created and bound after the authentication is passed | If you select this check box and a user that passes the authentication of the CAS server does not exist in Bastionhost, the user is automatically created in Bastionhost. |
| Default User Role | The role of the user that is automatically created in Bastionhost after the user passes the authentication of the CAS server. |
| Admin User Mapping | After a user on the CAS server logs on to Bastionhost by using SSO, the user is mapped to the admin user if the user attributes returned by the CAS server include the configured attribute and its value is the same as the configured attribute value. |
| Set CAS as Default Logon Method | If you select this check box, a user who accesses Bastionhost from a browser is automatically redirected to the logon page of the CAS server for authentication. If you do not select this check box, a user who accesses Bastionhost from a browser must manually click the CAS icon to go to the logon page of the CAS server. |

| Exit from CAS Server upon Logoff | If you select this check box, a CAS-authenticated user automatically logs off from the CAS server when the user logs off from Bastionhost. |
|---|---|

**Configure the SAML 2.0 authentication method**

If you enable the SAML 2.0 authentication method, a user requires only one authentication by the SAML 2.0 server by using the username and password. Then, the user can access other mutually trusted application systems without the need for logons. On the **Authentication Source** tab, click SAML2. In the **Configure SAML2** panel, configure the parameters to create an SAML 2.0 server and click **Save**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Status | The switch to enable or disable the SAML 2.0 authentication method. Users can use the SAML 2.0 authentication method only after you enable the method. |
| Authentication Source Name | The name of the authentication method, which is used only for identification. The name must be unique. |
| Authentication Source Logo | The custom logo of the SAML 2.0 server. Click Upload Image and select an image from your computer. |
| Exit from SAML Server upon Logoff | If you select this check box, an SAML 2.0-autenticated user automatically logs off from the SAML 2.0 server when the user logs off from Bastionhost. You must also configure the IDP Logout URL parameter. |
| IDP Login URL | The URL used to log on to the SAML 2.0 server by using SSO. You can obtain the URL by clicking Show Meta Information on the installation page after the SAML 2.0 server is started. |
| IDP Logout URL | The URL used to log off from the SAML 2.0 server by using SSO. You can obtain the URL by clicking Show Meta Information on the installation page after the SAML 2.0 server is started. |
| SP ACS URL | The SAML 2.0 Assertion Consumer Service (ACS) URL of Bastionhost. You must enter this URL in the SAML 2.0 server configuration. |

| SAML2 Server Certificate | The certificate of the SAML 2.0 server. Click Upload Certificate, select a PEM certificate file from your computer, and then upload the file to Bastionhost. |
|---|---|
| IDP Entity ID | The ID of the SAML 2.0 server. |
| SP Entity ID | The ID of Bastionhost. Default value: USM. |
| A local user is automatically created and bound after the authentication is passed | If you select this check box and a user that passes the authentication of the CAS server does not exist in Bastionhost, the user is automatically created in Bastionhost. |
| Default User Role | The role of the user that is automatically created in Bastionhost after the user passes the authentication of the SAML 2.0 server. |
| Admin User Mapping | After a user on the SAML 2.0 server logs on to Bastionhost by using SSO, the user is mapped to the admin user if the user attributes returned by the SAML 2.0 server include the configured attribute and its value is the same as the configured attribute value. |
| Mapping Relationship | The mapping between local user attributes in Bastionhost and user attributes on the SAML 2.0 server. By default, the mapping between usernames exists. Click Add to add user attributes such as the name, email address, mobile phone number, and description. |
| Set SAML2 as Default Logon Method | If you select this check box, a user who accesses Bastionhost from a browser is automatically redirected to the logon page of the SAML 2.0 server for authentication. If you do not select this check box, a user who accesses Bastionhost from a browser must manually click the CAS icon to go to the logon page of the SAML 2.0 server. |
| Exit Signature | If you select this check box, the logoff request is signed when a user logs off from Bastionhost. |
| Download Metadata | Click Download Metadata to download SAML 2.0 metadata. |

**Configure the multi-factor authentication method**

If you enable the multi-factor authentication method, after a user enters a valid username and password, the user must also enter a valid one-time password (OTP) or text message verification code before the user can log on to Bastionhost. By default, the multi-factor authentication method is disabled. On the **Multi-factor Authentication** tab, configure the multi-factor authentication method.

| Parameter | Description |
|---|---|
| Mobile Phone OTP | If you select this check box, a user must bind an OTP app on the Personal Information page of the personal workbench. A user can also be prompted to configure an OTP app the first time the user logs on to Bastionhost from a browser. Then, the user can obtain an OTP and complete multi-factor authentication when the user logs on to Bastionhost. The time deviation is 5 minutes by default and ranges from 0 to 5 minutes. If the time deviation between the mobile phone on which the OTP app is installed and Bastionhost exceeds the specified value, the obtained OTP is invalid. |
| OTP | If you select this check box, you must import a token file on the OTP Management page and grant a user the token permissions. Then, the user can obtain an OTP and complete multi-factor authentication when the user logs on to Bastionhost. |
| SMS Token | If you select this check box, you must configure text message settings in the SMS configuration section. This way, a user can obtain a verification code from a text message and complete multi-factor authentication when the user logs on to Bastionhost. |

**Configure custom attributes**

You can configure custom attributes for users. On the **Custom Attribute** tab, click **Create** to create a custom attribute.

| Parameter | Description |
|---|---|
| Name | The name of the custom attribute. The name must be unique. |
| Type | The type of the custom attribute. Valid values: String, Digits, Options, and Date. |
| Length Limit | If you set the Type parameter to String, you must specify the maximum length of the string. |
| Option List | If you set the Type parameter to Options, you must configure options. Enter one option in each row. |
| Valid Scope | If you set the Type parameter to Date, you must specify a time range. Valid values: Unlimited and Custom. If you set the Type parameter to Digits, you must specify a numeric range. |

#### Configure role settings

**Create a role**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Role Configuration**.
4. Click **Create**. In the **Create Role** panel, enter a name and description for the role, select
the required permissions, and then click **Confirm**.

**Modify the information about a role**

1. In the role list, find the role that you want to manage and click **Edit** in the **Actions** column.
2. In the Modify Role panel, modify the name and description of the role, select the required
permissions, and then click **Confirm**.

**Delete a role**

1. In the role list, find the role that you want to manage and click **Delete** in the **Actions**
column.
2. In the message that appears, click **Confirm**.

#### Configure assets

##### Manage asset directories

**Create an asset directory**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the Asset Directory tab, find the root directory and click **Create Child Directory** in the
**Actions** column.
5. In the Create Child Directory panel, enter a directory name and click Confirm.

**What to do next**

Delete an asset directory: Find the asset directory that you want to manage and click
**Delete** in the **Actions** column. In the message that appears, click Confirm.
Modify an asset directory: Find the asset directory that you want to manage and click **Edit** in the **Actions** column. In the Modify Directory panel, modify the asset directory.

##### Manage network settings

**Create a LAN**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Asset > Network Management**.
4. Click **Add LAN**. In the **Create Network** panel, configure the following parameters and
click **Confirm**.

| Parameter | Description |
|---|---|
| Network Name | The custom name of the LAN, which is used only for identification. |
| Remark | The remarks of the LAN. |
| Proxy Server | If assets are in different LANs and the LANs are isolated, you can configure a proxy server. This way, users can access the assets in the LANs by using the proxy server. Create a proxy server Click Add. In the Create Proxy Server panel, select the protocol between Bastionhost and the proxy server, enter the IP address of the proxy server, the port number of the proxy server, and the username and password of the proxy server. Click Test Connectivity. After the connection is established, click Confirm. SSH and SOCKS5 are supported. If you select SOCKS5, you can leave the username and password empty for the proxy server and set the Authentication Method parameter to None. Modify the information about a proxy server Click Edit. In the Modify Proxy Server panel, modify the information about the proxy server and click Test Connectivity. After the connection is established, click Confirm. Delete a proxy server Click Delete. |

**Modify the information about a LAN**

Click the icon. In the **Modify Network** panel, modify the information about the LAN and click **Confirm**.

**Delete a LAN**

After you delete a LAN, assets in the LAN are automatically moved to the default LAN. You cannot delete the default LAN. Click the icon.

**View the assets in a LAN**

Click the **number of assets** in a LAN. On the **Asset Management** page, view the assets in the network.

##### Configure a password change script

You can configure a password change script and associate the script with multiple accounts to change the passwords of the accounts at a time.

**Create a password change script**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Account > Password Change Script**.
4. Click **Create**. In the **Add Password Change Script** panel, configure the Script Name and
Script Command parameters and click **Confirm**. Script commands support interactive commands and special keys, which can be included in a script at the same time. Add Interactive Command: Click **Add Interactive Command**. In the **Add Interactive**
**Command** panel, configure the Prompt and Command parameters, select **Break Line**
**After Command Is Submitted** based on your business requirements, and then click
**Confirm**.
Add Special Key: Click **Add Special Key**. In the **Add Interactive Command** panel, configure the Special Key parameter and click **Confirm**.

**Associate a password change script with an account**

You can associate a password change script with an account.
1. In the password change script list, find the script that you want to manage and click
**Associate Account** in the **Actions** column.
2. In the **Associate Account** panel, select the required account and click **Confirm**.
3. In the message that appears, click **Confirm**.

**Dissociate a password change script from an account**

1. In the password change script list, find the script that you want to manage and click the
number in the **Associated Accounts** column.
2. In the **Associated Account** panel, select the required account and click **Disassociate**.

**Export a password change script**

In the password change script list, find the script that you want to manage and click **Export** in the **Actions** column.

**Modify a password change script**

1. In the password change script list, find the script that you want to manage and click **Edit** in
the **Actions** column.
2. In the **Modify Password Change Script** panel, modify the parameters and click **Confirm**.

**Delete a password change script**

1. In the password change script list, select the script that you want to manage and click
**Delete** above the script list.
2. In the message that appears, click **Confirm**.

##### Asset Template

You can create an asset template by configuring information such as the protocols, ports, accounts, system code, and account switch command. When you create an asset, you can select the asset template to quickly reference the configurations.

**Create an asset template**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the **Asset Template** tab, click **Create**. In the **Create Template** panel, configure the
parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Template Name | The name of the custom template, which is used only for identification. |
| Template Type | The type of the template. Valid values: OS, DB, NETWORK, and APP. |
| Secondary Type | If you set the Template Type parameter to OS, you must select an operating system. Valid values: Linux, Unix, and Windows. |
| Enable Service | Select the protocols supported by the asset and clickC onfigure. In the Configure Service panel, configure the port numbers of the selected protocols. If you do not configure port numbers, the default port number of each protocol is used. |
| Default Account | If the same username and password are used for the assets created by using the asset template, you can add the username and password to the template to quickly import the username and password to the assets. Add an account Click Add. In the Add Asset Account panel, configure the following parameters: Account Name, Password, Apply to Service, Automatic Password Change, Password Change Script, and Custom Attribute. Then, click Confirm. If you select SSH for the Apply to Service parameter, you can select an SSH key. Then, users can use the SSH key to access the asset. You must create the SSH key on the Key Management page in advance. If you select ORACLE for the Apply to Service parameter, you must select a value for the Connected To parameter based on the user role of the account in Oracle. You must create a password change script on the Password Change Script page in advance. You can manage custom attributes on the Custom Account Attribute tab. Modify an account Click Edit. In the Modify Asset Account panel, modify the account information and click Confirm. Delete an account Click Delete to delete the account. |
| System Code | The system code. |

| Account Switch Command | The command used to switch between accounts. If the SSH- or Telnet-based accounts created by using the asset template use the same account switch command, you can configure the script in the asset template for centralized management. |
|---|---|

**Modify an asset template**

1. In the asset template list, find the template that you want to manage and click **Edit** in the
**Actions** column.
2. In the **Modify Template** panel, modify the template information and click **Confirm**.

**Delete an asset template**

1. In the asset template list, find the template that you want to manage and click **Delete** in
the **Actions** column.
2. In the message that appears, click **Confirm**.

##### Configure O&M settings

On the O&M Configuration tab, you can configure the O&M logon, O&M duration, and number of sessions.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the **O&M Configuration** tab, configure the parameters and click **Save**. The following
table describes the parameters.

| Parameter |   | Description |
|---|---|---|
| Unauthorized Logon | Allow Unauthorized Logons from Web | After you select this check box, the unauthorized logon feature is displayed on the O&M page of the personal workbench. This feature allows users to log on to unauthorized assets from a browser. |
|   | Collect Unauthorized Logons | After you select this check box, the system automatically collects the authorization relationships between users and assets after unauthorized users log on to Bastionhost, and displays the authorization relationships on the Authorize > Unauthorized Logon page. If an administrator approves the authorization relationships, the system automatically creates O&M rules. This eliminates the need for manual authorization when the users log on to the assets to perform O&M operations. |
|   | Collect Passwords of Host Accounts | After you select this check box, the system automatically collects the account passwords of unauthorized logon assets. |

|   | Automatically create authorization rules | After you select this check box, the system automatically creates an authorization relationship (O&M rule) when an unauthorized user logs on to Bastionhost. This eliminates the need for manual authorization when the user logs on to the required asset to perform O&M operations. |
|---|---|---|
| SSH Logon | Allow Logon to Host Using User Password | After you select this check box, users can log on to assets by using the Bastionhost account. You can enable this feature in scenarios in which a user is an Active Directory (AD)- or a Lightweight Directory Access Protocol (LDAP)- authenticated user and the username of the account is the same as the name of the AD- or LDAP-authenticated user. |
|   | Allow Logon to Host Using User SSH Private Key | After you select this check box, users can directly use the SSH private key to log on to assets without passwords. |
|   | Allow Logon to SSH Server in SSH-Agent- Forwarding Mode | After you select this check box, the system supports the SSH-agent-forwarding feature. If the same SSH private key is used to log on to Bastionhost and the SSH server, you can enable this feature. If Xshell is used, you must configure SSH banners in the SSH logon section. |
|   | Allow Sending Environment Variable | After you select this check box, users can send variables, such as O&M user information and O&M source IP addresses during SSH-based O&M. You can specify the variable names based on your business requirements. |
|   | Use Command Line through Shell | After you select this check box, users can log on to assets by using CLIs when the users perform SSH-based O&M. |

| If the idle time exceeds xx, the connection is automatically cut off | After you specify a duration, an idle O&M session is automatically disconnected after the duration of the O&M session reaches the specified value. Valid values: 1 to 43200. The value 0 specifies that an idle O&M session is not automatically disconnected. Different protocols have different definitions of idle O&M sessions: RDP and VNC: No data is sent from the client. FTP: No data is sent from the command channel and data tunnel. SSH, Telnet, Rlogin, SFTP, MySQL, SQL Server, Oracle, DB2, PostgreSQL, KingbaseES, and DM: No data is sent from the client and the server. |
|---|---|
| When the authorization expires, immediately block the session | After you select this check box, O&M sessions are automatically disconnected after O&M rules expire. |
| Each user can open at most xx sessions | After you specify a value, the number of sessions that a user can establish at the same time cannot exceed the value. Valid values: 0 to 100. The value 0 specifies that the number of sessions that a user can establish at the same time is unlimited. |
| O&M Method | If you select an O&M method, the O&M method is supported. If you do not select an O&M method, the O&M method is not supported. Valid values: Local Client and HTML5 Client. |
| Remote Client | After you turn on the switch, users can perform O&M operations over Oracle, MySQL, SQL Server, PostgreSQL, or DB2 by using only remote clients. By default, this switch is turned off. |

##### Configure custom attributes for assets

**Create a custom attribute**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the **Custom Asset Attribute** tab, click **Create**. In the **Create Attribute** panel,
configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|

| Name | The name of the custom attribute. The name must be unique. |
|---|---|
| Type | The type of the custom attribute. Valid values: String, Digits, Options, and Date. |
| Length Limit | If you set the Type parameter to String, you must specify the maximum length of the string. |
| Option List | If you set the Type parameter to Options, you must configure options. Enter one option in each row. |
| Valid Scope | If you set the Type parameter to Date, you must specify a time range. Valid values: Unlimited and Custom. If you set the Type parameter to Digits, you must specify a numeric range. |

**Modify a custom attribute**

1. On the **Custom Asset Attribute** tab, find the custom attribute that you want to manage
and click **Edit** in the **Actions** column.
2. In the **Modify Attribute** panel, modify the custom attribute and click **Confirm**.

**Delete a custom attribute**

1. On the **Custom Asset Attribute** tab, find the custom attribute that you want to manage
and click **Delete** in the **Actions** column.
2. In the message that appears, click **Confirm**.

##### Configure custom attributes for accounts

**Create a custom attribute**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the **Custom Account Attribute** tab, click **Create**. In the **Create Attribute** panel,
configure the parameters and click **Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Name | The name of the custom attribute. The name must be unique. |
| Type | The type of the custom attribute. Valid values: String, Digits, Options, and Date. |

| Length Limit | If you set the Type parameter to String, you must specify the maximum length of the string. |
|---|---|
| Option List | If you set the Type parameter to Options, you must configure options. Enter one option in each row. |
| Valid Scope | If you set the Type parameter to Date, you must configure a time range. Valid values: Unlimited and Custom. If you set the Type parameter to Digits, you must configure a number range. |

**Modify a custom attribute**

1. On the **Custom Account Attribute** tab, find the custom attribute that you want to
manage and click **Edit** in the **Actions** column.
2. In the **Modify Attribute** panel, modify the custom attribute and click **Confirm**.

**Delete a custom attribute**

1. On the **Custom Account Attribute** tab, find the custom attribute that you want to
manage and click **Delete** in the **Actions** column.
2. In the message that appears, click **Confirm**.

#### Manage operating systems

You can add and manage operating systems and view the number of assets and asset templates associated with existing operating systems.

**Add an operating system**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > Asset Configuration**.
4. On the **Operating System** tab, click **Create**. In the Create operating system dialog box,
select a platform, enter a name, and then click **Confirm**.

**What to do next**

Modify an operating system: Find the operating system that you want to manage and click
**Edit** in the **Actions** column. In the Edit operating system dialog box, modify the operating
system. Disable operating systems: Select one or more operating systems that you want to manage and click **Disable** above the list. Enable operating systems: Select one or more operating systems that you want to manage and click **Enable** above the list. Remove an operating system: Find the operating system that you want to manage and click
**Delete** in the **Actions** column. In the message that appears, click Confirm.

#### Connect to an application system

A third-party application system can call API operations to connect to Bastionhost. After the application system is connected to Bastionhost, the application system can query the accounts, passwords, and keys of authorized assets.

**Create an access token**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Configure > System Connection**.
4. On the **Access Token** section, click **Create**. In the **Create Access Token** panel, configure
the parameters described in the following table and click **Confirm**.

| Parameter | Description |
|---|---|
| Name | The name of the application system, which is used only for identification. The name must be unique. |
| Permission | The user whose access token is in the bastion host. The access token has the same permissions as the selected user. The user must have the asset management or account management permissions to access the authorized account by calling API operations. |
| Authentication Method | Only token is supported. |

**Manage access tokens**

Modify an access token: Find the access token that you want to manage and click **Edit** in the **Actions** column. View access logs: Find the access token that you want to manage and click **Access Logs** in the **Actions** column. In the **Access Logs** panel, view the access time and source IP address of the application system. Delete an application system: Select the access token that you want to manage and click
**Delete** above the access token list. In the message that appears, click Confirm.

**API access control**

1. In the **API Access Control** section, select **Whitelist Mode** for Protection Mode and click
**New**.
2. In the **Add Whitelist IP** panel, enter an IP address or a CIDR block and click **Confirm**.

### System

#### Manage network settings

You can view network interface information.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Network Management**.
4. On the Network Settings page, view the network interface information.

##### View NIC configurations

You can view the information about network interface controllers (NICs).
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Network Management**.
4. In the **NIC Configuration** section of the **Network Settings** tab, view the NIC information.

##### Configure ports

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **Port Configuration** tab, enable or disable a port, or change a port number, and
then click **Save**.

##### Configure security settings

If you select High Security in the TLS Security Configuration section, only TLS 1.2 is supported for the File Transfer Protocol Secure (FTPS), Reverse Direction Grant (RDG), and RDP protocols. Triple Data Encryption Standard (3DES) and Secure Hash Algorithm 1 (SHA1) are disabled. This improves system security over the FTPS, RDG, and RDP protocols.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **Security Configuration** tab, select or deselect High Security and click **Save**.

##### Configure communication settings

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **Communication Configuration** tab, configure the parameters and click **Save**. The
following table describes the parameters.

| Parameter | Description |
|---|---|
| Mode | Select the mode of the SM communication. Compatible with SM Communications: supports Rivest- Shamir-Adleman (RSA) and SM SM Communications Only: supports only SM |

##### Manage web certificates

Bastionhost allows you to upload an SM or RSA certificate, which helps to prevent man-in-themiddle attacks, ensure transmission security, and meet compliance requirements such as Multi-Level Protection Scheme (MLPS). This topic describes how to upload an SM or RSA certificate.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Network Management**.
4. In the **Custom Web Certificate** section of the **Web Certificate Configuration** tab,
upload an SM or RSA certificate and click **Save**. The following table describes the related parameters.

| Parameter |   | Description |
|---|---|---|
| SM Certific ate | Encryption Certificate | Upload an SM certificate. The certificate must have the Key Encipherment or Key Agreement field. Only certificates in the PEM, DER, and CRT formats are supported. |
|   | Encryption Private Key | Upload an encryption private key. Only SM2 algorithm keys in the KEY format are supported. |
|   | Encryption Token | Enter the encryption password. Leave this parameter empty if no password is set. |
|   | Signature Certificate | Upload a signature certificate. The certificate must support digital signature. Only certificates in the PEM, DER, and CRT formats are supported. |
|   | Signature Private Key | Upload a signature private key. Only SM2 algorithm keys in the KEY format are supported. |

|   | Signature Token | Enter the signature password. Leave this parameter empty if no password is set. |
|---|---|---|
|   | Certificate Chain | Upload a file that contains multiple PEM certificates separated by blank lines. The certificate chain must be associated with the uploaded certificates. |
|   | Certificate | Upload an RSA certificate. Only certificates in the PEM, DER, and CRT formats are supported. |
|   | Private Key | Upload a private key. Only RSA algorithm keys in the KEY format are supported. |
| RSA Certific ate |   |   |
|   | Encryption Token | Enter the encryption password. Leave this parameter empty if no password is set. |
|   | Certificate Chain | Upload a file that contains multiple PEM certificates separated by blank lines. The certificate chain must be related to the uploaded certificates. |

##### Configure firewall settings

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Network Management**.
4. On the **Firewall** tab, click **Change** to set the Protection Mode parameter to Whitelist Mode
or Blacklist Mode, and click **Confirm**. If the Protection Mode parameter is set to Disable, the firewall feature is disabled, and no IP address whitelist or blacklist needs to be maintained. If the Protection Mode parameter is set to Blacklist Mode, click the Blacklist tab, and then click **Add Blacklist**. In the Add Blacklist panel, configure the blacklist by adding or updating IP addresses and CIDR blocks, and click **Confirm**. If the Protection Mode parameter is set to Whitelist Mode, click the Whitelist tab, and then click **Add Whitelist**. In the Add Whitelist panel, configure the whitelist by adding or updating IP addresses and CIDR blocks, and click **Confirm**.

#### HA cluster

You can view the information about cluster nodes.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > HA or Cluster**.
4. In the Cluster Node List section, view the information about cluster nodes.

#### Configure Syslog servers

You can configure one or more Syslog servers.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **Log Shipping** tab, change the Status switch, configure the parameters, and then
click **Send Test Data**. After the test succeeds, click **Save**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Sender ID | The ID of the user who sends logs to the Syslog server, which is used for identification. |
| Server Address | The IP address and port of the Syslog server. Click the icon to add a Syslog server. Click the icon to delete the Syslog server. |
| Send Data | The type of logs that you want to send to the Syslog server. Valid values: Operation Logs and Alert Logs. |

#### Manage data

##### Manage basic data

**View the OSS storage status**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Data Management**.
4. On the **Data Management** tab, view the storage status of Object Storage Service (OSS).

**Configure automatic storage cleanup**

On the **Data Management** tab, configure automatic storage cleanup and click **Save**.

##### Manage a file server

**Create a file server**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **File Server** tab, click **Create**.
5. In the **Create File Server** panel, configure the parameters and click**Test Connectivity**.
After the test succeeds, click **Save**. The following table describes the parameters

| Parameter | Description |
|---|---|
| Name | The name of the file server, which is used only for identification. |
| Address | The address of the file server. |
| Service | The protocol used by the file server. |
| Port | The port number of the file server. The default port number for FTP is 21 and for SFTP is 22. Enter the actual port number of the file server. |
| Account Name | The username and password used to log on to the file server. |
| Password |   |

**Modify a file server**

1. On the **File Server** tab, find the server that you want to manage and click **Edit** in the
**Actions** column.
2. In the **Modify File Server** panel, modify the information and click **Test Connectivity**.
After the test succeeds, click **Save**.

**Delete a file server**

On the **File Server** tab, select the file server that you want to manage and click **Delete**.

##### Configure system backup files

You can back up the current configurations and data of the system. If an error occurs or data is lost, you can use the system backup files for restoration.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Data Management**.
4. On the **Configuration Backup** tab, perform the related operations.

**Configure the sending method for system backup files**

After you turn on the switch, the system backup files that are automatically and manually created are sent to the configured file server for storage. Make sure that you configured a file server. In the **System Backup Sending Method** section, turn on the switch, select a file server, enter the absolute path of system backup files, and then click **Save**.

**Manually create a system backup file**

In the **Backup List** section, click **Create**. In the **Create System Configuration Backup** panel, configure the Remark parameter and click **Confirm** to manually create a system backup file.

**Automatically create a system backup file**

After you enable the automatic backup feature, the system automatically creates a system backup file based on the specified time. In the **Backup List** section, click **Automatic Backup Configuration**. In the **Automatic**
**Backup Configuration** panel, turn on the switch, specify the backup cycle, number of
system backup files to be retained, and backup start time, and then click **Confirm**.

**Note**

We recommend that you set the backup start time to a point in time during off-peak hours to minimize the impact on your workloads. In the **Backup List** section, you can manage system backup files. Click **Download** to download a system backup file to your computer. Click **Restore** to restore the system based on the configuration data in a system backup file. Select a system backup file and click **Delete** to delete the system backup file.

**Restore the system based on the configuration data in a**

**system backup file**

In the **Upload and Restore System Configuration** section, click **Upload** and select a system backup file. After the system backup file is uploaded, click **Restore** to restore the system based on the configuration data in the system backup file.

##### Configure log backup files

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Data Management**.
4. On the **Log Backup** tab, click **Create**.
5. In the **Create Backup Log** panel, specify the backup time period, description, and log
type, and click **Confirm**.

**Download a log backup file**

On the **Log Backup** tab, find the log backup file that you want to manage and click
**Download** in the **Actions** column to download the log backup file to your computer.

**Delete a log backup file**

On the **Log Backup** tab, select the log backup file that you want to manage and click **Delete** to delete the selected file.

##### Restored updated data

You can use a configuration backup file of V3.8222.x or earlier to restore data. After the restoration, the backup data overwrites the current system data.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Data Management**.
4. On the **Data Upgrade and Restore** tab, upload a configuration backup file.
5. After the file is uploaded, click **Restore**.

#### Configure monitoring and alerting

##### View resource monitoring

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Monitor or Alert**.
4. On the **Resource Monitoring** tab, view the status of system resources, such as the CPU
utilization, memory usage, network speed, and disk read and write speed.

##### Configure alert settings

When the resource usage exceeds the specified thresholds, the system sends an alert log by internal message, email, or text message, or to a Syslog server.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Monitor or Alert**.
4. On the **Alert Configuration** tab, configure the thresholds and click **Save**.

##### Configure the notification settings

You can configure the notification methods and recipients.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. On the **Notifications** tab, configure the notification methods and recipients.
Configure notification methods Select the Internal Message, Email, or SMS notification method based on your business requirements. Add notification recipients a. Find a message that you want to manage and click **Add** in the Actions column or select a message and click **Batch Add Recipients**. b. In the **Select User** panel, search for users or select users by department, and then click **Confirm**. Remove notification recipients Click the icon next to a recipient to remove the recipient, or perform the following operations to remove multiple recipients at a time: a. Select the messages that you want to manage and click **Batch Remove Recipients**. b. In the **Select User** panel, select the users that you want to manage and click **Confirm** to remove the selected users at a time.

##### Configure notification methods

**Configure email settings**

You can configure an email server.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. In the **Email Configuration** section of the **Notification Configuration** tab, turn on the
switch, configure an email server, and then click **Test**. After the test succeeds, click **Save**.

**Configure text message settings**

You can configure a custom text message gateway or configure Alibaba Cloud Short Message Service (SMS). Custom SMS Gateway: In the **SMS Configuration** section of the **Notification**
**Configuration** tab, select **Custom SMS Gateway** from the Status drop-down list and
configure the parameters. Click **Send Test Information**. After the test succeeds, click
**Save**.
Alibaba Cloud SMS Service: In the **SMS Configuration** section of the **Notification**
**Configuration** tab, select **Alibaba Cloud SMS Service** from the Status drop-down list
and configure the parameters. Click **Send Test Information**. After the test succeeds, click
**Save**.

#### System logs

##### Manage operation logs

You can configure levels, and export and view operation logs.

**Search for an operation log and view the log details**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **Audit > Operation Logs**.
4. On the Operation Logs page, search for an operation log and view the log details by time
range, level, and username.
5. In the **Actions** column, click **Details** to view the log details.

**Configure log levels for operation logs**

1. In the upper-right corner of the operation log list, click **Configure**.
2. In the **Operation Log Configuration**panel, configure log levels and click**Save Changes**.

**Export operations logs**

In the upper-left corner of the operation log list, click **Export Records**.

##### Manage alert logs

You can view, confirm, and export alert logs.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Monitor or Alert**.
4. On the **Alert Logs** tab, view historical alert logs, log confirmation time, and users who
confirm the alert logs. Select the alert log that you want to manage and click **Confirm Alert** to confirm the alert log. If you confirm the alert log, you acknowledge the alert log. Click the icon. In the **Export** dialog box, enter the encryption password of the file to be exported. The encryption password is used to decrypt the exported ZIP package. We recommend you configure an encryption password to ensure the security of the file.

#### Local maintenance

##### Configure settings on the Country or

**Region tab**

**Configure the system time**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Service Management**.
4. In the **System Time** and **Configuration of System Time Synchronization** sections of
the **Country or Region** tab, configure the system time based on your business requirements. To configure the time server, enter the address of the time server and click **Save**. You can configure the address of the time server. The default address is time.windows.com. To manually synchronize the system time, click **Synchronize Server Time** to synchronize the time of the time server, or click **Synchronize Browser Time** to synchronize the time of the current browser. To automatically synchronize the system time, turn on Automatic Synchronization and configure the Synchronization Period parameter. The value can be accurate to minutes. Then, click **Save**. The system automatically synchronizes the time from the configured time server based on the specified period.

**Configure a time zone**

You can change the time zone only in standalone mode. If the time zone is different from the current system time zone, Bastionhost is restarted after the change takes effect. Proceed with caution. In the **Time Zone Configuration** section of the **Country or Region** tab, select a time zone and click **Save**. UTC is short for Coordinated Universal Time (UTC). GMT is short for Greenwich Mean Time (GMT). You can set the Time Zone parameter to GMT+08:00 for China.

##### Configure language-specific UI

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Local Machine Maintenance**.
4. On the **Language-specific UI** tab, configure settings described in the following table.

| Setting | Description |
|---|---|
| System Language | In the System Language section, select a language from the drop-down list and click Save. |

| UI Settings | In the UI Settings section, configure the browser favicon, logon page logo, logon page background, and homepage logo by uploading images as prompted, and then click Save. Click Restore to Default to restore to the default settings. |
|---|---|
| Website Filing Number Setting | In the Website Filing Number Setting section, configure the ICP Filing Number, ICP Link Address, Net Security Filing Number, and Net Security Link Address parameters based on your business requirements, and then click Save. |
| Watermark Settings | In the Watermark Settings section, turn on File watermark and Status, configure the Transparency parameter based on your business requirements, and then click Save. |

##### Configure announcements

You can configure system announcements. After you customize the content of an announcement, you can push the announcement to the email addresses of users. You can also specify whether to send a pop-up notification after users log on.

**Create an announcement**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Local Machine Maintenance**.
4. On the **Announcement settings** tab, click **Create**. In the Create Announcement panel,
enter the title and content of the announcement, click **Upload Image** to upload images, specify whether to send a notification after the announcement is published and whether to pin the announcement to the top, and then click **Confirm**.

**Manage announcements**

Modify an announcement: Find the announcement that you want to manage and click **Edit** in the **Actions** column. In the Modify Announcement panel, modify the announcement. Pin announcements: Select one or more announcements that you want to manage and click
**Pin** above the announcement list. In the message that appears, click Confirm.
Delete announcements: Select one or more announcements that you want to manage and click **Delete** above the announcement list. In the message that appears, click Confirm.

**View announcements**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Logs**. On the page that appears, click the
**Announcement** tab.
4. Click an announcement name to view the content and images of the announcement.

##### use diagnostics tools

**Connectivitytesttool**

**Connectivity test tool**

You can test the connectivity of a host address.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Local Machine Maintenance**.
4. In the **Test Connectivity** section of the **Diagnostics Tool** tab, set the operation type to
**PING**, enter the host address, and then click **Execute Test**.
The following operation types are supported: PING: checks the network connectivity between the bastion host and the specified host address. Trace Route: detects the routing information of the bastion host and the specified host address. TCP Port Detection: detects the TCP port status of the specified host address. UDP Port Detection: detects the UDP port status of the specified host address.

**TCPDUMP packet capture tool**

You can obtain the communication packets between the bastion host and the specified host.
1. In the **TCPDUMP packet capture** section of the **Diagnostics Tool** tab, enter the host IP
address, port, listening interface, and number of packets, and then click **Start**.

**Note**

If you do not specify a port, all communication packets between the bastion host and the host IP address are obtained. If you specify a port, the communication packets between the bastion host and the host IP address over the specified port are obtained.
2. Click **End** and then click **Download** to download the obtained communication packets to
your on-premises device. You can view the downloaded files by using tools such as network analyzers.

**System diagnostics tool**

You can download system diagnostic logs for technical engineers to troubleshoot issues. In the **System Diagnostics Tool** section of the **Diagnostics Tool** tab, click **Download**
**Diagnostics Logs** to download the system diagnostic logs to your on-premises device. You
can view the logs after decompressing the downloaded files.

##### Perform health checks

You can perform a health check for the system to check items, including the system license, device status, network status, proxy service status, connection service, storage status, and system status. You can also view and export health reports.

**Perform a health check**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Local Machine Maintenance**.
4. Click the **Health check** tab. In the **Health check** section, click **One-click check** to start
the health check. Wait a few minutes and refresh the page to view the health check results.

**Export the health report**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
3. In the left-side navigation pane, choose **System > Local Machine Maintenance**.
4. Click the **Health check** tab. In the **Health check** section, click **Export health report** to
download the health check report to your on-premises computer.

## Use the personal

**workbench**

Before you configure local client tools for protocols, make sure that you download and install Bastionhost Assistant on your computer.

### Homepage

After you log on to Bastionhost, the homepage is displayed. You can handle to-do items, and view the time and source IP address of the last logon, handled items, and unread messages.

**Handle to-do items**

In the **To-do List** section, click the **To Be Handled by Me or Passed** tab to view the tickets that are pending or approved. Click **Details** in the Actions column of a ticket to go to the ticket review page to review the ticket or view the ticket details.

**Read unread messages**

The **Unread Messages** section displays the unread internal messages. Click **Details** to go to the message details page and read the message. Click **Read All** to mark all unread messages as read. Then, the messages are removed from the Unread Messages section. Click **View More** to go to the message details page. The first message is automatically marked as read.

### O&M

#### Configure O&M settings

This topic describes how to configure O&M logon parameters for protocols such as RDP, SSH, Telnet, Rlogin, FTP, SFTP, VNC, X Window System (X11), SQL Server, MySQL, Oracle, Db2, PostgreSQL, KingbaseES, and DM. The O&M logon parameters include the local client tool, session title content, and logon parameters.

**Procedure**

**Important**

Before you configure local client tools for protocols, make sure that Bastionhost Assistant is downloaded and installed on your computer.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **O&M Configuration**.
5. In the **O&M Configuration** panel, select a protocol, configure the parameters, and then
click **Confirm**.

**Important**

If Bastionhost Assistant can identify the path of the local client tool, the configuration is complete. If Bastionhost Assistant cannot identify the path of the local client tool, the
**Bastionhost Assistant Configuration** dialog box appears. For more
information, see Step 6.

| Parameter | Description |
|---|---|
| Resolution | The resolution of the session page of the local client tool when you configure RDP-based O&M. |
| HTML5 Client Resolution | The resolution of the HTML5 session page when you configure RDP-based O&M. Only the default resolution is supported for batch O&M operations. |
| Session Title | The title content and the order in which the content is displayed in an O&M session. If you use FTP or SFTP and the local client tool is eFX, FlashFXP, or Xftp, you cannot change the session title. |
| Connection Mode | If you select this option, you can enable the session management feature. |
| Local Devices and Resources | The local devices and resources that can be used for RDP-based O&M. |
| Local Driver | The drive letters that can be mapped during RDP-based O&M. |
|   | During Browser/Server (B/S) O&M, the local client tool on the computer is called by Bastionhost Assistant to log on to an asset for O&M. You must configure the local client tool on the computer and associate the client tool with a protocol. The following section lists the local client tools supported by different protocols in different operating systems: |

|   | Windows | SSH, Telnet, and Rlogin: Xshell, PuTTY, SecreCRT, and MobaXterm FTP and SFTP: Xftp, WinSCP, FileZilla, FlashFXP, SecureFX, and MobaXterm VNC and X11: RealVNC, TightVNC, and TigerVNC SQL Server: SQL Server Management Studio (SSMS), sqlwb, DBeaver, Navicat Premium, Navicat for SQL Server, and SqlDbx Professional MySQL: MySQL CLI, MySQL Workbench, DbVisualizer, DBeaver, MySQL-Front, Navicat Premium, Navicat for MySQL, HeidiSQL, and SqlDbx Professional Oracle: PL-SQL (PL/SQL), SQL Plus, Toad, DbVisualizer, DBeaver, Navicat Premium, Navicat for Oracle, and SqlDbx Professional Db2: Db2 CMD, QuestCentral, Toad for Db2, DbVisualizer, and DBeaver PostgreSQL: pgAdmin3, psql, DbVisualizer, DBeaver, HeidiSQL, SqlDbx Professional, Navicat Premium, and Navicat for PostgreSQL KingbaseES: KSQL, LSQL, and DbVisualizer DM: DLSQL, LSQL, DbVisualizer, and DM Manager |
|---|---|---|
| Local Client |   |   |
|   | macOS | RDP: Remote Desktop Client SSH, Telnet, and Rlogin: ZOC8 FTP and SFTP: FileZilla VNC and X11: RealVNC SQL Server, MySQL, Oracle, Db2, PostgreSQL, KingbaseES, and DM: DbVisualizer |

|   | Linux | RDP: Remminaand xfreerdp SSH, Telnet, and Rlogin: PuTTY FTP and SFTP: FileZilla VNC and X11: TightVNC and Remmina SQL Server: DBeaver MySQL: DbVisualizer, MySQL Workbench, MySQL CLI, and DBeaver Oracle: DbVisualizer, SQL Plus, and DBeaver Db2: DbVisualizer, CLP Plus, and DBeaver PostgreSQL: DbVisualizer and DBeaver KingbaseES: DbVisualizer DM: DbVisualizer and DM Manager |
|---|---|---|
| Terminal Type | The terminal type that is based on the selected local client tool. Valid values: VT100, Xterm, and Linux. If you set the Local Client parameter to MobaXterm, you cannot configure the terminal type. |   |
| Encoding | The value is fixed as UTF-8. |   |
| Remote Client | The access mode used to connect to an application server during graphical database O&M. Use an HTML5 RDP client for access: If you select this option, you can use only an HTML5 page to access an application server. Use a local RDP client for access: If you select this option, you can use only a local client tool to access an application server. |   |
| Configuration File Path | When you perform O&M operations on an Oracle database, you can configure the absolute path of the tnsnames.ora file, such as G:11.2.0\dbhome 1\NETWORK\ADMIN\tnsnames.ora. _ If the path of the configuration file is not configured, you can use the local client tool to log on to the database. However, the local client tool does not display the information about the database. PL-SQL (PL/SQL) and SQL Plus use the servicename attribute for logon. toad uses the sid attribute for logon. If the path of the configuration file is configured, make sure that the system user of your computer has the permissions to modify the configuration file. The local client tool displays the information about the database. The local client tool determines whether to use the sid or servicename attribute for logon based on the account information that is saved by Bastionhost. |   |

6. Optional. Select the local client tool, click **Browse**, and then select the installation path of
the tool. The path must include the name of the .exe application, such as C:\Users\wsn\Desktop\mysql\mysql\Navicat Premium 15\Navicat Premium 15\navicat.exe. Then, click **OK** to complete the configuration.

#### Perform host O&M

##### Perform B/S O&M

**Prerequisites**

Before you perform Browser/Server (B/S) O&M, the following preparations are complete: Bastionhost Assistant is downloaded and installed on your computer. An O&M tool is downloaded and installed on your computer. The O&M tool is configured in the **Workbench > O&M > O&M Configuration** panel. The host that you want to manage is added and a host account is created for the host on the **Management Console > Asset > Asset Management** page. You are granted permissions on the host account on the **Management Console >**
**Authorize > Authorization Rule** page.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **All Assets** or a group. The information about the hosts in the
group is displayed on the right side of the page. Find the host that you want to manage, move the pointer over the **Access** column, and click the icon. In the dialog box that appears, select a value from the **Account or Service** drop-down list, select **Local O&M** for O&M Method, and then click **Log On**.
5. Bastionhost Assistant is called. Click **Open usmsso** to open and log on to the configured
O&M tool to start O&M.
6. **Optional**. If you select Set as Default in Step 4, B/S O&M is automatically selected the next
time you select the same value from the Account or Service drop-down list.

##### Perform HTML5-based O&M

**Prerequisites**

Before you perform O&M, the following preparations are complete: The host that you want to manage is added and a host account is created for the host on the **Management Console > Asset > Asset Management** page. You are granted permissions on the host account on the **Management Console >**
**Authorize > Authorization Rule** page.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **All Assets** or a group. The information about the hosts in the
group is displayed on the right side of the page. Find the host that you want to manage, move the pointer over the **Access** column, and click the icon. In the dialog box that appears, select a value from the **Account or Service** drop-down list, select **HTML5 O&M** for O&M Method, and then click **Log On**.
5. **Optional**. If you select **Set as Default** in Step 4, HTML5-based O&M is automatically
selected the next time you select the same value from the Account or Service drop-down list.

##### Perform C/S O&M

**Prerequisites**

Before you perform Client/Server (C/S) O&M, the following preparations are complete: The Use Command Line through Shell option is deselected in the SSH Logon section on the

**Management Console > Configure > Asset Conﬁguration > O&M Conﬁguration**

tab. If the Use Command Line through Shell option is selected, authorized assets are not displayed on the SSH logon page. The host that you want to manage is added and a host account is created for the host on the **Management Console > Asset > Asset Management** page. You are granted permissions on the host account on the **Management Console >**
**Authorize > Authorization Rule** page.

**Procedure**

In this topic, Xshell is used as an example.
1. Start Xshell. Click the New icon on the File menu. In the Properties of New Session dialog
box, click Connection in the left-side navigation pane and enter the IP address of Bastionhost and an SSH port number in the General section.

**Note**

The default SSH port is 20022. To view the port number, choose **Management**
**Console** > **System > Service Management > Port Configuration**.
2. In the left-side navigation pane, choose Connection > Authentication and configure the
related parameters. i. If you select the Password authentication method, enter the username and password of Bastionhost. ii. If you select the Public Key authentication method, configure the public key of your SSH key pair on Bastionhost and select the private key.
3. Click **Connect**. After Bastionhost is connected, authorized assets are displayed.
4. Press the upward or downward arrow key to select the host for which you want to perform
O&M operations, and press the Enter key to access the required host for O&M.

#### Perform database O&M

You can use a database account on which you have permissions to log on to the database to perform O&M. Only Browser/Server (B/S) O&M is supported.

**Prerequisites**

Before you perform B/S O&M, the following preparations are complete: Bastionhost Assistant is downloaded and installed on your computer. An O&M tool is downloaded and installed on your computer. The O&M tool is configured in the **Workbench > O&M > O&M Configuration** panel. A database account is created for the database that you want to manage on the
**Management Console > Asset > Asset Management** page.
You are granted permissions on the database account on the **Management Console >**
**Authorize > Authorization Rule** page.
Your account is associated with the database and database account on the **Management**
**Console > Policy > Access Control** page.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **All Assets** or a group. The information about the hosts in the
group is displayed on the right side of the page.
5. Find the database that you want to manage, move the pointer over the **Access** column,
and click the icon. In the dialog box that appears, select a value from the **Account or**
**Service** drop-down list, select **Do Not Use** for **Remote Client**, select **Local O&M** for O&M
Method, and then click **Log On**.
6. Bastionhost Assistant is called. Click **Open usmsso** to open and log on to the configured
O&M tool to start O&M.

#### Perform remote client O&M

If the client tools or protocols, such as HTTPS, are not supported by Bastionhost, you can use an application server to perform remote client O&M and audit. Remote client O&M supports Browser/Server (B/S) O&M and HTML5-based O&M.

##### Perform B/S O&M

**Prerequisites**

Before you perform Browser/Server (B/S) O&M, the following preparations are complete: Bastionhost Assistant is downloaded and installed on your computer. An O&M tool is downloaded and installed on your computer. A remote client tool is created, the application server and remote client tool are valid, and an application account is added on the **Management Console > Asset > Asset**
**Management** page.
You are granted permissions on the host account, database account, or application account on the **Management Console > Authorize > Authorization Rule** page. Your account is associated with the host account, database account, or application account on the **Management Console > Policy > Access Control** page.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **All Assets** or a group. The information about the hosts in the
group is displayed on the right side of the page.
5. Find the object that you want to manage, move the pointer over the **Access** column, and
then click the icon. In the dialog box that appears, select a value from the **Account or**
**Service** drop-down list, select the remote client tool for **Remote Client**, and then select
Local O&M for O&M Method. Then, click **Log On**.
6. Bastionhost Assistant is called. Click **Open usmsso** to open RemoteApp to start O&M.

##### Perform HTML5-based O&M

**Prerequisites**

Before you perform HTML5-based O&M, the following preparations are complete: An O&M tool is installed on an application server. A remote client tool is created, the application server and remote client tool are valid, and an application account is added on the **Management Console > Asset > Asset**
**Management** page.
You are granted permissions on the host account, database account, or application account on the **Management Console > Authorize > Authorization Rule** page. Your account is associated with the host account, database account, or application account on the **Management Console > Policy > Access Control** page.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **All Assets** or a group. The information about the hosts in the
group is displayed on the right side of the page.
5. Find the object that you want to manage, move the pointer over the **Access** column, and
then click the icon. In the dialog box that appears, select a value from the **Account or**
**Service** drop-down list, select the remote client tool for **Remote Client**, and then select
**HTML5 O&M** for O&M Method. Then, click **Log On** to open an HTML5 page and call the
remote client tool, such as the configured Google Chrome browser, of the application server to start O&M.

#### Perform ticket O&M

If you do not have the permissions on the asset on which you want to perform O&M operations and the unauthorized logon O&M feature is disabled, you can submit a ticket to obtain the O&M permissions on the asset. If the asset type is a host account, you can use the account to perform Browser/Server (B/S) O&M and HTML5-based O&M. If the asset type is a database account, you can use the account to perform only B/S O&M.

##### Perform B/S O&M

**Prerequisites**

Before you perform Browser/Server (B/S) O&M, the following preparations are complete: You are granted the permissions on the asset on which you want to perform O&M operations on the **O&M** page of the workbench. Bastionhost Assistant is downloaded and installed on your computer. If the asset type is a host account or a database account, the following requirements are met: An O&M tool is downloaded and installed on your computer. The O&M tool is configured in the **O&M > O&M Configuration** panel of the workbench. If the asset type is an application account, the following requirements are met: An O&M tool is downloaded and installed on the application server. The O&M tool and the application server that is associated with the application are valid on the **Asset > Remote Client** tab.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click the **Ticket** directory and select an approved ticket. The
information about the asset is displayed on the right side of the page.
5. Move the pointer over the **Access** column and click the
icon. In the dialog box that appears, select a value from the **Account or Service** dropdown list, select **Local O&M** for O&M Method, and then click **Log On**. Bastionhost Assistant is called.
6. Click **Open usmsso** to open and log on to the configured O&M tool to start O&M.

##### Perform HTML5-based O&M

**Prerequisites**

Before you perform O&M, the following preparations are complete: You are granted the permissions on the asset on which you want to perform O&M operations on the **O&M** page of the personal workbench.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click the **Ticket** directory and select an approved ticket. The
information about the asset is displayed on the right side of the page.
5. Move the pointer over the **Access** column and click the show more icon. In the dialog box
that appears, select a value from the **Account or Service** drop-down list and select
**HTML5 O&M** for O&M Method. Then, click **Log On** to open an HTML5 page and log on to
the host to start O&M.

#### Manage the favorite list

After you add an asset to the favorite list, you can log on to the asset to perform O&M in an efficient manner.

##### Add an asset to the favorite list

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click the **All Assets** directory. The asset information is displayed on the
right side of the page.
5. Click the
icon to add an asset to the favorite list.

##### Manage the favorite list

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click the **Favorites** directory. The assets that are added to the favorite
list are displayed on the right side of the page.
5. Find the asset that you want to manage, move the pointer over the **Access** column, and
then click the icon. In the dialog box that appears, select a value from the **Account or**
**Service** drop-down list, select **HTML5 O&M** for O&M Method, and then click **Log On**.

#### Log on to multiple assets and perform

**O&M at a time**

You can log on to multiple assets and perform O&M at a time.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click the **Favorites, Ticket, or All Assets** directory. The asset
information is displayed on the right side of the page.
5. Find the asset that you want to manage, move the pointer over the **Access** column, and
then click the icon. In the dialog box that appears, select a value from the Account or Service drop-down list, configure the O&M Method parameter, and then click **Set as**

**Default**

6. Select multiple assets and click **Batch Logon** to log on to the selected assets and perform
O&M at a time.

**Note**

If you click Batch Logon in the **All Assets** directory and the selected assets that use the same protocol have the same accounts, the **Batch Logon** dialog box appears. You must configure the O&M method, logon protocol, and logon name. Then, you can click **Log On** to start O&M. Default Method: Use the default O&M method of each asset. Custom: Select the same logon protocol, logon name, and O&M method for the selected assets.

#### Perform HTML5-based collaborative

**O&M**

Multiple Bastionhost users can perform HTML5-based collaborative O&M.

**Procedure**

1. Go to the O&M page. For more information, see Perform host O&M, Perform database O&M,
or Perform remote client O&M.
2. Click the arrow on the right side of the page to expand the operation section.
3. On the **Collaborative Operation and Management** tab, click **Start Sharing**.
4. Click **Invite**. A dialog box appears.
5. After you specify the reason for the invitation, click **Click to generate invitation link** to
generate a link.
6. Copy the link and send the link to a Bastionhost user.
7. After the Bastionhost user receives the link, the user can paste the link in the browser and
log on to Bastionhost. In the dialog box that appears, click **Join Collaboration** to open the HTML5-based O&M page.
8. The user joins the HTML5-based collaborative O&M.
9. The user is displayed on the collaborative O&M tab.

#### Perform unauthorized logon O&M

If you do not have the permissions on the asset on which you want to perform O&M, you can perform unauthorized logon O&M to access the asset.

**Note**

By default, the unauthorized logon feature is disabled. To use this feature, you must select **Allow Unauthorized Logons from Web** on the **ConfigureAsset**
**ConfigurationO&M Configuration** tab. For more information, see Configure O&M
settings.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. On the **O&M** page, click **Unauthorized Logon**. The **Unauthorized Logon** dialog box
appears.
5. The following table describes the parameters that you can configure to log on to an asset.
After the configuration is complete, click **OK**.

| Parameter | Description |
|---|---|
| Project | The project to which the asset belongs. |
| Service | The protocol that is used to log on to the asset. Valid values: RDP, SSH, TELNET, VNC, X11, SFTP, FTP, SQL Server, MySQL, ORACLE, DB2, PostgreSQL, KINGBASE, DM, and RLOGIN. |
| IP | The IP address of the asset. |
| Port | The port of the asset. We recommend that you use the default port. |
| Account | The account of the asset. |
| Password | The password of the asset account. |
| O&M Method | The O&M method. Valid values: Local O&M and HTML5 O&M. |

#### Manage assets by group

You can create three-level groups in the **All Assets** directory to manage all assets by group.

**Create a group**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the middle navigation pane, click **O&M**.
4. In the right-side navigation pane of the **O&M** page, move the pointer over the **All Assets**
directory or a group. The icon appears on the right side of the pane.
5. Move the pointer over the
icon and click **Create Group**. A field is displayed.
6. Enter a group name in the field and click the
icon next to the field to create a group.

**Edit a group**

1. In the right-side navigation pane of the **O&M** page, move the pointer over the **All Assets**
directory or a group. The icon appears on the right side of the pane.
2. Move the pointer over the
icon and click **Modify Group**. A field is displayed.

**Delete a group**

1. In the right-side navigation pane of the **O&M** page, move the pointer over the **All Assets**
directory or a group. The icon appears on the right side of the pane.
2. Move the pointer over the
icon and click **Delete Group**. A message is displayed. Click Confirm to delete the group and its sub groups.

**Add an asset to a group**

1. On the **O&M** page, click **Ungrouped** in the **All Assets** directory. The information about the
assets that are not added to groups is displayed on the right side of the page.
2. Select the asset that you want to add to a group, click **Join Group**, select the group to
which you want to add the asset, and then click **Confirm**.

**Remove an asset from a group**

1. On the **O&M** page, click a group in the **All Assets** directory. The information about the
assets that are added to the group is displayed on the right side of the page.
2. Select the asset that you want to remove from the group, click **Remove from Group**,
select the group to which you want to add the removed asset, and then click **Confirm**. The asset is added to the new group.

### Tickets

#### Create a ticket

**Note**

If a ticket applicant and the ticket reviewer want to be notified by email, make sure that an email server is configured and email addresses are configured for the ticket applicant and ticket reviewer.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. Click **Create Ticket**. In the panel that appears, configure the parameters and click
**Confirm**. The following table describes the parameters.

| Parameter | Description |
|---|---|
| Project | The project to which the ticket belongs. |
| Ticket Name | The name of the ticket. The name can be up to 30 characters in length. If you do not specify this parameter, the system uses the ticket number as the ticket name. |
| Validity Period | Start date: the start time of the validity period of the ticket. The start time of the validity period cannot be earlier than the current time. End date: the end time of the validity period of the ticket. |
| Application Reason | The reason for the ticket application. The reason can be up to 120 characters in length. |
| Asset Account | The account to which the ticket is bound. After the ticket is approved, the ticket applicant can perform O&M operations by using the account. |
| Operation Permissions | Automatic Matching: The ticket is submitted to apply for the permissions specified in policies. Apply: The ticket is submitted to apply for file transfer and command permissions. The file transfer and command permissions have a higher priority than the permissions specified in policies. |

#### Cancel a ticket

The ticket applicant can cancel the ticket that is in the pending state to stop the application.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. On the **Ticket** page, find the ticket that you want to manage and click **Cancel Application**
in the **Actions** column.

#### View the details of a ticket

**Note**

Users who have different permissions can view different types of tickets. Users who have the ticket review permissions can view the status, review process, and details of pending and handled tickets. Users who have the permissions to submit tickets can view the status, review process, and details of submitted tickets.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. On the **Ticket** page, click the **Submitted, Pending**, or **Processed** card to view the review
status, applicant, and summary of the tickets.
5. **Optional**. Click the
icon to view the review process and information about a ticket.
6. **Optional**. Click **Details** to view the details of a ticket.

#### Search for a ticket

You can search for a ticket by review status, applicant, application reason, or ticket number.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. On the **Ticket** page, click the **Submitted, Pending**, or **Processed** card to go to the
required ticket list.
5. Enter a search condition and click **Search** to search for a ticket.

#### Review a ticket

##### Review a ticket

After you create a ticket, the system automatically triggers the review process. After the ticket is approved by a security administrator, the applicant can perform O&M operations on the required asset.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. On the **Ticket** page, find the ticket that you want to manage and click **Approve** or **Reject**
in the **Actions** column. You can also click **Details**. In the Ticket Details panel, click **Approve** or **Reject**.

##### Review a ticket by using a review code

The system sends a review code to the selected reviewer by email. The ticket applicant can request the review code from the reviewer. Then, the applicant can use the review code to complete the ticket review process.

**Procedure**

1. After the ticket review process is triggered, click **Ticket** of the **workbench** to go to the
ticket application page.
2. Click the
icon in the ticket list. In the **Approval Process** dialog box, select a reviewer and click **Send Approval Code**. The review code is sent to the email address of the reviewer.
3. Request the review code from the reviewer, enter the code in the Approval Process dialog
box, and click **OK**. After the system verifies the review code, the ticket is approved by the reviewer.

#### Revoke a ticket

As an approver, you can revoke approved O&M tickets, pre-authorization tickets, and emergency O&M tickets to cancel asset authorization.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tickets**.
4. On the **Ticket** page, find the ticket that you want to manage and click **Revoke** in the
**Actions** column.

### Cloud drives

You can view, upload, and download files on the Netdisk page.

**View cloud drives within your account**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Netdisk**.
4. In the **User Network Disk** section, view the cloud drives that you are authorized to use.

**Upload files to a cloud drive**

You can upload a file directory or files to a cloud drive.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Netdisk**.
4. In the User Network Disk section, click the cloud drive that you want to manage. Choose
**Upload** > **Select Directory**. Then, select a file directory to upload it to the cloud drive.
5. Choose **Upload** > **Select File**. Then, select a file to upload it to the cloud drive.

**Download files from a cloud drive**

You can download files from a cloud drive to your computer.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Netdisk**.
4. Select the file directories and files that you want to download and click **Download** to
download them to your computer.

**Manage files in transfer**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Netdisk**. In the Transfer List section, click
**Transferring**. Then, you can view files in transfer within your account.
4. To pause the transfer of a file, select the file and click **Pause**.
5. To resume the transfer of a file, select the file and click **Restore**.
6. To retransfer a file, select the file and click **Retry**.
7. To cancel the transfer of a file, select the file and click **Cancel**.

**View file transfer records**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Netdisk**. In the Transfer List section, click **Transfer**
**Records**. Then, you can view file transfer records within your account.
4. To delete a file transfer record, select the file transfer record and click **Delete Record**.

### Tasks

You can implement flexible orchestration and automatic execution for multiple O&M tasks such as command operations and file operations.

#### Manage a task set

**Create a task set**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Task**.
4. In the **Task Set** section, click the
icon to create a task set.
5. In the New Task Set dialog box, enter a task name and click **Confirm**.
6. Move the mouse over the created task set. The icon
is displayed on the right.
7. Click the
icon, select **Create Child Task Set**, enter a task name, and then click the icon.

**Modify a task set**

1. In the **Task Set** section, move the pointer over the task set that you want to manage. The
icon is displayed on the right.
2. Click the
icon and select **Rename**.
3. Enter a new name and click the
icon.

**Delete a task set**

1. In the **Task Set** section, move the pointer over the task set that you want to delete. The
icon is displayed on the right.
2. Click the
icon and select **Delete**. In the message that appears, click **Confirm**.

#### Task orchestration

**Create an orchestrated task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Task**.
4. In the Task Set section, click a task set or child task set. Then, click **Create**. In the Basic
Information section, enter a task name and select the task set or child task set to which the task belongs. You can set the Push Method parameter to Do Not Send, Email, or File Server. You can set the Execution Method parameter to Manual or Period.
5. In the Destination Asset section, click **Add**. In the Select Asset panel, select the SSH- or
Telnet-based authorized account that you want to add, and click **Confirm**.
6. In the Action Flow section, click **Add Node** and select an action type for the action node to
be added. The following types of actions are supported: Execute Command, Download File, and Upload File. If you select **Execute Command**, enter a node name and the commands to be run. Set the **Destination Asset** parameter to Same Target Assets as Task or Custom, and specify whether manual confirmation is required after node execution. If you select **Upload File**, enter a node name and specify the files to be uploaded and the destination path. Set the **Destination Asset** parameter to Same Target Assets as Task or Custom, and specify whether manual confirmation is required after node execution. If you select **Download File**, enter a node name and configure the **Source Asset**, Source File Path, and Download to parameters. Specify whether manual confirmation is required after node execution.
7. Add more action nodes to the task by referring to the preceding steps. Then, click **Save**
**Task**.

**Modify the information about an orchestrated task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Task**.
4. In the task list, find the task that you want to manage and click **Edit** in the Actions column.
Modify the basic information, destination assets, and action nodes of the task, and then click **Save Task**.

**Delete an orchestrated task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Task**.
4. In the task list, find the task that you want to delete and click **Delete** in the Actions column.
In the message that appears, click Confirm. You can also select multiple tasks and click
**Delete** above the list to delete them at a time.

**Immediately run an orchestrated task**

1. In the task list, find the task that you want to run and click **Immediately Execute** in the
Actions column. In the message that appears, click Confirm.
2. You can also select multiple tasks and click **Immediately Execute** above the list to
immediately run them at a time.

**Stop an orchestrated task**

1. In the task list, select the task that you want to stop and click **Stop Execution** above the
list. In the message that appears, click Confirm.

**View the execution results of an orchestrated task**

1. In the task list, find the task that you want to view and click **Historical Execution**
**Records** in the Execution Records column.
2. Find the execution record that you want to view and click **Details** in the Actions column to
view the execution details. To download the execution results to your computer, click
**Download** in the Actions column.

**Search for an orchestrated task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Task**.
4. Specify the search conditions and click **Search** to search for a task. To reset the search
conditions, click **Reset**.

### Logs

You can view operation logs and internal messages.

**View operation logs**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Logs**.
4. On the **Operation Logs** tab, view all system operation logs.
Find the log that you want to manage and click **Details**. In the **Log Details** panel, view the log details.

**View internal messages**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Logs**.
4. On the **Internal Messages** tab, view the internal messages.
Click a message to view the details of the message in the right side of the page. A green dot indicates that the message is unread. After you click the message or click All Read, the green dot is no longer displayed. Click the drop-down arrow in the upper-left corner to display read or unread messages. To search for a message, enter the message content or title keyword in the search box in the upper-right corner and press the Enter key.

### Personal information

#### View the basic information

You can view the basic information about the logon user, such as the name, mobile phone number, and email address.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Basic Information** section, view the user role, modify the basic information about
the user, such as the name, mobile phone number, or email address, and then click **Save**.

#### Configure the logon settings

##### Configure an OTP device

If you enable two-factor authentication, you must obtain the verification code from the bound one-time password (OTP) device for secondary authentication before you can log on to Bastionhost.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Logon Configuration** section, click **Bind** in the **Mobile Phone OTP** section. The
**Bind OTP to Mobile Phone** panel appears.
5. Open the OTP device on your mobile phone and scan the quick response (QR) code or enter
the key to bind the OTP device. Then, obtain the verification code from the OTP device, enter the verification code, and then click **Confirm**.

##### Configure a C/S logon password

When you perform Client/Server (C/S) O&M on an FTP server, Oracle client, or RDP gateway, you must use C/S logon passwords to complete logons.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Logon Configuration** section, click **Set** in the **CS Logon Password** section. The
**Configure CS Logon Password** panel appears.
5. Enter a C/S logon password and click **Confirm**.

##### Configure SSH public keys

You can use an SSH public key to log on to Bastionhost over SSH. Only OpenSSH public keys are supported.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Logon Configuration** section, click **Set** in the **SSH Public Key** section. The
**Configure SSH Public Key** panel appears.
5. Enter the content of the SSH public key and click **Confirm**.

##### Configure an SSH private key

You can use an SSH private key to log on to an asset over SSH to perform O&M operations. Only RSA, DSA, ECDSA, and ED25519 private keys generated by ssh-keygen are supported.

**Note**

Make sure that the **Allow Logon to Host Using User SSH Private Key** option is selected in the SSH Logon section. To go to the SSH logon section, choose **Configure >**
**Asset Configuration > O&M Configuration**. For more information, see Configure O&M
settings.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Logon Configuration** section, click **Set** in the **SSH Private Key** section. The
**Configure SSH Private Key** panel appears.
5. Enter the content of an SSH private key and an encryption password, and click **Confirm**.

#### Configure security settings

**Configure a PGP public key**

After you configure a Pretty Good Privacy (PGP) public key, the public key is used to encrypt files when you export assets or download historical passwords. This helps ensure data security.

**Important**

If PGP is not installed, click the link that is displayed in the PGP Public Key section to download and install PGP.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Personal Information**.
4. In the **Security Configuration** section, click **Upload** in the **PGP Public Key** section. In
the dialog box that appears, select a PGP public key file.

### Download tools

Bastionhost provides download links for O&M, audit, and other tools or plug-ins to help you quickly obtain related tools.

**Procedure**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the console switch section, click the
icon and click **Workbench**.
3. In the left-side navigation pane, click **Tool Download**.
4. Download tools such as O&M tools, audit tools, or plug-ins based on your business
requirements. For information about the usage of each tool, see the following table.

| Tool name | Description |
|---|---|
| Bastionhost Assistant | Bastionhost Assistant is used to log on to an O&M client tool from a browser. |
| Google Chrome plug-in of auto-fill scripts for web applications | A script recording plug-in for web applications. |
| Chrome | The Google Chrome browser. |

| FileZilla | A tool that is used to connect to an SFTP or FTP server. |
|---|---|
| WinSCP | A tool that is used to connect to an SFTP or FTP server. |
| PuTTY | A tool that is used to connect to an SSH, Telnet, or rlogin server. |
| Mstsc | A tool that is used to connect to an RDP server. |
| RealVNC | A tool that is used to connect to a VNC server. |
| SecureFX | A tool that is used to connect to an SFTP or FTP server. |
| SecureCRT | A tool that is used to connect to an SSH, Telnet, or rlogin server. |
| Xshell | A tool that is used to connect to an SSH, Telnet, or rlogin server. |
| Flash Player 12 | A Flash player, which is a plug-in for upload and download buttons, and audit session playback. |

## Best practices

### Configure a DNAT entry to

**access a bastion host over the**

**Internet**

**Background information**

In view of system security, public endpoints are disabled for tenant-side bastion hosts. You can configure DNAT entries to access bastion hosts over the Internet in a secure manner.

**Step 1: Obtain the vpc_vip value of a bastion host**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost.
2. In the bastion host list, obtain a private endpoint of the bastion host that you want to
manage and run the `ping` command to obtain the corresponding IP address. The private endpoint can be accessed only within the virtual private cloud (VPC) of the current user. Record the **vpc_vip** and **user_vpc_id** values obtained by running the `ping` command for later use.

**Step 2: Create an elastic IP address (EIP)**

1. Change the user role to **Organization Administrator**.
2. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.
3. In the left-side navigation pane, click **Elastic IP Addresses**.
4. On the EIP page, click **Create EIP**, configure the parameters as required, and then click
**Submit**.
Set the Organization, Resource Set, and Region parameters to the organization, resource set, and region of the bastion host. Select **BGP** as the line type and **Internet** as the network type.

**Step 3: Create a NAT gateway**

1. Change the user role to **Organization Administrator**.
2. In the top navigation bar, choose **Products > Networking > Virtual Private Cloud**.
3. In the left-side navigation pane, click **NAT Gateways**.
4. On the NAT Gateways page, click **Create NAT Gateway**, configure the parameters as
required, and then click **Submit**. Set the Organization, Resource Set, Region, and VPC parameters to the organization, resource set, region, and VPC of the bastion host.

**Step 4: Associate the NAT gateway with the EIP**

1. In the NAT gateway list, find the NAT gateway that you created in **Step 3**, move the pointer
over the More icon in the Actions column, and then select **Associate EIP**.
2. In the dialog box that appears, select the EIP that you created in **Step 2**.

**Step 5: Configure a DNAT entry**

1. In the NAT gateways list, find the NAT gateway that you created and click **Set DNAT** in the
Actions column.
2. On the **DNAT** tab, click **Create DNAT Entry**.
Configure the parameters as required. Set the Public IP Address parameter to the EIP that you created and associated with the NAT gateway in **Step 2**, set the Private IP Address parameter to the **vpc_vip** value of the bastion host, and then specify Protocol Type based on your business requirements.
3. In the DNAT entry list, obtain the public IP address of the created DNAT entry.

**Step 6: Use a public IP address to access the bastion host**

Access the bastion host by using the public IP address obtained in **Step 5** from a browser.

### Configure data for connecting

**Bastionhost to IDaaS**

This topic describes how to configure data for connecting Bastionhost to Identity as a Service (IDaaS).

**Step 1: Configure data in the IDaaS console**

1. Log in to the IDaaS console and create a SAML 2.0 application. For more information, see
IDaaS User Guide.
2. Click the created application. On the**Sign-In**tab, configure the following parameters.
**ACS URL**: Enter `https://<Bastionhost IP address>/pamapi/auth/v1/saml/acs` .
**SP Entity ID**: Enter a custom unique identifier string. The identifier in Bastionhost is USM
by default and can be modified.
**Advanced Settings > Attribute Statements**: Set **Key** to **username** and set **Value** to
**user.username**.
3. In the**Application Settings**section, obtain**IdP Sign-In URL**and**IdP Entity ID**.

**Step 2: Configure data in the Bastionhost console**

1. Log in to Bastionhost.
2. Go to the**Management Console > Configuration > User Configuration >**
**Authentication Source** tab.
3. Click**Edit** on the **SAML2** card to open the Configuration SAML2 panel.
4. Set**Status**to**Enable**and configure the required parameters based on the description in
the following table.

| Parameter | Description |
|---|---|
| Authentication Source Name | Enter the custom name of the authentication source. |
| Automatically log out of SAML2 server on logout | If you select this option, the IDaaS user logs out of the IDaaS console when the user logs out of the Bastionhost page. |
| IDP Login URL | Enter the IdP Sign-In URL obtained in the IDaaS console. |
| SAML2 Server Certificate | If a certificate is configured on the IDaaS side, upload the certificate here. If no certificate is configured on the IDaaS side, you can leave this parameter empty. |
| IDP Entity ID | Enter the IdP Entity ID obtained in the IDaaS console. |
| SP Entity ID | Enter the SP Entity ID obtained in the IDaaS console. |
| After the authentication is passed, the system automatically creates and binds a local user | If you do not select this option, you must manually create a user on the bastion host and set the authentication source of the user to SAML2. |
| User Attributes in Authentication Source | Enter the username. |

5. Click **Save**.
