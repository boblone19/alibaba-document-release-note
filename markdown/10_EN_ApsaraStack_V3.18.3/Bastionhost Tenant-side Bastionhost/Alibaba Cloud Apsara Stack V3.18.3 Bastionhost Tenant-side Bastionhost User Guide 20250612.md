---
title: "Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost User Guide 20250612"
product_version: "V3.18.3"
doc_version: "20250612"
pdf_pages: 65
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost User Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E5%A0%A1%E5%9E%92%E6%9C%BA/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Bastionhost%20Tenant-side%C2%A0Bastionhost%20User%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Bastionhost Tenant-side Bastionhost User Guide 20250612

## Table of Contents

- 1 Restrictions
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
  - 2.3 Upgrade a bastion host
- 3 User guide
  - 3.1 Overview
  - 3.2 Quick deployment guide
    - 3.2.1 Deploy a bastion host
    - 3.2.2 Log on to Bastionhost from the Apsara Uni-manager Management Console
    - 3.2.3 Log on to a bastion host from a web page
  - 3.3 Dashboards
  - 3.4 Departments
    - 3.4.1 Enable department management
    - 3.4.2 Create a department
    - 3.4.3 Manage departments
  - 3.5 Users
    - 3.5.1 User management
      - 3.5.1.1 Create or import users
      - 3.5.1.2 Export users
      - 3.5.1.3 Manage users
    - 3.5.2 User group management
    - 3.5.3 Dynamic token management
  - 3.6 Assets
    - 3.6.1 Host management
      - 3.6.1.1 Create and import hosts
      - 3.6.1.2 Export host information
      - 3.6.1.3 Create a host account
      - 3.6.1.4 Associate a host with a shared account
      - 3.6.1.5 Manage hosts
    - 3.6.2 Account management
      - 3.6.2.1 Search for a host account
      - 3.6.2.2 Delete host accounts
      - 3.6.2.3 Create shared accounts
      - 3.6.2.4 Associate a shared account with a host
      - 3.6.2.5 Manage shared accounts
    - 3.6.3 Host group management
      - 3.6.3.1 Create a host group
      - 3.6.3.2 Add a host to a host group
      - 3.6.3.3 Manage host groups
    - 3.6.4 Account group management
      - 3.6.4.1 Create an account group
      - 3.6.4.2 Add host accounts to an account group
      - 3.6.4.3 Manage account groups
    - 3.6.5 Application management
      - 3.6.5.1 Create an application center
      - 3.6.5.2 Create application center tools
      - 3.6.5.3 Create or import applications
      - 3.6.5.4 Export applications
    - 3.6.6 Application account group management
      - 3.6.6.1 Create an application account group
      - 3.6.6.2 Add members to an application account group
      - 3.6.6.3 Manage application account groups
  - 3.7 Authorization
    - 3.7.1 O&M rules
      - 3.7.1.1 Create an O&M rule
      - 3.7.1.2 Export O&M rules
      - 3.7.1.3 Manage O&M rules
    - 3.7.2 Review rules
      - 3.7.2.1 Create a review rule
      - 3.7.2.2 Delete a review rule
    - 3.7.3 Review unauthorized logons
      - 3.7.3.1 Perform authorization on review entries
      - 3.7.3.2 Manage review entries
  - 3.8 Policies
    - 3.8.1 Create a host command policy
    - 3.8.2 Associate an O&M rule with a host command policy
    - 3.8.3 Manage policies
  - 3.9 Audit
    - 3.9.1 Session audit
      - 3.9.1.1 Search for audit sessions
      - 3.9.1.2 View all sessions
      - 3.9.1.3 View application sessions
      - 3.9.1.4 View ticket sessions
    - 3.9.2 Event auditing
    - 3.9.3 Audit rules
      - 3.9.3.1 Create an audit rule
      - 3.9.3.2 Manage audit rules
  - 3.10 Tickets
    - 3.11.1 Host O&M
      - 3.11.1.1 Configure Bastionhost Assistant
      - 3.11.1.2 Configure web-based O&M settings
      - 3.11.1.3 Perform O&M operations on hosts
      - 3.11.1.4 Perform O&M operations on applications
      - 3.11.1.5 Perform O&M operations on tickets
      - 3.11.1.6 Perform quick O&M
      - 3.11.1.7 Perform HTML5-based O&M
    - 3.11.2 Perform real-time monitoring
    - 3.11.3 Review commands
    - 3.11.4 Process O&M permission requests
    - 3.11.5 View, export, and configure the setting for automatically sending O&M reports
  - 3.12 Tasks
    - 3.12.1 Password change tasks
    - 3.12.2 Automatic O&M
  - 3.13 System
    - 3.13.1. [DO NOT TRANSLATE]
      - 3.13.1.1 Configure network settings
      - 3.13.1.2 Configure web settings
    - 3.13.2. [DO NOT TRANSLATE]
      - 3.13.2.1 Configure security settings
      - 3.13.2.2 Configure remote authentication
      - 3.13.2.3 Configure two-factor authentication
    - 3.13.3 System settings
      - 3.13.3.1 Configure O&M management settings
      - 3.13.3.2 Configure alert settings
      - 3.13.3.3 Configure the language and user interfaces
      - 3.13.3.4 Configure features
      - 3.13.3.5 Create a password change script
    - 3.13.4 Storage management
      - 3.13.4.1 Archive data
      - 3.13.4.2 Back up logs
    - 3.13.5 View system operation logs
    - 3.13.6 View system reports
    - 3.13.7. [DO NOT TRANSLATE]
      - 3.13.7.1 View the system time
      - 3.13.7.2 Upgrade Bastionhost
      - 3.13.7.3 Back up and restore system settings
      - 3.13.7.4 Push and receive system settings
      - 3.13.7.5 View debugging logs
- 4 Best practices
  - 4.1 Configure a DNAT entry to access a bastion host over the Internet

## 1 Restrictions

Before logging on to Apsara Stack Security Center, make sure that your local PC meets the requirements. Table 1. Configuration requirements

| Item | Requirements |
|---|---|
| Browser | Internet Explorer: 11 or later Google Chrome (recommended): 42.0.0 or later Mozilla Firefox: 30 or later Safari: 9.0.2 or later |
| Operating system | Windows XP, Windows 7, or later Mac |

## 2 Quick start

### 2.1 User roles and permissions

This topic describes the user roles involved in Bastionhost. All roles in Apsara Stack Security Center are provided by default. You cannot create custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see Default roles in Bastionhost. Table 1. Default roles in Bastionhost

| Role name | Description |
|---|---|
| Organization security administrator | Uses SOC to manage the security of hosts, applications, and networks for an organization. This role also manages security products related to Elastic Compute Service (ECS). |
| Global organization security administrator | Uses SOC to conduct security management for Apsara Stack and all tenants, and manages security products related to ECS. |
| Security auditor | Manages security auditing for Apsara Stack. |
| Global organization security auditor | Uses SOC to check the security conditions of all organizations. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel before you log on to the Apsara Uni-manager Management Console. We recommend that you use the Google Chrome browser.
1. In the address bar, enter the URL of the Apsara Uni-manager Management Console. Press
the Enter key.
2. Enter your username and password.
Obtain the username and password that you can use to log on to the console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your username. Your password must meet complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: It is the first time that you log on to the console after MFA is forcibly enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the account and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA authentication code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable** **MFA** topic in **Apsara Uni-manager Operations Console User Guide** .

### 2.3 Upgrade a bastion host

If the current bastion host cannot meet your business requirements, you can upgrade your bastion host on the Bastionhost page. This topic describes how to upgrade a bastion host.
1. Log on to the Apsara Uni-manager Management Console. For more information, see Log on
to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **O&M Audit > Tenant-side Bastionhost**. On the **Tenant-side Bastionhost**
page, select a region from the **Region** drop-down list and click **Access with Authorized**
**Role**.
3. On the **Bastionhost** page, find the bastion host that you want to manage and click
**Settings** in the **Actions** column.
4. In the **Configure Instance** panel, configure the following parameters and click **OK**.

**Note**

After a bastion host is created, make sure that all security groups in the virtual private cloud (VPC) allow access from the bastion host. Otherwise, the connection between the bastion host and your Elastic Compute Service (ECS) instance may fail.

| Parameter | Description |
|---|---|

| Instances Name | The name of the bastion host that you want to upgrade. |
|---|---|
| Package specifications | The new specification of the bastion host. Valid values: Basic Edition (Assets: Less Than 200): supports ECS instances with 4 vCPUs, 8 GB of memory, 80 GB of system disk, and 250 GB of data disk. Less than 200 ECS instances can be managed. Standard Edition (Assets: 200 to 600): supports ECS instances with 8 vCPUs, 16 GB of memory, 80 GB of system disk, and 250 GB of data disk. 200 to 600 ECS instances can be managed. Advanced Edition (Assets: 600 to 2,000): supports ECS instances with 8 vCPUs, 32 GB of memory, 80 GB of system disk, and 250 GB of data disk. 600 to 2,000 ECS instances can be managed. Top Edition (Assets More Than 2,000): supports ECS instances with 16 vCPUs, 64 GB of memory, 80 GB of system disk, and 250 GB of data disk. More than 2,000 ECS instances can be managed. Important You can only upgrade your bastion host to a higher specification. You cannot roll back the upgrade. Proceed with caution. The upgrade process involves a downtime during which the bastion host is stopped and upgraded. The bastion host is unavailable during the downtime. |
| Asset Quota | The number of assets that the bastion host can manage. The value of this parameter must be a multiple of 10. Minimum value: 50. |
| Support for High Availability | Specifies whether to enable a single-zone high availability (HA) architecture. |

## 3 User guide

### 3.1 Overview

