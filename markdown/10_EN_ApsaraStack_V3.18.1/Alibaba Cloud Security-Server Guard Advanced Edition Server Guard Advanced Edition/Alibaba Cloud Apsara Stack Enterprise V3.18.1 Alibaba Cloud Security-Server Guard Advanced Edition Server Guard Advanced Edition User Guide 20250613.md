---
title: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613"
product_version: "V3.18.1"
doc_version: "20250613"
pdf_pages: 90
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3.18.1%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%AE%89%E9%AA%91%E5%A3%AB/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.18.1%20Alibaba%20Cloud%20Security-Server%20Guard%20Advanced%20Edition%20Server%20Guard%20Advanced%20Edition%20User%20Guide%2020250613.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.18.1 Alibaba Cloud Security-Server Guard Advanced Edition Server Guard Advanced Edition User Guide 20250613

## Table of Contents

- 1 Usage notes
- 2 Quick start
  - 2.1 User roles and permissions
  - 2.2 Log on to the Apsara Uni-manager Management Console
- 3 Server Guard
  - 3.1 Server security overview
  - 3.2 Assets
    - 3.2.1 Assets
    - 3.2.2 Server fingerprints
  - 3.3 Threat protection
    - 3.3.1 Vulnerability management
      - 3.3.1.1 Manage Linux vulnerabilities
      - 3.3.1.2 Manage Windows system vulnerabilities
      - 3.3.1.3 Manage Web-CMS vulnerabilities
      - 3.3.1.4 Manage urgent vulnerabilities
      - 3.3.1.5 Configure vulnerability management policies
    - 3.3.2 Baseline check
      - 3.3.2.1 Baseline check overview
      - 3.3.2.2 Create baseline check policies
      - 3.3.2.3 View baseline check results and handle baseline risks
    - 3.3.3 Risk exposure detection
    - 3.3.4 Application protection
  - 3.4 Intrusion prevention
    - 3.4.1 Virus detection and removal
    - 3.4.2 Website tamper-proofing
      - 3.4.2.1 Overview
      - 3.4.2.2 Configure tamper proofing
      - 3.4.2.3 View protection status
    - 3.4.3 Application whitelist
    - 3.4.4 Attack analysis
    - 3.4.5 Security alert
      - 3.4.5.1 Overview
      - 3.4.5.2 View and handle alert events
      - 3.4.5.3 View exceptions related to an alert
      - 3.4.5.4 Quarantine
      - 3.4.5.5 Configure alerts
  - 3.5 Log retrieval
    - 3.5.1 Log retrieval overview
    - 3.5.2 Query logs
    - 3.5.3 Supported log sources and fields
    - 3.5.4 Logical operators
  - 3.6 Server settings
    - 3.6.1 Install the Security Center agent
    - 3.6.2 Manage protection modes
- 4 Apsara Stack Security configurations
  - 4.1 Log on to the Apsara Uni-manager Management Console
  - 4.2 System monitoring
  - 4.3 Rules
    - 4.3.1 Create and manage IPS rules
    - 4.3.2 Manage Anti-DDoS Service rules
    - 4.3.3 Manage Server Guard rules
    - 4.3.4 Create and manage WAF rules
  - 4.4 Alert settings
  - 4.5 Updates
    - 4.5.1 Upgrade center overview
    - 4.5.2 Update feature libraries or the version of Apsara Stack Security
    - 4.5.3 Download update packages
  - 4.6 Global configuration
    - 4.6.1 Configure host security rules
    - 4.6.2 Configure a whitelist
    - 4.6.3 Configure the attack blocking feature
    - 4.6.4 Add a Server Guard account
  - 4.7 Cloud Firewall monitoring
  - 4.8 Account management
    - 4.8.1 Manage Apsara Stack tenant accounts
    - 4.8.2 Manage Alibaba Cloud accounts

## 1 Usage notes

Before you log on to Apsara Stack Security Center, make sure that your computer meets the configuration requirements. For more information about the configuration requirements, see . Table 1. Configuration requirements

| Item | Requirement |
|---|---|
| Browser | Internet Explorer: V11 or later Google Chrome (recommended): V42.0.0 or later Mozilla Firefox: V30 or later Safari: V9.0.2 or later GmSSL browser that runs the Chrome kernel: V69.0.0 or later |
| Operating system | Windows XP Windows 7 or later macOS Anolis OS |

## 2 Quick start

### 2.1 User roles and permissions

This topic describes the user roles involved in Apsara Stack Security. All roles in Apsara Stack Security Center are provided by default. You cannot create custom roles. Before you log on to Apsara Stack Security Center, make sure that your account is assigned the required role. For more information, see Default roles in Apsara Stack Security. Table 1. Default roles in Apsara Stack Security

| Role name | Description |
|---|---|
| Organization security administrator | Uses SOC to manage the security of hosts, applications, and networks for an organization. This role also manages security products related to Elastic Compute Service (ECS). |
| Global organization security administrator | Uses SOC to conduct security management for Apsara Stack and all tenants, and manages security products related to ECS. |

If you do not have an account that assumes the required role, contact the administrator to create an account and assign the role to the account. For more information, see the **Create a**
**user** topic in **Apsara Uni-manager Management Console User Guide** .

### 2.2 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You must obtain the username and password from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform corresponding
operations in the following scenarios: It is the first time that you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password that you entered in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

## 3 Server Guard

### 3.1 Server security overview

This topic describes how to view the details of server security on the security overview page of Apsara Stack Security Center. This helps security administrators understand the security status of the servers. The servers refer to servers on the cloud. To view the security overview and the security dashboards, log on to Apsara Stack Security Center and choose **Server Guard > SecurityOverview**. Security Overview

**Security Overview**

This tab displays the numbers of security vulnerabilities and security events on servers. For security vulnerabilities, you can view **Unhandled Vulnerabilities** and **Baseline Risks**. For security events, you can view **Unhandled Alerts**, **Precision Defense (Nearly 15 Days)**, and **File Tampering Attempts Prevented in Last 15 Days** .
**Server Risks**: This section displays the number of unhandled vulnerabilities, the number of
baseline risks, and the distribution of risk levels.
**Asset Protection**: This section displays the number of protected servers and the number
of offline servers.
**Recent Important Security Risks and Intrusions**: This section displays the recent risks
and events on your servers. You can click a risk or an event to view the details.
**Operating System Distribution**: This section displays your servers by operating system.

**Security Screen**

The tab displays data such as assets, vulnerabilities, baselines, and alerts. You can configure the custom content of a dashboard based on your business requirements.

**Configure the custom content of a dashboard**

1. On the **Security Screen** tab, click **Direct access**.
Security Screen
2. On the page that appears, click the
icon in the upper-right corner.
3. On the **Configurations** tab, configure the following information: **Title** and **Title**
**Decoration**.
4. **Optional.** Click the **Select Statistics** tab and complete the data configuration.
Select the type of data that you want to display in real time on the dashboard. You can select **All** or a data type.
5. Click **Save**.

**Create a custom scenario-specific dashboard**

You can create custom scenario-specific dashboards based on your business requirements.
1. On the **Security Screen** tab, click **Direct access**.
Security Screen
2. On the page that appears, click the
icon in the upper-right corner.
3. On the **Scenarios** page, click **Create**.
4. On the **Configurations** tab, configure the following information: **Title** and **Title**
**Decoration**.
5. **Optional.** Click the **Select Statistics** tab and complete the data configuration.
Select the type of data that you want to display in real time on the dashboard. You can select **All** or a data type.
6. Click **Save**.
If you want to display a dashboard, find the dashboard on the **Scenarios** page and click
**Enable Now**.

> **Note:** The number of dashboards that you can create is unlimited.

**Introduction to the dashboard**

**Vulnerabilities**

The **Vulnerabilities** section displays the total number of vulnerabilities in your assets, a doughnut chart that shows the proportions of vulnerabilities of different priorities, the number of vulnerabilities of each priority, and a chart that shows the vulnerability information in the last seven days. **In this section, the following information is displayed:**
**Total**: The total number of vulnerabilities in your assets.
**Urgent**: The number of vulnerabilities that must be fixed at the earliest opportunity. The
status icon is a red dot.
**Moderate**: The number of vulnerabilities that can be fixed at a later point in time. The
status icon is an orange dot.
**Low**: The number of vulnerabilities that do not require a fix. The status icon is a grey dot.
A chart that shows the number of vulnerabilities of each priority in the last seven days.

**Assets**

The **Assets** section displays the statistics about detected assets. **In this section, the**

**following information is displayed:**

**Total**: The total number of assets.
**Compromised**: The number of servers with unhandled high-risk alerts. The status icon is a
red dot.
**At-risk**: The number of servers with vulnerabilities, baseline risks, or medium- or low-risk
alerts. The status icon is an orange dot.
**Safe**: The number of servers without vulnerabilities, baseline risks, or alerts. The status
icon is a green dot. A list that displays the top five high-risk assets and the corresponding status.

**Baseline Check**

The **Baseline Check** section displays the total number of baseline risks in your assets, the number of check items at each risk level, and a chart that shows the check items at each risk level in the last seven days. Real-time data is displayed. **In this section, the following**

**information is displayed:**

**Total**: The total number of at-risk check items in your assets.
**High**: The number of high-risk check items. The status icon is a red dot. We recommend
that you troubleshoot and handle the risks at the earliest opportunity.
**Medium**: The number of medium-risk check items. The status icon is an orange dot.
**Low**: The number of low-risk check items. The status icon is a grey dot.
A chart that shows the check items at each risk level in the last seven days.

**Security Trend**

The **Security Trend** section displays the trend chart of security scores in the last seven days, 15 days, or 30 days. Real-time data is displayed.

**Alert**

The **Alert** section displays the information about the top 5 unhandled high-risk alerts in the last 24 hours, including the alert time, alert name, and the affected servers.

**Attack Source Top5**

The **Attack Source Top5** section displays the top five attacker IP addresses and the number of attacks on your server in the last 24 hours.

**Cloud Platform Best Practices**

The **Cloud Platform Best Practices** section displays the information about the check items that are detected by the configuration assessment feature in real time. In this section, the following information is displayed:
**Check Item**: The check items that are supported by the configuration assessment feature.
**Risk Level**: The risk level of a check item. The following items describe the relationship
between colors and risk levels. Red: indicates a high level of risk. Orange: indicates a medium level of risk. Gray: indicates a low level of risk. Green: indicates a normal state.
**Affected**: the number of affected assets.

**High-risk Assets**

The **High-risk Assets** section displays the top five high-risk assets.

### 3.2 Assets

#### 3.2.1 Assets

After you add servers to Server Guard, you can manually synchronize the information about the most recent servers, view server information, and manage servers by group. This topic describes how to manage servers.

**Synchronize the information about the most recent servers**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Assets** > **Asset Management**.
4. On the **Assets** page, click **Synchronize Assets**.
Server Guard obtains the information about the most recent servers and updates the server list.

> **Note:** The system takes 1 minute to update the information. Wait until the information is updated.

**View server information**

1. Log on to Apsara Stack Security Center. For more information, see Log on to Apsara Stack
Security Center.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Assets** > **Asset Management**.
4. On the **Assets** page, view server information.
View the information about servers that match one or more search conditions You can configure search conditions above the server list to search for a server. The search conditions include **Instance name**, **Internet IP**, and **Private IP**. You can configure one or more search conditions. Find a server that you want to manage and view the security status of the server in the
**Risk profile** column.
Find a server whose details you want to view and click **Fix** in the **Details** column. On the details page of the server, view the details of the server.

| Tab | Description |
|---|---|
| Basic Information | Risk State: displays risks such as vulnerabilities and alerts. Detail: displays the basic information about the server. The information includes ID, Region, Group, and OS. Cloud disk snapshot: displays disk snapshots. Vulnerability check: displays the types of vulnerabilities that can be detected. You can specify the types of vulnerabilities that you want to detect for the server. Asset Investigation: displays server fingerprints. Login security setting: displays the added approved logon locations, approved IP addresses, approved time ranges, and approved accounts. You can manage alerts for the server. |
| Vulnerabilities | This tab displays the vulnerabilities that are detected on the server. |
| Alerts | This tab displays the alerts that are generated for the server. |
| Non-exposure | This tab displays information about servers that are exposed on the Internet. |
| Baseline Risks | This tab displays the baseline check results of the server. |

| Asset Fingerprints | This tab displays information about the fingerprints of the server. |
|---|---|

View the information about servers in a category. Server Guard allows you to manage servers by category. The categories include **Security Risk** and **Asset attribute**. In the server list, you can perform the following operations.

| Operation | Procedure |
|---|---|
| Classify servers | i. Select the required servers and choose Asset Classification > Group below the server list. ii. In the Group dialog box, select a group and click OK. |
| Send commands to servers | i. Select the required servers and click Order issuance below the server list. ii. In the Order issuance dialog box, select required items and click OK. |
| Export information | Select the server whose information you want to export and click the information that you want to export below the server list. You can export basic asset information, weak password information, asset vulnerability information, baseline risk information, baseline check information, and client logs. |

**Add multi-cloud servers**

Server Guard allows you to protect and manage third-party cloud servers and servers in data centers. The following procedure describes how to add a multi-cloud or data center provider.
1. Log on to Apsara Stack Security Center. For more information, see Log on to Apsara Stack
Security Center.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Assets** > **Asset Management**.
4. In the left-side navigation tree, click Providers below **Asset classification management**.
5. Click Create Provider. In the dialog box that appears, specify theprovider information**.**
If the provider does not define regions, retain the default region created by the system to manage data center information. After the provider is added, you can perform the following operations in the **Actions** column: **Edit**, **Delete**, and **Add Region**.

**Manage server groups and tags**

1. Log on to Apsara Stack Security Center. For more information, see Log on to Apsara Stack
Security Center.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Assets** > **Asset Management**.
4. In the left-side navigation tree of the **Assets** page, manage server groups and tags.
Manage server groups: You can add servers to server groups in advance. This way, when you use the features of Server Guard, you can select servers on which you want the features to take effect by server group. The features include web tamper proofing, baseline check, and vulnerability scan. In the left-side navigation tree, click **Server Group** below **Asset classification**
**management**. On the**Server Group** page, you can manage server groups.
Create a server group: Click**Add Group**. In the dialog box that appears, enter a group name in the **Group name**field, select servers that you want to add to the group, and then click**OK**. Modify a server group: Find the server group that you want to modify and click
**Manage** in the**Actions**column.
Delete a server: Find the server that you want to delete and click**Delete** in the
**Actions**column.
Manage server tags: You can add **tags** to servers to identify their special attributes. This allows you to search for servers that have the same attributes. In the left-side navigation tree, manage server tags in the **Tag** section. Create a tag: Click **Management**. In the Add tag dialog box, enter a tag name, select the servers to which you want to add the tag, and then click **OK**. Delete a tag: Find the tag that you want to delete and click the icon. In the**Note** message, click**OK**.

#### 3.2.2 Server fingerprints

This topic describes how to view the information about the listening port on a server, the software version, the process, the account, the scheduled task, and middleware.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Assets** > **Server Fingerprints**.
4. Click **Settings**. In the dialog box that appears, configure the fingerprint collection
frequency.
5. On the **Server Fingerprints** page, view the server fingerprints.
On the **Overview** tab, view the server fingerprints.

**Port**

> **Note:** You can view information about listening ports to perform the following checks: check for servers that listen on a specific port and check for ports on which a specific server listens.

On the **Port** tab, view the **Port**, **Protocol**, and Server parameters. You can search for a port by port number, server process name, server name, or server IP address. In the server information list, you can view the **process**, **IP address**, and **latest scan**
**time** of a server.

**Manage software versions**

> **Note:** You can view information about software versions to perform the following checks and operation: check for software assets that are installed without authorization, check for outdated versions of software assets, and identify affected assets if vulnerabilities are detected.

On the **Software** tab, view all the **software assets** that are in use and the **numbers of**
**servers** that use the software assets.
You can search for specific software by name, version, installation directory, server name, or IP address. Click the name of software to view the software details, such as the software version and the servers that use the software. You can click the icon in the upper-right corner to download a software version table to your computer for subsequent asset check.

**Manage running processes**

> **Note:** You can view information about running processes to perform the following checks: check for servers on which a specific process runs and check for processes that run on a specific server.

On the **Server Fingerprints** page, click the **Process** tab to view all running processes and the number of servers on which these processes are running. You can search for a process by **process name**, **running user**, **startup parameter**,
**server name, or IP address**.
Click the name of a process to view the details of the process, such as the servers, paths, and startup parameters.

**Manage accounts**

> **Note:** You can view information about accounts to perform the following checks: check for servers on which a specific account is created and check for accounts that are created on a server.

On the **Server Fingerprints** page, click the **Accounts** tab to view all logged-on accounts and the number of servers on which the accounts are created. You can search for an account by account name, root permissions, server name, or IP address. Click the name of an account to view the details of the account, such as the server information, root permissions, and user group.

**Manage scheduled tasks**

On the **Server Fingerprints** page, click the **Scheduled Tasks** tab. On the tab that appears, view the paths of all tasks and the numbers of servers that run these tasks. You can search for a task by using path, server name, or IP address. Click a task path to view the details such as the servers, executed commands, and task cycles.

**Manage middleware**

On the **Server Fingerprints** page, click the **Middleware** tab. On the tab that appears, view the number of middleware fingerprints of all tasks. You can search for a task by using path, server name, or IP address. Click a task path to view the details such as the servers, executed commands, and task cycles.

**Manage startup items**

On the **Server Fingerprints** tab, click the **Startup Items** tab to view the startup items and the number of fingerprints.

### 3.3 Threat protection

#### 3.3.1 Vulnerability management

##### 3.3.1.1 Manage Linux vulnerabilities

This topic describes how to manage Linux vulnerabilities.

**Background information**

Apsara Stack Security automatically scans software that is installed on your servers to detect the vulnerabilities in the Common Vulnerabilities and Exposures (CVE) list. Apsara Stack Security also sends you alert notifications about the detected vulnerabilities. In addition, Apsara Stack Security provides commands that you can use to fix vulnerabilities and allows you to verify vulnerability fixes.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Linux Software** tab, view the detected Linux vulnerabilities.

> **Note:** You can search for specific vulnerabilities by using the search and filter features.

5. Click a vulnerability. In the panel that appears, you can view the details of the vulnerability
and the assets that are affected by the vulnerability.

> **Note:** You can find the affected assets by using the search and filter features.

**Detail**: This tab displays the basic information about the vulnerability.
**Pending vulnerability**: This tab displays the servers that are affected by the
vulnerability.
6. Fix a vulnerability based on the impact.
Table 1 Operations to fix vulnerabilities

| Operation | Description |
|---|---|

| Generate Fix Command | Select this option to generate the commands that can be used to fix the vulnerabilities. Then, you can log on to the server and run these commands. |
|---|---|
| Fix | Select this option to fix the vulnerability. |
| Restarted and Verified | If a vulnerability fix takes effect only after a server reboot, reboot the server after the status of the vulnerability changes to Fixed (To Be Restarted). After the reboot, click Restarted and Verified. |
| Ignore | Select this option to ignore the vulnerability. The system no longer reports alerts for ignored vulnerabilities. |
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected assets at the same time. To manage a vulnerability for one affected asset, select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.2 Manage Windows system vulnerabilities

This topic describes how to manage Window system vulnerabilities.

**Background information**

Apsara Stack Security automatically checks whether the latest Microsoft updates are installed on your servers, and notifies you of the detected vulnerabilities. Apsara Stack Security also automatically detects and fixes major vulnerabilities on your servers.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Windows System** tab, view the detected Windows system vulnerabilities.

> **Note:** You can search for specific vulnerabilities by using the search and filter features.

5. Click a vulnerability. In the panel that appears, you can view details about the vulnerability
and the assets that are affected by the vulnerability.

> **Note:** You can find affected assets by using the search and filter features.

**Detail**: This tab displays the basic information about the vulnerability.
**Pending vulnerability**: This tab displays the servers that are affected by the
vulnerability.
6. Handle the vulnerability based on its impact. The following table describes the actions that
are used to fix vulnerabilities. Table 1 Actions to fix vulnerabilities

| Action | Description |
|---|---|
| Fix | Select this action to fix the vulnerability. The system caches an official Windows patch in the cloud. Your server can automatically download the patch for updates. |
| Ignore | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. |
| Restarted and Verified | If a vulnerability fix takes effect only after a server reboot, you must reboot the server after the status of the vulnerability changes to Fixed (To Be Restarted). After the reboot, click Restarted and Verified. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.3 Manage Web-CMS vulnerabilities

This topic describes how to manage Web-CMS vulnerabilities.

**Background information**

The Web-CMS vulnerability detection feature obtains information about the latest vulnerabilities and provides patches in the cloud. This helps you detect and fix vulnerabilities.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Web CMS** tab, view all vulnerabilities.

> **Note:** You can search for specific vulnerabilities by using the search and filter features.

5. Click a vulnerability. In the panel that appears, you can view details about the vulnerability
and the assets that are affected by the vulnerability.

> **Note:** You can find affected assets by using the search and filter features.

6. Handle the vulnerability based on its impact. The following table describes the actions that
are used to fix vulnerabilities. Table 1 Actions to fix vulnerabilities

| Action | Description |
|---|---|
| Fix | If you select this action, the system replaces the web files affected by the vulnerability on your server to fix the Web-CMS vulnerability. Note Before you fix the vulnerability, we recommend that you back up the web files affected by the vulnerability. For more information about the paths of the web files, click Details in the Actions column. |
| Ignore | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify the fix of a vulnerability, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |
| Roll Back | For vulnerabilities that have been fixed, click Roll Back to restore the web files that have been replaced. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.4 Manage urgent vulnerabilities

This topic describes how to manage urgent vulnerabilities.

**Background information**

Apsara Stack Security automatically detects vulnerabilities on servers, such as the unauthorized Redis access vulnerability and Struts S2-052 vulnerability, and generates vulnerability alerts. After you fix a vulnerability, you can also check whether the fix is successful.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. On the **Application(Urgent Vulnerability Included)** tab, view all vulnerabilities.
You can search for a specific vulnerability by using the search and filter features.
5. Click the name of a vulnerability. In the panel that appears, view the details in the following
sections: **Details**, **Suggestions**, and **Affected Assets**. You can find affected assets by using the search and filter features.
6. Handle the vulnerability based on its impact. The following table describes the actions that
are used to fix vulnerabilities. Follow the instructions to manually fix the vulnerabilities on the **Application(Urgent**
**Vulnerability Included)** tab.
Table 1 Actions to fix vulnerabilities

| Action | Description |
|---|---|
| Ignore | If you select this action to ignore a vulnerability, the system no longer reports alerts for the vulnerability. |
| Verify | Click Verify to verify the vulnerability fix. If you do not manually verify a fix, the system automatically verifies the fix within 48 hours after the vulnerability is fixed. |

You can manage a vulnerability for one or more affected assets at a time. To manage a vulnerability for one affected asset, find the asset and select an action from the **Actions** column of the asset. To manage a vulnerability for multiple affected assets, select the assets and select an action below the list of the affected assets.

##### 3.3.1.5 Configure vulnerability management policies

**policies**

You can enable or disable automatic detection for different types of vulnerabilities and enable vulnerability detection for specific servers. You can also set a time duration for which invalid vulnerabilities are retained and configure a vulnerability whitelist.

**Background information**

A vulnerability whitelist allows you to exclude vulnerabilities from the detection list. You can add multiple vulnerabilities in the vulnerability list to the whitelist. The system does not detect vulnerabilities that are added to the whitelist. You can manage the vulnerability whitelist on the vulnerability settings panel.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Vulnerabilities**.
4. In the upper-right corner, click **Settings** to configure vulnerability management policies.
Select a vulnerability type and enable or disable detection for vulnerabilities of this type. Click **Manage** next to a vulnerability type and specify the servers on which vulnerabilities of this type are detected. Select a time duration during which invalid vulnerabilities are retained. For example, you can select 7 days, 30 days, or 90 days.

> **Note:** If you do not take an action on a detected vulnerability, the system determines that the alert is invalid. The system deletes the vulnerability after the specified duration.

Select the vulnerability severities for scanning.
**High**: Vulnerabilities of this severity must be fixed as soon as possible.
**Medium**: Vulnerabilities of this severity can be fixed later.
**Low**: Vulnerabilities of this severity are less urgent, and can be fixed later.
Select vulnerabilities in the whitelist and click **Remove** to enable the system to detect these vulnerabilities and generate alerts for these vulnerabilities.

#### 3.3.2 Baseline check

##### 3.3.2.1 Baseline check overview

The baseline check feature automatically checks the security configurations on servers and provides detailed check results and suggestions for baseline reinforcement. After you enable the baseline check feature, Apsara Stack Security automatically checks for risks related to the operating systems, accounts, databases, passwords, and security compliance configurations of your servers, and provides reinforcement suggestions. For more information, see Baselines. By default, a full baseline check is automatically performed from 00:00 to 06:00 every day. You can create and manage scan policies for baseline checks. When you create or modify a policy, you can specify the baselines, interval, and time period, and select the servers to which you want to apply this policy. For more information, see Add a custom baseline check policy.

**Precautions**

By default, the following baselines are disabled. To check these baselines, make sure that these baselines do not affect your business and select them when you customize a scan policy. Baselines related to weak passwords for specific applications such as MySQL, PostgreSQL, and SQL Server

> **Note:** If these baselines are enabled, the system attempts to log on to servers with weak passwords. The logon attempts consume server resources and generate a large number of logon failure records.

Baselines related to China classified protection of cybersecurity Baselines related to the Center for Internet Security (CIS) standard

**Baselines**

| Category | Baseline |
|---|---|
| High risk exploit | High risk exploit - CouchDB unauthorized access high exploit risk High risk exploit - Docker unauthorized access high vulnerability risk High risk exploit - Elasticsearch unauthorized access high exploit vulnerability risk High risk exploit - Memcached unauthorized access high exploit vulnerability risk High risk exploit - Apache Tomcat AJP File Read/Inclusion Vulnerability High risk exploit - ZooKeeper unauthorized access high exploit vulnerability risk |
| CIS and China's Protection of Cybersecurity | Security baseline check against the Alibaba Cloud standard: Alibaba Cloud Standard-Aliyun Linux 2 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 6 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 7 Security Baseline Check Alibaba Cloud Standard - Debian Linux 8 Security Baseline Alibaba Cloud Standard - Redhat Linux 6 Security Baseline Check Alibaba Cloud Standard - Redhat Linux 7 Security Baseline Check Alibaba Cloud Standard - Ubuntu Security Baseline Check Alibaba Cloud Standard - Windows Server 2008 R2 Security Baseline Check Alibaba Cloud Standard - Windows 2012 R2 Security Baseline Alibaba Cloud Standard - Windows 2016/2019 R2 Security Baseline |
|   | Security baseline check against the CIS standard: Alibaba Cloud Aliyun Linux 2 CIS Benchmark CIS CentOS Linux 6 LTS Benchmark CIS CentOS Linux 7 LTS Benchmark CIS Debian Linux 8 Benchmark CIS Ubuntu Linux 14 LTS Benchmark CIS Ubuntu Linux 16/18 LTS Benchmark CIS Microsoft Windows Server 2008 R2 Benchmark CIS Microsoft Windows Server 2012 R2 Benchmark CIS Microsoft Windows Server 2016/2019 R2 Benchmark |

|   | Baseline check on compliance of China classified protection of cybersecurity level III: Aliyun Linux 2 Baseline for China classified protection of cybersecurity-Level III CentOS Linux 6 Baseline for China classified protection of cybersecurity-Level III CentOS Linux 7 Baseline for China classified protection of cybersecurity-Level III Debian Linux 8 Baseline for China classified protection of cybersecurity-Level III Redhat Linux 6 Baseline for China classified protection of cybersecurity-Level III Redhat Linux 7 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 10 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 11 Baseline for China classified protection of cybersecurity-Level III SUSE Linux 12 Baseline for China classified protection of cybersecurity-Level III Ubuntu 14 Baseline for China classified protection of cybersecurity-Level III Waiting for Level 3-Ubuntu 16/18 compliance regulations inspection China's Level 3 Protection of Cybersecurity - Windows Server 2008 R2 Compliance Baseline Check Windows 2012 R2 Baseline for China classified protection of cybersecurity-Level III Windows 2016/2019 R2 Baseline for China classified protection of cybersecurity-Level III |
|---|---|
| Best security practices | Alibaba Cloud Standard-Aliyun Linux 2 Security Baseline Check Alibaba Cloud Standard - Apache Security Baseline Check Alibaba Cloud Standard - CentOS Linux 6 Security Baseline Check Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check Alibaba Cloud Standard - Debian Linux 8 Security Baseline Alibaba Cloud Standard - IIS 8 Security Baseline Check Alibaba Cloud Standard - Memcached Security Baseline Check Alibaba Cloud Standard - MongoDB 3.x Security Baseline Check Alibaba Cloud Standard - Mysql Security Baseline Check Alibaba Cloud Standard - Nginx Security Baseline Check Alibaba Cloud Standard - Redhat Linux 6 Security Baseline Check Alibaba Cloud Standard - Redhat Linux 7 Security Baseline Check Alibaba Cloud Standard - Redis Security Baseline Check Alibaba Cloud Standard - Ubuntu Security Baseline Check Alibaba Cloud Standard - Windows Server 2008 R2 Security Baseline Check Alibaba Cloud Standard - Windows 2012 R2 Security Baseline Alibaba Cloud Standard - Windows 2016/2019 R2 Security Baseline Alibaba Cloud Standard-Apache Tomcat Security Baseline |