Bastionhost allows you to play back audit videos and manage permissions on O&M operations on cloud servers. Bastionhost provides a centralized management solution based on account, authentication, authorization, and audit. Bastionhost supports identity management, authorization management, two-factor authentication, real-time session monitoring and disconnection, audit video playback, and query of high-risk commands. This enhances the security of O&M management. Bastionhost can help meet the requirements of various laws, regulations, and policies, including the requirements of classified protection, China Banking and Insurance Regulatory Commission (CBIRC), China Securities Regulatory Commission (CSRC), PCI Security Standards Council (PCI SSC), and internal management of enterprises.

### 3.2 Quick deployment guide

#### 3.2.1 Deploy a bastion host

This topic describes how to deploy a bastion host.

**Prerequisites**

Your account is granted the permissions on the cloud resources of a department. For example, your account has the permissions of the department administrator role.
1. Log on to the Apsara Uni-manager Management Console. For more information, see Log on
to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security > O&M Audit > Tenant-side Bastionhost**.

> **Note:** In multi-level organization mode, all data permissions are managed by using resource sets in organizations. In the top navigation bar of the console, select an organization or a resource set. Then, you can view or manage the assets of the organization or resource set.
> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. On the **Bastion Host** page, click **Create Instance**.
4. In the **Create Instance** panel, configure the following parameters and click **OK**.
After you enable multi-level organization management, you must select an organization and a resource set.

| Parameter | Description |
|---|---|

| VPC ID | Select the virtual private cloud (VPC) to which the bastion host belongs. Important After the bastion host is created, make sure that access rules are configured for all security groups in the VPC to allow access from the bastion host. Otherwise, the bastion host may fail to access the Elastic Compute Service (ECS) instance. |
|---|---|
| Vswitch ID | Select the ID of the vSwitch to which the bastion host belongs. |
| Package specifications | Select the edition of the bastion host. Valid values: Basic Edition (Assets: Less Than 200): ECS instance of basic specifications: 4 vCPUs, 8 GB memory, 80 GB system disk, and 250 GB data disk. Concurrency: The maximum number of character protocol-based connections is 200. The maximum number of graphics protocol- based connections is 40. Standard Edition (Assets: 200 to 600): ECS instance of standard specifications: 8 vCPUs, 16 GB memory, 80 GB system disk, and 250 GB data disk. Concurrency: The maximum number of character protocol-based connections is 500 and the maximum number of graphics protocol- based connections is 100. Advanced Edition (Assets: 600 to 2,000): ECS instance of high specifications: 8 vCPUs, 32 GB memory, 80 GB system disk, and 250 GB data disk. Concurrency: The maximum number of character protocol-based connections is 2,000 and the maximum number of graphics protocol-based connections is 400. Top Edition (Assets: More Than 2,000): ECS instance of top specifications: 16 vCPUs, 64 GB memory, 80 GB system disk, and 250 GB data disk. Concurrency: The maximum number of character protocol-based connections is 3,000 and the maximum number of graphics protocol-based connections is 600. |

| Asset Quota | The asset quota. Note When you create a bastion host, you can specify the maximum number of assets that can be managed by the bastion host. The total number of assets that can be managed by your bastion host depends on the value that you specify for the Asset Quota parameter when you create the bastion host. To increase or decrease the minimum asset quota for bastion hosts, log on to the Apsara Uni-manager Operations Console. In the top navigation bar, choose Product Operation > Security O&M > Cloud Security Operations Center. In the left-side navigation pane, choose Cloud Services > OEM O&M > Permissions. On the page that appears, specify the minimum asset quota. For more information, see the security administrator guide. |
|---|---|

> **Important:** You can no longer configure public endpoints for new bastion hosts. Existing bastion hosts that are configured with public endpoints can still be accessed by using the public endpoints. However, if you disable the public endpoint of a bastion host, you cannot enable the public endpoint for the bastion host again.

#### 3.2.2 Log on to Bastionhost from the Apsara Uni-manager Management Console

**Uni-manager Management Console**

This topic describes how to log on to Bastionhost from the Apsara Uni-manager Management Console as the super administrator.

**Background information**

Make sure that your account has the permissions on the cloud resources of a department. For example, you have the permissions of the administrator role in a department. The first time you log on to Bastionhost, you must change the default password of the super administrator. You can obtain the default password from the technical support engineers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **O&M Audit** > **Tenant-side Bastionhost**.
3. On the **Tenant-side Bastionhost** page**,** select a region from the **Region** drop-down list
**and** click **Access with Authorized Role.**
4. On the **Bastion Host** page, find the desired bastion host and click **Details** in the **Actions**
column.

#### 3.2.3 Log on to a bastion host from a web page

**page**

This topic describes how to log on to a bastion host.

**Prerequisites**

The client that you use can access the bastion host. The access address of the bastion host is obtained from the system deployment personnel. The username and password of the bastion host are obtained from the system deployment personnel. The following table describes the basic roles in Bastionhost.

| User | Description |
|---|---|
| Super administrator | Super administrator: admin. Note If you use the admin user, you must log on to a bastion host from the Apsara Uni-manager Management Console. For more information, see Log on to a bastion host from the Apsara Uni-manager Management Console. |
| Audit administrator | An auditor can use this account to audit O&M operations. This account is created by the super administrator on the User Management page. |
| System administrator | A system administrator can use this account to manage bastion hosts. This account is created by the super administrator on the User Management page. |
| O&M engineer | An O&M engineer can use this account to manage hosts. This account is created by the super administrator on the User Management page. |

1. Open your Google Chrome browser.
2. In the address bar, enter the access address of the bastion host in the https://
`The IP address of Bastionhost` format and press Enter.
3. Enter the username, password, and verification code.
A user is created by the super administrator on the **User Management** page.
4. Click **Log On** to log on to the bastion host.

> **Note:** The first time a user logs on to a bastion host, the super administrator must change the password of the user.

### 3.3 Dashboards

The Dashboards module displays the common features, system status, recent O&M sessions, and system license.
1. Log on to the Apsara Uni-manager Management Console.
2. In the left-side navigation pane, click **My Templates**.
3. On the Dashboards page, view the overall system information.

| Section | Description |
|---|---|
| Users, Host, Application, and O&M Rules | Displays the numbers of users, hosts, applications, and O&M rules that you can manage. Click each section to go to the specific management page. |
| Weekly O&M Operations | Displays the number of O&M operations per day in a week based on session type. |
| Top 5 Users for O&M in One Week | Displays the top five users who perform the largest number of O&M operations. |
| Top 5 Hosts for O&M in One Week | Displays the top five hosts on which the largest number of O&M operations are performed. |
| Real-time Monitoring | Displays the numbers of active sessions, active users, and active hosts. |
| New Sessions Today | Displays the number of O&M sessions on the current day and the size of the sessions. |
| Recent O&M Records | Displays the five latest O&M records. |
| System Running Status | Displays the system name and the duration for which the system runs. |
| License Information | Displays the maximum number of active connections and the maximum number of hosts that are supported by the system. |

### 3.4 Departments

#### 3.4.1 Enable department management

This topic describes how to enable the department management feature.

> **Background information**
> The department management feature is used in scenarios where system objects need to be separately managed. System objects include users, assets, authorization data, and audit data.
> After department management is enabled, the administrator role can manage only the system objects of the current department and lower-level departments, but cannot manage the system objects of upper-level or same-level departments.
> After department management is enabled, you must specify a department for each system object that you add.

> **Note:** If you specify too many levels of departments, it may cause difficulties in managing system objects and confusion of permissions. We recommend that you reasonably specify the levels of departments.
> **Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **System** > **System Configuration**.
4. On the **Feature Settings** tab of the **System Settings** page, set Status to Enable in the
Department Management section and click **Save**.

#### 3.4.2 Create a department

**Prerequisites**

The department management feature is enabled. For more information, see Enable department management.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. In the left-side navigation pane, click **Users**.
4. On the **Departments** page, click **Create Department**.
5. In the **Create Department** dialog box, select a parent department, enter a department
name, and then click **Create Department**.

#### 3.4.3 Manage departments

**Prerequisites**

A department is created. For more information, see Create a department.

**Modify the name of a department**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. In the left-side navigation pane, click **Users**.
4. On the **Departments** page, find the department whose name you want to modify and click
its name.
5. In the **Department Information** dialog box, modify the department name and click **Save**.

**Manage security codes of departments**

The security codes of a department are classified into KeyA security codes and KeyB security codes. KeyA and KeyB security codes are used to encrypt files that contain data to be exported from the department.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. In the left-side navigation pane, click **Users**.
4. On the **Departments** page, find the department whose security codes you want to manage
and click **Manage** in the **Security Code** column.
5. On the Security Code page, change the value of KeyA or KeyB and click **Save**.

> **Note:** Length: The security code must be 10 to 64 bits in length.
> Complexity: The security code must contain digits (0 to 9), lowercase letters (a to z), uppercase letters (A to Z), and other special characters.
> Correlation: The security code cannot be the same as the username, the same as the username in reverse order, or the same as the last two passwords that are entered most recently.

**Delete a department**

> **Warning:** If you delete a department, data such as users, user groups, hosts, host groups, account groups, applications, password change tasks, automatic O&M tasks, O&M permissions, and audit rules are also deleted.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. In the left-side navigation pane, click **Users**.
4. On the **Departments** page, find the department that you want to delete and click **Delete**
**Department**.
5. In the message that appears, click **OK**.

### 3.5 Users

#### 3.5.1 User management

##### 3.5.1.1 Create or import users

On the User Management page, you can create, import, and export users. You can also modify user information. This topic describes how to create or import a user.

**Create a user**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Management**.
4. On the **User Management** page, click **Add User**.
5. On the **Add User** page, configure the parameters and click **Create**.

| Parameter | Description |
|---|---|
| Username | Enter a username. |
| Department | Select the department to which the user belongs. For more information, see Create a department. |
| Roles | Select a role. You can click Permissions to view the permissions of each role. |
| Authentication Mode | Select an authentication method for user logon. By default, Local is selected. You can also specify a different value. |
| Password | Set a password for the user. You can enter a password or clickG enerate Password to generate a random password. |
| Confirm Password | Re-enter the password. |
| Name | Enter the name of the user. |
| Email Address | Enter the email address of the user. |
| Mobile Phone Number | Enter the mobile phone number of the user. |
| Description | Enter the description of the user for subsequent operations. |

**Import multiple users at a time**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Management**.
4. On the **User Management** page, click **Import User**.
5. On the **Import User** page, upload a file that is exported from the current system, configure
the **Authentication Mode** parameter, select **Other Options**, and then click **Import User**. You can also click **download a template file**, complete the file in the specified format, and then upload the file to the system.

##### 3.5.1.2 Export users

This topic describes how to export users.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Management**.
4. On the **User Management** page, click **Export User**.
5. In the **Export User** dialog box, click **Export**.
The result file will be compressed into a ZIP file. You can specify whether to encrypt the ZIP file. If you leave the ZIP Password parameter empty, the ZIP file is not encrypted.

##### 3.5.1.3 Manage users

This topic describes how to search for, delete, lock, unlock, and configure users.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Management**.
4. On the **User Management** page, manage users.

| Scenario | Description |
|---|---|
| Search for a user | You can search for a user by username, name, role, authentication mode, and department. |
| Delete a user | i. Select the user that you want to delete and clickD elete. ii. In the Delete User message, click OK. |
| Lock a user | i. Select the user that you want to lock and clickL ock. ii. In the Lock User message, click OK. |

| Unlock a user | i. Select the user that you want to unlock and clickU nlock. ii. In the Unlock User message, click OK. |
|---|---|
| Configure a user | i. Select the user that you want to manage and chooseB atch Edit > User Settings. ii. On the User Information page, configure parameters such as the Status and Authentication Method parameters. Then, click Save. |

#### 3.5.2 User group management

In the user group management module, you can perform operations such as creating, modifying, and deleting user groups, and adding user members to a user group. This topic describes how to create and manage user groups.

**Create a user group**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Group Management**.
4. On the **User Group Management** page, click **Create User Group**.
5. On the **Create User Group** page, select a department, enter a user group name, and then
click **Create User Group**.

**Manage user groups**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **User Group Management**.
4. On the **User Group Management** page, manage user groups.

| Scenario | Description |
|---|---|
| Search for a user group | Search for a user group by name or department. |
| Modify the name of a user group | i. Find the user group whose name you want to modify and click its name. ii. On the Change User Group Name tab, modify the name of the user group and click Save. |

| Add user members to a user group | i. Find the user group to which you want to add user members and click the number of user members. ii. On the User tab, click Add Member. iii. In the Add User dialog box, select the user member that you want to add and click Add. To remove a user member, select the user member that you want to remove and click Disassociate. |
|---|---|
| Delete a user group | i. Select the user group that you want to delete and clickD elete. ii. In the Delete User dialog box, click OK. |

#### 3.5.3 Dynamic token management

Dynamic tokens are used for two-factor authentication. This topic describes how to import and manage token files.

**Import a token file**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **Dynamic Token Management**.
4. On the **Dynamic Token Management** page, click **Import Token File**.

**Bind a token with a user**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **Dynamic Token Management**.
4. On the **Dynamic Token Management** page, find the token that you want to bind with a
user and click **Bind to User** in the **Actions** column.
5. In the **Select User** dialog box, select a user and click **OK**.
After you select a user who needs to use the token for two-factor authentication, you can bind the token with the selected user. When the user logs on to the system, the user can select a dynamic token for authentication.

**Manage dynamic tokens**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **User** > **Dynamic Token Management**.
4. On the **Dynamic Token Management** page, manage dynamic tokens.

| Scenario | Description |
|---|---|

| Unbind a token from a user | Select the token that you want to unbind from the user and click Disassociate to unbind the token from the user. If you unbind the token from the user, the user can no longer use the token for authentication. The token can be rebound to the user. |
|---|---|
| Disable a token | Select the token that you want to disable and clickD isable. A token cannot be used after it is disabled. You must enable it before it can be used. |
| Enable a token | Select the token that you want to enable and clickE nable. |
| Report for loss for a token | Select the token for which you want to report for loss and clickR eport Lost. A token cannot be used after it is reported for loss. |
| Delete a token | Select the token that you want to delete and clickD elete. |
| Change the department to which a token belongs | Select the token whose department you want to change. Move the pointer over Move and select a new department for the token. |

### 3.6 Assets

#### 3.6.1 Host management

##### 3.6.1.1 Create and import hosts

This topic describes how to create and import a host.

**Create a host**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, click **Add Host**.
5. On the **Add Host** page, configure the parameters and click **Create Host**.

**Import multiple hosts at the same time**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, click **Import Host**.
5. On the **Import Host** page, upload the file that is exported from the current system, or click
**download a template file**, fill out the template in the specified format, and then upload
the template to the system. Specify **Other Options** and click **Import Host**.

##### 3.6.1.2 Export host information

This topic describes how to export host information.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, find the host whose information you want to export and
click **Export Host**. The exported information includes the host IP address, hostname, operating system, username and password used to log on to the host, host group, host network, and host code. You can directly import the file that contains the exported host information into Bastionhost. You can export the information about a host by repeating the preceding operations and then modify the information about multiple hosts and host accounts at the same time.

##### 3.6.1.3 Create a host account

A host account can be used to log on to the required host and application for management. This topic describes how to create a host account.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, find the host that you want to manage and click the
number in the Host Accounts column.
5. On the **Host Account** tab of the page that appears, click **Add Host Account**.
6. In the **Create Host Account** dialog box, configure the parameters and click **Create Host**
**Account**.

| Parameter | Description |
|---|---|
| Protocol | Select the protocol of the host account. Hosts on Bastionhost support the following protocols: SYSDEF, SSH, Telnet, FTP, SFTP, RDP, VNC, Rlogin, Oracle, MySQL, DB2, and SQL server. |

| Logon Mode | Select the logon mode. Bastionhost supports the following logon modes: automatic logon, automatic logon (account switch), and manual logon. If you select automatic logon and host the username and password of the host account on a bastion host, you can log on to the host in password-free mode when you perform O&M operations on the host. If you select manual logon, you must enter a valid username and password of the host account before you can perform O&M operations on the host. If you select automatic logon (account switch), you can select only SSH or Telnet to automatically switch the logon account from a standard account to a privileged account. If a switch is configured with the remote account mode and the enable command mode and you want to automatically switch to the enable mode, you must select automatic logon (account switch). |
|---|---|
| Account Type | Select the account type. Bastionhost supports standard accounts and privileged command accounts of switches. |
| Logon Name | Enter the username of the host account and select Privileged Account or Use Privileged Account to Change Password. |
| Password | Enter the password of the host account. |

##### 3.6.1.4 Associate a host with a shared account

This topic describes how to associate a host with a shared account.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, find the host that you want to associate with a shared
account and click the number in the Shared Accounts column.
5. On the **Shared Accounts** tab, click **Associated Shared Account**.
6. In the **Associated Shared Account** dialog box, select a shared account and click **Add**.

##### 3.6.1.5 Manage hosts

This topic describes how to search for, enable, and disable hosts, and modify information about hosts.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Management**.
4. On the **Host Management** page, manage hosts.

| Scenario | Description |
|---|---|
| Search for a host | Fuzzy match and exact match are supported to search for hosts based on conditions such as IP addresses and names of the hosts. Click Advanced Search to search for hosts by O&M start time and end time. |
| Delete a host | Select the host that you want to delete and clickD elete. |
| Disable a host | Select the host that you want to disable and clickD isable. Users cannot access a disabled host. |
| Enable a host | Select the host that you want to enable and clickE nable. |
| Modify host information | Modify the information about a single host: Find the host whose information you want to modify and click its name. On the Basic information tab of the page that appears, modify the information about the host. Modify the information about multiple hosts at the same time: Select the hosts whose information you want to modify, and choose Batch Edit > Host Information to modify the information about the hosts. |
| Configure a protocol port for a host | Configure a protocol port for a single host: Find the host for which you want to configure a protocol port and click its name. On the Basic information tab of the page that appears, configure a protocol port for the host. Configure protocol ports for multiple hosts at the same time: Select the hosts for which you want to configure protocol ports, and choose Batch Edit > Port Settings to configure protocol ports for the hosts. |

#### 3.6.2 Account management

##### 3.6.2.1 Search for a host account

This topic describes how to search for a host account.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Host Account** tab of the **Host Management** page, specify search conditions to
search for a host account. In the host account list, you can search for a host account by host IP address, hostname, username, protocol, department, and logon mode. You can click **Advanced Search** to search for a host account based on the start time and end time of O&M operations.

##### 3.6.2.2 Delete host accounts

This topic describes how to delete a host account.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Host Account** tab of the **Account Management** page, select the host account
that you want to delete and click **Delete**.

##### 3.6.2.3 Create shared accounts

Users who have the permissions on a shared account can use the shared account to log on to multiple hosts that are associated with the shared account, which reduces the workload of creating accounts for hosts. This topic describes how to create a shared account.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Shared Account** tab of the **Account Management** page, click **Create Shared**
**Account**.
5. In the **Create Shared Account** dialog box, configure the parameters and click **Create**
**Shared Account**. The following table describes the parameters.

| Parameter |   | Description |
|---|---|---|
| Department |   | The department to which the shared account belongs. |
| Username |   | The name of the shared account. |
| Protocol |   | The protocol of the shared account. |
| Logon Name |   | The logon name of the shared account. |
| Authen ticatio n Type | Pas swo rd | The password of the shared account. |
|   | Key | SSH supports key-based authentication. Key: Only Rivest-Shamir-Adleman (RSA) private keys that are generated by using the ssh-keygen utility are supported. Encryption Password: Enter an encrypted password. You can leave the parameter empty if you do not have an encrypted password. |

##### 3.6.2.4 Associate a shared account with a host

This topic describes how to associate a shared account with a host.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Shared Account** tab of the **Account Management** page, find the account that
you want to associate with a host and click **Associate Host** in the **Actions** column. You can also click the number in the **Associate Host** column of a shared account.
5. On the **Shared Account Information** page, click **Associate Host**.
6. In the **Associate Host** dialog box, select a host and click **Add**.
To remove an associated host, select the host that you want to remove and click
**Disassociate**.