| Weak password | Weak Password-MongoDB Weak Password baseline(support version 2. X) Weak password - Ftp login weak password baseline Weak password - Linux system login weak password baseline Weak password - MongoDB login weak password baseline Weak password - SQL Server DB login weak password baseline Weak password - Mysql DB login weak password baseline Weak password - Mysql DB login weak password baseline(Windows version) Weak password - PostgreSQL DB login weak password baseline Weak password - Redis DB login weak password baseline Weak password - rsync login weak password baseline Weak password - svn login weak password baseline |
|---|---|

##### 3.3.2.2 Create baseline check policies

This topic describes how to create, modify, and delete baseline check policies. This topic also describes how to specify baseline check levels.

**Background information**

By default, the baseline check feature uses **default baseline check policies** to check the baseline risks of assets. You can also create custom baseline check policies based on your business requirements. For example, you can create a custom baseline check policy to check the compliance based on Multi-Level Protection Scheme (MLPS) level 2 in China.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Baseline Check**.
4. In the upper-right corner of the Baseline Check page, click **Manage Policies**. In the
**Manage Policies** panel, create, modify, or delete a custom baseline check policy. You can
also modify the default baseline check policy. In the upper-right corner of the panel, click **Add custom policy** to create a custom baseline check policy. Then, click **Ok**.

| Parameter | Description |
|---|---|
| Policy Name | The name of the policy. |

| Schedule | Specify the time interval for scheduled scan tasks to 1 day, Every 3 Day, Every 7 Day, or Every 30 Day. Then, select one of the following time ranges for scheduled scan tasks: 0:00 to 6:00, 6:00 to 12:00, 12:00 to 18:00, and 18:00 to 24:00. |
|---|---|
| Check Items | Select the baseline items that need to be checked. |
| Servers | Select the server groups to which you want to apply the baseline check policy. Note By default, newly purchased servers are classified into theUngrouped > Asset Group. To apply the policy to new servers, select Ungrouped. |

Click **Edit** or **Delete** next to a policy to modify or delete the policy.

> **Note:** You cannot restore a policy after you delete policy.

In the Manage Policies panel, you can find the **default baseline check** policy and click
**Edit** in the **Actions** column to change the server groups to which the policy is applied.

> **Note:** You cannot delete the default baseline check policy or modify the baseline items of the default baseline check policy. You can only change the server groups to which the default baseline check policy is applied.

In the lower part of the **Manage Policies** panel, specify the baseline check levels. Valid values: High, Medium, and Low.
5. Click **Ok**.

##### 3.3.2.3 View baseline check results and handle baseline risks

**baseline risks**

Apsara Stack Security Center provides details of baseline check results and suggestions on how to manage failed check items. This topic describes how to view baseline check results and manage failed check items in Apsara Stack Security Center. The check results include affected assets, checked items, and suggestions.

**View the summary of baseline check results**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Prevention** > **Baseline Check**.
4. In the upper part of the **Baseline Check** page, view the summary of baseline check
results. You can filter data by baseline check policy. You can select a baseline check policy from the **Select Policy** drop-down list to view the following information:
**Checked Servers**: The number of servers on which the baseline check runs. These
servers are specified in the selected baseline check policy.
**Check Items**: The number of **check items** specified in the selected baseline check
policy.
**Last Pass Rate**: The pass rate of the last baseline check.
If the number below **Last Pass Rate** is green, the pass rate of the checked servers is high. If the number is red, a large number of failed check items were detected on the checked servers. We recommend that you view the details of the check result and manage the failed check items.

**View all baselines**

1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, click **Baseline Check**.
4. Select **All** from the **Select Policy** drop-down list.
The **Baseline Check** page displays the details of all baselines, such as **Baseline**, **Checked**
**Item**, **Failed Items/Affected Servers**, **Category**, and **Last Check**.

> **Note:** You can also select a baseline check policy from the **Select Policy** drop-down list to view the baselines that are specified in the policy.

**View the details of a baseline**

1. Log on to Apsara Stack Security Center.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, click **Baseline Check**.
4. In the **Baseline** column, click a baseline to view the details of the baseline.
Baseline details include the affected assets and the numbers of **Passed Items** and **At-Risk**
**Items**.
5. Manage baseline risks on the baseline details page.
Find the asset that you want to manage and click **View** in the **Actions** column to open the **At-Risk Items** panel. Click **Verify** in the **Actions** column to check whether the baseline risks of an asset are managed. If the verification is passed, the number of **At-Risk Items** is reduced, and the status of the check items changes to **Passed**.

**View the details of a failed check item**

1. Find the baseline that you want to manage and click the baseline. In the panel that
appears, find the asset that you want to manage and click **View** in the **Actions** column to view failed check items. You can view the check items of the asset and the status of the check items. The status can be **Passed** or **Failed**.
2. Find a check item and click **Details** in the **Actions** column to view the description, result,
and suggestion for the check item.

> **Note:** We recommend that you follow the suggestions to manage check items whose status is **Failed** at the earliest opportunity, especially high-risk check items.

**Manage failed check items**

In the At-Risk Items panel, manage failed check items.

**Add check items to the whitelist**

If you want to disable alerts for a check item, click **Whitelist** to add the check item to the whitelist. Check items in the whitelist do not trigger alerts.

> **Note:** You can also select multiple check items and click **Whitelist** in the lower-left corner to add the check items to the whitelist at a time.

**Repair**

Server Guard allows you to fix only multiple baseline risks that are detected based on the Alibaba Cloud standards at a time. You can select multiple servers that have the same baseline risks.

> **Important:** Fixing baseline risks may be risky. Before you handle baseline risks, make sure that a backup is performed.

**Remove check items from the whitelist**

If you want to enable alerts for a check item in the whitelist, click **Remove** to remove the check item from the whitelist. You can remove one or more check items from the whitelist at a time. After you remove a check item from the whitelist, the check item triggers alerts.

**Verify the fix of a failed check item**

After you fix a check item, you can click Verify to check whether the check item is fixed. After you click Verify, the status of the check item changes to **Checking**. If you do not manually perform the verification, Apsara Stack Security automatically verifies the fix based on the detection interval specified in the policy. If the verification is passed, the **Status** of the check item changes to **Passed**.

#### 3.3.3 Risk exposure detection

The risk exposure detection feature automatically analyzes the exposure of your servers on the Internet. This helps you quickly detect abnormal exposure of your assets and applications on the Internet. The feature also provides suggestions on how to fix the detected vulnerabilities. This topic describes how to use the risk exposure detection feature.

**Statistics**

| Parameter | Description |
|---|---|
| Exposed Assets/Public IP Addresses | The total numbers of servers and IP addresses that are exposed on the Internet. |
| Gateways | The total number of gateway assets that are exposed on the Internet. The gateway assets include NAT gateways and Server Load Balancer (SLB) instances. You can click the number below Gateways to go to the Gateways panel. In the panel, you can view the gateway assets that are exposed on the Internet. |
| Exposed Ports | The total number of ports that are exposed on the Internet. You can click the number below Exposed Ports to go to the Exposed Ports panel. In the panel, you can view the ports that are exposed on the Internet. |
| Exposed Components | The total number of system components that run on your Elastic Compute Service (ECS) instances and are exposed on the Internet. The components include OpenSSL and OpenSSH. You can click the number below Exposed Components to go to the Exposed Components panel. In the panel, you can view the components that are exposed on the Internet. |
| Exploitable Vulnerabilities | The total number of vulnerabilities that are exposed on the Internet and can be exploited by attackers, and the numbers of high-risk, medium-risk, and low- risk vulnerabilities. You can click the number of high-risk, medium-risk, or low- risk vulnerabilities to go to the Vulnerabilities page. Vulnerabilities of different severities are marked in different colors: High-risk vulnerabilities: red. These vulnerabilities pose major threats to your assets. We recommend that you take note of these vulnerabilities and fix them at the earliest opportunity. Medium-risk vulnerabilities: orange. These vulnerabilities cause damage to your assets. We recommend that you fix the vulnerabilities at the earliest opportunity. Low-risk vulnerabilities: gray. These vulnerabilities are less harmful to your assets than high-risk and medium-risk vulnerabilities. You can fix low-risk vulnerabilities at your convenience. |

**View the exposure details of assets**

**Exposed assets**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Prevention** > **Risk Exposure Detection**.
4. On the **Asset Exposure** tab of the **Risk Exposure Detection** page, view the information
about exposed assets. Filter assets: Filter assets by vulnerability, asset group, or port. View the exposure details of an asset: Find the asset whose details you want to view and click **Exposure Details** in the **Actions** column. In the panel that appears, you can view the communication link topology between the asset and the Internet, and the details of the links. Export data of exposed assets: Click the icon in the upper-right corner of the exposed asset list to export and save the details of the exposed assets to your computer. The exported file is in the Excel format.

**Exposed applications**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Prevention** > **Risk Exposure Detection**.
4. On the **Application exposure** tab of the **Risk Exposure Detection** page, view the
information about exposed applications. Filter applications: Filter applications by specifying whether vulnerabilities exist or entering the service version or middleware version, or the service name or middleware name. View the exposure details of an application: Find the application whose details you want to view and click **Exposure Details** in the **Actions** column. In the panel that appears, you can view the exposure details of the application. Export data of an exposed application: Click the icon in the upper-right corner of the list of exposed applications to export and save the details of the exposed applications to your computer. The exported file is in the Excel format.

#### 3.3.4 Application protection

The application protection feature is developed based on the runtime application selfprotection (RASP) technology. This feature can detect attacks and provide protection during application runtime. To use the application protection feature, you do not need to change the application code. You need to only install the application protection agent on the servers that you want to protect. The feature can protect your applications against attacks that are launched by exploiting most unknown vulnerabilities.

**Step 1: Add applications for protection**

Before you can use the application protection feature, you must add an application and then enable the application protection feature for the server or container in which the application is deployed.

**Add an application**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **Configuration** tab of the **Application protection** page, click **New application**. In
the New application dialog box, enter the name and description of the application that you want to add, and click **OK**. After you add an application, the default policy takes effect for the application. The default protection mode is Monitor. You can click **Protection strategy** in the **Operation** column to view information about the default policy.
5. In the **Prompt** message, click **Cancel**.
You can also click **OK** to add the application. For more information, see Enable the application security feature for a server and Enable the application security feature for a container.
6. **Optional**. If you do not want to use the default policy, perform the following steps to modify
the protection policy: i. In the application list of the **Configuration** tab, find the application whose protection policy you want to modify and click **Protection strategy** in the **Operation** column. ii. In the **Protection strategy** panel, modify the policy and click **OK**.

| Configuratio n item | Description |
|---|---|
| Protection Mode | The protection mode for the application. Valid values: Monitor: monitors your application to detect attacks. The running of the application is not affected. If an attack is detected, an alert is generated. For this alert, Processing method is Monitor. Block: monitors and blocks attacks, and monitors high-risk operations that are performed on the application. If an attack is blocked, an alert is generated. For this alert, Processing method is Block. Disable: disables the application protection feature for the application. Attacks are not monitored or blocked. |
| Detection timeout | The maximum timeout period for attack detection. Valid values: 1 to 60000. Unit: milliseconds. Default value: 300. After the specified period elapses, the original business logic continues regardless of whether the detection logic is incomplete. We recommend that you use the default value. |
| SOURCE IP judgment method | The method that is used to obtain source IP addresses. If you select Default, the system obtains source IP addresses based on the values of standard request headers that record source IP addresses. Standard request headers that record source IP addresses include X-Real-IP, True-Client-IP, and X-Forwarded-For. If you select Taken from the value that defines the header, the system preferentially obtains source IP addresses based on the values of custom headers. If the system cannot obtain source IP addresses based on the values of custom headers, the value Default is used. |
| Detection type | The types of attacks that you want to detect. We recommend that you retain the default settings. To retain the default settings, select All Selection. For more information about the different types of attacks, see Attack types. |

**Enable the application security feature for a server**

1. In the application list of the **Configuration** tab, find the required application and click
**Access management** in the **Operation** column.
2. In the panel, follow the on-screen instructions on the **Host Access Guide** tab to install the
RASP agent. Then, restart the application. You can also click **Point-and-click Push** to push and install the RASP agent on the server on which the application resides. Before you restart an application, you must complete related deployment based on the runtime environment of the application. The following table describes the parameter settings for deployment in different runtime environments. When you configure the parameters, replace `{appId}` with the application ID that is displayed on the **Host Access Guide** tab.

| Runtime | Parameter setting |
|---|---|

| Tomcat on Linux |   | Add the following configurations to the first line of the {TOMCAT HOME}/bin/setenv.sh file: _ JAVA OPTS="$JAVA OPTS - _ _ javaagent:/usr/local/aegis/rasp/apps/{appId}/rasp.jar" If your Tomcat version does not support the setenv.sh configuration file, open the {TOMCAT HOME}/bin/catalina.sh file _ and append the preceding configurations to JAVA OPTS. _ |   |   |
|---|---|---|---|---|
| Tomcat on Windows |   | Add the following configurations below :setArgs in the {TOMCAT HOME}/bin/catalina.bat file: _ 64-bit Windows: set JAVA OPTS=%JAVA OPTS% "-javaagent:C:\Program _ _ Files (x86)\Alibaba\Aegis\rasp\apps\ {appId}\rasp.jar" 32-bit Windows: set JAVA OPTS=%JAVA OPTS% "-javaagent:C:\Program _ _ Files\Alibaba\Aegis\rasp\apps\{appId}\rasp.jar" |   |   |
| Jetty |   | Add the following configurations to the {JETTY HOME}/start.ini _ configuration file: --exec - javaagent:/usr/local/aegis/rasp/apps/{appId}/rasp.jar |   |   |
| Spring Boot |   | Add the -javaagent parameter to the startup command for the Spring Boot process: java - javaagent:/usr/local/aegis/rasp/apps/{appId}/rasp.jar For example, the original startup command of the Spring Boot process is java -jar app.jar . Before you restart your application to install the RASP agent, you must change the startup command to java - |   |   |
|   |   |   | java - |   |
|   |   | javaagent:/usr/local/aegis/rasp/apps/{appId}/rasp.jar - |   |   |
|   |   | jar app.jar |   |   |