##### 3.6.2.5 Manage shared accounts

This topic describes how to search for, delete, and modify shared accounts.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Shared Account** tab of the **Account Management** page, search for, delete, or
modify shared accounts.

| Scenario | Description |
|---|---|
| Search for a shared account | In the list of shared accounts, search for the desired account by specifying conditions such as the account name, logon name, protocol, and authentication type. |
| Modify a shared account | In the list of shared accounts, find the shared account that you want to modify and click Modify in the Actions column. |
| Delete a shared account | Select the shared account that you want to delete and clickD elete. |

#### 3.6.3 Host group management

##### 3.6.3.1 Create a host group

Host groups are used to group hosts and facilitate batch authorization for hosts. This topic describes how to create a host group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Group Management**.
4. On the **Host Group Management** page, click **Create Host Group**.
5. In the **Create Host Group** dialog box, select a department, enter a host group name, and
then click **Create Host Group**.

##### 3.6.3.2 Add a host to a host group

This topic describes how to add a host to a host group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Group Management**.
4. On the **Host Group Management** page, find the host group to which you want to add a
host and click **Add Host** in the **Actions** column.
5. On the **Hosts** tab of the **Host Group Information** page, click **Add Host**.
6. In the **Associate Host** dialog box, select a host and click **Add**.
To remove a host, select the host and click **Disassociate**.

##### 3.6.3.3 Manage host groups

This topic describes how to search for, modify, and delete a host group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Server Group Management**.
4. On the **Host Group Management** page, search for, delete, or modify a host group.

| Scenario | Description |
|---|---|
| Search for a host group | In the list of host groups, search for the desired host group by specifying conditions such as the name and department of the host group. |
| Modify the name of a host group | In the list of host groups, find the host group whose name you want to modify and click Modify in the Actions column. |
| Delete a host group | Select the host group that you want to delete and clickD elete. |

#### 3.6.4 Account group management

##### 3.6.4.1 Create an account group

Account groups are used to group host accounts and facilitate batch authorization for accounts. This topic describes how to create an account group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Account Group Management** page, click **Create Account Group**.
5. In the **Create Account Group** dialog box, select a department, enter an account group
name, and then click **Create Account Group**.

##### 3.6.4.2 Add host accounts to an account group

This topic describes how to add host accounts to an account group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Account Group Management** page, find the account group to which you want to
add host accounts and click **Add Host Account** in the **Actions** column.
5. On the **Host Account** tab of the **Account Group Information** page, click **Add Host**
**Account**.
6. In the **Select Host Account** dialog box, select the host account that you want to add and
click **Add**. To remove a host account, select the host account that you want to remove and click
**Disassociate**.

##### 3.6.4.3 Manage account groups

This topic describes how to search for, modify, and delete an account group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Account Management**.
4. On the **Account Group Management** page, search for, delete, or modify an account
group.

| Scenario | Description |
|---|---|
| Search for an account group | In the list of account groups, search for the desired account group by specifying conditions such as the name and department of the account group. |
| Modify the name of an account group | In the list of account groups, find the account group whose name you want to modify and click Modify in the Actions column. |
| Delete an account group | Select the account group that you want to delete and clickD elete. |

#### 3.6.5 Application management

##### 3.6.5.1 Create an application center

This topic describes how to create an application center.

**Background information**

If the application server runs the Windows operating system, you can use a RemoteAPP to publish applications. The Windows operating system does not limit the access permissions of applications. O&M engineers may access the local file directory of the application server by using published applications during application O&M. You can determine whether to use this feature based on your security and risk management requirements. If you want to use the feature, refer to the following security hardening suggestions. Deploy the application server in an independent network and apply strict access control policies. This way, the application server cannot access servers or network devices on which the application server has no permissions. Do not store sensitive information, such as business operation data and personal information, on the application server. Use accounts with limited permissions to publish applications. Separately publish important applications on different application servers to significantly reduce risks. Grant the permissions to publish applications only to required accounts. Do not grant the permissions to unnecessary accounts. Audit all session logs of application publishing by using Bastionhost on a regular basis. Regularly update the application server and perform necessary security hardening on the application server.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Application Management**.
4. On the **Application Center** tab of the **Application Management** page, click **Create**
**Application Center**.
5. In the **Create Application Center** dialog box, configure an application center.
i. In the **Create Application Center** step, select a department, enter an application center name, and then click **Next**. ii. In the **Add Instance** step, configure the parameters and click **Next**.

| Parameter | Description |
|---|---|
| Server Address | The server address of the instance. |
| Port Number | The port number of the server. |
| Administrator Account Username | The username of the administrator account. |
| Password | The password. |
| Operating System Type | The operating system type. |
| Instance Type | The instance type. You cannot configure this parameter if you set Operating System Type to LINUX. |
| Domain | The domain. This parameter is required if you set Operating System Type to WINDOWS. |

iii. In the **Add Tool** step, click **Create Tool**. In the entry that appears, configure the parameters such as the icon and name of the tool and click **Complete**.

> **Important:** Make sure that the information is valid. Otherwise, you cannot start the tool during O&M.

After you create the application center, you can perform the following operations to manage the application center: Search: Search for the application center by operating system. Modify: In the **Actions** column, click **Modify** to modify the application center. Delete: In the **Actions** column, click **Delete** to delete the application center. Calibrate Application Center: Click **Calibrate Application Center** to calibrate data in the application center.

##### 3.6.5.2 Create application center tools

This topic describes how to create an application center tool.

**Prerequisites**

An application center is created. For more information, see Create an application center.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Application Management**.
4. On the **Application Center Tools** tab of the **Application Management** page, click
**Create Application Center Tool**.
5. On the **Create Application Center Tool** page, configure the parameters and click **Create**
**Application Center Tool**.
After you create an application center, you can perform the following operations to manage application center tools: Search: Search for an application center tool by path, name, and application center. Modify: Find the desired application center tool and click **Modify** in the **Actions** column to modify the application center tool. Delete: Select the desired application center tool and click **Delete** to delete the application center tool.

##### 3.6.5.3 Create or import applications

This topic describes how to create or import an application.

**Create an application**

**Prerequisites**

An application center is created. For more information, see Create an application center. An application center tool is created. For more information, see Create application center tools.
1. Log on to Bastionhost from the Apsara Uni-manager Management Console. For more
information, see Log on to Bastionhost from the Apsara Uni-manager Management Console.
2. Choose **Assets** > **Application Management**.
3. On the **Applications** tab of the **Application Management** page, click **Create**
**Application**.
i. In the Basic information step, configure the parameters that are described in the following table and click Next.

| Parameter | Description |
|---|---|
| Application Center | The application center to which the application belongs. |
| Application Type | The type of the application. |
| Application Name | The name of the application. |
| Destination Address | The address of the application. The address of an application is displayed if the application is a web application or a custom application. |
| Database IP Address | The IP address of the database. This parameter is required if the type of the application is Database. |
| Database Name | The name of the database. This parameter is required if the type of the application is Database. |
| Associate Tool | Select an application center tool. |

ii. In the **Create Account** step, click **Create Account**, configure the logon name and password, and then click **Complete**.

**Import multiple applications at the same time**

1. Log on to the Apsara Uni-manager Management Console. For more information, see Log on
to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **O&M Audit** > **Tenant-side Bastionhost**.
3. On the **Tenant-side Bastionhost** page**,** select a region from the **Region** drop-down list
**and** click **Access with Authorized Role.**
4. Choose **Assets** > **Application Management**.
5. On the **Applications** tab of the **Application Management** page, click **Import**
**Application**.
6. On the **Import Application** page, upload the file that is exported from the current system,
select Overwrite Existing Autofill Applications for the **Option** parameter, and then click
**Import**.
You can also click **download a template file**, fill out the template in the specified format, and then upload the template to the system. After you create or import applications, you can perform the following operations to manage the applications: Search: Search for an application by specifying conditions such as name and address. Modify: Find the desired application and click **Modify** in the **Actions** column to modify the application. Delete: Select the desired application and click **Delete** to delete the application.

##### 3.6.5.4 Export applications

This topic describes how to export an application.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Assets** > **Application Management**.
4. On the **Applications** tab of the **Application Management** page, click **Export**
**Application**.

#### 3.6.6 Application account group management

**management**

##### 3.6.6.1 Create an application account group

Application account groups are used to group applications and facilitate batch authorization for applications. This topic describes how to manage application account groups.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Asset** > **Application Account Group Management**.
4. On the **Application Account Group Management** page, click **Create Application**
**Account Group**.
5. In the **Create Application Account Group** dialog box, select a department, enter an
application account group name, and then click **Create Application Account Group**.

##### 3.6.6.2 Add members to an application account group

**group**

This topic describes how to add members to an application account group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Asset** > **Application Account Group Management**.
4. On the **Application Account Group Management** page, find the application account
group to which you want to add a member and click **Add Member** in the **Actions** column.
5. On the **Application Account Group Member** tab of the **Application Account Group**
**Information** page, click **Add Application Account**.
6. In the **Add Application Account** dialog box, select the application accounts that you want
to add and click **Add**. To remove an application account, select the application account that you want to remove and click **Disassociate**.

##### 3.6.6.3 Manage application account groups

This topic describes how to search for, modify, and delete an application account group.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Asset** > **Application Account Group Management**.
4. On the **Application Account Group Management** page, search for, delete, or modify an
application account group.

| Scenario | Description |
|---|---|
| Search for an application account group | In the list of application account groups, search for the desired application account group by specifying conditions such as the name and department of the application account group. |
| Modify the name of an application account group | In the list of application account groups, find the application account group that you want to modify and click Modify in the Actions column. |
| Delete an application account group | Find the application account group that you want to delete and click Delete. |

### 3.7 Authorization

#### 3.7.1 O&M rules

##### 3.7.1.1 Create an O&M rule

O&M rules associate users with host assets in Bastionhost. You can use the O&M authorization feature to allow users to access only hosts on which the users have O&M permissions. This topic describes how to create an O&M rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **O&M Rules**.
4. On the **O&M Rules** page, click **Create O&M Rule**.
5. On the **Create O&M Rule** page, configure the Rule Name and Rule Validity Period
parameters, specify users and assets in the Users and Assets sections, and click **Create**
**O&M Rule**.

##### 3.7.1.2 Export O&M rules

This topic describes how to export O&M rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **O&M Rules**.
4. On the **O&M Rules** page, click **Export O&M Rule**.
5. In the **Export O&M Rules** dialog box, click **Export**.
The result file will be compressed into a ZIP file. You can specify whether to encrypt the ZIP file. If you leave the ZIP Password parameter empty, the ZIP file is not encrypted. The results in the file are not sorted by O&M rule name due to search efficiency issues.

##### 3.7.1.3 Manage O&M rules

This topic describes how to manage O&M rules.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **O&M Rules**.
4. On the **O&M Rules** page, manage O&M rules.

| Scenario | Description |
|---|---|
| Search for O&M rules | Fuzzy match and exact match are supported. You can search for an O&M rule by name and user. |
| Delete O&M rules | To delete multiple rules at a time, select the rules that you want to delete and click Delete. To delete a single rule, find the rule that you want to delete and choose Actions > Delete Rule in the Actions column. |
| Disable O&M rules | Select the rule that you want to disable and clickD isable. |
| Enable O&M rules | Select the rule that you want to enable and clickE nable. |
| Specify the validity period, logon restrictions, and protocol control items for multiple O&M rules at a time | Select the O&M rules that you want to manage and chooseB atch Edit > Rule Validity Period to configure a validity period for the O&M rules. Select the O&M rule that you want to manage and chooseB atch Edit > Logon Restrictions to configure logon restrictions for the O&M rules. Select the O&M rule that you want to manage and chooseB atch Edit > Protocol Control to configure protocol control items. |
| Modify O&M rules | In the Actions column of an O&M rule, choose Actions > Modify Rule to modify the O&M rule. |
| Copy O&M rules | In the Actions column of an O&M rule, choose Actions > Copy Rule to copy the O&M rule. |

| Attach a policy to an O&M rule | In the Actions column of an O&M rule, choose Actions > Associate Policy to attach a policy to the O&M rule. Note An O&M rule can be attached to only one policy. |
|---|---|

#### 3.7.2 Review rules

##### 3.7.2.1 Create a review rule

Review rules can be used to review hosts or O&M rules. You can specify reviewers for review rules and set the review type to command review or secondary review for O&M operations. After you specify reviewers and review objects, the host commands or O&M rules that are specified in the review rule can be reviewed by only the specified reviewers. This topic describes how to create a review rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **Approval Rules**.
4. On the **Review Rules** page, click **Create Review Rule**.
5. On the **Create Review Rule** page, configure the Rule Name, Review Type, Reviewer, and
Review Object parameters and click **Create Review Rule**.

##### 3.7.2.2 Delete a review rule

This topic describes how to delete a review rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **Approval Rules**.
4. On the **Review Rules** page, select the rule that you want to delete and click **Delete**.
5. In the **Delete Review Rule** dialog box, click **OK**.

#### 3.7.3 Review unauthorized logons

##### 3.7.3.1 Perform authorization on review entries

Review of unauthorized logons is to review the relationship between a host and a user and determine whether to allow an unauthorized logon. After authorization, the relationship between the host and the user is created as a fixed O&M rule, and the user does not need to enter the host information if the user wants to perform O&M operations on the host. This topic describes how to perform authorization on review entries.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **Unauthorized Logon Review**.
4. On the **Review of Unauthorized Logons** page, select a review entry and click
**Authorization**.

##### 3.7.3.2 Manage review entries

This topic describes how to search for and delete review entries.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Authorization** > **Unauthorized Logon Review**.
4. On the **Review of Unauthorized Logons** page, search for or delete review entries.

| Scenario | Description |
|---|---|
| Search for a review entry | In the list of review entries, search for the desired review entry by specifying conditions such as the username, host IP address, protocol, and logon name. |
| Delete a review entry | Select the review entry that you want to delete and clickD elete. |

### 3.8 Policies

#### 3.8.1 Create a host command policy

Host command policies are used to control commands that you run when you perform O&M operations on the SSH, Telnet, and Rlogin character protocols. This topic describes how to create a host command policy.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Policy** > **Server Command Policy**.
4. On the **Host Command Policies** page, click **Create Policy**.
5. On the **Create Host Command Policy** page, configure the parameters based on the
following table and click **Create Policy**.

| Parameter | Description |
|---|---|
| Policy name | The name of the policy. |

| Command and Control | Click Create Command Set. In the Create Command Set dialog box, configure the parameters, such as Command Set Name, Action, Log Level, and Match Mode, and click OK. After the command set is created, the result similar to that shown in the following figure is displayed. You can modify the attributes. |
|---|---|

#### 3.8.2 Associate an O&M rule with a host command policy

**command policy**

This topic describes how to associate an O&M rule with a host command policy.

**Prerequisites**

A host command policy is created. For more information, see Create a host command policy. An O&M rule is created. For more information, see Create an O&M rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Policy** > **Server Command Policy**.
4. On the **Host Command Policies** page, find the policy with which you want to associate an
O&M rule and click **Associate O&M Rule** in the **Actions** column.
5. In the **Add O&M Rule** dialog box, select the O&M rule that you want to associate with the
policy and click **Add**. After the association, users authorized by the O&M rule to perform O&M operations are restricted by the host command policy when the users perform O&M operations. When the commands in the command set are run, the actions specified by the policy are triggered, such as blocking the current session or commands.

#### 3.8.3 Manage policies

This topic describes how to modify, copy, and delete a policy.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Policy** > **Server Command Policy**.
4. On the **Host Command Policies** page, manage policies.

| Scenario | Description |
|---|---|
| Search for a policy | In the list of policies, search for the desired policy by name. |

| Modify a policy | On the Host Command Policies page, find the policy that you want to modify and choose Operate more > Modify Policy in the Actions column. |
|---|---|
| Copy a policy | On the Host Command Policies page, find the policy that you want to copy and choose Operate more > Copy Policy in the Actions column. |
| Delete a policy | To delete a single policy, find the policy that you want to delete and choose Operate more > Delete Policy in the Actions column. To delete multiple policies at the same time, select the policies that you want to delete and click Delete. |

### 3.9 Audit

#### 3.9.1 Session audit

##### 3.9.1.1 Search for audit sessions

This topic describes how to use the search feature to search for audit sessions that meet specific conditions.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Session Audit**.
4. On the **All Sessions**, **Ticket Sessions**, and **Application Sessions** tabs of the **Session**
**Audit** page, click **Display More Search Conditions**.
5. Specify search conditions based on your business requirements and click **Search** to view
the session logs that meet the conditions.

##### 3.9.1.2 View all sessions

Session auditing records the session logs of operations that are performed on hosts by O&M engineers. This topic describes how to view all sessions.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Session Audit**.
4. On the **All Sessions** tab of the **Session Audit** page, view the session audit logs of
characters, graphics, files, and applications. You can select a session and perform more audit operations on the session. View session details: Click **Details** in the Actions column to view the details of the session. Download the session file: Click **Download** in the Actions column to download the session file to your on-premises machine. After you download the session file, you can use an offline player to play the audit video. Play the session logs: Click **Play** in the Actions column to view the playback of the session audit on a web page. Online play supports functionalities such as log playback, command recording, and search.

##### 3.9.1.3 View application sessions

Application sessions are used to record the process of application O&M sessions. You can play sessions as videos. This topic describes how to view application sessions.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Session Audit**.
4. On the **Application Sessions** tab of the **Session Audit** page, view application sessions.
You can select a session and perform more audit operations on the session. View session details: Click **Details** in the Actions column to view the details of the session. Download the session file: Click **Download** in the Actions column to download the session file to your on-premises machine. After you download the session file, you can use an offline player to play the session. Play back the session: Click **Play** in the Actions column to view the playback of the session audit on a web page. Online play supports functionalities such as log playback, command recording, and search.

##### 3.9.1.4 View ticket sessions

Ticket sessions are used to record the process of O&M sessions that are established by using tickets. Video playback of ticket sessions is supported. This topic describes how to view ticket sessions.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Session Audit**.
4. On the **Ticket Sessions** tab of the **Session Audit** page, view ticket sessions.
You can select a session and perform more audit operations on the session. View the details of a session: Click **Details** in the Actions column to view the details of a session. Download a session file: Click **Download** in the Actions column to download the session file to your computer. After you download the session file, you can use an offline player to play back the session. Play back a session: Click **Play** in the Actions column to play back and audit a session on a web page. Online playback supports features such as log playback, command recording, and search.

#### 3.9.2 Event auditing

Auditors can search for key events in a session to locate the related complete session. This topic describes how to search for key events such as character commands and graphic texts in a session.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Event Audit**.
4. On the **Event Audit** page, click an event tab based on your business requirements.
**Commands**: You can view the audit logs of character command operations when you
access assets by using the Bastionhost SSH O&M method.
**Graphic Text**: You can view the audit logs that are generated when you access assets by
using the Bastionhost Remote Desktop Protocol (RDP) O&M method.
**File Transmission**: You can view the audit logs of operations such as uploading, deleting,
and renaming files when you access assets by using the Bastionhost O&M method.
**Database Audit**: You can view the SQL statements and execution results of databases
when you perform O&M operations on the databases in Bastionhost.
5. Specify search conditions and click **Search**.
6. In the event list, find the desired event. Click Details in the **Actions**column to view the
session details.

#### 3.9.3 Audit rules

##### 3.9.3.1 Create an audit rule