If you no longer want the application protection feature to protect the application, you can click the **Uninstallation guide** tab and follow the on-screen instructions on the tab to uninstall the RASP agent.

**Enable the application security feature for a container**

1. In the application list of the **Configuration** tab, find the required application and click
**Access management** in the **Operation** column.
2. In the panel, follow the on-screen instructions on the **Add Container** tab to install the RASP
agent. Then, restart the container in which the application resides. You can also click **Point-and-click Push** to push and install the RASP agent for the container in which the application resides. Before you restart a container, you must complete related deployment based on the runtime environment of the container. The following table describes the parameter settings for deployment in different runtime environments. When you configure the parameters, replace `{manager.key}` with the value of `Dmanager.key` that is displayed on the Add Container tab.

| Runtime |   |   | Parameter setting |   |   |   |   |
|---|---|---|---|---|---|---|---|
| SpringBoot |   |   | To install the RASP agent when an image is being packaged, modify the startup parameters in the Dockerfile and change the startup command for your application from CMD ["java","- jar","/app.jar"] to CMD ["java","- |   |   |   |   |
|   |   |   |   |   |   | CMD ["java","- |   |
|   |   |   | jar","/app.jar"] | CMD ["java","- |   |   |   |
|   |   |   | {manager.key}","-jar","/app.jar"] |   |   |   |   |
| Tomcat |   |   | To install the RASP agent when an image is being packaged, add the following configurations to the Dockerfile: ENV JAVA OPTS="-javaagent:/rasp/rasp.jar - _ Dmanager.key={manager.key}" To install the RASP agent when a container is being started, add the following configurations to the startup command: docker --env JAVA OPTS="-javaagent:/rasp/rasp.jar - _ Dmanager.key={manager.key}" For example, the original startup command of a container is docker -itd --name=test -P image name . Before you restart the container to install the RASP agent, you must change the startup command to docker -itd --env |   |   |   |   |
|   |   |   |   |   | docker -itd --env |   |   |
|   |   |   | JAVA OPTS="-javaagent:/rasp/rasp.jar -Dmanager.key= _ |   |   |   |   |
|   |   |   | {manager.key}" --name=test -P image name |   |   |   |   |

| Weblogic |   | To install the RASP agent when an image is being packaged, add the following configurations to the Dockerfile: ENV JAVA OPTIONS="-javaagent:/rasp/rasp.jar - _ Dmanager.key={manager.key}" To install the RASP agent when a container is being started, add the following configurations to the startup command: docker --env JAVA OPTIONS="- _ javaagent:/rasp/rasp.jar -Dmanager.key= {manager.key}" For example, the original startup command of a container is docker -itd --name=test -P image name . Before you restart the container to install the RASP agent, you must change the startup command to docker -itd --env |   |
|---|---|---|---|
|   |   |   | docker -itd --env |
|   |   | JAVA OPTIONS="-javaagent:/rasp/rasp.jar - _ |   |
|   |   | Dmanager.key={manager.key}" --name=test -P image |   |
|   |   | name |   |

If you no longer want the application protection feature to protect the container, you can click the **Uninstallation guide** tab and follow the on-screen instructions on the tab to uninstall the RASP agent.

**Step 2: View alert events**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **Alert** tab of the **Application protection** page, view the information about alert
events. On the **Alert** tab, the doughnut charts display the behavior of applications after the application protection feature is enabled for the applications and the statistics about attacks on the applications. The list in the lower part of the page displays the details of each attack. The details include the type, URL, behavior data, and handling method of an attack. View statistics about application behavior The **Applied Behavior Statistics** section displays the application behavior that is monitored by the application protection feature and the behavior types. The behavior types include normal behavior and attacks. View attack statistics The **Attack statistics** section displays the attacks that are detected by the application protection feature and the types of attacks. View attack details The list in the lower part of the Application protection page displays the details of each attack. You can view the time, type, URL, behavior data, and handling method of each attack in the list. You can also view the details of an attack. To view the details of an attack, find the attack and click **View** in the **Operation** column. In the **Details** panel, view the details, including vulnerability details, request details, and server details.

**Configure a whitelist rule**

You can configure a whitelist rule to allow requests from specific IP addresses. If requests match a whitelist rule that you specify, Server Guard does not block or generate alerts on the requests.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Prevention** > **Application Protection**.
4. On the **White list** tab of the **Application protection** page, click **Configure a whitelist**.
In the **Configure a whitelist** panel, perform the following steps to configure a whitelist rule and select applications to which you want the rule to take effect. i. In the **Rule Name** field, enter a name for the rule. ii. In the **Source IP** section, enter the source IP addresses that you want to add to the whitelist. You can enter up to 100 IP addresses or CIDR blocks.

> **Important:** If you enter 0.0.0.0/0, Server Guard allows requests from all IP addresses. Proceed with caution.

iii. In the **The request path** section, configure the path that is used to match requests from the IP addresses in the whitelist. You can select one of the following match methods for the path:
**Prefix Match**: If requests are sent from IP addresses in the whitelist and the prefixes of
the request paths match a specified prefix, the requests are allowed. Example:

```
 http://39.104.XX.XX:8080/ .
```

**Suffix Match**: If requests are sent from IP addresses in the whitelist and the suffixes of
the request paths match a specified suffix, the requests are allowed. Example:

```
 /Vulns/file/io/read .
```

> **Note:** When Server Guard matches a request path against the specified condition, Server Guard ignores the content in the query string. For example, the request path is
> http://127.0.XX.XX:8088/Vulns/file/io/read?path=/etc/passwd . Server Guard ignores the question mark (?) and the content that follows the question mark (?). In this example, ?path=/etc/passwd is ignored.

iv. In the **Detection type** section, select the detection type and click **Next**. v. Select the applications for which you want the whitelist rule to take effect and click **OK**. After the configuration is complete, the whitelist rule takes effect on all online application instances of the selected applications.

**Attack types**

The following table describes the types of attacks that the application protection feature can detect and the solutions to defend against each type of attack.

| Attack type | Description | Protection suggestion |
|---|---|---|
| JNI injection | Java Native Interface (JNI) injection is a common method to bypass the RASP technology. After an attacker obtains the permissions to execute code, the attacker can use JNI functions to call external malicious dynamic-link libraries. This allows the attacker to bypass the security protection at the Java layer and conceal specific malicious behavior. | A code execution vulnerability may exist on your server. Check the location of the vulnerability and limit the permissions to execute code. |
| SQL injection | An SQL injection attack inserts SQL statements into the query strings of web requests or web forms and induces the server to execute the SQL statements. An attacker can obtain the data on websites on which security vulnerabilities exist by inserting SQL statements into web forms. | SQL injection is caused by concatenating SQL statements. Precompile input parameters or use whitelists and blacklists to limit concatenated parameters. |
| XXE | XXE injection is short for XML external entity injection. If an XML file references an external entity, an attacker can construct malicious content to cause arbitrary file reads, command execution, and internal network attacks. | Check whether your application needs to load external entities when XML files are parsed. If your application does not need to load external entities, disable external entities in the XML parsing configuration. |
| Malicious DNS query | An attacker can use multiple methods to exploit malicious Domain Name System (DNS) queries. An attacker can use the DNS protocol to obtain sensitive information from internal networks. The attacker can also use the DNS protocol to check whether an internal network system has vulnerabilities such as Server-Side Request Forgery (SSRF) and Java Naming and Directory Interface (JNDI) injection. | Malicious DNS queries are caused by server requests for user-controlled parameters. Check parameter settings and configure whitelists. |
| Malicious reflection call | The self-protection module of RASP prohibits attackers from using reflection to modify RASP data during runtime. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| SSRF | SSRF is a web vulnerability that allows an attacker to attack the internal system of a website by inducing a server-side application to initiate HTTP requests. | SSRF is caused by server requests for input parameters. Check parameter settings and configure whitelists. |

| Malicious file read and write | Java provides the RandomAccessFile class for file read and write operations. If you use this class to read and write files but do not restrict the file path or file content, an attacker may read sensitive system files or upload trojan files. | Check whether file read or write operations are normal. If an exception occurs, check the function code and configure blacklists. |
|---|---|---|
| Malicious file upload | For the file upload feature provided by a website, if the types of files are not restricted, an attacker may obtain higher permissions on the server by uploading trojan files. This causes serious harm. | Restrict the types of files that can be uploaded and prohibit the upload of files that have the execute permissions, such as Jakarta Server Pages (JSP) files. |
| Command execution | A command execution vulnerability allows an attacker to execute arbitrary system commands on a server. | In most cases, remote command execution is caused by webshells or the risky code of a server. Check the location in which commands are executed. If command execution is caused by webshells, delete the webshells at the earliest opportunity. If commands are executed to implement normal features on a server, configure whitelists to limit the commands that can be executed. |
| Directory traversal | The directories of a website may be arbitrarily browsed due to the configuration defects of the website. This results in the disclosure of privacy information. An attacker can use the disclosed information to attack the website. | Check whether directory traversal operations are normal. If an exception occurs, check the function code and configure blacklists to restrict related commands, such as "./" and "../". |
| In-memory webshell injection | Memory horse is an emerging trojan horse technique. An attacker can inject trojans into memory by using special technical methods, which can bypass the detection of Web Application Firewall (WAF) and host defense. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| Arbitrary file read | For the file download and read feature provided by a website, if files are read and downloaded by using an absolute path or a directory traversal character and file paths are not restricted, an attacker can exploit this vulnerability to obtain sensitive information and attack the server. | Check whether file read operations are normal. If an exception occurs, check the function code and configure blacklists to restrict input parameters, such as "./" and "../". |

| Weak database password | If a database password is weak, an attacker can initiate brute-force attacks to obtain the password. Then, the attacker can steal data from the database and obtain system permissions. | Use a more complex password. |
|---|---|---|
| Thread injection | Thread injection is a common method that is used to bypass the RASP technology. If an attacker obtains the permissions to execute code, the attacker can create a thread that causes RASP to lose the context of the runtime environment. In this case, the defense capability of RASP is compromised. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| Malicious Attach API | The Attach API is a Java technology that can be used to dynamically modify the bytecode of running applications. An attacker can use the technology to inject agent-type in- memory webshells. This method is highly deceptive. | Your server may have a code execution vulnerability. Check the location of the vulnerability and limit the permissions to execute code. |
| JNDI injection | If an application initiates a JNDI query but the query URL is controlled by an attacker, the attacker can induce the server on which the application runs to query malicious links and load malicious classes. This results in arbitrary code execution on the server. | If this vulnerability is caused by third-party components, you must upgrade the components at the earliest opportunity. If this vulnerability is caused by self- written code for JNDI queries, you must restrict the query URLs to prohibit queries over insecure protocols. |
| Usage of insecure protocols | If a server accesses a URL that is user- controllable and the URL protocol is not restricted on your application, an attacker can read sensitive files on the server over insecure protocols such as File and NetDoc. | Restrict URL protocols. |
| Deserialization attack | Java deserialization is the process of restoring a sequence of bytes into a Java object. If the Java object contains high-risk code, an attacker can control the member variables of the Java object to initiate attacks during the deserialization process. | Upgrade the components on which vulnerabilities are detected at the earliest opportunity. If no official component versions in which the vulnerabilities are fixed are released, temporarily disable deserialization. |

| Arbitrary file deletion | For the file deletion feature provided by a website, if files are read and downloaded by using an absolute path or a directory traversal character and file paths are not restricted, an attacker can exploit this vulnerability to obtain sensitive information and attack the server. | Check whether file delete operations are normal. If an exception occurs, check the function code and configure blacklists to restrict input parameters, such as "./" and "../". |
|---|---|---|
| Expression language (EL) injection | Expressions provide various features, such as data query and processing during runtime. Multiple expressions also provide features that require advanced permissions such as function calls. If the features are not restricted, attackers can modify the content of expressions and execute arbitrary code. | Strictly restrict the content of expressions and disable Java function calls. If this vulnerability is caused by third-party components, upgrade the components at the earliest opportunity. |
| Engine injection | Java provides various third-party JavaScript engines such as Rhino and Nashorn, and template engines such as Apache Velocity and FreeMarker. In most cases, the engines provide features that require advanced permissions such as function calls. If the features are not restricted, attackers can modify the content that is executed by the engines and execute arbitrary code. | Strictly restrict the content imported to the engines and disable Java function calls. If this vulnerability is caused by third-party components, upgrade the components at the earliest opportunity. |
| Malicious beans binding | Some Java frameworks support bean property binding when applications are running. If the types of bean properties that can be bound are not restricted, attackers can modify the values of sensitive bean properties to disrupt the running of applications or execute arbitrary code. | Restrict the types of bean properties that can be bound to prevent the values of bean properties such as class and class loaders from being changed. If this vulnerability is caused by third- party components, upgrade the components at the earliest opportunity. |
| Malicious class loading | Zero-day vulnerabilities and webshells depend on the loading of malicious classes. After malicious classes are loaded, attackers can initialize malicious classes, obtain the permissions to execute code, and perform malicious operations. | If malicious classes are loaded by using webshells, delete the webshells at the earliest opportunity. If malicious classes are loaded due to framework vulnerabilities, upgrade the frameworks at the earliest opportunity. |

| JSTL file inclusion | The JavaServer Pages Standard Tag Library (JSTL) is a set of JavaServer Pages (JSP) tags, which encapsulates the common core features of JSP applications. If a user-controllable parameter is directly concatenated in JSTL without any restrictions on the parameter, attackers can construct a special script that causes arbitrary file reads and SSRF attacks. | We recommend that you do not directly concatenate user-controllable parameters into JSTL. If you need to directly concatenate user-controllable parameters into JSTL, you must implement strict whitelist control on the content of the parameters. |
|---|---|---|

### 3.4 Intrusion prevention

#### 3.4.1 Virus detection and removal

Server Guard provides the anti-virus feature. This feature allows you to configure custom settings for virus and webshell detection.

**Virus detection and removal**

The anti-virus feature can automatically quarantine common Internet viruses, such as common trojans, ransomware, mining programs, and DDoS trojans. Apsara Stack Security experts check and verify all the automatically quarantined viruses to ensure a minimum false positive rate. If the virus blocking feature is disabled, Server Guard generates alerts when viruses are detected. You must manually manage detected viruses in Apsara Stack Security Center. We recommend that you enable the virus blocking feature to improve the security of your servers.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Defense** > **Virus Defense**.
4. On the **Anti-virus** tab, click **Scan**.
5. In the dialog box that appears, select the servers that you want to scan.
6. Click **Scan**.
7. On the **Virus Defense** page, click the **Real-time protection** tab and enable the virus
blocking feature. After the virus blocking feature is enabled, Server Guard automatically quarantines common viruses that are detected. Quarantined viruses are listed on the Security Alerts page. To filter quarantined viruses, you can select the **Precision defense** type.

**Webshell detection and removal**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Defense** > **Virus Defense**.
4. Specify servers for webshell detection.
i. In the **Webshell Detection** section, click **Manage**. ii. Select the servers for which you want to enable webshell detection. iii. Click **OK**.

#### 3.4.2 Website tamper-proofing

##### 3.4.2.1 Overview

Tamper protection monitors website directories in real time, restores modified files or directories, and protects websites from trojans, hidden links, and uploads of violent and illicit content.

**Background information**

To make illegal profits or conduct business attacks, attackers exploit vulnerabilities in websites to insert illegal hidden links and tamper with the websites. Defaced web pages affect normal user access and may lead to serious economic losses, damaged brand reputation, or political risks. Tamper protection allows you to add Linux and Windows processes to the whitelist and update protected files in real time.

**How tamper protection works**

The Security Center agent automatically collects the list of processes that attempt to modify files in the protected directories of the protected servers. It identifies unusual processes and file changes in real time and blocks unusual processes. The alert list is displayed on the Tamper Protection page. You can view unusual file changes, the corresponding processes, and the number of attempts made by each process in the alert list. If a file is modified by a trusted process, you can add the process to the whitelist. After the process is added to the whitelist, tamper protection no longer blocks the process. In scenarios where the content of websites, such as news and education websites, is frequently modified, the whitelist saves you the effort of frequently enabling and disabling tamper protection.

**Versions of operating systems and kernels supported by**

**tamper protection**

| OS | Supported operating system version | Supported kernel version |
|---|---|---|
| Windows | Windows Server 2008 and later | All versions |
| CentOS | 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, and 7.6 | 2.6.32-x 3.10.0-x |

| Ubuntu | 14, 16, and 18 | 3.13.0-32-generic 3.13.0-86-generic 4.4.0-62-generic 4.4.0-63-generic 4.4.0-93-generic 4.4.0-151-generic 4.4.0-117-generic 4.15.0-23-generic 4.15.0-42-generic 4.15.0-45-generic 4.15.0-52-generic |
|---|---|---|

> **Note:** The preceding table lists kernel versions supported by tamper protection. Servers that use an unsupported kernel version cannot use tamper protection. Make sure that your server uses a supported kernel version. If a kernel version is not supported, you must upgrade it to a supported version. Otherwise, you cannot add processes to the whitelist.
> Before you upgrade the server kernel, back up your asset data.

##### 3.4.2.2 Configure tamper proofing

Server Guard allows you to configure tamper proofing for web pages.

**Limits**

You can add up to 10 directories that you want to protect for each server. If you want to add directories that are on a Windows server, the directories must meet the following requirements: The size of each directory does not exceed 20 GB. Each directory contains no more than 2,000 folders. The number of directory levels does not exceed 20. The size of each file does not exceed 3 MB. If you want to add directories that are on a Linux server, the directories must meet the following requirements: The size of each directory does not exceed 20 GB. Each directory contains no more than 3,000 folders. The number of directory levels does not exceed 20. The size of each file does not exceed 3 MB. Before you add a directory for protection, make sure that the directory meets the preceding requirements. We recommend that you exclude file formats that do not require protection, such as LOG, PNG, JPG, MP4, AVI, and MP3. Separate multiple file formats with semicolons (;).

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Security** > **Server Security** > **Server Guard**.
You can select an organization, a resource set, and a region in the top navigation bar. You can select a resource set that belongs to a level-2 organization or a specific user.
3. In the left-side navigation pane, choose **Defense** > **Tamper Proofing**.
4. On the **Tamper Proofing** page, click **Add Servers for Protection**.
5. In the **Add Servers for Protection** panel, select a server that you want to protect.
6. Click **Next** to go to the **Add Directory** step.
7. In the **Add Directory** step, configure the parameters.
Select a protection mode. The settings of other parameters vary based on the protection mode. You can select **Whitelist Mode** or **Blacklist Mode**. In whitelist mode, tamper proofing is enabled for the specified directories and file formats. In blacklist mode, tamper proofing is enabled for the subdirectories, file formats, and files that are not specified in the protected directory. By default, Whitelist Mode is selected. The following table describes the parameters that you must configure when you select Whitelist Mode.

| Parameter | Description |
|---|---|
| Protected Directory | Enter the directory that you want to protect. Note Servers that run Linux or Windows operating systems use different path formats. Enter a valid directory path based on the type of your operating system. |
| Protected File Formats | Select file formats that you want to protect from the drop-down list, such as js, html, xml, and jpg. |
| Local Backup Directory | The default directory in which backup files of the protected directory are stored. By default, Apsara Stack Security assigns /usr/local/aegis/bak as the backup directory for Linux servers and C:\Program Files (x86)\Alibaba\Aegis\bak as the backup directory for Windows servers. You can change the default directory based on your business requirements. |

The following table describes the parameters that you must configure when you select Blacklist Mode.

| Parameter | Description |
|---|---|
| Protected Directory | Enter the directory that you want to protect. |
| Excluded Sub- Directories | Enter the subdirectories that do not require tamper proofing. Click Add Sub-Directory to add more subdirectories. Apsara Stack Security Center does not provide tamper proofing for files in the excluded subdirectories. |
| Excluded File Formats | Select the file formats that do not require tamper proofing from the drop-down list, such as log, txt, and ldb. Apsara Stack Security Center does not provide tamper proofing for files in the excluded formats. |
| Excluded Files | Enter the path of the file that do not require tamper proofing. Click Add File to add more files. Apsara Stack Security Center does not provide tamper proofing for the excluded files. |

| Local Backup Directory | The default directory in which backup files of the protected directory are stored. By default, Apsara Stack Security Center assigns /usr/local/aegis/bak as the backup directory for Linux servers and C:\Program Files (x86)\Alibaba\Aegis\bak as the backup directory for Windows servers. You can change the default directory based on your business requirements. |
|---|---|

8. Click **Enable Protection**.
After you add the server for protection, the server is displayed on the Management tab of the **Tamper Proofing** page.

> **Note:** By default, tamper proofing is **disabled** for the server. To enable tamper proofing for the server, you must **turn on** the switch in the Protection column on the **Tamper** **Proofing** page.

9. On the **Tamper Proofing** page, click the **Management** tab, find the server that you
added, and then turn on the switch in the **Protection** column to enable protection for the server.

> **Note:** By default, tamper proofing is **disabled** for the server. To enable tamper proofing for the server, you must turn on the switch in the Protection column on the **Tamper** **Proofing** page.

After tamper proofing is enabled, the status of the server changes to **Running**.

> **Note:** If the status of a server is **Exception**, move the pointer over **Exception** in the Status column to view the cause and click **Retry** to re-enable tamper proofing.

**What to do next**

After you enable tamper proofing for a server, you can go to the **Security Alerts** page and select Webpage Tampering from the alert type drop-down list to view the alerts that are generated when tampering events are detected.

> **Note:** Tamper protection does not take effect immediately after you configure the protected directory, and you can still write files to the directory. In this case, you must go to the **Management** page, disable **Protection** for the server where the directory is located, and then enable **Protection** again.

**Handling suggestions for abnormal protection states**

| State | Description | Suggestion |
|---|---|---|

| erver Guard Advanced Edition U er Guide·Server Guard |   | Alibaba Cloud Security-Server G ard Advanced Editio |
|---|---|---|

| Starting | Tamper proofing is being initialized. | The first time you enable tamper proofing for a server, the protection status is Initializing. Wait until tamper proofing is enabled. |
|---|---|---|
| Running | Tamper proofing is enabled and running as expected. | None. |
| Exception | An error occurred when tamper proofing is enabled. | Move the pointer over Exception in the Status column to view the cause of the exception and click Retry. |
| Not Initialized | Tamper proofing is disabled. | Turn on the switch in the Protection column to enable tamper proofing. |

##### 3.4.2.3 View protection status

This topic describes how to view the status of web tamper proofing for your assets.

**Background information**

The web tamper proofing feature monitors changes to the files in website directories in real time and blocks suspicious file changes. To view the status and details of the web tamper proofing feature, you must log on to Apsara Stack Security Center and choose **Server**
**Security > Server Guard > Defense > Tamper Proofing**. The following information is
displayed: Tamper proofing overview You can view the numbers of files that are changed on the current day and in the last 15 days, the number of protected servers, and the number of protected directories. File type distribution Protected file formats include TXT, PNG, MSI, and ZIP. You can also add additional formats for protection based on your business requirements.

> **Note:** All file formats can be added for protection.

Top five file changes This section shows the names and paths of the top five files with the most number of changes in the last 15 days in descending order. Tamper proofing alerts This section displays the alerts that are generated for suspicious file changes that are blocked for your assets. You can view details of the alerts, including the severity, alert name, affected assets, paths of files with suspicious changes, and protection status.

> **Note:** If an alert is reported more than 100 times, we recommend that you handle the alert at the earliest opportunity.
> The severity level of alerts is **Medium**.
> The status of alerts is **Defended**. The alerts are triggered when web tamper proofing intercepts suspicious processes that modify files without authorization.

#### 3.4.3 Application whitelist

The application whitelist feature prevents unauthorized programs from running on your servers and provides a trusted running environment for your servers. This topic describes how to use the application whitelist feature.

**Create an application whitelist policy**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Policies** tab of the **Application Whitelist** page, click **Create Policy**.
5. In the**Create Application Whitelist** panel, configure an application whitelist policy and
click **Create**.

| Parameter | Description |
|---|---|
| Policy Name | The name of the application whitelist policy that you want to create. |
| Policy Mode | The mode of the policy. Valid values: Alert Mode and Observation Mode. |
| Policy Content | The content of the policy. You can click Settings next to each content item to configure the policy in the panel that appears. |
| Select an asset | The assets on which the policy takes effect. |

In the application whitelist policy list, you can perform the following operations: Modify a policy: Find the policy that you want to modify and click **Edit** in the **Actions** column. Enable or disable a policy: Select the policy that you want to enable or disable and click
**Enable all or Disable all** below the policy list.
Delete a policy: Select the policy that you want to delete and click **Delete** below the policy list.

**View the servers on which the application whitelist policy takes**

**effect**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Application Whitelist**page, click the **Servers**tab and view the servers on which
the policy takes effect. You can filter servers by policy status, policy mode, and asset status. You can also filter servers by server group and protection status. In the server list, you can perform the following operations: View the policy details of a server: Find the server that you want to view and click
**Details**in the**Actions**column.
Enable or disable the policy for a server: Select the server for which you want to enable or disable the policy and click**Enable Policy or Disable Policy** below the server list. Remove the policy: Select the server from which you want to remove the policy and choose**More Operations**>**Detach Policy**below the server list.

**Create a collection task**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Application Whitelist** page, click the **Knowledge Bases** tab and then click the
**Process Collection** tab.
5. On the**Process Collection**tab, click**Create Collection Task**.
6. In the**Create Process Collection Task**panel, configure Task Name, Observation End
Time, and Scan Assets, and click**OK**. You can re-scan assets and view task details in the collection task list.

**Create a custom process group**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Application Whitelists**.
4. On the **Application Whitelist**page, click the**Knowledge Bases**tab and then click the
**Custom Process Group** tab.
5. On the**Custom Process Group**tab, click**Create Custom Process Group**.
6. In the**Create Custom Process Group** dialog box, enter a process group name and click
**Create**.
After you create the custom process group, you can change the name of the process group, delete the process group, or add an MD5 hash value to the process group.

#### 3.4.4 Attack analysis

This topic describes the statistics that are provided by the attack analysis feature. The statistics include the total number of attacks, distribution of attack types, top 5 attack sources, top 5 attacked assets, and the attack list.

**Background information**

After Server Guard detects basic attacks, Server Guard blocks the attacks. The attack statistics are displayed on the **Attack Analysis** page. You do not need to handle the attacks. If high-risk attacks are detected, you can use the attack analysis feature to identify the source addresses of the attacks and take preventive measures We recommend that you deploy firewalls and adopt business-specific security measures to develop a more refined and precise defense system. On the **Attack Analysis** page, you can specify a time range to view attack details. You can view the attack analysis statistics of the current day, last 7 days, or last 15 days. You can also configure a custom **time range** to view the statistics. You can view the following details of attacks on your assets: Attacks: the total number of attacks detected in your assets within the specified time range. Attack Type Distribution: the attack types and the number of attacks for each type. Top 5 Attack Sources: the top 5 IP addresses from which the most attacks are launched. Top 5 Attacked Assets: the top 5 assets that encountered the most attacks. Attack list: the details of all attacks, including the attack time, source IP address, attacked asset, attack type, and attack status.

**Attacks**

In the **Attacks** section, a graph displays the attack trend within the specified time range. You can view the peak and valley values in the graph. You can move the pointer over the graph to view the attack date, the attack time, and the number of attacks. image

**Attack Type Distribution**

In the **Attack Type Distribution** section, you can view the attack types and the number of attacks for each type. image

**Top 5 Attack Sources**

In the **Top 5 Attack Sources** section, you can view the top 5 IP addresses from which attacks are most launched and the number of attacks that are initiated from each IP address. image

**Top 5 Attacked Assets**

In the **Top 5 Attacked Assets** section, you can view the public IP addresses of the top 5 assets that encountered the most attacks and the number of attacks on each asset. image

**Attack list**

In the attack list, you can view the details of each attack, including the attack time, source IP address, attacked asset, attack type, attack method, and attack status. image You can perform the following operations on attacks in the attack list: Search for an attack To search for an attack and view the details of the attack, specify search conditions above the attack list. Search conditions include the attack type, attacked asset, and source IP address. View the details of an attacked asset To view the details of an attacked asset, move the pointer over the name of the attacked asset in the **Attacked Asset** column. Export the attack list To export and save the attack list to your computer, click the icon in the upper-left corner of the attack list. The exported file is in the Excel format.

#### 3.4.5 Security alert

##### 3.4.5.1 Overview

If Server Guard detects sensitive file tampering operations, webshells, unusual logons, suspicious processes, and malicious processes, Server Guard generates alerts. You can monitor the security status of your assets based on the alerts and handle potential threats at the earliest opportunity. Apsara Stack Security Center provides statistics about alerts. This helps you understand the overall protection situation. You can view the statistics about alerts on the **Security Alerts** page of Apsara Stack Security Center.

**Alerts**

The following table describes the alerts.

| Alert name | Description |
|---|---|
| Unusual Logon | Server Guard detects unusual logons to your servers. You can configure approved logon IP addresses, time ranges, and accounts. Logons from unapproved IP addresses, accounts, or time ranges trigger alerts. You can manually add approved logon locations or configure the system to automatically update approved logon locations. You can also specify the assets on which alerts are triggered when unusual logon locations are detected. Server Guard can detect the following suspicious activities: Logons to Elastic Compute Service (ECS) instances from unapproved IP addresses Logons to an ECS instance from an unapproved location Suspicious command sequence executed after ECS logons over SSH ECS instance compromised due to brute-force attacks on SSH |
| Application Whitelist | You can create a whitelist policy for applications on servers that require reinforced protection. If the suspicious or malicious processes that are identified by the policy are not added to the whitelist, Server Guard generates alerts. |
| Webshell | Server Guard uses engines developed by Alibaba Cloud to scan common webshell files. Server Guard supports scheduled scan tasks, provides real-time protection, and quarantines webshell files. Server Guard scans an entire web directory early in the morning on a daily basis. If a file in the web directory changes, Server Guard immediately scans for webshells. You can specify the assets on which Server Guard scans for webshells. You can quarantine, restore, or ignore the detected trojan files. |

| Unusual Network Connection | Server Guard detects unusual network connections and disconnections. |
|---|---|
| Precise defense | Server Guard automatically blocks common Internet viruses, such as ransomware, DDoS trojans, mining and trojan programs, malicious programs, webshells, and computer worms. |
| Suspicious Account | Server Guard detects unapproved accounts that attempt to log on to your assets. |
| Persistence | Server Guard detects suspicious scheduled tasks on servers. If persistent threats against the servers are detected, Server Guard generates alerts. |
| Suspicious Process | Server Guard detects suspicious processes. |
| Malware Software | The threat detection model detects malware that is being executed on your server. |
| Sensitive File Tampering | Server Guard checks whether the sensitive files on your servers are tampered with. The sensitive files include pre-loaded configuration files in the shared libraries of Linux. |
| Malicious scripts | Server Guard detects whether the system services of your assets are attacked or modified by malicious scripts. If potential script attacks are detected, Server Guard generates alerts. Malicious scripts are classified into file-based scripts and fileless scripts. After an attacker gains control over a server, the attacker uses scripts for additional attacks. For example, the attacker may insert mining programs and webshells, and add administrator accounts to your system. Programming languages of malicious scripts include Bash, Python, Perl, PowerShell, Batch, and VBScript. |
| Exploit | The threat detection model detects exploits on your server. An exploit takes advantage of known vulnerabilities in operating systems and applications to escalate privileges, implement escapes, and execute arbitrary code. |

##### 3.4.5.2 View and handle alert events

This topic describes how to view and handle alert events that are detected by Server Guard.

**Background information**

After Apsara Stack Security detects an alert event, the information about the alert event is displayed. If the alert event is not handled, the alert event is displayed in the **Unhandled**
**Alerts** list on the **Security Alerts** page. After the alert event is handled, the status of the
alert event changes from **Unhandled Alerts** to **Handled**.

> **Note:** Apsara Stack Security retains the records of **Unhandled Alerts** and **Handled** on the **Security Alerts** page. By default, the records of **Unhandled Alerts** are displayed.

**View the details of an alert event**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the Security Alerts page, view or search all alert events and the details of the alert
events.

**Handle alert events**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the **Security Alerts** page, find the alert event that you want to handle and click
**Handle** in the **Actions** column. In the dialog box that appears, configure Process Method
and click **Process Now**.

> **Note:** If the alert event contains multiple correlated exceptions, you can handle the exceptions on the page that appears after you click **Handle**.

**Ignore**: If you ignore the alert event, the status of the alert event changes to **Handled**.
Server Guard no longer generates alerts for the event.
**Add To Whitelist**: If the alert event is a false positive, you can add the alert event to the
whitelist. Then, the status of the alert event changes to **Handled**. Server Guard no longer generates alerts for the event. In the **Handled** list, you can click **Cancel whitelist** to remove the alert event from the whitelist.

> **Note:** A false positive indicates that Server Guard generated an alert on a normal process. A common false positive is a **suspicious process that sends TCP packets**. The false positive notifies you that suspicious scans on other devices are detected on your servers.

**Batch unhandled**: This method allows you to handle multiple alert events at a time.
Before you handle multiple alert events at a time, we recommend that you view the details of the alert events.
5. **Optional.** If you confirm that one or more alert events can be ignored or are false
positives, select the alert events and click **Ignore Once** or **Whitelist** on the **Security**
**Alerts** page.

**Export alert events**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the **Security Alerts** page, click the
icon above the alert event list to export alert events. After the alert event list is exported, the **Done** message appears in the upper-right corner of the Security Alerts page.
5. In the **Done** notification of the **Alerts** page, click **Download**.
The alert list is downloaded to your computer.

##### 3.4.5.3 View exceptions related to an alert

Server Guard supports automatic analysis of exceptions related to an alert. You can click the name of an alert in the alert list to view and manage all exceptions that are related to the alert. You can also view the results of automatic attack tracing to analyze and handle the exceptions.

**Background information**

Security Center automatically associates alerts with exceptions in real time to detect potential threats. Exceptions related to an alert are listed in chronological order. This allows you to analyze and handle the exceptions to improve the emergency response mechanism of your system. An automatically correlated alert is identified by the icon.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the Security Alerts page, click the name of the required alert in the **Event** column. The
alert details panel appears.
5. In the alert details panel, view the alert details and related exceptions of the alert. Then,
handle the exceptions. View the details about an alert View the assets that are affected by an alert, the first time and last time when the alert was triggered, and the details about the related exceptions. View affected assets Move the pointer over the name of an **affected asset** to view the details about the asset. The details include information about all the alerts, vulnerabilities, baseline risks, and asset fingerprints on the asset. View and manage **related exceptions** In the **Related Exceptions** section, view the details about all the exceptions that are related to the alert. You can also view suggestions on how to handle the exceptions. Click **Note** to the right of an exception to add a note for the exception. Click the icon to the right of a note to delete the note.

##### 3.4.5.4 Quarantine

Sever Guard can quarantine malicious files. Quarantined files are listed in the quarantine box on the Intrusions page. The system automatically deletes a quarantined file 30 days after the file is quarantined. You can restore a quarantined file with a few clicks before the file is deleted. This topic describes how to view and restore quarantined files.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. On the **Security Alerts** page, click **Quarantine** in the upper-right corner.
In the **Quarantine** panel, you can perform the following operations: View information about quarantined files. The information includes server IP addresses, paths that store the files, file status, and modification time. Click **Restore** in the **Actions** column to remove a quarantined file. The file is displayed in the alert list again.

##### 3.4.5.5 Configure alerts

This topic describes how to configure alerts. You can specify approved logon locations and web directories to scan.

**Background information**

Server Guard supports advanced logon settings. You can configure fine-grained logon detection rules. For example, you can specify approved logon IP addresses, approved logon time ranges, and approved logon accounts to block unauthorized access to your assets.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Security**. In the **Server Security** section, click **Server**
**Guard**.
3. In the left-side navigation pane, choose **Defense** > **Security Alerts**.
4. In the upper-right corner of the page that appears, click **Settings**.
Configure parameters on different tabs.

**Add an approved logon location**

a. In the **Login Location** section, click **Management** on the right. b. Select the logon location that you want to add and select the servers that allow logons from the location. c. Click **OK**. Server Guard allows you to **modify** or **remove** approved logon locations. To change the servers that allow logons from an approved logon location, find the location and click **Edit** in the Actions column. To remove an approved logon location, find the location and click **Delete** in the Actions column.

**Configure advanced logon settings**

> **Note:** When you configure advanced logon settings, you can specify the IP addresses, accounts, and time ranges that are allowed for logons to your assets. After the advanced logon settings are configured, Server Guard sends you alerts if your assets receive logon requests that are outside the logon settings. The procedure to configure advanced logon settings is similar to the procedure to configure **approved** **logon locations**. You can follow the preceding procedure to **create**, **modify**, and **delete** advanced logon settings.

Turn on or turn off Uncommon IP Alert to the right of **Common Login IPs**. If you turn on Uncommon IP Alert and your assets receive logon requests from unapproved IP addresses, alerts are triggered. Turn on or turn off Uncommon Time Alert to the right of **Common Login Time**. If you turn on Uncommon Time Alert and your assets receive logon requests in unapproved time ranges, alerts are triggered. Turn on or turn off Uncommon Account Alert to the right of **Common Login Accounts**. If you turn on Uncommon Account Alert and your assets receive logon requests from unapproved accounts, alerts are triggered.

**Add web directories to scan**

Server Guard automatically scans web directories of data assets in your servers and runs dynamic and static scan tasks. You can also manually add custom web directories. a. In the **Add Scan Targets** section, click **Management** on the right. b. Specify a valid web directory and select the servers on which the web directory is scanned.

> **Note:** To ensure the scan performance and efficiency, we recommend that you do not specify a root directory.

c. Click **OK**.

### 3.5 Log retrieval

#### 3.5.1 Log retrieval overview

Server Guard provides the log retrieval feature. You can use the feature to manage logs that are scattered in various systems of Apsara Stack in a centralized manner. This way, you can easily identify the causes of issues that occur on your servers. The log retrieval feature allows you to store logs for 180 days and query logs that are generated within 30 days.

**Features**

The log retrieval feature provides the following benefits:
**End-to-end log retrieval platform**: allows you to retrieve logs of various Apsara Stack
services over a unified interface and trace issues in a more efficient manner.
**Log service-related software as a service**: allows you to query logs on all servers in
Apsara Stack without the need to install or deploy specific software. TB-level data retrieval: allows you to obtain full-text search results within several seconds. You can also add up to 50 Boolean expressions in a search condition. Support for various log sources. Log delivery: allows you to deliver security logs to Log Service for further analysis.

**Scenarios**

You can use the log retrieval feature to meet the following requirements:
**Security event analysis**: When a security event is detected on a server, you can retrieve
the logs to identify the cause of the issue and assess the extent of the damage and affected assets.
**Operation audit**: You can audit the operation logs on a server to identify high-risk
operations and serious issues in a precise manner.

**Retrievable log types**

Table 1. Log sources

| Log source | Description |
|---|---|
| Logon history | Logs of successful system logons |
| Process snapshots | Logs of processes on a server at a specific point in time |
| Port listening snapshots | Logs of listening ports on a server at a specific point in time |
| Account snapshots | Logs of account-based logons on a server at a specific point in time |
| Process startups | Logs of process startups on a server |
| Network connections | Logs of outbound connections that are initiated from servers |

#### 3.5.2 Query logs

This topic describes how to search for and view physical server logs.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, click **Log Retrieval**.
4. Configure search conditions.

| Search condition | Description |
|---|---|
| Log source | The log source that you want to query. For more information, seeL og sources. |
| Field | The field that is recorded for the log source. For more information, see Log sources. |
| Keywords | The keyword of the field. |
| Logical operator | The equality operator. |
| + | You can click the plus sign to add expressions for a log source. |
| Add conditions | The search conditions for different log sources. |

5. Click **Search** and view the search result.
**Reset search conditions**: Click **Reset** to remove existing search conditions.
**Save search conditions**: Click **Save search logic** to save a search condition, which
can be used for subsequent log searches.
**Use saved search conditions**: Click **Saved Search Conditions** to select and use a
search condition that you saved.

#### 3.5.3 Supported log sources and fields

This topic describes the log sources and fields that are supported by the log retrieval feature. The log retrieval feature allows you to query the following types of log sources. You can click a log source link to view the fields that are supported.

| Log source | Description |
|---|---|

| Logon history | Logs of successful system logons |
|---|---|
| Process snapshots | Logs of processes on a server at a specific point in time |
| Port listening snapshots | Logs of listening ports on a server at a specific point in time |
| Account snapshots | Logs of account-based logons on a server at a specific point in time |
| Process startups | Logs of process startups on a server |
| Network connection logs | Logs of active connections from a server to the Internet. |

**Logon history**

The following table describes the fields that are supported in the logon history.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| warn ip _ | string | The source IP address used for the logon. |
| warn port _ | string | The port number of the logon. |
| warn user _ | string | The username for the logon. |
| warn type _ | string | The type of the logon. |
| warn count _ | string | The number of logon attempts. |

**Process startups**

The following table describes the fields that are supported in process startup logs.

| Field | Type | Description |
|---|---|---|

| uuid | string | The ID of the client. |
|---|---|---|
| IP | string | The IP address. |
| pid | string | The ID of the process. |
| groupname | string | The user group. |
| ppid | string | The ID of the parent process. |
| uid | string | The ID of the user. |
| username | string | The username. |
| filename | string | The name of the process file. |
| pfilename | string | The name of the parent process file. |
| cmdline | string | The command line. |
| filepath | string | The path of the process file. |
| pfilepath | string | The path of the parent process file. |

**Port listening snapshots**

The following table describes the fields that are supported in logs of listening port snapshots.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| src port _ | string | The listening port. |
| src ip _ | string | The listening IP address. |

| proc path _ | string | The path of the process file. |
|---|---|---|
| pid | string | The ID of the process. |
| proc name _ | string | The name of the process. |
| proto | string | The protocol. |

**Account snapshots**

The following table describes the fields that are supported in account snapshot logs.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| perm | string | Indicates whether the user has root permissions. |
| home dir _ | string | The home directory. |
| warn time _ | string | The time at which a password expiration notification is sent. |
| groups | string | The group to which the user belongs. |
| login ip _ | string | The IP address of the last logon. |
| last chg _ | string | The time at which the password was last changed. |
| shell | string | The Linux shell command. |
| domain | string | The domain in Windows. |
| tty | string | The terminal of the logon. |

| account expire _ | string | The time at which the account expires. |
|---|---|---|
| passwd expire _ | string | The time at which the password expires. |
| last logon _ | string | The time of the last logon. |
| user | string | The username. |
| status | string | The account status. Valid values: 0: disabled 1: normal |

**Process snapshots**

The following table describes the fields that are supported in process snapshot logs.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| path | string | The path of the process file. |
| start time _ | string | The time at which the process was started. |
| uid | string | The ID of the user. |
| cmdline | string | The command line. |
| pname | string | The name of the parent process. |
| name | string | The name of the process. |
| pid | string | The ID of the process. |

| user | string | The username. |
|---|---|---|
| md5 | string | The MD5 hash value of the process file. If the size of the process file exceeds 1 MB, the system does not calculate the MD5 hash value of the process file. |

**Network connection logs**

The following table describes the fields that are supported in network connection logs.

| Field | Type | Description |
|---|---|---|
| uuid | string | The ID of the client. |
| IP | string | The IP address. |
| src ip _ | string | The source IP address. |
| src port _ | string | The source port. |
| proc path _ | string | The path of the process file. |
| dst port _ | string | The destination port. |
| proc name _ | string | The name of the process. |
| dst ip _ | string | The destination IP address. |
| status | string | The status. |

#### 3.5.4 Logical operators

The log retrieval feature supports multiple search conditions. You can add multiple logical operators to one search condition for one log source, or combine multiple search conditions for several log sources by using different logical operators. This topic describes the logical operators that are supported in log retrieval. Examples are provided to help you understand these operators. The following table describes the logical operators that are supported in log retrieval. Table 1.

| Logical operator | Description |
|---|---|
| and | Binary operator. This operator is in the format of query 1 and query 2 , which indicates the intersection of the query results of query 1 and query 2 . Note If no logical operators are used for multiple keywords, the default operator is AND. |
| or | Binary operator. This operator is in the format of query 1 or query 2 , which indicates the union of the query results of query 1 and query 2 . |
| not | Binary operator. This operator is in the format of query 1 not query 2 , which indicates the results that match query 1 but do not match query 2 . This format is equivalent to query 1 - query 2 . Note If you use only not query 1 , the log data that does not contain the query results of query 1 is returned. |

|   | query 1 not query 2 |   |
|---|---|---|
| query 1 |   |   |

### 3.6 Server settings

#### 3.6.1 Install the Security Center agent

If you want to monitor the security of assets in Server Guard, you must install the Security Center agent on your server. This topic describes how to install the Security Center agent by using Server Guard settings.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Settings** > **Agent Installation**.
4. **Optional.** Click the **Client to be installed** tab to view the number of servers on which the
agent is not installed and the information about the servers. You can specify the operating system type, server IP address, or server name to search for a server.
5. Click the **Client Installation Guide** tab to install the Security Center agent.
CLI Installation

**Deploy Hosts in Apsara Stack**

a. On the **CLI Installation** tab, find the operating system of your server and click **Copy** on the right.

> **Note:** If you do not find the required installation command for the operating system of your server, click **Create Installation Command**, configure the **Organization**, **Resource Set**, and **Client Type** parameters, and then click OK. Then, click **Copy** on the right.

b. Run the command on your server. c. Click the **Installation Verification** tab to verify the command based on the operating system of the server.

**Deploy Hosts Outside Apsara Stack**

> **Important:** Before you install the Security Center agent, make sure that your quota of data centers meets your requirements, and the domain name of the server is resolved to the Server Guard server. You can click **View Domain Name Resolution** or **View Quota** to view the required information.

a. Click **Manage Service Provider**. On the **Assets** page, click the **Server(s)** tab. b. On the tab that appears, click **Create Provider**, configure the **Provider Name** parameter, and then click **OK**. c. Go to the **Agent Installation** page. On the **Client Installation Guide** tab, click **CLI**
**Installation**.
d. In the **Deploy Hosts Outside Apsara Stack** section, find the new service provider and click Create Installation Command. In the dialog box that appears, configure the
**Organization**, **Resource Set**, **Client Type**, **Effective Duration**, **Region**, **Data**
**Center**, and **Asset Group** parameters.
e. After the configuration is complete, click **Copy** and run the command on your server. f. Click the **Installation Verification** tab to verify the command based on the operating system of the server.

**Image Installation**

> **Important:** Before you install the Security Center agent, make sure that your quota of data centers meets your requirements, and the domain name of the server is resolved to the Server Guard server. You can click **View Domain Name Resolution** or **View** **Quota** to view the required information.

a. On the **Image Installation** tab, install the agent as prompted. b. Click the **Installation Verification** tab to verify the command based on the operating system of the server.

#### 3.6.2 Manage protection modes

This topic describes how to manage protection modes for each server to improve the efficiency and security of servers.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Server Security > Server Guard**. On the **Server Guard** page, select a
region from the **Region** drop-down list and click **Access with Authorized Role**. In multi-level organization mode,all data permissions are managed by using resource sets in organizations.You can select an organization or a resource set in the top navigation bar of the console to view or manage the assets of the organization or resource set.

> The parent organization has the highest management permissions. Modifications to the parent organization take effect on all child organizations and resource sets that belong to the parent organization. Proceed with caution when you modify the configurations.

3. In the left-side navigation pane, choose **Settings** > **Mitigation Mode**.
4. On the **Mitigation Mode** page, manage protection modes.
The advanced prevention mode and the security protection mode for major activities are supported. You must select a protection mode for each server to improve the protection efficiency. Self-protection is supported. The system automatically blocks activities that attempt to uninstall the Server Guard agent. This ensures the stability of the Server Guard agent. We recommend that you run important services in an operating system that supports selfprotection. This helps prevent the Server Guard agent from being illegally uninstalled. If the Server Guard agent is uninstalled, the server is not protected, which can cause security risks. The system requires 30 minutes to disable self-protection. configurations

## 4 Apsara Stack Security configurations

**configurations**

### 4.1 Log on to the Apsara Uni-manager Management Console

**manager Management Console**

This topic describes how to log on to the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. Enter your username and password.
You must obtain the username and password from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform corresponding
operations in the following scenarios: It is the first time that you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password that you entered in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You enabled MFA and bound an MFA device: Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

configurations

### 4.2 System monitoring

On the Monitoring Overview tab, you can monitor cloud services to identify abnormal services at the earliest opportunity. This facilitates service O&M. This topic describes how to view the monitoring data.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **System Monitoring**.
4. On the System Monitoring page, view the monitoring overview and monitoring data of cloud
services. On the **Monitoring Overview** tab, you can view the following information. Monitoring overview: You can view the total numbers of monitored services, abnormal services, metrics, and exceptions. Cloud service monitoring data: You can view the information about cloud services, such as the number of metrics, the number of exceptions, and the service status. You can view the monitoring data of each cloud service on the corresponding cloud service tab. Cloud services that can be monitored include Server Guard, Basic Service, Automated Orchestration, Platform for Connecting to Third-party Services, Data Encryption Service, Threat Intelligence, Intelligent Analysis Platform, Updates, Trusted Computing, NDR, Security Operations Center, Key Management Service, Password service platform, Key Management Service(Base Edition), and Container safety. configurations Monitored data includes data of all services that are connected to Alibaba Cloud services. In this topic, Server Guard is used as an example. Click the **Server Guard** tab to view all services that are required to run Server Guard. You can search for a service by service name or status in the search box above the service list. In the service card section, you can view the service status, CPU utilization, memory usage, loads, TCP connections, processes, and NGINX queries per second (QPS). You can click a service card to view the monitoring details of the service.

| Metric | Description |
|---|---|
| Basic Monitoring | You can configure the monitoring time and monitoring view. The monitoring time supports 3 Hours, 6 Hours, 12 Hours, 1 Day, 2 Days, and Custom. You can click the icon to manually update the monitoring data. You can also turn on Auto Refresh to automatically update the monitoring data. The monitoring view supports Cluster View and Single- server View. |
| Middleware |   |
| Health Check | You can check the health status of all hosts in an application based on check methods such as TCP- and HTTP-based health checks. |

### 4.3 Rules

#### 4.3.1 Create and manage IPS rules

Cloud Firewall provides built-in intrusion prevention system (IPS) rules. You can create custom IPS rules based on your business requirements and network environment to monitor the operations of Cloud Firewall. This topic describes how to create and manage custom IPS rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
configurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Cloud Firewall IPS Rules** tab, click **Create Rule**. In the panel that appears,
configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Rule Name | The name of the IPS rule. We recommend that you enter an informative name for easy management. |
| Rules Engine | The rules engine that you want to use. Valid values:B asic Policies and Virtual Patches. |
| Attack Type | The type of attacks that you want to detect by using the IPS rule |
| Severity | The level of the severity. Valid values: Low, Medium, and High. |
| CVE | The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability that you want to list in the IPS rule. Note CVE provides a list of public security vulnerabilities. CVE IDs are allocated by a CVE Numbering Authority (CNA). |
| Application | The name of the attacked application. |
| Rule Mode | The mode of the IPS rule. Valid values: Packet and Traffic. |
| Direction | The direction of traffic that you want to monitor by using the IPS rule. Valid values: Inbound and Outbound, Inbound, and Outbound. |
| Rule Content | The content of the IPS rule. You must specify the content by using the Snort syntax. Note To prevent negative impact on your business, make sure that you enter valid content for the rule. |
| Rule Description | The description of the IPS rule. We recommend that you enter information such as the purpose or impact of the rule. |

configurations

| Description | The additional description of the IPS rule. We recommend that you enter information that can help you identify the IPS rule, such as the purpose or impact of the rule. |
|---|---|

After you create a custom IPS rule, you can perform the following operations on the rule: View the details of the rule You can filter rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details. Enable the rule Find the rule that you want to enable and turn on the switch in the **Enable or not** column to change the status of the rule from **Disable** to **Enable**. Disable the rule If a rule does not meet your business requirements, you can disable the rule. Find the rule that you want to disable and turn off the switch in the **Enable or not** column to change the status of the rule from **Enable** to **Disable**.

#### 4.3.2 Manage Anti-DDoS Service rules

On the Anti-DDoS Service rules page, you can modify threshold settings for traffic scrubbing and redirection based on your business requirements. This topic describes how to modify threshold settings for traffic scrubbing and redirection.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Anti-DDoS Service Rules** tab, click **Scrubbing Policy**. Then, specify a custom
threshold for traffic scrubbing. i. Find the traffic scrubbing rule whose threshold you want to modify and click **Modify**
**Threshold** in the **Solution** column.
ii. In the **Modify Threshold** dialog box, specify a threshold and click **OK**.
5. On the **Anti-DDoS Service Rules** tab, click **Reroute Threshold**. Then, specify custom
thresholds for traffic redirection. i. Find the rule whose thresholds you want to modify and click **Modify Threshold** in the
**Solution** column.
ii. In the **Modify Threshold** dialog box, specify custom thresholds and click **OK**. configurations iii. **Optional.** Click **Automatic DDoS Traffic Redirection and Scrubbing**. In the **Enable**
**Automatic Redirection** message, click **OK**.

> **Note:** By default, **Automatic DDoS Traffic Redirection and Scrubbing** is turned off.

If you turn on Automatic DDoS Traffic Redirection and Scrubbing, traffic scrubbing events are triggered based on custom thresholds. The traffic of attacked IP addresses is automatically forwarded to an Anti-DDoS cluster for scrubbing. If you turn off Automatic DDoS Traffic Redirection and Scrubbing, alert events are triggered based on custom thresholds. You can start or end traffic scrubbing in the Anti-DDoS Service console based on your business requirements.

#### 4.3.3 Manage Server Guard rules

You can view vulnerabilities, baselines, and server exceptions on the Server Guard Rules tab. This topic describes how to view the information about Server Guard rules.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **Server Guard Rules** tab, view the information about Server Guard rules.

| Item | Description |
|---|---|
| Overview (marked 1 in the preceding figure) | You can view the following information: Total Vulnerability Detection Rules, Total Baseline Check Items, Total Host Exception Detection Rules, and Engines. |
| Vulnerabilities (marked 2 in the preceding figure) | On the Vulnerabilities tab, you can view all detected vulnerabilities and the total number of detected vulnerabilities. To search for a vulnerability, you can select a vulnerability type from the Vulnerability Type drop-down list and enter a Common Vulnerabilities and Exposures (CVE) ID or operating system (OS) name in the search box. In the vulnerability list, you can view the following information about a detected vulnerability: Vulnerability Name, CVE ID, Vulnerability Type, OS, Updated At, and Status. |

configurations

| Baselines (marked 2 in the preceding figure) | On the Baselines tab, you can view the baseline types and check the items that are used. To search for a baseline, you can select a baseline type from the Baseline Type drop-down list, select a severity from the Risk Level drop-down list, and enter a check item category or name in the search box. In the baseline list, you can view the following information about a baseline: Baseline Type, Check Item Category, Check Item Name, Risk Level, Updated At, and Status. |
|---|---|
| Server Exceptions (marked 2 in the preceding figure) | On the Server Exceptions tab, you can view the following information: Rule Alert Types and Webshell & Malicious Processes. To search for an exception on a server, you can select a rule category from the Rule Category drop-down list, select a severity level from the Risk Level drop-down list, and then enter a rule subcategory name in the search box. In the server exception list, you can view the following information: Rule Subcategory, Rule Category, Risk Level, Updated At, Source, and Status. |

#### 4.3.4 Create and manage WAF rules

You can create custom Web Application Firewall (WAF) rules based on your business requirements and network environment to monitor the operations of WAF. This topic describes how to create and manage WAF rules.

**Procedure**

> **Important:** WAF rules are global custom rules that take effect on all tenants. Proceed with caution.

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Rule Operation**.
4. On the **WAF Rules** tab, click **Create Rule**. Configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Mode | The handling action and status of the rule. You can set the handling action to Block, Allow, Monitor, or Detection Module Control. You can set the status to Enable or Disable. |
| Description | The description of the rule. |

configurations

| Severity | The level of the severity. Valid values: No Threat, Low, Moderate, and Important. |
|---|---|
| Match Condition | The match condition of the rule. Each match condition consists of am atch field, a logical operator, and a match value. |
| Logging | Specifies whether to record logs. Valid values: Perform Logging When Match Condition Is Met and Do not Perform Logging When Match Condition Is Met. |
| Attack Type | The type of attacks that you want the rule to detect. You can select only one value. |
| Blocking Status Code | The status code that is returned. You can select only one value. |
| Expire At | The expiration time of the rule. If you do not specify an expiration time, the rule never expires. |

After you create a rule, you can perform the following operations on the rule: Filter the WAF rules. Find the rule whose details you want to view and click **Details** in the **Actions** column to view the rule details.

### 4.4 Alert settings

On the Alert Settings page, you can configure alert contacts and alert rules. When monitoring data meets the conditions of an alert rule, the system automatically sends an alert to specified alert contacts by email and DingTalk message. This topic describes how to configure alert contacts and alert rules.

**Configure alert contacts**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the **Alert Settings** tab, click **Create Contact**. Configure the Contact Name, DingTalk
Chatbot Token, and Email parameters, and click **Determine**. You can view the added contact in the contact list. You can **modify** a contact or **delete** multiple contacts at a time.

**Configure alert rules**

1. Log on to the Apsara Uni-manager Management Console.
configurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Alert Settings**.
4. On the **AEGIS** tab, select the alert type, severity, notification method, and frequency, and
click **Save**.

### 4.5 Updates

#### 4.5.1 Upgrade center overview

The upgrade center allows you to manually or automatically update the feature library and the version of Apsara Stack Security to ensure up-to-date protection. You can perform the following steps for an update:
1. Configure the import mode of your update package.
The upgrade center supports**automatic import** and **manual import**. If Apsara Stack can be accessed over the Internet, select **Online Automatic Import**. If Apsara Stack cannot be accessed over the Internet, select **Offline Manual Import**. If you select this option, you must download the update package. For more information, see Download update packages.
2. Update the feature library and the version of Apsara Stack Security. For more information,
see Update the feature library or the version of Apsara Stack Security.

#### 4.5.2 Update feature libraries or the version of Apsara Stack Security

**of Apsara Stack Security**

The upgrade center supports automatic import and manual import of update packages. You can use the update packages to update feature libraries or the version of Apsara Stack Security. This topic describes how to update feature libraries or the version of Apsara Stack Security.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Upgrade Center**.
4. On the **Upgrade configuration** tab, configure Upgrade Package Import.

**Manual import**

If your Apsara Stack environment is inaccessible over the Internet, you can manually import update packages to update feature libraries or the version of Apsara Stack Security. a. Set Upgrade Package Import to **Offline Manual Import** and click **Generate Upgrade**
**Identifier**. Then, download update packages. For more information, see Download
update packages. configurations b. Click Import Upgrade Package and drag the downloaded update packages to the dotted box. You can also click the icon to upload the update packages.

> **Note:** Before you upload the update packages, click the link in the **Manually Import** **offline upgrade packages**dialog box and trust the certificate.

After you import the update packages, you can view the update packages on the Feature Library Upgrade page and Version Upgrade page and perform updates.

**Automatic import**

If the Apsara Stack environment can connect to the Internet, you can select the automatic import method to import update packages and update feature libraries or the version of Apsara Stack Security. a. Set Upgrade Package Import to **Online Automatic Import** and configure the parameters.

| Parameter | Description |
|---|---|
| Alibaba Cloud account ID | Enter the ID of your Apsara Stack tenant account. |
| Access Key | Enter the AccessKey ID of the account. |
| Access Secret | Enter an AccessKey secret of the account. |
| Automatic upgrade time period | Select a time period for automatic updates. Valid values: 0-6 when 0-8 when 0-24 when 22-6 when |

b. Click **Connectivity test**. c. If the connectivity test is successful, turn on **Automatic update**. After **Automatic update** is turned on, the system automatically downloads update packages at regular intervals
5. Update feature libraries or the version of Apsara Stack Security.

**Update feature libraries**

Batch update: On the **Feature Library Upgrade** tab, click **One-click upgrade**. Update a service in Apsara Stack Security: Find the service that you want to update on the **Feature Library Upgrade** tab and click **Upgrade now** in the **Operation** column. After the update is complete, the status of the service is **Upgrade successful**. configurations If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: On the **Feature Library Upgrade** tab, find the service and click **Version Details** in the **Operation** column to view the versions of the updated rule libraries. You can click **Restart Upgrade** to update a rule library in a feature library. In the **Feature Library Upgrade Records**panel, find the feature library that you want to view and click **Details** in the **Operation** column to view the details of the feature library update package. You can find a rule library and click **Restart**
**Upgrade** in the **Operation** column to update the rule library.
On the **Feature Library Upgrade** tab, find the service and click **Upgrade Records** in the **Operation** column to view the versions of the updated feature libraries.

**Update the version of Apsara Stack Security**

Batch upgrade: On the **Version Upgrade** tab, click **One-click upgrade**. Update a service in Apsara Stack Security: Find the service that you want to update on the **Version Upgrade** tab and click **Upgrade now** in the **Operation** column. After the update is complete, the status of the service is **Upgrade successful**. If the update fails, you can click **Upgrade Records** in the **Operation** column to find the versions of the feature libraries that failed to be updated and click **Retry** in the Operation column. If the update is successful, you can perform the following operations: Click **Upgrade Records** in the **Operation** column to view the versions of the updated feature libraries. You can also click **Restart Upgrade** or **Rollback**.

#### 4.5.3 Download update packages

If you need to update the version of Apsara Stack Security or update Apsara Stack Security services, you can download the required update packages in the Alibaba Cloud Security Center console and upload the update packages in Apsara Stack Security Center to complete the update. This topic describes the update modes of Apsara Stack Security and how to download update packages in different update modes.

**Update modes**

Security Center provides two update modes: standard mode and advanced mode. The following table describes the two update modes.

| Update mode | Description | References |
|---|---|---|

configurations

| Standard mode | In this mode, the system provides the update packages that are required for version update or service update based on the version of Apsara Stack Security that you entered, and encapsulates these update packages into a combined update package. In this mode, you do not need to manually select update packages. We recommend that you use the standard mode. In this mode, you can update the version of Apsara Stack Security or update Apsara Stack Security services in a more convenient and efficient manner. | Standard mode |
|---|---|---|
| Advanced mode | In this mode, you can select the version of Apsara Stack Security to obtain the latest update packages. You can also download update packages to update Apsara Stack Security services based on your business requirements. Note In advanced mode, you need to know the dependencies and update sequence between update packages. | Advanced mode |

**Standard mode**

1. Log on to the Security Center console.
2. In the left-side navigation pane, choose **Operation > Upgrade packages**.
3. In the **Upgrade Mode** section on the **Upgrade packages** page, click **Standard Mode**.
4. In the **Identifier of Apsara Stack Security Version** search box, enter the version of
Apsara Stack Security to which you want to update and click **Obtain Rule Package** to obtain update packages.

> **Note:** For more information about how to obtain the version identifier of Apsara Stack Security, click **How to Obtain Upgrade Package** below the search box.
> If you use Apsara Stack Security V3.12, V3.13, or V3.14, you must enter the version identifier of Apsara Stack Security in the Identifier of Apsara Stack Security Version search box to obtain update packages.

5. In the **Download Upgrade Package** section, find the update packages that you want to
download and click **Download** in the **Operation** column. After the update packages are downloaded, upload the update packages to Apsara Stack Security Center. In Apsara Stack Security Center, perform update-related operations to complete the update.

**Advanced mode**

1. Log on to the Security Center console.
2. In the left-side navigation pane, choose **Operation > Upgrade packages**.
3. In the **Upgrade Mode** section on the **Upgrade packages** page, click **Advanced Mode**.
4. In the **Identifier of Apsara Stack Security Version** section, select Apsara Stack Security
from the drop-down list on the left and select the version of the update package that you want to download from the drop-down list on the right.
5. In the **Download Upgrade Package** section, find the update packages that you want to
configurations download and click **Download** in the **Operation** column. After the update packages are downloaded, upload the update packages to Apsara Stack Security Center. In Apsara Stack Security Center, perform update-related operations to complete the update.

### 4.6 Global configuration

#### 4.6.1 Configure host security rules

You can configure global brute-force attack detection rules to prevent hosts from being cracked by brute-force attacks and prevent unusual batch logons and suspicious account logons. This topic describes how to configure host security rules.

**Important**

If you modify global brute-force attack detection rules, all host assets, including tenantside hosts and platform-side physical servers, are affected. The modification also affects the attack analysis results of Threat Detection Service (TDS). Proceed with caution.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Host security rule settings** tab, configure a global brute-force attack detection
rule and click **Save and Apply**.

| Parameter | Description |
|---|---|
| Host brute force cracking | Specify the time range within which you want to detect brute-force attacks and the threshold of logon failures that are allowed. If the number of logon failures exceeds the specified threshold within the specified time range, brute-force attacks occur. |
| Batch abnormal login | Specify the time range within which you want to detect unusual logons and the threshold of servers that can be logged on to by using an account. If the number of servers that can be logged on to by using an account exceeds the specified threshold within the specified time range, unusual logons occur. |
| Suspicious account login | If a remote logon account is included in the list of suspicious accounts, an alert is generated for logons that use the account. Click Manage list of suspicious accounts. In the Suspicious account management panel, enter suspicious accounts or upload a list of suspicious accounts by using a template. The file must be less than 5 KB in size. To ensure compatibility with the Windows system mechanism, use lowercase letters when you enter Windows accounts. |

configurations

#### 4.6.2 Configure a whitelist

If a normal request is considered an attack by the attack blocking feature of Threat Detection Service (TDS) or the unusual logon detection feature of Server Guard, you can add the source IP address of the request to a whitelist to avoid false positives. This topic describes how to configure a global whitelist for unusual logons and brute-force attacks.

> **Note:** Make sure that only trusted IP addresses are included in the whitelist.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Whitelists** tab, click **Add**, configure parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Type | Global Logon Whitelist: Server Guard does not generate alerts for unusual logons from the IP addresses that are included in this whitelist. Brute-force Whitelist: Server Guard does not generate alerts for brute-force attacks from the IP addresses that are included in this whitelist. |
| SOURCE IP | Enter a source IP address or CIDR block. |
| Destination IP | Enter a destination IP address or CIDR block. If you set Type toB rute-force Whitelist, you must configure this parameter. |

You can **delete** a whitelist that is no longer required.

#### 4.6.3 Configure the attack blocking feature

The attack blocking feature protects your servers from web attacks. This topic describes how to configure the attack blocking feature.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
configurations
4. On the **Global Settings** tab, turn on or off the switch in the Actions column to enable or
disable the attack blocking feature. After you disable the attack blocking feature, Server Guard generates alerts for web attacks but does not block them.

#### 4.6.4 Add a Server Guard account

After you add a Server Guard account, you can use the account to configure and manage Server Guard and Web Application Firewall (WAF) resources. This topic describes how to add a Server Guard account.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Global Settings**.
4. On the **Physical Server Protection** tab, click **Add**. In the Add Account of Server Guard
Installed on Physical Machines dialog box, configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Username | The username of the Server Guard account that you want to add. If you do not have a Server Guard account, follow the on-screen instructions to create an account. |
| Organization | The platform organization. Retain the default value. |
| Organization UID or Primary Key | The UID or primary key of the organization to which the Server Guard account belongs. |

### 4.7 Cloud Firewall monitoring

You can use the Cloud Firewall monitoring feature to monitor the status of Cloud Firewall, detect abnormal traffic, and handle abnormal events at the earliest opportunity. This topic describes how to perform system inspection and service monitoring.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Cloud Firewall Monitoring**.
4. In the **System Inspection** section, click **One-click Inspection**.
After the inspection is complete, you can perform the following operations: configurations Click **Details** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
**(CCFW)**, or **Traffic Monitoring (Beaver)** to view the status of each system.
Click **Inspect Now** in the **Actions** column of **Internet Firewall (ICFW)**, **VPC Firewall**
**(CCFW)**, or **Traffic Monitoring (Beaver)** to perform inspection on each system.
5. In the **Service Monitoring** section, configure the monitoring settings on the **ICFW** or
**CCFW** tab.

**ISW-side Cloud Firewall (ICFW)**

a. In the **Traffic Forwarding Configuration - Service CIDR Block** section, click **Add**, configure the parameters, and then click **OK**.

| Parameter | Description |
|---|---|
| Device Cluster ID | The cluster ID of specific devices. The devices use the CIDR block that you want to add for traffic redirection. |
| Traffic Redirection Method | The traffic redirection method. Valid values: ISW and XGW. |
| CIDR Block for Traffic Diversion | The CIDR block for traffic redirection. |
| Type | The type of the CIDR block for traffic redirection. Value values: Test and Business. |
| Service Description | The service-related description. |

After the configuration is complete, you can view the automatic check frequency for the CIDR block and the self-check result of each cluster in the **Service Check Status** and **Interface Status** sections. In each section, you can select a check frequency from the**automatic check** drop-down list to specify an automatic check frequency for the CIDR block. You can

> icon to manually refresh the check frequency for the CIDR block.

also click the configurations b. In the**Connectivity Check**section, click**Add**. Configure the parameters and click **OK**.

| Parameter | Description |
|---|---|
| Device Cluster ID | The cluster ID of specific devices. The devices use the CIDR block that you want to add for traffic redirection. |
| Test IP Address | The IP address of the device that you want to connect. |
| Type | The type of the connectivity health check. Valid values: Business, Test, and system. |
| Check Frequency | The check frequency. Unit: seconds. The value must be an integer from 1 to 60. |
| Check Threshold | The check threshold. Unit: times. The value must be an integer from 1 to 30. |
| Action | The action that you want to take. Valid values:A utomatic Bypass and Alert. |

After you complete the configuration, you can test the connectivity to the IP address. c. Set **Global Default Policy**to**block all** or**permit all**. The parameter takes effect for only inbound traffic.

**CSW-side Cloud Firewall (CCFW)**

Click the **CCFW** tab to view the following information: Cloud Firewall Taskflows, Cloud Firewall Status Self-check, Device Status Self-check, Interface Status, and Connectivity Test.

### 4.8 Account management

#### 4.8.1 Manage Apsara Stack tenant accounts

This topic describes how to view and modify the information about your Apsara Stack tenant account.

> **Important:** All assets in Apsara Stack Security are bound to your Apsara Stack tenant account. You can modify the account information. Proceed with caution.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
configurations
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Apsara Stack Account** tab, modify the information about your Apsara Stack
tenant account. i. Find your Apsara Stack tenant account and click **Revised** in the **Operation** column. ii. In the **Change Account** dialog box, modify Apsara Stack Account, Access Key, and Access Secret, and click **OK**. After the modification, you can click Details in the **Operation** column to view the details of the Apsara Stack tenant account.

#### 4.8.2 Manage Alibaba Cloud accounts

After you add an Alibaba Cloud account to Apsara Stack Security Center, you can manage the Anti-DDoS Pro, Anti-DDoS Premium, and Web Application Firewall (WAF) instances that belong to the Alibaba Cloud account in Apsara Stack Security Center. This way, you can use features in a hybrid cloud. This topic describes how to add an Alibaba Cloud account to Apsara Stack Security Center.

**Procedure**

To use features in a hybrid cloud, you can add an Alibaba Cloud account to Apsara Stack Security Center.
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the Apsara Uni-manager Management Console, choose
**Security** > **Global Platform Security > System Configurations**. On the **System**
**Configurations** page, select a region from the **Region** drop-down list and click **Access**
**with Authorized Role**.
3. In the left-side navigation pane, click **Accounts**.
4. On the **Alibaba Cloud Account** tab, click **Add**.
i.

| Parameter | Description |
|---|---|
| Access Key | The AccessKey ID of the Alibaba Cloud account that you want to add. |
| Access Secret | The AccessKey secret of the Alibaba Cloud account. |
| Alibaba Cloud Service | The Alibaba Cloud services that you want to use. Valid values:A nti- DDoS Pro and Anti-DDoS Premium IP and Web Application Protection. You can select one value or both. |

After the Alibaba Cloud account is added, you can view the account in the account list. You can **modify** or **remove** the account.