Audit rules are used to specify the audit data that auditors can audit. Auditors can view only the audit data that is generated when users perform O&M operations on assets that are specified in an audit rule. This topic describes how to create an audit rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Audit Rules**.
4. On the **Audit Rules** page, click **Create Audit Rule**.
5. On the **Create Audit Rule** page, enter a rule name, select an auditor and the assets that
the auditor can audit, and then click **Create Audit Rule**.

##### 3.9.3.2 Manage audit rules

This topic describes how to modify and delete an audit rule.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Audit** > **Audit Rules**.
4. On the **Audit Rules** page, modify or delete an audit rule.

| Scenario | Description |
|---|---|
| Modify an audit rule | In the list of audit rules, find the audit rule that you want to modify and click its name. |
| Delete an audit rule | Select the audit rule that you want to delete and clickD elete. |

### 3.10 Tickets

If an O&M engineer needs to perform O&M operations on a host on which the O&M engineer does not have permissions and a Bastionhost administrator does not enable unauthorized logon, the O&M engineer must submit a ticket to the Bastionhost administrator to obtain the required permissions on the host. After the administrator approves the ticket, the system automatically grants the permissions to the O&M engineer.

**Create a ticket as an O&M engineer**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Ticket** > **My Tickets**.
4. On the **My Tickets** page, click **Create Ticket**.
5. On the **Create Ticket** page, add an asset, specify the validity period and description for
the ticket, and then click **Create Ticket**. After you create the ticket, the ticket displays the information that you specify. The ticket is in the Pending state.

**Review a ticket as a Bastionhost administrator**

Only a Bastionhost administrator has the permissions to review tickets. After an O&M engineer submits a ticket, a Bastionhost administrator must review the ticket.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **Ticket** > **Ticket Approval**.
4. On the **Ticket Review** page, select the ticket that you want to review and approve or
reject the ticket. Click **Approve** to approve a ticket. If a ticket is in the Pending state, you can click the ticket number or click Details in the Actions column of the ticket to modify the ticket. Click **Deny**to reject a ticket.

### 3.11 O&M

#### 3.11.1 Host O&M

##### 3.11.1.1 Configure Bastionhost Assistant

This topic describes how to configure Bastionhost Assistant.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Host O&M** or **Application O&M** tab, click **Bastionhost Assistant** in the
description.
5. Install Bastionhost Assistant to your on-premises machine.
6. Configure the client called by Bastionhost Assistant that uses a specific protocol and click
**Exit**.

##### 3.11.1.2 Configure web-based O&M settings

This topic describes how to configure web-based O&M settings.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. In the upper-right corner of the **Host O&M** page, click **Web-based O&M Settings**.
5. In the **Web-based O&M Settings** dialog box, click a protocol tab, configure the settings,
and then click **Save**.

##### 3.11.1.3 Perform O&M operations on hosts

This topic describes how to perform O&M operations on hosts.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Host O&M** tab, find the host on which you want to perform O&M operations and
click the icon in the **Logon** column.

##### 3.11.1.4 Perform O&M operations on applications

This topic describes how to perform O&M operations on applications.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Application O&M** tab, find the application on which you want to perform O&M
operations and click the icon in the **Logon** column.

##### 3.11.1.5 Perform O&M operations on tickets

If tickets have been approved by the administrator and the tickets are within the validity period, you can access an asset and perform O&M operations on the tickets. This topic describes how to perform O&M operations on tickets.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Ticket O&M** tab, find the ticket on which you want to perform O&M operations and
click **Details** in the **Details** column.
5. In the **Details** dialog box, click **Logon** in the **Logon** column.
6. In the **O&M Logon** dialog box, select a logon method and click **OK**.

##### 3.11.1.6 Perform quick O&M

You can use the quick O&M feature to find the hosts to which you recently logged on for multiple times. The feature is suitable for scenarios in which you need to frequently log on to specific hosts for O&M. This topic describes how to perform quick O&M.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Host O&M** page, enter the hostname, host IP address, or logon name in the upper-
left search box. The system automatically filters the information about the host that you query.
5. In the search result, click the host account and the host that you want to query. Then, you
can log on to the host.

##### 3.11.1.7 Perform HTML5-based O&M

This topic describes how to perform HTML5-based O&M.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of Apsara Stack Security Center, click **Security**. and choose **O&M**
3. Choose **O&M** > **Server O&M**.
4. On the **Host O&M** tab, find the host on which you want to perform O&M operations and
click the icon in the **Logon** column. If you perform HTML5-based O&M, you do not need to install Bastionhost Assistant or a client tool. HTML5-based O&M supports Telnet-, SSH-, RDP-, VNC-, Rlogin-, and SFTP-based O&M. The following operations are not supported during RDP-based O&M: printer and drive mapping, file upload and download by using clipboard, resolution control, and ZMODEM transmission.

#### 3.11.2 Perform real-time monitoring

Real-time monitoring focuses on in-process control. You can use Bastionhost to access an O&M session at any time to view on-site operations, manage sessions of the hosts on which O&M operations are being performed, and perform operations such as reviewing commands or blocking sessions.

**View O&M sessions**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **Real-time Monitoring**.
3. On the **Real-time Monitoring** page, click **All Sessions**.
4. On the **All Sessions** tab, find the desired session and click **Play** in the **Actions** column.
5. On the Real-time Monitoring page, view the real-time status of the O&M operations that are
performed on the session. If commands that need to be reviewed exist, the Command Approval dialog box appears. You can approve or reject the commands based on your business requirements.

**Block sessions**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **Real-time Monitoring**.
3. On the **Real-time Monitoring** page, click **All Sessions**.
4. Select the session that you want to block and click**Block Session**.

#### 3.11.3 Review commands

This topic describes how to review commands.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **Real-time Monitoring**.
3. On the **Real-time Monitoring** page, click **Commands That Require Review**.
4. On the **Commands That Require Review** tab, select the command that needs to be
reviewed and click **Allow** to approve the command or click **Deny** to deny the command.

#### 3.11.4 Process O&M permission requests

O&M permission request processing is the second O&M permission request processing. If the second O&M permission request processing is configured for hosts, O&M engineers cannot directly log on to the hosts even if the engineers are authorized to log on to the hosts. The system automatically generates an O&M permission request, which must be approved by the administrator before the O&M engineers can log on to the hosts.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **Assets** > **Host Management**. On the Host Settings tab of the Host Information
page, select **Enable Session Review**and click Save. image
3. Choose **O&M** > **O&M Approval**.
4. On the**My Applications**tab, view the processing progress of requests for O&M
permissions on hosts.

> **Note:** For the hosts on which the requests for O&M permissions are approved, the Logon text is displayed for the hosts. Click Logon to perform O&M operations on the hosts.

5. On the**O&M Application Review**tab, view the O&M permission requests of O&M
engineers. Select an O&M permission request and click**Approve**. In the O&M Approval dialog box, enter an **approval validity period**to complete the procedure of the O&M permission request.

#### 3.11.5 View, export, and configure the setting for automatically sending O&M reports

**setting for automatically sending O&M**

**reports**

O&M reports are used to collect statistics on O&M operations of the current user. This topic describes how to view and export O&M reports and configure the setting for automatically sending O&M reports.

**View O&M reports**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **O&M Reports**.
3. On the **O&M Reports** page, specify a time range, such as Today, Yesterday, This Week, or
This Month, to view O&M reports. After you select a user, you can view the O&M reports of the user.

**Export O&M reports**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **O&M Reports**.
3. On the **O&M Reports** page, click **Export Report** and select a format to export O&M
reports. You can view the reports after you export them.

**Automatically send O&M reports**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **O&M** > **O&M Reports**.
3. In the upper-right corner of the **O&M Reports** page, click **Automatic Report Sending**. In
the dialog box that appears, configure the Status, Sending Cycle, and File Format parameters, and click **OK**.

### 3.12 Tasks

#### 3.12.1 Password change tasks

The password change task feature of DAS-USM can be used to manage passwords of SSH-, Telnet-, and RDP-based accounts. You can use the password change task feature to create a password change task to automatically change the passwords of SSH-, Telnet-, and RDPbased accounts at the same time or periodically change the passwords of SSH-, Telnet-, and RDP-based accounts.

**Create a password change task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **Tasks** > **Change Plan**.
3. On the Tasks tab of the **Password Change Task** page, click **Create Password Change**
**Task**.
4. On the **Create Password Change Task** page, configure the parameters and click **Create**
**Task**.
The following table describes the parameters.

| Parameter | Description |
|---|---|
| Execution Method | The execution method of the password change task. Valid values: Manual Execution, Scheduled Execution, and Periodic Execution. |

| Password Change Method | The password change method of the password change task. Valid values: Proactive Probing: If you do not know the type of the host whose password you want to change, you can determine the type of the host based on active detection and then change the password of the host. Custom: If you know the type of the host whose password you want to change, you can define a script command to change the password of the host. For information about the script syntax, click Help. Password Change Script: If the managed accounts in multiple password change tasks belong to the same system and the passwords of related hosts must be changed by using a script, you can use the password change script. To configure the password change script, choose System > System Settings > Password Change Script. |
|---|---|
| Password Generation Method | The password generation method of the password change task. Valid values: Automatically Generate Upload Manually Specify |
| Password Sending Mode | The password sending mode of the password change task. Valid values: Do Not Send. Email: Sends the new password to the email address of the user. FTP: Sends the new password to the FTP server. You can specify the path where you want the password to be located. The default path is the root directory of the user account. For example, in the Windows operating system, the default path is C:\Users\****. **** is the name of a specific user. SFTP: Sends the new password to the SFTP server. You can specify the path where you want the password to be located. The default path is the root directory of the user account. For example, in the Windows operating system, the default path is C:\Users\****. **** is the name of a specific user. |

5. On the **Hosted Accounts** tab that is displayed after you create the task, click **Add Host**
**Account**.
6. In the**Add Host Account** dialog box, select the host account that you want to add and
click **Add**. |

**Modify, start, stop, or delete a password change task**

After you create a password change task, you can modify, start, stop, or delete the task on the**Password Change Task**page.

**Modify**

Bastionhost allows you to modify the basic information and associated accounts of a password change task. On the **Password Change Task**page, click the name of the task whose information you want to modify. On the**Basic information**tab, modify the basic information about the task and click**Save**. To modify a managed account, click the **Hosted**
**Accounts** tab. On the **Hosted Accounts** tab, add or remove host accounts.

**Stop**

If you no longer need one or more password change tasks within a specific period of time, you can stop the tasks. On the **Password Change Task** page, select the task that you want to stop and click **Stop**. After the task is stopped, the status of the task changes to
**Canceled**. In this case, the task is not automatically run, and you cannot immediately run
the task.

**Start**

If you want to run one or more password change tasks that are stopped, you can start the tasks. On the **Password Change Task** page, select the task that you want to start and click **Start**. After the task is started, the status of the task changes to **Pending Execution**. In this case, the task is automatically run based on the execution time or cycle that you specify.

**Delete**

If you no longer need one or more password change tasks, you can delete the tasks. On the
**Password Change Task** page, select the task that you want to delete and click **Delete**. In
the Delete Task message, click **OK**.

#### 3.12.2 Automatic O&M

DAS-USM supports automatic O&M operations. This indicates that the system automatically performs O&M operations on behalf of O&M engineers. Automatic O&M supports common commands, interactive commands, and special keys.

**Create an automatic O&M task**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **Tasks** > **Automatic O&M**.
3. On the **Automatic O&M** page, click **Create Automatic O&M Task**.
4. On the **Create Automatic O&M Task** page, configure the Task Name, Execution Method,
O&M Result Sending Method, and Commands parameters, and click **Create Task**.

| Parameter | Description |
|---|---|
| Task Name | The name of the custom task. |
| Execution Method | The execution method of the task. Valid values: Manual Execution, Scheduled Execution, and Periodic Execution. |

| O&M Result Sending Method | The method for sending O&M results. Valid values: Do Not Send. Email: Sends O&M results to the email address of the user. FTP: Sends O&M results to the FTP server. You can specify the path where you want O&M results to be located. The default path is the root directory of the user account. For example, in the Windows operating system, the default path is C:\Users\****. **** is the name of a specific user. SFTP: Sends O&M results to the SFTP server. You can specify the path where you want O&M results to be located. The default path is the root directory of the user account. For example, in the Windows operating system, the default path is C:\Users\****. **** is the name of a specific user. |
|---|---|
| Commands | Commands, interactive commands, and special keys are supported. For information about the format of commands, click Help. |

5. On the **Account** tab that is displayed after you create the task, click **Add Host Account**.
6. In the**Add Host Account** dialog box, select the host account that you want to add and
click **Add**. |

### 3.13 System

#### 3.13.1. [DO NOT TRANSLATE]

##### 3.13.1.1 Configure network settings

This topic describes how to configure a network for Bastionhost.

**Background information**

The network settings that you configure for Bastionhost can ensure the network connectivity of Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Network Configuration**.
3. On the **Network Settings** tab of the **Network Settings** page, configure a network.
You can configure the following items: Protocol ports Interface information TLS security

##### 3.13.1.2 Configure web settings

This topic describes how to configure web settings for Bastionhost.

**Background information**

The web settings that you configure for Bastionhost and the HTTPS service that you enable can ensure the security of Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Network Configuration**.
3. On the **Web settings** tab of the **Network Settings** page, configure the web settings.
You can configure the following items: Enable or disable national secret communications. Enable or disable IPv6.

#### 3.13.2. [DO NOT TRANSLATE]

##### 3.13.2.1 Configure security settings

This topic describes how to configure security policies for user logons.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Authentication Management**.
3. On the **Security Settings** tab of the **Authentication Management** page, configure
security policies for Bastionhost. In the **Logon Settings** section, you can configure the Logon Timeout Period, Verification Code Expires After, and Simultaneous Logons parameters and click **Save** to save your configurations. In the **User Lockout** section, you can configure the Account Lockout Threshold, Account Lockout Duration, and Reset Account Lockout Count parameters and click **Save** to save your configurations. In the **Password Policy Settings** section, you can specify a password policy based on your business requirements and click **Save** to save your configurations.

##### 3.13.2.2 Configure remote authentication

This topic describes how to configure remote authentication.

**Background information**

Bastionhost supports remote authentication methods such as Active Directory (AD), Lightweight Directory Access Protocol (LDAP), and Remote Authentication Dial-In User Service (RADIUS). The remote authentication methods can be used to manage users and passwords in a unified manner to ensure the security of Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Authentication Management**.
3. On the Remote Authentication tab of the **Authentication Management** page, configure
the parameters for remote authentication. In the **Local Authentication** section, select whether to enable local authentication. If local authentication is disabled, users cannot log on to Bastionhost by using the local authentication method. In the **Remote Authentication AD/LDAP** section, set Remote Authentication to LDAP or AD, configure other related parameters, and then click **Connection testing**. Click
**Immediately Synchronize Users** to synchronize the AD or LDAP server users to
Bastionhost. In the **Remote Authentication RADIUS** section, set Remote Authentication to Disable or RADIUS. Three RADIUS authentication modes are provided: If you set Authentication Mode to Username + Password, authentication is performed based on a username and a password. If you set Authentication Mode to Username + Dynamic Code, authentication is performed based on a username, a password, and a dynamic code. If you set Authentication Mode to Username + Dynamic Code + Token PIN, authentication is performed based on a username and a password, or based on a username, a token PIN, and a dynamic code.

##### 3.13.2.3 Configure two-factor authentication

This topic describes how to configure two-factor authentication.

**Background information**

The two-factor authentication mechanism uses SMS passwords and OTP app tokens to control the risk of account password leaks and prevent account abuse for O&M engineers. After twofactor authentication is enabled, O&M engineers must perform the following operations to log on to Bastionhost: Enter the account password. After the password is verified, enter an authentication password to log on to Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Authentication Management**.
3. On the Remote Authentication tab of the **Authentication Management** page, configure
the parameters for remote authentication. In the **Two-factor Authentication** section of the Two-factor Authentication tab, configure the Authentication Method parameter and click **Save**. Two-factor authentication supports passwords, OTP app tokens, and SMS passwords. If Password is one of the options that you selected, a password is preferentially used for authentication. This indicates that O&M engineers must enter an account password to log on to Bastionhost. If Password is not selected and you select Password and Text Message Verification Code or Password and OTP App Token for the Authentication Method parameter, O&M engineers must perform the following operations to log on to Bastionhost: Enter the account password. After the password is verified, enter an authentication password to log on to Bastionhost. In the **SMS setting** section of the Two-factor Authentication tab, configure the Status parameter, select the SMS gateway that you want to use, and enter the information about the gateway. Enter a mobile phone number and click Send Text Message for Test to test whether the SMS gateway is available.

#### 3.13.3 System settings

##### 3.13.3.1 Configure O&M management settings

This topic describes how to configure O&M management settings, including unauthorized logons, O&M logons, SSH logons, and O&M duration limits.

**Background information**

You can specify items such as the logon method and logon duration for O&M engineers by configuring O&M management settings to ensure O&M security.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **System Configuration**.
3. On the **O&M Settings** tab of the **System Settings** page, configure the parameters.
Unauthorized Logon: settings that are related to unauthorized logons. If you select
**Allows Unauthorized Web-based Logons** , O&M engineers can perform O&M
operations on assets on which they are not authorized to perform O&M operations by using the unauthorized logon method on the **O&M** page.
**Collects Information About Unauthorized Logons** : After a user logs on to
Bastionhost to perform O&M operations on a host by using the unauthorized logon method, the system automatically collects information about the relationship between the user and the host. You can view the relationship on the **Review of Unauthorized**
**Logons** page.
**Collects Passwords of Host Accounts**: After a user logs on to Bastionhost to
perform O&M operations on a host by using the unauthorized logon method, the system automatically collects information about the username and password of the host account.
**Automatically Creates O&M Rules**: If the system detects unauthorized logons, the
system automatically creates the related authorization relationship. The administrator does not need to manually authorize a user to perform O&M operations on hosts. O&M Logon:
**Allows Host Logons by Using Password of User**: allows a user to log on to a host
by using the password of the Bastionhost account of the user. If you select this option, related items are displayed in the account list on the Host O&M page. For example, the [SYSDEF][SELF] account is displayed for each host on the page, and you can use the account to log on to a host. A user needs to select this option if both the user and the host account are authenticated by using Active Directory (AD) or Lightweight Directory Access Protocol (LDAP).
**Allows Host Logons by Using SSH Private Key of User**: If a user selects this
option, Bastionhost allows the user to log on to a host to perform O&M operations by using the added SSH private key of the Bastionhost account of the user instead of the password of the host account.
**Allows SSH Server Logons by Using SSH-agent-forwarding Mode** : If a user
selects this option, Bastionhost supports the SSH agent forwarding feature. Users need to select this option if the same SSH private key is used to log on to Bastionhost and the SSH server. To use this feature, you need to enter an SSH banner in the SSH banner field. SSH Logon:
**Allows Logon by Using Public Key** : If a user selects this option, the user can log on
to the O&M audit system by using an SSH public key.
**Allows Logon by Using Password** : If a user selects this option, the user can log on to
the O&M audit system by using a password.
**Allows Sending Environment Variables** : If a user selects this option, the user can
configure the setting to allow for sending of O&M user information and O&M source IP address.
**Uses Shell**: If a user selects this option, the user can log on to a host by using the CLI.
Idle Timeout Interval If the idle duration for a protocol connection exceeds this limit, the network connection is automatically disconnected. Definition of the idle state for each type of protocol connection: rdp and vnc: when no data is sent from the client. ftp: when no data is sent from the command channel or data tunnel. ssh, telnet, and sftp: when no data is sent from the client or server. Limits on User Sessions The number of user sessions.

##### 3.13.3.2 Configure alert settings

This topic describes how to configure alert settings for Bastionhost.

**Background information**

In Bastionhost, alert notifications for operations performed by users are sent by email or Syslog. This allows managers to receive related notifications and handle alerts at the earliest opportunity based on actual conditions.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **System Configuration**.
3. On the **Alert Settings** tab of the **System Settings** page, configure the parameters for an
alert. In the Alert Notification Settings section, you can select whether to enable operation logs. If you set Operation Logs to Enable, you can configure the Email Alerting and Syslog Alerting parameters. You can also decide whether to select Sends to Syslog Server. After the configuration is complete, click **Save**. In the System Resource Alerting Settings section, you can configure the Alert Thresholds and Email Alerting parameters. In the Email Settings section, you can configure the Server Address, Port Number, Username, Password, and Recipient parameters, and click Send Test Email to test whether the email is successfully configured. Click **Save** to save your configurations. Then, specify other items such as the status, severity level of the alert for system logs, and policy log alert. In the Syslog-related Settings section, you can configure the Sender ID, Server IP Address, Port Number, and Data Format parameters, and click Send Test Data to test whether the connection is established. Click **Save** to go back to the management page. Then, specify other items such as the status, severity level of the alert for system logs, and policy log alert. You can select whether to send host commands to the Syslog server.

##### 3.13.3.3 Configure the language and user interfaces

**interfaces**

This topic describes how to configure the language and user interfaces (UIs) for Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **System Configuration**.
3. On the **Language and UI** tab of the **System Settings** page, configure the parameters for
the language and background. In the Language Settings section, you can configure the System Language parameter. Valid values are Simplified Chinese, Traditional Chinese, and English. In the Background Image Settings section, you can upload a custom page logo image and background image of the logon page.

##### 3.13.3.4 Configure features

This topic describes how to configure the features of Bastionhost.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **System Configuration**.
3. On the **Feature Settings** tab of the **System Settings** page, configure the parameters for
features. You can configure the following features. After the configuration is complete, click **Save**. Department management Host export settings Asset scan settings Ticket settings Automatic report statistics

##### 3.13.3.5 Create a password change script

This topic describes how to create a password change script.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **System Configuration**.
3. On the **Password Change Script** tab of the **System Settings** page, click **Create**
**Password Change Script**.
4. In the **Create Password Change Script** dialog box, configure the Script Name and Script
Commands parameters and click **Create**.

#### 3.13.4 Storage management

##### 3.13.4.1 Archive data

Storage management allows you to view the disk size of Bastionhost and manage the data information in Bastionhost. This topic describes how to use the data archiving feature.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Storage Management**.
3. On the **Storage Settings** page, click **Data Archiving**.
In the **Data Disk Usage** section, view the usage of data disks. In the **Video Archiving** section, you can enable or disable the video archiving feature and send archived data to the destination server by using FTP or Secure File Transfer Protocol (SFTP). In the **Automatically Delete** section, you can configure the system to delete data that is generated specific days ago.

##### 3.13.4.2 Back up logs

You can use the log backup feature to back up operation logs and session logs. You can also download backup logs and save them to your on-premises machine. This allows managers to view the logs in the future. 1.
2. Choose **System** > **Storage Management**.
3. On the **Storage Settings** page, click **Log Backup**.
4. On the **Log Backup** tab, you can configure the Time Range, Description, and Content
parameters and click **Create Log Backup**. In the Backup Files section, click **Download** in the Actions column to download the backup file to your on-premises machine. In the Backup Files section, click **Delete** in the Actions column to delete the backup file.

#### 3.13.5 View system operation logs

Operation logs are generated when you perform operations or configure Bastionhost. You can view all operation logs on the Web Management page of Bastionhost, or use multiple filter conditions to query specific log records.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Operation Logs**.
3. On the **Operation Logs** tab of the **Operation Logs** page, you can search for or export
logs. Click the Operation Log Settings tab. On this tab, you can configure the priority level of each type of log.

#### 3.13.6 View system reports

This topic describes how to view system reports. 1.
2. Choose **System** > **System Reports**.
3. On the **System Reports** page, view information about system reports.
You can view information about the following types of system reports.

| Tab | Description |
|---|---|
| System Status | Displays the resource usage of the system, including the CPU utilization, memory usage, system partition space usage, and session partition space usage. |
| Operation Priority | Displays the distribution of system operations with different priorities. For more information, see Operation log classification in Operation logs. |
| User Control | Displays the distribution of locked users and unlocked users. |
| Host Control | Displays the distribution of hosts on which O&M is disabled and hosts on which O&M is enabled. |
| Session Control | Displays the session control trend. |
| Operations Related to Users and Assets | Displays the number of added and deleted users, user groups, hosts, and host accounts. |
| Source IP Addresses of Users | Displays the top five users with the maximum number of source IP addresses. |
| Abnormal Users | Displays the top five users with the maximum number of logon attempt failures. |

| Abnormal IP Addresses | Displays the top five IP addresses with the maximum number of logon attempt failures. |
|---|---|

4. Click the **Export Report** tab. On this tab, configure the Frequency, Time Period, and File
Format parameters and click **Export System Report** to export a complete system report to your on-premises machine.

#### 3.13.7. [DO NOT TRANSLATE]

##### 3.13.7.1 View the system time

This topic describes how to view the system time.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Local Maintenance**.
3. On the **System Management** tab of the **Host Maintenance** page, view the system time.

##### 3.13.7.2 Upgrade Bastionhost

This topic describes how to upgrade Bastionhost.

**Prerequisites**

The valid Bastionhost upgrade package is obtained.

**Background information**

Upgrading the Bastionhost system version makes the running of Bastionhost more stable.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Local Maintenance**.
3. On the **System Update** tab of the **Host Maintenance** page, click Upload Tool File.
After the restart is complete, the system is upgraded to the latest version.

##### 3.13.7.3 Back up and restore system settings

This topic describes how to back up and restore system settings.

**Background information**

If you want to replace the current bastion host, you can back up the system settings of the current bastion host and restore the system settings for the new bastion host to implement rapid deployment of bastion hosts.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Local Maintenance**.
3. On the **System Backup** tab of the **Host Maintenance** page, back up or restore system
settings. In the Automatic Backup of System Settings section, set Status to Enable, specify the backup frequency and retained automatic backup files, and then click **Save**. In the Manual Backup of System Settings section, configure the Description parameter and click **Create System Setting Backup File** . The backup file will be displayed in the Backup Files section. In the System Settings Upload and Restoration section, click **Upload System Setting**
**File**. The backup system setting file will be restored in the system.
In addition to backup and restoration, you can also perform the following operations: Download a backup file a. In the **Backup Files** section, find the backup file that you want to download. b. Click **Download** in the Actions column to download the backup file. Delete a backup file a. In the **Backup Files** section, find the backup file that you want to delete. b. Click **Delete** in the Actions column to download the backup system setting file.

##### 3.13.7.4 Push and receive system settings

This topic describes how to synchronously push and receive system settings.

**Background information**

If you enable system setting pushing, Bastionhost periodically pushes the system settings of the current bastion host to the destination bastion host. The feature of synchronously pushing and receiving system settings enables other bastion hosts to use the same system settings as those of the current bastion host, which helps achieve rapid deployment of multiple bastion hosts at a time.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Local Maintenance**.
3. On the **Host Maintenance** page, click **Synchronous Push of System Settings**.
4. In the **System Setting Push** section, enable the push feature and click **Save**.

| Parameter | Description |
|---|---|
| Status | Set the value to Enable. |
| Frequency | The push frequency. |
| Push Key | The key for push authentication. |

5. In the **Add Destination Device** section, specify the bastion host to which you want to
push system settings and click **Add Destination Device**.

| Parameter | Description |
|---|---|
| Name | The name of the destination bastion host. |
| Destination IP Address | The IP address of the destination bastion host. |

6. In the **Destination Devices** section, you can view and delete the destination bastion host,
or manually push the system settings of the current bastion host to the destination bastion host. If you enable system setting pushing, Bastionhost periodically pushes the system settings of the current bastion host to the destination bastion host.

##### 3.13.7.5 View debugging logs

This topic describes how to view debugging logs.

**Background information**

If issues such as a running failure occur on a bastion host, you can view debugging logs to locate the root cause of the issue.
1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. Choose **System** > **Local Maintenance**.
3. On the **Debugging Logs** tab of the **Host Maintenance** page, perform debugging.
Click **Disable Refresh** to pause the update of debugging logs. Click **Export Log** to export the debugging logs to your on-premises machine for viewing.

## 4 Best practices

### 4.1 Configure a DNAT entry to access a bastion host over the Internet

**access a bastion host over the**

**Internet**

**Background information**

In view of system security, public endpoints are disabled for tenant-side bastion hosts. You can configure DNAT entries to access bastion hosts over the Internet in a secure manner.

**Step 1: Obtain the vpc_vip value of a bastion host**

1. Log on to Bastionhost. For more information, see Log on to Bastionhost from the Apsara
Uni-manager Management Console.
2. In the bastion host list, obtain a private endpoint of the bastion host that you want to
manage and run the ping command to obtain the corresponding IP address. The private endpoint can be accessed only within the virtual private cloud (VPC) of the current user. Record the **vpc_vip** and **user_vpc_id** values obtained by running the `ping` command for later use.

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
over the More icon in the Actions column, and click **Associate EIP**.
2. In the dialog box that appears, select the EIP that you created in **Step 2**.

**Step 5: Configure a DNAT entry**

1. In the NAT gateways list, find the NAT gateway that you created and click **Set DNAT** in the
Actions column.
2. On the **DNAT Management** tab, click **Create DNAT Entry**.
Configure the parameters as required. Set the Public IP Address parameter to the EIP that you created and associated with the NAT gateway in **Step 2**, set the Private IP Address parameter to the **vpc_vip** value of the bastion host, and then specify Protocol Type based on your business requirements.
3. In the DNAT entry list, obtain the public IP address of the created DNAT entry.

**Step 6: Use a public IP address to access the bastion host**

Access the bastion host by using the public IP address obtained in **Step 5** from a browser.
